#!/usr/bin/env python

import os
import subprocess

from datadog import initialize, statsd

options = {
    'api_key': os.environ['DATADOG_API_KEY'],
}

initialize(**options)

df = subprocess.Popen(
    ["df", "--output=pcent", "/var/lib/docker"],
    stdout=subprocess.PIPE
)

data_percent = subprocess.check_output(
    ["tail", "-n", "1"], stdin=df.stdout
).decode("utf-8").replace("%", "").strip()
df.wait()

statsd.gauge('mmdocker.thinpool.data.in_use', float(data_percent))
