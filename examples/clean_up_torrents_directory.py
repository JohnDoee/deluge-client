#!/bin/env python3

from deluge_client import DelugeRPCClient
import os, shutil

deluge_host="172.18.0.9"
deluge_port=58765
deluge_username="localclient"
deluge_password="01a23b45c67d89e01f23a45b67c89d01e23f4567"
cleanup_path="/downloads/tv"

client = DelugeRPCClient(deluge_host, deluge_port, deluge_username, deluge_password)
client.connect()

dir_list = os.listdir(cleanup_path)
print(f"{len(dir_list)} items in {cleanup_path} before clean-up.")

# Get a list of torrents, containing 'name' and 'download_location' only
torrents_list = client.core.get_torrents_status({}, ['name', 'download_location'])

# This is the data structure in torrents_list:
'''
>>> print(list(torrents.items())[0])
(b'9876543210987654321098765432109876543210', {b'download_location': b'/downloads/tv', b'name': b'My.TV.Show.S02E06.1080p.WEB.h264-SUPER'})
'''
for id, data in torrents_list.items():
    for key, val in data.items():
        if key.decode() == "name":
            if val.decode() in dir_list:
                dir_list.remove(val.decode())

print(f"{len(dir_list)} items in {cleanup_path} after clean-up.")

for entry in dir_list:
    print(f"Deleting: {cleanup_path}/{entry}")
    shutil.rmtree(f"{cleanup_path}/{entry}")
