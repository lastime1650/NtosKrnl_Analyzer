# MiInitializeDynamicPfns

- RVA: `0x00672BD0`–`0x006730EF` (길이 `1,311` bytes)
- VA: `0x0000000140672BD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7A84`
- 디코드: `332`개 명령, `1,311/1,311` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00672C6A` → [MiUpdatePhysicalPages](../69/MiUpdatePhysicalPages_function_0069232C.md) (function, `0x0069232C`)
- `0x00672CC3` → [MiInitializeAllResidentPageBasePfns](../46/MiInitializeAllResidentPageBasePfns_function_00462AF8.md) (function, `0x00462AF8`)
- `0x00672CFF` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00672D13` → [MiReferenceControlAreaPfn](../36/MiReferenceControlAreaPfn_function_00364084.md) (function, `0x00364084`)
- `0x00672D27` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00672D58` → [MiUpdatePartitionChildPageCounts](../69/MiUpdatePartitionChildPageCounts_function_006921D4.md) (function, `0x006921D4`)
- `0x00672D7C` → [MiCreatePfnTemplate](MiCreatePfnTemplate_function_00671824.md) (function, `0x00671824`)
- `0x00672D90` → [MiRestrictRangeToNode](../40/MiRestrictRangeToNode_function_0040199C.md) (function, `0x0040199C`)
- `0x00672DCA` → [MiLockProtoPoolPageForce](../32/MiLockProtoPoolPageForce_function_00320E10.md) (function, `0x00320E10`)
- `0x00672E10` → [MiInitializeNewPfns](MiInitializeNewPfns_function_00670E94.md) (function, `0x00670E94`)
- `0x00672E23` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00672E2B` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x00672E3C` → [MiInitializeDpcGang](../43/MiInitializeDpcGang_function_0043E9DC.md) (function, `0x0043E9DC`)
- `0x00672E7F` → [MiStartDpcGang](../2C/MiStartDpcGang_function_002C8C34.md) (function, `0x002C8C34`)
- `0x00672E94` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00672ED3` → [MiUpdateLargePageBitMap](../37/MiUpdateLargePageBitMap_function_0037619C.md) (function, `0x0037619C`)
- `0x00672F5B` → [MiUpdatePartitionChildPageCounts](../69/MiUpdatePartitionChildPageCounts_function_006921D4.md) (function, `0x006921D4`)
- `0x00672F88` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00672FBE` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x00672FF1` → [MiSetPfnRemovalRequested](MiSetPfnRemovalRequested_function_0067A4D0.md) (function, `0x0067A4D0`)
- `0x00672FFB` → [MiPageCombiningActive](../46/MiPageCombiningActive_function_00462348.md) (function, `0x00462348`)
- `0x00673018` → [MiCopyPfnEntryRaw](../44/MiCopyPfnEntryRaw_function_00448500.md) (function, `0x00448500`)
- `0x00673020` → [MiAbortCombineScan](../2A/MiAbortCombineScan_function_002A1160.md) (function, `0x002A1160`)
- `0x00673031` → [MiCopyPfnEntryRaw](../44/MiCopyPfnEntryRaw_function_00448500.md) (function, `0x00448500`)
- `0x00673056` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x0067306F` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00673093` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x006730BE` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x006730D5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiMapNewPfns](../../page/7F/MiMapNewPfns_function_007FA63C.md) at `0x007FA802`
- [MiUnmapPfns](../../page/7F/MiUnmapPfns_function_007FB0A0.md) at `0x007FB0D7`

### Static image references
- `0x00672BEC` → RVA `0x00E0A740` (`.data`; read)
- `0x00672C4A` → RVA `0x00E38D00` (`.data`; read)
- `0x00672CF1` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00672EDC` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00672BD0  40 55                           push rbp
00672BD2  53                              push rbx
00672BD3  56                              push rsi
00672BD4  57                              push rdi
00672BD5  41 54                           push r12
00672BD7  41 55                           push r13
00672BD9  41 56                           push r14
00672BDB  41 57                           push r15
00672BDD  48 8D AC 24 78 FE FF FF         lea rbp, [rsp - 0x188]
00672BE5  48 81 EC 88 02 00 00            sub rsp, 0x288
00672BEC  48 8B 05 4D 7B 79 00            mov rax, qword ptr [rip + 0x797b4d]
00672BF3  48 33 C4                        xor rax, rsp
00672BF6  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
00672BFD  4C 8B A5 F0 01 00 00            mov r12, qword ptr [rbp + 0x1f0]
00672C04  48 8D 34 49                     lea rsi, [rcx + rcx*2]
00672C08  0F 57 C0                        xorps xmm0, xmm0
00672C0B  48 C1 E6 04                     shl rsi, 4
00672C0F  0F 57 C9                        xorps xmm1, xmm1
00672C12  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
00672C17  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
00672C1B  45 8B F1                        mov r14d, r9d
00672C1E  48 8B FA                        mov rdi, rdx
00672C21  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
00672C25  4C 8B F9                        mov r15, rcx
00672C28  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00672C32  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
00672C36  0F 11 4C 24 68                  movups xmmword ptr [rsp + 0x68], xmm1
00672C3B  0F 11 4C 24 78                  movups xmmword ptr [rsp + 0x78], xmm1
00672C40  0F 11 4D 88                     movups xmmword ptr [rbp - 0x78], xmm1
00672C44  48 8B C0                        mov rax, rax
00672C47  48 03 F0                        add rsi, rax
00672C4A  48 8D 0D AF 60 7C 00            lea rcx, [rip + 0x7c60af]
00672C51  41 8B C1                        mov eax, r9d
00672C54  BB 05 00 00 00                  mov ebx, 5
00672C59  25 0A 00 08 00                  and eax, 0x8000a
00672C5E  44 8D 6B FC                     lea r13d, [rbx - 4]
00672C62  83 F8 08                        cmp eax, 8
00672C65  75 13                           jne 0x140672c7a
00672C67  45 8B C5                        mov r8d, r13d
00672C6A  E8 BD F6 01 00                  call 0x14069232c
00672C6F  48 8D 0D 8A 60 7C 00            lea rcx, [rip + 0x7c608a]
00672C76  41 8D 5D 05                     lea ebx, [r13 + 5]
00672C7A  45 84 F5                        test r13b, r14b
00672C7D  0F 84 35 02 00 00               je 0x140672eb8
00672C83  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00672C88  0F 57 C0                        xorps xmm0, xmm0
00672C8B  33 DB                           xor ebx, ebx
00672C8D  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
00672C91  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00672C95  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00672C99  41 F7 C6 00 30 00 00            test r14d, 0x3000
00672CA0  74 26                           je 0x140672cc8
00672CA2  45 8B CE                        mov r9d, r14d
00672CA5  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00672CA9  41 C1 E9 0C                     shr r9d, 0xc
00672CAD  4C 8B C7                        mov r8, rdi
00672CB0  45 23 CD                        and r9d, r13d
00672CB3  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00672CB8  49 8B D7                        mov rdx, r15
00672CBB  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00672CC0  48 8B CE                        mov rcx, rsi
00672CC3  E8 30 FE DE FF                  call 0x140462af8
00672CC8  41 BD 02 00 00 00               mov r13d, 2
00672CCE  45 84 F5                        test r13b, r14b
00672CD1  74 6D                           je 0x140672d40
00672CD3  49 8B 04 24                     mov rax, qword ptr [r12]
00672CD7  49 8B 74 24 08                  mov rsi, qword ptr [r12 + 8]
00672CDC  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
00672CE1  48 8B 00                        mov rax, qword ptr [rax]
00672CE4  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00672CE9  44 0F 20 C6                     mov rsi, cr8
00672CED  45 0F 22 C5                     mov cr8, r13
00672CF1  39 1D 29 40 95 00               cmp dword ptr [rip + 0x954029], ebx
00672CF7  74 10                           je 0x140672d09
00672CF9  41 8A D5                        mov dl, r13b
00672CFC  40 8A CE                        mov cl, sil
00672CFF  E8 F8 29 E8 FF                  call 0x1404f56fc
00672D04  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00672D09  49 8B 14 24                     mov rdx, qword ptr [r12]
00672D0D  44 8B C7                        mov r8d, edi
00672D10  48 8B C8                        mov rcx, rax
00672D13  E8 6C 13 CF FF                  call 0x140364084
00672D18  39 1D 02 40 95 00               cmp dword ptr [rip + 0x954002], ebx
00672D1E  74 0C                           je 0x140672d2c
00672D20  44 0F 20 C1                     mov rcx, cr8
00672D24  40 8A D6                        mov dl, sil
00672D27  E8 6C 29 E8 FF                  call 0x1404f5698
00672D2C  40 0F B6 C6                     movzx eax, sil
00672D30  44 0F 22 C0                     mov cr8, rax
00672D34  45 0B 74 24 10                  or r14d, dword ptr [r12 + 0x10]
00672D39  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00672D3E  EB 22                           jmp 0x140672d62
00672D40  48 8D 0D B9 5F 7C 00            lea rcx, [rip + 0x7c5fb9]
00672D47  48 3B F1                        cmp rsi, rcx
00672D4A  74 11                           je 0x140672d5d
00672D4C  48 8B D1                        mov rdx, rcx
00672D4F  4C 8B CF                        mov r9, rdi
00672D52  48 8B CE                        mov rcx, rsi
00672D55  4D 8B C7                        mov r8, r15
00672D58  E8 77 F4 01 00                  call 0x1406921d4
00672D5D  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00672D62  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00672D67  C6 44 24 40 11                  mov byte ptr [rsp + 0x40], 0x11
00672D6C  4D 85 E4                        test r12, r12
00672D6F  74 10                           je 0x140672d81
00672D71  44 0F B7 06                     movzx r8d, word ptr [rsi]
00672D75  48 8D 4D C8                     lea rcx, [rbp - 0x38]
00672D79  41 8B D6                        mov edx, r14d
00672D7C  E8 A3 EA FF FF                  call 0x140671824
00672D81  48 85 FF                        test rdi, rdi
00672D84  0F 84 41 03 00 00               je 0x1406730cb
00672D8A  48 8B D7                        mov rdx, rdi
00672D8D  49 8B CF                        mov rcx, r15
00672D90  E8 07 EC D8 FF                  call 0x14040199c
00672D95  48 8B F0                        mov rsi, rax
00672D98  4D 85 E4                        test r12, r12
00672D9B  74 7A                           je 0x140672e17
00672D9D  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00672DA2  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00672DA7  41 8B C8                        mov ecx, r8d
00672DAA  B8 00 10 00 00                  mov eax, 0x1000
00672DAF  81 E1 FF 0F 00 00               and ecx, 0xfff
00672DB5  2B C1                           sub eax, ecx
00672DB7  8B C8                           mov ecx, eax
00672DB9  48 C1 E9 03                     shr rcx, 3
00672DBD  48 3B F1                        cmp rsi, rcx
00672DC0  48 0F 46 CE                     cmovbe rcx, rsi
00672DC4  48 8B F1                        mov rsi, rcx
00672DC7  49 8B C8                        mov rcx, r8
00672DCA  E8 41 E0 CA FF                  call 0x140320e10
00672DCF  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
00672DD3  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00672DD8  48 C1 E1 04                     shl rcx, 4
00672DDC  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00672DE6  48 8B D0                        mov rdx, rax
00672DE9  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
00672DEE  4C 8D 45 C8                     lea r8, [rbp - 0x38]
00672DF2  48 03 CA                        add rcx, rdx
00672DF5  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00672DFA  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00672DFF  49 8B 14 24                     mov rdx, qword ptr [r12]
00672E03  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00672E08  48 8B D6                        mov rdx, rsi
00672E0B  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00672E10  E8 7F E0 FF FF                  call 0x140670e94
00672E15  EB 6D                           jmp 0x140672e84
00672E17  33 D2                           xor edx, edx
00672E19  48 8D 4D 00                     lea rcx, [rbp]
00672E1D  41 B8 68 01 00 00               mov r8d, 0x168
00672E23  E8 18 3E 05 00                  call 0x1406c6c40
00672E28  49 8B CF                        mov rcx, r15
00672E2B  E8 A0 5E CC FF                  call 0x140338cd0
00672E30  41 B8 01 00 00 00               mov r8d, 1
00672E36  48 8D 4D 00                     lea rcx, [rbp]
00672E3A  8B D0                           mov edx, eax
00672E3C  E8 9B BB DC FF                  call 0x14043e9dc
00672E41  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00672E46  48 89 85 A8 00 00 00            mov qword ptr [rbp + 0xa8], rax
00672E4D  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00672E53  83 C8 04                        or eax, 4
00672E56  44 89 B5 B4 00 00 00            mov dword ptr [rbp + 0xb4], r14d
00672E5D  4C 89 7D 00                     mov qword ptr [rbp], r15
00672E61  48 89 75 08                     mov qword ptr [rbp + 8], rsi
00672E65  89 85 B8 00 00 00               mov dword ptr [rbp + 0xb8], eax
00672E6B  41 0F BA E6 12                  bt r14d, 0x12
00672E70  72 09                           jb 0x140672e7b
00672E72  41 0B C5                        or eax, r13d
00672E75  89 85 B8 00 00 00               mov dword ptr [rbp + 0xb8], eax
00672E7B  48 8D 4D 00                     lea rcx, [rbp]
00672E7F  E8 B0 5D C5 FF                  call 0x1402c8c34
00672E84  48 39 5C 24 50                  cmp qword ptr [rsp + 0x50], rbx
00672E89  74 1C                           je 0x140672ea7
00672E8B  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
00672E8F  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00672E94  E8 F7 31 BD FF                  call 0x140246090
00672E99  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00672E9E  48 8D 04 F0                     lea rax, [rax + rsi*8]
00672EA2  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00672EA7  4C 03 FE                        add r15, rsi
00672EAA  48 2B FE                        sub rdi, rsi
00672EAD  0F 85 D7 FE FF FF               jne 0x140672d8a
00672EB3  E9 13 02 00 00                  jmp 0x1406730cb
00672EB8  41 8B C6                        mov eax, r14d
00672EBB  41 BD 02 00 00 00               mov r13d, 2
00672EC1  41 23 C5                        and eax, r13d
00672EC4  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00672EC8  75 0E                           jne 0x140672ed8
00672ECA  45 33 C9                        xor r9d, r9d
00672ECD  4C 8B C7                        mov r8, rdi
00672ED0  49 8B D7                        mov rdx, r15
00672ED3  E8 C4 32 D0 FF                  call 0x14037619c
00672ED8  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00672EDC  48 8B 0D A5 D1 7B 00            mov rcx, qword ptr [rip + 0x7bd1a5]
00672EE3  48 C1 E8 2B                     shr rax, 0x2b
00672EE7  25 FF 03 00 00                  and eax, 0x3ff
00672EEC  4C 8B 14 C1                     mov r10, qword ptr [rcx + rax*8]
00672EF0  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00672EFA  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00672EFE  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00672F02  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
00672F05  41 0F B7 12                     movzx edx, word ptr [r10]
00672F09  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00672F0D  C1 E8 10                        shr eax, 0x10
00672F10  24 F8                           and al, 0xf8
00672F12  48 C1 E2 2B                     shl rdx, 0x2b
00672F16  0A C3                           or al, bl
00672F18  4C 89 54 24 60                  mov qword ptr [rsp + 0x60], r10
00672F1D  88 44 24 4A                     mov byte ptr [rsp + 0x4a], al
00672F21  48 8B CA                        mov rcx, rdx
00672F24  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
00672F28  89 45 88                        mov dword ptr [rbp - 0x78], eax
00672F2B  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00672F2F  48 33 C8                        xor rcx, rax
00672F32  48 B8 FF FF FF FF FF 07 E0 FF   movabs rax, 0xffe007ffffffffff
00672F3C  48 23 C8                        and rcx, rax
00672F3F  48 33 CA                        xor rcx, rdx
00672F42  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
00672F46  48 8D 0D B3 5D 7C 00            lea rcx, [rip + 0x7c5db3]
00672F4D  4C 3B D1                        cmp r10, rcx
00672F50  74 0E                           je 0x140672f60
00672F52  4C 8B CF                        mov r9, rdi
00672F55  4D 8B C7                        mov r8, r15
00672F58  49 8B D2                        mov rdx, r10
00672F5B  E8 74 F2 01 00                  call 0x1406921d4
00672F60  48 8D 04 7F                     lea rax, [rdi + rdi*2]
00672F64  48 C1 E0 04                     shl rax, 4
00672F68  48 03 F0                        add rsi, rax
00672F6B  33 DB                           xor ebx, ebx
00672F6D  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00672F72  45 0F 20 C7                     mov r15, cr8
00672F76  45 0F 22 C5                     mov cr8, r13
00672F7A  39 1D A0 3D 95 00               cmp dword ptr [rip + 0x953da0], ebx
00672F80  74 0B                           je 0x140672f8d
00672F82  41 8A D5                        mov dl, r13b
00672F85  41 8A CF                        mov cl, r15b
00672F88  E8 6F 27 E8 FF                  call 0x1404f56fc
00672F8D  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
00672F92  48 85 FF                        test rdi, rdi
00672F95  0F 84 14 01 00 00               je 0x1406730af
00672F9B  41 83 E6 20                     and r14d, 0x20
00672F9F  4C 8D 66 18                     lea r12, [rsi + 0x18]
00672FA3  48 83 EE 30                     sub rsi, 0x30
00672FA7  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00672FAB  4D 8D 64 24 D0                  lea r12, [r12 - 0x30]
00672FB0  F0 49 0F BA 2C 24 3F            lock bts qword ptr [r12], 0x3f
00672FB7  73 15                           jae 0x140672fce
00672FB9  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00672FBE  E8 3D 8D D8 FF                  call 0x1403fbd00
00672FC3  49 8B 04 24                     mov rax, qword ptr [r12]
00672FC7  48 85 C0                        test rax, rax
00672FCA  78 ED                           js 0x140672fb9
00672FCC  EB E2                           jmp 0x140672fb0
00672FCE  39 5C 24 50                     cmp dword ptr [rsp + 0x50], ebx
00672FD2  75 05                           jne 0x140672fd9
00672FD4  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00672FD9  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00672FDE  C1 E8 18                        shr eax, 0x18
00672FE1  A8 40                           test al, 0x40
00672FE3  74 11                           je 0x140672ff6
00672FE5  45 33 C9                        xor r9d, r9d
00672FE8  33 D2                           xor edx, edx
00672FEA  48 8B CE                        mov rcx, rsi
00672FED  45 8D 41 01                     lea r8d, [r9 + 1]
00672FF1  E8 DA 74 00 00                  call 0x14067a4d0
00672FF6  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00672FFB  E8 48 F3 DE FF                  call 0x140462348
00673000  48 8B CE                        mov rcx, rsi
00673003  85 C0                           test eax, eax
00673005  75 0C                           jne 0x140673013
00673007  45 85 F6                        test r14d, r14d
0067300A  75 21                           jne 0x14067302d
0067300C  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00673011  EB 1E                           jmp 0x140673031
00673013  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00673018  E8 E3 54 DD FF                  call 0x140448500
0067301D  48 8B CE                        mov rcx, rsi
00673020  E8 3B E1 C2 FF                  call 0x1402a1160
00673025  45 85 F6                        test r14d, r14d
00673028  74 0C                           je 0x140673036
0067302A  48 8B CE                        mov rcx, rsi
0067302D  48 8D 55 98                     lea rdx, [rbp - 0x68]
00673031  E8 CA 54 DD FF                  call 0x140448500
00673036  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00673040  F0 49 21 04 24                  lock and qword ptr [r12], rax
00673045  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0067304A  48 FF C0                        inc rax
0067304D  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00673052  A8 3F                           test al, 0x3f
00673054  75 49                           jne 0x14067309f
00673056  E8 85 43 C0 FF                  call 0x1402773e0
0067305B  85 C0                           test eax, eax
0067305D  74 40                           je 0x14067309f
0067305F  39 1D BB 3C 95 00               cmp dword ptr [rip + 0x953cbb], ebx
00673065  74 0D                           je 0x140673074
00673067  44 0F 20 C1                     mov rcx, cr8
0067306B  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
0067306F  E8 24 26 E8 FF                  call 0x1404f5698
00673074  0F B6 44 24 40                  movzx eax, byte ptr [rsp + 0x40]
00673079  44 0F 22 C0                     mov cr8, rax
0067307D  45 0F 20 C7                     mov r15, cr8
00673081  45 0F 22 C5                     mov cr8, r13
00673085  39 1D 95 3C 95 00               cmp dword ptr [rip + 0x953c95], ebx
0067308B  74 0B                           je 0x140673098
0067308D  41 8A D5                        mov dl, r13b
00673090  41 8A CF                        mov cl, r15b
00673093  E8 64 26 E8 FF                  call 0x1404f56fc
00673098  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
0067309D  EB 05                           jmp 0x1406730a4
0067309F  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
006730A4  48 39 7C 24 58                  cmp qword ptr [rsp + 0x58], rdi
006730A9  0F 82 F4 FE FF FF               jb 0x140672fa3
006730AF  39 1D 6B 3C 95 00               cmp dword ptr [rip + 0x953c6b], ebx
006730B5  74 0C                           je 0x1406730c3
006730B7  44 0F 20 C1                     mov rcx, cr8
006730BB  41 8A D7                        mov dl, r15b
006730BE  E8 D5 25 E8 FF                  call 0x1404f5698
006730C3  41 0F B6 C7                     movzx eax, r15b
006730C7  44 0F 22 C0                     mov cr8, rax
006730CB  48 8B 8D 70 01 00 00            mov rcx, qword ptr [rbp + 0x170]
006730D2  48 33 CC                        xor rcx, rsp
006730D5  E8 66 95 03 00                  call 0x1406ac640
006730DA  48 81 C4 88 02 00 00            add rsp, 0x288
006730E1  41 5F                           pop r15
006730E3  41 5E                           pop r14
006730E5  41 5D                           pop r13
006730E7  41 5C                           pop r12
006730E9  5F                              pop rdi
006730EA  5E                              pop rsi
006730EB  5B                              pop rbx
006730EC  5D                              pop rbp
006730ED  C3                              ret
006730EE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializeDynamicPfns(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m110;
    unsigned int v_stack_m114;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int8 v_stack_m27E;
    unsigned __int64 v_stack_m280;
    unsigned __int8 v_stack_m288;
    unsigned int v_stack_m298;
    unsigned int v_stack_m2A0;
    unsigned int v_stack_m2A8;
    unsigned __int64 v_stack_m58;

    v_rsp = (v_rsp) - (648);
    result = (*(unsigned __int64 *)(v_rip + 7961421)) ^ (v_rsp);
    v_stack_m58 = result;
    v_rsi = (a1 + a1 * 2) << (4);
    v_stack_m280 = a3;
    v_stack_m230 = v_xmm0;
    v_stack_m220 = v_xmm0;
    v_stack_m210 = v_xmm0;
    v_stack_m260 = v_xmm1;
    v_stack_m250 = v_xmm1;
    v_stack_m240 = v_xmm1;
    v_rsi = (v_rsi) + (result);
    result = (unsigned int)(((unsigned int)(a4)) & (0x8000AULL));
    v_rbx = 5;
    if (((unsigned int)(result)) == 8) {
        a3 = (unsigned int)(5 - 4);
        result = MiUpdatePhysicalPages(v_rip + 8151215, a2, a3, a4);
        a1 = v_rip + 8151178;
        v_rbx = 5 - 4 + 5;
    }
    if ((((unsigned __int8)(5 - 4)) & ((unsigned __int8)((unsigned int)(a4)))) == 0) goto loc_00672EB8;
    v_rbx = 0;
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    if ((((unsigned int)((unsigned int)(a4))) & (0x3000ULL)) != 0) {
        a4 = (unsigned int)((unsigned int)(a4));
        v_stack_m298 = 0;
        a4 = (unsigned int)((a4) >> (12));
        a3 = a2;
        a4 = (unsigned int)((a4) & ((unsigned int)(5 - 4)));
        v_stack_m2A0 = (unsigned int)(5 - 4);
        a2 = a1;
        v_stack_m2A8 = (unsigned int)(5 - 4);
        a1 = v_stack_m280;
        result = MiInitializeAllResidentPageBasePfns(a1, a2, a3, a4);
    }
    if (((2) & ((unsigned __int8)((unsigned int)(a4)))) == 0) goto loc_00672D40;
    v_stack_m278 = *(unsigned __int64 *)(a5 + 8);
    v_stack_m270 = *(unsigned __int64 *)(*(unsigned __int64 *)(a5));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a5));
    if ((*(unsigned int *)(v_rip + 9781289)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
        result = v_stack_m270;
    }
    result = MiReferenceControlAreaPfn(result, *(unsigned __int64 *)(a5), (unsigned int)((unsigned int)(a2)), a4);
    if ((*(unsigned int *)(v_rip + 9781250)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)((unsigned int)(a2)), a4);
    }
    v_r14 = (unsigned int)(((unsigned int)(a4)) | (*(unsigned int *)(a5 + 16)));
    goto loc_00672D62;
loc_00672D40:
    result = (unsigned __int8)(v_cr8);
    if (v_stack_m280 != (v_rip + 8150969)) {
        a2 = v_rip + 8150969;
        a4 = a2;
        a1 = v_stack_m280;
        a3 = a1;
        result = MiUpdatePartitionChildPageCounts(a1, a2, a3, a4);
    }
    v_stack_m278 = 0;
loc_00672D62:
    v_stack_m270 = 0;
    v_stack_m288 = 17;
    if (a5 != 0) {
        a3 = *(unsigned __int16 *)(v_stack_m280);
        a1 = v_stack_m200;
        a2 = (unsigned int)(v_r14);
        result = MiCreatePfnTemplate(a1, a2, a3, a4);
    }
    if (a2 == 0) goto loc_006730CB;
loc_00672D8A:
    result = MiRestrictRangeToNode(a1, a2, a3, a4);
    if (a5 == 0) goto loc_00672E17;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m278))) & (0xFFFULL));
    result = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)(a1)));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    if (result <= a1) { a1 = result; }
    result = MiLockProtoPoolPageForce(v_stack_m278, v_stack_m288, v_stack_m278, a4);
    v_stack_m270 = result;
    a1 = (a1 + a1 * 2) << (4);
    a1 = (a1) + (result);
    v_stack_m298 = v_stack_m278;
    v_stack_m2A0 = *(unsigned __int64 *)(a5);
    v_stack_m2A8 = (unsigned int)(v_r14);
    result = MiInitializeNewPfns(a1, a1, v_stack_m200, v_stack_m280);
    goto loc_00672E84;
loc_00672E17:
    a2 = 0;
    result = memset(v_stack_m1C8, a2, 360, v_stack_m280);
    result = MiPageToNode(a1, a2, 360, v_stack_m280);
    result = MiInitializeDpcGang(v_stack_m1C8, (unsigned int)((unsigned int)(result)), 1, v_stack_m280);
    v_stack_m120 = v_stack_m280;
    result = (unsigned int)(((unsigned int)(v_stack_m110)) | (4));
    v_stack_m114 = (unsigned int)(v_r14);
    v_stack_m1C8 = a1;
    v_stack_m1C0 = a1;
    v_stack_m110 = (unsigned int)(result);
    if (!(condition_is_below)) {
        result = (unsigned int)((result) | (2));
        v_stack_m110 = (unsigned int)(result);
    }
    result = MiStartDpcGang(v_stack_m1C8, (unsigned int)((unsigned int)(result)), 1, v_stack_m280);
loc_00672E84:
    if (v_stack_m278 != 0) {
        a2 = v_stack_m288;
        a1 = v_stack_m270;
        result = MiUnlockProtoPoolPage(a1, a2, 1, v_stack_m280);
        result = v_stack_m278;
        result = result + a1 * 8;
        v_stack_m278 = result;
    }
    v_r15 = (a1) + (a1);
    v_rdi = (a2) - (a1);
    if (condition_is_not_equal) goto loc_00672D8A;
    goto loc_006730CB;
loc_00672EB8:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (2));
    v_stack_m278 = (unsigned int)(result);
    if (!(condition_is_not_equal)) {
        a4 = 0;
        a3 = v_rdi;
        a2 = v_r15;
        result = MiUpdateLargePageBitMap(a1, a2, a3, a4);
    }
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m218 = result;
    v_stack_m248 = result;
    v_stack_m280 = (unsigned int)((unsigned int)(v_stack_m240));
    result = (unsigned int)(((unsigned int)(v_stack_m240)) >> (16));
    result = (unsigned __int8)((result) & (248));
    a2 = (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8114597) + result * 8))) << (43);
    result = (unsigned __int8)((result) | (0));
    v_stack_m268 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8114597) + result * 8);
    v_stack_m27E = (unsigned __int8)(result);
    v_stack_m240 = (unsigned int)((unsigned int)(v_stack_m280));
    a1 = (a2) ^ (v_stack_m238);
    a1 = (a1) & (v_stack_m238);
    a1 = (a1) ^ (a2);
    v_stack_m238 = a1;
    result = v_stack_m238;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8114597) + result * 8)) != (v_rip + 8150451)) {
        a4 = v_rdi;
        a3 = v_r15;
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8114597) + result * 8);
        result = MiUpdatePartitionChildPageCounts(v_rip + 8150451, a2, a3, a4);
    }
    result = (v_rdi + v_rdi * 2) << (4);
    v_rsi = (a1) + (result);
    v_rbx = 0;
    v_stack_m270 = 0;
    if ((*(unsigned int *)(v_rip + 9780640)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_stack_m288 = (unsigned __int8)((unsigned __int8)(v_cr8));
    if (v_rdi == 0) goto loc_006730AF;
    v_r14 = (unsigned int)((v_r14) & (32));
loc_00672FA3:
    v_rsi = (v_rsi) - (48);
    v_stack_m280 = 0;
loc_00672FB0:
    if (condition_is_above_or_equal) goto loc_00672FCE;
loc_00672FB9:
    result = KeYieldProcessorEx(v_stack_m280, a2, a3, a4);
    if (sign_flag) goto loc_00672FB9;
    goto loc_00672FB0;
loc_00672FCE:
    result = *(unsigned __int64 *)(v_rsi + 24 - 48);
    if (v_stack_m278 == 0) {
        result = *(unsigned int *)(v_rsi + 24 - 48 + 8);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 24 - 48 + 8))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) {
        a4 = 0;
        a2 = 0;
        a1 = v_rsi;
        a3 = a4 + 1;
        result = MiSetPfnRemovalRequested(a1, a2, a3, a4);
    }
    result = MiPageCombiningActive(v_stack_m268, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00673013;
    if ((unsigned int)(v_r14) != 0) goto loc_0067302D;
    goto loc_00673031;
loc_00673013:
    result = MiCopyPfnEntryRaw(v_rsi, v_stack_m260, a3, a4);
    result = MiAbortCombineScan(v_rsi, v_stack_m260, a3, a4);
    if ((unsigned int)(v_r14) == 0) goto loc_00673036;
loc_0067302D:
loc_00673031:
    result = MiCopyPfnEntryRaw(v_rsi, v_stack_m230, a3, a4);
loc_00673036:
    result = (v_stack_m270) + 1;
    v_stack_m270 = result;
    if ((((unsigned __int8)(result)) & (63)) != 0) goto loc_0067309F;
    result = KeShouldYieldProcessor(v_rsi, v_stack_m230, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0067309F;
    if ((*(unsigned int *)(v_rip + 9780411)) != 0) {
        a1 = 2;
        a2 = v_stack_m288;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    result = v_stack_m288;
    if ((*(unsigned int *)(v_rip + 9780373)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)(v_stack_m288);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_stack_m288 = (unsigned __int8)(v_stack_m288);
    goto loc_006730A4;
loc_0067309F:
loc_006730A4:
    if (v_stack_m270 < v_rdi) goto loc_00672FA3;
loc_006730AF:
    if ((*(unsigned int *)(v_rip + 9780331)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m288);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_006730CB:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (648);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitializeDynamicPfns(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m110;
    uint32_t v_stack_m114;
    uint64_t v_stack_m120;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m200;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint8_t v_stack_m27E;
    uint64_t v_stack_m280;
    uint8_t v_stack_m288;
    uint32_t v_stack_m298;
    uint32_t v_stack_m2A0;
    uint32_t v_stack_m2A8;
    uint64_t v_stack_m58;

    local_rsp = (local_rsp) - (648);
    result = (*(uint64_t *)(v_rip + 0x797B4D)) ^ (local_rsp);
    v_stack_m58 = result;
    local_rsi = (Arg1 + Arg1 * 2) << (4);
    v_stack_m280 = Arg3;
    v_stack_m230 = v_xmm0;
    v_stack_m220 = v_xmm0;
    v_stack_m210 = v_xmm0;
    v_stack_m260 = v_xmm1;
    v_stack_m250 = v_xmm1;
    v_stack_m240 = v_xmm1;
    local_rsi = (local_rsi) + (result);
    result = (uint32_t)(((uint32_t)(Arg4)) & (0x8000AULL));
    local_rbx = 5;
    if (((uint32_t)(result)) == 8) {
        Arg3 = (uint32_t)(5 - 4);
        result = MiUpdatePhysicalPages(v_rip + 8151215, Arg2, Arg3, Arg4);
        Arg1 = v_rip + 8151178;
        local_rbx = 5 - 4 + 5;
    }
    if ((((uint8_t)(5 - 4)) & ((uint8_t)((uint32_t)(Arg4)))) == 0) goto loc_00672EB8;
    local_rbx = 0;
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x3000ULL)) != 0) {
        Arg4 = (uint32_t)((uint32_t)(Arg4));
        v_stack_m298 = 0;
        Arg4 = (uint32_t)((Arg4) >> (12));
        Arg3 = Arg2;
        Arg4 = (uint32_t)((Arg4) & ((uint32_t)(5 - 4)));
        v_stack_m2A0 = (uint32_t)(5 - 4);
        Arg2 = Arg1;
        v_stack_m2A8 = (uint32_t)(5 - 4);
        Arg1 = v_stack_m280;
        result = MiInitializeAllResidentPageBasePfns(Arg1, Arg2, Arg3, Arg4);
    }
    if (((2) & ((uint8_t)((uint32_t)(Arg4)))) == 0) goto loc_00672D40;
    v_stack_m278 = *(uint64_t *)(arg5 + 0x8);
    v_stack_m270 = *(uint64_t *)(*(uint64_t *)(arg5));
    result = *(uint64_t *)(*(uint64_t *)(arg5));
    if ((*(uint32_t *)(v_rip + 0x954029)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m270;
    }
    result = MiReferenceControlAreaPfn(result, *(uint64_t *)(arg5), (uint32_t)((uint32_t)(Arg2)), Arg4);
    if ((*(uint32_t *)(v_rip + 0x954002)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)((uint32_t)(Arg2)), Arg4);
    }
    local_r14 = (uint32_t)(((uint32_t)(Arg4)) | (*(uint32_t *)(arg5 + 0x10)));
    goto loc_00672D62;
loc_00672D40:
    result = (uint8_t)(v_cr8);
    if (v_stack_m280 != (v_rip + 8150969)) {
        Arg2 = v_rip + 8150969;
        Arg4 = Arg2;
        Arg1 = v_stack_m280;
        Arg3 = Arg1;
        result = MiUpdatePartitionChildPageCounts(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m278 = 0;
loc_00672D62:
    v_stack_m270 = 0;
    v_stack_m288 = 17;
    if (Arg5 != NULL) {
        Arg3 = *(uint16_t *)(v_stack_m280);
        Arg1 = v_stack_m200;
        Arg2 = (uint32_t)(local_r14);
        result = MiCreatePfnTemplate(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg2 == NULL) goto loc_006730CB;
loc_00672D8A:
    result = MiRestrictRangeToNode(Arg1, Arg2, Arg3, Arg4);
    if (Arg5 == NULL) goto loc_00672E17;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m278))) & (0xFFFULL));
    result = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)(Arg1)));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    if (result <= Arg1) { Arg1 = result; }
    result = MiLockProtoPoolPageForce(v_stack_m278, v_stack_m288, v_stack_m278, Arg4);
    v_stack_m270 = result;
    Arg1 = (Arg1 + Arg1 * 2) << (4);
    Arg1 = (Arg1) + (result);
    v_stack_m298 = v_stack_m278;
    v_stack_m2A0 = *(uint64_t *)(arg5);
    v_stack_m2A8 = (uint32_t)(local_r14);
    result = MiInitializeNewPfns(Arg1, Arg1, v_stack_m200, v_stack_m280);
    goto loc_00672E84;
loc_00672E17:
    Arg2 = 0;
    result = memset(v_stack_m1C8, Arg2, 360, v_stack_m280);
    result = MiPageToNode(Arg1, Arg2, 360, v_stack_m280);
    result = MiInitializeDpcGang(v_stack_m1C8, (uint32_t)((uint32_t)(result)), 1, v_stack_m280);
    v_stack_m120 = v_stack_m280;
    result = (uint32_t)(((uint32_t)(v_stack_m110)) | (4));
    v_stack_m114 = (uint32_t)(local_r14);
    v_stack_m1C8 = Arg1;
    v_stack_m1C0 = Arg1;
    v_stack_m110 = (uint32_t)(result);
    if (!(condition_is_below)) {
        result = (uint32_t)((result) | (2));
        v_stack_m110 = (uint32_t)(result);
    }
    result = MiStartDpcGang(v_stack_m1C8, (uint32_t)((uint32_t)(result)), 1, v_stack_m280);
loc_00672E84:
    if (v_stack_m278 != 0) {
        Arg2 = v_stack_m288;
        Arg1 = v_stack_m270;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, 1, v_stack_m280);
        result = v_stack_m278;
        result = result + Arg1 * 8;
        v_stack_m278 = result;
    }
    local_r15 = (Arg1) + (Arg1);
    local_rdi = (Arg2) - (Arg1);
    if (condition_is_not_equal) goto loc_00672D8A;
    goto loc_006730CB;
loc_00672EB8:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (2));
    v_stack_m278 = (uint32_t)(result);
    if (!(condition_is_not_equal)) {
        Arg4 = 0;
        Arg3 = local_rdi;
        Arg2 = local_r15;
        result = MiUpdateLargePageBitMap(Arg1, Arg2, Arg3, Arg4);
    }
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m218 = result;
    v_stack_m248 = result;
    v_stack_m280 = (uint32_t)((uint32_t)(v_stack_m240));
    result = (uint32_t)(((uint32_t)(v_stack_m240)) >> (16));
    result = (uint8_t)((result) & (248));
    Arg2 = (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BD1A5) + result * 8))) << (43);
    result = (uint8_t)((result) | (0));
    v_stack_m268 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x7BD1A5) + result * 8);
    v_stack_m27E = (uint8_t)(result);
    v_stack_m240 = (uint32_t)((uint32_t)(v_stack_m280));
    Arg1 = (Arg2) ^ (v_stack_m238);
    Arg1 = (Arg1) & (v_stack_m238);
    Arg1 = (Arg1) ^ (Arg2);
    v_stack_m238 = Arg1;
    result = v_stack_m238;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BD1A5) + result * 8)) != (v_rip + 8150451)) {
        Arg4 = local_rdi;
        Arg3 = local_r15;
        Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x7BD1A5) + result * 8);
        result = MiUpdatePartitionChildPageCounts(v_rip + 8150451, Arg2, Arg3, Arg4);
    }
    result = (local_rdi + local_rdi * 2) << (4);
    local_rsi = (Arg1) + (result);
    local_rbx = 0;
    v_stack_m270 = 0;
    if ((*(uint32_t *)(v_rip + 0x953DA0)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)((uint8_t)(v_cr8));
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m288 = (uint8_t)((uint8_t)(v_cr8));
    if (local_rdi == 0) goto loc_006730AF;
    local_r14 = (uint32_t)((local_r14) & (32));
loc_00672FA3:
    local_rsi = (local_rsi) - (48);
    v_stack_m280 = 0;
loc_00672FB0:
    if (condition_is_above_or_equal) goto loc_00672FCE;
loc_00672FB9:
    result = KeYieldProcessorEx(v_stack_m280, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00672FB9;
    goto loc_00672FB0;
loc_00672FCE:
    result = *(uint64_t *)(local_rsi + 0x18 - 0x30);
    if (v_stack_m278 == 0) {
        result = *(uint32_t *)(local_rsi + 0x18 - 0x30 + 0x8);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x18 - 0x30 + 0x8))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) {
        Arg4 = 0;
        Arg2 = 0;
        Arg1 = local_rsi;
        Arg3 = Arg4 + 1;
        result = MiSetPfnRemovalRequested(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiPageCombiningActive(v_stack_m268, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00673013;
    if ((uint32_t)(local_r14) != 0) goto loc_0067302D;
    goto loc_00673031;
loc_00673013:
    result = MiCopyPfnEntryRaw(local_rsi, v_stack_m260, Arg3, Arg4);
    result = MiAbortCombineScan(local_rsi, v_stack_m260, Arg3, Arg4);
    if ((uint32_t)(local_r14) == 0) goto loc_00673036;
loc_0067302D:
loc_00673031:
    result = MiCopyPfnEntryRaw(local_rsi, v_stack_m230, Arg3, Arg4);
loc_00673036:
    result = (v_stack_m270) + 1;
    v_stack_m270 = result;
    if ((((uint8_t)(result)) & (63)) != 0) goto loc_0067309F;
    result = KeShouldYieldProcessor(local_rsi, v_stack_m230, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0067309F;
    if ((*(uint32_t *)(v_rip + 0x953CBB)) != 0) {
        Arg1 = 2;
        Arg2 = v_stack_m288;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    result = v_stack_m288;
    if ((*(uint32_t *)(v_rip + 0x953C95)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)(v_stack_m288);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m288 = (uint8_t)(v_stack_m288);
    goto loc_006730A4;
loc_0067309F:
loc_006730A4:
    if (v_stack_m270 < local_rdi) goto loc_00672FA3;
loc_006730AF:
    if ((*(uint32_t *)(v_rip + 0x953C6B)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m288);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
loc_006730CB:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (648);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + r15*2` | `64` | `R` |
| `Arg1` | `+ 0x0 + rcx*2` | `64` | `R` |
| `Arg2` | `+ 0x0 + rdi*2` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x8` | `64` | `R` |
| `Arg5` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00672BD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
