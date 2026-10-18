# MmDeleteKernelStack

- RVA: `0x0033A960`–`0x0033B06E` (길이 `1,806` bytes)
- VA: `0x000000014033A960`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00076C58`
- 디코드: `406`개 명령, `1,806/1,806` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **14**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0033AB7C` → [MiPageToNode](MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x0033AB9E` → [MiAddKernelStackToPrcbCache](MiAddKernelStackToPrcbCache_function_00338710.md) (function, `0x00338710`)
- `0x0033AD0B` → [MiClearStackOwners](../2B/MiClearStackOwners_function_002B0D90.md) (function, `0x002B0D90`)
- `0x0033AD27` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0033AD3D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0033AD72` → [MiDeleteKernelStackPages](../2D/MiDeleteKernelStackPages_function_002D9938.md) (function, `0x002D9938`)
- `0x0033AD93` → [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) (function, `0x00247240`)
- `0x0033ADBF` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0033ADF1` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0033AE16` → [MiLogKernelStackEvent](../4D/MiLogKernelStackEvent_function_004D6848.md) (function, `0x004D6848`)
- `0x0033AE62` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0033AE81` → [MiDeleteKernelStackPages](../2D/MiDeleteKernelStackPages_function_002D9938.md) (function, `0x002D9938`)
- `0x0033AEAF` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0033AEBC` → [ExpInterlockedPopEntrySList](../6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x0033AF06` → [MiKernelShadowStackIdealForCaching](../48/MiKernelShadowStackIdealForCaching_function_00484330.md) (function, `0x00484330`)
- `0x0033AF1B` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0033AF3C` → [VslResetKernelShadowStack](../../page/A6/VslResetKernelShadowStack_function_00A6577C.md) (function, `0x00A6577C`)
- `0x0033AF97` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0033AFF8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0033B040` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0033B068` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [PspDeleteKernelStack](../2A/PspDeleteKernelStack_function_002A1550.md) at `0x002A159B`
- [sub_002F8911](../2F/Unknown_function_002F8911.md) at `0x002F8B96`
- [KiEnableOptionalXStateFeatures](../3D/KiEnableOptionalXStateFeatures_function_003D8BE8.md) at `0x003D8CBE`
- [KiFreeProcessorStacks](../5B/KiFreeProcessorStacks_function_005B7F84.md) at `0x005B7FC7`
- [KiDeleteXStateStack](../5B/KiDeleteXStateStack_function_005B93C4.md) at `0x005B9403`
- [KeEnableOptionalXStateFeaturesApc](../5B/KeEnableOptionalXStateFeaturesApc_function_005B9B90.md) at `0x005B9BFD`
- [KiFreeTemporaryStacks](../5B/KiFreeTemporaryStacks_function_005BD820.md) at `0x005BD876`
- [PspEnableProcessOptionalXStateFeatures](../../page/78/PspEnableProcessOptionalXStateFeatures_function_00781EF0.md) at `0x0078215B`
- [PspEnableProcessOptionalXStateFeatures](../../page/78/PspEnableProcessOptionalXStateFeatures_function_00781EF0.md) at `0x00782250`
- [KeUserModeCallback](../../page/8E/KeUserModeCallback_function_008E8A00.md) at `0x008E8DE8`
- [KeUserModeCallback](../../page/8E/KeUserModeCallback_function_008E8A00.md) at `0x008E8E38`
- [KeUninitThread](../../page/A2/KeUninitThread_function_00A25D2C.md) at `0x00A25D65`
- [KiDeleteKernelShadowStack](../../page/A2/KiDeleteKernelShadowStack_function_00A25DC8.md) at `0x00A25DF9`
- [KeFreeCalloutStack](../../page/A9/KeFreeCalloutStack_function_00A99AB0.md) at `0x00A99B24`
- [sub_00B42BA8](../../page/B4/Unknown_function_00B42BA8.md) at `0x00B42BC1`
- [KeInitThread](../../pagelk/B7/KeInitThread_function_00B78450.md) at `0x00B7898D`

### Static image references
- `0x0033A9E8` → RVA `0x00E35FA4` (`.data`; read)
- `0x0033AA7A` → RVA `0x00FC5088` (`ALMOSTRO`; read)
- `0x0033AAF6` → RVA `0x00FCEC68` (`ALMOSTRO`; read)
- `0x0033AB21` → RVA `0x00E38D00` (`.data`; read)
- `0x0033AB3F` → RVA `0x00E30088` (`.data`; read)
- `0x0033ACC8` → RVA `0x00E37600` (`.data`; read)
- `0x0033ACF4` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0033AD86` → RVA `0x00E35EE0` (`.data`; read)
- `0x0033AD9D` → RVA `0x00FC6CF8` (`ALMOSTRO`; read)
- `0x0033ADFB` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0033AE8D` → RVA `0x00E35F40` (`.data`; read)
- `0x0033AFC5` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0033AF3C` → [VslResetKernelShadowStack](../../page/A6/VslResetKernelShadowStack_function_00A6577C.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0033B032` → [sub_006E1FEC](../6E/Unknown_function_006E1FEC.md) (`tail-transfer`)
  - `0x0033B046` → [sub_006E1FEC](../6E/Unknown_function_006E1FEC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0033A960  40 53                           push rbx
0033A962  55                              push rbp
0033A963  56                              push rsi
0033A964  57                              push rdi
0033A965  41 54                           push r12
0033A967  41 55                           push r13
0033A969  41 56                           push r14
0033A96B  41 57                           push r15
0033A96D  48 81 EC 88 00 00 00            sub rsp, 0x88
0033A974  8B 11                           mov edx, dword ptr [rcx]
0033A976  48 8B D9                        mov rbx, rcx
0033A979  48 8B 69 18                     mov rbp, qword ptr [rcx + 0x18]
0033A97D  33 F6                           xor esi, esi
0033A97F  48 8B 79 10                     mov rdi, qword ptr [rcx + 0x10]
0033A983  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
0033A98D  44 8B 71 04                     mov r14d, dword ptr [rcx + 4]
0033A991  44 8B EE                        mov r13d, esi
0033A994  48 8B CD                        mov rcx, rbp
0033A997  89 94 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], edx
0033A99E  48 C1 E9 09                     shr rcx, 9
0033A9A2  49 23 C8                        and rcx, r8
0033A9A5  89 B4 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], esi
0033A9AC  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0033A9B6  49 8B C1                        mov rax, r9
0033A9B9  4C 8D 78 F8                     lea r15, [rax - 8]
0033A9BD  4C 03 F9                        add r15, rcx
0033A9C0  8D 4E 01                        lea ecx, [rsi + 1]
0033A9C3  41 83 FE 05                     cmp r14d, 5
0033A9C7  75 55                           jne 0x14033aa1e
0033A9C9  44 8D 56 02                     lea r10d, [rsi + 2]
0033A9CD  F6 C2 08                        test dl, 8
0033A9D0  0F 85 C7 03 00 00               jne 0x14033ad9d
0033A9D6  89 B4 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], esi
0033A9DD  44 8B E6                        mov r12d, esi
0033A9E0  84 D1                           test cl, dl
0033A9E2  0F 85 92 00 00 00               jne 0x14033aa7a
0033A9E8  44 0F B6 0D B4 B5 AF 00         movzx r9d, byte ptr [rip + 0xafb5b4]
0033A9F0  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
0033A9F5  4D 8B C1                        mov r8, r9
0033A9F8  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
0033A9FD  45 8B EA                        mov r13d, r10d
0033AA00  44 89 94 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r10d
0033AA08  F6 C2 04                        test dl, 4
0033AA0B  0F 84 81 00 00 00               je 0x14033aa92
0033AA11  44 0B E9                        or r13d, ecx
0033AA14  44 89 AC 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r13d
0033AA1C  EB 74                           jmp 0x14033aa92
0033AA1E  49 83 EF 08                     sub r15, 8
0033AA22  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0033AA27  45 8D 66 03                     lea r12d, [r14 + 3]
0033AA2B  41 BD 02 00 00 00               mov r13d, 2
0033AA31  41 83 FC 05                     cmp r12d, 5
0033AA35  41 BB 03 00 00 00               mov r11d, 3
0033AA3B  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
0033AA40  44 0F 4F EE                     cmovg r13d, esi
0033AA44  48 81 C5 00 D0 FF FF            add rbp, -0x3000
0033AA4B  48 C1 ED 09                     shr rbp, 9
0033AA4F  49 23 E8                        and rbp, r8
0033AA52  F6 C2 04                        test dl, 4
0033AA55  0F 85 6E 03 00 00               jne 0x14033adc9
0033AA5B  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0033AA60  49 8B C1                        mov rax, r9
0033AA63  48 03 E8                        add rbp, rax
0033AA66  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0033AA6B  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
0033AA70  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
0033AA75  E9 A7 00 00 00                  jmp 0x14033ab21
0033AA7A  44 8B 0D 07 A6 C8 00            mov r9d, dword ptr [rip + 0xc8a607]
0033AA81  49 C1 E9 0C                     shr r9, 0xc
0033AA85  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
0033AA8A  4D 8B C1                        mov r8, r9
0033AA8D  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
0033AA92  45 8D 59 01                     lea r11d, [r9 + 1]
0033AA96  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0033AAA0  41 8B CB                        mov ecx, r11d
0033AAA3  44 89 9C 24 E0 00 00 00         mov dword ptr [rsp + 0xe0], r11d
0033AAAB  C1 E1 0C                        shl ecx, 0xc
0033AAAE  48 2B E9                        sub rbp, rcx
0033AAB1  48 8B CD                        mov rcx, rbp
0033AAB4  48 C1 E9 09                     shr rcx, 9
0033AAB8  48 23 C8                        and rcx, rax
0033AABB  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0033AAC5  48 8B C0                        mov rax, rax
0033AAC8  48 03 C8                        add rcx, rax
0033AACB  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
0033AAD0  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0033AAD5  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0033AADA  41 84 D2                        test r10b, dl
0033AADD  0F 85 18 03 00 00               jne 0x14033adfb
0033AAE3  4D 8B C1                        mov r8, r9
0033AAE6  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0033AAEB  49 C1 E0 0C                     shl r8, 0xc
0033AAEF  48 8D 8D 00 10 00 00            lea rcx, [rbp + 0x1000]
0033AAF6  40 38 35 6B 41 C9 00            cmp byte ptr [rip + 0xc9416b], sil
0033AAFD  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0033AB02  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
0033AB07  0F 85 26 03 00 00               jne 0x14033ae33
0033AB0D  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
0033AB17  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0033AB21  48 8D 05 D8 E1 AF 00            lea rax, [rip + 0xafe1d8]
0033AB28  48 85 FF                        test rdi, rdi
0033AB2B  0F 84 22 04 00 00               je 0x14033af53
0033AB31  48 8B 87 20 02 00 00            mov rax, qword ptr [rdi + 0x220]
0033AB38  0F B7 88 AE 04 00 00            movzx ecx, word ptr [rax + 0x4ae]
0033AB3F  48 8B 05 42 55 AF 00            mov rax, qword ptr [rip + 0xaf5542]
0033AB46  48 8B 3C C8                     mov rdi, qword ptr [rax + rcx*8]
0033AB4A  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
0033AB4E  48 C1 E9 09                     shr rcx, 9
0033AB52  49 23 C8                        and rcx, r8
0033AB55  49 8B C1                        mov rax, r9
0033AB58  48 03 C8                        add rcx, rax
0033AB5B  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0033AB65  83 7B 04 05                     cmp dword ptr [rbx + 4], 5
0033AB69  48 8D 51 F8                     lea rdx, [rcx - 8]
0033AB6D  48 0F 44 D1                     cmove rdx, rcx
0033AB71  48 8B 4A F8                     mov rcx, qword ptr [rdx - 8]
0033AB75  48 C1 E9 0C                     shr rcx, 0xc
0033AB79  48 23 C8                        and rcx, rax
0033AB7C  E8 4F E1 FF FF                  call 0x140338cd0
0033AB81  89 43 08                        mov dword ptr [rbx + 8], eax
0033AB84  41 F6 C5 01                     test r13b, 1
0033AB88  74 6E                           je 0x14033abf8
0033AB8A  48 8D 05 6F E1 AF 00            lea rax, [rip + 0xafe16f]
0033AB91  48 3B F8                        cmp rdi, rax
0033AB94  75 62                           jne 0x14033abf8
0033AB96  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0033AB9B  48 8B CB                        mov rcx, rbx
0033AB9E  E8 6D DB FF FF                  call 0x140338710
0033ABA3  85 C0                           test eax, eax
0033ABA5  74 51                           je 0x14033abf8
0033ABA7  41 83 FE 05                     cmp r14d, 5
0033ABAB  B8 01 00 00 00                  mov eax, 1
0033ABB0  44 0F 44 E0                     cmove r12d, eax
0033ABB4  8B 43 08                        mov eax, dword ptr [rbx + 8]
0033ABB7  48 69 C8 A8 04 00 00            imul rcx, rax, 0x4a8
0033ABBE  49 63 C4                        movsxd rax, r12d
0033ABC1  48 81 C1 3F 01 00 00            add rcx, 0x13f
0033ABC8  48 03 C8                        add rcx, rax
0033ABCB  48 8D 14 49                     lea rdx, [rcx + rcx*2]
0033ABCF  48 C1 E2 04                     shl rdx, 4
0033ABD3  48 03 57 10                     add rdx, qword ptr [rdi + 0x10]
0033ABD7  8B 42 24                        mov eax, dword ptr [rdx + 0x24]
0033ABDA  83 E8 01                        sub eax, 1
0033ABDD  0F 49 F0                        cmovns esi, eax
0033ABE0  89 72 24                        mov dword ptr [rdx + 0x24], esi
0033ABE3  48 81 C4 88 00 00 00            add rsp, 0x88
0033ABEA  41 5F                           pop r15
0033ABEC  41 5E                           pop r14
0033ABEE  41 5D                           pop r13
0033ABF0  41 5C                           pop r12
0033ABF2  5F                              pop rdi
0033ABF3  5E                              pop rsi
0033ABF4  5D                              pop rbp
0033ABF5  5B                              pop rbx
0033ABF6  C3                              ret
0033ABF7  CC                              int3
0033ABF8  41 F6 C5 02                     test r13b, 2
0033ABFC  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0033AC01  0F 84 56 01 00 00               je 0x14033ad5d
0033AC07  8B 43 08                        mov eax, dword ptr [rbx + 8]
0033AC0A  4C 69 C8 80 DF 00 00            imul r9, rax, 0xdf80
0033AC11  4D 63 C4                        movsxd r8, r12d
0033AC14  8B C6                           mov eax, esi
0033AC16  4C 03 4F 10                     add r9, qword ptr [rdi + 0x10]
0033AC1A  49 8D 90 3F 01 00 00            lea rdx, [r8 + 0x13f]
0033AC21  4F 8D 04 40                     lea r8, [r8 + r8*2]
0033AC25  48 8D 14 52                     lea rdx, [rdx + rdx*2]
0033AC29  48 03 D2                        add rdx, rdx
0033AC2C  41 8B 4C D1 24                  mov ecx, dword ptr [r9 + rdx*8 + 0x24]
0033AC31  83 E9 01                        sub ecx, 1
0033AC34  0F 49 C1                        cmovns eax, ecx
0033AC37  49 81 C0 BD 03 00 00            add r8, 0x3bd
0033AC3E  41 89 44 D1 24                  mov dword ptr [r9 + rdx*8 + 0x24], eax
0033AC43  8B C6                           mov eax, esi
0033AC45  49 C1 E0 04                     shl r8, 4
0033AC49  4D 03 C1                        add r8, r9
0033AC4C  41 8B 48 24                     mov ecx, dword ptr [r8 + 0x24]
0033AC50  83 E9 01                        sub ecx, 1
0033AC53  0F 49 C1                        cmovns eax, ecx
0033AC56  41 89 40 24                     mov dword ptr [r8 + 0x24], eax
0033AC5A  41 8B 50 28                     mov edx, dword ptr [r8 + 0x28]
0033AC5E  8B CE                           mov ecx, esi
0033AC60  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0033AC65  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0033AC6A  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
0033AC6E  4C 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r8
0033AC76  41 8B 44 80 10                  mov eax, dword ptr [r8 + rax*4 + 0x10]
0033AC7B  85 C0                           test eax, eax
0033AC7D  0F 49 C8                        cmovns ecx, eax
0033AC80  41 0F B7 00                     movzx eax, word ptr [r8]
0033AC84  3B D1                           cmp edx, ecx
0033AC86  0F 42 D1                        cmovb edx, ecx
0033AC89  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
0033AC8D  89 8C 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], ecx
0033AC94  3B C2                           cmp eax, edx
0033AC96  0F 83 B3 00 00 00               jae 0x14033ad4f
0033AC9C  41 83 FE 05                     cmp r14d, 5
0033ACA0  0F 85 0F 02 00 00               jne 0x14033aeb5
0033ACA6  49 8B F7                        mov rsi, r15
0033ACA9  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0033ACB3  48 C1 E6 19                     shl rsi, 0x19
0033ACB7  48 8B C0                        mov rax, rax
0033ACBA  48 C1 E0 19                     shl rax, 0x19
0033ACBE  48 2B F0                        sub rsi, rax
0033ACC1  48 C1 FE 10                     sar rsi, 0x10
0033ACC5  48 8B C6                        mov rax, rsi
0033ACC8  48 33 05 31 C9 AF 00            xor rax, qword ptr [rip + 0xafc931]
0033ACCF  48 89 86 E0 0F 00 00            mov qword ptr [rsi + 0xfe0], rax
0033ACD6  44 89 A6 F8 0F 00 00            mov dword ptr [rsi + 0xff8], r12d
0033ACDD  41 83 FC 01                     cmp r12d, 1
0033ACE1  0F 84 00 01 00 00               je 0x14033ade7
0033ACE7  45 0F 20 C4                     mov r12, cr8
0033ACEB  B8 02 00 00 00                  mov eax, 2
0033ACF0  44 0F 22 C0                     mov cr8, rax
0033ACF4  83 3D 25 C0 C8 00 00            cmp dword ptr [rip + 0xc8c025], 0
0033ACFB  0F 85 B7 00 00 00               jne 0x14033adb8
0033AD01  8B 94 24 E8 00 00 00            mov edx, dword ptr [rsp + 0xe8]
0033AD08  49 8B CF                        mov rcx, r15
0033AD0B  E8 80 60 F7 FF                  call 0x1402b0d90
0033AD10  85 C0                           test eax, eax
0033AD12  0F 84 13 03 00 00               je 0x14033b02b
0033AD18  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
0033AD20  48 8D 96 F0 0F 00 00            lea rdx, [rsi + 0xff0]
0033AD27  E8 84 F8 37 00                  call 0x1406ba5b0
0033AD2C  83 3D ED BF C8 00 00            cmp dword ptr [rip + 0xc8bfed], 0
0033AD33  74 0D                           je 0x14033ad42
0033AD35  44 0F 20 C1                     mov rcx, cr8
0033AD39  41 0F B6 D4                     movzx edx, r12b
0033AD3D  E8 56 A9 1B 00                  call 0x1404f5698
0033AD42  41 0F B6 C4                     movzx eax, r12b
0033AD46  44 0F 22 C0                     mov cr8, rax
0033AD4A  E9 94 FE FF FF                  jmp 0x14033abe3
0033AD4F  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0033AD53  41 83 FC 01                     cmp r12d, 1
0033AD57  0F 84 FE 01 00 00               je 0x14033af5b
0033AD5D  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0033AD61  45 8B CE                        mov r9d, r14d
0033AD64  4D 8B C5                        mov r8, r13
0033AD67  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0033AD6C  48 8B D5                        mov rdx, rbp
0033AD6F  48 8B CF                        mov rcx, rdi
0033AD72  E8 C1 EB F9 FF                  call 0x1402d9938
0033AD77  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0033AD7C  41 83 FE 05                     cmp r14d, 5
0033AD80  0F 85 07 01 00 00               jne 0x14033ae8d
0033AD86  48 8D 0D 53 B1 AF 00            lea rcx, [rip + 0xafb153]
0033AD8D  44 8B C0                        mov r8d, eax
0033AD90  48 8B D5                        mov rdx, rbp
0033AD93  E8 A8 C4 F0 FF                  call 0x140247240
0033AD98  E9 46 FE FF FF                  jmp 0x14033abe3
0033AD9D  44 8B 0D 54 BF C8 00            mov r9d, dword ptr [rip + 0xc8bf54]
0033ADA4  45 8B E2                        mov r12d, r10d
0033ADA7  49 C1 E9 0C                     shr r9, 0xc
0033ADAB  44 89 94 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r10d
0033ADB3  E9 38 FC FF FF                  jmp 0x14033a9f0
0033ADB8  0F B6 D0                        movzx edx, al
0033ADBB  41 0F B6 CC                     movzx ecx, r12b
0033ADBF  E8 38 A9 1B 00                  call 0x1404f56fc
0033ADC4  E9 38 FF FF FF                  jmp 0x14033ad01
0033ADC9  41 83 FC 05                     cmp r12d, 5
0033ADCD  75 03                           jne 0x14033add2
0033ADCF  44 0B E9                        or r13d, ecx
0033ADD2  49 8B C1                        mov rax, r9
0033ADD5  48 03 E8                        add rbp, rax
0033ADD8  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0033ADDD  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
0033ADE2  E9 3A FD FF FF                  jmp 0x14033ab21
0033ADE7  48 8D 96 F0 0F 00 00            lea rdx, [rsi + 0xff0]
0033ADEE  49 8B C8                        mov rcx, r8
0033ADF1  E8 BA F7 37 00                  call 0x1406ba5b0
0033ADF6  E9 E8 FD FF FF                  jmp 0x14033abe3
0033ADFB  8B 05 03 BD C8 00               mov eax, dword ptr [rip + 0xc8bd03]
0033AE01  A8 01                           test al, 1
0033AE03  0F 84 DA FC FF FF               je 0x14033aae3
0033AE09  48 8D 8D 00 10 00 00            lea rcx, [rbp + 0x1000]
0033AE10  45 33 C0                        xor r8d, r8d
0033AE13  49 8B D1                        mov rdx, r9
0033AE16  E8 2D BA 19 00                  call 0x1404d6848
0033AE1B  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
0033AE20  41 BA 02 00 00 00               mov r10d, 2
0033AE26  44 8B 9C 24 E0 00 00 00         mov r11d, dword ptr [rsp + 0xe0]
0033AE2E  E9 B0 FC FF FF                  jmp 0x14033aae3
0033AE33  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0033AE3D  48 3B C8                        cmp rcx, rax
0033AE40  72 57                           jb 0x14033ae99
0033AE42  F6 C1 07                        test cl, 7
0033AE45  0F 84 2D 01 00 00               je 0x14033af78
0033AE4B  4C 8B C9                        mov r9, rcx
0033AE4E  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
0033AE57  B9 F1 01 00 00                  mov ecx, 0x1f1
0033AE5C  4D 8B C2                        mov r8, r10
0033AE5F  49 8B D2                        mov rdx, r10
0033AE62  E8 F9 27 1C 00                  call 0x1404fd660
0033AE67  CC                              int3
0033AE68  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0033AE6C  45 8B CE                        mov r9d, r14d
0033AE6F  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0033AE74  48 8B CF                        mov rcx, rdi
0033AE77  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0033AE7C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0033AE81  E8 B2 EA F9 FF                  call 0x1402d9938
0033AE86  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
0033AE8D  48 8D 0D AC B0 AF 00            lea rcx, [rip + 0xafb0ac]
0033AE94  E9 F4 FE FF FF                  jmp 0x14033ad8d
0033AE99  4C 8B C9                        mov r9, rcx
0033AE9C  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0033AEA1  B9 F1 01 00 00                  mov ecx, 0x1f1
0033AEA6  41 B8 01 00 00 00               mov r8d, 1
0033AEAC  49 8B D2                        mov rdx, r10
0033AEAF  E8 AC 27 1C 00                  call 0x1404fd660
0033AEB4  CC                              int3
0033AEB5  48 8D 8F C0 01 00 00            lea rcx, [rdi + 0x1c0]
0033AEBC  E8 AF F6 37 00                  call 0x1406ba570
0033AEC1  4C 8B E8                        mov r13, rax
0033AEC4  48 85 C0                        test rax, rax
0033AEC7  74 9F                           je 0x14033ae68
0033AEC9  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
0033AECD  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
0033AED5  89 B4 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], esi
0033AEDC  48 89 B4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rsi
0033AEE4  41 83 FC 05                     cmp r12d, 5
0033AEE8  75 47                           jne 0x14033af31
0033AEEA  49 89 4D 10                     mov qword ptr [r13 + 0x10], rcx
0033AEEE  49 8D 57 08                     lea rdx, [r15 + 8]
0033AEF2  48 8D 4D 08                     lea rcx, [rbp + 8]
0033AEF6  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
0033AEFE  4C 8D 84 24 E8 00 00 00         lea r8, [rsp + 0xe8]
0033AF06  E8 25 94 14 00                  call 0x140484330
0033AF0B  48 8B BC 24 E0 00 00 00         mov rdi, qword ptr [rsp + 0xe0]
0033AF13  49 8B D5                        mov rdx, r13
0033AF16  48 8B CF                        mov rcx, rdi
0033AF19  8B D8                           mov ebx, eax
0033AF1B  E8 90 F6 37 00                  call 0x1406ba5b0
0033AF20  85 DB                           test ebx, ebx
0033AF22  0F 84 BB FC FF FF               je 0x14033abe3
0033AF28  C6 47 2C 01                     mov byte ptr [rdi + 0x2c], 1
0033AF2C  E9 B2 FC FF FF                  jmp 0x14033abe3
0033AF31  48 8D 94 24 D8 00 00 00         lea rdx, [rsp + 0xd8]
0033AF39  41 8B CE                        mov ecx, r14d
0033AF3C  E8 3B A8 72 00                  call 0x140a6577c
0033AF41  85 C0                           test eax, eax
0033AF43  0F 88 02 01 00 00               js 0x14033b04b
0033AF49  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0033AF51  EB 97                           jmp 0x14033aeea
0033AF53  48 8B F8                        mov rdi, rax
0033AF56  E9 EF FB FF FF                  jmp 0x14033ab4a
0033AF5B  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0033AF60  4D 8D 81 D0 3B 00 00            lea r8, [r9 + 0x3bd0]
0033AF67  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0033AF6C  44 8B E6                        mov r12d, esi
0033AF6F  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0033AF73  E9 E2 FC FF FF                  jmp 0x14033ac5a
0033AF78  4A 8D 04 01                     lea rax, [rcx + r8]
0033AF7C  48 3B C1                        cmp rax, rcx
0033AF7F  73 1C                           jae 0x14033af9d
0033AF81  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0033AF86  4C 8B C9                        mov r9, rcx
0033AF89  41 B8 03 00 00 00               mov r8d, 3
0033AF8F  B9 F1 01 00 00                  mov ecx, 0x1f1
0033AF94  49 8B D2                        mov rdx, r10
0033AF97  E8 C4 26 1C 00                  call 0x1404fd660
0033AF9C  CC                              int3
0033AF9D  8B AC 24 D0 00 00 00            mov ebp, dword ptr [rsp + 0xd0]
0033AFA4  48 B8 00 00 00 00 00 80 00 00   movabs rax, 0x800000000000
0033AFAE  44 8B A4 24 D8 00 00 00         mov r12d, dword ptr [rsp + 0xd8]
0033AFB6  48 03 C8                        add rcx, rax
0033AFB9  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0033AFBE  44 8B ED                        mov r13d, ebp
0033AFC1  48 C1 E9 03                     shr rcx, 3
0033AFC5  48 03 0D 0C BF C8 00            add rcx, qword ptr [rip + 0xc8bf0c]
0033AFCC  49 C1 E8 03                     shr r8, 3
0033AFD0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0033AFD5  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0033AFDA  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
0033AFDF  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
0033AFE4  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0033AFE9  4D 85 C0                        test r8, r8
0033AFEC  75 08                           jne 0x14033aff6
0033AFEE  48 8B E8                        mov rbp, rax
0033AFF1  E9 17 FB FF FF                  jmp 0x14033ab0d
0033AFF6  33 D2                           xor edx, edx
0033AFF8  E8 43 BC 38 00                  call 0x1406c6c40
0033AFFD  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0033B002  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0033B007  8B 8C 24 E0 00 00 00            mov ecx, dword ptr [rsp + 0xe0]
0033B00E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0033B013  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0033B018  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0033B01D  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0033B021  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
0033B026  E9 E2 FA FF FF                  jmp 0x14033ab0d
0033B02B  83 3D EE BC C8 00 00            cmp dword ptr [rip + 0xc8bcee], 0
0033B032  0F 84 B4 6F 3A 00               je 0x1406e1fec
0033B038  44 0F 20 C1                     mov rcx, cr8
0033B03C  41 0F B6 D4                     movzx edx, r12b
0033B040  E8 53 A6 1B 00                  call 0x1404f5698
0033B045  90                              nop
0033B046  E9 A1 6F 3A 00                  jmp 0x1406e1fec
0033B04B  4C 63 C8                        movsxd r9, eax
0033B04E  4C 8B C5                        mov r8, rbp
0033B051  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0033B059  BA 42 15 05 00                  mov edx, 0x51542
0033B05E  B9 1A 00 00 00                  mov ecx, 0x1a
0033B063  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0033B068  E8 F3 25 1C 00                  call 0x1404fd660
0033B06D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmDeleteKernelStack(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p8;
    unsigned int v_stack_pD0;
    unsigned int v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned int v_stack_pE8;

    v_rsp = (v_rsp) - (136);
    v_rsi = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    a1 = (*(unsigned __int64 *)(a1 + 24)) >> (9);
    a1 = (a1) & (a3);
    v_stack_p8 = 0;
    v_r15 = (a4 - 8) + (a1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) != 5) goto loc_0033AA1E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (8)) != 0) goto loc_0033AD9D;
    v_stack_p10 = 0;
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1))))) != 0) goto loc_0033AA7A;
loc_0033A9F0:
    v_stack_m98 = *(unsigned __int8 *)(v_rip + 11515316);
    v_stack_m78 = *(unsigned __int8 *)(v_rip + 11515316);
    v_stack_p8 = (unsigned int)(v_rsi + 2);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (4)) == 0) goto loc_0033AA92;
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi + 2))) | ((unsigned int)(v_rsi + 1)));
    v_stack_p8 = (unsigned int)(v_r13);
    goto loc_0033AA92;
loc_0033AA1E:
    v_r15 = (v_r15) - (8);
    v_stack_m80 = v_rsi + 1;
    v_stack_m88 = 3;
    v_r13 = 2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) + 3)) > 5) { v_r13 = 0; }
    v_rbp = (*(unsigned __int64 *)(a1 + 24)) + (0xFFFFFFFFFFFFD000ULL);
    v_rbp = (v_rbp) >> (9);
    v_rbp = (v_rbp) & (*(unsigned __int8 *)(v_rip + 11515316));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (4)) != 0) goto loc_0033ADC9;
    v_stack_m98 = v_rsi + 1;
    v_rbp = (v_rbp) + (*(unsigned __int8 *)(v_rip + 11515316));
    v_stack_m80 = v_rsi + 1;
    v_stack_m90 = v_rbp;
    v_stack_m88 = 3;
    goto loc_0033AB21;
loc_0033AA7A:
    a4 = ((unsigned int)(*(unsigned int *)(v_rip + 13149703))) >> (12);
    v_stack_m78 = a4;
    v_stack_m98 = a4;
loc_0033AA92:
    v_stack_p18 = (unsigned int)(a4 + 1);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a4 + 1))) << (12));
    v_rbp = (v_rbp) - (a1);
    a1 = (v_rbp) >> (9);
    a1 = (a1) & (*(unsigned __int8 *)(v_rip + 11515316));
    a1 = (a1) + (*(unsigned __int8 *)(v_rip + 11515316));
    v_stack_m68 = a4;
    v_stack_m90 = a1;
    v_stack_m60 = a1;
    if ((((unsigned __int8)(v_rsi + 2)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1))))) != 0) goto loc_0033ADFB;
loc_0033AAE3:
    v_stack_m80 = a4;
    a3 = (a4) << (12);
    v_stack_m88 = (unsigned int)(a4 + 1);
    if ((*(unsigned __int8 *)(v_rip + 13189483)) != 0) goto loc_0033AE33;
loc_0033AB0D:
loc_0033AB21:
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_0033AF53;
loc_0033AB4A:
    a1 = (*(unsigned __int64 *)(a1 + 24)) >> (9);
    a1 = (a1) & (a3);
    a1 = (a1) + (a4);
    a2 = a1 - 8;
    if ((*(unsigned int *)(a1 + 4)) == 5) { a2 = a1; }
    a1 = (*(unsigned __int64 *)(a2 - 8)) >> (12);
    a1 = (a1) & (a4);
    result = MiPageToNode(a1, a2, a3, a4);
    *(unsigned int *)(a1 + 8) = (unsigned int)(result);
    if ((((unsigned __int8)(v_r13)) & (1)) == 0) goto loc_0033ABF8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11490626) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 544) + 1198) * 8)) != (v_rip + 11526511)) goto loc_0033ABF8;
    result = MiAddKernelStackToPrcbCache(a1, v_stack_m80, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0033ABF8;
    v_r12 = (unsigned int)(*(unsigned int *)(a1 + 4)) + 3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) == 5) { v_r12 = 1; }
    a1 = (a1) * ((unsigned int)(*(unsigned int *)(a1 + 8)));
    a1 = (a1) + (319);
    a1 = (a1) + ((int)((unsigned int)(v_r12)));
    a2 = (a1 + a1 * 2) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11490626) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 544) + 1198) * 8) + 16));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 36))) - (1));
    if (!sign_flag) { v_rsi = (unsigned int)(result); }
    *(unsigned int *)(a2 + 36) = (unsigned int)(v_rsi);
loc_0033ABE3:
    v_rsp = (v_rsp) + (136);
    return result;
loc_0033ABF8:
    if ((((unsigned __int8)(v_r13)) & (2)) == 0) goto loc_0033AD5D;
    a4 = (a4) * ((unsigned int)(*(unsigned int *)(a1 + 8)));
    a4 = (a4) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11490626) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 544) + 1198) * 8) + 16));
    a2 = ((int)((unsigned int)(v_r12)) + 319 + (int)((unsigned int)(v_r12)) + 319 * 2) + ((int)((unsigned int)(v_r12)) + 319 + (int)((unsigned int)(v_r12)) + 319 * 2);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + a2 * 8 + 36))) - (1));
    result = (unsigned int)((unsigned int)(v_rsi));
    if (!sign_flag) { result = (unsigned int)(a1); }
    a3 = ((int)((unsigned int)(v_r12)) + (int)((unsigned int)(v_r12)) * 2) + (957);
    *(unsigned int *)(a4 + a2 * 8 + 36) = (unsigned int)(result);
    a3 = (a3) << (4);
    a3 = (a3) + (a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 36))) - (1));
    result = (unsigned int)((unsigned int)(v_rsi));
    if (!sign_flag) { result = (unsigned int)(a1); }
    *(unsigned int *)(a3 + 36) = (unsigned int)(result);
loc_0033AC5A:
    v_stack_p30 = v_stack_p30;
    v_stack_pE0 = a3;
    a1 = (unsigned int)((unsigned int)(v_rsi));
    if (!sign_flag) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + (unsigned int)(*(unsigned int *)(a3 + 32)) * 4 + 16))); }
    a2 = (unsigned int)(*(unsigned int *)(a3 + 40));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 40)))) < ((unsigned int)(a1))) { a2 = (unsigned int)(a1); }
    v_stack_pD0 = (unsigned int)((unsigned int)(v_stack_p40));
    if (((unsigned int)(*(unsigned __int16 *)(a3))) >= ((unsigned int)(a2))) goto loc_0033AD4F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) != 5) goto loc_0033AEB5;
    v_rsi = (v_r15) << (25);
    result = (*(unsigned __int16 *)(a3)) << (25);
    v_rsi = (v_rsi) - (result);
    v_rsi = (v_rsi) >> (16);
    result = (v_rsi) ^ (*(unsigned __int64 *)(v_rip + 11520305));
    *(unsigned __int64 *)(v_rsi + 4064) = result;
    *(unsigned int *)(v_rsi + 4088) = (unsigned int)(v_r12);
    if (((unsigned int)(v_r12)) == 1) goto loc_0033ADE7;
    if ((*(unsigned int *)(v_rip + 13156389)) != 0) goto loc_0033ADB8;
loc_0033AD01:
    result = MiClearStackOwners(v_r15, (unsigned int)(v_stack_pE8), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0033B02B;
    result = ExpInterlockedPushEntrySList(v_stack_pE0, v_rsi + 4080, a3, a4);
    if ((*(unsigned int *)(v_rip + 13156333)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    goto loc_0033ABE3;
loc_0033AD4F:
    v_stack_p40 = (unsigned int)(a1);
    if (((unsigned int)(v_cr8)) == 1) goto loc_0033AF5B;
loc_0033AD5D:
    v_stack_p20 = *(unsigned __int64 *)(a1 + 40);
    result = MiDeleteKernelStackPages(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11490626) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 544) + 1198) * 8), v_stack_m90, v_stack_p48, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) != 5) goto loc_0033AE8D;
loc_0033AD8D:
    result = MiReleasePtes(v_rip + 11514195, v_stack_m90, (unsigned int)((unsigned int)(v_stack_p40)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    goto loc_0033ABE3;
loc_0033AD9D:
    a4 = ((unsigned int)(*(unsigned int *)(v_rip + 13156180))) >> (12);
    v_stack_pD8 = (unsigned int)(v_rsi + 2);
    goto loc_0033A9F0;
loc_0033ADB8:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned int)((unsigned int)(v_rsi + 2))), (unsigned __int8)(result), (unsigned int)((unsigned int)(v_stack_p40)), a4);
    goto loc_0033AD01;
loc_0033ADC9:
    v_r13 = v_stack_p48;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi + 2)))) == 5) {
        v_r13 = (unsigned int)((v_stack_p48) | ((unsigned int)((unsigned __int8)((unsigned int)((unsigned int)(v_rsi + 2))))));
    }
    v_rbp = (v_stack_m90) + (a4);
    v_stack_p30 = (unsigned __int8)((unsigned int)((unsigned int)(v_rsi + 2)));
    v_stack_p38 = v_rbp;
    goto loc_0033AB21;
loc_0033ADE7:
    result = ExpInterlockedPushEntrySList((unsigned int)((unsigned int)(v_stack_p40)), v_rsi + 4080, (unsigned int)((unsigned int)(v_stack_p40)), a4);
    goto loc_0033ABE3;
loc_0033ADFB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13155587)))) & (1)) == 0) goto loc_0033AAE3;
    a3 = 0;
    result = MiLogKernelStackEvent(v_rbp + 4096, a4, a3, a4);
    goto loc_0033AAE3;
loc_0033AE33:
    if ((v_rbp + 4096) < result) goto loc_0033AE99;
    if ((((unsigned __int8)(v_rbp + 4096)) & (7)) == 0) goto loc_0033AF78;
    v_stack_p20 = 8;
    result = KeBugCheckEx(497, 2, 2, v_rbp + 4096);
loc_0033AE68:
    v_stack_p20 = *(unsigned __int64 *)(a1 + 40);
    result = MiDeleteKernelStackPages(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11490626) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 544) + 1198) * 8), v_stack_p38, v_stack_p30, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
loc_0033AE8D:
    goto loc_0033AD8D;
loc_0033AE99:
    v_stack_p20 = v_rsi;
    result = KeBugCheckEx(497, 2, 1, v_rip + 11514028);
loc_0033AEB5:
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11490626) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 544) + 1198) * 8) + 448, 2, 1, v_rip + 11514028);
    if (result == 0) goto loc_0033AE68;
    v_stack_pD8 = *(unsigned __int64 *)(a1 + 40);
    v_stack_pD0 = (unsigned int)(v_rsi);
    v_stack_pE8 = v_rsi;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi + 2)))) != 5) goto loc_0033AF31;
loc_0033AEEA:
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(a1 + 40);
    result = MiKernelShadowStackIdealForCaching(v_rbp + 8, v_r15 + 8, v_stack_pE8, v_stack_pD0);
    result = ExpInterlockedPushEntrySList(v_stack_pE0, result, v_stack_pE8, v_stack_pD0);
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_0033ABE3;
    *(unsigned __int8 *)(v_stack_pE0 + 44) = 1;
    goto loc_0033ABE3;
loc_0033AF31:
    result = VslResetKernelShadowStack((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))), v_stack_pD8, v_stack_pE8, v_stack_pD0);
    if (sign_flag) goto loc_0033B04B;
    goto loc_0033AEEA;
loc_0033AF53:
    goto loc_0033AB4A;
loc_0033AF5B:
    v_stack_p38 = v_stack_p38;
    v_stack_p40 = (unsigned int)(v_stack_pD8);
    goto loc_0033AC5A;
loc_0033AF78:
    result = v_stack_pD8 + v_stack_pD0 + 15312 * 1;
    if ((v_stack_pD8 + v_stack_pD0 + 15312 * 1) < v_stack_pD8) {
        v_stack_p20 = v_stack_pD0 + 15312;
        a4 = v_stack_pD8;
        a3 = 3;
        a1 = 497;
        a2 = 2;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = (a1) + (result);
    a1 = (a1) >> (3);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 13156108));
    a3 = (a3) >> (3);
    v_stack_p30 = v_stack_p60;
    v_stack_p48 = a4;
    v_stack_p40 = (unsigned int)((unsigned int)(v_stack_pE0));
    v_stack_p38 = v_stack_p68;
    if (a3 != 0) goto loc_0033AFF6;
    goto loc_0033AB0D;
loc_0033AFF6:
    a2 = 0;
    result = memset(a1, a2, a3, a4);
    v_stack_p48 = v_stack_p50;
    v_stack_p30 = v_stack_p60;
    v_stack_p40 = (unsigned int)((unsigned int)(v_stack_pE0));
    v_stack_p38 = v_stack_p68;
    goto loc_0033AB0D;
loc_0033B02B:
    result = KiLowerIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), (unsigned __int8)((unsigned int)(v_stack_pD8)), a3, a4);
loc_0033B04B:
    v_stack_p20 = v_stack_pD8;
    result = KeBugCheckEx(26, (unsigned int)(0x51542ULL), v_stack_p68, (int)((unsigned int)(result)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmDeleteKernelStack(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p8;
    uint32_t v_stack_pD0;
    uint32_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint32_t v_stack_pE8;

    local_rsp = (local_rsp) - (136);
    local_rsi = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    Arg1 = (*(uint64_t *)(arg1 + 0x18)) >> (9);
    Arg1 = (Arg1) & (a3);
    v_stack_p8 = 0;
    local_r15 = (a4 - 8) + (Arg1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) != 5) goto loc_0033AA1E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (8)) != 0) goto loc_0033AD9D;
    v_stack_p10 = 0;
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1))))) != 0) goto loc_0033AA7A;
loc_0033A9F0:
    v_stack_m98 = *(uint8_t *)(v_rip + 0xAFB5B4);
    v_stack_m78 = *(uint8_t *)(v_rip + 0xAFB5B4);
    v_stack_p8 = (uint32_t)(local_rsi + 2);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (4)) == 0) goto loc_0033AA92;
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi + 2))) | ((uint32_t)(local_rsi + 1)));
    v_stack_p8 = (uint32_t)(local_r13);
    goto loc_0033AA92;
loc_0033AA1E:
    local_r15 = (local_r15) - (8);
    v_stack_m80 = local_rsi + 1;
    v_stack_m88 = 3;
    local_r13 = 2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) + 3)) > 5) { local_r13 = 0; }
    local_rbp = (*(uint64_t *)(arg1 + 0x18)) + (0xFFFFFFFFFFFFD000ULL);
    local_rbp = (local_rbp) >> (9);
    local_rbp = (local_rbp) & (*(uint8_t *)(v_rip + 0xAFB5B4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (4)) != 0) goto loc_0033ADC9;
    v_stack_m98 = local_rsi + 1;
    local_rbp = (local_rbp) + (*(uint8_t *)(v_rip + 0xAFB5B4));
    v_stack_m80 = local_rsi + 1;
    v_stack_m90 = local_rbp;
    v_stack_m88 = 3;
    goto loc_0033AB21;
loc_0033AA7A:
    a4 = ((uint32_t)(*(uint32_t *)(v_rip + 0xC8A607))) >> (12);
    v_stack_m78 = a4;
    v_stack_m98 = a4;
loc_0033AA92:
    v_stack_p18 = (uint32_t)(a4 + 1);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(a4 + 1))) << (12));
    local_rbp = (local_rbp) - (Arg1);
    Arg1 = (local_rbp) >> (9);
    Arg1 = (Arg1) & (*(uint8_t *)(v_rip + 0xAFB5B4));
    Arg1 = (Arg1) + (*(uint8_t *)(v_rip + 0xAFB5B4));
    v_stack_m68 = a4;
    v_stack_m90 = Arg1;
    v_stack_m60 = Arg1;
    if ((((uint8_t)(local_rsi + 2)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1))))) != 0) goto loc_0033ADFB;
loc_0033AAE3:
    v_stack_m80 = a4;
    a3 = (a4) << (12);
    v_stack_m88 = (uint32_t)(a4 + 1);
    if ((*(uint8_t *)(v_rip + 0xC9416B)) != 0) goto loc_0033AE33;
loc_0033AB0D:
loc_0033AB21:
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_0033AF53;
loc_0033AB4A:
    Arg1 = (*(uint64_t *)(arg1 + 0x18)) >> (9);
    Arg1 = (Arg1) & (a3);
    Arg1 = (Arg1) + (a4);
    a2 = Arg1 - 8;
    if ((*(uint32_t *)(arg1 + 0x4)) == 5) { a2 = Arg1; }
    Arg1 = (*(uint64_t *)(a2 - 0x8)) >> (12);
    Arg1 = (Arg1) & (a4);
    result = MiPageToNode(Arg1, a2, a3, a4);
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(result);
    if ((((uint8_t)(local_r13)) & (1)) == 0) goto loc_0033ABF8;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF5542) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x220) + 0x4AE) * 8)) != (v_rip + 11526511)) goto loc_0033ABF8;
    result = MiAddKernelStackToPrcbCache(Arg1, v_stack_m80, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0033ABF8;
    local_r12 = (uint32_t)(*(uint32_t *)(arg1 + 0x4)) + 3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) == 5) { local_r12 = 1; }
    Arg1 = (Arg1) * ((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    Arg1 = (Arg1) + (319);
    Arg1 = (Arg1) + ((int32_t)((uint32_t)(local_r12)));
    a2 = (Arg1 + Arg1 * 2) << (4);
    a2 = (a2) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF5542) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x220) + 0x4AE) * 8) + 0x10));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(a2 + 0x24))) - (1));
    if (!sign_flag) { local_rsi = (uint32_t)(result); }
    *(uint32_t *)(a2 + 0x24) = (uint32_t)(local_rsi);
loc_0033ABE3:
    local_rsp = (local_rsp) + (136);
    return result;
loc_0033ABF8:
    if ((((uint8_t)(local_r13)) & (2)) == 0) goto loc_0033AD5D;
    a4 = (a4) * ((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    a4 = (a4) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF5542) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x220) + 0x4AE) * 8) + 0x10));
    a2 = ((int32_t)((uint32_t)(local_r12)) + 319 + (int32_t)((uint32_t)(local_r12)) + 319 * 2) + ((int32_t)((uint32_t)(local_r12)) + 319 + (int32_t)((uint32_t)(local_r12)) + 319 * 2);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(a4 + a2 * 8 + 0x24))) - (1));
    result = (uint32_t)((uint32_t)(local_rsi));
    if (!sign_flag) { result = (uint32_t)(Arg1); }
    a3 = ((int32_t)((uint32_t)(local_r12)) + (int32_t)((uint32_t)(local_r12)) * 2) + (957);
    *(uint32_t *)(a4 + a2 * 8 + 0x24) = (uint32_t)(result);
    a3 = (a3) << (4);
    a3 = (a3) + (a4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(a3 + 0x24))) - (1));
    result = (uint32_t)((uint32_t)(local_rsi));
    if (!sign_flag) { result = (uint32_t)(Arg1); }
    *(uint32_t *)(a3 + 0x24) = (uint32_t)(result);
loc_0033AC5A:
    v_stack_p30 = v_stack_p30;
    v_stack_pE0 = a3;
    Arg1 = (uint32_t)((uint32_t)(local_rsi));
    if (!sign_flag) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(a3 + (uint32_t)(*(uint32_t *)(a3 + 0x20)) * 4 + 0x10))); }
    a2 = (uint32_t)(*(uint32_t *)(a3 + 0x28));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a3 + 0x28)))) < ((uint32_t)(Arg1))) { a2 = (uint32_t)(Arg1); }
    v_stack_pD0 = (uint32_t)((uint32_t)(v_stack_p40));
    if (((uint32_t)(*(uint16_t *)(a3))) >= ((uint32_t)(a2))) goto loc_0033AD4F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) != 5) goto loc_0033AEB5;
    local_rsi = (local_r15) << (25);
    result = (*(uint16_t *)(a3)) << (25);
    local_rsi = (local_rsi) - (result);
    local_rsi = (local_rsi) >> (16);
    result = (local_rsi) ^ (*(uint64_t *)(v_rip + 0xAFC931));
    *(uint64_t *)(local_rsi + 0xFE0) = result;
    *(uint32_t *)(local_rsi + 0xFF8) = (uint32_t)(local_r12);
    if (((uint32_t)(local_r12)) == 1) goto loc_0033ADE7;
    if ((*(uint32_t *)(v_rip + 0xC8C025)) != 0) goto loc_0033ADB8;
loc_0033AD01:
    result = MiClearStackOwners(local_r15, (uint32_t)(v_stack_pE8), a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0033B02B;
    result = ExpInterlockedPushEntrySList(v_stack_pE0, local_rsi + 4080, a3, a4);
    if ((*(uint32_t *)(v_rip + 0xC8BFED)) != 0) {
        Arg1 = 2;
        a2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, a3, a4);
    }
    goto loc_0033ABE3;
loc_0033AD4F:
    v_stack_p40 = (uint32_t)(Arg1);
    if (((uint32_t)(v_cr8)) == 1) goto loc_0033AF5B;
loc_0033AD5D:
    v_stack_p20 = *(uint64_t *)(arg1 + 0x28);
    result = MiDeleteKernelStackPages(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF5542) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x220) + 0x4AE) * 8), v_stack_m90, v_stack_p48, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) != 5) goto loc_0033AE8D;
loc_0033AD8D:
    result = MiReleasePtes(v_rip + 11514195, v_stack_m90, (uint32_t)((uint32_t)(v_stack_p40)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
    goto loc_0033ABE3;
loc_0033AD9D:
    a4 = ((uint32_t)(*(uint32_t *)(v_rip + 0xC8BF54))) >> (12);
    v_stack_pD8 = (uint32_t)(local_rsi + 2);
    goto loc_0033A9F0;
loc_0033ADB8:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint32_t)((uint32_t)(local_rsi + 2))), (uint8_t)(result), (uint32_t)((uint32_t)(v_stack_p40)), a4);
    goto loc_0033AD01;
loc_0033ADC9:
    local_r13 = v_stack_p48;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi + 2)))) == 5) {
        local_r13 = (uint32_t)((v_stack_p48) | ((uint32_t)((uint8_t)((uint32_t)((uint32_t)(local_rsi + 2))))));
    }
    local_rbp = (v_stack_m90) + (a4);
    v_stack_p30 = (uint8_t)((uint32_t)((uint32_t)(local_rsi + 2)));
    v_stack_p38 = local_rbp;
    goto loc_0033AB21;
loc_0033ADE7:
    result = ExpInterlockedPushEntrySList((uint32_t)((uint32_t)(v_stack_p40)), local_rsi + 4080, (uint32_t)((uint32_t)(v_stack_p40)), a4);
    goto loc_0033ABE3;
loc_0033ADFB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8BD03)))) & (1)) == 0) goto loc_0033AAE3;
    a3 = 0;
    result = MiLogKernelStackEvent(local_rbp + 4096, a4, a3, a4);
    goto loc_0033AAE3;
loc_0033AE33:
    if ((local_rbp + 4096) < result) goto loc_0033AE99;
    if ((((uint8_t)(local_rbp + 4096)) & (7)) == 0) goto loc_0033AF78;
    v_stack_p20 = 8;
    result = KeBugCheckEx(497, 2, 2, local_rbp + 4096);
loc_0033AE68:
    v_stack_p20 = *(uint64_t *)(arg1 + 0x28);
    result = MiDeleteKernelStackPages(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF5542) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x220) + 0x4AE) * 8), v_stack_p38, v_stack_p30, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
loc_0033AE8D:
    goto loc_0033AD8D;
loc_0033AE99:
    v_stack_p20 = local_rsi;
    result = KeBugCheckEx(497, 2, 1, v_rip + 11514028);
loc_0033AEB5:
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF5542) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x220) + 0x4AE) * 8) + 448, 2, 1, v_rip + 11514028);
    if (result == 0) goto loc_0033AE68;
    v_stack_pD8 = *(uint64_t *)(arg1 + 0x28);
    v_stack_pD0 = (uint32_t)(local_rsi);
    v_stack_pE8 = local_rsi;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi + 2)))) != 5) goto loc_0033AF31;
loc_0033AEEA:
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(arg1 + 0x28);
    result = MiKernelShadowStackIdealForCaching(local_rbp + 8, local_r15 + 8, v_stack_pE8, v_stack_pD0);
    result = ExpInterlockedPushEntrySList(v_stack_pE0, result, v_stack_pE8, v_stack_pD0);
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_0033ABE3;
    *(uint8_t *)(v_stack_pE0 + 0x2C) = 1;
    goto loc_0033ABE3;
loc_0033AF31:
    result = VslResetKernelShadowStack((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))), v_stack_pD8, v_stack_pE8, v_stack_pD0);
    if (sign_flag) goto loc_0033B04B;
    goto loc_0033AEEA;
loc_0033AF53:
    goto loc_0033AB4A;
loc_0033AF5B:
    v_stack_p38 = v_stack_p38;
    v_stack_p40 = (uint32_t)(v_stack_pD8);
    goto loc_0033AC5A;
loc_0033AF78:
    result = v_stack_pD8 + v_stack_pD0 + 15312 * 1;
    if ((v_stack_pD8 + v_stack_pD0 + 15312 * 1) < v_stack_pD8) {
        v_stack_p20 = v_stack_pD0 + 15312;
        a4 = v_stack_pD8;
        a3 = 3;
        Arg1 = 497;
        a2 = 2;
        result = KeBugCheckEx(Arg1, a2, a3, a4);
    }
    Arg1 = (Arg1) + (result);
    Arg1 = (Arg1) >> (3);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xC8BF0C));
    a3 = (a3) >> (3);
    v_stack_p30 = v_stack_p60;
    v_stack_p48 = a4;
    v_stack_p40 = (uint32_t)((uint32_t)(v_stack_pE0));
    v_stack_p38 = v_stack_p68;
    if (a3 != 0) goto loc_0033AFF6;
    goto loc_0033AB0D;
loc_0033AFF6:
    a2 = 0;
    result = memset(Arg1, a2, a3, a4);
    v_stack_p48 = v_stack_p50;
    v_stack_p30 = v_stack_p60;
    v_stack_p40 = (uint32_t)((uint32_t)(v_stack_pE0));
    v_stack_p38 = v_stack_p68;
    goto loc_0033AB0D;
loc_0033B02B:
    result = KiLowerIrqlProcessIrqlFlags((uint8_t)(v_cr8), (uint8_t)((uint32_t)(v_stack_pD8)), a3, a4);
loc_0033B04B:
    v_stack_p20 = v_stack_pD8;
    result = KeBugCheckEx(26, (uint32_t)(0x51542ULL), v_stack_p68, (int32_t)((uint32_t)(result)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033A960&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
