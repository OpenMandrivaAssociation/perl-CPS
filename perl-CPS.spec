%define upstream_name    CPS
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Iterate at some later point
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


