%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	boxes manager for GNOME
Name:		gnome-boxes
Version:	48.0
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
Url:		https://live.gnome.org/Boxes
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gnome-boxes/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  appstream-util
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:  spice-gtk
BuildRequires:	vala
BuildRequires:	vala-tools
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(tinysparql-3.0)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(freerdp2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:	pkgconfig(spice-client-gtk-3.0)
BuildRequires:	pkgconfig(govirt-1.0)
BuildRequires:	pkgconfig(gtk-vnc-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libvirt-gconfig-1.0)
# Workaround
BuildRequires:  gtk-vnc
BuildRequires:  gtk-vnc-common
BuildRequires:  typelib(SpiceClientGtk)
BuildRequires:  %{_lib}spice-client-gtk3.0_5
BuildRequires:  %{_lib}gtk-vnc-gir2.0
BuildRequires:  %{_lib}gtk-vnc2.0-devel
BuildRequires:  %{_lib}gtk-vnc2.0_0
BuildRequires:  %{_lib}gvnc-gir1.0
BuildRequires:  %{_lib}gvnc1.0-devel
BuildRequires:  %{_lib}gvnc1.0_0
BuildRequires:  %{_lib}vncpulse-gir1.0
BuildRequires:  %{_lib}vncpulse1.0_0
BuildRequires:  pkgconfig(gvncpulse-1.0)

BuildRequires:  pkgconfig(libarchive)
BuildRequires:	pkgconfig(libosinfo-1.0)
BuildRequires:	pkgconfig(libvirt-gobject-1.0)
BuildRequires:	pkgconfig(libvirt-gconfig-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:	yelp-tools
BuildRequires:	meson
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(tinysparql-3.0)
BuildRequires:	tinysparql-vala
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  libosinfo-vala
BuildRequires:  typelib(Handy)
BuildRequires:  appstream-util

# XXX - libvirtd service should be running
Requires:	libvirt-utils
Requires:	qemu-img
Requires:	qemu
Requires: qemu-kvm
Requires: qemu-audio-spice
Recommends: qemu-system-x86
Requires: tinysparql
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
export CC=gcc
export CXX=g++
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
%doc README.md NEWS
%{_bindir}/%{name}
%{_libexecdir}/gnome-boxes-search-provider
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Boxes.metainfo.xml
%{_datadir}/applications/org.gnome.Boxes.desktop
%{_datadir}/dbus-1/services/org.gnome.Boxes.service
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Boxes.SearchProvider.ini
%{_iconsdir}/hicolor/*/apps/org.gnome.Boxes.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Boxes-symbolic.svg
%{_libdir}/gnome-boxes/libgovf-0.1.so
#{_libdir}/gnome-boxes/libgtk-frdp-0.1.so
