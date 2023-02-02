# Mounting Volumes on Linux
- `sudo -s` to start, or append all with sudo
- `lsblk` to get volume name
- `mkfs -t xfs /dev/<volume-name>` to format the volume
- `mkdir /dir/to/mount/to` to have a directory to mount the volume to
- `mount /dev/<volume-name> /dir/to/mount/to` to mount the volume to the directory

## Creating fstab entry
- `sudo -s` still doing sudo stuff
- `cp /etc/fstab /etc/fstab.orig` to create a backup of the fstab
- `blkid` to get UUID of volume for use in fstab
- `vi /etc/fstab` and add `UUID=<string-from-previous-step> /dir/to/mount/to xfs defaults,nofail 0 2` at the bottom of the file (type `G` `o`in vi to go to the bottom and make a new line under the last line)
- `umount /dir/to/mount/to` then `mount -a` to test that the directory automatically mounts 