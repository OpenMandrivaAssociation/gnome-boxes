Summary:	boxes manager for GNOME
Name:		gnome-boxes
Version:	3.4.2
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
URL:		https://live.gnome.org/Boxes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-boxes/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	vala >= 0.13.0
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.1
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0) => 2.29.90
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.3.5
BuildRequires:	pkgconfig(gtk-vnc-2.0) >= 0.4.4
BuildRequires:	pkgconfig(libvirt-gobject-1.0) >= 0.0.7
BuildRequires:	pkgconfig(libvirt-gconfig-1.0) >= 0.0.7
BuildRequires:	pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:	pkgconfig(spice-client-gtk-3.0) >= 0.9
BuildRequires:	pkgconfig(gudev-1.0) >= 167
BuildRequires:	pkgconfig(libosinfo-1.0) >= 0.1.1
BuildRequires:	tracker-devel
# XXX - libvirtd service should be running
Requires:	libvirt-utils
Requires:	qemu-img
Requires:	qemu
# Needed for unattended installer:
Requires:	mtools
Requires:	fuseiso
# gnome-boxes uses a dark theme
Requires: gnome-icon-theme

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
%{_iconsdir}/hicolor/*/apps/gnome-boxes.*

