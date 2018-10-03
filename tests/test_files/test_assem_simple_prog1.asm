.include beta.uasm

main:
    CMOVE(0, R1)
    CMOVE(10, R2)

main_loop:
    CMPLT(R1, R2, R0)
    BF(R0, main_end)
    ADDC(R1, 1, R1)
    BR(main_loop)

main_end:
    HALT()