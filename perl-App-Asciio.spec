%define module   App-Asciio
%define version  1.02.71

%define _requires_exceptions perl(App::Asciio::.*)  

Name:		perl-%{module}
Version:    %{version}
Release:    %mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Plain ASCII diagram
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/App/%{module}-%{version}.tar.gz
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
BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This gtk2-perl application allows you to draw ASCII diagrams in a modern (but
simple) graphical application. The ASCII graphs can be saved as ASCII or in a
format that allows you to modify them later.

%prep
%setup -q -n %{module}-%{version} 

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

