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
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libmatchbox1-devel
BuildRequires:	libtool
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
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dbus-launch-systembus.sh
%attr(755,root,root) %{_bindir}/dbus-launch.sh
%attr(755,root,root) %{_bindir}/osso-date
%attr(755,root,root) %{_libdir}/hildon.so.*.*.*
%{_sysconfdir}/dbus-1/system.d/hildon.conf
%dir %{_sysconfdir}/hildon
%{_sysconfdir}/hildon/sessionbus-hildon.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/hildon.so
%{_libdir}/hildon.la
%{_includedir}/hildon.h
%{_includedir}/log-functions.h
%{_includedir}/osso-log.h
%{_includedir}/osso-mem.h
%{_pkgconfigdir}/hildon.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/hildon.a
