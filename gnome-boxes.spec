%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	boxes manager for GNOME
Name:		gnome-boxes
Version:	40.1
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
BuildRequires:  pkgconfig(gtksourceview-4)
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
BuildRequires:	pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(tracker-sparql-3.0)
BuildRequires:	tracker-vala
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  libosinfo-vala
BuildRequires:  typelib(Handy)
BuildRequires:  appstream-util

# XXX - libvirtd service should be running
Requires:	libvirt-utils
Requires:	qemu-img
Requires:	qemu
Requires: qemu-kvm
Recommends: qemu-system-x86
Requires: tracker
# Needed for unattended installer:
Requires:	mtools
Requires:	fuseiso
# gnome-boxes uses a dark theme
Requires:	gnome-icon-theme

%description
Standalone boxes manager for GNOME desktop.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

# Remove unneeded development files
rm -rf %{buildroot}%{_includedir}/gnome-boxes/
rm -rf %{buildroot}%{_libdir}/gnome-boxes/girepository-1.0/
rm -rf %{buildroot}%{_libdir}/gnome-boxes/pkgconfig/
rm -rf %{buildroot}%{_datadir}/gnome-boxes/gir-1.0/
rm -rf %{buildroot}%{_datadir}/gnome-boxes/vapi/

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS README.md NEWS
%{_bindir}/%{name}
%{_libexecdir}/gnome-boxes-search-provider
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Boxes.appdata.xml
%{_datadir}/applications/org.gnome.Boxes.desktop
%{_datadir}/dbus-1/services/org.gnome.Boxes.service
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Boxes.SearchProvider.ini
%{_iconsdir}/hicolor/*/apps/org.gnome.Boxes.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Boxes-symbolic.svg
%{_libdir}/gnome-boxes/libgovf-0.1.so
#{_libdir}/gnome-boxes/libgtk-frdp-0.1.so
