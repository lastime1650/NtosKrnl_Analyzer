# PiDevCfgFindDeviceDriver

- RVA: `0x0097602C`–`0x00976D2E` (길이 `3,330` bytes)
- VA: `0x000000014097602C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000966BC`
- 디코드: `845`개 명령, `3,330/3,330` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x009760C3` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x009760CF` → [PiDevCfgClearDeviceDrivers](../70/PiDevCfgClearDeviceDrivers_function_00704A60.md) (function, `0x00704A60`)
- `0x0097611C` → [PiDevCfgQueryDriverPolicy](../73/PiDevCfgQueryDriverPolicy_function_00734CA4.md) (function, `0x00734CA4`)
- `0x00976137` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009761D3` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x0097620B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0097621E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00976279` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x009762AE` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x009762CE` → [DrvDbSplitDeviceIdDriverInfMatch](../A6/DrvDbSplitDeviceIdDriverInfMatch_function_00A62808.md) (function, `0x00A62808`)
- `0x00976405` → [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) (function, `0x0073435C`)
- `0x0097644C` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (function, `0x004C2740`)
- `0x0097652C` → [PiDevCfgMatchDriverConfigurationId](../../text/5A/PiDevCfgMatchDriverConfigurationId_function_005A7DD8.md) (function, `0x005A7DD8`)
- `0x0097655D` → [PiDevCfgMatchDriverConfigurationId](../../text/5A/PiDevCfgMatchDriverConfigurationId_function_005A7DD8.md) (function, `0x005A7DD8`)
- `0x009765E4` → [PiDevCfgCompareDrivers](../../text/4B/PiDevCfgCompareDrivers_function_004B9DD8.md) (function, `0x004B9DD8`)
- `0x009766EA` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x00976711` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x0097674A` → [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) (function, `0x0073435C`)
- `0x009767BF` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x00976879` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x009768DC` → [PiDevCfgCompareDrivers](../../text/4B/PiDevCfgCompareDrivers_function_004B9DD8.md) (function, `0x004B9DD8`)
- `0x0097693F` → [PnpIsNullGuid](../8D/PnpIsNullGuid_function_008DD9E0.md) (function, `0x008DD9E0`)
- `0x009769C9` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x00976A4D` → [PiDevCfgMatchDriverConfigurationId](../../text/5A/PiDevCfgMatchDriverConfigurationId_function_005A7DD8.md) (function, `0x005A7DD8`)
- `0x00976A86` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x00976AB2` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x00976AC7` → [PiDevCfgFreeDriverNode](../73/PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x00976B5F` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x00976B6E` → [PiDevCfgFreeDriverNode](../73/PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x00976B8F` → [PiDevCfgCompareDrivers](../../text/4B/PiDevCfgCompareDrivers_function_004B9DD8.md) (function, `0x004B9DD8`)
- `0x00976BFA` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (function, `0x004F7944`)
- `0x00976C08` → [PiDevCfgFreeDriverNode](../73/PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x00976C16` → [PnpIsNullGuid](../8D/PnpIsNullGuid_function_008DD9E0.md) (function, `0x008DD9E0`)
- `0x00976CA2` → [PiDevCfgFreeDriverNode](../73/PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x00976CDA` → [PiDevCfgFreeDriverNode](../73/PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x00976CF0` → [PiDevCfgFreeDriverNode](../73/PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)
- `0x00976CFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00976D0D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiDevCfgCheckDeviceNeedsUpdate](../73/PiDevCfgCheckDeviceNeedsUpdate_function_00731DDC.md) at `0x00731E78`
- [PpDevCfgProcessDeviceExtensions](../73/PpDevCfgProcessDeviceExtensions_function_00736C2C.md) at `0x00736DAC`
- [PiDevCfgProcessDevice](PiDevCfgProcessDevice_function_00976D34.md) at `0x00976E37`

### Static image references
- `0x00976048` → RVA `0x00E0A740` (`.data`; read)
- `0x00976103` → RVA `0x00E66245` (`.data`; read)
- `0x0097615F` → RVA `0x00011EF8` (`.rdata`; read)
- `0x0097618C` → RVA `0x00E66398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x009760C3` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x00976137` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0097620B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0097621E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009762AE` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x0097644C` → [PnpMultiSzContainsString](../../text/4C/PnpMultiSzContainsString_function_004C2740.md) (`PAGE` → `.text`)
  - `0x0097652C` → [PiDevCfgMatchDriverConfigurationId](../../text/5A/PiDevCfgMatchDriverConfigurationId_function_005A7DD8.md) (`PAGE` → `.text`)
  - `0x0097655D` → [PiDevCfgMatchDriverConfigurationId](../../text/5A/PiDevCfgMatchDriverConfigurationId_function_005A7DD8.md) (`PAGE` → `.text`)
  - `0x009765E4` → [PiDevCfgCompareDrivers](../../text/4B/PiDevCfgCompareDrivers_function_004B9DD8.md) (`PAGE` → `.text`)
  - `0x009766EA` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x00976711` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x009767BF` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x00976879` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x009768DC` → [PiDevCfgCompareDrivers](../../text/4B/PiDevCfgCompareDrivers_function_004B9DD8.md) (`PAGE` → `.text`)
  - `0x009769C9` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x00976A4D` → [PiDevCfgMatchDriverConfigurationId](../../text/5A/PiDevCfgMatchDriverConfigurationId_function_005A7DD8.md) (`PAGE` → `.text`)
  - `0x00976A86` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x00976AB2` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x00976B5F` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x00976B8F` → [PiDevCfgCompareDrivers](../../text/4B/PiDevCfgCompareDrivers_function_004B9DD8.md) (`PAGE` → `.text`)
  - `0x00976BFA` → [Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline_function_004F7944.md) (`PAGE` → `.text`)
  - `0x00976CFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00976D0D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0097602C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00976031  55                              push rbp
00976032  56                              push rsi
00976033  57                              push rdi
00976034  41 54                           push r12
00976036  41 55                           push r13
00976038  41 56                           push r14
0097603A  41 57                           push r15
0097603C  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
00976041  48 81 EC 20 01 00 00            sub rsp, 0x120
00976048  48 8B 05 F1 46 49 00            mov rax, qword ptr [rip + 0x4946f1]
0097604F  48 33 C4                        xor rax, rsp
00976052  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00976056  45 33 E4                        xor r12d, r12d
00976059  4C 89 45 F0                     mov qword ptr [rbp - 0x10], r8
0097605D  33 C0                           xor eax, eax
0097605F  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
00976063  89 45 08                        mov dword ptr [rbp + 8], eax
00976066  0F 57 C0                        xorps xmm0, xmm0
00976069  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0097606E  44 89 64 24 68                  mov dword ptr [rsp + 0x68], r12d
00976073  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00976078  45 8D 6C 24 01                  lea r13d, [r12 + 1]
0097607D  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00976082  4C 89 65 C8                     mov qword ptr [rbp - 0x38], r12
00976086  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0097608B  48 8B DA                        mov rbx, rdx
0097608E  48 8D 45 A8                     lea rax, [rbp - 0x58]
00976092  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
00976096  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0097609A  4C 8B F9                        mov r15, rcx
0097609D  48 8D 45 A8                     lea rax, [rbp - 0x58]
009760A1  44 89 65 94                     mov dword ptr [rbp - 0x6c], r12d
009760A5  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
009760A9  41 8B F4                        mov esi, r12d
009760AC  41 8B FC                        mov edi, r12d
009760AF  44 89 6D 98                     mov dword ptr [rbp - 0x68], r13d
009760B3  44 89 65 90                     mov dword ptr [rbp - 0x70], r12d
009760B7  45 8B F4                        mov r14d, r12d
009760BA  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
009760BF  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
009760C3  E8 7C 18 B8 FF                  call 0x1404f7944
009760C8  85 C0                           test eax, eax
009760CA  74 08                           je 0x1409760d4
009760CC  49 8B CF                        mov rcx, r15
009760CF  E8 8C E9 D8 FF                  call 0x140704a60
009760D4  48 85 DB                        test rbx, rbx
009760D7  74 2A                           je 0x140976103
009760D9  48 89 5D C8                     mov qword ptr [rbp - 0x38], rbx
009760DD  48 83 C8 FF                     or rax, 0xffffffffffffffff
009760E1  48 FF C0                        inc rax
009760E4  66 44 39 24 43                  cmp word ptr [rbx + rax*2], r12w
009760E9  75 F6                           jne 0x1409760e1
009760EB  48 8D 4B 02                     lea rcx, [rbx + 2]
009760EF  48 8D 0C 41                     lea rcx, [rcx + rax*2]
009760F3  0F B7 01                        movzx eax, word ptr [rcx]
009760F6  66 F7 D8                        neg ax
009760F9  48 1B C0                        sbb rax, rax
009760FC  48 23 C1                        and rax, rcx
009760FF  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00976103  44 38 25 3B 01 4F 00            cmp byte ptr [rip + 0x4f013b], r12b
0097610A  41 8B C5                        mov eax, r13d
0097610D  B9 03 00 00 00                  mov ecx, 3
00976112  0F 45 C1                        cmovne eax, ecx
00976115  48 8D 4D F8                     lea rcx, [rbp - 8]
00976119  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0097611C  E8 83 EB DB FF                  call 0x140734ca4
00976121  BB 08 02 00 00                  mov ebx, 0x208
00976126  41 B8 50 70 64 63               mov r8d, 0x63647050
0097612C  8B D3                           mov edx, ebx
0097612E  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
00976132  B9 00 01 00 00                  mov ecx, 0x100
00976137  E8 B4 BF 20 00                  call 0x140b820f0
0097613C  45 33 DB                        xor r11d, r11d
0097613F  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00976143  4C 8B E0                        mov r12, rax
00976146  48 85 C0                        test rax, rax
00976149  75 0A                           jne 0x140976155
0097614B  BE 9A 00 00 C0                  mov esi, 0xc000009a
00976150  E9 17 0B 00 00                  jmp 0x140976c6c
00976155  41 8B C3                        mov eax, r11d
00976158  49 8D 4F 30                     lea rcx, [r15 + 0x30]
0097615C  89 45 9C                        mov dword ptr [rbp - 0x64], eax
0097615F  48 8D 15 92 BD 69 FF            lea rdx, [rip - 0x96426e]
00976166  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
0097616A  4C 8B 29                        mov r13, qword ptr [rcx]
0097616D  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
00976171  4D 85 ED                        test r13, r13
00976174  0F 84 29 05 00 00               je 0x1409766a3
0097617A  45 8B FB                        mov r15d, r11d
0097617D  44 89 5D 80                     mov dword ptr [rbp - 0x80], r11d
00976181  66 45 39 5D 00                  cmp word ptr [r13], r11w
00976186  0F 84 0F 05 00 00               je 0x14097669b
0097618C  48 8B 0D 05 02 4F 00            mov rcx, qword ptr [rip + 0x4f0205]
00976193  48 8D 45 90                     lea rax, [rbp - 0x70]
00976197  44 89 5C 24 50                  mov dword ptr [rsp + 0x50], r11d
0097619C  49 83 C9 FF                     or r9, 0xffffffffffffffff
009761A0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009761A5  48 8D 45 98                     lea rax, [rbp - 0x68]
009761A9  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009761AD  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
009761B2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009761B7  45 8D 41 0C                     lea r8d, [r9 + 0xc]
009761BB  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
009761C0  49 8B D5                        mov rdx, r13
009761C3  C7 45 98 01 00 00 00            mov dword ptr [rbp - 0x68], 1
009761CA  44 89 5D 90                     mov dword ptr [rbp - 0x70], r11d
009761CE  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
009761D3  E8 A8 BF F6 FF                  call 0x1408e2180
009761D8  45 33 DB                        xor r11d, r11d
009761DB  8B F0                           mov esi, eax
009761DD  85 C0                           test eax, eax
009761DF  0F 89 39 01 00 00               jns 0x14097631e
009761E5  81 FE 23 00 00 C0               cmp esi, 0xc0000023
009761EB  0F 85 2D 01 00 00               jne 0x14097631e
009761F1  39 5D 90                        cmp dword ptr [rbp - 0x70], ebx
009761F4  0F 86 98 01 00 00               jbe 0x140976392
009761FA  8B 5D 90                        mov ebx, dword ptr [rbp - 0x70]
009761FD  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
00976201  4D 85 E4                        test r12, r12
00976204  74 0A                           je 0x140976210
00976206  33 D2                           xor edx, edx
00976208  49 8B CC                        mov rcx, r12
0097620B  E8 60 C6 20 00                  call 0x140b82870
00976210  48 8B D3                        mov rdx, rbx
00976213  B9 00 01 00 00                  mov ecx, 0x100
00976218  41 B8 50 70 64 63               mov r8d, 0x63647050
0097621E  E8 CD BE 20 00                  call 0x140b820f0
00976223  45 33 DB                        xor r11d, r11d
00976226  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0097622A  4C 8B E0                        mov r12, rax
0097622D  48 85 C0                        test rax, rax
00976230  0F 84 15 FF FF FF               je 0x14097614b
00976236  48 8B 0D 5B 01 4F 00            mov rcx, qword ptr [rip + 0x4f015b]
0097623D  48 8D 45 90                     lea rax, [rbp - 0x70]
00976241  44 89 5C 24 50                  mov dword ptr [rsp + 0x50], r11d
00976246  45 8D 43 0B                     lea r8d, [r11 + 0xb]
0097624A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0097624F  49 83 C9 FF                     or r9, 0xffffffffffffffff
00976253  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00976257  48 8D 45 98                     lea rax, [rbp - 0x68]
0097625B  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00976260  49 8B D5                        mov rdx, r13
00976263  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00976268  48 8D 05 89 BC 69 FF            lea rax, [rip - 0x964377]
0097626F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00976274  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00976279  E8 02 BF F6 FF                  call 0x1408e2180
0097627E  45 33 DB                        xor r11d, r11d
00976281  8B F0                           mov esi, eax
00976283  85 C0                           test eax, eax
00976285  0F 88 5A FF FF FF               js 0x1409761e5
0097628B  81 7D 98 12 20 00 00            cmp dword ptr [rbp - 0x68], 0x2012
00976292  0F 85 B6 03 00 00               jne 0x14097664e
00976298  4D 8B FC                        mov r15, r12
0097629B  66 45 39 1C 24                  cmp word ptr [r12], r11w
009762A0  0F 84 A4 03 00 00               je 0x14097664a
009762A6  BA 5C 00 00 00                  mov edx, 0x5c
009762AB  49 8B CF                        mov rcx, r15
009762AE  E8 AD B7 B8 FF                  call 0x140501a60
009762B3  45 33 DB                        xor r11d, r11d
009762B6  48 8B D8                        mov rbx, rax
009762B9  48 85 C0                        test rax, rax
009762BC  0F 84 5E 03 00 00               je 0x140976620
009762C2  4C 8D 4D 94                     lea r9, [rbp - 0x6c]
009762C6  45 33 C0                        xor r8d, r8d
009762C9  33 D2                           xor edx, edx
009762CB  49 8B CF                        mov rcx, r15
009762CE  E8 35 C5 0E 00                  call 0x140a62808
009762D3  45 33 DB                        xor r11d, r11d
009762D6  8B F0                           mov esi, eax
009762D8  85 C0                           test eax, eax
009762DA  0F 88 66 03 00 00               js 0x140976646
009762E0  44 8B 45 9C                     mov r8d, dword ptr [rbp - 0x64]
009762E4  4D 8B D7                        mov r10, r15
009762E7  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
009762EA  4C 8D 7B 02                     lea r15, [rbx + 2]
009762EE  66 44 89 1B                     mov word ptr [rbx], r11w
009762F2  8B D0                           mov edx, eax
009762F4  8B 5D 94                        mov ebx, dword ptr [rbp - 0x6c]
009762F7  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
009762FB  41 83 F8 02                     cmp r8d, 2
009762FF  75 0C                           jne 0x14097630d
00976301  80 FB 03                        cmp bl, 3
00976304  0F 85 16 03 00 00               jne 0x140976620
0097630A  83 CA 08                        or edx, 8
0097630D  80 FB 01                        cmp bl, 1
00976310  0F 85 84 00 00 00               jne 0x14097639a
00976316  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
00976319  E9 A5 00 00 00                  jmp 0x1409763c3
0097631E  49 8B CC                        mov rcx, r12
00976321  8B C6                           mov eax, esi
00976323  81 FE 9A 00 00 C0               cmp esi, 0xc000009a
00976329  0F 84 5E 03 00 00               je 0x14097668d
0097632F  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00976333  44 8B C3                        mov r8d, ebx
00976336  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
0097633A  85 C0                           test eax, eax
0097633C  0F 89 49 FF FF FF               jns 0x14097628b
00976342  3D 22 00 00 C0                  cmp eax, 0xc0000022
00976347  74 24                           je 0x14097636d
00976349  3D 67 04 00 C0                  cmp eax, 0xc0000467
0097634E  74 1D                           je 0x14097636d
00976350  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
00976354  41 B8 34 00 00 C0               mov r8d, 0xc0000034
0097635A  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
0097635E  41 3B C0                        cmp eax, r8d
00976361  75 2F                           jne 0x140976392
00976363  41 8B F8                        mov edi, r8d
00976366  44 89 44 24 68                  mov dword ptr [rsp + 0x68], r8d
0097636B  EB 1A                           jmp 0x140976387
0097636D  85 FF                           test edi, edi
0097636F  74 10                           je 0x140976381
00976371  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
00976375  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00976379  81 FF 34 00 00 C0               cmp edi, 0xc0000034
0097637F  74 11                           je 0x140976392
00976381  8B F8                           mov edi, eax
00976383  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00976387  44 8B C3                        mov r8d, ebx
0097638A  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
0097638E  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
00976392  41 8B F3                        mov esi, r11d
00976395  E9 B4 02 00 00                  jmp 0x14097664e
0097639A  80 FB 02                        cmp bl, 2
0097639D  75 11                           jne 0x1409763b0
0097639F  0F B7 45 96                     movzx eax, word ptr [rbp - 0x6a]
009763A3  B9 00 10 00 00                  mov ecx, 0x1000
009763A8  C1 E0 08                        shl eax, 8
009763AB  03 45 80                        add eax, dword ptr [rbp - 0x80]
009763AE  EB 16                           jmp 0x1409763c6
009763B0  80 FB 03                        cmp bl, 3
009763B3  0F 85 67 02 00 00               jne 0x140976620
009763B9  0F B7 45 96                     movzx eax, word ptr [rbp - 0x6a]
009763BD  C1 E0 08                        shl eax, 8
009763C0  03 45 80                        add eax, dword ptr [rbp - 0x80]
009763C3  41 8B CB                        mov ecx, r11d
009763C6  3D 00 10 00 00                  cmp eax, 0x1000
009763CB  41 B9 FF 0F 00 00               mov r9d, 0xfff
009763D1  41 0F 43 C1                     cmovae eax, r9d
009763D5  44 0F B6 4D 95                  movzx r9d, byte ptr [rbp - 0x6b]
009763DA  41 C1 E0 0D                     shl r8d, 0xd
009763DE  44 03 C1                        add r8d, ecx
009763E1  41 C1 E1 10                     shl r9d, 0x10
009763E5  44 03 C0                        add r8d, eax
009763E8  49 8B CA                        mov rcx, r10
009763EB  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009763F0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009763F5  48 8D 45 F8                     lea rax, [rbp - 8]
009763F9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009763FE  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00976402  49 8B D5                        mov rdx, r13
00976405  E8 52 DF DB FF                  call 0x14073435c
0097640A  45 33 DB                        xor r11d, r11d
0097640D  8B F0                           mov esi, eax
0097640F  85 C0                           test eax, eax
00976411  79 08                           jns 0x14097641b
00976413  41 8B F3                        mov esi, r11d
00976416  E9 05 02 00 00                  jmp 0x140976620
0097641B  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00976420  4C 8B BF A8 00 00 00            mov r15, qword ptr [rdi + 0xa8]
00976427  4D 85 FF                        test r15, r15
0097642A  0F 84 87 00 00 00               je 0x1409764b7
00976430  66 45 39 1F                     cmp word ptr [r15], r11w
00976434  74 6C                           je 0x1409764a2
00976436  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
0097643A  45 8B E3                        mov r12d, r11d
0097643D  49 8D 7D 30                     lea rdi, [r13 + 0x30]
00976441  48 8B 0F                        mov rcx, qword ptr [rdi]
00976444  48 85 C9                        test rcx, rcx
00976447  74 10                           je 0x140976459
00976449  49 8B D7                        mov rdx, r15
0097644C  E8 EF C2 B4 FF                  call 0x1404c2740
00976451  45 33 DB                        xor r11d, r11d
00976454  48 85 C0                        test rax, rax
00976457  75 0F                           jne 0x140976468
00976459  41 FF C4                        inc r12d
0097645C  48 83 C7 10                     add rdi, 0x10
00976460  41 83 FC 03                     cmp r12d, 3
00976464  72 DB                           jb 0x140976441
00976466  EB 0C                           jmp 0x140976474
00976468  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0097646D  4C 89 B8 B0 00 00 00            mov qword ptr [rax + 0xb0], r15
00976474  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00976479  4C 39 9F B0 00 00 00            cmp qword ptr [rdi + 0xb0], r11
00976480  75 1C                           jne 0x14097649e
00976482  48 83 C8 FF                     or rax, 0xffffffffffffffff
00976486  48 FF C0                        inc rax
00976489  66 45 39 1C 47                  cmp word ptr [r15 + rax*2], r11w
0097648E  75 F6                           jne 0x140976486
00976490  4D 8D 3C 47                     lea r15, [r15 + rax*2]
00976494  49 83 C7 02                     add r15, 2
00976498  66 45 39 1F                     cmp word ptr [r15], r11w
0097649C  75 9C                           jne 0x14097643a
0097649E  4C 8B 6D E0                     mov r13, qword ptr [rbp - 0x20]
009764A2  4C 39 9F B0 00 00 00            cmp qword ptr [rdi + 0xb0], r11
009764A9  74 0C                           je 0x1409764b7
009764AB  81 4F 6C FF FF 00 00            or dword ptr [rdi + 0x6c], 0xffff
009764B2  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
009764B7  80 FB 03                        cmp bl, 3
009764BA  75 28                           jne 0x1409764e4
009764BC  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
009764C0  48 8D 4D A8                     lea rcx, [rbp - 0x58]
009764C4  48 39 08                        cmp qword ptr [rax], rcx
009764C7  0F 85 14 08 00 00               jne 0x140976ce1
009764CD  48 89 47 08                     mov qword ptr [rdi + 8], rax
009764D1  48 8D 4D A8                     lea rcx, [rbp - 0x58]
009764D5  48 89 0F                        mov qword ptr [rdi], rcx
009764D8  48 89 38                        mov qword ptr [rax], rdi
009764DB  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
009764DF  E9 38 01 00 00                  jmp 0x14097661c
009764E4  F7 87 B8 00 00 00 00 02 00 00   test dword ptr [rdi + 0xb8], 0x200
009764EE  74 5E                           je 0x14097654e
009764F0  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
009764F5  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
009764FA  48 39 08                        cmp qword ptr [rax], rcx
009764FD  0F 85 DE 07 00 00               jne 0x140976ce1
00976503  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00976508  48 89 47 08                     mov qword ptr [rdi + 8], rax
0097650C  48 89 0F                        mov qword ptr [rdi], rcx
0097650F  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00976513  48 89 38                        mov qword ptr [rax], rdi
00976516  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0097651B  48 85 C9                        test rcx, rcx
0097651E  0F 84 F8 00 00 00               je 0x14097661c
00976524  48 8B D1                        mov rdx, rcx
00976527  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0097652C  E8 A7 18 C3 FF                  call 0x1405a7dd8
00976531  4C 8B 7D A0                     mov r15, qword ptr [rbp - 0x60]
00976535  45 33 DB                        xor r11d, r11d
00976538  84 C0                           test al, al
0097653A  0F 84 E0 00 00 00               je 0x140976620
00976540  BF 6B 03 00 C0                  mov edi, 0xc000036b
00976545  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
00976549  E9 D6 00 00 00                  jmp 0x140976624
0097654E  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00976552  48 85 C9                        test rcx, rcx
00976555  74 48                           je 0x14097659f
00976557  48 8B D1                        mov rdx, rcx
0097655A  48 8B CF                        mov rcx, rdi
0097655D  E8 76 18 C3 FF                  call 0x1405a7dd8
00976562  45 33 DB                        xor r11d, r11d
00976565  84 C0                           test al, al
00976567  75 31                           jne 0x14097659a
00976569  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0097656E  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00976573  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00976578  48 39 11                        cmp qword ptr [rcx], rdx
0097657B  0F 85 60 07 00 00               jne 0x140976ce1
00976581  48 89 48 08                     mov qword ptr [rax + 8], rcx
00976585  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
0097658A  48 89 10                        mov qword ptr [rax], rdx
0097658D  48 89 01                        mov qword ptr [rcx], rax
00976590  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00976595  E9 82 00 00 00                  jmp 0x14097661c
0097659A  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
0097659F  4C 39 9F B0 00 00 00            cmp qword ptr [rdi + 0xb0], r11
009765A6  74 29                           je 0x1409765d1
009765A8  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
009765AD  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
009765B2  48 39 08                        cmp qword ptr [rax], rcx
009765B5  0F 85 26 07 00 00               jne 0x140976ce1
009765BB  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
009765C0  48 89 0F                        mov qword ptr [rdi], rcx
009765C3  48 89 47 08                     mov qword ptr [rdi + 8], rax
009765C7  48 89 38                        mov qword ptr [rax], rdi
009765CA  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
009765CF  EB 4B                           jmp 0x14097661c
009765D1  4D 85 F6                        test r14, r14
009765D4  75 05                           jne 0x1409765db
009765D6  4C 8B F7                        mov r14, rdi
009765D9  EB 41                           jmp 0x14097661c
009765DB  45 33 C0                        xor r8d, r8d
009765DE  49 8B D6                        mov rdx, r14
009765E1  48 8B CF                        mov rcx, rdi
009765E4  E8 EF 37 B4 FF                  call 0x1404b9dd8
009765E9  45 33 DB                        xor r11d, r11d
009765EC  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
009765F1  85 C0                           test eax, eax
009765F3  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
009765F8  79 B8                           jns 0x1409765b2
009765FA  48 39 08                        cmp qword ptr [rax], rcx
009765FD  0F 85 DE 06 00 00               jne 0x140976ce1
00976603  49 89 46 08                     mov qword ptr [r14 + 8], rax
00976607  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0097660C  49 89 0E                        mov qword ptr [r14], rcx
0097660F  4C 89 30                        mov qword ptr [rax], r14
00976612  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
00976617  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
0097661C  4C 8B 7D A0                     mov r15, qword ptr [rbp - 0x60]
00976620  8B 7C 24 68                     mov edi, dword ptr [rsp + 0x68]
00976624  48 83 C8 FF                     or rax, 0xffffffffffffffff
00976628  48 FF C0                        inc rax
0097662B  66 45 39 1C 47                  cmp word ptr [r15 + rax*2], r11w
00976630  75 F6                           jne 0x140976628
00976632  4D 8D 3C 47                     lea r15, [r15 + rax*2]
00976636  49 83 C7 02                     add r15, 2
0097663A  66 45 39 1F                     cmp word ptr [r15], r11w
0097663E  0F 85 62 FC FF FF               jne 0x1409762a6
00976644  EB 04                           jmp 0x14097664a
00976646  8B 7C 24 68                     mov edi, dword ptr [rsp + 0x68]
0097664A  44 8B 7D 80                     mov r15d, dword ptr [rbp - 0x80]
0097664E  48 83 C8 FF                     or rax, 0xffffffffffffffff
00976652  48 FF C0                        inc rax
00976655  66 45 39 5C 45 00               cmp word ptr [r13 + rax*2], r11w
0097665B  75 F5                           jne 0x140976652
0097665D  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
00976661  4D 8D 6C 45 00                  lea r13, [r13 + rax*2]
00976666  4C 8B 65 C0                     mov r12, qword ptr [rbp - 0x40]
0097666A  48 8D 15 87 B8 69 FF            lea rdx, [rip - 0x964779]
00976671  49 83 C5 02                     add r13, 2
00976675  41 FF C7                        inc r15d
00976678  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
0097667C  44 89 7D 80                     mov dword ptr [rbp - 0x80], r15d
00976680  66 45 39 5D 00                  cmp word ptr [r13], r11w
00976685  0F 85 01 FB FF FF               jne 0x14097618c
0097668B  EB 07                           jmp 0x140976694
0097668D  48 8D 15 64 B8 69 FF            lea rdx, [rip - 0x96479c]
00976694  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00976698  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
0097669B  85 F6                           test esi, esi
0097669D  0F 88 C9 05 00 00               js 0x140976c6c
009766A3  FF C0                           inc eax
009766A5  48 83 C1 10                     add rcx, 0x10
009766A9  89 45 9C                        mov dword ptr [rbp - 0x64], eax
009766AC  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
009766B0  83 F8 03                        cmp eax, 3
009766B3  0F 82 B1 FA FF FF               jb 0x14097616a
009766B9  85 F6                           test esi, esi
009766BB  0F 88 AB 05 00 00               js 0x140976c6c
009766C1  4C 8B 6D C8                     mov r13, qword ptr [rbp - 0x38]
009766C5  4D 85 ED                        test r13, r13
009766C8  0F 84 D5 00 00 00               je 0x1409767a3
009766CE  4D 85 F6                        test r14, r14
009766D1  0F 85 5C 01 00 00               jne 0x140976833
009766D7  81 FF 6B 03 00 C0               cmp edi, 0xc000036b
009766DD  0F 84 C9 00 00 00               je 0x1409767ac
009766E3  41 8D 56 3A                     lea edx, [r14 + 0x3a]
009766E7  49 8B CD                        mov rcx, r13
009766EA  E8 71 B3 B8 FF                  call 0x140501a60
009766EF  45 33 DB                        xor r11d, r11d
009766F2  48 8B D8                        mov rbx, rax
009766F5  48 85 C0                        test rax, rax
009766F8  75 0A                           jne 0x140976704
009766FA  BE 33 00 00 C0                  mov esi, 0xc0000033
009766FF  E9 68 05 00 00                  jmp 0x140976c6c
00976704  BA 2C 00 00 00                  mov edx, 0x2c
00976709  66 44 89 18                     mov word ptr [rax], r11w
0097670D  48 8D 48 02                     lea rcx, [rax + 2]
00976711  E8 4A B3 B8 FF                  call 0x140501a60
00976716  45 33 DB                        xor r11d, r11d
00976719  48 85 C0                        test rax, rax
0097671C  74 DC                           je 0x1409766fa
0097671E  66 44 89 18                     mov word ptr [rax], r11w
00976722  48 8D 53 02                     lea rdx, [rbx + 2]
00976726  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0097672B  45 33 C9                        xor r9d, r9d
0097672E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00976733  45 33 C0                        xor r8d, r8d
00976736  48 8D 45 F8                     lea rax, [rbp - 8]
0097673A  49 8B CD                        mov rcx, r13
0097673D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00976742  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
0097674A  E8 0D DC DB FF                  call 0x14073435c
0097674F  45 33 DB                        xor r11d, r11d
00976752  85 C0                           test eax, eax
00976754  78 56                           js 0x1409767ac
00976756  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0097675B  F7 81 B8 00 00 00 00 02 00 00   test dword ptr [rcx + 0xb8], 0x200
00976765  74 34                           je 0x14097679b
00976767  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0097676C  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00976771  48 39 10                        cmp qword ptr [rax], rdx
00976774  0F 85 67 05 00 00               jne 0x140976ce1
0097677A  48 89 41 08                     mov qword ptr [rcx + 8], rax
0097677E  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00976783  48 89 11                        mov qword ptr [rcx], rdx
00976786  BF 6B 03 00 C0                  mov edi, 0xc000036b
0097678B  48 89 08                        mov qword ptr [rax], rcx
0097678E  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00976793  41 8B CB                        mov ecx, r11d
00976796  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0097679B  48 85 C9                        test rcx, rcx
0097679E  74 0C                           je 0x1409767ac
009767A0  4C 8B F1                        mov r14, rcx
009767A3  4D 85 F6                        test r14, r14
009767A6  0F 85 87 00 00 00               jne 0x140976833
009767AC  85 FF                           test edi, edi
009767AE  74 0A                           je 0x1409767ba
009767B0  8B F7                           mov esi, edi
009767B2  81 FF 34 00 00 C0               cmp edi, 0xc0000034
009767B8  75 05                           jne 0x1409767bf
009767BA  BE 90 04 00 C0                  mov esi, 0xc0000490
009767BF  E8 80 11 B8 FF                  call 0x1404f7944
009767C4  85 C0                           test eax, eax
009767C6  0F 84 A0 04 00 00               je 0x140976c6c
009767CC  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
009767D0  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
009767D5  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009767DA  48 3B C8                        cmp rcx, rax
009767DD  0F 84 89 04 00 00               je 0x140976c6c
009767E3  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009767E8  48 39 41 08                     cmp qword ptr [rcx + 8], rax
009767EC  0F 85 EF 04 00 00               jne 0x140976ce1
009767F2  48 8B 01                        mov rax, qword ptr [rcx]
009767F5  48 39 48 08                     cmp qword ptr [rax + 8], rcx
009767F9  0F 85 E2 04 00 00               jne 0x140976ce1
009767FF  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00976804  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00976809  48 89 50 08                     mov qword ptr [rax + 8], rdx
0097680D  49 8D 47 18                     lea rax, [r15 + 0x18]
00976811  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00976815  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0097681A  48 39 02                        cmp qword ptr [rdx], rax
0097681D  0F 85 BE 04 00 00               jne 0x140976ce1
00976823  48 89 01                        mov qword ptr [rcx], rax
00976826  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0097682A  48 89 0A                        mov qword ptr [rdx], rcx
0097682D  48 89 48 08                     mov qword ptr [rax + 8], rcx
00976831  EB 9D                           jmp 0x1409767d0
00976833  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
00976837  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0097683C  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00976841  48 3B C1                        cmp rax, rcx
00976844  0F 84 B1 00 00 00               je 0x1409768fb
0097684A  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0097684F  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00976853  0F 85 88 04 00 00               jne 0x140976ce1
00976859  48 8B 08                        mov rcx, qword ptr [rax]
0097685C  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00976860  0F 85 7B 04 00 00               jne 0x140976ce1
00976866  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
0097686B  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00976870  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00976874  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00976879  E8 C6 10 B8 FF                  call 0x1404f7944
0097687E  45 33 DB                        xor r11d, r11d
00976881  49 8D 8E E0 00 00 00            lea rcx, [r14 + 0xe0]
00976888  85 C0                           test eax, eax
0097688A  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0097688F  74 04                           je 0x140976895
00976891  49 8D 4F 18                     lea rcx, [r15 + 0x18]
00976895  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00976899  48 39 0A                        cmp qword ptr [rdx], rcx
0097689C  0F 85 3F 04 00 00               jne 0x140976ce1
009768A2  48 89 08                        mov qword ptr [rax], rcx
009768A5  48 89 50 08                     mov qword ptr [rax + 8], rdx
009768A9  48 89 02                        mov qword ptr [rdx], rax
009768AC  48 89 41 08                     mov qword ptr [rcx + 8], rax
009768B0  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009768B5  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
009768BB  A8 04                           test al, 4
009768BD  0F 84 74 FF FF FF               je 0x140976837
009768C3  41 8B 9E B8 00 00 00            mov ebx, dword ptr [r14 + 0xb8]
009768CA  F6 C3 08                        test bl, 8
009768CD  0F 85 64 FF FF FF               jne 0x140976837
009768D3  41 B8 04 00 00 00               mov r8d, 4
009768D9  49 8B D6                        mov rdx, r14
009768DC  E8 F7 34 B4 FF                  call 0x1404b9dd8
009768E1  45 33 DB                        xor r11d, r11d
009768E4  85 C0                           test eax, eax
009768E6  0F 89 4B FF FF FF               jns 0x140976837
009768EC  83 CB 08                        or ebx, 8
009768EF  41 89 9E B8 00 00 00            mov dword ptr [r14 + 0xb8], ebx
009768F6  E9 3C FF FF FF                  jmp 0x140976837
009768FB  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
009768FF  48 8D 45 A8                     lea rax, [rbp - 0x58]
00976903  48 3B C8                        cmp rcx, rax
00976906  0F 84 56 03 00 00               je 0x140976c62
0097690C  48 8D 45 A8                     lea rax, [rbp - 0x58]
00976910  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00976914  0F 85 C7 03 00 00               jne 0x140976ce1
0097691A  48 8B 01                        mov rax, qword ptr [rcx]
0097691D  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00976921  0F 85 BA 03 00 00               jne 0x140976ce1
00976927  48 8D 55 A8                     lea rdx, [rbp - 0x58]
0097692B  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0097692F  48 89 50 08                     mov qword ptr [rax + 8], rdx
00976933  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00976938  48 81 C1 BC 00 00 00            add rcx, 0xbc
0097693F  E8 9C 70 F6 FF                  call 0x1408dd9e0
00976944  45 33 DB                        xor r11d, r11d
00976947  84 C0                           test al, al
00976949  0F 85 AB 02 00 00               jne 0x140976bfa
0097694F  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00976954  4C 39 9B B0 00 00 00            cmp qword ptr [rbx + 0xb0], r11
0097695B  0F 85 99 02 00 00               jne 0x140976bfa
00976961  4C 8B BB 90 00 00 00            mov r15, qword ptr [rbx + 0x90]
00976968  4D 85 FF                        test r15, r15
0097696B  0F 84 AC 00 00 00               je 0x140976a1d
00976971  41 8B BE 98 00 00 00            mov edi, dword ptr [r14 + 0x98]
00976978  41 8B D3                        mov edx, r11d
0097697B  85 FF                           test edi, edi
0097697D  74 4A                           je 0x1409769c9
0097697F  44 8B 93 98 00 00 00            mov r10d, dword ptr [rbx + 0x98]
00976986  41 8B CB                        mov ecx, r11d
00976989  45 85 D2                        test r10d, r10d
0097698C  74 35                           je 0x1409769c3
0097698E  4D 8B 9E 90 00 00 00            mov r11, qword ptr [r14 + 0x90]
00976995  44 8B C2                        mov r8d, edx
00976998  4D 03 C0                        add r8, r8
0097699B  4B 8B 04 C3                     mov rax, qword ptr [r11 + r8*8]
0097699F  44 8B C9                        mov r9d, ecx
009769A2  49 C1 E1 04                     shl r9, 4
009769A6  4D 03 CF                        add r9, r15
009769A9  49 3B 01                        cmp rax, qword ptr [r9]
009769AC  75 0B                           jne 0x1409769b9
009769AE  4B 8B 44 C3 08                  mov rax, qword ptr [r11 + r8*8 + 8]
009769B3  49 3B 41 08                     cmp rax, qword ptr [r9 + 8]
009769B7  74 5C                           je 0x140976a15
009769B9  FF C1                           inc ecx
009769BB  41 3B CA                        cmp ecx, r10d
009769BE  72 DB                           jb 0x14097699b
009769C0  45 33 DB                        xor r11d, r11d
009769C3  FF C2                           inc edx
009769C5  3B D7                           cmp edx, edi
009769C7  72 BD                           jb 0x140976986
009769C9  E8 76 0F B8 FF                  call 0x1404f7944
009769CE  45 33 DB                        xor r11d, r11d
009769D1  85 C0                           test eax, eax
009769D3  0F 84 E9 00 00 00               je 0x140976ac2
009769D9  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
009769DE  C7 80 C0 01 00 00 B9 02 00 C0   mov dword ptr [rax + 0x1c0], 0xc00002b9
009769E8  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
009769EC  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
009769F1  49 8D 4F 18                     lea rcx, [r15 + 0x18]
009769F5  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
009769F9  48 39 0A                        cmp qword ptr [rdx], rcx
009769FC  0F 85 DF 02 00 00               jne 0x140976ce1
00976A02  48 89 08                        mov qword ptr [rax], rcx
00976A05  48 89 50 08                     mov qword ptr [rax + 8], rdx
00976A09  48 89 02                        mov qword ptr [rdx], rax
00976A0C  48 89 41 08                     mov qword ptr [rcx + 8], rax
00976A10  E9 E6 FE FF FF                  jmp 0x1409768fb
00976A15  45 33 DB                        xor r11d, r11d
00976A18  4D 85 C9                        test r9, r9
00976A1B  74 A6                           je 0x1409769c3
00976A1D  4D 85 ED                        test r13, r13
00976A20  0F 84 80 00 00 00               je 0x140976aa6
00976A26  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00976A2A  48 85 C9                        test rcx, rcx
00976A2D  74 57                           je 0x140976a86
00976A2F  0F B7 01                        movzx eax, word ptr [rcx]
00976A32  66 83 F8 2A                     cmp ax, 0x2a
00976A36  75 07                           jne 0x140976a3f
00976A38  66 83 79 02 00                  cmp word ptr [rcx + 2], 0
00976A3D  74 42                           je 0x140976a81
00976A3F  48 8B F9                        mov rdi, rcx
00976A42  66 85 C0                        test ax, ax
00976A45  74 3F                           je 0x140976a86
00976A47  48 8B D7                        mov rdx, rdi
00976A4A  48 8B CB                        mov rcx, rbx
00976A4D  E8 86 13 C3 FF                  call 0x1405a7dd8
00976A52  45 33 DB                        xor r11d, r11d
00976A55  84 C0                           test al, al
00976A57  75 23                           jne 0x140976a7c
00976A59  48 83 C8 FF                     or rax, 0xffffffffffffffff
00976A5D  48 FF C0                        inc rax
00976A60  66 44 39 1C 47                  cmp word ptr [rdi + rax*2], r11w
00976A65  75 F6                           jne 0x140976a5d
00976A67  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00976A6B  48 83 C7 02                     add rdi, 2
00976A6F  66 44 39 1F                     cmp word ptr [rdi], r11w
00976A73  74 11                           je 0x140976a86
00976A75  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00976A7A  EB CB                           jmp 0x140976a47
00976A7C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00976A81  48 85 DB                        test rbx, rbx
00976A84  75 20                           jne 0x140976aa6
00976A86  E8 B9 0E B8 FF                  call 0x1404f7944
00976A8B  45 33 DB                        xor r11d, r11d
00976A8E  85 C0                           test eax, eax
00976A90  74 30                           je 0x140976ac2
00976A92  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00976A97  C7 80 C0 01 00 00 19 07 00 C0   mov dword ptr [rax + 0x1c0], 0xc0000719
00976AA1  E9 42 FF FF FF                  jmp 0x1409769e8
00976AA6  F7 83 B8 00 00 00 00 02 00 00   test dword ptr [rbx + 0xb8], 0x200
00976AB0  74 23                           je 0x140976ad5
00976AB2  E8 8D 0E B8 FF                  call 0x1404f7944
00976AB7  45 33 DB                        xor r11d, r11d
00976ABA  85 C0                           test eax, eax
00976ABC  0F 85 26 FF FF FF               jne 0x1409769e8
00976AC2  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00976AC7  E8 88 C8 DB FF                  call 0x140733354
00976ACC  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
00976AD0  E9 85 01 00 00                  jmp 0x140976c5a
00976AD5  49 8D 8E D0 00 00 00            lea rcx, [r14 + 0xd0]
00976ADC  48 8B 39                        mov rdi, qword ptr [rcx]
00976ADF  EB 23                           jmp 0x140976b04
00976AE1  48 8B 87 BC 00 00 00            mov rax, qword ptr [rdi + 0xbc]
00976AE8  48 3B 83 BC 00 00 00            cmp rax, qword ptr [rbx + 0xbc]
00976AEF  75 10                           jne 0x140976b01
00976AF1  48 8B 87 C4 00 00 00            mov rax, qword ptr [rdi + 0xc4]
00976AF8  48 3B 83 C4 00 00 00            cmp rax, qword ptr [rbx + 0xc4]
00976AFF  74 3C                           je 0x140976b3d
00976B01  48 8B 3F                        mov rdi, qword ptr [rdi]
00976B04  48 3B F9                        cmp rdi, rcx
00976B07  75 D8                           jne 0x140976ae1
00976B09  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
00976B0D  48 85 DB                        test rbx, rbx
00976B10  0F 84 E5 FD FF FF               je 0x1409768fb
00976B16  49 8D 86 D0 00 00 00            lea rax, [r14 + 0xd0]
00976B1D  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00976B21  48 39 01                        cmp qword ptr [rcx], rax
00976B24  0F 85 B7 01 00 00               jne 0x140976ce1
00976B2A  48 89 03                        mov qword ptr [rbx], rax
00976B2D  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
00976B31  48 89 19                        mov qword ptr [rcx], rbx
00976B34  48 89 58 08                     mov qword ptr [rax + 8], rbx
00976B38  E9 BE FD FF FF                  jmp 0x1409768fb
00976B3D  4C 39 9F 90 00 00 00            cmp qword ptr [rdi + 0x90], r11
00976B44  74 37                           je 0x140976b7d
00976B46  4C 39 9B 90 00 00 00            cmp qword ptr [rbx + 0x90], r11
00976B4D  75 37                           jne 0x140976b86
00976B4F  48 8B FB                        mov rdi, rbx
00976B52  49 8B DB                        mov rbx, r11
00976B55  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00976B5A  48 85 FF                        test rdi, rdi
00976B5D  74 AA                           je 0x140976b09
00976B5F  E8 E0 0D B8 FF                  call 0x1404f7944
00976B64  45 33 DB                        xor r11d, r11d
00976B67  85 C0                           test eax, eax
00976B69  75 58                           jne 0x140976bc3
00976B6B  48 8B CF                        mov rcx, rdi
00976B6E  E8 E1 C7 DB FF                  call 0x140733354
00976B73  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00976B78  45 33 DB                        xor r11d, r11d
00976B7B  EB 8C                           jmp 0x140976b09
00976B7D  4C 39 9B 90 00 00 00            cmp qword ptr [rbx + 0x90], r11
00976B84  75 15                           jne 0x140976b9b
00976B86  45 33 C0                        xor r8d, r8d
00976B89  48 8B D7                        mov rdx, rdi
00976B8C  48 8B CB                        mov rcx, rbx
00976B8F  E8 44 32 B4 FF                  call 0x1404b9dd8
00976B94  45 33 DB                        xor r11d, r11d
00976B97  85 C0                           test eax, eax
00976B99  79 B4                           jns 0x140976b4f
00976B9B  48 8B 0F                        mov rcx, qword ptr [rdi]
00976B9E  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
00976BA2  0F 85 39 01 00 00               jne 0x140976ce1
00976BA8  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00976BAC  48 39 38                        cmp qword ptr [rax], rdi
00976BAF  0F 85 2C 01 00 00               jne 0x140976ce1
00976BB5  48 89 08                        mov qword ptr [rax], rcx
00976BB8  48 89 41 08                     mov qword ptr [rcx + 8], rax
00976BBC  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00976BC1  EB 97                           jmp 0x140976b5a
00976BC3  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
00976BC7  C7 87 C0 01 00 00 72 02 00 C0   mov dword ptr [rdi + 0x1c0], 0xc0000272
00976BD1  49 8D 47 18                     lea rax, [r15 + 0x18]
00976BD5  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00976BD9  48 39 01                        cmp qword ptr [rcx], rax
00976BDC  0F 85 FF 00 00 00               jne 0x140976ce1
00976BE2  48 89 07                        mov qword ptr [rdi], rax
00976BE5  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
00976BE9  48 89 39                        mov qword ptr [rcx], rdi
00976BEC  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00976BF1  48 89 78 08                     mov qword ptr [rax + 8], rdi
00976BF5  E9 13 FF FF FF                  jmp 0x140976b0d
00976BFA  E8 45 0D B8 FF                  call 0x1404f7944
00976BFF  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00976C04  85 C0                           test eax, eax
00976C06  75 07                           jne 0x140976c0f
00976C08  E8 47 C7 DB FF                  call 0x140733354
00976C0D  EB 4B                           jmp 0x140976c5a
00976C0F  48 81 C1 BC 00 00 00            add rcx, 0xbc
00976C16  E8 C5 6D F6 FF                  call 0x1408dd9e0
00976C1B  F6 D8                           neg al
00976C1D  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00976C22  1B C9                           sbb ecx, ecx
00976C24  81 E1 52 FF FF FF               and ecx, 0xffffff52
00976C2A  81 C1 BB 00 00 C0               add ecx, 0xc00000bb
00976C30  89 88 C0 01 00 00               mov dword ptr [rax + 0x1c0], ecx
00976C36  49 8D 4F 18                     lea rcx, [r15 + 0x18]
00976C3A  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00976C3E  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00976C43  48 39 0A                        cmp qword ptr [rdx], rcx
00976C46  0F 85 95 00 00 00               jne 0x140976ce1
00976C4C  48 89 08                        mov qword ptr [rax], rcx
00976C4F  48 89 50 08                     mov qword ptr [rax + 8], rdx
00976C53  48 89 02                        mov qword ptr [rdx], rax
00976C56  48 89 41 08                     mov qword ptr [rcx + 8], rax
00976C5A  45 33 DB                        xor r11d, r11d
00976C5D  E9 99 FC FF FF                  jmp 0x1409768fb
00976C62  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00976C66  4C 89 30                        mov qword ptr [rax], r14
00976C69  4D 8B F3                        mov r14, r11
00976C6C  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00976C71  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00976C76  48 3B C8                        cmp rcx, rax
00976C79  74 2E                           je 0x140976ca9
00976C7B  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00976C80  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00976C84  75 5B                           jne 0x140976ce1
00976C86  48 8B 01                        mov rax, qword ptr [rcx]
00976C89  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00976C8D  75 52                           jne 0x140976ce1
00976C8F  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00976C94  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00976C99  48 89 50 08                     mov qword ptr [rax + 8], rdx
00976C9D  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00976CA2  E8 AD C6 DB FF                  call 0x140733354
00976CA7  EB C3                           jmp 0x140976c6c
00976CA9  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00976CAD  48 8D 45 A8                     lea rax, [rbp - 0x58]
00976CB1  48 3B C8                        cmp rcx, rax
00976CB4  74 32                           je 0x140976ce8
00976CB6  48 8D 45 A8                     lea rax, [rbp - 0x58]
00976CBA  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00976CBE  75 21                           jne 0x140976ce1
00976CC0  48 8B 01                        mov rax, qword ptr [rcx]
00976CC3  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00976CC7  75 18                           jne 0x140976ce1
00976CC9  48 8D 55 A8                     lea rdx, [rbp - 0x58]
00976CCD  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00976CD1  48 89 50 08                     mov qword ptr [rax + 8], rdx
00976CD5  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00976CDA  E8 75 C6 DB FF                  call 0x140733354
00976CDF  EB C8                           jmp 0x140976ca9
00976CE1  B9 03 00 00 00                  mov ecx, 3
00976CE6  CD 29                           int 0x29
00976CE8  4D 85 F6                        test r14, r14
00976CEB  74 08                           je 0x140976cf5
00976CED  49 8B CE                        mov rcx, r14
00976CF0  E8 5F C6 DB FF                  call 0x140733354
00976CF5  4D 85 E4                        test r12, r12
00976CF8  74 0A                           je 0x140976d04
00976CFA  33 D2                           xor edx, edx
00976CFC  49 8B CC                        mov rcx, r12
00976CFF  E8 6C BB 20 00                  call 0x140b82870
00976D04  8B C6                           mov eax, esi
00976D06  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00976D0A  48 33 CC                        xor rcx, rsp
00976D0D  E8 2E 59 D3 FF                  call 0x1406ac640
00976D12  48 8B 9C 24 78 01 00 00         mov rbx, qword ptr [rsp + 0x178]
00976D1A  48 81 C4 20 01 00 00            add rsp, 0x120
00976D21  41 5F                           pop r15
00976D23  41 5E                           pop r14
00976D25  41 5D                           pop r13
00976D27  41 5C                           pop r12
00976D29  5F                              pop rdi
00976D2A  5E                              pop rsi
00976D2B  5D                              pop rbp
00976D2C  C3                              ret
00976D2D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgFindDeviceDriver(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int16 v_stack_mC2;
    unsigned __int8 v_stack_mC3;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 4802289)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r12 = 0;
    v_stack_m68 = a3;
    result = 0;
    v_stack_mD0 = a1;
    v_stack_m50 = 0;
    v_stack_mF0 = 0;
    v_stack_mE0 = v_stack_mE8;
    v_stack_m90 = 0;
    v_stack_mE8 = v_stack_mE8;
    v_stack_m70 = 0;
    v_stack_mA8 = v_stack_mB0;
    v_stack_mC4 = 0;
    v_stack_mB0 = v_stack_mB0;
    v_stack_mC0 = (unsigned int)(v_r12 + 1);
    v_stack_mC8 = 0;
    v_stack_mF8 = 0;
    v_stack_m60 = v_xmm0;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        a1 = a1;
        result = PiDevCfgClearDeviceDrivers(a1, a2, a3, a4);
    }
    if (a2 == 0) goto loc_00976103;
    v_stack_m90 = a2;
    result = (result) | (-1);
loc_009760E1:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(a2 + result * 2)) != 0) goto loc_009760E1;
    result = (unsigned __int16)(-(*(unsigned __int16 *)(a2 + 2 + result * 2)));
    result = (result) & (a2 + 2 + result * 2);
    v_stack_m70 = result;
loc_00976103:
    result = (unsigned int)((unsigned int)(v_r12 + 1));
    if ((*(unsigned __int8 *)(v_rip + 5177659)) != 0) { result = 3; }
    v_stack_m88 = (unsigned int)(result);
    result = PiDevCfgQueryDriverPolicy(v_stack_m60, a2, a3, a4);
    v_stack_mA0 = 520;
    result = ExAllocatePool2(256, 520, (unsigned int)(0x63647050ULL), a4);
    v_r11 = 0;
    v_stack_m98 = result;
    if (result != 0) goto loc_00976155;
loc_0097614B:
    goto loc_00976C6C;
loc_00976155:
    v_stack_mBC = 0;
    v_stack_m80 = a1 + 48;
loc_0097616A:
    v_stack_m78 = *(unsigned __int64 *)(a1 + 48);
    if (*(unsigned __int64 *)(a1 + 48) == 0) goto loc_009766A3;
    v_stack_mD8 = 0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 48))) == 0) goto loc_0097669B;
loc_0097618C:
    v_stack_m108 = 0;
    a4 = (a4) | (-1);
    v_stack_m110 = v_stack_mC8;
    v_stack_m118 = 520;
    v_stack_m120 = result;
    v_stack_m128 = v_stack_mC0;
    v_stack_m130 = v_rip - 9847406;
    v_stack_mC0 = 1;
    v_stack_mC8 = 0;
    v_stack_m138 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 5177861), *(unsigned __int64 *)(a1 + 48), a4 + 12, a4);
    v_r11 = 0;
    if (!sign_flag) goto loc_0097631E;
loc_009761E5:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000023ULL) goto loc_0097631E;
    if (v_stack_mC8 <= 520) goto loc_00976392;
    v_stack_mA0 = (unsigned int)(v_stack_mC8);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a4 + 12, a4);
    }
    result = ExAllocatePool2(256, (unsigned int)(v_stack_mC8), (unsigned int)(0x63647050ULL), a4);
    v_r11 = 0;
    v_stack_m98 = result;
    if (result == 0) goto loc_0097614B;
    v_stack_m108 = 0;
    v_stack_m110 = v_stack_mC8;
    a4 = (a4) | (-1);
    v_stack_m118 = (unsigned int)((unsigned int)(v_stack_mC8));
    v_stack_m120 = result;
    v_stack_m128 = v_stack_mC0;
    v_stack_m130 = v_rip - 9847671;
    v_stack_m138 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 5177691), *(unsigned __int64 *)(a1 + 48), v_r11 + 11, a4);
    v_r11 = 0;
    if (sign_flag) goto loc_009761E5;
loc_0097628B:
    if (v_stack_mC0 != 0x2012ULL) goto loc_0097664E;
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_0097664A;
loc_009762A6:
    result = wcschr(result, 92, v_r11 + 11, a4);
    v_r11 = 0;
    if (result == 0) goto loc_00976620;
    a3 = 0;
    a2 = 0;
    result = DrvDbSplitDeviceIdDriverInfMatch(result, a2, a3, v_stack_mC4);
    v_r11 = 0;
    if (sign_flag) goto loc_00976646;
    *(unsigned __int16 *)(result) = 0;
    v_stack_mB8 = result + 2;
    if (((unsigned int)((unsigned int)(v_stack_mBC))) != 2) goto loc_0097630D;
    if (((unsigned __int8)((unsigned int)(v_stack_mC4))) != 3) goto loc_00976620;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m88)))) | (8));
loc_0097630D:
    if (((unsigned __int8)((unsigned int)(v_stack_mC4))) != 1) goto loc_0097639A;
    goto loc_009763C3;
loc_0097631E:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC000009AULL) goto loc_0097668D;
    v_stack_m98 = result;
    v_stack_mA0 = (unsigned int)((unsigned int)((unsigned int)(v_stack_mC4)));
    if (!sign_flag) goto loc_0097628B;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))) == 0xC0000022ULL) goto loc_0097636D;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))) == 0xC0000467ULL) goto loc_0097636D;
    v_stack_mA0 = (unsigned int)((unsigned int)((unsigned int)(v_stack_mC4)));
    v_stack_m98 = result;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_00976392;
    v_stack_mF0 = (unsigned int)((unsigned int)(0xC0000034ULL));
    goto loc_00976387;
loc_0097636D:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL)))) == 0) goto loc_00976381;
    v_stack_mA0 = (unsigned int)(0xC0000034ULL);
    v_stack_m98 = result;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL))))) == 0xC0000034ULL) goto loc_00976392;
loc_00976381:
    v_stack_mF0 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_00976387:
    v_stack_m98 = result;
    v_stack_mA0 = (unsigned int)((unsigned int)((unsigned int)(v_stack_mC4)));
loc_00976392:
    goto loc_0097664E;
loc_0097639A:
    if (((unsigned __int8)((unsigned int)(v_stack_mC4))) != 2) goto loc_009763B0;
    result = (unsigned int)((v_stack_mC2) << (8));
    result = (unsigned int)((result) + (v_stack_mD8));
    goto loc_009763C6;
loc_009763B0:
    if (((unsigned __int8)((unsigned int)(v_stack_mC4))) != 3) goto loc_00976620;
    result = (unsigned int)((v_stack_mC2) << (8));
    result = (unsigned int)((result) + (v_stack_mD8));
loc_009763C3:
loc_009763C6:
    if (((unsigned int)(result)) >= 0x1000ULL) { result = (unsigned int)((unsigned int)(0xFFFULL)); }
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mC4)))) << (13));
    a3 = (unsigned int)((a3) + (0));
    a4 = (unsigned int)((v_stack_mC3) << (16));
    a3 = (unsigned int)((a3) + ((unsigned int)(result)));
    v_stack_m128 = v_stack_mF8;
    v_stack_m130 = v_stack_m60;
    v_stack_m138 = (unsigned int)(a2);
    result = PiDevCfgQueryDriverNode(result, *(unsigned __int64 *)(a1 + 48), a3, a4);
    v_r11 = 0;
    if (!sign_flag) goto loc_0097641B;
    goto loc_00976620;
loc_0097641B:
    if (*(unsigned __int64 *)(v_stack_mF8 + 168) == 0) goto loc_009764B7;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mF8 + 168))) == 0) goto loc_009764A2;
loc_0097643A:
loc_00976441:
    if (*(unsigned __int64 *)(v_stack_mD0 + 48) == 0) goto loc_00976459;
    result = PnpMultiSzContainsString(*(unsigned __int64 *)(v_stack_mD0 + 48), *(unsigned __int64 *)(v_stack_mF8 + 168), a3, a4);
    v_r11 = 0;
    if (result != 0) goto loc_00976468;
loc_00976459:
    v_r12 = (unsigned int)((0) + 1);
    v_rdi = (v_stack_mD0 + 48) + (16);
    if (((unsigned int)(v_r12)) < 3) goto loc_00976441;
    goto loc_00976474;
loc_00976468:
    *(unsigned __int64 *)(v_stack_mF8 + 176) = *(unsigned __int64 *)(v_stack_mF8 + 168);
loc_00976474:
    if ((*(unsigned __int64 *)(v_stack_mF8 + 176)) != 0) goto loc_0097649E;
    result = (v_stack_mF8) | (-1);
loc_00976486:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mF8 + 168) + result * 2)) != 0) goto loc_00976486;
    v_r15 = (*(unsigned __int64 *)(v_stack_mF8 + 168) + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_r15)) != 0) goto loc_0097643A;
loc_0097649E:
loc_009764A2:
    v_rdi = v_stack_mF8;
    if ((*(unsigned __int64 *)(v_stack_mF8 + 176)) != 0) {
        v_rdi = v_stack_mF8;
    }
    if (((unsigned __int8)((unsigned int)(v_stack_mC4))) != 3) goto loc_009764E4;
    if ((*(unsigned __int64 *)(v_stack_mA8)) != v_stack_mB0) goto loc_00976CE1;
    *(unsigned __int64 *)(v_rdi + 8) = v_stack_mA8;
    *(unsigned __int64 *)(v_rdi) = v_stack_mB0;
    *(unsigned __int64 *)(v_stack_mA8) = v_rdi;
    v_stack_mA8 = v_rdi;
    goto loc_0097661C;
loc_009764E4:
    if (((*(unsigned int *)(v_rdi + 184)) & (512)) == 0) goto loc_0097654E;
    if ((*(unsigned __int64 *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(unsigned __int64 *)(v_rdi + 8) = v_stack_mE0;
    *(unsigned __int64 *)(v_rdi) = v_stack_mE8;
    *(unsigned __int64 *)(v_stack_mE0) = v_rdi;
    v_stack_mE0 = v_rdi;
    if (v_stack_m90 == 0) goto loc_0097661C;
    result = PiDevCfgMatchDriverConfigurationId(v_stack_mF8, v_stack_m90, a3, a4);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00976620;
    v_stack_mF0 = (unsigned int)((unsigned int)(0xC000036BULL));
    goto loc_00976624;
loc_0097654E:
    if (v_stack_m90 == 0) goto loc_0097659F;
    result = PiDevCfgMatchDriverConfigurationId((unsigned int)(0xC000036BULL), v_stack_m90, a3, a4);
    v_r11 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_0097659A;
    if ((*(unsigned __int64 *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mF8 + 8) = v_stack_mE0;
    *(unsigned __int64 *)(v_stack_mF8) = v_stack_mE8;
    *(unsigned __int64 *)(v_stack_mE0) = v_stack_mF8;
    v_stack_mE0 = v_stack_mF8;
    goto loc_0097661C;
loc_0097659A:
loc_0097659F:
    if ((*(unsigned __int64 *)(v_stack_mF8 + 176)) == 0) goto loc_009765D1;
loc_009765B2:
    if ((*(unsigned __int64 *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mF8) = v_stack_mE8;
    *(unsigned __int64 *)(v_stack_mF8 + 8) = v_stack_mE0;
    *(unsigned __int64 *)(v_stack_mE0) = v_stack_mF8;
    v_stack_mE0 = v_stack_mF8;
    goto loc_0097661C;
loc_009765D1:
    if (0 != 0) goto loc_009765DB;
    goto loc_0097661C;
loc_009765DB:
    a3 = 0;
    result = PiDevCfgCompareDrivers(v_stack_mF8, v_stack_mF8, a3, a4);
    v_r11 = 0;
    if (!sign_flag) goto loc_009765B2;
    if ((*(unsigned __int64 *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mF8 + 8) = v_stack_mE0;
    *(unsigned __int64 *)(v_stack_mF8) = v_stack_mE8;
    *(unsigned __int64 *)(v_stack_mE0) = v_stack_mF8;
    v_stack_mE0 = v_stack_mF8;
loc_0097661C:
loc_00976620:
loc_00976624:
    result = (v_stack_mE0) | (-1);
loc_00976628:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_mB8 + result * 2)) != 0) goto loc_00976628;
    v_r15 = (v_stack_mB8 + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_r15)) != 0) goto loc_009762A6;
    goto loc_0097664A;
loc_00976646:
loc_0097664A:
loc_0097664E:
    result = (result) | (-1);
loc_00976652:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m78 + result * 2)) != 0) goto loc_00976652;
    v_r13 = (v_stack_m78 + result * 2) + (2);
    v_r15 = (unsigned int)(((unsigned int)(v_stack_mD8)) + 1);
    v_stack_m78 = v_r13;
    v_stack_mD8 = (unsigned int)(v_r15);
    if ((*(unsigned __int16 *)(v_r13)) != 0) goto loc_0097618C;
    goto loc_00976694;
loc_0097668D:
loc_00976694:
loc_0097669B:
    if (sign_flag) goto loc_00976C6C;
loc_009766A3:
    result = (unsigned int)(((unsigned int)(v_stack_mBC)) + 1);
    a1 = (v_stack_m80) + (16);
    v_stack_mBC = (unsigned int)(result);
    v_stack_m80 = a1;
    if (((unsigned int)(result)) < 3) goto loc_0097616A;
    if (sign_flag) goto loc_00976C6C;
    if (v_stack_m90 == 0) goto loc_009767A3;
    if (v_stack_mF8 != 0) goto loc_00976833;
    if (((unsigned int)((unsigned int)(v_stack_mF0))) == 0xC000036BULL) goto loc_009767AC;
    result = wcschr(v_stack_m90, v_stack_mF8 + 58, a3, a4);
    v_r11 = 0;
    if (result != 0) goto loc_00976704;
loc_009766FA:
    goto loc_00976C6C;
loc_00976704:
    *(unsigned __int16 *)(result) = 0;
    result = wcschr(result + 2, 44, a3, a4);
    v_r11 = 0;
    if (result == 0) goto loc_009766FA;
    *(unsigned __int16 *)(result) = 0;
    a4 = 0;
    v_stack_m128 = v_stack_mF8;
    a3 = 0;
    v_stack_m130 = v_stack_m60;
    v_stack_m138 = 4;
    result = PiDevCfgQueryDriverNode(v_stack_m90, result + 2, a3, a4);
    v_r11 = 0;
    if (sign_flag) goto loc_009767AC;
    if (((*(unsigned int *)(v_stack_mF8 + 184)) & (512)) == 0) goto loc_0097679B;
    if ((*(unsigned __int64 *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mF8 + 8) = v_stack_mE0;
    *(unsigned __int64 *)(v_stack_mF8) = v_stack_mE8;
    *(unsigned __int64 *)(v_stack_mE0) = v_stack_mF8;
    v_stack_mE0 = v_stack_mF8;
    v_stack_mF8 = 0;
loc_0097679B:
    if (0 == 0) goto loc_009767AC;
loc_009767A3:
    if (0 != 0) goto loc_00976833;
loc_009767AC:
    if ((unsigned int)((unsigned int)(0xC000036BULL)) == 0) goto loc_009767BA;
    v_rsi = (unsigned int)((unsigned int)((unsigned int)(0xC000036BULL)));
    if (((unsigned int)((unsigned int)(0xC000036BULL))) == 0xC0000034ULL) {
        v_rsi = 0xC0000490ULL;
    }
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(0, v_stack_mE8, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00976C6C;
loc_009767D0:
    if (v_stack_mE8 == v_stack_mE8) goto loc_00976C6C;
    if ((*(unsigned __int64 *)(v_stack_mE8 + 8)) != v_stack_mE8) goto loc_00976CE1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 8)) != v_stack_mE8) goto loc_00976CE1;
    v_stack_mE8 = *(unsigned __int64 *)(v_stack_mE8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 8) = v_stack_mE8;
    v_stack_mF8 = v_stack_mE8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24 + 8))) != (v_stack_mD0 + 24)) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mE8) = v_stack_mD0 + 24;
    *(unsigned __int64 *)(v_stack_mE8 + 8) = *(unsigned __int64 *)(v_stack_mD0 + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24 + 8)) = v_stack_mE8;
    *(unsigned __int64 *)(v_stack_mD0 + 24 + 8) = v_stack_mE8;
    goto loc_009767D0;
loc_00976833:
loc_00976837:
    if (v_stack_mE8 == v_stack_mE8) goto loc_009768FB;
    if ((*(unsigned __int64 *)(v_stack_mE8 + 8)) != v_stack_mE8) goto loc_00976CE1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 8)) != v_stack_mE8) goto loc_00976CE1;
    v_stack_mE8 = *(unsigned __int64 *)(v_stack_mE8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 8) = v_stack_mE8;
    v_stack_mF8 = v_stack_mE8;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_stack_mE8), v_stack_mE8, a3, a4);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) {
        a1 = v_stack_mD0 + 24;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != a1) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mF8) = a1;
    *(unsigned __int64 *)(v_stack_mF8 + 8) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) = v_stack_mF8;
    *(unsigned __int64 *)(a1 + 8) = v_stack_mF8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mF8 + 184)))) & (4)) == 0) goto loc_00976837;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(0 + 184)))) & (8)) != 0) goto loc_00976837;
    result = PiDevCfgCompareDrivers(v_stack_mF8, 0, 4, a4);
    v_r11 = 0;
    if (!sign_flag) goto loc_00976837;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 184))) | (8));
    *(unsigned int *)(0 + 184) = (unsigned int)(v_rbx);
    goto loc_00976837;
loc_009768FB:
    if (v_stack_mB0 == v_stack_mB0) goto loc_00976C62;
    if ((*(unsigned __int64 *)(v_stack_mB0 + 8)) != v_stack_mB0) goto loc_00976CE1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0) + 8)) != v_stack_mB0) goto loc_00976CE1;
    v_stack_mB0 = *(unsigned __int64 *)(v_stack_mB0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0) + 8) = v_stack_mB0;
    v_stack_mF8 = v_stack_mB0;
    a1 = (v_stack_mB0) + (188);
    result = PnpIsNullGuid(a1, v_stack_mB0, 4, a4);
    v_r11 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00976BFA;
    if ((*(unsigned __int64 *)(v_stack_mF8 + 176)) != 0) goto loc_00976BFA;
    if (*(unsigned __int64 *)(v_stack_mF8 + 144) == 0) goto loc_00976A1D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 152))) == 0) goto loc_009769C9;
loc_00976986:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF8 + 152))) == 0) goto loc_009769C3;
    a3 = (0) + (0);
loc_0097699B:
    a4 = (0) << (4);
    a4 = (a4) + (*(unsigned __int64 *)(v_stack_mF8 + 144));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 144) + a3 * 8)) != (*(unsigned __int64 *)(a4))) goto loc_009769B9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 144) + a3 * 8 + 8)) == (*(unsigned __int64 *)(a4 + 8))) goto loc_00976A15;
loc_009769B9:
    a1 = (unsigned int)((0) + 1);
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF8 + 152))))) goto loc_0097699B;
    v_r11 = 0;
loc_009769C3:
    a2 = (unsigned int)((0) + 1);
    if (((unsigned int)(a2)) < ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 152))))) goto loc_00976986;
loc_009769C9:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00976AC2;
    *(unsigned int *)(v_stack_mF8 + 448) = 0xC00002B9ULL;
loc_009769E8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24 + 8))) != (v_stack_mD0 + 24)) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mF8) = v_stack_mD0 + 24;
    *(unsigned __int64 *)(v_stack_mF8 + 8) = *(unsigned __int64 *)(v_stack_mD0 + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24 + 8)) = v_stack_mF8;
    *(unsigned __int64 *)(v_stack_mD0 + 24 + 8) = v_stack_mF8;
    goto loc_009768FB;
loc_00976A15:
    v_r11 = 0;
    if (a4 == 0) goto loc_009769C3;
loc_00976A1D:
    if (v_stack_m90 == 0) goto loc_00976AA6;
    if (v_stack_m70 == 0) goto loc_00976A86;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m70))) != 42) goto loc_00976A3F;
    if ((*(unsigned __int16 *)(v_stack_m70 + 2)) == 0) goto loc_00976A81;
loc_00976A3F:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m70)) == 0) goto loc_00976A86;
loc_00976A47:
    result = PiDevCfgMatchDriverConfigurationId(v_stack_mF8, v_stack_m70, a3, a4);
    v_r11 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00976A7C;
    result = (result) | (-1);
loc_00976A5D:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m70 + result * 2)) != 0) goto loc_00976A5D;
    v_rdi = (v_stack_m70 + result * 2) + (2);
    if ((*(unsigned __int16 *)(v_rdi)) == 0) goto loc_00976A86;
    goto loc_00976A47;
loc_00976A7C:
loc_00976A81:
    if (v_stack_mF8 != 0) goto loc_00976AA6;
loc_00976A86:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(v_stack_mF8, v_stack_m70, a3, a4);
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00976AC2;
    *(unsigned int *)(v_stack_mF8 + 448) = 0xC0000719ULL;
    goto loc_009769E8;
loc_00976AA6:
    if (((*(unsigned int *)(v_stack_mF8 + 184)) & (512)) == 0) goto loc_00976AD5;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(v_stack_mF8, v_stack_m70, a3, a4);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_009769E8;
loc_00976AC2:
    result = PiDevCfgFreeDriverNode(v_stack_mF8, v_stack_m70, a3, a4);
    goto loc_00976C5A;
loc_00976AD5:
    goto loc_00976B04;
loc_00976AE1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 208) + 188)) != (*(unsigned __int64 *)(v_stack_mF8 + 188))) goto loc_00976B01;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 208) + 196)) == (*(unsigned __int64 *)(v_stack_mF8 + 196))) goto loc_00976B3D;
loc_00976B01:
loc_00976B04:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 208))) != (0 + 208)) goto loc_00976AE1;
loc_00976B09:
loc_00976B0D:
    if (v_stack_mF8 == 0) goto loc_009768FB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 208 + 8))) != (0 + 208)) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mF8) = 0 + 208;
    *(unsigned __int64 *)(v_stack_mF8 + 8) = *(unsigned __int64 *)(0 + 208 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(0 + 208 + 8)) = v_stack_mF8;
    *(unsigned __int64 *)(0 + 208 + 8) = v_stack_mF8;
    goto loc_009768FB;
loc_00976B3D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 208)) + 144)) == 0) goto loc_00976B7D;
    if ((*(unsigned __int64 *)(v_stack_mF8 + 144)) != 0) goto loc_00976B86;
loc_00976B4F:
    v_stack_mF8 = 0;
loc_00976B5A:
    if (v_stack_mF8 == 0) goto loc_00976B09;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(0 + 208 + 8), v_stack_m70, a3, a4);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00976BC3;
    result = PiDevCfgFreeDriverNode(v_stack_mF8, v_stack_m70, a3, a4);
    v_r11 = 0;
    goto loc_00976B09;
loc_00976B7D:
    if ((*(unsigned __int64 *)(v_stack_mF8 + 144)) != 0) goto loc_00976B9B;
loc_00976B86:
    a3 = 0;
    result = PiDevCfgCompareDrivers(v_stack_mF8, v_stack_mF8, a3, a4);
    v_r11 = 0;
    if (!sign_flag) goto loc_00976B4F;
loc_00976B9B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF8) + 8)) != v_stack_mF8) goto loc_00976CE1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF8 + 8))) != v_stack_mF8) goto loc_00976CE1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF8 + 8)) = *(unsigned __int64 *)(v_stack_mF8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF8) + 8) = *(unsigned __int64 *)(v_stack_mF8 + 8);
    goto loc_00976B5A;
loc_00976BC3:
    *(unsigned int *)(v_stack_mF8 + 448) = 0xC0000272ULL;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24 + 8))) != (v_stack_mD0 + 24)) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mF8) = v_stack_mD0 + 24;
    *(unsigned __int64 *)(v_stack_mF8 + 8) = *(unsigned __int64 *)(v_stack_mD0 + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24 + 8)) = v_stack_mF8;
    *(unsigned __int64 *)(v_stack_mD0 + 24 + 8) = v_stack_mF8;
    goto loc_00976B0D;
loc_00976BFA:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_stack_mD0 + 24 + 8), v_stack_mF8, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00976C0F;
    result = PiDevCfgFreeDriverNode(v_stack_mF8, v_stack_mF8, a3, a4);
    goto loc_00976C5A;
loc_00976C0F:
    a1 = (v_stack_mF8) + (188);
    result = PnpIsNullGuid(a1, v_stack_mF8, a3, a4);
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)((a1) & (0xFFFFFF52ULL));
    a1 = (unsigned int)((a1) + (0xC00000BBULL));
    *(unsigned int *)(v_stack_mF8 + 448) = (unsigned int)(a1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24 + 8))) != (v_stack_mD0 + 24)) goto loc_00976CE1;
    *(unsigned __int64 *)(v_stack_mF8) = v_stack_mD0 + 24;
    *(unsigned __int64 *)(v_stack_mF8 + 8) = *(unsigned __int64 *)(v_stack_mD0 + 24 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24 + 8)) = v_stack_mF8;
    *(unsigned __int64 *)(v_stack_mD0 + 24 + 8) = v_stack_mF8;
loc_00976C5A:
    v_r11 = 0;
    goto loc_009768FB;
loc_00976C62:
    *(unsigned __int64 *)(v_stack_m68) = 0;
loc_00976C6C:
    if (v_stack_mE8 == v_stack_mE8) goto loc_00976CA9;
    if ((*(unsigned __int64 *)(v_stack_mE8 + 8)) != v_stack_mE8) goto loc_00976CE1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 8)) != v_stack_mE8) goto loc_00976CE1;
    v_stack_mE8 = *(unsigned __int64 *)(v_stack_mE8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8) + 8) = v_stack_mE8;
    v_stack_mF8 = v_stack_mE8;
    result = PiDevCfgFreeDriverNode(v_stack_mE8, v_stack_mE8, a3, a4);
    goto loc_00976C6C;
loc_00976CA9:
    if (v_stack_mB0 == v_stack_mB0) goto loc_00976CE8;
    if ((*(unsigned __int64 *)(v_stack_mB0 + 8)) != v_stack_mB0) goto loc_00976CE1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0) + 8)) != v_stack_mB0) goto loc_00976CE1;
    v_stack_mB0 = *(unsigned __int64 *)(v_stack_mB0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0) + 8) = v_stack_mB0;
    v_stack_mF8 = v_stack_mB0;
    result = PiDevCfgFreeDriverNode(v_stack_mB0, v_stack_mB0, a3, a4);
    goto loc_00976CA9;
loc_00976CE1:
loc_00976CE8:
    if (0 != 0) {
        a1 = 0;
        result = PiDevCfgFreeDriverNode(a1, v_stack_mB0, a3, a4);
    }
    if (v_stack_m98 != 0) {
        a2 = 0;
        a1 = v_stack_m98;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (288);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgFindDeviceDriver(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint16_t v_stack_mC2;
    uint8_t v_stack_mC3;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0x4946F1)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r12 = 0;
    v_stack_m68 = Arg3;
    result = 0;
    v_stack_mD0 = Arg1;
    v_stack_m50 = 0;
    v_stack_mF0 = 0;
    v_stack_mE0 = v_stack_mE8;
    v_stack_m90 = 0;
    v_stack_mE8 = v_stack_mE8;
    v_stack_m70 = 0;
    v_stack_mA8 = v_stack_mB0;
    v_stack_mC4 = 0;
    v_stack_mB0 = v_stack_mB0;
    v_stack_mC0 = (uint32_t)(local_r12 + 1);
    v_stack_mC8 = 0;
    v_stack_mF8 = 0;
    v_stack_m60 = v_xmm0;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
        Arg1 = Arg1;
        result = PiDevCfgClearDeviceDrivers(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg2 == 0) goto loc_00976103;
    v_stack_m90 = Arg2;
    result = (result) | (-1);
loc_009760E1:
    result = (result) + 1;
    if ((*(uint16_t *)(Arg2 + result * 2)) != 0) goto loc_009760E1;
    result = (uint16_t)(-(*(uint16_t *)(Arg2 + 0x2 + result * 2)));
    result = (result) & (Arg2 + 2 + result * 2);
    v_stack_m70 = result;
loc_00976103:
    result = (uint32_t)((uint32_t)(local_r12 + 1));
    if ((*(uint8_t *)(v_rip + 0x4F013B)) != 0) { result = 3; }
    v_stack_m88 = (uint32_t)(result);
    result = PiDevCfgQueryDriverPolicy(v_stack_m60, Arg2, Arg3, Arg4);
    v_stack_mA0 = 520;
    result = ExAllocatePool2(256, 520, (uint32_t)(0x63647050ULL), Arg4);
    local_r11 = 0;
    v_stack_m98 = result;
    if (result != 0) goto loc_00976155;
loc_0097614B:
    goto loc_00976C6C;
loc_00976155:
    v_stack_mBC = 0;
    v_stack_m80 = Arg1 + 48;
loc_0097616A:
    v_stack_m78 = *(uint64_t *)(arg1 + 0x30);
    if (*(uint64_t *)(arg1 + 0x30) == 0) goto loc_009766A3;
    v_stack_mD8 = 0;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x30))) == 0) goto loc_0097669B;
loc_0097618C:
    v_stack_m108 = 0;
    Arg4 = (Arg4) | (-1);
    v_stack_m110 = v_stack_mC8;
    v_stack_m118 = 520;
    v_stack_m120 = result;
    v_stack_m128 = v_stack_mC0;
    v_stack_m130 = v_rip - 9847406;
    v_stack_mC0 = 1;
    v_stack_mC8 = 0;
    v_stack_m138 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x4F0205), *(uint64_t *)(arg1 + 0x30), Arg4 + 12, Arg4);
    local_r11 = 0;
    if (!sign_flag) goto loc_0097631E;
loc_009761E5:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000023ULL) goto loc_0097631E;
    if (v_stack_mC8 <= 520) goto loc_00976392;
    v_stack_mA0 = (uint32_t)(v_stack_mC8);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg4 + 12, Arg4);
    }
    result = ExAllocatePool2(256, (uint32_t)(v_stack_mC8), (uint32_t)(0x63647050ULL), Arg4);
    local_r11 = 0;
    v_stack_m98 = result;
    if (result == 0) goto loc_0097614B;
    v_stack_m108 = 0;
    v_stack_m110 = v_stack_mC8;
    Arg4 = (Arg4) | (-1);
    v_stack_m118 = (uint32_t)((uint32_t)(v_stack_mC8));
    v_stack_m120 = result;
    v_stack_m128 = v_stack_mC0;
    v_stack_m130 = v_rip - 9847671;
    v_stack_m138 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x4F015B), *(uint64_t *)(arg1 + 0x30), local_r11 + 11, Arg4);
    local_r11 = 0;
    if (sign_flag) goto loc_009761E5;
loc_0097628B:
    if (v_stack_mC0 != 0x2012ULL) goto loc_0097664E;
    if ((*(uint16_t *)(result)) == 0) goto loc_0097664A;
loc_009762A6:
    result = wcschr(result, 92, local_r11 + 11, Arg4);
    local_r11 = 0;
    if (result == 0) goto loc_00976620;
    Arg3 = 0;
    Arg2 = 0;
    result = DrvDbSplitDeviceIdDriverInfMatch(result, Arg2, Arg3, v_stack_mC4);
    local_r11 = 0;
    if (sign_flag) goto loc_00976646;
    *(uint16_t *)(result) = 0;
    v_stack_mB8 = result + 2;
    if (((uint32_t)((uint32_t)(v_stack_mBC))) != 2) goto loc_0097630D;
    if (((uint8_t)((uint32_t)(v_stack_mC4))) != 3) goto loc_00976620;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m88)))) | (8));
loc_0097630D:
    if (((uint8_t)((uint32_t)(v_stack_mC4))) != 1) goto loc_0097639A;
    goto loc_009763C3;
loc_0097631E:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC000009AULL) goto loc_0097668D;
    v_stack_m98 = result;
    v_stack_mA0 = (uint32_t)((uint32_t)((uint32_t)(v_stack_mC4)));
    if (!sign_flag) goto loc_0097628B;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))) == 0xC0000022ULL) goto loc_0097636D;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))) == 0xC0000467ULL) goto loc_0097636D;
    v_stack_mA0 = (uint32_t)((uint32_t)((uint32_t)(v_stack_mC4)));
    v_stack_m98 = result;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_00976392;
    v_stack_mF0 = (uint32_t)((uint32_t)(0xC0000034ULL));
    goto loc_00976387;
loc_0097636D:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL)))) == 0) goto loc_00976381;
    v_stack_mA0 = (uint32_t)(0xC0000034ULL);
    v_stack_m98 = result;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL))))) == 0xC0000034ULL) goto loc_00976392;
loc_00976381:
    v_stack_mF0 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_00976387:
    v_stack_m98 = result;
    v_stack_mA0 = (uint32_t)((uint32_t)((uint32_t)(v_stack_mC4)));
loc_00976392:
    goto loc_0097664E;
loc_0097639A:
    if (((uint8_t)((uint32_t)(v_stack_mC4))) != 2) goto loc_009763B0;
    result = (uint32_t)((v_stack_mC2) << (8));
    result = (uint32_t)((result) + (v_stack_mD8));
    goto loc_009763C6;
loc_009763B0:
    if (((uint8_t)((uint32_t)(v_stack_mC4))) != 3) goto loc_00976620;
    result = (uint32_t)((v_stack_mC2) << (8));
    result = (uint32_t)((result) + (v_stack_mD8));
loc_009763C3:
loc_009763C6:
    if (((uint32_t)(result)) >= 0x1000ULL) { result = (uint32_t)((uint32_t)(0xFFFULL)); }
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mC4)))) << (13));
    Arg3 = (uint32_t)((Arg3) + (0));
    Arg4 = (uint32_t)((v_stack_mC3) << (16));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(result)));
    v_stack_m128 = v_stack_mF8;
    v_stack_m130 = v_stack_m60;
    v_stack_m138 = (uint32_t)(Arg2);
    result = PiDevCfgQueryDriverNode(result, *(uint64_t *)(arg1 + 0x30), Arg3, Arg4);
    local_r11 = 0;
    if (!sign_flag) goto loc_0097641B;
    goto loc_00976620;
loc_0097641B:
    if (*(uint64_t *)(v_stack_mF8 + 0xA8) == 0) goto loc_009764B7;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_mF8 + 0xA8))) == 0) goto loc_009764A2;
loc_0097643A:
loc_00976441:
    if (*(uint64_t *)(v_stack_mD0 + 0x30) == 0) goto loc_00976459;
    result = PnpMultiSzContainsString(*(uint64_t *)(v_stack_mD0 + 0x30), *(uint64_t *)(v_stack_mF8 + 0xA8), Arg3, Arg4);
    local_r11 = 0;
    if (result != 0) goto loc_00976468;
loc_00976459:
    local_r12 = (uint32_t)((0) + 1);
    local_rdi = (v_stack_mD0 + 48) + (16);
    if (((uint32_t)(local_r12)) < 3) goto loc_00976441;
    goto loc_00976474;
loc_00976468:
    *(uint64_t *)(v_stack_mF8 + 0xB0) = *(uint64_t *)(v_stack_mF8 + 0xA8);
loc_00976474:
    if ((*(uint64_t *)(v_stack_mF8 + 0xB0)) != 0) goto loc_0097649E;
    result = (v_stack_mF8) | (-1);
loc_00976486:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_mF8 + 0xA8) + result * 2)) != 0) goto loc_00976486;
    local_r15 = (*(uint64_t *)(v_stack_mF8 + 0xA8) + result * 2) + (2);
    if ((*(uint16_t *)(local_r15)) != 0) goto loc_0097643A;
loc_0097649E:
loc_009764A2:
    local_rdi = v_stack_mF8;
    if ((*(uint64_t *)(v_stack_mF8 + 0xB0)) != 0) {
        local_rdi = v_stack_mF8;
    }
    if (((uint8_t)((uint32_t)(v_stack_mC4))) != 3) goto loc_009764E4;
    if ((*(uint64_t *)(v_stack_mA8)) != v_stack_mB0) goto loc_00976CE1;
    *(uint64_t *)(local_rdi + 0x8) = v_stack_mA8;
    *(uint64_t *)(local_rdi) = v_stack_mB0;
    *(uint64_t *)(v_stack_mA8) = local_rdi;
    v_stack_mA8 = local_rdi;
    goto loc_0097661C;
loc_009764E4:
    if (((*(uint32_t *)(local_rdi + 0xB8)) & (512)) == 0) goto loc_0097654E;
    if ((*(uint64_t *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(uint64_t *)(local_rdi + 0x8) = v_stack_mE0;
    *(uint64_t *)(local_rdi) = v_stack_mE8;
    *(uint64_t *)(v_stack_mE0) = local_rdi;
    v_stack_mE0 = local_rdi;
    if (v_stack_m90 == 0) goto loc_0097661C;
    result = PiDevCfgMatchDriverConfigurationId(v_stack_mF8, v_stack_m90, Arg3, Arg4);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_00976620;
    v_stack_mF0 = (uint32_t)((uint32_t)(0xC000036BULL));
    goto loc_00976624;
loc_0097654E:
    if (v_stack_m90 == 0) goto loc_0097659F;
    result = PiDevCfgMatchDriverConfigurationId((uint32_t)(0xC000036BULL), v_stack_m90, Arg3, Arg4);
    local_r11 = 0;
    if ((uint8_t)(result) != 0) goto loc_0097659A;
    if ((*(uint64_t *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(uint64_t *)(v_stack_mF8 + 0x8) = v_stack_mE0;
    *(uint64_t *)(v_stack_mF8) = v_stack_mE8;
    *(uint64_t *)(v_stack_mE0) = v_stack_mF8;
    v_stack_mE0 = v_stack_mF8;
    goto loc_0097661C;
loc_0097659A:
loc_0097659F:
    if ((*(uint64_t *)(v_stack_mF8 + 0xB0)) == 0) goto loc_009765D1;
loc_009765B2:
    if ((*(uint64_t *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(uint64_t *)(v_stack_mF8) = v_stack_mE8;
    *(uint64_t *)(v_stack_mF8 + 0x8) = v_stack_mE0;
    *(uint64_t *)(v_stack_mE0) = v_stack_mF8;
    v_stack_mE0 = v_stack_mF8;
    goto loc_0097661C;
loc_009765D1:
    if (0 != 0) goto loc_009765DB;
    goto loc_0097661C;
loc_009765DB:
    Arg3 = 0;
    result = PiDevCfgCompareDrivers(v_stack_mF8, v_stack_mF8, Arg3, Arg4);
    local_r11 = 0;
    if (!sign_flag) goto loc_009765B2;
    if ((*(uint64_t *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(uint64_t *)(v_stack_mF8 + 0x8) = v_stack_mE0;
    *(uint64_t *)(v_stack_mF8) = v_stack_mE8;
    *(uint64_t *)(v_stack_mE0) = v_stack_mF8;
    v_stack_mE0 = v_stack_mF8;
loc_0097661C:
loc_00976620:
loc_00976624:
    result = (v_stack_mE0) | (-1);
loc_00976628:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_mB8 + result * 2)) != 0) goto loc_00976628;
    local_r15 = (v_stack_mB8 + result * 2) + (2);
    if ((*(uint16_t *)(local_r15)) != 0) goto loc_009762A6;
    goto loc_0097664A;
loc_00976646:
loc_0097664A:
loc_0097664E:
    result = (result) | (-1);
loc_00976652:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m78 + result * 2)) != 0) goto loc_00976652;
    local_r13 = (v_stack_m78 + result * 2) + (2);
    local_r15 = (uint32_t)(((uint32_t)(v_stack_mD8)) + 1);
    v_stack_m78 = local_r13;
    v_stack_mD8 = (uint32_t)(local_r15);
    if ((*(uint16_t *)(local_r13)) != 0) goto loc_0097618C;
    goto loc_00976694;
loc_0097668D:
loc_00976694:
loc_0097669B:
    if (sign_flag) goto loc_00976C6C;
loc_009766A3:
    result = (uint32_t)(((uint32_t)(v_stack_mBC)) + 1);
    Arg1 = (v_stack_m80) + (16);
    v_stack_mBC = (uint32_t)(result);
    v_stack_m80 = Arg1;
    if (((uint32_t)(result)) < 3) goto loc_0097616A;
    if (sign_flag) goto loc_00976C6C;
    if (v_stack_m90 == 0) goto loc_009767A3;
    if (v_stack_mF8 != 0) goto loc_00976833;
    if (((uint32_t)((uint32_t)(v_stack_mF0))) == 0xC000036BULL) goto loc_009767AC;
    result = wcschr(v_stack_m90, v_stack_mF8 + 58, Arg3, Arg4);
    local_r11 = 0;
    if (result != 0) goto loc_00976704;
loc_009766FA:
    goto loc_00976C6C;
loc_00976704:
    *(uint16_t *)(result) = 0;
    result = wcschr(result + 2, 44, Arg3, Arg4);
    local_r11 = 0;
    if (result == 0) goto loc_009766FA;
    *(uint16_t *)(result) = 0;
    Arg4 = 0;
    v_stack_m128 = v_stack_mF8;
    Arg3 = 0;
    v_stack_m130 = v_stack_m60;
    v_stack_m138 = 4;
    result = PiDevCfgQueryDriverNode(v_stack_m90, result + 2, Arg3, Arg4);
    local_r11 = 0;
    if (sign_flag) goto loc_009767AC;
    if (((*(uint32_t *)(v_stack_mF8 + 0xB8)) & (512)) == 0) goto loc_0097679B;
    if ((*(uint64_t *)(v_stack_mE0)) != v_stack_mE8) goto loc_00976CE1;
    *(uint64_t *)(v_stack_mF8 + 0x8) = v_stack_mE0;
    *(uint64_t *)(v_stack_mF8) = v_stack_mE8;
    *(uint64_t *)(v_stack_mE0) = v_stack_mF8;
    v_stack_mE0 = v_stack_mF8;
    v_stack_mF8 = 0;
loc_0097679B:
    if (0 == 0) goto loc_009767AC;
loc_009767A3:
    if (0 != 0) goto loc_00976833;
loc_009767AC:
    if ((uint32_t)((uint32_t)(0xC000036BULL)) == 0) goto loc_009767BA;
    local_rsi = (uint32_t)((uint32_t)((uint32_t)(0xC000036BULL)));
    if (((uint32_t)((uint32_t)(0xC000036BULL))) == 0xC0000034ULL) {
        local_rsi = 0xC0000490ULL;
    }
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(0, v_stack_mE8, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00976C6C;
loc_009767D0:
    if (v_stack_mE8 == v_stack_mE8) goto loc_00976C6C;
    if ((*(uint64_t *)(v_stack_mE8 + 0x8)) != v_stack_mE8) goto loc_00976CE1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x8)) != v_stack_mE8) goto loc_00976CE1;
    v_stack_mE8 = *(uint64_t *)(v_stack_mE8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x8) = v_stack_mE8;
    v_stack_mF8 = v_stack_mE8;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18 + 0x8))) != (v_stack_mD0 + 24)) goto loc_00976CE1;
    *(uint64_t *)(v_stack_mE8) = v_stack_mD0 + 24;
    *(uint64_t *)(v_stack_mE8 + 0x8) = *(uint64_t *)(v_stack_mD0 + 0x18 + 0x8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18 + 0x8)) = v_stack_mE8;
    *(uint64_t *)(v_stack_mD0 + 0x18 + 0x8) = v_stack_mE8;
    goto loc_009767D0;
loc_00976833:
loc_00976837:
    if (v_stack_mE8 == v_stack_mE8) goto loc_009768FB;
    if ((*(uint64_t *)(v_stack_mE8 + 0x8)) != v_stack_mE8) goto loc_00976CE1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x8)) != v_stack_mE8) goto loc_00976CE1;
    v_stack_mE8 = *(uint64_t *)(v_stack_mE8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x8) = v_stack_mE8;
    v_stack_mF8 = v_stack_mE8;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_stack_mE8), v_stack_mE8, Arg3, Arg4);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) {
        Arg1 = v_stack_mD0 + 24;
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != Arg1) goto loc_00976CE1;
    *(void **)(v_stack_mF8) = Arg1;
    *(uint64_t *)(v_stack_mF8 + 0x8) = *(uint64_t *)(arg1 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) = v_stack_mF8;
    *(uint64_t *)(arg1 + 0x8) = v_stack_mF8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0xB8)))) & (4)) == 0) goto loc_00976837;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(0 + 0xB8)))) & (8)) != 0) goto loc_00976837;
    result = PiDevCfgCompareDrivers(v_stack_mF8, 0, 4, Arg4);
    local_r11 = 0;
    if (!sign_flag) goto loc_00976837;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0xB8))) | (8));
    *(uint32_t *)(0 + 0xB8) = (uint32_t)(local_rbx);
    goto loc_00976837;
loc_009768FB:
    if (v_stack_mB0 == v_stack_mB0) goto loc_00976C62;
    if ((*(uint64_t *)(v_stack_mB0 + 0x8)) != v_stack_mB0) goto loc_00976CE1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mB0) + 0x8)) != v_stack_mB0) goto loc_00976CE1;
    v_stack_mB0 = *(uint64_t *)(v_stack_mB0);
    *(uint64_t *)(*(uint64_t *)(v_stack_mB0) + 0x8) = v_stack_mB0;
    v_stack_mF8 = v_stack_mB0;
    Arg1 = (v_stack_mB0) + (188);
    result = PnpIsNullGuid(Arg1, v_stack_mB0, 4, Arg4);
    local_r11 = 0;
    if ((uint8_t)(result) != 0) goto loc_00976BFA;
    if ((*(uint64_t *)(v_stack_mF8 + 0xB0)) != 0) goto loc_00976BFA;
    if (*(uint64_t *)(v_stack_mF8 + 0x90) == 0) goto loc_00976A1D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x98))) == 0) goto loc_009769C9;
loc_00976986:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x98))) == 0) goto loc_009769C3;
    Arg3 = (0) + (0);
loc_0097699B:
    Arg4 = (0) << (4);
    Arg4 = (Arg4) + (*(uint64_t *)(v_stack_mF8 + 0x90));
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0x90) + Arg3 * 8)) != (*(uint64_t *)(Arg4))) goto loc_009769B9;
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0x90) + Arg3 * 8 + 0x8)) == (*(uint64_t *)(Arg4 + 0x8))) goto loc_00976A15;
loc_009769B9:
    Arg1 = (uint32_t)((0) + 1);
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x98))))) goto loc_0097699B;
    local_r11 = 0;
loc_009769C3:
    Arg2 = (uint32_t)((0) + 1);
    if (((uint32_t)(Arg2)) < ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x98))))) goto loc_00976986;
loc_009769C9:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00976AC2;
    *(uint32_t *)(v_stack_mF8 + 0x1C0) = 0xC00002B9ULL;
loc_009769E8:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18 + 0x8))) != (v_stack_mD0 + 24)) goto loc_00976CE1;
    *(uint64_t *)(v_stack_mF8) = v_stack_mD0 + 24;
    *(uint64_t *)(v_stack_mF8 + 0x8) = *(uint64_t *)(v_stack_mD0 + 0x18 + 0x8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18 + 0x8)) = v_stack_mF8;
    *(uint64_t *)(v_stack_mD0 + 0x18 + 0x8) = v_stack_mF8;
    goto loc_009768FB;
loc_00976A15:
    local_r11 = 0;
    if (Arg4 == 0) goto loc_009769C3;
loc_00976A1D:
    if (v_stack_m90 == 0) goto loc_00976AA6;
    if (v_stack_m70 == 0) goto loc_00976A86;
    if (((uint16_t)(*(uint16_t *)(v_stack_m70))) != 42) goto loc_00976A3F;
    if ((*(uint16_t *)(v_stack_m70 + 0x2)) == 0) goto loc_00976A81;
loc_00976A3F:
    if ((uint16_t)(*(uint16_t *)(v_stack_m70)) == 0) goto loc_00976A86;
loc_00976A47:
    result = PiDevCfgMatchDriverConfigurationId(v_stack_mF8, v_stack_m70, Arg3, Arg4);
    local_r11 = 0;
    if ((uint8_t)(result) != 0) goto loc_00976A7C;
    result = (result) | (-1);
loc_00976A5D:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m70 + result * 2)) != 0) goto loc_00976A5D;
    local_rdi = (v_stack_m70 + result * 2) + (2);
    if ((*(uint16_t *)(local_rdi)) == 0) goto loc_00976A86;
    goto loc_00976A47;
loc_00976A7C:
loc_00976A81:
    if (v_stack_mF8 != 0) goto loc_00976AA6;
loc_00976A86:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(v_stack_mF8, v_stack_m70, Arg3, Arg4);
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00976AC2;
    *(uint32_t *)(v_stack_mF8 + 0x1C0) = 0xC0000719ULL;
    goto loc_009769E8;
loc_00976AA6:
    if (((*(uint32_t *)(v_stack_mF8 + 0xB8)) & (512)) == 0) goto loc_00976AD5;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(v_stack_mF8, v_stack_m70, Arg3, Arg4);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_009769E8;
loc_00976AC2:
    result = PiDevCfgFreeDriverNode(v_stack_mF8, v_stack_m70, Arg3, Arg4);
    goto loc_00976C5A;
loc_00976AD5:
    goto loc_00976B04;
loc_00976AE1:
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0xD0) + 0xBC)) != (*(uint64_t *)(v_stack_mF8 + 0xBC))) goto loc_00976B01;
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0xD0) + 0xC4)) == (*(uint64_t *)(v_stack_mF8 + 0xC4))) goto loc_00976B3D;
loc_00976B01:
loc_00976B04:
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0xD0))) != (0 + 208)) goto loc_00976AE1;
loc_00976B09:
loc_00976B0D:
    if (v_stack_mF8 == 0) goto loc_009768FB;
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0xD0 + 0x8))) != (0 + 208)) goto loc_00976CE1;
    *(uint64_t *)(v_stack_mF8) = 0 + 208;
    *(uint64_t *)(v_stack_mF8 + 0x8) = *(uint64_t *)(0 + 0xD0 + 0x8);
    *(uint64_t *)(*(uint64_t *)(0 + 0xD0 + 0x8)) = v_stack_mF8;
    *(uint64_t *)(0 + 0xD0 + 0x8) = v_stack_mF8;
    goto loc_009768FB;
loc_00976B3D:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(0 + 0xD0)) + 0x90)) == 0) goto loc_00976B7D;
    if ((*(uint64_t *)(v_stack_mF8 + 0x90)) != 0) goto loc_00976B86;
loc_00976B4F:
    v_stack_mF8 = 0;
loc_00976B5A:
    if (v_stack_mF8 == 0) goto loc_00976B09;
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(0 + 0xD0 + 0x8), v_stack_m70, Arg3, Arg4);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00976BC3;
    result = PiDevCfgFreeDriverNode(v_stack_mF8, v_stack_m70, Arg3, Arg4);
    local_r11 = 0;
    goto loc_00976B09;
loc_00976B7D:
    if ((*(uint64_t *)(v_stack_mF8 + 0x90)) != 0) goto loc_00976B9B;
loc_00976B86:
    Arg3 = 0;
    result = PiDevCfgCompareDrivers(v_stack_mF8, v_stack_mF8, Arg3, Arg4);
    local_r11 = 0;
    if (!sign_flag) goto loc_00976B4F;
loc_00976B9B:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF8) + 0x8)) != v_stack_mF8) goto loc_00976CE1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF8 + 0x8))) != v_stack_mF8) goto loc_00976CE1;
    *(uint64_t *)(*(uint64_t *)(v_stack_mF8 + 0x8)) = *(uint64_t *)(v_stack_mF8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mF8) + 0x8) = *(uint64_t *)(v_stack_mF8 + 0x8);
    goto loc_00976B5A;
loc_00976BC3:
    *(uint32_t *)(v_stack_mF8 + 0x1C0) = 0xC0000272ULL;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18 + 0x8))) != (v_stack_mD0 + 24)) goto loc_00976CE1;
    *(uint64_t *)(v_stack_mF8) = v_stack_mD0 + 24;
    *(uint64_t *)(v_stack_mF8 + 0x8) = *(uint64_t *)(v_stack_mD0 + 0x18 + 0x8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18 + 0x8)) = v_stack_mF8;
    *(uint64_t *)(v_stack_mD0 + 0x18 + 0x8) = v_stack_mF8;
    goto loc_00976B0D;
loc_00976BFA:
    result = Feature_KernelPnP_LogBlockedDrivers__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_stack_mD0 + 0x18 + 0x8), v_stack_mF8, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00976C0F;
    result = PiDevCfgFreeDriverNode(v_stack_mF8, v_stack_mF8, Arg3, Arg4);
    goto loc_00976C5A;
loc_00976C0F:
    Arg1 = (v_stack_mF8) + (188);
    result = PnpIsNullGuid(Arg1, v_stack_mF8, Arg3, Arg4);
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFF52ULL));
    Arg1 = (uint32_t)((Arg1) + (0xC00000BBULL));
    *(uint32_t *)(v_stack_mF8 + 0x1C0) = (uint32_t)(Arg1);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18 + 0x8))) != (v_stack_mD0 + 24)) goto loc_00976CE1;
    *(uint64_t *)(v_stack_mF8) = v_stack_mD0 + 24;
    *(uint64_t *)(v_stack_mF8 + 0x8) = *(uint64_t *)(v_stack_mD0 + 0x18 + 0x8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18 + 0x8)) = v_stack_mF8;
    *(uint64_t *)(v_stack_mD0 + 0x18 + 0x8) = v_stack_mF8;
loc_00976C5A:
    local_r11 = 0;
    goto loc_009768FB;
loc_00976C62:
    *(uint64_t *)(v_stack_m68) = 0;
loc_00976C6C:
    if (v_stack_mE8 == v_stack_mE8) goto loc_00976CA9;
    if ((*(uint64_t *)(v_stack_mE8 + 0x8)) != v_stack_mE8) goto loc_00976CE1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x8)) != v_stack_mE8) goto loc_00976CE1;
    v_stack_mE8 = *(uint64_t *)(v_stack_mE8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mE8) + 0x8) = v_stack_mE8;
    v_stack_mF8 = v_stack_mE8;
    result = PiDevCfgFreeDriverNode(v_stack_mE8, v_stack_mE8, Arg3, Arg4);
    goto loc_00976C6C;
loc_00976CA9:
    if (v_stack_mB0 == v_stack_mB0) goto loc_00976CE8;
    if ((*(uint64_t *)(v_stack_mB0 + 0x8)) != v_stack_mB0) goto loc_00976CE1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mB0) + 0x8)) != v_stack_mB0) goto loc_00976CE1;
    v_stack_mB0 = *(uint64_t *)(v_stack_mB0);
    *(uint64_t *)(*(uint64_t *)(v_stack_mB0) + 0x8) = v_stack_mB0;
    v_stack_mF8 = v_stack_mB0;
    result = PiDevCfgFreeDriverNode(v_stack_mB0, v_stack_mB0, Arg3, Arg4);
    goto loc_00976CA9;
loc_00976CE1:
loc_00976CE8:
    if (0 != 0) {
        Arg1 = 0;
        result = PiDevCfgFreeDriverNode(Arg1, v_stack_mB0, Arg3, Arg4);
    }
    if (v_stack_m98 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m98;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (288);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097602C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
