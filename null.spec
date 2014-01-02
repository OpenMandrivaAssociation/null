%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Epoch:		1
Name:		null
Version:	2.1
Release:	82
Summary:	A dummy package for bs testing purpose
Group:		Development/Other
License:	GPL

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

%install
mkdir -p %{buildroot}

%post -p /bin/csh
echo "csh sux"

%files
%files dummy

