import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_datadog_package_installed(host):
    pip_packages = host.pip_package.get_packages()
    assert 'datadog' in pip_packages


def test_disk_usage_cron_script_exists(host):
    f = host.file('/etc/cron.d/datadog-docker-disk-usage')
    assert f.exists


def test_docker_config_for_datadog_exists(host):
    f = host.file('/etc/datadog-agent/conf.d/docker.d/conf.yaml')
    assert f.exists


def test_datadog_jmx_config_file_exists(host):
    f = host.file('/etc/datadog-agent/conf.d/jmx.d/conf.yaml')
    assert f.exists


def test_datadog_docker_image_exists(host):
    output = host.check_output('docker images datadog/agent -q | wc -l')
    assert '1' in output
