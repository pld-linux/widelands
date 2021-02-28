# TODO:
# - check locales
# - use system fonts where possible
#
%define		buildver	21
Summary:	A real-time build-up strategy game
Summary(pl.UTF-8):	Gra strategiczna czasu rzeczywistego z budowaniem
Name:		widelands
Version:	0.build%{buildver}
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
#Source0Download: https://wl.widelands.org/wiki/Download/#release
Source0:	http://launchpad.net/widelands/build%{buildver}/build%{buildver}/+download/%{name}-build%{buildver}-source.tar.gz
# Source0-md5:	2933da247b2009f5608e92624d606851
Patch0:		%{name}-pld.patch
Patch1:		gcc8.patch
Patch2:		%{name}-install.patch
URL:		https://wl.widelands.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel >= 2
BuildRequires:	SDL2_image-devel >= 2
BuildRequires:	SDL2_mixer-devel >= 2
BuildRequires:	SDL2_ttf-devel >= 2.0.12
BuildRequires:	boost-devel >= 1.48
BuildRequires:	cmake >= 2.8.7
BuildRequires:	gettext-tools
BuildRequires:	glew-devel
BuildRequires:	libicu-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 6:4.8
BuildRequires:	python >= 2
BuildRequires:	python-modules >= 2
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
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

%package data
Summary:	A real-time build-up strategy game - data files
Summary(pl.UTF-8):	Gra strategiczna czasu rzeczywistego z budowaniem - pliki danych
Group:		X11/Applications/Games
BuildArch:	noarch

%description data
Data files for Widelands, a real-time build-up strategy game inspired
by Settlers II.

%description data -l pl.UTF-8
Pliki danych do Widelands - gry strategicznej czasu rzeczywistego z
budowaniem, zainspirowanej Settlers II.

%prep
%setup -q -n %{name}-build%{buildver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake .. \
	-DWL_INSTALL_BASEDIR=%{_prefix} \
	-DWL_INSTALL_BINDIR=%{_bindir} \
	-DWL_INSTALL_DATADIR=%{_datadir}/games/%{name}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# VERSION unneeded, COPYING generic GPL v2, the rest packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_prefix}/{COPYING,CREDITS,ChangeLog,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS
%attr(755,root,root) %{_bindir}/widelands
%attr(755,root,root) %{_bindir}/wl_create_spritesheet
%attr(755,root,root) %{_bindir}/wl_map_info
%attr(755,root,root) %{_bindir}/wl_map_object_info
%{_datadir}/metainfo/org.widelands.Widelands.appdata.xml
%{_desktopdir}/org.widelands.Widelands.desktop
%{_iconsdir}/hicolor/*x*/apps/org.widelands.Widelands.png
%{_mandir}/man6/widelands.6*

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/ai
%{_datadir}/games/%{name}/campaigns
%dir %{_datadir}/games/%{name}/i18n
%{_datadir}/games/%{name}/i18n/fonts.lua
%{_datadir}/games/%{name}/i18n/locales.lua
%dir %{_datadir}/games/%{name}/i18n/fonts
# font-set=hebrew
%lang(he) %{_datadir}/games/%{name}/i18n/fonts/Culmus
# font-set=default
%{_datadir}/games/%{name}/i18n/fonts/DejaVu
# font-set=cjk
%lang(ja,ko,zh_CN,zh_TW) %{_datadir}/games/%{name}/i18n/fonts/MicroHei
# font-set=devanagari
%lang(hi,mr) %{_datadir}/games/%{name}/i18n/fonts/Nakula
%{_datadir}/games/%{name}/i18n/fonts/Widelands
# font-set=arabic
%lang(ar,fa,ms) %{_datadir}/games/%{name}/i18n/fonts/amiri
%dir %{_datadir}/games/%{name}/i18n/locales
%lang(ar) %{_datadir}/games/%{name}/i18n/locales/ar.json
%lang(bg) %{_datadir}/games/%{name}/i18n/locales/bg.json
%lang(br) %{_datadir}/games/%{name}/i18n/locales/br.json
%lang(ca) %{_datadir}/games/%{name}/i18n/locales/ca.json
%lang(cs) %{_datadir}/games/%{name}/i18n/locales/cs.json
%lang(da) %{_datadir}/games/%{name}/i18n/locales/da.json
%lang(de) %{_datadir}/games/%{name}/i18n/locales/de.json
%lang(el) %{_datadir}/games/%{name}/i18n/locales/el.json
%lang(en_GB) %{_datadir}/games/%{name}/i18n/locales/en_GB.json
%lang(en_US) %{_datadir}/games/%{name}/i18n/locales/en_US.json
%lang(eo) %{_datadir}/games/%{name}/i18n/locales/eo.json
%lang(es) %{_datadir}/games/%{name}/i18n/locales/es.json
%lang(eu) %{_datadir}/games/%{name}/i18n/locales/eu.json
%lang(fa) %{_datadir}/games/%{name}/i18n/locales/fa.json
%lang(fi) %{_datadir}/games/%{name}/i18n/locales/fi.json
%lang(fr) %{_datadir}/games/%{name}/i18n/locales/fr.json
%lang(fy) %{_datadir}/games/%{name}/i18n/locales/fy.json
%lang(ga) %{_datadir}/games/%{name}/i18n/locales/ga.json
%lang(gd) %{_datadir}/games/%{name}/i18n/locales/gd.json
%lang(gl) %{_datadir}/games/%{name}/i18n/locales/gl.json
%lang(he) %{_datadir}/games/%{name}/i18n/locales/he.json
%lang(hi) %{_datadir}/games/%{name}/i18n/locales/hi.json
%lang(hr) %{_datadir}/games/%{name}/i18n/locales/hr.json
%lang(hu) %{_datadir}/games/%{name}/i18n/locales/hu.json
%lang(id) %{_datadir}/games/%{name}/i18n/locales/id.json
%lang(ig) %{_datadir}/games/%{name}/i18n/locales/ig.json
%lang(it) %{_datadir}/games/%{name}/i18n/locales/it.json
%lang(ja) %{_datadir}/games/%{name}/i18n/locales/ja.json
%lang(ka) %{_datadir}/games/%{name}/i18n/locales/ka.json
%lang(ko) %{_datadir}/games/%{name}/i18n/locales/ko.json
%lang(krl) %{_datadir}/games/%{name}/i18n/locales/krl.json
%lang(la) %{_datadir}/games/%{name}/i18n/locales/la.json
%{_datadir}/games/%{name}/i18n/locales/locales_translators.json
%lang(lt) %{_datadir}/games/%{name}/i18n/locales/lt.json
%lang(ms) %{_datadir}/games/%{name}/i18n/locales/ms.json
%lang(nb) %{_datadir}/games/%{name}/i18n/locales/nb.json
%lang(nds) %{_datadir}/games/%{name}/i18n/locales/nds.json
%lang(nl) %{_datadir}/games/%{name}/i18n/locales/nl.json
%lang(nn) %{_datadir}/games/%{name}/i18n/locales/nn.json
%lang(pl) %{_datadir}/games/%{name}/i18n/locales/pl.json
%lang(pt) %{_datadir}/games/%{name}/i18n/locales/pt.json
%lang(pt_BR) %{_datadir}/games/%{name}/i18n/locales/pt_BR.json
%lang(ro) %{_datadir}/games/%{name}/i18n/locales/ro.json
%lang(ru) %{_datadir}/games/%{name}/i18n/locales/ru.json
%lang(sk) %{_datadir}/games/%{name}/i18n/locales/sk.json
%lang(sl) %{_datadir}/games/%{name}/i18n/locales/sl.json
%lang(sr) %{_datadir}/games/%{name}/i18n/locales/sr.json
%lang(sr_RS) %{_datadir}/games/%{name}/i18n/locales/sr_RS.json
%lang(sv) %{_datadir}/games/%{name}/i18n/locales/sv.json
%lang(tr) %{_datadir}/games/%{name}/i18n/locales/tr.json
%lang(uk) %{_datadir}/games/%{name}/i18n/locales/uk.json
%lang(zh_CN) %{_datadir}/games/%{name}/i18n/locales/zh_CN.json
%lang(zh_TW) %{_datadir}/games/%{name}/i18n/locales/zh_TW.json
%{_datadir}/games/%{name}/i18n/translation_stats.conf
%{_datadir}/games/%{name}/images
%dir %{_datadir}/games/%{name}/locale
%lang(ar) %{_datadir}/games/%{name}/locale/ar
%lang(bg) %{_datadir}/games/%{name}/locale/bg
%lang(br) %{_datadir}/games/%{name}/locale/br
%lang(ca) %{_datadir}/games/%{name}/locale/ca
%lang(cs) %{_datadir}/games/%{name}/locale/cs
%lang(da) %{_datadir}/games/%{name}/locale/da
%lang(de) %{_datadir}/games/%{name}/locale/de
%lang(el) %{_datadir}/games/%{name}/locale/el
%lang(en_GB) %{_datadir}/games/%{name}/locale/en_GB
%lang(en_US) %{_datadir}/games/%{name}/locale/en_US
%lang(eo) %{_datadir}/games/%{name}/locale/eo
%lang(es) %{_datadir}/games/%{name}/locale/es
%lang(eu) %{_datadir}/games/%{name}/locale/eu
%lang(fa) %{_datadir}/games/%{name}/locale/fa
%lang(fi) %{_datadir}/games/%{name}/locale/fi
%lang(fr) %{_datadir}/games/%{name}/locale/fr
%lang(fy) %{_datadir}/games/%{name}/locale/fy
%lang(ga) %{_datadir}/games/%{name}/locale/ga
%lang(gd) %{_datadir}/games/%{name}/locale/gd
%lang(gl) %{_datadir}/games/%{name}/locale/gl
%lang(he) %{_datadir}/games/%{name}/locale/he
%lang(hi) %{_datadir}/games/%{name}/locale/hi
%lang(hr) %{_datadir}/games/%{name}/locale/hr
%lang(hu) %{_datadir}/games/%{name}/locale/hu
%lang(id) %{_datadir}/games/%{name}/locale/id
%lang(ig) %{_datadir}/games/%{name}/locale/ig
%lang(it) %{_datadir}/games/%{name}/locale/it
%lang(ja) %{_datadir}/games/%{name}/locale/ja
%lang(ka) %{_datadir}/games/%{name}/locale/ka
%lang(ko) %{_datadir}/games/%{name}/locale/ko
%lang(krl) %{_datadir}/games/%{name}/locale/krl
%lang(la) %{_datadir}/games/%{name}/locale/la
%lang(lt) %{_datadir}/games/%{name}/locale/lt
%lang(ms) %{_datadir}/games/%{name}/locale/ms
%lang(nb) %{_datadir}/games/%{name}/locale/nb
%lang(nds) %{_datadir}/games/%{name}/locale/nds
%lang(nl) %{_datadir}/games/%{name}/locale/nl
%lang(nn) %{_datadir}/games/%{name}/locale/nn
%lang(pl) %{_datadir}/games/%{name}/locale/pl
%lang(pt) %{_datadir}/games/%{name}/locale/pt
%lang(pt_BR) %{_datadir}/games/%{name}/locale/pt_BR
%lang(ro) %{_datadir}/games/%{name}/locale/ro
%lang(ru) %{_datadir}/games/%{name}/locale/ru
%lang(sk) %{_datadir}/games/%{name}/locale/sk
%lang(sl) %{_datadir}/games/%{name}/locale/sl
%lang(sr) %{_datadir}/games/%{name}/locale/sr
%lang(sr_RS) %{_datadir}/games/%{name}/locale/sr_RS
%lang(sv) %{_datadir}/games/%{name}/locale/sv
%lang(tr) %{_datadir}/games/%{name}/locale/tr
%lang(uk) %{_datadir}/games/%{name}/locale/uk
%lang(zh_CN) %{_datadir}/games/%{name}/locale/zh_CN
%lang(zh_TW) %{_datadir}/games/%{name}/locale/zh_TW
%{_datadir}/games/%{name}/maps
%{_datadir}/games/%{name}/music
%{_datadir}/games/%{name}/scripting
%{_datadir}/games/%{name}/shaders
%{_datadir}/games/%{name}/sound
%{_datadir}/games/%{name}/templates
%{_datadir}/games/%{name}/tribes
%{_datadir}/games/%{name}/txts
%{_datadir}/games/%{name}/world
