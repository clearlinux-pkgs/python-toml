#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-toml
Version  : 0.9.2
Release  : 3
URL      : http://pypi.debian.net/toml/toml-0.9.2.tar.gz
Source0  : http://pypi.debian.net/toml/toml-0.9.2.tar.gz
Summary  : Python Library for Tom's Obvious, Minimal Language
Group    : Development/Tools
License  : MIT
Requires: python-toml-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
TOML
====
Original repository: https://github.com/uiri/toml
See also https://github.com/mojombo/toml

%package python
Summary: python components for the python-toml package.
Group: Default

%description python
python components for the python-toml package.


%prep
%setup -q -n toml-0.9.2

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
