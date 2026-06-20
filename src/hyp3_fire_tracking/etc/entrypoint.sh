#!/bin/bash --login
set -e
conda activate hyp3-fire-tracking
exec python -um hyp3_fire_tracking "$@"
