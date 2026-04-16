%define oname pydata_sphinx_theme

Name:		python-pydata-sphinx-theme
Version:	0.17.0
Release:	1
Summary:	Bootstrap-based Sphinx theme from the PyData community
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/pydata-sphinx-theme/
Source0:	https://files.pythonhosted.org/packages/source/p/pydata_sphinx_theme/pydata_sphinx_theme-%{version}.tar.gz
Source1:	pydata_sphinx_theme-%{version}-vendor.tar.xz
Source100:	prepare_vendor.sh

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(nodeenv)
BuildRequires:	python%{pyver}dist(sphinx-theme-builder)
BuildRequires:	nodejs
BuildRequires:	yarn

%global node_version %(node --version |sed -e 's,^v,,')

%description
Bootstrap-based Sphinx theme from the PyData community

%prep
%autosetup -p1 -a1 -n %{oname}-%{version}
sed -i -e 's,^node-version =.*,node-version = "%{node_version}",' pyproject.toml

%build -p
export YARN_CACHE_FOLDER="$(pwd)/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $(pwd)/.nodeenv

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
