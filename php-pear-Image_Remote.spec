%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Remote
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Retrieve information on remote image files
Summary(pl):	%{_pearname} - otrzymywanie informacji o zdalnych rysunkach
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	f7baae627bdec430e1d7aad9cda66ecf
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class can be used for retrieving size information of remote image
files via http without downloading the whole image.

This class has in PEAR status: %{_status}

%description -l pl
Dzieki tej klasie mo�na uzyska� informacje o zdalnym obrazku poprzez
http bez �ci�gania ca�ego rysunku.

Ta klasa ma w PEAR status: %{_status}

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php