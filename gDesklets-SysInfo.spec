%define	pname	SysInfo
%define	pver	0_1
Summary:	A sensor and a display for system status meters
Summary(pl):	Czujnik i wy¶wietlacz dla pomiarów stanu systemu
Name:		gDesklets-%{pname}
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/%{pname}-%{pver}.tar.bz2
# Source0-md5:	c2aa7c36b9bd78701ce0c20b3dd6abff
URL:		http://www.pycage.de/software_gdesklets.html
Buildrequires:	python >= 2.3
Requires:	gDesklets
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A sensor and a display for system status meters.

%description -l pl
Czujnik i wy¶wietlacz dla pomiarów stanu systemu.

%prep
%setup -q -n %{pname}
tail -c 20480 Install_SysInfo_Sensor.bin 2>&1 | tar -xz 2>&1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gdesklets/{Sensors,Displays/%{pname}}

cp -R SysInfo $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors
cp -R gfx *.display $RPM_BUILD_ROOT%{_datadir}/gdesklets/Displays/%{pname}

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
