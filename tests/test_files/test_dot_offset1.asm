.include beta.uasm

CMOVE(stack__, SP)
MOVE(SP, BP)
BR(main)

STORAGE(256)

main:
    ADDC(R1, 1, R1)
    HALT()

stack__:
    |;