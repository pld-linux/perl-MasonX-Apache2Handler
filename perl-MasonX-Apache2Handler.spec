#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MasonX
%define	pnam	Apache2Handler
Summary:	MasonX::Apache2Handler - experimental (alpha) Mason/mod_perl2 interface
Summary(pl):	MasonX::Apache2Handler - eksperymentalny (alfa) interfejs Mason/mod_perl2
Name:		perl-MasonX-Apache2Handler
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64fbb393e3e9a3a28e39827e74e9b11d
BuildRequires:	perl-devel >= 1:5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	apache-mod_perl >= 1.99_1
BuildRequires:	perl(Apache::Cookie) >= 2.02-dev
BuildRequires:	perl(Apache::Request) >= 2.02-dev
BuildRequires:	perl-HTML-Mason >= 1.25
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a Mason add-on which allows Mason to run in a pure
mod_perl2 environment.

MasonX::Apache2Handler is highly experimental (alpha) and should only
be used in a test environment.

%description -l pl
Ten modu³ jest dodatkiem do Masona umo¿liwiaj±cym Masonowi dzia³anie w
czystym ¶rodowisku mod_perl2. 

MasonX::Apache2Handler jest bardzo eksperymentalny (alfa) i powinien
byæ u¿ywany tylko w ¶rodowiskach testowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg scripts $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README htdocs/*.{html,css,gif}
%{perl_vendorlib}/MasonX/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
