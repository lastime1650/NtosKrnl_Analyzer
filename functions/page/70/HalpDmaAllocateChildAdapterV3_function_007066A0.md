# HalpDmaAllocateChildAdapterV3

- RVA: `0x007066A0`–`0x00706E29` (길이 `1,929` bytes)
- VA: `0x00000001407066A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C394C`
- 디코드: `462`개 명령, `1,929/1,929` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00706711` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0070671E` → [HalpIommuGetSecurityPolicy](../../text/4F/HalpIommuGetSecurityPolicy_function_004FC720.md) (function, `0x004FC720`)
- `0x007067A5` → [HalpDmaGetIommuInterface](../../text/53/HalpDmaGetIommuInterface_function_0053E2A0.md) (function, `0x0053E2A0`)
- `0x007067C5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0070683F` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x00706859` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00706872` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x0070689D` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x007068AE` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00706944` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0070695A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0070696B` → [HalpDmaIsThinDmarCapable](../../text/4D/HalpDmaIsThinDmarCapable_function_004DC54C.md) (function, `0x004DC54C`)
- `0x00706A5B` → [HalpDmaAllocateLocalScatterPool](HalpDmaAllocateLocalScatterPool_function_007091D4.md) (function, `0x007091D4`)
- `0x00706A62` → [HalpDmaAllocateLocalContiguousPool](HalpDmaAllocateLocalContiguousPool_function_00708EE4.md) (function, `0x00708EE4`)
- `0x00706AE3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00706AF1` → [IidCloneDeviceId](../82/IidCloneDeviceId_function_008289F8.md) (function, `0x008289F8`)
- `0x00706B38` → [HalpIommuCheckExceptionList](../../text/4C/HalpIommuCheckExceptionList_function_004CFD84.md) (function, `0x004CFD84`)
- `0x00706B45` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00706B5B` → [HalpDmaGetDefaultRemappingDomainPolicy](../../text/53/HalpDmaGetDefaultRemappingDomainPolicy_function_0053E240.md) (function, `0x0053E240`)
- `0x00706BB8` → [HalpDmaFindAdapterByDeviceId](../../text/53/HalpDmaFindAdapterByDeviceId_function_0053E0CC.md) (function, `0x0053E0CC`)
- `0x00706BDD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00706BF6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00706C1C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00706C39` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00706CC3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00706CCA` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (function, `0x004F7B90`)
- `0x00706D0C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00706D4B` → [HalJoinDmaDomain](../../text/4E/HalJoinDmaDomain_function_004E3320.md) (function, `0x004E3320`)
- `0x00706D7E` → [HalJoinDmaDomain](../../text/4E/HalJoinDmaDomain_function_004E3320.md) (function, `0x004E3320`)
- `0x00706D8A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00706DDE` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00706DE6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00706DEE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00706DFD` → [HalpDmaIsThinDmaCapable](../../text/55/HalpDmaIsThinDmaCapable_function_00552B80.md) (function, `0x00552B80`)

### Direct callers
- [HalGetAdapterV3](HalGetAdapterV3_function_00709838.md) at `0x00709BF5`

### Static image references
- `0x00706822` → RVA `0x00FC6D38` (`ALMOSTRO`; read)
- `0x007068BA` → RVA `0x00007280` (`.rdata`; read)
- `0x007068C8` → RVA `0x00FC3C20` (`.data`; read)
- `0x007068F0` → RVA `0x00FC3D20` (`.data`; read)
- `0x00706978` → RVA `0x00007500` (`.rdata`; read)
- `0x00706A24` → RVA `0x00550650` (`IoFreeAdapterChannelV3Passive`; read)
- `0x00706C29` → RVA `0x00E00C98` (`.data`; read)
- `0x00706C61` → RVA `0x00FC3F78` (`.data`; read)
- `0x00706CA0` → RVA `0x00FC1778` (`.data`; read)
- `0x00706E06` → RVA `0x000073C0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **29**
  - `0x00706711` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0070671E` → [HalpIommuGetSecurityPolicy](../../text/4F/HalpIommuGetSecurityPolicy_function_004FC720.md) (`PAGE` → `.text`)
  - `0x007067A5` → [HalpDmaGetIommuInterface](../../text/53/HalpDmaGetIommuInterface_function_0053E2A0.md) (`PAGE` → `.text`)
  - `0x007067C5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00706859` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00706872` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x007068AE` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00706944` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0070695A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0070696B` → [HalpDmaIsThinDmarCapable](../../text/4D/HalpDmaIsThinDmarCapable_function_004DC54C.md) (`PAGE` → `.text`)
  - `0x00706AE3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00706B38` → [HalpIommuCheckExceptionList](../../text/4C/HalpIommuCheckExceptionList_function_004CFD84.md) (`PAGE` → `.text`)
  - `0x00706B45` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (`PAGE` → `.text`)
  - `0x00706B5B` → [HalpDmaGetDefaultRemappingDomainPolicy](../../text/53/HalpDmaGetDefaultRemappingDomainPolicy_function_0053E240.md) (`PAGE` → `.text`)
  - `0x00706BB8` → [HalpDmaFindAdapterByDeviceId](../../text/53/HalpDmaFindAdapterByDeviceId_function_0053E0CC.md) (`PAGE` → `.text`)
  - `0x00706BDD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00706BF6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00706C1C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00706C39` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00706CC3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00706CCA` → [Feature_Test57481295__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test57481295__private_IsEnabledDeviceUsageNoInline_function_004F7B90.md) (`PAGE` → `.text`)
  - `0x00706D0C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00706D4B` → [HalJoinDmaDomain](../../text/4E/HalJoinDmaDomain_function_004E3320.md) (`PAGE` → `.text`)
  - `0x00706D7E` → [HalJoinDmaDomain](../../text/4E/HalJoinDmaDomain_function_004E3320.md) (`PAGE` → `.text`)
  - `0x00706D8A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00706DDE` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00706DE6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00706DEE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00706DFD` → [HalpDmaIsThinDmaCapable](../../text/55/HalpDmaIsThinDmaCapable_function_00552B80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007066A0  48 8B C4                        mov rax, rsp
007066A3  44 88 48 20                     mov byte ptr [rax + 0x20], r9b
007066A7  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
007066AB  89 50 10                        mov dword ptr [rax + 0x10], edx
007066AE  89 48 08                        mov dword ptr [rax + 8], ecx
007066B1  55                              push rbp
007066B2  53                              push rbx
007066B3  56                              push rsi
007066B4  57                              push rdi
007066B5  41 54                           push r12
007066B7  41 55                           push r13
007066B9  41 56                           push r14
007066BB  41 57                           push r15
007066BD  48 8D 68 98                     lea rbp, [rax - 0x68]
007066C1  48 81 EC 28 01 00 00            sub rsp, 0x128
007066C8  33 FF                           xor edi, edi
007066CA  48 C7 45 A0 30 00 00 00         mov qword ptr [rbp - 0x60], 0x30
007066D2  0F 57 C0                        xorps xmm0, xmm0
007066D5  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
007066D9  33 D2                           xor edx, edx
007066DB  48 C7 45 B8 10 02 00 00         mov qword ptr [rbp - 0x48], 0x210
007066E3  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007066E7  40 88 BD C8 00 00 00            mov byte ptr [rbp + 0xc8], dil
007066EE  44 8D 47 50                     lea r8d, [rdi + 0x50]
007066F2  40 88 7C 24 50                  mov byte ptr [rsp + 0x50], dil
007066F7  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
007066FC  44 8B F7                        mov r14d, edi
007066FF  44 8A FF                        mov r15b, dil
00706702  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
00706706  8B F7                           mov esi, edi
00706708  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
0070670D  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
00706711  E8 2A 05 FC FF                  call 0x1406c6c40
00706716  C7 44 24 60 02 00 00 00         mov dword ptr [rsp + 0x60], 2
0070671E  E8 FD 5F DF FF                  call 0x1404fc720
00706723  0F 57 C0                        xorps xmm0, xmm0
00706726  B9 88 02 00 00                  mov ecx, 0x288
0070672B  8B D9                           mov ebx, ecx
0070672D  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00706731  44 8B EF                        mov r13d, edi
00706734  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
00706738  F3 0F 7F 45 C0                  movdqu xmmword ptr [rbp - 0x40], xmm0
0070673D  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
00706741  40 38 BD 90 00 00 00            cmp byte ptr [rbp + 0x90], dil
00706748  75 1A                           jne 0x140706764
0070674A  8B 85 A8 00 00 00               mov eax, dword ptr [rbp + 0xa8]
00706750  FF C0                           inc eax
00706752  44 8D 2C 40                     lea r13d, [rax + rax*2]
00706756  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0070675A  41 C1 E5 03                     shl r13d, 3
0070675E  41 8B DD                        mov ebx, r13d
00706761  48 03 D9                        add rbx, rcx
00706764  4C 8B A5 C0 00 00 00            mov r12, qword ptr [rbp + 0xc0]
0070676B  B9 01 00 00 00                  mov ecx, 1
00706770  8B BD B8 00 00 00               mov edi, dword ptr [rbp + 0xb8]
00706776  4D 85 E4                        test r12, r12
00706779  75 15                           jne 0x140706790
0070677B  85 FF                           test edi, edi
0070677D  74 11                           je 0x140706790
0070677F  83 FF 02                        cmp edi, 2
00706782  75 04                           jne 0x140706788
00706784  33 FF                           xor edi, edi
00706786  EB 08                           jmp 0x140706790
00706788  3B C1                           cmp eax, ecx
0070678A  0F 84 81 06 00 00               je 0x140706e11
00706790  48 21 74 24 58                  and qword ptr [rsp + 0x58], rsi
00706795  85 FF                           test edi, edi
00706797  74 76                           je 0x14070680f
00706799  4D 85 E4                        test r12, r12
0070679C  74 71                           je 0x14070680f
0070679E  48 8D 55 D0                     lea rdx, [rbp - 0x30]
007067A2  49 8B CC                        mov rcx, r12
007067A5  E8 F6 7A E3 FF                  call 0x14053e2a0
007067AA  85 C0                           test eax, eax
007067AC  78 49                           js 0x1407067f7
007067AE  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
007067B2  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
007067B7  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
007067BB  45 33 C0                        xor r8d, r8d
007067BE  33 D2                           xor edx, edx
007067C0  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
007067C5  E8 06 43 FB FF                  call 0x1406baad0
007067CA  3D 23 00 00 C0                  cmp eax, 0xc0000023
007067CF  75 07                           jne 0x1407067d8
007067D1  48 39 74 24 58                  cmp qword ptr [rsp + 0x58], rsi
007067D6  75 37                           jne 0x14070680f
007067D8  83 FF 02                        cmp edi, 2
007067DB  75 04                           jne 0x1407067e1
007067DD  33 FF                           xor edi, edi
007067DF  EB 0F                           jmp 0x1407067f0
007067E1  B8 01 00 00 00                  mov eax, 1
007067E6  39 44 24 54                     cmp dword ptr [rsp + 0x54], eax
007067EA  0F 84 62 01 00 00               je 0x140706952
007067F0  48 21 74 24 58                  and qword ptr [rsp + 0x58], rsi
007067F5  EB 18                           jmp 0x14070680f
007067F7  83 FF 02                        cmp edi, 2
007067FA  75 04                           jne 0x140706800
007067FC  33 FF                           xor edi, edi
007067FE  EB 0F                           jmp 0x14070680f
00706800  B8 01 00 00 00                  mov eax, 1
00706805  39 44 24 54                     cmp dword ptr [rsp + 0x54], eax
00706809  0F 84 02 06 00 00               je 0x140706e11
0070680F  48 21 74 24 48                  and qword ptr [rsp + 0x48], rsi
00706814  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00706819  48 03 5C 24 58                  add rbx, qword ptr [rsp + 0x58]
0070681E  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00706822  48 8B 15 0F 05 8C 00            mov rdx, qword ptr [rip + 0x8c050f]
00706829  45 33 C9                        xor r9d, r9d
0070682C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00706831  33 C9                           xor ecx, ecx
00706833  21 74 24 38                     and dword ptr [rsp + 0x38], esi
00706837  21 74 24 30                     and dword ptr [rsp + 0x30], esi
0070683B  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
0070683F  E8 9C 49 19 00                  call 0x14089b1e0
00706844  85 C0                           test eax, eax
00706846  0F 88 FD 00 00 00               js 0x140706949
0070684C  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00706851  4C 8B C3                        mov r8, rbx
00706854  48 8B CE                        mov rcx, rsi
00706857  33 D2                           xor edx, edx
00706859  E8 E2 03 FC FF                  call 0x1406c6c40
0070685E  4C 8B 05 D3 04 8C 00            mov r8, qword ptr [rip + 0x8c04d3]
00706865  BB 00 00 02 00                  mov ebx, 0x20000
0070686A  8B D3                           mov edx, ebx
0070686C  45 33 C9                        xor r9d, r9d
0070686F  48 8B CE                        mov rcx, rsi
00706872  E8 89 24 D3 FF                  call 0x140438d00
00706877  85 C0                           test eax, eax
00706879  0F 88 CA 00 00 00               js 0x140706949
0070687F  48 8D 45 98                     lea rax, [rbp - 0x68]
00706883  45 33 C9                        xor r9d, r9d
00706886  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0070688B  44 8B C3                        mov r8d, ebx
0070688E  4C 21 74 24 28                  and qword ptr [rsp + 0x28], r14
00706893  33 D2                           xor edx, edx
00706895  44 21 74 24 20                  and dword ptr [rsp + 0x20], r14d
0070689A  48 8B CE                        mov rcx, rsi
0070689D  E8 FE 2E 1B 00                  call 0x1408b97a0
007068A2  85 C0                           test eax, eax
007068A4  0F 88 9F 00 00 00               js 0x140706949
007068AA  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
007068AE  E8 FD 69 FA FF                  call 0x1406ad2b0
007068B3  4C 21 B6 80 00 00 00            and qword ptr [rsi + 0x80], r14
007068BA  48 8D 05 BF 09 90 FF            lea rax, [rip - 0x6ff641]
007068C1  4C 21 B6 88 00 00 00            and qword ptr [rsi + 0x88], r14
007068C8  48 8D 15 51 D3 8B 00            lea rdx, [rip + 0x8bd351]
007068CF  44 8B 85 80 00 00 00            mov r8d, dword ptr [rbp + 0x80]
007068D6  41 B9 01 00 00 00               mov r9d, 1
007068DC  48 89 46 08                     mov qword ptr [rsi + 8], rax
007068E0  41 83 F8 20                     cmp r8d, 0x20
007068E4  8A 85 98 00 00 00               mov al, byte ptr [rbp + 0x98]
007068EA  88 86 99 00 00 00               mov byte ptr [rsi + 0x99], al
007068F0  48 8D 05 29 D4 8B 00            lea rax, [rip + 0x8bd429]
007068F7  48 0F 43 D0                     cmovae rdx, rax
007068FB  C7 06 01 00 88 02               mov dword ptr [rsi], 0x2880001
00706901  48 83 CB FF                     or rbx, 0xffffffffffffffff
00706905  C7 46 10 48 44 6D 61            mov dword ptr [rsi + 0x10], 0x616d4448
0070690C  44 88 B6 98 00 00 00            mov byte ptr [rsi + 0x98], r14b
00706913  48 89 96 A0 00 00 00            mov qword ptr [rsi + 0xa0], rdx
0070691A  41 83 F8 40                     cmp r8d, 0x40
0070691E  72 05                           jb 0x140706925
00706920  48 8B C3                        mov rax, rbx
00706923  EB 0C                           jmp 0x140706931
00706925  41 8B C8                        mov ecx, r8d
00706928  49 8B C1                        mov rax, r9
0070692B  48 D3 E0                        shl rax, cl
0070692E  49 2B C1                        sub rax, r9
00706931  48 89 86 90 00 00 00            mov qword ptr [rsi + 0x90], rax
00706938  48 3B 82 90 00 00 00            cmp rax, qword ptr [rdx + 0x90]
0070693F  73 43                           jae 0x140706984
00706941  48 8B CE                        mov rcx, rsi
00706944  E8 07 2A BF FF                  call 0x1402f9350
00706949  33 F6                           xor esi, esi
0070694B  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
00706950  74 0D                           je 0x14070695f
00706952  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00706956  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0070695A  E8 71 41 FB FF                  call 0x1406baad0
0070695F  48 85 F6                        test rsi, rsi
00706962  0F 84 A9 04 00 00               je 0x140706e11
00706968  48 8B CE                        mov rcx, rsi
0070696B  E8 DC 5B DD FF                  call 0x1404dc54c
00706970  84 C0                           test al, al
00706972  0F 84 85 04 00 00               je 0x140706dfd
00706978  48 8D 05 81 0B 90 FF            lea rax, [rip - 0x6ff47f]
0070697F  E9 89 04 00 00                  jmp 0x140706e0d
00706984  4C 21 B6 40 01 00 00            and qword ptr [rsi + 0x140], r14
0070698B  48 8D 86 C0 00 00 00            lea rax, [rsi + 0xc0]
00706992  8B 4D 70                        mov ecx, dword ptr [rbp + 0x70]
00706995  8A 95 88 00 00 00               mov dl, byte ptr [rbp + 0x88]
0070699B  44 88 B6 5A 01 00 00            mov byte ptr [rsi + 0x15a], r14b
007069A2  48 89 40 08                     mov qword ptr [rax + 8], rax
007069A6  48 89 00                        mov qword ptr [rax], rax
007069A9  4C 21 B6 B8 00 00 00            and qword ptr [rsi + 0xb8], r14
007069B0  8A 85 A0 00 00 00               mov al, byte ptr [rbp + 0xa0]
007069B6  44 88 B6 E0 00 00 00            mov byte ptr [rsi + 0xe0], r14b
007069BD  89 8E E8 00 00 00               mov dword ptr [rsi + 0xe8], ecx
007069C3  88 96 BA 01 00 00               mov byte ptr [rsi + 0x1ba], dl
007069C9  88 86 BD 01 00 00               mov byte ptr [rsi + 0x1bd], al
007069CF  48 8B 85 B0 00 00 00            mov rax, qword ptr [rbp + 0xb0]
007069D6  48 89 86 C8 01 00 00            mov qword ptr [rsi + 0x1c8], rax
007069DD  8A 85 90 00 00 00               mov al, byte ptr [rbp + 0x90]
007069E3  88 86 B9 01 00 00               mov byte ptr [rsi + 0x1b9], al
007069E9  48 8D 86 40 02 00 00            lea rax, [rsi + 0x240]
007069F0  83 8E 80 01 00 00 FF            or dword ptr [rsi + 0x180], 0xffffffff
007069F7  44 89 86 C0 01 00 00            mov dword ptr [rsi + 0x1c0], r8d
007069FE  44 89 AE 74 02 00 00            mov dword ptr [rsi + 0x274], r13d
00706A05  C7 86 9C 00 00 00 03 00 00 00   mov dword ptr [rsi + 0x9c], 3
00706A0F  44 21 B6 70 02 00 00            and dword ptr [rsi + 0x270], r14d
00706A16  4C 21 B6 38 02 00 00            and qword ptr [rsi + 0x238], r14
00706A1D  48 89 40 08                     mov qword ptr [rax + 8], rax
00706A21  48 89 00                        mov qword ptr [rax], rax
00706A24  48 8D 05 25 9C E4 FF            lea rax, [rip - 0x1b63db]
00706A2B  44 88 B6 50 02 00 00            mov byte ptr [rsi + 0x250], r14b
00706A32  44 21 B6 68 02 00 00            and dword ptr [rsi + 0x268], r14d
00706A39  4C 21 B6 E0 01 00 00            and qword ptr [rsi + 0x1e0], r14
00706A40  48 89 86 F0 01 00 00            mov qword ptr [rsi + 0x1f0], rax
00706A47  48 89 B6 F8 01 00 00            mov qword ptr [rsi + 0x1f8], rsi
00706A4E  85 C9                           test ecx, ecx
00706A50  74 2C                           je 0x140706a7e
00706A52  84 D2                           test dl, dl
00706A54  8B D1                           mov edx, ecx
00706A56  48 8B CE                        mov rcx, rsi
00706A59  74 07                           je 0x140706a62
00706A5B  E8 74 27 00 00                  call 0x1407091d4
00706A60  EB 05                           jmp 0x140706a67
00706A62  E8 7D 24 00 00                  call 0x140708ee4
00706A67  85 C0                           test eax, eax
00706A69  0F 88 D2 FE FF FF               js 0x140706941
00706A6F  8B 8E E8 00 00 00               mov ecx, dword ptr [rsi + 0xe8]
00706A75  44 88 B6 59 01 00 00            mov byte ptr [rsi + 0x159], r14b
00706A7C  EB 10                           jmp 0x140706a8e
00706A7E  44 21 B6 E8 00 00 00            and dword ptr [rsi + 0xe8], r14d
00706A85  33 C9                           xor ecx, ecx
00706A87  44 88 8E 59 01 00 00            mov byte ptr [rsi + 0x159], r9b
00706A8E  48 8B 85 D0 00 00 00            mov rax, qword ptr [rbp + 0xd0]
00706A95  89 08                           mov dword ptr [rax], ecx
00706A97  8B 45 78                        mov eax, dword ptr [rbp + 0x78]
00706A9A  89 86 FC 00 00 00               mov dword ptr [rsi + 0xfc], eax
00706AA0  44 21 B6 08 02 00 00            and dword ptr [rsi + 0x208], r14d
00706AA7  4C 89 A6 10 02 00 00            mov qword ptr [rsi + 0x210], r12
00706AAE  4C 39 74 24 58                  cmp qword ptr [rsp + 0x58], r14
00706AB3  74 68                           je 0x140706b1d
00706AB5  41 8B D5                        mov edx, r13d
00706AB8  48 81 C2 88 02 00 00            add rdx, 0x288
00706ABF  48 03 D6                        add rdx, rsi
00706AC2  48 89 96 18 02 00 00            mov qword ptr [rsi + 0x218], rdx
00706AC9  44 38 74 24 50                  cmp byte ptr [rsp + 0x50], r14b
00706ACE  74 1A                           je 0x140706aea
00706AD0  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00706AD4  4C 8B C2                        mov r8, rdx
00706AD7  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00706ADC  45 33 C9                        xor r9d, r9d
00706ADF  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
00706AE3  E8 E8 3F FB FF                  call 0x1406baad0
00706AE8  EB 0C                           jmp 0x140706af6
00706AEA  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00706AEF  33 C9                           xor ecx, ecx
00706AF1  E8 02 1F 12 00                  call 0x1408289f8
00706AF6  85 C0                           test eax, eax
00706AF8  0F 89 B3 00 00 00               jns 0x140706bb1
00706AFE  4C 21 B6 18 02 00 00            and qword ptr [rsi + 0x218], r14
00706B05  83 FF 02                        cmp edi, 2
00706B08  0F 84 25 02 00 00               je 0x140706d33
00706B0E  B8 01 00 00 00                  mov eax, 1
00706B13  39 44 24 54                     cmp dword ptr [rsp + 0x54], eax
00706B17  0F 84 2E FE FF FF               je 0x14070694b
00706B1D  85 FF                           test edi, edi
00706B1F  0F 84 0E 02 00 00               je 0x140706d33
00706B25  48 8B 8E 18 02 00 00            mov rcx, qword ptr [rsi + 0x218]
00706B2C  45 8A E7                        mov r12b, r15b
00706B2F  48 85 C9                        test rcx, rcx
00706B32  0F 84 FB 01 00 00               je 0x140706d33
00706B38  E8 47 92 DC FF                  call 0x1404cfd84
00706B3D  84 C0                           test al, al
00706B3F  0F 85 EE 01 00 00               jne 0x140706d33
00706B45  E8 46 10 DF FF                  call 0x1404f7b90
00706B4A  33 C9                           xor ecx, ecx
00706B4C  85 C0                           test eax, eax
00706B4E  0F 84 F7 00 00 00               je 0x140706c4b
00706B54  48 8B 8E 18 02 00 00            mov rcx, qword ptr [rsi + 0x218]
00706B5B  E8 E0 76 E3 FF                  call 0x14053e240
00706B60  4C 8B AD C0 00 00 00            mov r13, qword ptr [rbp + 0xc0]
00706B67  33 C9                           xor ecx, ecx
00706B69  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00706B6D  4D 85 ED                        test r13, r13
00706B70  74 30                           je 0x140706ba2
00706B72  8D 51 01                        lea edx, [rcx + 1]
00706B75  3B C2                           cmp eax, edx
00706B77  75 29                           jne 0x140706ba2
00706B79  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00706B7E  48 C7 45 80 03 00 00 00         mov qword ptr [rbp - 0x80], 3
00706B86  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00706B8B  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00706B90  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00706B95  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00706B9A  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00706B9E  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
00706BA2  44 88 BD C8 00 00 00            mov byte ptr [rbp + 0xc8], r15b
00706BA9  44 8B FF                        mov r15d, edi
00706BAC  E9 EF 00 00 00                  jmp 0x140706ca0
00706BB1  48 8B 8E 18 02 00 00            mov rcx, qword ptr [rsi + 0x218]
00706BB8  E8 0F 75 E3 FF                  call 0x14053e0cc
00706BBD  4C 8B F0                        mov r14, rax
00706BC0  48 85 C0                        test rax, rax
00706BC3  74 5C                           je 0x140706c21
00706BC5  4C 39 A0 10 02 00 00            cmp qword ptr [rax + 0x210], r12
00706BCC  74 4B                           je 0x140706c19
00706BCE  48 8D B0 40 01 00 00            lea rsi, [rax + 0x140]
00706BD5  45 33 C0                        xor r8d, r8d
00706BD8  48 8B CE                        mov rcx, rsi
00706BDB  33 D2                           xor edx, edx
00706BDD  E8 4E 96 B0 FF                  call 0x140210230
00706BE2  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00706BE8  4C 8B F8                        mov r15, rax
00706BEB  73 0E                           jae 0x140706bfb
00706BED  4C 8B C6                        mov r8, rsi
00706BF0  48 8B D0                        mov rdx, rax
00706BF3  48 8B CE                        mov rcx, rsi
00706BF6  E8 95 90 B0 FF                  call 0x14020fc90
00706BFB  B8 01 00 00 00                  mov eax, 1
00706C00  4D 85 FF                        test r15, r15
00706C03  74 04                           je 0x140706c09
00706C05  41 88 47 0A                     mov byte ptr [r15 + 0xa], al
00706C09  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00706C0E  44 8A F8                        mov r15b, al
00706C11  88 85 C8 00 00 00               mov byte ptr [rbp + 0xc8], al
00706C17  EB 08                           jmp 0x140706c21
00706C19  48 8B C8                        mov rcx, rax
00706C1C  E8 2F 27 BF FF                  call 0x1402f9350
00706C21  85 FF                           test edi, edi
00706C23  0F 84 0A 01 00 00               je 0x140706d33
00706C29  48 8B 05 68 A0 6F 00            mov rax, qword ptr [rip + 0x6fa068]
00706C30  33 D2                           xor edx, edx
00706C32  48 8B 8E 18 02 00 00            mov rcx, qword ptr [rsi + 0x218]
00706C39  E8 92 3E FB FF                  call 0x1406baad0
00706C3E  84 C0                           test al, al
00706C40  0F 85 DF FE FF FF               jne 0x140706b25
00706C46  E9 E8 00 00 00                  jmp 0x140706d33
00706C4B  4C 8B AD C0 00 00 00            mov r13, qword ptr [rbp + 0xc0]
00706C52  44 8B FF                        mov r15d, edi
00706C55  44 88 A5 C8 00 00 00            mov byte ptr [rbp + 0xc8], r12b
00706C5C  4C 3B E9                        cmp r13, rcx
00706C5F  74 3F                           je 0x140706ca0
00706C61  38 0D 11 D3 8B 00               cmp byte ptr [rip + 0x8bd311], cl
00706C67  44 88 A5 C8 00 00 00            mov byte ptr [rbp + 0xc8], r12b
00706C6E  74 30                           je 0x140706ca0
00706C70  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00706C75  48 C7 45 80 03 00 00 00         mov qword ptr [rbp - 0x80], 3
00706C7D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00706C82  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00706C87  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00706C8C  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00706C91  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00706C95  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
00706C99  44 88 A5 C8 00 00 00            mov byte ptr [rbp + 0xc8], r12b
00706CA0  48 8B 05 D1 AA 8B 00            mov rax, qword ptr [rip + 0x8baad1]
00706CA7  4C 8D A6 20 02 00 00            lea r12, [rsi + 0x220]
00706CAE  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
00706CB2  4D 8B C4                        mov r8, r12
00706CB5  48 8B 8E 10 02 00 00            mov rcx, qword ptr [rsi + 0x210]
00706CBC  48 8B 80 A0 00 00 00            mov rax, qword ptr [rax + 0xa0]
00706CC3  E8 08 3E FB FF                  call 0x1406baad0
00706CC8  8B F8                           mov edi, eax
00706CCA  E8 C1 0E DF FF                  call 0x1404f7b90
00706CCF  85 FF                           test edi, edi
00706CD1  79 59                           jns 0x140706d2c
00706CD3  4D 85 ED                        test r13, r13
00706CD6  74 3D                           je 0x140706d15
00706CD8  85 C0                           test eax, eax
00706CDA  74 0D                           je 0x140706ce9
00706CDC  B8 01 00 00 00                  mov eax, 1
00706CE1  39 44 24 60                     cmp dword ptr [rsp + 0x60], eax
00706CE5  75 2E                           jne 0x140706d15
00706CE7  EB 09                           jmp 0x140706cf2
00706CE9  80 3D 88 D2 8B 00 00            cmp byte ptr [rip + 0x8bd288], 0
00706CF0  74 23                           je 0x140706d15
00706CF2  48 8B 05 7F AA 8B 00            mov rax, qword ptr [rip + 0x8baa7f]
00706CF9  4D 8B C4                        mov r8, r12
00706CFC  48 8B 8E 10 02 00 00            mov rcx, qword ptr [rsi + 0x210]
00706D03  33 D2                           xor edx, edx
00706D05  48 8B 80 A0 00 00 00            mov rax, qword ptr [rax + 0xa0]
00706D0C  E8 BF 3D FB FF                  call 0x1406baad0
00706D11  85 C0                           test eax, eax
00706D13  79 17                           jns 0x140706d2c
00706D15  41 83 FF 02                     cmp r15d, 2
00706D19  74 18                           je 0x140706d33
00706D1B  8B 7C 24 54                     mov edi, dword ptr [rsp + 0x54]
00706D1F  41 BF 01 00 00 00               mov r15d, 1
00706D25  41 3B FF                        cmp edi, r15d
00706D28  74 5D                           je 0x140706d87
00706D2A  EB 11                           jmp 0x140706d3d
00706D2C  44 89 BE 08 02 00 00            mov dword ptr [rsi + 0x208], r15d
00706D33  8B 7C 24 54                     mov edi, dword ptr [rsp + 0x54]
00706D37  41 BF 01 00 00 00               mov r15d, 1
00706D3D  48 83 A6 00 02 00 00 00         and qword ptr [rsi + 0x200], 0
00706D45  48 8B D3                        mov rdx, rbx
00706D48  48 8B CE                        mov rcx, rsi
00706D4B  E8 D0 C5 DD FF                  call 0x1404e3320
00706D50  85 C0                           test eax, eax
00706D52  79 4A                           jns 0x140706d9e
00706D54  8B 86 08 02 00 00               mov eax, dword ptr [rsi + 0x208]
00706D5A  85 C0                           test eax, eax
00706D5C  74 29                           je 0x140706d87
00706D5E  83 F8 02                        cmp eax, 2
00706D61  75 09                           jne 0x140706d6c
00706D63  83 A6 08 02 00 00 00            and dword ptr [rsi + 0x208], 0
00706D6A  EB 05                           jmp 0x140706d71
00706D6C  41 3B FF                        cmp edi, r15d
00706D6F  74 16                           je 0x140706d87
00706D71  83 A6 08 02 00 00 00            and dword ptr [rsi + 0x208], 0
00706D78  48 8B D3                        mov rdx, rbx
00706D7B  48 8B CE                        mov rcx, rsi
00706D7E  E8 9D C5 DD FF                  call 0x1404e3320
00706D83  85 C0                           test eax, eax
00706D85  79 17                           jns 0x140706d9e
00706D87  48 8B CE                        mov rcx, rsi
00706D8A  E8 C1 25 BF FF                  call 0x1402f9350
00706D8F  8A 8D C8 00 00 00               mov cl, byte ptr [rbp + 0xc8]
00706D95  33 F6                           xor esi, esi
00706D97  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
00706D9C  EB 21                           jmp 0x140706dbf
00706D9E  8A 8D C8 00 00 00               mov cl, byte ptr [rbp + 0xc8]
00706DA4  4D 85 F6                        test r14, r14
00706DA7  74 0B                           je 0x140706db4
00706DA9  84 C9                           test cl, cl
00706DAB  74 07                           je 0x140706db4
00706DAD  45 88 BE 5A 01 00 00            mov byte ptr [r14 + 0x15a], r15b
00706DB4  48 8B 86 00 02 00 00            mov rax, qword ptr [rsi + 0x200]
00706DBB  48 89 70 38                     mov qword ptr [rax + 0x38], rsi
00706DBF  84 C9                           test cl, cl
00706DC1  0F 84 84 FB FF FF               je 0x14070694b
00706DC7  49 8D BE 40 01 00 00            lea rdi, [r14 + 0x140]
00706DCE  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
00706DD3  80 E3 06                        and bl, 6
00706DD6  80 FB 02                        cmp bl, 2
00706DD9  75 08                           jne 0x140706de3
00706DDB  48 8B CF                        mov rcx, rdi
00706DDE  E8 ED EF B5 FF                  call 0x140265dd0
00706DE3  48 8B CF                        mov rcx, rdi
00706DE6  E8 15 A8 BD FF                  call 0x1402e1600
00706DEB  49 8B CE                        mov rcx, r14
00706DEE  E8 5D 25 BF FF                  call 0x1402f9350
00706DF3  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00706DF8  E9 4E FB FF FF                  jmp 0x14070694b
00706DFD  E8 7E BD E4 FF                  call 0x140552b80
00706E02  84 C0                           test al, al
00706E04  74 0B                           je 0x140706e11
00706E06  48 8D 05 B3 05 90 FF            lea rax, [rip - 0x6ffa4d]
00706E0D  48 89 46 08                     mov qword ptr [rsi + 8], rax
00706E11  48 8B C6                        mov rax, rsi
00706E14  48 81 C4 28 01 00 00            add rsp, 0x128
00706E1B  41 5F                           pop r15
00706E1D  41 5E                           pop r14
00706E1F  41 5D                           pop r13
00706E21  41 5C                           pop r12
00706E23  5F                              pop rdi
00706E24  5E                              pop rsi
00706E25  5B                              pop rbx
00706E26  5D                              pop rbp
00706E27  C3                              ret
00706E28  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpDmaAllocateChildAdapterV3(int a1, int a2, int a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned __int8 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned int v_stack_m138;
    unsigned int v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int8 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (296);
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 96) = 48;
    *(unsigned __int64 *)(v_rsp - 104 - 104) = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 72) = 528;
    *(unsigned __int8 *)(v_rsp - 104 + 200) = 0;
    v_stack_m118 = 0;
    v_stack_mF8 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104 - 128) = v_xmm0;
    v_stack_m100 = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 112) = 0;
    result = memset(v_rsp - 104 - 48, a2, v_rdi + 80, a4);
    v_stack_m108 = 2;
    result = HalpIommuGetSecurityPolicy(v_rsp - 104 - 48, a2, v_rdi + 80, a4);
    v_stack_m114 = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 104 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104 - 80) = 0;
    v_rbx = 648;
    v_r13 = 0;
    if ((*(unsigned __int8 *)(v_rsp - 104 + 144)) == 0) {
        result = *(unsigned int *)(v_rsp - 104 + 168);
        result = (unsigned int)((result) + 1);
        v_r13 = result + result * 2;
        result = v_stack_m114;
        v_r13 = (unsigned int)((v_r13) << (3));
        v_rbx = (unsigned int)(v_r13);
        v_rbx = (v_rbx) + (648);
    }
    if (*(unsigned __int64 *)(v_rsp - 104 + 192) != 0) goto loc_00706790;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 184))) == 0) goto loc_00706790;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 184)))) != 2) goto loc_00706788;
    v_rdi = 0;
    goto loc_00706790;
loc_00706788:
    if (((unsigned int)(result)) == 1) goto loc_00706E11;
loc_00706790:
    if (0 == 0) goto loc_0070680F;
    if (*(unsigned __int64 *)(v_rsp - 104 + 192) == 0) goto loc_0070680F;
    result = HalpDmaGetIommuInterface(*(unsigned __int64 *)(v_rsp - 104 + 192), v_rsp - 104 - 48, v_rdi + 80, a4);
    if (sign_flag) goto loc_007067F7;
    a3 = 0;
    a2 = 0;
    v_stack_m118 = 1;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 104 - 40), a2, a3, v_stack_m110);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_007067D8;
    if (v_stack_m110 != 0) goto loc_0070680F;
loc_007067D8:
    if (0 != 2) goto loc_007067E1;
    v_rdi = 0;
    goto loc_007067F0;
loc_007067E1:
    if (v_stack_m114 == 1) goto loc_00706952;
loc_007067F0:
    goto loc_0070680F;
loc_007067F7:
    if (0 != 2) goto loc_00706800;
    v_rdi = 0;
    goto loc_0070680F;
loc_00706800:
    if (v_stack_m114 == 1) goto loc_00706E11;
loc_0070680F:
    v_rbx = (v_rbx) + (v_stack_m110);
    a4 = 0;
    v_stack_m128 = v_stack_m100;
    a1 = 0;
    v_stack_m140 = (unsigned int)(v_rbx);
    result = ObCreateObjectEx(a1, *(unsigned __int64 *)(v_rip + 9176335), v_rsp - 104 - 96, a4);
    if (sign_flag) goto loc_00706949;
    a2 = 0;
    result = memset(v_stack_m100, a2, v_rbx, a4);
    a4 = 0;
    result = ObReferenceObjectByPointer(v_stack_m100, (unsigned int)((unsigned int)((unsigned int)(0x20000ULL))), *(unsigned __int64 *)(v_rip + 9176275), a4);
    if (sign_flag) goto loc_00706949;
    a4 = 0;
    v_stack_m138 = v_rsp - 104 - 104;
    a2 = 0;
    result = ObInsertObjectEx(v_stack_m100, a2, (unsigned int)((unsigned int)((unsigned int)(0x20000ULL))), a4);
    if (sign_flag) goto loc_00706949;
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 104 - 104), a2, (unsigned int)((unsigned int)((unsigned int)(0x20000ULL))), a4);
    *(unsigned __int64 *)(v_stack_m100 + 8) = v_rip - 7337537;
    *(unsigned __int8 *)(v_stack_m100 + 153) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 + 152));
    a2 = v_rip + 9163601;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 128)))) >= 32) { a2 = v_rip + 9163817; }
    *(unsigned int *)(v_stack_m100) = 0x2880001ULL;
    v_rbx = ((unsigned int)(0x20000ULL)) | (-1);
    *(unsigned int *)(v_stack_m100 + 16) = 0x616D4448ULL;
    *(unsigned __int8 *)(v_stack_m100 + 152) = 0;
    *(unsigned __int64 *)(v_stack_m100 + 160) = a2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 128)))) < 64) goto loc_00706925;
    goto loc_00706931;
loc_00706925:
    result = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 128))))));
    result = (result) - (1);
loc_00706931:
    *(unsigned __int64 *)(v_stack_m100 + 144) = result;
    if (result >= (*(unsigned __int64 *)(a2 + 144))) goto loc_00706984;
loc_00706941:
    result = ObfDereferenceObject(v_stack_m100, a2, (unsigned int)(*(unsigned int *)(v_rsp - 104 + 128)), 1);
loc_00706949:
    v_rsi = 0;
loc_0070694B:
    if (v_stack_m118 != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 104 - 40);
        result = *(unsigned __int64 *)(v_rsp - 104 - 24);
        result = guard_dispatch_icall(a1, a2, (unsigned int)(*(unsigned int *)(v_rsp - 104 + 128)), 1);
    }
    if (0 == 0) goto loc_00706E11;
    result = HalpDmaIsThinDmarCapable(0, a2, (unsigned int)(*(unsigned int *)(v_rsp - 104 + 128)), 1);
    if ((unsigned __int8)(result) == 0) goto loc_00706DFD;
    goto loc_00706E0D;
loc_00706984:
    *(unsigned __int8 *)(v_rsi + 346) = 0;
    *(unsigned __int64 *)(v_rsi + 192 + 8) = v_rsi + 192;
    *(unsigned __int64 *)(v_rsi + 192) = v_rsi + 192;
    *(unsigned __int8 *)(v_rsi + 224) = 0;
    *(unsigned int *)(v_rsi + 232) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 112)));
    *(unsigned __int8 *)(v_rsi + 442) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 + 136));
    *(unsigned __int8 *)(v_rsi + 445) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 + 160));
    *(unsigned __int64 *)(v_rsi + 456) = *(unsigned __int64 *)(v_rsp - 104 + 176);
    *(unsigned __int8 *)(v_rsi + 441) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 + 144));
    *(unsigned int *)(v_rsi + 448) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 128)));
    *(unsigned int *)(v_rsi + 628) = (unsigned int)(v_r13);
    *(unsigned int *)(v_rsi + 156) = 3;
    *(unsigned __int64 *)(v_rsi + 576 + 8) = v_rsi + 576;
    *(unsigned __int64 *)(v_rsi + 576) = v_rsi + 576;
    *(unsigned __int8 *)(v_rsi + 592) = 0;
    *(unsigned __int64 *)(v_rsi + 496) = v_rip - 1795035;
    *(unsigned __int64 *)(v_rsi + 504) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 112))) == 0) goto loc_00706A7E;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 + 136)) == 0) goto loc_00706A62;
    result = HalpDmaAllocateLocalScatterPool(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 112)))), (unsigned int)(*(unsigned int *)(v_rsp - 104 + 128)), 1);
    goto loc_00706A67;
loc_00706A62:
    result = HalpDmaAllocateLocalContiguousPool(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 112)))), (unsigned int)(*(unsigned int *)(v_rsp - 104 + 128)), 1);
loc_00706A67:
    if (sign_flag) goto loc_00706941;
    *(unsigned __int8 *)(v_rsi + 345) = 0;
    goto loc_00706A8E;
loc_00706A7E:
    a1 = 0;
    *(unsigned __int8 *)(v_rsi + 345) = 1;
loc_00706A8E:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 208)) = 0;
    *(unsigned int *)(v_rsi + 252) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 104 + 120)));
    *(unsigned __int64 *)(v_rsi + 528) = *(unsigned __int64 *)(v_rsp - 104 + 192);
    if (v_stack_m110 == 0) goto loc_00706B1D;
    a2 = ((unsigned int)((unsigned int)(v_r13))) + (648);
    a2 = (a2) + (0);
    *(unsigned __int64 *)(v_rsi + 536) = a2;
    if (v_stack_m118 == 0) goto loc_00706AEA;
    a4 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rsp - 104 - 40), v_stack_m110, a2, a4);
    goto loc_00706AF6;
loc_00706AEA:
    a1 = 0;
    result = IidCloneDeviceId(a1, v_stack_m110, v_stack_m110, a4);
loc_00706AF6:
    if (!sign_flag) goto loc_00706BB1;
    if (0 == 2) goto loc_00706D33;
    if (v_stack_m114 == 1) goto loc_0070694B;
loc_00706B1D:
    if (0 == 0) goto loc_00706D33;
loc_00706B25:
    if (*(unsigned __int64 *)(v_rsi + 536) == 0) goto loc_00706D33;
    result = HalpIommuCheckExceptionList(*(unsigned __int64 *)(v_rsi + 536), v_stack_m110, v_stack_m110, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00706D33;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_rsi + 536), v_stack_m110, v_stack_m110, a4);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00706C4B;
    result = HalpDmaGetDefaultRemappingDomainPolicy(*(unsigned __int64 *)(v_rsi + 536), v_stack_m110, v_stack_m110, a4);
    a1 = 0;
    v_stack_m108 = (unsigned int)(result);
    if (*(unsigned __int64 *)(v_rsp - 104 + 192) == 0) goto loc_00706BA2;
    if (((unsigned int)(result)) == ((unsigned int)(a1 + 1))) {
        result = v_stack_mF8;
        *(unsigned __int64 *)(v_rsp - 104 - 128) = 3;
        v_stack_mF0 = result;
        result = v_stack_mF8;
        v_stack_mF8 = result;
        result = v_stack_mF8;
        *(unsigned __int64 *)(v_rsp - 104 - 112) = result;
        *(unsigned __int64 *)(v_rsp - 104 - 120) = 0;
    }
    *(unsigned __int8 *)(v_rsp - 104 + 200) = 0;
    goto loc_00706CA0;
loc_00706BB1:
    result = HalpDmaFindAdapterByDeviceId(*(unsigned __int64 *)(v_rsi + 536), a1 + 1, v_stack_m110, a4);
    if (result == 0) goto loc_00706C21;
    if ((*(unsigned __int64 *)(result + 528)) == 0) goto loc_00706C19;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 320, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = result + 320;
        a2 = result;
        a1 = result + 320;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int8 *)(v_rsp - 104 + 200) = 1;
    goto loc_00706C21;
loc_00706C19:
    result = ObfDereferenceObject(1, a2, a3, a4);
loc_00706C21:
    if (0 == 0) goto loc_00706D33;
    a2 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_m100 + 536), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00706B25;
    goto loc_00706D33;
loc_00706C4B:
    *(unsigned __int8 *)(v_rsp - 104 + 200) = 0;
    if ((*(unsigned __int64 *)(v_rsp - 104 + 192)) == (*(unsigned __int64 *)(v_stack_m100 + 536))) goto loc_00706CA0;
    *(unsigned __int8 *)(v_rsp - 104 + 200) = 0;
    if ((*(unsigned __int8 *)(v_rip + 9163537)) != ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m100 + 536)))) {
        result = v_stack_mF8;
        *(unsigned __int64 *)(v_rsp - 104 - 128) = 3;
        v_stack_mF0 = result;
        result = v_stack_mF8;
        v_stack_mF8 = result;
        result = v_stack_mF8;
        *(unsigned __int64 *)(v_rsp - 104 - 112) = result;
        *(unsigned __int64 *)(v_rsp - 104 - 120) = *(unsigned __int64 *)(v_stack_m100 + 536);
        *(unsigned __int8 *)(v_rsp - 104 + 200) = 0;
    }
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_m100 + 528), *(unsigned __int64 *)(v_rsp - 104 - 112), v_stack_m100 + 544, a4);
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_stack_m100 + 528), *(unsigned __int64 *)(v_rsp - 104 - 112), v_stack_m100 + 544, a4);
    if (!sign_flag) goto loc_00706D2C;
    if (*(unsigned __int64 *)(v_rsp - 104 + 192) == 0) goto loc_00706D15;
    if ((unsigned int)(result) == 0) goto loc_00706CE9;
    if (v_stack_m108 != 1) goto loc_00706D15;
    goto loc_00706CF2;
loc_00706CE9:
    if ((*(unsigned __int8 *)(v_rip + 9163400)) == 0) goto loc_00706D15;
loc_00706CF2:
    a2 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_m100 + 528), a2, v_stack_m100 + 544, a4);
    if (!sign_flag) goto loc_00706D2C;
loc_00706D15:
    if (0 == 2) goto loc_00706D33;
    if (((unsigned int)((unsigned int)(v_stack_m114))) == 1) goto loc_00706D87;
    goto loc_00706D3D;
loc_00706D2C:
    *(unsigned int *)(v_stack_m100 + 520) = 1;
loc_00706D33:
loc_00706D3D:
    result = HalJoinDmaDomain(v_stack_m100, v_rbx, v_stack_m100 + 544, a4);
    if (!sign_flag) goto loc_00706D9E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m100 + 520))) == 0) goto loc_00706D87;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m100 + 520)))) != 2) goto loc_00706D6C;
    goto loc_00706D71;
loc_00706D6C:
    if (((unsigned int)((unsigned int)(v_stack_m114))) == 1) goto loc_00706D87;
loc_00706D71:
    result = HalJoinDmaDomain(v_stack_m100, v_rbx, v_stack_m100 + 544, a4);
    if (!sign_flag) goto loc_00706D9E;
loc_00706D87:
    result = ObfDereferenceObject(v_stack_m100, v_rbx, v_stack_m100 + 544, a4);
    v_rsi = 0;
    v_stack_m100 = 0;
    goto loc_00706DBF;
loc_00706D9E:
    if (result == 0) goto loc_00706DB4;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 + 200)) != 0) {
        *(unsigned __int8 *)(result + 346) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 512) + 56) = 0;
loc_00706DBF:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 + 200)) == 0) goto loc_0070694B;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    result = *(unsigned __int64 *)(v_rsi + 512);
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = result + 320;
        result = ExfTryToWakePushLock(a1, v_rbx, v_stack_m100 + 544, a4);
    }
    result = KeAbPostRelease(result + 320, v_rbx, v_stack_m100 + 544, a4);
    result = ObfDereferenceObject(result, v_rbx, v_stack_m100 + 544, a4);
    goto loc_0070694B;
loc_00706DFD:
    result = HalpDmaIsThinDmaCapable(result, v_rbx, v_stack_m100 + 544, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00706E11;
loc_00706E0D:
    *(unsigned __int64 *)(v_stack_m100 + 8) = v_rip - 7338573;
loc_00706E11:
    v_rsp = (v_rsp) + (296);
    return v_stack_m100;
}
```

## 5. (Beta) C Style

```c
int64_t HalpDmaAllocateChildAdapterV3(int32_t Arg1, int32_t Arg2, int32_t Arg3, uint8_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m114;
    uint8_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint32_t v_stack_m138;
    uint32_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint8_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (296);
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x60) = 48;
    *(uint64_t *)(local_rsp - 0x68 - 0x68) = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x48) = 528;
    *(uint8_t *)(local_rsp - 0x68 + 0xC8) = 0;
    v_stack_m118 = 0;
    v_stack_mF8 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68 - 0x80) = v_xmm0;
    v_stack_m100 = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x70) = 0;
    result = memset(local_rsp - 104 - 48, Arg2, local_rdi + 80, Arg4);
    v_stack_m108 = 2;
    result = HalpIommuGetSecurityPolicy(local_rsp - 104 - 48, Arg2, local_rdi + 80, Arg4);
    v_stack_m114 = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x68 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68 - 0x50) = 0;
    local_rbx = 648;
    local_r13 = 0;
    if ((*(uint8_t *)(local_rsp - 0x68 + 0x90)) == 0) {
        result = *(uint32_t *)(local_rsp - 0x68 + 0xA8);
        result = (uint32_t)((result) + 1);
        local_r13 = result + result * 2;
        result = v_stack_m114;
        local_r13 = (uint32_t)((local_r13) << (3));
        local_rbx = (uint32_t)(local_r13);
        local_rbx = (local_rbx) + (648);
    }
    if (*(uint64_t *)(local_rsp - 0x68 + 0xC0) != 0) goto loc_00706790;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0xB8))) == 0) goto loc_00706790;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0xB8)))) != 2) goto loc_00706788;
    local_rdi = 0;
    goto loc_00706790;
loc_00706788:
    if (((uint32_t)(result)) == 1) goto loc_00706E11;
loc_00706790:
    if (0 == 0) goto loc_0070680F;
    if (*(uint64_t *)(local_rsp - 0x68 + 0xC0) == 0) goto loc_0070680F;
    result = HalpDmaGetIommuInterface(*(uint64_t *)(local_rsp - 0x68 + 0xC0), local_rsp - 104 - 48, local_rdi + 80, Arg4);
    if (sign_flag) goto loc_007067F7;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m118 = 1;
    result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x68 - 0x28), Arg2, Arg3, v_stack_m110);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_007067D8;
    if (v_stack_m110 != 0) goto loc_0070680F;
loc_007067D8:
    if (0 != 2) goto loc_007067E1;
    local_rdi = 0;
    goto loc_007067F0;
loc_007067E1:
    if (v_stack_m114 == 1) goto loc_00706952;
loc_007067F0:
    goto loc_0070680F;
loc_007067F7:
    if (0 != 2) goto loc_00706800;
    local_rdi = 0;
    goto loc_0070680F;
loc_00706800:
    if (v_stack_m114 == 1) goto loc_00706E11;
loc_0070680F:
    local_rbx = (local_rbx) + (v_stack_m110);
    Arg4 = 0;
    v_stack_m128 = v_stack_m100;
    Arg1 = 0;
    v_stack_m140 = (uint32_t)(local_rbx);
    result = ObCreateObjectEx(Arg1, *(uint64_t *)(v_rip + 0x8C050F), local_rsp - 104 - 96, Arg4);
    if (sign_flag) goto loc_00706949;
    Arg2 = 0;
    result = memset(v_stack_m100, Arg2, local_rbx, Arg4);
    Arg4 = 0;
    result = ObReferenceObjectByPointer(v_stack_m100, (uint32_t)((uint32_t)((uint32_t)(0x20000ULL))), *(uint64_t *)(v_rip + 0x8C04D3), Arg4);
    if (sign_flag) goto loc_00706949;
    Arg4 = 0;
    v_stack_m138 = local_rsp - 104 - 104;
    Arg2 = 0;
    result = ObInsertObjectEx(v_stack_m100, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x20000ULL))), Arg4);
    if (sign_flag) goto loc_00706949;
    result = ZwClose(*(uint64_t *)(local_rsp - 0x68 - 0x68), Arg2, (uint32_t)((uint32_t)((uint32_t)(0x20000ULL))), Arg4);
    *(uint64_t *)(v_stack_m100 + 0x8) = v_rip - 7337537;
    *(uint8_t *)(v_stack_m100 + 0x99) = (uint8_t)(*(uint8_t *)(local_rsp - 0x68 + 0x98));
    Arg2 = v_rip + 9163601;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x80)))) >= 32) { Arg2 = v_rip + 9163817; }
    *(uint32_t *)(v_stack_m100) = 0x2880001ULL;
    local_rbx = ((uint32_t)(0x20000ULL)) | (-1);
    *(uint32_t *)(v_stack_m100 + 0x10) = 0x616D4448ULL;
    *(uint8_t *)(v_stack_m100 + 0x98) = 0;
    *(uint64_t *)(v_stack_m100 + 0xA0) = Arg2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x80)))) < 64) goto loc_00706925;
    goto loc_00706931;
loc_00706925:
    result = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x80))))));
    result = (result) - (1);
loc_00706931:
    *(uint64_t *)(v_stack_m100 + 0x90) = result;
    if (result >= (*(uint64_t *)(Arg2 + 0x90))) goto loc_00706984;
loc_00706941:
    result = ObfDereferenceObject(v_stack_m100, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x80)), 1);
loc_00706949:
    local_rsi = 0;
loc_0070694B:
    if (v_stack_m118 != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x68 - 0x28);
        result = *(uint64_t *)(local_rsp - 0x68 - 0x18);
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x80)), 1);
    }
    if (0 == 0) goto loc_00706E11;
    result = HalpDmaIsThinDmarCapable(0, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x80)), 1);
    if ((uint8_t)(result) == 0) goto loc_00706DFD;
    goto loc_00706E0D;
loc_00706984:
    *(uint8_t *)(local_rsi + 0x15A) = 0;
    *(uint64_t *)(local_rsi + 0xC0 + 0x8) = local_rsi + 192;
    *(uint64_t *)(local_rsi + 0xC0) = local_rsi + 192;
    *(uint8_t *)(local_rsi + 0xE0) = 0;
    *(uint32_t *)(local_rsi + 0xE8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x70)));
    *(uint8_t *)(local_rsi + 0x1BA) = (uint8_t)(*(uint8_t *)(local_rsp - 0x68 + 0x88));
    *(uint8_t *)(local_rsi + 0x1BD) = (uint8_t)(*(uint8_t *)(local_rsp - 0x68 + 0xA0));
    *(uint64_t *)(local_rsi + 0x1C8) = *(uint64_t *)(local_rsp - 0x68 + 0xB0);
    *(uint8_t *)(local_rsi + 0x1B9) = (uint8_t)(*(uint8_t *)(local_rsp - 0x68 + 0x90));
    *(uint32_t *)(local_rsi + 0x1C0) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x80)));
    *(uint32_t *)(local_rsi + 0x274) = (uint32_t)(local_r13);
    *(uint32_t *)(local_rsi + 0x9C) = 3;
    *(uint64_t *)(local_rsi + 0x240 + 0x8) = local_rsi + 576;
    *(uint64_t *)(local_rsi + 0x240) = local_rsi + 576;
    *(uint8_t *)(local_rsi + 0x250) = 0;
    *(uint64_t *)(local_rsi + 0x1F0) = v_rip - 1795035;
    *(uint64_t *)(local_rsi + 0x1F8) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x70))) == 0) goto loc_00706A7E;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x68 + 0x88)) == 0) goto loc_00706A62;
    result = HalpDmaAllocateLocalScatterPool(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x70)))), (uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x80)), 1);
    goto loc_00706A67;
loc_00706A62:
    result = HalpDmaAllocateLocalContiguousPool(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x70)))), (uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x80)), 1);
loc_00706A67:
    if (sign_flag) goto loc_00706941;
    *(uint8_t *)(local_rsi + 0x159) = 0;
    goto loc_00706A8E;
loc_00706A7E:
    Arg1 = 0;
    *(uint8_t *)(local_rsi + 0x159) = 1;
loc_00706A8E:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0xD0)) = 0;
    *(uint32_t *)(local_rsi + 0xFC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x68 + 0x78)));
    *(uint64_t *)(local_rsi + 0x210) = *(uint64_t *)(local_rsp - 0x68 + 0xC0);
    if (v_stack_m110 == 0) goto loc_00706B1D;
    Arg2 = ((uint32_t)((uint32_t)(local_r13))) + (648);
    Arg2 = (Arg2) + (0);
    *(uint64_t *)(local_rsi + 0x218) = Arg2;
    if (v_stack_m118 == 0) goto loc_00706AEA;
    Arg4 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(local_rsp - 0x68 - 0x28), v_stack_m110, Arg2, Arg4);
    goto loc_00706AF6;
loc_00706AEA:
    Arg1 = 0;
    result = IidCloneDeviceId(Arg1, v_stack_m110, v_stack_m110, Arg4);
loc_00706AF6:
    if (!sign_flag) goto loc_00706BB1;
    if (0 == 2) goto loc_00706D33;
    if (v_stack_m114 == 1) goto loc_0070694B;
loc_00706B1D:
    if (0 == 0) goto loc_00706D33;
loc_00706B25:
    if (*(uint64_t *)(local_rsi + 0x218) == 0) goto loc_00706D33;
    result = HalpIommuCheckExceptionList(*(uint64_t *)(local_rsi + 0x218), v_stack_m110, v_stack_m110, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00706D33;
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(local_rsi + 0x218), v_stack_m110, v_stack_m110, Arg4);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00706C4B;
    result = HalpDmaGetDefaultRemappingDomainPolicy(*(uint64_t *)(local_rsi + 0x218), v_stack_m110, v_stack_m110, Arg4);
    Arg1 = 0;
    v_stack_m108 = (uint32_t)(result);
    if (*(uint64_t *)(local_rsp - 0x68 + 0xC0) == 0) goto loc_00706BA2;
    if (((uint32_t)(result)) == ((uint32_t)(Arg1 + 1))) {
        result = v_stack_mF8;
        *(uint64_t *)(local_rsp - 0x68 - 0x80) = 3;
        v_stack_mF0 = result;
        result = v_stack_mF8;
        v_stack_mF8 = result;
        result = v_stack_mF8;
        *(uint64_t *)(local_rsp - 0x68 - 0x70) = result;
        *(uint64_t *)(local_rsp - 0x68 - 0x78) = 0;
    }
    *(uint8_t *)(local_rsp - 0x68 + 0xC8) = 0;
    goto loc_00706CA0;
loc_00706BB1:
    result = HalpDmaFindAdapterByDeviceId(*(uint64_t *)(local_rsi + 0x218), Arg1 + 1, v_stack_m110, Arg4);
    if (result == 0) goto loc_00706C21;
    if ((*(uint64_t *)(result + 0x210)) == 0) goto loc_00706C19;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 320, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 320;
        Arg2 = result;
        Arg1 = result + 320;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint8_t *)(local_rsp - 0x68 + 0xC8) = 1;
    goto loc_00706C21;
loc_00706C19:
    result = ObfDereferenceObject(1, Arg2, Arg3, Arg4);
loc_00706C21:
    if (0 == 0) goto loc_00706D33;
    Arg2 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_m100 + 0x218), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00706B25;
    goto loc_00706D33;
loc_00706C4B:
    *(uint8_t *)(local_rsp - 0x68 + 0xC8) = 0;
    if ((*(uint64_t *)(local_rsp - 0x68 + 0xC0)) == (*(uint64_t *)(v_stack_m100 + 0x218))) goto loc_00706CA0;
    *(uint8_t *)(local_rsp - 0x68 + 0xC8) = 0;
    if ((*(uint8_t *)(v_rip + 0x8BD311)) != ((uint8_t)(*(uint64_t *)(v_stack_m100 + 0x218)))) {
        result = v_stack_mF8;
        *(uint64_t *)(local_rsp - 0x68 - 0x80) = 3;
        v_stack_mF0 = result;
        result = v_stack_mF8;
        v_stack_mF8 = result;
        result = v_stack_mF8;
        *(uint64_t *)(local_rsp - 0x68 - 0x70) = result;
        *(uint64_t *)(local_rsp - 0x68 - 0x78) = *(uint64_t *)(v_stack_m100 + 0x218);
        *(uint8_t *)(local_rsp - 0x68 + 0xC8) = 0;
    }
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_m100 + 0x210), *(uint64_t *)(local_rsp - 0x68 - 0x70), v_stack_m100 + 544, Arg4);
    result = Feature_Test57481295__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_stack_m100 + 0x210), *(uint64_t *)(local_rsp - 0x68 - 0x70), v_stack_m100 + 544, Arg4);
    if (!sign_flag) goto loc_00706D2C;
    if (*(uint64_t *)(local_rsp - 0x68 + 0xC0) == 0) goto loc_00706D15;
    if ((uint32_t)(result) == 0) goto loc_00706CE9;
    if (v_stack_m108 != 1) goto loc_00706D15;
    goto loc_00706CF2;
loc_00706CE9:
    if ((*(uint8_t *)(v_rip + 0x8BD288)) == 0) goto loc_00706D15;
loc_00706CF2:
    Arg2 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_m100 + 0x210), Arg2, v_stack_m100 + 544, Arg4);
    if (!sign_flag) goto loc_00706D2C;
loc_00706D15:
    if (0 == 2) goto loc_00706D33;
    if (((uint32_t)((uint32_t)(v_stack_m114))) == 1) goto loc_00706D87;
    goto loc_00706D3D;
loc_00706D2C:
    *(uint32_t *)(v_stack_m100 + 0x208) = 1;
loc_00706D33:
loc_00706D3D:
    result = HalJoinDmaDomain(v_stack_m100, local_rbx, v_stack_m100 + 544, Arg4);
    if (!sign_flag) goto loc_00706D9E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x208))) == 0) goto loc_00706D87;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x208)))) != 2) goto loc_00706D6C;
    goto loc_00706D71;
loc_00706D6C:
    if (((uint32_t)((uint32_t)(v_stack_m114))) == 1) goto loc_00706D87;
loc_00706D71:
    result = HalJoinDmaDomain(v_stack_m100, local_rbx, v_stack_m100 + 544, Arg4);
    if (!sign_flag) goto loc_00706D9E;
loc_00706D87:
    result = ObfDereferenceObject(v_stack_m100, local_rbx, v_stack_m100 + 544, Arg4);
    local_rsi = 0;
    v_stack_m100 = 0;
    goto loc_00706DBF;
loc_00706D9E:
    if (result == 0) goto loc_00706DB4;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x68 + 0xC8)) != 0) {
        *(uint8_t *)(result + 0x15A) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(local_rsi + 0x200) + 0x38) = 0;
loc_00706DBF:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x68 + 0xC8)) == 0) goto loc_0070694B;
    local_rbx = (uint8_t)((local_rbx) & (6));
    result = *(uint64_t *)(local_rsi + 0x200);
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = result + 320;
        result = ExfTryToWakePushLock(Arg1, local_rbx, v_stack_m100 + 544, Arg4);
    }
    result = KeAbPostRelease(result + 320, local_rbx, v_stack_m100 + 544, Arg4);
    result = ObfDereferenceObject(result, local_rbx, v_stack_m100 + 544, Arg4);
    goto loc_0070694B;
loc_00706DFD:
    result = HalpDmaIsThinDmaCapable(result, local_rbx, v_stack_m100 + 544, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00706E11;
loc_00706E0D:
    *(uint64_t *)(v_stack_m100 + 0x8) = v_rip - 7338573;
loc_00706E11:
    local_rsp = (local_rsp) + (296);
    return v_stack_m100;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007066A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
