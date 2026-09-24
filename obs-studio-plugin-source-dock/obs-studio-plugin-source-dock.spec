%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname obs-source-dock
%global commit b78fe9ea7649ece2984bc89432f71ca5f06322d4
%global date 20260511

Name:           obs-studio-plugin-source-dock
Version:        0.5.1^%{date}.%(c=%{commit}; echo ${c:0:7})
Release:        1%{?dist}
Summary:        Plugin for OBS Studio to add docks for any source

License:        GPL-2.0-or-later
URL:            https://github.com/exeldro/obs-source-dock
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

BuildRequires:  qt6-qtbase-private-devel

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
A Plugin for OBS Studio allowing you to create a Dock for a source, which lets
you interact, see audio levels, change volume and control media.


%prep
%autosetup -n %{srcname}-%{commit} -p1


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
* Thu Sep 24 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.5.1^20260511.b78fe9e-1
- new version
  - update to git snapshot for post-release commit fixing a dockstate issue
- removed CMakeLists.txt modification

* Wed Sep 02 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.5.0-3
- rebuilt

* Sun Jul 05 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.5.0-2
- rebuilt

* Mon Feb 02 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.5.0-1
- initial packaging
