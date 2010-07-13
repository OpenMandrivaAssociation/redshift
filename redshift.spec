%define name	redshift
%define version	1.4.1
%define rel	3

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

%package gtk
Summary:	GTK integration for Redshift
Group:		Graphical desktop/Other
%py_requires
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
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std \
	uninstall-ubuntu_mono_dark_iconDATA \
	uninstall-ubuntu_mono_light_iconDATA

#desktop file
mkdir -p %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Redshift
Comment=Adjusts the color temperature of your screen
Exec=gtk-redshift
Terminal=false
Type=Application
Icon=%{name}
Categories=Utility;
EOF

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS AUTHORS README 
%{_bindir}/%{name}

%files gtk
%defattr(-,root,root)
%{_bindir}/gtk-%{name}
%{_iconsdir}/hicolor/scalable/apps/%{name}*.svg
%{_datadir}/applications/%{name}.desktop
%{python_sitelib}/gtk_redshift/
