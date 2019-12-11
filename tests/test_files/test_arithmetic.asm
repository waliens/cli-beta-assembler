.include beta.uasm
CMOVE(-10, R1)
CMOVE(8, R2)
ADDC(R1, 8, R10)  | -2
ADD(R1, R2, R11)  | -2
SUBC(R1, 8, R12)  | -18
SUB(R1, R2, R13)  | -18
MULC(R1, 8, R14)  | -80
MUL(R1, R2, R15)  | -80
DIVC(R1, 8, R16)  | -1
DIV(R1, R2, R17)  | -1

HALT()