# Disable debug subpackages because we don't upload them anyway
%bcond debug 0

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-text-pango
%global commit bc9af01217ad9baa0bdb17ecec1f15424fbdc4f8
%global date 20250131

# as of now this produces an incorrect version
%global forgeurl https://github.com/kkartaltepe/obs-text-pango
#Version:        1.0
# forgemeta -iv

Name:           obs-studio-plugin-text-pango
Version:        1.0^%{date}.%(c=%{commit}; echo ${c:0:7})
Release:        1%{?dist}
Summary:        OBS plugin for Pango-based text source

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{url}/archive/%{commit}.tar.gz
Patch1:         31.patch

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
%autosetup -n %{srcname}-%{commit} -p1
# can't use this without forgemeta
# forgeautosetup -p1


%build
%cmake \
	-DOBS_INCLUDE_DIRS="/usr/include/obs" \
	-DCMAKE_INSTALL_PREFIX="%{_tmppath}/obs-pango"
%cmake_build


%install
%cmake_install
# project's build system is not built for system-wide installs so we move the files manually
mkdir -p %{buildroot}%{_libdir}/obs-plugins
mv %{buildroot}%{_tmppath}/obs-pango/bin/libtext-pango.so %{buildroot}%{_libdir}/obs-plugins
mkdir -p %{buildroot}%{_datadir}/obs/obs-plugins/text-pango
mv -T %{buildroot}%{_tmppath}/obs-pango/data/ %{buildroot}%{_datadir}/obs/obs-plugins/text-pango/


%files
%doc README.md
%license COPYING
%{_libdir}/obs-plugins/*
%{_datadir}/obs/obs-plugins/*


%changelog
* Fri Jan 31 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.0^20250131.bc9af01-1
- initial packaging
- includes a patch to avoid SIG_TRAP on OBS 31+
