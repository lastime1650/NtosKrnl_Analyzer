# IopAllocRealFileObject

- RVA: `0x00899720`–`0x00899ED4` (길이 `1,972` bytes)
- VA: `0x0000000140899720`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E528`
- 디코드: `470`개 명령, `1,972/1,972` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **41**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x008997BA` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x008997D7` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x008997F5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0089982E` → [ObpCaptureObjectCreateInformation](ObpCaptureObjectCreateInformation_function_0089B930.md) (function, `0x0089B930`)
- `0x0089988A` → [ObpAllocateObject](ObpAllocateObject_function_00899FF0.md) (function, `0x00899FF0`)
- `0x008998DD` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008998F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00899923` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0089993E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0089996B` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x008999B3` → [IopRetrieveTransactionParameters](IopRetrieveTransactionParameters_function_00898520.md) (function, `0x00898520`)
- `0x008999E1` → [IopCheckInitiatorHint](../../text/45/IopCheckInitiatorHint_function_00457134.md) (function, `0x00457134`)
- `0x00899A39` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x00899ACE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00899B05` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00899B27` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00899BCA` → [IopGetSetSpecificExtension](../../text/42/IopGetSetSpecificExtension_function_0042EE80.md) (function, `0x0042EE80`)
- `0x00899BF6` → [IopRetrieveTransactionParametersFromOpenPacket](../A2/IopRetrieveTransactionParametersFromOpenPacket_function_00A2027C.md) (function, `0x00A2027C`)
- `0x00899C2B` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x00899C40` → [PsAcquireSiloHardReference](../../text/46/PsAcquireSiloHardReference_function_00467620.md) (function, `0x00467620`)
- `0x00899C72` → [IopGetSetSpecificExtension](../../text/42/IopGetSetSpecificExtension_function_0042EE80.md) (function, `0x0042EE80`)
- `0x00899C9D` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00899CCA` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00899CE7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00899D27` → [IopSetFileObjectExtensionFlag](../../text/43/IopSetFileObjectExtensionFlag_function_0043D710.md) (function, `0x0043D710`)
- `0x00899D40` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x00899D5A` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (function, `0x00438490`)
- `0x00899D62` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x00899D8E` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (function, `0x00438490`)
- `0x00899D96` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x00899DD5` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00899E0D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00899E1A` → [PsIsServerSilo](../../text/22/PsIsServerSilo_function_00225828.md) (function, `0x00225828`)
- `0x00899E2A` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (function, `0x00438490`)
- `0x00899E67` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00899E7C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00899E91` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00899E9B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00899EA8` → [ObpRegisterObject](../AC/ObpRegisterObject_function_00ACF3EC.md) (function, `0x00ACF3EC`)
- `0x00899EC0` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00899ECA` → [PsReleaseSiloHardReference](../../text/38/PsReleaseSiloHardReference_function_0038DEA0.md) (function, `0x0038DEA0`)

### Direct callers
- [IopParseDevice](IopParseDevice_function_0089E510.md) at `0x0089F329`
- [IopParseDevice](IopParseDevice_function_0089E510.md) at `0x0089F5E7`

### Static image references
- `0x0089973C` → RVA `0x00E0A740` (`.data`; read)
- `0x00899756` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x0089989E` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x00899AEF` → RVA `0x00FD9BD0` (`PAGEDATA`; read)
- `0x00899D74` → RVA `0x00FC5010` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **34**
  - `0x008997BA` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x008997D7` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x008997F5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008998DD` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008998F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00899923` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x0089993E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0089996B` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x008999E1` → [IopCheckInitiatorHint](../../text/45/IopCheckInitiatorHint_function_00457134.md) (`PAGE` → `.text`)
  - `0x00899A39` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x00899ACE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00899BCA` → [IopGetSetSpecificExtension](../../text/42/IopGetSetSpecificExtension_function_0042EE80.md) (`PAGE` → `.text`)
  - `0x00899C2B` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x00899C40` → [PsAcquireSiloHardReference](../../text/46/PsAcquireSiloHardReference_function_00467620.md) (`PAGE` → `.text`)
  - `0x00899C72` → [IopGetSetSpecificExtension](../../text/42/IopGetSetSpecificExtension_function_0042EE80.md) (`PAGE` → `.text`)
  - `0x00899C9D` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x00899CCA` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x00899CE7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00899D27` → [IopSetFileObjectExtensionFlag](../../text/43/IopSetFileObjectExtensionFlag_function_0043D710.md) (`PAGE` → `.text`)
  - `0x00899D40` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x00899D5A` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (`PAGE` → `.text`)
  - `0x00899D62` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x00899D8E` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (`PAGE` → `.text`)
  - `0x00899D96` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x00899DD5` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00899E0D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00899E1A` → [PsIsServerSilo](../../text/22/PsIsServerSilo_function_00225828.md) (`PAGE` → `.text`)
  - `0x00899E2A` → [IoGetSilo](../../text/43/IoGetSilo_function_00438490.md) (`PAGE` → `.text`)
  - `0x00899E67` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00899E7C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00899E91` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00899E9B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00899EC0` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x00899ECA` → [PsReleaseSiloHardReference](../../text/38/PsReleaseSiloHardReference_function_0038DEA0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00899720  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00899725  55                              push rbp
00899726  56                              push rsi
00899727  57                              push rdi
00899728  41 54                           push r12
0089972A  41 55                           push r13
0089972C  41 56                           push r14
0089972E  41 57                           push r15
00899730  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00899735  48 81 EC D0 00 00 00            sub rsp, 0xd0
0089973C  48 8B 05 FD 0F 57 00            mov rax, qword ptr [rip + 0x570ffd]
00899743  48 33 C4                        xor rax, rsp
00899746  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0089974A  65 4C 8B 34 25 20 00 00 00      mov r14, qword ptr gs:[0x20]
00899753  45 33 FF                        xor r15d, r15d
00899756  4C 8B 2D 83 D3 72 00            mov r13, qword ptr [rip + 0x72d383]
0089975D  4C 8B E1                        mov r12, rcx
00899760  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
00899764  41 8B C1                        mov eax, r9d
00899767  48 8B 75 6F                     mov rsi, qword ptr [rbp + 0x6f]
0089976B  0F 57 C0                        xorps xmm0, xmm0
0089976E  49 8B 9E 40 08 00 00            mov rbx, qword ptr [r14 + 0x840]
00899775  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0089977A  48 8B CB                        mov rcx, rbx
0089977D  66 44 89 7C 24 40               mov word ptr [rsp + 0x40], r15w
00899783  89 45 87                        mov dword ptr [rbp - 0x79], eax
00899786  FF 43 14                        inc dword ptr [rbx + 0x14]
00899789  4C 89 45 DF                     mov qword ptr [rbp - 0x21], r8
0089978D  48 89 55 A7                     mov qword ptr [rbp - 0x59], rdx
00899791  48 C7 45 AF 30 00 00 00         mov qword ptr [rbp - 0x51], 0x30
00899799  44 89 7D CB                     mov dword ptr [rbp - 0x35], r15d
0089979D  4C 89 7D B7                     mov qword ptr [rbp - 0x49], r15
008997A1  89 45 C7                        mov dword ptr [rbp - 0x39], eax
008997A4  4C 89 7D BF                     mov qword ptr [rbp - 0x41], r15
008997A8  F3 0F 7F 45 CF                  movdqu xmmword ptr [rbp - 0x31], xmm0
008997AD  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
008997B2  0F 11 45 8F                     movups xmmword ptr [rbp - 0x71], xmm0
008997B6  4C 89 7D 9F                     mov qword ptr [rbp - 0x61], r15
008997BA  E8 B1 0D E2 FF                  call 0x1406ba570
008997BF  48 8B F8                        mov rdi, rax
008997C2  48 85 C0                        test rax, rax
008997C5  75 3B                           jne 0x140899802
008997C7  FF 43 18                        inc dword ptr [rbx + 0x18]
008997CA  49 8B 9E 48 08 00 00            mov rbx, qword ptr [r14 + 0x848]
008997D1  48 8B CB                        mov rcx, rbx
008997D4  FF 43 14                        inc dword ptr [rbx + 0x14]
008997D7  E8 94 0D E2 FF                  call 0x1406ba570
008997DC  48 8B F8                        mov rdi, rax
008997DF  48 85 C0                        test rax, rax
008997E2  75 1E                           jne 0x140899802
008997E4  8B 53 2C                        mov edx, dword ptr [rbx + 0x2c]
008997E7  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
008997EB  44 8B 43 28                     mov r8d, dword ptr [rbx + 0x28]
008997EF  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
008997F2  FF 43 18                        inc dword ptr [rbx + 0x18]
008997F5  E8 D6 12 E2 FF                  call 0x1406baad0
008997FA  48 8B F8                        mov rdi, rax
008997FD  48 85 C0                        test rax, rax
00899800  74 06                           je 0x140899808
00899802  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
00899806  89 07                           mov dword ptr [rdi], eax
00899808  48 85 FF                        test rdi, rdi
0089980B  0F 84 60 06 00 00               je 0x140899e71
00899811  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00899816  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
0089981A  44 0F B6 7D 67                  movzx r15d, byte ptr [rbp + 0x67]
0089981F  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00899823  41 0F B6 D7                     movzx edx, r15b
00899827  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0089982C  33 C9                           xor ecx, ecx
0089982E  E8 FD 20 00 00                  call 0x14089b930
00899833  44 8B F0                        mov r14d, eax
00899836  85 C0                           test eax, eax
00899838  0F 88 69 04 00 00               js 0x140899ca7
0089983E  8B 0F                           mov ecx, dword ptr [rdi]
00899840  41 85 4D 48                     test dword ptr [r13 + 0x48], ecx
00899844  0F 85 3C 06 00 00               jne 0x140899e86
0089984A  F6 C1 10                        test cl, 0x10
0089984D  0F 85 9C 02 00 00               jne 0x140899aef
00899853  41 8B 45 68                     mov eax, dword ptr [r13 + 0x68]
00899857  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
0089985B  41 8B 4D 6C                     mov ecx, dword ptr [r13 + 0x6c]
0089985F  4D 8B C5                        mov r8, r13
00899862  89 47 14                        mov dword ptr [rdi + 0x14], eax
00899865  41 0F B6 D7                     movzx edx, r15b
00899869  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0089986E  89 4F 18                        mov dword ptr [rdi + 0x18], ecx
00899871  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00899876  48 8B CF                        mov rcx, rdi
00899879  48 8D 45 9F                     lea rax, [rbp - 0x61]
0089987D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00899882  C7 44 24 20 D8 00 00 00         mov dword ptr [rsp + 0x20], 0xd8
0089988A  E8 61 07 00 00                  call 0x140899ff0
0089988F  44 8B F0                        mov r14d, eax
00899892  85 C0                           test eax, eax
00899894  0F 89 DA 04 00 00               jns 0x140899d74
0089989A  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0089989E  48 8D 1D AB 8F 2E 00            lea rbx, [rip + 0x2e8fab]
008998A5  48 85 C9                        test rcx, rcx
008998A8  74 38                           je 0x1408998e2
008998AA  B8 F8 00 00 00                  mov eax, 0xf8
008998AF  66 39 45 91                     cmp word ptr [rbp - 0x6f], ax
008998B3  0F 85 2C 04 00 00               jne 0x140899ce5
008998B9  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008998C2  48 8B 8A 50 08 00 00            mov rcx, qword ptr [rdx + 0x850]
008998C9  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008998CC  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008998D0  66 39 01                        cmp word ptr [rcx], ax
008998D3  0F 83 06 05 00 00               jae 0x140899ddf
008998D9  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
008998DD  E8 CE 0C E2 FF                  call 0x1406ba5b0
008998E2  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
008998E6  48 85 C9                        test rcx, rcx
008998E9  74 15                           je 0x140899900
008998EB  80 7F 10 01                     cmp byte ptr [rdi + 0x10], 1
008998EF  77 07                           ja 0x1408998f8
008998F1  33 D2                           xor edx, edx
008998F3  E8 78 8F 2E 00                  call 0x140b82870
008998F8  48 C7 47 20 00 00 00 00         mov qword ptr [rdi + 0x20], 0
00899900  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00899909  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
00899910  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00899913  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00899917  66 39 01                        cmp word ptr [rcx], ax
0089991A  0F 83 88 04 00 00               jae 0x140899da8
00899920  48 8B D7                        mov rdx, rdi
00899923  E8 88 0C E2 FF                  call 0x1406ba5b0
00899928  33 DB                           xor ebx, ebx
0089992A  45 85 F6                        test r14d, r14d
0089992D  0F 88 9C 03 00 00               js 0x140899ccf
00899933  33 D2                           xor edx, edx
00899935  41 B8 D8 00 00 00               mov r8d, 0xd8
0089993B  48 8B CB                        mov rcx, rbx
0089993E  E8 FD D2 E2 FF                  call 0x1406c6c40
00899943  80 7D 7F 00                     cmp byte ptr [rbp + 0x7f], 0
00899947  0F 85 E4 01 00 00               jne 0x140899b31
0089994D  8B 86 98 00 00 00               mov eax, dword ptr [rsi + 0x98]
00899953  44 8B AD 87 00 00 00            mov r13d, dword ptr [rbp + 0x87]
0089995A  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
0089995F  A8 47                           test al, 0x47
00899961  0F 85 26 02 00 00               jne 0x140899b8d
00899967  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0089996B  E8 C0 A1 BA FF                  call 0x140443b30
00899970  84 C0                           test al, al
00899972  0F 84 15 02 00 00               je 0x140899b8d
00899978  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
0089997C  48 85 C9                        test rcx, rcx
0089997F  0F 85 09 04 00 00               jne 0x140899d8e
00899985  45 85 F6                        test r14d, r14d
00899988  78 5F                           js 0x1408999e9
0089998A  45 84 FF                        test r15b, r15b
0089998D  74 5A                           je 0x1408999e9
0089998F  8B 86 98 00 00 00               mov eax, dword ptr [rsi + 0x98]
00899995  A8 20                           test al, 0x20
00899997  74 26                           je 0x1408999bf
00899999  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
0089999D  F7 41 30 00 00 04 00            test dword ptr [rcx + 0x30], 0x40000
008999A4  0F 84 47 03 00 00               je 0x140899cf1
008999AA  4C 8B CB                        mov r9, rbx
008999AD  45 8B C5                        mov r8d, r13d
008999B0  48 8B D6                        mov rdx, rsi
008999B3  E8 68 EB FF FF                  call 0x140898520
008999B8  44 8B F0                        mov r14d, eax
008999BB  85 C0                           test eax, eax
008999BD  78 2A                           js 0x1408999e9
008999BF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008999C8  F7 40 74 00 04 00 00            test dword ptr [rax + 0x74], 0x400
008999CF  75 18                           jne 0x1408999e9
008999D1  F7 46 40 00 00 02 00            test dword ptr [rsi + 0x40], 0x20000
008999D8  74 0F                           je 0x1408999e9
008999DA  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
008999DE  48 8B CB                        mov rcx, rbx
008999E1  E8 4E D7 BB FF                  call 0x140457134
008999E6  44 8B F0                        mov r14d, eax
008999E9  49 89 1C 24                     mov qword ptr [r12], rbx
008999ED  80 BE 8A 00 00 00 00            cmp byte ptr [rsi + 0x8a], 0
008999F4  0F 85 8E 00 00 00               jne 0x140899a88
008999FA  80 BE 89 00 00 00 00            cmp byte ptr [rsi + 0x89], 0
00899A01  0F 85 81 00 00 00               jne 0x140899a88
00899A07  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
00899A0A  A8 30                           test al, 0x30
00899A0C  74 16                           je 0x140899a24
00899A0E  8B 4B 50                        mov ecx, dword ptr [rbx + 0x50]
00899A11  83 C9 02                        or ecx, 2
00899A14  89 4B 50                        mov dword ptr [rbx + 0x50], ecx
00899A17  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
00899A1A  A8 10                           test al, 0x10
00899A1C  74 06                           je 0x140899a24
00899A1E  83 C9 04                        or ecx, 4
00899A21  89 4B 50                        mov dword ptr [rbx + 0x50], ecx
00899A24  8B 43 50                        mov eax, dword ptr [rbx + 0x50]
00899A27  A8 02                           test al, 2
00899A29  74 1C                           je 0x140899a47
00899A2B  45 33 C0                        xor r8d, r8d
00899A2E  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
00899A35  41 8D 50 01                     lea edx, [r8 + 1]
00899A39  E8 D2 42 B7 FF                  call 0x14040dd10
00899A3E  33 C0                           xor eax, eax
00899A40  89 43 70                        mov dword ptr [rbx + 0x70], eax
00899A43  48 89 43 68                     mov qword ptr [rbx + 0x68], rax
00899A47  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
00899A4A  A8 08                           test al, 8
00899A4C  74 04                           je 0x140899a52
00899A4E  83 4B 50 08                     or dword ptr [rbx + 0x50], 8
00899A52  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
00899A55  A8 02                           test al, 2
00899A57  74 04                           je 0x140899a5d
00899A59  83 4B 50 10                     or dword ptr [rbx + 0x50], 0x10
00899A5D  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
00899A60  A8 04                           test al, 4
00899A62  74 04                           je 0x140899a68
00899A64  83 4B 50 20                     or dword ptr [rbx + 0x50], 0x20
00899A68  F7 46 40 00 08 00 00            test dword ptr [rsi + 0x40], 0x800
00899A6F  74 07                           je 0x140899a78
00899A71  81 4B 50 00 00 10 00            or dword ptr [rbx + 0x50], 0x100000
00899A78  F7 46 40 00 00 02 00            test dword ptr [rsi + 0x40], 0x20000
00899A7F  74 07                           je 0x140899a88
00899A81  81 4B 50 00 00 00 02            or dword ptr [rbx + 0x50], 0x2000000
00899A88  F6 45 87 40                     test byte ptr [rbp - 0x79], 0x40
00899A8C  75 07                           jne 0x140899a95
00899A8E  81 4B 50 00 00 02 00            or dword ptr [rbx + 0x50], 0x20000
00899A95  C7 03 05 00 D8 00               mov dword ptr [rbx], 0xd80005
00899A9B  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00899A9F  48 89 43 40                     mov qword ptr [rbx + 0x40], rax
00899AA3  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
00899AA7  48 89 43 08                     mov qword ptr [rbx + 8], rax
00899AAB  48 C7 83 B8 00 00 00 00 00 00 00  mov qword ptr [rbx + 0xb8], 0
00899AB6  48 81 C3 C0 00 00 00            add rbx, 0xc0
00899ABD  48 89 5B 08                     mov qword ptr [rbx + 8], rbx
00899AC1  48 89 1B                        mov qword ptr [rbx], rbx
00899AC4  41 8B C6                        mov eax, r14d
00899AC7  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
00899ACB  48 33 CC                        xor rcx, rsp
00899ACE  E8 6D 2B E1 FF                  call 0x1406ac640
00899AD3  48 8B 9C 24 18 01 00 00         mov rbx, qword ptr [rsp + 0x118]
00899ADB  48 81 C4 D0 00 00 00            add rsp, 0xd0
00899AE2  41 5F                           pop r15
00899AE4  41 5E                           pop r14
00899AE6  41 5D                           pop r13
00899AE8  41 5C                           pop r12
00899AEA  5F                              pop rdi
00899AEB  5E                              pop rsi
00899AEC  5D                              pop rbp
00899AED  C3                              ret
00899AEE  CC                              int3
00899AEF  48 8B 1D DA 00 74 00            mov rbx, qword ptr [rip + 0x7400da]
00899AF6  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00899AFA  0F 57 C0                        xorps xmm0, xmm0
00899AFD  0F 11 45 AF                     movups xmmword ptr [rbp - 0x51], xmm0
00899B01  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00899B05  E8 16 1D FD FF                  call 0x14086b820
00899B0A  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00899B0E  C7 45 E7 01 00 00 00            mov dword ptr [rbp - 0x19], 1
00899B15  C7 45 EB 01 00 00 00            mov dword ptr [rbp - 0x15], 1
00899B1C  48 89 5D EF                     mov qword ptr [rbp - 0x11], rbx
00899B20  C7 45 F7 00 00 00 00            mov dword ptr [rbp - 9], 0
00899B27  E8 E4 1B FD FF                  call 0x14086b710
00899B2C  E9 22 FD FF FF                  jmp 0x140899853
00899B31  49 8B 04 24                     mov rax, qword ptr [r12]
00899B35  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00899B39  48 89 4B 18                     mov qword ptr [rbx + 0x18], rcx
00899B3D  49 8B 04 24                     mov rax, qword ptr [r12]
00899B41  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00899B45  48 89 4B 20                     mov qword ptr [rbx + 0x20], rcx
00899B49  49 8B 04 24                     mov rax, qword ptr [r12]
00899B4D  0F B7 48 58                     movzx ecx, word ptr [rax + 0x58]
00899B51  66 89 4B 58                     mov word ptr [rbx + 0x58], cx
00899B55  49 8B 04 24                     mov rax, qword ptr [r12]
00899B59  0F B7 48 5A                     movzx ecx, word ptr [rax + 0x5a]
00899B5D  66 89 4B 5A                     mov word ptr [rbx + 0x5a], cx
00899B61  49 8B 04 24                     mov rax, qword ptr [r12]
00899B65  48 8B 48 60                     mov rcx, qword ptr [rax + 0x60]
00899B69  48 89 4B 60                     mov qword ptr [rbx + 0x60], rcx
00899B6D  49 8B 04 24                     mov rax, qword ptr [r12]
00899B71  48 8B 88 D0 00 00 00            mov rcx, qword ptr [rax + 0xd0]
00899B78  48 85 C9                        test rcx, rcx
00899B7B  0F 84 68 FE FF FF               je 0x1408999e9
00899B81  48 89 8B D0 00 00 00            mov qword ptr [rbx + 0xd0], rcx
00899B88  E9 5C FE FF FF                  jmp 0x1408999e9
00899B8D  8B 86 98 00 00 00               mov eax, dword ptr [rsi + 0x98]
00899B93  A8 02                           test al, 2
00899B95  0F 85 84 01 00 00               jne 0x140899d1f
00899B9B  8B 86 98 00 00 00               mov eax, dword ptr [rsi + 0x98]
00899BA1  A8 01                           test al, 1
00899BA3  74 44                           je 0x140899be9
00899BA5  33 C0                           xor eax, eax
00899BA7  BA 01 00 00 00                  mov edx, 1
00899BAC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00899BB1  41 B1 01                        mov r9b, 1
00899BB4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00899BB9  48 8B CB                        mov rcx, rbx
00899BBC  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00899BC1  44 8D 42 1F                     lea r8d, [rdx + 0x1f]
00899BC5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00899BCA  E8 B1 52 B9 FF                  call 0x14042ee80
00899BCF  44 8B F0                        mov r14d, eax
00899BD2  85 C0                           test eax, eax
00899BD4  0F 88 0F FE FF FF               js 0x1408999e9
00899BDA  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00899BDF  48 8B 8E B0 00 00 00            mov rcx, qword ptr [rsi + 0xb0]
00899BE6  48 89 08                        mov qword ptr [rax], rcx
00899BE9  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00899BED  4C 8B CB                        mov r9, rbx
00899BF0  45 8B C5                        mov r8d, r13d
00899BF3  48 8B D6                        mov rdx, rsi
00899BF6  E8 81 66 18 00                  call 0x140a2027c
00899BFB  44 8B F0                        mov r14d, eax
00899BFE  85 C0                           test eax, eax
00899C00  0F 88 E3 FD FF FF               js 0x1408999e9
00899C06  8B 86 98 00 00 00               mov eax, dword ptr [rsi + 0x98]
00899C0C  A8 40                           test al, 0x40
00899C0E  0F 84 28 01 00 00               je 0x140899d3c
00899C14  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
00899C18  45 33 F6                        xor r14d, r14d
00899C1B  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
00899C1F  48 85 D2                        test rdx, rdx
00899C22  0F 85 EF 01 00 00               jne 0x140899e17
00899C28  48 8B CF                        mov rcx, rdi
00899C2B  E8 00 9F BA FF                  call 0x140443b30
00899C30  84 C0                           test al, al
00899C32  0F 85 4D FD FF FF               jne 0x140899985
00899C38  48 8B CF                        mov rcx, rdi
00899C3B  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00899C40  E8 DB D9 BC FF                  call 0x140467620
00899C45  44 8B F0                        mov r14d, eax
00899C48  85 C0                           test eax, eax
00899C4A  0F 88 99 FD FF FF               js 0x1408999e9
00899C50  BA 07 00 00 00                  mov edx, 7
00899C55  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
00899C5E  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00899C63  41 B1 01                        mov r9b, 1
00899C66  48 8B CB                        mov rcx, rbx
00899C69  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00899C6E  44 8D 42 09                     lea r8d, [rdx + 9]
00899C72  E8 09 52 B9 FF                  call 0x14042ee80
00899C77  44 8B F0                        mov r14d, eax
00899C7A  48 8B CF                        mov rcx, rdi
00899C7D  85 C0                           test eax, eax
00899C7F  0F 88 45 02 00 00               js 0x140899eca
00899C85  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00899C8A  BA 49 6F 53 70                  mov edx, 0x70536f49
00899C8F  C7 00 10 00 00 00               mov dword ptr [rax], 0x10
00899C95  48 89 78 08                     mov qword ptr [rax + 8], rdi
00899C99  83 48 04 01                     or dword ptr [rax + 4], 1
00899C9D  E8 6E 6A 97 FF                  call 0x140210710
00899CA2  E9 DE FC FF FF                  jmp 0x140899985
00899CA7  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00899CB0  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
00899CB7  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00899CBA  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00899CBE  66 39 01                        cmp word ptr [rcx], ax
00899CC1  0F 83 70 01 00 00               jae 0x140899e37
00899CC7  48 8B D7                        mov rdx, rdi
00899CCA  E8 E1 08 E2 FF                  call 0x1406ba5b0
00899CCF  45 33 FF                        xor r15d, r15d
00899CD2  80 7D 7F 00                     cmp byte ptr [rbp + 0x7f], 0
00899CD6  0F 85 E8 FD FF FF               jne 0x140899ac4
00899CDC  4D 89 3C 24                     mov qword ptr [r12], r15
00899CE0  E9 DF FD FF FF                  jmp 0x140899ac4
00899CE5  33 D2                           xor edx, edx
00899CE7  E8 84 8B 2E 00                  call 0x140b82870
00899CEC  E9 F1 FB FF FF                  jmp 0x1408998e2
00899CF1  8B 41 48                        mov eax, dword ptr [rcx + 0x48]
00899CF4  83 F8 08                        cmp eax, 8
00899CF7  0F 84 AD FC FF FF               je 0x1408999aa
00899CFD  83 F8 35                        cmp eax, 0x35
00899D00  0F 87 B9 FC FF FF               ja 0x1408999bf
00899D06  48 BA 08 00 10 00 01 00 20 00   movabs rdx, 0x20000100100008
00899D10  48 0F A3 C2                     bt rdx, rax
00899D14  0F 83 A5 FC FF FF               jae 0x1408999bf
00899D1A  E9 8B FC FF FF                  jmp 0x1408999aa
00899D1F  BA 01 00 00 00                  mov edx, 1
00899D24  48 8B CB                        mov rcx, rbx
00899D27  E8 E4 39 BA FF                  call 0x14043d710
00899D2C  44 8B F0                        mov r14d, eax
00899D2F  85 C0                           test eax, eax
00899D31  0F 89 64 FE FF FF               jns 0x140899b9b
00899D37  E9 AD FC FF FF                  jmp 0x1408999e9
00899D3C  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00899D40  E8 EB 9D BA FF                  call 0x140443b30
00899D45  84 C0                           test al, al
00899D47  0F 84 C7 FE FF FF               je 0x140899c14
00899D4D  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00899D51  48 85 C9                        test rcx, rcx
00899D54  0F 84 2B FC FF FF               je 0x140899985
00899D5A  E8 31 E7 B9 FF                  call 0x140438490
00899D5F  48 8B C8                        mov rcx, rax
00899D62  E8 C9 9D BA FF                  call 0x140443b30
00899D67  84 C0                           test al, al
00899D69  0F 84 A5 FE FF FF               je 0x140899c14
00899D6F  E9 11 FC FF FF                  jmp 0x140899985
00899D74  83 3D 95 B2 72 00 00            cmp dword ptr [rip + 0x72b295], 0
00899D7B  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
00899D7F  0F 85 20 01 00 00               jne 0x140899ea5
00899D85  48 83 C3 30                     add rbx, 0x30
00899D89  E9 A5 FB FF FF                  jmp 0x140899933
00899D8E  E8 FD E6 B9 FF                  call 0x140438490
00899D93  48 8B C8                        mov rcx, rax
00899D96  E8 95 9D BA FF                  call 0x140443b30
00899D9B  84 C0                           test al, al
00899D9D  0F 85 E2 FB FF FF               jne 0x140899985
00899DA3  E9 E5 FD FF FF                  jmp 0x140899b8d
00899DA8  FF 41 20                        inc dword ptr [rcx + 0x20]
00899DAB  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
00899DB2  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00899DB5  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00899DB9  66 39 01                        cmp word ptr [rcx], ax
00899DBC  0F 82 5E FB FF FF               jb 0x140899920
00899DC2  FF 41 20                        inc dword ptr [rcx + 0x20]
00899DC5  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00899DC9  48 8B CF                        mov rcx, rdi
00899DCC  48 3B C3                        cmp rax, rbx
00899DCF  0F 85 C6 00 00 00               jne 0x140899e9b
00899DD5  E8 76 8A 2E 00                  call 0x140b82850
00899DDA  E9 49 FB FF FF                  jmp 0x140899928
00899DDF  FF 41 20                        inc dword ptr [rcx + 0x20]
00899DE2  48 8B 8A 58 08 00 00            mov rcx, qword ptr [rdx + 0x858]
00899DE9  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00899DEC  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00899DF0  66 39 01                        cmp word ptr [rcx], ax
00899DF3  0F 82 E0 FA FF FF               jb 0x1408998d9
00899DF9  FF 41 20                        inc dword ptr [rcx + 0x20]
00899DFC  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00899E00  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00899E04  48 3B C3                        cmp rax, rbx
00899E07  0F 85 84 00 00 00               jne 0x140899e91
00899E0D  E8 3E 8A 2E 00                  call 0x140b82850
00899E12  E9 CB FA FF FF                  jmp 0x1408998e2
00899E17  48 8B CF                        mov rcx, rdi
00899E1A  E8 09 BA 98 FF                  call 0x140225828
00899E1F  84 C0                           test al, al
00899E21  0F 84 01 FE FF FF               je 0x140899c28
00899E27  48 8B CA                        mov rcx, rdx
00899E2A  E8 61 E6 B9 FF                  call 0x140438490
00899E2F  48 8B F8                        mov rdi, rax
00899E32  E9 F1 FD FF FF                  jmp 0x140899c28
00899E37  FF 41 20                        inc dword ptr [rcx + 0x20]
00899E3A  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
00899E41  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00899E44  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00899E48  66 39 01                        cmp word ptr [rcx], ax
00899E4B  0F 82 76 FE FF FF               jb 0x140899cc7
00899E51  FF 41 20                        inc dword ptr [rcx + 0x20]
00899E54  48 8D 1D F5 89 2E 00            lea rbx, [rip + 0x2e89f5]
00899E5B  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00899E5F  48 8B CF                        mov rcx, rdi
00899E62  48 3B C3                        cmp rax, rbx
00899E65  75 15                           jne 0x140899e7c
00899E67  E8 E4 89 2E 00                  call 0x140b82850
00899E6C  E9 5E FE FF FF                  jmp 0x140899ccf
00899E71  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
00899E77  E9 56 FE FF FF                  jmp 0x140899cd2
00899E7C  E8 4F 0C E2 FF                  call 0x1406baad0
00899E81  E9 49 FE FF FF                  jmp 0x140899ccf
00899E86  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00899E8C  E9 09 FA FF FF                  jmp 0x14089989a
00899E91  E8 3A 0C E2 FF                  call 0x1406baad0
00899E96  E9 47 FA FF FF                  jmp 0x1408998e2
00899E9B  E8 30 0C E2 FF                  call 0x1406baad0
00899EA0  E9 83 FA FF FF                  jmp 0x140899928
00899EA5  48 8B CB                        mov rcx, rbx
00899EA8  E8 3F 55 23 00                  call 0x140acf3ec
00899EAD  41 B8 01 00 00 00               mov r8d, 1
00899EB3  41 B9 44 66 6C 74               mov r9d, 0x746c6644
00899EB9  41 0F B6 D0                     movzx edx, r8b
00899EBD  48 8B CB                        mov rcx, rbx
00899EC0  E8 1F 6B 97 FF                  call 0x1402109e4
00899EC5  E9 BB FE FF FF                  jmp 0x140899d85
00899ECA  E8 D1 3F AF FF                  call 0x14038dea0
00899ECF  E9 15 FB FF FF                  jmp 0x1408999e9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopAllocRealFileObject(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, __int64 a6, __int64 a7, unsigned __int8 a8, unsigned int a9)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int16 v_stack_mAE;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int16 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p48;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 5705725)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r15 = 0;
    v_stack_mC0 = a7;
    v_stack_mC8 = 0;
    v_stack_mB8 = (unsigned int)((unsigned int)(a4));
    v_stack_m60 = a3;
    v_stack_m98 = a2;
    v_stack_m90 = 48;
    v_stack_m74 = 0;
    v_stack_m88 = 0;
    v_stack_m78 = (unsigned int)((unsigned int)(a4));
    v_stack_m80 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_mC8 = 1;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = 0;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a2, a3, a4);
    if (result != 0) goto loc_00899802;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120), a2, a3, a4);
    if (result != 0) goto loc_00899802;
    result = guard_dispatch_icall((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 36)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 44)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 40)), a4);
    if (result != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36);
        *(unsigned int *)(result) = (unsigned int)(result);
    }
    if (result == 0) goto loc_00899E71;
    v_stack_mE0 = 0;
    v_stack_mE8 = result;
    a1 = 0;
    result = ObpCaptureObjectCreateInformation(a1, a5, v_stack_m90, v_stack_mB0);
    if (sign_flag) goto loc_00899CA7;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525251) + 72)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result))))) != 0) goto loc_00899E86;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result)))) & (16)) != 0) goto loc_00899AEF;
loc_00899853:
    *(unsigned int *)(result + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525251) + 104)));
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7525251) + 108)));
    v_stack_mD8 = v_stack_mC8;
    v_stack_mE0 = v_stack_mA0;
    v_stack_mE8 = 216;
    result = ObpAllocateObject(result, a5, *(unsigned __int64 *)(v_rip + 7525251), v_stack_mB0);
    if (!sign_flag) goto loc_00899D74;
loc_0089989A:
    if (v_stack_mA8 == 0) goto loc_008998E2;
    if (v_stack_mAE != 248) goto loc_00899CE5;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128) + 16)))) goto loc_00899DDF;
loc_008998D9:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128), v_stack_mA8, *(unsigned __int64 *)(v_rip + 7525251), v_stack_mB0);
loc_008998E2:
    if (*(unsigned __int64 *)(result + 32) == 0) goto loc_00899900;
    if ((*(unsigned __int8 *)(result + 16)) <= 1) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 32), a2, *(unsigned __int64 *)(v_rip + 7525251), v_stack_mB0);
    }
    *(unsigned __int64 *)(result + 32) = 0;
loc_00899900:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_00899DA8;
loc_00899920:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), result, *(unsigned __int64 *)(v_rip + 7525251), v_stack_mB0);
loc_00899928:
    v_rbx = 0;
    if (sign_flag) goto loc_00899CCF;
loc_00899933:
    a2 = 0;
    result = memset(0, a2, 216, v_stack_mB0);
    if (a8 != 0) goto loc_00899B31;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 152)))) & (71)) != 0) goto loc_00899B8D;
    result = PsIsHostSilo(*(unsigned __int64 *)(v_stack_mC0 + 8), a2, 216, v_stack_mB0);
    if ((unsigned __int8)(result) == 0) goto loc_00899B8D;
    if (*(unsigned __int64 *)(a6 + 40) != 0) goto loc_00899D8E;
loc_00899985:
    if (sign_flag) goto loc_008999E9;
    if (a5 == 0) goto loc_008999E9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 152)))) & (32)) == 0) goto loc_008999BF;
    if (((*(unsigned int *)(v_stack_m98 + 48)) & (0x40000ULL)) == 0) goto loc_00899CF1;
loc_008999AA:
    result = IopRetrieveTransactionParameters(v_stack_m98, a6, (unsigned int)((unsigned int)((unsigned int)(a9))), 0);
    if (sign_flag) goto loc_008999E9;
loc_008999BF:
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x400ULL)) != 0) goto loc_008999E9;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_r14 = (unsigned int)((unsigned int)(result));
    if (((*(unsigned int *)(a6 + 64)) & (0x20000ULL)) != 0) {
        a2 = *(unsigned __int64 *)(a6 + 40);
        a1 = 0;
        result = IopCheckInitiatorHint(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a9))), 0);
        v_r14 = (unsigned int)(result);
    }
    *(unsigned __int64 *)(a1) = 0;
    if ((*(unsigned __int8 *)(a6 + 138)) != 0) goto loc_00899A88;
    if ((*(unsigned __int8 *)(a6 + 137)) != 0) goto loc_00899A88;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 64)))) & (48)) == 0) goto loc_00899A24;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 80))) | (2));
    *(unsigned int *)(v_rbx + 80) = (unsigned int)(a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 64)))) & (16)) != 0) {
        a1 = (unsigned int)((a1) | (4));
        *(unsigned int *)(v_rbx + 80) = (unsigned int)(a1);
    }
    result = (unsigned int)(*(unsigned int *)(v_rbx + 80));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 80)))) & (2)) != 0) {
        a3 = 0;
        a1 = v_rbx + 128;
        a2 = a3 + 1;
        result = KeInitializeEvent(a1, a2, a3, 0);
        result = 0;
        *(unsigned int *)(v_rbx + 112) = 0;
        *(unsigned __int64 *)(v_rbx + 104) = 0;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 64)))) & (8)) != 0) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 64)))) & (2)) != 0) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 64)))) & (4)) != 0) {
    }
    if (((*(unsigned int *)(a6 + 64)) & (0x800ULL)) != 0) {
    }
    if (((*(unsigned int *)(a6 + 64)) & (0x20000ULL)) != 0) {
    }
    if (((v_stack_mB8) & (64)) == 0) {
    }
    *(unsigned int *)(v_rbx) = 0xD80005ULL;
    *(unsigned __int64 *)(v_rbx + 64) = *(unsigned __int64 *)(a6 + 40);
    *(unsigned __int64 *)(v_rbx + 8) = v_stack_m60;
    *(unsigned __int64 *)(v_rbx + 184) = 0;
    v_rbx = (v_rbx) + (192);
    *(unsigned __int64 *)(v_rbx + 8) = v_rbx;
    *(unsigned __int64 *)(v_rbx) = v_rbx;
loc_00899AC4:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 0);
    v_rsp = (v_rsp) + (208);
    return result;
loc_00899AEF:
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m90, a2, a3, 0);
    v_stack_m58 = 1;
    v_stack_m54 = 1;
    v_stack_m50 = *(unsigned __int64 *)(v_rip + 7602394);
    v_stack_m48 = 0;
    result = SeReleaseSubjectContext(v_stack_m90, a2, a3, 0);
    goto loc_00899853;
loc_00899B31:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7602394) + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7602394) + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 7602394) + 88) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 88));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 7602394) + 90) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 90));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7602394) + 96) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 96);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 208) == 0) goto loc_008999E9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7602394) + 208) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 208);
    goto loc_008999E9;
loc_00899B8D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 152)))) & (2)) != 0) goto loc_00899D1F;
loc_00899B9B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 152)))) & (1)) == 0) goto loc_00899BE9;
    result = 0;
    v_stack_p28 = 0;
    v_stack_p48 = 0;
    v_stack_p20 = v_stack_p48;
    result = IopGetSetSpecificExtension(*(unsigned __int64 *)(v_rip + 7602394), 1, 1 + 31, 1);
    if (sign_flag) goto loc_008999E9;
    *(unsigned __int64 *)(v_stack_p48) = *(unsigned __int64 *)(a6 + 176);
loc_00899BE9:
    result = IopRetrieveTransactionParametersFromOpenPacket(v_stack_m98, a6, (unsigned int)((unsigned int)((unsigned int)(a9))), *(unsigned __int64 *)(v_rip + 7602394));
    if (sign_flag) goto loc_008999E9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6 + 152)))) & (64)) == 0) goto loc_00899D3C;
loc_00899C14:
    v_r14 = 0;
    if (*(unsigned __int64 *)(a6 + 40) != 0) goto loc_00899E17;
loc_00899C28:
    result = PsIsHostSilo(*(unsigned __int64 *)(v_stack_mC0 + 8), *(unsigned __int64 *)(a6 + 40), (unsigned int)((unsigned int)((unsigned int)(a9))), *(unsigned __int64 *)(v_rip + 7602394));
    if ((unsigned __int8)(result) != 0) goto loc_00899985;
    v_stack_p48 = 0;
    result = PsAcquireSiloHardReference(*(unsigned __int64 *)(v_stack_mC0 + 8), *(unsigned __int64 *)(a6 + 40), (unsigned int)((unsigned int)((unsigned int)(a9))), *(unsigned __int64 *)(v_rip + 7602394));
    if (sign_flag) goto loc_008999E9;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p48;
    result = IopGetSetSpecificExtension(*(unsigned __int64 *)(v_rip + 7602394), 7, 7 + 9, 1);
    if (sign_flag) goto loc_00899ECA;
    *(unsigned int *)(v_stack_p48) = 16;
    *(unsigned __int64 *)(v_stack_p48 + 8) = *(unsigned __int64 *)(v_stack_mC0 + 8);
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(v_stack_mC0 + 8), (unsigned int)(0x70536F49ULL), 7 + 9, 1);
    goto loc_00899985;
loc_00899CA7:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_00899E37;
loc_00899CC7:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), *(unsigned __int64 *)(v_stack_mC0 + 8), 7 + 9, 1);
loc_00899CCF:
    v_r15 = 0;
loc_00899CD2:
    if (a8 != 0) goto loc_00899AC4;
    *(unsigned __int64 *)(a1) = 0;
    goto loc_00899AC4;
loc_00899CE5:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a2, 7 + 9, 1);
    goto loc_008998E2;
loc_00899CF1:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 72)))) == 8) goto loc_008999AA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 72)))) > 53) goto loc_008999BF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 72)))) >= 53) goto loc_008999BF;
    goto loc_008999AA;
loc_00899D1F:
    result = IopSetFileObjectExtensionFlag(*(unsigned __int64 *)(v_rip + 7602394), 1, 7 + 9, 1);
    if (!sign_flag) goto loc_00899B9B;
    goto loc_008999E9;
loc_00899D3C:
    result = PsIsHostSilo(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC0 + 8) + 8), 1, 7 + 9, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00899C14;
    if (*(unsigned __int64 *)(a6 + 40) == 0) goto loc_00899985;
    result = IoGetSilo(*(unsigned __int64 *)(a6 + 40), 1, 7 + 9, 1);
    result = PsIsHostSilo(result, 1, 7 + 9, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00899C14;
    goto loc_00899985;
loc_00899D74:
    if ((*(unsigned int *)(v_rip + 7516821)) != 0) goto loc_00899EA5;
loc_00899D85:
    v_rbx = (v_stack_mA0) + (48);
    goto loc_00899933;
loc_00899D8E:
    result = IoGetSilo(result, 1, 7 + 9, 1);
    result = PsIsHostSilo(result, 1, 7 + 9, 1);
    if ((unsigned __int8)(result) != 0) goto loc_00899985;
    goto loc_00899B8D;
loc_00899DA8:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(1 + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(1 + 2120) + 16)))) goto loc_00899920;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 2120) + 56)) != v_rbx) goto loc_00899E9B;
    result = ExFreePool(*(unsigned __int64 *)(v_stack_mC0 + 8), 1, 7 + 9, 1);
    goto loc_00899928;
loc_00899DDF:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(1 + 2136))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(1 + 2136) + 16)))) goto loc_008998D9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 2136) + 56)) != v_rbx) goto loc_00899E91;
    result = ExFreePool(v_stack_mA8, 1, 7 + 9, 1);
    goto loc_008998E2;
loc_00899E17:
    result = PsIsServerSilo(*(unsigned __int64 *)(v_stack_mC0 + 8), 1, 7 + 9, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00899C28;
    result = IoGetSilo(1, 1, 7 + 9, 1);
    goto loc_00899C28;
loc_00899E37:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(1 + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(1 + 2120) + 16)))) goto loc_00899CC7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 2120) + 56)) != (v_rip + 3049973)) goto loc_00899E7C;
    result = ExFreePool(result, 1, 7 + 9, 1);
    goto loc_00899CCF;
loc_00899E71:
    goto loc_00899CD2;
loc_00899E7C:
    result = guard_dispatch_icall(result, 1, 7 + 9, 1);
    goto loc_00899CCF;
loc_00899E86:
    goto loc_0089989A;
loc_00899E91:
    result = guard_dispatch_icall(result, 1, 7 + 9, 1);
    goto loc_008998E2;
loc_00899E9B:
    result = guard_dispatch_icall(result, 1, 7 + 9, 1);
    goto loc_00899928;
loc_00899EA5:
    result = ObpRegisterObject(v_rip + 3049973, 1, 7 + 9, 1);
    result = ObpPushStackInfo(v_rip + 3049973, 1, 1, (unsigned int)(0x746C6644ULL));
    goto loc_00899D85;
loc_00899ECA:
    result = PsReleaseSiloHardReference(v_rip + 3049973, 1, 1, (unsigned int)(0x746C6644ULL));
    goto loc_008999E9;
}
```

## 5. (Beta) C Style

```c
int64_t IopAllocRealFileObject(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5, void *Arg6, int64_t Arg7, uint8_t Arg8, uint32_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint16_t v_stack_mAE;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint16_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p48;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x570FFD)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r15 = 0;
    v_stack_mC0 = Arg7;
    v_stack_mC8 = 0;
    v_stack_mB8 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m60 = Arg3;
    v_stack_m98 = Arg2;
    v_stack_m90 = 48;
    v_stack_m74 = 0;
    v_stack_m88 = 0;
    v_stack_m78 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m80 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_mC8 = 1;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = 0;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00899802;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00899802;
    result = guard_dispatch_icall((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x24)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x2C)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x28)), Arg4);
    if (result != 0) {
        result = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24);
        *(uint32_t *)(result) = (uint32_t)(result);
    }
    if (result == 0) goto loc_00899E71;
    v_stack_mE0 = 0;
    v_stack_mE8 = result;
    Arg1 = 0;
    result = ObpCaptureObjectCreateInformation(Arg1, Arg5, v_stack_m90, v_stack_mB0);
    if (sign_flag) goto loc_00899CA7;
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D383) + 0x48)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result))))) != 0) goto loc_00899E86;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result)))) & (16)) != 0) goto loc_00899AEF;
loc_00899853:
    *(uint32_t *)(result + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D383) + 0x68)));
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x72D383) + 0x6C)));
    v_stack_mD8 = v_stack_mC8;
    v_stack_mE0 = v_stack_mA0;
    v_stack_mE8 = 216;
    result = ObpAllocateObject(result, Arg5, *(uint64_t *)(v_rip + 0x72D383), v_stack_mB0);
    if (!sign_flag) goto loc_00899D74;
loc_0089989A:
    if (v_stack_mA8 == 0) goto loc_008998E2;
    if (v_stack_mAE != 248) goto loc_00899CE5;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850) + 0x10)))) goto loc_00899DDF;
loc_008998D9:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850), v_stack_mA8, *(uint64_t *)(v_rip + 0x72D383), v_stack_mB0);
loc_008998E2:
    if (*(uint64_t *)(result + 0x20) == 0) goto loc_00899900;
    if ((*(uint8_t *)(result + 0x10)) <= 1) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x20), Arg2, *(uint64_t *)(v_rip + 0x72D383), v_stack_mB0);
    }
    *(uint64_t *)(result + 0x20) = 0;
loc_00899900:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_00899DA8;
loc_00899920:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), result, *(uint64_t *)(v_rip + 0x72D383), v_stack_mB0);
loc_00899928:
    local_rbx = 0;
    if (sign_flag) goto loc_00899CCF;
loc_00899933:
    Arg2 = 0;
    result = memset(0, Arg2, 216, v_stack_mB0);
    if (Arg8 != 0) goto loc_00899B31;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x98)))) & (71)) != 0) goto loc_00899B8D;
    result = PsIsHostSilo(*(uint64_t *)(v_stack_mC0 + 0x8), Arg2, 216, v_stack_mB0);
    if ((uint8_t)(result) == 0) goto loc_00899B8D;
    if (*(uint64_t *)(arg6 + 0x28) != 0) goto loc_00899D8E;
loc_00899985:
    if (sign_flag) goto loc_008999E9;
    if (Arg5 == 0) goto loc_008999E9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x98)))) & (32)) == 0) goto loc_008999BF;
    if (((*(uint32_t *)(v_stack_m98 + 0x30)) & (0x40000ULL)) == 0) goto loc_00899CF1;
loc_008999AA:
    result = IopRetrieveTransactionParameters(v_stack_m98, Arg6, (uint32_t)((uint32_t)((uint32_t)(Arg9))), 0);
    if (sign_flag) goto loc_008999E9;
loc_008999BF:
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x400ULL)) != 0) goto loc_008999E9;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    local_r14 = (uint32_t)((uint32_t)(result));
    if (((*(uint32_t *)(arg6 + 0x40)) & (0x20000ULL)) != 0) {
        Arg2 = *(uint64_t *)(arg6 + 0x28);
        Arg1 = 0;
        result = IopCheckInitiatorHint(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg9))), 0);
        local_r14 = (uint32_t)(result);
    }
    *(uint64_t *)(arg1) = 0;
    if ((*(uint8_t *)(arg6 + 0x8A)) != 0) goto loc_00899A88;
    if ((*(uint8_t *)(arg6 + 0x89)) != 0) goto loc_00899A88;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x40)))) & (48)) == 0) goto loc_00899A24;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x50))) | (2));
    *(uint32_t *)(local_rbx + 0x50) = (uint32_t)(Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x40)))) & (16)) != 0) {
        Arg1 = (uint32_t)((Arg1) | (4));
        *(uint32_t *)(local_rbx + 0x50) = (uint32_t)(Arg1);
    }
    result = (uint32_t)(*(uint32_t *)(local_rbx + 0x50));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x50)))) & (2)) != 0) {
        Arg3 = 0;
        Arg1 = local_rbx + 128;
        Arg2 = Arg3 + 1;
        result = KeInitializeEvent(Arg1, Arg2, Arg3, 0);
        result = 0;
        *(uint32_t *)(local_rbx + 0x70) = 0;
        *(uint64_t *)(local_rbx + 0x68) = 0;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x40)))) & (8)) != 0) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x40)))) & (2)) != 0) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x40)))) & (4)) != 0) {
    }
    if (((*(uint32_t *)(arg6 + 0x40)) & (0x800ULL)) != 0) {
    }
    if (((*(uint32_t *)(arg6 + 0x40)) & (0x20000ULL)) != 0) {
    }
    if (((v_stack_mB8) & (64)) == 0) {
    }
    *(uint32_t *)(local_rbx) = 0xD80005ULL;
    *(uint64_t *)(local_rbx + 0x40) = *(uint64_t *)(arg6 + 0x28);
    *(uint64_t *)(local_rbx + 0x8) = v_stack_m60;
    *(uint64_t *)(local_rbx + 0xB8) = 0;
    local_rbx = (local_rbx) + (192);
    *(uint64_t *)(local_rbx + 0x8) = local_rbx;
    *(uint64_t *)(local_rbx) = local_rbx;
loc_00899AC4:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, 0);
    local_rsp = (local_rsp) + (208);
    return result;
loc_00899AEF:
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m90, Arg2, Arg3, 0);
    v_stack_m58 = 1;
    v_stack_m54 = 1;
    v_stack_m50 = *(uint64_t *)(v_rip + 0x7400DA);
    v_stack_m48 = 0;
    result = SeReleaseSubjectContext(v_stack_m90, Arg2, Arg3, 0);
    goto loc_00899853;
loc_00899B31:
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x7400DA) + 0x18) = *(uint64_t *)(*(uint64_t *)(arg1) + 0x18);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x7400DA) + 0x20) = *(uint64_t *)(*(uint64_t *)(arg1) + 0x20);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x7400DA) + 0x58) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1) + 0x58));
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x7400DA) + 0x5A) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1) + 0x5A));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x7400DA) + 0x60) = *(uint64_t *)(*(uint64_t *)(arg1) + 0x60);
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0xD0) == 0) goto loc_008999E9;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x7400DA) + 0xD0) = *(uint64_t *)(*(uint64_t *)(arg1) + 0xD0);
    goto loc_008999E9;
loc_00899B8D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x98)))) & (2)) != 0) goto loc_00899D1F;
loc_00899B9B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x98)))) & (1)) == 0) goto loc_00899BE9;
    result = 0;
    v_stack_p28 = 0;
    v_stack_p48 = 0;
    v_stack_p20 = v_stack_p48;
    result = IopGetSetSpecificExtension(*(uint64_t *)(v_rip + 0x7400DA), 1, 1 + 31, 1);
    if (sign_flag) goto loc_008999E9;
    *(uint64_t *)(v_stack_p48) = *(uint64_t *)(arg6 + 0xB0);
loc_00899BE9:
    result = IopRetrieveTransactionParametersFromOpenPacket(v_stack_m98, Arg6, (uint32_t)((uint32_t)((uint32_t)(Arg9))), *(uint64_t *)(v_rip + 0x7400DA));
    if (sign_flag) goto loc_008999E9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6 + 0x98)))) & (64)) == 0) goto loc_00899D3C;
loc_00899C14:
    local_r14 = 0;
    if (*(uint64_t *)(arg6 + 0x28) != 0) goto loc_00899E17;
loc_00899C28:
    result = PsIsHostSilo(*(uint64_t *)(v_stack_mC0 + 0x8), *(uint64_t *)(arg6 + 0x28), (uint32_t)((uint32_t)((uint32_t)(Arg9))), *(uint64_t *)(v_rip + 0x7400DA));
    if ((uint8_t)(result) != 0) goto loc_00899985;
    v_stack_p48 = 0;
    result = PsAcquireSiloHardReference(*(uint64_t *)(v_stack_mC0 + 0x8), *(uint64_t *)(arg6 + 0x28), (uint32_t)((uint32_t)((uint32_t)(Arg9))), *(uint64_t *)(v_rip + 0x7400DA));
    if (sign_flag) goto loc_008999E9;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p48;
    result = IopGetSetSpecificExtension(*(uint64_t *)(v_rip + 0x7400DA), 7, 7 + 9, 1);
    if (sign_flag) goto loc_00899ECA;
    *(uint32_t *)(v_stack_p48) = 16;
    *(uint64_t *)(v_stack_p48 + 0x8) = *(uint64_t *)(v_stack_mC0 + 0x8);
    result = ObfReferenceObjectWithTag(*(uint64_t *)(v_stack_mC0 + 0x8), (uint32_t)(0x70536F49ULL), 7 + 9, 1);
    goto loc_00899985;
loc_00899CA7:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_00899E37;
loc_00899CC7:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), *(uint64_t *)(v_stack_mC0 + 0x8), 7 + 9, 1);
loc_00899CCF:
    local_r15 = 0;
loc_00899CD2:
    if (Arg8 != 0) goto loc_00899AC4;
    *(uint64_t *)(arg1) = 0;
    goto loc_00899AC4;
loc_00899CE5:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg2, 7 + 9, 1);
    goto loc_008998E2;
loc_00899CF1:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x48)))) == 8) goto loc_008999AA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x48)))) > 53) goto loc_008999BF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x48)))) >= 53) goto loc_008999BF;
    goto loc_008999AA;
loc_00899D1F:
    result = IopSetFileObjectExtensionFlag(*(uint64_t *)(v_rip + 0x7400DA), 1, 7 + 9, 1);
    if (!sign_flag) goto loc_00899B9B;
    goto loc_008999E9;
loc_00899D3C:
    result = PsIsHostSilo(*(uint64_t *)(*(uint64_t *)(v_stack_mC0 + 0x8) + 0x8), 1, 7 + 9, 1);
    if ((uint8_t)(result) == 0) goto loc_00899C14;
    if (*(uint64_t *)(arg6 + 0x28) == 0) goto loc_00899985;
    result = IoGetSilo(*(uint64_t *)(arg6 + 0x28), 1, 7 + 9, 1);
    result = PsIsHostSilo(result, 1, 7 + 9, 1);
    if ((uint8_t)(result) == 0) goto loc_00899C14;
    goto loc_00899985;
loc_00899D74:
    if ((*(uint32_t *)(v_rip + 0x72B295)) != 0) goto loc_00899EA5;
loc_00899D85:
    local_rbx = (v_stack_mA0) + (48);
    goto loc_00899933;
loc_00899D8E:
    result = IoGetSilo(result, 1, 7 + 9, 1);
    result = PsIsHostSilo(result, 1, 7 + 9, 1);
    if ((uint8_t)(result) != 0) goto loc_00899985;
    goto loc_00899B8D;
loc_00899DA8:
    if ((*(uint16_t *)(*(uint64_t *)(1 + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(1 + 0x848) + 0x10)))) goto loc_00899920;
    if ((*(uint64_t *)(*(uint64_t *)(1 + 0x848) + 0x38)) != local_rbx) goto loc_00899E9B;
    result = ExFreePool(*(uint64_t *)(v_stack_mC0 + 0x8), 1, 7 + 9, 1);
    goto loc_00899928;
loc_00899DDF:
    if ((*(uint16_t *)(*(uint64_t *)(1 + 0x858))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(1 + 0x858) + 0x10)))) goto loc_008998D9;
    if ((*(uint64_t *)(*(uint64_t *)(1 + 0x858) + 0x38)) != local_rbx) goto loc_00899E91;
    result = ExFreePool(v_stack_mA8, 1, 7 + 9, 1);
    goto loc_008998E2;
loc_00899E17:
    result = PsIsServerSilo(*(uint64_t *)(v_stack_mC0 + 0x8), 1, 7 + 9, 1);
    if ((uint8_t)(result) == 0) goto loc_00899C28;
    result = IoGetSilo(1, 1, 7 + 9, 1);
    goto loc_00899C28;
loc_00899E37:
    if ((*(uint16_t *)(*(uint64_t *)(1 + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(1 + 0x848) + 0x10)))) goto loc_00899CC7;
    if ((*(uint64_t *)(*(uint64_t *)(1 + 0x848) + 0x38)) != (v_rip + 3049973)) goto loc_00899E7C;
    result = ExFreePool(result, 1, 7 + 9, 1);
    goto loc_00899CCF;
loc_00899E71:
    goto loc_00899CD2;
loc_00899E7C:
    result = guard_dispatch_icall(result, 1, 7 + 9, 1);
    goto loc_00899CCF;
loc_00899E86:
    goto loc_0089989A;
loc_00899E91:
    result = guard_dispatch_icall(result, 1, 7 + 9, 1);
    goto loc_008998E2;
loc_00899E9B:
    result = guard_dispatch_icall(result, 1, 7 + 9, 1);
    goto loc_00899928;
loc_00899EA5:
    result = ObpRegisterObject(v_rip + 3049973, 1, 7 + 9, 1);
    result = ObpPushStackInfo(v_rip + 3049973, 1, 1, (uint32_t)(0x746C6644ULL));
    goto loc_00899D85;
loc_00899ECA:
    result = PsReleaseSiloHardReference(v_rip + 3049973, 1, 1, (uint32_t)(0x746C6644ULL));
    goto loc_008999E9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg6` | `+ 0x28` | `64` | `R` |
| `Arg6` | `+ 0x40` | `32` | `R` |
| `Arg6` | `+ 0x89` | `8` | `R` |
| `Arg6` | `+ 0x8A` | `8` | `R` |
| `Arg6` | `+ 0x98` | `32` | `R` |
| `Arg6` | `+ 0xB0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00899720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
