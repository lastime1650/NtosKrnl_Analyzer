# PiDevCfgCopyDeviceKey

- RVA: `0x00997374`–`0x00997B4B` (길이 `2,007` bytes)
- VA: `0x0000000140997374`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00099358`
- 디코드: `497`개 명령, `2,007/2,007` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00997436` → [IopGetRegistryKeyInformation](IopGetRegistryKeyInformation_function_009972C0.md) (function, `0x009972C0`)
- `0x0099746E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997480` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009974B7` → [ZwEnumerateValueKey](../../text/6A/ZwEnumerateValueKey_function_006AD330.md) (function, `0x006AD330`)
- `0x009974DD` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x0099756C` → [IopGetRegistryValue](IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00997623` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x00997655` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0099769B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0099772E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997748` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00997792` → [PiDevCfgResolveMultiSzValue](../AB/PiDevCfgResolveMultiSzValue_function_00AB6894.md) (function, `0x00AB6894`)
- `0x009977DB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997822` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (function, `0x006AD710`)
- `0x00997848` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00997890` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x009978BD` → [PiDevCfgGetKeySecurityDescriptor](PiDevCfgGetKeySecurityDescriptor_function_00996240.md) (function, `0x00996240`)
- `0x00997929` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00997959` → [PiDevCfgPushCopyKeyEntry](../../text/4A/PiDevCfgPushCopyKeyEntry_function_004AFBA4.md) (function, `0x004AFBA4`)
- `0x009979C1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009979D9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00997A04` → [PiDevCfgParsePropertyKeyName](../../text/5A/PiDevCfgParsePropertyKeyName_function_005A7E70.md) (function, `0x005A7E70`)
- `0x00997A56` → [PiDevCfgPushCopyKeyEntry](../../text/4A/PiDevCfgPushCopyKeyEntry_function_004AFBA4.md) (function, `0x004AFBA4`)
- `0x00997A6D` → [ZwDeleteValueKey](../../text/6A/ZwDeleteValueKey_function_006AECB0.md) (function, `0x006AECB0`)
- `0x00997A8D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997AA8` → [PnpCtxRegDeleteTree](../96/PnpCtxRegDeleteTree_function_00965CC8.md) (function, `0x00965CC8`)
- `0x00997ADE` → [ZwSetSecurityObject](../../text/6B/ZwSetSecurityObject_function_006B0810.md) (function, `0x006B0810`)
- `0x00997AEC` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00997AFD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997B10` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00997B2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997B37` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00997B41` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [PiDevCfgCopyDeviceProperties](../70/PiDevCfgCopyDeviceProperties_function_007044F0.md) at `0x0070450C`
- [PiDevCfgCopyDeviceKeys](PiDevCfgCopyDeviceKeys_function_00995E1C.md) at `0x00995EE8`

### Static image references
- `0x00997390` → RVA `0x00E0A740` (`.data`; read)
- `0x00997AA1` → RVA `0x00E66398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **28**
  - `0x0099746E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997480` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009974B7` → [ZwEnumerateValueKey](../../text/6A/ZwEnumerateValueKey_function_006AD330.md) (`PAGE` → `.text`)
  - `0x009974DD` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00997623` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x00997655` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0099769B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0099772E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997748` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009977DB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997822` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (`PAGE` → `.text`)
  - `0x00997848` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00997890` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x00997929` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x00997959` → [PiDevCfgPushCopyKeyEntry](../../text/4A/PiDevCfgPushCopyKeyEntry_function_004AFBA4.md) (`PAGE` → `.text`)
  - `0x009979C1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009979D9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00997A04` → [PiDevCfgParsePropertyKeyName](../../text/5A/PiDevCfgParsePropertyKeyName_function_005A7E70.md) (`PAGE` → `.text`)
  - `0x00997A56` → [PiDevCfgPushCopyKeyEntry](../../text/4A/PiDevCfgPushCopyKeyEntry_function_004AFBA4.md) (`PAGE` → `.text`)
  - `0x00997A6D` → [ZwDeleteValueKey](../../text/6A/ZwDeleteValueKey_function_006AECB0.md) (`PAGE` → `.text`)
  - `0x00997A8D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997ADE` → [ZwSetSecurityObject](../../text/6B/ZwSetSecurityObject_function_006B0810.md) (`PAGE` → `.text`)
  - `0x00997AEC` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00997AFD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997B10` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00997B2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997B37` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00997B41` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x0099754D` → [sub_00B2C5F4 + 0x9C](../B2/Unknown_function_00B2C5F4.md) (`tail-transfer`)
  - `0x009975A8` → [sub_00B2C5F4 + 0x132](../B2/Unknown_function_00B2C5F4.md) (`tail-transfer`)
  - `0x009975F6` → [sub_00B2C5F4 + 0x22D](../B2/Unknown_function_00B2C5F4.md) (`tail-transfer`)
  - `0x00997710` → [sub_00B2C5F4](../B2/Unknown_function_00B2C5F4.md) (`tail-transfer`)
  - `0x009978DA` → [sub_00B2C5F4 + 0x406](../B2/Unknown_function_00B2C5F4.md) (`tail-transfer`)
  - `0x009979A3` → [sub_00B2C5F4 + 0x369](../B2/Unknown_function_00B2C5F4.md) (`tail-transfer`)
  - `0x009979E4` → [sub_00B2C5F4 + 0x55D](../B2/Unknown_function_00B2C5F4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00997374  40 55                           push rbp
00997376  53                              push rbx
00997377  56                              push rsi
00997378  57                              push rdi
00997379  41 54                           push r12
0099737B  41 55                           push r13
0099737D  41 56                           push r14
0099737F  41 57                           push r15
00997381  48 8D AC 24 68 FF FF FF         lea rbp, [rsp - 0x98]
00997389  48 81 EC 98 01 00 00            sub rsp, 0x198
00997390  48 8B 05 A9 33 47 00            mov rax, qword ptr [rip + 0x4733a9]
00997397  48 33 C4                        xor rax, rsp
0099739A  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
009973A1  48 8B 85 08 01 00 00            mov rax, qword ptr [rbp + 0x108]
009973A8  0F 57 C0                        xorps xmm0, xmm0
009973AB  48 8B F1                        mov rsi, rcx
009973AE  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
009973B2  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
009973B9  0F 57 C9                        xorps xmm1, xmm1
009973BC  48 89 4D 20                     mov qword ptr [rbp + 0x20], rcx
009973C0  4D 8B F8                        mov r15, r8
009973C3  33 C9                           xor ecx, ecx
009973C5  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
009973C9  33 C0                           xor eax, eax
009973CB  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
009973D0  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
009973D4  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
009973D8  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
009973DC  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
009973E0  89 4D DC                        mov dword ptr [rbp - 0x24], ecx
009973E3  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
009973E7  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
009973EB  89 4D A8                        mov dword ptr [rbp - 0x58], ecx
009973EE  48 8B CE                        mov rcx, rsi
009973F1  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
009973F6  48 8D 55 B8                     lea rdx, [rbp - 0x48]
009973FA  44 89 4D D4                     mov dword ptr [rbp - 0x2c], r9d
009973FE  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
00997402  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00997406  48 89 45 08                     mov qword ptr [rbp + 8], rax
0099740A  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
0099740E  89 45 10                        mov dword ptr [rbp + 0x10], eax
00997411  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
00997415  89 85 80 00 00 00               mov dword ptr [rbp + 0x80], eax
0099741B  0F 11 4D 40                     movups xmmword ptr [rbp + 0x40], xmm1
0099741F  C7 45 D0 01 00 00 00            mov dword ptr [rbp - 0x30], 1
00997426  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
0099742A  0F 11 4D C0                     movups xmmword ptr [rbp - 0x40], xmm1
0099742E  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
00997432  0F 11 4D 70                     movups xmmword ptr [rbp + 0x70], xmm1
00997436  E8 85 FE FF FF                  call 0x1409972c0
0099743B  8B D8                           mov ebx, eax
0099743D  85 C0                           test eax, eax
0099743F  0F 88 2F 02 00 00               js 0x140997674
00997445  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00997449  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
0099744C  8D 14 45 1A 00 00 00            lea edx, [rax*2 + 0x1a]
00997453  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
00997456  8D 04 45 12 00 00 00            lea eax, [rax*2 + 0x12]
0099745D  3B C2                           cmp eax, edx
0099745F  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00997463  0F 46 C2                        cmovbe eax, edx
00997466  33 D2                           xor edx, edx
00997468  8B D8                           mov ebx, eax
0099746A  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
0099746E  E8 FD B3 1E 00                  call 0x140b82870
00997473  8B D3                           mov edx, ebx
00997475  B9 00 01 00 00                  mov ecx, 0x100
0099747A  41 B8 50 70 64 63               mov r8d, 0x63647050
00997480  E8 6B AC 1E 00                  call 0x140b820f0
00997485  33 D2                           xor edx, edx
00997487  4C 8B E8                        mov r13, rax
0099748A  48 85 C0                        test rax, rax
0099748D  0F 84 5B 05 00 00               je 0x1409979ee
00997493  4C 8B F0                        mov r14, rax
00997496  44 8B E2                        mov r12d, edx
00997499  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0099749E  44 89 65 D8                     mov dword ptr [rbp - 0x28], r12d
009974A2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009974A7  4D 8B CE                        mov r9, r14
009974AA  45 33 C0                        xor r8d, r8d
009974AD  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
009974B1  41 8B D4                        mov edx, r12d
009974B4  48 8B CE                        mov rcx, rsi
009974B7  E8 74 5E D1 FF                  call 0x1406ad330
009974BC  33 D2                           xor edx, edx
009974BE  8B D8                           mov ebx, eax
009974C0  85 C0                           test eax, eax
009974C2  0F 88 4D 02 00 00               js 0x140997715
009974C8  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
009974CC  48 8D 4D 60                     lea rcx, [rbp + 0x60]
009974D0  48 D1 E8                        shr rax, 1
009974D3  66 41 89 54 46 0C               mov word ptr [r14 + rax*2 + 0xc], dx
009974D9  49 8D 56 0C                     lea rdx, [r14 + 0xc]
009974DD  E8 7E C4 AC FF                  call 0x140463960
009974E2  33 D2                           xor edx, edx
009974E4  8B D8                           mov ebx, eax
009974E6  85 C0                           test eax, eax
009974E8  0F 88 70 01 00 00               js 0x14099765e
009974EE  0F 28 45 60                     movaps xmm0, xmmword ptr [rbp + 0x60]
009974F2  8B FA                           mov edi, edx
009974F4  48 8B 5D 20                     mov rbx, qword ptr [rbp + 0x20]
009974F8  66 0F 7F 45 C0                  movdqa xmmword ptr [rbp - 0x40], xmm0
009974FD  66 0F 73 D8 08                  psrldq xmm0, 8
00997502  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
00997506  66 48 0F 7E C6                  movq rsi, xmm0
0099750B  48 85 DB                        test rbx, rbx
0099750E  0F 85 F2 01 00 00               jne 0x140997706
00997514  41 8B 5E 04                     mov ebx, dword ptr [r14 + 4]
00997518  81 E3 00 00 FF FF               and ebx, 0xffff0000
0099751E  66 41 89 56 06                  mov word ptr [r14 + 6], dx
00997523  0F BA E3 16                     bt ebx, 0x16
00997527  0F 82 B0 01 00 00               jb 0x1409976dd
0099752D  4D 85 FF                        test r15, r15
00997530  0F 85 C2 04 00 00               jne 0x1409979f8
00997536  0B DF                           or ebx, edi
00997538  F7 C3 00 00 03 00               test ebx, 0x30000
0099753E  0F 94 C1                        sete cl
00997541  F6 85 00 01 00 00 01            test byte ptr [rbp + 0x100], 1
00997548  0F 95 C0                        setne al
0099754B  84 C8                           test al, cl
0099754D  0F 84 3D 51 19 00               je 0x140b2c690
00997553  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00997557  4C 8D 4D 88                     lea r9, [rbp - 0x78]
0099755B  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
0099755F  4C 8B E2                        mov r12, rdx
00997562  48 89 55 B8                     mov qword ptr [rbp - 0x48], rdx
00997566  45 33 C0                        xor r8d, r8d
00997569  48 8B D6                        mov rdx, rsi
0099756C  E8 7B 1B 00 00                  call 0x1409990ec
00997571  33 D2                           xor edx, edx
00997573  8B D8                           mov ebx, eax
00997575  85 C0                           test eax, eax
00997577  0F 88 E1 00 00 00               js 0x14099765e
0099757D  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00997581  8B 41 04                        mov eax, dword ptr [rcx + 4]
00997584  44 8B F8                        mov r15d, eax
00997587  8B 71 08                        mov esi, dword ptr [rcx + 8]
0099758A  41 81 E7 00 00 FF FF            and r15d, 0xffff0000
00997591  8B 79 0C                        mov edi, dword ptr [rcx + 0xc]
00997594  48 03 F1                        add rsi, rcx
00997597  44 0F B7 F0                     movzx r14d, ax
0099759B  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
0099759F  48 85 C0                        test rax, rax
009975A2  74 0A                           je 0x1409975ae
009975A4  48 39 50 10                     cmp qword ptr [rax + 0x10], rdx
009975A8  0F 85 78 51 19 00               jne 0x140b2c726
009975AE  41 83 FE 01                     cmp r14d, 1
009975B2  0F 85 FD 00 00 00               jne 0x1409976b5
009975B8  41 F7 C7 00 00 0C 00            test r15d, 0xc0000
009975BF  0F 85 9C 01 00 00               jne 0x140997761
009975C5  45 33 C0                        xor r8d, r8d
009975C8  48 85 F6                        test rsi, rsi
009975CB  0F 84 27 01 00 00               je 0x1409976f8
009975D1  41 81 FE 00 80 00 00            cmp r14d, 0x8000
009975D8  0F 84 42 04 00 00               je 0x140997a20
009975DE  45 85 F6                        test r14d, r14d
009975E1  0F 84 06 01 00 00               je 0x1409976ed
009975E7  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
009975EB  41 8B C7                        mov eax, r15d
009975EE  25 00 00 20 00                  and eax, 0x200000
009975F3  48 85 D2                        test rdx, rdx
009975F6  0F 85 25 52 19 00               jne 0x140b2c821
009975FC  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00997600  85 C0                           test eax, eax
00997602  0F 85 5D 04 00 00               jne 0x140997a65
00997608  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
0099760C  45 8B CE                        mov r9d, r14d
0099760F  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
00997613  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00997618  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
0099761D  48 8B CE                        mov rcx, rsi
00997620  44 8B 07                        mov r8d, dword ptr [rdi]
00997623  E8 A8 66 D1 FF                  call 0x1406adcd0
00997628  8B D8                           mov ebx, eax
0099762A  45 33 C0                        xor r8d, r8d
0099762D  4D 85 E4                        test r12, r12
00997630  0F 85 52 04 00 00               jne 0x140997a88
00997636  4C 39 45 E0                     cmp qword ptr [rbp - 0x20], r8
0099763A  75 14                           jne 0x140997650
0099763C  41 81 FE 00 80 00 00            cmp r14d, 0x8000
00997643  74 0B                           je 0x140997650
00997645  41 0F BA E7 14                  bt r15d, 0x14
0099764A  0F 82 4A 04 00 00               jb 0x140997a9a
00997650  33 D2                           xor edx, edx
00997652  48 8B CF                        mov rcx, rdi
00997655  E8 16 B2 1E 00                  call 0x140b82870
0099765A  85 DB                           test ebx, ebx
0099765C  79 74                           jns 0x1409976d2
0099765E  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
00997662  4D 85 ED                        test r13, r13
00997665  0F 85 6B 01 00 00               jne 0x1409977d6
0099766B  4D 85 F6                        test r14, r14
0099766E  0F 85 B4 04 00 00               jne 0x140997b28
00997674  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00997679  48 85 C9                        test rcx, rcx
0099767C  0F 85 B5 04 00 00               jne 0x140997b37
00997682  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00997686  48 85 C9                        test rcx, rcx
00997689  0F 85 B2 04 00 00               jne 0x140997b41
0099768F  8B C3                           mov eax, ebx
00997691  48 8B 8D 88 00 00 00            mov rcx, qword ptr [rbp + 0x88]
00997698  48 33 CC                        xor rcx, rsp
0099769B  E8 A0 4F D1 FF                  call 0x1406ac640
009976A0  48 81 C4 98 01 00 00            add rsp, 0x198
009976A7  41 5F                           pop r15
009976A9  41 5E                           pop r14
009976AB  41 5D                           pop r13
009976AD  41 5C                           pop r12
009976AF  5F                              pop rdi
009976B0  5E                              pop rsi
009976B1  5B                              pop rbx
009976B2  5D                              pop rbp
009976B3  C3                              ret
009976B4  CC                              int3
009976B5  B8 02 00 00 00                  mov eax, 2
009976BA  44 3B F0                        cmp r14d, eax
009976BD  0F 84 F5 FE FF FF               je 0x1409975b8
009976C3  41 83 FE 07                     cmp r14d, 7
009976C7  0F 85 F8 FE FF FF               jne 0x1409975c5
009976CD  E9 E6 FE FF FF                  jmp 0x1409975b8
009976D2  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
009976D6  4D 8B F5                        mov r14, r13
009976D9  44 8B 65 D8                     mov r12d, dword ptr [rbp - 0x28]
009976DD  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
009976E1  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
009976E5  41 FF C4                        inc r12d
009976E8  E9 AC FD FF FF                  jmp 0x140997499
009976ED  41 0F BA E7 14                  bt r15d, 0x14
009976F2  0F 83 EF FE FF FF               jae 0x1409975e7
009976F8  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
009976FD  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
00997701  E9 27 FF FF FF                  jmp 0x14099762d
00997706  48 39 53 10                     cmp qword ptr [rbx + 0x10], rdx
0099770A  0F 84 04 FE FF FF               je 0x140997514
00997710  E9 DF 4E 19 00                  jmp 0x140b2c5f4
00997715  3D 1A 00 00 80                  cmp eax, 0x8000001a
0099771A  0F 84 C5 00 00 00               je 0x1409977e5
00997720  3D 05 00 00 80                  cmp eax, 0x80000005
00997725  0F 85 33 FF FF FF               jne 0x14099765e
0099772B  49 8B CD                        mov rcx, r13
0099772E  E8 3D B1 1E 00                  call 0x140b82870
00997733  8B 5C 24 70                     mov ebx, dword ptr [rsp + 0x70]
00997737  B9 00 01 00 00                  mov ecx, 0x100
0099773C  8B D3                           mov edx, ebx
0099773E  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
00997742  41 B8 50 70 64 63               mov r8d, 0x63647050
00997748  E8 A3 A9 1E 00                  call 0x140b820f0
0099774D  4C 8B E8                        mov r13, rax
00997750  48 85 C0                        test rax, rax
00997753  0F 84 59 03 00 00               je 0x140997ab2
00997759  4C 8B F0                        mov r14, rax
0099775C  41 FF CC                        dec r12d
0099775F  EB 84                           jmp 0x1409976e5
00997761  48 8D 45 B8                     lea rax, [rbp - 0x48]
00997765  45 8B CF                        mov r9d, r15d
00997768  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0099776D  4C 8B C6                        mov r8, rsi
00997770  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00997775  8B D7                           mov edx, edi
00997777  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0099777C  41 8B CE                        mov ecx, r14d
0099777F  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00997783  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00997788  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0099778D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00997792  E8 FD F0 11 00                  call 0x140ab6894
00997797  4C 8B 65 B8                     mov r12, qword ptr [rbp - 0x48]
0099779B  45 33 C0                        xor r8d, r8d
0099779E  8B D8                           mov ebx, eax
009977A0  85 C0                           test eax, eax
009977A2  0F 88 70 02 00 00               js 0x140997a18
009977A8  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
009977AC  41 BE 07 00 00 00               mov r14d, 7
009977B2  49 8B F4                        mov rsi, r12
009977B5  41 8D 46 FB                     lea eax, [r14 - 5]
009977B9  3B F8                           cmp edi, eax
009977BB  0F 82 07 FE FF FF               jb 0x1409975c8
009977C1  66 45 39 04 24                  cmp word ptr [r12], r8w
009977C6  0F 85 FC FD FF FF               jne 0x1409975c8
009977CC  41 0F BA EF 15                  bts r15d, 0x15
009977D1  E9 F2 FD FF FF                  jmp 0x1409975c8
009977D6  33 D2                           xor edx, edx
009977D8  49 8B CD                        mov rcx, r13
009977DB  E8 90 B0 1E 00                  call 0x140b82870
009977E0  E9 86 FE FF FF                  jmp 0x14099766b
009977E5  8B DA                           mov ebx, edx
009977E7  4D 85 FF                        test r15, r15
009977EA  0F 85 6E FE FF FF               jne 0x14099765e
009977F0  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
009977F4  48 39 55 28                     cmp qword ptr [rbp + 0x28], rdx
009977F8  0F 84 64 FE FF FF               je 0x140997662
009977FE  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
00997802  8B F2                           mov esi, edx
00997804  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
00997808  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0099780D  4D 8B CD                        mov r9, r13
00997810  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00997815  45 33 C0                        xor r8d, r8d
00997818  8B D6                           mov edx, esi
0099781A  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
0099781F  49 8B CC                        mov rcx, r12
00997822  E8 E9 5E D1 FF                  call 0x1406ad710
00997827  33 D2                           xor edx, edx
00997829  8B D8                           mov ebx, eax
0099782B  85 C0                           test eax, eax
0099782D  0F 88 75 01 00 00               js 0x1409979a8
00997833  41 8B 45 0C                     mov eax, dword ptr [r13 + 0xc]
00997837  48 8D 4D 50                     lea rcx, [rbp + 0x50]
0099783B  48 D1 E8                        shr rax, 1
0099783E  66 41 89 54 45 10               mov word ptr [r13 + rax*2 + 0x10], dx
00997844  49 8D 55 10                     lea rdx, [r13 + 0x10]
00997848  E8 13 C1 AC FF                  call 0x140463960
0099784D  8B D8                           mov ebx, eax
0099784F  85 C0                           test eax, eax
00997851  0F 88 0B FE FF FF               js 0x140997662
00997857  0F 28 45 50                     movaps xmm0, xmmword ptr [rbp + 0x50]
0099785B  48 8D 45 50                     lea rax, [rbp + 0x50]
0099785F  66 0F 7F 45 40                  movdqa xmmword ptr [rbp + 0x40], xmm0
00997864  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00997868  0F 57 C0                        xorps xmm0, xmm0
0099786B  C7 45 E8 30 00 00 00            mov dword ptr [rbp - 0x18], 0x30
00997872  BA 19 00 02 00                  mov edx, 0x20019
00997877  4C 89 65 F0                     mov qword ptr [rbp - 0x10], r12
0099787B  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00997880  C7 45 00 40 02 00 00            mov dword ptr [rbp], 0x240
00997887  F3 0F 7F 45 08                  movdqu xmmword ptr [rbp + 8], xmm0
0099788C  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00997890  E8 7B 5A D1 FF                  call 0x1406ad310
00997895  33 D2                           xor edx, edx
00997897  8B D8                           mov ebx, eax
00997899  85 C0                           test eax, eax
0099789B  0F 88 C1 FD FF FF               js 0x140997662
009978A1  48 8B 5D 20                     mov rbx, qword ptr [rbp + 0x20]
009978A5  8B FA                           mov edi, edx
009978A7  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
009978AB  48 85 DB                        test rbx, rbx
009978AE  0F 85 E5 00 00 00               jne 0x140997999
009978B4  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009978B9  48 8D 55 90                     lea rdx, [rbp - 0x70]
009978BD  E8 7E E9 FF FF                  call 0x140996240
009978C2  33 D2                           xor edx, edx
009978C4  8B D8                           mov ebx, eax
009978C6  85 C0                           test eax, eax
009978C8  0F 89 F2 01 00 00               jns 0x140997ac0
009978CE  8B DA                           mov ebx, edx
009978D0  48 89 55 90                     mov qword ptr [rbp - 0x70], rdx
009978D4  44 8B F2                        mov r14d, edx
009978D7  48 85 FF                        test rdi, rdi
009978DA  0F 85 1A 51 19 00               jne 0x140b2c9fa
009978E0  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
009978E5  4C 8D 45 E8                     lea r8, [rbp - 0x18]
009978E9  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
009978ED  48 8D 4D 80                     lea rcx, [rbp - 0x80]
009978F1  48 8D 45 40                     lea rax, [rbp + 0x40]
009978F5  48 89 55 10                     mov qword ptr [rbp + 0x10], rdx
009978F9  48 89 45 F8                     mov qword ptr [rbp - 8], rax
009978FD  45 33 C9                        xor r9d, r9d
00997900  48 8D 45 DC                     lea rax, [rbp - 0x24]
00997904  C7 45 E8 30 00 00 00            mov dword ptr [rbp - 0x18], 0x30
0099790B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00997910  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00997914  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00997919  BA 3F 00 0F 00                  mov edx, 0xf003f
0099791E  C7 45 00 40 02 00 00            mov dword ptr [rbp], 0x240
00997925  4C 89 75 08                     mov qword ptr [rbp + 8], r14
00997929  E8 42 5B D1 FF                  call 0x1406ad470
0099792E  8B D8                           mov ebx, eax
00997930  85 C0                           test eax, eax
00997932  78 3F                           js 0x140997973
00997934  8D 47 02                        lea eax, [rdi + 2]
00997937  39 45 DC                        cmp dword ptr [rbp - 0x24], eax
0099793A  0F 84 89 01 00 00               je 0x140997ac9
00997940  44 8B 8D 00 01 00 00            mov r9d, dword ptr [rbp + 0x100]
00997947  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
0099794B  41 0F BA E9 1E                  bts r9d, 0x1e
00997950  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00997955  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00997959  E8 46 82 B1 FF                  call 0x1404afba4
0099795E  33 D2                           xor edx, edx
00997960  8B D8                           mov ebx, eax
00997962  85 C0                           test eax, eax
00997964  0F 88 7E 01 00 00               js 0x140997ae8
0099796A  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
0099796F  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
00997973  4D 85 F6                        test r14, r14
00997976  0F 85 7C 01 00 00               jne 0x140997af8
0099797C  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00997981  48 85 C9                        test rcx, rcx
00997984  0F 85 86 01 00 00               jne 0x140997b10
0099798A  85 DB                           test ebx, ebx
0099798C  0F 88 D0 FC FF FF               js 0x140997662
00997992  FF C6                           inc esi
00997994  E9 6F FE FF FF                  jmp 0x140997808
00997999  48 39 53 10                     cmp qword ptr [rbx + 0x10], rdx
0099799D  0F 84 11 FF FF FF               je 0x1409978b4
009979A3  E9 B5 4F 19 00                  jmp 0x140b2c95d
009979A8  3D 1A 00 00 80                  cmp eax, 0x8000001a
009979AD  0F 84 6E 01 00 00               je 0x140997b21
009979B3  3D 05 00 00 80                  cmp eax, 0x80000005
009979B8  0F 85 A4 FC FF FF               jne 0x140997662
009979BE  49 8B CD                        mov rcx, r13
009979C1  E8 AA AE 1E 00                  call 0x140b82870
009979C6  44 8B 7C 24 70                  mov r15d, dword ptr [rsp + 0x70]
009979CB  B9 00 01 00 00                  mov ecx, 0x100
009979D0  41 8B D7                        mov edx, r15d
009979D3  41 B8 50 70 64 63               mov r8d, 0x63647050
009979D9  E8 12 A7 1E 00                  call 0x140b820f0
009979DE  4C 8B E8                        mov r13, rax
009979E1  48 85 C0                        test rax, rax
009979E4  0F 84 67 51 19 00               je 0x140b2cb51
009979EA  FF CE                           dec esi
009979EC  EB A4                           jmp 0x140997992
009979EE  BB 9A 00 00 C0                  mov ebx, 0xc000009a
009979F3  E9 7C FC FF FF                  jmp 0x140997674
009979F8  4C 8D 45 D0                     lea r8, [rbp - 0x30]
009979FC  48 8D 55 70                     lea rdx, [rbp + 0x70]
00997A00  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00997A04  E8 67 04 C1 FF                  call 0x1405a7e70
00997A09  33 D2                           xor edx, edx
00997A0B  84 C0                           test al, al
00997A0D  0F 84 CA FC FF FF               je 0x1409976dd
00997A13  E9 1E FB FF FF                  jmp 0x140997536
00997A18  41 8B D8                        mov ebx, r8d
00997A1B  E9 D8 FC FF FF                  jmp 0x1409976f8
00997A20  48 83 7D E0 00                  cmp qword ptr [rbp - 0x20], 0
00997A25  0F 85 CD FC FF FF               jne 0x1409976f8
00997A2B  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
00997A2F  48 85 C0                        test rax, rax
00997A32  0F 84 C0 FC FF FF               je 0x1409976f8
00997A38  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00997A3D  45 8B CF                        mov r9d, r15d
00997A40  41 C1 E9 11                     shr r9d, 0x11
00997A44  48 8B D6                        mov rdx, rsi
00997A47  41 F7 D1                        not r9d
00997A4A  48 8B C8                        mov rcx, rax
00997A4D  41 83 E1 01                     and r9d, 1
00997A51  41 0F BA E9 1F                  bts r9d, 0x1f
00997A56  E8 49 81 B1 FF                  call 0x1404afba4
00997A5B  8B D8                           mov ebx, eax
00997A5D  45 33 C0                        xor r8d, r8d
00997A60  E9 93 FC FF FF                  jmp 0x1409976f8
00997A65  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00997A6A  48 8B CE                        mov rcx, rsi
00997A6D  E8 3E 72 D1 FF                  call 0x1406aecb0
00997A72  3D 34 00 00 C0                  cmp eax, 0xc0000034
00997A77  8B D8                           mov ebx, eax
00997A79  41 B8 00 00 00 00               mov r8d, 0
00997A7F  41 0F 44 D8                     cmove ebx, r8d
00997A83  E9 75 FC FF FF                  jmp 0x1409976fd
00997A88  33 D2                           xor edx, edx
00997A8A  49 8B CC                        mov rcx, r12
00997A8D  E8 DE AD 1E 00                  call 0x140b82870
00997A92  45 33 C0                        xor r8d, r8d
00997A95  E9 9C FB FF FF                  jmp 0x140997636
00997A9A  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
00997A9E  48 8B D6                        mov rdx, rsi
00997AA1  48 8B 0D F0 E8 4C 00            mov rcx, qword ptr [rip + 0x4ce8f0]
00997AA8  E8 1B E2 FC FF                  call 0x140965cc8
00997AAD  E9 9E FB FF FF                  jmp 0x140997650
00997AB2  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
00997AB6  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00997ABB  E9 AB FB FF FF                  jmp 0x14099766b
00997AC0  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
00997AC4  E9 0E FE FF FF                  jmp 0x1409978d7
00997AC9  4D 85 F6                        test r14, r14
00997ACC  0F 84 6E FE FF FF               je 0x140997940
00997AD2  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00997AD6  4D 8B C6                        mov r8, r14
00997AD9  BA 04 00 00 00                  mov edx, 4
00997ADE  E8 2D 8D D1 FF                  call 0x1406b0810
00997AE3  E9 58 FE FF FF                  jmp 0x140997940
00997AE8  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00997AEC  E8 BF 57 D1 FF                  call 0x1406ad2b0
00997AF1  33 D2                           xor edx, edx
00997AF3  E9 72 FE FF FF                  jmp 0x14099796a
00997AF8  33 D2                           xor edx, edx
00997AFA  49 8B CE                        mov rcx, r14
00997AFD  E8 6E AD 1E 00                  call 0x140b82870
00997B02  33 D2                           xor edx, edx
00997B04  44 8B F2                        mov r14d, edx
00997B07  48 89 55 90                     mov qword ptr [rbp - 0x70], rdx
00997B0B  E9 6C FE FF FF                  jmp 0x14099797c
00997B10  E8 9B 57 D1 FF                  call 0x1406ad2b0
00997B15  33 D2                           xor edx, edx
00997B17  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
00997B1C  E9 69 FE FF FF                  jmp 0x14099798a
00997B21  8B DA                           mov ebx, edx
00997B23  E9 3A FB FF FF                  jmp 0x140997662
00997B28  33 D2                           xor edx, edx
00997B2A  49 8B CE                        mov rcx, r14
00997B2D  E8 3E AD 1E 00                  call 0x140b82870
00997B32  E9 3D FB FF FF                  jmp 0x140997674
00997B37  E8 74 57 D1 FF                  call 0x1406ad2b0
00997B3C  E9 41 FB FF FF                  jmp 0x140997682
00997B41  E8 6A 57 D1 FF                  call 0x1406ad2b0
00997B46  E9 44 FB FF FF                  jmp 0x14099768f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgCopyDeviceKey(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (408);
    result = (*(unsigned __int64 *)(v_rip + 4666281)) ^ (v_rsp);
    v_stack_m50 = result;
    v_stack_m138 = a1;
    v_stack_mB8 = a7;
    a1 = 0;
    v_stack_mB0 = a6;
    result = 0;
    v_stack_m160 = 0;
    v_stack_m158 = 0;
    v_stack_m148 = 0;
    v_stack_m168 = 0;
    v_stack_m120 = 0;
    v_stack_mFC = 0;
    v_stack_mC0 = 0;
    v_stack_m178 = 0;
    v_stack_m130 = 0;
    v_stack_m170 = a2;
    v_stack_m104 = a4;
    v_stack_mF8 = a3;
    v_stack_mF0 = v_xmm0;
    v_stack_mD0 = 0;
    v_stack_mE0 = v_xmm0;
    v_stack_mC8 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m58 = 0;
    v_stack_m98 = v_xmm1;
    v_stack_m108 = 1;
    v_stack_m78 = v_xmm0;
    v_stack_m118 = v_xmm1;
    v_stack_mA8 = v_xmm0;
    v_stack_m68 = v_xmm1;
    result = IopGetRegistryKeyInformation(0, v_stack_m120, a3, a4);
    if (sign_flag) goto loc_00997674;
    v_stack_m168 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m120 + 36)) * 2 + 18);
    result = (unsigned int)(*(unsigned int *)(v_stack_m120 + 36)) * 2 + 18;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m120 + 36)) * 2 + 18)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m120 + 24)) * 2 + 26))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m120 + 24)) * 2 + 26); }
    a2 = 0;
    v_stack_m140 = (unsigned int)((unsigned int)(result));
    result = ExFreePoolWithTag(v_stack_m120, a2, a3, a4);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x63647050ULL), a4);
    a2 = 0;
    if (result == 0) goto loc_009979EE;
loc_00997499:
    v_stack_m100 = 0;
    v_stack_m1B0 = v_stack_m168;
    a3 = 0;
    v_stack_m1B8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = ZwEnumerateValueKey(0, 0, a3, result);
    a2 = 0;
    if (sign_flag) goto loc_00997715;
    result = ((unsigned int)(*(unsigned int *)(result + 8))) >> (1);
    *(unsigned __int16 *)(result + result * 2 + 12) = 0;
    result = RtlInitUnicodeStringEx(v_stack_m78, result + 12, a3, result);
    a2 = 0;
    if (sign_flag) goto loc_0099765E;
    v_stack_m118 = v_xmm0;
    v_stack_m164 = 0;
    if (v_stack_mB8 != 0) goto loc_00997706;
loc_00997514:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 4))) & (0xFFFF0000ULL));
    *(unsigned __int16 *)(result + 6) = 0;
    if (condition_is_below) goto loc_009976DD;
    if (0 != 0) goto loc_009979F8;
loc_00997536:
    v_rbx = (unsigned int)((v_rbx) | (0));
    a1 = ((((unsigned int)(v_rbx)) & (0x30000ULL)) == 0) ? 1 : 0;
    result = (((a5) & (1)) != 0) ? 1 : 0;
    v_stack_m150 = 0;
    v_stack_m120 = 0;
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m138, a1, a3, v_stack_m150);
    a2 = 0;
    if (sign_flag) goto loc_0099765E;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))) & (0xFFFF0000ULL));
    v_rsi = ((unsigned int)(*(unsigned int *)(v_stack_m150 + 8))) + (v_stack_m150);
    if (v_stack_mB8 == 0) goto loc_009975AE;
loc_009975AE:
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))) != 1) goto loc_009976B5;
loc_009975B8:
    if ((((unsigned int)(v_r15)) & (0xC0000ULL)) != 0) goto loc_00997761;
loc_009975C5:
    a3 = 0;
loc_009975C8:
    if (v_rsi == 0) goto loc_009976F8;
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))) == 0x8000ULL) goto loc_00997A20;
    if ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4)))) == 0) goto loc_009976ED;
loc_009975E7:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (0x200000ULL));
    if ((unsigned int)(result) != 0) goto loc_00997A65;
    v_stack_m1B0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m150 + 12)));
    v_stack_m1B8 = v_rsi;
    result = ZwSetValueKey(v_stack_m170, v_stack_m118, (unsigned int)(*(unsigned int *)(v_stack_m150)), (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))));
    a3 = 0;
loc_0099762D:
    if (0 != 0) goto loc_00997A88;
loc_00997636:
    if (v_stack_mF8 != 0) goto loc_00997650;
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))) == 0x8000ULL) goto loc_00997650;
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))) < 0x8000ULL) goto loc_00997A9A;
loc_00997650:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m150, a2, a3, (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))));
    if (!sign_flag) goto loc_009976D2;
loc_0099765E:
loc_00997662:
    if (result != 0) goto loc_009977D6;
loc_0099766B:
    if (v_stack_m148 != 0) goto loc_00997B28;
loc_00997674:
    if (v_stack_m160 != 0) goto loc_00997B37;
loc_00997682:
    if (v_stack_m158 != 0) goto loc_00997B41;
loc_0099768F:
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))));
    v_rsp = (v_rsp) + (408);
    return result;
loc_009976B5:
    if (((unsigned int)(v_stack_m148)) == 2) goto loc_009975B8;
    if (((unsigned int)(v_stack_m148)) != 7) goto loc_009975C5;
    goto loc_009975B8;
loc_009976D2:
loc_009976DD:
loc_009976E5:
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m100)) + 1);
    goto loc_00997499;
loc_009976ED:
    if (((unsigned int)(v_stack_m148)) >= 7) goto loc_009975E7;
loc_009976F8:
loc_009976FD:
    goto loc_0099762D;
loc_00997706:
    if ((*(unsigned __int64 *)(v_stack_m140 + 16)) == 0) goto loc_00997514;
loc_00997715:
    if (2 == 0x8000001AULL) goto loc_009977E5;
    if (2 != 0x80000005ULL) goto loc_0099765E;
    result = ExFreePoolWithTag(result, a2, a3, (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))));
    v_stack_m140 = (unsigned int)(v_stack_p70);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_p70))), (unsigned int)(0x63647050ULL), (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m150 + 4))))));
    if (result == 0) goto loc_00997AB2;
    v_r12 = (unsigned int)((v_r12) - 1);
    goto loc_009976E5;
loc_00997761:
    v_stack_p38 = v_stack_m120;
    v_stack_p30 = v_stack_p70;
    v_stack_p28 = v_stack_m110;
    v_stack_p20 = v_stack_p68;
    result = PiDevCfgResolveMultiSzValue((unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_stack_m150)), v_stack_p68, (unsigned int)((unsigned int)(v_stack_mF8)));
    a3 = 0;
    if (sign_flag) goto loc_00997A18;
    if (((unsigned int)((unsigned int)(v_stack_p70))) < ((unsigned int)(7 - 5))) goto loc_009975C8;
    if ((*(unsigned __int16 *)(v_stack_m120)) != 0) goto loc_009975C8;
    goto loc_009975C8;
loc_009977D6:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, (unsigned int)((unsigned int)(v_stack_mF8)));
    goto loc_0099766B;
loc_009977E5:
    if (v_stack_mF8 != 0) goto loc_0099765E;
    if (v_stack_mB0 == 0) goto loc_00997662;
loc_00997808:
    v_stack_p28 = v_stack_p70;
    a3 = 0;
    v_stack_p20 = (unsigned int)(v_stack_m140);
    result = ZwEnumerateKey(v_stack_m138, 0, a3, result);
    a2 = 0;
    if (sign_flag) goto loc_009979A8;
    result = ((unsigned int)(*(unsigned int *)(result + 12))) >> (1);
    *(unsigned __int16 *)(result + result * 2 + 16) = 0;
    result = RtlInitUnicodeStringEx(v_stack_m88, result + 16, a3, result);
    if (sign_flag) goto loc_00997662;
    v_stack_m98 = v_xmm0;
    v_stack_mF0 = 48;
    v_stack_mE8 = v_stack_m138;
    v_stack_mD8 = 576;
    v_stack_mD0 = v_xmm0;
    v_stack_mE0 = v_stack_m88;
    result = ZwOpenKey(v_stack_p78, (unsigned int)(0x20019ULL), v_stack_mF0, result);
    a2 = 0;
    if (sign_flag) goto loc_00997662;
    v_stack_p74 = 0;
    if (v_stack_mB8 != 0) goto loc_00997999;
loc_009978B4:
    result = PiDevCfgGetKeySecurityDescriptor(v_stack_p78, v_stack_m148, v_stack_mF0, result);
    a2 = 0;
    if (!sign_flag) goto loc_00997AC0;
    v_stack_m148 = 0;
loc_009978D7:
    v_stack_mE8 = v_stack_p68;
    v_stack_mC8 = 0;
    v_stack_mE0 = v_stack_m98;
    a4 = 0;
    v_stack_mF0 = 48;
    v_stack_p30 = v_stack_mFC;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    v_stack_mD8 = 576;
    v_stack_mD0 = 0;
    result = ZwCreateKey(v_stack_m158, (unsigned int)(0xF003FULL), v_stack_mF0, a4);
    if (sign_flag) goto loc_00997973;
    if (v_stack_mFC == ((unsigned int)(0 + 2))) goto loc_00997AC9;
loc_00997940:
    result = PiDevCfgPushCopyKeyEntry(v_stack_mB0, v_stack_p78, v_stack_m158, (unsigned int)(a5));
    a2 = 0;
    if (sign_flag) goto loc_00997AE8;
loc_0099796A:
    v_stack_p78 = 0;
    v_stack_m158 = 0;
loc_00997973:
    if (0 != 0) goto loc_00997AF8;
loc_0099797C:
    if (v_stack_p78 != 0) goto loc_00997B10;
loc_0099798A:
    if (sign_flag) goto loc_00997662;
loc_00997992:
    v_rsi = (unsigned int)((0) + 1);
    goto loc_00997808;
loc_00997999:
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 16)) == 0) goto loc_009978B4;
loc_009979A8:
    if (((unsigned int)(result)) == 0x8000001AULL) goto loc_00997B21;
    if (((unsigned int)(result)) != 0x80000005ULL) goto loc_00997662;
    result = ExFreePoolWithTag(result, a2, v_stack_m158, (unsigned int)(a5));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_p70))), (unsigned int)(0x63647050ULL), (unsigned int)(a5));
    v_rsi = (unsigned int)((v_rsi) - 1);
    goto loc_00997992;
loc_009979EE:
    goto loc_00997674;
loc_009979F8:
    result = PiDevCfgParsePropertyKeyName(v_stack_m118, v_stack_m68, v_stack_m108, (unsigned int)(a5));
    a2 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_009976DD;
    goto loc_00997536;
loc_00997A18:
    goto loc_009976F8;
loc_00997A20:
    if (v_stack_mF8 != 0) goto loc_009976F8;
    if (v_stack_mB0 == 0) goto loc_009976F8;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p70)))) >> (17));
    a4 = (unsigned int)(~(a4));
    a4 = (unsigned int)((a4) & (1));
    result = PiDevCfgPushCopyKeyEntry(v_stack_mB0, v_rsi, v_stack_p68, a4);
    a3 = 0;
    goto loc_009976F8;
loc_00997A65:
    result = ZwDeleteValueKey(v_stack_p68, v_rsi, a3, a4);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 0xC0000034ULL) { v_rbx = 0; }
    goto loc_009976FD;
loc_00997A88:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m138, a2, 0, a4);
    a3 = 0;
    goto loc_00997636;
loc_00997A9A:
    result = PnpCtxRegDeleteTree(*(unsigned __int64 *)(v_rip + 5040368), v_stack_p68, v_stack_m110, a4);
    goto loc_00997650;
loc_00997AB2:
    goto loc_0099766B;
loc_00997AC0:
    goto loc_009978D7;
loc_00997AC9:
    if (v_stack_m148 == 0) goto loc_00997940;
    result = ZwSetSecurityObject(v_stack_m158, 4, v_stack_m148, a4);
    goto loc_00997940;
loc_00997AE8:
    result = ZwClose(v_stack_m158, 4, v_stack_m148, a4);
    a2 = 0;
    goto loc_0099796A;
loc_00997AF8:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m148, a2, v_stack_m148, a4);
    a2 = 0;
    v_stack_m148 = 0;
    goto loc_0099797C;
loc_00997B10:
    result = ZwClose(v_stack_m148, a2, v_stack_m148, a4);
    a2 = 0;
    v_stack_p78 = 0;
    goto loc_0099798A;
loc_00997B21:
    goto loc_00997662;
loc_00997B28:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, v_stack_m148, a4);
    goto loc_00997674;
loc_00997B37:
    result = ZwClose(0, a2, v_stack_m148, a4);
    goto loc_00997682;
loc_00997B41:
    result = ZwClose(0, a2, v_stack_m148, a4);
    goto loc_0099768F;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgCopyDeviceKey(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5, int64_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (408);
    result = (*(uint64_t *)(v_rip + 0x4733A9)) ^ (local_rsp);
    v_stack_m50 = result;
    v_stack_m138 = Arg1;
    v_stack_mB8 = Arg7;
    Arg1 = 0;
    v_stack_mB0 = Arg6;
    result = 0;
    v_stack_m160 = 0;
    v_stack_m158 = 0;
    v_stack_m148 = 0;
    v_stack_m168 = 0;
    v_stack_m120 = 0;
    v_stack_mFC = 0;
    v_stack_mC0 = 0;
    v_stack_m178 = 0;
    v_stack_m130 = 0;
    v_stack_m170 = Arg2;
    v_stack_m104 = Arg4;
    v_stack_mF8 = Arg3;
    v_stack_mF0 = v_xmm0;
    v_stack_mD0 = 0;
    v_stack_mE0 = v_xmm0;
    v_stack_mC8 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m58 = 0;
    v_stack_m98 = v_xmm1;
    v_stack_m108 = 1;
    v_stack_m78 = v_xmm0;
    v_stack_m118 = v_xmm1;
    v_stack_mA8 = v_xmm0;
    v_stack_m68 = v_xmm1;
    result = IopGetRegistryKeyInformation(0, v_stack_m120, Arg3, Arg4);
    if (sign_flag) goto loc_00997674;
    v_stack_m168 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m120 + 0x24)) * 2 + 18);
    result = (uint32_t)(*(uint32_t *)(v_stack_m120 + 0x24)) * 2 + 18;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m120 + 0x24)) * 2 + 18)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m120 + 0x18)) * 2 + 26))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m120 + 0x18)) * 2 + 26); }
    Arg2 = 0;
    v_stack_m140 = (uint32_t)((uint32_t)(result));
    result = ExFreePoolWithTag(v_stack_m120, Arg2, Arg3, Arg4);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x63647050ULL), Arg4);
    Arg2 = 0;
    if (result == 0) goto loc_009979EE;
loc_00997499:
    v_stack_m100 = 0;
    v_stack_m1B0 = v_stack_m168;
    Arg3 = 0;
    v_stack_m1B8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = ZwEnumerateValueKey(0, 0, Arg3, result);
    Arg2 = 0;
    if (sign_flag) goto loc_00997715;
    result = ((uint32_t)(*(uint32_t *)(result + 0x8))) >> (1);
    *(uint16_t *)(result + result * 2 + 0xC) = 0;
    result = RtlInitUnicodeStringEx(v_stack_m78, result + 12, Arg3, result);
    Arg2 = 0;
    if (sign_flag) goto loc_0099765E;
    v_stack_m118 = v_xmm0;
    v_stack_m164 = 0;
    if (v_stack_mB8 != 0) goto loc_00997706;
loc_00997514:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x4))) & (0xFFFF0000ULL));
    *(uint16_t *)(result + 0x6) = 0;
    if (condition_is_below) goto loc_009976DD;
    if (0 != 0) goto loc_009979F8;
loc_00997536:
    local_rbx = (uint32_t)((local_rbx) | (0));
    Arg1 = ((((uint32_t)(local_rbx)) & (0x30000ULL)) == 0) ? 1 : 0;
    result = (((Arg5) & (1)) != 0) ? 1 : 0;
    v_stack_m150 = 0;
    v_stack_m120 = 0;
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m138, Arg1, Arg3, v_stack_m150);
    Arg2 = 0;
    if (sign_flag) goto loc_0099765E;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))) & (0xFFFF0000ULL));
    local_rsi = ((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x8))) + (v_stack_m150);
    if (v_stack_mB8 == 0) goto loc_009975AE;
loc_009975AE:
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))) != 1) goto loc_009976B5;
loc_009975B8:
    if ((((uint32_t)(local_r15)) & (0xC0000ULL)) != 0) goto loc_00997761;
loc_009975C5:
    Arg3 = 0;
loc_009975C8:
    if (local_rsi == 0) goto loc_009976F8;
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))) == 0x8000ULL) goto loc_00997A20;
    if ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4)))) == 0) goto loc_009976ED;
loc_009975E7:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (0x200000ULL));
    if ((uint32_t)(result) != 0) goto loc_00997A65;
    v_stack_m1B0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0xC)));
    v_stack_m1B8 = local_rsi;
    result = ZwSetValueKey(v_stack_m170, v_stack_m118, (uint32_t)(*(uint32_t *)(v_stack_m150)), (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))));
    Arg3 = 0;
loc_0099762D:
    if (0 != 0) goto loc_00997A88;
loc_00997636:
    if (v_stack_mF8 != 0) goto loc_00997650;
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))) == 0x8000ULL) goto loc_00997650;
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))) < 0x8000ULL) goto loc_00997A9A;
loc_00997650:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m150, Arg2, Arg3, (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))));
    if (!sign_flag) goto loc_009976D2;
loc_0099765E:
loc_00997662:
    if (result != 0) goto loc_009977D6;
loc_0099766B:
    if (v_stack_m148 != 0) goto loc_00997B28;
loc_00997674:
    if (v_stack_m160 != 0) goto loc_00997B37;
loc_00997682:
    if (v_stack_m158 != 0) goto loc_00997B41;
loc_0099768F:
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))));
    local_rsp = (local_rsp) + (408);
    return result;
loc_009976B5:
    if (((uint32_t)(v_stack_m148)) == 2) goto loc_009975B8;
    if (((uint32_t)(v_stack_m148)) != 7) goto loc_009975C5;
    goto loc_009975B8;
loc_009976D2:
loc_009976DD:
loc_009976E5:
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m100)) + 1);
    goto loc_00997499;
loc_009976ED:
    if (((uint32_t)(v_stack_m148)) >= 7) goto loc_009975E7;
loc_009976F8:
loc_009976FD:
    goto loc_0099762D;
loc_00997706:
    if ((*(uint64_t *)(v_stack_m140 + 0x10)) == 0) goto loc_00997514;
loc_00997715:
    if (2 == 0x8000001AULL) goto loc_009977E5;
    if (2 != 0x80000005ULL) goto loc_0099765E;
    result = ExFreePoolWithTag(result, Arg2, Arg3, (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))));
    v_stack_m140 = (uint32_t)(v_stack_p70);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_p70))), (uint32_t)(0x63647050ULL), (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x4))))));
    if (result == 0) goto loc_00997AB2;
    local_r12 = (uint32_t)((local_r12) - 1);
    goto loc_009976E5;
loc_00997761:
    v_stack_p38 = v_stack_m120;
    v_stack_p30 = v_stack_p70;
    v_stack_p28 = v_stack_m110;
    v_stack_p20 = v_stack_p68;
    result = PiDevCfgResolveMultiSzValue((uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(v_stack_m150)), v_stack_p68, (uint32_t)((uint32_t)(v_stack_mF8)));
    Arg3 = 0;
    if (sign_flag) goto loc_00997A18;
    if (((uint32_t)((uint32_t)(v_stack_p70))) < ((uint32_t)(7 - 5))) goto loc_009975C8;
    if ((*(uint16_t *)(v_stack_m120)) != 0) goto loc_009975C8;
    goto loc_009975C8;
loc_009977D6:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, (uint32_t)((uint32_t)(v_stack_mF8)));
    goto loc_0099766B;
loc_009977E5:
    if (v_stack_mF8 != 0) goto loc_0099765E;
    if (v_stack_mB0 == 0) goto loc_00997662;
loc_00997808:
    v_stack_p28 = v_stack_p70;
    Arg3 = 0;
    v_stack_p20 = (uint32_t)(v_stack_m140);
    result = ZwEnumerateKey(v_stack_m138, 0, Arg3, result);
    Arg2 = 0;
    if (sign_flag) goto loc_009979A8;
    result = ((uint32_t)(*(uint32_t *)(result + 0xC))) >> (1);
    *(uint16_t *)(result + result * 2 + 0x10) = 0;
    result = RtlInitUnicodeStringEx(v_stack_m88, result + 16, Arg3, result);
    if (sign_flag) goto loc_00997662;
    v_stack_m98 = v_xmm0;
    v_stack_mF0 = 48;
    v_stack_mE8 = v_stack_m138;
    v_stack_mD8 = 576;
    v_stack_mD0 = v_xmm0;
    v_stack_mE0 = v_stack_m88;
    result = ZwOpenKey(v_stack_p78, (uint32_t)(0x20019ULL), v_stack_mF0, result);
    Arg2 = 0;
    if (sign_flag) goto loc_00997662;
    v_stack_p74 = 0;
    if (v_stack_mB8 != 0) goto loc_00997999;
loc_009978B4:
    result = PiDevCfgGetKeySecurityDescriptor(v_stack_p78, v_stack_m148, v_stack_mF0, result);
    Arg2 = 0;
    if (!sign_flag) goto loc_00997AC0;
    v_stack_m148 = 0;
loc_009978D7:
    v_stack_mE8 = v_stack_p68;
    v_stack_mC8 = 0;
    v_stack_mE0 = v_stack_m98;
    Arg4 = 0;
    v_stack_mF0 = 48;
    v_stack_p30 = v_stack_mFC;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    v_stack_mD8 = 576;
    v_stack_mD0 = 0;
    result = ZwCreateKey(v_stack_m158, (uint32_t)(0xF003FULL), v_stack_mF0, Arg4);
    if (sign_flag) goto loc_00997973;
    if (v_stack_mFC == ((uint32_t)(0 + 2))) goto loc_00997AC9;
loc_00997940:
    result = PiDevCfgPushCopyKeyEntry(v_stack_mB0, v_stack_p78, v_stack_m158, (uint32_t)(Arg5));
    Arg2 = 0;
    if (sign_flag) goto loc_00997AE8;
loc_0099796A:
    v_stack_p78 = 0;
    v_stack_m158 = 0;
loc_00997973:
    if (0 != 0) goto loc_00997AF8;
loc_0099797C:
    if (v_stack_p78 != 0) goto loc_00997B10;
loc_0099798A:
    if (sign_flag) goto loc_00997662;
loc_00997992:
    local_rsi = (uint32_t)((0) + 1);
    goto loc_00997808;
loc_00997999:
    if ((*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x10)) == 0) goto loc_009978B4;
loc_009979A8:
    if (((uint32_t)(result)) == 0x8000001AULL) goto loc_00997B21;
    if (((uint32_t)(result)) != 0x80000005ULL) goto loc_00997662;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m158, (uint32_t)(Arg5));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_p70))), (uint32_t)(0x63647050ULL), (uint32_t)(Arg5));
    local_rsi = (uint32_t)((local_rsi) - 1);
    goto loc_00997992;
loc_009979EE:
    goto loc_00997674;
loc_009979F8:
    result = PiDevCfgParsePropertyKeyName(v_stack_m118, v_stack_m68, v_stack_m108, (uint32_t)(Arg5));
    Arg2 = 0;
    if ((uint8_t)(result) == 0) goto loc_009976DD;
    goto loc_00997536;
loc_00997A18:
    goto loc_009976F8;
loc_00997A20:
    if (v_stack_mF8 != 0) goto loc_009976F8;
    if (v_stack_mB0 == 0) goto loc_009976F8;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p70)))) >> (17));
    Arg4 = (uint32_t)(~(Arg4));
    Arg4 = (uint32_t)((Arg4) & (1));
    result = PiDevCfgPushCopyKeyEntry(v_stack_mB0, local_rsi, v_stack_p68, Arg4);
    Arg3 = 0;
    goto loc_009976F8;
loc_00997A65:
    result = ZwDeleteValueKey(v_stack_p68, local_rsi, Arg3, Arg4);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 0xC0000034ULL) { local_rbx = 0; }
    goto loc_009976FD;
loc_00997A88:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m138, Arg2, 0, Arg4);
    Arg3 = 0;
    goto loc_00997636;
loc_00997A9A:
    result = PnpCtxRegDeleteTree(*(uint64_t *)(v_rip + 0x4CE8F0), v_stack_p68, v_stack_m110, Arg4);
    goto loc_00997650;
loc_00997AB2:
    goto loc_0099766B;
loc_00997AC0:
    goto loc_009978D7;
loc_00997AC9:
    if (v_stack_m148 == 0) goto loc_00997940;
    result = ZwSetSecurityObject(v_stack_m158, 4, v_stack_m148, Arg4);
    goto loc_00997940;
loc_00997AE8:
    result = ZwClose(v_stack_m158, 4, v_stack_m148, Arg4);
    Arg2 = 0;
    goto loc_0099796A;
loc_00997AF8:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m148, Arg2, v_stack_m148, Arg4);
    Arg2 = 0;
    v_stack_m148 = 0;
    goto loc_0099797C;
loc_00997B10:
    result = ZwClose(v_stack_m148, Arg2, v_stack_m148, Arg4);
    Arg2 = 0;
    v_stack_p78 = 0;
    goto loc_0099798A;
loc_00997B21:
    goto loc_00997662;
loc_00997B28:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, v_stack_m148, Arg4);
    goto loc_00997674;
loc_00997B37:
    result = ZwClose(0, Arg2, v_stack_m148, Arg4);
    goto loc_00997682;
loc_00997B41:
    result = ZwClose(0, Arg2, v_stack_m148, Arg4);
    goto loc_0099768F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00997374&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
