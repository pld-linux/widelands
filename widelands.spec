#
# TODO:
# - create bcond for ggz
#
%define		buildver	15
Summary:	Game like Settlers II
Summary(pl.UTF-8):	Remake gry Settlers II
Name:		widelands
Version:	0.build%{buildver}
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://launchpad.net/widelands/build%{buildver}/build%{buildver}/+download/%{name}-build%{buildver}-src.tar.bz2
# Source0-md5:	5b2e2d0913272f66055e424f91360b1d
Source1:	%{name}.desktop
Patch0:		%{name}-locale.patch
URL:		http://widelands.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.11
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel >= 1.2.7
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel >= 2.0.0
BuildRequires:	boost-devel >= 1.35
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
Requires:	SDL_image >= 1.2.10
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
%setup -q -n %{name}-build%{buildver}-src
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DWL_INSTALL_BINDIR=%{_bindir} \
	-DWL_INSTALL_DATADIR=%{_datadir}/games/%{name} \
	-DWL_INSTALL_LOCALEDIR=%{_datadir}/games/%{name}/locale \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install pics/wl-ico-128.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/VERSION
%{_datadir}/games/%{name}/campaigns
%{_datadir}/games/%{name}/fonts
%{_datadir}/games/%{name}/global
%{_datadir}/games/%{name}/maps
%{_datadir}/games/%{name}/music
%{_datadir}/games/%{name}/pics
%{_datadir}/games/%{name}/sound
%{_datadir}/games/%{name}/tribes
%{_datadir}/games/%{name}/txts
%{_datadir}/games/%{name}/worlds
%dir %{_datadir}/games/%{name}/locale
%lang(ar) %{_datadir}/games/%{name}/locale/ar
%lang(ca) %{_datadir}/games/%{name}/locale/ca
%lang(cs) %{_datadir}/games/%{name}/locale/cs
%lang(da) %{_datadir}/games/%{name}/locale/da
%lang(de) %{_datadir}/games/%{name}/locale/de
%lang(en_GB) %{_datadir}/games/%{name}/locale/en_GB
%lang(eo) %{_datadir}/games/%{name}/locale/eo
%lang(es) %{_datadir}/games/%{name}/locale/es
%lang(eu) %{_datadir}/games/%{name}/locale/eu
%lang(fi) %{_datadir}/games/%{name}/locale/fi
%lang(fr) %{_datadir}/games/%{name}/locale/fr
%lang(gl) %{_datadir}/games/%{name}/locale/gl
%lang(he) %{_datadir}/games/%{name}/locale/he
%lang(hu) %{_datadir}/games/%{name}/locale/hu
%lang(ia) %{_datadir}/games/%{name}/locale/ia
%lang(id) %{_datadir}/games/%{name}/locale/id
%lang(it) %{_datadir}/games/%{name}/locale/it
%lang(ja) %{_datadir}/games/%{name}/locale/ja
%lang(la) %{_datadir}/games/%{name}/locale/la
%lang(nl) %{_datadir}/games/%{name}/locale/nl
%lang(nn) %{_datadir}/games/%{name}/locale/nn
%lang(pl) %{_datadir}/games/%{name}/locale/pl
%lang(pt_BR) %{_datadir}/games/%{name}/locale/pt_BR
%lang(ru) %{_datadir}/games/%{name}/locale/ru
%lang(si) %{_datadir}/games/%{name}/locale/si
%lang(sk) %{_datadir}/games/%{name}/locale/sk
%lang(sl) %{_datadir}/games/%{name}/locale/sl
%lang(sr) %{_datadir}/games/%{name}/locale/sr
%lang(sv) %{_datadir}/games/%{name}/locale/sv
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
