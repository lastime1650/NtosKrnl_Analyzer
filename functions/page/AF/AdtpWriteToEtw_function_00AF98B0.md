# AdtpWriteToEtw

- RVA: `0x00AF98B0`–`0x00AF9CDF` (길이 `1,071` bytes)
- VA: `0x0000000140AF98B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DA180`
- 디코드: `276`개 명령, `1,071/1,071` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AF9904` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF9916` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF993B` → [AdtpNormalizeAuditInfoHelper](../../text/45/AdtpNormalizeAuditInfoHelper_function_00459834.md) (function, `0x00459834`)
- `0x00AF9995` → [AdtpPackageParameters](../../text/45/AdtpPackageParameters_function_00459964.md) (function, `0x00459964`)
- `0x00AF99C2` → [AdtpGetCategoryAndSubCategoryId](../A5/AdtpGetCategoryAndSubCategoryId_function_00A57588.md) (function, `0x00A57588`)
- `0x00AF9A9E` → [Feature_Servicing_EnhancedAuditingForKerberosEtypes__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Servicing_EnhancedAuditingForKerberosEtypes__private_IsEnabledDeviceUsageNoInline_function_0069D8F4.md) (function, `0x0069D8F4`)
- `0x00AF9BB5` → [Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline_function_0069D8A0.md) (function, `0x0069D8A0`)
- `0x00AF9BC6` → [Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline_function_0069D8A0.md) (function, `0x0069D8A0`)
- `0x00AF9C12` → [Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline_function_0069D8A0.md) (function, `0x0069D8A0`)
- `0x00AF9C5F` → [Feature_Servicing_RpcBufferAuditing__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Servicing_RpcBufferAuditing__private_IsEnabledDeviceUsageNoInline_function_0069D948.md) (function, `0x0069D948`)
- `0x00AF9C84` → [EtwWriteKMSecurityEvent](../../text/22/EtwWriteKMSecurityEvent_function_00225B8C.md) (function, `0x00225B8C`)
- `0x00AF9CAD` → [AdtpCleanupParameterAllocations](../../text/47/AdtpCleanupParameterAllocations_function_0047DFC4.md) (function, `0x0047DFC4`)
- `0x00AF9CBE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SepRmCallLsa](../../text/22/SepRmCallLsa_function_00223630.md) at `0x002237B3`

### Static image references
- `0x00AF98CF` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00AF9904` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF9916` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF993B` → [AdtpNormalizeAuditInfoHelper](../../text/45/AdtpNormalizeAuditInfoHelper_function_00459834.md) (`PAGE` → `.text`)
  - `0x00AF9995` → [AdtpPackageParameters](../../text/45/AdtpPackageParameters_function_00459964.md) (`PAGE` → `.text`)
  - `0x00AF9A9E` → [Feature_Servicing_EnhancedAuditingForKerberosEtypes__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Servicing_EnhancedAuditingForKerberosEtypes__private_IsEnabledDeviceUsageNoInline_function_0069D8F4.md) (`PAGE` → `.text`)
  - `0x00AF9BB5` → [Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline_function_0069D8A0.md) (`PAGE` → `.text`)
  - `0x00AF9BC6` → [Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline_function_0069D8A0.md) (`PAGE` → `.text`)
  - `0x00AF9C12` → [Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline_function_0069D8A0.md) (`PAGE` → `.text`)
  - `0x00AF9C5F` → [Feature_Servicing_RpcBufferAuditing__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_Servicing_RpcBufferAuditing__private_IsEnabledDeviceUsageNoInline_function_0069D948.md) (`PAGE` → `.text`)
  - `0x00AF9C84` → [EtwWriteKMSecurityEvent](../../text/22/EtwWriteKMSecurityEvent_function_00225B8C.md) (`PAGE` → `.text`)
  - `0x00AF9CAD` → [AdtpCleanupParameterAllocations](../../text/47/AdtpCleanupParameterAllocations_function_0047DFC4.md) (`PAGE` → `.text`)
  - `0x00AF9CBE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AF98B0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00AF98B5  55                              push rbp
00AF98B6  56                              push rsi
00AF98B7  57                              push rdi
00AF98B8  41 54                           push r12
00AF98BA  41 55                           push r13
00AF98BC  41 56                           push r14
00AF98BE  41 57                           push r15
00AF98C0  48 8D AC 24 20 F4 FF FF         lea rbp, [rsp - 0xbe0]
00AF98C8  48 81 EC E0 0C 00 00            sub rsp, 0xce0
00AF98CF  48 8B 05 6A 0E 31 00            mov rax, qword ptr [rip + 0x310e6a]
00AF98D6  48 33 C4                        xor rax, rsp
00AF98D9  48 89 85 D0 0B 00 00            mov qword ptr [rbp + 0xbd0], rax
00AF98E0  4C 8B FA                        mov r15, rdx
00AF98E3  4C 8B F1                        mov r14, rcx
00AF98E6  0F 57 C0                        xorps xmm0, xmm0
00AF98E9  48 8D 8D D0 03 00 00            lea rcx, [rbp + 0x3d0]
00AF98F0  33 FF                           xor edi, edi
00AF98F2  33 D2                           xor edx, edx
00AF98F4  41 B8 00 08 00 00               mov r8d, 0x800
00AF98FA  66 89 7C 24 40                  mov word ptr [rsp + 0x40], di
00AF98FF  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00AF9904  E8 37 D3 BC FF                  call 0x1406c6c40
00AF9909  33 D2                           xor edx, edx
00AF990B  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AF9910  41 B8 40 01 00 00               mov r8d, 0x140
00AF9916  E8 25 D3 BC FF                  call 0x1406c6c40
00AF991B  0F 57 C0                        xorps xmm0, xmm0
00AF991E  41 88 3F                        mov byte ptr [r15], dil
00AF9921  33 D2                           xor edx, edx
00AF9923  49 8B CE                        mov rcx, r14
00AF9926  0F 11 85 A0 03 00 00            movups xmmword ptr [rbp + 0x3a0], xmm0
00AF992D  0F 11 85 B0 03 00 00            movups xmmword ptr [rbp + 0x3b0], xmm0
00AF9934  0F 11 85 C0 03 00 00            movups xmmword ptr [rbp + 0x3c0], xmm0
00AF993B  E8 F4 FE 95 FF                  call 0x140459834
00AF9940  49 39 7E 30                     cmp qword ptr [r14 + 0x30], rdi
00AF9944  75 0A                           jne 0x140af9950
00AF9946  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AF994B  E9 46 03 00 00                  jmp 0x140af9c96
00AF9950  45 0F B7 66 12                  movzx r12d, word ptr [r14 + 0x12]
00AF9955  48 8D 85 A0 03 00 00            lea rax, [rbp + 0x3a0]
00AF995C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AF9961  4C 8D 8D D0 03 00 00            lea r9, [rbp + 0x3d0]
00AF9968  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AF996D  BB 02 00 00 00                  mov ebx, 2
00AF9972  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AF9977  44 8B C3                        mov r8d, ebx
00AF997A  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00AF9981  33 D2                           xor edx, edx
00AF9983  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AF9988  49 8B CE                        mov rcx, r14
00AF998B  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00AF9990  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF9995  E8 CA FF 95 FF                  call 0x140459964
00AF999A  8B F0                           mov esi, eax
00AF999C  85 C0                           test eax, eax
00AF999E  0F 88 F2 02 00 00               js 0x140af9c96
00AF99A4  41 0F B7 46 10                  movzx eax, word ptr [r14 + 0x10]
00AF99A9  66 85 C0                        test ax, ax
00AF99AC  74 1D                           je 0x140af99cb
00AF99AE  8B C8                           mov ecx, eax
00AF99B0  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00AF99B4  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00AF99B9  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00AF99BD  48 8D 54 24 44                  lea rdx, [rsp + 0x44]
00AF99C2  E8 C1 DB F5 FF                  call 0x140a57588
00AF99C7  85 C0                           test eax, eax
00AF99C9  79 07                           jns 0x140af99d2
00AF99CB  BE 00 FF 00 00                  mov esi, 0xff00
00AF99D0  EB 19                           jmp 0x140af99eb
00AF99D2  0F B7 4C 24 44                  movzx ecx, word ptr [rsp + 0x44]
00AF99D7  B8 00 01 00 00                  mov eax, 0x100
00AF99DC  66 83 C1 30                     add cx, 0x30
00AF99E0  0F B7 F1                        movzx esi, cx
00AF99E3  0F AF F0                        imul esi, eax
00AF99E6  66 03 74 24 48                  add si, word ptr [rsp + 0x48]
00AF99EB  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00AF99EF  B9 49 13 00 00                  mov ecx, 0x1349
00AF99F4  41 BD 08 00 00 00               mov r13d, 8
00AF99FA  3B C1                           cmp eax, ecx
00AF99FC  0F 87 3F 01 00 00               ja 0x140af9b41
00AF9A02  0F 84 BA 00 00 00               je 0x140af9ac2
00AF9A08  B9 A0 12 00 00                  mov ecx, 0x12a0
00AF9A0D  3B C1                           cmp eax, ecx
00AF9A0F  77 6C                           ja 0x140af9a7d
00AF9A11  0F 84 87 00 00 00               je 0x140af9a9e
00AF9A17  B9 59 12 00 00                  mov ecx, 0x1259
00AF9A1C  3B C1                           cmp eax, ecx
00AF9A1E  77 3A                           ja 0x140af9a5a
00AF9A20  0F 84 9C 00 00 00               je 0x140af9ac2
00AF9A26  2D 08 12 00 00                  sub eax, 0x1208
00AF9A2B  0F 84 91 00 00 00               je 0x140af9ac2
00AF9A31  41 2B C5                        sub eax, r13d
00AF9A34  74 20                           je 0x140af9a56
00AF9A36  83 E8 1E                        sub eax, 0x1e
00AF9A39  0F 84 83 00 00 00               je 0x140af9ac2
00AF9A3F  2B C3                           sub eax, ebx
00AF9A41  74 7F                           je 0x140af9ac2
00AF9A43  83 E8 05                        sub eax, 5
00AF9A46  74 7A                           je 0x140af9ac2
00AF9A48  2B C3                           sub eax, ebx
00AF9A4A  74 76                           je 0x140af9ac2
00AF9A4C  83 F8 19                        cmp eax, 0x19
00AF9A4F  74 73                           je 0x140af9ac4
00AF9A51  E9 01 02 00 00                  jmp 0x140af9c57
00AF9A56  B3 03                           mov bl, 3
00AF9A58  EB 6A                           jmp 0x140af9ac4
00AF9A5A  2D 5A 12 00 00                  sub eax, 0x125a
00AF9A5F  74 61                           je 0x140af9ac2
00AF9A61  83 E8 01                        sub eax, 1
00AF9A64  74 5C                           je 0x140af9ac2
00AF9A66  83 E8 01                        sub eax, 1
00AF9A69  74 57                           je 0x140af9ac2
00AF9A6B  83 E8 01                        sub eax, 1
00AF9A6E  74 52                           je 0x140af9ac2
00AF9A70  83 E8 01                        sub eax, 1
00AF9A73  74 4D                           je 0x140af9ac2
00AF9A75  83 F8 11                        cmp eax, 0x11
00AF9A78  E9 D4 01 00 00                  jmp 0x140af9c51
00AF9A7D  B9 19 13 00 00                  mov ecx, 0x1319
00AF9A82  3B C1                           cmp eax, ecx
00AF9A84  77 22                           ja 0x140af9aa8
00AF9A86  74 3A                           je 0x140af9ac2
00AF9A88  2D A1 12 00 00                  sub eax, 0x12a1
00AF9A8D  74 0F                           je 0x140af9a9e
00AF9A8F  83 E8 01                        sub eax, 1
00AF9A92  74 2E                           je 0x140af9ac2
00AF9A94  83 E8 2E                        sub eax, 0x2e
00AF9A97  74 29                           je 0x140af9ac2
00AF9A99  83 E8 46                        sub eax, 0x46
00AF9A9C  EB 1E                           jmp 0x140af9abc
00AF9A9E  E8 51 3E BA FF                  call 0x14069d8f4
00AF9AA3  E9 12 01 00 00                  jmp 0x140af9bba
00AF9AA8  2D 40 13 00 00                  sub eax, 0x1340
00AF9AAD  74 13                           je 0x140af9ac2
00AF9AAF  83 E8 01                        sub eax, 1
00AF9AB2  74 0E                           je 0x140af9ac2
00AF9AB4  83 E8 01                        sub eax, 1
00AF9AB7  74 09                           je 0x140af9ac2
00AF9AB9  83 E8 01                        sub eax, 1
00AF9ABC  0F 85 83 01 00 00               jne 0x140af9c45
00AF9AC2  B3 01                           mov bl, 1
00AF9AC4  41 0F B7 46 04                  movzx eax, word ptr [r14 + 4]
00AF9AC9  66 45 3B E5                     cmp r12w, r13w
00AF9ACD  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
00AF9AD2  48 B9 00 00 00 00 00 00 10 80   movabs rcx, 0x8010000000000000
00AF9ADC  48 B8 00 00 00 00 00 00 20 80   movabs rax, 0x8020000000000000
00AF9AE6  88 5C 24 52                     mov byte ptr [rsp + 0x52], bl
00AF9AEA  48 0F 45 C1                     cmovne rax, rcx
00AF9AEE  66 C7 44 24 53 0A 00            mov word ptr [rsp + 0x53], 0xa
00AF9AF5  0F B7 4C 24 40                  movzx ecx, word ptr [rsp + 0x40]
00AF9AFA  66 89 74 24 56                  mov word ptr [rsp + 0x56], si
00AF9AFF  40 88 7C 24 55                  mov byte ptr [rsp + 0x55], dil
00AF9B04  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00AF9B09  66 3B F9                        cmp di, cx
00AF9B0C  0F 83 57 01 00 00               jae 0x140af9c69
00AF9B12  48 8D 85 A8 00 00 00            lea rax, [rbp + 0xa8]
00AF9B19  8B D1                           mov edx, ecx
00AF9B1B  03 38                           add edi, dword ptr [rax]
00AF9B1D  48 8D 40 10                     lea rax, [rax + 0x10]
00AF9B21  48 83 EA 01                     sub rdx, 1
00AF9B25  75 F4                           jne 0x140af9b1b
00AF9B27  81 FF 00 DC 00 00               cmp edi, 0xdc00
00AF9B2D  0F 86 36 01 00 00               jbe 0x140af9c69
00AF9B33  41 C6 07 01                     mov byte ptr [r15], 1
00AF9B37  BE 05 00 00 80                  mov esi, 0x80000005
00AF9B3C  E9 5A 01 00 00                  jmp 0x140af9c9b
00AF9B41  B9 25 14 00 00                  mov ecx, 0x1425
00AF9B46  3B C1                           cmp eax, ecx
00AF9B48  0F 87 8B 00 00 00               ja 0x140af9bd9
00AF9B4E  74 76                           je 0x140af9bc6
00AF9B50  B9 1E 14 00 00                  mov ecx, 0x141e
00AF9B55  3B C1                           cmp eax, ecx
00AF9B57  77 34                           ja 0x140af9b8d
00AF9B59  0F 84 63 FF FF FF               je 0x140af9ac2
00AF9B5F  2D C2 13 00 00                  sub eax, 0x13c2
00AF9B64  0F 84 58 FF FF FF               je 0x140af9ac2
00AF9B6A  83 E8 01                        sub eax, 1
00AF9B6D  0F 84 4F FF FF FF               je 0x140af9ac2
00AF9B73  83 E8 42                        sub eax, 0x42
00AF9B76  0F 84 46 FF FF FF               je 0x140af9ac2
00AF9B7C  83 E8 0F                        sub eax, 0xf
00AF9B7F  0F 84 3D FF FF FF               je 0x140af9ac2
00AF9B85  83 E8 06                        sub eax, 6
00AF9B88  E9 BB 00 00 00                  jmp 0x140af9c48
00AF9B8D  2D 1F 14 00 00                  sub eax, 0x141f
00AF9B92  0F 84 2A FF FF FF               je 0x140af9ac2
00AF9B98  83 E8 01                        sub eax, 1
00AF9B9B  74 18                           je 0x140af9bb5
00AF9B9D  83 E8 01                        sub eax, 1
00AF9BA0  74 13                           je 0x140af9bb5
00AF9BA2  83 E8 01                        sub eax, 1
00AF9BA5  74 6B                           je 0x140af9c12
00AF9BA7  83 E8 01                        sub eax, 1
00AF9BAA  74 66                           je 0x140af9c12
00AF9BAC  83 F8 01                        cmp eax, 1
00AF9BAF  0F 85 A2 00 00 00               jne 0x140af9c57
00AF9BB5  E8 E6 3C BA FF                  call 0x14069d8a0
00AF9BBA  85 C0                           test eax, eax
00AF9BBC  0F 95 C3                        setne bl
00AF9BBF  FE C3                           inc bl
00AF9BC1  E9 FE FE FF FF                  jmp 0x140af9ac4
00AF9BC6  E8 D5 3C BA FF                  call 0x14069d8a0
00AF9BCB  85 C0                           test eax, eax
00AF9BCD  B3 03                           mov bl, 3
00AF9BCF  0F 95 C0                        setne al
00AF9BD2  02 D8                           add bl, al
00AF9BD4  E9 EB FE FF FF                  jmp 0x140af9ac4
00AF9BD9  B9 4C 15 00 00                  mov ecx, 0x154c
00AF9BDE  3B C1                           cmp eax, ecx
00AF9BE0  77 3F                           ja 0x140af9c21
00AF9BE2  0F 84 DA FE FF FF               je 0x140af9ac2
00AF9BE8  2D 26 14 00 00                  sub eax, 0x1426
00AF9BED  74 23                           je 0x140af9c12
00AF9BEF  83 E8 01                        sub eax, 1
00AF9BF2  74 1E                           je 0x140af9c12
00AF9BF4  83 E8 01                        sub eax, 1
00AF9BF7  74 19                           je 0x140af9c12
00AF9BF9  2D D8 00 00 00                  sub eax, 0xd8
00AF9BFE  0F 84 BE FE FF FF               je 0x140af9ac2
00AF9C04  83 E8 01                        sub eax, 1
00AF9C07  0F 84 B5 FE FF FF               je 0x140af9ac2
00AF9C0D  83 F8 4A                        cmp eax, 0x4a
00AF9C10  EB 3F                           jmp 0x140af9c51
00AF9C12  E8 89 3C BA FF                  call 0x14069d8a0
00AF9C17  85 C0                           test eax, eax
00AF9C19  0F 95 C3                        setne bl
00AF9C1C  E9 A3 FE FF FF                  jmp 0x140af9ac4
00AF9C21  2D 00 16 00 00                  sub eax, 0x1600
00AF9C26  0F 84 96 FE FF FF               je 0x140af9ac2
00AF9C2C  83 E8 50                        sub eax, 0x50
00AF9C2F  74 2E                           je 0x140af9c5f
00AF9C31  2D 30 02 00 00                  sub eax, 0x230
00AF9C36  0F 84 88 FE FF FF               je 0x140af9ac4
00AF9C3C  83 E8 01                        sub eax, 1
00AF9C3F  0F 84 7F FE FF FF               je 0x140af9ac4
00AF9C45  83 E8 01                        sub eax, 1
00AF9C48  0F 84 74 FE FF FF               je 0x140af9ac2
00AF9C4E  83 F8 01                        cmp eax, 1
00AF9C51  0F 84 6B FE FF FF               je 0x140af9ac2
00AF9C57  40 8A DF                        mov bl, dil
00AF9C5A  E9 65 FE FF FF                  jmp 0x140af9ac4
00AF9C5F  E8 E4 3C BA FF                  call 0x14069d948
00AF9C64  E9 51 FF FF FF                  jmp 0x140af9bba
00AF9C69  0F B7 C1                        movzx eax, cx
00AF9C6C  44 8B C1                        mov r8d, ecx
00AF9C6F  66 F7 D8                        neg ax
00AF9C72  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00AF9C77  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00AF9C7E  4D 1B C9                        sbb r9, r9
00AF9C81  4C 23 C8                        and r9, rax
00AF9C84  E8 03 BF 72 FF                  call 0x140225b8c
00AF9C89  8B F0                           mov esi, eax
00AF9C8B  3D FE 02 00 C0                  cmp eax, 0xc00002fe
00AF9C90  75 04                           jne 0x140af9c96
00AF9C92  41 C6 07 01                     mov byte ptr [r15], 1
00AF9C96  0F B7 4C 24 40                  movzx ecx, word ptr [rsp + 0x40]
00AF9C9B  44 0F B7 C1                     movzx r8d, cx
00AF9C9F  48 8D 95 A0 00 00 00            lea rdx, [rbp + 0xa0]
00AF9CA6  48 8D 8D A0 03 00 00            lea rcx, [rbp + 0x3a0]
00AF9CAD  E8 12 43 98 FF                  call 0x14047dfc4
00AF9CB2  8B C6                           mov eax, esi
00AF9CB4  48 8B 8D D0 0B 00 00            mov rcx, qword ptr [rbp + 0xbd0]
00AF9CBB  48 33 CC                        xor rcx, rsp
00AF9CBE  E8 7D 29 BB FF                  call 0x1406ac640
00AF9CC3  48 8B 9C 24 30 0D 00 00         mov rbx, qword ptr [rsp + 0xd30]
00AF9CCB  48 81 C4 E0 0C 00 00            add rsp, 0xce0
00AF9CD2  41 5F                           pop r15
00AF9CD4  41 5E                           pop r14
00AF9CD6  41 5D                           pop r13
00AF9CD8  41 5C                           pop r12
00AF9CDA  5F                              pop rdi
00AF9CDB  5E                              pop rsi
00AF9CDC  5D                              pop rbp
00AF9CDD  C3                              ret
00AF9CDE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AdtpWriteToEtw(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m848;
    unsigned __int64 v_stack_m858;
    unsigned __int64 v_stack_m868;
    unsigned __int64 v_stack_m878;
    unsigned __int64 v_stack_mB70;
    unsigned __int64 v_stack_mB78;
    unsigned __int64 v_stack_mC18;
    unsigned __int64 v_stack_mCB8;
    unsigned __int64 v_stack_mCC0;
    unsigned __int16 v_stack_mCC2;
    unsigned __int8 v_stack_mCC3;
    unsigned __int16 v_stack_mCC5;
    unsigned __int8 v_stack_mCC6;
    unsigned __int64 v_stack_mCC8;
    unsigned __int64 v_stack_mCD0;
    unsigned int v_stack_mCD4;
    unsigned __int16 v_stack_mCD8;
    unsigned __int64 v_stack_mCE0;
    unsigned __int64 v_stack_mCE8;
    unsigned __int64 v_stack_mCF0;
    unsigned __int64 v_stack_mCF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (0xCE0ULL);
    result = (*(unsigned __int64 *)(v_rip + 3214954)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = 0;
    a2 = 0;
    v_stack_mCD8 = 0;
    v_stack_mCC8 = v_xmm0;
    result = memset(v_stack_m848, a2, (unsigned int)(0x800ULL), a4);
    a2 = 0;
    result = memset(v_stack_mCB8, a2, 320, a4);
    *(unsigned __int8 *)(a2) = 0;
    a2 = 0;
    v_stack_m878 = v_xmm0;
    v_stack_m868 = v_xmm0;
    v_stack_m858 = v_xmm0;
    result = AdtpNormalizeAuditInfoHelper(a1, a2, 320, a4);
    if ((*(unsigned __int64 *)(a1 + 48)) != 0) goto loc_00AF9950;
    goto loc_00AF9C96;
loc_00AF9950:
    v_stack_mCE0 = v_stack_m878;
    v_stack_mCE8 = v_stack_mCD8;
    a2 = 0;
    v_stack_mCF0 = v_stack_mB78;
    v_stack_mCF8 = v_stack_mCB8;
    result = AdtpPackageParameters(a1, a2, 2, v_stack_m848);
    if (sign_flag) goto loc_00AF9C96;
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 16)) == 0) goto loc_00AF99CB;
    v_stack_mCD4 = 0;
    v_stack_mCD0 = 0;
    result = AdtpGetCategoryAndSubCategoryId((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 16))), v_stack_mCD4, v_stack_mCD0, v_stack_m848);
    if (!sign_flag) goto loc_00AF99D2;
loc_00AF99CB:
    goto loc_00AF99EB;
loc_00AF99D2:
    a1 = (unsigned __int16)((v_stack_mCD4) + (48));
    v_rsi = (unsigned int)(((unsigned __int16)(a1)) * (256));
    v_rsi = (unsigned __int16)((v_rsi) + (v_stack_mCD0));
loc_00AF99EB:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) > ((unsigned int)((unsigned int)(0x1349ULL)))) goto loc_00AF9B41;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) == ((unsigned int)((unsigned int)(0x1349ULL)))) goto loc_00AF9AC2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) > ((unsigned int)((unsigned int)(0x12A0ULL)))) goto loc_00AF9A7D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) == ((unsigned int)((unsigned int)(0x12A0ULL)))) goto loc_00AF9A9E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) > ((unsigned int)((unsigned int)(0x1259ULL)))) goto loc_00AF9A5A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) == ((unsigned int)((unsigned int)(0x1259ULL)))) goto loc_00AF9AC2;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) - (0x1208ULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (8));
    if (condition_is_equal) goto loc_00AF9A56;
    result = (unsigned int)((result) - (30));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (5));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_00AF9AC2;
    if (((unsigned int)(result)) == 25) goto loc_00AF9AC4;
    goto loc_00AF9C57;
loc_00AF9A56:
    goto loc_00AF9AC4;
loc_00AF9A5A:
    result = (unsigned int)((result) - (0x125AULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    goto loc_00AF9C51;
loc_00AF9A7D:
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(0x1319ULL)))) goto loc_00AF9AA8;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x1319ULL)))) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (0x12A1ULL));
    if (condition_is_equal) goto loc_00AF9A9E;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (46));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (70));
    goto loc_00AF9ABC;
loc_00AF9A9E:
    result = Feature_Servicing_EnhancedAuditingForKerberosEtypes__private_IsEnabledDeviceUsageNoInline((unsigned int)(0x1319ULL), v_stack_mCD4, v_stack_mCD0, v_stack_m848);
    goto loc_00AF9BBA;
loc_00AF9AA8:
    result = (unsigned int)((result) - (0x1340ULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
loc_00AF9ABC:
    if (condition_is_not_equal) goto loc_00AF9C45;
loc_00AF9AC2:
loc_00AF9AC4:
    v_stack_mCC8 = (unsigned __int16)(*(unsigned __int16 *)(a1 + 4));
    v_stack_mCC6 = 1;
    result = *(unsigned __int16 *)(a1 + 4);
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18))) != 8) { result = (unsigned int)(0x1319ULL); }
    v_stack_mCC5 = 10;
    v_stack_mCC2 = (unsigned __int16)(v_rsi);
    v_stack_mCC3 = 0;
    v_stack_mCC0 = result;
    if (0 >= ((unsigned __int16)(v_stack_mCD8))) goto loc_00AF9C69;
loc_00AF9B1B:
    v_rdi = (unsigned int)((v_rdi) + (*(unsigned int *)(v_stack_mB70)));
    a2 = ((unsigned int)((unsigned int)(v_stack_mCD8))) - (1);
    if (condition_is_not_equal) goto loc_00AF9B1B;
    if (((unsigned int)(v_rdi)) <= 0xDC00ULL) goto loc_00AF9C69;
    *(unsigned __int8 *)(a2) = 1;
    goto loc_00AF9C9B;
loc_00AF9B41:
    if (((unsigned int)(v_stack_mB70 + 16)) > ((unsigned int)((unsigned int)(0x1425ULL)))) goto loc_00AF9BD9;
    if (((unsigned int)(v_stack_mB70 + 16)) == ((unsigned int)((unsigned int)(0x1425ULL)))) goto loc_00AF9BC6;
    if (((unsigned int)(v_stack_mB70 + 16)) > ((unsigned int)((unsigned int)(0x141EULL)))) goto loc_00AF9B8D;
    if (((unsigned int)(v_stack_mB70 + 16)) == ((unsigned int)((unsigned int)(0x141EULL)))) goto loc_00AF9AC2;
    result = (unsigned int)((v_stack_mB70 + 16) - (0x13C2ULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (66));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (15));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (6));
    goto loc_00AF9C48;
loc_00AF9B8D:
    result = (unsigned int)((result) - (0x141FULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9BB5;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9BB5;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9C12;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9C12;
    if (((unsigned int)(result)) != 1) goto loc_00AF9C57;
loc_00AF9BB5:
    result = Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline((unsigned int)(0x141EULL), a2, v_stack_mCD0, v_stack_m848);
loc_00AF9BBA:
    v_rbx = ((unsigned int)(result) != 0) ? 1 : 0;
    v_rbx = (unsigned __int8)((v_rbx) + 1);
    goto loc_00AF9AC4;
loc_00AF9BC6:
    result = Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline((unsigned int)(0x141EULL), a2, v_stack_mCD0, v_stack_m848);
    result = ((unsigned int)(result) != 0) ? 1 : 0;
    v_rbx = (unsigned __int8)((3) + ((unsigned __int8)(result)));
    goto loc_00AF9AC4;
loc_00AF9BD9:
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(0x154CULL)))) goto loc_00AF9C21;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x154CULL)))) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (0x1426ULL));
    if (condition_is_equal) goto loc_00AF9C12;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9C12;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9C12;
    result = (unsigned int)((result) - (216));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    goto loc_00AF9C51;
loc_00AF9C12:
    result = Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline((unsigned int)(0x154CULL), a2, v_stack_mCD0, v_stack_m848);
    v_rbx = ((unsigned int)(result) != 0) ? 1 : 0;
    goto loc_00AF9AC4;
loc_00AF9C21:
    result = (unsigned int)((result) - (0x1600ULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (unsigned int)((result) - (80));
    if (condition_is_equal) goto loc_00AF9C5F;
    result = (unsigned int)((result) - (560));
    if (condition_is_equal) goto loc_00AF9AC4;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC4;
loc_00AF9C45:
    result = (unsigned int)((result) - (1));
loc_00AF9C48:
    if (condition_is_equal) goto loc_00AF9AC2;
loc_00AF9C51:
    if (((unsigned int)(result)) == 1) goto loc_00AF9AC2;
loc_00AF9C57:
    goto loc_00AF9AC4;
loc_00AF9C5F:
    result = Feature_Servicing_RpcBufferAuditing__private_IsEnabledDeviceUsageNoInline((unsigned int)(0x154CULL), a2, v_stack_mCD0, v_stack_m848);
    goto loc_00AF9BBA;
loc_00AF9C69:
    result = (unsigned __int16)(-((unsigned __int16)((unsigned int)(0x154CULL))));
    a4 = (v_stack_m848) & (v_stack_mB78);
    result = EtwWriteKMSecurityEvent(v_stack_mCC8, a2, (unsigned int)((unsigned int)((unsigned int)(0x154CULL))), a4);
    if (((unsigned int)(result)) == 0xC00002FEULL) {
        *(unsigned __int8 *)(a2) = 1;
    }
loc_00AF9C9B:
    result = AdtpCleanupParameterAllocations(v_stack_m878, v_stack_mB78, (unsigned __int16)(v_stack_mCD8), a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mB78, (unsigned __int16)(v_stack_mCD8), a4);
    v_rsp = (v_rsp) + (0xCE0ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AdtpWriteToEtw(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m848;
    uint64_t v_stack_m858;
    uint64_t v_stack_m868;
    uint64_t v_stack_m878;
    uint64_t v_stack_mB70;
    uint64_t v_stack_mB78;
    uint64_t v_stack_mC18;
    uint64_t v_stack_mCB8;
    uint64_t v_stack_mCC0;
    uint16_t v_stack_mCC2;
    uint8_t v_stack_mCC3;
    uint16_t v_stack_mCC5;
    uint8_t v_stack_mCC6;
    uint64_t v_stack_mCC8;
    uint64_t v_stack_mCD0;
    uint32_t v_stack_mCD4;
    uint16_t v_stack_mCD8;
    uint64_t v_stack_mCE0;
    uint64_t v_stack_mCE8;
    uint64_t v_stack_mCF0;
    uint64_t v_stack_mCF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (0xCE0ULL);
    result = (*(uint64_t *)(v_rip + 0x310E6A)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = 0;
    Arg2 = 0;
    v_stack_mCD8 = 0;
    v_stack_mCC8 = v_xmm0;
    result = memset(v_stack_m848, Arg2, (uint32_t)(0x800ULL), a4);
    Arg2 = 0;
    result = memset(v_stack_mCB8, Arg2, 320, a4);
    *(uint8_t *)(arg2) = 0;
    Arg2 = 0;
    v_stack_m878 = v_xmm0;
    v_stack_m868 = v_xmm0;
    v_stack_m858 = v_xmm0;
    result = AdtpNormalizeAuditInfoHelper(Arg1, Arg2, 320, a4);
    if ((*(uint64_t *)(arg1 + 0x30)) != 0) goto loc_00AF9950;
    goto loc_00AF9C96;
loc_00AF9950:
    v_stack_mCE0 = v_stack_m878;
    v_stack_mCE8 = v_stack_mCD8;
    Arg2 = 0;
    v_stack_mCF0 = v_stack_mB78;
    v_stack_mCF8 = v_stack_mCB8;
    result = AdtpPackageParameters(Arg1, Arg2, 2, v_stack_m848);
    if (sign_flag) goto loc_00AF9C96;
    if ((uint16_t)(*(uint16_t *)(arg1 + 0x10)) == 0) goto loc_00AF99CB;
    v_stack_mCD4 = 0;
    v_stack_mCD0 = 0;
    result = AdtpGetCategoryAndSubCategoryId((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x10))), v_stack_mCD4, v_stack_mCD0, v_stack_m848);
    if (!sign_flag) goto loc_00AF99D2;
loc_00AF99CB:
    goto loc_00AF99EB;
loc_00AF99D2:
    Arg1 = (uint16_t)((v_stack_mCD4) + (48));
    local_rsi = (uint32_t)(((uint16_t)(Arg1)) * (256));
    local_rsi = (uint16_t)((local_rsi) + (v_stack_mCD0));
loc_00AF99EB:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) > ((uint32_t)((uint32_t)(0x1349ULL)))) goto loc_00AF9B41;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) == ((uint32_t)((uint32_t)(0x1349ULL)))) goto loc_00AF9AC2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) > ((uint32_t)((uint32_t)(0x12A0ULL)))) goto loc_00AF9A7D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) == ((uint32_t)((uint32_t)(0x12A0ULL)))) goto loc_00AF9A9E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) > ((uint32_t)((uint32_t)(0x1259ULL)))) goto loc_00AF9A5A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) == ((uint32_t)((uint32_t)(0x1259ULL)))) goto loc_00AF9AC2;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) - (0x1208ULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (8));
    if (condition_is_equal) goto loc_00AF9A56;
    result = (uint32_t)((result) - (30));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (5));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_00AF9AC2;
    if (((uint32_t)(result)) == 25) goto loc_00AF9AC4;
    goto loc_00AF9C57;
loc_00AF9A56:
    goto loc_00AF9AC4;
loc_00AF9A5A:
    result = (uint32_t)((result) - (0x125AULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    goto loc_00AF9C51;
loc_00AF9A7D:
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(0x1319ULL)))) goto loc_00AF9AA8;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x1319ULL)))) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (0x12A1ULL));
    if (condition_is_equal) goto loc_00AF9A9E;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (46));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (70));
    goto loc_00AF9ABC;
loc_00AF9A9E:
    result = Feature_Servicing_EnhancedAuditingForKerberosEtypes__private_IsEnabledDeviceUsageNoInline((uint32_t)(0x1319ULL), v_stack_mCD4, v_stack_mCD0, v_stack_m848);
    goto loc_00AF9BBA;
loc_00AF9AA8:
    result = (uint32_t)((result) - (0x1340ULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
loc_00AF9ABC:
    if (condition_is_not_equal) goto loc_00AF9C45;
loc_00AF9AC2:
loc_00AF9AC4:
    v_stack_mCC8 = (uint16_t)(*(uint16_t *)(arg1 + 0x4));
    v_stack_mCC6 = 1;
    result = *(uint16_t *)(arg1 + 0x4);
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12))) != 8) { result = (uint32_t)(0x1319ULL); }
    v_stack_mCC5 = 10;
    v_stack_mCC2 = (uint16_t)(local_rsi);
    v_stack_mCC3 = 0;
    v_stack_mCC0 = result;
    if (0 >= ((uint16_t)(v_stack_mCD8))) goto loc_00AF9C69;
loc_00AF9B1B:
    local_rdi = (uint32_t)((local_rdi) + (*(uint32_t *)(v_stack_mB70)));
    Arg2 = ((uint32_t)((uint32_t)(v_stack_mCD8))) - (1);
    if (condition_is_not_equal) goto loc_00AF9B1B;
    if (((uint32_t)(local_rdi)) <= 0xDC00ULL) goto loc_00AF9C69;
    *(uint8_t *)(arg2) = 1;
    goto loc_00AF9C9B;
loc_00AF9B41:
    if (((uint32_t)(v_stack_mB70 + 16)) > ((uint32_t)((uint32_t)(0x1425ULL)))) goto loc_00AF9BD9;
    if (((uint32_t)(v_stack_mB70 + 16)) == ((uint32_t)((uint32_t)(0x1425ULL)))) goto loc_00AF9BC6;
    if (((uint32_t)(v_stack_mB70 + 16)) > ((uint32_t)((uint32_t)(0x141EULL)))) goto loc_00AF9B8D;
    if (((uint32_t)(v_stack_mB70 + 16)) == ((uint32_t)((uint32_t)(0x141EULL)))) goto loc_00AF9AC2;
    result = (uint32_t)((v_stack_mB70 + 16) - (0x13C2ULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (66));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (15));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (6));
    goto loc_00AF9C48;
loc_00AF9B8D:
    result = (uint32_t)((result) - (0x141FULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9BB5;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9BB5;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9C12;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9C12;
    if (((uint32_t)(result)) != 1) goto loc_00AF9C57;
loc_00AF9BB5:
    result = Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline((uint32_t)(0x141EULL), Arg2, v_stack_mCD0, v_stack_m848);
loc_00AF9BBA:
    local_rbx = ((uint32_t)(result) != 0) ? 1 : 0;
    local_rbx = (uint8_t)((local_rbx) + 1);
    goto loc_00AF9AC4;
loc_00AF9BC6:
    result = Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline((uint32_t)(0x141EULL), Arg2, v_stack_mCD0, v_stack_m848);
    result = ((uint32_t)(result) != 0) ? 1 : 0;
    local_rbx = (uint8_t)((3) + ((uint8_t)(result)));
    goto loc_00AF9AC4;
loc_00AF9BD9:
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(0x154CULL)))) goto loc_00AF9C21;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x154CULL)))) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (0x1426ULL));
    if (condition_is_equal) goto loc_00AF9C12;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9C12;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9C12;
    result = (uint32_t)((result) - (216));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC2;
    goto loc_00AF9C51;
loc_00AF9C12:
    result = Feature_Netsec_WFP_Audit_Event_Enrichment__private_IsEnabledDeviceUsageNoInline((uint32_t)(0x154CULL), Arg2, v_stack_mCD0, v_stack_m848);
    local_rbx = ((uint32_t)(result) != 0) ? 1 : 0;
    goto loc_00AF9AC4;
loc_00AF9C21:
    result = (uint32_t)((result) - (0x1600ULL));
    if (condition_is_equal) goto loc_00AF9AC2;
    result = (uint32_t)((result) - (80));
    if (condition_is_equal) goto loc_00AF9C5F;
    result = (uint32_t)((result) - (560));
    if (condition_is_equal) goto loc_00AF9AC4;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AF9AC4;
loc_00AF9C45:
    result = (uint32_t)((result) - (1));
loc_00AF9C48:
    if (condition_is_equal) goto loc_00AF9AC2;
loc_00AF9C51:
    if (((uint32_t)(result)) == 1) goto loc_00AF9AC2;
loc_00AF9C57:
    goto loc_00AF9AC4;
loc_00AF9C5F:
    result = Feature_Servicing_RpcBufferAuditing__private_IsEnabledDeviceUsageNoInline((uint32_t)(0x154CULL), Arg2, v_stack_mCD0, v_stack_m848);
    goto loc_00AF9BBA;
loc_00AF9C69:
    result = (uint16_t)(-((uint16_t)((uint32_t)(0x154CULL))));
    a4 = (v_stack_m848) & (v_stack_mB78);
    result = EtwWriteKMSecurityEvent(v_stack_mCC8, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x154CULL))), a4);
    if (((uint32_t)(result)) == 0xC00002FEULL) {
        *(uint8_t *)(arg2) = 1;
    }
loc_00AF9C9B:
    result = AdtpCleanupParameterAllocations(v_stack_m878, v_stack_mB78, (uint16_t)(v_stack_mCD8), a4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mB78, (uint16_t)(v_stack_mCD8), a4);
    local_rsp = (local_rsp) + (0xCE0ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `16` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x10` | `16` | `R` |
| `Arg1` | `+ 0x12` | `16` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AF98B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
