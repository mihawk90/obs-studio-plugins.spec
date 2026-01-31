%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-aitum-stream-suite

Name:           obs-studio-plugin-aitum-stream-suite
Version:        0.6.1
Release:        1%{?dist}
Summary:        OBS Studio plugin to manage multiple stream destinations

License:        GPL-2.0-or-later
URL:            https://aitum.tv/products/stream-suite
Source0:        https://github.com/Aitum/obs-aitum-stream-suite/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  libcurl-devel

Requires:       obs-studio%{?_isa} >= 32.0.0
Enhances:       obs-studio%{?_isa} >= 32.0.0

# this plugin contains both of these
Conflicts:      obs-studio-plugin-aitum-multistream
Conflicts:      obs-studio-plugin-aitum-vertical-canvas


%description
The Aitum Stream Suite plugin for OBS Studio includes both Aitum Multistream as
well as Aitum Vertical. It extends these with various management features such
as a multi chat, stream information, and activity feed docks to manage all setup
stream locations in one place.


%prep
%autosetup -n %{srcname}-%{version} -p1

sed -i '31 a find_package(Qt6GuiPrivate REQUIRED)' CMakeLists.txt


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
* Sat Jan 31 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.6.1-1
- initial packaging
