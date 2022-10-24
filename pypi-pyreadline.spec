#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyreadline
Version  : 2.1
Release  : 30
URL      : https://files.pythonhosted.org/packages/bc/7c/d724ef1ec3ab2125f38a1d53285745445ec4a8f19b9bb0761b4064316679/pyreadline-2.1.zip
Source0  : https://files.pythonhosted.org/packages/bc/7c/d724ef1ec3ab2125f38a1d53285745445ec4a8f19b9bb0761b4064316679/pyreadline-2.1.zip
Summary  : A python implmementation of GNU readline.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pyreadline-license = %{version}-%{release}
Requires: pypi-pyreadline-python = %{version}-%{release}
Requires: pypi-pyreadline-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
The pyreadline package is a python implementation of GNU readline functionality
        it is based on the ctypes based UNC readline package by Gary Bishop.
        It is not complete. It has been tested for use with windows 2000 and windows xp.
        
        * pyreadline 2.1 <2015-09-16>
        
          This is a bugfix release to make pyreadline work with python 3.5.

%package license
Summary: license components for the pypi-pyreadline package.
Group: Default

%description license
license components for the pypi-pyreadline package.


%package python
Summary: python components for the pypi-pyreadline package.
Group: Default
Requires: pypi-pyreadline-python3 = %{version}-%{release}

%description python
python components for the pypi-pyreadline package.


%package python3
Summary: python3 components for the pypi-pyreadline package.
Group: Default
Requires: python3-core
Provides: pypi(pyreadline)

%description python3
python3 components for the pypi-pyreadline package.


%prep
%setup -q -n pyreadline-2.1
cd %{_builddir}/pyreadline-2.1
pushd ..
cp -a pyreadline-2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656399855
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyreadline
cp %{_builddir}/pyreadline-2.1/doc/COPYING %{buildroot}/usr/share/package-licenses/pypi-pyreadline/73bbd67c3b98ceffb9c7d040331bd631b0f6a3e4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyreadline/73bbd67c3b98ceffb9c7d040331bd631b0f6a3e4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
