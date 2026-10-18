# PpmIdleExecuteTransition

- RVA: `0x002D0A1C`–`0x002D123A` (길이 `2,078` bytes)
- VA: `0x00000001402D0A1C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006F73C`
- 디코드: `458`개 명령, `2,078/2,078` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x002D0A72` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002D0AFC` → [KeIsEmptyAffinityEx](KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x002D0B85` → [PpmEndActiveTimeAccumulation](PpmEndActiveTimeAccumulation_function_002D17F0.md) (function, `0x002D17F0`)
- `0x002D0BB9` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x002D0BC7` → [PpmBeginActiveTimeAccumulation](PpmBeginActiveTimeAccumulation_function_002D18D0.md) (function, `0x002D18D0`)
- `0x002D0C43` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002D0C92` → [PpmExitCoordinatedIdle](PpmExitCoordinatedIdle_function_002D184C.md) (function, `0x002D184C`)
- `0x002D0CD4` → [PpmUnlockProcessors](PpmUnlockProcessors_function_002D15B0.md) (function, `0x002D15B0`)
- `0x002D0CF5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002D0D2E` → [PpmEnterCoordinatedIdle](PpmEnterCoordinatedIdle_function_002D19B0.md) (function, `0x002D19B0`)
- `0x002D0D56` → [PpmEventEnterIdleState](PpmEventEnterIdleState_function_002D1B40.md) (function, `0x002D1B40`)
- `0x002D0D89` → [KeDeepSleepProcessor](../5B/KeDeepSleepProcessor_function_005BDB24.md) (function, `0x005BDB24`)
- `0x002D0DF3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002D0E20` → [HvlSetPlatformIdleState](../58/HvlSetPlatformIdleState_function_0058AA20.md) (function, `0x0058AA20`)
- `0x002D0E62` → [PpmIdleUpdateConcurrency](../48/PpmIdleUpdateConcurrency_function_004854C0.md) (function, `0x004854C0`)
- `0x002D0E84` → [PpmIdleUpdateConcurrency](../48/PpmIdleUpdateConcurrency_function_004854C0.md) (function, `0x004854C0`)
- `0x002D0EC0` → [KiCancelClockTimer](../47/KiCancelClockTimer_function_004743CC.md) (function, `0x004743CC`)
- `0x002D0ED6` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002D0EF6` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002D0F2F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002D0F71` → [PpmEventExitIdleState](PpmEventExitIdleState_function_002D1AC4.md) (function, `0x002D1AC4`)
- `0x002D1040` → [PpmIdleSetSynchronizationState](../4D/PpmIdleSetSynchronizationState_function_004D9958.md) (function, `0x004D9958`)
- `0x002D107B` → [PpmIdleUpdateConcurrency](../48/PpmIdleUpdateConcurrency_function_004854C0.md) (function, `0x004854C0`)
- `0x002D1099` → [PpmIdleUpdateConcurrency](../48/PpmIdleUpdateConcurrency_function_004854C0.md) (function, `0x004854C0`)
- `0x002D10C0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002D10ED` → [HvlSetPlatformIdleState](../58/HvlSetPlatformIdleState_function_0058AA20.md) (function, `0x0058AA20`)
- `0x002D110F` → [PpmIdleSetSynchronizationState](../4D/PpmIdleSetSynchronizationState_function_004D9958.md) (function, `0x004D9958`)
- `0x002D112C` → [KeWakeProcessor](../5B/KeWakeProcessor_function_005BE080.md) (function, `0x005BE080`)
- `0x002D114B` → [PpmIdleSetSynchronizationState](../4D/PpmIdleSetSynchronizationState_function_004D9958.md) (function, `0x004D9958`)
- `0x002D1182` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002D11C7` → [KiCancelClockTimer](../47/KiCancelClockTimer_function_004743CC.md) (function, `0x004743CC`)
- `0x002D1222` → [PpmTraceExitLatency](../5D/PpmTraceExitLatency_function_005D0A64.md) (function, `0x005D0A64`)

### Direct callers
- [PoIdle](../2C/PoIdle_function_002CFB40.md) at `0x002CFCCB`

### Static image references
- `0x002D0A35` → RVA `0x00E0A740` (`.data`; read)
- `0x002D0BFC` → RVA `0x00F0ED10` (`.data`; read)
- `0x002D0C37` → RVA `0x00E00C08` (`.data`; read)
- `0x002D0E01` → RVA `0x00E0B3B4` (`.data`; read)
- `0x002D0E2A` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x002D0EAE` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002D11D1` → RVA `0x00FC6AD0` (`ALMOSTRO`; read)
- `0x002D11F3` → RVA `0x00E67684` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **15**
  - `0x002D0B4A` → [sub_006DCEEE](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D0C24` → [sub_006DCEEE + 0x355](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D0D83` → [sub_006DCEEE + 0x28D](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D0DAF` → [sub_006DCEEE + 0x297](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D0DBF` → [sub_006DCEEE + 0x297](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D0DD0` → [sub_006DCEEE + 0x297](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D1051` → [sub_006DCEEE + 0x73](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D1064` → [sub_006DCEEE + 0x73](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D1153` → [sub_006DCEEE + 0x340](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D115B` → [sub_006DCEEE + 0x340](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D1166` → [sub_006DCEEE + 0x340](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D1198` → [sub_006DCEEE + 0x34C](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D11B8` → [sub_006DCEEE + 0x443](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D1209` → [sub_006DCEEE + 0x47B](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)
  - `0x002D122B` → [sub_006DCEEE + 0x47B](../6D/Unknown_function_006DCEEE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002D0A1C  40 55                           push rbp
002D0A1E  53                              push rbx
002D0A1F  56                              push rsi
002D0A20  57                              push rdi
002D0A21  41 54                           push r12
002D0A23  41 55                           push r13
002D0A25  41 56                           push r14
002D0A27  41 57                           push r15
002D0A29  48 8D 6C 24 B8                  lea rbp, [rsp - 0x48]
002D0A2E  48 81 EC 48 01 00 00            sub rsp, 0x148
002D0A35  48 8B 05 04 9D B3 00            mov rax, qword ptr [rip + 0xb39d04]
002D0A3C  48 33 C4                        xor rax, rsp
002D0A3F  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
002D0A43  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
002D0A4A  41 8B F0                        mov esi, r8d
002D0A4D  44 8B F2                        mov r14d, edx
002D0A50  48 8B D9                        mov rbx, rcx
002D0A53  44 89 44 24 68                  mov dword ptr [rsp + 0x68], r8d
002D0A58  48 8D 4D A0                     lea rcx, [rbp - 0x60]
002D0A5C  33 D2                           xor edx, edx
002D0A5E  44 89 74 24 58                  mov dword ptr [rsp + 0x58], r14d
002D0A63  41 B8 88 00 00 00               mov r8d, 0x88
002D0A69  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002D0A6E  4C 89 4D 98                     mov qword ptr [rbp - 0x68], r9
002D0A72  E8 C9 61 3F 00                  call 0x1406c6c40
002D0A77  48 8B BB 40 88 00 00            mov rdi, qword ptr [rbx + 0x8840]
002D0A7E  33 D2                           xor edx, edx
002D0A80  83 4C 24 74 FF                  or dword ptr [rsp + 0x74], 0xffffffff
002D0A85  44 8B E2                        mov r12d, edx
002D0A88  49 69 CE 58 01 00 00            imul rcx, r14, 0x158
002D0A8F  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
002D0A93  44 8B FA                        mov r15d, edx
002D0A96  48 8B 87 98 02 00 00            mov rax, qword ptr [rdi + 0x298]
002D0A9D  48 03 CF                        add rcx, rdi
002D0AA0  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002D0AA4  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
002D0AA9  88 54 24 51                     mov byte ptr [rsp + 0x51], dl
002D0AAD  88 54 24 54                     mov byte ptr [rsp + 0x54], dl
002D0AB1  44 0F B6 EA                     movzx r13d, dl
002D0AB5  88 10                           mov byte ptr [rax], dl
002D0AB7  8D 42 01                        lea eax, [rdx + 1]
002D0ABA  88 54 24 55                     mov byte ptr [rsp + 0x55], dl
002D0ABE  88 54 24 56                     mov byte ptr [rsp + 0x56], dl
002D0AC2  88 54 24 50                     mov byte ptr [rsp + 0x50], dl
002D0AC6  C7 45 80 0B 00 00 00            mov dword ptr [rbp - 0x80], 0xb
002D0ACD  C7 44 24 6C 82 00 00 00         mov dword ptr [rsp + 0x6c], 0x82
002D0AD5  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
002D0AD9  88 54 24 57                     mov byte ptr [rsp + 0x57], dl
002D0ADD  38 95 C8 00 00 00               cmp byte ptr [rbp + 0xc8], dl
002D0AE3  0F 85 02 05 00 00               jne 0x1402d0feb
002D0AE9  44 8A F2                        mov r14b, dl
002D0AEC  48 8D 8F 50 01 00 00            lea rcx, [rdi + 0x150]
002D0AF3  44 88 74 24 53                  mov byte ptr [rsp + 0x53], r14b
002D0AF8  88 54 24 52                     mov byte ptr [rsp + 0x52], dl
002D0AFC  E8 7F 0A 00 00                  call 0x1402d1580
002D0B01  45 33 DB                        xor r11d, r11d
002D0B04  85 C0                           test eax, eax
002D0B06  0F 84 FF 04 00 00               je 0x1402d100b
002D0B0C  44 38 9D D8 00 00 00            cmp byte ptr [rbp + 0xd8], r11b
002D0B13  0F 85 FC 04 00 00               jne 0x1402d1015
002D0B19  B9 02 00 00 00                  mov ecx, 2
002D0B1E  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
002D0B22  89 83 80 88 00 00               mov dword ptr [rbx + 0x8880], eax
002D0B28  44 88 B3 7C 88 00 00            mov byte ptr [rbx + 0x887c], r14b
002D0B2F  44 38 9D C8 00 00 00            cmp byte ptr [rbp + 0xc8], r11b
002D0B36  0F 85 E7 04 00 00               jne 0x1402d1023
002D0B3C  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
002D0B40  41 B9 01 00 00 00               mov r9d, 1
002D0B46  48 83 F8 FF                     cmp rax, -1
002D0B4A  0F 85 9E C3 40 00               jne 0x1406dceee
002D0B50  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
002D0B54  44 38 98 71 05 00 00            cmp byte ptr [rax + 0x571], r11b
002D0B5B  0F 84 E9 04 00 00               je 0x1402d104a
002D0B61  4C 8B AB F8 89 00 00            mov r13, qword ptr [rbx + 0x89f8]
002D0B68  4C 8B B5 B8 00 00 00            mov r14, qword ptr [rbp + 0xb8]
002D0B6F  4D 85 ED                        test r13, r13
002D0B72  0F 85 F1 04 00 00               jne 0x1402d1069
002D0B78  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
002D0B7C  49 8B D6                        mov rdx, r14
002D0B7F  48 8B CB                        mov rcx, rbx
002D0B82  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
002D0B85  E8 66 0C 00 00                  call 0x1402d17f0
002D0B8A  4C 8B 97 58 02 00 00            mov r10, qword ptr [rdi + 0x258]
002D0B91  4C 8D A7 08 04 00 00            lea r12, [rdi + 0x408]
002D0B98  4D 85 D2                        test r10, r10
002D0B9B  0F 85 02 05 00 00               jne 0x1402d10a3
002D0BA1  83 FE FF                        cmp esi, -1
002D0BA4  0F 85 23 05 00 00               jne 0x1402d10cd
002D0BAA  45 85 FF                        test r15d, r15d
002D0BAD  0F 89 5C 01 00 00               jns 0x1402d0d0f
002D0BB3  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
002D0BB7  33 C9                           xor ecx, ecx
002D0BB9  E8 22 DC 0A 00                  call 0x14037e7e0
002D0BBE  48 8B D0                        mov rdx, rax
002D0BC1  48 8B CB                        mov rcx, rbx
002D0BC4  4C 8B E0                        mov r12, rax
002D0BC7  E8 04 0D 00 00                  call 0x1402d18d0
002D0BCC  45 33 DB                        xor r11d, r11d
002D0BCF  4D 85 ED                        test r13, r13
002D0BD2  0F 85 7B 02 00 00               jne 0x1402d0e53
002D0BD8  49 8B C4                        mov rax, r12
002D0BDB  49 2B C6                        sub rax, r14
002D0BDE  48 89 83 50 88 00 00            mov qword ptr [rbx + 0x8850], rax
002D0BE5  44 38 9D C8 00 00 00            cmp byte ptr [rbp + 0xc8], r11b
002D0BEC  0F 85 50 05 00 00               jne 0x1402d1142
002D0BF2  44 8A 6C 24 52                  mov r13b, byte ptr [rsp + 0x52]
002D0BF7  B9 01 00 00 00                  mov ecx, 1
002D0BFC  48 8B 05 0D E1 C3 00            mov rax, qword ptr [rip + 0xc3e10d]
002D0C03  4C 8D B7 08 04 00 00            lea r14, [rdi + 0x408]
002D0C0A  48 39 83 50 88 00 00            cmp qword ptr [rbx + 0x8850], rax
002D0C11  0F 82 71 05 00 00               jb 0x1402d1188
002D0C17  44 88 5F 41                     mov byte ptr [rdi + 0x41], r11b
002D0C1B  8A 44 24 50                     mov al, byte ptr [rsp + 0x50]
002D0C1F  44 38 5C 24 54                  cmp byte ptr [rsp + 0x54], r11b
002D0C24  0F 85 19 C6 40 00               jne 0x1406dd243
002D0C2A  44 38 9D D8 00 00 00            cmp byte ptr [rbp + 0xd8], r11b
002D0C31  0F 85 7C 05 00 00               jne 0x1402d11b3
002D0C37  48 8B 05 CA FF B2 00            mov rax, qword ptr [rip + 0xb2ffca]
002D0C3E  B9 01 00 00 00                  mov ecx, 1
002D0C43  E8 88 9E 3E 00                  call 0x1406baad0
002D0C48  33 C9                           xor ecx, ecx
002D0C4A  38 4C 24 56                     cmp byte ptr [rsp + 0x56], cl
002D0C4E  0F 85 D6 01 00 00               jne 0x1402d0e2a
002D0C54  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
002D0C58  45 8B CF                        mov r9d, r15d
002D0C5B  44 8A 44 24 50                  mov r8b, byte ptr [rsp + 0x50]
002D0C60  49 8B D6                        mov rdx, r14
002D0C63  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
002D0C67  48 8B CB                        mov rcx, rbx
002D0C6A  48 8D 45 A0                     lea rax, [rbp - 0x60]
002D0C6E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002D0C73  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
002D0C78  8A 00                           mov al, byte ptr [rax]
002D0C7A  88 44 24 38                     mov byte ptr [rsp + 0x38], al
002D0C7E  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
002D0C84  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002D0C88  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
002D0C8D  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
002D0C92  E8 B5 0B 00 00                  call 0x1402d184c
002D0C97  45 84 ED                        test r13b, r13b
002D0C9A  8B F0                           mov esi, eax
002D0C9C  44 8B 6C 24 58                  mov r13d, dword ptr [rsp + 0x58]
002D0CA1  0F 84 2E 01 00 00               je 0x1402d0dd5
002D0CA7  4D 8B 4E 10                     mov r9, qword ptr [r14 + 0x10]
002D0CAB  45 8B 46 04                     mov r8d, dword ptr [r14 + 4]
002D0CAF  45 33 F6                        xor r14d, r14d
002D0CB2  45 85 C0                        test r8d, r8d
002D0CB5  0F 85 16 05 00 00               jne 0x1402d11d1
002D0CBB  44 38 74 24 57                  cmp byte ptr [rsp + 0x57], r14b
002D0CC0  0F 85 2D 05 00 00               jne 0x1402d11f3
002D0CC6  48 8D 97 50 01 00 00            lea rdx, [rdi + 0x150]
002D0CCD  48 8D 8F 50 01 00 00            lea rcx, [rdi + 0x150]
002D0CD4  E8 D7 08 00 00                  call 0x1402d15b0
002D0CD9  44 38 77 03                     cmp byte ptr [rdi + 3], r14b
002D0CDD  0F 85 1C 05 00 00               jne 0x1402d11ff
002D0CE3  8A 44 24 52                     mov al, byte ptr [rsp + 0x52]
002D0CE7  88 47 40                        mov byte ptr [rdi + 0x40], al
002D0CEA  44 89 7F 3C                     mov dword ptr [rdi + 0x3c], r15d
002D0CEE  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
002D0CF2  48 33 CC                        xor rcx, rsp
002D0CF5  E8 46 B9 3D 00                  call 0x1406ac640
002D0CFA  48 81 C4 48 01 00 00            add rsp, 0x148
002D0D01  41 5F                           pop r15
002D0D03  41 5E                           pop r14
002D0D05  41 5D                           pop r13
002D0D07  41 5C                           pop r12
002D0D09  5F                              pop rdi
002D0D0A  5E                              pop rsi
002D0D0B  5B                              pop rbx
002D0D0C  5D                              pop rbp
002D0D0D  C3                              ret
002D0D0E  CC                              int3
002D0D0F  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
002D0D15  4D 8B CE                        mov r9, r14
002D0D18  49 8B 54 24 10                  mov rdx, qword ptr [r12 + 0x10]
002D0D1D  44 8B C6                        mov r8d, esi
002D0D20  41 8B 4C 24 04                  mov ecx, dword ptr [r12 + 4]
002D0D25  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002D0D29  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
002D0D2E  E8 7D 0C 00 00                  call 0x1402d19b0
002D0D33  83 FE FF                        cmp esi, -1
002D0D36  0F 85 BB 03 00 00               jne 0x1402d10f7
002D0D3C  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
002D0D41  41 8B CF                        mov ecx, r15d
002D0D44  4C 8B 8F B0 02 00 00            mov r9, qword ptr [rdi + 0x2b0]
002D0D4B  44 8A 87 CD 02 00 00            mov r8b, byte ptr [rdi + 0x2cd]
002D0D52  0F B7 57 38                     movzx edx, word ptr [rdi + 0x38]
002D0D56  E8 E5 0D 00 00                  call 0x1402d1b40
002D0D5B  45 33 D2                        xor r10d, r10d
002D0D5E  44 38 95 C8 00 00 00            cmp byte ptr [rbp + 0xc8], r10b
002D0D65  0F 85 96 03 00 00               jne 0x1402d1101
002D0D6B  41 B9 02 00 00 00               mov r9d, 2
002D0D71  44 38 54 24 54                  cmp byte ptr [rsp + 0x54], r10b
002D0D76  74 21                           je 0x1402d0d99
002D0D78  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
002D0D7C  44 38 88 70 05 00 00            cmp byte ptr [rax + 0x570], r9b
002D0D83  0F 82 F2 C3 40 00               jb 0x1406dd17b
002D0D89  E8 96 CD 2E 00                  call 0x1405bdb24
002D0D8E  45 33 D2                        xor r10d, r10d
002D0D91  88 44 24 51                     mov byte ptr [rsp + 0x51], al
002D0D95  45 8D 4A 02                     lea r9d, [r10 + 2]
002D0D99  F0 FE 83 E7 38 00 00            lock inc byte ptr [rbx + 0x38e7]
002D0DA0  B9 01 00 00 00                  mov ecx, 1
002D0DA5  45 0F B7 C2                     movzx r8d, r10w
002D0DA9  84 8B DC 06 00 00               test byte ptr [rbx + 0x6dc], cl
002D0DAF  0F 84 D0 C3 40 00               je 0x1406dd185
002D0DB5  0F B7 83 E6 06 00 00            movzx eax, word ptr [rbx + 0x6e6]
002D0DBC  66 85 C0                        test ax, ax
002D0DBF  0F 84 C0 C3 40 00               je 0x1406dd185
002D0DC5  66 09 8B D8 06 00 00            or word ptr [rbx + 0x6d8], cx
002D0DCC  44 0F B7 C0                     movzx r8d, ax
002D0DD0  E9 B0 C3 40 00                  jmp 0x1406dd185
002D0DD5  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
002D0DD9  44 8B C6                        mov r8d, esi
002D0DDC  48 8B 87 80 02 00 00            mov rax, qword ptr [rdi + 0x280]
002D0DE3  41 8B D5                        mov edx, r13d
002D0DE6  45 8B 4E 04                     mov r9d, dword ptr [r14 + 4]
002D0DEA  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002D0DEF  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
002D0DF3  E8 D8 9C 3E 00                  call 0x1406baad0
002D0DF8  83 FE FF                        cmp esi, -1
002D0DFB  0F 84 A6 FE FF FF               je 0x1402d0ca7
002D0E01  3B 35 AD A5 B3 00               cmp esi, dword ptr [rip + 0xb3a5ad]
002D0E07  0F 85 9A FE FF FF               jne 0x1402d0ca7
002D0E0D  B8 02 00 00 00                  mov eax, 2
002D0E12  39 83 20 89 00 00               cmp dword ptr [rbx + 0x8920], eax
002D0E18  0F 8C 89 FE FF FF               jl 0x1402d0ca7
002D0E1E  33 C9                           xor ecx, ecx
002D0E20  E8 FB 9B 2B 00                  call 0x14058aa20
002D0E25  E9 7D FE FF FF                  jmp 0x1402d0ca7
002D0E2A  38 0D 55 5C CF 00               cmp byte ptr [rip + 0xcf5c55], cl
002D0E30  75 5F                           jne 0x1402d0e91
002D0E32  48 8B 83 C0 00 00 00            mov rax, qword ptr [rbx + 0xc0]
002D0E39  0F B6 8B D1 00 00 00            movzx ecx, byte ptr [rbx + 0xd1]
002D0E40  F0 48 0F B3 48 48               lock btr qword ptr [rax + 0x48], rcx
002D0E46  48 83 8B 70 88 00 00 FF         or qword ptr [rbx + 0x8870], 0xffffffffffffffff
002D0E4E  E9 01 FE FF FF                  jmp 0x1402d0c54
002D0E53  41 B9 01 00 00 00               mov r9d, 1
002D0E59  45 33 C0                        xor r8d, r8d
002D0E5C  49 8B D4                        mov rdx, r12
002D0E5F  49 8B CD                        mov rcx, r13
002D0E62  E8 59 46 1B 00                  call 0x1404854c0
002D0E67  48 8B 8B 00 8A 00 00            mov rcx, qword ptr [rbx + 0x8a00]
002D0E6E  45 33 DB                        xor r11d, r11d
002D0E71  48 85 C9                        test rcx, rcx
002D0E74  0F 84 5E FD FF FF               je 0x1402d0bd8
002D0E7A  45 8D 4B 01                     lea r9d, [r11 + 1]
002D0E7E  45 33 C0                        xor r8d, r8d
002D0E81  49 8B D4                        mov rdx, r12
002D0E84  E8 37 46 1B 00                  call 0x1404854c0
002D0E89  45 33 DB                        xor r11d, r11d
002D0E8C  E9 47 FD FF FF                  jmp 0x1402d0bd8
002D0E91  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
002D0E95  38 88 71 05 00 00               cmp byte ptr [rax + 0x571], cl
002D0E9B  0F 84 1C 03 00 00               je 0x1402d11bd
002D0EA1  44 0F 20 C6                     mov rsi, cr8
002D0EA5  BA 0F 00 00 00                  mov edx, 0xf
002D0EAA  44 0F 22 C2                     mov cr8, rdx
002D0EAE  39 0D 6C 5E CF 00               cmp dword ptr [rip + 0xcf5e6c], ecx
002D0EB4  75 3D                           jne 0x1402d0ef3
002D0EB6  45 33 C0                        xor r8d, r8d
002D0EB9  48 8B CB                        mov rcx, rbx
002D0EBC  41 8D 50 05                     lea edx, [r8 + 5]
002D0EC0  E8 07 35 1A 00                  call 0x1404743cc
002D0EC5  33 C0                           xor eax, eax
002D0EC7  39 05 53 5E CF 00               cmp dword ptr [rip + 0xcf5e53], eax
002D0ECD  74 0C                           je 0x1402d0edb
002D0ECF  44 0F 20 C1                     mov rcx, cr8
002D0ED3  40 8A D6                        mov dl, sil
002D0ED6  E8 BD 47 22 00                  call 0x1404f5698
002D0EDB  40 0F B6 C6                     movzx eax, sil
002D0EDF  44 0F 22 C0                     mov cr8, rax
002D0EE3  48 C7 83 70 88 00 00 FF FF FF FF  mov qword ptr [rbx + 0x8870], 0xffffffffffffffff
002D0EEE  E9 61 FD FF FF                  jmp 0x1402d0c54
002D0EF3  40 8A CE                        mov cl, sil
002D0EF6  E8 01 48 22 00                  call 0x1404f56fc
002D0EFB  EB B9                           jmp 0x1402d0eb6
002D0EFD  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
002D0F02  45 8B C7                        mov r8d, r15d
002D0F05  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
002D0F0A  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
002D0F0E  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
002D0F12  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002D0F17  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
002D0F1C  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
002D0F20  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
002D0F24  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002D0F28  48 8B 87 60 02 00 00            mov rax, qword ptr [rdi + 0x260]
002D0F2F  E8 9C 9B 3E 00                  call 0x1406baad0
002D0F34  44 8B F8                        mov r15d, eax
002D0F37  40 F6 C6 04                     test sil, 4
002D0F3B  75 3E                           jne 0x1402d0f7b
002D0F3D  B8 FE FF 00 00                  mov eax, 0xfffe
002D0F42  33 F6                           xor esi, esi
002D0F44  66 21 83 D8 06 00 00            and word ptr [rbx + 0x6d8], ax
002D0F4B  F0 FE 8B E7 38 00 00            lock dec byte ptr [rbx + 0x38e7]
002D0F52  40 38 74 24 51                  cmp byte ptr [rsp + 0x51], sil
002D0F57  0F 85 BC 01 00 00               jne 0x1402d1119
002D0F5D  8B 47 3C                        mov eax, dword ptr [rdi + 0x3c]
002D0F60  85 C0                           test eax, eax
002D0F62  0F 88 CE 01 00 00               js 0x1402d1136
002D0F68  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
002D0F6C  41 8B D7                        mov edx, r15d
002D0F6F  8B CE                           mov ecx, esi
002D0F71  E8 4E 0B 00 00                  call 0x1402d1ac4
002D0F76  E9 3C FC FF FF                  jmp 0x1402d0bb7
002D0F7B  48 8B 93 B0 2D 00 00            mov rdx, qword ptr [rbx + 0x2db0]
002D0F82  0F 0D 8A E0 06 00 00            prefetchw byte ptr [rdx + 0x6e0]
002D0F89  41 B8 02 00 00 00               mov r8d, 2
002D0F8F  0F B7 82 E0 06 00 00            movzx eax, word ptr [rdx + 0x6e0]
002D0F96  0F B7 C8                        movzx ecx, ax
002D0F99  66 83 E1 F7                     and cx, 0xfff7
002D0F9D  66 41 0B C8                     or cx, r8w
002D0FA1  66 F0 0F B1 8A E0 06 00 00      lock cmpxchg word ptr [rdx + 0x6e0], cx
002D0FAA  75 E3                           jne 0x1402d0f8f
002D0FAC  0F B7 83 E0 06 00 00            movzx eax, word ptr [rbx + 0x6e0]
002D0FB3  A8 10                           test al, 0x10
002D0FB5  75 86                           jne 0x1402d0f3d
002D0FB7  0F B7 83 E6 06 00 00            movzx eax, word ptr [rbx + 0x6e6]
002D0FBE  41 84 C0                        test r8b, al
002D0FC1  0F 84 76 FF FF FF               je 0x1402d0f3d
002D0FC7  B9 FD FF 00 00                  mov ecx, 0xfffd
002D0FCC  66 23 C1                        and ax, cx
002D0FCF  B9 48 00 00 00                  mov ecx, 0x48
002D0FD4  0F B7 D0                        movzx edx, ax
002D0FD7  66 89 93 E6 06 00 00            mov word ptr [rbx + 0x6e6], dx
002D0FDE  8B C2                           mov eax, edx
002D0FE0  48 C1 EA 20                     shr rdx, 0x20
002D0FE4  0F 30                           wrmsr
002D0FE6  E9 52 FF FF FF                  jmp 0x1402d0f3d
002D0FEB  38 97 CB 02 00 00               cmp byte ptr [rdi + 0x2cb], dl
002D0FF1  0F 85 F2 FA FF FF               jne 0x1402d0ae9
002D0FF7  44 8A F0                        mov r14b, al
002D0FFA  38 91 75 05 00 00               cmp byte ptr [rcx + 0x575], dl
002D1000  0F 84 E6 FA FF FF               je 0x1402d0aec
002D1006  E9 DE FA FF FF                  jmp 0x1402d0ae9
002D100B  66 83 4F 38 20                  or word ptr [rdi + 0x38], 0x20
002D1010  E9 F7 FA FF FF                  jmp 0x1402d0b0c
002D1015  B8 00 80 00 00                  mov eax, 0x8000
002D101A  66 09 47 38                     or word ptr [rdi + 0x38], ax
002D101E  E9 F6 FA FF FF                  jmp 0x1402d0b19
002D1023  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
002D1027  8A D1                           mov dl, cl
002D1029  48 8D 8B 8C 88 00 00            lea rcx, [rbx + 0x888c]
002D1030  44 38 98 72 05 00 00            cmp byte ptr [rax + 0x572], r11b
002D1037  0F 94 C0                        sete al
002D103A  88 83 7D 88 00 00               mov byte ptr [rbx + 0x887d], al
002D1040  E8 13 89 20 00                  call 0x1404d9958
002D1045  E9 F2 FA FF FF                  jmp 0x1402d0b3c
002D104A  44 38 9D D0 00 00 00            cmp byte ptr [rbp + 0xd0], r11b
002D1051  0F 84 0A BF 40 00               je 0x1406dcf61
002D1057  44 38 1D 27 5A CF 00            cmp byte ptr [rip + 0xcf5a27], r11b
002D105E  0F 84 FD FA FF FF               je 0x1402d0b61
002D1064  E9 F8 BE 40 00                  jmp 0x1406dcf61
002D1069  41 BC 01 00 00 00               mov r12d, 1
002D106F  49 8B D6                        mov rdx, r14
002D1072  45 8A CC                        mov r9b, r12b
002D1075  45 8A C4                        mov r8b, r12b
002D1078  49 8B CD                        mov rcx, r13
002D107B  E8 40 44 1B 00                  call 0x1404854c0
002D1080  48 8B 8B 00 8A 00 00            mov rcx, qword ptr [rbx + 0x8a00]
002D1087  48 85 C9                        test rcx, rcx
002D108A  0F 84 E8 FA FF FF               je 0x1402d0b78
002D1090  45 8A CC                        mov r9b, r12b
002D1093  45 8A C4                        mov r8b, r12b
002D1096  49 8B D6                        mov rdx, r14
002D1099  E8 22 44 1B 00                  call 0x1404854c0
002D109E  E9 D5 FA FF FF                  jmp 0x1402d0b78
002D10A3  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
002D10A8  44 8B C6                        mov r8d, esi
002D10AB  45 8B 4C 24 04                  mov r9d, dword ptr [r12 + 4]
002D10B0  8B 54 24 58                     mov edx, dword ptr [rsp + 0x58]
002D10B4  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
002D10B8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002D10BD  49 8B C2                        mov rax, r10
002D10C0  E8 0B 9A 3E 00                  call 0x1406baad0
002D10C5  44 8B F8                        mov r15d, eax
002D10C8  E9 D4 FA FF FF                  jmp 0x1402d0ba1
002D10CD  3B 35 E1 A2 B3 00               cmp esi, dword ptr [rip + 0xb3a2e1]
002D10D3  0F 85 D1 FA FF FF               jne 0x1402d0baa
002D10D9  B8 02 00 00 00                  mov eax, 2
002D10DE  39 83 20 89 00 00               cmp dword ptr [rbx + 0x8920], eax
002D10E4  0F 8C C0 FA FF FF               jl 0x1402d0baa
002D10EA  8D 48 FF                        lea ecx, [rax - 1]
002D10ED  E8 2E 99 2B 00                  call 0x14058aa20
002D10F2  E9 B3 FA FF FF                  jmp 0x1402d0baa
002D10F7  66 83 4F 38 10                  or word ptr [rdi + 0x38], 0x10
002D10FC  E9 3B FC FF FF                  jmp 0x1402d0d3c
002D1101  8A 54 24 53                     mov dl, byte ptr [rsp + 0x53]
002D1105  48 8D 8B 8C 88 00 00            lea rcx, [rbx + 0x888c]
002D110C  80 C2 03                        add dl, 3
002D110F  E8 44 88 20 00                  call 0x1404d9958
002D1114  E9 52 FC FF FF                  jmp 0x1402d0d6b
002D1119  8A 83 5A 86 00 00               mov al, byte ptr [rbx + 0x865a]
002D111F  40 88 74 24 51                  mov byte ptr [rsp + 0x51], sil
002D1124  84 C0                           test al, al
002D1126  0F 84 31 FE FF FF               je 0x1402d0f5d
002D112C  E8 4F CF 2E 00                  call 0x1405be080
002D1131  E9 27 FE FF FF                  jmp 0x1402d0f5d
002D1136  45 85 FF                        test r15d, r15d
002D1139  44 0F 49 F8                     cmovns r15d, eax
002D113D  E9 26 FE FF FF                  jmp 0x1402d0f68
002D1142  33 D2                           xor edx, edx
002D1144  48 8D 8B 8C 88 00 00            lea rcx, [rbx + 0x888c]
002D114B  E8 08 88 20 00                  call 0x1404d9958
002D1150  45 85 FF                        test r15d, r15d
002D1153  0F 88 D5 C0 40 00               js 0x1406dd22e
002D1159  3C 08                           cmp al, 8
002D115B  0F 84 CD C0 40 00               je 0x1406dd22e
002D1161  44 38 5C 24 53                  cmp byte ptr [rsp + 0x53], r11b
002D1166  0F 84 C2 C0 40 00               je 0x1406dd22e
002D116C  44 0F B6 C8                     movzx r9d, al
002D1170  BA 02 07 00 00                  mov edx, 0x702
002D1175  44 8B C6                        mov r8d, esi
002D1178  B9 A0 00 00 00                  mov ecx, 0xa0
002D117D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
002D1182  E8 D9 C4 22 00                  call 0x1404fd660
002D1187  CC                              int3
002D1188  45 39 5E 04                     cmp dword ptr [r14 + 4], r11d
002D118C  0F 86 85 FA FF FF               jbe 0x1402d0c17
002D1192  8A 44 24 50                     mov al, byte ptr [rsp + 0x50]
002D1196  84 C0                           test al, al
002D1198  0F 84 9C C0 40 00               je 0x1406dd23a
002D119E  8A 47 41                        mov al, byte ptr [rdi + 0x41]
002D11A1  3C 05                           cmp al, 5
002D11A3  0F 83 72 FA FF FF               jae 0x1402d0c1b
002D11A9  02 C1                           add al, cl
002D11AB  88 47 41                        mov byte ptr [rdi + 0x41], al
002D11AE  E9 68 FA FF FF                  jmp 0x1402d0c1b
002D11B3  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002D11B8  E9 74 C1 40 00                  jmp 0x1406dd331
002D11BD  45 33 C0                        xor r8d, r8d
002D11C0  48 8B CB                        mov rcx, rbx
002D11C3  41 8D 50 05                     lea edx, [r8 + 5]
002D11C7  E8 00 32 1A 00                  call 0x1404743cc
002D11CC  E9 12 FD FF FF                  jmp 0x1402d0ee3
002D11D1  48 8B 05 F8 58 CF 00            mov rax, qword ptr [rip + 0xcf58f8]
002D11D8  41 FF C8                        dec r8d
002D11DB  43 8B 0C 81                     mov ecx, dword ptr [r9 + r8*4]
002D11DF  48 69 D1 C0 01 00 00            imul rdx, rcx, 0x1c0
002D11E6  44 89 B4 02 A0 01 00 00         mov dword ptr [rdx + rax + 0x1a0], r14d
002D11EE  E9 BF FA FF FF                  jmp 0x1402d0cb2
002D11F3  F0 FF 0D 8A 64 B9 00            lock dec dword ptr [rip + 0xb9648a]
002D11FA  E9 C7 FA FF FF                  jmp 0x1402d0cc6
002D11FF  4C 8B B3 40 88 00 00            mov r14, qword ptr [rbx + 0x8840]
002D1206  45 85 FF                        test r15d, r15d
002D1209  0F 88 5A C1 40 00               js 0x1406dd369
002D120F  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
002D1213  44 8B C6                        mov r8d, esi
002D1216  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
002D121B  41 8B D5                        mov edx, r13d
002D121E  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002D1222  E8 3D F8 2F 00                  call 0x1405d0a64
002D1227  33 C9                           xor ecx, ecx
002D1229  85 C0                           test eax, eax
002D122B  0F 88 38 C1 40 00               js 0x1406dd369
002D1231  41 88 4E 03                     mov byte ptr [r14 + 3], cl
002D1235  E9 A9 FA FF FF                  jmp 0x1402d0ce3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmIdleExecuteTransition(__int64 a1, int a2, int a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, unsigned __int8 a8, unsigned __int8 a9, unsigned __int8 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m114;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int8 v_stack_m131;
    unsigned __int8 v_stack_m132;
    unsigned __int8 v_stack_m133;
    unsigned __int8 v_stack_m134;
    unsigned __int8 v_stack_m135;
    unsigned __int8 v_stack_m136;
    unsigned __int8 v_stack_m137;
    unsigned __int8 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int8 v_stack_m150;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int8 v_stack_m168;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p50;
    unsigned __int8 v_stack_p51;
    unsigned __int8 v_stack_p53;
    unsigned __int8 v_stack_p54;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p74;

    v_rsp = (v_rsp) - (328);
    result = (*(unsigned __int64 *)(v_rip + 11771140)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m120 = a3;
    a2 = 0;
    v_stack_m130 = (unsigned int)((unsigned int)(a2));
    v_stack_m128 = a11;
    v_stack_mF0 = a4;
    result = memset(v_stack_mE8, a2, 136, a4);
    a2 = 0;
    a1 = (v_stack_mE8) * ((unsigned int)(a2));
    v_stack_m108 = 0;
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 34880));
    v_stack_mF8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 664);
    v_stack_m137 = 0;
    v_stack_m134 = 0;
    *(unsigned __int8 *)(v_stack_m128) = 0;
    v_stack_m133 = 0;
    v_stack_m132 = 0;
    v_stack_m138 = 0;
    v_stack_m108 = 11;
    v_stack_m11C = 130;
    v_stack_m100 = a1;
    v_stack_m131 = 0;
    if (a8 != 0) goto loc_002D0FEB;
loc_002D0AE9:
loc_002D0AEC:
    v_stack_m135 = 0;
    v_stack_m136 = 0;
    result = KeIsEmptyAffinityEx(*(unsigned __int64 *)(a1 + 34880) + 336, a2, 136, a4);
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_002D100B;
loc_002D0B0C:
    if (a10 != 0) goto loc_002D1015;
loc_002D0B19:
    *(unsigned int *)(a1 + 34944) = (unsigned int)((unsigned int)(v_stack_m130));
    *(unsigned __int8 *)(a1 + 34940) = 0;
    if (a8 != 0) goto loc_002D1023;
loc_002D0B3C:
    if ((*(unsigned __int8 *)(v_stack_m100 + 1393)) == 0) goto loc_002D104A;
loc_002D0B61:
    if (*(unsigned __int64 *)(a1 + 35320) != 0) goto loc_002D1069;
loc_002D0B78:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 28) = (unsigned int)((unsigned int)(v_stack_m130));
    result = PpmEndActiveTimeAccumulation(a1, a6, 136, 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 600) != 0) goto loc_002D10A3;
loc_002D0BA1:
    if (((unsigned int)((unsigned int)(a3))) != -1) goto loc_002D10CD;
loc_002D0BAA:
    if (!sign_flag) goto loc_002D0D0F;
loc_002D0BB7:
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a6, 136, 1);
    result = PpmBeginActiveTimeAccumulation(0, result, 136, 1);
    v_r11 = 0;
    if (*(unsigned __int64 *)(a1 + 35320) != 0) goto loc_002D0E53;
loc_002D0BD8:
    result = (result) - (a6);
    *(unsigned __int64 *)(a1 + 34896) = result;
    if (a8 != 0) goto loc_002D1142;
    if ((*(unsigned __int64 *)(a1 + 34896)) < (*(unsigned __int64 *)(v_rip + 12837133))) goto loc_002D1188;
loc_002D0C17:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 65) = 0;
loc_002D0C1B:
    if (a10 != 0) goto loc_002D11B3;
    result = guard_dispatch_icall(1, result, 136, 1);
    a1 = 0;
    if (v_stack_m132 != 0) goto loc_002D0E2A;
loc_002D0C54:
    v_stack_m140 = (unsigned int)((unsigned int)(v_stack_m11C));
    v_stack_m148 = v_stack_mE8;
    v_stack_m150 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m128));
    v_stack_m158 = (unsigned int)((unsigned int)(a5));
    v_stack_m160 = result;
    v_stack_m168 = (unsigned __int8)(v_stack_m136);
    result = PpmExitCoordinatedIdle(0, *(unsigned __int64 *)(a1 + 34880) + 1032, v_stack_m138, 0);
    if ((unsigned __int8)(v_stack_m136) == 0) goto loc_002D0DD5;
loc_002D0CA7:
    v_r14 = 0;
loc_002D0CB2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 1032 + 4))) != 0) goto loc_002D11D1;
    if (v_stack_m131 != 0) goto loc_002D11F3;
loc_002D0CC6:
    result = PpmUnlockProcessors(*(unsigned __int64 *)(a1 + 34880) + 336, *(unsigned __int64 *)(a1 + 34880) + 336, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 1032 + 4)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1032 + 16));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 3)) != 0) goto loc_002D11FF;
loc_002D0CE3:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 64) = (unsigned __int8)(v_stack_m136);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 60) = 0;
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 34880) + 336, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 34880) + 1032 + 4)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 1032 + 16));
    v_rsp = (v_rsp) + (328);
    return result;
loc_002D0D0F:
    v_stack_p20 = (unsigned int)((unsigned int)(a5));
    v_stack_p50 = 1;
    result = PpmEnterCoordinatedIdle((unsigned int)(*(unsigned int *)(result + 4)), *(unsigned __int64 *)(result + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 0);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != -1) goto loc_002D10F7;
loc_002D0D3C:
    result = PpmEventEnterIdleState((unsigned int)((unsigned int)((unsigned int)(v_stack_p58))), *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 34880) + 56), *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 717), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 34880) + 688));
    v_r10 = 0;
    if (a8 != 0) goto loc_002D1101;
loc_002D0D6B:
    if (v_stack_p54 == 0) goto loc_002D0D99;
    result = KeDeepSleepProcessor((unsigned int)((unsigned int)((unsigned int)(v_stack_p58))), *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 34880) + 56), *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 717), 2);
    v_r10 = 0;
    v_stack_p51 = (unsigned __int8)(result);
loc_002D0D99:
loc_002D0DD5:
    v_stack_p20 = *(unsigned __int64 *)(v_r14 + 16);
    result = guard_dispatch_icall(v_stack_mF8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m130))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(*(unsigned int *)(v_r14 + 4)));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == -1) goto loc_002D0CA7;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != (*(unsigned int *)(v_rip + 11773357))) goto loc_002D0CA7;
    if ((*(unsigned int *)(a1 + 35104)) < 2) goto loc_002D0CA7;
    a1 = 0;
    result = HvlSetPlatformIdleState(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m130))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(*(unsigned int *)(v_r14 + 4)));
    goto loc_002D0CA7;
loc_002D0E2A:
    if ((*(unsigned __int8 *)(v_rip + 13589589)) != 0) goto loc_002D0E91;
    goto loc_002D0C54;
loc_002D0E53:
    a3 = 0;
    result = PpmIdleUpdateConcurrency((unsigned int)(v_stack_m130), result, a3, 1);
    v_r11 = 0;
    if (*(unsigned __int64 *)(a1 + 35328) == 0) goto loc_002D0BD8;
    a3 = 0;
    result = PpmIdleUpdateConcurrency(*(unsigned __int64 *)(a1 + 35328), result, a3, v_r11 + 1);
    v_r11 = 0;
    goto loc_002D0BD8;
loc_002D0E91:
    if ((*(unsigned __int8 *)(v_stack_m100 + 1393)) == ((unsigned __int8)(*(unsigned __int64 *)(a1 + 35328)))) goto loc_002D11BD;
    if ((*(unsigned int *)(v_rip + 13590124)) != ((unsigned int)(*(unsigned __int64 *)(a1 + 35328)))) goto loc_002D0EF3;
loc_002D0EB6:
    a3 = 0;
    result = KiCancelClockTimer(0, a3 + 5, a3, v_r11 + 1);
    result = 0;
    if ((*(unsigned int *)(v_rip + 13590099)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, v_r11 + 1);
    }
loc_002D0EE3:
    *(unsigned __int64 *)(a1 + 34928) = -1;
    goto loc_002D0C54;
loc_002D0EF3:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), a2, a3, v_r11 + 1);
    goto loc_002D0EB6;
loc_002D0FEB:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 715)) != ((unsigned __int8)(a2))) goto loc_002D0AE9;
    if ((*(unsigned __int8 *)((unsigned __int8)(v_cr8) + 1397)) == ((unsigned __int8)(a2))) goto loc_002D0AEC;
    goto loc_002D0AE9;
loc_002D100B:
    goto loc_002D0B0C;
loc_002D1015:
    goto loc_002D0B19;
loc_002D1023:
    result = ((*(unsigned __int8 *)(v_stack_m100 + 1394)) == 0) ? 1 : 0;
    *(unsigned __int8 *)(a1 + 34941) = (unsigned __int8)(result);
    result = PpmIdleSetSynchronizationState(a1 + 34956, (unsigned __int8)((unsigned __int8)(v_cr8)), a3, v_r11 + 1);
    goto loc_002D0B3C;
loc_002D104A:
    if ((*(unsigned __int8 *)(v_rip + 13589031)) == 0) goto loc_002D0B61;
loc_002D1069:
    result = PpmIdleUpdateConcurrency((unsigned int)(v_stack_m130), (unsigned __int8)(result), 1, 1);
    if (*(unsigned __int64 *)(a1 + 35328) == 0) goto loc_002D0B78;
    result = PpmIdleUpdateConcurrency(*(unsigned __int64 *)(a1 + 35328), (unsigned __int8)(result), 1, 1);
    goto loc_002D0B78;
loc_002D10A3:
    v_stack_p20 = *(unsigned __int64 *)(1 + 16);
    result = guard_dispatch_icall(v_stack_mF8, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_cr8)), (unsigned int)(*(unsigned int *)(1 + 4)));
    goto loc_002D0BA1;
loc_002D10CD:
    if (((unsigned int)(v_cr8)) != (*(unsigned int *)(v_rip + 11772641))) goto loc_002D0BAA;
    if ((*(unsigned int *)(a1 + 35104)) < 2) goto loc_002D0BAA;
    result = HvlSetPlatformIdleState(2 - 1, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_cr8)), (unsigned int)(*(unsigned int *)(1 + 4)));
    goto loc_002D0BAA;
loc_002D10F7:
    goto loc_002D0D3C;
loc_002D1101:
    a2 = (unsigned __int8)((v_stack_p53) + (3));
    result = PpmIdleSetSynchronizationState(a1 + 34956, a2, (unsigned int)((unsigned int)(v_cr8)), (unsigned int)(*(unsigned int *)(1 + 4)));
    goto loc_002D0D6B;
loc_002D1142:
    a2 = 0;
    result = PpmIdleSetSynchronizationState(a1 + 34956, a2, (unsigned int)((unsigned int)(v_cr8)), (unsigned int)(*(unsigned int *)(1 + 4)));
    v_stack_p20 = a1;
    result = KeBugCheckEx(160, (unsigned int)(0x702ULL), (unsigned int)((unsigned int)(v_cr8)), (unsigned __int8)(result));
loc_002D1188:
    if ((*(unsigned int *)((unsigned __int8)(result) + 4)) <= 0) goto loc_002D0C17;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 65))) >= 5) goto loc_002D0C1B;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 65)) + (160));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 65) = (unsigned __int8)(result);
    goto loc_002D0C1B;
loc_002D11B3:
loc_002D11BD:
    a3 = 0;
    result = KiCancelClockTimer(a1, a3 + 5, a3, (unsigned __int8)(result));
    goto loc_002D0EE3;
loc_002D11D1:
    a3 = (unsigned int)((a3) - 1);
    a2 = (a3 + 5) * ((unsigned int)(*(unsigned int *)((unsigned __int8)(result) + a3 * 4)));
    *(unsigned int *)(a2 + *(unsigned __int64 *)(v_rip + 13588728) * 1 + 416) = (unsigned int)((unsigned __int8)(result));
    goto loc_002D0CB2;
loc_002D11F3:
    goto loc_002D0CC6;
loc_002D11FF:
    v_stack_p28 = 1;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p74));
    result = PpmTraceExitLatency((unsigned int)(*(unsigned int *)((unsigned __int8)(result) + a3 * 4)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m130))), (unsigned int)((unsigned int)(v_stack_p60)), (unsigned __int8)(result));
    a1 = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34880) + 3) = 0;
    goto loc_002D0CE3;
}
```

## 5. (Beta) C Style

```c
int64_t PpmIdleExecuteTransition(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, uint64_t Arg7, uint8_t Arg8, uint8_t Arg9, uint8_t Arg10, int64_t Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m114;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint8_t v_stack_m131;
    uint8_t v_stack_m132;
    uint8_t v_stack_m133;
    uint8_t v_stack_m134;
    uint8_t v_stack_m135;
    uint8_t v_stack_m136;
    uint8_t v_stack_m137;
    uint8_t v_stack_m138;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint8_t v_stack_m150;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint8_t v_stack_m168;
    uint64_t v_stack_m58;
    uint64_t v_stack_m88;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p50;
    uint8_t v_stack_p51;
    uint8_t v_stack_p53;
    uint8_t v_stack_p54;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p74;

    local_rsp = (local_rsp) - (328);
    result = (*(uint64_t *)(v_rip + 0xB39D04)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m120 = Arg3;
    Arg2 = 0;
    v_stack_m130 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m128 = Arg11;
    v_stack_mF0 = Arg4;
    result = memset(v_stack_mE8, Arg2, 136, Arg4);
    Arg2 = 0;
    Arg1 = (v_stack_mE8) * ((uint32_t)(Arg2));
    v_stack_m108 = 0;
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x8840));
    v_stack_mF8 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x298);
    v_stack_m137 = 0;
    v_stack_m134 = 0;
    *(uint8_t *)(v_stack_m128) = 0;
    v_stack_m133 = 0;
    v_stack_m132 = 0;
    v_stack_m138 = 0;
    v_stack_m108 = 11;
    v_stack_m11C = 130;
    v_stack_m100 = Arg1;
    v_stack_m131 = 0;
    if (Arg8 != 0) goto loc_002D0FEB;
loc_002D0AE9:
loc_002D0AEC:
    v_stack_m135 = 0;
    v_stack_m136 = 0;
    result = KeIsEmptyAffinityEx(*(uint64_t *)(arg1 + 0x8840) + 336, Arg2, 136, Arg4);
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_002D100B;
loc_002D0B0C:
    if (Arg10 != 0) goto loc_002D1015;
loc_002D0B19:
    *(uint32_t *)(arg1 + 0x8880) = (uint32_t)((uint32_t)(v_stack_m130));
    *(uint8_t *)(arg1 + 0x887C) = 0;
    if (Arg8 != 0) goto loc_002D1023;
loc_002D0B3C:
    if ((*(uint8_t *)(v_stack_m100 + 0x571)) == 0) goto loc_002D104A;
loc_002D0B61:
    if (*(uint64_t *)(arg1 + 0x89F8) != 0) goto loc_002D1069;
loc_002D0B78:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x1C) = (uint32_t)((uint32_t)(v_stack_m130));
    result = PpmEndActiveTimeAccumulation(Arg1, Arg6, 136, 1);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x258) != 0) goto loc_002D10A3;
loc_002D0BA1:
    if (((uint32_t)((uint32_t)(Arg3))) != -1) goto loc_002D10CD;
loc_002D0BAA:
    if (!sign_flag) goto loc_002D0D0F;
loc_002D0BB7:
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg6, 136, 1);
    result = PpmBeginActiveTimeAccumulation(0, result, 136, 1);
    local_r11 = 0;
    if (*(uint64_t *)(arg1 + 0x89F8) != 0) goto loc_002D0E53;
loc_002D0BD8:
    result = (result) - (Arg6);
    *(uint64_t *)(arg1 + 0x8850) = result;
    if (Arg8 != 0) goto loc_002D1142;
    if ((*(uint64_t *)(arg1 + 0x8850)) < (*(uint64_t *)(v_rip + 0xC3E10D))) goto loc_002D1188;
loc_002D0C17:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x41) = 0;
loc_002D0C1B:
    if (Arg10 != 0) goto loc_002D11B3;
    result = guard_dispatch_icall(1, result, 136, 1);
    Arg1 = 0;
    if (v_stack_m132 != 0) goto loc_002D0E2A;
loc_002D0C54:
    v_stack_m140 = (uint32_t)((uint32_t)(v_stack_m11C));
    v_stack_m148 = v_stack_mE8;
    v_stack_m150 = (uint8_t)(*(uint8_t *)(v_stack_m128));
    v_stack_m158 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m160 = result;
    v_stack_m168 = (uint8_t)(v_stack_m136);
    result = PpmExitCoordinatedIdle(0, *(uint64_t *)(arg1 + 0x8840) + 1032, v_stack_m138, 0);
    if ((uint8_t)(v_stack_m136) == 0) goto loc_002D0DD5;
loc_002D0CA7:
    local_r14 = 0;
loc_002D0CB2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x408 + 0x4))) != 0) goto loc_002D11D1;
    if (v_stack_m131 != 0) goto loc_002D11F3;
loc_002D0CC6:
    result = PpmUnlockProcessors(*(uint64_t *)(arg1 + 0x8840) + 336, *(uint64_t *)(arg1 + 0x8840) + 336, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x408 + 0x4)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x408 + 0x10));
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3)) != 0) goto loc_002D11FF;
loc_002D0CE3:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x40) = (uint8_t)(v_stack_m136);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3C) = 0;
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x8840) + 336, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x408 + 0x4)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x408 + 0x10));
    local_rsp = (local_rsp) + (328);
    return result;
loc_002D0D0F:
    v_stack_p20 = (uint32_t)((uint32_t)(Arg5));
    v_stack_p50 = 1;
    result = PpmEnterCoordinatedIdle((uint32_t)(*(uint32_t *)(result + 0x4)), *(uint64_t *)(result + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 0);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != -1) goto loc_002D10F7;
loc_002D0D3C:
    result = PpmEventEnterIdleState((uint32_t)((uint32_t)((uint32_t)(v_stack_p58))), *(uint16_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x38), *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x2CD), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x2B0));
    local_r10 = 0;
    if (Arg8 != 0) goto loc_002D1101;
loc_002D0D6B:
    if (v_stack_p54 == 0) goto loc_002D0D99;
    result = KeDeepSleepProcessor((uint32_t)((uint32_t)((uint32_t)(v_stack_p58))), *(uint16_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x38), *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x2CD), 2);
    local_r10 = 0;
    v_stack_p51 = (uint8_t)(result);
loc_002D0D99:
loc_002D0DD5:
    v_stack_p20 = *(uint64_t *)(local_r14 + 0x10);
    result = guard_dispatch_icall(v_stack_mF8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m130))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(*(uint32_t *)(local_r14 + 0x4)));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == -1) goto loc_002D0CA7;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != (*(uint32_t *)(v_rip + 0xB3A5AD))) goto loc_002D0CA7;
    if ((*(uint32_t *)(arg1 + 0x8920)) < 2) goto loc_002D0CA7;
    Arg1 = 0;
    result = HvlSetPlatformIdleState(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m130))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(*(uint32_t *)(local_r14 + 0x4)));
    goto loc_002D0CA7;
loc_002D0E2A:
    if ((*(uint8_t *)(v_rip + 0xCF5C55)) != 0) goto loc_002D0E91;
    goto loc_002D0C54;
loc_002D0E53:
    Arg3 = 0;
    result = PpmIdleUpdateConcurrency((uint32_t)(v_stack_m130), result, Arg3, 1);
    local_r11 = 0;
    if (*(uint64_t *)(arg1 + 0x8A00) == 0) goto loc_002D0BD8;
    Arg3 = 0;
    result = PpmIdleUpdateConcurrency(*(uint64_t *)(arg1 + 0x8A00), result, Arg3, local_r11 + 1);
    local_r11 = 0;
    goto loc_002D0BD8;
loc_002D0E91:
    if ((*(uint8_t *)(v_stack_m100 + 0x571)) == ((uint8_t)(*(uint64_t *)(arg1 + 0x8A00)))) goto loc_002D11BD;
    if ((*(uint32_t *)(v_rip + 0xCF5E6C)) != ((uint32_t)(*(uint64_t *)(arg1 + 0x8A00)))) goto loc_002D0EF3;
loc_002D0EB6:
    Arg3 = 0;
    result = KiCancelClockTimer(0, Arg3 + 5, Arg3, local_r11 + 1);
    result = 0;
    if ((*(uint32_t *)(v_rip + 0xCF5E53)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, local_r11 + 1);
    }
loc_002D0EE3:
    *(uint64_t *)(arg1 + 0x8870) = -1;
    goto loc_002D0C54;
loc_002D0EF3:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), Arg2, Arg3, local_r11 + 1);
    goto loc_002D0EB6;
loc_002D0FEB:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x2CB)) != ((uint8_t)(Arg2))) goto loc_002D0AE9;
    if ((*(uint8_t *)((uint8_t)(v_cr8) + 0x575)) == ((uint8_t)(Arg2))) goto loc_002D0AEC;
    goto loc_002D0AE9;
loc_002D100B:
    goto loc_002D0B0C;
loc_002D1015:
    goto loc_002D0B19;
loc_002D1023:
    result = ((*(uint8_t *)(v_stack_m100 + 0x572)) == 0) ? 1 : 0;
    *(uint8_t *)(arg1 + 0x887D) = (uint8_t)(result);
    result = PpmIdleSetSynchronizationState(Arg1 + 34956, (uint8_t)((uint8_t)(v_cr8)), Arg3, local_r11 + 1);
    goto loc_002D0B3C;
loc_002D104A:
    if ((*(uint8_t *)(v_rip + 0xCF5A27)) == 0) goto loc_002D0B61;
loc_002D1069:
    result = PpmIdleUpdateConcurrency((uint32_t)(v_stack_m130), (uint8_t)(result), 1, 1);
    if (*(uint64_t *)(arg1 + 0x8A00) == 0) goto loc_002D0B78;
    result = PpmIdleUpdateConcurrency(*(uint64_t *)(arg1 + 0x8A00), (uint8_t)(result), 1, 1);
    goto loc_002D0B78;
loc_002D10A3:
    v_stack_p20 = *(uint64_t *)(1 + 0x10);
    result = guard_dispatch_icall(v_stack_mF8, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(v_cr8)), (uint32_t)(*(uint32_t *)(1 + 0x4)));
    goto loc_002D0BA1;
loc_002D10CD:
    if (((uint32_t)(v_cr8)) != (*(uint32_t *)(v_rip + 0xB3A2E1))) goto loc_002D0BAA;
    if ((*(uint32_t *)(arg1 + 0x8920)) < 2) goto loc_002D0BAA;
    result = HvlSetPlatformIdleState(2 - 1, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(v_cr8)), (uint32_t)(*(uint32_t *)(1 + 0x4)));
    goto loc_002D0BAA;
loc_002D10F7:
    goto loc_002D0D3C;
loc_002D1101:
    Arg2 = (uint8_t)((v_stack_p53) + (3));
    result = PpmIdleSetSynchronizationState(Arg1 + 34956, Arg2, (uint32_t)((uint32_t)(v_cr8)), (uint32_t)(*(uint32_t *)(1 + 0x4)));
    goto loc_002D0D6B;
loc_002D1142:
    Arg2 = 0;
    result = PpmIdleSetSynchronizationState(Arg1 + 34956, Arg2, (uint32_t)((uint32_t)(v_cr8)), (uint32_t)(*(uint32_t *)(1 + 0x4)));
    v_stack_p20 = Arg1;
    result = KeBugCheckEx(160, (uint32_t)(0x702ULL), (uint32_t)((uint32_t)(v_cr8)), (uint8_t)(result));
loc_002D1188:
    if ((*(uint32_t *)((uint8_t)(result) + 0x4)) <= 0) goto loc_002D0C17;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x41))) >= 5) goto loc_002D0C1B;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x41)) + (160));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x41) = (uint8_t)(result);
    goto loc_002D0C1B;
loc_002D11B3:
loc_002D11BD:
    Arg3 = 0;
    result = KiCancelClockTimer(Arg1, Arg3 + 5, Arg3, (uint8_t)(result));
    goto loc_002D0EE3;
loc_002D11D1:
    Arg3 = (uint32_t)((Arg3) - 1);
    Arg2 = (Arg3 + 5) * ((uint32_t)(*(uint32_t *)((uint8_t)(result) + Arg3 * 4)));
    *(uint32_t *)(Arg2 + *(uint64_t *)(v_rip + 0xCF58F8) * 1 + 0x1A0) = (uint32_t)((uint8_t)(result));
    goto loc_002D0CB2;
loc_002D11F3:
    goto loc_002D0CC6;
loc_002D11FF:
    v_stack_p28 = 1;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p74));
    result = PpmTraceExitLatency((uint32_t)(*(uint32_t *)((uint8_t)(result) + Arg3 * 4)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m130))), (uint32_t)((uint32_t)(v_stack_p60)), (uint8_t)(result));
    Arg1 = 0;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8840) + 0x3) = 0;
    goto loc_002D0CE3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xD1` | `8` | `R` |
| `Arg1` | `+ 0x6D8` | `16` | `R/W` |
| `Arg1` | `+ 0x6DC` | `8` | `R` |
| `Arg1` | `+ 0x6E6` | `16` | `R` |
| `Arg1` | `+ 0x38E7` | `8` | `R/W` |
| `Arg1` | `+ 0x8840` | `64` | `R` |
| `Arg1` | `+ 0x8850` | `64` | `R` |
| `Arg1` | `+ 0x8850` | `64` | `W` |
| `Arg1` | `+ 0x8870` | `64` | `R/W` |
| `Arg1` | `+ 0x8870` | `64` | `W` |
| `Arg1` | `+ 0x887C` | `8` | `W` |
| `Arg1` | `+ 0x887D` | `8` | `W` |
| `Arg1` | `+ 0x8880` | `32` | `W` |
| `Arg1` | `+ 0x888C` | `64` | `R` |
| `Arg1` | `+ 0x8920` | `32` | `R` |
| `Arg1` | `+ 0x89F8` | `64` | `R` |
| `Arg1` | `+ 0x8A00` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D0A1C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
