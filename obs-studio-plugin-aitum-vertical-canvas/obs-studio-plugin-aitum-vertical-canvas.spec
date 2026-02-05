%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-vertical-canvas

Name:           obs-studio-plugin-aitum-vertical-canvas
Version:        1.6.2
Release:        1%{?dist}
Summary:        OBS Studio plugin to render a secondary vertical canvas

License:        GPL-2.0-or-later
URL:            https://aitum.tv/products/vertical
Source0:        https://github.com/Aitum/obs-vertical-canvas/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs) >= 32.0.0

BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  libcurl-devel

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}

# stream-suite already contains this
Conflicts:      obs-studio-plugin-aitum-stream-suite


%description
The Aitum Vertical Plugin for OBS Studio makes it simple to create vertical
layouts of your existing OBS setup, ready to record or go live at the click
of a button.

Also supports the Aitum Multistream plugin.


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
* Thu Feb 05 2026 Tarulia <mihawk.90+git@googlemail.com> - 1.6.2-1
- new version

* Mon Feb 02 2026 Tarulia <mihawk.90+git@googlemail.com> - 1.6.1-3
- move minimum OBS version from Requires to BuildRequires

* Sat Jan 31 2026 Tarulia <mihawk.90+git@googlemail.com> - 1.6.1-2
- Use proper product URL
- Add Conflicts with stream-suite package
- Add specific OBS version requirement

* Tue Dec 16 2025 Tarulia <mihawk.90+git@googlemail.com> - 1.6.1-1
- initial packaging
