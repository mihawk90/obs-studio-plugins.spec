# Disable debug subpackages because we don't upload them anyway
%bcond debug 0

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-text-pango
%global commit 47d3139de004e29611d6db847b331ab95da40ea0
%global date 20250316

Name:           obs-studio-plugin-text-pango
Version:        1.0^%{date}.%(c=%{commit}; echo ${c:0:7})
Release:        1%{?dist}
Summary:        OBS plugin for Pango-based text source

License:        GPL-2.0-or-later
URL:            https://github.com/kkartaltepe/obs-text-pango
Source0:        %{url}/archive/%{commit}.tar.gz
Patch1:         fix-header-include.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

BuildRequires:  pkgconfig(pango)

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
This plugin provides a text source for OBS Studio. The text is layed out and rendered using Pango.


%prep
%autosetup -n %{srcname}-%{commit} -p1


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
* Thu Mar 27 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.0^20250316.47d3139-1
- Update to latest commit

* Fri Jan 31 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.0^20250131.bc9af01-1
- initial packaging
- includes a patch to avoid SIG_TRAP on OBS 31+
