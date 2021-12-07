global _start
section .text

_start:
    mov eax, [num1]
    mov edx, [num2]
    add eax, edx

l1:
    sub eax, 0x00000002
    jnz l1

    xor edx, edx        ; clear the edx register.
    syscall             ; syscall to exit

section .data
        num1: dd 0x80000001
        num2: dd 0x80000005