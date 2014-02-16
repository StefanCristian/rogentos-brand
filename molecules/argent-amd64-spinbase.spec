# Use abs path, otherwise daily builds automagic won't work
%env %import ${ROGENTOS_MOLECULE_HOME:-/argent}/molecules/spinbase.common
%env %import ${ROGENTOS_MOLECULE_HOME:-/argent}/molecules/amd64.common

# Release Version
# Keep this here, otherwise daily builds automagic won't work
release_version: 2

# Release Version string description
release_desc: amd64 SpinBase

# Source chroot directory, where files are pulled from
%env source_chroot: ${ROGENTOS_MOLECULE_HOME:-/argent}/sources/amd64

# Destination ISO image name, call whatever you want.iso, not mandatory
# Keep this here and set, otherwise daily builds automagic won't work
%env destination_iso_image_name: Argent_Linux_2_amd64_SpinBase.iso