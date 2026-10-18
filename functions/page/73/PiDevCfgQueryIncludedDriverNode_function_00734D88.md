# PiDevCfgQueryIncludedDriverNode

- RVA: `0x00734D88`–`0x007351FC` (길이 `1,140` bytes)
- VA: `0x0000000140734D88`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8BA0`
- 디코드: `312`개 명령, `1,140/1,140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00734DDE` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00734DF2` → [PiDevCfgOpenDriverConfiguration](../A9/PiDevCfgOpenDriverConfiguration_function_00A995F0.md) (function, `0x00A995F0`)
- `0x00734E1E` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00734E3C` → [PiDevCfgGetDriverPackageId](../97/PiDevCfgGetDriverPackageId_function_00977690.md) (function, `0x00977690`)
- `0x00734E84` → [PnpOpenObjectRegKey](../8E/PnpOpenObjectRegKey_function_008E15E8.md) (function, `0x008E15E8`)
- `0x00734EA3` → [PiDevCfgOpenDriverConfiguration](../A9/PiDevCfgOpenDriverConfiguration_function_00A995F0.md) (function, `0x00A995F0`)
- `0x00734EC6` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00734EDC` → [PiDevCfgOpenDriverConfiguration](../A9/PiDevCfgOpenDriverConfiguration_function_00A995F0.md) (function, `0x00A995F0`)
- `0x00734F27` → [PnpCtxRegOpenKey](../8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x00734F61` → [PiDevCfgGetDriverPackageId](../97/PiDevCfgGetDriverPackageId_function_00977690.md) (function, `0x00977690`)
- `0x00734F9D` → [PnpOpenObjectRegKey](../8E/PnpOpenObjectRegKey_function_008E15E8.md) (function, `0x008E15E8`)
- `0x00734FC0` → [PiDevCfgOpenDriverConfiguration](../A9/PiDevCfgOpenDriverConfiguration_function_00A995F0.md) (function, `0x00A995F0`)
- `0x00734FDC` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00734FEB` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0073502E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00735049` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x00735083` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x00735094` → [PiDevCfgFreeDriverNode](PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x007350A3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007350B1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007350BF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007350C8` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007350F6` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00735106` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x00735129` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00735150` → [PnpValidateRegistryMultiSz](../../text/4D/PnpValidateRegistryMultiSz_function_004DC170.md) (function, `0x004DC170`)
- `0x007351A2` → [PiDevCfgGetDriverConfigurationKeyScope](../../text/5A/PiDevCfgGetDriverConfigurationKeyScope_function_005A7D68.md) (function, `0x005A7D68`)

### Direct callers
- [PiDevCfgQueryIncludedDriverConfigurations](../97/PiDevCfgQueryIncludedDriverConfigurations_function_009754BC.md) at `0x00975651`

### Static image references
- `0x00734E7D` → RVA `0x00E66398` (`.data`; read)
- `0x0073511F` → RVA `0x00AFF070` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00734DDE` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00734E1E` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00734EC6` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00734FDC` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0073502E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00735049` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x007350A3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007350B1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007350BF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007350F6` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00735150` → [PnpValidateRegistryMultiSz](../../text/4D/PnpValidateRegistryMultiSz_function_004DC170.md) (`PAGE` → `.text`)
  - `0x007351A2` → [PiDevCfgGetDriverConfigurationKeyScope](../../text/5A/PiDevCfgGetDriverConfigurationKeyScope_function_005A7D68.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00734D88  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00734D8D  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00734D92  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00734D97  55                              push rbp
00734D98  41 54                           push r12
00734D9A  41 55                           push r13
00734D9C  41 56                           push r14
00734D9E  41 57                           push r15
00734DA0  48 8B EC                        mov rbp, rsp
00734DA3  48 83 EC 60                     sub rsp, 0x60
00734DA7  48 8B F9                        mov rdi, rcx
00734DAA  45 8B E9                        mov r13d, r9d
00734DAD  33 C9                           xor ecx, ecx
00734DAF  4D 8B F8                        mov r15, r8
00734DB2  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00734DB6  48 8B F2                        mov rsi, rdx
00734DB9  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
00734DBD  8B D9                           mov ebx, ecx
00734DBF  48 89 4D 38                     mov qword ptr [rbp + 0x38], rcx
00734DC3  44 8B E1                        mov r12d, ecx
00734DC6  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
00734DCA  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
00734DCE  48 85 D2                        test rdx, rdx
00734DD1  0F 84 DD 00 00 00               je 0x140734eb4
00734DD7  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00734DDB  48 8B CE                        mov rcx, rsi
00734DDE  E8 9D B2 DC FF                  call 0x140500080
00734DE3  85 C0                           test eax, eax
00734DE5  75 4E                           jne 0x140734e35
00734DE7  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00734DEB  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00734DEF  49 8B D7                        mov rdx, r15
00734DF2  E8 F9 47 36 00                  call 0x140a995f0
00734DF7  41 BE 34 00 00 C0               mov r14d, 0xc0000034
00734DFD  8B D8                           mov ebx, eax
00734DFF  41 3B C6                        cmp eax, r14d
00734E02  75 0A                           jne 0x140734e0e
00734E04  BB 92 04 00 C0                  mov ebx, 0xc0000492
00734E09  E9 9A 02 00 00                  jmp 0x1407350a8
00734E0E  85 C0                           test eax, eax
00734E10  0F 88 92 02 00 00               js 0x1407350a8
00734E16  48 8D 57 38                     lea rdx, [rdi + 0x38]
00734E1A  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00734E1E  E8 21 72 D9 FF                  call 0x1404cc044
00734E23  84 C0                           test al, al
00734E25  0F 85 DA 00 00 00               jne 0x140734f05
00734E2B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00734E30  E9 73 02 00 00                  jmp 0x1407350a8
00734E35  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00734E39  48 8B CE                        mov rcx, rsi
00734E3C  E8 4F 28 24 00                  call 0x140977690
00734E41  41 BE 34 00 00 C0               mov r14d, 0xc0000034
00734E47  8B D8                           mov ebx, eax
00734E49  41 3B C6                        cmp eax, r14d
00734E4C  75 0A                           jne 0x140734e58
00734E4E  BB 91 04 00 C0                  mov ebx, 0xc0000491
00734E53  E9 50 02 00 00                  jmp 0x1407350a8
00734E58  33 C9                           xor ecx, ecx
00734E5A  85 C0                           test eax, eax
00734E5C  0F 88 46 02 00 00               js 0x1407350a8
00734E62  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
00734E66  48 8D 45 38                     lea rax, [rbp + 0x38]
00734E6A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00734E6F  44 8D 41 08                     lea r8d, [rcx + 8]
00734E73  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00734E77  41 B9 19 00 02 00               mov r9d, 0x20019
00734E7D  48 8B 0D 14 15 73 00            mov rcx, qword ptr [rip + 0x731514]
00734E84  E8 5F C7 1A 00                  call 0x1408e15e8
00734E89  8B D8                           mov ebx, eax
00734E8B  41 3B C6                        cmp eax, r14d
00734E8E  74 BE                           je 0x140734e4e
00734E90  85 C0                           test eax, eax
00734E92  0F 88 10 02 00 00               js 0x1407350a8
00734E98  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
00734E9C  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00734EA0  49 8B D7                        mov rdx, r15
00734EA3  E8 48 47 36 00                  call 0x140a995f0
00734EA8  8B D8                           mov ebx, eax
00734EAA  41 3B C6                        cmp eax, r14d
00734EAD  75 7F                           jne 0x140734f2e
00734EAF  E9 50 FF FF FF                  jmp 0x140734e04
00734EB4  48 8B 57 60                     mov rdx, qword ptr [rdi + 0x60]
00734EB8  41 BE 34 00 00 C0               mov r14d, 0xc0000034
00734EBE  48 85 D2                        test rdx, rdx
00734EC1  74 0E                           je 0x140734ed1
00734EC3  49 8B CF                        mov rcx, r15
00734EC6  E8 B5 B1 DC FF                  call 0x140500080
00734ECB  33 C9                           xor ecx, ecx
00734ECD  85 C0                           test eax, eax
00734ECF  74 25                           je 0x140734ef6
00734ED1  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00734ED5  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00734ED9  49 8B D7                        mov rdx, r15
00734EDC  E8 0F 47 36 00                  call 0x140a995f0
00734EE1  33 C9                           xor ecx, ecx
00734EE3  8B D8                           mov ebx, eax
00734EE5  41 3B C6                        cmp eax, r14d
00734EE8  75 04                           jne 0x140734eee
00734EEA  8B D9                           mov ebx, ecx
00734EEC  EB 08                           jmp 0x140734ef6
00734EEE  85 C0                           test eax, eax
00734EF0  0F 88 B2 01 00 00               js 0x1407350a8
00734EF6  48 39 4D E0                     cmp qword ptr [rbp - 0x20], rcx
00734EFA  74 3F                           je 0x140734f3b
00734EFC  48 8B 77 30                     mov rsi, qword ptr [rdi + 0x30]
00734F00  E9 11 FF FF FF                  jmp 0x140734e16
00734F05  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
00734F09  48 8D 45 38                     lea rax, [rbp + 0x38]
00734F0D  48 8B 0D 84 14 73 00            mov rcx, qword ptr [rip + 0x731484]
00734F14  45 33 C9                        xor r9d, r9d
00734F17  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00734F1C  45 33 C0                        xor r8d, r8d
00734F1F  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00734F27  E8 8C A8 1B 00                  call 0x1408ef7b8
00734F2C  8B D8                           mov ebx, eax
00734F2E  85 C0                           test eax, eax
00734F30  0F 88 72 01 00 00               js 0x1407350a8
00734F36  E9 E3 00 00 00                  jmp 0x14073501e
00734F3B  48 8B B7 68 01 00 00            mov rsi, qword ptr [rdi + 0x168]
00734F42  48 85 F6                        test rsi, rsi
00734F45  75 0A                           jne 0x140734f51
00734F47  BB 92 04 00 C0                  mov ebx, 0xc0000492
00734F4C  E9 65 01 00 00                  jmp 0x1407350b6
00734F51  66 39 0E                        cmp word ptr [rsi], cx
00734F54  0F 84 B2 00 00 00               je 0x14073500c
00734F5A  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00734F5E  48 8B CE                        mov rcx, rsi
00734F61  E8 2A 27 24 00                  call 0x140977690
00734F66  8B D8                           mov ebx, eax
00734F68  41 3B C6                        cmp eax, r14d
00734F6B  0F 84 DD FE FF FF               je 0x140734e4e
00734F71  33 C9                           xor ecx, ecx
00734F73  85 C0                           test eax, eax
00734F75  0F 88 2D 01 00 00               js 0x1407350a8
00734F7B  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
00734F7F  48 8D 45 38                     lea rax, [rbp + 0x38]
00734F83  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00734F88  44 8D 41 08                     lea r8d, [rcx + 8]
00734F8C  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00734F90  41 B9 19 00 02 00               mov r9d, 0x20019
00734F96  48 8B 0D FB 13 73 00            mov rcx, qword ptr [rip + 0x7313fb]
00734F9D  E8 46 C6 1A 00                  call 0x1408e15e8
00734FA2  8B D8                           mov ebx, eax
00734FA4  41 3B C6                        cmp eax, r14d
00734FA7  0F 84 A1 FE FF FF               je 0x140734e4e
00734FAD  85 C0                           test eax, eax
00734FAF  0F 88 F3 00 00 00               js 0x1407350a8
00734FB5  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
00734FB9  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00734FBD  49 8B D7                        mov rdx, r15
00734FC0  E8 2B 46 36 00                  call 0x140a995f0
00734FC5  33 C9                           xor ecx, ecx
00734FC7  8B D8                           mov ebx, eax
00734FC9  85 C0                           test eax, eax
00734FCB  79 47                           jns 0x140735014
00734FCD  41 3B C6                        cmp eax, r14d
00734FD0  0F 85 D2 00 00 00               jne 0x1407350a8
00734FD6  8B D9                           mov ebx, ecx
00734FD8  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
00734FDC  E8 CF 82 F7 FF                  call 0x1406ad2b0
00734FE1  33 C0                           xor eax, eax
00734FE3  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00734FE7  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00734FEB  E8 10 B8 28 00                  call 0x1409c0800
00734FF0  48 83 C8 FF                     or rax, 0xffffffffffffffff
00734FF4  33 C9                           xor ecx, ecx
00734FF6  48 FF C0                        inc rax
00734FF9  66 39 0C 46                     cmp word ptr [rsi + rax*2], cx
00734FFD  75 F7                           jne 0x140734ff6
00734FFF  48 8D 34 46                     lea rsi, [rsi + rax*2]
00735003  48 83 C6 02                     add rsi, 2
00735007  E9 45 FF FF FF                  jmp 0x140734f51
0073500C  85 DB                           test ebx, ebx
0073500E  0F 88 94 00 00 00               js 0x1407350a8
00735014  48 39 4D E0                     cmp qword ptr [rbp - 0x20], rcx
00735018  0F 84 29 FF FF FF               je 0x140734f47
0073501E  BA C8 01 00 00                  mov edx, 0x1c8
00735023  B9 00 01 00 00                  mov ecx, 0x100
00735028  41 B8 50 70 64 63               mov r8d, 0x63647050
0073502E  E8 BD D0 44 00                  call 0x140b820f0
00735033  48 8B F8                        mov rdi, rax
00735036  48 85 C0                        test rax, rax
00735039  0F 84 EC FD FF FF               je 0x140734e2b
0073503F  C7 80 B8 00 00 00 20 00 00 00   mov dword ptr [rax + 0xb8], 0x20
00735049  E8 F6 28 DC FF                  call 0x1404f7944
0073504E  85 C0                           test eax, eax
00735050  75 0E                           jne 0x140735060
00735052  48 8D 87 E0 00 00 00            lea rax, [rdi + 0xe0]
00735059  48 89 40 08                     mov qword ptr [rax + 8], rax
0073505D  48 89 00                        mov qword ptr [rax], rax
00735060  48 8D 87 D0 00 00 00            lea rax, [rdi + 0xd0]
00735067  48 8B D6                        mov rdx, rsi
0073506A  48 89 40 08                     mov qword ptr [rax + 8], rax
0073506E  48 8D 4F 28                     lea rcx, [rdi + 0x28]
00735072  48 89 00                        mov qword ptr [rax], rax
00735075  48 8D 87 80 01 00 00            lea rax, [rdi + 0x180]
0073507C  48 89 40 08                     mov qword ptr [rax + 8], rax
00735080  48 89 00                        mov qword ptr [rax], rax
00735083  E8 D8 87 28 00                  call 0x1409bd860
00735088  84 C0                           test al, al
0073508A  75 62                           jne 0x1407350ee
0073508C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00735091  48 8B CF                        mov rcx, rdi
00735094  E8 BB E2 FF FF                  call 0x140733354
00735099  4D 85 E4                        test r12, r12
0073509C  74 0A                           je 0x1407350a8
0073509E  33 D2                           xor edx, edx
007350A0  49 8B CC                        mov rcx, r12
007350A3  E8 C8 D7 44 00                  call 0x140b82870
007350A8  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
007350AC  48 85 C9                        test rcx, rcx
007350AF  74 05                           je 0x1407350b6
007350B1  E8 FA 81 F7 FF                  call 0x1406ad2b0
007350B6  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
007350BA  48 85 C9                        test rcx, rcx
007350BD  74 05                           je 0x1407350c4
007350BF  E8 EC 81 F7 FF                  call 0x1406ad2b0
007350C4  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007350C8  E8 33 B7 28 00                  call 0x1409c0800
007350CD  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
007350D2  8B C3                           mov eax, ebx
007350D4  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
007350D8  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
007350DC  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
007350E0  49 8B E3                        mov rsp, r11
007350E3  41 5F                           pop r15
007350E5  41 5E                           pop r14
007350E7  41 5D                           pop r13
007350E9  41 5C                           pop r12
007350EB  5D                              pop rbp
007350EC  C3                              ret
007350ED  CC                              int3
007350EE  48 8D 4F 38                     lea rcx, [rdi + 0x38]
007350F2  48 8D 55 F0                     lea rdx, [rbp - 0x10]
007350F6  E8 49 6F D9 FF                  call 0x1404cc044
007350FB  84 C0                           test al, al
007350FD  74 8D                           je 0x14073508c
007350FF  48 8D 4F 58                     lea rcx, [rdi + 0x58]
00735103  49 8B D7                        mov rdx, r15
00735106  E8 55 87 28 00                  call 0x1409bd860
0073510B  84 C0                           test al, al
0073510D  0F 84 79 FF FF FF               je 0x14073508c
00735113  44 89 6F 68                     mov dword ptr [rdi + 0x68], r13d
00735117  4C 8D 4D E8                     lea r9, [rbp - 0x18]
0073511B  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
0073511F  48 8D 15 4A 9F 3C 00            lea rdx, [rip + 0x3c9f4a]
00735126  45 33 C0                        xor r8d, r8d
00735129  E8 BE 3F 26 00                  call 0x1409990ec
0073512E  4C 8B 65 E8                     mov r12, qword ptr [rbp - 0x18]
00735132  8B D8                           mov ebx, eax
00735134  41 3B C6                        cmp eax, r14d
00735137  75 09                           jne 0x140735142
00735139  33 C0                           xor eax, eax
0073513B  8B D8                           mov ebx, eax
0073513D  E9 94 00 00 00                  jmp 0x1407351d6
00735142  45 33 FF                        xor r15d, r15d
00735145  85 C0                           test eax, eax
00735147  0F 88 44 FF FF FF               js 0x140735091
0073514D  49 8B CC                        mov rcx, r12
00735150  E8 1B 70 DA FF                  call 0x1404dc170
00735155  84 C0                           test al, al
00735157  75 0A                           jne 0x140735163
00735159  BB 01 00 00 C0                  mov ebx, 0xc0000001
0073515E  E9 2E FF FF FF                  jmp 0x140735091
00735163  41 8B 74 24 08                  mov esi, dword ptr [r12 + 8]
00735168  49 03 F4                        add rsi, r12
0073516B  0F B7 16                        movzx edx, word ptr [rsi]
0073516E  66 85 D2                        test dx, dx
00735171  74 63                           je 0x1407351d6
00735173  0F B7 CA                        movzx ecx, dx
00735176  83 E9 2A                        sub ecx, 0x2a
00735179  75 0A                           jne 0x140735185
0073517B  0F B7 4E 02                     movzx ecx, word ptr [rsi + 2]
0073517F  41 0F B7 C7                     movzx eax, r15w
00735183  2B C8                           sub ecx, eax
00735185  85 C9                           test ecx, ecx
00735187  74 49                           je 0x1407351d2
00735189  41 B6 01                        mov r14b, 1
0073518C  66 83 FA 2B                     cmp dx, 0x2b
00735190  74 09                           je 0x14073519b
00735192  66 83 FA 2D                     cmp dx, 0x2d
00735196  75 07                           jne 0x14073519f
00735198  45 8A F7                        mov r14b, r15b
0073519B  48 83 C6 02                     add rsi, 2
0073519F  48 8B CE                        mov rcx, rsi
007351A2  E8 C1 2B E7 FF                  call 0x1405a7d68
007351A7  8B 4F 68                        mov ecx, dword ptr [rdi + 0x68]
007351AA  45 84 F6                        test r14b, r14b
007351AD  74 04                           je 0x1407351b3
007351AF  0B C8                           or ecx, eax
007351B1  EB 04                           jmp 0x1407351b7
007351B3  F7 D0                           not eax
007351B5  23 C8                           and ecx, eax
007351B7  89 4F 68                        mov dword ptr [rdi + 0x68], ecx
007351BA  48 83 C8 FF                     or rax, 0xffffffffffffffff
007351BE  48 FF C0                        inc rax
007351C1  66 44 39 3C 46                  cmp word ptr [rsi + rax*2], r15w
007351C6  75 F6                           jne 0x1407351be
007351C8  48 8D 34 46                     lea rsi, [rsi + rax*2]
007351CC  48 83 C6 02                     add rsi, 2
007351D0  EB 99                           jmp 0x14073516b
007351D2  83 4F 68 FF                     or dword ptr [rdi + 0x68], 0xffffffff
007351D6  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
007351DA  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
007351DE  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
007351E2  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
007351E6  33 C0                           xor eax, eax
007351E8  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
007351EC  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
007351F0  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
007351F4  48 89 38                        mov qword ptr [rax], rdi
007351F7  E9 9D FE FF FF                  jmp 0x140735099
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgQueryIncludedDriverNode(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (96);
    a1 = 0;
    v_stack_m38 = 0;
    v_stack_m30 = 0;
    v_stack_p10 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    if (a2 == 0) goto loc_00734EB4;
    result = wcsicmp(a2, *(unsigned __int64 *)(a1 + 48), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00734E35;
    result = PiDevCfgOpenDriverConfiguration(*(unsigned __int64 *)(a1 + 16), a3, v_stack_m48, a4);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734E0E;
loc_00734E04:
    goto loc_007350A8;
loc_00734E0E:
    if (sign_flag) goto loc_007350A8;
loc_00734E16:
    result = PnpDuplicateUnicodeString(v_stack_m38, a1 + 56, v_stack_m48, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00734F05;
loc_00734E2B:
    goto loc_007350A8;
loc_00734E35:
    result = PiDevCfgGetDriverPackageId(a2, v_stack_m38, v_stack_m48, a4);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734E58;
loc_00734E4E:
    goto loc_007350A8;
loc_00734E58:
    a1 = 0;
    if (sign_flag) goto loc_007350A8;
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = 0;
    result = PnpOpenObjectRegKey(*(unsigned __int64 *)(v_rip + 7542036), v_stack_m30, a1 + 8, (unsigned int)(0x20019ULL));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734E4E;
    if (sign_flag) goto loc_007350A8;
    result = PiDevCfgOpenDriverConfiguration(v_stack_p10, a3, v_stack_m48, (unsigned int)(0x20019ULL));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734F2E;
    goto loc_00734E04;
loc_00734EB4:
    if (*(unsigned __int64 *)(a1 + 96) == 0) goto loc_00734ED1;
    result = wcsicmp(a3, *(unsigned __int64 *)(a1 + 96), v_stack_m48, (unsigned int)(0x20019ULL));
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00734EF6;
loc_00734ED1:
    result = PiDevCfgOpenDriverConfiguration(*(unsigned __int64 *)(a1 + 16), a3, v_stack_m48, (unsigned int)(0x20019ULL));
    a1 = 0;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734EEE;
    goto loc_00734EF6;
loc_00734EEE:
    if (sign_flag) goto loc_007350A8;
loc_00734EF6:
    if (v_stack_m48 == 0) goto loc_00734F3B;
    goto loc_00734E16;
loc_00734F05:
    a4 = 0;
    v_stack_m60 = v_stack_p10;
    a3 = 0;
    v_stack_m68 = 0x20019ULL;
    result = PnpCtxRegOpenKey(*(unsigned __int64 *)(v_rip + 7541892), *(unsigned __int64 *)(a1 + 16), a3, a4);
loc_00734F2E:
    if (sign_flag) goto loc_007350A8;
    goto loc_0073501E;
loc_00734F3B:
    if (*(unsigned __int64 *)(a1 + 360) != 0) goto loc_00734F51;
loc_00734F47:
    goto loc_007350B6;
loc_00734F51:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 360))) == ((unsigned __int16)(*(unsigned __int64 *)(v_rip + 7541892)))) goto loc_0073500C;
    result = PiDevCfgGetDriverPackageId(*(unsigned __int64 *)(a1 + 360), v_stack_m38, a3, a4);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734E4E;
    a1 = 0;
    if (sign_flag) goto loc_007350A8;
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = 0;
    result = PnpOpenObjectRegKey(*(unsigned __int64 *)(v_rip + 7541755), v_stack_m30, a1 + 8, (unsigned int)(0x20019ULL));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734E4E;
    if (sign_flag) goto loc_007350A8;
    result = PiDevCfgOpenDriverConfiguration(v_stack_p10, 0, v_stack_m48, (unsigned int)(0x20019ULL));
    a1 = 0;
    if (!sign_flag) goto loc_00735014;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_007350A8;
    result = ZwClose(v_stack_p10, 0, v_stack_m48, (unsigned int)(0x20019ULL));
    result = 0;
    v_stack_p10 = 0;
    result = RtlFreeAnsiString(v_stack_m38, 0, v_stack_m48, (unsigned int)(0x20019ULL));
    result = (result) | (-1);
    a1 = 0;
loc_00734FF6:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 360) + result * 2)) != 0) goto loc_00734FF6;
    v_rsi = (*(unsigned __int64 *)(a1 + 360) + result * 2) + (2);
    goto loc_00734F51;
loc_0073500C:
    if (sign_flag) goto loc_007350A8;
loc_00735014:
    if (v_stack_m48 == 0) goto loc_00734F47;
loc_0073501E:
    result = ExAllocatePool2(256, 456, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
    if (result == 0) goto loc_00734E2B;
    *(unsigned int *)(result + 184) = 32;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(256, 456, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
    if ((unsigned int)(result) == 0) {
        result = result + 224;
        *(unsigned __int64 *)(result + 8) = result;
        *(unsigned __int64 *)(result) = result;
    }
    *(unsigned __int64 *)(result + 208 + 8) = result + 208;
    *(unsigned __int64 *)(result + 208) = result + 208;
    *(unsigned __int64 *)(result + 384 + 8) = result + 384;
    *(unsigned __int64 *)(result + 384) = result + 384;
    result = RtlCreateUnicodeString(result + 40, v_rsi, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
    if ((unsigned __int8)(result) != 0) goto loc_007350EE;
loc_0073508C:
loc_00735091:
    result = PiDevCfgFreeDriverNode(result, v_rsi, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
loc_00735099:
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
    }
    if (v_stack_m48 != 0) {
        result = ZwClose(v_stack_m48, a2, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
    }
    if (v_stack_p10 != 0) {
        result = ZwClose(v_stack_p10, a2, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
    }
    result = RtlFreeAnsiString(v_stack_m38, a2, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
    return (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
loc_007350EE:
    result = PnpDuplicateUnicodeString(*(unsigned __int64 *)(v_stack_m28 + 72) + 56, v_stack_m38, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
    if ((unsigned __int8)(result) == 0) goto loc_0073508C;
    result = RtlCreateUnicodeString(*(unsigned __int64 *)(v_stack_m28 + 72) + 88, 0, (unsigned int)(0x63647050ULL), (unsigned int)(0x20019ULL));
    if ((unsigned __int8)(result) == 0) goto loc_0073508C;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 104) = (unsigned int)((unsigned int)(a4));
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m48, v_rip + 3972938, a3, v_stack_m40);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00735142;
    result = 0;
    goto loc_007351D6;
loc_00735142:
    v_r15 = 0;
    if (sign_flag) goto loc_00735091;
    result = PnpValidateRegistryMultiSz(v_stack_m40, v_rip + 3972938, a3, v_stack_m40);
    if ((unsigned __int8)(result) != 0) goto loc_00735163;
    goto loc_00735091;
loc_00735163:
    v_rsi = ((unsigned int)(*(unsigned int *)(v_stack_m40 + 8))) + (v_stack_m40);
loc_0073516B:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) == 0) goto loc_007351D6;
    a1 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) - (42));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int16 *)(v_rsi + 2);
        result = 0;
        a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    }
    if ((unsigned int)(a1) == 0) goto loc_007351D2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) == 43) goto loc_0073519B;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) != 45) goto loc_0073519F;
loc_0073519B:
    v_rsi = (v_rsi) + (2);
loc_0073519F:
    result = PiDevCfgGetDriverConfigurationKeyScope(v_rsi, *(unsigned __int16 *)(v_rsi), a3, v_stack_m40);
    if (0 == 0) goto loc_007351B3;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 104))) | ((unsigned int)(result)));
    goto loc_007351B7;
loc_007351B3:
    result = (unsigned int)(~(result));
    a1 = (unsigned int)((a1) & ((unsigned int)(result)));
loc_007351B7:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 104) = (unsigned int)(a1);
    result = (result) | (-1);
loc_007351BE:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rsi + result * 2)) != 0) goto loc_007351BE;
    v_rsi = (v_rsi + result * 2) + (2);
    goto loc_0073516B;
loc_007351D2:
loc_007351D6:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16) = v_stack_p10;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 32) = v_stack_m48;
    result = 0;
    v_stack_p10 = 0;
    v_stack_m48 = 0;
    *(unsigned __int64 *)(a5) = *(unsigned __int64 *)(v_stack_m28 + 72);
    goto loc_00735099;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgQueryIncludedDriverNode(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m60;
    uint8_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (96);
    Arg1 = 0;
    v_stack_m38 = 0;
    v_stack_m30 = 0;
    v_stack_p10 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    if (Arg2 == 0) goto loc_00734EB4;
    result = wcsicmp(Arg2, *(uint64_t *)(arg1 + 0x30), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00734E35;
    result = PiDevCfgOpenDriverConfiguration(*(uint64_t *)(arg1 + 0x10), Arg3, v_stack_m48, Arg4);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734E0E;
loc_00734E04:
    goto loc_007350A8;
loc_00734E0E:
    if (sign_flag) goto loc_007350A8;
loc_00734E16:
    result = PnpDuplicateUnicodeString(v_stack_m38, Arg1 + 56, v_stack_m48, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00734F05;
loc_00734E2B:
    goto loc_007350A8;
loc_00734E35:
    result = PiDevCfgGetDriverPackageId(Arg2, v_stack_m38, v_stack_m48, Arg4);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734E58;
loc_00734E4E:
    goto loc_007350A8;
loc_00734E58:
    Arg1 = 0;
    if (sign_flag) goto loc_007350A8;
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = 0;
    result = PnpOpenObjectRegKey(*(uint64_t *)(v_rip + 0x731514), v_stack_m30, Arg1 + 8, (uint32_t)(0x20019ULL));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734E4E;
    if (sign_flag) goto loc_007350A8;
    result = PiDevCfgOpenDriverConfiguration(v_stack_p10, Arg3, v_stack_m48, (uint32_t)(0x20019ULL));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734F2E;
    goto loc_00734E04;
loc_00734EB4:
    if (*(uint64_t *)(arg1 + 0x60) == 0) goto loc_00734ED1;
    result = wcsicmp(Arg3, *(uint64_t *)(arg1 + 0x60), v_stack_m48, (uint32_t)(0x20019ULL));
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00734EF6;
loc_00734ED1:
    result = PiDevCfgOpenDriverConfiguration(*(uint64_t *)(arg1 + 0x10), Arg3, v_stack_m48, (uint32_t)(0x20019ULL));
    Arg1 = 0;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734EEE;
    goto loc_00734EF6;
loc_00734EEE:
    if (sign_flag) goto loc_007350A8;
loc_00734EF6:
    if (v_stack_m48 == 0) goto loc_00734F3B;
    goto loc_00734E16;
loc_00734F05:
    Arg4 = 0;
    v_stack_m60 = v_stack_p10;
    Arg3 = 0;
    v_stack_m68 = 0x20019ULL;
    result = PnpCtxRegOpenKey(*(uint64_t *)(v_rip + 0x731484), *(uint64_t *)(arg1 + 0x10), Arg3, Arg4);
loc_00734F2E:
    if (sign_flag) goto loc_007350A8;
    goto loc_0073501E;
loc_00734F3B:
    if (*(uint64_t *)(arg1 + 0x168) != 0) goto loc_00734F51;
loc_00734F47:
    goto loc_007350B6;
loc_00734F51:
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x168))) == ((uint16_t)(*(uint64_t *)(v_rip + 0x731484)))) goto loc_0073500C;
    result = PiDevCfgGetDriverPackageId(*(uint64_t *)(arg1 + 0x168), v_stack_m38, Arg3, Arg4);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734E4E;
    Arg1 = 0;
    if (sign_flag) goto loc_007350A8;
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = 0;
    result = PnpOpenObjectRegKey(*(uint64_t *)(v_rip + 0x7313FB), v_stack_m30, Arg1 + 8, (uint32_t)(0x20019ULL));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734E4E;
    if (sign_flag) goto loc_007350A8;
    result = PiDevCfgOpenDriverConfiguration(v_stack_p10, 0, v_stack_m48, (uint32_t)(0x20019ULL));
    Arg1 = 0;
    if (!sign_flag) goto loc_00735014;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_007350A8;
    result = ZwClose(v_stack_p10, 0, v_stack_m48, (uint32_t)(0x20019ULL));
    result = 0;
    v_stack_p10 = 0;
    result = RtlFreeAnsiString(v_stack_m38, 0, v_stack_m48, (uint32_t)(0x20019ULL));
    result = (result) | (-1);
    Arg1 = 0;
loc_00734FF6:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x168) + result * 2)) != 0) goto loc_00734FF6;
    local_rsi = (*(uint64_t *)(arg1 + 0x168) + result * 2) + (2);
    goto loc_00734F51;
loc_0073500C:
    if (sign_flag) goto loc_007350A8;
loc_00735014:
    if (v_stack_m48 == 0) goto loc_00734F47;
loc_0073501E:
    result = ExAllocatePool2(256, 456, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
    if (result == 0) goto loc_00734E2B;
    *(uint32_t *)(result + 0xB8) = 32;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(256, 456, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
    if ((uint32_t)(result) == 0) {
        result = result + 224;
        *(uint64_t *)(result + 0x8) = result;
        *(uint64_t *)(result) = result;
    }
    *(uint64_t *)(result + 0xD0 + 0x8) = result + 208;
    *(uint64_t *)(result + 0xD0) = result + 208;
    *(uint64_t *)(result + 0x180 + 0x8) = result + 384;
    *(uint64_t *)(result + 0x180) = result + 384;
    result = RtlCreateUnicodeString(result + 40, local_rsi, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
    if ((uint8_t)(result) != 0) goto loc_007350EE;
loc_0073508C:
loc_00735091:
    result = PiDevCfgFreeDriverNode(result, local_rsi, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
loc_00735099:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
    }
    if (v_stack_m48 != 0) {
        result = ZwClose(v_stack_m48, Arg2, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
    }
    if (v_stack_p10 != 0) {
        result = ZwClose(v_stack_p10, Arg2, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
    }
    result = RtlFreeAnsiString(v_stack_m38, Arg2, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
    return (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
loc_007350EE:
    result = PnpDuplicateUnicodeString(*(uint64_t *)(v_stack_m28 + 0x48) + 56, v_stack_m38, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
    if ((uint8_t)(result) == 0) goto loc_0073508C;
    result = RtlCreateUnicodeString(*(uint64_t *)(v_stack_m28 + 0x48) + 88, 0, (uint32_t)(0x63647050ULL), (uint32_t)(0x20019ULL));
    if ((uint8_t)(result) == 0) goto loc_0073508C;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x68) = (uint32_t)((uint32_t)(Arg4));
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m48, v_rip + 3972938, Arg3, v_stack_m40);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00735142;
    result = 0;
    goto loc_007351D6;
loc_00735142:
    local_r15 = 0;
    if (sign_flag) goto loc_00735091;
    result = PnpValidateRegistryMultiSz(v_stack_m40, v_rip + 3972938, Arg3, v_stack_m40);
    if ((uint8_t)(result) != 0) goto loc_00735163;
    goto loc_00735091;
loc_00735163:
    local_rsi = ((uint32_t)(*(uint32_t *)(v_stack_m40 + 0x8))) + (v_stack_m40);
loc_0073516B:
    if ((uint16_t)(*(uint16_t *)(local_rsi)) == 0) goto loc_007351D6;
    Arg1 = (uint32_t)(((uint16_t)(*(uint16_t *)(local_rsi))) - (42));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint16_t *)(local_rsi + 0x2);
        result = 0;
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    }
    if ((uint32_t)(Arg1) == 0) goto loc_007351D2;
    if (((uint16_t)(*(uint16_t *)(local_rsi))) == 43) goto loc_0073519B;
    if (((uint16_t)(*(uint16_t *)(local_rsi))) != 45) goto loc_0073519F;
loc_0073519B:
    local_rsi = (local_rsi) + (2);
loc_0073519F:
    result = PiDevCfgGetDriverConfigurationKeyScope(local_rsi, *(uint16_t *)(local_rsi), Arg3, v_stack_m40);
    if (0 == 0) goto loc_007351B3;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x68))) | ((uint32_t)(result)));
    goto loc_007351B7;
loc_007351B3:
    result = (uint32_t)(~(result));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
loc_007351B7:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x68) = (uint32_t)(Arg1);
    result = (result) | (-1);
loc_007351BE:
    result = (result) + 1;
    if ((*(uint16_t *)(local_rsi + result * 2)) != 0) goto loc_007351BE;
    local_rsi = (local_rsi + result * 2) + (2);
    goto loc_0073516B;
loc_007351D2:
loc_007351D6:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10) = v_stack_p10;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x20) = v_stack_m48;
    result = 0;
    v_stack_p10 = 0;
    v_stack_m48 = 0;
    *(uint64_t *)(arg5) = *(uint64_t *)(v_stack_m28 + 0x48);
    goto loc_00735099;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x168` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00734D88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
