#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (incomplete dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Mock object framework for Python 2/3
Summary(pl.UTF-8):	Szkielet obiektów atrap dla Pythona 2/3
Name:		python-mox3
# keep 0.x here for python2 support
Version:	0.28.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mox3/
Source0:	https://files.pythonhosted.org/packages/source/m/mox3/mox3-%{version}.tar.gz
# Source0-md5:	c930d8479996541b04447a67e96e4a62
URL:		https://pypi.org/project/mox3/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-stestr >= 2.0.0
BuildRequires:	python-subunit >= 1.0.0
BuildRequires:	python-testtools >= 2.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-testtools >= 2.2.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-openstackdocstheme >= 1.18.1
BuildRequires:	sphinx-pdg-2 >= 1.7.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mox3 is an unofficial port of the Google mox framework to Python 3. It
was meant to be as compatible with mox as possible, but small
enhancements have been made.

%description -l pl.UTF-8
Mox3 to nieoficjalny port szkieletu Google mox do Pythona 3. Ma być
możliwie zgodny z mox, ale zostały dodane niewielkie rozszerzenia.

%package -n python3-mox3
Summary:	Mock object framework for Python 3
Summary(pl.UTF-8):	Szkielet obiektów atrap dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-mox3
Mox3 is an unofficial port of the Google mox framework to Python 3. It
was meant to be as compatible with mox as possible, but small
enhancements have been made.

%description -n python3-mox3 -l pl.UTF-8
Mox3 to nieoficjalny port szkieletu Google mox do Pythona 3. Ma być
możliwie zgodny z mox, ale zostały dodane niewielkie rozszerzenia.

%package apidocs
Summary:	API documentation for Python mox3 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona mox3
Group:		Documentation

%description apidocs
API documentation for Python mox3 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona mox3.

%prep
%setup -q -n mox3-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
stestr run
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
stestr run
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/mox3/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/mox3/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/mox3
%{py_sitescriptdir}/mox3-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-mox3
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/mox3
%{py3_sitescriptdir}/mox3-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,user,*.html,*.js}
%endif
