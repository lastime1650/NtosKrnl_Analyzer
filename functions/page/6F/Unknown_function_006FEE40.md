# sub_006FEE40

- RVA: `0x006FEE40`–`0x006FF208` (길이 `968` bytes)
- VA: `0x00000001406FEE40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060300`
- 디코드: `287`개 명령, `968/968` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006FEF31` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006FEF5B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006FEFC6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006FF146` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x006FF1E0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A859`

### Static image references
- `0x006FEF48` → RVA `0x00FD8338` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x006FEF31` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x006FEF5B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x006FEFC6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x006FF146` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x006FF1E0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006FEE40  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
006FEE45  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
006FEE4A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
006FEE4F  57                              push rdi
006FEE50  41 56                           push r14
006FEE52  41 57                           push r15
006FEE54  48 83 EC 20                     sub rsp, 0x20
006FEE58  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
006FEE5C  49 8B F9                        mov rdi, r9
006FEE5F  48 8B F2                        mov rsi, rdx
006FEE62  4C 8B C9                        mov r9, rcx
006FEE65  4D 85 C0                        test r8, r8
006FEE68  74 52                           je 0x1406feebc
006FEE6A  83 39 03                        cmp dword ptr [rcx], 3
006FEE6D  76 4D                           jbe 0x1406feebc
006FEE6F  49 8B C0                        mov rax, r8
006FEE72  33 D2                           xor edx, edx
006FEE74  44 8B 10                        mov r10d, dword ptr [rax]
006FEE77  48 8D 48 04                     lea rcx, [rax + 4]
006FEE7B  83 FA 03                        cmp edx, 3
006FEE7E  73 1A                           jae 0x1406fee9a
006FEE80  48 3B C8                        cmp rcx, rax
006FEE83  0F 82 5E 03 00 00               jb 0x1406ff1e7
006FEE89  4A 8D 04 11                     lea rax, [rcx + r10]
006FEE8D  48 3B C1                        cmp rax, rcx
006FEE90  0F 82 51 03 00 00               jb 0x1406ff1e7
006FEE96  FF C2                           inc edx
006FEE98  EB DA                           jmp 0x1406fee74
006FEE9A  48 3B C8                        cmp rcx, rax
006FEE9D  0F 82 44 03 00 00               jb 0x1406ff1e7
006FEEA3  33 ED                           xor ebp, ebp
006FEEA5  45 85 D2                        test r10d, r10d
006FEEA8  48 0F 45 E9                     cmovne rbp, rcx
006FEEAC  41 83 FA 08                     cmp r10d, 8
006FEEB0  75 54                           jne 0x1406fef06
006FEEB2  41 83 39 04                     cmp dword ptr [r9], 4
006FEEB6  48 8B 6D 00                     mov rbp, qword ptr [rbp]
006FEEBA  77 0A                           ja 0x1406feec6
006FEEBC  BB 0D 00 00 C0                  mov ebx, 0xc000000d
006FEEC1  E9 26 03 00 00                  jmp 0x1406ff1ec
006FEEC6  33 D2                           xor edx, edx
006FEEC8  45 8B 08                        mov r9d, dword ptr [r8]
006FEECB  49 8D 48 04                     lea rcx, [r8 + 4]
006FEECF  83 FA 04                        cmp edx, 4
006FEED2  73 1A                           jae 0x1406feeee
006FEED4  49 3B C8                        cmp rcx, r8
006FEED7  0F 82 0A 03 00 00               jb 0x1406ff1e7
006FEEDD  4E 8D 04 09                     lea r8, [rcx + r9]
006FEEE1  4C 3B C1                        cmp r8, rcx
006FEEE4  0F 82 FD 02 00 00               jb 0x1406ff1e7
006FEEEA  FF C2                           inc edx
006FEEEC  EB DA                           jmp 0x1406feec8
006FEEEE  49 3B C8                        cmp rcx, r8
006FEEF1  0F 82 F0 02 00 00               jb 0x1406ff1e7
006FEEF7  33 C0                           xor eax, eax
006FEEF9  45 85 C9                        test r9d, r9d
006FEEFC  48 0F 45 C1                     cmovne rax, rcx
006FEF00  41 83 F9 04                     cmp r9d, 4
006FEF04  74 0A                           je 0x1406fef10
006FEF06  BB 23 00 00 C0                  mov ebx, 0xc0000023
006FEF0B  E9 DC 02 00 00                  jmp 0x1406ff1ec
006FEF10  B9 08 10 00 00                  mov ecx, 0x1008
006FEF15  39 08                           cmp dword ptr [rax], ecx
006FEF17  74 0A                           je 0x1406fef23
006FEF19  BB 3E 00 00 C0                  mov ebx, 0xc000003e
006FEF1E  E9 C9 02 00 00                  jmp 0x1406ff1ec
006FEF23  48 8B D1                        mov rdx, rcx
006FEF26  41 B8 53 4C 53 20               mov r8d, 0x20534c53
006FEF2C  B9 00 01 00 00                  mov ecx, 0x100
006FEF31  E8 BA 31 48 00                  call 0x140b820f0
006FEF36  4C 8B F8                        mov r15, rax
006FEF39  48 85 C0                        test rax, rax
006FEF3C  75 0A                           jne 0x1406fef48
006FEF3E  BB 17 00 00 C0                  mov ebx, 0xc0000017
006FEF43  E9 A4 02 00 00                  jmp 0x1406ff1ec
006FEF48  48 8B 05 E9 93 8D 00            mov rax, qword ptr [rip + 0x8d93e9]
006FEF4F  48 85 C0                        test rax, rax
006FEF52  0F 84 7E 02 00 00               je 0x1406ff1d6
006FEF58  49 8B CF                        mov rcx, r15
006FEF5B  E8 70 BB FB FF                  call 0x1406baad0
006FEF60  8B D8                           mov ebx, eax
006FEF62  85 C0                           test eax, eax
006FEF64  0F 88 71 02 00 00               js 0x1406ff1db
006FEF6A  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
006FEF6D  8B 56 20                        mov edx, dword ptr [rsi + 0x20]
006FEF70  05 40 10 00 00                  add eax, 0x1040
006FEF75  3D 40 10 00 00                  cmp eax, 0x1040
006FEF7A  0F 82 4F 02 00 00               jb 0x1406ff1cf
006FEF80  8D 48 04                        lea ecx, [rax + 4]
006FEF83  44 8B F3                        mov r14d, ebx
006FEF86  3B C8                           cmp ecx, eax
006FEF88  0F 82 41 02 00 00               jb 0x1406ff1cf
006FEF8E  8D 04 11                        lea eax, [rcx + rdx]
006FEF91  BE 95 00 00 C0                  mov esi, 0xc0000095
006FEF96  3B C1                           cmp eax, ecx
006FEF98  1B DB                           sbb ebx, ebx
006FEF9A  23 DE                           and ebx, esi
006FEF9C  0F 8C 39 02 00 00               jl 0x1406ff1db
006FEFA2  48 85 FF                        test rdi, rdi
006FEFA5  75 0A                           jne 0x1406fefb1
006FEFA7  BB 0D 00 00 C0                  mov ebx, 0xc000000d
006FEFAC  E9 2A 02 00 00                  jmp 0x1406ff1db
006FEFB1  BA 28 10 00 00                  mov edx, 0x1028
006FEFB6  B9 00 01 00 00                  mov ecx, 0x100
006FEFBB  41 B8 53 4C 53 20               mov r8d, 0x20534c53
006FEFC1  89 57 04                        mov dword ptr [rdi + 4], edx
006FEFC4  33 DB                           xor ebx, ebx
006FEFC6  E8 25 31 48 00                  call 0x140b820f0
006FEFCB  48 85 C0                        test rax, rax
006FEFCE  75 07                           jne 0x1406fefd7
006FEFD0  BB 17 00 00 C0                  mov ebx, 0xc0000017
006FEFD5  EB 06                           jmp 0x1406fefdd
006FEFD7  48 89 47 08                     mov qword ptr [rdi + 8], rax
006FEFDB  21 1F                           and dword ptr [rdi], ebx
006FEFDD  85 DB                           test ebx, ebx
006FEFDF  0F 88 F6 01 00 00               js 0x1406ff1db
006FEFE5  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
006FEFE9  41 0F BA EE 1C                  bts r14d, 0x1c
006FEFEE  48 85 D2                        test rdx, rdx
006FEFF1  75 13                           jne 0x1406ff006
006FEFF3  8B 47 04                        mov eax, dword ptr [rdi + 4]
006FEFF6  8D 48 08                        lea ecx, [rax + 8]
006FEFF9  3B C8                           cmp ecx, eax
006FEFFB  0F 82 DC 00 00 00               jb 0x1406ff0dd
006FF001  89 4F 04                        mov dword ptr [rdi + 4], ecx
006FF004  EB 58                           jmp 0x1406ff05e
006FF006  44 8B 0F                        mov r9d, dword ptr [rdi]
006FF009  33 C9                           xor ecx, ecx
006FF00B  41 3B C9                        cmp ecx, r9d
006FF00E  73 24                           jae 0x1406ff034
006FF010  8B 02                           mov eax, dword ptr [rdx]
006FF012  83 C0 04                        add eax, 4
006FF015  83 F8 04                        cmp eax, 4
006FF018  0F 82 C3 00 00 00               jb 0x1406ff0e1
006FF01E  44 8B C0                        mov r8d, eax
006FF021  4C 03 C2                        add r8, rdx
006FF024  4C 3B C2                        cmp r8, rdx
006FF027  0F 82 B4 00 00 00               jb 0x1406ff0e1
006FF02D  49 8B D0                        mov rdx, r8
006FF030  FF C1                           inc ecx
006FF032  EB D7                           jmp 0x1406ff00b
006FF034  4C 8D 42 04                     lea r8, [rdx + 4]
006FF038  4C 3B C2                        cmp r8, rdx
006FF03B  0F 82 A0 00 00 00               jb 0x1406ff0e1
006FF041  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
006FF044  48 8D 42 08                     lea rax, [rdx + 8]
006FF048  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
006FF04C  48 3B C1                        cmp rax, rcx
006FF04F  0F 87 D5 00 00 00               ja 0x1406ff12a
006FF055  C7 02 04 00 00 00               mov dword ptr [rdx], 4
006FF05B  45 89 30                        mov dword ptr [r8], r14d
006FF05E  FF 07                           inc dword ptr [rdi]
006FF060  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
006FF064  48 85 D2                        test rdx, rdx
006FF067  75 0F                           jne 0x1406ff078
006FF069  8B 47 04                        mov eax, dword ptr [rdi + 4]
006FF06C  8D 48 0C                        lea ecx, [rax + 0xc]
006FF06F  3B C8                           cmp ecx, eax
006FF071  72 6A                           jb 0x1406ff0dd
006FF073  89 4F 04                        mov dword ptr [rdi + 4], ecx
006FF076  EB 48                           jmp 0x1406ff0c0
006FF078  44 8B 0F                        mov r9d, dword ptr [rdi]
006FF07B  33 C9                           xor ecx, ecx
006FF07D  41 3B C9                        cmp ecx, r9d
006FF080  73 1C                           jae 0x1406ff09e
006FF082  8B 02                           mov eax, dword ptr [rdx]
006FF084  83 C0 04                        add eax, 4
006FF087  83 F8 04                        cmp eax, 4
006FF08A  72 55                           jb 0x1406ff0e1
006FF08C  44 8B C0                        mov r8d, eax
006FF08F  4C 03 C2                        add r8, rdx
006FF092  4C 3B C2                        cmp r8, rdx
006FF095  72 4A                           jb 0x1406ff0e1
006FF097  49 8B D0                        mov rdx, r8
006FF09A  FF C1                           inc ecx
006FF09C  EB DF                           jmp 0x1406ff07d
006FF09E  4C 8D 42 04                     lea r8, [rdx + 4]
006FF0A2  4C 3B C2                        cmp r8, rdx
006FF0A5  72 3A                           jb 0x1406ff0e1
006FF0A7  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
006FF0AA  48 8D 42 0C                     lea rax, [rdx + 0xc]
006FF0AE  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
006FF0B2  48 3B C1                        cmp rax, rcx
006FF0B5  77 73                           ja 0x1406ff12a
006FF0B7  C7 02 08 00 00 00               mov dword ptr [rdx], 8
006FF0BD  49 89 28                        mov qword ptr [r8], rbp
006FF0C0  FF 07                           inc dword ptr [rdi]
006FF0C2  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
006FF0C6  48 85 D2                        test rdx, rdx
006FF0C9  75 1D                           jne 0x1406ff0e8
006FF0CB  8B 47 04                        mov eax, dword ptr [rdi + 4]
006FF0CE  8D 88 0C 10 00 00               lea ecx, [rax + 0x100c]
006FF0D4  3B C8                           cmp ecx, eax
006FF0D6  72 05                           jb 0x1406ff0dd
006FF0D8  89 4F 04                        mov dword ptr [rdi + 4], ecx
006FF0DB  EB 6E                           jmp 0x1406ff14b
006FF0DD  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
006FF0E1  8B DE                           mov ebx, esi
006FF0E3  E9 F3 00 00 00                  jmp 0x1406ff1db
006FF0E8  44 8B 0F                        mov r9d, dword ptr [rdi]
006FF0EB  33 C9                           xor ecx, ecx
006FF0ED  41 3B C9                        cmp ecx, r9d
006FF0F0  73 1C                           jae 0x1406ff10e
006FF0F2  8B 02                           mov eax, dword ptr [rdx]
006FF0F4  83 C0 04                        add eax, 4
006FF0F7  83 F8 04                        cmp eax, 4
006FF0FA  72 E5                           jb 0x1406ff0e1
006FF0FC  44 8B C0                        mov r8d, eax
006FF0FF  4C 03 C2                        add r8, rdx
006FF102  4C 3B C2                        cmp r8, rdx
006FF105  72 DA                           jb 0x1406ff0e1
006FF107  49 8B D0                        mov rdx, r8
006FF10A  FF C1                           inc ecx
006FF10C  EB DF                           jmp 0x1406ff0ed
006FF10E  4C 8D 4A 04                     lea r9, [rdx + 4]
006FF112  4C 3B CA                        cmp r9, rdx
006FF115  72 CA                           jb 0x1406ff0e1
006FF117  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
006FF11A  48 8D 82 0C 10 00 00            lea rax, [rdx + 0x100c]
006FF121  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
006FF125  48 3B C1                        cmp rax, rcx
006FF128  76 0A                           jbe 0x1406ff134
006FF12A  BB 23 00 00 C0                  mov ebx, 0xc0000023
006FF12F  E9 A7 00 00 00                  jmp 0x1406ff1db
006FF134  C7 02 08 10 00 00               mov dword ptr [rdx], 0x1008
006FF13A  41 B8 08 10 00 00               mov r8d, 0x1008
006FF140  49 8B D7                        mov rdx, r15
006FF143  49 8B C9                        mov rcx, r9
006FF146  E8 F5 76 FC FF                  call 0x1406c6840
006FF14B  FF 07                           inc dword ptr [rdi]
006FF14D  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
006FF151  48 85 D2                        test rdx, rdx
006FF154  75 17                           jne 0x1406ff16d
006FF156  8B 47 04                        mov eax, dword ptr [rdi + 4]
006FF159  8D 48 08                        lea ecx, [rax + 8]
006FF15C  3B C8                           cmp ecx, eax
006FF15E  0F 82 79 FF FF FF               jb 0x1406ff0dd
006FF164  FF 07                           inc dword ptr [rdi]
006FF166  33 DB                           xor ebx, ebx
006FF168  89 4F 04                        mov dword ptr [rdi + 4], ecx
006FF16B  EB 6E                           jmp 0x1406ff1db
006FF16D  44 8B 0F                        mov r9d, dword ptr [rdi]
006FF170  33 C9                           xor ecx, ecx
006FF172  41 3B C9                        cmp ecx, r9d
006FF175  73 24                           jae 0x1406ff19b
006FF177  8B 02                           mov eax, dword ptr [rdx]
006FF179  83 C0 04                        add eax, 4
006FF17C  83 F8 04                        cmp eax, 4
006FF17F  0F 82 5C FF FF FF               jb 0x1406ff0e1
006FF185  44 8B C0                        mov r8d, eax
006FF188  4C 03 C2                        add r8, rdx
006FF18B  4C 3B C2                        cmp r8, rdx
006FF18E  0F 82 4D FF FF FF               jb 0x1406ff0e1
006FF194  49 8B D0                        mov rdx, r8
006FF197  FF C1                           inc ecx
006FF199  EB D7                           jmp 0x1406ff172
006FF19B  4C 8D 42 04                     lea r8, [rdx + 4]
006FF19F  4C 3B C2                        cmp r8, rdx
006FF1A2  0F 82 39 FF FF FF               jb 0x1406ff0e1
006FF1A8  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
006FF1AB  48 8D 42 08                     lea rax, [rdx + 8]
006FF1AF  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
006FF1B3  33 DB                           xor ebx, ebx
006FF1B5  48 3B C1                        cmp rax, rcx
006FF1B8  0F 87 6C FF FF FF               ja 0x1406ff12a
006FF1BE  C7 02 04 00 00 00               mov dword ptr [rdx], 4
006FF1C4  41 C7 00 08 10 00 00            mov dword ptr [r8], 0x1008
006FF1CB  FF 07                           inc dword ptr [rdi]
006FF1CD  EB 0C                           jmp 0x1406ff1db
006FF1CF  BB 95 00 00 C0                  mov ebx, 0xc0000095
006FF1D4  EB 05                           jmp 0x1406ff1db
006FF1D6  BB BB 00 00 C0                  mov ebx, 0xc00000bb
006FF1DB  33 D2                           xor edx, edx
006FF1DD  49 8B CF                        mov rcx, r15
006FF1E0  E8 8B 36 48 00                  call 0x140b82870
006FF1E5  EB 05                           jmp 0x1406ff1ec
006FF1E7  BB 95 00 00 C0                  mov ebx, 0xc0000095
006FF1EC  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
006FF1F1  8B C3                           mov eax, ebx
006FF1F3  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
006FF1F8  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
006FF1FD  48 83 C4 20                     add rsp, 0x20
006FF201  41 5F                           pop r15
006FF203  41 5E                           pop r14
006FF205  5F                              pop rdi
006FF206  C3                              ret
006FF207  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006FEE40(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_006FEEBC;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_006FEEBC;
    a2 = 0;
loc_006FEE74:
    if (0 >= 3) goto loc_006FEE9A;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_006FF1E7;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_006FF1E7;
    a2 = (unsigned int)((a2) + 1);
    goto loc_006FEE74;
loc_006FEE9A:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_006FF1E7;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_006FEF06;
    if ((*(unsigned int *)(a1)) > 4) goto loc_006FEEC6;
loc_006FEEBC:
    goto loc_006FF1EC;
loc_006FEEC6:
    a2 = 0;
loc_006FEEC8:
    if (0 >= 4) goto loc_006FEEEE;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_006FF1E7;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_006FF1E7;
    a2 = (unsigned int)((a2) + 1);
    goto loc_006FEEC8;
loc_006FEEEE:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_006FF1E7;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 4) goto loc_006FEF10;
loc_006FEF06:
    goto loc_006FF1EC;
loc_006FEF10:
    if ((*(unsigned int *)(result)) == ((unsigned int)((unsigned int)(0x1008ULL)))) goto loc_006FEF23;
    goto loc_006FF1EC;
loc_006FEF23:
    result = ExAllocatePool2(256, (unsigned int)(0x1008ULL), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    if (result != 0) goto loc_006FEF48;
    goto loc_006FF1EC;
loc_006FEF48:
    if (*(unsigned __int64 *)(v_rip + 9278441) == 0) goto loc_006FF1D6;
    result = guard_dispatch_icall(result, (unsigned int)(0x1008ULL), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    if (sign_flag) goto loc_006FF1DB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) + (0x1040ULL));
    if (((unsigned int)(result)) < 0x1040ULL) goto loc_006FF1CF;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_006FF1CF;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (condition_is_less) goto loc_006FF1DB;
    if (a4 != 0) goto loc_006FEFB1;
    goto loc_006FF1DB;
loc_006FEFB1:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(0x1028ULL));
    v_rbx = 0;
    result = ExAllocatePool2(256, (unsigned int)(0x1028ULL), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    if (result != 0) goto loc_006FEFD7;
    goto loc_006FEFDD;
loc_006FEFD7:
    *(unsigned __int64 *)(a4 + 8) = result;
loc_006FEFDD:
    if (sign_flag) goto loc_006FF1DB;
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_006FF006;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_006FF0DD;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_006FF05E;
loc_006FF006:
    a1 = 0;
loc_006FF00B:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_006FF034;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_006FF0E1;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_006FF0E1;
    a1 = (unsigned int)((a1) + 1);
    goto loc_006FF00B;
loc_006FF034:
    if ((a3 + 4) < a3) goto loc_006FF0E1;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_006FF12A;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_006FF05E:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_006FF078;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_006FF0DD;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12);
    goto loc_006FF0C0;
loc_006FF078:
    a1 = 0;
loc_006FF07D:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_006FF09E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_006FF0E1;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_006FF0E1;
    a1 = (unsigned int)((a1) + 1);
    goto loc_006FF07D;
loc_006FF09E:
    if ((a3 + 4) < a3) goto loc_006FF0E1;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_006FF12A;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_rbp);
loc_006FF0C0:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_006FF0E8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 4108)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_006FF0DD;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 4108);
    goto loc_006FF14B;
loc_006FF0DD:
loc_006FF0E1:
    goto loc_006FF1DB;
loc_006FF0E8:
    a1 = 0;
loc_006FF0ED:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_006FF10E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_006FF0E1;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_006FF0E1;
    a1 = (unsigned int)((a1) + 1);
    goto loc_006FF0ED;
loc_006FF10E:
    if ((a3 + 4) < a3) goto loc_006FF0E1;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 4108) <= a1) goto loc_006FF134;
loc_006FF12A:
    goto loc_006FF1DB;
loc_006FF134:
    *(unsigned int *)(a3) = 0x1008ULL;
    result = memcpy(a3 + 4, result, (unsigned int)(0x1008ULL), a3 + 4);
loc_006FF14B:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_006FF16D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_006FF0DD;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_006FF1DB;
loc_006FF16D:
    a1 = 0;
loc_006FF172:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_006FF19B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_006FF0E1;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_006FF0E1;
    a1 = (unsigned int)((a1) + 1);
    goto loc_006FF172;
loc_006FF19B:
    if ((a3 + 4) < a3) goto loc_006FF0E1;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    v_rbx = 0;
    if ((a3 + 8) > a1) goto loc_006FF12A;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = 0x1008ULL;
    goto loc_006FF1DB;
loc_006FF1CF:
    goto loc_006FF1DB;
loc_006FF1D6:
loc_006FF1DB:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3 + 4, (unsigned int)(*(unsigned int *)(a4)));
    goto loc_006FF1EC;
loc_006FF1E7:
loc_006FF1EC:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006FEE40(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_006FEEBC;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_006FEEBC;
    Arg2 = 0;
loc_006FEE74:
    if (0 >= 3) goto loc_006FEE9A;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_006FF1E7;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_006FF1E7;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_006FEE74;
loc_006FEE9A:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_006FF1E7;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_006FEF06;
    if ((*(uint32_t *)(arg1)) > 4) goto loc_006FEEC6;
loc_006FEEBC:
    goto loc_006FF1EC;
loc_006FEEC6:
    Arg2 = 0;
loc_006FEEC8:
    if (0 >= 4) goto loc_006FEEEE;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_006FF1E7;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_006FF1E7;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_006FEEC8;
loc_006FEEEE:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_006FF1E7;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { result = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 4) goto loc_006FEF10;
loc_006FEF06:
    goto loc_006FF1EC;
loc_006FEF10:
    if ((*(uint32_t *)(result)) == ((uint32_t)((uint32_t)(0x1008ULL)))) goto loc_006FEF23;
    goto loc_006FF1EC;
loc_006FEF23:
    result = ExAllocatePool2(256, (uint32_t)(0x1008ULL), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    if (result != 0) goto loc_006FEF48;
    goto loc_006FF1EC;
loc_006FEF48:
    if (*(uint64_t *)(v_rip + 0x8D93E9) == 0) goto loc_006FF1D6;
    result = guard_dispatch_icall(result, (uint32_t)(0x1008ULL), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    if (sign_flag) goto loc_006FF1DB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) + (0x1040ULL));
    if (((uint32_t)(result)) < 0x1040ULL) goto loc_006FF1CF;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_006FF1CF;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (condition_is_less) goto loc_006FF1DB;
    if (Arg4 != 0) goto loc_006FEFB1;
    goto loc_006FF1DB;
loc_006FEFB1:
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(0x1028ULL));
    local_rbx = 0;
    result = ExAllocatePool2(256, (uint32_t)(0x1028ULL), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    if (result != 0) goto loc_006FEFD7;
    goto loc_006FEFDD;
loc_006FEFD7:
    *(uint64_t *)(Arg4 + 0x8) = result;
loc_006FEFDD:
    if (sign_flag) goto loc_006FF1DB;
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_006FF006;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_006FF0DD;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_006FF05E;
loc_006FF006:
    Arg1 = 0;
loc_006FF00B:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_006FF034;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_006FF0E1;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_006FF0E1;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_006FF00B;
loc_006FF034:
    if ((Arg3 + 4) < Arg3) goto loc_006FF0E1;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_006FF12A;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_006FF05E:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_006FF078;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_006FF0DD;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12);
    goto loc_006FF0C0;
loc_006FF078:
    Arg1 = 0;
loc_006FF07D:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_006FF09E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_006FF0E1;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_006FF0E1;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_006FF07D;
loc_006FF09E:
    if ((Arg3 + 4) < Arg3) goto loc_006FF0E1;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_006FF12A;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_rbp);
loc_006FF0C0:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_006FF0E8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 4108)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_006FF0DD;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 4108);
    goto loc_006FF14B;
loc_006FF0DD:
loc_006FF0E1:
    goto loc_006FF1DB;
loc_006FF0E8:
    Arg1 = 0;
loc_006FF0ED:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_006FF10E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_006FF0E1;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_006FF0E1;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_006FF0ED;
loc_006FF10E:
    if ((Arg3 + 4) < Arg3) goto loc_006FF0E1;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 4108) <= Arg1) goto loc_006FF134;
loc_006FF12A:
    goto loc_006FF1DB;
loc_006FF134:
    *(uint32_t *)(Arg3) = 0x1008ULL;
    result = memcpy(Arg3 + 4, result, (uint32_t)(0x1008ULL), Arg3 + 4);
loc_006FF14B:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_006FF16D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_006FF0DD;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_006FF1DB;
loc_006FF16D:
    Arg1 = 0;
loc_006FF172:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_006FF19B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_006FF0E1;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_006FF0E1;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_006FF172;
loc_006FF19B:
    if ((Arg3 + 4) < Arg3) goto loc_006FF0E1;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    local_rbx = 0;
    if ((Arg3 + 8) > Arg1) goto loc_006FF12A;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = 0x1008ULL;
    goto loc_006FF1DB;
loc_006FF1CF:
    goto loc_006FF1DB;
loc_006FF1D6:
loc_006FF1DB:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3 + 4, (uint32_t)(*(uint32_t *)(Arg4)));
    goto loc_006FF1EC;
loc_006FF1E7:
loc_006FF1EC:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x006FEE40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
