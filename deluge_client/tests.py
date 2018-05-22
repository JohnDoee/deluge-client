import os
import sys

import pytest

from .client import DelugeRPCClient, RemoteException


if sys.version_info > (3,):
    long = int


@pytest.fixture
def client():
    if sys.platform.startswith('win'):
        auth_path = os.path.join(os.getenv('APPDATA'), 'deluge', 'auth')
    else:
        auth_path = os.path.expanduser("~/.config/deluge/auth")

    with open(auth_path, 'rb') as f:
        filedata = f.read().decode("utf-8").split('\n')[0].split(':')

    username, password = filedata[:2]
    ip = '127.0.0.1'
    port = 58846
    client = DelugeRPCClient(ip, port, username, password)
    client.connect()

    yield client

    try:
        client.disconnect()
    except:
        pass


def test_connect(client):
    assert client.connected


def test_call_method(client):
    assert isinstance(client.call('core.get_free_space'), (int, long))


def test_call_method_arguments(client):
    assert isinstance(client.call('core.get_free_space', '/'), (int, long))


def test_call_method_exception(client):
    with pytest.raises(RemoteException) as ex_info:
        client.call('core.get_free_space', '1', '2')
    assert 'takes at most 2 arguments' in str(ex_info.value)


def test_attr_caller(client):
    assert isinstance(client.core.get_free_space(), (int, long))
    assert isinstance(client.core.get_free_space('/'), (int, long))
