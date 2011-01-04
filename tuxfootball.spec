Summary:	Great 2D soccer (sometimes called football) game
Name:		tuxfootball
Version:	0.3.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/project/tuxfootball/0.3/%{name}-%{version}.tar.gz
# Source0-md5:	fa2475227ef30685887cc6e41663d4d3
BuildRequires:	SDL_image
BuildRequires:	SDL_mixer
BuildRequires:	gettext-devel
BuildRequires:	pkg-config
URL:		http://tuxfootball.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tux Football is a great 2D soccer (sometimes called football) game for
Windows and Linux. It's bringing old style gameplay from DOS times
back to the desktop with up to date graphics! It's gameplay is similar
to old classics such as Amco's Kick Off and Sensible Software's
Sensible Soccer.

%prep
%setup -q

%build
%configure --disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
