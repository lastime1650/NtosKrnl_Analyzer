# HalpIommuAllocateDmaDomain

- RVA: `0x00554904`–`0x00554CAA` (길이 `934` bytes)
- VA: `0x0000000140554904`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4518`
- 디코드: `271`개 명령, `934/934` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00554952` → [HalpMmAllocCtxAlloc](../3E/HalpMmAllocCtxAlloc_function_003E10B8.md) (function, `0x003E10B8`)
- `0x00554971` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00554A33` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00554A47` → [HalpGetCpuInfo](../49/HalpGetCpuInfo_function_00498A70.md) (function, `0x00498A70`)
- `0x00554AF1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00554B41` → [HalpIommuGetPageTableType](HalpIommuGetPageTableType_function_00555220.md) (function, `0x00555220`)
- `0x00554B69` → [HalpIommuCreateDmarPageTable](../56/HalpIommuCreateDmarPageTable_function_00568C4C.md) (function, `0x00568C4C`)
- `0x00554BB2` → [HalpBuddyAllocatorCreateAllocator](../57/HalpBuddyAllocatorCreateAllocator_function_00575B4C.md) (function, `0x00575B4C`)
- `0x00554BF2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00554C1F` → [HalpIommuDomainMapLogicalRange](HalpIommuDomainMapLogicalRange_function_00555064.md) (function, `0x00555064`)
- `0x00554C46` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00554C8E` → [HalpIommuDomainUnmapLogicalRange](../30/HalpIommuDomainUnmapLogicalRange_function_00307258.md) (function, `0x00307258`)
- `0x00554CA3` → [HalpIommuFreeDmaDomain](HalpIommuFreeDmaDomain_function_005550F8.md) (function, `0x005550F8`)

### Direct callers
- [HalpIommuInitializeDmar](HalpIommuInitializeDmar_function_0055541C.md) at `0x00555455`
- [IommuDomainCreate](../../page/70/IommuDomainCreate_function_0070D370.md) at `0x0070D38A`
- [IommuDomainCreateEx](../../page/70/IommuDomainCreateEx_function_0070D3A0.md) at `0x0070D3AE`

### Static image references
- `0x0055491E` → RVA `0x00E0A740` (`.data`; read)
- `0x005549F1` → RVA `0x00FC1710` (`.data`; read)
- `0x00554A0F` → RVA `0x00FC18F0` (`.data`; read)
- `0x00554A1A` → RVA `0x00FC18EC` (`.data`; read)
- `0x00554A95` → RVA `0x00FC1712` (`.data`; read)
- `0x00554AB0` → RVA `0x00E10408` (`.data`; read/write)
- `0x00554AE7` → RVA `0x00FC1E08` (`.data`; read)
- `0x00554B0F` → RVA `0x00FC1711` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00554904  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00554909  55                              push rbp
0055490A  56                              push rsi
0055490B  57                              push rdi
0055490C  41 54                           push r12
0055490E  41 55                           push r13
00554910  41 56                           push r14
00554912  41 57                           push r15
00554914  48 8B EC                        mov rbp, rsp
00554917  48 81 EC 80 00 00 00            sub rsp, 0x80
0055491E  48 8B 05 1B 5E 8B 00            mov rax, qword ptr [rip + 0x8b5e1b]
00554925  48 33 C4                        xor rax, rsp
00554928  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0055492C  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00554930  48 8B DA                        mov rbx, rdx
00554933  83 65 C8 00                     and dword ptr [rbp - 0x38], 0
00554937  33 FF                           xor edi, edi
00554939  4D 8B E1                        mov r12, r9
0055493C  4C 89 45 D8                     mov qword ptr [rbp - 0x28], r8
00554940  89 4D C4                        mov dword ptr [rbp - 0x3c], ecx
00554943  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00554947  44 8D 77 70                     lea r14d, [rdi + 0x70]
0055494B  C6 45 C2 00                     mov byte ptr [rbp - 0x3e], 0
0055494F  41 8B D6                        mov edx, r14d
00554952  E8 61 C7 E8 FF                  call 0x1403e10b8
00554957  48 8B F0                        mov rsi, rax
0055495A  48 85 C0                        test rax, rax
0055495D  75 0A                           jne 0x140554969
0055495F  BF 9A 00 00 C0                  mov edi, 0xc000009a
00554964  E9 D4 02 00 00                  jmp 0x140554c3d
00554969  4D 8B C6                        mov r8, r14
0055496C  33 D2                           xor edx, edx
0055496E  48 8B CE                        mov rcx, rsi
00554971  E8 CA 22 17 00                  call 0x1406c6c40
00554976  8B 55 C4                        mov edx, dword ptr [rbp - 0x3c]
00554979  41 B9 04 00 00 00               mov r9d, 4
0055497F  83 4E 38 FF                     or dword ptr [rsi + 0x38], 0xffffffff
00554983  8B CA                           mov ecx, edx
00554985  44 89 4E 08                     mov dword ptr [rsi + 8], r9d
00554989  85 D2                           test edx, edx
0055498B  74 42                           je 0x1405549cf
0055498D  83 E9 01                        sub ecx, 1
00554990  74 2F                           je 0x1405549c1
00554992  83 E9 01                        sub ecx, 1
00554995  74 1A                           je 0x1405549b1
00554997  83 F9 01                        cmp ecx, 1
0055499A  74 0A                           je 0x1405549a6
0055499C  BF EF 00 00 C0                  mov edi, 0xc00000ef
005549A1  E9 FA 02 00 00                  jmp 0x140554ca0
005549A6  4C 8D 6E 34                     lea r13, [rsi + 0x34]
005549AA  41 C6 45 00 01                  mov byte ptr [r13], 1
005549AF  EB 22                           jmp 0x1405549d3
005549B1  45 32 FF                        xor r15b, r15b
005549B4  C6 46 34 01                     mov byte ptr [rsi + 0x34], 1
005549B8  45 32 F6                        xor r14b, r14b
005549BB  4C 8D 6E 34                     lea r13, [rsi + 0x34]
005549BF  EB 18                           jmp 0x1405549d9
005549C1  45 32 FF                        xor r15b, r15b
005549C4  4C 8D 6E 34                     lea r13, [rsi + 0x34]
005549C8  33 C0                           xor eax, eax
005549CA  45 32 F6                        xor r14b, r14b
005549CD  EB 0F                           jmp 0x1405549de
005549CF  4C 8D 6E 34                     lea r13, [rsi + 0x34]
005549D3  41 B7 01                        mov r15b, 1
005549D6  45 8A F7                        mov r14b, r15b
005549D9  B8 02 00 00 00                  mov eax, 2
005549DE  89 46 0C                        mov dword ptr [rsi + 0xc], eax
005549E1  48 8D 46 48                     lea rax, [rsi + 0x48]
005549E5  89 56 08                        mov dword ptr [rsi + 8], edx
005549E8  48 89 40 08                     mov qword ptr [rax + 8], rax
005549EC  48 89 00                        mov qword ptr [rax], rax
005549EF  33 C0                           xor eax, eax
005549F1  38 05 19 CD A6 00               cmp byte ptr [rip + 0xa6cd19], al
005549F7  89 46 58                        mov dword ptr [rsi + 0x58], eax
005549FA  74 04                           je 0x140554a00
005549FC  48 21 46 68                     and qword ptr [rsi + 0x68], rax
00554A00  83 FA 02                        cmp edx, 2
00554A03  75 0A                           jne 0x140554a0f
00554A05  BF BB 00 00 C0                  mov edi, 0xc00000bb
00554A0A  E9 91 02 00 00                  jmp 0x140554ca0
00554A0F  44 8B 05 DA CE A6 00            mov r8d, dword ptr [rip + 0xa6ceda]
00554A16  44 89 45 CC                     mov dword ptr [rbp - 0x34], r8d
00554A1A  44 8B 05 CB CE A6 00            mov r8d, dword ptr [rip + 0xa6cecb]
00554A21  44 89 45 D0                     mov dword ptr [rbp - 0x30], r8d
00554A25  41 38 45 00                     cmp byte ptr [r13], al
00554A29  74 4A                           je 0x140554a75
00554A2B  44 89 4D CC                     mov dword ptr [rbp - 0x34], r9d
00554A2F  44 89 4D D0                     mov dword ptr [rbp - 0x30], r9d
00554A33  E8 58 31 FA FF                  call 0x1404f7b90
00554A38  85 C0                           test eax, eax
00554A3A  74 36                           je 0x140554a72
00554A3C  4C 8D 4D C2                     lea r9, [rbp - 0x3e]
00554A40  45 33 C0                        xor r8d, r8d
00554A43  33 D2                           xor edx, edx
00554A45  33 C9                           xor ecx, ecx
00554A47  E8 24 40 F4 FF                  call 0x140498a70
00554A4C  84 C0                           test al, al
00554A4E  74 22                           je 0x140554a72
00554A50  80 7D C2 02                     cmp byte ptr [rbp - 0x3e], 2
00554A54  41 8A D7                        mov dl, r15b
00554A57  8B 55 C4                        mov edx, dword ptr [rbp - 0x3c]
00554A5A  49 8B CD                        mov rcx, r13
00554A5D  41 8A C6                        mov al, r14b
00554A60  75 13                           jne 0x140554a75
00554A62  41 B8 04 00 00 00               mov r8d, 4
00554A68  44 89 45 CC                     mov dword ptr [rbp - 0x34], r8d
00554A6C  44 89 45 D0                     mov dword ptr [rbp - 0x30], r8d
00554A70  EB 03                           jmp 0x140554a75
00554A72  8B 55 C4                        mov edx, dword ptr [rbp - 0x3c]
00554A75  40 38 3D 94 CC A6 00            cmp byte ptr [rip + 0xa6cc94], dil
00554A7C  0F 84 96 00 00 00               je 0x140554b18
00554A82  83 FA 01                        cmp edx, 1
00554A85  75 08                           jne 0x140554a8f
00554A87  21 7E 30                        and dword ptr [rsi + 0x30], edi
00554A8A  E9 A6 00 00 00                  jmp 0x140554b35
00554A8F  41 38 7D 00                     cmp byte ptr [r13], dil
00554A93  75 7A                           jne 0x140554b0f
00554A95  40 38 3D 76 CC A6 00            cmp byte ptr [rip + 0xa6cc76], dil
00554A9C  0F 84 63 FF FF FF               je 0x140554a05
00554AA2  83 FA 03                        cmp edx, 3
00554AA5  0F 84 87 00 00 00               je 0x140554b32
00554AAB  B8 01 00 00 00                  mov eax, 1
00554AB0  F0 0F C1 05 50 B9 8B 00         lock xadd dword ptr [rip + 0x8bb950], eax
00554AB8  FF C0                           inc eax
00554ABA  89 46 30                        mov dword ptr [rsi + 0x30], eax
00554ABD  85 D2                           test edx, edx
00554ABF  75 42                           jne 0x140554b03
00554AC1  33 C9                           xor ecx, ecx
00554AC3  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
00554AC7  89 45 E8                        mov dword ptr [rbp - 0x18], eax
00554ACA  8A 46 34                        mov al, byte ptr [rsi + 0x34]
00554ACD  88 45 EC                        mov byte ptr [rbp - 0x14], al
00554AD0  48 8B C3                        mov rax, rbx
00554AD3  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
00554AD6  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00554ADA  48 C1 E8 3E                     shr rax, 0x3e
00554ADE  24 01                           and al, 1
00554AE0  48 C1 EB 3F                     shr rbx, 0x3f
00554AE4  88 45 F0                        mov byte ptr [rbp - 0x10], al
00554AE7  48 8B 05 1A D3 A6 00            mov rax, qword ptr [rip + 0xa6d31a]
00554AEE  88 5D F1                        mov byte ptr [rbp - 0xf], bl
00554AF1  E8 DA 5F 16 00                  call 0x1406baad0
00554AF6  8B F8                           mov edi, eax
00554AF8  85 C0                           test eax, eax
00554AFA  0F 88 A0 01 00 00               js 0x140554ca0
00554B00  8B 55 C4                        mov edx, dword ptr [rbp - 0x3c]
00554B03  45 8A F7                        mov r14b, r15b
00554B06  85 D2                           test edx, edx
00554B08  75 2B                           jne 0x140554b35
00554B0A  45 32 F6                        xor r14b, r14b
00554B0D  EB 26                           jmp 0x140554b35
00554B0F  40 38 3D FB CB A6 00            cmp byte ptr [rip + 0xa6cbfb], dil
00554B16  EB 84                           jmp 0x140554a9c
00554B18  48 0F BA E3 3E                  bt rbx, 0x3e
00554B1D  0F 82 E2 FE FF FF               jb 0x140554a05
00554B23  48 8D 46 10                     lea rax, [rsi + 0x10]
00554B27  48 89 40 08                     mov qword ptr [rax + 8], rax
00554B2B  48 89 00                        mov qword ptr [rax], rax
00554B2E  48 21 7E 20                     and qword ptr [rsi + 0x20], rdi
00554B32  45 8A F7                        mov r14b, r15b
00554B35  45 84 F6                        test r14b, r14b
00554B38  74 3E                           je 0x140554b78
00554B3A  8A 4E 34                        mov cl, byte ptr [rsi + 0x34]
00554B3D  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00554B41  E8 DA 06 00 00                  call 0x140555220
00554B46  8B F8                           mov edi, eax
00554B48  85 C0                           test eax, eax
00554B4A  0F 88 50 01 00 00               js 0x140554ca0
00554B50  44 8B 45 CC                     mov r8d, dword ptr [rbp - 0x34]
00554B54  48 8D 46 28                     lea rax, [rsi + 0x28]
00554B58  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00554B5B  8B 4D C8                        mov ecx, dword ptr [rbp - 0x38]
00554B5E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00554B63  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00554B69  E8 DE 40 01 00                  call 0x140568c4c
00554B6E  8B F8                           mov edi, eax
00554B70  85 C0                           test eax, eax
00554B72  0F 88 28 01 00 00               js 0x140554ca0
00554B78  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00554B7C  4D 85 C0                        test r8, r8
00554B7F  74 44                           je 0x140554bc5
00554B81  45 84 FF                        test r15b, r15b
00554B84  75 10                           jne 0x140554b96
00554B86  41 83 38 00                     cmp dword ptr [r8], 0
00554B8A  74 0A                           je 0x140554b96
00554B8C  BF 0D 00 00 C0                  mov edi, 0xc000000d
00554B91  E9 0A 01 00 00                  jmp 0x140554ca0
00554B96  48 8D 56 40                     lea rdx, [rsi + 0x40]
00554B9A  48 83 22 00                     and qword ptr [rdx], 0
00554B9E  41 8B 08                        mov ecx, dword ptr [r8]
00554BA1  85 C9                           test ecx, ecx
00554BA3  74 1E                           je 0x140554bc3
00554BA5  83 F9 01                        cmp ecx, 1
00554BA8  0F 85 EE FD FF FF               jne 0x14055499c
00554BAE  41 8B 48 04                     mov ecx, dword ptr [r8 + 4]
00554BB2  E8 95 0F 02 00                  call 0x140575b4c
00554BB7  8B F8                           mov edi, eax
00554BB9  85 C0                           test eax, eax
00554BBB  0F 88 DF 00 00 00               js 0x140554ca0
00554BC1  EB 02                           jmp 0x140554bc5
00554BC3  33 FF                           xor edi, edi
00554BC5  49 8B DC                        mov rbx, r12
00554BC8  49 C7 C5 00 F0 FF FF            mov r13, 0xfffffffffffff000
00554BCF  4D 85 E4                        test r12, r12
00554BD2  74 5E                           je 0x140554c32
00554BD4  4C 8B 73 08                     mov r14, qword ptr [rbx + 8]
00554BD8  48 8B 4E 40                     mov rcx, qword ptr [rsi + 0x40]
00554BDC  4D 23 F5                        and r14, r13
00554BDF  48 85 C9                        test rcx, rcx
00554BE2  74 1D                           je 0x140554c01
00554BE4  48 8B 01                        mov rax, qword ptr [rcx]
00554BE7  49 8B D6                        mov rdx, r14
00554BEA  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00554BEE  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00554BF2  E8 D9 5E 16 00                  call 0x1406baad0
00554BF7  8B F8                           mov edi, eax
00554BF9  85 C0                           test eax, eax
00554BFB  0F 88 96 00 00 00               js 0x140554c97
00554C01  80 7B 18 00                     cmp byte ptr [rbx + 0x18], 0
00554C05  74 23                           je 0x140554c2a
00554C07  4C 8B 4B 10                     mov r9, qword ptr [rbx + 0x10]
00554C0B  4D 8B C6                        mov r8, r14
00554C0E  49 C1 E1 0C                     shl r9, 0xc
00554C12  BA 03 00 00 00                  mov edx, 3
00554C17  48 8B CE                        mov rcx, rsi
00554C1A  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00554C1F  E8 40 04 00 00                  call 0x140555064
00554C24  8B F8                           mov edi, eax
00554C26  85 C0                           test eax, eax
00554C28  78 6D                           js 0x140554c97
00554C2A  48 8B 1B                        mov rbx, qword ptr [rbx]
00554C2D  48 85 DB                        test rbx, rbx
00554C30  75 A2                           jne 0x140554bd4
00554C32  85 FF                           test edi, edi
00554C34  78 61                           js 0x140554c97
00554C36  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00554C3A  48 89 30                        mov qword ptr [rax], rsi
00554C3D  8B C7                           mov eax, edi
00554C3F  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00554C43  48 33 CC                        xor rcx, rsp
00554C46  E8 F5 79 15 00                  call 0x1406ac640
00554C4B  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
00554C53  48 81 C4 80 00 00 00            add rsp, 0x80
00554C5A  41 5F                           pop r15
00554C5C  41 5E                           pop r14
00554C5E  41 5D                           pop r13
00554C60  41 5C                           pop r12
00554C62  5F                              pop rdi
00554C63  5E                              pop rsi
00554C64  5D                              pop rbp
00554C65  C3                              ret
00554C66  CC                              int3
00554C67  41 80 7C 24 18 00               cmp byte ptr [r12 + 0x18], 0
00554C6D  74 24                           je 0x140554c93
00554C6F  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
00554C74  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00554C78  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
00554C7D  45 33 C9                        xor r9d, r9d
00554C80  48 C1 E0 0C                     shl rax, 0xc
00554C84  49 23 D5                        and rdx, r13
00554C87  48 8B CE                        mov rcx, rsi
00554C8A  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00554C8E  E8 C5 25 DB FF                  call 0x140307258
00554C93  4D 8B 24 24                     mov r12, qword ptr [r12]
00554C97  4C 3B E3                        cmp r12, rbx
00554C9A  75 CB                           jne 0x140554c67
00554C9C  85 FF                           test edi, edi
00554C9E  79 9D                           jns 0x140554c3d
00554CA0  48 8B CE                        mov rcx, rsi
00554CA3  E8 50 04 00 00                  call 0x1405550f8
00554CA8  EB 93                           jmp 0x140554c3d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIommuAllocateDmaDomain(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int8 v_stack_m47;
    unsigned int v_stack_m48;
    unsigned __int8 v_stack_m4C;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_m76;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 9133595)) ^ (v_rsp);
    v_stack_m40 = result;
    v_rdi = 0;
    v_stack_m60 = a3;
    v_stack_m74 = a1;
    v_stack_m58 = a5;
    v_stack_m76 = 0;
    result = HalpMmAllocCtxAlloc(a1, (unsigned int)((unsigned int)(v_rdi + 112)), a3, a4);
    if (result != 0) goto loc_00554969;
    goto loc_00554C3D;
loc_00554969:
    a2 = 0;
    result = memset(result, a2, v_rdi + 112, a4);
    *(unsigned int *)(result + 8) = 4;
    if ((unsigned int)((unsigned int)(v_stack_m74)) == 0) goto loc_005549CF;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m74)))) - (1));
    if (condition_is_equal) goto loc_005549C1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005549B1;
    if (a1 == 1) goto loc_005549A6;
loc_0055499C:
    goto loc_00554CA0;
loc_005549A6:
    *(unsigned __int8 *)(result + 52) = 1;
    goto loc_005549D3;
loc_005549B1:
    v_r15 = 0;
    *(unsigned __int8 *)(result + 52) = 1;
    v_r14 = 0;
    goto loc_005549D9;
loc_005549C1:
    v_r15 = 0;
    result = 0;
    v_r14 = 0;
    goto loc_005549DE;
loc_005549CF:
loc_005549D3:
loc_005549D9:
loc_005549DE:
    *(unsigned int *)(result + 12) = 2;
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(v_stack_m74));
    *(unsigned __int64 *)(result + 72 + 8) = result + 72;
    *(unsigned __int64 *)(result + 72) = result + 72;
    result = 0;
    *(unsigned int *)(result + 88) = 0;
    if ((*(unsigned __int8 *)(v_rip + 10931481)) != 0) {
    }
    if (((unsigned int)((unsigned int)(v_stack_m74))) != 2) goto loc_00554A0F;
loc_00554A05:
    goto loc_00554CA0;
loc_00554A0F:
    v_stack_m6C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10931930)));
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10931915)));
    if ((*(unsigned __int8 *)(result + 52)) == 0) goto loc_00554A75;
    v_stack_m6C = 4;
    v_stack_m68 = 4;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)(v_stack_m74), (unsigned int)(*(unsigned int *)(v_rip + 10931915)), 4);
    if ((unsigned int)(result) == 0) goto loc_00554A72;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = HalpGetCpuInfo(a1, a2, a3, v_stack_m76);
    if ((unsigned __int8)(result) == 0) goto loc_00554A72;
    if (v_stack_m76 != 2) goto loc_00554A75;
    v_stack_m6C = 4;
    v_stack_m68 = 4;
    goto loc_00554A75;
loc_00554A72:
loc_00554A75:
    if ((*(unsigned __int8 *)(v_rip + 10931348)) == ((unsigned __int8)((unsigned int)(0xC00000BBULL)))) goto loc_00554B18;
    if (((unsigned int)((unsigned int)(v_stack_m74))) != 1) goto loc_00554A8F;
    goto loc_00554B35;
loc_00554A8F:
    if ((*(unsigned __int8 *)(result + 52)) != ((unsigned __int8)((unsigned int)(0xC00000BBULL)))) goto loc_00554B0F;
loc_00554A9C:
    if ((*(unsigned __int8 *)(v_rip + 10931318)) == ((unsigned __int8)((unsigned int)(0xC00000BBULL)))) goto loc_00554A05;
    if (((unsigned int)((unsigned int)(v_stack_m74))) == 3) goto loc_00554B32;
    result = (unsigned int)((1) + 1);
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(v_stack_m74)) != 0) goto loc_00554B03;
    a1 = 0;
    v_stack_m50 = 0;
    v_stack_m50 = (unsigned int)(result);
    v_stack_m4C = (unsigned __int8)(*(unsigned __int8 *)(result + 52));
    v_stack_m48 = 0;
    result = (0) >> (62);
    result = (unsigned __int8)((result) & (1));
    v_rbx = (a2) >> (63);
    v_stack_m48 = (unsigned __int8)(result);
    v_stack_m47 = (unsigned __int8)(v_rbx);
    result = guard_dispatch_icall(v_stack_m50, (unsigned int)(v_stack_m74), 4, v_stack_m76);
    if (sign_flag) goto loc_00554CA0;
loc_00554B03:
    if ((unsigned int)((unsigned int)(v_stack_m74)) != 0) goto loc_00554B35;
    v_r14 = 0;
    goto loc_00554B35;
loc_00554B0F:
    goto loc_00554A9C;
loc_00554B18:
    if ((*(unsigned __int8 *)(v_rip + 10931195)) < ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_00554A05;
    *(unsigned __int64 *)(result + 16 + 8) = result + 16;
    *(unsigned __int64 *)(result + 16) = result + 16;
loc_00554B32:
loc_00554B35:
    if (1 == 0) goto loc_00554B78;
    result = HalpIommuGetPageTableType(*(unsigned __int8 *)(result + 52), v_stack_m70, 4, v_stack_m76);
    if (sign_flag) goto loc_00554CA0;
    v_stack_m88 = result + 40;
    result = HalpIommuCreateDmarPageTable((unsigned int)(v_stack_m70), (unsigned int)(v_stack_m68), (unsigned int)(v_stack_m6C), v_stack_m76);
    if (sign_flag) goto loc_00554CA0;
loc_00554B78:
    if (v_stack_m60 == 0) goto loc_00554BC5;
    if (1 != 0) goto loc_00554B96;
    if ((*(unsigned int *)(v_stack_m60)) == 0) goto loc_00554B96;
    goto loc_00554CA0;
loc_00554B96:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60))) == 0) goto loc_00554BC3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60)))) != 1) goto loc_0055499C;
    result = HalpBuddyAllocatorCreateAllocator((unsigned int)(*(unsigned int *)(v_stack_m60 + 4)), result + 64, v_stack_m60, v_stack_m76);
    if (sign_flag) goto loc_00554CA0;
    goto loc_00554BC5;
loc_00554BC3:
    v_rdi = 0;
loc_00554BC5:
    if (a4 == 0) goto loc_00554C32;
loc_00554BD4:
    v_r14 = (*(unsigned __int64 *)(a4 + 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (*(unsigned __int64 *)(result + 64) == 0) goto loc_00554C01;
    result = guard_dispatch_icall(*(unsigned __int64 *)(result + 64), v_r14, *(unsigned __int64 *)(a4 + 16), v_stack_m76);
    if (sign_flag) goto loc_00554C97;
loc_00554C01:
    if ((*(unsigned __int8 *)(a4 + 24)) == 0) goto loc_00554C2A;
    a4 = (*(unsigned __int64 *)(a4 + 16)) << (12);
    v_stack_m98 = v_r14;
    result = HalpIommuDomainMapLogicalRange(result, 3, v_r14, a4);
    if (sign_flag) goto loc_00554C97;
loc_00554C2A:
    if (*(unsigned __int64 *)(a4) != 0) goto loc_00554BD4;
loc_00554C32:
    if (sign_flag) goto loc_00554C97;
    *(unsigned __int64 *)(v_stack_m58) = result;
loc_00554C3D:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, 3, v_r14, a4);
    v_rsp = (v_rsp) + (128);
    return result;
loc_00554C67:
    if ((*(unsigned __int8 *)(a4 + 24)) != 0) {
        result = *(unsigned __int64 *)(a4 + 16);
        a3 = v_stack_m60;
        a2 = *(unsigned __int64 *)(a4 + 8);
        a4 = 0;
        result = (result) << (12);
        a2 = (a2) & (0xFFFFFFFFFFFFF000ULL);
        a1 = result;
        v_stack_m60 = result;
        result = HalpIommuDomainUnmapLogicalRange(a1, a2, a3, a4);
    }
loc_00554C97:
    if ((*(unsigned __int64 *)(a4)) != v_stack_p8) goto loc_00554C67;
    if (!sign_flag) goto loc_00554C3D;
loc_00554CA0:
    result = HalpIommuFreeDmaDomain(result, a2, a3, a4);
    goto loc_00554C3D;
}
```

## 5. (Beta) C Style

```c
int64_t HalpIommuAllocateDmaDomain(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint8_t v_stack_m47;
    uint32_t v_stack_m48;
    uint8_t v_stack_m4C;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_m76;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x8B5E1B)) ^ (local_rsp);
    v_stack_m40 = result;
    local_rdi = 0;
    v_stack_m60 = Arg3;
    v_stack_m74 = Arg1;
    v_stack_m58 = Arg5;
    v_stack_m76 = 0;
    result = HalpMmAllocCtxAlloc(Arg1, (uint32_t)((uint32_t)(local_rdi + 112)), Arg3, Arg4);
    if (result != 0) goto loc_00554969;
    goto loc_00554C3D;
loc_00554969:
    Arg2 = 0;
    result = memset(result, Arg2, local_rdi + 112, Arg4);
    *(uint32_t *)(result + 0x8) = 4;
    if ((uint32_t)((uint32_t)(v_stack_m74)) == 0) goto loc_005549CF;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m74)))) - (1));
    if (condition_is_equal) goto loc_005549C1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005549B1;
    if (Arg1 == 1) goto loc_005549A6;
loc_0055499C:
    goto loc_00554CA0;
loc_005549A6:
    *(uint8_t *)(result + 0x34) = 1;
    goto loc_005549D3;
loc_005549B1:
    local_r15 = 0;
    *(uint8_t *)(result + 0x34) = 1;
    local_r14 = 0;
    goto loc_005549D9;
loc_005549C1:
    local_r15 = 0;
    result = 0;
    local_r14 = 0;
    goto loc_005549DE;
loc_005549CF:
loc_005549D3:
loc_005549D9:
loc_005549DE:
    *(uint32_t *)(result + 0xC) = 2;
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(v_stack_m74));
    *(uint64_t *)(result + 0x48 + 0x8) = result + 72;
    *(uint64_t *)(result + 0x48) = result + 72;
    result = 0;
    *(uint32_t *)(result + 0x58) = 0;
    if ((*(uint8_t *)(v_rip + 0xA6CD19)) != 0) {
    }
    if (((uint32_t)((uint32_t)(v_stack_m74))) != 2) goto loc_00554A0F;
loc_00554A05:
    goto loc_00554CA0;
loc_00554A0F:
    v_stack_m6C = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA6CEDA)));
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA6CECB)));
    if ((*(uint8_t *)(result + 0x34)) == 0) goto loc_00554A75;
    v_stack_m6C = 4;
    v_stack_m68 = 4;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)(v_stack_m74), (uint32_t)(*(uint32_t *)(v_rip + 0xA6CECB)), 4);
    if ((uint32_t)(result) == 0) goto loc_00554A72;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = HalpGetCpuInfo(Arg1, Arg2, Arg3, v_stack_m76);
    if ((uint8_t)(result) == 0) goto loc_00554A72;
    if (v_stack_m76 != 2) goto loc_00554A75;
    v_stack_m6C = 4;
    v_stack_m68 = 4;
    goto loc_00554A75;
loc_00554A72:
loc_00554A75:
    if ((*(uint8_t *)(v_rip + 0xA6CC94)) == ((uint8_t)((uint32_t)(0xC00000BBULL)))) goto loc_00554B18;
    if (((uint32_t)((uint32_t)(v_stack_m74))) != 1) goto loc_00554A8F;
    goto loc_00554B35;
loc_00554A8F:
    if ((*(uint8_t *)(result + 0x34)) != ((uint8_t)((uint32_t)(0xC00000BBULL)))) goto loc_00554B0F;
loc_00554A9C:
    if ((*(uint8_t *)(v_rip + 0xA6CC76)) == ((uint8_t)((uint32_t)(0xC00000BBULL)))) goto loc_00554A05;
    if (((uint32_t)((uint32_t)(v_stack_m74))) == 3) goto loc_00554B32;
    result = (uint32_t)((1) + 1);
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(v_stack_m74)) != 0) goto loc_00554B03;
    Arg1 = 0;
    v_stack_m50 = 0;
    v_stack_m50 = (uint32_t)(result);
    v_stack_m4C = (uint8_t)(*(uint8_t *)(result + 0x34));
    v_stack_m48 = 0;
    result = (0) >> (62);
    result = (uint8_t)((result) & (1));
    local_rbx = (Arg2) >> (63);
    v_stack_m48 = (uint8_t)(result);
    v_stack_m47 = (uint8_t)(local_rbx);
    result = guard_dispatch_icall(v_stack_m50, (uint32_t)(v_stack_m74), 4, v_stack_m76);
    if (sign_flag) goto loc_00554CA0;
loc_00554B03:
    if ((uint32_t)((uint32_t)(v_stack_m74)) != 0) goto loc_00554B35;
    local_r14 = 0;
    goto loc_00554B35;
loc_00554B0F:
    goto loc_00554A9C;
loc_00554B18:
    if ((*(uint8_t *)(v_rip + 0xA6CBFB)) < ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_00554A05;
    *(uint64_t *)(result + 0x10 + 0x8) = result + 16;
    *(uint64_t *)(result + 0x10) = result + 16;
loc_00554B32:
loc_00554B35:
    if (1 == 0) goto loc_00554B78;
    result = HalpIommuGetPageTableType(*(uint8_t *)(result + 0x34), v_stack_m70, 4, v_stack_m76);
    if (sign_flag) goto loc_00554CA0;
    v_stack_m88 = result + 40;
    result = HalpIommuCreateDmarPageTable((uint32_t)(v_stack_m70), (uint32_t)(v_stack_m68), (uint32_t)(v_stack_m6C), v_stack_m76);
    if (sign_flag) goto loc_00554CA0;
loc_00554B78:
    if (v_stack_m60 == 0) goto loc_00554BC5;
    if (1 != 0) goto loc_00554B96;
    if ((*(uint32_t *)(v_stack_m60)) == 0) goto loc_00554B96;
    goto loc_00554CA0;
loc_00554B96:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60))) == 0) goto loc_00554BC3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60)))) != 1) goto loc_0055499C;
    result = HalpBuddyAllocatorCreateAllocator((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x4)), result + 64, v_stack_m60, v_stack_m76);
    if (sign_flag) goto loc_00554CA0;
    goto loc_00554BC5;
loc_00554BC3:
    local_rdi = 0;
loc_00554BC5:
    if (Arg4 == 0) goto loc_00554C32;
loc_00554BD4:
    local_r14 = (*(uint64_t *)(Arg4 + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    if (*(uint64_t *)(result + 0x40) == 0) goto loc_00554C01;
    result = guard_dispatch_icall(*(uint64_t *)(result + 0x40), local_r14, *(uint64_t *)(Arg4 + 0x10), v_stack_m76);
    if (sign_flag) goto loc_00554C97;
loc_00554C01:
    if ((*(uint8_t *)(Arg4 + 0x18)) == 0) goto loc_00554C2A;
    Arg4 = (*(uint64_t *)(Arg4 + 0x10)) << (12);
    v_stack_m98 = local_r14;
    result = HalpIommuDomainMapLogicalRange(result, 3, local_r14, Arg4);
    if (sign_flag) goto loc_00554C97;
loc_00554C2A:
    if (*(uint64_t *)(Arg4) != 0) goto loc_00554BD4;
loc_00554C32:
    if (sign_flag) goto loc_00554C97;
    *(uint64_t *)(v_stack_m58) = result;
loc_00554C3D:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 3, local_r14, Arg4);
    local_rsp = (local_rsp) + (128);
    return result;
loc_00554C67:
    if ((*(uint8_t *)(Arg4 + 0x18)) != 0) {
        result = *(uint64_t *)(Arg4 + 0x10);
        Arg3 = v_stack_m60;
        Arg2 = *(uint64_t *)(Arg4 + 0x8);
        Arg4 = 0;
        result = (result) << (12);
        Arg2 = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
        Arg1 = result;
        v_stack_m60 = result;
        result = HalpIommuDomainUnmapLogicalRange(Arg1, Arg2, Arg3, Arg4);
    }
loc_00554C97:
    if ((*(uint64_t *)(Arg4)) != v_stack_p8) goto loc_00554C67;
    if (!sign_flag) goto loc_00554C3D;
loc_00554CA0:
    result = HalpIommuFreeDmaDomain(result, Arg2, Arg3, Arg4);
    goto loc_00554C3D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00554904&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
