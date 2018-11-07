.macro WORD(x) x%0x100 (x>>8)%0x100
.macro LONG(x) WORD(x) WORD(x >> 16)	| little-endian for Maybe
.macro STORAGE(NWORDS)	. = .+(4*NWORDS)| Reserve NWORDS words of RAM
.macro betaopc(OP,RA,CC,RC) {
      .align 4
      LONG((OP<<26)+((RC%0x20)<<21)+((RA%0x20)<<16)+(CC%0x10000)) }
r31 = 31
.macro BETABR(OP,RA,RC,LABEL)	betaopc(OP,RA,((LABEL-.)>>2)-1, RC)
.macro BEQ(RA, LABEL, RC)	BETABR(0x1D,RA,RC,LABEL)
.macro BEQ(RA, LABEL)		BETABR(0x1D,RA,r31,LABEL)
.macro BF(RA, LABEL, RC)	BEQ(RA,LABEL,RC)
.macro BF(RA,LABEL)		BEQ(RA,LABEL)
.macro BNE(RA, LABEL, RC)	BETABR(0x1E,RA,RC,LABEL)
.macro BNE(RA, LABEL)		BETABR(0x1E,RA,r31,LABEL)
.macro BT(RA,LABEL,RC)		BNE(RA,LABEL,RC)
.macro BT(RA,LABEL)		BNE(RA,LABEL)
.macro BR(LABEL,RC)		BEQ(r31, LABEL, RC)
.macro BR(LABEL)		BR(LABEL, r31)

BR(label1)
label1:
    BR(label2, 26)
    STORAGE(1)
label2:
    BR(label3)
    STORAGE(255)
label3:
