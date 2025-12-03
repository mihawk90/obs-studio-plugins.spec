%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname media-playlist-source

Name:           obs-studio-plugin-media-playlist-source
Version:        0.1.3
Release:        2%{?dist}
Summary:        Media Playlist Source plugin for OBS Studio

License:        GPL-2.0-or-later
URL:            https://github.com/CodeYan01/media-playlist-source
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}-source.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
An OBS Studio plugin that supports media playlists serving as an alternative to
the VLC source. It is based on the the builtin Media Source.


%prep
%autosetup -n %{srcname}-%{version}-source -p1


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
* Tue Dec 02 2025 Tarulia <mihawk.90+git@googlemail.com> - 0.1.3-2
- Enable `debuginfo` subpackage

* Sun Aug 10 2025 Tarulia <mihawk.90+git@googlemail.com> - 0.1.3-1
- initial packaging
