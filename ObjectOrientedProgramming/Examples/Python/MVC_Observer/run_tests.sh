#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./run_tests.sh
Runs tests with coverage. Make sure test plugin is installed: pip install pytest-cov
'
    exit
fi
cd "$(dirname "$0")"

python -m coverage run --source=. -m unittest;
python -m coverage report;
python -m coverage html;