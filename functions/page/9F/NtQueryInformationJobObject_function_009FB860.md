# NtQueryInformationJobObject

- RVA: `0x009FB860`–`0x009FC641` (길이 `3,553` bytes)
- VA: `0x00000001409FB860`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A70C4`
- 디코드: `716`개 명령, `3,553/3,553` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x009FB8CC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FB8F2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FB972` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FB9A5` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FB9C4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FB9D7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FB9EA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FBA22` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FBAA3` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FBBD2` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009FBC3F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009FBC53` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009FBCC1` → [PspQueryJobHierarchyAccountingInformation](../91/PspQueryJobHierarchyAccountingInformation_function_0091864C.md) (function, `0x0091864C`)
- `0x009FBCFE` → [PspLockJobExclusive](../91/PspLockJobExclusive_function_0091A4B8.md) (function, `0x0091A4B8`)
- `0x009FBD26` → [PspLockJobMemoryLimitsShared](../91/PspLockJobMemoryLimitsShared_function_0091A394.md) (function, `0x0091A394`)
- `0x009FBD55` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009FBD61` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009FBE13` → [PspQueryRateControlHistory](../91/PspQueryRateControlHistory_function_00918D1C.md) (function, `0x00918D1C`)
- `0x009FBE6D` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x009FBF8B` → [EtwTraceJobSetQuery](EtwTraceJobSetQuery_function_009FB480.md) (function, `0x009FB480`)
- `0x009FC027` → [PspLockJobMemoryLimitsShared](../91/PspLockJobMemoryLimitsShared_function_0091A394.md) (function, `0x0091A394`)
- `0x009FC072` → [PspUnlockJobMemoryLimitsShared](../91/PspUnlockJobMemoryLimitsShared_function_0091A420.md) (function, `0x0091A420`)
- `0x009FC0B3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009FC0D0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009FC108` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x009FC1B7` → [PspGetJobLimitInformationValidFlags](PspGetJobLimitInformationValidFlags_function_009FB458.md) (function, `0x009FB458`)
- `0x009FC1E2` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x009FC23E` → [PspAllocateAndQueryNotificationChannel](../91/PspAllocateAndQueryNotificationChannel_function_00917EE4.md) (function, `0x00917EE4`)
- `0x009FC273` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FC280` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x009FC290` → [PspQueryJobIoAttribution](PspQueryJobIoAttribution_function_009FC648.md) (function, `0x009FC648`)
- `0x009FC29F` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x009FC2F2` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x009FC3A5` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x009FC4CF` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x009FC4E4` → [PspQueryJobHierarchyInterferenceCount](../78/PspQueryJobHierarchyInterferenceCount_function_00785110.md) (function, `0x00785110`)
- `0x009FC55B` → [PspQueryJobHierarchyAccountingInformation](../91/PspQueryJobHierarchyAccountingInformation_function_0091864C.md) (function, `0x0091864C`)
- `0x009FC5DD` → [PspRateControlLimitFlag](../91/PspRateControlLimitFlag_function_0091A3FC.md) (function, `0x0091A3FC`)
- `0x009FC607` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FC625` → [PsGetJobServerSilo](../../text/4C/PsGetJobServerSilo_function_004C2440.md) (function, `0x004C2440`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009FB873` → RVA `0x00E0A740` (`.data`; read)
- `0x009FBB5B` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x009FBC11` → RVA `0x00FC6C58` (`ALMOSTRO`; read)
- `0x009FBF5A` → RVA `0x00FC6B00` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x009FB8CC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FB8F2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FB972` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FB9A5` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FB9C4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FB9D7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FB9EA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FBA22` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FBAA3` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FBC53` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009FBD55` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009FBD61` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009FC0B3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009FC0D0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009FC273` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FC4CF` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x009FC607` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FC625` → [PsGetJobServerSilo](../../text/4C/PsGetJobServerSilo_function_004C2440.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **18**
  - `0x009FBB72` → [sub_00B316B4](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FBE79` → [sub_00B316B4 + 0xB55](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FBFFF` → [sub_00B316B4 + 0x80E](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC00F` → [sub_00B316B4 + 0x5E6](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC0E1` → [sub_00B316B4 + 0x127](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC0FC` → [sub_00B316B4 + 0x4E](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC1D7` → [sub_00B316B4 + 0x26C](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC1F7` → [sub_00B316B4 + 0x419](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC200` → [sub_00B316B4 + 0x38D](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC21B` → [sub_00B316B4 + 0x311](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC25F` → [sub_00B316B4 + 0xC93](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC3B1` → [sub_00B316B4 + 0x789](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC3BA` → [sub_00B316B4 + 0x6F4](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC530` → [sub_00B316B4 + 0xD1C](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC5CB` → [sub_00B316B4 + 0xAB3](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC5D5` → [sub_00B316B4 + 0xAB3](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC614` → [sub_00B316B4 + 0xC39](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)
  - `0x009FC632` → [sub_00B316B4 + 0xC3F](../B3/Unknown_function_00B316B4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009FB860  40 53                           push rbx
009FB862  56                              push rsi
009FB863  57                              push rdi
009FB864  41 54                           push r12
009FB866  41 55                           push r13
009FB868  41 56                           push r14
009FB86A  41 57                           push r15
009FB86C  48 81 EC 80 0A 00 00            sub rsp, 0xa80
009FB873  48 8B 05 C6 EE 40 00            mov rax, qword ptr [rip + 0x40eec6]
009FB87A  48 33 C4                        xor rax, rsp
009FB87D  48 89 84 24 70 0A 00 00         mov qword ptr [rsp + 0xa70], rax
009FB885  41 8B D9                        mov ebx, r9d
009FB888  89 5C 24 6C                     mov dword ptr [rsp + 0x6c], ebx
009FB88C  49 8B F8                        mov rdi, r8
009FB88F  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
009FB894  4C 63 F2                        movsxd r14, edx
009FB897  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
009FB89F  4C 8B BC 24 E0 0A 00 00         mov r15, qword ptr [rsp + 0xae0]
009FB8A7  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
009FB8AC  4C 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r8
009FB8B4  4C 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r15
009FB8BC  33 D2                           xor edx, edx
009FB8BE  41 B8 D0 01 00 00               mov r8d, 0x1d0
009FB8C4  48 8D 8C 24 50 05 00 00         lea rcx, [rsp + 0x550]
009FB8CC  E8 6F B3 CC FF                  call 0x1406c6c40
009FB8D1  0F 57 C0                        xorps xmm0, xmm0
009FB8D4  0F 11 84 24 50 02 00 00         movups xmmword ptr [rsp + 0x250], xmm0
009FB8DC  33 F6                           xor esi, esi
009FB8DE  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
009FB8E2  33 D2                           xor edx, edx
009FB8E4  41 B8 08 01 00 00               mov r8d, 0x108
009FB8EA  48 8D 8C 24 20 07 00 00         lea rcx, [rsp + 0x720]
009FB8F2  E8 49 B3 CC FF                  call 0x1406c6c40
009FB8F7  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
009FB8FC  40 88 74 24 5E                  mov byte ptr [rsp + 0x5e], sil
009FB901  48 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rsi
009FB909  48 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rsi
009FB911  89 B4 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], esi
009FB918  48 89 B4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rsi
009FB920  89 B4 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], esi
009FB927  0F 57 C0                        xorps xmm0, xmm0
009FB92A  33 C0                           xor eax, eax
009FB92C  0F 11 84 24 F0 02 00 00         movups xmmword ptr [rsp + 0x2f0], xmm0
009FB934  0F 11 84 24 00 03 00 00         movups xmmword ptr [rsp + 0x300], xmm0
009FB93C  89 84 24 10 03 00 00            mov dword ptr [rsp + 0x310], eax
009FB943  0F 11 84 24 18 03 00 00         movups xmmword ptr [rsp + 0x318], xmm0
009FB94B  48 89 B4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rsi
009FB953  89 B4 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], esi
009FB95A  48 89 B4 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rsi
009FB962  33 D2                           xor edx, edx
009FB964  41 B8 98 00 00 00               mov r8d, 0x98
009FB96A  48 8D 8C 24 20 04 00 00         lea rcx, [rsp + 0x420]
009FB972  E8 C9 B2 CC FF                  call 0x1406c6c40
009FB977  0F 57 C0                        xorps xmm0, xmm0
009FB97A  0F 11 84 24 F0 01 00 00         movups xmmword ptr [rsp + 0x1f0], xmm0
009FB982  66 89 74 24 68                  mov word ptr [rsp + 0x68], si
009FB987  89 B4 24 88 00 00 00            mov dword ptr [rsp + 0x88], esi
009FB98E  33 C0                           xor eax, eax
009FB990  89 84 24 C4 04 00 00            mov dword ptr [rsp + 0x4c4], eax
009FB997  33 D2                           xor edx, edx
009FB999  44 8D 46 44                     lea r8d, [rsi + 0x44]
009FB99D  48 8D 8C 24 C0 04 00 00         lea rcx, [rsp + 0x4c0]
009FB9A5  E8 96 B2 CC FF                  call 0x1406c6c40
009FB9AA  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
009FB9AF  89 B4 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], esi
009FB9B6  33 D2                           xor edx, edx
009FB9B8  44 8D 46 68                     lea r8d, [rsi + 0x68]
009FB9BC  48 8D 8C 24 60 01 00 00         lea rcx, [rsp + 0x160]
009FB9C4  E8 77 B2 CC FF                  call 0x1406c6c40
009FB9C9  33 D2                           xor edx, edx
009FB9CB  44 8D 46 50                     lea r8d, [rsi + 0x50]
009FB9CF  48 8D 8C 24 30 03 00 00         lea rcx, [rsp + 0x330]
009FB9D7  E8 64 B2 CC FF                  call 0x1406c6c40
009FB9DC  33 D2                           xor edx, edx
009FB9DE  44 8D 46 58                     lea r8d, [rsi + 0x58]
009FB9E2  48 8D 8C 24 80 03 00 00         lea rcx, [rsp + 0x380]
009FB9EA  E8 51 B2 CC FF                  call 0x1406c6c40
009FB9EF  0F 57 C0                        xorps xmm0, xmm0
009FB9F2  33 C0                           xor eax, eax
009FB9F4  0F 11 84 24 C8 02 00 00         movups xmmword ptr [rsp + 0x2c8], xmm0
009FB9FC  0F 11 84 24 D8 02 00 00         movups xmmword ptr [rsp + 0x2d8], xmm0
009FBA04  48 89 84 24 E8 02 00 00         mov qword ptr [rsp + 0x2e8], rax
009FBA0C  0F 11 84 24 D0 01 00 00         movups xmmword ptr [rsp + 0x1d0], xmm0
009FBA14  33 D2                           xor edx, edx
009FBA16  44 8D 46 48                     lea r8d, [rsi + 0x48]
009FBA1A  48 8D 8C 24 00 02 00 00         lea rcx, [rsp + 0x200]
009FBA22  E8 19 B2 CC FF                  call 0x1406c6c40
009FBA27  0F 57 C0                        xorps xmm0, xmm0
009FBA2A  0F 11 84 24 60 02 00 00         movups xmmword ptr [rsp + 0x260], xmm0
009FBA32  0F 11 84 24 70 02 00 00         movups xmmword ptr [rsp + 0x270], xmm0
009FBA3A  0F 11 84 24 80 02 00 00         movups xmmword ptr [rsp + 0x280], xmm0
009FBA42  0F 57 C9                        xorps xmm1, xmm1
009FBA45  33 C0                           xor eax, eax
009FBA47  0F 11 8C 24 90 02 00 00         movups xmmword ptr [rsp + 0x290], xmm1
009FBA4F  0F 11 8C 24 A0 02 00 00         movups xmmword ptr [rsp + 0x2a0], xmm1
009FBA57  0F 11 8C 24 B0 02 00 00         movups xmmword ptr [rsp + 0x2b0], xmm1
009FBA5F  48 89 84 24 C0 02 00 00         mov qword ptr [rsp + 0x2c0], rax
009FBA67  89 B4 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], esi
009FBA6E  0F 11 84 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm0
009FBA76  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
009FBA7E  0F 11 84 24 40 01 00 00         movups xmmword ptr [rsp + 0x140], xmm0
009FBA86  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
009FBA8D  48 89 B4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rsi
009FBA95  33 D2                           xor edx, edx
009FBA97  44 8D 46 40                     lea r8d, [rsi + 0x40]
009FBA9B  48 8D 8C 24 10 05 00 00         lea rcx, [rsp + 0x510]
009FBAA3  E8 98 B1 CC FF                  call 0x1406c6c40
009FBAA8  0F 57 C0                        xorps xmm0, xmm0
009FBAAB  0F 11 84 24 E0 01 00 00         movups xmmword ptr [rsp + 0x1e0], xmm0
009FBAB3  0F 57 C9                        xorps xmm1, xmm1
009FBAB6  33 C0                           xor eax, eax
009FBAB8  0F 11 8C 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm1
009FBAC0  0F 11 8C 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm1
009FBAC8  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
009FBAD0  0F 11 84 24 E0 03 00 00         movups xmmword ptr [rsp + 0x3e0], xmm0
009FBAD8  0F 11 84 24 F0 03 00 00         movups xmmword ptr [rsp + 0x3f0], xmm0
009FBAE0  0F 11 84 24 00 04 00 00         movups xmmword ptr [rsp + 0x400], xmm0
009FBAE8  89 84 24 10 04 00 00            mov dword ptr [rsp + 0x410], eax
009FBAEF  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
009FBAF7  40 88 74 24 5D                  mov byte ptr [rsp + 0x5d], sil
009FBAFC  40 88 74 24 5F                  mov byte ptr [rsp + 0x5f], sil
009FBB01  41 8D 46 FF                     lea eax, [r14 - 1]
009FBB05  83 F8 32                        cmp eax, 0x32
009FBB08  0F 87 29 0B 00 00               ja 0x1409fc637
009FBB0E  41 8B CE                        mov ecx, r14d
009FBB11  83 E9 09                        sub ecx, 9
009FBB14  0F 84 B2 07 00 00               je 0x1409fc2cc
009FBB1A  83 E9 03                        sub ecx, 3
009FBB1D  0F 84 93 09 00 00               je 0x1409fc4b6
009FBB23  83 E9 01                        sub ecx, 1
009FBB26  0F 84 79 09 00 00               je 0x1409fc4a5
009FBB2C  83 E9 06                        sub ecx, 6
009FBB2F  0F 84 52 09 00 00               je 0x1409fc487
009FBB35  83 E9 01                        sub ecx, 1
009FBB38  0F 84 8C 04 00 00               je 0x1409fbfca
009FBB3E  83 E9 08                        sub ecx, 8
009FBB41  0F 84 2F 09 00 00               je 0x1409fc476
009FBB47  8D 56 02                        lea edx, [rsi + 2]
009FBB4A  2B CA                           sub ecx, edx
009FBB4C  0F 84 13 09 00 00               je 0x1409fc465
009FBB52  83 F9 0D                        cmp ecx, 0xd
009FBB55  0F 84 EA 08 00 00               je 0x1409fc445
009FBB5B  4C 8D 05 9E 44 60 FF            lea r8, [rip - 0x9fbb62]
009FBB62  47 8B AC B0 2C E5 B4 00         mov r13d, dword ptr [r8 + r14*4 + 0xb4e52c]
009FBB6A  44 89 6C 24 58                  mov dword ptr [rsp + 0x58], r13d
009FBB6F  41 3B DD                        cmp ebx, r13d
009FBB72  0F 85 3C 5B 13 00               jne 0x140b316b4
009FBB78  41 BC 01 00 00 00               mov r12d, 1
009FBB7E  44 89 AC 24 8C 00 00 00         mov dword ptr [rsp + 0x8c], r13d
009FBB86  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009FBB8F  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
009FBB94  8A 81 32 02 00 00               mov al, byte ptr [rcx + 0x232]
009FBB9A  88 44 24 5C                     mov byte ptr [rsp + 0x5c], al
009FBB9E  84 C0                           test al, al
009FBBA0  74 5E                           je 0x1409fbc00
009FBBA2  43 8B 84 B0 FC E5 B4 00         mov eax, dword ptr [r8 + r14*4 + 0xb4e5fc]
009FBBAA  85 DB                           test ebx, ebx
009FBBAC  75 1C                           jne 0x1409fbbca
009FBBAE  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009FBBB8  4D 85 FF                        test r15, r15
009FBBBB  74 3B                           je 0x1409fbbf8
009FBBBD  4C 3B FA                        cmp r15, rdx
009FBBC0  49 0F 42 D7                     cmovb rdx, r15
009FBBC4  8B 02                           mov eax, dword ptr [rdx]
009FBBC6  89 02                           mov dword ptr [rdx], eax
009FBBC8  EB 2E                           jmp 0x1409fbbf8
009FBBCA  8D 48 FF                        lea ecx, [rax - 1]
009FBBCD  48 85 CF                        test rdi, rcx
009FBBD0  74 05                           je 0x1409fbbd7
009FBBD2  E8 F9 E3 E9 FF                  call 0x140899fd0
009FBBD7  48 8D 0C 1F                     lea rcx, [rdi + rbx]
009FBBDB  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009FBBE5  48 3B CA                        cmp rcx, rdx
009FBBE8  77 05                           ja 0x1409fbbef
009FBBEA  48 3B CF                        cmp rcx, rdi
009FBBED  73 02                           jae 0x1409fbbf1
009FBBEF  8A 02                           mov al, byte ptr [rdx]
009FBBF1  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009FBBF6  EB C0                           jmp 0x1409fbbb8
009FBBF8  8A 44 24 5C                     mov al, byte ptr [rsp + 0x5c]
009FBBFC  EB 02                           jmp 0x1409fbc00
009FBBFE  EB 48                           jmp 0x1409fbc48
009FBC00  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
009FBC08  4D 85 D2                        test r10, r10
009FBC0B  0F 84 84 03 00 00               je 0x1409fbf95
009FBC11  4C 8B 05 40 B0 5C 00            mov r8, qword ptr [rip + 0x5cb040]
009FBC18  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
009FBC1D  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
009FBC22  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
009FBC27  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
009FBC2C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009FBC34  44 8A C8                        mov r9b, al
009FBC37  BA 04 00 00 00                  mov edx, 4
009FBC3C  49 8B CA                        mov rcx, r10
009FBC3F  E8 0C DA E6 FF                  call 0x140869650
009FBC44  85 C0                           test eax, eax
009FBC46  79 24                           jns 0x1409fbc6c
009FBC48  48 8B 8C 24 70 0A 00 00         mov rcx, qword ptr [rsp + 0xa70]
009FBC50  48 33 CC                        xor rcx, rsp
009FBC53  E8 E8 09 CB FF                  call 0x1406ac640
009FBC58  48 81 C4 80 0A 00 00            add rsp, 0xa80
009FBC5F  41 5F                           pop r15
009FBC61  41 5E                           pop r14
009FBC63  41 5D                           pop r13
009FBC65  41 5C                           pop r12
009FBC67  5F                              pop rdi
009FBC68  5E                              pop rsi
009FBC69  5B                              pop rbx
009FBC6A  C3                              ret
009FBC6B  CC                              int3
009FBC6C  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009FBC71  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009FBC76  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
009FBC7B  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
009FBC80  4C 8B FE                        mov r15, rsi
009FBC83  8B DE                           mov ebx, esi
009FBC85  41 83 FE 1A                     cmp r14d, 0x1a
009FBC89  0F 8F 5C 03 00 00               jg 0x1409fbfeb
009FBC8F  0F 84 44 08 00 00               je 0x1409fc4d9
009FBC95  41 83 FE 0C                     cmp r14d, 0xc
009FBC99  0F 8E 38 04 00 00               jle 0x1409fc0d7
009FBC9F  41 8B D6                        mov edx, r14d
009FBCA2  83 EA 0D                        sub edx, 0xd
009FBCA5  0F 85 49 05 00 00               jne 0x1409fc1f4
009FBCAB  33 C0                           xor eax, eax
009FBCAD  66 89 44 24 58                  mov word ptr [rsp + 0x58], ax
009FBCB2  88 44 24 5A                     mov byte ptr [rsp + 0x5a], al
009FBCB6  48 8D 94 24 50 05 00 00         lea rdx, [rsp + 0x550]
009FBCBE  48 8B CF                        mov rcx, rdi
009FBCC1  E8 86 C9 F1 FF                  call 0x14091864c
009FBCC6  48 8B 84 24 98 05 00 00         mov rax, qword ptr [rsp + 0x598]
009FBCCE  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
009FBCD6  48 8B 84 24 A0 05 00 00         mov rax, qword ptr [rsp + 0x5a0]
009FBCDE  48 89 84 24 78 01 00 00         mov qword ptr [rsp + 0x178], rax
009FBCE6  48 8B 84 24 50 05 00 00         mov rax, qword ptr [rsp + 0x550]
009FBCEE  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
009FBCF6  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
009FBCFB  48 8B CF                        mov rcx, rdi
009FBCFE  E8 B5 E7 F1 FF                  call 0x14091a4b8
009FBD03  8B 87 10 06 00 00               mov eax, dword ptr [rdi + 0x610]
009FBD09  B9 08 40 00 00                  mov ecx, 0x4008
009FBD0E  23 C1                           and eax, ecx
009FBD10  3B C1                           cmp eax, ecx
009FBD12  74 0D                           je 0x1409fbd21
009FBD14  F0 83 A7 10 06 00 00 FB         lock and dword ptr [rdi + 0x610], 0xfffffffb
009FBD1C  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009FBD21  33 D2                           xor edx, edx
009FBD23  48 8B CF                        mov rcx, rdi
009FBD26  E8 69 E6 F1 FF                  call 0x14091a394
009FBD2B  48 8B 87 B8 04 00 00            mov rax, qword ptr [rdi + 0x4b8]
009FBD32  48 C1 E0 0C                     shl rax, 0xc
009FBD36  48 89 84 24 98 01 00 00         mov qword ptr [rsp + 0x198], rax
009FBD3E  B8 11 00 00 00                  mov eax, 0x11
009FBD43  F0 48 0F B1 B7 F0 04 00 00      lock cmpxchg qword ptr [rdi + 0x4f0], rsi
009FBD4C  74 0C                           je 0x1409fbd5a
009FBD4E  48 8D 8F F0 04 00 00            lea rcx, [rdi + 0x4f0]
009FBD55  E8 E6 76 86 FF                  call 0x140263440
009FBD5A  48 8D 8F F0 04 00 00            lea rcx, [rdi + 0x4f0]
009FBD61  E8 9A 58 8E FF                  call 0x1402e1600
009FBD66  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009FBD6B  48 8B 87 C0 04 00 00            mov rax, qword ptr [rdi + 0x4c0]
009FBD72  48 85 C0                        test rax, rax
009FBD75  0F 85 28 08 00 00               jne 0x1409fc5a3
009FBD7B  48 89 B4 24 60 01 00 00         mov qword ptr [rsp + 0x160], rsi
009FBD83  48 89 B4 24 70 01 00 00         mov qword ptr [rsp + 0x170], rsi
009FBD8B  48 89 B4 24 80 01 00 00         mov qword ptr [rsp + 0x180], rsi
009FBD93  48 89 B4 24 90 01 00 00         mov qword ptr [rsp + 0x190], rsi
009FBD9B  48 89 B4 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rsi
009FBDA3  48 89 B4 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rsi
009FBDAB  8B CE                           mov ecx, esi
009FBDAD  85 C9                           test ecx, ecx
009FBDAF  0F 84 56 06 00 00               je 0x1409fc40b
009FBDB5  83 F9 01                        cmp ecx, 1
009FBDB8  0F 84 5A 06 00 00               je 0x1409fc418
009FBDBE  48 8D 84 24 AC 01 00 00         lea rax, [rsp + 0x1ac]
009FBDC6  89 30                           mov dword ptr [rax], esi
009FBDC8  41 03 CC                        add ecx, r12d
009FBDCB  83 F9 03                        cmp ecx, 3
009FBDCE  7C DD                           jl 0x1409fbdad
009FBDD0  44 8B FE                        mov r15d, esi
009FBDD3  48 8D 5C 24 58                  lea rbx, [rsp + 0x58]
009FBDD8  41 B8 3C 00 00 00               mov r8d, 0x3c
009FBDDE  4C 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], r8
009FBDE6  48 8B 97 C0 04 00 00            mov rdx, qword ptr [rdi + 0x4c0]
009FBDED  48 85 D2                        test rdx, rdx
009FBDF0  0F 85 E4 07 00 00               jne 0x1409fc5da
009FBDF6  41 8B D4                        mov edx, r12d
009FBDF9  89 94 24 88 00 00 00            mov dword ptr [rsp + 0x88], edx
009FBE00  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
009FBE05  4C 8D 8C 24 BC 00 00 00         lea r9, [rsp + 0xbc]
009FBE0D  44 8A 03                        mov r8b, byte ptr [rbx]
009FBE10  48 8B CF                        mov rcx, rdi
009FBE13  E8 04 CF F1 FF                  call 0x140918d1c
009FBE18  45 85 FF                        test r15d, r15d
009FBE1B  0F 85 04 06 00 00               jne 0x1409fc425
009FBE21  48 8D 8C 24 C0 01 00 00         lea rcx, [rsp + 0x1c0]
009FBE29  8B 84 24 BC 00 00 00            mov eax, dword ptr [rsp + 0xbc]
009FBE30  89 01                           mov dword ptr [rcx], eax
009FBE32  45 03 FC                        add r15d, r12d
009FBE35  4C 8B 84 24 80 00 00 00         mov r8, qword ptr [rsp + 0x80]
009FBE3D  49 83 C0 04                     add r8, 4
009FBE41  4C 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], r8
009FBE49  49 03 DC                        add rbx, r12
009FBE4C  41 83 FF 03                     cmp r15d, 3
009FBE50  7C 94                           jl 0x1409fbde6
009FBE52  48 8B 87 C0 04 00 00            mov rax, qword ptr [rdi + 0x4c0]
009FBE59  48 85 C0                        test rax, rax
009FBE5C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009FBE61  0F 85 8C 07 00 00               jne 0x1409fc5f3
009FBE67  48 8B D3                        mov rdx, rbx
009FBE6A  48 8B CF                        mov rcx, rdi
009FBE6D  E8 8E DF F1 FF                  call 0x140919e00
009FBE72  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
009FBE76  83 F8 58                        cmp eax, 0x58
009FBE79  0F 85 8A 63 13 00               jne 0x140b32209
009FBE7F  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
009FBE87  48 89 84 24 88 03 00 00         mov qword ptr [rsp + 0x388], rax
009FBE8F  48 8B 84 24 70 01 00 00         mov rax, qword ptr [rsp + 0x170]
009FBE97  48 89 84 24 90 03 00 00         mov qword ptr [rsp + 0x390], rax
009FBE9F  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
009FBEA7  48 89 84 24 98 03 00 00         mov qword ptr [rsp + 0x398], rax
009FBEAF  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
009FBEB7  48 89 84 24 A0 03 00 00         mov qword ptr [rsp + 0x3a0], rax
009FBEBF  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
009FBEC7  48 89 84 24 A8 03 00 00         mov qword ptr [rsp + 0x3a8], rax
009FBECF  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
009FBED7  48 89 84 24 B0 03 00 00         mov qword ptr [rsp + 0x3b0], rax
009FBEDF  48 8B 84 24 98 01 00 00         mov rax, qword ptr [rsp + 0x198]
009FBEE7  48 89 84 24 B8 03 00 00         mov qword ptr [rsp + 0x3b8], rax
009FBEEF  48 8B 84 24 B0 01 00 00         mov rax, qword ptr [rsp + 0x1b0]
009FBEF7  48 89 84 24 C0 03 00 00         mov qword ptr [rsp + 0x3c0], rax
009FBEFF  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
009FBF07  48 89 84 24 C8 03 00 00         mov qword ptr [rsp + 0x3c8], rax
009FBF0F  8B 84 24 A8 01 00 00            mov eax, dword ptr [rsp + 0x1a8]
009FBF16  89 84 24 D0 03 00 00            mov dword ptr [rsp + 0x3d0], eax
009FBF1D  8B 84 24 AC 01 00 00            mov eax, dword ptr [rsp + 0x1ac]
009FBF24  89 84 24 D4 03 00 00            mov dword ptr [rsp + 0x3d4], eax
009FBF2B  8B 84 24 60 01 00 00            mov eax, dword ptr [rsp + 0x160]
009FBF32  B9 04 82 27 00                  mov ecx, 0x278204
009FBF37  23 C1                           and eax, ecx
009FBF39  89 84 24 80 03 00 00            mov dword ptr [rsp + 0x380], eax
009FBF40  8B 84 24 64 01 00 00            mov eax, dword ptr [rsp + 0x164]
009FBF47  23 C1                           and eax, ecx
009FBF49  89 84 24 84 03 00 00            mov dword ptr [rsp + 0x384], eax
009FBF50  4C 8D BC 24 80 03 00 00         lea r15, [rsp + 0x380]
009FBF58  8B DE                           mov ebx, esi
009FBF5A  F7 05 9C AB 5C 00 00 00 08 00   test dword ptr [rip + 0x5cab9c], 0x80000
009FBF64  0F 84 17 01 00 00               je 0x1409fc081
009FBF6A  66 C7 44 24 28 26 07            mov word ptr [rsp + 0x28], 0x726
009FBF71  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
009FBF75  4C 8D 8C 24 88 00 00 00         lea r9, [rsp + 0x88]
009FBF7D  4C 8D 84 24 60 01 00 00         lea r8, [rsp + 0x160]
009FBF85  41 8B D6                        mov edx, r14d
009FBF88  48 8B CF                        mov rcx, rdi
009FBF8B  E8 F0 F4 FF FF                  call 0x1409fb480
009FBF90  E9 EC 00 00 00                  jmp 0x1409fc081
009FBF95  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
009FBF9C  48 8B B8 A0 02 00 00            mov rdi, qword ptr [rax + 0x2a0]
009FBFA3  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
009FBFA8  48 85 FF                        test rdi, rdi
009FBFAB  0F 85 16 05 00 00               jne 0x1409fc4c7
009FBFB1  41 8D 46 E1                     lea eax, [r14 - 0x1f]
009FBFB5  A9 F7 FF FF FF                  test eax, 0xfffffff7
009FBFBA  0F 84 B6 FC FF FF               je 0x1409fbc76
009FBFC0  B8 22 00 00 C0                  mov eax, 0xc0000022
009FBFC5  E9 7E FC FF FF                  jmp 0x1409fbc48
009FBFCA  83 FB 28                        cmp ebx, 0x28
009FBFCD  74 09                           je 0x1409fbfd8
009FBFCF  83 FB 40                        cmp ebx, 0x40
009FBFD2  0F 85 0A 03 00 00               jne 0x1409fc2e2
009FBFD8  4C 8D 05 21 40 60 FF            lea r8, [rip - 0x9fbfdf]
009FBFDF  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
009FBFE3  44 8B EB                        mov r13d, ebx
009FBFE6  E9 8D FB FF FF                  jmp 0x1409fbb78
009FBFEB  41 83 FE 27                     cmp r14d, 0x27
009FBFEF  0F 8F 66 02 00 00               jg 0x1409fc25b
009FBFF5  0F 84 16 06 00 00               je 0x1409fc611
009FBFFB  41 83 FE 21                     cmp r14d, 0x21
009FBFFF  0F 8F BD 5E 13 00               jg 0x140b31ec2
009FC005  0F 84 E1 02 00 00               je 0x1409fc2ec
009FC00B  41 83 EE 1C                     sub r14d, 0x1c
009FC00F  0F 85 85 5C 13 00               jne 0x140b31c9a
009FC015  0F 57 C0                        xorps xmm0, xmm0
009FC018  F3 0F 7F 84 24 E0 02 00 00      movdqu xmmword ptr [rsp + 0x2e0], xmm0
009FC021  48 8B D1                        mov rdx, rcx
009FC024  48 8B CF                        mov rcx, rdi
009FC027  E8 68 E3 F1 FF                  call 0x14091a394
009FC02C  48 8B 87 D0 02 00 00            mov rax, qword ptr [rdi + 0x2d0]
009FC033  48 C1 E0 0C                     shl rax, 0xc
009FC037  48 89 84 24 D0 02 00 00         mov qword ptr [rsp + 0x2d0], rax
009FC03F  48 8B 87 B8 04 00 00            mov rax, qword ptr [rdi + 0x4b8]
009FC046  48 C1 E0 0C                     shl rax, 0xc
009FC04A  48 89 84 24 C8 02 00 00         mov qword ptr [rsp + 0x2c8], rax
009FC052  48 8B 87 20 06 00 00            mov rax, qword ptr [rdi + 0x620]
009FC059  48 C1 E0 0C                     shl rax, 0xc
009FC05D  48 89 84 24 D8 02 00 00         mov qword ptr [rsp + 0x2d8], rax
009FC065  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
009FC06A  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009FC06F  48 8B CF                        mov rcx, rdi
009FC072  E8 A9 E3 F1 FF                  call 0x14091a420
009FC077  4C 8D BC 24 C8 02 00 00         lea r15, [rsp + 0x2c8]
009FC07F  8B DE                           mov ebx, esi
009FC081  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
009FC086  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
009FC08B  48 85 FF                        test rdi, rdi
009FC08E  75 38                           jne 0x1409fc0c8
009FC090  85 DB                           test ebx, ebx
009FC092  79 0F                           jns 0x1409fc0a3
009FC094  4D 85 E4                        test r12, r12
009FC097  74 21                           je 0x1409fc0ba
009FC099  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
009FC09D  41 89 04 24                     mov dword ptr [r12], eax
009FC0A1  EB 17                           jmp 0x1409fc0ba
009FC0A3  40 38 74 24 40                  cmp byte ptr [rsp + 0x40], sil
009FC0A8  75 EA                           jne 0x1409fc094
009FC0AA  45 8B C5                        mov r8d, r13d
009FC0AD  49 8B D7                        mov rdx, r15
009FC0B0  49 8B CE                        mov rcx, r14
009FC0B3  E8 88 A7 CC FF                  call 0x1406c6840
009FC0B8  EB DA                           jmp 0x1409fc094
009FC0BA  EB 05                           jmp 0x1409fc0c1
009FC0BC  E9 87 FB FF FF                  jmp 0x1409fbc48
009FC0C1  8B C3                           mov eax, ebx
009FC0C3  E9 80 FB FF FF                  jmp 0x1409fbc48
009FC0C8  BA 50 73 51 79                  mov edx, 0x79517350
009FC0CD  48 8B CF                        mov rcx, rdi
009FC0D0  E8 0B B8 8F FF                  call 0x1402f78e0
009FC0D5  EB B9                           jmp 0x1409fc090
009FC0D7  0F 84 0F 02 00 00               je 0x1409fc2ec
009FC0DD  41 83 FE 06                     cmp r14d, 6
009FC0E1  0F 8F F4 56 13 00               jg 0x140b317db
009FC0E7  0F 84 26 04 00 00               je 0x1409fc513
009FC0ED  41 8B D6                        mov edx, r14d
009FC0F0  83 EA 01                        sub edx, 1
009FC0F3  0F 84 57 04 00 00               je 0x1409fc550
009FC0F9  83 EA 01                        sub edx, 1
009FC0FC  0F 85 00 56 13 00               jne 0x140b31702
009FC102  48 8B D1                        mov rdx, rcx
009FC105  48 8B CF                        mov rcx, rdi
009FC108  E8 83 E3 F1 FF                  call 0x14091a490
009FC10D  48 8B 87 F0 00 00 00            mov rax, qword ptr [rdi + 0xf0]
009FC114  48 89 84 24 38 04 00 00         mov qword ptr [rsp + 0x438], rax
009FC11C  48 8B 87 F8 00 00 00            mov rax, qword ptr [rdi + 0xf8]
009FC123  48 89 84 24 40 04 00 00         mov qword ptr [rsp + 0x440], rax
009FC12B  8B 87 04 01 00 00               mov eax, dword ptr [rdi + 0x104]
009FC131  89 84 24 48 04 00 00            mov dword ptr [rsp + 0x448], eax
009FC138  0F B6 87 4D 04 00 00            movzx eax, byte ptr [rdi + 0x44d]
009FC13F  89 84 24 58 04 00 00            mov dword ptr [rsp + 0x458], eax
009FC146  8B 87 44 02 00 00               mov eax, dword ptr [rdi + 0x244]
009FC14C  89 84 24 5C 04 00 00            mov dword ptr [rsp + 0x45c], eax
009FC153  B9 20 00 00 00                  mov ecx, 0x20
009FC158  0F B7 D1                        movzx edx, cx
009FC15B  66 89 4C 24 68                  mov word ptr [rsp + 0x68], cx
009FC160  44 0F B7 C6                     movzx r8d, si
009FC164  44 0F B7 8F 08 01 00 00         movzx r9d, word ptr [rdi + 0x108]
009FC16C  66 45 3B C1                     cmp r8w, r9w
009FC170  0F 82 3B 01 00 00               jb 0x1409fc2b1
009FC176  66 3B D1                        cmp dx, cx
009FC179  0F 84 7F 02 00 00               je 0x1409fc3fe
009FC17F  0F B7 C2                        movzx eax, dx
009FC182  48 8B 8C C7 10 01 00 00         mov rcx, qword ptr [rdi + rax*8 + 0x110]
009FC18A  48 89 8C 24 50 04 00 00         mov qword ptr [rsp + 0x450], rcx
009FC192  48 8B 87 E0 00 00 00            mov rax, qword ptr [rdi + 0xe0]
009FC199  48 89 84 24 20 04 00 00         mov qword ptr [rsp + 0x420], rax
009FC1A1  48 8B 87 E8 00 00 00            mov rax, qword ptr [rdi + 0xe8]
009FC1A8  48 89 84 24 28 04 00 00         mov qword ptr [rsp + 0x428], rax
009FC1B0  8B 54 24 6C                     mov edx, dword ptr [rsp + 0x6c]
009FC1B4  41 8B CE                        mov ecx, r14d
009FC1B7  E8 9C F2 FF FF                  call 0x1409fb458
009FC1BC  0D FF 7F 00 00                  or eax, 0x7fff
009FC1C1  8B 8F 00 01 00 00               mov ecx, dword ptr [rdi + 0x100]
009FC1C7  23 C8                           and ecx, eax
009FC1C9  89 8C 24 30 04 00 00            mov dword ptr [rsp + 0x430], ecx
009FC1D0  48 8B CF                        mov rcx, rdi
009FC1D3  41 83 FE 09                     cmp r14d, 9
009FC1D7  0F 84 43 57 13 00               je 0x140b31920
009FC1DD  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
009FC1E2  E8 19 DC F1 FF                  call 0x140919e00
009FC1E7  4C 8D BC 24 20 04 00 00         lea r15, [rsp + 0x420]
009FC1EF  E9 8B FE FF FF                  jmp 0x1409fc07f
009FC1F4  83 EA 01                        sub edx, 1
009FC1F7  0F 84 D0 58 13 00               je 0x140b31acd
009FC1FD  83 EA 01                        sub edx, 1
009FC200  0F 84 3B 58 13 00               je 0x140b31a41
009FC206  83 EA 01                        sub edx, 1
009FC209  0F 84 7A 03 00 00               je 0x1409fc589
009FC20F  83 EA 01                        sub edx, 1
009FC212  0F 84 55 03 00 00               je 0x1409fc56d
009FC218  83 EA 01                        sub edx, 1
009FC21B  0F 84 A4 57 13 00               je 0x140b319c5
009FC221  83 EA 01                        sub edx, 1
009FC224  0F 84 26 03 00 00               je 0x1409fc550
009FC22A  83 EA 01                        sub edx, 1
009FC22D  0F 85 FA 02 00 00               jne 0x1409fc52d
009FC233  4C 8D 84 24 10 05 00 00         lea r8, [rsp + 0x510]
009FC23B  48 8B D7                        mov rdx, rdi
009FC23E  E8 A1 BC F1 FF                  call 0x140917ee4
009FC243  4C 8D BC 24 10 05 00 00         lea r15, [rsp + 0x510]
009FC24B  85 C0                           test eax, eax
009FC24D  4C 0F 48 FE                     cmovs r15, rsi
009FC251  8B DE                           mov ebx, esi
009FC253  0F 48 D8                        cmovs ebx, eax
009FC256  E9 26 FE FF FF                  jmp 0x1409fc081
009FC25B  41 83 EE 2A                     sub r14d, 0x2a
009FC25F  0F 85 E2 60 13 00               jne 0x140b32347
009FC265  33 D2                           xor edx, edx
009FC267  45 8D 46 48                     lea r8d, [r14 + 0x48]
009FC26B  48 8D 8C 24 C0 04 00 00         lea rcx, [rsp + 0x4c0]
009FC273  E8 C8 A9 CC FF                  call 0x1406c6c40
009FC278  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
009FC27D  48 8B CF                        mov rcx, rdi
009FC280  E8 0B E2 F1 FF                  call 0x14091a490
009FC285  48 8D 94 24 C0 04 00 00         lea rdx, [rsp + 0x4c0]
009FC28D  48 8B CF                        mov rcx, rdi
009FC290  E8 B3 03 00 00                  call 0x1409fc648
009FC295  8B D8                           mov ebx, eax
009FC297  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
009FC29C  48 8B CF                        mov rcx, rdi
009FC29F  E8 5C DB F1 FF                  call 0x140919e00
009FC2A4  4C 8D BC 24 C0 04 00 00         lea r15, [rsp + 0x4c0]
009FC2AC  E9 D0 FD FF FF                  jmp 0x1409fc081
009FC2B1  41 0F B7 C0                     movzx eax, r8w
009FC2B5  48 39 B4 C7 10 01 00 00         cmp qword ptr [rdi + rax*8 + 0x110], rsi
009FC2BD  0F 85 28 01 00 00               jne 0x1409fc3eb
009FC2C3  66 45 03 C4                     add r8w, r12w
009FC2C7  E9 A0 FE FF FF                  jmp 0x1409fc16c
009FC2CC  8B C3                           mov eax, ebx
009FC2CE  2D 90 00 00 00                  sub eax, 0x90
009FC2D3  0F 84 FF FC FF FF               je 0x1409fbfd8
009FC2D9  83 F8 08                        cmp eax, 8
009FC2DC  0F 84 F6 FC FF FF               je 0x1409fbfd8
009FC2E2  B8 04 00 00 C0                  mov eax, 0xc0000004
009FC2E7  E9 5C F9 FF FF                  jmp 0x1409fbc48
009FC2EC  48 8B D1                        mov rdx, rcx
009FC2EF  48 8B CF                        mov rcx, rdi
009FC2F2  E8 99 E1 F1 FF                  call 0x14091a490
009FC2F7  48 8B 8F C0 04 00 00            mov rcx, qword ptr [rdi + 0x4c0]
009FC2FE  48 85 C9                        test rcx, rcx
009FC301  0F 84 96 00 00 00               je 0x1409fc39d
009FC307  8B 01                           mov eax, dword ptr [rcx]
009FC309  89 84 24 28 02 00 00            mov dword ptr [rsp + 0x228], eax
009FC310  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
009FC314  48 89 84 24 00 02 00 00         mov qword ptr [rsp + 0x200], rax
009FC31C  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
009FC320  48 89 84 24 08 02 00 00         mov qword ptr [rsp + 0x208], rax
009FC328  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
009FC32C  48 89 84 24 10 02 00 00         mov qword ptr [rsp + 0x210], rax
009FC334  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
009FC338  48 C1 E0 0C                     shl rax, 0xc
009FC33C  48 89 84 24 30 02 00 00         mov qword ptr [rsp + 0x230], rax
009FC344  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
009FC348  48 C1 E0 0C                     shl rax, 0xc
009FC34C  48 89 84 24 18 02 00 00         mov qword ptr [rsp + 0x218], rax
009FC354  8B D6                           mov edx, esi
009FC356  48 83 C1 3C                     add rcx, 0x3c
009FC35A  85 D2                           test edx, edx
009FC35C  74 79                           je 0x1409fc3d7
009FC35E  83 FA 01                        cmp edx, 1
009FC361  75 6A                           jne 0x1409fc3cd
009FC363  4C 8D 84 24 2C 02 00 00         lea r8, [rsp + 0x22c]
009FC36B  8B 41 F4                        mov eax, dword ptr [rcx - 0xc]
009FC36E  41 89 00                        mov dword ptr [r8], eax
009FC371  85 D2                           test edx, edx
009FC373  74 0F                           je 0x1409fc384
009FC375  83 FA 01                        cmp edx, 1
009FC378  75 67                           jne 0x1409fc3e1
009FC37A  4C 8D 84 24 38 02 00 00         lea r8, [rsp + 0x238]
009FC382  EB 08                           jmp 0x1409fc38c
009FC384  4C 8D 84 24 40 02 00 00         lea r8, [rsp + 0x240]
009FC38C  8B 01                           mov eax, dword ptr [rcx]
009FC38E  41 89 00                        mov dword ptr [r8], eax
009FC391  41 03 D4                        add edx, r12d
009FC394  48 83 C1 04                     add rcx, 4
009FC398  83 FA 03                        cmp edx, 3
009FC39B  7C BD                           jl 0x1409fc35a
009FC39D  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
009FC3A2  48 8B CF                        mov rcx, rdi
009FC3A5  E8 56 DA F1 FF                  call 0x140919e00
009FC3AA  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
009FC3AE  83 F8 30                        cmp eax, 0x30
009FC3B1  0F 84 86 5A 13 00               je 0x140b31e3d
009FC3B7  83 F8 38                        cmp eax, 0x38
009FC3BA  0F 84 E8 59 13 00               je 0x140b31da8
009FC3C0  4C 8D BC 24 00 02 00 00         lea r15, [rsp + 0x200]
009FC3C8  E9 B2 FC FF FF                  jmp 0x1409fc07f
009FC3CD  4C 8D 84 24 20 02 00 00         lea r8, [rsp + 0x220]
009FC3D5  EB 94                           jmp 0x1409fc36b
009FC3D7  4C 8D 84 24 3C 02 00 00         lea r8, [rsp + 0x23c]
009FC3DF  EB 8A                           jmp 0x1409fc36b
009FC3E1  4C 8D 84 24 24 02 00 00         lea r8, [rsp + 0x224]
009FC3E9  EB A1                           jmp 0x1409fc38c
009FC3EB  66 3B D1                        cmp dx, cx
009FC3EE  75 0E                           jne 0x1409fc3fe
009FC3F0  41 0F B7 D0                     movzx edx, r8w
009FC3F4  66 89 54 24 68                  mov word ptr [rsp + 0x68], dx
009FC3F9  E9 C5 FE FF FF                  jmp 0x1409fc2c3
009FC3FE  48 89 B4 24 50 04 00 00         mov qword ptr [rsp + 0x450], rsi
009FC406  E9 87 FD FF FF                  jmp 0x1409fc192
009FC40B  48 8D 84 24 C4 01 00 00         lea rax, [rsp + 0x1c4]
009FC413  E9 AE F9 FF FF                  jmp 0x1409fbdc6
009FC418  48 8D 84 24 BC 01 00 00         lea rax, [rsp + 0x1bc]
009FC420  E9 A1 F9 FF FF                  jmp 0x1409fbdc6
009FC425  41 83 FF 01                     cmp r15d, 1
009FC429  74 0D                           je 0x1409fc438
009FC42B  48 8D 8C 24 A8 01 00 00         lea rcx, [rsp + 0x1a8]
009FC433  E9 F1 F9 FF FF                  jmp 0x1409fbe29
009FC438  48 8D 8C 24 B8 01 00 00         lea rcx, [rsp + 0x1b8]
009FC440  E9 E4 F9 FF FF                  jmp 0x1409fbe29
009FC445  83 FB 01                        cmp ebx, 1
009FC448  0F 85 94 FE FF FF               jne 0x1409fc2e2
009FC44E  44 8B E3                        mov r12d, ebx
009FC451  45 8B EC                        mov r13d, r12d
009FC454  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
009FC459  4C 8D 05 A0 3B 60 FF            lea r8, [rip - 0x9fc460]
009FC460  E9 19 F7 FF FF                  jmp 0x1409fbb7e
009FC465  83 FB 10                        cmp ebx, 0x10
009FC468  0F 84 6A FB FF FF               je 0x1409fbfd8
009FC46E  83 FB 24                        cmp ebx, 0x24
009FC471  E9 5C FB FF FF                  jmp 0x1409fbfd2
009FC476  83 FB 10                        cmp ebx, 0x10
009FC479  0F 84 59 FB FF FF               je 0x1409fbfd8
009FC47F  83 FB 28                        cmp ebx, 0x28
009FC482  E9 4B FB FF FF                  jmp 0x1409fbfd2
009FC487  8B C3                           mov eax, ebx
009FC489  2D B0 01 00 00                  sub eax, 0x1b0
009FC48E  0F 84 44 FB FF FF               je 0x1409fbfd8
009FC494  83 E8 10                        sub eax, 0x10
009FC497  0F 84 3B FB FF FF               je 0x1409fbfd8
009FC49D  83 F8 10                        cmp eax, 0x10
009FC4A0  E9 2D FB FF FF                  jmp 0x1409fbfd2
009FC4A5  83 FB 50                        cmp ebx, 0x50
009FC4A8  0F 84 2A FB FF FF               je 0x1409fbfd8
009FC4AE  83 FB 58                        cmp ebx, 0x58
009FC4B1  E9 1C FB FF FF                  jmp 0x1409fbfd2
009FC4B6  83 FB 30                        cmp ebx, 0x30
009FC4B9  0F 84 19 FB FF FF               je 0x1409fbfd8
009FC4BF  83 FB 38                        cmp ebx, 0x38
009FC4C2  E9 0B FB FF FF                  jmp 0x1409fbfd2
009FC4C7  BA 50 73 51 79                  mov edx, 0x79517350
009FC4CC  48 8B CF                        mov rcx, rdi
009FC4CF  E8 3C 42 81 FF                  call 0x140210710
009FC4D4  E9 98 F7 FF FF                  jmp 0x1409fbc71
009FC4D9  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
009FC4DE  49 8B D6                        mov rdx, r14
009FC4E1  48 8B CF                        mov rcx, rdi
009FC4E4  E8 27 8C D8 FF                  call 0x140785110
009FC4E9  8B D8                           mov ebx, eax
009FC4EB  0F B6 44 24 40                  movzx eax, byte ptr [rsp + 0x40]
009FC4F0  85 DB                           test ebx, ebx
009FC4F2  41 0F 49 C4                     cmovns eax, r12d
009FC4F6  88 44 24 40                     mov byte ptr [rsp + 0x40], al
009FC4FA  8B C3                           mov eax, ebx
009FC4FC  C1 F8 1F                        sar eax, 0x1f
009FC4FF  83 E0 F8                        and eax, 0xfffffff8
009FC502  83 C0 08                        add eax, 8
009FC505  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
009FC509  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
009FC50E  E9 78 FB FF FF                  jmp 0x1409fc08b
009FC513  8B 87 24 02 00 00               mov eax, dword ptr [rdi + 0x224]
009FC519  89 84 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], eax
009FC520  4C 8D BC 24 B4 00 00 00         lea r15, [rsp + 0xb4]
009FC528  E9 52 FB FF FF                  jmp 0x1409fc07f
009FC52D  83 FA 01                        cmp edx, 1
009FC530  0F 85 9A 5E 13 00               jne 0x140b323d0
009FC536  8B 87 10 06 00 00               mov eax, dword ptr [rdi + 0x610]
009FC53C  C1 E8 0A                        shr eax, 0xa
009FC53F  41 22 C4                        and al, r12b
009FC542  88 44 24 5E                     mov byte ptr [rsp + 0x5e], al
009FC546  4C 8D 7C 24 5E                  lea r15, [rsp + 0x5e]
009FC54B  E9 2F FB FF FF                  jmp 0x1409fc07f
009FC550  48 8D 94 24 50 05 00 00         lea rdx, [rsp + 0x550]
009FC558  48 8B CF                        mov rcx, rdi
009FC55B  E8 EC C0 F1 FF                  call 0x14091864c
009FC560  4C 8D BC 24 50 05 00 00         lea r15, [rsp + 0x550]
009FC568  E9 12 FB FF FF                  jmp 0x1409fc07f
009FC56D  48 8B 87 38 02 00 00            mov rax, qword ptr [rdi + 0x238]
009FC574  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
009FC57C  4C 8D BC 24 E0 00 00 00         lea r15, [rsp + 0xe0]
009FC584  E9 F6 FA FF FF                  jmp 0x1409fc07f
009FC589  8B 87 50 04 00 00               mov eax, dword ptr [rdi + 0x450]
009FC58F  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
009FC596  4C 8D BC 24 B8 00 00 00         lea r15, [rsp + 0xb8]
009FC59E  E9 DC FA FF FF                  jmp 0x1409fc07f
009FC5A3  8B 00                           mov eax, dword ptr [rax]
009FC5A5  89 84 24 60 01 00 00            mov dword ptr [rsp + 0x160], eax
009FC5AC  48 8B 87 C0 04 00 00            mov rax, qword ptr [rdi + 0x4c0]
009FC5B3  8B 48 04                        mov ecx, dword ptr [rax + 4]
009FC5B6  89 8C 24 64 01 00 00            mov dword ptr [rsp + 0x164], ecx
009FC5BD  48 8B 8F C0 04 00 00            mov rcx, qword ptr [rdi + 0x4c0]
009FC5C4  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
009FC5C8  48 85 C0                        test rax, rax
009FC5CB  0F 85 96 5B 13 00               jne 0x140b32167
009FC5D1  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
009FC5D5  E9 8D 5B 13 00                  jmp 0x140b32167
009FC5DA  41 8B CF                        mov ecx, r15d
009FC5DD  E8 1A DE F1 FF                  call 0x14091a3fc
009FC5E2  85 02                           test dword ptr [rdx], eax
009FC5E4  0F 84 0C F8 FF FF               je 0x1409fbdf6
009FC5EA  42 8B 14 02                     mov edx, dword ptr [rdx + r8]
009FC5EE  E9 06 F8 FF FF                  jmp 0x1409fbdf9
009FC5F3  89 70 04                        mov dword ptr [rax + 4], esi
009FC5F6  48 8B 8F C0 04 00 00            mov rcx, qword ptr [rdi + 0x4c0]
009FC5FD  48 83 C1 48                     add rcx, 0x48
009FC601  33 D2                           xor edx, edx
009FC603  44 8D 42 40                     lea r8d, [rdx + 0x40]
009FC607  E8 34 A6 CC FF                  call 0x1406c6c40
009FC60C  E9 56 F8 FF FF                  jmp 0x1409fbe67
009FC611  48 85 FF                        test rdi, rdi
009FC614  0F 84 D3 5C 13 00               je 0x140b322ed
009FC61A  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
009FC622  48 8B CF                        mov rcx, rdi
009FC625  E8 16 5E AC FF                  call 0x1404c2440
009FC62A  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
009FC632  E9 BC 5C 13 00                  jmp 0x140b322f3
009FC637  B8 03 00 00 C0                  mov eax, 0xc0000003
009FC63C  E9 07 F6 FF FF                  jmp 0x1409fbc48
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryInformationJobObject(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m398;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m568;
    unsigned __int64 v_stack_m5A8;
    unsigned int v_stack_m5F4;
    unsigned __int64 v_stack_m5F8;
    unsigned __int64 v_stack_m698;
    unsigned int v_stack_m6A8;
    unsigned __int64 v_stack_m6B8;
    unsigned __int64 v_stack_m6C8;
    unsigned __int64 v_stack_m6D8;
    unsigned __int64 v_stack_m738;
    unsigned __int64 v_stack_m788;
    unsigned __int64 v_stack_m7A0;
    unsigned int v_stack_m7A8;
    unsigned __int64 v_stack_m7B8;
    unsigned __int64 v_stack_m7C8;
    unsigned __int64 v_stack_m7D0;
    unsigned __int64 v_stack_m7E0;
    unsigned __int64 v_stack_m7F0;
    unsigned __int64 v_stack_m7F8;
    unsigned __int64 v_stack_m808;
    unsigned __int64 v_stack_m818;
    unsigned __int64 v_stack_m828;
    unsigned __int64 v_stack_m838;
    unsigned __int64 v_stack_m848;
    unsigned __int64 v_stack_m858;
    unsigned __int64 v_stack_m868;
    unsigned __int64 v_stack_m8B8;
    unsigned __int64 v_stack_m8C8;
    unsigned __int64 v_stack_m8D8;
    unsigned __int64 v_stack_m8E8;
    unsigned __int64 v_stack_m958;
    unsigned int v_stack_m968;
    unsigned __int64 v_stack_m978;
    unsigned __int64 v_stack_m988;
    unsigned __int64 v_stack_m990;
    unsigned __int64 v_stack_m9A0;
    unsigned __int64 v_stack_m9B0;
    unsigned __int64 v_stack_m9C0;
    unsigned __int64 v_stack_m9C8;
    unsigned __int64 v_stack_m9D0;
    unsigned __int64 v_stack_m9D8;
    unsigned __int64 v_stack_m9E0;
    unsigned int v_stack_m9E8;
    unsigned __int64 v_stack_m9F0;
    unsigned __int64 v_stack_m9F8;
    unsigned int v_stack_m9FC;
    unsigned int v_stack_mA00;
    unsigned int v_stack_mA04;
    unsigned int v_stack_mA08;
    unsigned __int64 v_stack_mA10;
    unsigned __int64 v_stack_mA18;
    unsigned __int64 v_stack_mA28;
    unsigned int v_stack_mA2C;
    unsigned int v_stack_mA30;
    unsigned __int64 v_stack_mA38;
    unsigned __int64 v_stack_mA40;
    unsigned int v_stack_mA48;
    unsigned int v_stack_mA4C;
    unsigned __int16 v_stack_mA50;
    unsigned __int64 v_stack_mA58;
    unsigned __int8 v_stack_mA59;
    unsigned __int8 v_stack_mA5A;
    unsigned __int8 v_stack_mA5B;
    unsigned __int8 v_stack_mA5C;
    unsigned int v_stack_mA60;
    unsigned __int64 v_stack_mA68;
    unsigned __int64 v_stack_mA70;
    unsigned __int8 v_stack_mA78;
    unsigned __int64 v_stack_mA80;
    unsigned __int64 v_stack_mA88;
    unsigned __int64 v_stack_mA90;
    unsigned int v_stack_mA98;
    unsigned __int64 v_stack_p160;
    unsigned int v_stack_p164;
    unsigned __int64 v_stack_p168;
    unsigned __int64 v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p198;
    unsigned __int64 v_stack_p1A0;
    unsigned int v_stack_p1A8;
    unsigned __int64 v_stack_p1AC;
    unsigned __int64 v_stack_p1B0;
    unsigned __int64 v_stack_p1B8;
    unsigned __int64 v_stack_p1BC;
    unsigned __int64 v_stack_p1C0;
    unsigned __int64 v_stack_p1C4;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p200;
    unsigned __int64 v_stack_p208;
    unsigned __int64 v_stack_p210;
    unsigned __int64 v_stack_p218;
    unsigned __int64 v_stack_p220;
    unsigned __int64 v_stack_p224;
    unsigned int v_stack_p228;
    unsigned __int64 v_stack_p22C;
    unsigned __int64 v_stack_p230;
    unsigned __int64 v_stack_p238;
    unsigned __int64 v_stack_p23C;
    unsigned __int64 v_stack_p240;
    unsigned __int16 v_stack_p28;
    unsigned __int64 v_stack_p2C8;
    unsigned __int64 v_stack_p2D0;
    unsigned __int64 v_stack_p2D8;
    unsigned __int64 v_stack_p2E0;
    unsigned int v_stack_p380;
    unsigned int v_stack_p384;
    unsigned __int64 v_stack_p388;
    unsigned __int64 v_stack_p390;
    unsigned __int64 v_stack_p398;
    unsigned __int64 v_stack_p3A0;
    unsigned __int64 v_stack_p3A8;
    unsigned __int64 v_stack_p3B0;
    unsigned __int64 v_stack_p3B8;
    unsigned __int64 v_stack_p3C0;
    unsigned __int64 v_stack_p3C8;
    unsigned int v_stack_p3D0;
    unsigned int v_stack_p3D4;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p420;
    unsigned __int64 v_stack_p428;
    unsigned int v_stack_p430;
    unsigned __int64 v_stack_p438;
    unsigned __int64 v_stack_p440;
    unsigned int v_stack_p448;
    unsigned __int64 v_stack_p450;
    unsigned int v_stack_p458;
    unsigned int v_stack_p45C;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p4C0;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p510;
    unsigned __int64 v_stack_p550;
    unsigned __int16 v_stack_p58;
    unsigned __int64 v_stack_p598;
    unsigned __int8 v_stack_p5A;
    unsigned __int64 v_stack_p5A0;
    unsigned __int8 v_stack_p5E;
    unsigned __int64 v_stack_p60;
    unsigned __int16 v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned int v_stack_pB4;
    unsigned int v_stack_pB8;
    unsigned __int64 v_stack_pBC;
    unsigned __int64 v_stack_pE0;

    v_rsp = (v_rsp) - (0xA80ULL);
    result = (*(unsigned __int64 *)(v_rip + 4255430)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mA4C = (unsigned int)((unsigned int)(a4));
    v_stack_mA70 = a3;
    v_stack_mA18 = a1;
    v_stack_mA68 = a5;
    v_stack_mA10 = a3;
    v_stack_mA38 = a5;
    a2 = 0;
    result = memset(v_stack_m568, a2, 464, a4);
    v_stack_m868 = v_xmm0;
    v_rsi = 0;
    v_stack_mA48 = 0;
    a2 = 0;
    result = memset(v_stack_m398, a2, 264, a4);
    v_stack_mA78 = 0;
    v_stack_mA5A = 0;
    v_stack_m9F0 = 0;
    v_stack_m9F8 = 0;
    v_stack_mA08 = 0;
    v_stack_m9D8 = 0;
    v_stack_mA00 = 0;
    result = 0;
    v_stack_m7C8 = v_xmm0;
    v_stack_m7B8 = v_xmm0;
    v_stack_m7A8 = 0;
    v_stack_m7A0 = v_xmm0;
    v_stack_m9E0 = 0;
    v_stack_mA04 = 0;
    v_stack_m9C8 = 0;
    a2 = 0;
    result = memset(v_stack_m698, a2, 152, a4);
    v_stack_m8C8 = v_xmm0;
    v_stack_mA50 = 0;
    v_stack_mA30 = 0;
    result = 0;
    v_stack_m5F4 = 0;
    a2 = 0;
    result = memset(v_stack_m5F8, a2, v_rsi + 68, a4);
    v_stack_mA40 = 0;
    v_stack_m9E8 = 0;
    a2 = 0;
    result = memset(v_stack_m958, a2, v_rsi + 104, a4);
    a2 = 0;
    result = memset(v_stack_m788, a2, v_rsi + 80, a4);
    a2 = 0;
    result = memset(v_stack_m738, a2, v_rsi + 88, a4);
    result = 0;
    v_stack_m7F0 = v_xmm0;
    v_stack_m7E0 = v_xmm0;
    v_stack_m7D0 = 0;
    v_stack_m8E8 = v_xmm0;
    a2 = 0;
    result = memset(v_stack_m8B8, a2, v_rsi + 72, a4);
    v_stack_m858 = v_xmm0;
    v_stack_m848 = v_xmm0;
    v_stack_m838 = v_xmm0;
    result = 0;
    v_stack_m828 = v_xmm1;
    v_stack_m818 = v_xmm1;
    v_stack_m808 = v_xmm1;
    v_stack_m7F8 = 0;
    v_stack_m9FC = 0;
    v_stack_m9C0 = v_xmm0;
    v_stack_m988 = v_xmm0;
    v_stack_m978 = v_xmm0;
    v_stack_m968 = 0;
    v_stack_m9D0 = 0;
    a2 = 0;
    result = memset(v_stack_m5A8, a2, v_rsi + 64, a4);
    v_stack_m8D8 = v_xmm0;
    result = 0;
    v_stack_m9B0 = v_xmm1;
    v_stack_m9A0 = v_xmm1;
    v_stack_m990 = 0;
    v_stack_m6D8 = v_xmm0;
    v_stack_m6C8 = v_xmm0;
    v_stack_m6B8 = v_xmm0;
    v_stack_m6A8 = 0;
    v_stack_mA28 = 0;
    v_stack_mA5B = 0;
    v_stack_mA59 = 0;
    if (((unsigned int)((int)(a2) - 1)) > 50) goto loc_009FC637;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((int)(a2)))) - (9));
    if (condition_is_equal) goto loc_009FC2CC;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_009FC4B6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009FC4A5;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_009FC487;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009FBFCA;
    a1 = (unsigned int)((a1) - (8));
    if (condition_is_equal) goto loc_009FC476;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_rsi + 2)));
    if (condition_is_equal) goto loc_009FC465;
    if (((unsigned int)(a1)) == 13) goto loc_009FC445;
    v_stack_mA60 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 10468194 + (int)(a2) * 4 + 11855148)));
loc_009FBB78:
loc_009FBB7E:
    v_stack_mA2C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 10468194 + (int)(a2) * 4 + 11855148)));
    v_stack_mA58 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_mA5C = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_009FBC00;
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_009FBBCA;
loc_009FBBB8:
    if (a5 == 0) goto loc_009FBBF8;
    a2 = v_rsi + 2;
    if (a5 < (v_rsi + 2)) { a2 = a5; }
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    goto loc_009FBBF8;
loc_009FBBCA:
    result = (unsigned int)(*(unsigned int *)(a2));
    if (((a3) & ((unsigned int)(*(unsigned int *)(a2)) - 1)) != 0) {
        result = ExRaiseDatatypeMisalignment((unsigned int)(*(unsigned int *)(a2)) - 1, a2, v_rip - 10468194, a4);
    }
    if ((a3 + (unsigned int)(a4) * 1) > a2) goto loc_009FBBEF;
    if ((a3 + (unsigned int)(a4) * 1) < a3) {
        result = *(unsigned __int8 *)(a2);
    }
    goto loc_009FBBB8;
loc_009FBBF8:
    goto loc_009FBC00;
loc_009FBC00:
    if (v_stack_mA18 == 0) goto loc_009FBF95;
    v_stack_mA80 = 0;
    v_stack_mA88 = 0;
    v_stack_mA90 = v_stack_mA40;
    v_stack_mA98 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_mA18, 4, *(unsigned __int64 *)(v_rip + 6074432), (unsigned __int8)(v_stack_mA5C));
    if (!sign_flag) goto loc_009FBC6C;
loc_009FBC48:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, 4, *(unsigned __int64 *)(v_rip + 6074432), (unsigned __int8)(v_stack_mA5C));
    v_rsp = (v_rsp) + (0xA80ULL);
    return result;
loc_009FBC6C:
loc_009FBC71:
loc_009FBC76:
    v_stack_p70 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 10468194 + (int)(a2) * 4 + 11855148)));
    v_stack_p40 = 0;
    if (((unsigned int)((int)(a2))) > 26) goto loc_009FBFEB;
    if (((unsigned int)((int)(a2))) == 26) goto loc_009FC4D9;
    if (((unsigned int)((int)(a2))) <= 12) goto loc_009FC0D7;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((int)(a2)))) - (13));
    if (condition_is_not_equal) goto loc_009FC1F4;
    result = 0;
    v_stack_p58 = 0;
    v_stack_p5A = 0;
    result = PspQueryJobHierarchyAccountingInformation(v_stack_p78, v_stack_p550, *(unsigned __int64 *)(v_rip + 6074432), (unsigned __int8)(v_stack_mA5C));
    v_stack_p168 = v_stack_p598;
    v_stack_p178 = v_stack_p5A0;
    v_stack_p188 = v_stack_p550;
    result = PspLockJobExclusive(v_stack_p78, v_stack_p60, *(unsigned __int64 *)(v_rip + 6074432), (unsigned __int8)(v_stack_mA5C));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p78 + 1552))) & ((unsigned int)((unsigned int)(0x4008ULL))));
    v_rdi = v_stack_p78;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x4008ULL)))) {
        v_rdi = v_stack_p78;
    }
    a2 = 0;
    result = PspLockJobMemoryLimitsShared(v_rdi, a2, *(unsigned __int64 *)(v_rip + 6074432), (unsigned __int8)(v_stack_mA5C));
    result = (*(unsigned __int64 *)(v_rdi + 1208)) << (12);
    v_stack_p198 = result;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_rdi + 1264;
        result = ExfReleasePushLockShared(a1, a2, *(unsigned __int64 *)(v_rip + 6074432), (unsigned __int8)(v_stack_mA5C));
    }
    result = KeAbPostRelease(v_rdi + 1264, a2, *(unsigned __int64 *)(v_rip + 6074432), (unsigned __int8)(v_stack_mA5C));
    if (*(unsigned __int64 *)(v_stack_p78 + 1216) != 0) goto loc_009FC5A3;
    v_stack_p160 = 0;
    v_stack_p170 = 0;
    v_stack_p180 = 0;
    v_stack_p190 = 0;
    v_stack_p1B0 = 0;
    v_stack_p1A0 = 0;
loc_009FBDAD:
    if (0 == 0) goto loc_009FC40B;
    if (0 == 1) goto loc_009FC418;
loc_009FBDC6:
    *(unsigned int *)(v_stack_p1AC) = 0;
    a1 = (unsigned int)((0) + (1));
    if (((unsigned int)(a1)) < 3) goto loc_009FBDAD;
    v_stack_p80 = 60;
loc_009FBDE6:
    if (*(unsigned __int64 *)(v_stack_p78 + 1216) != 0) goto loc_009FC5DA;
loc_009FBDF6:
loc_009FBDF9:
    v_stack_p88 = 1;
    v_stack_p20 = 0;
    result = PspQueryRateControlHistory(v_stack_p78, 1, *(unsigned __int8 *)(v_stack_p58), v_stack_pBC);
    if (0 != 0) goto loc_009FC425;
loc_009FBE29:
    *(unsigned int *)(v_stack_p1C0) = (unsigned int)((unsigned int)(v_stack_pBC));
    v_r15 = (unsigned int)((0) + (1));
    a3 = (v_stack_p80) + (4);
    v_stack_p80 = a3;
    v_rbx = (v_stack_p58) + (1);
    if (((unsigned int)(v_r15)) < 3) goto loc_009FBDE6;
    if (*(unsigned __int64 *)(v_stack_p78 + 1216) != 0) goto loc_009FC5F3;
loc_009FBE67:
    result = PspUnlockJob(v_stack_p78, v_stack_p60, a3, v_stack_pBC);
    v_stack_p388 = v_stack_p168;
    v_stack_p390 = v_stack_p170;
    v_stack_p398 = v_stack_p178;
    v_stack_p3A0 = v_stack_p180;
    v_stack_p3A8 = v_stack_p188;
    v_stack_p3B0 = v_stack_p190;
    v_stack_p3B8 = v_stack_p198;
    v_stack_p3C0 = v_stack_p1B0;
    v_stack_p3C8 = v_stack_p1A0;
    v_stack_p3D0 = (unsigned int)((unsigned int)(v_stack_p1A8));
    v_stack_p3D4 = (unsigned int)((unsigned int)(v_stack_p1AC));
    result = (unsigned int)(((unsigned int)(v_stack_p160)) & ((unsigned int)((unsigned int)(0x278204ULL))));
    v_stack_p380 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(v_stack_p164)) & ((unsigned int)((unsigned int)(0x278204ULL))));
    v_stack_p384 = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 6073244)) & (0x80000ULL)) == 0) goto loc_009FC081;
    v_stack_p28 = 0x726ULL;
    v_stack_p20 = 0;
    result = EtwTraceJobSetQuery(v_stack_p78, (unsigned int)((unsigned int)((int)(a2))), v_stack_p160, v_stack_p88);
    goto loc_009FC081;
loc_009FBF95:
    v_stack_p78 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 184) + 672);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 184) + 672) != 0) goto loc_009FC4C7;
    if ((((unsigned int)((int)(a2) - 31)) & (0xFFFFFFF7ULL)) == 0) goto loc_009FBC76;
    goto loc_009FBC48;
loc_009FBFCA:
    if (0 == 40) goto loc_009FBFD8;
loc_009FBFD2:
    if (0 != 64) goto loc_009FC2E2;
loc_009FBFD8:
    v_stack_p58 = 0;
    goto loc_009FBB78;
loc_009FBFEB:
    if (((unsigned int)((int)(a2))) > 39) goto loc_009FC25B;
    if (((unsigned int)((int)(a2))) == 39) goto loc_009FC611;
    if (((unsigned int)((int)(a2))) == 33) goto loc_009FC2EC;
    v_r14 = (unsigned int)(((int)(a2)) - (28));
    v_stack_p2E0 = v_xmm0;
    result = PspLockJobMemoryLimitsShared(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 184) + 672), v_stack_p78, v_rip - 10469343, v_stack_p88);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 184) + 672) + 720)) << (12);
    v_stack_p2D0 = result;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 184) + 672) + 1208)) << (12);
    v_stack_p2C8 = result;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 184) + 672) + 1568)) << (12);
    v_stack_p2D8 = result;
    result = PspUnlockJobMemoryLimitsShared(v_stack_p78, v_stack_p60, v_rip - 10469343, v_stack_p88);
loc_009FC07F:
loc_009FC081:
loc_009FC08B:
    if (v_stack_p78 != 0) goto loc_009FC0C8;
loc_009FC090:
    if (!sign_flag) goto loc_009FC0A3;
loc_009FC094:
    if (v_stack_p50 == 0) goto loc_009FC0BA;
    *(unsigned int *)(v_stack_p50) = (unsigned int)((unsigned int)(v_stack_p70));
    goto loc_009FC0BA;
loc_009FC0A3:
    if (v_stack_p40 != 0) goto loc_009FC094;
    result = memcpy(v_stack_p48, v_stack_p2C8, 0, v_stack_p88);
    goto loc_009FC094;
loc_009FC0BA:
    goto loc_009FC0C1;
loc_009FC0C1:
    goto loc_009FBC48;
loc_009FC0C8:
    result = ObfDereferenceObjectWithTag(v_stack_p78, (unsigned int)(0x79517350ULL), 0, v_stack_p88);
    goto loc_009FC090;
loc_009FC0D7:
    if (v_stack_p40 == 0) goto loc_009FC2EC;
    if (((unsigned int)(v_stack_p48)) == 6) goto loc_009FC513;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p48))) - (1));
    if (condition_is_equal) goto loc_009FC550;
    a2 = (unsigned int)((a2) - (1));
    result = PspLockJobShared(v_stack_p78, v_stack_p78, 0, v_stack_p88);
    v_stack_p438 = *(unsigned __int64 *)(v_stack_p78 + 240);
    v_stack_p440 = *(unsigned __int64 *)(v_stack_p78 + 248);
    v_stack_p448 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p78 + 260)));
    v_stack_p458 = (unsigned int)(*(unsigned __int8 *)(v_stack_p78 + 1101));
    v_stack_p45C = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p78 + 580)));
    v_stack_p68 = 32;
loc_009FC16C:
    if (0 < ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p78 + 264)))) goto loc_009FC2B1;
    if (32 == 32) goto loc_009FC3FE;
    v_stack_p450 = *(unsigned __int64 *)(v_stack_p78 + 32 * 8 + 272);
loc_009FC192:
    v_stack_p420 = *(unsigned __int64 *)(v_stack_p78 + 224);
    v_stack_p428 = *(unsigned __int64 *)(v_stack_p78 + 232);
    result = PspGetJobLimitInformationValidFlags((unsigned int)((unsigned int)(v_stack_p48)), (unsigned int)(v_stack_p6C), 0, *(unsigned __int16 *)(v_stack_p78 + 264));
    result = (unsigned int)((result) | (0x7FFFULL));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p78 + 256))) & ((unsigned int)(result)));
    v_stack_p430 = (unsigned int)(a1);
    result = PspUnlockJob(v_stack_p78, v_stack_p60, 0, *(unsigned __int16 *)(v_stack_p78 + 264));
    goto loc_009FC07F;
loc_009FC1F4:
    a2 = (unsigned int)((v_stack_p60) - (1));
    a2 = (unsigned int)((a2) - (1));
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009FC589;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009FC56D;
    a2 = (unsigned int)((a2) - (1));
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009FC550;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_not_equal) goto loc_009FC52D;
    result = PspAllocateAndQueryNotificationChannel(v_stack_p78, v_stack_p78, v_stack_p510, *(unsigned __int16 *)(v_stack_p78 + 264));
    v_r15 = v_stack_p510;
    if (sign_flag) { v_r15 = 0; }
    v_rbx = 0;
    if (sign_flag) { v_rbx = (unsigned int)(result); }
    goto loc_009FC081;
loc_009FC25B:
    v_r14 = (unsigned int)((v_stack_p48) - (42));
    a2 = 0;
    result = memset(v_stack_p4C0, a2, v_r14 + 72, *(unsigned __int16 *)(v_stack_p78 + 264));
    result = PspLockJobShared(v_stack_p78, v_stack_p60, v_r14 + 72, *(unsigned __int16 *)(v_stack_p78 + 264));
    result = PspQueryJobIoAttribution(v_stack_p78, v_stack_p4C0, v_r14 + 72, *(unsigned __int16 *)(v_stack_p78 + 264));
    result = PspUnlockJob(v_stack_p78, v_stack_p60, v_r14 + 72, *(unsigned __int16 *)(v_stack_p78 + 264));
    goto loc_009FC081;
loc_009FC2B1:
    if ((*(unsigned __int64 *)(v_stack_p78 + (unsigned __int16)(v_r14 + 72) * 8 + 272)) != 0) goto loc_009FC3EB;
loc_009FC2C3:
    a3 = (unsigned __int16)((v_r14 + 72) + ((unsigned __int16)(v_stack_p50)));
    goto loc_009FC16C;
loc_009FC2CC:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - (144));
    if (condition_is_equal) goto loc_009FBFD8;
    if (((unsigned int)(result)) == 8) goto loc_009FBFD8;
loc_009FC2E2:
    goto loc_009FBC48;
loc_009FC2EC:
    result = PspLockJobShared(v_stack_p78, v_stack_p78, a3, *(unsigned __int16 *)(v_stack_p78 + 264));
    if (*(unsigned __int64 *)(v_stack_p78 + 1216) == 0) goto loc_009FC39D;
    v_stack_p228 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + 1216))));
    v_stack_p200 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 1216) + 8);
    v_stack_p208 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 1216) + 16);
    v_stack_p210 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 1216) + 24);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 1216) + 32)) << (12);
    v_stack_p230 = result;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p78 + 1216) + 40)) << (12);
    v_stack_p218 = result;
    a1 = (*(unsigned __int64 *)(v_stack_p78 + 1216)) + (60);
loc_009FC35A:
    if (0 == 0) goto loc_009FC3D7;
    if (0 != 1) goto loc_009FC3CD;
loc_009FC36B:
    *(unsigned int *)(v_stack_p22C) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 - 12)));
    if (0 == 0) goto loc_009FC384;
    if (0 != 1) goto loc_009FC3E1;
    goto loc_009FC38C;
loc_009FC384:
loc_009FC38C:
    *(unsigned int *)(v_stack_p240) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    a2 = (unsigned int)((0) + ((unsigned int)(v_stack_p50)));
    a1 = (a1) + (4);
    if (a2 < 3) goto loc_009FC35A;
loc_009FC39D:
    result = PspUnlockJob(v_stack_p78, v_stack_p60, v_stack_p240, *(unsigned __int16 *)(v_stack_p78 + 264));
    goto loc_009FC07F;
loc_009FC3CD:
    goto loc_009FC36B;
loc_009FC3D7:
    goto loc_009FC36B;
loc_009FC3E1:
    goto loc_009FC38C;
loc_009FC3EB:
    if (((unsigned __int16)(v_stack_p60)) != ((unsigned __int16)(v_stack_p78))) goto loc_009FC3FE;
    v_stack_p68 = (unsigned __int16)((unsigned __int16)(v_stack_p224));
    goto loc_009FC2C3;
loc_009FC3FE:
    v_stack_p450 = 0;
    goto loc_009FC192;
loc_009FC40B:
    goto loc_009FBDC6;
loc_009FC418:
    goto loc_009FBDC6;
loc_009FC425:
    if (((unsigned int)(v_stack_p200)) == 1) goto loc_009FC438;
    goto loc_009FBE29;
loc_009FC438:
    goto loc_009FBE29;
loc_009FC445:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 1) goto loc_009FC2E2;
    v_stack_p58 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_009FBB7E;
loc_009FC465:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 16) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC476:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 16) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC487:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - (432));
    if (condition_is_equal) goto loc_009FBFD8;
    result = (unsigned int)((result) - (16));
    if (condition_is_equal) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC4A5:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 80) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC4B6:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 48) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC4C7:
    result = ObfReferenceObjectWithTag(v_stack_p78, (unsigned int)(0x79517350ULL), v_rip - 10470496, *(unsigned __int16 *)(v_stack_p78 + 264));
    goto loc_009FBC71;
loc_009FC4D9:
    result = PspQueryJobHierarchyInterferenceCount(v_stack_p78, v_stack_p48, v_rip - 10470496, *(unsigned __int16 *)(v_stack_p78 + 264));
    result = v_stack_p40;
    if (!sign_flag) { result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))); }
    v_stack_p40 = (unsigned __int8)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) >> (31));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    result = (unsigned int)((result) + (8));
    v_stack_p70 = (unsigned int)(result);
    goto loc_009FC08B;
loc_009FC513:
    v_stack_pB4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p78 + 548)));
    goto loc_009FC07F;
loc_009FC52D:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p78 + 1552))) >> (10));
    result = (unsigned __int8)((result) & ((unsigned __int8)(v_stack_p50)));
    v_stack_p5E = (unsigned __int8)(result);
    goto loc_009FC07F;
loc_009FC550:
    result = PspQueryJobHierarchyAccountingInformation(v_stack_p78, v_stack_p550, v_rip - 10470496, *(unsigned __int16 *)(v_stack_p78 + 264));
    goto loc_009FC07F;
loc_009FC56D:
    v_stack_pE0 = *(unsigned __int64 *)(v_stack_p78 + 568);
    goto loc_009FC07F;
loc_009FC589:
    v_stack_pB8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p78 + 1104)));
    goto loc_009FC07F;
loc_009FC5A3:
    v_stack_p160 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_p78 + 1104)))));
    v_stack_p164 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p78 + 1216) + 4)));
loc_009FC5DA:
    result = PspRateControlLimitFlag((unsigned int)((unsigned int)(v_stack_pB8)), v_stack_p550, v_rip - 10470496, *(unsigned __int16 *)(v_stack_p78 + 264));
    if (((*(unsigned int *)(v_stack_p550)) & ((unsigned int)(result))) == 0) goto loc_009FBDF6;
    goto loc_009FBDF9;
loc_009FC5F3:
    *(unsigned int *)(result + 4) = 0;
    a1 = (*(unsigned __int64 *)(v_stack_p78 + 1216)) + (72);
    a2 = 0;
    result = memset(a1, a2, a2 + 64, *(unsigned __int16 *)(v_stack_p78 + 264));
    goto loc_009FBE67;
loc_009FC611:
    result = PsGetJobServerSilo(v_stack_p78, v_stack_p90, a2 + 64, *(unsigned __int16 *)(v_stack_p78 + 264));
loc_009FC637:
    goto loc_009FBC48;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryInformationJobObject(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m398;
    uint64_t v_stack_m48;
    uint64_t v_stack_m568;
    uint64_t v_stack_m5A8;
    uint32_t v_stack_m5F4;
    uint64_t v_stack_m5F8;
    uint64_t v_stack_m698;
    uint32_t v_stack_m6A8;
    uint64_t v_stack_m6B8;
    uint64_t v_stack_m6C8;
    uint64_t v_stack_m6D8;
    uint64_t v_stack_m738;
    uint64_t v_stack_m788;
    uint64_t v_stack_m7A0;
    uint32_t v_stack_m7A8;
    uint64_t v_stack_m7B8;
    uint64_t v_stack_m7C8;
    uint64_t v_stack_m7D0;
    uint64_t v_stack_m7E0;
    uint64_t v_stack_m7F0;
    uint64_t v_stack_m7F8;
    uint64_t v_stack_m808;
    uint64_t v_stack_m818;
    uint64_t v_stack_m828;
    uint64_t v_stack_m838;
    uint64_t v_stack_m848;
    uint64_t v_stack_m858;
    uint64_t v_stack_m868;
    uint64_t v_stack_m8B8;
    uint64_t v_stack_m8C8;
    uint64_t v_stack_m8D8;
    uint64_t v_stack_m8E8;
    uint64_t v_stack_m958;
    uint32_t v_stack_m968;
    uint64_t v_stack_m978;
    uint64_t v_stack_m988;
    uint64_t v_stack_m990;
    uint64_t v_stack_m9A0;
    uint64_t v_stack_m9B0;
    uint64_t v_stack_m9C0;
    uint64_t v_stack_m9C8;
    uint64_t v_stack_m9D0;
    uint64_t v_stack_m9D8;
    uint64_t v_stack_m9E0;
    uint32_t v_stack_m9E8;
    uint64_t v_stack_m9F0;
    uint64_t v_stack_m9F8;
    uint32_t v_stack_m9FC;
    uint32_t v_stack_mA00;
    uint32_t v_stack_mA04;
    uint32_t v_stack_mA08;
    uint64_t v_stack_mA10;
    uint64_t v_stack_mA18;
    uint64_t v_stack_mA28;
    uint32_t v_stack_mA2C;
    uint32_t v_stack_mA30;
    uint64_t v_stack_mA38;
    uint64_t v_stack_mA40;
    uint32_t v_stack_mA48;
    uint32_t v_stack_mA4C;
    uint16_t v_stack_mA50;
    uint64_t v_stack_mA58;
    uint8_t v_stack_mA59;
    uint8_t v_stack_mA5A;
    uint8_t v_stack_mA5B;
    uint8_t v_stack_mA5C;
    uint32_t v_stack_mA60;
    uint64_t v_stack_mA68;
    uint64_t v_stack_mA70;
    uint8_t v_stack_mA78;
    uint64_t v_stack_mA80;
    uint64_t v_stack_mA88;
    uint64_t v_stack_mA90;
    uint32_t v_stack_mA98;
    uint64_t v_stack_p160;
    uint32_t v_stack_p164;
    uint64_t v_stack_p168;
    uint64_t v_stack_p170;
    uint64_t v_stack_p178;
    uint64_t v_stack_p180;
    uint64_t v_stack_p188;
    uint64_t v_stack_p190;
    uint64_t v_stack_p198;
    uint64_t v_stack_p1A0;
    uint32_t v_stack_p1A8;
    uint64_t v_stack_p1AC;
    uint64_t v_stack_p1B0;
    uint64_t v_stack_p1B8;
    uint64_t v_stack_p1BC;
    uint64_t v_stack_p1C0;
    uint64_t v_stack_p1C4;
    uint32_t v_stack_p20;
    uint64_t v_stack_p200;
    uint64_t v_stack_p208;
    uint64_t v_stack_p210;
    uint64_t v_stack_p218;
    uint64_t v_stack_p220;
    uint64_t v_stack_p224;
    uint32_t v_stack_p228;
    uint64_t v_stack_p22C;
    uint64_t v_stack_p230;
    uint64_t v_stack_p238;
    uint64_t v_stack_p23C;
    uint64_t v_stack_p240;
    uint16_t v_stack_p28;
    uint64_t v_stack_p2C8;
    uint64_t v_stack_p2D0;
    uint64_t v_stack_p2D8;
    uint64_t v_stack_p2E0;
    uint32_t v_stack_p380;
    uint32_t v_stack_p384;
    uint64_t v_stack_p388;
    uint64_t v_stack_p390;
    uint64_t v_stack_p398;
    uint64_t v_stack_p3A0;
    uint64_t v_stack_p3A8;
    uint64_t v_stack_p3B0;
    uint64_t v_stack_p3B8;
    uint64_t v_stack_p3C0;
    uint64_t v_stack_p3C8;
    uint32_t v_stack_p3D0;
    uint32_t v_stack_p3D4;
    uint8_t v_stack_p40;
    uint64_t v_stack_p420;
    uint64_t v_stack_p428;
    uint32_t v_stack_p430;
    uint64_t v_stack_p438;
    uint64_t v_stack_p440;
    uint32_t v_stack_p448;
    uint64_t v_stack_p450;
    uint32_t v_stack_p458;
    uint32_t v_stack_p45C;
    uint64_t v_stack_p48;
    uint64_t v_stack_p4C0;
    uint64_t v_stack_p50;
    uint64_t v_stack_p510;
    uint64_t v_stack_p550;
    uint16_t v_stack_p58;
    uint64_t v_stack_p598;
    uint8_t v_stack_p5A;
    uint64_t v_stack_p5A0;
    uint8_t v_stack_p5E;
    uint64_t v_stack_p60;
    uint16_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint32_t v_stack_p88;
    uint64_t v_stack_p90;
    uint32_t v_stack_pB4;
    uint32_t v_stack_pB8;
    uint64_t v_stack_pBC;
    uint64_t v_stack_pE0;

    local_rsp = (local_rsp) - (0xA80ULL);
    result = (*(uint64_t *)(v_rip + 0x40EEC6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mA4C = (uint32_t)((uint32_t)(Arg4));
    v_stack_mA70 = Arg3;
    v_stack_mA18 = Arg1;
    v_stack_mA68 = Arg5;
    v_stack_mA10 = Arg3;
    v_stack_mA38 = Arg5;
    Arg2 = 0;
    result = memset(v_stack_m568, Arg2, 464, Arg4);
    v_stack_m868 = v_xmm0;
    local_rsi = 0;
    v_stack_mA48 = 0;
    Arg2 = 0;
    result = memset(v_stack_m398, Arg2, 264, Arg4);
    v_stack_mA78 = 0;
    v_stack_mA5A = 0;
    v_stack_m9F0 = 0;
    v_stack_m9F8 = 0;
    v_stack_mA08 = 0;
    v_stack_m9D8 = 0;
    v_stack_mA00 = 0;
    result = 0;
    v_stack_m7C8 = v_xmm0;
    v_stack_m7B8 = v_xmm0;
    v_stack_m7A8 = 0;
    v_stack_m7A0 = v_xmm0;
    v_stack_m9E0 = 0;
    v_stack_mA04 = 0;
    v_stack_m9C8 = 0;
    Arg2 = 0;
    result = memset(v_stack_m698, Arg2, 152, Arg4);
    v_stack_m8C8 = v_xmm0;
    v_stack_mA50 = 0;
    v_stack_mA30 = 0;
    result = 0;
    v_stack_m5F4 = 0;
    Arg2 = 0;
    result = memset(v_stack_m5F8, Arg2, local_rsi + 68, Arg4);
    v_stack_mA40 = 0;
    v_stack_m9E8 = 0;
    Arg2 = 0;
    result = memset(v_stack_m958, Arg2, local_rsi + 104, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m788, Arg2, local_rsi + 80, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m738, Arg2, local_rsi + 88, Arg4);
    result = 0;
    v_stack_m7F0 = v_xmm0;
    v_stack_m7E0 = v_xmm0;
    v_stack_m7D0 = 0;
    v_stack_m8E8 = v_xmm0;
    Arg2 = 0;
    result = memset(v_stack_m8B8, Arg2, local_rsi + 72, Arg4);
    v_stack_m858 = v_xmm0;
    v_stack_m848 = v_xmm0;
    v_stack_m838 = v_xmm0;
    result = 0;
    v_stack_m828 = v_xmm1;
    v_stack_m818 = v_xmm1;
    v_stack_m808 = v_xmm1;
    v_stack_m7F8 = 0;
    v_stack_m9FC = 0;
    v_stack_m9C0 = v_xmm0;
    v_stack_m988 = v_xmm0;
    v_stack_m978 = v_xmm0;
    v_stack_m968 = 0;
    v_stack_m9D0 = 0;
    Arg2 = 0;
    result = memset(v_stack_m5A8, Arg2, local_rsi + 64, Arg4);
    v_stack_m8D8 = v_xmm0;
    result = 0;
    v_stack_m9B0 = v_xmm1;
    v_stack_m9A0 = v_xmm1;
    v_stack_m990 = 0;
    v_stack_m6D8 = v_xmm0;
    v_stack_m6C8 = v_xmm0;
    v_stack_m6B8 = v_xmm0;
    v_stack_m6A8 = 0;
    v_stack_mA28 = 0;
    v_stack_mA5B = 0;
    v_stack_mA59 = 0;
    if (((uint32_t)((int32_t)(Arg2) - 1)) > 50) goto loc_009FC637;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((int32_t)(Arg2)))) - (9));
    if (condition_is_equal) goto loc_009FC2CC;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_009FC4B6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009FC4A5;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_009FC487;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009FBFCA;
    Arg1 = (uint32_t)((Arg1) - (8));
    if (condition_is_equal) goto loc_009FC476;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_rsi + 2)));
    if (condition_is_equal) goto loc_009FC465;
    if (((uint32_t)(Arg1)) == 13) goto loc_009FC445;
    v_stack_mA60 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x9FBB62 + (int32_t)(arg2) * 4 + 0xB4E52C)));
loc_009FBB78:
loc_009FBB7E:
    v_stack_mA2C = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x9FBB62 + (int32_t)(arg2) * 4 + 0xB4E52C)));
    v_stack_mA58 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_mA5C = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_009FBC00;
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_009FBBCA;
loc_009FBBB8:
    if (Arg5 == 0) goto loc_009FBBF8;
    Arg2 = local_rsi + 2;
    if (Arg5 < (local_rsi + 2)) { Arg2 = Arg5; }
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    goto loc_009FBBF8;
loc_009FBBCA:
    result = (uint32_t)(*(uint32_t *)(arg2));
    if (((Arg3) & ((uint32_t)(*(uint32_t *)(arg2)) - 1)) != 0) {
        result = ExRaiseDatatypeMisalignment((uint32_t)(*(uint32_t *)(arg2)) - 1, Arg2, v_rip - 10468194, Arg4);
    }
    if ((Arg3 + (uint32_t)(Arg4) * 1) > Arg2) goto loc_009FBBEF;
    if ((Arg3 + (uint32_t)(Arg4) * 1) < Arg3) {
        result = *(uint8_t *)(arg2);
    }
    goto loc_009FBBB8;
loc_009FBBF8:
    goto loc_009FBC00;
loc_009FBC00:
    if (v_stack_mA18 == 0) goto loc_009FBF95;
    v_stack_mA80 = 0;
    v_stack_mA88 = 0;
    v_stack_mA90 = v_stack_mA40;
    v_stack_mA98 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_mA18, 4, *(uint64_t *)(v_rip + 0x5CB040), (uint8_t)(v_stack_mA5C));
    if (!sign_flag) goto loc_009FBC6C;
loc_009FBC48:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 4, *(uint64_t *)(v_rip + 0x5CB040), (uint8_t)(v_stack_mA5C));
    local_rsp = (local_rsp) + (0xA80ULL);
    return result;
loc_009FBC6C:
loc_009FBC71:
loc_009FBC76:
    v_stack_p70 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x9FBB62 + (int32_t)(arg2) * 4 + 0xB4E52C)));
    v_stack_p40 = 0;
    if (((uint32_t)((int32_t)(Arg2))) > 26) goto loc_009FBFEB;
    if (((uint32_t)((int32_t)(Arg2))) == 26) goto loc_009FC4D9;
    if (((uint32_t)((int32_t)(Arg2))) <= 12) goto loc_009FC0D7;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((int32_t)(Arg2)))) - (13));
    if (condition_is_not_equal) goto loc_009FC1F4;
    result = 0;
    v_stack_p58 = 0;
    v_stack_p5A = 0;
    result = PspQueryJobHierarchyAccountingInformation(v_stack_p78, v_stack_p550, *(uint64_t *)(v_rip + 0x5CB040), (uint8_t)(v_stack_mA5C));
    v_stack_p168 = v_stack_p598;
    v_stack_p178 = v_stack_p5A0;
    v_stack_p188 = v_stack_p550;
    result = PspLockJobExclusive(v_stack_p78, v_stack_p60, *(uint64_t *)(v_rip + 0x5CB040), (uint8_t)(v_stack_mA5C));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x610))) & ((uint32_t)((uint32_t)(0x4008ULL))));
    local_rdi = v_stack_p78;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x4008ULL)))) {
        local_rdi = v_stack_p78;
    }
    Arg2 = 0;
    result = PspLockJobMemoryLimitsShared(local_rdi, Arg2, *(uint64_t *)(v_rip + 0x5CB040), (uint8_t)(v_stack_mA5C));
    result = (*(uint64_t *)(local_rdi + 0x4B8)) << (12);
    v_stack_p198 = result;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = local_rdi + 1264;
        result = ExfReleasePushLockShared(Arg1, Arg2, *(uint64_t *)(v_rip + 0x5CB040), (uint8_t)(v_stack_mA5C));
    }
    result = KeAbPostRelease(local_rdi + 1264, Arg2, *(uint64_t *)(v_rip + 0x5CB040), (uint8_t)(v_stack_mA5C));
    if (*(uint64_t *)(v_stack_p78 + 0x4C0) != 0) goto loc_009FC5A3;
    v_stack_p160 = 0;
    v_stack_p170 = 0;
    v_stack_p180 = 0;
    v_stack_p190 = 0;
    v_stack_p1B0 = 0;
    v_stack_p1A0 = 0;
loc_009FBDAD:
    if (0 == 0) goto loc_009FC40B;
    if (0 == 1) goto loc_009FC418;
loc_009FBDC6:
    *(uint32_t *)(v_stack_p1AC) = 0;
    Arg1 = (uint32_t)((0) + (1));
    if (((uint32_t)(Arg1)) < 3) goto loc_009FBDAD;
    v_stack_p80 = 60;
loc_009FBDE6:
    if (*(uint64_t *)(v_stack_p78 + 0x4C0) != 0) goto loc_009FC5DA;
loc_009FBDF6:
loc_009FBDF9:
    v_stack_p88 = 1;
    v_stack_p20 = 0;
    result = PspQueryRateControlHistory(v_stack_p78, 1, *(uint8_t *)(v_stack_p58), v_stack_pBC);
    if (0 != 0) goto loc_009FC425;
loc_009FBE29:
    *(uint32_t *)(v_stack_p1C0) = (uint32_t)((uint32_t)(v_stack_pBC));
    local_r15 = (uint32_t)((0) + (1));
    Arg3 = (v_stack_p80) + (4);
    v_stack_p80 = Arg3;
    local_rbx = (v_stack_p58) + (1);
    if (((uint32_t)(local_r15)) < 3) goto loc_009FBDE6;
    if (*(uint64_t *)(v_stack_p78 + 0x4C0) != 0) goto loc_009FC5F3;
loc_009FBE67:
    result = PspUnlockJob(v_stack_p78, v_stack_p60, Arg3, v_stack_pBC);
    v_stack_p388 = v_stack_p168;
    v_stack_p390 = v_stack_p170;
    v_stack_p398 = v_stack_p178;
    v_stack_p3A0 = v_stack_p180;
    v_stack_p3A8 = v_stack_p188;
    v_stack_p3B0 = v_stack_p190;
    v_stack_p3B8 = v_stack_p198;
    v_stack_p3C0 = v_stack_p1B0;
    v_stack_p3C8 = v_stack_p1A0;
    v_stack_p3D0 = (uint32_t)((uint32_t)(v_stack_p1A8));
    v_stack_p3D4 = (uint32_t)((uint32_t)(v_stack_p1AC));
    result = (uint32_t)(((uint32_t)(v_stack_p160)) & ((uint32_t)((uint32_t)(0x278204ULL))));
    v_stack_p380 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(v_stack_p164)) & ((uint32_t)((uint32_t)(0x278204ULL))));
    v_stack_p384 = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0x5CAB9C)) & (0x80000ULL)) == 0) goto loc_009FC081;
    v_stack_p28 = 0x726ULL;
    v_stack_p20 = 0;
    result = EtwTraceJobSetQuery(v_stack_p78, (uint32_t)((uint32_t)((int32_t)(Arg2))), v_stack_p160, v_stack_p88);
    goto loc_009FC081;
loc_009FBF95:
    v_stack_p78 = *(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0xB8) + 0x2A0);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0xB8) + 0x2A0) != 0) goto loc_009FC4C7;
    if ((((uint32_t)((int32_t)(Arg2) - 31)) & (0xFFFFFFF7ULL)) == 0) goto loc_009FBC76;
    goto loc_009FBC48;
loc_009FBFCA:
    if (0 == 40) goto loc_009FBFD8;
loc_009FBFD2:
    if (0 != 64) goto loc_009FC2E2;
loc_009FBFD8:
    v_stack_p58 = 0;
    goto loc_009FBB78;
loc_009FBFEB:
    if (((uint32_t)((int32_t)(Arg2))) > 39) goto loc_009FC25B;
    if (((uint32_t)((int32_t)(Arg2))) == 39) goto loc_009FC611;
    if (((uint32_t)((int32_t)(Arg2))) == 33) goto loc_009FC2EC;
    local_r14 = (uint32_t)(((int32_t)(Arg2)) - (28));
    v_stack_p2E0 = v_xmm0;
    result = PspLockJobMemoryLimitsShared(*(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0xB8) + 0x2A0), v_stack_p78, v_rip - 10469343, v_stack_p88);
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0xB8) + 0x2A0) + 0x2D0)) << (12);
    v_stack_p2D0 = result;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0xB8) + 0x2A0) + 0x4B8)) << (12);
    v_stack_p2C8 = result;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0xB8) + 0x2A0) + 0x620)) << (12);
    v_stack_p2D8 = result;
    result = PspUnlockJobMemoryLimitsShared(v_stack_p78, v_stack_p60, v_rip - 10469343, v_stack_p88);
loc_009FC07F:
loc_009FC081:
loc_009FC08B:
    if (v_stack_p78 != 0) goto loc_009FC0C8;
loc_009FC090:
    if (!sign_flag) goto loc_009FC0A3;
loc_009FC094:
    if (v_stack_p50 == 0) goto loc_009FC0BA;
    *(uint32_t *)(v_stack_p50) = (uint32_t)((uint32_t)(v_stack_p70));
    goto loc_009FC0BA;
loc_009FC0A3:
    if (v_stack_p40 != 0) goto loc_009FC094;
    result = memcpy(v_stack_p48, v_stack_p2C8, 0, v_stack_p88);
    goto loc_009FC094;
loc_009FC0BA:
    goto loc_009FC0C1;
loc_009FC0C1:
    goto loc_009FBC48;
loc_009FC0C8:
    result = ObfDereferenceObjectWithTag(v_stack_p78, (uint32_t)(0x79517350ULL), 0, v_stack_p88);
    goto loc_009FC090;
loc_009FC0D7:
    if (v_stack_p40 == 0) goto loc_009FC2EC;
    if (((uint32_t)(v_stack_p48)) == 6) goto loc_009FC513;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p48))) - (1));
    if (condition_is_equal) goto loc_009FC550;
    Arg2 = (uint32_t)((Arg2) - (1));
    result = PspLockJobShared(v_stack_p78, v_stack_p78, 0, v_stack_p88);
    v_stack_p438 = *(uint64_t *)(v_stack_p78 + 0xF0);
    v_stack_p440 = *(uint64_t *)(v_stack_p78 + 0xF8);
    v_stack_p448 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x104)));
    v_stack_p458 = (uint32_t)(*(uint8_t *)(v_stack_p78 + 0x44D));
    v_stack_p45C = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x244)));
    v_stack_p68 = 32;
loc_009FC16C:
    if (0 < ((uint16_t)(*(uint16_t *)(v_stack_p78 + 0x108)))) goto loc_009FC2B1;
    if (32 == 32) goto loc_009FC3FE;
    v_stack_p450 = *(uint64_t *)(v_stack_p78 + 0x20 * 8 + 0x110);
loc_009FC192:
    v_stack_p420 = *(uint64_t *)(v_stack_p78 + 0xE0);
    v_stack_p428 = *(uint64_t *)(v_stack_p78 + 0xE8);
    result = PspGetJobLimitInformationValidFlags((uint32_t)((uint32_t)(v_stack_p48)), (uint32_t)(v_stack_p6C), 0, *(uint16_t *)(v_stack_p78 + 0x108));
    result = (uint32_t)((result) | (0x7FFFULL));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x100))) & ((uint32_t)(result)));
    v_stack_p430 = (uint32_t)(Arg1);
    result = PspUnlockJob(v_stack_p78, v_stack_p60, 0, *(uint16_t *)(v_stack_p78 + 0x108));
    goto loc_009FC07F;
loc_009FC1F4:
    Arg2 = (uint32_t)((v_stack_p60) - (1));
    Arg2 = (uint32_t)((Arg2) - (1));
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009FC589;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009FC56D;
    Arg2 = (uint32_t)((Arg2) - (1));
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009FC550;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_not_equal) goto loc_009FC52D;
    result = PspAllocateAndQueryNotificationChannel(v_stack_p78, v_stack_p78, v_stack_p510, *(uint16_t *)(v_stack_p78 + 0x108));
    local_r15 = v_stack_p510;
    if (sign_flag) { local_r15 = 0; }
    local_rbx = 0;
    if (sign_flag) { local_rbx = (uint32_t)(result); }
    goto loc_009FC081;
loc_009FC25B:
    local_r14 = (uint32_t)((v_stack_p48) - (42));
    Arg2 = 0;
    result = memset(v_stack_p4C0, Arg2, local_r14 + 72, *(uint16_t *)(v_stack_p78 + 0x108));
    result = PspLockJobShared(v_stack_p78, v_stack_p60, local_r14 + 72, *(uint16_t *)(v_stack_p78 + 0x108));
    result = PspQueryJobIoAttribution(v_stack_p78, v_stack_p4C0, local_r14 + 72, *(uint16_t *)(v_stack_p78 + 0x108));
    result = PspUnlockJob(v_stack_p78, v_stack_p60, local_r14 + 72, *(uint16_t *)(v_stack_p78 + 0x108));
    goto loc_009FC081;
loc_009FC2B1:
    if ((*(uint64_t *)(v_stack_p78 + (uint16_t)(local_r14 + 0x48) * 8 + 0x110)) != 0) goto loc_009FC3EB;
loc_009FC2C3:
    Arg3 = (uint16_t)((local_r14 + 72) + ((uint16_t)(v_stack_p50)));
    goto loc_009FC16C;
loc_009FC2CC:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - (144));
    if (condition_is_equal) goto loc_009FBFD8;
    if (((uint32_t)(result)) == 8) goto loc_009FBFD8;
loc_009FC2E2:
    goto loc_009FBC48;
loc_009FC2EC:
    result = PspLockJobShared(v_stack_p78, v_stack_p78, Arg3, *(uint16_t *)(v_stack_p78 + 0x108));
    if (*(uint64_t *)(v_stack_p78 + 0x4C0) == 0) goto loc_009FC39D;
    v_stack_p228 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p78 + 0x4C0))));
    v_stack_p200 = *(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0x4C0) + 0x8);
    v_stack_p208 = *(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0x4C0) + 0x10);
    v_stack_p210 = *(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0x4C0) + 0x18);
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0x4C0) + 0x20)) << (12);
    v_stack_p230 = result;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_p78 + 0x4C0) + 0x28)) << (12);
    v_stack_p218 = result;
    Arg1 = (*(uint64_t *)(v_stack_p78 + 0x4C0)) + (60);
loc_009FC35A:
    if (0 == 0) goto loc_009FC3D7;
    if (0 != 1) goto loc_009FC3CD;
loc_009FC36B:
    *(uint32_t *)(v_stack_p22C) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 - 0xC)));
    if (0 == 0) goto loc_009FC384;
    if (0 != 1) goto loc_009FC3E1;
    goto loc_009FC38C;
loc_009FC384:
loc_009FC38C:
    *(uint32_t *)(v_stack_p240) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    Arg2 = (uint32_t)((0) + ((uint32_t)(v_stack_p50)));
    Arg1 = (Arg1) + (4);
    if (Arg2 < 3) goto loc_009FC35A;
loc_009FC39D:
    result = PspUnlockJob(v_stack_p78, v_stack_p60, v_stack_p240, *(uint16_t *)(v_stack_p78 + 0x108));
    goto loc_009FC07F;
loc_009FC3CD:
    goto loc_009FC36B;
loc_009FC3D7:
    goto loc_009FC36B;
loc_009FC3E1:
    goto loc_009FC38C;
loc_009FC3EB:
    if (((uint16_t)(v_stack_p60)) != ((uint16_t)(v_stack_p78))) goto loc_009FC3FE;
    v_stack_p68 = (uint16_t)((uint16_t)(v_stack_p224));
    goto loc_009FC2C3;
loc_009FC3FE:
    v_stack_p450 = 0;
    goto loc_009FC192;
loc_009FC40B:
    goto loc_009FBDC6;
loc_009FC418:
    goto loc_009FBDC6;
loc_009FC425:
    if (((uint32_t)(v_stack_p200)) == 1) goto loc_009FC438;
    goto loc_009FBE29;
loc_009FC438:
    goto loc_009FBE29;
loc_009FC445:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 1) goto loc_009FC2E2;
    v_stack_p58 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_009FBB7E;
loc_009FC465:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 16) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC476:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 16) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC487:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - (432));
    if (condition_is_equal) goto loc_009FBFD8;
    result = (uint32_t)((result) - (16));
    if (condition_is_equal) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC4A5:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 80) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC4B6:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 48) goto loc_009FBFD8;
    goto loc_009FBFD2;
loc_009FC4C7:
    result = ObfReferenceObjectWithTag(v_stack_p78, (uint32_t)(0x79517350ULL), v_rip - 10470496, *(uint16_t *)(v_stack_p78 + 0x108));
    goto loc_009FBC71;
loc_009FC4D9:
    result = PspQueryJobHierarchyInterferenceCount(v_stack_p78, v_stack_p48, v_rip - 10470496, *(uint16_t *)(v_stack_p78 + 0x108));
    result = v_stack_p40;
    if (!sign_flag) { result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))); }
    v_stack_p40 = (uint8_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) >> (31));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    result = (uint32_t)((result) + (8));
    v_stack_p70 = (uint32_t)(result);
    goto loc_009FC08B;
loc_009FC513:
    v_stack_pB4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x224)));
    goto loc_009FC07F;
loc_009FC52D:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x610))) >> (10));
    result = (uint8_t)((result) & ((uint8_t)(v_stack_p50)));
    v_stack_p5E = (uint8_t)(result);
    goto loc_009FC07F;
loc_009FC550:
    result = PspQueryJobHierarchyAccountingInformation(v_stack_p78, v_stack_p550, v_rip - 10470496, *(uint16_t *)(v_stack_p78 + 0x108));
    goto loc_009FC07F;
loc_009FC56D:
    v_stack_pE0 = *(uint64_t *)(v_stack_p78 + 0x238);
    goto loc_009FC07F;
loc_009FC589:
    v_stack_pB8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x450)));
    goto loc_009FC07F;
loc_009FC5A3:
    v_stack_p160 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x450)))));
    v_stack_p164 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p78 + 0x4C0) + 0x4)));
loc_009FC5DA:
    result = PspRateControlLimitFlag((uint32_t)((uint32_t)(v_stack_pB8)), v_stack_p550, v_rip - 10470496, *(uint16_t *)(v_stack_p78 + 0x108));
    if (((*(uint32_t *)(v_stack_p550)) & ((uint32_t)(result))) == 0) goto loc_009FBDF6;
    goto loc_009FBDF9;
loc_009FC5F3:
    *(uint32_t *)(result + 0x4) = 0;
    Arg1 = (*(uint64_t *)(v_stack_p78 + 0x4C0)) + (72);
    Arg2 = 0;
    result = memset(Arg1, Arg2, Arg2 + 64, *(uint16_t *)(v_stack_p78 + 0x108));
    goto loc_009FBE67;
loc_009FC611:
    result = PsGetJobServerSilo(v_stack_p78, v_stack_p90, Arg2 + 64, *(uint16_t *)(v_stack_p78 + 0x108));
loc_009FC637:
    goto loc_009FBC48;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x1F` | `32` | `R` |
| `Arg2` | `- 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009FB860&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
