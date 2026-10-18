# MiReplacePageOfProtoPool

- RVA: `0x00364BB8`–`0x0036535C` (길이 `1,956` bytes)
- VA: `0x0000000140364BB8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079EE8`
- 디코드: `518`개 명령, `1,956/1,956` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00364C12` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00364C1E` → [MiGetPrototypePteRanges](../3E/MiGetPrototypePteRanges_function_003E0720.md) (function, `0x003E0720`)
- `0x00364C7B` → [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) (function, `0x00323270`)
- `0x00364CB7` → [MiMakeProtectionPfnCompatible](../22/MiMakeProtectionPfnCompatible_function_00229CD0.md) (function, `0x00229CD0`)
- `0x00364CCA` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00364EC8` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00364EE8` → [MiLockLeafPage](MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x00365136` → [MiSetPfnContainingFrame](MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x0036518D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003651CC` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003652D3` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x003652EB` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003652FA` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00365312` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00365321` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00365339` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00365348` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B33DA`

### Static image references
- `0x00364BD1` → RVA `0x00E0A740` (`.data`; read)
- `0x00364CCF` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00364F41` → RVA `0x00EF51E0` (`.data`; read/write)
- `0x00364FF8` → RVA `0x00EF51E8` (`.data`; read/write)
- `0x0036500D` → RVA `0x00010880` (`.rdata`; read)
- `0x003650F7` → RVA `0x00E2DC80` (`.data`; read)
- `0x003651F4` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0036520D` → RVA `0x00EF51E4` (`.data`; read/write)
- `0x00365226` → RVA `0x00EF51EC` (`.data`; read/write)
- `0x003652DD` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00364BB8  40 55                           push rbp
00364BBA  53                              push rbx
00364BBB  56                              push rsi
00364BBC  57                              push rdi
00364BBD  41 54                           push r12
00364BBF  41 55                           push r13
00364BC1  41 56                           push r14
00364BC3  41 57                           push r15
00364BC5  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00364BCA  48 81 EC D8 00 00 00            sub rsp, 0xd8
00364BD1  48 8B 05 68 5B AA 00            mov rax, qword ptr [rip + 0xaa5b68]
00364BD8  48 33 C4                        xor rax, rsp
00364BDB  48 89 45 07                     mov qword ptr [rbp + 7], rax
00364BDF  48 8B DA                        mov rbx, rdx
00364BE2  4C 89 45 B7                     mov qword ptr [rbp - 0x49], r8
00364BE6  33 D2                           xor edx, edx
00364BE8  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00364BED  4D 8B E8                        mov r13, r8
00364BF0  48 C7 45 8F 00 02 00 00         mov qword ptr [rbp - 0x71], 0x200
00364BF8  83 65 93 00                     and dword ptr [rbp - 0x6d], 0
00364BFC  48 8D 45 C7                     lea rax, [rbp - 0x39]
00364C00  48 8B F1                        mov rsi, rcx
00364C03  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00364C07  44 8D 42 40                     lea r8d, [rdx + 0x40]
00364C0B  49 8B F9                        mov rdi, r9
00364C0E  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00364C12  E8 29 20 36 00                  call 0x1406c6c40
00364C17  48 8D 55 8F                     lea rdx, [rbp - 0x71]
00364C1B  48 8B CE                        mov rcx, rsi
00364C1E  E8 FD BA 07 00                  call 0x1403e0720
00364C23  85 C0                           test eax, eax
00364C25  0F 84 86 05 00 00               je 0x1403651b1
00364C2B  33 C0                           xor eax, eax
00364C2D  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
00364C35  4C 8D 34 5B                     lea r14, [rbx + rbx*2]
00364C39  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00364C3D  49 C1 E6 04                     shl r14, 4
00364C41  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
00364C4B  48 8B C1                        mov rax, rcx
00364C4E  4E 8D 3C 6D 00 00 00 00         lea r15, [r13*2]
00364C56  4C 03 F0                        add r14, rax
00364C59  4D 03 FD                        add r15, r13
00364C5C  49 C1 E7 04                     shl r15, 4
00364C60  48 8B C1                        mov rax, rcx
00364C63  BA 03 00 00 00                  mov edx, 3
00364C68  48 8D 4F 60                     lea rcx, [rdi + 0x60]
00364C6C  4C 03 F8                        add r15, rax
00364C6F  4C 89 7D 9F                     mov qword ptr [rbp - 0x61], r15
00364C73  44 8D 4A 01                     lea r9d, [rdx + 1]
00364C77  44 8D 42 FE                     lea r8d, [rdx - 2]
00364C7B  E8 F0 E5 FB FF                  call 0x140323270
00364C80  48 8B F8                        mov rdi, rax
00364C83  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
00364C87  4C 8B E0                        mov r12, rax
00364C8A  48 C1 EF 09                     shr rdi, 9
00364C8E  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00364C98  48 BE 00 00 00 00 80 F6 FF FF   movabs rsi, 0xfffff68000000000
00364CA2  48 23 F8                        and rdi, rax
00364CA5  48 8B CE                        mov rcx, rsi
00364CA8  48 03 F9                        add rdi, rcx
00364CAB  49 8B D7                        mov rdx, r15
00364CAE  B9 04 00 00 00                  mov ecx, 4
00364CB3  48 89 7D AF                     mov qword ptr [rbp - 0x51], rdi
00364CB7  E8 14 50 EC FF                  call 0x140229cd0
00364CBC  0D 00 00 00 A0                  or eax, 0xa0000000
00364CC1  49 8B D5                        mov rdx, r13
00364CC4  44 8B C0                        mov r8d, eax
00364CC7  48 8B CF                        mov rcx, rdi
00364CCA  E8 C1 08 F6 FF                  call 0x1402c5590
00364CCF  48 0F BA 25 B0 1D C6 00 24      bt qword ptr [rip + 0xc61db0], 0x24
00364CD8  48 8B D8                        mov rbx, rax
00364CDB  0F 82 C4 05 00 00               jb 0x1403652a5
00364CE1  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00364CE5  48 89 1F                        mov qword ptr [rdi], rbx
00364CE8  83 E1 04                        and ecx, 4
00364CEB  48 8D 75 C7                     lea rsi, [rbp - 0x39]
00364CEF  33 FF                           xor edi, edi
00364CF1  8B C1                           mov eax, ecx
00364CF3  48 F7 D8                        neg rax
00364CF6  45 1B ED                        sbb r13d, r13d
00364CF9  41 83 E5 20                     and r13d, 0x20
00364CFD  48 F7 D9                        neg rcx
00364D00  48 1B C0                        sbb rax, rax
00364D03  83 E0 04                        and eax, 4
00364D06  48 2B F0                        sub rsi, rax
00364D09  48 89 75 A7                     mov qword ptr [rbp - 0x59], rsi
00364D0D  44 8B 4D 8F                     mov r9d, dword ptr [rbp - 0x71]
00364D11  41 83 CF FF                     or r15d, 0xffffffff
00364D15  41 3B F9                        cmp edi, r9d
00364D18  45 1B C0                        sbb r8d, r8d
00364D1B  44 23 C7                        and r8d, edi
00364D1E  41 8D 41 FF                     lea eax, [r9 - 1]
00364D22  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
00364D27  46 8D 14 28                     lea r10d, [rax + r13]
00364D2B  41 8B C2                        mov eax, r10d
00364D2E  43 8D 0C 28                     lea ecx, [r8 + r13]
00364D32  2B C1                           sub eax, ecx
00364D34  FF C0                           inc eax
00364D36  83 F8 01                        cmp eax, 1
00364D39  0F 82 3D 05 00 00               jb 0x14036527c
00364D3F  41 8B C2                        mov eax, r10d
00364D42  BA 01 00 00 00                  mov edx, 1
00364D47  48 C1 E8 06                     shr rax, 6
00364D4B  4C 8D 1C C6                     lea r11, [rsi + rax*8]
00364D4F  8B C1                           mov eax, ecx
00364D51  48 C1 E8 06                     shr rax, 6
00364D55  80 E1 3F                        and cl, 0x3f
00364D58  48 D3 E2                        shl rdx, cl
00364D5B  48 FF CA                        dec rdx
00364D5E  48 8D 1C C6                     lea rbx, [rsi + rax*8]
00364D62  48 8B 03                        mov rax, qword ptr [rbx]
00364D65  48 F7 D0                        not rax
00364D68  48 0B D0                        or rdx, rax
00364D6B  48 83 FA FF                     cmp rdx, -1
00364D6F  75 15                           jne 0x140364d86
00364D71  48 83 C3 08                     add rbx, 8
00364D75  49 3B DB                        cmp rbx, r11
00364D78  0F 87 FE 04 00 00               ja 0x14036527c
00364D7E  48 8B 13                        mov rdx, qword ptr [rbx]
00364D81  48 F7 D2                        not rdx
00364D84  EB E5                           jmp 0x140364d6b
00364D86  48 2B DE                        sub rbx, rsi
00364D89  48 F7 D2                        not rdx
00364D8C  48 0F BC C2                     bsf rax, rdx
00364D90  48 C1 FB 03                     sar rbx, 3
00364D94  C1 E3 06                        shl ebx, 6
00364D97  03 D8                           add ebx, eax
00364D99  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00364D9D  41 3B DA                        cmp ebx, r10d
00364DA0  0F 87 D6 04 00 00               ja 0x14036527c
00364DA6  41 3B DF                        cmp ebx, r15d
00364DA9  0F 84 D0 04 00 00               je 0x14036527f
00364DAF  41 2B DD                        sub ebx, r13d
00364DB2  3B DF                           cmp ebx, edi
00364DB4  0F 82 5E 04 00 00               jb 0x140365218
00364DBA  41 3B DF                        cmp ebx, r15d
00364DBD  0F 84 55 04 00 00               je 0x140365218
00364DC3  41 BA 00 02 00 00               mov r10d, 0x200
00364DC9  48 BE FF FF FF FF FF FF FF 7F   movabs rsi, 0x7fffffffffffffff
00364DD3  3B DF                           cmp ebx, edi
00364DD5  0F 85 DA 03 00 00               jne 0x1403651b5
00364DDB  83 64 24 24 00                  and dword ptr [rsp + 0x24], 0
00364DE0  33 FF                           xor edi, edi
00364DE2  44 8B FB                        mov r15d, ebx
00364DE5  41 3B DA                        cmp ebx, r10d
00364DE8  0F 83 B9 03 00 00               jae 0x1403651a7
00364DEE  41 8B C7                        mov eax, r15d
00364DF1  4C 8D 45 C7                     lea r8, [rbp - 0x39]
00364DF5  48 C1 E8 05                     shr rax, 5
00364DF9  4C 8D 5D 03                     lea r11, [rbp + 3]
00364DFD  8B CB                           mov ecx, ebx
00364DFF  83 E1 1F                        and ecx, 0x1f
00364E02  4D 8D 04 80                     lea r8, [r8 + rax*4]
00364E06  45 8B 08                        mov r9d, dword ptr [r8]
00364E09  8D 47 01                        lea eax, [rdi + 1]
00364E0C  D3 E0                           shl eax, cl
00364E0E  FF C8                           dec eax
00364E10  44 0B C8                        or r9d, eax
00364E13  49 8D 40 04                     lea rax, [r8 + 4]
00364E17  41 F7 D1                        not r9d
00364E1A  45 85 C9                        test r9d, r9d
00364E1D  75 16                           jne 0x140364e35
00364E1F  49 3B C3                        cmp rax, r11
00364E22  0F 87 75 04 00 00               ja 0x14036529d
00364E28  49 83 C0 04                     add r8, 4
00364E2C  48 83 C0 04                     add rax, 4
00364E30  45 8B 08                        mov r9d, dword ptr [r8]
00364E33  EB E2                           jmp 0x140364e17
00364E35  41 8B C1                        mov eax, r9d
00364E38  49 8B D0                        mov rdx, r8
00364E3B  48 0F BC C8                     bsf rcx, rax
00364E3F  48 8D 45 C7                     lea rax, [rbp - 0x39]
00364E43  48 2B D0                        sub rdx, rax
00364E46  89 4C 24 24                     mov dword ptr [rsp + 0x24], ecx
00364E4A  48 C1 FA 02                     sar rdx, 2
00364E4E  C1 E2 05                        shl edx, 5
00364E51  03 D1                           add edx, ecx
00364E53  41 3B D2                        cmp edx, r10d
00364E56  0F 87 41 04 00 00               ja 0x14036529d
00364E5C  B8 01 00 00 00                  mov eax, 1
00364E61  D3 E0                           shl eax, cl
00364E63  FF C8                           dec eax
00364E65  41 0B C1                        or eax, r9d
00364E68  F7 D0                           not eax
00364E6A  85 C0                           test eax, eax
00364E6C  75 14                           jne 0x140364e82
00364E6E  49 8D 40 04                     lea rax, [r8 + 4]
00364E72  49 3B C3                        cmp rax, r11
00364E75  0F 87 D7 04 00 00               ja 0x140365352
00364E7B  4C 8B C0                        mov r8, rax
00364E7E  8B 00                           mov eax, dword ptr [rax]
00364E80  EB E8                           jmp 0x140364e6a
00364E82  48 0F BC C0                     bsf rax, rax
00364E86  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00364E8A  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00364E8E  4C 2B C1                        sub r8, rcx
00364E91  49 8B F8                        mov rdi, r8
00364E94  48 C1 FF 02                     sar rdi, 2
00364E98  C1 E7 05                        shl edi, 5
00364E9B  03 F8                           add edi, eax
00364E9D  41 3B FA                        cmp edi, r10d
00364EA0  41 0F 47 FA                     cmova edi, r10d
00364EA4  2B FA                           sub edi, edx
00364EA6  85 FF                           test edi, edi
00364EA8  0F 84 F9 02 00 00               je 0x1403651a7
00364EAE  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00364EB3  8B F2                           mov esi, edx
00364EB5  8B C2                           mov eax, edx
00364EB7  2B F3                           sub esi, ebx
00364EB9  44 8B C7                        mov r8d, edi
00364EBC  49 C1 E0 03                     shl r8, 3
00364EC0  48 8D 14 C1                     lea rdx, [rcx + rax*8]
00364EC4  49 8D 0C C4                     lea rcx, [r12 + rax*8]
00364EC8  E8 73 19 36 00                  call 0x1406c6840
00364ECD  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00364ED2  03 FE                           add edi, esi
00364ED4  03 FB                           add edi, ebx
00364ED6  4C 2B E0                        sub r12, rax
00364ED9  4E 8D 3C F8                     lea r15, [rax + r15*8]
00364EDD  85 F6                           test esi, esi
00364EDF  74 6B                           je 0x140364f4c
00364EE1  8B 54 24 28                     mov edx, dword ptr [rsp + 0x28]
00364EE5  49 8B CF                        mov rcx, r15
00364EE8  E8 D3 09 00 00                  call 0x1403658c0
00364EED  48 85 C0                        test rax, rax
00364EF0  75 28                           jne 0x140364f1a
00364EF2  8B D3                           mov edx, ebx
00364EF4  8B C3                           mov eax, ebx
00364EF6  48 C1 EA 03                     shr rdx, 3
00364EFA  83 E0 07                        and eax, 7
00364EFD  0F BE 4C 15 C7                  movsx ecx, byte ptr [rbp + rdx - 0x39]
00364F02  0F B3 C1                        btr ecx, eax
00364F05  88 4C 15 C7                     mov byte ptr [rbp + rdx - 0x39], cl
00364F09  49 8B 0F                        mov rcx, qword ptr [r15]
00364F0C  4B 89 0C 3C                     mov qword ptr [r12 + r15], rcx
00364F10  FF C3                           inc ebx
00364F12  49 83 C7 08                     add r15, 8
00364F16  FF CE                           dec esi
00364F18  EB C3                           jmp 0x140364edd
00364F1A  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
00364F1E  83 4C 24 28 01                  or dword ptr [rsp + 0x28], 1
00364F23  FF C2                           inc edx
00364F25  F6 40 22 08                     test byte ptr [rax + 0x22], 8
00364F29  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00364F2D  0F 85 DA 02 00 00               jne 0x14036520d
00364F33  49 8B 0F                        mov rcx, qword ptr [r15]
00364F36  F6 C1 01                        test cl, 1
00364F39  75 D1                           jne 0x140364f0c
00364F3B  F6 40 22 20                     test byte ptr [rax + 0x22], 0x20
00364F3F  74 CB                           je 0x140364f0c
00364F41  FF 05 99 02 B9 00               inc dword ptr [rip + 0xb90299]
00364F47  E9 B7 00 00 00                  jmp 0x140365003
00364F4C  B8 00 02 00 00                  mov eax, 0x200
00364F51  3B F8                           cmp edi, eax
00364F53  0F 82 D8 02 00 00               jb 0x140365231
00364F59  48 BE FF FF FF FF FF FF FF 7F   movabs rsi, 0x7fffffffffffffff
00364F63  33 DB                           xor ebx, ebx
00364F65  39 5C 24 20                     cmp dword ptr [rsp + 0x20], ebx
00364F69  0F 84 76 02 00 00               je 0x1403651e5
00364F6F  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00364F76  0F 82 C2 02 00 00               jb 0x14036523e
00364F7C  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00364F80  B9 02 00 00 00                  mov ecx, 2
00364F85  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
00364F89  66 3B C1                        cmp ax, cx
00364F8C  0F 85 94 02 00 00               jne 0x140365226
00364F92  49 8B 5E 18                     mov rbx, qword ptr [r14 + 0x18]
00364F96  8D 4A 01                        lea ecx, [rdx + 1]
00364F99  0F B7 C3                        movzx eax, bx
00364F9C  48 3B C1                        cmp rax, rcx
00364F9F  75 57                           jne 0x140364ff8
00364FA1  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00364FA5  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
00364FAF  48 23 C1                        and rax, rcx
00364FB2  48 3D 00 00 01 00               cmp rax, 0x10000
00364FB8  73 3E                           jae 0x140364ff8
00364FBA  4C 8B 7D 9F                     mov r15, qword ptr [rbp - 0x61]
00364FBE  33 FF                           xor edi, edi
00364FC0  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
00364FC7  0F 82 90 02 00 00               jb 0x14036525d
00364FCD  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00364FD1  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
00364FDB  48 33 C3                        xor rax, rbx
00364FDE  48 23 C1                        and rax, rcx
00364FE1  48 33 C3                        xor rax, rbx
00364FE4  49 89 47 18                     mov qword ptr [r15 + 0x18], rax
00364FE8  F0 49 21 77 18                  lock and qword ptr [r15 + 0x18], rsi
00364FED  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
00364FF1  BF 01 00 00 00                  mov edi, 1
00364FF6  EB 0D                           jmp 0x140365005
00364FF8  FF 05 EA 01 B9 00               inc dword ptr [rip + 0xb901ea]
00364FFE  F0 49 21 76 18                  lock and qword ptr [r14 + 0x18], rsi
00365003  33 FF                           xor edi, edi
00365005  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00365009  4C 8D 7D C7                     lea r15, [rbp - 0x39]
0036500D  48 8B 05 6C B8 CA FF            mov rax, qword ptr [rip - 0x354794]
00365014  45 33 D2                        xor r10d, r10d
00365017  4C 8B 65 B7                     mov r12, qword ptr [rbp - 0x49]
0036501B  49 BD FF FF FF FF FF 00 00 00   movabs r13, 0xffffffffff
00365025  48 89 01                        mov qword ptr [rcx], rax
00365028  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0036502C  83 E1 04                        and ecx, 4
0036502F  8B C1                           mov eax, ecx
00365031  48 F7 D8                        neg rax
00365034  45 1B F6                        sbb r14d, r14d
00365037  41 83 E6 20                     and r14d, 0x20
0036503B  48 F7 D9                        neg rcx
0036503E  48 1B C0                        sbb rax, rax
00365041  83 E0 04                        and eax, 4
00365044  4C 2B F8                        sub r15, rax
00365047  85 D2                           test edx, edx
00365049  0F 84 35 01 00 00               je 0x140365184
0036504F  44 8B 4D 8F                     mov r9d, dword ptr [rbp - 0x71]
00365053  45 3B D1                        cmp r10d, r9d
00365056  45 1B C0                        sbb r8d, r8d
00365059  45 23 C2                        and r8d, r10d
0036505C  41 8D 41 FF                     lea eax, [r9 - 1]
00365060  83 65 87 00                     and dword ptr [rbp - 0x79], 0
00365064  46 8D 1C 30                     lea r11d, [rax + r14]
00365068  41 8B C3                        mov eax, r11d
0036506B  43 8D 0C 30                     lea ecx, [r8 + r14]
0036506F  2B C1                           sub eax, ecx
00365071  FF C0                           inc eax
00365073  83 F8 01                        cmp eax, 1
00365076  0F 82 E7 00 00 00               jb 0x140365163
0036507C  41 8B C3                        mov eax, r11d
0036507F  BA 01 00 00 00                  mov edx, 1
00365084  48 C1 E8 06                     shr rax, 6
00365088  49 8D 34 C7                     lea rsi, [r15 + rax*8]
0036508C  8B C1                           mov eax, ecx
0036508E  48 C1 E8 06                     shr rax, 6
00365092  80 E1 3F                        and cl, 0x3f
00365095  48 D3 E2                        shl rdx, cl
00365098  48 FF CA                        dec rdx
0036509B  49 8D 1C C7                     lea rbx, [r15 + rax*8]
0036509F  48 8B 03                        mov rax, qword ptr [rbx]
003650A2  48 F7 D0                        not rax
003650A5  48 0B D0                        or rdx, rax
003650A8  48 83 FA FF                     cmp rdx, -1
003650AC  75 15                           jne 0x1403650c3
003650AE  48 83 C3 08                     add rbx, 8
003650B2  48 3B DE                        cmp rbx, rsi
003650B5  0F 87 A8 00 00 00               ja 0x140365163
003650BB  48 8B 13                        mov rdx, qword ptr [rbx]
003650BE  48 F7 D2                        not rdx
003650C1  EB E5                           jmp 0x1403650a8
003650C3  49 2B DF                        sub rbx, r15
003650C6  48 F7 D2                        not rdx
003650C9  48 0F BC C2                     bsf rax, rdx
003650CD  48 C1 FB 03                     sar rbx, 3
003650D1  C1 E3 06                        shl ebx, 6
003650D4  03 D8                           add ebx, eax
003650D6  89 45 87                        mov dword ptr [rbp - 0x79], eax
003650D9  41 3B DB                        cmp ebx, r11d
003650DC  0F 87 81 00 00 00               ja 0x140365163
003650E2  83 FB FF                        cmp ebx, -1
003650E5  74 7F                           je 0x140365166
003650E7  41 2B DE                        sub ebx, r14d
003650EA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003650EF  48 8B 04 D9                     mov rax, qword ptr [rcx + rbx*8]
003650F3  A8 01                           test al, 1
003650F5  75 16                           jne 0x14036510d
003650F7  48 8B 0D 82 8B AC 00            mov rcx, qword ptr [rip + 0xac8b82]
003650FE  48 85 C9                        test rcx, rcx
00365101  74 0A                           je 0x14036510d
00365103  A8 10                           test al, 0x10
00365105  75 56                           jne 0x14036515d
00365107  48 F7 D1                        not rcx
0036510A  48 23 C1                        and rax, rcx
0036510D  48 C1 E8 0C                     shr rax, 0xc
00365111  49 23 C5                        and rax, r13
00365114  48 8D 34 40                     lea rsi, [rax + rax*2]
00365118  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00365122  48 C1 E6 04                     shl rsi, 4
00365126  48 8B C0                        mov rax, rax
00365129  48 03 F0                        add rsi, rax
0036512C  85 FF                           test edi, edi
0036512E  74 0B                           je 0x14036513b
00365130  49 8B D4                        mov rdx, r12
00365133  48 8B CE                        mov rcx, rsi
00365136  E8 85 EE FF FF                  call 0x140363fc0
0036513B  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
0036513F  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00365149  FF CA                           dec edx
0036514B  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
0036514F  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00365154  44 8D 53 01                     lea r10d, [rbx + 1]
00365158  E9 EA FE FF FF                  jmp 0x140365047
0036515D  48 83 E0 EF                     and rax, 0xffffffffffffffef
00365161  EB AA                           jmp 0x14036510d
00365163  83 CB FF                        or ebx, 0xffffffff
00365166  45 85 C0                        test r8d, r8d
00365169  0F 84 7B FF FF FF               je 0x1403650ea
0036516F  41 8D 42 01                     lea eax, [r10 + 1]
00365173  41 3B C1                        cmp eax, r9d
00365176  41 0F 47 C1                     cmova eax, r9d
0036517A  FF C8                           dec eax
0036517C  45 33 C0                        xor r8d, r8d
0036517F  E9 DC FE FF FF                  jmp 0x140365060
00365184  8B C7                           mov eax, edi
00365186  48 8B 4D 07                     mov rcx, qword ptr [rbp + 7]
0036518A  48 33 CC                        xor rcx, rsp
0036518D  E8 AE 74 34 00                  call 0x1406ac640
00365192  48 81 C4 D8 00 00 00            add rsp, 0xd8
00365199  41 5F                           pop r15
0036519B  41 5E                           pop r14
0036519D  41 5D                           pop r13
0036519F  41 5C                           pop r12
003651A1  5F                              pop rdi
003651A2  5E                              pop rsi
003651A3  5B                              pop rbx
003651A4  5D                              pop rbp
003651A5  C3                              ret
003651A6  CC                              int3
003651A7  41 8B F2                        mov esi, r10d
003651AA  2B F3                           sub esi, ebx
003651AC  E9 1C FD FF FF                  jmp 0x140364ecd
003651B1  33 C0                           xor eax, eax
003651B3  EB D1                           jmp 0x140365186
003651B5  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
003651BA  49 8D 0C FC                     lea rcx, [r12 + rdi*8]
003651BE  44 8B C3                        mov r8d, ebx
003651C1  44 2B C7                        sub r8d, edi
003651C4  49 C1 E0 03                     shl r8, 3
003651C8  48 8D 14 F8                     lea rdx, [rax + rdi*8]
003651CC  E8 6F 16 36 00                  call 0x1406c6840
003651D1  41 BA 00 02 00 00               mov r10d, 0x200
003651D7  41 3B DA                        cmp ebx, r10d
003651DA  0F 85 FB FB FF FF               jne 0x140364ddb
003651E0  E9 7E FD FF FF                  jmp 0x140364f63
003651E5  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
003651EC  0F 83 8A FD FF FF               jae 0x140364f7c
003651F2  FF C3                           inc ebx
003651F4  85 1D B2 00 C6 00               test dword ptr [rip + 0xc600b2], ebx
003651FA  0F 84 04 01 00 00               je 0x140365304
00365200  F3 90                           pause
00365202  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00365206  48 85 C0                        test rax, rax
00365209  79 DA                           jns 0x1403651e5
0036520B  EB E5                           jmp 0x1403651f2
0036520D  FF 05 D1 FF B8 00               inc dword ptr [rip + 0xb8ffd1]
00365213  E9 EB FD FF FF                  jmp 0x140365003
00365218  41 BA 00 02 00 00               mov r10d, 0x200
0036521E  41 8B DA                        mov ebx, r10d
00365221  E9 A3 FB FF FF                  jmp 0x140364dc9
00365226  FF 05 C0 FF B8 00               inc dword ptr [rip + 0xb8ffc0]
0036522C  E9 CD FD FF FF                  jmp 0x140364ffe
00365231  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
00365235  4C 8B 65 87                     mov r12, qword ptr [rbp - 0x79]
00365239  E9 CF FA FF FF                  jmp 0x140364d0d
0036523E  FF C3                           inc ebx
00365240  85 1D 66 00 C6 00               test dword ptr [rip + 0xc60066], ebx
00365246  0F 84 91 00 00 00               je 0x1403652dd
0036524C  F3 90                           pause
0036524E  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00365252  48 85 C0                        test rax, rax
00365255  0F 89 14 FD FF FF               jns 0x140364f6f
0036525B  EB E1                           jmp 0x14036523e
0036525D  FF C7                           inc edi
0036525F  85 3D 47 00 C6 00               test dword ptr [rip + 0xc60047], edi
00365265  0F 84 C0 00 00 00               je 0x14036532b
0036526B  F3 90                           pause
0036526D  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00365271  48 85 C0                        test rax, rax
00365274  0F 89 46 FD FF FF               jns 0x140364fc0
0036527A  EB E1                           jmp 0x14036525d
0036527C  41 8B DF                        mov ebx, r15d
0036527F  45 85 C0                        test r8d, r8d
00365282  0F 84 2A FB FF FF               je 0x140364db2
00365288  8D 47 01                        lea eax, [rdi + 1]
0036528B  41 3B C1                        cmp eax, r9d
0036528E  41 0F 47 C1                     cmova eax, r9d
00365292  41 03 C7                        add eax, r15d
00365295  45 33 C0                        xor r8d, r8d
00365298  E9 85 FA FF FF                  jmp 0x140364d22
0036529D  41 8B D2                        mov edx, r10d
003652A0  E9 01 FC FF FF                  jmp 0x140364ea6
003652A5  F6 C3 20                        test bl, 0x20
003652A8  0F 85 33 FA FF FF               jne 0x140364ce1
003652AE  48 8B C6                        mov rax, rsi
003652B1  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
003652BB  48 03 C1                        add rax, rcx
003652BE  48 3B F8                        cmp rdi, rax
003652C1  0F 82 1A FA FF FF               jb 0x140364ce1
003652C7  41 B8 80 00 00 00               mov r8d, 0x80
003652CD  48 8B D3                        mov rdx, rbx
003652D0  48 8B CF                        mov rcx, rdi
003652D3  E8 A8 DA F2 FF                  call 0x140292d80
003652D8  E9 04 FA FF FF                  jmp 0x140364ce1
003652DD  8B 05 D5 17 C6 00               mov eax, dword ptr [rip + 0xc617d5]
003652E3  A8 40                           test al, 0x40
003652E5  0F 84 61 FF FF FF               je 0x14036524c
003652EB  E8 A0 A1 FA FF                  call 0x14030f490
003652F0  84 C0                           test al, al
003652F2  0F 84 54 FF FF FF               je 0x14036524c
003652F8  8B CB                           mov ecx, ebx
003652FA  E8 61 A1 FA FF                  call 0x14030f460
003652FF  E9 4A FF FF FF                  jmp 0x14036524e
00365304  8B 05 AE 17 C6 00               mov eax, dword ptr [rip + 0xc617ae]
0036530A  A8 40                           test al, 0x40
0036530C  0F 84 EE FE FF FF               je 0x140365200
00365312  E8 79 A1 FA FF                  call 0x14030f490
00365317  84 C0                           test al, al
00365319  0F 84 E1 FE FF FF               je 0x140365200
0036531F  8B CB                           mov ecx, ebx
00365321  E8 3A A1 FA FF                  call 0x14030f460
00365326  E9 D7 FE FF FF                  jmp 0x140365202
0036532B  8B 05 87 17 C6 00               mov eax, dword ptr [rip + 0xc61787]
00365331  A8 40                           test al, 0x40
00365333  0F 84 32 FF FF FF               je 0x14036526b
00365339  E8 52 A1 FA FF                  call 0x14030f490
0036533E  84 C0                           test al, al
00365340  0F 84 25 FF FF FF               je 0x14036526b
00365346  8B CF                           mov ecx, edi
00365348  E8 13 A1 FA FF                  call 0x14030f460
0036534D  E9 1B FF FF FF                  jmp 0x14036526d
00365352  B8 20 00 00 00                  mov eax, 0x20
00365357  E9 2A FB FF FF                  jmp 0x140364e86
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReplacePageOfProtoPool(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p30;

    v_rsp = (v_rsp) - (216);
    result = (*(unsigned __int64 *)(v_rip + 11164520)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_mA8 = a3;
    a2 = 0;
    v_stack_mE8 = a1;
    v_stack_mD0 = 512;
    v_stack_mC8 = v_stack_m98;
    result = memset(v_stack_m98, a2, a2 + 64, a4);
    result = MiGetPrototypePteRanges(a1, v_stack_mD0, a2 + 64, a4);
    if ((unsigned int)(result) == 0) goto loc_003651B1;
    result = 0;
    v_stack_mF0 = 2;
    v_stack_mF8 = 0;
    v_r14 = (a2 + a2 * 2) << (4);
    v_r14 = (v_r14) + (a1);
    v_r15 = (a3 * 2) + (a3);
    v_r15 = (v_r15) << (4);
    v_r15 = (v_r15) + (a1);
    v_stack_mC0 = v_r15;
    result = MiGetUltraMapping(a4 + 96, 3, 3 - 2, 3 + 1);
    v_stack_mD8 = result;
    v_rdi = (result) >> (9);
    v_rdi = (v_rdi) & (result);
    v_rdi = (v_rdi) + (a1);
    v_stack_mB0 = v_rdi;
    result = MiMakeProtectionPfnCompatible(4, v_r15, 3 - 2, 3 + 1);
    result = (unsigned int)((result) | (0xA0000000ULL));
    result = MiMakeValidPte(v_rdi, a3, (unsigned int)((unsigned int)(result)), 3 + 1);
    if (condition_is_below) goto loc_003652A5;
loc_00364CE1:
    *(unsigned __int64 *)(v_rdi) = result;
    a1 = (unsigned int)((v_stack_m98) & (4));
    v_rdi = 0;
    result = -((unsigned int)((unsigned int)(a1)));
    v_r13 = (unsigned int)((a3) & (32));
    a1 = -(a1);
    result = (unsigned int)((result) & (4));
    v_rsi = (v_stack_m98) - (result);
    v_stack_mB8 = v_rsi;
loc_00364D0D:
    v_r15 = (unsigned int)((v_r15) | (0xFFFFFFFFULL));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0));
loc_00364D22:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0) - 1 + v_r13 * 1))) - ((unsigned int)(a3 + v_r13 * 1)));
    result = (unsigned int)((result) + 1);
    if (((unsigned int)(result)) < 1) goto loc_0036527C;
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0) - 1 + v_r13 * 1))) >> (6);
    result = ((unsigned int)((unsigned int)(a3 + v_r13 * 1))) >> (6);
    a1 = (unsigned __int8)((a3 + v_r13 * 1) & (63));
    a2 = (1) << ((unsigned __int8)(a1));
    a2 = (a2) - 1;
    result = ~(*(unsigned __int64 *)(v_rsi + result * 8));
    a2 = (a2) | (result);
loc_00364D6B:
    if (a2 != -1) goto loc_00364D86;
    v_rbx = (v_rsi + result * 8) + (8);
    if (v_rbx > (v_rsi + result * 8)) goto loc_0036527C;
    a2 = ~(*(unsigned __int64 *)(v_rbx));
    goto loc_00364D6B;
loc_00364D86:
    v_rbx = (v_rbx) - (v_rsi);
    a2 = ~(a2);
    v_rbx = (v_rbx) >> (3);
    v_rbx = (unsigned int)((v_rbx) << (6));
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(result)));
    v_stack_mE0 = (unsigned int)(result);
    if (((unsigned int)(v_rbx)) > ((unsigned int)((unsigned int)(v_stack_mD0) - 1 + v_r13 * 1))) goto loc_0036527C;
    if (((unsigned int)(v_rbx)) == ((unsigned int)(v_r15))) goto loc_0036527F;
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_r13)));
loc_00364DB2:
    if (((unsigned int)(v_rbx)) < 0) goto loc_00365218;
    if (((unsigned int)(v_rbx)) == ((unsigned int)(v_r15))) goto loc_00365218;
loc_00364DC9:
    if (((unsigned int)(v_rbx)) != 0) goto loc_003651B5;
loc_00364DDB:
    v_rdi = 0;
    if (((unsigned int)(v_rbx)) >= 512) goto loc_003651A7;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx))))) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (31));
    result = (unsigned int)((v_rdi + 1) << ((unsigned __int8)(a1)));
    result = (unsigned int)((result) - 1);
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m98 + result * 4))) | ((unsigned int)(result)));
loc_00364E17:
    a4 = (unsigned int)(~(a4));
    if ((unsigned int)(a4) != 0) goto loc_00364E35;
    if ((v_stack_m98 + result * 4 + 4) > v_stack_m5C) goto loc_0036529D;
    a3 = (v_stack_m98 + result * 4) + (4);
    result = (v_stack_m98 + result * 4 + 4) + (4);
    goto loc_00364E17;
loc_00364E35:
    a2 = (a3) - (v_stack_m98);
    v_stack_mF4 = (unsigned int)(a1);
    a2 = (a2) >> (2);
    a2 = (unsigned int)((a2) << (5));
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    if (((unsigned int)(a2)) > 512) goto loc_0036529D;
    result = (unsigned int)((1) << ((unsigned __int8)(a1)));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) | ((unsigned int)((unsigned int)(*(unsigned int *)(a3)))));
    result = (unsigned int)(~(result));
loc_00364E6A:
    if ((unsigned int)(result) != 0) goto loc_00364E82;
    if ((a3 + 4) > v_stack_m5C) goto loc_00365352;
    goto loc_00364E6A;
loc_00364E82:
loc_00364E86:
    v_stack_mF4 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)));
    a3 = (a3 + 4) - (v_stack_m98);
    v_rdi = (a3) >> (2);
    v_rdi = (unsigned int)((v_rdi) << (5));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))));
    if (((unsigned int)(v_rdi)) > 512) { v_rdi = 512; }
    v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(a2)));
loc_00364EA6:
    if ((unsigned int)(v_rdi) == 0) goto loc_003651A7;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(v_rbx)));
    a3 = ((unsigned int)((unsigned int)(v_rdi))) << (3);
    result = memcpy(result + (unsigned int)((unsigned int)(a2)) * 8, v_stack_mE8 + (unsigned int)((unsigned int)(a2)) * 8, a3, (unsigned int)(*(unsigned int *)(a3)));
loc_00364ECD:
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rsi)));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rbx)));
    v_r12 = (result) - (v_stack_mE8);
loc_00364EDD:
    if ((unsigned int)(v_rsi) == 0) goto loc_00364F4C;
    result = MiLockLeafPage(v_stack_mE8 + (unsigned int)((unsigned int)(v_rbx)) * 8, (unsigned int)(v_stack_mF0), a3, (unsigned int)(*(unsigned int *)(a3)));
    if (result != 0) goto loc_00364F1A;
    a2 = ((unsigned int)((unsigned int)(v_rbx))) >> (3);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (7));
    *(unsigned __int8 *)(v_stack_m5F + a2 * 1 - 57) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(v_stack_m5F + a2 * 1 - 57)));
loc_00364F0C:
    *(unsigned __int64 *)(v_r12 + v_stack_mE8 + (unsigned int)((unsigned int)(v_rbx)) * 8 * 1) = *(unsigned __int64 *)(v_stack_mE8 + (unsigned int)((unsigned int)(v_rbx)) * 8);
    v_rbx = (unsigned int)((v_rbx) + 1);
    v_r15 = (v_stack_mE8 + (unsigned int)((unsigned int)(v_rbx)) * 8) + (8);
    v_rsi = (unsigned int)((v_rsi) - 1);
    goto loc_00364EDD;
loc_00364F1A:
    a2 = (unsigned int)(((unsigned int)(v_stack_mF8)) + 1);
    v_stack_mF8 = (unsigned int)(a2);
    if (((*(unsigned __int8 *)(result + 34)) & (8)) != 0) goto loc_0036520D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) != 0) goto loc_00364F0C;
    if (((*(unsigned __int8 *)(result + 34)) & (32)) == 0) goto loc_00364F0C;
    goto loc_00365003;
loc_00364F4C:
    if (((unsigned int)(v_rdi)) < 512) goto loc_00365231;
loc_00364F63:
    v_rbx = 0;
    if (v_stack_mF8 == 0) goto loc_003651E5;
loc_00364F6F:
    if (v_stack_mF8 < 0) goto loc_0036523E;
loc_00364F7C:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r14 + 32)))) != 2) goto loc_00365226;
    if (((unsigned __int16)(*(unsigned __int64 *)(v_r14 + 24))) != ((unsigned int)(v_stack_mF8) + 1)) goto loc_00364FF8;
    result = (*(unsigned __int64 *)(v_r14 + 24)) & ((unsigned int)(v_stack_mF8) + 1);
    if (result >= 0x10000ULL) goto loc_00364FF8;
    v_rdi = 0;
loc_00364FC0:
    if (condition_is_below) goto loc_0036525D;
    result = (*(unsigned __int64 *)(v_stack_mC0 + 24)) ^ (*(unsigned __int64 *)(v_r14 + 24));
    result = (result) & ((unsigned int)(v_stack_mF8) + 1);
    result = (result) ^ (*(unsigned __int64 *)(v_r14 + 24));
    *(unsigned __int64 *)(v_stack_mC0 + 24) = result;
    goto loc_00365005;
loc_00364FF8:
loc_00364FFE:
loc_00365003:
    v_rdi = 0;
loc_00365005:
    v_r10 = 0;
    *(unsigned __int64 *)(v_stack_mB0) = *(unsigned __int64 *)(v_rip - 3491732);
    a1 = (unsigned int)((v_stack_m98) & (4));
    result = -((unsigned int)((unsigned int)(a1)));
    v_r14 = (unsigned int)((v_r14) & (32));
    a1 = -(a1);
    result = (unsigned int)((result) & (4));
    v_r15 = (v_stack_m98) - (result);
loc_00365047:
    if ((unsigned int)((unsigned int)(v_stack_mF8)) == 0) goto loc_00365184;
    a3 = (unsigned int)((a3) & (0));
loc_00365060:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0) - 1 + v_r14 * 1))) - ((unsigned int)(a3 + v_r14 * 1)));
    result = (unsigned int)((result) + 1);
    if (((unsigned int)(result)) < 1) goto loc_00365163;
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0) - 1 + v_r14 * 1))) >> (6);
    result = ((unsigned int)((unsigned int)(a3 + v_r14 * 1))) >> (6);
    a1 = (unsigned __int8)((a3 + v_r14 * 1) & (63));
    a2 = (1) << ((unsigned __int8)(a1));
    a2 = (a2) - 1;
    result = ~(*(unsigned __int64 *)(v_r15 + result * 8));
    a2 = (a2) | (result);
loc_003650A8:
    if (a2 != -1) goto loc_003650C3;
    v_rbx = (v_r15 + result * 8) + (8);
    if (v_rbx > (v_r15 + result * 8)) goto loc_00365163;
    a2 = ~(*(unsigned __int64 *)(v_rbx));
    goto loc_003650A8;
loc_003650C3:
    v_rbx = (v_rbx) - (v_r15);
    a2 = ~(a2);
    v_rbx = (v_rbx) >> (3);
    v_rbx = (unsigned int)((v_rbx) << (6));
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(result)));
    v_stack_mD8 = (unsigned int)(result);
    if (((unsigned int)(v_rbx)) > ((unsigned int)((unsigned int)(v_stack_mD0) - 1 + v_r14 * 1))) goto loc_00365163;
    if (((unsigned int)(v_rbx)) == -1) goto loc_00365166;
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_r14)));
loc_003650EA:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_mE8 + v_rbx * 8))) & (1)) != 0) goto loc_0036510D;
    if (*(unsigned __int64 *)(v_rip + 11307906) == 0) goto loc_0036510D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_mE8 + v_rbx * 8))) & (16)) != 0) goto loc_0036515D;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11307906));
    result = (*(unsigned __int64 *)(v_stack_mE8 + v_rbx * 8)) & (a1);
loc_0036510D:
    result = (result) >> (12);
    result = (result) & (v_r13);
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (result);
    if (0 != 0) {
        a2 = v_stack_mA8;
        a1 = v_rsi;
        result = MiSetPfnContainingFrame(a1, a2, a3, (unsigned int)(v_stack_mD0));
    }
    a2 = (unsigned int)(((unsigned int)(v_stack_mF8)) - 1);
    v_stack_mF8 = (unsigned int)(a2);
    goto loc_00365047;
loc_0036515D:
    result = (result) & (-17);
    goto loc_0036510D;
loc_00365163:
    v_rbx = (unsigned int)((v_rbx) | (0xFFFFFFFFULL));
loc_00365166:
    if ((unsigned int)(a3) == 0) goto loc_003650EA;
    result = v_rbx + 1 + 1;
    if (((unsigned int)(v_rbx + 1 + 1)) > ((unsigned int)((unsigned int)(v_stack_mD0)))) { result = (unsigned int)((unsigned int)(v_stack_mD0)); }
    result = (unsigned int)((result) - 1);
    a3 = 0;
    goto loc_00365060;
loc_00365184:
loc_00365186:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)(v_stack_mD0));
    v_rsp = (v_rsp) + (216);
    return result;
loc_003651A7:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rbx + 1))) - ((unsigned int)(v_rbx)));
    goto loc_00364ECD;
loc_003651B1:
    result = 0;
    goto loc_00365186;
loc_003651B5:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (0));
    a3 = (a3) << (3);
    result = memcpy(v_stack_mA8 + v_rdi * 8, v_stack_p30 + v_rdi * 8, a3, (unsigned int)(v_stack_mD0));
    if (((unsigned int)(v_rbx)) != 512) goto loc_00364DDB;
    goto loc_00364F63;
loc_003651E5:
    if (((unsigned int)(v_rbx)) >= 512) goto loc_00364F7C;
loc_003651F2:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 12976306)) & ((unsigned int)(v_rbx))) == 0) goto loc_00365304;
loc_00365200:
loc_00365202:
    if (!sign_flag) goto loc_003651E5;
    goto loc_003651F2;
loc_0036520D:
    goto loc_00365003;
loc_00365218:
    goto loc_00364DC9;
loc_00365226:
    goto loc_00364FFE;
loc_00365231:
    goto loc_00364D0D;
loc_0036523E:
    v_rbx = (unsigned int)((512) + 1);
    if (((*(unsigned int *)(v_rip + 12976230)) & ((unsigned int)(v_rbx))) == 0) goto loc_003652DD;
loc_0036524C:
loc_0036524E:
    if (!sign_flag) goto loc_00364F6F;
    goto loc_0036523E;
loc_0036525D:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 12976199)) & ((unsigned int)(v_rdi))) == 0) goto loc_0036532B;
loc_0036526B:
loc_0036526D:
    if (!sign_flag) goto loc_00364FC0;
    goto loc_0036525D;
loc_0036527C:
loc_0036527F:
    if ((unsigned int)(a3) == 0) goto loc_00364DB2;
    result = v_rdi + 1;
    if (((unsigned int)(v_rdi + 1)) > ((unsigned int)((unsigned int)(v_stack_mD0)))) { result = (unsigned int)((unsigned int)(v_stack_mD0)); }
    result = (unsigned int)((result) + ((unsigned int)(v_r15)));
    a3 = 0;
    goto loc_00364D22;
loc_0036529D:
    goto loc_00364EA6;
loc_003652A5:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_r15)))) & (32)) != 0) goto loc_00364CE1;
    result = (v_stack_mB8) + (v_stack_mA8 + v_rdi * 8);
    if (v_rdi < result) goto loc_00364CE1;
    result = MiCheckLinearProtectedPteAccessedBit(v_rdi, (unsigned int)((unsigned int)(v_r15)), 128, (unsigned int)(v_stack_mD0));
    goto loc_00364CE1;
loc_003652DD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12982229)))) & (64)) == 0) goto loc_0036524C;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rdi, (unsigned int)((unsigned int)(v_r15)), 128, (unsigned int)(v_stack_mD0));
    if ((unsigned __int8)(result) == 0) goto loc_0036524C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))), (unsigned int)((unsigned int)(v_r15)), 128, (unsigned int)(v_stack_mD0));
    goto loc_0036524E;
loc_00365304:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12982190)))) & (64)) == 0) goto loc_00365200;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))), (unsigned int)((unsigned int)(v_r15)), 128, (unsigned int)(v_stack_mD0));
    if ((unsigned __int8)(result) == 0) goto loc_00365200;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))), (unsigned int)((unsigned int)(v_r15)), 128, (unsigned int)(v_stack_mD0));
    goto loc_00365202;
loc_0036532B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12982151)))) & (64)) == 0) goto loc_0036526B;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))), (unsigned int)((unsigned int)(v_r15)), 128, (unsigned int)(v_stack_mD0));
    if ((unsigned __int8)(result) == 0) goto loc_0036526B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(v_r15)), 128, (unsigned int)(v_stack_mD0));
    goto loc_0036526D;
loc_00365352:
    goto loc_00364E86;
}
```

## 5. (Beta) C Style

```c
int64_t MiReplacePageOfProtoPool(int64_t Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p30;

    local_rsp = (local_rsp) - (216);
    result = (*(uint64_t *)(v_rip + 0xAA5B68)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_mA8 = Arg3;
    Arg2 = 0;
    v_stack_mE8 = Arg1;
    v_stack_mD0 = 512;
    v_stack_mC8 = v_stack_m98;
    result = memset(v_stack_m98, Arg2, Arg2 + 64, Arg4);
    result = MiGetPrototypePteRanges(Arg1, v_stack_mD0, Arg2 + 64, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003651B1;
    result = 0;
    v_stack_mF0 = 2;
    v_stack_mF8 = 0;
    local_r14 = (Arg2 + Arg2 * 2) << (4);
    local_r14 = (local_r14) + (Arg1);
    local_r15 = (Arg3 * 2) + (Arg3);
    local_r15 = (local_r15) << (4);
    local_r15 = (local_r15) + (Arg1);
    v_stack_mC0 = local_r15;
    result = MiGetUltraMapping(Arg4 + 96, 3, 3 - 2, 3 + 1);
    v_stack_mD8 = result;
    local_rdi = (result) >> (9);
    local_rdi = (local_rdi) & (result);
    local_rdi = (local_rdi) + (Arg1);
    v_stack_mB0 = local_rdi;
    result = MiMakeProtectionPfnCompatible(4, local_r15, 3 - 2, 3 + 1);
    result = (uint32_t)((result) | (0xA0000000ULL));
    result = MiMakeValidPte(local_rdi, Arg3, (uint32_t)((uint32_t)(result)), 3 + 1);
    if (condition_is_below) goto loc_003652A5;
loc_00364CE1:
    *(uint64_t *)(local_rdi) = result;
    Arg1 = (uint32_t)((v_stack_m98) & (4));
    local_rdi = 0;
    result = -((uint32_t)((uint32_t)(Arg1)));
    local_r13 = (uint32_t)((Arg3) & (32));
    Arg1 = -(Arg1);
    result = (uint32_t)((result) & (4));
    local_rsi = (v_stack_m98) - (result);
    v_stack_mB8 = local_rsi;
loc_00364D0D:
    local_r15 = (uint32_t)((local_r15) | (0xFFFFFFFFULL));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0));
loc_00364D22:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0) - 1 + local_r13 * 1))) - ((uint32_t)(Arg3 + local_r13 * 1)));
    result = (uint32_t)((result) + 1);
    if (((uint32_t)(result)) < 1) goto loc_0036527C;
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0) - 1 + local_r13 * 1))) >> (6);
    result = ((uint32_t)((uint32_t)(Arg3 + local_r13 * 1))) >> (6);
    Arg1 = (uint8_t)((Arg3 + local_r13 * 1) & (63));
    Arg2 = (1) << ((uint8_t)(Arg1));
    Arg2 = (Arg2) - 1;
    result = ~(*(uint64_t *)(local_rsi + result * 8));
    Arg2 = (Arg2) | (result);
loc_00364D6B:
    if (Arg2 != -1) goto loc_00364D86;
    local_rbx = (local_rsi + result * 8) + (8);
    if (local_rbx > (local_rsi + result * 8)) goto loc_0036527C;
    Arg2 = ~(*(uint64_t *)(local_rbx));
    goto loc_00364D6B;
loc_00364D86:
    local_rbx = (local_rbx) - (local_rsi);
    Arg2 = ~(Arg2);
    local_rbx = (local_rbx) >> (3);
    local_rbx = (uint32_t)((local_rbx) << (6));
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(result)));
    v_stack_mE0 = (uint32_t)(result);
    if (((uint32_t)(local_rbx)) > ((uint32_t)((uint32_t)(v_stack_mD0) - 1 + local_r13 * 1))) goto loc_0036527C;
    if (((uint32_t)(local_rbx)) == ((uint32_t)(local_r15))) goto loc_0036527F;
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_r13)));
loc_00364DB2:
    if (((uint32_t)(local_rbx)) < 0) goto loc_00365218;
    if (((uint32_t)(local_rbx)) == ((uint32_t)(local_r15))) goto loc_00365218;
loc_00364DC9:
    if (((uint32_t)(local_rbx)) != 0) goto loc_003651B5;
loc_00364DDB:
    local_rdi = 0;
    if (((uint32_t)(local_rbx)) >= 512) goto loc_003651A7;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx))))) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (31));
    result = (uint32_t)((local_rdi + 1) << ((uint8_t)(Arg1)));
    result = (uint32_t)((result) - 1);
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m98 + result * 4))) | ((uint32_t)(result)));
loc_00364E17:
    Arg4 = (uint32_t)(~(Arg4));
    if ((uint32_t)(Arg4) != 0) goto loc_00364E35;
    if ((v_stack_m98 + result * 4 + 4) > v_stack_m5C) goto loc_0036529D;
    Arg3 = (v_stack_m98 + result * 4) + (4);
    result = (v_stack_m98 + result * 4 + 4) + (4);
    goto loc_00364E17;
loc_00364E35:
    Arg2 = (Arg3) - (v_stack_m98);
    v_stack_mF4 = (uint32_t)(Arg1);
    Arg2 = (Arg2) >> (2);
    Arg2 = (uint32_t)((Arg2) << (5));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
    if (((uint32_t)(Arg2)) > 512) goto loc_0036529D;
    result = (uint32_t)((1) << ((uint8_t)(Arg1)));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) | ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))));
    result = (uint32_t)(~(result));
loc_00364E6A:
    if ((uint32_t)(result) != 0) goto loc_00364E82;
    if ((Arg3 + 4) > v_stack_m5C) goto loc_00365352;
    goto loc_00364E6A;
loc_00364E82:
loc_00364E86:
    v_stack_mF4 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)));
    Arg3 = (Arg3 + 4) - (v_stack_m98);
    local_rdi = (Arg3) >> (2);
    local_rdi = (uint32_t)((local_rdi) << (5));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)))));
    if (((uint32_t)(local_rdi)) > 512) { local_rdi = 512; }
    local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(Arg2)));
loc_00364EA6:
    if ((uint32_t)(local_rdi) == 0) goto loc_003651A7;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(local_rbx)));
    Arg3 = ((uint32_t)((uint32_t)(local_rdi))) << (3);
    result = memcpy(result + (uint32_t)((uint32_t)(Arg2)) * 8, v_stack_mE8 + (uint32_t)((uint32_t)(Arg2)) * 8, Arg3, (uint32_t)(*(uint32_t *)(Arg3)));
loc_00364ECD:
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rsi)));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rbx)));
    local_r12 = (result) - (v_stack_mE8);
loc_00364EDD:
    if ((uint32_t)(local_rsi) == 0) goto loc_00364F4C;
    result = MiLockLeafPage(v_stack_mE8 + (uint32_t)((uint32_t)(local_rbx)) * 8, (uint32_t)(v_stack_mF0), Arg3, (uint32_t)(*(uint32_t *)(Arg3)));
    if (result != 0) goto loc_00364F1A;
    Arg2 = ((uint32_t)((uint32_t)(local_rbx))) >> (3);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (7));
    *(uint8_t *)(v_stack_m5F + arg2 * 1 - 0x39) = (uint8_t)((int8_t)(*(uint8_t *)(v_stack_m5F + arg2 * 1 - 0x39)));
loc_00364F0C:
    *(uint64_t *)(local_r12 + v_stack_mE8 + (uint32_t)((uint32_t)(local_rbx)) * 8 * 1) = *(uint64_t *)(v_stack_mE8 + (uint32_t)((uint32_t)(local_rbx)) * 8);
    local_rbx = (uint32_t)((local_rbx) + 1);
    local_r15 = (v_stack_mE8 + (uint32_t)((uint32_t)(local_rbx)) * 8) + (8);
    local_rsi = (uint32_t)((local_rsi) - 1);
    goto loc_00364EDD;
loc_00364F1A:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mF8)) + 1);
    v_stack_mF8 = (uint32_t)(Arg2);
    if (((*(uint8_t *)(result + 0x22)) & (8)) != 0) goto loc_0036520D;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) != 0) goto loc_00364F0C;
    if (((*(uint8_t *)(result + 0x22)) & (32)) == 0) goto loc_00364F0C;
    goto loc_00365003;
loc_00364F4C:
    if (((uint32_t)(local_rdi)) < 512) goto loc_00365231;
loc_00364F63:
    local_rbx = 0;
    if (v_stack_mF8 == 0) goto loc_003651E5;
loc_00364F6F:
    if (v_stack_mF8 < 0) goto loc_0036523E;
loc_00364F7C:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)))) != 2) goto loc_00365226;
    if (((uint16_t)(*(uint64_t *)(local_r14 + 0x18))) != ((uint32_t)(v_stack_mF8) + 1)) goto loc_00364FF8;
    result = (*(uint64_t *)(local_r14 + 0x18)) & ((uint32_t)(v_stack_mF8) + 1);
    if (result >= 0x10000ULL) goto loc_00364FF8;
    local_rdi = 0;
loc_00364FC0:
    if (condition_is_below) goto loc_0036525D;
    result = (*(uint64_t *)(v_stack_mC0 + 0x18)) ^ (*(uint64_t *)(local_r14 + 0x18));
    result = (result) & ((uint32_t)(v_stack_mF8) + 1);
    result = (result) ^ (*(uint64_t *)(local_r14 + 0x18));
    *(uint64_t *)(v_stack_mC0 + 0x18) = result;
    goto loc_00365005;
loc_00364FF8:
loc_00364FFE:
loc_00365003:
    local_rdi = 0;
loc_00365005:
    local_r10 = 0;
    *(uint64_t *)(v_stack_mB0) = *(uint64_t *)(v_rip - 0x354794);
    Arg1 = (uint32_t)((v_stack_m98) & (4));
    result = -((uint32_t)((uint32_t)(Arg1)));
    local_r14 = (uint32_t)((local_r14) & (32));
    Arg1 = -(Arg1);
    result = (uint32_t)((result) & (4));
    local_r15 = (v_stack_m98) - (result);
loc_00365047:
    if ((uint32_t)((uint32_t)(v_stack_mF8)) == 0) goto loc_00365184;
    Arg3 = (uint32_t)((Arg3) & (0));
loc_00365060:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0) - 1 + local_r14 * 1))) - ((uint32_t)(Arg3 + local_r14 * 1)));
    result = (uint32_t)((result) + 1);
    if (((uint32_t)(result)) < 1) goto loc_00365163;
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0) - 1 + local_r14 * 1))) >> (6);
    result = ((uint32_t)((uint32_t)(Arg3 + local_r14 * 1))) >> (6);
    Arg1 = (uint8_t)((Arg3 + local_r14 * 1) & (63));
    Arg2 = (1) << ((uint8_t)(Arg1));
    Arg2 = (Arg2) - 1;
    result = ~(*(uint64_t *)(local_r15 + result * 8));
    Arg2 = (Arg2) | (result);
loc_003650A8:
    if (Arg2 != -1) goto loc_003650C3;
    local_rbx = (local_r15 + result * 8) + (8);
    if (local_rbx > (local_r15 + result * 8)) goto loc_00365163;
    Arg2 = ~(*(uint64_t *)(local_rbx));
    goto loc_003650A8;
loc_003650C3:
    local_rbx = (local_rbx) - (local_r15);
    Arg2 = ~(Arg2);
    local_rbx = (local_rbx) >> (3);
    local_rbx = (uint32_t)((local_rbx) << (6));
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(result)));
    v_stack_mD8 = (uint32_t)(result);
    if (((uint32_t)(local_rbx)) > ((uint32_t)((uint32_t)(v_stack_mD0) - 1 + local_r14 * 1))) goto loc_00365163;
    if (((uint32_t)(local_rbx)) == -1) goto loc_00365166;
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_r14)));
loc_003650EA:
    if ((((uint8_t)(*(uint64_t *)(v_stack_mE8 + local_rbx * 8))) & (1)) != 0) goto loc_0036510D;
    if (*(uint64_t *)(v_rip + 0xAC8B82) == 0) goto loc_0036510D;
    if ((((uint8_t)(*(uint64_t *)(v_stack_mE8 + local_rbx * 8))) & (16)) != 0) goto loc_0036515D;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xAC8B82));
    result = (*(uint64_t *)(v_stack_mE8 + local_rbx * 8)) & (Arg1);
loc_0036510D:
    result = (result) >> (12);
    result = (result) & (local_r13);
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (result);
    if (0 != 0) {
        Arg2 = v_stack_mA8;
        Arg1 = local_rsi;
        result = MiSetPfnContainingFrame(Arg1, Arg2, Arg3, (uint32_t)(v_stack_mD0));
    }
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mF8)) - 1);
    v_stack_mF8 = (uint32_t)(Arg2);
    goto loc_00365047;
loc_0036515D:
    result = (result) & (-17);
    goto loc_0036510D;
loc_00365163:
    local_rbx = (uint32_t)((local_rbx) | (0xFFFFFFFFULL));
loc_00365166:
    if ((uint32_t)(Arg3) == 0) goto loc_003650EA;
    result = local_rbx + 1 + 1;
    if (((uint32_t)(local_rbx + 1 + 1)) > ((uint32_t)((uint32_t)(v_stack_mD0)))) { result = (uint32_t)((uint32_t)(v_stack_mD0)); }
    result = (uint32_t)((result) - 1);
    Arg3 = 0;
    goto loc_00365060;
loc_00365184:
loc_00365186:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (uint32_t)(v_stack_mD0));
    local_rsp = (local_rsp) + (216);
    return result;
loc_003651A7:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rbx + 1))) - ((uint32_t)(local_rbx)));
    goto loc_00364ECD;
loc_003651B1:
    result = 0;
    goto loc_00365186;
loc_003651B5:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (0));
    Arg3 = (Arg3) << (3);
    result = memcpy(v_stack_mA8 + local_rdi * 8, v_stack_p30 + local_rdi * 8, Arg3, (uint32_t)(v_stack_mD0));
    if (((uint32_t)(local_rbx)) != 512) goto loc_00364DDB;
    goto loc_00364F63;
loc_003651E5:
    if (((uint32_t)(local_rbx)) >= 512) goto loc_00364F7C;
loc_003651F2:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xC600B2)) & ((uint32_t)(local_rbx))) == 0) goto loc_00365304;
loc_00365200:
loc_00365202:
    if (!sign_flag) goto loc_003651E5;
    goto loc_003651F2;
loc_0036520D:
    goto loc_00365003;
loc_00365218:
    goto loc_00364DC9;
loc_00365226:
    goto loc_00364FFE;
loc_00365231:
    goto loc_00364D0D;
loc_0036523E:
    local_rbx = (uint32_t)((512) + 1);
    if (((*(uint32_t *)(v_rip + 0xC60066)) & ((uint32_t)(local_rbx))) == 0) goto loc_003652DD;
loc_0036524C:
loc_0036524E:
    if (!sign_flag) goto loc_00364F6F;
    goto loc_0036523E;
loc_0036525D:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC60047)) & ((uint32_t)(local_rdi))) == 0) goto loc_0036532B;
loc_0036526B:
loc_0036526D:
    if (!sign_flag) goto loc_00364FC0;
    goto loc_0036525D;
loc_0036527C:
loc_0036527F:
    if ((uint32_t)(Arg3) == 0) goto loc_00364DB2;
    result = local_rdi + 1;
    if (((uint32_t)(local_rdi + 1)) > ((uint32_t)((uint32_t)(v_stack_mD0)))) { result = (uint32_t)((uint32_t)(v_stack_mD0)); }
    result = (uint32_t)((result) + ((uint32_t)(local_r15)));
    Arg3 = 0;
    goto loc_00364D22;
loc_0036529D:
    goto loc_00364EA6;
loc_003652A5:
    if ((((uint8_t)((uint32_t)((uint32_t)(local_r15)))) & (32)) != 0) goto loc_00364CE1;
    result = (v_stack_mB8) + (v_stack_mA8 + local_rdi * 8);
    if (local_rdi < result) goto loc_00364CE1;
    result = MiCheckLinearProtectedPteAccessedBit(local_rdi, (uint32_t)((uint32_t)(local_r15)), 128, (uint32_t)(v_stack_mD0));
    goto loc_00364CE1;
loc_003652DD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC617D5)))) & (64)) == 0) goto loc_0036524C;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rdi, (uint32_t)((uint32_t)(local_r15)), 128, (uint32_t)(v_stack_mD0));
    if ((uint8_t)(result) == 0) goto loc_0036524C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))), (uint32_t)((uint32_t)(local_r15)), 128, (uint32_t)(v_stack_mD0));
    goto loc_0036524E;
loc_00365304:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC617AE)))) & (64)) == 0) goto loc_00365200;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))), (uint32_t)((uint32_t)(local_r15)), 128, (uint32_t)(v_stack_mD0));
    if ((uint8_t)(result) == 0) goto loc_00365200;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))), (uint32_t)((uint32_t)(local_r15)), 128, (uint32_t)(v_stack_mD0));
    goto loc_00365202;
loc_0036532B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC61787)))) & (64)) == 0) goto loc_0036526B;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))), (uint32_t)((uint32_t)(local_r15)), 128, (uint32_t)(v_stack_mD0));
    if ((uint8_t)(result) == 0) goto loc_0036526B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(local_r15)), 128, (uint32_t)(v_stack_mD0));
    goto loc_0036526D;
loc_00365352:
    goto loc_00364E86;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rbx*2` | `64` | `R` |
| `Arg4` | `+ 0x60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00364BB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
