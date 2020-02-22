#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : modules
Version  : 4.4.1
Release  : 12
URL      : https://github.com/cea-hpc/modules/releases/download/v4.4.1/modules-4.4.1.tar.bz2
Source0  : https://github.com/cea-hpc/modules/releases/download/v4.4.1/modules-4.4.1.tar.bz2
Summary  : Provides dynamic modification of a user's environment
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: modules-bin = %{version}-%{release}
Requires: modules-data = %{version}-%{release}
Requires: modules-libexec = %{version}-%{release}
Requires: modules-license = %{version}-%{release}
Requires: modules-man = %{version}-%{release}
Requires: python3
Requires: tcl
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : less
BuildRequires : pkgconfig(x11)
BuildRequires : procps-ng
BuildRequires : python3
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-staticdev

%description
The Environment Modules package provides for the dynamic modification of
a user's environment via modulefiles.

Each modulefile contains the information needed to configure the shell
for an application. Once the Modules package is initialized, the
environment can be modified on a per-module basis using the module
command which interprets modulefiles. Typically modulefiles instruct
the module command to alter or set shell environment variables such as
PATH, MANPATH, etc. modulefiles may be shared by many users on a system
and users may have their own collection to supplement or replace the
shared modulefiles.

Modules can be loaded and unloaded dynamically and atomically, in an
clean fashion. All popular shells are supported, including bash, ksh,
zsh, sh, csh, tcsh, as well as some scripting languages such as perl.

Modules are useful in managing different versions of applications.
Modules can also be bundled into metamodules that will load an entire
suite of different applications.

NOTE: You will need to get a new shell after installing this package to
have access to the module alias.

%package bin
Summary: bin components for the modules package.
Group: Binaries
Requires: modules-data = %{version}-%{release}
Requires: modules-libexec = %{version}-%{release}
Requires: modules-license = %{version}-%{release}

%description bin
bin components for the modules package.


%package data
Summary: data components for the modules package.
Group: Data

%description data
data components for the modules package.


%package dev
Summary: dev components for the modules package.
Group: Development
Requires: modules-bin = %{version}-%{release}
Requires: modules-data = %{version}-%{release}
Provides: modules-devel = %{version}-%{release}
Requires: modules = %{version}-%{release}

%description dev
dev components for the modules package.


%package doc
Summary: doc components for the modules package.
Group: Documentation
Requires: modules-man = %{version}-%{release}

%description doc
doc components for the modules package.


%package libexec
Summary: libexec components for the modules package.
Group: Default
Requires: modules-license = %{version}-%{release}

%description libexec
libexec components for the modules package.


%package license
Summary: license components for the modules package.
Group: Default

%description license
license components for the modules package.


%package man
Summary: man components for the modules package.
Group: Default

%description man
man components for the modules package.


%prep
%setup -q -n modules-4.4.1
cd %{_builddir}/modules-4.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582331359
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --without-tclx \
--prefix=/usr/share/modules \
--etcdir=/usr/share/defaults/etc \
--docdir=/usr/share/doc/environment-modules \
--vimdatadir=/usr/share/vim/vimfiles
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export SOURCE_DATE_EPOCH=1582331359
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/modules
cp %{_builddir}/modules-4.4.1/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/modules/db95910cb27890d60e596e4c622fc3eeba6693fa
cp %{_builddir}/modules-4.4.1/compat/LICENSE.GPL %{buildroot}/usr/share/package-licenses/modules/db95910cb27890d60e596e4c622fc3eeba6693fa
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/profile.d
ln -s /usr/share/modules/init/profile.sh  %{buildroot}/usr/share/defaults/etc/profile.d/modules.sh
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/add.modules
/usr/bin/envml
/usr/bin/mkroot
/usr/bin/modulecmd

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/profile.d/modules.sh
/usr/share/defaults/etc/siteconfig.tcl
/usr/share/modules/init/bash
/usr/share/modules/init/bash_completion
/usr/share/modules/init/cmake
/usr/share/modules/init/csh
/usr/share/modules/init/fish
/usr/share/modules/init/fish_completion
/usr/share/modules/init/ksh
/usr/share/modules/init/ksh-functions/module
/usr/share/modules/init/ksh-functions/switchml
/usr/share/modules/init/lisp
/usr/share/modules/init/modulerc
/usr/share/modules/init/perl.pm
/usr/share/modules/init/profile-compat.csh
/usr/share/modules/init/profile-compat.sh
/usr/share/modules/init/profile.csh
/usr/share/modules/init/profile.sh
/usr/share/modules/init/python.py
/usr/share/modules/init/r.R
/usr/share/modules/init/ruby.rb
/usr/share/modules/init/sh
/usr/share/modules/init/tcl
/usr/share/modules/init/tcsh
/usr/share/modules/init/tcsh_completion
/usr/share/modules/init/zsh
/usr/share/modules/init/zsh-functions/_module
/usr/share/modules/modulefiles/dot
/usr/share/modules/modulefiles/module-git
/usr/share/modules/modulefiles/module-info
/usr/share/modules/modulefiles/modules
/usr/share/modules/modulefiles/null
/usr/share/modules/modulefiles/use.own
/usr/share/vim/vimfiles/ftdetect/modulefile.vim
/usr/share/vim/vimfiles/ftplugin/modulefile.vim
/usr/share/vim/vimfiles/syntax/modulefile.vim

%files dev
%defattr(-,root,root,-)
/usr/lib64/libtclenvmodules.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/environment-modules/CONTRIBUTING.txt
/usr/share/doc/environment-modules/COPYING.GPLv2
/usr/share/doc/environment-modules/ChangeLog
/usr/share/doc/environment-modules/ChangeLog-compat
/usr/share/doc/environment-modules/INSTALL.txt
/usr/share/doc/environment-modules/MIGRATING.txt
/usr/share/doc/environment-modules/NEWS-compat
/usr/share/doc/environment-modules/NEWS.txt
/usr/share/doc/environment-modules/README
/usr/share/doc/environment-modules/diff_v3_v4.txt
/usr/share/doc/environment-modules/example.txt

%files libexec
%defattr(-,root,root,-)
/usr/libexec/modulecmd-compat
/usr/libexec/modulecmd.tcl

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/modules/db95910cb27890d60e596e4c622fc3eeba6693fa

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/module-compat.1
/usr/share/man/man1/module.1
/usr/share/man/man4/modulefile-compat.4
/usr/share/man/man4/modulefile.4
