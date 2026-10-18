# PiDevCfgQueryDriverNode

- RVA: `0x0073435C`–`0x00734C9B` (길이 `2,367` bytes)
- VA: `0x000000014073435C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8C20`
- 디코드: `552`개 명령, `2,367/2,367` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **22**

### Outgoing calls
- `0x0073440A` → [PiDevCfgGetDriverPackageId](../97/PiDevCfgGetDriverPackageId_function_00977690.md) (function, `0x00977690`)
- `0x0073443E` → [PnpOpenObjectRegKey](../8E/PnpOpenObjectRegKey_function_008E15E8.md) (function, `0x008E15E8`)
- `0x00734459` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007344C0` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x0073450C` → [PipCheckComputerSupported](../72/PipCheckComputerSupported_function_007232B0.md) (function, `0x007232B0`)
- `0x00734561` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00734575` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x007345AF` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x007345C4` → [PiDevCfgFreeDriverNode](PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x007345D3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007345E2` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007345F0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007345FF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00734609` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00734612` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00734623` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0073464D` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (function, `0x004CC044`)
- `0x00734661` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x0073467D` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x00734696` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00734759` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x007347BD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00734818` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0073485E` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x007348BA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00734943` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)
- `0x00734997` → [PiDevCfgEnforceDriverPolicy](PiDevCfgEnforceDriverPolicy_function_007328C4.md) (function, `0x007328C4`)
- `0x007349D7` → [IopOpenRegistryKeyEx](../A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00734A01` → [IopOpenRegistryKeyEx](../A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00734A2C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00734A77` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x00734A95` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00734AB1` → [PiDevCfgOpenDriverConfiguration](../A9/PiDevCfgOpenDriverConfiguration_function_00A995F0.md) (function, `0x00A995F0`)
- `0x00734ADC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00734B6D` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x00734B92` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00734BC6` → [PnpRegistryValueExists](../../text/5A/PnpRegistryValueExists_function_005A81A0.md) (function, `0x005A81A0`)
- `0x00734BF0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00734C38` → [PiDevCfgQueryObjectProperties](../97/PiDevCfgQueryObjectProperties_function_0097776C.md) (function, `0x0097776C`)

### Direct callers
- [PiDevCfgFindDeviceDriver](../97/PiDevCfgFindDeviceDriver_function_0097602C.md) at `0x00976405`
- [PiDevCfgFindDeviceDriver](../97/PiDevCfgFindDeviceDriver_function_0097602C.md) at `0x0097674A`

### Static image references
- `0x0073437B` → RVA `0x00E0A740` (`.data`; read)
- `0x00734423` → RVA `0x00E66398` (`.data`; read)
- `0x00734463` → RVA `0x00022258` (`.rdata`; read)
- `0x00734480` → RVA `0x00021570` (`.rdata`; read)
- `0x007346A0` → RVA `0x00023190` (`.rdata`; read)
- `0x007346BC` → RVA `0x00020E58` (`.rdata`; read)
- `0x007346E0` → RVA `0x00011EE0` (`.rdata`; read)
- `0x00734709` → RVA `0x00020E70` (`.rdata`; read)
- `0x00734714` → RVA `0x00022DC0` (`.rdata`; read)
- `0x00734822` → RVA `0x000214F8` (`.rdata`; read)
- `0x007348C4` → RVA `0x00021398` (`.rdata`; read)
- `0x007348ED` → RVA `0x000214B8` (`.rdata`; read)
- `0x00734901` → RVA `0x00022570` (`.rdata`; read)
- `0x007349B3` → RVA `0x00AFEED0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00734A36` → RVA `0x00AFE850` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00734AE1` → RVA `0x00734D60` (`PiDevCfgQueryDriverVersionValueCallback`; read)
- `0x00734AEF` → RVA `0x00AFEEF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00734B0B` → RVA `0x00AFEE10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00734B49` → RVA `0x00AFEE30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00734B97` → RVA `0x00E0A9E0` (`.data`; read)
- `0x00734BA9` → RVA `0x00AFEE50` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00734BFA` → RVA `0x00012EF8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00734459` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00734561` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00734575` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x007345D3` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007345E2` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007345F0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007345FF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00734623` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0073464D` → [PnpDuplicateUnicodeString](../../text/4C/PnpDuplicateUnicodeString_function_004CC044.md) (`PAGE` → `.text`)
  - `0x00734696` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007347BD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00734818` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007348BA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00734A2C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00734ADC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00734BC6` → [PnpRegistryValueExists](../../text/5A/PnpRegistryValueExists_function_005A81A0.md) (`PAGE` → `.text`)
  - `0x00734BF0` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0073435C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00734361  55                              push rbp
00734362  56                              push rsi
00734363  57                              push rdi
00734364  41 54                           push r12
00734366  41 55                           push r13
00734368  41 56                           push r14
0073436A  41 57                           push r15
0073436C  48 8D AC 24 80 FE FF FF         lea rbp, [rsp - 0x180]
00734374  48 81 EC 80 02 00 00            sub rsp, 0x280
0073437B  48 8B 05 BE 63 6D 00            mov rax, qword ptr [rip + 0x6d63be]
00734382  48 33 C4                        xor rax, rsp
00734385  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
0073438C  48 8B 85 F0 01 00 00            mov rax, qword ptr [rbp + 0x1f0]
00734393  45 33 F6                        xor r14d, r14d
00734396  4C 8B E2                        mov r12, rdx
00734399  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0073439D  0F 57 C0                        xorps xmm0, xmm0
007343A0  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
007343A5  41 83 CD FF                     or r13d, 0xffffffff
007343A9  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
007343AE  48 83 CF FF                     or rdi, 0xffffffffffffffff
007343B2  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
007343B7  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
007343BC  44 88 74 24 43                  mov byte ptr [rsp + 0x43], r14b
007343C1  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
007343C5  41 8B F6                        mov esi, r14d
007343C8  4C 89 75 A8                     mov qword ptr [rbp - 0x58], r14
007343CC  4C 8B F9                        mov r15, rcx
007343CF  44 88 74 24 41                  mov byte ptr [rsp + 0x41], r14b
007343D4  44 89 6C 24 54                  mov dword ptr [rsp + 0x54], r13d
007343D9  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
007343DD  44 88 74 24 40                  mov byte ptr [rsp + 0x40], r14b
007343E2  44 88 74 24 42                  mov byte ptr [rsp + 0x42], r14b
007343E7  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
007343EC  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
007343F0  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
007343F5  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
007343FA  44 89 4D 88                     mov dword ptr [rbp - 0x78], r9d
007343FE  44 89 45 8C                     mov dword ptr [rbp - 0x74], r8d
00734402  C7 44 24 50 00 00 00 FF         mov dword ptr [rsp + 0x50], 0xff000000
0073440A  E8 81 32 24 00                  call 0x140977690
0073440F  8B D8                           mov ebx, eax
00734411  85 C0                           test eax, eax
00734413  0F 88 B0 01 00 00               js 0x1407345c9
00734419  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0073441E  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00734423  48 8B 0D 6E 1F 73 00            mov rcx, qword ptr [rip + 0x731f6e]
0073442A  45 8D 46 08                     lea r8d, [r14 + 8]
0073442E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00734433  41 B9 19 00 02 00               mov r9d, 0x20019
00734439  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
0073443E  E8 A5 D1 1A 00                  call 0x1408e15e8
00734443  8B D8                           mov ebx, eax
00734445  85 C0                           test eax, eax
00734447  0F 88 7C 01 00 00               js 0x1407345c9
0073444D  33 D2                           xor edx, edx
0073444F  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00734453  41 B8 C8 00 00 00               mov r8d, 0xc8
00734459  E8 E2 27 F9 FF                  call 0x1406c6c40
0073445E  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
00734463  48 8D 05 EE DD 8E FF            lea rax, [rip - 0x712212]
0073446A  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0073446F  45 8D 46 08                     lea r8d, [r14 + 8]
00734473  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00734477  48 8D 44 24 43                  lea rax, [rsp + 0x43]
0073447C  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00734480  48 8D 05 E9 D0 8E FF            lea rax, [rip - 0x712f17]
00734487  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0073448B  48 8D 45 A0                     lea rax, [rbp - 0x60]
0073448F  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00734493  48 8D 45 C0                     lea rax, [rbp - 0x40]
00734497  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
0073449F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007344A4  C7 45 C8 11 00 00 00            mov dword ptr [rbp - 0x38], 0x11
007344AB  C7 45 D8 01 00 00 00            mov dword ptr [rbp - 0x28], 1
007344B2  C7 45 F0 12 20 00 00            mov dword ptr [rbp - 0x10], 0x2012
007344B9  C7 45 04 06 00 00 00            mov dword ptr [rbp + 4], 6
007344C0  E8 A7 32 24 00                  call 0x14097776c
007344C5  8B D8                           mov ebx, eax
007344C7  85 C0                           test eax, eax
007344C9  0F 88 FA 00 00 00               js 0x1407345c9
007344CF  44 39 75 E0                     cmp dword ptr [rbp - 0x20], r14d
007344D3  7C 11                           jl 0x1407344e6
007344D5  40 38 7C 24 43                  cmp byte ptr [rsp + 0x43], dil
007344DA  75 0A                           jne 0x1407344e6
007344DC  BB 56 00 00 C0                  mov ebx, 0xc0000056
007344E1  E9 E3 00 00 00                  jmp 0x1407345c9
007344E6  BB 02 00 00 00                  mov ebx, 2
007344EB  44 39 75 08                     cmp dword ptr [rbp + 8], r14d
007344EF  7C 4E                           jl 0x14073453f
007344F1  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
007344F5  48 85 C0                        test rax, rax
007344F8  74 45                           je 0x14073453f
007344FA  66 39 5D A0                     cmp word ptr [rbp - 0x60], bx
007344FE  76 3F                           jbe 0x14073453f
00734500  48 8B F0                        mov rsi, rax
00734503  66 44 39 30                     cmp word ptr [rax], r14w
00734507  74 26                           je 0x14073452f
00734509  48 8B CE                        mov rcx, rsi
0073450C  E8 9F ED FE FF                  call 0x1407232b0
00734511  84 C0                           test al, al
00734513  75 1A                           jne 0x14073452f
00734515  48 8B C7                        mov rax, rdi
00734518  48 FF C0                        inc rax
0073451B  66 44 39 34 46                  cmp word ptr [rsi + rax*2], r14w
00734520  75 F6                           jne 0x140734518
00734522  48 8D 34 46                     lea rsi, [rsi + rax*2]
00734526  48 03 F3                        add rsi, rbx
00734529  66 44 39 36                     cmp word ptr [rsi], r14w
0073452D  75 DA                           jne 0x140734509
0073452F  66 44 39 36                     cmp word ptr [rsi], r14w
00734533  75 0A                           jne 0x14073453f
00734535  BB 24 04 00 C0                  mov ebx, 0xc0000424
0073453A  E9 8A 00 00 00                  jmp 0x1407345c9
0073453F  44 8B B5 E0 01 00 00            mov r14d, dword ptr [rbp + 0x1e0]
00734546  41 F6 C6 08                     test r14b, 8
0073454A  74 05                           je 0x140734551
0073454C  48 85 F6                        test rsi, rsi
0073454F  74 E4                           je 0x140734535
00734551  BA C8 01 00 00                  mov edx, 0x1c8
00734556  B9 00 01 00 00                  mov ecx, 0x100
0073455B  41 B8 50 70 64 63               mov r8d, 0x63647050
00734561  E8 8A DB 44 00                  call 0x140b820f0
00734566  48 8B F8                        mov rdi, rax
00734569  48 85 C0                        test rax, rax
0073456C  75 07                           jne 0x140734575
0073456E  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00734573  EB 54                           jmp 0x1407345c9
00734575  E8 CA 33 DC FF                  call 0x1404f7944
0073457A  85 C0                           test eax, eax
0073457C  75 0E                           jne 0x14073458c
0073457E  48 8D 87 E0 00 00 00            lea rax, [rdi + 0xe0]
00734585  48 89 40 08                     mov qword ptr [rax + 8], rax
00734589  48 89 00                        mov qword ptr [rax], rax
0073458C  48 8D 87 D0 00 00 00            lea rax, [rdi + 0xd0]
00734593  49 8B D7                        mov rdx, r15
00734596  48 89 40 08                     mov qword ptr [rax + 8], rax
0073459A  48 8D 4F 28                     lea rcx, [rdi + 0x28]
0073459E  48 89 00                        mov qword ptr [rax], rax
007345A1  48 8D 87 80 01 00 00            lea rax, [rdi + 0x180]
007345A8  48 89 40 08                     mov qword ptr [rax + 8], rax
007345AC  48 89 00                        mov qword ptr [rax], rax
007345AF  E8 AC 92 28 00                  call 0x1409bd860
007345B4  84 C0                           test al, al
007345B6  0F 85 88 00 00 00               jne 0x140734644
007345BC  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007345C1  48 8B CF                        mov rcx, rdi
007345C4  E8 8B ED FF FF                  call 0x140733354
007345C9  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007345CE  48 85 C9                        test rcx, rcx
007345D1  74 05                           je 0x1407345d8
007345D3  E8 D8 8C F7 FF                  call 0x1406ad2b0
007345D8  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
007345DD  48 85 C9                        test rcx, rcx
007345E0  74 05                           je 0x1407345e7
007345E2  E8 C9 8C F7 FF                  call 0x1406ad2b0
007345E7  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
007345EB  48 85 C9                        test rcx, rcx
007345EE  74 05                           je 0x1407345f5
007345F0  E8 BB 8C F7 FF                  call 0x1406ad2b0
007345F5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007345FA  48 85 C9                        test rcx, rcx
007345FD  74 05                           je 0x140734604
007345FF  E8 AC 8C F7 FF                  call 0x1406ad2b0
00734604  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00734609  E8 F2 C1 28 00                  call 0x1409c0800
0073460E  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00734612  E8 E9 C1 28 00                  call 0x1409c0800
00734617  8B C3                           mov eax, ebx
00734619  48 8B 8D 70 01 00 00            mov rcx, qword ptr [rbp + 0x170]
00734620  48 33 CC                        xor rcx, rsp
00734623  E8 18 80 F7 FF                  call 0x1406ac640
00734628  48 8B 9C 24 D0 02 00 00         mov rbx, qword ptr [rsp + 0x2d0]
00734630  48 81 C4 80 02 00 00            add rsp, 0x280
00734637  41 5F                           pop r15
00734639  41 5E                           pop r14
0073463B  41 5D                           pop r13
0073463D  41 5C                           pop r12
0073463F  5F                              pop rdi
00734640  5E                              pop rsi
00734641  5D                              pop rbp
00734642  C3                              ret
00734643  CC                              int3
00734644  48 8D 4F 38                     lea rcx, [rdi + 0x38]
00734648  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
0073464D  E8 F2 79 D9 FF                  call 0x1404cc044
00734652  84 C0                           test al, al
00734654  0F 84 62 FF FF FF               je 0x1407345bc
0073465A  48 8D 4F 48                     lea rcx, [rdi + 0x48]
0073465E  49 8B D4                        mov rdx, r12
00734661  E8 FA 91 28 00                  call 0x1409bd860
00734666  84 C0                           test al, al
00734668  0F 84 4E FF FF FF               je 0x1407345bc
0073466E  48 85 F6                        test rsi, rsi
00734671  74 17                           je 0x14073468a
00734673  48 8D 8F 80 00 00 00            lea rcx, [rdi + 0x80]
0073467A  48 8B D6                        mov rdx, rsi
0073467D  E8 DE 91 28 00                  call 0x1409bd860
00734682  84 C0                           test al, al
00734684  0F 84 32 FF FF FF               je 0x1407345bc
0073468A  33 D2                           xor edx, edx
0073468C  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00734690  41 B8 C8 00 00 00               mov r8d, 0xc8
00734696  E8 A5 25 F9 FF                  call 0x1406c6c40
0073469B  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
007346A0  48 8D 05 E9 EA 8E FF            lea rax, [rip - 0x711517]
007346A7  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007346AB  4C 8D 67 70                     lea r12, [rdi + 0x70]
007346AF  B9 10 00 00 00                  mov ecx, 0x10
007346B4  C7 44 24 28 05 00 00 00         mov dword ptr [rsp + 0x28], 5
007346BC  48 8D 05 95 C7 8E FF            lea rax, [rip - 0x71386b]
007346C3  89 4D C8                        mov dword ptr [rbp - 0x38], ecx
007346C6  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
007346CA  4C 8D BF BC 00 00 00            lea r15, [rdi + 0xbc]
007346D1  48 8D 47 78                     lea rax, [rdi + 0x78]
007346D5  4C 89 65 D0                     mov qword ptr [rbp - 0x30], r12
007346D9  48 89 45 F8                     mov qword ptr [rbp - 8], rax
007346DD  8D 51 F8                        lea edx, [rcx - 8]
007346E0  48 8D 05 F9 D7 8D FF            lea rax, [rip - 0x722807]
007346E7  89 55 D8                        mov dword ptr [rbp - 0x28], edx
007346EA  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
007346EE  48 8D B7 90 00 00 00            lea rsi, [rdi + 0x90]
007346F5  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007346FA  89 55 00                        mov dword ptr [rbp], edx
007346FD  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00734701  44 8B C2                        mov r8d, edx
00734704  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00734709  48 8D 05 60 C7 8E FF            lea rax, [rip - 0x7138a0]
00734710  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00734714  48 8D 05 A5 E6 8E FF            lea rax, [rip - 0x71195b]
0073471B  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0073471F  48 8D 45 C0                     lea rax, [rbp - 0x40]
00734723  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00734728  C7 45 F0 09 00 00 00            mov dword ptr [rbp - 0x10], 9
0073472F  C7 45 18 07 00 00 00            mov dword ptr [rbp + 0x18], 7
00734736  C7 45 28 04 00 00 00            mov dword ptr [rbp + 0x28], 4
0073473D  C7 45 40 0D 00 00 00            mov dword ptr [rbp + 0x40], 0xd
00734744  4C 89 7D 48                     mov qword ptr [rbp + 0x48], r15
00734748  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
0073474B  C7 45 68 0D 10 00 00            mov dword ptr [rbp + 0x68], 0x100d
00734752  48 89 75 70                     mov qword ptr [rbp + 0x70], rsi
00734756  89 5D 7C                        mov dword ptr [rbp + 0x7c], ebx
00734759  E8 0E 30 24 00                  call 0x14097776c
0073475E  33 C9                           xor ecx, ecx
00734760  8B D8                           mov ebx, eax
00734762  85 C0                           test eax, eax
00734764  0F 88 57 FE FF FF               js 0x1407345c1
0073476A  39 4D E0                        cmp dword ptr [rbp - 0x20], ecx
0073476D  7D 06                           jge 0x140734775
0073476F  33 C0                           xor eax, eax
00734771  49 89 04 24                     mov qword ptr [r12], rax
00734775  39 4D 08                        cmp dword ptr [rbp + 8], ecx
00734778  7D 06                           jge 0x140734780
0073477A  33 C0                           xor eax, eax
0073477C  48 89 47 78                     mov qword ptr [rdi + 0x78], rax
00734780  39 4D 30                        cmp dword ptr [rbp + 0x30], ecx
00734783  7D 08                           jge 0x14073478d
00734785  C7 44 24 50 00 00 00 FF         mov dword ptr [rsp + 0x50], 0xff000000
0073478D  39 4D 58                        cmp dword ptr [rbp + 0x58], ecx
00734790  7D 07                           jge 0x140734799
00734792  0F 57 C0                        xorps xmm0, xmm0
00734795  41 0F 11 07                     movups xmmword ptr [r15], xmm0
00734799  39 8D 80 00 00 00               cmp dword ptr [rbp + 0x80], ecx
0073479F  7D 05                           jge 0x1407347a6
007347A1  48 89 0E                        mov qword ptr [rsi], rcx
007347A4  EB 20                           jmp 0x1407347c6
007347A6  8B 45 78                        mov eax, dword ptr [rbp + 0x78]
007347A9  A8 0F                           test al, 0xf
007347AB  75 0B                           jne 0x1407347b8
007347AD  C1 E8 04                        shr eax, 4
007347B0  89 87 98 00 00 00               mov dword ptr [rdi + 0x98], eax
007347B6  EB 0E                           jmp 0x1407347c6
007347B8  48 8B 0E                        mov rcx, qword ptr [rsi]
007347BB  33 D2                           xor edx, edx
007347BD  E8 AE E0 44 00                  call 0x140b82870
007347C2  48 83 26 00                     and qword ptr [rsi], 0
007347C6  41 F6 C6 04                     test r14b, 4
007347CA  74 05                           je 0x1407347d1
007347CC  41 8B CD                        mov ecx, r13d
007347CF  EB 29                           jmp 0x1407347fa
007347D1  41 8B C6                        mov eax, r14d
007347D4  24 01                           and al, 1
007347D6  F6 D8                           neg al
007347D8  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
007347DB  1B C9                           sbb ecx, ecx
007347DD  25 00 00 FF 00                  and eax, 0xff0000
007347E2  81 E1 00 00 00 F1               and ecx, 0xf1000000
007347E8  81 C1 00 00 00 FF               add ecx, 0xff000000
007347EE  23 4C 24 50                     and ecx, dword ptr [rsp + 0x50]
007347F2  0B C8                           or ecx, eax
007347F4  0F B7 45 8C                     movzx eax, word ptr [rbp - 0x74]
007347F8  0B C8                           or ecx, eax
007347FA  41 BF 02 00 00 00               mov r15d, 2
00734800  89 4F 6C                        mov dword ptr [rdi + 0x6c], ecx
00734803  45 84 F7                        test r15b, r14b
00734806  0F 84 84 00 00 00               je 0x140734890
0073480C  33 D2                           xor edx, edx
0073480E  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00734812  41 B8 C8 00 00 00               mov r8d, 0xc8
00734818  E8 23 24 F9 FF                  call 0x1406c6c40
0073481D  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
00734822  48 8D 05 CF CC 8E FF            lea rax, [rip - 0x713331]
00734829  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
0073482E  45 8D 47 06                     lea r8d, [r15 + 6]
00734832  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00734836  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0073483B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0073483F  48 8D 45 C0                     lea rax, [rbp - 0x40]
00734843  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
0073484B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00734850  C7 45 C8 11 00 00 00            mov dword ptr [rbp - 0x38], 0x11
00734857  C7 45 D8 01 00 00 00            mov dword ptr [rbp - 0x28], 1
0073485E  E8 09 2F 24 00                  call 0x14097776c
00734863  45 33 F6                        xor r14d, r14d
00734866  8B D8                           mov ebx, eax
00734868  85 C0                           test eax, eax
0073486A  0F 88 51 FD FF FF               js 0x1407345c1
00734870  44 39 75 E0                     cmp dword ptr [rbp - 0x20], r14d
00734874  7D 09                           jge 0x14073487f
00734876  41 8A C6                        mov al, r14b
00734879  88 44 24 40                     mov byte ptr [rsp + 0x40], al
0073487D  EB 04                           jmp 0x140734883
0073487F  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00734883  3C FF                           cmp al, 0xff
00734885  75 0C                           jne 0x140734893
00734887  44 09 BF B8 00 00 00            or dword ptr [rdi + 0xb8], r15d
0073488E  EB 03                           jmp 0x140734893
00734890  45 33 F6                        xor r14d, r14d
00734893  48 8B B5 E8 01 00 00            mov rsi, qword ptr [rbp + 0x1e8]
0073489A  48 85 F6                        test rsi, rsi
0073489D  0F 84 0B 01 00 00               je 0x1407349ae
007348A3  8B 06                           mov eax, dword ptr [rsi]
007348A5  41 84 C7                        test r15b, al
007348A8  0F 84 00 01 00 00               je 0x1407349ae
007348AE  33 D2                           xor edx, edx
007348B0  48 8D 4D C0                     lea rcx, [rbp - 0x40]
007348B4  41 B8 C8 00 00 00               mov r8d, 0xc8
007348BA  E8 81 23 F9 FF                  call 0x1406c6c40
007348BF  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
007348C4  48 8D 05 CD CA 8E FF            lea rax, [rip - 0x713533]
007348CB  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
007348D0  B9 08 00 00 00                  mov ecx, 8
007348D5  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007348D9  44 8B C1                        mov r8d, ecx
007348DC  48 8D 44 24 41                  lea rax, [rsp + 0x41]
007348E1  C7 44 24 28 03 00 00 00         mov dword ptr [rsp + 0x28], 3
007348E9  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
007348ED  48 8D 05 C4 CB 8E FF            lea rax, [rip - 0x71343c]
007348F4  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
007348F8  48 8D 44 24 54                  lea rax, [rsp + 0x54]
007348FD  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00734901  48 8D 05 68 DC 8E FF            lea rax, [rip - 0x712398]
00734908  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0073490C  48 8D 45 90                     lea rax, [rbp - 0x70]
00734910  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00734914  48 8D 45 C0                     lea rax, [rbp - 0x40]
00734918  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0073491D  C7 45 C8 11 00 00 00            mov dword ptr [rbp - 0x38], 0x11
00734924  C7 45 D8 01 00 00 00            mov dword ptr [rbp - 0x28], 1
0073492B  C7 45 F0 07 00 00 00            mov dword ptr [rbp - 0x10], 7
00734932  C7 45 00 04 00 00 00            mov dword ptr [rbp], 4
00734939  C7 45 18 09 00 00 00            mov dword ptr [rbp + 0x18], 9
00734940  89 4D 28                        mov dword ptr [rbp + 0x28], ecx
00734943  E8 24 2E 24 00                  call 0x14097776c
00734948  8B D8                           mov ebx, eax
0073494A  85 C0                           test eax, eax
0073494C  0F 88 6F FC FF FF               js 0x1407345c1
00734952  44 39 75 E0                     cmp dword ptr [rbp - 0x20], r14d
00734956  7D 09                           jge 0x140734961
00734958  41 8A C6                        mov al, r14b
0073495B  88 44 24 41                     mov byte ptr [rsp + 0x41], al
0073495F  EB 04                           jmp 0x140734965
00734961  8A 44 24 41                     mov al, byte ptr [rsp + 0x41]
00734965  44 39 75 08                     cmp dword ptr [rbp + 8], r14d
00734969  7D 07                           jge 0x140734972
0073496B  44 89 6C 24 54                  mov dword ptr [rsp + 0x54], r13d
00734970  EB 05                           jmp 0x140734977
00734972  44 8B 6C 24 54                  mov r13d, dword ptr [rsp + 0x54]
00734977  44 39 75 30                     cmp dword ptr [rbp + 0x30], r14d
0073497B  7D 0A                           jge 0x140734987
0073497D  49 83 C8 FF                     or r8, 0xffffffffffffffff
00734981  4C 89 45 90                     mov qword ptr [rbp - 0x70], r8
00734985  EB 04                           jmp 0x14073498b
00734987  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
0073498B  3C FF                           cmp al, 0xff
0073498D  41 8B D5                        mov edx, r13d
00734990  48 8B CE                        mov rcx, rsi
00734993  41 0F 94 C1                     sete r9b
00734997  E8 28 DF FF FF                  call 0x1407328c4
0073499C  85 C0                           test eax, eax
0073499E  79 0E                           jns 0x1407349ae
007349A0  0F BA AF B8 00 00 00 09         bts dword ptr [rdi + 0xb8], 9
007349A8  89 87 C0 01 00 00               mov dword ptr [rdi + 0x1c0], eax
007349AE  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
007349B3  48 8D 05 16 A5 3C 00            lea rax, [rip + 0x3ca516]
007349BA  BE 19 00 02 00                  mov esi, 0x20019
007349BF  C7 44 24 78 16 00 18 00         mov dword ptr [rsp + 0x78], 0x180016
007349C7  44 8B CE                        mov r9d, esi
007349CA  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
007349CE  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007349D3  48 8D 4D 98                     lea rcx, [rbp - 0x68]
007349D7  E8 68 D1 31 00                  call 0x140a51b44
007349DC  41 BF 34 00 00 C0               mov r15d, 0xc0000034
007349E2  8B D8                           mov ebx, eax
007349E4  41 3B C7                        cmp eax, r15d
007349E7  74 24                           je 0x140734a0d
007349E9  85 C0                           test eax, eax
007349EB  0F 88 D0 FB FF FF               js 0x1407345c1
007349F1  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
007349F5  4C 8D 47 48                     lea r8, [rdi + 0x48]
007349F9  44 8B CE                        mov r9d, esi
007349FC  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00734A01  E8 3E D1 31 00                  call 0x140a51b44
00734A06  8B D8                           mov ebx, eax
00734A08  41 3B C7                        cmp eax, r15d
00734A0B  75 08                           jne 0x140734a15
00734A0D  41 8B DE                        mov ebx, r14d
00734A10  E9 85 00 00 00                  jmp 0x140734a9a
00734A15  85 C0                           test eax, eax
00734A17  0F 88 A4 FB FF FF               js 0x1407345c1
00734A1D  33 D2                           xor edx, edx
00734A1F  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
00734A26  41 B8 E0 00 00 00               mov r8d, 0xe0
00734A2C  E8 0F 22 F9 FF                  call 0x1406c6c40
00734A31  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00734A36  48 8D 05 13 9E 3C 00            lea rax, [rip + 0x3c9e13]
00734A3D  48 8D 77 58                     lea rsi, [rdi + 0x58]
00734A41  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
00734A48  45 33 C9                        xor r9d, r9d
00734A4B  C7 85 B0 00 00 00 00 00 00 01   mov dword ptr [rbp + 0xb0], 0x1000000
00734A55  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
00734A5C  48 89 B5 A8 00 00 00            mov qword ptr [rbp + 0xa8], rsi
00734A63  B9 00 00 00 C0                  mov ecx, 0xc0000000
00734A68  C7 85 98 00 00 00 20 01 00 00   mov dword ptr [rbp + 0x98], 0x120
00734A72  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00734A77  E8 D4 45 19 00                  call 0x1408c9050
00734A7C  8B D8                           mov ebx, eax
00734A7E  85 C0                           test eax, eax
00734A80  0F 88 3B FB FF FF               js 0x1407345c1
00734A86  66 44 39 36                     cmp word ptr [rsi], r14w
00734A8A  75 0E                           jne 0x140734a9a
00734A8C  4C 39 77 60                     cmp qword ptr [rdi + 0x60], r14
00734A90  74 08                           je 0x140734a9a
00734A92  48 8B CE                        mov rcx, rsi
00734A95  E8 66 BD 28 00                  call 0x1409c0800
00734A9A  48 8B 57 60                     mov rdx, qword ptr [rdi + 0x60]
00734A9E  48 85 D2                        test rdx, rdx
00734AA1  0F 84 F0 00 00 00               je 0x140734b97
00734AA7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00734AAC  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00734AB1  E8 3A 4B 36 00                  call 0x140a995f0
00734AB6  8B D8                           mov ebx, eax
00734AB8  41 3B C7                        cmp eax, r15d
00734ABB  75 08                           jne 0x140734ac5
00734ABD  41 8B DE                        mov ebx, r14d
00734AC0  E9 D2 00 00 00                  jmp 0x140734b97
00734AC5  85 C0                           test eax, eax
00734AC7  0F 88 F4 FA FF FF               js 0x1407345c1
00734ACD  33 D2                           xor edx, edx
00734ACF  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
00734AD6  41 B8 E0 00 00 00               mov r8d, 0xe0
00734ADC  E8 5F 21 F9 FF                  call 0x1406c6c40
00734AE1  48 8D 15 78 02 00 00            lea rdx, [rip + 0x278]
00734AE8  4C 89 A5 A8 00 00 00            mov qword ptr [rbp + 0xa8], r12
00734AEF  48 8D 05 FA A3 3C 00            lea rax, [rip + 0x3ca3fa]
00734AF6  48 89 95 90 00 00 00            mov qword ptr [rbp + 0x90], rdx
00734AFD  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
00734B04  48 8D B7 A0 00 00 00            lea rsi, [rdi + 0xa0]
00734B0B  48 8D 05 FE A2 3C 00            lea rax, [rip + 0x3ca2fe]
00734B12  48 89 95 C8 00 00 00            mov qword ptr [rbp + 0xc8], rdx
00734B19  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00734B1E  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
00734B25  48 89 85 D8 00 00 00            mov qword ptr [rbp + 0xd8], rax
00734B2C  45 33 C9                        xor r9d, r9d
00734B2F  48 8D 47 78                     lea rax, [rdi + 0x78]
00734B33  C7 85 20 01 00 00 00 00 00 07   mov dword ptr [rbp + 0x120], 0x7000000
00734B3D  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
00734B44  B9 00 00 00 C0                  mov ecx, 0xc0000000
00734B49  48 8D 05 E0 A2 3C 00            lea rax, [rip + 0x3ca2e0]
00734B50  48 89 B5 18 01 00 00            mov qword ptr [rbp + 0x118], rsi
00734B57  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00734B5E  C7 85 08 01 00 00 30 01 00 00   mov dword ptr [rbp + 0x108], 0x130
00734B68  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00734B6D  E8 DE 44 19 00                  call 0x1408c9050
00734B72  8B D8                           mov ebx, eax
00734B74  85 C0                           test eax, eax
00734B76  0F 88 45 FA FF FF               js 0x1407345c1
00734B7C  B8 02 00 00 00                  mov eax, 2
00734B81  66 39 06                        cmp word ptr [rsi], ax
00734B84  77 11                           ja 0x140734b97
00734B86  4C 39 B7 A8 00 00 00            cmp qword ptr [rdi + 0xa8], r14
00734B8D  74 08                           je 0x140734b97
00734B8F  48 8B CE                        mov rcx, rsi
00734B92  E8 69 BC 28 00                  call 0x1409c0800
00734B97  44 38 35 42 5E 6D 00            cmp byte ptr [rip + 0x6d5e42], r14b
00734B9E  0F 84 C1 00 00 00               je 0x140734c65
00734BA4  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00734BA9  48 8D 05 A0 A2 3C 00            lea rax, [rip + 0x3ca2a0]
00734BB0  C7 44 24 78 16 00 18 00         mov dword ptr [rsp + 0x78], 0x180016
00734BB8  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00734BBC  48 85 C9                        test rcx, rcx
00734BBF  74 0E                           je 0x140734bcf
00734BC1  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00734BC6  E8 D5 35 E7 FF                  call 0x1405a81a0
00734BCB  84 C0                           test al, al
00734BCD  75 07                           jne 0x140734bd6
00734BCF  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
00734BD6  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00734BDC  A8 24                           test al, 0x24
00734BDE  0F 85 81 00 00 00               jne 0x140734c65
00734BE4  33 D2                           xor edx, edx
00734BE6  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00734BEA  41 B8 C8 00 00 00               mov r8d, 0xc8
00734BF0  E8 4B 20 F9 FF                  call 0x1406c6c40
00734BF5  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
00734BFA  48 8D 05 F7 E2 8D FF            lea rax, [rip - 0x721d09]
00734C01  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00734C06  41 B8 08 00 00 00               mov r8d, 8
00734C0C  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00734C10  48 8D 44 24 42                  lea rax, [rsp + 0x42]
00734C15  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00734C19  48 8D 45 C0                     lea rax, [rbp - 0x40]
00734C1D  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00734C25  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00734C2A  C7 45 C8 11 00 00 00            mov dword ptr [rbp - 0x38], 0x11
00734C31  C7 45 D8 01 00 00 00            mov dword ptr [rbp - 0x28], 1
00734C38  E8 2F 2B 24 00                  call 0x14097776c
00734C3D  8B D8                           mov ebx, eax
00734C3F  85 C0                           test eax, eax
00734C41  0F 88 7A F9 FF FF               js 0x1407345c1
00734C47  44 39 75 E0                     cmp dword ptr [rbp - 0x20], r14d
00734C4B  7D 09                           jge 0x140734c56
00734C4D  41 8A C6                        mov al, r14b
00734C50  88 44 24 42                     mov byte ptr [rsp + 0x42], al
00734C54  EB 04                           jmp 0x140734c5a
00734C56  8A 44 24 42                     mov al, byte ptr [rsp + 0x42]
00734C5A  3C FF                           cmp al, 0xff
00734C5C  75 07                           jne 0x140734c65
00734C5E  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
00734C65  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00734C6A  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00734C6E  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00734C73  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00734C77  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00734C7C  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
00734C80  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00734C84  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00734C89  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
00734C8E  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00734C93  48 89 38                        mov qword ptr [rax], rdi
00734C96  E9 2E F9 FF FF                  jmp 0x1407345c9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgQueryDriverNode(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned int v_stack_m1B4;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned int v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned int v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned int v_stack_m22C;
    unsigned int v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned int v_stack_m264;
    unsigned int v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int8 v_stack_m275;
    unsigned __int8 v_stack_m276;
    unsigned __int8 v_stack_m277;
    unsigned __int8 v_stack_m278;
    unsigned __int64 v_stack_m290;
    unsigned __int8 v_stack_m298;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p41;
    unsigned __int64 v_stack_p42;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (640);
    result = (*(unsigned __int64 *)(v_rip + 7168958)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r14 = 0;
    v_stack_m208 = a7;
    v_stack_m258 = 0;
    v_r13 = (unsigned int)((v_r13) | (0xFFFFFFFFULL));
    v_stack_m250 = 0;
    v_rdi = (v_rdi) | (-1);
    v_stack_m270 = 0;
    v_stack_m275 = 0;
    v_stack_m218 = 0;
    v_stack_m210 = 0;
    v_stack_m277 = 0;
    v_stack_m264 = (unsigned int)(v_r13);
    v_stack_m228 = v_rdi;
    v_stack_m278 = 0;
    v_stack_m276 = 0;
    v_stack_m240 = v_xmm0;
    v_stack_m220 = 0;
    v_stack_m248 = 0;
    v_stack_m260 = 0;
    v_stack_m230 = a4;
    v_stack_m22C = a3;
    v_stack_m268 = 0xFF000000ULL;
    result = PiDevCfgGetDriverPackageId(a1, v_stack_m258, a3, a4);
    if (sign_flag) goto loc_007345C9;
    v_stack_m290 = v_stack_m270;
    v_stack_m298 = 0;
    result = PnpOpenObjectRegKey(*(unsigned __int64 *)(v_rip + 7544686), v_stack_m250, v_r14 + 8, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_007345C9;
    a2 = 0;
    result = memset(v_stack_m1F8, a2, 200, (unsigned int)(0x20019ULL));
    v_stack_m1F8 = v_rip - 7414290;
    v_stack_m1E8 = v_stack_m275;
    v_stack_m1D0 = v_rip - 7417623;
    v_stack_m1C0 = v_stack_m218;
    v_stack_m290 = 2;
    v_stack_m298 = v_stack_m1F8;
    v_stack_m1F0 = 17;
    v_stack_m1E0 = 1;
    v_stack_m1C8 = 0x2012ULL;
    v_stack_m1B4 = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_m1F8, v_stack_m250, v_r14 + 8, v_stack_m270);
    if (sign_flag) goto loc_007345C9;
    if (v_stack_m1D8 < 0) goto loc_007344E6;
    if (v_stack_m275 != ((unsigned __int8)(v_rdi))) goto loc_007344E6;
    goto loc_007345C9;
loc_007344E6:
    if (v_stack_m1B0 < 0) goto loc_0073453F;
    if (v_stack_m210 == 0) goto loc_0073453F;
    if (v_stack_m218 <= 2) goto loc_0073453F;
    if ((*(unsigned __int16 *)(v_stack_m210)) == 0) goto loc_0073452F;
loc_00734509:
    result = PipCheckComputerSupported(v_stack_m210, v_stack_m250, v_r14 + 8, v_stack_m270);
    if ((unsigned __int8)(result) != 0) goto loc_0073452F;
loc_00734518:
    result = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(v_stack_m210 + result * 2)) != 0) goto loc_00734518;
    v_rsi = (v_stack_m210 + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_rsi)) != 0) goto loc_00734509;
loc_0073452F:
    if ((*(unsigned __int16 *)(v_rsi)) != 0) goto loc_0073453F;
loc_00734535:
    goto loc_007345C9;
loc_0073453F:
    if ((((unsigned __int8)((unsigned int)(a5))) & (8)) == 0) goto loc_00734551;
    if (v_rsi == 0) goto loc_00734535;
loc_00734551:
    result = ExAllocatePool2(256, 456, (unsigned int)(0x63647050ULL), v_stack_m270);
    if (result != 0) goto loc_00734575;
    goto loc_007345C9;
loc_00734575:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(256, 456, (unsigned int)(0x63647050ULL), v_stack_m270);
    if ((unsigned int)(result) == 0) {
        result = result + 224;
        *(unsigned __int64 *)(result + 8) = result;
        *(unsigned __int64 *)(result) = result;
    }
    *(unsigned __int64 *)(result + 208 + 8) = result + 208;
    *(unsigned __int64 *)(result + 208) = result + 208;
    *(unsigned __int64 *)(result + 384 + 8) = result + 384;
    *(unsigned __int64 *)(result + 384) = result + 384;
    result = RtlCreateUnicodeString(result + 40, a1, (unsigned int)(0x63647050ULL), v_stack_m270);
    if ((unsigned __int8)(result) != 0) goto loc_00734644;
loc_007345BC:
loc_007345C1:
    result = PiDevCfgFreeDriverNode(result, a1, (unsigned int)(0x63647050ULL), v_stack_m270);
loc_007345C9:
    if (v_stack_m270 != 0) {
        result = ZwClose(v_stack_m270, a1, (unsigned int)(0x63647050ULL), v_stack_m270);
    }
    if (v_stack_m248 != 0) {
        result = ZwClose(v_stack_m248, a1, (unsigned int)(0x63647050ULL), v_stack_m270);
    }
    if (v_stack_m220 != 0) {
        result = ZwClose(v_stack_m220, a1, (unsigned int)(0x63647050ULL), v_stack_m270);
    }
    if (v_stack_m260 != 0) {
        result = ZwClose(v_stack_m260, a1, (unsigned int)(0x63647050ULL), v_stack_m270);
    }
    result = RtlFreeAnsiString(v_stack_m258, a1, (unsigned int)(0x63647050ULL), v_stack_m270);
    result = RtlFreeAnsiString(v_stack_m218, a1, (unsigned int)(0x63647050ULL), v_stack_m270);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a1, (unsigned int)(0x63647050ULL), v_stack_m270);
    v_rsp = (v_rsp) + (640);
    return result;
loc_00734644:
    result = PnpDuplicateUnicodeString(result + 56, v_stack_p60, (unsigned int)(0x63647050ULL), v_stack_m270);
    if ((unsigned __int8)(result) == 0) goto loc_007345BC;
    result = RtlCreateUnicodeString(result + 72, 0, (unsigned int)(0x63647050ULL), v_stack_m270);
    if ((unsigned __int8)(result) == 0) goto loc_007345BC;
    if (v_rsi == 0) goto loc_0073468A;
    result = RtlCreateUnicodeString(result + 128, v_rsi, (unsigned int)(0x63647050ULL), v_stack_m270);
    if ((unsigned __int8)(result) == 0) goto loc_007345BC;
loc_0073468A:
    a2 = 0;
    result = memset(v_stack_m1F8, a2, 200, v_stack_m270);
    v_stack_m1F8 = v_rip - 7410967;
    v_stack_p28 = 5;
    v_stack_m1F0 = 16;
    v_stack_m1D0 = v_rip - 7420011;
    v_stack_m1E8 = result + 112;
    v_stack_m1C0 = result + 120;
    v_stack_m1E0 = (unsigned int)(16 - 8);
    v_stack_m1A8 = v_rip - 7481351;
    v_stack_m1B8 = (unsigned int)(16 - 8);
    v_stack_m198 = v_stack_p50;
    v_stack_m180 = v_rip - 7420064;
    v_stack_m158 = v_rip - 7412059;
    v_stack_p20 = v_stack_m1F8;
    v_stack_m1C8 = 9;
    v_stack_m1A0 = 7;
    v_stack_m190 = 4;
    v_stack_m178 = 13;
    v_stack_m170 = result + 188;
    v_stack_m168 = 16;
    v_stack_m150 = 0x100DULL;
    v_stack_m148 = result + 144;
    v_stack_m13C = (unsigned int)(v_stack_p18);
    result = PiDevCfgQueryObjectProperties(16, v_stack_p68, (unsigned int)((unsigned int)(16 - 8)), v_stack_p48);
    a1 = 0;
    if (sign_flag) goto loc_007345C1;
    if (v_stack_m1D8 < 0) {
        result = 0;
        *(unsigned __int64 *)(result + 112) = 0;
    }
    if (v_stack_m1B0 < 0) {
        result = 0;
        *(unsigned __int64 *)(result + 120) = 0;
    }
    if (v_stack_m188 < 0) {
        v_stack_p50 = 0xFF000000ULL;
    }
    if (v_stack_m160 < 0) {
        *(unsigned __int64 *)(result + 188) = v_xmm0;
    }
    if (v_stack_m138 >= 0) goto loc_007347A6;
    *(unsigned __int64 *)(result + 144) = 0;
    goto loc_007347C6;
loc_007347A6:
    if ((((unsigned __int8)((unsigned int)(v_stack_m140))) & (15)) != 0) goto loc_007347B8;
    result = (unsigned int)(((unsigned int)(v_stack_m140)) >> (4));
    *(unsigned int *)(result + 152) = (unsigned int)(result);
    goto loc_007347C6;
loc_007347B8:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 144), a2, (unsigned int)((unsigned int)(16 - 8)), v_stack_p48);
loc_007347C6:
    if ((((unsigned __int8)((unsigned int)(a5))) & (4)) == 0) goto loc_007347D1;
    goto loc_007347FA;
loc_007347D1:
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (1));
    result = (unsigned __int8)(-(result));
    result = (unsigned int)(((unsigned int)(v_stack_m230)) & (0xFF0000ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) & (0xF1000000ULL));
    a1 = (unsigned int)((a1) + (0xFF000000ULL));
    a1 = (unsigned int)((a1) & (v_stack_p50));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    a1 = (unsigned int)((a1) | ((unsigned int)(v_stack_m22C)));
loc_007347FA:
    *(unsigned int *)(result + 108) = (unsigned int)(a1);
    if (((2) & ((unsigned __int8)((unsigned int)(a5)))) == 0) goto loc_00734890;
    a2 = 0;
    result = memset(v_stack_m1F8, a2, 200, v_stack_p48);
    v_stack_m1F8 = v_rip - 7418673;
    v_stack_m1E8 = v_stack_p40;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_m1F8;
    v_stack_m1F0 = 17;
    v_stack_m1E0 = 1;
    result = PiDevCfgQueryObjectProperties(v_stack_m1F8, v_stack_p68, 2 + 6, v_stack_p48);
    v_r14 = 0;
    if (sign_flag) goto loc_007345C1;
    if (v_stack_m1D8 >= 0) goto loc_0073487F;
    v_stack_p40 = 0;
    goto loc_00734883;
loc_0073487F:
loc_00734883:
    if (((unsigned __int8)(v_stack_p40)) != 255) goto loc_00734893;
    goto loc_00734893;
loc_00734890:
    v_r14 = 0;
loc_00734893:
    if (a6 == 0) goto loc_007349AE;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a6))))) == 0) goto loc_007349AE;
    a2 = 0;
    result = memset(v_stack_m1F8, a2, 200, v_stack_p48);
    v_stack_m1F8 = v_rip - 7419187;
    v_stack_p28 = 3;
    v_stack_m1E8 = v_stack_p41;
    v_stack_m1D0 = v_rip - 7418940;
    v_stack_m1C0 = v_stack_p54;
    v_stack_m1A8 = v_rip - 7414680;
    v_stack_m198 = v_stack_m228;
    v_stack_p20 = v_stack_m1F8;
    v_stack_m1F0 = 17;
    v_stack_m1E0 = 1;
    v_stack_m1C8 = 7;
    v_stack_m1B8 = 4;
    v_stack_m1A0 = 9;
    v_stack_m190 = 8;
    result = PiDevCfgQueryObjectProperties(8, v_stack_p68, 8, v_stack_p48);
    if (sign_flag) goto loc_007345C1;
    if (v_stack_m1D8 >= 0) goto loc_00734961;
    v_stack_p41 = 0;
    goto loc_00734965;
loc_00734961:
loc_00734965:
    if (v_stack_m1B0 >= 0) goto loc_00734972;
    v_stack_p54 = (unsigned int)(v_r13);
    goto loc_00734977;
loc_00734972:
loc_00734977:
    if (v_stack_m188 >= 0) goto loc_00734987;
    a3 = (8) | (-1);
    v_stack_m228 = a3;
    goto loc_0073498B;
loc_00734987:
loc_0073498B:
    a4 = (((unsigned __int8)(v_stack_p41)) == 255) ? 1 : 0;
    result = PiDevCfgEnforceDriverPolicy(a6, (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))), v_stack_m228, a4);
    if (sign_flag) {
        *(unsigned int *)(result + 448) = (unsigned int)(result);
    }
    v_stack_p78 = 0x180016ULL;
    v_stack_m238 = v_rip + 3974422;
    result = IopOpenRegistryKeyEx(v_stack_m220, v_stack_p48, v_stack_p78, (unsigned int)((unsigned int)((unsigned int)(0x20019ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734A0D;
    if (sign_flag) goto loc_007345C1;
    result = IopOpenRegistryKeyEx(v_stack_p70, v_stack_m220, result + 72, (unsigned int)((unsigned int)((unsigned int)(0x20019ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734A15;
loc_00734A0D:
    goto loc_00734A9A;
loc_00734A15:
    if (sign_flag) goto loc_007345C1;
    a2 = 0;
    result = memset(v_stack_m128, a2, 224, (unsigned int)((unsigned int)((unsigned int)(0x20019ULL))));
    v_stack_m118 = v_rip + 3972627;
    a4 = 0;
    v_stack_m108 = 0x1000000ULL;
    v_stack_m110 = result + 88;
    v_stack_m120 = 288;
    v_stack_p28 = 1;
    result = RtlpQueryRegistryValues((unsigned int)(0xC0000000ULL), v_stack_p70, v_stack_m128, a4);
    if (sign_flag) goto loc_007345C1;
    if ((*(unsigned __int16 *)(result + 88)) != 0) goto loc_00734A9A;
    if ((*(unsigned __int64 *)(result + 96)) != 0) {
        a1 = result + 88;
        result = RtlFreeAnsiString(a1, v_stack_p70, v_stack_m128, a4);
    }
    if (*(unsigned __int64 *)(result + 96) == 0) goto loc_00734B97;
    result = PiDevCfgOpenDriverConfiguration(v_stack_p48, *(unsigned __int64 *)(result + 96), v_stack_p58, a4);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00734AC5;
    goto loc_00734B97;
loc_00734AC5:
    if (sign_flag) goto loc_007345C1;
    a2 = 0;
    result = memset(v_stack_m128, a2, 224, a4);
    v_stack_m110 = result + 112;
    v_stack_m128 = v_rip + 632;
    v_stack_m118 = v_rip + 3974138;
    v_stack_mF0 = v_rip + 632;
    v_stack_mE0 = v_rip + 3973886;
    a4 = 0;
    v_stack_m98 = 0x7000000ULL;
    v_stack_mD8 = result + 120;
    v_stack_mA0 = result + 160;
    v_stack_mA8 = v_rip + 3973856;
    v_stack_mB0 = 304;
    v_stack_p28 = 1;
    result = RtlpQueryRegistryValues((unsigned int)(0xC0000000ULL), v_stack_p58, v_stack_m128, a4);
    if (sign_flag) goto loc_007345C1;
    if ((*(unsigned __int16 *)(result + 160)) > 2) goto loc_00734B97;
    result = 2;
    if ((*(unsigned __int64 *)(result + 168)) != 0) {
        a1 = result + 160;
        result = RtlFreeAnsiString(a1, v_stack_p58, v_stack_m128, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 7167554)) == 0) goto loc_00734C65;
    v_stack_p78 = 0x180016ULL;
    v_stack_m238 = v_rip + 3973792;
    if (v_stack_p58 == 0) goto loc_00734BCF;
    result = PnpRegistryValueExists(v_stack_p58, v_stack_p78, v_stack_m128, a4);
    if ((unsigned __int8)(result) == 0) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 184)))) & (36)) != 0) goto loc_00734C65;
    a2 = 0;
    result = memset(v_stack_m1F8, a2, 200, a4);
    v_stack_m1F8 = v_rip - 7478537;
    v_stack_m1E8 = v_stack_p42;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_m1F8;
    v_stack_m1F0 = 17;
    v_stack_m1E0 = 1;
    result = PiDevCfgQueryObjectProperties(v_stack_m1F8, v_stack_p68, 8, v_stack_p48);
    if (sign_flag) goto loc_007345C1;
    if (v_stack_m1D8 >= 0) goto loc_00734C56;
    v_stack_p42 = 0;
    goto loc_00734C5A;
loc_00734C56:
loc_00734C5A:
    if (((unsigned __int8)(v_stack_p42)) == 255) {
    }
    *(unsigned __int64 *)(result + 16) = v_stack_p48;
    *(unsigned __int64 *)(result + 24) = v_stack_p70;
    *(unsigned __int64 *)(result + 32) = v_stack_p58;
    v_stack_p48 = 0;
    v_stack_p70 = 0;
    v_stack_p58 = 0;
    *(unsigned __int64 *)(v_stack_m208) = result;
    goto loc_007345C9;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgQueryDriverNode(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint32_t v_stack_m1B4;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint32_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint32_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint32_t v_stack_m22C;
    uint32_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint32_t v_stack_m264;
    uint32_t v_stack_m268;
    uint64_t v_stack_m270;
    uint8_t v_stack_m275;
    uint8_t v_stack_m276;
    uint8_t v_stack_m277;
    uint8_t v_stack_m278;
    uint64_t v_stack_m290;
    uint8_t v_stack_m298;
    uint64_t v_stack_m48;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p40;
    uint64_t v_stack_p41;
    uint64_t v_stack_p42;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p54;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (640);
    result = (*(uint64_t *)(v_rip + 0x6D63BE)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r14 = 0;
    v_stack_m208 = Arg7;
    v_stack_m258 = 0;
    local_r13 = (uint32_t)((local_r13) | (0xFFFFFFFFULL));
    v_stack_m250 = 0;
    local_rdi = (local_rdi) | (-1);
    v_stack_m270 = 0;
    v_stack_m275 = 0;
    v_stack_m218 = 0;
    v_stack_m210 = 0;
    v_stack_m277 = 0;
    v_stack_m264 = (uint32_t)(local_r13);
    v_stack_m228 = local_rdi;
    v_stack_m278 = 0;
    v_stack_m276 = 0;
    v_stack_m240 = v_xmm0;
    v_stack_m220 = 0;
    v_stack_m248 = 0;
    v_stack_m260 = 0;
    v_stack_m230 = Arg4;
    v_stack_m22C = Arg3;
    v_stack_m268 = 0xFF000000ULL;
    result = PiDevCfgGetDriverPackageId(Arg1, v_stack_m258, Arg3, Arg4);
    if (sign_flag) goto loc_007345C9;
    v_stack_m290 = v_stack_m270;
    v_stack_m298 = 0;
    result = PnpOpenObjectRegKey(*(uint64_t *)(v_rip + 0x731F6E), v_stack_m250, local_r14 + 8, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_007345C9;
    Arg2 = 0;
    result = memset(v_stack_m1F8, Arg2, 200, (uint32_t)(0x20019ULL));
    v_stack_m1F8 = v_rip - 7414290;
    v_stack_m1E8 = v_stack_m275;
    v_stack_m1D0 = v_rip - 7417623;
    v_stack_m1C0 = v_stack_m218;
    v_stack_m290 = 2;
    v_stack_m298 = v_stack_m1F8;
    v_stack_m1F0 = 17;
    v_stack_m1E0 = 1;
    v_stack_m1C8 = 0x2012ULL;
    v_stack_m1B4 = 6;
    result = PiDevCfgQueryObjectProperties(v_stack_m1F8, v_stack_m250, local_r14 + 8, v_stack_m270);
    if (sign_flag) goto loc_007345C9;
    if (v_stack_m1D8 < 0) goto loc_007344E6;
    if (v_stack_m275 != ((uint8_t)(local_rdi))) goto loc_007344E6;
    goto loc_007345C9;
loc_007344E6:
    if (v_stack_m1B0 < 0) goto loc_0073453F;
    if (v_stack_m210 == 0) goto loc_0073453F;
    if (v_stack_m218 <= 2) goto loc_0073453F;
    if ((*(uint16_t *)(v_stack_m210)) == 0) goto loc_0073452F;
loc_00734509:
    result = PipCheckComputerSupported(v_stack_m210, v_stack_m250, local_r14 + 8, v_stack_m270);
    if ((uint8_t)(result) != 0) goto loc_0073452F;
loc_00734518:
    result = (local_rdi) + 1;
    if ((*(uint16_t *)(v_stack_m210 + result * 2)) != 0) goto loc_00734518;
    local_rsi = (v_stack_m210 + result * 2) + (2);
    if ((*(uint16_t *)(local_rsi)) != 0) goto loc_00734509;
loc_0073452F:
    if ((*(uint16_t *)(local_rsi)) != 0) goto loc_0073453F;
loc_00734535:
    goto loc_007345C9;
loc_0073453F:
    if ((((uint8_t)((uint32_t)(Arg5))) & (8)) == 0) goto loc_00734551;
    if (local_rsi == 0) goto loc_00734535;
loc_00734551:
    result = ExAllocatePool2(256, 456, (uint32_t)(0x63647050ULL), v_stack_m270);
    if (result != 0) goto loc_00734575;
    goto loc_007345C9;
loc_00734575:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(256, 456, (uint32_t)(0x63647050ULL), v_stack_m270);
    if ((uint32_t)(result) == 0) {
        result = result + 224;
        *(uint64_t *)(result + 0x8) = result;
        *(uint64_t *)(result) = result;
    }
    *(uint64_t *)(result + 0xD0 + 0x8) = result + 208;
    *(uint64_t *)(result + 0xD0) = result + 208;
    *(uint64_t *)(result + 0x180 + 0x8) = result + 384;
    *(uint64_t *)(result + 0x180) = result + 384;
    result = RtlCreateUnicodeString(result + 40, Arg1, (uint32_t)(0x63647050ULL), v_stack_m270);
    if ((uint8_t)(result) != 0) goto loc_00734644;
loc_007345BC:
loc_007345C1:
    result = PiDevCfgFreeDriverNode(result, Arg1, (uint32_t)(0x63647050ULL), v_stack_m270);
loc_007345C9:
    if (v_stack_m270 != 0) {
        result = ZwClose(v_stack_m270, Arg1, (uint32_t)(0x63647050ULL), v_stack_m270);
    }
    if (v_stack_m248 != 0) {
        result = ZwClose(v_stack_m248, Arg1, (uint32_t)(0x63647050ULL), v_stack_m270);
    }
    if (v_stack_m220 != 0) {
        result = ZwClose(v_stack_m220, Arg1, (uint32_t)(0x63647050ULL), v_stack_m270);
    }
    if (v_stack_m260 != 0) {
        result = ZwClose(v_stack_m260, Arg1, (uint32_t)(0x63647050ULL), v_stack_m270);
    }
    result = RtlFreeAnsiString(v_stack_m258, Arg1, (uint32_t)(0x63647050ULL), v_stack_m270);
    result = RtlFreeAnsiString(v_stack_m218, Arg1, (uint32_t)(0x63647050ULL), v_stack_m270);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1, (uint32_t)(0x63647050ULL), v_stack_m270);
    local_rsp = (local_rsp) + (640);
    return result;
loc_00734644:
    result = PnpDuplicateUnicodeString(result + 56, v_stack_p60, (uint32_t)(0x63647050ULL), v_stack_m270);
    if ((uint8_t)(result) == 0) goto loc_007345BC;
    result = RtlCreateUnicodeString(result + 72, 0, (uint32_t)(0x63647050ULL), v_stack_m270);
    if ((uint8_t)(result) == 0) goto loc_007345BC;
    if (local_rsi == 0) goto loc_0073468A;
    result = RtlCreateUnicodeString(result + 128, local_rsi, (uint32_t)(0x63647050ULL), v_stack_m270);
    if ((uint8_t)(result) == 0) goto loc_007345BC;
loc_0073468A:
    Arg2 = 0;
    result = memset(v_stack_m1F8, Arg2, 200, v_stack_m270);
    v_stack_m1F8 = v_rip - 7410967;
    v_stack_p28 = 5;
    v_stack_m1F0 = 16;
    v_stack_m1D0 = v_rip - 7420011;
    v_stack_m1E8 = result + 112;
    v_stack_m1C0 = result + 120;
    v_stack_m1E0 = (uint32_t)(16 - 8);
    v_stack_m1A8 = v_rip - 7481351;
    v_stack_m1B8 = (uint32_t)(16 - 8);
    v_stack_m198 = v_stack_p50;
    v_stack_m180 = v_rip - 7420064;
    v_stack_m158 = v_rip - 7412059;
    v_stack_p20 = v_stack_m1F8;
    v_stack_m1C8 = 9;
    v_stack_m1A0 = 7;
    v_stack_m190 = 4;
    v_stack_m178 = 13;
    v_stack_m170 = result + 188;
    v_stack_m168 = 16;
    v_stack_m150 = 0x100DULL;
    v_stack_m148 = result + 144;
    v_stack_m13C = (uint32_t)(v_stack_p18);
    result = PiDevCfgQueryObjectProperties(16, v_stack_p68, (uint32_t)((uint32_t)(16 - 8)), v_stack_p48);
    Arg1 = 0;
    if (sign_flag) goto loc_007345C1;
    if (v_stack_m1D8 < 0) {
        result = 0;
        *(uint64_t *)(result + 0x70) = 0;
    }
    if (v_stack_m1B0 < 0) {
        result = 0;
        *(uint64_t *)(result + 0x78) = 0;
    }
    if (v_stack_m188 < 0) {
        v_stack_p50 = 0xFF000000ULL;
    }
    if (v_stack_m160 < 0) {
        *(uint64_t *)(result + 0xBC) = v_xmm0;
    }
    if (v_stack_m138 >= 0) goto loc_007347A6;
    *(uint64_t *)(result + 0x90) = 0;
    goto loc_007347C6;
loc_007347A6:
    if ((((uint8_t)((uint32_t)(v_stack_m140))) & (15)) != 0) goto loc_007347B8;
    result = (uint32_t)(((uint32_t)(v_stack_m140)) >> (4));
    *(uint32_t *)(result + 0x98) = (uint32_t)(result);
    goto loc_007347C6;
loc_007347B8:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(result + 0x90), Arg2, (uint32_t)((uint32_t)(16 - 8)), v_stack_p48);
loc_007347C6:
    if ((((uint8_t)((uint32_t)(Arg5))) & (4)) == 0) goto loc_007347D1;
    goto loc_007347FA;
loc_007347D1:
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (1));
    result = (uint8_t)(-(result));
    result = (uint32_t)(((uint32_t)(v_stack_m230)) & (0xFF0000ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) & (0xF1000000ULL));
    Arg1 = (uint32_t)((Arg1) + (0xFF000000ULL));
    Arg1 = (uint32_t)((Arg1) & (v_stack_p50));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(v_stack_m22C)));
loc_007347FA:
    *(uint32_t *)(result + 0x6C) = (uint32_t)(Arg1);
    if (((2) & ((uint8_t)((uint32_t)(Arg5)))) == 0) goto loc_00734890;
    Arg2 = 0;
    result = memset(v_stack_m1F8, Arg2, 200, v_stack_p48);
    v_stack_m1F8 = v_rip - 7418673;
    v_stack_m1E8 = v_stack_p40;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_m1F8;
    v_stack_m1F0 = 17;
    v_stack_m1E0 = 1;
    result = PiDevCfgQueryObjectProperties(v_stack_m1F8, v_stack_p68, 2 + 6, v_stack_p48);
    local_r14 = 0;
    if (sign_flag) goto loc_007345C1;
    if (v_stack_m1D8 >= 0) goto loc_0073487F;
    v_stack_p40 = 0;
    goto loc_00734883;
loc_0073487F:
loc_00734883:
    if (((uint8_t)(v_stack_p40)) != 255) goto loc_00734893;
    goto loc_00734893;
loc_00734890:
    local_r14 = 0;
loc_00734893:
    if (Arg6 == 0) goto loc_007349AE;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg6))))) == 0) goto loc_007349AE;
    Arg2 = 0;
    result = memset(v_stack_m1F8, Arg2, 200, v_stack_p48);
    v_stack_m1F8 = v_rip - 7419187;
    v_stack_p28 = 3;
    v_stack_m1E8 = v_stack_p41;
    v_stack_m1D0 = v_rip - 7418940;
    v_stack_m1C0 = v_stack_p54;
    v_stack_m1A8 = v_rip - 7414680;
    v_stack_m198 = v_stack_m228;
    v_stack_p20 = v_stack_m1F8;
    v_stack_m1F0 = 17;
    v_stack_m1E0 = 1;
    v_stack_m1C8 = 7;
    v_stack_m1B8 = 4;
    v_stack_m1A0 = 9;
    v_stack_m190 = 8;
    result = PiDevCfgQueryObjectProperties(8, v_stack_p68, 8, v_stack_p48);
    if (sign_flag) goto loc_007345C1;
    if (v_stack_m1D8 >= 0) goto loc_00734961;
    v_stack_p41 = 0;
    goto loc_00734965;
loc_00734961:
loc_00734965:
    if (v_stack_m1B0 >= 0) goto loc_00734972;
    v_stack_p54 = (uint32_t)(local_r13);
    goto loc_00734977;
loc_00734972:
loc_00734977:
    if (v_stack_m188 >= 0) goto loc_00734987;
    Arg3 = (8) | (-1);
    v_stack_m228 = Arg3;
    goto loc_0073498B;
loc_00734987:
loc_0073498B:
    Arg4 = (((uint8_t)(v_stack_p41)) == 255) ? 1 : 0;
    result = PiDevCfgEnforceDriverPolicy(Arg6, (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))), v_stack_m228, Arg4);
    if (sign_flag) {
        *(uint32_t *)(result + 0x1C0) = (uint32_t)(result);
    }
    v_stack_p78 = 0x180016ULL;
    v_stack_m238 = v_rip + 3974422;
    result = IopOpenRegistryKeyEx(v_stack_m220, v_stack_p48, v_stack_p78, (uint32_t)((uint32_t)((uint32_t)(0x20019ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734A0D;
    if (sign_flag) goto loc_007345C1;
    result = IopOpenRegistryKeyEx(v_stack_p70, v_stack_m220, result + 72, (uint32_t)((uint32_t)((uint32_t)(0x20019ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734A15;
loc_00734A0D:
    goto loc_00734A9A;
loc_00734A15:
    if (sign_flag) goto loc_007345C1;
    Arg2 = 0;
    result = memset(v_stack_m128, Arg2, 224, (uint32_t)((uint32_t)((uint32_t)(0x20019ULL))));
    v_stack_m118 = v_rip + 3972627;
    Arg4 = 0;
    v_stack_m108 = 0x1000000ULL;
    v_stack_m110 = result + 88;
    v_stack_m120 = 288;
    v_stack_p28 = 1;
    result = RtlpQueryRegistryValues((uint32_t)(0xC0000000ULL), v_stack_p70, v_stack_m128, Arg4);
    if (sign_flag) goto loc_007345C1;
    if ((*(uint16_t *)(result + 0x58)) != 0) goto loc_00734A9A;
    if ((*(uint64_t *)(result + 0x60)) != 0) {
        Arg1 = result + 88;
        result = RtlFreeAnsiString(Arg1, v_stack_p70, v_stack_m128, Arg4);
    }
    if (*(uint64_t *)(result + 0x60) == 0) goto loc_00734B97;
    result = PiDevCfgOpenDriverConfiguration(v_stack_p48, *(uint64_t *)(result + 0x60), v_stack_p58, Arg4);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00734AC5;
    goto loc_00734B97;
loc_00734AC5:
    if (sign_flag) goto loc_007345C1;
    Arg2 = 0;
    result = memset(v_stack_m128, Arg2, 224, Arg4);
    v_stack_m110 = result + 112;
    v_stack_m128 = v_rip + 632;
    v_stack_m118 = v_rip + 3974138;
    v_stack_mF0 = v_rip + 632;
    v_stack_mE0 = v_rip + 3973886;
    Arg4 = 0;
    v_stack_m98 = 0x7000000ULL;
    v_stack_mD8 = result + 120;
    v_stack_mA0 = result + 160;
    v_stack_mA8 = v_rip + 3973856;
    v_stack_mB0 = 304;
    v_stack_p28 = 1;
    result = RtlpQueryRegistryValues((uint32_t)(0xC0000000ULL), v_stack_p58, v_stack_m128, Arg4);
    if (sign_flag) goto loc_007345C1;
    if ((*(uint16_t *)(result + 0xA0)) > 2) goto loc_00734B97;
    result = 2;
    if ((*(uint64_t *)(result + 0xA8)) != 0) {
        Arg1 = result + 160;
        result = RtlFreeAnsiString(Arg1, v_stack_p58, v_stack_m128, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0x6D5E42)) == 0) goto loc_00734C65;
    v_stack_p78 = 0x180016ULL;
    v_stack_m238 = v_rip + 3973792;
    if (v_stack_p58 == 0) goto loc_00734BCF;
    result = PnpRegistryValueExists(v_stack_p58, v_stack_p78, v_stack_m128, Arg4);
    if ((uint8_t)(result) == 0) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))) & (36)) != 0) goto loc_00734C65;
    Arg2 = 0;
    result = memset(v_stack_m1F8, Arg2, 200, Arg4);
    v_stack_m1F8 = v_rip - 7478537;
    v_stack_m1E8 = v_stack_p42;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_m1F8;
    v_stack_m1F0 = 17;
    v_stack_m1E0 = 1;
    result = PiDevCfgQueryObjectProperties(v_stack_m1F8, v_stack_p68, 8, v_stack_p48);
    if (sign_flag) goto loc_007345C1;
    if (v_stack_m1D8 >= 0) goto loc_00734C56;
    v_stack_p42 = 0;
    goto loc_00734C5A;
loc_00734C56:
loc_00734C5A:
    if (((uint8_t)(v_stack_p42)) == 255) {
    }
    *(uint64_t *)(result + 0x10) = v_stack_p48;
    *(uint64_t *)(result + 0x18) = v_stack_p70;
    *(uint64_t *)(result + 0x20) = v_stack_p58;
    v_stack_p48 = 0;
    v_stack_p70 = 0;
    v_stack_p58 = 0;
    *(uint64_t *)(v_stack_m208) = result;
    goto loc_007345C9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0073435C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
