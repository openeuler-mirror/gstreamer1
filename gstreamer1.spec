Name:           gstreamer1
Version:        1.16.2
Release:        1
Summary:        Bindings for GStreamer 1.0, the open source multimedia framework

License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz
# Source1 and Source2 are from fedora 29
Source1:        gstreamer1.attr
Source2:        gstreamer1.prov

Patch0001:      Adapt-to-backwards-incompatible-change-in-GUN.patch

BuildRequires:  automake bison check-devel chrpath docbook-style-dsssl docbook-style-xsl
BuildRequires:  docbook-utils flex gettext gettext-devel ghostscript glib2-devel >= 2.32.0 transfig
BuildRequires:  gobject-introspection-devel >= 1.31.1 gtk-doc >= 1.3 libtool libxslt m4 texlive-jadetex
BuildRequires:  libxml2-devel >= 2.4.0 netpbm-progs openjade pkgconfig python3 texlive-dvips

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
NOCONFIGURE=1 ./autogen.sh
%configure --enable-gtk-doc --enable-debug --disable-fatal-warnings --disable-silent-rules \
           --disable-tests --disable-examples
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
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
%{_datadir}/gtk-doc/html/gstreamer-1.0/*
%{_datadir}/gtk-doc/html/gstreamer-libs-1.0/*
%{_datadir}/gtk-doc/html/gstreamer-plugins-1.0/*
%{_mandir}/man1/*.gz

%changelog
* Tue Aug 18 2020 jinzhimin <jinzhimin2@huawei.com> - 1.16.2-1
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

