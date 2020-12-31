#!/bin/bash

python preprocess.py

datasette serve data.db -m metadata.json --port 8080 --host 0.0.0.0
