# ExpWatchProductTypeWork

- RVA: `0x006FFCA0`–`0x007003BD` (길이 `1,821` bytes)
- VA: `0x00000001406FFCA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF2EC`
- 디코드: `436`개 명령, `1,821/1,821` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x006FFD23` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x006FFD56` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x006FFD82` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x006FFDAF` → [NtOpenKeyEx](../A4/NtOpenKeyEx_function_00A45CC0.md) (function, `0x00A45CC0`)
- `0x006FFDCD` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x006FFDDF` → [NtOpenKeyEx](../A4/NtOpenKeyEx_function_00A45CC0.md) (function, `0x00A45CC0`)
- `0x006FFE00` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x006FFE34` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x006FFE63` → [NtQueryValueKey](../8B/NtQueryValueKey_function_008B2A00.md) (function, `0x008B2A00`)
- `0x006FFE81` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x006FFEA8` → [NtQueryValueKey](../8B/NtQueryValueKey_function_008B2A00.md) (function, `0x008B2A00`)
- `0x006FFFAC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x006FFFC8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006FFFD8` → [CmSizeOfThreadInfo](../../text/66/CmSizeOfThreadInfo_function_0066AB5C.md) (function, `0x0066AB5C`)
- `0x006FFFF6` → [_chkstk](../../text/6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x0070000A` → [CmInitializeThreadInfo](../../text/66/CmInitializeThreadInfo_function_0066AB44.md) (function, `0x0066AB44`)
- `0x00700017` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x00700049` → [NtSetValueKey](../84/NtSetValueKey_function_00844EA0.md) (function, `0x00844EA0`)
- `0x00700065` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00700094` → [NtSetValueKey](../84/NtSetValueKey_function_00844EA0.md) (function, `0x00844EA0`)
- `0x007000B9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007000D7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00700106` → [NtSetValueKey](../84/NtSetValueKey_function_00844EA0.md) (function, `0x00844EA0`)
- `0x00700122` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00700151` → [NtSetValueKey](../84/NtSetValueKey_function_00844EA0.md) (function, `0x00844EA0`)
- `0x00700176` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0070017C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0070018C` → [NtDeleteValueKey](../84/NtDeleteValueKey_function_00848770.md) (function, `0x00848770`)
- `0x007001A6` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00700203` → [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) (function, `0x009DC6B0`)
- `0x0070023A` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x0070027C` → [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) (function, `0x009DC6B0`)
- `0x0070029B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007002A8` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x007002C7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00700312` → [PsCreateSystemThreadEx](../9E/PsCreateSystemThreadEx_function_009ED120.md) (function, `0x009ED120`)
- `0x0070031F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0070035B` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00700367` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00700378` → [NtFlushKey](../A8/NtFlushKey_function_00A8A030.md) (function, `0x00A8A030`)
- `0x00700382` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00700391` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006FFCCB` → RVA `0x00E0A740` (`.data`; read)
- `0x006FFCDC` → RVA `0x00B4AD78` (`PAGE`; read)
- `0x006FFD4A` → RVA `0x00EFEE30` (`.data`; read)
- `0x006FFD90` → RVA `0x00EFEE18` (`.data`; read)
- `0x006FFE06` → RVA `0x00EF0139` (`.data`; read)
- `0x006FFE1C` → RVA `0x00EFEE18` (`.data`; write)
- `0x006FFE29` → RVA `0x00B4AD80` (`PAGE`; read)
- `0x006FFEB9` → RVA `0x00B4AD88` (`PAGE`; read)
- `0x006FFEE1` → RVA `0x00B4AD90` (`PAGE`; read)
- `0x006FFF0F` → RVA `0x00EFEE00` (`.data`; read)
- `0x006FFF16` → RVA `0x00B4AD98` (`PAGE`; read)
- `0x006FFFB8` → RVA `0x00FD8488` (`PAGEDATA`; read)
- `0x007000BF` → RVA `0x00E61EA8` (`.data`; read)
- `0x007000CA` → RVA `0x00B4ADA0` (`PAGE`; read)
- `0x007001B8` → RVA `0x00EFEE08` (`.data`; read)
- `0x007001DE` → RVA `0x00EFEDC0` (`.data`; read)
- `0x007001F2` → RVA `0x00EFEDE0` (`.data`; read)
- `0x007002F9` → RVA `0x007C5AF0` (`ExpExpirationThread`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x006FFD23` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x006FFD56` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x006FFD82` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x006FFDCD` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x006FFE00` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x006FFE34` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x006FFE81` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x006FFFAC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x006FFFC8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x006FFFD8` → [CmSizeOfThreadInfo](../../text/66/CmSizeOfThreadInfo_function_0066AB5C.md) (`PAGE` → `.text`)
  - `0x006FFFF6` → [_chkstk](../../text/6B/_chkstk_function_006BA960.md) (`PAGE` → `.text`)
  - `0x0070000A` → [CmInitializeThreadInfo](../../text/66/CmInitializeThreadInfo_function_0066AB44.md) (`PAGE` → `.text`)
  - `0x00700065` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x007000B9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007000D7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00700122` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x00700176` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0070017C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007001A6` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0070023A` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x0070029B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007002A8` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x007002C7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0070031F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0070035B` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00700367` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00700391` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006FFCA0  40 55                           push rbp
006FFCA2  41 54                           push r12
006FFCA4  41 55                           push r13
006FFCA6  41 56                           push r14
006FFCA8  41 57                           push r15
006FFCAA  48 81 EC 20 01 00 00            sub rsp, 0x120
006FFCB1  48 8D 6C 24 60                  lea rbp, [rsp + 0x60]
006FFCB6  48 89 9D F0 00 00 00            mov qword ptr [rbp + 0xf0], rbx
006FFCBD  48 89 B5 F8 00 00 00            mov qword ptr [rbp + 0xf8], rsi
006FFCC4  48 89 BD 00 01 00 00            mov qword ptr [rbp + 0x100], rdi
006FFCCB  48 8B 05 6E AA 70 00            mov rax, qword ptr [rip + 0x70aa6e]
006FFCD2  48 33 C5                        xor rax, rbp
006FFCD5  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
006FFCDC  48 8B 15 95 B0 44 00            mov rdx, qword ptr [rip + 0x44b095]
006FFCE3  48 8D 4D 78                     lea rcx, [rbp + 0x78]
006FFCE7  45 33 ED                        xor r13d, r13d
006FFCEA  0F 57 C0                        xorps xmm0, xmm0
006FFCED  0F 57 C9                        xorps xmm1, xmm1
006FFCF0  44 89 6D 4C                     mov dword ptr [rbp + 0x4c], r13d
006FFCF4  41 B4 01                        mov r12b, 1
006FFCF7  44 89 6D 64                     mov dword ptr [rbp + 0x64], r13d
006FFCFB  0F 11 45 78                     movups xmmword ptr [rbp + 0x78], xmm0
006FFCFF  4C 89 6D 38                     mov qword ptr [rbp + 0x38], r13
006FFD03  41 8A F5                        mov sil, r13b
006FFD06  0F 11 4D 18                     movups xmmword ptr [rbp + 0x18], xmm1
006FFD0A  44 89 6D 10                     mov dword ptr [rbp + 0x10], r13d
006FFD0E  41 8A DD                        mov bl, r13b
006FFD11  44 88 65 00                     mov byte ptr [rbp], r12b
006FFD15  45 8B FD                        mov r15d, r13d
006FFD18  4C 89 6D 28                     mov qword ptr [rbp + 0x28], r13
006FFD1C  45 8B F5                        mov r14d, r13d
006FFD1F  4C 89 6D 30                     mov qword ptr [rbp + 0x30], r13
006FFD23  E8 58 AA D2 FF                  call 0x14042a780
006FFD28  48 8D 45 78                     lea rax, [rbp + 0x78]
006FFD2C  C7 45 48 30 00 00 00            mov dword ptr [rbp + 0x48], 0x30
006FFD33  0F 57 C0                        xorps xmm0, xmm0
006FFD36  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
006FFD3A  45 33 C0                        xor r8d, r8d
006FFD3D  4C 89 6D 50                     mov qword ptr [rbp + 0x50], r13
006FFD41  33 D2                           xor edx, edx
006FFD43  C7 45 60 40 02 00 00            mov dword ptr [rbp + 0x60], 0x240
006FFD4A  48 8D 0D DF F0 7F 00            lea rcx, [rip + 0x7ff0df]
006FFD51  F3 0F 7F 45 68                  movdqu xmmword ptr [rbp + 0x68], xmm0
006FFD56  E8 D5 04 B1 FF                  call 0x140210230
006FFD5B  48 8B F8                        mov rdi, rax
006FFD5E  41 8D 4D 11                     lea ecx, [r13 + 0x11]
006FFD62  33 C0                           xor eax, eax
006FFD64  F0 48 0F B1 0D C3 F0 7F 00      lock cmpxchg qword ptr [rip + 0x7ff0c3], rcx
006FFD6D  74 18                           je 0x1406ffd87
006FFD6F  4C 8D 0D BA F0 7F 00            lea r9, [rip + 0x7ff0ba]
006FFD76  4C 8B C7                        mov r8, rdi
006FFD79  33 D2                           xor edx, edx
006FFD7B  48 8D 0D AE F0 7F 00            lea rcx, [rip + 0x7ff0ae]
006FFD82  E8 C5 06 B1 FF                  call 0x14021044c
006FFD87  48 85 FF                        test rdi, rdi
006FFD8A  74 04                           je 0x1406ffd90
006FFD8C  44 88 67 0A                     mov byte ptr [rdi + 0xa], r12b
006FFD90  4C 39 2D 81 F0 7F 00            cmp qword ptr [rip + 0x7ff081], r13
006FFD97  0F 84 87 05 00 00               je 0x140700324
006FFD9D  BB 1F 00 02 00                  mov ebx, 0x2001f
006FFDA2  4C 8D 45 48                     lea r8, [rbp + 0x48]
006FFDA6  8B D3                           mov edx, ebx
006FFDA8  48 8D 4D 28                     lea rcx, [rbp + 0x28]
006FFDAC  45 33 C9                        xor r9d, r9d
006FFDAF  E8 0C 5F 34 00                  call 0x140a45cc0
006FFDB4  BF 9A 00 00 C0                  mov edi, 0xc000009a
006FFDB9  3B C7                           cmp eax, edi
006FFDBB  75 2B                           jne 0x1406ffde8
006FFDBD  48 C7 45 08 80 69 67 FF         mov qword ptr [rbp + 8], 0xffffffffff676980
006FFDC5  4C 8D 45 08                     lea r8, [rbp + 8]
006FFDC9  33 D2                           xor edx, edx
006FFDCB  33 C9                           xor ecx, ecx
006FFDCD  E8 7E 97 B0 FF                  call 0x140209550
006FFDD2  45 33 C9                        xor r9d, r9d
006FFDD5  4C 8D 45 48                     lea r8, [rbp + 0x48]
006FFDD9  8B D3                           mov edx, ebx
006FFDDB  48 8D 4D 28                     lea rcx, [rbp + 0x28]
006FFDDF  E8 DC 5E 34 00                  call 0x140a45cc0
006FFDE4  3B C7                           cmp eax, edi
006FFDE6  74 DD                           je 0x1406ffdc5
006FFDE8  85 C0                           test eax, eax
006FFDEA  79 1A                           jns 0x1406ffe06
006FFDEC  45 33 C9                        xor r9d, r9d
006FFDEF  44 8B C0                        mov r8d, eax
006FFDF2  B9 9A 00 00 00                  mov ecx, 0x9a
006FFDF7  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
006FFDFC  41 8D 51 0D                     lea edx, [r9 + 0xd]
006FFE00  E8 5B D8 DF FF                  call 0x1404fd660
006FFE05  CC                              int3
006FFE06  44 38 2D 2C 03 7F 00            cmp byte ptr [rip + 0x7f032c], r13b
006FFE0D  4C 8B 3D 04 F0 7F 00            mov r15, qword ptr [rip + 0x7ff004]
006FFE14  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
006FFE18  4C 89 7D 40                     mov qword ptr [rbp + 0x40], r15
006FFE1C  48 89 05 F5 EF 7F 00            mov qword ptr [rip + 0x7feff5], rax
006FFE23  0F 85 83 03 00 00               jne 0x1407001ac
006FFE29  48 8B 15 50 AF 44 00            mov rdx, qword ptr [rip + 0x44af50]
006FFE30  48 8D 4D 18                     lea rcx, [rbp + 0x18]
006FFE34  E8 47 A9 D2 FF                  call 0x14042a780
006FFE39  48 8B 0D D8 EF 7F 00            mov rcx, qword ptr [rip + 0x7fefd8]
006FFE40  48 8D 45 10                     lea rax, [rbp + 0x10]
006FFE44  BF 22 00 00 00                  mov edi, 0x22
006FFE49  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006FFE4E  4C 8D 8D 88 00 00 00            lea r9, [rbp + 0x88]
006FFE55  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
006FFE59  48 8D 55 18                     lea rdx, [rbp + 0x18]
006FFE5D  8D 5F E0                        lea ebx, [rdi - 0x20]
006FFE60  44 8B C3                        mov r8d, ebx
006FFE63  E8 98 2B 1B 00                  call 0x1408b2a00
006FFE68  BE 9A 00 00 C0                  mov esi, 0xc000009a
006FFE6D  3B C6                           cmp eax, esi
006FFE6F  75 40                           jne 0x1406ffeb1
006FFE71  48 C7 45 08 80 69 67 FF         mov qword ptr [rbp + 8], 0xffffffffff676980
006FFE79  4C 8D 45 08                     lea r8, [rbp + 8]
006FFE7D  33 D2                           xor edx, edx
006FFE7F  33 C9                           xor ecx, ecx
006FFE81  E8 CA 96 B0 FF                  call 0x140209550
006FFE86  48 8B 0D 8B EF 7F 00            mov rcx, qword ptr [rip + 0x7fef8b]
006FFE8D  48 8D 45 10                     lea rax, [rbp + 0x10]
006FFE91  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006FFE96  4C 8D 8D 88 00 00 00            lea r9, [rbp + 0x88]
006FFE9D  44 8B C3                        mov r8d, ebx
006FFEA0  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
006FFEA4  48 8D 55 18                     lea rdx, [rbp + 0x18]
006FFEA8  E8 53 2B 1B 00                  call 0x1408b2a00
006FFEAD  3B C6                           cmp eax, esi
006FFEAF  74 C8                           je 0x1406ffe79
006FFEB1  85 C0                           test eax, eax
006FFEB3  0F 88 E6 00 00 00               js 0x1406fff9f
006FFEB9  48 8B 05 C8 AE 44 00            mov rax, qword ptr [rip + 0x44aec8]
006FFEC0  4C 8D 85 94 00 00 00            lea r8, [rbp + 0x94]
006FFEC7  4C 2B C0                        sub r8, rax
006FFECA  0F B7 08                        movzx ecx, word ptr [rax]
006FFECD  42 0F B7 14 00                  movzx edx, word ptr [rax + r8]
006FFED2  2B CA                           sub ecx, edx
006FFED4  75 07                           jne 0x1406ffedd
006FFED6  48 03 C3                        add rax, rbx
006FFED9  85 D2                           test edx, edx
006FFEDB  75 ED                           jne 0x1406ffeca
006FFEDD  85 C9                           test ecx, ecx
006FFEDF  74 2B                           je 0x1406fff0c
006FFEE1  48 8B 05 A8 AE 44 00            mov rax, qword ptr [rip + 0x44aea8]
006FFEE8  4C 8D 85 94 00 00 00            lea r8, [rbp + 0x94]
006FFEEF  4C 2B C0                        sub r8, rax
006FFEF2  0F B7 08                        movzx ecx, word ptr [rax]
006FFEF5  42 0F B7 14 00                  movzx edx, word ptr [rax + r8]
006FFEFA  2B CA                           sub ecx, edx
006FFEFC  75 07                           jne 0x1406fff05
006FFEFE  48 03 C3                        add rax, rbx
006FFF01  85 D2                           test edx, edx
006FFF03  75 ED                           jne 0x1406ffef2
006FFF05  45 8A D5                        mov r10b, r13b
006FFF08  85 C9                           test ecx, ecx
006FFF0A  75 03                           jne 0x1406fff0f
006FFF0C  45 8A D4                        mov r10b, r12b
006FFF0F  48 8B 15 EA EE 7F 00            mov rdx, qword ptr [rip + 0x7feeea]
006FFF16  48 8B 05 7B AE 44 00            mov rax, qword ptr [rip + 0x44ae7b]
006FFF1D  48 83 C2 0C                     add rdx, 0xc
006FFF21  4C 8B CA                        mov r9, rdx
006FFF24  4C 2B C8                        sub r9, rax
006FFF27  0F B7 08                        movzx ecx, word ptr [rax]
006FFF2A  46 0F B7 04 08                  movzx r8d, word ptr [rax + r9]
006FFF2F  41 2B C8                        sub ecx, r8d
006FFF32  75 08                           jne 0x1406fff3c
006FFF34  48 03 C3                        add rax, rbx
006FFF37  45 85 C0                        test r8d, r8d
006FFF3A  75 EB                           jne 0x1406fff27
006FFF3C  85 C9                           test ecx, ecx
006FFF3E  74 2F                           je 0x1406fff6f
006FFF40  45 84 D2                        test r10b, r10b
006FFF43  74 2A                           je 0x1406fff6f
006FFF45  48 8B 0D B4 EE 7F 00            mov rcx, qword ptr [rip + 0x7feeb4]
006FFF4C  45 8A E5                        mov r12b, r13b
006FFF4F  0F 10 85 88 00 00 00            movups xmm0, xmmword ptr [rbp + 0x88]
006FFF56  0F 11 01                        movups xmmword ptr [rcx], xmm0
006FFF59  0F 10 8D 98 00 00 00            movups xmm1, xmmword ptr [rbp + 0x98]
006FFF60  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
006FFF64  0F B7 85 A8 00 00 00            movzx eax, word ptr [rbp + 0xa8]
006FFF6B  66 89 41 20                     mov word ptr [rcx + 0x20], ax
006FFF6F  48 8D 8D 94 00 00 00            lea rcx, [rbp + 0x94]
006FFF76  48 2B CA                        sub rcx, rdx
006FFF79  0F B7 02                        movzx eax, word ptr [rdx]
006FFF7C  66 3B 04 0A                     cmp ax, word ptr [rdx + rcx]
006FFF80  75 0D                           jne 0x1406fff8f
006FFF82  48 03 D3                        add rdx, rbx
006FFF85  66 85 C0                        test ax, ax
006FFF88  75 EF                           jne 0x1406fff79
006FFF8A  41 8B C5                        mov eax, r13d
006FFF8D  EB 05                           jmp 0x1406fff94
006FFF8F  1B C0                           sbb eax, eax
006FFF91  83 C8 01                        or eax, 1
006FFF94  F7 D8                           neg eax
006FFF96  1A C0                           sbb al, al
006FFF98  44 22 E0                        and r12b, al
006FFF9B  44 88 65 00                     mov byte ptr [rbp], r12b
006FFF9F  48 8B 15 72 EE 7F 00            mov rdx, qword ptr [rip + 0x7fee72]
006FFFA6  41 B8 02 00 00 C0               mov r8d, 0xc0000002
006FFFAC  E8 3F E2 BF FF                  call 0x1402fe1f0
006FFFB1  48 8B 88 68 03 00 00            mov rcx, qword ptr [rax + 0x368]
006FFFB8  48 8B 05 C9 84 8D 00            mov rax, qword ptr [rip + 0x8d84c9]
006FFFBF  48 85 C0                        test rax, rax
006FFFC2  0F 84 CB 01 00 00               je 0x140700193
006FFFC8  E8 03 AB FB FF                  call 0x1406baad0
006FFFCD  44 8B C0                        mov r8d, eax
006FFFD0  85 C0                           test eax, eax
006FFFD2  0F 88 BB 01 00 00               js 0x140700193
006FFFD8  E8 7F AB F6 FF                  call 0x14066ab5c
006FFFDD  8B C8                           mov ecx, eax
006FFFDF  48 8D 41 0F                     lea rax, [rcx + 0xf]
006FFFE3  48 3B C1                        cmp rax, rcx
006FFFE6  77 0A                           ja 0x1406ffff2
006FFFE8  48 B8 F0 FF FF FF FF FF FF 0F   movabs rax, 0xffffffffffffff0
006FFFF2  48 83 E0 F0                     and rax, 0xfffffffffffffff0
006FFFF6  E8 65 A9 FB FF                  call 0x1406ba960
006FFFFB  48 2B E0                        sub rsp, rax
006FFFFE  4C 8D 74 24 60                  lea r14, [rsp + 0x60]
00700003  49 8B CE                        mov rcx, r14
00700006  4C 89 75 30                     mov qword ptr [rbp + 0x30], r14
0070000A  E8 35 AB F6 FF                  call 0x14066ab44
0070000F  BF 01 00 00 00                  mov edi, 1
00700014  40 8A CF                        mov cl, dil
00700017  E8 C8 4A 2B 00                  call 0x1409b4ae4
0070001C  4C 8B 0D DD ED 7F 00            mov r9, qword ptr [rip + 0x7feddd]
00700023  48 8D 55 18                     lea rdx, [rbp + 0x18]
00700027  45 33 C0                        xor r8d, r8d
0070002A  40 8A F7                        mov sil, dil
0070002D  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
00700031  49 8D 49 0C                     lea rcx, [r9 + 0xc]
00700035  45 8B 49 04                     mov r9d, dword ptr [r9 + 4]
00700039  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0070003D  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00700042  48 8B 0D CF ED 7F 00            mov rcx, qword ptr [rip + 0x7fedcf]
00700049  E8 52 4E 14 00                  call 0x140844ea0
0070004E  3D 9A 00 00 C0                  cmp eax, 0xc000009a
00700053  75 4B                           jne 0x1407000a0
00700055  48 C7 45 08 80 69 67 FF         mov qword ptr [rbp + 8], 0xffffffffff676980
0070005D  4C 8D 45 08                     lea r8, [rbp + 8]
00700061  33 D2                           xor edx, edx
00700063  33 C9                           xor ecx, ecx
00700065  E8 E6 94 B0 FF                  call 0x140209550
0070006A  4C 8B 0D 8F ED 7F 00            mov r9, qword ptr [rip + 0x7fed8f]
00700071  48 8D 55 18                     lea rdx, [rbp + 0x18]
00700075  45 33 C0                        xor r8d, r8d
00700078  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
0070007C  49 8D 49 0C                     lea rcx, [r9 + 0xc]
00700080  45 8B 49 04                     mov r9d, dword ptr [r9 + 4]
00700084  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00700088  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0070008D  48 8B 0D 84 ED 7F 00            mov rcx, qword ptr [rip + 0x7fed84]
00700094  E8 07 4E 14 00                  call 0x140844ea0
00700099  3D 9A 00 00 C0                  cmp eax, 0xc000009a
0070009E  74 BD                           je 0x14070005d
007000A0  85 C0                           test eax, eax
007000A2  79 1B                           jns 0x1407000bf
007000A4  44 8B C0                        mov r8d, eax
007000A7  4C 8B CF                        mov r9, rdi
007000AA  BA 11 00 00 00                  mov edx, 0x11
007000AF  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
007000B4  B9 9A 00 00 00                  mov ecx, 0x9a
007000B9  E8 A2 D5 DF FF                  call 0x1404fd660
007000BE  CC                              int3
007000BF  4C 39 2D E2 1D 76 00            cmp qword ptr [rip + 0x761de2], r13
007000C6  48 8D 4D 18                     lea rcx, [rbp + 0x18]
007000CA  48 8B 15 CF AC 44 00            mov rdx, qword ptr [rip + 0x44accf]
007000D1  0F 84 A5 00 00 00               je 0x14070017c
007000D7  E8 A4 A6 D2 FF                  call 0x14042a780
007000DC  4C 8B 0D C5 1D 76 00            mov r9, qword ptr [rip + 0x761dc5]
007000E3  48 8D 55 18                     lea rdx, [rbp + 0x18]
007000E7  45 33 C0                        xor r8d, r8d
007000EA  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
007000EE  49 8D 49 0C                     lea rcx, [r9 + 0xc]
007000F2  45 8B 49 04                     mov r9d, dword ptr [r9 + 4]
007000F6  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007000FA  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
007000FF  48 8B 0D 12 ED 7F 00            mov rcx, qword ptr [rip + 0x7fed12]
00700106  E8 95 4D 14 00                  call 0x140844ea0
0070010B  3D 9A 00 00 C0                  cmp eax, 0xc000009a
00700110  75 4B                           jne 0x14070015d
00700112  48 C7 45 08 80 69 67 FF         mov qword ptr [rbp + 8], 0xffffffffff676980
0070011A  4C 8D 45 08                     lea r8, [rbp + 8]
0070011E  33 D2                           xor edx, edx
00700120  33 C9                           xor ecx, ecx
00700122  E8 29 94 B0 FF                  call 0x140209550
00700127  4C 8B 0D 7A 1D 76 00            mov r9, qword ptr [rip + 0x761d7a]
0070012E  48 8D 55 18                     lea rdx, [rbp + 0x18]
00700132  45 33 C0                        xor r8d, r8d
00700135  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
00700139  49 8D 49 0C                     lea rcx, [r9 + 0xc]
0070013D  45 8B 49 04                     mov r9d, dword ptr [r9 + 4]
00700141  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00700145  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0070014A  48 8B 0D C7 EC 7F 00            mov rcx, qword ptr [rip + 0x7fecc7]
00700151  E8 4A 4D 14 00                  call 0x140844ea0
00700156  3D 9A 00 00 C0                  cmp eax, 0xc000009a
0070015B  74 BD                           je 0x14070011a
0070015D  85 C0                           test eax, eax
0070015F  79 50                           jns 0x1407001b1
00700161  44 8B C0                        mov r8d, eax
00700164  4C 8B CB                        mov r9, rbx
00700167  BA 11 00 00 00                  mov edx, 0x11
0070016C  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00700171  B9 9A 00 00 00                  mov ecx, 0x9a
00700176  E8 E5 D4 DF FF                  call 0x1404fd660
0070017B  CC                              int3
0070017C  E8 FF A5 D2 FF                  call 0x14042a780
00700181  48 8B 0D 90 EC 7F 00            mov rcx, qword ptr [rip + 0x7fec90]
00700188  48 8D 55 18                     lea rdx, [rbp + 0x18]
0070018C  E8 DF 85 14 00                  call 0x140848770
00700191  EB 1E                           jmp 0x1407001b1
00700193  BA 11 00 00 00                  mov edx, 0x11
00700198  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0070019D  B9 9A 00 00 00                  mov ecx, 0x9a
007001A2  44 8D 4A F0                     lea r9d, [rdx - 0x10]
007001A6  E8 B5 D4 DF FF                  call 0x1404fd660
007001AB  CC                              int3
007001AC  BF 01 00 00 00                  mov edi, 1
007001B1  48 8B 0D 60 EC 7F 00            mov rcx, qword ptr [rip + 0x7fec60]
007001B8  48 8D 05 49 EC 7F 00            lea rax, [rip + 0x7fec49]
007001BF  40 88 7C 24 58                  mov byte ptr [rsp + 0x58], dil
007001C4  45 33 C9                        xor r9d, r9d
007001C7  C7 44 24 50 04 00 00 00         mov dword ptr [rsp + 0x50], 4
007001CF  45 33 C0                        xor r8d, r8d
007001D2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007001D7  33 D2                           xor edx, edx
007001D9  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
007001DE  48 8D 05 DB EB 7F 00            lea rax, [rip + 0x7febdb]
007001E5  C7 44 24 38 05 00 00 10         mov dword ptr [rsp + 0x38], 0x10000005
007001ED  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007001F2  48 8D 05 E7 EB 7F 00            lea rax, [rip + 0x7febe7]
007001F9  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
007001FE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00700203  E8 A8 C4 2D 00                  call 0x1409dc6b0
00700208  8B D8                           mov ebx, eax
0070020A  3D 9A 00 00 C0                  cmp eax, 0xc000009a
0070020F  0F 85 81 00 00 00               jne 0x140700296
00700215  48 C7 45 08 80 69 67 FF         mov qword ptr [rbp + 8], 0xffffffffff676980
0070021D  4C 8D 25 E4 EB 7F 00            lea r12, [rip + 0x7febe4]
00700224  4C 8D 3D 95 EB 7F 00            lea r15, [rip + 0x7feb95]
0070022B  4C 8D 35 AE EB 7F 00            lea r14, [rip + 0x7febae]
00700232  4C 8D 45 08                     lea r8, [rbp + 8]
00700236  33 D2                           xor edx, edx
00700238  33 C9                           xor ecx, ecx
0070023A  E8 11 93 B0 FF                  call 0x140209550
0070023F  48 8B 0D D2 EB 7F 00            mov rcx, qword ptr [rip + 0x7febd2]
00700246  45 33 C9                        xor r9d, r9d
00700249  40 88 7C 24 58                  mov byte ptr [rsp + 0x58], dil
0070024E  45 33 C0                        xor r8d, r8d
00700251  C7 44 24 50 04 00 00 00         mov dword ptr [rsp + 0x50], 4
00700259  33 D2                           xor edx, edx
0070025B  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00700260  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
00700265  C7 44 24 38 05 00 00 10         mov dword ptr [rsp + 0x38], 0x10000005
0070026D  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00700272  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00700277  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0070027C  E8 2F C4 2D 00                  call 0x1409dc6b0
00700281  8B D8                           mov ebx, eax
00700283  3D 9A 00 00 C0                  cmp eax, 0xc000009a
00700288  74 A8                           je 0x140700232
0070028A  4C 8B 75 30                     mov r14, qword ptr [rbp + 0x30]
0070028E  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00700292  44 8A 65 00                     mov r12b, byte ptr [rbp]
00700296  40 84 F6                        test sil, sil
00700299  74 05                           je 0x1407002a0
0070029B  E8 E4 97 4C 00                  call 0x140bc9a84
007002A0  4D 85 F6                        test r14, r14
007002A3  74 08                           je 0x1407002ad
007002A5  49 8B CE                        mov rcx, r14
007002A8  E8 A3 FA D1 FF                  call 0x14041fd50
007002AD  85 DB                           test ebx, ebx
007002AF  79 1C                           jns 0x1407002cd
007002B1  BA 11 00 00 00                  mov edx, 0x11
007002B6  44 8B C3                        mov r8d, ebx
007002B9  B9 9A 00 00 00                  mov ecx, 0x9a
007002BE  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
007002C3  44 8D 4A F3                     lea r9d, [rdx - 0xd]
007002C7  E8 94 D3 DF FF                  call 0x1404fd660
007002CC  CC                              int3
007002CD  44 38 2D 65 FE 7E 00            cmp byte ptr [rip + 0x7efe65], r13b
007002D4  40 8A DE                        mov bl, sil
007002D7  75 4B                           jne 0x140700324
007002D9  45 84 E4                        test r12b, r12b
007002DC  74 46                           je 0x140700324
007002DE  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
007002E3  48 8D 4D 38                     lea rcx, [rbp + 0x38]
007002E7  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
007002EC  B8 6A 02 00 C0                  mov eax, 0xc000026a
007002F1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007002F6  45 33 C9                        xor r9d, r9d
007002F9  48 8D 05 F0 57 0C 00            lea rax, [rip + 0xc57f0]
00700300  45 33 C0                        xor r8d, r8d
00700303  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00700308  BA FF FF 1F 00                  mov edx, 0x1fffff
0070030D  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00700312  E8 09 CE 2E 00                  call 0x1409ed120
00700317  85 C0                           test eax, eax
00700319  78 09                           js 0x140700324
0070031B  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
0070031F  E8 8C CF FA FF                  call 0x1406ad2b0
00700324  0F 0D 0D 05 EB 7F 00            prefetchw byte ptr [rip + 0x7feb05]
0070032B  48 8B 05 FE EA 7F 00            mov rax, qword ptr [rip + 0x7feafe]
00700332  48 8B C8                        mov rcx, rax
00700335  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00700339  48 83 F9 10                     cmp rcx, 0x10
0070033D  48 8D 50 F0                     lea rdx, [rax - 0x10]
00700341  49 0F 46 D5                     cmovbe rdx, r13
00700345  A8 02                           test al, 2
00700347  75 0B                           jne 0x140700354
00700349  F0 48 0F B1 15 DE EA 7F 00      lock cmpxchg qword ptr [rip + 0x7feade], rdx
00700352  74 0C                           je 0x140700360
00700354  48 8D 0D D5 EA 7F 00            lea rcx, [rip + 0x7fead5]
0070035B  E8 70 35 B6 FF                  call 0x1402638d0
00700360  48 8D 0D C9 EA 7F 00            lea rcx, [rip + 0x7feac9]
00700367  E8 94 12 BE FF                  call 0x1402e1600
0070036C  4D 85 FF                        test r15, r15
0070036F  74 16                           je 0x140700387
00700371  84 DB                           test bl, bl
00700373  74 08                           je 0x14070037d
00700375  49 8B CF                        mov rcx, r15
00700378  E8 B3 9C 38 00                  call 0x140a8a030
0070037D  33 D2                           xor edx, edx
0070037F  49 8B CF                        mov rcx, r15
00700382  E8 E9 14 1A 00                  call 0x1408a1870
00700387  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
0070038E  48 33 CD                        xor rcx, rbp
00700391  E8 AA C2 FA FF                  call 0x1406ac640
00700396  48 8B 9D F0 00 00 00            mov rbx, qword ptr [rbp + 0xf0]
0070039D  48 8B B5 F8 00 00 00            mov rsi, qword ptr [rbp + 0xf8]
007003A4  48 8B BD 00 01 00 00            mov rdi, qword ptr [rbp + 0x100]
007003AB  48 8D A5 C0 00 00 00            lea rsp, [rbp + 0xc0]
007003B2  41 5F                           pop r15
007003B4  41 5E                           pop r14
007003B6  41 5D                           pop r13
007003B8  41 5C                           pop r12
007003BA  5D                              pop rbp
007003BB  C3                              ret
007003BC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWatchProductTypeWork(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int8 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int16 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m54;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int8 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (288);
    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    result = (*(unsigned __int64 *)(v_rip + 7383662)) ^ (v_stack_mE8);
    v_stack_m38 = result;
    v_r13 = 0;
    v_stack_m9C = 0;
    v_stack_m84 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_mB0 = 0;
    v_stack_mD0 = v_xmm1;
    v_stack_mD8 = 0;
    v_stack_mE8 = 1;
    v_stack_mC0 = 0;
    v_stack_mB8 = 0;
    result = RtlInitUnicodeString(v_stack_m70, *(unsigned __int64 *)(v_rip + 4501653), a3, a4);
    v_stack_mA0 = 48;
    v_stack_m90 = v_stack_m70;
    a3 = 0;
    v_stack_m98 = 0;
    a2 = 0;
    v_stack_m88 = 576;
    v_stack_m80 = v_xmm0;
    result = KeAbPreAcquire(v_rip + 8384735, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 8384698;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 8384686;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_rip + 8384641)) == 0) goto loc_00700324;
    a4 = 0;
    result = NtOpenKeyEx(v_stack_mC0, (unsigned int)((unsigned int)((unsigned int)(0x2001FULL))), v_stack_mA0, a4);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC000009AULL)))) goto loc_006FFDE8;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_006FFDC5:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_stack_mE0, a4);
    a4 = 0;
    result = NtOpenKeyEx(v_stack_mC0, (unsigned int)((unsigned int)((unsigned int)(0x2001FULL))), v_stack_mA0, a4);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC000009AULL)))) goto loc_006FFDC5;
loc_006FFDE8:
    if (sign_flag) {
        a4 = 0;
        a3 = (unsigned int)(result);
        a1 = 154;
        v_stack_m128 = 0;
        a2 = a4 + 13;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_stack_mA8 = *(unsigned __int64 *)(v_rip + 8384516);
    *(unsigned __int64 *)(v_rip + 8384501) = v_stack_mC0;
    if ((*(unsigned __int8 *)(v_rip + 8323884)) != 0) goto loc_007001AC;
    result = RtlInitUnicodeString(v_stack_mD0, *(unsigned __int64 *)(v_rip + 4501328), a3, a4);
    v_stack_m120 = v_stack_mD8;
    v_stack_m128 = 34;
    result = NtQueryValueKey(*(unsigned __int64 *)(v_rip + 8384472), v_stack_mD0, (unsigned int)((unsigned int)(34 - 32)), v_stack_m60);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC000009AULL)))) goto loc_006FFEB1;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_006FFE79:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_stack_mE0, v_stack_m60);
    v_stack_m120 = v_stack_mD8;
    v_stack_m128 = 34;
    result = NtQueryValueKey(*(unsigned __int64 *)(v_rip + 8384395), v_stack_mD0, (unsigned int)((unsigned int)(34 - 32)), v_stack_m60);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC000009AULL)))) goto loc_006FFE79;
loc_006FFEB1:
    if (sign_flag) goto loc_006FFF9F;
    a3 = (v_stack_m54) - (*(unsigned __int64 *)(v_rip + 4501192));
loc_006FFECA:
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4501192))) - ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4501192) + a3 * 1))));
    if (condition_is_not_equal) goto loc_006FFEDD;
    result = (*(unsigned __int64 *)(v_rip + 4501192)) + (34 - 32);
    if ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4501192) + a3 * 1)) != 0) goto loc_006FFECA;
loc_006FFEDD:
    if ((unsigned int)(a1) == 0) goto loc_006FFF0C;
    a3 = (v_stack_m54) - (*(unsigned __int64 *)(v_rip + 4501160));
loc_006FFEF2:
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4501160))) - ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4501160) + a3 * 1))));
    if (condition_is_not_equal) goto loc_006FFF05;
    result = (*(unsigned __int64 *)(v_rip + 4501160)) + (34 - 32);
    if ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4501160) + a3 * 1)) != 0) goto loc_006FFEF2;
loc_006FFF05:
    v_r10 = 0;
    if ((unsigned int)(a1) == 0) {
        v_r10 = 1;
    }
    a2 = (*(unsigned __int64 *)(v_rip + 8384234)) + (12);
    a4 = (a2) - (*(unsigned __int64 *)(v_rip + 4501115));
loc_006FFF27:
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4501115))) - ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4501115) + a4 * 1))));
    if (condition_is_not_equal) goto loc_006FFF3C;
    result = (*(unsigned __int64 *)(v_rip + 4501115)) + (34 - 32);
    if ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4501115) + a4 * 1)) != 0) goto loc_006FFF27;
loc_006FFF3C:
    if ((unsigned int)(a1) == 0) goto loc_006FFF6F;
    v_r12 = 1;
    if ((unsigned __int8)(v_r10) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 8384180);
        v_r12 = 0;
        *(unsigned __int64 *)(a1) = v_xmm0;
        *(unsigned __int64 *)(a1 + 16) = v_xmm1;
        result = v_stack_m40;
        *(unsigned __int16 *)(a1 + 32) = (unsigned __int16)(result);
    }
    a1 = (v_stack_m54) - (a2);
loc_006FFF79:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2))) != (*(unsigned __int16 *)(a2 + a1 * 1))) goto loc_006FFF8F;
    a2 = (a2) + (34 - 32);
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) != 0) goto loc_006FFF79;
    goto loc_006FFF94;
loc_006FFF8F:
    result = (unsigned int)((0) | (1));
loc_006FFF94:
    result = (unsigned int)(-(result));
    v_r12 = (unsigned __int8)((v_r12) & ((unsigned __int8)(result)));
    v_stack_mE8 = (unsigned __int8)(v_r12);
loc_006FFF9F:
    result = PsGetCurrentServerSiloGlobals(a1, *(unsigned __int64 *)(v_rip + 8384114), (unsigned int)(0xC0000002ULL), a4);
    if (*(unsigned __int64 *)(v_rip + 9274569) == 0) goto loc_00700193;
    result = guard_dispatch_icall(*(unsigned __int64 *)(result + 872), *(unsigned __int64 *)(v_rip + 8384114), (unsigned int)(0xC0000002ULL), a4);
    if (sign_flag) goto loc_00700193;
    result = CmSizeOfThreadInfo(*(unsigned __int64 *)(result + 872), *(unsigned __int64 *)(v_rip + 8384114), (unsigned int)((unsigned int)(result)), a4);
    if (((unsigned int)((unsigned int)(result)) + 15) <= ((unsigned int)((unsigned int)(result)))) {
    }
    result = ((unsigned int)((unsigned int)(result)) + 15) & (-16);
    result = _chkstk((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_rip + 8384114), (unsigned int)((unsigned int)(result)), a4);
    v_rsp = (v_rsp) - (result);
    v_stack_mB8 = v_stack_mE8;
    result = CmInitializeThreadInfo(v_stack_mE8, *(unsigned __int64 *)(v_rip + 8384114), (unsigned int)((unsigned int)(result)), a4);
    result = CmpLockRegistryFreezeAware(1, *(unsigned __int64 *)(v_rip + 8384114), (unsigned int)((unsigned int)(result)), a4);
    a3 = 0;
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8383965) + 8)));
    v_stack_m128 = *(unsigned __int64 *)(v_rip + 8383965) + 12;
    result = NtSetValueKey(*(unsigned __int64 *)(v_rip + 8383951), v_stack_mD0, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8383965) + 4)));
    if (((unsigned int)(result)) != 0xC000009AULL) goto loc_007000A0;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_0070005D:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_stack_mE0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8383965) + 4)));
    a3 = 0;
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8383887) + 8)));
    v_stack_m128 = *(unsigned __int64 *)(v_rip + 8383887) + 12;
    result = NtSetValueKey(*(unsigned __int64 *)(v_rip + 8383876), v_stack_mD0, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8383887) + 4)));
    if (((unsigned int)(result)) == 0xC000009AULL) goto loc_0070005D;
loc_007000A0:
    if (sign_flag) {
        a3 = (unsigned int)(result);
        a4 = 1;
        a2 = 17;
        v_stack_m128 = 0;
        a1 = 154;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(v_rip + 7740898)) == 0) goto loc_0070017C;
    result = RtlInitUnicodeString(v_stack_mD0, *(unsigned __int64 *)(v_rip + 4500687), a3, a4);
    a3 = 0;
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7740869) + 8)));
    v_stack_m128 = *(unsigned __int64 *)(v_rip + 7740869) + 12;
    result = NtSetValueKey(*(unsigned __int64 *)(v_rip + 8383762), v_stack_mD0, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7740869) + 4)));
    if (((unsigned int)(result)) != 0xC000009AULL) goto loc_0070015D;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_0070011A:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_stack_mE0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7740869) + 4)));
    a3 = 0;
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7740794) + 8)));
    v_stack_m128 = *(unsigned __int64 *)(v_rip + 7740794) + 12;
    result = NtSetValueKey(*(unsigned __int64 *)(v_rip + 8383687), v_stack_mD0, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7740794) + 4)));
    if (((unsigned int)(result)) == 0xC000009AULL) goto loc_0070011A;
loc_0070015D:
    if (!sign_flag) goto loc_007001B1;
    v_stack_m128 = 0;
    result = KeBugCheckEx(154, 17, (unsigned int)((unsigned int)(result)), 34 - 32);
loc_0070017C:
    result = RtlInitUnicodeString(154, 17, (unsigned int)((unsigned int)(result)), 34 - 32);
    result = NtDeleteValueKey(*(unsigned __int64 *)(v_rip + 8383632), v_stack_mD0, (unsigned int)((unsigned int)(result)), 34 - 32);
    goto loc_007001B1;
loc_00700193:
    v_stack_m128 = 0;
    result = KeBugCheckEx(154, 17, (unsigned int)((unsigned int)(result)), 17 - 16);
loc_007001AC:
loc_007001B1:
    v_stack_mF0 = 1;
    a4 = 0;
    v_stack_mF8 = 4;
    a3 = 0;
    v_stack_m100 = v_rip + 8383561;
    a2 = 0;
    v_stack_m108 = 0;
    v_stack_m110 = 0x10000005ULL;
    v_stack_m118 = v_rip + 8383451;
    v_stack_m120 = 1;
    v_stack_m128 = v_rip + 8383463;
    result = NtNotifyChangeMultipleKeys(*(unsigned __int64 *)(v_rip + 8383584), a2, a3, a4);
    if (((unsigned int)(result)) != 0xC000009AULL) goto loc_00700296;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_00700232:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_stack_mE0, a4);
    a4 = 0;
    v_stack_mF0 = 1;
    a3 = 0;
    v_stack_mF8 = 4;
    a2 = 0;
    v_stack_m100 = v_rip + 8383460;
    v_stack_m108 = 0;
    v_stack_m110 = 0x10000005ULL;
    v_stack_m118 = v_rip + 8383381;
    v_stack_m120 = 1;
    v_stack_m128 = v_rip + 8383406;
    result = NtNotifyChangeMultipleKeys(*(unsigned __int64 *)(v_rip + 8383442), a2, a3, a4);
    if (((unsigned int)(result)) == 0xC000009AULL) goto loc_00700232;
loc_00700296:
    if (1 != 0) {
        result = CmpUnlockRegistry(*(unsigned __int64 *)(v_rip + 8383442), a2, a3, a4);
    }
    if (v_stack_mB8 != 0) {
        a1 = v_stack_mB8;
        result = CmCleanupThreadInfo(a1, a2, a3, a4);
    }
    if (sign_flag) {
        a2 = 17;
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = 154;
        v_stack_m128 = 0;
        a4 = a2 - 13;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 8322661)) != 0) goto loc_00700324;
    if ((unsigned __int8)(v_stack_mE8) == 0) goto loc_00700324;
    v_stack_m108 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = (unsigned int)(0xC000026AULL);
    a4 = 0;
    a3 = 0;
    v_stack_m120 = v_rip + 808944;
    v_stack_m128 = 0;
    result = PsCreateSystemThreadEx(v_stack_mB0, (unsigned int)(0x1FFFFFULL), a3, a4);
    if (!(sign_flag)) {
        a1 = v_stack_mB0;
        result = ZwClose(a1, (unsigned int)(0x1FFFFFULL), a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rip + 8383230)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 8383230) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 8383230))) & (2)) != 0) goto loc_00700354;
    result = *(unsigned __int64 *)(v_rip + 8383230);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 8383230))) & (2)) != 0) {
        a1 = v_rip + 8383189;
        result = ExfReleasePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 8383177, a2, a3, a4);
    if (v_stack_mA8 == 0) goto loc_00700387;
    if (1 != 0) {
        a1 = v_stack_mA8;
        result = NtFlushKey(a1, a2, a3, a4);
    }
    a2 = 0;
    result = ObCloseHandle(v_stack_mA8, a2, a3, a4);
loc_00700387:
    a1 = (v_stack_m38) ^ (v_stack_mE8);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWatchProductTypeWork(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint8_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint16_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m54;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint8_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (288);
    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    result = (*(uint64_t *)(v_rip + 0x70AA6E)) ^ (v_stack_mE8);
    v_stack_m38 = result;
    local_r13 = 0;
    v_stack_m9C = 0;
    v_stack_m84 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_mB0 = 0;
    v_stack_mD0 = v_xmm1;
    v_stack_mD8 = 0;
    v_stack_mE8 = 1;
    v_stack_mC0 = 0;
    v_stack_mB8 = 0;
    result = RtlInitUnicodeString(v_stack_m70, *(uint64_t *)(v_rip + 0x44B095), Arg3, a4);
    v_stack_mA0 = 48;
    v_stack_m90 = v_stack_m70;
    Arg3 = 0;
    v_stack_m98 = 0;
    Arg2 = 0;
    v_stack_m88 = 576;
    v_stack_m80 = v_xmm0;
    result = KeAbPreAcquire(v_rip + 8384735, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 8384698;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 8384686;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(v_rip + 0x7FF081)) == 0) goto loc_00700324;
    a4 = 0;
    result = NtOpenKeyEx(v_stack_mC0, (uint32_t)((uint32_t)((uint32_t)(0x2001FULL))), v_stack_mA0, a4);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC000009AULL)))) goto loc_006FFDE8;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_006FFDC5:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_stack_mE0, a4);
    a4 = 0;
    result = NtOpenKeyEx(v_stack_mC0, (uint32_t)((uint32_t)((uint32_t)(0x2001FULL))), v_stack_mA0, a4);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC000009AULL)))) goto loc_006FFDC5;
loc_006FFDE8:
    if (sign_flag) {
        a4 = 0;
        Arg3 = (uint32_t)(result);
        Arg1 = 154;
        v_stack_m128 = 0;
        Arg2 = a4 + 13;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    v_stack_mA8 = *(uint64_t *)(v_rip + 0x7FF004);
    *(uint64_t *)(v_rip + 0x7FEFF5) = v_stack_mC0;
    if ((*(uint8_t *)(v_rip + 0x7F032C)) != 0) goto loc_007001AC;
    result = RtlInitUnicodeString(v_stack_mD0, *(uint64_t *)(v_rip + 0x44AF50), Arg3, a4);
    v_stack_m120 = v_stack_mD8;
    v_stack_m128 = 34;
    result = NtQueryValueKey(*(uint64_t *)(v_rip + 0x7FEFD8), v_stack_mD0, (uint32_t)((uint32_t)(34 - 32)), v_stack_m60);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC000009AULL)))) goto loc_006FFEB1;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_006FFE79:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_stack_mE0, v_stack_m60);
    v_stack_m120 = v_stack_mD8;
    v_stack_m128 = 34;
    result = NtQueryValueKey(*(uint64_t *)(v_rip + 0x7FEF8B), v_stack_mD0, (uint32_t)((uint32_t)(34 - 32)), v_stack_m60);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC000009AULL)))) goto loc_006FFE79;
loc_006FFEB1:
    if (sign_flag) goto loc_006FFF9F;
    Arg3 = (v_stack_m54) - (*(uint64_t *)(v_rip + 0x44AEC8));
loc_006FFECA:
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x44AEC8))) - ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x44AEC8) + Arg3 * 1))));
    if (condition_is_not_equal) goto loc_006FFEDD;
    result = (*(uint64_t *)(v_rip + 0x44AEC8)) + (34 - 32);
    if ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x44AEC8) + Arg3 * 1)) != 0) goto loc_006FFECA;
loc_006FFEDD:
    if ((uint32_t)(Arg1) == 0) goto loc_006FFF0C;
    Arg3 = (v_stack_m54) - (*(uint64_t *)(v_rip + 0x44AEA8));
loc_006FFEF2:
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x44AEA8))) - ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x44AEA8) + Arg3 * 1))));
    if (condition_is_not_equal) goto loc_006FFF05;
    result = (*(uint64_t *)(v_rip + 0x44AEA8)) + (34 - 32);
    if ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x44AEA8) + Arg3 * 1)) != 0) goto loc_006FFEF2;
loc_006FFF05:
    local_r10 = 0;
    if ((uint32_t)(Arg1) == 0) {
        local_r10 = 1;
    }
    Arg2 = (*(uint64_t *)(v_rip + 0x7FEEEA)) + (12);
    a4 = (Arg2) - (*(uint64_t *)(v_rip + 0x44AE7B));
loc_006FFF27:
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x44AE7B))) - ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x44AE7B) + a4 * 1))));
    if (condition_is_not_equal) goto loc_006FFF3C;
    result = (*(uint64_t *)(v_rip + 0x44AE7B)) + (34 - 32);
    if ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x44AE7B) + a4 * 1)) != 0) goto loc_006FFF27;
loc_006FFF3C:
    if ((uint32_t)(Arg1) == 0) goto loc_006FFF6F;
    local_r12 = 1;
    if ((uint8_t)(local_r10) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x7FEEB4);
        local_r12 = 0;
        *(uint64_t *)(Arg1) = v_xmm0;
        *(uint64_t *)(Arg1 + 0x10) = v_xmm1;
        result = v_stack_m40;
        *(uint16_t *)(Arg1 + 0x20) = (uint16_t)(result);
    }
    Arg1 = (v_stack_m54) - (Arg2);
loc_006FFF79:
    if (((uint16_t)(*(uint16_t *)(Arg2))) != (*(uint16_t *)(Arg2 + Arg1 * 1))) goto loc_006FFF8F;
    Arg2 = (Arg2) + (34 - 32);
    if ((uint16_t)(*(uint16_t *)(Arg2)) != 0) goto loc_006FFF79;
    goto loc_006FFF94;
loc_006FFF8F:
    result = (uint32_t)((0) | (1));
loc_006FFF94:
    result = (uint32_t)(-(result));
    local_r12 = (uint8_t)((local_r12) & ((uint8_t)(result)));
    v_stack_mE8 = (uint8_t)(local_r12);
loc_006FFF9F:
    result = PsGetCurrentServerSiloGlobals(Arg1, *(uint64_t *)(v_rip + 0x7FEE72), (uint32_t)(0xC0000002ULL), a4);
    if (*(uint64_t *)(v_rip + 0x8D84C9) == 0) goto loc_00700193;
    result = guard_dispatch_icall(*(uint64_t *)(result + 0x368), *(uint64_t *)(v_rip + 0x7FEE72), (uint32_t)(0xC0000002ULL), a4);
    if (sign_flag) goto loc_00700193;
    result = CmSizeOfThreadInfo(*(uint64_t *)(result + 0x368), *(uint64_t *)(v_rip + 0x7FEE72), (uint32_t)((uint32_t)(result)), a4);
    if (((uint32_t)((uint32_t)(result)) + 15) <= ((uint32_t)((uint32_t)(result)))) {
    }
    result = ((uint32_t)((uint32_t)(result)) + 15) & (-16);
    result = _chkstk((uint32_t)((uint32_t)(result)), *(uint64_t *)(v_rip + 0x7FEE72), (uint32_t)((uint32_t)(result)), a4);
    local_rsp = (local_rsp) - (result);
    v_stack_mB8 = v_stack_mE8;
    result = CmInitializeThreadInfo(v_stack_mE8, *(uint64_t *)(v_rip + 0x7FEE72), (uint32_t)((uint32_t)(result)), a4);
    result = CmpLockRegistryFreezeAware(1, *(uint64_t *)(v_rip + 0x7FEE72), (uint32_t)((uint32_t)(result)), a4);
    Arg3 = 0;
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x7FEDDD) + 0x8)));
    v_stack_m128 = *(uint64_t *)(v_rip + 0x7FEDDD) + 12;
    result = NtSetValueKey(*(uint64_t *)(v_rip + 0x7FEDCF), v_stack_mD0, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x7FEDDD) + 0x4)));
    if (((uint32_t)(result)) != 0xC000009AULL) goto loc_007000A0;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_0070005D:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_stack_mE0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x7FEDDD) + 0x4)));
    Arg3 = 0;
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x7FED8F) + 0x8)));
    v_stack_m128 = *(uint64_t *)(v_rip + 0x7FED8F) + 12;
    result = NtSetValueKey(*(uint64_t *)(v_rip + 0x7FED84), v_stack_mD0, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x7FED8F) + 0x4)));
    if (((uint32_t)(result)) == 0xC000009AULL) goto loc_0070005D;
loc_007000A0:
    if (sign_flag) {
        Arg3 = (uint32_t)(result);
        a4 = 1;
        Arg2 = 17;
        v_stack_m128 = 0;
        Arg1 = 154;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint64_t *)(v_rip + 0x761DE2)) == 0) goto loc_0070017C;
    result = RtlInitUnicodeString(v_stack_mD0, *(uint64_t *)(v_rip + 0x44ACCF), Arg3, a4);
    Arg3 = 0;
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x761DC5) + 0x8)));
    v_stack_m128 = *(uint64_t *)(v_rip + 0x761DC5) + 12;
    result = NtSetValueKey(*(uint64_t *)(v_rip + 0x7FED12), v_stack_mD0, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x761DC5) + 0x4)));
    if (((uint32_t)(result)) != 0xC000009AULL) goto loc_0070015D;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_0070011A:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_stack_mE0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x761DC5) + 0x4)));
    Arg3 = 0;
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x761D7A) + 0x8)));
    v_stack_m128 = *(uint64_t *)(v_rip + 0x761D7A) + 12;
    result = NtSetValueKey(*(uint64_t *)(v_rip + 0x7FECC7), v_stack_mD0, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x761D7A) + 0x4)));
    if (((uint32_t)(result)) == 0xC000009AULL) goto loc_0070011A;
loc_0070015D:
    if (!sign_flag) goto loc_007001B1;
    v_stack_m128 = 0;
    result = KeBugCheckEx(154, 17, (uint32_t)((uint32_t)(result)), 34 - 32);
loc_0070017C:
    result = RtlInitUnicodeString(154, 17, (uint32_t)((uint32_t)(result)), 34 - 32);
    result = NtDeleteValueKey(*(uint64_t *)(v_rip + 0x7FEC90), v_stack_mD0, (uint32_t)((uint32_t)(result)), 34 - 32);
    goto loc_007001B1;
loc_00700193:
    v_stack_m128 = 0;
    result = KeBugCheckEx(154, 17, (uint32_t)((uint32_t)(result)), 17 - 16);
loc_007001AC:
loc_007001B1:
    v_stack_mF0 = 1;
    a4 = 0;
    v_stack_mF8 = 4;
    Arg3 = 0;
    v_stack_m100 = v_rip + 8383561;
    Arg2 = 0;
    v_stack_m108 = 0;
    v_stack_m110 = 0x10000005ULL;
    v_stack_m118 = v_rip + 8383451;
    v_stack_m120 = 1;
    v_stack_m128 = v_rip + 8383463;
    result = NtNotifyChangeMultipleKeys(*(uint64_t *)(v_rip + 0x7FEC60), Arg2, Arg3, a4);
    if (((uint32_t)(result)) != 0xC000009AULL) goto loc_00700296;
    v_stack_mE0 = 0xFFFFFFFFFF676980ULL;
loc_00700232:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_stack_mE0, a4);
    a4 = 0;
    v_stack_mF0 = 1;
    Arg3 = 0;
    v_stack_mF8 = 4;
    Arg2 = 0;
    v_stack_m100 = v_rip + 8383460;
    v_stack_m108 = 0;
    v_stack_m110 = 0x10000005ULL;
    v_stack_m118 = v_rip + 8383381;
    v_stack_m120 = 1;
    v_stack_m128 = v_rip + 8383406;
    result = NtNotifyChangeMultipleKeys(*(uint64_t *)(v_rip + 0x7FEBD2), Arg2, Arg3, a4);
    if (((uint32_t)(result)) == 0xC000009AULL) goto loc_00700232;
loc_00700296:
    if (1 != 0) {
        result = CmpUnlockRegistry(*(uint64_t *)(v_rip + 0x7FEBD2), Arg2, Arg3, a4);
    }
    if (v_stack_mB8 != 0) {
        Arg1 = v_stack_mB8;
        result = CmCleanupThreadInfo(Arg1, Arg2, Arg3, a4);
    }
    if (sign_flag) {
        Arg2 = 17;
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = 154;
        v_stack_m128 = 0;
        a4 = Arg2 - 13;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint8_t *)(v_rip + 0x7EFE65)) != 0) goto loc_00700324;
    if ((uint8_t)(v_stack_mE8) == 0) goto loc_00700324;
    v_stack_m108 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = (uint32_t)(0xC000026AULL);
    a4 = 0;
    Arg3 = 0;
    v_stack_m120 = v_rip + 808944;
    v_stack_m128 = 0;
    result = PsCreateSystemThreadEx(v_stack_mB0, (uint32_t)(0x1FFFFFULL), Arg3, a4);
    if (!(sign_flag)) {
        Arg1 = v_stack_mB0;
        result = ZwClose(Arg1, (uint32_t)(0x1FFFFFULL), Arg3, a4);
    }
    Arg1 = (*(uint64_t *)(v_rip + 0x7FEAFE)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x7FEAFE) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x7FEAFE))) & (2)) != 0) goto loc_00700354;
    result = *(uint64_t *)(v_rip + 0x7FEAFE);
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x7FEAFE))) & (2)) != 0) {
        Arg1 = v_rip + 8383189;
        result = ExfReleasePushLock(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(v_rip + 8383177, Arg2, Arg3, a4);
    if (v_stack_mA8 == 0) goto loc_00700387;
    if (1 != 0) {
        Arg1 = v_stack_mA8;
        result = NtFlushKey(Arg1, Arg2, Arg3, a4);
    }
    Arg2 = 0;
    result = ObCloseHandle(v_stack_mA8, Arg2, Arg3, a4);
loc_00700387:
    Arg1 = (v_stack_m38) ^ (v_stack_mE8);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x006FFCA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
