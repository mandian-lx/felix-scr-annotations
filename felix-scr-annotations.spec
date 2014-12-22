%{?_javapackages_macros:%_javapackages_macros}
%global project   felix
%global bundle    org.apache.felix.scr.annotations
Name:          felix-scr-annotations
Version:       1.9.6
Release:       3.2
Summary:       Annotations for SCR
Group:         Development/Java
License:       ASL 2.0
URL:           http://felix.apache.org/
Source0:       http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildRequires: java-devel
BuildRequires: mvn(org.apache.felix:felix-parent:pom:)
BuildRequires: mvn(org.apache.felix:org.apache.felix.scr.generator)

BuildRequires: maven-local
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-surefire-plugin
# i dont know which package as missing this required...
BuildRequires: mvn(org.mockito:mockito-all)

#Requires:      mvn(org.apache.felix:org.apache.felix.scr.generator)

BuildArch:     noarch

%description
Annotations for generating OSGi service descriptors.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%build

%mvn_file :%{bundle} %{project}/%{bundle}
# no test to run
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE changelog.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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
