Name: signon-plugin-oauth2-qt5
Version: 0.15
Release: 1
Summary: Plugin which provides oauth and oauth2 authentication enablers to signond
Group: System/Libraries
License: LGPLv2.1
URL: http://code.google.com/p/accounts-sso/
Source0: %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Test)
# FIXME: change to pkgconfig(signond) when mer core no longer provides broken qt4-using
# signond.pc
BuildRequires: signon-qt5-devel


%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_libdir}/signon/liboauth2plugin.so

%prep
%setup -q -n %{name}-%{version}/signon-plugin-oauth2


%package oauthclient
Summary: OAuth2 SignOn Plugin OAuth Client
Group: System/Tools

%description oauthclient
%{summary}.

%files oauthclient
%defattr(-,root,root,-)
%{_bindir}/oauthclient
%{_sysconfdir}/signon-ui/webkit-options.d/m.facebook.com.conf
%{_sysconfdir}/signon-ui/webkit-options.d/www.facebook.com.conf


%package devel
Summary: Tests for the oauth2 signon plugin
Group: System/Libraries

%description devel
%{summary}.

%files devel
%{_includedir}/signon-plugins/oauth1data.h
%{_includedir}/signon-plugins/oauth2data.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc


%package tests
Summary: Tests for the oauth2 signon plugin
Group: System/Libraries

%description tests
%{summary}.

%files tests
%{_bindir}/signon-oauth2plugin-tests
%{_datadir}/signon-oauth2plugin-tests/tests.xml


%build
sed -i 's,$${INSTALL_PREFIX}/lib64,$${INSTALL_PREFIX}/lib,g' common-project-config.pri
%qmake5
make %{?jobs:-j%jobs}

%install
%qmake5_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig