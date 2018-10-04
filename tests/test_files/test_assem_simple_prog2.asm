.include beta.uasm

CMOVE(stack__, SP)
MOVE(SP, BP)
BR(main)

sum:
    PUSH(LP) PUSH(BP)
    MOVE(SP, BP)
    PUSH(R1) PUSH(R2)
    LD(BP, -12, R1)
    LD(BP, -16, R2)
    ADD(R1, R2, R0)
    POP(R2) POP(R1)
    POP(BP) POP(LP)
    RTN()

main:
    CMOVE(0, R1)
    CMOVE(10, R2)
    CMOVE(0, R3)

main_loop:
    CMPLT(R1, R2, R0)
    BF(R0, main_end)
    ADDC(R1, 1, R1)
    PUSH(R3) PUSH(R1)
    CALL(sum, 2)
    MOVE(R0, R3)
    BR(main_loop)

main_end:
    HALT()


LONG(0xDEADCAFE)
stack__:
