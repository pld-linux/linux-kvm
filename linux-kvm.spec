# TODO: use linux tarball when kernel 3.1 is released
%define	rel	31
%define	snap	20110726
Summary:	Native Linux KVM tool
Summary(pl.UTF-8):	Natywne narzędzie KVM dla Linuksa
Name:		linux-kvm
Version:	3.1
Release:	0.%{snap}.%{rel}
License:	GPL v2
Group:		Applications/System
# git://github.com/penberg/linux-kvm.git
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	b0b94a75d915f70ae14a089ddc7d7abb
Patch0:		fix-types.patch
BuildRequires:	binutils-devel
BuildRequires:	glibc-devel(ix86)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of this tool is to provide a clean, from-scratch, lightweight
KVM host tool implementation that can boot Linux guest images (just a
hobby, won't be big and professional like QEMU) with no BIOS
dependencies and with only the minimal amount of legacy device
emulation.

%description -l pl.UTF-8
Celem tego narzędzia jest dostarczenie czystej, lekkiej, napisanej od
zera implementacji hosta KVM, potrafiącego uruchamiać obrazy gościa
Linuksa (tylko hobby, nie będzie duża i profesjonalna jak QEMU) bez
zależności oD BIOS-u i z minimalną emulacją tradycyjnych urządzeń.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%{__make} -C tools/kvm \
	CC="%{__cc} %{rpmcppflags} %{rpmcflags} %{rpmldflags}" \
	WERROR=0 \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install tools/kvm/kvm $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc tools/kvm/Documentation/* tools/kvm/README
%attr(755,root,root) %{_sbindir}/kvm
