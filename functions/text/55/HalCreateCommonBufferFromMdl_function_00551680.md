# HalCreateCommonBufferFromMdl

- RVA: `0x00551680`–`0x00551A63` (길이 `995` bytes)
- VA: `0x0000000140551680`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD158`
- 디코드: `282`개 명령, `995/995` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0055170A` → [HalpCreateCommonBufferFromMdlVerifyParams](HalpCreateCommonBufferFromMdlVerifyParams_function_00550478.md) (function, `0x00550478`)
- `0x0055177D` → [HalpDmaReferenceDomainObject](../3E/HalpDmaReferenceDomainObject_function_003E9B08.md) (function, `0x003E9B08`)
- `0x005517E9` → [MmGetCacheAttributeEx](../67/MmGetCacheAttributeEx_function_00674F80.md) (function, `0x00674F80`)
- `0x005518F7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00551965` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005519A8` → [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x005519CC` → [HalpAllocateCommonBufferEntry](../3E/HalpAllocateCommonBufferEntry_function_003E99F4.md) (function, `0x003E99F4`)
- `0x00551A08` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00551A2C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00551A34` → [HalpDmaDereferenceDomainObject](../3F/HalpDmaDereferenceDomainObject_function_003F69DC.md) (function, `0x003F69DC`)
- `0x00551A42` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0055169C` → RVA `0x00E0A740` (`.data`; read)
- `0x005518E1` → RVA `0x00FC1778` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00551680  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00551685  55                              push rbp
00551686  56                              push rsi
00551687  57                              push rdi
00551688  41 54                           push r12
0055168A  41 55                           push r13
0055168C  41 56                           push r14
0055168E  41 57                           push r15
00551690  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00551695  48 81 EC E0 00 00 00            sub rsp, 0xe0
0055169C  48 8B 05 9D 90 8B 00            mov rax, qword ptr [rip + 0x8b909d]
005516A3  48 33 C4                        xor rax, rsp
005516A6  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
005516AA  48 8B B1 00 02 00 00            mov rsi, qword ptr [rcx + 0x200]
005516B1  33 FF                           xor edi, edi
005516B3  48 89 55 87                     mov qword ptr [rbp - 0x79], rdx
005516B7  0F 57 C0                        xorps xmm0, xmm0
005516BA  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
005516BE  41 8B C1                        mov eax, r9d
005516C1  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
005516C5  4C 8D 4D E7                     lea r9, [rbp - 0x19]
005516C9  33 D2                           xor edx, edx
005516CB  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
005516CF  4D 8B D0                        mov r10, r8
005516D2  48 89 55 07                     mov qword ptr [rbp + 7], rdx
005516D6  89 55 CF                        mov dword ptr [rbp - 0x31], edx
005516D9  48 8D 4D 87                     lea rcx, [rbp - 0x79]
005516DD  49 8B D2                        mov rdx, r10
005516E0  89 7D 8F                        mov dword ptr [rbp - 0x71], edi
005516E3  44 8B C0                        mov r8d, eax
005516E6  48 89 7D 9F                     mov qword ptr [rbp - 0x61], rdi
005516EA  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
005516EE  48 89 7D AF                     mov qword ptr [rbp - 0x51], rdi
005516F2  44 8A E7                        mov r12b, dil
005516F5  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
005516F9  48 89 7D 97                     mov qword ptr [rbp - 0x69], rdi
005516FD  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00551701  40 88 7D 80                     mov byte ptr [rbp - 0x80], dil
00551705  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
0055170A  E8 69 ED FF FF                  call 0x140550478
0055170F  8B D8                           mov ebx, eax
00551711  BF 01 00 00 00                  mov edi, 1
00551716  85 C0                           test eax, eax
00551718  79 18                           jns 0x140551732
0055171A  8D 88 11 FF FF 3F               lea ecx, [rax + 0x3fffff11]
00551720  3B CF                           cmp ecx, edi
00551722  0F 87 11 03 00 00               ja 0x140551a39
00551728  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0055172D  E9 07 03 00 00                  jmp 0x140551a39
00551732  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
00551736  4C 8B 6D 87                     mov r13, qword ptr [rbp - 0x79]
0055173A  4C 8B 75 F7                     mov r14, qword ptr [rbp - 9]
0055173E  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
00551742  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
00551746  4D 8D 7D 30                     lea r15, [r13 + 0x30]
0055174A  48 03 C1                        add rax, rcx
0055174D  48 8B 4D 07                     mov rcx, qword ptr [rbp + 7]
00551751  48 C1 E8 0C                     shr rax, 0xc
00551755  4D 8D 3C C7                     lea r15, [r15 + rax*8]
00551759  4C 89 7D A7                     mov qword ptr [rbp - 0x59], r15
0055175D  85 C9                           test ecx, ecx
0055175F  74 16                           je 0x140551777
00551761  3B CF                           cmp ecx, edi
00551763  74 09                           je 0x14055176e
00551765  C7 45 87 03 00 00 00            mov dword ptr [rbp - 0x79], 3
0055176C  EB 0C                           jmp 0x14055177a
0055176E  C7 45 87 02 00 00 00            mov dword ptr [rbp - 0x79], 2
00551775  EB 03                           jmp 0x14055177a
00551777  89 7D 87                        mov dword ptr [rbp - 0x79], edi
0055177A  48 8B CE                        mov rcx, rsi
0055177D  E8 86 83 E9 FF                  call 0x1403e9b08
00551782  8B D8                           mov ebx, eax
00551784  85 C0                           test eax, eax
00551786  0F 88 AD 02 00 00               js 0x140551a39
0055178C  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
00551790  48 85 C0                        test rax, rax
00551793  74 07                           je 0x14055179c
00551795  40 88 B8 0C 02 00 00            mov byte ptr [rax + 0x20c], dil
0055179C  44 38 65 0B                     cmp byte ptr [rbp + 0xb], r12b
005517A0  74 12                           je 0x1405517b4
005517A2  48 8D 45 E7                     lea rax, [rbp - 0x19]
005517A6  4C 8D 5D EF                     lea r11, [rbp - 0x11]
005517AA  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
005517AE  4C 89 5D AF                     mov qword ptr [rbp - 0x51], r11
005517B2  EB 04                           jmp 0x1405517b8
005517B4  4C 8B 5D AF                     mov r11, qword ptr [rbp - 0x51]
005517B8  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
005517BC  44 38 A0 BD 01 00 00            cmp byte ptr [rax + 0x1bd], r12b
005517C3  75 55                           jne 0x14055181a
005517C5  45 33 FF                        xor r15d, r15d
005517C8  4D 8B E6                        mov r12, r14
005517CB  49 C1 EC 0C                     shr r12, 0xc
005517CF  41 8B CF                        mov ecx, r15d
005517D2  49 3B CC                        cmp rcx, r12
005517D5  73 36                           jae 0x14055180d
005517D7  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
005517DB  4C 8D 45 8F                     lea r8, [rbp - 0x71]
005517DF  33 D2                           xor edx, edx
005517E1  4A 8B 0C F8                     mov rcx, qword ptr [rax + r15*8]
005517E5  48 C1 E1 0C                     shl rcx, 0xc
005517E9  E8 92 37 12 00                  call 0x140674f80
005517EE  8B D8                           mov ebx, eax
005517F0  85 C0                           test eax, eax
005517F2  0F 88 39 02 00 00               js 0x140551a31
005517F8  83 7D 8F 00                     cmp dword ptr [rbp - 0x71], 0
005517FC  75 05                           jne 0x140551803
005517FE  44 03 FF                        add r15d, edi
00551801  EB CC                           jmp 0x1405517cf
00551803  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00551808  E9 24 02 00 00                  jmp 0x140551a31
0055180D  4C 8B 7D A7                     mov r15, qword ptr [rbp - 0x59]
00551811  44 8A 64 24 40                  mov r12b, byte ptr [rsp + 0x40]
00551816  4C 8B 5D AF                     mov r11, qword ptr [rbp - 0x51]
0055181A  4D 8B C6                        mov r8, r14
0055181D  C7 45 BF 02 00 00 00            mov dword ptr [rbp - 0x41], 2
00551824  49 C1 E8 0C                     shr r8, 0xc
00551828  4C 89 45 CF                     mov qword ptr [rbp - 0x31], r8
0055182C  4C 89 7D C7                     mov qword ptr [rbp - 0x39], r15
00551830  8B 4E 30                        mov ecx, dword ptr [rsi + 0x30]
00551833  85 C9                           test ecx, ecx
00551835  74 0C                           je 0x140551843
00551837  2B CF                           sub ecx, edi
00551839  74 08                           je 0x140551843
0055183B  3B CF                           cmp ecx, edi
0055183D  0F 85 F2 00 00 00               jne 0x140551935
00551843  4D 8B 17                        mov r10, qword ptr [r15]
00551846  8B D7                           mov edx, edi
00551848  49 C1 E2 0C                     shl r10, 0xc
0055184C  33 DB                           xor ebx, ebx
0055184E  4C 89 55 97                     mov qword ptr [rbp - 0x69], r10
00551852  48 89 5D A7                     mov qword ptr [rbp - 0x59], rbx
00551856  44 8B CA                        mov r9d, edx
00551859  4D 3B C8                        cmp r9, r8
0055185C  73 22                           jae 0x140551880
0055185E  4B 8B 04 CF                     mov rax, qword ptr [r15 + r9*8]
00551862  8D 4A FF                        lea ecx, [rdx - 1]
00551865  48 2B C7                        sub rax, rdi
00551868  49 3B 04 CF                     cmp rax, qword ptr [r15 + rcx*8]
0055186C  75 04                           jne 0x140551872
0055186E  03 D7                           add edx, edi
00551870  EB E4                           jmp 0x140551856
00551872  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
00551876  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0055187B  E9 A0 00 00 00                  jmp 0x140551920
00551880  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00551884  8B 88 C0 01 00 00               mov ecx, dword ptr [rax + 0x1c0]
0055188A  83 F9 40                        cmp ecx, 0x40
0055188D  72 06                           jb 0x140551895
0055188F  48 83 CA FF                     or rdx, 0xffffffffffffffff
00551893  EB 09                           jmp 0x14055189e
00551895  48 8B D7                        mov rdx, rdi
00551898  48 D3 E2                        shl rdx, cl
0055189B  48 2B D7                        sub rdx, rdi
0055189E  4D 85 DB                        test r11, r11
005518A1  74 29                           je 0x1405518cc
005518A3  49 8B 0B                        mov rcx, qword ptr [r11]
005518A6  48 3B CA                        cmp rcx, rdx
005518A9  48 0F 43 CA                     cmovae rcx, rdx
005518AD  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
005518B1  49 89 0B                        mov qword ptr [r11], rcx
005518B4  4C 3B 12                        cmp r10, qword ptr [rdx]
005518B7  72 0C                           jb 0x1405518c5
005518B9  49 8D 46 FF                     lea rax, [r14 - 1]
005518BD  49 03 C2                        add rax, r10
005518C0  48 3B C1                        cmp rax, rcx
005518C3  76 17                           jbe 0x1405518dc
005518C5  BB 0D 00 00 C0                  mov ebx, 0xc000000d
005518CA  EB 54                           jmp 0x140551920
005518CC  49 8D 46 FF                     lea rax, [r14 - 1]
005518D0  49 03 C2                        add rax, r10
005518D3  48 3B C2                        cmp rax, rdx
005518D6  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
005518DA  EB E7                           jmp 0x1405518c3
005518DC  39 7E 30                        cmp dword ptr [rsi + 0x30], edi
005518DF  75 34                           jne 0x140551915
005518E1  48 8B 05 90 FE A6 00            mov rax, qword ptr [rip + 0xa6fe90]
005518E8  4C 8D 45 BF                     lea r8, [rbp - 0x41]
005518EC  8B 55 87                        mov edx, dword ptr [rbp - 0x79]
005518EF  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
005518F3  48 8B 40 48                     mov rax, qword ptr [rax + 0x48]
005518F7  E8 D4 91 16 00                  call 0x1406baad0
005518FC  8B D8                           mov ebx, eax
005518FE  85 C0                           test eax, eax
00551900  0F 88 2B 01 00 00               js 0x140551a31
00551906  4C 8B 55 97                     mov r10, qword ptr [rbp - 0x69]
0055190A  48 8B 5D A7                     mov rbx, qword ptr [rbp - 0x59]
0055190E  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00551913  EB 6E                           jmp 0x140551983
00551915  83 7D 07 02                     cmp dword ptr [rbp + 7], 2
00551919  74 62                           je 0x14055197d
0055191B  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00551920  83 7E 30 02                     cmp dword ptr [rsi + 0x30], 2
00551924  74 13                           je 0x140551939
00551926  32 C0                           xor al, al
00551928  85 DB                           test ebx, ebx
0055192A  0F 89 09 01 00 00               jns 0x140551a39
00551930  E9 BB 00 00 00                  jmp 0x1405519f0
00551935  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
00551939  48 8B 05 38 FE A6 00            mov rax, qword ptr [rip + 0xa6fe38]
00551940  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00551944  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00551949  4C 8D 45 BF                     lea r8, [rbp - 0x41]
0055194D  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00551951  45 33 C9                        xor r9d, r9d
00551954  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
00551959  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
0055195D  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00551962  8B 55 87                        mov edx, dword ptr [rbp - 0x79]
00551965  E8 66 91 16 00                  call 0x1406baad0
0055196A  8B D8                           mov ebx, eax
0055196C  85 C0                           test eax, eax
0055196E  78 74                           js 0x1405519e4
00551970  4C 8B 55 97                     mov r10, qword ptr [rbp - 0x69]
00551974  49 8B DD                        mov rbx, r13
00551977  40 88 7D 80                     mov byte ptr [rbp - 0x80], dil
0055197B  EB 06                           jmp 0x140551983
0055197D  32 C0                           xor al, al
0055197F  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00551983  41 F6 45 0A 05                  test byte ptr [r13 + 0xa], 5
00551988  74 06                           je 0x140551990
0055198A  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
0055198E  EB 21                           jmp 0x1405519b1
00551990  C7 44 24 28 00 00 00 40         mov dword ptr [rsp + 0x28], 0x40000000
00551998  45 33 C9                        xor r9d, r9d
0055199B  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
005519A0  44 8B C7                        mov r8d, edi
005519A3  33 D2                           xor edx, edx
005519A5  49 8B CD                        mov rcx, r13
005519A8  E8 53 6E DC FF                  call 0x140318800
005519AD  4C 8B 55 97                     mov r10, qword ptr [rbp - 0x69]
005519B1  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
005519B5  4C 8B CE                        mov r9, rsi
005519B8  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005519BE  48 03 D0                        add rdx, rax
005519C1  4D 8B C2                        mov r8, r10
005519C4  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
005519C9  48 8B CB                        mov rcx, rbx
005519CC  E8 23 80 E9 FF                  call 0x1403e99f4
005519D1  8B D8                           mov ebx, eax
005519D3  85 C0                           test eax, eax
005519D5  78 0D                           js 0x1405519e4
005519D7  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
005519DB  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
005519DF  48 89 01                        mov qword ptr [rcx], rax
005519E2  EB 55                           jmp 0x140551a39
005519E4  4C 8B 55 97                     mov r10, qword ptr [rbp - 0x69]
005519E8  44 8A 64 24 40                  mov r12b, byte ptr [rsp + 0x40]
005519ED  8A 45 80                        mov al, byte ptr [rbp - 0x80]
005519F0  45 84 E4                        test r12b, r12b
005519F3  74 1A                           je 0x140551a0f
005519F5  48 8B 05 7C FD A6 00            mov rax, qword ptr [rip + 0xa6fd7c]
005519FC  48 8D 55 BF                     lea rdx, [rbp - 0x41]
00551A00  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00551A04  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
00551A08  E8 C3 90 16 00                  call 0x1406baad0
00551A0D  EB 22                           jmp 0x140551a31
00551A0F  84 C0                           test al, al
00551A11  74 1E                           je 0x140551a31
00551A13  48 8B 05 5E FD A6 00            mov rax, qword ptr [rip + 0xa6fd5e]
00551A1A  49 8B D2                        mov rdx, r10
00551A1D  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00551A21  49 C1 EE 0C                     shr r14, 0xc
00551A25  4D 8B C6                        mov r8, r14
00551A28  48 8B 40 40                     mov rax, qword ptr [rax + 0x40]
00551A2C  E8 9F 90 16 00                  call 0x1406baad0
00551A31  48 8B CE                        mov rcx, rsi
00551A34  E8 A3 4F EA FF                  call 0x1403f69dc
00551A39  8B C3                           mov eax, ebx
00551A3B  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
00551A3F  48 33 CC                        xor rcx, rsp
00551A42  E8 F9 AB 15 00                  call 0x1406ac640
00551A47  48 8B 9C 24 38 01 00 00         mov rbx, qword ptr [rsp + 0x138]
00551A4F  48 81 C4 E0 00 00 00            add rsp, 0xe0
00551A56  41 5F                           pop r15
00551A58  41 5E                           pop r14
00551A5A  41 5D                           pop r13
00551A5C  41 5C                           pop r12
00551A5E  5F                              pop rdi
00551A5F  5E                              pop rsi
00551A60  5D                              pop rbp
00551A61  C3                              ret
00551A62  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalCreateCommonBufferFromMdl(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m4C;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m57;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int8 v_stack_mD7;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 9146525)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = 0;
    v_stack_mD0 = a2;
    v_stack_m78 = a5;
    a2 = 0;
    v_stack_mA0 = a1;
    v_stack_m50 = 0;
    v_stack_m88 = 0;
    v_stack_mC8 = 0;
    v_stack_mB8 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_mA8 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_mC0 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_mD7 = 0;
    v_stack_mD8 = 0;
    result = HalpCreateCommonBufferFromMdlVerifyParams(v_stack_mD0, a3, (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_m70);
    if (!sign_flag) goto loc_00551732;
    if (((unsigned int)(result + 1073741585)) > 1) goto loc_00551A39;
    goto loc_00551A39;
loc_00551732:
    v_stack_m80 = v_stack_m58;
    result = ((unsigned int)(*(unsigned int *)(v_stack_mD0 + 44))) + (v_stack_m58);
    result = (result) >> (12);
    v_stack_mB0 = v_stack_mD0 + 48 + result * 8;
    if ((unsigned int)(v_stack_m50) == 0) goto loc_00551777;
    if (((unsigned int)(v_stack_m50)) == 1) goto loc_0055176E;
    v_stack_mD0 = 3;
    goto loc_0055177A;
loc_0055176E:
    v_stack_mD0 = 2;
    goto loc_0055177A;
loc_00551777:
    v_stack_mD0 = 1;
loc_0055177A:
    result = HalpDmaReferenceDomainObject(*(unsigned __int64 *)(a1 + 512), a3, (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_m70);
    if (sign_flag) goto loc_00551A39;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 512) + 56) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 512) + 56) + 524) = 1;
    }
    if (v_stack_m4C == 0) goto loc_005517B4;
    v_stack_mB8 = v_stack_m70;
    v_stack_mA8 = v_stack_m68;
    goto loc_005517B8;
loc_005517B4:
loc_005517B8:
    if ((*(unsigned __int8 *)(v_stack_mA0 + 445)) != 0) goto loc_0055181A;
    v_r15 = 0;
    v_r12 = (v_stack_m60) >> (12);
loc_005517CF:
    if (0 >= v_r12) goto loc_0055180D;
    a2 = 0;
    a1 = (*(unsigned __int64 *)(v_stack_mB0 + v_r15 * 8)) << (12);
    result = MmGetCacheAttributeEx(a1, a2, v_stack_mC8, v_stack_m70);
    if (sign_flag) goto loc_00551A31;
    if (v_stack_mC8 != 0) goto loc_00551803;
    v_r15 = (unsigned int)((v_r15) + (1));
    goto loc_005517CF;
loc_00551803:
    goto loc_00551A31;
loc_0055180D:
loc_0055181A:
    v_stack_m98 = 2;
    a3 = (v_stack_m60) >> (12);
    v_stack_m88 = a3;
    v_stack_m90 = v_stack_mB0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 512) + 48))) == 0) goto loc_00551843;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 512) + 48))) - (1));
    if (condition_is_equal) goto loc_00551843;
    if (((unsigned int)(a1)) != 1) goto loc_00551935;
loc_00551843:
    v_r10 = (*(unsigned __int64 *)(v_stack_mB0)) << (12);
    v_rbx = 0;
    v_stack_mC0 = v_r10;
    v_stack_mB0 = 0;
loc_00551856:
    if (1 >= a3) goto loc_00551880;
    result = (*(unsigned __int64 *)(v_stack_mB0 + 1 * 8)) - (1);
    if (result != (*(unsigned __int64 *)(v_stack_mB0 + 1 - 1 * 8))) goto loc_00551872;
    a2 = (unsigned int)((1) + (1));
    goto loc_00551856;
loc_00551872:
    goto loc_00551920;
loc_00551880:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA0 + 448)))) < 64) goto loc_00551895;
    a2 = (v_stack_mB8) | (-1);
    goto loc_0055189E;
loc_00551895:
    a2 = (1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mA0 + 448))));
    a2 = (a2) - (1);
loc_0055189E:
    if (v_stack_mA8 == 0) goto loc_005518CC;
    a1 = *(unsigned __int64 *)(v_stack_mA8);
    if ((*(unsigned __int64 *)(v_stack_mA8)) >= a2) { a1 = a2; }
    *(unsigned __int64 *)(v_stack_mA8) = a1;
    if (v_r10 < (*(unsigned __int64 *)(v_stack_mB8))) goto loc_005518C5;
    result = (v_stack_m60 - 1) + (v_r10);
loc_005518C3:
    if (result <= a1) goto loc_005518DC;
loc_005518C5:
    goto loc_00551920;
loc_005518CC:
    result = (v_stack_m60 - 1) + (v_r10);
    goto loc_005518C3;
loc_005518DC:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 512) + 48)) != 1) goto loc_00551915;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 512) + 40), (unsigned int)(v_stack_mD0), v_stack_m98, 1);
    if (sign_flag) goto loc_00551A31;
    v_stack_mD8 = 1;
    goto loc_00551983;
loc_00551915:
    if (v_stack_m50 == 2) goto loc_0055197D;
loc_00551920:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 512) + 48)) == 2) goto loc_00551939;
    result = 0;
    if (!sign_flag) goto loc_00551A39;
    goto loc_005519F0;
loc_00551935:
loc_00551939:
    v_stack_mE8 = v_stack_mC0;
    a4 = 0;
    v_stack_mF0 = v_stack_mA8;
    v_stack_mF8 = v_stack_mB8;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 512) + 40), (unsigned int)(v_stack_mD0), v_stack_m98, a4);
    if (sign_flag) goto loc_005519E4;
    v_stack_mD7 = 1;
    goto loc_00551983;
loc_0055197D:
    result = 0;
    v_stack_mD8 = 0;
loc_00551983:
    if (((*(unsigned __int8 *)(v_stack_mD0 + 10)) & (5)) == 0) goto loc_00551990;
    goto loc_005519B1;
loc_00551990:
    v_stack_mF0 = 0x40000000ULL;
    a4 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(v_stack_mD0, a2, 1, a4);
loc_005519B1:
    a2 = (v_stack_m80) + (result);
    v_stack_mF8 = 0;
    result = HalpAllocateCommonBufferEntry(v_stack_mD0, a2, v_stack_mC0, *(unsigned __int64 *)(a1 + 512));
    if (sign_flag) goto loc_005519E4;
    *(unsigned __int64 *)(v_stack_m78) = v_stack_mC0;
    goto loc_00551A39;
loc_005519E4:
loc_005519F0:
    if ((unsigned __int8)(v_stack_mD8) == 0) goto loc_00551A0F;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 512) + 40), v_stack_m98, v_stack_mC0, *(unsigned __int64 *)(a1 + 512));
    goto loc_00551A31;
loc_00551A0F:
    v_r14 = v_stack_m60;
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(v_rip + 10943838);
        a2 = v_stack_mC0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 512) + 40);
        v_r14 = (v_stack_m60) >> (12);
        a3 = v_r14;
        result = *(unsigned __int64 *)(result + 64);
        result = guard_dispatch_icall(a1, a2, a3, *(unsigned __int64 *)(a1 + 512));
    }
    result = HalpDmaDereferenceDomainObject(*(unsigned __int64 *)(a1 + 512), a2, a3, *(unsigned __int64 *)(a1 + 512));
loc_00551A39:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, *(unsigned __int64 *)(a1 + 512));
    v_rsp = (v_rsp) + (224);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalCreateCommonBufferFromMdl(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint8_t v_stack_m4C;
    uint64_t v_stack_m50;
    uint64_t v_stack_m57;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint8_t v_stack_mD7;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x8B909D)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = 0;
    v_stack_mD0 = Arg2;
    v_stack_m78 = Arg5;
    Arg2 = 0;
    v_stack_mA0 = Arg1;
    v_stack_m50 = 0;
    v_stack_m88 = 0;
    v_stack_mC8 = 0;
    v_stack_mB8 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_mA8 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_mC0 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_mD7 = 0;
    v_stack_mD8 = 0;
    result = HalpCreateCommonBufferFromMdlVerifyParams(v_stack_mD0, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_m70);
    if (!sign_flag) goto loc_00551732;
    if (((uint32_t)(result + 1073741585)) > 1) goto loc_00551A39;
    goto loc_00551A39;
loc_00551732:
    v_stack_m80 = v_stack_m58;
    result = ((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x2C))) + (v_stack_m58);
    result = (result) >> (12);
    v_stack_mB0 = v_stack_mD0 + 48 + result * 8;
    if ((uint32_t)(v_stack_m50) == 0) goto loc_00551777;
    if (((uint32_t)(v_stack_m50)) == 1) goto loc_0055176E;
    v_stack_mD0 = 3;
    goto loc_0055177A;
loc_0055176E:
    v_stack_mD0 = 2;
    goto loc_0055177A;
loc_00551777:
    v_stack_mD0 = 1;
loc_0055177A:
    result = HalpDmaReferenceDomainObject(*(uint64_t *)(arg1 + 0x200), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_m70);
    if (sign_flag) goto loc_00551A39;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x200) + 0x38) != 0) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x200) + 0x38) + 0x20C) = 1;
    }
    if (v_stack_m4C == 0) goto loc_005517B4;
    v_stack_mB8 = v_stack_m70;
    v_stack_mA8 = v_stack_m68;
    goto loc_005517B8;
loc_005517B4:
loc_005517B8:
    if ((*(uint8_t *)(v_stack_mA0 + 0x1BD)) != 0) goto loc_0055181A;
    local_r15 = 0;
    local_r12 = (v_stack_m60) >> (12);
loc_005517CF:
    if (0 >= local_r12) goto loc_0055180D;
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(v_stack_mB0 + local_r15 * 8)) << (12);
    result = MmGetCacheAttributeEx(Arg1, Arg2, v_stack_mC8, v_stack_m70);
    if (sign_flag) goto loc_00551A31;
    if (v_stack_mC8 != 0) goto loc_00551803;
    local_r15 = (uint32_t)((local_r15) + (1));
    goto loc_005517CF;
loc_00551803:
    goto loc_00551A31;
loc_0055180D:
loc_0055181A:
    v_stack_m98 = 2;
    Arg3 = (v_stack_m60) >> (12);
    v_stack_m88 = Arg3;
    v_stack_m90 = v_stack_mB0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x200) + 0x30))) == 0) goto loc_00551843;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x200) + 0x30))) - (1));
    if (condition_is_equal) goto loc_00551843;
    if (((uint32_t)(Arg1)) != 1) goto loc_00551935;
loc_00551843:
    local_r10 = (*(uint64_t *)(v_stack_mB0)) << (12);
    local_rbx = 0;
    v_stack_mC0 = local_r10;
    v_stack_mB0 = 0;
loc_00551856:
    if (1 >= Arg3) goto loc_00551880;
    result = (*(uint64_t *)(v_stack_mB0 + 0x1 * 8)) - (1);
    if (result != (*(uint64_t *)(v_stack_mB0 + 0x1 - 0x1 * 8))) goto loc_00551872;
    Arg2 = (uint32_t)((1) + (1));
    goto loc_00551856;
loc_00551872:
    goto loc_00551920;
loc_00551880:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x1C0)))) < 64) goto loc_00551895;
    Arg2 = (v_stack_mB8) | (-1);
    goto loc_0055189E;
loc_00551895:
    Arg2 = (1) << ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x1C0))));
    Arg2 = (Arg2) - (1);
loc_0055189E:
    if (v_stack_mA8 == 0) goto loc_005518CC;
    Arg1 = *(uint64_t *)(v_stack_mA8);
    if ((*(uint64_t *)(v_stack_mA8)) >= Arg2) { Arg1 = Arg2; }
    *(void **)(v_stack_mA8) = Arg1;
    if (local_r10 < (*(uint64_t *)(v_stack_mB8))) goto loc_005518C5;
    result = (v_stack_m60 - 1) + (local_r10);
loc_005518C3:
    if (result <= Arg1) goto loc_005518DC;
loc_005518C5:
    goto loc_00551920;
loc_005518CC:
    result = (v_stack_m60 - 1) + (local_r10);
    goto loc_005518C3;
loc_005518DC:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x200) + 0x30)) != 1) goto loc_00551915;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(arg1 + 0x200) + 0x28), (uint32_t)(v_stack_mD0), v_stack_m98, 1);
    if (sign_flag) goto loc_00551A31;
    v_stack_mD8 = 1;
    goto loc_00551983;
loc_00551915:
    if (v_stack_m50 == 2) goto loc_0055197D;
loc_00551920:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x200) + 0x30)) == 2) goto loc_00551939;
    result = 0;
    if (!sign_flag) goto loc_00551A39;
    goto loc_005519F0;
loc_00551935:
loc_00551939:
    v_stack_mE8 = v_stack_mC0;
    Arg4 = 0;
    v_stack_mF0 = v_stack_mA8;
    v_stack_mF8 = v_stack_mB8;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(arg1 + 0x200) + 0x28), (uint32_t)(v_stack_mD0), v_stack_m98, Arg4);
    if (sign_flag) goto loc_005519E4;
    v_stack_mD7 = 1;
    goto loc_00551983;
loc_0055197D:
    result = 0;
    v_stack_mD8 = 0;
loc_00551983:
    if (((*(uint8_t *)(v_stack_mD0 + 0xA)) & (5)) == 0) goto loc_00551990;
    goto loc_005519B1;
loc_00551990:
    v_stack_mF0 = 0x40000000ULL;
    Arg4 = 0;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(v_stack_mD0, Arg2, 1, Arg4);
loc_005519B1:
    Arg2 = (v_stack_m80) + (result);
    v_stack_mF8 = 0;
    result = HalpAllocateCommonBufferEntry(v_stack_mD0, Arg2, v_stack_mC0, *(uint64_t *)(arg1 + 0x200));
    if (sign_flag) goto loc_005519E4;
    *(uint64_t *)(v_stack_m78) = v_stack_mC0;
    goto loc_00551A39;
loc_005519E4:
loc_005519F0:
    if ((uint8_t)(v_stack_mD8) == 0) goto loc_00551A0F;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(arg1 + 0x200) + 0x28), v_stack_m98, v_stack_mC0, *(uint64_t *)(arg1 + 0x200));
    goto loc_00551A31;
loc_00551A0F:
    local_r14 = v_stack_m60;
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(v_rip + 0xA6FD5E);
        Arg2 = v_stack_mC0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x200) + 0x28);
        local_r14 = (v_stack_m60) >> (12);
        Arg3 = local_r14;
        result = *(uint64_t *)(result + 0x40);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, *(uint64_t *)(arg1 + 0x200));
    }
    result = HalpDmaDereferenceDomainObject(*(uint64_t *)(arg1 + 0x200), Arg2, Arg3, *(uint64_t *)(arg1 + 0x200));
loc_00551A39:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, *(uint64_t *)(arg1 + 0x200));
    local_rsp = (local_rsp) + (224);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x200` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00551680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
