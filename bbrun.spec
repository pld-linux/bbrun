Summary:	A simple run window with dropdown history list
Summary(pl):	Proste okienko uruchamiania z rozwijan± list± historii
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

%description -l pl
BBrun to narzêdzie do uruchamiania dla BlackBoksa. Mo¿e byæ
uruchamiane w szparze lub w trybie cofniêtym, wiêc mo¿e byæ przypisane
do klawisza z bbkeys. Ma tak¿e listê historii ostatnio wywo³ywanych
poleceñ.

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
