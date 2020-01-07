%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	boxes manager for GNOME
Name:		gnome-boxes
Version:	3.34.3
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
Url:		https://live.gnome.org/Boxes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-boxes/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	vala
BuildRequires:	vala-tools
BuildRequires:	vala-devel
BuildRequires:	tracker-devel
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(freerdp2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(spice-client-gtk-3.0)
BuildRequires:	pkgconfig(govirt-1.0)
BuildRequires:	pkgconfig(gtk-vnc-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:	pkgconfig(libosinfo-1.0)
BuildRequires:	pkgconfig(libvirt-gobject-1.0)
BuildRequires:	pkgconfig(libvirt-gconfig-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:	yelp-tools
BuildRequires:	meson
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	pkgconfig(tracker-sparql-2.0)
BuildRequires:	tracker-vala
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  libosinfo-vala

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
%autopatch -p1

%build
export CC=gcc
export CXX=g++
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS README.md NEWS TODO
%{_bindir}/%{name}
%{_libexecdir}/gnome-boxes-search-provider
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Boxes.appdata.xml
%{_datadir}/applications/org.gnome.Boxes.desktop
%{_datadir}/dbus-1/services/org.gnome.Boxes.service
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/gnome-boxes-search-provider.ini
%{_iconsdir}/hicolor/*/apps/org.gnome.Boxes.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Boxes-symbolic.svg
%{_includedir}/gnome-boxes/govf/*.h
%{_includedir}/gnome-boxes/gtk-frdp/*.h
%{_libdir}/gnome-boxes/libgovf-0.1.so
%{_libdir}/gnome-boxes/libgtk-frdp-0.1.so
%{_libdir}/gnome-boxes/pkgconfig
%{_libdir}/gnome-boxes/girepository-1.0/

