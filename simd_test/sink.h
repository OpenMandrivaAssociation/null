#pragma once

#if defined(USE_NEON)
extern volatile float sink_sum[4];
extern volatile float sink_prod[4];
#else
extern volatile double sink_sum[4];
extern volatile double sink_prod[4];
#endif
