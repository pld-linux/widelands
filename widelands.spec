#
# TODO:
# - create bcond for ggz
#
%define		buildver	14
Summary:	Game like Settlers II
Summary(pl.UTF-8):	Remake gry Settlers II
Name:		widelands
Version:	0.build%{buildver}
Release:	0.6
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/widelands/Widelands-Build%{buildver}-src.7z
# Source0-md5:	06d63783b82b68af7af26198bc0a5afa
Source1:	%{name}.desktop
#Patch0:		%{name}-syntax.patch
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
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	p7zip
BuildRequires:	scons
BuildRequires:	sed >= 4.0
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
%setup -q -c -T -n %{name}
7z x -o.. %{SOURCE0}
#%%patch0 -p1
#%{__sed} -i 's/framework-mt/framework/' SConstruct

%{__sed} -i '/env.strip=1/d' build/scons-tools/scons_configure.py

%build
%scons \
	cxx="%{__cxx}" \
	cc="%{__cc}" \
	extra_compile_flags="%{rpmcxxflags} -O0" \
	extra_link_flags="%{rpmcxxflags} %{rpmldflags}" \
	build="release" \
	pretty_compile_output="false" \
	install_prefix="" \
	bindir="%{_bindir}" \
	datadir="%{_datadir}/games/%{name}" \
	localedir="%{_datadir}/games/%{name}/locale" \
	enable_ggz="false"

%install
rm -rf $RPM_BUILD_ROOT

%{__scons} install \
	build="release" \
	install_prefix="$RPM_BUILD_ROOT%{_prefix}" \
	bindir="$RPM_BUILD_ROOT%{_bindir}" \
	datadir="$RPM_BUILD_ROOT%{_datadir}/games/%{name}" \
	localedir="$RPM_BUILD_ROOT%{_datadir}/games/%{name}/locale" \

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
%lang(cs) %{_datadir}/games/%{name}/locale/cs_CZ
%lang(da) %{_datadir}/games/%{name}/locale/da_DK
%lang(de) %{_datadir}/games/%{name}/locale/de_DE
%lang(es) %{_datadir}/games/%{name}/locale/es_ES
%lang(fi) %{_datadir}/games/%{name}/locale/fi_FI
%lang(fr) %{_datadir}/games/%{name}/locale/fr_FR
%lang(gl) %{_datadir}/games/%{name}/locale/gl_ES
%lang(he) %{_datadir}/games/%{name}/locale/he_HE
%lang(hu) %{_datadir}/games/%{name}/locale/hu_HU
%lang(it) %{_datadir}/games/%{name}/locale/it_IT
%lang(nl) %{_datadir}/games/%{name}/locale/nl_NL
%lang(pl) %{_datadir}/games/%{name}/locale/pl_PL
%lang(ru) %{_datadir}/games/%{name}/locale/ru_RU
%lang(sk) %{_datadir}/games/%{name}/locale/sk_SK
%lang(sv) %{_datadir}/games/%{name}/locale/sv_SE
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
