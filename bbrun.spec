Summary:	A simple run window with dropdown history list
Summary(pl.UTF-8):	Proste okienko uruchamiania z rozwijaną listą historii
Name:		bbrun
Version:	1.6
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.darkops.net/bbrun/%{name}-%{version}.tar.gz
# Source0-md5:	820960e3d52ddf2d5cf7e4ba51821bfd
URL:		http://www.darkops.net/bbrun/
BuildRequires:	XFree86-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BBrun is a run utility for BlackBox which can be run in the slit or in
withdrawn mode so that it can be bound to a keystroke from bbkeys. It
also features a history list of the most recent commands.

%description -l pl.UTF-8
BBrun to narzędzie do uruchamiania dla BlackBoksa. Może być
uruchamiane w szparze lub w trybie cofniętym, więc może być przypisane
do klawisza z bbkeys. Ma także listę historii ostatnio wywoływanych
poleceń.

%prep
%setup -q

%build
%{__make} -C bbrun \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `pkg-config --cflags gtk+-2.0`"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/%{name}
