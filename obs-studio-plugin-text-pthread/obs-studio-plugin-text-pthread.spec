%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-text-pthread

Name:           obs-studio-plugin-text-pthread
Version:        2.1.0
Release:        2%{?dist}
Summary:        OBS plugin for Pango-based text source

License:        GPL-2.0-or-later
URL:            https://github.com/norihiro/obs-text-pthread
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++

BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(pango)

# For directory ownership
Requires:       obs-studio%{?_isa}

Enhances:       obs-studio%{?_isa}


%description
This plugin provides a text source for OBS Studio. The text is layed out and rendered using Pango.

%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%{cmake} -DLINUX_PORTABLE=OFF -DLINUX_RPATH=OFF
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license LICENSE
%{_libdir}/obs-plugins/*
%{_datadir}/obs/obs-plugins/*


%changelog
* Tue Dec 02 2025 Tarulia <mihawk.90+git@googlemail.com> - 2.1.0-2
- Enable `debuginfo` subpackage

* Sat Nov 08 2025 Tarulia <mihawk.90+git@googlemail.com> - 2.1.0-1
- new version

* Fri Aug 29 2025 Tarulia <mihawk.90+git@googlemail.com> - 2.0.7-1
- new version

* Sat Aug 23 2025 Tarulia <mihawk.90+git@googlemail.com> - 2.0.6-1
- new version

* Fri Jan 31 2025 Tarulia <mihawk.90+git@googlemail.com> - 2.0.5-1
- initial packaging
