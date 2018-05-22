Deluge Client
=============
.. image:: https://travis-ci.org/JohnDoee/deluge-client.svg
    :target: https://travis-ci.org/JohnDoee/deluge-client

.. image:: https://ci.appveyor.com/api/projects/status/8s3g4uucg2xcay6v/branch/develop?svg=true
    :target: https://ci.appveyor.com/project/AndersJensen/deluge-client

A lightweight pure-python rpc client for deluge.
Note, does not support events and any additional replies from deluge will mess up the datastream.

Requirements
------------

- Deluge 1.3.x, 2.0 beta
- Python 2.7, 3.4, 3.5, 3.6

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
    >>> client.core.get_torrents_status({}, ['name'])
    {'79816060ea56d56f2a2148cd45705511079f9bca': {'name': 'TPB.AFK.2013.720p.h264-SimonKlose'}}


Idiom to use for automatic reconnect where the daemon might be offline at call time.
::

    import time

    from deluge_client import DelugeRPCClient, FailedToReconnectException

    def call_retry(client, method, *args, **kwargs):
        # We will only try the command 10 times
        for _ in range(10):
            try:
                return client.call(method, *args, **kwargs)
            except FailedToReconnectException:
                # 5 second delay between calls
                time.sleep(5)

Idiom usage
::

    client = DelugeRPCClient('127.0.0.1', 58846, 'username', 'password', automatic_reconnect=True)
    # The client has to be online when you start the process,
    # otherwise you must handle that yourself.
    client.connect()
    call_retry(client, 'core.get_torrents_status', {}, ['name'])

License
-------

MIT, see LICENSE
