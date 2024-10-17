Summary:	A GUI frontend for autotrace
Name: 		frontline
Version:	0.5.4
Release:	18
Group:		Graphics
License:	GPLv2+
Url:		https://autotrace.sourceforge.net/frontline

Source:		http://autotrace.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Source3:	%{name}.png
Patch0:		frontline-0.5.4-mdv-fix-str-fmt.patch
Patch1:		frontline-0.5.4-mdv-fix-linkage.patch

BuildRequires:	gnome-libs-devel
BuildRequires:	popt-devel
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(autotrace)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(pstoedit)
BuildRequires:	pkgconfig(ImageMagick)

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

%package -n %{name}-devel
Summary:	Frontline devel file
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description -n %{name}-devel
Frontline devel file.

%prep
%setup -q
%patch0 -p1 -b .strfmt
%patch1 -p1 -b .linkage

%build
%configure2_5x
make

%install
%makeinstall_std

%find_lang %{name}

# menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=FrontLine
Comment=A GUI frontend for autotrace
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Graphics;Graphics;
EOF

# icon
mkdir -p %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
install -m 644 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}%{_liconsdir}/%{name}.png
install -m 644 %{SOURCE3} %{buildroot}%{_iconsdir}/%{name}.png

rm -Rf %{buildroot}%{_libdir}/gimp/

%files -f %{name}.lang
%doc README NEWS AUTHORS TODO ChangeLog
%{_bindir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*
%{_datadir}/gnome/*/*/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png

%files -n %{name}-devel
%{_includedir}/*
%{_bindir}/%{name}-config
%{_libdir}/pkgconfig/*
%{_libdir}/*.a
%{_datadir}/aclocal/*

