# MiDeleteSectionCluster

- RVA: `0x00373DF0`–`0x0037441C` (길이 `1,580` bytes)
- VA: `0x0000000140373DF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007AAB8`
- 디코드: `398`개 명령, `1,580/1,580` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00373E66` → [MiTryLockLeafPage](MiTryLockLeafPage_function_003728DC.md) (function, `0x003728DC`)
- `0x00373F22` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x00373F3E` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x00373F6D` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x00373FB6` → [MiTransferSoftwarePte](../38/MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x00374037` → [MiSetPfnIdentity](../2A/MiSetPfnIdentity_function_002A2350.md) (function, `0x002A2350`)
- `0x00374049` → [MiClearPfnReuseFields](MiClearPfnReuseFields_function_003759F0.md) (function, `0x003759F0`)
- `0x00374050` → [MiSetPfnModified](../36/MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x003740E3` → [MiDereferenceControlAreaPfnList](../2A/MiDereferenceControlAreaPfnList_function_002A45E8.md) (function, `0x002A45E8`)
- `0x00374206` → [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x0037427F` → [MiInitializeAllResidentPageBasePfns](../46/MiInitializeAllResidentPageBasePfns_function_00462AF8.md) (function, `0x00462AF8`)
- `0x003742A0` → [MiCreateInitialLargeLeafPfns](../44/MiCreateInitialLargeLeafPfns_function_004428E0.md) (function, `0x004428E0`)
- `0x003742DA` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x0037431C` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x0037433B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0037434D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00374375` → [MiClearPfnImageVerified](../40/MiClearPfnImageVerified_function_00407000.md) (function, `0x00407000`)
- `0x00374394` → [MiBadShareCount](MiBadShareCount_function_00370EF8.md) (function, `0x00370EF8`)
- `0x003743B3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [MiPurgeSubsection](MiPurgeSubsection_function_003712F0.md) at `0x003719EF`

### Static image references
- `0x00373E8A` → RVA `0x00E2DC80` (`.data`; read)
- `0x00374216` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0037432D` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003743E7` → [sub_006E3E8A](../6E/Unknown_function_006E3E8A.md) (`tail-transfer`)
  - `0x00374417` → [sub_006E3E8A + 0x1B](../6E/Unknown_function_006E3E8A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00373DF0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00373DF5  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00373DFA  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00373DFF  55                              push rbp
00373E00  56                              push rsi
00373E01  57                              push rdi
00373E02  41 54                           push r12
00373E04  41 55                           push r13
00373E06  41 56                           push r14
00373E08  41 57                           push r15
00373E0A  48 8B EC                        mov rbp, rsp
00373E0D  48 83 EC 70                     sub rsp, 0x70
00373E11  33 C0                           xor eax, eax
00373E13  C7 45 DC 01 00 00 00            mov dword ptr [rbp - 0x24], 1
00373E1A  49 83 CE FF                     or r14, 0xffffffffffffffff
00373E1E  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00373E21  8B F8                           mov edi, eax
00373E23  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00373E27  44 8B F8                        mov r15d, eax
00373E2A  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00373E2E  44 8B E0                        mov r12d, eax
00373E31  89 45 58                        mov dword ptr [rbp + 0x58], eax
00373E34  8B D8                           mov ebx, eax
00373E36  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00373E3A  8B F0                           mov esi, eax
00373E3C  45 33 C9                        xor r9d, r9d
00373E3F  4C 8B EA                        mov r13, rdx
00373E42  8B C6                           mov eax, esi
00373E44  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00373E48  48 83 F8 10                     cmp rax, 0x10
00373E4C  0F 83 75 02 00 00               jae 0x1403740c7
00373E52  49 8B CD                        mov rcx, r13
00373E55  85 F6                           test esi, esi
00373E57  0F 84 A7 03 00 00               je 0x140374204
00373E5D  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00373E61  BA 01 00 00 00                  mov edx, 1
00373E66  E8 71 EA FF FF                  call 0x1403728dc
00373E6B  49 8B 45 00                     mov rax, qword ptr [r13]
00373E6F  45 33 C9                        xor r9d, r9d
00373E72  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00373E76  48 85 FF                        test rdi, rdi
00373E79  0F 84 40 02 00 00               je 0x1403740bf
00373E7F  49 FF C4                        inc r12
00373E82  A8 01                           test al, 1
00373E84  0F 85 2F 05 00 00               jne 0x1403743b9
00373E8A  48 8B 0D EF 9D AB 00            mov rcx, qword ptr [rip + 0xab9def]
00373E91  48 8B D0                        mov rdx, rax
00373E94  48 85 C9                        test rcx, rcx
00373E97  74 11                           je 0x140373eaa
00373E99  A8 10                           test al, 0x10
00373E9B  0F 85 41 03 00 00               jne 0x1403741e2
00373EA1  48 8B D1                        mov rdx, rcx
00373EA4  48 F7 D2                        not rdx
00373EA7  48 23 D0                        and rdx, rax
00373EAA  48 C1 EA 0C                     shr rdx, 0xc
00373EAE  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00373EB8  48 23 D1                        and rdx, rcx
00373EBB  85 F6                           test esi, esi
00373EBD  0F 84 28 03 00 00               je 0x1403741eb
00373EC3  8B CE                           mov ecx, esi
00373EC5  49 03 CE                        add rcx, r14
00373EC8  48 3B D1                        cmp rdx, rcx
00373ECB  0F 85 F6 01 00 00               jne 0x1403740c7
00373ED1  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00373ED5  48 BA 00 00 00 00 00 00 00 80   movabs rdx, 0x8000000000000000
00373EDF  48 0B CA                        or rcx, rdx
00373EE2  49 3B CD                        cmp rcx, r13
00373EE5  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00373EE9  0F 85 AB 04 00 00               jne 0x14037439a
00373EEF  8A 41 22                        mov al, byte ptr [rcx + 0x22]
00373EF2  24 07                           and al, 7
00373EF4  3C 06                           cmp al, 6
00373EF6  0F 84 98 04 00 00               je 0x140374394
00373EFC  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00373EFF  66 85 C0                        test ax, ax
00373F02  0F 85 5C 04 00 00               jne 0x140374364
00373F08  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00373F0C  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
00373F0F  C1 E9 18                        shr ecx, 0x18
00373F12  F6 C1 40                        test cl, 0x40
00373F15  0F 85 49 04 00 00               jne 0x140374364
00373F1B  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00373F1F  48 8B CF                        mov rcx, rdi
00373F22  E8 F1 D0 F3 FF                  call 0x1402b1018
00373F27  85 C0                           test eax, eax
00373F29  0F 85 98 01 00 00               jne 0x1403740c7
00373F2F  48 0F BA 67 28 35               bt qword ptr [rdi + 0x28], 0x35
00373F35  0F 82 8C 01 00 00               jb 0x1403740c7
00373F3B  48 8B CF                        mov rcx, rdi
00373F3E  E8 8D A3 F1 FF                  call 0x14028e2d0
00373F43  83 F8 09                        cmp eax, 9
00373F46  0F 85 7B 01 00 00               jne 0x1403740c7
00373F4C  8A 4F 22                        mov cl, byte ptr [rdi + 0x22]
00373F4F  C0 E9 04                        shr cl, 4
00373F52  F6 45 50 01                     test byte ptr [rbp + 0x50], 1
00373F56  0F 94 C0                        sete al
00373F59  22 C8                           and cl, al
00373F5B  F6 C1 01                        test cl, 1
00373F5E  0F 85 63 01 00 00               jne 0x1403740c7
00373F64  48 FF 45 E8                     inc qword ptr [rbp - 0x18]
00373F68  33 D2                           xor edx, edx
00373F6A  48 8B CF                        mov rcx, rdi
00373F6D  E8 1E 36 F1 FF                  call 0x140287590
00373F72  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00373F76  48 FF C3                        inc rbx
00373F79  48 89 5D F0                     mov qword ptr [rbp - 0x10], rbx
00373F7D  48 0F BA E0 0A                  bt rax, 0xa
00373F82  0F 83 9E 03 00 00               jae 0x140374326
00373F88  4C 8B F8                        mov r15, rax
00373F8B  48 8B 05 EE 9C AB 00            mov rax, qword ptr [rip + 0xab9cee]
00373F92  48 85 C0                        test rax, rax
00373F95  74 0C                           je 0x140373fa3
00373F97  41 F6 C7 10                     test r15b, 0x10
00373F9B  75 06                           jne 0x140373fa3
00373F9D  48 F7 D0                        not rax
00373FA0  4C 23 F8                        and r15, rax
00373FA3  FF 45 58                        inc dword ptr [rbp + 0x58]
00373FA6  45 33 C9                        xor r9d, r9d
00373FA9  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00373FAD  45 33 C0                        xor r8d, r8d
00373FB0  49 C1 FF 10                     sar r15, 0x10
00373FB4  33 D2                           xor edx, edx
00373FB6  E8 35 E2 00 00                  call 0x1403821f0
00373FBB  48 8B D8                        mov rbx, rax
00373FBE  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00373FC2  48 C1 E8 3C                     shr rax, 0x3c
00373FC6  24 07                           and al, 7
00373FC8  3C 03                           cmp al, 3
00373FCA  0F 84 9D 03 00 00               je 0x14037436d
00373FD0  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00373FD4  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00373FD8  48 0F BA E0 0A                  bt rax, 0xa
00373FDD  72 20                           jb 0x140373fff
00373FDF  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
00373FE3  C0 E8 02                        shr al, 2
00373FE6  A8 01                           test al, 1
00373FE8  75 08                           jne 0x140373ff2
00373FEA  8A C2                           mov al, dl
00373FEC  D0 E8                           shr al, 1
00373FEE  A8 01                           test al, 1
00373FF0  74 09                           je 0x140373ffb
00373FF2  48 85 D2                        test rdx, rdx
00373FF5  0F 85 17 03 00 00               jne 0x140374312
00373FFB  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00373FFF  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00374002  C0 E8 02                        shr al, 2
00374005  A8 01                           test al, 1
00374007  0F 85 26 02 00 00               jne 0x140374233
0037400D  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00374010  D0 E8                           shr al, 1
00374012  A8 01                           test al, 1
00374014  0F 85 65 03 00 00               jne 0x14037437f
0037401A  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
0037401D  33 D2                           xor edx, edx
0037401F  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00374023  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00374026  48 8B CF                        mov rcx, rdi
00374029  C1 E8 18                        shr eax, 0x18
0037402C  24 F8                           and al, 0xf8
0037402E  88 45 D3                        mov byte ptr [rbp - 0x2d], al
00374031  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
00374034  89 47 20                        mov dword ptr [rdi + 0x20], eax
00374037  E8 14 E3 F2 FF                  call 0x1402a2350
0037403C  83 7D D8 00                     cmp dword ptr [rbp - 0x28], 0
00374040  0F 84 AD 02 00 00               je 0x1403742f3
00374046  48 8B CF                        mov rcx, rdi
00374049  E8 A2 19 00 00                  call 0x1403759f0
0037404E  33 D2                           xor edx, edx
00374050  E8 0B E9 FE FF                  call 0x140362960
00374055  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00374058  45 33 C9                        xor r9d, r9d
0037405B  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
0037405F  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00374062  C1 E8 10                        shr eax, 0x10
00374065  24 F9                           and al, 0xf9
00374067  0C 01                           or al, 1
00374069  88 45 D2                        mov byte ptr [rbp - 0x2e], al
0037406C  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
0037406F  89 41 20                        mov dword ptr [rcx + 0x20], eax
00374072  4C 89 49 08                     mov qword ptr [rcx + 8], r9
00374076  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0037407A  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
00374084  48 23 C1                        and rax, rcx
00374087  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
0037408B  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
0037408F  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00374093  48 B9 FF FF FF FF FF FF FF BF   movabs rcx, 0xbfffffffffffffff
0037409D  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
003740A1  48 23 C1                        and rax, rcx
003740A4  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
003740A8  4C 89 4F 10                     mov qword ptr [rdi + 0x10], r9
003740AC  49 89 5D 00                     mov qword ptr [r13], rbx
003740B0  49 83 C5 08                     add r13, 8
003740B4  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
003740B8  FF C6                           inc esi
003740BA  E9 83 FD FF FF                  jmp 0x140373e42
003740BF  85 F6                           test esi, esi
003740C1  0F 84 02 03 00 00               je 0x1403743c9
003740C7  4C 8B 6D E8                     mov r13, qword ptr [rbp - 0x18]
003740CB  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
003740CE  BE 02 00 00 00                  mov esi, 2
003740D3  85 C0                           test eax, eax
003740D5  74 14                           je 0x1403740eb
003740D7  49 8B 0F                        mov rcx, qword ptr [r15]
003740DA  44 8B C0                        mov r8d, eax
003740DD  44 8B CE                        mov r9d, esi
003740E0  49 8B D7                        mov rdx, r15
003740E3  E8 00 05 F3 FF                  call 0x1402a45e8
003740E8  45 33 C9                        xor r9d, r9d
003740EB  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
003740F5  49 BA FF FF FF FF FF FF FF 7F   movabs r10, 0x7fffffffffffffff
003740FF  48 85 DB                        test rbx, rbx
00374102  0F 84 8B 00 00 00               je 0x140374193
00374108  4B 8D 04 76                     lea rax, [r14 + r14*2]
0037410C  48 03 C0                        add rax, rax
0037410F  48 B9 28 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000028
00374119  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0037411D  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00374127  48 23 C1                        and rax, rcx
0037412A  48 8D 1C 40                     lea rbx, [rax + rax*2]
0037412E  48 C1 E3 04                     shl rbx, 4
00374132  4C 8B FA                        mov r15, rdx
00374135  41 8B F9                        mov edi, r9d
00374138  48 BA 18 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000018
00374142  F0 48 0F BA 2C 13 3F            lock bts qword ptr [rbx + rdx], 0x3f
00374149  0F 82 C5 00 00 00               jb 0x140374214
0037414F  48 8B 04 13                     mov rax, qword ptr [rbx + rdx]
00374153  49 B8 00 00 00 00 00 00 00 C0   movabs r8, 0xc000000000000000
0037415D  48 8B C8                        mov rcx, rax
00374160  49 BA FF FF FF FF FF FF FF 7F   movabs r10, 0x7fffffffffffffff
0037416A  48 2B 4D F0                     sub rcx, qword ptr [rbp - 0x10]
0037416E  48 33 C1                        xor rax, rcx
00374171  49 23 C0                        and rax, r8
00374174  48 33 C1                        xor rax, rcx
00374177  4A 89 44 3B 18                  mov qword ptr [rbx + r15 + 0x18], rax
0037417C  F0 4C 21 14 13                  lock and qword ptr [rbx + rdx], r10
00374181  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00374185  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
00374189  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
00374193  48 83 7D D0 10                  cmp qword ptr [rbp - 0x30], 0x10
00374198  0F 84 AA 00 00 00               je 0x140374248
0037419E  4C 3B E3                        cmp r12, rbx
003741A1  74 08                           je 0x1403741ab
003741A3  F0 4C 21 57 18                  lock and qword ptr [rdi + 0x18], r10
003741A8  49 FF CC                        dec r12
003741AB  4F 8D 04 76                     lea r8, [r14 + r14*2]
003741AF  49 C1 E0 04                     shl r8, 4
003741B3  48 8B C2                        mov rax, rdx
003741B6  4C 03 C0                        add r8, rax
003741B9  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
003741BD  4D 85 E4                        test r12, r12
003741C0  0F 85 3D 02 00 00               jne 0x140374403
003741C6  49 8B C5                        mov rax, r13
003741C9  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
003741D1  48 83 C4 70                     add rsp, 0x70
003741D5  41 5F                           pop r15
003741D7  41 5E                           pop r14
003741D9  41 5D                           pop r13
003741DB  41 5C                           pop r12
003741DD  5F                              pop rdi
003741DE  5E                              pop rsi
003741DF  5D                              pop rbp
003741E0  C3                              ret
003741E1  CC                              int3
003741E2  48 83 E2 EF                     and rdx, 0xffffffffffffffef
003741E6  E9 BF FC FF FF                  jmp 0x140373eaa
003741EB  F6 C2 0F                        test dl, 0xf
003741EE  0F 85 D3 FE FF FF               jne 0x1403740c7
003741F4  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
003741F8  4C 8B F2                        mov r14, rdx
003741FB  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
003741FF  E9 CD FC FF FF                  jmp 0x140373ed1
00374204  33 D2                           xor edx, edx
00374206  E8 B5 16 FF FF                  call 0x1403658c0
0037420B  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0037420F  E9 57 FC FF FF                  jmp 0x140373e6b
00374214  FF C7                           inc edi
00374216  85 3D 90 10 C5 00               test dword ptr [rip + 0xc51090], edi
0037421C  0F 84 0B 01 00 00               je 0x14037432d
00374222  F3 90                           pause
00374224  48 8B 04 13                     mov rax, qword ptr [rbx + rdx]
00374228  48 85 C0                        test rax, rax
0037422B  0F 89 11 FF FF FF               jns 0x140374142
00374231  EB E1                           jmp 0x140374214
00374233  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00374237  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
0037423B  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0037423F  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00374243  E9 C5 FD FF FF                  jmp 0x14037400d
00374248  4B 8D 1C 76                     lea rbx, [r14 + r14*2]
0037424C  48 C1 E3 04                     shl rbx, 4
00374250  48 8B C2                        mov rax, rdx
00374253  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00374257  41 BC 01 00 00 00               mov r12d, 1
0037425D  8B 7D DC                        mov edi, dword ptr [rbp - 0x24]
00374260  44 8B CE                        mov r9d, esi
00374263  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00374268  49 8B D6                        mov rdx, r14
0037426B  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00374270  49 8B CF                        mov rcx, r15
00374273  45 8D 44 24 0F                  lea r8d, [r12 + 0xf]
00374278  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
0037427C  48 03 D8                        add rbx, rax
0037427F  E8 74 E8 0E 00                  call 0x140462af8
00374284  41 0F B7 07                     movzx eax, word ptr [r15]
00374288  41 8D 54 24 0F                  lea edx, [r12 + 0xf]
0037428D  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00374292  44 8B CF                        mov r9d, edi
00374295  44 8B C6                        mov r8d, esi
00374298  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
0037429D  49 8B CE                        mov rcx, r14
003742A0  E8 3B E6 0C 00                  call 0x1404428e0
003742A5  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
003742A9  41 8B CC                        mov ecx, r12d
003742AC  4D 3B C4                        cmp r8, r12
003742AF  76 24                           jbe 0x1403742d5
003742B1  48 8D 53 48                     lea rdx, [rbx + 0x48]
003742B5  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
003742BF  F0 4C 21 2A                     lock and qword ptr [rdx], r13
003742C3  41 03 CC                        add ecx, r12d
003742C6  48 8D 52 30                     lea rdx, [rdx + 0x30]
003742CA  8B C1                           mov eax, ecx
003742CC  49 3B C0                        cmp rax, r8
003742CF  72 EE                           jb 0x1403742bf
003742D1  4C 8B 6D E8                     mov r13, qword ptr [rbp - 0x18]
003742D5  8B D6                           mov edx, esi
003742D7  49 8B CE                        mov rcx, r14
003742DA  E8 41 0A FC FF                  call 0x140334d20
003742DF  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003742E9  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
003742EE  E9 D3 FE FF FF                  jmp 0x1403741c6
003742F3  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
003742F6  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
003742FA  C1 E8 10                        shr eax, 0x10
003742FD  0F B6 C0                        movzx eax, al
00374300  C1 E8 06                        shr eax, 6
00374303  89 45 DC                        mov dword ptr [rbp - 0x24], eax
00374306  C7 45 D8 01 00 00 00            mov dword ptr [rbp - 0x28], 1
0037430D  E9 34 FD FF FF                  jmp 0x140374046
00374312  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00374316  41 B8 01 00 00 00               mov r8d, 1
0037431C  E8 AF FC F0 FF                  call 0x140283fd0
00374321  E9 D5 FC FF FF                  jmp 0x140373ffb
00374326  33 DB                           xor ebx, ebx
00374328  E9 91 FC FF FF                  jmp 0x140373fbe
0037432D  8B 05 85 27 C5 00               mov eax, dword ptr [rip + 0xc52785]
00374333  A8 40                           test al, 0x40
00374335  0F 84 E7 FE FF FF               je 0x140374222
0037433B  E8 50 B1 F9 FF                  call 0x14030f490
00374340  45 33 C9                        xor r9d, r9d
00374343  84 C0                           test al, al
00374345  0F 84 A9 00 00 00               je 0x1403743f4
0037434B  8B CF                           mov ecx, edi
0037434D  E8 0E B1 F9 FF                  call 0x14030f460
00374352  45 33 C9                        xor r9d, r9d
00374355  48 BA 18 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000018
0037435F  E9 C0 FE FF FF                  jmp 0x140374224
00374364  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00374368  E9 5A FD FF FF                  jmp 0x1403740c7
0037436D  BA 0C 00 00 00                  mov edx, 0xc
00374372  48 8B CF                        mov rcx, rdi
00374375  E8 86 2C 09 00                  call 0x140407000
0037437A  E9 51 FC FF FF                  jmp 0x140373fd0
0037437F  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00374383  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00374387  48 83 E0 FD                     and rax, 0xfffffffffffffffd
0037438B  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
0037438F  E9 86 FC FF FF                  jmp 0x14037401a
00374394  E8 5F CB FF FF                  call 0x140370ef8
00374399  CC                              int3
0037439A  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0037439E  4C 8B C8                        mov r9, rax
003743A1  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
003743A6  4D 8B C5                        mov r8, r13
003743A9  BA 03 04 00 00                  mov edx, 0x403
003743AE  B9 1A 00 00 00                  mov ecx, 0x1a
003743B3  E8 A8 92 18 00                  call 0x1404fd660
003743B8  CC                              int3
003743B9  4C 8B 6D E8                     mov r13, qword ptr [rbp - 0x18]
003743BD  49 FF C5                        inc r13
003743C0  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
003743C4  E9 02 FD FF FF                  jmp 0x1403740cb
003743C9  48 A9 00 0C 00 00               test rax, 0xc00
003743CF  0F 85 F2 FC FF FF               jne 0x1403740c7
003743D5  48 85 C0                        test rax, rax
003743D8  0F 84 E9 FC FF FF               je 0x1403740c7
003743DE  BE 02 00 00 00                  mov esi, 2
003743E3  40 84 75 50                     test byte ptr [rbp + 0x50], sil
003743E7  0F 84 9D FA 36 00               je 0x1406e3e8a
003743ED  33 C0                           xor eax, eax
003743EF  E9 D5 FD FF FF                  jmp 0x1403741c9
003743F4  48 BA 18 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000018
003743FE  E9 1F FE FF FF                  jmp 0x140374222
00374403  49 8D 78 18                     lea rdi, [r8 + 0x18]
00374407  49 8B D8                        mov rbx, r8
0037440A  4D 8B F8                        mov r15, r8
0037440D  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
00374417  E9 89 FA 36 00                  jmp 0x1406e3ea5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeleteSectionCluster(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int8 v_stack_m65;
    unsigned __int8 v_stack_m66;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m5C = 1;
    v_r14 = (v_r14) | (-1);
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m48 = 0;
    v_stack_p20 = 0;
    v_stack_m50 = 0;
    a4 = 0;
loc_00373E42:
    v_stack_m68 = 0;
    if (0 >= 16) goto loc_003740C7;
    if (0 == 0) goto loc_00374204;
    result = MiTryLockLeafPage(a2, 1, v_stack_m58, a4);
loc_00373E6B:
    a4 = 0;
    if (v_stack_m58 == 0) goto loc_003740BF;
    v_r12 = (0) + 1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) != 0) goto loc_003743B9;
    if (*(unsigned __int64 *)(v_rip + 11247087) == 0) goto loc_00373EAA;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (16)) != 0) goto loc_003741E2;
    a2 = ~(*(unsigned __int64 *)(v_rip + 11247087));
    a2 = (a2) & (*(unsigned __int64 *)(a2));
loc_00373EAA:
    a2 = (a2) >> (12);
    a2 = (a2) & (*(unsigned __int64 *)(v_rip + 11247087));
    if (0 == 0) goto loc_003741EB;
    a1 = (0) + (v_r14);
    if (a2 != a1) goto loc_003740C7;
loc_00373ED1:
    a1 = (*(unsigned __int64 *)(v_stack_m58 + 8)) | (a2);
    if (a1 != a2) goto loc_0037439A;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m58 + 34)) & (7));
    if (((unsigned __int8)(result)) == 6) goto loc_00374394;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m58 + 32))) != 0) goto loc_00374364;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m58 + 32))) >> (24));
    if ((((unsigned __int8)(a1)) & (64)) != 0) goto loc_00374364;
    result = MiIsPageOnBadList(v_stack_m58, a2, v_stack_m58, a4);
    if ((unsigned int)(result) != 0) goto loc_003740C7;
    if (condition_is_below) goto loc_003740C7;
    result = MiGetPfnSlabType(v_stack_m58, a2, v_stack_m58, a4);
    if (((unsigned int)(result)) != 9) goto loc_003740C7;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m58 + 34)) >> (4));
    result = (((v_stack_p18) & (1)) == 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_003740C7;
    a2 = 0;
    result = MiUnlinkPageFromListEx(v_stack_m58, a2, v_stack_m58, a4);
    v_rbx = (0) + 1;
    v_stack_m48 = v_rbx;
    if (condition_is_above_or_equal) goto loc_00374326;
    if (*(unsigned __int64 *)(v_rip + 11246830) == 0) goto loc_00373FA3;
    result = *(unsigned __int64 *)(v_rip + 11246830);
    v_r15 = *(unsigned __int64 *)(v_stack_m58 + 16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m58 + 16))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 11246830));
        v_r15 = (*(unsigned __int64 *)(v_stack_m58 + 16)) & (result);
    }
    a4 = 0;
    a3 = 0;
    v_r15 = (v_r15) >> (16);
    a2 = 0;
    result = MiTransferSoftwarePte(*(unsigned __int64 *)(v_stack_m58 + 16), a2, a3, a4);
loc_00373FBE:
    result = (*(unsigned __int64 *)(v_stack_m58 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 3) goto loc_0037436D;
loc_00373FD0:
    v_stack_m40 = *(unsigned __int64 *)(v_stack_m58 + 16);
    if (((unsigned __int8)(result)) < 3) goto loc_00373FFF;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_stack_m58 + 16)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00373FF2;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_m40)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00373FFB;
loc_00373FF2:
    if (v_stack_m40 != 0) goto loc_00374312;
loc_00373FFB:
loc_00373FFF:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m58 + 16))) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00374233;
loc_0037400D:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m58 + 16))) >> (1));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0037437F;
loc_0037401A:
    a2 = 0;
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m58 + 32))) >> (24));
    result = (unsigned __int8)((result) & (248));
    v_stack_m65 = (unsigned __int8)(result);
    *(unsigned int *)(v_stack_m58 + 32) = (unsigned int)((unsigned int)(v_stack_m68));
    result = MiSetPfnIdentity(v_stack_m58, a2, a3, a4);
    if (v_stack_m60 == 0) goto loc_003742F3;
loc_00374046:
    result = MiClearPfnReuseFields(v_stack_m58, a2, a3, a4);
    a2 = 0;
    result = MiSetPfnModified(v_stack_m58, a2, a3, a4);
    a4 = 0;
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m58 + 32))) >> (16));
    result = (unsigned __int8)((result) & (249));
    result = (unsigned __int8)((result) | (1));
    v_stack_m66 = (unsigned __int8)(result);
    *(unsigned int *)(v_stack_m58 + 32) = (unsigned int)((unsigned int)(v_stack_m68));
    *(unsigned __int64 *)(v_stack_m58 + 8) = 0;
    result = (*(unsigned __int64 *)(v_stack_m58 + 24)) & (v_stack_m58);
    *(unsigned __int64 *)(v_stack_m58 + 24) = result;
    result = (*(unsigned __int64 *)(v_stack_m58 + 24)) & (v_stack_m58);
    *(unsigned __int64 *)(v_stack_m58 + 24) = result;
    *(unsigned __int64 *)(v_stack_m58 + 16) = 0;
    *(unsigned __int64 *)(a2) = result;
    v_r13 = (a2) + (8);
    v_rsi = (unsigned int)((0) + 1);
    goto loc_00373E42;
loc_003740BF:
    if ((unsigned int)(v_rsi) == 0) goto loc_003743C9;
loc_003740C7:
loc_003740CB:
    result = (unsigned int)(v_stack_p20);
    if ((unsigned int)((unsigned int)(v_stack_p20)) != 0) {
        a1 = *(unsigned __int64 *)(v_r15);
        a3 = (unsigned int)((unsigned int)(v_stack_p20));
        a4 = 2;
        a2 = v_r15;
        result = MiDereferenceControlAreaPfnList(a1, a2, a3, a4);
        a4 = 0;
    }
    if (v_stack_m48 == 0) goto loc_00374193;
    result = (v_r14 + v_r14 * 2) + (v_r14 + v_r14 * 2);
    result = (*(unsigned __int64 *)(a1 + result * 8)) & (a1);
    v_rbx = (result + result * 2) << (4);
loc_00374142:
    if (condition_is_below) goto loc_00374214;
    a1 = (*(unsigned __int64 *)(v_rbx + a2 * 1)) - (v_stack_m48);
    result = (*(unsigned __int64 *)(v_rbx + a2 * 1)) ^ (a1);
    result = (result) & (a3);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_rbx + a2 * 1 + 24) = result;
loc_00374193:
    if (v_stack_m68 == 16) goto loc_00374248;
    if (v_r12 != v_stack_m48) {
        v_r12 = (v_r12) - 1;
    }
    a3 = (v_r14 + v_r14 * 2) << (4);
    a3 = (a3) + (a2);
    v_stack_m58 = a3;
    if (v_r12 != 0) goto loc_00374403;
loc_003741C6:
loc_003741C9:
    v_rsp = (v_rsp) + (112);
    return v_stack_m50;
loc_003741E2:
    a2 = (a2) & (-17);
    goto loc_00373EAA;
loc_003741EB:
    if ((((unsigned __int8)(a2)) & (15)) != 0) goto loc_003740C7;
    goto loc_00373ED1;
loc_00374204:
    a2 = 0;
    result = MiLockLeafPage(*(unsigned __int64 *)(v_stack_m58 + 40), a2, a3, a4);
    v_stack_m58 = result;
    goto loc_00373E6B;
loc_00374214:
    v_rdi = (unsigned int)((v_stack_m58) + 1);
    if (((*(unsigned int *)(v_rip + 12914832)) & ((unsigned int)(v_rdi))) == 0) goto loc_0037432D;
loc_00374222:
loc_00374224:
    if (!sign_flag) goto loc_00374142;
    goto loc_00374214;
loc_00374233:
    result = (*(unsigned __int64 *)(v_rdi + 16)) & (-5);
    *(unsigned __int64 *)(v_stack_m58 + 16) = result;
    goto loc_0037400D;
loc_00374248:
    v_rbx = (a2 + a2 * 2) << (4);
    v_stack_p30 = 1;
    v_stack_p28 = 1;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m5C));
    v_rbx = (v_rbx) + (0);
    result = MiInitializeAllResidentPageBasePfns(v_stack_p8, 0, 1 + 15, 2);
    v_stack_p28 = 1;
    v_stack_p20 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_p8));
    result = MiCreateInitialLargeLeafPfns(0, 1 + 15, 2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))));
    if (v_stack_m48 <= 1) goto loc_003742D5;
loc_003742BF:
    a1 = (unsigned int)((1) + (1));
    if (((unsigned int)((unsigned int)(a1))) < v_stack_m48) goto loc_003742BF;
loc_003742D5:
    result = MiInsertPageInFreeOrZeroedList(0, 2, v_stack_m48, (unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))));
    goto loc_003741C6;
loc_003742F3:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m5C) + 32))) >> (16));
    result = (unsigned int)(((unsigned __int8)(result)) >> (6));
    v_stack_m5C = (unsigned int)(result);
    v_stack_m60 = 1;
    goto loc_00374046;
loc_00374312:
    result = MiReleasePageFileInfo(v_stack_p8, 2, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))));
    goto loc_00373FFB;
loc_00374326:
    v_rbx = 0;
    goto loc_00373FBE;
loc_0037432D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12920709)))) & (64)) == 0) goto loc_00374222;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p8, 2, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))));
    a4 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_003743F4;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_m58)), 2, 1, a4);
    a4 = 0;
    goto loc_00374224;
loc_00374364:
    goto loc_003740C7;
loc_0037436D:
    result = MiClearPfnImageVerified(v_stack_m58, 12, 1, a4);
    goto loc_00373FD0;
loc_0037437F:
    result = (*(unsigned __int64 *)(v_stack_m58 + 16)) & (-3);
    *(unsigned __int64 *)(v_stack_m58 + 16) = result;
    goto loc_0037401A;
loc_00374394:
    result = MiBadShareCount(v_stack_m58, 12, 1, a4);
loc_0037439A:
    v_stack_p20 = *(unsigned __int64 *)(v_stack_m58 + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x403ULL), v_stack_m50, result);
loc_003743B9:
    v_r13 = (v_stack_m50) + 1;
    v_stack_m50 = v_r13;
    goto loc_003740CB;
loc_003743C9:
    if (((result) & (0xC00ULL)) != 0) goto loc_003740C7;
    if (result == 0) goto loc_003740C7;
    result = 0;
    goto loc_003741C9;
loc_003743F4:
    goto loc_00374222;
loc_00374403:
}
```

## 5. (Beta) C Style

```c
int64_t MiDeleteSectionCluster(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint8_t v_stack_m65;
    uint8_t v_stack_m66;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m5C = 1;
    local_r14 = (local_r14) | (-1);
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m48 = 0;
    v_stack_p20 = 0;
    v_stack_m50 = 0;
    Arg4 = 0;
loc_00373E42:
    v_stack_m68 = 0;
    if (0 >= 16) goto loc_003740C7;
    if (0 == 0) goto loc_00374204;
    result = MiTryLockLeafPage(Arg2, 1, v_stack_m58, Arg4);
loc_00373E6B:
    Arg4 = 0;
    if (v_stack_m58 == 0) goto loc_003740BF;
    local_r12 = (0) + 1;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (1)) != 0) goto loc_003743B9;
    if (*(uint64_t *)(v_rip + 0xAB9DEF) == 0) goto loc_00373EAA;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (16)) != 0) goto loc_003741E2;
    Arg2 = ~(*(uint64_t *)(v_rip + 0xAB9DEF));
    Arg2 = (Arg2) & (*(uint64_t *)(arg2));
loc_00373EAA:
    Arg2 = (Arg2) >> (12);
    Arg2 = (Arg2) & (*(uint64_t *)(v_rip + 0xAB9DEF));
    if (0 == 0) goto loc_003741EB;
    Arg1 = (0) + (local_r14);
    if (Arg2 != Arg1) goto loc_003740C7;
loc_00373ED1:
    Arg1 = (*(uint64_t *)(v_stack_m58 + 0x8)) | (Arg2);
    if (Arg1 != Arg2) goto loc_0037439A;
    result = (uint8_t)((*(uint8_t *)(v_stack_m58 + 0x22)) & (7));
    if (((uint8_t)(result)) == 6) goto loc_00374394;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20))) != 0) goto loc_00374364;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20))) >> (24));
    if ((((uint8_t)(Arg1)) & (64)) != 0) goto loc_00374364;
    result = MiIsPageOnBadList(v_stack_m58, Arg2, v_stack_m58, Arg4);
    if ((uint32_t)(result) != 0) goto loc_003740C7;
    if (condition_is_below) goto loc_003740C7;
    result = MiGetPfnSlabType(v_stack_m58, Arg2, v_stack_m58, Arg4);
    if (((uint32_t)(result)) != 9) goto loc_003740C7;
    Arg1 = (uint8_t)((*(uint8_t *)(v_stack_m58 + 0x22)) >> (4));
    result = (((v_stack_p18) & (1)) == 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_003740C7;
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(v_stack_m58, Arg2, v_stack_m58, Arg4);
    local_rbx = (0) + 1;
    v_stack_m48 = local_rbx;
    if (condition_is_above_or_equal) goto loc_00374326;
    if (*(uint64_t *)(v_rip + 0xAB9CEE) == 0) goto loc_00373FA3;
    result = *(uint64_t *)(v_rip + 0xAB9CEE);
    local_r15 = *(uint64_t *)(v_stack_m58 + 0x10);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m58 + 0x10))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xAB9CEE));
        local_r15 = (*(uint64_t *)(v_stack_m58 + 0x10)) & (result);
    }
    Arg4 = 0;
    Arg3 = 0;
    local_r15 = (local_r15) >> (16);
    Arg2 = 0;
    result = MiTransferSoftwarePte(*(uint64_t *)(v_stack_m58 + 0x10), Arg2, Arg3, Arg4);
loc_00373FBE:
    result = (*(uint64_t *)(v_stack_m58 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 3) goto loc_0037436D;
loc_00373FD0:
    v_stack_m40 = *(uint64_t *)(v_stack_m58 + 0x10);
    if (((uint8_t)(result)) < 3) goto loc_00373FFF;
    result = (uint8_t)((*(uint64_t *)(v_stack_m58 + 0x10)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00373FF2;
    result = (uint8_t)(((uint8_t)(v_stack_m40)) >> (1));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00373FFB;
loc_00373FF2:
    if (v_stack_m40 != 0) goto loc_00374312;
loc_00373FFB:
loc_00373FFF:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x10))) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00374233;
loc_0037400D:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x10))) >> (1));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0037437F;
loc_0037401A:
    Arg2 = 0;
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20))) >> (24));
    result = (uint8_t)((result) & (248));
    v_stack_m65 = (uint8_t)(result);
    *(uint32_t *)(v_stack_m58 + 0x20) = (uint32_t)((uint32_t)(v_stack_m68));
    result = MiSetPfnIdentity(v_stack_m58, Arg2, Arg3, Arg4);
    if (v_stack_m60 == 0) goto loc_003742F3;
loc_00374046:
    result = MiClearPfnReuseFields(v_stack_m58, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = MiSetPfnModified(v_stack_m58, Arg2, Arg3, Arg4);
    Arg4 = 0;
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m58 + 0x20))) >> (16));
    result = (uint8_t)((result) & (249));
    result = (uint8_t)((result) | (1));
    v_stack_m66 = (uint8_t)(result);
    *(uint32_t *)(v_stack_m58 + 0x20) = (uint32_t)((uint32_t)(v_stack_m68));
    *(uint64_t *)(v_stack_m58 + 0x8) = 0;
    result = (*(uint64_t *)(v_stack_m58 + 0x18)) & (v_stack_m58);
    *(uint64_t *)(v_stack_m58 + 0x18) = result;
    result = (*(uint64_t *)(v_stack_m58 + 0x18)) & (v_stack_m58);
    *(uint64_t *)(v_stack_m58 + 0x18) = result;
    *(uint64_t *)(v_stack_m58 + 0x10) = 0;
    *(uint64_t *)(arg2) = result;
    local_r13 = (Arg2) + (8);
    local_rsi = (uint32_t)((0) + 1);
    goto loc_00373E42;
loc_003740BF:
    if ((uint32_t)(local_rsi) == 0) goto loc_003743C9;
loc_003740C7:
loc_003740CB:
    result = (uint32_t)(v_stack_p20);
    if ((uint32_t)((uint32_t)(v_stack_p20)) != 0) {
        Arg1 = *(uint64_t *)(local_r15);
        Arg3 = (uint32_t)((uint32_t)(v_stack_p20));
        Arg4 = 2;
        Arg2 = local_r15;
        result = MiDereferenceControlAreaPfnList(Arg1, Arg2, Arg3, Arg4);
        Arg4 = 0;
    }
    if (v_stack_m48 == 0) goto loc_00374193;
    result = (local_r14 + local_r14 * 2) + (local_r14 + local_r14 * 2);
    result = (*(uint64_t *)(Arg1 + result * 8)) & (Arg1);
    local_rbx = (result + result * 2) << (4);
loc_00374142:
    if (condition_is_below) goto loc_00374214;
    Arg1 = (*(uint64_t *)(local_rbx + arg2 * 1)) - (v_stack_m48);
    result = (*(uint64_t *)(local_rbx + arg2 * 1)) ^ (Arg1);
    result = (result) & (Arg3);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_rbx + arg2 * 1 + 0x18) = result;
loc_00374193:
    if (v_stack_m68 == 16) goto loc_00374248;
    if (local_r12 != v_stack_m48) {
        local_r12 = (local_r12) - 1;
    }
    Arg3 = (local_r14 + local_r14 * 2) << (4);
    Arg3 = (Arg3) + (Arg2);
    v_stack_m58 = Arg3;
    if (local_r12 != 0) goto loc_00374403;
loc_003741C6:
loc_003741C9:
    local_rsp = (local_rsp) + (112);
    return v_stack_m50;
loc_003741E2:
    Arg2 = (Arg2) & (-17);
    goto loc_00373EAA;
loc_003741EB:
    if ((((uint8_t)(Arg2)) & (15)) != 0) goto loc_003740C7;
    goto loc_00373ED1;
loc_00374204:
    Arg2 = 0;
    result = MiLockLeafPage(*(uint64_t *)(v_stack_m58 + 0x28), Arg2, Arg3, Arg4);
    v_stack_m58 = result;
    goto loc_00373E6B;
loc_00374214:
    local_rdi = (uint32_t)((v_stack_m58) + 1);
    if (((*(uint32_t *)(v_rip + 0xC51090)) & ((uint32_t)(local_rdi))) == 0) goto loc_0037432D;
loc_00374222:
loc_00374224:
    if (!sign_flag) goto loc_00374142;
    goto loc_00374214;
loc_00374233:
    result = (*(uint64_t *)(local_rdi + 0x10)) & (-5);
    *(uint64_t *)(v_stack_m58 + 0x10) = result;
    goto loc_0037400D;
loc_00374248:
    local_rbx = (Arg2 + Arg2 * 2) << (4);
    v_stack_p30 = 1;
    v_stack_p28 = 1;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m5C));
    local_rbx = (local_rbx) + (0);
    result = MiInitializeAllResidentPageBasePfns(v_stack_p8, 0, 1 + 15, 2);
    v_stack_p28 = 1;
    v_stack_p20 = (uint16_t)(*(uint16_t *)(v_stack_p8));
    result = MiCreateInitialLargeLeafPfns(0, 1 + 15, 2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))));
    if (v_stack_m48 <= 1) goto loc_003742D5;
loc_003742BF:
    Arg1 = (uint32_t)((1) + (1));
    if (((uint32_t)((uint32_t)(Arg1))) < v_stack_m48) goto loc_003742BF;
loc_003742D5:
    result = MiInsertPageInFreeOrZeroedList(0, 2, v_stack_m48, (uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))));
    goto loc_003741C6;
loc_003742F3:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m5C) + 0x20))) >> (16));
    result = (uint32_t)(((uint8_t)(result)) >> (6));
    v_stack_m5C = (uint32_t)(result);
    v_stack_m60 = 1;
    goto loc_00374046;
loc_00374312:
    result = MiReleasePageFileInfo(v_stack_p8, 2, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))));
    goto loc_00373FFB;
loc_00374326:
    local_rbx = 0;
    goto loc_00373FBE;
loc_0037432D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC52785)))) & (64)) == 0) goto loc_00374222;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p8, 2, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))));
    Arg4 = 0;
    if ((uint8_t)(result) == 0) goto loc_003743F4;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_m58)), 2, 1, Arg4);
    Arg4 = 0;
    goto loc_00374224;
loc_00374364:
    goto loc_003740C7;
loc_0037436D:
    result = MiClearPfnImageVerified(v_stack_m58, 12, 1, Arg4);
    goto loc_00373FD0;
loc_0037437F:
    result = (*(uint64_t *)(v_stack_m58 + 0x10)) & (-3);
    *(uint64_t *)(v_stack_m58 + 0x10) = result;
    goto loc_0037401A;
loc_00374394:
    result = MiBadShareCount(v_stack_m58, 12, 1, Arg4);
loc_0037439A:
    v_stack_p20 = *(uint64_t *)(v_stack_m58 + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x403ULL), v_stack_m50, result);
loc_003743B9:
    local_r13 = (v_stack_m50) + 1;
    v_stack_m50 = local_r13;
    goto loc_003740CB;
loc_003743C9:
    if (((result) & (0xC00ULL)) != 0) goto loc_003740C7;
    if (result == 0) goto loc_003740C7;
    result = 0;
    goto loc_003741C9;
loc_003743F4:
    goto loc_00374222;
loc_00374403:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00373DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
