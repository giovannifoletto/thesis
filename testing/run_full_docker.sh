#!/usr/bin/bash

# Runner for VictoriaDB

mkdir victoria-logs-data

podman run --rm -it -p 9428:9428 -v ./victoria-logs-data:/victoria-logs-data docker.io/victoriametrics/victoria-logs:v0.4.1-victorialogs
