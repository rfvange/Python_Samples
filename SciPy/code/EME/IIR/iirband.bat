rem iirband-f.pl and iirband.pl are identical
rem iirband-a.pl uses arrays for reversing rather than files.
perl iirband-a.pl 0.005 572 8192 ..\unkn422-1.out iir.out
perl ..\to-wvn_norm.pl iir.out ..\unkn422.wav > iir.wav
rem perl ..\to-wvn.pl iir.out 612728 ..\unkn422.wav > iir1b.wav
rem perl iirband.pl 0.001 572 8192 adapt1\qsig1.dat > iir.out
rem 0.001 -> 8.192 Hz, 0.005 -> 44.5 Hz, etc.