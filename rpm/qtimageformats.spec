%global qt_module qtimageformats
%global qt_version 5.15.8

Summary: Qt5 - QtImageFormats component
Name:    opt-qt5-%{qt_module}
Version: 5.15.8
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: %{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: opt-qt5-qtbase-devel >= %{qt_version}
BuildRequires: opt-qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

BuildRequires: libmng-devel
BuildRequires: libtiff-devel
BuildRequires: jasper-devel
BuildRequires: libwebp-devel >= 0.4.4

# prior -devel subpkg contained only runtime cmake bits
Provides:  opt-qt5-qtimageformats-devel = %{version}-%{release}

# filter plugin provides
%global __provides_exclude_from ^%{_opt_qt5_plugindir}/.*\\.so$

%description
The core Qt Gui library by default supports reading and writing image
files of the most common file formats: PNG, JPEG, BMP, GIF and a few more,
ref. Reading and Writing Image Files. The Qt Image Formats add-on module
provides optional support for other image file formats, including:
MNG, TGA, TIFF, WBMP.

%prep
%autosetup -n %{name}-%{version}/upstream

rm -rv src/3rdparty


%build
%{opt_qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}


%files
%license LICENSE.GPL*
%license LICENSE.LGPL*
%{_opt_qt5_plugindir}/imageformats/libqmng.so
%{_opt_qt5_plugindir}/imageformats/libqtga.so
%{_opt_qt5_plugindir}/imageformats/libqtiff.so
%{_opt_qt5_plugindir}/imageformats/libqwbmp.so
%{_opt_qt5_plugindir}/imageformats/libqicns.so
%{_opt_qt5_plugindir}/imageformats/libqjp2.so
%{_opt_qt5_plugindir}/imageformats/libqwebp.so
%{_opt_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_*Plugin.cmake
