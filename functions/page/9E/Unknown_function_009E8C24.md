# sub_009E8C24

- RVA: `0x009E8C24`–`0x009E9269` (길이 `1,605` bytes)
- VA: `0x00000001409E8C24`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A4F10`
- 디코드: `399`개 명령, `1,605/1,605` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009E8C5F` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009E8CBC` → [EtwpGetMetaProviderContext](../../text/43/EtwpGetMetaProviderContext_function_00437B70.md) (function, `0x00437B70`)
- `0x009E8CD6` → [EtwpFindGuidEntryByGuid](../8C/EtwpFindGuidEntryByGuid_function_008C1DB0.md) (function, `0x008C1DB0`)
- `0x009E8CF7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009E8D19` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009E8D3E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009E8E69` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009E8E77` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x009E8E89` → [EtwpUnreferenceGuidEntry](../8C/EtwpUnreferenceGuidEntry_function_008C3320.md) (function, `0x008C3320`)
- `0x009E8F25` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009E8F33` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x009E8F90` → [EtwpUnreferenceGuidEntry](../8C/EtwpUnreferenceGuidEntry_function_008C3320.md) (function, `0x008C3320`)
- `0x009E9069` → [EtwpUnreferenceGuidEntry](../8C/EtwpUnreferenceGuidEntry_function_008C3320.md) (function, `0x008C3320`)
- `0x009E90A9` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x009E918B` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x009E91A1` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x009E91F4` → [EtwpMapMetaProviderKeywords](../../text/47/EtwpMapMetaProviderKeywords_function_00471A84.md) (function, `0x00471A84`)
- `0x009E920C` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (function, `0x00396810`)
- `0x009E922B` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x009E9238` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009E8C29` → RVA `0x00B4C360` (`EtwpUmglProviders`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x009E8C5F` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009E8CBC` → [EtwpGetMetaProviderContext](../../text/43/EtwpGetMetaProviderContext_function_00437B70.md) (`PAGE` → `.text`)
  - `0x009E8CF7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009E8D19` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009E8D3E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009E8E69` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009E8E77` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x009E8F25` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009E8F33` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x009E90A9` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x009E91A1` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x009E91F4` → [EtwpMapMetaProviderKeywords](../../text/47/EtwpMapMetaProviderKeywords_function_00471A84.md) (`PAGE` → `.text`)
  - `0x009E920C` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (`PAGE` → `.text`)
  - `0x009E922B` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x009E9238` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009E8C7D` → [sub_009E9280](Unknown_function_009E9280.md) (`tail-transfer`)
  - `0x009E8DD4` → [sub_009E9280 + 0x36](Unknown_function_009E9280.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009E8C24  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
009E8C29  48 8D 05 30 37 16 00            lea rax, [rip + 0x163730]
009E8C30  83 FA 0A                        cmp edx, 0xa
009E8C33  0F 83 80 00 00 00               jae 0x1409e8cb9
009E8C39  8B FA                           mov edi, edx
009E8C3B  48 03 FF                        add rdi, rdi
009E8C3E  4C 8B 04 F8                     mov r8, qword ptr [rax + rdi*8]
009E8C42  49 8B 08                        mov rcx, qword ptr [r8]
009E8C45  48 2B 0E                        sub rcx, qword ptr [rsi]
009E8C48  75 08                           jne 0x1409e8c52
009E8C4A  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
009E8C4E  48 2B 4E 08                     sub rcx, qword ptr [rsi + 8]
009E8C52  48 85 C9                        test rcx, rcx
009E8C55  75 5B                           jne 0x1409e8cb2
009E8C57  4D 8B C4                        mov r8, r12
009E8C5A  33 D2                           xor edx, edx
009E8C5C  49 8B CF                        mov rcx, r15
009E8C5F  E8 DC DF CD FF                  call 0x1406c6c40
009E8C64  48 8D 05 F5 36 16 00            lea rax, [rip + 0x1636f5]
009E8C6B  BB 18 00 00 00                  mov ebx, 0x18
009E8C70  0F B6 44 F8 08                  movzx eax, byte ptr [rax + rdi*8 + 8]
009E8C75  45 38 2C 46                     cmp byte ptr [r14 + rax*2], r13b
009E8C79  49 8D 0C 46                     lea rcx, [r14 + rax*2]
009E8C7D  0F 85 FD 05 00 00               jne 0x1409e9280
009E8C83  44 3B E3                        cmp r12d, ebx
009E8C86  0F 82 17 02 00 00               jb 0x1409e8ea3
009E8C8C  45 33 C0                        xor r8d, r8d
009E8C8F  45 89 47 0C                     mov dword ptr [r15 + 0xc], r8d
009E8C93  41 C7 07 01 00 00 00            mov dword ptr [r15], 1
009E8C9A  41 8B F5                        mov esi, r13d
009E8C9D  41 C7 47 14 01 00 00 00         mov dword ptr [r15 + 0x14], 1
009E8CA5  45 89 47 10                     mov dword ptr [r15 + 0x10], r8d
009E8CA9  45 89 47 08                     mov dword ptr [r15 + 8], r8d
009E8CAD  E9 E3 02 00 00                  jmp 0x1409e8f95
009E8CB2  FF C2                           inc edx
009E8CB4  E9 70 FF FF FF                  jmp 0x1409e8c29
009E8CB9  48 8B CE                        mov rcx, rsi
009E8CBC  E8 AF EE A4 FF                  call 0x140437b70
009E8CC1  48 8B F8                        mov rdi, rax
009E8CC4  48 85 C0                        test rax, rax
009E8CC7  0F 85 7E 04 00 00               jne 0x1409e914b
009E8CCD  45 33 C0                        xor r8d, r8d
009E8CD0  48 8B D6                        mov rdx, rsi
009E8CD3  48 8B CD                        mov rcx, rbp
009E8CD6  E8 D5 90 ED FF                  call 0x1408c1db0
009E8CDB  48 8B E8                        mov rbp, rax
009E8CDE  48 85 C0                        test rax, rax
009E8CE1  0F 84 CC 03 00 00               je 0x1409e90b3
009E8CE7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009E8CEF  33 D2                           xor edx, edx
009E8CF1  49 8B CF                        mov rcx, r15
009E8CF4  44 8B 00                        mov r8d, dword ptr [rax]
009E8CF7  E8 44 DF CD FF                  call 0x1406c6c40
009E8CFC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009E8D05  48 8D 8D 98 02 00 00            lea rcx, [rbp + 0x298]
009E8D0C  45 33 C0                        xor r8d, r8d
009E8D0F  33 D2                           xor edx, edx
009E8D11  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
009E8D18  90                              nop
009E8D19  E8 12 75 82 FF                  call 0x140210230
009E8D1E  F0 48 0F BA AD 98 02 00 00 00   lock bts qword ptr [rbp + 0x298], 0
009E8D28  48 8B F0                        mov rsi, rax
009E8D2B  73 16                           jae 0x1409e8d43
009E8D2D  4C 8D 85 98 02 00 00            lea r8, [rbp + 0x298]
009E8D34  48 8B D0                        mov rdx, rax
009E8D37  48 8D 8D 98 02 00 00            lea rcx, [rbp + 0x298]
009E8D3E  E8 4D 6F 82 FF                  call 0x14020fc90
009E8D43  48 85 F6                        test rsi, rsi
009E8D46  74 04                           je 0x1409e8d4c
009E8D48  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
009E8D4C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009E8D55  48 8D 75 38                     lea rsi, [rbp + 0x38]
009E8D59  48 8B 16                        mov rdx, qword ptr [rsi]
009E8D5C  45 33 D2                        xor r10d, r10d
009E8D5F  48 89 85 A0 02 00 00            mov qword ptr [rbp + 0x2a0], rax
009E8D66  EB 1F                           jmp 0x1409e8d87
009E8D68  40 B7 01                        mov dil, 1
009E8D6B  40 84 7D 5B                     test byte ptr [rbp + 0x5b], dil
009E8D6F  0F 85 96 00 00 00               jne 0x1409e8e0b
009E8D75  48 8B 12                        mov rdx, qword ptr [rdx]
009E8D78  3B 5C 24 70                     cmp ebx, dword ptr [rsp + 0x70]
009E8D7C  0F 86 2B 01 00 00               jbe 0x1409e8ead
009E8D82  44 8B 6C 24 24                  mov r13d, dword ptr [rsp + 0x24]
009E8D87  48 3B D6                        cmp rdx, rsi
009E8D8A  0F 84 58 01 00 00               je 0x1409e8ee8
009E8D90  44 8B CB                        mov r9d, ebx
009E8D93  8D 43 10                        lea eax, [rbx + 0x10]
009E8D96  4D 03 CF                        add r9, r15
009E8D99  40 32 FF                        xor dil, dil
009E8D9C  44 8B E3                        mov r12d, ebx
009E8D9F  3B C3                           cmp eax, ebx
009E8DA1  72 79                           jb 0x1409e8e1c
009E8DA3  41 FF C5                        inc r13d
009E8DA6  44 8B D8                        mov r11d, eax
009E8DA9  4D 03 DF                        add r11, r15
009E8DAC  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
009E8DB1  F6 42 62 08                     test byte ptr [rdx + 0x62], 8
009E8DB5  45 8B F2                        mov r14d, r10d
009E8DB8  8B D8                           mov ebx, eax
009E8DBA  4C 8B EA                        mov r13, rdx
009E8DBD  75 A9                           jne 0x1409e8d68
009E8DBF  66 83 7A 64 00                  cmp word ptr [rdx + 0x64], 0
009E8DC4  75 07                           jne 0x1409e8dcd
009E8DC6  66 83 7A 66 00                  cmp word ptr [rdx + 0x66], 0
009E8DCB  74 A8                           je 0x1409e8d75
009E8DCD  45 8B C2                        mov r8d, r10d
009E8DD0  41 83 F8 10                     cmp r8d, 0x10
009E8DD4  0F 83 DC 04 00 00               jae 0x1409e92b6
009E8DDA  45 8B D0                        mov r10d, r8d
009E8DDD  49 83 C2 04                     add r10, 4
009E8DE1  49 C1 E2 05                     shl r10, 5
009E8DE5  41 83 3C 2A 00                  cmp dword ptr [r10 + rbp], 0
009E8DEA  0F 85 13 03 00 00               jne 0x1409e9103
009E8DF0  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
009E8DF4  48 85 C0                        test rax, rax
009E8DF7  74 0D                           je 0x1409e8e06
009E8DF9  4C 03 D0                        add r10, rax
009E8DFC  41 83 3A 00                     cmp dword ptr [r10], 0
009E8E00  0F 85 B7 02 00 00               jne 0x1409e90bd
009E8E06  41 FF C0                        inc r8d
009E8E09  EB C5                           jmp 0x1409e8dd0
009E8E0B  83 C0 20                        add eax, 0x20
009E8E0E  41 BE 01 00 00 00               mov r14d, 1
009E8E14  3B C3                           cmp eax, ebx
009E8E16  0F 83 5A 02 00 00               jae 0x1409e9076
009E8E1C  45 33 C0                        xor r8d, r8d
009E8E1F  C7 44 24 20 05 00 00 80         mov dword ptr [rsp + 0x20], 0x80000005
009E8E27  4C 89 85 A0 02 00 00            mov qword ptr [rbp + 0x2a0], r8
009E8E2E  48 8D BD 98 02 00 00            lea rdi, [rbp + 0x298]
009E8E35  BB FF FF FF FF                  mov ebx, 0xffffffff
009E8E3A  0F 0D 0F                        prefetchw byte ptr [rdi]
009E8E3D  48 8B 07                        mov rax, qword ptr [rdi]
009E8E40  48 8B C8                        mov rcx, rax
009E8E43  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
009E8E47  48 83 F9 10                     cmp rcx, 0x10
009E8E4B  48 8D 50 F0                     lea rdx, [rax - 0x10]
009E8E4F  49 0F 46 D0                     cmovbe rdx, r8
009E8E53  A8 02                           test al, 2
009E8E55  0F 85 DA 03 00 00               jne 0x1409e9235
009E8E5B  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
009E8E60  0F 85 CF 03 00 00               jne 0x1409e9235
009E8E66  48 8B CF                        mov rcx, rdi
009E8E69  E8 92 87 8F FF                  call 0x1402e1600
009E8E6E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009E8E77  E8 74 61 87 FF                  call 0x14025eff0
009E8E7C  44 8B 74 24 24                  mov r14d, dword ptr [rsp + 0x24]
009E8E81  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
009E8E86  48 8B CD                        mov rcx, rbp
009E8E89  E8 92 A4 ED FF                  call 0x1408c3320
009E8E8E  8B 74 24 20                     mov esi, dword ptr [rsp + 0x20]
009E8E92  85 F6                           test esi, esi
009E8E94  0F 88 FB 00 00 00               js 0x1409e8f95
009E8E9A  41 3B DC                        cmp ebx, r12d
009E8E9D  0F 86 CB 01 00 00               jbe 0x1409e906e
009E8EA3  BE 23 00 00 C0                  mov esi, 0xc0000023
009E8EA8  E9 E8 00 00 00                  jmp 0x1409e8f95
009E8EAD  40 84 FF                        test dil, dil
009E8EB0  74 08                           je 0x1409e8eba
009E8EB2  41 C7 41 0C 01 00 00 00         mov dword ptr [r9 + 0xc], 1
009E8EBA  41 F6 45 62 02                  test byte ptr [r13 + 0x62], 2
009E8EBF  0F 84 B6 00 00 00               je 0x1409e8f7b
009E8EC5  49 8B 45 50                     mov rax, qword ptr [r13 + 0x50]
009E8EC9  8B 88 D0 01 00 00               mov ecx, dword ptr [rax + 0x1d0]
009E8ECF  8B C3                           mov eax, ebx
009E8ED1  41 89 49 08                     mov dword ptr [r9 + 8], ecx
009E8ED5  41 2B C4                        sub eax, r12d
009E8ED8  45 89 71 04                     mov dword ptr [r9 + 4], r14d
009E8EDC  41 89 01                        mov dword ptr [r9], eax
009E8EDF  48 3B D6                        cmp rdx, rsi
009E8EE2  0F 85 9A FE FF FF               jne 0x1409e8d82
009E8EE8  4C 89 95 A0 02 00 00            mov qword ptr [rbp + 0x2a0], r10
009E8EEF  48 8D BD 98 02 00 00            lea rdi, [rbp + 0x298]
009E8EF6  0F 0D 0F                        prefetchw byte ptr [rdi]
009E8EF9  48 8B 07                        mov rax, qword ptr [rdi]
009E8EFC  48 8B C8                        mov rcx, rax
009E8EFF  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
009E8F03  48 83 F9 10                     cmp rcx, 0x10
009E8F07  48 8D 50 F0                     lea rdx, [rax - 0x10]
009E8F0B  49 0F 46 D2                     cmovbe rdx, r10
009E8F0F  A8 02                           test al, 2
009E8F11  0F 85 8F 01 00 00               jne 0x1409e90a6
009E8F17  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
009E8F1C  0F 85 84 01 00 00               jne 0x1409e90a6
009E8F22  48 8B CF                        mov rcx, rdi
009E8F25  E8 D6 86 8F FF                  call 0x1402e1600
009E8F2A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009E8F33  E8 B8 60 87 FF                  call 0x14025eff0
009E8F38  44 8B 74 24 24                  mov r14d, dword ptr [rsp + 0x24]
009E8F3D  8D 53 10                        lea edx, [rbx + 0x10]
009E8F40  44 8B C3                        mov r8d, ebx
009E8F43  41 83 C6 02                     add r14d, 2
009E8F47  4D 03 C7                        add r8, r15
009E8F4A  3B D3                           cmp edx, ebx
009E8F4C  72 35                           jb 0x1409e8f83
009E8F4E  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
009E8F52  44 8D 52 20                     lea r10d, [rdx + 0x20]
009E8F56  44 8B CA                        mov r9d, edx
009E8F59  4D 03 CF                        add r9, r15
009E8F5C  33 F6                           xor esi, esi
009E8F5E  44 8B DE                        mov r11d, esi
009E8F61  8B CE                           mov ecx, esi
009E8F63  83 F9 10                        cmp ecx, 0x10
009E8F66  73 7A                           jae 0x1409e8fe2
009E8F68  8B C1                           mov eax, ecx
009E8F6A  48 83 C0 04                     add rax, 4
009E8F6E  48 C1 E0 05                     shl rax, 5
009E8F72  39 34 28                        cmp dword ptr [rax + rbp], esi
009E8F75  75 40                           jne 0x1409e8fb7
009E8F77  FF C1                           inc ecx
009E8F79  EB E8                           jmp 0x1409e8f63
009E8F7B  41 8B CA                        mov ecx, r10d
009E8F7E  E9 4C FF FF FF                  jmp 0x1409e8ecf
009E8F83  48 8B CD                        mov rcx, rbp
009E8F86  BE 05 00 00 80                  mov esi, 0x80000005
009E8F8B  BB FF FF FF FF                  mov ebx, 0xffffffff
009E8F90  E8 8B A3 ED FF                  call 0x1408c3320
009E8F95  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009E8F9D  89 18                           mov dword ptr [rax], ebx
009E8F9F  8B C6                           mov eax, esi
009E8FA1  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009E8FA6  48 83 C4 30                     add rsp, 0x30
009E8FAA  41 5F                           pop r15
009E8FAC  41 5E                           pop r14
009E8FAE  41 5D                           pop r13
009E8FB0  41 5C                           pop r12
009E8FB2  5E                              pop rsi
009E8FB3  5D                              pop rbp
009E8FB4  5B                              pop rbx
009E8FB5  C3                              ret
009E8FB6  CC                              int3
009E8FB7  41 FF C3                        inc r11d
009E8FBA  44 3B D2                        cmp r10d, edx
009E8FBD  72 C4                           jb 0x1409e8f83
009E8FBF  83 C2 20                        add edx, 0x20
009E8FC2  41 83 C2 20                     add r10d, 0x20
009E8FC6  3B D7                           cmp edx, edi
009E8FC8  77 AD                           ja 0x1409e8f77
009E8FCA  0F 10 04 28                     movups xmm0, xmmword ptr [rax + rbp]
009E8FCE  41 0F 11 01                     movups xmmword ptr [r9], xmm0
009E8FD2  0F 10 4C 28 10                  movups xmm1, xmmword ptr [rax + rbp + 0x10]
009E8FD7  41 0F 11 49 10                  movups xmmword ptr [r9 + 0x10], xmm1
009E8FDC  49 83 C1 20                     add r9, 0x20
009E8FE0  EB 95                           jmp 0x1409e8f77
009E8FE2  44 8B E7                        mov r12d, edi
009E8FE5  3B D7                           cmp edx, edi
009E8FE7  77 17                           ja 0x1409e9000
009E8FE9  8B C2                           mov eax, edx
009E8FEB  41 89 70 08                     mov dword ptr [r8 + 8], esi
009E8FEF  2B C3                           sub eax, ebx
009E8FF1  45 89 58 04                     mov dword ptr [r8 + 4], r11d
009E8FF5  41 89 00                        mov dword ptr [r8], eax
009E8FF8  41 C7 40 0C 02 00 00 00         mov dword ptr [r8 + 0xc], 2
009E9000  8B CA                           mov ecx, edx
009E9002  8D 42 10                        lea eax, [rdx + 0x10]
009E9005  49 03 CF                        add rcx, r15
009E9008  3B C2                           cmp eax, edx
009E900A  0F 82 73 FF FF FF               jb 0x1409e8f83
009E9010  8B D0                           mov edx, eax
009E9012  8D 58 20                        lea ebx, [rax + 0x20]
009E9015  49 03 D7                        add rdx, r15
009E9018  3B D8                           cmp ebx, eax
009E901A  0F 82 63 FF FF FF               jb 0x1409e8f83
009E9020  3B DF                           cmp ebx, edi
009E9022  0F 87 5E FE FF FF               ja 0x1409e8e86
009E9028  48 89 71 04                     mov qword ptr [rcx + 4], rsi
009E902C  89 31                           mov dword ptr [rcx], esi
009E902E  C7 41 0C 03 00 00 00            mov dword ptr [rcx + 0xc], 3
009E9035  0F B6 45 5B                     movzx eax, byte ptr [rbp + 0x5b]
009E9039  83 E0 01                        and eax, 1
009E903C  89 02                           mov dword ptr [rdx], eax
009E903E  F6 45 5B 01                     test byte ptr [rbp + 0x5b], 1
009E9042  0F 84 3E FE FF FF               je 0x1409e8e86
009E9048  C7 41 04 01 00 00 00            mov dword ptr [rcx + 4], 1
009E904F  48 8B CD                        mov rcx, rbp
009E9052  0F B6 45 5A                     movzx eax, byte ptr [rbp + 0x5a]
009E9056  88 42 04                        mov byte ptr [rdx + 4], al
009E9059  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
009E905D  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
009E9061  0F B7 45 58                     movzx eax, word ptr [rbp + 0x58]
009E9065  66 89 42 06                     mov word ptr [rdx + 6], ax
009E9069  E8 B2 A2 ED FF                  call 0x1408c3320
009E906E  45 89 37                        mov dword ptr [r15], r14d
009E9071  E9 1F FF FF FF                  jmp 0x1409e8f95
009E9076  8B D8                           mov ebx, eax
009E9078  3B 44 24 70                     cmp eax, dword ptr [rsp + 0x70]
009E907C  0F 87 F3 FC FF FF               ja 0x1409e8d75
009E9082  45 89 33                        mov dword ptr [r11], r14d
009E9085  0F B6 45 5A                     movzx eax, byte ptr [rbp + 0x5a]
009E9089  41 88 43 04                     mov byte ptr [r11 + 4], al
009E908D  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
009E9091  49 89 43 10                     mov qword ptr [r11 + 0x10], rax
009E9095  0F B7 45 58                     movzx eax, word ptr [rbp + 0x58]
009E9099  66 41 89 43 06                  mov word ptr [r11 + 6], ax
009E909E  48 8B 12                        mov rdx, qword ptr [rdx]
009E90A1  E9 0C FE FF FF                  jmp 0x1409e8eb2
009E90A6  48 8B CF                        mov rcx, rdi
009E90A9  E8 22 A8 87 FF                  call 0x1402638d0
009E90AE  E9 6F FE FF FF                  jmp 0x1409e8f22
009E90B3  B8 95 02 00 C0                  mov eax, 0xc0000295
009E90B8  E9 E4 FE FF FF                  jmp 0x1409e8fa1
009E90BD  0F B7 42 66                     movzx eax, word ptr [rdx + 0x66]
009E90C1  41 0F B6 C8                     movzx ecx, r8b
009E90C5  0F A3 C8                        bt eax, ecx
009E90C8  0F 83 38 FD FF FF               jae 0x1409e8e06
009E90CE  41 FF C6                        inc r14d
009E90D1  8D 43 20                        lea eax, [rbx + 0x20]
009E90D4  3B C3                           cmp eax, ebx
009E90D6  0F 82 40 FD FF FF               jb 0x1409e8e1c
009E90DC  8B D8                           mov ebx, eax
009E90DE  3B 44 24 70                     cmp eax, dword ptr [rsp + 0x70]
009E90E2  0F 87 1E FD FF FF               ja 0x1409e8e06
009E90E8  41 0F 10 02                     movups xmm0, xmmword ptr [r10]
009E90EC  41 0F 11 03                     movups xmmword ptr [r11], xmm0
009E90F0  41 0F 10 4A 10                  movups xmm1, xmmword ptr [r10 + 0x10]
009E90F5  41 0F 11 4B 10                  movups xmmword ptr [r11 + 0x10], xmm1
009E90FA  49 83 C3 20                     add r11, 0x20
009E90FE  E9 03 FD FF FF                  jmp 0x1409e8e06
009E9103  0F B7 42 64                     movzx eax, word ptr [rdx + 0x64]
009E9107  41 0F B6 C8                     movzx ecx, r8b
009E910B  0F A3 C8                        bt eax, ecx
009E910E  0F 83 DC FC FF FF               jae 0x1409e8df0
009E9114  41 FF C6                        inc r14d
009E9117  8D 43 20                        lea eax, [rbx + 0x20]
009E911A  3B C3                           cmp eax, ebx
009E911C  0F 82 FA FC FF FF               jb 0x1409e8e1c
009E9122  8B D8                           mov ebx, eax
009E9124  3B 44 24 70                     cmp eax, dword ptr [rsp + 0x70]
009E9128  0F 87 C2 FC FF FF               ja 0x1409e8df0
009E912E  41 0F 10 04 2A                  movups xmm0, xmmword ptr [r10 + rbp]
009E9133  41 0F 11 03                     movups xmmword ptr [r11], xmm0
009E9137  41 0F 10 4C 2A 10               movups xmm1, xmmword ptr [r10 + rbp + 0x10]
009E913D  41 0F 11 4B 10                  movups xmmword ptr [r11 + 0x10], xmm1
009E9142  49 83 C3 20                     add r11, 0x20
009E9146  E9 A5 FC FF FF                  jmp 0x1409e8df0
009E914B  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
009E9150  4D 8D 6F 18                     lea r13, [r15 + 0x18]
009E9154  BB 18 00 00 00                  mov ebx, 0x18
009E9159  4C 8D B5 98 11 00 00            lea r14, [rbp + 0x1198]
009E9160  45 8B E1                        mov r12d, r9d
009E9163  41 8B F1                        mov esi, r9d
009E9166  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
009E9170  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009E9179  41 B0 01                        mov r8b, 1
009E917C  48 8B CD                        mov rcx, rbp
009E917F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
009E9186  90                              nop
009E9187  41 0F B6 16                     movzx edx, byte ptr [r14]
009E918B  E8 90 97 F4 FF                  call 0x140932920
009E9190  4C 8B F8                        mov r15, rax
009E9193  48 85 C0                        test rax, rax
009E9196  75 44                           jne 0x1409e91dc
009E9198  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009E91A1  E8 4A 5E 87 FF                  call 0x14025eff0
009E91A6  FF C6                           inc esi
009E91A8  49 83 C6 02                     add r14, 2
009E91AC  83 FE 08                        cmp esi, 8
009E91AF  72 BF                           jb 0x1409e9170
009E91B1  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
009E91B9  45 33 C0                        xor r8d, r8d
009E91BC  44 89 40 08                     mov dword ptr [rax + 8], r8d
009E91C0  44 89 60 0C                     mov dword ptr [rax + 0xc], r12d
009E91C4  3B 5C 24 70                     cmp ebx, dword ptr [rsp + 0x70]
009E91C8  0F 87 D5 FC FF FF               ja 0x1409e8ea3
009E91CE  C7 00 01 00 00 00               mov dword ptr [rax], 1
009E91D4  41 8B F0                        mov esi, r8d
009E91D7  E9 B9 FD FF FF                  jmp 0x1409e8f95
009E91DC  8B D6                           mov edx, esi
009E91DE  4C 8D 44 24 28                  lea r8, [rsp + 0x28]
009E91E3  48 C1 E2 05                     shl rdx, 5
009E91E7  48 8B CF                        mov rcx, rdi
009E91EA  48 81 C2 CC 11 00 00            add rdx, 0x11cc
009E91F1  48 03 D5                        add rdx, rbp
009E91F4  E8 8B 88 A8 FF                  call 0x140471a84
009E91F9  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
009E91FE  4D 85 C0                        test r8, r8
009E9201  75 3F                           jne 0x1409e9242
009E9203  49 8D 8F 78 02 00 00            lea rcx, [r15 + 0x278]
009E920A  33 D2                           xor edx, edx
009E920C  E8 FF D5 9A FF                  call 0x140396810
009E9211  49 8B 87 50 05 00 00            mov rax, qword ptr [r15 + 0x550]
009E9218  BA 01 00 00 00                  mov edx, 1
009E921D  45 8B 07                        mov r8d, dword ptr [r15]
009E9220  48 8B 88 C0 02 00 00            mov rcx, qword ptr [rax + 0x2c0]
009E9227  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
009E922B  E8 20 5E 87 FF                  call 0x14025f050
009E9230  E9 63 FF FF FF                  jmp 0x1409e9198
009E9235  48 8B CF                        mov rcx, rdi
009E9238  E8 93 A6 87 FF                  call 0x1402638d0
009E923D  E9 24 FC FF FF                  jmp 0x1409e8e66
009E9242  41 FF C4                        inc r12d
009E9245  83 C3 20                        add ebx, 0x20
009E9248  3B 5C 24 70                     cmp ebx, dword ptr [rsp + 0x70]
009E924C  77 B5                           ja 0x1409e9203
009E924E  41 C7 45 00 01 00 00 00         mov dword ptr [r13], 1
009E9256  4D 89 45 10                     mov qword ptr [r13 + 0x10], r8
009E925A  41 0F B6 06                     movzx eax, byte ptr [r14]
009E925E  66 41 89 45 06                  mov word ptr [r13 + 6], ax
009E9263  49 83 C5 20                     add r13, 0x20
009E9267  EB 9A                           jmp 0x1409e9203
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009E8C24(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, unsigned int a14, __int64 a15, __int64 a16, __int64 a17)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p20;
    unsigned int v_stack_p24;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p90;

    v_stack_p78 = v_rdi;
loc_009E8C29:
    if (a2 >= 10) goto loc_009E8CB9;
    v_rdi = ((unsigned int)(a2)) + ((unsigned int)(a2));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1455920 + v_rdi * 8))) - (*(unsigned __int64 *)(v_rsi));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1455920 + v_rdi * 8) + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rsi + 8));
    }
    if (a1 != 0) goto loc_009E8CB2;
    a2 = 0;
    result = memset(v_r15, a2, v_r12, a4);
    if (((unsigned int)(v_r12)) < 24) goto loc_009E8EA3;
    a3 = 0;
    *(unsigned int *)(v_r15 + 12) = 0;
    *(unsigned int *)(v_r15) = 1;
    *(unsigned int *)(v_r15 + 20) = 1;
    *(unsigned int *)(v_r15 + 16) = 0;
    *(unsigned int *)(v_r15 + 8) = 0;
    goto loc_009E8F95;
loc_009E8CB2:
    a2 = (unsigned int)((a2) + 1);
    goto loc_009E8C29;
loc_009E8CB9:
    result = EtwpGetMetaProviderContext((unsigned int)((unsigned int)(v_r13)), a2, a3, a4);
    if (result != 0) goto loc_009E914B;
    a3 = 0;
    result = EtwpFindGuidEntryByGuid(v_rbp, (unsigned int)((unsigned int)(v_r13)), a3, a4);
    if (result == 0) goto loc_009E90B3;
    a2 = 0;
    result = memset(v_r15, a2, (unsigned int)(*(unsigned int *)(a17)), a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 664, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = result + 664;
        a2 = result;
        a1 = result + 664;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_r10 = 0;
    *(unsigned __int64 *)(result + 672) = *(unsigned __int64 *)(gs_base + (0 + 392));
    goto loc_009E8D87;
loc_009E8D68:
    if (((*(unsigned __int8 *)(result + 91)) & (1)) != 0) goto loc_009E8E0B;
loc_009E8D75:
    if (24 <= a14) goto loc_009E8EAD;
loc_009E8D82:
loc_009E8D87:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56))) == (result + 56)) goto loc_009E8EE8;
    a4 = (24) + (v_r15);
    v_rdi = 0;
    if (((unsigned int)(24 + 16)) < 24) goto loc_009E8E1C;
    v_r13 = (unsigned int)(((unsigned int)(v_stack_p24)) + 1);
    v_r11 = ((unsigned int)((unsigned int)(24 + 16))) + (v_r15);
    v_stack_p24 = (unsigned int)(v_r13);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56)) + 98)) & (8)) != 0) goto loc_009E8D68;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56)) + 100)) != 0) goto loc_009E8DCD;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56)) + 102)) == 0) goto loc_009E8D75;
loc_009E8DCD:
loc_009E8DD0:
    v_r10 = (0) + (4);
    v_r10 = (v_r10) << (5);
    if ((*(unsigned int *)(v_r10 + result * 1)) != 0) goto loc_009E9103;
loc_009E8DF0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56)) + 40) == 0) goto loc_009E8E06;
    v_r10 = (v_r10) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56)) + 40));
    if ((*(unsigned int *)(v_r10)) != 0) goto loc_009E90BD;
loc_009E8E06:
    a3 = (unsigned int)((0) + 1);
    goto loc_009E8DD0;
loc_009E8E0B:
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56)) + 40)) + (32));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)((unsigned int)(24 + 16))))) goto loc_009E9076;
loc_009E8E1C:
    a3 = 0;
    v_stack_p20 = 0x80000005ULL;
    *(unsigned __int64 *)(result + 672) = 0;
    a1 = (*(unsigned __int64 *)(result + 664)) & (-16);
    a2 = *(unsigned __int64 *)(result + 664) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 664))) & (2)) != 0) goto loc_009E9235;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 664))) & (2)) != 0) goto loc_009E9235;
loc_009E8E66:
    result = KeAbPostRelease(result + 664, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
loc_009E8E86:
    result = EtwpUnreferenceGuidEntry(result, a2, a3, a4);
    if (sign_flag) goto loc_009E8F95;
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) <= ((unsigned int)((unsigned int)(a14)))) goto loc_009E906E;
loc_009E8EA3:
    goto loc_009E8F95;
loc_009E8EAD:
    if ((unsigned __int8)(result + 664) != 0) {
        *(unsigned int *)(a4 + 12) = 1;
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56)) + 98)) & (2)) == 0) goto loc_009E8F7B;
loc_009E8ECF:
    *(unsigned int *)(a4 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56)) + 80) + 464)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) - ((unsigned int)((unsigned int)(a14))));
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(v_stack_p24));
    *(unsigned int *)(a4) = (unsigned int)(result);
    if (a2 != ((unsigned int)(0xC0000023ULL))) goto loc_009E8D82;
loc_009E8EE8:
    *(unsigned __int64 *)(result + 672) = v_r10;
    a1 = (*(unsigned __int64 *)(result + 664)) & (-16);
    a2 = *(unsigned __int64 *)(result + 664) - 16;
    if (a1 <= 16) { a2 = v_r10; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 664))) & (2)) != 0) goto loc_009E90A6;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 664))) & (2)) != 0) goto loc_009E90A6;
loc_009E8F22:
    result = KeAbPostRelease(result + 664, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_r14 = (unsigned int)(((unsigned int)(v_stack_p24)) + (2));
    a3 = ((unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) + (v_r15);
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL) + 16)) < ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_009E8F83;
    a4 = ((unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL) + 16))) + (v_r15);
    v_rsi = 0;
loc_009E8F63:
    if (0 >= 16) goto loc_009E8FE2;
    result = (0) + (4);
    result = (result) << (5);
    if ((*(unsigned int *)(result + result * 1)) != 0) goto loc_009E8FB7;
loc_009E8F77:
    a1 = (unsigned int)((0) + 1);
    goto loc_009E8F63;
loc_009E8F7B:
    goto loc_009E8ECF;
loc_009E8F83:
    result = EtwpUnreferenceGuidEntry(result, (unsigned int)(0xFFFFFFFFULL) + 16, a3, a4);
loc_009E8F95:
    *(unsigned int *)(a17) = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
loc_009E8FA1:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0x80000005ULL)));
loc_009E8FB7:
    v_r11 = (unsigned int)((0) + 1);
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL) + 16 + 32)) < ((unsigned int)((unsigned int)(0xFFFFFFFFULL) + 16))) goto loc_009E8F83;
    a2 = (unsigned int)(((unsigned int)(0xFFFFFFFFULL) + 16) + (32));
    v_r10 = (unsigned int)(((unsigned int)(0xFFFFFFFFULL) + 16 + 32) + (32));
    if (a2 > ((unsigned int)(a15))) goto loc_009E8F77;
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned __int64 *)(a4 + 16) = v_xmm1;
    a4 = (a4) + (32);
    goto loc_009E8F77;
loc_009E8FE2:
    result = (unsigned int)((unsigned int)((unsigned int)(0x80000005ULL)));
    if (a2 <= ((unsigned int)(a15))) {
        result = a2;
        *(unsigned int *)(a3 + 8) = (unsigned int)((unsigned int)(0x80000005ULL));
        result = (unsigned int)((result) - ((unsigned int)((unsigned int)(0xFFFFFFFFULL))));
        *(unsigned int *)(a3 + 4) = (unsigned int)(v_r11);
        *(unsigned int *)(a3) = (unsigned int)(result);
        *(unsigned int *)(a3 + 12) = 2;
    }
    a1 = ((unsigned int)(a2)) + (v_r15);
    if (((unsigned int)(a2 + 16)) < a2) goto loc_009E8F83;
    a2 = ((unsigned int)((unsigned int)(a2 + 16))) + (v_r15);
    if (((unsigned int)(a2 + 16 + 32)) < ((unsigned int)(a2 + 16))) goto loc_009E8F83;
    if (((unsigned int)(a2 + 16 + 32)) > ((unsigned int)(a15))) goto loc_009E8E86;
    *(unsigned __int64 *)(a1 + 4) = (unsigned int)(0x80000005ULL);
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(0x80000005ULL));
    *(unsigned int *)(a1 + 12) = 3;
    result = (unsigned int)((*(unsigned __int8 *)(result + 91)) & (1));
    *(unsigned int *)(a2) = (unsigned int)(result);
    if (((*(unsigned __int8 *)(result + 91)) & (1)) == 0) goto loc_009E8E86;
    *(unsigned int *)(a1 + 4) = 1;
    *(unsigned __int8 *)(a2 + 4) = (unsigned __int8)(*(unsigned __int8 *)(result + 90));
    *(unsigned __int64 *)(a2 + 16) = *(unsigned __int64 *)(result + 80);
    *(unsigned __int16 *)(a2 + 6) = (unsigned __int16)(*(unsigned __int16 *)(result + 88));
    result = EtwpUnreferenceGuidEntry(result, a2, a3, a4);
loc_009E906E:
    *(unsigned int *)(v_r15) = (unsigned int)(v_r14);
    goto loc_009E8F95;
loc_009E9076:
    if (((unsigned int)(result)) > a14) goto loc_009E8D75;
    *(unsigned int *)(v_r11) = (unsigned int)(v_r14);
    *(unsigned __int8 *)(v_r11 + 4) = (unsigned __int8)(*(unsigned __int8 *)(result + 90));
    *(unsigned __int64 *)(v_r11 + 16) = *(unsigned __int64 *)(result + 80);
    *(unsigned __int16 *)(v_r11 + 6) = (unsigned __int16)(*(unsigned __int16 *)(result + 88));
    goto loc_009E8EB2;
loc_009E90A6:
    result = ExfReleasePushLock(a15, *(unsigned __int64 *)(a2), a3, a4);
    goto loc_009E8F22;
loc_009E90B3:
    goto loc_009E8FA1;
loc_009E90BD:
    if (((unsigned int)(result)) >= a14) goto loc_009E8E06;
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((unsigned int)((unsigned int)((unsigned int)(result)) + 32)) < ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_009E8E1C;
    if (((unsigned int)((unsigned int)((unsigned int)(result)) + 32)) > a14) goto loc_009E8E06;
    *(unsigned __int64 *)(v_r11) = v_xmm0;
    *(unsigned __int64 *)(v_r11 + 16) = v_xmm1;
    v_r11 = (v_r11) + (32);
    goto loc_009E8E06;
loc_009E9103:
    if (condition_is_above_or_equal) goto loc_009E8DF0;
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)) + 32)) + 32)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)) + 32))))) goto loc_009E8E1C;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)) + 32)) + 32)) > a14) goto loc_009E8DF0;
    *(unsigned __int64 *)(v_r11) = v_xmm0;
    *(unsigned __int64 *)(v_r11 + 16) = v_xmm1;
    v_r11 = (v_r11) + (32);
    goto loc_009E8DF0;
loc_009E914B:
    v_stack_p90 = a4;
loc_009E9170:
    result = EtwpAcquireLoggerContextByLoggerId(result, *(unsigned __int8 *)(result + 4504), 1, a4);
    if (result != 0) goto loc_009E91DC;
loc_009E9198:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int8 *)(result + 4504), 1, a4);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a4))) + 1);
    v_r14 = (result + 4504) + (2);
    if (((unsigned int)(v_rsi)) < 8) goto loc_009E9170;
    a3 = 0;
    *(unsigned int *)(a16 + 8) = 0;
    *(unsigned int *)(a16 + 12) = (unsigned int)((unsigned int)((unsigned int)(a4)));
    if (24 > a14) goto loc_009E8EA3;
    *(unsigned int *)(a16) = 1;
    goto loc_009E8F95;
loc_009E91DC:
    a2 = (0) << (5);
    a2 = (a2) + (0x11CCULL);
    a2 = (a2) + (result);
    result = EtwpMapMetaProviderKeywords(a15, a2, a5, a4);
    if (a5 != 0) goto loc_009E9242;
loc_009E9203:
    a2 = 0;
    result = KeReleaseMutex(result + 632, a2, a5, a4);
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1360) + 704) + (unsigned int)(*(unsigned int *)(result)) * 8), 1, (unsigned int)(*(unsigned int *)(result)), a4);
    goto loc_009E9198;
loc_009E9235:
    result = ExfReleasePushLock(a15, 1, (unsigned int)(*(unsigned int *)(result)), a4);
    goto loc_009E8E66;
loc_009E9242:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(a4))) + 1);
    v_rbx = (unsigned int)((24) + (32));
    if (((unsigned int)(v_rbx)) > a14) goto loc_009E9203;
    *(unsigned int *)(v_r15 + 24) = 1;
    *(unsigned __int64 *)(v_r15 + 24 + 16) = (unsigned int)(*(unsigned int *)(result));
    *(unsigned __int16 *)(v_r15 + 24 + 6) = (unsigned __int16)(*(unsigned __int8 *)(v_r14));
    v_r13 = (v_r15 + 24) + (32);
    goto loc_009E9203;
}
```

## 5. (Beta) C Style

```c
int64_t sub_009E8C24(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint32_t Arg14, int64_t Arg15, void *Arg16, void *Arg17)
{
    uint8_t *arg16 = (uint8_t *)Arg16;
    uint8_t *arg17 = (uint8_t *)Arg17;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p20;
    uint32_t v_stack_p24;
    uint64_t v_stack_p78;
    uint64_t v_stack_p90;

    v_stack_p78 = local_rdi;
loc_009E8C29:
    if (Arg2 >= 10) goto loc_009E8CB9;
    local_rdi = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x163730 + local_rdi * 8))) - (*(uint64_t *)(local_rsi));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x163730 + local_rdi * 8) + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(local_rsi + 0x8));
    }
    if (Arg1 != 0) goto loc_009E8CB2;
    Arg2 = 0;
    result = memset(local_r15, Arg2, local_r12, Arg4);
    if (((uint32_t)(local_r12)) < 24) goto loc_009E8EA3;
    Arg3 = 0;
    *(uint32_t *)(local_r15 + 0xC) = 0;
    *(uint32_t *)(local_r15) = 1;
    *(uint32_t *)(local_r15 + 0x14) = 1;
    *(uint32_t *)(local_r15 + 0x10) = 0;
    *(uint32_t *)(local_r15 + 0x8) = 0;
    goto loc_009E8F95;
loc_009E8CB2:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_009E8C29;
loc_009E8CB9:
    result = EtwpGetMetaProviderContext((uint32_t)((uint32_t)(local_r13)), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_009E914B;
    Arg3 = 0;
    result = EtwpFindGuidEntryByGuid(local_rbp, (uint32_t)((uint32_t)(local_r13)), Arg3, Arg4);
    if (result == 0) goto loc_009E90B3;
    Arg2 = 0;
    result = memset(local_r15, Arg2, (uint32_t)(*(uint32_t *)(arg17)), Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 664, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 664;
        Arg2 = result;
        Arg1 = result + 664;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_r10 = 0;
    *(uint64_t *)(result + 0x2A0) = *(uint64_t *)(gs_base + (0 + 0x188));
    goto loc_009E8D87;
loc_009E8D68:
    if (((*(uint8_t *)(result + 0x5B)) & (1)) != 0) goto loc_009E8E0B;
loc_009E8D75:
    if (24 <= Arg14) goto loc_009E8EAD;
loc_009E8D82:
loc_009E8D87:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x38))) == (result + 56)) goto loc_009E8EE8;
    Arg4 = (24) + (local_r15);
    local_rdi = 0;
    if (((uint32_t)(24 + 16)) < 24) goto loc_009E8E1C;
    local_r13 = (uint32_t)(((uint32_t)(v_stack_p24)) + 1);
    local_r11 = ((uint32_t)((uint32_t)(24 + 16))) + (local_r15);
    v_stack_p24 = (uint32_t)(local_r13);
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x38)) + 0x62)) & (8)) != 0) goto loc_009E8D68;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x38)) + 0x64)) != 0) goto loc_009E8DCD;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x38)) + 0x66)) == 0) goto loc_009E8D75;
loc_009E8DCD:
loc_009E8DD0:
    local_r10 = (0) + (4);
    local_r10 = (local_r10) << (5);
    if ((*(uint32_t *)(local_r10 + result * 1)) != 0) goto loc_009E9103;
loc_009E8DF0:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x38)) + 0x28) == 0) goto loc_009E8E06;
    local_r10 = (local_r10) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x38)) + 0x28));
    if ((*(uint32_t *)(local_r10)) != 0) goto loc_009E90BD;
loc_009E8E06:
    Arg3 = (uint32_t)((0) + 1);
    goto loc_009E8DD0;
loc_009E8E0B:
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x38)) + 0x28)) + (32));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)((uint32_t)(24 + 16))))) goto loc_009E9076;
loc_009E8E1C:
    Arg3 = 0;
    v_stack_p20 = 0x80000005ULL;
    *(uint64_t *)(result + 0x2A0) = 0;
    Arg1 = (*(uint64_t *)(result + 0x298)) & (-16);
    Arg2 = *(uint64_t *)(result + 0x298) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(result + 0x298))) & (2)) != 0) goto loc_009E9235;
    if ((((uint8_t)(*(uint64_t *)(result + 0x298))) & (2)) != 0) goto loc_009E9235;
loc_009E8E66:
    result = KeAbPostRelease(result + 664, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
loc_009E8E86:
    result = EtwpUnreferenceGuidEntry(result, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_009E8F95;
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) <= ((uint32_t)((uint32_t)(Arg14)))) goto loc_009E906E;
loc_009E8EA3:
    goto loc_009E8F95;
loc_009E8EAD:
    if ((uint8_t)(result + 664) != 0) {
        *(uint32_t *)(Arg4 + 0xC) = 1;
    }
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x38)) + 0x62)) & (2)) == 0) goto loc_009E8F7B;
loc_009E8ECF:
    *(uint32_t *)(Arg4 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x38)) + 0x50) + 0x1D0)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) - ((uint32_t)((uint32_t)(Arg14))));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(v_stack_p24));
    *(uint32_t *)(Arg4) = (uint32_t)(result);
    if (Arg2 != ((uint32_t)(0xC0000023ULL))) goto loc_009E8D82;
loc_009E8EE8:
    *(uint64_t *)(result + 0x2A0) = local_r10;
    Arg1 = (*(uint64_t *)(result + 0x298)) & (-16);
    Arg2 = *(uint64_t *)(result + 0x298) - 16;
    if (Arg1 <= 16) { Arg2 = local_r10; }
    if ((((uint8_t)(*(uint64_t *)(result + 0x298))) & (2)) != 0) goto loc_009E90A6;
    if ((((uint8_t)(*(uint64_t *)(result + 0x298))) & (2)) != 0) goto loc_009E90A6;
loc_009E8F22:
    result = KeAbPostRelease(result + 664, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    local_r14 = (uint32_t)(((uint32_t)(v_stack_p24)) + (2));
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) + (local_r15);
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL) + 16)) < ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_009E8F83;
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL) + 16))) + (local_r15);
    local_rsi = 0;
loc_009E8F63:
    if (0 >= 16) goto loc_009E8FE2;
    result = (0) + (4);
    result = (result) << (5);
    if ((*(uint32_t *)(result + result * 1)) != 0) goto loc_009E8FB7;
loc_009E8F77:
    Arg1 = (uint32_t)((0) + 1);
    goto loc_009E8F63;
loc_009E8F7B:
    goto loc_009E8ECF;
loc_009E8F83:
    result = EtwpUnreferenceGuidEntry(result, (uint32_t)(0xFFFFFFFFULL) + 16, Arg3, Arg4);
loc_009E8F95:
    *(uint32_t *)(arg17) = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
loc_009E8FA1:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)(0x80000005ULL)));
loc_009E8FB7:
    local_r11 = (uint32_t)((0) + 1);
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL) + 16 + 32)) < ((uint32_t)((uint32_t)(0xFFFFFFFFULL) + 16))) goto loc_009E8F83;
    Arg2 = (uint32_t)(((uint32_t)(0xFFFFFFFFULL) + 16) + (32));
    local_r10 = (uint32_t)(((uint32_t)(0xFFFFFFFFULL) + 16 + 32) + (32));
    if (Arg2 > ((uint32_t)(Arg15))) goto loc_009E8F77;
    *(uint64_t *)(Arg4) = v_xmm0;
    *(uint64_t *)(Arg4 + 0x10) = v_xmm1;
    Arg4 = (Arg4) + (32);
    goto loc_009E8F77;
loc_009E8FE2:
    result = (uint32_t)((uint32_t)((uint32_t)(0x80000005ULL)));
    if (Arg2 <= ((uint32_t)(Arg15))) {
        result = Arg2;
        *(uint32_t *)(Arg3 + 0x8) = (uint32_t)((uint32_t)(0x80000005ULL));
        result = (uint32_t)((result) - ((uint32_t)((uint32_t)(0xFFFFFFFFULL))));
        *(uint32_t *)(Arg3 + 0x4) = (uint32_t)(local_r11);
        *(uint32_t *)(Arg3) = (uint32_t)(result);
        *(uint32_t *)(Arg3 + 0xC) = 2;
    }
    Arg1 = ((uint32_t)(Arg2)) + (local_r15);
    if (((uint32_t)(Arg2 + 16)) < Arg2) goto loc_009E8F83;
    Arg2 = ((uint32_t)((uint32_t)(Arg2 + 16))) + (local_r15);
    if (((uint32_t)(Arg2 + 16 + 32)) < ((uint32_t)(Arg2 + 16))) goto loc_009E8F83;
    if (((uint32_t)(Arg2 + 16 + 32)) > ((uint32_t)(Arg15))) goto loc_009E8E86;
    *(uint64_t *)(Arg1 + 0x4) = (uint32_t)(0x80000005ULL);
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(0x80000005ULL));
    *(uint32_t *)(Arg1 + 0xC) = 3;
    result = (uint32_t)((*(uint8_t *)(result + 0x5B)) & (1));
    *(uint32_t *)(Arg2) = (uint32_t)(result);
    if (((*(uint8_t *)(result + 0x5B)) & (1)) == 0) goto loc_009E8E86;
    *(uint32_t *)(Arg1 + 0x4) = 1;
    *(uint8_t *)(Arg2 + 0x4) = (uint8_t)(*(uint8_t *)(result + 0x5A));
    *(uint64_t *)(Arg2 + 0x10) = *(uint64_t *)(result + 0x50);
    *(uint16_t *)(Arg2 + 0x6) = (uint16_t)(*(uint16_t *)(result + 0x58));
    result = EtwpUnreferenceGuidEntry(result, Arg2, Arg3, Arg4);
loc_009E906E:
    *(uint32_t *)(local_r15) = (uint32_t)(local_r14);
    goto loc_009E8F95;
loc_009E9076:
    if (((uint32_t)(result)) > Arg14) goto loc_009E8D75;
    *(uint32_t *)(local_r11) = (uint32_t)(local_r14);
    *(uint8_t *)(local_r11 + 0x4) = (uint8_t)(*(uint8_t *)(result + 0x5A));
    *(uint64_t *)(local_r11 + 0x10) = *(uint64_t *)(result + 0x50);
    *(uint16_t *)(local_r11 + 0x6) = (uint16_t)(*(uint16_t *)(result + 0x58));
    goto loc_009E8EB2;
loc_009E90A6:
    result = ExfReleasePushLock(Arg15, *(uint64_t *)(Arg2), Arg3, Arg4);
    goto loc_009E8F22;
loc_009E90B3:
    goto loc_009E8FA1;
loc_009E90BD:
    if (((uint32_t)(result)) >= Arg14) goto loc_009E8E06;
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((uint32_t)((uint32_t)((uint32_t)(result)) + 32)) < ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_009E8E1C;
    if (((uint32_t)((uint32_t)((uint32_t)(result)) + 32)) > Arg14) goto loc_009E8E06;
    *(uint64_t *)(local_r11) = v_xmm0;
    *(uint64_t *)(local_r11 + 0x10) = v_xmm1;
    local_r11 = (local_r11) + (32);
    goto loc_009E8E06;
loc_009E9103:
    if (condition_is_above_or_equal) goto loc_009E8DF0;
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)) + 32)) + 32)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)) + 32))))) goto loc_009E8E1C;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)) + 32)) + 32)) > Arg14) goto loc_009E8DF0;
    *(uint64_t *)(local_r11) = v_xmm0;
    *(uint64_t *)(local_r11 + 0x10) = v_xmm1;
    local_r11 = (local_r11) + (32);
    goto loc_009E8DF0;
loc_009E914B:
    v_stack_p90 = Arg4;
loc_009E9170:
    result = EtwpAcquireLoggerContextByLoggerId(result, *(uint8_t *)(result + 0x1198), 1, Arg4);
    if (result != 0) goto loc_009E91DC;
loc_009E9198:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint8_t *)(result + 0x1198), 1, Arg4);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) + 1);
    local_r14 = (result + 4504) + (2);
    if (((uint32_t)(local_rsi)) < 8) goto loc_009E9170;
    Arg3 = 0;
    *(uint32_t *)(arg16 + 0x8) = 0;
    *(uint32_t *)(arg16 + 0xC) = (uint32_t)((uint32_t)((uint32_t)(Arg4)));
    if (24 > Arg14) goto loc_009E8EA3;
    *(uint32_t *)(arg16) = 1;
    goto loc_009E8F95;
loc_009E91DC:
    Arg2 = (0) << (5);
    Arg2 = (Arg2) + (0x11CCULL);
    Arg2 = (Arg2) + (result);
    result = EtwpMapMetaProviderKeywords(Arg15, Arg2, Arg5, Arg4);
    if (Arg5 != 0) goto loc_009E9242;
loc_009E9203:
    Arg2 = 0;
    result = KeReleaseMutex(result + 632, Arg2, Arg5, Arg4);
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x550) + 0x2C0) + (uint32_t)(*(uint32_t *)(result)) * 8), 1, (uint32_t)(*(uint32_t *)(result)), Arg4);
    goto loc_009E9198;
loc_009E9235:
    result = ExfReleasePushLock(Arg15, 1, (uint32_t)(*(uint32_t *)(result)), Arg4);
    goto loc_009E8E66;
loc_009E9242:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) + 1);
    local_rbx = (uint32_t)((24) + (32));
    if (((uint32_t)(local_rbx)) > Arg14) goto loc_009E9203;
    *(uint32_t *)(local_r15 + 0x18) = 1;
    *(uint64_t *)(local_r15 + 0x18 + 0x10) = (uint32_t)(*(uint32_t *)(result));
    *(uint16_t *)(local_r15 + 0x18 + 0x6) = (uint16_t)(*(uint8_t *)(local_r14));
    local_r13 = (local_r15 + 24) + (32);
    goto loc_009E9203;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg16` | `+ 0x0` | `32` | `W` |
| `Arg16` | `+ 0x8` | `32` | `W` |
| `Arg16` | `+ 0xC` | `32` | `W` |
| `Arg17` | `+ 0x0` | `32` | `R` |
| `Arg17` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E8C24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
