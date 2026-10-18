# MiSwitchToTransition

- RVA: `0x004C0F5C`–`0x004C171B` (길이 `1,983` bytes)
- VA: `0x00000001404C0F5C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC7D8`
- 디코드: `483`개 명령, `1,983/1,983` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **35**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x004C0FB6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C0FDC` → [MiGetEffectivePagePriorityThread](../36/MiGetEffectivePagePriorityThread_function_003626E0.md) (function, `0x003626E0`)
- `0x004C0FE8` → [MiGetReadyInPageBlock](../../page/AB/MiGetReadyInPageBlock_function_00ABB398.md) (function, `0x00ABB398`)
- `0x004C1049` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x004C109B` → [MiObtainFaultCharges](../28/MiObtainFaultCharges_function_0028AEB0.md) (function, `0x0028AEB0`)
- `0x004C10F3` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x004C110A` → [MiWaitForFreePage](../2A/MiWaitForFreePage_function_002A3324.md) (function, `0x002A3324`)
- `0x004C1133` → [MiPageAttributeBatchChangeNeeded](../29/MiPageAttributeBatchChangeNeeded_function_0029FAD0.md) (function, `0x0029FAD0`)
- `0x004C1141` → [MiMakeLinkedListPte](../2C/MiMakeLinkedListPte_function_002C98C0.md) (function, `0x002C98C0`)
- `0x004C116F` → [MiReturnFaultCharges](../36/MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)
- `0x004C118D` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x004C11A3` → [MiChangePageAttributeBatch](../2A/MiChangePageAttributeBatch_function_002A06E0.md) (function, `0x002A06E0`)
- `0x004C11BD` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x004C122A` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004C1259` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x004C126C` → [MiUnlockOpportunisticPagesInPageTable](../2A/MiUnlockOpportunisticPagesInPageTable_function_002AA88C.md) (function, `0x002AA88C`)
- `0x004C1274` → [MiGetContainingPageTable](../34/MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x004C128A` → [MiUnlockOpportunisticPagesInPageTable](../2A/MiUnlockOpportunisticPagesInPageTable_function_002AA88C.md) (function, `0x002AA88C`)
- `0x004C1396` → [MiCaptureWriteWatchDirtyBit](../46/MiCaptureWriteWatchDirtyBit_function_00465224.md) (function, `0x00465224`)
- `0x004C13ED` → [MiUpdateProtectionMask](../28/MiUpdateProtectionMask_function_002845DC.md) (function, `0x002845DC`)
- `0x004C13F8` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x004C1443` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x004C1467` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x004C1472` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004C14CC` → [MiAddLockedPageCharge](../28/MiAddLockedPageCharge_function_0028B550.md) (function, `0x0028B550`)
- `0x004C152F` → [ExAcquireRundownProtectionCacheAware](../23/ExAcquireRundownProtectionCacheAware_function_0023D110.md) (function, `0x0023D110`)
- `0x004C1551` → [MiReturnResident](../28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x004C1561` → [MiMakeTransitionPte](../36/MiMakeTransitionPte_function_00363F70.md) (function, `0x00363F70`)
- `0x004C15A5` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C15C0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C15E0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C15F5` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004C1601` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x004C1611` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x004C162B` → [MiReturnFaultCharges](../36/MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)
- `0x004C1679` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x004C1693` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x004C169C` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x004C16E9` → [MiAddMdlTracker](../49/MiAddMdlTracker_function_0049A240.md) (function, `0x0049A240`)
- `0x004C16FA` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiReplaceRotateWithDemandZero](../../page/A7/MiReplaceRotateWithDemandZero_function_00A7C010.md) at `0x00A7C17F`

### Static image references
- `0x004C0F7B` → RVA `0x00E0A740` (`.data`; read)
- `0x004C1080` → RVA `0x00E30088` (`.data`; read)
- `0x004C10CA` → RVA `0x00E2DCC0` (`.data`; read)
- `0x004C12EE` → RVA `0x00E2DCE0` (`.data`; read)
- `0x004C1455` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x004C145D` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x004C16D2` → RVA `0x00FC6BBC` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004C0FE8` → [MiGetReadyInPageBlock](../../page/AB/MiGetReadyInPageBlock_function_00ABB398.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C0F5C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004C0F61  55                              push rbp
004C0F62  56                              push rsi
004C0F63  57                              push rdi
004C0F64  41 54                           push r12
004C0F66  41 55                           push r13
004C0F68  41 56                           push r14
004C0F6A  41 57                           push r15
004C0F6C  48 8D AC 24 40 FF FF FF         lea rbp, [rsp - 0xc0]
004C0F74  48 81 EC C0 01 00 00            sub rsp, 0x1c0
004C0F7B  48 8B 05 BE 97 94 00            mov rax, qword ptr [rip + 0x9497be]
004C0F82  48 33 C4                        xor rax, rsp
004C0F85  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
004C0F8C  45 8B F8                        mov r15d, r8d
004C0F8F  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
004C0F94  48 8B DA                        mov rbx, rdx
004C0F97  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
004C0F9B  4C 8B F1                        mov r14, rcx
004C0F9E  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
004C0FA3  0F 57 C0                        xorps xmm0, xmm0
004C0FA6  48 8D 4D E0                     lea rcx, [rbp - 0x20]
004C0FAA  33 D2                           xor edx, edx
004C0FAC  41 B8 C8 00 00 00               mov r8d, 0xc8
004C0FB2  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
004C0FB6  E8 85 5C 20 00                  call 0x1406c6c40
004C0FBB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004C0FC4  48 83 64 24 70 00               and qword ptr [rsp + 0x70], 0
004C0FCA  48 8B C8                        mov rcx, rax
004C0FCD  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
004C0FD1  48 8B B0 B8 00 00 00            mov rsi, qword ptr [rax + 0xb8]
004C0FD8  48 89 75 90                     mov qword ptr [rbp - 0x70], rsi
004C0FDC  E8 FF 16 EA FF                  call 0x1403626e0
004C0FE1  48 8B CB                        mov rcx, rbx
004C0FE4  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
004C0FE8  E8 AB A3 5F 00                  call 0x140abb398
004C0FED  41 8B 5E 28                     mov ebx, dword ptr [r14 + 0x28]
004C0FF1  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
004C0FF5  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
004C0FF9  48 8B F8                        mov rdi, rax
004C0FFC  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
004C1000  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
004C100A  48 C1 EF 09                     shr rdi, 9
004C100E  48 23 F8                        and rdi, rax
004C1011  48 C1 EB 0C                     shr rbx, 0xc
004C1015  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004C101F  48 8B C8                        mov rcx, rax
004C1022  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
004C1027  48 8D 86 00 04 00 00            lea rax, [rsi + 0x400]
004C102E  45 33 C0                        xor r8d, r8d
004C1031  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
004C1036  48 03 F9                        add rdi, rcx
004C1039  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004C103E  4C 8D 4D A0                     lea r9, [rbp - 0x60]
004C1042  48 8B C8                        mov rcx, rax
004C1045  41 8D 50 03                     lea edx, [r8 + 3]
004C1049  E8 C2 F3 E5 FF                  call 0x140320410
004C104E  8B 45 A8                        mov eax, dword ptr [rbp - 0x58]
004C1051  45 8B CF                        mov r9d, r15d
004C1054  0F B7 8E AE 04 00 00            movzx ecx, word ptr [rsi + 0x4ae]
004C105B  25 FF FF F3 FF                  and eax, 0xfff3ffff
004C1060  41 83 E1 03                     and r9d, 3
004C1064  45 33 FF                        xor r15d, r15d
004C1067  41 C1 E1 12                     shl r9d, 0x12
004C106B  48 8B D3                        mov rdx, rbx
004C106E  44 0B C8                        or r9d, eax
004C1071  48 B8 FF FF FF FF 7F 00 00 00   movabs rax, 0x7fffffffff
004C107B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004C1080  48 8B 05 01 F0 96 00            mov rax, qword ptr [rip + 0x96f001]
004C1087  45 8D 47 02                     lea r8d, [r15 + 2]
004C108B  44 89 4D A8                     mov dword ptr [rbp - 0x58], r9d
004C108F  4C 8B 2C C8                     mov r13, qword ptr [rax + rcx*8]
004C1093  49 8B CD                        mov rcx, r13
004C1096  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
004C109B  E8 10 9E DC FF                  call 0x14028aeb0
004C10A0  33 F6                           xor esi, esi
004C10A2  4C 8B E0                        mov r12, rax
004C10A5  48 83 CB FF                     or rbx, 0xffffffffffffffff
004C10A9  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
004C10AE  BA 01 00 00 00                  mov edx, 1
004C10B3  49 3B F4                        cmp rsi, r12
004C10B6  0F 84 BB 00 00 00               je 0x1404c1177
004C10BC  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
004C10C0  8B C2                           mov eax, edx
004C10C2  F0 0F C1 01                     lock xadd dword ptr [rcx], eax
004C10C6  4C 8B 45 A8                     mov r8, qword ptr [rbp - 0x58]
004C10CA  4C 8D 0D EF CB 96 00            lea r9, [rip + 0x96cbef]
004C10D1  33 D2                           xor edx, edx
004C10D3  49 8B C8                        mov rcx, r8
004C10D6  48 C1 E9 10                     shr rcx, 0x10
004C10DA  83 E1 03                        and ecx, 3
004C10DD  41 F7 34 89                     div dword ptr [r9 + rcx*4]
004C10E1  49 8B CD                        mov rcx, r13
004C10E4  41 33 D0                        xor edx, r8d
004C10E7  0F B6 D2                        movzx edx, dl
004C10EA  41 33 D0                        xor edx, r8d
004C10ED  41 B8 08 00 00 00               mov r8d, 8
004C10F3  E8 C8 73 DC FF                  call 0x1402884c0
004C10F8  4C 8B F0                        mov r14, rax
004C10FB  48 3B C3                        cmp rax, rbx
004C10FE  75 11                           jne 0x1404c1111
004C1100  49 8B CD                        mov rcx, r13
004C1103  48 85 F6                        test rsi, rsi
004C1106  75 5E                           jne 0x1404c1166
004C1108  33 D2                           xor edx, edx
004C110A  E8 15 22 DE FF                  call 0x1402a3324
004C110F  EB 9D                           jmp 0x1404c10ae
004C1111  48 8D 1C 40                     lea rbx, [rax + rax*2]
004C1115  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004C111F  48 C1 E3 04                     shl rbx, 4
004C1123  48 8B C0                        mov rax, rax
004C1126  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
004C112A  48 03 D8                        add rbx, rax
004C112D  48 8B CB                        mov rcx, rbx
004C1130  45 33 C0                        xor r8d, r8d
004C1133  E8 98 E9 DD FF                  call 0x14029fad0
004C1138  85 C0                           test eax, eax
004C113A  74 13                           je 0x1404c114f
004C113C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004C1141  E8 7A 87 E0 FF                  call 0x1402c98c0
004C1146  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
004C114A  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
004C114F  4C 89 3B                        mov qword ptr [rbx], r15
004C1152  BA 01 00 00 00                  mov edx, 1
004C1157  48 03 F2                        add rsi, rdx
004C115A  4C 8B FB                        mov r15, rbx
004C115D  48 83 CB FF                     or rbx, 0xffffffffffffffff
004C1161  E9 4D FF FF FF                  jmp 0x1404c10b3
004C1166  4C 2B E6                        sub r12, rsi
004C1169  45 33 C0                        xor r8d, r8d
004C116C  49 8B D4                        mov rdx, r12
004C116F  E8 B4 C7 EA FF                  call 0x14036d928
004C1174  4C 8B E6                        mov r12, rsi
004C1177  48 B8 FF FF FF FF 7F 00 00 00   movabs rax, 0x7fffffffff
004C1181  48 39 44 24 48                  cmp qword ptr [rsp + 0x48], rax
004C1186  74 20                           je 0x1404c11a8
004C1188  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
004C118D  E8 0A 98 DC FF                  call 0x14028a99c
004C1192  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
004C1196  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
004C119B  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
004C11A0  45 33 C9                        xor r9d, r9d
004C11A3  E8 38 F5 DD FF                  call 0x1402a06e0
004C11A8  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
004C11AD  4A 8D 1C E7                     lea rbx, [rdi + r12*8]
004C11B1  49 8B CE                        mov rcx, r14
004C11B4  48 89 5D 88                     mov qword ptr [rbp - 0x78], rbx
004C11B8  45 33 ED                        xor r13d, r13d
004C11BB  33 F6                           xor esi, esi
004C11BD  E8 2E BA DB FF                  call 0x14027cbf0
004C11C2  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
004C11C6  88 44 24 31                     mov byte ptr [rsp + 0x31], al
004C11CA  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
004C11D4  48 C1 E9 09                     shr rcx, 9
004C11D8  48 23 C8                        and rcx, rax
004C11DB  49 BA 00 00 00 00 80 F6 FF FF   movabs r10, 0xfffff68000000000
004C11E5  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004C11EA  48 2B C1                        sub rax, rcx
004C11ED  49 8B CA                        mov rcx, r10
004C11F0  48 2B C1                        sub rax, rcx
004C11F3  45 8D 5D 01                     lea r11d, [r13 + 1]
004C11F7  48 83 C0 30                     add rax, 0x30
004C11FB  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
004C11FF  49 B9 FF FF FF FF FF 00 00 00   movabs r9, 0xffffffffff
004C1209  48 3B FB                        cmp rdi, rbx
004C120C  0F 83 D4 03 00 00               jae 0x1404c15e6
004C1212  4D 85 ED                        test r13, r13
004C1215  74 22                           je 0x1404c1239
004C1217  48 F7 C7 FF 0F 00 00            test rdi, 0xfff
004C121E  0F 85 A0 00 00 00               jne 0x1404c12c4
004C1224  49 8B D5                        mov rdx, r13
004C1227  49 8B CE                        mov rcx, r14
004C122A  E8 91 5C D5 FF                  call 0x140216ec0
004C122F  49 BA 00 00 00 00 80 F6 FF FF   movabs r10, 0xfffff68000000000
004C1239  4C 8B EF                        mov r13, rdi
004C123C  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
004C1246  49 C1 ED 09                     shr r13, 9
004C124A  4C 23 E8                        and r13, rax
004C124D  49 8B C2                        mov rax, r10
004C1250  4C 03 E8                        add r13, rax
004C1253  49 8B CE                        mov rcx, r14
004C1256  49 8B D5                        mov rdx, r13
004C1259  E8 32 D6 D7 FF                  call 0x14023e890
004C125E  8A 54 24 31                     mov dl, byte ptr [rsp + 0x31]
004C1262  4C 8D 4B F8                     lea r9, [rbx - 8]
004C1266  4C 8B C7                        mov r8, rdi
004C1269  49 8B CE                        mov rcx, r14
004C126C  E8 1B 96 DE FF                  call 0x1402aa88c
004C1271  48 8B CF                        mov rcx, rdi
004C1274  E8 77 55 E8 FF                  call 0x1403467f0
004C1279  4C 8D 4B F8                     lea r9, [rbx - 8]
004C127D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
004C1282  4C 8B C7                        mov r8, rdi
004C1285  B2 11                           mov dl, 0x11
004C1287  49 8B CE                        mov rcx, r14
004C128A  E8 FD 95 DE FF                  call 0x1402aa88c
004C128F  48 85 C0                        test rax, rax
004C1292  74 16                           je 0x1404c12aa
004C1294  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
004C1298  BB 19 00 00 40                  mov ebx, 0x40000019
004C129D  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
004C12A1  48 3B F8                        cmp rdi, rax
004C12A4  0F 84 40 03 00 00               je 0x1404c15ea
004C12AA  49 BA 00 00 00 00 80 F6 FF FF   movabs r10, 0xfffff68000000000
004C12B4  49 B9 FF FF FF FF FF 00 00 00   movabs r9, 0xffffffffff
004C12BE  41 BB 01 00 00 00               mov r11d, 1
004C12C4  48 8B 1F                        mov rbx, qword ptr [rdi]
004C12C7  41 84 DB                        test r11b, bl
004C12CA  0F 84 F6 02 00 00               je 0x1404c15c6
004C12D0  48 8B CB                        mov rcx, rbx
004C12D3  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004C12DD  48 C1 E9 0C                     shr rcx, 0xc
004C12E1  49 23 C9                        and rcx, r9
004C12E4  4C 8D 04 49                     lea r8, [rcx + rcx*2]
004C12E8  4D 03 C0                        add r8, r8
004C12EB  48 8B C0                        mov rax, rax
004C12EE  48 3B 0D EB C9 96 00            cmp rcx, qword ptr [rip + 0x96c9eb]
004C12F5  4A 8D 14 C0                     lea rdx, [rax + r8*8]
004C12F9  77 67                           ja 0x1404c1362
004C12FB  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
004C1305  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
004C1309  48 C1 E8 36                     shr rax, 0x36
004C130D  41 85 C3                        test r11d, eax
004C1310  74 50                           je 0x1404c1362
004C1312  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
004C1316  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
004C1320  48 0B C1                        or rax, rcx
004C1323  48 3B C7                        cmp rax, rdi
004C1326  0F 84 7F 02 00 00               je 0x1404c15ab
004C132C  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
004C1330  41 0F B7 CB                     movzx ecx, r11w
004C1334  48 0F BA E0 28                  bt rax, 0x28
004C1339  72 16                           jb 0x1404c1351
004C133B  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
004C133F  49 B8 FE FF FF FF 3F 00 00 00   movabs r8, 0x3ffffffffe
004C1349  49 23 C1                        and rax, r9
004C134C  49 3B C0                        cmp rax, r8
004C134F  75 05                           jne 0x1404c1356
004C1351  B9 02 00 00 00                  mov ecx, 2
004C1356  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
004C1359  66 3B C1                        cmp ax, cx
004C135C  0F 82 2E 02 00 00               jb 0x1404c1590
004C1362  F6 C3 42                        test bl, 0x42
004C1365  74 3A                           je 0x1404c13a1
004C1367  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
004C136B  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
004C136E  25 00 00 60 00                  and eax, 0x600000
004C1373  3D 00 00 60 00                  cmp eax, 0x600000
004C1378  75 27                           jne 0x1404c13a1
004C137A  48 8B D7                        mov rdx, rdi
004C137D  48 C1 E2 19                     shl rdx, 0x19
004C1381  49 8B C2                        mov rax, r10
004C1384  48 C1 E0 19                     shl rax, 0x19
004C1388  4C 8B C1                        mov r8, rcx
004C138B  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
004C138F  48 2B D0                        sub rdx, rax
004C1392  48 C1 FA 10                     sar rdx, 0x10
004C1396  E8 89 3E FA FF                  call 0x140465224
004C139B  41 BB 01 00 00 00               mov r11d, 1
004C13A1  45 33 C0                        xor r8d, r8d
004C13A4  4D 8B F7                        mov r14, r15
004C13A7  4D 85 FF                        test r15, r15
004C13AA  74 03                           je 0x1404c13af
004C13AC  4D 8B 3F                        mov r15, qword ptr [r15]
004C13AF  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004C13B9  48 8B C0                        mov rax, rax
004C13BC  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
004C13C0  49 8B CE                        mov rcx, r14
004C13C3  48 2B C8                        sub rcx, rax
004C13C6  81 E3 00 08 00 00               and ebx, 0x800
004C13CC  48 C1 F9 04                     sar rcx, 4
004C13D0  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
004C13DA  48 0F AF C8                     imul rcx, rax
004C13DE  48 F7 DB                        neg rbx
004C13E1  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
004C13E5  1B C9                           sbb ecx, ecx
004C13E7  83 E1 03                        and ecx, 3
004C13EA  41 03 CB                        add ecx, r11d
004C13ED  E8 EA 31 DC FF                  call 0x1402845dc
004C13F2  8B C8                           mov ecx, eax
004C13F4  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
004C13F8  E8 03 66 E7 FF                  call 0x140337a00
004C13FD  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
004C1401  44 38 44 24 30                  cmp byte ptr [rsp + 0x30], r8b
004C1406  75 33                           jne 0x1404c143b
004C1408  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
004C140C  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
004C1410  44 88 5C 24 30                  mov byte ptr [rsp + 0x30], r11b
004C1415  48 89 88 98 00 00 00            mov qword ptr [rax + 0x98], rcx
004C141C  4C 89 B0 F8 00 00 00            mov qword ptr [rax + 0xf8], r14
004C1423  44 89 40 50                     mov dword ptr [rax + 0x50], r8d
004C1427  4C 89 40 58                     mov qword ptr [rax + 0x58], r8
004C142B  8B 88 C0 00 00 00               mov ecx, dword ptr [rax + 0xc0]
004C1431  0F BA E9 07                     bts ecx, 7
004C1435  89 88 C0 00 00 00               mov dword ptr [rax + 0xc0], ecx
004C143B  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
004C1440  49 8B CE                        mov rcx, r14
004C1443  E8 78 2B EA FF                  call 0x140363fc0
004C1448  33 DB                           xor ebx, ebx
004C144A  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
004C1451  73 33                           jae 0x1404c1486
004C1453  FF C3                           inc ebx
004C1455  85 1D 51 3E B0 00               test dword ptr [rip + 0xb03e51], ebx
004C145B  75 1C                           jne 0x1404c1479
004C145D  8B 05 55 56 B0 00               mov eax, dword ptr [rip + 0xb05655]
004C1463  A8 40                           test al, 0x40
004C1465  74 12                           je 0x1404c1479
004C1467  E8 24 E0 E4 FF                  call 0x14030f490
004C146C  84 C0                           test al, al
004C146E  74 09                           je 0x1404c1479
004C1470  8B CB                           mov ecx, ebx
004C1472  E8 E9 DF E4 FF                  call 0x14030f460
004C1477  EB 02                           jmp 0x1404c147b
004C1479  F3 90                           pause
004C147B  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
004C147F  48 85 C0                        test rax, rax
004C1482  79 C6                           jns 0x1404c144a
004C1484  EB CD                           jmp 0x1404c1453
004C1486  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
004C148A  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
004C148E  C1 E8 10                        shr eax, 0x10
004C1491  0C 20                           or al, 0x20
004C1493  88 44 24 36                     mov byte ptr [rsp + 0x36], al
004C1497  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
004C149B  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
004C149F  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
004C14A3  48 85 C0                        test rax, rax
004C14A6  74 04                           je 0x1404c14ac
004C14A8  48 83 C0 20                     add rax, 0x20
004C14AC  49 89 06                        mov qword ptr [r14], rax
004C14AF  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
004C14B9  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
004C14BD  BA 01 00 00 00                  mov edx, 1
004C14C2  48 23 C1                        and rax, rcx
004C14C5  49 8B CE                        mov rcx, r14
004C14C8  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
004C14CC  E8 7F A0 DC FF                  call 0x14028b550
004C14D1  49 89 7E 08                     mov qword ptr [r14 + 8], rdi
004C14D5  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
004C14D9  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
004C14DD  C1 E8 10                        shr eax, 0x10
004C14E0  24 FA                           and al, 0xfa
004C14E2  0C 02                           or al, 2
004C14E4  88 44 24 36                     mov byte ptr [rsp + 0x36], al
004C14E8  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
004C14EC  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
004C14F0  41 8B 4E 20                     mov ecx, dword ptr [r14 + 0x20]
004C14F4  8A 44 24 50                     mov al, byte ptr [rsp + 0x50]
004C14F8  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
004C14FC  C1 E9 18                        shr ecx, 0x18
004C14FF  32 C1                           xor al, cl
004C1501  24 07                           and al, 7
004C1503  32 C1                           xor al, cl
004C1505  B9 FF 03 00 00                  mov ecx, 0x3ff
004C150A  88 44 24 37                     mov byte ptr [rsp + 0x37], al
004C150E  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
004C1512  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
004C1516  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
004C151A  48 C1 E8 2B                     shr rax, 0x2b
004C151E  66 85 C1                        test cx, ax
004C1521  74 11                           je 0x1404c1534
004C1523  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
004C1528  48 8B 89 F0 0A 00 00            mov rcx, qword ptr [rcx + 0xaf0]
004C152F  E8 DC BB D7 FF                  call 0x14023d110
004C1534  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
004C153E  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
004C1543  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
004C1548  41 BB 01 00 00 00               mov r11d, 1
004C154E  41 8B D3                        mov edx, r11d
004C1551  E8 3A 53 DC FF                  call 0x140286890
004C1556  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
004C155A  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
004C155E  49 8B C8                        mov rcx, r8
004C1561  E8 0A 2A EA FF                  call 0x140363f70
004C1566  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
004C156B  49 03 F3                        add rsi, r11
004C156E  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
004C1572  48 89 07                        mov qword ptr [rdi], rax
004C1575  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
004C1579  49 BA 00 00 00 00 80 F6 FF FF   movabs r10, 0xfffff68000000000
004C1583  4C 89 04 38                     mov qword ptr [rax + rdi], r8
004C1587  48 83 C7 08                     add rdi, 8
004C158B  E9 6F FC FF FF                  jmp 0x1404c11ff
004C1590  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
004C1595  4C 8B CB                        mov r9, rbx
004C1598  BA 81 60 00 00                  mov edx, 0x6081
004C159D  4C 8B C7                        mov r8, rdi
004C15A0  B9 1A 00 00 00                  mov ecx, 0x1a
004C15A5  E8 B6 C0 03 00                  call 0x1404fd660
004C15AA  CC                              int3
004C15AB  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
004C15B0  4C 8B CB                        mov r9, rbx
004C15B3  BA 80 60 00 00                  mov edx, 0x6080
004C15B8  4C 8B C7                        mov r8, rdi
004C15BB  B9 1A 00 00 00                  mov ecx, 0x1a
004C15C0  E8 9B C0 03 00                  call 0x1404fd660
004C15C5  CC                              int3
004C15C6  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004C15CB  4C 8B CB                        mov r9, rbx
004C15CE  4C 8B C7                        mov r8, rdi
004C15D1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004C15D6  BA 00 12 04 00                  mov edx, 0x41200
004C15DB  B9 1A 00 00 00                  mov ecx, 0x1a
004C15E0  E8 7B C0 03 00                  call 0x1404fd660
004C15E5  CC                              int3
004C15E6  8B 5C 24 3C                     mov ebx, dword ptr [rsp + 0x3c]
004C15EA  4D 85 ED                        test r13, r13
004C15ED  74 0B                           je 0x1404c15fa
004C15EF  49 8B D5                        mov rdx, r13
004C15F2  49 8B CE                        mov rcx, r14
004C15F5  E8 C6 58 D5 FF                  call 0x140216ec0
004C15FA  8A 54 24 31                     mov dl, byte ptr [rsp + 0x31]
004C15FE  49 8B CE                        mov rcx, r14
004C1601  E8 8A C0 DB FF                  call 0x14027d690
004C1606  49 8B CF                        mov rcx, r15
004C1609  4D 85 FF                        test r15, r15
004C160C  74 0A                           je 0x1404c1618
004C160E  4D 8B 3F                        mov r15, qword ptr [r15]
004C1611  E8 CA 34 E7 FF                  call 0x140334ae0
004C1616  EB EE                           jmp 0x1404c1606
004C1618  49 3B F4                        cmp rsi, r12
004C161B  74 1E                           je 0x1404c163b
004C161D  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
004C1622  4C 2B E6                        sub r12, rsi
004C1625  49 8B D4                        mov rdx, r12
004C1628  45 33 C0                        xor r8d, r8d
004C162B  E8 F8 C2 EA FF                  call 0x14036d928
004C1630  48 85 F6                        test rsi, rsi
004C1633  B8 19 00 00 40                  mov eax, 0x40000019
004C1638  0F 44 D8                        cmove ebx, eax
004C163B  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
004C1640  8B C6                           mov eax, esi
004C1642  C1 E0 0C                        shl eax, 0xc
004C1645  41 89 46 28                     mov dword ptr [r14 + 0x28], eax
004C1649  48 85 F6                        test rsi, rsi
004C164C  0F 84 9C 00 00 00               je 0x1404c16ee
004C1652  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
004C1656  F0 48 01 B7 88 02 00 00         lock add qword ptr [rdi + 0x288], rsi
004C165E  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
004C1663  48 8D 4D E0                     lea rcx, [rbp - 0x20]
004C1667  41 B9 08 00 00 00               mov r9d, 8
004C166D  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
004C1675  45 8D 41 0C                     lea r8d, [r9 + 0xc]
004C1679  E8 82 38 DD FF                  call 0x140294f00
004C167E  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
004C1682  48 8D 4D E0                     lea rcx, [rbp - 0x20]
004C1686  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
004C168D  45 33 C9                        xor r9d, r9d
004C1690  4C 8B C6                        mov r8, rsi
004C1693  E8 D8 1F DD FF                  call 0x140293670
004C1698  48 8D 4D E0                     lea rcx, [rbp - 0x20]
004C169C  E8 1F 09 E5 FF                  call 0x140311fc0
004C16A1  49 89 7E 10                     mov qword ptr [r14 + 0x10], rdi
004C16A5  B8 02 00 00 00                  mov eax, 2
004C16AA  66 41 09 46 0A                  or word ptr [r14 + 0xa], ax
004C16AF  65 44 8B 04 25 A4 01 00 00      mov r8d, dword ptr gs:[0x1a4]
004C16B8  49 D1 E8                        shr r8, 1
004C16BB  41 83 E0 03                     and r8d, 3
004C16BF  49 83 C0 08                     add r8, 8
004C16C3  49 C1 E0 06                     shl r8, 6
004C16C7  4C 03 87 10 04 00 00            add r8, qword ptr [rdi + 0x410]
004C16CE  F0 49 01 30                     lock add qword ptr [r8], rsi
004C16D2  44 8B 05 E3 54 B0 00            mov r8d, dword ptr [rip + 0xb054e3]
004C16D9  41 F6 C0 01                     test r8b, 1
004C16DD  74 0F                           je 0x1404c16ee
004C16DF  44 8D 40 02                     lea r8d, [rax + 2]
004C16E3  48 8B D6                        mov rdx, rsi
004C16E6  49 8B CE                        mov rcx, r14
004C16E9  E8 52 8B FD FF                  call 0x14049a240
004C16EE  8B C3                           mov eax, ebx
004C16F0  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
004C16F7  48 33 CC                        xor rcx, rsp
004C16FA  E8 41 AF 1E 00                  call 0x1406ac640
004C16FF  48 8B 9C 24 18 02 00 00         mov rbx, qword ptr [rsp + 0x218]
004C1707  48 81 C4 C0 01 00 00            add rsp, 0x1c0
004C170E  41 5F                           pop r15
004C1710  41 5E                           pop r14
004C1712  41 5D                           pop r13
004C1714  41 5C                           pop r12
004C1716  5F                              pop rdi
004C1717  5E                              pop rsi
004C1718  5D                              pop rbp
004C1719  C3                              ret
004C171A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSwitchToTransition(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned int v_stack_m1BC;
    unsigned int v_stack_m1C0;
    unsigned __int8 v_stack_m1C1;
    unsigned __int8 v_stack_m1C2;
    unsigned int v_stack_m1C4;
    unsigned __int8 v_stack_m1C7;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 9738174)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1C0 = a3;
    v_stack_m148 = a2;
    v_stack_m198 = a1;
    a2 = 0;
    v_stack_m158 = v_xmm0;
    result = memset(v_stack_m118, a2, 200, a4);
    v_stack_m140 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m168 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = MiGetEffectivePagePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, 200, a4);
    v_stack_m1A8 = (unsigned int)(result);
    result = MiGetReadyInPageBlock(0, a2, 200, a4);
    v_stack_m178 = result;
    v_stack_m160 = *(unsigned __int64 *)(a1 + 32);
    v_rdi = (*(unsigned __int64 *)(a1 + 32)) >> (9);
    v_rdi = (v_rdi) & (*(unsigned __int64 *)(a1 + 32));
    v_rbx = ((unsigned int)(*(unsigned int *)(a1 + 40))) >> (12);
    a3 = 0;
    v_stack_m1C8 = 0;
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a1 + 32));
    v_stack_m190 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    result = MiInitializePageColorBase(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a3 + 3, a3, v_stack_m158);
    result = (unsigned int)(((unsigned int)(v_stack_m150)) & (0xFFF3FFFFULL));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (3));
    v_r15 = 0;
    a4 = (unsigned int)((a4) << (18));
    a4 = (unsigned int)((a4) | ((unsigned int)(result)));
    v_stack_m1B0 = result;
    v_stack_m150 = (unsigned int)(a4);
    v_stack_m1A0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891841) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8);
    result = MiObtainFaultCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891841) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8), v_rbx, v_r15 + 2, a4);
    v_rsi = 0;
    v_rbx = (v_rbx) | (-1);
    v_stack_m180 = v_rbx;
loc_004C10AE:
loc_004C10B3:
    if (0 == result) goto loc_004C1177;
    a2 = 0;
    a1 = (v_stack_m150) >> (16);
    a1 = (unsigned int)((a1) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(v_stack_m150)));
    a2 = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)(v_stack_m150)));
    result = MiGetPage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891841) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8), a2, 8, v_rip + 9882607);
    if (result != v_rbx) goto loc_004C1111;
    if (0 != 0) goto loc_004C1166;
    a2 = 0;
    result = MiWaitForFreePage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9891841) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8), a2, 8, v_rip + 9882607);
    goto loc_004C10AE;
loc_004C1111:
    v_rbx = (result + result * 2) << (4);
    v_rbx = (v_rbx) + (result);
    a3 = 0;
    result = MiPageAttributeBatchChangeNeeded(v_rbx, (unsigned int)(v_stack_m1C0), a3, v_rip + 9882607);
    if ((unsigned int)(result) != 0) {
        a1 = v_stack_m1B0;
        result = MiMakeLinkedListPte(a1, (unsigned int)(v_stack_m1C0), a3, v_rip + 9882607);
        *(unsigned __int64 *)(v_rbx + 16) = result;
        v_stack_m1B0 = result;
    }
    *(unsigned __int64 *)(v_rbx) = 0;
    v_rsi = (v_rsi) + (1);
    v_rbx = (v_rbx) | (-1);
    goto loc_004C10B3;
loc_004C1166:
    v_r12 = (result) - (v_rsi);
    a3 = 0;
    result = MiReturnFaultCharges(a1, v_r12, a3, v_rip + 9882607);
loc_004C1177:
    if (v_stack_m1B0 != result) {
        a1 = v_stack_m188;
        result = MiSetOriginalPtePfnFromFreeList(a1, v_r12, a3, v_rip + 9882607);
        a2 = v_stack_m1C0;
        a1 = v_stack_m1B0;
        a3 = v_stack_m188;
        a4 = 0;
        result = MiChangePageAttributeBatch(a1, a2, a3, a4);
    }
    v_stack_m170 = v_rdi + v_rsi * 8;
    v_r13 = 0;
    v_rsi = 0;
    result = MiLockWorkingSetShared(v_stack_m190, a2, a3, a4);
    v_stack_m1C7 = (unsigned __int8)(result);
    a1 = (v_stack_m160) >> (9);
    a1 = (a1) & (result);
    result = (v_stack_m198) - (a1);
    result = (result) - (v_r10);
    result = (result) + (48);
    v_stack_m130 = result;
loc_004C11FF:
    if (v_rdi >= (v_rdi + v_rsi * 8)) goto loc_004C15E6;
    if (0 == 0) goto loc_004C1239;
    if (((v_rdi) & (0xFFFULL)) != 0) goto loc_004C12C4;
    result = MiUnlockPageTable(v_stack_m190, 0, a3, a4);
loc_004C1239:
    v_r13 = (v_rdi) >> (9);
    v_r13 = (v_r13) & (result);
    v_r13 = (v_r13) + (v_r10);
    result = MiLockNestedPageTable(v_stack_m190, v_r13, a3, a4);
    result = MiUnlockOpportunisticPagesInPageTable(v_stack_m190, v_stack_m1C7, v_rdi, v_rdi + v_rsi * 8 - 8);
    result = MiGetContainingPageTable(v_rdi, v_stack_m1C7, v_rdi, v_rdi + v_rsi * 8 - 8);
    v_stack_m180 = result;
    result = MiUnlockOpportunisticPagesInPageTable(v_stack_m190, 17, v_rdi, v_rdi + v_rsi * 8 - 8);
    if (result == 0) goto loc_004C12AA;
    v_stack_m170 = result;
    v_stack_m1BC = (unsigned int)((unsigned int)(0x40000019ULL));
    if (v_rdi == result) goto loc_004C15EA;
loc_004C12AA:
loc_004C12C4:
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_rdi)))) == 0) goto loc_004C15C6;
    a1 = (*(unsigned __int64 *)(v_rdi)) >> (12);
    a1 = (a1) & (v_rdi + v_rsi * 8 - 8);
    a3 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if (a1 > (*(unsigned __int64 *)(v_rip + 9882091))) goto loc_004C1362;
    result = (*(unsigned __int64 *)(result + a3 * 8)) >> (54);
    if (((1) & ((unsigned int)(result))) == 0) goto loc_004C1362;
    result = (*(unsigned __int64 *)(result + a3 * 8 + 8)) | (a1);
    if (result == v_rdi) goto loc_004C15AB;
    if (result < v_rdi) goto loc_004C1351;
    result = (*(unsigned __int64 *)(result + a3 * 8 + 40)) & (v_rdi + v_rsi * 8 - 8);
    if (result == a3) {
        a1 = 2;
    }
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(result + a3 * 8 + 32)))) < ((unsigned __int16)(a1))) goto loc_004C1590;
loc_004C1362:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (66)) == 0) goto loc_004C13A1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m148 + 48))) & (0x600000ULL));
    v_r11 = 1;
    if (((unsigned int)(result)) == 0x600000ULL) {
        a2 = v_rdi;
        a2 = (a2) << (25);
        result = v_r10;
        result = (result) << (25);
        a3 = v_stack_m148;
        a1 = v_stack_m168;
        a2 = (a2) - (result);
        a2 = (a2) >> (16);
        result = MiCaptureWriteWatchDirtyBit(a1, a2, a3, v_rdi + v_rsi * 8 - 8);
        v_r11 = 1;
    }
    a3 = 0;
    v_r15 = v_rbx;
    if (v_rbx != 0) {
        v_r15 = *(unsigned __int64 *)(v_rbx);
    }
    a1 = (v_rbx) - (result);
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_rdi)) & (0x800ULL));
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    v_rbx = -(v_rbx);
    v_stack_m138 = a1;
    a1 = (unsigned int)((a1) & (3));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r11)));
    result = MiUpdateProtectionMask(a1, (unsigned int)(v_stack_m1C0), a3, v_rdi + v_rsi * 8 - 8);
    v_stack_m1B8 = (unsigned int)(result);
    result = MiMakeDemandZeroPte((unsigned int)((unsigned int)(result)), (unsigned int)(v_stack_m1C0), a3, v_rdi + v_rsi * 8 - 8);
    *(unsigned __int64 *)(v_rbx + 16) = result;
    if (v_stack_m1C8 == 0) {
        result = v_stack_m178;
        a1 = v_stack_m140;
        v_stack_m1C8 = (unsigned __int8)(v_r11);
        *(unsigned __int64 *)(result + 152) = a1;
        *(unsigned __int64 *)(result + 248) = v_rbx;
        *(unsigned int *)(result + 80) = 0;
        *(unsigned __int64 *)(result + 88) = 0;
        a1 = *(unsigned int *)(result + 192);
        *(unsigned int *)(result + 192) = (unsigned int)(a1);
    }
    result = MiSetPfnContainingFrame(v_rbx, v_stack_m180, a3, v_rdi + v_rsi * 8 - 8);
    v_rbx = 0;
loc_004C144A:
    if (condition_is_above_or_equal) goto loc_004C1486;
loc_004C1453:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 11550289)) & ((unsigned int)(v_rbx))) != 0) goto loc_004C1479;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11556437)))) & (64)) == 0) goto loc_004C1479;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rbx, v_stack_m180, a3, v_rdi + v_rsi * 8 - 8);
    if ((unsigned __int8)(result) == 0) goto loc_004C1479;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_stack_m180, a3, v_rdi + v_rsi * 8 - 8);
    goto loc_004C147B;
loc_004C1479:
loc_004C147B:
    if (!sign_flag) goto loc_004C144A;
    goto loc_004C1453;
loc_004C1486:
    v_stack_m1C4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (16));
    result = (unsigned __int8)((result) | (32));
    v_stack_m1C2 = (unsigned __int8)(result);
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_m1C4));
    result = v_stack_m178;
    if (v_stack_m178 != 0) {
        result = (v_stack_m178) + (32);
    }
    *(unsigned __int64 *)(v_rbx) = result;
    result = (*(unsigned __int64 *)(v_rbx + 24)) & ((unsigned int)((unsigned int)(v_rbx)));
    *(unsigned __int64 *)(v_rbx + 24) = result;
    result = MiAddLockedPageCharge(v_rbx, 1, a3, v_rdi + v_rsi * 8 - 8);
    *(unsigned __int64 *)(v_rbx + 8) = v_rdi;
    v_stack_m1C4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (16));
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_m1C2 = (unsigned __int8)(result);
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_m1C4));
    v_stack_m1C4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (24));
    result = (unsigned __int8)((v_stack_m1A8) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (7));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    v_stack_m1C1 = (unsigned __int8)(result);
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_m1C4));
    result = (*(unsigned __int64 *)(v_rbx + 40)) >> (43);
    if ((((unsigned __int16)((unsigned int)(0x3FFULL))) & ((unsigned __int16)(result))) != 0) {
        a1 = v_stack_m1A0;
        a1 = *(unsigned __int64 *)(a1 + 2800);
        result = ExAcquireRundownProtectionCacheAware(a1, 1, a3, v_rdi + v_rsi * 8 - 8);
    }
    result = MiReturnResident(v_stack_m1A0, 1, a3, v_rdi + v_rsi * 8 - 8);
    result = MiMakeTransitionPte(v_stack_m138, (unsigned int)(v_stack_m1B8), v_stack_m138, v_rdi + v_rsi * 8 - 8);
    v_rsi = (v_rsi) + (1);
    *(unsigned __int64 *)(v_rdi) = result;
    *(unsigned __int64 *)(v_stack_m130 + v_rdi * 1) = v_stack_m138;
    v_rdi = (v_rdi) + (8);
    goto loc_004C11FF;
loc_004C1590:
    v_stack_m1D8 = (unsigned int)(v_stack_m1B8);
    result = KeBugCheckEx(26, (unsigned int)(0x6081ULL), v_rdi, v_stack_m170);
loc_004C15AB:
    v_stack_m1D8 = (unsigned int)(0x6081ULL);
    result = KeBugCheckEx(26, (unsigned int)(0x6080ULL), v_rdi, v_stack_m170);
loc_004C15C6:
    v_stack_m1D8 = v_stack_m198;
    result = KeBugCheckEx(26, (unsigned int)(0x41200ULL), v_rdi, v_stack_m170);
loc_004C15E6:
loc_004C15EA:
    if (v_r13 != 0) {
        a2 = v_r13;
        a1 = v_stack_m190;
        result = MiUnlockPageTable(a1, a2, v_rdi, v_stack_m170);
    }
    result = MiUnlockWorkingSetShared(v_stack_m190, v_stack_m1C7, v_rdi, v_stack_m170);
loc_004C1606:
    if (v_r15 == 0) goto loc_004C1618;
    result = MiReleaseFreshPage(v_r15, v_stack_m1C7, v_rdi, v_stack_m170);
    goto loc_004C1606;
loc_004C1618:
    v_rbx = (unsigned int)(v_stack_m1BC);
    v_r12 = v_rsi;
    if (v_rsi != v_rsi) {
        a1 = v_stack_m1A0;
        v_r12 = (v_rsi) - (v_rsi);
        a2 = v_r12;
        a3 = 0;
        result = MiReturnFaultCharges(a1, a2, a3, v_stack_m170);
        result = 0x40000019ULL;
        v_rbx = (unsigned int)(v_stack_m1BC);
        if (v_rsi == 0) { v_rbx = (unsigned int)(result); }
    }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) << (12));
    *(unsigned int *)(v_stack_m198 + 40) = (unsigned int)(result);
    if (v_rsi == 0) goto loc_004C16EE;
    v_stack_m1D8 = 1;
    result = MiInitializeTbFlushList(v_stack_m118, v_stack_m190, 8 + 12, 8);
    a2 = (v_stack_m160) & (0xFFFFFFFFFFFFF000ULL);
    a4 = 0;
    result = MiInsertTbFlushEntry(v_stack_m118, a2, v_rsi, a4);
    result = MiFlushTbList(v_stack_m118, a2, v_rsi, a4);
    *(unsigned __int64 *)(v_stack_m198 + 16) = v_stack_m168;
    a3 = ((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) >> (1);
    a3 = (unsigned int)((a3) & (3));
    a3 = (a3) + (8);
    a3 = (a3) << (6);
    a3 = (a3) + (*(unsigned __int64 *)(v_stack_m168 + 1040));
    result = 2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11556067)))) & (1)) != 0) {
        a3 = 2 + 2;
        a2 = v_rsi;
        a1 = v_stack_m198;
        result = MiAddMdlTracker(a1, a2, a3, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (448);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiSwitchToTransition(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint32_t v_stack_m1BC;
    uint32_t v_stack_m1C0;
    uint8_t v_stack_m1C1;
    uint8_t v_stack_m1C2;
    uint32_t v_stack_m1C4;
    uint8_t v_stack_m1C7;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0x9497BE)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1C0 = Arg3;
    v_stack_m148 = Arg2;
    v_stack_m198 = Arg1;
    Arg2 = 0;
    v_stack_m158 = v_xmm0;
    result = memset(v_stack_m118, Arg2, 200, a4);
    v_stack_m140 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m168 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = MiGetEffectivePagePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, 200, a4);
    v_stack_m1A8 = (uint32_t)(result);
    result = MiGetReadyInPageBlock(0, Arg2, 200, a4);
    v_stack_m178 = result;
    v_stack_m160 = *(uint64_t *)(arg1 + 0x20);
    local_rdi = (*(uint64_t *)(arg1 + 0x20)) >> (9);
    local_rdi = (local_rdi) & (*(uint64_t *)(arg1 + 0x20));
    local_rbx = ((uint32_t)(*(uint32_t *)(arg1 + 0x28))) >> (12);
    Arg3 = 0;
    v_stack_m1C8 = 0;
    local_rdi = (local_rdi) + (*(uint64_t *)(arg1 + 0x20));
    v_stack_m190 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    result = MiInitializePageColorBase(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg3 + 3, Arg3, v_stack_m158);
    result = (uint32_t)(((uint32_t)(v_stack_m150)) & (0xFFF3FFFFULL));
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (3));
    local_r15 = 0;
    a4 = (uint32_t)((a4) << (18));
    a4 = (uint32_t)((a4) | ((uint32_t)(result)));
    v_stack_m1B0 = result;
    v_stack_m150 = (uint32_t)(a4);
    v_stack_m1A0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x96F001) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8);
    result = MiObtainFaultCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96F001) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8), local_rbx, local_r15 + 2, a4);
    local_rsi = 0;
    local_rbx = (local_rbx) | (-1);
    v_stack_m180 = local_rbx;
loc_004C10AE:
loc_004C10B3:
    if (0 == result) goto loc_004C1177;
    Arg2 = 0;
    Arg1 = (v_stack_m150) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(v_stack_m150)));
    Arg2 = (uint32_t)(((uint8_t)(Arg2)) ^ ((uint32_t)(v_stack_m150)));
    result = MiGetPage(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96F001) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8), Arg2, 8, v_rip + 9882607);
    if (result != local_rbx) goto loc_004C1111;
    if (0 != 0) goto loc_004C1166;
    Arg2 = 0;
    result = MiWaitForFreePage(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96F001) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8), Arg2, 8, v_rip + 9882607);
    goto loc_004C10AE;
loc_004C1111:
    local_rbx = (result + result * 2) << (4);
    local_rbx = (local_rbx) + (result);
    Arg3 = 0;
    result = MiPageAttributeBatchChangeNeeded(local_rbx, (uint32_t)(v_stack_m1C0), Arg3, v_rip + 9882607);
    if ((uint32_t)(result) != 0) {
        Arg1 = v_stack_m1B0;
        result = MiMakeLinkedListPte(Arg1, (uint32_t)(v_stack_m1C0), Arg3, v_rip + 9882607);
        *(uint64_t *)(local_rbx + 0x10) = result;
        v_stack_m1B0 = result;
    }
    *(uint64_t *)(local_rbx) = 0;
    local_rsi = (local_rsi) + (1);
    local_rbx = (local_rbx) | (-1);
    goto loc_004C10B3;
loc_004C1166:
    local_r12 = (result) - (local_rsi);
    Arg3 = 0;
    result = MiReturnFaultCharges(Arg1, local_r12, Arg3, v_rip + 9882607);
loc_004C1177:
    if (v_stack_m1B0 != result) {
        Arg1 = v_stack_m188;
        result = MiSetOriginalPtePfnFromFreeList(Arg1, local_r12, Arg3, v_rip + 9882607);
        Arg2 = v_stack_m1C0;
        Arg1 = v_stack_m1B0;
        Arg3 = v_stack_m188;
        a4 = 0;
        result = MiChangePageAttributeBatch(Arg1, Arg2, Arg3, a4);
    }
    v_stack_m170 = local_rdi + local_rsi * 8;
    local_r13 = 0;
    local_rsi = 0;
    result = MiLockWorkingSetShared(v_stack_m190, Arg2, Arg3, a4);
    v_stack_m1C7 = (uint8_t)(result);
    Arg1 = (v_stack_m160) >> (9);
    Arg1 = (Arg1) & (result);
    result = (v_stack_m198) - (Arg1);
    result = (result) - (local_r10);
    result = (result) + (48);
    v_stack_m130 = result;
loc_004C11FF:
    if (local_rdi >= (local_rdi + local_rsi * 8)) goto loc_004C15E6;
    if (0 == 0) goto loc_004C1239;
    if (((local_rdi) & (0xFFFULL)) != 0) goto loc_004C12C4;
    result = MiUnlockPageTable(v_stack_m190, 0, Arg3, a4);
loc_004C1239:
    local_r13 = (local_rdi) >> (9);
    local_r13 = (local_r13) & (result);
    local_r13 = (local_r13) + (local_r10);
    result = MiLockNestedPageTable(v_stack_m190, local_r13, Arg3, a4);
    result = MiUnlockOpportunisticPagesInPageTable(v_stack_m190, v_stack_m1C7, local_rdi, local_rdi + local_rsi * 8 - 8);
    result = MiGetContainingPageTable(local_rdi, v_stack_m1C7, local_rdi, local_rdi + local_rsi * 8 - 8);
    v_stack_m180 = result;
    result = MiUnlockOpportunisticPagesInPageTable(v_stack_m190, 17, local_rdi, local_rdi + local_rsi * 8 - 8);
    if (result == 0) goto loc_004C12AA;
    v_stack_m170 = result;
    v_stack_m1BC = (uint32_t)((uint32_t)(0x40000019ULL));
    if (local_rdi == result) goto loc_004C15EA;
loc_004C12AA:
loc_004C12C4:
    if (((1) & ((uint8_t)(*(uint64_t *)(local_rdi)))) == 0) goto loc_004C15C6;
    Arg1 = (*(uint64_t *)(local_rdi)) >> (12);
    Arg1 = (Arg1) & (local_rdi + local_rsi * 8 - 8);
    Arg3 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if (Arg1 > (*(uint64_t *)(v_rip + 0x96C9EB))) goto loc_004C1362;
    result = (*(uint64_t *)(result + Arg3 * 8)) >> (54);
    if (((1) & ((uint32_t)(result))) == 0) goto loc_004C1362;
    result = (*(uint64_t *)(result + Arg3 * 8 + 0x8)) | (Arg1);
    if (result == local_rdi) goto loc_004C15AB;
    if (result < local_rdi) goto loc_004C1351;
    result = (*(uint64_t *)(result + Arg3 * 8 + 0x28)) & (local_rdi + local_rsi * 8 - 8);
    if (result == Arg3) {
        Arg1 = 2;
    }
    if (((uint16_t)((uint32_t)(*(uint32_t *)(result + Arg3 * 8 + 0x20)))) < ((uint16_t)(Arg1))) goto loc_004C1590;
loc_004C1362:
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (66)) == 0) goto loc_004C13A1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x30))) & (0x600000ULL));
    local_r11 = 1;
    if (((uint32_t)(result)) == 0x600000ULL) {
        Arg2 = local_rdi;
        Arg2 = (Arg2) << (25);
        result = local_r10;
        result = (result) << (25);
        Arg3 = v_stack_m148;
        Arg1 = v_stack_m168;
        Arg2 = (Arg2) - (result);
        Arg2 = (Arg2) >> (16);
        result = MiCaptureWriteWatchDirtyBit(Arg1, Arg2, Arg3, local_rdi + local_rsi * 8 - 8);
        local_r11 = 1;
    }
    Arg3 = 0;
    local_r15 = local_rbx;
    if (local_rbx != 0) {
        local_r15 = *(uint64_t *)(local_rbx);
    }
    Arg1 = (local_rbx) - (result);
    local_rbx = (uint32_t)((*(uint64_t *)(local_rdi)) & (0x800ULL));
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    local_rbx = -(local_rbx);
    v_stack_m138 = Arg1;
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r11)));
    result = MiUpdateProtectionMask(Arg1, (uint32_t)(v_stack_m1C0), Arg3, local_rdi + local_rsi * 8 - 8);
    v_stack_m1B8 = (uint32_t)(result);
    result = MiMakeDemandZeroPte((uint32_t)((uint32_t)(result)), (uint32_t)(v_stack_m1C0), Arg3, local_rdi + local_rsi * 8 - 8);
    *(uint64_t *)(local_rbx + 0x10) = result;
    if (v_stack_m1C8 == 0) {
        result = v_stack_m178;
        Arg1 = v_stack_m140;
        v_stack_m1C8 = (uint8_t)(local_r11);
        *(void **)(result + 0x98) = Arg1;
        *(uint64_t *)(result + 0xF8) = local_rbx;
        *(uint32_t *)(result + 0x50) = 0;
        *(uint64_t *)(result + 0x58) = 0;
        Arg1 = *(uint32_t *)(result + 0xC0);
        *(uint32_t *)(result + 0xC0) = (uint32_t)(Arg1);
    }
    result = MiSetPfnContainingFrame(local_rbx, v_stack_m180, Arg3, local_rdi + local_rsi * 8 - 8);
    local_rbx = 0;
loc_004C144A:
    if (condition_is_above_or_equal) goto loc_004C1486;
loc_004C1453:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xB03E51)) & ((uint32_t)(local_rbx))) != 0) goto loc_004C1479;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB05655)))) & (64)) == 0) goto loc_004C1479;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rbx, v_stack_m180, Arg3, local_rdi + local_rsi * 8 - 8);
    if ((uint8_t)(result) == 0) goto loc_004C1479;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_stack_m180, Arg3, local_rdi + local_rsi * 8 - 8);
    goto loc_004C147B;
loc_004C1479:
loc_004C147B:
    if (!sign_flag) goto loc_004C144A;
    goto loc_004C1453;
loc_004C1486:
    v_stack_m1C4 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (16));
    result = (uint8_t)((result) | (32));
    v_stack_m1C2 = (uint8_t)(result);
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_m1C4));
    result = v_stack_m178;
    if (v_stack_m178 != 0) {
        result = (v_stack_m178) + (32);
    }
    *(uint64_t *)(local_rbx) = result;
    result = (*(uint64_t *)(local_rbx + 0x18)) & ((uint32_t)((uint32_t)(local_rbx)));
    *(uint64_t *)(local_rbx + 0x18) = result;
    result = MiAddLockedPageCharge(local_rbx, 1, Arg3, local_rdi + local_rsi * 8 - 8);
    *(uint64_t *)(local_rbx + 0x8) = local_rdi;
    v_stack_m1C4 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (16));
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_m1C2 = (uint8_t)(result);
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_m1C4));
    v_stack_m1C4 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (24));
    result = (uint8_t)((v_stack_m1A8) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (7));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    v_stack_m1C1 = (uint8_t)(result);
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_m1C4));
    result = (*(uint64_t *)(local_rbx + 0x28)) >> (43);
    if ((((uint16_t)((uint32_t)(0x3FFULL))) & ((uint16_t)(result))) != 0) {
        Arg1 = v_stack_m1A0;
        Arg1 = *(uint64_t *)(arg1 + 0xAF0);
        result = ExAcquireRundownProtectionCacheAware(Arg1, 1, Arg3, local_rdi + local_rsi * 8 - 8);
    }
    result = MiReturnResident(v_stack_m1A0, 1, Arg3, local_rdi + local_rsi * 8 - 8);
    result = MiMakeTransitionPte(v_stack_m138, (uint32_t)(v_stack_m1B8), v_stack_m138, local_rdi + local_rsi * 8 - 8);
    local_rsi = (local_rsi) + (1);
    *(uint64_t *)(local_rdi) = result;
    *(uint64_t *)(v_stack_m130 + local_rdi * 1) = v_stack_m138;
    local_rdi = (local_rdi) + (8);
    goto loc_004C11FF;
loc_004C1590:
    v_stack_m1D8 = (uint32_t)(v_stack_m1B8);
    result = KeBugCheckEx(26, (uint32_t)(0x6081ULL), local_rdi, v_stack_m170);
loc_004C15AB:
    v_stack_m1D8 = (uint32_t)(0x6081ULL);
    result = KeBugCheckEx(26, (uint32_t)(0x6080ULL), local_rdi, v_stack_m170);
loc_004C15C6:
    v_stack_m1D8 = v_stack_m198;
    result = KeBugCheckEx(26, (uint32_t)(0x41200ULL), local_rdi, v_stack_m170);
loc_004C15E6:
loc_004C15EA:
    if (local_r13 != 0) {
        Arg2 = local_r13;
        Arg1 = v_stack_m190;
        result = MiUnlockPageTable(Arg1, Arg2, local_rdi, v_stack_m170);
    }
    result = MiUnlockWorkingSetShared(v_stack_m190, v_stack_m1C7, local_rdi, v_stack_m170);
loc_004C1606:
    if (local_r15 == 0) goto loc_004C1618;
    result = MiReleaseFreshPage(local_r15, v_stack_m1C7, local_rdi, v_stack_m170);
    goto loc_004C1606;
loc_004C1618:
    local_rbx = (uint32_t)(v_stack_m1BC);
    local_r12 = local_rsi;
    if (local_rsi != local_rsi) {
        Arg1 = v_stack_m1A0;
        local_r12 = (local_rsi) - (local_rsi);
        Arg2 = local_r12;
        Arg3 = 0;
        result = MiReturnFaultCharges(Arg1, Arg2, Arg3, v_stack_m170);
        result = 0x40000019ULL;
        local_rbx = (uint32_t)(v_stack_m1BC);
        if (local_rsi == 0) { local_rbx = (uint32_t)(result); }
    }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) << (12));
    *(uint32_t *)(v_stack_m198 + 0x28) = (uint32_t)(result);
    if (local_rsi == 0) goto loc_004C16EE;
    v_stack_m1D8 = 1;
    result = MiInitializeTbFlushList(v_stack_m118, v_stack_m190, 8 + 12, 8);
    Arg2 = (v_stack_m160) & (0xFFFFFFFFFFFFF000ULL);
    a4 = 0;
    result = MiInsertTbFlushEntry(v_stack_m118, Arg2, local_rsi, a4);
    result = MiFlushTbList(v_stack_m118, Arg2, local_rsi, a4);
    *(uint64_t *)(v_stack_m198 + 0x10) = v_stack_m168;
    Arg3 = ((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) >> (1);
    Arg3 = (uint32_t)((Arg3) & (3));
    Arg3 = (Arg3) + (8);
    Arg3 = (Arg3) << (6);
    Arg3 = (Arg3) + (*(uint64_t *)(v_stack_m168 + 0x410));
    result = 2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB054E3)))) & (1)) != 0) {
        Arg3 = 2 + 2;
        Arg2 = local_rsi;
        Arg1 = v_stack_m198;
        result = MiAddMdlTracker(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (448);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C0F5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
