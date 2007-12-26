#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	Tiny
Summary:	Config::Tiny - Read/Write .ini style files with as little code as possible
Summary(pl.UTF-8):	Config::Tiny - czytanie/zapisywanie plików w stylu .ini w minimalnym kodzie
Name:		perl-Config-Tiny
Version:	2.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1df5a4ff37cd1d80532ddbe28015d1f0
URL:		http://search.cpan.org/dist/Config-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(FindBin)
BuildRequires:	perl-Test-Simple
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

%description -l pl.UTF-8
Config::Tiny to klasa Perla do odczytu i zapisu plików
konfiguracyjnych w stylu .ini przy użyciu tak małego kodu, jak to
możliwe, co zmniejsza czas ładowania i użycie pamięci. Użycie pamięci
jest zwykle wyśmiewane w Perlu, ale zdaniem autora powinno być
przynajmniej brane pod uwagę.

Ten moduł służy głównie do czytania plików napisanych przez ludzi i
wszystko co zapisujemy nie powinno potrzebować dokumentacji czy
komentarzy. Jeśli potrzebujemy czegoś o większych możliwościach,
można przerzucić się na Config::Simple, Config::General lub jeden z
wielu innych modułów Config::. Innymi słowy, Config::Tiny nie
zachowuje komentarzy, odstępów ani porządku w pliku konfiguracyjnym.

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
%{perl_vendorlib}/Config/Tiny.pm
%{_mandir}/man3/*
