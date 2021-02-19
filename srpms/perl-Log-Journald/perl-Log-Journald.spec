Name:           perl-Log-Journald
Version:        0.30
Release:        1%{?dist}
Summary:        Send messages to a systemd journal
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Log-Journald/
Source0:        http://www.cpan.org/authors/id/L/LK/LKUNDRAK/Log-Journald-%{version}.tar.gz
Patch0:         Log-Journald_sd_journal_sendv.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  systemd-devel
BuildRequires:  perl(Test::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module wraps sd-journal(3) APIs for easy use in Perl. It makes it
possible to easily use systemd-journald.service(8)'s structured logging
capabilities and includes location of the logging point in the source code
in the messages.

%prep
%setup -q -n Log-Journald-%{version}
%autosetup -n Log-Journald-%{version} -p1

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc META.json README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Log*
%{_mandir}/man3/*

%changelog
* Mon Jan 07 2019 Madison Kelly <mkelly@alteeve.ca> 0.30-1
- Updated codebase to 0.30.
- Added the Log-Journald_sd_journal_sendv.patch patch.

* Fri Oct 06 2017 Madison Kelly <mkelly@alteeve.ca> 0.20-2
- Applied https://github.com/lkundrak/perl-Log-Journald/pull/4 to source.

* Fri Sep 29 2017 Madison Kelly <mkelly@alteeve.ca> 0.20-1
- Specfile autogenerated by cpanspec 1.78 and adapted to work.
