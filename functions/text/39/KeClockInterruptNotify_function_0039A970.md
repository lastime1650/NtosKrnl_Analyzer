# KeClockInterruptNotify

- RVA: `0x0039A970`–`0x0039B309` (길이 `2,457` bytes)
- VA: `0x000000014039A970`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00081890`
- 디코드: `546`개 명령, `2,457/2,457` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **41**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **24**

### Outgoing calls
- `0x0039AAD5` → [KiSetNextClockTickDueTime](../23/KiSetNextClockTickDueTime_function_002363F0.md) (function, `0x002363F0`)
- `0x0039AAEA` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039AB1F` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x0039AB3A` → [PoExecuteIdleCheck](PoExecuteIdleCheck_function_0039CF20.md) (function, `0x0039CF20`)
- `0x0039AB67` → [KiRcuReportQuiescentState](../20/KiRcuReportQuiescentState_function_0020AB8C.md) (function, `0x0020AB8C`)
- `0x0039AB7B` → [KiRcuFlushCompleted](../20/KiRcuFlushCompleted_function_0020AD38.md) (function, `0x0020AD38`)
- `0x0039AC2A` → [KiUpdateTime](KiUpdateTime_function_0039B530.md) (function, `0x0039B530`)
- `0x0039AC66` → [KiSetNextClockTickDueTime](../23/KiSetNextClockTickDueTime_function_002363F0.md) (function, `0x002363F0`)
- `0x0039AC7B` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039AD1E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0039AD53` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0039AD62` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0039AD8A` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0039ADA4` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x0039ADB8` → [KiUpdateRunTime](KiUpdateRunTime_function_0039BB70.md) (function, `0x0039BB70`)
- `0x0039AE21` → [KiSetNextClockTickDueTime](../23/KiSetNextClockTickDueTime_function_002363F0.md) (function, `0x002363F0`)
- `0x0039AE36` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039AE53` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0039AE67` → [KiUpdateTimeAssist](KiUpdateTimeAssist_function_0039E230.md) (function, `0x0039E230`)
- `0x0039AE96` → [KiSetClockTimerKTimerDeadlines](../23/KiSetClockTimerKTimerDeadlines_function_0023671C.md) (function, `0x0023671C`)
- `0x0039AEAB` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039AF1B` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039AF38` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039AF49` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039AF5A` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039AF8A` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039AFAE` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0039AFB5` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0039B01E` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0039B0A4` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0039B103` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039B113` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039B13B` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0039B191` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0039B1B6` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0039B219` → [KiSrcuReportQuiescent](../5C/KiSrcuReportQuiescent_function_005C2C08.md) (function, `0x005C2C08`)
- `0x0039B22A` → [KiSrcuFlushCompleted](../5C/KiSrcuFlushCompleted_function_005C22B4.md) (function, `0x005C22B4`)
- `0x0039B279` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039B2AD` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039B2C3` → [KiRestoreClockTickRate](../4D/KiRestoreClockTickRate_function_004D2780.md) (function, `0x004D2780`)
- `0x0039B2E9` → [KiEventClockStateChange](../46/KiEventClockStateChange_function_0046279C.md) (function, `0x0046279C`)

### Direct callers
- [HalpTimerClockInterrupt](../20/HalpTimerClockInterrupt_function_002086A0.md) at `0x002087A3`
- [sub_00208C94](../20/Unknown_function_00208C94.md) at `0x00208C9F`
- [HalpTimerClockIpiRoutine](HalpTimerClockIpiRoutine_function_00399CC0.md) at `0x00399CDF`
- [HalpTimerAlwaysOnClockInterrupt](../56/HalpTimerAlwaysOnClockInterrupt_function_00560240.md) at `0x00560333`

### Static image references
- `0x0039A994` → RVA `0x00E0A740` (`.data`; read)
- `0x0039AA0F` → RVA `0x00FC6FF0` (`ALMOSTRO`; read)
- `0x0039AA30` → RVA `0x00F23140` (`.data`; read/write)
- `0x0039AA3E` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0039AA4C` → RVA `0x00F23140` (`.data`; read)
- `0x0039AA9B` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x0039AABB` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0039AB00` → RVA `0x00F21F78` (`.data`; read/write)
- `0x0039AB0C` → RVA `0x00F233CC` (`.data`; read)
- `0x0039AB48` → RVA `0x00F110C0` (`.data`; read)
- `0x0039ABD2` → RVA `0x00F223C8` (`.data`; read)
- `0x0039ABD8` → RVA `0x00F21FE0` (`.data`; read)
- `0x0039ABF1` → RVA `0x00F223C8` (`.data`; write)
- `0x0039AC11` → RVA `0x00F21FA8` (`.data`; read)
- `0x0039ACCF` → RVA `0x00FCF000` (`CACHEALI`; read)
- `0x0039ACE2` → RVA `0x00FC6B7C` (`ALMOSTRO`; read)
- `0x0039ACEF` → RVA `0x00F21F88` (`.data`; write)
- `0x0039AD45` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0039AD94` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x0039AEE7` → RVA `0x00F21FA8` (`.data`; write)
- `0x0039AEF1` → RVA `0x00F21F90` (`.data`; write)
- `0x0039AEFF` → RVA `0x00E070D8` (`.data`; read)
- `0x0039B24A` → RVA `0x00F210E8` (`.data`; read)
- `0x0039B2D4` → RVA `0x00FCF000` (`CACHEALI`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x0039AB31` → [sub_006E5A5E + 0x12](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)
  - `0x0039AB40` → [sub_006E5A5E + 0x12](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)
  - `0x0039AF06` → [sub_006E5A5E + 0x97](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)
  - `0x0039B0F8` → [sub_006E5A5E + 0x139](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)
  - `0x0039B109` → [sub_006E5A5E + 0x139](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)
  - `0x0039B1E5` → [sub_006E5A5E](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)
  - `0x0039B26B` → [sub_006E5A5E + 0xF4](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)
  - `0x0039B27F` → [sub_006E5A5E + 0xF4](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)
  - `0x0039B29F` → [sub_006E5A5E + 0x123](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)
  - `0x0039B2B3` → [sub_006E5A5E + 0x123](../6E/Unknown_function_006E5A5E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0039A970  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0039A975  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0039A97A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0039A97F  55                              push rbp
0039A980  41 54                           push r12
0039A982  41 55                           push r13
0039A984  41 56                           push r14
0039A986  41 57                           push r15
0039A988  48 8D 6C 24 C9                  lea rbp, [rsp - 0x37]
0039A98D  48 81 EC D0 00 00 00            sub rsp, 0xd0
0039A994  48 8B 05 A5 FD A6 00            mov rax, qword ptr [rip + 0xa6fda5]
0039A99B  48 33 C4                        xor rax, rsp
0039A99E  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0039A9A2  33 DB                           xor ebx, ebx
0039A9A4  44 89 45 AF                     mov dword ptr [rbp - 0x51], r8d
0039A9A8  48 89 5D C7                     mov qword ptr [rbp - 0x39], rbx
0039A9AC  45 32 FF                        xor r15b, r15b
0039A9AF  65 48 8B 3C 25 20 00 00 00      mov rdi, qword ptr gs:[0x20]
0039A9B8  4C 8B F1                        mov r14, rcx
0039A9BB  88 55 97                        mov byte ptr [rbp - 0x69], dl
0039A9BE  44 8B E3                        mov r12d, ebx
0039A9C1  48 89 5D B7                     mov qword ptr [rbp - 0x49], rbx
0039A9C5  48 89 5D D7                     mov qword ptr [rbp - 0x29], rbx
0039A9C9  80 7F 20 01                     cmp byte ptr [rdi + 0x20], 1
0039A9CD  4C 8D AF 80 95 00 00            lea r13, [rdi + 0x9580]
0039A9D4  4C 89 6D CF                     mov qword ptr [rbp - 0x31], r13
0039A9D8  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
0039A9DC  48 89 5D A7                     mov qword ptr [rbp - 0x59], rbx
0039A9E0  77 2D                           ja 0x14039aa0f
0039A9E2  48 39 9F F8 38 00 00            cmp qword ptr [rdi + 0x38f8], rbx
0039A9E9  0F 85 C6 05 00 00               jne 0x14039afb5
0039A9EF  38 9F E5 38 00 00               cmp byte ptr [rdi + 0x38e5], bl
0039A9F5  0F 85 9D 06 00 00               jne 0x14039b098
0039A9FB  48 8B 97 E8 38 00 00            mov rdx, qword ptr [rdi + 0x38e8]
0039AA02  48 3B 97 F0 38 00 00            cmp rdx, qword ptr [rdi + 0x38f0]
0039AA09  0F 85 36 01 00 00               jne 0x14039ab45
0039AA0F  39 1D DB C5 C2 00               cmp dword ptr [rip + 0xc2c5db], ebx
0039AA15  0F 85 6A 01 00 00               jne 0x14039ab85
0039AA1B  38 5F 21                        cmp byte ptr [rdi + 0x21], bl
0039AA1E  0F 84 61 01 00 00               je 0x14039ab85
0039AA24  FA                              cli
0039AA25  8B F3                           mov esi, ebx
0039AA27  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0039AA30  F0 48 0F BA 2D 06 87 B8 00 00   lock bts qword ptr [rip + 0xb88706], 0
0039AA3A  73 1E                           jae 0x14039aa5a
0039AA3C  FF C6                           inc esi
0039AA3E  85 35 68 A8 C2 00               test dword ptr [rip + 0xc2a868], esi
0039AA44  0F 84 FB 02 00 00               je 0x14039ad45
0039AA4A  F3 90                           pause
0039AA4C  48 8B 05 ED 86 B8 00            mov rax, qword ptr [rip + 0xb886ed]
0039AA53  48 85 C0                        test rax, rax
0039AA56  74 D8                           je 0x14039aa30
0039AA58  EB E2                           jmp 0x14039aa3c
0039AA5A  39 1D 90 C5 C2 00               cmp dword ptr [rip + 0xc2c590], ebx
0039AA60  0F 84 A6 00 00 00               je 0x14039ab0c
0039AA66  F0 48 21 1D D2 86 B8 00         lock and qword ptr [rip + 0xb886d2], rbx
0039AA6E  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0039AA77  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0039AA7E  4D 85 C0                        test r8, r8
0039AA81  0F 85 E5 02 00 00               jne 0x14039ad6c
0039AA87  FB                              sti
0039AA88  45 84 FF                        test r15b, r15b
0039AA8B  0F 84 F4 00 00 00               je 0x14039ab85
0039AA91  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
0039AA95  41 BE 0F 00 00 00               mov r14d, 0xf
0039AA9B  80 3D E3 BF C2 00 00            cmp byte ptr [rip + 0xc2bfe3], 0
0039AAA2  0F 84 34 06 00 00               je 0x14039b0dc
0039AAA8  41 83 7D 10 01                  cmp dword ptr [r13 + 0x10], 1
0039AAAD  0F 85 29 06 00 00               jne 0x14039b0dc
0039AAB3  44 0F 20 C3                     mov rbx, cr8
0039AAB7  45 0F 22 C6                     mov cr8, r14
0039AABB  83 3D 5E C2 C2 00 00            cmp dword ptr [rip + 0xc2c25e], 0
0039AAC2  0F 85 46 06 00 00               jne 0x14039b10e
0039AAC8  B2 01                           mov dl, 1
0039AACA  41 C7 45 10 02 00 00 00         mov dword ptr [r13 + 0x10], 2
0039AAD2  48 8B CE                        mov rcx, rsi
0039AAD5  E8 16 B9 E9 FF                  call 0x1402363f0
0039AADA  83 3D 3F C2 C2 00 00            cmp dword ptr [rip + 0xc2c23f], 0
0039AAE1  74 0C                           je 0x14039aaef
0039AAE3  44 0F 20 C1                     mov rcx, cr8
0039AAE7  0F B6 D3                        movzx edx, bl
0039AAEA  E8 A9 AB 15 00                  call 0x1404f5698
0039AAEF  0F B6 C3                        movzx eax, bl
0039AAF2  44 0F 22 C0                     mov cr8, rax
0039AAF6  4D 85 E4                        test r12, r12
0039AAF9  74 05                           je 0x14039ab00
0039AAFB  41 C6 04 24 01                  mov byte ptr [r12], 1
0039AB00  48 FF 05 71 74 B8 00            inc qword ptr [rip + 0xb87471]
0039AB07  E9 0B 02 00 00                  jmp 0x14039ad17
0039AB0C  8B 05 BA 88 B8 00               mov eax, dword ptr [rip + 0xb888ba]
0039AB12  83 F8 04                        cmp eax, 4
0039AB15  0F 85 4B FF FF FF               jne 0x14039aa66
0039AB1B  48 8D 4D B7                     lea rcx, [rbp - 0x49]
0039AB1F  E8 9C F9 E6 FF                  call 0x14020a4c0
0039AB24  38 1D 5B BF C2 00               cmp byte ptr [rip + 0xc2bf5b], bl
0039AB2A  48 8B F0                        mov rsi, rax
0039AB2D  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
0039AB31  0F 85 39 AF 34 00               jne 0x1406e5a70
0039AB37  48 8B C8                        mov rcx, rax
0039AB3A  E8 E1 23 00 00                  call 0x14039cf20
0039AB3F  90                              nop
0039AB40  E9 2B AF 34 00                  jmp 0x1406e5a70
0039AB45  8B 4F 24                        mov ecx, dword ptr [rdi + 0x24]
0039AB48  48 8D 05 71 65 B7 00            lea rax, [rip + 0xb76571]
0039AB4F  48 C1 E1 05                     shl rcx, 5
0039AB53  48 03 C8                        add rcx, rax
0039AB56  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0039AB5A  4C 8B 01                        mov r8, qword ptr [rcx]
0039AB5D  4C 85 40 38                     test qword ptr [rax + 0x38], r8
0039AB61  0F 85 A8 FE FF FF               jne 0x14039aa0f
0039AB67  E8 20 00 E7 FF                  call 0x14020ab8c
0039AB6C  85 C0                           test eax, eax
0039AB6E  0F 84 9B FE FF FF               je 0x14039aa0f
0039AB74  0F B6 8F E6 38 00 00            movzx ecx, byte ptr [rdi + 0x38e6]
0039AB7B  E8 B8 01 E7 FF                  call 0x14020ad38
0039AB80  E9 8A FE FF FF                  jmp 0x14039aa0f
0039AB85  41 8B 8D 8C 00 00 00            mov ecx, dword ptr [r13 + 0x8c]
0039AB8C  4D 8D A5 98 00 00 00            lea r12, [r13 + 0x98]
0039AB93  48 8D 04 89                     lea rax, [rcx + rcx*4]
0039AB97  4D 8D 24 C4                     lea r12, [r12 + rax*8]
0039AB9B  8D 41 01                        lea eax, [rcx + 1]
0039AB9E  83 E0 0F                        and eax, 0xf
0039ABA1  41 89 85 8C 00 00 00            mov dword ptr [r13 + 0x8c], eax
0039ABA8  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
0039ABB2  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
0039ABB7  45 0F B6 AE 70 01 00 00         movzx r13d, byte ptr [r14 + 0x170]
0039ABBF  41 BE 0F 00 00 00               mov r14d, 0xf
0039ABC5  41 80 E5 01                     and r13b, 1
0039ABC9  38 5F 21                        cmp byte ptr [rdi + 0x21], bl
0039ABCC  0F 84 C2 01 00 00               je 0x14039ad94
0039ABD2  8B 15 F0 77 B8 00               mov edx, dword ptr [rip + 0xb877f0]
0039ABD8  48 8D 05 01 74 B8 00            lea rax, [rip + 0xb87401]
0039ABDF  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
0039ABE3  48 8D 34 C8                     lea rsi, [rax + rcx*8]
0039ABE7  8D 42 01                        lea eax, [rdx + 1]
0039ABEA  48 89 75 DF                     mov qword ptr [rbp - 0x21], rsi
0039ABEE  41 23 C6                        and eax, r14d
0039ABF1  89 05 D1 77 B8 00               mov dword ptr [rip + 0xb877d1], eax
0039ABF7  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
0039AC01  38 1D 7E BE C2 00               cmp byte ptr [rip + 0xc2be7e], bl
0039AC07  48 89 46 08                     mov qword ptr [rsi + 8], rax
0039AC0B  0F 85 AB 02 00 00               jne 0x14039aebc
0039AC11  83 3D 90 73 B8 00 01            cmp dword ptr [rip + 0xb87390], 1
0039AC18  0F 84 3F 06 00 00               je 0x14039b25d
0039AC1E  44 8B 45 AF                     mov r8d, dword ptr [rbp - 0x51]
0039AC22  41 0F B6 CD                     movzx ecx, r13b
0039AC26  0F B6 55 97                     movzx edx, byte ptr [rbp - 0x69]
0039AC2A  E8 01 09 00 00                  call 0x14039b530
0039AC2F  49 BD 08 00 00 00 80 F7 FF FF   movabs r13, 0xfffff78000000008
0039AC39  4D 8B 6D 00                     mov r13, qword ptr [r13]
0039AC3D  38 1D 42 BE C2 00               cmp byte ptr [rip + 0xc2be42], bl
0039AC43  4C 89 6D A7                     mov qword ptr [rbp - 0x59], r13
0039AC47  0F 84 37 06 00 00               je 0x14039b284
0039AC4D  44 0F 20 C7                     mov rdi, cr8
0039AC51  45 0F 22 C6                     mov cr8, r14
0039AC55  39 1D C5 C0 C2 00               cmp dword ptr [rip + 0xc2c0c5], ebx
0039AC5B  0F 85 CF 02 00 00               jne 0x14039af30
0039AC61  B2 01                           mov dl, 1
0039AC63  49 8B CD                        mov rcx, r13
0039AC66  E8 85 B7 E9 FF                  call 0x1402363f0
0039AC6B  39 1D AF C0 C2 00               cmp dword ptr [rip + 0xc2c0af], ebx
0039AC71  74 0D                           je 0x14039ac80
0039AC73  40 0F B6 D7                     movzx edx, dil
0039AC77  44 0F 20 C1                     mov rcx, cr8
0039AC7B  E8 18 AA 15 00                  call 0x1404f5698
0039AC80  40 0F B6 C7                     movzx eax, dil
0039AC84  44 0F 22 C0                     mov cr8, rax
0039AC88  48 A1 50 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000350]
0039AC92  48 89 06                        mov qword ptr [rsi], rax
0039AC95  48 A1 50 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000350]
0039AC9F  49 89 04 24                     mov qword ptr [r12], rax
0039ACA3  0F 31                           rdtsc
0039ACA5  48 C1 E2 20                     shl rdx, 0x20
0039ACA9  48 0B C2                        or rax, rdx
0039ACAC  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
0039ACB0  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0039ACB8  89 46 20                        mov dword ptr [rsi + 0x20], eax
0039ACBB  0F 31                           rdtsc
0039ACBD  48 C1 E2 20                     shl rdx, 0x20
0039ACC1  48 0B C2                        or rax, rdx
0039ACC4  41 C6 44 24 20 01               mov byte ptr [r12 + 0x20], 1
0039ACCA  49 89 44 24 18                  mov qword ptr [r12 + 0x18], rax
0039ACCF  8B 05 2B 43 C3 00               mov eax, dword ptr [rip + 0xc3432b]
0039ACD5  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
0039ACD9  83 F8 02                        cmp eax, 2
0039ACDC  0F 84 D6 05 00 00               je 0x14039b2b8
0039ACE2  8B 05 94 BE C2 00               mov eax, dword ptr [rip + 0xc2be94]
0039ACE8  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
0039ACEC  48 03 C6                        add rax, rsi
0039ACEF  48 89 05 92 72 B8 00            mov qword ptr [rip + 0xb87292], rax
0039ACF6  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
0039ACFA  48 03 C6                        add rax, rsi
0039ACFD  49 89 45 00                     mov qword ptr [r13], rax
0039AD01  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
0039AD05  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0039AD09  49 89 74 24 10                  mov qword ptr [r12 + 0x10], rsi
0039AD0E  45 84 FF                        test r15b, r15b
0039AD11  0F 85 E9 05 00 00               jne 0x14039b300
0039AD17  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
0039AD1B  48 33 CC                        xor rcx, rsp
0039AD1E  E8 1D 19 31 00                  call 0x1406ac640
0039AD23  4C 8D 9C 24 D0 00 00 00         lea r11, [rsp + 0xd0]
0039AD2B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0039AD2F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0039AD33  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0039AD37  49 8B E3                        mov rsp, r11
0039AD3A  41 5F                           pop r15
0039AD3C  41 5E                           pop r14
0039AD3E  41 5D                           pop r13
0039AD40  41 5C                           pop r12
0039AD42  5D                              pop rbp
0039AD43  C3                              ret
0039AD44  CC                              int3
0039AD45  8B 05 6D BD C2 00               mov eax, dword ptr [rip + 0xc2bd6d]
0039AD4B  A8 40                           test al, 0x40
0039AD4D  0F 84 F7 FC FF FF               je 0x14039aa4a
0039AD53  E8 38 47 F7 FF                  call 0x14030f490
0039AD58  84 C0                           test al, al
0039AD5A  0F 84 EA FC FF FF               je 0x14039aa4a
0039AD60  8B CE                           mov ecx, esi
0039AD62  E8 F9 46 F7 FF                  call 0x14030f460
0039AD67  E9 E0 FC FF FF                  jmp 0x14039aa4c
0039AD6C  41 0F 0D 08                     prefetchw byte ptr [r8]
0039AD70  41 8B 00                        mov eax, dword ptr [r8]
0039AD73  8B D0                           mov edx, eax
0039AD75  0F BA F2 15                     btr edx, 0x15
0039AD79  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0039AD7E  75 F3                           jne 0x14039ad73
0039AD80  0F BA E0 15                     bt eax, 0x15
0039AD84  0F 83 FD FC FF FF               jae 0x14039aa87
0039AD8A  E8 41 84 EC FF                  call 0x1402631d0
0039AD8F  E9 F3 FC FF FF                  jmp 0x14039aa87
0039AD94  39 1D 96 A2 C2 00               cmp dword ptr [rip + 0xc2a296], ebx
0039AD9A  0F 84 A7 00 00 00               je 0x14039ae47
0039ADA0  48 8D 4D B7                     lea rcx, [rbp - 0x49]
0039ADA4  E8 17 F7 E6 FF                  call 0x14020a4c0
0039ADA9  48 8B F0                        mov rsi, rax
0039ADAC  44 8B 45 AF                     mov r8d, dword ptr [rbp - 0x51]
0039ADB0  41 0F B6 CD                     movzx ecx, r13b
0039ADB4  0F B6 55 97                     movzx edx, byte ptr [rbp - 0x69]
0039ADB8  E8 B3 0D 00 00                  call 0x14039bb70
0039ADBD  49 89 74 24 10                  mov qword ptr [r12 + 0x10], rsi
0039ADC2  48 A1 50 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000350]
0039ADCC  49 89 04 24                     mov qword ptr [r12], rax
0039ADD0  0F 31                           rdtsc
0039ADD2  48 C1 E2 20                     shl rdx, 0x20
0039ADD6  48 0B C2                        or rax, rdx
0039ADD9  41 C6 44 24 20 00               mov byte ptr [r12 + 0x20], 0
0039ADDF  80 3D 9F BC C2 00 00            cmp byte ptr [rip + 0xc2bc9f], 0
0039ADE6  49 89 44 24 18                  mov qword ptr [r12 + 0x18], rax
0039ADEB  0F 84 06 05 00 00               je 0x14039b2f7
0039ADF1  44 0F 20 C3                     mov rbx, cr8
0039ADF5  45 0F 22 C6                     mov cr8, r14
0039ADF9  83 3D 20 BF C2 00 00            cmp dword ptr [rip + 0xc2bf20], 0
0039AE00  0F 85 3C 01 00 00               jne 0x14039af42
0039AE06  4C 8D AF 80 95 00 00            lea r13, [rdi + 0x9580]
0039AE0D  41 83 7D 10 01                  cmp dword ptr [r13 + 0x10], 1
0039AE12  75 08                           jne 0x14039ae1c
0039AE14  41 C7 45 10 02 00 00 00         mov dword ptr [r13 + 0x10], 2
0039AE1C  B2 01                           mov dl, 1
0039AE1E  48 8B CE                        mov rcx, rsi
0039AE21  E8 CA B5 E9 FF                  call 0x1402363f0
0039AE26  83 3D F3 BE C2 00 00            cmp dword ptr [rip + 0xc2bef3], 0
0039AE2D  74 0C                           je 0x14039ae3b
0039AE2F  44 0F 20 C1                     mov rcx, cr8
0039AE33  0F B6 D3                        movzx edx, bl
0039AE36  E8 5D A8 15 00                  call 0x1404f5698
0039AE3B  0F B6 C3                        movzx eax, bl
0039AE3E  44 0F 22 C0                     mov cr8, rax
0039AE42  E9 C7 FE FF FF                  jmp 0x14039ad0e
0039AE47  38 1D 38 BC C2 00               cmp byte ptr [rip + 0xc2bc38], bl
0039AE4D  0F 84 4D FF FF FF               je 0x14039ada0
0039AE53  E8 88 CD E7 FF                  call 0x140217be0
0039AE58  33 D2                           xor edx, edx
0039AE5A  4C 8D 4D B7                     lea r9, [rbp - 0x49]
0039AE5E  33 C9                           xor ecx, ecx
0039AE60  4C 8D 45 A7                     lea r8, [rbp - 0x59]
0039AE64  0F B6 D8                        movzx ebx, al
0039AE67  E8 C4 33 00 00                  call 0x14039e230
0039AE6C  84 DB                           test bl, bl
0039AE6E  0F 85 F4 00 00 00               jne 0x14039af68
0039AE74  44 0F 20 C3                     mov rbx, cr8
0039AE78  45 0F 22 C6                     mov cr8, r14
0039AE7C  83 3D 9D BE C2 00 00            cmp dword ptr [rip + 0xc2be9d], 0
0039AE83  0F 85 FA 00 00 00               jne 0x14039af83
0039AE89  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
0039AE8D  45 33 C0                        xor r8d, r8d
0039AE90  48 8B D6                        mov rdx, rsi
0039AE93  48 8B CF                        mov rcx, rdi
0039AE96  E8 81 B8 E9 FF                  call 0x14023671c
0039AE9B  83 3D 7E BE C2 00 00            cmp dword ptr [rip + 0xc2be7e], 0
0039AEA2  74 0C                           je 0x14039aeb0
0039AEA4  44 0F 20 C1                     mov rcx, cr8
0039AEA8  0F B6 D3                        movzx edx, bl
0039AEAB  E8 E8 A7 15 00                  call 0x1404f5698
0039AEB0  0F B6 C3                        movzx eax, bl
0039AEB3  44 0F 22 C0                     mov cr8, rax
0039AEB7  E9 F0 FE FF FF                  jmp 0x14039adac
0039AEBC  83 BF 90 95 00 00 01            cmp dword ptr [rdi + 0x9590], 1
0039AEC3  0F 85 55 FD FF FF               jne 0x14039ac1e
0039AEC9  44 0F 20 C0                     mov rax, cr8
0039AECD  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
0039AED1  45 0F 22 C6                     mov cr8, r14
0039AED5  39 1D 45 BE C2 00               cmp dword ptr [rip + 0xc2be45], ebx
0039AEDB  75 76                           jne 0x14039af53
0039AEDD  C7 87 90 95 00 00 02 00 00 00   mov dword ptr [rdi + 0x9590], 2
0039AEE7  C7 05 B7 70 B8 00 02 00 00 00   mov dword ptr [rip + 0xb870b7], 2
0039AEF1  48 89 1D 98 70 B8 00            mov qword ptr [rip + 0xb87098], rbx
0039AEF8  80 A7 C4 95 00 00 FE            and byte ptr [rdi + 0x95c4], 0xfe
0039AEFF  83 3D D2 C1 A6 00 05            cmp dword ptr [rip + 0xa6c1d2], 5
0039AF06  0F 87 E9 AB 34 00               ja 0x1406e5af5
0039AF0C  39 1D 0E BE C2 00               cmp dword ptr [rip + 0xc2be0e], ebx
0039AF12  74 10                           je 0x14039af24
0039AF14  44 0F 20 C1                     mov rcx, cr8
0039AF18  0F B6 D0                        movzx edx, al
0039AF1B  E8 78 A7 15 00                  call 0x1404f5698
0039AF20  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0039AF24  0F B6 C0                        movzx eax, al
0039AF27  44 0F 22 C0                     mov cr8, rax
0039AF2B  E9 EE FC FF FF                  jmp 0x14039ac1e
0039AF30  41 0F B6 D6                     movzx edx, r14b
0039AF34  40 0F B6 CF                     movzx ecx, dil
0039AF38  E8 BF A7 15 00                  call 0x1404f56fc
0039AF3D  E9 1F FD FF FF                  jmp 0x14039ac61
0039AF42  41 0F B6 D6                     movzx edx, r14b
0039AF46  0F B6 CB                        movzx ecx, bl
0039AF49  E8 AE A7 15 00                  call 0x1404f56fc
0039AF4E  E9 B3 FE FF FF                  jmp 0x14039ae06
0039AF53  41 0F B6 D6                     movzx edx, r14b
0039AF57  0F B6 C8                        movzx ecx, al
0039AF5A  E8 9D A7 15 00                  call 0x1404f56fc
0039AF5F  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0039AF63  E9 75 FF FF FF                  jmp 0x14039aedd
0039AF68  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0039AF71  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0039AF78  4D 85 C0                        test r8, r8
0039AF7B  75 17                           jne 0x14039af94
0039AF7D  FB                              sti
0039AF7E  E9 F1 FE FF FF                  jmp 0x14039ae74
0039AF83  41 0F B6 D6                     movzx edx, r14b
0039AF87  0F B6 CB                        movzx ecx, bl
0039AF8A  E8 6D A7 15 00                  call 0x1404f56fc
0039AF8F  E9 F5 FE FF FF                  jmp 0x14039ae89
0039AF94  41 0F 0D 08                     prefetchw byte ptr [r8]
0039AF98  41 8B 00                        mov eax, dword ptr [r8]
0039AF9B  8B D0                           mov edx, eax
0039AF9D  0F BA F2 15                     btr edx, 0x15
0039AFA1  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0039AFA6  75 F3                           jne 0x14039af9b
0039AFA8  0F BA E0 15                     bt eax, 0x15
0039AFAC  73 CF                           jae 0x14039af7d
0039AFAE  E8 1D 82 EC FF                  call 0x1402631d0
0039AFB3  EB C8                           jmp 0x14039af7d
0039AFB5  E8 26 CC E7 FF                  call 0x140217be0
0039AFBA  48 8B B7 F8 38 00 00            mov rsi, qword ptr [rdi + 0x38f8]
0039AFC1  44 0F B6 C0                     movzx r8d, al
0039AFC5  48 85 F6                        test rsi, rsi
0039AFC8  0F 84 F2 01 00 00               je 0x14039b1c0
0039AFCE  48 8B 06                        mov rax, qword ptr [rsi]
0039AFD1  48 39 5E F8                     cmp qword ptr [rsi - 8], rbx
0039AFD5  0F 85 0F 02 00 00               jne 0x14039b1ea
0039AFDB  48 3B C6                        cmp rax, rsi
0039AFDE  75 74                           jne 0x14039b054
0039AFE0  48 89 9F F8 38 00 00            mov qword ptr [rdi + 0x38f8], rbx
0039AFE7  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
0039AFEB  48 89 1E                        mov qword ptr [rsi], rbx
0039AFEE  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
0039AFF2  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
0039AFF6  45 84 C0                        test r8b, r8b
0039AFF9  75 7E                           jne 0x14039b079
0039AFFB  4C 8B 46 10                     mov r8, qword ptr [rsi + 0x10]
0039AFFF  4C 3B 46 18                     cmp r8, qword ptr [rsi + 0x18]
0039B003  0F 84 E6 F9 FF FF               je 0x14039a9ef
0039B009  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0039B00D  48 8B 56 20                     mov rdx, qword ptr [rsi + 0x20]
0039B011  48 8B 08                        mov rcx, qword ptr [rax]
0039B014  48 85 4A 28                     test qword ptr [rdx + 0x28], rcx
0039B018  0F 84 F4 01 00 00               je 0x14039b212
0039B01E  E8 BD CB E7 FF                  call 0x140217be0
0039B023  44 0F B6 C0                     movzx r8d, al
0039B027  48 39 1E                        cmp qword ptr [rsi], rbx
0039B02A  0F 85 23 01 00 00               jne 0x14039b153
0039B030  48 8B 8F F8 38 00 00            mov rcx, qword ptr [rdi + 0x38f8]
0039B037  48 85 C9                        test rcx, rcx
0039B03A  0F 84 BF 01 00 00               je 0x14039b1ff
0039B040  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0039B044  48 39 08                        cmp qword ptr [rax], rcx
0039B047  0F 84 F8 00 00 00               je 0x14039b145
0039B04D  B9 03 00 00 00                  mov ecx, 3
0039B052  CD 29                           int 0x29
0039B054  48 89 87 F8 38 00 00            mov qword ptr [rdi + 0x38f8], rax
0039B05B  48 8B 0E                        mov rcx, qword ptr [rsi]
0039B05E  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0039B062  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
0039B066  75 E5                           jne 0x14039b04d
0039B068  48 39 30                        cmp qword ptr [rax], rsi
0039B06B  75 E0                           jne 0x14039b04d
0039B06D  48 89 08                        mov qword ptr [rax], rcx
0039B070  48 89 41 08                     mov qword ptr [rcx + 8], rax
0039B074  E9 6E FF FF FF                  jmp 0x14039afe7
0039B079  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0039B082  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0039B089  4D 85 C0                        test r8, r8
0039B08C  0F 85 8B 00 00 00               jne 0x14039b11d
0039B092  FB                              sti
0039B093  E9 63 FF FF FF                  jmp 0x14039affb
0039B098  39 9F E0 38 00 00               cmp dword ptr [rdi + 0x38e0], ebx
0039B09E  0F 85 57 F9 FF FF               jne 0x14039a9fb
0039B0A4  E8 37 CB E7 FF                  call 0x140217be0
0039B0A9  38 9F E5 38 00 00               cmp byte ptr [rdi + 0x38e5], bl
0039B0AF  0F 85 7F 01 00 00               jne 0x14039b234
0039B0B5  84 C0                           test al, al
0039B0B7  0F 84 3E F9 FF FF               je 0x14039a9fb
0039B0BD  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0039B0C6  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0039B0CD  4D 85 C0                        test r8, r8
0039B0D0  0F 85 C2 00 00 00               jne 0x14039b198
0039B0D6  FB                              sti
0039B0D7  E9 1F F9 FF FF                  jmp 0x14039a9fb
0039B0DC  83 3D C5 6E B8 00 01            cmp dword ptr [rip + 0xb86ec5], 1
0039B0E3  0F 85 2E FC FF FF               jne 0x14039ad17
0039B0E9  44 0F 20 C3                     mov rbx, cr8
0039B0ED  45 0F 22 C6                     mov cr8, r14
0039B0F1  83 3D 28 BC C2 00 00            cmp dword ptr [rip + 0xc2bc28], 0
0039B0F8  0F 84 99 AA 34 00               je 0x1406e5b97
0039B0FE  B2 0F                           mov dl, 0xf
0039B100  0F B6 CB                        movzx ecx, bl
0039B103  E8 F4 A5 15 00                  call 0x1404f56fc
0039B108  90                              nop
0039B109  E9 89 AA 34 00                  jmp 0x1406e5b97
0039B10E  B2 0F                           mov dl, 0xf
0039B110  0F B6 CB                        movzx ecx, bl
0039B113  E8 E4 A5 15 00                  call 0x1404f56fc
0039B118  E9 AB F9 FF FF                  jmp 0x14039aac8
0039B11D  41 0F 0D 08                     prefetchw byte ptr [r8]
0039B121  41 8B 00                        mov eax, dword ptr [r8]
0039B124  8B D0                           mov edx, eax
0039B126  0F BA F2 15                     btr edx, 0x15
0039B12A  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0039B12F  75 F3                           jne 0x14039b124
0039B131  0F BA E0 15                     bt eax, 0x15
0039B135  0F 83 57 FF FF FF               jae 0x14039b092
0039B13B  E8 90 80 EC FF                  call 0x1402631d0
0039B140  E9 4D FF FF FF                  jmp 0x14039b092
0039B145  48 89 0E                        mov qword ptr [rsi], rcx
0039B148  48 89 46 08                     mov qword ptr [rsi + 8], rax
0039B14C  48 89 30                        mov qword ptr [rax], rsi
0039B14F  48 89 71 08                     mov qword ptr [rcx + 8], rsi
0039B153  45 84 C0                        test r8b, r8b
0039B156  0F 84 93 F8 FF FF               je 0x14039a9ef
0039B15C  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0039B165  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0039B16C  4D 85 C0                        test r8, r8
0039B16F  75 06                           jne 0x14039b177
0039B171  FB                              sti
0039B172  E9 78 F8 FF FF                  jmp 0x14039a9ef
0039B177  41 0F 0D 08                     prefetchw byte ptr [r8]
0039B17B  41 8B 00                        mov eax, dword ptr [r8]
0039B17E  8B D0                           mov edx, eax
0039B180  0F BA F2 15                     btr edx, 0x15
0039B184  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0039B189  75 F3                           jne 0x14039b17e
0039B18B  0F BA E0 15                     bt eax, 0x15
0039B18F  73 E0                           jae 0x14039b171
0039B191  E8 3A 80 EC FF                  call 0x1402631d0
0039B196  EB D9                           jmp 0x14039b171
0039B198  41 0F 0D 08                     prefetchw byte ptr [r8]
0039B19C  41 8B 00                        mov eax, dword ptr [r8]
0039B19F  8B D0                           mov edx, eax
0039B1A1  0F BA F2 15                     btr edx, 0x15
0039B1A5  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0039B1AA  75 F3                           jne 0x14039b19f
0039B1AC  0F BA E0 15                     bt eax, 0x15
0039B1B0  0F 83 20 FF FF FF               jae 0x14039b0d6
0039B1B6  E8 15 80 EC FF                  call 0x1402631d0
0039B1BB  E9 16 FF FF FF                  jmp 0x14039b0d6
0039B1C0  45 84 C0                        test r8b, r8b
0039B1C3  0F 84 26 F8 FF FF               je 0x14039a9ef
0039B1C9  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0039B1D2  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0039B1D9  4D 85 C0                        test r8, r8
0039B1DC  74 93                           je 0x14039b171
0039B1DE  41 0F 0D 08                     prefetchw byte ptr [r8]
0039B1E2  41 8B 00                        mov eax, dword ptr [r8]
0039B1E5  E9 74 A8 34 00                  jmp 0x1406e5a5e
0039B1EA  48 3B F0                        cmp rsi, rax
0039B1ED  0F 84 03 FE FF FF               je 0x14039aff6
0039B1F3  48 89 87 F8 38 00 00            mov qword ptr [rdi + 0x38f8], rax
0039B1FA  E9 F7 FD FF FF                  jmp 0x14039aff6
0039B1FF  48 89 76 08                     mov qword ptr [rsi + 8], rsi
0039B203  48 89 36                        mov qword ptr [rsi], rsi
0039B206  48 89 B7 F8 38 00 00            mov qword ptr [rdi + 0x38f8], rsi
0039B20D  E9 41 FF FF FF                  jmp 0x14039b153
0039B212  49 8B D0                        mov rdx, r8
0039B215  48 8D 4E F8                     lea rcx, [rsi - 8]
0039B219  E8 EA 79 22 00                  call 0x1405c2c08
0039B21E  85 C0                           test eax, eax
0039B220  0F 84 C9 F7 FF FF               je 0x14039a9ef
0039B226  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
0039B22A  E8 85 70 22 00                  call 0x1405c22b4
0039B22F  E9 BB F7 FF FF                  jmp 0x14039a9ef
0039B234  39 9F E0 38 00 00               cmp dword ptr [rdi + 0x38e0], ebx
0039B23A  0F 85 75 FE FF FF               jne 0x14039b0b5
0039B240  88 9F E5 38 00 00               mov byte ptr [rdi + 0x38e5], bl
0039B246  F0 09 1C 24                     lock or dword ptr [rsp], ebx
0039B24A  48 8B 0D 97 5E B8 00            mov rcx, qword ptr [rip + 0xb85e97]
0039B251  48 89 8F E8 38 00 00            mov qword ptr [rdi + 0x38e8], rcx
0039B258  E9 58 FE FF FF                  jmp 0x14039b0b5
0039B25D  44 0F 20 C7                     mov rdi, cr8
0039B261  45 0F 22 C6                     mov cr8, r14
0039B265  39 1D B5 BA C2 00               cmp dword ptr [rip + 0xc2bab5], ebx
0039B26B  0F 84 E1 A8 34 00               je 0x1406e5b52
0039B271  41 0F B6 D6                     movzx edx, r14b
0039B275  40 0F B6 CF                     movzx ecx, dil
0039B279  E8 7E A4 15 00                  call 0x1404f56fc
0039B27E  90                              nop
0039B27F  E9 CE A8 34 00                  jmp 0x1406e5b52
0039B284  83 3D 1D 6D B8 00 02            cmp dword ptr [rip + 0xb86d1d], 2
0039B28B  0F 85 F7 F9 FF FF               jne 0x14039ac88
0039B291  44 0F 20 C7                     mov rdi, cr8
0039B295  45 0F 22 C6                     mov cr8, r14
0039B299  39 1D 81 BA C2 00               cmp dword ptr [rip + 0xc2ba81], ebx
0039B29F  0F 84 DC A8 34 00               je 0x1406e5b81
0039B2A5  41 0F B6 D6                     movzx edx, r14b
0039B2A9  40 0F B6 CF                     movzx ecx, dil
0039B2AD  E8 4A A4 15 00                  call 0x1404f56fc
0039B2B2  90                              nop
0039B2B3  E9 C9 A8 34 00                  jmp 0x1406e5b81
0039B2B8  4C 8D 45 C7                     lea r8, [rbp - 0x39]
0039B2BC  48 8B CE                        mov rcx, rsi
0039B2BF  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0039B2C3  E8 B8 74 13 00                  call 0x1404d2780
0039B2C8  38 1D B7 B7 C2 00               cmp byte ptr [rip + 0xc2b7b7], bl
0039B2CE  0F 85 0E FA FF FF               jne 0x14039ace2
0039B2D4  87 1D 26 3D C3 00               xchg dword ptr [rip + 0xc33d26], ebx
0039B2DA  4C 8D 4D BF                     lea r9, [rbp - 0x41]
0039B2DE  BA 02 00 00 00                  mov edx, 2
0039B2E3  4C 8D 45 C7                     lea r8, [rbp - 0x39]
0039B2E7  33 C9                           xor ecx, ecx
0039B2E9  E8 AE 74 0C 00                  call 0x14046279c
0039B2EE  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
0039B2F2  E9 EB F9 FF FF                  jmp 0x14039ace2
0039B2F7  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
0039B2FB  E9 0E FA FF FF                  jmp 0x14039ad0e
0039B300  4C 8B 65 D7                     mov r12, qword ptr [rbp - 0x29]
0039B304  E9 92 F7 FF FF                  jmp 0x14039aa9b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeClockInterruptNotify(__int64 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 10943909)) ^ (v_rsp);
    v_stack_m38 = result;
    v_rbx = 0;
    v_stack_mB0 = a3;
    v_stack_m98 = 0;
    v_r15 = 0;
    v_stack_mC8 = a2;
    v_stack_mA8 = 0;
    v_stack_m88 = 0;
    v_stack_m90 = *(unsigned __int64 *)(gs_base + (0 + 32)) + 38272;
    v_stack_mA0 = 0;
    v_stack_mB8 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) > 1) goto loc_0039AA0F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14584)) != 0) goto loc_0039AFB5;
loc_0039A9EF:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14565)) != 0) goto loc_0039B098;
loc_0039A9FB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14568)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14576))) goto loc_0039AB45;
loc_0039AA0F:
    if ((*(unsigned int *)(v_rip + 12764635)) != 0) goto loc_0039AB85;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) == 0) goto loc_0039AB85;
loc_0039AA30:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) >= 0) goto loc_0039AA5A;
loc_0039AA3C:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 12757096)) & ((unsigned int)(v_rsi))) == 0) goto loc_0039AD45;
loc_0039AA4A:
loc_0039AA4C:
    if (*(unsigned __int64 *)(v_rip + 12093165) == 0) goto loc_0039AA30;
    goto loc_0039AA3C;
loc_0039AA5A:
    if ((*(unsigned int *)(v_rip + 12764560)) == 0) goto loc_0039AB0C;
loc_0039AA66:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039AD6C;
loc_0039AA87:
    if (0 == 0) goto loc_0039AB85;
loc_0039AA9B:
    if ((*(unsigned __int8 *)(v_rip + 12763107)) == 0) goto loc_0039B0DC;
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 16)) != 1) goto loc_0039B0DC;
    if ((*(unsigned int *)(v_rip + 12763742)) != 0) goto loc_0039B10E;
loc_0039AAC8:
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 16) = 2;
    result = KiSetNextClockTickDueTime(v_stack_mB8, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    if ((*(unsigned int *)(v_rip + 12763711)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
    if (0 != 0) {
        *(unsigned __int8 *)(0) = 1;
    }
    goto loc_0039AD17;
loc_0039AB0C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12093626)))) != 4) goto loc_0039AA66;
    result = RtlGetInterruptTimePrecise(v_stack_mA8, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    v_stack_mB8 = result;
    result = PoExecuteIdleCheck(result, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_0039AB45:
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36))) << (5);
    a1 = (a1) + (v_rip + 12019057);
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 56)) & (*(unsigned __int64 *)(a1))) != 0) goto loc_0039AA0F;
    result = KiRcuReportQuiescentState(a1, a2, *(unsigned __int64 *)(a1), a4);
    if ((unsigned int)(result) == 0) goto loc_0039AA0F;
    result = KiRcuFlushCompleted(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14566), a2, *(unsigned __int64 *)(a1), a4);
    goto loc_0039AA0F;
loc_0039AB85:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + 1) & (15));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 152 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) * 4 * 8 + 8) = result;
    v_r13 = (unsigned __int8)((*(unsigned __int8 *)(15 + 368)) & (1));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33)) == ((unsigned __int8)(v_cr8))) goto loc_0039AD94;
    v_stack_m80 = v_rip + 12088321 + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) * 4 * 8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12089328)) + 1) & (15));
    *(unsigned int *)(v_rip + 12089297) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rip + 12088321 + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) * 4 * 8 + 8) = result;
    if ((*(unsigned __int8 *)(v_rip + 12762750)) != ((unsigned __int8)(v_cr8))) goto loc_0039AEBC;
    if ((*(unsigned int *)(v_rip + 12088208)) == 1) goto loc_0039B25D;
loc_0039AC1E:
    result = KiUpdateTime((unsigned __int8)(v_r13), v_stack_mC8, (unsigned int)(v_stack_mB0), a4);
    v_stack_mB8 = *(unsigned __int64 *)(v_r13);
    if ((*(unsigned __int8 *)(v_rip + 12762690)) == ((unsigned __int8)(v_cr8))) goto loc_0039B284;
    if ((*(unsigned int *)(v_rip + 12763333)) != ((unsigned int)(v_cr8))) goto loc_0039AF30;
loc_0039AC61:
    result = KiSetNextClockTickDueTime(*(unsigned __int64 *)(v_r13), 1, (unsigned int)(v_stack_mB0), a4);
    if ((*(unsigned int *)(v_rip + 12763311)) != ((unsigned int)(v_cr8))) {
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        a1 = 15;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(v_stack_mB0), a4);
    }
loc_0039AC88:
    *(unsigned __int64 *)(v_rip + 12088321 + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) * 4 * 8) = (unsigned __int8)((unsigned __int8)(v_cr8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 152 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) * 4 * 8) = (unsigned __int8)((unsigned __int8)(v_cr8));
    a2 = (a2) << (32);
    result = ((unsigned __int8)((unsigned __int8)(v_cr8))) | (a2);
    *(unsigned __int64 *)(v_rip + 12088321 + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) * 4 * 8 + 24) = result;
    *(unsigned int *)(v_rip + 12088321 + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) + (unsigned int)(*(unsigned int *)(v_rip + 12089328)) * 4 * 8 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))));
    a2 = (a2) << (32);
    result = ((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) | (a2);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 152 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) * 4 * 8 + 32) = 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 152 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) * 4 * 8 + 24) = result;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12796715)))) == 2) goto loc_0039B2B8;
loc_0039ACE2:
    result = ((unsigned int)(*(unsigned int *)(v_rip + 12762772))) + (v_stack_mB8);
    *(unsigned __int64 *)(v_rip + 12087954) = result;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m90 + 8))) + (v_stack_mB8);
    *(unsigned __int64 *)(v_stack_m90) = result;
    *(unsigned __int64 *)(v_stack_m80 + 16) = v_stack_mB8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 152 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) * 4 * 8 + 16) = v_stack_mB8;
loc_0039AD0E:
    if (0 != 0) goto loc_0039B300;
loc_0039AD17:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(v_stack_mB0), a4);
    return result;
loc_0039AD45:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12762477)))) & (64)) == 0) goto loc_0039AA4A;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, (unsigned int)(v_stack_mB0), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0039AA4A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))), a2, (unsigned int)(v_stack_mB0), a4);
    goto loc_0039AA4C;
loc_0039AD6C:
loc_0039AD73:
    if ((unsigned __int8)(result) != 0) goto loc_0039AD73;
    if (condition_is_above_or_equal) goto loc_0039AA87;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mB0))))), (unsigned int)(v_stack_mB0), a4);
    goto loc_0039AA87;
loc_0039AD94:
    if ((*(unsigned int *)(v_rip + 12755606)) == ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48)))) goto loc_0039AE47;
loc_0039ADA0:
    result = RtlGetInterruptTimePrecise(v_stack_mA8, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mB0))))), (unsigned int)(v_stack_mB0), a4);
loc_0039ADAC:
    result = KiUpdateRunTime((unsigned __int8)(v_stack_m90), v_stack_mC8, (unsigned int)(v_stack_mB0), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 152 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) * 4 * 8 + 16) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 152 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) * 4 * 8) = result;
    a2 = (v_stack_mC8) << (32);
    result = (result) | (a2);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 152 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) * 4 * 8 + 32) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 152 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 38272 + 140)) * 4 * 8 + 24) = result;
    if ((*(unsigned __int8 *)(v_rip + 12762271)) == 0) goto loc_0039B2F7;
    if ((*(unsigned int *)(v_rip + 12762912)) != 0) goto loc_0039AF42;
loc_0039AE06:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 38272 + 16)) == 1) {
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 38272 + 16) = 2;
    }
    result = KiSetNextClockTickDueTime(result, 1, (unsigned int)(v_stack_mB0), a4);
    if ((*(unsigned int *)(v_rip + 12762867)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(v_stack_mB0), a4);
    }
    goto loc_0039AD0E;
loc_0039AE47:
    if ((*(unsigned __int8 *)(v_rip + 12762168)) == ((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))))) goto loc_0039ADA0;
    result = KeDisableInterrupts(a1, a2, (unsigned int)(v_stack_mB0), a4);
    a2 = 0;
    a1 = 0;
    result = KiUpdateTimeAssist(a1, a2, v_stack_mB8, v_stack_mA8);
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0039AF68;
loc_0039AE74:
    if ((*(unsigned int *)(v_rip + 12762781)) != 0) goto loc_0039AF83;
loc_0039AE89:
    a3 = 0;
    result = KiSetClockTimerKTimerDeadlines(*(unsigned __int64 *)(v_stack_m28 + 64), v_stack_mB8, a3, v_stack_mA8);
    if ((*(unsigned int *)(v_rip + 12762750)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, v_stack_mA8);
    }
    goto loc_0039ADAC;
loc_0039AEBC:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 38288)) != 1) goto loc_0039AC1E;
    v_stack_mC0 = (unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))));
    if ((*(unsigned int *)(v_rip + 12762693)) != ((unsigned int)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))))) goto loc_0039AF53;
loc_0039AEDD:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 38288) = 2;
    *(unsigned int *)(v_rip + 12087479) = 2;
    *(unsigned __int64 *)(v_rip + 12087448) = (unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)));
    result = (unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))));
    if ((*(unsigned int *)(v_rip + 12762638)) != ((unsigned int)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))))) {
        a1 = 15;
        a2 = (unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, v_stack_mA8);
        result = v_stack_mC0;
    }
    goto loc_0039AC1E;
loc_0039AF30:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)), 15, a3, v_stack_mA8);
    goto loc_0039AC61;
loc_0039AF42:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))), 15, a3, v_stack_mA8);
    goto loc_0039AE06;
loc_0039AF53:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), 15, a3, v_stack_mA8);
    goto loc_0039AEDD;
loc_0039AF68:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039AF94;
loc_0039AF7D:
    goto loc_0039AE74;
loc_0039AF83:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))), 15, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    goto loc_0039AE89;
loc_0039AF94:
loc_0039AF9B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039AF9B;
    if (condition_is_above_or_equal) goto loc_0039AF7D;
    result = KiRemoveSystemWorkPriorityKick((unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    goto loc_0039AF7D;
loc_0039AFB5:
    result = KeDisableInterrupts((unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) == 0) goto loc_0039B1C0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) - 8)) != ((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))))) goto loc_0039B1EA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584))) goto loc_0039B054;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) = (unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)));
loc_0039AFE7:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584)) = (unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 48) + 56);
loc_0039AFF6:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0039B079;
loc_0039AFFB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 16)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 24))) goto loc_0039A9EF;
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 32) + 40)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 40)))) == 0) goto loc_0039B212;
    result = KeDisableInterrupts(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 40)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 16), v_stack_mA8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584))) != ((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))))) goto loc_0039B153;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) == 0) goto loc_0039B1FF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 8))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584))) goto loc_0039B145;
loc_0039B04D:
loc_0039B054:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584))) goto loc_0039B04D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584))) goto loc_0039B04D;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 8);
    goto loc_0039AFE7;
loc_0039B079:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039B11D;
loc_0039B092:
    goto loc_0039AFFB;
loc_0039B098:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14560)) != ((unsigned int)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))))) goto loc_0039A9FB;
    result = KeDisableInterrupts(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14565)) != ((unsigned __int8)((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)))))) goto loc_0039B234;
loc_0039B0B5:
    if ((unsigned __int8)(result) == 0) goto loc_0039A9FB;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039B198;
loc_0039B0D6:
    goto loc_0039A9FB;
loc_0039B0DC:
    if ((*(unsigned int *)(v_rip + 12086981)) != 1) goto loc_0039AD17;
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(result)), 15, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
loc_0039B10E:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(result)), 15, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    goto loc_0039AAC8;
loc_0039B11D:
loc_0039B124:
    if ((*(unsigned int *)(v_rip + 12762152)) != 0) goto loc_0039B124;
    if ((*(unsigned int *)(v_rip + 12762152)) >= 0) goto loc_0039B092;
    result = KiRemoveSystemWorkPriorityKick((unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    goto loc_0039B092;
loc_0039B145:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584)) = (unsigned __int8)((unsigned __int8)(result));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 8) = result;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584);
    *(unsigned __int64 *)((unsigned __int8)((unsigned __int8)(result)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584);
loc_0039B153:
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)) == 0) goto loc_0039A9EF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039B177;
loc_0039B171:
    goto loc_0039A9EF;
loc_0039B177:
loc_0039B17E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039B17E;
    if (condition_is_above_or_equal) goto loc_0039B171;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    goto loc_0039B171;
loc_0039B198:
loc_0039B19F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039B19F;
    if (condition_is_above_or_equal) goto loc_0039B0D6;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    goto loc_0039B0D6;
loc_0039B1C0:
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)) == 0) goto loc_0039A9EF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) == 0) goto loc_0039B171;
loc_0039B1EA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584)) == ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))) goto loc_0039AFF6;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)));
    goto loc_0039AFF6;
loc_0039B1FF:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584);
    goto loc_0039B153;
loc_0039B212:
    result = KiSrcuReportQuiescent(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) - 8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    if ((unsigned int)(result) == 0) goto loc_0039A9EF;
    result = KiSrcuFlushCompleted(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584) + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
    goto loc_0039A9EF;
loc_0039B234:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14560)) != ((unsigned int)((unsigned __int8)(result)))) goto loc_0039B0B5;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14565) = (unsigned __int8)((unsigned __int8)(result));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14568) = *(unsigned __int64 *)(v_rip + 12082839);
    goto loc_0039B0B5;
loc_0039B25D:
    result = KiRaiseIrqlProcessIrqlFlags(15, 15, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
loc_0039B284:
    if ((*(unsigned int *)(v_rip + 12086557)) != 2) goto loc_0039AC88;
    result = KiRaiseIrqlProcessIrqlFlags(15, 15, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_stack_mA8);
loc_0039B2B8:
    result = KiRestoreClockTickRate(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 14584), v_stack_mA0, v_stack_m98, v_stack_mA8);
    if ((*(unsigned __int8 *)(v_rip + 12761015)) != ((unsigned __int8)((unsigned __int8)(result)))) goto loc_0039ACE2;
    a1 = 0;
    result = KiEventClockStateChange(a1, 2, v_stack_m98, v_stack_mA0);
    goto loc_0039ACE2;
loc_0039B2F7:
    goto loc_0039AD0E;
loc_0039B300:
    goto loc_0039AA9B;
}
```

## 5. (Beta) C Style

```c
int64_t KeClockInterruptNotify(void *Arg1, uint8_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0xA6FDA5)) ^ (local_rsp);
    v_stack_m38 = result;
    local_rbx = 0;
    v_stack_mB0 = Arg3;
    v_stack_m98 = 0;
    local_r15 = 0;
    v_stack_mC8 = Arg2;
    v_stack_mA8 = 0;
    v_stack_m88 = 0;
    v_stack_m90 = *(uint64_t *)(gs_base + (0 + 0x20)) + 38272;
    v_stack_mA0 = 0;
    v_stack_mB8 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) > 1) goto loc_0039AA0F;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38F8)) != 0) goto loc_0039AFB5;
loc_0039A9EF:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38E5)) != 0) goto loc_0039B098;
loc_0039A9FB:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38E8)) != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38F0))) goto loc_0039AB45;
loc_0039AA0F:
    if ((*(uint32_t *)(v_rip + 0xC2C5DB)) != 0) goto loc_0039AB85;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) == 0) goto loc_0039AB85;
loc_0039AA30:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) >= 0) goto loc_0039AA5A;
loc_0039AA3C:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xC2A868)) & ((uint32_t)(local_rsi))) == 0) goto loc_0039AD45;
loc_0039AA4A:
loc_0039AA4C:
    if (*(uint64_t *)(v_rip + 0xB886ED) == 0) goto loc_0039AA30;
    goto loc_0039AA3C;
loc_0039AA5A:
    if ((*(uint32_t *)(v_rip + 0xC2C590)) == 0) goto loc_0039AB0C;
loc_0039AA66:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039AD6C;
loc_0039AA87:
    if (0 == 0) goto loc_0039AB85;
loc_0039AA9B:
    if ((*(uint8_t *)(v_rip + 0xC2BFE3)) == 0) goto loc_0039B0DC;
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x10)) != 1) goto loc_0039B0DC;
    if ((*(uint32_t *)(v_rip + 0xC2C25E)) != 0) goto loc_0039B10E;
loc_0039AAC8:
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x10) = 2;
    result = KiSetNextClockTickDueTime(v_stack_mB8, 1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    if ((*(uint32_t *)(v_rip + 0xC2C23F)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    }
    if (0 != 0) {
        *(uint8_t *)(0) = 1;
    }
    goto loc_0039AD17;
loc_0039AB0C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB888BA)))) != 4) goto loc_0039AA66;
    result = RtlGetInterruptTimePrecise(v_stack_mA8, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    v_stack_mB8 = result;
    result = PoExecuteIdleCheck(result, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
loc_0039AB45:
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24))) << (5);
    Arg1 = (Arg1) + (v_rip + 12019057);
    if (((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x38)) & (*(uint64_t *)(arg1))) != 0) goto loc_0039AA0F;
    result = KiRcuReportQuiescentState(Arg1, Arg2, *(uint64_t *)(arg1), a4);
    if ((uint32_t)(result) == 0) goto loc_0039AA0F;
    result = KiRcuFlushCompleted(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38E6), Arg2, *(uint64_t *)(arg1), a4);
    goto loc_0039AA0F;
loc_0039AB85:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + 1) & (15));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x98 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) * 4 * 8 + 0x8) = result;
    local_r13 = (uint8_t)((*(uint8_t *)(15 + 0x170)) & (1));
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x21)) == ((uint8_t)(v_cr8))) goto loc_0039AD94;
    v_stack_m80 = v_rip + 12088321 + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) * 4 * 8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) + 1) & (15));
    *(uint32_t *)(v_rip + 0xB877D1) = (uint32_t)(result);
    *(uint64_t *)(v_rip + 0xB87401 + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) * 4 * 8 + 0x8) = result;
    if ((*(uint8_t *)(v_rip + 0xC2BE7E)) != ((uint8_t)(v_cr8))) goto loc_0039AEBC;
    if ((*(uint32_t *)(v_rip + 0xB87390)) == 1) goto loc_0039B25D;
loc_0039AC1E:
    result = KiUpdateTime((uint8_t)(local_r13), v_stack_mC8, (uint32_t)(v_stack_mB0), a4);
    v_stack_mB8 = *(uint64_t *)(local_r13);
    if ((*(uint8_t *)(v_rip + 0xC2BE42)) == ((uint8_t)(v_cr8))) goto loc_0039B284;
    if ((*(uint32_t *)(v_rip + 0xC2C0C5)) != ((uint32_t)(v_cr8))) goto loc_0039AF30;
loc_0039AC61:
    result = KiSetNextClockTickDueTime(*(uint64_t *)(local_r13), 1, (uint32_t)(v_stack_mB0), a4);
    if ((*(uint32_t *)(v_rip + 0xC2C0AF)) != ((uint32_t)(v_cr8))) {
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        Arg1 = 15;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(v_stack_mB0), a4);
    }
loc_0039AC88:
    *(uint64_t *)(v_rip + 0xB87401 + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) * 4 * 8) = (uint8_t)((uint8_t)(v_cr8));
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x98 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) * 4 * 8) = (uint8_t)((uint8_t)(v_cr8));
    Arg2 = (Arg2) << (32);
    result = ((uint8_t)((uint8_t)(v_cr8))) | (Arg2);
    *(uint64_t *)(v_rip + 0xB87401 + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) * 4 * 8 + 0x18) = result;
    *(uint32_t *)(v_rip + 0xB87401 + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) + (uint32_t)(*(uint32_t *)(v_rip + 0xB877F0)) * 4 * 8 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))));
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) | (Arg2);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x98 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) * 4 * 8 + 0x20) = 1;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x98 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) * 4 * 8 + 0x18) = result;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC3432B)))) == 2) goto loc_0039B2B8;
loc_0039ACE2:
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0xC2BE94))) + (v_stack_mB8);
    *(uint64_t *)(v_rip + 0xB87292) = result;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x8))) + (v_stack_mB8);
    *(uint64_t *)(v_stack_m90) = result;
    *(uint64_t *)(v_stack_m80 + 0x10) = v_stack_mB8;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x98 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) * 4 * 8 + 0x10) = v_stack_mB8;
loc_0039AD0E:
    if (0 != 0) goto loc_0039B300;
loc_0039AD17:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(v_stack_mB0), a4);
    return result;
loc_0039AD45:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2BD6D)))) & (64)) == 0) goto loc_0039AA4A;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, (uint32_t)(v_stack_mB0), a4);
    if ((uint8_t)(result) == 0) goto loc_0039AA4A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))), Arg2, (uint32_t)(v_stack_mB0), a4);
    goto loc_0039AA4C;
loc_0039AD6C:
loc_0039AD73:
    if ((uint8_t)(result) != 0) goto loc_0039AD73;
    if (condition_is_above_or_equal) goto loc_0039AA87;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mB0))))), (uint32_t)(v_stack_mB0), a4);
    goto loc_0039AA87;
loc_0039AD94:
    if ((*(uint32_t *)(v_rip + 0xC2A296)) == ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30)))) goto loc_0039AE47;
loc_0039ADA0:
    result = RtlGetInterruptTimePrecise(v_stack_mA8, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mB0))))), (uint32_t)(v_stack_mB0), a4);
loc_0039ADAC:
    result = KiUpdateRunTime((uint8_t)(v_stack_m90), v_stack_mC8, (uint32_t)(v_stack_mB0), a4);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x98 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) * 4 * 8 + 0x10) = result;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x98 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) * 4 * 8) = result;
    Arg2 = (v_stack_mC8) << (32);
    result = (result) | (Arg2);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x98 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) * 4 * 8 + 0x20) = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x98 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9580 + 0x8C)) * 4 * 8 + 0x18) = result;
    if ((*(uint8_t *)(v_rip + 0xC2BC9F)) == 0) goto loc_0039B2F7;
    if ((*(uint32_t *)(v_rip + 0xC2BF20)) != 0) goto loc_0039AF42;
loc_0039AE06:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x9580 + 0x10)) == 1) {
        *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x9580 + 0x10) = 2;
    }
    result = KiSetNextClockTickDueTime(result, 1, (uint32_t)(v_stack_mB0), a4);
    if ((*(uint32_t *)(v_rip + 0xC2BEF3)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)((uint8_t)((uint8_t)(v_cr8)));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(v_stack_mB0), a4);
    }
    goto loc_0039AD0E;
loc_0039AE47:
    if ((*(uint8_t *)(v_rip + 0xC2BC38)) == ((uint8_t)((uint8_t)((uint8_t)(v_cr8))))) goto loc_0039ADA0;
    result = KeDisableInterrupts(Arg1, Arg2, (uint32_t)(v_stack_mB0), a4);
    Arg2 = 0;
    Arg1 = 0;
    result = KiUpdateTimeAssist(Arg1, Arg2, v_stack_mB8, v_stack_mA8);
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0039AF68;
loc_0039AE74:
    if ((*(uint32_t *)(v_rip + 0xC2BE9D)) != 0) goto loc_0039AF83;
loc_0039AE89:
    Arg3 = 0;
    result = KiSetClockTimerKTimerDeadlines(*(uint64_t *)(v_stack_m28 + 0x40), v_stack_mB8, Arg3, v_stack_mA8);
    if ((*(uint32_t *)(v_rip + 0xC2BE7E)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8))));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, v_stack_mA8);
    }
    goto loc_0039ADAC;
loc_0039AEBC:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x9590)) != 1) goto loc_0039AC1E;
    v_stack_mC0 = (uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8))));
    if ((*(uint32_t *)(v_rip + 0xC2BE45)) != ((uint32_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))))) goto loc_0039AF53;
loc_0039AEDD:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x9590) = 2;
    *(uint32_t *)(v_rip + 0xB870B7) = 2;
    *(uint64_t *)(v_rip + 0xB87098) = (uint8_t)((uint8_t)((uint8_t)(v_cr8)));
    result = (uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8))));
    if ((*(uint32_t *)(v_rip + 0xC2BE0E)) != ((uint32_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))))) {
        Arg1 = 15;
        Arg2 = (uint8_t)((uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, v_stack_mA8);
        result = v_stack_mC0;
    }
    goto loc_0039AC1E;
loc_0039AF30:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)), 15, Arg3, v_stack_mA8);
    goto loc_0039AC61;
loc_0039AF42:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))), 15, Arg3, v_stack_mA8);
    goto loc_0039AE06;
loc_0039AF53:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), 15, Arg3, v_stack_mA8);
    goto loc_0039AEDD;
loc_0039AF68:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039AF94;
loc_0039AF7D:
    goto loc_0039AE74;
loc_0039AF83:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))), 15, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    goto loc_0039AE89;
loc_0039AF94:
loc_0039AF9B:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039AF9B;
    if (condition_is_above_or_equal) goto loc_0039AF7D;
    result = KiRemoveSystemWorkPriorityKick((uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    goto loc_0039AF7D;
loc_0039AFB5:
    result = KeDisableInterrupts((uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) == 0) goto loc_0039B1C0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) - 0x8)) != ((uint8_t)((uint8_t)((uint8_t)(v_cr8))))) goto loc_0039B1EA;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8))) != (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8))) goto loc_0039B054;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) = (uint8_t)((uint8_t)((uint8_t)(v_cr8)));
loc_0039AFE7:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8)) = (uint8_t)((uint8_t)((uint8_t)(v_cr8)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x30) + 0x38);
loc_0039AFF6:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0039B079;
loc_0039AFFB:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x10)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x18))) goto loc_0039A9EF;
    if (((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x20) + 0x28)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x28)))) == 0) goto loc_0039B212;
    result = KeDisableInterrupts(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x28)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x20), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x10), v_stack_mA8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8))) != ((uint8_t)((uint8_t)((uint8_t)(v_cr8))))) goto loc_0039B153;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) == 0) goto loc_0039B1FF;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x8))) == (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8))) goto loc_0039B145;
loc_0039B04D:
loc_0039B054:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8))) goto loc_0039B04D;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8))) goto loc_0039B04D;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8)) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x8);
    goto loc_0039AFE7;
loc_0039B079:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039B11D;
loc_0039B092:
    goto loc_0039AFFB;
loc_0039B098:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38E0)) != ((uint32_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))))) goto loc_0039A9FB;
    result = KeDisableInterrupts(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x20), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38E5)) != ((uint8_t)((uint8_t)((uint8_t)((uint8_t)(v_cr8)))))) goto loc_0039B234;
loc_0039B0B5:
    if ((uint8_t)(result) == 0) goto loc_0039A9FB;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039B198;
loc_0039B0D6:
    goto loc_0039A9FB;
loc_0039B0DC:
    if ((*(uint32_t *)(v_rip + 0xB86EC5)) != 1) goto loc_0039AD17;
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(result)), 15, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
loc_0039B10E:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(result)), 15, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    goto loc_0039AAC8;
loc_0039B11D:
loc_0039B124:
    if ((*(uint32_t *)(v_rip + 0xC2BC28)) != 0) goto loc_0039B124;
    if ((*(uint32_t *)(v_rip + 0xC2BC28)) >= 0) goto loc_0039B092;
    result = KiRemoveSystemWorkPriorityKick((uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    goto loc_0039B092;
loc_0039B145:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8)) = (uint8_t)((uint8_t)(result));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x8) = result;
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8);
    *(uint64_t *)((uint8_t)((uint8_t)(result)) + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8);
loc_0039B153:
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)) == 0) goto loc_0039A9EF;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039B177;
loc_0039B171:
    goto loc_0039A9EF;
loc_0039B177:
loc_0039B17E:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039B17E;
    if (condition_is_above_or_equal) goto loc_0039B171;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    goto loc_0039B171;
loc_0039B198:
loc_0039B19F:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039B19F;
    if (condition_is_above_or_equal) goto loc_0039B0D6;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    goto loc_0039B0D6;
loc_0039B1C0:
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)) == 0) goto loc_0039A9EF;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) == 0) goto loc_0039B171;
loc_0039B1EA:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8)) == ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))) goto loc_0039AFF6;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)));
    goto loc_0039AFF6;
loc_0039B1FF:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8)) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8);
    goto loc_0039B153;
loc_0039B212:
    result = KiSrcuReportQuiescent(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) - 8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    if ((uint32_t)(result) == 0) goto loc_0039A9EF;
    result = KiSrcuFlushCompleted(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8) + 0x30), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
    goto loc_0039A9EF;
loc_0039B234:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38E0)) != ((uint32_t)((uint8_t)(result)))) goto loc_0039B0B5;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38E5) = (uint8_t)((uint8_t)(result));
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38E8) = *(uint64_t *)(v_rip + 0xB85E97);
    goto loc_0039B0B5;
loc_0039B25D:
    result = KiRaiseIrqlProcessIrqlFlags(15, 15, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
loc_0039B284:
    if ((*(uint32_t *)(v_rip + 0xB86D1D)) != 2) goto loc_0039AC88;
    result = KiRaiseIrqlProcessIrqlFlags(15, 15, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), v_stack_mA8);
loc_0039B2B8:
    result = KiRestoreClockTickRate(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x38F8), v_stack_mA0, v_stack_m98, v_stack_mA8);
    if ((*(uint8_t *)(v_rip + 0xC2B7B7)) != ((uint8_t)((uint8_t)(result)))) goto loc_0039ACE2;
    Arg1 = 0;
    result = KiEventClockStateChange(Arg1, 2, v_stack_m98, v_stack_mA0);
    goto loc_0039ACE2;
loc_0039B2F7:
    goto loc_0039AD0E;
loc_0039B300:
    goto loc_0039AA9B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x170` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039A970&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
