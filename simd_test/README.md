# SIMD test package

This package builds a small executable that uses AVX, AVX2, or NEON intrinsics
depending on the target architecture flags passed by rpmbuild.

After building, the RPM will contain:
- `/usr/bin/simd_test` — the test binary
- `/usr/share/simd_test/simd_test.disasm` — disassembly of the binary

The disassembly is also printed in the build log for inspection.
