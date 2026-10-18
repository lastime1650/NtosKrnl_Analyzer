# ObpDecrementHandleCount

- RVA: `0x008632E0`–`0x00863AC6` (길이 `2,022` bytes)
- VA: `0x00000001408632E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B84C`
- 디코드: `475`개 명령, `2,022/2,022` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **50**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00863397` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x0086339F` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x008633AF` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x008633D8` → [CmpCloseKeyObject](CmpCloseKeyObject_function_00863AD0.md) (function, `0x00863AD0`)
- `0x008633E9` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x008633F1` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (function, `0x00449AC0`)
- `0x0086342E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00863482` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x008634B5` → [EtwpEventWriteTemplateSessAndProv](EtwpEventWriteTemplateSessAndProv_function_00863D18.md) (function, `0x00863D18`)
- `0x008634E5` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00863501` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086355E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086356C` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00863590` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008635AC` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00863687` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00863695` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008636B9` → [IopCloseFile](IopCloseFile_function_008640C0.md) (function, `0x008640C0`)
- `0x00863710` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00863761` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086376B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008637AC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086380B` → [ObpDeleteSymbolicLinkName](../A7/ObpDeleteSymbolicLinkName_function_00A7BC80.md) (function, `0x00A7BC80`)
- `0x0086381B` → [ObpLookupDirectoryEntry](../85/ObpLookupDirectoryEntry_function_0085D5B0.md) (function, `0x0085D5B0`)
- `0x00863882` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00863890` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008638A8` → [ObpUnlockDirectory](../99/ObpUnlockDirectory_function_0099F8A0.md) (function, `0x0099F8A0`)
- `0x008638B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008638BF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008638ED` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008638F7` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x00863905` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00863926` → [KeAbPostReleaseEx](../../text/26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x00863934` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086393C` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00863974` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00863982` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008639A4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008639C9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008639F2` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00863A0E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00863A27` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x00863A57` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00863A65` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00863A6D` → [HalPutDmaAdapter](../../text/48/HalPutDmaAdapter_function_0048E530.md) (function, `0x0048E530`)
- `0x00863A7B` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00863A89` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00863A9F` → [HalPutDmaAdapter](../../text/48/HalPutDmaAdapter_function_0048E530.md) (function, `0x0048E530`)
- `0x00863AA9` → [ObpDeleteDirectoryName](../99/ObpDeleteDirectoryName_function_0099EF94.md) (function, `0x0099EF94`)
- `0x00863AB3` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)

### Direct callers
- [ObpCreateHandle](ObpCreateHandle_function_0086B950.md) at `0x0086CDFF`
- [ObCompleteObjectDuplication](../89/ObCompleteObjectDuplication_function_0089387C.md) at `0x00893AA6`
- [ObCompleteObjectDuplication](../89/ObCompleteObjectDuplication_function_0089387C.md) at `0x00893ACD`
- [ObDuplicateObject](../8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C5837`
- [ObDuplicateObject](../8C/ObDuplicateObject_function_008C4FA0.md) at `0x008C5D49`
- [ObpInsertOrLocateNamedObject](../99/ObpInsertOrLocateNamedObject_function_0099F2C0.md) at `0x0099F5FC`
- [ObpInsertOrLocateNamedObject](../99/ObpInsertOrLocateNamedObject_function_0099F2C0.md) at `0x0099F629`
- [ObpInsertOrLocateNamedObject](../99/ObpInsertOrLocateNamedObject_function_0099F2C0.md) at `0x0099F7F0`
- [ObReleaseDuplicateInfo](../A2/ObReleaseDuplicateInfo_function_00A21DB8.md) at `0x00A21DD1`

### Static image references
- `0x008632F7` → RVA `0x00E0A740` (`.data`; read)
- `0x00863326` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x00863330` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008633BB` → RVA `0x00863AD0` (`CmpCloseKeyObject`; read)
- `0x0086344F` → RVA `0x00A0CEB0` (`EtwpCloseRegistrationObject`; read)
- `0x00863474` → RVA `0x00EFF840` (`.data`; read)
- `0x0086347B` → RVA `0x00010888` (`.rdata`; read)
- `0x0086369F` → RVA `0x008640C0` (`IopCloseFile`; read)
- `0x008637F6` → RVA `0x00F0F658` (`.data`; read)
- `0x008638C4` → RVA `0x00F0F650` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **43**
  - `0x00863397` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x0086339F` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x008633AF` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x008633E9` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x008633F1` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (`PAGE` → `.text`)
  - `0x0086342E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00863482` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x008634E5` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00863501` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086355E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086356C` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00863590` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008635AC` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00863687` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00863695` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00863710` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00863761` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086376B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008637AC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00863882` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00863890` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008638B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008638BF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008638ED` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008638F7` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x00863905` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00863926` → [KeAbPostReleaseEx](../../text/26/KeAbPostReleaseEx_function_00262210.md) (`PAGE` → `.text`)
  - `0x00863934` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086393C` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00863974` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00863982` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008639A4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008639C9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008639F2` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00863A0E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00863A27` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x00863A57` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00863A65` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00863A6D` → [HalPutDmaAdapter](../../text/48/HalPutDmaAdapter_function_0048E530.md) (`PAGE` → `.text`)
  - `0x00863A7B` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00863A89` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00863A9F` → [HalPutDmaAdapter](../../text/48/HalPutDmaAdapter_function_0048E530.md) (`PAGE` → `.text`)
  - `0x00863AB3` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008632E0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008632E5  55                              push rbp
008632E6  56                              push rsi
008632E7  57                              push rdi
008632E8  41 54                           push r12
008632EA  41 55                           push r13
008632EC  41 56                           push r14
008632EE  41 57                           push r15
008632F0  48 81 EC 80 00 00 00            sub rsp, 0x80
008632F7  48 8B 05 42 74 5A 00            mov rax, qword ptr [rip + 0x5a7442]
008632FE  48 33 C4                        xor rax, rsp
00863301  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00863306  0F 57 C0                        xorps xmm0, xmm0
00863309  45 33 FF                        xor r15d, r15d
0086330C  48 8B C2                        mov rax, rdx
0086330F  48 8B FA                        mov rdi, rdx
00863312  48 C1 E8 08                     shr rax, 8
00863316  48 8B E9                        mov rbp, rcx
00863319  0F B6 D8                        movzx ebx, al
0086331C  45 8B E7                        mov r12d, r15d
0086331F  0F B6 42 18                     movzx eax, byte ptr [rdx + 0x18]
00863323  48 33 D8                        xor rbx, rax
00863326  0F B6 05 1F 3B 76 00            movzx eax, byte ptr [rip + 0x763b1f]
0086332D  48 33 D8                        xor rbx, rax
00863330  48 8D 05 C9 CC 79 FF            lea rax, [rip - 0x863337]
00863337  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
0086333C  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00863341  48 8B 9C D8 00 78 FC 00         mov rbx, qword ptr [rax + rbx*8 + 0xfc7800]
00863349  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
0086334E  F6 43 42 10                     test byte ptr [rbx + 0x42], 0x10
00863352  0F 85 1E 02 00 00               jne 0x140863576
00863358  F6 42 1B 08                     test byte ptr [rdx + 0x1b], 8
0086335C  0F 85 14 02 00 00               jne 0x140863576
00863362  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00863369  F0 48 0F C1 42 08               lock xadd qword ptr [rdx + 8], rax
0086336F  48 8B F0                        mov rsi, rax
00863372  48 83 BB 80 00 00 00 00         cmp qword ptr [rbx + 0x80], 0
0086337A  74 7A                           je 0x1408633f6
0086337C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00863385  45 32 F6                        xor r14b, r14b
00863388  48 39 A8 B8 00 00 00            cmp qword ptr [rax + 0xb8], rbp
0086338F  74 23                           je 0x1408633b4
00863391  48 8B CD                        mov rcx, rbp
00863394  41 B6 01                        mov r14b, 1
00863397  E8 44 8B BE FF                  call 0x14044bee0
0086339C  48 8B C8                        mov rcx, rax
0086339F  E8 1C F5 BD FF                  call 0x1404428c0
008633A4  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
008633A9  48 8B CD                        mov rcx, rbp
008633AC  4C 8B F8                        mov r15, rax
008633AF  E8 4C 34 9B FF                  call 0x140216800
008633B4  48 8B 83 80 00 00 00            mov rax, qword ptr [rbx + 0x80]
008633BB  48 8D 0D 0E 07 00 00            lea rcx, [rip + 0x70e]
008633C2  45 8B C4                        mov r8d, r12d
008633C5  48 3B C1                        cmp rax, rcx
008633C8  0F 85 81 00 00 00               jne 0x14086344f
008633CE  4C 8B CE                        mov r9, rsi
008633D1  48 8D 57 30                     lea rdx, [rdi + 0x30]
008633D5  48 8B CD                        mov rcx, rbp
008633D8  E8 F3 06 00 00                  call 0x140863ad0
008633DD  45 84 F6                        test r14b, r14b
008633E0  74 14                           je 0x1408633f6
008633E2  33 D2                           xor edx, edx
008633E4  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
008633E9  E8 42 49 9B FF                  call 0x140217d30
008633EE  49 8B CF                        mov rcx, r15
008633F1  E8 CA 66 BE FF                  call 0x140449ac0
008633F6  48 83 FE 01                     cmp rsi, 1
008633FA  75 26                           jne 0x140863422
008633FC  0F B6 47 1A                     movzx eax, byte ptr [rdi + 0x1a]
00863400  A8 02                           test al, 2
00863402  74 1E                           je 0x140863422
00863404  83 E0 03                        and eax, 3
00863407  48 8D 0D F2 CB 79 FF            lea rcx, [rip - 0x86340e]
0086340E  48 8B F7                        mov rsi, rdi
00863411  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
00863419  48 2B F0                        sub rsi, rax
0086341C  0F 85 A6 00 00 00               jne 0x1408634c8
00863422  F0 FF 4B 30                     lock dec dword ptr [rbx + 0x30]
00863426  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0086342B  48 33 CC                        xor rcx, rsp
0086342E  E8 0D 92 E4 FF                  call 0x1406ac640
00863433  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
0086343B  48 81 C4 80 00 00 00            add rsp, 0x80
00863442  41 5F                           pop r15
00863444  41 5E                           pop r14
00863446  41 5D                           pop r13
00863448  41 5C                           pop r12
0086344A  5F                              pop rdi
0086344B  5E                              pop rsi
0086344C  5D                              pop rbp
0086344D  C3                              ret
0086344E  CC                              int3
0086344F  48 8D 0D 5A 9A 1A 00            lea rcx, [rip + 0x1a9a5a]
00863456  48 3B C1                        cmp rax, rcx
00863459  0F 85 40 02 00 00               jne 0x14086369f
0086345F  48 83 FE 01                     cmp rsi, 1
00863463  0F 85 74 FF FF FF               jne 0x1408633dd
00863469  0F B6 87 92 00 00 00            movzx eax, byte ptr [rdi + 0x92]
00863470  A8 02                           test al, 2
00863472  74 46                           je 0x1408634ba
00863474  48 8B 0D C5 C3 69 00            mov rcx, qword ptr [rip + 0x69c3c5]
0086347B  48 8D 15 06 D4 7A FF            lea rdx, [rip - 0x852bfa]
00863482  E8 C9 EF B2 FF                  call 0x140392450
00863487  84 C0                           test al, al
00863489  74 2F                           je 0x1408634ba
0086348B  48 8B 47 50                     mov rax, qword ptr [rdi + 0x50]
0086348F  48 8D 15 F2 D3 7A FF            lea rdx, [rip - 0x852c0e]
00863496  48 8B 0D A3 C3 69 00            mov rcx, qword ptr [rip + 0x69c3a3]
0086349D  48 83 C0 28                     add rax, 0x28
008634A1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008634A6  44 8B CE                        mov r9d, esi
008634A9  45 33 C0                        xor r8d, r8d
008634AC  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
008634B5  E8 5E 08 00 00                  call 0x140863d18
008634BA  66 F0 83 8F 92 00 00 00 20      lock or word ptr [rdi + 0x92], 0x20
008634C3  E9 15 FF FF FF                  jmp 0x1408633dd
008634C8  45 33 ED                        xor r13d, r13d
008634CB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008634D4  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008634D8  45 33 C0                        xor r8d, r8d
008634DB  33 D2                           xor edx, edx
008634DD  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008634E4  90                              nop
008634E5  E8 46 CD 9A FF                  call 0x140210230
008634EA  F0 48 0F BA 6F 10 00            lock bts qword ptr [rdi + 0x10], 0
008634F1  48 8B E8                        mov rbp, rax
008634F4  73 10                           jae 0x140863506
008634F6  4C 8D 47 10                     lea r8, [rdi + 0x10]
008634FA  48 8B D0                        mov rdx, rax
008634FD  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863501  E8 8A C7 9A FF                  call 0x14020fc90
00863506  48 85 ED                        test rbp, rbp
00863509  74 04                           je 0x14086350f
0086350B  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
0086350F  48 8B 2E                        mov rbp, qword ptr [rsi]
00863512  48 85 ED                        test rbp, rbp
00863515  0F 84 C6 01 00 00               je 0x1408636e1
0086351B  F6 47 1B 10                     test byte ptr [rdi + 0x1b], 0x10
0086351F  75 0A                           jne 0x14086352b
00863521  4C 39 6F 08                     cmp qword ptr [rdi + 8], r13
00863525  0F 84 4A 02 00 00               je 0x140863775
0086352B  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
0086352F  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00863533  48 8B C8                        mov rcx, rax
00863536  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086353A  48 83 F9 10                     cmp rcx, 0x10
0086353E  48 8D 50 F0                     lea rdx, [rax - 0x10]
00863542  49 0F 46 D5                     cmovbe rdx, r13
00863546  A8 02                           test al, 2
00863548  0F 85 BE 01 00 00               jne 0x14086370c
0086354E  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
00863554  0F 85 B2 01 00 00               jne 0x14086370c
0086355A  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086355E  E8 9D E0 A7 FF                  call 0x1402e1600
00863563  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086356C  E8 7F BA 9F FF                  call 0x14025eff0
00863571  E9 AC FE FF FF                  jmp 0x140863422
00863576  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086357F  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863583  45 33 C0                        xor r8d, r8d
00863586  33 D2                           xor edx, edx
00863588  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086358F  90                              nop
00863590  E8 9B CC 9A FF                  call 0x140210230
00863595  F0 48 0F BA 6F 10 00            lock bts qword ptr [rdi + 0x10], 0
0086359C  4C 8B F8                        mov r15, rax
0086359F  73 10                           jae 0x1408635b1
008635A1  4C 8D 47 10                     lea r8, [rdi + 0x10]
008635A5  48 8B D0                        mov rdx, rax
008635A8  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008635AC  E8 DF C6 9A FF                  call 0x14020fc90
008635B1  4D 85 FF                        test r15, r15
008635B4  74 05                           je 0x1408635bb
008635B6  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
008635BB  48 8B 77 08                     mov rsi, qword ptr [rdi + 8]
008635BF  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
008635C6  F0 48 0F C1 47 08               lock xadd qword ptr [rdi + 8], rax
008635CC  48 8D 15 2D CA 79 FF            lea rdx, [rip - 0x8635d3]
008635D3  48 83 E8 01                     sub rax, 1
008635D7  0F 85 E6 00 00 00               jne 0x1408636c3
008635DD  0F B6 47 1B                     movzx eax, byte ptr [rdi + 0x1b]
008635E1  A8 08                           test al, 8
008635E3  0F 84 DA 00 00 00               je 0x1408636c3
008635E9  0F B6 47 1A                     movzx eax, byte ptr [rdi + 0x1a]
008635ED  48 8B CF                        mov rcx, rdi
008635F0  83 E0 1F                        and eax, 0x1f
008635F3  0F B6 84 10 80 FF F0 00         movzx eax, byte ptr [rax + rdx + 0xf0ff80]
008635FB  48 2B C8                        sub rcx, rax
008635FE  45 33 FF                        xor r15d, r15d
00863601  4C 89 39                        mov qword ptr [rcx], r15
00863604  0F B6 43 42                     movzx eax, byte ptr [rbx + 0x42]
00863608  A8 10                           test al, 0x10
0086360A  74 48                           je 0x140863654
0086360C  0F B6 47 1A                     movzx eax, byte ptr [rdi + 0x1a]
00863610  A8 04                           test al, 4
00863612  0F 85 B3 00 00 00               jne 0x1408636cb
00863618  49 8B D7                        mov rdx, r15
0086361B  F6 47 1B 40                     test byte ptr [rdi + 0x1b], 0x40
0086361F  0F 84 F5 00 00 00               je 0x14086371a
00863625  44 8B 62 08                     mov r12d, dword ptr [rdx + 8]
00863629  41 8B CC                        mov ecx, r12d
0086362C  41 81 E4 FF FF FF 00            and r12d, 0xffffff
00863633  8D 41 FF                        lea eax, [rcx - 1]
00863636  33 C1                           xor eax, ecx
00863638  25 FF FF FF 00                  and eax, 0xffffff
0086363D  33 C1                           xor eax, ecx
0086363F  89 42 08                        mov dword ptr [rdx + 8], eax
00863642  80 7A 0B 00                     cmp byte ptr [rdx + 0xb], 0
00863646  75 0C                           jne 0x140863654
00863648  F7 42 08 FF FF FF 00            test dword ptr [rdx + 8], 0xffffff
0086364F  75 03                           jne 0x140863654
00863651  4C 89 3A                        mov qword ptr [rdx], r15
00863654  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
00863658  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0086365C  48 8B C8                        mov rcx, rax
0086365F  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00863663  48 83 F9 10                     cmp rcx, 0x10
00863667  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086366B  49 0F 46 D7                     cmovbe rdx, r15
0086366F  A8 02                           test al, 2
00863671  0F 85 E6 00 00 00               jne 0x14086375d
00863677  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
0086367D  0F 85 DA 00 00 00               jne 0x14086375d
00863683  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863687  E8 74 DF A7 FF                  call 0x1402e1600
0086368C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00863695  E8 56 B9 9F FF                  call 0x14025eff0
0086369A  E9 D3 FC FF FF                  jmp 0x140863372
0086369F  48 8D 0D 1A 0A 00 00            lea rcx, [rip + 0xa1a]
008636A6  4C 8B CE                        mov r9, rsi
008636A9  48 3B C1                        cmp rax, rcx
008636AC  48 8D 57 30                     lea rdx, [rdi + 0x30]
008636B0  48 8B CD                        mov rcx, rbp
008636B3  0F 85 B2 00 00 00               jne 0x14086376b
008636B9  E8 02 0A 00 00                  call 0x1408640c0
008636BE  E9 1A FD FF FF                  jmp 0x1408633dd
008636C3  45 33 FF                        xor r15d, r15d
008636C6  E9 39 FF FF FF                  jmp 0x140863604
008636CB  83 E0 07                        and eax, 7
008636CE  0F B6 84 10 80 FF F0 00         movzx eax, byte ptr [rax + rdx + 0xf0ff80]
008636D6  48 8B D7                        mov rdx, rdi
008636D9  48 2B D0                        sub rdx, rax
008636DC  E9 3A FF FF FF                  jmp 0x14086361b
008636E1  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
008636E5  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008636E9  48 8B C8                        mov rcx, rax
008636EC  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
008636F0  48 83 F9 10                     cmp rcx, 0x10
008636F4  48 8D 50 F0                     lea rdx, [rax - 0x10]
008636F8  49 0F 46 D5                     cmovbe rdx, r13
008636FC  A8 02                           test al, 2
008636FE  75 0C                           jne 0x14086370c
00863700  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
00863706  0F 84 4E FE FF FF               je 0x14086355a
0086370C  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863710  E8 BB 01 A0 FF                  call 0x1402638d0
00863715  E9 40 FE FF FF                  jmp 0x14086355a
0086371A  48 8B 02                        mov rax, qword ptr [rdx]
0086371D  8B 08                           mov ecx, dword ptr [rax]
0086371F  48 8D 50 08                     lea rdx, [rax + 8]
00863723  85 C9                           test ecx, ecx
00863725  0F 84 17 FF FF FF               je 0x140863642
0086372B  44 8B 42 08                     mov r8d, dword ptr [rdx + 8]
0086372F  41 8B C0                        mov eax, r8d
00863732  25 FF FF FF 00                  and eax, 0xffffff
00863737  74 05                           je 0x14086373e
00863739  48 39 2A                        cmp qword ptr [rdx], rbp
0086373C  74 08                           je 0x140863746
0086373E  48 83 C2 10                     add rdx, 0x10
00863742  FF C9                           dec ecx
00863744  EB DD                           jmp 0x140863723
00863746  44 8B E0                        mov r12d, eax
00863749  41 8D 40 FF                     lea eax, [r8 - 1]
0086374D  41 33 C0                        xor eax, r8d
00863750  25 FF FF FF 00                  and eax, 0xffffff
00863755  41 33 C0                        xor eax, r8d
00863758  E9 E2 FE FF FF                  jmp 0x14086363f
0086375D  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863761  E8 6A 01 A0 FF                  call 0x1402638d0
00863766  E9 18 FF FF FF                  jmp 0x140863683
0086376B  E8 60 73 E5 FF                  call 0x1406baad0
00863770  E9 68 FC FF FF                  jmp 0x1408633dd
00863775  33 C0                           xor eax, eax
00863777  48 8D 8D 28 01 00 00            lea rcx, [rbp + 0x128]
0086377E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00863783  33 D2                           xor edx, edx
00863785  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086378E  0F 57 C0                        xorps xmm0, xmm0
00863791  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
00863796  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
0086379B  44 8D 42 01                     lea r8d, [rdx + 1]
0086379F  C6 44 24 45 01                  mov byte ptr [rsp + 0x45], 1
008637A4  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008637AB  90                              nop
008637AC  E8 7F CA 9A FF                  call 0x140210230
008637B1  F0 48 0F BA AD 28 01 00 00 00   lock bts qword ptr [rbp + 0x128], 0
008637BB  0F 82 56 01 00 00               jb 0x140863917
008637C1  48 85 C0                        test rax, rax
008637C4  0F 85 F3 02 00 00               jne 0x140863abd
008637CA  44 39 6E 18                     cmp dword ptr [rsi + 0x18], r13d
008637CE  0F 85 3B 01 00 00               jne 0x14086390f
008637D4  48 8B C7                        mov rax, rdi
008637D7  4C 8D 35 22 C8 79 FF            lea r14, [rip - 0x8637de]
008637DE  48 C1 E8 08                     shr rax, 8
008637E2  0F B6 C8                        movzx ecx, al
008637E5  0F B6 47 18                     movzx eax, byte ptr [rdi + 0x18]
008637E9  48 33 C8                        xor rcx, rax
008637EC  0F B6 05 59 36 76 00            movzx eax, byte ptr [rip + 0x763659]
008637F3  48 33 C8                        xor rcx, rax
008637F6  48 8B 05 5B BE 6A 00            mov rax, qword ptr [rip + 0x6abe5b]
008637FD  49 39 84 CE 00 78 FC 00         cmp qword ptr [r14 + rcx*8 + 0xfc7800], rax
00863805  75 09                           jne 0x140863810
00863807  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0086380B  E8 70 84 21 00                  call 0x140a7bc80
00863810  48 8D 4E 08                     lea rcx, [rsi + 8]
00863814  33 D2                           xor edx, edx
00863816  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
0086381B  E8 90 9D FF FF                  call 0x14085d5b0
00863820  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00863825  48 8B 32                        mov rsi, qword ptr [rdx]
00863828  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0086382C  48 83 E9 30                     sub rcx, 0x30
00863830  0F B6 41 1A                     movzx eax, byte ptr [rcx + 0x1a]
00863834  83 E0 03                        and eax, 3
00863837  42 0F B6 84 30 80 FF F0 00      movzx eax, byte ptr [rax + r14 + 0xf0ff80]
00863840  48 2B C8                        sub rcx, rax
00863843  4C 89 29                        mov qword ptr [rcx], r13
00863846  48 8B 06                        mov rax, qword ptr [rsi]
00863849  48 89 02                        mov qword ptr [rdx], rax
0086384C  4C 89 2E                        mov qword ptr [rsi], r13
0086384F  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
00863853  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00863857  48 8B C8                        mov rcx, rax
0086385A  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086385E  48 83 F9 10                     cmp rcx, 0x10
00863862  48 8D 50 F0                     lea rdx, [rax - 0x10]
00863866  49 0F 46 D5                     cmovbe rdx, r13
0086386A  A8 02                           test al, 2
0086386C  0F 85 8F 00 00 00               jne 0x140863901
00863872  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
00863878  0F 85 83 00 00 00               jne 0x140863901
0086387E  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863882  E8 79 DD A7 FF                  call 0x1402e1600
00863887  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00863890  E8 5B B7 9F FF                  call 0x14025eff0
00863895  48 85 F6                        test rsi, rsi
00863898  74 58                           je 0x1408638f2
0086389A  48 8B 6E 08                     mov rbp, qword ptr [rsi + 8]
0086389E  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
008638A3  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
008638A8  E8 F3 BF 13 00                  call 0x14099f8a0
008638AD  33 D2                           xor edx, edx
008638AF  48 8B CE                        mov rcx, rsi
008638B2  E8 B9 EF 31 00                  call 0x140b82870
008638B7  BA 4F 62 44 69                  mov edx, 0x6944624f
008638BC  48 8B CF                        mov rcx, rdi
008638BF  E8 1C 40 A9 FF                  call 0x1402f78e0
008638C4  48 8B 05 85 BD 6A 00            mov rax, qword ptr [rip + 0x6abd85]
008638CB  48 8D 55 D0                     lea rdx, [rbp - 0x30]
008638CF  48 C1 EA 08                     shr rdx, 8
008638D3  48 8B CD                        mov rcx, rbp
008638D6  32 55 E8                        xor dl, byte ptr [rbp - 0x18]
008638D9  32 15 6D 35 76 00               xor dl, byte ptr [rip + 0x76356d]
008638DF  3A 50 28                        cmp dl, byte ptr [rax + 0x28]
008638E2  0F 84 C1 01 00 00               je 0x140863aa9
008638E8  BA 4F 62 44 69                  mov edx, 0x6944624f
008638ED  E8 EE 3F A9 FF                  call 0x1402f78e0
008638F2  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
008638F7  E8 34 04 A0 FF                  call 0x140263d30
008638FC  E9 21 FB FF FF                  jmp 0x140863422
00863901  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863905  E8 C6 FF 9F FF                  call 0x1402638d0
0086390A  E9 6F FF FF FF                  jmp 0x14086387e
0086390F  49 8B F5                        mov rsi, r13
00863912  E9 38 FF FF FF                  jmp 0x14086384f
00863917  48 85 C0                        test rax, rax
0086391A  74 0F                           je 0x14086392b
0086391C  48 8B D0                        mov rdx, rax
0086391F  48 8D 8D 28 01 00 00            lea rcx, [rbp + 0x128]
00863926  E8 E5 E8 9F FF                  call 0x140262210
0086392B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00863934  E8 B7 B6 9F FF                  call 0x14025eff0
00863939  48 8B CD                        mov rcx, rbp
0086393C  E8 DF C0 9A FF                  call 0x14020fa20
00863941  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
00863945  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00863949  48 8B C8                        mov rcx, rax
0086394C  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00863950  48 83 F9 10                     cmp rcx, 0x10
00863954  48 8D 50 F0                     lea rdx, [rax - 0x10]
00863958  49 0F 46 D5                     cmovbe rdx, r13
0086395C  A8 02                           test al, 2
0086395E  0F 85 13 01 00 00               jne 0x140863a77
00863964  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
0086396A  0F 85 07 01 00 00               jne 0x140863a77
00863970  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863974  E8 87 DC A7 FF                  call 0x1402e1600
00863979  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00863982  E8 69 B6 9F FF                  call 0x14025eff0
00863987  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00863990  48 8D 8D 28 01 00 00            lea rcx, [rbp + 0x128]
00863997  45 33 C0                        xor r8d, r8d
0086399A  33 D2                           xor edx, edx
0086399C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008639A3  90                              nop
008639A4  E8 87 C8 9A FF                  call 0x140210230
008639A9  F0 48 0F BA AD 28 01 00 00 00   lock bts qword ptr [rbp + 0x128], 0
008639B3  4C 8B F8                        mov r15, rax
008639B6  73 16                           jae 0x1408639ce
008639B8  4C 8D 85 28 01 00 00            lea r8, [rbp + 0x128]
008639BF  48 8B D0                        mov rdx, rax
008639C2  48 8D 8D 28 01 00 00            lea rcx, [rbp + 0x128]
008639C9  E8 C2 C2 9A FF                  call 0x14020fc90
008639CE  4D 85 FF                        test r15, r15
008639D1  74 05                           je 0x1408639d8
008639D3  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
008639D8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008639E1  48 8D 4F 10                     lea rcx, [rdi + 0x10]
008639E5  45 33 C0                        xor r8d, r8d
008639E8  33 D2                           xor edx, edx
008639EA  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008639F1  90                              nop
008639F2  E8 39 C8 9A FF                  call 0x140210230
008639F7  F0 48 0F BA 6F 10 00            lock bts qword ptr [rdi + 0x10], 0
008639FE  4C 8B F8                        mov r15, rax
00863A01  73 10                           jae 0x140863a13
00863A03  4C 8D 47 10                     lea r8, [rdi + 0x10]
00863A07  48 8B D0                        mov rdx, rax
00863A0A  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863A0E  E8 7D C2 9A FF                  call 0x14020fc90
00863A13  4D 85 FF                        test r15, r15
00863A16  74 05                           je 0x140863a1d
00863A18  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
00863A1D  48 39 2E                        cmp qword ptr [rsi], rbp
00863A20  74 6E                           je 0x140863a90
00863A22  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00863A27  E8 04 03 A0 FF                  call 0x140263d30
00863A2C  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
00863A30  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00863A34  48 8B C8                        mov rcx, rax
00863A37  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00863A3B  48 83 F9 10                     cmp rcx, 0x10
00863A3F  48 8D 50 F0                     lea rdx, [rax - 0x10]
00863A43  49 0F 46 D5                     cmovbe rdx, r13
00863A47  A8 02                           test al, 2
00863A49  75 3A                           jne 0x140863a85
00863A4B  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
00863A51  75 32                           jne 0x140863a85
00863A53  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863A57  E8 A4 DB A7 FF                  call 0x1402e1600
00863A5C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00863A65  E8 86 B5 9F FF                  call 0x14025eff0
00863A6A  48 8B CD                        mov rcx, rbp
00863A6D  E8 BE AA C2 FF                  call 0x14048e530
00863A72  E9 54 FA FF FF                  jmp 0x1408634cb
00863A77  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863A7B  E8 50 FE 9F FF                  call 0x1402638d0
00863A80  E9 EB FE FF FF                  jmp 0x140863970
00863A85  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00863A89  E8 42 FE 9F FF                  call 0x1402638d0
00863A8E  EB C3                           jmp 0x140863a53
00863A90  F6 47 1B 10                     test byte ptr [rdi + 0x1b], 0x10
00863A94  75 8C                           jne 0x140863a22
00863A96  4C 39 6F 08                     cmp qword ptr [rdi + 8], r13
00863A9A  75 86                           jne 0x140863a22
00863A9C  48 8B CD                        mov rcx, rbp
00863A9F  E8 8C AA C2 FF                  call 0x14048e530
00863AA4  E9 21 FD FF FF                  jmp 0x1408637ca
00863AA9  E8 E6 B4 13 00                  call 0x14099ef94
00863AAE  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00863AB3  E8 78 02 A0 FF                  call 0x140263d30
00863AB8  E9 65 F9 FF FF                  jmp 0x140863422
00863ABD  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
00863AC1  E9 04 FD FF FF                  jmp 0x1408637ca
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpDecrementHandleCount(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p45;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 5928002)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r15 = 0;
    result = (a2) >> (8);
    v_rbx = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a2 + 24));
    v_rbx = (v_rbx) ^ (*(unsigned __int8 *)(v_rip + 7748383));
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8794935 + v_rbx * 8 + 16545792) + 66)) & (16)) != 0) goto loc_00863576;
    if (((*(unsigned __int8 *)(a2 + 27)) & (8)) != 0) goto loc_00863576;
loc_00863372:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8794935 + v_rbx * 8 + 16545792) + 128)) == 0) goto loc_008633F6;
    v_r14 = 0;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != a1) {
        a1 = a1;
        v_r14 = 1;
        result = PsGetProcessServerSilo(a1, a2, a3, a4);
        a1 = result;
        result = PsAttachSiloToCurrentThread(a1, a2, a3, a4);
        a2 = v_stack_m70;
        a1 = a1;
        v_r15 = result;
        result = KeStackAttachProcess(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8794935 + v_rbx * 8 + 16545792) + 128)) != (v_rip + 1806)) goto loc_0086344F;
    result = CmpCloseKeyObject(a1, a2 + 48, 0, -1);
loc_008633DD:
    if ((unsigned __int8)(v_r14) != 0) {
        a2 = 0;
        a1 = v_stack_m70;
        result = KiUnstackDetachProcess(a1, a2, 0, -1);
        a1 = v_r15;
        result = PsDetachSiloFromCurrentThread(a1, a2, 0, -1);
    }
    if (-1 != 1) goto loc_00863422;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 26))) & (2)) == 0) goto loc_00863422;
    result = (unsigned int)((*(unsigned __int8 *)(a2 + 26)) & (3));
    v_rsi = (0) - (*(unsigned __int8 *)(result + v_rip - 8795150 * 1 + 15794048));
    if (condition_is_not_equal) goto loc_008634C8;
loc_00863422:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 0, -1);
    v_rsp = (v_rsp) + (128);
    return result;
loc_0086344F:
    if (result != (v_rip + 1743450)) goto loc_0086369F;
    if (v_rsi != 1) goto loc_008633DD;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 146))) & (2)) == 0) goto loc_008634BA;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6931397), v_rip - 8727546, 0, -1);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(a2 + 80);
        a2 = v_rip - 8727566;
        a1 = *(unsigned __int64 *)(v_rip + 6931363);
        result = (result) + (40);
        v_stack_p28 = result;
        a4 = (unsigned int)(v_rsi);
        a3 = 0;
        v_stack_p20 = 0;
        result = EtwpEventWriteTemplateSessAndProv(a1, a2, a3, a4);
    }
    goto loc_008633DD;
loc_008634C8:
    v_r13 = 0;
loc_008634CB:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a2 + 16, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a2 + 16;
        a2 = result;
        a1 = a2 + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_008636E1;
    if (((*(unsigned __int8 *)(a2 + 27)) & (16)) != 0) goto loc_0086352B;
    if ((*(unsigned __int64 *)(a2 + 8)) == 0) goto loc_00863775;
loc_0086352B:
    a1 = (*(unsigned __int64 *)(a2 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(a2 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 16))) & (2)) != 0) goto loc_0086370C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 16))) & (2)) != 0) goto loc_0086370C;
loc_0086355A:
    result = KeAbPostRelease(a2 + 16, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    goto loc_00863422;
loc_00863576:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a2 + 16, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a2 + 16;
        a2 = result;
        a1 = a2 + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (-1) - (1);
    if (condition_is_not_equal) goto loc_008636C3;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 27))) & (8)) == 0) goto loc_008636C3;
    result = (unsigned int)((*(unsigned __int8 *)(a2 + 26)) & (31));
    a1 = (a2) - (*(unsigned __int8 *)(result + v_rip - 8795603 * 1 + 15794048));
    v_r15 = 0;
    *(unsigned __int64 *)(a1) = 0;
loc_00863604:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p18 + 66))) & (16)) == 0) goto loc_00863654;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 26))) & (4)) != 0) goto loc_008636CB;
loc_0086361B:
    if (((*(unsigned __int8 *)(a2 + 27)) & (64)) == 0) goto loc_0086371A;
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 8))) & (0xFFFFFFULL));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))) - 1) ^ ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))))));
    result = (unsigned int)((result) & (0xFFFFFFULL));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))))));
loc_0086363F:
    *(unsigned int *)(0 + 8) = (unsigned int)(result);
loc_00863642:
    if ((*(unsigned __int8 *)(0 + 11)) != 0) goto loc_00863654;
    if (((*(unsigned int *)(0 + 8)) & (0xFFFFFFULL)) == 0) {
        *(unsigned __int64 *)(0) = 0;
    }
    a1 = (*(unsigned __int64 *)(a2 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(a2 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 16))) & (2)) != 0) goto loc_0086375D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 16))) & (2)) != 0) goto loc_0086375D;
loc_00863683:
    result = KeAbPostRelease(a2 + 16, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    goto loc_00863372;
loc_0086369F:
    if (result != (v_rip + 2586)) goto loc_0086376B;
    result = IopCloseFile(*(unsigned __int64 *)(v_rsi), a2 + 48, a3, *(unsigned __int64 *)(a2 + 8));
    goto loc_008633DD;
loc_008636C3:
    v_r15 = 0;
    goto loc_00863604;
loc_008636CB:
    result = (unsigned int)((result) & (7));
    a2 = (a2) - (*(unsigned __int8 *)(result + a2 + 48 * 1 + 15794048));
    goto loc_0086361B;
loc_008636E1:
    a1 = (*(unsigned __int64 *)(a2 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(a2 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 16))) & (2)) != 0) goto loc_0086370C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 16))) & (2)) == 0) goto loc_0086355A;
loc_0086370C:
    result = ExfReleasePushLock(a2 + 16, a2, a3, *(unsigned __int64 *)(a2 + 8));
    goto loc_0086355A;
loc_0086371A:
loc_00863723:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2)))) == 0) goto loc_00863642;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 8 + 8))))) & (0xFFFFFFULL));
    if (condition_is_equal) goto loc_0086373E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 8)) == (*(unsigned __int64 *)(v_rsi))) goto loc_00863746;
loc_0086373E:
    a2 = (*(unsigned __int64 *)(a2) + 8) + (16);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2)))) - 1);
    goto loc_00863723;
loc_00863746:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 8 + 8)) - 1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 8 + 8)))));
    result = (unsigned int)((result) & (0xFFFFFFULL));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 8 + 8)))));
    goto loc_0086363F;
loc_0086375D:
    result = ExfReleasePushLock(a2 + 16, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 8 + 8)), *(unsigned __int64 *)(a2 + 8));
    goto loc_00863683;
loc_0086376B:
    result = guard_dispatch_icall(a2 + 16, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 8 + 8)), *(unsigned __int64 *)(a2 + 8));
    goto loc_008633DD;
loc_00863775:
    result = 0;
    v_stack_p40 = 0;
    a2 = 0;
    v_stack_p30 = v_xmm0;
    v_stack_p30 = *(unsigned __int64 *)(v_rsi);
    v_stack_p45 = 1;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_rsi) + 296, a2, a2 + 1, *(unsigned __int64 *)(a2 + 8));
    if (condition_is_below) goto loc_00863917;
    if (result != 0) goto loc_00863ABD;
loc_008637CA:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 24)) != 0) goto loc_0086390F;
    result = (0) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a2 + 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7747161));
    result = *(unsigned __int64 *)(v_rip + 6995547);
    if ((*(unsigned __int64 *)(v_rip - 8796126 + a1 * 8 + 16545792)) == (*(unsigned __int64 *)(v_rip + 6995547))) {
        a1 = a2 + 48;
        result = ObpDeleteSymbolicLinkName(a1, a2, a2 + 1, *(unsigned __int64 *)(a2 + 8));
    }
    a2 = 0;
    result = ObpLookupDirectoryEntry(*(unsigned __int64 *)(a2 + 8) + 8, a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8)) - (48);
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 26)) & (3));
    a1 = (a1) - (*(unsigned __int8 *)(result + v_rip - 8796126 * 1 + 15794048));
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int64 *)(v_stack_p38) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38)) = 0;
loc_0086384F:
    a1 = (*(unsigned __int64 *)(a2 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(a2 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 16))) & (2)) != 0) goto loc_00863901;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 16))) & (2)) != 0) goto loc_00863901;
loc_0086387E:
    result = KeAbPostRelease(a2 + 16, a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    if (*(unsigned __int64 *)(v_stack_p38) == 0) goto loc_008638F2;
    result = ObpUnlockDirectory(v_stack_p30, a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p38), a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    result = ObfDereferenceObjectWithTag(v_stack_p30, (unsigned int)(0x6944624FULL), v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8) - 48) >> (8);
    a2 = (unsigned __int8)((a2) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8) - 24)));
    a2 = (unsigned __int8)((a2) ^ (*(unsigned __int8 *)(v_rip + 7746925)));
    if (((unsigned __int8)(a2)) == (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 6995333) + 40))) goto loc_00863AA9;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8), (unsigned int)(0x6944624FULL), v_stack_p30, *(unsigned __int64 *)(a2 + 8));
loc_008638F2:
    result = ObpReleaseLookupContext(v_stack_p30, (unsigned int)(0x6944624FULL), v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    goto loc_00863422;
loc_00863901:
    result = ExfReleasePushLock(v_stack_p30 + 16, (unsigned int)(0x6944624FULL), v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    goto loc_0086387E;
loc_0086390F:
    goto loc_0086384F;
loc_00863917:
    if (result != 0) {
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8) + 296;
        result = KeAbPostReleaseEx(a1, a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    }
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    result = ObfReferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8), a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    a1 = (*(unsigned __int64 *)(v_stack_p30 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(v_stack_p30 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p30 + 16))) & (2)) != 0) goto loc_00863A77;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p30 + 16))) & (2)) != 0) goto loc_00863A77;
loc_00863970:
    result = KeAbPostRelease(v_stack_p30 + 16, a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p30, *(unsigned __int64 *)(a2 + 8));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8) + 296, a2, a3, *(unsigned __int64 *)(a2 + 8));
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8) + 296;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8) + 296;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(a2 + 8));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_p30 + 16, a2, a3, *(unsigned __int64 *)(a2 + 8));
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_p30 + 16;
        a2 = result;
        a1 = v_stack_p30 + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(a2 + 8));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(0)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8))) goto loc_00863A90;
loc_00863A22:
    result = ObpReleaseLookupContext(v_stack_p30, a2, a3, *(unsigned __int64 *)(a2 + 8));
    a1 = (*(unsigned __int64 *)(v_stack_p30 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(v_stack_p30 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p30 + 16))) & (2)) != 0) goto loc_00863A85;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p30 + 16))) & (2)) != 0) goto loc_00863A85;
loc_00863A53:
    result = KeAbPostRelease(v_stack_p30 + 16, a2, a3, *(unsigned __int64 *)(a2 + 8));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, *(unsigned __int64 *)(a2 + 8));
    result = HalPutDmaAdapter(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8), a2, a3, *(unsigned __int64 *)(a2 + 8));
    goto loc_008634CB;
loc_00863A77:
    result = ExfReleasePushLock(v_stack_p30 + 16, a2, a3, *(unsigned __int64 *)(a2 + 8));
    goto loc_00863970;
loc_00863A85:
    result = ExfReleasePushLock(v_stack_p30 + 16, a2, a3, *(unsigned __int64 *)(a2 + 8));
    goto loc_00863A53;
loc_00863A90:
    if (((*(unsigned __int8 *)(v_stack_p30 + 27)) & (16)) != 0) goto loc_00863A22;
    if ((*(unsigned __int64 *)(v_stack_p30 + 8)) != 0) goto loc_00863A22;
    result = HalPutDmaAdapter(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8), a2, a3, *(unsigned __int64 *)(a2 + 8));
    goto loc_008637CA;
loc_00863AA9:
    result = ObpDeleteDirectoryName(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38) + 8), a2, a3, *(unsigned __int64 *)(a2 + 8));
    result = ObpReleaseLookupContext(v_stack_p30, a2, a3, *(unsigned __int64 *)(a2 + 8));
    goto loc_00863422;
loc_00863ABD:
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_008637CA;
}
```

## 5. (Beta) C Style

```c
int64_t ObpDecrementHandleCount(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p45;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x5A7442)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r15 = 0;
    result = (Arg2) >> (8);
    local_rbx = ((uint8_t)(result)) ^ (*(uint8_t *)(arg2 + 0x18));
    local_rbx = (local_rbx) ^ (*(uint8_t *)(v_rip + 0x763B1F));
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x863337 + local_rbx * 8 + 0xFC7800) + 0x42)) & (16)) != 0) goto loc_00863576;
    if (((*(uint8_t *)(arg2 + 0x1B)) & (8)) != 0) goto loc_00863576;
loc_00863372:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x863337 + local_rbx * 8 + 0xFC7800) + 0x80)) == 0) goto loc_008633F6;
    local_r14 = 0;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != Arg1) {
        Arg1 = Arg1;
        local_r14 = 1;
        result = PsGetProcessServerSilo(Arg1, Arg2, a3, a4);
        Arg1 = result;
        result = PsAttachSiloToCurrentThread(Arg1, Arg2, a3, a4);
        Arg2 = v_stack_m70;
        Arg1 = Arg1;
        local_r15 = result;
        result = KeStackAttachProcess(Arg1, Arg2, a3, a4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x863337 + local_rbx * 8 + 0xFC7800) + 0x80)) != (v_rip + 1806)) goto loc_0086344F;
    result = CmpCloseKeyObject(Arg1, Arg2 + 48, 0, -1);
loc_008633DD:
    if ((uint8_t)(local_r14) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m70;
        result = KiUnstackDetachProcess(Arg1, Arg2, 0, -1);
        Arg1 = local_r15;
        result = PsDetachSiloFromCurrentThread(Arg1, Arg2, 0, -1);
    }
    if (-1 != 1) goto loc_00863422;
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0x1A))) & (2)) == 0) goto loc_00863422;
    result = (uint32_t)((*(uint8_t *)(arg2 + 0x1A)) & (3));
    local_rsi = (0) - (*(uint8_t *)(result + v_rip - 0x86340E * 1 + 0xF0FF80));
    if (condition_is_not_equal) goto loc_008634C8;
loc_00863422:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 0, -1);
    local_rsp = (local_rsp) + (128);
    return result;
loc_0086344F:
    if (result != (v_rip + 1743450)) goto loc_0086369F;
    if (local_rsi != 1) goto loc_008633DD;
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0x92))) & (2)) == 0) goto loc_008634BA;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x69C3C5), v_rip - 8727546, 0, -1);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(arg2 + 0x50);
        Arg2 = v_rip - 8727566;
        Arg1 = *(uint64_t *)(v_rip + 0x69C3A3);
        result = (result) + (40);
        v_stack_p28 = result;
        a4 = (uint32_t)(local_rsi);
        a3 = 0;
        v_stack_p20 = 0;
        result = EtwpEventWriteTemplateSessAndProv(Arg1, Arg2, a3, a4);
    }
    goto loc_008633DD;
loc_008634C8:
    local_r13 = 0;
loc_008634CB:
    a3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg2 + 16, Arg2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = Arg2 + 16;
        Arg2 = result;
        Arg1 = Arg2 + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, a3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(local_rsi) == 0) goto loc_008636E1;
    if (((*(uint8_t *)(arg2 + 0x1B)) & (16)) != 0) goto loc_0086352B;
    if ((*(uint64_t *)(arg2 + 0x8)) == 0) goto loc_00863775;
loc_0086352B:
    Arg1 = (*(uint64_t *)(arg2 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(arg2 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg2 + 0x10))) & (2)) != 0) goto loc_0086370C;
    if ((((uint8_t)(*(uint64_t *)(arg2 + 0x10))) & (2)) != 0) goto loc_0086370C;
loc_0086355A:
    result = KeAbPostRelease(Arg2 + 16, Arg2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    goto loc_00863422;
loc_00863576:
    a3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg2 + 16, Arg2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = Arg2 + 16;
        Arg2 = result;
        Arg1 = Arg2 + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, a3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (-1) - (1);
    if (condition_is_not_equal) goto loc_008636C3;
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0x1B))) & (8)) == 0) goto loc_008636C3;
    result = (uint32_t)((*(uint8_t *)(arg2 + 0x1A)) & (31));
    Arg1 = (Arg2) - (*(uint8_t *)(result + v_rip - 0x8635D3 * 1 + 0xF0FF80));
    local_r15 = 0;
    *(uint64_t *)(Arg1) = 0;
loc_00863604:
    if ((((uint8_t)(*(uint8_t *)(v_stack_p18 + 0x42))) & (16)) == 0) goto loc_00863654;
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0x1A))) & (4)) != 0) goto loc_008636CB;
loc_0086361B:
    if (((*(uint8_t *)(arg2 + 0x1B)) & (64)) == 0) goto loc_0086371A;
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x8))) & (0xFFFFFFULL));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))) - 1) ^ ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))))));
    result = (uint32_t)((result) & (0xFFFFFFULL));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))))));
loc_0086363F:
    *(uint32_t *)(0 + 0x8) = (uint32_t)(result);
loc_00863642:
    if ((*(uint8_t *)(0 + 0xB)) != 0) goto loc_00863654;
    if (((*(uint32_t *)(0 + 0x8)) & (0xFFFFFFULL)) == 0) {
        *(uint64_t *)(0) = 0;
    }
    Arg1 = (*(uint64_t *)(arg2 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(arg2 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg2 + 0x10))) & (2)) != 0) goto loc_0086375D;
    if ((((uint8_t)(*(uint64_t *)(arg2 + 0x10))) & (2)) != 0) goto loc_0086375D;
loc_00863683:
    result = KeAbPostRelease(Arg2 + 16, Arg2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    goto loc_00863372;
loc_0086369F:
    if (result != (v_rip + 2586)) goto loc_0086376B;
    result = IopCloseFile(*(uint64_t *)(local_rsi), Arg2 + 48, a3, *(uint64_t *)(arg2 + 0x8));
    goto loc_008633DD;
loc_008636C3:
    local_r15 = 0;
    goto loc_00863604;
loc_008636CB:
    result = (uint32_t)((result) & (7));
    Arg2 = (Arg2) - (*(uint8_t *)(result + arg2 + 0x30 * 1 + 0xF0FF80));
    goto loc_0086361B;
loc_008636E1:
    Arg1 = (*(uint64_t *)(arg2 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(arg2 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg2 + 0x10))) & (2)) != 0) goto loc_0086370C;
    if ((((uint8_t)(*(uint64_t *)(arg2 + 0x10))) & (2)) == 0) goto loc_0086355A;
loc_0086370C:
    result = ExfReleasePushLock(Arg2 + 16, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    goto loc_0086355A;
loc_0086371A:
loc_00863723:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2)))) == 0) goto loc_00863642;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x8 + 0x8))))) & (0xFFFFFFULL));
    if (condition_is_equal) goto loc_0086373E;
    if ((*(uint64_t *)(*(uint64_t *)(arg2) + 0x8)) == (*(uint64_t *)(local_rsi))) goto loc_00863746;
loc_0086373E:
    Arg2 = (*(uint64_t *)(arg2) + 8) + (16);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2)))) - 1);
    goto loc_00863723;
loc_00863746:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x8 + 0x8)) - 1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x8 + 0x8)))));
    result = (uint32_t)((result) & (0xFFFFFFULL));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x8 + 0x8)))));
    goto loc_0086363F;
loc_0086375D:
    result = ExfReleasePushLock(Arg2 + 16, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x8 + 0x8)), *(uint64_t *)(arg2 + 0x8));
    goto loc_00863683;
loc_0086376B:
    result = guard_dispatch_icall(Arg2 + 16, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x8 + 0x8)), *(uint64_t *)(arg2 + 0x8));
    goto loc_008633DD;
loc_00863775:
    result = 0;
    v_stack_p40 = 0;
    Arg2 = 0;
    v_stack_p30 = v_xmm0;
    v_stack_p30 = *(uint64_t *)(local_rsi);
    v_stack_p45 = 1;
    result = KeAbPreAcquire(*(uint64_t *)(local_rsi) + 296, Arg2, Arg2 + 1, *(uint64_t *)(arg2 + 0x8));
    if (condition_is_below) goto loc_00863917;
    if (result != 0) goto loc_00863ABD;
loc_008637CA:
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x18)) != 0) goto loc_0086390F;
    result = (0) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg2 + 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x763659));
    result = *(uint64_t *)(v_rip + 0x6ABE5B);
    if ((*(uint64_t *)(v_rip - 0x8637DE + Arg1 * 8 + 0xFC7800)) == (*(uint64_t *)(v_rip + 0x6ABE5B))) {
        Arg1 = Arg2 + 48;
        result = ObpDeleteSymbolicLinkName(Arg1, Arg2, Arg2 + 1, *(uint64_t *)(arg2 + 0x8));
    }
    Arg2 = 0;
    result = ObpLookupDirectoryEntry(*(uint64_t *)(arg2 + 0x8) + 8, Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8)) - (48);
    result = (uint32_t)((*(uint8_t *)(Arg1 + 0x1A)) & (3));
    Arg1 = (Arg1) - (*(uint8_t *)(result + v_rip - 0x8637DE * 1 + 0xF0FF80));
    *(uint64_t *)(Arg1) = 0;
    *(uint64_t *)(v_stack_p38) = *(uint64_t *)(*(uint64_t *)(v_stack_p38));
    *(uint64_t *)(*(uint64_t *)(v_stack_p38)) = 0;
loc_0086384F:
    Arg1 = (*(uint64_t *)(arg2 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(arg2 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg2 + 0x10))) & (2)) != 0) goto loc_00863901;
    if ((((uint8_t)(*(uint64_t *)(arg2 + 0x10))) & (2)) != 0) goto loc_00863901;
loc_0086387E:
    result = KeAbPostRelease(Arg2 + 16, Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    if (*(uint64_t *)(v_stack_p38) == 0) goto loc_008638F2;
    result = ObpUnlockDirectory(v_stack_p30, Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p38), Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    result = ObfDereferenceObjectWithTag(v_stack_p30, (uint32_t)(0x6944624FULL), v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8) - 48) >> (8);
    Arg2 = (uint8_t)((Arg2) ^ (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8) - 0x18)));
    Arg2 = (uint8_t)((Arg2) ^ (*(uint8_t *)(v_rip + 0x76356D)));
    if (((uint8_t)(Arg2)) == (*(uint8_t *)(*(uint64_t *)(v_rip + 0x6ABD85) + 0x28))) goto loc_00863AA9;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8), (uint32_t)(0x6944624FULL), v_stack_p30, *(uint64_t *)(arg2 + 0x8));
loc_008638F2:
    result = ObpReleaseLookupContext(v_stack_p30, (uint32_t)(0x6944624FULL), v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    goto loc_00863422;
loc_00863901:
    result = ExfReleasePushLock(v_stack_p30 + 16, (uint32_t)(0x6944624FULL), v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    goto loc_0086387E;
loc_0086390F:
    goto loc_0086384F;
loc_00863917:
    if (result != 0) {
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8) + 296;
        result = KeAbPostReleaseEx(Arg1, Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    }
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    result = ObfReferenceObject(*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8), Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    Arg1 = (*(uint64_t *)(v_stack_p30 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(v_stack_p30 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_stack_p30 + 0x10))) & (2)) != 0) goto loc_00863A77;
    if ((((uint8_t)(*(uint64_t *)(v_stack_p30 + 0x10))) & (2)) != 0) goto loc_00863A77;
loc_00863970:
    result = KeAbPostRelease(v_stack_p30 + 16, Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p30, *(uint64_t *)(arg2 + 0x8));
    a3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8) + 296, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    if (!(condition_is_above_or_equal)) {
        a3 = *(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8) + 296;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8) + 296;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    a3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_p30 + 16, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_p30 + 16;
        Arg2 = result;
        Arg1 = v_stack_p30 + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(0)) == (*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8))) goto loc_00863A90;
loc_00863A22:
    result = ObpReleaseLookupContext(v_stack_p30, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    Arg1 = (*(uint64_t *)(v_stack_p30 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(v_stack_p30 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_stack_p30 + 0x10))) & (2)) != 0) goto loc_00863A85;
    if ((((uint8_t)(*(uint64_t *)(v_stack_p30 + 0x10))) & (2)) != 0) goto loc_00863A85;
loc_00863A53:
    result = KeAbPostRelease(v_stack_p30 + 16, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    result = HalPutDmaAdapter(*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8), Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    goto loc_008634CB;
loc_00863A77:
    result = ExfReleasePushLock(v_stack_p30 + 16, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    goto loc_00863970;
loc_00863A85:
    result = ExfReleasePushLock(v_stack_p30 + 16, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    goto loc_00863A53;
loc_00863A90:
    if (((*(uint8_t *)(v_stack_p30 + 0x1B)) & (16)) != 0) goto loc_00863A22;
    if ((*(uint64_t *)(v_stack_p30 + 0x8)) != 0) goto loc_00863A22;
    result = HalPutDmaAdapter(*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8), Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    goto loc_008637CA;
loc_00863AA9:
    result = ObpDeleteDirectoryName(*(uint64_t *)(*(uint64_t *)(v_stack_p38) + 0x8), Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    result = ObpReleaseLookupContext(v_stack_p30, Arg2, a3, *(uint64_t *)(arg2 + 0x8));
    goto loc_00863422;
loc_00863ABD:
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_008637CA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R/W` |
| `Arg2` | `+ 0x10` | `8` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R/W` |
| `Arg2` | `+ 0x18` | `8` | `R` |
| `Arg2` | `+ 0x18` | `32` | `R` |
| `Arg2` | `+ 0x1A` | `8` | `R` |
| `Arg2` | `+ 0x1B` | `8` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0x92` | `8` | `R` |
| `Arg2` | `+ 0x92` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008632E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
