Summary:	A simple run window with dropdown history list
Summary(pl):	Proste okienko uruchamiania z rozwijan± list± historii
Name:		bbrun
Version:	1.4
Release:	alt1
License:	GPL
Group:		Applications
Source0:	http://www.dwave.net/~jking/bbrun/%{name}-%{version}.tar.gz
Patch0:		%{name}-1.4-alt-make.patch
URL:		http://www.dwave.net/~jking/bbrun/
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BBrun is a run utility for BlackBox which can be run in the slit or in
withdrawn mode so that it can be bound to a keystroke from bbkeys. It
also features a history list of the most recent commands.

%description -l pl
BBrun to narzêdzie do uruchamiania dla BlackBoksa. Mo¿e byæ
uruchamiane w szparze lub w trybie cofniêtym, wiêc mo¿e by przypisany
do klawisza z bbkeys. Ma tak¿e listê historii ostatnio wywo³ywanych
poleceñ.

%prep
%setup -q
%patch -p1

%build
%make_build -C %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
#install -D %{name}/%name.xpm %buildroot%_miconsdir/%name.xpm
#%__mkdir_p %buildroot%_menudir
#%__cat <<EOF >%buildroot%_menudir/%name
#?package(%name): \
#	command="%_bindir/%name -w" \
#	needs="x11" \
#	icon="%name.xpm" \
#	section="Applications/File tools" \
#	title="BBrun" \
#	longtitle="A simple run window"
#EOF

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/%{name}
#%_menudir/%name
#%_miconsdir/%name.xpm
