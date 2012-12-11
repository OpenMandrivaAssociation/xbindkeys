%define	version	1.8.3
%define release	%mkrel 3

Summary:	Link keyboard and mouse input events with shell commands
Name:		xbindkeys
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/X11
URL:		http://hocwp.free.fr/xbindkeys/xbindkeys.html
Source:		http://hocwp.free.fr/xbindkeys/%{name}-%{version}.tar.bz2
Patch0:         xbindkeys-1.7.3-rplmalloc.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libx11-devel guile-devel
# (for xbindkey_show)
Requires:	tk

%description
%{name} is a program that allows you to launch shell commands with
your keyboard or your mouse under X Window. It links commands to keys
or mouse buttons, using a configuration file. It's independent of the
window manager and can capture all keyboard keys (e.g. Power, Wake...).

%prep
%setup -q
%patch0 -b .rplmalloc

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog README
%{_bindir}/*
%{_mandir}/man?/*




%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.8.3-3mdv2010.0
+ Revision: 445887
- rebuild

* Thu Jan 29 2009 Funda Wang <fundawang@mandriva.org> 1.8.3-2mdv2009.1
+ Revision: 335145
- rebuild

* Mon Jan 26 2009 Jérôme Soyer <saispo@mandriva.org> 1.8.3-1mdv2009.1
+ Revision: 333685
- New upstream release

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.8.2-3mdv2009.0
+ Revision: 242988
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Apr 20 2007 Jérôme Soyer <saispo@mandriva.org> 1.8.2-1mdv2008.0
+ Revision: 15692
- New release 1.8.2

* Tue Apr 17 2007 Jérôme Soyer <saispo@mandriva.org> 1.8.1-1mdv2007.1
+ Revision: 13617
- New release 0.8.1


* Sat Feb 17 2007 Jérôme Soyer <saispo@mandriva.org> 1.8.0-1mdv2007.0
+ Revision: 122101
- New release 1.8.0
- Import xbindkeys

* Thu Jun 22 2006 Jerome Soyer <saispo@mandriva.org> 1.7.3-1mdv2007.0
- New release 1.7.3

* Sat Apr 29 2006 Jerome Soyer <saispo@mandriva.org> 1.7.2-1mdk
- New release 1.7.2

* Tue Nov 22 2005 Abel Cheung <deaddog@mandriva.org> 1.7.1-2mdk
- Add missing requirement (#17769)

* Wed Apr 27 2005 Abel Cheung <deaddog@mandriva.org> 1.7.1-1mdk
- First Mandriva Linux package

