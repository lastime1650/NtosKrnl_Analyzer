# MiLockProtoPoolPage

- RVA: `0x002B8B80`–`0x002B9239` (길이 `1,721` bytes)
- VA: `0x00000001402B8B80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006DBE0`
- 디코드: `380`개 명령, `1,721/1,721` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **19**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002B8E80` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002B8F95` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002B9031` → [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x002B9046` → [MiIsDecayPfn](MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x002B9064` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002B9093` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B90A2` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B90BA` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B90C9` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B90DF` → [MiGetLeafPfnBuddy](../43/MiGetLeafPfnBuddy_function_00438E30.md) (function, `0x00438E30`)
- `0x002B9134` → [MiSpinForProtoPoolLock](../43/MiSpinForProtoPoolLock_function_00434540.md) (function, `0x00434540`)
- `0x002B916D` → [MiChargePartitionResidentAvailable](../28/MiChargePartitionResidentAvailable_function_0028B000.md) (function, `0x0028B000`)
- `0x002B918C` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x002B91A0` → [MiWriteValidPteVolatile](../29/MiWriteValidPteVolatile_function_00292B60.md) (function, `0x00292B60`)
- `0x002B91C1` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x002B91D9` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B91E9` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [MiTranslatePageForCopy](../22/MiTranslatePageForCopy_function_00228960.md) at `0x00228DC7`
- [MiCombineWithStandbyExisting](../22/MiCombineWithStandbyExisting_function_00229E74.md) at `0x00229F28`
- [MiCombineWithExisting](../22/MiCombineWithExisting_function_0022B4B8.md) at `0x0022B57B`
- [MiResolveProtoCombine](../22/MiResolveProtoCombine_function_0022CD00.md) at `0x0022CD26`
- [MiWalkVaRange](../24/MiWalkVaRange_function_00243BF0.md) at `0x002445FE`
- [MiMigratePfn](../28/MiMigratePfn_function_0028DBB0.md) at `0x0028DF6A`
- [MiGetWorkingSetInfoList](../2A/MiGetWorkingSetInfoList_function_002AF770.md) at `0x002B059A`
- [MiStealPage](MiStealPage_function_002B28D0.md) at `0x002B35D7`
- [MiMakePageAvoidRead](MiMakePageAvoidRead_function_002B7DE0.md) at `0x002B8135`
- [MiSoftFaultMappedView](../36/MiSoftFaultMappedView_function_00365364.md) at `0x00365681`
- [MiWalkEntireImage](../36/MiWalkEntireImage_function_00365D70.md) at `0x00366905`
- [MiZeroCfgSystemWideBitmapWorker](../36/MiZeroCfgSystemWideBitmapWorker_function_00367060.md) at `0x00367481`
- [MiResolveMappedFileFault](../36/MiResolveMappedFileFault_function_0036B640.md) at `0x0036B88B`
- [MiAllocateInPageSupport](../36/MiAllocateInPageSupport_function_0036F100.md) at `0x0036F1B3`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x0036FF7C`
- [MiDeleteMergedPte](../37/MiDeleteMergedPte_function_00371040.md) at `0x00371067`
- [MiReplaceLockedPage](../38/MiReplaceLockedPage_function_0038351C.md) at `0x00383658`
- [MiGetPageFileSectionForReservation](../38/MiGetPageFileSectionForReservation_function_00385E2C.md) at `0x00385EAC`
- [MiInsertLargeVadMapping](../3F/MiInsertLargeVadMapping_function_003F0498.md) at `0x003F04D1`

### Static image references
- `0x002B8C2E` → RVA `0x00E2DCE0` (`.data`; read)
- `0x002B8C79` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002B8EB1` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002B8F3C` → RVA `0x00E30088` (`.data`; read)
- `0x002B8F51` → RVA `0x00E38D00` (`.data`; read)
- `0x002B8FC1` → RVA `0x00E35C00` (`.data`; read)
- `0x002B9085` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002B8B80  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002B8B85  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
002B8B8A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
002B8B8F  55                              push rbp
002B8B90  41 54                           push r12
002B8B92  41 55                           push r13
002B8B94  41 56                           push r14
002B8B96  41 57                           push r15
002B8B98  48 81 EC E0 00 00 00            sub rsp, 0xe0
002B8B9F  48 8D 6C 24 60                  lea rbp, [rsp + 0x60]
002B8BA4  48 83 E5 C0                     and rbp, 0xffffffffffffffc0
002B8BA8  4C 8B E2                        mov r12, rdx
002B8BAB  48 85 D2                        test rdx, rdx
002B8BAE  74 03                           je 0x1402b8bb3
002B8BB0  C6 02 11                        mov byte ptr [rdx], 0x11
002B8BB3  48 C1 E9 09                     shr rcx, 9
002B8BB7  49 BE F8 FF FF FF 7F 00 00 00   movabs r14, 0x7ffffffff8
002B8BC1  4C 23 F1                        and r14, rcx
002B8BC4  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
002B8BCE  49 8B C3                        mov rax, r11
002B8BD1  4C 03 F0                        add r14, rax
002B8BD4  48 BE 00 00 00 00 00 00 40 00   movabs rsi, 0x40000000000000
002B8BDE  45 33 ED                        xor r13d, r13d
002B8BE1  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
002B8BEB  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
002B8BF5  41 B9 02 00 00 00               mov r9d, 2
002B8BFB  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
002B8C05  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
002B8C10  49 8B 1E                        mov rbx, qword ptr [r14]
002B8C13  F6 C3 01                        test bl, 1
002B8C16  0F 84 DF 00 00 00               je 0x1402b8cfb
002B8C1C  48 0F BA E3 09                  bt rbx, 9
002B8C21  0F 82 D4 00 00 00               jb 0x1402b8cfb
002B8C27  48 C1 EB 0C                     shr rbx, 0xc
002B8C2B  48 23 DA                        and rbx, rdx
002B8C2E  48 3B 1D AB 50 B7 00            cmp rbx, qword ptr [rip + 0xb750ab]
002B8C35  77 D9                           ja 0x1402b8c10
002B8C37  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
002B8C3B  48 03 C9                        add rcx, rcx
002B8C3E  48 8B C0                        mov rax, rax
002B8C41  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
002B8C45  48 85 C6                        test rsi, rax
002B8C48  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
002B8C52  74 BC                           je 0x1402b8c10
002B8C54  49 8B C0                        mov rax, r8
002B8C57  48 8D 3C C8                     lea rdi, [rax + rcx*8]
002B8C5B  4D 85 E4                        test r12, r12
002B8C5E  0F 84 38 02 00 00               je 0x1402b8e9c
002B8C64  48 3B 1D 75 50 B7 00            cmp rbx, qword ptr [rip + 0xb75075]
002B8C6B  0F 87 50 03 00 00               ja 0x1402b8fc1
002B8C71  45 0F 20 C7                     mov r15, cr8
002B8C75  45 0F 22 C1                     mov cr8, r9
002B8C79  44 39 2D A0 E0 D0 00            cmp dword ptr [rip + 0xd0e0a0], r13d
002B8C80  0F 85 09 03 00 00               jne 0x1402b8f8f
002B8C86  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
002B8C8A  48 85 C6                        test rsi, rax
002B8C8D  0F 84 B0 03 00 00               je 0x1402b9043
002B8C93  41 8B F5                        mov esi, r13d
002B8C96  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
002B8C9D  0F 82 2D 02 00 00               jb 0x1402b8ed0
002B8CA3  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
002B8CAD  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
002B8CB7  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
002B8CC1  48 BE 00 00 00 00 00 00 40 00   movabs rsi, 0x40000000000000
002B8CCB  41 B9 02 00 00 00               mov r9d, 2
002B8CD1  41 80 FF 11                     cmp r15b, 0x11
002B8CD5  0F 84 35 FF FF FF               je 0x1402b8c10
002B8CDB  49 8B 06                        mov rax, qword ptr [r14]
002B8CDE  A8 01                           test al, 1
002B8CE0  75 3D                           jne 0x1402b8d1f
002B8CE2  41 80 FF 11                     cmp r15b, 0x11
002B8CE6  0F 85 CE 04 00 00               jne 0x1402b91ba
002B8CEC  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B8CF6  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
002B8CFB  33 C0                           xor eax, eax
002B8CFD  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
002B8D05  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
002B8D09  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
002B8D0D  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
002B8D11  49 8B E3                        mov rsp, r11
002B8D14  41 5F                           pop r15
002B8D16  41 5E                           pop r14
002B8D18  41 5D                           pop r13
002B8D1A  41 5C                           pop r12
002B8D1C  5D                              pop rbp
002B8D1D  C3                              ret
002B8D1E  CC                              int3
002B8D1F  48 0F BA E0 09                  bt rax, 9
002B8D24  72 BC                           jb 0x1402b8ce2
002B8D26  48 C1 E8 0C                     shr rax, 0xc
002B8D2A  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
002B8D34  48 23 C2                        and rax, rdx
002B8D37  48 3B D8                        cmp rbx, rax
002B8D3A  0F 85 F2 00 00 00               jne 0x1402b8e32
002B8D40  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
002B8D44  49 B8 00 00 00 00 00 00 00 80   movabs r8, 0x8000000000000000
002B8D4E  48 0F BA E0 28                  bt rax, 0x28
002B8D53  72 4C                           jb 0x1402b8da1
002B8D55  48 0F BA 67 28 35               bt qword ptr [rdi + 0x28], 0x35
002B8D5B  72 44                           jb 0x1402b8da1
002B8D5D  8B 57 20                        mov edx, dword ptr [rdi + 0x20]
002B8D60  48 8D 77 20                     lea rsi, [rdi + 0x20]
002B8D64  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
002B8D68  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
002B8D72  48 23 C1                        and rax, rcx
002B8D75  41 8B CD                        mov ecx, r13d
002B8D78  66 85 D2                        test dx, dx
002B8D7B  0F 84 6E 01 00 00               je 0x1402b8eef
002B8D81  66 83 FA 01                     cmp dx, 1
002B8D85  0F 85 14 02 00 00               jne 0x1402b8f9f
002B8D8B  48 85 C0                        test rax, rax
002B8D8E  0F 84 E2 02 00 00               je 0x1402b9076
002B8D94  B9 01 00 00 00                  mov ecx, 1
002B8D99  85 C9                           test ecx, ecx
002B8D9B  0F 85 4E 01 00 00               jne 0x1402b8eef
002B8DA1  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
002B8DA4  48 8D 77 20                     lea rsi, [rdi + 0x20]
002B8DA8  89 45 00                        mov dword ptr [rbp], eax
002B8DAB  66 FF C0                        inc ax
002B8DAE  66 89 45 00                     mov word ptr [rbp], ax
002B8DB2  8B 45 00                        mov eax, dword ptr [rbp]
002B8DB5  89 47 20                        mov dword ptr [rdi + 0x20], eax
002B8DB8  41 80 FF 11                     cmp r15b, 0x11
002B8DBC  74 04                           je 0x1402b8dc2
002B8DBE  45 88 3C 24                     mov byte ptr [r12], r15b
002B8DC2  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
002B8DC6  0F 57 C0                        xorps xmm0, xmm0
002B8DC9  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
002B8DD3  48 0B D8                        or rbx, rax
002B8DD6  F6 47 22 20                     test byte ptr [rdi + 0x22], 0x20
002B8DDA  0F 11 45 40                     movups xmmword ptr [rbp + 0x40], xmm0
002B8DDE  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
002B8DE2  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
002B8DE6  0F 11 45 70                     movups xmmword ptr [rbp + 0x70], xmm0
002B8DEA  0F 85 E3 02 00 00               jne 0x1402b90d3
002B8DF0  8B 06                           mov eax, dword ptr [rsi]
002B8DF2  48 BE FF FF FF FF FF FF FF 7F   movabs rsi, 0x7fffffffffffffff
002B8DFC  89 45 00                        mov dword ptr [rbp], eax
002B8DFF  C1 E8 10                        shr eax, 0x10
002B8E02  0C 20                           or al, 0x20
002B8E04  88 45 02                        mov byte ptr [rbp + 2], al
002B8E07  8B 45 00                        mov eax, dword ptr [rbp]
002B8E0A  89 47 20                        mov dword ptr [rdi + 0x20], eax
002B8E0D  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
002B8E11  48 0F BA E0 3E                  bt rax, 0x3e
002B8E16  72 0D                           jb 0x1402b8e25
002B8E18  4C 8B 03                        mov r8, qword ptr [rbx]
002B8E1B  41 F6 C0 20                     test r8b, 0x20
002B8E1F  0F 84 71 03 00 00               je 0x1402b9196
002B8E25  F0 48 21 77 18                  lock and qword ptr [rdi + 0x18], rsi
002B8E2A  48 8B C7                        mov rax, rdi
002B8E2D  E9 CB FE FF FF                  jmp 0x1402b8cfd
002B8E32  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B8E3C  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
002B8E41  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
002B8E4B  48 BE 00 00 00 00 00 00 40 00   movabs rsi, 0x40000000000000
002B8E55  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
002B8E5F  41 B9 02 00 00 00               mov r9d, 2
002B8E65  41 80 FF 01                     cmp r15b, 1
002B8E69  0F 87 A1 FD FF FF               ja 0x1402b8c10
002B8E6F  44 39 2D AA DE D0 00            cmp dword ptr [rip + 0xd0deaa], r13d
002B8E76  74 17                           je 0x1402b8e8f
002B8E78  44 0F 20 C1                     mov rcx, cr8
002B8E7C  41 0F B6 D7                     movzx edx, r15b
002B8E80  E8 13 C8 23 00                  call 0x1404f5698
002B8E85  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
002B8E8F  41 0F B6 C7                     movzx eax, r15b
002B8E93  44 0F 22 C0                     mov cr8, rax
002B8E97  E9 4F FD FF FF                  jmp 0x1402b8beb
002B8E9C  41 B7 11                        mov r15b, 0x11
002B8E9F  41 8B F5                        mov esi, r13d
002B8EA2  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
002B8EA9  0F 83 2C FE FF FF               jae 0x1402b8cdb
002B8EAF  FF C6                           inc esi
002B8EB1  85 35 F5 C3 D0 00               test dword ptr [rip + 0xd0c3f5], esi
002B8EB7  0F 84 EF 01 00 00               je 0x1402b90ac
002B8EBD  F3 90                           pause
002B8EBF  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
002B8EC3  48 85 C0                        test rax, rax
002B8EC6  79 DA                           jns 0x1402b8ea2
002B8EC8  EB E5                           jmp 0x1402b8eaf
002B8ECA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
002B8ED0  FF C6                           inc esi
002B8ED2  85 35 D4 C3 D0 00               test dword ptr [rip + 0xd0c3d4], esi
002B8ED8  0F 84 A7 01 00 00               je 0x1402b9085
002B8EDE  F3 90                           pause
002B8EE0  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
002B8EE4  48 85 C0                        test rax, rax
002B8EE7  0F 89 A9 FD FF FF               jns 0x1402b8c96
002B8EED  EB E1                           jmp 0x1402b8ed0
002B8EEF  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
002B8EF3  45 32 F6                        xor r14b, r14b
002B8EF6  48 85 C0                        test rax, rax
002B8EF9  0F 88 F0 00 00 00               js 0x1402b8fef
002B8EFF  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
002B8F03  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
002B8F0D  49 8B C3                        mov rax, r11
002B8F10  48 BA 78 FF FF FF 3F 00 00 00   movabs rdx, 0x3fffffff78
002B8F1A  49 0B C8                        or rcx, r8
002B8F1D  48 03 C2                        add rax, rdx
002B8F20  48 3B C8                        cmp rcx, rax
002B8F23  77 13                           ja 0x1402b8f38
002B8F25  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
002B8F29  49 0B C8                        or rcx, r8
002B8F2C  49 8B C3                        mov rax, r11
002B8F2F  48 3B C8                        cmp rcx, rax
002B8F32  0F 83 C7 00 00 00               jae 0x1402b8fff
002B8F38  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
002B8F3C  48 8B 05 45 71 B7 00            mov rax, qword ptr [rip + 0xb77145]
002B8F43  48 C1 E9 2B                     shr rcx, 0x2b
002B8F47  81 E1 FF 03 00 00               and ecx, 0x3ff
002B8F4D  48 8B 1C C8                     mov rbx, qword ptr [rax + rcx*8]
002B8F51  48 8D 05 A8 FD B7 00            lea rax, [rip + 0xb7fda8]
002B8F58  48 3B D8                        cmp rbx, rax
002B8F5B  0F 85 FE 01 00 00               jne 0x1402b915f
002B8F61  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
002B8F6A  8B 82 9C 8B 00 00               mov eax, dword ptr [rdx + 0x8b9c]
002B8F70  8D 48 FF                        lea ecx, [rax - 1]
002B8F73  83 F9 FD                        cmp ecx, -3
002B8F76  0F 87 E3 01 00 00               ja 0x1402b915f
002B8F7C  8D 48 FF                        lea ecx, [rax - 1]
002B8F7F  F0 0F B1 8A 9C 8B 00 00         lock cmpxchg dword ptr [rdx + 0x8b9c], ecx
002B8F87  0F 84 14 FE FF FF               je 0x1402b8da1
002B8F8D  EB E1                           jmp 0x1402b8f70
002B8F8F  B2 02                           mov dl, 2
002B8F91  41 0F B6 CF                     movzx ecx, r15b
002B8F95  E8 62 C7 23 00                  call 0x1404f56fc
002B8F9A  E9 E7 FC FF FF                  jmp 0x1402b8c86
002B8F9F  66 83 FA 02                     cmp dx, 2
002B8FA3  0F 85 F8 FD FF FF               jne 0x1402b8da1
002B8FA9  48 85 C0                        test rax, rax
002B8FAC  0F 84 EF FD FF FF               je 0x1402b8da1
002B8FB2  F6 47 22 08                     test byte ptr [rdi + 0x22], 8
002B8FB6  0F 85 33 FF FF FF               jne 0x1402b8eef
002B8FBC  E9 E0 FD FF FF                  jmp 0x1402b8da1
002B8FC1  48 8B 05 38 CC B7 00            mov rax, qword ptr [rip + 0xb7cc38]
002B8FC8  48 3B D8                        cmp rbx, rax
002B8FCB  0F 82 2A FC FF FF               jb 0x1402b8bfb
002B8FD1  48 05 00 08 00 00               add rax, 0x800
002B8FD7  48 3B D8                        cmp rbx, rax
002B8FDA  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
002B8FE4  0F 83 26 FC FF FF               jae 0x1402b8c10
002B8FEA  E9 82 FC FF FF                  jmp 0x1402b8c71
002B8FEF  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
002B8FF2  48 0F BA E0 0A                  bt rax, 0xa
002B8FF7  0F 83 02 FF FF FF               jae 0x1402b8eff
002B8FFD  EB 0A                           jmp 0x1402b9009
002B8FFF  F6 47 23 20                     test byte ptr [rdi + 0x23], 0x20
002B9003  0F 84 13 02 00 00               je 0x1402b921c
002B9009  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
002B900D  BA 01 00 00 00                  mov edx, 1
002B9012  48 8B 05 6F 70 B7 00            mov rax, qword ptr [rip + 0xb7706f]
002B9019  41 B6 01                        mov r14b, 1
002B901C  48 C1 E9 2B                     shr rcx, 0x2b
002B9020  81 E1 FF 03 00 00               and ecx, 0x3ff
002B9026  44 8D 42 03                     lea r8d, [rdx + 3]
002B902A  48 8B 1C C8                     mov rbx, qword ptr [rax + rcx*8]
002B902E  48 8B CB                        mov rcx, rbx
002B9031  E8 7A DE FC FF                  call 0x140286eb0
002B9036  85 C0                           test eax, eax
002B9038  0F 84 7A FD FF FF               je 0x1402b8db8
002B903E  E9 0E FF FF FF                  jmp 0x1402b8f51
002B9043  48 8B CB                        mov rcx, rbx
002B9046  E8 F5 01 00 00                  call 0x1402b9240
002B904B  85 C0                           test eax, eax
002B904D  0F 85 40 FC FF FF               jne 0x1402b8c93
002B9053  44 39 2D C6 DC D0 00            cmp dword ptr [rip + 0xd0dcc6], r13d
002B905A  74 0D                           je 0x1402b9069
002B905C  44 0F 20 C1                     mov rcx, cr8
002B9060  41 0F B6 D7                     movzx edx, r15b
002B9064  E8 2F C6 23 00                  call 0x1404f5698
002B9069  41 0F B6 C7                     movzx eax, r15b
002B906D  44 0F 22 C0                     mov cr8, rax
002B9071  E9 6B FB FF FF                  jmp 0x1402b8be1
002B9076  F6 47 22 08                     test byte ptr [rdi + 0x22], 8
002B907A  0F 84 19 FD FF FF               je 0x1402b8d99
002B9080  E9 0F FD FF FF                  jmp 0x1402b8d94
002B9085  8B 05 2D DA D0 00               mov eax, dword ptr [rip + 0xd0da2d]
002B908B  A8 40                           test al, 0x40
002B908D  0F 84 4B FE FF FF               je 0x1402b8ede
002B9093  E8 F8 63 05 00                  call 0x14030f490
002B9098  84 C0                           test al, al
002B909A  0F 84 3E FE FF FF               je 0x1402b8ede
002B90A0  8B CE                           mov ecx, esi
002B90A2  E8 B9 63 05 00                  call 0x14030f460
002B90A7  E9 34 FE FF FF                  jmp 0x1402b8ee0
002B90AC  8B 05 06 DA D0 00               mov eax, dword ptr [rip + 0xd0da06]
002B90B2  A8 40                           test al, 0x40
002B90B4  0F 84 03 FE FF FF               je 0x1402b8ebd
002B90BA  E8 D1 63 05 00                  call 0x14030f490
002B90BF  84 C0                           test al, al
002B90C1  0F 84 F6 FD FF FF               je 0x1402b8ebd
002B90C7  8B CE                           mov ecx, esi
002B90C9  E8 92 63 05 00                  call 0x14030f460
002B90CE  E9 EC FD FF FF                  jmp 0x1402b8ebf
002B90D3  BA 01 00 00 00                  mov edx, 1
002B90D8  44 89 6D 50                     mov dword ptr [rbp + 0x50], r13d
002B90DC  48 8B CF                        mov rcx, rdi
002B90DF  E8 4C FD 17 00                  call 0x140438e30
002B90E4  48 85 C0                        test rax, rax
002B90E7  0F 85 BD 00 00 00               jne 0x1402b91aa
002B90ED  48 8D 45 40                     lea rax, [rbp + 0x40]
002B90F1  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
002B90F5  48 8D 55 40                     lea rdx, [rbp + 0x40]
002B90F9  48 8D 45 40                     lea rax, [rbp + 0x40]
002B90FD  48 C1 EA 03                     shr rdx, 3
002B9101  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
002B9105  48 8B CA                        mov rcx, rdx
002B9108  48 8B 07                        mov rax, qword ptr [rdi]
002B910B  48 33 C8                        xor rcx, rax
002B910E  48 B8 01 00 00 00 00 F0 FF FF   movabs rax, 0xfffff00000000001
002B9118  48 23 C8                        and rcx, rax
002B911B  48 33 CA                        xor rcx, rdx
002B911E  48 89 0F                        mov qword ptr [rdi], rcx
002B9121  48 BE FF FF FF FF FF FF FF 7F   movabs rsi, 0x7fffffffffffffff
002B912B  F0 48 21 77 18                  lock and qword ptr [rdi + 0x18], rsi
002B9130  48 8D 4D 40                     lea rcx, [rbp + 0x40]
002B9134  E8 07 B4 17 00                  call 0x140434540
002B9139  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
002B9140  0F 83 C7 FC FF FF               jae 0x1402b8e0d
002B9146  41 FF C5                        inc r13d
002B9149  44 85 2D 5C C1 D0 00            test dword ptr [rip + 0xd0c15c], r13d
002B9150  74 79                           je 0x1402b91cb
002B9152  F3 90                           pause
002B9154  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
002B9158  48 85 C0                        test rax, rax
002B915B  79 DC                           jns 0x1402b9139
002B915D  EB E7                           jmp 0x1402b9146
002B915F  BA 01 00 00 00                  mov edx, 1
002B9164  41 B8 FF FF FF FF               mov r8d, 0xffffffff
002B916A  48 8B CB                        mov rcx, rbx
002B916D  E8 8E 1E FD FF                  call 0x14028b000
002B9172  85 C0                           test eax, eax
002B9174  0F 85 27 FC FF FF               jne 0x1402b8da1
002B917A  45 84 F6                        test r14b, r14b
002B917D  0F 84 8C 00 00 00               je 0x1402b920f
002B9183  45 33 C0                        xor r8d, r8d
002B9186  8D 50 01                        lea edx, [rax + 1]
002B9189  48 8B CB                        mov rcx, rbx
002B918C  E8 7F F2 F8 FF                  call 0x140248410
002B9191  E9 22 FC FF FF                  jmp 0x1402b8db8
002B9196  45 33 C0                        xor r8d, r8d
002B9199  48 8B CB                        mov rcx, rbx
002B919C  41 8D 50 01                     lea edx, [r8 + 1]
002B91A0  E8 BB 99 FD FF                  call 0x140292b60
002B91A5  E9 7B FC FF FF                  jmp 0x1402b8e25
002B91AA  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002B91AE  48 39 01                        cmp qword ptr [rcx], rax
002B91B1  74 40                           je 0x1402b91f3
002B91B3  B9 03 00 00 00                  mov ecx, 3
002B91B8  CD 29                           int 0x29
002B91BA  41 0F B6 D7                     movzx edx, r15b
002B91BE  48 8B CF                        mov rcx, rdi
002B91C1  E8 1A 12 06 00                  call 0x14031a3e0
002B91C6  E9 30 FB FF FF                  jmp 0x1402b8cfb
002B91CB  8B 05 E7 D8 D0 00               mov eax, dword ptr [rip + 0xd0d8e7]
002B91D1  A8 40                           test al, 0x40
002B91D3  0F 84 79 FF FF FF               je 0x1402b9152
002B91D9  E8 B2 62 05 00                  call 0x14030f490
002B91DE  84 C0                           test al, al
002B91E0  0F 84 6C FF FF FF               je 0x1402b9152
002B91E6  41 8B CD                        mov ecx, r13d
002B91E9  E8 72 62 05 00                  call 0x14030f460
002B91EE  E9 61 FF FF FF                  jmp 0x1402b9154
002B91F3  48 89 4D 48                     mov qword ptr [rbp + 0x48], rcx
002B91F7  48 8D 55 40                     lea rdx, [rbp + 0x40]
002B91FB  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
002B91FF  48 89 11                        mov qword ptr [rcx], rdx
002B9202  48 8D 4D 40                     lea rcx, [rbp + 0x40]
002B9206  48 89 48 08                     mov qword ptr [rax + 8], rcx
002B920A  E9 12 FF FF FF                  jmp 0x1402b9121
002B920F  85 C0                           test eax, eax
002B9211  0F 85 8A FB FF FF               jne 0x1402b8da1
002B9217  E9 9C FB FF FF                  jmp 0x1402b8db8
002B921C  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
002B9220  48 8B 0D 61 6E B7 00            mov rcx, qword ptr [rip + 0xb76e61]
002B9227  48 C1 E8 2B                     shr rax, 0x2b
002B922B  25 FF 03 00 00                  and eax, 0x3ff
002B9230  48 8B 1C C1                     mov rbx, qword ptr [rcx + rax*8]
002B9234  E9 18 FD FF FF                  jmp 0x1402b8f51
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockProtoPoolPage(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_mA6;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (224);
    v_rbp = (v_stack_mA8) & (-64);
    if (a2 != 0) {
        *(unsigned __int8 *)(a2) = 17;
    }
    a1 = (a1) >> (9);
    v_r14 = (v_r14) & (a1);
    v_r14 = (v_r14) + (v_r11);
    v_r13 = 0;
loc_002B8BE1:
loc_002B8BEB:
loc_002B8BFB:
loc_002B8C10:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (1)) == 0) goto loc_002B8CFB;
    if (condition_is_below) goto loc_002B8CFB;
    v_rbx = (*(unsigned __int64 *)(v_r14)) >> (12);
    v_rbx = (v_rbx) & (a2);
    if (v_rbx > (*(unsigned __int64 *)(v_rip + 12013739))) goto loc_002B8C10;
    a1 = (v_rbx + v_rbx * 2) + (v_rbx + v_rbx * 2);
    if (((v_rsi) & (*(unsigned __int64 *)(v_r11 + a1 * 8))) == 0) goto loc_002B8C10;
    if (a2 == 0) goto loc_002B8E9C;
    if (v_rbx > (*(unsigned __int64 *)(v_rip + 12013685))) goto loc_002B8FC1;
loc_002B8C71:
    if ((*(unsigned int *)(v_rip + 13688992)) != 0) goto loc_002B8F8F;
loc_002B8C86:
    if (((v_rsi) & (*(unsigned __int64 *)(a3 + a1 * 8 + 40))) == 0) goto loc_002B9043;
loc_002B8C93:
loc_002B8C96:
    if (condition_is_below) goto loc_002B8ED0;
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_002B8C10;
loc_002B8CDB:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (1)) != 0) goto loc_002B8D1F;
loc_002B8CE2:
    if (((unsigned __int8)(v_cr8)) != 17) goto loc_002B91BA;
loc_002B8CFB:
    result = 0;
loc_002B8CFD:
    return result;
loc_002B8D1F:
    if (condition_is_below) goto loc_002B8CE2;
    result = (result) >> (12);
    result = (result) & (a2);
    if ((*(unsigned __int64 *)(v_stack_m28 + 48)) != result) goto loc_002B8E32;
    if ((*(unsigned __int64 *)(v_stack_m28 + 48)) < result) goto loc_002B8DA1;
    if ((*(unsigned __int64 *)(v_stack_m28 + 48)) < result) goto loc_002B8DA1;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 24)) & (a1);
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32))) == 0) goto loc_002B8EEF;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)))) != 1) goto loc_002B8F9F;
    if (result == 0) goto loc_002B9076;
loc_002B8D94:
loc_002B8D99:
    if (1 != 0) goto loc_002B8EEF;
loc_002B8DA1:
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)));
    result = (unsigned __int16)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32))) + 1);
    v_stack_mA8 = (unsigned __int16)(result);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32) = (unsigned int)((unsigned int)(v_stack_mA8));
loc_002B8DB8:
    if (((unsigned __int8)(v_cr8)) != 17) {
        *(unsigned __int8 *)(a2) = (unsigned __int8)(v_cr8);
    }
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8)) | ((unsigned int)(v_stack_mA8));
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 34)) & (32)) != 0) goto loc_002B90D3;
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32))) >> (16));
    result = (unsigned __int8)((result) | (32));
    v_stack_mA6 = (unsigned __int8)(result);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32) = (unsigned int)((unsigned int)(v_stack_mA8));
loc_002B8E0D:
    if (condition_is_below) goto loc_002B8E25;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (32)) == 0) goto loc_002B9196;
loc_002B8E25:
    goto loc_002B8CFD;
loc_002B8E32:
    if (((unsigned __int8)(v_cr8)) > 1) goto loc_002B8C10;
    result = *(unsigned __int64 *)(v_stack_m28 + 64);
    if ((*(unsigned int *)(v_rip + 13688490)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rbx), 2);
    }
    goto loc_002B8BEB;
loc_002B8E9C:
loc_002B8EA2:
    if ((*(unsigned int *)(v_rip + 13688490)) >= 0) goto loc_002B8CDB;
loc_002B8EAF:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13681653)) & ((unsigned int)(v_rsi))) == 0) goto loc_002B90AC;
loc_002B8EBD:
loc_002B8EBF:
    if (!sign_flag) goto loc_002B8EA2;
    goto loc_002B8EAF;
loc_002B8ED0:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 13681620)) & ((unsigned int)(v_rsi))) == 0) goto loc_002B9085;
loc_002B8EDE:
loc_002B8EE0:
    if (!sign_flag) goto loc_002B8C96;
    goto loc_002B8ED0;
loc_002B8EEF:
    v_r14 = 0;
    if (sign_flag) goto loc_002B8FEF;
loc_002B8EFF:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8)) | (*(unsigned __int64 *)(v_rbx));
    result = (v_stack_m28) + (a2);
    if (a1 > result) goto loc_002B8F38;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8)) | (*(unsigned __int64 *)(v_rbx));
    if (a1 >= v_stack_m28) goto loc_002B8FFF;
loc_002B8F38:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
loc_002B8F51:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12022085) + a1 * 8)) != (v_rip + 12058024)) goto loc_002B915F;
loc_002B8F70:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)) - 1)) > -3) goto loc_002B915F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)) - 1)) == -3) goto loc_002B8DA1;
    goto loc_002B8F70;
loc_002B8F8F:
    result = KiRaiseIrqlProcessIrqlFlags(17, 2, *(unsigned __int64 *)(v_rbx), 2);
    goto loc_002B8C86;
loc_002B8F9F:
    if (2 != 2) goto loc_002B8DA1;
    if (result == 0) goto loc_002B8DA1;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 34)) & (8)) != 0) goto loc_002B8EEF;
    goto loc_002B8DA1;
loc_002B8FC1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12022085) + a1 * 8)) < (*(unsigned __int64 *)(v_rip + 12045368))) goto loc_002B8BFB;
    result = (*(unsigned __int64 *)(v_rip + 12045368)) + (0x800ULL);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12022085) + a1 * 8)) >= result) goto loc_002B8C10;
    goto loc_002B8C71;
loc_002B8FEF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12022085) + a1 * 8)) >= result) goto loc_002B8EFF;
    goto loc_002B9009;
loc_002B8FFF:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 35)) & (32)) == 0) goto loc_002B921C;
loc_002B9009:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    result = MiChargeCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12021871) + a1 * 8), 1, 1 + 3, 2);
    if ((unsigned int)(result) == 0) goto loc_002B8DB8;
    goto loc_002B8F51;
loc_002B9043:
    result = MiIsDecayPfn(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12021871) + a1 * 8), 1, 1 + 3, 2);
    if ((unsigned int)(result) != 0) goto loc_002B8C93;
    if ((*(unsigned int *)(v_rip + 13688006)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1 + 3, 2);
    }
    goto loc_002B8BE1;
loc_002B9076:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 34)) & (8)) == 0) goto loc_002B8D99;
    goto loc_002B8D94;
loc_002B9085:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13687341)))) & (64)) == 0) goto loc_002B8EDE;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, 1 + 3, 2);
    if ((unsigned __int8)(result) == 0) goto loc_002B8EDE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), a2, 1 + 3, 2);
    goto loc_002B8EE0;
loc_002B90AC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13687302)))) & (64)) == 0) goto loc_002B8EBD;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), a2, 1 + 3, 2);
    if ((unsigned __int8)(result) == 0) goto loc_002B8EBD;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), a2, 1 + 3, 2);
    goto loc_002B8EBF;
loc_002B90D3:
    v_stack_m58 = 0;
    result = MiGetLeafPfnBuddy(*(unsigned __int64 *)(v_stack_m28 + 64), 1, 1 + 3, 2);
    if (result != 0) goto loc_002B91AA;
    v_stack_m60 = v_stack_m68;
    a2 = (v_stack_m68) >> (3);
    v_stack_m68 = v_stack_m68;
    a1 = (a2) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)));
    a1 = (a1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)));
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64)) = a1;
loc_002B9121:
    result = MiSpinForProtoPoolLock(v_stack_m68, a2, 1 + 3, 2);
loc_002B9139:
    if (condition_is_above_or_equal) goto loc_002B8E0D;
loc_002B9146:
    v_r13 = (unsigned int)((v_r13) + 1);
    if (((*(unsigned int *)(v_rip + 13680988)) & ((unsigned int)(v_r13))) == 0) goto loc_002B91CB;
loc_002B9152:
loc_002B9154:
    if (!sign_flag) goto loc_002B9139;
    goto loc_002B9146;
loc_002B915F:
    result = MiChargePartitionResidentAvailable(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12021871) + a1 * 8), 1, (unsigned int)(0xFFFFFFFFULL), 2);
    if ((unsigned int)(result) != 0) goto loc_002B8DA1;
    if (1 == 0) goto loc_002B920F;
    a3 = 0;
    result = MiReturnCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12021871) + a1 * 8), result + 1, a3, 2);
    goto loc_002B8DB8;
loc_002B9196:
    a3 = 0;
    result = MiWriteValidPteVolatile(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12021871) + a1 * 8), a3 + 1, a3, 2);
    goto loc_002B8E25;
loc_002B91AA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) == result) goto loc_002B91F3;
loc_002B91BA:
    result = MiUnlockPage(*(unsigned __int64 *)(v_stack_m28 + 64), 17, a3, 2);
    goto loc_002B8CFB;
loc_002B91CB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13687015)))) & (64)) == 0) goto loc_002B9152;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_stack_m28 + 64), 17, a3, 2);
    if ((unsigned __int8)(result) == 0) goto loc_002B9152;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r13)), 17, a3, 2);
    goto loc_002B9154;
loc_002B91F3:
    v_stack_m60 = (unsigned int)((unsigned int)(v_r13));
    v_stack_m68 = result;
    *(unsigned __int64 *)((unsigned int)((unsigned int)(v_r13))) = v_stack_m68;
    *(unsigned __int64 *)(result + 8) = v_stack_m68;
    goto loc_002B9121;
loc_002B920F:
    if ((unsigned int)(result) != 0) goto loc_002B8DA1;
    goto loc_002B8DB8;
loc_002B921C:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    goto loc_002B8F51;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockProtoPoolPage(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint8_t v_stack_mA6;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (224);
    local_rbp = (v_stack_mA8) & (-64);
    if (Arg2 != 0) {
        *(uint8_t *)(Arg2) = 17;
    }
    Arg1 = (Arg1) >> (9);
    local_r14 = (local_r14) & (Arg1);
    local_r14 = (local_r14) + (local_r11);
    local_r13 = 0;
loc_002B8BE1:
loc_002B8BEB:
loc_002B8BFB:
loc_002B8C10:
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (1)) == 0) goto loc_002B8CFB;
    if (condition_is_below) goto loc_002B8CFB;
    local_rbx = (*(uint64_t *)(local_r14)) >> (12);
    local_rbx = (local_rbx) & (Arg2);
    if (local_rbx > (*(uint64_t *)(v_rip + 0xB750AB))) goto loc_002B8C10;
    Arg1 = (local_rbx + local_rbx * 2) + (local_rbx + local_rbx * 2);
    if (((local_rsi) & (*(uint64_t *)(local_r11 + Arg1 * 8))) == 0) goto loc_002B8C10;
    if (Arg2 == 0) goto loc_002B8E9C;
    if (local_rbx > (*(uint64_t *)(v_rip + 0xB75075))) goto loc_002B8FC1;
loc_002B8C71:
    if ((*(uint32_t *)(v_rip + 0xD0E0A0)) != 0) goto loc_002B8F8F;
loc_002B8C86:
    if (((local_rsi) & (*(uint64_t *)(a3 + Arg1 * 8 + 0x28))) == 0) goto loc_002B9043;
loc_002B8C93:
loc_002B8C96:
    if (condition_is_below) goto loc_002B8ED0;
    if (((uint8_t)(v_cr8)) == 17) goto loc_002B8C10;
loc_002B8CDB:
    if ((((uint8_t)(*(uint64_t *)(local_r14))) & (1)) != 0) goto loc_002B8D1F;
loc_002B8CE2:
    if (((uint8_t)(v_cr8)) != 17) goto loc_002B91BA;
loc_002B8CFB:
    result = 0;
loc_002B8CFD:
    return result;
loc_002B8D1F:
    if (condition_is_below) goto loc_002B8CE2;
    result = (result) >> (12);
    result = (result) & (Arg2);
    if ((*(uint64_t *)(v_stack_m28 + 0x30)) != result) goto loc_002B8E32;
    if ((*(uint64_t *)(v_stack_m28 + 0x30)) < result) goto loc_002B8DA1;
    if ((*(uint64_t *)(v_stack_m28 + 0x30)) < result) goto loc_002B8DA1;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x18)) & (Arg1);
    if ((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20))) == 0) goto loc_002B8EEF;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)))) != 1) goto loc_002B8F9F;
    if (result == 0) goto loc_002B9076;
loc_002B8D94:
loc_002B8D99:
    if (1 != 0) goto loc_002B8EEF;
loc_002B8DA1:
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)));
    result = (uint16_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20))) + 1);
    v_stack_mA8 = (uint16_t)(result);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20) = (uint32_t)((uint32_t)(v_stack_mA8));
loc_002B8DB8:
    if (((uint8_t)(v_cr8)) != 17) {
        *(uint8_t *)(Arg2) = (uint8_t)(v_cr8);
    }
    local_rbx = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8)) | ((uint32_t)(v_stack_mA8));
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x22)) & (32)) != 0) goto loc_002B90D3;
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20))) >> (16));
    result = (uint8_t)((result) | (32));
    v_stack_mA6 = (uint8_t)(result);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20) = (uint32_t)((uint32_t)(v_stack_mA8));
loc_002B8E0D:
    if (condition_is_below) goto loc_002B8E25;
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (32)) == 0) goto loc_002B9196;
loc_002B8E25:
    goto loc_002B8CFD;
loc_002B8E32:
    if (((uint8_t)(v_cr8)) > 1) goto loc_002B8C10;
    result = *(uint64_t *)(v_stack_m28 + 0x40);
    if ((*(uint32_t *)(v_rip + 0xD0DEAA)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(local_rbx), 2);
    }
    goto loc_002B8BEB;
loc_002B8E9C:
loc_002B8EA2:
    if ((*(uint32_t *)(v_rip + 0xD0DEAA)) >= 0) goto loc_002B8CDB;
loc_002B8EAF:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD0C3F5)) & ((uint32_t)(local_rsi))) == 0) goto loc_002B90AC;
loc_002B8EBD:
loc_002B8EBF:
    if (!sign_flag) goto loc_002B8EA2;
    goto loc_002B8EAF;
loc_002B8ED0:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xD0C3D4)) & ((uint32_t)(local_rsi))) == 0) goto loc_002B9085;
loc_002B8EDE:
loc_002B8EE0:
    if (!sign_flag) goto loc_002B8C96;
    goto loc_002B8ED0;
loc_002B8EEF:
    local_r14 = 0;
    if (sign_flag) goto loc_002B8FEF;
loc_002B8EFF:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8)) | (*(uint64_t *)(local_rbx));
    result = (v_stack_m28) + (Arg2);
    if (Arg1 > result) goto loc_002B8F38;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8)) | (*(uint64_t *)(local_rbx));
    if (Arg1 >= v_stack_m28) goto loc_002B8FFF;
loc_002B8F38:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
loc_002B8F51:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB77145) + Arg1 * 8)) != (v_rip + 12058024)) goto loc_002B915F;
loc_002B8F70:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)) - 1)) > -3) goto loc_002B915F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)) - 1)) == -3) goto loc_002B8DA1;
    goto loc_002B8F70;
loc_002B8F8F:
    result = KiRaiseIrqlProcessIrqlFlags(17, 2, *(uint64_t *)(local_rbx), 2);
    goto loc_002B8C86;
loc_002B8F9F:
    if (2 != 2) goto loc_002B8DA1;
    if (result == 0) goto loc_002B8DA1;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x22)) & (8)) != 0) goto loc_002B8EEF;
    goto loc_002B8DA1;
loc_002B8FC1:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB77145) + Arg1 * 8)) < (*(uint64_t *)(v_rip + 0xB7CC38))) goto loc_002B8BFB;
    result = (*(uint64_t *)(v_rip + 0xB7CC38)) + (0x800ULL);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB77145) + Arg1 * 8)) >= result) goto loc_002B8C10;
    goto loc_002B8C71;
loc_002B8FEF:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB77145) + Arg1 * 8)) >= result) goto loc_002B8EFF;
    goto loc_002B9009;
loc_002B8FFF:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x23)) & (32)) == 0) goto loc_002B921C;
loc_002B9009:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    result = MiChargeCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7706F) + Arg1 * 8), 1, 1 + 3, 2);
    if ((uint32_t)(result) == 0) goto loc_002B8DB8;
    goto loc_002B8F51;
loc_002B9043:
    result = MiIsDecayPfn(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7706F) + Arg1 * 8), 1, 1 + 3, 2);
    if ((uint32_t)(result) != 0) goto loc_002B8C93;
    if ((*(uint32_t *)(v_rip + 0xD0DCC6)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1 + 3, 2);
    }
    goto loc_002B8BE1;
loc_002B9076:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x22)) & (8)) == 0) goto loc_002B8D99;
    goto loc_002B8D94;
loc_002B9085:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0DA2D)))) & (64)) == 0) goto loc_002B8EDE;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, 1 + 3, 2);
    if ((uint8_t)(result) == 0) goto loc_002B8EDE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), Arg2, 1 + 3, 2);
    goto loc_002B8EE0;
loc_002B90AC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0DA06)))) & (64)) == 0) goto loc_002B8EBD;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), Arg2, 1 + 3, 2);
    if ((uint8_t)(result) == 0) goto loc_002B8EBD;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), Arg2, 1 + 3, 2);
    goto loc_002B8EBF;
loc_002B90D3:
    v_stack_m58 = 0;
    result = MiGetLeafPfnBuddy(*(uint64_t *)(v_stack_m28 + 0x40), 1, 1 + 3, 2);
    if (result != 0) goto loc_002B91AA;
    v_stack_m60 = v_stack_m68;
    Arg2 = (v_stack_m68) >> (3);
    v_stack_m68 = v_stack_m68;
    Arg1 = (Arg2) ^ (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)));
    Arg1 = (Arg1) & (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)));
    Arg1 = (Arg1) ^ (Arg2);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40)) = Arg1;
loc_002B9121:
    result = MiSpinForProtoPoolLock(v_stack_m68, Arg2, 1 + 3, 2);
loc_002B9139:
    if (condition_is_above_or_equal) goto loc_002B8E0D;
loc_002B9146:
    local_r13 = (uint32_t)((local_r13) + 1);
    if (((*(uint32_t *)(v_rip + 0xD0C15C)) & ((uint32_t)(local_r13))) == 0) goto loc_002B91CB;
loc_002B9152:
loc_002B9154:
    if (!sign_flag) goto loc_002B9139;
    goto loc_002B9146;
loc_002B915F:
    result = MiChargePartitionResidentAvailable(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7706F) + Arg1 * 8), 1, (uint32_t)(0xFFFFFFFFULL), 2);
    if ((uint32_t)(result) != 0) goto loc_002B8DA1;
    if (1 == 0) goto loc_002B920F;
    a3 = 0;
    result = MiReturnCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7706F) + Arg1 * 8), result + 1, a3, 2);
    goto loc_002B8DB8;
loc_002B9196:
    a3 = 0;
    result = MiWriteValidPteVolatile(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7706F) + Arg1 * 8), a3 + 1, a3, 2);
    goto loc_002B8E25;
loc_002B91AA:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) == result) goto loc_002B91F3;
loc_002B91BA:
    result = MiUnlockPage(*(uint64_t *)(v_stack_m28 + 0x40), 17, a3, 2);
    goto loc_002B8CFB;
loc_002B91CB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0D8E7)))) & (64)) == 0) goto loc_002B9152;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(v_stack_m28 + 0x40), 17, a3, 2);
    if ((uint8_t)(result) == 0) goto loc_002B9152;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r13)), 17, a3, 2);
    goto loc_002B9154;
loc_002B91F3:
    v_stack_m60 = (uint32_t)((uint32_t)(local_r13));
    v_stack_m68 = result;
    *(uint64_t *)((uint32_t)((uint32_t)(local_r13))) = v_stack_m68;
    *(uint64_t *)(result + 0x8) = v_stack_m68;
    goto loc_002B9121;
loc_002B920F:
    if ((uint32_t)(result) != 0) goto loc_002B8DA1;
    goto loc_002B8DB8;
loc_002B921C:
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    goto loc_002B8F51;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B8B80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
