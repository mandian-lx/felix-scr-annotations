%{?_javapackages_macros:%_javapackages_macros}

%global bundle org.apache.felix.scr.annotations

Name:          felix-scr-annotations
Version:       1.12.0
Release:       2.1
Summary:       Annotations for SCR
License:       ASL 2.0
URL:           http://felix.apache.org/
Source0:       http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.scr.generator)

%description
Annotations for generating OSGi service descriptors.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file : felix/%{bundle}

%build
# no test to run
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Mat Booth <mat.booth@redhat.com> - 1.12.0-1
- Update to latest upstream release
- Re-generate BRs

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 gil cattaneo <puntogil@libero.it> 1.9.12-1
- update to 1.9.12

* Sun Feb 01 2015 gil cattaneo <puntogil@libero.it> 1.9.10-2
- introduce license macro

* Fri Jan 23 2015 gil cattaneo <puntogil@libero.it> 1.9.10-1
- update to 1.9.10

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 19 2013 gil cattaneo <puntogil@libero.it> 1.9.6-2
- add missing BR mockito

* Thu Aug 29 2013 gil cattaneo <puntogil@libero.it> 1.9.6-1
- update to 1.9.6

* Mon Jun 24 2013 gil cattaneo <puntogil@libero.it> 1.9.4-1
- update to 1.9.4

* Tue Apr 02 2013 gil cattaneo <puntogil@libero.it> 1.9.0-1
- update to 1.9.0

* Mon Jan 21 2013 gil cattaneo <puntogil@libero.it> 1.7.0-1
- initial rpm
