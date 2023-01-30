#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./run_tests.sh
Runs tests with coverage
'
    exit
fi
cd "$(dirname "$0")"

python -m coverage run -m unittest; coverage report -m