#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Low-level CSS parser for Python
Name:		python3-tinycss2
Version:	1.1.0
Release:	2
License:	BSD
Source0:	https://files.pythonhosted.org/packages/source/t/tinycss2/tinycss2-%{version}.tar.gz
# Source0-md5:	7caf513c4e87fc2449dcfbf407a8416f
Patch0:		disable-flake8-isort-for-pytest.patch
Patch1:		disable-missing-data-tests.patch
URL:		https://pypi.python.org/pypi/tinycss2/
# required to run the tests
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-pytest-runner
BuildRequires:	python3-setuptools
BuildRequires:	python3-webencodings >= 0.4
%endif
BuildArch:	noarch

%description
tinycss2 is a modern, low-level CSS parser for Python. tinycss2 is a
rewrite of tinycss with a simpler API, based on the more recent CSS
Syntax Level 3 specification.

%prep
%setup -n tinycss2-%{version}
%patch0 -p1
%patch1 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%if %{with tests}
%{__python3} -m pytest -v
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/tinycss2
%{py3_sitescriptdir}/tinycss2-%{version}-py*.egg-info
