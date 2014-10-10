%define upstream_name    App-Asciio
%define upstream_version 1.02.71


%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(App::Asciio::(.*)\\)'
%else
%define _requires_exceptions perl(App::Asciio::.*)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Plain ASCII diagram
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildRequires:	perl(Data::TreeDumper)
BuildRequires:	perl(Data::TreeDumper::Renderer::GTK)
BuildRequires:	perl(Directory::Scratch)
BuildRequires:	perl(Directory::Scratch::Structured)
BuildRequires:	perl(Data::Compare)
BuildRequires:	perl(Eval::Context)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Block)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Strict)
BuildRequires:	perl(Term::Size)
BuildRequires:	perl(Module::Build)

BuildArch:	noarch

%description
This gtk2-perl application allows you to draw ASCII diagrams in a modern (but
simple) graphical application. The ASCII graphs can be saved as ASCII or in a
format that allows you to modify them later.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
# test don't run, even with xvfb-run
# xvfb-run ./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README Todo.txt Changes
%{_mandir}/man3/*
%{_bindir}/asciio
%{perl_vendorlib}/App


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.2.71-4mdv2011.0
+ Revision: 680575
- add br
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.2.71-3mdv2011.0
+ Revision: 504569
- bump mkrel
- rebuild using %%perl_convert_version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Feb 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.02.71-2mdv2009.1
+ Revision: 344557
- fix dependencies

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.02.71-1mdv2009.1
+ Revision: 343971
- import perl-App-Asciio


* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.02.71-1mdv2009.1
- first mdv release 
