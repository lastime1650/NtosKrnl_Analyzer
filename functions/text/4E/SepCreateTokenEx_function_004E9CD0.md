# SepCreateTokenEx

- RVA: `0x004E9CD0`–`0x004EA93C` (길이 `3,180` bytes)
- VA: `0x00000001404E9CD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D13D0`
- 디코드: `767`개 명령, `3,180/3,180` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **49**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x004E9DAD` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004E9DC1` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004E9DE8` → [SeCaptureObjectAttributeSecurityDescriptorPresent](../45/SeCaptureObjectAttributeSecurityDescriptorPresent_function_0045F834.md) (function, `0x0045F834`)
- `0x004E9E18` → [RtlEqualSid](../40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x004E9E6C` → [RtlEqualSid](../40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x004E9E8B` → [RtlEqualSid](../40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x004E9F17` → [RtlIdentifierAuthoritySid](../../page/A7/RtlIdentifierAuthoritySid_function_00A76904.md) (function, `0x00A76904`)
- `0x004E9F26` → [RtlIdentifierAuthoritySid](../../page/A7/RtlIdentifierAuthoritySid_function_00A76904.md) (function, `0x00A76904`)
- `0x004E9FBB` → [RtlEqualSid](../40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x004E9FDD` → [RtlEqualSid](../40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x004EA109` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004EA148` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004EA192` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004EA1A4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004EA1B7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004EA1CB` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x004EA21F` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x004EA23C` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x004EA2AC` → [ObCreateObject](../../page/87/ObCreateObject_function_00872CB0.md) (function, `0x00872CB0`)
- `0x004EA2BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004EA2D2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004EA2DC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004EA2F7` → [ExInitializeResourceLite2](../41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x004EA431` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004EA4CA` → [SepReferenceLogonSession](../../page/A3/SepReferenceLogonSession_function_00A3B74C.md) (function, `0x00A3B74C`)
- `0x004EA4EA` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004EA5C4` → [RtlWalkFrameChain](../2F/RtlWalkFrameChain_function_002F85E0.md) (function, `0x002F85E0`)
- `0x004EA5ED` → [RtlWalkFrameChain](../2F/RtlWalkFrameChain_function_002F85E0.md) (function, `0x002F85E0`)
- `0x004EA5F5` → [SepAddTokenLogonSession](../../page/7A/SepAddTokenLogonSession_function_007A14E0.md) (function, `0x007A14E0`)
- `0x004EA619` → [SepSetTokenUserAndGroups](../../page/9F/SepSetTokenUserAndGroups_function_009FDCD0.md) (function, `0x009FDCD0`)
- `0x004EA687` → [RtlCopySidAndAttributesArray](../../page/9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x004EA6B8` → [RtlCopySidAndAttributesArray](../../page/9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x004EA6D1` → [RtlSidHashInitialize](../41/RtlSidHashInitialize_function_00416EA0.md) (function, `0x00416EA0`)
- `0x004EA6F2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004EA720` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x004EA72F` → [RtlCopySid](../../page/9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x004EA75D` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004EA780` → [SepSetTokenClaims](../../page/A6/SepSetTokenClaims_function_00A6E0D8.md) (function, `0x00A6E0D8`)
- `0x004EA78B` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (function, `0x006066CC`)
- `0x004EA797` → [SepUserClaimsContainAgentId](../../page/7A/SepUserClaimsContainAgentId_function_007A1148.md) (function, `0x007A1148`)
- `0x004EA7BD` → [SepSetTokenTrust](../../page/9E/SepSetTokenTrust_function_009E79B0.md) (function, `0x009E79B0`)
- `0x004EA7D0` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004EA851` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x004EA87D` → [SeCreateAccessState](../../page/8C/SeCreateAccessState_function_008C6AC0.md) (function, `0x008C6AC0`)
- `0x004EA8A7` → [ObInsertObject](../../page/8B/ObInsertObject_function_008B9100.md) (function, `0x008B9100`)
- `0x004EA8B2` → [SeDeleteAccessState](../../page/8C/SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x004EA8CD` → [SepFinalizeTokenAcls](../../page/8B/SepFinalizeTokenAcls_function_008B63F4.md) (function, `0x008B63F4`)
- `0x004EA90A` → [ObInsertObject](../../page/8B/ObInsertObject_function_008B9100.md) (function, `0x008B9100`)
- `0x004EA91F` → [SepFinalizeTokenAcls](../../page/8B/SepFinalizeTokenAcls_function_008B63F4.md) (function, `0x008B63F4`)

### Direct callers
- [SepCreateToken](../../page/7A/SepCreateToken_function_007A0DEC.md) at `0x007A0EAF`
- [NtCreateTokenEx](../../page/9C/NtCreateTokenEx_function_009C7C80.md) at `0x009C865C`

### Static image references
- `0x004E9CEF` → RVA `0x00E0A740` (`.data`; read)
- `0x004E9F1C` → RVA `0x00F05818` (`.data`; read)
- `0x004EA137` → RVA `0x00FD8010` (`PAGEDATA`; read)
- `0x004EA164` → RVA `0x00012D08` (`.rdata`; read)
- `0x004EA16E` → RVA `0x00E0EBF0` (`.data`; read/write)
- `0x004EA1F9` → RVA `0x00E67BF0` (`.data`; read)
- `0x004EA281` → RVA `0x00FD8020` (`PAGEDATA`; read)
- `0x004EA7B3` → RVA `0x00F05828` (`.data`; read)
- `0x004EA7E9` → RVA `0x00E67BA4` (`.data`; read)
- `0x004EA802` → RVA `0x00E67B98` (`.data`; read)
- `0x004EA815` → RVA `0x00E67BA8` (`.data`; read/write)
- `0x004EA83F` → RVA `0x00E67BA0` (`.data`; read)
- `0x004EA84A` → RVA `0x006CD6C0` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **30**
  - `0x004E9F17` → [RtlIdentifierAuthoritySid](../../page/A7/RtlIdentifierAuthoritySid_function_00A76904.md) (`.text` → `PAGE`)
  - `0x004E9F26` → [RtlIdentifierAuthoritySid](../../page/A7/RtlIdentifierAuthoritySid_function_00A76904.md) (`.text` → `PAGE`)
  - `0x004EA109` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004EA148` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004EA192` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004EA1A4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004EA1B7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004EA21F` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`.text` → `PAGE`)
  - `0x004EA23C` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`.text` → `PAGE`)
  - `0x004EA2AC` → [ObCreateObject](../../page/87/ObCreateObject_function_00872CB0.md) (`.text` → `PAGE`)
  - `0x004EA2BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004EA2D2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004EA2DC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004EA4CA` → [SepReferenceLogonSession](../../page/A3/SepReferenceLogonSession_function_00A3B74C.md) (`.text` → `PAGE`)
  - `0x004EA5F5` → [SepAddTokenLogonSession](../../page/7A/SepAddTokenLogonSession_function_007A14E0.md) (`.text` → `PAGE`)
  - `0x004EA619` → [SepSetTokenUserAndGroups](../../page/9F/SepSetTokenUserAndGroups_function_009FDCD0.md) (`.text` → `PAGE`)
  - `0x004EA687` → [RtlCopySidAndAttributesArray](../../page/9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (`.text` → `PAGE`)
  - `0x004EA6B8` → [RtlCopySidAndAttributesArray](../../page/9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (`.text` → `PAGE`)
  - `0x004EA6F2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004EA720` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`.text` → `PAGE`)
  - `0x004EA72F` → [RtlCopySid](../../page/9A/RtlCopySid_function_009A9A50.md) (`.text` → `PAGE`)
  - `0x004EA780` → [SepSetTokenClaims](../../page/A6/SepSetTokenClaims_function_00A6E0D8.md) (`.text` → `PAGE`)
  - `0x004EA797` → [SepUserClaimsContainAgentId](../../page/7A/SepUserClaimsContainAgentId_function_007A1148.md) (`.text` → `PAGE`)
  - `0x004EA7BD` → [SepSetTokenTrust](../../page/9E/SepSetTokenTrust_function_009E79B0.md) (`.text` → `PAGE`)
  - `0x004EA87D` → [SeCreateAccessState](../../page/8C/SeCreateAccessState_function_008C6AC0.md) (`.text` → `PAGE`)
  - `0x004EA8A7` → [ObInsertObject](../../page/8B/ObInsertObject_function_008B9100.md) (`.text` → `PAGE`)
  - `0x004EA8B2` → [SeDeleteAccessState](../../page/8C/SeDeleteAccessState_function_008C5F70.md) (`.text` → `PAGE`)
  - `0x004EA8CD` → [SepFinalizeTokenAcls](../../page/8B/SepFinalizeTokenAcls_function_008B63F4.md) (`.text` → `PAGE`)
  - `0x004EA90A` → [ObInsertObject](../../page/8B/ObInsertObject_function_008B9100.md) (`.text` → `PAGE`)
  - `0x004EA91F` → [SepFinalizeTokenAcls](../../page/8B/SepFinalizeTokenAcls_function_008B63F4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E9CD0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
004E9CD5  55                              push rbp
004E9CD6  56                              push rsi
004E9CD7  57                              push rdi
004E9CD8  41 54                           push r12
004E9CDA  41 55                           push r13
004E9CDC  41 56                           push r14
004E9CDE  41 57                           push r15
004E9CE0  48 8D AC 24 60 FE FF FF         lea rbp, [rsp - 0x1a0]
004E9CE8  48 81 EC A0 02 00 00            sub rsp, 0x2a0
004E9CEF  48 8B 05 4A 0A 92 00            mov rax, qword ptr [rip + 0x920a4a]
004E9CF6  48 33 C4                        xor rax, rsp
004E9CF9  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
004E9D00  48 8B 85 10 02 00 00            mov rax, qword ptr [rbp + 0x210]
004E9D07  45 33 F6                        xor r14d, r14d
004E9D0A  48 8B BD 20 02 00 00            mov rdi, qword ptr [rbp + 0x220]
004E9D11  8A DA                           mov bl, dl
004E9D13  4C 8B A5 30 02 00 00            mov r12, qword ptr [rbp + 0x230]
004E9D1A  49 8B F1                        mov rsi, r9
004E9D1D  4C 8B BD 50 02 00 00            mov r15, qword ptr [rbp + 0x250]
004E9D24  44 8B AD 28 02 00 00            mov r13d, dword ptr [rbp + 0x228]
004E9D2B  83 4C 24 58 FF                  or dword ptr [rsp + 0x58], 0xffffffff
004E9D30  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
004E9D34  48 8B 85 48 02 00 00            mov rax, qword ptr [rbp + 0x248]
004E9D3B  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
004E9D3F  48 8B 85 58 02 00 00            mov rax, qword ptr [rbp + 0x258]
004E9D46  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
004E9D4A  48 8B 85 60 02 00 00            mov rax, qword ptr [rbp + 0x260]
004E9D51  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
004E9D55  48 8B 85 70 02 00 00            mov rax, qword ptr [rbp + 0x270]
004E9D5C  48 89 45 00                     mov qword ptr [rbp], rax
004E9D60  48 8B 85 78 02 00 00            mov rax, qword ptr [rbp + 0x278]
004E9D67  48 89 45 F8                     mov qword ptr [rbp - 8], rax
004E9D6B  48 8B 85 88 02 00 00            mov rax, qword ptr [rbp + 0x288]
004E9D72  44 89 45 98                     mov dword ptr [rbp - 0x68], r8d
004E9D76  41 B8 A0 00 00 00               mov r8d, 0xa0
004E9D7C  88 54 24 53                     mov byte ptr [rsp + 0x53], dl
004E9D80  33 D2                           xor edx, edx
004E9D82  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
004E9D86  48 8D 4D 10                     lea rcx, [rbp + 0x10]
004E9D8A  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
004E9D8E  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
004E9D92  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
004E9D96  4C 89 65 D0                     mov qword ptr [rbp - 0x30], r12
004E9D9A  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
004E9D9F  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
004E9DA4  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
004E9DA8  44 89 74 24 54                  mov dword ptr [rsp + 0x54], r14d
004E9DAD  E8 8E CE 1D 00                  call 0x1406c6c40
004E9DB2  33 D2                           xor edx, edx
004E9DB4  48 8D 8D B0 00 00 00            lea rcx, [rbp + 0xb0]
004E9DBB  41 B8 E0 00 00 00               mov r8d, 0xe0
004E9DC1  E8 7A CE 1D 00                  call 0x1406c6c40
004E9DC6  4C 8D 44 24 51                  lea r8, [rsp + 0x51]
004E9DCB  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
004E9DCF  8A D3                           mov dl, bl
004E9DD1  44 88 74 24 50                  mov byte ptr [rsp + 0x50], r14b
004E9DD6  48 8B CE                        mov rcx, rsi
004E9DD9  44 88 74 24 52                  mov byte ptr [rsp + 0x52], r14b
004E9DDE  44 88 74 24 51                  mov byte ptr [rsp + 0x51], r14b
004E9DE3  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
004E9DE8  E8 47 5A F7 FF                  call 0x14045f834
004E9DED  85 C0                           test eax, eax
004E9DEF  0F 88 CC 03 00 00               js 0x1404ea1c1
004E9DF5  4C 8B 37                        mov r14, qword ptr [rdi]
004E9DF8  33 C0                           xor eax, eax
004E9DFA  8B D8                           mov ebx, eax
004E9DFC  45 85 ED                        test r13d, r13d
004E9DFF  74 61                           je 0x1404e9e62
004E9E01  44 8D 78 01                     lea r15d, [rax + 1]
004E9E05  8B F3                           mov esi, ebx
004E9E07  41 3B DD                        cmp ebx, r13d
004E9E0A  73 3C                           jae 0x1404e9e48
004E9E0C  8B FE                           mov edi, esi
004E9E0E  49 8B CE                        mov rcx, r14
004E9E11  48 03 FF                        add rdi, rdi
004E9E14  49 8B 14 FC                     mov rdx, qword ptr [r12 + rdi*8]
004E9E18  E8 B3 6C F1 FF                  call 0x140400ad0
004E9E1D  84 C0                           test al, al
004E9E1F  74 1F                           je 0x1404e9e40
004E9E21  41 8B 44 FC 08                  mov eax, dword ptr [r12 + rdi*8 + 8]
004E9E26  A8 20                           test al, 0x20
004E9E28  75 16                           jne 0x1404e9e40
004E9E2A  41 FF CD                        dec r13d
004E9E2D  41 8B C5                        mov eax, r13d
004E9E30  48 03 C0                        add rax, rax
004E9E33  41 0F 10 04 C4                  movups xmm0, xmmword ptr [r12 + rax*8]
004E9E38  F3 41 0F 7F 04 FC               movdqu xmmword ptr [r12 + rdi*8], xmm0
004E9E3E  EB 03                           jmp 0x1404e9e43
004E9E40  41 03 F7                        add esi, r15d
004E9E43  41 3B F5                        cmp esi, r13d
004E9E46  72 C4                           jb 0x1404e9e0c
004E9E48  8B C3                           mov eax, ebx
004E9E4A  41 03 DF                        add ebx, r15d
004E9E4D  48 03 C0                        add rax, rax
004E9E50  4D 8B 34 C4                     mov r14, qword ptr [r12 + rax*8]
004E9E54  41 3B DD                        cmp ebx, r13d
004E9E57  72 AC                           jb 0x1404e9e05
004E9E59  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
004E9E5E  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
004E9E62  48 8B 1F                        mov rbx, qword ptr [rdi]
004E9E65  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
004E9E69  48 8B D3                        mov rdx, rbx
004E9E6C  E8 5F 6C F1 FF                  call 0x140400ad0
004E9E71  84 C0                           test al, al
004E9E73  40 0F 95 C6                     setne sil
004E9E77  4D 85 FF                        test r15, r15
004E9E7A  75 09                           jne 0x1404e9e85
004E9E7C  45 8D 57 01                     lea r10d, [r15 + 1]
004E9E80  45 8A F2                        mov r14b, r10b
004E9E83  EB 1C                           jmp 0x1404e9ea1
004E9E85  48 8B D3                        mov rdx, rbx
004E9E88  49 8B CF                        mov rcx, r15
004E9E8B  E8 40 6C F1 FF                  call 0x140400ad0
004E9E90  45 33 FF                        xor r15d, r15d
004E9E93  84 C0                           test al, al
004E9E95  45 0F B6 F7                     movzx r14d, r15b
004E9E99  45 8D 57 01                     lea r10d, [r15 + 1]
004E9E9D  45 0F 45 F2                     cmovne r14d, r10d
004E9EA1  8B 47 08                        mov eax, dword ptr [rdi + 8]
004E9EA4  A8 10                           test al, 0x10
004E9EA6  74 15                           je 0x1404e9ebd
004E9EA8  A8 06                           test al, 6
004E9EAA  0F 85 27 02 00 00               jne 0x1404ea0d7
004E9EB0  41 B9 00 08 00 00               mov r9d, 0x800
004E9EB6  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
004E9EBB  EB 05                           jmp 0x1404e9ec2
004E9EBD  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
004E9EC2  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
004E9EC7  45 85 ED                        test r13d, r13d
004E9ECA  0F 84 56 01 00 00               je 0x1404ea026
004E9ED0  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
004E9ED5  49 83 C4 08                     add r12, 8
004E9ED9  45 8B FA                        mov r15d, r10d
004E9EDC  41 8B 1C 24                     mov ebx, dword ptr [r12]
004E9EE0  41 BB 00 20 00 00               mov r11d, 0x2000
004E9EE6  44 89 7C 24 74                  mov dword ptr [rsp + 0x74], r15d
004E9EEB  41 84 DA                        test r10b, bl
004E9EEE  74 07                           je 0x1404e9ef7
004E9EF0  83 CB 06                        or ebx, 6
004E9EF3  41 89 1C 24                     mov dword ptr [r12], ebx
004E9EF7  F6 C3 10                        test bl, 0x10
004E9EFA  74 13                           je 0x1404e9f0f
004E9EFC  F6 C3 06                        test bl, 6
004E9EFF  0F 85 D2 01 00 00               jne 0x1404ea0d7
004E9F05  41 0F BA E9 0B                  bts r9d, 0xb
004E9F0A  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
004E9F0F  49 8B 7C 24 F8                  mov rdi, qword ptr [r12 - 8]
004E9F14  48 8B CF                        mov rcx, rdi
004E9F17  E8 E8 C9 58 00                  call 0x140a76904
004E9F1C  48 8B 0D F5 B8 A1 00            mov rcx, qword ptr [rip + 0xa1b8f5]
004E9F23  48 8B D0                        mov rdx, rax
004E9F26  E8 D9 C9 58 00                  call 0x140a76904
004E9F2B  48 8B C8                        mov rcx, rax
004E9F2E  8B 00                           mov eax, dword ptr [rax]
004E9F30  3B 02                           cmp eax, dword ptr [rdx]
004E9F32  75 7B                           jne 0x1404e9faf
004E9F34  0F B7 41 04                     movzx eax, word ptr [rcx + 4]
004E9F38  66 3B 42 04                     cmp ax, word ptr [rdx + 4]
004E9F3C  75 71                           jne 0x1404e9faf
004E9F3E  0F B6 57 01                     movzx edx, byte ptr [rdi + 1]
004E9F42  33 C9                           xor ecx, ecx
004E9F44  84 D2                           test dl, dl
004E9F46  75 05                           jne 0x1404e9f4d
004E9F48  44 8B C1                        mov r8d, ecx
004E9F4B  EB 14                           jmp 0x1404e9f61
004E9F4D  8D 42 FF                        lea eax, [rdx - 1]
004E9F50  44 8B C2                        mov r8d, edx
004E9F53  81 7C 87 08 00 40 00 00         cmp dword ptr [rdi + rax*4 + 8], 0x4000
004E9F5B  0F 87 B8 00 00 00               ja 0x1404ea019
004E9F61  F6 C3 40                        test bl, 0x40
004E9F64  74 49                           je 0x1404e9faf
004E9F66  83 7C 24 58 FF                  cmp dword ptr [rsp + 0x58], -1
004E9F6B  0F 85 66 01 00 00               jne 0x1404ea0d7
004E9F71  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
004E9F76  84 D2                           test dl, dl
004E9F78  75 06                           jne 0x1404e9f80
004E9F7A  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
004E9F7E  EB 1B                           jmp 0x1404e9f9b
004E9F80  41 FF C8                        dec r8d
004E9F83  42 81 7C 87 08 00 30 00 00      cmp dword ptr [rdi + r8*4 + 8], 0x3000
004E9F8C  73 14                           jae 0x1404e9fa2
004E9F8E  33 C0                           xor eax, eax
004E9F90  88 44 24 50                     mov byte ptr [rsp + 0x50], al
004E9F94  46 39 5C 87 08                  cmp dword ptr [rdi + r8*4 + 8], r11d
004E9F99  73 0C                           jae 0x1404e9fa7
004E9F9B  44 88 54 24 52                  mov byte ptr [rsp + 0x52], r10b
004E9FA0  EB 0D                           jmp 0x1404e9faf
004E9FA2  44 88 54 24 50                  mov byte ptr [rsp + 0x50], r10b
004E9FA7  45 0B CB                        or r9d, r11d
004E9FAA  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
004E9FAF  40 84 F6                        test sil, sil
004E9FB2  75 1C                           jne 0x1404e9fd0
004E9FB4  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
004E9FB8  48 8B D7                        mov rdx, rdi
004E9FBB  E8 10 6B F1 FF                  call 0x140400ad0
004E9FC0  84 C0                           test al, al
004E9FC2  40 0F B6 F6                     movzx esi, sil
004E9FC6  41 BA 01 00 00 00               mov r10d, 1
004E9FCC  41 0F 45 F2                     cmovne esi, r10d
004E9FD0  45 84 F6                        test r14b, r14b
004E9FD3  75 2C                           jne 0x1404ea001
004E9FD5  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004E9FDA  48 8B D7                        mov rdx, rdi
004E9FDD  E8 EE 6A F1 FF                  call 0x140400ad0
004E9FE2  84 C0                           test al, al
004E9FE4  74 15                           je 0x1404e9ffb
004E9FE6  F6 C3 08                        test bl, 8
004E9FE9  74 4F                           je 0x1404ea03a
004E9FEB  41 BA 01 00 00 00               mov r10d, 1
004E9FF1  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
004E9FF6  45 8A F2                        mov r14b, r10b
004E9FF9  EB 06                           jmp 0x1404ea001
004E9FFB  41 BA 01 00 00 00               mov r10d, 1
004EA001  45 03 FA                        add r15d, r10d
004EA004  49 83 C4 10                     add r12, 0x10
004EA008  44 39 6C 24 74                  cmp dword ptr [rsp + 0x74], r13d
004EA00D  73 14                           jae 0x1404ea023
004EA00F  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
004EA014  E9 C3 FE FF FF                  jmp 0x1404e9edc
004EA019  B8 46 04 00 C0                  mov eax, 0xc0000446
004EA01E  E9 9E 01 00 00                  jmp 0x1404ea1c1
004EA023  45 33 FF                        xor r15d, r15d
004EA026  40 84 F6                        test sil, sil
004EA029  75 0A                           jne 0x1404ea035
004EA02B  B8 5B 00 00 C0                  mov eax, 0xc000005b
004EA030  E9 8C 01 00 00                  jmp 0x1404ea1c1
004EA035  45 84 F6                        test r14b, r14b
004EA038  75 0A                           jne 0x1404ea044
004EA03A  B8 5A 00 00 C0                  mov eax, 0xc000005a
004EA03F  E9 7D 01 00 00                  jmp 0x1404ea1c1
004EA044  44 8B 9D 40 02 00 00            mov r11d, dword ptr [rbp + 0x240]
004EA04B  49 8B DF                        mov rbx, r15
004EA04E  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
004EA052  4D 8B D7                        mov r10, r15
004EA055  4C 89 7D B0                     mov qword ptr [rbp - 0x50], r15
004EA059  49 8B FF                        mov rdi, r15
004EA05C  4C 89 7D B8                     mov qword ptr [rbp - 0x48], r15
004EA060  45 8B CF                        mov r9d, r15d
004EA063  45 85 DB                        test r11d, r11d
004EA066  74 58                           je 0x1404ea0c0
004EA068  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
004EA06C  48 83 C2 08                     add rdx, 8
004EA070  8B 0A                           mov ecx, dword ptr [rdx]
004EA072  F7 C1 F8 FF FF 7F               test ecx, 0x7ffffff8
004EA078  75 5D                           jne 0x1404ea0d7
004EA07A  44 8B 42 F8                     mov r8d, dword ptr [rdx - 8]
004EA07E  83 E1 03                        and ecx, 3
004EA081  89 0A                           mov dword ptr [rdx], ecx
004EA083  41 83 F8 24                     cmp r8d, 0x24
004EA087  77 62                           ja 0x1404ea0eb
004EA089  4D 0F A3 C2                     bt r10, r8
004EA08D  72 52                           jb 0x1404ea0e1
004EA08F  41 8B C0                        mov eax, r8d
004EA092  49 0F AB C2                     bts r10, rax
004EA096  4C 89 55 B0                     mov qword ptr [rbp - 0x50], r10
004EA09A  F6 C1 02                        test cl, 2
004EA09D  74 08                           je 0x1404ea0a7
004EA09F  48 0F AB C7                     bts rdi, rax
004EA0A3  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
004EA0A7  F6 C1 01                        test cl, 1
004EA0AA  74 08                           je 0x1404ea0b4
004EA0AC  48 0F AB C3                     bts rbx, rax
004EA0B0  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
004EA0B4  41 FF C1                        inc r9d
004EA0B7  48 83 C2 0C                     add rdx, 0xc
004EA0BB  45 3B CB                        cmp r9d, r11d
004EA0BE  72 B0                           jb 0x1404ea070
004EA0C0  48 8B 85 90 02 00 00            mov rax, qword ptr [rbp + 0x290]
004EA0C7  41 BE FC FF FF FF               mov r14d, 0xfffffffc
004EA0CD  48 85 C0                        test rax, rax
004EA0D0  74 23                           je 0x1404ea0f5
004EA0D2  44 85 30                        test dword ptr [rax], r14d
004EA0D5  74 1E                           je 0x1404ea0f5
004EA0D7  B8 0D 00 00 C0                  mov eax, 0xc000000d
004EA0DC  E9 E0 00 00 00                  jmp 0x1404ea1c1
004EA0E1  B8 A6 01 00 C0                  mov eax, 0xc00001a6
004EA0E6  E9 D6 00 00 00                  jmp 0x1404ea1c1
004EA0EB  B8 60 00 00 C0                  mov eax, 0xc0000060
004EA0F0  E9 CC 00 00 00                  jmp 0x1404ea1c1
004EA0F5  BB 53 65 41 74                  mov ebx, 0x74416553
004EA0FA  BF 00 01 00 00                  mov edi, 0x100
004EA0FF  44 8B C3                        mov r8d, ebx
004EA102  8B CF                           mov ecx, edi
004EA104  BA 30 00 00 00                  mov edx, 0x30
004EA109  E8 E2 7F 69 00                  call 0x140b820f0
004EA10E  48 8B F0                        mov rsi, rax
004EA111  48 85 C0                        test rax, rax
004EA114  0F 84 A2 00 00 00               je 0x1404ea1bc
004EA11A  44 89 38                        mov dword ptr [rax], r15d
004EA11D  48 83 C0 08                     add rax, 8
004EA121  44 89 7E 18                     mov dword ptr [rsi + 0x18], r15d
004EA125  48 89 40 08                     mov qword ptr [rax + 8], rax
004EA129  48 89 00                        mov qword ptr [rax], rax
004EA12C  48 8D 46 20                     lea rax, [rsi + 0x20]
004EA130  48 89 40 08                     mov qword ptr [rax + 8], rax
004EA134  48 89 00                        mov qword ptr [rax], rax
004EA137  44 39 3D D2 DE AE 00            cmp dword ptr [rip + 0xaeded2], r15d
004EA13E  74 1F                           je 0x1404ea15f
004EA140  44 8B C3                        mov r8d, ebx
004EA143  8D 57 20                        lea edx, [rdi + 0x20]
004EA146  8B CF                           mov ecx, edi
004EA148  E8 A3 7F 69 00                  call 0x140b820f0
004EA14D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
004EA152  48 8B D8                        mov rbx, rax
004EA155  48 85 C0                        test rax, rax
004EA158  75 0A                           jne 0x1404ea164
004EA15A  48 8B CE                        mov rcx, rsi
004EA15D  EB 56                           jmp 0x1404ea1b5
004EA15F  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
004EA164  48 8B 15 9D 8B B2 FF            mov rdx, qword ptr [rip - 0x4d7463]
004EA16B  48 8B C2                        mov rax, rdx
004EA16E  F0 48 0F C1 05 79 4A 92 00      lock xadd qword ptr [rip + 0x924a79], rax
004EA177  48 03 C2                        add rax, rdx
004EA17A  41 B8 53 65 54 6C               mov r8d, 0x6c546553
004EA180  BA 68 00 00 00                  mov edx, 0x68
004EA185  89 45 A0                        mov dword ptr [rbp - 0x60], eax
004EA188  48 C1 E8 20                     shr rax, 0x20
004EA18C  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
004EA18F  8D 4A D8                        lea ecx, [rdx - 0x28]
004EA192  E8 59 7F 69 00                  call 0x140b820f0
004EA197  48 8B F8                        mov rdi, rax
004EA19A  48 85 C0                        test rax, rax
004EA19D  75 4D                           jne 0x1404ea1ec
004EA19F  33 D2                           xor edx, edx
004EA1A1  48 8B CE                        mov rcx, rsi
004EA1A4  E8 C7 86 69 00                  call 0x140b82870
004EA1A9  44 39 3D 60 DE AE 00            cmp dword ptr [rip + 0xaede60], r15d
004EA1B0  74 0A                           je 0x1404ea1bc
004EA1B2  48 8B CB                        mov rcx, rbx
004EA1B5  33 D2                           xor edx, edx
004EA1B7  E8 B4 86 69 00                  call 0x140b82870
004EA1BC  B8 9A 00 00 C0                  mov eax, 0xc000009a
004EA1C1  48 8B 8D 90 01 00 00            mov rcx, qword ptr [rbp + 0x190]
004EA1C8  48 33 CC                        xor rcx, rsp
004EA1CB  E8 70 24 1C 00                  call 0x1406ac640
004EA1D0  48 8B 9C 24 E8 02 00 00         mov rbx, qword ptr [rsp + 0x2e8]
004EA1D8  48 81 C4 A0 02 00 00            add rsp, 0x2a0
004EA1DF  41 5F                           pop r15
004EA1E1  41 5E                           pop r14
004EA1E3  41 5D                           pop r13
004EA1E5  41 5C                           pop r12
004EA1E7  5F                              pop rdi
004EA1E8  5E                              pop rsi
004EA1E9  5D                              pop rbp
004EA1EA  C3                              ret
004EA1EB  CC                              int3
004EA1EC  44 8B A5 38 02 00 00            mov r12d, dword ptr [rbp + 0x238]
004EA1F3  41 8B DD                        mov ebx, r13d
004EA1F6  C1 E3 04                        shl ebx, 4
004EA1F9  44 38 3D F0 D9 97 00            cmp byte ptr [rip + 0x97d9f0], r15b
004EA200  74 0A                           je 0x1404ea20c
004EA202  44 8D 73 17                     lea r14d, [rbx + 0x17]
004EA206  41 83 E6 F8                     and r14d, 0xfffffff8
004EA20A  EB 28                           jmp 0x1404ea234
004EA20C  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
004EA210  41 83 C4 07                     add r12d, 7
004EA214  41 83 E4 F8                     and r12d, 0xfffffff8
004EA218  48 8B 00                        mov rax, qword ptr [rax]
004EA21B  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
004EA21F  E8 AC 02 4E 00                  call 0x1409ca4d0
004EA224  83 C0 03                        add eax, 3
004EA227  41 23 C6                        and eax, r14d
004EA22A  45 8D 74 24 10                  lea r14d, [r12 + 0x10]
004EA22F  03 C3                           add eax, ebx
004EA231  44 03 F0                        add r14d, eax
004EA234  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
004EA238  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
004EA23C  E8 8F 02 4E 00                  call 0x1409ca4d0
004EA241  BA FC FF FF FF                  mov edx, 0xfffffffc
004EA246  45 33 C0                        xor r8d, r8d
004EA249  44 8D 78 03                     lea r15d, [rax + 3]
004EA24D  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
004EA251  44 23 FA                        and r15d, edx
004EA254  48 85 C0                        test rax, rax
004EA257  74 0C                           je 0x1404ea265
004EA259  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
004EA25D  83 C1 03                        add ecx, 3
004EA260  23 CA                           and ecx, edx
004EA262  44 03 F9                        add r15d, ecx
004EA265  41 8D 8E C0 05 00 00            lea ecx, [r14 + 0x5c0]
004EA26C  B8 00 10 00 00                  mov eax, 0x1000
004EA271  44 3B F8                        cmp r15d, eax
004EA274  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
004EA279  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
004EA27E  41 B1 01                        mov r9b, 1
004EA281  48 8B 15 98 DD AE 00            mov rdx, qword ptr [rip + 0xaedd98]
004EA288  41 0F 43 C7                     cmovae eax, r15d
004EA28C  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
004EA291  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
004EA295  03 C1                           add eax, ecx
004EA297  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004EA29B  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
004EA29F  8A 4C 24 53                     mov cl, byte ptr [rsp + 0x53]
004EA2A3  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
004EA2A8  4C 8B 45 E8                     mov r8, qword ptr [rbp - 0x18]
004EA2AC  E8 FF 89 38 00                  call 0x140872cb0
004EA2B1  8B D8                           mov ebx, eax
004EA2B3  85 C0                           test eax, eax
004EA2B5  79 31                           jns 0x1404ea2e8
004EA2B7  33 D2                           xor edx, edx
004EA2B9  48 8B CE                        mov rcx, rsi
004EA2BC  E8 AF 85 69 00                  call 0x140b82870
004EA2C1  33 C0                           xor eax, eax
004EA2C3  39 05 47 DD AE 00               cmp dword ptr [rip + 0xaedd47], eax
004EA2C9  74 0C                           je 0x1404ea2d7
004EA2CB  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
004EA2D0  33 D2                           xor edx, edx
004EA2D2  E8 99 85 69 00                  call 0x140b82870
004EA2D7  33 D2                           xor edx, edx
004EA2D9  48 8B CF                        mov rcx, rdi
004EA2DC  E8 8F 85 69 00                  call 0x140b82870
004EA2E1  8B C3                           mov eax, ebx
004EA2E3  E9 D9 FE FF FF                  jmp 0x1404ea1c1
004EA2E8  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
004EA2ED  83 CA FF                        or edx, 0xffffffff
004EA2F0  48 8B CF                        mov rcx, rdi
004EA2F3  48 89 7B 30                     mov qword ptr [rbx + 0x30], rdi
004EA2F7  E8 14 54 F3 FF                  call 0x14041f710
004EA2FC  48 8B 0D 05 8A B2 FF            mov rcx, qword ptr [rip - 0x4d75fb]
004EA303  48 8B C1                        mov rax, rcx
004EA306  F0 48 0F C1 05 E1 48 92 00      lock xadd qword ptr [rip + 0x9248e1], rax
004EA30F  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
004EA314  48 03 C1                        add rax, rcx
004EA317  89 43 10                        mov dword ptr [rbx + 0x10], eax
004EA31A  33 D2                           xor edx, edx
004EA31C  48 C1 E8 20                     shr rax, 0x20
004EA320  41 B8 10 01 00 00               mov r8d, 0x110
004EA326  89 43 14                        mov dword ptr [rbx + 0x14], eax
004EA329  33 DB                           xor ebx, ebx
004EA32B  48 89 5F 20                     mov qword ptr [rdi + 0x20], rbx
004EA32F  8B C3                           mov eax, ebx
004EA331  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
004EA335  48 89 9F E0 00 00 00            mov qword ptr [rdi + 0xe0], rbx
004EA33C  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
004EA341  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
004EA346  48 8B 00                        mov rax, qword ptr [rax]
004EA349  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
004EA34D  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
004EA351  88 9F CC 00 00 00               mov byte ptr [rdi + 0xcc], bl
004EA357  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
004EA35B  48 8B 85 18 02 00 00            mov rax, qword ptr [rbp + 0x218]
004EA362  48 8B 08                        mov rcx, qword ptr [rax]
004EA365  8B 85 00 02 00 00               mov eax, dword ptr [rbp + 0x200]
004EA36B  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
004EA36F  48 8D 8F 28 03 00 00            lea rcx, [rdi + 0x328]
004EA376  89 87 C0 00 00 00               mov dword ptr [rdi + 0xc0], eax
004EA37C  8B 85 08 02 00 00               mov eax, dword ptr [rbp + 0x208]
004EA382  89 87 C4 00 00 00               mov dword ptr [rdi + 0xc4], eax
004EA388  48 8B 85 68 02 00 00            mov rax, qword ptr [rbp + 0x268]
004EA38F  0F 10 00                        movups xmm0, xmmword ptr [rax]
004EA392  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
004EA396  F3 0F 7F 07                     movdqu xmmword ptr [rdi], xmm0
004EA39A  89 87 C8 00 00 00               mov dword ptr [rdi + 0xc8], eax
004EA3A0  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
004EA3A4  89 5F 78                        mov dword ptr [rdi + 0x78], ebx
004EA3A7  48 89 9F 88 04 00 00            mov qword ptr [rdi + 0x488], rbx
004EA3AE  89 87 88 00 00 00               mov dword ptr [rdi + 0x88], eax
004EA3B4  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
004EA3B8  89 9F 8C 00 00 00               mov dword ptr [rdi + 0x8c], ebx
004EA3BE  89 87 90 00 00 00               mov dword ptr [rdi + 0x90], eax
004EA3C4  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
004EA3C8  48 89 9F B8 00 00 00            mov qword ptr [rdi + 0xb8], rbx
004EA3CF  48 89 9F 60 04 00 00            mov qword ptr [rdi + 0x460], rbx
004EA3D6  48 89 9F 68 04 00 00            mov qword ptr [rdi + 0x468], rbx
004EA3DD  44 89 B7 84 00 00 00            mov dword ptr [rdi + 0x84], r14d
004EA3E4  89 87 D0 00 00 00               mov dword ptr [rdi + 0xd0], eax
004EA3EA  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
004EA3EE  89 9F D4 00 00 00               mov dword ptr [rdi + 0xd4], ebx
004EA3F4  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
004EA3F8  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
004EA3FC  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
004EA400  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
004EA404  48 89 47 50                     mov qword ptr [rdi + 0x50], rax
004EA408  89 9F 20 03 00 00               mov dword ptr [rdi + 0x320], ebx
004EA40E  48 89 9F 18 03 00 00            mov qword ptr [rdi + 0x318], rbx
004EA415  48 89 9F 10 03 00 00            mov qword ptr [rdi + 0x310], rbx
004EA41C  48 89 9F 38 04 00 00            mov qword ptr [rdi + 0x438], rbx
004EA423  48 89 9F 40 04 00 00            mov qword ptr [rdi + 0x440], rbx
004EA42A  48 89 9F 80 04 00 00            mov qword ptr [rdi + 0x480], rbx
004EA431  E8 0A C8 1D 00                  call 0x1406c6c40
004EA436  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
004EA43B  48 89 9F 50 04 00 00            mov qword ptr [rdi + 0x450], rbx
004EA442  48 89 9F 58 04 00 00            mov qword ptr [rdi + 0x458], rbx
004EA449  48 89 9F 70 04 00 00            mov qword ptr [rdi + 0x470], rbx
004EA450  48 89 87 78 04 00 00            mov qword ptr [rdi + 0x478], rax
004EA457  48 8B 85 90 02 00 00            mov rax, qword ptr [rbp + 0x290]
004EA45E  48 85 C0                        test rax, rax
004EA461  74 08                           je 0x1404ea46b
004EA463  8B 00                           mov eax, dword ptr [rax]
004EA465  89 87 D4 00 00 00               mov dword ptr [rdi + 0xd4], eax
004EA46B  38 5C 24 50                     cmp byte ptr [rsp + 0x50], bl
004EA46F  75 12                           jne 0x1404ea483
004EA471  48 B8 7B F9 E9 DF EE FF FF FF   movabs rax, 0xffffffeedfe9f97b
004EA47B  48 21 47 48                     and qword ptr [rdi + 0x48], rax
004EA47F  48 21 47 50                     and qword ptr [rdi + 0x50], rax
004EA483  80 7C 24 52 01                  cmp byte ptr [rsp + 0x52], 1
004EA488  75 12                           jne 0x1404ea49c
004EA48A  48 B8 00 00 80 02 02 00 00 00   movabs rax, 0x202800000
004EA494  48 21 47 48                     and qword ptr [rdi + 0x48], rax
004EA498  48 21 47 50                     and qword ptr [rdi + 0x50], rax
004EA49C  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
004EA4A0  0F 57 C0                        xorps xmm0, xmm0
004EA4A3  0F 11 47 58                     movups xmmword ptr [rdi + 0x58], xmm0
004EA4A7  0F 11 47 68                     movups xmmword ptr [rdi + 0x68], xmm0
004EA4AB  48 89 B7 08 03 00 00            mov qword ptr [rdi + 0x308], rsi
004EA4B2  48 89 9F 48 04 00 00            mov qword ptr [rdi + 0x448], rbx
004EA4B9  48 89 9F B0 00 00 00            mov qword ptr [rdi + 0xb0], rbx
004EA4C0  48 8D 9F D8 00 00 00            lea rbx, [rdi + 0xd8]
004EA4C7  48 8B D3                        mov rdx, rbx
004EA4CA  E8 7D 12 55 00                  call 0x140a3b74c
004EA4CF  45 33 C0                        xor r8d, r8d
004EA4D2  8B F0                           mov esi, eax
004EA4D4  85 C0                           test eax, eax
004EA4D6  79 1E                           jns 0x1404ea4f6
004EA4D8  83 8F C8 00 00 00 20            or dword ptr [rdi + 0xc8], 0x20
004EA4DF  BA 44 66 6C 74                  mov edx, 0x746c6644
004EA4E4  48 8B CF                        mov rcx, rdi
004EA4E7  4C 89 03                        mov qword ptr [rbx], r8
004EA4EA  E8 F1 D3 E0 FF                  call 0x1402f78e0
004EA4EF  8B C6                           mov eax, esi
004EA4F1  E9 CB FC FF FF                  jmp 0x1404ea1c1
004EA4F6  44 39 05 13 DB AE 00            cmp dword ptr [rip + 0xaedb13], r8d
004EA4FD  0F 84 FA 00 00 00               je 0x1404ea5fd
004EA503  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
004EA50C  BB 1E 00 00 00                  mov ebx, 0x1e
004EA511  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004EA516  48 8B 88 78 04 00 00            mov rcx, qword ptr [rax + 0x478]
004EA51D  48 8B 82 08 05 00 00            mov rax, qword ptr [rdx + 0x508]
004EA524  48 89 01                        mov qword ptr [rcx], rax
004EA527  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004EA530  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
004EA535  48 8B 80 10 05 00 00            mov rax, qword ptr [rax + 0x510]
004EA53C  48 8B 8A 78 04 00 00            mov rcx, qword ptr [rdx + 0x478]
004EA543  48 89 41 08                     mov qword ptr [rcx + 8], rax
004EA547  48 8B 82 78 04 00 00            mov rax, qword ptr [rdx + 0x478]
004EA54E  C7 40 20 0C 00 00 00            mov dword ptr [rax + 0x20], 0xc
004EA555  48 8B 82 78 04 00 00            mov rax, qword ptr [rdx + 0x478]
004EA55C  44 89 80 18 01 00 00            mov dword ptr [rax + 0x118], r8d
004EA563  48 8B 82 78 04 00 00            mov rax, qword ptr [rdx + 0x478]
004EA56A  44 89 80 1C 01 00 00            mov dword ptr [rax + 0x11c], r8d
004EA571  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004EA57A  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
004EA57F  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
004EA586  48 8B 8F 78 04 00 00            mov rcx, qword ptr [rdi + 0x478]
004EA58D  F2 0F 10 82 38 03 00 00         movsd xmm0, qword ptr [rdx + 0x338]
004EA595  F2 0F 11 41 10                  movsd qword ptr [rcx + 0x10], xmm0
004EA59A  8B 82 40 03 00 00               mov eax, dword ptr [rdx + 0x340]
004EA5A0  89 41 18                        mov dword ptr [rcx + 0x18], eax
004EA5A3  0F B7 82 44 03 00 00            movzx eax, word ptr [rdx + 0x344]
004EA5AA  66 89 41 1C                     mov word ptr [rcx + 0x1c], ax
004EA5AE  8A 82 46 03 00 00               mov al, byte ptr [rdx + 0x346]
004EA5B4  8B D3                           mov edx, ebx
004EA5B6  88 41 1E                        mov byte ptr [rcx + 0x1e], al
004EA5B9  48 8B 8F 78 04 00 00            mov rcx, qword ptr [rdi + 0x478]
004EA5C0  48 83 C1 28                     add rcx, 0x28
004EA5C4  E8 17 E0 E0 FF                  call 0x1402f85e0
004EA5C9  44 0F 20 C1                     mov rcx, cr8
004EA5CD  80 F9 02                        cmp cl, 2
004EA5D0  73 20                           jae 0x1404ea5f2
004EA5D2  2B D8                           sub ebx, eax
004EA5D4  8B C8                           mov ecx, eax
004EA5D6  48 8B 87 78 04 00 00            mov rax, qword ptr [rdi + 0x478]
004EA5DD  41 B8 01 00 00 00               mov r8d, 1
004EA5E3  48 83 C0 28                     add rax, 0x28
004EA5E7  8B D3                           mov edx, ebx
004EA5E9  48 8D 0C C8                     lea rcx, [rax + rcx*8]
004EA5ED  E8 EE DF E0 FF                  call 0x1402f85e0
004EA5F2  48 8B CF                        mov rcx, rdi
004EA5F5  E8 E6 6E 2B 00                  call 0x1407a14e0
004EA5FA  45 33 C0                        xor r8d, r8d
004EA5FD  44 38 05 EC D5 97 00            cmp byte ptr [rip + 0x97d5ec], r8b
004EA604  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
004EA608  74 26                           je 0x1404ea630
004EA60A  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
004EA60E  45 8B C5                        mov r8d, r13d
004EA611  48 8B CF                        mov rcx, rdi
004EA614  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
004EA619  E8 B2 36 51 00                  call 0x1409fdcd0
004EA61E  45 33 E4                        xor r12d, r12d
004EA621  8B D8                           mov ebx, eax
004EA623  85 C0                           test eax, eax
004EA625  0F 89 95 00 00 00               jns 0x1404ea6c0
004EA62B  E9 98 01 00 00                  jmp 0x1404ea7c8
004EA630  41 8D 45 01                     lea eax, [r13 + 1]
004EA634  8B C8                           mov ecx, eax
004EA636  48 8D 9F C0 05 00 00            lea rbx, [rdi + 0x5c0]
004EA63D  48 C1 E1 04                     shl rcx, 4
004EA641  4C 8B CB                        mov r9, rbx
004EA644  48 03 CB                        add rcx, rbx
004EA647  48 89 9F 98 00 00 00            mov qword ptr [rdi + 0x98], rbx
004EA64E  89 47 7C                        mov dword ptr [rdi + 0x7c], eax
004EA651  41 8B C5                        mov eax, r13d
004EA654  C1 E0 04                        shl eax, 4
004EA657  44 2B F0                        sub r14d, eax
004EA65A  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
004EA65E  48 8D 44 24 58                  lea rax, [rsp + 0x58]
004EA663  41 83 EE 10                     sub r14d, 0x10
004EA667  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004EA66C  45 8B C6                        mov r8d, r14d
004EA66F  48 8D 45 88                     lea rax, [rbp - 0x78]
004EA673  44 89 74 24 58                  mov dword ptr [rsp + 0x58], r14d
004EA678  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004EA67D  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
004EA682  B9 01 00 00 00                  mov ecx, 1
004EA687  E8 54 E5 4B 00                  call 0x1409a8be0
004EA68C  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
004EA691  48 8D 44 24 58                  lea rax, [rsp + 0x58]
004EA696  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
004EA69A  4C 8D 4B 10                     lea r9, [rbx + 0x10]
004EA69E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004EA6A3  41 8B CD                        mov ecx, r13d
004EA6A6  48 8D 45 88                     lea rax, [rbp - 0x78]
004EA6AA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004EA6AF  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
004EA6B3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004EA6B8  E8 23 E5 4B 00                  call 0x1409a8be0
004EA6BD  45 33 E4                        xor r12d, r12d
004EA6C0  8B 57 7C                        mov edx, dword ptr [rdi + 0x7c]
004EA6C3  4C 8D 87 E8 00 00 00            lea r8, [rdi + 0xe8]
004EA6CA  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
004EA6D1  E8 CA C7 F2 FF                  call 0x140416ea0
004EA6D6  4C 89 A7 A0 00 00 00            mov qword ptr [rdi + 0xa0], r12
004EA6DD  B9 00 01 00 00                  mov ecx, 0x100
004EA6E2  41 8B D7                        mov edx, r15d
004EA6E5  41 B8 53 65 54 64               mov r8d, 0x64546553
004EA6EB  44 89 A7 80 00 00 00            mov dword ptr [rdi + 0x80], r12d
004EA6F2  E8 F9 79 69 00                  call 0x140b820f0
004EA6F7  48 89 87 B0 00 00 00            mov qword ptr [rdi + 0xb0], rax
004EA6FE  48 8B F0                        mov rsi, rax
004EA701  48 85 C0                        test rax, rax
004EA704  75 0A                           jne 0x1404ea710
004EA706  BB 17 00 00 C0                  mov ebx, 0xc0000017
004EA70B  E9 B8 00 00 00                  jmp 0x1404ea7c8
004EA710  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
004EA714  48 89 B7 A8 00 00 00            mov qword ptr [rdi + 0xa8], rsi
004EA71B  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
004EA720  E8 AB FD 4D 00                  call 0x1409ca4d0
004EA725  4D 8B C6                        mov r8, r14
004EA728  48 8B D6                        mov rdx, rsi
004EA72B  8B C8                           mov ecx, eax
004EA72D  8B D8                           mov ebx, eax
004EA72F  E8 1C F3 4B 00                  call 0x1409a9a50
004EA734  8D 43 03                        lea eax, [rbx + 3]
004EA737  B9 FC FF FF FF                  mov ecx, 0xfffffffc
004EA73C  48 23 C1                        and rax, rcx
004EA73F  48 03 F0                        add rsi, rax
004EA742  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
004EA746  48 85 C0                        test rax, rax
004EA749  74 17                           je 0x1404ea762
004EA74B  48 89 B7 B8 00 00 00            mov qword ptr [rdi + 0xb8], rsi
004EA752  48 8B D0                        mov rdx, rax
004EA755  44 0F B7 40 02                  movzx r8d, word ptr [rax + 2]
004EA75A  48 8B CE                        mov rcx, rsi
004EA75D  E8 DE C0 1D 00                  call 0x1406c6840
004EA762  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
004EA766  48 8B CF                        mov rcx, rdi
004EA769  48 8B 75 00                     mov rsi, qword ptr [rbp]
004EA76D  44 8B 8D 80 02 00 00            mov r9d, dword ptr [rbp + 0x280]
004EA774  48 8B D6                        mov rdx, rsi
004EA777  4C 8B 45 F8                     mov r8, qword ptr [rbp - 8]
004EA77B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004EA780  E8 53 39 58 00                  call 0x140a6e0d8
004EA785  8B D8                           mov ebx, eax
004EA787  85 C0                           test eax, eax
004EA789  78 3D                           js 0x1404ea7c8
004EA78B  E8 3C BF 11 00                  call 0x1406066cc
004EA790  85 C0                           test eax, eax
004EA792  74 13                           je 0x1404ea7a7
004EA794  48 8B CE                        mov rcx, rsi
004EA797  E8 AC 69 2B 00                  call 0x1407a1148
004EA79C  84 C0                           test al, al
004EA79E  74 07                           je 0x1404ea7a7
004EA7A0  83 8F 90 04 00 00 02            or dword ptr [rdi + 0x490], 2
004EA7A7  40 8A B5 98 02 00 00            mov sil, byte ptr [rbp + 0x298]
004EA7AE  40 84 F6                        test sil, sil
004EA7B1  74 27                           je 0x1404ea7da
004EA7B3  48 8B 15 6E B0 A1 00            mov rdx, qword ptr [rip + 0xa1b06e]
004EA7BA  48 8B CF                        mov rcx, rdi
004EA7BD  E8 EE D1 4F 00                  call 0x1409e79b0
004EA7C2  8B D8                           mov ebx, eax
004EA7C4  85 C0                           test eax, eax
004EA7C6  79 12                           jns 0x1404ea7da
004EA7C8  48 8B CF                        mov rcx, rdi
004EA7CB  BA 44 66 6C 74                  mov edx, 0x746c6644
004EA7D0  E8 0B D1 E0 FF                  call 0x1402f78e0
004EA7D5  E9 07 FB FF FF                  jmp 0x1404ea2e1
004EA7DA  44 39 25 2F D8 AE 00            cmp dword ptr [rip + 0xaed82f], r12d
004EA7E1  41 BE 01 00 00 00               mov r14d, 1
004EA7E7  74 75                           je 0x1404ea85e
004EA7E9  83 3D B4 D3 97 00 0C            cmp dword ptr [rip + 0x97d3b4], 0xc
004EA7F0  75 6C                           jne 0x1404ea85e
004EA7F2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004EA7FB  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
004EA802  48 8B 05 8F D3 97 00            mov rax, qword ptr [rip + 0x97d38f]
004EA809  48 39 81 D0 01 00 00            cmp qword ptr [rcx + 0x1d0], rax
004EA810  75 47                           jne 0x1404ea859
004EA812  41 8B CE                        mov ecx, r14d
004EA815  F0 0F C1 0D 8B D3 97 00         lock xadd dword ptr [rip + 0x97d38b], ecx
004EA81D  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
004EA822  41 03 CE                        add ecx, r14d
004EA825  48 8B 87 78 04 00 00            mov rax, qword ptr [rdi + 0x478]
004EA82C  89 88 18 01 00 00               mov dword ptr [rax + 0x118], ecx
004EA832  48 8B 87 78 04 00 00            mov rax, qword ptr [rdi + 0x478]
004EA839  8B 90 18 01 00 00               mov edx, dword ptr [rax + 0x118]
004EA83F  3B 15 5B D3 97 00               cmp edx, dword ptr [rip + 0x97d35b]
004EA845  7C 17                           jl 0x1404ea85e
004EA847  4C 8B C7                        mov r8, rdi
004EA84A  48 8D 0D 6F 2E 1E 00            lea rcx, [rip + 0x1e2e6f]
004EA851  E8 5A E4 E6 FF                  call 0x140358cb0
004EA856  CC                              int3
004EA857  EB 05                           jmp 0x1404ea85e
004EA859  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
004EA85E  40 84 F6                        test sil, sil
004EA861  75 74                           jne 0x1404ea8d7
004EA863  4C 8B 0D B6 D7 AE 00            mov r9, qword ptr [rip + 0xaed7b6]
004EA86A  48 8D 95 B0 00 00 00            lea rdx, [rbp + 0xb0]
004EA871  44 8B 45 98                     mov r8d, dword ptr [rbp - 0x68]
004EA875  48 8D 4D 10                     lea rcx, [rbp + 0x10]
004EA879  49 83 C1 4C                     add r9, 0x4c
004EA87D  E8 3E C2 3D 00                  call 0x1408c6ac0
004EA882  8B D8                           mov ebx, eax
004EA884  48 8B CF                        mov rcx, rdi
004EA887  85 C0                           test eax, eax
004EA889  0F 88 3C FF FF FF               js 0x1404ea7cb
004EA88F  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
004EA893  48 8D 55 10                     lea rdx, [rbp + 0x10]
004EA897  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004EA89C  45 8B CE                        mov r9d, r14d
004EA89F  45 33 C0                        xor r8d, r8d
004EA8A2  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
004EA8A7  E8 54 E8 3C 00                  call 0x1408b9100
004EA8AC  48 8D 4D 10                     lea rcx, [rbp + 0x10]
004EA8B0  8B D8                           mov ebx, eax
004EA8B2  E8 B9 B6 3D 00                  call 0x1408c5f70
004EA8B7  85 DB                           test ebx, ebx
004EA8B9  0F 88 22 FA FF FF               js 0x1404ea2e1
004EA8BF  44 38 64 24 51                  cmp byte ptr [rsp + 0x51], r12b
004EA8C4  0F 85 FE FE FF FF               jne 0x1404ea7c8
004EA8CA  48 8B CF                        mov rcx, rdi
004EA8CD  E8 22 BB 3C 00                  call 0x1408b63f4
004EA8D2  E9 F1 FE FF FF                  jmp 0x1404ea7c8
004EA8D7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004EA8E0  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
004EA8E5  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
004EA8EC  4C 39 A1 48 02 00 00            cmp qword ptr [rcx + 0x248], r12
004EA8F3  74 1C                           je 0x1404ea911
004EA8F5  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
004EA8FA  45 33 C9                        xor r9d, r9d
004EA8FD  45 33 C0                        xor r8d, r8d
004EA900  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
004EA905  33 D2                           xor edx, edx
004EA907  48 8B CF                        mov rcx, rdi
004EA90A  E8 F1 E7 3C 00                  call 0x1408b9100
004EA90F  8B D8                           mov ebx, eax
004EA911  85 DB                           test ebx, ebx
004EA913  78 1B                           js 0x1404ea930
004EA915  44 38 64 24 51                  cmp byte ptr [rsp + 0x51], r12b
004EA91A  75 08                           jne 0x1404ea924
004EA91C  48 8B CF                        mov rcx, rdi
004EA91F  E8 D0 BA 3C 00                  call 0x1408b63f4
004EA924  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
004EA928  48 89 38                        mov qword ptr [rax], rdi
004EA92B  E9 B1 F9 FF FF                  jmp 0x1404ea2e1
004EA930  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
004EA934  4C 89 20                        mov qword ptr [rax], r12
004EA937  E9 A5 F9 FF FF                  jmp 0x1404ea2e1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepCreateTokenEx(__int64 a1, int a2, int a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, unsigned int a10, __int64 a11, unsigned int a12, unsigned int a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, unsigned int a21, __int64 a22, __int64 a23, unsigned __int8 a24)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m234;
    unsigned __int64 v_stack_m238;
    unsigned int v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned int v_stack_m264;
    unsigned int v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned int v_stack_m280;
    unsigned int v_stack_m284;
    unsigned __int8 v_stack_m285;
    unsigned __int8 v_stack_m286;
    unsigned __int64 v_stack_m287;
    unsigned __int8 v_stack_m288;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned __int8 v_stack_p51;
    unsigned __int8 v_stack_p52;
    unsigned __int8 v_stack_p53;
    unsigned int v_stack_p54;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (672);
    result = (*(unsigned __int64 *)(v_rip + 9570890)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r14 = 0;
    v_stack_m210 = a7;
    v_stack_m1F8 = a14;
    v_stack_m248 = a16;
    v_stack_m200 = a17;
    v_stack_m1D8 = a19;
    v_stack_m1E0 = a20;
    v_stack_m240 = a3;
    v_stack_m285 = (unsigned __int8)(a2);
    a2 = 0;
    v_stack_m230 = a1;
    v_stack_m1E8 = a22;
    v_stack_m1F0 = a4;
    v_stack_m258 = a9;
    v_stack_m208 = a11;
    v_stack_m270 = a15;
    v_stack_m278 = 0;
    v_stack_m250 = 0;
    v_stack_m284 = 0;
    result = memset(v_stack_m1C8, a2, 160, a4);
    a2 = 0;
    result = memset(v_stack_m128, a2, 224, a4);
    v_stack_m238 = 0;
    v_stack_m288 = 0;
    v_stack_m286 = 0;
    v_stack_m287 = 0;
    v_stack_m260 = 0;
    result = SeCaptureObjectAttributeSecurityDescriptorPresent(a4, (unsigned __int8)((unsigned __int8)(a2)), v_stack_m287, a4);
    if (sign_flag) goto loc_004EA1C1;
    result = 0;
    if ((unsigned int)((unsigned int)(a10)) == 0) goto loc_004E9E62;
loc_004E9E05:
    if (0 >= ((unsigned int)((unsigned int)(a10)))) goto loc_004E9E48;
loc_004E9E0C:
    v_rdi = (0) + (0);
    result = RtlEqualSid(*(unsigned __int64 *)(a9), *(unsigned __int64 *)(a11 + v_rdi * 8), v_stack_m287, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004E9E40;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a11 + v_rdi * 8 + 8)))) & (32)) != 0) goto loc_004E9E40;
    v_r13 = (unsigned int)(((unsigned int)(a10)) - 1);
    result = ((unsigned int)((unsigned int)(v_r13))) + ((unsigned int)((unsigned int)(v_r13)));
    *(unsigned __int64 *)(a11 + v_rdi * 8) = v_xmm0;
    goto loc_004E9E43;
loc_004E9E40:
    v_rsi = (unsigned int)((0) + ((unsigned int)(result + 1)));
loc_004E9E43:
    if (((unsigned int)(v_rsi)) < ((unsigned int)(v_r13))) goto loc_004E9E0C;
loc_004E9E48:
    v_rbx = (unsigned int)((0) + ((unsigned int)(result + 1)));
    result = (0) + (0);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(v_r13))) goto loc_004E9E05;
loc_004E9E62:
    result = RtlEqualSid(v_stack_m248, *(unsigned __int64 *)(v_stack_m258), v_stack_m287, a4);
    v_rsi = ((unsigned __int8)(result) != 0) ? 1 : 0;
    if (v_stack_m270 != 0) goto loc_004E9E85;
    goto loc_004E9EA1;
loc_004E9E85:
    result = RtlEqualSid(v_stack_m270, *(unsigned __int64 *)(v_stack_m258), v_stack_m287, a4);
    v_r15 = 0;
    v_r14 = 0;
    if ((unsigned __int8)(result) != 0) { v_r14 = (unsigned int)(v_r15 + 1); }
loc_004E9EA1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m258 + 8)))) & (16)) == 0) goto loc_004E9EBD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m258 + 8)))) & (6)) != 0) goto loc_004EA0D7;
    v_stack_m284 = (unsigned int)((unsigned int)(0x800ULL));
    goto loc_004E9EC2;
loc_004E9EBD:
loc_004E9EC2:
    v_stack_m268 = 0;
    if ((unsigned int)(v_r13) == 0) goto loc_004EA026;
    v_stack_m268 = 0;
    v_r12 = (a11) + (8);
loc_004E9EDC:
    v_stack_m264 = (unsigned int)((unsigned int)((unsigned int)(v_r15 + 1)));
    v_rbx = (unsigned int)(*(unsigned int *)(v_r12));
    if ((((unsigned __int8)(v_r15 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r12))))) != 0) {
        v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r12))) | (6));
        *(unsigned int *)(v_r12) = (unsigned int)(v_rbx);
    }
    if ((((unsigned __int8)(v_rbx)) & (16)) == 0) goto loc_004E9F0F;
    if ((((unsigned __int8)(v_rbx)) & (6)) != 0) goto loc_004EA0D7;
    v_stack_m284 = (unsigned int)((unsigned int)(v_stack_m284));
loc_004E9F0F:
    result = RtlIdentifierAuthoritySid(*(unsigned __int64 *)(v_r12 - 8), *(unsigned __int64 *)(v_stack_m258), v_stack_m287, (unsigned int)(v_stack_m284));
    result = RtlIdentifierAuthoritySid(*(unsigned __int64 *)(v_rip + 10598645), result, v_stack_m287, (unsigned int)(v_stack_m284));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) != (*(unsigned int *)(result))) goto loc_004E9FAF;
    if (((unsigned __int16)(*(unsigned __int16 *)(result + 4))) != (*(unsigned __int16 *)(result + 4))) goto loc_004E9FAF;
    a1 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 - 8) + 1)) != 0) goto loc_004E9F4D;
    goto loc_004E9F61;
loc_004E9F4D:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_r12 - 8) + *(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 - 8) + 1) - 1 * 4 + 8)) > 0x4000ULL) goto loc_004EA019;
loc_004E9F61:
    if ((((unsigned __int8)(v_rbx)) & (64)) == 0) goto loc_004E9FAF;
    if (v_stack_m280 != -1) goto loc_004EA0D7;
    v_stack_m280 = (unsigned int)((unsigned int)((unsigned int)(v_r15 + 1)));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 - 8) + 1)) != 0) goto loc_004E9F80;
    v_stack_m288 = 0;
    goto loc_004E9F9B;
loc_004E9F80:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 - 8) + 1)))) - 1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_r12 - 8) + a3 * 4 + 8)) >= 0x3000ULL) goto loc_004E9FA2;
    result = 0;
    v_stack_m288 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_r12 - 8) + a3 * 4 + 8)) >= ((unsigned int)((unsigned int)(0x2000ULL)))) goto loc_004E9FA7;
loc_004E9F9B:
    v_stack_m286 = (unsigned __int8)(v_r15 + 1);
    goto loc_004E9FAF;
loc_004E9FA2:
    v_stack_m288 = (unsigned __int8)(v_r15 + 1);
loc_004E9FA7:
    a4 = (unsigned int)(((unsigned int)(v_stack_m284)) | ((unsigned int)((unsigned int)(0x2000ULL))));
    v_stack_m284 = (unsigned int)(a4);
loc_004E9FAF:
    v_r10 = v_r15 + 1;
    if ((unsigned __int8)(v_rsi) == 0) {
        a1 = v_stack_m248;
        a2 = *(unsigned __int64 *)(v_r12 - 8);
        result = RtlEqualSid(a1, a2, a3, a4);
        v_rsi = (unsigned __int8)(v_rsi);
        v_r10 = 1;
        if ((unsigned __int8)(result) != 0) { v_rsi = (unsigned int)(v_r10); }
    }
    if ((unsigned __int8)(v_r14) != 0) goto loc_004EA001;
    result = RtlEqualSid(v_stack_m270, *(unsigned __int64 *)(v_r12 - 8), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004E9FFB;
    if ((((unsigned __int8)(v_rbx)) & (8)) == 0) goto loc_004EA03A;
    v_stack_m268 = (unsigned int)((unsigned int)((unsigned int)(v_r15 + 1)));
    goto loc_004EA001;
loc_004E9FFB:
loc_004EA001:
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r15 + 1))) + (1));
    v_r12 = (v_r12) + (16);
    if (v_stack_m264 >= ((unsigned int)(v_r13))) goto loc_004EA023;
    goto loc_004E9EDC;
loc_004EA019:
    goto loc_004EA1C1;
loc_004EA023:
    v_r15 = 0;
loc_004EA026:
    if ((unsigned __int8)(v_rsi) != 0) goto loc_004EA035;
    goto loc_004EA1C1;
loc_004EA035:
    if (1 != 0) goto loc_004EA044;
loc_004EA03A:
    goto loc_004EA1C1;
loc_004EA044:
    v_stack_m218 = 0;
    v_stack_m228 = 0;
    v_stack_m220 = 0;
    if ((unsigned int)((unsigned int)(a13)) == 0) goto loc_004EA0C0;
    a2 = (v_stack_m1F8) + (8);
loc_004EA070:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) & (0x7FFFFFF8ULL)) != 0) goto loc_004EA0D7;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (3));
    *(unsigned int *)(a2) = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 - 8)))) > 36) goto loc_004EA0EB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 - 8)))) < 36) goto loc_004EA0E1;
    v_stack_m228 = 0;
    if ((((unsigned __int8)(a1)) & (2)) != 0) {
        v_stack_m220 = 0;
    }
    if ((((unsigned __int8)(a1)) & (1)) != 0) {
        v_stack_m218 = 0;
    }
    a4 = (unsigned int)((0) + 1);
    a2 = (a2) + (12);
    if (((unsigned int)(a4)) < ((unsigned int)((unsigned int)(a13)))) goto loc_004EA070;
loc_004EA0C0:
    if (a23 == 0) goto loc_004EA0F5;
    if (((*(unsigned int *)(a23)) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL)))) == 0) goto loc_004EA0F5;
loc_004EA0D7:
    goto loc_004EA1C1;
loc_004EA0E1:
    goto loc_004EA1C1;
loc_004EA0EB:
    goto loc_004EA1C1;
loc_004EA0F5:
    result = ExAllocatePool2(256, 48, (unsigned int)((unsigned int)((unsigned int)(0x74416553ULL))), a4);
    if (result == 0) goto loc_004EA1BC;
    *(unsigned int *)(result) = 0;
    result = (result) + (8);
    *(unsigned int *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int64 *)(result + 32 + 8) = result + 32;
    *(unsigned __int64 *)(result + 32) = result + 32;
    if ((*(unsigned int *)(v_rip + 11460306)) == 0) goto loc_004EA15F;
    result = ExAllocatePool2(256, 256 + 32, (unsigned int)((unsigned int)((unsigned int)(0x74416553ULL))), a4);
    v_stack_m260 = result;
    if (result != 0) goto loc_004EA164;
    goto loc_004EA1B5;
loc_004EA15F:
loc_004EA164:
    result = (*(unsigned __int64 *)(v_rip - 5076067)) + (*(unsigned __int64 *)(v_rip - 5076067));
    v_stack_m238 = (unsigned int)(result);
    result = (result) >> (32);
    v_stack_m234 = (unsigned int)(result);
    result = ExAllocatePool2(104 - 40, 104, (unsigned int)(0x6C546553ULL), a4);
    if (result != 0) goto loc_004EA1EC;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x6C546553ULL), a4);
    if ((*(unsigned int *)(v_rip + 11460192)) == 0) goto loc_004EA1BC;
loc_004EA1B5:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m260, a2, (unsigned int)(0x6C546553ULL), a4);
loc_004EA1BC:
loc_004EA1C1:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x6C546553ULL), a4);
    v_rsp = (v_rsp) + (672);
    return result;
loc_004EA1EC:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) << (4));
    if ((*(unsigned __int8 *)(v_rip + 9951728)) == 0) goto loc_004EA20C;
    v_r14 = (unsigned int)((v_rbx + 23) & (0xFFFFFFF8ULL));
    goto loc_004EA234;
loc_004EA20C:
    v_r12 = (unsigned int)(((unsigned int)(a12)) + (7));
    v_r12 = (unsigned int)((v_r12) & (0xFFFFFFF8ULL));
    result = RtlLengthRequiredSid(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m258) + 1), a2, (unsigned int)(0x6C546553ULL), a4);
    result = (unsigned int)((result) + (3));
    result = (unsigned int)((result) & ((unsigned int)(v_r14)));
    result = (unsigned int)((result) + ((unsigned int)(v_rbx)));
    v_r14 = (unsigned int)((v_r12 + 16) + ((unsigned int)(result)));
loc_004EA234:
    result = RtlLengthRequiredSid(*(unsigned __int8 *)(v_stack_m248 + 1), a2, (unsigned int)(0x6C546553ULL), a4);
    a3 = 0;
    v_r15 = (unsigned int)((result + 3) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    if (v_stack_m200 != 0) {
        a1 = *(unsigned __int16 *)(v_stack_m200 + 2);
        a1 = (unsigned int)((a1) + (3));
        a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
        v_r15 = (unsigned int)((v_r15) + ((unsigned int)(a1)));
    }
    v_stack_p40 = v_stack_p60;
    result = (unsigned int)(0x1000ULL);
    if (((unsigned int)(v_r15)) >= ((unsigned int)((unsigned int)(0x1000ULL)))) { result = (unsigned int)(v_r15); }
    v_stack_p38 = 0;
    v_stack_p74 = (unsigned int)(result);
    result = (unsigned int)((result) + ((unsigned int)(v_r14 + 1472)));
    v_stack_p30 = (unsigned int)(result);
    v_stack_p28 = (unsigned int)(v_r14 + 1472);
    v_stack_p20 = 0;
    result = ObCreateObject(v_stack_p53, *(unsigned __int64 *)(v_rip + 11459992), v_stack_m1F0, 1);
    if (!sign_flag) goto loc_004EA2E8;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m1F0, 1);
    result = 0;
    if ((*(unsigned int *)(v_rip + 11459911)) != 0) {
        a1 = v_stack_p78;
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m1F0, 1);
    }
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m1F0, 1);
loc_004EA2E1:
    goto loc_004EA1C1;
loc_004EA2E8:
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_stack_p60 + 48) = result;
    result = ExInitializeResourceLite2(result, a2, v_stack_m1F0, 1);
    result = (*(unsigned __int64 *)(v_rip - 5076475)) + (*(unsigned __int64 *)(v_rip - 5076475));
    *(unsigned int *)(v_stack_p60 + 16) = (unsigned int)(result);
    a2 = 0;
    result = (result) >> (32);
    *(unsigned int *)(v_stack_p60 + 20) = (unsigned int)(result);
    v_rbx = 0;
    *(unsigned __int64 *)(v_stack_p60 + 32) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 224) = 0;
    v_stack_p68 = 0;
    v_stack_p68 = 0;
    *(unsigned __int64 *)(v_stack_p60 + 24) = *(unsigned __int64 *)(v_stack_m210);
    *(unsigned __int8 *)(v_stack_p60 + 204) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 56) = v_stack_m238;
    *(unsigned __int64 *)(v_stack_p60 + 40) = *(unsigned __int64 *)(a8);
    *(unsigned int *)(v_stack_p60 + 192) = (unsigned int)((unsigned int)(a5));
    *(unsigned int *)(v_stack_p60 + 196) = (unsigned int)((unsigned int)(a6));
    *(unsigned __int64 *)(v_stack_p60) = v_xmm0;
    *(unsigned int *)(v_stack_p60 + 200) = (unsigned int)((unsigned int)(v_stack_p54));
    *(unsigned int *)(v_stack_p60 + 120) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 1160) = 0;
    *(unsigned int *)(v_stack_p60 + 136) = (unsigned int)((unsigned int)(v_stack_p74));
    *(unsigned int *)(v_stack_p60 + 140) = 0;
    *(unsigned int *)(v_stack_p60 + 144) = (unsigned int)((unsigned int)(v_stack_p70));
    *(unsigned __int64 *)(v_stack_p60 + 184) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 1120) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 1128) = 0;
    *(unsigned int *)(v_stack_p60 + 132) = (unsigned int)(v_r14);
    *(unsigned int *)(v_stack_p60 + 208) = (unsigned int)((unsigned int)(v_stack_p58));
    *(unsigned int *)(v_stack_p60 + 212) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 64) = v_stack_m228;
    *(unsigned __int64 *)(v_stack_p60 + 72) = v_stack_m220;
    *(unsigned __int64 *)(v_stack_p60 + 80) = v_stack_m218;
    *(unsigned int *)(v_stack_p60 + 800) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 792) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 784) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 1080) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 1088) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 1152) = 0;
    result = memset(v_stack_p60 + 808, a2, 272, 1);
    *(unsigned __int64 *)(v_stack_p60 + 1104) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 1112) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 1136) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 1144) = v_stack_p78;
    result = a23;
    if (a23 != 0) {
        result = *(unsigned int *)(a23);
        *(unsigned int *)(v_stack_p60 + 212) = (unsigned int)(result);
    }
    if (v_stack_p50 == 0) {
    }
    if (v_stack_p52 == 1) {
    }
    *(unsigned __int64 *)(v_stack_p60 + 88) = v_xmm0;
    *(unsigned __int64 *)(v_stack_p60 + 104) = v_xmm0;
    *(unsigned __int64 *)(v_stack_p60 + 776) = result;
    *(unsigned __int64 *)(v_stack_p60 + 1096) = 0;
    *(unsigned __int64 *)(v_stack_p60 + 176) = 0;
    result = SepReferenceLogonSession(v_stack_m210, v_stack_p60 + 216, 272, 1);
    a3 = 0;
    if (!sign_flag) goto loc_004EA4F6;
    *(unsigned __int64 *)(v_stack_p60 + 216) = 0;
    result = ObfDereferenceObjectWithTag(v_stack_p60, (unsigned int)(0x746C6644ULL), a3, 1);
    goto loc_004EA1C1;
loc_004EA4F6:
    if ((*(unsigned int *)(v_rip + 11459347)) == 0) goto loc_004EA5FD;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p60 + 1144)) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1288);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1296);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 32) = 12;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 280) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 284) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 16) = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 832)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 28) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 836));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 30) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 838));
    a1 = (*(unsigned __int64 *)(v_stack_p60 + 1144)) + (40);
    result = RtlWalkFrameChain(a1, 30, a3, 1);
    v_rbx = 30;
    if (((unsigned __int8)(v_cr8)) < 2) {
        v_rbx = (unsigned int)((30) - ((unsigned int)(result)));
        a1 = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_stack_p60 + 1144);
        a3 = 1;
        result = (result) + (40);
        a2 = (unsigned int)(v_rbx);
        a1 = result + a1 * 8;
        result = RtlWalkFrameChain(a1, a2, a3, 1);
    }
    result = SepAddTokenLogonSession(v_stack_p60, a2, a3, 1);
    a3 = 0;
loc_004EA5FD:
    if ((*(unsigned __int8 *)(v_rip + 9950700)) == 0) goto loc_004EA630;
    v_stack_p20 = (unsigned int)(v_r12);
    result = SepSetTokenUserAndGroups(v_stack_p60, v_stack_m258, (unsigned int)((unsigned int)(v_r13)), v_stack_m208);
    v_r12 = 0;
    if (!sign_flag) goto loc_004EA6C0;
    goto loc_004EA7C8;
loc_004EA630:
    a1 = ((unsigned int)((unsigned int)(v_r13 + 1))) << (4);
    a1 = (a1) + (v_stack_p60 + 1472);
    *(unsigned __int64 *)(v_stack_p60 + 152) = v_stack_p60 + 1472;
    *(unsigned int *)(v_stack_p60 + 124) = (unsigned int)(v_r13 + 1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) << (4));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result)));
    v_stack_m250 = a1;
    v_r14 = (unsigned int)((v_r14) - (16));
    v_stack_p30 = v_stack_p58;
    v_stack_p58 = (unsigned int)(v_r14);
    v_stack_p28 = v_stack_m250;
    v_stack_p20 = a1;
    result = RtlCopySidAndAttributesArray(1, v_stack_m258, (unsigned int)((unsigned int)(v_r14)), v_stack_p60 + 1472);
    v_stack_p30 = v_stack_p58;
    v_stack_p28 = v_stack_m250;
    v_stack_p20 = v_stack_m250;
    result = RtlCopySidAndAttributesArray((unsigned int)((unsigned int)(v_r13)), v_stack_m208, (unsigned int)(v_stack_p58), v_stack_p60 + 1472 + 16);
    v_r12 = 0;
loc_004EA6C0:
    result = RtlSidHashInitialize(*(unsigned __int64 *)(v_stack_p60 + 152), (unsigned int)(*(unsigned int *)(v_stack_p60 + 124)), v_stack_p60 + 232, v_stack_p60 + 1472 + 16);
    *(unsigned __int64 *)(v_stack_p60 + 160) = 0;
    *(unsigned int *)(v_stack_p60 + 128) = 0;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x64546553ULL), v_stack_p60 + 1472 + 16);
    *(unsigned __int64 *)(v_stack_p60 + 176) = result;
    if (result != 0) goto loc_004EA710;
    goto loc_004EA7C8;
loc_004EA710:
    *(unsigned __int64 *)(v_stack_p60 + 168) = result;
    result = RtlLengthRequiredSid(*(unsigned __int8 *)(v_stack_m248 + 1), (unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x64546553ULL), v_stack_p60 + 1472 + 16);
    result = RtlCopySid((unsigned int)((unsigned int)(result)), result, v_stack_m248, v_stack_p60 + 1472 + 16);
    result = ((unsigned int)((unsigned int)(result)) + 3) & ((unsigned int)(0xFFFFFFFCULL));
    v_rsi = (result) + (result);
    result = v_stack_m200;
    if (v_stack_m200 != 0) {
        *(unsigned __int64 *)(v_stack_p60 + 184) = v_rsi;
        a2 = v_stack_m200;
        a3 = *(unsigned __int16 *)(v_stack_m200 + 2);
        a1 = v_rsi;
        result = memcpy(a1, a2, a3, v_stack_p60 + 1472 + 16);
    }
    v_stack_p20 = v_stack_m1E8;
    result = SepSetTokenClaims(v_stack_p60, v_stack_m1D8, v_stack_m1E0, (unsigned int)(a21));
    if (sign_flag) goto loc_004EA7C8;
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(v_stack_p60, v_stack_m1D8, v_stack_m1E0, (unsigned int)(a21));
    if ((unsigned int)(result) == 0) goto loc_004EA7A7;
    result = SepUserClaimsContainAgentId(v_stack_m1D8, v_stack_m1D8, v_stack_m1E0, (unsigned int)(a21));
    if ((unsigned __int8)(result) != 0) {
    }
    if (a24 == 0) goto loc_004EA7DA;
    result = SepSetTokenTrust(v_stack_p60, *(unsigned __int64 *)(v_rip + 10596462), v_stack_m1E0, (unsigned int)(a21));
    if (!sign_flag) goto loc_004EA7DA;
loc_004EA7C8:
loc_004EA7CB:
    result = ObfDereferenceObjectWithTag(v_stack_p60, (unsigned int)(0x746C6644ULL), v_stack_m1E0, (unsigned int)(a21));
    goto loc_004EA2E1;
loc_004EA7DA:
    if ((*(unsigned int *)(v_rip + 11458607)) == 0) goto loc_004EA85E;
    if ((*(unsigned int *)(v_rip + 9950132)) != 12) goto loc_004EA85E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464)) != (*(unsigned __int64 *)(v_rip + 9950095))) goto loc_004EA859;
    a1 = (unsigned int)((1) + (1));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 280) = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 280)))) < (*(unsigned int *)(v_rip + 9950043))) goto loc_004EA85E;
    result = DbgPrint(v_rip + 1977967, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p60 + 1144) + 280)), v_stack_p60, (unsigned int)(a21));
    goto loc_004EA85E;
loc_004EA859:
loc_004EA85E:
    if (a24 != 0) goto loc_004EA8D7;
    a4 = (*(unsigned __int64 *)(v_rip + 11458486)) + (76);
    result = SeCreateAccessState(v_stack_m1C8, v_stack_m128, (unsigned int)(v_stack_m240), a4);
    if (sign_flag) goto loc_004EA7CB;
    v_stack_p28 = v_stack_m230;
    a3 = 0;
    v_stack_p20 = 0;
    result = ObInsertObject(v_stack_p60, v_stack_m1C8, a3, 1);
    result = SeDeleteAccessState(v_stack_m1C8, v_stack_m1C8, a3, 1);
    if (sign_flag) goto loc_004EA2E1;
    if (v_stack_p51 != 0) goto loc_004EA7C8;
    result = SepFinalizeTokenAcls(v_stack_p60, v_stack_m1C8, a3, 1);
    goto loc_004EA7C8;
loc_004EA8D7:
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_rbx = (unsigned int)((unsigned int)(result));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 584)) != 0) {
        v_stack_p28 = 0;
        a4 = 0;
        a3 = 0;
        v_stack_p20 = 0;
        a2 = 0;
        a1 = v_stack_p60;
        result = ObInsertObject(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (sign_flag) goto loc_004EA930;
    if (v_stack_p51 == 0) {
        a1 = v_stack_p60;
        result = SepFinalizeTokenAcls(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_stack_m230) = v_stack_p60;
    goto loc_004EA2E1;
loc_004EA930:
    *(unsigned __int64 *)(v_stack_m230) = 0;
    goto loc_004EA2E1;
}
```

## 5. (Beta) C Style

```c
int64_t SepCreateTokenEx(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7, void *Arg8, void *Arg9, uint32_t Arg10, void *Arg11, void *Arg12, uint32_t Arg13, int64_t Arg14, int64_t Arg15, int64_t Arg16, int64_t Arg17, void *Arg18, int64_t Arg19, int64_t Arg20, uint32_t Arg21, int64_t Arg22, int64_t Arg23, uint8_t Arg24)
{
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg11 = (uint8_t *)Arg11;
    uint8_t *arg12 = (uint8_t *)Arg12;
    uint8_t *arg18 = (uint8_t *)Arg18;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m128;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m234;
    uint64_t v_stack_m238;
    uint32_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint32_t v_stack_m264;
    uint32_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint32_t v_stack_m280;
    uint32_t v_stack_m284;
    uint8_t v_stack_m285;
    uint8_t v_stack_m286;
    uint64_t v_stack_m287;
    uint8_t v_stack_m288;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p50;
    uint8_t v_stack_p51;
    uint8_t v_stack_p52;
    uint8_t v_stack_p53;
    uint32_t v_stack_p54;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (672);
    result = (*(uint64_t *)(v_rip + 0x920A4A)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r14 = 0;
    v_stack_m210 = Arg7;
    v_stack_m1F8 = Arg14;
    v_stack_m248 = Arg16;
    v_stack_m200 = Arg17;
    v_stack_m1D8 = Arg19;
    v_stack_m1E0 = Arg20;
    v_stack_m240 = Arg3;
    v_stack_m285 = (uint8_t)(Arg2);
    Arg2 = 0;
    v_stack_m230 = Arg1;
    v_stack_m1E8 = Arg22;
    v_stack_m1F0 = Arg4;
    v_stack_m258 = Arg9;
    v_stack_m208 = Arg11;
    v_stack_m270 = Arg15;
    v_stack_m278 = 0;
    v_stack_m250 = 0;
    v_stack_m284 = 0;
    result = memset(v_stack_m1C8, Arg2, 160, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m128, Arg2, 224, Arg4);
    v_stack_m238 = 0;
    v_stack_m288 = 0;
    v_stack_m286 = 0;
    v_stack_m287 = 0;
    v_stack_m260 = 0;
    result = SeCaptureObjectAttributeSecurityDescriptorPresent(Arg4, (uint8_t)((uint8_t)(Arg2)), v_stack_m287, Arg4);
    if (sign_flag) goto loc_004EA1C1;
    result = 0;
    if ((uint32_t)((uint32_t)(Arg10)) == 0) goto loc_004E9E62;
loc_004E9E05:
    if (0 >= ((uint32_t)((uint32_t)(Arg10)))) goto loc_004E9E48;
loc_004E9E0C:
    local_rdi = (0) + (0);
    result = RtlEqualSid(*(uint64_t *)(arg9), *(uint64_t *)(arg11 + local_rdi * 8), v_stack_m287, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004E9E40;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg11 + local_rdi * 8 + 0x8)))) & (32)) != 0) goto loc_004E9E40;
    local_r13 = (uint32_t)(((uint32_t)(Arg10)) - 1);
    result = ((uint32_t)((uint32_t)(local_r13))) + ((uint32_t)((uint32_t)(local_r13)));
    *(uint64_t *)(arg11 + local_rdi * 8) = v_xmm0;
    goto loc_004E9E43;
loc_004E9E40:
    local_rsi = (uint32_t)((0) + ((uint32_t)(result + 1)));
loc_004E9E43:
    if (((uint32_t)(local_rsi)) < ((uint32_t)(local_r13))) goto loc_004E9E0C;
loc_004E9E48:
    local_rbx = (uint32_t)((0) + ((uint32_t)(result + 1)));
    result = (0) + (0);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(local_r13))) goto loc_004E9E05;
loc_004E9E62:
    result = RtlEqualSid(v_stack_m248, *(uint64_t *)(v_stack_m258), v_stack_m287, Arg4);
    local_rsi = ((uint8_t)(result) != 0) ? 1 : 0;
    if (v_stack_m270 != 0) goto loc_004E9E85;
    goto loc_004E9EA1;
loc_004E9E85:
    result = RtlEqualSid(v_stack_m270, *(uint64_t *)(v_stack_m258), v_stack_m287, Arg4);
    local_r15 = 0;
    local_r14 = 0;
    if ((uint8_t)(result) != 0) { local_r14 = (uint32_t)(local_r15 + 1); }
loc_004E9EA1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)))) & (16)) == 0) goto loc_004E9EBD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)))) & (6)) != 0) goto loc_004EA0D7;
    v_stack_m284 = (uint32_t)((uint32_t)(0x800ULL));
    goto loc_004E9EC2;
loc_004E9EBD:
loc_004E9EC2:
    v_stack_m268 = 0;
    if ((uint32_t)(local_r13) == 0) goto loc_004EA026;
    v_stack_m268 = 0;
    local_r12 = (Arg11) + (8);
loc_004E9EDC:
    v_stack_m264 = (uint32_t)((uint32_t)((uint32_t)(local_r15 + 1)));
    local_rbx = (uint32_t)(*(uint32_t *)(local_r12));
    if ((((uint8_t)(local_r15 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_r12))))) != 0) {
        local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r12))) | (6));
        *(uint32_t *)(local_r12) = (uint32_t)(local_rbx);
    }
    if ((((uint8_t)(local_rbx)) & (16)) == 0) goto loc_004E9F0F;
    if ((((uint8_t)(local_rbx)) & (6)) != 0) goto loc_004EA0D7;
    v_stack_m284 = (uint32_t)((uint32_t)(v_stack_m284));
loc_004E9F0F:
    result = RtlIdentifierAuthoritySid(*(uint64_t *)(local_r12 - 0x8), *(uint64_t *)(v_stack_m258), v_stack_m287, (uint32_t)(v_stack_m284));
    result = RtlIdentifierAuthoritySid(*(uint64_t *)(v_rip + 0xA1B8F5), result, v_stack_m287, (uint32_t)(v_stack_m284));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) != (*(uint32_t *)(result))) goto loc_004E9FAF;
    if (((uint16_t)(*(uint16_t *)(result + 0x4))) != (*(uint16_t *)(result + 0x4))) goto loc_004E9FAF;
    Arg1 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_r12 - 0x8) + 0x1)) != 0) goto loc_004E9F4D;
    goto loc_004E9F61;
loc_004E9F4D:
    if ((*(uint32_t *)(*(uint64_t *)(local_r12 - 0x8) + *(uint8_t *)(*(uint64_t *)(local_r12 - 0x8) + 0x1) - 0x1 * 4 + 0x8)) > 0x4000ULL) goto loc_004EA019;
loc_004E9F61:
    if ((((uint8_t)(local_rbx)) & (64)) == 0) goto loc_004E9FAF;
    if (v_stack_m280 != -1) goto loc_004EA0D7;
    v_stack_m280 = (uint32_t)((uint32_t)((uint32_t)(local_r15 + 1)));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_r12 - 0x8) + 0x1)) != 0) goto loc_004E9F80;
    v_stack_m288 = 0;
    goto loc_004E9F9B;
loc_004E9F80:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_r12 - 0x8) + 0x1)))) - 1);
    if ((*(uint32_t *)(*(uint64_t *)(local_r12 - 0x8) + Arg3 * 4 + 0x8)) >= 0x3000ULL) goto loc_004E9FA2;
    result = 0;
    v_stack_m288 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(local_r12 - 0x8) + Arg3 * 4 + 0x8)) >= ((uint32_t)((uint32_t)(0x2000ULL)))) goto loc_004E9FA7;
loc_004E9F9B:
    v_stack_m286 = (uint8_t)(local_r15 + 1);
    goto loc_004E9FAF;
loc_004E9FA2:
    v_stack_m288 = (uint8_t)(local_r15 + 1);
loc_004E9FA7:
    Arg4 = (uint32_t)(((uint32_t)(v_stack_m284)) | ((uint32_t)((uint32_t)(0x2000ULL))));
    v_stack_m284 = (uint32_t)(Arg4);
loc_004E9FAF:
    local_r10 = local_r15 + 1;
    if ((uint8_t)(local_rsi) == 0) {
        Arg1 = v_stack_m248;
        Arg2 = *(uint64_t *)(local_r12 - 0x8);
        result = RtlEqualSid(Arg1, Arg2, Arg3, Arg4);
        local_rsi = (uint8_t)(local_rsi);
        local_r10 = 1;
        if ((uint8_t)(result) != 0) { local_rsi = (uint32_t)(local_r10); }
    }
    if ((uint8_t)(local_r14) != 0) goto loc_004EA001;
    result = RtlEqualSid(v_stack_m270, *(uint64_t *)(local_r12 - 0x8), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004E9FFB;
    if ((((uint8_t)(local_rbx)) & (8)) == 0) goto loc_004EA03A;
    v_stack_m268 = (uint32_t)((uint32_t)((uint32_t)(local_r15 + 1)));
    goto loc_004EA001;
loc_004E9FFB:
loc_004EA001:
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r15 + 1))) + (1));
    local_r12 = (local_r12) + (16);
    if (v_stack_m264 >= ((uint32_t)(local_r13))) goto loc_004EA023;
    goto loc_004E9EDC;
loc_004EA019:
    goto loc_004EA1C1;
loc_004EA023:
    local_r15 = 0;
loc_004EA026:
    if ((uint8_t)(local_rsi) != 0) goto loc_004EA035;
    goto loc_004EA1C1;
loc_004EA035:
    if (1 != 0) goto loc_004EA044;
loc_004EA03A:
    goto loc_004EA1C1;
loc_004EA044:
    v_stack_m218 = 0;
    v_stack_m228 = 0;
    v_stack_m220 = 0;
    if ((uint32_t)((uint32_t)(Arg13)) == 0) goto loc_004EA0C0;
    Arg2 = (v_stack_m1F8) + (8);
loc_004EA070:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))) & (0x7FFFFFF8ULL)) != 0) goto loc_004EA0D7;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) & (3));
    *(uint32_t *)(Arg2) = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 - 0x8)))) > 36) goto loc_004EA0EB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 - 0x8)))) < 36) goto loc_004EA0E1;
    v_stack_m228 = 0;
    if ((((uint8_t)(Arg1)) & (2)) != 0) {
        v_stack_m220 = 0;
    }
    if ((((uint8_t)(Arg1)) & (1)) != 0) {
        v_stack_m218 = 0;
    }
    Arg4 = (uint32_t)((0) + 1);
    Arg2 = (Arg2) + (12);
    if (((uint32_t)(Arg4)) < ((uint32_t)((uint32_t)(Arg13)))) goto loc_004EA070;
loc_004EA0C0:
    if (Arg23 == 0) goto loc_004EA0F5;
    if (((*(uint32_t *)(Arg23)) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL)))) == 0) goto loc_004EA0F5;
loc_004EA0D7:
    goto loc_004EA1C1;
loc_004EA0E1:
    goto loc_004EA1C1;
loc_004EA0EB:
    goto loc_004EA1C1;
loc_004EA0F5:
    result = ExAllocatePool2(256, 48, (uint32_t)((uint32_t)((uint32_t)(0x74416553ULL))), Arg4);
    if (result == 0) goto loc_004EA1BC;
    *(uint32_t *)(result) = 0;
    result = (result) + (8);
    *(uint32_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    *(uint64_t *)(result + 0x20 + 0x8) = result + 32;
    *(uint64_t *)(result + 0x20) = result + 32;
    if ((*(uint32_t *)(v_rip + 0xAEDED2)) == 0) goto loc_004EA15F;
    result = ExAllocatePool2(256, 256 + 32, (uint32_t)((uint32_t)((uint32_t)(0x74416553ULL))), Arg4);
    v_stack_m260 = result;
    if (result != 0) goto loc_004EA164;
    goto loc_004EA1B5;
loc_004EA15F:
loc_004EA164:
    result = (*(uint64_t *)(v_rip - 0x4D7463)) + (*(uint64_t *)(v_rip - 0x4D7463));
    v_stack_m238 = (uint32_t)(result);
    result = (result) >> (32);
    v_stack_m234 = (uint32_t)(result);
    result = ExAllocatePool2(104 - 40, 104, (uint32_t)(0x6C546553ULL), Arg4);
    if (result != 0) goto loc_004EA1EC;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x6C546553ULL), Arg4);
    if ((*(uint32_t *)(v_rip + 0xAEDE60)) == 0) goto loc_004EA1BC;
loc_004EA1B5:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m260, Arg2, (uint32_t)(0x6C546553ULL), Arg4);
loc_004EA1BC:
loc_004EA1C1:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x6C546553ULL), Arg4);
    local_rsp = (local_rsp) + (672);
    return result;
loc_004EA1EC:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) << (4));
    if ((*(uint8_t *)(v_rip + 0x97D9F0)) == 0) goto loc_004EA20C;
    local_r14 = (uint32_t)((local_rbx + 23) & (0xFFFFFFF8ULL));
    goto loc_004EA234;
loc_004EA20C:
    local_r12 = (uint32_t)(((uint32_t)(Arg12)) + (7));
    local_r12 = (uint32_t)((local_r12) & (0xFFFFFFF8ULL));
    result = RtlLengthRequiredSid(*(uint8_t *)(*(uint64_t *)(v_stack_m258) + 0x1), Arg2, (uint32_t)(0x6C546553ULL), Arg4);
    result = (uint32_t)((result) + (3));
    result = (uint32_t)((result) & ((uint32_t)(local_r14)));
    result = (uint32_t)((result) + ((uint32_t)(local_rbx)));
    local_r14 = (uint32_t)((local_r12 + 16) + ((uint32_t)(result)));
loc_004EA234:
    result = RtlLengthRequiredSid(*(uint8_t *)(v_stack_m248 + 0x1), Arg2, (uint32_t)(0x6C546553ULL), Arg4);
    Arg3 = 0;
    local_r15 = (uint32_t)((result + 3) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    if (v_stack_m200 != 0) {
        Arg1 = *(uint16_t *)(v_stack_m200 + 0x2);
        Arg1 = (uint32_t)((Arg1) + (3));
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
        local_r15 = (uint32_t)((local_r15) + ((uint32_t)(Arg1)));
    }
    v_stack_p40 = v_stack_p60;
    result = (uint32_t)(0x1000ULL);
    if (((uint32_t)(local_r15)) >= ((uint32_t)((uint32_t)(0x1000ULL)))) { result = (uint32_t)(local_r15); }
    v_stack_p38 = 0;
    v_stack_p74 = (uint32_t)(result);
    result = (uint32_t)((result) + ((uint32_t)(local_r14 + 1472)));
    v_stack_p30 = (uint32_t)(result);
    v_stack_p28 = (uint32_t)(local_r14 + 1472);
    v_stack_p20 = 0;
    result = ObCreateObject(v_stack_p53, *(uint64_t *)(v_rip + 0xAEDD98), v_stack_m1F0, 1);
    if (!sign_flag) goto loc_004EA2E8;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m1F0, 1);
    result = 0;
    if ((*(uint32_t *)(v_rip + 0xAEDD47)) != 0) {
        Arg1 = v_stack_p78;
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m1F0, 1);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m1F0, 1);
loc_004EA2E1:
    goto loc_004EA1C1;
loc_004EA2E8:
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    *(uint64_t *)(v_stack_p60 + 0x30) = result;
    result = ExInitializeResourceLite2(result, Arg2, v_stack_m1F0, 1);
    result = (*(uint64_t *)(v_rip - 0x4D75FB)) + (*(uint64_t *)(v_rip - 0x4D75FB));
    *(uint32_t *)(v_stack_p60 + 0x10) = (uint32_t)(result);
    Arg2 = 0;
    result = (result) >> (32);
    *(uint32_t *)(v_stack_p60 + 0x14) = (uint32_t)(result);
    local_rbx = 0;
    *(uint64_t *)(v_stack_p60 + 0x20) = 0;
    *(uint64_t *)(v_stack_p60 + 0xE0) = 0;
    v_stack_p68 = 0;
    v_stack_p68 = 0;
    *(uint64_t *)(v_stack_p60 + 0x18) = *(uint64_t *)(v_stack_m210);
    *(uint8_t *)(v_stack_p60 + 0xCC) = 0;
    *(uint64_t *)(v_stack_p60 + 0x38) = v_stack_m238;
    *(uint64_t *)(v_stack_p60 + 0x28) = *(uint64_t *)(arg8);
    *(uint32_t *)(v_stack_p60 + 0xC0) = (uint32_t)((uint32_t)(Arg5));
    *(uint32_t *)(v_stack_p60 + 0xC4) = (uint32_t)((uint32_t)(Arg6));
    *(uint64_t *)(v_stack_p60) = v_xmm0;
    *(uint32_t *)(v_stack_p60 + 0xC8) = (uint32_t)((uint32_t)(v_stack_p54));
    *(uint32_t *)(v_stack_p60 + 0x78) = 0;
    *(uint64_t *)(v_stack_p60 + 0x488) = 0;
    *(uint32_t *)(v_stack_p60 + 0x88) = (uint32_t)((uint32_t)(v_stack_p74));
    *(uint32_t *)(v_stack_p60 + 0x8C) = 0;
    *(uint32_t *)(v_stack_p60 + 0x90) = (uint32_t)((uint32_t)(v_stack_p70));
    *(uint64_t *)(v_stack_p60 + 0xB8) = 0;
    *(uint64_t *)(v_stack_p60 + 0x460) = 0;
    *(uint64_t *)(v_stack_p60 + 0x468) = 0;
    *(uint32_t *)(v_stack_p60 + 0x84) = (uint32_t)(local_r14);
    *(uint32_t *)(v_stack_p60 + 0xD0) = (uint32_t)((uint32_t)(v_stack_p58));
    *(uint32_t *)(v_stack_p60 + 0xD4) = 0;
    *(uint64_t *)(v_stack_p60 + 0x40) = v_stack_m228;
    *(uint64_t *)(v_stack_p60 + 0x48) = v_stack_m220;
    *(uint64_t *)(v_stack_p60 + 0x50) = v_stack_m218;
    *(uint32_t *)(v_stack_p60 + 0x320) = 0;
    *(uint64_t *)(v_stack_p60 + 0x318) = 0;
    *(uint64_t *)(v_stack_p60 + 0x310) = 0;
    *(uint64_t *)(v_stack_p60 + 0x438) = 0;
    *(uint64_t *)(v_stack_p60 + 0x440) = 0;
    *(uint64_t *)(v_stack_p60 + 0x480) = 0;
    result = memset(v_stack_p60 + 808, Arg2, 272, 1);
    *(uint64_t *)(v_stack_p60 + 0x450) = 0;
    *(uint64_t *)(v_stack_p60 + 0x458) = 0;
    *(uint64_t *)(v_stack_p60 + 0x470) = 0;
    *(uint64_t *)(v_stack_p60 + 0x478) = v_stack_p78;
    result = Arg23;
    if (Arg23 != 0) {
        result = *(uint32_t *)(Arg23);
        *(uint32_t *)(v_stack_p60 + 0xD4) = (uint32_t)(result);
    }
    if (v_stack_p50 == 0) {
    }
    if (v_stack_p52 == 1) {
    }
    *(uint64_t *)(v_stack_p60 + 0x58) = v_xmm0;
    *(uint64_t *)(v_stack_p60 + 0x68) = v_xmm0;
    *(uint64_t *)(v_stack_p60 + 0x308) = result;
    *(uint64_t *)(v_stack_p60 + 0x448) = 0;
    *(uint64_t *)(v_stack_p60 + 0xB0) = 0;
    result = SepReferenceLogonSession(v_stack_m210, v_stack_p60 + 216, 272, 1);
    Arg3 = 0;
    if (!sign_flag) goto loc_004EA4F6;
    *(uint64_t *)(v_stack_p60 + 0xD8) = 0;
    result = ObfDereferenceObjectWithTag(v_stack_p60, (uint32_t)(0x746C6644ULL), Arg3, 1);
    goto loc_004EA1C1;
loc_004EA4F6:
    if ((*(uint32_t *)(v_rip + 0xAEDB13)) == 0) goto loc_004EA5FD;
    *(uint64_t *)(*(uint64_t *)(v_stack_p60 + 0x478)) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x508);
    *(uint64_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x8) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x510);
    *(uint32_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x20) = 12;
    *(uint32_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x118) = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x11C) = 0;
    *(uint64_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x10) = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x340)));
    *(uint16_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x1C) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x344));
    *(uint8_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x1E) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x346));
    Arg1 = (*(uint64_t *)(v_stack_p60 + 0x478)) + (40);
    result = RtlWalkFrameChain(Arg1, 30, Arg3, 1);
    local_rbx = 30;
    if (((uint8_t)(v_cr8)) < 2) {
        local_rbx = (uint32_t)((30) - ((uint32_t)(result)));
        Arg1 = (uint32_t)(result);
        result = *(uint64_t *)(v_stack_p60 + 0x478);
        Arg3 = 1;
        result = (result) + (40);
        Arg2 = (uint32_t)(local_rbx);
        Arg1 = result + Arg1 * 8;
        result = RtlWalkFrameChain(Arg1, Arg2, Arg3, 1);
    }
    result = SepAddTokenLogonSession(v_stack_p60, Arg2, Arg3, 1);
    Arg3 = 0;
loc_004EA5FD:
    if ((*(uint8_t *)(v_rip + 0x97D5EC)) == 0) goto loc_004EA630;
    v_stack_p20 = (uint32_t)(local_r12);
    result = SepSetTokenUserAndGroups(v_stack_p60, v_stack_m258, (uint32_t)((uint32_t)(local_r13)), v_stack_m208);
    local_r12 = 0;
    if (!sign_flag) goto loc_004EA6C0;
    goto loc_004EA7C8;
loc_004EA630:
    Arg1 = ((uint32_t)((uint32_t)(local_r13 + 1))) << (4);
    Arg1 = (Arg1) + (v_stack_p60 + 1472);
    *(uint64_t *)(v_stack_p60 + 0x98) = v_stack_p60 + 1472;
    *(uint32_t *)(v_stack_p60 + 0x7C) = (uint32_t)(local_r13 + 1);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) << (4));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result)));
    v_stack_m250 = Arg1;
    local_r14 = (uint32_t)((local_r14) - (16));
    v_stack_p30 = v_stack_p58;
    v_stack_p58 = (uint32_t)(local_r14);
    v_stack_p28 = v_stack_m250;
    v_stack_p20 = Arg1;
    result = RtlCopySidAndAttributesArray(1, v_stack_m258, (uint32_t)((uint32_t)(local_r14)), v_stack_p60 + 1472);
    v_stack_p30 = v_stack_p58;
    v_stack_p28 = v_stack_m250;
    v_stack_p20 = v_stack_m250;
    result = RtlCopySidAndAttributesArray((uint32_t)((uint32_t)(local_r13)), v_stack_m208, (uint32_t)(v_stack_p58), v_stack_p60 + 1472 + 16);
    local_r12 = 0;
loc_004EA6C0:
    result = RtlSidHashInitialize(*(uint64_t *)(v_stack_p60 + 0x98), (uint32_t)(*(uint32_t *)(v_stack_p60 + 0x7C)), v_stack_p60 + 232, v_stack_p60 + 1472 + 16);
    *(uint64_t *)(v_stack_p60 + 0xA0) = 0;
    *(uint32_t *)(v_stack_p60 + 0x80) = 0;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x64546553ULL), v_stack_p60 + 1472 + 16);
    *(uint64_t *)(v_stack_p60 + 0xB0) = result;
    if (result != 0) goto loc_004EA710;
    goto loc_004EA7C8;
loc_004EA710:
    *(uint64_t *)(v_stack_p60 + 0xA8) = result;
    result = RtlLengthRequiredSid(*(uint8_t *)(v_stack_m248 + 0x1), (uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x64546553ULL), v_stack_p60 + 1472 + 16);
    result = RtlCopySid((uint32_t)((uint32_t)(result)), result, v_stack_m248, v_stack_p60 + 1472 + 16);
    result = ((uint32_t)((uint32_t)(result)) + 3) & ((uint32_t)(0xFFFFFFFCULL));
    local_rsi = (result) + (result);
    result = v_stack_m200;
    if (v_stack_m200 != 0) {
        *(uint64_t *)(v_stack_p60 + 0xB8) = local_rsi;
        Arg2 = v_stack_m200;
        Arg3 = *(uint16_t *)(v_stack_m200 + 0x2);
        Arg1 = local_rsi;
        result = memcpy(Arg1, Arg2, Arg3, v_stack_p60 + 1472 + 16);
    }
    v_stack_p20 = v_stack_m1E8;
    result = SepSetTokenClaims(v_stack_p60, v_stack_m1D8, v_stack_m1E0, (uint32_t)(Arg21));
    if (sign_flag) goto loc_004EA7C8;
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(v_stack_p60, v_stack_m1D8, v_stack_m1E0, (uint32_t)(Arg21));
    if ((uint32_t)(result) == 0) goto loc_004EA7A7;
    result = SepUserClaimsContainAgentId(v_stack_m1D8, v_stack_m1D8, v_stack_m1E0, (uint32_t)(Arg21));
    if ((uint8_t)(result) != 0) {
    }
    if (Arg24 == 0) goto loc_004EA7DA;
    result = SepSetTokenTrust(v_stack_p60, *(uint64_t *)(v_rip + 0xA1B06E), v_stack_m1E0, (uint32_t)(Arg21));
    if (!sign_flag) goto loc_004EA7DA;
loc_004EA7C8:
loc_004EA7CB:
    result = ObfDereferenceObjectWithTag(v_stack_p60, (uint32_t)(0x746C6644ULL), v_stack_m1E0, (uint32_t)(Arg21));
    goto loc_004EA2E1;
loc_004EA7DA:
    if ((*(uint32_t *)(v_rip + 0xAED82F)) == 0) goto loc_004EA85E;
    if ((*(uint32_t *)(v_rip + 0x97D3B4)) != 12) goto loc_004EA85E;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0)) != (*(uint64_t *)(v_rip + 0x97D38F))) goto loc_004EA859;
    Arg1 = (uint32_t)((1) + (1));
    *(uint32_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x118) = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x118)))) < (*(uint32_t *)(v_rip + 0x97D35B))) goto loc_004EA85E;
    result = DbgPrint(v_rip + 1977967, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p60 + 0x478) + 0x118)), v_stack_p60, (uint32_t)(Arg21));
    goto loc_004EA85E;
loc_004EA859:
loc_004EA85E:
    if (Arg24 != 0) goto loc_004EA8D7;
    Arg4 = (*(uint64_t *)(v_rip + 0xAED7B6)) + (76);
    result = SeCreateAccessState(v_stack_m1C8, v_stack_m128, (uint32_t)(v_stack_m240), Arg4);
    if (sign_flag) goto loc_004EA7CB;
    v_stack_p28 = v_stack_m230;
    Arg3 = 0;
    v_stack_p20 = 0;
    result = ObInsertObject(v_stack_p60, v_stack_m1C8, Arg3, 1);
    result = SeDeleteAccessState(v_stack_m1C8, v_stack_m1C8, Arg3, 1);
    if (sign_flag) goto loc_004EA2E1;
    if (v_stack_p51 != 0) goto loc_004EA7C8;
    result = SepFinalizeTokenAcls(v_stack_p60, v_stack_m1C8, Arg3, 1);
    goto loc_004EA7C8;
loc_004EA8D7:
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    local_rbx = (uint32_t)((uint32_t)(result));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x248)) != 0) {
        v_stack_p28 = 0;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_p20 = 0;
        Arg2 = 0;
        Arg1 = v_stack_p60;
        result = ObInsertObject(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (sign_flag) goto loc_004EA930;
    if (v_stack_p51 == 0) {
        Arg1 = v_stack_p60;
        result = SepFinalizeTokenAcls(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(v_stack_m230) = v_stack_p60;
    goto loc_004EA2E1;
loc_004EA930:
    *(uint64_t *)(v_stack_m230) = 0;
    goto loc_004EA2E1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg8` | `+ 0x0` | `64` | `R` |
| `Arg9` | `+ 0x0` | `64` | `R` |
| `Arg11` | `- 0x8` | `64` | `R` |
| `Arg11` | `+ 0x0` | `32` | `R` |
| `Arg11` | `+ 0x0` | `32` | `W` |
| `Arg11` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg11` | `+ 0x0 + rax*8` | `128` | `R` |
| `Arg11` | `+ 0x0 + rdi*8` | `64` | `R` |
| `Arg11` | `+ 0x0 + rdi*8` | `128` | `W` |
| `Arg11` | `+ 0x8 + rdi*8` | `32` | `R` |
| `Arg12` | `+ 0x10` | `32` | `R` |
| `Arg18` | `+ 0x0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E9CD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
