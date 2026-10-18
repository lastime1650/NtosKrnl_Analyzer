# ExpGetProcessInformation

- RVA: `0x0091A878`–`0x0091BC99` (길이 `5,153` bytes)
- VA: `0x000000014091A878`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008AE3C`
- 디코드: `1,055`개 명령, `5,153/5,153` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x0091A8DF` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091A90E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091A94D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091A9F9` → [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) (function, `0x00A217E8`)
- `0x0091AA27` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (function, `0x00225710`)
- `0x0091AA76` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091AAB8` → [ExpGetNextProcessThread](ExpGetNextProcessThread_function_0091BCA0.md) (function, `0x0091BCA0`)
- `0x0091AB29` → [KeQueryValuesThread](../../text/30/KeQueryValuesThread_function_0030EE30.md) (function, `0x0030EE30`)
- `0x0091ADC2` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x0091ADD4` → [SeSecurityAttributePresent](../../text/21/SeSecurityAttributePresent_function_00213660.md) (function, `0x00213660`)
- `0x0091ADED` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)
- `0x0091AE9D` → [PsQueryProcessEnergyValues](PsQueryProcessEnergyValues_function_0091A4E0.md) (function, `0x0091A4E0`)
- `0x0091B177` → [ExGetNextProcess](ExGetNextProcess_function_0091CAD0.md) (function, `0x0091CAD0`)
- `0x0091B190` → [ExpSysInfoShouldSkipProcess](ExpSysInfoShouldSkipProcess_function_0091BE50.md) (function, `0x0091BE50`)
- `0x0091B1AE` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (function, `0x002233A0`)
- `0x0091B1D8` → [PsIsProcessInSilo](../../text/41/PsIsProcessInSilo_function_004185E0.md) (function, `0x004185E0`)
- `0x0091B2C1` → [PsGetProcessActiveThreadCount](../../text/4C/PsGetProcessActiveThreadCount_function_004C0240.md) (function, `0x004C0240`)
- `0x0091B2D1` → [ObGetProcessHandleCount](ObGetProcessHandleCount_function_009195D0.md) (function, `0x009195D0`)
- `0x0091B37D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0091B404` → [ExpCopyProcessInfo](ExpCopyProcessInfo_function_00919134.md) (function, `0x00919134`)
- `0x0091B6CF` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x0091B710` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0091B73C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0091B745` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0091B74A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0091B79C` → [RtlQueryPackageIdentity](../../text/45/RtlQueryPackageIdentity_function_0045C390.md) (function, `0x0045C390`)
- `0x0091B7C2` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)
- `0x0091B8BC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0091B949` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0091BACD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0091BB7D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0091BC2B` → [ExCheckFullProcessInformationAccess](../95/ExCheckFullProcessInformationAccess_function_0095D93C.md) (function, `0x0095D93C`)
- `0x0091BC4A` → [KeFlushProcessWriteBuffers](../../text/2C/KeFlushProcessWriteBuffers_function_002CE4FC.md) (function, `0x002CE4FC`)
- `0x0091BC69` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0091BC8F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5B76E`

### Static image references
- `0x0091A893` → RVA `0x00E0A740` (`.data`; read)
- `0x0091AA34` → RVA `0x00FC6B70` (`ALMOSTRO`; read)
- `0x0091AB77` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x0091ADCA` → RVA `0x00B4BEA8` (`PspSysAppIdClaim`; read)
- `0x0091AF40` → RVA `0x00FC6B78` (`ALMOSTRO`; read)
- `0x0091AF5C` → RVA `0x00FC5518` (`ALMOSTRO`; read)
- `0x0091AF7A` → RVA `0x00FC6AA6` (`ALMOSTRO`; read)
- `0x0091AF9B` → RVA `0x00FC6CB8` (`ALMOSTRO`; read)
- `0x0091AFB8` → RVA `0x00EF7208` (`.data`; read)
- `0x0091B0A0` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x0091B0AD` → RVA `0x00001FF8` (`.rdata`; read)
- `0x0091B33A` → RVA `0x00002018` (`.rdata`; read)
- `0x0091B448` → RVA `0x00E2DCE8` (`.data`; read)
- `0x0091BB28` → RVA `0x00002048` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x0091A8DF` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091A90E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091A94D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091AA27` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (`PAGE` → `.text`)
  - `0x0091AA76` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091AB29` → [KeQueryValuesThread](../../text/30/KeQueryValuesThread_function_0030EE30.md) (`PAGE` → `.text`)
  - `0x0091ADC2` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x0091ADD4` → [SeSecurityAttributePresent](../../text/21/SeSecurityAttributePresent_function_00213660.md) (`PAGE` → `.text`)
  - `0x0091ADED` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`PAGE` → `.text`)
  - `0x0091B1AE` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (`PAGE` → `.text`)
  - `0x0091B1D8` → [PsIsProcessInSilo](../../text/41/PsIsProcessInSilo_function_004185E0.md) (`PAGE` → `.text`)
  - `0x0091B2C1` → [PsGetProcessActiveThreadCount](../../text/4C/PsGetProcessActiveThreadCount_function_004C0240.md) (`PAGE` → `.text`)
  - `0x0091B37D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0091B6CF` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x0091B710` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0091B73C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0091B745` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0091B74A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0091B79C` → [RtlQueryPackageIdentity](../../text/45/RtlQueryPackageIdentity_function_0045C390.md) (`PAGE` → `.text`)
  - `0x0091B7C2` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`PAGE` → `.text`)
  - `0x0091B8BC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0091B949` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0091BACD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0091BB7D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0091BC4A` → [KeFlushProcessWriteBuffers](../../text/2C/KeFlushProcessWriteBuffers_function_002CE4FC.md) (`PAGE` → `.text`)
  - `0x0091BC69` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0091BC8F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0091BC18` → [sub_00B21BB0](../B2/Unknown_function_00B21BB0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0091A878  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0091A87D  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0091A881  53                              push rbx
0091A882  56                              push rsi
0091A883  57                              push rdi
0091A884  41 54                           push r12
0091A886  41 55                           push r13
0091A888  41 56                           push r14
0091A88A  41 57                           push r15
0091A88C  48 81 EC 00 06 00 00            sub rsp, 0x600
0091A893  48 8B 05 A6 FE 4E 00            mov rax, qword ptr [rip + 0x4efea6]
0091A89A  48 33 C4                        xor rax, rsp
0091A89D  48 89 84 24 F0 05 00 00         mov qword ptr [rsp + 0x5f0], rax
0091A8A5  49 8B D8                        mov rbx, r8
0091A8A8  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
0091A8AD  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
0091A8B5  48 89 8C 24 68 01 00 00         mov qword ptr [rsp + 0x168], rcx
0091A8BD  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
0091A8C5  33 FF                           xor edi, edi
0091A8C7  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
0091A8CF  33 D2                           xor edx, edx
0091A8D1  41 B8 B8 01 00 00               mov r8d, 0x1b8
0091A8D7  48 8D 8C 24 A0 02 00 00         lea rcx, [rsp + 0x2a0]
0091A8DF  E8 5C C3 DA FF                  call 0x1406c6c40
0091A8E4  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
0091A8E8  89 BC 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], edi
0091A8EF  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
0091A8F3  48 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdi
0091A8FB  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
0091A900  33 D2                           xor edx, edx
0091A902  44 8D 47 68                     lea r8d, [rdi + 0x68]
0091A906  48 8D 8C 24 E0 01 00 00         lea rcx, [rsp + 0x1e0]
0091A90E  E8 2D C3 DA FF                  call 0x1406c6c40
0091A913  40 88 7C 24 50                  mov byte ptr [rsp + 0x50], dil
0091A918  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
0091A920  0F 57 C0                        xorps xmm0, xmm0
0091A923  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
0091A92B  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
0091A933  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
0091A937  48 89 BC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rdi
0091A93F  33 D2                           xor edx, edx
0091A941  44 8D 47 44                     lea r8d, [rdi + 0x44]
0091A945  48 8D 8C 24 50 02 00 00         lea rcx, [rsp + 0x250]
0091A94D  E8 EE C2 DA FF                  call 0x1406c6c40
0091A952  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0091A957  89 BC 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edi
0091A95E  48 85 DB                        test rbx, rbx
0091A961  74 02                           je 0x14091a965
0091A963  89 3B                           mov dword ptr [rbx], edi
0091A965  44 8B A4 24 60 06 00 00         mov r12d, dword ptr [rsp + 0x660]
0091A96D  41 81 FC FC 00 00 00            cmp r12d, 0xfc
0091A974  0F 85 1C 12 00 00               jne 0x14091bb96
0091A97A  40 88 7C 24 3C                  mov byte ptr [rsp + 0x3c], dil
0091A97F  C7 84 24 80 00 00 00 30 00 00 00  mov dword ptr [rsp + 0x80], 0x30
0091A98A  89 7C 24 7C                     mov dword ptr [rsp + 0x7c], edi
0091A98E  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0091A996  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
0091A99E  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
0091A9A6  48 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdi
0091A9AE  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
0091A9B5  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
0091A9BC  39 84 24 48 06 00 00            cmp dword ptr [rsp + 0x648], eax
0091A9C3  0F 82 4C 12 00 00               jb 0x14091bc15
0091A9C9  1B DB                           sbb ebx, ebx
0091A9CB  81 E3 04 00 00 C0               and ebx, 0xc0000004
0091A9D1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0091A9DA  40 8A B0 32 02 00 00            mov sil, byte ptr [rax + 0x232]
0091A9E1  41 81 FC 94 00 00 00            cmp r12d, 0x94
0091A9E8  0F 84 3A 12 00 00               je 0x14091bc28
0091A9EE  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
0091A9F6  40 8A CE                        mov cl, sil
0091A9F9  E8 EA 6D 10 00                  call 0x140a217e8
0091A9FE  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
0091AA05  85 C0                           test eax, eax
0091AA07  0F 95 44 24 73                  setne byte ptr [rsp + 0x73]
0091AA0C  8B F7                           mov esi, edi
0091AA0E  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
0091AA12  41 8D 84 24 04 FF FF FF         lea eax, [r12 - 0xfc]
0091AA1A  B9 01 00 00 00                  mov ecx, 1
0091AA1F  3B C1                           cmp eax, ecx
0091AA21  0F 87 16 12 00 00               ja 0x14091bc3d
0091AA27  E8 E4 AC 90 FF                  call 0x140225710
0091AA2C  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
0091AA34  4C 8B 2D 35 C1 6A 00            mov r13, qword ptr [rip + 0x6ac135]
0091AA3B  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
0091AA40  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
0091AA44  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091AA49  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091AA4E  E9 31 07 00 00                  jmp 0x14091b184
0091AA53  44 8B F1                        mov r14d, ecx
0091AA56  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
0091AA5A  8B F7                           mov esi, edi
0091AA5C  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0091AA60  85 F6                           test esi, esi
0091AA62  0F 88 B1 08 00 00               js 0x14091b319
0091AA68  33 D2                           xor edx, edx
0091AA6A  44 8D 42 68                     lea r8d, [rdx + 0x68]
0091AA6E  48 8D 8C 24 E0 01 00 00         lea rcx, [rsp + 0x1e0]
0091AA76  E8 C5 C1 DA FF                  call 0x1406c6c40
0091AA7B  44 3B B4 24 48 06 00 00         cmp r14d, dword ptr [rsp + 0x648]
0091AA83  0F 86 63 09 00 00               jbe 0x14091b3ec
0091AA89  C7 44 24 30 04 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000004
0091AA91  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0091AA96  48 85 DB                        test rbx, rbx
0091AA99  0F 84 B5 10 00 00               je 0x14091bb54
0091AA9F  4C 8B BC 24 90 00 00 00         mov r15, qword ptr [rsp + 0x90]
0091AAA7  49 81 C7 00 01 00 00            add r15, 0x100
0091AAAE  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0091AAB3  33 D2                           xor edx, edx
0091AAB5  49 8B CD                        mov rcx, r13
0091AAB8  E8 E3 11 00 00                  call 0x14091bca0
0091AABD  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0091AAC5  4C 8B C0                        mov r8, rax
0091AAC8  48 85 C0                        test rax, rax
0091AACB  0F 84 C8 02 00 00               je 0x14091ad99
0091AAD1  40 38 78 04                     cmp byte ptr [rax + 4], dil
0091AAD5  74 0A                           je 0x14091aae1
0091AAD7  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0091AADF  EB D4                           jmp 0x14091aab5
0091AAE1  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
0091AAE5  41 8D 0C 06                     lea ecx, [r14 + rax]
0091AAE9  41 3B CE                        cmp ecx, r14d
0091AAEC  0F 82 94 02 00 00               jb 0x14091ad86
0091AAF2  44 8B F1                        mov r14d, ecx
0091AAF5  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
0091AAF9  8B F7                           mov esi, edi
0091AAFB  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0091AAFF  85 F6                           test esi, esi
0091AB01  0F 88 12 08 00 00               js 0x14091b319
0091AB07  01 44 24 40                     add dword ptr [rsp + 0x40], eax
0091AB0B  44 3B B4 24 48 06 00 00         cmp r14d, dword ptr [rsp + 0x648]
0091AB13  0F 87 3A 08 00 00               ja 0x14091b353
0091AB19  48 8D 94 24 08 01 00 00         lea rdx, [rsp + 0x108]
0091AB21  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0091AB29  E8 02 43 9F FF                  call 0x14030ee30
0091AB2E  80 BC 24 10 01 00 00 04         cmp byte ptr [rsp + 0x110], 4
0091AB36  0F 84 49 0F 00 00               je 0x14091ba85
0091AB3C  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
0091AB43  41 89 47 18                     mov dword ptr [r15 + 0x18], eax
0091AB47  0F B6 84 24 10 01 00 00         movzx eax, byte ptr [rsp + 0x110]
0091AB4F  41 89 47 44                     mov dword ptr [r15 + 0x44], eax
0091AB53  0F B6 84 24 11 01 00 00         movzx eax, byte ptr [rsp + 0x111]
0091AB5B  41 89 47 48                     mov dword ptr [r15 + 0x48], eax
0091AB5F  0F BE 84 24 12 01 00 00         movsx eax, byte ptr [rsp + 0x112]
0091AB67  41 89 47 38                     mov dword ptr [r15 + 0x38], eax
0091AB6B  0F BE 84 24 13 01 00 00         movsx eax, byte ptr [rsp + 0x113]
0091AB73  41 89 47 3C                     mov dword ptr [r15 + 0x3c], eax
0091AB77  8B 0D 23 BF 6A 00               mov ecx, dword ptr [rip + 0x6abf23]
0091AB7D  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
0091AB85  41 8B 80 8C 02 00 00            mov eax, dword ptr [r8 + 0x28c]
0091AB8C  48 0F AF C1                     imul rax, rcx
0091AB90  49 89 07                        mov qword ptr [r15], rax
0091AB93  41 8B 80 DC 02 00 00            mov eax, dword ptr [r8 + 0x2dc]
0091AB9A  48 0F AF C1                     imul rax, rcx
0091AB9E  49 89 47 08                     mov qword ptr [r15 + 8], rax
0091ABA2  49 8B 80 C0 04 00 00            mov rax, qword ptr [r8 + 0x4c0]
0091ABA9  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
0091ABAD  41 8B 80 54 01 00 00            mov eax, dword ptr [r8 + 0x154]
0091ABB4  41 89 47 40                     mov dword ptr [r15 + 0x40], eax
0091ABB8  41 0F 10 80 08 05 00 00         movups xmm0, xmmword ptr [r8 + 0x508]
0091ABC0  F3 41 0F 7F 47 28               movdqu xmmword ptr [r15 + 0x28], xmm0
0091ABC6  41 F7 40 74 00 04 00 00         test dword ptr [r8 + 0x74], 0x400
0091ABCE  0F 85 22 01 00 00               jne 0x14091acf6
0091ABD4  41 8B 80 A8 05 00 00            mov eax, dword ptr [r8 + 0x5a8]
0091ABDB  A8 08                           test al, 8
0091ABDD  0F 85 C0 00 00 00               jne 0x14091aca3
0091ABE3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0091ABEB  48 8B 88 E0 04 00 00            mov rcx, qword ptr [rax + 0x4e0]
0091ABF2  F0 09 3C 24                     lock or dword ptr [rsp], edi
0091ABF6  41 8B 80 A8 05 00 00            mov eax, dword ptr [r8 + 0x5a8]
0091ABFD  A8 08                           test al, 8
0091ABFF  48 8B C7                        mov rax, rdi
0091AC02  48 0F 44 C1                     cmove rax, rcx
0091AC06  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091AC0B  8B 74 24 38                     mov esi, dword ptr [rsp + 0x38]
0091AC0F  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091AC14  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091AC19  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
0091AC21  48 BA FF FF FE FF FF 7F 00 00   movabs rdx, 0x7ffffffeffff
0091AC2B  39 BC 24 A0 00 00 00            cmp dword ptr [rsp + 0xa0], edi
0091AC32  74 77                           je 0x14091acab
0091AC34  49 89 7F 20                     mov qword ptr [r15 + 0x20], rdi
0091AC38  40 38 7C 24 3C                  cmp byte ptr [rsp + 0x3c], dil
0091AC3D  0F 84 ED 00 00 00               je 0x14091ad30
0091AC43  39 BC 24 A0 00 00 00            cmp dword ptr [rsp + 0xa0], edi
0091AC4A  74 71                           je 0x14091acbd
0091AC4C  49 89 7F 50                     mov qword ptr [r15 + 0x50], rdi
0091AC50  49 89 7F 58                     mov qword ptr [r15 + 0x58], rdi
0091AC54  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0091AC5C  48 8B 88 60 05 00 00            mov rcx, qword ptr [rax + 0x560]
0091AC63  48 89 8C 24 00 01 00 00         mov qword ptr [rsp + 0x100], rcx
0091AC6B  39 BC 24 A0 00 00 00            cmp dword ptr [rsp + 0xa0], edi
0091AC72  0F 84 9D 00 00 00               je 0x14091ad15
0091AC78  49 89 7F 60                     mov qword ptr [r15 + 0x60], rdi
0091AC7C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0091AC84  48 8B 88 F0 00 00 00            mov rcx, qword ptr [rax + 0xf0]
0091AC8B  49 89 4F 68                     mov qword ptr [r15 + 0x68], rcx
0091AC8F  49 89 7F 70                     mov qword ptr [r15 + 0x70], rdi
0091AC93  49 89 7F 78                     mov qword ptr [r15 + 0x78], rdi
0091AC97  49 89 BF 80 00 00 00            mov qword ptr [r15 + 0x80], rdi
0091AC9E  E9 8D 00 00 00                  jmp 0x14091ad30
0091ACA3  48 8B C7                        mov rax, rdi
0091ACA6  E9 5B FF FF FF                  jmp 0x14091ac06
0091ACAB  39 BC 24 B8 00 00 00            cmp dword ptr [rsp + 0xb8], edi
0091ACB2  75 56                           jne 0x14091ad0a
0091ACB4  49 89 47 20                     mov qword ptr [r15 + 0x20], rax
0091ACB8  E9 7B FF FF FF                  jmp 0x14091ac38
0091ACBD  39 BC 24 B8 00 00 00            cmp dword ptr [rsp + 0xb8], edi
0091ACC4  75 86                           jne 0x14091ac4c
0091ACC6  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
0091ACCE  49 8B 40 38                     mov rax, qword ptr [r8 + 0x38]
0091ACD2  49 89 47 50                     mov qword ptr [r15 + 0x50], rax
0091ACD6  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
0091ACDA  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091ACDF  49 89 47 58                     mov qword ptr [r15 + 0x58], rax
0091ACE3  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091ACE8  8B 74 24 38                     mov esi, dword ptr [rsp + 0x38]
0091ACEC  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091ACF1  E9 5E FF FF FF                  jmp 0x14091ac54
0091ACF6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0091ACFE  48 8B 80 60 05 00 00            mov rax, qword ptr [rax + 0x560]
0091AD05  E9 0F FF FF FF                  jmp 0x14091ac19
0091AD0A  48 3B C2                        cmp rax, rdx
0091AD0D  0F 87 21 FF FF FF               ja 0x14091ac34
0091AD13  EB 9F                           jmp 0x14091acb4
0091AD15  39 BC 24 B8 00 00 00            cmp dword ptr [rsp + 0xb8], edi
0091AD1C  74 09                           je 0x14091ad27
0091AD1E  48 3B CA                        cmp rcx, rdx
0091AD21  0F 87 51 FF FF FF               ja 0x14091ac78
0091AD27  49 89 4F 60                     mov qword ptr [r15 + 0x60], rcx
0091AD2B  E9 4C FF FF FF                  jmp 0x14091ac7c
0091AD30  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0091AD38  8B 41 04                        mov eax, dword ptr [rcx + 4]
0091AD3B  FF C0                           inc eax
0091AD3D  89 41 04                        mov dword ptr [rcx + 4], eax
0091AD40  EB 2B                           jmp 0x14091ad6d
0091AD42  8B F0                           mov esi, eax
0091AD44  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
0091AD4B  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091AD4F  33 FF                           xor edi, edi
0091AD51  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091AD56  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091AD5B  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091AD60  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
0091AD68  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
0091AD6D  85 F6                           test esi, esi
0091AD6F  0F 88 A4 05 00 00               js 0x14091b319
0091AD75  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
0091AD79  4C 03 F8                        add r15, rax
0091AD7C  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0091AD81  E9 51 FD FF FF                  jmp 0x14091aad7
0091AD86  41 83 CE FF                     or r14d, 0xffffffff
0091AD8A  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0091AD8F  BE 95 00 00 C0                  mov esi, 0xc0000095
0091AD94  E9 62 FD FF FF                  jmp 0x14091aafb
0091AD99  4D 8B E7                        mov r12, r15
0091AD9C  4C 89 BC 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r15
0091ADA4  49 81 C7 70 01 00 00            add r15, 0x170
0091ADAB  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0091ADB0  39 7C 24 30                     cmp dword ptr [rsp + 0x30], edi
0091ADB4  0F 8C AF 02 00 00               jl 0x14091b069
0091ADBA  BA 44 66 6C 74                  mov edx, 0x746c6644
0091ADBF  49 8B CD                        mov rcx, r13
0091ADC2  E8 B9 51 8F FF                  call 0x14020ff80
0091ADC7  48 8B D8                        mov rbx, rax
0091ADCA  48 8D 15 D7 10 23 00            lea rdx, [rip + 0x2310d7]
0091ADD1  48 8B C8                        mov rcx, rax
0091ADD4  E8 87 88 8F FF                  call 0x140213660
0091ADD9  88 44 24 50                     mov byte ptr [rsp + 0x50], al
0091ADDD  49 8D 8D 48 02 00 00            lea rcx, [r13 + 0x248]
0091ADE4  41 B8 44 66 6C 74               mov r8d, 0x746c6644
0091ADEA  48 8B D3                        mov rdx, rbx
0091ADED  E8 FE 27 AD FF                  call 0x1403ed5f0
0091ADF2  90                              nop
0091ADF3  49 83 64 24 34 00               and qword ptr [r12 + 0x34], 0
0091ADF9  41 89 BC 24 50 01 00 00         mov dword ptr [r12 + 0x150], edi
0091AE01  49 8B 85 A8 06 00 00            mov rax, qword ptr [r13 + 0x6a8]
0091AE08  48 C1 E0 0C                     shl rax, 0xc
0091AE0C  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
0091AE14  48 89 83 58 01 00 00            mov qword ptr [rbx + 0x158], rax
0091AE1B  48 8B 84 24 00 02 00 00         mov rax, qword ptr [rsp + 0x200]
0091AE23  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
0091AE27  89 7B 30                        mov dword ptr [rbx + 0x30], edi
0091AE2A  41 BE 01 00 00 00               mov r14d, 1
0091AE30  40 38 7C 24 50                  cmp byte ptr [rsp + 0x50], dil
0091AE35  0F 85 DE 01 00 00               jne 0x14091b019
0091AE3B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0091AE40  48 8B 86 38 06 00 00            mov rax, qword ptr [rsi + 0x638]
0091AE47  48 85 C0                        test rax, rax
0091AE4A  0F 84 A7 01 00 00               je 0x14091aff7
0091AE50  0F 10 00                        movups xmm0, xmmword ptr [rax]
0091AE53  0F 11 03                        movups xmmword ptr [rbx], xmm0
0091AE56  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
0091AE5A  0F 11 4B 10                     movups xmmword ptr [rbx + 0x10], xmm1
0091AE5E  F2 0F 10 40 20                  movsd xmm0, qword ptr [rax + 0x20]
0091AE63  F2 0F 11 43 20                  movsd qword ptr [rbx + 0x20], xmm0
0091AE68  8B 8E FC 05 00 00               mov ecx, dword ptr [rsi + 0x5fc]
0091AE6E  0F BA E1 0C                     bt ecx, 0xc
0091AE72  0F 83 23 01 00 00               jae 0x14091af9b
0091AE78  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0091AE7B  83 E0 E3                        and eax, 0xffffffe3
0091AE7E  83 C8 02                        or eax, 2
0091AE81  89 43 30                        mov dword ptr [rbx + 0x30], eax
0091AE84  48 8B 86 78 06 00 00            mov rax, qword ptr [rsi + 0x678]
0091AE8B  48 89 83 68 01 00 00            mov qword ptr [rbx + 0x168], rax
0091AE92  48 8D 94 24 A0 02 00 00         lea rdx, [rsp + 0x2a0]
0091AE9A  48 8B CE                        mov rcx, rsi
0091AE9D  E8 3E F6 FF FF                  call 0x14091a4e0
0091AEA2  48 8D 43 40                     lea rax, [rbx + 0x40]
0091AEA6  48 8D 8C 24 A0 02 00 00         lea rcx, [rsp + 0x2a0]
0091AEAE  BA 02 00 00 00                  mov edx, 2
0091AEB3  0F 10 01                        movups xmm0, xmmword ptr [rcx]
0091AEB6  0F 11 00                        movups xmmword ptr [rax], xmm0
0091AEB9  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
0091AEBD  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
0091AEC1  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
0091AEC5  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
0091AEC9  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
0091AECD  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
0091AED1  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
0091AED5  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
0091AED9  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
0091AEDD  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
0091AEE1  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
0091AEE5  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
0091AEE9  48 8D 80 80 00 00 00            lea rax, [rax + 0x80]
0091AEF0  0F 10 49 70                     movups xmm1, xmmword ptr [rcx + 0x70]
0091AEF4  0F 11 48 F0                     movups xmmword ptr [rax - 0x10], xmm1
0091AEF8  48 8D 89 80 00 00 00            lea rcx, [rcx + 0x80]
0091AEFF  48 83 EA 01                     sub rdx, 1
0091AF03  75 AE                           jne 0x14091aeb3
0091AF05  0F 10 01                        movups xmm0, xmmword ptr [rcx]
0091AF08  0F 11 00                        movups xmmword ptr [rax], xmm0
0091AF0B  48 8B 86 A0 02 00 00            mov rax, qword ptr [rsi + 0x2a0]
0091AF12  48 85 C0                        test rax, rax
0091AF15  0F 84 CF 00 00 00               je 0x14091afea
0091AF1B  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0091AF20  48 8B 88 A0 02 00 00            mov rcx, qword ptr [rax + 0x2a0]
0091AF27  8B 81 BC 05 00 00               mov eax, dword ptr [rcx + 0x5bc]
0091AF2D  41 89 84 24 60 01 00 00         mov dword ptr [r12 + 0x160], eax
0091AF35  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091AF3A  41 39 7D 44                     cmp dword ptr [r13 + 0x44], edi
0091AF3E  75 52                           jne 0x14091af92
0091AF40  8B 05 32 BC 6A 00               mov eax, dword ptr [rip + 0x6abc32]
0091AF46  85 C0                           test eax, eax
0091AF48  0F 84 E2 00 00 00               je 0x14091b030
0091AF4E  41 8B 85 88 00 00 00            mov eax, dword ptr [r13 + 0x88]
0091AF55  48 C1 E8 07                     shr rax, 7
0091AF59  83 E0 0F                        and eax, 0xf
0091AF5C  48 8D 15 B5 A5 6A 00            lea rdx, [rip + 0x6aa5b5]
0091AF63  8B 14 82                        mov edx, dword ptr [rdx + rax*4]
0091AF66  83 FA 07                        cmp edx, 7
0091AF69  75 0C                           jne 0x14091af77
0091AF6B  45 38 B5 47 03 00 00            cmp byte ptr [r13 + 0x347], r14b
0091AF72  41 8A CE                        mov cl, r14b
0091AF75  74 03                           je 0x14091af7a
0091AF77  40 8A CF                        mov cl, dil
0091AF7A  8A 05 26 BB 6A 00               mov al, byte ptr [rip + 0x6abb26]
0091AF80  84 C0                           test al, al
0091AF82  0F 84 A8 00 00 00               je 0x14091b030
0091AF88  8D 42 FF                        lea eax, [rdx - 1]
0091AF8B  A9 FA FF FF FF                  test eax, 0xfffffffa
0091AF90  75 52                           jne 0x14091afe4
0091AF92  83 4B 30 20                     or dword ptr [rbx + 0x30], 0x20
0091AF96  E9 95 00 00 00                  jmp 0x14091b030
0091AF9B  48 3B 35 16 BD 6A 00            cmp rsi, qword ptr [rip + 0x6abd16]
0091AFA2  74 7E                           je 0x14091b022
0091AFA4  0F BA E1 1E                     bt ecx, 0x1e
0091AFA8  73 0E                           jae 0x14091afb8
0091AFAA  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0091AFAD  83 E0 E7                        and eax, 0xffffffe7
0091AFB0  83 C8 06                        or eax, 6
0091AFB3  E9 C9 FE FF FF                  jmp 0x14091ae81
0091AFB8  48 8B 05 49 C2 5D 00            mov rax, qword ptr [rip + 0x5dc249]
0091AFBF  48 85 C0                        test rax, rax
0091AFC2  74 48                           je 0x14091b00c
0091AFC4  48 3B F0                        cmp rsi, rax
0091AFC7  0F 94 C1                        sete cl
0091AFCA  88 4C 24 6C                     mov byte ptr [rsp + 0x6c], cl
0091AFCE  41 8B 44 24 30                  mov eax, dword ptr [r12 + 0x30]
0091AFD3  84 C9                           test cl, cl
0091AFD5  75 3A                           jne 0x14091b011
0091AFD7  83 E0 E1                        and eax, 0xffffffe1
0091AFDA  41 89 44 24 30                  mov dword ptr [r12 + 0x30], eax
0091AFDF  E9 A0 FE FF FF                  jmp 0x14091ae84
0091AFE4  84 C9                           test cl, cl
0091AFE6  74 48                           je 0x14091b030
0091AFE8  EB A8                           jmp 0x14091af92
0091AFEA  41 89 BC 24 60 01 00 00         mov dword ptr [r12 + 0x160], edi
0091AFF2  E9 3E FF FF FF                  jmp 0x14091af35
0091AFF7  0F 57 C0                        xorps xmm0, xmm0
0091AFFA  33 C0                           xor eax, eax
0091AFFC  0F 11 03                        movups xmmword ptr [rbx], xmm0
0091AFFF  0F 11 43 10                     movups xmmword ptr [rbx + 0x10], xmm0
0091B003  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
0091B007  E9 5C FE FF FF                  jmp 0x14091ae68
0091B00C  40 8A CF                        mov cl, dil
0091B00F  EB B9                           jmp 0x14091afca
0091B011  83 E0 E9                        and eax, 0xffffffe9
0091B014  83 C8 08                        or eax, 8
0091B017  EB C1                           jmp 0x14091afda
0091B019  44 89 73 30                     mov dword ptr [rbx + 0x30], r14d
0091B01D  E9 19 FE FF FF                  jmp 0x14091ae3b
0091B022  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0091B025  83 E0 E5                        and eax, 0xffffffe5
0091B028  83 C8 04                        or eax, 4
0091B02B  E9 51 FE FF FF                  jmp 0x14091ae81
0091B030  8B 74 24 38                     mov esi, dword ptr [rsp + 0x38]
0091B034  EB 21                           jmp 0x14091b057
0091B036  8B F0                           mov esi, eax
0091B038  89 84 24 D0 01 00 00            mov dword ptr [rsp + 0x1d0], eax
0091B03F  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B043  33 FF                           xor edi, edi
0091B045  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B04A  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0091B052  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0091B057  85 F6                           test esi, esi
0091B059  0F 88 BA 02 00 00               js 0x14091b319
0091B05F  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B064  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091B069  44 8B A4 24 60 06 00 00         mov r12d, dword ptr [rsp + 0x660]
0091B071  41 81 FC 94 00 00 00            cmp r12d, 0x94
0091B078  0F 84 49 06 00 00               je 0x14091b6c7
0091B07E  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
0091B083  41 81 FC FD 00 00 00            cmp r12d, 0xfd
0091B08A  0F 84 D5 00 00 00               je 0x14091b165
0091B090  48 8B 05 D9 BA 6A 00            mov rax, qword ptr [rip + 0x6abad9]
0091B097  4C 3B E8                        cmp r13, rax
0091B09A  0F 84 BB 00 00 00               je 0x14091b15b
0091B0A0  4C 3B 2D 09 BA 6A 00            cmp r13, qword ptr [rip + 0x6aba09]
0091B0A7  0F 85 75 02 00 00               jne 0x14091b322
0091B0AD  48 8D 05 44 6F 6E FF            lea rax, [rip - 0x9190bc]
0091B0B4  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
0091B0BC  0F B7 08                        movzx ecx, word ptr [rax]
0091B0BF  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0091B0C3  89 8C 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], ecx
0091B0CA  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
0091B0CE  49 8B D0                        mov rdx, r8
0091B0D1  48 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdx
0091B0D9  44 8B E1                        mov r12d, ecx
0091B0DC  44 8B 8C 24 60 06 00 00         mov r9d, dword ptr [rsp + 0x660]
0091B0E4  41 81 F9 94 00 00 00            cmp r9d, 0x94
0091B0EB  0F 85 65 01 00 00               jne 0x14091b256
0091B0F1  41 83 C4 09                     add r12d, 9
0091B0F5  41 83 E4 F8                     and r12d, 0xfffffff8
0091B0F9  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
0091B0FE  47 8D 04 26                     lea r8d, [r14 + r12]
0091B102  43 8D 04 34                     lea eax, [r12 + r14]
0091B106  41 3B C6                        cmp eax, r14d
0091B109  0F 82 34 01 00 00               jb 0x14091b243
0091B10F  45 8B F0                        mov r14d, r8d
0091B112  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
0091B117  8B F7                           mov esi, edi
0091B119  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0091B11D  85 F6                           test esi, esi
0091B11F  0F 88 F4 01 00 00               js 0x14091b319
0091B125  44 01 64 24 40                  add dword ptr [rsp + 0x40], r12d
0091B12A  44 3B B4 24 48 06 00 00         cmp r14d, dword ptr [rsp + 0x648]
0091B132  0F 86 31 02 00 00               jbe 0x14091b369
0091B138  C7 44 24 30 04 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000004
0091B140  4D 85 D2                        test r10, r10
0091B143  0F 84 0B 0A 00 00               je 0x14091bb54
0091B149  39 7C 24 30                     cmp dword ptr [rsp + 0x30], edi
0091B14D  0F 8D 4D 03 00 00               jge 0x14091b4a0
0091B153  44 8B A4 24 60 06 00 00         mov r12d, dword ptr [rsp + 0x660]
0091B15B  39 7C 24 30                     cmp dword ptr [rsp + 0x30], edi
0091B15F  0F 8D B4 03 00 00               jge 0x14091b519
0091B165  4C 3B 2D 04 BA 6A 00            cmp r13, qword ptr [rip + 0x6aba04]
0091B16C  4C 0F 44 EF                     cmove r13, rdi
0091B170  8A 54 24 73                     mov dl, byte ptr [rsp + 0x73]
0091B174  49 8B CD                        mov rcx, r13
0091B177  E8 54 19 00 00                  call 0x14091cad0
0091B17C  4C 8B E8                        mov r13, rax
0091B17F  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0091B184  4D 85 ED                        test r13, r13
0091B187  0F 84 C5 04 00 00               je 0x14091b652
0091B18D  49 8B CD                        mov rcx, r13
0091B190  E8 BB 0C 00 00                  call 0x14091be50
0091B195  84 C0                           test al, al
0091B197  0F 85 9D 04 00 00               jne 0x14091b63a
0091B19D  48 39 BC 24 58 06 00 00         cmp qword ptr [rsp + 0x658], rdi
0091B1A5  0F 85 94 08 00 00               jne 0x14091ba3f
0091B1AB  49 8B CD                        mov rcx, r13
0091B1AE  E8 ED 81 90 FF                  call 0x1402233a0
0091B1B3  8B D8                           mov ebx, eax
0091B1B5  89 84 24 44 01 00 00            mov dword ptr [rsp + 0x144], eax
0091B1BC  48 8B 8C 24 58 06 00 00         mov rcx, qword ptr [rsp + 0x658]
0091B1C4  48 85 C9                        test rcx, rcx
0091B1C7  0F 85 87 08 00 00               jne 0x14091ba54
0091B1CD  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
0091B1D5  49 8B CD                        mov rcx, r13
0091B1D8  E8 03 D4 AF FF                  call 0x1404185e0
0091B1DD  84 C0                           test al, al
0091B1DF  0F 84 55 04 00 00               je 0x14091b63a
0091B1E5  41 81 FC FD 00 00 00            cmp r12d, 0xfd
0091B1EC  0F 84 C2 00 00 00               je 0x14091b2b4
0091B1F2  41 8B D6                        mov edx, r14d
0091B1F5  48 03 94 24 68 01 00 00         add rdx, qword ptr [rsp + 0x168]
0091B1FD  8B 8C 24 E0 00 00 00            mov ecx, dword ptr [rsp + 0xe0]
0091B204  41 03 CE                        add ecx, r14d
0091B207  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
0091B20E  41 81 FC FC 00 00 00            cmp r12d, 0xfc
0091B215  0F 84 5F 03 00 00               je 0x14091b57a
0091B21B  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
0091B223  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0091B227  41 3B CE                        cmp ecx, r14d
0091B22A  0F 83 23 F8 FF FF               jae 0x14091aa53
0091B230  41 83 CE FF                     or r14d, 0xffffffff
0091B234  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0091B239  BE 95 00 00 C0                  mov esi, 0xc0000095
0091B23E  E9 19 F8 FF FF                  jmp 0x14091aa5c
0091B243  41 83 CE FF                     or r14d, 0xffffffff
0091B247  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0091B24C  BE 95 00 00 C0                  mov esi, 0xc0000095
0091B251  E9 C3 FE FF FF                  jmp 0x14091b119
0091B256  85 C9                           test ecx, ecx
0091B258  0F 84 93 FE FF FF               je 0x14091b0f1
0091B25E  48 8B C1                        mov rax, rcx
0091B261  48 D1 E8                        shr rax, 1
0091B264  49 8D 14 40                     lea rdx, [r8 + rax*2]
0091B268  48 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdx
0091B270  B8 02 00 00 00                  mov eax, 2
0091B275  49 3B D0                        cmp rdx, r8
0091B278  74 1E                           je 0x14091b298
0091B27A  48 2B D0                        sub rdx, rax
0091B27D  48 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdx
0091B285  66 83 3A 5C                     cmp word ptr [rdx], 0x5c
0091B289  74 02                           je 0x14091b28d
0091B28B  EB E8                           jmp 0x14091b275
0091B28D  48 03 D0                        add rdx, rax
0091B290  48 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdx
0091B298  48 8B C2                        mov rax, rdx
0091B29B  49 2B C0                        sub rax, r8
0091B29E  48 D1 F8                        sar rax, 1
0091B2A1  03 C0                           add eax, eax
0091B2A3  2B C8                           sub ecx, eax
0091B2A5  89 8C 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], ecx
0091B2AC  44 8B E1                        mov r12d, ecx
0091B2AF  E9 3D FE FF FF                  jmp 0x14091b0f1
0091B2B4  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
0091B2BC  FF 03                           inc dword ptr [rbx]
0091B2BE  49 8B CD                        mov rcx, r13
0091B2C1  E8 7A 4F BA FF                  call 0x1404c0240
0091B2C6  03 43 04                        add eax, dword ptr [rbx + 4]
0091B2C9  89 43 04                        mov dword ptr [rbx + 4], eax
0091B2CC  33 D2                           xor edx, edx
0091B2CE  49 8B CD                        mov rcx, r13
0091B2D1  E8 FA E2 FF FF                  call 0x1409195d0
0091B2D6  03 43 08                        add eax, dword ptr [rbx + 8]
0091B2D9  89 43 08                        mov dword ptr [rbx + 8], eax
0091B2DC  EB 33                           jmp 0x14091b311
0091B2DE  8B F0                           mov esi, eax
0091B2E0  89 84 24 48 01 00 00            mov dword ptr [rsp + 0x148], eax
0091B2E7  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B2EB  33 FF                           xor edi, edi
0091B2ED  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B2F2  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B2F7  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091B2FC  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0091B304  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0091B309  44 8B A4 24 60 06 00 00         mov r12d, dword ptr [rsp + 0x660]
0091B311  85 F6                           test esi, esi
0091B313  0F 89 65 FD FF FF               jns 0x14091b07e
0091B319  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
0091B31D  E9 32 08 00 00                  jmp 0x14091bb54
0091B322  4C 3B 2D 8F B9 6A 00            cmp r13, qword ptr [rip + 0x6ab98f]
0091B329  0F 84 F9 07 00 00               je 0x14091bb28
0091B32F  41 F7 85 FC 05 00 00 00 00 00 40  test dword ptr [r13 + 0x5fc], 0x40000000
0091B33A  48 8D 05 D7 6C 6E FF            lea rax, [rip - 0x919329]
0091B341  0F 85 6D FD FF FF               jne 0x14091b0b4
0091B347  49 8B 85 50 03 00 00            mov rax, qword ptr [r13 + 0x350]
0091B34E  E9 61 FD FF FF                  jmp 0x14091b0b4
0091B353  C7 44 24 30 04 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000004
0091B35B  48 85 DB                        test rbx, rbx
0091B35E  0F 85 73 F7 FF FF               jne 0x14091aad7
0091B364  E9 EB 07 00 00                  jmp 0x14091bb54
0091B369  4C 89 BC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r15
0091B371  85 C9                           test ecx, ecx
0091B373  74 1C                           je 0x14091b391
0091B375  8B D9                           mov ebx, ecx
0091B377  44 8B C1                        mov r8d, ecx
0091B37A  49 8B CF                        mov rcx, r15
0091B37D  E8 BE B4 DA FF                  call 0x1406c6840
0091B382  48 D1 EB                        shr rbx, 1
0091B385  49 8D 04 5F                     lea rax, [r15 + rbx*2]
0091B389  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
0091B391  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
0091B399  66 89 38                        mov word ptr [rax], di
0091B39C  48 83 84 24 C8 00 00 00 02      add qword ptr [rsp + 0xc8], 2
0091B3A5  EB 30                           jmp 0x14091b3d7
0091B3A7  8B F0                           mov esi, eax
0091B3A9  89 84 24 38 01 00 00            mov dword ptr [rsp + 0x138], eax
0091B3B0  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B3B4  33 FF                           xor edi, edi
0091B3B6  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
0091B3BB  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B3C0  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B3C5  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091B3CA  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0091B3D2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0091B3D7  85 F6                           test esi, esi
0091B3D9  0F 88 3A FF FF FF               js 0x14091b319
0091B3DF  44 8B 8C 24 60 06 00 00         mov r9d, dword ptr [rsp + 0x660]
0091B3E7  E9 5D FD FF FF                  jmp 0x14091b149
0091B3EC  4C 8D 8C 24 E0 01 00 00         lea r9, [rsp + 0x1e0]
0091B3F4  44 8A 44 24 3C                  mov r8b, byte ptr [rsp + 0x3c]
0091B3F9  49 8B D5                        mov rdx, r13
0091B3FC  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0091B404  E8 2B DD FF FF                  call 0x140919134
0091B409  8B F0                           mov esi, eax
0091B40B  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B40F  85 C0                           test eax, eax
0091B411  0F 88 65 06 00 00               js 0x14091ba7c
0091B417  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0091B41F  48 83 21 00                     and qword ptr [rcx], 0
0091B423  89 59 64                        mov dword ptr [rcx + 0x64], ebx
0091B426  48 89 79 40                     mov qword ptr [rcx + 0x40], rdi
0091B42A  83 61 38 00                     and dword ptr [rcx + 0x38], 0
0091B42E  4C 3B 2D 3B B7 6A 00            cmp r13, qword ptr [rip + 0x6ab73b]
0091B435  75 05                           jne 0x14091b43c
0091B437  48 83 61 60 00                  and qword ptr [rcx + 0x60], 0
0091B43C  48 8B 05 75 B8 6A 00            mov rax, qword ptr [rip + 0x6ab875]
0091B443  4C 3B E8                        cmp r13, rax
0091B446  75 1E                           jne 0x14091b466
0091B448  48 8B 05 99 28 51 00            mov rax, qword ptr [rip + 0x512899]
0091B44F  48 C1 E0 0C                     shl rax, 0xc
0091B453  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0091B45B  48 89 81 90 00 00 00            mov qword ptr [rcx + 0x90], rax
0091B462  48 89 41 08                     mov qword ptr [rcx + 8], rax
0091B466  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0091B46B  EB 26                           jmp 0x14091b493
0091B46D  8B F0                           mov esi, eax
0091B46F  89 84 24 4C 01 00 00            mov dword ptr [rsp + 0x14c], eax
0091B476  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B47A  33 FF                           xor edi, edi
0091B47C  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B481  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B486  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
0091B48E  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
0091B493  85 F6                           test esi, esi
0091B495  0F 89 04 F6 FF FF               jns 0x14091aa9f
0091B49B  E9 79 FE FF FF                  jmp 0x14091b319
0091B4A0  41 81 F9 FC 00 00 00            cmp r9d, 0xfc
0091B4A7  74 0E                           je 0x14091b4b7
0091B4A9  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0091B4B1  48 8D 48 38                     lea rcx, [rax + 0x38]
0091B4B5  EB 0C                           jmp 0x14091b4c3
0091B4B7  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0091B4BF  48 8D 48 20                     lea rcx, [rax + 0x20]
0091B4C3  0F B7 84 24 C8 00 00 00         movzx eax, word ptr [rsp + 0xc8]
0091B4CB  66 41 2B C7                     sub ax, r15w
0091B4CF  66 83 E8 02                     sub ax, 2
0091B4D3  66 89 01                        mov word ptr [rcx], ax
0091B4D6  66 44 89 61 02                  mov word ptr [rcx + 2], r12w
0091B4DB  4C 89 79 08                     mov qword ptr [rcx + 8], r15
0091B4DF  EB 2B                           jmp 0x14091b50c
0091B4E1  8B F0                           mov esi, eax
0091B4E3  89 84 24 3C 01 00 00            mov dword ptr [rsp + 0x13c], eax
0091B4EA  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B4EE  33 FF                           xor edi, edi
0091B4F0  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B4F5  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B4FA  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091B4FF  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0091B507  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0091B50C  85 F6                           test esi, esi
0091B50E  0F 89 3F FC FF FF               jns 0x14091b153
0091B514  E9 00 FE FF FF                  jmp 0x14091b319
0091B519  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
0091B51D  41 81 FC FC 00 00 00            cmp r12d, 0xfc
0091B524  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0091B52C  74 08                           je 0x14091b536
0091B52E  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0091B536  89 08                           mov dword ptr [rax], ecx
0091B538  EB 33                           jmp 0x14091b56d
0091B53A  8B F0                           mov esi, eax
0091B53C  89 84 24 34 01 00 00            mov dword ptr [rsp + 0x134], eax
0091B543  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B547  33 FF                           xor edi, edi
0091B549  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B54E  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B553  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091B558  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0091B560  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0091B565  44 8B A4 24 60 06 00 00         mov r12d, dword ptr [rsp + 0x660]
0091B56D  85 F6                           test esi, esi
0091B56F  0F 89 F0 FB FF FF               jns 0x14091b165
0091B575  E9 9F FD FF FF                  jmp 0x14091b319
0091B57A  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
0091B582  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0091B586  41 3B CE                        cmp ecx, r14d
0091B589  0F 82 B0 00 00 00               jb 0x14091b63f
0091B58F  44 8B F1                        mov r14d, ecx
0091B592  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
0091B596  8B F7                           mov esi, edi
0091B598  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0091B59C  85 F6                           test esi, esi
0091B59E  0F 88 75 FD FF FF               js 0x14091b319
0091B5A4  44 3B B4 24 48 06 00 00         cmp r14d, dword ptr [rsp + 0x648]
0091B5AC  0F 87 AF 04 00 00               ja 0x14091ba61
0091B5B2  39 7C 24 30                     cmp dword ptr [rsp + 0x30], edi
0091B5B6  0F 8C C2 FA FF FF               jl 0x14091b07e
0091B5BC  49 8B 85 D0 01 00 00            mov rax, qword ptr [r13 + 0x1d0]
0091B5C3  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
0091B5CB  48 89 41 08                     mov qword ptr [rcx + 8], rax
0091B5CF  49 8B 85 D0 02 00 00            mov rax, qword ptr [r13 + 0x2d0]
0091B5D6  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
0091B5DA  49 8B 85 78 06 00 00            mov rax, qword ptr [r13 + 0x678]
0091B5E1  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
0091B5E5  48 89 79 28                     mov qword ptr [rcx + 0x28], rdi
0091B5E9  83 61 20 00                     and dword ptr [rcx + 0x20], 0
0091B5ED  EB 2E                           jmp 0x14091b61d
0091B5EF  8B F0                           mov esi, eax
0091B5F1  89 84 24 40 01 00 00            mov dword ptr [rsp + 0x140], eax
0091B5F8  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B5FC  33 FF                           xor edi, edi
0091B5FE  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B603  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B608  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0091B610  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0091B615  44 8B A4 24 60 06 00 00         mov r12d, dword ptr [rsp + 0x660]
0091B61D  85 F6                           test esi, esi
0091B61F  0F 88 F4 FC FF FF               js 0x14091b319
0091B625  45 8B FE                        mov r15d, r14d
0091B628  4C 03 BC 24 D8 00 00 00         add r15, qword ptr [rsp + 0xd8]
0091B630  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0091B635  E9 44 FA FF FF                  jmp 0x14091b07e
0091B63A  E9 26 FB FF FF                  jmp 0x14091b165
0091B63F  41 83 CE FF                     or r14d, 0xffffffff
0091B643  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0091B648  BE 95 00 00 C0                  mov esi, 0xc0000095
0091B64D  E9 46 FF FF FF                  jmp 0x14091b598
0091B652  39 7C 24 30                     cmp dword ptr [rsp + 0x30], edi
0091B656  7C 59                           jl 0x14091b6b1
0091B658  41 81 FC FC 00 00 00            cmp r12d, 0xfc
0091B65F  0F 84 CF 04 00 00               je 0x14091bb34
0091B665  48 39 BC 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rdi
0091B66D  74 42                           je 0x14091b6b1
0091B66F  41 81 FC FC 00 00 00            cmp r12d, 0xfc
0091B676  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0091B67E  74 08                           je 0x14091b688
0091B680  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0091B688  89 38                           mov dword ptr [rax], edi
0091B68A  EB 1D                           jmp 0x14091b6a9
0091B68C  8B F0                           mov esi, eax
0091B68E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B692  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B697  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B69C  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0091B6A4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0091B6A9  85 F6                           test esi, esi
0091B6AB  0F 88 68 FC FF FF               js 0x14091b319
0091B6B1  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0091B6B6  48 85 C0                        test rax, rax
0091B6B9  0F 84 95 04 00 00               je 0x14091bb54
0091B6BF  44 89 30                        mov dword ptr [rax], r14d
0091B6C2  E9 8D 04 00 00                  jmp 0x14091bb54
0091B6C7  BA 44 66 6C 74                  mov edx, 0x746c6644
0091B6CC  49 8B CD                        mov rcx, r13
0091B6CF  E8 AC 48 8F FF                  call 0x14020ff80
0091B6D4  48 89 84 24 90 01 00 00         mov qword ptr [rsp + 0x190], rax
0091B6DC  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0091B6E5  48 89 8C 24 D8 01 00 00         mov qword ptr [rsp + 0x1d8], rcx
0091B6ED  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
0091B6F4  BA 01 00 00 00                  mov edx, 1
0091B6F9  66 2B C2                        sub ax, dx
0091B6FC  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
0091B703  90                              nop
0091B704  48 8B 9C 24 90 01 00 00         mov rbx, qword ptr [rsp + 0x190]
0091B70C  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0091B710  E8 AB 64 8F FF                  call 0x140211bc0
0091B715  48 8B 83 98 00 00 00            mov rax, qword ptr [rbx + 0x98]
0091B71C  48 8B 10                        mov rdx, qword ptr [rax]
0091B71F  0F B6 42 01                     movzx eax, byte ptr [rdx + 1]
0091B723  44 8D 3C 85 08 00 00 00         lea r15d, [rax*4 + 8]
0091B72B  41 83 FF 44                     cmp r15d, 0x44
0091B72F  77 10                           ja 0x14091b741
0091B731  45 8B C7                        mov r8d, r15d
0091B734  48 8D 8C 24 50 02 00 00         lea rcx, [rsp + 0x250]
0091B73C  E8 FF B0 DA FF                  call 0x1406c6840
0091B741  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0091B745  E8 C6 42 94 FF                  call 0x14025fa10
0091B74A  E8 61 21 94 FF                  call 0x14025d8b0
0091B74F  44 89 BC 24 BC 00 00 00         mov dword ptr [rsp + 0xbc], r15d
0091B757  48 C7 84 24 C0 00 00 00 FE 00 00 00  mov qword ptr [rsp + 0xc0], 0xfe
0091B763  48 C7 84 24 B0 00 00 00 82 00 00 00  mov qword ptr [rsp + 0xb0], 0x82
0091B76F  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0091B774  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
0091B77C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0091B781  4C 8D 8C 24 60 04 00 00         lea r9, [rsp + 0x460]
0091B789  4C 8D 84 24 C0 00 00 00         lea r8, [rsp + 0xc0]
0091B791  48 8D 94 24 F0 04 00 00         lea rdx, [rsp + 0x4f0]
0091B799  48 8B CB                        mov rcx, rbx
0091B79C  E8 EF 0B B4 FF                  call 0x14045c390
0091B7A1  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B7A5  85 C0                           test eax, eax
0091B7A7  0F 88 ED 02 00 00               js 0x14091ba9a
0091B7AD  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B7B2  49 8D 8D 48 02 00 00            lea rcx, [r13 + 0x248]
0091B7B9  41 B8 44 66 6C 74               mov r8d, 0x746c6644
0091B7BF  48 8B D3                        mov rdx, rbx
0091B7C2  E8 29 1E AD FF                  call 0x1403ed5f0
0091B7C7  41 8D 5F 07                     lea ebx, [r15 + 7]
0091B7CB  83 E3 F8                        and ebx, 0xfffffff8
0091B7CE  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
0091B7D2  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
0091B7D6  44 8D 34 19                     lea r14d, [rcx + rbx]
0091B7DA  8D 04 0B                        lea eax, [rbx + rcx]
0091B7DD  3B C1                           cmp eax, ecx
0091B7DF  0F 82 32 01 00 00               jb 0x14091b917
0091B7E5  8B F7                           mov esi, edi
0091B7E7  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0091B7EC  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0091B7F0  85 F6                           test esi, esi
0091B7F2  0F 88 21 FB FF FF               js 0x14091b319
0091B7F8  01 5C 24 40                     add dword ptr [rsp + 0x40], ebx
0091B7FC  44 3B B4 24 48 06 00 00         cmp r14d, dword ptr [rsp + 0x648]
0091B804  0F 86 1B 01 00 00               jbe 0x14091b925
0091B80A  C7 44 24 30 04 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000004
0091B812  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0091B817  48 85 D2                        test rdx, rdx
0091B81A  0F 84 34 03 00 00               je 0x14091bb54
0091B820  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
0091B828  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091B82D  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
0091B835  48 8D 41 FF                     lea rax, [rcx - 1]
0091B839  BB FE FF FF FF                  mov ebx, 0xfffffffe
0091B83E  48 3B C3                        cmp rax, rbx
0091B841  0F 86 7C 01 00 00               jbe 0x14091b9c3
0091B847  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0091B84F  48 8D 41 FF                     lea rax, [rcx - 1]
0091B853  48 3B C3                        cmp rax, rbx
0091B856  0F 87 5A 01 00 00               ja 0x14091b9b6
0091B85C  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0091B860  42 8D 04 31                     lea eax, [rcx + r14]
0091B864  41 3B C6                        cmp eax, r14d
0091B867  0F 82 36 01 00 00               jb 0x14091b9a3
0091B86D  44 8B F0                        mov r14d, eax
0091B870  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0091B874  8B F7                           mov esi, edi
0091B876  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0091B87A  85 F6                           test esi, esi
0091B87C  0F 88 97 FA FF FF               js 0x14091b319
0091B882  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
0091B889  01 44 24 40                     add dword ptr [rsp + 0x40], eax
0091B88D  44 3B B4 24 48 06 00 00         cmp r14d, dword ptr [rsp + 0x648]
0091B895  0F 87 79 01 00 00               ja 0x14091ba14
0091B89B  41 8B C7                        mov eax, r15d
0091B89E  41 2B C4                        sub eax, r12d
0091B8A1  41 89 84 24 50 01 00 00         mov dword ptr [r12 + 0x150], eax
0091B8A9  44 8B 84 24 B0 00 00 00         mov r8d, dword ptr [rsp + 0xb0]
0091B8B1  48 8D 94 24 60 04 00 00         lea rdx, [rsp + 0x460]
0091B8B9  49 8B CF                        mov rcx, r15
0091B8BC  E8 7F AF DA FF                  call 0x1406c6840
0091B8C1  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
0091B8C6  EB 2B                           jmp 0x14091b8f3
0091B8C8  8B F0                           mov esi, eax
0091B8CA  89 84 24 30 01 00 00            mov dword ptr [rsp + 0x130], eax
0091B8D1  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B8D5  33 FF                           xor edi, edi
0091B8D7  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B8DC  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B8E1  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091B8E6  4C 8B 94 24 98 00 00 00         mov r10, qword ptr [rsp + 0x98]
0091B8EE  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
0091B8F3  85 F6                           test esi, esi
0091B8F5  0F 88 1E FA FF FF               js 0x14091b319
0091B8FB  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
0091B902  4C 03 F8                        add r15, rax
0091B905  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0091B90A  44 8B A4 24 60 06 00 00         mov r12d, dword ptr [rsp + 0x660]
0091B912  E9 6C F7 FF FF                  jmp 0x14091b083
0091B917  41 83 CE FF                     or r14d, 0xffffffff
0091B91B  BE 95 00 00 C0                  mov esi, 0xc0000095
0091B920  E9 C2 FE FF FF                  jmp 0x14091b7e7
0091B925  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
0091B92D  41 C7 44 24 34 70 01 00 00      mov dword ptr [r12 + 0x34], 0x170
0091B936  45 8B C7                        mov r8d, r15d
0091B939  48 8D 94 24 50 02 00 00         lea rdx, [rsp + 0x250]
0091B941  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091B946  49 8B CF                        mov rcx, r15
0091B949  E8 F2 AE DA FF                  call 0x1406c6840
0091B94E  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0091B953  EB 37                           jmp 0x14091b98c
0091B955  8B F0                           mov esi, eax
0091B957  89 84 24 28 01 00 00            mov dword ptr [rsp + 0x128], eax
0091B95E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091B962  33 FF                           xor edi, edi
0091B964  8B 5C 24 78                     mov ebx, dword ptr [rsp + 0x78]
0091B968  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091B96D  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
0091B975  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091B97A  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091B97F  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0091B987  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0091B98C  85 F6                           test esi, esi
0091B98E  0F 88 85 F9 FF FF               js 0x14091b319
0091B994  8B C3                           mov eax, ebx
0091B996  4C 03 F8                        add r15, rax
0091B999  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0091B99E  E9 8A FE FF FF                  jmp 0x14091b82d
0091B9A3  41 83 CE FF                     or r14d, 0xffffffff
0091B9A7  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0091B9AC  BE 95 00 00 C0                  mov esi, 0xc0000095
0091B9B1  E9 C0 FE FF FF                  jmp 0x14091b876
0091B9B6  44 8B A4 24 60 06 00 00         mov r12d, dword ptr [rsp + 0x660]
0091B9BE  E9 BB F6 FF FF                  jmp 0x14091b07e
0091B9C3  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0091B9C7  42 8D 04 31                     lea eax, [rcx + r14]
0091B9CB  41 3B C6                        cmp eax, r14d
0091B9CE  72 5F                           jb 0x14091ba2f
0091B9D0  44 8B F0                        mov r14d, eax
0091B9D3  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0091B9D7  8B F7                           mov esi, edi
0091B9D9  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0091B9DD  85 F6                           test esi, esi
0091B9DF  0F 88 34 F9 FF FF               js 0x14091b319
0091B9E5  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
0091B9EC  01 44 24 40                     add dword ptr [rsp + 0x40], eax
0091B9F0  44 3B B4 24 48 06 00 00         cmp r14d, dword ptr [rsp + 0x648]
0091B9F8  0F 86 B1 00 00 00               jbe 0x14091baaf
0091B9FE  C7 44 24 30 04 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000004
0091BA06  48 85 D2                        test rdx, rdx
0091BA09  0F 85 38 FE FF FF               jne 0x14091b847
0091BA0F  E9 40 01 00 00                  jmp 0x14091bb54
0091BA14  C7 44 24 30 04 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000004
0091BA1C  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
0091BA21  4D 85 D2                        test r10, r10
0091BA24  0F 85 E0 FE FF FF               jne 0x14091b90a
0091BA2A  E9 25 01 00 00                  jmp 0x14091bb54
0091BA2F  41 83 CE FF                     or r14d, 0xffffffff
0091BA33  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0091BA38  BE 95 00 00 C0                  mov esi, 0xc0000095
0091BA3D  EB 9A                           jmp 0x14091b9d9
0091BA3F  48 8B 05 2A B1 6A 00            mov rax, qword ptr [rip + 0x6ab12a]
0091BA46  4C 3B E8                        cmp r13, rax
0091BA49  0F 84 EB FB FF FF               je 0x14091b63a
0091BA4F  E9 57 F7 FF FF                  jmp 0x14091b1ab
0091BA54  3B 19                           cmp ebx, dword ptr [rcx]
0091BA56  0F 85 DE FB FF FF               jne 0x14091b63a
0091BA5C  E9 6C F7 FF FF                  jmp 0x14091b1cd
0091BA61  C7 44 24 30 04 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000004
0091BA69  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0091BA6E  48 85 C0                        test rax, rax
0091BA71  0F 84 DD 00 00 00               je 0x14091bb54
0091BA77  E9 36 FB FF FF                  jmp 0x14091b5b2
0091BA7C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0091BA80  E9 CF 00 00 00                  jmp 0x14091bb54
0091BA85  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
0091BA89  29 44 24 40                     sub dword ptr [rsp + 0x40], eax
0091BA8D  44 2B F0                        sub r14d, eax
0091BA90  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0091BA95  E9 3D F0 FF FF                  jmp 0x14091aad7
0091BA9A  48 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdi
0091BAA2  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
0091BAAA  E9 FE FC FF FF                  jmp 0x14091b7ad
0091BAAF  41 8B C7                        mov eax, r15d
0091BAB2  41 2B C4                        sub eax, r12d
0091BAB5  41 89 44 24 38                  mov dword ptr [r12 + 0x38], eax
0091BABA  44 8B 84 24 C0 00 00 00         mov r8d, dword ptr [rsp + 0xc0]
0091BAC2  48 8D 94 24 F0 04 00 00         lea rdx, [rsp + 0x4f0]
0091BACA  49 8B CF                        mov rcx, r15
0091BACD  E8 6E AD DA FF                  call 0x1406c6840
0091BAD2  EB 38                           jmp 0x14091bb0c
0091BAD4  8B F0                           mov esi, eax
0091BAD6  89 84 24 2C 01 00 00            mov dword ptr [rsp + 0x12c], eax
0091BADD  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0091BAE1  33 FF                           xor edi, edi
0091BAE3  BB FE FF FF FF                  mov ebx, 0xfffffffe
0091BAE8  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0091BAED  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
0091BAF5  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0091BAFA  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0091BAFF  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0091BB07  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0091BB0C  85 F6                           test esi, esi
0091BB0E  0F 88 05 F8 FF FF               js 0x14091b319
0091BB14  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
0091BB1B  4C 03 F8                        add r15, rax
0091BB1E  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0091BB23  E9 1F FD FF FF                  jmp 0x14091b847
0091BB28  48 8D 05 19 65 6E FF            lea rax, [rip - 0x919ae7]
0091BB2F  E9 80 F5 FF FF                  jmp 0x14091b0b4
0091BB34  48 39 BC 24 A8 00 00 00         cmp qword ptr [rsp + 0xa8], rdi
0091BB3C  0F 85 2D FB FF FF               jne 0x14091b66f
0091BB42  41 81 FC FC 00 00 00            cmp r12d, 0xfc
0091BB49  0F 84 62 FB FF FF               je 0x14091b6b1
0091BB4F  E9 11 FB FF FF                  jmp 0x14091b665
0091BB54  4D 85 ED                        test r13, r13
0091BB57  0F 85 F7 00 00 00               jne 0x14091bc54
0091BB5D  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
0091BB65  4D 85 C0                        test r8, r8
0091BB68  0F 85 05 01 00 00               jne 0x14091bc73
0091BB6E  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0091BB72  48 8B 8C 24 F0 05 00 00         mov rcx, qword ptr [rsp + 0x5f0]
0091BB7A  48 33 CC                        xor rcx, rsp
0091BB7D  E8 BE 0A D9 FF                  call 0x1406ac640
0091BB82  48 81 C4 00 06 00 00            add rsp, 0x600
0091BB89  41 5F                           pop r15
0091BB8B  41 5E                           pop r14
0091BB8D  41 5D                           pop r13
0091BB8F  41 5C                           pop r12
0091BB91  5F                              pop rdi
0091BB92  5E                              pop rsi
0091BB93  5B                              pop rbx
0091BB94  C3                              ret
0091BB95  CC                              int3
0091BB96  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
0091BB9E  41 81 FC FD 00 00 00            cmp r12d, 0xfd
0091BBA5  74 38                           je 0x14091bbdf
0091BBA7  C7 84 24 80 00 00 00 70 02 00 00  mov dword ptr [rsp + 0x80], 0x270
0091BBB2  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0091BBBA  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0091BBC2  B8 88 00 00 00                  mov eax, 0x88
0091BBC7  8D 48 C8                        lea ecx, [rax - 0x38]
0091BBCA  41 83 FC 05                     cmp r12d, 5
0091BBCE  0F 44 C1                        cmove eax, ecx
0091BBD1  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
0091BBD5  0F 95 44 24 3C                  setne byte ptr [rsp + 0x3c]
0091BBDA  E9 C7 ED FF FF                  jmp 0x14091a9a6
0091BBDF  40 88 7C 24 3C                  mov byte ptr [rsp + 0x3c], dil
0091BBE4  B8 0C 00 00 00                  mov eax, 0xc
0091BBE9  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
0091BBF0  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0091BBF4  89 7C 24 7C                     mov dword ptr [rsp + 0x7c], edi
0091BBF8  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0091BC00  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
0091BC08  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
0091BC10  E9 99 ED FF FF                  jmp 0x14091a9ae
0091BC15  48 85 DB                        test rbx, rbx
0091BC18  0F 85 92 5F 20 00               jne 0x140b21bb0
0091BC1E  B8 04 00 00 C0                  mov eax, 0xc0000004
0091BC23  E9 4A FF FF FF                  jmp 0x14091bb72
0091BC28  40 8A CE                        mov cl, sil
0091BC2B  E8 0C 1D 04 00                  call 0x14095d93c
0091BC30  85 C0                           test eax, eax
0091BC32  0F 88 3A FF FF FF               js 0x14091bb72
0091BC38  E9 B1 ED FF FF                  jmp 0x14091a9ee
0091BC3D  39 BC 24 48 06 00 00            cmp dword ptr [rsp + 0x648], edi
0091BC44  0F 84 DD ED FF FF               je 0x14091aa27
0091BC4A  E8 AD 28 9B FF                  call 0x1402ce4fc
0091BC4F  E9 D3 ED FF FF                  jmp 0x14091aa27
0091BC54  4C 3B 2D 15 AF 6A 00            cmp r13, qword ptr [rip + 0x6aaf15]
0091BC5B  0F 84 FC FE FF FF               je 0x14091bb5d
0091BC61  BA 50 73 45 6E                  mov edx, 0x6e457350
0091BC66  49 8B CD                        mov rcx, r13
0091BC69  E8 72 BC 9D FF                  call 0x1402f78e0
0091BC6E  E9 EA FE FF FF                  jmp 0x14091bb5d
0091BC73  48 8B 05 F6 AE 6A 00            mov rax, qword ptr [rip + 0x6aaef6]
0091BC7A  49 39 80 20 02 00 00            cmp qword ptr [r8 + 0x220], rax
0091BC81  0F 84 E7 FE FF FF               je 0x14091bb6e
0091BC87  BA 50 73 45 6E                  mov edx, 0x6e457350
0091BC8C  49 8B C8                        mov rcx, r8
0091BC8F  E8 4C BC 9D FF                  call 0x1402f78e0
0091BC94  E9 D5 FE FF FF                  jmp 0x14091bb6e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpGetProcessInformation(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m398;
    unsigned __int64 v_stack_m3E8;
    unsigned __int64 v_stack_m438;
    unsigned __int64 v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned int v_stack_m468;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m4D0;
    unsigned __int64 v_stack_m4E0;
    unsigned int v_stack_m4E8;
    unsigned int v_stack_m4EC;
    unsigned int v_stack_m4F0;
    unsigned int v_stack_m4F4;
    unsigned int v_stack_m4F8;
    unsigned int v_stack_m4FC;
    unsigned int v_stack_m500;
    unsigned int v_stack_m504;
    unsigned int v_stack_m508;
    unsigned int v_stack_m50C;
    unsigned int v_stack_m510;
    unsigned __int64 v_stack_m520;
    unsigned __int8 v_stack_m525;
    unsigned __int8 v_stack_m526;
    unsigned __int8 v_stack_m527;
    unsigned __int8 v_stack_m528;
    unsigned __int64 v_stack_m530;
    unsigned __int64 v_stack_m538;
    unsigned __int64 v_stack_m540;
    unsigned __int64 v_stack_m548;
    unsigned __int64 v_stack_m550;
    unsigned int v_stack_m558;
    unsigned __int64 v_stack_m560;
    unsigned __int64 v_stack_m568;
    unsigned __int64 v_stack_m570;
    unsigned __int64 v_stack_m578;
    unsigned int v_stack_m57C;
    unsigned int v_stack_m580;
    unsigned __int64 v_stack_m588;
    unsigned __int64 v_stack_m590;
    unsigned int v_stack_m598;
    unsigned __int64 v_stack_m5A0;
    unsigned __int64 v_stack_m5A8;
    unsigned __int64 v_stack_m5B0;
    unsigned int v_stack_m5B8;
    unsigned int v_stack_m5BC;
    unsigned int v_stack_m5C0;
    unsigned __int8 v_stack_m5C5;
    unsigned __int8 v_stack_m5CC;
    unsigned __int64 v_stack_m5D8;
    unsigned __int64 v_stack_m5E0;
    unsigned __int8 v_stack_m5E8;
    unsigned __int64 v_stack_m5F0;
    unsigned int v_stack_m5F8;
    unsigned __int8 v_stack_m5FC;
    unsigned int v_stack_m600;
    unsigned int v_stack_m604;
    unsigned int v_stack_m608;
    unsigned __int64 v_stack_m610;
    unsigned __int64 v_stack_m618;
    unsigned int v_stack_m638;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p34;
    unsigned __int8 v_stack_p3C;
    unsigned int v_stack_p648;
    unsigned int v_stack_p7C;
    unsigned int v_stack_p80;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE8;

    v_stack_p20 = a4;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (0x600ULL);
    result = (*(unsigned __int64 *)(v_rip + 5176998)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m5F0 = a3;
    v_stack_m560 = a1;
    v_stack_m4D0 = a1;
    v_stack_m5A0 = a3;
    v_rdi = 0;
    v_stack_m588 = 0;
    a2 = 0;
    result = memset(v_stack_m398, a2, 440, a4);
    v_stack_m5C0 = 0;
    v_stack_m57C = 0;
    v_stack_m5F8 = 0;
    v_stack_m578 = 0;
    v_stack_m5D8 = 0;
    a2 = 0;
    result = memset(v_stack_m458, a2, v_rdi + 104, a4);
    v_stack_m5E8 = 0;
    v_stack_m5B0 = 0;
    v_stack_m530 = v_xmm0;
    v_stack_m520 = v_xmm0;
    v_stack_m604 = 0;
    v_stack_m570 = 0;
    a2 = 0;
    result = memset(v_stack_m3E8, a2, v_rdi + 68, a4);
    v_stack_m5E0 = 0;
    v_stack_m598 = 0;
    if (a3 != 0) {
        *(unsigned int *)(a3) = 0;
    }
    if (((unsigned int)((unsigned int)(a5))) != 252) goto loc_0091BB96;
    v_stack_m5FC = 0;
    v_stack_m5B8 = 48;
    v_stack_m5BC = 0;
    v_stack_m590 = v_stack_m560;
    v_stack_m5A8 = 0;
loc_0091A9A6:
    v_stack_m550 = 0;
loc_0091A9AE:
    v_stack_m558 = (unsigned int)((unsigned int)(v_stack_m5B8));
    if (v_stack_p10 < ((unsigned int)((unsigned int)(v_stack_m5B8)))) goto loc_0091BC15;
    v_rbx = (unsigned int)((a3) & (0xC0000004ULL));
    if (((unsigned int)((unsigned int)(a5))) == 148) goto loc_0091BC28;
loc_0091A9EE:
    result = ExIsRestrictedCaller((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m598, v_rdi + 68, a4);
    v_stack_m580 = (unsigned int)(result);
    v_stack_m600 = 0;
    if (((unsigned int)((unsigned int)(a5) - 252)) > 1) goto loc_0091BC3D;
loc_0091AA27:
    result = PsGetCurrentServerSilo(1, v_stack_m598, v_rdi + 68, a4);
    v_stack_m4E0 = result;
    v_stack_m5D8 = *(unsigned __int64 *)(v_rip + 6996277);
    v_stack_m608 = (unsigned int)(v_rbx);
    goto loc_0091B184;
loc_0091AA53:
    v_stack_m604 = 1;
loc_0091AA5C:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    a2 = 0;
    result = memset(v_stack_m458, a2, a2 + 104, a4);
    if (1 <= v_stack_p10) goto loc_0091B3EC;
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
loc_0091AA9F:
    v_r15 = (v_stack_m5A8) + (256);
    v_stack_m5E0 = v_r15;
    a2 = 0;
loc_0091AAB5:
    result = ExpGetNextProcessThread(*(unsigned __int64 *)(v_rip + 6996277), a2, a2 + 104, a4);
    v_stack_m5B0 = result;
    if (result == 0) goto loc_0091AD99;
    if ((*(unsigned __int8 *)(result + 4)) == 0) goto loc_0091AAE1;
loc_0091AAD7:
    goto loc_0091AAB5;
loc_0091AAE1:
    if (((unsigned int)(1 + (unsigned int)(v_stack_m5BC) * 1)) < 1) goto loc_0091AD86;
    v_stack_m604 = (unsigned int)(1 + (unsigned int)(v_stack_m5BC) * 1);
loc_0091AAFB:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((unsigned int)((unsigned int)((unsigned int)(1 + (unsigned int)(v_stack_m5BC) * 1)))) > v_stack_p10) goto loc_0091B353;
    result = KeQueryValuesThread(v_stack_m5B0, v_stack_m530, result, a4);
    if (v_stack_m528 == 4) goto loc_0091BA85;
    *(unsigned int *)(v_r15 + 24) = (unsigned int)((unsigned int)(v_stack_m530));
    *(unsigned int *)(v_r15 + 68) = (unsigned int)(v_stack_m528);
    *(unsigned int *)(v_r15 + 72) = (unsigned int)(v_stack_m527);
    *(unsigned int *)(v_r15 + 56) = (unsigned int)((__int8)(v_stack_m526));
    *(unsigned int *)(v_r15 + 60) = (unsigned int)((__int8)(v_stack_m525));
    result = ((unsigned int)(*(unsigned int *)(v_stack_m5B0 + 652))) * ((unsigned int)(*(unsigned int *)(v_rip + 6995747)));
    *(unsigned __int64 *)(v_r15) = result;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m5B0 + 732))) * ((unsigned int)(*(unsigned int *)(v_rip + 6995747)));
    *(unsigned __int64 *)(v_r15 + 8) = result;
    *(unsigned __int64 *)(v_r15 + 16) = *(unsigned __int64 *)(v_stack_m5B0 + 1216);
    *(unsigned int *)(v_r15 + 64) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m5B0 + 340)));
    *(unsigned __int64 *)(v_r15 + 40) = v_xmm0;
    if (((*(unsigned int *)(v_stack_m5B0 + 116)) & (0x400ULL)) != 0) goto loc_0091ACF6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m5B0 + 1448)))) & (8)) != 0) goto loc_0091ACA3;
    result = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m5B0 + 1448)))) & (8)) == 0) { result = *(unsigned __int64 *)(v_stack_m5B0 + 1248); }
loc_0091AC06:
loc_0091AC19:
    v_stack_m538 = result;
    if (v_stack_m598 == 0) goto loc_0091ACAB;
loc_0091AC34:
    *(unsigned __int64 *)(v_stack_m5E0 + 32) = 0;
loc_0091AC38:
    if (v_stack_m5FC == 0) goto loc_0091AD30;
    if (v_stack_m598 == 0) goto loc_0091ACBD;
loc_0091AC4C:
    *(unsigned __int64 *)(v_stack_m5E0 + 80) = 0;
    *(unsigned __int64 *)(v_stack_m5E0 + 88) = 0;
loc_0091AC54:
    v_stack_m538 = *(unsigned __int64 *)(v_stack_m5B0 + 1376);
    if (v_stack_m598 == 0) goto loc_0091AD15;
loc_0091AC78:
    *(unsigned __int64 *)(v_stack_m5E0 + 96) = 0;
loc_0091AC7C:
    *(unsigned __int64 *)(v_stack_m5E0 + 104) = *(unsigned __int64 *)(v_stack_m5B0 + 240);
    *(unsigned __int64 *)(v_stack_m5E0 + 112) = 0;
    *(unsigned __int64 *)(v_stack_m5E0 + 120) = 0;
    *(unsigned __int64 *)(v_stack_m5E0 + 128) = 0;
    goto loc_0091AD30;
loc_0091ACA3:
    goto loc_0091AC06;
loc_0091ACAB:
    if (v_stack_m580 != 0) goto loc_0091AD0A;
loc_0091ACB4:
    *(unsigned __int64 *)(v_stack_m5E0 + 32) = 0;
    goto loc_0091AC38;
loc_0091ACBD:
    if (v_stack_m580 != 0) goto loc_0091AC4C;
    *(unsigned __int64 *)(v_stack_m5E0 + 80) = *(unsigned __int64 *)(v_stack_m5B0 + 56);
    *(unsigned __int64 *)(v_stack_m5E0 + 88) = *(unsigned __int64 *)(v_stack_m5B0 + 48);
    goto loc_0091AC54;
loc_0091ACF6:
    goto loc_0091AC19;
loc_0091AD0A:
    if ((*(unsigned __int64 *)(v_stack_m5B0 + 1376)) > v_stack_m530) goto loc_0091AC34;
    goto loc_0091ACB4;
loc_0091AD15:
    if (v_stack_m580 == 0) goto loc_0091AD27;
    if ((*(unsigned __int64 *)(v_stack_m5B0 + 240)) > v_stack_m530) goto loc_0091AC78;
loc_0091AD27:
    *(unsigned __int64 *)(v_stack_m5E0 + 96) = *(unsigned __int64 *)(v_stack_m5B0 + 240);
    goto loc_0091AC7C;
loc_0091AD30:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m5A8 + 4))) + 1);
    *(unsigned int *)(v_stack_m5A8 + 4) = (unsigned int)(result);
    goto loc_0091AD6D;
loc_0091AD6D:
    if (sign_flag) goto loc_0091B319;
    v_r15 = (v_stack_m5E0) + ((unsigned int)(v_stack_m5BC));
    v_stack_m5E0 = v_r15;
    goto loc_0091AAD7;
loc_0091AD86:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m604)) | (0xFFFFFFFFULL));
    v_stack_m604 = (unsigned int)(v_r14);
    goto loc_0091AAFB;
loc_0091AD99:
    v_stack_m568 = v_r15;
    v_r15 = (v_r15) + (368);
    v_stack_m5E0 = v_r15;
    if (v_stack_m608 < 0) goto loc_0091B069;
    result = PsReferencePrimaryTokenWithTag(v_stack_m5D8, (unsigned int)(0x746C6644ULL), v_stack_m5B0, a4);
    result = SeSecurityAttributePresent(result, v_rip + 2298071, v_stack_m5B0, a4);
    v_stack_m5E8 = (unsigned __int8)(result);
    result = ObFastDereferenceObject(v_stack_m5D8 + 584, result, (unsigned int)(0x746C6644ULL), a4);
    *(unsigned int *)(v_r15 + 336) = 0;
    result = (*(unsigned __int64 *)(v_stack_m5D8 + 1704)) << (12);
    *(unsigned __int64 *)(v_stack_m568 + 344) = result;
    *(unsigned __int64 *)(v_stack_m568 + 40) = v_stack_m438;
    *(unsigned int *)(v_stack_m568 + 48) = 0;
    if (v_stack_m5E8 != 0) goto loc_0091B019;
loc_0091AE3B:
    if (*(unsigned __int64 *)(v_stack_m5D8 + 1592) == 0) goto loc_0091AFF7;
    *(unsigned __int64 *)(v_stack_m568) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m568 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m568 + 32) = v_xmm0;
loc_0091AE68:
    if (condition_is_above_or_equal) goto loc_0091AF9B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m568 + 48))) & (0xFFFFFFE3ULL));
    result = (unsigned int)((result) | (2));
loc_0091AE81:
    *(unsigned int *)(v_stack_m568 + 48) = (unsigned int)(result);
loc_0091AE84:
    *(unsigned __int64 *)(v_stack_m568 + 360) = *(unsigned __int64 *)(v_stack_m5D8 + 1656);
    result = PsQueryProcessEnergyValues(v_stack_m5D8, v_stack_m398, (unsigned int)(0x746C6644ULL), a4);
loc_0091AEB3:
    *(unsigned __int64 *)(v_stack_m568 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m568 + 64 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m568 + 64 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m568 + 64 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m568 + 64 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m568 + 64 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m568 + 64 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m568 + 64 + 128 - 16) = v_xmm1;
    a2 = (2) - (1);
    if (condition_is_not_equal) goto loc_0091AEB3;
    *(unsigned __int64 *)(v_stack_m568 + 64 + 128) = v_xmm0;
    if (*(unsigned __int64 *)(v_stack_m5D8 + 672) == 0) goto loc_0091AFEA;
    *(unsigned int *)(v_r15 + 352) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m5D8 + 672) + 1468)));
loc_0091AF35:
    if ((*(unsigned int *)(v_stack_m5D8 + 68)) != 0) goto loc_0091AF92;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6994994))) == 0) goto loc_0091B030;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m5D8 + 136))) >> (7);
    result = (unsigned int)((result) & (15));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6989237 + result * 4)))) != 7) goto loc_0091AF77;
    if ((*(unsigned __int8 *)(v_stack_m5D8 + 839)) != 1) {
        a1 = 0;
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 6994726)) == 0) goto loc_0091B030;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6989237 + result * 4)) - 1)) & (0xFFFFFFFAULL)) != 0) goto loc_0091AFE4;
loc_0091AF92:
    goto loc_0091B030;
loc_0091AF9B:
    if (v_stack_m5D8 == (*(unsigned __int64 *)(v_rip + 6995222))) goto loc_0091B022;
    if (v_stack_m5D8 >= (*(unsigned __int64 *)(v_rip + 6995222))) goto loc_0091AFB8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m568 + 48))) & (0xFFFFFFE7ULL));
    result = (unsigned int)((result) | (6));
    goto loc_0091AE81;
loc_0091AFB8:
    if (*(unsigned __int64 *)(v_rip + 6144585) == 0) goto loc_0091B00C;
    a1 = (v_stack_m5D8 == (*(unsigned __int64 *)(v_rip + 6144585))) ? 1 : 0;
loc_0091AFCA:
    v_stack_m5CC = (unsigned __int8)(a1);
    if ((unsigned __int8)(a1) != 0) goto loc_0091B011;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 48))) & (0xFFFFFFE1ULL));
loc_0091AFDA:
    *(unsigned int *)(v_r15 + 48) = (unsigned int)(result);
    goto loc_0091AE84;
loc_0091AFE4:
    if ((unsigned __int8)(a1) == 0) goto loc_0091B030;
    goto loc_0091AF92;
loc_0091AFEA:
    *(unsigned int *)(v_r15 + 352) = 0;
    goto loc_0091AF35;
loc_0091AFF7:
    result = 0;
    *(unsigned __int64 *)(v_stack_m568) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m568 + 16) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m568 + 32) = 0;
    goto loc_0091AE68;
loc_0091B00C:
    goto loc_0091AFCA;
loc_0091B011:
    result = (unsigned int)((result) & (0xFFFFFFE9ULL));
    result = (unsigned int)((result) | (8));
    goto loc_0091AFDA;
loc_0091B019:
    *(unsigned int *)(v_stack_m568 + 48) = 1;
    goto loc_0091AE3B;
loc_0091B022:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m568 + 48))) & (0xFFFFFFE5ULL));
    result = (unsigned int)((result) | (4));
    goto loc_0091AE81;
loc_0091B030:
    goto loc_0091B057;
loc_0091B057:
    if (sign_flag) goto loc_0091B319;
loc_0091B069:
    if (((unsigned int)((unsigned int)(a5))) == 148) goto loc_0091B6C7;
loc_0091B07E:
loc_0091B083:
    if (((unsigned int)((unsigned int)(a5))) == 253) goto loc_0091B165;
    if (v_stack_m5D8 == (*(unsigned __int64 *)(v_rip + 6994649))) goto loc_0091B15B;
    if (v_stack_m5D8 != (*(unsigned __int64 *)(v_rip + 6994441))) goto loc_0091B322;
loc_0091B0B4:
    v_stack_m548 = v_rip - 9539772;
    v_stack_m5C0 = (unsigned int)(*(unsigned __int16 *)(v_rip - 9539772));
    v_stack_m57C = (unsigned int)(*(unsigned __int16 *)(v_rip - 9539772));
    v_stack_m540 = *(unsigned __int64 *)(v_rip - 9539772 + 8);
    if (((unsigned int)((unsigned int)(a5))) != 148) goto loc_0091B256;
loc_0091B0F1:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip - 9539772)))) + (9));
    v_r12 = (unsigned int)((v_r12) & (0xFFFFFFF8ULL));
    v_stack_m5C0 = (unsigned int)(v_r12);
    if (((unsigned int)(v_r12 + (unsigned int)(v_stack_m604) * 1)) < ((unsigned int)((unsigned int)(v_stack_m604)))) goto loc_0091B243;
    v_stack_m604 = (unsigned int)((unsigned int)(v_stack_m604) + v_r12 * 1);
loc_0091B119:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m604) + v_r12 * 1)))) <= v_stack_p10) goto loc_0091B369;
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
loc_0091B149:
    if (v_stack_m608 >= 0) goto loc_0091B4A0;
loc_0091B153:
loc_0091B15B:
    if (v_stack_m608 >= 0) goto loc_0091B519;
loc_0091B165:
    v_r13 = v_stack_m5D8;
    if (v_stack_m5D8 == (*(unsigned __int64 *)(v_rip + 6994436))) { v_r13 = 0; }
    result = ExGetNextProcess(v_r13, v_stack_m5C5, (unsigned int)(v_stack_m604) + v_r12 * 1, (unsigned int)(a5));
    v_stack_m5D8 = result;
loc_0091B184:
    if (result == 0) goto loc_0091B652;
    result = ExpSysInfoShouldSkipProcess(result, v_stack_m5C5, (unsigned int)(v_stack_m604) + v_r12 * 1, (unsigned int)(a5));
    if ((unsigned __int8)(result) != 0) goto loc_0091B63A;
    if (v_stack_p20 != 0) goto loc_0091BA3F;
loc_0091B1AB:
    result = PsGetProcessSessionId(result, v_stack_m5C5, (unsigned int)(v_stack_m604) + v_r12 * 1, (unsigned int)(a5));
    v_stack_m4F4 = (unsigned int)(result);
    if (v_stack_p20 != 0) goto loc_0091BA54;
loc_0091B1CD:
    result = PsIsProcessInSilo(result, v_stack_m4E0, (unsigned int)(v_stack_m604) + v_r12 * 1, (unsigned int)(a5));
    if ((unsigned __int8)(result) == 0) goto loc_0091B63A;
    if (((unsigned int)((unsigned int)(a5))) == 253) goto loc_0091B2B4;
    a2 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m604) + v_r12 * 1))))) + (v_stack_m4D0);
    a1 = (unsigned int)(((unsigned int)(v_stack_m558)) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m604) + v_r12 * 1)))));
    if (((unsigned int)((unsigned int)(a5))) == 252) goto loc_0091B57A;
    v_stack_m5A8 = a2;
    v_stack_m5F8 = (unsigned int)((unsigned int)(v_stack_m5B8));
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m604) + v_r12 * 1))))) goto loc_0091AA53;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m604) + v_r12 * 1))) | (0xFFFFFFFFULL));
    v_stack_m604 = (unsigned int)(v_r14);
    goto loc_0091AA5C;
loc_0091B243:
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    v_stack_m604 = (unsigned int)(v_r14);
    goto loc_0091B119;
loc_0091B256:
    if ((unsigned int)(a1) == 0) goto loc_0091B0F1;
    result = (a1) >> (1);
    v_stack_m540 = (unsigned int)(v_stack_m604) + v_r12 * 1 + result * 2;
loc_0091B275:
    if (((unsigned int)(v_stack_m604) + v_r12 * 1 + result * 2) == ((unsigned int)(v_stack_m604) + v_r12 * 1)) goto loc_0091B298;
    a2 = ((unsigned int)(v_stack_m604) + v_r12 * 1 + result * 2) - (2);
    v_stack_m540 = a2;
    if ((*(unsigned __int16 *)(a2)) == 92) goto loc_0091B28D;
    goto loc_0091B275;
loc_0091B28D:
    a2 = (a2) + (2);
    v_stack_m540 = a2;
loc_0091B298:
    result = (a2) - ((unsigned int)(v_stack_m604) + v_r12 * 1);
    result = (result) >> (1);
    result = (unsigned int)((result) + ((unsigned int)(result)));
    a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    v_stack_m57C = (unsigned int)(a1);
    goto loc_0091B0F1;
loc_0091B2B4:
    result = PsGetProcessActiveThreadCount(result, a2, (unsigned int)(v_stack_m604) + v_r12 * 1, (unsigned int)(a5));
    result = (unsigned int)((result) + (*(unsigned int *)(v_stack_m550 + 4)));
    *(unsigned int *)(v_stack_m550 + 4) = (unsigned int)(result);
    a2 = 0;
    result = ObGetProcessHandleCount(result, a2, (unsigned int)(v_stack_m604) + v_r12 * 1, (unsigned int)(a5));
    result = (unsigned int)((result) + (*(unsigned int *)(v_stack_m550 + 8)));
    *(unsigned int *)(v_stack_m550 + 8) = (unsigned int)(result);
    goto loc_0091B311;
loc_0091B311:
    if (!sign_flag) goto loc_0091B07E;
loc_0091B319:
    v_stack_m608 = (unsigned int)((unsigned int)(0xC0000095ULL));
    goto loc_0091BB54;
loc_0091B322:
    if (result == (*(unsigned __int64 *)(v_rip + 6994319))) goto loc_0091BB28;
    if (((*(unsigned int *)(result + 1532)) & (0x40000000ULL)) != 0) goto loc_0091B0B4;
    goto loc_0091B0B4;
loc_0091B353:
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m550 != 0) goto loc_0091AAD7;
    goto loc_0091BB54;
loc_0091B369:
    v_stack_m570 = v_stack_m5E0;
    result = *(unsigned __int64 *)(result + 848);
    v_rbx = v_stack_m550;
    if ((unsigned int)(result) != 0) {
        v_rbx = (unsigned int)(result);
        a3 = (unsigned int)(result);
        a1 = v_stack_m5E0;
        result = memcpy(a1, a2, a3, (unsigned int)(a5));
        v_rbx = (v_rbx) >> (1);
        result = v_stack_m5E0 + v_rbx * 2;
        v_stack_m570 = result;
    }
    *(unsigned __int16 *)(v_stack_m570) = 0;
    goto loc_0091B3D7;
loc_0091B3D7:
    if (sign_flag) goto loc_0091B319;
    goto loc_0091B149;
loc_0091B3EC:
    result = ExpCopyProcessInfo(v_stack_m5A8, result, v_stack_m5FC, v_stack_m458);
    v_stack_m600 = (unsigned int)(result);
    if (sign_flag) goto loc_0091BA7C;
    *(unsigned int *)(v_stack_m5A8 + 100) = (unsigned int)(v_rbx);
    *(unsigned __int64 *)(v_stack_m5A8 + 64) = 0;
    if (result == (*(unsigned __int64 *)(v_rip + 6993723))) {
    }
    result = *(unsigned __int64 *)(v_rip + 6994037);
    if (result == (*(unsigned __int64 *)(v_rip + 6994037))) {
        result = *(unsigned __int64 *)(v_rip + 5318809);
        result = (result) << (12);
        a1 = v_stack_m5A8;
        *(unsigned __int64 *)(a1 + 144) = result;
        *(unsigned __int64 *)(a1 + 8) = result;
    }
    goto loc_0091B493;
loc_0091B493:
    if (!sign_flag) goto loc_0091AA9F;
    goto loc_0091B319;
loc_0091B4A0:
    if (((unsigned int)(v_stack_m458)) == 252) goto loc_0091B4B7;
    goto loc_0091B4C3;
loc_0091B4B7:
loc_0091B4C3:
    result = (unsigned __int16)((v_stack_m570) - ((unsigned __int16)(v_stack_m5E0)));
    result = (unsigned __int16)((result) - (2));
    *(unsigned __int16 *)(v_stack_m590 + 32) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_stack_m590 + 32 + 2) = (unsigned __int16)((unsigned int)((unsigned int)(a1)));
    *(unsigned __int64 *)(v_stack_m590 + 32 + 8) = v_stack_m5E0;
    goto loc_0091B50C;
loc_0091B50C:
    if (!sign_flag) goto loc_0091B153;
    goto loc_0091B319;
loc_0091B519:
    result = v_stack_m590;
    if (((unsigned int)((unsigned int)((unsigned int)(a1)))) != 252) {
        result = v_stack_m5A8;
    }
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(v_stack_m5F8));
    goto loc_0091B56D;
loc_0091B56D:
    if (!sign_flag) goto loc_0091B165;
    goto loc_0091B319;
loc_0091B57A:
    v_stack_m590 = result;
    v_stack_m5F8 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(v_stack_m5F8))) < ((unsigned int)(v_r14))) goto loc_0091B63F;
    v_stack_m604 = (unsigned int)((unsigned int)(v_stack_m5F8));
loc_0091B598:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m5F8))))) > v_stack_p10) goto loc_0091BA61;
loc_0091B5B2:
    if (v_stack_m608 < 0) goto loc_0091B07E;
    *(unsigned __int64 *)(v_stack_m590 + 8) = *(unsigned __int64 *)(result + 464);
    *(unsigned __int64 *)(v_stack_m590 + 16) = *(unsigned __int64 *)(result + 720);
    *(unsigned __int64 *)(v_stack_m590 + 24) = *(unsigned __int64 *)(result + 1656);
    *(unsigned __int64 *)(v_stack_m590 + 40) = 0;
    goto loc_0091B61D;
loc_0091B61D:
    if (sign_flag) goto loc_0091B319;
    v_r15 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m5F8)))))) + (v_stack_m560);
    v_stack_m5E0 = v_r15;
    goto loc_0091B07E;
loc_0091B63A:
    goto loc_0091B165;
loc_0091B63F:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m5F8)))) | (0xFFFFFFFFULL));
    v_stack_m604 = (unsigned int)(v_r14);
    goto loc_0091B598;
loc_0091B652:
    if (v_stack_m608 < 0) goto loc_0091B6B1;
    if (((unsigned int)((unsigned int)((unsigned int)(a1)))) == 252) goto loc_0091BB34;
loc_0091B665:
    if (v_stack_m5A8 == 0) goto loc_0091B6B1;
loc_0091B66F:
    result = v_stack_m590;
    if (((unsigned int)((unsigned int)((unsigned int)(a1)))) != 252) {
        result = v_stack_m5A8;
    }
    *(unsigned int *)(result) = 0;
    goto loc_0091B6A9;
loc_0091B6A9:
    if (sign_flag) goto loc_0091B319;
loc_0091B6B1:
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
    *(unsigned int *)(v_stack_m5F0) = (unsigned int)(v_r14);
    goto loc_0091BB54;
loc_0091B6C7:
    result = PsReferencePrimaryTokenWithTag(result, (unsigned int)(0x746C6644ULL), v_stack_m5FC, v_stack_m458);
    v_stack_m4A8 = result;
    v_stack_m460 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m4A8 + 48), 1, v_stack_m5FC, v_stack_m458);
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4A8 + 152)) + 1);
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4A8 + 152)) + 1) * 4 + 8)) <= 68) {
        a3 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4A8 + 152)) + 1) * 4 + 8);
        a1 = v_stack_m3E8;
        result = memcpy(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4A8 + 152)), a3, v_stack_m458);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m4A8 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4A8 + 152)), a3, v_stack_m458);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m4A8 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4A8 + 152)), a3, v_stack_m458);
    v_stack_m57C = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4A8 + 152)) + 1) * 4 + 8);
    v_stack_m578 = 254;
    v_stack_m588 = 130;
    v_stack_m610 = 0;
    v_stack_m618 = v_stack_m588;
    result = RtlQueryPackageIdentity(v_stack_m4A8, v_stack_m148, v_stack_m578, v_stack_m1D8);
    v_stack_m600 = (unsigned int)(result);
    if (sign_flag) goto loc_0091BA9A;
loc_0091B7AD:
    result = ObFastDereferenceObject(v_stack_m5D8 + 584, v_stack_m4A8, (unsigned int)(0x746C6644ULL), v_stack_m1D8);
    v_rbx = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m4A8 + 152)) + 1) * 4 + 8 + 7) & (0xFFFFFFF8ULL));
    v_stack_m5C0 = (unsigned int)(v_rbx);
    if (((unsigned int)(v_rbx + (unsigned int)(v_stack_m604) * 1)) < ((unsigned int)((unsigned int)(v_stack_m604)))) goto loc_0091B917;
loc_0091B7E7:
    v_stack_m604 = (unsigned int)((unsigned int)(v_stack_m604) + v_rbx * 1);
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((unsigned int)((unsigned int)(v_stack_m604) + v_rbx * 1)) <= v_stack_p10) goto loc_0091B925;
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
loc_0091B82D:
    if ((v_stack_m578 - 1) <= ((unsigned int)(0xFFFFFFFEULL))) goto loc_0091B9C3;
loc_0091B847:
    if ((v_stack_m588 - 1) > ((unsigned int)(0xFFFFFFFEULL))) goto loc_0091B9B6;
    v_stack_m5C0 = (unsigned int)(v_stack_m588);
    if (((unsigned int)(v_stack_m588 + (unsigned int)(v_stack_m604) + v_rbx * 1 * 1)) < ((unsigned int)((unsigned int)(v_stack_m604) + v_rbx * 1))) goto loc_0091B9A3;
    v_stack_m604 = (unsigned int)(v_stack_m588 + (unsigned int)(v_stack_m604) + v_rbx * 1 * 1);
loc_0091B876:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_m588 + (unsigned int)(v_stack_m604) + v_rbx * 1 * 1)))) > v_stack_p10) goto loc_0091BA14;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m5E0))) - ((unsigned int)(v_stack_m568)));
    *(unsigned int *)(v_stack_m568 + 336) = (unsigned int)(result);
    result = memcpy(v_stack_m5E0, v_stack_m1D8, (unsigned int)(v_stack_m588), v_stack_m1D8);
    goto loc_0091B8F3;
loc_0091B8F3:
    if (sign_flag) goto loc_0091B319;
    v_r15 = (v_stack_m5E0) + ((unsigned int)(v_stack_m588));
    v_stack_m5E0 = v_r15;
loc_0091B90A:
    goto loc_0091B083;
loc_0091B917:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m588 + (unsigned int)(v_stack_m604) + v_rbx * 1 * 1))) | (0xFFFFFFFFULL));
    goto loc_0091B7E7;
loc_0091B925:
    *(unsigned int *)(v_stack_m568 + 52) = 368;
    result = memcpy(v_stack_m5E0, v_stack_m3E8, (unsigned int)((unsigned int)(v_r15)), v_stack_m1D8);
    goto loc_0091B98C;
loc_0091B98C:
    if (sign_flag) goto loc_0091B319;
    v_r15 = (v_stack_m5E0) + ((unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFEULL))));
    v_stack_m5E0 = v_r15;
    goto loc_0091B82D;
loc_0091B9A3:
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    v_stack_m604 = (unsigned int)(v_r14);
    goto loc_0091B876;
loc_0091B9B6:
    goto loc_0091B07E;
loc_0091B9C3:
    v_stack_m5C0 = (unsigned int)(v_stack_m5E0);
    if (((unsigned int)(v_stack_m5E0 + v_r14 * 1)) < ((unsigned int)(v_r14))) goto loc_0091BA2F;
    v_stack_m604 = (unsigned int)(v_stack_m5E0 + v_r14 * 1);
loc_0091B9D9:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_m5E0 + v_r14 * 1)))) <= v_stack_p10) goto loc_0091BAAF;
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 != 0) goto loc_0091B847;
    goto loc_0091BB54;
loc_0091BA14:
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 != 0) goto loc_0091B90A;
    goto loc_0091BB54;
loc_0091BA2F:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m5E0 + v_r14 * 1))) | (0xFFFFFFFFULL));
    v_stack_m604 = (unsigned int)(v_r14);
    goto loc_0091B9D9;
loc_0091BA3F:
    if (v_stack_m5D8 == (*(unsigned __int64 *)(v_rip + 6992170))) goto loc_0091B63A;
    goto loc_0091B1AB;
loc_0091BA54:
    if (((unsigned int)((unsigned int)(0xFFFFFFFEULL))) != (*(unsigned int *)(v_stack_m5E0))) goto loc_0091B63A;
    goto loc_0091B1CD;
loc_0091BA61:
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
    goto loc_0091B5B2;
loc_0091BA7C:
    v_stack_m608 = (unsigned int)(v_stack_m5F0);
    goto loc_0091BB54;
loc_0091BA85:
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)((unsigned int)(v_stack_m5BC))));
    v_stack_m604 = (unsigned int)(v_r14);
    goto loc_0091AAD7;
loc_0091BA9A:
    v_stack_m578 = 0;
    v_stack_m588 = 0;
    goto loc_0091B7AD;
loc_0091BAAF:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) - ((unsigned int)((unsigned int)(a5))));
    *(unsigned int *)((unsigned int)(a5) + 56) = (unsigned int)(result);
    result = memcpy(v_r15, v_stack_m148, (unsigned int)(v_stack_m578), v_stack_m1D8);
    goto loc_0091BB0C;
loc_0091BB0C:
    if (sign_flag) goto loc_0091B319;
    v_r15 = (v_r15) + ((unsigned int)(v_stack_m578));
    v_stack_m5E0 = v_r15;
    goto loc_0091B847;
loc_0091BB28:
    goto loc_0091B0B4;
loc_0091BB34:
    if (v_stack_m590 != 0) goto loc_0091B66F;
    if (((unsigned int)((unsigned int)(a5))) == 252) goto loc_0091B6B1;
    goto loc_0091B665;
loc_0091BB54:
    if (v_stack_m5D8 != 0) goto loc_0091BC54;
loc_0091BB5D:
    if (v_stack_m5B0 != 0) goto loc_0091BC73;
loc_0091BB6E:
loc_0091BB72:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m148, v_stack_m5B0, v_stack_m1D8);
    v_rsp = (v_rsp) + (0x600ULL);
    return result;
loc_0091BB96:
    v_stack_pA8 = 0;
    if (((unsigned int)((unsigned int)(a5))) == 253) goto loc_0091BBDF;
    v_stack_p80 = 624;
    v_stack_p90 = v_stack_pD8;
    result = 136;
    if (((unsigned int)((unsigned int)(a5))) == 5) { result = (unsigned int)(136 - 56); }
    v_stack_p7C = (unsigned int)(result);
    goto loc_0091A9A6;
loc_0091BBDF:
    v_stack_p3C = 0;
    v_stack_p80 = 12;
    v_stack_p34 = 12;
    v_stack_p7C = 0;
    v_stack_pE8 = v_stack_pD8;
    v_stack_p90 = 0;
    goto loc_0091A9AE;
loc_0091BC15:
    goto loc_0091BB72;
loc_0091BC28:
    result = ExCheckFullProcessInformationAccess((unsigned __int8)((unsigned int)(0xC0000095ULL)), v_stack_m148, v_stack_m5B0, v_stack_m1D8);
    if (sign_flag) goto loc_0091BB72;
    goto loc_0091A9EE;
loc_0091BC3D:
    if (v_stack_p648 == 0) goto loc_0091AA27;
    result = KeFlushProcessWriteBuffers((unsigned __int8)((unsigned int)(0xC0000095ULL)), v_stack_m148, v_stack_m5B0, v_stack_m1D8);
    goto loc_0091AA27;
loc_0091BC54:
    if (v_stack_m5D8 == (*(unsigned __int64 *)(v_rip + 6991637))) goto loc_0091BB5D;
    result = ObfDereferenceObjectWithTag(v_stack_m5D8, (unsigned int)(0x6E457350ULL), v_stack_m5B0, v_stack_m1D8);
    goto loc_0091BB5D;
loc_0091BC73:
    if ((*(unsigned __int64 *)(v_stack_m5B0 + 544)) == (*(unsigned __int64 *)(v_rip + 6991606))) goto loc_0091BB6E;
    result = ObfDereferenceObjectWithTag(v_stack_m5B0, (unsigned int)(0x6E457350ULL), v_stack_m5B0, v_stack_m1D8);
    goto loc_0091BB6E;
}
```

## 5. (Beta) C Style

```c
int64_t ExpGetProcessInformation(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m398;
    uint64_t v_stack_m3E8;
    uint64_t v_stack_m438;
    uint64_t v_stack_m458;
    uint64_t v_stack_m460;
    uint32_t v_stack_m468;
    uint64_t v_stack_m48;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m4D0;
    uint64_t v_stack_m4E0;
    uint32_t v_stack_m4E8;
    uint32_t v_stack_m4EC;
    uint32_t v_stack_m4F0;
    uint32_t v_stack_m4F4;
    uint32_t v_stack_m4F8;
    uint32_t v_stack_m4FC;
    uint32_t v_stack_m500;
    uint32_t v_stack_m504;
    uint32_t v_stack_m508;
    uint32_t v_stack_m50C;
    uint32_t v_stack_m510;
    uint64_t v_stack_m520;
    uint8_t v_stack_m525;
    uint8_t v_stack_m526;
    uint8_t v_stack_m527;
    uint8_t v_stack_m528;
    uint64_t v_stack_m530;
    uint64_t v_stack_m538;
    uint64_t v_stack_m540;
    uint64_t v_stack_m548;
    uint64_t v_stack_m550;
    uint32_t v_stack_m558;
    uint64_t v_stack_m560;
    uint64_t v_stack_m568;
    uint64_t v_stack_m570;
    uint64_t v_stack_m578;
    uint32_t v_stack_m57C;
    uint32_t v_stack_m580;
    uint64_t v_stack_m588;
    uint64_t v_stack_m590;
    uint32_t v_stack_m598;
    uint64_t v_stack_m5A0;
    uint64_t v_stack_m5A8;
    uint64_t v_stack_m5B0;
    uint32_t v_stack_m5B8;
    uint32_t v_stack_m5BC;
    uint32_t v_stack_m5C0;
    uint8_t v_stack_m5C5;
    uint8_t v_stack_m5CC;
    uint64_t v_stack_m5D8;
    uint64_t v_stack_m5E0;
    uint8_t v_stack_m5E8;
    uint64_t v_stack_m5F0;
    uint32_t v_stack_m5F8;
    uint8_t v_stack_m5FC;
    uint32_t v_stack_m600;
    uint32_t v_stack_m604;
    uint32_t v_stack_m608;
    uint64_t v_stack_m610;
    uint64_t v_stack_m618;
    uint32_t v_stack_m638;
    uint32_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p34;
    uint8_t v_stack_p3C;
    uint32_t v_stack_p648;
    uint32_t v_stack_p7C;
    uint32_t v_stack_p80;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE8;

    v_stack_p20 = Arg4;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (0x600ULL);
    result = (*(uint64_t *)(v_rip + 0x4EFEA6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m5F0 = Arg3;
    v_stack_m560 = Arg1;
    v_stack_m4D0 = Arg1;
    v_stack_m5A0 = Arg3;
    local_rdi = 0;
    v_stack_m588 = 0;
    Arg2 = 0;
    result = memset(v_stack_m398, Arg2, 440, Arg4);
    v_stack_m5C0 = 0;
    v_stack_m57C = 0;
    v_stack_m5F8 = 0;
    v_stack_m578 = 0;
    v_stack_m5D8 = 0;
    Arg2 = 0;
    result = memset(v_stack_m458, Arg2, local_rdi + 104, Arg4);
    v_stack_m5E8 = 0;
    v_stack_m5B0 = 0;
    v_stack_m530 = v_xmm0;
    v_stack_m520 = v_xmm0;
    v_stack_m604 = 0;
    v_stack_m570 = 0;
    Arg2 = 0;
    result = memset(v_stack_m3E8, Arg2, local_rdi + 68, Arg4);
    v_stack_m5E0 = 0;
    v_stack_m598 = 0;
    if (Arg3 != 0) {
        *(uint32_t *)(Arg3) = 0;
    }
    if (((uint32_t)((uint32_t)(Arg5))) != 252) goto loc_0091BB96;
    v_stack_m5FC = 0;
    v_stack_m5B8 = 48;
    v_stack_m5BC = 0;
    v_stack_m590 = v_stack_m560;
    v_stack_m5A8 = 0;
loc_0091A9A6:
    v_stack_m550 = 0;
loc_0091A9AE:
    v_stack_m558 = (uint32_t)((uint32_t)(v_stack_m5B8));
    if (v_stack_p10 < ((uint32_t)((uint32_t)(v_stack_m5B8)))) goto loc_0091BC15;
    local_rbx = (uint32_t)((Arg3) & (0xC0000004ULL));
    if (((uint32_t)((uint32_t)(Arg5))) == 148) goto loc_0091BC28;
loc_0091A9EE:
    result = ExIsRestrictedCaller((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m598, local_rdi + 68, Arg4);
    v_stack_m580 = (uint32_t)(result);
    v_stack_m600 = 0;
    if (((uint32_t)((uint32_t)(Arg5) - 252)) > 1) goto loc_0091BC3D;
loc_0091AA27:
    result = PsGetCurrentServerSilo(1, v_stack_m598, local_rdi + 68, Arg4);
    v_stack_m4E0 = result;
    v_stack_m5D8 = *(uint64_t *)(v_rip + 0x6AC135);
    v_stack_m608 = (uint32_t)(local_rbx);
    goto loc_0091B184;
loc_0091AA53:
    v_stack_m604 = 1;
loc_0091AA5C:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    Arg2 = 0;
    result = memset(v_stack_m458, Arg2, Arg2 + 104, Arg4);
    if (1 <= v_stack_p10) goto loc_0091B3EC;
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
loc_0091AA9F:
    local_r15 = (v_stack_m5A8) + (256);
    v_stack_m5E0 = local_r15;
    Arg2 = 0;
loc_0091AAB5:
    result = ExpGetNextProcessThread(*(uint64_t *)(v_rip + 0x6AC135), Arg2, Arg2 + 104, Arg4);
    v_stack_m5B0 = result;
    if (result == 0) goto loc_0091AD99;
    if ((*(uint8_t *)(result + 0x4)) == 0) goto loc_0091AAE1;
loc_0091AAD7:
    goto loc_0091AAB5;
loc_0091AAE1:
    if (((uint32_t)(1 + (uint32_t)(v_stack_m5BC) * 1)) < 1) goto loc_0091AD86;
    v_stack_m604 = (uint32_t)(1 + (uint32_t)(v_stack_m5BC) * 1);
loc_0091AAFB:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((uint32_t)((uint32_t)((uint32_t)(1 + (uint32_t)(v_stack_m5BC) * 1)))) > v_stack_p10) goto loc_0091B353;
    result = KeQueryValuesThread(v_stack_m5B0, v_stack_m530, result, Arg4);
    if (v_stack_m528 == 4) goto loc_0091BA85;
    *(uint32_t *)(local_r15 + 0x18) = (uint32_t)((uint32_t)(v_stack_m530));
    *(uint32_t *)(local_r15 + 0x44) = (uint32_t)(v_stack_m528);
    *(uint32_t *)(local_r15 + 0x48) = (uint32_t)(v_stack_m527);
    *(uint32_t *)(local_r15 + 0x38) = (uint32_t)((int8_t)(v_stack_m526));
    *(uint32_t *)(local_r15 + 0x3C) = (uint32_t)((int8_t)(v_stack_m525));
    result = ((uint32_t)(*(uint32_t *)(v_stack_m5B0 + 0x28C))) * ((uint32_t)(*(uint32_t *)(v_rip + 0x6ABF23)));
    *(uint64_t *)(local_r15) = result;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m5B0 + 0x2DC))) * ((uint32_t)(*(uint32_t *)(v_rip + 0x6ABF23)));
    *(uint64_t *)(local_r15 + 0x8) = result;
    *(uint64_t *)(local_r15 + 0x10) = *(uint64_t *)(v_stack_m5B0 + 0x4C0);
    *(uint32_t *)(local_r15 + 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m5B0 + 0x154)));
    *(uint64_t *)(local_r15 + 0x28) = v_xmm0;
    if (((*(uint32_t *)(v_stack_m5B0 + 0x74)) & (0x400ULL)) != 0) goto loc_0091ACF6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m5B0 + 0x5A8)))) & (8)) != 0) goto loc_0091ACA3;
    result = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m5B0 + 0x5A8)))) & (8)) == 0) { result = *(uint64_t *)(v_stack_m5B0 + 0x4E0); }
loc_0091AC06:
loc_0091AC19:
    v_stack_m538 = result;
    if (v_stack_m598 == 0) goto loc_0091ACAB;
loc_0091AC34:
    *(uint64_t *)(v_stack_m5E0 + 0x20) = 0;
loc_0091AC38:
    if (v_stack_m5FC == 0) goto loc_0091AD30;
    if (v_stack_m598 == 0) goto loc_0091ACBD;
loc_0091AC4C:
    *(uint64_t *)(v_stack_m5E0 + 0x50) = 0;
    *(uint64_t *)(v_stack_m5E0 + 0x58) = 0;
loc_0091AC54:
    v_stack_m538 = *(uint64_t *)(v_stack_m5B0 + 0x560);
    if (v_stack_m598 == 0) goto loc_0091AD15;
loc_0091AC78:
    *(uint64_t *)(v_stack_m5E0 + 0x60) = 0;
loc_0091AC7C:
    *(uint64_t *)(v_stack_m5E0 + 0x68) = *(uint64_t *)(v_stack_m5B0 + 0xF0);
    *(uint64_t *)(v_stack_m5E0 + 0x70) = 0;
    *(uint64_t *)(v_stack_m5E0 + 0x78) = 0;
    *(uint64_t *)(v_stack_m5E0 + 0x80) = 0;
    goto loc_0091AD30;
loc_0091ACA3:
    goto loc_0091AC06;
loc_0091ACAB:
    if (v_stack_m580 != 0) goto loc_0091AD0A;
loc_0091ACB4:
    *(uint64_t *)(v_stack_m5E0 + 0x20) = 0;
    goto loc_0091AC38;
loc_0091ACBD:
    if (v_stack_m580 != 0) goto loc_0091AC4C;
    *(uint64_t *)(v_stack_m5E0 + 0x50) = *(uint64_t *)(v_stack_m5B0 + 0x38);
    *(uint64_t *)(v_stack_m5E0 + 0x58) = *(uint64_t *)(v_stack_m5B0 + 0x30);
    goto loc_0091AC54;
loc_0091ACF6:
    goto loc_0091AC19;
loc_0091AD0A:
    if ((*(uint64_t *)(v_stack_m5B0 + 0x560)) > v_stack_m530) goto loc_0091AC34;
    goto loc_0091ACB4;
loc_0091AD15:
    if (v_stack_m580 == 0) goto loc_0091AD27;
    if ((*(uint64_t *)(v_stack_m5B0 + 0xF0)) > v_stack_m530) goto loc_0091AC78;
loc_0091AD27:
    *(uint64_t *)(v_stack_m5E0 + 0x60) = *(uint64_t *)(v_stack_m5B0 + 0xF0);
    goto loc_0091AC7C;
loc_0091AD30:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m5A8 + 0x4))) + 1);
    *(uint32_t *)(v_stack_m5A8 + 0x4) = (uint32_t)(result);
    goto loc_0091AD6D;
loc_0091AD6D:
    if (sign_flag) goto loc_0091B319;
    local_r15 = (v_stack_m5E0) + ((uint32_t)(v_stack_m5BC));
    v_stack_m5E0 = local_r15;
    goto loc_0091AAD7;
loc_0091AD86:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m604)) | (0xFFFFFFFFULL));
    v_stack_m604 = (uint32_t)(local_r14);
    goto loc_0091AAFB;
loc_0091AD99:
    v_stack_m568 = local_r15;
    local_r15 = (local_r15) + (368);
    v_stack_m5E0 = local_r15;
    if (v_stack_m608 < 0) goto loc_0091B069;
    result = PsReferencePrimaryTokenWithTag(v_stack_m5D8, (uint32_t)(0x746C6644ULL), v_stack_m5B0, Arg4);
    result = SeSecurityAttributePresent(result, v_rip + 2298071, v_stack_m5B0, Arg4);
    v_stack_m5E8 = (uint8_t)(result);
    result = ObFastDereferenceObject(v_stack_m5D8 + 584, result, (uint32_t)(0x746C6644ULL), Arg4);
    *(uint32_t *)(local_r15 + 0x150) = 0;
    result = (*(uint64_t *)(v_stack_m5D8 + 0x6A8)) << (12);
    *(uint64_t *)(v_stack_m568 + 0x158) = result;
    *(uint64_t *)(v_stack_m568 + 0x28) = v_stack_m438;
    *(uint32_t *)(v_stack_m568 + 0x30) = 0;
    if (v_stack_m5E8 != 0) goto loc_0091B019;
loc_0091AE3B:
    if (*(uint64_t *)(v_stack_m5D8 + 0x638) == 0) goto loc_0091AFF7;
    *(uint64_t *)(v_stack_m568) = v_xmm0;
    *(uint64_t *)(v_stack_m568 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m568 + 0x20) = v_xmm0;
loc_0091AE68:
    if (condition_is_above_or_equal) goto loc_0091AF9B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m568 + 0x30))) & (0xFFFFFFE3ULL));
    result = (uint32_t)((result) | (2));
loc_0091AE81:
    *(uint32_t *)(v_stack_m568 + 0x30) = (uint32_t)(result);
loc_0091AE84:
    *(uint64_t *)(v_stack_m568 + 0x168) = *(uint64_t *)(v_stack_m5D8 + 0x678);
    result = PsQueryProcessEnergyValues(v_stack_m5D8, v_stack_m398, (uint32_t)(0x746C6644ULL), Arg4);
loc_0091AEB3:
    *(uint64_t *)(v_stack_m568 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m568 + 0x40 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m568 + 0x40 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m568 + 0x40 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m568 + 0x40 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m568 + 0x40 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_m568 + 0x40 + 0x60) = v_xmm0;
    *(uint64_t *)(v_stack_m568 + 0x40 + 0x80 - 0x10) = v_xmm1;
    Arg2 = (2) - (1);
    if (condition_is_not_equal) goto loc_0091AEB3;
    *(uint64_t *)(v_stack_m568 + 0x40 + 0x80) = v_xmm0;
    if (*(uint64_t *)(v_stack_m5D8 + 0x2A0) == 0) goto loc_0091AFEA;
    *(uint32_t *)(local_r15 + 0x160) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m5D8 + 0x2A0) + 0x5BC)));
loc_0091AF35:
    if ((*(uint32_t *)(v_stack_m5D8 + 0x44)) != 0) goto loc_0091AF92;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6ABC32))) == 0) goto loc_0091B030;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m5D8 + 0x88))) >> (7);
    result = (uint32_t)((result) & (15));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6AA5B5 + result * 4)))) != 7) goto loc_0091AF77;
    if ((*(uint8_t *)(v_stack_m5D8 + 0x347)) != 1) {
        Arg1 = 0;
    }
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x6ABB26)) == 0) goto loc_0091B030;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6AA5B5 + result * 4)) - 1)) & (0xFFFFFFFAULL)) != 0) goto loc_0091AFE4;
loc_0091AF92:
    goto loc_0091B030;
loc_0091AF9B:
    if (v_stack_m5D8 == (*(uint64_t *)(v_rip + 0x6ABD16))) goto loc_0091B022;
    if (v_stack_m5D8 >= (*(uint64_t *)(v_rip + 0x6ABD16))) goto loc_0091AFB8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m568 + 0x30))) & (0xFFFFFFE7ULL));
    result = (uint32_t)((result) | (6));
    goto loc_0091AE81;
loc_0091AFB8:
    if (*(uint64_t *)(v_rip + 0x5DC249) == 0) goto loc_0091B00C;
    Arg1 = (v_stack_m5D8 == (*(uint64_t *)(v_rip + 0x5DC249))) ? 1 : 0;
loc_0091AFCA:
    v_stack_m5CC = (uint8_t)(Arg1);
    if ((uint8_t)(Arg1) != 0) goto loc_0091B011;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x30))) & (0xFFFFFFE1ULL));
loc_0091AFDA:
    *(uint32_t *)(local_r15 + 0x30) = (uint32_t)(result);
    goto loc_0091AE84;
loc_0091AFE4:
    if ((uint8_t)(Arg1) == 0) goto loc_0091B030;
    goto loc_0091AF92;
loc_0091AFEA:
    *(uint32_t *)(local_r15 + 0x160) = 0;
    goto loc_0091AF35;
loc_0091AFF7:
    result = 0;
    *(uint64_t *)(v_stack_m568) = v_xmm0;
    *(uint64_t *)(v_stack_m568 + 0x10) = v_xmm0;
    *(uint64_t *)(v_stack_m568 + 0x20) = 0;
    goto loc_0091AE68;
loc_0091B00C:
    goto loc_0091AFCA;
loc_0091B011:
    result = (uint32_t)((result) & (0xFFFFFFE9ULL));
    result = (uint32_t)((result) | (8));
    goto loc_0091AFDA;
loc_0091B019:
    *(uint32_t *)(v_stack_m568 + 0x30) = 1;
    goto loc_0091AE3B;
loc_0091B022:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m568 + 0x30))) & (0xFFFFFFE5ULL));
    result = (uint32_t)((result) | (4));
    goto loc_0091AE81;
loc_0091B030:
    goto loc_0091B057;
loc_0091B057:
    if (sign_flag) goto loc_0091B319;
loc_0091B069:
    if (((uint32_t)((uint32_t)(Arg5))) == 148) goto loc_0091B6C7;
loc_0091B07E:
loc_0091B083:
    if (((uint32_t)((uint32_t)(Arg5))) == 253) goto loc_0091B165;
    if (v_stack_m5D8 == (*(uint64_t *)(v_rip + 0x6ABAD9))) goto loc_0091B15B;
    if (v_stack_m5D8 != (*(uint64_t *)(v_rip + 0x6ABA09))) goto loc_0091B322;
loc_0091B0B4:
    v_stack_m548 = v_rip - 9539772;
    v_stack_m5C0 = (uint32_t)(*(uint16_t *)(v_rip - 0x9190BC));
    v_stack_m57C = (uint32_t)(*(uint16_t *)(v_rip - 0x9190BC));
    v_stack_m540 = *(uint64_t *)(v_rip - 0x9190BC + 0x8);
    if (((uint32_t)((uint32_t)(Arg5))) != 148) goto loc_0091B256;
loc_0091B0F1:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip - 0x9190BC)))) + (9));
    local_r12 = (uint32_t)((local_r12) & (0xFFFFFFF8ULL));
    v_stack_m5C0 = (uint32_t)(local_r12);
    if (((uint32_t)(local_r12 + (uint32_t)(v_stack_m604) * 1)) < ((uint32_t)((uint32_t)(v_stack_m604)))) goto loc_0091B243;
    v_stack_m604 = (uint32_t)((uint32_t)(v_stack_m604) + local_r12 * 1);
loc_0091B119:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m604) + local_r12 * 1)))) <= v_stack_p10) goto loc_0091B369;
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
loc_0091B149:
    if (v_stack_m608 >= 0) goto loc_0091B4A0;
loc_0091B153:
loc_0091B15B:
    if (v_stack_m608 >= 0) goto loc_0091B519;
loc_0091B165:
    local_r13 = v_stack_m5D8;
    if (v_stack_m5D8 == (*(uint64_t *)(v_rip + 0x6ABA04))) { local_r13 = 0; }
    result = ExGetNextProcess(local_r13, v_stack_m5C5, (uint32_t)(v_stack_m604) + local_r12 * 1, (uint32_t)(Arg5));
    v_stack_m5D8 = result;
loc_0091B184:
    if (result == 0) goto loc_0091B652;
    result = ExpSysInfoShouldSkipProcess(result, v_stack_m5C5, (uint32_t)(v_stack_m604) + local_r12 * 1, (uint32_t)(Arg5));
    if ((uint8_t)(result) != 0) goto loc_0091B63A;
    if (v_stack_p20 != 0) goto loc_0091BA3F;
loc_0091B1AB:
    result = PsGetProcessSessionId(result, v_stack_m5C5, (uint32_t)(v_stack_m604) + local_r12 * 1, (uint32_t)(Arg5));
    v_stack_m4F4 = (uint32_t)(result);
    if (v_stack_p20 != 0) goto loc_0091BA54;
loc_0091B1CD:
    result = PsIsProcessInSilo(result, v_stack_m4E0, (uint32_t)(v_stack_m604) + local_r12 * 1, (uint32_t)(Arg5));
    if ((uint8_t)(result) == 0) goto loc_0091B63A;
    if (((uint32_t)((uint32_t)(Arg5))) == 253) goto loc_0091B2B4;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m604) + local_r12 * 1))))) + (v_stack_m4D0);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m558)) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m604) + local_r12 * 1)))));
    if (((uint32_t)((uint32_t)(Arg5))) == 252) goto loc_0091B57A;
    v_stack_m5A8 = Arg2;
    v_stack_m5F8 = (uint32_t)((uint32_t)(v_stack_m5B8));
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m604) + local_r12 * 1))))) goto loc_0091AA53;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m604) + local_r12 * 1))) | (0xFFFFFFFFULL));
    v_stack_m604 = (uint32_t)(local_r14);
    goto loc_0091AA5C;
loc_0091B243:
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    v_stack_m604 = (uint32_t)(local_r14);
    goto loc_0091B119;
loc_0091B256:
    if ((uint32_t)(Arg1) == 0) goto loc_0091B0F1;
    result = (Arg1) >> (1);
    v_stack_m540 = (uint32_t)(v_stack_m604) + local_r12 * 1 + result * 2;
loc_0091B275:
    if (((uint32_t)(v_stack_m604) + local_r12 * 1 + result * 2) == ((uint32_t)(v_stack_m604) + local_r12 * 1)) goto loc_0091B298;
    Arg2 = ((uint32_t)(v_stack_m604) + local_r12 * 1 + result * 2) - (2);
    v_stack_m540 = Arg2;
    if ((*(uint16_t *)(Arg2)) == 92) goto loc_0091B28D;
    goto loc_0091B275;
loc_0091B28D:
    Arg2 = (Arg2) + (2);
    v_stack_m540 = Arg2;
loc_0091B298:
    result = (Arg2) - ((uint32_t)(v_stack_m604) + local_r12 * 1);
    result = (result) >> (1);
    result = (uint32_t)((result) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    v_stack_m57C = (uint32_t)(Arg1);
    goto loc_0091B0F1;
loc_0091B2B4:
    result = PsGetProcessActiveThreadCount(result, Arg2, (uint32_t)(v_stack_m604) + local_r12 * 1, (uint32_t)(Arg5));
    result = (uint32_t)((result) + (*(uint32_t *)(v_stack_m550 + 0x4)));
    *(uint32_t *)(v_stack_m550 + 0x4) = (uint32_t)(result);
    Arg2 = 0;
    result = ObGetProcessHandleCount(result, Arg2, (uint32_t)(v_stack_m604) + local_r12 * 1, (uint32_t)(Arg5));
    result = (uint32_t)((result) + (*(uint32_t *)(v_stack_m550 + 0x8)));
    *(uint32_t *)(v_stack_m550 + 0x8) = (uint32_t)(result);
    goto loc_0091B311;
loc_0091B311:
    if (!sign_flag) goto loc_0091B07E;
loc_0091B319:
    v_stack_m608 = (uint32_t)((uint32_t)(0xC0000095ULL));
    goto loc_0091BB54;
loc_0091B322:
    if (result == (*(uint64_t *)(v_rip + 0x6AB98F))) goto loc_0091BB28;
    if (((*(uint32_t *)(result + 0x5FC)) & (0x40000000ULL)) != 0) goto loc_0091B0B4;
    goto loc_0091B0B4;
loc_0091B353:
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m550 != 0) goto loc_0091AAD7;
    goto loc_0091BB54;
loc_0091B369:
    v_stack_m570 = v_stack_m5E0;
    result = *(uint64_t *)(result + 0x350);
    local_rbx = v_stack_m550;
    if ((uint32_t)(result) != 0) {
        local_rbx = (uint32_t)(result);
        Arg3 = (uint32_t)(result);
        Arg1 = v_stack_m5E0;
        result = memcpy(Arg1, Arg2, Arg3, (uint32_t)(Arg5));
        local_rbx = (local_rbx) >> (1);
        result = v_stack_m5E0 + local_rbx * 2;
        v_stack_m570 = result;
    }
    *(uint16_t *)(v_stack_m570) = 0;
    goto loc_0091B3D7;
loc_0091B3D7:
    if (sign_flag) goto loc_0091B319;
    goto loc_0091B149;
loc_0091B3EC:
    result = ExpCopyProcessInfo(v_stack_m5A8, result, v_stack_m5FC, v_stack_m458);
    v_stack_m600 = (uint32_t)(result);
    if (sign_flag) goto loc_0091BA7C;
    *(uint32_t *)(v_stack_m5A8 + 0x64) = (uint32_t)(local_rbx);
    *(uint64_t *)(v_stack_m5A8 + 0x40) = 0;
    if (result == (*(uint64_t *)(v_rip + 0x6AB73B))) {
    }
    result = *(uint64_t *)(v_rip + 0x6AB875);
    if (result == (*(uint64_t *)(v_rip + 0x6AB875))) {
        result = *(uint64_t *)(v_rip + 0x512899);
        result = (result) << (12);
        Arg1 = v_stack_m5A8;
        *(uint64_t *)(Arg1 + 0x90) = result;
        *(uint64_t *)(Arg1 + 0x8) = result;
    }
    goto loc_0091B493;
loc_0091B493:
    if (!sign_flag) goto loc_0091AA9F;
    goto loc_0091B319;
loc_0091B4A0:
    if (((uint32_t)(v_stack_m458)) == 252) goto loc_0091B4B7;
    goto loc_0091B4C3;
loc_0091B4B7:
loc_0091B4C3:
    result = (uint16_t)((v_stack_m570) - ((uint16_t)(v_stack_m5E0)));
    result = (uint16_t)((result) - (2));
    *(uint16_t *)(v_stack_m590 + 0x20) = (uint16_t)(result);
    *(uint16_t *)(v_stack_m590 + 0x20 + 0x2) = (uint16_t)((uint32_t)((uint32_t)(Arg1)));
    *(uint64_t *)(v_stack_m590 + 0x20 + 0x8) = v_stack_m5E0;
    goto loc_0091B50C;
loc_0091B50C:
    if (!sign_flag) goto loc_0091B153;
    goto loc_0091B319;
loc_0091B519:
    result = v_stack_m590;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg1)))) != 252) {
        result = v_stack_m5A8;
    }
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(v_stack_m5F8));
    goto loc_0091B56D;
loc_0091B56D:
    if (!sign_flag) goto loc_0091B165;
    goto loc_0091B319;
loc_0091B57A:
    v_stack_m590 = result;
    v_stack_m5F8 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(v_stack_m5F8))) < ((uint32_t)(local_r14))) goto loc_0091B63F;
    v_stack_m604 = (uint32_t)((uint32_t)(v_stack_m5F8));
loc_0091B598:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m5F8))))) > v_stack_p10) goto loc_0091BA61;
loc_0091B5B2:
    if (v_stack_m608 < 0) goto loc_0091B07E;
    *(uint64_t *)(v_stack_m590 + 0x8) = *(uint64_t *)(result + 0x1D0);
    *(uint64_t *)(v_stack_m590 + 0x10) = *(uint64_t *)(result + 0x2D0);
    *(uint64_t *)(v_stack_m590 + 0x18) = *(uint64_t *)(result + 0x678);
    *(uint64_t *)(v_stack_m590 + 0x28) = 0;
    goto loc_0091B61D;
loc_0091B61D:
    if (sign_flag) goto loc_0091B319;
    local_r15 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m5F8)))))) + (v_stack_m560);
    v_stack_m5E0 = local_r15;
    goto loc_0091B07E;
loc_0091B63A:
    goto loc_0091B165;
loc_0091B63F:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m5F8)))) | (0xFFFFFFFFULL));
    v_stack_m604 = (uint32_t)(local_r14);
    goto loc_0091B598;
loc_0091B652:
    if (v_stack_m608 < 0) goto loc_0091B6B1;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg1)))) == 252) goto loc_0091BB34;
loc_0091B665:
    if (v_stack_m5A8 == 0) goto loc_0091B6B1;
loc_0091B66F:
    result = v_stack_m590;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg1)))) != 252) {
        result = v_stack_m5A8;
    }
    *(uint32_t *)(result) = 0;
    goto loc_0091B6A9;
loc_0091B6A9:
    if (sign_flag) goto loc_0091B319;
loc_0091B6B1:
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
    *(uint32_t *)(v_stack_m5F0) = (uint32_t)(local_r14);
    goto loc_0091BB54;
loc_0091B6C7:
    result = PsReferencePrimaryTokenWithTag(result, (uint32_t)(0x746C6644ULL), v_stack_m5FC, v_stack_m458);
    v_stack_m4A8 = result;
    v_stack_m460 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - (1));
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m4A8 + 0x30), 1, v_stack_m5FC, v_stack_m458);
    result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m4A8 + 0x98)) + 0x1);
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m4A8 + 0x98)) + 0x1) * 4 + 8)) <= 68) {
        Arg3 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m4A8 + 0x98)) + 0x1) * 4 + 8);
        Arg1 = v_stack_m3E8;
        result = memcpy(Arg1, *(uint64_t *)(*(uint64_t *)(v_stack_m4A8 + 0x98)), Arg3, v_stack_m458);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m4A8 + 0x30), *(uint64_t *)(*(uint64_t *)(v_stack_m4A8 + 0x98)), Arg3, v_stack_m458);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m4A8 + 0x30), *(uint64_t *)(*(uint64_t *)(v_stack_m4A8 + 0x98)), Arg3, v_stack_m458);
    v_stack_m57C = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m4A8 + 0x98)) + 0x1) * 4 + 8);
    v_stack_m578 = 254;
    v_stack_m588 = 130;
    v_stack_m610 = 0;
    v_stack_m618 = v_stack_m588;
    result = RtlQueryPackageIdentity(v_stack_m4A8, v_stack_m148, v_stack_m578, v_stack_m1D8);
    v_stack_m600 = (uint32_t)(result);
    if (sign_flag) goto loc_0091BA9A;
loc_0091B7AD:
    result = ObFastDereferenceObject(v_stack_m5D8 + 584, v_stack_m4A8, (uint32_t)(0x746C6644ULL), v_stack_m1D8);
    local_rbx = (uint32_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m4A8 + 0x98)) + 0x1) * 4 + 8 + 7) & (0xFFFFFFF8ULL));
    v_stack_m5C0 = (uint32_t)(local_rbx);
    if (((uint32_t)(local_rbx + (uint32_t)(v_stack_m604) * 1)) < ((uint32_t)((uint32_t)(v_stack_m604)))) goto loc_0091B917;
loc_0091B7E7:
    v_stack_m604 = (uint32_t)((uint32_t)(v_stack_m604) + local_rbx * 1);
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((uint32_t)((uint32_t)(v_stack_m604) + local_rbx * 1)) <= v_stack_p10) goto loc_0091B925;
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
loc_0091B82D:
    if ((v_stack_m578 - 1) <= ((uint32_t)(0xFFFFFFFEULL))) goto loc_0091B9C3;
loc_0091B847:
    if ((v_stack_m588 - 1) > ((uint32_t)(0xFFFFFFFEULL))) goto loc_0091B9B6;
    v_stack_m5C0 = (uint32_t)(v_stack_m588);
    if (((uint32_t)(v_stack_m588 + (uint32_t)(v_stack_m604) + local_rbx * 1 * 1)) < ((uint32_t)((uint32_t)(v_stack_m604) + local_rbx * 1))) goto loc_0091B9A3;
    v_stack_m604 = (uint32_t)(v_stack_m588 + (uint32_t)(v_stack_m604) + local_rbx * 1 * 1);
loc_0091B876:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_m588 + (uint32_t)(v_stack_m604) + local_rbx * 1 * 1)))) > v_stack_p10) goto loc_0091BA14;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m5E0))) - ((uint32_t)(v_stack_m568)));
    *(uint32_t *)(v_stack_m568 + 0x150) = (uint32_t)(result);
    result = memcpy(v_stack_m5E0, v_stack_m1D8, (uint32_t)(v_stack_m588), v_stack_m1D8);
    goto loc_0091B8F3;
loc_0091B8F3:
    if (sign_flag) goto loc_0091B319;
    local_r15 = (v_stack_m5E0) + ((uint32_t)(v_stack_m588));
    v_stack_m5E0 = local_r15;
loc_0091B90A:
    goto loc_0091B083;
loc_0091B917:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m588 + (uint32_t)(v_stack_m604) + local_rbx * 1 * 1))) | (0xFFFFFFFFULL));
    goto loc_0091B7E7;
loc_0091B925:
    *(uint32_t *)(v_stack_m568 + 0x34) = 368;
    result = memcpy(v_stack_m5E0, v_stack_m3E8, (uint32_t)((uint32_t)(local_r15)), v_stack_m1D8);
    goto loc_0091B98C;
loc_0091B98C:
    if (sign_flag) goto loc_0091B319;
    local_r15 = (v_stack_m5E0) + ((uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFEULL))));
    v_stack_m5E0 = local_r15;
    goto loc_0091B82D;
loc_0091B9A3:
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    v_stack_m604 = (uint32_t)(local_r14);
    goto loc_0091B876;
loc_0091B9B6:
    goto loc_0091B07E;
loc_0091B9C3:
    v_stack_m5C0 = (uint32_t)(v_stack_m5E0);
    if (((uint32_t)(v_stack_m5E0 + local_r14 * 1)) < ((uint32_t)(local_r14))) goto loc_0091BA2F;
    v_stack_m604 = (uint32_t)(v_stack_m5E0 + local_r14 * 1);
loc_0091B9D9:
    v_stack_m600 = 0;
    if (sign_flag) goto loc_0091B319;
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_m5E0 + local_r14 * 1)))) <= v_stack_p10) goto loc_0091BAAF;
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 != 0) goto loc_0091B847;
    goto loc_0091BB54;
loc_0091BA14:
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 != 0) goto loc_0091B90A;
    goto loc_0091BB54;
loc_0091BA2F:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m5E0 + local_r14 * 1))) | (0xFFFFFFFFULL));
    v_stack_m604 = (uint32_t)(local_r14);
    goto loc_0091B9D9;
loc_0091BA3F:
    if (v_stack_m5D8 == (*(uint64_t *)(v_rip + 0x6AB12A))) goto loc_0091B63A;
    goto loc_0091B1AB;
loc_0091BA54:
    if (((uint32_t)((uint32_t)(0xFFFFFFFEULL))) != (*(uint32_t *)(v_stack_m5E0))) goto loc_0091B63A;
    goto loc_0091B1CD;
loc_0091BA61:
    v_stack_m608 = 0xC0000004ULL;
    if (v_stack_m5F0 == 0) goto loc_0091BB54;
    goto loc_0091B5B2;
loc_0091BA7C:
    v_stack_m608 = (uint32_t)(v_stack_m5F0);
    goto loc_0091BB54;
loc_0091BA85:
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)((uint32_t)(v_stack_m5BC))));
    v_stack_m604 = (uint32_t)(local_r14);
    goto loc_0091AAD7;
loc_0091BA9A:
    v_stack_m578 = 0;
    v_stack_m588 = 0;
    goto loc_0091B7AD;
loc_0091BAAF:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) - ((uint32_t)((uint32_t)(Arg5))));
    *(uint32_t *)((uint32_t)(Arg5) + 0x38) = (uint32_t)(result);
    result = memcpy(local_r15, v_stack_m148, (uint32_t)(v_stack_m578), v_stack_m1D8);
    goto loc_0091BB0C;
loc_0091BB0C:
    if (sign_flag) goto loc_0091B319;
    local_r15 = (local_r15) + ((uint32_t)(v_stack_m578));
    v_stack_m5E0 = local_r15;
    goto loc_0091B847;
loc_0091BB28:
    goto loc_0091B0B4;
loc_0091BB34:
    if (v_stack_m590 != 0) goto loc_0091B66F;
    if (((uint32_t)((uint32_t)(Arg5))) == 252) goto loc_0091B6B1;
    goto loc_0091B665;
loc_0091BB54:
    if (v_stack_m5D8 != 0) goto loc_0091BC54;
loc_0091BB5D:
    if (v_stack_m5B0 != 0) goto loc_0091BC73;
loc_0091BB6E:
loc_0091BB72:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m148, v_stack_m5B0, v_stack_m1D8);
    local_rsp = (local_rsp) + (0x600ULL);
    return result;
loc_0091BB96:
    v_stack_pA8 = 0;
    if (((uint32_t)((uint32_t)(Arg5))) == 253) goto loc_0091BBDF;
    v_stack_p80 = 624;
    v_stack_p90 = v_stack_pD8;
    result = 136;
    if (((uint32_t)((uint32_t)(Arg5))) == 5) { result = (uint32_t)(136 - 56); }
    v_stack_p7C = (uint32_t)(result);
    goto loc_0091A9A6;
loc_0091BBDF:
    v_stack_p3C = 0;
    v_stack_p80 = 12;
    v_stack_p34 = 12;
    v_stack_p7C = 0;
    v_stack_pE8 = v_stack_pD8;
    v_stack_p90 = 0;
    goto loc_0091A9AE;
loc_0091BC15:
    goto loc_0091BB72;
loc_0091BC28:
    result = ExCheckFullProcessInformationAccess((uint8_t)((uint32_t)(0xC0000095ULL)), v_stack_m148, v_stack_m5B0, v_stack_m1D8);
    if (sign_flag) goto loc_0091BB72;
    goto loc_0091A9EE;
loc_0091BC3D:
    if (v_stack_p648 == 0) goto loc_0091AA27;
    result = KeFlushProcessWriteBuffers((uint8_t)((uint32_t)(0xC0000095ULL)), v_stack_m148, v_stack_m5B0, v_stack_m1D8);
    goto loc_0091AA27;
loc_0091BC54:
    if (v_stack_m5D8 == (*(uint64_t *)(v_rip + 0x6AAF15))) goto loc_0091BB5D;
    result = ObfDereferenceObjectWithTag(v_stack_m5D8, (uint32_t)(0x6E457350ULL), v_stack_m5B0, v_stack_m1D8);
    goto loc_0091BB5D;
loc_0091BC73:
    if ((*(uint64_t *)(v_stack_m5B0 + 0x220)) == (*(uint64_t *)(v_rip + 0x6AAEF6))) goto loc_0091BB6E;
    result = ObfDereferenceObjectWithTag(v_stack_m5B0, (uint32_t)(0x6E457350ULL), v_stack_m5B0, v_stack_m1D8);
    goto loc_0091BB6E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0091A878&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
