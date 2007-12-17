%define name frontline
%define version 0.5.4
%define release %mkrel 9

%define Summary A GUI frontend for autotrace
%define title Frontline
%define section Multimedia/Graphics

%define major 0
%define libname %mklibname frontline %major

Summary: 	%Summary
Name: 		%name
Version: 	%version
Release: 	%release
Group: 		Graphics
License: 	GPL
Url: 		http://autotrace.sourceforge.net/frontline

Source: http://autotrace.sourceforge.net/%name/%name-%version.tar.bz2
Source1:	%name-16.png
Source2:	%name-32.png
Source3:	%name.png


BuildRequires: gnome-libs-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libautotrace-devel
BuildRequires: libexif-devel
BuildRequires: libpstoedit-devel 
BuildRequires: ImageMagick-devel 
BuildRequires: libpopt-devel

Provides: %libname = %{version}-%{release}
Obsoletes: %libname

%description
Frontline provides a gtk+/gnome based GUI frontend for 
autotrace (http://autotrace.sourceforge.net) in 4 ways.

1. Stand alone program. A command `frontline' runs as a stand alone
   program. It will work well with Gnome desktop and nautilus.
   
2. Reusable library. A library `libfrontline.a' could be used as a
   building block of your application that needs the autotrace function.
   APIs are listed in frontline.h.  The stand alone program frontline
   itself uses libfrontline.a.

3. Sodipodi, a drawing editor add-on module. add-on module uses the 
   libfrontline.a. See below.

%package -n %name-devel
Summary: 	Frontline devel file
Requires:	%name = %version
Group: 		Development/C
Provides: %libname-devel = %{version}-%{release}
Obsoletes: %libname-devel

%description -n %name-devel
Frontline devel file.

#%package gimp
#Summary: Frontline plugin for GIMP
#Group: Graphics
#
#%description gimp
#Gimp plug-in. You can launch frontline from the GIMP's menu.
#Select "<Image>/Filters/Trace/Trace..." .
#
%prep
%setup -q

%build
%configure2_5x

make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/%name-config

%find_lang %name

# menu
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name << EOF
?package(%name): \
command="%_bindir/%name" \
needs="x11" \
icon="%name.png" \
section="%section" \
title="%title" \
longtitle="%Summary" \
xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=FrontLine
Comment=%{Summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Graphics;Graphics;
EOF

# icon
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/%name.png

rm -Rf $RPM_BUILD_ROOT/%{_libdir}/gimp/

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS TODO ChangeLog
%_bindir/%name
%_datadir/pixmaps/*
%_datadir/mime-info/*
%_datadir/gnome/*/*/*
%_datadir/applications/mandriva-%{name}.desktop
%_menudir/%name
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png

%files -n %name-devel
%defattr(-,root,root)
%_includedir/*
%_bindir/%name-config
%multiarch %{multiarch_bindir}/%name-config
%_libdir/pkgconfig/*
%_libdir/*.a
%_datadir/aclocal/*

#%files gimp
#%defattr(-,root,root)
#%{_libdir}/gimp/*/plug-ins/*
#


