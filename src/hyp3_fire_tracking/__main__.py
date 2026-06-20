"""fire-tracking processing for HyP3."""

import logging
from argparse import ArgumentParser

from hyp3lib.aws import upload_file_to_s3

from hyp3_fire_tracking.process import process_fire_tracking


def main() -> None:
    """HyP3 entrypoint for hyp3_fire_tracking."""
    parser = ArgumentParser()
    parser.add_argument('--bucket', help='AWS S3 bucket HyP3 for upload the final product(s)')
    parser.add_argument('--bucket-prefix', default='', help='Add a bucket prefix to product(s)')

    # TODO: Your arguments here
    parser.add_argument('--input-bucket', default='ak-fire-safe-data', help='Input bucket')
    parser.add_argument('--input-prefix', default='nc', help='Input prefix')

    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    product_file = process_fire_tracking(
        input_bucket=args.input_bucket,
        input_prefix=args.input_prefix,
    )

    if args.bucket:
        upload_file_to_s3(product_file, args.bucket, args.bucket_prefix)


if __name__ == '__main__':
    main()
