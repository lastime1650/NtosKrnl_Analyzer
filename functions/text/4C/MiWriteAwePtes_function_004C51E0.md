# MiWriteAwePtes

- RVA: `0x004C51E0`–`0x004C5A6F` (길이 `2,191` bytes)
- VA: `0x00000001404C51E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCE60`
- 디코드: `574`개 명령, `2,191/2,191` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x004C525A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C5286` → [MiGetAweViewPageSize](MiGetAweViewPageSize_function_004C51AC.md) (function, `0x004C51AC`)
- `0x004C529C` → [MiPageSizeToPteLevel](../41/MiPageSizeToPteLevel_function_0041F57C.md) (function, `0x0041F57C`)
- `0x004C5349` → [MI_GET_GRAPHICS_PROTECTION_FROM_VAD](../43/MI_GET_GRAPHICS_PROTECTION_FROM_VAD_function_00438CA0.md) (function, `0x00438CA0`)
- `0x004C535F` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x004C538E` → [Feature_Servicing_Mm_AweLazyFlushOptIn__private_IsEnabledDeviceUsageNoInline](../68/Feature_Servicing_Mm_AweLazyFlushOptIn__private_IsEnabledDeviceUsageNoInline_function_00687974.md) (function, `0x00687974`)
- `0x004C54BF` → [MiGetAweNode](../4F/MiGetAweNode_function_004F600C.md) (function, `0x004F600C`)
- `0x004C5515` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x004C55B0` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x004C562C` → [MiFinishPteChangesInPageTable](../4E/MiFinishPteChangesInPageTable_function_004EE660.md) (function, `0x004EE660`)
- `0x004C5640` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x004C5655` → [Feature_Servicing_Mm_AweLazyFlushOptIn__private_IsEnabledDeviceUsageNoInline](../68/Feature_Servicing_Mm_AweLazyFlushOptIn__private_IsEnabledDeviceUsageNoInline_function_00687974.md) (function, `0x00687974`)
- `0x004C5676` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x004C569C` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x004C56D0` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x004C56E1` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x004C56F3` → [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) (function, `0x00276340`)
- `0x004C572E` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004C5740` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x004C5813` → [MiCompareTbFlushTimeStamp](../31/MiCompareTbFlushTimeStamp_function_0031ADE4.md) (function, `0x0031ADE4`)
- `0x004C5825` → [MiZeroAndFlushAweLazyPtes](../68/MiZeroAndFlushAweLazyPtes_function_00689B1C.md) (function, `0x00689B1C`)
- `0x004C58D2` → [MiWriteAweClusterPte](../4E/MiWriteAweClusterPte_function_004E16A8.md) (function, `0x004E16A8`)
- `0x004C5947` → [MiGetAweFlushList](../68/MiGetAweFlushList_function_00688D34.md) (function, `0x00688D34`)
- `0x004C595F` → [MiInsertAweFlushList](../68/MiInsertAweFlushList_function_00688FEC.md) (function, `0x00688FEC`)
- `0x004C59A0` → [MiDecrementAweMapCount](../68/MiDecrementAweMapCount_function_00688158.md) (function, `0x00688158`)
- `0x004C59D0` → [MiDecrementAweMapCount](../68/MiDecrementAweMapCount_function_00688158.md) (function, `0x00688158`)
- `0x004C5A42` → [MiFinishPteChangesInPageTable](../4E/MiFinishPteChangesInPageTable_function_004EE660.md) (function, `0x004EE660`)
- `0x004C5A4E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiDeleteVadAwePtes](MiDeleteVadAwePtes_function_004C4F3C.md) at `0x004C509F`
- [NtMapUserPhysicalPages](../../page/80/NtMapUserPhysicalPages_function_0080B460.md) at `0x0080B69F`
- [NtMapUserPhysicalPagesScatter](../../page/80/NtMapUserPhysicalPagesScatter_function_0080B750.md) at `0x0080BA29`

### Static image references
- `0x004C51FC` → RVA `0x00E0A740` (`.data`; read)
- `0x004C5549` → RVA `0x00010880` (`.rdata`; read)
- `0x004C57D9` → RVA `0x00E2DC80` (`.data`; read)
- `0x004C5980` → RVA `0x00FCF080` (`CACHEALI`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C51E0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
004C51E5  55                              push rbp
004C51E6  56                              push rsi
004C51E7  57                              push rdi
004C51E8  41 54                           push r12
004C51EA  41 55                           push r13
004C51EC  41 56                           push r14
004C51EE  41 57                           push r15
004C51F0  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
004C51F5  48 81 EC 70 01 00 00            sub rsp, 0x170
004C51FC  48 8B 05 3D 55 94 00            mov rax, qword ptr [rip + 0x94553d]
004C5203  48 33 C4                        xor rax, rsp
004C5206  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
004C520A  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
004C5211  48 8B F2                        mov rsi, rdx
004C5214  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
004C5218  48 8B F9                        mov rdi, rcx
004C521B  4C 8B 85 D0 00 00 00            mov r8, qword ptr [rbp + 0xd0]
004C5222  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
004C5227  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004C5230  4C 8B 71 20                     mov r14, qword ptr [rcx + 0x20]
004C5234  48 8D 4D A0                     lea rcx, [rbp - 0x60]
004C5238  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
004C523D  33 D2                           xor edx, edx
004C523F  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
004C5244  41 B8 B8 00 00 00               mov r8d, 0xb8
004C524A  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
004C5251  4C 89 4D 88                     mov qword ptr [rbp - 0x78], r9
004C5255  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
004C525A  E8 E1 19 20 00                  call 0x1406c6c40
004C525F  48 8D 83 00 04 00 00            lea rax, [rbx + 0x400]
004C5266  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
004C526A  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
004C526E  48 8B CF                        mov rcx, rdi
004C5271  4C 89 75 48                     mov qword ptr [rbp + 0x48], r14
004C5275  4D 8B 4E 10                     mov r9, qword ptr [r14 + 0x10]
004C5279  45 8B 66 08                     mov r12d, dword ptr [r14 + 8]
004C527D  4C 89 4D 98                     mov qword ptr [rbp - 0x68], r9
004C5281  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
004C5286  E8 21 FF FF FF                  call 0x1404c51ac
004C528B  45 33 D2                        xor r10d, r10d
004C528E  49 8B C9                        mov rcx, r9
004C5291  48 85 C0                        test rax, rax
004C5294  48 0F 45 C8                     cmovne rcx, rax
004C5298  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
004C529C  E8 DB A2 F5 FF                  call 0x14041f57c
004C52A1  48 8B 5F 18                     mov rbx, qword ptr [rdi + 0x18]
004C52A5  83 F8 01                        cmp eax, 1
004C52A8  89 45 3C                        mov dword ptr [rbp + 0x3c], eax
004C52AB  41 BB 00 00 00 04               mov r11d, 0x4000000
004C52B1  45 0F 4C DA                     cmovl r11d, r10d
004C52B5  44 88 57 40                     mov byte ptr [rdi + 0x40], r10b
004C52B9  48 83 F9 10                     cmp rcx, 0x10
004C52BD  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
004C52C2  41 8D 42 01                     lea eax, [r10 + 1]
004C52C6  C7 45 E8 00 02 00 00            mov dword ptr [rbp - 0x18], 0x200
004C52CD  49 0F 44 C1                     cmove rax, r9
004C52D1  C6 45 50 11                     mov byte ptr [rbp + 0x50], 0x11
004C52D5  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
004C52D9  48 BF 78 FF FF FF 3F 00 00 00   movabs rdi, 0x3fffffff78
004C52E3  48 8D 45 F8                     lea rax, [rbp - 8]
004C52E7  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
004C52F1  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
004C52F5  8B 85 D8 00 00 00               mov eax, dword ptr [rbp + 0xd8]
004C52FB  89 45 38                        mov dword ptr [rbp + 0x38], eax
004C52FE  A8 01                           test al, 1
004C5300  0F 84 B1 00 00 00               je 0x1404c53b7
004C5306  B9 00 00 60 00                  mov ecx, 0x600000
004C530B  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
004C530F  44 8B 6B 30                     mov r13d, dword ptr [rbx + 0x30]
004C5313  41 8B C5                        mov eax, r13d
004C5316  23 C1                           and eax, ecx
004C5318  3B C1                           cmp eax, ecx
004C531A  74 0A                           je 0x1404c5326
004C531C  41 0F BA EB 1F                  bts r11d, 0x1f
004C5321  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
004C5326  41 F6 C4 01                     test r12b, 1
004C532A  74 0D                           je 0x1404c5339
004C532C  41 BD 04 00 00 00               mov r13d, 4
004C5332  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
004C5337  EB 18                           jmp 0x1404c5351
004C5339  41 C1 ED 07                     shr r13d, 7
004C533D  48 8B CB                        mov rcx, rbx
004C5340  41 83 E5 1F                     and r13d, 0x1f
004C5344  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
004C5349  E8 52 39 F7 FF                  call 0x140438ca0
004C534E  89 45 54                        mov dword ptr [rbp + 0x54], eax
004C5351  45 8B C3                        mov r8d, r11d
004C5354  45 0B C5                        or r8d, r13d
004C5357  49 8B C9                        mov rcx, r9
004C535A  48 03 CF                        add rcx, rdi
004C535D  33 D2                           xor edx, edx
004C535F  E8 2C 02 E0 FF                  call 0x1402c5590
004C5364  4C 8B F8                        mov r15, rax
004C5367  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004C536C  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
004C536F  BA 00 00 20 04                  mov edx, 0x4200000
004C5374  44 8B F0                        mov r14d, eax
004C5377  23 C2                           and eax, edx
004C5379  41 C1 EE 0C                     shr r14d, 0xc
004C537D  41 83 E6 7F                     and r14d, 0x7f
004C5381  44 89 74 24 4C                  mov dword ptr [rsp + 0x4c], r14d
004C5386  3B C2                           cmp eax, edx
004C5388  75 04                           jne 0x1404c538e
004C538A  83 4D B4 08                     or dword ptr [rbp - 0x4c], 8
004C538E  E8 E1 25 1C 00                  call 0x140687974
004C5393  45 33 D2                        xor r10d, r10d
004C5396  85 C0                           test eax, eax
004C5398  74 12                           je 0x1404c53ac
004C539A  48 83 FE 01                     cmp rsi, 1
004C539E  75 0C                           jne 0x1404c53ac
004C53A0  83 4D B4 01                     or dword ptr [rbp - 0x4c], 1
004C53A4  41 8B F2                        mov esi, r10d
004C53A7  4C 89 54 24 58                  mov qword ptr [rsp + 0x58], r10
004C53AC  48 8B 5D D0                     mov rbx, qword ptr [rbp - 0x30]
004C53B0  44 8B 5C 24 30                  mov r11d, dword ptr [rsp + 0x30]
004C53B5  EB 4D                           jmp 0x1404c5404
004C53B7  8B 4D B4                        mov ecx, dword ptr [rbp - 0x4c]
004C53BA  BA 00 00 20 04                  mov edx, 0x4200000
004C53BF  83 C9 04                        or ecx, 4
004C53C2  44 89 55 54                     mov dword ptr [rbp + 0x54], r10d
004C53C6  41 0F BA EB 1F                  bts r11d, 0x1f
004C53CB  89 4D B4                        mov dword ptr [rbp - 0x4c], ecx
004C53CE  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
004C53D1  41 BD 18 00 00 00               mov r13d, 0x18
004C53D7  23 C2                           and eax, edx
004C53D9  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
004C53DE  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
004C53E3  4D 8B FA                        mov r15, r10
004C53E6  44 89 54 24 4C                  mov dword ptr [rsp + 0x4c], r10d
004C53EB  45 8B F2                        mov r14d, r10d
004C53EE  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
004C53F3  3B C2                           cmp eax, edx
004C53F5  75 06                           jne 0x1404c53fd
004C53F7  83 C9 08                        or ecx, 8
004C53FA  89 4D B4                        mov dword ptr [rbp - 0x4c], ecx
004C53FD  49 8B DA                        mov rbx, r10
004C5400  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
004C5404  4D 8B CA                        mov r9, r10
004C5407  44 89 54 24 48                  mov dword ptr [rsp + 0x48], r10d
004C540C  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
004C5411  4C 39 55 80                     cmp qword ptr [rbp - 0x80], r10
004C5415  0F 86 23 06 00 00               jbe 0x1404c5a3e
004C541B  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
004C5420  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
004C5424  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
004C542E  48 85 C0                        test rax, rax
004C5431  0F 84 20 01 00 00               je 0x1404c5557
004C5437  4E 8B 04 C8                     mov r8, qword ptr [rax + r9*8]
004C543B  49 8B F8                        mov rdi, r8
004C543E  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004C5448  48 C1 EF 09                     shr rdi, 9
004C544C  48 23 FA                        and rdi, rdx
004C544F  48 8B C0                        mov rax, rax
004C5452  8B 4D 3C                        mov ecx, dword ptr [rbp + 0x3c]
004C5455  48 03 F8                        add rdi, rax
004C5458  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
004C545D  85 C9                           test ecx, ecx
004C545F  74 26                           je 0x1404c5487
004C5461  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
004C546B  48 C1 EF 09                     shr rdi, 9
004C546F  48 23 FA                        and rdi, rdx
004C5472  49 8B C4                        mov rax, r12
004C5475  48 03 F8                        add rdi, rax
004C5478  83 E9 01                        sub ecx, 1
004C547B  75 EE                           jne 0x1404c546b
004C547D  44 8B 64 24 50                  mov r12d, dword ptr [rsp + 0x50]
004C5482  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
004C5487  0F B6 4B 20                     movzx ecx, byte ptr [rbx + 0x20]
004C548B  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
004C548E  48 C1 E1 20                     shl rcx, 0x20
004C5492  48 0B C8                        or rcx, rax
004C5495  48 C1 E1 0C                     shl rcx, 0xc
004C5499  4C 3B C1                        cmp r8, rcx
004C549C  72 1E                           jb 0x1404c54bc
004C549E  0F B6 53 21                     movzx edx, byte ptr [rbx + 0x21]
004C54A2  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
004C54A5  48 C1 E2 20                     shl rdx, 0x20
004C54A9  48 0B D0                        or rdx, rax
004C54AC  48 C1 E2 0C                     shl rdx, 0xc
004C54B0  48 81 CA FF 0F 00 00            or rdx, 0xfff
004C54B7  4C 3B C2                        cmp r8, rdx
004C54BA  76 7F                           jbe 0x1404c553b
004C54BC  49 8B C8                        mov rcx, r8
004C54BF  E8 48 0B 03 00                  call 0x1404f600c
004C54C4  C6 40 40 00                     mov byte ptr [rax + 0x40], 0
004C54C8  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
004C54CC  48 8B 58 18                     mov rbx, qword ptr [rax + 0x18]
004C54D0  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
004C54D4  41 F6 C4 01                     test r12b, 1
004C54D8  74 08                           je 0x1404c54e2
004C54DA  41 BD 04 00 00 00               mov r13d, 4
004C54E0  EB 0C                           jmp 0x1404c54ee
004C54E2  44 8B 6B 30                     mov r13d, dword ptr [rbx + 0x30]
004C54E6  41 C1 ED 07                     shr r13d, 7
004C54EA  41 83 E5 1F                     and r13d, 0x1f
004C54EE  45 8B C3                        mov r8d, r11d
004C54F1  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
004C54F6  45 0B C5                        or r8d, r13d
004C54F9  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004C5503  48 8B C8                        mov rcx, rax
004C5506  48 B8 78 FF FF FF 3F 00 00 00   movabs rax, 0x3fffffff78
004C5510  33 D2                           xor edx, edx
004C5512  48 03 C8                        add rcx, rax
004C5515  E8 76 00 E0 FF                  call 0x1402c5590
004C551A  44 8B 73 30                     mov r14d, dword ptr [rbx + 0x30]
004C551E  4C 8B F8                        mov r15, rax
004C5521  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
004C5526  41 C1 EE 0C                     shr r14d, 0xc
004C552A  41 83 E6 7F                     and r14d, 0x7f
004C552E  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004C5533  44 89 74 24 4C                  mov dword ptr [rsp + 0x4c], r14d
004C5538  45 33 D2                        xor r10d, r10d
004C553B  48 85 F6                        test rsi, rsi
004C553E  74 09                           je 0x1404c5549
004C5540  4E 39 14 CE                     cmp qword ptr [rsi + r9*8], r10
004C5544  49 8B F7                        mov rsi, r15
004C5547  75 07                           jne 0x1404c5550
004C5549  48 8B 35 30 B3 B4 FF            mov rsi, qword ptr [rip - 0x4b4cd0]
004C5550  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
004C5555  EB 13                           jmp 0x1404c556a
004C5557  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
004C555C  48 8B 35 1D B3 B4 FF            mov rsi, qword ptr [rip - 0x4b4ce3]
004C5563  48 85 D2                        test rdx, rdx
004C5566  49 0F 45 F7                     cmovne rsi, r15
004C556A  40 F6 C6 01                     test sil, 1
004C556E  74 64                           je 0x1404c55d4
004C5570  4A 8B 14 CA                     mov rdx, qword ptr [rdx + r9*8]
004C5574  48 85 D2                        test rdx, rdx
004C5577  79 44                           jns 0x1404c55bd
004C5579  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
004C5583  45 8B C5                        mov r8d, r13d
004C5586  41 83 E0 F9                     and r8d, 0xfffffff9
004C558A  48 23 D0                        and rdx, rax
004C558D  44 0B 44 24 30                  or r8d, dword ptr [rsp + 0x30]
004C5592  41 83 C8 01                     or r8d, 1
004C5596  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004C55A0  48 8B C8                        mov rcx, rax
004C55A3  48 B8 78 FF FF FF 3F 00 00 00   movabs rax, 0x3fffffff78
004C55AD  48 03 C8                        add rcx, rax
004C55B0  E8 DB FF DF FF                  call 0x1402c5590
004C55B5  48 8B F0                        mov rsi, rax
004C55B8  45 33 D2                        xor r10d, r10d
004C55BB  EB 17                           jmp 0x1404c55d4
004C55BD  48 C1 E2 0C                     shl rdx, 0xc
004C55C1  48 B9 FF 0F 00 00 00 00 F0 FF   movabs rcx, 0xfff0000000000fff
004C55CB  48 33 F2                        xor rsi, rdx
004C55CE  48 23 F1                        and rsi, rcx
004C55D1  48 33 F2                        xor rsi, rdx
004C55D4  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004C55DE  49 BD F8 FF FF FF 7F 00 00 00   movabs r13, 0x7ffffffff8
004C55E8  48 85 DB                        test rbx, rbx
004C55EB  75 19                           jne 0x1404c5606
004C55ED  48 8B CF                        mov rcx, rdi
004C55F0  48 C1 E9 09                     shr rcx, 9
004C55F4  49 23 CD                        and rcx, r13
004C55F7  48 8B C0                        mov rax, rax
004C55FA  48 03 C8                        add rcx, rax
004C55FD  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
004C5601  E9 42 01 00 00                  jmp 0x1404c5748
004C5606  48 8B DF                        mov rbx, rdi
004C5609  48 C1 EB 09                     shr rbx, 9
004C560D  49 23 DD                        and rbx, r13
004C5610  48 8B C0                        mov rax, rax
004C5613  48 03 D8                        add rbx, rax
004C5616  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
004C561A  48 3B C3                        cmp rax, rbx
004C561D  0F 84 25 01 00 00               je 0x1404c5748
004C5623  48 85 C0                        test rax, rax
004C5626  74 0B                           je 0x1404c5633
004C5628  48 8D 4D A0                     lea rcx, [rbp - 0x60]
004C562C  E8 2F 90 02 00                  call 0x1404ee660
004C5631  EB 12                           jmp 0x1404c5645
004C5633  F6 45 B4 04                     test byte ptr [rbp - 0x4c], 4
004C5637  74 0F                           je 0x1404c5648
004C5639  8A 55 50                        mov dl, byte ptr [rbp + 0x50]
004C563C  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
004C5640  E8 4B 80 DB FF                  call 0x14027d690
004C5645  45 33 D2                        xor r10d, r10d
004C5648  83 4D B4 06                     or dword ptr [rbp - 0x4c], 6
004C564C  44 89 54 24 48                  mov dword ptr [rsp + 0x48], r10d
004C5651  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
004C5655  E8 1A 23 1C 00                  call 0x140687974
004C565A  44 8B 4D B4                     mov r9d, dword ptr [rbp - 0x4c]
004C565E  85 C0                           test eax, eax
004C5660  74 07                           je 0x1404c5669
004C5662  41 0F BA E1 00                  bt r9d, 0
004C5667  73 63                           jae 0x1404c56cc
004C5669  41 F6 C4 10                     test r12b, 0x10
004C566D  74 5D                           je 0x1404c56cc
004C566F  4C 8B 5D A0                     mov r11, qword ptr [rbp - 0x60]
004C5673  49 8B CB                        mov rcx, r11
004C5676  E8 25 6A DB FF                  call 0x14027c0a0
004C567B  4C 8B 55 D0                     mov r10, qword ptr [rbp - 0x30]
004C567F  41 0F B6 52 20                  movzx edx, byte ptr [r10 + 0x20]
004C5684  41 8B 4A 18                     mov ecx, dword ptr [r10 + 0x18]
004C5688  48 C1 E2 20                     shl rdx, 0x20
004C568C  48 0B D1                        or rdx, rcx
004C568F  48 C1 E2 0C                     shl rdx, 0xc
004C5693  48 3B C2                        cmp rax, rdx
004C5696  72 34                           jb 0x1404c56cc
004C5698  49 8D 4B 08                     lea rcx, [r11 + 8]
004C569C  E8 FF 69 DB FF                  call 0x14027c0a0
004C56A1  41 0F B6 52 21                  movzx edx, byte ptr [r10 + 0x21]
004C56A6  48 FF C8                        dec rax
004C56A9  41 8B 4A 1C                     mov ecx, dword ptr [r10 + 0x1c]
004C56AD  48 C1 E2 20                     shl rdx, 0x20
004C56B1  48 0B D1                        or rdx, rcx
004C56B4  48 C1 E2 0C                     shl rdx, 0xc
004C56B8  48 81 CA FF 0F 00 00            or rdx, 0xfff
004C56BF  48 3B C2                        cmp rax, rdx
004C56C2  77 08                           ja 0x1404c56cc
004C56C4  41 83 E1 FD                     and r9d, 0xfffffffd
004C56C8  44 89 4D B4                     mov dword ptr [rbp - 0x4c], r9d
004C56CC  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
004C56D0  E8 1B 75 DB FF                  call 0x14027cbf0
004C56D5  83 7D 3C 01                     cmp dword ptr [rbp + 0x3c], 1
004C56D9  88 45 50                        mov byte ptr [rbp + 0x50], al
004C56DC  7C 55                           jl 0x1404c5733
004C56DE  48 8B CF                        mov rcx, rdi
004C56E1  E8 BA 69 DB FF                  call 0x14027c0a0
004C56E6  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
004C56EA  48 8B D0                        mov rdx, rax
004C56ED  41 B8 08 00 00 00               mov r8d, 8
004C56F3  E8 48 0C DB FF                  call 0x140276340
004C56F8  45 33 D2                        xor r10d, r10d
004C56FB  85 C0                           test eax, eax
004C56FD  74 34                           je 0x1404c5733
004C56FF  8D 48 FF                        lea ecx, [rax - 1]
004C5702  3B 4D 3C                        cmp ecx, dword ptr [rbp + 0x3c]
004C5705  74 41                           je 0x1404c5748
004C5707  48 8B D7                        mov rdx, rdi
004C570A  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
004C5714  48 C1 EA 09                     shr rdx, 9
004C5718  49 23 D5                        and rdx, r13
004C571B  49 8B C8                        mov rcx, r8
004C571E  48 03 D1                        add rdx, rcx
004C5721  83 F8 01                        cmp eax, 1
004C5724  0F 85 05 03 00 00               jne 0x1404c5a2f
004C572A  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
004C572E  E8 8D 17 D5 FF                  call 0x140216ec0
004C5733  44 8A 45 50                     mov r8b, byte ptr [rbp + 0x50]
004C5737  45 33 C9                        xor r9d, r9d
004C573A  41 8B D6                        mov edx, r14d
004C573D  48 8B CF                        mov rcx, rdi
004C5740  E8 2B A8 DB FF                  call 0x14027ff70
004C5745  45 33 D2                        xor r10d, r10d
004C5748  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
004C574C  45 8B EA                        mov r13d, r10d
004C574F  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
004C5753  48 85 C0                        test rax, rax
004C5756  45 8B C2                        mov r8d, r10d
004C5759  44 89 54 24 3C                  mov dword ptr [rsp + 0x3c], r10d
004C575E  48 0F 44 C7                     cmove rax, rdi
004C5762  44 89 54 24 38                  mov dword ptr [rsp + 0x38], r10d
004C5767  48 FF C9                        dec rcx
004C576A  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
004C576E  48 8D 0C CF                     lea rcx, [rdi + rcx*8]
004C5772  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
004C5776  B9 01 00 00 00                  mov ecx, 1
004C577B  48 8B 1F                        mov rbx, qword ptr [rdi]
004C577E  40 84 F1                        test cl, sil
004C5781  0F 84 B3 00 00 00               je 0x1404c583a
004C5787  84 D9                           test cl, bl
004C5789  74 28                           je 0x1404c57b3
004C578B  48 3B F3                        cmp rsi, rbx
004C578E  0F 84 28 01 00 00               je 0x1404c58bc
004C5794  8B 45 3C                        mov eax, dword ptr [rbp + 0x3c]
004C5797  F7 D8                           neg eax
004C5799  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
004C579D  C7 44 24 38 40 00 00 00         mov dword ptr [rsp + 0x38], 0x40
004C57A5  45 1B ED                        sbb r13d, r13d
004C57A8  41 F7 DD                        neg r13d
004C57AB  44 03 E9                        add r13d, ecx
004C57AE  E9 09 01 00 00                  jmp 0x1404c58bc
004C57B3  41 BD 05 00 00 00               mov r13d, 5
004C57B9  48 0F BA E3 0B                  bt rbx, 0xb
004C57BE  0F 82 F8 00 00 00               jb 0x1404c58bc
004C57C4  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
004C57C8  48 01 45 A8                     add qword ptr [rbp - 0x58], rax
004C57CC  48 85 DB                        test rbx, rbx
004C57CF  75 08                           jne 0x1404c57d9
004C57D1  01 45 B0                        add dword ptr [rbp - 0x50], eax
004C57D4  E9 E3 00 00 00                  jmp 0x1404c58bc
004C57D9  48 8B 05 A0 84 96 00            mov rax, qword ptr [rip + 0x9684a0]
004C57E0  48 8B FB                        mov rdi, rbx
004C57E3  48 85 C0                        test rax, rax
004C57E6  74 14                           je 0x1404c57fc
004C57E8  F6 C3 10                        test bl, 0x10
004C57EB  75 0B                           jne 0x1404c57f8
004C57ED  48 8B F8                        mov rdi, rax
004C57F0  48 F7 D7                        not rdi
004C57F3  48 23 FB                        and rdi, rbx
004C57F6  EB 04                           jmp 0x1404c57fc
004C57F8  48 83 E7 EF                     and rdi, 0xffffffffffffffef
004C57FC  48 C1 EF 20                     shr rdi, 0x20
004C5800  85 FF                           test edi, edi
004C5802  74 28                           je 0x1404c582c
004C5804  3B 7C 24 48                     cmp edi, dword ptr [rsp + 0x48]
004C5808  75 07                           jne 0x1404c5811
004C580A  44 89 54 24 3C                  mov dword ptr [rsp + 0x3c], r10d
004C580F  EB 1B                           jmp 0x1404c582c
004C5811  8B CF                           mov ecx, edi
004C5813  E8 CC 55 E5 FF                  call 0x14031ade4
004C5818  84 C0                           test al, al
004C581A  74 10                           je 0x1404c582c
004C581C  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
004C5821  48 8D 4D A0                     lea rcx, [rbp - 0x60]
004C5825  E8 F2 42 1C 00                  call 0x140689b1c
004C582A  33 FF                           xor edi, edi
004C582C  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
004C5830  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
004C5835  E9 82 00 00 00                  jmp 0x1404c58bc
004C583A  48 85 DB                        test rbx, rbx
004C583D  74 7D                           je 0x1404c58bc
004C583F  84 D9                           test cl, bl
004C5841  74 56                           je 0x1404c5899
004C5843  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
004C5847  48 29 45 A8                     sub qword ptr [rbp - 0x58], rax
004C584B  29 45 B0                        sub dword ptr [rbp - 0x50], eax
004C584E  8B 45 3C                        mov eax, dword ptr [rbp + 0x3c]
004C5851  F7 D8                           neg eax
004C5853  45 1B ED                        sbb r13d, r13d
004C5856  41 F7 DD                        neg r13d
004C5859  41 83 C5 03                     add r13d, 3
004C585D  4C 39 55 D0                     cmp qword ptr [rbp - 0x30], r10
004C5861  74 2F                           je 0x1404c5892
004C5863  F6 45 B4 02                     test byte ptr [rbp - 0x4c], 2
004C5867  74 09                           je 0x1404c5872
004C5869  44 8B C1                        mov r8d, ecx
004C586C  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
004C5870  EB 20                           jmp 0x1404c5892
004C5872  8B D7                           mov edx, edi
004C5874  C1 EA 03                        shr edx, 3
004C5877  81 E2 FF 01 00 00               and edx, 0x1ff
004C587D  8B CA                           mov ecx, edx
004C587F  83 E2 07                        and edx, 7
004C5882  48 C1 E9 03                     shr rcx, 3
004C5886  48 03 4D F0                     add rcx, qword ptr [rbp - 0x10]
004C588A  0F BE 01                        movsx eax, byte ptr [rcx]
004C588D  0F AB D0                        bts eax, edx
004C5890  88 01                           mov byte ptr [rcx], al
004C5892  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
004C5897  EB 23                           jmp 0x1404c58bc
004C5899  48 0F BA E3 0B                  bt rbx, 0xb
004C589E  73 0A                           jae 0x1404c58aa
004C58A0  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
004C58A4  48 29 45 A8                     sub qword ptr [rbp - 0x58], rax
004C58A8  EB 09                           jmp 0x1404c58b3
004C58AA  4C 39 55 D0                     cmp qword ptr [rbp - 0x30], r10
004C58AE  75 0C                           jne 0x1404c58bc
004C58B0  8B 45 40                        mov eax, dword ptr [rbp + 0x40]
004C58B3  29 45 B0                        sub dword ptr [rbp - 0x50], eax
004C58B6  41 BD 06 00 00 00               mov r13d, 6
004C58BC  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
004C58C0  45 8B CD                        mov r9d, r13d
004C58C3  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
004C58C7  4C 8B C6                        mov r8, rsi
004C58CA  48 8B D7                        mov rdx, rdi
004C58CD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004C58D2  E8 D1 BD 01 00                  call 0x1404e16a8
004C58D7  45 33 D2                        xor r10d, r10d
004C58DA  48 83 CF FF                     or rdi, 0xffffffffffffffff
004C58DE  48 85 DB                        test rbx, rbx
004C58E1  74 4A                           je 0x1404c592d
004C58E3  F6 C3 01                        test bl, 1
004C58E6  74 05                           je 0x1404c58ed
004C58E8  48 8B FB                        mov rdi, rbx
004C58EB  EB 2A                           jmp 0x1404c5917
004C58ED  48 0F BA E3 0B                  bt rbx, 0xb
004C58F2  73 36                           jae 0x1404c592a
004C58F4  48 8B 05 85 83 96 00            mov rax, qword ptr [rip + 0x968385]
004C58FB  48 8B FB                        mov rdi, rbx
004C58FE  48 85 C0                        test rax, rax
004C5901  74 14                           je 0x1404c5917
004C5903  F6 C3 10                        test bl, 0x10
004C5906  75 0B                           jne 0x1404c5913
004C5908  48 8B F8                        mov rdi, rax
004C590B  48 F7 D7                        not rdi
004C590E  48 23 FB                        and rdi, rbx
004C5911  EB 04                           jmp 0x1404c5917
004C5913  48 83 E7 EF                     and rdi, 0xffffffffffffffef
004C5917  48 C1 EF 0C                     shr rdi, 0xc
004C591B  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
004C5925  48 23 F8                        and rdi, rax
004C5928  EB 03                           jmp 0x1404c592d
004C592A  49 8B DA                        mov rbx, r10
004C592D  44 39 54 24 3C                  cmp dword ptr [rsp + 0x3c], r10d
004C5932  74 33                           je 0x1404c5967
004C5934  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
004C5938  8B 74 24 38                     mov esi, dword ptr [rsp + 0x38]
004C593C  48 85 C0                        test rax, rax
004C593F  75 0F                           jne 0x1404c5950
004C5941  8B D6                           mov edx, esi
004C5943  48 8D 4D A0                     lea rcx, [rbp - 0x60]
004C5947  E8 E8 33 1C 00                  call 0x140688d34
004C594C  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
004C5950  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
004C5955  48 8D 4D A0                     lea rcx, [rbp - 0x60]
004C5959  44 8B CE                        mov r9d, esi
004C595C  48 8B D0                        mov rdx, rax
004C595F  E8 88 36 1C 00                  call 0x140688fec
004C5964  45 33 D2                        xor r10d, r10d
004C5967  48 85 DB                        test rbx, rbx
004C596A  0F 84 82 00 00 00               je 0x1404c59f2
004C5970  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
004C5975  41 F6 C4 10                     test r12b, 0x10
004C5979  74 0E                           je 0x1404c5989
004C597B  F0 44 09 14 24                  lock or dword ptr [rsp], r10d
004C5980  8B 05 FA 96 B0 00               mov eax, dword ptr [rip + 0xb096fa]
004C5986  89 41 10                        mov dword ptr [rcx + 0x10], eax
004C5989  41 F6 C4 08                     test r12b, 8
004C598D  74 18                           je 0x1404c59a7
004C598F  4C 8B C9                        mov r9, rcx
004C5992  41 B8 02 00 00 00               mov r8d, 2
004C5998  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
004C599D  48 8B D7                        mov rdx, rdi
004C59A0  E8 B3 27 1C 00                  call 0x140688158
004C59A5  EB 48                           jmp 0x1404c59ef
004C59A7  48 8B 75 90                     mov rsi, qword ptr [rbp - 0x70]
004C59AB  49 8B DA                        mov rbx, r10
004C59AE  48 85 F6                        test rsi, rsi
004C59B1  74 3F                           je 0x1404c59f2
004C59B3  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
004C59B8  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
004C59BD  4C 8B 75 98                     mov r14, qword ptr [rbp - 0x68]
004C59C1  4D 8B CC                        mov r9, r12
004C59C4  41 B8 02 00 00 00               mov r8d, 2
004C59CA  48 8B D7                        mov rdx, rdi
004C59CD  49 8B CF                        mov rcx, r15
004C59D0  E8 83 27 1C 00                  call 0x140688158
004C59D5  49 03 FE                        add rdi, r14
004C59D8  49 03 DE                        add rbx, r14
004C59DB  48 3B DE                        cmp rbx, rsi
004C59DE  72 E1                           jb 0x1404c59c1
004C59E0  44 8B 74 24 4C                  mov r14d, dword ptr [rsp + 0x4c]
004C59E5  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
004C59EA  44 8B 64 24 50                  mov r12d, dword ptr [rsp + 0x50]
004C59EF  45 33 D2                        xor r10d, r10d
004C59F2  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
004C59F7  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
004C59FC  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
004C5A00  49 FF C1                        inc r9
004C5A03  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
004C5A08  48 8D 3C C7                     lea rdi, [rdi + rax*8]
004C5A0C  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
004C5A11  4C 3B 4D 80                     cmp r9, qword ptr [rbp - 0x80]
004C5A15  73 27                           jae 0x1404c5a3e
004C5A17  48 8B 5D D0                     mov rbx, qword ptr [rbp - 0x30]
004C5A1B  44 8B 6C 24 34                  mov r13d, dword ptr [rsp + 0x34]
004C5A20  44 8B 5C 24 30                  mov r11d, dword ptr [rsp + 0x30]
004C5A25  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
004C5A2A  E9 F1 F9 FF FF                  jmp 0x1404c5420
004C5A2F  48 C1 EA 09                     shr rdx, 9
004C5A33  49 23 D5                        and rdx, r13
004C5A36  49 8B C0                        mov rax, r8
004C5A39  48 03 D0                        add rdx, rax
004C5A3C  EB F1                           jmp 0x1404c5a2f
004C5A3E  48 8D 4D A0                     lea rcx, [rbp - 0x60]
004C5A42  E8 19 8C 02 00                  call 0x1404ee660
004C5A47  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
004C5A4B  48 33 CC                        xor rcx, rsp
004C5A4E  E8 ED 6B 1E 00                  call 0x1406ac640
004C5A53  48 8B 9C 24 C0 01 00 00         mov rbx, qword ptr [rsp + 0x1c0]
004C5A5B  48 81 C4 70 01 00 00            add rsp, 0x170
004C5A62  41 5F                           pop r15
004C5A64  41 5E                           pop r14
004C5A66  41 5D                           pop r13
004C5A68  41 5C                           pop r12
004C5A6A  5F                              pop rdi
004C5A6B  5E                              pop rsi
004C5A6C  5D                              pop rbp
004C5A6D  C3                              ret
004C5A6E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWriteAwePtes(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m158;
    unsigned int v_stack_m15C;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m54;
    unsigned __int8 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 9721149)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m128 = a3;
    v_stack_m148 = a7;
    v_stack_m150 = a2;
    a2 = 0;
    v_stack_m168 = a5;
    v_stack_m120 = a4;
    v_stack_m130 = *(unsigned __int64 *)(a1 + 32);
    result = memset(v_stack_m108, a2, 184, a4);
    v_stack_mD0 = a1;
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    v_stack_m60 = *(unsigned __int64 *)(a1 + 32);
    v_stack_m110 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16);
    v_stack_m158 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 8)));
    result = MiGetAweViewPageSize(a1, a2, 184, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16));
    v_r10 = 0;
    a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16);
    if (result != 0) { a1 = result; }
    v_stack_m118 = a1;
    result = MiPageSizeToPteLevel(a1, a2, 184, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16));
    v_stack_m6C = (unsigned int)(result);
    v_r11 = (unsigned int)(0x4000000ULL);
    if (((unsigned int)(result)) < 1) { v_r11 = 0; }
    *(unsigned __int8 *)(a1 + 64) = 0;
    v_stack_m178 = (unsigned int)(v_r11);
    v_stack_mC0 = 512;
    result = v_r10 + 1;
    if (a1 == 16) { result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16); }
    v_stack_m58 = 17;
    v_stack_m68 = result;
    v_stack_mB8 = v_stack_mB0;
    v_stack_m70 = (unsigned int)((unsigned int)(a6));
    if ((((unsigned __int8)((unsigned int)(a6))) & (1)) == 0) goto loc_004C53B7;
    v_stack_mD8 = *(unsigned __int64 *)(a1 + 24);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 48))))) & ((unsigned int)((unsigned int)(0x600000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x600000ULL)))) {
        v_stack_m178 = (unsigned int)(v_r11);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 8)))) & (1)) == 0) goto loc_004C5339;
    v_stack_m174 = 4;
    goto loc_004C5351;
loc_004C5339:
    v_r13 = (unsigned int)((4) >> (7));
    v_r13 = (unsigned int)((v_r13) & (31));
    v_stack_m174 = (unsigned int)(v_r13);
    result = MI_GET_GRAPHICS_PROTECTION_FROM_VAD(*(unsigned __int64 *)(a1 + 24), a2, 184, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16));
    v_stack_m54 = (unsigned int)(result);
loc_004C5351:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) | ((unsigned int)(v_r13)));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16)) + (a1);
    a2 = 0;
    result = MiMakeValidPte(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16));
    v_stack_m140 = result;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 48))) & ((unsigned int)((unsigned int)(0x4200000ULL))));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 48))))) >> (12));
    v_r14 = (unsigned int)((v_r14) & (127));
    v_stack_m15C = (unsigned int)(v_r14);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x4200000ULL)))) {
    }
    result = Feature_Servicing_Mm_AweLazyFlushOptIn__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)(0x4200000ULL), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16));
    v_r10 = 0;
    if ((unsigned int)(result) == 0) goto loc_004C53AC;
    v_rsi = a2;
    if (0 == 1) {
        v_rsi = 0;
        v_stack_m150 = 0;
    }
    goto loc_004C5404;
loc_004C53B7:
    a1 = (unsigned int)(((unsigned int)(v_stack_mF4)) | (4));
    v_stack_m54 = 0;
    v_stack_mF4 = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD8 + 48))) & ((unsigned int)((unsigned int)(0x4200000ULL))));
    v_stack_m140 = 0;
    v_stack_m174 = 24;
    v_stack_m15C = 0;
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m178));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x4200000ULL)))) {
        a1 = (unsigned int)((a1) | (8));
        v_stack_mF4 = (unsigned int)(a1);
    }
    v_stack_mD8 = 0;
loc_004C5404:
    v_stack_m160 = 0;
    v_stack_m138 = 0;
    if (v_stack_m128 <= 0) goto loc_004C5A3E;
loc_004C5420:
    if (v_stack_m120 == 0) goto loc_004C5557;
    v_rdi = (*(unsigned __int64 *)(v_stack_m120 + 0 * 8)) >> (9);
    v_rdi = (v_rdi) & ((unsigned int)(0x4200000ULL));
    v_rdi = (v_rdi) + (v_stack_m120);
    v_stack_m168 = v_rdi;
    if ((unsigned int)((unsigned int)(v_stack_m6C)) == 0) goto loc_004C5487;
loc_004C546B:
    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & ((unsigned int)(0x4200000ULL));
    v_rdi = (v_rdi) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 8)));
    a1 = (unsigned int)(((unsigned int)(v_stack_m6C)) - (1));
    if (condition_is_not_equal) goto loc_004C546B;
    v_stack_m168 = v_rdi;
loc_004C5487:
    a1 = (*(unsigned __int8 *)(0 + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(0 + 24)));
    a1 = (a1) << (12);
    if ((*(unsigned __int64 *)(v_stack_m120 + 0 * 8)) < a1) goto loc_004C54BC;
    a2 = (*(unsigned __int8 *)(0 + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(0 + 28)));
    a2 = (a2) << (12);
    a2 = (a2) | (0xFFFULL);
    if ((*(unsigned __int64 *)(v_stack_m120 + 0 * 8)) <= a2) goto loc_004C553B;
loc_004C54BC:
    result = MiGetAweNode(*(unsigned __int64 *)(v_stack_m120 + 0 * 8), a2, *(unsigned __int64 *)(v_stack_m120 + 0 * 8), 0);
    *(unsigned __int8 *)(result + 64) = 0;
    v_stack_mD0 = result;
    v_stack_mD8 = *(unsigned __int64 *)(result + 24);
    if ((((unsigned __int8)((unsigned int)(v_stack_m158))) & (1)) == 0) goto loc_004C54E2;
    goto loc_004C54EE;
loc_004C54E2:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 48))) >> (7));
    v_r13 = (unsigned int)((v_r13) & (31));
loc_004C54EE:
    v_stack_m174 = (unsigned int)(v_r13);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m178)))) | ((unsigned int)(v_r13)));
    a2 = 0;
    a1 = (result) + (result);
    result = MiMakeValidPte(a1, a2, a3, 0);
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 48))) >> (12));
    v_r14 = (unsigned int)((v_r14) & (127));
    v_stack_m140 = result;
    v_stack_m15C = (unsigned int)(v_r14);
    v_r10 = 0;
loc_004C553B:
    if (v_rsi == 0) goto loc_004C5549;
    v_rsi = result;
    if ((*(unsigned __int64 *)(v_rsi + v_stack_m138 * 8)) == 0) {
        v_rsi = *(unsigned __int64 *)(v_rip - 4934864);
    }
    goto loc_004C556A;
loc_004C5557:
    v_rsi = *(unsigned __int64 *)(v_rip - 4934883);
    if (v_stack_m150 != 0) { v_rsi = result; }
loc_004C556A:
    if ((((unsigned __int8)(v_rsi)) & (1)) == 0) goto loc_004C55D4;
    if (!sign_flag) goto loc_004C55BD;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) & (0xFFFFFFF9ULL));
    a2 = (*(unsigned __int64 *)(v_stack_m150 + v_stack_m138 * 8)) & (result);
    a3 = (unsigned int)((a3) | (v_stack_m178));
    a3 = (unsigned int)((a3) | (1));
    a1 = (result) + (result);
    result = MiMakeValidPte(a1, a2, a3, v_stack_m138);
    v_r10 = 0;
    goto loc_004C55D4;
loc_004C55BD:
    a2 = (a2) << (12);
    v_rsi = (result) ^ (a2);
    v_rsi = (v_rsi) & (a1);
    v_rsi = (v_rsi) ^ (a2);
loc_004C55D4:
    if (*(unsigned __int64 *)(result + 24) != 0) goto loc_004C5606;
    a1 = (v_rdi) >> (9);
    a1 = (a1) & (v_r13);
    a1 = (a1) + (result);
    v_stack_m108 = a1;
    goto loc_004C5748;
loc_004C5606:
    v_rbx = (v_rdi) >> (9);
    v_rbx = (v_rbx) & (v_r13);
    v_rbx = (v_rbx) + (result);
    if (v_stack_m108 == v_rbx) goto loc_004C5748;
    if (v_stack_m108 == 0) goto loc_004C5633;
    result = MiFinishPteChangesInPageTable(v_stack_m108, a2, a3, v_stack_m138);
    goto loc_004C5645;
loc_004C5633:
    if (((v_stack_mF4) & (4)) == 0) goto loc_004C5648;
    result = MiUnlockWorkingSetShared(v_stack_mE0, v_stack_m58, a3, v_stack_m138);
loc_004C5645:
    v_r10 = 0;
loc_004C5648:
    v_stack_m160 = 0;
    v_stack_m108 = v_rbx;
    result = Feature_Servicing_Mm_AweLazyFlushOptIn__private_IsEnabledDeviceUsageNoInline(v_stack_mE0, v_stack_m58, a3, v_stack_m138);
    if ((unsigned int)(result) == 0) goto loc_004C5669;
    if (condition_is_above_or_equal) goto loc_004C56CC;
loc_004C5669:
    if ((((unsigned __int8)((unsigned int)(v_stack_m158))) & (16)) == 0) goto loc_004C56CC;
    result = MiGetLeafVa(v_stack_m108, v_stack_m58, a3, (unsigned int)(v_stack_mF4));
    a2 = (*(unsigned __int8 *)(v_stack_mD8 + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_stack_mD8 + 24)));
    a2 = (a2) << (12);
    if (result < a2) goto loc_004C56CC;
    result = MiGetLeafVa(v_stack_m108 + 8, a2, a3, (unsigned int)(v_stack_mF4));
    result = (result) - 1;
    a2 = (*(unsigned __int8 *)(v_stack_mD8 + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_stack_mD8 + 28)));
    a2 = (a2) << (12);
    a2 = (a2) | (0xFFFULL);
    if (result <= a2) {
        a4 = (unsigned int)(((unsigned int)(v_stack_mF4)) & (0xFFFFFFFDULL));
        v_stack_mF4 = (unsigned int)(a4);
    }
    result = MiLockWorkingSetShared(v_stack_mE0, a2, a3, a4);
    v_stack_m58 = (unsigned __int8)(result);
    if (v_stack_m6C < 1) goto loc_004C5733;
    result = MiGetLeafVa(v_rdi, a2, a3, a4);
    result = MiFastLockLeafPageTable(v_stack_mE0, result, 8, a4);
    v_r10 = 0;
    if ((unsigned int)(result) == 0) goto loc_004C5733;
    if (((unsigned int)(result - 1)) == v_stack_m6C) goto loc_004C5748;
    a2 = (v_rdi) >> (9);
    a2 = (a2) & (v_r13);
    a2 = (a2) + (8);
    if (((unsigned int)(result)) != 1) goto loc_004C5A2F;
    result = MiUnlockPageTable(v_stack_mE0, a2, 8, a4);
loc_004C5733:
    a4 = 0;
    result = MiMakeSystemAddressValid(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m58, a4);
    v_r10 = 0;
loc_004C5748:
    v_stack_m16C = 0;
    result = v_stack_mF0;
    if (v_stack_mF0 == 0) { result = v_rdi; }
    v_stack_m170 = 0;
    a1 = (v_stack_m68) - 1;
    v_stack_mF0 = result;
    v_stack_mE8 = v_rdi + a1 * 8;
    if (((1) & ((unsigned __int8)(v_rsi))) == 0) goto loc_004C583A;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_rdi)))) == 0) goto loc_004C57B3;
    if (v_rsi == (*(unsigned __int64 *)(v_rdi))) goto loc_004C58BC;
    result = (unsigned int)(-((unsigned int)(v_stack_m6C)));
    v_stack_m16C = 1;
    v_stack_m170 = 64;
    v_r13 = (unsigned int)(-(0));
    v_r13 = (unsigned int)((v_r13) + (1));
    goto loc_004C58BC;
loc_004C57B3:
    if (condition_is_below) goto loc_004C58BC;
    if (*(unsigned __int64 *)(v_rdi) != 0) goto loc_004C57D9;
    goto loc_004C58BC;
loc_004C57D9:
    if (*(unsigned __int64 *)(v_rip + 9864352) == 0) goto loc_004C57FC;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (16)) != 0) goto loc_004C57F8;
    v_rdi = ~(*(unsigned __int64 *)(v_rip + 9864352));
    v_rdi = (v_rdi) & (*(unsigned __int64 *)(v_rdi));
    goto loc_004C57FC;
loc_004C57F8:
    v_rdi = (v_rdi) & (-17);
loc_004C57FC:
    v_rdi = (v_rdi) >> (32);
    if ((unsigned int)(v_rdi) == 0) goto loc_004C582C;
    if (((unsigned int)(v_rdi)) != v_stack_m160) goto loc_004C5811;
    v_stack_m16C = 0;
    goto loc_004C582C;
loc_004C5811:
    result = MiCompareTbFlushTimeStamp((unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(v_r14)), 0, a4);
    if ((unsigned __int8)(result) != 0) {
        a2 = v_stack_m168;
        a1 = v_stack_m108;
        result = MiZeroAndFlushAweLazyPtes(a1, a2, 0, a4);
        v_rdi = 0;
    }
    v_stack_m160 = 0;
    goto loc_004C58BC;
loc_004C583A:
    if (*(unsigned __int64 *)(v_rdi) == 0) goto loc_004C58BC;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rdi)))) == 0) goto loc_004C5899;
    result = (unsigned int)(-((unsigned int)(v_stack_m6C)));
    v_r13 = (unsigned int)(-(5));
    v_r13 = (unsigned int)((v_r13) + (3));
    if (v_stack_mD8 == 0) goto loc_004C5892;
    if (((v_stack_mF4) & (2)) == 0) goto loc_004C5872;
    v_stack_m16C = (unsigned int)(a1);
    goto loc_004C5892;
loc_004C5872:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m168))) >> (3));
    a2 = (unsigned int)((a2) & (511));
    a2 = (unsigned int)((a2) & (7));
    a1 = ((unsigned int)((unsigned int)(a2))) >> (3);
    a1 = (a1) + (v_stack_mB8);
    *(unsigned __int8 *)(a1) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a1)));
loc_004C5892:
    v_stack_m170 = (unsigned int)((unsigned int)((unsigned int)(a1)));
    goto loc_004C58BC;
loc_004C5899:
    if (condition_is_above_or_equal) goto loc_004C58AA;
    goto loc_004C58B3;
loc_004C58AA:
    if (v_stack_mD8 != 0) goto loc_004C58BC;
loc_004C58B3:
loc_004C58BC:
    v_stack_m188 = v_stack_m68;
    result = MiWriteAweClusterPte(v_stack_mE0, v_stack_m168, v_rsi, 6);
    v_r10 = 0;
    v_rdi = (v_stack_m168) | (-1);
    if (*(unsigned __int64 *)(v_rdi) == 0) goto loc_004C592D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (1)) == 0) goto loc_004C58ED;
    goto loc_004C5917;
loc_004C58ED:
    if (condition_is_above_or_equal) goto loc_004C592A;
    if (*(unsigned __int64 *)(v_rip + 9864069) == 0) goto loc_004C5917;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (16)) != 0) goto loc_004C5913;
    v_rdi = ~(*(unsigned __int64 *)(v_rip + 9864069));
    v_rdi = (v_rdi) & (*(unsigned __int64 *)(v_rdi));
    goto loc_004C5917;
loc_004C5913:
    v_rdi = (v_rdi) & (-17);
loc_004C5917:
    v_rdi = (v_rdi) >> (12);
    v_rdi = (v_rdi) & (*(unsigned __int64 *)(v_rip + 9864069));
    goto loc_004C592D;
loc_004C592A:
loc_004C592D:
    if (v_stack_m16C == 0) goto loc_004C5967;
    result = v_stack_mC8;
    if (v_stack_mC8 == 0) {
        a2 = (unsigned int)((unsigned int)(v_stack_m170));
        a1 = v_stack_m108;
        result = MiGetAweFlushList(a1, a2, v_rsi, 6);
        v_stack_mC8 = result;
    }
    result = MiInsertAweFlushList(v_stack_m108, result, v_stack_m168, (unsigned int)((unsigned int)((unsigned int)(v_stack_m170))));
    v_r10 = 0;
loc_004C5967:
    if (0 == 0) goto loc_004C59F2;
    if ((((unsigned __int8)((unsigned int)(v_stack_m158))) & (16)) != 0) {
        result = *(unsigned int *)(v_rip + 11572986);
        *(unsigned int *)(v_stack_m148 + 16) = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_m158))) & (8)) == 0) goto loc_004C59A7;
    result = MiDecrementAweMapCount(v_stack_m130, v_rdi, 2, v_stack_m148);
    goto loc_004C59EF;
loc_004C59A7:
    if (v_stack_m118 == 0) goto loc_004C59F2;
loc_004C59C1:
    result = MiDecrementAweMapCount(v_stack_m130, v_rdi, 2, v_stack_m148);
    v_rdi = (v_rdi) + (v_stack_m110);
    v_rbx = (0) + (v_stack_m110);
    if (v_rbx < v_stack_m118) goto loc_004C59C1;
loc_004C59EF:
    v_r10 = 0;
loc_004C59F2:
    a4 = (v_stack_m138) + 1;
    v_stack_m138 = a4;
    v_stack_m168 = v_stack_m168 + v_stack_m68 * 8;
    if (a4 >= v_stack_m128) goto loc_004C5A3E;
    goto loc_004C5420;
loc_004C5A2F:
    a2 = (v_rdi) >> (9);
    a2 = (a2) & ((unsigned int)(v_stack_m174));
    a2 = (a2) + (2);
    goto loc_004C5A2F;
loc_004C5A3E:
    result = MiFinishPteChangesInPageTable(v_stack_m108, a2, 2, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 2, a4);
    v_rsp = (v_rsp) + (368);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiWriteAwePtes(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m158;
    uint32_t v_stack_m15C;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint64_t v_stack_m188;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m48;
    uint32_t v_stack_m54;
    uint8_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x94553D)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m128 = Arg3;
    v_stack_m148 = Arg7;
    v_stack_m150 = Arg2;
    Arg2 = 0;
    v_stack_m168 = Arg5;
    v_stack_m120 = Arg4;
    v_stack_m130 = *(uint64_t *)(arg1 + 0x20);
    result = memset(v_stack_m108, Arg2, 184, Arg4);
    v_stack_mD0 = Arg1;
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    v_stack_m60 = *(uint64_t *)(arg1 + 0x20);
    v_stack_m110 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10);
    v_stack_m158 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)));
    result = MiGetAweViewPageSize(Arg1, Arg2, 184, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10));
    local_r10 = 0;
    Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10);
    if (result != 0) { Arg1 = result; }
    v_stack_m118 = Arg1;
    result = MiPageSizeToPteLevel(Arg1, Arg2, 184, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10));
    v_stack_m6C = (uint32_t)(result);
    local_r11 = (uint32_t)(0x4000000ULL);
    if (((uint32_t)(result)) < 1) { local_r11 = 0; }
    *(uint8_t *)(arg1 + 0x40) = 0;
    v_stack_m178 = (uint32_t)(local_r11);
    v_stack_mC0 = 512;
    result = local_r10 + 1;
    if (Arg1 == 16) { result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10); }
    v_stack_m58 = 17;
    v_stack_m68 = result;
    v_stack_mB8 = v_stack_mB0;
    v_stack_m70 = (uint32_t)((uint32_t)(Arg6));
    if ((((uint8_t)((uint32_t)(Arg6))) & (1)) == 0) goto loc_004C53B7;
    v_stack_mD8 = *(uint64_t *)(arg1 + 0x18);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30))))) & ((uint32_t)((uint32_t)(0x600000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x600000ULL)))) {
        v_stack_m178 = (uint32_t)(local_r11);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)))) & (1)) == 0) goto loc_004C5339;
    v_stack_m174 = 4;
    goto loc_004C5351;
loc_004C5339:
    local_r13 = (uint32_t)((4) >> (7));
    local_r13 = (uint32_t)((local_r13) & (31));
    v_stack_m174 = (uint32_t)(local_r13);
    result = MI_GET_GRAPHICS_PROTECTION_FROM_VAD(*(uint64_t *)(arg1 + 0x18), Arg2, 184, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10));
    v_stack_m54 = (uint32_t)(result);
loc_004C5351:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) | ((uint32_t)(local_r13)));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10)) + (Arg1);
    Arg2 = 0;
    result = MiMakeValidPte(Arg1, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10));
    v_stack_m140 = result;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30))) & ((uint32_t)((uint32_t)(0x4200000ULL))));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x30))))) >> (12));
    local_r14 = (uint32_t)((local_r14) & (127));
    v_stack_m15C = (uint32_t)(local_r14);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x4200000ULL)))) {
    }
    result = Feature_Servicing_Mm_AweLazyFlushOptIn__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)(0x4200000ULL), Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10));
    local_r10 = 0;
    if ((uint32_t)(result) == 0) goto loc_004C53AC;
    local_rsi = Arg2;
    if (0 == 1) {
        local_rsi = 0;
        v_stack_m150 = 0;
    }
    goto loc_004C5404;
loc_004C53B7:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mF4)) | (4));
    v_stack_m54 = 0;
    v_stack_mF4 = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD8 + 0x30))) & ((uint32_t)((uint32_t)(0x4200000ULL))));
    v_stack_m140 = 0;
    v_stack_m174 = 24;
    v_stack_m15C = 0;
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m178));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x4200000ULL)))) {
        Arg1 = (uint32_t)((Arg1) | (8));
        v_stack_mF4 = (uint32_t)(Arg1);
    }
    v_stack_mD8 = 0;
loc_004C5404:
    v_stack_m160 = 0;
    v_stack_m138 = 0;
    if (v_stack_m128 <= 0) goto loc_004C5A3E;
loc_004C5420:
    if (v_stack_m120 == 0) goto loc_004C5557;
    local_rdi = (*(uint64_t *)(v_stack_m120 + 0x0 * 8)) >> (9);
    local_rdi = (local_rdi) & ((uint32_t)(0x4200000ULL));
    local_rdi = (local_rdi) + (v_stack_m120);
    v_stack_m168 = local_rdi;
    if ((uint32_t)((uint32_t)(v_stack_m6C)) == 0) goto loc_004C5487;
loc_004C546B:
    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & ((uint32_t)(0x4200000ULL));
    local_rdi = (local_rdi) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m6C)) - (1));
    if (condition_is_not_equal) goto loc_004C546B;
    v_stack_m168 = local_rdi;
loc_004C5487:
    Arg1 = (*(uint8_t *)(0 + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(0 + 0x18)));
    Arg1 = (Arg1) << (12);
    if ((*(uint64_t *)(v_stack_m120 + 0x0 * 8)) < Arg1) goto loc_004C54BC;
    Arg2 = (*(uint8_t *)(0 + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(0 + 0x1C)));
    Arg2 = (Arg2) << (12);
    Arg2 = (Arg2) | (0xFFFULL);
    if ((*(uint64_t *)(v_stack_m120 + 0x0 * 8)) <= Arg2) goto loc_004C553B;
loc_004C54BC:
    result = MiGetAweNode(*(uint64_t *)(v_stack_m120 + 0x0 * 8), Arg2, *(uint64_t *)(v_stack_m120 + 0x0 * 8), 0);
    *(uint8_t *)(result + 0x40) = 0;
    v_stack_mD0 = result;
    v_stack_mD8 = *(uint64_t *)(result + 0x18);
    if ((((uint8_t)((uint32_t)(v_stack_m158))) & (1)) == 0) goto loc_004C54E2;
    goto loc_004C54EE;
loc_004C54E2:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x30))) >> (7));
    local_r13 = (uint32_t)((local_r13) & (31));
loc_004C54EE:
    v_stack_m174 = (uint32_t)(local_r13);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m178)))) | ((uint32_t)(local_r13)));
    Arg2 = 0;
    Arg1 = (result) + (result);
    result = MiMakeValidPte(Arg1, Arg2, Arg3, 0);
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x30))) >> (12));
    local_r14 = (uint32_t)((local_r14) & (127));
    v_stack_m140 = result;
    v_stack_m15C = (uint32_t)(local_r14);
    local_r10 = 0;
loc_004C553B:
    if (local_rsi == 0) goto loc_004C5549;
    local_rsi = result;
    if ((*(uint64_t *)(local_rsi + v_stack_m138 * 8)) == 0) {
        local_rsi = *(uint64_t *)(v_rip - 0x4B4CD0);
    }
    goto loc_004C556A;
loc_004C5557:
    local_rsi = *(uint64_t *)(v_rip - 0x4B4CE3);
    if (v_stack_m150 != 0) { local_rsi = result; }
loc_004C556A:
    if ((((uint8_t)(local_rsi)) & (1)) == 0) goto loc_004C55D4;
    if (!sign_flag) goto loc_004C55BD;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) & (0xFFFFFFF9ULL));
    Arg2 = (*(uint64_t *)(v_stack_m150 + v_stack_m138 * 8)) & (result);
    Arg3 = (uint32_t)((Arg3) | (v_stack_m178));
    Arg3 = (uint32_t)((Arg3) | (1));
    Arg1 = (result) + (result);
    result = MiMakeValidPte(Arg1, Arg2, Arg3, v_stack_m138);
    local_r10 = 0;
    goto loc_004C55D4;
loc_004C55BD:
    Arg2 = (Arg2) << (12);
    local_rsi = (result) ^ (Arg2);
    local_rsi = (local_rsi) & (Arg1);
    local_rsi = (local_rsi) ^ (Arg2);
loc_004C55D4:
    if (*(uint64_t *)(result + 0x18) != 0) goto loc_004C5606;
    Arg1 = (local_rdi) >> (9);
    Arg1 = (Arg1) & (local_r13);
    Arg1 = (Arg1) + (result);
    v_stack_m108 = Arg1;
    goto loc_004C5748;
loc_004C5606:
    local_rbx = (local_rdi) >> (9);
    local_rbx = (local_rbx) & (local_r13);
    local_rbx = (local_rbx) + (result);
    if (v_stack_m108 == local_rbx) goto loc_004C5748;
    if (v_stack_m108 == 0) goto loc_004C5633;
    result = MiFinishPteChangesInPageTable(v_stack_m108, Arg2, Arg3, v_stack_m138);
    goto loc_004C5645;
loc_004C5633:
    if (((v_stack_mF4) & (4)) == 0) goto loc_004C5648;
    result = MiUnlockWorkingSetShared(v_stack_mE0, v_stack_m58, Arg3, v_stack_m138);
loc_004C5645:
    local_r10 = 0;
loc_004C5648:
    v_stack_m160 = 0;
    v_stack_m108 = local_rbx;
    result = Feature_Servicing_Mm_AweLazyFlushOptIn__private_IsEnabledDeviceUsageNoInline(v_stack_mE0, v_stack_m58, Arg3, v_stack_m138);
    if ((uint32_t)(result) == 0) goto loc_004C5669;
    if (condition_is_above_or_equal) goto loc_004C56CC;
loc_004C5669:
    if ((((uint8_t)((uint32_t)(v_stack_m158))) & (16)) == 0) goto loc_004C56CC;
    result = MiGetLeafVa(v_stack_m108, v_stack_m58, Arg3, (uint32_t)(v_stack_mF4));
    Arg2 = (*(uint8_t *)(v_stack_mD8 + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(v_stack_mD8 + 0x18)));
    Arg2 = (Arg2) << (12);
    if (result < Arg2) goto loc_004C56CC;
    result = MiGetLeafVa(v_stack_m108 + 8, Arg2, Arg3, (uint32_t)(v_stack_mF4));
    result = (result) - 1;
    Arg2 = (*(uint8_t *)(v_stack_mD8 + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(v_stack_mD8 + 0x1C)));
    Arg2 = (Arg2) << (12);
    Arg2 = (Arg2) | (0xFFFULL);
    if (result <= Arg2) {
        Arg4 = (uint32_t)(((uint32_t)(v_stack_mF4)) & (0xFFFFFFFDULL));
        v_stack_mF4 = (uint32_t)(Arg4);
    }
    result = MiLockWorkingSetShared(v_stack_mE0, Arg2, Arg3, Arg4);
    v_stack_m58 = (uint8_t)(result);
    if (v_stack_m6C < 1) goto loc_004C5733;
    result = MiGetLeafVa(local_rdi, Arg2, Arg3, Arg4);
    result = MiFastLockLeafPageTable(v_stack_mE0, result, 8, Arg4);
    local_r10 = 0;
    if ((uint32_t)(result) == 0) goto loc_004C5733;
    if (((uint32_t)(result - 1)) == v_stack_m6C) goto loc_004C5748;
    Arg2 = (local_rdi) >> (9);
    Arg2 = (Arg2) & (local_r13);
    Arg2 = (Arg2) + (8);
    if (((uint32_t)(result)) != 1) goto loc_004C5A2F;
    result = MiUnlockPageTable(v_stack_mE0, Arg2, 8, Arg4);
loc_004C5733:
    Arg4 = 0;
    result = MiMakeSystemAddressValid(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m58, Arg4);
    local_r10 = 0;
loc_004C5748:
    v_stack_m16C = 0;
    result = v_stack_mF0;
    if (v_stack_mF0 == 0) { result = local_rdi; }
    v_stack_m170 = 0;
    Arg1 = (v_stack_m68) - 1;
    v_stack_mF0 = result;
    v_stack_mE8 = local_rdi + Arg1 * 8;
    if (((1) & ((uint8_t)(local_rsi))) == 0) goto loc_004C583A;
    if (((1) & ((uint8_t)(*(uint64_t *)(local_rdi)))) == 0) goto loc_004C57B3;
    if (local_rsi == (*(uint64_t *)(local_rdi))) goto loc_004C58BC;
    result = (uint32_t)(-((uint32_t)(v_stack_m6C)));
    v_stack_m16C = 1;
    v_stack_m170 = 64;
    local_r13 = (uint32_t)(-(0));
    local_r13 = (uint32_t)((local_r13) + (1));
    goto loc_004C58BC;
loc_004C57B3:
    if (condition_is_below) goto loc_004C58BC;
    if (*(uint64_t *)(local_rdi) != 0) goto loc_004C57D9;
    goto loc_004C58BC;
loc_004C57D9:
    if (*(uint64_t *)(v_rip + 0x9684A0) == 0) goto loc_004C57FC;
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (16)) != 0) goto loc_004C57F8;
    local_rdi = ~(*(uint64_t *)(v_rip + 0x9684A0));
    local_rdi = (local_rdi) & (*(uint64_t *)(local_rdi));
    goto loc_004C57FC;
loc_004C57F8:
    local_rdi = (local_rdi) & (-17);
loc_004C57FC:
    local_rdi = (local_rdi) >> (32);
    if ((uint32_t)(local_rdi) == 0) goto loc_004C582C;
    if (((uint32_t)(local_rdi)) != v_stack_m160) goto loc_004C5811;
    v_stack_m16C = 0;
    goto loc_004C582C;
loc_004C5811:
    result = MiCompareTbFlushTimeStamp((uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(local_r14)), 0, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg2 = v_stack_m168;
        Arg1 = v_stack_m108;
        result = MiZeroAndFlushAweLazyPtes(Arg1, Arg2, 0, Arg4);
        local_rdi = 0;
    }
    v_stack_m160 = 0;
    goto loc_004C58BC;
loc_004C583A:
    if (*(uint64_t *)(local_rdi) == 0) goto loc_004C58BC;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(*(uint64_t *)(local_rdi)))) == 0) goto loc_004C5899;
    result = (uint32_t)(-((uint32_t)(v_stack_m6C)));
    local_r13 = (uint32_t)(-(5));
    local_r13 = (uint32_t)((local_r13) + (3));
    if (v_stack_mD8 == 0) goto loc_004C5892;
    if (((v_stack_mF4) & (2)) == 0) goto loc_004C5872;
    v_stack_m16C = (uint32_t)(Arg1);
    goto loc_004C5892;
loc_004C5872:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m168))) >> (3));
    Arg2 = (uint32_t)((Arg2) & (511));
    Arg2 = (uint32_t)((Arg2) & (7));
    Arg1 = ((uint32_t)((uint32_t)(Arg2))) >> (3);
    Arg1 = (Arg1) + (v_stack_mB8);
    *(uint8_t *)(arg1) = (uint8_t)((int8_t)(*(uint8_t *)(arg1)));
loc_004C5892:
    v_stack_m170 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
    goto loc_004C58BC;
loc_004C5899:
    if (condition_is_above_or_equal) goto loc_004C58AA;
    goto loc_004C58B3;
loc_004C58AA:
    if (v_stack_mD8 != 0) goto loc_004C58BC;
loc_004C58B3:
loc_004C58BC:
    v_stack_m188 = v_stack_m68;
    result = MiWriteAweClusterPte(v_stack_mE0, v_stack_m168, local_rsi, 6);
    local_r10 = 0;
    local_rdi = (v_stack_m168) | (-1);
    if (*(uint64_t *)(local_rdi) == 0) goto loc_004C592D;
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (1)) == 0) goto loc_004C58ED;
    goto loc_004C5917;
loc_004C58ED:
    if (condition_is_above_or_equal) goto loc_004C592A;
    if (*(uint64_t *)(v_rip + 0x968385) == 0) goto loc_004C5917;
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (16)) != 0) goto loc_004C5913;
    local_rdi = ~(*(uint64_t *)(v_rip + 0x968385));
    local_rdi = (local_rdi) & (*(uint64_t *)(local_rdi));
    goto loc_004C5917;
loc_004C5913:
    local_rdi = (local_rdi) & (-17);
loc_004C5917:
    local_rdi = (local_rdi) >> (12);
    local_rdi = (local_rdi) & (*(uint64_t *)(v_rip + 0x968385));
    goto loc_004C592D;
loc_004C592A:
loc_004C592D:
    if (v_stack_m16C == 0) goto loc_004C5967;
    result = v_stack_mC8;
    if (v_stack_mC8 == 0) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_m170));
        Arg1 = v_stack_m108;
        result = MiGetAweFlushList(Arg1, Arg2, local_rsi, 6);
        v_stack_mC8 = result;
    }
    result = MiInsertAweFlushList(v_stack_m108, result, v_stack_m168, (uint32_t)((uint32_t)((uint32_t)(v_stack_m170))));
    local_r10 = 0;
loc_004C5967:
    if (0 == 0) goto loc_004C59F2;
    if ((((uint8_t)((uint32_t)(v_stack_m158))) & (16)) != 0) {
        result = *(uint32_t *)(v_rip + 0xB096FA);
        *(uint32_t *)(v_stack_m148 + 0x10) = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(v_stack_m158))) & (8)) == 0) goto loc_004C59A7;
    result = MiDecrementAweMapCount(v_stack_m130, local_rdi, 2, v_stack_m148);
    goto loc_004C59EF;
loc_004C59A7:
    if (v_stack_m118 == 0) goto loc_004C59F2;
loc_004C59C1:
    result = MiDecrementAweMapCount(v_stack_m130, local_rdi, 2, v_stack_m148);
    local_rdi = (local_rdi) + (v_stack_m110);
    local_rbx = (0) + (v_stack_m110);
    if (local_rbx < v_stack_m118) goto loc_004C59C1;
loc_004C59EF:
    local_r10 = 0;
loc_004C59F2:
    Arg4 = (v_stack_m138) + 1;
    v_stack_m138 = Arg4;
    v_stack_m168 = v_stack_m168 + v_stack_m68 * 8;
    if (Arg4 >= v_stack_m128) goto loc_004C5A3E;
    goto loc_004C5420;
loc_004C5A2F:
    Arg2 = (local_rdi) >> (9);
    Arg2 = (Arg2) & ((uint32_t)(v_stack_m174));
    Arg2 = (Arg2) + (2);
    goto loc_004C5A2F;
loc_004C5A3E:
    result = MiFinishPteChangesInPageTable(v_stack_m108, Arg2, 2, Arg4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 2, Arg4);
    local_rsp = (local_rsp) + (368);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x40` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C51E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
