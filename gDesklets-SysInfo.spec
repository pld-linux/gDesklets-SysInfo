%define	pname	SysInfo
Summary:	A sensor and a display for system status meters
Summary(pl):	Czujnik i wy¶wietlacz dla pomiarów stanu systemu
Name:		gDesklets-%{pname}
Version:	0.20
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname}-%{version}.tar.bz2
# Source0-md5:	56227e4f5d2d648d0e94ad38ca6473b4
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=39
Buildrequires:	python >= 2.3
Buildrequires:	python-pygtk >= 2.0.0
Requires:	gDesklets
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
%setup -q -c -n %{pname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_sysinfo_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

cp -R %{pname}/{gfx,*.display} $RPM_BUILD_ROOT%{_displaysdir}/%{pname}
mv $RPM_BUILD_ROOT%{_sensorsdir}/sysinfo $RPM_BUILD_ROOT%{_sensorsdir}/SysInfo

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sensorsdir}/*
%{_displaysdir}/*
