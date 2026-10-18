# MiResolveTransitionFault

- RVA: `0x00282940`–`0x002837F9` (길이 `3,769` bytes)
- VA: `0x0000000140282940`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00066848`
- 디코드: `855`개 명령, `3,769/3,769` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00282AB2` → [MiHandleTransitionFault](MiHandleTransitionFault_function_00283800.md) (function, `0x00283800`)
- `0x00282AF7` → [MI_READ_PTE_LOCK_FREE](MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00282B0D` → [MiUpdateProtectionMask](MiUpdateProtectionMask_function_002845DC.md) (function, `0x002845DC`)
- `0x00282B2E` → [MiMakeTransitionPteValid](MiMakeTransitionPteValid_function_00283D60.md) (function, `0x00283D60`)
- `0x00282BAE` → [MI_READ_PTE_LOCK_FREE](MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00282BC2` → [MiWriteValidPteNewProtection](MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x00282D0C` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x00282D36` → [MiReleasePageFileInfo](MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x00282D98` → [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) (function, `0x00345710`)
- `0x00282E13` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00282E99` → [MI_READ_PTE_LOCK_FREE](MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00282F40` → [MI_READ_PTE_LOCK_FREE](MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00282F9F` → [MI_READ_PTE_LOCK_FREE](MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00283074` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x002830FD` → [MiEmptyDeferredWorkingSetEntries](../34/MiEmptyDeferredWorkingSetEntries_function_00347910.md) (function, `0x00347910`)
- `0x0028315A` → [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) (function, `0x003332C0`)
- `0x00283179` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x0028320E` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x0028336D` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002833BF` → [MiIsDecayPfn](../2B/MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x002833DF` → [MiGetPfnSlabType](MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x002834CE` → [MiRelinkStandbyPage](../2B/MiRelinkStandbyPage_function_002B9D30.md) (function, `0x002B9D30`)
- `0x00283519` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00283529` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00283536` → [MiCheckWriteInProgressFault](../48/MiCheckWriteInProgressFault_function_0048DDA8.md) (function, `0x0048DDA8`)
- `0x00283577` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0028358B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028359B` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002835CF` → [MiHandleCollidedFault](../36/MiHandleCollidedFault_function_00369B48.md) (function, `0x00369B48`)
- `0x00283607` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x00283646` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x0028365B` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x002836CD` → [MiFreeInPageSupportBlock](../2B/MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)
- `0x002836DA` → [MiCanPfnOriginalPteBeLost](../37/MiCanPfnOriginalPteBeLost_function_00373D3C.md) (function, `0x00373D3C`)
- `0x00283751` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00283797` → [MiHandleSpecialPurposeMemoryCachedFault](../44/MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) (function, `0x0044C740`)
- `0x002837B6` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002837C9` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x002837DB` → [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) (function, `0x002A2854`)

### Direct callers
- [sub_00320866](../32/Unknown_function_00320866.md) at `0x00320B90`
- [MiResolveProtoPteFault](../32/MiResolveProtoPteFault_function_00321750.md) at `0x00321D22`

### Static image references
- `0x002829E2` → RVA `0x00E2DC80` (`.data`; read)
- `0x00282A43` → RVA `0x00E30088` (`.data`; read)
- `0x00282B33` → RVA `0x00010880` (`.rdata`; read)
- `0x00282C68` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00282EF8` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00282FD3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0028350B` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00283772` → [sub_006DA1C6](../6D/Unknown_function_006DA1C6.md) (`tail-transfer`)
  - `0x002837A2` → [sub_006DA1C6 + 0xA](../6D/Unknown_function_006DA1C6.md) (`tail-transfer`)
  - `0x002837E4` → [sub_006DA1C6 + 0x1D](../6D/Unknown_function_006DA1C6.md) (`tail-transfer`)
  - `0x002837F4` → [sub_006DA1C6 + 0x1D](../6D/Unknown_function_006DA1C6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00282940  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00282945  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0028294A  53                              push rbx
0028294B  56                              push rsi
0028294C  57                              push rdi
0028294D  41 54                           push r12
0028294F  41 55                           push r13
00282951  41 56                           push r14
00282953  41 57                           push r15
00282955  48 81 EC 80 00 00 00            sub rsp, 0x80
0028295C  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00282960  45 33 DB                        xor r11d, r11d
00282963  4C 8B A4 24 E0 00 00 00         mov r12, qword ptr [rsp + 0xe0]
0028296B  4D 8B F0                        mov r14, r8
0028296E  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
00282972  4C 8B FA                        mov r15, rdx
00282975  44 89 9C 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r11d
0028297D  4C 8B E9                        mov r13, rcx
00282980  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00282985  41 B9 FF 01 00 00               mov r9d, 0x1ff
0028298B  4D 89 1C 24                     mov qword ptr [r12], r11
0028298F  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
00282994  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
00282999  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
002829A3  48 BA F8 D7 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed7f8
002829AD  4D 85 F6                        test r14, r14
002829B0  0F 84 CC 04 00 00               je 0x140282e82
002829B6  49 8B 1F                        mov rbx, qword ptr [r15]
002829B9  48 8B C1                        mov rax, rcx
002829BC  4C 3B F8                        cmp r15, rax
002829BF  72 21                           jb 0x1402829e2
002829C1  48 8B C2                        mov rax, rdx
002829C4  4C 3B F8                        cmp r15, rax
002829C7  77 19                           ja 0x1402829e2
002829C9  F6 C3 01                        test bl, 1
002829CC  74 14                           je 0x1402829e2
002829CE  F6 C3 42                        test bl, 0x42
002829D1  0F 95 C1                        setne cl
002829D4  F6 C3 20                        test bl, 0x20
002829D7  0F 95 C0                        setne al
002829DA  84 C8                           test al, cl
002829DC  0F 84 3A 04 00 00               je 0x140282e1c
002829E2  48 8B 0D 97 B2 BA 00            mov rcx, qword ptr [rip + 0xbab297]
002829E9  48 8B C3                        mov rax, rbx
002829EC  48 85 C9                        test rcx, rcx
002829EF  74 0E                           je 0x1402829ff
002829F1  F6 C3 10                        test bl, 0x10
002829F4  75 09                           jne 0x1402829ff
002829F6  48 8B C1                        mov rax, rcx
002829F9  48 F7 D0                        not rax
002829FC  48 23 C3                        and rax, rbx
002829FF  48 C1 E8 0C                     shr rax, 0xc
00282A03  48 BF FF FF FF FF FF 00 00 00   movabs rdi, 0xffffffffff
00282A0D  48 23 C7                        and rax, rdi
00282A10  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
00282A1A  48 8D 34 40                     lea rsi, [rax + rax*2]
00282A1E  48 C1 E6 04                     shl rsi, 4
00282A22  48 8B C2                        mov rax, rdx
00282A25  48 03 F0                        add rsi, rax
00282A28  F6 46 23 10                     test byte ptr [rsi + 0x23], 0x10
00282A2C  0F 85 38 0D 00 00               jne 0x14028376a
00282A32  4D 8B F8                        mov r15, r8
00282A35  41 83 E7 01                     and r15d, 1
00282A39  0F 85 7A 03 00 00               jne 0x140282db9
00282A3F  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00282A43  48 8B 0D 3E D6 BA 00            mov rcx, qword ptr [rip + 0xbad63e]
00282A4A  48 C1 E8 2B                     shr rax, 0x2b
00282A4E  25 FF 03 00 00                  and eax, 0x3ff
00282A53  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00282A57  8B 40 04                        mov eax, dword ptr [rax + 4]
00282A5A  84 C0                           test al, al
00282A5C  0F 88 20 0D 00 00               js 0x140283782
00282A62  65 FF 04 25 98 2E 00 00         inc dword ptr gs:[0x2e98]
00282A6A  0F B6 56 22                     movzx edx, byte ptr [rsi + 0x22]
00282A6E  F6 C2 08                        test dl, 8
00282A71  0F 85 BC 0A 00 00               jne 0x140283533
00282A77  48 8B BC 24 C8 00 00 00         mov rdi, qword ptr [rsp + 0xc8]
00282A7F  F6 C2 20                        test dl, 0x20
00282A82  48 8B D7                        mov rdx, rdi
00282A85  4C 8B CE                        mov r9, rsi
00282A88  4D 8B C6                        mov r8, r14
00282A8B  49 8B CD                        mov rcx, r13
00282A8E  0F 85 29 0B 00 00               jne 0x1402835bd
00282A94  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00282A99  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
00282A9E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00282AA3  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00282AA8  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00282AAD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00282AB2  E8 49 0D 00 00                  call 0x140283800
00282AB7  85 C0                           test eax, eax
00282AB9  0F 88 E6 02 00 00               js 0x140282da5
00282ABF  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00282AC4  48 85 C0                        test rax, rax
00282AC7  48 0F 45 F0                     cmovne rsi, rax
00282ACB  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
00282ACF  48 8B C3                        mov rax, rbx
00282AD2  4C 8B A4 24 D8 00 00 00         mov r12, qword ptr [rsp + 0xd8]
00282ADA  F6 C1 01                        test cl, 1
00282ADD  0F 85 6E 07 00 00               jne 0x140283251
00282AE3  48 C1 E8 05                     shr rax, 5
00282AE7  BB 01 00 00 00                  mov ebx, 1
00282AEC  83 E0 1F                        and eax, 0x1f
00282AEF  83 F8 18                        cmp eax, 0x18
00282AF2  75 37                           jne 0x140282b2b
00282AF4  48 8B CF                        mov rcx, rdi
00282AF7  E8 A4 FD FF FF                  call 0x1402828a0
00282AFC  4C 8B C0                        mov r8, rax
00282AFF  8B CB                           mov ecx, ebx
00282B01  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00282B04  C1 E8 10                        shr eax, 0x10
00282B07  0F B6 D0                        movzx edx, al
00282B0A  C1 EA 06                        shr edx, 6
00282B0D  E8 CA 1A 00 00                  call 0x1402845dc
00282B12  8B D0                           mov edx, eax
00282B14  48 C1 E2 05                     shl rdx, 5
00282B18  48 8B CA                        mov rcx, rdx
00282B1B  49 33 C8                        xor rcx, r8
00282B1E  48 81 E1 1F FC FF FF            and rcx, 0xfffffffffffffc1f
00282B25  48 33 CA                        xor rcx, rdx
00282B28  48 89 0F                        mov qword ptr [rdi], rcx
00282B2B  48 8B CF                        mov rcx, rdi
00282B2E  E8 2D 12 00 00                  call 0x140283d60
00282B33  48 8B 3D 46 DD D8 FF            mov rdi, qword ptr [rip - 0x2722ba]
00282B3A  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00282B42  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00282B46  48 8B 0D 3B D5 BA 00            mov rcx, qword ptr [rip + 0xbad53b]
00282B4D  48 C1 E8 2B                     shr rax, 0x2b
00282B51  25 FF 03 00 00                  and eax, 0x3ff
00282B56  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00282B5A  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00282B5E  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00282B63  48 0F BA E0 0A                  bt rax, 0xa
00282B68  72 2A                           jb 0x140282b94
00282B6A  0F B6 C8                        movzx ecx, al
00282B6D  C0 E9 02                        shr cl, 2
00282B70  84 CB                           test bl, cl
00282B72  74 20                           je 0x140282b94
00282B74  8B 8A B4 04 00 00               mov ecx, dword ptr [rdx + 0x4b4]
00282B7A  48 C1 E8 0C                     shr rax, 0xc
00282B7E  83 E0 0F                        and eax, 0xf
00282B81  3B C1                           cmp eax, ecx
00282B83  75 0F                           jne 0x140282b94
00282B85  0F B6 4E 22                     movzx ecx, byte ptr [rsi + 0x22]
00282B89  33 FF                           xor edi, edi
00282B8B  F6 C1 10                        test cl, 0x10
00282B8E  0F 84 05 07 00 00               je 0x140283299
00282B94  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00282B98  48 0F BA E0 0A                  bt rax, 0xa
00282B9D  72 28                           jb 0x140282bc7
00282B9F  48 0F BA E0 1A                  bt rax, 0x1a
00282BA4  73 21                           jae 0x140282bc7
00282BA6  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
00282BAE  E8 ED FC FF FF                  call 0x1402828a0
00282BB3  48 83 C8 40                     or rax, 0x40
00282BB7  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
00282BBF  48 8B D0                        mov rdx, rax
00282BC2  E8 49 EC FF FF                  call 0x140281810
00282BC7  48 F7 84 24 D0 00 00 00 00 08 00 00  test qword ptr [rsp + 0xd0], 0x800
00282BD3  74 36                           je 0x140282c0b
00282BD5  48 83 BC 24 D8 00 00 00 00      cmp qword ptr [rsp + 0xd8], 0
00282BDE  0F 85 B0 05 00 00               jne 0x140283194
00282BE4  F6 46 22 10                     test byte ptr [rsi + 0x22], 0x10
00282BE8  0F 84 07 06 00 00               je 0x1402831f5
00282BEE  4D 85 E4                        test r12, r12
00282BF1  0F 85 1F 06 00 00               jne 0x140283216
00282BF7  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00282C01  49 39 45 00                     cmp qword ptr [r13], rax
00282C05  0F 83 0B 06 00 00               jae 0x140283216
00282C0B  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00282C0F  49 B8 00 00 00 00 40 00 00 00   movabs r8, 0x4000000000
00282C19  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00282C23  48 85 C9                        test rcx, rcx
00282C26  79 5B                           jns 0x140282c83
00282C28  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00282C30  45 33 E4                        xor r12d, r12d
00282C33  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00282C38  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00282C42  48 8B C0                        mov rax, rax
00282C45  4C 8B 8C 24 C8 00 00 00         mov r9, qword ptr [rsp + 0xc8]
00282C4D  4C 3B C8                        cmp r9, rax
00282C50  72 16                           jb 0x140282c68
00282C52  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
00282C5C  48 8B C0                        mov rax, rax
00282C5F  4C 3B C8                        cmp r9, rax
00282C62  0F 86 9A 09 00 00               jbe 0x140283602
00282C68  48 0F BA 25 17 3E D4 00 24      bt qword ptr [rip + 0xd43e17], 0x24
00282C71  0F 82 D2 06 00 00               jb 0x140283349
00282C77  49 89 19                        mov qword ptr [r9], rbx
00282C7A  45 85 E4                        test r12d, r12d
00282C7D  0F 85 D2 09 00 00               jne 0x140283655
00282C83  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00282C8D  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00282C92  4D 85 F6                        test r14, r14
00282C95  0F 84 85 00 00 00               je 0x140282d20
00282C9B  45 33 E4                        xor r12d, r12d
00282C9E  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00282CA5  0F 82 25 03 00 00               jb 0x140282fd0
00282CAB  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00282CAF  48 85 C0                        test rax, rax
00282CB2  78 1D                           js 0x140282cd1
00282CB4  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00282CB8  48 0F BA E0 28                  bt rax, 0x28
00282CBD  72 12                           jb 0x140282cd1
00282CBF  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00282CC3  48 C1 E8 3C                     shr rax, 0x3c
00282CC7  24 07                           and al, 7
00282CC9  3C 01                           cmp al, 1
00282CCB  74 04                           je 0x140282cd1
00282CCD  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00282CD1  49 8B 06                        mov rax, qword ptr [r14]
00282CD4  48 B9 FE FF FF FF FF 0F 00 00   movabs rcx, 0xffffffffffe
00282CDE  48 85 C1                        test rcx, rax
00282CE1  0F 85 0A 03 00 00               jne 0x140282ff1
00282CE7  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00282CEB  49 8B CE                        mov rcx, r14
00282CEE  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00282CF5  C1 E8 10                        shr eax, 0x10
00282CF8  24 DF                           and al, 0xdf
00282CFA  88 84 24 E2 00 00 00            mov byte ptr [rsp + 0xe2], al
00282D01  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00282D08  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00282D0C  E8 BF 2C FC FF                  call 0x1402459d0
00282D11  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00282D1B  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00282D20  41 BC 01 00 00 00               mov r12d, 1
00282D26  48 85 FF                        test rdi, rdi
00282D29  74 10                           je 0x140282d3b
00282D2B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00282D30  45 8B C4                        mov r8d, r12d
00282D33  48 8B D7                        mov rdx, rdi
00282D36  E8 95 12 00 00                  call 0x140283fd0
00282D3B  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00282D40  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00282D48  48 85 C0                        test rax, rax
00282D4B  0F 85 65 09 00 00               jne 0x1402836b6
00282D51  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00282D55  48 85 C0                        test rax, rax
00282D58  0F 89 32 03 00 00               jns 0x140283090
00282D5E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00282D68  48 8B C0                        mov rax, rax
00282D6B  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00282D70  48 2B F0                        sub rsi, rax
00282D73  4C 8B 84 24 D8 00 00 00         mov r8, qword ptr [rsp + 0xd8]
00282D7B  48 BA AB AA AA AA AA AA AA AA   movabs rdx, 0xaaaaaaaaaaaaaaab
00282D85  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00282D8A  45 33 C9                        xor r9d, r9d
00282D8D  48 C1 FE 04                     sar rsi, 4
00282D91  49 8B CD                        mov rcx, r13
00282D94  48 0F AF D6                     imul rdx, rsi
00282D98  E8 73 29 0C 00                  call 0x140345710
00282D9D  85 C0                           test eax, eax
00282D9F  0F 89 C2 03 00 00               jns 0x140283167
00282DA5  48 81 C4 80 00 00 00            add rsp, 0x80
00282DAC  41 5F                           pop r15
00282DAE  41 5E                           pop r14
00282DB0  41 5D                           pop r13
00282DB2  41 5C                           pop r12
00282DB4  5F                              pop rdi
00282DB5  5E                              pop rsi
00282DB6  5B                              pop rbx
00282DB7  C3                              ret
00282DB8  CC                              int3
00282DB9  4D 8B D0                        mov r10, r8
00282DBC  49 83 E2 FE                     and r10, 0xfffffffffffffffe
00282DC0  41 80 3A 01                     cmp byte ptr [r10], 1
00282DC4  0F 85 75 FC FF FF               jne 0x140282a3f
00282DCA  44 8B 46 20                     mov r8d, dword ptr [rsi + 0x20]
00282DCE  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00282DD1  45 8B 52 50                     mov r10d, dword ptr [r10 + 0x50]
00282DD5  C1 E8 18                        shr eax, 0x18
00282DD8  41 83 E2 07                     and r10d, 7
00282DDC  A8 08                           test al, 8
00282DDE  0F 85 9E 04 00 00               jne 0x140283282
00282DE4  41 C1 E8 18                     shr r8d, 0x18
00282DE8  41 83 E0 07                     and r8d, 7
00282DEC  45 3B D0                        cmp r10d, r8d
00282DEF  74 06                           je 0x140282df7
00282DF1  0F 83 FB 05 00 00               jae 0x1402833f2
00282DF7  41 8B FB                        mov edi, r11d
00282DFA  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00282E04  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00282E09  4D 85 F6                        test r14, r14
00282E0C  74 0A                           je 0x140282e18
00282E0E  B2 11                           mov dl, 0x11
00282E10  49 8B CE                        mov rcx, r14
00282E13  E8 78 32 FC FF                  call 0x140246090
00282E18  8B C7                           mov eax, edi
00282E1A  EB 89                           jmp 0x140282da5
00282E1C  48 F7 05 61 3C D4 00 00 00 60 00  test qword ptr [rip + 0xd43c61], 0x600000
00282E27  0F 84 B5 FB FF FF               je 0x1402829e2
00282E2D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00282E36  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00282E3D  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00282E44  0F 84 98 FB FF FF               je 0x1402829e2
00282E4A  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
00282E51  48 85 D2                        test rdx, rdx
00282E54  0F 84 88 FB FF FF               je 0x1402829e2
00282E5A  49 8B C7                        mov rax, r15
00282E5D  48 C1 E8 03                     shr rax, 3
00282E61  49 23 C1                        and rax, r9
00282E64  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
00282E68  A8 20                           test al, 0x20
00282E6A  74 04                           je 0x140282e70
00282E6C  48 83 CB 20                     or rbx, 0x20
00282E70  48 8B CB                        mov rcx, rbx
00282E73  48 83 CB 42                     or rbx, 0x42
00282E77  A8 42                           test al, 0x42
00282E79  48 0F 44 D9                     cmove rbx, rcx
00282E7D  E9 60 FB FF FF                  jmp 0x1402829e2
00282E82  48 BF FF FF FF FF FF 00 00 00   movabs rdi, 0xffffffffff
00282E8C  48 BE 00 00 00 00 00 DE FF FF   movabs rsi, 0xffffde0000000000
00282E96  49 8B CF                        mov rcx, r15
00282E99  E8 02 FA FF FF                  call 0x1402828a0
00282E9E  48 8B D8                        mov rbx, rax
00282EA1  48 0F BA E0 0B                  bt rax, 0xb
00282EA6  0F 83 DE 02 00 00               jae 0x14028318a
00282EAC  F6 C3 01                        test bl, 1
00282EAF  75 E5                           jne 0x140282e96
00282EB1  48 85 C0                        test rax, rax
00282EB4  74 10                           je 0x140282ec6
00282EB6  48 8B 05 C3 AD BA 00            mov rax, qword ptr [rip + 0xbaadc3]
00282EBD  48 85 C0                        test rax, rax
00282EC0  0F 85 F8 00 00 00               jne 0x140282fbe
00282EC6  48 8B 05 B3 AD BA 00            mov rax, qword ptr [rip + 0xbaadb3]
00282ECD  48 8B CB                        mov rcx, rbx
00282ED0  48 85 C0                        test rax, rax
00282ED3  74 12                           je 0x140282ee7
00282ED5  F6 C3 10                        test bl, 0x10
00282ED8  0F 85 A9 01 00 00               jne 0x140283087
00282EDE  48 8B C8                        mov rcx, rax
00282EE1  48 F7 D1                        not rcx
00282EE4  48 23 CB                        and rcx, rbx
00282EE7  48 C1 E9 0C                     shr rcx, 0xc
00282EEB  48 23 CF                        and rcx, rdi
00282EEE  48 8D 14 49                     lea rdx, [rcx + rcx*2]
00282EF2  48 03 D2                        add rdx, rdx
00282EF5  48 8B C6                        mov rax, rsi
00282EF8  48 3B 0D E1 AD BA 00            cmp rcx, qword ptr [rip + 0xbaade1]
00282EFF  48 8D 34 D0                     lea rsi, [rax + rdx*8]
00282F03  77 87                           ja 0x140282e8c
00282F05  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00282F0F  48 8B C0                        mov rax, rax
00282F12  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
00282F16  48 0F BA E0 36                  bt rax, 0x36
00282F1B  0F 83 6B FF FF FF               jae 0x140282e8c
00282F21  45 33 E4                        xor r12d, r12d
00282F24  0F 1F 40 00                     nop dword ptr [rax]
00282F28  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00282F30  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
00282F37  0F 82 F3 02 00 00               jb 0x140283230
00282F3D  49 8B CF                        mov rcx, r15
00282F40  E8 5B F9 FF FF                  call 0x1402828a0
00282F45  4C 8B A4 24 E0 00 00 00         mov r12, qword ptr [rsp + 0xe0]
00282F4D  48 3B C3                        cmp rax, rbx
00282F50  0F 85 B5 03 00 00               jne 0x14028330b
00282F56  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00282F5A  48 8B 0D 27 D1 BA 00            mov rcx, qword ptr [rip + 0xbad127]
00282F61  48 C1 E8 2B                     shr rax, 0x2b
00282F65  25 FF 03 00 00                  and eax, 0x3ff
00282F6A  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00282F6E  8B 40 04                        mov eax, dword ptr [rax + 4]
00282F71  84 C0                           test al, al
00282F73  0F 88 F8 01 00 00               js 0x140283171
00282F79  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00282F7D  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
00282F87  48 0B C1                        or rax, rcx
00282F8A  49 3B C7                        cmp rax, r15
00282F8D  0F 85 BC 05 00 00               jne 0x14028354f
00282F93  48 85 F6                        test rsi, rsi
00282F96  0F 84 EE 01 00 00               je 0x14028318a
00282F9C  49 8B CF                        mov rcx, r15
00282F9F  E8 FC F8 FF FF                  call 0x1402828a0
00282FA4  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00282FA9  48 8B D8                        mov rbx, rax
00282FAC  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
00282FB6  45 33 DB                        xor r11d, r11d
00282FB9  E9 6A FA FF FF                  jmp 0x140282a28
00282FBE  48 85 C3                        test rbx, rax
00282FC1  0F 85 FF FE FF FF               jne 0x140282ec6
00282FC7  E9 CA FE FF FF                  jmp 0x140282e96
00282FCC  0F 1F 40 00                     nop dword ptr [rax]
00282FD0  41 FF C4                        inc r12d
00282FD3  44 85 25 D2 22 D4 00            test dword ptr [rip + 0xd422d2], r12d
00282FDA  0F 84 2B 05 00 00               je 0x14028350b
00282FE0  F3 90                           pause
00282FE2  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00282FE6  48 85 C0                        test rax, rax
00282FE9  0F 89 AF FC FF FF               jns 0x140282c9e
00282FEF  EB DF                           jmp 0x140282fd0
00282FF1  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00282FF5  48 B9 00 00 00 00 00 F0 FF FF   movabs rcx, 0xfffff00000000000
00282FFF  48 0B C1                        or rax, rcx
00283002  48 8B 0C C5 00 00 00 00         mov rcx, qword ptr [rax*8]
0028300A  4C 8D 24 C5 00 00 00 00         lea r12, [rax*8]
00283012  49 3B CC                        cmp rcx, r12
00283015  0F 84 8A 05 00 00               je 0x1402835a5
0028301B  48 8B 01                        mov rax, qword ptr [rcx]
0028301E  4C 39 61 08                     cmp qword ptr [rcx + 8], r12
00283022  0F 85 3B 07 00 00               jne 0x140283763
00283028  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0028302C  0F 85 31 07 00 00               jne 0x140283763
00283032  49 89 04 24                     mov qword ptr [r12], rax
00283036  4C 89 60 08                     mov qword ptr [rax + 8], r12
0028303A  49 8B 04 24                     mov rax, qword ptr [r12]
0028303E  49 3B C4                        cmp rax, r12
00283041  0F 85 1E 06 00 00               jne 0x140283665
00283047  48 89 09                        mov qword ptr [rcx], rcx
0028304A  48 8B C1                        mov rax, rcx
0028304D  48 89 41 08                     mov qword ptr [rcx + 8], rax
00283051  49 B8 01 00 00 00 00 F0 FF FF   movabs r8, 0xfffff00000000001
0028305B  49 8B 06                        mov rax, qword ptr [r14]
0028305E  48 C1 E9 03                     shr rcx, 3
00283062  48 8B D1                        mov rdx, rcx
00283065  48 33 D0                        xor rdx, rax
00283068  49 23 D0                        and rdx, r8
0028306B  48 33 D1                        xor rdx, rcx
0028306E  49 89 16                        mov qword ptr [r14], rdx
00283071  49 8B CE                        mov rcx, r14
00283074  E8 57 29 FC FF                  call 0x1402459d0
00283079  41 C7 44 24 10 01 00 00 00      mov dword ptr [r12 + 0x10], 1
00283082  E9 8A FC FF FF                  jmp 0x140282d11
00283087  48 83 E1 EF                     and rcx, 0xffffffffffffffef
0028308B  E9 57 FE FF FF                  jmp 0x140282ee7
00283090  4D 85 FF                        test r15, r15
00283093  0F 85 93 03 00 00               jne 0x14028342c
00283099  45 33 F6                        xor r14d, r14d
0028309C  41 F6 45 45 10                  test byte ptr [r13 + 0x45], 0x10
002830A1  0F 85 34 04 00 00               jne 0x1402834db
002830A7  41 0F B6 4D 45                  movzx ecx, byte ptr [r13 + 0x45]
002830AC  0F B6 C1                        movzx eax, cl
002830AF  24 09                           and al, 9
002830B1  3C 08                           cmp al, 8
002830B3  75 75                           jne 0x14028312a
002830B5  F6 C1 04                        test cl, 4
002830B8  75 70                           jne 0x14028312a
002830BA  41 0F B7 45 42                  movzx eax, word ptr [r13 + 0x42]
002830BF  41 B8 FF 01 00 00               mov r8d, 0x1ff
002830C5  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
002830CD  66 85 C0                        test ax, ax
002830D0  74 3E                           je 0x140283110
002830D2  41 0F B7 4D 40                  movzx ecx, word ptr [r13 + 0x40]
002830D7  03 C8                           add ecx, eax
002830D9  8B C2                           mov eax, edx
002830DB  C1 E8 03                        shr eax, 3
002830DE  41 23 C0                        and eax, r8d
002830E1  3B C8                           cmp ecx, eax
002830E3  75 14                           jne 0x1402830f9
002830E5  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002830E9  48 85 C0                        test rax, rax
002830EC  0F 88 09 02 00 00               js 0x1402832fb
002830F2  41 F6 45 45 02                  test byte ptr [r13 + 0x45], 2
002830F7  75 17                           jne 0x140283110
002830F9  49 8D 4D 38                     lea rcx, [r13 + 0x38]
002830FD  E8 0E 48 0C 00                  call 0x140347910
00283102  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0028310A  41 B8 FF 01 00 00               mov r8d, 0x1ff
00283110  41 0F B7 45 42                  movzx eax, word ptr [r13 + 0x42]
00283115  66 85 C0                        test ax, ax
00283118  0F 84 01 02 00 00               je 0x14028331f
0028311E  66 FF C0                        inc ax
00283121  66 41 89 45 42                  mov word ptr [r13 + 0x42], ax
00283126  41 83 CE 04                     or r14d, 4
0028312A  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
00283132  41 8B FE                        mov edi, r14d
00283135  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0028313A  83 CF 10                        or edi, 0x10
0028313D  41 F6 45 45 01                  test byte ptr [r13 + 0x45], 1
00283142  4C 8B C6                        mov r8, rsi
00283145  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0028314A  41 0F 44 FE                     cmove edi, r14d
0028314E  45 33 C9                        xor r9d, r9d
00283151  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00283155  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0028315A  E8 61 01 0B 00                  call 0x1403332c0
0028315F  85 C0                           test eax, eax
00283161  0F 84 6C 06 00 00               je 0x1402837d3
00283167  B8 10 01 00 00                  mov eax, 0x110
0028316C  E9 34 FC FF FF                  jmp 0x140282da5
00283171  BA 02 00 00 00                  mov edx, 2
00283176  48 8B CE                        mov rcx, rsi
00283179  E8 72 18 18 00                  call 0x1404049f0
0028317E  48 8B F0                        mov rsi, rax
00283181  48 85 C0                        test rax, rax
00283184  0F 85 EF FD FF FF               jne 0x140282f79
0028318A  B8 34 04 00 C0                  mov eax, 0xc0000434
0028318F  E9 11 FC FF FF                  jmp 0x140282da5
00283194  48 B9 FF FF FE FF FF 7F 00 00   movabs rcx, 0x7ffffffeffff
0028319E  49 39 4D 00                     cmp qword ptr [r13], rcx
002831A2  0F 87 3C FA FF FF               ja 0x140282be4
002831A8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002831B1  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002831B8  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
002831C2  48 85 84 24 D0 00 00 00         test qword ptr [rsp + 0xd0], rax
002831CA  0F 84 1F 04 00 00               je 0x1402835ef
002831D0  48 8B 81 78 07 00 00            mov rax, qword ptr [rcx + 0x778]
002831D7  48 85 C0                        test rax, rax
002831DA  0F 84 04 FA FF FF               je 0x140282be4
002831E0  48 83 C0 18                     add rax, 0x18
002831E4  48 39 00                        cmp qword ptr [rax], rax
002831E7  0F 84 F7 F9 FF FF               je 0x140282be4
002831ED  45 33 E4                        xor r12d, r12d
002831F0  E9 EF F9 FF FF                  jmp 0x140282be4
002831F5  4D 85 E4                        test r12, r12
002831F8  0F 84 0D FA FF FF               je 0x140282c0b
002831FE  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00283202  48 85 C0                        test rax, rax
00283205  0F 88 00 FA FF FF               js 0x140282c0b
0028320B  48 8B CE                        mov rcx, rsi
0028320E  E8 BD DB 0E 00                  call 0x140370dd0
00283213  48 8B F8                        mov rdi, rax
00283216  48 83 8C 24 D0 00 00 00 42      or qword ptr [rsp + 0xd0], 0x42
0028321F  E9 E7 F9 FF FF                  jmp 0x140282c0b
00283224  0F 1F 40 00                     nop dword ptr [rax]
00283228  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00283230  41 FF C4                        inc r12d
00283233  44 85 25 72 20 D4 00            test dword ptr [rip + 0xd42072], r12d
0028323A  0F 84 3D 03 00 00               je 0x14028357d
00283240  F3 90                           pause
00283242  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00283246  48 85 C0                        test rax, rax
00283249  0F 89 E1 FC FF FF               jns 0x140282f30
0028324F  EB DF                           jmp 0x140283230
00283251  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00283255  80 39 04                        cmp byte ptr [rcx], 4
00283258  0F 85 85 F8 FF FF               jne 0x140282ae3
0028325E  48 8B 07                        mov rax, qword ptr [rdi]
00283261  48 25 9F FC FF FF               and rax, 0xfffffffffffffc9f
00283267  48 0F BA E8 07                  bts rax, 7
0028326C  48 89 07                        mov qword ptr [rdi], rax
0028326F  48 8B C3                        mov rax, rbx
00283272  48 25 9F FC FF FF               and rax, 0xfffffffffffffc9f
00283278  48 0F BA E8 07                  bts rax, 7
0028327D  E9 61 F8 FF FF                  jmp 0x140282ae3
00283282  48 8B C2                        mov rax, rdx
00283285  48 3B F0                        cmp rsi, rax
00283288  0F 83 F1 00 00 00               jae 0x14028337f
0028328E  41 B8 05 00 00 00               mov r8d, 5
00283294  E9 53 FB FF FF                  jmp 0x140282dec
00283299  C0 E9 03                        shr cl, 3
0028329C  48 0F BA 66 10 0A               bt qword ptr [rsi + 0x10], 0xa
002832A2  F6 D1                           not cl
002832A4  0F 93 C0                        setae al
002832A7  22 C8                           and cl, al
002832A9  84 CB                           test bl, cl
002832AB  74 19                           je 0x1402832c6
002832AD  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
002832B1  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002832B6  C0 E8 02                        shr al, 2
002832B9  84 C3                           test bl, al
002832BB  0F 85 74 03 00 00               jne 0x140283635
002832C1  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
002832C6  8B 5E 20                        mov ebx, dword ptr [rsi + 0x20]
002832C9  89 9C 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], ebx
002832D0  C1 EB 10                        shr ebx, 0x10
002832D3  44 0F B6 DB                     movzx r11d, bl
002832D7  F6 C3 08                        test bl, 8
002832DA  0F 85 F7 03 00 00               jne 0x1402836d7
002832E0  41 80 CB 10                     or r11b, 0x10
002832E4  44 88 9C 24 E2 00 00 00         mov byte ptr [rsp + 0xe2], r11b
002832EC  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
002832F3  89 46 20                        mov dword ptr [rsi + 0x20], eax
002832F6  E9 99 F8 FF FF                  jmp 0x140282b94
002832FB  41 F6 45 45 02                  test byte ptr [r13 + 0x45], 2
00283300  0F 85 F3 FD FF FF               jne 0x1402830f9
00283306  E9 05 FE FF FF                  jmp 0x140283110
0028330B  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00283315  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0028331A  E9 6D FB FF FF                  jmp 0x140282e8c
0028331F  8B C2                           mov eax, edx
00283321  66 45 89 65 42                  mov word ptr [r13 + 0x42], r12w
00283326  C1 E8 03                        shr eax, 3
00283329  66 41 23 C0                     and ax, r8w
0028332D  66 41 89 45 40                  mov word ptr [r13 + 0x40], ax
00283332  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00283336  48 85 C0                        test rax, rax
00283339  0F 89 C2 01 00 00               jns 0x140283501
0028333F  41 80 65 45 FD                  and byte ptr [r13 + 0x45], 0xfd
00283344  E9 DD FD FF FF                  jmp 0x140283126
00283349  F6 C3 20                        test bl, 0x20
0028334C  0F 85 25 F9 FF FF               jne 0x140282c77
00283352  48 8B CA                        mov rcx, rdx
00283355  49 03 C8                        add rcx, r8
00283358  4C 3B C9                        cmp r9, rcx
0028335B  0F 82 16 F9 FF FF               jb 0x140282c77
00283361  41 B8 80 00 00 00               mov r8d, 0x80
00283367  48 8B D3                        mov rdx, rbx
0028336A  49 8B C9                        mov rcx, r9
0028336D  E8 0E FA 00 00                  call 0x140292d80
00283372  4C 8B 8C 24 C8 00 00 00         mov r9, qword ptr [rsp + 0xc8]
0028337A  E9 F8 F8 FF FF                  jmp 0x140282c77
0028337F  48 8B 05 5A A9 BA 00            mov rax, qword ptr [rip + 0xbaa95a]
00283386  48 8D 0C 40                     lea rcx, [rax + rax*2]
0028338A  48 C1 E1 04                     shl rcx, 4
0028338E  48 B8 30 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000030
00283398  48 03 C8                        add rcx, rax
0028339B  48 3B F1                        cmp rsi, rcx
0028339E  0F 83 EA FE FF FF               jae 0x14028328e
002833A4  48 8B C2                        mov rax, rdx
002833A7  48 8B CE                        mov rcx, rsi
002833AA  48 2B C8                        sub rcx, rax
002833AD  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002833B7  48 C1 F9 04                     sar rcx, 4
002833BB  48 0F AF C8                     imul rcx, rax
002833BF  E8 7C 5E 03 00                  call 0x1402b9240
002833C4  85 C0                           test eax, eax
002833C6  0F 85 C2 FE FF FF               jne 0x14028328e
002833CC  41 8B C0                        mov eax, r8d
002833CF  C1 E8 10                        shr eax, 0x10
002833D2  24 07                           and al, 7
002833D4  3C 06                           cmp al, 6
002833D6  0F 84 08 FA FF FF               je 0x140282de4
002833DC  48 8B CE                        mov rcx, rsi
002833DF  E8 EC AE 00 00                  call 0x14028e2d0
002833E4  83 F8 09                        cmp eax, 9
002833E7  0F 85 F7 F9 FF FF               jne 0x140282de4
002833ED  E9 9C FE FF FF                  jmp 0x14028328e
002833F2  0F B6 46 22                     movzx eax, byte ptr [rsi + 0x22]
002833F6  24 07                           and al, 7
002833F8  3C 02                           cmp al, 2
002833FA  74 60                           je 0x14028345c
002833FC  3C 06                           cmp al, 6
002833FE  75 04                           jne 0x140283404
00283400  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00283404  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00283407  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
0028340E  C1 E8 18                        shr eax, 0x18
00283411  24 F8                           and al, 0xf8
00283413  41 0A C2                        or al, r10b
00283416  88 84 24 E3 00 00 00            mov byte ptr [rsp + 0xe3], al
0028341D  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00283424  89 46 20                        mov dword ptr [rsi + 0x20], eax
00283427  E9 CB F9 FF FF                  jmp 0x140282df7
0028342C  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00283431  48 8B C1                        mov rax, rcx
00283434  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00283438  80 38 04                        cmp byte ptr [rax], 4
0028343B  0F 84 4D 02 00 00               je 0x14028368e
00283441  48 8B C1                        mov rax, rcx
00283444  45 33 FF                        xor r15d, r15d
00283447  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0028344B  80 38 03                        cmp byte ptr [rax], 3
0028344E  0F 85 22 02 00 00               jne 0x140283676
00283454  45 8B F4                        mov r14d, r12d
00283457  E9 40 FC FF FF                  jmp 0x14028309c
0028345C  45 85 C0                        test r8d, r8d
0028345F  75 67                           jne 0x1402834c8
00283461  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
00283464  48 0F BA E0 0A                  bt rax, 0xa
00283469  72 5D                           jb 0x1402834c8
0028346B  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028346F  48 8B 0D 12 CC BA 00            mov rcx, qword ptr [rip + 0xbacc12]
00283476  48 C1 E8 2B                     shr rax, 0x2b
0028347A  25 FF 03 00 00                  and eax, 0x3ff
0028347F  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00283483  8B 40 04                        mov eax, dword ptr [rax + 4]
00283486  84 C0                           test al, al
00283488  78 3E                           js 0x1402834c8
0028348A  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
0028348E  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00283492  0F B6 D0                        movzx edx, al
00283495  C0 EA 02                        shr dl, 2
00283498  F6 C2 01                        test dl, 1
0028349B  74 2B                           je 0x1402834c8
0028349D  4C 8B 05 E4 CB BA 00            mov r8, qword ptr [rip + 0xbacbe4]
002834A4  48 C1 E9 2B                     shr rcx, 0x2b
002834A8  81 E1 FF 03 00 00               and ecx, 0x3ff
002834AE  48 C1 E8 0C                     shr rax, 0xc
002834B2  83 E0 0F                        and eax, 0xf
002834B5  4D 8B 0C C8                     mov r9, qword ptr [r8 + rcx*8]
002834B9  41 8B 89 B4 04 00 00            mov ecx, dword ptr [r9 + 0x4b4]
002834C0  3B C1                           cmp eax, ecx
002834C2  0F 84 2F F9 FF FF               je 0x140282df7
002834C8  41 8B D2                        mov edx, r10d
002834CB  48 8B CE                        mov rcx, rsi
002834CE  E8 5D 68 03 00                  call 0x1402b9d30
002834D3  45 33 DB                        xor r11d, r11d
002834D6  E9 1C F9 FF FF                  jmp 0x140282df7
002834DB  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
002834DF  A8 01                           test al, 1
002834E1  74 0D                           je 0x1402834f0
002834E3  48 83 E0 FE                     and rax, 0xfffffffffffffffe
002834E7  80 38 02                        cmp byte ptr [rax], 2
002834EA  0F 84 B7 FB FF FF               je 0x1402830a7
002834F0  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
002834F8  48 83 E3 DF                     and rbx, 0xffffffffffffffdf
002834FC  E9 A6 FB FF FF                  jmp 0x1402830a7
00283501  41 80 4D 45 02                  or byte ptr [r13 + 0x45], 2
00283506  E9 1B FC FF FF                  jmp 0x140283126
0028350B  8B 05 A7 35 D4 00               mov eax, dword ptr [rip + 0xd435a7]
00283511  A8 40                           test al, 0x40
00283513  0F 84 C7 FA FF FF               je 0x140282fe0
00283519  E8 72 BF 08 00                  call 0x14030f490
0028351E  84 C0                           test al, al
00283520  0F 84 BA FA FF FF               je 0x140282fe0
00283526  41 8B CC                        mov ecx, r12d
00283529  E8 32 BF 08 00                  call 0x14030f460
0028352E  E9 AF FA FF FF                  jmp 0x140282fe2
00283533  48 8B CE                        mov rcx, rsi
00283536  E8 6D A8 20 00                  call 0x14048dda8
0028353B  8B F8                           mov edi, eax
0028353D  85 C0                           test eax, eax
0028353F  0F 89 32 F5 FF FF               jns 0x140282a77
00283545  41 83 4D 50 04                  or dword ptr [r13 + 0x50], 4
0028354A  E9 AB F8 FF FF                  jmp 0x140282dfa
0028354F  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00283553  48 0F BA E0 28                  bt rax, 0x28
00283558  0F 82 35 FA FF FF               jb 0x140282f93
0028355E  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00283562  4C 8B CB                        mov r9, rbx
00283565  4D 8B C7                        mov r8, r15
00283568  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0028356D  BA 11 04 00 00                  mov edx, 0x411
00283572  B9 1A 00 00 00                  mov ecx, 0x1a
00283577  E8 E4 A0 27 00                  call 0x1404fd660
0028357C  CC                              int3
0028357D  8B 05 35 35 D4 00               mov eax, dword ptr [rip + 0xd43535]
00283583  A8 40                           test al, 0x40
00283585  0F 84 B5 FC FF FF               je 0x140283240
0028358B  E8 00 BF 08 00                  call 0x14030f490
00283590  84 C0                           test al, al
00283592  0F 84 A8 FC FF FF               je 0x140283240
00283598  41 8B CC                        mov ecx, r12d
0028359B  E8 C0 BE 08 00                  call 0x14030f460
002835A0  E9 9D FC FF FF                  jmp 0x140283242
002835A5  49 8B 06                        mov rax, qword ptr [r14]
002835A8  49 B8 01 00 00 00 00 F0 FF FF   movabs r8, 0xfffff00000000001
002835B2  49 23 C0                        and rax, r8
002835B5  49 89 06                        mov qword ptr [r14], rax
002835B8  E9 B4 FA FF FF                  jmp 0x140283071
002835BD  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
002835C5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002835CA  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
002835CF  E8 74 65 0E 00                  call 0x140369b48
002835D4  83 BC 24 C0 00 00 00 01         cmp dword ptr [rsp + 0xc0], 1
002835DC  0F 86 C3 F7 FF FF               jbe 0x140282da5
002835E2  85 C0                           test eax, eax
002835E4  0F 88 BB F7 FF FF               js 0x140282da5
002835EA  E9 DC F4 FF FF                  jmp 0x140282acb
002835EF  8B 81 F4 01 00 00               mov eax, dword ptr [rcx + 0x1f4]
002835F5  A8 10                           test al, 0x10
002835F7  0F 84 D3 FB FF FF               je 0x1402831d0
002835FD  E9 EB FB FF FF                  jmp 0x1402831ed
00283602  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00283607  E8 5C 15 01 00                  call 0x140294b68
0028360C  4C 8B 8C 24 C8 00 00 00         mov r9, qword ptr [rsp + 0xc8]
00283614  44 8B E0                        mov r12d, eax
00283617  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0028361C  49 B8 00 00 00 00 40 00 00 00   movabs r8, 0x4000000000
00283626  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00283630  E9 33 F6 FF FF                  jmp 0x140282c68
00283635  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00283639  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0028363E  48 83 E0 FB                     and rax, 0xfffffffffffffffb
00283642  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
00283646  E8 41 80 0A 00                  call 0x14032b68c
0028364B  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00283650  E9 71 FC FF FF                  jmp 0x1402832c6
00283655  48 8B D3                        mov rdx, rbx
00283658  49 8B C9                        mov rcx, r9
0028365B  E8 4C 18 01 00                  call 0x140294eac
00283660  E9 1E F6 FF FF                  jmp 0x140282c83
00283665  48 89 48 08                     mov qword ptr [rax + 8], rcx
00283669  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0028366E  48 89 08                        mov qword ptr [rax], rcx
00283671  E9 D7 F9 FF FF                  jmp 0x14028304d
00283676  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0028367A  45 33 F6                        xor r14d, r14d
0028367D  80 39 05                        cmp byte ptr [rcx], 5
00283680  0F 85 16 FA FF FF               jne 0x14028309c
00283686  4C 8B F9                        mov r15, rcx
00283689  E9 0E FA FF FF                  jmp 0x14028309c
0028368E  48 0F BA 25 F1 33 D4 00 24      bt qword ptr [rip + 0xd433f1], 0x24
00283697  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
0028369F  72 74                           jb 0x140283715
002836A1  4C 8B B4 24 C8 00 00 00         mov r14, qword ptr [rsp + 0xc8]
002836A9  49 89 1E                        mov qword ptr [r14], rbx
002836AC  B8 10 01 00 00                  mov eax, 0x110
002836B1  E9 EF F6 FF FF                  jmp 0x140282da5
002836B6  8B 80 B0 00 00 00               mov eax, dword ptr [rax + 0xb0]
002836BC  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
002836C1  83 F8 01                        cmp eax, 1
002836C4  0F 8F F6 00 00 00               jg 0x1402837c0
002836CA  48 8B CF                        mov rcx, rdi
002836CD  E8 2E 22 03 00                  call 0x1402b5900
002836D2  E9 7A F6 FF FF                  jmp 0x140282d51
002836D7  48 8B CE                        mov rcx, rsi
002836DA  E8 5D 06 0F 00                  call 0x140373d3c
002836DF  85 C0                           test eax, eax
002836E1  0F 84 F9 FB FF FF               je 0x1402832e0
002836E7  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
002836EB  0F B6 4E 22                     movzx ecx, byte ptr [rsi + 0x22]
002836EF  C0 E9 04                        shr cl, 4
002836F2  A8 04                           test al, 4
002836F4  F6 D1                           not cl
002836F6  0F 95 C0                        setne al
002836F9  22 C8                           and cl, al
002836FB  F6 C1 01                        test cl, 1
002836FE  0F 84 DC FB FF FF               je 0x1402832e0
00283704  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
00283708  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0028370C  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
00283710  E9 CB FB FF FF                  jmp 0x1402832e0
00283715  F6 C3 20                        test bl, 0x20
00283718  75 87                           jne 0x1402836a1
0028371A  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00283724  48 8B C0                        mov rax, rax
00283727  4C 8B B4 24 C8 00 00 00         mov r14, qword ptr [rsp + 0xc8]
0028372F  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00283739  48 03 C1                        add rax, rcx
0028373C  4C 3B F0                        cmp r14, rax
0028373F  0F 82 64 FF FF FF               jb 0x1402836a9
00283745  41 B8 80 00 00 00               mov r8d, 0x80
0028374B  48 8B D3                        mov rdx, rbx
0028374E  49 8B CE                        mov rcx, r14
00283751  E8 2A F6 00 00                  call 0x140292d80
00283756  B8 10 01 00 00                  mov eax, 0x110
0028375B  49 89 1E                        mov qword ptr [r14], rbx
0028375E  E9 42 F6 FF FF                  jmp 0x140282da5
00283763  B9 03 00 00 00                  mov ecx, 3
00283768  CD 29                           int 0x29
0028376A  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0028376D  C1 E8 18                        shr eax, 0x18
00283770  A8 40                           test al, 0x40
00283772  0F 84 4E 6A 45 00               je 0x1406da1c6
00283778  BF 09 07 00 C0                  mov edi, 0xc0000709
0028377D  E9 78 F6 FF FF                  jmp 0x140282dfa
00283782  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0028378A  4C 8B CE                        mov r9, rsi
0028378D  49 8B 55 00                     mov rdx, qword ptr [r13]
00283791  4C 8B C3                        mov r8, rbx
00283794  49 8B CD                        mov rcx, r13
00283797  E8 A4 8F 1C 00                  call 0x14044c740
0028379C  48 8B F0                        mov rsi, rax
0028379F  48 85 C0                        test rax, rax
002837A2  0F 85 28 6A 45 00               jne 0x1406da1d0
002837A8  4D 85 F6                        test r14, r14
002837AB  0F 84 D9 F9 FF FF               je 0x14028318a
002837B1  B2 11                           mov dl, 0x11
002837B3  49 8B CE                        mov rcx, r14
002837B6  E8 D5 28 FC FF                  call 0x140246090
002837BB  E9 CA F9 FF FF                  jmp 0x14028318a
002837C0  48 8D 4F 38                     lea rcx, [rdi + 0x38]
002837C4  45 33 C0                        xor r8d, r8d
002837C7  33 D2                           xor edx, edx
002837C9  E8 42 BB 0B 00                  call 0x14033f310
002837CE  E9 F7 FE FF FF                  jmp 0x1402836ca
002837D3  BA 02 00 00 00                  mov edx, 2
002837D8  48 8B CE                        mov rcx, rsi
002837DB  E8 74 F0 01 00                  call 0x1402a2854
002837E0  40 F6 C7 04                     test dil, 4
002837E4  0F 84 F9 69 45 00               je 0x1406da1e3
002837EA  B8 FF FF 00 00                  mov eax, 0xffff
002837EF  66 41 01 45 42                  add word ptr [r13 + 0x42], ax
002837F4  E9 EA 69 45 00                  jmp 0x1406da1e3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiResolveTransitionFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p2A;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pE0;
    unsigned __int8 v_stack_pE2;
    unsigned __int8 v_stack_pE3;

    v_stack_p20 = a4;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    v_r11 = 0;
    v_stack_p8 = 0;
    v_stack_m48 = *(unsigned __int64 *)(a1 + 56);
    *(unsigned __int64 *)(a5) = 0;
    v_stack_m68 = *(unsigned __int64 *)(a1 + 16);
    v_stack_m70 = 0;
    if (a3 == 0) goto loc_00282E82;
    if (a2 < a1) goto loc_002829E2;
    if (a2 > a2) goto loc_002829E2;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) == 0) goto loc_002829E2;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00282E1C;
loc_002829E2:
    if (*(unsigned __int64 *)(v_rip + 12235415) == 0) goto loc_002829FF;
    result = *(unsigned __int64 *)(a2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 12235415);
        result = ~(result);
        result = (result) & (*(unsigned __int64 *)(a2));
    }
    result = (result) >> (12);
    result = (result) & (v_rdi);
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (a2);
loc_00282A28:
    if (((*(unsigned __int8 *)(v_rsi + 35)) & (16)) != 0) goto loc_0028376A;
    v_r15 = (unsigned int)((*(unsigned __int64 *)(a1 + 16)) & (1));
    if (condition_is_not_equal) goto loc_00282DB9;
loc_00282A3F:
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00283782;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 34))) & (8)) != 0) goto loc_00283533;
loc_00282A77:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 34))) & (32)) != 0) goto loc_002835BD;
    v_stack_m60 = 0;
    v_stack_m88 = v_stack_m70;
    v_stack_m90 = *(unsigned __int64 *)(a2);
    v_stack_m98 = v_stack_m60;
    result = MiHandleTransitionFault(a1, v_stack_p10, a3, v_rsi);
    if (sign_flag) goto loc_00282DA5;
    if (v_stack_m60 != 0) { v_rsi = v_stack_m60; }
loc_00282ACB:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) != 0) goto loc_00283251;
loc_00282AE3:
    result = (*(unsigned __int64 *)(a2)) >> (5);
    result = (unsigned int)((result) & (31));
    if (((unsigned int)(result)) == 24) {
        a1 = v_stack_p10;
        result = MI_READ_PTE_LOCK_FREE(a1, v_stack_p10, a3, v_rsi);
        a3 = result;
        a1 = 1;
        result = *(unsigned int *)(v_rsi + 32);
        result = (unsigned int)((result) >> (16));
        a2 = (unsigned __int8)(result);
        a2 = (unsigned int)((a2) >> (6));
        result = MiUpdateProtectionMask(a1, a2, a3, v_rsi);
        a2 = (unsigned int)(result);
        a2 = (a2) << (5);
        a1 = a2;
        a1 = (a1) ^ (a3);
        a1 = (a1) & (-993);
        a1 = (a1) ^ (a2);
        *(unsigned __int64 *)(v_stack_p10) = a1;
    }
    result = MiMakeTransitionPteValid(v_stack_p10, a2, a3, v_rsi);
    v_stack_p18 = result;
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12244283) + result * 8);
    if (condition_is_below) goto loc_00282B94;
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_rsi + 16))) >> (2));
    if (((1) & ((unsigned __int8)(a1))) == 0) goto loc_00282B94;
    result = (*(unsigned __int64 *)(v_rsi + 16)) >> (12);
    result = (unsigned int)((result) & (15));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12244283) + result * 8) + 1204))))) goto loc_00282B94;
    v_rdi = 0;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 34))) & (16)) == 0) goto loc_00283299;
loc_00282B94:
    if (condition_is_below) goto loc_00282BC7;
    result = *(unsigned __int64 *)(v_rsi + 16);
    if (!(condition_is_above_or_equal)) {
        a1 = v_stack_p18;
        result = MI_READ_PTE_LOCK_FREE(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12244283) + result * 8), a3, v_rsi);
        result = (result) | (64);
        a1 = v_stack_p18;
        a2 = result;
        result = MiWriteValidPteNewProtection(a1, a2, a3, v_rsi);
    }
    if (((v_stack_p18) & (0x800ULL)) == 0) goto loc_00282C0B;
    if (v_stack_p20 != 0) goto loc_00283194;
loc_00282BE4:
    if (((*(unsigned __int8 *)(v_rsi + 34)) & (16)) == 0) goto loc_002831F5;
    if (v_stack_p20 != 0) goto loc_00283216;
    if ((*(unsigned __int64 *)(a1)) >= result) goto loc_00283216;
loc_00282C0B:
    if (!sign_flag) goto loc_00282C83;
    v_r12 = 0;
    v_stack_m58 = v_stack_p18;
    if (v_stack_p10 < result) goto loc_00282C68;
    if (v_stack_p10 <= result) goto loc_00283602;
loc_00282C68:
    if (v_stack_p10 < result) goto loc_00283349;
loc_00282C77:
    *(unsigned __int64 *)(v_stack_p10) = v_stack_p18;
    if (0 != 0) goto loc_00283655;
loc_00282C83:
    if (a3 == 0) goto loc_00282D20;
    v_r12 = 0;
loc_00282C9E:
    if (condition_is_below) goto loc_00282FD0;
    if (sign_flag) goto loc_00282CD1;
    if (condition_is_below) goto loc_00282CD1;
    result = (*(unsigned __int64 *)(a3 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != 1) {
        result = *(unsigned __int64 *)(a3 + 8);
    }
    if (((*(unsigned __int64 *)(v_rsi + 40)) & (*(unsigned __int64 *)(a3))) != 0) goto loc_00282FF1;
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 32))) >> (16));
    result = (unsigned __int8)((result) & (223));
    v_stack_p2A = (unsigned __int8)(result);
    *(unsigned int *)(a3 + 32) = (unsigned int)((unsigned int)(a5));
    result = MiRemoveLockedPageChargeAndDecRef(a3, a2, a3, v_stack_p10);
loc_00282D11:
loc_00282D20:
    if (0 != 0) {
        a1 = v_stack_m50;
        a3 = 1;
        a2 = 0;
        result = MiReleasePageFileInfo(a1, a2, a3, v_stack_p10);
    }
    if (v_stack_m70 != 0) goto loc_002836B6;
loc_00282D51:
    if (!sign_flag) goto loc_00283090;
    v_rsi = (v_rsi) - (*(unsigned __int64 *)(v_rsi + 40));
    v_stack_m98 = v_stack_m68;
    a4 = 0;
    v_rsi = (v_rsi) >> (4);
    a2 = (a2) * (v_rsi);
    result = MiCompleteProtoPteFault(a1, a2, v_stack_p20, a4);
    if (!sign_flag) goto loc_00283167;
loc_00282DA5:
    v_rsp = (v_rsp) + (128);
    return result;
loc_00282DB9:
    v_r10 = (v_stack_p20) & (-2);
    if ((*(unsigned __int8 *)(v_r10)) != 1) goto loc_00282A3F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (24));
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10 + 80))) & (7));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_00283282;
loc_00282DE4:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (24));
    a3 = (unsigned int)((a3) & (7));
loc_00282DEC:
    if (((unsigned int)(v_r10)) == ((unsigned int)(a3))) goto loc_00282DF7;
    if (((unsigned int)(v_r10)) >= ((unsigned int)(a3))) goto loc_002833F2;
loc_00282DF7:
loc_00282DFA:
    if (a3 != 0) {
        a2 = 17;
        a1 = a3;
        result = MiUnlockProtoPoolPage(a1, a2, a3, a4);
    }
    goto loc_00282DA5;
loc_00282E1C:
    if (((*(unsigned __int64 *)(v_rip + 13909089)) & (0x600000ULL)) == 0) goto loc_002829E2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_002829E2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_002829E2;
    result = (v_r15) >> (3);
    result = (result) & (0);
    v_rbx = v_stack_p18;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        v_rbx = (v_stack_p18) | (32);
    }
    v_rbx = (v_rbx) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { v_rbx = v_rbx; }
    goto loc_002829E2;
loc_00282E82:
loc_00282E8C:
loc_00282E96:
    result = MI_READ_PTE_LOCK_FREE(v_r15, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288), a3, a4);
    if (condition_is_above_or_equal) goto loc_0028318A;
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00282E96;
    if (result == 0) goto loc_00282EC6;
    if (*(unsigned __int64 *)(v_rip + 12234179) != 0) goto loc_00282FBE;
loc_00282EC6:
    if (*(unsigned __int64 *)(v_rip + 12234163) == 0) goto loc_00282EE7;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_00283087;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12234163));
    a1 = (a1) & (result);
loc_00282EE7:
    a1 = (a1) >> (12);
    a1 = (a1) & (0);
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if (a1 > (*(unsigned __int64 *)(v_rip + 12234209))) goto loc_00282E8C;
    if (a1 >= (*(unsigned __int64 *)(v_rip + 12234209))) goto loc_00282E8C;
    v_r12 = 0;
loc_00282F30:
    if (condition_is_below) goto loc_00283230;
    result = MI_READ_PTE_LOCK_FREE(v_r15, a2, a3, a4);
    if (result != result) goto loc_0028330B;
    result = (*(unsigned __int64 *)(v_rsi + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00283171;
loc_00282F79:
    result = (*(unsigned __int64 *)(v_rsi + a2 * 8 + 8)) | (*(unsigned __int64 *)(v_rip + 12243239));
    if (result != v_r15) goto loc_0028354F;
loc_00282F93:
    if (v_rsi + a2 * 8 == 0) goto loc_0028318A;
    result = MI_READ_PTE_LOCK_FREE(v_r15, a2, a3, a4);
    v_r11 = 0;
    goto loc_00282A28;
loc_00282FBE:
    if (result != 0) goto loc_00282EC6;
    goto loc_00282E96;
loc_00282FD0:
    v_r12 = (unsigned int)((a5) + 1);
    if (((*(unsigned int *)(v_rip + 13902546)) & ((unsigned int)(v_r12))) == 0) goto loc_0028350B;
loc_00282FE0:
loc_00282FE2:
    if (!sign_flag) goto loc_00282C9E;
    goto loc_00282FD0;
loc_00282FF1:
    result = (*(unsigned __int64 *)(a3 + 24)) & (-2);
    result = (result) | (v_r15);
    if ((*(unsigned __int64 *)(result * 8)) == (result * 8)) goto loc_002835A5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result * 8) + 8)) != (result * 8)) goto loc_00283763;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result * 8)) + 8)) != (*(unsigned __int64 *)(result * 8))) goto loc_00283763;
    *(unsigned __int64 *)(result * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(result * 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result * 8)) + 8) = result * 8;
    if ((*(unsigned __int64 *)(result * 8)) != (result * 8)) goto loc_00283665;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result * 8)) = *(unsigned __int64 *)(result * 8);
loc_0028304D:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result * 8) + 8) = *(unsigned __int64 *)(result * 8);
    a1 = (*(unsigned __int64 *)(result * 8)) >> (3);
    a2 = (a1) ^ (*(unsigned __int64 *)(a3));
    a2 = (a2) & (v_stack_p50);
    a2 = (a2) ^ (a1);
    *(unsigned __int64 *)(a3) = a2;
loc_00283071:
    result = MiRemoveLockedPageChargeAndDecRef(a3, a2, v_stack_p50, a4);
    *(unsigned int *)(result * 8 + 16) = 1;
    goto loc_00282D11;
loc_00283087:
    a1 = (a3) & (-17);
    goto loc_00282EE7;
loc_00283090:
    if (v_r15 != 0) goto loc_0028342C;
    v_r14 = 0;
loc_0028309C:
    if (((*(unsigned __int8 *)(a1 + 69)) & (16)) != 0) goto loc_002834DB;
loc_002830A7:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + 69))) & (9));
    if (((unsigned __int8)(result)) != 8) goto loc_0028312A;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 69))) & (4)) != 0) goto loc_0028312A;
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 66)) == 0) goto loc_00283110;
    a1 = (unsigned int)((*(unsigned __int16 *)(a1 + 64)) + ((unsigned int)(*(unsigned __int16 *)(a1 + 66))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_pC8))) >> (3));
    result = (unsigned int)((result) & (511));
    if (((unsigned int)(a1)) != ((unsigned int)(result))) goto loc_002830F9;
    if (sign_flag) goto loc_002832FB;
    result = *(unsigned __int64 *)(v_rsi + a2 * 8 + 40);
    if (((*(unsigned __int8 *)(a1 + 69)) & (2)) == 0) {
        a1 = a1 + 56;
        result = MiEmptyDeferredWorkingSetEntries(a1, v_stack_pC8, 511, a4);
        a2 = v_stack_pC8;
        a3 = 511;
    }
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 66)) == 0) goto loc_0028331F;
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 66)) + 1);
    *(unsigned __int16 *)(a1 + 66) = (unsigned __int16)(result);
loc_00283126:
    v_r14 = (unsigned int)((v_r14) | (4));
loc_0028312A:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) | (16));
    v_stack_p30 = v_r15;
    if (((*(unsigned __int8 *)(a1 + 69)) & (1)) == 0) { v_rdi = (unsigned int)(v_r14); }
    a4 = 0;
    v_stack_p28 = (unsigned int)(v_rdi);
    v_stack_p20 = result;
    result = MiAllocateWsle(v_stack_p70, v_stack_pC8, v_rsi + a2 * 8, a4);
    if ((unsigned int)(result) == 0) goto loc_002837D3;
loc_00283167:
    goto loc_00282DA5;
loc_00283171:
    result = MiLockSpecialPurposeMemoryCachedPage(v_rsi + a2 * 8, 2, v_rsi + a2 * 8, a4);
    if (result != 0) goto loc_00282F79;
loc_0028318A:
    goto loc_00282DA5;
loc_00283194:
    if ((*(unsigned __int64 *)(a1)) > (v_rsi + a2 * 8)) goto loc_00282BE4;
    if (((v_stack_pD0) & (*(unsigned __int64 *)(gs_base + (0 + 392)))) == 0) goto loc_002835EF;
loc_002831D0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1912) == 0) goto loc_00282BE4;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1912)) + (24);
    if ((*(unsigned __int64 *)(result)) == result) goto loc_00282BE4;
loc_002831ED:
    v_r12 = 0;
    goto loc_00282BE4;
loc_002831F5:
    if (0 == 0) goto loc_00282C0B;
    if (sign_flag) goto loc_00282C0B;
    result = MiCaptureDirtyBitToPfn(result, 2, v_rsi + a2 * 8, a4);
loc_00283216:
    goto loc_00282C0B;
loc_00283230:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 13901938)) & ((unsigned int)(v_r12))) == 0) goto loc_0028357D;
loc_00283240:
loc_00283242:
    if (!sign_flag) goto loc_00282F30;
    goto loc_00283230;
loc_00283251:
    a1 = (result) & (-2);
    if ((*(unsigned __int8 *)(a1)) != 4) goto loc_00282AE3;
    result = (*(unsigned __int64 *)(result)) & (-865);
    *(unsigned __int64 *)(result) = result;
    result = (result) & (-865);
    goto loc_00282AE3;
loc_00283282:
    if (result >= 2) goto loc_0028337F;
loc_0028328E:
    goto loc_00282DEC;
loc_00283299:
    a1 = (unsigned __int8)((a1) >> (3));
    a1 = (unsigned __int8)(~(a1));
    result = (condition_is_above_or_equal) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002832C6;
    v_stack_p40 = *(unsigned __int64 *)(result + 16);
    result = (unsigned __int8)((*(unsigned __int64 *)(result + 16)) >> (2));
    if ((unsigned __int8)(result) != 0) goto loc_00283635;
    v_stack_p40 = result;
loc_002832C6:
    v_stack_pE0 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32)));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (16));
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) goto loc_002836D7;
loc_002832E0:
    v_r11 = (unsigned __int8)(((unsigned __int8)(v_rbx)) | (16));
    v_stack_pE2 = (unsigned __int8)(v_r11);
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(a5));
    goto loc_00282B94;
loc_002832FB:
    if (((*(unsigned __int8 *)(a1 + 69)) & (2)) != 0) goto loc_002830F9;
    goto loc_00283110;
loc_0028330B:
    goto loc_00282E8C;
loc_0028331F:
    *(unsigned __int16 *)(a1 + 66) = (unsigned __int16)(v_r12);
    result = (unsigned int)((2) >> (3));
    result = (unsigned __int16)((result) & (5));
    *(unsigned __int16 *)(a1 + 64) = (unsigned __int16)(result);
    if (!sign_flag) goto loc_00283501;
    goto loc_00283126;
loc_00283349:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_00282C77;
    a1 = (2) + (5);
    if (0 < a1) goto loc_00282C77;
    result = MiCheckLinearProtectedPteAccessedBit(0, v_rbx, 128, a4);
    goto loc_00282C77;
loc_0028337F:
    a1 = (*(unsigned __int64 *)(v_rip + 12233050) + *(unsigned __int64 *)(v_rip + 12233050) * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 12233050));
    if (result >= a1) goto loc_0028328E;
    a1 = (result) - (v_rbx);
    a1 = (a1) >> (4);
    a1 = (a1) * (v_rbx);
    result = MiIsDecayPfn(a1, v_rbx, 128, v_stack_pC8);
    if ((unsigned int)(result) != 0) goto loc_0028328E;
    result = (unsigned int)((128) >> (16));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 6) goto loc_00282DE4;
    result = MiGetPfnSlabType(result, v_rbx, 128, v_stack_pC8);
    if (((unsigned int)(result)) != 9) goto loc_00282DE4;
    goto loc_0028328E;
loc_002833F2:
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 34)) & (7));
    if (((unsigned __int8)(result)) == 2) goto loc_0028345C;
    if (((unsigned __int8)(result)) == 6) {
        result = *(unsigned __int64 *)(result + 24);
    }
    v_stack_pE0 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (24));
    result = (unsigned __int8)((result) & (248));
    result = (unsigned __int8)((result) | ((unsigned __int8)(v_r10)));
    v_stack_pE3 = (unsigned __int8)(result);
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(a5));
    goto loc_00282DF7;
loc_0028342C:
    result = (v_stack_p50) & (-2);
    if ((*(unsigned __int8 *)(result)) == 4) goto loc_0028368E;
    v_r15 = 0;
    result = (v_stack_p50) & (-2);
    if ((*(unsigned __int8 *)(result)) != 3) goto loc_00283676;
    goto loc_0028309C;
loc_0028345C:
    if (128 != 0) goto loc_002834C8;
    if (condition_is_below) goto loc_002834C8;
    result = (*(unsigned __int64 *)(result + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_002834C8;
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(result + 16))) >> (2));
    if ((((unsigned __int8)(a2)) & (1)) == 0) goto loc_002834C8;
    a1 = (*(unsigned __int64 *)(result + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    result = (*(unsigned __int64 *)(result + 16)) >> (12);
    result = (unsigned int)((result) & (15));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12241892) + a1 * 8) + 1204))))) goto loc_00282DF7;
loc_002834C8:
    result = MiRelinkStandbyPage(result, (unsigned int)((unsigned int)(v_r10)), *(unsigned __int64 *)(v_rip + 12241892), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12241892) + a1 * 8));
    v_r11 = 0;
    goto loc_00282DF7;
loc_002834DB:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) == 0) goto loc_002834F0;
    result = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 2) goto loc_002830A7;
loc_002834F0:
    v_rbx = (v_stack_pD0) & (-33);
    goto loc_002830A7;
loc_00283501:
    goto loc_00283126;
loc_0028350B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13907367)))) & (64)) == 0) goto loc_00282FE0;
    result = KiCheckVpBackingLongSpinWaitHypercall(result, (unsigned int)((unsigned int)(v_r10)), *(unsigned __int64 *)(v_rip + 12241892), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12241892) + a1 * 8));
    if ((unsigned __int8)(result) == 0) goto loc_00282FE0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)(v_r10)), *(unsigned __int64 *)(v_rip + 12241892), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12241892) + a1 * 8));
    goto loc_00282FE2;
loc_00283533:
    result = MiCheckWriteInProgressFault(result, (unsigned int)((unsigned int)(v_r10)), *(unsigned __int64 *)(v_rip + 12241892), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12241892) + a1 * 8));
    if (!sign_flag) goto loc_00282A77;
    goto loc_00282DFA;
loc_0028354F:
    if (condition_is_below) goto loc_00282F93;
    v_stack_p20 = *(unsigned __int64 *)(result + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x411ULL), 0, v_rbx);
loc_0028357D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13907253)))) & (64)) == 0) goto loc_00283240;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (unsigned int)(0x411ULL), 0, v_rbx);
    if ((unsigned __int8)(result) == 0) goto loc_00283240;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x411ULL), 0, v_rbx);
    goto loc_00283242;
loc_002835A5:
    result = (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_r12)))) & (0);
    *(unsigned __int64 *)((unsigned int)((unsigned int)(v_r12))) = result;
    goto loc_00283071;
loc_002835BD:
    v_stack_p28 = v_stack_pC0;
    v_stack_p20 = v_r12;
    result = MiHandleCollidedFault((unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x411ULL), 0, v_rbx);
    if (v_stack_pC0 <= 1) goto loc_00282DA5;
    if (sign_flag) goto loc_00282DA5;
    goto loc_00282ACB;
loc_002835EF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r12)) + 500)))) & (16)) == 0) goto loc_002831D0;
    goto loc_002831ED;
loc_00283602:
    result = MiSanitizeShadowPxe((unsigned int)((unsigned int)(v_r12)), v_stack_p60, 0, v_rbx);
    goto loc_00282C68;
loc_00283635:
    result = (*(unsigned __int64 *)(result + 16)) & (-5);
    *(unsigned __int64 *)(result + 16) = result;
    result = MiClearPageFileReservation(v_stack_p40, v_stack_p60, 0, v_stack_pC8);
    goto loc_002832C6;
loc_00283655:
    result = MiWritePteShadow(v_stack_pC8, v_stack_p60, 0, v_stack_pC8);
    goto loc_00282C83;
loc_00283665:
    *(unsigned __int64 *)(result + 8) = v_stack_pC8;
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8)) = v_stack_pC8;
    goto loc_0028304D;
loc_00283676:
    a1 = (v_stack_pC8) & (-2);
    v_r14 = 0;
    if ((*(unsigned __int8 *)(a1)) != 5) goto loc_0028309C;
    goto loc_0028309C;
loc_0028368E:
    if ((*(unsigned __int8 *)(a1)) < 5) goto loc_00283715;
loc_002836A1:
loc_002836A9:
    *(unsigned __int64 *)(v_stack_pC8) = v_stack_pD0;
    goto loc_00282DA5;
loc_002836B6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(272 + 176)))) > 1) goto loc_002837C0;
loc_002836CA:
    result = MiFreeInPageSupportBlock(v_stack_p48, v_stack_p60, 0, v_stack_pC8);
    goto loc_00282D51;
loc_002836D7:
    result = MiCanPfnOriginalPteBeLost(result, v_stack_p60, 0, v_stack_pC8);
    if ((unsigned int)(result) == 0) goto loc_002832E0;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result + 34)) >> (4));
    a1 = (unsigned __int8)(~(a1));
    result = ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (4)) != 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) == 0) goto loc_002832E0;
    result = (*(unsigned __int64 *)(result + 16)) & (-5);
    *(unsigned __int64 *)(result + 16) = result;
    goto loc_002832E0;
loc_00283715:
    if ((((unsigned __int8)(v_stack_pD0)) & (32)) != 0) goto loc_002836A1;
    result = (result) + (a1);
    if (v_stack_pC8 < result) goto loc_002836A9;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_pC8, v_stack_pD0, 128, v_stack_pC8);
    *(unsigned __int64 *)(v_stack_pC8) = v_stack_pD0;
    goto loc_00282DA5;
loc_00283763:
loc_0028376A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (24));
    goto loc_00282DFA;
loc_00283782:
    result = MiHandleSpecialPurposeMemoryCachedFault(a1, *(unsigned __int64 *)(a1), v_stack_pC8, result);
    if (v_stack_pC8 == 0) goto loc_0028318A;
    result = MiUnlockProtoPoolPage(v_stack_pC8, 17, v_stack_pC8, result);
    goto loc_0028318A;
loc_002837C0:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent((unsigned int)(0xC0000709ULL) + 56, a2, a3, result);
    goto loc_002836CA;
loc_002837D3:
    result = MiLockAndDecrementShareCount(result, 2, a3, result);
}
```

## 5. (Beta) C Style

```c
int64_t MiResolveTransitionFault(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint8_t v_stack_p2A;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p70;
    uint32_t v_stack_p8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pE0;
    uint8_t v_stack_pE2;
    uint8_t v_stack_pE3;

    v_stack_p20 = Arg4;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    local_r11 = 0;
    v_stack_p8 = 0;
    v_stack_m48 = *(uint64_t *)(arg1 + 0x38);
    *(uint64_t *)(arg5) = 0;
    v_stack_m68 = *(uint64_t *)(arg1 + 0x10);
    v_stack_m70 = 0;
    if (Arg3 == 0) goto loc_00282E82;
    if (Arg2 < Arg1) goto loc_002829E2;
    if (Arg2 > Arg2) goto loc_002829E2;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (1)) == 0) goto loc_002829E2;
    Arg1 = ((((uint8_t)(*(uint64_t *)(arg2))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(arg2))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00282E1C;
loc_002829E2:
    if (*(uint64_t *)(v_rip + 0xBAB297) == 0) goto loc_002829FF;
    result = *(uint64_t *)(arg2);
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xBAB297);
        result = ~(result);
        result = (result) & (*(uint64_t *)(arg2));
    }
    result = (result) >> (12);
    result = (result) & (local_rdi);
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (Arg2);
loc_00282A28:
    if (((*(uint8_t *)(local_rsi + 0x23)) & (16)) != 0) goto loc_0028376A;
    local_r15 = (uint32_t)((*(uint64_t *)(arg1 + 0x10)) & (1));
    if (condition_is_not_equal) goto loc_00282DB9;
loc_00282A3F:
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00283782;
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x22))) & (8)) != 0) goto loc_00283533;
loc_00282A77:
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x22))) & (32)) != 0) goto loc_002835BD;
    v_stack_m60 = 0;
    v_stack_m88 = v_stack_m70;
    v_stack_m90 = *(uint64_t *)(arg2);
    v_stack_m98 = v_stack_m60;
    result = MiHandleTransitionFault(Arg1, v_stack_p10, Arg3, local_rsi);
    if (sign_flag) goto loc_00282DA5;
    if (v_stack_m60 != 0) { local_rsi = v_stack_m60; }
loc_00282ACB:
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) != 0) goto loc_00283251;
loc_00282AE3:
    result = (*(uint64_t *)(arg2)) >> (5);
    result = (uint32_t)((result) & (31));
    if (((uint32_t)(result)) == 24) {
        Arg1 = v_stack_p10;
        result = MI_READ_PTE_LOCK_FREE(Arg1, v_stack_p10, Arg3, local_rsi);
        Arg3 = result;
        Arg1 = 1;
        result = *(uint32_t *)(local_rsi + 0x20);
        result = (uint32_t)((result) >> (16));
        Arg2 = (uint8_t)(result);
        Arg2 = (uint32_t)((Arg2) >> (6));
        result = MiUpdateProtectionMask(Arg1, Arg2, Arg3, local_rsi);
        Arg2 = (uint32_t)(result);
        Arg2 = (Arg2) << (5);
        Arg1 = Arg2;
        Arg1 = (Arg1) ^ (Arg3);
        Arg1 = (Arg1) & (-993);
        Arg1 = (Arg1) ^ (Arg2);
        *(void **)(v_stack_p10) = Arg1;
    }
    result = MiMakeTransitionPteValid(v_stack_p10, Arg2, Arg3, local_rsi);
    v_stack_p18 = result;
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAD53B) + result * 8);
    if (condition_is_below) goto loc_00282B94;
    Arg1 = (uint8_t)(((uint8_t)(*(uint64_t *)(local_rsi + 0x10))) >> (2));
    if (((1) & ((uint8_t)(Arg1))) == 0) goto loc_00282B94;
    result = (*(uint64_t *)(local_rsi + 0x10)) >> (12);
    result = (uint32_t)((result) & (15));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBAD53B) + result * 8) + 0x4B4))))) goto loc_00282B94;
    local_rdi = 0;
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x22))) & (16)) == 0) goto loc_00283299;
loc_00282B94:
    if (condition_is_below) goto loc_00282BC7;
    result = *(uint64_t *)(local_rsi + 0x10);
    if (!(condition_is_above_or_equal)) {
        Arg1 = v_stack_p18;
        result = MI_READ_PTE_LOCK_FREE(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAD53B) + result * 8), Arg3, local_rsi);
        result = (result) | (64);
        Arg1 = v_stack_p18;
        Arg2 = result;
        result = MiWriteValidPteNewProtection(Arg1, Arg2, Arg3, local_rsi);
    }
    if (((v_stack_p18) & (0x800ULL)) == 0) goto loc_00282C0B;
    if (v_stack_p20 != 0) goto loc_00283194;
loc_00282BE4:
    if (((*(uint8_t *)(local_rsi + 0x22)) & (16)) == 0) goto loc_002831F5;
    if (v_stack_p20 != 0) goto loc_00283216;
    if ((*(uint64_t *)(arg1)) >= result) goto loc_00283216;
loc_00282C0B:
    if (!sign_flag) goto loc_00282C83;
    local_r12 = 0;
    v_stack_m58 = v_stack_p18;
    if (v_stack_p10 < result) goto loc_00282C68;
    if (v_stack_p10 <= result) goto loc_00283602;
loc_00282C68:
    if (v_stack_p10 < result) goto loc_00283349;
loc_00282C77:
    *(uint64_t *)(v_stack_p10) = v_stack_p18;
    if (0 != 0) goto loc_00283655;
loc_00282C83:
    if (Arg3 == 0) goto loc_00282D20;
    local_r12 = 0;
loc_00282C9E:
    if (condition_is_below) goto loc_00282FD0;
    if (sign_flag) goto loc_00282CD1;
    if (condition_is_below) goto loc_00282CD1;
    result = (*(uint64_t *)(Arg3 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != 1) {
        result = *(uint64_t *)(Arg3 + 0x8);
    }
    if (((*(uint64_t *)(local_rsi + 0x28)) & (*(uint64_t *)(Arg3))) != 0) goto loc_00282FF1;
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x20))) >> (16));
    result = (uint8_t)((result) & (223));
    v_stack_p2A = (uint8_t)(result);
    *(uint32_t *)(Arg3 + 0x20) = (uint32_t)((uint32_t)(Arg5));
    result = MiRemoveLockedPageChargeAndDecRef(Arg3, Arg2, Arg3, v_stack_p10);
loc_00282D11:
loc_00282D20:
    if (0 != 0) {
        Arg1 = v_stack_m50;
        Arg3 = 1;
        Arg2 = 0;
        result = MiReleasePageFileInfo(Arg1, Arg2, Arg3, v_stack_p10);
    }
    if (v_stack_m70 != 0) goto loc_002836B6;
loc_00282D51:
    if (!sign_flag) goto loc_00283090;
    local_rsi = (local_rsi) - (*(uint64_t *)(local_rsi + 0x28));
    v_stack_m98 = v_stack_m68;
    Arg4 = 0;
    local_rsi = (local_rsi) >> (4);
    Arg2 = (Arg2) * (local_rsi);
    result = MiCompleteProtoPteFault(Arg1, Arg2, v_stack_p20, Arg4);
    if (!sign_flag) goto loc_00283167;
loc_00282DA5:
    local_rsp = (local_rsp) + (128);
    return result;
loc_00282DB9:
    local_r10 = (v_stack_p20) & (-2);
    if ((*(uint8_t *)(local_r10)) != 1) goto loc_00282A3F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (24));
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10 + 0x50))) & (7));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_00283282;
loc_00282DE4:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (24));
    Arg3 = (uint32_t)((Arg3) & (7));
loc_00282DEC:
    if (((uint32_t)(local_r10)) == ((uint32_t)(Arg3))) goto loc_00282DF7;
    if (((uint32_t)(local_r10)) >= ((uint32_t)(Arg3))) goto loc_002833F2;
loc_00282DF7:
loc_00282DFA:
    if (Arg3 != 0) {
        Arg2 = 17;
        Arg1 = Arg3;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_00282DA5;
loc_00282E1C:
    if (((*(uint64_t *)(v_rip + 0xD43C61)) & (0x600000ULL)) == 0) goto loc_002829E2;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_002829E2;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_002829E2;
    result = (local_r15) >> (3);
    result = (result) & (0);
    local_rbx = v_stack_p18;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        local_rbx = (v_stack_p18) | (32);
    }
    local_rbx = (local_rbx) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { local_rbx = local_rbx; }
    goto loc_002829E2;
loc_00282E82:
loc_00282E8C:
loc_00282E96:
    result = MI_READ_PTE_LOCK_FREE(local_r15, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508), Arg3, Arg4);
    if (condition_is_above_or_equal) goto loc_0028318A;
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00282E96;
    if (result == 0) goto loc_00282EC6;
    if (*(uint64_t *)(v_rip + 0xBAADC3) != 0) goto loc_00282FBE;
loc_00282EC6:
    if (*(uint64_t *)(v_rip + 0xBAADB3) == 0) goto loc_00282EE7;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_00283087;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xBAADB3));
    Arg1 = (Arg1) & (result);
loc_00282EE7:
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (0);
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xBAADE1))) goto loc_00282E8C;
    if (Arg1 >= (*(uint64_t *)(v_rip + 0xBAADE1))) goto loc_00282E8C;
    local_r12 = 0;
loc_00282F30:
    if (condition_is_below) goto loc_00283230;
    result = MI_READ_PTE_LOCK_FREE(local_r15, Arg2, Arg3, Arg4);
    if (result != result) goto loc_0028330B;
    result = (*(uint64_t *)(local_rsi + arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00283171;
loc_00282F79:
    result = (*(uint64_t *)(local_rsi + arg2 * 8 + 0x8)) | (*(uint64_t *)(v_rip + 0xBAD127));
    if (result != local_r15) goto loc_0028354F;
loc_00282F93:
    if (local_rsi + Arg2 * 8 == 0) goto loc_0028318A;
    result = MI_READ_PTE_LOCK_FREE(local_r15, Arg2, Arg3, Arg4);
    local_r11 = 0;
    goto loc_00282A28;
loc_00282FBE:
    if (result != 0) goto loc_00282EC6;
    goto loc_00282E96;
loc_00282FD0:
    local_r12 = (uint32_t)((Arg5) + 1);
    if (((*(uint32_t *)(v_rip + 0xD422D2)) & ((uint32_t)(local_r12))) == 0) goto loc_0028350B;
loc_00282FE0:
loc_00282FE2:
    if (!sign_flag) goto loc_00282C9E;
    goto loc_00282FD0;
loc_00282FF1:
    result = (*(uint64_t *)(Arg3 + 0x18)) & (-2);
    result = (result) | (local_r15);
    if ((*(uint64_t *)(result * 8)) == (result * 8)) goto loc_002835A5;
    if ((*(uint64_t *)(*(uint64_t *)(result * 8) + 0x8)) != (result * 8)) goto loc_00283763;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result * 8)) + 0x8)) != (*(uint64_t *)(result * 8))) goto loc_00283763;
    *(uint64_t *)(result * 8) = *(uint64_t *)(*(uint64_t *)(result * 8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result * 8)) + 0x8) = result * 8;
    if ((*(uint64_t *)(result * 8)) != (result * 8)) goto loc_00283665;
    *(uint64_t *)(*(uint64_t *)(result * 8)) = *(uint64_t *)(result * 8);
loc_0028304D:
    *(uint64_t *)(*(uint64_t *)(result * 8) + 0x8) = *(uint64_t *)(result * 8);
    Arg1 = (*(uint64_t *)(result * 8)) >> (3);
    Arg2 = (Arg1) ^ (*(uint64_t *)(Arg3));
    Arg2 = (Arg2) & (v_stack_p50);
    Arg2 = (Arg2) ^ (Arg1);
    *(void **)(Arg3) = Arg2;
loc_00283071:
    result = MiRemoveLockedPageChargeAndDecRef(Arg3, Arg2, v_stack_p50, Arg4);
    *(uint32_t *)(result * 8 + 0x10) = 1;
    goto loc_00282D11;
loc_00283087:
    Arg1 = (Arg3) & (-17);
    goto loc_00282EE7;
loc_00283090:
    if (local_r15 != 0) goto loc_0028342C;
    local_r14 = 0;
loc_0028309C:
    if (((*(uint8_t *)(arg1 + 0x45)) & (16)) != 0) goto loc_002834DB;
loc_002830A7:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + 0x45))) & (9));
    if (((uint8_t)(result)) != 8) goto loc_0028312A;
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x45))) & (4)) != 0) goto loc_0028312A;
    if ((uint16_t)(*(uint16_t *)(arg1 + 0x42)) == 0) goto loc_00283110;
    Arg1 = (uint32_t)((*(uint16_t *)(arg1 + 0x40)) + ((uint32_t)(*(uint16_t *)(arg1 + 0x42))));
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_pC8))) >> (3));
    result = (uint32_t)((result) & (511));
    if (((uint32_t)(Arg1)) != ((uint32_t)(result))) goto loc_002830F9;
    if (sign_flag) goto loc_002832FB;
    result = *(uint64_t *)(local_rsi + arg2 * 8 + 0x28);
    if (((*(uint8_t *)(arg1 + 0x45)) & (2)) == 0) {
        Arg1 = Arg1 + 56;
        result = MiEmptyDeferredWorkingSetEntries(Arg1, v_stack_pC8, 511, Arg4);
        Arg2 = v_stack_pC8;
        Arg3 = 511;
    }
    if ((uint16_t)(*(uint16_t *)(arg1 + 0x42)) == 0) goto loc_0028331F;
    result = (uint16_t)((*(uint16_t *)(arg1 + 0x42)) + 1);
    *(uint16_t *)(arg1 + 0x42) = (uint16_t)(result);
loc_00283126:
    local_r14 = (uint32_t)((local_r14) | (4));
loc_0028312A:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) | (16));
    v_stack_p30 = local_r15;
    if (((*(uint8_t *)(arg1 + 0x45)) & (1)) == 0) { local_rdi = (uint32_t)(local_r14); }
    Arg4 = 0;
    v_stack_p28 = (uint32_t)(local_rdi);
    v_stack_p20 = result;
    result = MiAllocateWsle(v_stack_p70, v_stack_pC8, local_rsi + Arg2 * 8, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002837D3;
loc_00283167:
    goto loc_00282DA5;
loc_00283171:
    result = MiLockSpecialPurposeMemoryCachedPage(local_rsi + Arg2 * 8, 2, local_rsi + Arg2 * 8, Arg4);
    if (result != 0) goto loc_00282F79;
loc_0028318A:
    goto loc_00282DA5;
loc_00283194:
    if ((*(uint64_t *)(arg1)) > (local_rsi + Arg2 * 8)) goto loc_00282BE4;
    if (((v_stack_pD0) & (*(uint64_t *)(gs_base + (0 + 0x188)))) == 0) goto loc_002835EF;
loc_002831D0:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x778) == 0) goto loc_00282BE4;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x778)) + (24);
    if ((*(uint64_t *)(result)) == result) goto loc_00282BE4;
loc_002831ED:
    local_r12 = 0;
    goto loc_00282BE4;
loc_002831F5:
    if (0 == 0) goto loc_00282C0B;
    if (sign_flag) goto loc_00282C0B;
    result = MiCaptureDirtyBitToPfn(result, 2, local_rsi + Arg2 * 8, Arg4);
loc_00283216:
    goto loc_00282C0B;
loc_00283230:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xD42072)) & ((uint32_t)(local_r12))) == 0) goto loc_0028357D;
loc_00283240:
loc_00283242:
    if (!sign_flag) goto loc_00282F30;
    goto loc_00283230;
loc_00283251:
    Arg1 = (result) & (-2);
    if ((*(uint8_t *)(arg1)) != 4) goto loc_00282AE3;
    result = (*(uint64_t *)(result)) & (-865);
    *(uint64_t *)(result) = result;
    result = (result) & (-865);
    goto loc_00282AE3;
loc_00283282:
    if (result >= 2) goto loc_0028337F;
loc_0028328E:
    goto loc_00282DEC;
loc_00283299:
    Arg1 = (uint8_t)((Arg1) >> (3));
    Arg1 = (uint8_t)(~(Arg1));
    result = (condition_is_above_or_equal) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002832C6;
    v_stack_p40 = *(uint64_t *)(result + 0x10);
    result = (uint8_t)((*(uint64_t *)(result + 0x10)) >> (2));
    if ((uint8_t)(result) != 0) goto loc_00283635;
    v_stack_p40 = result;
loc_002832C6:
    v_stack_pE0 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (16));
    if ((((uint8_t)(local_rbx)) & (8)) != 0) goto loc_002836D7;
loc_002832E0:
    local_r11 = (uint8_t)(((uint8_t)(local_rbx)) | (16));
    v_stack_pE2 = (uint8_t)(local_r11);
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(Arg5));
    goto loc_00282B94;
loc_002832FB:
    if (((*(uint8_t *)(arg1 + 0x45)) & (2)) != 0) goto loc_002830F9;
    goto loc_00283110;
loc_0028330B:
    goto loc_00282E8C;
loc_0028331F:
    *(uint16_t *)(arg1 + 0x42) = (uint16_t)(local_r12);
    result = (uint32_t)((2) >> (3));
    result = (uint16_t)((result) & (5));
    *(uint16_t *)(arg1 + 0x40) = (uint16_t)(result);
    if (!sign_flag) goto loc_00283501;
    goto loc_00283126;
loc_00283349:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_00282C77;
    Arg1 = (2) + (5);
    if (0 < Arg1) goto loc_00282C77;
    result = MiCheckLinearProtectedPteAccessedBit(0, local_rbx, 128, Arg4);
    goto loc_00282C77;
loc_0028337F:
    Arg1 = (*(uint64_t *)(v_rip + 0xBAA95A) + *(uint64_t *)(v_rip + 0xBAA95A) * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xBAA95A));
    if (result >= Arg1) goto loc_0028328E;
    Arg1 = (result) - (local_rbx);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (local_rbx);
    result = MiIsDecayPfn(Arg1, local_rbx, 128, v_stack_pC8);
    if ((uint32_t)(result) != 0) goto loc_0028328E;
    result = (uint32_t)((128) >> (16));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 6) goto loc_00282DE4;
    result = MiGetPfnSlabType(result, local_rbx, 128, v_stack_pC8);
    if (((uint32_t)(result)) != 9) goto loc_00282DE4;
    goto loc_0028328E;
loc_002833F2:
    result = (uint8_t)((*(uint8_t *)(result + 0x22)) & (7));
    if (((uint8_t)(result)) == 2) goto loc_0028345C;
    if (((uint8_t)(result)) == 6) {
        result = *(uint64_t *)(result + 0x18);
    }
    v_stack_pE0 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (24));
    result = (uint8_t)((result) & (248));
    result = (uint8_t)((result) | ((uint8_t)(local_r10)));
    v_stack_pE3 = (uint8_t)(result);
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(Arg5));
    goto loc_00282DF7;
loc_0028342C:
    result = (v_stack_p50) & (-2);
    if ((*(uint8_t *)(result)) == 4) goto loc_0028368E;
    local_r15 = 0;
    result = (v_stack_p50) & (-2);
    if ((*(uint8_t *)(result)) != 3) goto loc_00283676;
    goto loc_0028309C;
loc_0028345C:
    if (128 != 0) goto loc_002834C8;
    if (condition_is_below) goto loc_002834C8;
    result = (*(uint64_t *)(result + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_002834C8;
    Arg2 = (uint8_t)(((uint8_t)(*(uint64_t *)(result + 0x10))) >> (2));
    if ((((uint8_t)(Arg2)) & (1)) == 0) goto loc_002834C8;
    Arg1 = (*(uint64_t *)(result + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    result = (*(uint64_t *)(result + 0x10)) >> (12);
    result = (uint32_t)((result) & (15));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBACBE4) + arg1 * 8) + 0x4B4))))) goto loc_00282DF7;
loc_002834C8:
    result = MiRelinkStandbyPage(result, (uint32_t)((uint32_t)(local_r10)), *(uint64_t *)(v_rip + 0xBACBE4), *(uint64_t *)(*(uint64_t *)(v_rip + 0xBACBE4) + arg1 * 8));
    local_r11 = 0;
    goto loc_00282DF7;
loc_002834DB:
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) == 0) goto loc_002834F0;
    result = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if ((*(uint8_t *)(result)) == 2) goto loc_002830A7;
loc_002834F0:
    local_rbx = (v_stack_pD0) & (-33);
    goto loc_002830A7;
loc_00283501:
    goto loc_00283126;
loc_0028350B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD435A7)))) & (64)) == 0) goto loc_00282FE0;
    result = KiCheckVpBackingLongSpinWaitHypercall(result, (uint32_t)((uint32_t)(local_r10)), *(uint64_t *)(v_rip + 0xBACBE4), *(uint64_t *)(*(uint64_t *)(v_rip + 0xBACBE4) + arg1 * 8));
    if ((uint8_t)(result) == 0) goto loc_00282FE0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)(local_r10)), *(uint64_t *)(v_rip + 0xBACBE4), *(uint64_t *)(*(uint64_t *)(v_rip + 0xBACBE4) + arg1 * 8));
    goto loc_00282FE2;
loc_00283533:
    result = MiCheckWriteInProgressFault(result, (uint32_t)((uint32_t)(local_r10)), *(uint64_t *)(v_rip + 0xBACBE4), *(uint64_t *)(*(uint64_t *)(v_rip + 0xBACBE4) + arg1 * 8));
    if (!sign_flag) goto loc_00282A77;
    goto loc_00282DFA;
loc_0028354F:
    if (condition_is_below) goto loc_00282F93;
    v_stack_p20 = *(uint64_t *)(result + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x411ULL), 0, local_rbx);
loc_0028357D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD43535)))) & (64)) == 0) goto loc_00283240;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (uint32_t)(0x411ULL), 0, local_rbx);
    if ((uint8_t)(result) == 0) goto loc_00283240;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x411ULL), 0, local_rbx);
    goto loc_00283242;
loc_002835A5:
    result = (*(uint64_t *)((uint32_t)((uint32_t)(local_r12)))) & (0);
    *(uint64_t *)((uint32_t)((uint32_t)(local_r12))) = result;
    goto loc_00283071;
loc_002835BD:
    v_stack_p28 = v_stack_pC0;
    v_stack_p20 = local_r12;
    result = MiHandleCollidedFault((uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x411ULL), 0, local_rbx);
    if (v_stack_pC0 <= 1) goto loc_00282DA5;
    if (sign_flag) goto loc_00282DA5;
    goto loc_00282ACB;
loc_002835EF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r12)) + 0x1F4)))) & (16)) == 0) goto loc_002831D0;
    goto loc_002831ED;
loc_00283602:
    result = MiSanitizeShadowPxe((uint32_t)((uint32_t)(local_r12)), v_stack_p60, 0, local_rbx);
    goto loc_00282C68;
loc_00283635:
    result = (*(uint64_t *)(result + 0x10)) & (-5);
    *(uint64_t *)(result + 0x10) = result;
    result = MiClearPageFileReservation(v_stack_p40, v_stack_p60, 0, v_stack_pC8);
    goto loc_002832C6;
loc_00283655:
    result = MiWritePteShadow(v_stack_pC8, v_stack_p60, 0, v_stack_pC8);
    goto loc_00282C83;
loc_00283665:
    *(uint64_t *)(result + 0x8) = v_stack_pC8;
    *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8)) = v_stack_pC8;
    goto loc_0028304D;
loc_00283676:
    Arg1 = (v_stack_pC8) & (-2);
    local_r14 = 0;
    if ((*(uint8_t *)(arg1)) != 5) goto loc_0028309C;
    goto loc_0028309C;
loc_0028368E:
    if ((*(uint8_t *)(arg1)) < 5) goto loc_00283715;
loc_002836A1:
loc_002836A9:
    *(uint64_t *)(v_stack_pC8) = v_stack_pD0;
    goto loc_00282DA5;
loc_002836B6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(272 + 0xB0)))) > 1) goto loc_002837C0;
loc_002836CA:
    result = MiFreeInPageSupportBlock(v_stack_p48, v_stack_p60, 0, v_stack_pC8);
    goto loc_00282D51;
loc_002836D7:
    result = MiCanPfnOriginalPteBeLost(result, v_stack_p60, 0, v_stack_pC8);
    if ((uint32_t)(result) == 0) goto loc_002832E0;
    Arg1 = (uint8_t)((*(uint8_t *)(result + 0x22)) >> (4));
    Arg1 = (uint8_t)(~(Arg1));
    result = ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (4)) != 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) == 0) goto loc_002832E0;
    result = (*(uint64_t *)(result + 0x10)) & (-5);
    *(uint64_t *)(result + 0x10) = result;
    goto loc_002832E0;
loc_00283715:
    if ((((uint8_t)(v_stack_pD0)) & (32)) != 0) goto loc_002836A1;
    result = (result) + (Arg1);
    if (v_stack_pC8 < result) goto loc_002836A9;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_pC8, v_stack_pD0, 128, v_stack_pC8);
    *(uint64_t *)(v_stack_pC8) = v_stack_pD0;
    goto loc_00282DA5;
loc_00283763:
loc_0028376A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (24));
    goto loc_00282DFA;
loc_00283782:
    result = MiHandleSpecialPurposeMemoryCachedFault(Arg1, *(uint64_t *)(arg1), v_stack_pC8, result);
    if (v_stack_pC8 == 0) goto loc_0028318A;
    result = MiUnlockProtoPoolPage(v_stack_pC8, 17, v_stack_pC8, result);
    goto loc_0028318A;
loc_002837C0:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent((uint32_t)(0xC0000709ULL) + 56, Arg2, Arg3, result);
    goto loc_002836CA;
loc_002837D3:
    result = MiLockAndDecrementShareCount(result, 2, Arg3, result);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `16` | `R` |
| `Arg1` | `+ 0x40` | `16` | `W` |
| `Arg1` | `+ 0x42` | `16` | `R` |
| `Arg1` | `+ 0x42` | `16` | `R/W` |
| `Arg1` | `+ 0x42` | `16` | `W` |
| `Arg1` | `+ 0x45` | `8` | `R` |
| `Arg1` | `+ 0x45` | `8` | `R/W` |
| `Arg1` | `+ 0x50` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00282940&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
