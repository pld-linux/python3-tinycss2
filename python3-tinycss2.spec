#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Low-level CSS parser for Python
Summary(pl.UTF-8):	Niskopoziomowy parser CSS dla Pythona
Name:		python3-tinycss2
Version:	1.4.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tinycss2/
Source0:	https://files.pythonhosted.org/packages/source/t/tinycss2/tinycss2-%{version}.tar.gz
# Source0-md5:	de6bd20b47354352c2b2344c842385c7
URL:		https://pypi.org/project/tinycss2/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-webencodings >= 0.4
%endif
%if %{with doc}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-sphinx_rtd_theme
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tinycss2 is a modern, low-level CSS parser for Python. tinycss2 is a
rewrite of tinycss with a simpler API, based on the more recent CSS
Syntax Level 3 specification.

%description -l pl.UTF-8
tinycss2 to nowoczesny, niskopoziomowy parser CSS dla Ptyhona. Jest to
napisany od początku tinycss z prostszym API, oparty na nowszej
specyfikacji CSS Syntax Level 3.

%package apidocs
Summary:	API documentation for Python tinycss2 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona tinycss2
Group:		Documentation

%description apidocs
API documentation for Python tinycss2 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona tinycss2.

%prep
%setup -q -n tinycss2-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest -v
%endif

%if %{with doc}
cd docs
PYTHONPATH=$(pwd)/.. \
%{__python3} -m sphinx -W . build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/tinycss2
%{py3_sitescriptdir}/tinycss2-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif
