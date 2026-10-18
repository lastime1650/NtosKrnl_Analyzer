# MmProtectPool

- RVA: `0x002697AC`–`0x00269FDC` (길이 `2,096` bytes)
- VA: `0x00000001402697AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00065380`
- 디코드: `485`개 명령, `2,096/2,096` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002697D6` → [MiMakeProtectionMask](../32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x00269831` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x0026986B` → [MiFindLargeMapping](../45/MiFindLargeMapping_function_00457020.md) (function, `0x00457020`)
- `0x002698CE` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002698E6` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0026996D` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00269995` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x00269A1D` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x00269A63` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00269A68` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00269A78` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00269AAE` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x00269ACC` → [MiLockNonPagedPoolPte](../44/MiLockNonPagedPoolPte_function_004450EC.md) (function, `0x004450EC`)
- `0x00269AD7` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00269B7E` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00269C04` → [MiLockNonPagedPoolPte](../44/MiLockNonPagedPoolPte_function_004450EC.md) (function, `0x004450EC`)
- `0x00269C44` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00269C69` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x00269C7B` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x00269CB4` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x00269CDF` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x00269D0A` → [MI_TIGHTER_PERMISSIONS](../38/MI_TIGHTER_PERMISSIONS_function_00384C30.md) (function, `0x00384C30`)
- `0x00269D22` → [MI_TIGHTER_PERMISSIONS](../38/MI_TIGHTER_PERMISSIONS_function_00384C30.md) (function, `0x00384C30`)
- `0x00269D75` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00269DE1` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00269DFD` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00269E02` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00269E18` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00269E27` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00269E53` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x00269E5B` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00269E66` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x00269E7E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00269E8D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00269ECF` → [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) (function, `0x00362A0C`)
- `0x00269EE4` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00269EF3` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00269F00` → [MiCopyOnWriteCheckConditions](../2A/MiCopyOnWriteCheckConditions_function_002A750C.md) (function, `0x002A750C`)
- `0x00269F3E` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00269F43` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00269F61` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00269FC2` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00269FC7` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)

### Direct callers
- [ExProtectPoolEx](ExProtectPoolEx_function_002695D8.md) at `0x00269719`

### Static image references
- `0x00269836` → RVA `0x00E380C0` (`.data`; read)
- `0x0026987E` → RVA `0x00E38480` (`.data`; read)
- `0x002698AB` → RVA `0x00E30088` (`.data`; read)
- `0x002699D2` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00269CEB` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00269E70` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00269F73` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x00269BEA` → [sub_006D9212 + 0x16D](../6D/Unknown_function_006D9212.md) (`tail-transfer`)
  - `0x00269BFB` → [sub_006D9212 + 0x11](../6D/Unknown_function_006D9212.md) (`tail-transfer`)
  - `0x00269C0F` → [sub_006D9212 + 0x4C](../6D/Unknown_function_006D9212.md) (`tail-transfer`)
  - `0x00269D8B` → [sub_006D9212 + 0x420](../6D/Unknown_function_006D9212.md) (`tail-transfer`)
  - `0x00269F35` → [sub_006D9212](../6D/Unknown_function_006D9212.md) (`tail-transfer`)
  - `0x00269F53` → [sub_006D9212](../6D/Unknown_function_006D9212.md) (`tail-transfer`)
  - `0x00269F5B` → [sub_006D9212 + 0x14A](../6D/Unknown_function_006D9212.md) (`tail-transfer`)
  - `0x00269F6E` → [sub_006D9212 + 0x14A](../6D/Unknown_function_006D9212.md) (`tail-transfer`)
  - `0x00269FAF` → [sub_006D9212 + 0x39B](../6D/Unknown_function_006D9212.md) (`tail-transfer`)
  - `0x00269FBA` → [sub_006D9212 + 0x361](../6D/Unknown_function_006D9212.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002697AC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002697B1  55                              push rbp
002697B2  56                              push rsi
002697B3  57                              push rdi
002697B4  41 54                           push r12
002697B6  41 55                           push r13
002697B8  41 56                           push r14
002697BA  41 57                           push r15
002697BC  48 81 EC 90 00 00 00            sub rsp, 0x90
002697C3  4C 8B CA                        mov r9, rdx
002697C6  48 8B D9                        mov rbx, rcx
002697C9  41 F6 C0 10                     test r8b, 0x10
002697CD  0F 85 37 07 00 00               jne 0x140269f0a
002697D3  41 8B C8                        mov ecx, r8d
002697D6  E8 A5 FC 0B 00                  call 0x140329480
002697DB  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002697DF  44 8B F8                        mov r15d, eax
002697E2  83 F8 08                        cmp eax, 8
002697E5  0F 83 39 07 00 00               jae 0x140269f24
002697EB  8B C8                           mov ecx, eax
002697ED  83 E1 05                        and ecx, 5
002697F0  80 F9 05                        cmp cl, 5
002697F3  74 52                           je 0x140269847
002697F5  83 F8 FF                        cmp eax, -1
002697F8  74 4D                           je 0x140269847
002697FA  48 8B F3                        mov rsi, rbx
002697FD  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
00269807  48 C1 EE 09                     shr rsi, 9
0026980B  4D 8D 71 FF                     lea r14, [r9 - 1]
0026980F  33 ED                           xor ebp, ebp
00269811  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0026981B  48 23 F0                        and rsi, rax
0026981E  89 AC 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ebp
00269825  4C 03 F3                        add r14, rbx
00269828  49 8B C4                        mov rax, r12
0026982B  48 8B CB                        mov rcx, rbx
0026982E  48 03 F0                        add rsi, rax
00269831  E8 4A 54 02 00                  call 0x14028ec80
00269836  4C 8D 2D 83 E8 BC 00            lea r13, [rip + 0xbce883]
0026983D  83 F8 05                        cmp eax, 5
00269840  74 43                           je 0x140269885
00269842  83 F8 04                        cmp eax, 4
00269845  74 1E                           je 0x140269865
00269847  33 C0                           xor eax, eax
00269849  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00269851  48 81 C4 90 00 00 00            add rsp, 0x90
00269858  41 5F                           pop r15
0026985A  41 5E                           pop r14
0026985C  41 5D                           pop r13
0026985E  41 5C                           pop r12
00269860  5F                              pop rdi
00269861  5E                              pop rsi
00269862  5D                              pop rbp
00269863  C3                              ret
00269864  CC                              int3
00269865  49 8B D6                        mov rdx, r14
00269868  48 8B CB                        mov rcx, rbx
0026986B  E8 B0 D7 1E 00                  call 0x140457020
00269870  85 C0                           test eax, eax
00269872  75 D3                           jne 0x140269847
00269874  8D 68 01                        lea ebp, [rax + 1]
00269877  89 AC 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ebp
0026987E  4C 8D 2D FB EB BC 00            lea r13, [rip + 0xbcebfb]
00269885  33 FF                           xor edi, edi
00269887  49 C1 EE 09                     shr r14, 9
0026988B  48 BB F8 FF FF FF 7F 00 00 00   movabs rbx, 0x7ffffffff8
00269895  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
0026989A  4C 23 F3                        and r14, rbx
0026989D  49 8B C4                        mov rax, r12
002698A0  41 0F B7 8D AE 00 00 00         movzx ecx, word ptr [r13 + 0xae]
002698A8  4C 03 F0                        add r14, rax
002698AB  48 8B 05 D6 67 BC 00            mov rax, qword ptr [rip + 0xbc67d6]
002698B2  45 33 E4                        xor r12d, r12d
002698B5  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
002698BA  45 33 F6                        xor r14d, r14d
002698BD  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
002698C2  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
002698C6  49 8B CD                        mov rcx, r13
002698C9  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002698CE  E8 1D 33 01 00                  call 0x14027cbf0
002698D3  88 84 24 E0 00 00 00            mov byte ptr [rsp + 0xe0], al
002698DA  48 3B 74 24 50                  cmp rsi, qword ptr [rsp + 0x50]
002698DF  76 14                           jbe 0x1402698f5
002698E1  8A D0                           mov dl, al
002698E3  49 8B CD                        mov rcx, r13
002698E6  E8 A5 3D 01 00                  call 0x14027d690
002698EB  B8 01 00 00 00                  mov eax, 1
002698F0  E9 54 FF FF FF                  jmp 0x140269849
002698F5  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
002698FF  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
00269909  48 85 FF                        test rdi, rdi
0026990C  0F 84 77 01 00 00               je 0x140269a89
00269912  48 F7 C6 FF 0F 00 00            test rsi, 0xfff
00269919  0F 84 13 06 00 00               je 0x140269f32
0026991F  48 8B 1E                        mov rbx, qword ptr [rsi]
00269922  41 8B 85 B8 00 00 00            mov eax, dword ptr [r13 + 0xb8]
00269929  24 0F                           and al, 0xf
0026992B  41 83 FF 18                     cmp r15d, 0x18
0026992F  0F 84 AD 02 00 00               je 0x140269be2
00269935  3C 07                           cmp al, 7
00269937  0F 85 08 02 00 00               jne 0x140269b45
0026993D  41 0F BA EF 1F                  bts r15d, 0x1f
00269942  4C 8B F3                        mov r14, rbx
00269945  48 8B D3                        mov rdx, rbx
00269948  41 83 E6 01                     and r14d, 1
0026994C  0F 84 21 06 00 00               je 0x140269f73
00269952  48 C1 EA 0C                     shr rdx, 0xc
00269956  49 23 D0                        and rdx, r8
00269959  48 8D 2C 52                     lea rbp, [rdx + rdx*2]
0026995D  48 C1 E5 04                     shl rbp, 4
00269961  49 8B C1                        mov rax, r9
00269964  45 8B C7                        mov r8d, r15d
00269967  48 8B CE                        mov rcx, rsi
0026996A  48 03 E8                        add rbp, rax
0026996D  E8 1E BC 05 00                  call 0x1402c5590
00269972  48 8B F8                        mov rdi, rax
00269975  4D 85 F6                        test r14, r14
00269978  0F 84 1C 06 00 00               je 0x140269f9a
0026997E  44 8B B4 24 E8 00 00 00         mov r14d, dword ptr [rsp + 0xe8]
00269986  48 8B CE                        mov rcx, rsi
00269989  45 85 F6                        test r14d, r14d
0026998C  0F 85 3A 01 00 00               jne 0x140269acc
00269992  48 8B D0                        mov rdx, rax
00269995  E8 76 7E 01 00                  call 0x140281810
0026999A  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
0026999E  44 8B 7C 24 38                  mov r15d, dword ptr [rsp + 0x38]
002699A3  41 8B D7                        mov edx, r15d
002699A6  48 C1 E2 05                     shl rdx, 5
002699AA  48 8B CA                        mov rcx, rdx
002699AD  48 33 C8                        xor rcx, rax
002699B0  48 81 E1 1F FC FF FF            and rcx, 0xfffffffffffffc1f
002699B7  48 33 CA                        xor rcx, rdx
002699BA  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
002699BE  45 85 F6                        test r14d, r14d
002699C1  74 0F                           je 0x1402699d2
002699C3  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002699CD  F0 48 21 45 18                  lock and qword ptr [rbp + 0x18], rax
002699D2  48 F7 05 AB D0 D5 00 00 01 00 00  test qword ptr [rip + 0xd5d0ab], 0x100
002699DD  0F 85 39 03 00 00               jne 0x140269d1c
002699E3  48 8B DE                        mov rbx, rsi
002699E6  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002699F0  48 C1 E3 19                     shl rbx, 0x19
002699F4  48 8B C0                        mov rax, rax
002699F7  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
002699FC  48 C1 E0 19                     shl rax, 0x19
00269A00  48 2B D8                        sub rbx, rax
00269A03  48 C1 FB 10                     sar rbx, 0x10
00269A07  4D 85 E4                        test r12, r12
00269A0A  0F 84 48 05 00 00               je 0x140269f58
00269A10  45 33 C9                        xor r9d, r9d
00269A13  48 8B D3                        mov rdx, rbx
00269A16  49 8B CC                        mov rcx, r12
00269A19  45 8D 41 01                     lea r8d, [r9 + 1]
00269A1D  E8 4E 9C 02 00                  call 0x140293670
00269A22  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00269A27  48 83 C6 08                     add rsi, 8
00269A2B  48 BB F8 FF FF FF 7F 00 00 00   movabs rbx, 0x7ffffffff8
00269A35  8B AC 24 E8 00 00 00            mov ebp, dword ptr [rsp + 0xe8]
00269A3C  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
00269A46  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
00269A50  48 3B 74 24 50                  cmp rsi, qword ptr [rsp + 0x50]
00269A55  0F 86 AE FE FF FF               jbe 0x140269909
00269A5B  4D 85 E4                        test r12, r12
00269A5E  74 0D                           je 0x140269a6d
00269A60  49 8B CC                        mov rcx, r12
00269A63  E8 58 85 0A 00                  call 0x140311fc0
00269A68  E8 03 A2 0A 00                  call 0x140313c70
00269A6D  48 8B D7                        mov rdx, rdi
00269A70  48 85 D2                        test rdx, rdx
00269A73  74 08                           je 0x140269a7d
00269A75  49 8B CD                        mov rcx, r13
00269A78  E8 43 D4 FA FF                  call 0x140216ec0
00269A7D  8A 84 24 E0 00 00 00            mov al, byte ptr [rsp + 0xe0]
00269A84  E9 58 FE FF FF                  jmp 0x1402698e1
00269A89  48 8B FE                        mov rdi, rsi
00269A8C  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00269A96  48 C1 EF 09                     shr rdi, 9
00269A9A  48 23 FB                        and rdi, rbx
00269A9D  48 8B C0                        mov rax, rax
00269AA0  48 03 F8                        add rdi, rax
00269AA3  49 8B CD                        mov rcx, r13
00269AA6  48 8B D7                        mov rdx, rdi
00269AA9  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00269AAE  E8 DD 4D FD FF                  call 0x14023e890
00269AB3  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
00269ABD  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
00269AC7  E9 53 FE FF FF                  jmp 0x14026991f
00269ACC  E8 1B B6 1D 00                  call 0x1404450ec
00269AD1  48 8B CE                        mov rcx, rsi
00269AD4  48 8B E8                        mov rbp, rax
00269AD7  E8 C4 8D 01 00                  call 0x1402828a0
00269ADC  48 3B C3                        cmp rax, rbx
00269ADF  75 39                           jne 0x140269b1a
00269AE1  48 0F BA E3 09                  bt rbx, 9
00269AE6  73 05                           jae 0x140269aed
00269AE8  48 0F BA EF 09                  bts rdi, 9
00269AED  48 F7 05 90 CF D5 00 00 00 00 02  test qword ptr [rip + 0xd5cf90], 0x2000000
00269AF8  74 03                           je 0x140269afd
00269AFA  0F AE E8                        lfence
00269AFD  48 0F BA 25 82 CF D5 00 24      bt qword ptr [rip + 0xd5cf82], 0x24
00269B06  0F 82 2D 02 00 00               jb 0x140269d39
00269B0C  48 8B C3                        mov rax, rbx
00269B0F  F0 48 0F B1 3E                  lock cmpxchg qword ptr [rsi], rdi
00269B14  0F 84 80 FE FF FF               je 0x14026999a
00269B1A  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00269B24  F0 48 21 4D 18                  lock and qword ptr [rbp + 0x18], rcx
00269B29  48 8B D8                        mov rbx, rax
00269B2C  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
00269B36  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
00269B40  E9 FD FD FF FF                  jmp 0x140269942
00269B45  F6 C3 01                        test bl, 1
00269B48  0F 84 31 02 00 00               je 0x140269d7f
00269B4E  48 8B D3                        mov rdx, rbx
00269B51  48 C1 EA 0C                     shr rdx, 0xc
00269B55  49 23 D0                        and rdx, r8
00269B58  48 8D 2C 52                     lea rbp, [rdx + rdx*2]
00269B5C  48 C1 E5 04                     shl rbp, 4
00269B60  49 8B C1                        mov rax, r9
00269B63  48 03 E8                        add rbp, rax
00269B66  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
00269B6A  48 85 C0                        test rax, rax
00269B6D  0F 88 24 03 00 00               js 0x140269e97
00269B73  45 8B C7                        mov r8d, r15d
00269B76  48 8B CE                        mov rcx, rsi
00269B79  41 0F BA E8 1F                  bts r8d, 0x1f
00269B7E  E8 0D BA 05 00                  call 0x1402c5590
00269B83  48 8B F8                        mov rdi, rax
00269B86  48 B9 00 00 00 00 00 00 00 7F   movabs rcx, 0x7f00000000000000
00269B90  48 B8 FF FF FF FF FF FF FF 80   movabs rax, 0x80ffffffffffffff
00269B9A  48 23 F8                        and rdi, rax
00269B9D  48 8B C3                        mov rax, rbx
00269BA0  48 23 C1                        and rax, rcx
00269BA3  48 0B F8                        or rdi, rax
00269BA6  48 F7 05 D7 CE D5 00 00 00 00 02  test qword ptr [rip + 0xd5ced7], 0x2000000
00269BB1  74 03                           je 0x140269bb6
00269BB3  0F AE E8                        lfence
00269BB6  48 0F BA 25 C9 CE D5 00 24      bt qword ptr [rip + 0xd5cec9], 0x24
00269BBF  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
00269BC9  0F 82 E0 01 00 00               jb 0x140269daf
00269BCF  48 8B C3                        mov rax, rbx
00269BD2  F0 48 0F B1 3E                  lock cmpxchg qword ptr [rsi], rdi
00269BD7  74 3B                           je 0x140269c14
00269BD9  48 83 EE 08                     sub rsi, 8
00269BDD  E9 40 FE FF FF                  jmp 0x140269a22
00269BE2  48 8B CB                        mov rcx, rbx
00269BE5  83 E1 01                        and ecx, 1
00269BE8  3C 07                           cmp al, 7
00269BEA  0F 85 8F F7 46 00               jne 0x1406d937f
00269BF0  48 85 C9                        test rcx, rcx
00269BF3  0F 84 29 FE FF FF               je 0x140269a22
00269BF9  85 ED                           test ebp, ebp
00269BFB  0F 84 22 F6 46 00               je 0x1406d9223
00269C01  48 8B CE                        mov rcx, rsi
00269C04  E8 E3 B4 1D 00                  call 0x1404450ec
00269C09  48 8B 1E                        mov rbx, qword ptr [rsi]
00269C0C  48 8B E8                        mov rbp, rax
00269C0F  E9 4A F6 46 00                  jmp 0x1406d925e
00269C14  48 F7 05 69 CE D5 00 00 01 00 00  test qword ptr [rip + 0xd5ce69], 0x100
00269C1F  0F 85 DF 00 00 00               jne 0x140269d04
00269C25  48 8B FE                        mov rdi, rsi
00269C28  48 C1 E7 19                     shl rdi, 0x19
00269C2C  49 8B C0                        mov rax, r8
00269C2F  48 C1 E0 19                     shl rax, 0x19
00269C33  48 2B F8                        sub rdi, rax
00269C36  48 C1 FF 10                     sar rdi, 0x10
00269C3A  4D 85 E4                        test r12, r12
00269C3D  75 2F                           jne 0x140269c6e
00269C3F  4D 85 F6                        test r14, r14
00269C42  75 0D                           jne 0x140269c51
00269C44  E8 47 90 FD FF                  call 0x140242c90
00269C49  4C 8B F0                        mov r14, rax
00269C4C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00269C51  45 8B 46 0C                     mov r8d, dword ptr [r14 + 0xc]
00269C55  45 33 C9                        xor r9d, r9d
00269C58  49 8B D5                        mov rdx, r13
00269C5B  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
00269C63  49 8B CE                        mov rcx, r14
00269C66  4D 8B E6                        mov r12, r14
00269C69  E8 92 B2 02 00                  call 0x140294f00
00269C6E  45 33 C9                        xor r9d, r9d
00269C71  48 8B D7                        mov rdx, rdi
00269C74  49 8B CC                        mov rcx, r12
00269C77  45 8D 41 01                     lea r8d, [r9 + 1]
00269C7B  E8 F0 99 02 00                  call 0x140293670
00269C80  33 FF                           xor edi, edi
00269C82  F0 48 0F BA 6D 18 3F            lock bts qword ptr [rbp + 0x18], 0x3f
00269C89  72 5E                           jb 0x140269ce9
00269C8B  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
00269C8F  41 8B D7                        mov edx, r15d
00269C92  48 C1 E2 05                     shl rdx, 5
00269C96  48 8B CA                        mov rcx, rdx
00269C99  48 33 C8                        xor rcx, rax
00269C9C  33 C0                           xor eax, eax
00269C9E  48 81 E1 1F FC FF FF            and rcx, 0xfffffffffffffc1f
00269CA5  48 33 CA                        xor rcx, rdx
00269CA8  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
00269CAC  F6 C3 42                        test bl, 0x42
00269CAF  74 08                           je 0x140269cb9
00269CB1  48 8B CD                        mov rcx, rbp
00269CB4  E8 17 71 10 00                  call 0x140370dd0
00269CB9  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00269CC3  F0 48 21 4D 18                  lock and qword ptr [rbp + 0x18], rcx
00269CC8  48 85 C0                        test rax, rax
00269CCB  0F 84 51 FD FF FF               je 0x140269a22
00269CD1  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00269CD6  41 B8 01 00 00 00               mov r8d, 1
00269CDC  48 8B D0                        mov rdx, rax
00269CDF  E8 EC A2 01 00                  call 0x140283fd0
00269CE4  E9 39 FD FF FF                  jmp 0x140269a22
00269CE9  FF C7                           inc edi
00269CEB  85 3D BB B5 D5 00               test dword ptr [rip + 0xd5b5bb], edi
00269CF1  0F 84 79 01 00 00               je 0x140269e70
00269CF7  F3 90                           pause
00269CF9  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00269CFD  48 85 C0                        test rax, rax
00269D00  79 80                           jns 0x140269c82
00269D02  EB E5                           jmp 0x140269ce9
00269D04  48 8B D7                        mov rdx, rdi
00269D07  48 8B CB                        mov rcx, rbx
00269D0A  E8 21 AF 11 00                  call 0x140384c30
00269D0F  85 C0                           test eax, eax
00269D11  0F 84 69 FF FF FF               je 0x140269c80
00269D17  E9 09 FF FF FF                  jmp 0x140269c25
00269D1C  48 8B D7                        mov rdx, rdi
00269D1F  48 8B CB                        mov rcx, rbx
00269D22  E8 09 AF 11 00                  call 0x140384c30
00269D27  85 C0                           test eax, eax
00269D29  0F 85 B4 FC FF FF               jne 0x1402699e3
00269D2F  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
00269D34  E9 E9 FC FF FF                  jmp 0x140269a22
00269D39  40 8A C7                        mov al, dil
00269D3C  24 21                           and al, 0x21
00269D3E  3C 01                           cmp al, 1
00269D40  0F 85 C6 FD FF FF               jne 0x140269b0c
00269D46  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00269D50  48 8B C0                        mov rax, rax
00269D53  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00269D5D  48 03 C1                        add rax, rcx
00269D60  48 3B F0                        cmp rsi, rax
00269D63  0F 82 A3 FD FF FF               jb 0x140269b0c
00269D69  41 B8 80 00 00 00               mov r8d, 0x80
00269D6F  48 8B D7                        mov rdx, rdi
00269D72  48 8B CE                        mov rcx, rsi
00269D75  E8 06 90 02 00                  call 0x140292d80
00269D7A  E9 8D FD FF FF                  jmp 0x140269b0c
00269D7F  48 0F BA E3 0A                  bt rbx, 0xa
00269D84  72 6F                           jb 0x140269df5
00269D86  48 0F BA E3 0B                  bt rbx, 0xb
00269D8B  0F 82 A1 F8 46 00               jb 0x1406d9632
00269D91  41 8B CF                        mov ecx, r15d
00269D94  48 C1 E1 05                     shl rcx, 5
00269D98  48 8B C1                        mov rax, rcx
00269D9B  48 33 C3                        xor rax, rbx
00269D9E  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
00269DA4  48 33 C1                        xor rax, rcx
00269DA7  48 89 06                        mov qword ptr [rsi], rax
00269DAA  E9 73 FC FF FF                  jmp 0x140269a22
00269DAF  40 8A C7                        mov al, dil
00269DB2  24 21                           and al, 0x21
00269DB4  3C 01                           cmp al, 1
00269DB6  0F 85 13 FE FF FF               jne 0x140269bcf
00269DBC  49 8B C0                        mov rax, r8
00269DBF  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00269DC9  48 03 C1                        add rax, rcx
00269DCC  48 3B F0                        cmp rsi, rax
00269DCF  0F 82 FA FD FF FF               jb 0x140269bcf
00269DD5  41 B8 80 00 00 00               mov r8d, 0x80
00269DDB  48 8B D7                        mov rdx, rdi
00269DDE  48 8B CE                        mov rcx, rsi
00269DE1  E8 9A 8F 02 00                  call 0x140292d80
00269DE6  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
00269DF0  E9 DA FD FF FF                  jmp 0x140269bcf
00269DF5  4D 85 E4                        test r12, r12
00269DF8  74 18                           je 0x140269e12
00269DFA  49 8B CC                        mov rcx, r12
00269DFD  E8 BE 81 0A 00                  call 0x140311fc0
00269E02  E8 69 9E 0A 00                  call 0x140313c70
00269E07  45 33 E4                        xor r12d, r12d
00269E0A  45 33 F6                        xor r14d, r14d
00269E0D  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00269E12  48 8B D7                        mov rdx, rdi
00269E15  49 8B CD                        mov rcx, r13
00269E18  E8 A3 D0 FA FF                  call 0x140216ec0
00269E1D  8A 94 24 E0 00 00 00            mov dl, byte ptr [rsp + 0xe0]
00269E24  49 8B CD                        mov rcx, r13
00269E27  E8 64 38 01 00                  call 0x14027d690
00269E2C  48 8B D6                        mov rdx, rsi
00269E2F  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00269E39  48 C1 E2 19                     shl rdx, 0x19
00269E3D  48 8B C0                        mov rax, rax
00269E40  48 C1 E0 19                     shl rax, 0x19
00269E44  45 33 C9                        xor r9d, r9d
00269E47  48 2B D0                        sub rdx, rax
00269E4A  45 33 C0                        xor r8d, r8d
00269E4D  48 C1 FA 10                     sar rdx, 0x10
00269E51  33 C9                           xor ecx, ecx
00269E53  E8 28 50 01 00                  call 0x14027ee80
00269E58  49 8B CD                        mov rcx, r13
00269E5B  E8 90 2D 01 00                  call 0x14027cbf0
00269E60  48 8B D7                        mov rdx, rdi
00269E63  49 8B CD                        mov rcx, r13
00269E66  E8 25 4A FD FF                  call 0x14023e890
00269E6B  E9 69 FD FF FF                  jmp 0x140269bd9
00269E70  8B 05 42 CC D5 00               mov eax, dword ptr [rip + 0xd5cc42]
00269E76  A8 40                           test al, 0x40
00269E78  0F 84 79 FE FF FF               je 0x140269cf7
00269E7E  E8 0D 56 0A 00                  call 0x14030f490
00269E83  84 C0                           test al, al
00269E85  0F 84 6C FE FF FF               je 0x140269cf7
00269E8B  8B CF                           mov ecx, edi
00269E8D  E8 CE 55 0A 00                  call 0x14030f460
00269E92  E9 62 FE FF FF                  jmp 0x140269cf9
00269E97  4D 85 E4                        test r12, r12
00269E9A  0F 85 1F 01 00 00               jne 0x140269fbf
00269EA0  48 8B CE                        mov rcx, rsi
00269EA3  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00269EAD  48 C1 E1 19                     shl rcx, 0x19
00269EB1  48 8B C0                        mov rax, rax
00269EB4  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00269EBA  45 33 C9                        xor r9d, r9d
00269EBD  48 C1 E0 19                     shl rax, 0x19
00269EC1  49 83 C8 FF                     or r8, 0xffffffffffffffff
00269EC5  48 2B C8                        sub rcx, rax
00269EC8  48 8B D6                        mov rdx, rsi
00269ECB  48 C1 F9 10                     sar rcx, 0x10
00269ECF  E8 38 8B 0F 00                  call 0x140362a0c
00269ED4  8B D8                           mov ebx, eax
00269ED6  85 C0                           test eax, eax
00269ED8  0F 89 FB FC FF FF               jns 0x140269bd9
00269EDE  48 8B D7                        mov rdx, rdi
00269EE1  49 8B CD                        mov rcx, r13
00269EE4  E8 D7 CF FA FF                  call 0x140216ec0
00269EE9  8A 94 24 E0 00 00 00            mov dl, byte ptr [rsp + 0xe0]
00269EF0  49 8B CD                        mov rcx, r13
00269EF3  E8 98 37 01 00                  call 0x14027d690
00269EF8  45 33 C0                        xor r8d, r8d
00269EFB  8B D3                           mov edx, ebx
00269EFD  49 8B CD                        mov rcx, r13
00269F00  E8 07 D6 03 00                  call 0x1402a750c
00269F05  E9 4E FF FF FF                  jmp 0x140269e58
00269F0A  48 F7 05 73 CB D5 00 00 80 00 00  test qword ptr [rip + 0xd5cb73], 0x8000
00269F15  0F 84 B8 F8 FF FF               je 0x1402697d3
00269F1B  41 83 E0 EF                     and r8d, 0xffffffef
00269F1F  E9 AF F8 FF FF                  jmp 0x1402697d3
00269F24  83 F8 18                        cmp eax, 0x18
00269F27  0F 85 1A F9 FF FF               jne 0x140269847
00269F2D  E9 B9 F8 FF FF                  jmp 0x1402697eb
00269F32  4D 85 E4                        test r12, r12
00269F35  0F 84 D7 F2 46 00               je 0x1406d9212
00269F3B  49 8B CC                        mov rcx, r12
00269F3E  E8 7D 80 0A 00                  call 0x140311fc0
00269F43  E8 28 9D 0A 00                  call 0x140313c70
00269F48  45 33 E4                        xor r12d, r12d
00269F4B  45 33 F6                        xor r14d, r14d
00269F4E  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00269F53  E9 BA F2 46 00                  jmp 0x1406d9212
00269F58  4D 85 F6                        test r14, r14
00269F5B  0F 85 FB F3 46 00               jne 0x1406d935c
00269F61  E8 2A 8D FD FF                  call 0x140242c90
00269F66  4C 8B F0                        mov r14, rax
00269F69  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00269F6E  E9 E9 F3 46 00                  jmp 0x1406d935c
00269F73  48 8B 05 06 3D BC 00            mov rax, qword ptr [rip + 0xbc3d06]
00269F7A  48 85 C0                        test rax, rax
00269F7D  0F 84 CF F9 FF FF               je 0x140269952
00269F83  F6 C3 10                        test bl, 0x10
00269F86  0F 85 C6 F9 FF FF               jne 0x140269952
00269F8C  48 8B D0                        mov rdx, rax
00269F8F  48 F7 D2                        not rdx
00269F92  48 23 D3                        and rdx, rbx
00269F95  E9 B8 F9 FF FF                  jmp 0x140269952
00269F9A  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00269F9E  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
00269FA8  48 23 C1                        and rax, rcx
00269FAB  48 83 F8 01                     cmp rax, 1
00269FAF  0F 84 F8 F5 46 00               je 0x1406d95ad
00269FB5  83 64 24 40 00                  and dword ptr [rsp + 0x40], 0
00269FBA  E9 B4 F5 46 00                  jmp 0x1406d9573
00269FBF  49 8B CC                        mov rcx, r12
00269FC2  E8 F9 7F 0A 00                  call 0x140311fc0
00269FC7  E8 A4 9C 0A 00                  call 0x140313c70
00269FCC  45 33 E4                        xor r12d, r12d
00269FCF  45 33 F6                        xor r14d, r14d
00269FD2  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00269FD7  E9 C4 FE FF FF                  jmp 0x140269ea0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmProtectPool(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m90;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p8;
    unsigned __int8 v_stack_pE0;
    unsigned int v_stack_pE8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (144);
    if ((((unsigned __int8)(a3)) & (16)) != 0) goto loc_00269F0A;
loc_002697D3:
    result = MiMakeProtectionMask((unsigned int)(a3), a2, a3, a2);
    v_stack_m90 = (unsigned int)(result);
    if (((unsigned int)(result)) >= 8) goto loc_00269F24;
loc_002697EB:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (5));
    if (((unsigned __int8)(a1)) == 5) goto loc_00269847;
    if (((unsigned int)(result)) == -1) goto loc_00269847;
    v_rsi = (a1) >> (9);
    v_rbp = 0;
    v_rsi = (v_rsi) & (result);
    v_stack_p20 = 0;
    v_r14 = (a2 - 1) + (a1);
    v_rsi = (v_rsi) + (v_r12);
    result = MiGetSystemRegionType(a1, a2, a3, a2);
    if (((unsigned int)(result)) == 5) goto loc_00269885;
    if (((unsigned int)(result)) == 4) goto loc_00269865;
loc_00269847:
    result = 0;
loc_00269849:
    v_rsp = (v_rsp) + (144);
    return result;
loc_00269865:
    result = MiFindLargeMapping(v_stack_p8, v_r14, a3, a2);
    if ((unsigned int)(result) != 0) goto loc_00269847;
    v_stack_pE8 = (unsigned int)(result + 1);
loc_00269885:
    v_rdi = 0;
    v_r14 = (v_r14) >> (9);
    v_stack_p48 = 0;
    v_r14 = (v_r14) & (v_stack_p8);
    v_r14 = (v_r14) + (v_r12);
    v_r12 = 0;
    v_stack_p50 = v_r14;
    v_r14 = 0;
    v_stack_p30 = 0;
    v_stack_p58 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12347350) + *(unsigned __int16 *)(v_rip + 12381179 + 174) * 8);
    result = MiLockWorkingSetShared(v_rip + 12381179, v_r14, a3, a2);
    v_stack_pE0 = (unsigned __int8)(result);
    if (v_rsi <= v_stack_p50) goto loc_002698F5;
loc_002698E1:
    result = MiUnlockWorkingSetShared(v_rip + 12381179, (unsigned __int8)(result), a3, a2);
    goto loc_00269849;
loc_002698F5:
loc_00269909:
    if (0 == 0) goto loc_00269A89;
    if (((v_rsi) & (0xFFFULL)) == 0) goto loc_00269F32;
loc_0026991F:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rip + 12381179 + 184))) & (15));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 24) goto loc_00269BE2;
    if (((unsigned __int8)(result)) != 7) goto loc_00269B45;
loc_00269942:
    v_r14 = (unsigned int)((*(unsigned __int64 *)(v_rsi)) & (1));
    if (condition_is_equal) goto loc_00269F73;
loc_00269952:
    a2 = (*(unsigned __int64 *)(v_rsi)) >> (12);
    a2 = (a2) & (a3);
    v_rbp = (a2 + a2 * 2) << (4);
    v_rbp = (v_rbp) + (a2);
    result = MiMakeValidPte(v_rsi, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2);
    if (v_r14 == 0) goto loc_00269F9A;
    if ((unsigned int)((unsigned int)(v_stack_pE8)) != 0) goto loc_00269ACC;
    result = MiWriteValidPteNewProtection(v_rsi, result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2);
loc_0026999A:
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p38)))) << (5);
    a1 = (a2) ^ (*(unsigned __int64 *)(v_rbp + 16));
    a1 = (a1) & (-993);
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(v_rbp + 16) = a1;
    if ((unsigned int)((unsigned int)(v_stack_pE8)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 14012587)) & (256)) != 0) goto loc_00269D1C;
loc_002699E3:
    v_rbx = (v_rsi) << (25);
    result = (*(unsigned __int64 *)(v_rbp + 16)) << (25);
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) >> (16);
    if (0 == 0) goto loc_00269F58;
    a4 = 0;
    result = MiInsertTbFlushEntry(0, v_rbx, a4 + 1, a4);
loc_00269A22:
    v_rsi = (v_rsi) + (8);
    if (v_rsi <= v_stack_p50) goto loc_00269909;
    if (0 != 0) {
        a1 = 0;
        result = MiFlushTbList(a1, v_rbx, a4 + 1, a4);
        result = MiReleaseProcessorFlushList(a1, v_rbx, a4 + 1, a4);
    }
    if (v_stack_p48 != 0) {
        a1 = v_rip + 12381179;
        result = MiUnlockPageTable(a1, v_stack_p48, a4 + 1, a4);
    }
    goto loc_002698E1;
loc_00269A89:
    v_rdi = (v_rsi) >> (9);
    v_rdi = (v_rdi) & (v_rbx);
    v_rdi = (v_rdi) + (v_stack_pE0);
    v_stack_p48 = v_rdi;
    result = MiLockNestedPageTable(v_rip + 12381179, v_rdi, a4 + 1, a4);
    goto loc_0026991F;
loc_00269ACC:
    result = MiLockNonPagedPoolPte(v_rip + 12381179, v_rdi, a4 + 1, a4);
    result = MI_READ_PTE_LOCK_FREE(v_rsi, v_rdi, a4 + 1, a4);
    if (result != v_rbx) goto loc_00269B1A;
    if (result < v_rbx) {
    }
    if (((*(unsigned __int64 *)(v_rip + 14012304)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00269D39;
loc_00269B0C:
    if (((*(unsigned __int64 *)(v_rip + 14012304)) & (0x2000000ULL)) == 0) goto loc_0026999A;
loc_00269B1A:
    goto loc_00269942;
loc_00269B45:
    if ((((unsigned __int8)(v_rbx)) & (1)) == 0) goto loc_00269D7F;
    a2 = (v_rbx) >> (12);
    a2 = (a2) & (a4 + 1);
    v_rbp = (a2 + a2 * 2) << (4);
    v_rbp = (v_rbp) + (0);
    if (sign_flag) goto loc_00269E97;
    result = MiMakeValidPte(v_rsi, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_p38))), a4);
    v_rdi = (result) & (result);
    result = (v_rbx) & (v_rsi);
    v_rdi = (v_rdi) | (result);
    if (((*(unsigned __int64 *)(v_rip + 14012119)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00269DAF;
loc_00269BCF:
    if (((*(unsigned __int64 *)(v_rip + 14012119)) & (0x2000000ULL)) == 0) goto loc_00269C14;
loc_00269BD9:
    v_rsi = (v_rsi) - (8);
    goto loc_00269A22;
loc_00269BE2:
    a1 = (unsigned int)((v_rbx) & (1));
    if (a1 == 0) goto loc_00269A22;
    result = MiLockNonPagedPoolPte(v_rsi, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_p38))), a4);
loc_00269C14:
    if (((*(unsigned __int64 *)(v_rip + 14012009)) & (256)) != 0) goto loc_00269D04;
loc_00269C25:
    v_rdi = (v_rsi) << (25);
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p38)))) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) >> (16);
    if (0 != 0) goto loc_00269C6E;
    v_r14 = v_stack_p30;
    if (v_stack_p30 == 0) {
        result = MiGetProcessorFlushList(v_rsi, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_p38))), a4);
        v_r14 = result;
        v_stack_p30 = result;
    }
    a4 = 0;
    v_stack_p20 = 32;
    result = MiInitializeTbFlushList(v_r14, v_rip + 12381179, (unsigned int)(*(unsigned int *)(v_r14 + 12)), a4);
loc_00269C6E:
    a4 = 0;
    result = MiInsertTbFlushEntry(v_r14, v_rdi, a4 + 1, a4);
loc_00269C80:
    v_rdi = 0;
loc_00269C82:
    if (condition_is_below) goto loc_00269CE9;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p38)))) << (5);
    a1 = (a2) ^ (*(unsigned __int64 *)(result + 16));
    result = 0;
    a1 = (a1) & (-993);
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(result + 16) = a1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsi))) & (66)) != 0) {
        a1 = 0;
        result = MiCaptureDirtyBitToPfn(a1, a2, a4 + 1, a4);
    }
    if (result == 0) goto loc_00269A22;
    result = MiReleasePageFileInfo(v_stack_p58, result, 1, a4);
    goto loc_00269A22;
loc_00269CE9:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 14005691)) & ((unsigned int)(v_rdi))) == 0) goto loc_00269E70;
loc_00269CF7:
loc_00269CF9:
    if (!sign_flag) goto loc_00269C82;
    goto loc_00269CE9;
loc_00269D04:
    result = MI_TIGHTER_PERMISSIONS(*(unsigned __int64 *)(v_rsi), v_rdi, 1, a4);
    if ((unsigned int)(result) == 0) goto loc_00269C80;
    goto loc_00269C25;
loc_00269D1C:
    result = MI_TIGHTER_PERMISSIONS(*(unsigned __int64 *)(v_rsi), v_rdi, 1, a4);
    if ((unsigned int)(result) != 0) goto loc_002699E3;
    goto loc_00269A22;
loc_00269D39:
    result = (unsigned __int8)(((unsigned __int8)(v_rdi)) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_00269B0C;
    result = (result) + (*(unsigned __int64 *)(v_rsi));
    if (v_rsi < result) goto loc_00269B0C;
    result = MiCheckLinearProtectedPteAccessedBit(v_rsi, v_rdi, 128, a4);
    goto loc_00269B0C;
loc_00269D7F:
    if (v_rsi < result) goto loc_00269DF5;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p38)))) << (5);
    result = (a1) ^ (*(unsigned __int64 *)(v_rsi));
    result = (result) & (-993);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_rsi) = result;
    goto loc_00269A22;
loc_00269DAF:
    result = (unsigned __int8)(((unsigned __int8)(v_rdi)) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_00269BCF;
    result = (128) + (a1);
    if (v_rsi < result) goto loc_00269BCF;
    result = MiCheckLinearProtectedPteAccessedBit(v_rsi, v_rdi, 128, a4);
    goto loc_00269BCF;
loc_00269DF5:
    v_r12 = v_r14;
    v_r14 = v_stack_p30;
    if (v_r14 != 0) {
        a1 = v_r14;
        result = MiFlushTbList(a1, v_rdi, 128, a4);
        result = MiReleaseProcessorFlushList(a1, v_rdi, 128, a4);
        v_r12 = 0;
        v_r14 = 0;
        v_stack_p30 = 0;
    }
    result = MiUnlockPageTable(v_rip + 12381179, v_rdi, 128, a4);
    result = MiUnlockWorkingSetShared(v_rip + 12381179, v_stack_pE0, 128, a4);
    a2 = (v_rsi) << (25);
    result = (result) << (25);
    a4 = 0;
    a2 = (a2) - (result);
    a3 = 0;
    a2 = (a2) >> (16);
    a1 = 0;
    result = MmAccessFault(a1, a2, a3, a4);
loc_00269E58:
    result = MiLockWorkingSetShared(v_rip + 12381179, a2, a3, a4);
    result = MiLockNestedPageTable(v_rip + 12381179, v_rdi, a3, a4);
    goto loc_00269BD9;
loc_00269E70:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14011458)))) & (64)) == 0) goto loc_00269CF7;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rip + 12381179, v_rdi, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00269CF7;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), v_rdi, a3, a4);
    goto loc_00269CF9;
loc_00269E97:
    if (0 != 0) goto loc_00269FBF;
loc_00269EA0:
    a1 = (v_rsi) << (25);
    a4 = 0;
    result = (result) << (25);
    a3 = (a3) | (-1);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    result = MiCopyOnWrite(a1, v_rsi, a3, a4);
    if (!sign_flag) goto loc_00269BD9;
    result = MiUnlockPageTable(v_rip + 12381179, v_rdi, a3, a4);
    result = MiUnlockWorkingSetShared(v_rip + 12381179, v_stack_pE0, a3, a4);
    a3 = 0;
    result = MiCopyOnWriteCheckConditions(v_rip + 12381179, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    goto loc_00269E58;
loc_00269F0A:
    if (((*(unsigned __int64 *)(v_rip + 14011251)) & (0x8000ULL)) == 0) goto loc_002697D3;
    a3 = (unsigned int)((a3) & (0xFFFFFFEFULL));
    goto loc_002697D3;
loc_00269F24:
    if (((unsigned int)(result)) != 24) goto loc_00269847;
    goto loc_002697EB;
loc_00269F32:
    result = MiFlushTbList(0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    result = MiReleaseProcessorFlushList(0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    v_r12 = 0;
    v_r14 = 0;
    v_stack_p30 = 0;
loc_00269F58:
    result = MiGetProcessorFlushList(0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    v_stack_p30 = result;
loc_00269F73:
    if (*(unsigned __int64 *)(v_rip + 12336390) == 0) goto loc_00269952;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (16)) != 0) goto loc_00269952;
    a2 = ~(*(unsigned __int64 *)(v_rip + 12336390));
    a2 = (a2) & ((unsigned int)((unsigned int)(result)));
    goto loc_00269952;
loc_00269F9A:
    result = (*(unsigned __int64 *)(result + 24)) & (0);
loc_00269FBF:
    result = MiFlushTbList(0, a2, a3, a4);
    result = MiReleaseProcessorFlushList(0, a2, a3, a4);
    v_r12 = 0;
    v_r14 = 0;
    v_stack_p30 = 0;
    goto loc_00269EA0;
}
```

## 5. (Beta) C Style

```c
int64_t MmProtectPool(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m90;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p8;
    uint8_t v_stack_pE0;
    uint32_t v_stack_pE8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (144);
    if ((((uint8_t)(Arg3)) & (16)) != 0) goto loc_00269F0A;
loc_002697D3:
    result = MiMakeProtectionMask((uint32_t)(Arg3), Arg2, Arg3, Arg2);
    v_stack_m90 = (uint32_t)(result);
    if (((uint32_t)(result)) >= 8) goto loc_00269F24;
loc_002697EB:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (5));
    if (((uint8_t)(Arg1)) == 5) goto loc_00269847;
    if (((uint32_t)(result)) == -1) goto loc_00269847;
    local_rsi = (Arg1) >> (9);
    local_rbp = 0;
    local_rsi = (local_rsi) & (result);
    v_stack_p20 = 0;
    local_r14 = (Arg2 - 1) + (Arg1);
    local_rsi = (local_rsi) + (local_r12);
    result = MiGetSystemRegionType(Arg1, Arg2, Arg3, Arg2);
    if (((uint32_t)(result)) == 5) goto loc_00269885;
    if (((uint32_t)(result)) == 4) goto loc_00269865;
loc_00269847:
    result = 0;
loc_00269849:
    local_rsp = (local_rsp) + (144);
    return result;
loc_00269865:
    result = MiFindLargeMapping(v_stack_p8, local_r14, Arg3, Arg2);
    if ((uint32_t)(result) != 0) goto loc_00269847;
    v_stack_pE8 = (uint32_t)(result + 1);
loc_00269885:
    local_rdi = 0;
    local_r14 = (local_r14) >> (9);
    v_stack_p48 = 0;
    local_r14 = (local_r14) & (v_stack_p8);
    local_r14 = (local_r14) + (local_r12);
    local_r12 = 0;
    v_stack_p50 = local_r14;
    local_r14 = 0;
    v_stack_p30 = 0;
    v_stack_p58 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBC67D6) + *(uint16_t *)(v_rip + 0xBCEBFB + 0xAE) * 8);
    result = MiLockWorkingSetShared(v_rip + 12381179, local_r14, Arg3, Arg2);
    v_stack_pE0 = (uint8_t)(result);
    if (local_rsi <= v_stack_p50) goto loc_002698F5;
loc_002698E1:
    result = MiUnlockWorkingSetShared(v_rip + 12381179, (uint8_t)(result), Arg3, Arg2);
    goto loc_00269849;
loc_002698F5:
loc_00269909:
    if (0 == 0) goto loc_00269A89;
    if (((local_rsi) & (0xFFFULL)) == 0) goto loc_00269F32;
loc_0026991F:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xBCEBFB + 0xB8))) & (15));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 24) goto loc_00269BE2;
    if (((uint8_t)(result)) != 7) goto loc_00269B45;
loc_00269942:
    local_r14 = (uint32_t)((*(uint64_t *)(local_rsi)) & (1));
    if (condition_is_equal) goto loc_00269F73;
loc_00269952:
    Arg2 = (*(uint64_t *)(local_rsi)) >> (12);
    Arg2 = (Arg2) & (Arg3);
    local_rbp = (Arg2 + Arg2 * 2) << (4);
    local_rbp = (local_rbp) + (Arg2);
    result = MiMakeValidPte(local_rsi, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg2);
    if (local_r14 == 0) goto loc_00269F9A;
    if ((uint32_t)((uint32_t)(v_stack_pE8)) != 0) goto loc_00269ACC;
    result = MiWriteValidPteNewProtection(local_rsi, result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg2);
loc_0026999A:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p38)))) << (5);
    Arg1 = (Arg2) ^ (*(uint64_t *)(local_rbp + 0x10));
    Arg1 = (Arg1) & (-993);
    Arg1 = (Arg1) ^ (Arg2);
    *(uint64_t *)(local_rbp + 0x10) = Arg1;
    if ((uint32_t)((uint32_t)(v_stack_pE8)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD5D0AB)) & (256)) != 0) goto loc_00269D1C;
loc_002699E3:
    local_rbx = (local_rsi) << (25);
    result = (*(uint64_t *)(local_rbp + 0x10)) << (25);
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) >> (16);
    if (0 == 0) goto loc_00269F58;
    a4 = 0;
    result = MiInsertTbFlushEntry(0, local_rbx, a4 + 1, a4);
loc_00269A22:
    local_rsi = (local_rsi) + (8);
    if (local_rsi <= v_stack_p50) goto loc_00269909;
    if (0 != 0) {
        Arg1 = 0;
        result = MiFlushTbList(Arg1, local_rbx, a4 + 1, a4);
        result = MiReleaseProcessorFlushList(Arg1, local_rbx, a4 + 1, a4);
    }
    if (v_stack_p48 != 0) {
        Arg1 = v_rip + 12381179;
        result = MiUnlockPageTable(Arg1, v_stack_p48, a4 + 1, a4);
    }
    goto loc_002698E1;
loc_00269A89:
    local_rdi = (local_rsi) >> (9);
    local_rdi = (local_rdi) & (local_rbx);
    local_rdi = (local_rdi) + (v_stack_pE0);
    v_stack_p48 = local_rdi;
    result = MiLockNestedPageTable(v_rip + 12381179, local_rdi, a4 + 1, a4);
    goto loc_0026991F;
loc_00269ACC:
    result = MiLockNonPagedPoolPte(v_rip + 12381179, local_rdi, a4 + 1, a4);
    result = MI_READ_PTE_LOCK_FREE(local_rsi, local_rdi, a4 + 1, a4);
    if (result != local_rbx) goto loc_00269B1A;
    if (result < local_rbx) {
    }
    if (((*(uint64_t *)(v_rip + 0xD5CF90)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00269D39;
loc_00269B0C:
    if (((*(uint64_t *)(v_rip + 0xD5CF90)) & (0x2000000ULL)) == 0) goto loc_0026999A;
loc_00269B1A:
    goto loc_00269942;
loc_00269B45:
    if ((((uint8_t)(local_rbx)) & (1)) == 0) goto loc_00269D7F;
    Arg2 = (local_rbx) >> (12);
    Arg2 = (Arg2) & (a4 + 1);
    local_rbp = (Arg2 + Arg2 * 2) << (4);
    local_rbp = (local_rbp) + (0);
    if (sign_flag) goto loc_00269E97;
    result = MiMakeValidPte(local_rsi, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_p38))), a4);
    local_rdi = (result) & (result);
    result = (local_rbx) & (local_rsi);
    local_rdi = (local_rdi) | (result);
    if (((*(uint64_t *)(v_rip + 0xD5CED7)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00269DAF;
loc_00269BCF:
    if (((*(uint64_t *)(v_rip + 0xD5CED7)) & (0x2000000ULL)) == 0) goto loc_00269C14;
loc_00269BD9:
    local_rsi = (local_rsi) - (8);
    goto loc_00269A22;
loc_00269BE2:
    Arg1 = (uint32_t)((local_rbx) & (1));
    if (Arg1 == 0) goto loc_00269A22;
    result = MiLockNonPagedPoolPte(local_rsi, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_p38))), a4);
loc_00269C14:
    if (((*(uint64_t *)(v_rip + 0xD5CE69)) & (256)) != 0) goto loc_00269D04;
loc_00269C25:
    local_rdi = (local_rsi) << (25);
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p38)))) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) >> (16);
    if (0 != 0) goto loc_00269C6E;
    local_r14 = v_stack_p30;
    if (v_stack_p30 == 0) {
        result = MiGetProcessorFlushList(local_rsi, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_p38))), a4);
        local_r14 = result;
        v_stack_p30 = result;
    }
    a4 = 0;
    v_stack_p20 = 32;
    result = MiInitializeTbFlushList(local_r14, v_rip + 12381179, (uint32_t)(*(uint32_t *)(local_r14 + 0xC)), a4);
loc_00269C6E:
    a4 = 0;
    result = MiInsertTbFlushEntry(local_r14, local_rdi, a4 + 1, a4);
loc_00269C80:
    local_rdi = 0;
loc_00269C82:
    if (condition_is_below) goto loc_00269CE9;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p38)))) << (5);
    Arg1 = (Arg2) ^ (*(uint64_t *)(result + 0x10));
    result = 0;
    Arg1 = (Arg1) & (-993);
    Arg1 = (Arg1) ^ (Arg2);
    *(uint64_t *)(result + 0x10) = Arg1;
    if ((((uint8_t)(*(uint64_t *)(local_rsi))) & (66)) != 0) {
        Arg1 = 0;
        result = MiCaptureDirtyBitToPfn(Arg1, Arg2, a4 + 1, a4);
    }
    if (result == 0) goto loc_00269A22;
    result = MiReleasePageFileInfo(v_stack_p58, result, 1, a4);
    goto loc_00269A22;
loc_00269CE9:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xD5B5BB)) & ((uint32_t)(local_rdi))) == 0) goto loc_00269E70;
loc_00269CF7:
loc_00269CF9:
    if (!sign_flag) goto loc_00269C82;
    goto loc_00269CE9;
loc_00269D04:
    result = MI_TIGHTER_PERMISSIONS(*(uint64_t *)(local_rsi), local_rdi, 1, a4);
    if ((uint32_t)(result) == 0) goto loc_00269C80;
    goto loc_00269C25;
loc_00269D1C:
    result = MI_TIGHTER_PERMISSIONS(*(uint64_t *)(local_rsi), local_rdi, 1, a4);
    if ((uint32_t)(result) != 0) goto loc_002699E3;
    goto loc_00269A22;
loc_00269D39:
    result = (uint8_t)(((uint8_t)(local_rdi)) & (33));
    if (((uint8_t)(result)) != 1) goto loc_00269B0C;
    result = (result) + (*(uint64_t *)(local_rsi));
    if (local_rsi < result) goto loc_00269B0C;
    result = MiCheckLinearProtectedPteAccessedBit(local_rsi, local_rdi, 128, a4);
    goto loc_00269B0C;
loc_00269D7F:
    if (local_rsi < result) goto loc_00269DF5;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p38)))) << (5);
    result = (Arg1) ^ (*(uint64_t *)(local_rsi));
    result = (result) & (-993);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_rsi) = result;
    goto loc_00269A22;
loc_00269DAF:
    result = (uint8_t)(((uint8_t)(local_rdi)) & (33));
    if (((uint8_t)(result)) != 1) goto loc_00269BCF;
    result = (128) + (Arg1);
    if (local_rsi < result) goto loc_00269BCF;
    result = MiCheckLinearProtectedPteAccessedBit(local_rsi, local_rdi, 128, a4);
    goto loc_00269BCF;
loc_00269DF5:
    local_r12 = local_r14;
    local_r14 = v_stack_p30;
    if (local_r14 != 0) {
        Arg1 = local_r14;
        result = MiFlushTbList(Arg1, local_rdi, 128, a4);
        result = MiReleaseProcessorFlushList(Arg1, local_rdi, 128, a4);
        local_r12 = 0;
        local_r14 = 0;
        v_stack_p30 = 0;
    }
    result = MiUnlockPageTable(v_rip + 12381179, local_rdi, 128, a4);
    result = MiUnlockWorkingSetShared(v_rip + 12381179, v_stack_pE0, 128, a4);
    Arg2 = (local_rsi) << (25);
    result = (result) << (25);
    a4 = 0;
    Arg2 = (Arg2) - (result);
    Arg3 = 0;
    Arg2 = (Arg2) >> (16);
    Arg1 = 0;
    result = MmAccessFault(Arg1, Arg2, Arg3, a4);
loc_00269E58:
    result = MiLockWorkingSetShared(v_rip + 12381179, Arg2, Arg3, a4);
    result = MiLockNestedPageTable(v_rip + 12381179, local_rdi, Arg3, a4);
    goto loc_00269BD9;
loc_00269E70:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD5CC42)))) & (64)) == 0) goto loc_00269CF7;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rip + 12381179, local_rdi, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00269CF7;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), local_rdi, Arg3, a4);
    goto loc_00269CF9;
loc_00269E97:
    if (0 != 0) goto loc_00269FBF;
loc_00269EA0:
    Arg1 = (local_rsi) << (25);
    a4 = 0;
    result = (result) << (25);
    Arg3 = (Arg3) | (-1);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    result = MiCopyOnWrite(Arg1, local_rsi, Arg3, a4);
    if (!sign_flag) goto loc_00269BD9;
    result = MiUnlockPageTable(v_rip + 12381179, local_rdi, Arg3, a4);
    result = MiUnlockWorkingSetShared(v_rip + 12381179, v_stack_pE0, Arg3, a4);
    Arg3 = 0;
    result = MiCopyOnWriteCheckConditions(v_rip + 12381179, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, a4);
    goto loc_00269E58;
loc_00269F0A:
    if (((*(uint64_t *)(v_rip + 0xD5CB73)) & (0x8000ULL)) == 0) goto loc_002697D3;
    Arg3 = (uint32_t)((Arg3) & (0xFFFFFFEFULL));
    goto loc_002697D3;
loc_00269F24:
    if (((uint32_t)(result)) != 24) goto loc_00269847;
    goto loc_002697EB;
loc_00269F32:
    result = MiFlushTbList(0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, a4);
    result = MiReleaseProcessorFlushList(0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, a4);
    local_r12 = 0;
    local_r14 = 0;
    v_stack_p30 = 0;
loc_00269F58:
    result = MiGetProcessorFlushList(0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, a4);
    v_stack_p30 = result;
loc_00269F73:
    if (*(uint64_t *)(v_rip + 0xBC3D06) == 0) goto loc_00269952;
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (16)) != 0) goto loc_00269952;
    Arg2 = ~(*(uint64_t *)(v_rip + 0xBC3D06));
    Arg2 = (Arg2) & ((uint32_t)((uint32_t)(result)));
    goto loc_00269952;
loc_00269F9A:
    result = (*(uint64_t *)(result + 0x18)) & (0);
loc_00269FBF:
    result = MiFlushTbList(0, Arg2, Arg3, a4);
    result = MiReleaseProcessorFlushList(0, Arg2, Arg3, a4);
    local_r12 = 0;
    local_r14 = 0;
    v_stack_p30 = 0;
    goto loc_00269EA0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002697AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
