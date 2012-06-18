Next step:

Design a narrow DC filter, ifft, window it (Blackman), translate it to 576 Hz.
This is the filter kernel.  Correlate it with the unk422_af9y.out
to get a filtered unk422_af9y_filt.out.  Correlate with af9y_xx.out signal.

Filter the af9y signal with a "dot" that has been windowed.  This will make sure the full bandwidth of a call
sign will fit in the bandwidth. This creates a new unkn422-1_9y_filt.out.

Use Blackman.

Blackman window (slower rolloff, better stopband: -80dB): A smooth curve used in the
design of filters and spectral analysis, calculated
from : 0.42 - 0.5cos(2*pi*n/M) + 0.08cos(4*pi*n/M),
where n runs from 0 to M.

Hamming window (faster rolloff, less stopband: -60dB): A smooth curve used in the
design of filters and spectral analysis, calculated
from: 0.54 - 0.46cos(2*pi*n/M), where n runs from
0 to M.

Old xxxxx

Run with 60 & 65 ke0b and see which one has the least response.  That's the one you choose.

Freq = 567 Hz
Divide by noise freq.

Take FFT of signal, make conj(), and divide by abs val of noise freq.
This is the matched filter.
Multiply by the signal.
The inverse will be the correlation.
Probably not worth doing because most of the noise is around the signal freq.