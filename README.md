# HyP3 fire-tracking

Plugin to draw fire polygon from fire detections

## Usage

The HyP3-fire-tracking plugin provides a workflow (accessible directly in Python or via a CLI) that can be used to draw fire perimeters from VIIRS fire detections.

The command line tool can be run using the following structure:
```bash
python -m hyp3_fire_tracking \
  --input-bucket bucket \
  --input-prefix prefix \
```
Where:

* `--input-bucket` is the bucket with the VIIRS fire detection netcdf files
* `--input-prefix` is the folder in the bucket with the netcdf files

### Credentials

Generally, credentials are provided via environment variables, but some may be provided by command-line arguments or via a `.netrc` file. 

#### AWS Credentials

You must provide AWS credentials because the data is hosted by USGS in a "requester pays" bucket. To provide AWS credentials, you can either use an AWS profile specified in your `~/.aws/credentials` by exporting:
```
export AWS_PROFILE=your-profile
```
or by exporting credential environment variables:
```
export AWS_ACCESS_KEY_ID=your-id
export AWS_SECRET_ACCESS_KEY=your-key
export AWS_SESSION_TOKEN=your-token  # optional; for when using temporary credentials
```

For more information, please see: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

## Developer Setup
1. Ensure that conda is installed on your system (we recommend using [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) to reduce setup times).
2. Download a local version of the `hyp3-fire-tracking` repository (`git clone https://github.com/ASFHyP3/hyp3-fire-tracking.git`)
3. In the base directory for this project call `mamba env create -f environment.yml` to create your Python environment, then activate it (`mamba activate hyp3-fire-tracking`)
4. Finally, install a development version of the package (`python -m pip install -e .`)

To run all commands in sequence use:
```bash
git clone https://github.com/ASFHyP3/hyp3-fire-tracking.git
cd hyp3-fire-tracking
mamba env create -f environment.yml
mamba activate hyp3-fire-tracking
python -m pip install -e .
```

## Contributing
Contributions to the HyP3 fire-tracking plugin are welcome! If you would like to contribute, please submit a pull request on the GitHub repository.

## Contact Us
Want to talk about HyP3 fire-tracking? We would love to hear from you!

Found a bug? Want to request a feature?
[open an issue](https://github.com/ASFHyP3/hyp3-fire-tracking/issues/new)
