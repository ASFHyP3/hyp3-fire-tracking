"""fire-tracking processing."""

import logging
from pathlib import Path


log = logging.getLogger(__name__)


def download_bucket(input_bucket: str, input_prefix: str):
    """Download netcdf files from s3 bucket.

    Args:
        input_bucket: Input bucket
        input_prefix: Input prefix
    """


def process_fire_tracking(input_bucket: str, input_prefix: str) -> Path:
    """Draw fire polygon from fire detections.

    Args:
        input_bucket: Input bucket
        input_prefix: Input prefix
    """
    log.debug(f'Drawing...')
    product_file = Path('greeting.txt')
    product_file.write_text(greeting)
    return product_file
