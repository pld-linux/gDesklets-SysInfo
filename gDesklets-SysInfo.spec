%define	pname	SysInfo
Summary:	A sensor and a display for system status meters
Summary(pl):	Czujnik i wy¶wietlacz dla pomiarów stanu systemu
Name:		gDesklets-%{pname}
Version:	0.25
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname}-%{version}.tar.bz2
# Source0-md5:	6d6c6c21b0f73227c33649d07a88b4c6
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=56
BuildRequires:	python >= 2.3
BuildRequires:	python-pygtk >= 2.0.0
Requires:	gDesklets
Requires:	python-gnome-vfs
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sensorsdir	%{_datadir}/gdesklets/Sensors
%define	_displaysdir	%{_datadir}/gdesklets/Displays

%description
A sensor and a display for system status meters.

%description -l pl
Czujnik i wy¶wietlacz dla pomiarów stanu systemu.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_SysInfo_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

rm -rf %{pname}/gfx/CVS
cp -R %{pname}/{gfx,*.display} $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{pname}/ChangeLog
%{_displaysdir}/*
%dir %{_sensorsdir}/%{pname}
%{_sensorsdir}/%{pname}/*.py[co]
%lang(ca) %{_sensorsdir}/%{pname}/locale/ca
%lang(cs) %{_sensorsdir}/%{pname}/locale/cs
%lang(de) %{_sensorsdir}/%{pname}/locale/de
%lang(es) %{_sensorsdir}/%{pname}/locale/es
%lang(fr) %{_sensorsdir}/%{pname}/locale/fr
%lang(nl) %{_sensorsdir}/%{pname}/locale/nl
%lang(pt) %{_sensorsdir}/%{pname}/locale/pt
%lang(pt_BR) %{_sensorsdir}/%{pname}/locale/pt_BR
%lang(sq) %{_sensorsdir}/%{pname}/locale/sq
%lang(sr) %{_sensorsdir}/%{pname}/locale/sr
%lang(sr@Latn) %{_sensorsdir}/%{pname}/locale/sr@Latn
%lang(sv) %{_sensorsdir}/%{pname}/locale/sv
