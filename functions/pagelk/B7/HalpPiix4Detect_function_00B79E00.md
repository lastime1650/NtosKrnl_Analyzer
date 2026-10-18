# HalpPiix4Detect

- RVA: `0x00B79E00`–`0x00B7A452` (길이 `1,618` bytes)
- VA: `0x0000000140B79E00`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B8D50`
- 디코드: `410`개 명령, `1,618/1,618` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **20**

### Outgoing calls
- `0x00B79E7D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B79F3C` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00B79F8E` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00B79FA7` → [HalpGetCpuInfo](../../text/49/HalpGetCpuInfo_function_00498A70.md) (function, `0x00498A70`)
- `0x00B7A015` → [HalGetBusData](../../text/53/HalGetBusData_function_0053F280.md) (function, `0x0053F280`)
- `0x00B7A04D` → [HalGetBusData](../../text/53/HalGetBusData_function_0053F280.md) (function, `0x0053F280`)
- `0x00B7A05A` → [HalpInterruptModel](../../text/4A/HalpInterruptModel_function_004ACA38.md) (function, `0x004ACA38`)
- `0x00B7A09A` → [HalpInterruptSetMsiOverride](../../text/54/HalpInterruptSetMsiOverride_function_00544748.md) (function, `0x00544748`)
- `0x00B7A0E5` → [HalGetBusDataByOffset](../../text/46/HalGetBusDataByOffset_function_00461730.md) (function, `0x00461730`)
- `0x00B7A11E` → [HalpGetChipHacks](../../init/C2/HalpGetChipHacks_function_00C241CC.md) (function, `0x00C241CC`)
- `0x00B7A144` → [HalpWhackICHUsbSmi](../../text/56/HalpWhackICHUsbSmi_function_00563900.md) (function, `0x00563900`)
- `0x00B7A1F4` → [HalpInterruptSetLineSpecificOverride](../../text/54/HalpInterruptSetLineSpecificOverride_function_0054468C.md) (function, `0x0054468C`)
- `0x00B7A1FE` → [HalpInterruptSetLineSpecificOverride](../../text/54/HalpInterruptSetLineSpecificOverride_function_0054468C.md) (function, `0x0054468C`)
- `0x00B7A27F` → [HalGetBusData](../../text/53/HalGetBusData_function_0053F280.md) (function, `0x0053F280`)
- `0x00B7A2B3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B7A2E7` → [HalGetBusDataByOffset](../../text/46/HalGetBusDataByOffset_function_00461730.md) (function, `0x00461730`)
- `0x00B7A313` → [HalSetBusDataByOffset](../../text/46/HalSetBusDataByOffset_function_004614A0.md) (function, `0x004614A0`)
- `0x00B7A326` → [HalpUsbLegacyStopUhciInterrupt](../../text/56/HalpUsbLegacyStopUhciInterrupt_function_00563BD4.md) (function, `0x00563BD4`)
- `0x00B7A348` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00B7A3AF` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00B7A3DD` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x00B7A3FF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00B7A40E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00B7A41F` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00B7A42B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HalpAcpiDetectPiix4Work](../../page/70/HalpAcpiDetectPiix4Work_function_00708810.md) at `0x0070881E`
- [HaliInitPowerManagement](../../page/70/HaliInitPowerManagement_function_0070BAE0.md) at `0x0070BB21`
- [HalpAcpiPostSleep](HalpAcpiPostSleep_function_00B79990.md) at `0x00B79B19`

### Static image references
- `0x00B79E23` → RVA `0x00E0A740` (`.data`; read)
- `0x00B79E82` → RVA `0x0001C050` (`.rdata`; read)
- `0x00B79E98` → RVA `0x0001C0E8` (`.rdata`; read)
- `0x00B79EAF` → RVA `0x0001C078` (`.rdata`; read)
- `0x00B79EC5` → RVA `0x0001C090` (`.rdata`; read)
- `0x00B79EEC` → RVA `0x00F8FE30` (`.data`; read)
- `0x00B79F01` → RVA `0x00F8FE34` (`.data`; read/write)
- `0x00B7A10B` → RVA `0x00FC1AB0` (`.data`; write)
- `0x00B7A133` → RVA `0x00FC1ED9` (`.data`; write)
- `0x00B7A265` → RVA `0x00F8FE30` (`.data`; write)
- `0x00B7A287` → RVA `0x00FC1ED4` (`.data`; read)
- `0x00B7A28D` → RVA `0x00FC1AC8` (`.data`; write)
- `0x00B7A29D` → RVA `0x00025A10` (`.rdata`; read)
- `0x00B7A2C8` → RVA `0x00FC1AC4` (`.data`; read)
- `0x00B7A2D6` → RVA `0x00FC1AC0` (`.data`; write)
- `0x00B7A2DE` → RVA `0x00FC1ACC` (`.data`; write)
- `0x00B7A2EC` → RVA `0x00FC1ACC` (`.data`; read)
- `0x00B7A2FA` → RVA `0x00FC1AC0` (`.data`; read)
- `0x00B7A303` → RVA `0x00FC1AC4` (`.data`; read/write)
- `0x00B7A416` → RVA `0x00F8FE40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **25**
  - `0x00B79E7D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B79F3C` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGELK` → `.text`)
  - `0x00B79F8E` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGELK` → `.text`)
  - `0x00B79FA7` → [HalpGetCpuInfo](../../text/49/HalpGetCpuInfo_function_00498A70.md) (`PAGELK` → `.text`)
  - `0x00B7A015` → [HalGetBusData](../../text/53/HalGetBusData_function_0053F280.md) (`PAGELK` → `.text`)
  - `0x00B7A04D` → [HalGetBusData](../../text/53/HalGetBusData_function_0053F280.md) (`PAGELK` → `.text`)
  - `0x00B7A05A` → [HalpInterruptModel](../../text/4A/HalpInterruptModel_function_004ACA38.md) (`PAGELK` → `.text`)
  - `0x00B7A09A` → [HalpInterruptSetMsiOverride](../../text/54/HalpInterruptSetMsiOverride_function_00544748.md) (`PAGELK` → `.text`)
  - `0x00B7A0E5` → [HalGetBusDataByOffset](../../text/46/HalGetBusDataByOffset_function_00461730.md) (`PAGELK` → `.text`)
  - `0x00B7A11E` → [HalpGetChipHacks](../../init/C2/HalpGetChipHacks_function_00C241CC.md) (`PAGELK` → `INIT`)
  - `0x00B7A144` → [HalpWhackICHUsbSmi](../../text/56/HalpWhackICHUsbSmi_function_00563900.md) (`PAGELK` → `.text`)
  - `0x00B7A1F4` → [HalpInterruptSetLineSpecificOverride](../../text/54/HalpInterruptSetLineSpecificOverride_function_0054468C.md) (`PAGELK` → `.text`)
  - `0x00B7A1FE` → [HalpInterruptSetLineSpecificOverride](../../text/54/HalpInterruptSetLineSpecificOverride_function_0054468C.md) (`PAGELK` → `.text`)
  - `0x00B7A27F` → [HalGetBusData](../../text/53/HalGetBusData_function_0053F280.md) (`PAGELK` → `.text`)
  - `0x00B7A2B3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B7A2E7` → [HalGetBusDataByOffset](../../text/46/HalGetBusDataByOffset_function_00461730.md) (`PAGELK` → `.text`)
  - `0x00B7A313` → [HalSetBusDataByOffset](../../text/46/HalSetBusDataByOffset_function_004614A0.md) (`PAGELK` → `.text`)
  - `0x00B7A326` → [HalpUsbLegacyStopUhciInterrupt](../../text/56/HalpUsbLegacyStopUhciInterrupt_function_00563BD4.md) (`PAGELK` → `.text`)
  - `0x00B7A348` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGELK` → `.text`)
  - `0x00B7A3AF` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGELK` → `.text`)
  - `0x00B7A3DD` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGELK` → `.text`)
  - `0x00B7A3FF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGELK` → `.text`)
  - `0x00B7A40E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGELK` → `.text`)
  - `0x00B7A41F` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGELK` → `.text`)
  - `0x00B7A42B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B79E00  48 8B C4                        mov rax, rsp
00B79E03  48 89 58 08                     mov qword ptr [rax + 8], rbx
00B79E07  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00B79E0B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00B79E0F  55                              push rbp
00B79E10  41 54                           push r12
00B79E12  41 55                           push r13
00B79E14  41 56                           push r14
00B79E16  41 57                           push r15
00B79E18  48 8D 68 98                     lea rbp, [rax - 0x68]
00B79E1C  48 81 EC 40 01 00 00            sub rsp, 0x140
00B79E23  48 8B 05 16 09 29 00            mov rax, qword ptr [rip + 0x290916]
00B79E2A  48 33 C4                        xor rax, rsp
00B79E2D  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00B79E31  33 FF                           xor edi, edi
00B79E33  33 C0                           xor eax, eax
00B79E35  0F 57 C0                        xorps xmm0, xmm0
00B79E38  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00B79E3D  44 8A E9                        mov r13b, cl
00B79E40  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00B79E45  33 D2                           xor edx, edx
00B79E47  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00B79E4B  8D 5F 40                        lea ebx, [rdi + 0x40]
00B79E4E  40 88 7C 24 41                  mov byte ptr [rsp + 0x41], dil
00B79E53  44 8B C3                        mov r8d, ebx
00B79E56  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00B79E5A  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00B79E5E  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00B79E63  40 88 7C 24 42                  mov byte ptr [rsp + 0x42], dil
00B79E68  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
00B79E6C  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00B79E71  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00B79E75  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00B79E7A  89 45 90                        mov dword ptr [rbp - 0x70], eax
00B79E7D  E8 BE CD B4 FF                  call 0x1406c6c40
00B79E82  48 8D 05 C7 21 4A FF            lea rax, [rip - 0xb5de39]
00B79E89  48 C7 45 C8 24 00 26 00         mov qword ptr [rbp - 0x38], 0x260024
00B79E91  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00B79E95  8D 77 30                        lea esi, [rdi + 0x30]
00B79E98  48 8D 05 49 22 4A FF            lea rax, [rip - 0xb5ddb7]
00B79E9F  48 C7 45 B8 30 00 32 00         mov qword ptr [rbp - 0x48], 0x320030
00B79EA7  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00B79EAB  44 8D 77 01                     lea r14d, [rdi + 1]
00B79EAF  48 8D 05 C2 21 4A FF            lea rax, [rip - 0xb5de3e]
00B79EB6  48 C7 45 A8 16 00 18 00         mov qword ptr [rbp - 0x58], 0x180016
00B79EBE  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00B79EC2  0F 57 C0                        xorps xmm0, xmm0
00B79EC5  48 8D 05 C4 21 4A FF            lea rax, [rip - 0xb5de3c]
00B79ECC  48 C7 45 98 54 00 56 00         mov qword ptr [rbp - 0x68], 0x560054
00B79ED4  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00B79ED8  41 BF 19 00 02 00               mov r15d, 0x20019
00B79EDE  33 C0                           xor eax, eax
00B79EE0  89 45 30                        mov dword ptr [rbp + 0x30], eax
00B79EE3  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
00B79EE7  45 84 ED                        test r13b, r13b
00B79EEA  75 12                           jne 0x140b79efe
00B79EEC  40 38 3D 3D 5F 41 00            cmp byte ptr [rip + 0x415f3d], dil
00B79EF3  0F 85 A2 00 00 00               jne 0x140b79f9b
00B79EF9  E9 26 05 00 00                  jmp 0x140b7a424
00B79EFE  41 8B C6                        mov eax, r14d
00B79F01  F0 0F C1 05 2B 5F 41 00         lock xadd dword ptr [rip + 0x415f2b], eax
00B79F09  41 03 C6                        add eax, r14d
00B79F0C  41 3B C6                        cmp eax, r14d
00B79F0F  0F 85 0F 05 00 00               jne 0x140b7a424
00B79F15  48 8D 45 98                     lea rax, [rbp - 0x68]
00B79F19  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
00B79F1D  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00B79F22  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00B79F27  41 8B D7                        mov edx, r15d
00B79F2A  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00B79F2F  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00B79F34  89 5D 80                        mov dword ptr [rbp - 0x80], ebx
00B79F37  F3 0F 7F 45 88                  movdqu xmmword ptr [rbp - 0x78], xmm0
00B79F3C  E8 CF 33 B3 FF                  call 0x1406ad310
00B79F41  85 C0                           test eax, eax
00B79F43  0F 88 DB 04 00 00               js 0x140b7a424
00B79F49  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00B79F4E  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00B79F53  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00B79F58  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00B79F5D  48 8D 45 A8                     lea rax, [rbp - 0x58]
00B79F61  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
00B79F65  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00B79F6A  0F 57 C0                        xorps xmm0, xmm0
00B79F6D  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00B79F72  89 5D 80                        mov dword ptr [rbp - 0x80], ebx
00B79F75  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B79F7A  45 33 C9                        xor r9d, r9d
00B79F7D  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00B79F81  41 8B D7                        mov edx, r15d
00B79F84  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B79F89  F3 0F 7F 45 88                  movdqu xmmword ptr [rbp - 0x78], xmm0
00B79F8E  E8 DD 34 B3 FF                  call 0x1406ad470
00B79F93  85 C0                           test eax, eax
00B79F95  0F 88 5A 04 00 00               js 0x140b7a3f5
00B79F9B  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00B79FA0  45 33 C0                        xor r8d, r8d
00B79FA3  33 D2                           xor edx, edx
00B79FA5  33 C9                           xor ecx, ecx
00B79FA7  E8 C4 EA 91 FF                  call 0x140498a70
00B79FAC  F6 D8                           neg al
00B79FAE  44 8A E7                        mov r12b, dil
00B79FB1  8B F7                           mov esi, edi
00B79FB3  45 1A FF                        sbb r15b, r15b
00B79FB6  44 22 7C 24 40                  and r15b, byte ptr [rsp + 0x40]
00B79FBB  81 FE 00 01 00 00               cmp esi, 0x100
00B79FC1  0F 83 6E 03 00 00               jae 0x140b7a335
00B79FC7  8B DF                           mov ebx, edi
00B79FC9  44 8B F7                        mov r14d, edi
00B79FCC  B8 01 00 00 00                  mov eax, 1
00B79FD1  41 83 FE 20                     cmp r14d, 0x20
00B79FD5  0F 83 6A 02 00 00               jae 0x140b7a245
00B79FDB  83 FF 08                        cmp edi, 8
00B79FDE  0F 83 57 02 00 00               jae 0x140b7a23b
00B79FE4  8B C3                           mov eax, ebx
00B79FE6  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
00B79FEE  25 00 FF FF FF                  and eax, 0xffffff00
00B79FF3  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00B79FF7  8B CF                           mov ecx, edi
00B79FF9  8B D6                           mov edx, esi
00B79FFB  83 E1 07                        and ecx, 7
00B79FFE  C1 E1 05                        shl ecx, 5
00B7A001  8B D9                           mov ebx, ecx
00B7A003  B9 04 00 00 00                  mov ecx, 4
00B7A008  0B D8                           or ebx, eax
00B7A00A  41 8B C6                        mov eax, r14d
00B7A00D  83 E0 1F                        and eax, 0x1f
00B7A010  0B D8                           or ebx, eax
00B7A012  44 8B C3                        mov r8d, ebx
00B7A015  E8 66 52 9C FF                  call 0x14053f280
00B7A01A  85 C0                           test eax, eax
00B7A01C  0F 84 0B 03 00 00               je 0x140b7a32d
00B7A022  0F B7 45 E0                     movzx eax, word ptr [rbp - 0x20]
00B7A026  B9 FD FF 00 00                  mov ecx, 0xfffd
00B7A02B  66 FF C8                        dec ax
00B7A02E  66 3B C1                        cmp ax, cx
00B7A031  0F 87 EF 01 00 00               ja 0x140b7a226
00B7A037  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00B7A03B  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
00B7A043  44 8B C3                        mov r8d, ebx
00B7A046  8B D6                           mov edx, esi
00B7A048  B9 04 00 00 00                  mov ecx, 4
00B7A04D  E8 2E 52 9C FF                  call 0x14053f280
00B7A052  85 C0                           test eax, eax
00B7A054  0F 84 D0 01 00 00               je 0x140b7a22a
00B7A05A  E8 D9 29 93 FF                  call 0x1404aca38
00B7A05F  45 84 ED                        test r13b, r13b
00B7A062  0F 84 9B 01 00 00               je 0x140b7a203
00B7A068  44 8A 45 E8                     mov r8b, byte ptr [rbp - 0x18]
00B7A06C  BA 01 00 00 00                  mov edx, 1
00B7A071  44 0F B7 55 E0                  movzx r10d, word ptr [rbp - 0x20]
00B7A076  3B C2                           cmp eax, edx
00B7A078  75 25                           jne 0x140b7a09f
00B7A07A  85 F6                           test esi, esi
00B7A07C  75 21                           jne 0x140b7a09f
00B7A07E  45 85 F6                        test r14d, r14d
00B7A081  75 1C                           jne 0x140b7a09f
00B7A083  85 FF                           test edi, edi
00B7A085  75 18                           jne 0x140b7a09f
00B7A087  B8 06 11 00 00                  mov eax, 0x1106
00B7A08C  66 44 3B D0                     cmp r10w, ax
00B7A090  75 0D                           jne 0x140b7a09f
00B7A092  41 80 F8 80                     cmp r8b, 0x80
00B7A096  73 07                           jae 0x140b7a09f
00B7A098  33 C9                           xor ecx, ecx
00B7A09A  E8 A9 A6 9C FF                  call 0x140544748
00B7A09F  B8 86 80 00 00                  mov eax, 0x8086
00B7A0A4  66 44 3B D0                     cmp r10w, ax
00B7A0A8  75 67                           jne 0x140b7a111
00B7A0AA  0F B7 45 E2                     movzx eax, word ptr [rbp - 0x1e]
00B7A0AE  B9 90 71 00 00                  mov ecx, 0x7190
00B7A0B3  66 2B C1                        sub ax, cx
00B7A0B6  B9 FD FF 00 00                  mov ecx, 0xfffd
00B7A0BB  66 85 C1                        test cx, ax
00B7A0BE  75 51                           jne 0x140b7a111
00B7A0C0  41 80 F8 02                     cmp r8b, 2
00B7A0C4  77 4B                           ja 0x140b7a111
00B7A0C6  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00B7A0CA  4C 8D 4C 24 41                  lea r9, [rsp + 0x41]
00B7A0CF  88 54 24 42                     mov byte ptr [rsp + 0x42], dl
00B7A0D3  44 8B C3                        mov r8d, ebx
00B7A0D6  8B D6                           mov edx, esi
00B7A0D8  C7 44 24 20 57 00 00 00         mov dword ptr [rsp + 0x20], 0x57
00B7A0E0  B9 04 00 00 00                  mov ecx, 4
00B7A0E5  E8 46 76 8E FF                  call 0x140461730
00B7A0EA  8A 4C 24 41                     mov cl, byte ptr [rsp + 0x41]
00B7A0EE  44 8A 45 E8                     mov r8b, byte ptr [rbp - 0x18]
00B7A0F2  F6 C1 18                        test cl, 0x18
00B7A0F5  44 0F B7 55 E0                  movzx r10d, word ptr [rbp - 0x20]
00B7A0FA  0F 95 C0                        setne al
00B7A0FD  C0 E9 05                        shr cl, 5
00B7A100  22 C1                           and al, cl
00B7A102  B9 01 00 00 00                  mov ecx, 1
00B7A107  84 C1                           test cl, al
00B7A109  74 06                           je 0x140b7a111
00B7A10B  88 0D 9F 79 44 00               mov byte ptr [rip + 0x44799f], cl
00B7A111  0F B7 55 E2                     movzx edx, word ptr [rbp - 0x1e]
00B7A115  4C 8D 4C 24 44                  lea r9, [rsp + 0x44]
00B7A11A  41 0F B7 CA                     movzx ecx, r10w
00B7A11E  E8 A9 A0 0A 00                  call 0x140c241cc
00B7A123  85 C0                           test eax, eax
00B7A125  78 22                           js 0x140b7a149
00B7A127  F6 44 24 44 02                  test byte ptr [rsp + 0x44], 2
00B7A12C  74 0B                           je 0x140b7a139
00B7A12E  B8 01 00 00 00                  mov eax, 1
00B7A133  88 05 A0 7D 44 00               mov byte ptr [rip + 0x447da0], al
00B7A139  F6 44 24 44 08                  test byte ptr [rsp + 0x44], 8
00B7A13E  74 09                           je 0x140b7a149
00B7A140  8B D3                           mov edx, ebx
00B7A142  8B CE                           mov ecx, esi
00B7A144  E8 B7 97 9E FF                  call 0x140563900
00B7A149  41 80 FF 02                     cmp r15b, 2
00B7A14D  0F 85 B0 00 00 00               jne 0x140b7a203
00B7A153  45 84 E4                        test r12b, r12b
00B7A156  0F 85 A7 00 00 00               jne 0x140b7a203
00B7A15C  B8 86 80 00 00                  mov eax, 0x8086
00B7A161  66 39 45 E0                     cmp word ptr [rbp - 0x20], ax
00B7A165  0F 85 B1 00 00 00               jne 0x140b7a21c
00B7A16B  85 F6                           test esi, esi
00B7A16D  0F 85 9B 00 00 00               jne 0x140b7a20e
00B7A173  0F B7 45 E2                     movzx eax, word ptr [rbp - 0x1e]
00B7A177  41 83 FE 11                     cmp r14d, 0x11
00B7A17B  75 21                           jne 0x140b7a19e
00B7A17D  85 FF                           test edi, edi
00B7A17F  75 0A                           jne 0x140b7a18b
00B7A181  B9 D0 98 00 00                  mov ecx, 0x98d0
00B7A186  66 3B C1                        cmp ax, cx
00B7A189  74 60                           je 0x140b7a1eb
00B7A18B  B9 01 00 00 00                  mov ecx, 1
00B7A190  3B F9                           cmp edi, ecx
00B7A192  75 7E                           jne 0x140b7a212
00B7A194  B9 D1 98 00 00                  mov ecx, 0x98d1
00B7A199  66 3B C1                        cmp ax, cx
00B7A19C  74 4D                           je 0x140b7a1eb
00B7A19E  41 83 FE 10                     cmp r14d, 0x10
00B7A1A2  75 6E                           jne 0x140b7a212
00B7A1A4  83 FF 06                        cmp edi, 6
00B7A1A7  75 0A                           jne 0x140b7a1b3
00B7A1A9  B9 D0 A0 00 00                  mov ecx, 0xa0d0
00B7A1AE  66 3B C1                        cmp ax, cx
00B7A1B1  74 38                           je 0x140b7a1eb
00B7A1B3  83 FF 07                        cmp edi, 7
00B7A1B6  75 0A                           jne 0x140b7a1c2
00B7A1B8  B9 D1 A0 00 00                  mov ecx, 0xa0d1
00B7A1BD  66 3B C1                        cmp ax, cx
00B7A1C0  74 29                           je 0x140b7a1eb
00B7A1C2  8A 4D E8                        mov cl, byte ptr [rbp - 0x18]
00B7A1C5  83 FF 06                        cmp edi, 6
00B7A1C8  75 0E                           jne 0x140b7a1d8
00B7A1CA  BA D0 43 00 00                  mov edx, 0x43d0
00B7A1CF  66 3B C2                        cmp ax, dx
00B7A1D2  75 3E                           jne 0x140b7a212
00B7A1D4  84 C9                           test cl, cl
00B7A1D6  74 13                           je 0x140b7a1eb
00B7A1D8  83 FF 07                        cmp edi, 7
00B7A1DB  75 35                           jne 0x140b7a212
00B7A1DD  BA D1 43 00 00                  mov edx, 0x43d1
00B7A1E2  66 3B C2                        cmp ax, dx
00B7A1E5  75 2B                           jne 0x140b7a212
00B7A1E7  84 C9                           test cl, cl
00B7A1E9  75 3F                           jne 0x140b7a22a
00B7A1EB  B9 17 00 00 00                  mov ecx, 0x17
00B7A1F0  44 8D 61 EA                     lea r12d, [rcx - 0x16]
00B7A1F4  E8 93 A4 9C FF                  call 0x14054468c
00B7A1F9  41 8D 4C 24 15                  lea ecx, [r12 + 0x15]
00B7A1FE  E8 89 A4 9C FF                  call 0x14054468c
00B7A203  B8 86 80 00 00                  mov eax, 0x8086
00B7A208  66 39 45 E0                     cmp word ptr [rbp - 0x20], ax
00B7A20C  75 0E                           jne 0x140b7a21c
00B7A20E  0F B7 45 E2                     movzx eax, word ptr [rbp - 0x1e]
00B7A212  B9 10 71 00 00                  mov ecx, 0x7110
00B7A217  66 3B C1                        cmp ax, cx
00B7A21A  74 37                           je 0x140b7a253
00B7A21C  85 FF                           test edi, edi
00B7A21E  75 0A                           jne 0x140b7a22a
00B7A220  F6 45 EE 80                     test byte ptr [rbp - 0x12], 0x80
00B7A224  EB 02                           jmp 0x140b7a228
00B7A226  85 FF                           test edi, edi
00B7A228  74 0C                           je 0x140b7a236
00B7A22A  B8 01 00 00 00                  mov eax, 1
00B7A22F  03 F8                           add edi, eax
00B7A231  E9 A5 FD FF FF                  jmp 0x140b79fdb
00B7A236  B8 01 00 00 00                  mov eax, 1
00B7A23B  44 03 F0                        add r14d, eax
00B7A23E  33 FF                           xor edi, edi
00B7A240  E9 8C FD FF FF                  jmp 0x140b79fd1
00B7A245  41 BE 01 00 00 00               mov r14d, 1
00B7A24B  41 03 F6                        add esi, r14d
00B7A24E  E9 68 FD FF FF                  jmp 0x140b79fbb
00B7A253  41 BE 01 00 00 00               mov r14d, 1
00B7A259  C7 44 24 20 40 00 00 00         mov dword ptr [rsp + 0x20], 0x40
00B7A261  0F BA F3 07                     btr ebx, 7
00B7A265  44 88 35 C4 5B 41 00            mov byte ptr [rip + 0x415bc4], r14b
00B7A26C  83 CB 60                        or ebx, 0x60
00B7A26F  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00B7A273  44 8B C3                        mov r8d, ebx
00B7A276  8B D6                           mov edx, esi
00B7A278  45 8D 7E 03                     lea r15d, [r14 + 3]
00B7A27C  41 8B CF                        mov ecx, r15d
00B7A27F  E8 FC 4F 9C FF                  call 0x14053f280
00B7A284  8A 4D E8                        mov cl, byte ptr [rbp - 0x18]
00B7A287  8B 05 47 7C 44 00               mov eax, dword ptr [rip + 0x447c47]
00B7A28D  88 0D 35 78 44 00               mov byte ptr [rip + 0x447835], cl
00B7A293  A8 02                           test al, 2
00B7A295  75 22                           jne 0x140b7a2b9
00B7A297  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B7A29D  4C 8D 05 6C B7 4A FF            lea r8, [rip - 0xb54894]
00B7A2A4  41 B9 7B 06 00 00               mov r9d, 0x67b
00B7A2AA  41 8D 4E 5B                     lea ecx, [r14 + 0x5b]
00B7A2AE  BA 11 01 00 00                  mov edx, 0x111
00B7A2B3  E8 A8 33 98 FF                  call 0x1404fd660
00B7A2B8  CC                              int3
00B7A2B9  41 3A CE                        cmp cl, r14b
00B7A2BC  77 5A                           ja 0x140b7a318
00B7A2BE  BF 58 00 00 00                  mov edi, 0x58
00B7A2C3  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00B7A2C8  4C 8D 0D F5 77 44 00            lea r9, [rip + 0x4477f5]
00B7A2CF  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00B7A2D3  44 8B C3                        mov r8d, ebx
00B7A2D6  89 35 E4 77 44 00               mov dword ptr [rip + 0x4477e4], esi
00B7A2DC  8B D6                           mov edx, esi
00B7A2DE  89 1D E8 77 44 00               mov dword ptr [rip + 0x4477e8], ebx
00B7A2E4  41 8B CF                        mov ecx, r15d
00B7A2E7  E8 44 74 8E FF                  call 0x140461730
00B7A2EC  44 8B 05 D9 77 44 00            mov r8d, dword ptr [rip + 0x4477d9]
00B7A2F3  4C 8D 0D CA 77 44 00            lea r9, [rip + 0x4477ca]
00B7A2FA  8B 15 C0 77 44 00               mov edx, dword ptr [rip + 0x4477c0]
00B7A300  41 8B CF                        mov ecx, r15d
00B7A303  83 0D BA 77 44 00 23            or dword ptr [rip + 0x4477ba], 0x23
00B7A30A  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00B7A30F  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00B7A313  E8 88 71 8E FF                  call 0x1404614a0
00B7A318  81 E3 5F FF FF FF               and ebx, 0xffffff5f
00B7A31E  45 8A CE                        mov r9b, r14b
00B7A321  44 8B C3                        mov r8d, ebx
00B7A324  8B D6                           mov edx, esi
00B7A326  E8 A9 98 9E FF                  call 0x140563bd4
00B7A32B  EB 06                           jmp 0x140b7a333
00B7A32D  41 BE 01 00 00 00               mov r14d, 1
00B7A333  33 FF                           xor edi, edi
00B7A335  45 84 ED                        test r13b, r13b
00B7A338  0F 84 E6 00 00 00               je 0x140b7a424
00B7A33E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00B7A343  48 85 C9                        test rcx, rcx
00B7A346  74 0D                           je 0x140b7a355
00B7A348  E8 63 2F B3 FF                  call 0x1406ad2b0
00B7A34D  48 8B CF                        mov rcx, rdi
00B7A350  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00B7A355  40 38 7C 24 42                  cmp byte ptr [rsp + 0x42], dil
00B7A35A  0F 84 9A 00 00 00               je 0x140b7a3fa
00B7A360  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00B7A365  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00B7A36A  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00B7A36F  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00B7A374  48 8D 45 B8                     lea rax, [rbp - 0x48]
00B7A378  C7 44 24 68 30 00 00 00         mov dword ptr [rsp + 0x68], 0x30
00B7A380  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00B7A385  0F 57 C0                        xorps xmm0, xmm0
00B7A388  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00B7A38D  C7 45 80 40 00 00 00            mov dword ptr [rbp - 0x80], 0x40
00B7A394  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B7A399  45 33 C9                        xor r9d, r9d
00B7A39C  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00B7A3A0  BA 19 00 02 00                  mov edx, 0x20019
00B7A3A5  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B7A3AA  F3 0F 7F 45 88                  movdqu xmmword ptr [rbp - 0x78], xmm0
00B7A3AF  E8 BC 30 B3 FF                  call 0x1406ad470
00B7A3B4  85 C0                           test eax, eax
00B7A3B6  78 3D                           js 0x140b7a3f5
00B7A3B8  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00B7A3BD  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B7A3C2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B7A3C7  4C 8D 4D 20                     lea r9, [rbp + 0x20]
00B7A3CB  41 B8 02 00 00 00               mov r8d, 2
00B7A3D1  C7 44 24 20 14 00 00 00         mov dword ptr [rsp + 0x20], 0x14
00B7A3D9  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00B7A3DD  E8 CE 2F B3 FF                  call 0x1406ad3b0
00B7A3E2  85 C0                           test eax, eax
00B7A3E4  78 0F                           js 0x140b7a3f5
00B7A3E6  44 39 75 28                     cmp dword ptr [rbp + 0x28], r14d
00B7A3EA  72 09                           jb 0x140b7a3f5
00B7A3EC  8A 45 2C                        mov al, byte ptr [rbp + 0x2c]
00B7A3EF  88 05 BB 76 44 00               mov byte ptr [rip + 0x4476bb], al
00B7A3F5  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00B7A3FA  48 85 C9                        test rcx, rcx
00B7A3FD  74 05                           je 0x140b7a404
00B7A3FF  E8 AC 2E B3 FF                  call 0x1406ad2b0
00B7A404  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00B7A409  48 85 C9                        test rcx, rcx
00B7A40C  74 05                           je 0x140b7a413
00B7A40E  E8 9D 2E B3 FF                  call 0x1406ad2b0
00B7A413  45 33 C0                        xor r8d, r8d
00B7A416  48 8D 0D 23 5A 41 00            lea rcx, [rip + 0x415a23]
00B7A41D  33 D2                           xor edx, edx
00B7A41F  E8 EC 4E 7C FF                  call 0x14033f310
00B7A424  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
00B7A428  48 33 CC                        xor rcx, rsp
00B7A42B  E8 10 22 B3 FF                  call 0x1406ac640
00B7A430  4C 8D 9C 24 40 01 00 00         lea r11, [rsp + 0x140]
00B7A438  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00B7A43C  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00B7A440  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00B7A444  49 8B E3                        mov rsp, r11
00B7A447  41 5F                           pop r15
00B7A449  41 5E                           pop r14
00B7A44B  41 5D                           pop r13
00B7A44D  41 5C                           pop r12
00B7A44F  5D                              pop rbp
00B7A450  C3                              ret
00B7A451  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpPiix4Detect(unsigned __int8 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m124;
    unsigned __int8 v_stack_m126;
    unsigned __int8 v_stack_m127;
    unsigned __int8 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 2689302)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 104 + 56) = result;
    v_rdi = 0;
    result = 0;
    v_stack_m110 = 0;
    v_stack_m128 = 0;
    a2 = 0;
    v_stack_m118 = 0;
    v_stack_m127 = 0;
    v_stack_m124 = 0;
    v_stack_m120 = 0;
    v_stack_m126 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104 - 120) = 0;
    v_stack_mF0 = v_xmm0;
    *(unsigned int *)(v_rsp - 104 - 112) = 0;
    result = memset(v_rsp - 104 - 32, a2, (unsigned int)((unsigned int)(v_rdi + 64)), a4);
    *(unsigned __int64 *)(v_rsp - 104 - 56) = 0x260024ULL;
    *(unsigned __int64 *)(v_rsp - 104 - 48) = v_rip - 11918905;
    *(unsigned __int64 *)(v_rsp - 104 - 72) = 0x320030ULL;
    *(unsigned __int64 *)(v_rsp - 104 - 64) = v_rip - 11918775;
    *(unsigned __int64 *)(v_rsp - 104 - 88) = 0x180016ULL;
    *(unsigned __int64 *)(v_rsp - 104 - 80) = v_rip - 11918910;
    *(unsigned __int64 *)(v_rsp - 104 - 104) = 0x560054ULL;
    *(unsigned __int64 *)(v_rsp - 104 - 96) = v_rip - 11918908;
    result = 0;
    *(unsigned int *)(v_rsp - 104 + 48) = 0;
    *(unsigned __int64 *)(v_rsp - 104 + 32) = v_xmm0;
    if (a1 != 0) goto loc_00B79EFE;
    if ((*(unsigned __int8 *)(v_rip + 4284221)) != 0) goto loc_00B79F9B;
    goto loc_00B7A424;
loc_00B79EFE:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) + ((unsigned int)(v_rdi + 1)));
    if (((unsigned int)(result)) != ((unsigned int)(v_rdi + 1))) goto loc_00B7A424;
    v_stack_m100 = (unsigned int)(v_rdi + 48);
    v_stack_mF0 = v_rsp - 104 - 104;
    v_stack_mF8 = 0;
    *(unsigned int *)(v_rsp - 104 - 128) = (unsigned int)(v_rdi + 64);
    *(unsigned __int64 *)(v_rsp - 104 - 120) = v_xmm0;
    result = ZwOpenKey(v_stack_m110, (unsigned int)((unsigned int)((unsigned int)(0x20019ULL))), v_stack_m100, a4);
    if (sign_flag) goto loc_00B7A424;
    v_stack_mF8 = v_stack_m110;
    v_stack_m100 = (unsigned int)(v_rdi + 48);
    v_stack_mF0 = v_rsp - 104 - 88;
    *(unsigned int *)(v_rsp - 104 - 128) = (unsigned int)(v_rdi + 64);
    v_stack_m138 = v_stack_m118;
    a4 = 0;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 120) = v_xmm0;
    result = ZwCreateKey(v_stack_m120, (unsigned int)((unsigned int)((unsigned int)(0x20019ULL))), v_stack_m100, a4);
    if (sign_flag) goto loc_00B7A3F5;
loc_00B79F9B:
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = HalpGetCpuInfo(a1, a2, a3, v_stack_m128);
    result = (unsigned __int8)(-(result));
    v_r15 = (unsigned __int8)(((unsigned int)(0x20019ULL)) & (v_stack_m128));
loc_00B79FBB:
    if (0 >= 256) goto loc_00B7A335;
loc_00B79FD1:
    if (0 >= 32) goto loc_00B7A245;
loc_00B79FDB:
    if (0 >= 8) goto loc_00B7A23B;
    v_stack_m148 = 2;
    result = (unsigned int)((0) & (0xFFFFFF00ULL));
    a1 = (unsigned int)((0) & (7));
    a1 = (unsigned int)((a1) << (5));
    v_rbx = (unsigned int)(((unsigned int)(a1)) | ((unsigned int)(result)));
    result = (unsigned int)((0) & (31));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    result = HalGetBusData(4, 0, (unsigned int)((unsigned int)(v_rbx)), v_rsp - 104 - 32);
    if ((unsigned int)(result) == 0) goto loc_00B7A32D;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rsp - 104 - 32)) - 1);
    if (((unsigned __int16)(result)) > ((unsigned __int16)((unsigned int)(0xFFFDULL)))) goto loc_00B7A226;
    v_stack_m148 = 16;
    result = HalGetBusData(4, 0, (unsigned int)((unsigned int)(v_rbx)), v_rsp - 104 - 32);
    if ((unsigned int)(result) == 0) goto loc_00B7A22A;
    result = HalpInterruptModel(4, 0, (unsigned int)((unsigned int)(v_rbx)), v_rsp - 104 - 32);
    if (a1 == 0) goto loc_00B7A203;
    if (((unsigned int)(result)) != 1) goto loc_00B7A09F;
    if (0 != 0) goto loc_00B7A09F;
    if (0 != 0) goto loc_00B7A09F;
    if (0 != 0) goto loc_00B7A09F;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 32))) != ((unsigned __int16)((unsigned int)(0x1106ULL)))) goto loc_00B7A09F;
    result = (unsigned int)(0x1106ULL);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 - 24))) < 128) {
        a1 = 0;
        result = HalpInterruptSetMsiOverride(a1, 1, *(unsigned __int8 *)(v_rsp - 104 - 24), v_rsp - 104 - 32);
    }
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 32))) != ((unsigned __int16)((unsigned int)(0x8086ULL)))) goto loc_00B7A111;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rsp - 104 - 30)) - ((unsigned __int16)((unsigned int)(0x7190ULL))));
    if ((((unsigned __int16)((unsigned int)(0xFFFDULL))) & ((unsigned __int16)(result))) != 0) goto loc_00B7A111;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 - 24))) > 2) goto loc_00B7A111;
    v_stack_m140 = 1;
    v_stack_m126 = 1;
    v_stack_m148 = 87;
    result = HalGetBusDataByOffset(4, 0, (unsigned int)((unsigned int)(v_rbx)), v_stack_m127);
    result = ((((unsigned __int8)(v_stack_m127)) & (24)) != 0) ? 1 : 0;
    a1 = (unsigned __int8)((v_stack_m127) >> (5));
    result = (unsigned __int8)((result) & (a1));
    if (((1) & ((unsigned __int8)(result))) != 0) {
        *(unsigned __int8 *)(v_rip + 4487583) = 1;
    }
    result = HalpGetChipHacks((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 32)), *(unsigned __int16 *)(v_rsp - 104 - 30), *(unsigned __int8 *)(v_rsp - 104 - 24), v_stack_m124);
    if (sign_flag) goto loc_00B7A149;
    if (((v_stack_m124) & (2)) != 0) {
        result = 1;
        *(unsigned __int8 *)(v_rip + 4488608) = (unsigned __int8)(result);
    }
    if (((v_stack_m124) & (8)) != 0) {
        a2 = (unsigned int)(v_rbx);
        a1 = 0;
        result = HalpWhackICHUsbSmi(a1, a2, *(unsigned __int8 *)(v_rsp - 104 - 24), v_stack_m124);
    }
    if (((unsigned __int8)(v_r15)) != 2) goto loc_00B7A203;
    if (0 != 0) goto loc_00B7A203;
    if ((*(unsigned __int16 *)(v_rsp - 104 - 32)) != ((unsigned __int16)((unsigned int)(0x8086ULL)))) goto loc_00B7A21C;
    if (0 != 0) goto loc_00B7A20E;
    if (0 != 17) goto loc_00B7A19E;
    if (0 != 0) goto loc_00B7A18B;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 30))) == ((unsigned __int16)((unsigned int)(0x98D0ULL)))) goto loc_00B7A1EB;
loc_00B7A18B:
    if (0 != 1) goto loc_00B7A212;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 30))) == ((unsigned __int16)((unsigned int)(0x98D1ULL)))) goto loc_00B7A1EB;
loc_00B7A19E:
    if (0 != 16) goto loc_00B7A212;
    if (0 != 6) goto loc_00B7A1B3;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 30))) == ((unsigned __int16)((unsigned int)(0xA0D0ULL)))) goto loc_00B7A1EB;
loc_00B7A1B3:
    if (0 != 7) goto loc_00B7A1C2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 30))) == ((unsigned __int16)((unsigned int)(0xA0D1ULL)))) goto loc_00B7A1EB;
loc_00B7A1C2:
    if (0 != 6) goto loc_00B7A1D8;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 30))) != ((unsigned __int16)((unsigned int)(0x43D0ULL)))) goto loc_00B7A212;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 - 24)) == 0) goto loc_00B7A1EB;
loc_00B7A1D8:
    if (0 != 7) goto loc_00B7A212;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 30))) != ((unsigned __int16)((unsigned int)(0x43D1ULL)))) goto loc_00B7A212;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 - 24)) != 0) goto loc_00B7A22A;
loc_00B7A1EB:
    result = HalpInterruptSetLineSpecificOverride(23, (unsigned int)(0x43D1ULL), *(unsigned __int8 *)(v_rsp - 104 - 24), v_stack_m124);
    result = HalpInterruptSetLineSpecificOverride(23 - 22 + 21, (unsigned int)(0x43D1ULL), *(unsigned __int8 *)(v_rsp - 104 - 24), v_stack_m124);
loc_00B7A203:
    if ((*(unsigned __int16 *)(v_rsp - 104 - 32)) != ((unsigned __int16)((unsigned int)(0x8086ULL)))) goto loc_00B7A21C;
loc_00B7A20E:
loc_00B7A212:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 104 - 30))) == ((unsigned __int16)((unsigned int)(0x7110ULL)))) goto loc_00B7A253;
loc_00B7A21C:
    if (0 != 0) goto loc_00B7A22A;
    goto loc_00B7A228;
loc_00B7A226:
loc_00B7A228:
    if (0 == 0) goto loc_00B7A236;
loc_00B7A22A:
    v_rdi = (unsigned int)((v_rdi) + (1));
    goto loc_00B79FDB;
loc_00B7A236:
loc_00B7A23B:
    v_r14 = (unsigned int)((0) + (1));
    v_rdi = 0;
    goto loc_00B79FD1;
loc_00B7A245:
    v_rsi = (unsigned int)((0) + (1));
    goto loc_00B79FBB;
loc_00B7A253:
    v_stack_m148 = 64;
    *(unsigned __int8 *)(v_rip + 4283332) = 1;
    v_rbx = (unsigned int)((v_rbx) | (96));
    result = HalGetBusData((unsigned int)((unsigned int)(1 + 3)), (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)(v_rbx)), v_rsp - 104 - 32);
    *(unsigned __int8 *)(v_rip + 4487221) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 104 - 24));
    result = (unsigned int)(*(unsigned int *)(v_rip + 4488263));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4488263)))) & (2)) == 0) {
        a3 = v_rip - 11880596;
        a4 = 0x67BULL;
        a1 = 1 + 91;
        a2 = 273;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (a1 <= 1) {
        v_rdi = 88;
        v_stack_m140 = (unsigned int)(1 + 3);
        a4 = v_rip + 4487157;
        v_stack_m148 = (unsigned int)(v_rdi);
        a3 = (unsigned int)(v_rbx);
        *(unsigned int *)(v_rip + 4487140) = (unsigned int)(v_rsi);
        a2 = (unsigned int)(v_rsi);
        *(unsigned int *)(v_rip + 4487144) = (unsigned int)(v_rbx);
        a1 = (unsigned int)(1 + 3);
        result = HalGetBusDataByOffset(a1, a2, a3, a4);
        a3 = *(unsigned int *)(v_rip + 4487129);
        a4 = v_rip + 4487114;
        a2 = *(unsigned int *)(v_rip + 4487104);
        a1 = (unsigned int)(1 + 3);
        v_stack_m140 = (unsigned int)(1 + 3);
        v_stack_m148 = (unsigned int)(v_rdi);
        result = HalSetBusDataByOffset(a1, a2, a3, a4);
    }
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFF5FULL));
    result = HalpUsbLegacyStopUhciInterrupt(a1, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)(v_rbx)), 1);
    goto loc_00B7A333;
loc_00B7A32D:
loc_00B7A333:
    v_rdi = 0;
loc_00B7A335:
    if (a1 == 0) goto loc_00B7A424;
    if (v_stack_m120 != 0) {
        result = ZwClose(v_stack_m120, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)(v_rbx)), 1);
        a1 = 0;
        v_stack_m120 = a1;
    }
    if (v_stack_m126 == 0) goto loc_00B7A3FA;
    v_stack_mF8 = v_stack_m110;
    v_stack_m100 = 48;
    v_stack_mF0 = v_rsp - 104 - 72;
    *(unsigned int *)(v_rsp - 104 - 128) = 64;
    v_stack_m138 = v_stack_m118;
    a4 = 0;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    *(unsigned __int64 *)(v_rsp - 104 - 120) = v_xmm0;
    result = ZwCreateKey(v_stack_m120, (unsigned int)(0x20019ULL), v_stack_m100, a4);
    if (sign_flag) goto loc_00B7A3F5;
    v_stack_m140 = v_stack_m108;
    v_stack_m148 = 20;
    result = ZwQueryValueKey(v_stack_m120, v_rsp - 104 - 56, 2, v_rsp - 104 + 32);
    if (sign_flag) goto loc_00B7A3F5;
    if ((*(unsigned int *)(v_rsp - 104 + 40)) >= 1) {
        result = *(unsigned __int8 *)(v_rsp - 104 + 44);
        *(unsigned __int8 *)(v_rip + 4486843) = (unsigned __int8)(result);
    }
loc_00B7A3FA:
    if (v_stack_m120 != 0) {
        result = ZwClose(v_stack_m120, v_rsp - 104 - 56, 2, v_rsp - 104 + 32);
    }
    if (v_stack_m110 != 0) {
        result = ZwClose(v_stack_m110, v_rsp - 104 - 56, 2, v_rsp - 104 + 32);
    }
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 4282915, a2, a3, v_rsp - 104 + 32);
loc_00B7A424:
    a1 = (*(unsigned __int64 *)(v_rsp - 104 + 56)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_rsp - 104 + 32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpPiix4Detect(uint8_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m124;
    uint8_t v_stack_m126;
    uint8_t v_stack_m127;
    uint8_t v_stack_m128;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m28;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x290916)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x68 + 0x38) = result;
    local_rdi = 0;
    result = 0;
    v_stack_m110 = 0;
    v_stack_m128 = 0;
    Arg2 = 0;
    v_stack_m118 = 0;
    v_stack_m127 = 0;
    v_stack_m124 = 0;
    v_stack_m120 = 0;
    v_stack_m126 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68 - 0x78) = 0;
    v_stack_mF0 = v_xmm0;
    *(uint32_t *)(local_rsp - 0x68 - 0x70) = 0;
    result = memset(local_rsp - 104 - 32, Arg2, (uint32_t)((uint32_t)(local_rdi + 64)), Arg4);
    *(uint64_t *)(local_rsp - 0x68 - 0x38) = 0x260024ULL;
    *(uint64_t *)(local_rsp - 0x68 - 0x30) = v_rip - 11918905;
    *(uint64_t *)(local_rsp - 0x68 - 0x48) = 0x320030ULL;
    *(uint64_t *)(local_rsp - 0x68 - 0x40) = v_rip - 11918775;
    *(uint64_t *)(local_rsp - 0x68 - 0x58) = 0x180016ULL;
    *(uint64_t *)(local_rsp - 0x68 - 0x50) = v_rip - 11918910;
    *(uint64_t *)(local_rsp - 0x68 - 0x68) = 0x560054ULL;
    *(uint64_t *)(local_rsp - 0x68 - 0x60) = v_rip - 11918908;
    result = 0;
    *(uint32_t *)(local_rsp - 0x68 + 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x68 + 0x20) = v_xmm0;
    if (Arg1 != 0) goto loc_00B79EFE;
    if ((*(uint8_t *)(v_rip + 0x415F3D)) != 0) goto loc_00B79F9B;
    goto loc_00B7A424;
loc_00B79EFE:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) + ((uint32_t)(local_rdi + 1)));
    if (((uint32_t)(result)) != ((uint32_t)(local_rdi + 1))) goto loc_00B7A424;
    v_stack_m100 = (uint32_t)(local_rdi + 48);
    v_stack_mF0 = local_rsp - 104 - 104;
    v_stack_mF8 = 0;
    *(uint32_t *)(local_rsp - 0x68 - 0x80) = (uint32_t)(local_rdi + 64);
    *(uint64_t *)(local_rsp - 0x68 - 0x78) = v_xmm0;
    result = ZwOpenKey(v_stack_m110, (uint32_t)((uint32_t)((uint32_t)(0x20019ULL))), v_stack_m100, Arg4);
    if (sign_flag) goto loc_00B7A424;
    v_stack_mF8 = v_stack_m110;
    v_stack_m100 = (uint32_t)(local_rdi + 48);
    v_stack_mF0 = local_rsp - 104 - 88;
    *(uint32_t *)(local_rsp - 0x68 - 0x80) = (uint32_t)(local_rdi + 64);
    v_stack_m138 = v_stack_m118;
    Arg4 = 0;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x78) = v_xmm0;
    result = ZwCreateKey(v_stack_m120, (uint32_t)((uint32_t)((uint32_t)(0x20019ULL))), v_stack_m100, Arg4);
    if (sign_flag) goto loc_00B7A3F5;
loc_00B79F9B:
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = HalpGetCpuInfo(Arg1, Arg2, Arg3, v_stack_m128);
    result = (uint8_t)(-(result));
    local_r15 = (uint8_t)(((uint32_t)(0x20019ULL)) & (v_stack_m128));
loc_00B79FBB:
    if (0 >= 256) goto loc_00B7A335;
loc_00B79FD1:
    if (0 >= 32) goto loc_00B7A245;
loc_00B79FDB:
    if (0 >= 8) goto loc_00B7A23B;
    v_stack_m148 = 2;
    result = (uint32_t)((0) & (0xFFFFFF00ULL));
    Arg1 = (uint32_t)((0) & (7));
    Arg1 = (uint32_t)((Arg1) << (5));
    local_rbx = (uint32_t)(((uint32_t)(Arg1)) | ((uint32_t)(result)));
    result = (uint32_t)((0) & (31));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    result = HalGetBusData(4, 0, (uint32_t)((uint32_t)(local_rbx)), local_rsp - 104 - 32);
    if ((uint32_t)(result) == 0) goto loc_00B7A32D;
    result = (uint16_t)((*(uint16_t *)(local_rsp - 0x68 - 0x20)) - 1);
    if (((uint16_t)(result)) > ((uint16_t)((uint32_t)(0xFFFDULL)))) goto loc_00B7A226;
    v_stack_m148 = 16;
    result = HalGetBusData(4, 0, (uint32_t)((uint32_t)(local_rbx)), local_rsp - 104 - 32);
    if ((uint32_t)(result) == 0) goto loc_00B7A22A;
    result = HalpInterruptModel(4, 0, (uint32_t)((uint32_t)(local_rbx)), local_rsp - 104 - 32);
    if (Arg1 == 0) goto loc_00B7A203;
    if (((uint32_t)(result)) != 1) goto loc_00B7A09F;
    if (0 != 0) goto loc_00B7A09F;
    if (0 != 0) goto loc_00B7A09F;
    if (0 != 0) goto loc_00B7A09F;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x20))) != ((uint16_t)((uint32_t)(0x1106ULL)))) goto loc_00B7A09F;
    result = (uint32_t)(0x1106ULL);
    if (((uint8_t)(*(uint8_t *)(local_rsp - 0x68 - 0x18))) < 128) {
        Arg1 = 0;
        result = HalpInterruptSetMsiOverride(Arg1, 1, *(uint8_t *)(local_rsp - 0x68 - 0x18), local_rsp - 104 - 32);
    }
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x20))) != ((uint16_t)((uint32_t)(0x8086ULL)))) goto loc_00B7A111;
    result = (uint16_t)((*(uint16_t *)(local_rsp - 0x68 - 0x1E)) - ((uint16_t)((uint32_t)(0x7190ULL))));
    if ((((uint16_t)((uint32_t)(0xFFFDULL))) & ((uint16_t)(result))) != 0) goto loc_00B7A111;
    if (((uint8_t)(*(uint8_t *)(local_rsp - 0x68 - 0x18))) > 2) goto loc_00B7A111;
    v_stack_m140 = 1;
    v_stack_m126 = 1;
    v_stack_m148 = 87;
    result = HalGetBusDataByOffset(4, 0, (uint32_t)((uint32_t)(local_rbx)), v_stack_m127);
    result = ((((uint8_t)(v_stack_m127)) & (24)) != 0) ? 1 : 0;
    Arg1 = (uint8_t)((v_stack_m127) >> (5));
    result = (uint8_t)((result) & (Arg1));
    if (((1) & ((uint8_t)(result))) != 0) {
        *(uint8_t *)(v_rip + 0x44799F) = 1;
    }
    result = HalpGetChipHacks((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x20)), *(uint16_t *)(local_rsp - 0x68 - 0x1E), *(uint8_t *)(local_rsp - 0x68 - 0x18), v_stack_m124);
    if (sign_flag) goto loc_00B7A149;
    if (((v_stack_m124) & (2)) != 0) {
        result = 1;
        *(uint8_t *)(v_rip + 0x447DA0) = (uint8_t)(result);
    }
    if (((v_stack_m124) & (8)) != 0) {
        Arg2 = (uint32_t)(local_rbx);
        Arg1 = 0;
        result = HalpWhackICHUsbSmi(Arg1, Arg2, *(uint8_t *)(local_rsp - 0x68 - 0x18), v_stack_m124);
    }
    if (((uint8_t)(local_r15)) != 2) goto loc_00B7A203;
    if (0 != 0) goto loc_00B7A203;
    if ((*(uint16_t *)(local_rsp - 0x68 - 0x20)) != ((uint16_t)((uint32_t)(0x8086ULL)))) goto loc_00B7A21C;
    if (0 != 0) goto loc_00B7A20E;
    if (0 != 17) goto loc_00B7A19E;
    if (0 != 0) goto loc_00B7A18B;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x1E))) == ((uint16_t)((uint32_t)(0x98D0ULL)))) goto loc_00B7A1EB;
loc_00B7A18B:
    if (0 != 1) goto loc_00B7A212;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x1E))) == ((uint16_t)((uint32_t)(0x98D1ULL)))) goto loc_00B7A1EB;
loc_00B7A19E:
    if (0 != 16) goto loc_00B7A212;
    if (0 != 6) goto loc_00B7A1B3;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x1E))) == ((uint16_t)((uint32_t)(0xA0D0ULL)))) goto loc_00B7A1EB;
loc_00B7A1B3:
    if (0 != 7) goto loc_00B7A1C2;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x1E))) == ((uint16_t)((uint32_t)(0xA0D1ULL)))) goto loc_00B7A1EB;
loc_00B7A1C2:
    if (0 != 6) goto loc_00B7A1D8;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x1E))) != ((uint16_t)((uint32_t)(0x43D0ULL)))) goto loc_00B7A212;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x68 - 0x18)) == 0) goto loc_00B7A1EB;
loc_00B7A1D8:
    if (0 != 7) goto loc_00B7A212;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x1E))) != ((uint16_t)((uint32_t)(0x43D1ULL)))) goto loc_00B7A212;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x68 - 0x18)) != 0) goto loc_00B7A22A;
loc_00B7A1EB:
    result = HalpInterruptSetLineSpecificOverride(23, (uint32_t)(0x43D1ULL), *(uint8_t *)(local_rsp - 0x68 - 0x18), v_stack_m124);
    result = HalpInterruptSetLineSpecificOverride(23 - 22 + 21, (uint32_t)(0x43D1ULL), *(uint8_t *)(local_rsp - 0x68 - 0x18), v_stack_m124);
loc_00B7A203:
    if ((*(uint16_t *)(local_rsp - 0x68 - 0x20)) != ((uint16_t)((uint32_t)(0x8086ULL)))) goto loc_00B7A21C;
loc_00B7A20E:
loc_00B7A212:
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x68 - 0x1E))) == ((uint16_t)((uint32_t)(0x7110ULL)))) goto loc_00B7A253;
loc_00B7A21C:
    if (0 != 0) goto loc_00B7A22A;
    goto loc_00B7A228;
loc_00B7A226:
loc_00B7A228:
    if (0 == 0) goto loc_00B7A236;
loc_00B7A22A:
    local_rdi = (uint32_t)((local_rdi) + (1));
    goto loc_00B79FDB;
loc_00B7A236:
loc_00B7A23B:
    local_r14 = (uint32_t)((0) + (1));
    local_rdi = 0;
    goto loc_00B79FD1;
loc_00B7A245:
    local_rsi = (uint32_t)((0) + (1));
    goto loc_00B79FBB;
loc_00B7A253:
    v_stack_m148 = 64;
    *(uint8_t *)(v_rip + 0x415BC4) = 1;
    local_rbx = (uint32_t)((local_rbx) | (96));
    result = HalGetBusData((uint32_t)((uint32_t)(1 + 3)), (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)(local_rbx)), local_rsp - 104 - 32);
    *(uint8_t *)(v_rip + 0x447835) = (uint8_t)(*(uint8_t *)(local_rsp - 0x68 - 0x18));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x447C47));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x447C47)))) & (2)) == 0) {
        Arg3 = v_rip - 11880596;
        Arg4 = 0x67BULL;
        Arg1 = 1 + 91;
        Arg2 = 273;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg1 <= 1) {
        local_rdi = 88;
        v_stack_m140 = (uint32_t)(1 + 3);
        Arg4 = v_rip + 4487157;
        v_stack_m148 = (uint32_t)(local_rdi);
        Arg3 = (uint32_t)(local_rbx);
        *(uint32_t *)(v_rip + 0x4477E4) = (uint32_t)(local_rsi);
        Arg2 = (uint32_t)(local_rsi);
        *(uint32_t *)(v_rip + 0x4477E8) = (uint32_t)(local_rbx);
        Arg1 = (uint32_t)(1 + 3);
        result = HalGetBusDataByOffset(Arg1, Arg2, Arg3, Arg4);
        Arg3 = *(uint32_t *)(v_rip + 0x4477D9);
        Arg4 = v_rip + 4487114;
        Arg2 = *(uint32_t *)(v_rip + 0x4477C0);
        Arg1 = (uint32_t)(1 + 3);
        v_stack_m140 = (uint32_t)(1 + 3);
        v_stack_m148 = (uint32_t)(local_rdi);
        result = HalSetBusDataByOffset(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFF5FULL));
    result = HalpUsbLegacyStopUhciInterrupt(Arg1, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)(local_rbx)), 1);
    goto loc_00B7A333;
loc_00B7A32D:
loc_00B7A333:
    local_rdi = 0;
loc_00B7A335:
    if (Arg1 == 0) goto loc_00B7A424;
    if (v_stack_m120 != 0) {
        result = ZwClose(v_stack_m120, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)(local_rbx)), 1);
        Arg1 = 0;
        v_stack_m120 = Arg1;
    }
    if (v_stack_m126 == 0) goto loc_00B7A3FA;
    v_stack_mF8 = v_stack_m110;
    v_stack_m100 = 48;
    v_stack_mF0 = local_rsp - 104 - 72;
    *(uint32_t *)(local_rsp - 0x68 - 0x80) = 64;
    v_stack_m138 = v_stack_m118;
    Arg4 = 0;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    *(uint64_t *)(local_rsp - 0x68 - 0x78) = v_xmm0;
    result = ZwCreateKey(v_stack_m120, (uint32_t)(0x20019ULL), v_stack_m100, Arg4);
    if (sign_flag) goto loc_00B7A3F5;
    v_stack_m140 = v_stack_m108;
    v_stack_m148 = 20;
    result = ZwQueryValueKey(v_stack_m120, local_rsp - 104 - 56, 2, local_rsp - 104 + 32);
    if (sign_flag) goto loc_00B7A3F5;
    if ((*(uint32_t *)(local_rsp - 0x68 + 0x28)) >= 1) {
        result = *(uint8_t *)(local_rsp - 0x68 + 0x2C);
        *(uint8_t *)(v_rip + 0x4476BB) = (uint8_t)(result);
    }
loc_00B7A3FA:
    if (v_stack_m120 != 0) {
        result = ZwClose(v_stack_m120, local_rsp - 104 - 56, 2, local_rsp - 104 + 32);
    }
    if (v_stack_m110 != 0) {
        result = ZwClose(v_stack_m110, local_rsp - 104 - 56, 2, local_rsp - 104 + 32);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 4282915, Arg2, Arg3, local_rsp - 104 + 32);
loc_00B7A424:
    Arg1 = (*(uint64_t *)(local_rsp - 0x68 + 0x38)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, local_rsp - 104 + 32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B79E00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
