%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Remote
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Retrieve information on remote image files
Summary(pl):	%{_class}_%{_subclass} - otrzymywanie informacji o zdalnych rysunkach
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class can be used for retrieving size information of remote image
files via http without downloading the whole image.

%description -l pl
Dzieki tej klasie mo¿na uzyskaæ informacje o zdalnym obrazku poprzez
http bez ¶ci±gania ca³ego rysunku.

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
