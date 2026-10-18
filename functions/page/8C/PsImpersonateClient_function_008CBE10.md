# PsImpersonateClient

- RVA: `0x008CBE10`–`0x008CC4B9` (길이 `1,705` bytes)
- VA: `0x00000001408CBE10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00084550`
- 디코드: `377`개 명령, `1,705/1,705` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x008CBE71` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x008CBE93` → [SeTokenCanImpersonate](SeTokenCanImpersonate_function_008CC4C0.md) (function, `0x008CC4C0`)
- `0x008CBEF1` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x008CBEFE` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008CBF2A` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (function, `0x004E96E0`)
- `0x008CBF80` → [PsIsProcessLoggingEnabled](../../text/41/PsIsProcessLoggingEnabled_function_0041AF00.md) (function, `0x0041AF00`)
- `0x008CBF95` → [EtwTiLogImpersonateClient](EtwTiLogImpersonateClient_function_008CC9D0.md) (function, `0x008CC9D0`)
- `0x008CBFA0` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (function, `0x004E97C0`)
- `0x008CBFAB` → [PspWriteTebImpersonationInfo](PspWriteTebImpersonationInfo_function_008CC7F0.md) (function, `0x008CC7F0`)
- `0x008CBFCB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008CC005` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (function, `0x004E96E0`)
- `0x008CC045` → [PsIsProcessLoggingEnabled](../../text/41/PsIsProcessLoggingEnabled_function_0041AF00.md) (function, `0x0041AF00`)
- `0x008CC065` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x008CC078` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (function, `0x004E97C0`)
- `0x008CC08D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CC10B` → [SepDuplicateToken](../8B/SepDuplicateToken_function_008B87EC.md) (function, `0x008B87EC`)
- `0x008CC143` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x008CC174` → [SepAppendAceToTokenObjectAcl](../8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) (function, `0x008B6430`)
- `0x008CC1D5` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x008CC1E5` → [SeQueryTokenTrustSid](../../text/48/SeQueryTokenTrustSid_function_0048C85C.md) (function, `0x0048C85C`)
- `0x008CC23B` → [SepDuplicateToken](../8B/SepDuplicateToken_function_008B87EC.md) (function, `0x008B87EC`)
- `0x008CC268` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)
- `0x008CC279` → [SepSetProcessTrustLabelAceForToken](../../text/40/SepSetProcessTrustLabelAceForToken_function_004007A0.md) (function, `0x004007A0`)
- `0x008CC2AD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008CC2E6` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x008CC30C` → [SepFinalizeTokenAcls](../8B/SepFinalizeTokenAcls_function_008B63F4.md) (function, `0x008B63F4`)
- `0x008CC32C` → [SeSetTokenTrustLink](../../text/47/SeSetTokenTrustLink_function_00475004.md) (function, `0x00475004`)
- `0x008CC37B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008CC3B1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008CC3C8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CC3EA` → [SepAppendAceToTokenObjectAcl](../8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) (function, `0x008B6430`)
- `0x008CC419` → [SepAppendAceToTokenObjectAcl](../8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) (function, `0x008B6430`)
- `0x008CC42F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008CC465` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CC477` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CC4A1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [CmpCmdHiveOpen](../87/CmpCmdHiveOpen_function_00878404.md) at `0x008785DC`
- [CmpOpenHiveFile](../87/CmpOpenHiveFile_function_0087A71C.md) at `0x0087AC22`
- [CmpOpenHiveFile](../87/CmpOpenHiveFile_function_0087A71C.md) at `0x0087AC6B`
- [NtAlpcImpersonateClientOfPort](../89/NtAlpcImpersonateClientOfPort_function_008961A0.md) at `0x00896768`
- [sub_00896999](../89/Unknown_function_00896999.md) at `0x00896ACD`
- [NtSetInformationThread](NtSetInformationThread_function_008C9F60.md) at `0x008CA292`
- [NtSetInformationThread](NtSetInformationThread_function_008C9F60.md) at `0x008CA4DA`
- [PsAssignImpersonationToken](PsAssignImpersonationToken_function_008CBCB0.md) at `0x008CBCE1`
- [PsAssignImpersonationToken](PsAssignImpersonationToken_function_008CBCB0.md) at `0x008CBD53`
- [PsRevertThreadToSelf](PsRevertThreadToSelf_function_008CBD90.md) at `0x008CBDA4`
- [SeImpersonateClientEx](SeImpersonateClientEx_function_008CBDC0.md) at `0x008CBDF4`
- [PsRevertToSelf](PsRevertToSelf_function_008CD200.md) at `0x008CD21D`
- [NtImpersonateThread](NtImpersonateThread_function_008CD230.md) at `0x008CD39E`
- [NtImpersonateAnonymousToken](../A3/NtImpersonateAnonymousToken_function_00A3A150.md) at `0x00A3A23F`
- [NtImpersonateAnonymousToken](../A3/NtImpersonateAnonymousToken_function_00A3A150.md) at `0x00A3A386`

### Static image references
- `0x008CBE2C` → RVA `0x00E0A740` (`.data`; read)
- `0x008CBED8` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x008CC04E` → RVA `0x00EFFA30` (`.data`; read)
- `0x008CC055` → RVA `0x000113B0` (`.rdata`; read)
- `0x008CC165` → RVA `0x00FD9A68` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **25**
  - `0x008CBE71` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x008CBEF1` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x008CBEFE` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008CBF2A` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (`PAGE` → `.text`)
  - `0x008CBF80` → [PsIsProcessLoggingEnabled](../../text/41/PsIsProcessLoggingEnabled_function_0041AF00.md) (`PAGE` → `.text`)
  - `0x008CBFA0` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (`PAGE` → `.text`)
  - `0x008CBFCB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008CC005` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (`PAGE` → `.text`)
  - `0x008CC045` → [PsIsProcessLoggingEnabled](../../text/41/PsIsProcessLoggingEnabled_function_0041AF00.md) (`PAGE` → `.text`)
  - `0x008CC065` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x008CC078` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (`PAGE` → `.text`)
  - `0x008CC08D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CC1D5` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x008CC1E5` → [SeQueryTokenTrustSid](../../text/48/SeQueryTokenTrustSid_function_0048C85C.md) (`PAGE` → `.text`)
  - `0x008CC268` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`PAGE` → `.text`)
  - `0x008CC279` → [SepSetProcessTrustLabelAceForToken](../../text/40/SepSetProcessTrustLabelAceForToken_function_004007A0.md) (`PAGE` → `.text`)
  - `0x008CC2AD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008CC32C` → [SeSetTokenTrustLink](../../text/47/SeSetTokenTrustLink_function_00475004.md) (`PAGE` → `.text`)
  - `0x008CC37B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008CC3B1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008CC3C8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CC42F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008CC465` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CC477` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CC4A1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008CC06C` → [sub_00B1B7C0](../B1/Unknown_function_00B1B7C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008CBE10  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008CBE15  55                              push rbp
008CBE16  56                              push rsi
008CBE17  57                              push rdi
008CBE18  41 54                           push r12
008CBE1A  41 55                           push r13
008CBE1C  41 56                           push r14
008CBE1E  41 57                           push r15
008CBE20  48 8D 6C 24 A0                  lea rbp, [rsp - 0x60]
008CBE25  48 81 EC 60 01 00 00            sub rsp, 0x160
008CBE2C  48 8B 05 0D E9 53 00            mov rax, qword ptr [rip + 0x53e90d]
008CBE33  48 33 C4                        xor rax, rsp
008CBE36  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
008CBE3A  48 8B B1 20 02 00 00            mov rsi, qword ptr [rcx + 0x220]
008CBE41  45 32 FF                        xor r15b, r15b
008CBE44  45 33 E4                        xor r12d, r12d
008CBE47  44 88 44 24 41                  mov byte ptr [rsp + 0x41], r8b
008CBE4C  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
008CBE51  41 0F B6 D9                     movzx ebx, r9b
008CBE55  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
008CBE5A  4C 8B F2                        mov r14, rdx
008CBE5D  48 8B F9                        mov rdi, rcx
008CBE60  48 85 D2                        test rdx, rdx
008CBE63  0F 84 83 01 00 00               je 0x1408cbfec
008CBE69  BA 44 66 6C 74                  mov edx, 0x746c6644
008CBE6E  48 8B CE                        mov rcx, rsi
008CBE71  E8 0A 41 94 FF                  call 0x14020ff80
008CBE76  44 8B A5 C0 00 00 00            mov r12d, dword ptr [rbp + 0xc0]
008CBE7D  4C 8B E8                        mov r13, rax
008CBE80  48 85 C0                        test rax, rax
008CBE83  74 76                           je 0x1408cbefb
008CBE85  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
008CBE8A  45 8B C4                        mov r8d, r12d
008CBE8D  49 8B D6                        mov rdx, r14
008CBE90  48 8B C8                        mov rcx, rax
008CBE93  E8 28 06 00 00                  call 0x1408cc4c0
008CBE98  85 C0                           test eax, eax
008CBE9A  0F 88 07 02 00 00               js 0x1408cc0a7
008CBEA0  44 38 7C 24 40                  cmp byte ptr [rsp + 0x40], r15b
008CBEA5  0F 85 37 03 00 00               jne 0x1408cc1e2
008CBEAB  0F 0D 8E 48 02 00 00            prefetchw byte ptr [rsi + 0x248]
008CBEB2  48 8B 86 48 02 00 00            mov rax, qword ptr [rsi + 0x248]
008CBEB9  48 8B C8                        mov rcx, rax
008CBEBC  49 33 CD                        xor rcx, r13
008CBEBF  48 83 F9 0F                     cmp rcx, 0xf
008CBEC3  0F 83 94 05 00 00               jae 0x1408cc45d
008CBEC9  48 8D 48 01                     lea rcx, [rax + 1]
008CBECD  F0 48 0F B1 8E 48 02 00 00      lock cmpxchg qword ptr [rsi + 0x248], rcx
008CBED6  75 E1                           jne 0x1408cbeb9
008CBED8  83 3D 31 91 6F 00 00            cmp dword ptr [rip + 0x6f9131], 0
008CBEDF  74 15                           je 0x1408cbef6
008CBEE1  33 D2                           xor edx, edx
008CBEE3  49 8D 4D D0                     lea rcx, [r13 - 0x30]
008CBEE7  41 B9 44 66 6C 74               mov r9d, 0x746c6644
008CBEED  44 8D 42 01                     lea r8d, [rdx + 1]
008CBEF1  E8 EE 4A 94 FF                  call 0x1402109e4
008CBEF6  45 84 FF                        test r15b, r15b
008CBEF9  75 08                           jne 0x1408cbf03
008CBEFB  49 8B CE                        mov rcx, r14
008CBEFE  E8 1D 3B 94 FF                  call 0x14020fa20
008CBF03  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
008CBF0C  83 E3 01                        and ebx, 1
008CBF0F  48 C1 E3 02                     shl rbx, 2
008CBF13  41 83 E4 03                     and r12d, 3
008CBF17  49 8B C6                        mov rax, r14
008CBF1A  49 0B DC                        or rbx, r12
008CBF1D  48 83 E0 F8                     and rax, 0xfffffffffffffff8
008CBF21  49 8B D5                        mov rdx, r13
008CBF24  48 8B CF                        mov rcx, rdi
008CBF27  48 0B D8                        or rbx, rax
008CBF2A  E8 B1 D7 C1 FF                  call 0x1404e96e0
008CBF2F  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
008CBF35  A8 08                           test al, 8
008CBF37  0F 85 00 04 00 00               jne 0x1408cc33d
008CBF3D  45 33 FF                        xor r15d, r15d
008CBF40  45 33 E4                        xor r12d, r12d
008CBF43  F0 83 8F A0 05 00 00 08         lock or dword ptr [rdi + 0x5a0], 8
008CBF4B  80 7C 24 41 00                  cmp byte ptr [rsp + 0x41], 0
008CBF50  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008CBF55  48 89 87 48 06 00 00            mov qword ptr [rdi + 0x648], rax
008CBF5C  48 89 9F 38 05 00 00            mov qword ptr [rdi + 0x538], rbx
008CBF63  0F 84 2E 01 00 00               je 0x1408cc097
008CBF69  F0 81 8F A0 05 00 00 00 01 00 00  lock or dword ptr [rdi + 0x5a0], 0x100
008CBF74  41 B8 00 01 00 00               mov r8d, 0x100
008CBF7A  48 8B D6                        mov rdx, rsi
008CBF7D  48 8B CE                        mov rcx, rsi
008CBF80  E8 7B EF B4 FF                  call 0x14041af00
008CBF85  85 C0                           test eax, eax
008CBF87  74 11                           je 0x1408cbf9a
008CBF89  4D 8B CE                        mov r9, r14
008CBF8C  4D 8B C7                        mov r8, r15
008CBF8F  48 8B D7                        mov rdx, rdi
008CBF92  48 8B CE                        mov rcx, rsi
008CBF95  E8 36 0A 00 00                  call 0x1408cc9d0
008CBF9A  49 8B D5                        mov rdx, r13
008CBF9D  48 8B CF                        mov rcx, rdi
008CBFA0  E8 1B D8 C1 FF                  call 0x1404e97c0
008CBFA5  49 8B D5                        mov rdx, r13
008CBFA8  48 8B CF                        mov rcx, rdi
008CBFAB  E8 40 08 00 00                  call 0x1408cc7f0
008CBFB0  4D 85 FF                        test r15, r15
008CBFB3  0F 85 CC 00 00 00               jne 0x1408cc085
008CBFB9  4D 85 E4                        test r12, r12
008CBFBC  0F 85 FE 03 00 00               jne 0x1408cc3c0
008CBFC2  33 C0                           xor eax, eax
008CBFC4  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
008CBFC8  48 33 CC                        xor rcx, rsp
008CBFCB  E8 70 06 DE FF                  call 0x1406ac640
008CBFD0  48 8B 9C 24 B0 01 00 00         mov rbx, qword ptr [rsp + 0x1b0]
008CBFD8  48 81 C4 60 01 00 00            add rsp, 0x160
008CBFDF  41 5F                           pop r15
008CBFE1  41 5E                           pop r14
008CBFE3  41 5D                           pop r13
008CBFE5  41 5C                           pop r12
008CBFE7  5F                              pop rdi
008CBFE8  5E                              pop rsi
008CBFE9  5D                              pop rbp
008CBFEA  C3                              ret
008CBFEB  CC                              int3
008CBFEC  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
008CBFF2  45 33 FF                        xor r15d, r15d
008CBFF5  A8 08                           test al, 8
008CBFF7  74 C9                           je 0x1408cbfc2
008CBFF9  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
008CC002  48 8B D3                        mov rdx, rbx
008CC005  E8 D6 D6 C1 FF                  call 0x1404e96e0
008CC00A  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
008CC010  A8 08                           test al, 8
008CC012  74 5E                           je 0x1408cc072
008CC014  4C 8B BF 38 05 00 00            mov r15, qword ptr [rdi + 0x538]
008CC01B  4C 8B A7 48 06 00 00            mov r12, qword ptr [rdi + 0x648]
008CC022  49 83 E7 F8                     and r15, 0xfffffffffffffff8
008CC026  48 C7 87 48 06 00 00 00 00 00 00  mov qword ptr [rdi + 0x648], 0
008CC031  F0 83 A7 A0 05 00 00 F7         lock and dword ptr [rdi + 0x5a0], 0xfffffff7
008CC039  41 B8 00 01 00 00               mov r8d, 0x100
008CC03F  48 8B D6                        mov rdx, rsi
008CC042  48 8B CE                        mov rcx, rsi
008CC045  E8 B6 EE B4 FF                  call 0x14041af00
008CC04A  85 C0                           test eax, eax
008CC04C  74 24                           je 0x1408cc072
008CC04E  48 8B 0D DB 39 63 00            mov rcx, qword ptr [rip + 0x6339db]
008CC055  48 8D 15 54 53 74 FF            lea rdx, [rip - 0x8bacac]
008CC05C  48 C7 44 24 60 00 00 00 00      mov qword ptr [rsp + 0x60], 0
008CC065  E8 E6 63 AC FF                  call 0x140392450
008CC06A  84 C0                           test al, al
008CC06C  0F 85 4E F7 24 00               jne 0x140b1b7c0
008CC072  48 8B D3                        mov rdx, rbx
008CC075  48 8B CF                        mov rcx, rdi
008CC078  E8 43 D7 C1 FF                  call 0x1404e97c0
008CC07D  48 8B D3                        mov rdx, rbx
008CC080  E9 23 FF FF FF                  jmp 0x1408cbfa8
008CC085  BA 44 66 6C 74                  mov edx, 0x746c6644
008CC08A  49 8B CF                        mov rcx, r15
008CC08D  E8 4E B8 A2 FF                  call 0x1402f78e0
008CC092  E9 22 FF FF FF                  jmp 0x1408cbfb9
008CC097  F0 81 A7 A0 05 00 00 FF FE FF FF  lock and dword ptr [rdi + 0x5a0], 0xfffffeff
008CC0A2  E9 CD FE FF FF                  jmp 0x1408cbf74
008CC0A7  41 83 BE C0 00 00 00 02         cmp dword ptr [r14 + 0xc0], 2
008CC0AF  41 BC 01 00 00 00               mov r12d, 1
008CC0B5  0F 84 8A 03 00 00               je 0x1408cc445
008CC0BB  33 C0                           xor eax, eax
008CC0BD  48 C7 44 24 68 30 00 00 00      mov qword ptr [rsp + 0x68], 0x30
008CC0C6  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
008CC0CA  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
008CC0CF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008CC0D4  0F 57 C0                        xorps xmm0, xmm0
008CC0D7  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008CC0DC  41 B9 02 00 00 00               mov r9d, 2
008CC0E2  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008CC0E7  45 33 C0                        xor r8d, r8d
008CC0EA  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CC0EF  49 8B CE                        mov rcx, r14
008CC0F2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008CC0F7  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
008CC0FC  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
008CC101  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008CC106  F3 0F 7F 45 88                  movdqu xmmword ptr [rbp - 0x78], xmm0
008CC10B  E8 DC C6 FE FF                  call 0x1408b87ec
008CC110  44 8B F8                        mov r15d, eax
008CC113  85 C0                           test eax, eax
008CC115  79 05                           jns 0x1408cc11c
008CC117  45 33 F6                        xor r14d, r14d
008CC11A  EB 6A                           jmp 0x1408cc186
008CC11C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CC121  45 33 C9                        xor r9d, r9d
008CC124  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
008CC12D  45 33 C0                        xor r8d, r8d
008CC130  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
008CC139  33 D2                           xor edx, edx
008CC13B  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
008CC143  E8 58 D6 FE FF                  call 0x1408b97a0
008CC148  44 8B F8                        mov r15d, eax
008CC14B  85 C0                           test eax, eax
008CC14D  78 C8                           js 0x1408cc117
008CC14F  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
008CC154  41 F7 86 C8 00 00 00 00 40 00 00  test dword ptr [r14 + 0xc8], 0x4000
008CC15F  0F 85 6D 02 00 00               jne 0x1408cc3d2
008CC165  4C 8B 05 FC D8 70 00            mov r8, qword ptr [rip + 0x70d8fc]
008CC16C  BA 08 00 00 00                  mov edx, 8
008CC171  49 8B CE                        mov rcx, r14
008CC174  E8 B7 A2 FE FF                  call 0x1408b6430
008CC179  85 C0                           test eax, eax
008CC17B  0F 89 F5 00 00 00               jns 0x1408cc276
008CC181  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
008CC186  45 85 FF                        test r15d, r15d
008CC189  0F 89 AE 02 00 00               jns 0x1408cc43d
008CC18F  0F 0D 8E 48 02 00 00            prefetchw byte ptr [rsi + 0x248]
008CC196  48 8B 86 48 02 00 00            mov rax, qword ptr [rsi + 0x248]
008CC19D  48 8B C8                        mov rcx, rax
008CC1A0  49 33 CD                        xor rcx, r13
008CC1A3  48 83 F9 0F                     cmp rcx, 0xf
008CC1A7  0F 83 C2 02 00 00               jae 0x1408cc46f
008CC1AD  48 8D 48 01                     lea rcx, [rax + 1]
008CC1B1  F0 48 0F B1 8E 48 02 00 00      lock cmpxchg qword ptr [rsi + 0x248], rcx
008CC1BA  75 E1                           jne 0x1408cc19d
008CC1BC  83 3D 4D 8E 6F 00 00            cmp dword ptr [rip + 0x6f8e4d], 0
008CC1C3  74 15                           je 0x1408cc1da
008CC1C5  33 D2                           xor edx, edx
008CC1C7  49 8D 4D D0                     lea rcx, [r13 - 0x30]
008CC1CB  41 B9 44 66 6C 74               mov r9d, 0x746c6644
008CC1D1  44 8D 42 01                     lea r8d, [rdx + 1]
008CC1D5  E8 0A 48 94 FF                  call 0x1402109e4
008CC1DA  41 8B C7                        mov eax, r15d
008CC1DD  E9 E2 FD FF FF                  jmp 0x1408cbfc4
008CC1E2  49 8B CD                        mov rcx, r13
008CC1E5  E8 72 06 BC FF                  call 0x14048c85c
008CC1EA  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008CC1EF  48 8D 55 98                     lea rdx, [rbp - 0x68]
008CC1F3  33 C0                           xor eax, eax
008CC1F5  48 C7 45 98 30 00 00 00         mov qword ptr [rbp - 0x68], 0x30
008CC1FD  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
008CC201  0F 57 C0                        xorps xmm0, xmm0
008CC204  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008CC209  41 B9 02 00 00 00               mov r9d, 2
008CC20F  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
008CC213  45 33 C0                        xor r8d, r8d
008CC216  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
008CC21A  49 8B CE                        mov rcx, r14
008CC21D  48 8D 44 24 58                  lea rax, [rsp + 0x58]
008CC222  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008CC227  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
008CC22C  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
008CC231  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008CC236  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
008CC23B  E8 AC C5 FE FF                  call 0x1408b87ec
008CC240  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008CC244  85 C0                           test eax, eax
008CC246  79 3B                           jns 0x1408cc283
008CC248  45 33 E4                        xor r12d, r12d
008CC24B  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
008CC250  85 C0                           test eax, eax
008CC252  0F 89 C3 00 00 00               jns 0x1408cc31b
008CC258  48 8D 8E 48 02 00 00            lea rcx, [rsi + 0x248]
008CC25F  41 B8 44 66 6C 74               mov r8d, 0x746c6644
008CC265  49 8B D5                        mov rdx, r13
008CC268  E8 83 13 B2 FF                  call 0x1403ed5f0
008CC26D  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
008CC271  E9 4E FD FF FF                  jmp 0x1408cbfc4
008CC276  49 8B CE                        mov rcx, r14
008CC279  E8 22 45 B3 FF                  call 0x1404007a0
008CC27E  E9 FE FE FF FF                  jmp 0x1408cc181
008CC283  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008CC288  45 33 C9                        xor r9d, r9d
008CC28B  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
008CC290  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
008CC295  48 85 C0                        test rax, rax
008CC298  0F 85 C1 00 00 00               jne 0x1408cc35f
008CC29E  49 8B 8C 24 50 04 00 00         mov rcx, qword ptr [r12 + 0x450]
008CC2A6  48 85 C9                        test rcx, rcx
008CC2A9  74 0C                           je 0x1408cc2b7
008CC2AB  33 D2                           xor edx, edx
008CC2AD  E8 BE 65 2B 00                  call 0x140b82870
008CC2B2  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
008CC2B7  4D 89 8C 24 50 04 00 00         mov qword ptr [r12 + 0x450], r9
008CC2BF  45 33 C0                        xor r8d, r8d
008CC2C2  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CC2C7  45 33 C9                        xor r9d, r9d
008CC2CA  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
008CC2D3  33 D2                           xor edx, edx
008CC2D5  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
008CC2DE  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
008CC2E6  E8 B5 D4 FE FF                  call 0x1408b97a0
008CC2EB  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008CC2EF  85 C0                           test eax, eax
008CC2F1  0F 88 51 FF FF FF               js 0x1408cc248
008CC2F7  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CC2FC  F7 81 C8 00 00 00 00 40 00 00   test dword ptr [rcx + 0xc8], 0x4000
008CC306  0F 85 F8 00 00 00               jne 0x1408cc404
008CC30C  E8 E3 A0 FE FF                  call 0x1408b63f4
008CC311  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
008CC316  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
008CC31B  44 38 7C 24 41                  cmp byte ptr [rsp + 0x41], r15b
008CC320  0F 84 5B 01 00 00               je 0x1408cc481
008CC326  49 8B D6                        mov rdx, r14
008CC329  49 8B CC                        mov rcx, r12
008CC32C  E8 D3 8C BA FF                  call 0x140475004
008CC331  44 8B A5 C0 00 00 00            mov r12d, dword ptr [rbp + 0xc0]
008CC338  E9 6E FB FF FF                  jmp 0x1408cbeab
008CC33D  4C 8B BF 38 05 00 00            mov r15, qword ptr [rdi + 0x538]
008CC344  4C 8B A7 48 06 00 00            mov r12, qword ptr [rdi + 0x648]
008CC34B  49 83 E7 F8                     and r15, 0xfffffffffffffff8
008CC34F  48 C7 87 48 06 00 00 00 00 00 00  mov qword ptr [rdi + 0x648], 0
008CC35A  E9 EC FB FF FF                  jmp 0x1408cbf4b
008CC35F  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
008CC363  B9 00 01 00 00                  mov ecx, 0x100
008CC368  41 B8 53 65 53 69               mov r8d, 0x69536553
008CC36E  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
008CC375  8B D0                           mov edx, eax
008CC377  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008CC37B  E8 70 5D 2B 00                  call 0x140b820f0
008CC380  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008CC385  4C 8B C8                        mov r9, rax
008CC388  48 85 C0                        test rax, rax
008CC38B  0F 84 1A 01 00 00               je 0x1408cc4ab
008CC391  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
008CC396  0F B6 42 01                     movzx eax, byte ptr [rdx + 1]
008CC39A  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
008CC3A1  3B 44 24 48                     cmp eax, dword ptr [rsp + 0x48]
008CC3A5  0F 87 F3 FE FF FF               ja 0x1408cc29e
008CC3AB  44 8B C0                        mov r8d, eax
008CC3AE  49 8B C9                        mov rcx, r9
008CC3B1  E8 8A A4 DF FF                  call 0x1406c6840
008CC3B6  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
008CC3BB  E9 DE FE FF FF                  jmp 0x1408cc29e
008CC3C0  BA 44 66 6C 74                  mov edx, 0x746c6644
008CC3C5  49 8B CC                        mov rcx, r12
008CC3C8  E8 13 B5 A2 FF                  call 0x1402f78e0
008CC3CD  E9 F0 FB FF FF                  jmp 0x1408cbfc2
008CC3D2  4D 8B 86 10 03 00 00            mov r8, qword ptr [r14 + 0x310]
008CC3D9  4D 85 C0                        test r8, r8
008CC3DC  0F 84 83 FD FF FF               je 0x1408cc165
008CC3E2  BA FF 01 0F 00                  mov edx, 0xf01ff
008CC3E7  49 8B CE                        mov rcx, r14
008CC3EA  E8 41 A0 FE FF                  call 0x1408b6430
008CC3EF  44 8B F8                        mov r15d, eax
008CC3F2  85 C0                           test eax, eax
008CC3F4  0F 88 A2 00 00 00               js 0x1408cc49c
008CC3FA  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
008CC3FF  E9 61 FD FF FF                  jmp 0x1408cc165
008CC404  4C 8B 81 10 03 00 00            mov r8, qword ptr [rcx + 0x310]
008CC40B  4D 85 C0                        test r8, r8
008CC40E  0F 84 F8 FE FF FF               je 0x1408cc30c
008CC414  BA FF 01 0F 00                  mov edx, 0xf01ff
008CC419  E8 12 A0 FE FF                  call 0x1408b6430
008CC41E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CC423  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008CC427  85 C0                           test eax, eax
008CC429  0F 89 DD FE FF FF               jns 0x1408cc30c
008CC42F  E8 1C CF A2 FF                  call 0x1402f9350
008CC434  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
008CC438  E9 0B FE FF FF                  jmp 0x1408cc248
008CC43D  41 B7 01                        mov r15b, 1
008CC440  E9 66 FA FF FF                  jmp 0x1408cbeab
008CC445  41 8B 86 C4 00 00 00            mov eax, dword ptr [r14 + 0xc4]
008CC44C  41 3B C4                        cmp eax, r12d
008CC44F  0F 8D 66 FC FF FF               jge 0x1408cc0bb
008CC455  44 8B E0                        mov r12d, eax
008CC458  E9 5E FC FF FF                  jmp 0x1408cc0bb
008CC45D  BA 44 66 6C 74                  mov edx, 0x746c6644
008CC462  49 8B CD                        mov rcx, r13
008CC465  E8 76 B4 A2 FF                  call 0x1402f78e0
008CC46A  E9 87 FA FF FF                  jmp 0x1408cbef6
008CC46F  BA 44 66 6C 74                  mov edx, 0x746c6644
008CC474  49 8B CD                        mov rcx, r13
008CC477  E8 64 B4 A2 FF                  call 0x1402f78e0
008CC47C  E9 59 FD FF FF                  jmp 0x1408cc1da
008CC481  4D 8B F4                        mov r14, r12
008CC484  48 C7 44 24 50 00 00 00 00      mov qword ptr [rsp + 0x50], 0
008CC48D  44 8B A5 C0 00 00 00            mov r12d, dword ptr [rbp + 0xc0]
008CC494  41 B7 01                        mov r15b, 1
008CC497  E9 0F FA FF FF                  jmp 0x1408cbeab
008CC49C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CC4A1  E8 AA CE A2 FF                  call 0x1402f9350
008CC4A6  E9 6C FC FF FF                  jmp 0x1408cc117
008CC4AB  B8 9A 00 00 C0                  mov eax, 0xc000009a
008CC4B0  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008CC4B4  E9 8F FD FF FF                  jmp 0x1408cc248
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsImpersonateClient(__int64 a1, __int64 a2, unsigned __int8 a3, unsigned __int8 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m148;
    unsigned __int8 v_stack_m157;
    unsigned __int8 v_stack_m158;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p41;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (352);
    result = (*(unsigned __int64 *)(v_rip + 5499149)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r15 = 0;
    v_r12 = 0;
    v_stack_m157 = a3;
    v_stack_m158 = 0;
    v_stack_m148 = 0;
    if (a2 == 0) goto loc_008CBFEC;
    result = PsReferencePrimaryTokenWithTag(*(unsigned __int64 *)(a1 + 544), (unsigned int)(0x746C6644ULL), a3, a4);
    if (result == 0) goto loc_008CBEFB;
    result = SeTokenCanImpersonate(result, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m158);
    if (sign_flag) goto loc_008CC0A7;
    if (v_stack_m158 != 0) goto loc_008CC1E2;
loc_008CBEAB:
loc_008CBEB9:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 584)) ^ (result);
    if (a1 >= 15) goto loc_008CC45D;
    if (a1 != 15) goto loc_008CBEB9;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 584);
    if ((*(unsigned int *)(v_rip + 7311665)) != 0) {
        a2 = 0;
        a1 = result - 48;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    if (0 == 0) {
        a1 = 0;
        result = ObfReferenceObject(a1, a2, a3, a4);
    }
    v_rbx = (unsigned int)((a4) & (1));
    v_rbx = (v_rbx) << (2);
    v_r12 = (unsigned int)(((unsigned int)(a5)) & (3));
    v_rbx = (v_rbx) | (v_r12);
    result = (0) & (-8);
    v_rbx = (v_rbx) | (result);
    result = PspLockThreadSecurityExclusive(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1440)))) & (8)) != 0) goto loc_008CC33D;
    v_r15 = 0;
    v_r12 = 0;
loc_008CBF4B:
    *(unsigned __int64 *)(a1 + 1608) = v_stack_m148;
    *(unsigned __int64 *)(a1 + 1336) = v_rbx;
    if (v_stack_m157 == 0) goto loc_008CC097;
loc_008CBF74:
    result = PsIsProcessLoggingEnabled(*(unsigned __int64 *)(a1 + 544), *(unsigned __int64 *)(a1 + 544), 256, a4);
    if ((unsigned int)(result) != 0) {
        a4 = 0;
        a3 = 0;
        a2 = a1;
        a1 = *(unsigned __int64 *)(a1 + 544);
        result = EtwTiLogImpersonateClient(a1, a2, a3, a4);
    }
    result = PspUnlockThreadSecurityExclusive(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
loc_008CBFA8:
    result = PspWriteTebImpersonationInfo(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    if (0 != 0) goto loc_008CC085;
loc_008CBFB9:
    if (0 != 0) goto loc_008CC3C0;
loc_008CBFC2:
    result = 0;
loc_008CBFC4:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    v_rsp = (v_rsp) + (352);
    return result;
loc_008CBFEC:
    v_r15 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1440)))) & (8)) == 0) goto loc_008CBFC2;
    result = PspLockThreadSecurityExclusive(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1440)))) & (8)) == 0) goto loc_008CC072;
    v_r15 = (*(unsigned __int64 *)(a1 + 1336)) & (-8);
    *(unsigned __int64 *)(a1 + 1608) = 0;
    result = PsIsProcessLoggingEnabled(*(unsigned __int64 *)(a1 + 544), *(unsigned __int64 *)(a1 + 544), 256, a4);
    if ((unsigned int)(result) == 0) goto loc_008CC072;
    v_stack_p60 = 0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6502875), v_rip - 9153708, 256, a4);
loc_008CC072:
    result = PspUnlockThreadSecurityExclusive(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), 256, a4);
    goto loc_008CBFA8;
loc_008CC085:
    result = ObfDereferenceObjectWithTag(v_r15, (unsigned int)(0x746C6644ULL), 256, a4);
    goto loc_008CBFB9;
loc_008CC097:
    goto loc_008CBF74;
loc_008CC0A7:
    if ((*(unsigned int *)(a2 + 192)) == 2) goto loc_008CC445;
loc_008CC0BB:
    result = 0;
    v_stack_p68 = 48;
    v_stack_m118 = 0;
    v_stack_p48 = 0;
    v_stack_p70 = 0;
    v_stack_p78 = 0;
    a3 = 0;
    v_stack_p38 = v_stack_p48;
    v_stack_p30 = (unsigned __int8)(v_r15);
    v_stack_p28 = (unsigned __int8)(v_r15);
    v_stack_p20 = 1;
    v_stack_m110 = v_xmm0;
    result = SepDuplicateToken(a2, v_stack_p68, a3, 2);
    if (!sign_flag) goto loc_008CC11C;
loc_008CC117:
    v_r14 = 0;
    goto loc_008CC186;
loc_008CC11C:
    a4 = 0;
    v_stack_p30 = 0;
    a3 = 0;
    v_stack_p28 = 0;
    a2 = 0;
    v_stack_p20 = 0;
    result = ObInsertObjectEx(v_stack_p48, a2, a3, a4);
    if (sign_flag) goto loc_008CC117;
    if (((*(unsigned int *)(v_stack_p48 + 200)) & (0x4000ULL)) != 0) goto loc_008CC3D2;
loc_008CC165:
    result = SepAppendAceToTokenObjectAcl(v_stack_p48, 8, *(unsigned __int64 *)(v_rip + 7395580), a4);
    if (!sign_flag) goto loc_008CC276;
loc_008CC181:
loc_008CC186:
    if (!sign_flag) goto loc_008CC43D;
loc_008CC19D:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 584)) ^ (*(unsigned __int64 *)(gs_base + (0 + 392)));
    if (a1 >= 15) goto loc_008CC46F;
    if (a1 != 15) goto loc_008CC19D;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 584);
    if ((*(unsigned int *)(v_rip + 7310925)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392)) - 48;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    goto loc_008CBFC4;
loc_008CC1E2:
    result = SeQueryTokenTrustSid(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_stack_p60 = result;
    result = 0;
    v_stack_m100 = 48;
    v_stack_mE8 = 0;
    v_stack_p58 = 0;
    v_stack_mF8 = 0;
    a3 = 0;
    v_stack_mF0 = 0;
    v_stack_p38 = v_stack_p58;
    v_stack_p30 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    v_stack_p28 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    v_stack_p20 = 1;
    v_stack_mE0 = v_xmm0;
    result = SepDuplicateToken(v_stack_p48, v_stack_m100, a3, 2);
    v_stack_p48 = (unsigned int)(result);
    if (!sign_flag) goto loc_008CC283;
loc_008CC248:
    v_r12 = 0;
    v_stack_p50 = 0;
    if (!sign_flag) goto loc_008CC31B;
    result = ObFastDereferenceObject(*(unsigned __int64 *)(a1 + 544) + 584, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x746C6644ULL), 2);
    goto loc_008CBFC4;
loc_008CC276:
    result = SepSetProcessTrustLabelAceForToken(v_stack_p48, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x746C6644ULL), 2);
    goto loc_008CC181;
loc_008CC283:
    a4 = 0;
    v_stack_p50 = 0;
    if (v_stack_p60 != 0) goto loc_008CC35F;
loc_008CC29E:
    result = v_stack_p60;
    if (*(unsigned __int64 *)(v_stack_p58 + 1104) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p58 + 1104), a2, (unsigned int)(0x746C6644ULL), a4);
        a4 = v_stack_p50;
    }
    *(unsigned __int64 *)(v_stack_p58 + 1104) = a4;
    a3 = 0;
    a4 = 0;
    v_stack_p30 = 0;
    a2 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = ObInsertObjectEx(v_stack_p58, a2, a3, a4);
    v_stack_p48 = (unsigned int)(result);
    if (sign_flag) goto loc_008CC248;
    if (((*(unsigned int *)(v_stack_p58 + 200)) & (0x4000ULL)) != 0) goto loc_008CC404;
loc_008CC30C:
    result = SepFinalizeTokenAcls(v_stack_p58, a2, a3, a4);
    v_stack_p50 = v_stack_p58;
loc_008CC31B:
    if (v_stack_p41 == ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_008CC481;
    result = SeSetTokenTrustLink(v_stack_p58, v_stack_p48, a3, a4);
    goto loc_008CBEAB;
loc_008CC33D:
    v_r15 = (*(unsigned __int64 *)(a1 + 1336)) & (-8);
    *(unsigned __int64 *)(a1 + 1608) = 0;
    goto loc_008CBF4B;
loc_008CC35F:
    v_stack_p48 = (unsigned int)(*(unsigned __int8 *)(result + 1) * 4 + 8);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 1) * 4 + 8)), (unsigned int)(0x69536553ULL), a4);
    v_stack_p50 = result;
    if (result == 0) goto loc_008CC4AB;
    if (((unsigned int)(*(unsigned __int8 *)(v_stack_p60 + 1) * 4 + 8)) > v_stack_p48) goto loc_008CC29E;
    result = memcpy(result, v_stack_p60, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_p60 + 1) * 4 + 8)), result);
    goto loc_008CC29E;
loc_008CC3C0:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 1608), (unsigned int)(0x746C6644ULL), (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_p60 + 1) * 4 + 8)), v_stack_p50);
    goto loc_008CBFC2;
loc_008CC3D2:
    if (*(unsigned __int64 *)(v_stack_p48 + 784) == 0) goto loc_008CC165;
    result = SepAppendAceToTokenObjectAcl(v_stack_p48, (unsigned int)(0xF01FFULL), *(unsigned __int64 *)(v_stack_p48 + 784), v_stack_p50);
    if (sign_flag) goto loc_008CC49C;
    goto loc_008CC165;
loc_008CC404:
    if (*(unsigned __int64 *)(v_stack_p48 + 784) == 0) goto loc_008CC30C;
    result = SepAppendAceToTokenObjectAcl(v_stack_p48, (unsigned int)(0xF01FFULL), *(unsigned __int64 *)(v_stack_p48 + 784), v_stack_p50);
    v_stack_p48 = (unsigned int)(result);
    if (!sign_flag) goto loc_008CC30C;
    result = ObfDereferenceObject(v_stack_p58, (unsigned int)(0xF01FFULL), *(unsigned __int64 *)(v_stack_p48 + 784), v_stack_p50);
    goto loc_008CC248;
loc_008CC43D:
    goto loc_008CBEAB;
loc_008CC445:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p48 + 196)))) >= ((unsigned int)(*(unsigned __int64 *)(a1 + 1608)))) goto loc_008CC0BB;
    goto loc_008CC0BB;
loc_008CC45D:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_stack_p48 + 784), v_stack_p50);
    goto loc_008CBEF6;
loc_008CC46F:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_stack_p48 + 784), v_stack_p50);
    goto loc_008CC1DA;
loc_008CC481:
    v_stack_p50 = 0;
    goto loc_008CBEAB;
loc_008CC49C:
    result = ObfDereferenceObject(v_stack_p48, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_stack_p48 + 784), v_stack_p50);
    goto loc_008CC117;
loc_008CC4AB:
    v_stack_p48 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_008CC248;
}
```

## 5. (Beta) C Style

```c
int64_t PsImpersonateClient(void *Arg1, void *Arg2, uint8_t Arg3, uint8_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m148;
    uint8_t v_stack_m157;
    uint8_t v_stack_m158;
    uint64_t v_stack_m48;
    uint64_t v_stack_m98;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p41;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (352);
    result = (*(uint64_t *)(v_rip + 0x53E90D)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r15 = 0;
    local_r12 = 0;
    v_stack_m157 = Arg3;
    v_stack_m158 = 0;
    v_stack_m148 = 0;
    if (Arg2 == NULL) goto loc_008CBFEC;
    result = PsReferencePrimaryTokenWithTag(*(uint64_t *)(arg1 + 0x220), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    if (result == 0) goto loc_008CBEFB;
    result = SeTokenCanImpersonate(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m158);
    if (sign_flag) goto loc_008CC0A7;
    if (v_stack_m158 != 0) goto loc_008CC1E2;
loc_008CBEAB:
loc_008CBEB9:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x248)) ^ (result);
    if (Arg1 >= 15) goto loc_008CC45D;
    if (Arg1 != 15) goto loc_008CBEB9;
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x248);
    if ((*(uint32_t *)(v_rip + 0x6F9131)) != 0) {
        Arg2 = 0;
        Arg1 = result - 48;
        Arg4 = 0x746C6644ULL;
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    if (0 == 0) {
        Arg1 = 0;
        result = ObfReferenceObject(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (uint32_t)((Arg4) & (1));
    local_rbx = (local_rbx) << (2);
    local_r12 = (uint32_t)(((uint32_t)(Arg5)) & (3));
    local_rbx = (local_rbx) | (local_r12);
    result = (0) & (-8);
    local_rbx = (local_rbx) | (result);
    result = PspLockThreadSecurityExclusive(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5A0)))) & (8)) != 0) goto loc_008CC33D;
    local_r15 = 0;
    local_r12 = 0;
loc_008CBF4B:
    *(uint64_t *)(arg1 + 0x648) = v_stack_m148;
    *(uint64_t *)(arg1 + 0x538) = local_rbx;
    if (v_stack_m157 == 0) goto loc_008CC097;
loc_008CBF74:
    result = PsIsProcessLoggingEnabled(*(uint64_t *)(arg1 + 0x220), *(uint64_t *)(arg1 + 0x220), 256, Arg4);
    if ((uint32_t)(result) != 0) {
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = Arg1;
        Arg1 = *(uint64_t *)(arg1 + 0x220);
        result = EtwTiLogImpersonateClient(Arg1, Arg2, Arg3, Arg4);
    }
    result = PspUnlockThreadSecurityExclusive(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
loc_008CBFA8:
    result = PspWriteTebImpersonationInfo(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    if (0 != 0) goto loc_008CC085;
loc_008CBFB9:
    if (0 != 0) goto loc_008CC3C0;
loc_008CBFC2:
    result = 0;
loc_008CBFC4:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    local_rsp = (local_rsp) + (352);
    return result;
loc_008CBFEC:
    local_r15 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5A0)))) & (8)) == 0) goto loc_008CBFC2;
    result = PspLockThreadSecurityExclusive(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5A0)))) & (8)) == 0) goto loc_008CC072;
    local_r15 = (*(uint64_t *)(arg1 + 0x538)) & (-8);
    *(uint64_t *)(arg1 + 0x648) = 0;
    result = PsIsProcessLoggingEnabled(*(uint64_t *)(arg1 + 0x220), *(uint64_t *)(arg1 + 0x220), 256, Arg4);
    if ((uint32_t)(result) == 0) goto loc_008CC072;
    v_stack_p60 = 0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x6339DB), v_rip - 9153708, 256, Arg4);
loc_008CC072:
    result = PspUnlockThreadSecurityExclusive(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), 256, Arg4);
    goto loc_008CBFA8;
loc_008CC085:
    result = ObfDereferenceObjectWithTag(local_r15, (uint32_t)(0x746C6644ULL), 256, Arg4);
    goto loc_008CBFB9;
loc_008CC097:
    goto loc_008CBF74;
loc_008CC0A7:
    if ((*(uint32_t *)(arg2 + 0xC0)) == 2) goto loc_008CC445;
loc_008CC0BB:
    result = 0;
    v_stack_p68 = 48;
    v_stack_m118 = 0;
    v_stack_p48 = 0;
    v_stack_p70 = 0;
    v_stack_p78 = 0;
    Arg3 = 0;
    v_stack_p38 = v_stack_p48;
    v_stack_p30 = (uint8_t)(local_r15);
    v_stack_p28 = (uint8_t)(local_r15);
    v_stack_p20 = 1;
    v_stack_m110 = v_xmm0;
    result = SepDuplicateToken(Arg2, v_stack_p68, Arg3, 2);
    if (!sign_flag) goto loc_008CC11C;
loc_008CC117:
    local_r14 = 0;
    goto loc_008CC186;
loc_008CC11C:
    Arg4 = 0;
    v_stack_p30 = 0;
    Arg3 = 0;
    v_stack_p28 = 0;
    Arg2 = 0;
    v_stack_p20 = 0;
    result = ObInsertObjectEx(v_stack_p48, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_008CC117;
    if (((*(uint32_t *)(v_stack_p48 + 0xC8)) & (0x4000ULL)) != 0) goto loc_008CC3D2;
loc_008CC165:
    result = SepAppendAceToTokenObjectAcl(v_stack_p48, 8, *(uint64_t *)(v_rip + 0x70D8FC), Arg4);
    if (!sign_flag) goto loc_008CC276;
loc_008CC181:
loc_008CC186:
    if (!sign_flag) goto loc_008CC43D;
loc_008CC19D:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x248)) ^ (*(uint64_t *)(gs_base + (0 + 0x188)));
    if (Arg1 >= 15) goto loc_008CC46F;
    if (Arg1 != 15) goto loc_008CC19D;
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x248);
    if ((*(uint32_t *)(v_rip + 0x6F8E4D)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188)) - 48;
        Arg4 = 0x746C6644ULL;
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_008CBFC4;
loc_008CC1E2:
    result = SeQueryTokenTrustSid(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    v_stack_p60 = result;
    result = 0;
    v_stack_m100 = 48;
    v_stack_mE8 = 0;
    v_stack_p58 = 0;
    v_stack_mF8 = 0;
    Arg3 = 0;
    v_stack_mF0 = 0;
    v_stack_p38 = v_stack_p58;
    v_stack_p30 = (uint8_t)((uint32_t)((uint32_t)(result)));
    v_stack_p28 = (uint8_t)((uint32_t)((uint32_t)(result)));
    v_stack_p20 = 1;
    v_stack_mE0 = v_xmm0;
    result = SepDuplicateToken(v_stack_p48, v_stack_m100, Arg3, 2);
    v_stack_p48 = (uint32_t)(result);
    if (!sign_flag) goto loc_008CC283;
loc_008CC248:
    local_r12 = 0;
    v_stack_p50 = 0;
    if (!sign_flag) goto loc_008CC31B;
    result = ObFastDereferenceObject(*(uint64_t *)(arg1 + 0x220) + 584, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x746C6644ULL), 2);
    goto loc_008CBFC4;
loc_008CC276:
    result = SepSetProcessTrustLabelAceForToken(v_stack_p48, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x746C6644ULL), 2);
    goto loc_008CC181;
loc_008CC283:
    Arg4 = 0;
    v_stack_p50 = 0;
    if (v_stack_p60 != 0) goto loc_008CC35F;
loc_008CC29E:
    result = v_stack_p60;
    if (*(uint64_t *)(v_stack_p58 + 0x450) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p58 + 0x450), Arg2, (uint32_t)(0x746C6644ULL), Arg4);
        Arg4 = v_stack_p50;
    }
    *(uint64_t *)(v_stack_p58 + 0x450) = Arg4;
    Arg3 = 0;
    Arg4 = 0;
    v_stack_p30 = 0;
    Arg2 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = ObInsertObjectEx(v_stack_p58, Arg2, Arg3, Arg4);
    v_stack_p48 = (uint32_t)(result);
    if (sign_flag) goto loc_008CC248;
    if (((*(uint32_t *)(v_stack_p58 + 0xC8)) & (0x4000ULL)) != 0) goto loc_008CC404;
loc_008CC30C:
    result = SepFinalizeTokenAcls(v_stack_p58, Arg2, Arg3, Arg4);
    v_stack_p50 = v_stack_p58;
loc_008CC31B:
    if (v_stack_p41 == ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_008CC481;
    result = SeSetTokenTrustLink(v_stack_p58, v_stack_p48, Arg3, Arg4);
    goto loc_008CBEAB;
loc_008CC33D:
    local_r15 = (*(uint64_t *)(arg1 + 0x538)) & (-8);
    *(uint64_t *)(arg1 + 0x648) = 0;
    goto loc_008CBF4B;
loc_008CC35F:
    v_stack_p48 = (uint32_t)(*(uint8_t *)(result + 0x1) * 4 + 8);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(*(uint8_t *)(result + 0x1) * 4 + 8)), (uint32_t)(0x69536553ULL), Arg4);
    v_stack_p50 = result;
    if (result == 0) goto loc_008CC4AB;
    if (((uint32_t)(*(uint8_t *)(v_stack_p60 + 0x1) * 4 + 8)) > v_stack_p48) goto loc_008CC29E;
    result = memcpy(result, v_stack_p60, (uint32_t)((uint32_t)(*(uint8_t *)(v_stack_p60 + 0x1) * 4 + 8)), result);
    goto loc_008CC29E;
loc_008CC3C0:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x648), (uint32_t)(0x746C6644ULL), (uint32_t)((uint32_t)(*(uint8_t *)(v_stack_p60 + 0x1) * 4 + 8)), v_stack_p50);
    goto loc_008CBFC2;
loc_008CC3D2:
    if (*(uint64_t *)(v_stack_p48 + 0x310) == 0) goto loc_008CC165;
    result = SepAppendAceToTokenObjectAcl(v_stack_p48, (uint32_t)(0xF01FFULL), *(uint64_t *)(v_stack_p48 + 0x310), v_stack_p50);
    if (sign_flag) goto loc_008CC49C;
    goto loc_008CC165;
loc_008CC404:
    if (*(uint64_t *)(v_stack_p48 + 0x310) == 0) goto loc_008CC30C;
    result = SepAppendAceToTokenObjectAcl(v_stack_p48, (uint32_t)(0xF01FFULL), *(uint64_t *)(v_stack_p48 + 0x310), v_stack_p50);
    v_stack_p48 = (uint32_t)(result);
    if (!sign_flag) goto loc_008CC30C;
    result = ObfDereferenceObject(v_stack_p58, (uint32_t)(0xF01FFULL), *(uint64_t *)(v_stack_p48 + 0x310), v_stack_p50);
    goto loc_008CC248;
loc_008CC43D:
    goto loc_008CBEAB;
loc_008CC445:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p48 + 0xC4)))) >= ((uint32_t)(*(uint64_t *)(arg1 + 0x648)))) goto loc_008CC0BB;
    goto loc_008CC0BB;
loc_008CC45D:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x746C6644ULL), *(uint64_t *)(v_stack_p48 + 0x310), v_stack_p50);
    goto loc_008CBEF6;
loc_008CC46F:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x746C6644ULL), *(uint64_t *)(v_stack_p48 + 0x310), v_stack_p50);
    goto loc_008CC1DA;
loc_008CC481:
    v_stack_p50 = 0;
    goto loc_008CBEAB;
loc_008CC49C:
    result = ObfDereferenceObject(v_stack_p48, (uint32_t)(0x746C6644ULL), *(uint64_t *)(v_stack_p48 + 0x310), v_stack_p50);
    goto loc_008CC117;
loc_008CC4AB:
    v_stack_p48 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_008CC248;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x220` | `64` | `R` |
| `Arg1` | `+ 0x538` | `64` | `R` |
| `Arg1` | `+ 0x538` | `64` | `W` |
| `Arg1` | `+ 0x5A0` | `32` | `R` |
| `Arg1` | `+ 0x5A0` | `32` | `R/W` |
| `Arg1` | `+ 0x648` | `64` | `R` |
| `Arg1` | `+ 0x648` | `64` | `W` |
| `Arg2` | `+ 0xC0` | `32` | `R` |
| `Arg2` | `+ 0xC4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008CBE10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
