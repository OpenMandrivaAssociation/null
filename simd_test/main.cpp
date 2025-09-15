#include "sink.h"

#include <cstdio>
#include <ctime>

#if defined(USE_AVX2) || defined(USE_AVX)
#include <immintrin.h>
#elif defined(USE_NEON)
#include <arm_neon.h>
#else
#include <algorithm>
#endif

static inline double runtime_seed() {
	// Always runtime: depends on current time
	return 1.0 + double(std::time(nullptr) & 7);
}

int main() {
#if defined(USE_AVX2)
	__m256d a = _mm256_set_pd(1.0, 2.0, 3.0, 4.0);
	__m256d b = _mm256_set1_pd(runtime_seed());
	__m256d sum  = _mm256_add_pd(a, b);   // vaddpd
	__m256d prod = _mm256_mul_pd(a, b);   // vmulpd
	_mm256_storeu_pd((double *)sink_sum, sum);
	_mm256_storeu_pd((double *)sink_prod, prod);
#elif defined(USE_AVX)
	__m128d a = _mm_set_pd(1.0, 2.0);
	__m128d b = _mm_set1_pd(runtime_seed());
	__m128d sum  = _mm_add_pd(a, b);	  // vaddpd (128-bit)
	__m128d prod = _mm_mul_pd(a, b);	  // vmulpd (128-bit)
	_mm_storeu_pd((double *)sink_sum, sum);
	_mm_storeu_pd((double *)sink_prod, prod);
#elif defined(USE_NEON)
	float32x4_t a = {1.f, 2.f, 3.f, 4.f};
	float32x4_t b = vdupq_n_f32((float)runtime_seed());
	float32x4_t sum  = vaddq_f32(a, b);   // fadd
	float32x4_t prod = vmulq_f32(a, b);   // fmul
	vst1q_f32((float *)sink_sum, sum);
	vst1q_f32((float *)sink_prod, prod);
#else
	std::fill_n(sink_sum, 4, 0.0);
	std::fill_n(sink_prod, 4, 0.0);

	std::puts("No SIMD path compiled.");
#endif
	// Consume the sink so the compiler must keep the stores
	std::printf("%f\n", sink_sum[0]);
	std::printf("%f\n", sink_prod[1]);
}
