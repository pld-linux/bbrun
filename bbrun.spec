Name: bbrun
Version: 1.4
Release: alt1

Summary: A simple run window with dropdown history list
License: GPL
Group: File tools

Url: http://www.dwave.net/~jking/bbrun/
Source: %name-%version.tar.bz2
Patch: %name-1.4-alt-make.patch

Requires: common-licenses

# Automatically added by buildreq on Mon Feb 24 2003
BuildRequires: XFree86-devel glib-devel gtk+-devel xpm-devel

%description
BBrun is a run utility for BlackBox which can be run in the slit or
in withdrawn mode so that it can be bound to a keystroke from bbkeys.
It also features a history list of the most recent commands.

%prep
%setup -q
%patch -p1

%build
%make_build -C %name

%install
%__install -pD -m755 %name/%name %buildroot%_bindir/%name
%__install -pD -m644 %name/%name.xpm %buildroot%_miconsdir/%name.xpm
%__ln_s -f /usr/share/license/GPL-2 COPYING
%__mkdir_p %buildroot%_menudir
%__cat <<EOF >%buildroot%_menudir/%name
?package(%name): \
	command="%_bindir/%name -w" \
	needs="x11" \
	icon="%name.xpm" \
	section="Applications/File tools" \
	title="BBrun" \
	longtitle="A simple run window"
EOF

%post
%update_menus

%postun
%clean_menus

%files
%_bindir/%name
%_menudir/%name
%_miconsdir/%name.xpm
%doc Changelog README
%doc --no-dereference COPYING

%changelog
* Mon Feb 24 2003 Alexey Tourbin <at@altlinux.ru> 1.4-alt1
- initial revision
