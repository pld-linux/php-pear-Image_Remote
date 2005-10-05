%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Remote
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Retrieve information on remote image files
Summary(pl):	%{_pearname} - otrzymywanie informacji o zdalnych rysunkach
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
#Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Source0:	%{_pearname}-%{version}.tgz
# Source0-md5:	492f387fc4c2a9dff4ac3baa78d7c133
URL:		http://pear.php.net/package/Image_Remote/
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class can be used for retrieving size information of remote image
files via HTTP without downloading the whole image.

In PEAR status of this package is: %{_status}.

%description -l pl
Dzieki tej klasie mo¿na uzyskaæ informacje o zdalnym obrazku poprzez
HTTP bez ¶ci±gania ca³ego rysunku.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
