%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname advanced-scene-switcher

Name:           obs-studio-plugin-%{srcname}
Version:        1.32.7
Release:        1%{?dist}
Summary:        An automation plugin for OBS Studio

License:        GPL-2.0-or-later
URL:            https://github.com/WarmUpTill/SceneSwitcher
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}-source.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
# release notes say
# > minimum supported OBS version is OBS 31.1.1
# however it builds fine on EPEL's 30.0
BuildRequires:  pkgconfig(libobs)

BuildRequires:  alsa-lib-devel
BuildRequires:  asio-devel
BuildRequires:  json-devel
BuildRequires:  libcurl-devel
BuildRequires:  libusb1-devel
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXtst-devel
BuildRequires:  opencv-devel
BuildRequires:  procps-ng-devel
BuildRequires:  qt6-qtbase-devel

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
This plugin provides various automation tools for OBS Studio.

It provides the ability to execute various actions depending on the
current state of OBS Studio in an if-this-then-that (IFTTT) approach.


%prep
%autosetup -n %{srcname}-%{version}-source -p1


%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
    -DDISABLE_TWITCH_TIMESTAMP_VERIFICATION=ON
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license LICENSE
%{_libdir}/obs-plugins/*
%{_datadir}/obs/obs-plugins/*


%changelog
* Mon Feb 09 2026 Tarulia <mihawk.90+git@googlemail.com> - 1.32.7-1
- new version

* Mon Feb 02 2026 Tarulia <mihawk.90+git@googlemail.com> - 1.32.6-2
- removed minimum version from Requires

* Sat Dec 27 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.32.6-1
- new version

* Sun Dec 14 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.32.5-1
- new version

* Sat Dec 06 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.32.4-1
- new version

* Tue Dec 02 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.32.3-2
- Add patch for PR#1494

* Fri Nov 14 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.32.3-1
- new version

* Sat Nov 1 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.32.2-1
- new version

* Wed Oct 29 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.32.1-1
- new version

* Wed Oct 29 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.32.0-1
- new version

* Thu Jul 17 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.31.0-1
- new version

* Sat Jul 05 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.30.2-2
- Add crashfix patch
- Re-enable debug packages

* Fri Jun 13 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.30.2-1
- new version

* Sun Jun 01 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.30.1-1
- new version
- timestamp verification patch removed

* Wed May 28 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.30.0-2
- adv-ss: Temporarily disable Twitch timestamp verification
  This fixes an issue with the Twitch plugin not loading and thereby
  deleting Twitch connections and related actions.

* Tue May 27 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.30.0-1
- new version

* Fri Apr 11 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.29.3-1
- new version

* Fri Apr 04 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.29.2-1
- new version
- re-enable alsa-lib-devel dependency for libremidi

* Tue Mar 25 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.29.1-1
- initial packaging
