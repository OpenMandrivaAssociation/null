%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A dummy package for bs testing purpose
Name:		null
Version:	2.2
Release:	1.5
Epoch:		1
Group:		Development/Other
License:	GPL
Buildrequires: clang
%description
Dummy package.

%package dummy
Group:		Development/Other
Summary:	Test package

%description dummy
A dummy subpackage.

%prep
%setup -D -T -n .

%build
echo __GNUC__ | /usr/bin/clang -E -

%install
mkdir -p %{buildroot}

%post -p /bin/csh
echo "csh sux"

%files
%files dummy

