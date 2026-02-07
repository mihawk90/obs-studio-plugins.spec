%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname tuna

Name:           obs-studio-plugin-tuna
Version:        1.9.11
Release:        2%{?dist}
Summary:        Song information plugin for obs-studio

License:        GPL-2.0-or-later
URL:            https://github.com/univrsal/tuna
Source0:        %{url}/archive/v%{version}.tar.gz
Source101:      FindLibMPDClient.cmake.patch
Source102:      FindTaglib.cmake.patch
Source103:      deps_CMakeLists.txt.patch

Patch101:       240.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconfig(libobs)

BuildRequires:  curl-devel
BuildRequires:  dbus-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  taglib-devel
BuildRequires:  zlib-ng-compat-devel

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}


%description
Get song info from right within OBS Studio.

Currently supports MPD, Any Window title, OBS VLC source, YouTube Music, and
most music players through MPRIS. Also supports various websites from any
browser through a Tampermonkey script, including Soundcloud, Spotify Web Player,
Deezer, Yandex Music, and Pretzel.rocks.

Lyrics for the lyrics html overlay are served via developer's lrclib instance.

Note: Spotify and last.fm integrations are not available because they require
private API keys. This is a packaging limitation. Do not report this as a bug to
the plugin author.


%prep
%autosetup -n %{srcname}-%{version} -p1

# straight from tytan's AUR package
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=obs-tuna&id=ae9ddb2912af9373cbbd7833cf5329743320fdd6

cp %{SOURCE101} cmake/external/FindLibMPDClient.cmake
cp %{SOURCE102} cmake/external/FindTaglib.cmake
cp %{SOURCE103} deps/CMakeLists.txt

sed -i '28 a find_package(LibMPDClient REQUIRED)\nfind_package(Taglib REQUIRED)' CMakeLists.txt


%build
# Don't have Spotify/Last.fm API keys but there is no disable option
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
    -DCREDS="MISSING" \
    -DLASTFM_CREDS="MISSING"
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license LICENSE
%{_libdir}/obs-plugins/*
%{_datadir}/obs/obs-plugins/*


%changelog
* Sat Feb 07 2026 Tarulia <mihawk.90+git@googlemail.com> - 1.9.11-2
- add patch for deprecated taglib usage

* Fri Jan 30 2026 Tarulia <mihawk.90+git@googlemail.com> - 1.9.11-1
- initial packaging
