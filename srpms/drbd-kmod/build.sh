#!/bin/sh

set -e

rm -f *.tar.gz
# spectool on centos doesn´t like our spec file (works on fedora)
wget https://pkg.linbit.com//downloads/drbd/9/drbd-9.2.5.tar.gz
rpmbuild --define "_srcrpmdir $(pwd)" --define "_sourcedir $(pwd)" --nodeps -bs drbd-kmod.spec
rm -f *.tar.gz
