%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-pipewire-audio-capture

Name:           obs-studio-plugin-pipewire-audio-capture
Version:        1.2.1
Release:        1%{?dist}
Summary:        Audio device and application capture for OBS Studio

License:        GPL-2.0-or-later
URL:            https://github.com/dimtpap/obs-pipewire-audio-capture
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

BuildRequires:  pipewire-devel

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
This OBS Studio plugin adds three sources for capturing audio outputs,
inputs, and applications using PipeWire.


%prep
%autosetup -n %{srcname}-%{version} -p1


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
* Mon Dec 15 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.2.1-1
- initial packaging
