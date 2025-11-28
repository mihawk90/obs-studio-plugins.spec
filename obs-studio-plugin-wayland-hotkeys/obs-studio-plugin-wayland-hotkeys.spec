# Disable debug subpackages because we don't upload them anyway
%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-wayland-hotkeys

Name:           obs-studio-plugin-wayland-hotkeys
Version:        1.1.0
Release:        1%{?dist}
Summary:        OBS Studio plugin for Wayland shortcuts

License:        GPL-2.0-or-later
URL:            https://github.com/leia-uwu/obs-wayland-hotkeys
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

BuildRequires:  qt6-qtwayland-devel >= 6.9
BuildRequires:  qt6-qtbase-private-devel >= 6.9

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
An OBS Studio plugin to integrate OBS hotkeys with the wayland global shortcuts portal


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


%changelog
* Fri Nov 28 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.1.0-1
- new version

* Tue Nov 04 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.0.0-1
- initial packaging
