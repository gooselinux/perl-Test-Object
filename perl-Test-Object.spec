Name:           perl-Test-Object
Version:        0.07
Release:        6%{?dist}
Summary:        Thoroughly testing objects via registered handlers

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Object/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Test-Object-%{version}.tar.gz
Patch0:         Test-Object-0.07-Makefile.PL.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Scalar::Util) >= 1.16
BuildRequires:  perl(Test::Builder) >= 0.32
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Test::Object is a testing package designed to allow you to easily test
what you believe is a valid object against the expected behaviour of
all of the classes in its inheritance tree in one single call.


%prep
%setup -q -n Test-Object-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test AUTOMATED_TESTING=1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-6
- add readme
- Related: rhbz#543948

* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.07-5.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.07-3
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.07-2
- rebuild for new perl

* Thu Sep  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.07-1
- Update to 0.07.
- Test::Builder version problem (see #205537).
- Removed the README file (copy of the manpage).

* Wed Sep 06 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.06-1
- First build.
