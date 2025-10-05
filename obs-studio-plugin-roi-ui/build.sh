#!/bin/sh

### preparation

spec=$(echo *.spec)

if [ "$1" == "frel" ] && [ "$2" != "" ]; then
	frel=$2
	echo "Fedora Release version specified. Using $frel."
else
	frel=$(rpm -E %fedora)
	echo "No Fedora Release version specified. Using default $frel."
fi;

if [ "$1" == "all" ]; then
	echo "Building for Fedora Release $(($frel - 1)), $frel, and $(($frel + 1))."
	./build.sh frel $(($frel - 1))
	./build.sh frel $(($frel + 1))
	./build.sh $2
	exit
fi;

set -x
### build phase
rm ./f_downloads/*
# && so this fails early when the download fails
# instead of going through mock setup just to fail halfway
spectool -g $spec --directory ./f_downloads && \
cp *.patch ./f_downloads
rm -rf ./f_upload/$frel/
mock -r fedora-$frel-x86_64-rpmfusion_free --sources=./f_downloads --spec=$spec --resultdir=./f_upload/$frel/

pushd ./f_upload/$frel && \
rpm=$(echo obs-studio-plugin-*.fc$frel.x86_64.rpm) && \
sha512sum $rpm > ${rpm%.x86_64.rpm}.sha512 && \
\
if [ "$1" == "install" ]; then
	sudo dnf install $rpm
fi

popd

echo "All done!"

