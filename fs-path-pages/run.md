---
license: root directory descriptions based on: https://help.ubuntu.com/community/LinuxFilesystemTreeOverview originally created by contributors to the Ubuntu documentation wiki and the Filesystem Hierarchy Standard 2.3 created by Filesystem Hierarchy Standard Group.
path: /run
---

/run is a tmpfs (temporary file system) available early in the boot process where ephemeral run-time data is stored. Files under this directory are removed or truncated at the beginning of the boot process. (It deprecates various legacy locations such as /var/run, /var/lock, /lib/init/rw in otherwise non-ephemeral directory trees as well as /dev/.* and /dev/shm  which are not device files.)