%define upstream_name    App-Asciio
%define upstream_version 1.02.71

%define _requires_exceptions perl(App::Asciio::.*)  

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Plain ASCII diagram
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Clone)
BuildRequires:  perl(Data::TreeDumper)
BuildRequires:  perl(Data::TreeDumper::Renderer::GTK)
BuildRequires:  perl(Directory::Scratch)
BuildRequires:  perl(Directory::Scratch::Structured)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Eval::Context)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Block)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Strict)
BuildRequires:  perl(Term::Size)
BuildRequires:	perl(Module::Build)

BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This gtk2-perl application allows you to draw ASCII diagrams in a modern (but
simple) graphical application. The ASCII graphs can be saved as ASCII or in a
format that allows you to modify them later.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
# test don't run, even with xvfb-run
# xvfb-run ./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Todo.txt Changes
%{_mandir}/man3/*
%{_bindir}/asciio
%{perl_vendorlib}/App
