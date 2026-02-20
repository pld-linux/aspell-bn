Summary:	Bengali dictionary for aspell
Summary(pl.UTF-8):	Bengalski słownik dla aspella
Name:		aspell-bn
Version:	0.01.1
%define	subv	1
Release:	2
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/bn/aspell6-bn-%{version}-%{subv}.tar.bz2
# Source0-md5:	5ea70ec74e67f49b2844d306ddf38388
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bengali dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Bengalski słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-bn-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
