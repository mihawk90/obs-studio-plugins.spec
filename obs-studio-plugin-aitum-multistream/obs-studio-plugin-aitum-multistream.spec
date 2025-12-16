%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-aitum-multistream

Name:           obs-studio-plugin-aitum-multistream
Version:        1.0.7
Release:        1%{?dist}
Summary:        OBS Studio plugin to stream to multiple services

License:        GPL-2.0-or-later
URL:            https://github.com/Aitum/obs-aitum-multistream
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

BuildRequires:  qt6-qtbase-devel
BuildRequires:  libcurl-devel

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
The Aitum Multistream Plugin for OBS Studio lets you go live on as many
platforms as possible, completely free.

Stop paying for expensive Multistreaming services and make the full use of your
internet bandwidth.

Aitum Multistream guides you through getting set up.
You shouldn't need to be a stream professor to get started.

Also supports the Aitum Vertical Canvas plugin.


%prep
%autosetup -n %{srcname}-%{version} -p1

# CMake Error at cmake/common/helpers_common.cmake:89 (set_property):
#   set_property can not be used on an ALIAS target.
# fix derived from NicolaiVdS' obs-plugin-aitum-multistream-git AUR
# just way shorter for the same effect (i.e. comment the line)
sed -i '89 s/^/#/' cmake/common/helpers_common.cmake


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
* Tue Dec 16 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.0.7-1
- initial packaging
