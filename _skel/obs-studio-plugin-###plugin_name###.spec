%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname ###src_tarball_root_without_version###

Name:           obs-studio-plugin-###plugin_name###
Version:        ###Version###
Release:        1%{?dist}
Summary:        ###Summary###

License:        GPL-2.0-or-later
URL:            ###URL###
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

###plugin_deps###

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
###Description###


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
* ###date### Tarulia <mihawk.90+git@googlemail.com> - ###Version-Release###
- initial packaging
