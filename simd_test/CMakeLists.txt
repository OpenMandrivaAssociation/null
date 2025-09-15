cmake_minimum_required(VERSION 3.10)

project(simd_test CXX)

include(CheckCXXSourceCompiles)

# Detect AVX (V1)
check_cxx_source_compiles("
#ifndef __AVX__
#error No AVX
#endif
int main() { return 0; }" HAS_AVX)

# Detect AVX2
check_cxx_source_compiles("
#ifndef __AVX2__
#error No AVX2
#endif
int main() { return 0; }" HAS_AVX2)

# Detect NEON
check_cxx_source_compiles("
#ifndef __ARM_NEON
#error No NEON
#endif
int main() { return 0; }" HAS_NEON)

add_executable(simd_test main.cpp sink.cpp)

if(HAS_AVX2)
	message(STATUS "Target supports AVX2 — enabling AVX2 intrinsics")
	target_compile_definitions(simd_test PRIVATE USE_AVX2)
elseif(HAS_AVX)
	message(STATUS "Target supports AVX (V1) — enabling AVX intrinsics")
	target_compile_definitions(simd_test PRIVATE USE_AVX)
elseif(HAS_NEON)
	message(STATUS "Target supports NEON — enabling NEON intrinsics")
	target_compile_definitions(simd_test PRIVATE USE_NEON)
else()
	message(STATUS "No advanced SIMD detected for target")
endif()

install(TARGETS simd_test
	RUNTIME DESTINATION bin
)
