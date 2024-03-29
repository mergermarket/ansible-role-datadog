import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_datadog_package_installed(host):
    pip_packages = host.pip.get_packages()
    assert 'datadog' in pip_packages


def test_disk_usage_cron_script_exists(host):
    f = host.file('/etc/cron.d/datadog-docker-disk-usage')
    assert f.exists
