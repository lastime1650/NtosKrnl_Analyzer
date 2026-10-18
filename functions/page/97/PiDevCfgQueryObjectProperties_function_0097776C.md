# PiDevCfgQueryObjectProperties

- RVA: `0x0097776C`–`0x00977BAB` (길이 `1,087` bytes)
- VA: `0x000000014097776C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00096748`
- 디코드: `277`개 명령, `1,087/1,087` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009777D5` → [PnpOpenObjectRegKey](../8E/PnpOpenObjectRegKey_function_008E15E8.md) (function, `0x008E15E8`)
- `0x0097789E` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00977946` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0097796B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009779F1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00977A20` → [PnpValidateMultiSzData](../../text/4B/PnpValidateMultiSzData_function_004BD294.md) (function, `0x004BD294`)
- `0x00977A68` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00977A90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00977AA7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00977AC6` → [PnpValidateStringData](../../text/4B/PnpValidateStringData_function_004B7678.md) (function, `0x004B7678`)
- `0x00977B4A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00977B61` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00977B8C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00977BA1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [PiDevCfgCheckDeviceNeedsUpdate](../73/PiDevCfgCheckDeviceNeedsUpdate_function_00731DDC.md) at `0x00731F9D`
- [PiDevCfgCheckDeviceNeedsUpdate](../73/PiDevCfgCheckDeviceNeedsUpdate_function_00731DDC.md) at `0x0073206B`
- [PiDevCfgFindDeviceMigrationNode](../73/PiDevCfgFindDeviceMigrationNode_function_00732920.md) at `0x00732D67`
- [PiDevCfgFindDeviceMigrationNode](../73/PiDevCfgFindDeviceMigrationNode_function_00732920.md) at `0x00732E63`
- [PiDevCfgFindDeviceMigrationNode](../73/PiDevCfgFindDeviceMigrationNode_function_00732920.md) at `0x00732FA3`
- [PiDevCfgGetDeviceClassDriverConfigurable](../73/PiDevCfgGetDeviceClassDriverConfigurable_function_00733504.md) at `0x00733638`
- [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) at `0x007344C0`
- [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) at `0x00734759`
- [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) at `0x0073485E`
- [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) at `0x00734943`
- [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) at `0x00734C38`
- [PpDevCfgProcessDeviceClass](../73/PpDevCfgProcessDeviceClass_function_00736824.md) at `0x0073693B`
- [PpDevCfgProcessDeviceClass](../73/PpDevCfgProcessDeviceClass_function_00736824.md) at `0x00736A07`
- [PpDevCfgProcessDeviceExtensions](../73/PpDevCfgProcessDeviceExtensions_function_00736C2C.md) at `0x00736D80`
- [PpDevCfgProcessDeviceExtensions](../73/PpDevCfgProcessDeviceExtensions_function_00736C2C.md) at `0x0073703B`
- [PpDevCfgProcessDeviceReset](../96/PpDevCfgProcessDeviceReset_function_00965498.md) at `0x0096558B`
- [PiDevCfgQueryDriverConfiguration](PiDevCfgQueryDriverConfiguration_function_0097584C.md) at `0x00975D39`
- [PiDevCfgProcessDevice](PiDevCfgProcessDevice_function_00976D34.md) at `0x0097721A`
- [PiDevCfgInitDeviceContext](PiDevCfgInitDeviceContext_function_00977518.md) at `0x00977621`
- [PiDevCfgGetDriverPackageId](PiDevCfgGetDriverPackageId_function_00977690.md) at `0x00977728`
- [PiDevCfgConfigureDevice](PiDevCfgConfigureDevice_function_00977BB4.md) at `0x009784B5`
- [PiDevCfgConfigureDevice](PiDevCfgConfigureDevice_function_00977BB4.md) at `0x0097868C`
- [PiDevCfgConfigureDevice](PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00978753`
- [PiDevCfgConfigureDevice](PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00979040`
- [PiDevCfgLogDeviceStarted](../AB/PiDevCfgLogDeviceStarted_function_00ABEC8C.md) at `0x00ABEDB6`
- [PiDevCfgLogDeviceConfigured](../AD/PiDevCfgLogDeviceConfigured_function_00ADCDD4.md) at `0x00ADCFA5`
- [PiDevCfgLogDeviceConfigured](../AD/PiDevCfgLogDeviceConfigured_function_00ADCDD4.md) at `0x00ADDA3B`
- [PiDevCfgLogDeviceConfigured](../AD/PiDevCfgLogDeviceConfigured_function_00ADCDD4.md) at `0x00ADDEC1`
- [PpDevCfgInit](../../init/C3/PpDevCfgInit_function_00C351A4.md) at `0x00C35292`

### Static image references
- `0x00977796` → RVA `0x00E66398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00977946` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0097796B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009779F1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00977A20` → [PnpValidateMultiSzData](../../text/4B/PnpValidateMultiSzData_function_004BD294.md) (`PAGE` → `.text`)
  - `0x00977A68` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00977A90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00977AA7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00977AC6` → [PnpValidateStringData](../../text/4B/PnpValidateStringData_function_004B7678.md) (`PAGE` → `.text`)
  - `0x00977B4A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00977B61` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00977B8C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00977BA1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00977B81` → [sub_00B29CDC](../B2/Unknown_function_00B29CDC.md) (`tail-transfer`)
  - `0x00977B92` → [sub_00B29CDC + 0x16](../B2/Unknown_function_00B29CDC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0097776C  48 8B C4                        mov rax, rsp
0097776F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00977773  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00977777  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0097777B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0097777F  55                              push rbp
00977780  53                              push rbx
00977781  56                              push rsi
00977782  57                              push rdi
00977783  41 54                           push r12
00977785  41 55                           push r13
00977787  41 56                           push r14
00977789  41 57                           push r15
0097778B  48 8D 68 B1                     lea rbp, [rax - 0x4f]
0097778F  48 81 EC 98 00 00 00            sub rsp, 0x98
00977796  48 8B 0D FB EB 4E 00            mov rcx, qword ptr [rip + 0x4eebfb]
0097779D  45 33 D2                        xor r10d, r10d
009777A0  48 89 4D EF                     mov qword ptr [rbp - 0x11], rcx
009777A4  41 8B DA                        mov ebx, r10d
009777A7  4C 89 55 E7                     mov qword ptr [rbp - 0x19], r10
009777AB  41 8B FA                        mov edi, r10d
009777AE  C7 45 DB 01 00 00 00            mov dword ptr [rbp - 0x25], 1
009777B5  45 8B E2                        mov r12d, r10d
009777B8  44 89 55 D7                     mov dword ptr [rbp - 0x29], r10d
009777BC  4D 85 C9                        test r9, r9
009777BF  75 46                           jne 0x140977807
009777C1  48 8D 45 E7                     lea rax, [rbp - 0x19]
009777C5  41 B9 01 00 00 02               mov r9d, 0x2000001
009777CB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009777D0  44 88 54 24 20                  mov byte ptr [rsp + 0x20], r10b
009777D5  E8 0E 9E F6 FF                  call 0x1408e15e8
009777DA  45 33 D2                        xor r10d, r10d
009777DD  8B D8                           mov ebx, eax
009777DF  85 C0                           test eax, eax
009777E1  79 24                           jns 0x140977807
009777E3  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
009777E7  48 85 C9                        test rcx, rcx
009777EA  0F 85 B1 03 00 00               jne 0x140977ba1
009777F0  8B C3                           mov eax, ebx
009777F2  48 81 C4 98 00 00 00            add rsp, 0x98
009777F9  41 5F                           pop r15
009777FB  41 5E                           pop r14
009777FD  41 5D                           pop r13
009777FF  41 5C                           pop r12
00977801  5F                              pop rdi
00977802  5E                              pop rsi
00977803  5B                              pop rbx
00977804  5D                              pop rbp
00977805  C3                              ret
00977806  CC                              int3
00977807  4C 8B 7D 77                     mov r15, qword ptr [rbp + 0x77]
0097780B  41 8B C2                        mov eax, r10d
0097780E  89 45 DF                        mov dword ptr [rbp - 0x21], eax
00977811  3B 45 7F                        cmp eax, dword ptr [rbp + 0x7f]
00977814  0F 83 40 02 00 00               jae 0x140977a5a
0097781A  4C 8D 34 80                     lea r14, [rax + rax*4]
0097781E  43 8B 44 F7 1C                  mov eax, dword ptr [r15 + r14*8 + 0x1c]
00977823  4B 8B 74 F7 10                  mov rsi, qword ptr [r15 + r14*8 + 0x10]
00977828  A8 04                           test al, 4
0097782A  0F 84 90 01 00 00               je 0x1409779c0
00977830  4C 8B EE                        mov r13, rsi
00977833  48 8B 76 08                     mov rsi, qword ptr [rsi + 8]
00977837  41 0F B7 4D 02                  movzx ecx, word ptr [r13 + 2]
0097783C  89 4D 57                        mov dword ptr [rbp + 0x57], ecx
0097783F  A8 02                           test al, 2
00977841  74 12                           je 0x140977855
00977843  48 85 FF                        test rdi, rdi
00977846  0F 84 94 01 00 00               je 0x1409779e0
0097784C  48 8B F7                        mov rsi, rdi
0097784F  41 8B CC                        mov ecx, r12d
00977852  89 4D 57                        mov dword ptr [rbp + 0x57], ecx
00977855  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00977859  4C 8B 4D E7                     mov r9, qword ptr [rbp - 0x19]
0097785D  48 85 C0                        test rax, rax
00977860  44 8B 45 67                     mov r8d, dword ptr [rbp + 0x67]
00977864  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
00977868  4C 0F 45 C8                     cmovne r9, rax
0097786C  44 89 54 24 50                  mov dword ptr [rsp + 0x50], r10d
00977871  48 8D 45 D7                     lea rax, [rbp - 0x29]
00977875  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0097787A  48 8D 45 DB                     lea rax, [rbp - 0x25]
0097787E  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00977882  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
00977886  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0097788B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00977890  4B 8B 04 F7                     mov rax, qword ptr [r15 + r14*8]
00977894  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00977899  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
0097789E  E8 DD A8 F6 FF                  call 0x1408e2180
009778A3  8B D8                           mov ebx, eax
009778A5  8B C8                           mov ecx, eax
009778A7  3D 23 00 00 C0                  cmp eax, 0xc0000023
009778AC  0F 84 C0 01 00 00               je 0x140977a72
009778B2  4C 8B CF                        mov r9, rdi
009778B5  3D 9A 00 00 C0                  cmp eax, 0xc000009a
009778BA  0F 84 9A 01 00 00               je 0x140977a5a
009778C0  45 33 DB                        xor r11d, r11d
009778C3  45 8B D4                        mov r10d, r12d
009778C6  85 C0                           test eax, eax
009778C8  0F 88 C1 00 00 00               js 0x14097798f
009778CE  8B 45 DB                        mov eax, dword ptr [rbp - 0x25]
009778D1  8B 55 D7                        mov edx, dword ptr [rbp - 0x29]
009778D4  85 C0                           test eax, eax
009778D6  0F 84 3B 02 00 00               je 0x140977b17
009778DC  47 8B 44 F7 08                  mov r8d, dword ptr [r15 + r14*8 + 8]
009778E1  41 3B C0                        cmp eax, r8d
009778E4  0F 85 41 02 00 00               jne 0x140977b2b
009778EA  41 83 F8 12                     cmp r8d, 0x12
009778EE  0F 84 1B 01 00 00               je 0x140977a0f
009778F4  83 F8 14                        cmp eax, 0x14
009778F7  0F 84 C6 01 00 00               je 0x140977ac3
009778FD  83 F8 12                        cmp eax, 0x12
00977900  0F 84 BD 01 00 00               je 0x140977ac3
00977906  83 F8 19                        cmp eax, 0x19
00977909  0F 84 B4 01 00 00               je 0x140977ac3
0097790F  3D 12 20 00 00                  cmp eax, 0x2012
00977914  0F 84 03 01 00 00               je 0x140977a1d
0097791A  49 8B F9                        mov rdi, r9
0097791D  45 8B E2                        mov r12d, r10d
00977920  4D 85 ED                        test r13, r13
00977923  0F 85 A4 00 00 00               jne 0x1409779cd
00977929  43 8B 44 F7 1C                  mov eax, dword ptr [r15 + r14*8 + 0x1c]
0097792E  A8 02                           test al, 2
00977930  74 46                           je 0x140977978
00977932  B9 00 01 00 00                  mov ecx, 0x100
00977937  4D 85 ED                        test r13, r13
0097793A  0F 84 04 02 00 00               je 0x140977b44
00977940  41 B8 53 74 72 67               mov r8d, 0x67727453
00977946  E8 A5 A7 20 00                  call 0x140b820f0
0097794B  49 89 45 08                     mov qword ptr [r13 + 8], rax
0097794F  48 85 C0                        test rax, rax
00977952  0F 84 3F 02 00 00               je 0x140977b97
00977958  0F B7 4D D7                     movzx ecx, word ptr [rbp - 0x29]
0097795C  48 8B D7                        mov rdx, rdi
0097795F  66 41 89 4D 02                  mov word ptr [r13 + 2], cx
00977964  48 8B C8                        mov rcx, rax
00977967  44 8B 45 D7                     mov r8d, dword ptr [rbp - 0x29]
0097796B  E8 D0 EE D4 FF                  call 0x1406c6840
00977970  8B 55 D7                        mov edx, dword ptr [rbp - 0x29]
00977973  45 33 DB                        xor r11d, r11d
00977976  EB 05                           jmp 0x14097797d
00977978  4D 85 ED                        test r13, r13
0097797B  74 2F                           je 0x1409779ac
0097797D  66 41 89 55 00                  mov word ptr [r13], dx
00977982  81 7D DB 12 20 00 00            cmp dword ptr [rbp - 0x25], 0x2012
00977989  0F 85 4E 01 00 00               jne 0x140977add
0097798F  8B 4D 57                        mov ecx, dword ptr [rbp + 0x57]
00977992  45 33 D2                        xor r10d, r10d
00977995  43 89 5C F7 20                  mov dword ptr [r15 + r14*8 + 0x20], ebx
0097799A  85 DB                           test ebx, ebx
0097799C  0F 88 9A 00 00 00               js 0x140977a3c
009779A2  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
009779A5  FF C0                           inc eax
009779A7  E9 62 FE FF FF                  jmp 0x14097780e
009779AC  43 8B 44 F7 1C                  mov eax, dword ptr [r15 + r14*8 + 0x1c]
009779B1  A8 02                           test al, 2
009779B3  0F 85 B5 01 00 00               jne 0x140977b6e
009779B9  43 89 54 F7 18                  mov dword ptr [r15 + r14*8 + 0x18], edx
009779BE  EB CF                           jmp 0x14097798f
009779C0  43 8B 4C F7 18                  mov ecx, dword ptr [r15 + r14*8 + 0x18]
009779C5  4D 8B EA                        mov r13, r10
009779C8  E9 6F FE FF FF                  jmp 0x14097783c
009779CD  81 FA FE FF 00 00               cmp edx, 0xfffe
009779D3  0F 86 50 FF FF FF               jbe 0x140977929
009779D9  BB 05 00 00 80                  mov ebx, 0x80000005
009779DE  EB AF                           jmp 0x14097798f
009779E0  BA 04 01 00 00                  mov edx, 0x104
009779E5  41 B8 50 70 64 63               mov r8d, 0x63647050
009779EB  44 8B E2                        mov r12d, edx
009779EE  8D 4A FC                        lea ecx, [rdx - 4]
009779F1  E8 FA A6 20 00                  call 0x140b820f0
009779F6  45 33 D2                        xor r10d, r10d
009779F9  48 8B F8                        mov rdi, rax
009779FC  48 85 C0                        test rax, rax
009779FF  0F 85 47 FE FF FF               jne 0x14097784c
00977A05  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00977A0A  E9 D4 FD FF FF                  jmp 0x1409777e3
00977A0F  83 F8 19                        cmp eax, 0x19
00977A12  0F 85 DC FE FF FF               jne 0x1409778f4
00977A18  E9 19 01 00 00                  jmp 0x140977b36
00977A1D  48 8B CE                        mov rcx, rsi
00977A20  E8 6F 58 B4 FF                  call 0x1404bd294
00977A25  84 C0                           test al, al
00977A27  B8 01 00 00 C0                  mov eax, 0xc0000001
00977A2C  0F 44 D8                        cmove ebx, eax
00977A2F  85 DB                           test ebx, ebx
00977A31  0F 88 58 FF FF FF               js 0x14097798f
00977A37  E9 DE FE FF FF                  jmp 0x14097791a
00977A3C  43 8B 44 F7 1C                  mov eax, dword ptr [r15 + r14*8 + 0x1c]
00977A41  A8 08                           test al, 8
00977A43  0F 85 35 01 00 00               jne 0x140977b7e
00977A49  43 8B 44 F7 1C                  mov eax, dword ptr [r15 + r14*8 + 0x1c]
00977A4E  A8 01                           test al, 1
00977A50  75 08                           jne 0x140977a5a
00977A52  41 8B DA                        mov ebx, r10d
00977A55  E9 48 FF FF FF                  jmp 0x1409779a2
00977A5A  48 85 FF                        test rdi, rdi
00977A5D  0F 84 80 FD FF FF               je 0x1409777e3
00977A63  33 D2                           xor edx, edx
00977A65  48 8B CF                        mov rcx, rdi
00977A68  E8 03 AE 20 00                  call 0x140b82870
00977A6D  E9 71 FD FF FF                  jmp 0x1409777e3
00977A72  43 8B 44 F7 1C                  mov eax, dword ptr [r15 + r14*8 + 0x1c]
00977A77  8B 4D 57                        mov ecx, dword ptr [rbp + 0x57]
00977A7A  A8 02                           test al, 2
00977A7C  0F 84 10 FF FF FF               je 0x140977992
00977A82  39 4D D7                        cmp dword ptr [rbp - 0x29], ecx
00977A85  0F 86 96 00 00 00               jbe 0x140977b21
00977A8B  33 D2                           xor edx, edx
00977A8D  48 8B CF                        mov rcx, rdi
00977A90  E8 DB AD 20 00                  call 0x140b82870
00977A95  44 8B 65 D7                     mov r12d, dword ptr [rbp - 0x29]
00977A99  B9 00 01 00 00                  mov ecx, 0x100
00977A9E  41 8B D4                        mov edx, r12d
00977AA1  41 B8 50 70 64 63               mov r8d, 0x63647050
00977AA7  E8 44 A6 20 00                  call 0x140b820f0
00977AAC  45 33 D2                        xor r10d, r10d
00977AAF  48 8B F8                        mov rdi, rax
00977AB2  48 85 C0                        test rax, rax
00977AB5  0F 84 4A FF FF FF               je 0x140977a05
00977ABB  48 8B F0                        mov rsi, rax
00977ABE  E9 8C FD FF FF                  jmp 0x14097784f
00977AC3  48 8B CE                        mov rcx, rsi
00977AC6  E8 AD FB B3 FF                  call 0x1404b7678
00977ACB  84 C0                           test al, al
00977ACD  0F 85 47 FE FF FF               jne 0x14097791a
00977AD3  BB 01 00 00 C0                  mov ebx, 0xc0000001
00977AD8  E9 B2 FE FF FF                  jmp 0x14097798f
00977ADD  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
00977AE1  48 85 D2                        test rdx, rdx
00977AE4  0F 84 A5 FE FF FF               je 0x14097798f
00977AEA  8B 4D D7                        mov ecx, dword ptr [rbp - 0x29]
00977AED  66 83 F9 02                     cmp cx, 2
00977AF1  0F 82 98 FE FF FF               jb 0x14097798f
00977AF7  0F B7 C1                        movzx eax, cx
00977AFA  48 D1 E8                        shr rax, 1
00977AFD  66 44 39 5C 42 FE               cmp word ptr [rdx + rax*2 - 2], r11w
00977B03  0F 85 86 FE FF FF               jne 0x14097798f
00977B09  66 83 E9 02                     sub cx, 2
00977B0D  66 41 89 4D 00                  mov word ptr [r13], cx
00977B12  E9 78 FE FF FF                  jmp 0x14097798f
00977B17  47 89 5C F7 08                  mov dword ptr [r15 + r14*8 + 8], r11d
00977B1C  E9 F9 FD FF FF                  jmp 0x14097791a
00977B21  BB E5 00 00 C0                  mov ebx, 0xc00000e5
00977B26  E9 67 FE FF FF                  jmp 0x140977992
00977B2B  41 83 F8 12                     cmp r8d, 0x12
00977B2F  75 A2                           jne 0x140977ad3
00977B31  83 F8 19                        cmp eax, 0x19
00977B34  75 9D                           jne 0x140977ad3
00977B36  43 C7 44 F7 08 19 00 00 00      mov dword ptr [r15 + r14*8 + 8], 0x19
00977B3F  E9 B0 FD FF FF                  jmp 0x1409778f4
00977B44  41 B8 50 70 64 63               mov r8d, 0x63647050
00977B4A  E8 A1 A5 20 00                  call 0x140b820f0
00977B4F  48 8B F0                        mov rsi, rax
00977B52  48 85 C0                        test rax, rax
00977B55  74 40                           je 0x140977b97
00977B57  44 8B 45 D7                     mov r8d, dword ptr [rbp - 0x29]
00977B5B  48 8B D7                        mov rdx, rdi
00977B5E  48 8B C8                        mov rcx, rax
00977B61  E8 DA EC D4 FF                  call 0x1406c6840
00977B66  8B 55 D7                        mov edx, dword ptr [rbp - 0x29]
00977B69  E9 3E FE FF FF                  jmp 0x1409779ac
00977B6E  4B 8B 44 F7 10                  mov rax, qword ptr [r15 + r14*8 + 0x10]
00977B73  48 89 30                        mov qword ptr [rax], rsi
00977B76  8B 55 D7                        mov edx, dword ptr [rbp - 0x29]
00977B79  E9 3B FE FF FF                  jmp 0x1409779b9
00977B7E  4D 85 ED                        test r13, r13
00977B81  0F 84 55 21 1B 00               je 0x140b29cdc
00977B87  33 D2                           xor edx, edx
00977B89  49 8B CD                        mov rcx, r13
00977B8C  E8 EF 2B AB FF                  call 0x14042a780
00977B91  90                              nop
00977B92  E9 5B 21 1B 00                  jmp 0x140b29cf2
00977B97  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00977B9C  E9 B9 FE FF FF                  jmp 0x140977a5a
00977BA1  E8 0A 57 D3 FF                  call 0x1406ad2b0
00977BA6  E9 45 FC FF FF                  jmp 0x1409777f0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgQueryObjectProperties(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_mB0;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (152);
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 17) = *(unsigned __int64 *)(v_rip + 5172219);
    *(unsigned __int64 *)(v_rsp - 79 - 25) = 0;
    *(unsigned int *)(v_rsp - 79 - 37) = 1;
    *(unsigned int *)(v_rsp - 79 - 41) = 0;
    if (a4 != 0) goto loc_00977807;
    v_stack_mB0 = v_rsp - 79 - 25;
    v_stack_mB8 = 0;
    result = PnpOpenObjectRegKey(*(unsigned __int64 *)(v_rip + 5172219), a2, a3, (unsigned int)(0x2000001ULL));
    v_r10 = 0;
    if (!sign_flag) goto loc_00977807;
loc_009777E3:
    if (*(unsigned __int64 *)(v_rsp - 79 - 25) != 0) goto loc_00977BA1;
loc_009777F0:
    v_rsp = (v_rsp) + (152);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00977807:
loc_0097780E:
    *(unsigned int *)(v_rsp - 79 - 33) = 0;
    if (0 >= (*(unsigned int *)(v_rsp - 79 + 127))) goto loc_00977A5A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 28)))) & (4)) == 0) goto loc_009779C0;
loc_0097783C:
    *(unsigned int *)(v_rsp - 79 + 87) = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 16) + 2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 28)))) & (2)) == 0) goto loc_00977855;
    if (0 == 0) goto loc_009779E0;
loc_0097784C:
loc_0097784F:
    *(unsigned int *)(v_rsp - 79 + 87) = 0;
loc_00977855:
    a4 = *(unsigned __int64 *)(v_rsp - 79 - 25);
    if (*(unsigned __int64 *)(v_rsp - 79 + 111) != 0) { a4 = *(unsigned __int64 *)(v_rsp - 79 + 111); }
    v_stack_p50 = 0;
    v_stack_p48 = v_rsp - 79 - 41;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = v_rsp - 79 - 37;
    v_stack_p28 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8);
    v_stack_p20 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rsp - 79 - 17), *(unsigned __int64 *)(v_rsp - 79 + 95), (unsigned int)(*(unsigned int *)(v_rsp - 79 + 103)), a4);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00977A72;
    if (((unsigned int)(result)) == 0xC000009AULL) goto loc_00977A5A;
    v_r11 = 0;
    if (sign_flag) goto loc_0097798F;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 37))) == 0) goto loc_00977B17;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 37)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 8))))) goto loc_00977B2B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 8)))) == 18) goto loc_00977A0F;
loc_009778F4:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 37)))) == 20) goto loc_00977AC3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 37)))) == 18) goto loc_00977AC3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 37)))) == 25) goto loc_00977AC3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 37)))) == 0x2012ULL) goto loc_00977A1D;
loc_0097791A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 16) != 0) goto loc_009779CD;
loc_00977929:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 28)))) & (2)) == 0) goto loc_00977978;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 16) == 0) goto loc_00977B44;
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)), (unsigned int)(0x67727453ULL), 0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 16) + 8) = result;
    if (result == 0) goto loc_00977B97;
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 16) + 2) = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 79 - 41));
    result = memcpy(result, 0, (unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)), 0);
    v_r11 = 0;
    goto loc_0097797D;
loc_00977978:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 16) == 0) goto loc_009779AC;
loc_0097797D:
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 16)) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)));
    if ((*(unsigned int *)(v_rsp - 79 - 37)) != 0x2012ULL) goto loc_00977ADD;
loc_0097798F:
loc_00977992:
    v_r10 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 32) = (unsigned int)((unsigned int)((unsigned int)(result)));
    if (sign_flag) goto loc_00977A3C;
loc_009779A2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 79 - 33))) + 1);
    goto loc_0097780E;
loc_009779AC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 28)))) & (2)) != 0) goto loc_00977B6E;
loc_009779B9:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)));
    goto loc_0097798F;
loc_009779C0:
    goto loc_0097783C;
loc_009779CD:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)))) <= 0xFFFEULL) goto loc_00977929;
    goto loc_0097798F;
loc_009779E0:
    result = ExAllocatePool2(260 - 4, 260, (unsigned int)(0x63647050ULL), 0);
    v_r10 = 0;
    if (result != 0) goto loc_0097784C;
loc_00977A05:
    goto loc_009777E3;
loc_00977A0F:
    if (((unsigned int)(result)) != 25) goto loc_009778F4;
    goto loc_00977B36;
loc_00977A1D:
    result = PnpValidateMultiSzData(0, 260, (unsigned int)(0x63647050ULL), 0);
    v_rbx = (unsigned int)(0xC000009AULL);
    if ((unsigned __int8)(result) == 0) { v_rbx = (unsigned int)((unsigned int)(0xC0000001ULL)); }
    if (sign_flag) goto loc_0097798F;
    goto loc_0097791A;
loc_00977A3C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 28)))) & (8)) != 0) goto loc_00977B7E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 28)))) & (1)) != 0) goto loc_00977A5A;
    goto loc_009779A2;
loc_00977A5A:
    if (result == 0) goto loc_009777E3;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x63647050ULL), 0);
    goto loc_009777E3;
loc_00977A72:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 28)))) & (2)) == 0) goto loc_00977992;
    if ((*(unsigned int *)(v_rsp - 79 - 41)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87))))) goto loc_00977B21;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x63647050ULL), 0);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)))), (unsigned int)(0x63647050ULL), 0);
    v_r10 = 0;
    if (result == 0) goto loc_00977A05;
    goto loc_0097784F;
loc_00977AC3:
    result = PnpValidateStringData(result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)))), (unsigned int)(0x63647050ULL), 0);
    if ((unsigned __int8)(result) != 0) goto loc_0097791A;
loc_00977AD3:
    goto loc_0097798F;
loc_00977ADD:
    if (*(unsigned __int64 *)(0 + 8) == 0) goto loc_0097798F;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)))) < 2) goto loc_0097798F;
    result = ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)))) >> (1);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(0 + 8) + result * 2 - 2)) != 0) goto loc_0097798F;
    a1 = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_rsp - 79 - 41))) - (2));
    *(unsigned __int16 *)(0) = (unsigned __int16)(a1);
    goto loc_0097798F;
loc_00977B17:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 8) = 0;
    goto loc_0097791A;
loc_00977B21:
    goto loc_00977992;
loc_00977B2B:
    if (((unsigned int)((unsigned int)(0x63647050ULL))) != 18) goto loc_00977AD3;
    if (((unsigned int)(result)) != 25) goto loc_00977AD3;
loc_00977B36:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 8) = 25;
    goto loc_009778F4;
loc_00977B44:
    result = ExAllocatePool2(a1, *(unsigned __int64 *)(0 + 8), (unsigned int)(0x63647050ULL), 0);
    if (result == 0) goto loc_00977B97;
    result = memcpy(result, result, (unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)), 0);
    goto loc_009779AC;
loc_00977B6E:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119) + 0 + 0 * 4 * 8 + 16)) = result;
    goto loc_009779B9;
loc_00977B7E:
    a2 = 0;
    result = RtlInitUnicodeString(0, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)), 0);
loc_00977B97:
    goto loc_00977A5A;
loc_00977BA1:
    result = ZwClose(0, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 - 41)), 0);
    goto loc_009777F0;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgQueryObjectProperties(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_mB0;
    uint8_t v_stack_mB8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (152);
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = *(uint64_t *)(v_rip + 0x4EEBFB);
    *(uint64_t *)(local_rsp - 0x4F - 0x19) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x25) = 1;
    *(uint32_t *)(local_rsp - 0x4F - 0x29) = 0;
    if (Arg4 != 0) goto loc_00977807;
    v_stack_mB0 = local_rsp - 79 - 25;
    v_stack_mB8 = 0;
    result = PnpOpenObjectRegKey(*(uint64_t *)(v_rip + 0x4EEBFB), Arg2, Arg3, (uint32_t)(0x2000001ULL));
    local_r10 = 0;
    if (!sign_flag) goto loc_00977807;
loc_009777E3:
    if (*(uint64_t *)(local_rsp - 0x4F - 0x19) != 0) goto loc_00977BA1;
loc_009777F0:
    local_rsp = (local_rsp) + (152);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00977807:
loc_0097780E:
    *(uint32_t *)(local_rsp - 0x4F - 0x21) = 0;
    if (0 >= (*(uint32_t *)(local_rsp - 0x4F + 0x7F))) goto loc_00977A5A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x1C)))) & (4)) == 0) goto loc_009779C0;
loc_0097783C:
    *(uint32_t *)(local_rsp - 0x4F + 0x57) = (uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x1C)))) & (2)) == 0) goto loc_00977855;
    if (0 == 0) goto loc_009779E0;
loc_0097784C:
loc_0097784F:
    *(uint32_t *)(local_rsp - 0x4F + 0x57) = 0;
loc_00977855:
    Arg4 = *(uint64_t *)(local_rsp - 0x4F - 0x19);
    if (*(uint64_t *)(local_rsp - 0x4F + 0x6F) != 0) { Arg4 = *(uint64_t *)(local_rsp - 0x4F + 0x6F); }
    v_stack_p50 = 0;
    v_stack_p48 = local_rsp - 79 - 41;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = local_rsp - 79 - 37;
    v_stack_p28 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8);
    v_stack_p20 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(local_rsp - 0x4F - 0x11), *(uint64_t *)(local_rsp - 0x4F + 0x5F), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x67)), Arg4);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00977A72;
    if (((uint32_t)(result)) == 0xC000009AULL) goto loc_00977A5A;
    local_r11 = 0;
    if (sign_flag) goto loc_0097798F;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x25))) == 0) goto loc_00977B17;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x25)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x8))))) goto loc_00977B2B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x8)))) == 18) goto loc_00977A0F;
loc_009778F4:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x25)))) == 20) goto loc_00977AC3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x25)))) == 18) goto loc_00977AC3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x25)))) == 25) goto loc_00977AC3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x25)))) == 0x2012ULL) goto loc_00977A1D;
loc_0097791A:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x10) != 0) goto loc_009779CD;
loc_00977929:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x1C)))) & (2)) == 0) goto loc_00977978;
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x10) == 0) goto loc_00977B44;
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)), (uint32_t)(0x67727453ULL), 0);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8) = result;
    if (result == 0) goto loc_00977B97;
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x2) = (uint16_t)(*(uint16_t *)(local_rsp - 0x4F - 0x29));
    result = memcpy(result, 0, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)), 0);
    local_r11 = 0;
    goto loc_0097797D;
loc_00977978:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x10) == 0) goto loc_009779AC;
loc_0097797D:
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x10)) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)));
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x25)) != 0x2012ULL) goto loc_00977ADD;
loc_0097798F:
loc_00977992:
    local_r10 = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x20) = (uint32_t)((uint32_t)((uint32_t)(result)));
    if (sign_flag) goto loc_00977A3C;
loc_009779A2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x21))) + 1);
    goto loc_0097780E;
loc_009779AC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x1C)))) & (2)) != 0) goto loc_00977B6E;
loc_009779B9:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)));
    goto loc_0097798F;
loc_009779C0:
    goto loc_0097783C;
loc_009779CD:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)))) <= 0xFFFEULL) goto loc_00977929;
    goto loc_0097798F;
loc_009779E0:
    result = ExAllocatePool2(260 - 4, 260, (uint32_t)(0x63647050ULL), 0);
    local_r10 = 0;
    if (result != 0) goto loc_0097784C;
loc_00977A05:
    goto loc_009777E3;
loc_00977A0F:
    if (((uint32_t)(result)) != 25) goto loc_009778F4;
    goto loc_00977B36;
loc_00977A1D:
    result = PnpValidateMultiSzData(0, 260, (uint32_t)(0x63647050ULL), 0);
    local_rbx = (uint32_t)(0xC000009AULL);
    if ((uint8_t)(result) == 0) { local_rbx = (uint32_t)((uint32_t)(0xC0000001ULL)); }
    if (sign_flag) goto loc_0097798F;
    goto loc_0097791A;
loc_00977A3C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x1C)))) & (8)) != 0) goto loc_00977B7E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x1C)))) & (1)) != 0) goto loc_00977A5A;
    goto loc_009779A2;
loc_00977A5A:
    if (result == 0) goto loc_009777E3;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x63647050ULL), 0);
    goto loc_009777E3;
loc_00977A72:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x1C)))) & (2)) == 0) goto loc_00977992;
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x29)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57))))) goto loc_00977B21;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x63647050ULL), 0);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)))), (uint32_t)(0x63647050ULL), 0);
    local_r10 = 0;
    if (result == 0) goto loc_00977A05;
    goto loc_0097784F;
loc_00977AC3:
    result = PnpValidateStringData(result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)))), (uint32_t)(0x63647050ULL), 0);
    if ((uint8_t)(result) != 0) goto loc_0097791A;
loc_00977AD3:
    goto loc_0097798F;
loc_00977ADD:
    if (*(uint64_t *)(0 + 0x8) == 0) goto loc_0097798F;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)))) < 2) goto loc_0097798F;
    result = ((uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)))) >> (1);
    if ((*(uint16_t *)(*(uint64_t *)(0 + 0x8) + result * 2 - 0x2)) != 0) goto loc_0097798F;
    Arg1 = (uint16_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29))) - (2));
    *(uint16_t *)(0) = (uint16_t)(Arg1);
    goto loc_0097798F;
loc_00977B17:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x8) = 0;
    goto loc_0097791A;
loc_00977B21:
    goto loc_00977992;
loc_00977B2B:
    if (((uint32_t)((uint32_t)(0x63647050ULL))) != 18) goto loc_00977AD3;
    if (((uint32_t)(result)) != 25) goto loc_00977AD3;
loc_00977B36:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x8) = 25;
    goto loc_009778F4;
loc_00977B44:
    result = ExAllocatePool2(Arg1, *(uint64_t *)(0 + 0x8), (uint32_t)(0x63647050ULL), 0);
    if (result == 0) goto loc_00977B97;
    result = memcpy(result, result, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)), 0);
    goto loc_009779AC;
loc_00977B6E:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77) + 0x0 + 0x0 * 4 * 8 + 0x10)) = result;
    goto loc_009779B9;
loc_00977B7E:
    Arg2 = 0;
    result = RtlInitUnicodeString(0, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)), 0);
loc_00977B97:
    goto loc_00977A5A;
loc_00977BA1:
    result = ZwClose(0, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x29)), 0);
    goto loc_009777F0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097776C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
