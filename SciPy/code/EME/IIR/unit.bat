rem iirband-f.pl and iirband.pl are identical
rem iirband-a.pl uses arrays for reversing rather than files.
rem perl iirband-a.pl 0.005 572 8192 unit.txt unit.out rem rings 350
rem perl iirband-a.pl 0.010 572 8192 unit.txt unit.out rem rings 180
perl iirband-a.pl 0.002 572 8192 unit.txt unit.out rem rings 900
rem perl ..\to-wvn_norm.pl iir.out ..\unkn422.wav > iir.wav
rem perl ..\to-wvn.pl iir.out 612728 ..\unkn422.wav > iir1b.wav
rem perl iirband.pl 0.001 572 8192 adapt1\qsig1.dat > iir.out
