%define		_version	build10
Summary:	Game like Settlers II
Summary(pl.UTF-8):	Remake gry Settlers II
Name:		widelands
Version:	0.%{_version}
Release:	0.5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/widelands/%{name}-%{_version}-source.tar.bz2
# Source0-md5:	9e452baf7b8f22a27b4e371e2150e017
Source1:	%{name}.desktop
URL:		http://widelands.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel >= 1.2.7
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libstdc++-devel
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
%setup -q -n %{name}

%build
rm -f widelands
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -Isrc/ui/ui_basic -Isrc -Isrc/editor -Isrc/editor/ui_menus -Isrc/ui/ui_fs_menus -Isrc/editor/tools `sdl-config --cflags`" \
	IMPLICIT_LIBINTL="YES"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name},%{_desktopdir}}

install widelands $RPM_BUILD_ROOT%{_bindir}
cp -r campaigns fonts maps music pics sound tribes txts worlds $RPM_BUILD_ROOT%{_datadir}/games/%{name}

cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/widelands
%{_datadir}/games/widelands
%{_desktopdir}/widelands.desktop
