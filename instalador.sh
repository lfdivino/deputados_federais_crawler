#!/usr/bin/env bash
set -e -x
virtualenv -p python3 . --system-site-packages --no-setuptools
bin/python <(curl https://bootstrap.pypa.io/get-pip.py) --upgrade setuptools==33.1.1 zc.buildout
bin/pip install -r requirements.txt
bin/pip install .