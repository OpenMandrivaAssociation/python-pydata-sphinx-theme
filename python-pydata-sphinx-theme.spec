Name:		python-pydata-sphinx-theme
Version:	0.16.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pydata_sphinx_theme/pydata_sphinx_theme-%{version}.tar.gz
Source1:	pydata_sphinx_theme-0.16.1-vendor.tar.xz
Source100:	prepare_vendor.sh
Summary:	Bootstrap-based Sphinx theme from the PyData community
URL:		https://pypi.org/project/pydata-sphinx-theme/
License:	BSD-3-Clause
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(nodeenv)
BuildRequires:	nodejs
BuildRequires:	yarn

%global node_version %(node --version |sed -e 's,^v,,')

%description
Bootstrap-based Sphinx theme from the PyData community

%prep
%autosetup -p1 -a1 -n pydata_sphinx_theme-%{version}
sed -i -e 's,^node-version =.*,node-version = "%{node_version}",' pyproject.toml

%build -p
export YARN_CACHE_FOLDER="$(pwd)/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $(pwd)/.nodeenv

%files
%{py_sitedir}/pydata_sphinx_theme
%{py_sitedir}/pydata_sphinx_theme-*.*-info
