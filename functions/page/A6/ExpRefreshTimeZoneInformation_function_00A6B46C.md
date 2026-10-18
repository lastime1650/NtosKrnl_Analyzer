# ExpRefreshTimeZoneInformation

- RVA: `0x00A6B46C`–`0x00A6BB46` (길이 `1,754` bytes)
- VA: `0x0000000140A6B46C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B4340`
- 디코드: `435`개 명령, `1,754/1,754` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00A6B4B4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A6B4E1` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (function, `0x00225710`)
- `0x00A6B4E9` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x00A6B501` → [ExpInitializeTimeZoneInformation](ExpInitializeTimeZoneInformation_function_00A6BF78.md) (function, `0x00A6BF78`)
- `0x00A6B50F` → [ExpReadSiloTimeZoneMarker](../7C/ExpReadSiloTimeZoneMarker_function_007C61A8.md) (function, `0x007C61A8`)
- `0x00A6B51A` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x00A6B529` → [RtlpQueryTimeZoneInformationWorker](RtlpQueryTimeZoneInformationWorker_function_00A6BB6C.md) (function, `0x00A6BB6C`)
- `0x00A6B53C` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (function, `0x00449AC0`)
- `0x00A6B546` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00A6B54F` → [ExpReadSiloTimeZoneMarker](../7C/ExpReadSiloTimeZoneMarker_function_007C61A8.md) (function, `0x007C61A8`)
- `0x00A6B5D3` → [RtlpQueryTimeZoneInformationWorker](RtlpQueryTimeZoneInformationWorker_function_00A6BB6C.md) (function, `0x00A6BB6C`)
- `0x00A6B5F1` → [ExpLogRefreshTimeZoneInformationQueryFail](ExpLogRefreshTimeZoneInformationQueryFail_function_00A6BE6C.md) (function, `0x00A6BE6C`)
- `0x00A6B610` → [EtwTraceTimeZoneInformationRefresh](EtwTraceTimeZoneInformationRefresh_function_00A6C078.md) (function, `0x00A6C078`)
- `0x00A6B652` → [RtlTimeToTimeFields](../../text/42/RtlTimeToTimeFields_function_0042E0F0.md) (function, `0x0042E0F0`)
- `0x00A6B65F` → [RtlpCheckDynamicTimeZoneInformation](../78/RtlpCheckDynamicTimeZoneInformation_function_0078FB3C.md) (function, `0x0078FB3C`)
- `0x00A6B6AF` → [RtlGetPersistedStateLocation](../8C/RtlGetPersistedStateLocation_function_008C8DE0.md) (function, `0x008C8DE0`)
- `0x00A6B6CC` → [RtlpGetRegistryHandle](../8C/RtlpGetRegistryHandle_function_008C955C.md) (function, `0x008C955C`)
- `0x00A6B6EA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A6B6FE` → [RtlpSetTimeZoneInformationWorker](../78/RtlpSetTimeZoneInformationWorker_function_0078FEC8.md) (function, `0x0078FEC8`)
- `0x00A6B73A` → [RtlCutoverTimeToSystemTime](../78/RtlCutoverTimeToSystemTime_function_0078B110.md) (function, `0x0078B110`)
- `0x00A6B766` → [ExpLogRefreshTimeZoneInformationCutoverFail](../7C/ExpLogRefreshTimeZoneInformationCutoverFail_function_007C5BE0.md) (function, `0x007C5BE0`)
- `0x00A6B78E` → [RtlCutoverTimeToSystemTime](../78/RtlCutoverTimeToSystemTime_function_0078B110.md) (function, `0x0078B110`)
- `0x00A6B7B9` → [ExpLogRefreshTimeZoneInformationCutoverFail](../7C/ExpLogRefreshTimeZoneInformationCutoverFail_function_007C5BE0.md) (function, `0x007C5BE0`)
- `0x00A6B853` → [KeCancelTimer](../../text/23/KeCancelTimer_function_002327E0.md) (function, `0x002327E0`)
- `0x00A6B89D` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00A6B8AB` → [EtwTraceTimeZoneBiasChange](../7B/EtwTraceTimeZoneBiasChange_function_007B8300.md) (function, `0x007B8300`)
- `0x00A6B94C` → [RtlSetSystemGlobalData](../../text/43/RtlSetSystemGlobalData_function_00435AF0.md) (function, `0x00435AF0`)
- `0x00A6B95A` → [RtlTimeToTimeFields](../../text/42/RtlTimeToTimeFields_function_0042E0F0.md) (function, `0x0042E0F0`)
- `0x00A6B976` → [ExLocalTimeToSystemTime](../../text/49/ExLocalTimeToSystemTime_function_00494BC0.md) (function, `0x00494BC0`)
- `0x00A6B993` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (function, `0x00232CB0`)
- `0x00A6B9CA` → [RtlTimeFieldsToTime](../../text/42/RtlTimeFieldsToTime_function_0042E6B0.md) (function, `0x0042E6B0`)
- `0x00A6B9DE` → [ExLocalTimeToSystemTime](../../text/49/ExLocalTimeToSystemTime_function_00494BC0.md) (function, `0x00494BC0`)
- `0x00A6B9FF` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (function, `0x00232CB0`)
- `0x00A6BA17` → [RtlTimeFieldsToTime](../../text/42/RtlTimeFieldsToTime_function_0042E6B0.md) (function, `0x0042E6B0`)
- `0x00A6BA2B` → [ExLocalTimeToSystemTime](../../text/49/ExLocalTimeToSystemTime_function_00494BC0.md) (function, `0x00494BC0`)
- `0x00A6BA4C` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (function, `0x00232CB0`)
- `0x00A6BA67` → [ExpWriteTimeZoneBias](ExpWriteTimeZoneBias_function_00A6C028.md) (function, `0x00A6C028`)
- `0x00A6BA89` → [ExpWriteTimeZoneBiasStartEnd](ExpWriteTimeZoneBiasStartEnd_function_00A6C410.md) (function, `0x00A6C410`)
- `0x00A6BAAD` → [RtlSetActiveTimeBias](../78/RtlSetActiveTimeBias_function_0078FA2C.md) (function, `0x0078FA2C`)
- `0x00A6BAC3` → [RtlpUpdateDynamicTimeZones](../79/RtlpUpdateDynamicTimeZones_function_0079019C.md) (function, `0x0079019C`)
- `0x00A6BAEE` → [ExpLogRefreshTimeZoneInformationSuccess](ExpLogRefreshTimeZoneInformationSuccess_function_00A6C204.md) (function, `0x00A6C204`)
- `0x00A6BB0D` → [EtwTraceTimeZoneInformationRefresh](EtwTraceTimeZoneInformationRefresh_function_00A6C078.md) (function, `0x00A6C078`)
- `0x00A6BB1F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ExpReadLeapSecondData](../7C/ExpReadLeapSecondData_function_007C5EAC.md) at `0x007C60CC`
- [ExpRefreshSystemTime](../7C/ExpRefreshSystemTime_function_007C6264.md) at `0x007C62CF`
- [ExpTimeZoneInitSiloState](../7C/ExpTimeZoneInitSiloState_function_007C6430.md) at `0x007C64B8`
- [NtSetSystemTime](../7C/NtSetSystemTime_function_007C65F0.md) at `0x007C67D1`
- [NtSetSystemTime](../7C/NtSetSystemTime_function_007C65F0.md) at `0x007C6893`
- [ExpSetSystemTime](../../pagelk/B7/ExpSetSystemTime_function_00B7C838.md) at `0x00B7C8AB`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D6C4`

### Static image references
- `0x00A6B492` → RVA `0x00E0A740` (`.data`; read)
- `0x00A6B5EA` → RVA `0x00E0EB98` (`.data`; write)
- `0x00A6B68A` → RVA `0x00B056B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A6B6A8` → RVA `0x00B05970` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A6B879` → RVA `0x00020A78` (`.rdata`; read)
- `0x00A6BA51` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00A6BA9D` → RVA `0x00E68570` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x00A6B4B4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A6B4E1` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (`PAGE` → `.text`)
  - `0x00A6B4E9` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x00A6B51A` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x00A6B53C` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (`PAGE` → `.text`)
  - `0x00A6B546` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00A6B652` → [RtlTimeToTimeFields](../../text/42/RtlTimeToTimeFields_function_0042E0F0.md) (`PAGE` → `.text`)
  - `0x00A6B6EA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A6B853` → [KeCancelTimer](../../text/23/KeCancelTimer_function_002327E0.md) (`PAGE` → `.text`)
  - `0x00A6B89D` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00A6B94C` → [RtlSetSystemGlobalData](../../text/43/RtlSetSystemGlobalData_function_00435AF0.md) (`PAGE` → `.text`)
  - `0x00A6B95A` → [RtlTimeToTimeFields](../../text/42/RtlTimeToTimeFields_function_0042E0F0.md) (`PAGE` → `.text`)
  - `0x00A6B976` → [ExLocalTimeToSystemTime](../../text/49/ExLocalTimeToSystemTime_function_00494BC0.md) (`PAGE` → `.text`)
  - `0x00A6B993` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (`PAGE` → `.text`)
  - `0x00A6B9CA` → [RtlTimeFieldsToTime](../../text/42/RtlTimeFieldsToTime_function_0042E6B0.md) (`PAGE` → `.text`)
  - `0x00A6B9DE` → [ExLocalTimeToSystemTime](../../text/49/ExLocalTimeToSystemTime_function_00494BC0.md) (`PAGE` → `.text`)
  - `0x00A6B9FF` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (`PAGE` → `.text`)
  - `0x00A6BA17` → [RtlTimeFieldsToTime](../../text/42/RtlTimeFieldsToTime_function_0042E6B0.md) (`PAGE` → `.text`)
  - `0x00A6BA2B` → [ExLocalTimeToSystemTime](../../text/49/ExLocalTimeToSystemTime_function_00494BC0.md) (`PAGE` → `.text`)
  - `0x00A6BA4C` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (`PAGE` → `.text`)
  - `0x00A6BB1F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6B46C  48 8B C4                        mov rax, rsp
00A6B46F  48 89 58 08                     mov qword ptr [rax + 8], rbx
00A6B473  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00A6B477  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00A6B47B  55                              push rbp
00A6B47C  41 54                           push r12
00A6B47E  41 55                           push r13
00A6B480  41 56                           push r14
00A6B482  41 57                           push r15
00A6B484  48 8D A8 48 FC FF FF            lea rbp, [rax - 0x3b8]
00A6B48B  48 81 EC 90 04 00 00            sub rsp, 0x490
00A6B492  48 8B 05 A7 F2 39 00            mov rax, qword ptr [rip + 0x39f2a7]
00A6B499  48 33 C4                        xor rax, rsp
00A6B49C  48 89 85 80 03 00 00            mov qword ptr [rbp + 0x380], rax
00A6B4A3  8A D9                           mov bl, cl
00A6B4A5  41 BF B0 01 00 00               mov r15d, 0x1b0
00A6B4AB  45 8B C7                        mov r8d, r15d
00A6B4AE  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6B4B2  33 D2                           xor edx, edx
00A6B4B4  E8 87 B7 C5 FF                  call 0x1406c6c40
00A6B4B9  33 F6                           xor esi, esi
00A6B4BB  0F 57 C0                        xorps xmm0, xmm0
00A6B4BE  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
00A6B4C2  48 89 75 88                     mov qword ptr [rbp - 0x78], rsi
00A6B4C6  44 8A EE                        mov r13b, sil
00A6B4C9  48 89 75 90                     mov qword ptr [rbp - 0x70], rsi
00A6B4CD  41 B4 01                        mov r12b, 1
00A6B4D0  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
00A6B4D5  8B FE                           mov edi, esi
00A6B4D7  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00A6B4DC  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
00A6B4E1  E8 2A A2 7B FF                  call 0x140225710
00A6B4E6  48 8B C8                        mov rcx, rax
00A6B4E9  E8 B2 9B 7B FF                  call 0x1402250a0
00A6B4EE  4C 8B B0 C8 04 00 00            mov r14, qword ptr [rax + 0x4c8]
00A6B4F5  49 39 B6 50 02 00 00            cmp qword ptr [r14 + 0x250], rsi
00A6B4FC  75 0A                           jne 0x140a6b508
00A6B4FE  49 8B D6                        mov rdx, r14
00A6B501  E8 72 0A 00 00                  call 0x140a6bf78
00A6B506  EB 03                           jmp 0x140a6b50b
00A6B508  44 8A E6                        mov r12b, sil
00A6B50B  84 DB                           test bl, bl
00A6B50D  74 37                           je 0x140a6b546
00A6B50F  E8 94 AC D5 FF                  call 0x1407c61a8
00A6B514  84 C0                           test al, al
00A6B516  75 0A                           jne 0x140a6b522
00A6B518  33 C9                           xor ecx, ecx
00A6B51A  E8 A1 73 9D FF                  call 0x1404428c0
00A6B51F  48 8B F8                        mov rdi, rax
00A6B522  41 8B D7                        mov edx, r15d
00A6B525  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6B529  E8 3E 06 00 00                  call 0x140a6bb6c
00A6B52E  8B D8                           mov ebx, eax
00A6B530  48 85 FF                        test rdi, rdi
00A6B533  0F 84 A1 00 00 00               je 0x140a6b5da
00A6B539  48 8B CF                        mov rcx, rdi
00A6B53C  E8 7F E5 9D FF                  call 0x140449ac0
00A6B541  E9 94 00 00 00                  jmp 0x140a6b5da
00A6B546  E8 95 AD 9C FF                  call 0x1404362e0
00A6B54B  84 C0                           test al, al
00A6B54D  74 7D                           je 0x140a6b5cc
00A6B54F  E8 54 AC D5 FF                  call 0x1407c61a8
00A6B554  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6B558  84 C0                           test al, al
00A6B55A  75 74                           jne 0x140a6b5d0
00A6B55C  BA 03 00 00 00                  mov edx, 3
00A6B561  49 8B C6                        mov rax, r14
00A6B564  44 8D 42 7D                     lea r8d, [rdx + 0x7d]
00A6B568  0F 10 00                        movups xmm0, xmmword ptr [rax]
00A6B56B  0F 11 01                        movups xmmword ptr [rcx], xmm0
00A6B56E  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00A6B572  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00A6B576  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00A6B57A  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00A6B57E  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
00A6B582  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00A6B586  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00A6B58A  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00A6B58E  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
00A6B592  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
00A6B596  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
00A6B59A  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00A6B59E  49 03 C8                        add rcx, r8
00A6B5A1  0F 10 48 70                     movups xmm1, xmmword ptr [rax + 0x70]
00A6B5A5  49 03 C0                        add rax, r8
00A6B5A8  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
00A6B5AC  48 83 EA 01                     sub rdx, 1
00A6B5B0  75 B6                           jne 0x140a6b568
00A6B5B2  0F 10 00                        movups xmm0, xmmword ptr [rax]
00A6B5B5  8B DE                           mov ebx, esi
00A6B5B7  0F 11 01                        movups xmmword ptr [rcx], xmm0
00A6B5BA  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00A6B5BE  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00A6B5C2  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00A6B5C6  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00A6B5CA  EB 0E                           jmp 0x140a6b5da
00A6B5CC  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6B5D0  41 8B D7                        mov edx, r15d
00A6B5D3  E8 94 05 00 00                  call 0x140a6bb6c
00A6B5D8  8B D8                           mov ebx, eax
00A6B5DA  85 DB                           test ebx, ebx
00A6B5DC  79 3E                           jns 0x140a6b61c
00A6B5DE  41 FF 86 E8 03 00 00            inc dword ptr [r14 + 0x3e8]
00A6B5E5  41 8A D4                        mov dl, r12b
00A6B5E8  8B CB                           mov ecx, ebx
00A6B5EA  C6 05 A7 35 3A 00 01            mov byte ptr [rip + 0x3a35a7], 1
00A6B5F1  E8 76 08 00 00                  call 0x140a6be6c
00A6B5F6  45 33 C9                        xor r9d, r9d
00A6B5F9  41 8D 49 01                     lea ecx, [r9 + 1]
00A6B5FD  45 8B 86 B0 01 00 00            mov r8d, dword ptr [r14 + 0x1b0]
00A6B604  41 8B 96 B4 01 00 00            mov edx, dword ptr [r14 + 0x1b4]
00A6B60B  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00A6B610  E8 63 0A 00 00                  call 0x140a6c078
00A6B615  32 C0                           xor al, al
00A6B617  E9 F9 04 00 00                  jmp 0x140a6bb15
00A6B61C  48 BE 14 00 00 00 80 F7 FF FF   movabs rsi, 0xfffff78000000014
00A6B626  33 FF                           xor edi, edi
00A6B628  48 8B 36                        mov rsi, qword ptr [rsi]
00A6B62B  48 8B DE                        mov rbx, rsi
00A6B62E  49 2B 9E B8 01 00 00            sub rbx, qword ptr [r14 + 0x1b8]
00A6B635  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00A6B63A  40 38 BD 6C 01 00 00            cmp byte ptr [rbp + 0x16c], dil
00A6B641  75 32                           jne 0x140a6b675
00A6B643  66 39 7D 6C                     cmp word ptr [rbp + 0x6c], di
00A6B647  74 2C                           je 0x140a6b675
00A6B649  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00A6B64D  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00A6B652  E8 99 2A 9C FF                  call 0x14042e0f0
00A6B657  0F B7 55 A0                     movzx edx, word ptr [rbp - 0x60]
00A6B65B  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6B65F  E8 D8 44 D2 FF                  call 0x14078fb3c
00A6B664  84 C0                           test al, al
00A6B666  74 0D                           je 0x140a6b675
00A6B668  41 B5 01                        mov r13b, 1
00A6B66B  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
00A6B670  E9 82 00 00 00                  jmp 0x140a6b6f7
00A6B675  45 84 E4                        test r12b, r12b
00A6B678  0F 84 85 00 00 00               je 0x140a6b703
00A6B67E  48 8D 45 B0                     lea rax, [rbp - 0x50]
00A6B682  45 33 C9                        xor r9d, r9d
00A6B685  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A6B68A  48 8D 15 1F A0 09 00            lea rdx, [rip + 0x9a01f]
00A6B691  48 8D 85 70 01 00 00            lea rax, [rbp + 0x170]
00A6B698  C7 44 24 28 08 02 00 00         mov dword ptr [rsp + 0x28], 0x208
00A6B6A0  45 33 C0                        xor r8d, r8d
00A6B6A3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A6B6A8  48 8D 0D C1 A2 09 00            lea rcx, [rip + 0x9a2c1]
00A6B6AF  E8 2C D7 E5 FF                  call 0x1408c8de0
00A6B6B4  85 C0                           test eax, eax
00A6B6B6  78 4B                           js 0x140a6b703
00A6B6B8  4C 8D 4D 80                     lea r9, [rbp - 0x80]
00A6B6BC  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
00A6B6C0  45 33 C0                        xor r8d, r8d
00A6B6C3  48 8D 95 70 01 00 00            lea rdx, [rbp + 0x170]
00A6B6CA  33 C9                           xor ecx, ecx
00A6B6CC  E8 8B DE E5 FF                  call 0x1408c955c
00A6B6D1  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00A6B6D5  3D 34 00 00 C0                  cmp eax, 0xc0000034
00A6B6DA  8B F8                           mov edi, eax
00A6B6DC  41 0F 94 C5                     sete r13b
00A6B6E0  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
00A6B6E5  48 85 C9                        test rcx, rcx
00A6B6E8  74 05                           je 0x140a6b6ef
00A6B6EA  E8 C1 1B C4 FF                  call 0x1406ad2b0
00A6B6EF  81 FF 34 00 00 C0               cmp edi, 0xc0000034
00A6B6F5  75 0C                           jne 0x140a6b703
00A6B6F7  41 8B D7                        mov edx, r15d
00A6B6FA  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6B6FE  E8 C5 47 D2 FF                  call 0x14078fec8
00A6B703  8B 7D C0                        mov edi, dword ptr [rbp - 0x40]
00A6B706  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A6B70A  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A6B70F  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00A6B713  33 C0                           xor eax, eax
00A6B715  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
00A6B719  66 39 45 06                     cmp word ptr [rbp + 6], ax
00A6B71D  0F 84 26 01 00 00               je 0x140a6b849
00A6B723  66 39 45 5A                     cmp word ptr [rbp + 0x5a], ax
00A6B727  0F 84 1C 01 00 00               je 0x140a6b849
00A6B72D  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00A6B732  48 8D 55 88                     lea rdx, [rbp - 0x78]
00A6B736  48 8D 4D 04                     lea rcx, [rbp + 4]
00A6B73A  E8 D1 F9 D1 FF                  call 0x14078b110
00A6B73F  84 C0                           test al, al
00A6B741  75 35                           jne 0x140a6b778
00A6B743  41 FF 86 E8 03 00 00            inc dword ptr [r14 + 0x3e8]
00A6B74A  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00A6B74F  41 BD 02 00 00 00               mov r13d, 2
00A6B755  C6 05 3C 34 3A 00 01            mov byte ptr [rip + 0x3a343c], 1
00A6B75C  45 8B CD                        mov r9d, r13d
00A6B75F  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6B763  41 8A D4                        mov dl, r12b
00A6B766  E8 75 A4 D5 FF                  call 0x1407c5be0
00A6B76B  44 8A 4C 24 40                  mov r9b, byte ptr [rsp + 0x40]
00A6B770  41 8B CD                        mov ecx, r13d
00A6B773  E9 85 FE FF FF                  jmp 0x140a6b5fd
00A6B778  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
00A6B77C  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00A6B781  48 8D 55 90                     lea rdx, [rbp - 0x70]
00A6B785  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
00A6B78A  48 8D 4D 58                     lea rcx, [rbp + 0x58]
00A6B78E  E8 7D F9 D1 FF                  call 0x14078b110
00A6B793  33 D2                           xor edx, edx
00A6B795  84 C0                           test al, al
00A6B797  75 2F                           jne 0x140a6b7c8
00A6B799  41 FF 86 E8 03 00 00            inc dword ptr [r14 + 0x3e8]
00A6B7A0  8D 7A 03                        lea edi, [rdx + 3]
00A6B7A3  44 8B CF                        mov r9d, edi
00A6B7A6  C6 05 EB 33 3A 00 01            mov byte ptr [rip + 0x3a33eb], 1
00A6B7AD  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00A6B7B2  41 8A D4                        mov dl, r12b
00A6B7B5  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6B7B9  E8 22 A4 D5 FF                  call 0x1407c5be0
00A6B7BE  45 8A CD                        mov r9b, r13b
00A6B7C1  8B CF                           mov ecx, edi
00A6B7C3  E9 35 FE FF FF                  jmp 0x140a6b5fd
00A6B7C8  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00A6B7CC  41 BD 02 00 00 00               mov r13d, 2
00A6B7D2  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00A6B7D6  48 3B D8                        cmp rbx, rax
00A6B7D9  7C 19                           jl 0x140a6b7f4
00A6B7DB  48 3B DF                        cmp rbx, rdi
00A6B7DE  7C 14                           jl 0x140a6b7f4
00A6B7E0  48 3B F8                        cmp rdi, rax
00A6B7E3  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00A6B7E8  8B CA                           mov ecx, edx
00A6B7EA  48 8B DA                        mov rbx, rdx
00A6B7ED  0F 9E C1                        setle cl
00A6B7F0  FF C1                           inc ecx
00A6B7F2  EB 33                           jmp 0x140a6b827
00A6B7F4  48 3B C7                        cmp rax, rdi
00A6B7F7  7D 19                           jge 0x140a6b812
00A6B7F9  48 3B D8                        cmp rbx, rax
00A6B7FC  7C 05                           jl 0x140a6b803
00A6B7FE  48 3B DF                        cmp rbx, rdi
00A6B801  7C 19                           jl 0x140a6b81c
00A6B803  48 8B D8                        mov rbx, rax
00A6B806  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A6B80B  B9 01 00 00 00                  mov ecx, 1
00A6B810  EB 15                           jmp 0x140a6b827
00A6B812  48 3B DF                        cmp rbx, rdi
00A6B815  7C 05                           jl 0x140a6b81c
00A6B817  48 3B D8                        cmp rbx, rax
00A6B81A  7C E7                           jl 0x140a6b803
00A6B81C  48 8B DF                        mov rbx, rdi
00A6B81F  41 8B CD                        mov ecx, r13d
00A6B822  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00A6B827  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
00A6B82B  49 8B C6                        mov rax, r14
00A6B82E  4C 03 F8                        add r15, rax
00A6B831  41 3B CD                        cmp ecx, r13d
00A6B834  4D 8D AE 00 02 00 00            lea r13, [r14 + 0x200]
00A6B83B  41 89 0F                        mov dword ptr [r15], ecx
00A6B83E  8B 45 14                        mov eax, dword ptr [rbp + 0x14]
00A6B841  0F 44 45 68                     cmove eax, dword ptr [rbp + 0x68]
00A6B845  03 F8                           add edi, eax
00A6B847  EB 22                           jmp 0x140a6b86b
00A6B849  4D 8D AE 00 02 00 00            lea r13, [r14 + 0x200]
00A6B850  49 8B CD                        mov rcx, r13
00A6B853  E8 88 6F 7C FF                  call 0x1402327e0
00A6B858  33 D2                           xor edx, edx
00A6B85A  4D 8D BE B0 01 00 00            lea r15, [r14 + 0x1b0]
00A6B861  41 89 17                        mov dword ptr [r15], edx
00A6B864  8B DA                           mov ebx, edx
00A6B866  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00A6B86B  41 39 BE B4 01 00 00            cmp dword ptr [r14 + 0x1b4], edi
00A6B872  74 3C                           je 0x140a6b8b0
00A6B874  83 4C 24 7C FF                  or dword ptr [rsp + 0x7c], 0xffffffff
00A6B879  48 8D 0D F8 51 5B FF            lea rcx, [rip - 0xa4ae08]
00A6B880  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00A6B884  45 33 C9                        xor r9d, r9d
00A6B887  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00A6B88B  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
00A6B88F  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A6B894  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00A6B899  45 8D 41 08                     lea r8d, [r9 + 8]
00A6B89D  E8 6E 54 C4 FF                  call 0x1406b0d10
00A6B8A2  41 8B 96 B4 01 00 00            mov edx, dword ptr [r14 + 0x1b4]
00A6B8A9  8B CF                           mov ecx, edi
00A6B8AB  E8 50 CA D4 FF                  call 0x1407b8300
00A6B8B0  6B C7 3C                        imul eax, edi, 0x3c
00A6B8B3  41 89 BE B4 01 00 00            mov dword ptr [r14 + 0x1b4], edi
00A6B8BA  BF 03 00 00 00                  mov edi, 3
00A6B8BF  48 63 C8                        movsxd rcx, eax
00A6B8C2  8D 57 7D                        lea edx, [rdi + 0x7d]
00A6B8C5  48 69 C1 80 96 98 00            imul rax, rcx, 0x989680
00A6B8CC  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6B8D0  49 89 86 B8 01 00 00            mov qword ptr [r14 + 0x1b8], rax
00A6B8D7  49 8B C6                        mov rax, r14
00A6B8DA  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00A6B8DD  0F 11 00                        movups xmmword ptr [rax], xmm0
00A6B8E0  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00A6B8E4  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A6B8E8  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00A6B8EC  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00A6B8F0  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
00A6B8F4  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
00A6B8F8  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
00A6B8FC  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
00A6B900  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
00A6B904  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
00A6B908  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
00A6B90C  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
00A6B910  48 03 C2                        add rax, rdx
00A6B913  0F 10 49 70                     movups xmm1, xmmword ptr [rcx + 0x70]
00A6B917  48 03 CA                        add rcx, rdx
00A6B91A  0F 11 48 F0                     movups xmmword ptr [rax - 0x10], xmm1
00A6B91E  48 83 EF 01                     sub rdi, 1
00A6B922  75 B6                           jne 0x140a6b8da
00A6B924  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00A6B927  33 D2                           xor edx, edx
00A6B929  44 8D 47 04                     lea r8d, [rdi + 4]
00A6B92D  88 15 65 32 3A 00               mov byte ptr [rip + 0x3a3265], dl
00A6B933  49 8B D7                        mov rdx, r15
00A6B936  0F 11 00                        movups xmmword ptr [rax], xmm0
00A6B939  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00A6B93D  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A6B941  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00A6B945  8D 4F 06                        lea ecx, [rdi + 6]
00A6B948  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00A6B94C  E8 9F A1 9C FF                  call 0x140435af0
00A6B951  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00A6B955  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00A6B95A  E8 91 27 9C FF                  call 0x14042e0f0
00A6B95F  45 33 FF                        xor r15d, r15d
00A6B962  48 85 DB                        test rbx, rbx
00A6B965  74 31                           je 0x140a6b998
00A6B967  49 8D 9E E0 03 00 00            lea rbx, [r14 + 0x3e0]
00A6B96E  48 8B D3                        mov rdx, rbx
00A6B971  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00A6B976  E8 45 92 A2 FF                  call 0x140494bc0
00A6B97B  48 8B 13                        mov rdx, qword ptr [rbx]
00A6B97E  49 8D 86 C0 01 00 00            lea rax, [r14 + 0x1c0]
00A6B985  45 33 C9                        xor r9d, r9d
00A6B988  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A6B98D  45 33 C0                        xor r8d, r8d
00A6B990  49 8B CD                        mov rcx, r13
00A6B993  E8 18 73 7C FF                  call 0x140232cb0
00A6B998  0F BF 7D A0                     movsx edi, word ptr [rbp - 0x60]
00A6B99C  49 8D 8E B0 03 00 00            lea rcx, [r14 + 0x3b0]
00A6B9A3  B8 1F 85 EB 51                  mov eax, 0x51eb851f
00A6B9A8  41 BD 01 00 00 00               mov r13d, 1
00A6B9AE  F7 EF                           imul edi
00A6B9B0  C1 FA 05                        sar edx, 5
00A6B9B3  8B C2                           mov eax, edx
00A6B9B5  C1 E8 1F                        shr eax, 0x1f
00A6B9B8  03 C2                           add eax, edx
00A6B9BA  66 41 03 C5                     add ax, r13w
00A6B9BE  98                              cwde
00A6B9BF  6B D0 64                        imul edx, eax, 0x64
00A6B9C2  66 89 11                        mov word ptr [rcx], dx
00A6B9C5  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00A6B9CA  E8 E1 2C 9C FF                  call 0x14042e6b0
00A6B9CF  49 8D 9E A8 03 00 00            lea rbx, [r14 + 0x3a8]
00A6B9D6  48 8B D3                        mov rdx, rbx
00A6B9D9  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00A6B9DE  E8 DD 91 A2 FF                  call 0x140494bc0
00A6B9E3  48 8B 13                        mov rdx, qword ptr [rbx]
00A6B9E6  49 8D 86 60 02 00 00            lea rax, [r14 + 0x260]
00A6B9ED  49 8D 8E A0 02 00 00            lea rcx, [r14 + 0x2a0]
00A6B9F4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A6B9F9  45 33 C9                        xor r9d, r9d
00A6B9FC  45 33 C0                        xor r8d, r8d
00A6B9FF  E8 AC 72 7C FF                  call 0x140232cb0
00A6BA04  49 8D 8E C8 03 00 00            lea rcx, [r14 + 0x3c8]
00A6BA0B  66 41 03 FD                     add di, r13w
00A6BA0F  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00A6BA14  66 89 39                        mov word ptr [rcx], di
00A6BA17  E8 94 2C 9C FF                  call 0x14042e6b0
00A6BA1C  49 8D 9E C0 03 00 00            lea rbx, [r14 + 0x3c0]
00A6BA23  48 8B D3                        mov rdx, rbx
00A6BA26  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00A6BA2B  E8 90 91 A2 FF                  call 0x140494bc0
00A6BA30  48 8B 13                        mov rdx, qword ptr [rbx]
00A6BA33  49 8D 86 00 03 00 00            lea rax, [r14 + 0x300]
00A6BA3A  49 8D 8E 40 03 00 00            lea rcx, [r14 + 0x340]
00A6BA41  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A6BA46  45 33 C9                        xor r9d, r9d
00A6BA49  45 33 C0                        xor r8d, r8d
00A6BA4C  E8 5F 72 7C FF                  call 0x140232cb0
00A6BA51  48 8B 05 B0 95 55 00            mov rax, qword ptr [rip + 0x5595b0]
00A6BA58  F0 44 01 A8 5C 02 00 00         lock add dword ptr [rax + 0x25c], r13d
00A6BA60  49 8D 8E B8 01 00 00            lea rcx, [r14 + 0x1b8]
00A6BA67  E8 BC 05 00 00                  call 0x140a6c028
00A6BA6C  4C 39 7C 24 48                  cmp qword ptr [rsp + 0x48], r15
00A6BA71  74 09                           je 0x140a6ba7c
00A6BA73  49 8B 96 E0 03 00 00            mov rdx, qword ptr [r14 + 0x3e0]
00A6BA7A  EB 0A                           jmp 0x140a6ba86
00A6BA7C  48 8B 13                        mov rdx, qword ptr [rbx]
00A6BA7F  48 81 EA 10 27 00 00            sub rdx, 0x2710
00A6BA86  48 8B CE                        mov rcx, rsi
00A6BA89  E8 82 09 00 00                  call 0x140a6c410
00A6BA8E  48 8B 05 73 95 55 00            mov rax, qword ptr [rip + 0x559573]
00A6BA95  F0 44 01 A8 5C 02 00 00         lock add dword ptr [rax + 0x25c], r13d
00A6BA9D  44 39 3D CC CA 3F 00            cmp dword ptr [rip + 0x3fcacc], r15d
00A6BAA4  75 0C                           jne 0x140a6bab2
00A6BAA6  41 8B 8E B4 01 00 00            mov ecx, dword ptr [r14 + 0x1b4]
00A6BAAD  E8 7A 3F D2 FF                  call 0x14078fa2c
00A6BAB2  0F B7 5D A0                     movzx ebx, word ptr [rbp - 0x60]
00A6BAB6  66 41 3B 9E D8 03 00 00         cmp bx, word ptr [r14 + 0x3d8]
00A6BABE  74 14                           je 0x140a6bad4
00A6BAC0  0F B7 CB                        movzx ecx, bx
00A6BAC3  E8 D4 46 D2 FF                  call 0x14079019c
00A6BAC8  84 C0                           test al, al
00A6BACA  74 08                           je 0x140a6bad4
00A6BACC  66 41 89 9E D8 03 00 00         mov word ptr [r14 + 0x3d8], bx
00A6BAD4  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00A6BAD9  41 8A D4                        mov dl, r12b
00A6BADC  4C 8D 4D 98                     lea r9, [rbp - 0x68]
00A6BAE0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A6BAE5  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00A6BAEA  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A6BAEE  E8 11 07 00 00                  call 0x140a6c204
00A6BAF3  44 8A 4C 24 40                  mov r9b, byte ptr [rsp + 0x40]
00A6BAF8  33 C9                           xor ecx, ecx
00A6BAFA  45 8B 86 B0 01 00 00            mov r8d, dword ptr [r14 + 0x1b0]
00A6BB01  41 8B 96 B4 01 00 00            mov edx, dword ptr [r14 + 0x1b4]
00A6BB08  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00A6BB0D  E8 66 05 00 00                  call 0x140a6c078
00A6BB12  41 8A C5                        mov al, r13b
00A6BB15  48 8B 8D 80 03 00 00            mov rcx, qword ptr [rbp + 0x380]
00A6BB1C  48 33 CC                        xor rcx, rsp
00A6BB1F  E8 1C 0B C4 FF                  call 0x1406ac640
00A6BB24  4C 8D 9C 24 90 04 00 00         lea r11, [rsp + 0x490]
00A6BB2C  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00A6BB30  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00A6BB34  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00A6BB38  49 8B E3                        mov rsp, r11
00A6BB3B  41 5F                           pop r15
00A6BB3D  41 5E                           pop r14
00A6BB3F  41 5D                           pop r13
00A6BB41  41 5C                           pop r12
00A6BB43  5D                              pop rbp
00A6BB44  C3                              ret
00A6BB45  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpRefreshTimeZoneInformation(unsigned __int8 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m43C;
    unsigned __int64 v_stack_m440;
    unsigned int v_stack_m448;
    unsigned __int64 v_stack_m450;
    unsigned __int64 v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned __int64 v_stack_m470;
    unsigned __int8 v_stack_m478;
    unsigned __int64 v_stack_m488;
    unsigned int v_stack_m490;
    unsigned __int8 v_stack_m498;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (0x490ULL);
    result = (*(unsigned __int64 *)(v_rip + 3797671)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 952 + 896) = result;
    a2 = 0;
    result = memset(v_rsp - 952 - 64, a2, 432, a4);
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 952 - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 952 - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 952 - 112) = 0;
    v_stack_m458 = 0;
    v_stack_m440 = 0;
    v_stack_m478 = 0;
    result = PsGetCurrentServerSilo(v_rsp - 952 - 64, a2, 432, a4);
    result = PsGetServerSiloGlobals(result, a2, 432, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 592)) != 0) goto loc_00A6B508;
    result = ExpInitializeTimeZoneInformation(result, *(unsigned __int64 *)(result + 1224), 432, a4);
    goto loc_00A6B50B;
loc_00A6B508:
loc_00A6B50B:
    if (a1 == 0) goto loc_00A6B546;
    result = ExpReadSiloTimeZoneMarker(result, *(unsigned __int64 *)(result + 1224), 432, a4);
    v_rdi = 0;
    if ((unsigned __int8)(result) == 0) {
        a1 = 0;
        result = PsAttachSiloToCurrentThread(a1, *(unsigned __int64 *)(result + 1224), 432, a4);
        v_rdi = result;
    }
    result = RtlpQueryTimeZoneInformationWorker(v_rsp - 952 - 64, 432, 432, a4);
    if (v_rdi == 0) goto loc_00A6B5DA;
    result = PsDetachSiloFromCurrentThread(v_rdi, 432, 432, a4);
    goto loc_00A6B5DA;
loc_00A6B546:
    result = PsIsCurrentThreadInServerSilo(v_rdi, 432, 432, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A6B5CC;
    result = ExpReadSiloTimeZoneMarker(v_rdi, 432, 432, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A6B5D0;
loc_00A6B568:
    *(unsigned __int64 *)(v_rsp - 952 - 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 952 - 64 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 952 - 64 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 952 - 64 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 952 - 64 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 952 - 64 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 952 - 64 + 96) = v_xmm0;
    a1 = (v_rsp - 952 - 64) + (3 + 125);
    result = (*(unsigned __int64 *)(result + 1224)) + (3 + 125);
    *(unsigned __int64 *)(a1 - 16) = v_xmm1;
    a2 = (3) - (1);
    if (condition_is_not_equal) goto loc_00A6B568;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    goto loc_00A6B5DA;
loc_00A6B5CC:
loc_00A6B5D0:
    result = RtlpQueryTimeZoneInformationWorker(v_rsp - 952 - 64, 432, 3 + 125, a4);
loc_00A6B5DA:
    if (!sign_flag) goto loc_00A6B61C;
    *(unsigned __int8 *)(v_rip + 3814823) = 1;
    result = ExpLogRefreshTimeZoneInformationQueryFail((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 0, 3 + 125, a4);
    a4 = 0;
loc_00A6B5FD:
    v_stack_m498 = 0;
    result = EtwTraceTimeZoneInformationRefresh(a4 + 1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 432)), a4);
    result = 0;
    goto loc_00A6BB15;
loc_00A6B61C:
    v_rdi = 0;
    v_rbx = (*(unsigned __int64 *)(v_rsi)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 440));
    v_stack_m460 = v_rbx;
    if ((*(unsigned __int8 *)(v_rsp - 952 + 364)) != 0) goto loc_00A6B675;
    if ((*(unsigned __int16 *)(v_rsp - 952 + 108)) == 0) goto loc_00A6B675;
    result = RtlTimeToTimeFields(v_stack_m460, v_rsp - 952 - 96, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 432)), a4);
    result = RtlpCheckDynamicTimeZoneInformation(v_rsp - 952 - 64, *(unsigned __int16 *)(v_rsp - 952 - 96), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 432)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A6B675;
    v_stack_m478 = 1;
    goto loc_00A6B6F7;
loc_00A6B675:
    if (0 == 0) goto loc_00A6B703;
    a4 = 0;
    v_stack_m488 = v_rsp - 952 - 80;
    v_stack_m490 = 520;
    a3 = 0;
    v_stack_m498 = v_rsp - 952 + 368;
    result = RtlGetPersistedStateLocation(v_rip + 631489, v_rip + 630815, a3, a4);
    if (sign_flag) goto loc_00A6B703;
    *(unsigned __int64 *)(v_rsp - 952 - 128) = 0;
    a3 = 0;
    a1 = 0;
    result = RtlpGetRegistryHandle(a1, v_rsp - 952 + 368, a3, v_rsp - 952 - 128);
    v_r13 = (((unsigned int)(result)) == 0xC0000034ULL) ? 1 : 0;
    v_stack_m478 = (unsigned __int8)(v_r13);
    if (*(unsigned __int64 *)(v_rsp - 952 - 128) != 0) {
        result = ZwClose(*(unsigned __int64 *)(v_rsp - 952 - 128), v_rsp - 952 + 368, a3, v_rsp - 952 - 128);
    }
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000034ULL) {
        a2 = 432;
        a1 = v_rsp - 952 - 64;
        result = RtlpSetTimeZoneInformationWorker(a1, a2, a3, v_rsp - 952 - 128);
    }
    result = (result) | (-1);
    v_stack_m450 = result;
    *(unsigned __int64 *)(v_rsp - 952 - 104) = result;
    result = 0;
    v_stack_m448 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 952 - 64)));
    if ((*(unsigned __int16 *)(v_rsp - 952 + 6)) == 0) goto loc_00A6B849;
    if ((*(unsigned __int16 *)(v_rsp - 952 + 90)) == 0) goto loc_00A6B849;
    result = RtlCutoverTimeToSystemTime(v_rsp - 952 + 4, v_rsp - 952 - 120, v_stack_m460, v_rsp - 952 - 128);
    if ((unsigned __int8)(result) != 0) goto loc_00A6B778;
    *(unsigned __int8 *)(v_rip + 3814460) = 1;
    result = ExpLogRefreshTimeZoneInformationCutoverFail(v_rsp - 952 - 64, 0, v_stack_m450, 2);
    goto loc_00A6B5FD;
loc_00A6B778:
    v_stack_m450 = *(unsigned __int64 *)(v_rsp - 952 - 120);
    result = RtlCutoverTimeToSystemTime(v_rsp - 952 + 88, v_rsp - 952 - 112, v_stack_m460, v_stack_m478);
    a2 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00A6B7C8;
    *(unsigned __int8 *)(v_rip + 3814379) = 1;
    result = ExpLogRefreshTimeZoneInformationCutoverFail(v_rsp - 952 - 64, 0, v_stack_m450, (unsigned int)((unsigned int)(a2 + 3)));
    goto loc_00A6B5FD;
loc_00A6B7C8:
    *(unsigned __int64 *)(v_rsp - 952 - 104) = *(unsigned __int64 *)(v_rsp - 952 - 112);
    if (v_rbx < (*(unsigned __int64 *)(v_rsp - 952 - 112))) goto loc_00A6B7F4;
    if (v_rbx < (a2 + 3)) goto loc_00A6B7F4;
    v_stack_m470 = 0;
    a1 = ((a2 + 3) <= (*(unsigned __int64 *)(v_rsp - 952 - 112))) ? 1 : 0;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A6B827;
loc_00A6B7F4:
    if ((*(unsigned __int64 *)(v_rsp - 952 - 112)) >= (a2 + 3)) goto loc_00A6B812;
    if (0 < (*(unsigned __int64 *)(v_rsp - 952 - 112))) goto loc_00A6B803;
    if (0 < (a2 + 3)) goto loc_00A6B81C;
loc_00A6B803:
    v_stack_m470 = *(unsigned __int64 *)(v_rsp - 952 - 112);
    goto loc_00A6B827;
loc_00A6B812:
    if ((*(unsigned __int64 *)(v_rsp - 952 - 112)) < (a2 + 3)) goto loc_00A6B81C;
    if ((*(unsigned __int64 *)(v_rsp - 952 - 112)) < (*(unsigned __int64 *)(v_rsp - 952 - 112))) goto loc_00A6B803;
loc_00A6B81C:
    v_stack_m470 = a2 + 3;
loc_00A6B827:
    v_r15 = (432) + (*(unsigned __int64 *)(result + 1224));
    *(unsigned int *)(v_r15) = 2;
    result = (unsigned int)(*(unsigned int *)(v_rsp - 952 + 20));
    if (2 == 2) { result = *(unsigned int *)(v_rsp - 952 + 104); }
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m448)) + ((unsigned int)(result)));
    goto loc_00A6B86B;
loc_00A6B849:
    result = KeCancelTimer(*(unsigned __int64 *)(result + 1224) + 512, 0, v_stack_m450, 2);
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 432) = 0;
    v_stack_m470 = 0;
loc_00A6B86B:
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436)) != ((unsigned int)(v_rdi))) {
        a1 = v_rip - 10792456;
        v_stack_m488 = 0;
        a4 = 0;
        v_stack_m490 = 0;
        v_stack_m440 = 0;
        v_stack_m498 = 0;
        a2 = v_stack_m440;
        a3 = a4 + 8;
        result = ZwUpdateWnfStateData(a1, a2, a3, a4);
        a2 = *(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436);
        a1 = (unsigned int)(v_rdi);
        result = EtwTraceTimeZoneBiasChange(a1, a2, a3, a4);
    }
    result = (unsigned int)((result) * ((unsigned int)(v_rdi)));
    *(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436) = (unsigned int)(v_rdi);
    result = (result) * ((int)((unsigned int)(result)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 440) = result;
loc_00A6B8DA:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 16) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 48) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 64) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 80) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 96) = v_xmm0;
    result = (*(unsigned __int64 *)(result + 1224)) + (3 + 125);
    a1 = (v_rsp - 952 - 64) + (3 + 125);
    *(unsigned __int64 *)(result - 16) = v_xmm1;
    v_rdi = (3) - (1);
    if (condition_is_not_equal) goto loc_00A6B8DA;
    a2 = 0;
    *(unsigned __int8 *)(v_rip + 3813989) = 0;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    result = RtlSetSystemGlobalData(v_rdi + 6, *(unsigned __int64 *)(result + 1224) + 432, v_rdi + 4, a4);
    result = RtlTimeToTimeFields(v_stack_m460, v_rsp - 952 - 96, v_rdi + 4, a4);
    v_r15 = 0;
    v_rbx = 0;
    if (0 != 0) {
        v_rbx = *(unsigned __int64 *)(result + 1224) + 992;
        a2 = v_rbx;
        a1 = v_stack_m470;
        result = ExLocalTimeToSystemTime(a1, a2, v_rdi + 4, a4);
        a2 = *(unsigned __int64 *)(v_rbx);
        result = *(unsigned __int64 *)(result + 1224) + 448;
        a4 = 0;
        v_stack_m498 = result;
        a3 = 0;
        a1 = *(unsigned __int64 *)(result + 1224) + 512;
        result = KiSetTimerEx(a1, a2, a3, a4);
    }
    a2 = (unsigned int)((a2) >> (5));
    result = (unsigned int)(((unsigned int)(a2)) >> (31));
    result = (unsigned int)((result) + (a2));
    result = (unsigned __int16)((result) + (1));
    a2 = (unsigned int)((a2) * ((unsigned int)(result)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(result + 1224) + 944) = (unsigned __int16)(a2);
    result = RtlTimeFieldsToTime(*(unsigned __int64 *)(result + 1224) + 944, v_stack_m458, a3, a4);
    result = ExLocalTimeToSystemTime(v_stack_m458, *(unsigned __int64 *)(result + 1224) + 936, a3, a4);
    v_stack_m498 = *(unsigned __int64 *)(result + 1224) + 608;
    a4 = 0;
    a3 = 0;
    result = KiSetTimerEx(*(unsigned __int64 *)(result + 1224) + 672, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 936), a3, a4);
    v_rdi = (unsigned __int16)(((__int16)(*(unsigned __int16 *)(v_rsp - 952 - 96))) + (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(result + 1224) + 968) = (unsigned __int16)(v_rdi);
    result = RtlTimeFieldsToTime(*(unsigned __int64 *)(result + 1224) + 968, v_stack_m458, a3, a4);
    result = ExLocalTimeToSystemTime(v_stack_m458, *(unsigned __int64 *)(result + 1224) + 960, a3, a4);
    v_stack_m498 = *(unsigned __int64 *)(result + 1224) + 768;
    a4 = 0;
    a3 = 0;
    result = KiSetTimerEx(*(unsigned __int64 *)(result + 1224) + 832, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 960), a3, a4);
    result = ExpWriteTimeZoneBias(*(unsigned __int64 *)(result + 1224) + 440, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 960), a3, a4);
    if (v_stack_m470 == 0) goto loc_00A6BA7C;
    goto loc_00A6BA86;
loc_00A6BA7C:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 960)) - (0x2710ULL);
loc_00A6BA86:
    result = ExpWriteTimeZoneBiasStartEnd(*(unsigned __int64 *)(v_rsi), a2, a3, a4);
    result = *(unsigned __int64 *)(v_rip + 5608819);
    if ((*(unsigned int *)(v_rip + 4180684)) == 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436);
        result = RtlSetActiveTimeBias(a1, a2, a3, a4);
    }
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 952 - 96))) == (*(unsigned __int16 *)(*(unsigned __int64 *)(result + 1224) + 984))) goto loc_00A6BAD4;
    result = RtlpUpdateDynamicTimeZones((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 952 - 96)), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        *(unsigned __int16 *)(*(unsigned __int64 *)(result + 1224) + 984) = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 952 - 96));
    }
    v_stack_m498 = v_stack_m470;
    result = ExpLogRefreshTimeZoneInformationSuccess(v_rsp - 952 - 64, 0, v_stack_m450, v_rsp - 952 - 104);
    a1 = 0;
    v_stack_m498 = 0;
    result = EtwTraceTimeZoneInformationRefresh(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 432)), v_stack_m478);
loc_00A6BB15:
    a1 = (*(unsigned __int64 *)(v_rsp - 952 + 896)) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 432)), v_stack_m478);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpRefreshTimeZoneInformation(uint8_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m43C;
    uint64_t v_stack_m440;
    uint32_t v_stack_m448;
    uint64_t v_stack_m450;
    uint64_t v_stack_m458;
    uint64_t v_stack_m460;
    uint64_t v_stack_m470;
    uint8_t v_stack_m478;
    uint64_t v_stack_m488;
    uint32_t v_stack_m490;
    uint8_t v_stack_m498;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (0x490ULL);
    result = (*(uint64_t *)(v_rip + 0x39F2A7)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x3B8 + 0x380) = result;
    Arg2 = 0;
    result = memset(local_rsp - 952 - 64, Arg2, 432, Arg4);
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x70) = 0;
    v_stack_m458 = 0;
    v_stack_m440 = 0;
    v_stack_m478 = 0;
    result = PsGetCurrentServerSilo(local_rsp - 952 - 64, Arg2, 432, Arg4);
    result = PsGetServerSiloGlobals(result, Arg2, 432, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x250)) != 0) goto loc_00A6B508;
    result = ExpInitializeTimeZoneInformation(result, *(uint64_t *)(result + 0x4C8), 432, Arg4);
    goto loc_00A6B50B;
loc_00A6B508:
loc_00A6B50B:
    if (Arg1 == 0) goto loc_00A6B546;
    result = ExpReadSiloTimeZoneMarker(result, *(uint64_t *)(result + 0x4C8), 432, Arg4);
    local_rdi = 0;
    if ((uint8_t)(result) == 0) {
        Arg1 = 0;
        result = PsAttachSiloToCurrentThread(Arg1, *(uint64_t *)(result + 0x4C8), 432, Arg4);
        local_rdi = result;
    }
    result = RtlpQueryTimeZoneInformationWorker(local_rsp - 952 - 64, 432, 432, Arg4);
    if (local_rdi == 0) goto loc_00A6B5DA;
    result = PsDetachSiloFromCurrentThread(local_rdi, 432, 432, Arg4);
    goto loc_00A6B5DA;
loc_00A6B546:
    result = PsIsCurrentThreadInServerSilo(local_rdi, 432, 432, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A6B5CC;
    result = ExpReadSiloTimeZoneMarker(local_rdi, 432, 432, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00A6B5D0;
loc_00A6B568:
    *(uint64_t *)(local_rsp - 0x3B8 - 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x40 + 0x10) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x40 + 0x20) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x40 + 0x30) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x40 + 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x40 + 0x50) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x40 + 0x60) = v_xmm0;
    Arg1 = (local_rsp - 952 - 64) + (3 + 125);
    result = (*(uint64_t *)(result + 0x4C8)) + (3 + 125);
    *(uint64_t *)(Arg1 - 0x10) = v_xmm1;
    Arg2 = (3) - (1);
    if (condition_is_not_equal) goto loc_00A6B568;
    *(uint64_t *)(Arg1) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x20) = v_xmm0;
    goto loc_00A6B5DA;
loc_00A6B5CC:
loc_00A6B5D0:
    result = RtlpQueryTimeZoneInformationWorker(local_rsp - 952 - 64, 432, 3 + 125, Arg4);
loc_00A6B5DA:
    if (!sign_flag) goto loc_00A6B61C;
    *(uint8_t *)(v_rip + 0x3A35A7) = 1;
    result = ExpLogRefreshTimeZoneInformationQueryFail((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 0, 3 + 125, Arg4);
    Arg4 = 0;
loc_00A6B5FD:
    v_stack_m498 = 0;
    result = EtwTraceTimeZoneInformationRefresh(Arg4 + 1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B0)), Arg4);
    result = 0;
    goto loc_00A6BB15;
loc_00A6B61C:
    local_rdi = 0;
    local_rbx = (*(uint64_t *)(local_rsi)) - (*(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B8));
    v_stack_m460 = local_rbx;
    if ((*(uint8_t *)(local_rsp - 0x3B8 + 0x16C)) != 0) goto loc_00A6B675;
    if ((*(uint16_t *)(local_rsp - 0x3B8 + 0x6C)) == 0) goto loc_00A6B675;
    result = RtlTimeToTimeFields(v_stack_m460, local_rsp - 952 - 96, (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B0)), Arg4);
    result = RtlpCheckDynamicTimeZoneInformation(local_rsp - 952 - 64, *(uint16_t *)(local_rsp - 0x3B8 - 0x60), (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B0)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A6B675;
    v_stack_m478 = 1;
    goto loc_00A6B6F7;
loc_00A6B675:
    if (0 == 0) goto loc_00A6B703;
    Arg4 = 0;
    v_stack_m488 = local_rsp - 952 - 80;
    v_stack_m490 = 520;
    Arg3 = 0;
    v_stack_m498 = local_rsp - 952 + 368;
    result = RtlGetPersistedStateLocation(v_rip + 631489, v_rip + 630815, Arg3, Arg4);
    if (sign_flag) goto loc_00A6B703;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x80) = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = RtlpGetRegistryHandle(Arg1, local_rsp - 952 + 368, Arg3, local_rsp - 952 - 128);
    local_r13 = (((uint32_t)(result)) == 0xC0000034ULL) ? 1 : 0;
    v_stack_m478 = (uint8_t)(local_r13);
    if (*(uint64_t *)(local_rsp - 0x3B8 - 0x80) != 0) {
        result = ZwClose(*(uint64_t *)(local_rsp - 0x3B8 - 0x80), local_rsp - 952 + 368, Arg3, local_rsp - 952 - 128);
    }
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000034ULL) {
        Arg2 = 432;
        Arg1 = local_rsp - 952 - 64;
        result = RtlpSetTimeZoneInformationWorker(Arg1, Arg2, Arg3, local_rsp - 952 - 128);
    }
    result = (result) | (-1);
    v_stack_m450 = result;
    *(uint64_t *)(local_rsp - 0x3B8 - 0x68) = result;
    result = 0;
    v_stack_m448 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3B8 - 0x40)));
    if ((*(uint16_t *)(local_rsp - 0x3B8 + 0x6)) == 0) goto loc_00A6B849;
    if ((*(uint16_t *)(local_rsp - 0x3B8 + 0x5A)) == 0) goto loc_00A6B849;
    result = RtlCutoverTimeToSystemTime(local_rsp - 952 + 4, local_rsp - 952 - 120, v_stack_m460, local_rsp - 952 - 128);
    if ((uint8_t)(result) != 0) goto loc_00A6B778;
    *(uint8_t *)(v_rip + 0x3A343C) = 1;
    result = ExpLogRefreshTimeZoneInformationCutoverFail(local_rsp - 952 - 64, 0, v_stack_m450, 2);
    goto loc_00A6B5FD;
loc_00A6B778:
    v_stack_m450 = *(uint64_t *)(local_rsp - 0x3B8 - 0x78);
    result = RtlCutoverTimeToSystemTime(local_rsp - 952 + 88, local_rsp - 952 - 112, v_stack_m460, v_stack_m478);
    Arg2 = 0;
    if ((uint8_t)(result) != 0) goto loc_00A6B7C8;
    *(uint8_t *)(v_rip + 0x3A33EB) = 1;
    result = ExpLogRefreshTimeZoneInformationCutoverFail(local_rsp - 952 - 64, 0, v_stack_m450, (uint32_t)((uint32_t)(Arg2 + 3)));
    goto loc_00A6B5FD;
loc_00A6B7C8:
    *(uint64_t *)(local_rsp - 0x3B8 - 0x68) = *(uint64_t *)(local_rsp - 0x3B8 - 0x70);
    if (local_rbx < (*(uint64_t *)(local_rsp - 0x3B8 - 0x70))) goto loc_00A6B7F4;
    if (local_rbx < (Arg2 + 3)) goto loc_00A6B7F4;
    v_stack_m470 = 0;
    Arg1 = ((Arg2 + 3) <= (*(uint64_t *)(local_rsp - 0x3B8 - 0x70))) ? 1 : 0;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A6B827;
loc_00A6B7F4:
    if ((*(uint64_t *)(local_rsp - 0x3B8 - 0x70)) >= (Arg2 + 3)) goto loc_00A6B812;
    if (0 < (*(uint64_t *)(local_rsp - 0x3B8 - 0x70))) goto loc_00A6B803;
    if (0 < (Arg2 + 3)) goto loc_00A6B81C;
loc_00A6B803:
    v_stack_m470 = *(uint64_t *)(local_rsp - 0x3B8 - 0x70);
    goto loc_00A6B827;
loc_00A6B812:
    if ((*(uint64_t *)(local_rsp - 0x3B8 - 0x70)) < (Arg2 + 3)) goto loc_00A6B81C;
    if ((*(uint64_t *)(local_rsp - 0x3B8 - 0x70)) < (*(uint64_t *)(local_rsp - 0x3B8 - 0x70))) goto loc_00A6B803;
loc_00A6B81C:
    v_stack_m470 = Arg2 + 3;
loc_00A6B827:
    local_r15 = (432) + (*(uint64_t *)(result + 0x4C8));
    *(uint32_t *)(local_r15) = 2;
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x3B8 + 0x14));
    if (2 == 2) { result = *(uint32_t *)(local_rsp - 0x3B8 + 0x68); }
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m448)) + ((uint32_t)(result)));
    goto loc_00A6B86B;
loc_00A6B849:
    result = KeCancelTimer(*(uint64_t *)(result + 0x4C8) + 512, 0, v_stack_m450, 2);
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B0) = 0;
    v_stack_m470 = 0;
loc_00A6B86B:
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4)) != ((uint32_t)(local_rdi))) {
        Arg1 = v_rip - 10792456;
        v_stack_m488 = 0;
        Arg4 = 0;
        v_stack_m490 = 0;
        v_stack_m440 = 0;
        v_stack_m498 = 0;
        Arg2 = v_stack_m440;
        Arg3 = Arg4 + 8;
        result = ZwUpdateWnfStateData(Arg1, Arg2, Arg3, Arg4);
        Arg2 = *(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4);
        Arg1 = (uint32_t)(local_rdi);
        result = EtwTraceTimeZoneBiasChange(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)((result) * ((uint32_t)(local_rdi)));
    *(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4) = (uint32_t)(local_rdi);
    result = (result) * ((int32_t)((uint32_t)(result)));
    *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B8) = result;
loc_00A6B8DA:
    *(uint64_t *)(*(uint64_t *)(result + 0x4C8)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x10) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x30) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x40) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x50) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x60) = v_xmm0;
    result = (*(uint64_t *)(result + 0x4C8)) + (3 + 125);
    Arg1 = (local_rsp - 952 - 64) + (3 + 125);
    *(uint64_t *)(result - 0x10) = v_xmm1;
    local_rdi = (3) - (1);
    if (condition_is_not_equal) goto loc_00A6B8DA;
    Arg2 = 0;
    *(uint8_t *)(v_rip + 0x3A3265) = 0;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    result = RtlSetSystemGlobalData(local_rdi + 6, *(uint64_t *)(result + 0x4C8) + 432, local_rdi + 4, Arg4);
    result = RtlTimeToTimeFields(v_stack_m460, local_rsp - 952 - 96, local_rdi + 4, Arg4);
    local_r15 = 0;
    local_rbx = 0;
    if (0 != 0) {
        local_rbx = *(uint64_t *)(result + 0x4C8) + 992;
        Arg2 = local_rbx;
        Arg1 = v_stack_m470;
        result = ExLocalTimeToSystemTime(Arg1, Arg2, local_rdi + 4, Arg4);
        Arg2 = *(uint64_t *)(local_rbx);
        result = *(uint64_t *)(result + 0x4C8) + 448;
        Arg4 = 0;
        v_stack_m498 = result;
        Arg3 = 0;
        Arg1 = *(uint64_t *)(result + 0x4C8) + 512;
        result = KiSetTimerEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = (uint32_t)((Arg2) >> (5));
    result = (uint32_t)(((uint32_t)(Arg2)) >> (31));
    result = (uint32_t)((result) + (Arg2));
    result = (uint16_t)((result) + (1));
    Arg2 = (uint32_t)((Arg2) * ((uint32_t)(result)));
    *(uint16_t *)(*(uint64_t *)(result + 0x4C8) + 0x3B0) = (uint16_t)(Arg2);
    result = RtlTimeFieldsToTime(*(uint64_t *)(result + 0x4C8) + 944, v_stack_m458, Arg3, Arg4);
    result = ExLocalTimeToSystemTime(v_stack_m458, *(uint64_t *)(result + 0x4C8) + 936, Arg3, Arg4);
    v_stack_m498 = *(uint64_t *)(result + 0x4C8) + 608;
    Arg4 = 0;
    Arg3 = 0;
    result = KiSetTimerEx(*(uint64_t *)(result + 0x4C8) + 672, *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x3A8), Arg3, Arg4);
    local_rdi = (uint16_t)(((int16_t)(*(uint16_t *)(local_rsp - 0x3B8 - 0x60))) + (1));
    *(uint16_t *)(*(uint64_t *)(result + 0x4C8) + 0x3C8) = (uint16_t)(local_rdi);
    result = RtlTimeFieldsToTime(*(uint64_t *)(result + 0x4C8) + 968, v_stack_m458, Arg3, Arg4);
    result = ExLocalTimeToSystemTime(v_stack_m458, *(uint64_t *)(result + 0x4C8) + 960, Arg3, Arg4);
    v_stack_m498 = *(uint64_t *)(result + 0x4C8) + 768;
    Arg4 = 0;
    Arg3 = 0;
    result = KiSetTimerEx(*(uint64_t *)(result + 0x4C8) + 832, *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x3C0), Arg3, Arg4);
    result = ExpWriteTimeZoneBias(*(uint64_t *)(result + 0x4C8) + 440, *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x3C0), Arg3, Arg4);
    if (v_stack_m470 == 0) goto loc_00A6BA7C;
    goto loc_00A6BA86;
loc_00A6BA7C:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x3C0)) - (0x2710ULL);
loc_00A6BA86:
    result = ExpWriteTimeZoneBiasStartEnd(*(uint64_t *)(local_rsi), Arg2, Arg3, Arg4);
    result = *(uint64_t *)(v_rip + 0x559573);
    if ((*(uint32_t *)(v_rip + 0x3FCACC)) == 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4);
        result = RtlSetActiveTimeBias(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x3B8 - 0x60))) == (*(uint16_t *)(*(uint64_t *)(result + 0x4C8) + 0x3D8))) goto loc_00A6BAD4;
    result = RtlpUpdateDynamicTimeZones((uint16_t)(*(uint16_t *)(local_rsp - 0x3B8 - 0x60)), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        *(uint16_t *)(*(uint64_t *)(result + 0x4C8) + 0x3D8) = (uint16_t)(*(uint16_t *)(local_rsp - 0x3B8 - 0x60));
    }
    v_stack_m498 = v_stack_m470;
    result = ExpLogRefreshTimeZoneInformationSuccess(local_rsp - 952 - 64, 0, v_stack_m450, local_rsp - 952 - 104);
    Arg1 = 0;
    v_stack_m498 = 0;
    result = EtwTraceTimeZoneInformationRefresh(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B0)), v_stack_m478);
loc_00A6BB15:
    Arg1 = (*(uint64_t *)(local_rsp - 0x3B8 + 0x380)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B0)), v_stack_m478);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6B46C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
