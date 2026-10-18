# PiDevCfgResolveVariableKeyHandle

- RVA: `0x00AB2A24`–`0x00AB3152` (길이 `1,838` bytes)
- VA: `0x0000000140AB2A24`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC994`
- 디코드: `492`개 명령, `1,838/1,838` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00AB2AA0` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00AB2AB7` → [PnpValidateRegistryString](../../text/4B/PnpValidateRegistryString_function_004B763C.md) (function, `0x004B763C`)
- `0x00AB2AF2` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00AB2B43` → [_CmOpenDeviceRegKey](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x00AB2B9D` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00AB2BD1` → [PnpCtxOpenContextBaseKey](../96/PnpCtxOpenContextBaseKey_function_00962A0C.md) (function, `0x00962A0C`)
- `0x00AB2BF3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00AB2C0C` → [IopOpenRegistryKeyEx](../A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00AB2C20` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00AB2C47` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00AB2C6D` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00AB2C89` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00AB2CBC` → [IopOpenRegistryKeyEx](../A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00AB2CD0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AB2CEC` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00AB2D03` → [PnpValidateRegistryString](../../text/4B/PnpValidateRegistryString_function_004B763C.md) (function, `0x004B763C`)
- `0x00AB2D27` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x00AB2D41` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x00AB2D6D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AB2DB4` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x00AB2E04` → [PiDevCfgResolveVariable](../A8/PiDevCfgResolveVariable_function_00A81AB8.md) (function, `0x00A81AB8`)
- `0x00AB2EB7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AB2EC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AB2ED5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00AB2EE3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00AB2F23` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AB2F7B` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x00AB3033` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AB30BF` → [PnpRegSzToString](../A5/PnpRegSzToString_function_00A5DC40.md) (function, `0x00A5DC40`)
- `0x00AB30F8` → [IopOpenRegistryKeyEx](../A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00AB313A` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)

### Direct callers
- [PiDevCfgResolveVariableKeyCopy](../73/PiDevCfgResolveVariableKeyCopy_function_007360D0.md) at `0x007360FA`
- [PiDevCfgResolveVariableKeyValue](../73/PiDevCfgResolveVariableKeyValue_function_007361B0.md) at `0x007361E8`

### Static image references
- `0x00AB2A40` → RVA `0x00E0A740` (`.data`; read)
- `0x00AB2A7B` → RVA `0x00AFF4F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AB2ADC` → RVA `0x00B4D840` (`PAGE`; read)
- `0x00AB2B20` → RVA `0x00E66398` (`.data`; read)
- `0x00AB2C3D` → RVA `0x00AFF500` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AB2C5A` → RVA `0x00AFF510` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AB2C63` → RVA `0x00AFF430` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AB2C76` → RVA `0x00AFF450` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AB2C7F` → RVA `0x00AFF490` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AB2C96` → RVA `0x00AFF4B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AB2CE2` → RVA `0x00AFF550` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x00AB2AB7` → [PnpValidateRegistryString](../../text/4B/PnpValidateRegistryString_function_004B763C.md) (`PAGE` → `.text`)
  - `0x00AB2AF2` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00AB2BF3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00AB2C20` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00AB2C47` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00AB2C6D` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00AB2C89` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00AB2CD0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AB2D03` → [PnpValidateRegistryString](../../text/4B/PnpValidateRegistryString_function_004B763C.md) (`PAGE` → `.text`)
  - `0x00AB2D27` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x00AB2D41` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x00AB2D6D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AB2DB4` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x00AB2EB7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AB2EC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AB2ED5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00AB2EE3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00AB2F23` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AB2F7B` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x00AB3033` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AB313A` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB2A24  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00AB2A29  55                              push rbp
00AB2A2A  56                              push rsi
00AB2A2B  57                              push rdi
00AB2A2C  41 54                           push r12
00AB2A2E  41 55                           push r13
00AB2A30  41 56                           push r14
00AB2A32  41 57                           push r15
00AB2A34  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
00AB2A39  48 81 EC 20 01 00 00            sub rsp, 0x120
00AB2A40  48 8B 05 F9 7C 35 00            mov rax, qword ptr [rip + 0x357cf9]
00AB2A47  48 33 C4                        xor rax, rsp
00AB2A4A  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00AB2A4E  33 FF                           xor edi, edi
00AB2A50  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
00AB2A54  4C 8B FA                        mov r15, rdx
00AB2A57  49 89 38                        mov qword ptr [r8], rdi
00AB2A5A  4C 8B E9                        mov r13, rcx
00AB2A5D  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00AB2A62  0F 57 C0                        xorps xmm0, xmm0
00AB2A65  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00AB2A6A  45 33 C0                        xor r8d, r8d
00AB2A6D  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00AB2A72  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00AB2A77  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
00AB2A7B  48 8D 15 6E CA 04 00            lea rdx, [rip + 0x4ca6e]
00AB2A82  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
00AB2A86  49 8B CF                        mov rcx, r15
00AB2A89  89 7D 80                        mov dword ptr [rbp - 0x80], edi
00AB2A8C  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00AB2A91  89 7D 84                        mov dword ptr [rbp - 0x7c], edi
00AB2A94  44 8B E7                        mov r12d, edi
00AB2A97  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00AB2A9C  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
00AB2AA0  E8 47 66 EE FF                  call 0x1409990ec
00AB2AA5  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00AB2AAA  8B D8                           mov ebx, eax
00AB2AAC  85 C0                           test eax, eax
00AB2AAE  0F 88 08 04 00 00               js 0x140ab2ebc
00AB2AB4  49 8B CE                        mov rcx, r14
00AB2AB7  E8 80 4B A0 FF                  call 0x1404b763c
00AB2ABC  84 C0                           test al, al
00AB2ABE  75 0A                           jne 0x140ab2aca
00AB2AC0  BB 01 00 00 C0                  mov ebx, 0xc0000001
00AB2AC5  E9 F2 03 00 00                  jmp 0x140ab2ebc
00AB2ACA  41 8B 5E 08                     mov ebx, dword ptr [r14 + 8]
00AB2ACE  8B F7                           mov esi, edi
00AB2AD0  49 03 DE                        add rbx, r14
00AB2AD3  83 FE 07                        cmp esi, 7
00AB2AD6  0F 83 61 01 00 00               jae 0x140ab2c3d
00AB2ADC  48 8D 0D 5D AD 09 00            lea rcx, [rip + 0x9ad5d]
00AB2AE3  8B FE                           mov edi, esi
00AB2AE5  48 C1 E7 05                     shl rdi, 5
00AB2AE9  48 8B D3                        mov rdx, rbx
00AB2AEC  48 03 F9                        add rdi, rcx
00AB2AEF  48 8B 0F                        mov rcx, qword ptr [rdi]
00AB2AF2  E8 89 D5 A4 FF                  call 0x140500080
00AB2AF7  85 C0                           test eax, eax
00AB2AF9  74 04                           je 0x140ab2aff
00AB2AFB  FF C6                           inc esi
00AB2AFD  EB D4                           jmp 0x140ab2ad3
00AB2AFF  33 F6                           xor esi, esi
00AB2B01  48 85 FF                        test rdi, rdi
00AB2B04  0F 84 33 01 00 00               je 0x140ab2c3d
00AB2B0A  44 8B 47 10                     mov r8d, dword ptr [rdi + 0x10]
00AB2B0E  49 8B 55 00                     mov rdx, qword ptr [r13]
00AB2B12  45 85 C0                        test r8d, r8d
00AB2B15  74 36                           je 0x140ab2b4d
00AB2B17  48 8B 52 30                     mov rdx, qword ptr [rdx + 0x30]
00AB2B1B  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00AB2B20  48 8B 0D 71 38 3B 00            mov rcx, qword ptr [rip + 0x3b3871]
00AB2B27  33 FF                           xor edi, edi
00AB2B29  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AB2B2E  45 33 C9                        xor r9d, r9d
00AB2B31  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AB2B36  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00AB2B3B  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00AB2B43  E8 F8 B9 E3 FF                  call 0x1408ee540
00AB2B48  E9 74 01 00 00                  jmp 0x140ab2cc1
00AB2B4D  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
00AB2B50  85 C0                           test eax, eax
00AB2B52  0F 84 DB 00 00 00               je 0x140ab2c33
00AB2B58  83 F8 07                        cmp eax, 7
00AB2B5B  74 06                           je 0x140ab2b63
00AB2B5D  48 8B 77 18                     mov rsi, qword ptr [rdi + 0x18]
00AB2B61  EB 5B                           jmp 0x140ab2bbe
00AB2B63  48 8B 0D 2E 38 3B 00            mov rcx, qword ptr [rip + 0x3b382e]
00AB2B6A  48 8D 45 80                     lea rax, [rbp - 0x80]
00AB2B6E  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00AB2B72  41 B9 09 00 00 00               mov r9d, 9
00AB2B78  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AB2B7D  45 33 C0                        xor r8d, r8d
00AB2B80  48 8D 45 C0                     lea rax, [rbp - 0x40]
00AB2B84  C7 45 80 4E 00 00 00            mov dword ptr [rbp - 0x80], 0x4e
00AB2B8B  48 8B 52 30                     mov rdx, qword ptr [rdx + 0x30]
00AB2B8F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AB2B94  48 8D 45 84                     lea rax, [rbp - 0x7c]
00AB2B98  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB2B9D  E8 CE AC E3 FF                  call 0x1408ed870
00AB2BA2  8B D8                           mov ebx, eax
00AB2BA4  85 C0                           test eax, eax
00AB2BA6  0F 88 10 03 00 00               js 0x140ab2ebc
00AB2BAC  83 7D 84 01                     cmp dword ptr [rbp - 0x7c], 1
00AB2BB0  0F 85 0A FF FF FF               jne 0x140ab2ac0
00AB2BB6  66 89 75 0C                     mov word ptr [rbp + 0xc], si
00AB2BBA  48 8D 75 C0                     lea rsi, [rbp - 0x40]
00AB2BBE  8B 57 0C                        mov edx, dword ptr [rdi + 0xc]
00AB2BC1  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00AB2BC6  41 B9 19 00 02 00               mov r9d, 0x20019
00AB2BCC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB2BD1  E8 36 FE EA FF                  call 0x140962a0c
00AB2BD6  33 FF                           xor edi, edi
00AB2BD8  8B D8                           mov ebx, eax
00AB2BDA  85 C0                           test eax, eax
00AB2BDC  0F 88 DA 02 00 00               js 0x140ab2ebc
00AB2BE2  48 85 F6                        test rsi, rsi
00AB2BE5  0F 84 E0 00 00 00               je 0x140ab2ccb
00AB2BEB  48 8B D6                        mov rdx, rsi
00AB2BEE  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AB2BF3  E8 88 7B 97 FF                  call 0x14042a780
00AB2BF8  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00AB2BFD  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AB2C02  41 B9 19 00 02 00               mov r9d, 0x20019
00AB2C08  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00AB2C0C  E8 33 EF F9 FF                  call 0x140a51b44
00AB2C11  8B D8                           mov ebx, eax
00AB2C13  85 C0                           test eax, eax
00AB2C15  0F 88 A1 02 00 00               js 0x140ab2ebc
00AB2C1B  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AB2C20  E8 8B A6 BF FF                  call 0x1406ad2b0
00AB2C25  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00AB2C29  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AB2C2E  E9 98 00 00 00                  jmp 0x140ab2ccb
00AB2C33  BB E5 00 00 C0                  mov ebx, 0xc00000e5
00AB2C38  E9 7F 02 00 00                  jmp 0x140ab2ebc
00AB2C3D  48 8D 15 BC C8 04 00            lea rdx, [rip + 0x4c8bc]
00AB2C44  48 8B CB                        mov rcx, rbx
00AB2C47  E8 34 D4 A4 FF                  call 0x140500080
00AB2C4C  33 FF                           xor edi, edi
00AB2C4E  85 C0                           test eax, eax
00AB2C50  75 11                           jne 0x140ab2c63
00AB2C52  C7 44 24 60 30 00 32 00         mov dword ptr [rsp + 0x60], 0x320030
00AB2C5A  48 8D 05 AF C8 04 00            lea rax, [rip + 0x4c8af]
00AB2C61  EB 42                           jmp 0x140ab2ca5
00AB2C63  48 8D 15 C6 C7 04 00            lea rdx, [rip + 0x4c7c6]
00AB2C6A  48 8B CB                        mov rcx, rbx
00AB2C6D  E8 0E D4 A4 FF                  call 0x140500080
00AB2C72  85 C0                           test eax, eax
00AB2C74  75 09                           jne 0x140ab2c7f
00AB2C76  48 8D 05 D3 C7 04 00            lea rax, [rip + 0x4c7d3]
00AB2C7D  EB 1E                           jmp 0x140ab2c9d
00AB2C7F  48 8D 15 0A C8 04 00            lea rdx, [rip + 0x4c80a]
00AB2C86  48 8B CB                        mov rcx, rbx
00AB2C89  E8 F2 D3 A4 FF                  call 0x140500080
00AB2C8E  85 C0                           test eax, eax
00AB2C90  0F 85 97 04 00 00               jne 0x140ab312d
00AB2C96  48 8D 05 13 C8 04 00            lea rax, [rip + 0x4c813]
00AB2C9D  C7 44 24 60 34 00 36 00         mov dword ptr [rsp + 0x60], 0x360034
00AB2CA5  41 B9 19 00 02 00               mov r9d, 0x20019
00AB2CAB  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00AB2CB0  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AB2CB5  33 D2                           xor edx, edx
00AB2CB7  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00AB2CBC  E8 83 EE F9 FF                  call 0x140a51b44
00AB2CC1  8B D8                           mov ebx, eax
00AB2CC3  85 C0                           test eax, eax
00AB2CC5  0F 88 F1 01 00 00               js 0x140ab2ebc
00AB2CCB  33 D2                           xor edx, edx
00AB2CCD  49 8B CE                        mov rcx, r14
00AB2CD0  E8 9B FB 0C 00                  call 0x140b82870
00AB2CD5  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00AB2CDA  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00AB2CDF  45 33 C0                        xor r8d, r8d
00AB2CE2  48 8D 15 67 C8 04 00            lea rdx, [rip + 0x4c867]
00AB2CE9  49 8B CF                        mov rcx, r15
00AB2CEC  E8 FB 63 EE FF                  call 0x1409990ec
00AB2CF1  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00AB2CF6  8B D8                           mov ebx, eax
00AB2CF8  85 C0                           test eax, eax
00AB2CFA  0F 88 09 04 00 00               js 0x140ab3109
00AB2D00  49 8B CE                        mov rcx, r14
00AB2D03  E8 34 49 A0 FF                  call 0x1404b763c
00AB2D08  84 C0                           test al, al
00AB2D0A  0F 84 B0 FD FF FF               je 0x140ab2ac0
00AB2D10  41 8B 76 08                     mov esi, dword ptr [r14 + 8]
00AB2D14  41 BF 24 00 00 00               mov r15d, 0x24
00AB2D1A  49 03 F6                        add rsi, r14
00AB2D1D  41 8B D7                        mov edx, r15d
00AB2D20  48 8B CE                        mov rcx, rsi
00AB2D23  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
00AB2D27  E8 34 ED A4 FF                  call 0x140501a60
00AB2D2C  48 85 C0                        test rax, rax
00AB2D2F  0F 84 76 03 00 00               je 0x140ab30ab
00AB2D35  41 8B FC                        mov edi, r12d
00AB2D38  41 8B D7                        mov edx, r15d
00AB2D3B  48 8D 48 02                     lea rcx, [rax + 2]
00AB2D3F  FF C7                           inc edi
00AB2D41  E8 1A ED A4 FF                  call 0x140501a60
00AB2D46  48 85 C0                        test rax, rax
00AB2D49  75 ED                           jne 0x140ab2d38
00AB2D4B  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00AB2D50  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00AB2D54  85 FF                           test edi, edi
00AB2D56  0F 84 4D 03 00 00               je 0x140ab30a9
00AB2D5C  8B D7                           mov edx, edi
00AB2D5E  B9 00 01 00 00                  mov ecx, 0x100
00AB2D63  48 C1 E2 03                     shl rdx, 3
00AB2D67  41 B8 50 70 64 63               mov r8d, 0x63647050
00AB2D6D  E8 7E F3 0C 00                  call 0x140b820f0
00AB2D72  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00AB2D77  48 8B D0                        mov rdx, rax
00AB2D7A  48 85 C0                        test rax, rax
00AB2D7D  75 0A                           jne 0x140ab2d89
00AB2D7F  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AB2D84  E9 33 01 00 00                  jmp 0x140ab2ebc
00AB2D89  44 0F B7 65 92                  movzx r12d, word ptr [rbp - 0x6e]
00AB2D8E  33 D2                           xor edx, edx
00AB2D90  44 8B EA                        mov r13d, edx
00AB2D93  8D 42 5C                        lea eax, [rdx + 0x5c]
00AB2D96  44 8D 42 02                     lea r8d, [rdx + 2]
00AB2D9A  4C 8B FE                        mov r15, rsi
00AB2D9D  66 39 16                        cmp word ptr [rsi], dx
00AB2DA0  0F 84 5E 01 00 00               je 0x140ab2f04
00AB2DA6  44 3B EF                        cmp r13d, edi
00AB2DA9  0F 83 55 01 00 00               jae 0x140ab2f04
00AB2DAF  8B D0                           mov edx, eax
00AB2DB1  48 8B CE                        mov rcx, rsi
00AB2DB4  E8 A7 EC A4 FF                  call 0x140501a60
00AB2DB9  33 D2                           xor edx, edx
00AB2DBB  48 8B F0                        mov rsi, rax
00AB2DBE  48 85 C0                        test rax, rax
00AB2DC1  74 0E                           je 0x140ab2dd1
00AB2DC3  48 8B F8                        mov rdi, rax
00AB2DC6  66 89 10                        mov word ptr [rax], dx
00AB2DC9  49 2B FF                        sub rdi, r15
00AB2DCC  48 D1 FF                        sar rdi, 1
00AB2DCF  EB 0E                           jmp 0x140ab2ddf
00AB2DD1  48 83 CF FF                     or rdi, 0xffffffffffffffff
00AB2DD5  48 FF C7                        inc rdi
00AB2DD8  66 41 39 14 7F                  cmp word ptr [r15 + rdi*2], dx
00AB2DDD  75 F6                           jne 0x140ab2dd5
00AB2DDF  03 FF                           add edi, edi
00AB2DE1  B8 24 00 00 00                  mov eax, 0x24
00AB2DE6  66 41 39 07                     cmp word ptr [r15], ax
00AB2DEA  75 69                           jne 0x140ab2e55
00AB2DEC  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AB2DF1  49 8D 57 02                     lea rdx, [r15 + 2]
00AB2DF5  41 8B C5                        mov eax, r13d
00AB2DF8  4C 8D 24 C1                     lea r12, [rcx + rax*8]
00AB2DFC  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00AB2E01  4D 8B C4                        mov r8, r12
00AB2E04  E8 AF EC FC FF                  call 0x140a81ab8
00AB2E09  33 D2                           xor edx, edx
00AB2E0B  8B D8                           mov ebx, eax
00AB2E0D  85 C0                           test eax, eax
00AB2E0F  78 33                           js 0x140ab2e44
00AB2E11  49 8B 0C 24                     mov rcx, qword ptr [r12]
00AB2E15  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00AB2E18  83 E8 01                        sub eax, 1
00AB2E1B  74 1F                           je 0x140ab2e3c
00AB2E1D  83 E8 01                        sub eax, 1
00AB2E20  74 1A                           je 0x140ab2e3c
00AB2E22  83 F8 05                        cmp eax, 5
00AB2E25  75 26                           jne 0x140ab2e4d
00AB2E27  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00AB2E2B  48 83 CF FF                     or rdi, 0xffffffffffffffff
00AB2E2F  48 FF C7                        inc rdi
00AB2E32  66 39 14 78                     cmp word ptr [rax + rdi*2], dx
00AB2E36  75 F7                           jne 0x140ab2e2f
00AB2E38  03 FF                           add edi, edi
00AB2E3A  EB 11                           jmp 0x140ab2e4d
00AB2E3C  8B 79 24                        mov edi, dword ptr [rcx + 0x24]
00AB2E3F  83 EF 02                        sub edi, 2
00AB2E42  EB 09                           jmp 0x140ab2e4d
00AB2E44  3D 34 00 00 C0                  cmp eax, 0xc0000034
00AB2E49  75 65                           jne 0x140ab2eb0
00AB2E4B  8B DA                           mov ebx, edx
00AB2E4D  44 0F B7 65 92                  movzx r12d, word ptr [rbp - 0x6e]
00AB2E52  41 FF C5                        inc r13d
00AB2E55  41 0F B7 CC                     movzx ecx, r12w
00AB2E59  41 B8 02 00 00 00               mov r8d, 2
00AB2E5F  03 CF                           add ecx, edi
00AB2E61  49 03 C8                        add rcx, r8
00AB2E64  48 81 F9 FE FF 00 00            cmp rcx, 0xfffe
00AB2E6B  73 3E                           jae 0x140ab2eab
00AB2E6D  66 41 03 F8                     add di, r8w
00AB2E71  66 44 03 E7                     add r12w, di
00AB2E75  66 44 89 65 92                  mov word ptr [rbp - 0x6e], r12w
00AB2E7A  48 85 F6                        test rsi, rsi
00AB2E7D  74 0C                           je 0x140ab2e8b
00AB2E7F  41 8D 40 5A                     lea eax, [r8 + 0x5a]
00AB2E83  66 89 06                        mov word ptr [rsi], ax
00AB2E86  49 03 F0                        add rsi, r8
00AB2E89  EB 17                           jmp 0x140ab2ea2
00AB2E8B  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AB2E8F  48 FF C0                        inc rax
00AB2E92  66 41 39 14 47                  cmp word ptr [r15 + rax*2], dx
00AB2E97  75 F6                           jne 0x140ab2e8f
00AB2E99  49 8D 34 47                     lea rsi, [r15 + rax*2]
00AB2E9D  B8 5C 00 00 00                  mov eax, 0x5c
00AB2EA2  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
00AB2EA6  E9 EF FE FF FF                  jmp 0x140ab2d9a
00AB2EAB  BB 05 00 00 80                  mov ebx, 0x80000005
00AB2EB0  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AB2EB5  33 D2                           xor edx, edx
00AB2EB7  E8 B4 F9 0C 00                  call 0x140b82870
00AB2EBC  4D 85 F6                        test r14, r14
00AB2EBF  74 0A                           je 0x140ab2ecb
00AB2EC1  33 D2                           xor edx, edx
00AB2EC3  49 8B CE                        mov rcx, r14
00AB2EC6  E8 A5 F9 0C 00                  call 0x140b82870
00AB2ECB  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AB2ED0  48 85 C9                        test rcx, rcx
00AB2ED3  74 05                           je 0x140ab2eda
00AB2ED5  E8 D6 A3 BF FF                  call 0x1406ad2b0
00AB2EDA  8B C3                           mov eax, ebx
00AB2EDC  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AB2EE0  48 33 CC                        xor rcx, rsp
00AB2EE3  E8 58 97 BF FF                  call 0x1406ac640
00AB2EE8  48 8B 9C 24 78 01 00 00         mov rbx, qword ptr [rsp + 0x178]
00AB2EF0  48 81 C4 20 01 00 00            add rsp, 0x120
00AB2EF7  41 5F                           pop r15
00AB2EF9  41 5E                           pop r14
00AB2EFB  41 5D                           pop r13
00AB2EFD  41 5C                           pop r12
00AB2EFF  5F                              pop rdi
00AB2F00  5E                              pop rsi
00AB2F01  5D                              pop rbp
00AB2F02  C3                              ret
00AB2F03  CC                              int3
00AB2F04  85 DB                           test ebx, ebx
00AB2F06  78 A8                           js 0x140ab2eb0
00AB2F08  41 0F B7 C4                     movzx eax, r12w
00AB2F0C  41 0F B7 D4                     movzx edx, r12w
00AB2F10  66 41 2B C0                     sub ax, r8w
00AB2F14  B9 00 01 00 00                  mov ecx, 0x100
00AB2F19  41 B8 50 70 64 63               mov r8d, 0x63647050
00AB2F1F  66 89 45 90                     mov word ptr [rbp - 0x70], ax
00AB2F23  E8 C8 F1 0C 00                  call 0x140b820f0
00AB2F28  48 8B F8                        mov rdi, rax
00AB2F2B  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00AB2F30  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00AB2F34  33 C0                           xor eax, eax
00AB2F36  48 85 FF                        test rdi, rdi
00AB2F39  75 0F                           jne 0x140ab2f4a
00AB2F3B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AB2F40  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
00AB2F45  E9 E8 01 00 00                  jmp 0x140ab3132
00AB2F4A  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
00AB2F4E  4C 8B EF                        mov r13, rdi
00AB2F51  33 FF                           xor edi, edi
00AB2F53  45 0F B7 E4                     movzx r12d, r12w
00AB2F57  8B D8                           mov ebx, eax
00AB2F59  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00AB2F5D  8D 4F 02                        lea ecx, [rdi + 2]
00AB2F60  66 39 3E                        cmp word ptr [rsi], di
00AB2F63  0F 84 1B 01 00 00               je 0x140ab3084
00AB2F69  3B 5C 24 50                     cmp ebx, dword ptr [rsp + 0x50]
00AB2F6D  0F 83 11 01 00 00               jae 0x140ab3084
00AB2F73  BA 5C 00 00 00                  mov edx, 0x5c
00AB2F78  48 8B CE                        mov rcx, rsi
00AB2F7B  E8 E0 EA A4 FF                  call 0x140501a60
00AB2F80  4C 8B F8                        mov r15, rax
00AB2F83  48 85 C0                        test rax, rax
00AB2F86  74 0E                           je 0x140ab2f96
00AB2F88  48 8B C8                        mov rcx, rax
00AB2F8B  66 89 38                        mov word ptr [rax], di
00AB2F8E  48 2B CE                        sub rcx, rsi
00AB2F91  48 D1 F9                        sar rcx, 1
00AB2F94  EB 0D                           jmp 0x140ab2fa3
00AB2F96  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00AB2F9A  48 FF C1                        inc rcx
00AB2F9D  66 39 3C 4E                     cmp word ptr [rsi + rcx*2], di
00AB2FA1  75 F7                           jne 0x140ab2f9a
00AB2FA3  8D 14 09                        lea edx, [rcx + rcx]
00AB2FA6  4C 8B CE                        mov r9, rsi
00AB2FA9  41 BA 02 00 00 00               mov r10d, 2
00AB2FAF  48 3B 75 B0                     cmp rsi, qword ptr [rbp - 0x50]
00AB2FB3  74 17                           je 0x140ab2fcc
00AB2FB5  45 3B E2                        cmp r12d, r10d
00AB2FB8  0F 86 BC 00 00 00               jbe 0x140ab307a
00AB2FBE  66 41 C7 45 00 5C 00            mov word ptr [r13], 0x5c
00AB2FC5  4D 03 EA                        add r13, r10
00AB2FC8  41 83 C4 FE                     add r12d, -2
00AB2FCC  B8 24 00 00 00                  mov eax, 0x24
00AB2FD1  8B FA                           mov edi, edx
00AB2FD3  66 39 06                        cmp word ptr [rsi], ax
00AB2FD6  75 4B                           jne 0x140ab3023
00AB2FD8  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AB2FDD  45 33 C0                        xor r8d, r8d
00AB2FE0  8B C3                           mov eax, ebx
00AB2FE2  FF C3                           inc ebx
00AB2FE4  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00AB2FE8  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00AB2FEC  48 85 C9                        test rcx, rcx
00AB2FEF  74 32                           je 0x140ab3023
00AB2FF1  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00AB2FF4  83 E8 01                        sub eax, 1
00AB2FF7  74 20                           je 0x140ab3019
00AB2FF9  83 E8 01                        sub eax, 1
00AB2FFC  74 1B                           je 0x140ab3019
00AB2FFE  83 F8 05                        cmp eax, 5
00AB3001  75 20                           jne 0x140ab3023
00AB3003  4C 8B 49 28                     mov r9, qword ptr [rcx + 0x28]
00AB3007  48 83 CF FF                     or rdi, 0xffffffffffffffff
00AB300B  48 FF C7                        inc rdi
00AB300E  66 45 39 04 79                  cmp word ptr [r9 + rdi*2], r8w
00AB3013  75 F6                           jne 0x140ab300b
00AB3015  03 FF                           add edi, edi
00AB3017  EB 0A                           jmp 0x140ab3023
00AB3019  8B 79 24                        mov edi, dword ptr [rcx + 0x24]
00AB301C  4C 8B 49 28                     mov r9, qword ptr [rcx + 0x28]
00AB3020  41 2B FA                        sub edi, r10d
00AB3023  44 3B E7                        cmp r12d, edi
00AB3026  76 52                           jbe 0x140ab307a
00AB3028  44 8B C7                        mov r8d, edi
00AB302B  49 8B D1                        mov rdx, r9
00AB302E  49 8B CD                        mov rcx, r13
00AB3031  8B DF                           mov ebx, edi
00AB3033  E8 08 38 C1 FF                  call 0x1406c6840
00AB3038  48 D1 EB                        shr rbx, 1
00AB303B  44 2B E7                        sub r12d, edi
00AB303E  33 FF                           xor edi, edi
00AB3040  4D 8D 6C 5D 00                  lea r13, [r13 + rbx*2]
00AB3045  4D 85 FF                        test r15, r15
00AB3048  74 0E                           je 0x140ab3058
00AB304A  8D 4F 02                        lea ecx, [rdi + 2]
00AB304D  66 41 C7 07 5C 00               mov word ptr [r15], 0x5c
00AB3053  4C 03 F9                        add r15, rcx
00AB3056  EB 16                           jmp 0x140ab306e
00AB3058  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AB305C  48 FF C0                        inc rax
00AB305F  66 39 3C 46                     cmp word ptr [rsi + rax*2], di
00AB3063  75 F7                           jne 0x140ab305c
00AB3065  4C 8D 3C 46                     lea r15, [rsi + rax*2]
00AB3069  B9 02 00 00 00                  mov ecx, 2
00AB306E  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
00AB3072  49 8B F7                        mov rsi, r15
00AB3075  E9 E6 FE FF FF                  jmp 0x140ab2f60
00AB307A  BB 01 00 00 C0                  mov ebx, 0xc0000001
00AB307F  E9 BC FE FF FF                  jmp 0x140ab2f40
00AB3084  44 3B E1                        cmp r12d, ecx
00AB3087  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
00AB308C  74 0A                           je 0x140ab3098
00AB308E  BB 01 00 00 C0                  mov ebx, 0xc0000001
00AB3093  E9 9A 00 00 00                  jmp 0x140ab3132
00AB3098  0F 28 45 90                     movaps xmm0, xmmword ptr [rbp - 0x70]
00AB309C  66 41 89 7D 00                  mov word ptr [r13], di
00AB30A1  66 0F 7F 44 24 60               movdqa xmmword ptr [rsp + 0x60], xmm0
00AB30A7  EB 3B                           jmp 0x140ab30e4
00AB30A9  33 FF                           xor edi, edi
00AB30AB  41 8B 4E 08                     mov ecx, dword ptr [r14 + 8]
00AB30AF  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00AB30B4  41 8B 56 0C                     mov edx, dword ptr [r14 + 0xc]
00AB30B8  49 03 CE                        add rcx, r14
00AB30BB  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00AB30BF  E8 7C AB FA FF                  call 0x140a5dc40
00AB30C4  0F B7 4C 24 40                  movzx ecx, word ptr [rsp + 0x40]
00AB30C9  66 89 4C 24 60                  mov word ptr [rsp + 0x60], cx
00AB30CE  41 0F B7 46 0C                  movzx eax, word ptr [r14 + 0xc]
00AB30D3  66 89 44 24 62                  mov word ptr [rsp + 0x62], ax
00AB30D8  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00AB30DC  49 03 C6                        add rax, r14
00AB30DF  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00AB30E4  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00AB30E9  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AB30EE  41 B9 19 00 02 00               mov r9d, 0x20019
00AB30F4  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00AB30F8  E8 47 EA F9 FF                  call 0x140a51b44
00AB30FD  8B D8                           mov ebx, eax
00AB30FF  85 C0                           test eax, eax
00AB3101  78 2F                           js 0x140ab3132
00AB3103  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00AB3107  EB 1B                           jmp 0x140ab3124
00AB3109  3D 34 00 00 C0                  cmp eax, 0xc0000034
00AB310E  0F 85 A8 FD FF FF               jne 0x140ab2ebc
00AB3114  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AB3119  8B DF                           mov ebx, edi
00AB311B  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00AB311F  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00AB3124  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00AB3128  48 89 01                        mov qword ptr [rcx], rax
00AB312B  EB 05                           jmp 0x140ab3132
00AB312D  BB 34 00 00 C0                  mov ebx, 0xc0000034
00AB3132  4D 85 E4                        test r12, r12
00AB3135  74 08                           je 0x140ab313f
00AB3137  49 8B CC                        mov rcx, r12
00AB313A  E8 11 F7 0C 00                  call 0x140b82850
00AB313F  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AB3144  48 85 C9                        test rcx, rcx
00AB3147  0F 85 68 FD FF FF               jne 0x140ab2eb5
00AB314D  E9 6A FD FF FF                  jmp 0x140ab2ebc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgResolveVariableKeyHandle(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int8 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m48;
    unsigned __int16 v_stack_m4C;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int16 v_stack_mC6;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int16 v_stack_p62;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 3505401)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = 0;
    v_stack_mA0 = a3;
    *(unsigned __int64 *)(a3) = 0;
    v_stack_mE0 = a1;
    v_stack_m118 = 0;
    a3 = 0;
    v_stack_m110 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = 0;
    v_stack_mD8 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mD4 = 0;
    v_stack_mE8 = 0;
    v_stack_mC8 = 0;
    result = IopGetRegistryValue(a2, v_rip + 313966, a3, v_stack_m118);
    if (sign_flag) goto loc_00AB2EBC;
    result = PnpValidateRegistryString(v_stack_m118, v_rip + 313966, a3, v_stack_m118);
    if ((unsigned __int8)(result) != 0) goto loc_00AB2ACA;
loc_00AB2AC0:
    goto loc_00AB2EBC;
loc_00AB2ACA:
    v_rbx = ((unsigned int)(*(unsigned int *)(v_stack_m118 + 8))) + (v_stack_m118);
loc_00AB2AD3:
    if (0 >= 7) goto loc_00AB2C3D;
    v_rdi = (0) << (5);
    v_rdi = (v_rdi) + (v_rip + 634205);
    result = wcsicmp(*(unsigned __int64 *)(v_rdi), v_rbx, a3, v_stack_m118);
    if ((unsigned int)(result) == 0) goto loc_00AB2AFF;
    v_rsi = (unsigned int)((0) + 1);
    goto loc_00AB2AD3;
loc_00AB2AFF:
    v_rsi = 0;
    if (v_rdi == 0) goto loc_00AB2C3D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16))) == 0) goto loc_00AB2B4D;
    v_rdi = 0;
    v_stack_m120 = 0;
    a4 = 0;
    v_stack_m128 = v_stack_m110;
    v_stack_m130 = 0;
    v_stack_m138 = 0x20019ULL;
    result = _CmOpenDeviceRegKey(*(unsigned __int64 *)(v_rip + 3881073), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 48), (unsigned int)(*(unsigned int *)(v_rdi + 16)), a4);
    goto loc_00AB2CC1;
loc_00AB2B4D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 12))) == 0) goto loc_00AB2C33;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 12)))) == 7) goto loc_00AB2B63;
    goto loc_00AB2BBE;
loc_00AB2B63:
    v_stack_m120 = (unsigned int)(*(unsigned __int64 *)(v_rdi + 24));
    v_stack_m128 = v_stack_mD8;
    a3 = 0;
    v_stack_mD8 = 78;
    v_stack_m130 = v_stack_m98;
    v_stack_m138 = v_stack_mD4;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 3881006), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 48) + 48), a3, 9);
    if (sign_flag) goto loc_00AB2EBC;
    if (v_stack_mD4 != 1) goto loc_00AB2AC0;
    v_stack_m4C = (unsigned __int16)(*(unsigned __int64 *)(v_rdi + 24));
loc_00AB2BBE:
    v_stack_m138 = v_stack_m110;
    result = PnpCtxOpenContextBaseKey(*(unsigned __int64 *)(v_rip + 3881006), (unsigned int)(*(unsigned int *)(v_rdi + 12)), a3, (unsigned int)(0x20019ULL));
    v_rdi = 0;
    if (sign_flag) goto loc_00AB2EBC;
    if (v_stack_m98 == 0) goto loc_00AB2CCB;
    result = RtlInitUnicodeString(v_stack_mF8, v_stack_m98, a3, (unsigned int)(0x20019ULL));
    result = IopOpenRegistryKeyEx(v_stack_mB0, v_stack_m110, v_stack_mF8, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_00AB2EBC;
    result = ZwClose(v_stack_m110, v_stack_m110, v_stack_mF8, (unsigned int)(0x20019ULL));
    v_stack_m110 = v_stack_mB0;
    goto loc_00AB2CCB;
loc_00AB2C33:
    goto loc_00AB2EBC;
loc_00AB2C3D:
    result = wcsicmp((unsigned int)(0xC00000E5ULL), v_rip + 313532, v_stack_mF8, (unsigned int)(0x20019ULL));
    v_rdi = 0;
    if ((unsigned int)(result) != 0) goto loc_00AB2C63;
    v_stack_mF8 = 0x320030ULL;
    goto loc_00AB2CA5;
loc_00AB2C63:
    result = wcsicmp((unsigned int)(0xC00000E5ULL), v_rip + 313286, v_stack_mF8, (unsigned int)(0x20019ULL));
    if ((unsigned int)(result) != 0) goto loc_00AB2C7F;
    goto loc_00AB2C9D;
loc_00AB2C7F:
    result = wcsicmp((unsigned int)(0xC00000E5ULL), v_rip + 313354, v_stack_mF8, (unsigned int)(0x20019ULL));
    if ((unsigned int)(result) != 0) goto loc_00AB312D;
loc_00AB2C9D:
    v_stack_mF8 = 0x360034ULL;
loc_00AB2CA5:
    v_stack_mF0 = v_rip + 313363;
    a2 = 0;
    result = IopOpenRegistryKeyEx(v_stack_m110, a2, v_stack_mF8, (unsigned int)(0x20019ULL));
loc_00AB2CC1:
    if (sign_flag) goto loc_00AB2EBC;
loc_00AB2CCB:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m118, a2, v_stack_mF8, (unsigned int)(0x20019ULL));
    v_stack_m118 = 0;
    a3 = 0;
    result = IopGetRegistryValue(0, v_rip + 313447, a3, v_stack_m118);
    if (sign_flag) goto loc_00AB3109;
    result = PnpValidateRegistryString(v_stack_m118, v_rip + 313447, a3, v_stack_m118);
    if ((unsigned __int8)(result) == 0) goto loc_00AB2AC0;
    v_rsi = ((unsigned int)(*(unsigned int *)(v_stack_m118 + 8))) + (v_stack_m118);
    v_stack_mA8 = v_rsi;
    result = wcschr(v_rsi, 36, a3, v_stack_m118);
    if (result == 0) goto loc_00AB30AB;
loc_00AB2D38:
    v_rdi = (unsigned int)((0) + 1);
    result = wcschr(result + 2, 36, a3, v_stack_m118);
    if (result != 0) goto loc_00AB2D38;
    v_stack_m108 = (unsigned int)(v_rdi);
    if ((unsigned int)(v_rdi) == 0) goto loc_00AB30A9;
    a2 = ((unsigned int)((unsigned int)(v_rdi))) << (3);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x63647050ULL), v_stack_m118);
    v_stack_mE8 = result;
    if (result != 0) goto loc_00AB2D89;
    goto loc_00AB2EBC;
loc_00AB2D89:
    a2 = 0;
loc_00AB2D9A:
    if ((*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00AB2F04;
    if (0 >= ((unsigned int)(v_rdi))) goto loc_00AB2F04;
    result = wcschr(v_rsi, (unsigned int)((unsigned int)(a2 + 92)), a2 + 2, v_stack_m118);
    a2 = 0;
    if (result == 0) goto loc_00AB2DD1;
    *(unsigned __int16 *)(result) = 0;
    v_rdi = (result) - (v_rsi);
    v_rdi = (v_rdi) >> (1);
    goto loc_00AB2DDF;
loc_00AB2DD1:
    v_rdi = (v_rdi) | (-1);
loc_00AB2DD5:
    v_rdi = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(v_rsi + v_rdi * 2)) != 0) goto loc_00AB2DD5;
loc_00AB2DDF:
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rdi)));
    if ((*(unsigned __int16 *)(v_rsi)) != 36) goto loc_00AB2E55;
    result = PiDevCfgResolveVariable(v_stack_mE0, v_rsi + 2, v_stack_mE8 + 0 * 8, v_stack_m118);
    a2 = 0;
    if (sign_flag) goto loc_00AB2E44;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mE8 + 0 * 8) + 32))) - (1));
    if (condition_is_equal) goto loc_00AB2E3C;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AB2E3C;
    if (((unsigned int)(result)) != 5) goto loc_00AB2E4D;
    v_rdi = (v_rdi) | (-1);
loc_00AB2E2F:
    v_rdi = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 0 * 8) + 40) + v_rdi * 2)) != 0) goto loc_00AB2E2F;
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rdi)));
    goto loc_00AB2E4D;
loc_00AB2E3C:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mE8 + 0 * 8) + 36))) - (2));
    goto loc_00AB2E4D;
loc_00AB2E44:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 0 * 8) + 40))) != 0xC0000034ULL) goto loc_00AB2EB0;
loc_00AB2E4D:
    v_r13 = (unsigned int)((0) + 1);
loc_00AB2E55:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_mC6)) + ((unsigned int)(v_rdi)));
    a1 = (a1) + (2);
    if (a1 >= 0xFFFEULL) goto loc_00AB2EAB;
    v_rdi = (unsigned __int16)((v_rdi) + (2));
    v_r12 = (unsigned __int16)((v_stack_mC6) + ((unsigned __int16)(v_rdi)));
    v_stack_mC6 = (unsigned __int16)(v_r12);
    if (result == 0) goto loc_00AB2E8B;
    *(unsigned __int16 *)(result) = (unsigned __int16)(2 + 90);
    v_rsi = (result) + (2);
    goto loc_00AB2EA2;
loc_00AB2E8B:
    result = (2 + 90) | (-1);
loc_00AB2E8F:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rsi + result * 2)) != 0) goto loc_00AB2E8F;
loc_00AB2EA2:
    goto loc_00AB2D9A;
loc_00AB2EAB:
loc_00AB2EB0:
loc_00AB2EB5:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mE8, a2, 2, v_stack_m118);
loc_00AB2EBC:
    if (v_stack_m118 != 0) {
        a2 = 0;
        a1 = v_stack_m118;
        result = ExFreePoolWithTag(a1, a2, 2, v_stack_m118);
    }
    if (v_stack_m110 != 0) {
        result = ZwClose(v_stack_m110, a2, 2, v_stack_m118);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 2, v_stack_m118);
    v_rsp = (v_rsp) + (288);
    return result;
loc_00AB2F04:
    if (sign_flag) goto loc_00AB2EB0;
    result = (unsigned __int16)(((unsigned __int16)(v_r12)) - (2));
    v_stack_mC8 = (unsigned __int16)(result);
    result = ExAllocatePool2(256, (unsigned __int16)(v_r12), (unsigned int)(0x63647050ULL), v_stack_m118);
    v_stack_p78 = result;
    v_stack_mC0 = result;
    result = 0;
    if (0 != 0) goto loc_00AB2F4A;
loc_00AB2F40:
    goto loc_00AB3132;
loc_00AB2F4A:
    v_rdi = 0;
    v_stack_p40 = 0;
loc_00AB2F60:
    if ((*(unsigned __int16 *)(v_stack_mA8)) == 0) goto loc_00AB3084;
    if (0 >= v_stack_p50) goto loc_00AB3084;
    result = wcschr(v_stack_mA8, 92, (unsigned int)(0x63647050ULL), v_stack_m118);
    if (result == 0) goto loc_00AB2F96;
    *(unsigned __int16 *)(result) = 0;
    a1 = (result) - (v_stack_mA8);
    a1 = (a1) >> (1);
    goto loc_00AB2FA3;
loc_00AB2F96:
    a1 = (a1) | (-1);
loc_00AB2F9A:
    a1 = (a1) + 1;
    if ((*(unsigned __int16 *)(v_stack_mA8 + a1 * 2)) != 0) goto loc_00AB2F9A;
loc_00AB2FA3:
    if (v_stack_mA8 == v_stack_mA8) goto loc_00AB2FCC;
    if (((unsigned int)((unsigned __int16)(v_stack_p78))) <= 2) goto loc_00AB307A;
    *(unsigned __int16 *)(0) = 92;
    v_r13 = (0) + (2);
    v_r12 = (unsigned int)(((unsigned __int16)(v_stack_p78)) + (-2));
loc_00AB2FCC:
    if ((*(unsigned __int16 *)(v_stack_mA8)) != 36) goto loc_00AB3023;
    a3 = 0;
    v_rbx = (unsigned int)((0) + 1);
    v_stack_p40 = (unsigned int)(v_rbx);
    if (*(unsigned __int64 *)(v_stack_p70 + 0 * 8) == 0) goto loc_00AB3023;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p70 + 0 * 8) + 32))) - (1));
    if (condition_is_equal) goto loc_00AB3019;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AB3019;
    if (((unsigned int)(result)) != 5) goto loc_00AB3023;
    v_rdi = ((unsigned int)((unsigned int)(a1 + a1 * 1))) | (-1);
loc_00AB300B:
    v_rdi = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p70 + 0 * 8) + 40) + v_rdi * 2)) != 0) goto loc_00AB300B;
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rdi)));
    goto loc_00AB3023;
loc_00AB3019:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p70 + 0 * 8) + 36))) - (2));
loc_00AB3023:
    if (((unsigned int)(v_r12)) <= ((unsigned int)(v_rdi))) goto loc_00AB307A;
    result = memcpy(v_r13, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p70 + 0 * 8) + 40), (unsigned int)((unsigned int)(v_rdi)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p70 + 0 * 8) + 40));
    v_rbx = ((unsigned int)((unsigned int)(v_rdi))) >> (1);
    v_r12 = (unsigned int)((v_r12) - ((unsigned int)(v_rdi)));
    v_rdi = 0;
    if (result == 0) goto loc_00AB3058;
    *(unsigned __int16 *)(result) = 92;
    v_r15 = (result) + (v_rdi + 2);
    goto loc_00AB306E;
loc_00AB3058:
    result = (result) | (-1);
loc_00AB305C:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_mA8 + result * 2)) != 0) goto loc_00AB305C;
loc_00AB306E:
    goto loc_00AB2F60;
loc_00AB307A:
    goto loc_00AB2F40;
loc_00AB3084:
    if (((unsigned int)(v_r12)) == 2) goto loc_00AB3098;
    goto loc_00AB3132;
loc_00AB3098:
    *(unsigned __int16 *)(v_r13 + v_rbx * 2) = 0;
    v_stack_p60 = v_xmm0;
    goto loc_00AB30E4;
loc_00AB30A9:
    v_rdi = 0;
loc_00AB30AB:
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m118 + 8))) + (v_stack_m118);
    v_stack_p40 = 0;
    result = PnpRegSzToString(a1, (unsigned int)(*(unsigned int *)(v_stack_m118 + 12)), v_stack_p40, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p70 + 0 * 8) + 40));
    v_stack_p60 = (unsigned __int16)(v_stack_p40);
    v_stack_p62 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m118 + 12));
    result = ((unsigned int)(*(unsigned int *)(v_stack_m118 + 8))) + (v_stack_m118);
    v_stack_p68 = result;
loc_00AB30E4:
    result = IopOpenRegistryKeyEx(v_stack_mB8, v_stack_p48, v_stack_p60, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_00AB3132;
    goto loc_00AB3124;
loc_00AB3109:
    if (((unsigned int)(v_stack_mB8)) != 0xC0000034ULL) goto loc_00AB2EBC;
    v_stack_mB8 = v_stack_p48;
    v_stack_p48 = 0;
loc_00AB3124:
    *(unsigned __int64 *)(v_stack_mA0) = v_stack_p48;
    goto loc_00AB3132;
loc_00AB312D:
loc_00AB3132:
    result = v_stack_p48;
    if (v_stack_p78 != 0) {
        a1 = v_stack_p78;
        result = ExFreePool(a1, v_stack_p48, v_stack_p60, (unsigned int)(0x20019ULL));
    }
    if (v_stack_p70 != 0) goto loc_00AB2EB5;
    goto loc_00AB2EBC;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgResolveVariableKeyHandle(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint8_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m48;
    uint16_t v_stack_m4C;
    uint64_t v_stack_m58;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint16_t v_stack_mC6;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p60;
    uint16_t v_stack_p62;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0x357CF9)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = 0;
    v_stack_mA0 = Arg3;
    *(uint64_t *)(arg3) = 0;
    v_stack_mE0 = Arg1;
    v_stack_m118 = 0;
    Arg3 = 0;
    v_stack_m110 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = 0;
    v_stack_mD8 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mD4 = 0;
    v_stack_mE8 = 0;
    v_stack_mC8 = 0;
    result = IopGetRegistryValue(Arg2, v_rip + 313966, Arg3, v_stack_m118);
    if (sign_flag) goto loc_00AB2EBC;
    result = PnpValidateRegistryString(v_stack_m118, v_rip + 313966, Arg3, v_stack_m118);
    if ((uint8_t)(result) != 0) goto loc_00AB2ACA;
loc_00AB2AC0:
    goto loc_00AB2EBC;
loc_00AB2ACA:
    local_rbx = ((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x8))) + (v_stack_m118);
loc_00AB2AD3:
    if (0 >= 7) goto loc_00AB2C3D;
    local_rdi = (0) << (5);
    local_rdi = (local_rdi) + (v_rip + 634205);
    result = wcsicmp(*(uint64_t *)(local_rdi), local_rbx, Arg3, v_stack_m118);
    if ((uint32_t)(result) == 0) goto loc_00AB2AFF;
    local_rsi = (uint32_t)((0) + 1);
    goto loc_00AB2AD3;
loc_00AB2AFF:
    local_rsi = 0;
    if (local_rdi == 0) goto loc_00AB2C3D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x10))) == 0) goto loc_00AB2B4D;
    local_rdi = 0;
    v_stack_m120 = 0;
    a4 = 0;
    v_stack_m128 = v_stack_m110;
    v_stack_m130 = 0;
    v_stack_m138 = 0x20019ULL;
    result = _CmOpenDeviceRegKey(*(uint64_t *)(v_rip + 0x3B3871), *(uint64_t *)(*(uint64_t *)(arg1) + 0x30), (uint32_t)(*(uint32_t *)(local_rdi + 0x10)), a4);
    goto loc_00AB2CC1;
loc_00AB2B4D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC))) == 0) goto loc_00AB2C33;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)))) == 7) goto loc_00AB2B63;
    goto loc_00AB2BBE;
loc_00AB2B63:
    v_stack_m120 = (uint32_t)(*(uint64_t *)(local_rdi + 0x18));
    v_stack_m128 = v_stack_mD8;
    Arg3 = 0;
    v_stack_mD8 = 78;
    v_stack_m130 = v_stack_m98;
    v_stack_m138 = v_stack_mD4;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x3B382E), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x30) + 0x30), Arg3, 9);
    if (sign_flag) goto loc_00AB2EBC;
    if (v_stack_mD4 != 1) goto loc_00AB2AC0;
    v_stack_m4C = (uint16_t)(*(uint64_t *)(local_rdi + 0x18));
loc_00AB2BBE:
    v_stack_m138 = v_stack_m110;
    result = PnpCtxOpenContextBaseKey(*(uint64_t *)(v_rip + 0x3B382E), (uint32_t)(*(uint32_t *)(local_rdi + 0xC)), Arg3, (uint32_t)(0x20019ULL));
    local_rdi = 0;
    if (sign_flag) goto loc_00AB2EBC;
    if (v_stack_m98 == 0) goto loc_00AB2CCB;
    result = RtlInitUnicodeString(v_stack_mF8, v_stack_m98, Arg3, (uint32_t)(0x20019ULL));
    result = IopOpenRegistryKeyEx(v_stack_mB0, v_stack_m110, v_stack_mF8, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_00AB2EBC;
    result = ZwClose(v_stack_m110, v_stack_m110, v_stack_mF8, (uint32_t)(0x20019ULL));
    v_stack_m110 = v_stack_mB0;
    goto loc_00AB2CCB;
loc_00AB2C33:
    goto loc_00AB2EBC;
loc_00AB2C3D:
    result = wcsicmp((uint32_t)(0xC00000E5ULL), v_rip + 313532, v_stack_mF8, (uint32_t)(0x20019ULL));
    local_rdi = 0;
    if ((uint32_t)(result) != 0) goto loc_00AB2C63;
    v_stack_mF8 = 0x320030ULL;
    goto loc_00AB2CA5;
loc_00AB2C63:
    result = wcsicmp((uint32_t)(0xC00000E5ULL), v_rip + 313286, v_stack_mF8, (uint32_t)(0x20019ULL));
    if ((uint32_t)(result) != 0) goto loc_00AB2C7F;
    goto loc_00AB2C9D;
loc_00AB2C7F:
    result = wcsicmp((uint32_t)(0xC00000E5ULL), v_rip + 313354, v_stack_mF8, (uint32_t)(0x20019ULL));
    if ((uint32_t)(result) != 0) goto loc_00AB312D;
loc_00AB2C9D:
    v_stack_mF8 = 0x360034ULL;
loc_00AB2CA5:
    v_stack_mF0 = v_rip + 313363;
    Arg2 = 0;
    result = IopOpenRegistryKeyEx(v_stack_m110, Arg2, v_stack_mF8, (uint32_t)(0x20019ULL));
loc_00AB2CC1:
    if (sign_flag) goto loc_00AB2EBC;
loc_00AB2CCB:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m118, Arg2, v_stack_mF8, (uint32_t)(0x20019ULL));
    v_stack_m118 = 0;
    Arg3 = 0;
    result = IopGetRegistryValue(0, v_rip + 313447, Arg3, v_stack_m118);
    if (sign_flag) goto loc_00AB3109;
    result = PnpValidateRegistryString(v_stack_m118, v_rip + 313447, Arg3, v_stack_m118);
    if ((uint8_t)(result) == 0) goto loc_00AB2AC0;
    local_rsi = ((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x8))) + (v_stack_m118);
    v_stack_mA8 = local_rsi;
    result = wcschr(local_rsi, 36, Arg3, v_stack_m118);
    if (result == 0) goto loc_00AB30AB;
loc_00AB2D38:
    local_rdi = (uint32_t)((0) + 1);
    result = wcschr(result + 2, 36, Arg3, v_stack_m118);
    if (result != 0) goto loc_00AB2D38;
    v_stack_m108 = (uint32_t)(local_rdi);
    if ((uint32_t)(local_rdi) == 0) goto loc_00AB30A9;
    Arg2 = ((uint32_t)((uint32_t)(local_rdi))) << (3);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x63647050ULL), v_stack_m118);
    v_stack_mE8 = result;
    if (result != 0) goto loc_00AB2D89;
    goto loc_00AB2EBC;
loc_00AB2D89:
    Arg2 = 0;
loc_00AB2D9A:
    if ((*(uint16_t *)(local_rsi)) == 0) goto loc_00AB2F04;
    if (0 >= ((uint32_t)(local_rdi))) goto loc_00AB2F04;
    result = wcschr(local_rsi, (uint32_t)((uint32_t)(Arg2 + 92)), Arg2 + 2, v_stack_m118);
    Arg2 = 0;
    if (result == 0) goto loc_00AB2DD1;
    *(uint16_t *)(result) = 0;
    local_rdi = (result) - (local_rsi);
    local_rdi = (local_rdi) >> (1);
    goto loc_00AB2DDF;
loc_00AB2DD1:
    local_rdi = (local_rdi) | (-1);
loc_00AB2DD5:
    local_rdi = (local_rdi) + 1;
    if ((*(uint16_t *)(local_rsi + local_rdi * 2)) != 0) goto loc_00AB2DD5;
loc_00AB2DDF:
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rdi)));
    if ((*(uint16_t *)(local_rsi)) != 36) goto loc_00AB2E55;
    result = PiDevCfgResolveVariable(v_stack_mE0, local_rsi + 2, v_stack_mE8 + 0 * 8, v_stack_m118);
    Arg2 = 0;
    if (sign_flag) goto loc_00AB2E44;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mE8 + 0x0 * 8) + 0x20))) - (1));
    if (condition_is_equal) goto loc_00AB2E3C;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AB2E3C;
    if (((uint32_t)(result)) != 5) goto loc_00AB2E4D;
    local_rdi = (local_rdi) | (-1);
loc_00AB2E2F:
    local_rdi = (local_rdi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x0 * 8) + 0x28) + local_rdi * 2)) != 0) goto loc_00AB2E2F;
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rdi)));
    goto loc_00AB2E4D;
loc_00AB2E3C:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mE8 + 0x0 * 8) + 0x24))) - (2));
    goto loc_00AB2E4D;
loc_00AB2E44:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x0 * 8) + 0x28))) != 0xC0000034ULL) goto loc_00AB2EB0;
loc_00AB2E4D:
    local_r13 = (uint32_t)((0) + 1);
loc_00AB2E55:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_mC6)) + ((uint32_t)(local_rdi)));
    Arg1 = (Arg1) + (2);
    if (Arg1 >= 0xFFFEULL) goto loc_00AB2EAB;
    local_rdi = (uint16_t)((local_rdi) + (2));
    local_r12 = (uint16_t)((v_stack_mC6) + ((uint16_t)(local_rdi)));
    v_stack_mC6 = (uint16_t)(local_r12);
    if (result == 0) goto loc_00AB2E8B;
    *(uint16_t *)(result) = (uint16_t)(2 + 90);
    local_rsi = (result) + (2);
    goto loc_00AB2EA2;
loc_00AB2E8B:
    result = (2 + 90) | (-1);
loc_00AB2E8F:
    result = (result) + 1;
    if ((*(uint16_t *)(local_rsi + result * 2)) != 0) goto loc_00AB2E8F;
loc_00AB2EA2:
    goto loc_00AB2D9A;
loc_00AB2EAB:
loc_00AB2EB0:
loc_00AB2EB5:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mE8, Arg2, 2, v_stack_m118);
loc_00AB2EBC:
    if (v_stack_m118 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m118;
        result = ExFreePoolWithTag(Arg1, Arg2, 2, v_stack_m118);
    }
    if (v_stack_m110 != 0) {
        result = ZwClose(v_stack_m110, Arg2, 2, v_stack_m118);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 2, v_stack_m118);
    local_rsp = (local_rsp) + (288);
    return result;
loc_00AB2F04:
    if (sign_flag) goto loc_00AB2EB0;
    result = (uint16_t)(((uint16_t)(local_r12)) - (2));
    v_stack_mC8 = (uint16_t)(result);
    result = ExAllocatePool2(256, (uint16_t)(local_r12), (uint32_t)(0x63647050ULL), v_stack_m118);
    v_stack_p78 = result;
    v_stack_mC0 = result;
    result = 0;
    if (0 != 0) goto loc_00AB2F4A;
loc_00AB2F40:
    goto loc_00AB3132;
loc_00AB2F4A:
    local_rdi = 0;
    v_stack_p40 = 0;
loc_00AB2F60:
    if ((*(uint16_t *)(v_stack_mA8)) == 0) goto loc_00AB3084;
    if (0 >= v_stack_p50) goto loc_00AB3084;
    result = wcschr(v_stack_mA8, 92, (uint32_t)(0x63647050ULL), v_stack_m118);
    if (result == 0) goto loc_00AB2F96;
    *(uint16_t *)(result) = 0;
    Arg1 = (result) - (v_stack_mA8);
    Arg1 = (Arg1) >> (1);
    goto loc_00AB2FA3;
loc_00AB2F96:
    Arg1 = (Arg1) | (-1);
loc_00AB2F9A:
    Arg1 = (Arg1) + 1;
    if ((*(uint16_t *)(v_stack_mA8 + arg1 * 2)) != 0) goto loc_00AB2F9A;
loc_00AB2FA3:
    if (v_stack_mA8 == v_stack_mA8) goto loc_00AB2FCC;
    if (((uint32_t)((uint16_t)(v_stack_p78))) <= 2) goto loc_00AB307A;
    *(uint16_t *)(0) = 92;
    local_r13 = (0) + (2);
    local_r12 = (uint32_t)(((uint16_t)(v_stack_p78)) + (-2));
loc_00AB2FCC:
    if ((*(uint16_t *)(v_stack_mA8)) != 36) goto loc_00AB3023;
    Arg3 = 0;
    local_rbx = (uint32_t)((0) + 1);
    v_stack_p40 = (uint32_t)(local_rbx);
    if (*(uint64_t *)(v_stack_p70 + 0x0 * 8) == 0) goto loc_00AB3023;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p70 + 0x0 * 8) + 0x20))) - (1));
    if (condition_is_equal) goto loc_00AB3019;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AB3019;
    if (((uint32_t)(result)) != 5) goto loc_00AB3023;
    local_rdi = ((uint32_t)((uint32_t)(Arg1 + Arg1 * 1))) | (-1);
loc_00AB300B:
    local_rdi = (local_rdi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p70 + 0x0 * 8) + 0x28) + local_rdi * 2)) != 0) goto loc_00AB300B;
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rdi)));
    goto loc_00AB3023;
loc_00AB3019:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p70 + 0x0 * 8) + 0x24))) - (2));
loc_00AB3023:
    if (((uint32_t)(local_r12)) <= ((uint32_t)(local_rdi))) goto loc_00AB307A;
    result = memcpy(local_r13, *(uint64_t *)(*(uint64_t *)(v_stack_p70 + 0x0 * 8) + 0x28), (uint32_t)((uint32_t)(local_rdi)), *(uint64_t *)(*(uint64_t *)(v_stack_p70 + 0x0 * 8) + 0x28));
    local_rbx = ((uint32_t)((uint32_t)(local_rdi))) >> (1);
    local_r12 = (uint32_t)((local_r12) - ((uint32_t)(local_rdi)));
    local_rdi = 0;
    if (result == 0) goto loc_00AB3058;
    *(uint16_t *)(result) = 92;
    local_r15 = (result) + (local_rdi + 2);
    goto loc_00AB306E;
loc_00AB3058:
    result = (result) | (-1);
loc_00AB305C:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_mA8 + result * 2)) != 0) goto loc_00AB305C;
loc_00AB306E:
    goto loc_00AB2F60;
loc_00AB307A:
    goto loc_00AB2F40;
loc_00AB3084:
    if (((uint32_t)(local_r12)) == 2) goto loc_00AB3098;
    goto loc_00AB3132;
loc_00AB3098:
    *(uint16_t *)(local_r13 + local_rbx * 2) = 0;
    v_stack_p60 = v_xmm0;
    goto loc_00AB30E4;
loc_00AB30A9:
    local_rdi = 0;
loc_00AB30AB:
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x8))) + (v_stack_m118);
    v_stack_p40 = 0;
    result = PnpRegSzToString(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m118 + 0xC)), v_stack_p40, *(uint64_t *)(*(uint64_t *)(v_stack_p70 + 0x0 * 8) + 0x28));
    v_stack_p60 = (uint16_t)(v_stack_p40);
    v_stack_p62 = (uint16_t)(*(uint16_t *)(v_stack_m118 + 0xC));
    result = ((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x8))) + (v_stack_m118);
    v_stack_p68 = result;
loc_00AB30E4:
    result = IopOpenRegistryKeyEx(v_stack_mB8, v_stack_p48, v_stack_p60, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_00AB3132;
    goto loc_00AB3124;
loc_00AB3109:
    if (((uint32_t)(v_stack_mB8)) != 0xC0000034ULL) goto loc_00AB2EBC;
    v_stack_mB8 = v_stack_p48;
    v_stack_p48 = 0;
loc_00AB3124:
    *(uint64_t *)(v_stack_mA0) = v_stack_p48;
    goto loc_00AB3132;
loc_00AB312D:
loc_00AB3132:
    result = v_stack_p48;
    if (v_stack_p78 != 0) {
        Arg1 = v_stack_p78;
        result = ExFreePool(Arg1, v_stack_p48, v_stack_p60, (uint32_t)(0x20019ULL));
    }
    if (v_stack_p70 != 0) goto loc_00AB2EB5;
    goto loc_00AB2EBC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB2A24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
