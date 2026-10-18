# IopTrackLink

- RVA: `0x00A36764`–`0x00A37188` (길이 `2,596` bytes)
- VA: `0x0000000140A36764`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AD9E4`
- 디코드: `564`개 명령, `2,596/2,596` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **59**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A367D9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A367EB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A36811` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A36826` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A368A7` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A368E5` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36943` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36968` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (function, `0x006BA6F0`)
- `0x00A36976` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A3698C` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A369A5` → [IopGetVolumeId](IopGetVolumeId_function_00A372CC.md) (function, `0x00A372CC`)
- `0x00A369C3` → [IopGetVolumeId](IopGetVolumeId_function_00A372CC.md) (function, `0x00A372CC`)
- `0x00A369E4` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36AA6` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36AD6` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36AFC` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36B5D` → [IopMarshalIds](../71/IopMarshalIds_function_0071BC64.md) (function, `0x0071BC64`)
- `0x00A36BBB` → [IopSendMessageToTrackService](../AC/IopSendMessageToTrackService_function_00AC0E5C.md) (function, `0x00AC0E5C`)
- `0x00A36C23` → [IopGetVolumeId](IopGetVolumeId_function_00A372CC.md) (function, `0x00A372CC`)
- `0x00A36C4D` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36C6F` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (function, `0x006BA6F0`)
- `0x00A36C81` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A36C97` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A36CF9` → [IopSendMessageToTrackService](../AC/IopSendMessageToTrackService_function_00AC0E5C.md) (function, `0x00AC0E5C`)
- `0x00A36D17` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36D3B` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36D45` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36D64` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (function, `0x006BA6F0`)
- `0x00A36D75` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A36D8B` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A36DB0` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36DB7` → [IopGetVolumeId](IopGetVolumeId_function_00A372CC.md) (function, `0x00A372CC`)
- `0x00A36DE1` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36E0F` → [IopMarshalIds](../71/IopMarshalIds_function_0071BC64.md) (function, `0x0071BC64`)
- `0x00A36E3D` → [IopTrackLink](IopTrackLink_function_00A36764.md) (function, `0x00A36764`)
- `0x00A36E5E` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36E80` → [IopMarshalIds](../71/IopMarshalIds_function_0071BC64.md) (function, `0x0071BC64`)
- `0x00A36EAE` → [IopTrackLink](IopTrackLink_function_00A36764.md) (function, `0x00A36764`)
- `0x00A36F26` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36F50` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A36F60` → [IopSetRemoteLink](../71/IopSetRemoteLink_function_0071C690.md) (function, `0x0071C690`)
- `0x00A36F87` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (function, `0x006BA6F0`)
- `0x00A36F99` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A36FAF` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A36FE9` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A37013` → [IopGetSetObjectId](IopGetSetObjectId_function_00A37190.md) (function, `0x00A37190`)
- `0x00A3702E` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A37044` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (function, `0x004168D0`)
- `0x00A37072` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A3707F` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00A37091` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A370B8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A370CE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A370E3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A370F8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A37128` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A37145` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A37171` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A37181` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [NtSetInformationFile](../../text/29/NtSetInformationFile_function_0029C5E0.md) at `0x0029D302`
- [IopTrackLink](IopTrackLink_function_00A36764.md) at `0x00A36E3D`
- [IopTrackLink](IopTrackLink_function_00A36764.md) at `0x00A36EAE`

### Static image references
- `0x00A36777` → RVA `0x00E0A740` (`.data`; read)
- `0x00A36880` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **29**
  - `0x00A367D9` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A367EB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A36811` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A36826` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A36968` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (`PAGE` → `.text`)
  - `0x00A36976` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A3698C` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A36C6F` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (`PAGE` → `.text`)
  - `0x00A36C81` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A36C97` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A36D64` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (`PAGE` → `.text`)
  - `0x00A36D75` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A36D8B` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A36F87` → [RtlCompareMemoryUlong](../../text/6B/RtlCompareMemoryUlong_function_006BA6F0.md) (`PAGE` → `.text`)
  - `0x00A36F99` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A36FAF` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A3702E` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A37044` → [IoGetTransactionParameterBlock](../../text/41/IoGetTransactionParameterBlock_function_004168D0.md) (`PAGE` → `.text`)
  - `0x00A37072` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A3707F` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00A37091` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A370B8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A370CE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A370E3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A370F8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A37128` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A37145` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A37171` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A37181` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00A3714B` → [sub_00B3A062](../B3/Unknown_function_00B3A062.md) (`tail-transfer`)
  - `0x00A37157` → [sub_00B3A062](../B3/Unknown_function_00B3A062.md) (`tail-transfer`)
  - `0x00A37166` → [sub_00B3A062 + 0xA](../B3/Unknown_function_00B3A062.md) (`tail-transfer`)
  - `0x00A37177` → [sub_00B3A062 + 0xA](../B3/Unknown_function_00B3A062.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A36764  40 53                           push rbx
00A36766  56                              push rsi
00A36767  57                              push rdi
00A36768  41 54                           push r12
00A3676A  41 55                           push r13
00A3676C  41 56                           push r14
00A3676E  41 57                           push r15
00A36770  48 81 EC C0 02 00 00            sub rsp, 0x2c0
00A36777  48 8B 05 C2 3F 3D 00            mov rax, qword ptr [rip + 0x3d3fc2]
00A3677E  48 33 C4                        xor rax, rsp
00A36781  48 89 84 24 B0 02 00 00         mov qword ptr [rsp + 0x2b0], rax
00A36789  45 8B E9                        mov r13d, r9d
00A3678C  4D 8B F8                        mov r15, r8
00A3678F  4C 8B E2                        mov r12, rdx
00A36792  4C 8B F1                        mov r14, rcx
00A36795  48 8B 84 24 20 03 00 00         mov rax, qword ptr [rsp + 0x320]
00A3679D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A367A2  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A367A7  33 DB                           xor ebx, ebx
00A367A9  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00A367AE  8B F3                           mov esi, ebx
00A367B0  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00A367B5  0F 57 C0                        xorps xmm0, xmm0
00A367B8  33 C0                           xor eax, eax
00A367BA  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
00A367C2  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
00A367C9  8D 7B 40                        lea edi, [rbx + 0x40]
00A367CC  44 8B C7                        mov r8d, edi
00A367CF  33 D2                           xor edx, edx
00A367D1  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
00A367D9  E8 62 04 C9 FF                  call 0x1406c6c40
00A367DE  44 8B C7                        mov r8d, edi
00A367E1  33 D2                           xor edx, edx
00A367E3  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
00A367EB  E8 50 04 C9 FF                  call 0x1406c6c40
00A367F0  0F 57 C0                        xorps xmm0, xmm0
00A367F3  33 C0                           xor eax, eax
00A367F5  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
00A367FD  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
00A36804  44 8B C7                        mov r8d, edi
00A36807  33 D2                           xor edx, edx
00A36809  48 8D 8C 24 60 01 00 00         lea rcx, [rsp + 0x160]
00A36811  E8 2A 04 C9 FF                  call 0x1406c6c40
00A36816  33 D2                           xor edx, edx
00A36818  41 B8 10 01 00 00               mov r8d, 0x110
00A3681E  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00A36826  E8 15 04 C9 FF                  call 0x1406c6c40
00A3682B  38 9C 24 28 03 00 00            cmp byte ptr [rsp + 0x328], bl
00A36832  0F 85 72 08 00 00               jne 0x140a370aa
00A36838  49 8B FF                        mov rdi, r15
00A3683B  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
00A36840  48 8B 0F                        mov rcx, qword ptr [rdi]
00A36843  41 B7 01                        mov r15b, 1
00A36846  48 85 C9                        test rcx, rcx
00A36849  0F 84 E3 08 00 00               je 0x140a37132
00A3684F  41 83 FD 0C                     cmp r13d, 0xc
00A36853  0F 82 A9 08 00 00               jb 0x140a37102
00A36859  41 8D 45 F4                     lea eax, [r13 - 0xc]
00A3685D  8B 57 08                        mov edx, dword ptr [rdi + 8]
00A36860  3B C2                           cmp eax, edx
00A36862  0F 82 E8 08 00 00               jb 0x140a37150
00A36868  48 8D 42 24                     lea rax, [rdx + 0x24]
00A3686C  48 3D 00 01 00 00               cmp rax, 0x100
00A36872  0F 87 E7 08 00 00               ja 0x140a3715f
00A36878  45 33 ED                        xor r13d, r13d
00A3687B  48 85 C9                        test rcx, rcx
00A3687E  74 40                           je 0x140a368c0
00A36880  4C 8B 05 59 02 59 00            mov r8, qword ptr [rip + 0x590259]
00A36887  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00A3688C  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00A36891  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00A36896  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A3689B  44 8A 8C 24 28 03 00 00         mov r9b, byte ptr [rsp + 0x328]
00A368A3  41 8D 55 02                     lea edx, [r13 + 2]
00A368A7  E8 04 25 E3 FF                  call 0x140868db0
00A368AC  8B D8                           mov ebx, eax
00A368AE  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00A368B3  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00A368B8  85 C0                           test eax, eax
00A368BA  0F 88 55 08 00 00               js 0x140a37115
00A368C0  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00A368C4  8B 48 34                        mov ecx, dword ptr [rax + 0x34]
00A368C7  BB 10 00 00 00                  mov ebx, 0x10
00A368CC  84 CB                           test bl, cl
00A368CE  74 3C                           je 0x140a3690c
00A368D0  41 B9 9C 00 09 00               mov r9d, 0x9009c
00A368D6  44 8D 43 30                     lea r8d, [rbx + 0x30]
00A368DA  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
00A368E2  49 8B CE                        mov rcx, r14
00A368E5  E8 A6 08 00 00                  call 0x140a37190
00A368EA  8B D8                           mov ebx, eax
00A368EC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A368F0  3D 34 00 00 C0                  cmp eax, 0xc0000034
00A368F5  0F 85 75 06 00 00               jne 0x140a36f70
00A368FB  41 8B DD                        mov ebx, r13d
00A368FE  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00A36902  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00A36907  E9 50 07 00 00                  jmp 0x140a3705c
00A3690C  4C 39 2F                        cmp qword ptr [rdi], r13
00A3690F  0F 84 03 03 00 00               je 0x140a36c18
00A36915  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00A36919  8B 48 34                        mov ecx, dword ptr [rax + 0x34]
00A3691C  41 B9 9C 00 09 00               mov r9d, 0x9009c
00A36922  41 B8 40 00 00 00               mov r8d, 0x40
00A36928  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
00A36930  84 CB                           test bl, cl
00A36932  49 8B CE                        mov rcx, r14
00A36935  0F 85 0A 04 00 00               jne 0x140a36d45
00A3693B  45 8A E5                        mov r12b, r13b
00A3693E  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
00A36943  E8 48 08 00 00                  call 0x140a37190
00A36948  8B D8                           mov ebx, eax
00A3694A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A3694E  3D 34 00 00 C0                  cmp eax, 0xc0000034
00A36953  74 A6                           je 0x140a368fb
00A36955  85 C0                           test eax, eax
00A36957  78 A9                           js 0x140a36902
00A36959  45 33 C0                        xor r8d, r8d
00A3695C  41 8D 50 10                     lea edx, [r8 + 0x10]
00A36960  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00A36968  E8 83 3D C8 FF                  call 0x1406ba6f0
00A3696D  48 83 F8 10                     cmp rax, 0x10
00A36971  74 88                           je 0x140a368fb
00A36973  49 8B CE                        mov rcx, r14
00A36976  E8 55 FF 9D FF                  call 0x1404168d0
00A3697B  48 85 C0                        test rax, rax
00A3697E  0F 85 CE 06 00 00               jne 0x140a37052
00A36984  4C 39 2F                        cmp qword ptr [rdi], r13
00A36987  74 11                           je 0x140a3699a
00A36989  48 8B CE                        mov rcx, rsi
00A3698C  E8 3F FF 9D FF                  call 0x1404168d0
00A36991  48 85 C0                        test rax, rax
00A36994  0F 85 B8 06 00 00               jne 0x140a37052
00A3699A  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00A369A2  48 8B CE                        mov rcx, rsi
00A369A5  E8 22 09 00 00                  call 0x140a372cc
00A369AA  8B D8                           mov ebx, eax
00A369AC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A369B0  85 C0                           test eax, eax
00A369B2  0F 88 4A FF FF FF               js 0x140a36902
00A369B8  48 8D 94 24 00 01 00 00         lea rdx, [rsp + 0x100]
00A369C0  49 8B CE                        mov rcx, r14
00A369C3  E8 04 09 00 00                  call 0x140a372cc
00A369C8  8B D8                           mov ebx, eax
00A369CA  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A369CE  85 C0                           test eax, eax
00A369D0  0F 88 2C FF FF FF               js 0x140a36902
00A369D6  41 B9 A0 00 09 00               mov r9d, 0x900a0
00A369DC  45 33 C0                        xor r8d, r8d
00A369DF  33 D2                           xor edx, edx
00A369E1  49 8B CE                        mov rcx, r14
00A369E4  E8 A7 07 00 00                  call 0x140a37190
00A369E9  8B D8                           mov ebx, eax
00A369EB  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A369EF  85 C0                           test eax, eax
00A369F1  0F 88 0B FF FF FF               js 0x140a36902
00A369F7  0F 28 9C 24 C0 00 00 00         movaps xmm3, xmmword ptr [rsp + 0xc0]
00A369FF  0F 29 9C 24 60 01 00 00         movaps xmmword ptr [rsp + 0x160], xmm3
00A36A07  0F 28 94 24 D0 00 00 00         movaps xmm2, xmmword ptr [rsp + 0xd0]
00A36A0F  0F 29 94 24 70 01 00 00         movaps xmmword ptr [rsp + 0x170], xmm2
00A36A17  0F 28 8C 24 E0 00 00 00         movaps xmm1, xmmword ptr [rsp + 0xe0]
00A36A1F  0F 29 8C 24 80 01 00 00         movaps xmmword ptr [rsp + 0x180], xmm1
00A36A27  0F 28 84 24 F0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xf0]
00A36A2F  0F 29 84 24 90 01 00 00         movaps xmmword ptr [rsp + 0x190], xmm0
00A36A37  0F 29 9C 24 20 01 00 00         movaps xmmword ptr [rsp + 0x120], xmm3
00A36A3F  0F 29 94 24 30 01 00 00         movaps xmmword ptr [rsp + 0x130], xmm2
00A36A47  0F 29 8C 24 40 01 00 00         movaps xmmword ptr [rsp + 0x140], xmm1
00A36A4F  0F 29 84 24 50 01 00 00         movaps xmmword ptr [rsp + 0x150], xmm0
00A36A57  48 8B 84 24 A4 00 00 00         mov rax, qword ptr [rsp + 0xa4]
00A36A5F  48 2B 84 24 04 01 00 00         sub rax, qword ptr [rsp + 0x104]
00A36A67  75 10                           jne 0x140a36a79
00A36A69  48 8B 84 24 AC 00 00 00         mov rax, qword ptr [rsp + 0xac]
00A36A71  48 2B 84 24 0C 01 00 00         sub rax, qword ptr [rsp + 0x10c]
00A36A79  48 85 C0                        test rax, rax
00A36A7C  74 11                           je 0x140a36a8f
00A36A7E  8A 84 24 D0 00 00 00            mov al, byte ptr [rsp + 0xd0]
00A36A85  41 0A C7                        or al, r15b
00A36A88  88 84 24 30 01 00 00            mov byte ptr [rsp + 0x130], al
00A36A8F  41 B9 98 00 09 00               mov r9d, 0x90098
00A36A95  41 B8 40 00 00 00               mov r8d, 0x40
00A36A9B  48 8D 94 24 20 01 00 00         lea rdx, [rsp + 0x120]
00A36AA3  48 8B CE                        mov rcx, rsi
00A36AA6  E8 E5 06 00 00                  call 0x140a37190
00A36AAB  8B D8                           mov ebx, eax
00A36AAD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36AB1  3D BD 00 00 C0                  cmp eax, 0xc00000bd
00A36AB6  74 07                           je 0x140a36abf
00A36AB8  3D 35 00 00 C0                  cmp eax, 0xc0000035
00A36ABD  75 48                           jne 0x140a36b07
00A36ABF  41 B9 C0 00 09 00               mov r9d, 0x900c0
00A36AC5  41 B8 40 00 00 00               mov r8d, 0x40
00A36ACB  48 8D 94 24 60 01 00 00         lea rdx, [rsp + 0x160]
00A36AD3  48 8B CE                        mov rcx, rsi
00A36AD6  E8 B5 06 00 00                  call 0x140a37190
00A36ADB  8B D8                           mov ebx, eax
00A36ADD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36AE1  85 C0                           test eax, eax
00A36AE3  78 22                           js 0x140a36b07
00A36AE5  41 B9 BC 00 09 00               mov r9d, 0x900bc
00A36AEB  41 B8 30 00 00 00               mov r8d, 0x30
00A36AF1  48 8D 94 24 30 01 00 00         lea rdx, [rsp + 0x130]
00A36AF9  48 8B CE                        mov rcx, rsi
00A36AFC  E8 8F 06 00 00                  call 0x140a37190
00A36B01  8B D8                           mov ebx, eax
00A36B03  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36B07  85 DB                           test ebx, ebx
00A36B09  0F 88 BF 00 00 00               js 0x140a36bce
00A36B0F  45 8A E7                        mov r12b, r15b
00A36B12  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
00A36B17  48 8B 84 24 A4 00 00 00         mov rax, qword ptr [rsp + 0xa4]
00A36B1F  48 2B 84 24 04 01 00 00         sub rax, qword ptr [rsp + 0x104]
00A36B27  75 10                           jne 0x140a36b39
00A36B29  48 8B 84 24 AC 00 00 00         mov rax, qword ptr [rsp + 0xac]
00A36B31  48 2B 84 24 0C 01 00 00         sub rax, qword ptr [rsp + 0x10c]
00A36B39  48 85 C0                        test rax, rax
00A36B3C  0F 84 84 00 00 00               je 0x140a36bc6
00A36B42  4C 8B CF                        mov r9, rdi
00A36B45  4C 8D 84 24 60 01 00 00         lea r8, [rsp + 0x160]
00A36B4D  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00A36B55  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00A36B5D  E8 02 51 CE FF                  call 0x14071bc64
00A36B62  0F 28 84 24 C0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xc0]
00A36B6A  0F 29 44 24 60                  movaps xmmword ptr [rsp + 0x60], xmm0
00A36B6F  0F 28 94 24 D0 00 00 00         movaps xmm2, xmmword ptr [rsp + 0xd0]
00A36B77  0F 29 54 24 70                  movaps xmmword ptr [rsp + 0x70], xmm2
00A36B7C  0F 28 84 24 E0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xe0]
00A36B84  0F 29 84 24 80 00 00 00         movaps xmmword ptr [rsp + 0x80], xmm0
00A36B8C  0F 28 8C 24 F0 00 00 00         movaps xmm1, xmmword ptr [rsp + 0xf0]
00A36B94  0F 29 8C 24 90 00 00 00         movaps xmmword ptr [rsp + 0x90], xmm1
00A36B9C  66 0F 7E D0                     movd eax, xmm2
00A36BA0  24 FE                           and al, 0xfe
00A36BA2  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00A36BA6  4C 8D 84 24 A0 01 00 00         lea r8, [rsp + 0x1a0]
00A36BAE  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00A36BB3  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
00A36BBB  E8 9C A2 08 00                  call 0x140ac0e5c
00A36BC0  8B D8                           mov ebx, eax
00A36BC2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36BC6  85 DB                           test ebx, ebx
00A36BC8  0F 89 34 FD FF FF               jns 0x140a36902
00A36BCE  41 8B C5                        mov eax, r13d
00A36BD1  45 84 E4                        test r12b, r12b
00A36BD4  0F 84 42 01 00 00               je 0x140a36d1c
00A36BDA  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
00A36BE2  48 2B 84 24 C0 00 00 00         sub rax, qword ptr [rsp + 0xc0]
00A36BEA  75 10                           jne 0x140a36bfc
00A36BEC  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
00A36BF4  48 2B 84 24 C8 00 00 00         sub rax, qword ptr [rsp + 0xc8]
00A36BFC  48 8B CE                        mov rcx, rsi
00A36BFF  48 85 C0                        test rax, rax
00A36C02  0F 85 FB 00 00 00               jne 0x140a36d03
00A36C08  41 B9 A0 00 09 00               mov r9d, 0x900a0
00A36C0E  45 33 C0                        xor r8d, r8d
00A36C11  33 D2                           xor edx, edx
00A36C13  E9 FF 00 00 00                  jmp 0x140a36d17
00A36C18  48 8D 94 24 00 01 00 00         lea rdx, [rsp + 0x100]
00A36C20  49 8B CE                        mov rcx, r14
00A36C23  E8 A4 06 00 00                  call 0x140a372cc
00A36C28  8B D8                           mov ebx, eax
00A36C2A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36C2E  85 C0                           test eax, eax
00A36C30  0F 88 CC FC FF FF               js 0x140a36902
00A36C36  41 B9 9C 00 09 00               mov r9d, 0x9009c
00A36C3C  41 B8 40 00 00 00               mov r8d, 0x40
00A36C42  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
00A36C4A  49 8B CE                        mov rcx, r14
00A36C4D  E8 3E 05 00 00                  call 0x140a37190
00A36C52  8B D8                           mov ebx, eax
00A36C54  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36C58  85 C0                           test eax, eax
00A36C5A  0F 88 A2 FC FF FF               js 0x140a36902
00A36C60  45 33 C0                        xor r8d, r8d
00A36C63  41 8D 50 10                     lea edx, [r8 + 0x10]
00A36C67  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00A36C6F  E8 7C 3A C8 FF                  call 0x1406ba6f0
00A36C74  48 83 F8 10                     cmp rax, 0x10
00A36C78  0F 84 7D FC FF FF               je 0x140a368fb
00A36C7E  49 8B CE                        mov rcx, r14
00A36C81  E8 4A FC 9D FF                  call 0x1404168d0
00A36C86  48 85 C0                        test rax, rax
00A36C89  0F 85 C3 03 00 00               jne 0x140a37052
00A36C8F  4C 39 2F                        cmp qword ptr [rdi], r13
00A36C92  74 11                           je 0x140a36ca5
00A36C94  48 8B CE                        mov rcx, rsi
00A36C97  E8 34 FC 9D FF                  call 0x1404168d0
00A36C9C  48 85 C0                        test rax, rax
00A36C9F  0F 85 AD 03 00 00               jne 0x140a37052
00A36CA5  0F 28 84 24 C0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xc0]
00A36CAD  0F 29 44 24 60                  movaps xmmword ptr [rsp + 0x60], xmm0
00A36CB2  0F 28 94 24 D0 00 00 00         movaps xmm2, xmmword ptr [rsp + 0xd0]
00A36CBA  0F 29 54 24 70                  movaps xmmword ptr [rsp + 0x70], xmm2
00A36CBF  0F 28 84 24 E0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xe0]
00A36CC7  0F 29 84 24 80 00 00 00         movaps xmmword ptr [rsp + 0x80], xmm0
00A36CCF  0F 28 8C 24 F0 00 00 00         movaps xmm1, xmmword ptr [rsp + 0xf0]
00A36CD7  0F 29 8C 24 90 00 00 00         movaps xmmword ptr [rsp + 0x90], xmm1
00A36CDF  66 0F 7E D0                     movd eax, xmm2
00A36CE3  24 FE                           and al, 0xfe
00A36CE5  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00A36CE9  4C 8B C7                        mov r8, rdi
00A36CEC  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00A36CF1  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
00A36CF9  E8 5E A1 08 00                  call 0x140ac0e5c
00A36CFE  E9 62 02 00 00                  jmp 0x140a36f65
00A36D03  41 B9 BC 00 09 00               mov r9d, 0x900bc
00A36D09  41 B8 30 00 00 00               mov r8d, 0x30
00A36D0F  48 8D 94 24 70 01 00 00         lea rdx, [rsp + 0x170]
00A36D17  E8 74 04 00 00                  call 0x140a37190
00A36D1C  85 C0                           test eax, eax
00A36D1E  0F 88 DE FB FF FF               js 0x140a36902
00A36D24  41 B9 98 00 09 00               mov r9d, 0x90098
00A36D2A  41 B8 40 00 00 00               mov r8d, 0x40
00A36D30  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
00A36D38  49 8B CE                        mov rcx, r14
00A36D3B  E8 50 04 00 00                  call 0x140a37190
00A36D40  E9 BD FB FF FF                  jmp 0x140a36902
00A36D45  E8 46 04 00 00                  call 0x140a37190
00A36D4A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36D4E  85 C0                           test eax, eax
00A36D50  0F 88 A5 FB FF FF               js 0x140a368fb
00A36D56  45 33 C0                        xor r8d, r8d
00A36D59  48 8B D3                        mov rdx, rbx
00A36D5C  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00A36D64  E8 87 39 C8 FF                  call 0x1406ba6f0
00A36D69  48 3B C3                        cmp rax, rbx
00A36D6C  0F 84 89 FB FF FF               je 0x140a368fb
00A36D72  49 8B CE                        mov rcx, r14
00A36D75  E8 56 FB 9D FF                  call 0x1404168d0
00A36D7A  48 85 C0                        test rax, rax
00A36D7D  0F 85 CF 02 00 00               jne 0x140a37052
00A36D83  4C 39 2F                        cmp qword ptr [rdi], r13
00A36D86  74 11                           je 0x140a36d99
00A36D88  48 8B CE                        mov rcx, rsi
00A36D8B  E8 40 FB 9D FF                  call 0x1404168d0
00A36D90  48 85 C0                        test rax, rax
00A36D93  0F 85 B9 02 00 00               jne 0x140a37052
00A36D99  41 B9 E8 00 14 00               mov r9d, 0x1400e8
00A36D9F  41 B8 14 00 00 00               mov r8d, 0x14
00A36DA5  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00A36DAD  48 8B CE                        mov rcx, rsi
00A36DB0  E8 DB 03 00 00                  call 0x140a37190
00A36DB5  EB 05                           jmp 0x140a36dbc
00A36DB7  E8 10 05 00 00                  call 0x140a372cc
00A36DBC  8B D8                           mov ebx, eax
00A36DBE  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36DC2  85 C0                           test eax, eax
00A36DC4  0F 88 38 FB FF FF               js 0x140a36902
00A36DCA  41 B9 C0 00 09 00               mov r9d, 0x900c0
00A36DD0  41 B8 40 00 00 00               mov r8d, 0x40
00A36DD6  48 8D 94 24 60 01 00 00         lea rdx, [rsp + 0x160]
00A36DDE  48 8B CE                        mov rcx, rsi
00A36DE1  E8 AA 03 00 00                  call 0x140a37190
00A36DE6  8B D8                           mov ebx, eax
00A36DE8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36DEC  85 C0                           test eax, eax
00A36DEE  0F 88 0E FB FF FF               js 0x140a36902
00A36DF4  4C 8B CF                        mov r9, rdi
00A36DF7  4C 8D 84 24 60 01 00 00         lea r8, [rsp + 0x160]
00A36DFF  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00A36E07  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00A36E0F  E8 50 4E CE FF                  call 0x14071bc64
00A36E14  44 8B 8C 24 A8 01 00 00         mov r9d, dword ptr [rsp + 0x1a8]
00A36E1C  41 83 C1 0C                     add r9d, 0xc
00A36E20  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
00A36E25  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00A36E2A  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A36E2F  4C 8D 84 24 A0 01 00 00         lea r8, [rsp + 0x1a0]
00A36E37  49 8B D4                        mov rdx, r12
00A36E3A  49 8B CE                        mov rcx, r14
00A36E3D  E8 22 F9 FF FF                  call 0x140a36764
00A36E42  8B D8                           mov ebx, eax
00A36E44  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36E48  85 C0                           test eax, eax
00A36E4A  0F 88 0C 02 00 00               js 0x140a3705c
00A36E50  41 B9 A0 00 09 00               mov r9d, 0x900a0
00A36E56  45 33 C0                        xor r8d, r8d
00A36E59  33 D2                           xor edx, edx
00A36E5B  49 8B CE                        mov rcx, r14
00A36E5E  E8 2D 03 00 00                  call 0x140a37190
00A36E63  EB 4E                           jmp 0x140a36eb3
00A36E65  4C 8B CF                        mov r9, rdi
00A36E68  4C 8D 84 24 60 01 00 00         lea r8, [rsp + 0x160]
00A36E70  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00A36E78  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00A36E80  E8 DF 4D CE FF                  call 0x14071bc64
00A36E85  44 8B 8C 24 A8 01 00 00         mov r9d, dword ptr [rsp + 0x1a8]
00A36E8D  41 83 C1 0C                     add r9d, 0xc
00A36E91  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
00A36E96  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00A36E9B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A36EA0  4C 8D 84 24 A0 01 00 00         lea r8, [rsp + 0x1a0]
00A36EA8  49 8B D4                        mov rdx, r12
00A36EAB  49 8B CE                        mov rcx, r14
00A36EAE  E8 B1 F8 FF FF                  call 0x140a36764
00A36EB3  8B D8                           mov ebx, eax
00A36EB5  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36EB9  85 C0                           test eax, eax
00A36EBB  0F 88 9B 01 00 00               js 0x140a3705c
00A36EC1  0F 28 84 24 C0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xc0]
00A36EC9  0F 29 84 24 20 01 00 00         movaps xmmword ptr [rsp + 0x120], xmm0
00A36ED1  0F 28 94 24 D0 00 00 00         movaps xmm2, xmmword ptr [rsp + 0xd0]
00A36ED9  0F 29 94 24 30 01 00 00         movaps xmmword ptr [rsp + 0x130], xmm2
00A36EE1  0F 28 84 24 E0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xe0]
00A36EE9  0F 29 84 24 40 01 00 00         movaps xmmword ptr [rsp + 0x140], xmm0
00A36EF1  0F 28 8C 24 F0 00 00 00         movaps xmm1, xmmword ptr [rsp + 0xf0]
00A36EF9  0F 29 8C 24 50 01 00 00         movaps xmmword ptr [rsp + 0x150], xmm1
00A36F01  66 0F 7E D0                     movd eax, xmm2
00A36F05  41 0A C7                        or al, r15b
00A36F08  88 84 24 30 01 00 00            mov byte ptr [rsp + 0x130], al
00A36F0F  41 B9 BC 00 09 00               mov r9d, 0x900bc
00A36F15  41 B8 30 00 00 00               mov r8d, 0x30
00A36F1B  48 8D 94 24 30 01 00 00         lea rdx, [rsp + 0x130]
00A36F23  48 8B CE                        mov rcx, rsi
00A36F26  E8 65 02 00 00                  call 0x140a37190
00A36F2B  8B D8                           mov ebx, eax
00A36F2D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36F31  85 C0                           test eax, eax
00A36F33  0F 89 23 01 00 00               jns 0x140a3705c
00A36F39  41 B9 98 00 09 00               mov r9d, 0x90098
00A36F3F  41 B8 40 00 00 00               mov r8d, 0x40
00A36F45  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
00A36F4D  49 8B CE                        mov rcx, r14
00A36F50  E8 3B 02 00 00                  call 0x140a37190
00A36F55  E9 02 01 00 00                  jmp 0x140a3705c
00A36F5A  4C 8B C7                        mov r8, rdi
00A36F5D  49 8B CE                        mov rcx, r14
00A36F60  E8 2B 57 CE FF                  call 0x14071c690
00A36F65  8B D8                           mov ebx, eax
00A36F67  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36F6B  E9 92 F9 FF FF                  jmp 0x140a36902
00A36F70  85 C0                           test eax, eax
00A36F72  0F 88 8A F9 FF FF               js 0x140a36902
00A36F78  45 33 C0                        xor r8d, r8d
00A36F7B  41 8D 50 10                     lea edx, [r8 + 0x10]
00A36F7F  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00A36F87  E8 64 37 C8 FF                  call 0x1406ba6f0
00A36F8C  48 83 F8 10                     cmp rax, 0x10
00A36F90  0F 84 65 F9 FF FF               je 0x140a368fb
00A36F96  49 8B CE                        mov rcx, r14
00A36F99  E8 32 F9 9D FF                  call 0x1404168d0
00A36F9E  48 85 C0                        test rax, rax
00A36FA1  0F 85 AB 00 00 00               jne 0x140a37052
00A36FA7  4C 39 2F                        cmp qword ptr [rdi], r13
00A36FAA  74 7F                           je 0x140a3702b
00A36FAC  48 8B CE                        mov rcx, rsi
00A36FAF  E8 1C F9 9D FF                  call 0x1404168d0
00A36FB4  48 85 C0                        test rax, rax
00A36FB7  0F 85 95 00 00 00               jne 0x140a37052
00A36FBD  4C 39 2F                        cmp qword ptr [rdi], r13
00A36FC0  74 69                           je 0x140a3702b
00A36FC2  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00A36FC6  8B 48 34                        mov ecx, dword ptr [rax + 0x34]
00A36FC9  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00A36FD1  F6 C1 10                        test cl, 0x10
00A36FD4  48 8B CE                        mov rcx, rsi
00A36FD7  0F 84 DA FD FF FF               je 0x140a36db7
00A36FDD  41 B9 E8 00 14 00               mov r9d, 0x1400e8
00A36FE3  41 B8 14 00 00 00               mov r8d, 0x14
00A36FE9  E8 A2 01 00 00                  call 0x140a37190
00A36FEE  8B D8                           mov ebx, eax
00A36FF0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A36FF4  85 C0                           test eax, eax
00A36FF6  0F 88 06 F9 FF FF               js 0x140a36902
00A36FFC  41 B9 C0 00 09 00               mov r9d, 0x900c0
00A37002  41 B8 40 00 00 00               mov r8d, 0x40
00A37008  48 8D 94 24 60 01 00 00         lea rdx, [rsp + 0x160]
00A37010  48 8B CE                        mov rcx, rsi
00A37013  E8 78 01 00 00                  call 0x140a37190
00A37018  8B D8                           mov ebx, eax
00A3701A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A3701E  85 C0                           test eax, eax
00A37020  0F 88 DC F8 FF FF               js 0x140a36902
00A37026  E9 3A FE FF FF                  jmp 0x140a36e65
00A3702B  49 8B CE                        mov rcx, r14
00A3702E  E8 9D F8 9D FF                  call 0x1404168d0
00A37033  48 85 C0                        test rax, rax
00A37036  75 1A                           jne 0x140a37052
00A37038  4C 39 2F                        cmp qword ptr [rdi], r13
00A3703B  0F 84 19 FF FF FF               je 0x140a36f5a
00A37041  48 8B CE                        mov rcx, rsi
00A37044  E8 87 F8 9D FF                  call 0x1404168d0
00A37049  48 85 C0                        test rax, rax
00A3704C  0F 84 08 FF FF FF               je 0x140a36f5a
00A37052  BB 59 00 19 C0                  mov ebx, 0xc0190059
00A37057  E9 A2 F8 FF FF                  jmp 0x140a368fe
00A3705C  80 BC 24 28 03 00 00 00         cmp byte ptr [rsp + 0x328], 0
00A37064  0F 85 89 00 00 00               jne 0x140a370f3
00A3706A  48 85 F6                        test rsi, rsi
00A3706D  74 08                           je 0x140a37077
00A3706F  48 8B CE                        mov rcx, rsi
00A37072  E8 D9 22 8C FF                  call 0x1402f9350
00A37077  45 33 C0                        xor r8d, r8d
00A3707A  33 D2                           xor edx, edx
00A3707C  49 8B CD                        mov rcx, r13
00A3707F  E8 8C 82 90 FF                  call 0x14033f310
00A37084  8B C3                           mov eax, ebx
00A37086  48 8B 8C 24 B0 02 00 00         mov rcx, qword ptr [rsp + 0x2b0]
00A3708E  48 33 CC                        xor rcx, rsp
00A37091  E8 AA 55 C7 FF                  call 0x1406ac640
00A37096  48 81 C4 C0 02 00 00            add rsp, 0x2c0
00A3709D  41 5F                           pop r15
00A3709F  41 5E                           pop r14
00A370A1  41 5D                           pop r13
00A370A3  41 5C                           pop r12
00A370A5  5F                              pop rdi
00A370A6  5E                              pop rsi
00A370A7  5B                              pop rbx
00A370A8  C3                              ret
00A370A9  CC                              int3
00A370AA  41 B8 49 6F 20 20               mov r8d, 0x20206f49
00A370B0  49 8B D5                        mov rdx, r13
00A370B3  B9 23 01 00 00                  mov ecx, 0x123
00A370B8  E8 33 B0 14 00                  call 0x140b820f0
00A370BD  48 8B F8                        mov rdi, rax
00A370C0  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A370C5  4D 8B C5                        mov r8, r13
00A370C8  49 8B D7                        mov rdx, r15
00A370CB  48 8B C8                        mov rcx, rax
00A370CE  E8 6D F7 C8 FF                  call 0x1406c6840
00A370D3  EB 17                           jmp 0x140a370ec
00A370D5  8B D8                           mov ebx, eax
00A370D7  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00A370DC  48 85 C9                        test rcx, rcx
00A370DF  74 07                           je 0x140a370e8
00A370E1  33 D2                           xor edx, edx
00A370E3  E8 88 B7 14 00                  call 0x140b82870
00A370E8  8B C3                           mov eax, ebx
00A370EA  EB 9A                           jmp 0x140a37086
00A370EC  33 DB                           xor ebx, ebx
00A370EE  E9 4D F7 FF FF                  jmp 0x140a36840
00A370F3  33 D2                           xor edx, edx
00A370F5  48 8B CF                        mov rcx, rdi
00A370F8  E8 73 B7 14 00                  call 0x140b82870
00A370FD  E9 68 FF FF FF                  jmp 0x140a3706a
00A37102  38 9C 24 28 03 00 00            cmp byte ptr [rsp + 0x328], bl
00A37109  75 71                           jne 0x140a3717c
00A3710B  B8 95 00 00 C0                  mov eax, 0xc0000095
00A37110  E9 71 FF FF FF                  jmp 0x140a37086
00A37115  44 38 AC 24 28 03 00 00         cmp byte ptr [rsp + 0x328], r13b
00A3711D  0F 84 61 FF FF FF               je 0x140a37084
00A37123  33 D2                           xor edx, edx
00A37125  48 8B CF                        mov rcx, rdi
00A37128  E8 43 B7 14 00                  call 0x140b82870
00A3712D  E9 52 FF FF FF                  jmp 0x140a37084
00A37132  44 38 BC 24 28 03 00 00         cmp byte ptr [rsp + 0x328], r15b
00A3713A  0F 85 0F F7 FF FF               jne 0x140a3684f
00A37140  33 D2                           xor edx, edx
00A37142  48 8B CF                        mov rcx, rdi
00A37145  E8 26 B7 14 00                  call 0x140b82870
00A3714A  90                              nop
00A3714B  E9 12 2F 10 00                  jmp 0x140b3a062
00A37150  38 9C 24 28 03 00 00            cmp byte ptr [rsp + 0x328], bl
00A37157  0F 84 05 2F 10 00               je 0x140b3a062
00A3715D  EB E1                           jmp 0x140a37140
00A3715F  38 9C 24 28 03 00 00            cmp byte ptr [rsp + 0x328], bl
00A37166  0F 84 00 2F 10 00               je 0x140b3a06c
00A3716C  33 D2                           xor edx, edx
00A3716E  48 8B CF                        mov rcx, rdi
00A37171  E8 FA B6 14 00                  call 0x140b82870
00A37176  90                              nop
00A37177  E9 F0 2E 10 00                  jmp 0x140b3a06c
00A3717C  33 D2                           xor edx, edx
00A3717E  48 8B CF                        mov rcx, rdi
00A37181  E8 EA B6 14 00                  call 0x140b82870
00A37186  EB 83                           jmp 0x140a3710b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopTrackLink(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1EC;
    unsigned __int64 v_stack_m1F4;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned int v_stack_m248;
    unsigned __int64 v_stack_m24C;
    unsigned __int64 v_stack_m254;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int8 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned int v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p50;

    v_rsp = (v_rsp) - (704);
    result = (*(unsigned __int64 *)(v_rip + 4014018)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m2C0 = a5;
    v_stack_m2A0 = a5;
    v_rbx = 0;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    result = 0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1E8 = 0;
    a2 = 0;
    result = memset(v_stack_m238, a2, (unsigned int)((unsigned int)(v_rbx + 64)), a4);
    a2 = 0;
    result = memset(v_stack_m1D8, a2, (unsigned int)((unsigned int)(v_rbx + 64)), a4);
    result = 0;
    v_stack_m258 = v_xmm0;
    v_stack_m248 = 0;
    a2 = 0;
    result = memset(v_stack_m198, a2, (unsigned int)((unsigned int)(v_rbx + 64)), a4);
    a2 = 0;
    result = memset(v_stack_m158, a2, 272, a4);
    if (a6 != 0) goto loc_00A370AA;
    v_stack_m2A8 = a3;
loc_00A36840:
    if (*(unsigned __int64 *)(a3) == 0) goto loc_00A37132;
loc_00A3684F:
    if (((unsigned int)((unsigned int)(a4))) < 12) goto loc_00A37102;
    if (((unsigned int)((unsigned int)(a4) - 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 8))))) goto loc_00A37150;
    if (((unsigned int)(*(unsigned int *)(a3 + 8)) + 36) > 256) goto loc_00A3715F;
    v_r13 = 0;
    if (*(unsigned __int64 *)(a3) == 0) goto loc_00A368C0;
    v_stack_m2B0 = 0;
    v_stack_m2D0 = 0;
    v_stack_m2D8 = v_stack_m2B0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(a3), v_r13 + 2, *(unsigned __int64 *)(v_rip + 5833305), a6);
    v_stack_m2B0 = v_stack_m2B0;
    if (sign_flag) goto loc_00A37115;
loc_00A368C0:
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52))))) == 0) goto loc_00A3690C;
    result = IopGetSetObjectId(a1, v_stack_m238, 16 + 48, (unsigned int)(0x9009CULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00A36F70;
loc_00A368FB:
loc_00A368FE:
    v_stack_m2C8 = 0;
loc_00A36902:
    goto loc_00A3705C;
loc_00A3690C:
    if ((*(unsigned __int64 *)(a3)) == v_stack_m2C0) goto loc_00A36C18;
    if (((0) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2B0 + 8) + 52))))) != 0) goto loc_00A36D45;
    v_stack_m2B8 = (unsigned __int8)(v_stack_m2C0);
    result = IopGetSetObjectId(a1, v_stack_m238, 64, (unsigned int)(0x9009CULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00A368FB;
    if (sign_flag) goto loc_00A36902;
    a3 = 0;
    result = RtlCompareMemoryUlong(v_stack_m218, a3 + 16, a3, (unsigned int)(0x9009CULL));
    if (result == 16) goto loc_00A368FB;
    result = IoGetTransactionParameterBlock(a1, a3 + 16, a3, (unsigned int)(0x9009CULL));
    if (result != 0) goto loc_00A37052;
    if ((*(unsigned __int64 *)(a3)) == v_stack_m2C0) goto loc_00A3699A;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, a3 + 16, a3, (unsigned int)(0x9009CULL));
    if (result != 0) goto loc_00A37052;
loc_00A3699A:
    result = IopGetVolumeId(v_stack_m2B0, v_stack_m258, a3, (unsigned int)(0x9009CULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopGetVolumeId(a1, v_stack_m1F8, a3, (unsigned int)(0x9009CULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A36902;
    a3 = 0;
    a2 = 0;
    result = IopGetSetObjectId(a1, a2, a3, (unsigned int)(0x900A0ULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A36902;
    v_stack_m198 = v_xmm3;
    v_stack_m188 = v_xmm2;
    v_stack_m178 = v_xmm1;
    v_stack_m168 = v_xmm0;
    v_stack_m1D8 = v_xmm3;
    v_stack_m1C8 = v_xmm2;
    v_stack_m1B8 = v_xmm1;
    v_stack_m1A8 = v_xmm0;
    result = (v_stack_m254) - (v_stack_m1F4);
    if (!(condition_is_not_equal)) {
        result = v_stack_m24C;
        result = (result) - (v_stack_m1EC);
    }
    if (result != 0) {
        result = v_stack_m228;
        result = (unsigned __int8)((result) | (1));
        v_stack_m1C8 = (unsigned __int8)(result);
    }
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m1D8, 64, (unsigned int)(0x90098ULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (((unsigned int)(result)) == 0xC00000BDULL) goto loc_00A36ABF;
    if (((unsigned int)(result)) != 0xC0000035ULL) goto loc_00A36B07;
loc_00A36ABF:
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m198, 64, (unsigned int)(0x900C0ULL));
    v_stack_m2C8 = (unsigned int)(result);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a4 = 0x900BCULL;
        a3 = 48;
        a2 = v_stack_m1C8;
        a1 = v_stack_m2B0;
        result = IopGetSetObjectId(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
        v_stack_m2C8 = (unsigned int)(result);
    }
    if (sign_flag) goto loc_00A36BCE;
    v_stack_m2B8 = 1;
    result = (v_stack_m254) - (v_stack_m1F4);
    if (!(condition_is_not_equal)) {
        result = v_stack_m24C;
        result = (result) - (v_stack_m1EC);
    }
    if (result != 0) {
        a4 = a3;
        a3 = v_stack_m198;
        a2 = v_stack_m258;
        a1 = v_stack_m158;
        result = IopMarshalIds(a1, a2, a3, a4);
        v_stack_m298 = v_xmm0;
        v_stack_m288 = v_xmm2;
        v_stack_m278 = v_xmm0;
        v_stack_m268 = v_xmm1;
        result = (unsigned __int8)((result) & (254));
        v_stack_m288 = (unsigned __int8)(result);
        a3 = v_stack_m158;
        a2 = v_stack_m298;
        a1 = v_stack_m1F8;
        result = IopSendMessageToTrackService(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
        v_stack_m2C8 = (unsigned int)(result);
    }
    if (!sign_flag) goto loc_00A36902;
loc_00A36BCE:
    if (1 == 0) goto loc_00A36D1C;
    result = (v_stack_m198) - (v_stack_m238);
    if (!(condition_is_not_equal)) {
        result = v_stack_m190;
        result = (result) - (v_stack_m230);
    }
    if (result != 0) goto loc_00A36D03;
    a3 = 0;
    a2 = 0;
    goto loc_00A36D17;
loc_00A36C18:
    result = IopGetVolumeId(a1, v_stack_m1F8, a3, (unsigned int)(0x900A0ULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopGetSetObjectId(a1, v_stack_m238, 64, (unsigned int)(0x9009CULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A36902;
    a3 = 0;
    result = RtlCompareMemoryUlong(v_stack_m218, a3 + 16, a3, (unsigned int)(0x9009CULL));
    if (result == 16) goto loc_00A368FB;
    result = IoGetTransactionParameterBlock(a1, a3 + 16, a3, (unsigned int)(0x9009CULL));
    if (result != 0) goto loc_00A37052;
    if ((*(unsigned __int64 *)(a3)) == v_stack_m2C0) goto loc_00A36CA5;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, a3 + 16, a3, (unsigned int)(0x9009CULL));
    if (result != 0) goto loc_00A37052;
loc_00A36CA5:
    v_stack_m298 = v_xmm0;
    v_stack_m288 = v_xmm2;
    v_stack_m278 = v_xmm0;
    v_stack_m268 = v_xmm1;
    result = (unsigned __int8)((result) & (254));
    v_stack_m288 = (unsigned __int8)(result);
    result = IopSendMessageToTrackService(v_stack_m1F8, v_stack_m298, 0, (unsigned int)(0x9009CULL));
    goto loc_00A36F65;
loc_00A36D03:
loc_00A36D17:
    result = IopGetSetObjectId(v_stack_m1F8, v_stack_m188, 48, (unsigned int)(0x900BCULL));
loc_00A36D1C:
    if (sign_flag) goto loc_00A36902;
    result = IopGetSetObjectId(a1, v_stack_m238, 64, (unsigned int)(0x90098ULL));
    goto loc_00A36902;
loc_00A36D45:
    result = IopGetSetObjectId(a1, v_stack_m238, 64, (unsigned int)(0x90098ULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A368FB;
    a3 = 0;
    result = RtlCompareMemoryUlong(v_stack_m218, (unsigned int)((unsigned int)(result)), a3, (unsigned int)(0x90098ULL));
    if (result == ((unsigned int)((unsigned int)(result)))) goto loc_00A368FB;
    result = IoGetTransactionParameterBlock(a1, (unsigned int)((unsigned int)(result)), a3, (unsigned int)(0x90098ULL));
    if (result != 0) goto loc_00A37052;
    if ((*(unsigned __int64 *)(a3)) == v_stack_m2C0) goto loc_00A36D99;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, (unsigned int)((unsigned int)(result)), a3, (unsigned int)(0x90098ULL));
    if (result != 0) goto loc_00A37052;
loc_00A36D99:
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m258, 20, (unsigned int)(0x1400E8ULL));
    goto loc_00A36DBC;
loc_00A36DB7:
    result = IopGetVolumeId(v_stack_m2B0, v_stack_m258, 20, (unsigned int)(0x1400E8ULL));
loc_00A36DBC:
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m198, 64, (unsigned int)(0x900C0ULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopMarshalIds(v_stack_m158, v_stack_m258, v_stack_m198, 0);
    a4 = (unsigned int)(((unsigned int)(v_stack_m150)) + (12));
    v_stack_m2D0 = (unsigned __int8)(v_stack_m2C0);
    v_stack_m2D8 = v_stack_m2C0;
    result = IopTrackLink(a1, 1, v_stack_m158, a4);
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A3705C;
    a3 = 0;
    a2 = 0;
    result = IopGetSetObjectId(a1, a2, a3, (unsigned int)(0x900A0ULL));
    goto loc_00A36EB3;
loc_00A36E65:
    result = IopMarshalIds(v_stack_m158, v_stack_m258, v_stack_m198, 0);
    a4 = (unsigned int)(((unsigned int)(v_stack_m150)) + (12));
    v_stack_m2D0 = (unsigned __int8)(v_stack_m2C0);
    v_stack_m2D8 = v_stack_m2C0;
    result = IopTrackLink(a1, 1, v_stack_m158, a4);
loc_00A36EB3:
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A3705C;
    v_stack_m1D8 = v_xmm0;
    v_stack_m1C8 = v_xmm2;
    v_stack_m1B8 = v_xmm0;
    v_stack_m1A8 = v_xmm1;
    result = (unsigned __int8)((result) | (1));
    v_stack_m1C8 = (unsigned __int8)(result);
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m1C8, 48, (unsigned int)(0x900BCULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (!sign_flag) goto loc_00A3705C;
    result = IopGetSetObjectId(a1, v_stack_m238, 64, (unsigned int)(0x90098ULL));
    goto loc_00A3705C;
loc_00A36F5A:
    result = IopSetRemoteLink(a1, v_stack_m238, 0, (unsigned int)(0x90098ULL));
loc_00A36F65:
    v_stack_m2C8 = (unsigned int)(result);
    goto loc_00A36902;
loc_00A36F70:
    if (sign_flag) goto loc_00A36902;
    a3 = 0;
    result = RtlCompareMemoryUlong(v_stack_m218, a3 + 16, a3, (unsigned int)(0x90098ULL));
    if (result == 16) goto loc_00A368FB;
    result = IoGetTransactionParameterBlock(a1, a3 + 16, a3, (unsigned int)(0x90098ULL));
    if (result != 0) goto loc_00A37052;
    if ((*(unsigned __int64 *)(a3)) == v_stack_m2C0) goto loc_00A3702B;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, a3 + 16, a3, (unsigned int)(0x90098ULL));
    if (result != 0) goto loc_00A37052;
    if ((*(unsigned __int64 *)(a3)) == v_stack_m2C0) goto loc_00A3702B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2B0 + 8) + 52)))) & (16)) == 0) goto loc_00A36DB7;
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m258, 20, (unsigned int)(0x1400E8ULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m198, 64, (unsigned int)(0x900C0ULL));
    v_stack_m2C8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A36902;
    goto loc_00A36E65;
loc_00A3702B:
    result = IoGetTransactionParameterBlock(a1, v_stack_m198, 64, (unsigned int)(0x900C0ULL));
    if (result != 0) goto loc_00A37052;
    if ((*(unsigned __int64 *)(a3)) == v_stack_m2C0) goto loc_00A36F5A;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, v_stack_m198, 64, (unsigned int)(0x900C0ULL));
    if (result == 0) goto loc_00A36F5A;
loc_00A37052:
    goto loc_00A368FE;
loc_00A3705C:
    if (a6 != 0) goto loc_00A370F3;
loc_00A3706A:
    if (v_stack_m2B0 != 0) {
        a1 = v_stack_m2B0;
        result = ObfDereferenceObject(a1, v_stack_m198, 64, (unsigned int)(0x900C0ULL));
    }
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_stack_m2C0, a2, a3, (unsigned int)(0x900C0ULL));
loc_00A37084:
loc_00A37086:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)(0x900C0ULL));
    v_rsp = (v_rsp) + (704);
    return result;
loc_00A370AA:
    result = ExAllocatePool2(291, v_stack_m2C0, (unsigned int)(0x20206F49ULL), (unsigned int)(0x900C0ULL));
    v_stack_p50 = result;
    result = memcpy(result, 1, v_stack_m2C0, (unsigned int)(0x900C0ULL));
    goto loc_00A370EC;
loc_00A370EC:
    v_rbx = 0;
    goto loc_00A36840;
loc_00A370F3:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m2C0, (unsigned int)(0x900C0ULL));
    goto loc_00A3706A;
loc_00A37102:
    if (a6 != 0) goto loc_00A3717C;
loc_00A3710B:
    goto loc_00A37086;
loc_00A37115:
    if (a6 == ((unsigned __int8)(v_stack_m2C0))) goto loc_00A37084;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m2C0, (unsigned int)(0x900C0ULL));
    goto loc_00A37084;
loc_00A37132:
    if (a6 != 1) goto loc_00A3684F;
loc_00A37140:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m2C0, (unsigned int)(0x900C0ULL));
loc_00A37150:
    goto loc_00A37140;
loc_00A3715F:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m2C0, (unsigned int)(0x900C0ULL));
loc_00A3717C:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m2C0, (unsigned int)(0x900C0ULL));
    goto loc_00A3710B;
}
```

## 5. (Beta) C Style

```c
int64_t IopTrackLink(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, uint8_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1EC;
    uint64_t v_stack_m1F4;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m208;
    uint64_t v_stack_m218;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint32_t v_stack_m248;
    uint64_t v_stack_m24C;
    uint64_t v_stack_m254;
    uint64_t v_stack_m258;
    uint64_t v_stack_m268;
    uint64_t v_stack_m278;
    uint64_t v_stack_m288;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint8_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint32_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m48;
    uint64_t v_stack_p50;

    local_rsp = (local_rsp) - (704);
    result = (*(uint64_t *)(v_rip + 0x3D3FC2)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m2C0 = Arg5;
    v_stack_m2A0 = Arg5;
    local_rbx = 0;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    result = 0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1E8 = 0;
    Arg2 = 0;
    result = memset(v_stack_m238, Arg2, (uint32_t)((uint32_t)(local_rbx + 64)), Arg4);
    Arg2 = 0;
    result = memset(v_stack_m1D8, Arg2, (uint32_t)((uint32_t)(local_rbx + 64)), Arg4);
    result = 0;
    v_stack_m258 = v_xmm0;
    v_stack_m248 = 0;
    Arg2 = 0;
    result = memset(v_stack_m198, Arg2, (uint32_t)((uint32_t)(local_rbx + 64)), Arg4);
    Arg2 = 0;
    result = memset(v_stack_m158, Arg2, 272, Arg4);
    if (Arg6 != 0) goto loc_00A370AA;
    v_stack_m2A8 = Arg3;
loc_00A36840:
    if (*(uint64_t *)(Arg3) == 0) goto loc_00A37132;
loc_00A3684F:
    if (((uint32_t)((uint32_t)(Arg4))) < 12) goto loc_00A37102;
    if (((uint32_t)((uint32_t)(Arg4) - 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x8))))) goto loc_00A37150;
    if (((uint32_t)(*(uint32_t *)(Arg3 + 0x8)) + 36) > 256) goto loc_00A3715F;
    local_r13 = 0;
    if (*(uint64_t *)(Arg3) == 0) goto loc_00A368C0;
    v_stack_m2B0 = 0;
    v_stack_m2D0 = 0;
    v_stack_m2D8 = v_stack_m2B0;
    result = ObReferenceObjectByHandle(*(uint64_t *)(Arg3), local_r13 + 2, *(uint64_t *)(v_rip + 0x590259), Arg6);
    v_stack_m2B0 = v_stack_m2B0;
    if (sign_flag) goto loc_00A37115;
loc_00A368C0:
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34))))) == 0) goto loc_00A3690C;
    result = IopGetSetObjectId(Arg1, v_stack_m238, 16 + 48, (uint32_t)(0x9009CULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00A36F70;
loc_00A368FB:
loc_00A368FE:
    v_stack_m2C8 = 0;
loc_00A36902:
    goto loc_00A3705C;
loc_00A3690C:
    if ((*(uint64_t *)(Arg3)) == v_stack_m2C0) goto loc_00A36C18;
    if (((0) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2B0 + 0x8) + 0x34))))) != 0) goto loc_00A36D45;
    v_stack_m2B8 = (uint8_t)(v_stack_m2C0);
    result = IopGetSetObjectId(Arg1, v_stack_m238, 64, (uint32_t)(0x9009CULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00A368FB;
    if (sign_flag) goto loc_00A36902;
    Arg3 = 0;
    result = RtlCompareMemoryUlong(v_stack_m218, Arg3 + 16, Arg3, (uint32_t)(0x9009CULL));
    if (result == 16) goto loc_00A368FB;
    result = IoGetTransactionParameterBlock(Arg1, Arg3 + 16, Arg3, (uint32_t)(0x9009CULL));
    if (result != 0) goto loc_00A37052;
    if ((*(uint64_t *)(Arg3)) == v_stack_m2C0) goto loc_00A3699A;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, Arg3 + 16, Arg3, (uint32_t)(0x9009CULL));
    if (result != 0) goto loc_00A37052;
loc_00A3699A:
    result = IopGetVolumeId(v_stack_m2B0, v_stack_m258, Arg3, (uint32_t)(0x9009CULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopGetVolumeId(Arg1, v_stack_m1F8, Arg3, (uint32_t)(0x9009CULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A36902;
    Arg3 = 0;
    Arg2 = 0;
    result = IopGetSetObjectId(Arg1, Arg2, Arg3, (uint32_t)(0x900A0ULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A36902;
    v_stack_m198 = v_xmm3;
    v_stack_m188 = v_xmm2;
    v_stack_m178 = v_xmm1;
    v_stack_m168 = v_xmm0;
    v_stack_m1D8 = v_xmm3;
    v_stack_m1C8 = v_xmm2;
    v_stack_m1B8 = v_xmm1;
    v_stack_m1A8 = v_xmm0;
    result = (v_stack_m254) - (v_stack_m1F4);
    if (!(condition_is_not_equal)) {
        result = v_stack_m24C;
        result = (result) - (v_stack_m1EC);
    }
    if (result != 0) {
        result = v_stack_m228;
        result = (uint8_t)((result) | (1));
        v_stack_m1C8 = (uint8_t)(result);
    }
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m1D8, 64, (uint32_t)(0x90098ULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (((uint32_t)(result)) == 0xC00000BDULL) goto loc_00A36ABF;
    if (((uint32_t)(result)) != 0xC0000035ULL) goto loc_00A36B07;
loc_00A36ABF:
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m198, 64, (uint32_t)(0x900C0ULL));
    v_stack_m2C8 = (uint32_t)(result);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg4 = 0x900BCULL;
        Arg3 = 48;
        Arg2 = v_stack_m1C8;
        Arg1 = v_stack_m2B0;
        result = IopGetSetObjectId(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
        v_stack_m2C8 = (uint32_t)(result);
    }
    if (sign_flag) goto loc_00A36BCE;
    v_stack_m2B8 = 1;
    result = (v_stack_m254) - (v_stack_m1F4);
    if (!(condition_is_not_equal)) {
        result = v_stack_m24C;
        result = (result) - (v_stack_m1EC);
    }
    if (result != 0) {
        Arg4 = Arg3;
        Arg3 = v_stack_m198;
        Arg2 = v_stack_m258;
        Arg1 = v_stack_m158;
        result = IopMarshalIds(Arg1, Arg2, Arg3, Arg4);
        v_stack_m298 = v_xmm0;
        v_stack_m288 = v_xmm2;
        v_stack_m278 = v_xmm0;
        v_stack_m268 = v_xmm1;
        result = (uint8_t)((result) & (254));
        v_stack_m288 = (uint8_t)(result);
        Arg3 = v_stack_m158;
        Arg2 = v_stack_m298;
        Arg1 = v_stack_m1F8;
        result = IopSendMessageToTrackService(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
        v_stack_m2C8 = (uint32_t)(result);
    }
    if (!sign_flag) goto loc_00A36902;
loc_00A36BCE:
    if (1 == 0) goto loc_00A36D1C;
    result = (v_stack_m198) - (v_stack_m238);
    if (!(condition_is_not_equal)) {
        result = v_stack_m190;
        result = (result) - (v_stack_m230);
    }
    if (result != 0) goto loc_00A36D03;
    Arg3 = 0;
    Arg2 = 0;
    goto loc_00A36D17;
loc_00A36C18:
    result = IopGetVolumeId(Arg1, v_stack_m1F8, Arg3, (uint32_t)(0x900A0ULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopGetSetObjectId(Arg1, v_stack_m238, 64, (uint32_t)(0x9009CULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A36902;
    Arg3 = 0;
    result = RtlCompareMemoryUlong(v_stack_m218, Arg3 + 16, Arg3, (uint32_t)(0x9009CULL));
    if (result == 16) goto loc_00A368FB;
    result = IoGetTransactionParameterBlock(Arg1, Arg3 + 16, Arg3, (uint32_t)(0x9009CULL));
    if (result != 0) goto loc_00A37052;
    if ((*(uint64_t *)(Arg3)) == v_stack_m2C0) goto loc_00A36CA5;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, Arg3 + 16, Arg3, (uint32_t)(0x9009CULL));
    if (result != 0) goto loc_00A37052;
loc_00A36CA5:
    v_stack_m298 = v_xmm0;
    v_stack_m288 = v_xmm2;
    v_stack_m278 = v_xmm0;
    v_stack_m268 = v_xmm1;
    result = (uint8_t)((result) & (254));
    v_stack_m288 = (uint8_t)(result);
    result = IopSendMessageToTrackService(v_stack_m1F8, v_stack_m298, 0, (uint32_t)(0x9009CULL));
    goto loc_00A36F65;
loc_00A36D03:
loc_00A36D17:
    result = IopGetSetObjectId(v_stack_m1F8, v_stack_m188, 48, (uint32_t)(0x900BCULL));
loc_00A36D1C:
    if (sign_flag) goto loc_00A36902;
    result = IopGetSetObjectId(Arg1, v_stack_m238, 64, (uint32_t)(0x90098ULL));
    goto loc_00A36902;
loc_00A36D45:
    result = IopGetSetObjectId(Arg1, v_stack_m238, 64, (uint32_t)(0x90098ULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A368FB;
    Arg3 = 0;
    result = RtlCompareMemoryUlong(v_stack_m218, (uint32_t)((uint32_t)(result)), Arg3, (uint32_t)(0x90098ULL));
    if (result == ((uint32_t)((uint32_t)(result)))) goto loc_00A368FB;
    result = IoGetTransactionParameterBlock(Arg1, (uint32_t)((uint32_t)(result)), Arg3, (uint32_t)(0x90098ULL));
    if (result != 0) goto loc_00A37052;
    if ((*(uint64_t *)(Arg3)) == v_stack_m2C0) goto loc_00A36D99;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, (uint32_t)((uint32_t)(result)), Arg3, (uint32_t)(0x90098ULL));
    if (result != 0) goto loc_00A37052;
loc_00A36D99:
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m258, 20, (uint32_t)(0x1400E8ULL));
    goto loc_00A36DBC;
loc_00A36DB7:
    result = IopGetVolumeId(v_stack_m2B0, v_stack_m258, 20, (uint32_t)(0x1400E8ULL));
loc_00A36DBC:
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m198, 64, (uint32_t)(0x900C0ULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopMarshalIds(v_stack_m158, v_stack_m258, v_stack_m198, 0);
    Arg4 = (uint32_t)(((uint32_t)(v_stack_m150)) + (12));
    v_stack_m2D0 = (uint8_t)(v_stack_m2C0);
    v_stack_m2D8 = v_stack_m2C0;
    result = IopTrackLink(Arg1, 1, v_stack_m158, Arg4);
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A3705C;
    Arg3 = 0;
    Arg2 = 0;
    result = IopGetSetObjectId(Arg1, Arg2, Arg3, (uint32_t)(0x900A0ULL));
    goto loc_00A36EB3;
loc_00A36E65:
    result = IopMarshalIds(v_stack_m158, v_stack_m258, v_stack_m198, 0);
    Arg4 = (uint32_t)(((uint32_t)(v_stack_m150)) + (12));
    v_stack_m2D0 = (uint8_t)(v_stack_m2C0);
    v_stack_m2D8 = v_stack_m2C0;
    result = IopTrackLink(Arg1, 1, v_stack_m158, Arg4);
loc_00A36EB3:
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A3705C;
    v_stack_m1D8 = v_xmm0;
    v_stack_m1C8 = v_xmm2;
    v_stack_m1B8 = v_xmm0;
    v_stack_m1A8 = v_xmm1;
    result = (uint8_t)((result) | (1));
    v_stack_m1C8 = (uint8_t)(result);
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m1C8, 48, (uint32_t)(0x900BCULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (!sign_flag) goto loc_00A3705C;
    result = IopGetSetObjectId(Arg1, v_stack_m238, 64, (uint32_t)(0x90098ULL));
    goto loc_00A3705C;
loc_00A36F5A:
    result = IopSetRemoteLink(Arg1, v_stack_m238, 0, (uint32_t)(0x90098ULL));
loc_00A36F65:
    v_stack_m2C8 = (uint32_t)(result);
    goto loc_00A36902;
loc_00A36F70:
    if (sign_flag) goto loc_00A36902;
    Arg3 = 0;
    result = RtlCompareMemoryUlong(v_stack_m218, Arg3 + 16, Arg3, (uint32_t)(0x90098ULL));
    if (result == 16) goto loc_00A368FB;
    result = IoGetTransactionParameterBlock(Arg1, Arg3 + 16, Arg3, (uint32_t)(0x90098ULL));
    if (result != 0) goto loc_00A37052;
    if ((*(uint64_t *)(Arg3)) == v_stack_m2C0) goto loc_00A3702B;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, Arg3 + 16, Arg3, (uint32_t)(0x90098ULL));
    if (result != 0) goto loc_00A37052;
    if ((*(uint64_t *)(Arg3)) == v_stack_m2C0) goto loc_00A3702B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2B0 + 0x8) + 0x34)))) & (16)) == 0) goto loc_00A36DB7;
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m258, 20, (uint32_t)(0x1400E8ULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A36902;
    result = IopGetSetObjectId(v_stack_m2B0, v_stack_m198, 64, (uint32_t)(0x900C0ULL));
    v_stack_m2C8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A36902;
    goto loc_00A36E65;
loc_00A3702B:
    result = IoGetTransactionParameterBlock(Arg1, v_stack_m198, 64, (uint32_t)(0x900C0ULL));
    if (result != 0) goto loc_00A37052;
    if ((*(uint64_t *)(Arg3)) == v_stack_m2C0) goto loc_00A36F5A;
    result = IoGetTransactionParameterBlock(v_stack_m2B0, v_stack_m198, 64, (uint32_t)(0x900C0ULL));
    if (result == 0) goto loc_00A36F5A;
loc_00A37052:
    goto loc_00A368FE;
loc_00A3705C:
    if (Arg6 != 0) goto loc_00A370F3;
loc_00A3706A:
    if (v_stack_m2B0 != 0) {
        Arg1 = v_stack_m2B0;
        result = ObfDereferenceObject(Arg1, v_stack_m198, 64, (uint32_t)(0x900C0ULL));
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_stack_m2C0, Arg2, Arg3, (uint32_t)(0x900C0ULL));
loc_00A37084:
loc_00A37086:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (uint32_t)(0x900C0ULL));
    local_rsp = (local_rsp) + (704);
    return result;
loc_00A370AA:
    result = ExAllocatePool2(291, v_stack_m2C0, (uint32_t)(0x20206F49ULL), (uint32_t)(0x900C0ULL));
    v_stack_p50 = result;
    result = memcpy(result, 1, v_stack_m2C0, (uint32_t)(0x900C0ULL));
    goto loc_00A370EC;
loc_00A370EC:
    local_rbx = 0;
    goto loc_00A36840;
loc_00A370F3:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m2C0, (uint32_t)(0x900C0ULL));
    goto loc_00A3706A;
loc_00A37102:
    if (Arg6 != 0) goto loc_00A3717C;
loc_00A3710B:
    goto loc_00A37086;
loc_00A37115:
    if (Arg6 == ((uint8_t)(v_stack_m2C0))) goto loc_00A37084;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m2C0, (uint32_t)(0x900C0ULL));
    goto loc_00A37084;
loc_00A37132:
    if (Arg6 != 1) goto loc_00A3684F;
loc_00A37140:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m2C0, (uint32_t)(0x900C0ULL));
loc_00A37150:
    goto loc_00A37140;
loc_00A3715F:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m2C0, (uint32_t)(0x900C0ULL));
loc_00A3717C:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m2C0, (uint32_t)(0x900C0ULL));
    goto loc_00A3710B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A36764&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
