Summary:	Link keyboard and mouse input events with shell commands
Name:		xbindkeys
Version:	1.8.7
Release:	2
License:	GPL
Group:		System/X11
URL:		https://hocwp.free.fr/xbindkeys/xbindkeys.html
Source:		%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(x11) 
BuildRequires:  pkgconfig(guile-1.8)
# (for xbindkey_show)
Requires:	tk
Requires: guile1.8-runtime

%description
%{name} is a program that allows you to launch shell commands with
your keyboard or your mouse under X Window. It links commands to keys
or mouse buttons, using a configuration file. It's independent of the
window manager and can capture all keyboard keys (e.g. Power, Wake...).

%prep
%autosetup -p1
%build 
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS BUGS ChangeLog README
%{_bindir}/*
%{_mandir}/man?/*
