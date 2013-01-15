Summary:	A GTK+ theme engine that uses Qt4 for drawing
Summary(pl.UTF-8):	Silnik graficzny wykorzystujący Qt4 do rysowania kontrolek GTK+
Name:		gtk2-theme-engine-qt4
Version:	1.1
Release:	2
License:	GPL
Group:		Themes/GTK+
Source0:	http://gtk-qt-engine.googlecode.com/files/gtk-qt-engine-%{version}.tar.bz2
# Source0-md5:	de8048baef7dfe6c97cd97c463d66152
Patch0:		%{name}-build.patch
URL:		http://code.google.com/p/gtk-qt-engine/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtSvg-devel
BuildRequires:	cmake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	kde4-kdebase-devel
BuildRequires:	kde4-kdebase-workspace-devel
BuildRequires:	libbonoboui-devel
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This GTK+ theme engine uses the currently selected Qt4 style to do
it's drawing. Basically, it makes your GTK+ apps look like Qt4 ones.

%description -l pl.UTF-8
Ten silnik graficzny do rysowania kontrolek GTK+ używa aktualnie
wybranego stylu Qt4. Inaczej mówiąc - sprawia, że aplikacje GTK+
wyglądają jak aplikacje Qt4.

%prep
%setup -q -n gtk-qt-engine
%patch0 -p1

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/kde4/services
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# proper category
sed -i 's/Categories=.*/Categories=X-KDE-settings-looknfeel;/' \
	$RPM_BUILD_ROOT%{_desktopdir}/kde4/kcmgtk4.desktop

mv $RPM_BUILD_ROOT%{_desktopdir}/kde4/kcmgtk4.desktop \
	$RPM_BUILD_ROOT%{_datadir}/kde4/services
rm -rf $RPM_BUILD_ROOT%{_desktopdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la

%find_lang gtkqtengine --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gtkqtengine.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/Qt4
%{_datadir}/kde4/services/kcmgtk4.desktop
%{_iconsdir}/*.png
%attr(755,root,root) %{_libdir}/kde4/kcm_gtk4.so
