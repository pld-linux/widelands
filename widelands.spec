# TODO:
# - check locales
# - use system fonts where possible
#
Summary:	A real-time build-up strategy game
Summary(pl.UTF-8):	Gra strategiczna czasu rzeczywistego z budowaniem
Name:		widelands
Version:	1.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
#Source0Download: https://wl.widelands.org/wiki/Download/#release
Source0:	https://github.com/widelands/widelands/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	749233228813421efc5802b58cce21bb
Patch0:		%{name}-pld.patch
URL:		https://wl.widelands.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	SDL2-devel >= 2
BuildRequires:	SDL2_image-devel >= 2
BuildRequires:	SDL2_mixer-devel >= 2
BuildRequires:	SDL2_ttf-devel >= 2.0.12
BuildRequires:	asio-devel
BuildRequires:	boost-devel >= 1.48
BuildRequires:	cmake >= 3.12
BuildRequires:	curl-devel
BuildRequires:	doxygen
BuildRequires:	gettext-tools
BuildRequires:	glew-devel
BuildRequires:	graphviz
BuildRequires:	libicu-devel
BuildRequires:	libpng-devel >= 1.6
BuildRequires:	libstdc++-devel >= 6:4.8
BuildRequires:	minizip-devel
BuildRequires:	python3 >= 3
BuildRequires:	python3-modules >= 3
BuildRequires:	rpm-build >= 4.6
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
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description data
Data files for Widelands, a real-time build-up strategy game inspired
by Settlers II.

%description data -l pl.UTF-8
Pliki danych do Widelands - gry strategicznej czasu rzeczywistego z
budowaniem, zainspirowanej Settlers II.

%package debug
Summary:	Debugging tools for Widelands
Summary(pl.UTF-8):	Narzędzia debugowania dla Widelands
%description debug
Additional debugging data for Widelands. This package is not needed
for normal operation.

%description debug -l pl.UTF-8
Dodatkowe dane debugowania dla Widelands. Ten pakiet nie jest
potrzebny do normalnej pracy.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake .. \
	-DWL_INSTALL_PREFIX=%{_prefix} \
	-DWL_INSTALL_BINDIR=bin \
	-DWL_INSTALL_DATADIR=%{_datadir}/%{name} \
	-DWL_INSTALL_LOCALEDIR=%{_datadir}/%{name}/locale

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# VERSION unneeded, COPYING generic GPL v2, the rest packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_prefix}/{COPYING,CREDITS,ChangeLog,VERSION}
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc

find $RPM_BUILD_ROOT%{_datadir}/widelands/i18n/translations -name *.pot -type f -delete

# custom search for translations
cd $RPM_BUILD_ROOT
:> translations.txt
for LangDirs in \
        usr/share/widelands/i18n/translations/map_along_the_river.wmf \
        usr/share/widelands/i18n/translations/maps \
        usr/share/widelands/i18n/translations/map_the_green_plateau.wmf \
        usr/share/widelands/i18n/translations/mp_scenario_island_hopping.wmf \
        usr/share/widelands/i18n/translations/mp_scenario_smugglers.wmf \
        usr/share/widelands/i18n/translations/scenario_atl01.wmf \
        usr/share/widelands/i18n/translations/scenario_atl02.wmf \
        usr/share/widelands/i18n/translations/scenario_bar01.wmf \
        usr/share/widelands/i18n/translations/scenario_bar02.wmf \
        usr/share/widelands/i18n/translations/scenario_dummy.wmf \
        usr/share/widelands/i18n/translations/scenario_emp01.wmf \
        usr/share/widelands/i18n/translations/scenario_emp02.wmf \
        usr/share/widelands/i18n/translations/scenario_emp03.wmf \
        usr/share/widelands/i18n/translations/scenario_emp04.wmf \
        usr/share/widelands/i18n/translations/scenario_fri01.wmf \
        usr/share/widelands/i18n/translations/scenario_fri02.wmf \
        usr/share/widelands/i18n/translations/scenario_fri03.wmf \
        usr/share/widelands/i18n/translations/scenario_fri04.wmf \
        usr/share/widelands/i18n/translations/scenario_fri05.wmf \
        usr/share/widelands/i18n/translations/scenario_tutorial01_basic_control.wmf \
        usr/share/widelands/i18n/translations/scenario_tutorial02_warfare.wmf \
        usr/share/widelands/i18n/translations/scenario_tutorial03_seafaring.wmf \
        usr/share/widelands/i18n/translations/scenario_tutorial04_economy.wmf \
        usr/share/widelands/i18n/translations/texts \
        usr/share/widelands/i18n/translations/training_wheels \
        usr/share/widelands/i18n/translations/tribes \
        usr/share/widelands/i18n/translations/tribes_encyclopedia \
        usr/share/widelands/i18n/translations/widelands \
        usr/share/widelands/i18n/translations/widelands_console \
        usr/share/widelands/i18n/translations/widelands_editor \
        usr/share/widelands/i18n/translations/win_conditions \
        usr/share/widelands/i18n/translations/world
do
        find $LangDirs/ -name ??_??.po | sed -n "s#\($LangDirs/\(.*\_..\)\)#%lang(\2) /\1#p" >> translations.txt
        find $LangDirs/ -name ???.po | sed -n "s#\($LangDirs/\(...\)\)#%lang(\2) /\1#p" >> translations.txt
        find $LangDirs/ -name ??.po | sed -n "s#\($LangDirs/\(..\)\)#%lang(\2) /\1#p" >> translations.txt
done

cd -
%{__mv} $RPM_BUILD_ROOT/translations.txt .

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS CONTRIBUTING.md README.md Release_Notes.md
%attr(755,root,root) %{_bindir}/widelands
%{_datadir}/metainfo/org.widelands.Widelands.metainfo.xml
%{_desktopdir}/org.widelands.Widelands.desktop
%{_iconsdir}/hicolor/*x*/apps/org.widelands.Widelands.png
%{_mandir}/man6/widelands.6*

%files data -f translations.txt
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ai
%{_datadir}/%{name}/campaigns
%dir %{_datadir}//%{name}/i18n
%{_datadir}/%{name}/i18n/fonts.lua
%{_datadir}/%{name}/i18n/locales.lua
%dir %{_datadir}/%{name}/i18n/fonts
# font-set=hebrew
%lang(he) %{_datadir}/%{name}/i18n/fonts/Culmus
# font-set=default
%{_datadir}/%{name}/i18n/fonts/DejaVu
# font-set=cjk
%lang(ja,ko,zh_CN,zh_TW) %{_datadir}/%{name}/i18n/fonts/MicroHei
# font-set=devanagari
%lang(hi,mr) %{_datadir}/%{name}/i18n/fonts/Nakula
%{_datadir}/%{name}/i18n/fonts/Widelands
# font-set=arabic
%lang(ar,fa,ms) %{_datadir}/%{name}/i18n/fonts/amiri
%dir %{_datadir}/%{name}/i18n/locales
%lang(ar) %{_datadir}/%{name}/i18n/locales/ar.json
%lang(bg) %{_datadir}/%{name}/i18n/locales/bg.json
%lang(br) %{_datadir}/%{name}/i18n/locales/br.json
%lang(ca) %{_datadir}/%{name}/i18n/locales/ca.json
%lang(cs) %{_datadir}/%{name}/i18n/locales/cs.json
%lang(da) %{_datadir}/%{name}/i18n/locales/da.json
%lang(de) %{_datadir}/%{name}/i18n/locales/de.json
%lang(el) %{_datadir}/%{name}/i18n/locales/el.json
%lang(en_GB) %{_datadir}/%{name}/i18n/locales/en_GB.json
%lang(en_US) %{_datadir}/%{name}/i18n/locales/en_US.json
%lang(eo) %{_datadir}/%{name}/i18n/locales/eo.json
%lang(es) %{_datadir}/%{name}/i18n/locales/es.json
%lang(eu) %{_datadir}/%{name}/i18n/locales/eu.json
%lang(fa) %{_datadir}/%{name}/i18n/locales/fa.json
%lang(fi) %{_datadir}/%{name}/i18n/locales/fi.json
%lang(fr) %{_datadir}/%{name}/i18n/locales/fr.json
%lang(fy) %{_datadir}/%{name}/i18n/locales/fy.json
%lang(ga) %{_datadir}/%{name}/i18n/locales/ga.json
%lang(gd) %{_datadir}/%{name}/i18n/locales/gd.json
%lang(gl) %{_datadir}/%{name}/i18n/locales/gl.json
%lang(he) %{_datadir}/%{name}/i18n/locales/he.json
%lang(hi) %{_datadir}/%{name}/i18n/locales/hi.json
%lang(hr) %{_datadir}/%{name}/i18n/locales/hr.json
%lang(hu) %{_datadir}/%{name}/i18n/locales/hu.json
%lang(id) %{_datadir}/%{name}/i18n/locales/id.json
%lang(ig) %{_datadir}/%{name}/i18n/locales/ig.json
%lang(it) %{_datadir}/%{name}/i18n/locales/it.json
%lang(ja) %{_datadir}/%{name}/i18n/locales/ja.json
%lang(ka) %{_datadir}/%{name}/i18n/locales/ka.json
%lang(ko) %{_datadir}/%{name}/i18n/locales/ko.json
%lang(krl) %{_datadir}/%{name}/i18n/locales/krl.json
%lang(la) %{_datadir}/%{name}/i18n/locales/la.json
%{_datadir}/%{name}/i18n/locales/locales_translators.json
%lang(lt) %{_datadir}/%{name}/i18n/locales/lt.json
%lang(ms) %{_datadir}/%{name}/i18n/locales/ms.json
%lang(nb) %{_datadir}/%{name}/i18n/locales/nb.json
%lang(nds) %{_datadir}/%{name}/i18n/locales/nds.json
%lang(nl) %{_datadir}/%{name}/i18n/locales/nl.json
%lang(nn) %{_datadir}/%{name}/i18n/locales/nn.json
%lang(pl) %{_datadir}/%{name}/i18n/locales/pl.json
%lang(pt) %{_datadir}/%{name}/i18n/locales/pt.json
%lang(pt_BR) %{_datadir}/%{name}/i18n/locales/pt_BR.json
%lang(ro) %{_datadir}/%{name}/i18n/locales/ro.json
%lang(ru) %{_datadir}/%{name}/i18n/locales/ru.json
%lang(sk) %{_datadir}/%{name}/i18n/locales/sk.json
%lang(sl) %{_datadir}/%{name}/i18n/locales/sl.json
%lang(sr) %{_datadir}/%{name}/i18n/locales/sr.json
%lang(sr_RS) %{_datadir}/%{name}/i18n/locales/sr_RS.json
%lang(sv) %{_datadir}/%{name}/i18n/locales/sv.json
%lang(tr) %{_datadir}/%{name}/i18n/locales/tr.json
%lang(uk) %{_datadir}/%{name}/i18n/locales/uk.json
%lang(zh_CN) %{_datadir}/%{name}/i18n/locales/zh_CN.json
%lang(zh_TW) %{_datadir}/%{name}/i18n/locales/zh_TW.json
%{_datadir}/%{name}/i18n/translation_stats.conf
%{_datadir}/%{name}/images
%{_datadir}/%{name}/maps
%{_datadir}/%{name}/music
%{_datadir}/%{name}/scripting
%{_datadir}/%{name}/shaders
%{_datadir}/%{name}/sound
%{_datadir}/%{name}/templates
%{_datadir}/%{name}/tribes
%{_datadir}/%{name}/txts
%{_datadir}/%{name}/world
%{_datadir}/%{name}/datadirversion
# translations dirs
%dir %{_datadir}/widelands/i18n/translations
%dir %{_datadir}/widelands/i18n/translations/map_along_the_river.wmf
%dir %{_datadir}/widelands/i18n/translations/map_the_green_plateau.wmf
%dir %{_datadir}/widelands/i18n/translations/maps
%dir %{_datadir}/widelands/i18n/translations/mp_scenario_island_hopping.wmf
%dir %{_datadir}/widelands/i18n/translations/mp_scenario_smugglers.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_atl01.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_atl02.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_bar01.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_bar02.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_dummy.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_emp01.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_emp02.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_emp03.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_emp04.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_fri01.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_fri02.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_fri03.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_fri04.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_fri05.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_tutorial01_basic_control.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_tutorial02_warfare.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_tutorial03_seafaring.wmf
%dir %{_datadir}/widelands/i18n/translations/scenario_tutorial04_economy.wmf
%dir %{_datadir}/widelands/i18n/translations/texts
%dir %{_datadir}/widelands/i18n/translations/training_wheels
%dir %{_datadir}/widelands/i18n/translations/tribes
%dir %{_datadir}/widelands/i18n/translations/tribes_encyclopedia
%dir %{_datadir}/widelands/i18n/translations/widelands
%dir %{_datadir}/widelands/i18n/translations/widelands_console
%dir %{_datadir}/widelands/i18n/translations/widelands_editor
%dir %{_datadir}/widelands/i18n/translations/win_conditions
%dir %{_datadir}/widelands/i18n/translations/world

%files debug
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wl_create_spritesheet
%attr(755,root,root) %{_bindir}/wl_map_info
%attr(755,root,root) %{_bindir}/wl_map_object_info
