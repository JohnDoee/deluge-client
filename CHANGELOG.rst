================================
Changelog
================================

Version 1.10.2 (17-02-2024)
--------------------------------

* Bugfix: Auto publish to pypi code

Version 1.10.1 (17-02-2024)
--------------------------------

* Added: Configurable timeout support #42

* Bugfix: Bug related to hanging sockets #42
* Bugfix: Trying to fix cipher issues with ssl socket #44
* Bugfix: Issue with how the new ssl context is used after merging #45

Version 1.10.0 (15-02-2024)
--------------------------------

* Added: Python 3.12 support

* Removed: Old and EOLed python version support

Version 1.9.0 (16-05-2020)
--------------------------------

* Added: Changelog
* Added: Auto configuring local client for local auth (thanks int3l)

* Change: Removed Python 3.4 support and added Python 3.7 support.
  Probably still works in 3.4.

* Bugfix: Context manager returning correct instance now (thanks int3l)