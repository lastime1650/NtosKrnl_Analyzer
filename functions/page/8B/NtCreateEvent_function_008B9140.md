# NtCreateEvent

- RVA: `0x008B9140`–`0x008B978C` (길이 `1,612` bytes)
- VA: `0x00000001408B9140`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082C4C`
- 디코드: `365`개 명령, `1,612/1,612` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x008B91ED` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x008B920A` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x008B9228` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008B925B` → [ObpCaptureObjectCreateInformation](../89/ObpCaptureObjectCreateInformation_function_0089B930.md) (function, `0x0089B930`)
- `0x008B92B7` → [ObpAllocateObject](../89/ObpAllocateObject_function_00899FF0.md) (function, `0x00899FF0`)
- `0x008B9305` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008B9322` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B9352` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008B936F` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x008B9396` → [ObInsertObjectEx](ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x008B93CE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008B9409` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x008B946C` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (function, `0x0040B6B0`)
- `0x008B94B1` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x008B94C6` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x008B9532` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008B953E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B9563` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x008B9584` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x008B95C1` → [SepAdtPrivilegedServiceAuditAlarm](../87/SepAdtPrivilegedServiceAuditAlarm_function_008714F0.md) (function, `0x008714F0`)
- `0x008B970A` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008B9749` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008B975D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008B976A` → [ObpRegisterObject](../AC/ObpRegisterObject_function_00ACF3EC.md) (function, `0x00ACF3EC`)
- `0x008B9782` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)

### Direct callers
- [sub_008A8E86](../8A/Unknown_function_008A8E86.md) at `0x008A8F34`
- [PfSnOpenVolumesForPrefetch](../8A/PfSnOpenVolumesForPrefetch_function_008AA4AC.md) at `0x008AA5F7`
- [PfSnPrefetchMetadata](../93/PfSnPrefetchMetadata_function_0093B9B4.md) at `0x0093BA47`
- [SepAdtOpenEtwReadyEvent](../AC/SepAdtOpenEtwReadyEvent_function_00AC403C.md) at `0x00AC40A3`
- [FsRtlInitializeSmssEvent](../../init/C2/FsRtlInitializeSmssEvent_function_00C29030.md) at `0x00C29099`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B36D`

### Static image references
- `0x008B9153` → RVA `0x00E0A740` (`.data`; read)
- `0x008B91C3` → RVA `0x00FC6B80` (`ALMOSTRO`; read)
- `0x008B930A` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x008B93E7` → RVA `0x00FD9BD0` (`PAGEDATA`; read)
- `0x008B94AA` → RVA `0x00E67D58` (`.data`; read)
- `0x008B954D` → RVA `0x00FD9AA0` (`PAGEDATA`; read)
- `0x008B95B2` → RVA `0x000013A8` (`.rdata`; read)
- `0x008B95EC` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x008B9602` → RVA `0x00FD8238` (`PAGEDATA`; read)
- `0x008B9678` → RVA `0x00B4BE28` (`SepServicesFilterPrivileges`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x008B91ED` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x008B920A` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x008B9228` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008B9305` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008B9322` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B9352` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008B936F` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x008B93CE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008B946C` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (`PAGE` → `.text`)
  - `0x008B94B1` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x008B9532` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008B953E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B9563` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x008B9584` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x008B970A` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008B9749` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008B975D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008B9782` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008B9140  40 53                           push rbx
008B9142  56                              push rsi
008B9143  57                              push rdi
008B9144  41 54                           push r12
008B9146  41 55                           push r13
008B9148  41 56                           push r14
008B914A  41 57                           push r15
008B914C  48 81 EC D0 00 00 00            sub rsp, 0xd0
008B9153  48 8B 05 E6 15 55 00            mov rax, qword ptr [rip + 0x5515e6]
008B915A  48 33 C4                        xor rax, rsp
008B915D  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
008B9165  45 8B E1                        mov r12d, r9d
008B9168  4D 8B E8                        mov r13, r8
008B916B  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
008B916F  48 8B D1                        mov rdx, rcx
008B9172  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
008B9177  33 C9                           xor ecx, ecx
008B9179  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
008B917E  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
008B9183  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B918C  44 0F B6 B0 32 02 00 00         movzx r14d, byte ptr [rax + 0x232]
008B9194  45 84 F6                        test r14b, r14b
008B9197  74 20                           je 0x1408b91b9
008B9199  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
008B91A3  48 3B D1                        cmp rdx, rcx
008B91A6  48 0F 42 CA                     cmovb rcx, rdx
008B91AA  48 8B 01                        mov rax, qword ptr [rcx]
008B91AD  48 89 01                        mov qword ptr [rcx], rax
008B91B0  33 C9                           xor ecx, ecx
008B91B2  EB 05                           jmp 0x1408b91b9
008B91B4  E9 0A 02 00 00                  jmp 0x1408b93c3
008B91B9  41 83 FC 01                     cmp r12d, 1
008B91BD  0F 87 65 05 00 00               ja 0x1408b9728
008B91C3  4C 8B 3D B6 D9 70 00            mov r15, qword ptr [rip + 0x70d9b6]
008B91CA  0F 57 C0                        xorps xmm0, xmm0
008B91CD  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
008B91D2  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008B91D7  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
008B91E0  48 8B 9E 40 08 00 00            mov rbx, qword ptr [rsi + 0x840]
008B91E7  FF 43 14                        inc dword ptr [rbx + 0x14]
008B91EA  48 8B CB                        mov rcx, rbx
008B91ED  E8 7E 13 E0 FF                  call 0x1406ba570
008B91F2  48 8B F8                        mov rdi, rax
008B91F5  48 85 C0                        test rax, rax
008B91F8  75 36                           jne 0x1408b9230
008B91FA  FF 43 18                        inc dword ptr [rbx + 0x18]
008B91FD  48 8B 9E 48 08 00 00            mov rbx, qword ptr [rsi + 0x848]
008B9204  FF 43 14                        inc dword ptr [rbx + 0x14]
008B9207  48 8B CB                        mov rcx, rbx
008B920A  E8 61 13 E0 FF                  call 0x1406ba570
008B920F  48 8B F8                        mov rdi, rax
008B9212  48 85 C0                        test rax, rax
008B9215  75 19                           jne 0x1408b9230
008B9217  FF 43 18                        inc dword ptr [rbx + 0x18]
008B921A  8B 53 2C                        mov edx, dword ptr [rbx + 0x2c]
008B921D  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
008B9221  44 8B 43 28                     mov r8d, dword ptr [rbx + 0x28]
008B9225  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
008B9228  E8 A3 18 E0 FF                  call 0x1406baad0
008B922D  48 8B F8                        mov rdi, rax
008B9230  48 85 FF                        test rdi, rdi
008B9233  0F 84 01 05 00 00               je 0x1408b973a
008B9239  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
008B923C  89 07                           mov dword ptr [rdi], eax
008B923E  C7 44 24 28 00 00 00 00         mov dword ptr [rsp + 0x28], 0
008B9246  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008B924B  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
008B9250  4D 8B C5                        mov r8, r13
008B9253  41 0F B6 D6                     movzx edx, r14b
008B9257  41 0F B6 CE                     movzx ecx, r14b
008B925B  E8 D0 26 FE FF                  call 0x14089b930
008B9260  8B D8                           mov ebx, eax
008B9262  85 C0                           test eax, eax
008B9264  0F 88 74 02 00 00               js 0x1408b94de
008B926A  8B 0F                           mov ecx, dword ptr [rdi]
008B926C  41 85 4F 48                     test dword ptr [r15 + 0x48], ecx
008B9270  0F 85 DD 04 00 00               jne 0x1408b9753
008B9276  F6 C1 10                        test cl, 0x10
008B9279  0F 85 68 01 00 00               jne 0x1408b93e7
008B927F  41 8B 47 68                     mov eax, dword ptr [r15 + 0x68]
008B9283  41 8B 4F 6C                     mov ecx, dword ptr [r15 + 0x6c]
008B9287  89 47 14                        mov dword ptr [rdi + 0x14], eax
008B928A  89 4F 18                        mov dword ptr [rdi + 0x18], ecx
008B928D  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
008B9296  48 8D 44 24 50                  lea rax, [rsp + 0x50]
008B929B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B92A0  C7 44 24 20 18 00 00 00         mov dword ptr [rsp + 0x20], 0x18
008B92A8  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
008B92AD  4D 8B C7                        mov r8, r15
008B92B0  41 0F B6 D6                     movzx edx, r14b
008B92B4  48 8B CF                        mov rcx, rdi
008B92B7  E8 34 0D FE FF                  call 0x140899ff0
008B92BC  8B D8                           mov ebx, eax
008B92BE  85 C0                           test eax, eax
008B92C0  0F 89 21 03 00 00               jns 0x1408b95e7
008B92C6  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008B92CB  48 85 C9                        test rcx, rcx
008B92CE  74 3A                           je 0x1408b930a
008B92D0  B8 F8 00 00 00                  mov eax, 0xf8
008B92D5  66 39 44 24 62                  cmp word ptr [rsp + 0x62], ax
008B92DA  0F 85 5C 02 00 00               jne 0x1408b953c
008B92E0  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008B92E9  48 8B 8A 50 08 00 00            mov rcx, qword ptr [rdx + 0x850]
008B92F0  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B92F3  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B92F7  66 39 01                        cmp word ptr [rcx], ax
008B92FA  0F 83 D8 03 00 00               jae 0x1408b96d8
008B9300  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
008B9305  E8 A6 12 E0 FF                  call 0x1406ba5b0
008B930A  48 8D 35 3F 95 2C 00            lea rsi, [rip + 0x2c953f]
008B9311  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
008B9315  48 85 C9                        test rcx, rcx
008B9318  74 15                           je 0x1408b932f
008B931A  80 7F 10 01                     cmp byte ptr [rdi + 0x10], 1
008B931E  77 07                           ja 0x1408b9327
008B9320  33 D2                           xor edx, edx
008B9322  E8 49 95 2C 00                  call 0x140b82870
008B9327  48 C7 47 20 00 00 00 00         mov qword ptr [rdi + 0x20], 0
008B932F  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008B9338  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
008B933F  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B9342  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B9346  66 39 01                        cmp word ptr [rcx], ax
008B9349  0F 83 6A 03 00 00               jae 0x1408b96b9
008B934F  48 8B D7                        mov rdx, rdi
008B9352  E8 59 12 E0 FF                  call 0x1406ba5b0
008B9357  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008B935C  85 DB                           test ebx, ebx
008B935E  78 61                           js 0x1408b93c1
008B9360  44 0F B6 84 24 30 01 00 00      movzx r8d, byte ptr [rsp + 0x130]
008B9369  41 8B D4                        mov edx, r12d
008B936C  48 8B CF                        mov rcx, rdi
008B936F  E8 9C 49 B5 FF                  call 0x14040dd10
008B9374  48 8D 44 24 58                  lea rax, [rsp + 0x58]
008B9379  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B937E  33 C0                           xor eax, eax
008B9380  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B9385  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008B9389  45 33 C9                        xor r9d, r9d
008B938C  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
008B9391  33 D2                           xor edx, edx
008B9393  48 8B CF                        mov rcx, rdi
008B9396  E8 05 04 00 00                  call 0x1408b97a0
008B939B  8B D8                           mov ebx, eax
008B939D  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008B93A1  85 C0                           test eax, eax
008B93A3  78 1C                           js 0x1408b93c1
008B93A5  45 84 F6                        test r14b, r14b
008B93A8  0F 84 8B 02 00 00               je 0x1408b9639
008B93AE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008B93B3  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
008B93B8  48 89 0A                        mov qword ptr [rdx], rcx
008B93BB  EB 04                           jmp 0x1408b93c1
008B93BD  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
008B93C1  8B C3                           mov eax, ebx
008B93C3  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
008B93CB  48 33 CC                        xor rcx, rsp
008B93CE  E8 6D 32 DF FF                  call 0x1406ac640
008B93D3  48 81 C4 D0 00 00 00            add rsp, 0xd0
008B93DA  41 5F                           pop r15
008B93DC  41 5E                           pop r14
008B93DE  41 5D                           pop r13
008B93E0  41 5C                           pop r12
008B93E2  5F                              pop rdi
008B93E3  5E                              pop rsi
008B93E4  5B                              pop rbx
008B93E5  C3                              ret
008B93E6  CC                              int3
008B93E7  48 8B 1D E2 07 72 00            mov rbx, qword ptr [rip + 0x7207e2]
008B93EE  0F 57 C0                        xorps xmm0, xmm0
008B93F1  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
008B93F9  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
008B9401  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
008B9409  E8 12 24 FB FF                  call 0x14086b820
008B940E  BE 01 00 00 00                  mov esi, 1
008B9413  89 B4 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], esi
008B941A  89 B4 24 AC 00 00 00            mov dword ptr [rsp + 0xac], esi
008B9421  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
008B9429  C7 84 24 B8 00 00 00 00 00 00 00  mov dword ptr [rsp + 0xb8], 0
008B9434  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
008B943C  45 84 F6                        test r14b, r14b
008B943F  0F 84 06 02 00 00               je 0x1408b964b
008B9445  48 85 DB                        test rbx, rbx
008B9448  0F 85 7D 01 00 00               jne 0x1408b95cb
008B944E  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
008B9456  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
008B945B  44 8B CE                        mov r9d, esi
008B945E  44 8B C6                        mov r8d, esi
008B9461  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
008B9469  48 8B CB                        mov rcx, rbx
008B946C  E8 3F 22 B5 FF                  call 0x14040b6b0
008B9471  44 0F B6 E8                     movzx r13d, al
008B9475  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
008B947D  8B B4 24 A8 00 00 00            mov esi, dword ptr [rsp + 0xa8]
008B9484  45 84 F6                        test r14b, r14b
008B9487  74 35                           je 0x1408b94be
008B9489  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
008B9491  48 85 DB                        test rbx, rbx
008B9494  48 0F 45 CB                     cmovne rcx, rbx
008B9498  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
008B949F  48 8B 01                        mov rax, qword ptr [rcx]
008B94A2  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008B94A7  48 8B D0                        mov rdx, rax
008B94AA  48 8B 0D A7 E8 5A 00            mov rcx, qword ptr [rip + 0x5ae8a7]
008B94B1  E8 1A 76 B4 FF                  call 0x140400ad0
008B94B6  84 C0                           test al, al
008B94B8  0F 84 8A 00 00 00               je 0x1408b9548
008B94BE  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
008B94C6  E8 45 22 FB FF                  call 0x14086b710
008B94CB  45 84 ED                        test r13b, r13b
008B94CE  0F 85 AB FD FF FF               jne 0x1408b927f
008B94D4  BB 61 00 00 C0                  mov ebx, 0xc0000061
008B94D9  E9 E8 FD FF FF                  jmp 0x1408b92c6
008B94DE  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008B94E7  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
008B94EE  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B94F1  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B94F5  66 39 01                        cmp word ptr [rcx], ax
008B94F8  0F 82 51 FE FF FF               jb 0x1408b934f
008B94FE  FF 41 20                        inc dword ptr [rcx + 0x20]
008B9501  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
008B9508  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B950B  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B950F  66 39 01                        cmp word ptr [rcx], ax
008B9512  0F 82 37 FE FF FF               jb 0x1408b934f
008B9518  48 8D 35 31 93 2C 00            lea rsi, [rip + 0x2c9331]
008B951F  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
008B9523  FF 41 20                        inc dword ptr [rcx + 0x20]
008B9526  48 8B CF                        mov rcx, rdi
008B9529  48 3B C6                        cmp rax, rsi
008B952C  0F 85 17 02 00 00               jne 0x1408b9749
008B9532  E8 19 93 2C 00                  call 0x140b82850
008B9537  E9 1B FE FF FF                  jmp 0x1408b9357
008B953C  33 D2                           xor edx, edx
008B953E  E8 2D 93 2C 00                  call 0x140b82870
008B9543  E9 C2 FD FF FF                  jmp 0x1408b930a
008B9548  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
008B954D  48 8B 05 4C 05 72 00            mov rax, qword ptr [rip + 0x72054c]
008B9554  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
008B955C  48 8B 88 88 01 00 00            mov rcx, qword ptr [rax + 0x188]
008B9563  E8 68 75 B4 FF                  call 0x140400ad0
008B9568  84 C0                           test al, al
008B956A  0F 85 92 00 00 00               jne 0x1408b9602
008B9570  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
008B9575  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
008B957D  48 8B 89 80 01 00 00            mov rcx, qword ptr [rcx + 0x180]
008B9584  E8 47 75 B4 FF                  call 0x140400ad0
008B9589  84 C0                           test al, al
008B958B  75 75                           jne 0x1408b9602
008B958D  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
008B9592  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
008B959A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B959F  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
008B95A7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B95AC  4C 8B CB                        mov r9, rbx
008B95AF  45 33 C0                        xor r8d, r8d
008B95B2  48 8D 15 EF 7D 74 FF            lea rdx, [rip - 0x8b8211]
008B95B9  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
008B95C1  E8 2A 7F FB FF                  call 0x1408714f0
008B95C6  E9 F3 FE FF FF                  jmp 0x1408b94be
008B95CB  83 BC 24 88 00 00 00 02         cmp dword ptr [rsp + 0x88], 2
008B95D3  0F 8C 59 01 00 00               jl 0x1408b9732
008B95D9  48 85 DB                        test rbx, rbx
008B95DC  0F 84 6C FE FF FF               je 0x1408b944e
008B95E2  E9 6F FE FF FF                  jmp 0x1408b9456
008B95E7  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
008B95EC  83 3D 1D BA 70 00 00            cmp dword ptr [rip + 0x70ba1d], 0
008B95F3  0F 85 6E 01 00 00               jne 0x1408b9767
008B95F9  48 83 C7 30                     add rdi, 0x30
008B95FD  E9 5A FD FF FF                  jmp 0x1408b935c
008B9602  4C 8B 1D 2F EC 71 00            mov r11, qword ptr [rip + 0x71ec2f]
008B9609  45 33 D2                        xor r10d, r10d
008B960C  85 F6                           test esi, esi
008B960E  0F 84 AA FE FF FF               je 0x1408b94be
008B9614  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
008B961C  44 8B CE                        mov r9d, esi
008B961F  49 8B CB                        mov rcx, r11
008B9622  44 8B 02                        mov r8d, dword ptr [rdx]
008B9625  48 8B 01                        mov rax, qword ptr [rcx]
008B9628  44 3B 00                        cmp r8d, dword ptr [rax]
008B962B  74 27                           je 0x1408b9654
008B962D  48 83 C1 08                     add rcx, 8
008B9631  48 83 39 00                     cmp qword ptr [rcx], 0
008B9635  75 EE                           jne 0x1408b9625
008B9637  EB 26                           jmp 0x1408b965f
008B9639  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008B963E  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
008B9643  48 89 02                        mov qword ptr [rdx], rax
008B9646  E9 76 FD FF FF                  jmp 0x1408b93c1
008B964B  44 0F B6 EE                     movzx r13d, sil
008B964F  E9 30 FE FF FF                  jmp 0x1408b9484
008B9654  8B 40 04                        mov eax, dword ptr [rax + 4]
008B9657  39 42 04                        cmp dword ptr [rdx + 4], eax
008B965A  75 D1                           jne 0x1408b962d
008B965C  41 FF C2                        inc r10d
008B965F  48 83 C2 0C                     add rdx, 0xc
008B9663  49 83 E9 01                     sub r9, 1
008B9667  75 B6                           jne 0x1408b961f
008B9669  85 F6                           test esi, esi
008B966B  74 3E                           je 0x1408b96ab
008B966D  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
008B9675  44 8B C6                        mov r8d, esi
008B9678  4C 8D 1D A9 27 29 00            lea r11, [rip + 0x2927a9]
008B967F  49 8B D3                        mov rdx, r11
008B9682  44 8B 09                        mov r9d, dword ptr [rcx]
008B9685  48 8B 05 9C 27 29 00            mov rax, qword ptr [rip + 0x29279c]
008B968C  44 3B 08                        cmp r9d, dword ptr [rax]
008B968F  0F 84 7F 00 00 00               je 0x1408b9714
008B9695  48 83 C2 08                     add rdx, 8
008B9699  48 8B 02                        mov rax, qword ptr [rdx]
008B969C  48 85 C0                        test rax, rax
008B969F  75 EB                           jne 0x1408b968c
008B96A1  48 83 C1 0C                     add rcx, 0xc
008B96A5  49 83 E8 01                     sub r8, 1
008B96A9  75 D4                           jne 0x1408b967f
008B96AB  44 3B D6                        cmp r10d, esi
008B96AE  0F 84 0A FE FF FF               je 0x1408b94be
008B96B4  E9 D4 FE FF FF                  jmp 0x1408b958d
008B96B9  FF 41 20                        inc dword ptr [rcx + 0x20]
008B96BC  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
008B96C3  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B96C6  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B96CA  66 39 01                        cmp word ptr [rcx], ax
008B96CD  0F 82 7C FC FF FF               jb 0x1408b934f
008B96D3  E9 47 FE FF FF                  jmp 0x1408b951f
008B96D8  FF 41 20                        inc dword ptr [rcx + 0x20]
008B96DB  48 8B 8A 58 08 00 00            mov rcx, qword ptr [rdx + 0x858]
008B96E2  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B96E5  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B96E9  66 39 01                        cmp word ptr [rcx], ax
008B96EC  0F 82 0E FC FF FF               jb 0x1408b9300
008B96F2  FF 41 20                        inc dword ptr [rcx + 0x20]
008B96F5  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
008B96F9  48 8D 35 50 91 2C 00            lea rsi, [rip + 0x2c9150]
008B9700  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008B9705  48 3B C6                        cmp rax, rsi
008B9708  75 53                           jne 0x1408b975d
008B970A  E8 41 91 2C 00                  call 0x140b82850
008B970F  E9 FD FB FF FF                  jmp 0x1408b9311
008B9714  8B 40 04                        mov eax, dword ptr [rax + 4]
008B9717  39 41 04                        cmp dword ptr [rcx + 4], eax
008B971A  0F 85 75 FF FF FF               jne 0x1408b9695
008B9720  41 FF C2                        inc r10d
008B9723  E9 79 FF FF FF                  jmp 0x1408b96a1
008B9728  B8 0D 00 00 C0                  mov eax, 0xc000000d
008B972D  E9 91 FC FF FF                  jmp 0x1408b93c3
008B9732  45 32 ED                        xor r13b, r13b
008B9735  E9 4A FD FF FF                  jmp 0x1408b9484
008B973A  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008B973F  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008B9744  E9 13 FC FF FF                  jmp 0x1408b935c
008B9749  E8 82 13 E0 FF                  call 0x1406baad0
008B974E  E9 04 FC FF FF                  jmp 0x1408b9357
008B9753  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008B9758  E9 69 FB FF FF                  jmp 0x1408b92c6
008B975D  E8 6E 13 E0 FF                  call 0x1406baad0
008B9762  E9 AA FB FF FF                  jmp 0x1408b9311
008B9767  48 8B CF                        mov rcx, rdi
008B976A  E8 7D 5C 21 00                  call 0x140acf3ec
008B976F  41 B9 44 66 6C 74               mov r9d, 0x746c6644
008B9775  41 B8 01 00 00 00               mov r8d, 1
008B977B  41 0F B6 D0                     movzx edx, r8b
008B977F  48 8B CF                        mov rcx, rdi
008B9782  E8 5D 72 95 FF                  call 0x1402109e4
008B9787  E9 6D FE FF FF                  jmp 0x1408b95f9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCreateEvent(__int64 a1, int a2, __int64 a3, int a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int16 v_stack_mA6;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA0;
    unsigned int v_stack_pA8;
    unsigned int v_stack_pAC;
    unsigned __int64 v_stack_pB0;
    unsigned int v_stack_pB8;

    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 5576166)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mC8 = a2;
    v_stack_m90 = a1;
    a1 = 0;
    v_stack_mC0 = 0;
    v_stack_mB0 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008B91B9;
    if (0 < 0) { a1 = 0; }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    a1 = 0;
    goto loc_008B91B9;
loc_008B91B9:
    if (((unsigned int)((unsigned int)(a4))) > 1) goto loc_008B9728;
    v_stack_mA8 = v_xmm0;
    v_stack_mB8 = 0;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a1, a3, a4);
    if (result != 0) goto loc_008B9230;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120), a1, a3, a4);
    v_rdi = result;
    if (result == 0) {
        a2 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 44);
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 48);
        a3 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 40);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 36);
        result = guard_dispatch_icall(a1, a2, a3, a4);
        v_rdi = result;
    }
    if (v_rdi == 0) goto loc_008B973A;
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)));
    v_stack_mE0 = 0;
    v_stack_mE8 = v_rdi;
    result = ObpCaptureObjectCreateInformation((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, v_stack_mA8);
    if (sign_flag) goto loc_008B94DE;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7395766) + 72)) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi))))) != 0) goto loc_008B9753;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi)))) & (16)) != 0) goto loc_008B93E7;
loc_008B927F:
    *(unsigned int *)(v_rdi + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7395766) + 104)));
    *(unsigned int *)(v_rdi + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7395766) + 108)));
    v_stack_mD8 = 0;
    v_stack_mE0 = v_stack_mB8;
    v_stack_mE8 = 24;
    result = ObpAllocateObject(v_rdi, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_rip + 7395766), v_stack_mA8);
    if (!sign_flag) goto loc_008B95E7;
loc_008B92C6:
    if (v_stack_mA0 == 0) goto loc_008B930A;
    if (v_stack_mA6 != 248) goto loc_008B953C;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128) + 16)))) goto loc_008B96D8;
loc_008B9300:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128), v_stack_mA0, *(unsigned __int64 *)(v_rip + 7395766), v_stack_mA8);
loc_008B930A:
loc_008B9311:
    if (*(unsigned __int64 *)(v_rdi + 32) == 0) goto loc_008B932F;
    if ((*(unsigned __int8 *)(v_rdi + 16)) <= 1) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rdi + 32), a2, *(unsigned __int64 *)(v_rip + 7395766), v_stack_mA8);
    }
    *(unsigned __int64 *)(v_rdi + 32) = 0;
loc_008B932F:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_008B96B9;
loc_008B934F:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), v_rdi, *(unsigned __int64 *)(v_rip + 7395766), v_stack_mA8);
loc_008B9357:
loc_008B935C:
    if (sign_flag) goto loc_008B93C1;
    result = KeInitializeEvent(v_stack_mC0, (unsigned int)((unsigned int)((unsigned int)(a4))), a5, v_stack_mA8);
    v_stack_mD8 = v_stack_mB0;
    result = 0;
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    a4 = 0;
    a2 = 0;
    result = ObInsertObjectEx(v_stack_mC0, a2, (unsigned int)(v_stack_mC8), a4);
    v_stack_mC8 = (unsigned int)(result);
    if (sign_flag) goto loc_008B93C1;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008B9639;
    *(unsigned __int64 *)(v_stack_m90) = v_stack_mB0;
    goto loc_008B93C1;
loc_008B93C1:
loc_008B93C3:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m90, (unsigned int)(v_stack_mC8), a4);
    v_rsp = (v_rsp) + (208);
    return result;
loc_008B93E7:
    v_stack_p80 = v_xmm0;
    v_stack_p90 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_p80, v_stack_m90, (unsigned int)(v_stack_mC8), a4);
    v_stack_pA8 = 1;
    v_stack_pAC = 1;
    v_stack_pB0 = *(unsigned __int64 *)(v_rip + 7473122);
    v_stack_pB8 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008B964B;
    if (v_stack_p80 != 0) goto loc_008B95CB;
loc_008B944E:
loc_008B9456:
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = SepPrivilegeCheck(v_stack_p90, v_stack_pB0, 1, 1);
loc_008B9484:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008B94BE;
    a1 = v_stack_p90;
    if (v_stack_p80 != 0) { a1 = v_stack_p80; }
    v_stack_p70 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152));
    result = RtlEqualSid(*(unsigned __int64 *)(v_rip + 5957799), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)), 1, 1);
    if ((unsigned __int8)(result) == 0) goto loc_008B9548;
loc_008B94BE:
    result = SeReleaseSubjectContext(v_stack_p80, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)), 1, 1);
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_008B927F;
    goto loc_008B92C6;
loc_008B94DE:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_008B934F;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 16)))) goto loc_008B934F;
loc_008B951F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 56)) != (v_rip + 2921265)) goto loc_008B9749;
    result = ExFreePool(v_stack_mC0, *(unsigned __int64 *)(gs_base + (0 + 32)), 1, 1);
    goto loc_008B9357;
loc_008B953C:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mC0, a2, 1, 1);
    goto loc_008B930A;
loc_008B9548:
    v_stack_pA0 = *(unsigned __int64 *)(v_rip + 7472460);
    result = RtlEqualSid(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7472460) + 392), v_stack_p70, 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_008B9602;
    result = RtlEqualSid(*(unsigned __int64 *)(v_stack_pA0 + 384), v_stack_p70, 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_008B9602;
loc_008B958D:
    v_stack_p30 = (unsigned __int8)((unsigned __int8)(result));
    v_stack_p28 = v_stack_pA8;
    v_stack_p20 = v_stack_p90;
    a3 = 0;
    result = SepAdtPrivilegedServiceAuditAlarm(v_stack_p80, v_rip - 9142801, a3, (unsigned int)(0xC0000061ULL));
    goto loc_008B94BE;
loc_008B95CB:
    if (v_stack_p88 < 2) goto loc_008B9732;
    if ((unsigned int)(0xC0000061ULL) == 0) goto loc_008B944E;
    goto loc_008B9456;
loc_008B95E7:
    if ((*(unsigned int *)(v_rip + 7387677)) != 0) goto loc_008B9767;
loc_008B95F9:
    v_rdi = (v_stack_p50) + (48);
    goto loc_008B935C;
loc_008B9602:
    v_r10 = 0;
    if ((unsigned int)(v_rip + 2921265) == 0) goto loc_008B94BE;
loc_008B961F:
loc_008B9625:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pB0)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7466031))))) goto loc_008B9654;
loc_008B962D:
    a1 = (*(unsigned __int64 *)(v_rip + 7466031)) + (8);
    if ((*(unsigned __int64 *)(a1)) != 0) goto loc_008B9625;
    goto loc_008B965F;
loc_008B9639:
    *(unsigned __int64 *)(v_stack_p78) = v_stack_p58;
    goto loc_008B93C1;
loc_008B964B:
    goto loc_008B9484;
loc_008B9654:
    if ((*(unsigned int *)(v_stack_p78 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 4))))) goto loc_008B962D;
    v_r10 = (unsigned int)((v_r10) + 1);
loc_008B965F:
    a2 = (v_stack_p78) + (12);
    a4 = ((unsigned int)((unsigned int)(v_rip + 2921265))) - (1);
    if (condition_is_not_equal) goto loc_008B961F;
    if ((unsigned int)(v_rip + 2921265) == 0) goto loc_008B96AB;
loc_008B967F:
loc_008B968C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pB0)))) == (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2697116)))) goto loc_008B9714;
loc_008B9695:
    a2 = (v_rip + 2697129) + (8);
    if (*(unsigned __int64 *)(a2) != 0) goto loc_008B968C;
loc_008B96A1:
    a1 = (v_stack_pB0) + (12);
    a3 = ((unsigned int)((unsigned int)(v_rip + 2921265))) - (1);
    if (condition_is_not_equal) goto loc_008B967F;
loc_008B96AB:
    if (((unsigned int)(v_r10)) == ((unsigned int)(v_rip + 2921265))) goto loc_008B94BE;
    goto loc_008B958D;
loc_008B96B9:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2120) + 16)))) goto loc_008B934F;
    goto loc_008B951F;
loc_008B96D8:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2136))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2136) + 16)))) goto loc_008B9300;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2136) + 56)) != (v_rip + 2920784)) goto loc_008B975D;
    result = ExFreePool(v_stack_p68, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_pB0)));
    goto loc_008B9311;
loc_008B9714:
    if ((*(unsigned int *)(v_stack_p68 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4))))) goto loc_008B9695;
    v_r10 = (unsigned int)((v_r10) + 1);
    goto loc_008B96A1;
loc_008B9728:
    goto loc_008B93C3;
loc_008B9732:
    v_r13 = 0;
    goto loc_008B9484;
loc_008B973A:
    goto loc_008B935C;
loc_008B9749:
    result = guard_dispatch_icall(v_stack_p68, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_pB0)));
    goto loc_008B9357;
loc_008B9753:
    goto loc_008B92C6;
loc_008B975D:
    result = guard_dispatch_icall(v_stack_p68, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_pB0)));
    goto loc_008B9311;
loc_008B9767:
    result = ObpRegisterObject(v_stack_p48, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_pB0)));
    result = ObpPushStackInfo(v_stack_p48, 1, 1, (unsigned int)(0x746C6644ULL));
    goto loc_008B95F9;
}
```

## 5. (Beta) C Style

```c
int64_t NtCreateEvent(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint16_t v_stack_mA6;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint32_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA0;
    uint32_t v_stack_pA8;
    uint32_t v_stack_pAC;
    uint64_t v_stack_pB0;
    uint32_t v_stack_pB8;

    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x5515E6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mC8 = Arg2;
    v_stack_m90 = Arg1;
    Arg1 = 0;
    v_stack_mC0 = 0;
    v_stack_mB0 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008B91B9;
    if (0 < 0) { Arg1 = 0; }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    Arg1 = 0;
    goto loc_008B91B9;
loc_008B91B9:
    if (((uint32_t)((uint32_t)(Arg4))) > 1) goto loc_008B9728;
    v_stack_mA8 = v_xmm0;
    v_stack_mB8 = 0;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg1, Arg3, Arg4);
    if (result != 0) goto loc_008B9230;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848), Arg1, Arg3, Arg4);
    local_rdi = result;
    if (result == 0) {
        Arg2 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x2C);
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x30);
        Arg3 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x28);
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x24);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        local_rdi = result;
    }
    if (local_rdi == 0) goto loc_008B973A;
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)));
    v_stack_mE0 = 0;
    v_stack_mE8 = local_rdi;
    result = ObpCaptureObjectCreateInformation((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, v_stack_mA8);
    if (sign_flag) goto loc_008B94DE;
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0x70D9B6) + 0x48)) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi))))) != 0) goto loc_008B9753;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi)))) & (16)) != 0) goto loc_008B93E7;
loc_008B927F:
    *(uint32_t *)(local_rdi + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x70D9B6) + 0x68)));
    *(uint32_t *)(local_rdi + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x70D9B6) + 0x6C)));
    v_stack_mD8 = 0;
    v_stack_mE0 = v_stack_mB8;
    v_stack_mE8 = 24;
    result = ObpAllocateObject(local_rdi, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_rip + 0x70D9B6), v_stack_mA8);
    if (!sign_flag) goto loc_008B95E7;
loc_008B92C6:
    if (v_stack_mA0 == 0) goto loc_008B930A;
    if (v_stack_mA6 != 248) goto loc_008B953C;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850) + 0x10)))) goto loc_008B96D8;
loc_008B9300:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850), v_stack_mA0, *(uint64_t *)(v_rip + 0x70D9B6), v_stack_mA8);
loc_008B930A:
loc_008B9311:
    if (*(uint64_t *)(local_rdi + 0x20) == 0) goto loc_008B932F;
    if ((*(uint8_t *)(local_rdi + 0x10)) <= 1) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rdi + 0x20), Arg2, *(uint64_t *)(v_rip + 0x70D9B6), v_stack_mA8);
    }
    *(uint64_t *)(local_rdi + 0x20) = 0;
loc_008B932F:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_008B96B9;
loc_008B934F:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), local_rdi, *(uint64_t *)(v_rip + 0x70D9B6), v_stack_mA8);
loc_008B9357:
loc_008B935C:
    if (sign_flag) goto loc_008B93C1;
    result = KeInitializeEvent(v_stack_mC0, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg5, v_stack_mA8);
    v_stack_mD8 = v_stack_mB0;
    result = 0;
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = ObInsertObjectEx(v_stack_mC0, Arg2, (uint32_t)(v_stack_mC8), Arg4);
    v_stack_mC8 = (uint32_t)(result);
    if (sign_flag) goto loc_008B93C1;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008B9639;
    *(uint64_t *)(v_stack_m90) = v_stack_mB0;
    goto loc_008B93C1;
loc_008B93C1:
loc_008B93C3:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m90, (uint32_t)(v_stack_mC8), Arg4);
    local_rsp = (local_rsp) + (208);
    return result;
loc_008B93E7:
    v_stack_p80 = v_xmm0;
    v_stack_p90 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_p80, v_stack_m90, (uint32_t)(v_stack_mC8), Arg4);
    v_stack_pA8 = 1;
    v_stack_pAC = 1;
    v_stack_pB0 = *(uint64_t *)(v_rip + 0x7207E2);
    v_stack_pB8 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008B964B;
    if (v_stack_p80 != 0) goto loc_008B95CB;
loc_008B944E:
loc_008B9456:
    v_stack_p20 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = SepPrivilegeCheck(v_stack_p90, v_stack_pB0, 1, 1);
loc_008B9484:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008B94BE;
    Arg1 = v_stack_p90;
    if (v_stack_p80 != 0) { Arg1 = v_stack_p80; }
    v_stack_p70 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98));
    result = RtlEqualSid(*(uint64_t *)(v_rip + 0x5AE8A7), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98)), 1, 1);
    if ((uint8_t)(result) == 0) goto loc_008B9548;
loc_008B94BE:
    result = SeReleaseSubjectContext(v_stack_p80, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98)), 1, 1);
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_008B927F;
    goto loc_008B92C6;
loc_008B94DE:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_008B934F;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x10)))) goto loc_008B934F;
loc_008B951F:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x38)) != (v_rip + 2921265)) goto loc_008B9749;
    result = ExFreePool(v_stack_mC0, *(uint64_t *)(gs_base + (0 + 0x20)), 1, 1);
    goto loc_008B9357;
loc_008B953C:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mC0, Arg2, 1, 1);
    goto loc_008B930A;
loc_008B9548:
    v_stack_pA0 = *(uint64_t *)(v_rip + 0x72054C);
    result = RtlEqualSid(*(uint64_t *)(*(uint64_t *)(v_rip + 0x72054C) + 0x188), v_stack_p70, 1, 1);
    if ((uint8_t)(result) != 0) goto loc_008B9602;
    result = RtlEqualSid(*(uint64_t *)(v_stack_pA0 + 0x180), v_stack_p70, 1, 1);
    if ((uint8_t)(result) != 0) goto loc_008B9602;
loc_008B958D:
    v_stack_p30 = (uint8_t)((uint8_t)(result));
    v_stack_p28 = v_stack_pA8;
    v_stack_p20 = v_stack_p90;
    Arg3 = 0;
    result = SepAdtPrivilegedServiceAuditAlarm(v_stack_p80, v_rip - 9142801, Arg3, (uint32_t)(0xC0000061ULL));
    goto loc_008B94BE;
loc_008B95CB:
    if (v_stack_p88 < 2) goto loc_008B9732;
    if ((uint32_t)(0xC0000061ULL) == 0) goto loc_008B944E;
    goto loc_008B9456;
loc_008B95E7:
    if ((*(uint32_t *)(v_rip + 0x70BA1D)) != 0) goto loc_008B9767;
loc_008B95F9:
    local_rdi = (v_stack_p50) + (48);
    goto loc_008B935C;
loc_008B9602:
    local_r10 = 0;
    if ((uint32_t)(v_rip + 2921265) == 0) goto loc_008B94BE;
loc_008B961F:
loc_008B9625:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pB0)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x71EC2F))))) goto loc_008B9654;
loc_008B962D:
    Arg1 = (*(uint64_t *)(v_rip + 0x71EC2F)) + (8);
    if ((*(uint64_t *)(Arg1)) != 0) goto loc_008B9625;
    goto loc_008B965F;
loc_008B9639:
    *(uint64_t *)(v_stack_p78) = v_stack_p58;
    goto loc_008B93C1;
loc_008B964B:
    goto loc_008B9484;
loc_008B9654:
    if ((*(uint32_t *)(v_stack_p78 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x4))))) goto loc_008B962D;
    local_r10 = (uint32_t)((local_r10) + 1);
loc_008B965F:
    Arg2 = (v_stack_p78) + (12);
    Arg4 = ((uint32_t)((uint32_t)(v_rip + 2921265))) - (1);
    if (condition_is_not_equal) goto loc_008B961F;
    if ((uint32_t)(v_rip + 2921265) == 0) goto loc_008B96AB;
loc_008B967F:
loc_008B968C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pB0)))) == (*(uint32_t *)(*(uint64_t *)(v_rip + 0x29279C)))) goto loc_008B9714;
loc_008B9695:
    Arg2 = (v_rip + 2697129) + (8);
    if (*(uint64_t *)(Arg2) != 0) goto loc_008B968C;
loc_008B96A1:
    Arg1 = (v_stack_pB0) + (12);
    Arg3 = ((uint32_t)((uint32_t)(v_rip + 2921265))) - (1);
    if (condition_is_not_equal) goto loc_008B967F;
loc_008B96AB:
    if (((uint32_t)(local_r10)) == ((uint32_t)(v_rip + 2921265))) goto loc_008B94BE;
    goto loc_008B958D;
loc_008B96B9:
    if ((*(uint16_t *)(*(uint64_t *)(Arg2 + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg2 + 0x848) + 0x10)))) goto loc_008B934F;
    goto loc_008B951F;
loc_008B96D8:
    if ((*(uint16_t *)(*(uint64_t *)(Arg2 + 0x858))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg2 + 0x858) + 0x10)))) goto loc_008B9300;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x858) + 0x38)) != (v_rip + 2920784)) goto loc_008B975D;
    result = ExFreePool(v_stack_p68, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_pB0)));
    goto loc_008B9311;
loc_008B9714:
    if ((*(uint32_t *)(v_stack_p68 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))))) goto loc_008B9695;
    local_r10 = (uint32_t)((local_r10) + 1);
    goto loc_008B96A1;
loc_008B9728:
    goto loc_008B93C3;
loc_008B9732:
    local_r13 = 0;
    goto loc_008B9484;
loc_008B973A:
    goto loc_008B935C;
loc_008B9749:
    result = guard_dispatch_icall(v_stack_p68, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_pB0)));
    goto loc_008B9357;
loc_008B9753:
    goto loc_008B92C6;
loc_008B975D:
    result = guard_dispatch_icall(v_stack_p68, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_pB0)));
    goto loc_008B9311;
loc_008B9767:
    result = ObpRegisterObject(v_stack_p48, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_pB0)));
    result = ObpPushStackInfo(v_stack_p48, 1, 1, (uint32_t)(0x746C6644ULL));
    goto loc_008B95F9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B9140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
