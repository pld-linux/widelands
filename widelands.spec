%define		_version	b9half
Summary:	Game like Settlers II
Summary(pl):	Remake gry Settlers II
Name:		widelands
Version:	0.%{_version}
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/widelands/%{name}-%{_version}-source.tar.bz2
# Source0-md5:	7bced82bda4b83d884da3e5b0143b2b4
Source1:	%{name}.desktop
URL:		http://widelands.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
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

%description -l pl
W grze Widelands jeste� regentem niewielkiego plemienia. Rozpoczynasz
gr� tylko z kwater� g��wn�, czym� w rodzaju zamku, w kt�rej
przechowywane s� wszystkie Twoje zasoby. Ka�dy cz�onek plemienia
wykona swoje zadanie w procesie produkcji tych�e zasob�w - drewna,
�ywno�ci, �elaza, z�ota i wielu innych - aby zapewni� rozw�j. Jednak
nie jeste� sam na tym �wiecie i wcze�niej lub p�niej b�dziesz musia�
spotka� si� z innymi plemionami. Niekt�re z nich mog� by� przyja�nie
nastawione i rozpocz�� z Tob� handel. Jednak, je�li chcesz rz�dzi�
�wiatem, b�dziesz musia� wyszkoli� �o�nierzy i walczy�.

%prep
%setup -q -n %{name}-%{_version}

%build
rm -f widelands
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -Isrc/ui/ui_basic -Isrc -Isrc/editor -Isrc/editor/ui_menus -Isrc/ui/ui_fs_menus -Isrc/editor/tools `sdl-config --cflags`" \
	IMPLICIT_LIBINTL="YES"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir}}

install widelands $RPM_BUILD_ROOT%{_bindir}
cp -r campaigns fonts maps pics tribes worlds $RPM_BUILD_ROOT%{_datadir}/%{name}

cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/widelands
%{_datadir}/widelands
%{_desktopdir}/widelands.desktop
