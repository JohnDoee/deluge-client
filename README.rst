Deluge Client
=============
.. image:: https://github.com/JohnDoee/deluge-client/actions/workflows/main.yml/badge.svg?branch=develop

A lightweight pure-python rpc client for deluge.
Note, does not support events and any additional replies from deluge will mess up the datastream.

Requirements
------------

- Deluge 1.3.x, 2.0, 2.1
- Python 3.8, 3.9, 3.10, 3.11, 3.12

Install
-------

From GitHub (develop):

.. code-block:: bash

    pip install git+https://github.com/JohnDoee/deluge-client.git#develop

From PyPi (stable):

.. code-block:: bash

    pip install deluge-client

Usage
-----

.. code-block:: python

    >>> from deluge_client import DelugeRPCClient

    >>> client = DelugeRPCClient('127.0.0.1', 12345, 'username', 'password')
    >>> client.connect()
    >>> client.connected
    True
    >>> client.call('core.get_torrents_status', {}, ['name'])
    {'79816060ea56d56f2a2148cd45705511079f9bca': {'name': 'TPB.AFK.2013.720p.h264-SimonKlose'}}
    >>> client.core.get_torrents_status({}, ['name'])
    {'79816060ea56d56f2a2148cd45705511079f9bca': {'name': 'TPB.AFK.2013.720p.h264-SimonKlose'}}

It is also usable as a context manager.

.. code-block:: python

    >>> from deluge_client import DelugeRPCClient

    >>> with DelugeRPCClient('127.0.0.1', 12345, 'username', 'password') as client:
    ...     client.call('core.get_torrents_status', {}, ['name'])
    {'79816060ea56d56f2a2148cd45705511079f9bca': {'name': 'TPB.AFK.2013.720p.h264-SimonKlose'}}


Idiom to use for automatic reconnect where the daemon might be offline at call time.

.. code-block:: python

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

.. code-block:: python

    client = DelugeRPCClient('127.0.0.1', 58846, 'username', 'password', automatic_reconnect=True)
    # The client has to be online when you start the process,
    # otherwise you must handle that yourself.
    client.connect()
    call_retry(client, 'core.get_torrents_status', {}, ['name'])
    # or if you have local Deluge instance, you can use the local client
    # LocalDelugeRPCClient accepts the same parameters, but username and password can be omitted
    from deluge_client import LocalDelugeRPCClient
    localclient = LocalDelugeRPCClient()
    localclient.connect()

Examples
--------

There's an example of how you might use this client in the `examples </examples>`_ directory


List of Deluge RPC commands
---------------------------

Sadly, this part isn't well documented. Your best bet is to check out the source code and try to figure
out what you need. The commands are namespaced so the commands you mostly need, core commands, are prefixed
with a :code:`core.` - Check out `this search <https://github.com/deluge-torrent/deluge/search?l=Python&q=%22%40export%22>`_ for all commands
and `core.py <https://github.com/deluge-torrent/deluge/blob/develop/deluge/core/core.py>`_ for core commands.

The exported commands are decorated with :code:`@export`.

You can also get a list of exported commands by calling the :code:`daemon.get_method_list` method:

.. code-block:: python

    client.call('daemon.get_method_list')
    # or
    client.daemon.get_method_list()

License
-------

MIT, see LICENSE
