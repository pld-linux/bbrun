Summary:	A simple run window with dropdown history list
Summary(pl):	Proste okienko uruchamiania z rozwijan� list� historii
Name:		bbrun
Version:	1.4
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.dwave.net/~jking/bbrun/%{name}-%{version}.tar.gz
# Source0-md5:	d31cecada7d39b894bdf6012c6bae98a
URL:		http://www.dwave.net/~jking/bbrun/
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BBrun is a run utility for BlackBox which can be run in the slit or in
withdrawn mode so that it can be bound to a keystroke from bbkeys. It
also features a history list of the most recent commands.

%description -l pl
BBrun to narz�dzie do uruchamiania dla BlackBoksa. Mo�e by�
uruchamiane w szparze lub w trybie cofni�tym, wi�c mo�e by przypisany
do klawisza z bbkeys. Ma tak�e list� historii ostatnio wywo�ywanych
polece�.

%prep
%setup -q

%build
%{__make} -C bbrun \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/%{name}
