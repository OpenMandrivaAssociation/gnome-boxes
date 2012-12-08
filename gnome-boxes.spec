Summary:	boxes manager for GNOME
Name:		gnome-boxes
Version:	3.6.1
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
URL:		https://live.gnome.org/Boxes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-boxes/3.6/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	vala
BuildRequires:	vala-tools
BuildRequires:	tracker-devel
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk-vnc-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libosinfo-1.0)
BuildRequires:	pkgconfig(libvirt-gobject-1.0)
BuildRequires:	pkgconfig(libvirt-gconfig-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(spice-client-gtk-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
# XXX - libvirtd service should be running
Requires:	libvirt-utils
Requires:	qemu-img
Requires:	qemu
# Needed for unattended installer:
Requires:	mtools
Requires:	fuseiso
# gnome-boxes uses a dark theme
Requires:	gnome-icon-theme

%description
Standalone boxes manager for GNOME desktop.

%prep
%setup -q

# add semicolon after mimetype (will be fixed in 3.3.3!)
sed -i -e 's,^\(MimeType=.*[^;]\)$,\1;,g' data/gnome-boxes.desktop.in.in

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README NEWS TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%{_libexecdir}/gnome-boxes-search-provider
%{_datadir}/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/gnome-boxes-search-provider.ini
%{_iconsdir}/hicolor/*/apps/gnome-boxes.*


%changelog
* Wed Oct 17 2012 Arkady L. Shane <ashejn@rosalinux.ru> 3.6.1-1
- update to 3.6.1

* Mon Jun 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.3-1
+ Revision: 804394
- new version 3.4.3
- spec clean ups

* Thu May 17 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 799336
- update to new version 3.4.2

* Sat May 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.1-1
+ Revision: 796460
- BR:GL-devel
- BR:tracker-devel
- mkdrel macro removed
- imported package gnome-boxes

