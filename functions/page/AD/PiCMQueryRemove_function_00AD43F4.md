# PiCMQueryRemove

- RVA: `0x00AD43F4`–`0x00AD4840` (길이 `1,100` bytes)
- VA: `0x0000000140AD43F4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEC14`
- 디코드: `291`개 명령, `1,100/1,100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00AD4477` → [PiCMCaptureObjectInputData](../8E/PiCMCaptureObjectInputData_function_008E8220.md) (function, `0x008E8220`)
- `0x00AD44AB` → [McTemplateK0dz_EtwWriteTransfer](../../text/42/McTemplateK0dz_EtwWriteTransfer_function_0042316C.md) (function, `0x0042316C`)
- `0x00AD44DC` → [CmValidateDeviceName](../8F/CmValidateDeviceName_function_008F3CF0.md) (function, `0x008F3CF0`)
- `0x00AD44EE` → [CmIsRootDevice](../93/CmIsRootDevice_function_009325E4.md) (function, `0x009325E4`)
- `0x00AD451E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD4553` → [PiAuDoesClientHaveAccess](../96/PiAuDoesClientHaveAccess_function_00962940.md) (function, `0x00962940`)
- `0x00AD4563` → [PiAuDoesClientHavePrivilege](../96/PiAuDoesClientHavePrivilege_function_00964ADC.md) (function, `0x00964ADC`)
- `0x00AD45A9` → [CmGetDeviceStatus](../9D/CmGetDeviceStatus_function_009D154C.md) (function, `0x009D154C`)
- `0x00AD460C` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00AD4623` → [PiAuDoesClientHaveAccess](../96/PiAuDoesClientHaveAccess_function_00962940.md) (function, `0x00962940`)
- `0x00AD462F` → [PiAuDoesClientHavePrivilege](../96/PiAuDoesClientHavePrivilege_function_00964ADC.md) (function, `0x00964ADC`)
- `0x00AD4646` → [PnpGetCallerSessionId](../72/PnpGetCallerSessionId_function_0072C7C4.md) (function, `0x0072C7C4`)
- `0x00AD4651` → [RtlGetActiveConsoleId](../../text/43/RtlGetActiveConsoleId_function_00436230.md) (function, `0x00436230`)
- `0x00AD465F` → [PiAuCheckClientInteractive](../73/PiAuCheckClientInteractive_function_00731284.md) (function, `0x00731284`)
- `0x00AD4672` → [PiAuDoesClientHaveAccess](../96/PiAuDoesClientHaveAccess_function_00962940.md) (function, `0x00962940`)
- `0x00AD4680` → [PiAuDoesClientHavePrivilege](../96/PiAuDoesClientHavePrivilege_function_00964ADC.md) (function, `0x00964ADC`)
- `0x00AD46F3` → [PiAuDoesClientHaveAccess](../96/PiAuDoesClientHaveAccess_function_00962940.md) (function, `0x00962940`)
- `0x00AD4705` → [PiAuDoesClientHavePrivilege](../96/PiAuDoesClientHavePrivilege_function_00964ADC.md) (function, `0x00964ADC`)
- `0x00AD472E` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00AD475F` → [PnpQueueQueryAndRemoveEvent](../94/PnpQueueQueryAndRemoveEvent_function_0094FD2C.md) (function, `0x0094FD2C`)
- `0x00AD47D1` → [PiCMReturnBufferResultData](../8E/PiCMReturnBufferResultData_function_008ED6D0.md) (function, `0x008ED6D0`)
- `0x00AD47E5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD4800` → [McTemplateK0z_EtwWriteTransfer](../../text/4D/McTemplateK0z_EtwWriteTransfer_function_004DEF6C.md) (function, `0x004DEF6C`)
- `0x00AD481D` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)

### Direct callers
- [PiCMHandleIoctl](../8E/PiCMHandleIoctl_function_008EB880.md) at `0x008EC217`

### Static image references
- `0x00AD448D` → RVA `0x00EF012B` (`.data`; read)
- `0x00AD44A4` → RVA `0x00026FC0` (`.rdata`; read)
- `0x00AD4580` → RVA `0x00E66398` (`.data`; read)
- `0x00AD47F9` → RVA `0x00026EE0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00AD44AB` → [McTemplateK0dz_EtwWriteTransfer](../../text/42/McTemplateK0dz_EtwWriteTransfer_function_0042316C.md) (`PAGE` → `.text`)
  - `0x00AD451E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD4651` → [RtlGetActiveConsoleId](../../text/43/RtlGetActiveConsoleId_function_00436230.md) (`PAGE` → `.text`)
  - `0x00AD472E` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00AD47E5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD4800` → [McTemplateK0z_EtwWriteTransfer](../../text/4D/McTemplateK0z_EtwWriteTransfer_function_004DEF6C.md) (`PAGE` → `.text`)
  - `0x00AD481D` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD43F4  48 8B C4                        mov rax, rsp
00AD43F7  48 89 58 08                     mov qword ptr [rax + 8], rbx
00AD43FB  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00AD43FF  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00AD4403  55                              push rbp
00AD4404  56                              push rsi
00AD4405  57                              push rdi
00AD4406  41 54                           push r12
00AD4408  41 55                           push r13
00AD440A  41 56                           push r14
00AD440C  41 57                           push r15
00AD440E  48 8D 68 B1                     lea rbp, [rax - 0x4f]
00AD4412  48 81 EC C0 00 00 00            sub rsp, 0xc0
00AD4419  45 33 C0                        xor r8d, r8d
00AD441C  0F 57 C0                        xorps xmm0, xmm0
00AD441F  33 C0                           xor eax, eax
00AD4421  44 89 45 B3                     mov dword ptr [rbp - 0x4d], r8d
00AD4425  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00AD4429  41 8B F1                        mov esi, r9d
00AD442C  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00AD4430  4C 8D 4D D7                     lea r9, [rbp - 0x29]
00AD4434  44 89 45 C7                     mov dword ptr [rbp - 0x39], r8d
00AD4438  41 8B F8                        mov edi, r8d
00AD443B  44 89 45 C3                     mov dword ptr [rbp - 0x3d], r8d
00AD443F  45 8B F0                        mov r14d, r8d
00AD4442  44 89 45 BB                     mov dword ptr [rbp - 0x45], r8d
00AD4446  45 8B F8                        mov r15d, r8d
00AD4449  44 89 00                        mov dword ptr [rax], r8d
00AD444C  45 8B E0                        mov r12d, r8d
00AD444F  44 89 45 B7                     mov dword ptr [rbp - 0x49], r8d
00AD4453  44 89 45 CB                     mov dword ptr [rbp - 0x35], r8d
00AD4457  44 88 45 A7                     mov byte ptr [rbp - 0x59], r8b
00AD445B  44 89 45 BF                     mov dword ptr [rbp - 0x41], r8d
00AD445F  44 89 45 AB                     mov dword ptr [rbp - 0x55], r8d
00AD4463  44 89 45 AF                     mov dword ptr [rbp - 0x51], r8d
00AD4467  44 8B 45 77                     mov r8d, dword ptr [rbp + 0x77]
00AD446B  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00AD446F  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
00AD4473  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00AD4477  E8 A4 3D E1 FF                  call 0x1408e8220
00AD447C  4C 8B 6D E7                     mov r13, qword ptr [rbp - 0x19]
00AD4480  45 33 D2                        xor r10d, r10d
00AD4483  8B D8                           mov ebx, eax
00AD4485  85 C0                           test eax, eax
00AD4487  0F 88 60 03 00 00               js 0x140ad47ed
00AD448D  F6 05 97 BC 41 00 08            test byte ptr [rip + 0x41bc97], 8
00AD4494  49 8B DD                        mov rbx, r13
00AD4497  8B 7D F3                        mov edi, dword ptr [rbp - 0xd]
00AD449A  74 17                           je 0x140ad44b3
00AD449C  44 8B CF                        mov r9d, edi
00AD449F  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00AD44A4  48 8D 15 15 2B 55 FF            lea rdx, [rip - 0xaad4eb]
00AD44AB  E8 BC EC 94 FF                  call 0x14042316c
00AD44B0  45 33 D2                        xor r10d, r10d
00AD44B3  48 85 DB                        test rbx, rbx
00AD44B6  0F 84 BA 00 00 00               je 0x140ad4576
00AD44BC  83 7D DF 01                     cmp dword ptr [rbp - 0x21], 1
00AD44C0  0F 85 B0 00 00 00               jne 0x140ad4576
00AD44C6  4C 39 55 67                     cmp qword ptr [rbp + 0x67], r10
00AD44CA  0F 84 A6 00 00 00               je 0x140ad4576
00AD44D0  83 FE 14                        cmp esi, 0x14
00AD44D3  0F 82 9D 00 00 00               jb 0x140ad4576
00AD44D9  49 8B D5                        mov rdx, r13
00AD44DC  E8 0F F8 E1 FF                  call 0x1408f3cf0
00AD44E1  8B D8                           mov ebx, eax
00AD44E3  85 C0                           test eax, eax
00AD44E5  0F 88 BC 01 00 00               js 0x140ad46a7
00AD44EB  49 8B CD                        mov rcx, r13
00AD44EE  E8 F1 E0 E5 FF                  call 0x1409325e4
00AD44F3  84 C0                           test al, al
00AD44F5  74 0A                           je 0x140ad4501
00AD44F7  BB 33 00 00 C0                  mov ebx, 0xc0000033
00AD44FC  E9 9F 02 00 00                  jmp 0x140ad47a0
00AD4501  8D 46 EC                        lea eax, [rsi - 0x14]
00AD4504  41 8B F7                        mov esi, r15d
00AD4507  83 F8 02                        cmp eax, 2
00AD450A  0F 43 F0                        cmovae esi, eax
00AD450D  85 F6                           test esi, esi
00AD450F  74 28                           je 0x140ad4539
00AD4511  8B D6                           mov edx, esi
00AD4513  B9 00 01 00 00                  mov ecx, 0x100
00AD4518  41 B8 50 6E 70 34               mov r8d, 0x34706e50
00AD451E  E8 CD DB 0A 00                  call 0x140b820f0
00AD4523  4C 8B E0                        mov r12, rax
00AD4526  48 85 C0                        test rax, rax
00AD4529  75 0A                           jne 0x140ad4535
00AD452B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AD4530  E9 6B 02 00 00                  jmp 0x140ad47a0
00AD4535  66 44 89 38                     mov word ptr [rax], r15w
00AD4539  83 EF 01                        sub edi, 1
00AD453C  0F 84 AC 01 00 00               je 0x140ad46ee
00AD4542  83 EF 01                        sub edi, 1
00AD4545  0F 84 88 00 00 00               je 0x140ad45d3
00AD454B  83 FF 01                        cmp edi, 1
00AD454E  75 26                           jne 0x140ad4576
00AD4550  8D 4F 03                        lea ecx, [rdi + 3]
00AD4553  E8 E8 E3 E8 FF                  call 0x140962940
00AD4558  84 C0                           test al, al
00AD455A  0F 84 D8 00 00 00               je 0x140ad4638
00AD4560  8D 4F 09                        lea ecx, [rdi + 9]
00AD4563  E8 74 05 E9 FF                  call 0x140964adc
00AD4568  84 C0                           test al, al
00AD456A  0F 84 C8 00 00 00               je 0x140ad4638
00AD4570  44 39 7D DB                     cmp dword ptr [rbp - 0x25], r15d
00AD4574  74 0A                           je 0x140ad4580
00AD4576  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD457B  E9 20 02 00 00                  jmp 0x140ad47a0
00AD4580  48 8B 0D 11 1E 39 00            mov rcx, qword ptr [rip + 0x391e11]
00AD4587  48 8D 45 C3                     lea rax, [rbp - 0x3d]
00AD458B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AD4590  4C 8D 4D B3                     lea r9, [rbp - 0x4d]
00AD4594  48 8D 45 C7                     lea rax, [rbp - 0x39]
00AD4598  45 33 C0                        xor r8d, r8d
00AD459B  49 8B D5                        mov rdx, r13
00AD459E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AD45A3  41 BE 02 00 00 00               mov r14d, 2
00AD45A9  E8 9E CF EF FF                  call 0x1409d154c
00AD45AE  85 C0                           test eax, eax
00AD45B0  78 17                           js 0x140ad45c9
00AD45B2  F7 45 B3 00 20 00 00            test dword ptr [rbp - 0x4d], 0x2000
00AD45B9  0F 85 68 01 00 00               jne 0x140ad4727
00AD45BF  BB 10 00 00 C0                  mov ebx, 0xc0000010
00AD45C4  E9 D7 01 00 00                  jmp 0x140ad47a0
00AD45C9  BB 0E 00 00 C0                  mov ebx, 0xc000000e
00AD45CE  E9 CD 01 00 00                  jmp 0x140ad47a0
00AD45D3  48 8B 0D BE 1D 39 00            mov rcx, qword ptr [rip + 0x391dbe]
00AD45DA  48 8D 45 B7                     lea rax, [rbp - 0x49]
00AD45DE  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
00AD45E3  BF 04 00 00 00                  mov edi, 4
00AD45E8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AD45ED  45 33 C0                        xor r8d, r8d
00AD45F0  48 8D 45 BB                     lea rax, [rbp - 0x45]
00AD45F4  89 7D B7                        mov dword ptr [rbp - 0x49], edi
00AD45F7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AD45FC  49 8B D5                        mov rdx, r13
00AD45FF  48 8D 45 CB                     lea rax, [rbp - 0x35]
00AD4603  44 8D 4F 0C                     lea r9d, [rdi + 0xc]
00AD4607  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AD460C  E8 5F 92 E1 FF                  call 0x1408ed870
00AD4611  8B D8                           mov ebx, eax
00AD4613  85 C0                           test eax, eax
00AD4615  0F 88 81 00 00 00               js 0x140ad469c
00AD461B  F6 45 BB 08                     test byte ptr [rbp - 0x45], 8
00AD461F  74 21                           je 0x140ad4642
00AD4621  8B CF                           mov ecx, edi
00AD4623  E8 18 E3 E8 FF                  call 0x140962940
00AD4628  84 C0                           test al, al
00AD462A  74 0C                           je 0x140ad4638
00AD462C  8D 4F 15                        lea ecx, [rdi + 0x15]
00AD462F  E8 A8 04 E9 FF                  call 0x140964adc
00AD4634  84 C0                           test al, al
00AD4636  75 54                           jne 0x140ad468c
00AD4638  BB 22 00 00 C0                  mov ebx, 0xc0000022
00AD463D  E9 5E 01 00 00                  jmp 0x140ad47a0
00AD4642  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00AD4646  E8 79 81 C5 FF                  call 0x14072c7c4
00AD464B  8B D8                           mov ebx, eax
00AD464D  85 C0                           test eax, eax
00AD464F  78 0A                           js 0x140ad465b
00AD4651  E8 DA 1B 96 FF                  call 0x140436230
00AD4656  39 45 BF                        cmp dword ptr [rbp - 0x41], eax
00AD4659  74 31                           je 0x140ad468c
00AD465B  48 8D 4D A7                     lea rcx, [rbp - 0x59]
00AD465F  E8 20 CC C5 FF                  call 0x140731284
00AD4664  8B D8                           mov ebx, eax
00AD4666  85 C0                           test eax, eax
00AD4668  78 06                           js 0x140ad4670
00AD466A  44 38 7D A7                     cmp byte ptr [rbp - 0x59], r15b
00AD466E  75 1C                           jne 0x140ad468c
00AD4670  8B CF                           mov ecx, edi
00AD4672  E8 C9 E2 E8 FF                  call 0x140962940
00AD4677  84 C0                           test al, al
00AD4679  74 BD                           je 0x140ad4638
00AD467B  B9 0A 00 00 00                  mov ecx, 0xa
00AD4680  E8 57 04 E9 FF                  call 0x140964adc
00AD4685  84 C0                           test al, al
00AD4687  74 AF                           je 0x140ad4638
00AD4689  41 8B DF                        mov ebx, r15d
00AD468C  44 39 7D DB                     cmp dword ptr [rbp - 0x25], r15d
00AD4690  0F 85 E0 FE FF FF               jne 0x140ad4576
00AD4696  41 BE 08 00 00 00               mov r14d, 8
00AD469C  44 8B FE                        mov r15d, esi
00AD469F  85 DB                           test ebx, ebx
00AD46A1  0F 89 80 00 00 00               jns 0x140ad4727
00AD46A7  B9 28 00 00 80                  mov ecx, 0x80000028
00AD46AC  3B D9                           cmp ebx, ecx
00AD46AE  0F 85 E9 00 00 00               jne 0x140ad479d
00AD46B4  44 8B 45 AB                     mov r8d, dword ptr [rbp - 0x55]
00AD46B8  45 3B C7                        cmp r8d, r15d
00AD46BB  0F 87 DC 00 00 00               ja 0x140ad479d
00AD46C1  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00AD46C5  4D 8B CC                        mov r9, r12
00AD46C8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AD46CD  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
00AD46D0  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00AD46D4  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00AD46D8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AD46DD  8B 45 F7                        mov eax, dword ptr [rbp - 9]
00AD46E0  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AD46E4  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
00AD46E9  E9 DC 00 00 00                  jmp 0x140ad47ca
00AD46EE  B9 20 00 00 00                  mov ecx, 0x20
00AD46F3  E8 48 E2 E8 FF                  call 0x140962940
00AD46F8  84 C0                           test al, al
00AD46FA  0F 84 38 FF FF FF               je 0x140ad4638
00AD4700  B9 0A 00 00 00                  mov ecx, 0xa
00AD4705  E8 D2 03 E9 FF                  call 0x140964adc
00AD470A  84 C0                           test al, al
00AD470C  0F 84 26 FF FF FF               je 0x140ad4638
00AD4712  44 8B 75 DB                     mov r14d, dword ptr [rbp - 0x25]
00AD4716  41 F7 C6 FE FF FF FF            test r14d, 0xfffffffe
00AD471D  0F 85 53 FE FF FF               jne 0x140ad4576
00AD4723  41 83 E6 01                     and r14d, 1
00AD4727  49 8B D5                        mov rdx, r13
00AD472A  48 8D 4D FF                     lea rcx, [rbp - 1]
00AD472E  E8 2D F2 98 FF                  call 0x140463960
00AD4733  8B D8                           mov ebx, eax
00AD4735  44 8B FE                        mov r15d, esi
00AD4738  85 C0                           test eax, eax
00AD473A  0F 88 67 FF FF FF               js 0x140ad46a7
00AD4740  45 33 FF                        xor r15d, r15d
00AD4743  89 75 AB                        mov dword ptr [rbp - 0x55], esi
00AD4746  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00AD474B  4C 8D 4D AB                     lea r9, [rbp - 0x55]
00AD474F  4D 8B C4                        mov r8, r12
00AD4752  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00AD4757  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00AD475B  48 8D 4D FF                     lea rcx, [rbp - 1]
00AD475F  E8 C8 B5 E7 FF                  call 0x14094fd2c
00AD4764  B9 28 00 00 80                  mov ecx, 0x80000028
00AD4769  8B D8                           mov ebx, eax
00AD476B  3B C1                           cmp eax, ecx
00AD476D  75 26                           jne 0x140ad4795
00AD476F  44 8B 45 AB                     mov r8d, dword ptr [rbp - 0x55]
00AD4773  33 FF                           xor edi, edi
00AD4775  44 89 45 AB                     mov dword ptr [rbp - 0x55], r8d
00AD4779  44 8B FE                        mov r15d, esi
00AD477C  4D 85 E4                        test r12, r12
00AD477F  0F 84 33 FF FF FF               je 0x140ad46b8
00AD4785  8B C6                           mov eax, esi
00AD4787  48 D1 E8                        shr rax, 1
00AD478A  66 41 89 7C 44 FE               mov word ptr [r12 + rax*2 - 2], di
00AD4790  E9 23 FF FF FF                  jmp 0x140ad46b8
00AD4795  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00AD4798  89 45 AB                        mov dword ptr [rbp - 0x55], eax
00AD479B  EB 03                           jmp 0x140ad47a0
00AD479D  45 33 FF                        xor r15d, r15d
00AD47A0  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00AD47A4  45 33 C9                        xor r9d, r9d
00AD47A7  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AD47AC  8B CB                           mov ecx, ebx
00AD47AE  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
00AD47B1  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00AD47B5  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00AD47B9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AD47BE  8B 45 F7                        mov eax, dword ptr [rbp - 9]
00AD47C1  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AD47C5  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00AD47CA  44 8B 45 AF                     mov r8d, dword ptr [rbp - 0x51]
00AD47CE  8B 55 AB                        mov edx, dword ptr [rbp - 0x55]
00AD47D1  E8 FA 8E E1 FF                  call 0x1408ed6d0
00AD47D6  8B D8                           mov ebx, eax
00AD47D8  4D 85 E4                        test r12, r12
00AD47DB  74 0D                           je 0x140ad47ea
00AD47DD  BA 50 6E 70 34                  mov edx, 0x34706e50
00AD47E2  49 8B CC                        mov rcx, r12
00AD47E5  E8 86 E0 0A 00                  call 0x140b82870
00AD47EA  49 8B FD                        mov rdi, r13
00AD47ED  F6 05 37 B9 41 00 08            test byte ptr [rip + 0x41b937], 8
00AD47F4  74 0F                           je 0x140ad4805
00AD47F6  4C 8B CF                        mov r9, rdi
00AD47F9  48 8D 15 E0 26 55 FF            lea rdx, [rip - 0xaad920]
00AD4800  E8 67 A7 A0 FF                  call 0x1404def6c
00AD4805  4D 85 ED                        test r13, r13
00AD4808  74 18                           je 0x140ad4822
00AD480A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AD4813  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
00AD4817  8A 89 32 02 00 00               mov cl, byte ptr [rcx + 0x232]
00AD481D  E8 6E 41 97 FF                  call 0x140448990
00AD4822  8B C3                           mov eax, ebx
00AD4824  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
00AD482C  48 81 C4 C0 00 00 00            add rsp, 0xc0
00AD4833  41 5F                           pop r15
00AD4835  41 5E                           pop r14
00AD4837  41 5D                           pop r13
00AD4839  41 5C                           pop r12
00AD483B  5F                              pop rdi
00AD483C  5E                              pop rsi
00AD483D  5D                              pop rbp
00AD483E  C3                              ret
00AD483F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiCMQueryRemove(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (192);
    a3 = 0;
    result = 0;
    *(unsigned int *)(v_rsp - 79 - 77) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 9) = 0;
    *(unsigned int *)(v_rsp - 79 - 57) = 0;
    *(unsigned int *)(v_rsp - 79 - 61) = 0;
    *(unsigned int *)(v_rsp - 79 - 69) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 127)) = 0;
    *(unsigned int *)(v_rsp - 79 - 73) = 0;
    *(unsigned int *)(v_rsp - 79 - 53) = 0;
    *(unsigned __int8 *)(v_rsp - 79 - 89) = 0;
    *(unsigned int *)(v_rsp - 79 - 65) = 0;
    *(unsigned int *)(v_rsp - 79 - 85) = 0;
    *(unsigned int *)(v_rsp - 79 - 81) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 1) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 79 - 41) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 79 - 25) = v_xmm0;
    result = PiCMCaptureObjectInputData(a1, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)), v_rsp - 79 - 41);
    v_r10 = 0;
    if (sign_flag) goto loc_00AD47ED;
    if (((*(unsigned __int8 *)(v_rip + 4308119)) & (8)) != 0) {
        a4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 13)));
        v_stack_mD8 = *(unsigned __int64 *)(v_rsp - 79 - 25);
        a2 = v_rip - 11195627;
        result = McTemplateK0dz_EtwWriteTransfer(a1, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)), a4);
        v_r10 = 0;
    }
    if (*(unsigned __int64 *)(v_rsp - 79 - 25) == 0) goto loc_00AD4576;
    if ((*(unsigned int *)(v_rsp - 79 - 33)) != 1) goto loc_00AD4576;
    if ((*(unsigned __int64 *)(v_rsp - 79 + 103)) == 0) goto loc_00AD4576;
    if (((unsigned int)((unsigned int)(a4))) < 20) goto loc_00AD4576;
    result = CmValidateDeviceName(a1, *(unsigned __int64 *)(v_rsp - 79 - 25), (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)), a4);
    if (sign_flag) goto loc_00AD46A7;
    result = CmIsRootDevice(*(unsigned __int64 *)(v_rsp - 79 - 25), *(unsigned __int64 *)(v_rsp - 79 - 25), (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AD4501;
    goto loc_00AD47A0;
loc_00AD4501:
    v_rsi = 0;
    if (((unsigned int)((unsigned int)(a4) - 20)) >= 2) { v_rsi = (unsigned int)((unsigned int)(a4) - 20); }
    if ((unsigned int)(v_rsi) == 0) goto loc_00AD4539;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x34706E50ULL), a4);
    if (result != 0) goto loc_00AD4535;
    goto loc_00AD47A0;
loc_00AD4535:
    *(unsigned __int16 *)(result) = 0;
loc_00AD4539:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 79 - 13))) - (1));
    if (condition_is_equal) goto loc_00AD46EE;
    v_rdi = (unsigned int)((v_rdi) - (1));
    if (condition_is_equal) goto loc_00AD45D3;
    if (((unsigned int)(v_rdi)) != 1) goto loc_00AD4576;
    result = PiAuDoesClientHaveAccess(v_rdi + 3, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x34706E50ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AD4638;
    result = PiAuDoesClientHavePrivilege(v_rdi + 9, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x34706E50ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AD4638;
    if ((*(unsigned int *)(v_rsp - 79 - 37)) == 0) goto loc_00AD4580;
loc_00AD4576:
    goto loc_00AD47A0;
loc_00AD4580:
    v_stack_mD0 = v_rsp - 79 - 61;
    a3 = 0;
    v_stack_mD8 = v_rsp - 79 - 57;
    result = CmGetDeviceStatus(*(unsigned __int64 *)(v_rip + 3743249), *(unsigned __int64 *)(v_rsp - 79 - 25), a3, v_rsp - 79 - 77);
    if (sign_flag) goto loc_00AD45C9;
    if (((*(unsigned int *)(v_rsp - 79 - 77)) & (0x2000ULL)) != 0) goto loc_00AD4727;
    goto loc_00AD47A0;
loc_00AD45C9:
    goto loc_00AD47A0;
loc_00AD45D3:
    v_stack_mC0 = 0;
    v_stack_mC8 = v_rsp - 79 - 73;
    a3 = 0;
    *(unsigned int *)(v_rsp - 79 - 73) = 4;
    v_stack_mD0 = v_rsp - 79 - 69;
    v_stack_mD8 = v_rsp - 79 - 53;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 3743166), *(unsigned __int64 *)(v_rsp - 79 - 25), a3, 4 + 12);
    if (sign_flag) goto loc_00AD469C;
    if (((*(unsigned __int8 *)(v_rsp - 79 - 69)) & (8)) == 0) goto loc_00AD4642;
    result = PiAuDoesClientHaveAccess(4, *(unsigned __int64 *)(v_rsp - 79 - 25), a3, 4 + 12);
    if ((unsigned __int8)(result) == 0) goto loc_00AD4638;
    result = PiAuDoesClientHavePrivilege(4 + 21, *(unsigned __int64 *)(v_rsp - 79 - 25), a3, 4 + 12);
    if ((unsigned __int8)(result) != 0) goto loc_00AD468C;
loc_00AD4638:
    goto loc_00AD47A0;
loc_00AD4642:
    result = PnpGetCallerSessionId(v_rsp - 79 - 65, *(unsigned __int64 *)(v_rsp - 79 - 25), a3, 4 + 12);
    if (sign_flag) goto loc_00AD465B;
    result = RtlGetActiveConsoleId(v_rsp - 79 - 65, *(unsigned __int64 *)(v_rsp - 79 - 25), a3, 4 + 12);
    if ((*(unsigned int *)(v_rsp - 79 - 65)) == ((unsigned int)(result))) goto loc_00AD468C;
loc_00AD465B:
    result = PiAuCheckClientInteractive(v_rsp - 79 - 89, *(unsigned __int64 *)(v_rsp - 79 - 25), a3, 4 + 12);
    if (sign_flag) goto loc_00AD4670;
    if ((*(unsigned __int8 *)(v_rsp - 79 - 89)) != 0) goto loc_00AD468C;
loc_00AD4670:
    result = PiAuDoesClientHaveAccess(4, *(unsigned __int64 *)(v_rsp - 79 - 25), a3, 4 + 12);
    if ((unsigned __int8)(result) == 0) goto loc_00AD4638;
    result = PiAuDoesClientHavePrivilege(10, *(unsigned __int64 *)(v_rsp - 79 - 25), a3, 4 + 12);
    if ((unsigned __int8)(result) == 0) goto loc_00AD4638;
loc_00AD468C:
    if ((*(unsigned int *)(v_rsp - 79 - 37)) != 0) goto loc_00AD4576;
loc_00AD469C:
    if (!sign_flag) goto loc_00AD4727;
loc_00AD46A7:
    if (0 != ((unsigned int)((unsigned int)(0x80000028ULL)))) goto loc_00AD479D;
loc_00AD46B8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 85)))) > ((unsigned int)((unsigned int)((unsigned int)(v_rsi))))) goto loc_00AD479D;
    v_stack_mB8 = *(unsigned __int64 *)(v_rsp - 79 + 127);
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 111)));
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 79 + 103);
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 9)));
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 85)));
    goto loc_00AD47CA;
loc_00AD46EE:
    result = PiAuDoesClientHaveAccess(32, *(unsigned __int64 *)(v_rsp - 79 - 25), (unsigned int)(*(unsigned int *)(v_rsp - 79 - 85)), result);
    if ((unsigned __int8)(result) == 0) goto loc_00AD4638;
    result = PiAuDoesClientHavePrivilege(10, *(unsigned __int64 *)(v_rsp - 79 - 25), (unsigned int)(*(unsigned int *)(v_rsp - 79 - 85)), result);
    if ((unsigned __int8)(result) == 0) goto loc_00AD4638;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 37)))) & (0xFFFFFFFEULL)) != 0) goto loc_00AD4576;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 79 - 37))) & (1));
loc_00AD4727:
    result = RtlInitUnicodeStringEx(v_rsp - 79 - 1, *(unsigned __int64 *)(v_rsp - 79 - 25), (unsigned int)(*(unsigned int *)(v_rsp - 79 - 85)), result);
    if (sign_flag) goto loc_00AD46A7;
    v_r15 = 0;
    *(unsigned int *)(v_rsp - 79 - 85) = (unsigned int)(v_rsi);
    v_stack_mD0 = 0;
    v_stack_mD8 = (unsigned int)(v_r14);
    result = PnpQueueQueryAndRemoveEvent(v_rsp - 79 - 1, v_rsp - 79 - 81, result, v_rsp - 79 - 85);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x80000028ULL)))) goto loc_00AD4795;
    v_rdi = 0;
    *(unsigned int *)(v_rsp - 79 - 85) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 85)));
    if (result == 0) goto loc_00AD46B8;
    result = ((unsigned int)((unsigned int)(v_rsi))) >> (1);
    *(unsigned __int16 *)(result + result * 2 - 2) = 0;
    goto loc_00AD46B8;
loc_00AD4795:
    *(unsigned int *)(v_rsp - 79 - 85) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 85)));
    goto loc_00AD47A0;
loc_00AD479D:
    v_r15 = 0;
loc_00AD47A0:
    a4 = 0;
    v_stack_mB8 = *(unsigned __int64 *)(v_rsp - 79 + 127);
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 111)));
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 79 + 103);
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 9)));
    v_stack_mD8 = 0;
loc_00AD47CA:
    result = PiCMReturnBufferResultData((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(*(unsigned int *)(v_rsp - 79 - 85)), (unsigned int)(*(unsigned int *)(v_rsp - 79 - 81)), a4);
    if (result != 0) {
        a2 = 0x34706E50ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 - 81)), a4);
    }
loc_00AD47ED:
    if (((*(unsigned __int8 *)(v_rip + 4307255)) & (8)) != 0) {
        a4 = *(unsigned __int64 *)(v_rsp - 79 - 25);
        a2 = v_rip - 11196704;
        result = McTemplateK0z_EtwWriteTransfer(a1, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 - 81)), a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 79 - 25) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = *(unsigned __int64 *)(v_rsp - 79 - 25);
        a1 = *(unsigned __int8 *)(a1 + 562);
        result = PiControlFreeUserModeCallersBuffer(a1, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 - 81)), a4);
    }
    v_rsp = (v_rsp) + (192);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t PiCMQueryRemove(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (192);
    Arg3 = 0;
    result = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x4D) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x9) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x39) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x3D) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x45) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x7F)) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x49) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x35) = 0;
    *(uint8_t *)(local_rsp - 0x4F - 0x59) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x41) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x55) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x51) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x1) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x4F - 0x29) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x4F - 0x19) = v_xmm0;
    result = PiCMCaptureObjectInputData(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)), local_rsp - 79 - 41);
    local_r10 = 0;
    if (sign_flag) goto loc_00AD47ED;
    if (((*(uint8_t *)(v_rip + 0x41BC97)) & (8)) != 0) {
        Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0xD)));
        v_stack_mD8 = *(uint64_t *)(local_rsp - 0x4F - 0x19);
        Arg2 = v_rip - 11195627;
        result = McTemplateK0dz_EtwWriteTransfer(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)), Arg4);
        local_r10 = 0;
    }
    if (*(uint64_t *)(local_rsp - 0x4F - 0x19) == 0) goto loc_00AD4576;
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x21)) != 1) goto loc_00AD4576;
    if ((*(uint64_t *)(local_rsp - 0x4F + 0x67)) == 0) goto loc_00AD4576;
    if (((uint32_t)((uint32_t)(Arg4))) < 20) goto loc_00AD4576;
    result = CmValidateDeviceName(Arg1, *(uint64_t *)(local_rsp - 0x4F - 0x19), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)), Arg4);
    if (sign_flag) goto loc_00AD46A7;
    result = CmIsRootDevice(*(uint64_t *)(local_rsp - 0x4F - 0x19), *(uint64_t *)(local_rsp - 0x4F - 0x19), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AD4501;
    goto loc_00AD47A0;
loc_00AD4501:
    local_rsi = 0;
    if (((uint32_t)((uint32_t)(Arg4) - 20)) >= 2) { local_rsi = (uint32_t)((uint32_t)(Arg4) - 20); }
    if ((uint32_t)(local_rsi) == 0) goto loc_00AD4539;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x34706E50ULL), Arg4);
    if (result != 0) goto loc_00AD4535;
    goto loc_00AD47A0;
loc_00AD4535:
    *(uint16_t *)(result) = 0;
loc_00AD4539:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0xD))) - (1));
    if (condition_is_equal) goto loc_00AD46EE;
    local_rdi = (uint32_t)((local_rdi) - (1));
    if (condition_is_equal) goto loc_00AD45D3;
    if (((uint32_t)(local_rdi)) != 1) goto loc_00AD4576;
    result = PiAuDoesClientHaveAccess(local_rdi + 3, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x34706E50ULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AD4638;
    result = PiAuDoesClientHavePrivilege(local_rdi + 9, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x34706E50ULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AD4638;
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x25)) == 0) goto loc_00AD4580;
loc_00AD4576:
    goto loc_00AD47A0;
loc_00AD4580:
    v_stack_mD0 = local_rsp - 79 - 61;
    Arg3 = 0;
    v_stack_mD8 = local_rsp - 79 - 57;
    result = CmGetDeviceStatus(*(uint64_t *)(v_rip + 0x391E11), *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, local_rsp - 79 - 77);
    if (sign_flag) goto loc_00AD45C9;
    if (((*(uint32_t *)(local_rsp - 0x4F - 0x4D)) & (0x2000ULL)) != 0) goto loc_00AD4727;
    goto loc_00AD47A0;
loc_00AD45C9:
    goto loc_00AD47A0;
loc_00AD45D3:
    v_stack_mC0 = 0;
    v_stack_mC8 = local_rsp - 79 - 73;
    Arg3 = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x49) = 4;
    v_stack_mD0 = local_rsp - 79 - 69;
    v_stack_mD8 = local_rsp - 79 - 53;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x391DBE), *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, 4 + 12);
    if (sign_flag) goto loc_00AD469C;
    if (((*(uint8_t *)(local_rsp - 0x4F - 0x45)) & (8)) == 0) goto loc_00AD4642;
    result = PiAuDoesClientHaveAccess(4, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, 4 + 12);
    if ((uint8_t)(result) == 0) goto loc_00AD4638;
    result = PiAuDoesClientHavePrivilege(4 + 21, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, 4 + 12);
    if ((uint8_t)(result) != 0) goto loc_00AD468C;
loc_00AD4638:
    goto loc_00AD47A0;
loc_00AD4642:
    result = PnpGetCallerSessionId(local_rsp - 79 - 65, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, 4 + 12);
    if (sign_flag) goto loc_00AD465B;
    result = RtlGetActiveConsoleId(local_rsp - 79 - 65, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, 4 + 12);
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x41)) == ((uint32_t)(result))) goto loc_00AD468C;
loc_00AD465B:
    result = PiAuCheckClientInteractive(local_rsp - 79 - 89, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, 4 + 12);
    if (sign_flag) goto loc_00AD4670;
    if ((*(uint8_t *)(local_rsp - 0x4F - 0x59)) != 0) goto loc_00AD468C;
loc_00AD4670:
    result = PiAuDoesClientHaveAccess(4, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, 4 + 12);
    if ((uint8_t)(result) == 0) goto loc_00AD4638;
    result = PiAuDoesClientHavePrivilege(10, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, 4 + 12);
    if ((uint8_t)(result) == 0) goto loc_00AD4638;
loc_00AD468C:
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x25)) != 0) goto loc_00AD4576;
loc_00AD469C:
    if (!sign_flag) goto loc_00AD4727;
loc_00AD46A7:
    if (0 != ((uint32_t)((uint32_t)(0x80000028ULL)))) goto loc_00AD479D;
loc_00AD46B8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x55)))) > ((uint32_t)((uint32_t)((uint32_t)(local_rsi))))) goto loc_00AD479D;
    v_stack_mB8 = *(uint64_t *)(local_rsp - 0x4F + 0x7F);
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x6F)));
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x4F + 0x67);
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x9)));
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x55)));
    goto loc_00AD47CA;
loc_00AD46EE:
    result = PiAuDoesClientHaveAccess(32, *(uint64_t *)(local_rsp - 0x4F - 0x19), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x55)), result);
    if ((uint8_t)(result) == 0) goto loc_00AD4638;
    result = PiAuDoesClientHavePrivilege(10, *(uint64_t *)(local_rsp - 0x4F - 0x19), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x55)), result);
    if ((uint8_t)(result) == 0) goto loc_00AD4638;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x25)))) & (0xFFFFFFFEULL)) != 0) goto loc_00AD4576;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x25))) & (1));
loc_00AD4727:
    result = RtlInitUnicodeStringEx(local_rsp - 79 - 1, *(uint64_t *)(local_rsp - 0x4F - 0x19), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x55)), result);
    if (sign_flag) goto loc_00AD46A7;
    local_r15 = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x55) = (uint32_t)(local_rsi);
    v_stack_mD0 = 0;
    v_stack_mD8 = (uint32_t)(local_r14);
    result = PnpQueueQueryAndRemoveEvent(local_rsp - 79 - 1, local_rsp - 79 - 81, result, local_rsp - 79 - 85);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x80000028ULL)))) goto loc_00AD4795;
    local_rdi = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x55) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x55)));
    if (result == 0) goto loc_00AD46B8;
    result = ((uint32_t)((uint32_t)(local_rsi))) >> (1);
    *(uint16_t *)(result + result * 2 - 0x2) = 0;
    goto loc_00AD46B8;
loc_00AD4795:
    *(uint32_t *)(local_rsp - 0x4F - 0x55) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x55)));
    goto loc_00AD47A0;
loc_00AD479D:
    local_r15 = 0;
loc_00AD47A0:
    Arg4 = 0;
    v_stack_mB8 = *(uint64_t *)(local_rsp - 0x4F + 0x7F);
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x6F)));
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x4F + 0x67);
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x9)));
    v_stack_mD8 = 0;
loc_00AD47CA:
    result = PiCMReturnBufferResultData((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x55)), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x51)), Arg4);
    if (result != 0) {
        Arg2 = 0x34706E50ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x51)), Arg4);
    }
loc_00AD47ED:
    if (((*(uint8_t *)(v_rip + 0x41B937)) & (8)) != 0) {
        Arg4 = *(uint64_t *)(local_rsp - 0x4F - 0x19);
        Arg2 = v_rip - 11196704;
        result = McTemplateK0z_EtwWriteTransfer(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x51)), Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x4F - 0x19) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = *(uint64_t *)(local_rsp - 0x4F - 0x19);
        Arg1 = *(uint8_t *)(Arg1 + 0x232);
        result = PiControlFreeUserModeCallersBuffer(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x51)), Arg4);
    }
    local_rsp = (local_rsp) + (192);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD43F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
