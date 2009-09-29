#
# TODO:
# - translations
# - create bcond for ggz
# - could not find file or directory: pics/splash.jpg
#
%define		_build	14
Summary:	Game like Settlers II
Summary(pl.UTF-8):	Remake gry Settlers II
Name:		widelands
Version:	0.build%{_build}
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/widelands/Widelands-Build%{_build}-src.7z
# Source0-md5:	06d63783b82b68af7af26198bc0a5afa
Source1:	%{name}.desktop
Patch0:		%{name}-syntax.patch
URL:		http://widelands.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.11
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel >= 1.2.7
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel >= 2.0.0
BuildRequires:	boost-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	p7zip
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In Widelands, you are the regent of a small tribe. You start out with
nothing but your headquarters, a kind of castle in which all your
resources are stored. Every member of your tribe will do his or her
part to produce more resources - wood, food, iron, gold and more - to
further this growth. But you are not alone in the world, and you will
meet other tribes sooner or later. Some of them may be friendly and
trade with you. However, if you want to rule the world, you will have
to train soldiers and fight.

%description -l pl.UTF-8
W grze Widelands jesteś regentem niewielkiego plemienia. Rozpoczynasz
grę tylko z kwaterą główną, czymś w rodzaju zamku, w której
przechowywane są wszystkie Twoje zasoby. Każdy członek plemienia
wykona swoje zadanie w procesie produkcji tychże zasobów - drewna,
żywności, żelaza, złota i wielu innych - aby zapewnić rozwój. Jednak
nie jesteś sam na tym świecie i wcześniej lub później będziesz musiał
spotkać się z innymi plemionami. Niektóre z nich mogą być przyjaźnie
nastawione i rozpocząć z Tobą handel. Jednak, jeśli chcesz rządzić
światem, będziesz musiał wyszkolić żołnierzy i walczyć.

%prep
%setup -q -c -T -n %{name}
7z x -o.. %{SOURCE0}
%patch0 -p1
%{__sed} -i 's/framework-mt/framework/' SConstruct

%build
%scons -j 1 \
	build="release" \
	install_prefix="%{_prefix}" \
	bindir="%{_bindir}" \
	datadir="%{_datadir}/%{name}" \
	enable_ggz="false"

%install
rm -rf $RPM_BUILD_ROOT

%scons install \
	install_prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}/%{name}

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install pics/wl-ico-128.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
