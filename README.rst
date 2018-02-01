Deluge Client
=============

A lightweight pure-python rpc client for deluge.
Note, does not support events and any additional replies from deluge will mess up the datastream.

Requirements
------------

- Deluge 1.3.x, 2.0 beta
- Python 2.6, 2.7, 3.3, 3.4, 3.5

Install
-------

From GitHub (develop):
::

    pip install git+https://github.com/JohnDoee/deluge-client.git#develop

From PyPi (stable):
::

    pip install deluge-client

Usage
-----
::

    >>> from deluge_client import DelugeRPCClient

    >>> client = DelugeRPCClient('127.0.0.1', 12345, 'username', 'password')
    >>> client.connect()
    >>> client.connected
    True
    >>> client.call('core.get_torrents_status', {}, ['name'])
    {'79816060ea56d56f2a2148cd45705511079f9bca': {'name': 'TPB.AFK.2013.720p.h264-SimonKlose'}}

License
-------

MIT, see LICENSE
