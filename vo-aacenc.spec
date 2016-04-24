Name:		vo-aacenc
Version:	0.1.2
Release:	2%{?dist}
Summary:	VisualOn AAC encoder library
License:	ASL 2.0
Group:		System/Libraries
URL:		http://opencore-amr.sourceforge.net/
Source0:	http://sourceforge.net/projects/opencore-amr/files/%{name}/%{name}-%{version}.tar.gz
Requires:	glibc

%description
This library contains an encoder implementation of the Advanced Audio
Coding (AAC) audio codec. The library is based on a codec implementation
by VisualOn as part of the Stagefright framework from the Google
Android project.

This package is in the 'tainted' section because the AAC encoding 
standard is covered by patents.


%package devel
Group:		Development/C
Summary:	development files for %{name} AAC encoding library
Requires:	%{name} = %{version}-%{release}


%description devel
Header files and development libraries for %{name}


%prep
%setup -q

%build
%configure --disable-static
make
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%install
rm -rf %buildroot
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}


%files 
%{_libdir}/libvo-aacenc.so.0
%{_libdir}/libvo-aacenc.so.0.0.3


%files devel
%{_libdir}/lib%{name}.la
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_oldincludedir}/%{name}/cmnMemory.h
%{_oldincludedir}/%{name}/voAAC.h
%{_oldincludedir}/%{name}/voAMRWB.h
%{_oldincludedir}/%{name}/voAudio.h
%{_oldincludedir}/%{name}/voIndex.h
%{_oldincludedir}/%{name}/voMem.h
%{_oldincludedir}/%{name}/voType.h


%changelog

* Tue Apr 19 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 0.1.2-2
- Rebuilt

* Thu May 17 2012 David Vasquez <davidjeremias82 AT gmail DOT com> 0.1.2-1
- Initial build


