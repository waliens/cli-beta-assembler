.macro WORD(x) x%0x100 (x>>8)%0x100
.macro LONG(x) WORD(x) WORD(x >> 16)	| little-endian for Maybe
.macro A(a) { LONG(a + .) }

A(250)
A(250)
A(250)
A(250)
A(250)
A(250)
A(250)
A(250)
A(250)
A(250)

LONG(250)