%define name	redshift
%define version	1.6
%define rel	2

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:	Adjusts the color temperature of your screen according to time of day
Url:		http://jonls.dk/redshift/
Source:		http://launchpad.net/redshift/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
License:	GPLv3+
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	x11-server-devel
BuildRequires:	glib2-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	python-devel

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

%build
%configure2_5x \
	--disable-rpath \
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
%doc NEWS AUTHORS README 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%files gtk
%defattr(-,root,root)
%{_bindir}/gtk-%{name}
%{_iconsdir}/hicolor/scalable/apps/%{name}*.svg
%{_datadir}/applications/gtk-%{name}.desktop
%{python_sitelib}/gtk_redshift/
