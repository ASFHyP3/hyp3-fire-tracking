"""fire-tracking processing."""

import datetime as dt
import logging
import os
import shutil
from pathlib import Path

import boto3
import botocore
from tqdm.auto import tqdm

from hyp3_fire_tracking import utils


log = logging.getLogger(__name__)


def get_sat(suffix: str) -> str:
    """Get the VIIRS satellite from suffix.

    Args:
        suffix: Bucket with fire detection text files.

    Returns:
        sat: corresponding satellite
    """
    if suffix == 'j01':
        return 'n20'
    elif suffix == 'j02':
        return 'n21'
    elif suffix == 'npp':
        return suffix
    else:
        raise ValueError(f'Cannot recognize suffix {suffix}')


def download_data(input_bucket: str, input_prefix: str, output: str = 'output') -> None:
    """Download files from s3 bucket and make folder structure.

    Args:
        input_bucket: Bucket with fire detection text files.
        input_prefix: Prefix with fire detection text files.
        output: File path for the output product.
    """
    s3 = boto3.resource('s3', config=boto3.session.Config(signature_version=botocore.UNSIGNED))
    buck = s3.Bucket(input_bucket)
    for s3_object in tqdm(buck.objects.filter(Prefix=f'{input_prefix}')):
        path, filename = os.path.split(s3_object.key)
        if '_' in filename:
            suffix = filename.split('_')[1]
            sat = get_sat(suffix)
            start = dt.datetime.strptime('_'.join([filename.split('_')[2], filename.split('_')[3]]), 'd%Y%m%d_t%H%M%S%f')
            end = dt.datetime.strptime('_'.join([filename.split('_')[2], filename.split('_')[4]]), 'd%Y%m%d_e%H%M%S%f')
            sstart = start.strftime('%Y%m%d%H%M%S%f')
            send = end.strftime('%Y%m%d%H%M%S%f')
            corr = filename.split('_')[6][0:16]
            newfilename = f'EFIRE_VIIRSI_v1r3_{sat}_s{sstart}_e{send}_c{corr}.nc'
            folder = Path(start.strftime(f'{output}/staging/incoming/pass_{sat}_%Y%m%dT%H%M'))
            folder.mkdir(parents=True, exist_ok=True)
            buck.download_file(s3_object.key, f'{str(folder)}/{newfilename}')
            ready = Path(f'{str(folder)}/READY.flag')
            ready.touch()


def process_fire_tracking(
    input_bucket: str,
    input_prefix: str,
    work_dir: Path | None = None,
) -> Path:
    """Draw fire polygon from fire detections.

    Args:
        input_bucket: Input bucket
        input_prefix: Input prefix
        work_dir: File path for the output product
    """
    if work_dir is None:
        work_dir = Path('output')
    work_dir.mkdir(parents=True, exist_ok=True)
    log.debug('Downloading...')
    download_data(input_bucket, input_prefix, output=str(work_dir))
    log.debug('Drawing polygon')
    utils.call_fire_module('run_algorithm_watcher.py', args=['orchestration.watch_one_shot=true'], work_dir=work_dir)
    product_file = shutil.make_archive('output', 'zip', str(work_dir))
    return Path(product_file)
