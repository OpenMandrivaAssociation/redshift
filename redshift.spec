%define name	redshift
%define version	1.7

Name:		%{name}
Version:	%{version}
Release:	3
Summary:	Adjusts the color temperature of your screen according to time of day
Url:		http://jonls.dk/redshift/
Source:		http://launchpad.net/redshift/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
License:	GPLv3+
Group:		Graphical desktop/Other
BuildRequires:	x11-server-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	python-devel
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


%changelog
* Thu Dec 01 2011 Andrey Bondrov <abondrov@mandriva.org> 1.7-1
+ Revision: 735917
- New version 1.7

* Sat Oct 30 2010 Jani Välimaa <wally@mandriva.org> 1.6-2mdv2011.0
+ Revision: 590582
- rebuild for new python 2.7
- drop py_requires macro

* Mon Oct 18 2010 Jani Välimaa <wally@mandriva.org> 1.6-1mdv2011.0
+ Revision: 586676
- new version 1.6
- fix file list

* Sat Aug 21 2010 Jani Välimaa <wally@mandriva.org> 1.5-1mdv2011.0
+ Revision: 571775
- new version 1.5
- disable rpath
- use provided .desktop file

* Tue Jul 13 2010 Jani Välimaa <wally@mandriva.org> 1.4.1-3mdv2011.0
+ Revision: 552777
- use a fully versioned dependency in subpackage

* Sat Jul 10 2010 Jani Välimaa <wally@mandriva.org> 1.4.1-2mdv2011.0
+ Revision: 550503
- split GTK stuff to a separate package

* Wed Jun 23 2010 Jani Välimaa <wally@mandriva.org> 1.4.1-1mdv2011.0
+ Revision: 548748
- import redshift


