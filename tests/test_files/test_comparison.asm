.include beta.uasm
CMOVE(-5, R1)
CMPLE(R31, R1, R0)
CMPLE(R1, R31, R2)
CMPLE(R1, R1, R3)
CMPLEC(R31, -1, R4)
HALT()