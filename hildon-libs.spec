#
# TODO: possible patch to GTK/wait for upstream to support tap and hold 
#
Summary:	Maemo hildon widgets library
Summary(pl.UTF-8):	Biblioteka widgetów hildon dla platformy Maemo
Name:		hildon-libs
Version:	0.14.11
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/%{name}_%{version}-1.tar.gz
# Source0-md5:	7e16952584f06342c51745eeccd76927
Patch0:		%{name}-enumfix.patch
URL:		http://maemo.org/
BuildRequires:	GConf2-devel >= 2.6
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gtk+2-devel >= 2:2.6.10
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libmatchbox-devel >= 1.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hildon widgets library for the Maemo platform.

%description -l pl.UTF-8
Biblioteka widgetów hildon dla platformy Maemo.

%package devel
Summary:	Header files for hildon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki hildon
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.6
Requires:	esound-devel
Requires:	gtk+2-devel >= 2:2.6.10
Requires:	libmatchbox-devel >= 1.3

%description devel
Header files for hildon library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki hildon.

%package static
Summary:	Static hildon library
Summary(pl.UTF-8):	Statyczna biblioteka hildon
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hildon-libs library.

%description static -l pl.UTF-8
Statyczna biblioteka hildon-libs.

%prep
%setup -q
%patch -P0 -p1

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog*
%attr(755,root,root) %{_libdir}/libhildonwidgets.so.*.*.*
%dir %{_libdir}/hildon-widgets
%attr(755,root,root) %{_libdir}/hildon-widgets/hildoncolorchooser*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhildonwidgets.so
%{_libdir}/libhildonwidgets.la
%{_libdir}/libtimer.a
%{_includedir}/hildon-lgpl
%{_includedir}/hildon-widgets
%{_pkgconfigdir}/hildon-libs.pc
%{_gtkdocdir}/hildon-libs

%files static
%defattr(644,root,root,755)
%{_libdir}/libhildonwidgets.a
