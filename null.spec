Summary: Dummy package
Name:    null
Version: 2.0
Release: 2
Group:   Development/Other
License: GPL

Source0: readme.tar.zst

BuildRequires: binutils
BuildRequires: cmake

BuildSystem: cmake

%description
A dummy package for testing purposes.

%package simd_test
Group:   Development/Other
Summary: SIMD test

%description simd_test
A small test program to verify SIMD instructions are emitted for the target.

%prep
%setup -T -D -a 0 -n .
cat readme.txt

cp -a %{_sourcedir}/simd_test/* .

%install -a
# Run objdump on the installed binary, save and print
mkdir -p %{buildroot}%{_datadir}/simd_test
objdump -d %{buildroot}%{_bindir}/simd_test | tee %{buildroot}%{_datadir}/simd_test/simd_test.disasm

%files
%doc readme.txt

%files simd_test
%doc README.md
%{_bindir}/simd_test
%{_datadir}/simd_test/simd_test.disasm
