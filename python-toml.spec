#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-toml
Version  : 0.9.6
Release  : 24
URL      : https://files.pythonhosted.org/packages/0e/e8/1aa958599e5326b690a31334112da68a9b75e7563879e2c5103ca219d30a/toml-0.9.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/0e/e8/1aa958599e5326b690a31334112da68a9b75e7563879e2c5103ca219d30a/toml-0.9.6.tar.gz
Summary  : Python Library for Tom's Obvious, Minimal Language
Group    : Development/Tools
License  : MIT
Requires: python-toml-python3
Requires: python-toml-python
BuildRequires : buildreq-distutils3

%description
TOML
        ****

%package python
Summary: python components for the python-toml package.
Group: Default
Requires: python-toml-python3

%description python
python components for the python-toml package.


%package python3
Summary: python3 components for the python-toml package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-toml package.


%prep
%setup -q -n toml-0.9.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536587846
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
