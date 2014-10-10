%define upstream_name    CPS
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Iterate at some later point
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Objects based on this abstract class are used by the 'gk*' variants of the
the CPS manpage functions, to control their behavior. These objects are
expected to provide a method, 'again', which the functions will use to
re-invoke iterations of loops, and so on. By providing a different
implementation of this method, governor objects can provide such behaviours
as rate-limiting, asynchronisation or parallelism, and integration with
event-based IO frameworks.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 654245
- rebuild for updated spec-helper

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 626868
- import perl-CPS

