.include beta.uasm
.macro MYCALL(ra, rb) PUSH(ra) PUSH(rb) CALL(label, 2)
MYCALL(R1, R2)

label: 
    ADD(R1, R1, R1)
