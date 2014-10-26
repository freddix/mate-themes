Summary:	Default themes for MATE enviroment
Name:		mate-themes
Version:	1.8.1
Release:	1
License:	LGPL
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	5c348c11eb78c0ee0442ee429132d2c7
Patch0:		%{name}-bashizm.patch
URL:		http://www.mate.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	icon-naming-utils
BuildRequires:	intltool
BuildRequires:	libtool
BuildArch:	noarch
Requires:	mate-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for MATE enviroment.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-all-themes \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

CD=`pwd`
cd $RPM_BUILD_ROOT%{_iconsdir}
for dir in *
do
        gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/$dir
done
cd $CD

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,crh,si,ug}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_datadir}/themes/AlaDelta
%{_datadir}/themes/Atantla
%{_datadir}/themes/BlackMATE
%{_datadir}/themes/BlackMenta
%{_datadir}/themes/BlueMenta
%{_datadir}/themes/ContrastHigh
%{_datadir}/themes/ContrastHighInverse
%{_datadir}/themes/ContrastHighLargePrint
%{_datadir}/themes/ContrastHighLargePrintInverse
%{_datadir}/themes/ContrastLow
%{_datadir}/themes/ContrastLowLargePrint
%{_datadir}/themes/Fog
%{_datadir}/themes/GreenLaguna
%{_datadir}/themes/Menta
%{_datadir}/themes/PrintLarge
%{_datadir}/themes/Quid
%{_datadir}/themes/Reverse
%{_datadir}/themes/Shiny
%{_datadir}/themes/Simply
%{_datadir}/themes/TraditionalGreen
%{_datadir}/themes/TraditionalOk
%{_iconsdir}/ContrastHigh
%{_iconsdir}/ContrastHigh-SVG
%{_iconsdir}/ContrastHighInverse
%{_iconsdir}/ContrastHighLargePrint
%{_iconsdir}/ContrastHighLargePrintInverse
%{_iconsdir}/Fog
%{_iconsdir}/MateLargePrint
%{_iconsdir}/Quid
%{_iconsdir}/mate

