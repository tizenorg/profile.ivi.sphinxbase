Name:       sphinxbase
Version:    0.7
Release:    0
Group:      System/Libraries
License:    BSD-2-Clause
URL:        http://www.pocketsphinx.org/
Summary:    Speech Recognition Engine
Source:     http://sourceforge.net/projects/cmusphinx/files/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools

%description
Sphinxbase is a common library for CMU Sphinx voice recognition products.
This package does not provide voice recognition by itself.

%package devel
Summary:        Header and other development files for sphinxbase
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Header files and other development files for sphinxbase.

%package libs
Summary:        Libraries for sphinxbase
Group:          Development/Libraries

%description libs
The libraries for sphinxbase.

%package python
Summary:        Python interface to sphinxbase
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}

%description python
Python interface to sphinxbase package

%prep
%setup -q

%build
%reconfigure --disable-static --disable-rpath
%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{python_sitearch}
%make_install
rm -f %{buildroot}%{_libdir}/*.la

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/*.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/sphinxbase
%{_libdir}/libsphinxad.so
%{_libdir}/libsphinxbase.so
%{_libdir}/pkgconfig/sphinxbase.pc

%files libs
%defattr(-,root,root,-)
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libsphinxad.so.*
%{_libdir}/libsphinxbase.so.*

%files python
%defattr(-,root,root,-)
%{python_sitearch}/*
%changelog
