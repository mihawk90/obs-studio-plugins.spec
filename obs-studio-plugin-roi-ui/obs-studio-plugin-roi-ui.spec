# Disable debug subpackages because we don't upload them anyway
%bcond debug 0

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-roi-ui

Name:           obs-studio-plugin-roi-ui
Version:        1.1.1
Release:        1%{?dist}
Summary:        OBS Studio plugin to edit Encoder ROI

License:        GPL-2.0-or-later
URL:            https://github.com/derrod/obs-roi-ui
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

BuildRequires:  ffmpeg-free-devel
BuildRequires:  qt6-qtbase-devel qt6-qtbase-private-devel

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
Encoder ROI - or Region of Interest - is a method to (de)prioritise certain
areas of a video frame sent to the encoder. This can be used for example to
enhance quality at the center of the screen for first person games, or the
part of the video where your camera is located.


%prep
%autosetup -n %{srcname}-%{version} -p1

# These are from tytan's AUR package:
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=obs-roi-ui

sed -i '33 a #include <obs-nix-platform.h>\n#include <qpa/qplatformnativeinterface.h>' src/external/qt-wrappers.cpp
sed -i 's/find_qt(/find_package(Qt6 /g' CMakeLists.txt
sed -i 's/Qt::Widgets/Qt::Widgets Qt::GuiPrivate/g' CMakeLists.txt

sed -i 's|obs_sceneitem_get_id(item)|QVariant::fromValue(obs_sceneitem_get_id(item))|g' src/roi-editor.cpp
sed -i 's|findData(data.scene_item_id)|findData(QVariant::fromValue(data.scene_item_id))|g' src/roi-editor.cpp
sed -i 's|1LL|1L|g' src/roi-editor.cpp

sed -i '12 a #include <thread>\n#include <condition_variable>' src/encoder-preview.hpp


%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license LICENSE
%{_libdir}/obs-plugins/*
%{_datadir}/obs/obs-plugins/*


%changelog
* Sun Oct 05 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.1.1-1
- initial packaging
