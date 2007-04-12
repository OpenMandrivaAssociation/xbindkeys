%define	version	1.8.0
%define release	%mkrel 1

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
BuildRequires:	X11-devel guile-devel
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
%make LDFLAGS="-lpthread"

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


