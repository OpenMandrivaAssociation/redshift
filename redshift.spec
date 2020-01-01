%define name	redshift
%define version	1.12

Name:		%{name}
Version:	%{version}
Release:	1
Summary:	Adjusts the color temperature of your screen according to time of day
Url:		http://jonls.dk/redshift/
Source:		https://github.com/jonls/redshift/archive/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv3+
Group:		Graphical desktop/Other
BuildRequires:	x11-server-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	python-devel
BuildRequires:	pkgconfig(systemd)
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libtool
# For 1.7 geoclue support is reported to be broken, but later we can try it
# BuildRequires: geoclue-devel
# Requires:      geoclue

%package gtk
Summary:	GTK integration for Redshift
Group:		Graphical desktop/Other
Requires:	pygtk2.0
Requires:	redshift = %{version}-%{release}

%description
Redshift adjusts the color temperature of your screen according to your
surroundings. This may help your eyes hurt less if you are working in
front of the screen at night.

The color temperature is set according to the position of the sun. A
different color temperature is set during night and daytime. During
twilight and early morning, the color temperature transitions smoothly
from night to daytime temperature to allow your eyes to slowly
adapt.

%description gtk
GTK integration for Redshift, a screen color temperature adjustment
program.

%prep
%setup -q
autopoint -f && AUTOPOINT="intltoolize --automake --copy" autoreconf -f -i
%build

%configure \
	--disable-rpath \
	--with-systemduserunitdir=%{_unitdir} \
	--enable-gui
%make

%install
rm -rf %{buildroot}
%makeinstall_std \
	uninstall-ubuntu_mono_dark_iconDATA \
	uninstall-ubuntu_mono_light_iconDATA

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%files gtk
%defattr(-,root,root)
%{_bindir}/%{name}-gtk
%{_iconsdir}/hicolor/scalable/apps/%{name}*.svg
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}-gtk.appdata.xml
%{python_sitelib}/redshift_gtk/
%{_userunitdir}/*.service


