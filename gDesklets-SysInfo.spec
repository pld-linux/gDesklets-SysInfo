%define	pname	SysInfo
Summary:	A sensor and a display for system status meters
Summary(pl):	Czujnik i wy¶wietlacz dla pomiarów stanu systemu
Name:		gDesklets-%{pname}
Version:	0.11
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/sysinfo-desklet-%{version}.tar.bz2
# Source0-md5:	ef1b78d4699c31a719a301db131580d8
URL:		http://www.pycage.de/software_gdesklets.html
Buildrequires:	python >= 2.3
Buildrequires:	python-pygtk >= 1.99.14
Requires:	gDesklets
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A sensor and a display for system status meters.

%description -l pl
Czujnik i wy¶wietlacz dla pomiarów stanu systemu.

%prep
%setup -q -n sysinfo-desklet-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gdesklets/{Sensors,Displays/%{pname}}

./Install_SysInfo_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors

cp -R gfx *.display $RPM_BUILD_ROOT%{_datadir}/gdesklets/Displays/%{pname}

rm -rf $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors/%{pname}/{CVS,gfx/CVS,.#*}

%py_comp $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors

rm -f $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/gdesklets/Sensors/*
%{_datadir}/gdesklets/Displays/*
