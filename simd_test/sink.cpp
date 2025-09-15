#include "sink.h"

#if defined(USE_NEON)
volatile float sink_sum[4];
volatile float sink_prod[4];
#else
volatile double sink_sum[4];
volatile double sink_prod[4];
#endif
