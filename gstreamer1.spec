Name:           gstreamer1
Version:        1.19.3
Release:        1
Summary:        Bindings for GStreamer 1.0, the open source multimedia framework

License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz
Source1:        gstreamer1.attr
Source2:        gstreamer1.prov

Patch0001:      gstreamer-inspect-rpm-format.patch

BuildRequires:  bison check-devel chrpath meson >= 0.59.0 gcc
BuildRequires:  flex gettext gettext-devel glib2-devel >= 2.32.0
BuildRequires:  gobject-introspection-devel >= 1.31.1 libtool
BuildRequires:  libxml2-devel >= 2.4.0 pkgconfig libcap-devel
BuildRequires:  libunwind-devel elfutils-devel bash-completion

%description
GStreamer1 implements a framework that allows for processing and encoding of
multimedia sources in a manner similar to a shell pipeline.

Because it's introspection-based, most of the classes follow directly from the
C API. Therefore, most of the documentation is by example rather than a full
breakdown of the class structure.

%package        devel
Summary:        Development files for GStreamer streaming media framework
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel libxml2-devel check-devel

%description    devel
The %{name}-devel package includes the libraries, header files, etc.,
that you'll need to develop applications that are linked with the
gstreamer1 extensibility library.


%package        help
Summary:        Documents for %{name}
Buildarch:      noarch
Requires:       man info %{name} = %{version}-%{release}
Provides:       %{name}-devel-docs

%description    help
Man pages and other related documents for %{name}.

%prep
%autosetup -n gstreamer-%{version} -p1

%build
%meson  \
  -D gtk_doc=disabled -D tests=disabled -D examples=disabled \
  -D ptp-helper-permissions=capabilities -D dbghelp=disabled \
  -D doc=disabled
%meson_build

%install
%meson_install
%find_lang gstreamer-1.0
%delete_la
install -m0644 -D %{SOURCE1} %{buildroot}%{_rpmconfigdir}/fileattrs/gstreamer1.attr
install -m0755 -D %{SOURCE2} %{buildroot}%{_rpmconfigdir}/gstreamer1.prov
%ldconfig_scriptlets

%files -f gstreamer-1.0.lang
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/gst-*-1.0
%{_rpmconfigdir}/gstreamer1.prov
%{_rpmconfigdir}/fileattrs/gstreamer1.attr
%{_libdir}/*.so.*
%{_libdir}/gstreamer-1.0/*.so
%{_libdir}/girepository-1.0/*.typelib
%{_libexecdir}/gstreamer-1.0/*

%{_datadir}/bash-completion/helpers/gst
%{_datadir}/bash-completion/completions/gst-*

%files devel
%{_datadir}/aclocal/gst-element-check-1.0.m4
%{_datadir}/gir-1.0/*.gir
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gstreamer-1.0/gst/*.h
%{_includedir}/gstreamer-1.0/gst/net/*.h
%{_includedir}/gstreamer-1.0/gst/controller/*.h
%{_includedir}/gstreamer-1.0/gst/check/*.h
%{_includedir}/gstreamer-1.0/gst/base/*.h

%{_datadir}/gstreamer-1.0/gdb/*
%{_datadir}/gdb/auto-load/*

%files help
%doc RELEASE README
%{_mandir}/man1/*.gz

%changelog
* Fri Dec 3 2021 hanhui <hanhui15@huawei.com> - 1.19.3-1
- Upgrade to gstreamer-1.19.3

* Wed Jun 23 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 1.18.4-1
- Upgrade to 1.18.4
- Delete Adapt-to-backwards-incompatible-change-in-GUN.patch whose target
  patch file doesn't exist in this version 1.18.4
- Add gstreamer-inspect-rpm-format.patch
- Use meson rebuild

* Wed Mar 3 2021 yanan <yanan@huawei.com> - 1.16.2-3
- remove buildrequires for gtk-doc

* Tue Aug 4 2020 wangye <wangye70@huawei.com> - 1.16.2-2
- fix 1.16.2 make error

* Sat Jul 25 2020 hanhui <hanhui15@huawei.com> - 1.16.2-1
- update 1.16.2

* Tue Jan 7 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.14.4-4
- update software package

* Sun Dec 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.14.4-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:optimization the spec

* Tue Aug 27 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.14.4-2
- Package Init

