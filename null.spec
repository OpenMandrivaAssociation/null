%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A dummy package for bs testing purpose
Name:		null
Version:	12
Release:	1.11
Epoch:		1
Group:		Development/Other
License:	GPL

Source0:	readme.tar.zst

%description
Dummy package.

%package dummy
Group:		Development/Other
Summary:	Test package

%description dummy
A dummy subpackage.

%prep
%setup -T -D -a 0 -n .

%build
cat readme.txt

%install
mkdir -p %{buildroot}

%post -p /bin/csh
echo "csh sux"

%files
%files dummy
