import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vim_package_exist(host):
    assert host.package('vim').is_installed


def test_symlink_created(host):
    f = host.file('/home/jerry/.vimrc')
    assert f.linked_to == '/home/jerry/.vim/vimrc'
