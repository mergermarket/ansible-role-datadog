#!/usr/bin/env python

import os
import subprocess

from datadog import initialize, statsd

options = {
    'api_key': os.environ['DATADOG_API_KEY'],
}

initialize(**options)

data_percent = subprocess.check_output(["lvs", "--no-headings", "-o", "data_percent"])
metadata_percent = subprocess.check_output(["lvs", "--no-headings", "-o", "metadata_percent"])

statsd.gauge('mmdocker.thinpool.data.in_use', float(data_percent))
statsd.gauge('mmdocker.thinpool.metadata.in_use', float(metadata_percent))
