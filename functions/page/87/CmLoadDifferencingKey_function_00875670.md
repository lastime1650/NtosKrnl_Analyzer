# CmLoadDifferencingKey

- RVA: `0x00875670`–`0x00876304` (길이 `3,220` bytes)
- VA: `0x0000000140875670`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006C9C4`
- 디코드: `628`개 명령, `3,220/3,220` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **52**; 고유 호출 대상: **37**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00875752` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00875776` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00875785` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00875799` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008757D6` → [CmpInitializeParseContext](CmpInitializeParseContext_function_008767F0.md) (function, `0x008767F0`)
- `0x008757E6` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (function, `0x00BC9C6C`)
- `0x0087583A` → [CmCheckNoTxContext](CmCheckNoTxContext_function_00876A80.md) (function, `0x00876A80`)
- `0x008758AD` → [CmpNameFromAttributes](CmpNameFromAttributes_function_00876AC8.md) (function, `0x00876AC8`)
- `0x00875933` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (function, `0x00461190`)
- `0x0087595A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0087598E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00875A96` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00875A9C` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00875B46` → [CmConvertHandleToKernelHandle](CmConvertHandleToKernelHandle_function_00876DDC.md) (function, `0x00876DDC`)
- `0x00875B76` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00875BCF` → [CmpTraceHiveLoadStart](CmpTraceHiveLoadStart_function_00876F38.md) (function, `0x00876F38`)
- `0x00875C33` → [CmLoadAppKey](CmLoadAppKey_function_00876FFC.md) (function, `0x00876FFC`)
- `0x00875C47` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00875D06` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00875D1F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00875D31` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00875DC5` → [ObReferenceObjectByName](../8C/ObReferenceObjectByName_function_008C4A00.md) (function, `0x008C4A00`)
- `0x00875DDC` → [ObDeleteCapturedInsertInfo](ObDeleteCapturedInsertInfo_function_00876E90.md) (function, `0x00876E90`)
- `0x00875E20` → [ObOpenObjectByPointer](../8B/ObOpenObjectByPointer_function_008B7420.md) (function, `0x008B7420`)
- `0x00875E2A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00875EB9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00875ECB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00875EDD` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00875F0C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00875F20` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00875F2F` → [CmpCleanupParseContext](CmpCleanupParseContext_function_00876910.md) (function, `0x00876910`)
- `0x00875F3B` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (function, `0x00BC9CAC`)
- `0x00875F47` → [CmpTraceHiveLoadStop](CmpTraceHiveLoadStop_function_008769F0.md) (function, `0x008769F0`)
- `0x00875F54` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x00875F66` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00875F7F` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00875FB9` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008760A2` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x008760B9` → [CmReleaseLoadKeyContext](CmReleaseLoadKeyContext_function_00877C88.md) (function, `0x00877C88`)
- `0x008760E1` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (function, `0x004489E0`)
- `0x0087611B` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x00876192` → [CmLoadKey](CmLoadKey_function_008787CC.md) (function, `0x008787CC`)
- `0x008761CF` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x0087620C` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x00876219` → [CmpDereferenceKeyControlBlock](../85/CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x0087621E` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00876232` → [SeSinglePrivilegeCheck](SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00876249` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008762AE` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008762E3` → [CmReleaseLoadKeyContext](CmReleaseLoadKeyContext_function_00877C88.md) (function, `0x00877C88`)
- `0x008762F0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008762FA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [NtLoadKeyEx](NtLoadKeyEx_function_00875600.md) at `0x0087565F`
- [VrpLoadDifferencingHive](../93/VrpLoadDifferencingHive_function_00935F40.md) at `0x00936175`
- [NtLoadKey2](../AA/NtLoadKey2_function_00AA70D0.md) at `0x00AA7110`
- [NtLoadKey3](../AA/NtLoadKey3_function_00AACC70.md) at `0x00AACE15`
- [sub_00B4588A](../B4/Unknown_function_00B4588A.md) at `0x00B45DC3`

### Static image references
- `0x00875683` → RVA `0x00E0A740` (`.data`; read)
- `0x00875BB0` → RVA `0x00EEFB88` (`.data`; read)
- `0x00875DB3` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x0087622B` → RVA `0x00FD9AE0` (`PAGEDATA`; read)
- `0x00876288` → RVA `0x00FC6B80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **30**
  - `0x00875752` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00875776` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x00875785` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00875799` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008757E6` → [CmpAcquireHiveLoadUnloadRundown](../../pagecmrc/BC/CmpAcquireHiveLoadUnloadRundown_function_00BC9C6C.md) (`PAGE` → `PAGECMRC`)
  - `0x00875933` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (`PAGE` → `.text`)
  - `0x0087595A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0087598E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00875B76` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00875C47` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00875D1F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00875D31` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00875E2A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00875EB9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00875ECB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00875EDD` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00875F0C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00875F20` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00875F3B` → [CmpReleaseHiveLoadUnloadRundown](../../pagecmrc/BC/CmpReleaseHiveLoadUnloadRundown_function_00BC9CAC.md) (`PAGE` → `PAGECMRC`)
  - `0x00875F54` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x00875F66` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00875F7F` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008760E1` → [CmpFreePoolWithTag](../../text/44/CmpFreePoolWithTag_function_004489E0.md) (`PAGE` → `.text`)
  - `0x0087611B` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
  - `0x008761CF` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
  - `0x0087620C` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x0087621E` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00876249` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008762F0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008762FA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00875B0C` → [sub_00B17976](../B1/Unknown_function_00B17976.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00875670  40 53                           push rbx
00875672  56                              push rsi
00875673  57                              push rdi
00875674  41 54                           push r12
00875676  41 55                           push r13
00875678  41 56                           push r14
0087567A  41 57                           push r15
0087567C  48 81 EC 30 04 00 00            sub rsp, 0x430
00875683  48 8B 05 B6 50 59 00            mov rax, qword ptr [rip + 0x5950b6]
0087568A  48 33 C4                        xor rax, rsp
0087568D  48 89 84 24 20 04 00 00         mov qword ptr [rsp + 0x420], rax
00875695  45 8B F0                        mov r14d, r8d
00875698  48 89 94 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdx
008756A0  48 8B D9                        mov rbx, rcx
008756A3  48 8B 84 24 A8 04 00 00         mov rax, qword ptr [rsp + 0x4a8]
008756AB  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
008756B3  44 89 84 24 F8 00 00 00         mov dword ptr [rsp + 0xf8], r8d
008756BB  48 8B 84 24 90 04 00 00         mov rax, qword ptr [rsp + 0x490]
008756C3  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
008756CB  48 8B 84 24 98 04 00 00         mov rax, qword ptr [rsp + 0x498]
008756D3  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008756D8  48 8B B4 24 B8 04 00 00         mov rsi, qword ptr [rsp + 0x4b8]
008756E0  48 89 B4 24 90 01 00 00         mov qword ptr [rsp + 0x190], rsi
008756E8  48 8B 84 24 C8 04 00 00         mov rax, qword ptr [rsp + 0x4c8]
008756F0  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
008756F8  0F 57 C0                        xorps xmm0, xmm0
008756FB  33 C0                           xor eax, eax
008756FD  0F 11 84 24 D0 01 00 00         movups xmmword ptr [rsp + 0x1d0], xmm0
00875705  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
0087570D  0F 57 C9                        xorps xmm1, xmm1
00875710  0F 11 8C 24 50 01 00 00         movups xmmword ptr [rsp + 0x150], xmm1
00875718  0F 11 8C 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm1
00875720  0F 11 8C 24 70 01 00 00         movups xmmword ptr [rsp + 0x170], xmm1
00875728  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
00875730  0F 11 8C 24 28 01 00 00         movups xmmword ptr [rsp + 0x128], xmm1
00875738  33 FF                           xor edi, edi
0087573A  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
00875742  33 D2                           xor edx, edx
00875744  41 B8 D0 01 00 00               mov r8d, 0x1d0
0087574A  48 8D 8C 24 50 02 00 00         lea rcx, [rsp + 0x250]
00875752  E8 E9 14 E5 FF                  call 0x1406c6c40
00875757  48 89 BC 24 38 01 00 00         mov qword ptr [rsp + 0x138], rdi
0087575F  40 88 7C 24 61                  mov byte ptr [rsp + 0x61], dil
00875764  89 BC 24 80 01 00 00            mov dword ptr [rsp + 0x180], edi
0087576B  44 8A E7                        mov r12b, dil
0087576E  48 8D 8C 24 D0 01 00 00         lea rcx, [rsp + 0x1d0]
00875776  E8 F5 66 B8 FF                  call 0x1403fbe70
0087577B  33 D2                           xor edx, edx
0087577D  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00875785  E8 F6 4F BB FF                  call 0x14042a780
0087578A  40 88 7C 24 62                  mov byte ptr [rsp + 0x62], dil
0087578F  33 D2                           xor edx, edx
00875791  48 8D 8C 24 28 01 00 00         lea rcx, [rsp + 0x128]
00875799  E8 E2 4F BB FF                  call 0x14042a780
0087579E  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
008757A6  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
008757AE  48 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdi
008757B6  48 89 BC 24 00 01 00 00         mov qword ptr [rsp + 0x100], rdi
008757BE  44 8B FF                        mov r15d, edi
008757C1  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
008757C6  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
008757CE  48 8D 8C 24 50 02 00 00         lea rcx, [rsp + 0x250]
008757D6  E8 15 10 00 00                  call 0x1408767f0
008757DB  44 8B EF                        mov r13d, edi
008757DE  48 89 BC 24 08 01 00 00         mov qword ptr [rsp + 0x108], rdi
008757E6  E8 81 44 35 00                  call 0x140bc9c6c
008757EB  88 44 24 70                     mov byte ptr [rsp + 0x70], al
008757EF  84 C0                           test al, al
008757F1  0F 84 5C 0A 00 00               je 0x140876253
008757F7  40 88 7C 24 60                  mov byte ptr [rsp + 0x60], dil
008757FC  41 F7 C6 0B 00 FF FF            test r14d, 0xffff000b
00875803  0F 85 EA 09 00 00               jne 0x1408761f3
00875809  48 85 F6                        test rsi, rsi
0087580C  0F 85 EB 09 00 00               jne 0x1408761fd
00875812  40 38 BC 24 C0 04 00 00         cmp byte ptr [rsp + 0x4c0], dil
0087581A  0F 85 C3 09 00 00               jne 0x1408761e3
00875820  41 0F BA E6 0C                  bt r14d, 0xc
00875825  0F 82 3C 0A 00 00               jb 0x140876267
0087582B  41 8B C6                        mov eax, r14d
0087582E  25 10 08 00 00                  and eax, 0x810
00875833  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
0087583A  E8 41 12 00 00                  call 0x140876a80
0087583F  8B F0                           mov esi, eax
00875841  85 C0                           test eax, eax
00875843  0F 88 36 06 00 00               js 0x140875e7f
00875849  45 8B E6                        mov r12d, r14d
0087584C  41 83 E4 10                     and r12d, 0x10
00875850  44 89 A4 24 F0 00 00 00         mov dword ptr [rsp + 0xf0], r12d
00875858  44 8A BC 24 D0 04 00 00         mov r15b, byte ptr [rsp + 0x4d0]
00875860  0F 84 C2 09 00 00               je 0x140876228
00875866  39 BC 24 80 00 00 00            cmp dword ptr [rsp + 0x80], edi
0087586D  0F 84 29 09 00 00               je 0x14087619c
00875873  48 39 BC 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdi
0087587B  0F 84 B6 08 00 00               je 0x140876137
00875881  41 F7 C6 44 04 00 00            test r14d, 0x444
00875888  0F 95 C1                        setne cl
0087588B  41 F6 C6 10                     test r14b, 0x10
0087588F  0F 95 C0                        setne al
00875892  84 C8                           test al, cl
00875894  0F 85 E4 09 00 00               jne 0x14087627e
0087589A  4C 8D 84 24 28 01 00 00         lea r8, [rsp + 0x128]
008758A2  41 8A D7                        mov dl, r15b
008758A5  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
008758AD  E8 16 12 00 00                  call 0x140876ac8
008758B2  8B F0                           mov esi, eax
008758B4  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
008758BB  85 C0                           test eax, eax
008758BD  0F 88 79 08 00 00               js 0x14087613c
008758C3  41 B1 01                        mov r9b, 1
008758C6  45 3A F9                        cmp r15b, r9b
008758C9  0F 84 C2 01 00 00               je 0x140875a91
008758CF  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
008758D9  0F 10 03                        movups xmm0, xmmword ptr [rbx]
008758DC  0F 11 84 24 50 01 00 00         movups xmmword ptr [rsp + 0x150], xmm0
008758E4  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
008758E8  0F 11 8C 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm1
008758F0  0F 10 43 20                     movups xmm0, xmmword ptr [rbx + 0x20]
008758F4  0F 11 84 24 70 01 00 00         movups xmmword ptr [rsp + 0x170], xmm0
008758FC  45 85 E4                        test r12d, r12d
008758FF  0F 85 0A 01 00 00               jne 0x140875a0f
00875905  45 3A F9                        cmp r15b, r9b
00875908  0F 84 8A 00 00 00               je 0x140875998
0087590E  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00875912  0F 10 00                        movups xmm0, xmmword ptr [rax]
00875915  F3 0F 7F 84 24 A0 00 00 00      movdqu xmmword ptr [rsp + 0xa0], xmm0
0087591E  0F B7 B4 24 A0 00 00 00         movzx esi, word ptr [rsp + 0xa0]
00875926  66 85 F6                        test si, si
00875929  74 59                           je 0x140875984
0087592B  41 B8 43 4D 62 6B               mov r8d, 0x6b624d43
00875931  8B D6                           mov edx, esi
00875933  E8 58 B8 BE FF                  call 0x140461190
00875938  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00875940  48 85 C0                        test rax, rax
00875943  0F 84 D6 00 00 00               je 0x140875a1f
00875949  44 8B C6                        mov r8d, esi
0087594C  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00875954  48 8B D8                        mov rbx, rax
00875957  48 8B C8                        mov rcx, rax
0087595A  E8 E1 0E E5 FF                  call 0x1406c6840
0087595F  66 89 B4 24 A0 00 00 00         mov word ptr [rsp + 0xa0], si
00875967  66 89 B4 24 A2 00 00 00         mov word ptr [rsp + 0xa2], si
0087596F  48 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rbx
00875977  4C 8B AC 24 08 01 00 00         mov r13, qword ptr [rsp + 0x108]
0087597F  E9 1D 01 00 00                  jmp 0x140875aa1
00875984  33 D2                           xor edx, edx
00875986  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
0087598E  E8 ED 4D BB FF                  call 0x14042a780
00875993  E9 09 01 00 00                  jmp 0x140875aa1
00875998  0F 57 C0                        xorps xmm0, xmm0
0087599B  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
008759A3  48 8B 8C 24 60 01 00 00         mov rcx, qword ptr [rsp + 0x160]
008759AB  48 3B CA                        cmp rcx, rdx
008759AE  48 0F 43 CA                     cmovae rcx, rdx
008759B2  90                              nop
008759B3  8B 01                           mov eax, dword ptr [rcx]
008759B5  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
008759BC  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
008759C0  4C 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r8
008759C8  0F 28 84 24 D0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xd0]
008759D0  66 0F 7F 84 24 A0 00 00 00      movdqa xmmword ptr [rsp + 0xa0], xmm0
008759D9  66 0F 7E C0                     movd eax, xmm0
008759DD  66 85 C0                        test ax, ax
008759E0  0F 84 38 FF FF FF               je 0x14087591e
008759E6  45 84 C1                        test r9b, r8b
008759E9  0F 85 AD 00 00 00               jne 0x140875a9c
008759EF  0F B7 C0                        movzx eax, ax
008759F2  4E 8D 0C 00                     lea r9, [rax + r8]
008759F6  4A 8D 0C 00                     lea rcx, [rax + r8]
008759FA  48 3B CA                        cmp rcx, rdx
008759FD  77 09                           ja 0x140875a08
008759FF  4D 3B C8                        cmp r9, r8
00875A02  0F 83 16 FF FF FF               jae 0x14087591e
00875A08  8A 02                           mov al, byte ptr [rdx]
00875A0A  E9 0F FF FF FF                  jmp 0x14087591e
00875A0F  48 39 BC 24 58 01 00 00         cmp qword ptr [rsp + 0x158], rdi
00875A17  0F 84 E8 FE FF FF               je 0x140875905
00875A1D  EB 19                           jmp 0x140875a38
00875A1F  BE 9A 00 00 C0                  mov esi, 0xc000009a
00875A24  89 B4 24 84 00 00 00            mov dword ptr [rsp + 0x84], esi
00875A2B  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00875A30  45 8A E7                        mov r12b, r15b
00875A33  E9 47 04 00 00                  jmp 0x140875e7f
00875A38  BE EF 00 00 C0                  mov esi, 0xc00000ef
00875A3D  89 B4 24 84 00 00 00            mov dword ptr [rsp + 0x84], esi
00875A44  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00875A49  45 8A E7                        mov r12b, r15b
00875A4C  E9 2E 04 00 00                  jmp 0x140875e7f
00875A51  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
00875A5B  48 8B C2                        mov rax, rdx
00875A5E  48 3B DA                        cmp rbx, rdx
00875A61  48 0F 42 C3                     cmovb rax, rbx
00875A65  90                              nop
00875A66  8A 00                           mov al, byte ptr [rax]
00875A68  39 BC 24 80 00 00 00            cmp dword ptr [rsp + 0x80], edi
00875A6F  0F 84 64 FE FF FF               je 0x1408758d9
00875A75  48 8B C2                        mov rax, rdx
00875A78  48 39 94 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdx
00875A80  48 0F 42 84 24 B0 00 00 00      cmovb rax, qword ptr [rsp + 0xb0]
00875A89  48 89 38                        mov qword ptr [rax], rdi
00875A8C  E9 48 FE FF FF                  jmp 0x1408758d9
00875A91  F6 C3 03                        test bl, 3
00875A94  74 BB                           je 0x140875a51
00875A96  E8 35 45 02 00                  call 0x140899fd0
00875A9B  CC                              int3
00875A9C  E8 2F 45 02 00                  call 0x140899fd0
00875AA1  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00875AA9  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
00875AB1  48 89 BC 24 70 01 00 00         mov qword ptr [rsp + 0x170], rdi
00875AB9  EB 16                           jmp 0x140875ad1
00875ABB  8B F0                           mov esi, eax
00875ABD  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
00875AC4  33 FF                           xor edi, edi
00875AC6  44 8A E7                        mov r12b, dil
00875AC9  44 8B FF                        mov r15d, edi
00875ACC  E9 AE 03 00 00                  jmp 0x140875e7f
00875AD1  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
00875AD9  48 85 C0                        test rax, rax
00875ADC  0F 85 1F 06 00 00               jne 0x140876101
00875AE2  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00875AE7  48 85 C0                        test rax, rax
00875AEA  0F 85 98 07 00 00               jne 0x140876288
00875AF0  48 8B 8C 24 90 01 00 00         mov rcx, qword ptr [rsp + 0x190]
00875AF8  48 85 C9                        test rcx, rcx
00875AFB  0F 85 B7 06 00 00               jne 0x1408761b8
00875B01  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00875B09  48 85 C0                        test rax, rax
00875B0C  0F 85 64 1E 2A 00               jne 0x140b17976
00875B12  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00875B1B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00875B22  90                              nop
00875B23  C6 44 24 62 01                  mov byte ptr [rsp + 0x62], 1
00875B28  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
00875B30  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00875B35  41 B9 19 00 02 00               mov r9d, 0x20019
00875B3B  45 8A C7                        mov r8b, r15b
00875B3E  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
00875B46  E8 91 12 00 00                  call 0x140876ddc
00875B4B  8B F0                           mov esi, eax
00875B4D  85 C0                           test eax, eax
00875B4F  0F 88 20 03 00 00               js 0x140875e75
00875B55  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00875B5D  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
00875B65  48 8B DF                        mov rbx, rdi
00875B68  33 D2                           xor edx, edx
00875B6A  44 8D 42 60                     lea r8d, [rdx + 0x60]
00875B6E  48 8D 8C 24 F0 01 00 00         lea rcx, [rsp + 0x1f0]
00875B76  E8 C5 10 E5 FF                  call 0x1406c6c40
00875B7B  0F 57 C0                        xorps xmm0, xmm0
00875B7E  33 C0                           xor eax, eax
00875B80  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
00875B88  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00875B90  48 8D 84 24 18 01 00 00         lea rax, [rsp + 0x118]
00875B98  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
00875BA0  48 8D 84 24 18 01 00 00         lea rax, [rsp + 0x118]
00875BA8  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
00875BB0  39 1D D2 9F 67 00               cmp dword ptr [rip + 0x679fd2], ebx
00875BB6  0F 85 C3 03 00 00               jne 0x140875f7f
00875BBC  85 F6                           test esi, esi
00875BBE  0F 88 27 05 00 00               js 0x1408760eb
00875BC4  41 8B D6                        mov edx, r14d
00875BC7  48 8D 8C 24 28 01 00 00         lea rcx, [rsp + 0x128]
00875BCF  E8 64 13 00 00                  call 0x140876f38
00875BD4  C6 44 24 60 01                  mov byte ptr [rsp + 0x60], 1
00875BD9  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00875BE1  45 33 C9                        xor r9d, r9d
00875BE4  45 8B C6                        mov r8d, r14d
00875BE7  48 8D 94 24 28 01 00 00         lea rdx, [rsp + 0x128]
00875BEF  48 8D 8C 24 50 01 00 00         lea rcx, [rsp + 0x150]
00875BF7  45 85 E4                        test r12d, r12d
00875BFA  0F 84 47 05 00 00               je 0x140876147
00875C00  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00875C05  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
00875C0D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00875C12  44 88 7C 24 38                  mov byte ptr [rsp + 0x38], r15b
00875C17  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00875C1C  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00875C21  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00875C26  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00875C2E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00875C33  E8 C4 13 00 00                  call 0x140876ffc
00875C38  8B F0                           mov esi, eax
00875C3A  83 3D 47 9F 67 00 00            cmp dword ptr [rip + 0x679f47], 0
00875C41  0F 84 CB 00 00 00               je 0x140875d12
00875C47  E8 30 0E BE FF                  call 0x140456a7c
00875C4C  85 C0                           test eax, eax
00875C4E  0F 85 BE 00 00 00               jne 0x140875d12
00875C54  48 8D 84 24 18 01 00 00         lea rax, [rsp + 0x118]
00875C5C  48 39 84 24 18 01 00 00         cmp qword ptr [rsp + 0x118], rax
00875C64  0F 84 A8 00 00 00               je 0x140875d12
00875C6A  0F 57 C0                        xorps xmm0, xmm0
00875C6D  33 C0                           xor eax, eax
00875C6F  0F 11 84 24 98 01 00 00         movups xmmword ptr [rsp + 0x198], xmm0
00875C77  0F 11 84 24 A8 01 00 00         movups xmmword ptr [rsp + 0x1a8], xmm0
00875C7F  0F 11 84 24 B8 01 00 00         movups xmmword ptr [rsp + 0x1b8], xmm0
00875C87  48 89 84 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rax
00875C8F  48 89 9C 24 98 01 00 00         mov qword ptr [rsp + 0x198], rbx
00875C97  89 B4 24 A0 01 00 00            mov dword ptr [rsp + 0x1a0], esi
00875C9E  89 B4 24 B0 01 00 00            mov dword ptr [rsp + 0x1b0], esi
00875CA5  48 8D 84 24 F0 01 00 00         lea rax, [rsp + 0x1f0]
00875CAD  48 89 84 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rax
00875CB5  48 8D 84 24 98 01 00 00         lea rax, [rsp + 0x198]
00875CBD  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
00875CC5  48 8D 84 24 D0 00 00 00         lea rax, [rsp + 0xd0]
00875CCD  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00875CD5  48 8D 84 24 18 01 00 00         lea rax, [rsp + 0x118]
00875CDD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00875CE2  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00875CE7  C7 44 24 20 21 00 00 00         mov dword ptr [rsp + 0x20], 0x21
00875CEF  45 33 C9                        xor r9d, r9d
00875CF2  4C 8D 84 24 40 01 00 00         lea r8, [rsp + 0x140]
00875CFA  48 8D 94 24 98 01 00 00         lea rdx, [rsp + 0x198]
00875D02  41 8D 49 21                     lea ecx, [r9 + 0x21]
00875D06  E8 35 02 FF FF                  call 0x140865f40
00875D0B  8B B4 24 B0 01 00 00            mov esi, dword ptr [rsp + 0x1b0]
00875D12  44 8A 6C 24 61                  mov r13b, byte ptr [rsp + 0x61]
00875D17  48 85 DB                        test rbx, rbx
00875D1A  74 08                           je 0x140875d24
00875D1C  48 8B CB                        mov rcx, rbx
00875D1F  E8 2C 36 A8 FF                  call 0x1402f9350
00875D24  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00875D2C  48 85 C9                        test rcx, rcx
00875D2F  74 0D                           je 0x140875d3e
00875D31  E8 1A 36 A8 FF                  call 0x1402f9350
00875D36  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00875D3E  85 F6                           test esi, esi
00875D40  0F 88 2F 01 00 00               js 0x140875e75
00875D46  39 BC 24 80 00 00 00            cmp dword ptr [rsp + 0x80], edi
00875D4D  0F 84 22 01 00 00               je 0x140875e75
00875D53  45 84 ED                        test r13b, r13b
00875D56  0F 85 19 01 00 00               jne 0x140875e75
00875D5C  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00875D61  8B 84 24 50 02 00 00            mov eax, dword ptr [rsp + 0x250]
00875D68  BA 40 00 00 00                  mov edx, 0x40
00875D6D  45 85 E4                        test r12d, r12d
00875D70  0F 45 C2                        cmovne eax, edx
00875D73  89 84 24 50 02 00 00            mov dword ptr [rsp + 0x250], eax
00875D7A  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00875D82  48 85 C9                        test rcx, rcx
00875D85  75 10                           jne 0x140875d97
00875D87  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00875D8F  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
00875D97  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00875D9C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00875DA1  48 8D 84 24 50 02 00 00         lea rax, [rsp + 0x250]
00875DA9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00875DAE  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00875DB3  48 8B 05 06 0D 75 00            mov rax, qword ptr [rip + 0x750d06]
00875DBA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00875DBF  45 33 C9                        xor r9d, r9d
00875DC2  45 33 C0                        xor r8d, r8d
00875DC5  E8 36 EC 04 00                  call 0x1408c4a00
00875DCA  8B F0                           mov esi, eax
00875DCC  85 C0                           test eax, eax
00875DCE  0F 88 88 00 00 00               js 0x140875e5c
00875DD4  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00875DD9  48 8B CB                        mov rcx, rbx
00875DDC  E8 AF 10 00 00                  call 0x140876e90
00875DE1  41 8A C7                        mov al, r15b
00875DE4  F6 D8                           neg al
00875DE6  1B D2                           sbb edx, edx
00875DE8  81 E2 00 FE FF FF               and edx, 0xfffffe00
00875DEE  81 C2 40 02 00 00               add edx, 0x240
00875DF4  48 8D 84 24 38 01 00 00         lea rax, [rsp + 0x138]
00875DFC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00875E01  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
00875E06  48 8B 05 B3 0C 75 00            mov rax, qword ptr [rip + 0x750cb3]
00875E0D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00875E12  44 8B 8C 24 A0 04 00 00         mov r9d, dword ptr [rsp + 0x4a0]
00875E1A  45 33 C0                        xor r8d, r8d
00875E1D  48 8B CB                        mov rcx, rbx
00875E20  E8 FB 15 04 00                  call 0x1408b7420
00875E25  8B F0                           mov esi, eax
00875E27  48 8B CB                        mov rcx, rbx
00875E2A  E8 21 35 A8 FF                  call 0x1402f9350
00875E2F  85 F6                           test esi, esi
00875E31  78 29                           js 0x140875e5c
00875E33  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00875E3B  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00875E43  48 89 01                        mov qword ptr [rcx], rax
00875E46  EB 14                           jmp 0x140875e5c
00875E48  8B F0                           mov esi, eax
00875E4A  33 FF                           xor edi, edi
00875E4C  44 8B A4 24 F0 00 00 00         mov r12d, dword ptr [rsp + 0xf0]
00875E54  44 8B B4 24 F8 00 00 00         mov r14d, dword ptr [rsp + 0xf8]
00875E5C  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00875E64  48 85 C9                        test rcx, rcx
00875E67  0F 85 41 02 00 00               jne 0x1408760ae
00875E6D  85 F6                           test esi, esi
00875E6F  0F 88 5A 04 00 00               js 0x1408762cf
00875E75  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00875E7A  44 8A 64 24 60                  mov r12b, byte ptr [rsp + 0x60]
00875E7F  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00875E87  48 85 C9                        test rcx, rcx
00875E8A  0F 85 51 04 00 00               jne 0x1408762e1
00875E90  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00875E98  48 85 C9                        test rcx, rcx
00875E9B  0F 85 2A 02 00 00               jne 0x1408760cb
00875EA1  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00875EA9  48 85 C9                        test rcx, rcx
00875EAC  0F 85 97 03 00 00               jne 0x140876249
00875EB2  40 38 7C 24 62                  cmp byte ptr [rsp + 0x62], dil
00875EB7  74 05                           je 0x140875ebe
00875EB9  E8 F2 79 9E FF                  call 0x14025d8b0
00875EBE  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00875EC6  48 85 C9                        test rcx, rcx
00875EC9  74 05                           je 0x140875ed0
00875ECB  E8 80 34 A8 FF                  call 0x1402f9350
00875ED0  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00875ED8  48 85 C9                        test rcx, rcx
00875EDB  74 05                           je 0x140875ee2
00875EDD  E8 6E 34 A8 FF                  call 0x1402f9350
00875EE2  4D 85 FF                        test r15, r15
00875EE5  0F 85 02 04 00 00               jne 0x1408762ed
00875EEB  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00875EF3  48 85 C9                        test rcx, rcx
00875EF6  0F 85 FE 03 00 00               jne 0x1408762fa
00875EFC  48 8B 9C 24 10 01 00 00         mov rbx, qword ptr [rsp + 0x110]
00875F04  48 85 DB                        test rbx, rbx
00875F07  74 08                           je 0x140875f11
00875F09  48 8B CB                        mov rcx, rbx
00875F0C  E8 6F FE BF FF                  call 0x140475d80
00875F11  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
00875F19  48 85 C9                        test rcx, rcx
00875F1C  74 07                           je 0x140875f25
00875F1E  33 D2                           xor edx, edx
00875F20  E8 4B C9 30 00                  call 0x140b82870
00875F25  33 D2                           xor edx, edx
00875F27  48 8D 8C 24 50 02 00 00         lea rcx, [rsp + 0x250]
00875F2F  E8 DC 09 00 00                  call 0x140876910
00875F34  40 38 7C 24 70                  cmp byte ptr [rsp + 0x70], dil
00875F39  74 05                           je 0x140875f40
00875F3B  E8 6C 3D 35 00                  call 0x140bc9cac
00875F40  45 84 E4                        test r12b, r12b
00875F43  74 07                           je 0x140875f4c
00875F45  8B CE                           mov ecx, esi
00875F47  E8 A4 0A 00 00                  call 0x1408769f0
00875F4C  48 8D 8C 24 D0 01 00 00         lea rcx, [rsp + 0x1d0]
00875F54  E8 F7 9D BA FF                  call 0x14041fd50
00875F59  8B C6                           mov eax, esi
00875F5B  48 8B 8C 24 20 04 00 00         mov rcx, qword ptr [rsp + 0x420]
00875F63  48 33 CC                        xor rcx, rsp
00875F66  E8 D5 66 E3 FF                  call 0x1406ac640
00875F6B  48 81 C4 30 04 00 00            add rsp, 0x430
00875F72  41 5F                           pop r15
00875F74  41 5E                           pop r14
00875F76  41 5D                           pop r13
00875F78  41 5C                           pop r12
00875F7A  5F                              pop rdi
00875F7B  5E                              pop rsi
00875F7C  5B                              pop rbx
00875F7D  C3                              ret
00875F7E  CC                              int3
00875F7F  E8 F8 0A BE FF                  call 0x140456a7c
00875F84  85 C0                           test eax, eax
00875F86  0F 85 30 FC FF FF               jne 0x140875bbc
00875F8C  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
00875F94  48 85 C9                        test rcx, rcx
00875F97  74 2A                           je 0x140875fc3
00875F99  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00875F9E  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00875FA3  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00875FA8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00875FAD  45 33 C9                        xor r9d, r9d
00875FB0  4C 8B 05 09 0B 75 00            mov r8, qword ptr [rip + 0x750b09]
00875FB7  33 D2                           xor edx, edx
00875FB9  E8 F2 2D FF FF                  call 0x140868db0
00875FBE  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00875FC3  48 C7 84 24 40 02 00 00 02 00 00 00  mov qword ptr [rsp + 0x240], 2
00875FCF  48 89 9C 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rbx
00875FD7  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00875FDF  48 89 84 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rax
00875FE7  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
00875FEF  48 89 84 24 00 02 00 00         mov qword ptr [rsp + 0x200], rax
00875FF7  44 89 B4 24 08 02 00 00         mov dword ptr [rsp + 0x208], r14d
00875FFF  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00876007  48 89 84 24 10 02 00 00         mov qword ptr [rsp + 0x210], rax
0087600F  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00876014  48 89 84 24 18 02 00 00         mov qword ptr [rsp + 0x218], rax
0087601C  8B 84 24 A0 04 00 00            mov eax, dword ptr [rsp + 0x4a0]
00876023  89 84 24 20 02 00 00            mov dword ptr [rsp + 0x220], eax
0087602A  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00876032  48 89 84 24 28 02 00 00         mov qword ptr [rsp + 0x228], rax
0087603A  4C 89 AC 24 48 02 00 00         mov qword ptr [rsp + 0x248], r13
00876042  48 8D 84 24 F0 01 00 00         lea rax, [rsp + 0x1f0]
0087604A  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00876052  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0087605A  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
00876062  8A 84 24 C0 04 00 00            mov al, byte ptr [rsp + 0x4c0]
00876069  88 84 24 E0 00 00 00            mov byte ptr [rsp + 0xe0], al
00876070  48 8D 84 24 18 01 00 00         lea rax, [rsp + 0x118]
00876078  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0087607D  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00876082  C7 44 24 20 21 00 00 00         mov dword ptr [rsp + 0x20], 0x21
0087608A  41 B1 01                        mov r9b, 1
0087608D  4C 8D 84 24 D0 00 00 00         lea r8, [rsp + 0xd0]
00876095  48 8D 94 24 F0 01 00 00         lea rdx, [rsp + 0x1f0]
0087609D  B9 20 00 00 00                  mov ecx, 0x20
008760A2  E8 99 FE FE FF                  call 0x140865f40
008760A7  8B F0                           mov esi, eax
008760A9  E9 0E FB FF FF                  jmp 0x140875bbc
008760AE  45 85 E4                        test r12d, r12d
008760B1  0F 84 55 01 00 00               je 0x14087620c
008760B7  8B D6                           mov edx, esi
008760B9  E8 CA 1B 00 00                  call 0x140877c88
008760BE  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
008760C6  E9 A2 FD FF FF                  jmp 0x140875e6d
008760CB  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
008760D3  48 3B C8                        cmp rcx, rax
008760D6  0F 84 C5 FD FF FF               je 0x140875ea1
008760DC  BA 43 4D 4E 62                  mov edx, 0x624e4d43
008760E1  E8 FA 28 BD FF                  call 0x1404489e0
008760E6  E9 B6 FD FF FF                  jmp 0x140875ea1
008760EB  81 FE 03 05 00 C0               cmp esi, 0xc0000503
008760F1  0F 85 1B FC FF FF               jne 0x140875d12
008760F7  8B F7                           mov esi, edi
008760F9  41 B5 01                        mov r13b, 1
008760FC  E9 16 FC FF FF                  jmp 0x140875d17
00876101  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00876106  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
0087610E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00876113  45 8A CF                        mov r9b, r15b
00876116  33 D2                           xor edx, edx
00876118  48 8B C8                        mov rcx, rax
0087611B  E8 30 32 35 00                  call 0x140bc9350
00876120  8B F0                           mov esi, eax
00876122  85 C0                           test eax, eax
00876124  0F 89 B8 F9 FF FF               jns 0x140875ae2
0087612A  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0087612F  45 8A E7                        mov r12b, r15b
00876132  E9 48 FD FF FF                  jmp 0x140875e7f
00876137  BE F5 00 00 C0                  mov esi, 0xc00000f5
0087613C  44 8A E7                        mov r12b, dil
0087613F  4C 8B FF                        mov r15, rdi
00876142  E9 38 FD FF FF                  jmp 0x140875e7f
00876147  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0087614C  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
00876154  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00876159  44 88 7C 24 48                  mov byte ptr [rsp + 0x48], r15b
0087615E  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00876163  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00876168  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0087616D  8A 84 24 C0 04 00 00            mov al, byte ptr [rsp + 0x4c0]
00876174  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00876178  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00876180  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00876185  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0087618D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00876192  E8 35 26 00 00                  call 0x1408787cc
00876197  E9 9C FA FF FF                  jmp 0x140875c38
0087619C  48 39 BC 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdi
008761A4  75 91                           jne 0x140876137
008761A6  48 39 7C 24 78                  cmp qword ptr [rsp + 0x78], rdi
008761AB  0F 84 E9 F6 FF FF               je 0x14087589a
008761B1  BE F3 00 00 C0                  mov esi, 0xc00000f3
008761B6  EB 84                           jmp 0x14087613c
008761B8  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
008761BD  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
008761C5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008761CA  45 8A CF                        mov r9b, r15b
008761CD  33 D2                           xor edx, edx
008761CF  E8 7C 31 35 00                  call 0x140bc9350
008761D4  8B F0                           mov esi, eax
008761D6  85 C0                           test eax, eax
008761D8  0F 89 23 F9 FF FF               jns 0x140875b01
008761DE  E9 92 FC FF FF                  jmp 0x140875e75
008761E3  48 85 F6                        test rsi, rsi
008761E6  74 75                           je 0x14087625d
008761E8  41 0F BA E6 0E                  bt r14d, 0xe
008761ED  0F 82 2D F6 FF FF               jb 0x140875820
008761F3  BE F1 00 00 C0                  mov esi, 0xc00000f1
008761F8  E9 82 FC FF FF                  jmp 0x140875e7f
008761FD  41 F7 C6 FF 9E FF FF            test r14d, 0xffff9eff
00876204  0F 84 08 F6 FF FF               je 0x140875812
0087620A  EB E7                           jmp 0x1408761f3
0087620C  E8 23 39 35 00                  call 0x140bc9b34
00876211  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00876219  E8 F2 B0 FD FF                  call 0x140851310
0087621E  E8 61 38 35 00                  call 0x140bc9a84
00876223  E9 96 FE FF FF                  jmp 0x1408760be
00876228  41 8A D7                        mov dl, r15b
0087622B  48 8B 0D AE 38 76 00            mov rcx, qword ptr [rip + 0x7638ae]
00876232  E8 E9 BB FF FF                  call 0x140871e20
00876237  84 C0                           test al, al
00876239  0F 85 27 F6 FF FF               jne 0x140875866
0087623F  BE 61 00 00 C0                  mov esi, 0xc0000061
00876244  E9 F3 FE FF FF                  jmp 0x14087613c
00876249  E8 62 70 E3 FF                  call 0x1406ad2b0
0087624E  E9 5F FC FF FF                  jmp 0x140875eb2
00876253  BE 89 01 00 C0                  mov esi, 0xc0000189
00876258  E9 22 FC FF FF                  jmp 0x140875e7f
0087625D  BE F8 00 00 C0                  mov esi, 0xc00000f8
00876262  E9 18 FC FF FF                  jmp 0x140875e7f
00876267  41 8B C6                        mov eax, r14d
0087626A  B9 00 06 00 00                  mov ecx, 0x600
0087626F  23 C1                           and eax, ecx
00876271  3B C1                           cmp eax, ecx
00876273  0F 85 7A FF FF FF               jne 0x1408761f3
00876279  E9 AD F5 FF FF                  jmp 0x14087582b
0087627E  BE F1 00 00 C0                  mov esi, 0xc00000f1
00876283  E9 B4 FE FF FF                  jmp 0x14087613c
00876288  4C 8B 05 F1 08 75 00            mov r8, qword ptr [rip + 0x7508f1]
0087628F  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00876294  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00876299  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0087629E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008762A3  45 8A CF                        mov r9b, r15b
008762A6  BA 02 00 00 00                  mov edx, 2
008762AB  48 8B C8                        mov rcx, rax
008762AE  E8 FD 2A FF FF                  call 0x140868db0
008762B3  8B F0                           mov esi, eax
008762B5  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008762BA  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008762BF  85 F6                           test esi, esi
008762C1  0F 89 29 F8 FF FF               jns 0x140875af0
008762C7  4C 8B F8                        mov r15, rax
008762CA  E9 AB FB FF FF                  jmp 0x140875e7a
008762CF  41 0F BA E6 0B                  bt r14d, 0xb
008762D4  0F 83 9B FB FF FF               jae 0x140875e75
008762DA  8B F7                           mov esi, edi
008762DC  E9 94 FB FF FF                  jmp 0x140875e75
008762E1  8B D6                           mov edx, esi
008762E3  E8 A0 19 00 00                  call 0x140877c88
008762E8  E9 A3 FB FF FF                  jmp 0x140875e90
008762ED  49 8B CF                        mov rcx, r15
008762F0  E8 5B 30 A8 FF                  call 0x1402f9350
008762F5  E9 F1 FB FF FF                  jmp 0x140875eeb
008762FA  E8 51 30 A8 FF                  call 0x1402f9350
008762FF  E9 F8 FB FF FF                  jmp 0x140875efc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmLoadDifferencingKey(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10, unsigned __int8 a11, __int64 a12, unsigned __int8 a13)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2B0;
    unsigned int v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned int v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned int v_stack_m2E8;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m350;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned int v_stack_m370;
    unsigned int v_stack_m378;
    unsigned __int64 v_stack_m388;
    unsigned __int64 v_stack_m390;
    unsigned __int64 v_stack_m398;
    unsigned __int64 v_stack_m3A8;
    unsigned __int64 v_stack_m3B0;
    unsigned __int64 v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int16 v_stack_m3C6;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned int v_stack_m3E4;
    unsigned int v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned __int8 v_stack_m3F8;
    unsigned __int64 v_stack_m400;
    unsigned __int8 v_stack_m406;
    unsigned __int8 v_stack_m407;
    unsigned __int8 v_stack_m408;
    unsigned __int64 v_stack_m420;
    unsigned __int64 v_stack_m428;
    unsigned __int8 v_stack_m430;
    unsigned __int64 v_stack_m438;
    unsigned __int64 v_stack_m440;
    unsigned __int64 v_stack_m448;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p158;
    unsigned __int64 v_stack_p1F0;
    unsigned __int64 v_stack_p1F8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p200;
    unsigned int v_stack_p208;
    unsigned __int64 v_stack_p210;
    unsigned __int64 v_stack_p218;
    unsigned int v_stack_p220;
    unsigned __int64 v_stack_p228;
    unsigned __int64 v_stack_p240;
    unsigned __int64 v_stack_p248;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int8 v_stack_pE0;

    v_rsp = (v_rsp) - (0x430ULL);
    result = (*(unsigned __int64 *)(v_rip + 5853366)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m398 = a2;
    v_stack_m3B8 = a8;
    v_stack_m370 = a3;
    v_stack_m2E0 = a5;
    v_stack_m3F0 = a6;
    v_stack_m2D8 = a10;
    v_stack_m328 = a12;
    result = 0;
    v_stack_m298 = v_xmm0;
    v_stack_m288 = 0;
    v_stack_m318 = v_xmm1;
    v_stack_m308 = v_xmm1;
    v_stack_m2F8 = v_xmm1;
    v_stack_m3C8 = v_xmm0;
    v_stack_m340 = v_xmm1;
    v_rdi = 0;
    v_stack_m3B0 = 0;
    a2 = 0;
    result = memset(v_stack_m218, a2, 464, a4);
    v_stack_m330 = 0;
    v_stack_m407 = 0;
    v_stack_m2E8 = 0;
    result = CmpInitializeThreadInfo(v_stack_m298, a2, 464, a4);
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m3C8, a2, 464, a4);
    v_stack_m406 = 0;
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m340, a2, 464, a4);
    v_stack_m3E0 = 0;
    v_stack_m3D8 = 0;
    v_stack_m3A8 = 0;
    v_stack_m368 = 0;
    v_stack_m400 = 0;
    v_stack_m358 = 0;
    result = CmpInitializeParseContext(v_stack_m218, a2, 464, a4);
    v_stack_m360 = 0;
    result = CmpAcquireHiveLoadUnloadRundown(v_stack_m218, a2, 464, a4);
    v_stack_m3F8 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00876253;
    v_stack_m408 = 0;
    if ((((unsigned int)((unsigned int)(a3))) & (0xFFFF000BULL)) != 0) goto loc_008761F3;
    if (a10 != 0) goto loc_008761FD;
loc_00875812:
    if (a11 != 0) goto loc_008761E3;
loc_00875820:
    if (a11 < 0) goto loc_00876267;
loc_0087582B:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (0x810ULL));
    v_stack_m3E8 = (unsigned int)(result);
    result = CmCheckNoTxContext(v_stack_m218, a2, 464, a4);
    if (sign_flag) goto loc_00875E7F;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (16));
    v_stack_m378 = (unsigned int)(v_r12);
    if (condition_is_equal) goto loc_00876228;
loc_00875866:
    if (v_stack_m3E8 == 0) goto loc_0087619C;
    if (v_stack_m3B8 == 0) goto loc_00876137;
    a1 = ((((unsigned int)((unsigned int)(a3))) & (0x444ULL)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(a3))) & (16)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0087627E;
loc_0087589A:
    result = CmpNameFromAttributes(v_stack_m398, a13, v_stack_m340, a4);
    v_stack_m3E4 = (unsigned int)(result);
    if (sign_flag) goto loc_0087613C;
    if (a13 == 1) goto loc_00875A91;
loc_008758D9:
    v_stack_m318 = v_xmm0;
    v_stack_m308 = v_xmm1;
    v_stack_m2F8 = v_xmm0;
    if ((unsigned int)(v_r12) != 0) goto loc_00875A0F;
loc_00875905:
    if (a13 == 1) goto loc_00875998;
    v_stack_m3C8 = v_xmm0;
loc_0087591E:
    if ((unsigned __int16)(v_stack_m3C8) == 0) goto loc_00875984;
    result = CmpAllocateTransientPoolWithQuota(v_stack_m398, (unsigned int)((unsigned int)(v_stack_m3C8)), (unsigned int)(0x6B624D43ULL), 1);
    v_stack_m358 = result;
    if (result == 0) goto loc_00875A1F;
    result = memcpy(result, v_stack_m3C0, (unsigned int)((unsigned int)(v_stack_m3C8)), 1);
    v_stack_m3C8 = (unsigned __int16)(v_stack_m3C8);
    v_stack_m3C6 = (unsigned __int16)(v_stack_m3C8);
    v_stack_m3C0 = result;
    goto loc_00875AA1;
loc_00875984:
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m3C8, a2, (unsigned int)((unsigned int)(v_stack_m3C8)), 1);
    goto loc_00875AA1;
loc_00875998:
    v_stack_m398 = v_xmm0;
    a1 = v_stack_m308;
    if (v_stack_m308 >= 0) { a1 = 0; }
    v_stack_m398 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m390 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m3C8 = v_xmm0;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_0087591E;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 8)))) != 0) goto loc_00875A9C;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1) > 0) goto loc_00875A08;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_0087591E;
loc_00875A08:
    goto loc_0087591E;
loc_00875A0F:
    if (v_stack_m310 == 0) goto loc_00875905;
    goto loc_00875A38;
loc_00875A1F:
    v_stack_m3E4 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_00875E7F;
loc_00875A38:
    v_stack_m3E4 = (unsigned int)((unsigned int)(0xC00000EFULL));
    goto loc_00875E7F;
loc_00875A51:
    result = 0;
    if (result < 0) { result = result; }
    if (v_stack_m3E8 == 0) goto loc_008758D9;
    result = 0;
    if (v_stack_m3B8 < 0) { result = v_stack_m3B8; }
    *(unsigned __int64 *)(result) = 0;
    goto loc_008758D9;
loc_00875A91:
    if ((((unsigned __int8)(result)) & (3)) == 0) goto loc_00875A51;
    result = ExRaiseDatatypeMisalignment((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, a2, *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1);
loc_00875A9C:
    result = ExRaiseDatatypeMisalignment((unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1, a2, *(unsigned __int64 *)(a1 + 8), (unsigned __int16)((unsigned int)(*(unsigned int *)(a1))) + *(unsigned __int64 *)(a1 + 8) * 1);
loc_00875AA1:
    v_stack_m308 = v_stack_m3C8;
    v_stack_m2F8 = 0;
    goto loc_00875AD1;
loc_00875AD1:
    if (v_stack_m2E0 != 0) goto loc_00876101;
loc_00875AE2:
    if (v_stack_m3F0 != 0) goto loc_00876288;
loc_00875AF0:
    if (v_stack_m2D8 != 0) goto loc_008761B8;
loc_00875B01:
    v_stack_m406 = 1;
    v_stack_m448 = v_stack_m368;
    result = CmConvertHandleToKernelHandle(v_stack_m310, a2, (unsigned __int8)(v_stack_m400), (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_00875E75;
    v_stack_m310 = v_stack_m368;
    a2 = 0;
    result = memset(v_stack_m278, a2, a2 + 96, (unsigned int)(0x20019ULL));
    result = 0;
    v_stack_m398 = v_xmm0;
    v_stack_m388 = 0;
    v_stack_m348 = v_stack_m350;
    v_stack_m350 = v_stack_m350;
    if ((*(unsigned int *)(v_rip + 6791122)) != 0) goto loc_00875F7F;
loc_00875BBC:
    if (sign_flag) goto loc_008760EB;
    result = CmpTraceHiveLoadStart(v_stack_m340, (unsigned int)((unsigned int)((unsigned int)(a3))), a2 + 96, (unsigned int)(0x20019ULL));
    v_stack_m408 = 1;
    a4 = 0;
    if ((unsigned int)((unsigned __int8)(v_stack_m400)) == 0) goto loc_00876147;
    v_stack_m420 = v_stack_m3D8;
    v_stack_m428 = v_stack_m3B0;
    v_stack_m430 = (unsigned __int8)(v_stack_m400);
    v_stack_m438 = v_stack_m360;
    v_stack_m440 = v_stack_m400;
    v_stack_m448 = v_stack_m3E0;
    result = CmLoadAppKey(v_stack_m318, v_stack_m340, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
loc_00875C38:
    if ((*(unsigned int *)(v_rip + 6790983)) == 0) goto loc_00875D12;
    result = CmpIsRegistryLockAcquired(v_stack_m318, v_stack_m340, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned int)(result) != 0) goto loc_00875D12;
    result = v_stack_m350;
    v_rsi = (unsigned int)((unsigned int)(result));
    if (v_stack_m350 != v_stack_m350) {
        result = 0;
        v_stack_m2D0 = v_xmm0;
        v_stack_m2C0 = v_xmm0;
        v_stack_m2B0 = v_xmm0;
        v_stack_m2A0 = 0;
        v_stack_m2D0 = 0;
        v_stack_m2C8 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_m2B8 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = v_stack_m278;
        v_stack_m2C0 = result;
        result = v_stack_m2D0;
        v_stack_m328 = result;
        result = v_stack_m398;
        v_stack_m320 = result;
        result = v_stack_m350;
        v_stack_m438 = result;
        v_stack_m440 = 0;
        v_stack_m448 = 33;
        a4 = 0;
        a3 = v_stack_m328;
        a2 = v_stack_m2D0;
        a1 = a4 + 33;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rsi = v_stack_m2B8;
    }
loc_00875D17:
    if (0 != 0) {
        a1 = 0;
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    if (v_stack_m3E0 != 0) {
        result = ObfDereferenceObject(v_stack_m3E0, a2, a3, a4);
        v_stack_m3E0 = 0;
    }
    if (sign_flag) goto loc_00875E75;
    if (v_stack_m3E8 == 0) goto loc_00875E75;
    if ((unsigned __int8)(v_stack_m407) != 0) goto loc_00875E75;
    v_stack_m3F0 = 0;
    result = (unsigned int)(v_stack_m218);
    if ((unsigned int)((unsigned __int8)(v_stack_m400)) != 0) { result = 64; }
    v_stack_m218 = (unsigned int)(result);
    if (v_stack_m3B0 == 0) {
        a1 = v_stack_m3C8;
        v_stack_m3B0 = a1;
    }
    v_stack_m430 = v_stack_m3F0;
    v_stack_m438 = v_stack_m218;
    v_stack_m440 = 0;
    v_stack_m448 = *(unsigned __int64 *)(v_rip + 7671046);
    a4 = 0;
    a3 = 0;
    result = ObReferenceObjectByName(a1, 64, a3, a4);
    if (sign_flag) goto loc_00875E5C;
    result = ObDeleteCapturedInsertInfo(v_stack_m3F0, 64, a3, a4);
    result = (unsigned __int8)(-((unsigned __int8)(v_stack_m400)));
    a2 = (unsigned int)((64) & (0xFFFFFE00ULL));
    a2 = (unsigned int)((a2) + (576));
    v_stack_m438 = v_stack_m330;
    v_stack_m440 = (unsigned __int8)(v_stack_m400);
    v_stack_m448 = *(unsigned __int64 *)(v_rip + 7670963);
    a3 = 0;
    result = ObOpenObjectByPointer(v_stack_m3F0, a2, a3, (unsigned int)(a7));
    result = ObfDereferenceObject(v_stack_m3F0, a2, a3, (unsigned int)(a7));
    if (sign_flag) goto loc_00875E5C;
    *(unsigned __int64 *)(v_stack_m3B8) = v_stack_m330;
    goto loc_00875E5C;
loc_00875E5C:
    if (v_stack_m3D8 != 0) goto loc_008760AE;
loc_00875E6D:
    if (sign_flag) goto loc_008762CF;
loc_00875E75:
loc_00875E7A:
loc_00875E7F:
    if (v_stack_m3D8 != 0) goto loc_008762E1;
loc_00875E90:
    if (v_stack_m3B0 != 0) goto loc_008760CB;
loc_00875EA1:
    if (v_stack_m368 != 0) goto loc_00876249;
loc_00875EB2:
    result = v_stack_m330;
    if (v_stack_m406 != 0) {
        result = KeLeaveCriticalRegion(v_stack_m368, a2, a3, (unsigned int)(a7));
    }
    if (v_stack_m360 != 0) {
        result = ObfDereferenceObject(v_stack_m360, a2, a3, (unsigned int)(a7));
    }
    if (v_stack_m3A8 != 0) {
        result = ObfDereferenceObject(v_stack_m3A8, a2, a3, (unsigned int)(a7));
    }
    if (v_stack_m400 != 0) goto loc_008762ED;
loc_00875EEB:
    if (v_stack_m3E0 != 0) goto loc_008762FA;
loc_00875EFC:
    if (v_stack_m358 != 0) {
        a1 = v_stack_m358;
        result = CmSiFreeMemory(a1, a2, a3, (unsigned int)(a7));
    }
    if (v_stack_m338 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m338, a2, a3, (unsigned int)(a7));
    }
    a2 = 0;
    result = CmpCleanupParseContext(v_stack_m218, a2, a3, (unsigned int)(a7));
    if (v_stack_m3F8 != 0) {
        result = CmpReleaseHiveLoadUnloadRundown(v_stack_m218, a2, a3, (unsigned int)(a7));
    }
    if ((unsigned __int8)(v_stack_m408) != 0) {
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = CmpTraceHiveLoadStop(a1, a2, a3, (unsigned int)(a7));
    }
    result = CmCleanupThreadInfo(v_stack_m298, a2, a3, (unsigned int)(a7));
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)(a7));
    v_rsp = (v_rsp) + (0x430ULL);
    return result;
loc_00875F7F:
    result = CmpIsRegistryLockAcquired(a1, a2, a3, (unsigned int)(a7));
    if ((unsigned int)(result) != 0) goto loc_00875BBC;
    v_rbx = v_stack_m358;
    if (v_stack_p158 != 0) {
        v_stack_p78 = 0;
        v_stack_p28 = 0;
        result = v_stack_p78;
        v_stack_p20 = result;
        a4 = 0;
        a3 = *(unsigned __int64 *)(v_rip + 7670537);
        a2 = 0;
        result = ObReferenceObjectByHandle(v_stack_p158, a2, a3, a4);
        v_rbx = v_stack_p78;
    }
    v_stack_p240 = 2;
    v_stack_p1F0 = v_rbx;
    v_stack_p1F8 = v_stack_pA0;
    v_stack_p200 = v_stack_p128;
    v_stack_p208 = (unsigned int)((unsigned int)(a3));
    v_stack_p210 = v_stack_p88;
    v_stack_p218 = v_stack_p68;
    v_stack_p220 = (unsigned int)((unsigned int)(a7));
    v_stack_p228 = v_stack_pB0;
    v_stack_p248 = v_stack_m407;
    v_stack_pD0 = v_stack_p1F0;
    v_stack_pD8 = v_stack_pC0;
    v_stack_pE0 = a11;
    v_stack_p30 = v_stack_p118;
    v_stack_p28 = 0;
    v_stack_p20 = 33;
    result = CmpCallCallBacksEx(32, v_stack_p1F0, v_stack_pD0, 1);
    goto loc_00875BBC;
loc_008760AE:
    if ((unsigned int)(v_stack_m408) == 0) goto loc_0087620C;
    result = CmReleaseLoadKeyContext(32, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_pD0, 1);
loc_008760BE:
    v_stack_p90 = 0;
    goto loc_00875E6D;
loc_008760CB:
    if (32 == v_stack_pA0) goto loc_00875EA1;
    result = CmpFreePoolWithTag(32, (unsigned int)(0x624E4D43ULL), v_stack_pD0, 1);
    goto loc_00875EA1;
loc_008760EB:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000503ULL) goto loc_00875D12;
    goto loc_00875D17;
loc_00876101:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p88;
    a2 = 0;
    result = CmObReferenceObjectByHandle(result, a2, v_stack_pD0, (unsigned __int8)(v_stack_m400));
    if (!sign_flag) goto loc_00875AE2;
    goto loc_00875E7F;
loc_00876137:
loc_0087613C:
    goto loc_00875E7F;
loc_00876147:
    v_stack_p58 = result;
    v_stack_p50 = v_stack_pB8;
    v_stack_p48 = 0;
    v_stack_p40 = 1;
    v_stack_p38 = v_stack_p68;
    v_stack_p30 = a11;
    v_stack_p28 = v_stack_pC0;
    v_stack_p20 = v_stack_p88;
    result = CmLoadKey(result, a2, v_stack_pD0, (unsigned __int8)(v_stack_m400));
    goto loc_00875C38;
loc_0087619C:
    if (v_stack_pB0 != 0) goto loc_00876137;
    if (v_stack_p78 == 0) goto loc_0087589A;
    goto loc_0087613C;
loc_008761B8:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_pC0;
    a2 = 0;
    result = CmObReferenceObjectByHandle(result, a2, v_stack_pD0, 0);
    if (!sign_flag) goto loc_00875B01;
    goto loc_00875E75;
loc_008761E3:
    if ((unsigned int)((unsigned int)(result)) == 0) goto loc_0087625D;
    if (condition_is_below) goto loc_00875820;
loc_008761F3:
    goto loc_00875E7F;
loc_008761FD:
    if ((((unsigned int)((unsigned int)(a3))) & (0xFFFF9EFFULL)) == 0) goto loc_00875812;
    goto loc_008761F3;
loc_0087620C:
    result = CmpLockRegistry(result, a2, v_stack_pD0, 0);
    result = CmpDereferenceKeyControlBlock(v_stack_p90, a2, v_stack_pD0, 0);
    result = CmpUnlockRegistry(v_stack_p90, a2, v_stack_pD0, 0);
    goto loc_008760BE;
loc_00876228:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 7747758), 0, v_stack_pD0, 0);
    if ((unsigned __int8)(result) != 0) goto loc_00875866;
    goto loc_0087613C;
loc_00876249:
    result = ZwClose(*(unsigned __int64 *)(v_rip + 7747758), 0, v_stack_pD0, 0);
    goto loc_00875EB2;
loc_00876253:
    goto loc_00875E7F;
loc_0087625D:
    goto loc_00875E7F;
loc_00876267:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & ((unsigned int)((unsigned int)(0x600ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x600ULL)))) goto loc_008761F3;
    goto loc_0087582B;
loc_0087627E:
    goto loc_0087613C;
loc_00876288:
    v_stack_p78 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p78;
    result = ObReferenceObjectByHandle(result, 2, *(unsigned __int64 *)(v_rip + 7670001), 0);
    v_stack_p68 = v_stack_p78;
    if (!sign_flag) goto loc_00875AF0;
    goto loc_00875E7A;
loc_008762CF:
    if (condition_is_above_or_equal) goto loc_00875E75;
    goto loc_00875E75;
loc_008762E1:
    result = CmReleaseLoadKeyContext(result, 0, *(unsigned __int64 *)(v_rip + 7670001), 0);
    goto loc_00875E90;
loc_008762ED:
    result = ObfDereferenceObject(v_stack_p78, 0, *(unsigned __int64 *)(v_rip + 7670001), 0);
    goto loc_00875EEB;
loc_008762FA:
    result = ObfDereferenceObject(v_stack_p78, 0, *(unsigned __int64 *)(v_rip + 7670001), 0);
    goto loc_00875EFC;
}
```

## 5. (Beta) C Style

```c
int64_t CmLoadDifferencingKey(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8, uint64_t Arg9, int64_t Arg10, uint8_t Arg11, int64_t Arg12, uint8_t Arg13)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m218;
    uint64_t v_stack_m278;
    uint64_t v_stack_m288;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2B0;
    uint32_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint32_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint32_t v_stack_m2E8;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint64_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m340;
    uint64_t v_stack_m348;
    uint64_t v_stack_m350;
    uint64_t v_stack_m358;
    uint64_t v_stack_m360;
    uint64_t v_stack_m368;
    uint32_t v_stack_m370;
    uint32_t v_stack_m378;
    uint64_t v_stack_m388;
    uint64_t v_stack_m390;
    uint64_t v_stack_m398;
    uint64_t v_stack_m3A8;
    uint64_t v_stack_m3B0;
    uint64_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint16_t v_stack_m3C6;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint32_t v_stack_m3E4;
    uint32_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint8_t v_stack_m3F8;
    uint64_t v_stack_m400;
    uint8_t v_stack_m406;
    uint8_t v_stack_m407;
    uint8_t v_stack_m408;
    uint64_t v_stack_m420;
    uint64_t v_stack_m428;
    uint8_t v_stack_m430;
    uint64_t v_stack_m438;
    uint64_t v_stack_m440;
    uint64_t v_stack_m448;
    uint64_t v_stack_m48;
    uint64_t v_stack_p118;
    uint64_t v_stack_p128;
    uint64_t v_stack_p158;
    uint64_t v_stack_p1F0;
    uint64_t v_stack_p1F8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p200;
    uint32_t v_stack_p208;
    uint64_t v_stack_p210;
    uint64_t v_stack_p218;
    uint32_t v_stack_p220;
    uint64_t v_stack_p228;
    uint64_t v_stack_p240;
    uint64_t v_stack_p248;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint8_t v_stack_pE0;

    local_rsp = (local_rsp) - (0x430ULL);
    result = (*(uint64_t *)(v_rip + 0x5950B6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m398 = Arg2;
    v_stack_m3B8 = Arg8;
    v_stack_m370 = Arg3;
    v_stack_m2E0 = Arg5;
    v_stack_m3F0 = Arg6;
    v_stack_m2D8 = Arg10;
    v_stack_m328 = Arg12;
    result = 0;
    v_stack_m298 = v_xmm0;
    v_stack_m288 = 0;
    v_stack_m318 = v_xmm1;
    v_stack_m308 = v_xmm1;
    v_stack_m2F8 = v_xmm1;
    v_stack_m3C8 = v_xmm0;
    v_stack_m340 = v_xmm1;
    local_rdi = 0;
    v_stack_m3B0 = 0;
    Arg2 = 0;
    result = memset(v_stack_m218, Arg2, 464, Arg4);
    v_stack_m330 = 0;
    v_stack_m407 = 0;
    v_stack_m2E8 = 0;
    result = CmpInitializeThreadInfo(v_stack_m298, Arg2, 464, Arg4);
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m3C8, Arg2, 464, Arg4);
    v_stack_m406 = 0;
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m340, Arg2, 464, Arg4);
    v_stack_m3E0 = 0;
    v_stack_m3D8 = 0;
    v_stack_m3A8 = 0;
    v_stack_m368 = 0;
    v_stack_m400 = 0;
    v_stack_m358 = 0;
    result = CmpInitializeParseContext(v_stack_m218, Arg2, 464, Arg4);
    v_stack_m360 = 0;
    result = CmpAcquireHiveLoadUnloadRundown(v_stack_m218, Arg2, 464, Arg4);
    v_stack_m3F8 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00876253;
    v_stack_m408 = 0;
    if ((((uint32_t)((uint32_t)(Arg3))) & (0xFFFF000BULL)) != 0) goto loc_008761F3;
    if (Arg10 != 0) goto loc_008761FD;
loc_00875812:
    if (Arg11 != 0) goto loc_008761E3;
loc_00875820:
    if (Arg11 < 0) goto loc_00876267;
loc_0087582B:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (0x810ULL));
    v_stack_m3E8 = (uint32_t)(result);
    result = CmCheckNoTxContext(v_stack_m218, Arg2, 464, Arg4);
    if (sign_flag) goto loc_00875E7F;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (16));
    v_stack_m378 = (uint32_t)(local_r12);
    if (condition_is_equal) goto loc_00876228;
loc_00875866:
    if (v_stack_m3E8 == 0) goto loc_0087619C;
    if (v_stack_m3B8 == 0) goto loc_00876137;
    Arg1 = ((((uint32_t)((uint32_t)(Arg3))) & (0x444ULL)) != 0) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(Arg3))) & (16)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0087627E;
loc_0087589A:
    result = CmpNameFromAttributes(v_stack_m398, Arg13, v_stack_m340, Arg4);
    v_stack_m3E4 = (uint32_t)(result);
    if (sign_flag) goto loc_0087613C;
    if (Arg13 == 1) goto loc_00875A91;
loc_008758D9:
    v_stack_m318 = v_xmm0;
    v_stack_m308 = v_xmm1;
    v_stack_m2F8 = v_xmm0;
    if ((uint32_t)(local_r12) != 0) goto loc_00875A0F;
loc_00875905:
    if (Arg13 == 1) goto loc_00875998;
    v_stack_m3C8 = v_xmm0;
loc_0087591E:
    if ((uint16_t)(v_stack_m3C8) == 0) goto loc_00875984;
    result = CmpAllocateTransientPoolWithQuota(v_stack_m398, (uint32_t)((uint32_t)(v_stack_m3C8)), (uint32_t)(0x6B624D43ULL), 1);
    v_stack_m358 = result;
    if (result == 0) goto loc_00875A1F;
    result = memcpy(result, v_stack_m3C0, (uint32_t)((uint32_t)(v_stack_m3C8)), 1);
    v_stack_m3C8 = (uint16_t)(v_stack_m3C8);
    v_stack_m3C6 = (uint16_t)(v_stack_m3C8);
    v_stack_m3C0 = result;
    goto loc_00875AA1;
loc_00875984:
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m3C8, Arg2, (uint32_t)((uint32_t)(v_stack_m3C8)), 1);
    goto loc_00875AA1;
loc_00875998:
    v_stack_m398 = v_xmm0;
    Arg1 = v_stack_m308;
    if (v_stack_m308 >= 0) { Arg1 = 0; }
    v_stack_m398 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_m390 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m3C8 = v_xmm0;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) == 0) goto loc_0087591E;
    if (((1) & ((uint8_t)(*(uint64_t *)(Arg1 + 0x8)))) != 0) goto loc_00875A9C;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1) > 0) goto loc_00875A08;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1) >= (*(uint64_t *)(Arg1 + 0x8))) goto loc_0087591E;
loc_00875A08:
    goto loc_0087591E;
loc_00875A0F:
    if (v_stack_m310 == 0) goto loc_00875905;
    goto loc_00875A38;
loc_00875A1F:
    v_stack_m3E4 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_00875E7F;
loc_00875A38:
    v_stack_m3E4 = (uint32_t)((uint32_t)(0xC00000EFULL));
    goto loc_00875E7F;
loc_00875A51:
    result = 0;
    if (result < 0) { result = result; }
    if (v_stack_m3E8 == 0) goto loc_008758D9;
    result = 0;
    if (v_stack_m3B8 < 0) { result = v_stack_m3B8; }
    *(uint64_t *)(result) = 0;
    goto loc_008758D9;
loc_00875A91:
    if ((((uint8_t)(result)) & (3)) == 0) goto loc_00875A51;
    result = ExRaiseDatatypeMisalignment((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, Arg2, *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1);
loc_00875A9C:
    result = ExRaiseDatatypeMisalignment((uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1, Arg2, *(uint64_t *)(Arg1 + 0x8), (uint16_t)((uint32_t)(*(uint32_t *)(Arg1))) + *(uint64_t *)(Arg1 + 0x8) * 1);
loc_00875AA1:
    v_stack_m308 = v_stack_m3C8;
    v_stack_m2F8 = 0;
    goto loc_00875AD1;
loc_00875AD1:
    if (v_stack_m2E0 != 0) goto loc_00876101;
loc_00875AE2:
    if (v_stack_m3F0 != 0) goto loc_00876288;
loc_00875AF0:
    if (v_stack_m2D8 != 0) goto loc_008761B8;
loc_00875B01:
    v_stack_m406 = 1;
    v_stack_m448 = v_stack_m368;
    result = CmConvertHandleToKernelHandle(v_stack_m310, Arg2, (uint8_t)(v_stack_m400), (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_00875E75;
    v_stack_m310 = v_stack_m368;
    Arg2 = 0;
    result = memset(v_stack_m278, Arg2, Arg2 + 96, (uint32_t)(0x20019ULL));
    result = 0;
    v_stack_m398 = v_xmm0;
    v_stack_m388 = 0;
    v_stack_m348 = v_stack_m350;
    v_stack_m350 = v_stack_m350;
    if ((*(uint32_t *)(v_rip + 0x679FD2)) != 0) goto loc_00875F7F;
loc_00875BBC:
    if (sign_flag) goto loc_008760EB;
    result = CmpTraceHiveLoadStart(v_stack_m340, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg2 + 96, (uint32_t)(0x20019ULL));
    v_stack_m408 = 1;
    Arg4 = 0;
    if ((uint32_t)((uint8_t)(v_stack_m400)) == 0) goto loc_00876147;
    v_stack_m420 = v_stack_m3D8;
    v_stack_m428 = v_stack_m3B0;
    v_stack_m430 = (uint8_t)(v_stack_m400);
    v_stack_m438 = v_stack_m360;
    v_stack_m440 = v_stack_m400;
    v_stack_m448 = v_stack_m3E0;
    result = CmLoadAppKey(v_stack_m318, v_stack_m340, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
loc_00875C38:
    if ((*(uint32_t *)(v_rip + 0x679F47)) == 0) goto loc_00875D12;
    result = CmpIsRegistryLockAcquired(v_stack_m318, v_stack_m340, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00875D12;
    result = v_stack_m350;
    local_rsi = (uint32_t)((uint32_t)(result));
    if (v_stack_m350 != v_stack_m350) {
        result = 0;
        v_stack_m2D0 = v_xmm0;
        v_stack_m2C0 = v_xmm0;
        v_stack_m2B0 = v_xmm0;
        v_stack_m2A0 = 0;
        v_stack_m2D0 = 0;
        v_stack_m2C8 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_m2B8 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = v_stack_m278;
        v_stack_m2C0 = result;
        result = v_stack_m2D0;
        v_stack_m328 = result;
        result = v_stack_m398;
        v_stack_m320 = result;
        result = v_stack_m350;
        v_stack_m438 = result;
        v_stack_m440 = 0;
        v_stack_m448 = 33;
        Arg4 = 0;
        Arg3 = v_stack_m328;
        Arg2 = v_stack_m2D0;
        Arg1 = Arg4 + 33;
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
        local_rsi = v_stack_m2B8;
    }
loc_00875D17:
    if (0 != 0) {
        Arg1 = 0;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m3E0 != 0) {
        result = ObfDereferenceObject(v_stack_m3E0, Arg2, Arg3, Arg4);
        v_stack_m3E0 = 0;
    }
    if (sign_flag) goto loc_00875E75;
    if (v_stack_m3E8 == 0) goto loc_00875E75;
    if ((uint8_t)(v_stack_m407) != 0) goto loc_00875E75;
    v_stack_m3F0 = 0;
    result = (uint32_t)(v_stack_m218);
    if ((uint32_t)((uint8_t)(v_stack_m400)) != 0) { result = 64; }
    v_stack_m218 = (uint32_t)(result);
    if (v_stack_m3B0 == 0) {
        Arg1 = v_stack_m3C8;
        v_stack_m3B0 = Arg1;
    }
    v_stack_m430 = v_stack_m3F0;
    v_stack_m438 = v_stack_m218;
    v_stack_m440 = 0;
    v_stack_m448 = *(uint64_t *)(v_rip + 0x750D06);
    Arg4 = 0;
    Arg3 = 0;
    result = ObReferenceObjectByName(Arg1, 64, Arg3, Arg4);
    if (sign_flag) goto loc_00875E5C;
    result = ObDeleteCapturedInsertInfo(v_stack_m3F0, 64, Arg3, Arg4);
    result = (uint8_t)(-((uint8_t)(v_stack_m400)));
    Arg2 = (uint32_t)((64) & (0xFFFFFE00ULL));
    Arg2 = (uint32_t)((Arg2) + (576));
    v_stack_m438 = v_stack_m330;
    v_stack_m440 = (uint8_t)(v_stack_m400);
    v_stack_m448 = *(uint64_t *)(v_rip + 0x750CB3);
    Arg3 = 0;
    result = ObOpenObjectByPointer(v_stack_m3F0, Arg2, Arg3, (uint32_t)(Arg7));
    result = ObfDereferenceObject(v_stack_m3F0, Arg2, Arg3, (uint32_t)(Arg7));
    if (sign_flag) goto loc_00875E5C;
    *(uint64_t *)(v_stack_m3B8) = v_stack_m330;
    goto loc_00875E5C;
loc_00875E5C:
    if (v_stack_m3D8 != 0) goto loc_008760AE;
loc_00875E6D:
    if (sign_flag) goto loc_008762CF;
loc_00875E75:
loc_00875E7A:
loc_00875E7F:
    if (v_stack_m3D8 != 0) goto loc_008762E1;
loc_00875E90:
    if (v_stack_m3B0 != 0) goto loc_008760CB;
loc_00875EA1:
    if (v_stack_m368 != 0) goto loc_00876249;
loc_00875EB2:
    result = v_stack_m330;
    if (v_stack_m406 != 0) {
        result = KeLeaveCriticalRegion(v_stack_m368, Arg2, Arg3, (uint32_t)(Arg7));
    }
    if (v_stack_m360 != 0) {
        result = ObfDereferenceObject(v_stack_m360, Arg2, Arg3, (uint32_t)(Arg7));
    }
    if (v_stack_m3A8 != 0) {
        result = ObfDereferenceObject(v_stack_m3A8, Arg2, Arg3, (uint32_t)(Arg7));
    }
    if (v_stack_m400 != 0) goto loc_008762ED;
loc_00875EEB:
    if (v_stack_m3E0 != 0) goto loc_008762FA;
loc_00875EFC:
    if (v_stack_m358 != 0) {
        Arg1 = v_stack_m358;
        result = CmSiFreeMemory(Arg1, Arg2, Arg3, (uint32_t)(Arg7));
    }
    if (v_stack_m338 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m338, Arg2, Arg3, (uint32_t)(Arg7));
    }
    Arg2 = 0;
    result = CmpCleanupParseContext(v_stack_m218, Arg2, Arg3, (uint32_t)(Arg7));
    if (v_stack_m3F8 != 0) {
        result = CmpReleaseHiveLoadUnloadRundown(v_stack_m218, Arg2, Arg3, (uint32_t)(Arg7));
    }
    if ((uint8_t)(v_stack_m408) != 0) {
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = CmpTraceHiveLoadStop(Arg1, Arg2, Arg3, (uint32_t)(Arg7));
    }
    result = CmCleanupThreadInfo(v_stack_m298, Arg2, Arg3, (uint32_t)(Arg7));
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (uint32_t)(Arg7));
    local_rsp = (local_rsp) + (0x430ULL);
    return result;
loc_00875F7F:
    result = CmpIsRegistryLockAcquired(Arg1, Arg2, Arg3, (uint32_t)(Arg7));
    if ((uint32_t)(result) != 0) goto loc_00875BBC;
    local_rbx = v_stack_m358;
    if (v_stack_p158 != 0) {
        v_stack_p78 = 0;
        v_stack_p28 = 0;
        result = v_stack_p78;
        v_stack_p20 = result;
        Arg4 = 0;
        Arg3 = *(uint64_t *)(v_rip + 0x750B09);
        Arg2 = 0;
        result = ObReferenceObjectByHandle(v_stack_p158, Arg2, Arg3, Arg4);
        local_rbx = v_stack_p78;
    }
    v_stack_p240 = 2;
    v_stack_p1F0 = local_rbx;
    v_stack_p1F8 = v_stack_pA0;
    v_stack_p200 = v_stack_p128;
    v_stack_p208 = (uint32_t)((uint32_t)(Arg3));
    v_stack_p210 = v_stack_p88;
    v_stack_p218 = v_stack_p68;
    v_stack_p220 = (uint32_t)((uint32_t)(Arg7));
    v_stack_p228 = v_stack_pB0;
    v_stack_p248 = v_stack_m407;
    v_stack_pD0 = v_stack_p1F0;
    v_stack_pD8 = v_stack_pC0;
    v_stack_pE0 = Arg11;
    v_stack_p30 = v_stack_p118;
    v_stack_p28 = 0;
    v_stack_p20 = 33;
    result = CmpCallCallBacksEx(32, v_stack_p1F0, v_stack_pD0, 1);
    goto loc_00875BBC;
loc_008760AE:
    if ((uint32_t)(v_stack_m408) == 0) goto loc_0087620C;
    result = CmReleaseLoadKeyContext(32, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_pD0, 1);
loc_008760BE:
    v_stack_p90 = 0;
    goto loc_00875E6D;
loc_008760CB:
    if (32 == v_stack_pA0) goto loc_00875EA1;
    result = CmpFreePoolWithTag(32, (uint32_t)(0x624E4D43ULL), v_stack_pD0, 1);
    goto loc_00875EA1;
loc_008760EB:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000503ULL) goto loc_00875D12;
    goto loc_00875D17;
loc_00876101:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p88;
    Arg2 = 0;
    result = CmObReferenceObjectByHandle(result, Arg2, v_stack_pD0, (uint8_t)(v_stack_m400));
    if (!sign_flag) goto loc_00875AE2;
    goto loc_00875E7F;
loc_00876137:
loc_0087613C:
    goto loc_00875E7F;
loc_00876147:
    v_stack_p58 = result;
    v_stack_p50 = v_stack_pB8;
    v_stack_p48 = 0;
    v_stack_p40 = 1;
    v_stack_p38 = v_stack_p68;
    v_stack_p30 = Arg11;
    v_stack_p28 = v_stack_pC0;
    v_stack_p20 = v_stack_p88;
    result = CmLoadKey(result, Arg2, v_stack_pD0, (uint8_t)(v_stack_m400));
    goto loc_00875C38;
loc_0087619C:
    if (v_stack_pB0 != 0) goto loc_00876137;
    if (v_stack_p78 == 0) goto loc_0087589A;
    goto loc_0087613C;
loc_008761B8:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_pC0;
    Arg2 = 0;
    result = CmObReferenceObjectByHandle(result, Arg2, v_stack_pD0, 0);
    if (!sign_flag) goto loc_00875B01;
    goto loc_00875E75;
loc_008761E3:
    if ((uint32_t)((uint32_t)(result)) == 0) goto loc_0087625D;
    if (condition_is_below) goto loc_00875820;
loc_008761F3:
    goto loc_00875E7F;
loc_008761FD:
    if ((((uint32_t)((uint32_t)(Arg3))) & (0xFFFF9EFFULL)) == 0) goto loc_00875812;
    goto loc_008761F3;
loc_0087620C:
    result = CmpLockRegistry(result, Arg2, v_stack_pD0, 0);
    result = CmpDereferenceKeyControlBlock(v_stack_p90, Arg2, v_stack_pD0, 0);
    result = CmpUnlockRegistry(v_stack_p90, Arg2, v_stack_pD0, 0);
    goto loc_008760BE;
loc_00876228:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x7638AE), 0, v_stack_pD0, 0);
    if ((uint8_t)(result) != 0) goto loc_00875866;
    goto loc_0087613C;
loc_00876249:
    result = ZwClose(*(uint64_t *)(v_rip + 0x7638AE), 0, v_stack_pD0, 0);
    goto loc_00875EB2;
loc_00876253:
    goto loc_00875E7F;
loc_0087625D:
    goto loc_00875E7F;
loc_00876267:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & ((uint32_t)((uint32_t)(0x600ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x600ULL)))) goto loc_008761F3;
    goto loc_0087582B;
loc_0087627E:
    goto loc_0087613C;
loc_00876288:
    v_stack_p78 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p78;
    result = ObReferenceObjectByHandle(result, 2, *(uint64_t *)(v_rip + 0x7508F1), 0);
    v_stack_p68 = v_stack_p78;
    if (!sign_flag) goto loc_00875AF0;
    goto loc_00875E7A;
loc_008762CF:
    if (condition_is_above_or_equal) goto loc_00875E75;
    goto loc_00875E75;
loc_008762E1:
    result = CmReleaseLoadKeyContext(result, 0, *(uint64_t *)(v_rip + 0x7508F1), 0);
    goto loc_00875E90;
loc_008762ED:
    result = ObfDereferenceObject(v_stack_p78, 0, *(uint64_t *)(v_rip + 0x7508F1), 0);
    goto loc_00875EEB;
loc_008762FA:
    result = ObfDereferenceObject(v_stack_p78, 0, *(uint64_t *)(v_rip + 0x7508F1), 0);
    goto loc_00875EFC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00875670&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
