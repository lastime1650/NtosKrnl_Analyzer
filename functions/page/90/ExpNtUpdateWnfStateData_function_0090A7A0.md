# ExpNtUpdateWnfStateData

- RVA: `0x0090A7A0`–`0x0090B26E` (길이 `2,766` bytes)
- VA: `0x000000014090A7A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000890C0`
- 디코드: `613`개 명령, `2,766/2,766` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0090A968` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x0090A9AE` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x0090AA27` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x0090AA5F` → [PsGetSessionById](../../text/22/PsGetSessionById_function_00225150.md) (function, `0x00225150`)
- `0x0090AB2D` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x0090ABAF` → [ExpWnfResolveScopeInstance](ExpWnfResolveScopeInstance_function_0090B280.md) (function, `0x0090B280`)
- `0x0090ABD4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090ABF5` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0090AC5C` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)
- `0x0090AC7F` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0090AC88` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090ACF7` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x0090AD45` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x0090AD52` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0090ADB3` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x0090AE41` → [ExpWnfWriteStateData](ExpWnfWriteStateData_function_0090B7B0.md) (function, `0x0090B7B0`)
- `0x0090AEA3` → [ExpWnfNotifyNameSubscribers](ExpWnfNotifyNameSubscribers_function_0090C160.md) (function, `0x0090C160`)
- `0x0090AF14` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0090AF30` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0090AF5D` → [ExpWnfCheckCrossScopeAccess](ExpWnfCheckCrossScopeAccess_function_0090CA94.md) (function, `0x0090CA94`)
- `0x0090AF7B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090AFAB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0090B01E` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0090B028` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0090B09D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0090B0C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090B0EE` → [ExpWnfLookupPermanentName](../8B/ExpWnfLookupPermanentName_function_008BD914.md) (function, `0x008BD914`)
- `0x0090B12A` → [ExpWnfValidatePubSubPreconditions](../9E/ExpWnfValidatePubSubPreconditions_function_009E6E00.md) (function, `0x009E6E00`)
- `0x0090B156` → [ExpWnfCreateNameInstance](../8B/ExpWnfCreateNameInstance_function_008BF590.md) (function, `0x008BF590`)
- `0x0090B169` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0090B1A4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090B1C0` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0090B1FB` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x0090B210` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)
- `0x0090B228` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0090B25A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0090B264` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)

### Direct callers
- [ExWnfCrossVmCallback](../7C/ExWnfCrossVmCallback_function_007CF150.md) at `0x007CF196`
- [NtUpdateWnfStateData](NtUpdateWnfStateData_function_0090A760.md) at `0x0090A789`
- [PfSnPowerBoost](../93/PfSnPowerBoost_function_00939C14.md) at `0x00939CC6`
- [PfSnPowerBoost](../93/PfSnPowerBoost_function_00939C14.md) at `0x00939D14`
- [PfSnPowerBoostUpdate](../A9/PfSnPowerBoostUpdate_function_00A952C4.md) at `0x00A95337`

### Static image references
- `0x0090A7B3` → RVA `0x00E0A740` (`.data`; read)
- `0x0090A939` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x0090AB7C` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x0090AD1B` → RVA `0x00B4B070` (`ExpWnfNotificationMapping`; read)
- `0x0090ADA9` → RVA `0x00EFA118` (`.data`; read)
- `0x0090B1F1` → RVA `0x00EFA120` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x0090A9AE` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x0090AA27` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x0090AA5F` → [PsGetSessionById](../../text/22/PsGetSessionById_function_00225150.md) (`PAGE` → `.text`)
  - `0x0090ABD4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090ABF5` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0090AC5C` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
  - `0x0090AC7F` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0090AC88` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090AD45` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x0090ADB3` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x0090AF14` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0090AF30` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0090AF7B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090AFAB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0090B01E` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0090B028` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0090B09D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0090B0C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090B169` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0090B1A4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090B1C0` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0090B1FB` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x0090B210` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
  - `0x0090B228` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0090B25A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0090B264` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0090B21F` → [sub_00B21240](../B2/Unknown_function_00B21240.md) (`tail-transfer`)
  - `0x0090B22E` → [sub_00B21240](../B2/Unknown_function_00B21240.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0090A7A0  40 53                           push rbx
0090A7A2  56                              push rsi
0090A7A3  57                              push rdi
0090A7A4  41 54                           push r12
0090A7A6  41 55                           push r13
0090A7A8  41 56                           push r14
0090A7AA  41 57                           push r15
0090A7AC  48 81 EC 30 01 00 00            sub rsp, 0x130
0090A7B3  48 8B 05 86 FF 4F 00            mov rax, qword ptr [rip + 0x4fff86]
0090A7BA  48 33 C4                        xor rax, rsp
0090A7BD  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
0090A7C5  4D 8B F9                        mov r15, r9
0090A7C8  45 8B D0                        mov r10d, r8d
0090A7CB  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
0090A7D0  4C 8B DA                        mov r11, rdx
0090A7D3  48 89 94 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdx
0090A7DB  4C 8B B4 24 90 01 00 00         mov r14, qword ptr [rsp + 0x190]
0090A7E3  0F 57 C0                        xorps xmm0, xmm0
0090A7E6  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
0090A7EE  45 33 ED                        xor r13d, r13d
0090A7F1  4C 89 AC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r13
0090A7F9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0090A802  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0090A809  90                              nop
0090A80A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0090A813  44 0F B6 A0 32 02 00 00         movzx r12d, byte ptr [rax + 0x232]
0090A81B  44 88 64 24 54                  mov byte ptr [rsp + 0x54], r12b
0090A820  44 88 64 24 55                  mov byte ptr [rsp + 0x55], r12b
0090A825  44 88 64 24 57                  mov byte ptr [rsp + 0x57], r12b
0090A82A  4C 89 AC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r13
0090A832  4C 89 AC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r13
0090A83A  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
0090A83F  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
0090A844  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
0090A84C  4C 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r9
0090A854  4C 89 AC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r13
0090A85C  48 BE 00 00 FF FF FF 7F 00 00   movabs rsi, 0x7fffffff0000
0090A866  45 84 E4                        test r12b, r12b
0090A869  0F 85 27 01 00 00               jne 0x14090a996
0090A86F  48 8B 19                        mov rbx, qword ptr [rcx]
0090A872  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
0090A87A  48 B8 74 00 BC A3 6D 4E C6 41   movabs rax, 0x41c64e6da3bc0074
0090A884  48 33 D8                        xor rbx, rax
0090A887  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
0090A88C  0F B6 C3                        movzx eax, bl
0090A88F  24 0F                           and al, 0xf
0090A891  3C 01                           cmp al, 1
0090A893  0F 85 8A 00 00 00               jne 0x14090a923
0090A899  48 8B FB                        mov rdi, rbx
0090A89C  48 C1 EF 06                     shr rdi, 6
0090A8A0  44 8B C7                        mov r8d, edi
0090A8A3  41 83 E0 0F                     and r8d, 0xf
0090A8A7  48 8B CB                        mov rcx, rbx
0090A8AA  48 C1 E9 04                     shr rcx, 4
0090A8AE  44 8B C9                        mov r9d, ecx
0090A8B1  41 83 E1 03                     and r9d, 3
0090A8B5  48 8B D3                        mov rdx, rbx
0090A8B8  48 C1 EA 0A                     shr rdx, 0xa
0090A8BC  83 E2 01                        and edx, 1
0090A8BF  41 83 F9 03                     cmp r9d, 3
0090A8C3  75 4D                           jne 0x14090a912
0090A8C5  41 83 F8 05                     cmp r8d, 5
0090A8C9  0F 85 E8 01 00 00               jne 0x14090aab7
0090A8CF  85 D2                           test edx, edx
0090A8D1  0F 85 F6 00 00 00               jne 0x14090a9cd
0090A8D7  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
0090A8DC  83 E1 03                        and ecx, 3
0090A8DF  89 8C 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ecx
0090A8E6  83 E7 0F                        and edi, 0xf
0090A8E9  89 7C 24 64                     mov dword ptr [rsp + 0x64], edi
0090A8ED  45 84 E4                        test r12b, r12b
0090A8F0  0F 85 F3 00 00 00               jne 0x14090a9e9
0090A8F6  44 89 6C 24 5C                  mov dword ptr [rsp + 0x5c], r13d
0090A8FB  4D 85 F6                        test r14, r14
0090A8FE  75 30                           jne 0x14090a930
0090A900  4C 89 AC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r13
0090A908  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
0090A90D  E9 39 02 00 00                  jmp 0x14090ab4b
0090A912  45 85 C9                        test r9d, r9d
0090A915  74 AE                           je 0x14090a8c5
0090A917  41 83 E9 01                     sub r9d, 1
0090A91B  74 A8                           je 0x14090a8c5
0090A91D  41 83 F9 01                     cmp r9d, 1
0090A921  74 A2                           je 0x14090a8c5
0090A923  C7 44 24 50 0D 00 00 C0         mov dword ptr [rsp + 0x50], 0xc000000d
0090A92B  E9 7D 05 00 00                  jmp 0x14090aead
0090A930  83 FF 03                        cmp edi, 3
0090A933  0F 85 08 01 00 00               jne 0x14090aa41
0090A939  4C 8B 05 58 C1 6B 00            mov r8, qword ptr [rip + 0x6bc158]
0090A940  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0090A945  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
0090A94A  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
0090A952  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0090A957  C7 44 24 20 57 6E 66 20         mov dword ptr [rsp + 0x20], 0x20666e57
0090A95F  45 0F B6 CC                     movzx r9d, r12b
0090A963  33 D2                           xor edx, edx
0090A965  49 8B CE                        mov rcx, r14
0090A968  E8 E3 EC F5 FF                  call 0x140869650
0090A96D  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
0090A971  85 C0                           test eax, eax
0090A973  78 10                           js 0x14090a985
0090A975  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
0090A97D  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
0090A985  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090A989  85 C0                           test eax, eax
0090A98B  0F 89 BA 01 00 00               jns 0x14090ab4b
0090A991  E9 17 05 00 00                  jmp 0x14090aead
0090A996  48 8B D6                        mov rdx, rsi
0090A999  48 3B CE                        cmp rcx, rsi
0090A99C  48 0F 42 D1                     cmovb rdx, rcx
0090A9A0  41 B8 08 00 00 00               mov r8d, 8
0090A9A6  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
0090A9AE  E8 1D 20 DB FF                  call 0x1406bc9d0
0090A9B3  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
0090A9BB  44 8B 54 24 60                  mov r10d, dword ptr [rsp + 0x60]
0090A9C0  4C 8B 9C 24 D0 00 00 00         mov r11, qword ptr [rsp + 0xd0]
0090A9C8  E9 AD FE FF FF                  jmp 0x14090a87a
0090A9CD  41 F7 C0 F9 FF FF FF            test r8d, 0xfffffff9
0090A9D4  0F 85 49 FF FF FF               jne 0x14090a923
0090A9DA  41 83 F8 06                     cmp r8d, 6
0090A9DE  0F 85 F3 FE FF FF               jne 0x14090a8d7
0090A9E4  E9 3A FF FF FF                  jmp 0x14090a923
0090A9E9  45 85 D2                        test r10d, r10d
0090A9EC  74 18                           je 0x14090aa06
0090A9EE  41 8B CA                        mov ecx, r10d
0090A9F1  49 03 CB                        add rcx, r11
0090A9F4  48 3B CE                        cmp rcx, rsi
0090A9F7  0F 87 F3 00 00 00               ja 0x14090aaf0
0090A9FD  49 3B CB                        cmp rcx, r11
0090AA00  0F 82 EA 00 00 00               jb 0x14090aaf0
0090AA06  4D 85 FF                        test r15, r15
0090AA09  0F 84 E7 FE FF FF               je 0x14090a8f6
0090AA0F  48 8B D6                        mov rdx, rsi
0090AA12  4C 3B FE                        cmp r15, rsi
0090AA15  49 0F 42 D7                     cmovb rdx, r15
0090AA19  41 B8 10 00 00 00               mov r8d, 0x10
0090AA1F  48 8D 8C 24 18 01 00 00         lea rcx, [rsp + 0x118]
0090AA27  E8 A4 1F DB FF                  call 0x1406bc9d0
0090AA2C  48 8D 84 24 18 01 00 00         lea rax, [rsp + 0x118]
0090AA34  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
0090AA3C  E9 B5 FE FF FF                  jmp 0x14090a8f6
0090AA41  8B CF                           mov ecx, edi
0090AA43  85 FF                           test edi, edi
0090AA45  74 46                           je 0x14090aa8d
0090AA47  83 E9 01                        sub ecx, 1
0090AA4A  0F 85 B1 00 00 00               jne 0x14090ab01
0090AA50  45 84 E4                        test r12b, r12b
0090AA53  75 46                           jne 0x14090aa9b
0090AA55  41 8B 0E                        mov ecx, dword ptr [r14]
0090AA58  89 8C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ecx
0090AA5F  E8 EC A6 91 FF                  call 0x140225150
0090AA64  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0090AA6C  48 85 C0                        test rax, rax
0090AA6F  74 1C                           je 0x14090aa8d
0090AA71  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
0090AA79  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0090AA81  41 8B C5                        mov eax, r13d
0090AA84  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
0090AA88  E9 F8 FE FF FF                  jmp 0x14090a985
0090AA8D  B8 0D 00 00 C0                  mov eax, 0xc000000d
0090AA92  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
0090AA96  E9 EA FE FF FF                  jmp 0x14090a985
0090AA9B  4C 3B F6                        cmp r14, rsi
0090AA9E  49 0F 42 F6                     cmovb rsi, r14
0090AAA2  90                              nop
0090AAA3  8B 0E                           mov ecx, dword ptr [rsi]
0090AAA5  89 8C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ecx
0090AAAC  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0090AAB1  8B 7C 24 64                     mov edi, dword ptr [rsp + 0x64]
0090AAB5  EB A8                           jmp 0x14090aa5f
0090AAB7  45 8B C8                        mov r9d, r8d
0090AABA  45 85 C0                        test r8d, r8d
0090AABD  0F 84 0C FE FF FF               je 0x14090a8cf
0090AAC3  41 83 E9 01                     sub r9d, 1
0090AAC7  0F 84 02 FE FF FF               je 0x14090a8cf
0090AACD  41 83 E9 01                     sub r9d, 1
0090AAD1  0F 84 F8 FD FF FF               je 0x14090a8cf
0090AAD7  41 83 E9 01                     sub r9d, 1
0090AADB  0F 84 EE FD FF FF               je 0x14090a8cf
0090AAE1  41 83 F9 01                     cmp r9d, 1
0090AAE5  0F 85 38 FE FF FF               jne 0x14090a923
0090AAEB  E9 DF FD FF FF                  jmp 0x14090a8cf
0090AAF0  0F B6 06                        movzx eax, byte ptr [rsi]
0090AAF3  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0090AAF8  8B 7C 24 64                     mov edi, dword ptr [rsp + 0x64]
0090AAFC  E9 05 FF FF FF                  jmp 0x14090aa06
0090AB01  83 E9 01                        sub ecx, 1
0090AB04  74 0E                           je 0x14090ab14
0090AB06  B8 0D 00 00 C0                  mov eax, 0xc000000d
0090AB0B  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
0090AB0F  E9 71 FE FF FF                  jmp 0x14090a985
0090AB14  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
0090AB1C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0090AB21  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0090AB26  41 0F B6 D4                     movzx edx, r12b
0090AB2A  49 8B CE                        mov rcx, r14
0090AB2D  E8 A2 CB 01 00                  call 0x1409276d4
0090AB32  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
0090AB36  85 C0                           test eax, eax
0090AB38  0F 88 47 FE FF FF               js 0x14090a985
0090AB3E  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0090AB46  E9 32 FE FF FF                  jmp 0x14090a97d
0090AB4B  EB 0F                           jmp 0x14090ab5c
0090AB4D  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090AB51  44 0F B6 64 24 55               movzx r12d, byte ptr [rsp + 0x55]
0090AB57  E9 51 03 00 00                  jmp 0x14090aead
0090AB5C  45 84 E4                        test r12b, r12b
0090AB5F  0F 85 E4 03 00 00               jne 0x14090af49
0090AB65  C7 84 24 80 00 00 00 01 00 00 00  mov dword ptr [rsp + 0x80], 1
0090AB70  45 84 E4                        test r12b, r12b
0090AB73  0F 85 65 04 00 00               jne 0x14090afde
0090AB79  49 8B F5                        mov rsi, r13
0090AB7C  4C 8B 35 2D BF 6B 00            mov r14, qword ptr [rip + 0x6bbf2d]
0090AB83  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
0090AB88  83 FF 05                        cmp edi, 5
0090AB8B  0F 84 E7 01 00 00               je 0x14090ad78
0090AB91  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0090AB99  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0090AB9E  44 8B CF                        mov r9d, edi
0090ABA1  4C 8B C6                        mov r8, rsi
0090ABA4  49 8B D6                        mov rdx, r14
0090ABA7  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
0090ABAF  E8 CC 06 00 00                  call 0x14090b280
0090ABB4  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090ABB8  85 C0                           test eax, eax
0090ABBA  0F 88 ED 02 00 00               js 0x14090aead
0090ABC0  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0090ABC8  48 83 C3 30                     add rbx, 0x30
0090ABCC  45 33 C0                        xor r8d, r8d
0090ABCF  33 D2                           xor edx, edx
0090ABD1  48 8B CB                        mov rcx, rbx
0090ABD4  E8 57 56 90 FF                  call 0x140210230
0090ABD9  48 8B F8                        mov rdi, rax
0090ABDC  BE 11 00 00 00                  mov esi, 0x11
0090ABE1  33 C0                           xor eax, eax
0090ABE3  F0 48 0F B1 33                  lock cmpxchg qword ptr [rbx], rsi
0090ABE8  74 10                           je 0x14090abfa
0090ABEA  4C 8B CB                        mov r9, rbx
0090ABED  4C 8B C7                        mov r8, rdi
0090ABF0  33 D2                           xor edx, edx
0090ABF2  48 8B CB                        mov rcx, rbx
0090ABF5  E8 52 58 90 FF                  call 0x14021044c
0090ABFA  48 85 FF                        test rdi, rdi
0090ABFD  74 04                           je 0x14090ac03
0090ABFF  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0090AC03  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0090AC0B  48 8B 50 38                     mov rdx, qword ptr [rax + 0x38]
0090AC0F  48 85 D2                        test rdx, rdx
0090AC12  74 51                           je 0x14090ac65
0090AC14  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0090AC19  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0090AC20  48 3B 42 18                     cmp rax, qword ptr [rdx + 0x18]
0090AC24  0F 82 46 01 00 00               jb 0x14090ad70
0090AC2A  76 09                           jbe 0x14090ac35
0090AC2C  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
0090AC30  48 85 D2                        test rdx, rdx
0090AC33  75 EB                           jne 0x14090ac20
0090AC35  48 85 D2                        test rdx, rdx
0090AC38  74 2B                           je 0x14090ac65
0090AC3A  48 8D 5A F0                     lea rbx, [rdx - 0x10]
0090AC3E  48 85 DB                        test rbx, rbx
0090AC41  74 25                           je 0x14090ac68
0090AC43  48 8D 4B 08                     lea rcx, [rbx + 8]
0090AC47  0F 0D 09                        prefetchw byte ptr [rcx]
0090AC4A  48 8B 01                        mov rax, qword ptr [rcx]
0090AC4D  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090AC51  48 8D 50 02                     lea rdx, [rax + 2]
0090AC55  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0090AC5A  74 0C                           je 0x14090ac68
0090AC5C  E8 EF 13 A4 FF                  call 0x14034c050
0090AC61  84 C0                           test al, al
0090AC63  75 03                           jne 0x14090ac68
0090AC65  49 8B DD                        mov rbx, r13
0090AC68  48 8B BC 24 90 00 00 00         mov rdi, qword ptr [rsp + 0x90]
0090AC70  48 8B C6                        mov rax, rsi
0090AC73  F0 4C 0F B1 6F 30               lock cmpxchg qword ptr [rdi + 0x30], r13
0090AC79  74 09                           je 0x14090ac84
0090AC7B  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0090AC7F  E8 BC 87 95 FF                  call 0x140263440
0090AC84  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0090AC88  E8 73 69 9D FF                  call 0x1402e1600
0090AC8D  48 85 DB                        test rbx, rbx
0090AC90  0F 84 3E 03 00 00               je 0x14090afd4
0090AC96  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0090AC9B  41 8B C5                        mov eax, r13d
0090AC9E  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090ACA2  3D 34 00 00 C0                  cmp eax, 0xc0000034
0090ACA7  0F 84 23 04 00 00               je 0x14090b0d0
0090ACAD  85 C0                           test eax, eax
0090ACAF  0F 88 F8 01 00 00               js 0x14090aead
0090ACB5  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0090ACBA  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
0090ACC2  0F 85 24 01 00 00               jne 0x14090adec
0090ACC8  48 8B 5F 48                     mov rbx, qword ptr [rdi + 0x48]
0090ACCC  0F 57 C0                        xorps xmm0, xmm0
0090ACCF  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
0090ACD7  0F 11 84 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm0
0090ACDF  44 89 AC 24 BC 00 00 00         mov dword ptr [rsp + 0xbc], r13d
0090ACE7  44 89 AC 24 98 00 00 00         mov dword ptr [rsp + 0x98], r13d
0090ACEF  48 8D 8C 24 E8 00 00 00         lea rcx, [rsp + 0xe8]
0090ACF7  E8 24 0B F6 FF                  call 0x14086b820
0090ACFC  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
0090AD04  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0090AD09  48 8D 84 24 BC 00 00 00         lea rax, [rsp + 0xbc]
0090AD11  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0090AD16  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
0090AD1B  48 8D 05 4E 03 24 00            lea rax, [rip + 0x24034e]
0090AD22  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0090AD27  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0090AD2C  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
0090AD31  41 B9 02 00 00 00               mov r9d, 2
0090AD37  45 33 C0                        xor r8d, r8d
0090AD3A  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
0090AD42  48 8B CB                        mov rcx, rbx
0090AD45  E8 76 BE A9 FF                  call 0x1403a6bc0
0090AD4A  48 8D 8C 24 E8 00 00 00         lea rcx, [rsp + 0xe8]
0090AD52  E8 B9 09 F6 FF                  call 0x14086b710
0090AD57  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
0090AD5E  85 C0                           test eax, eax
0090AD60  0F 89 86 00 00 00               jns 0x14090adec
0090AD66  44 8B 7C 24 60                  mov r15d, dword ptr [rsp + 0x60]
0090AD6B  E9 9D 00 00 00                  jmp 0x14090ae0d
0090AD70  48 8B 12                        mov rdx, qword ptr [rdx]
0090AD73  E9 B8 FE FF FF                  jmp 0x14090ac30
0090AD78  83 BC 24 A8 01 00 00 00         cmp dword ptr [rsp + 0x1a8], 0
0090AD80  0F 84 0B FE FF FF               je 0x14090ab91
0090AD86  83 BC 24 A0 01 00 00 00         cmp dword ptr [rsp + 0x1a0], 0
0090AD8E  0F 85 CE 02 00 00               jne 0x14090b062
0090AD94  48 B8 74 00 BC A3 6D 4E C6 41   movabs rax, 0x41c64e6da3bc0074
0090AD9E  48 33 D8                        xor rbx, rax
0090ADA1  48 89 9C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rbx
0090ADA9  4C 8B 3D 68 F3 5E 00            mov r15, qword ptr [rip + 0x5ef368]
0090ADB0  49 8B CF                        mov rcx, r15
0090ADB3  E8 5C DA B1 FF                  call 0x140428814
0090ADB8  4C 8B F0                        mov r14, rax
0090ADBB  48 85 C0                        test rax, rax
0090ADBE  0F 85 AB 02 00 00               jne 0x14090b06f
0090ADC4  BB 02 00 00 C0                  mov ebx, 0xc0000002
0090ADC9  4D 85 F6                        test r14, r14
0090ADCC  0F 85 8F 04 00 00               jne 0x14090b261
0090ADD2  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
0090ADD6  81 FB 02 00 00 C0               cmp ebx, 0xc0000002
0090ADDC  0F 85 CB 00 00 00               jne 0x14090aead
0090ADE2  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
0090ADE7  E9 A5 FD FF FF                  jmp 0x14090ab91
0090ADEC  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
0090ADF0  48 85 C9                        test rcx, rcx
0090ADF3  0F 85 C4 01 00 00               jne 0x14090afbd
0090ADF9  44 8B 7C 24 60                  mov r15d, dword ptr [rsp + 0x60]
0090ADFE  44 3B 7F 38                     cmp r15d, dword ptr [rdi + 0x38]
0090AE02  0F 86 AD 01 00 00               jbe 0x14090afb5
0090AE08  B8 0D 00 00 C0                  mov eax, 0xc000000d
0090AE0D  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090AE11  85 C0                           test eax, eax
0090AE13  0F 88 94 00 00 00               js 0x14090aead
0090AE19  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0090AE1E  8B 84 24 A0 01 00 00            mov eax, dword ptr [rsp + 0x1a0]
0090AE25  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0090AE29  44 8B 8C 24 98 01 00 00         mov r9d, dword ptr [rsp + 0x198]
0090AE31  45 8B C7                        mov r8d, r15d
0090AE34  48 8B 94 24 D0 00 00 00         mov rdx, qword ptr [rsp + 0xd0]
0090AE3C  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0090AE41  E8 6A 09 00 00                  call 0x14090b7b0
0090AE46  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090AE4A  48 B9 74 00 BC A3 6D 4E C6 41   movabs rcx, 0x41c64e6da3bc0074
0090AE54  EB 25                           jmp 0x14090ae7b
0090AE56  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090AE5A  45 33 ED                        xor r13d, r13d
0090AE5D  48 B9 74 00 BC A3 6D 4E C6 41   movabs rcx, 0x41c64e6da3bc0074
0090AE67  41 8D 75 11                     lea esi, [r13 + 0x11]
0090AE6B  44 0F B6 64 24 55               movzx r12d, byte ptr [rsp + 0x55]
0090AE71  44 88 64 24 54                  mov byte ptr [rsp + 0x54], r12b
0090AE76  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0090AE7B  85 C0                           test eax, eax
0090AE7D  78 2E                           js 0x14090aead
0090AE7F  83 7C 24 64 05                  cmp dword ptr [rsp + 0x64], 5
0090AE84  0F 84 FE 02 00 00               je 0x14090b188
0090AE8A  45 8B CD                        mov r9d, r13d
0090AE8D  80 7C 24 57 00                  cmp byte ptr [rsp + 0x57], 0
0090AE92  41 0F 95 C1                     setne r9b
0090AE96  BA 01 00 00 00                  mov edx, 1
0090AE9B  44 8B C2                        mov r8d, edx
0090AE9E  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0090AEA3  E8 B8 12 00 00                  call 0x14090c160
0090AEA8  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
0090AEAD  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0090AEB2  48 85 C9                        test rcx, rcx
0090AEB5  74 1D                           je 0x14090aed4
0090AEB7  48 83 C1 08                     add rcx, 8
0090AEBB  0F 0D 09                        prefetchw byte ptr [rcx]
0090AEBE  48 8B 01                        mov rax, qword ptr [rcx]
0090AEC1  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090AEC5  48 8D 50 FE                     lea rdx, [rax - 2]
0090AEC9  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0090AECE  0F 85 4A 01 00 00               jne 0x14090b01e
0090AED4  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0090AEDC  48 85 C9                        test rcx, rcx
0090AEDF  74 1D                           je 0x14090aefe
0090AEE1  48 83 C1 08                     add rcx, 8
0090AEE5  0F 0D 09                        prefetchw byte ptr [rcx]
0090AEE8  48 8B 01                        mov rax, qword ptr [rcx]
0090AEEB  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0090AEEF  48 8D 50 FE                     lea rdx, [rax - 2]
0090AEF3  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0090AEF8  0F 85 2A 01 00 00               jne 0x14090b028
0090AEFE  48 8B B4 24 B0 00 00 00         mov rsi, qword ptr [rsp + 0xb0]
0090AF06  48 85 F6                        test rsi, rsi
0090AF09  75 68                           jne 0x14090af73
0090AF0B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0090AF14  E8 D7 40 95 FF                  call 0x14025eff0
0090AF19  8B 4C 24 64                     mov ecx, dword ptr [rsp + 0x64]
0090AF1D  85 C9                           test ecx, ecx
0090AF1F  75 61                           jne 0x14090af82
0090AF21  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0090AF25  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
0090AF2D  48 33 CC                        xor rcx, rsp
0090AF30  E8 0B 17 DA FF                  call 0x1406ac640
0090AF35  48 81 C4 30 01 00 00            add rsp, 0x130
0090AF3C  41 5F                           pop r15
0090AF3E  41 5E                           pop r14
0090AF40  41 5D                           pop r13
0090AF42  41 5C                           pop r12
0090AF44  5F                              pop rdi
0090AF45  5E                              pop rsi
0090AF46  5B                              pop rbx
0090AF47  C3                              ret
0090AF48  CC                              int3
0090AF49  44 89 AC 24 80 00 00 00         mov dword ptr [rsp + 0x80], r13d
0090AF51  4D 85 F6                        test r14, r14
0090AF54  0F 84 16 FC FF FF               je 0x14090ab70
0090AF5A  48 8B CB                        mov rcx, rbx
0090AF5D  E8 32 1B 00 00                  call 0x14090ca94
0090AF62  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090AF66  85 C0                           test eax, eax
0090AF68  0F 89 02 FC FF FF               jns 0x14090ab70
0090AF6E  E9 3A FF FF FF                  jmp 0x14090aead
0090AF73  BA 57 6E 66 20                  mov edx, 0x20666e57
0090AF78  48 8B CE                        mov rcx, rsi
0090AF7B  E8 F0 78 27 00                  call 0x140b82870
0090AF80  EB 89                           jmp 0x14090af0b
0090AF82  83 E9 01                        sub ecx, 1
0090AF85  74 7F                           je 0x14090b006
0090AF87  83 E9 01                        sub ecx, 1
0090AF8A  0F 84 19 01 00 00               je 0x14090b0a9
0090AF90  83 F9 01                        cmp ecx, 1
0090AF93  75 8C                           jne 0x14090af21
0090AF95  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0090AF9D  48 85 C9                        test rcx, rcx
0090AFA0  0F 84 7B FF FF FF               je 0x14090af21
0090AFA6  BA 57 6E 66 20                  mov edx, 0x20666e57
0090AFAB  E8 30 C9 9E FF                  call 0x1402f78e0
0090AFB0  E9 6C FF FF FF                  jmp 0x14090af21
0090AFB5  41 8B C5                        mov eax, r13d
0090AFB8  E9 50 FE FF FF                  jmp 0x14090ae0d
0090AFBD  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0090AFC5  48 85 D2                        test rdx, rdx
0090AFC8  75 68                           jne 0x14090b032
0090AFCA  B8 0D 00 00 C0                  mov eax, 0xc000000d
0090AFCF  E9 92 FD FF FF                  jmp 0x14090ad66
0090AFD4  B8 34 00 00 C0                  mov eax, 0xc0000034
0090AFD9  E9 C0 FC FF FF                  jmp 0x14090ac9e
0090AFDE  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
0090AFE7  4C 8B B6 B8 00 00 00            mov r14, qword ptr [rsi + 0xb8]
0090AFEE  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
0090AFF3  8B 7C 24 64                     mov edi, dword ptr [rsp + 0x64]
0090AFF7  83 FF 03                        cmp edi, 3
0090AFFA  74 54                           je 0x14090b050
0090AFFC  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0090B001  E9 82 FB FF FF                  jmp 0x14090ab88
0090B006  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0090B00E  48 85 C9                        test rcx, rcx
0090B011  0F 84 0A FF FF FF               je 0x14090af21
0090B017  BA 50 73 51 79                  mov edx, 0x79517350
0090B01C  EB 8D                           jmp 0x14090afab
0090B01E  E8 8D EE A3 FF                  call 0x140349eb0
0090B023  E9 AC FE FF FF                  jmp 0x14090aed4
0090B028  E8 83 EE A3 FF                  call 0x140349eb0
0090B02D  E9 CC FE FF FF                  jmp 0x14090aefe
0090B032  4C 8B 01                        mov r8, qword ptr [rcx]
0090B035  4C 2B 02                        sub r8, qword ptr [rdx]
0090B038  75 08                           jne 0x14090b042
0090B03A  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
0090B03E  4C 2B 42 08                     sub r8, qword ptr [rdx + 8]
0090B042  4D 85 C0                        test r8, r8
0090B045  0F 84 AE FD FF FF               je 0x14090adf9
0090B04B  E9 7A FF FF FF                  jmp 0x14090afca
0090B050  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0090B058  48 85 C0                        test rax, rax
0090B05B  74 05                           je 0x14090b062
0090B05D  4C 3B 30                        cmp r14, qword ptr [rax]
0090B060  75 9A                           jne 0x14090affc
0090B062  C7 44 24 50 0D 00 00 C0         mov dword ptr [rsp + 0x50], 0xc000000d
0090B06A  E9 3E FE FF FF                  jmp 0x14090aead
0090B06F  48 8B 40 70                     mov rax, qword ptr [rax + 0x70]
0090B073  8B 4C 24 60                     mov ecx, dword ptr [rsp + 0x60]
0090B077  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0090B07B  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
0090B083  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0090B088  41 B9 FF FF FF FF               mov r9d, 0xffffffff
0090B08E  4C 8D 84 24 10 01 00 00         lea r8, [rsp + 0x110]
0090B096  BA 01 00 00 00                  mov edx, 1
0090B09B  33 C9                           xor ecx, ecx
0090B09D  E8 2E FA DA FF                  call 0x1406baad0
0090B0A2  8B D8                           mov ebx, eax
0090B0A4  E9 20 FD FF FF                  jmp 0x14090adc9
0090B0A9  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0090B0B1  48 85 C9                        test rcx, rcx
0090B0B4  0F 84 67 FE FF FF               je 0x14090af21
0090B0BA  41 80 FC 01                     cmp r12b, 1
0090B0BE  0F 85 5D FE FF FF               jne 0x14090af21
0090B0C4  33 D2                           xor edx, edx
0090B0C6  E8 A5 77 27 00                  call 0x140b82870
0090B0CB  E9 51 FE FF FF                  jmp 0x14090af21
0090B0D0  83 BC 24 B8 00 00 00 03         cmp dword ptr [rsp + 0xb8], 3
0090B0D8  0F 84 CF FB FF FF               je 0x14090acad
0090B0DE  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
0090B0E6  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0090B0EB  48 8B CB                        mov rcx, rbx
0090B0EE  E8 21 28 FB FF                  call 0x1408bd914
0090B0F3  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090B0F7  85 C0                           test eax, eax
0090B0F9  0F 88 AE FD FF FF               js 0x14090aead
0090B0FF  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
0090B106  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0090B10A  4C 8B 8C 24 C8 00 00 00         mov r9, qword ptr [rsp + 0xc8]
0090B112  44 8B 7C 24 60                  mov r15d, dword ptr [rsp + 0x60]
0090B117  45 8B C7                        mov r8d, r15d
0090B11A  48 8B B4 24 B0 00 00 00         mov rsi, qword ptr [rsp + 0xb0]
0090B122  48 8B D6                        mov rdx, rsi
0090B125  B9 02 00 00 00                  mov ecx, 2
0090B12A  E8 D1 BC 0D 00                  call 0x1409e6e00
0090B12F  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090B133  85 C0                           test eax, eax
0090B135  0F 88 72 FD FF FF               js 0x14090aead
0090B13B  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0090B140  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0090B145  4D 8B CE                        mov r9, r14
0090B148  4C 8B C6                        mov r8, rsi
0090B14B  48 8B D3                        mov rdx, rbx
0090B14E  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0090B156  E8 35 44 FB FF                  call 0x1408bf590
0090B15B  8B F8                           mov edi, eax
0090B15D  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0090B161  BA 57 6E 66 20                  mov edx, 0x20666e57
0090B166  48 8B CE                        mov rcx, rsi
0090B169  E8 02 77 27 00                  call 0x140b82870
0090B16E  4C 89 AC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r13
0090B176  85 FF                           test edi, edi
0090B178  0F 88 2F FD FF FF               js 0x14090aead
0090B17E  BE 11 00 00 00                  mov esi, 0x11
0090B183  E9 96 FC FF FF                  jmp 0x14090ae1e
0090B188  48 33 D9                        xor rbx, rcx
0090B18B  48 89 9C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rbx
0090B193  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0090B198  48 83 C3 50                     add rbx, 0x50
0090B19C  45 33 C0                        xor r8d, r8d
0090B19F  33 D2                           xor edx, edx
0090B1A1  48 8B CB                        mov rcx, rbx
0090B1A4  E8 87 50 90 FF                  call 0x140210230
0090B1A9  48 8B F8                        mov rdi, rax
0090B1AC  33 C0                           xor eax, eax
0090B1AE  F0 48 0F B1 33                  lock cmpxchg qword ptr [rbx], rsi
0090B1B3  74 10                           je 0x14090b1c5
0090B1B5  4C 8B CB                        mov r9, rbx
0090B1B8  4C 8B C7                        mov r8, rdi
0090B1BB  33 D2                           xor edx, edx
0090B1BD  48 8B CB                        mov rcx, rbx
0090B1C0  E8 87 52 90 FF                  call 0x14021044c
0090B1C5  48 85 FF                        test rdi, rdi
0090B1C8  74 04                           je 0x14090b1ce
0090B1CA  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0090B1CE  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0090B1D3  48 8B 42 58                     mov rax, qword ptr [rdx + 0x58]
0090B1D7  49 8B CD                        mov rcx, r13
0090B1DA  48 83 F8 01                     cmp rax, 1
0090B1DE  48 0F 45 C8                     cmovne rcx, rax
0090B1E2  48 85 C9                        test rcx, rcx
0090B1E5  75 4C                           jne 0x14090b233
0090B1E7  49 8B F5                        mov rsi, r13
0090B1EA  45 8B F5                        mov r14d, r13d
0090B1ED  44 8B 62 60                     mov r12d, dword ptr [rdx + 0x60]
0090B1F1  4C 8B 3D 28 EF 5E 00            mov r15, qword ptr [rip + 0x5eef28]
0090B1F8  49 8B CF                        mov rcx, r15
0090B1FB  E8 14 D6 B1 FF                  call 0x140428814
0090B200  48 8B F8                        mov rdi, rax
0090B203  48 85 C0                        test rax, rax
0090B206  75 35                           jne 0x14090b23d
0090B208  48 85 FF                        test rdi, rdi
0090B20B  74 08                           je 0x14090b215
0090B20D  49 8B CF                        mov rcx, r15
0090B210  E8 AB BB B4 FF                  call 0x140456dc0
0090B215  B8 11 00 00 00                  mov eax, 0x11
0090B21A  F0 4C 0F B1 2B                  lock cmpxchg qword ptr [rbx], r13
0090B21F  0F 84 1B 60 21 00               je 0x140b21240
0090B225  48 8B CB                        mov rcx, rbx
0090B228  E8 13 82 95 FF                  call 0x140263440
0090B22D  90                              nop
0090B22E  E9 0D 60 21 00                  jmp 0x140b21240
0090B233  48 8D 71 10                     lea rsi, [rcx + 0x10]
0090B237  44 8B 71 08                     mov r14d, dword ptr [rcx + 8]
0090B23B  EB B0                           jmp 0x14090b1ed
0090B23D  48 8B 40 70                     mov rax, qword ptr [rax + 0x70]
0090B241  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0090B246  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0090B24B  45 8B CC                        mov r9d, r12d
0090B24E  4C 8D 84 24 08 01 00 00         lea r8, [rsp + 0x108]
0090B256  33 D2                           xor edx, edx
0090B258  33 C9                           xor ecx, ecx
0090B25A  E8 71 F8 DA FF                  call 0x1406baad0
0090B25F  EB A7                           jmp 0x14090b208
0090B261  49 8B CF                        mov rcx, r15
0090B264  E8 57 BB B4 FF                  call 0x140456dc0
0090B269  E9 64 FB FF FF                  jmp 0x14090add2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpNtUpdateWnfStateData(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned int a8)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned __int8 v_stack_m111;
    unsigned __int8 v_stack_m113;
    unsigned __int8 v_stack_m114;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p50;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pB0;
    unsigned int v_stack_pB8;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;

    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 5242758)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m108 = a3;
    v_stack_m98 = a2;
    v_stack_m50 = v_xmm0;
    v_r13 = 0;
    v_stack_mE0 = 0;
    v_stack_m114 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m113 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m111 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_mB8 = 0;
    v_stack_mD8 = 0;
    v_stack_mF8 = 0;
    v_stack_m104 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mA0 = a4;
    v_stack_mA8 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0090A996;
    v_stack_mA8 = *(unsigned __int64 *)(a1);
loc_0090A87A:
    v_rbx = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(gs_base + (0 + 392)));
    v_stack_m100 = v_rbx;
    result = (unsigned __int8)(((unsigned __int8)(v_rbx)) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_0090A923;
    v_rdi = (v_rbx) >> (6);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (15));
    a1 = (v_rbx) >> (4);
    a4 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (3));
    a2 = (v_rbx) >> (10);
    a2 = (unsigned int)((a2) & (1));
    if (((unsigned int)(a4)) != 3) goto loc_0090A912;
loc_0090A8C5:
    if (a3 != 5) goto loc_0090AAB7;
loc_0090A8CF:
    if ((unsigned int)(a2) != 0) goto loc_0090A9CD;
loc_0090A8D7:
    v_stack_m118 = 0;
    a1 = (unsigned int)((a1) & (3));
    v_stack_mB0 = (unsigned int)(a1);
    v_rdi = (unsigned int)((v_rdi) & (15));
    v_stack_m104 = (unsigned int)(v_rdi);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0090A9E9;
loc_0090A8F6:
    v_stack_m10C = 0;
    if (a5 != 0) goto loc_0090A930;
    v_stack_mE0 = 0;
    v_stack_m118 = 0;
    goto loc_0090AB4B;
loc_0090A912:
    if ((unsigned int)(a4) == 0) goto loc_0090A8C5;
    a4 = (unsigned int)((a4) - (1));
    if (condition_is_equal) goto loc_0090A8C5;
    if (((unsigned int)(a4)) == 1) goto loc_0090A8C5;
loc_0090A923:
    v_stack_m118 = 0xC000000DULL;
    goto loc_0090AEAD;
loc_0090A930:
    if (((unsigned int)(v_rdi)) != 3) goto loc_0090AA41;
    v_stack_m130 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = v_stack_mC8;
    v_stack_m148 = 0x20666E57ULL;
    a2 = 0;
    result = ObpReferenceObjectByHandleWithTag(a5, a2, *(unsigned __int64 *)(v_rip + 7061848), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m10C = (unsigned int)(result);
    if (sign_flag) goto loc_0090A985;
loc_0090A97D:
    v_stack_mE0 = v_stack_mC8;
loc_0090A985:
    v_stack_m118 = (unsigned int)(result);
    if (!sign_flag) goto loc_0090AB4B;
    goto loc_0090AEAD;
loc_0090A996:
    a2 = v_rsi;
    if (v_stack_mC8 < v_rsi) { a2 = v_stack_mC8; }
    result = RtlCopyVolatileMemory(v_stack_mA8, a2, 8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_0090A87A;
loc_0090A9CD:
    if (((8) & (0xFFFFFFF9ULL)) != 0) goto loc_0090A923;
    if (8 != 6) goto loc_0090A8D7;
    goto loc_0090A923;
loc_0090A9E9:
    if ((unsigned int)((unsigned int)(v_stack_m108)) == 0) goto loc_0090AA06;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m108)))) + (v_stack_m98);
    if (a1 > v_rsi) goto loc_0090AAF0;
    if (a1 < v_stack_m98) goto loc_0090AAF0;
loc_0090AA06:
    if (a4 == 0) goto loc_0090A8F6;
    a2 = v_rsi;
    if (a4 < v_rsi) { a2 = a4; }
    result = RtlCopyVolatileMemory(v_stack_m50, a2, 16, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_mA0 = v_stack_m50;
    goto loc_0090A8F6;
loc_0090AA41:
    if ((unsigned int)(v_rdi) == 0) goto loc_0090AA8D;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (1));
    if (condition_is_not_equal) goto loc_0090AB01;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0090AA9B;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(a5)));
loc_0090AA5F:
    result = PsGetSessionById((unsigned int)(*(unsigned int *)(a5)), a2, 16, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_mC8 = result;
    if (result == 0) goto loc_0090AA8D;
    v_stack_mE0 = v_stack_mC0;
    v_stack_m10C = 0;
    goto loc_0090A985;
loc_0090AA8D:
    v_stack_m10C = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0090A985;
loc_0090AA9B:
    if (a5 < v_rsi) { v_rsi = a5; }
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    goto loc_0090AA5F;
loc_0090AAB7:
    if (16 == 0) goto loc_0090A8CF;
    a4 = (unsigned int)((16) - (1));
    if (condition_is_equal) goto loc_0090A8CF;
    a4 = (unsigned int)((a4) - (1));
    if (condition_is_equal) goto loc_0090A8CF;
    a4 = (unsigned int)((a4) - (1));
    if (condition_is_equal) goto loc_0090A8CF;
    if (((unsigned int)(a4)) != 1) goto loc_0090A923;
    goto loc_0090A8CF;
loc_0090AAF0:
    goto loc_0090AA06;
loc_0090AB01:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) - (1));
    if (condition_is_equal) goto loc_0090AB14;
    v_stack_m10C = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0090A985;
loc_0090AB14:
    v_stack_m138 = v_stack_mC8;
    v_stack_m140 = 0;
    result = SeCaptureSid(a5, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 16, a4);
    v_stack_m10C = (unsigned int)(result);
    if (sign_flag) goto loc_0090A985;
    goto loc_0090A97D;
loc_0090AB4B:
    goto loc_0090AB5C;
loc_0090AB5C:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0090AF49;
    v_stack_mE8 = 1;
loc_0090AB70:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0090AFDE;
    v_stack_mF0 = *(unsigned __int64 *)(v_rip + 7061293);
loc_0090AB88:
    if (((unsigned int)((unsigned int)(v_stack_m104))) == 5) goto loc_0090AD78;
loc_0090AB91:
    v_stack_m148 = v_stack_mE0;
    result = ExpWnfResolveScopeInstance(v_stack_mD8, *(unsigned __int64 *)(v_rip + 7061293), 0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m104))));
    v_stack_m118 = (unsigned int)(result);
    if (sign_flag) goto loc_0090AEAD;
    v_rbx = (v_stack_mD8) + (48);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbx, a2, a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_m104))));
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rbx;
        a3 = 0;
        a2 = 0;
        a1 = v_rbx;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_stack_mD8 + 56) == 0) goto loc_0090AC65;
loc_0090AC20:
    if (v_stack_m100 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 56) + 24))) goto loc_0090AD70;
    if (v_stack_m100 <= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 56) + 24))) goto loc_0090AC35;
loc_0090AC30:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 56) + 8) != 0) goto loc_0090AC20;
loc_0090AC35:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 56) + 8) == 0) goto loc_0090AC65;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 56) + 8) - 16 == 0) goto loc_0090AC68;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 56) + 8) - 16 + 8)) & (-2);
    if (condition_is_equal) goto loc_0090AC68;
    result = ExfAcquireRundownProtection(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 56) + 8) - 16 + 8, result + 2, a3, a4);
    v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + 56) + 8) - 16;
    if ((unsigned __int8)(result) == 0) {
        v_rbx = 0;
    }
    result = 17;
    if ((unsigned __int8)(result) != 0) {
        a1 = v_stack_mD8 + 48;
        result = ExfReleasePushLockShared(a1, result + 2, a3, a4);
    }
    result = KeAbPostRelease(v_stack_mD8 + 48, result + 2, a3, a4);
    if (v_rbx == 0) goto loc_0090AFD4;
    v_stack_mF8 = v_rbx;
loc_0090AC9E:
    v_stack_m118 = 0;
    if (0 == 0xC0000034ULL) goto loc_0090B0D0;
loc_0090ACAD:
    if (sign_flag) goto loc_0090AEAD;
    if (v_stack_mE8 != 0) goto loc_0090ADEC;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    v_stack_mAC = 0;
    v_stack_mD0 = 0;
    result = SeCaptureSubjectContext(v_stack_m80, result + 2, a3, a4);
    v_stack_m120 = v_stack_mD0;
    v_stack_m128 = v_stack_mAC;
    v_stack_m130 = 1;
    v_stack_m138 = v_rip + 2360142;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    a3 = 0;
    result = SeAccessCheck(*(unsigned __int64 *)(v_stack_mF8 + 72), v_stack_m80, a3, 2);
    result = SeReleaseSubjectContext(v_stack_m80, v_stack_m80, a3, 2);
    if (!sign_flag) goto loc_0090ADEC;
loc_0090AD66:
    goto loc_0090AE0D;
loc_0090AD70:
    goto loc_0090AC30;
loc_0090AD78:
    if (a8 == 0) goto loc_0090AB91;
    if (a7 != 0) goto loc_0090B062;
    v_rbx = (*(unsigned __int64 *)(v_stack_mF8 + 72)) ^ ((unsigned int)(v_stack_mD0));
    v_stack_m58 = v_rbx;
    result = ExGetExtensionTable(*(unsigned __int64 *)(v_rip + 6222696), *(unsigned __int64 *)(v_stack_m80), a3, 2);
    if (result != 0) goto loc_0090B06F;
loc_0090ADC9:
    if (result != 0) goto loc_0090B261;
loc_0090ADD2:
    v_stack_m118 = (unsigned int)((unsigned int)(0xC0000002ULL));
    if (((unsigned int)((unsigned int)(0xC0000002ULL))) != 0xC0000002ULL) goto loc_0090AEAD;
    goto loc_0090AB91;
loc_0090ADEC:
    if (*(unsigned __int64 *)(v_stack_mF8 + 64) != 0) goto loc_0090AFBD;
loc_0090ADF9:
    if (((unsigned int)((unsigned int)(v_stack_m108))) <= (*(unsigned int *)(v_stack_mF8 + 56))) goto loc_0090AFB5;
loc_0090AE0D:
    v_stack_m118 = (unsigned int)((unsigned int)(0xC000000DULL));
    if (sign_flag) goto loc_0090AEAD;
loc_0090AE1E:
    v_stack_m148 = (unsigned int)((unsigned int)(a7));
    result = ExpWnfWriteStateData(v_stack_mF8, v_stack_m98, (unsigned int)((unsigned int)((unsigned int)(v_stack_m108))), (unsigned int)(a6));
    v_stack_m118 = (unsigned int)(result);
    goto loc_0090AE7B;
loc_0090AE7B:
    if (sign_flag) goto loc_0090AEAD;
    if (v_stack_m104 == 5) goto loc_0090B188;
    a4 = (v_stack_m111 != 0) ? 1 : 0;
    result = ExpWnfNotifyNameSubscribers(v_stack_mF8, 1, 1, a4);
    v_stack_m118 = 0;
loc_0090AEAD:
    if (v_stack_mF8 == 0) goto loc_0090AED4;
    a1 = (v_stack_mF8) + (8);
    result = (*(unsigned __int64 *)(a1)) & (-2);
    if (condition_is_not_equal) goto loc_0090B01E;
loc_0090AED4:
    if (v_stack_mD8 == 0) goto loc_0090AEFE;
    a1 = (v_stack_mD8) + (8);
    result = (*(unsigned __int64 *)(a1)) & (-2);
    if (condition_is_not_equal) goto loc_0090B028;
loc_0090AEFE:
    if (v_stack_mB8 != 0) goto loc_0090AF73;
loc_0090AF0B:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), result - 2, 1, a4);
    if ((unsigned int)((unsigned int)(v_stack_m104)) != 0) goto loc_0090AF82;
loc_0090AF21:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, result - 2, 1, a4);
    v_rsp = (v_rsp) + (304);
    return result;
loc_0090AF49:
    v_stack_p80 = 0;
    if (v_stack_mF0 == 0) goto loc_0090AB70;
    result = ExpWnfCheckCrossScopeAccess(v_stack_m100, result - 2, 1, a4);
    v_stack_p50 = (unsigned int)(result);
    if (!sign_flag) goto loc_0090AB70;
    goto loc_0090AEAD;
loc_0090AF73:
    result = ExFreePoolWithTag(v_stack_mB8, (unsigned int)(0x20666E57ULL), 1, a4);
    goto loc_0090AF0B;
loc_0090AF82:
    a1 = (unsigned int)((v_stack_mB8) - (1));
    if (condition_is_equal) goto loc_0090B006;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0090B0A9;
    if (((unsigned int)(a1)) != 1) goto loc_0090AF21;
    if (v_stack_pA0 == 0) goto loc_0090AF21;
loc_0090AFAB:
    result = ObfDereferenceObjectWithTag(v_stack_pA0, (unsigned int)(0x20666E57ULL), 1, a4);
    goto loc_0090AF21;
loc_0090AFB5:
    goto loc_0090AE0D;
loc_0090AFBD:
    if (v_stack_pC8 != 0) goto loc_0090B032;
loc_0090AFCA:
    goto loc_0090AD66;
loc_0090AFD4:
    goto loc_0090AC9E;
loc_0090AFDE:
    v_stack_p78 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    if (((unsigned int)((unsigned int)(v_stack_p64))) == 3) goto loc_0090B050;
loc_0090AFFC:
    goto loc_0090AB88;
loc_0090B006:
    if (v_stack_pA0 == 0) goto loc_0090AF21;
    goto loc_0090AFAB;
loc_0090B01E:
    result = ExfReleaseRundownProtection(v_stack_pA0, (unsigned int)(0x79517350ULL), 1, a4);
    goto loc_0090AED4;
loc_0090B028:
    result = ExfReleaseRundownProtection(v_stack_pA0, (unsigned int)(0x79517350ULL), 1, a4);
    goto loc_0090AEFE;
loc_0090B032:
    a3 = (*(unsigned __int64 *)(v_stack_pA0)) - (*(unsigned __int64 *)((unsigned int)(0x79517350ULL)));
    if (!(condition_is_not_equal)) {
        a3 = *(unsigned __int64 *)(v_stack_pA0 + 8);
        a3 = (a3) - (*(unsigned __int64 *)((unsigned int)(0x79517350ULL) + 8));
    }
    if (a3 == 0) goto loc_0090ADF9;
    goto loc_0090AFCA;
loc_0090B050:
    if (v_stack_p88 == 0) goto loc_0090B062;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != (*(unsigned __int64 *)(v_stack_p88))) goto loc_0090AFFC;
loc_0090B062:
    v_stack_p50 = 0xC000000DULL;
    goto loc_0090AEAD;
loc_0090B06F:
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p60));
    v_stack_p20 = v_stack_pD0;
    a1 = 0;
    result = guard_dispatch_icall(a1, 1, v_stack_p110, (unsigned int)(0xFFFFFFFFULL));
    goto loc_0090ADC9;
loc_0090B0A9:
    if (v_stack_pA0 == 0) goto loc_0090AF21;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != 1) goto loc_0090AF21;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_pA0, a2, v_stack_p110, (unsigned int)(0xFFFFFFFFULL));
    goto loc_0090AF21;
loc_0090B0D0:
    if (v_stack_pB8 == 3) goto loc_0090ACAD;
    result = ExpWnfLookupPermanentName(v_stack_p68, v_stack_pB0, v_stack_p110, (unsigned int)(0xFFFFFFFFULL));
    v_stack_p50 = (unsigned int)(result);
    if (sign_flag) goto loc_0090AEAD;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p80));
    result = ExpWnfValidatePubSubPreconditions(2, v_stack_pB0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p60))), v_stack_pC8);
    v_stack_p50 = (unsigned int)(result);
    if (sign_flag) goto loc_0090AEAD;
    v_stack_p20 = v_stack_p70;
    result = ExpWnfCreateNameInstance(v_stack_p90, v_stack_p68, v_stack_pB0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    v_stack_p50 = (unsigned int)(result);
    result = ExFreePoolWithTag(v_stack_pB0, (unsigned int)(0x20666E57ULL), v_stack_pB0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    v_stack_pB0 = 0;
    if (sign_flag) goto loc_0090AEAD;
    goto loc_0090AE1E;
loc_0090B188:
    v_rbx = (v_stack_p68) ^ (v_stack_pB0);
    v_stack_p108 = v_rbx;
    v_rbx = (v_stack_p70) + (80);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbx, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rbx;
        a3 = 0;
        a2 = 0;
        a1 = v_rbx;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a1 = 0;
    if ((*(unsigned __int64 *)(v_stack_p70 + 88)) != 1) { a1 = *(unsigned __int64 *)(v_stack_p70 + 88); }
    if (a1 != 0) goto loc_0090B233;
loc_0090B1ED:
    result = ExGetExtensionTable(*(unsigned __int64 *)(v_rip + 6221608), v_stack_p70, a3, a4);
    if (result != 0) goto loc_0090B23D;
loc_0090B208:
    if (result != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 6221608);
        result = ExReleaseExtensionTable(a1, v_stack_p70, a3, a4);
    }
    result = ExfReleasePushLockShared(v_rbx, v_stack_p70, a3, a4);
loc_0090B233:
    goto loc_0090B1ED;
loc_0090B23D:
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8)));
    v_stack_p20 = v_rbx + 16;
    a2 = 0;
    a1 = 0;
    result = guard_dispatch_icall(a1, a2, v_stack_p108, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p70 + 96)))));
    goto loc_0090B208;
loc_0090B261:
    result = ExReleaseExtensionTable(*(unsigned __int64 *)(v_rip + 6221608), a2, v_stack_p108, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p70 + 96)))));
    goto loc_0090ADD2;
}
```

## 5. (Beta) C Style

```c
int64_t ExpNtUpdateWnfStateData(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint32_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint8_t v_stack_m111;
    uint8_t v_stack_m113;
    uint8_t v_stack_m114;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p50;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pB0;
    uint32_t v_stack_pB8;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;

    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x4FFF86)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m108 = Arg3;
    v_stack_m98 = Arg2;
    v_stack_m50 = v_xmm0;
    local_r13 = 0;
    v_stack_mE0 = 0;
    v_stack_m114 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m113 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m111 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_mB8 = 0;
    v_stack_mD8 = 0;
    v_stack_mF8 = 0;
    v_stack_m104 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mA0 = Arg4;
    v_stack_mA8 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0090A996;
    v_stack_mA8 = *(uint64_t *)(arg1);
loc_0090A87A:
    local_rbx = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(gs_base + (0 + 0x188)));
    v_stack_m100 = local_rbx;
    result = (uint8_t)(((uint8_t)(local_rbx)) & (15));
    if (((uint8_t)(result)) != 1) goto loc_0090A923;
    local_rdi = (local_rbx) >> (6);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (15));
    Arg1 = (local_rbx) >> (4);
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (3));
    Arg2 = (local_rbx) >> (10);
    Arg2 = (uint32_t)((Arg2) & (1));
    if (((uint32_t)(Arg4)) != 3) goto loc_0090A912;
loc_0090A8C5:
    if (Arg3 != 5) goto loc_0090AAB7;
loc_0090A8CF:
    if ((uint32_t)(Arg2) != 0) goto loc_0090A9CD;
loc_0090A8D7:
    v_stack_m118 = 0;
    Arg1 = (uint32_t)((Arg1) & (3));
    v_stack_mB0 = (uint32_t)(Arg1);
    local_rdi = (uint32_t)((local_rdi) & (15));
    v_stack_m104 = (uint32_t)(local_rdi);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0090A9E9;
loc_0090A8F6:
    v_stack_m10C = 0;
    if (Arg5 != 0) goto loc_0090A930;
    v_stack_mE0 = 0;
    v_stack_m118 = 0;
    goto loc_0090AB4B;
loc_0090A912:
    if ((uint32_t)(Arg4) == 0) goto loc_0090A8C5;
    Arg4 = (uint32_t)((Arg4) - (1));
    if (condition_is_equal) goto loc_0090A8C5;
    if (((uint32_t)(Arg4)) == 1) goto loc_0090A8C5;
loc_0090A923:
    v_stack_m118 = 0xC000000DULL;
    goto loc_0090AEAD;
loc_0090A930:
    if (((uint32_t)(local_rdi)) != 3) goto loc_0090AA41;
    v_stack_m130 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = v_stack_mC8;
    v_stack_m148 = 0x20666E57ULL;
    Arg2 = 0;
    result = ObpReferenceObjectByHandleWithTag(Arg5, Arg2, *(uint64_t *)(v_rip + 0x6BC158), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m10C = (uint32_t)(result);
    if (sign_flag) goto loc_0090A985;
loc_0090A97D:
    v_stack_mE0 = v_stack_mC8;
loc_0090A985:
    v_stack_m118 = (uint32_t)(result);
    if (!sign_flag) goto loc_0090AB4B;
    goto loc_0090AEAD;
loc_0090A996:
    Arg2 = local_rsi;
    if (v_stack_mC8 < local_rsi) { Arg2 = v_stack_mC8; }
    result = RtlCopyVolatileMemory(v_stack_mA8, Arg2, 8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_0090A87A;
loc_0090A9CD:
    if (((8) & (0xFFFFFFF9ULL)) != 0) goto loc_0090A923;
    if (8 != 6) goto loc_0090A8D7;
    goto loc_0090A923;
loc_0090A9E9:
    if ((uint32_t)((uint32_t)(v_stack_m108)) == 0) goto loc_0090AA06;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m108)))) + (v_stack_m98);
    if (Arg1 > local_rsi) goto loc_0090AAF0;
    if (Arg1 < v_stack_m98) goto loc_0090AAF0;
loc_0090AA06:
    if (Arg4 == 0) goto loc_0090A8F6;
    Arg2 = local_rsi;
    if (Arg4 < local_rsi) { Arg2 = Arg4; }
    result = RtlCopyVolatileMemory(v_stack_m50, Arg2, 16, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_mA0 = v_stack_m50;
    goto loc_0090A8F6;
loc_0090AA41:
    if ((uint32_t)(local_rdi) == 0) goto loc_0090AA8D;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (1));
    if (condition_is_not_equal) goto loc_0090AB01;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0090AA9B;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg5)));
loc_0090AA5F:
    result = PsGetSessionById((uint32_t)(*(uint32_t *)(Arg5)), Arg2, 16, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_mC8 = result;
    if (result == 0) goto loc_0090AA8D;
    v_stack_mE0 = v_stack_mC0;
    v_stack_m10C = 0;
    goto loc_0090A985;
loc_0090AA8D:
    v_stack_m10C = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0090A985;
loc_0090AA9B:
    if (Arg5 < local_rsi) { local_rsi = Arg5; }
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    goto loc_0090AA5F;
loc_0090AAB7:
    if (16 == 0) goto loc_0090A8CF;
    Arg4 = (uint32_t)((16) - (1));
    if (condition_is_equal) goto loc_0090A8CF;
    Arg4 = (uint32_t)((Arg4) - (1));
    if (condition_is_equal) goto loc_0090A8CF;
    Arg4 = (uint32_t)((Arg4) - (1));
    if (condition_is_equal) goto loc_0090A8CF;
    if (((uint32_t)(Arg4)) != 1) goto loc_0090A923;
    goto loc_0090A8CF;
loc_0090AAF0:
    goto loc_0090AA06;
loc_0090AB01:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) - (1));
    if (condition_is_equal) goto loc_0090AB14;
    v_stack_m10C = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0090A985;
loc_0090AB14:
    v_stack_m138 = v_stack_mC8;
    v_stack_m140 = 0;
    result = SeCaptureSid(Arg5, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 16, Arg4);
    v_stack_m10C = (uint32_t)(result);
    if (sign_flag) goto loc_0090A985;
    goto loc_0090A97D;
loc_0090AB4B:
    goto loc_0090AB5C;
loc_0090AB5C:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0090AF49;
    v_stack_mE8 = 1;
loc_0090AB70:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0090AFDE;
    v_stack_mF0 = *(uint64_t *)(v_rip + 0x6BBF2D);
loc_0090AB88:
    if (((uint32_t)((uint32_t)(v_stack_m104))) == 5) goto loc_0090AD78;
loc_0090AB91:
    v_stack_m148 = v_stack_mE0;
    result = ExpWnfResolveScopeInstance(v_stack_mD8, *(uint64_t *)(v_rip + 0x6BBF2D), 0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m104))));
    v_stack_m118 = (uint32_t)(result);
    if (sign_flag) goto loc_0090AEAD;
    local_rbx = (v_stack_mD8) + (48);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_m104))));
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rbx;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(v_stack_mD8 + 0x38) == 0) goto loc_0090AC65;
loc_0090AC20:
    if (v_stack_m100 < (*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x38) + 0x18))) goto loc_0090AD70;
    if (v_stack_m100 <= (*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x38) + 0x18))) goto loc_0090AC35;
loc_0090AC30:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x38) + 0x8) != 0) goto loc_0090AC20;
loc_0090AC35:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x38) + 0x8) == 0) goto loc_0090AC65;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x38) + 0x8) - 16 == 0) goto loc_0090AC68;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x38) + 0x8) - 0x10 + 0x8)) & (-2);
    if (condition_is_equal) goto loc_0090AC68;
    result = ExfAcquireRundownProtection(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x38) + 0x8) - 16 + 8, result + 2, Arg3, Arg4);
    local_rbx = *(uint64_t *)(*(uint64_t *)(v_stack_mD8 + 0x38) + 0x8) - 16;
    if ((uint8_t)(result) == 0) {
        local_rbx = 0;
    }
    result = 17;
    if ((uint8_t)(result) != 0) {
        Arg1 = v_stack_mD8 + 48;
        result = ExfReleasePushLockShared(Arg1, result + 2, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_stack_mD8 + 48, result + 2, Arg3, Arg4);
    if (local_rbx == 0) goto loc_0090AFD4;
    v_stack_mF8 = local_rbx;
loc_0090AC9E:
    v_stack_m118 = 0;
    if (0 == 0xC0000034ULL) goto loc_0090B0D0;
loc_0090ACAD:
    if (sign_flag) goto loc_0090AEAD;
    if (v_stack_mE8 != 0) goto loc_0090ADEC;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    v_stack_mAC = 0;
    v_stack_mD0 = 0;
    result = SeCaptureSubjectContext(v_stack_m80, result + 2, Arg3, Arg4);
    v_stack_m120 = v_stack_mD0;
    v_stack_m128 = v_stack_mAC;
    v_stack_m130 = 1;
    v_stack_m138 = v_rip + 2360142;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    Arg3 = 0;
    result = SeAccessCheck(*(uint64_t *)(v_stack_mF8 + 0x48), v_stack_m80, Arg3, 2);
    result = SeReleaseSubjectContext(v_stack_m80, v_stack_m80, Arg3, 2);
    if (!sign_flag) goto loc_0090ADEC;
loc_0090AD66:
    goto loc_0090AE0D;
loc_0090AD70:
    goto loc_0090AC30;
loc_0090AD78:
    if (Arg8 == 0) goto loc_0090AB91;
    if (Arg7 != 0) goto loc_0090B062;
    local_rbx = (*(uint64_t *)(v_stack_mF8 + 0x48)) ^ ((uint32_t)(v_stack_mD0));
    v_stack_m58 = local_rbx;
    result = ExGetExtensionTable(*(uint64_t *)(v_rip + 0x5EF368), *(uint64_t *)(v_stack_m80), Arg3, 2);
    if (result != 0) goto loc_0090B06F;
loc_0090ADC9:
    if (result != 0) goto loc_0090B261;
loc_0090ADD2:
    v_stack_m118 = (uint32_t)((uint32_t)(0xC0000002ULL));
    if (((uint32_t)((uint32_t)(0xC0000002ULL))) != 0xC0000002ULL) goto loc_0090AEAD;
    goto loc_0090AB91;
loc_0090ADEC:
    if (*(uint64_t *)(v_stack_mF8 + 0x40) != 0) goto loc_0090AFBD;
loc_0090ADF9:
    if (((uint32_t)((uint32_t)(v_stack_m108))) <= (*(uint32_t *)(v_stack_mF8 + 0x38))) goto loc_0090AFB5;
loc_0090AE0D:
    v_stack_m118 = (uint32_t)((uint32_t)(0xC000000DULL));
    if (sign_flag) goto loc_0090AEAD;
loc_0090AE1E:
    v_stack_m148 = (uint32_t)((uint32_t)(Arg7));
    result = ExpWnfWriteStateData(v_stack_mF8, v_stack_m98, (uint32_t)((uint32_t)((uint32_t)(v_stack_m108))), (uint32_t)(Arg6));
    v_stack_m118 = (uint32_t)(result);
    goto loc_0090AE7B;
loc_0090AE7B:
    if (sign_flag) goto loc_0090AEAD;
    if (v_stack_m104 == 5) goto loc_0090B188;
    Arg4 = (v_stack_m111 != 0) ? 1 : 0;
    result = ExpWnfNotifyNameSubscribers(v_stack_mF8, 1, 1, Arg4);
    v_stack_m118 = 0;
loc_0090AEAD:
    if (v_stack_mF8 == 0) goto loc_0090AED4;
    Arg1 = (v_stack_mF8) + (8);
    result = (*(uint64_t *)(arg1)) & (-2);
    if (condition_is_not_equal) goto loc_0090B01E;
loc_0090AED4:
    if (v_stack_mD8 == 0) goto loc_0090AEFE;
    Arg1 = (v_stack_mD8) + (8);
    result = (*(uint64_t *)(arg1)) & (-2);
    if (condition_is_not_equal) goto loc_0090B028;
loc_0090AEFE:
    if (v_stack_mB8 != 0) goto loc_0090AF73;
loc_0090AF0B:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), result - 2, 1, Arg4);
    if ((uint32_t)((uint32_t)(v_stack_m104)) != 0) goto loc_0090AF82;
loc_0090AF21:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, result - 2, 1, Arg4);
    local_rsp = (local_rsp) + (304);
    return result;
loc_0090AF49:
    v_stack_p80 = 0;
    if (v_stack_mF0 == 0) goto loc_0090AB70;
    result = ExpWnfCheckCrossScopeAccess(v_stack_m100, result - 2, 1, Arg4);
    v_stack_p50 = (uint32_t)(result);
    if (!sign_flag) goto loc_0090AB70;
    goto loc_0090AEAD;
loc_0090AF73:
    result = ExFreePoolWithTag(v_stack_mB8, (uint32_t)(0x20666E57ULL), 1, Arg4);
    goto loc_0090AF0B;
loc_0090AF82:
    Arg1 = (uint32_t)((v_stack_mB8) - (1));
    if (condition_is_equal) goto loc_0090B006;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0090B0A9;
    if (((uint32_t)(Arg1)) != 1) goto loc_0090AF21;
    if (v_stack_pA0 == 0) goto loc_0090AF21;
loc_0090AFAB:
    result = ObfDereferenceObjectWithTag(v_stack_pA0, (uint32_t)(0x20666E57ULL), 1, Arg4);
    goto loc_0090AF21;
loc_0090AFB5:
    goto loc_0090AE0D;
loc_0090AFBD:
    if (v_stack_pC8 != 0) goto loc_0090B032;
loc_0090AFCA:
    goto loc_0090AD66;
loc_0090AFD4:
    goto loc_0090AC9E;
loc_0090AFDE:
    v_stack_p78 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    if (((uint32_t)((uint32_t)(v_stack_p64))) == 3) goto loc_0090B050;
loc_0090AFFC:
    goto loc_0090AB88;
loc_0090B006:
    if (v_stack_pA0 == 0) goto loc_0090AF21;
    goto loc_0090AFAB;
loc_0090B01E:
    result = ExfReleaseRundownProtection(v_stack_pA0, (uint32_t)(0x79517350ULL), 1, Arg4);
    goto loc_0090AED4;
loc_0090B028:
    result = ExfReleaseRundownProtection(v_stack_pA0, (uint32_t)(0x79517350ULL), 1, Arg4);
    goto loc_0090AEFE;
loc_0090B032:
    Arg3 = (*(uint64_t *)(v_stack_pA0)) - (*(uint64_t *)((uint32_t)(0x79517350ULL)));
    if (!(condition_is_not_equal)) {
        Arg3 = *(uint64_t *)(v_stack_pA0 + 0x8);
        Arg3 = (Arg3) - (*(uint64_t *)((uint32_t)(0x79517350ULL) + 0x8));
    }
    if (Arg3 == 0) goto loc_0090ADF9;
    goto loc_0090AFCA;
loc_0090B050:
    if (v_stack_p88 == 0) goto loc_0090B062;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != (*(uint64_t *)(v_stack_p88))) goto loc_0090AFFC;
loc_0090B062:
    v_stack_p50 = 0xC000000DULL;
    goto loc_0090AEAD;
loc_0090B06F:
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p60));
    v_stack_p20 = v_stack_pD0;
    Arg1 = 0;
    result = guard_dispatch_icall(Arg1, 1, v_stack_p110, (uint32_t)(0xFFFFFFFFULL));
    goto loc_0090ADC9;
loc_0090B0A9:
    if (v_stack_pA0 == 0) goto loc_0090AF21;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != 1) goto loc_0090AF21;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_pA0, Arg2, v_stack_p110, (uint32_t)(0xFFFFFFFFULL));
    goto loc_0090AF21;
loc_0090B0D0:
    if (v_stack_pB8 == 3) goto loc_0090ACAD;
    result = ExpWnfLookupPermanentName(v_stack_p68, v_stack_pB0, v_stack_p110, (uint32_t)(0xFFFFFFFFULL));
    v_stack_p50 = (uint32_t)(result);
    if (sign_flag) goto loc_0090AEAD;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p80));
    result = ExpWnfValidatePubSubPreconditions(2, v_stack_pB0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p60))), v_stack_pC8);
    v_stack_p50 = (uint32_t)(result);
    if (sign_flag) goto loc_0090AEAD;
    v_stack_p20 = v_stack_p70;
    result = ExpWnfCreateNameInstance(v_stack_p90, v_stack_p68, v_stack_pB0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    v_stack_p50 = (uint32_t)(result);
    result = ExFreePoolWithTag(v_stack_pB0, (uint32_t)(0x20666E57ULL), v_stack_pB0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    v_stack_pB0 = 0;
    if (sign_flag) goto loc_0090AEAD;
    goto loc_0090AE1E;
loc_0090B188:
    local_rbx = (v_stack_p68) ^ (v_stack_pB0);
    v_stack_p108 = local_rbx;
    local_rbx = (v_stack_p70) + (80);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rbx;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg1 = 0;
    if ((*(uint64_t *)(v_stack_p70 + 0x58)) != 1) { Arg1 = *(uint64_t *)(v_stack_p70 + 0x58); }
    if (Arg1 != NULL) goto loc_0090B233;
loc_0090B1ED:
    result = ExGetExtensionTable(*(uint64_t *)(v_rip + 0x5EEF28), v_stack_p70, Arg3, Arg4);
    if (result != 0) goto loc_0090B23D;
loc_0090B208:
    if (result != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x5EEF28);
        result = ExReleaseExtensionTable(Arg1, v_stack_p70, Arg3, Arg4);
    }
    result = ExfReleasePushLockShared(local_rbx, v_stack_p70, Arg3, Arg4);
loc_0090B233:
    goto loc_0090B1ED;
loc_0090B23D:
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8)));
    v_stack_p20 = local_rbx + 16;
    Arg2 = 0;
    Arg1 = 0;
    result = guard_dispatch_icall(Arg1, Arg2, v_stack_p108, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p70 + 0x60)))));
    goto loc_0090B208;
loc_0090B261:
    result = ExReleaseExtensionTable(*(uint64_t *)(v_rip + 0x5EEF28), Arg2, v_stack_p108, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p70 + 0x60)))));
    goto loc_0090ADD2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0090A7A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
