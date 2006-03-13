#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	Tiny
Summary:	Config::Tiny - Read/Write .ini style files with as little code as possible
Summary(pl):	Config::Tiny - czytanie/zapisywanie plików w stylu .ini w minimalnym kodzie
Name:		perl-Config-Tiny
Version:	2.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bac7f9eda771593c869313859fe45ff7
URL:		http://search.cpan.org/dist/Config-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::Tiny is a Perl class to read and write .ini style
configuration files with as little code as possible, reducing load
time and memory overhead. Memory usage is normally scoffed at in Perl,
but in my opinion should be at least kept in mind.

This module is primarily for reading human written files, and anything
we write shouldn't need to have documentation/comments. If you need
something with more power, move up to Config::Simple, Config::General
or one of the many other Config:: modules. To rephrase, Config::Tiny
does not preserve your comments, whitespace, or the order of your
config file.

%description -l pl
Config::Tiny to klasa Perla do odczytu i zapisu plików
konfiguracyjnych w stylu .ini przy u¿yciu tak ma³ego kodu, jak to
mo¿liwe, co zmniejsza czas ³adowania i u¿ycie pamiêci. U¿ycie pamiêci
jest zwykle wy¶miewane w Perlu, ale zdaniem autora powinno byæ
przynajmniej brane pod uwagê.

Ten modu³ s³u¿y g³ównie do czytania plików napisanych przez ludzi i
wszystko co zapisujemy nie powinno potrzebowaæ dokumentacji czy
komentarzy. Je¶li potrzebujemy czego¶ o wiêkszych mo¿liwo¶ciach,
mo¿na przerzuciæ siê na Config::Simple, Config::General lub jeden z
wielu innych modu³ów Config::. Innymi s³owy, Config::Tiny nie
zachowuje komentarzy, odstêpów ani porz±dku w pliku konfiguracyjnym.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Config/*.pm
%{_mandir}/man3/*
