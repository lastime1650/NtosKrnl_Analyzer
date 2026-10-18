# SeCaptureSecurityDescriptor

- RVA: `0x00929F40`–`0x0092A760` (길이 `2,080` bytes)
- VA: `0x0000000140929F40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DA58`
- 디코드: `528`개 명령, `2,080/2,080` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00929FF3` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00929FF8` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0092A16D` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0092A20D` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0092A29B` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0092A2B9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0092A309` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092A319` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092A342` → [RtlValidAcl](RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x0092A37F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092A397` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092A3F7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092A40F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092A4A2` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0092A529` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092A539` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092A564` → [RtlValidAcl](RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x0092A5CE` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0092A661` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092A6CB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092A700` → [RtlLengthRequiredSid](../9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x0092A725` → [RtlLengthRequiredSid](../9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)

### Direct callers
- [SeAccessCheckByType](../../text/44/SeAccessCheckByType_function_00440BC8.md) at `0x004411A7`
- [CmpCopySaclToVirtualKey](../7E/CmpCopySaclToVirtualKey_function_007ECA6C.md) at `0x007ECC5C`
- [ObpCaptureObjectCreateInformation](../89/ObpCaptureObjectCreateInformation_function_0089B930.md) at `0x0089BB90`
- [NtCreateWnfStateName](../8B/NtCreateWnfStateName_function_008BE2B0.md) at `0x008BE374`
- [NtCreateWnfStateName](../8B/NtCreateWnfStateName_function_008BE2B0.md) at `0x008BE55A`
- [SeTokenDefaultDaclChangedAuditAlarm](SeTokenDefaultDaclChangedAuditAlarm_function_00920570.md) at `0x0092069A`
- [SeTokenDefaultDaclChangedAuditAlarm](SeTokenDefaultDaclChangedAuditAlarm_function_00920570.md) at `0x009206F0`
- [AlpcpConnectPort](AlpcpConnectPort_function_00926C8C.md) at `0x00926E3B`
- [NtOpenObjectAuditAlarm](../97/NtOpenObjectAuditAlarm_function_00974700.md) at `0x00974844`
- [PipGetRegistrySecurityWithFallback](../99/PipGetRegistrySecurityWithFallback_function_0099542C.md) at `0x009955B0`
- [PipGetRegistrySecurityWithFallback](../99/PipGetRegistrySecurityWithFallback_function_0099542C.md) at `0x0099564E`
- [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1B5E0`
- [IopQuerySecureDeviceClassState](../AB/IopQuerySecureDeviceClassState_function_00ABC9A4.md) at `0x00ABCA27`
- [NtSetSecurityObject](../AD/NtSetSecurityObject_function_00ADE2B0.md) at `0x00ADE3CB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x0092A29B` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`PAGE` → `POOLCODE`)
  - `0x0092A2B9` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092A309` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092A319` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092A37F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092A397` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092A3F7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092A40F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092A529` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092A539` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092A661` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092A6CB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00929F40  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00929F45  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00929F4A  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00929F4F  57                              push rdi
00929F50  41 54                           push r12
00929F52  41 55                           push r13
00929F54  41 56                           push r14
00929F56  41 57                           push r15
00929F58  48 81 EC B0 00 00 00            sub rsp, 0xb0
00929F5F  45 8B D8                        mov r11d, r8d
00929F62  44 0F B6 E2                     movzx r12d, dl
00929F66  4C 8B D1                        mov r10, rcx
00929F69  0F 57 C0                        xorps xmm0, xmm0
00929F6C  33 C0                           xor eax, eax
00929F6E  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00929F73  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00929F78  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00929F7D  45 33 F6                        xor r14d, r14d
00929F80  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00929F85  44 89 74 24 24                  mov dword ptr [rsp + 0x24], r14d
00929F8A  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00929F8F  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00929F94  44 89 74 24 3C                  mov dword ptr [rsp + 0x3c], r14d
00929F99  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
00929F9E  48 85 C9                        test rcx, rcx
00929FA1  0F 84 9E 04 00 00               je 0x14092a445
00929FA7  84 D2                           test dl, dl
00929FA9  0F 84 D9 06 00 00               je 0x14092a688
00929FAF  41 F6 C2 03                     test r10b, 3
00929FB3  75 43                           jne 0x140929ff8
00929FB5  49 B9 00 00 FF FF FF 7F 00 00   movabs r9, 0x7fffffff0000
00929FBF  49 8B C1                        mov rax, r9
00929FC2  4D 3B D1                        cmp r10, r9
00929FC5  49 0F 42 C2                     cmovb rax, r10
00929FC9  90                              nop
00929FCA  0F B6 00                        movzx eax, byte ptr [rax]
00929FCD  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00929FD0  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
00929FD8  44 8B 41 10                     mov r8d, dword ptr [rcx + 0x10]
00929FDC  66 48 0F 7E C2                  movq rdx, xmm0
00929FE1  48 8B C2                        mov rax, rdx
00929FE4  48 C1 E8 10                     shr rax, 0x10
00929FE8  66 85 C0                        test ax, ax
00929FEB  78 11                           js 0x140929ffe
00929FED  41 F6 C2 07                     test r10b, 7
00929FF1  74 0B                           je 0x140929ffe
00929FF3  E8 D8 FF F6 FF                  call 0x140899fd0
00929FF8  E8 D3 FF F6 FF                  call 0x140899fd0
00929FFD  CC                              int3
00929FFE  EB 05                           jmp 0x14092a005
0092A000  E9 4D 04 00 00                  jmp 0x14092a452
0092A005  80 FA 01                        cmp dl, 1
0092A008  0F 85 48 07 00 00               jne 0x14092a756
0092A00E  88 54 24 48                     mov byte ptr [rsp + 0x48], dl
0092A012  48 8B C2                        mov rax, rdx
0092A015  48 C1 E8 08                     shr rax, 8
0092A019  88 44 24 49                     mov byte ptr [rsp + 0x49], al
0092A01D  48 8B CA                        mov rcx, rdx
0092A020  48 C1 E9 10                     shr rcx, 0x10
0092A024  0F B7 C1                        movzx eax, cx
0092A027  BB FF 7F 00 00                  mov ebx, 0x7fff
0092A02C  66 23 C3                        and ax, bx
0092A02F  66 89 44 24 4A                  mov word ptr [rsp + 0x4a], ax
0092A034  66 85 C9                        test cx, cx
0092A037  0F 88 90 00 00 00               js 0x14092a0cd
0092A03D  49 8B 5A 08                     mov rbx, qword ptr [r10 + 8]
0092A041  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0092A046  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0092A04B  66 85 C9                        test cx, cx
0092A04E  78 32                           js 0x14092a082
0092A050  4D 8B 7A 10                     mov r15, qword ptr [r10 + 0x10]
0092A054  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0092A059  F6 C1 10                        test cl, 0x10
0092A05C  75 40                           jne 0x14092a09e
0092A05E  49 8B C6                        mov rax, r14
0092A061  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092A066  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0092A06B  F6 C1 04                        test cl, 4
0092A06E  74 29                           je 0x14092a099
0092A070  66 85 C9                        test cx, cx
0092A073  79 1E                           jns 0x14092a093
0092A075  45 85 C0                        test r8d, r8d
0092A078  74 4E                           je 0x14092a0c8
0092A07A  41 8B F8                        mov edi, r8d
0092A07D  49 03 FA                        add rdi, r10
0092A080  EB 64                           jmp 0x14092a0e6
0092A082  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
0092A089  85 C0                           test eax, eax
0092A08B  74 2B                           je 0x14092a0b8
0092A08D  4D 8D 3C 02                     lea r15, [r10 + rax]
0092A091  EB C1                           jmp 0x14092a054
0092A093  49 8B 7A 20                     mov rdi, qword ptr [r10 + 0x20]
0092A097  EB 4D                           jmp 0x14092a0e6
0092A099  49 8B FE                        mov rdi, r14
0092A09C  EB 48                           jmp 0x14092a0e6
0092A09E  66 85 C9                        test cx, cx
0092A0A1  79 1F                           jns 0x14092a0c2
0092A0A3  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0092A0AB  48 C1 E8 20                     shr rax, 0x20
0092A0AF  85 C0                           test eax, eax
0092A0B1  74 0A                           je 0x14092a0bd
0092A0B3  49 03 C2                        add rax, r10
0092A0B6  EB A9                           jmp 0x14092a061
0092A0B8  4D 8B FE                        mov r15, r14
0092A0BB  EB 97                           jmp 0x14092a054
0092A0BD  49 8B C6                        mov rax, r14
0092A0C0  EB 9F                           jmp 0x14092a061
0092A0C2  49 8B 42 18                     mov rax, qword ptr [r10 + 0x18]
0092A0C6  EB 99                           jmp 0x14092a061
0092A0C8  49 8B FE                        mov rdi, r14
0092A0CB  EB 19                           jmp 0x14092a0e6
0092A0CD  48 C1 EA 20                     shr rdx, 0x20
0092A0D1  85 D2                           test edx, edx
0092A0D3  74 09                           je 0x14092a0de
0092A0D5  49 8D 1C 12                     lea rbx, [r10 + rdx]
0092A0D9  E9 63 FF FF FF                  jmp 0x14092a041
0092A0DE  49 8B DE                        mov rbx, r14
0092A0E1  E9 5B FF FF FF                  jmp 0x14092a041
0092A0E6  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
0092A0EB  EB 05                           jmp 0x14092a0f2
0092A0ED  E9 60 03 00 00                  jmp 0x14092a452
0092A0F2  45 8B EE                        mov r13d, r14d
0092A0F5  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
0092A0FA  41 8B F6                        mov esi, r14d
0092A0FD  44 89 74 24 24                  mov dword ptr [rsp + 0x24], r14d
0092A102  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
0092A107  41 8B D6                        mov edx, r14d
0092A10A  89 94 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], edx
0092A111  45 33 C0                        xor r8d, r8d
0092A114  44 89 44 24 74                  mov dword ptr [rsp + 0x74], r8d
0092A119  F6 44 24 4A 10                  test byte ptr [rsp + 0x4a], 0x10
0092A11E  0F 85 72 04 00 00               jne 0x14092a596
0092A124  33 C9                           xor ecx, ecx
0092A126  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0092A12B  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0092A130  F6 44 24 4A 04                  test byte ptr [rsp + 0x4a], 4
0092A135  0F 84 4F 04 00 00               je 0x14092a58a
0092A13B  48 85 FF                        test rdi, rdi
0092A13E  0F 84 46 04 00 00               je 0x14092a58a
0092A144  45 84 E4                        test r12b, r12b
0092A147  0F 84 6C 05 00 00               je 0x14092a6b9
0092A14D  48 8D 47 02                     lea rax, [rdi + 2]
0092A151  49 3B C1                        cmp rax, r9
0092A154  49 0F 43 C1                     cmovae rax, r9
0092A158  90                              nop
0092A159  0F B7 00                        movzx eax, word ptr [rax]
0092A15C  8B F0                           mov esi, eax
0092A15E  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
0092A162  85 C0                           test eax, eax
0092A164  74 27                           je 0x14092a18d
0092A166  F6 44 24 68 03                  test byte ptr [rsp + 0x68], 3
0092A16B  74 05                           je 0x14092a172
0092A16D  E8 5E FE F6 FF                  call 0x140899fd0
0092A172  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0092A177  48 8D 0C 07                     lea rcx, [rdi + rax]
0092A17B  49 3B C9                        cmp rcx, r9
0092A17E  77 05                           ja 0x14092a185
0092A180  48 3B CF                        cmp rcx, rdi
0092A183  73 0D                           jae 0x14092a192
0092A185  41 0F B6 01                     movzx eax, byte ptr [r9]
0092A189  8B 74 24 24                     mov esi, dword ptr [rsp + 0x24]
0092A18D  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0092A192  EB 05                           jmp 0x14092a199
0092A194  E9 B9 02 00 00                  jmp 0x14092a452
0092A199  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0092A19E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092A1A3  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0092A1A8  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0092A1AD  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0092A1B2  44 8B 6C 24 20                  mov r13d, dword ptr [rsp + 0x20]
0092A1B7  8D 56 03                        lea edx, [rsi + 3]
0092A1BA  83 E2 FC                        and edx, 0xfffffffc
0092A1BD  89 94 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], edx
0092A1C4  8D 42 F8                        lea eax, [rdx - 8]
0092A1C7  3D F7 FF 00 00                  cmp eax, 0xfff7
0092A1CC  0F 87 80 04 00 00               ja 0x14092a652
0092A1D2  48 85 DB                        test rbx, rbx
0092A1D5  0F 84 96 00 00 00               je 0x14092a271
0092A1DB  45 84 E4                        test r12b, r12b
0092A1DE  0F 84 39 05 00 00               je 0x14092a71d
0092A1E4  48 8D 43 01                     lea rax, [rbx + 1]
0092A1E8  49 3B C1                        cmp rax, r9
0092A1EB  49 0F 43 C1                     cmovae rax, r9
0092A1EF  90                              nop
0092A1F0  0F B6 00                        movzx eax, byte ptr [rax]
0092A1F3  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0092A1F7  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0092A1FE  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0092A202  85 C0                           test eax, eax
0092A204  74 2B                           je 0x14092a231
0092A206  F6 44 24 50 03                  test byte ptr [rsp + 0x50], 3
0092A20B  74 05                           je 0x14092a212
0092A20D  E8 BE FD F6 FF                  call 0x140899fd0
0092A212  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
0092A216  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0092A21B  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0092A220  48 03 CB                        add rcx, rbx
0092A223  49 3B C9                        cmp rcx, r9
0092A226  77 05                           ja 0x14092a22d
0092A228  48 3B CB                        cmp rcx, rbx
0092A22B  73 0E                           jae 0x14092a23b
0092A22D  41 0F B6 01                     movzx eax, byte ptr [r9]
0092A231  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0092A236  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092A23B  EB 05                           jmp 0x14092a242
0092A23D  E9 10 02 00 00                  jmp 0x14092a452
0092A242  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0092A247  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0092A24C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092A251  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0092A256  44 8B 6C 24 20                  mov r13d, dword ptr [rsp + 0x20]
0092A25B  8B 74 24 24                     mov esi, dword ptr [rsp + 0x24]
0092A25F  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
0092A264  41 83 C0 03                     add r8d, 3
0092A268  41 83 E0 FC                     and r8d, 0xfffffffc
0092A26C  44 89 44 24 74                  mov dword ptr [rsp + 0x74], r8d
0092A271  4D 85 FF                        test r15, r15
0092A274  0F 85 F6 01 00 00               jne 0x14092a470
0092A27A  43 8D 04 06                     lea eax, [r14 + r8]
0092A27E  03 C2                           add eax, edx
0092A280  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
0092A284  83 C1 14                        add ecx, 0x14
0092A287  03 C1                           add eax, ecx
0092A289  8B D8                           mov ebx, eax
0092A28B  41 0F BA EB 0A                  bts r11d, 0xa
0092A290  41 B8 53 65 53 63               mov r8d, 0x63536553
0092A296  8B D0                           mov edx, eax
0092A298  41 8B CB                        mov ecx, r11d
0092A29B  E8 70 7D 25 00                  call 0x140b82010
0092A2A0  4C 8B F0                        mov r14, rax
0092A2A3  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0092A2A8  48 85 C0                        test rax, rax
0092A2AB  0F 84 9B 04 00 00               je 0x14092a74c
0092A2B1  44 8B C3                        mov r8d, ebx
0092A2B4  33 D2                           xor edx, edx
0092A2B6  48 8B C8                        mov rcx, rax
0092A2B9  E8 82 C9 D9 FF                  call 0x1406c6c40
0092A2BE  0F 10 44 24 48                  movups xmm0, xmmword ptr [rsp + 0x48]
0092A2C3  41 0F 11 06                     movups xmmword ptr [r14], xmm0
0092A2C7  45 89 7E 10                     mov dword ptr [r14 + 0x10], r15d
0092A2CB  49 8D 5E 14                     lea rbx, [r14 + 0x14]
0092A2CF  B8 00 80 00 00                  mov eax, 0x8000
0092A2D4  66 41 09 46 02                  or word ptr [r14 + 2], ax
0092A2D9  F6 44 24 4A 10                  test byte ptr [rsp + 0x4a], 0x10
0092A2DE  0F 85 2E 02 00 00               jne 0x14092a512
0092A2E4  41 C7 46 0C 00 00 00 00         mov dword ptr [r14 + 0xc], 0
0092A2EC  F6 44 24 4A 04                  test byte ptr [rsp + 0x4a], 4
0092A2F1  0F 84 F3 03 00 00               je 0x14092a6ea
0092A2F7  48 85 FF                        test rdi, rdi
0092A2FA  0F 84 EA 03 00 00               je 0x14092a6ea
0092A300  44 8B C6                        mov r8d, esi
0092A303  48 8B D7                        mov rdx, rdi
0092A306  48 8B CB                        mov rcx, rbx
0092A309  E8 32 C5 D9 FF                  call 0x1406c6840
0092A30E  EB 15                           jmp 0x14092a325
0092A310  8B D8                           mov ebx, eax
0092A312  33 D2                           xor edx, edx
0092A314  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0092A319  E8 52 85 25 00                  call 0x140b82870
0092A31E  8B C3                           mov eax, ebx
0092A320  E9 2D 01 00 00                  jmp 0x14092a452
0092A325  45 84 E4                        test r12b, r12b
0092A328  74 25                           je 0x14092a34f
0092A32A  83 FE 08                        cmp esi, 8
0092A32D  0F 82 29 03 00 00               jb 0x14092a65c
0092A333  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
0092A337  3B F0                           cmp esi, eax
0092A339  0F 85 1D 03 00 00               jne 0x14092a65c
0092A33F  48 8B CB                        mov rcx, rbx
0092A342  E8 59 04 00 00                  call 0x14092a7a0
0092A347  84 C0                           test al, al
0092A349  0F 84 0D 03 00 00               je 0x14092a65c
0092A34F  8B C3                           mov eax, ebx
0092A351  41 2B C6                        sub eax, r14d
0092A354  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
0092A358  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
0092A35F  66 89 43 02                     mov word ptr [rbx + 2], ax
0092A363  48 03 D8                        add rbx, rax
0092A366  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0092A36B  48 85 C0                        test rax, rax
0092A36E  0F 84 FC 02 00 00               je 0x14092a670
0092A374  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
0092A379  48 8B D0                        mov rdx, rax
0092A37C  48 8B CB                        mov rcx, rbx
0092A37F  E8 BC C4 D9 FF                  call 0x1406c6840
0092A384  0F B6 44 24 38                  movzx eax, byte ptr [rsp + 0x38]
0092A389  88 43 01                        mov byte ptr [rbx + 1], al
0092A38C  EB 15                           jmp 0x14092a3a3
0092A38E  8B D8                           mov ebx, eax
0092A390  33 D2                           xor edx, edx
0092A392  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0092A397  E8 D4 84 25 00                  call 0x140b82870
0092A39C  8B C3                           mov eax, ebx
0092A39E  E9 AF 00 00 00                  jmp 0x14092a452
0092A3A3  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
0092A3AD  45 84 E4                        test r12b, r12b
0092A3B0  74 21                           je 0x14092a3d3
0092A3B2  48 3B DF                        cmp rbx, rdi
0092A3B5  0F 86 0B 03 00 00               jbe 0x14092a6c6
0092A3BB  0F B6 03                        movzx eax, byte ptr [rbx]
0092A3BE  24 0F                           and al, 0xf
0092A3C0  3C 01                           cmp al, 1
0092A3C2  0F 85 FE 02 00 00               jne 0x14092a6c6
0092A3C8  80 7C 24 38 0F                  cmp byte ptr [rsp + 0x38], 0xf
0092A3CD  0F 87 F3 02 00 00               ja 0x14092a6c6
0092A3D3  8B CB                           mov ecx, ebx
0092A3D5  41 2B CE                        sub ecx, r14d
0092A3D8  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
0092A3DC  48 03 D8                        add rbx, rax
0092A3DF  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
0092A3E3  4D 85 FF                        test r15, r15
0092A3E6  0F 84 95 02 00 00               je 0x14092a681
0092A3EC  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
0092A3F1  49 8B D7                        mov rdx, r15
0092A3F4  48 8B CB                        mov rcx, rbx
0092A3F7  E8 44 C4 D9 FF                  call 0x1406c6840
0092A3FC  0F B6 44 24 3C                  movzx eax, byte ptr [rsp + 0x3c]
0092A401  88 43 01                        mov byte ptr [rbx + 1], al
0092A404  EB 12                           jmp 0x14092a418
0092A406  8B D8                           mov ebx, eax
0092A408  33 D2                           xor edx, edx
0092A40A  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0092A40F  E8 5C 84 25 00                  call 0x140b82870
0092A414  8B C3                           mov eax, ebx
0092A416  EB 3A                           jmp 0x14092a452
0092A418  45 84 E4                        test r12b, r12b
0092A41B  74 21                           je 0x14092a43e
0092A41D  48 3B DF                        cmp rbx, rdi
0092A420  0F 86 A0 02 00 00               jbe 0x14092a6c6
0092A426  0F B6 03                        movzx eax, byte ptr [rbx]
0092A429  24 0F                           and al, 0xf
0092A42B  80 7C 24 3C 0F                  cmp byte ptr [rsp + 0x3c], 0xf
0092A430  0F 87 90 02 00 00               ja 0x14092a6c6
0092A436  3C 01                           cmp al, 1
0092A438  0F 85 88 02 00 00               jne 0x14092a6c6
0092A43E  41 2B DE                        sub ebx, r14d
0092A441  41 89 5E 08                     mov dword ptr [r14 + 8], ebx
0092A445  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
0092A44D  4C 89 30                        mov qword ptr [rax], r14
0092A450  33 C0                           xor eax, eax
0092A452  4C 8D 9C 24 B0 00 00 00         lea r11, [rsp + 0xb0]
0092A45A  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0092A45E  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
0092A462  49 8B E3                        mov rsp, r11
0092A465  41 5F                           pop r15
0092A467  41 5E                           pop r14
0092A469  41 5D                           pop r13
0092A46B  41 5C                           pop r12
0092A46D  5F                              pop rdi
0092A46E  C3                              ret
0092A46F  CC                              int3
0092A470  45 84 E4                        test r12b, r12b
0092A473  0F 84 7E 02 00 00               je 0x14092a6f7
0092A479  49 8D 47 01                     lea rax, [r15 + 1]
0092A47D  49 3B C1                        cmp rax, r9
0092A480  49 0F 43 C1                     cmovae rax, r9
0092A484  90                              nop
0092A485  0F B6 00                        movzx eax, byte ptr [rax]
0092A488  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
0092A48C  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0092A493  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0092A497  85 C0                           test eax, eax
0092A499  74 26                           je 0x14092a4c1
0092A49B  F6 44 24 58 03                  test byte ptr [rsp + 0x58], 3
0092A4A0  74 05                           je 0x14092a4a7
0092A4A2  E8 29 FB F6 FF                  call 0x140899fd0
0092A4A7  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
0092A4AB  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0092A4B0  49 03 CF                        add rcx, r15
0092A4B3  49 3B C9                        cmp rcx, r9
0092A4B6  77 05                           ja 0x14092a4bd
0092A4B8  49 3B CF                        cmp rcx, r15
0092A4BB  73 09                           jae 0x14092a4c6
0092A4BD  41 0F B6 01                     movzx eax, byte ptr [r9]
0092A4C1  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0092A4C6  EB 02                           jmp 0x14092a4ca
0092A4C8  EB 88                           jmp 0x14092a452
0092A4CA  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0092A4CF  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0092A4D4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092A4D9  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0092A4DE  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092A4E3  44 8B 6C 24 20                  mov r13d, dword ptr [rsp + 0x20]
0092A4E8  8B 74 24 24                     mov esi, dword ptr [rsp + 0x24]
0092A4EC  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0092A4F1  41 83 C6 03                     add r14d, 3
0092A4F5  41 83 E6 FC                     and r14d, 0xfffffffc
0092A4F9  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
0092A500  44 8B 9C 24 F0 00 00 00         mov r11d, dword ptr [rsp + 0xf0]
0092A508  44 8B 44 24 74                  mov r8d, dword ptr [rsp + 0x74]
0092A50D  E9 68 FD FF FF                  jmp 0x14092a27a
0092A512  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
0092A517  48 85 C0                        test rax, rax
0092A51A  0F 84 C4 FD FF FF               je 0x14092a2e4
0092A520  45 8B C5                        mov r8d, r13d
0092A523  48 8B D0                        mov rdx, rax
0092A526  48 8B CB                        mov rcx, rbx
0092A529  E8 12 C3 D9 FF                  call 0x1406c6840
0092A52E  EB 15                           jmp 0x14092a545
0092A530  8B D8                           mov ebx, eax
0092A532  33 D2                           xor edx, edx
0092A534  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0092A539  E8 32 83 25 00                  call 0x140b82870
0092A53E  8B C3                           mov eax, ebx
0092A540  E9 0D FF FF FF                  jmp 0x14092a452
0092A545  45 84 E4                        test r12b, r12b
0092A548  74 27                           je 0x14092a571
0092A54A  41 83 FD 08                     cmp r13d, 8
0092A54E  0F 82 08 01 00 00               jb 0x14092a65c
0092A554  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
0092A558  44 3B E8                        cmp r13d, eax
0092A55B  0F 85 FB 00 00 00               jne 0x14092a65c
0092A561  48 8B CB                        mov rcx, rbx
0092A564  E8 37 02 00 00                  call 0x14092a7a0
0092A569  84 C0                           test al, al
0092A56B  0F 84 EB 00 00 00               je 0x14092a65c
0092A571  8B C3                           mov eax, ebx
0092A573  41 2B C6                        sub eax, r14d
0092A576  41 89 46 0C                     mov dword ptr [r14 + 0xc], eax
0092A57A  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
0092A57E  66 89 43 02                     mov word ptr [rbx + 2], ax
0092A582  48 03 D8                        add rbx, rax
0092A585  E9 62 FD FF FF                  jmp 0x14092a2ec
0092A58A  33 FF                           xor edi, edi
0092A58C  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
0092A591  E9 3C FC FF FF                  jmp 0x14092a1d2
0092A596  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
0092A59B  48 85 C9                        test rcx, rcx
0092A59E  0F 84 80 FB FF FF               je 0x14092a124
0092A5A4  45 84 E4                        test r12b, r12b
0092A5A7  0F 84 61 01 00 00               je 0x14092a70e
0092A5AD  48 8D 41 02                     lea rax, [rcx + 2]
0092A5B1  49 3B C1                        cmp rax, r9
0092A5B4  49 0F 43 C1                     cmovae rax, r9
0092A5B8  90                              nop
0092A5B9  0F B7 00                        movzx eax, word ptr [rax]
0092A5BC  44 8B E8                        mov r13d, eax
0092A5BF  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0092A5C3  85 C0                           test eax, eax
0092A5C5  74 49                           je 0x14092a610
0092A5C7  F6 44 24 60 03                  test byte ptr [rsp + 0x60], 3
0092A5CC  74 05                           je 0x14092a5d3
0092A5CE  E8 FD F9 F6 FF                  call 0x140899fd0
0092A5D3  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0092A5D8  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0092A5DD  48 8D 14 01                     lea rdx, [rcx + rax]
0092A5E1  48 3B D1                        cmp rdx, rcx
0092A5E4  72 0E                           jb 0x14092a5f4
0092A5E6  49 3B D1                        cmp rdx, r9
0092A5E9  77 09                           ja 0x14092a5f4
0092A5EB  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
0092A5F2  EB 26                           jmp 0x14092a61a
0092A5F4  41 0F B6 01                     movzx eax, byte ptr [r9]
0092A5F8  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0092A5FD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092A602  44 8B 6C 24 20                  mov r13d, dword ptr [rsp + 0x20]
0092A607  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
0092A60E  EB 0A                           jmp 0x14092a61a
0092A610  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0092A615  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092A61A  EB 05                           jmp 0x14092a621
0092A61C  E9 31 FE FF FF                  jmp 0x14092a452
0092A621  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0092A626  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0092A62B  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0092A630  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0092A635  8B 74 24 24                     mov esi, dword ptr [rsp + 0x24]
0092A639  41 8D 45 03                     lea eax, [r13 + 3]
0092A63D  83 E0 FC                        and eax, 0xfffffffc
0092A640  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
0092A644  83 C0 F8                        add eax, -8
0092A647  3D F7 FF 00 00                  cmp eax, 0xfff7
0092A64C  0F 86 DE FA FF FF               jbe 0x14092a130
0092A652  B8 77 00 00 C0                  mov eax, 0xc0000077
0092A657  E9 F6 FD FF FF                  jmp 0x14092a452
0092A65C  33 D2                           xor edx, edx
0092A65E  49 8B CE                        mov rcx, r14
0092A661  E8 0A 82 25 00                  call 0x140b82870
0092A666  B8 77 00 00 C0                  mov eax, 0xc0000077
0092A66B  E9 E2 FD FF FF                  jmp 0x14092a452
0092A670  33 C9                           xor ecx, ecx
0092A672  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
0092A67C  E9 5E FD FF FF                  jmp 0x14092a3df
0092A681  33 DB                           xor ebx, ebx
0092A683  E9 B9 FD FF FF                  jmp 0x14092a441
0092A688  45 84 C9                        test r9b, r9b
0092A68B  74 4D                           je 0x14092a6da
0092A68D  45 84 E4                        test r12b, r12b
0092A690  0F 85 19 F9 FF FF               jne 0x140929faf
0092A696  0F 10 01                        movups xmm0, xmmword ptr [rcx]
0092A699  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
0092A6A1  44 8B 41 10                     mov r8d, dword ptr [rcx + 0x10]
0092A6A5  49 B9 00 00 FF FF FF 7F 00 00   movabs r9, 0x7fffffff0000
0092A6AF  66 48 0F 7E C2                  movq rdx, xmm0
0092A6B4  E9 4C F9 FF FF                  jmp 0x14092a005
0092A6B9  0F B7 77 02                     movzx esi, word ptr [rdi + 2]
0092A6BD  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
0092A6C1  E9 F1 FA FF FF                  jmp 0x14092a1b7
0092A6C6  33 D2                           xor edx, edx
0092A6C8  49 8B CE                        mov rcx, r14
0092A6CB  E8 A0 81 25 00                  call 0x140b82870
0092A6D0  B8 78 00 00 C0                  mov eax, 0xc0000078
0092A6D5  E9 78 FD FF FF                  jmp 0x14092a452
0092A6DA  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
0092A6E2  4C 89 10                        mov qword ptr [rax], r10
0092A6E5  E9 66 FD FF FF                  jmp 0x14092a450
0092A6EA  41 C7 46 10 00 00 00 00         mov dword ptr [r14 + 0x10], 0
0092A6F2  E9 6F FC FF FF                  jmp 0x14092a366
0092A6F7  41 0F B6 4F 01                  movzx ecx, byte ptr [r15 + 1]
0092A6FC  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
0092A700  E8 CB FD 09 00                  call 0x1409ca4d0
0092A705  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0092A709  E9 DE FD FF FF                  jmp 0x14092a4ec
0092A70E  44 0F B7 69 02                  movzx r13d, word ptr [rcx + 2]
0092A713  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
0092A718  E9 1C FF FF FF                  jmp 0x14092a639
0092A71D  0F B6 4B 01                     movzx ecx, byte ptr [rbx + 1]
0092A721  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0092A725  E8 A6 FD 09 00                  call 0x1409ca4d0
0092A72A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0092A72E  8B 94 24 E0 00 00 00            mov edx, dword ptr [rsp + 0xe0]
0092A735  44 8B 9C 24 F0 00 00 00         mov r11d, dword ptr [rsp + 0xf0]
0092A73D  49 B9 00 00 FF FF FF 7F 00 00   movabs r9, 0x7fffffff0000
0092A747  E9 13 FB FF FF                  jmp 0x14092a25f
0092A74C  B8 9A 00 00 C0                  mov eax, 0xc000009a
0092A751  E9 FC FC FF FF                  jmp 0x14092a452
0092A756  B8 58 00 00 C0                  mov eax, 0xc0000058
0092A75B  E9 F2 FC FF FF                  jmp 0x14092a452
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeCaptureSecurityDescriptor(__int64 a1, unsigned __int8 a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned __int16 v_stack_m8E;
    unsigned __int8 v_stack_m8F;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p40;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = v_rsi;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (176);
    result = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = 0;
    v_r14 = 0;
    v_stack_mB8 = 0;
    v_stack_mB4 = 0;
    v_stack_mA0 = 0;
    v_stack_mA8 = 0;
    v_stack_m9C = 0;
    v_stack_mA4 = 0;
    if (a1 == 0) goto loc_0092A445;
    if (a2 == 0) goto loc_0092A688;
loc_00929FAF:
    if ((((unsigned __int8)(a1)) & (3)) != 0) goto loc_00929FF8;
    if (a1 < a4) { a4 = a1; }
    v_stack_m58 = v_xmm0;
    result = (a2) >> (16);
    if (sign_flag) goto loc_00929FFE;
    if ((((unsigned __int8)(a1)) & (7)) == 0) goto loc_00929FFE;
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
loc_00929FF8:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
loc_00929FFE:
    goto loc_0092A005;
loc_0092A005:
    if (a2 != 1) goto loc_0092A756;
    v_stack_m90 = a2;
    result = (a2) >> (8);
    v_stack_m8F = (unsigned __int8)(result);
    a1 = (a2) >> (16);
    result = (unsigned __int16)(((unsigned __int16)(a1)) & ((unsigned __int16)((unsigned int)(0x7FFFULL))));
    v_stack_m8E = (unsigned __int16)(result);
    if (sign_flag) goto loc_0092A0CD;
loc_0092A041:
    v_stack_m98 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m88 = *(unsigned __int64 *)(a1 + 8);
    if (sign_flag) goto loc_0092A082;
loc_0092A054:
    v_stack_m80 = *(unsigned __int64 *)(a1 + 16);
    if ((((unsigned __int8)(a1)) & (16)) != 0) goto loc_0092A09E;
loc_0092A061:
    v_stack_mB0 = 0;
    v_stack_m78 = 0;
    if ((((unsigned __int8)(a1)) & (4)) == 0) goto loc_0092A099;
    if (!sign_flag) goto loc_0092A093;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))) == 0) goto loc_0092A0C8;
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) + (a1);
    goto loc_0092A0E6;
loc_0092A082:
    if ((unsigned int)((unsigned int)(v_stack_m50)) == 0) goto loc_0092A0B8;
    goto loc_0092A054;
loc_0092A093:
    goto loc_0092A0E6;
loc_0092A099:
    goto loc_0092A0E6;
loc_0092A09E:
    if (!sign_flag) goto loc_0092A0C2;
    result = (v_stack_m50) >> (32);
    if ((unsigned int)(result) == 0) goto loc_0092A0BD;
    result = (result) + (a1);
    goto loc_0092A061;
loc_0092A0B8:
    goto loc_0092A054;
loc_0092A0BD:
    goto loc_0092A061;
loc_0092A0C2:
    goto loc_0092A061;
loc_0092A0C8:
    goto loc_0092A0E6;
loc_0092A0CD:
    a2 = (a2) >> (32);
    if (a2 == 0) goto loc_0092A0DE;
    goto loc_0092A041;
loc_0092A0DE:
    goto loc_0092A041;
loc_0092A0E6:
    v_stack_m70 = 0;
    goto loc_0092A0F2;
loc_0092A0F2:
    v_stack_mB8 = 0;
    v_stack_mB4 = 0;
    v_stack_m68 = 0;
    v_stack_p8 = 0;
    a3 = 0;
    v_stack_m64 = 0;
    if (((v_stack_m8E) & (16)) != 0) goto loc_0092A596;
loc_0092A124:
    a1 = 0;
    v_stack_mB0 = 0;
    v_stack_m78 = 0;
loc_0092A130:
    if (((v_stack_m8E) & (4)) == 0) goto loc_0092A58A;
    if (0 == 0) goto loc_0092A58A;
    if (a2 == 0) goto loc_0092A6B9;
    result = 0 + 2;
    if ((0 + 2) >= a4) { result = a4; }
    v_stack_mB4 = (unsigned int)(*(unsigned __int16 *)(result));
    if ((unsigned int)(*(unsigned __int16 *)(result)) == 0) goto loc_0092A18D;
    result = *(unsigned __int16 *)(result);
    if (((v_stack_m70) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, 0, a3, a4);
    }
    if ((v_stack_m70 + result * 1) > a4) goto loc_0092A185;
    if ((v_stack_m70 + result * 1) >= v_stack_m70) goto loc_0092A192;
loc_0092A185:
loc_0092A18D:
loc_0092A192:
    goto loc_0092A199;
loc_0092A199:
    v_stack_mB0 = v_stack_m78;
    v_stack_m98 = v_stack_m88;
loc_0092A1B7:
    a2 = (unsigned int)(((unsigned int)(v_stack_mB4) + 3) & (0xFFFFFFFCULL));
    v_stack_p8 = a2;
    if (((unsigned int)(a2 - 8)) > 0xFFF7ULL) goto loc_0092A652;
loc_0092A1D2:
    if (v_stack_m88 == 0) goto loc_0092A271;
    if (a2 == 0) goto loc_0092A71D;
    result = v_stack_m88 + 1;
    if ((v_stack_m88 + 1) >= a4) { result = a4; }
    v_stack_mA0 = (unsigned int)(*(unsigned __int8 *)(result));
    v_stack_mA8 = (unsigned int)(*(unsigned __int8 *)(result) * 4 + 8);
    if ((unsigned int)(*(unsigned __int8 *)(result) * 4 + 8) == 0) goto loc_0092A231;
    result = *(unsigned __int8 *)(result) * 4 + 8;
    if (((v_stack_m88) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_m70 + result * 1, a2, a3, a4);
    }
    v_stack_m98 = v_stack_m88;
    a1 = ((unsigned int)(v_stack_mA8)) + (v_stack_m88);
    if (a1 > a4) goto loc_0092A22D;
    if (a1 >= v_stack_m88) goto loc_0092A23B;
loc_0092A22D:
loc_0092A231:
    v_stack_m98 = v_stack_m88;
loc_0092A23B:
    goto loc_0092A242;
loc_0092A242:
    v_stack_mB0 = v_stack_m78;
loc_0092A25F:
    a3 = (unsigned int)(((unsigned int)(v_stack_mA8)) + (3));
    a3 = (unsigned int)((a3) & (0xFFFFFFFCULL));
    v_stack_m64 = a3;
loc_0092A271:
    if (v_stack_m80 != 0) goto loc_0092A470;
loc_0092A27A:
    result = (unsigned int)((v_r14 + a3 * 1) + (a2));
    a1 = (unsigned int)(((unsigned int)(v_stack_m68)) + (20));
    result = (unsigned int)((result) + ((unsigned int)(a1)));
    result = ExAllocatePoolWithTag((unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)(result)), (unsigned int)(0x63536553ULL), a4);
    v_stack_m60 = result;
    if (result == 0) goto loc_0092A74C;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned int *)(result + 16) = (unsigned int)(v_stack_m80);
    if (((v_stack_m8E) & (16)) != 0) goto loc_0092A512;
loc_0092A2E4:
    *(unsigned int *)(result + 12) = 0;
loc_0092A2EC:
    if (((v_stack_m8E) & (4)) == 0) goto loc_0092A6EA;
    if (v_stack_m70 == 0) goto loc_0092A6EA;
    result = memcpy(result + 20, v_stack_m70, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))), a4);
    goto loc_0092A325;
loc_0092A325:
    if (0 == 0) goto loc_0092A34F;
    if (((unsigned int)((unsigned int)(v_stack_mB4))) < 8) goto loc_0092A65C;
    if (((unsigned int)((unsigned int)(v_stack_mB4))) != ((unsigned int)(*(unsigned __int16 *)(result + 20 + 2)))) goto loc_0092A65C;
    result = RtlValidAcl(result + 20, v_stack_m70, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0092A65C;
loc_0092A34F:
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 20))) - ((unsigned int)(result)));
    *(unsigned int *)(result + 16) = (unsigned int)(result);
    *(unsigned __int16 *)(result + 20 + 2) = (unsigned __int16)((unsigned int)(v_stack_p8));
    v_rbx = (result + 20) + ((unsigned int)(v_stack_p8));
loc_0092A366:
    if (v_stack_m98 == 0) goto loc_0092A670;
    result = memcpy(v_rbx, v_stack_m98, (unsigned int)(v_stack_mA8), a4);
    *(unsigned __int8 *)(v_rbx + 1) = (unsigned __int8)(v_stack_mA0);
    goto loc_0092A3A3;
loc_0092A3A3:
    if (0 == 0) goto loc_0092A3D3;
    if (v_rbx <= v_stack_m70) goto loc_0092A6C6;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbx)) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_0092A6C6;
    if (v_stack_mA0 > 15) goto loc_0092A6C6;
loc_0092A3D3:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(result)));
    v_rbx = (v_rbx) + ((unsigned int)(v_stack_m64));
loc_0092A3DF:
    *(unsigned int *)(result + 4) = (unsigned int)(a1);
    if (v_stack_m80 == 0) goto loc_0092A681;
    result = memcpy(v_rbx, v_stack_m80, (unsigned int)(v_stack_mA4), a4);
    *(unsigned __int8 *)(v_rbx + 1) = (unsigned __int8)(v_stack_m9C);
    goto loc_0092A418;
loc_0092A418:
    if (0 == 0) goto loc_0092A43E;
    if (v_rbx <= v_stack_m70) goto loc_0092A6C6;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbx)) & (15));
    if (v_stack_m9C > 15) goto loc_0092A6C6;
    if (((unsigned __int8)(result)) != 1) goto loc_0092A6C6;
loc_0092A43E:
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(result)));
loc_0092A441:
    *(unsigned int *)(result + 8) = (unsigned int)(v_rbx);
loc_0092A445:
    *(unsigned __int64 *)(a5) = result;
loc_0092A450:
    result = 0;
loc_0092A452:
    return result;
loc_0092A470:
    if (0 == 0) goto loc_0092A6F7;
    result = v_stack_m80 + 1;
    if ((v_stack_m80 + 1) >= a4) { result = a4; }
    v_stack_m74 = (unsigned int)(*(unsigned __int8 *)(result));
    v_stack_m7C = (unsigned int)(*(unsigned __int8 *)(result) * 4 + 8);
    if ((unsigned int)(*(unsigned __int8 *)(result) * 4 + 8) == 0) goto loc_0092A4C1;
    result = *(unsigned __int8 *)(result) * 4 + 8;
    if (((v_stack_m58) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_rbx, v_stack_m80, (unsigned int)(v_stack_mA4), a4);
    }
    a1 = ((unsigned int)(v_stack_m7C)) + (v_stack_m58);
    if (a1 > a4) goto loc_0092A4BD;
    if (a1 >= v_stack_m58) goto loc_0092A4C6;
loc_0092A4BD:
loc_0092A4C1:
loc_0092A4C6:
    goto loc_0092A4CA;
loc_0092A4CA:
    v_stack_m88 = v_stack_m50;
    v_stack_m70 = v_stack_m60;
loc_0092A4EC:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m7C)) + (3));
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFFCULL));
    goto loc_0092A27A;
loc_0092A512:
    if (v_stack_m88 == 0) goto loc_0092A2E4;
    result = memcpy(*(unsigned __int64 *)(v_stack_m28 + 56), v_stack_m88, (unsigned int)((unsigned int)((unsigned int)(v_stack_m90))), a4);
    goto loc_0092A545;
loc_0092A545:
    if (0 == 0) goto loc_0092A571;
    if (((unsigned int)((unsigned int)(v_stack_m90))) < 8) goto loc_0092A65C;
    if (((unsigned int)((unsigned int)(v_stack_m90))) != ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 2)))) goto loc_0092A65C;
    result = RtlValidAcl(*(unsigned __int64 *)(v_stack_m28 + 56), v_stack_m88, (unsigned int)((unsigned int)((unsigned int)(v_stack_m90))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0092A65C;
loc_0092A571:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) - ((unsigned int)(v_r14)));
    *(unsigned int *)(v_r14 + 12) = (unsigned int)(result);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 2) = (unsigned __int16)((unsigned int)(v_stack_m40));
    v_rbx = (*(unsigned __int64 *)(v_stack_m28 + 56)) + ((unsigned int)(v_stack_m40));
    goto loc_0092A2EC;
loc_0092A58A:
    v_rdi = 0;
    v_stack_m48 = 0;
    goto loc_0092A1D2;
loc_0092A596:
    if (v_stack_m88 == 0) goto loc_0092A124;
    if (0 == 0) goto loc_0092A70E;
    result = v_stack_m88 + 2;
    if ((v_stack_m88 + 2) >= a4) { result = a4; }
    v_stack_m90 = (unsigned int)(*(unsigned __int16 *)(result));
    if ((unsigned int)(*(unsigned __int16 *)(result)) == 0) goto loc_0092A610;
    result = *(unsigned __int16 *)(result);
    if (((v_stack_m50) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_m88, v_stack_m88, (unsigned int)((unsigned int)((unsigned int)(v_stack_m90))), a4);
    }
    v_stack_m88 = v_stack_m50;
    if ((v_stack_m50 + result * 1) < v_stack_m50) goto loc_0092A5F4;
    if ((v_stack_m50 + result * 1) > a4) goto loc_0092A5F4;
    goto loc_0092A61A;
loc_0092A5F4:
    v_stack_m88 = v_stack_m50;
    goto loc_0092A61A;
loc_0092A610:
    v_stack_m88 = v_stack_m50;
loc_0092A61A:
    goto loc_0092A621;
loc_0092A621:
    v_stack_m70 = v_stack_m60;
loc_0092A639:
    result = (unsigned int)(((unsigned int)(v_stack_m90) + 3) & (0xFFFFFFFCULL));
    v_stack_m40 = (unsigned int)(result);
    result = (unsigned int)((result) + (-8));
    if (((unsigned int)(result)) <= 0xFFF7ULL) goto loc_0092A130;
loc_0092A652:
    goto loc_0092A452;
loc_0092A65C:
    a2 = 0;
    result = ExFreePoolWithTag(v_r14, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m90))), a4);
    goto loc_0092A452;
loc_0092A670:
    a1 = 0;
    goto loc_0092A3DF;
loc_0092A681:
    v_rbx = 0;
    goto loc_0092A441;
loc_0092A688:
    if ((unsigned __int8)(a4) == 0) goto loc_0092A6DA;
    if (0 != 0) goto loc_00929FAF;
    v_stack_m30 = v_xmm0;
    goto loc_0092A005;
loc_0092A6B9:
    v_stack_m8C = (unsigned int)(*(unsigned __int16 *)(v_stack_m48 + 2));
    goto loc_0092A1B7;
loc_0092A6C6:
    a2 = 0;
    result = ExFreePoolWithTag(v_r14, a2, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
    goto loc_0092A452;
loc_0092A6DA:
    *(unsigned __int64 *)(a5) = 0;
    goto loc_0092A450;
loc_0092A6EA:
    *(unsigned int *)(v_r14 + 16) = 0;
    goto loc_0092A366;
loc_0092A6F7:
    v_stack_m74 = (unsigned int)(*(unsigned __int8 *)(v_stack_m58 + 1));
    result = RtlLengthRequiredSid(*(unsigned __int8 *)(v_stack_m58 + 1), a2, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
    v_stack_m7C = (unsigned int)(result);
    goto loc_0092A4EC;
loc_0092A70E:
    v_stack_m90 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int8 *)(v_stack_m58 + 1) + 2));
    goto loc_0092A639;
loc_0092A71D:
    v_stack_m78 = (unsigned int)(*(unsigned __int8 *)(v_rbx + 1));
    result = RtlLengthRequiredSid(*(unsigned __int8 *)(v_rbx + 1), a2, (unsigned int)(*(unsigned int *)(a1 + 16)), a4);
    v_stack_m80 = (unsigned int)(result);
    goto loc_0092A25F;
loc_0092A74C:
    goto loc_0092A452;
loc_0092A756:
    goto loc_0092A452;
}
```

## 5. (Beta) C Style

```c
int64_t SeCaptureSecurityDescriptor(int64_t Arg1, uint8_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint16_t v_stack_m8E;
    uint8_t v_stack_m8F;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p40;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = local_rsi;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (176);
    result = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = 0;
    local_r14 = 0;
    v_stack_mB8 = 0;
    v_stack_mB4 = 0;
    v_stack_mA0 = 0;
    v_stack_mA8 = 0;
    v_stack_m9C = 0;
    v_stack_mA4 = 0;
    if (Arg1 == 0) goto loc_0092A445;
    if (Arg2 == 0) goto loc_0092A688;
loc_00929FAF:
    if ((((uint8_t)(Arg1)) & (3)) != 0) goto loc_00929FF8;
    if (Arg1 < Arg4) { Arg4 = Arg1; }
    v_stack_m58 = v_xmm0;
    result = (Arg2) >> (16);
    if (sign_flag) goto loc_00929FFE;
    if ((((uint8_t)(Arg1)) & (7)) == 0) goto loc_00929FFE;
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint32_t)(*(uint32_t *)(Arg1 + 0x10)), Arg4);
loc_00929FF8:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint32_t)(*(uint32_t *)(Arg1 + 0x10)), Arg4);
loc_00929FFE:
    goto loc_0092A005;
loc_0092A005:
    if (Arg2 != 1) goto loc_0092A756;
    v_stack_m90 = Arg2;
    result = (Arg2) >> (8);
    v_stack_m8F = (uint8_t)(result);
    Arg1 = (Arg2) >> (16);
    result = (uint16_t)(((uint16_t)(Arg1)) & ((uint16_t)((uint32_t)(0x7FFFULL))));
    v_stack_m8E = (uint16_t)(result);
    if (sign_flag) goto loc_0092A0CD;
loc_0092A041:
    v_stack_m98 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m88 = *(uint64_t *)(Arg1 + 0x8);
    if (sign_flag) goto loc_0092A082;
loc_0092A054:
    v_stack_m80 = *(uint64_t *)(Arg1 + 0x10);
    if ((((uint8_t)(Arg1)) & (16)) != 0) goto loc_0092A09E;
loc_0092A061:
    v_stack_mB0 = 0;
    v_stack_m78 = 0;
    if ((((uint8_t)(Arg1)) & (4)) == 0) goto loc_0092A099;
    if (!sign_flag) goto loc_0092A093;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10))) == 0) goto loc_0092A0C8;
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10))))) + (Arg1);
    goto loc_0092A0E6;
loc_0092A082:
    if ((uint32_t)((uint32_t)(v_stack_m50)) == 0) goto loc_0092A0B8;
    goto loc_0092A054;
loc_0092A093:
    goto loc_0092A0E6;
loc_0092A099:
    goto loc_0092A0E6;
loc_0092A09E:
    if (!sign_flag) goto loc_0092A0C2;
    result = (v_stack_m50) >> (32);
    if ((uint32_t)(result) == 0) goto loc_0092A0BD;
    result = (result) + (Arg1);
    goto loc_0092A061;
loc_0092A0B8:
    goto loc_0092A054;
loc_0092A0BD:
    goto loc_0092A061;
loc_0092A0C2:
    goto loc_0092A061;
loc_0092A0C8:
    goto loc_0092A0E6;
loc_0092A0CD:
    Arg2 = (Arg2) >> (32);
    if (Arg2 == 0) goto loc_0092A0DE;
    goto loc_0092A041;
loc_0092A0DE:
    goto loc_0092A041;
loc_0092A0E6:
    v_stack_m70 = 0;
    goto loc_0092A0F2;
loc_0092A0F2:
    v_stack_mB8 = 0;
    v_stack_mB4 = 0;
    v_stack_m68 = 0;
    v_stack_p8 = 0;
    Arg3 = 0;
    v_stack_m64 = 0;
    if (((v_stack_m8E) & (16)) != 0) goto loc_0092A596;
loc_0092A124:
    Arg1 = 0;
    v_stack_mB0 = 0;
    v_stack_m78 = 0;
loc_0092A130:
    if (((v_stack_m8E) & (4)) == 0) goto loc_0092A58A;
    if (0 == 0) goto loc_0092A58A;
    if (Arg2 == 0) goto loc_0092A6B9;
    result = 0 + 2;
    if ((0 + 2) >= Arg4) { result = Arg4; }
    v_stack_mB4 = (uint32_t)(*(uint16_t *)(result));
    if ((uint32_t)(*(uint16_t *)(result)) == 0) goto loc_0092A18D;
    result = *(uint16_t *)(result);
    if (((v_stack_m70) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, 0, Arg3, Arg4);
    }
    if ((v_stack_m70 + result * 1) > Arg4) goto loc_0092A185;
    if ((v_stack_m70 + result * 1) >= v_stack_m70) goto loc_0092A192;
loc_0092A185:
loc_0092A18D:
loc_0092A192:
    goto loc_0092A199;
loc_0092A199:
    v_stack_mB0 = v_stack_m78;
    v_stack_m98 = v_stack_m88;
loc_0092A1B7:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mB4) + 3) & (0xFFFFFFFCULL));
    v_stack_p8 = Arg2;
    if (((uint32_t)(Arg2 - 8)) > 0xFFF7ULL) goto loc_0092A652;
loc_0092A1D2:
    if (v_stack_m88 == 0) goto loc_0092A271;
    if (Arg2 == 0) goto loc_0092A71D;
    result = v_stack_m88 + 1;
    if ((v_stack_m88 + 1) >= Arg4) { result = Arg4; }
    v_stack_mA0 = (uint32_t)(*(uint8_t *)(result));
    v_stack_mA8 = (uint32_t)(*(uint8_t *)(result) * 4 + 8);
    if ((uint32_t)(*(uint8_t *)(result) * 4 + 8) == 0) goto loc_0092A231;
    result = *(uint8_t *)(result) * 4 + 8;
    if (((v_stack_m88) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_m70 + result * 1, Arg2, Arg3, Arg4);
    }
    v_stack_m98 = v_stack_m88;
    Arg1 = ((uint32_t)(v_stack_mA8)) + (v_stack_m88);
    if (Arg1 > Arg4) goto loc_0092A22D;
    if (Arg1 >= v_stack_m88) goto loc_0092A23B;
loc_0092A22D:
loc_0092A231:
    v_stack_m98 = v_stack_m88;
loc_0092A23B:
    goto loc_0092A242;
loc_0092A242:
    v_stack_mB0 = v_stack_m78;
loc_0092A25F:
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mA8)) + (3));
    Arg3 = (uint32_t)((Arg3) & (0xFFFFFFFCULL));
    v_stack_m64 = Arg3;
loc_0092A271:
    if (v_stack_m80 != 0) goto loc_0092A470;
loc_0092A27A:
    result = (uint32_t)((local_r14 + Arg3 * 1) + (Arg2));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m68)) + (20));
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
    result = ExAllocatePoolWithTag((uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)(result)), (uint32_t)(0x63536553ULL), Arg4);
    v_stack_m60 = result;
    if (result == 0) goto loc_0092A74C;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
    *(uint64_t *)(result) = v_xmm0;
    *(uint32_t *)(result + 0x10) = (uint32_t)(v_stack_m80);
    if (((v_stack_m8E) & (16)) != 0) goto loc_0092A512;
loc_0092A2E4:
    *(uint32_t *)(result + 0xC) = 0;
loc_0092A2EC:
    if (((v_stack_m8E) & (4)) == 0) goto loc_0092A6EA;
    if (v_stack_m70 == 0) goto loc_0092A6EA;
    result = memcpy(result + 20, v_stack_m70, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))), Arg4);
    goto loc_0092A325;
loc_0092A325:
    if (0 == 0) goto loc_0092A34F;
    if (((uint32_t)((uint32_t)(v_stack_mB4))) < 8) goto loc_0092A65C;
    if (((uint32_t)((uint32_t)(v_stack_mB4))) != ((uint32_t)(*(uint16_t *)(result + 0x14 + 0x2)))) goto loc_0092A65C;
    result = RtlValidAcl(result + 20, v_stack_m70, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0092A65C;
loc_0092A34F:
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 20))) - ((uint32_t)(result)));
    *(uint32_t *)(result + 0x10) = (uint32_t)(result);
    *(uint16_t *)(result + 0x14 + 0x2) = (uint16_t)((uint32_t)(v_stack_p8));
    local_rbx = (result + 20) + ((uint32_t)(v_stack_p8));
loc_0092A366:
    if (v_stack_m98 == 0) goto loc_0092A670;
    result = memcpy(local_rbx, v_stack_m98, (uint32_t)(v_stack_mA8), Arg4);
    *(uint8_t *)(local_rbx + 0x1) = (uint8_t)(v_stack_mA0);
    goto loc_0092A3A3;
loc_0092A3A3:
    if (0 == 0) goto loc_0092A3D3;
    if (local_rbx <= v_stack_m70) goto loc_0092A6C6;
    result = (uint8_t)((*(uint8_t *)(local_rbx)) & (15));
    if (((uint8_t)(result)) != 1) goto loc_0092A6C6;
    if (v_stack_mA0 > 15) goto loc_0092A6C6;
loc_0092A3D3:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(result)));
    local_rbx = (local_rbx) + ((uint32_t)(v_stack_m64));
loc_0092A3DF:
    *(uint32_t *)(result + 0x4) = (uint32_t)(Arg1);
    if (v_stack_m80 == 0) goto loc_0092A681;
    result = memcpy(local_rbx, v_stack_m80, (uint32_t)(v_stack_mA4), Arg4);
    *(uint8_t *)(local_rbx + 0x1) = (uint8_t)(v_stack_m9C);
    goto loc_0092A418;
loc_0092A418:
    if (0 == 0) goto loc_0092A43E;
    if (local_rbx <= v_stack_m70) goto loc_0092A6C6;
    result = (uint8_t)((*(uint8_t *)(local_rbx)) & (15));
    if (v_stack_m9C > 15) goto loc_0092A6C6;
    if (((uint8_t)(result)) != 1) goto loc_0092A6C6;
loc_0092A43E:
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(result)));
loc_0092A441:
    *(uint32_t *)(result + 0x8) = (uint32_t)(local_rbx);
loc_0092A445:
    *(uint64_t *)(arg5) = result;
loc_0092A450:
    result = 0;
loc_0092A452:
    return result;
loc_0092A470:
    if (0 == 0) goto loc_0092A6F7;
    result = v_stack_m80 + 1;
    if ((v_stack_m80 + 1) >= Arg4) { result = Arg4; }
    v_stack_m74 = (uint32_t)(*(uint8_t *)(result));
    v_stack_m7C = (uint32_t)(*(uint8_t *)(result) * 4 + 8);
    if ((uint32_t)(*(uint8_t *)(result) * 4 + 8) == 0) goto loc_0092A4C1;
    result = *(uint8_t *)(result) * 4 + 8;
    if (((v_stack_m58) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(local_rbx, v_stack_m80, (uint32_t)(v_stack_mA4), Arg4);
    }
    Arg1 = ((uint32_t)(v_stack_m7C)) + (v_stack_m58);
    if (Arg1 > Arg4) goto loc_0092A4BD;
    if (Arg1 >= v_stack_m58) goto loc_0092A4C6;
loc_0092A4BD:
loc_0092A4C1:
loc_0092A4C6:
    goto loc_0092A4CA;
loc_0092A4CA:
    v_stack_m88 = v_stack_m50;
    v_stack_m70 = v_stack_m60;
loc_0092A4EC:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m7C)) + (3));
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFFCULL));
    goto loc_0092A27A;
loc_0092A512:
    if (v_stack_m88 == 0) goto loc_0092A2E4;
    result = memcpy(*(uint64_t *)(v_stack_m28 + 0x38), v_stack_m88, (uint32_t)((uint32_t)((uint32_t)(v_stack_m90))), Arg4);
    goto loc_0092A545;
loc_0092A545:
    if (0 == 0) goto loc_0092A571;
    if (((uint32_t)((uint32_t)(v_stack_m90))) < 8) goto loc_0092A65C;
    if (((uint32_t)((uint32_t)(v_stack_m90))) != ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x2)))) goto loc_0092A65C;
    result = RtlValidAcl(*(uint64_t *)(v_stack_m28 + 0x38), v_stack_m88, (uint32_t)((uint32_t)((uint32_t)(v_stack_m90))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0092A65C;
loc_0092A571:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) - ((uint32_t)(local_r14)));
    *(uint32_t *)(local_r14 + 0xC) = (uint32_t)(result);
    *(uint16_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x2) = (uint16_t)((uint32_t)(v_stack_m40));
    local_rbx = (*(uint64_t *)(v_stack_m28 + 0x38)) + ((uint32_t)(v_stack_m40));
    goto loc_0092A2EC;
loc_0092A58A:
    local_rdi = 0;
    v_stack_m48 = 0;
    goto loc_0092A1D2;
loc_0092A596:
    if (v_stack_m88 == 0) goto loc_0092A124;
    if (0 == 0) goto loc_0092A70E;
    result = v_stack_m88 + 2;
    if ((v_stack_m88 + 2) >= Arg4) { result = Arg4; }
    v_stack_m90 = (uint32_t)(*(uint16_t *)(result));
    if ((uint32_t)(*(uint16_t *)(result)) == 0) goto loc_0092A610;
    result = *(uint16_t *)(result);
    if (((v_stack_m50) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_m88, v_stack_m88, (uint32_t)((uint32_t)((uint32_t)(v_stack_m90))), Arg4);
    }
    v_stack_m88 = v_stack_m50;
    if ((v_stack_m50 + result * 1) < v_stack_m50) goto loc_0092A5F4;
    if ((v_stack_m50 + result * 1) > Arg4) goto loc_0092A5F4;
    goto loc_0092A61A;
loc_0092A5F4:
    v_stack_m88 = v_stack_m50;
    goto loc_0092A61A;
loc_0092A610:
    v_stack_m88 = v_stack_m50;
loc_0092A61A:
    goto loc_0092A621;
loc_0092A621:
    v_stack_m70 = v_stack_m60;
loc_0092A639:
    result = (uint32_t)(((uint32_t)(v_stack_m90) + 3) & (0xFFFFFFFCULL));
    v_stack_m40 = (uint32_t)(result);
    result = (uint32_t)((result) + (-8));
    if (((uint32_t)(result)) <= 0xFFF7ULL) goto loc_0092A130;
loc_0092A652:
    goto loc_0092A452;
loc_0092A65C:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_r14, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m90))), Arg4);
    goto loc_0092A452;
loc_0092A670:
    Arg1 = 0;
    goto loc_0092A3DF;
loc_0092A681:
    local_rbx = 0;
    goto loc_0092A441;
loc_0092A688:
    if ((uint8_t)(Arg4) == 0) goto loc_0092A6DA;
    if (0 != 0) goto loc_00929FAF;
    v_stack_m30 = v_xmm0;
    goto loc_0092A005;
loc_0092A6B9:
    v_stack_m8C = (uint32_t)(*(uint16_t *)(v_stack_m48 + 0x2));
    goto loc_0092A1B7;
loc_0092A6C6:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_r14, Arg2, (uint32_t)(*(uint32_t *)(Arg1 + 0x10)), Arg4);
    goto loc_0092A452;
loc_0092A6DA:
    *(uint64_t *)(arg5) = 0;
    goto loc_0092A450;
loc_0092A6EA:
    *(uint32_t *)(local_r14 + 0x10) = 0;
    goto loc_0092A366;
loc_0092A6F7:
    v_stack_m74 = (uint32_t)(*(uint8_t *)(v_stack_m58 + 0x1));
    result = RtlLengthRequiredSid(*(uint8_t *)(v_stack_m58 + 0x1), Arg2, (uint32_t)(*(uint32_t *)(Arg1 + 0x10)), Arg4);
    v_stack_m7C = (uint32_t)(result);
    goto loc_0092A4EC;
loc_0092A70E:
    v_stack_m90 = (uint32_t)(*(uint16_t *)(*(uint8_t *)(v_stack_m58 + 0x1) + 0x2));
    goto loc_0092A639;
loc_0092A71D:
    v_stack_m78 = (uint32_t)(*(uint8_t *)(local_rbx + 0x1));
    result = RtlLengthRequiredSid(*(uint8_t *)(local_rbx + 0x1), Arg2, (uint32_t)(*(uint32_t *)(Arg1 + 0x10)), Arg4);
    v_stack_m80 = (uint32_t)(result);
    goto loc_0092A25F;
loc_0092A74C:
    goto loc_0092A452;
loc_0092A756:
    goto loc_0092A452;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00929F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
