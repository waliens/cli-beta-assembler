.include test_import_file2.asm
ADD(1,2,3)
Z+1.macro ADD(a,b,c) a b c a+a b+b c+c
Z = 1