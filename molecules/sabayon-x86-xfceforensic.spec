# Use abs path, otherwise daily builds automagic won't work
%env %import ${SABAYON_MOLECULE_HOME:-/kogaion}/molecules/forensicxfce.common
%env %import ${SABAYON_MOLECULE_HOME:-/kogaion}/molecules/x86.common

prechroot: linux32

# Release Version
%env release_version: ${SABAYON_RELEASE:-11}

# Release Version string description
release_desc: x86 ForensicsXfce

# Path to source ISO file (MANDATORY)
%env source_iso: ${SABAYON_MOLECULE_HOME:-/kogaion}/iso/Sabayon_Linux_${ISO_TAG:-DAILY}_x86_Xfce.iso

destination_iso_image_name: Sabayon_Linux_DAILY_x86_ForensicsXfce.iso
