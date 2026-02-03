#!/bin/bash

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
spectool -g $spec --directory ./f_downloads
cp *.patch ./f_downloads
rm -rf ./f_upload/$frel/
if [ "$1" == "epel" ]; then
	mock -r epel-9-x86_64 \
		--sources=./f_downloads \
		--spec=$spec \
		--resultdir=./f_upload/$frel/ \
		--rootdir=$(pwd)/../mock_root/
else
	mock -r fedora-$frel-x86_64-rpmfusion_free \
		--sources=./f_downloads \
		--spec=$spec \
		--resultdir=./f_upload/$frel/ \
		--rootdir=$(pwd)/../mock_root/

	pushd ./f_upload/$frel && \
	rpm=$(ls  -1 obs-studio-plugin-*.fc$frel.x86_64.rpm | grep -vE "debug(info|source)") && \
	rpmlint $rpm 2>&1 | tee rpmlint.txt && \
	\
	if [ "$1" == "install" ]; then
		sudo dnf install $rpm
	fi

	popd
fi

echo "All done!"
