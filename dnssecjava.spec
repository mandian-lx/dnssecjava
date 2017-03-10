%{?_javapackages_macros:%_javapackages_macros}

Summary:	A DNSSEC validating stub resolver for Java
Name:		dnssecjava
Version:	1.1.3
Release:	1
License:	Eclipse Public License
Group:		Development/Java
Url:		https://github.com/ibauersachs/%{name}
Source0:	https://github.com/ibauersachs/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:		%{name}-1.1.3-checkstyle.patch
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(dnsjava:dnsjava)
#BuildRequires:	mvn(joda-time:joda-time)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-release-plugin)
#BuildRequires:	mvn(org.eluder.coveralls:coveralls-maven-plugin)
BuildRequires:	mvn(org.jacoco:jacoco-maven-plugin)
#BuildRequires:	mvn(org.powermock:powermock-api-mockito)
#BuildRequires:	mvn(org.powermock:powermock-module-junit4)
BuildRequires:	mvn(org.slf4j:slf4j-api)
BuildRequires:	mvn(org.slf4j:slf4j-jdk14)

%description
A DNSSEC validating stub resolver for Java.

%files -f .mfiles

#----------------------------------------------------------------------------

%package javadoc
Summary:	Javadoc for %{name}
BuildArch:	noarch

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{name}-%{version}
# Delete prebuild JARs and libs
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Apply all patches
%patch0 -p1 -b .orig

# Fix jar name
%mvn_file :%{name} %{name}-%{version} %{name}

%build
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

