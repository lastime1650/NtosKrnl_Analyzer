# sub_00B3807C

- RVA: `0x00B3807C`–`0x00B3875C` (길이 `1,760` bytes)
- VA: `0x0000000140B3807C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ABFC8`
- 디코드: `408`개 명령, `1,760/1,760` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00B380C8` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00B3811B` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00B38136` → [IopSafebootDriverLoad](../AD/IopSafebootDriverLoad_function_00AD2880.md) (function, `0x00AD2880`)
- `0x00B3815D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B3819E` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00B381AF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B381BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B381CC` → [IopBootLog](../A9/IopBootLog_function_00A90998.md) (function, `0x00A90998`)
- `0x00B381DF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B381FC` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00B38207` → [IopBootLog](../A9/IopBootLog_function_00A90998.md) (function, `0x00A90998`)
- `0x00B38239` → [CmOpenInstallerClassRegKey](../9D/CmOpenInstallerClassRegKey_function_009D4474.md) (function, `0x009D4474`)
- `0x00B38297` → [PnpCallDriverQueryServiceHelper](../99/PnpCallDriverQueryServiceHelper_function_00995FB0.md) (function, `0x00995FB0`)
- `0x00B38304` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00B3831F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B38334` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B383C7` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00B38418` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00B38472` → [PnpCallDriverQueryServiceHelper](../99/PnpCallDriverQueryServiceHelper_function_00995FB0.md) (function, `0x00995FB0`)
- `0x00B38490` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00B384E0` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00B38531` → [PnpCallDriverQueryServiceHelper](../99/PnpCallDriverQueryServiceHelper_function_00995FB0.md) (function, `0x00995FB0`)
- `0x00B38554` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00B385A0` → [PnpCallDriverQueryServiceHelper](../99/PnpCallDriverQueryServiceHelper_function_00995FB0.md) (function, `0x00995FB0`)
- `0x00B385BE` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00B3861D` → [PnpCallDriverQueryServiceHelper](../99/PnpCallDriverQueryServiceHelper_function_00995FB0.md) (function, `0x00995FB0`)
- `0x00B38644` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00B3869B` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00B386FC` → [CmSetDeviceRegProp](../8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00B38729` → [PnpUnloadAttachedDriver](../AA/PnpUnloadAttachedDriver_function_00AA80E8.md) (function, `0x00AA80E8`)
- `0x00B38731` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00B3873B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B38090` → RVA `0x00E66398` (`.data`; read)
- `0x00B380B7` → RVA `0x00027C50` (`.rdata`; read)
- `0x00B38120` → RVA `0x00FC41C4` (`.data`; read)
- `0x00B3826B` → RVA `0x0001EA00` (`.rdata`; read)
- `0x00B382F2` → RVA `0x0001E9E8` (`.rdata`; read)
- `0x00B3843D` → RVA `0x000140B0` (`.rdata`; read)
- `0x00B3856B` → RVA `0x000140C8` (`.rdata`; read)
- `0x00B385ED` → RVA `0x00014158` (`.rdata`; read)
- `0x00B38716` → RVA `0x00E66244` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x00B3811B` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00B3815D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B381AF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B381BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B381DF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B381FC` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00B3831F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B38334` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B384E0` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00B38731` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00B3873B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **28**
  - `0x00B380E1` → [PipCallDriverAddDevice + 0x10A](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B380F8` → [PipCallDriverAddDevice + 0x3FF](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38102` → [PipCallDriverAddDevice + 0x265](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B3810D` → [PipCallDriverAddDevice + 0x265](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B381D4` → [PipCallDriverAddDevice + 0x347](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B381E5` → [PipCallDriverAddDevice + 0x347](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B3823F` → [PipCallDriverAddDevice + 0x265](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B382AE` → [PipCallDriverAddDevice + 0x5F4](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38352` → [PipCallDriverAddDevice + 0x5F4](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38373` → [PipCallDriverAddDevice + 0x5F4](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38428` → [PipCallDriverAddDevice + 0x678](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38485` → [PipCallDriverAddDevice + 0x678](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38496` → [PipCallDriverAddDevice + 0x680](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38544` → [PipCallDriverAddDevice + 0x5F4](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B3855A` → [PipCallDriverAddDevice + 0x5F4](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B385B3` → [PipCallDriverAddDevice + 0x66B](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B385CA` → [PipCallDriverAddDevice + 0x351](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B385DB` → [PipCallDriverAddDevice + 0x351](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38634` → [PipCallDriverAddDevice + 0x4DA](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B3863A` → [PipCallDriverAddDevice + 0x351](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B3864A` → [PipCallDriverAddDevice + 0x351](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38652` → [PipCallDriverAddDevice + 0x3AA](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B386A2` → [PipCallDriverAddDevice + 0x3AA](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B386AC` → [PipCallDriverAddDevice + 0x3AA](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B386B6` → [PipCallDriverAddDevice + 0x3AA](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B386C4` → [PipCallDriverAddDevice + 0x3AA](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38702` → [PipCallDriverAddDevice + 0x3AA](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)
  - `0x00B38757` → [PipCallDriverAddDevice + 0x50A](../A2/PipCallDriverAddDevice_function_00A272E0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B3807C  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
00B38081  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00B38086  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00B3808A  41 B8 01 00 00 00               mov r8d, 1
00B38090  48 8B 0D 01 E3 32 00            mov rcx, qword ptr [rip + 0x32e301]
00B38097  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00B3809C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B380A1  48 8D 45 80                     lea rax, [rbp - 0x80]
00B380A5  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00B380A9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B380AE  48 8D 45 88                     lea rax, [rbp - 0x78]
00B380B2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B380B7  48 8D 05 92 FB 4E FF            lea rax, [rip - 0xb1046e]
00B380BE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B380C3  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00B380C8  E8 B3 A0 DA FF                  call 0x1408e2180
00B380CD  85 C0                           test eax, eax
00B380CF  78 16                           js 0x140b380e7
00B380D1  83 7D 88 07                     cmp dword ptr [rbp - 0x78], 7
00B380D5  75 10                           jne 0x140b380e7
00B380D7  39 5C 24 64                     cmp dword ptr [rsp + 0x64], ebx
00B380DB  75 0A                           jne 0x140b380e7
00B380DD  44 39 75 80                     cmp dword ptr [rbp - 0x80], r14d
00B380E1  0F 85 03 F3 EE FF               jne 0x140a273ea
00B380E7  41 B8 35 00 00 00               mov r8d, 0x35
00B380ED  EB 06                           jmp 0x140b380f5
00B380EF  41 B8 38 00 00 00               mov r8d, 0x38
00B380F5  45 33 C9                        xor r9d, r9d
00B380F8  E9 E2 F5 EE FF                  jmp 0x140a276df
00B380FD  83 7C 24 70 01                  cmp dword ptr [rsp + 0x70], 1
00B38102  0F 85 3D F4 EE FF               jne 0x140a27545
00B38108  44 39 74 24 60                  cmp dword ptr [rsp + 0x60], r14d
00B3810D  0F 84 32 F4 EE FF               je 0x140a27545
00B38113  48 8D 55 20                     lea rdx, [rbp + 0x20]
00B38117  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00B3811B  E8 40 B8 92 FF                  call 0x140463960
00B38120  44 39 35 9D C0 48 00            cmp dword ptr [rip + 0x48c09d], r14d
00B38127  0F 84 E6 00 00 00               je 0x140b38213
00B3812D  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00B38132  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00B38136  E8 45 A7 F9 FF                  call 0x140ad2880
00B3813B  84 C0                           test al, al
00B3813D  0F 85 CB 00 00 00               jne 0x140b3820e
00B38143  41 BF 00 01 00 00               mov r15d, 0x100
00B38149  41 BE 50 70 65 6E               mov r14d, 0x6e657050
00B3814F  45 8B C6                        mov r8d, r14d
00B38152  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
00B38157  41 8B D7                        mov edx, r15d
00B3815A  41 8B CF                        mov ecx, r15d
00B3815D  E8 8E 9F 04 00                  call 0x140b820f0
00B38162  48 8B D8                        mov rbx, rax
00B38165  48 85 C0                        test rax, rax
00B38168  74 5C                           je 0x140b381c6
00B3816A  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
00B3816F  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B38174  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00B38179  41 B9 01 00 00 00               mov r9d, 1
00B3817F  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00B38183  48 8B 0D 0E E2 32 00            mov rcx, qword ptr [rip + 0x32e20e]
00B3818A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B3818F  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00B38194  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00B38199  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B3819E  E8 CD 56 DB FF                  call 0x1408ed870
00B381A3  3D 23 00 00 C0                  cmp eax, 0xc0000023
00B381A8  75 40                           jne 0x140b381ea
00B381AA  33 D2                           xor edx, edx
00B381AC  48 8B CB                        mov rcx, rbx
00B381AF  E8 BC A6 04 00                  call 0x140b82870
00B381B4  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
00B381B8  45 8B C6                        mov r8d, r14d
00B381BB  41 8B CF                        mov ecx, r15d
00B381BE  E8 2D 9F 04 00                  call 0x140b820f0
00B381C3  48 8B D8                        mov rbx, rax
00B381C6  33 D2                           xor edx, edx
00B381C8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00B381CC  E8 C7 87 F5 FF                  call 0x140a90998
00B381D1  48 85 DB                        test rbx, rbx
00B381D4  0F 84 4D F4 EE FF               je 0x140a27627
00B381DA  33 D2                           xor edx, edx
00B381DC  48 8B CB                        mov rcx, rbx
00B381DF  E8 8C A6 04 00                  call 0x140b82870
00B381E4  90                              nop
00B381E5  E9 3D F4 EE FF                  jmp 0x140a27627
00B381EA  85 C0                           test eax, eax
00B381EC  78 D8                           js 0x140b381c6
00B381EE  0F 57 C0                        xorps xmm0, xmm0
00B381F1  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00B381F5  48 8B D3                        mov rdx, rbx
00B381F8  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00B381FC  E8 7F 25 8F FF                  call 0x14042a780
00B38201  33 D2                           xor edx, edx
00B38203  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00B38207  E8 8C 87 F5 FF                  call 0x140a90998
00B3820C  EB CC                           jmp 0x140b381da
00B3820E  44 8A 64 24 68                  mov r12b, byte ptr [rsp + 0x68]
00B38213  48 8B 0D 7E E1 32 00            mov rcx, qword ptr [rip + 0x32e17e]
00B3821A  48 8D 45 98                     lea rax, [rbp - 0x68]
00B3821E  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00B38223  48 8D 55 20                     lea rdx, [rbp + 0x20]
00B38227  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B3822C  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00B38231  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00B38239  E8 36 C2 E9 FF                  call 0x1409d4474
00B3823E  90                              nop
00B3823F  E9 01 F3 EE FF                  jmp 0x140a27545
00B38244  F7 44 24 6C 00 00 08 00         test dword ptr [rsp + 0x6c], 0x80000
00B3824C  0F 84 CB 01 00 00               je 0x140b3841d
00B38252  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00B38256  48 85 C9                        test rcx, rcx
00B38259  0F 84 1A 01 00 00               je 0x140b38379
00B3825F  48 8D 45 E0                     lea rax, [rbp - 0x20]
00B38263  45 33 C0                        xor r8d, r8d
00B38266  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B3826B  4C 8D 0D 8E 67 4E FF            lea r9, [rip - 0xb19872]
00B38272  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B38277  48 8D 45 20                     lea rax, [rbp + 0x20]
00B3827B  21 5C 24 38                     and dword ptr [rsp + 0x38], ebx
00B3827F  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00B38284  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00B38289  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B3828E  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00B38292  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B38297  E8 14 DD E5 FF                  call 0x140995fb0
00B3829C  8B D8                           mov ebx, eax
00B3829E  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B382A3  74 0F                           je 0x140b382b4
00B382A5  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B382AA  74 08                           je 0x140b382b4
00B382AC  85 C0                           test eax, eax
00B382AE  0F 88 20 F6 EE FF               js 0x140a278d4
00B382B4  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00B382B9  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00B382BE  48 8B 75 90                     mov rsi, qword ptr [rbp - 0x70]
00B382C2  48 8D 55 20                     lea rdx, [rbp + 0x20]
00B382C6  4C 8B 4D 98                     mov r9, qword ptr [rbp - 0x68]
00B382CA  41 B8 02 00 00 00               mov r8d, 2
00B382D0  48 8B 0D C1 E0 32 00            mov rcx, qword ptr [rip + 0x32e0c1]
00B382D7  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B382DC  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00B382E0  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B382E4  48 8D 45 A0                     lea rax, [rbp - 0x60]
00B382E8  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00B382ED  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B382F2  48 8D 05 EF 66 4E FF            lea rax, [rip - 0xb19911]
00B382F9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B382FE  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B38304  E8 77 9E DA FF                  call 0x1408e2180
00B38309  3D 23 00 00 C0                  cmp eax, 0xc0000023
00B3830E  75 47                           jne 0x140b38357
00B38310  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00B38314  39 44 24 64                     cmp dword ptr [rsp + 0x64], eax
00B38318  76 33                           jbe 0x140b3834d
00B3831A  33 D2                           xor edx, edx
00B3831C  48 8B CE                        mov rcx, rsi
00B3831F  E8 4C A5 04 00                  call 0x140b82870
00B38324  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00B38328  45 8B C6                        mov r8d, r14d
00B3832B  8B D0                           mov edx, eax
00B3832D  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B38331  49 8B CF                        mov rcx, r15
00B38334  E8 B7 9D 04 00                  call 0x140b820f0
00B38339  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00B3833D  48 85 C0                        test rax, rax
00B38340  0F 85 6E FF FF FF               jne 0x140b382b4
00B38346  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00B3834B  EB 24                           jmp 0x140b38371
00B3834D  BB 01 00 00 C0                  mov ebx, 0xc0000001
00B38352  E9 7D F5 EE FF                  jmp 0x140a278d4
00B38357  8B D8                           mov ebx, eax
00B38359  85 C0                           test eax, eax
00B3835B  0F 89 3A 01 00 00               jns 0x140b3849b
00B38361  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B38366  74 07                           je 0x140b3836f
00B38368  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B3836D  75 02                           jne 0x140b38371
00B3836F  33 DB                           xor ebx, ebx
00B38371  85 DB                           test ebx, ebx
00B38373  0F 88 5B F5 EE FF               js 0x140a278d4
00B38379  48 83 7D F0 00                  cmp qword ptr [rbp - 0x10], 0
00B3837E  0F 85 99 00 00 00               jne 0x140b3841d
00B38384  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
00B38389  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00B3838E  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00B38393  BE 04 00 00 00                  mov esi, 4
00B38398  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00B3839C  48 8B 0D F5 DF 32 00            mov rcx, qword ptr [rip + 0x32dff5]
00B383A3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B383A8  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00B383AD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B383B2  44 8D 76 07                     lea r14d, [rsi + 7]
00B383B6  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00B383BB  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
00B383BF  45 8B CE                        mov r9d, r14d
00B383C2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B383C7  E8 A4 54 DB FF                  call 0x1408ed870
00B383CC  85 C0                           test eax, eax
00B383CE  78 4D                           js 0x140b3841d
00B383D0  39 74 24 70                     cmp dword ptr [rsp + 0x70], esi
00B383D4  75 47                           jne 0x140b3841d
00B383D6  39 74 24 64                     cmp dword ptr [rsp + 0x64], esi
00B383DA  75 41                           jne 0x140b3841d
00B383DC  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00B383E0  0F BA E0 13                     bt eax, 0x13
00B383E4  73 37                           jae 0x140b3841d
00B383E6  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
00B383EB  0F BA F0 13                     btr eax, 0x13
00B383EF  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00B383F4  45 8B CE                        mov r9d, r14d
00B383F7  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00B383FB  48 8B 0D 96 DF 32 00            mov rcx, qword ptr [rip + 0x32df96]
00B38402  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
00B38406  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00B3840B  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00B3840F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B38414  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00B38418  E8 6F 52 DC FF                  call 0x1408fd68c
00B3841D  BE 00 00 00 04                  mov esi, 0x4000000
00B38422  85 B7 8C 01 00 00               test dword ptr [rdi + 0x18c], esi
00B38428  0F 85 2A F5 EE FF               jne 0x140a27958
00B3842E  48 8D 45 E0                     lea rax, [rbp - 0x20]
00B38432  41 B8 13 00 00 00               mov r8d, 0x13
00B38438  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B3843D  4C 8D 0D 6C BC 4D FF            lea r9, [rip - 0xb24394]
00B38444  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00B38449  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00B3844E  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B38453  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00B38457  C7 44 24 38 01 00 00 00         mov dword ptr [rsp + 0x38], 1
00B3845F  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
00B38464  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B38469  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
00B3846D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B38472  E8 39 DB E5 FF                  call 0x140995fb0
00B38477  8B D8                           mov ebx, eax
00B38479  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B3847E  74 0B                           je 0x140b3848b
00B38480  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B38485  0F 85 CD F4 EE FF               jne 0x140a27958
00B3848B  8B D6                           mov edx, esi
00B3848D  48 8B CF                        mov rcx, rdi
00B38490  E8 B3 3B DC FF                  call 0x1408fc048
00B38495  90                              nop
00B38496  E9 C5 F4 EE FF                  jmp 0x140a27960
00B3849B  81 7D A0 03 10 00 00            cmp dword ptr [rbp - 0x60], 0x1003
00B384A2  0F 85 D1 FE FF FF               jne 0x140b38379
00B384A8  8B 74 24 64                     mov esi, dword ptr [rsp + 0x64]
00B384AC  40 F6 C6 07                     test sil, 7
00B384B0  0F 85 C3 FE FF FF               jne 0x140b38379
00B384B6  85 F6                           test esi, esi
00B384B8  0F 84 BB FE FF FF               je 0x140b38379
00B384BE  48 8B 5D 90                     mov rbx, qword ptr [rbp - 0x70]
00B384C2  C1 EE 03                        shr esi, 3
00B384C5  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
00B384CA  45 33 C9                        xor r9d, r9d
00B384CD  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00B384D2  45 33 C0                        xor r8d, r8d
00B384D5  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B384DB  33 D2                           xor edx, edx
00B384DD  48 8B CB                        mov rcx, rbx
00B384E0  E8 2B 88 B7 FF                  call 0x1406b0d10
00B384E5  48 83 C3 08                     add rbx, 8
00B384E9  83 C6 FF                        add esi, -1
00B384EC  75 D7                           jne 0x140b384c5
00B384EE  E9 FC FB FF FF                  jmp 0x140b380ef
00B384F3  48 8D 45 E0                     lea rax, [rbp - 0x20]
00B384F7  45 33 C9                        xor r9d, r9d
00B384FA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B384FF  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00B38504  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00B38509  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00B3850D  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B38512  C7 44 24 38 03 00 00 00         mov dword ptr [rsp + 0x38], 3
00B3851A  45 8D 41 05                     lea r8d, [r9 + 5]
00B3851E  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
00B38523  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B38528  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
00B3852C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B38531  E8 7A DA E5 FF                  call 0x140995fb0
00B38536  8B D8                           mov ebx, eax
00B38538  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B3853D  74 0B                           je 0x140b3854a
00B3853F  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B38544  0F 85 8A F3 EE FF               jne 0x140a278d4
00B3854A  8B D6                           mov edx, esi
00B3854C  48 8B CF                        mov rcx, rdi
00B3854F  BB 34 00 00 C0                  mov ebx, 0xc0000034
00B38554  E8 EF 3A DC FF                  call 0x1408fc048
00B38559  90                              nop
00B3855A  E9 75 F3 EE FF                  jmp 0x140a278d4
00B3855F  48 8D 45 E0                     lea rax, [rbp - 0x20]
00B38563  45 8B C6                        mov r8d, r14d
00B38566  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B3856B  4C 8D 0D 56 BB 4D FF            lea r9, [rip - 0xb244aa]
00B38572  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00B38577  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00B3857C  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B38581  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00B38585  C7 44 24 38 04 00 00 00         mov dword ptr [rsp + 0x38], 4
00B3858D  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
00B38592  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B38597  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
00B3859B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B385A0  E8 0B DA E5 FF                  call 0x140995fb0
00B385A5  8B D8                           mov ebx, eax
00B385A7  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B385AC  74 0B                           je 0x140b385b9
00B385AE  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B385B3  0F 85 92 F3 EE FF               jne 0x140a2794b
00B385B9  8B D6                           mov edx, esi
00B385BB  48 8B CF                        mov rcx, rdi
00B385BE  E8 85 3A DC FF                  call 0x1408fc048
00B385C3  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00B385C7  48 85 C9                        test rcx, rcx
00B385CA  0F 84 61 F0 EE FF               je 0x140a27631
00B385D0  BE 00 00 00 40                  mov esi, 0x40000000
00B385D5  85 B7 8C 01 00 00               test dword ptr [rdi + 0x18c], esi
00B385DB  0F 85 50 F0 EE FF               jne 0x140a27631
00B385E1  48 8D 45 E0                     lea rax, [rbp - 0x20]
00B385E5  45 8B C6                        mov r8d, r14d
00B385E8  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B385ED  4C 8D 0D 64 BB 4D FF            lea r9, [rip - 0xb2449c]
00B385F4  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B385F9  48 8D 45 20                     lea rax, [rbp + 0x20]
00B385FD  C7 44 24 38 05 00 00 00         mov dword ptr [rsp + 0x38], 5
00B38605  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00B3860A  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00B3860F  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B38614  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00B38618  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B3861D  E8 8E D9 E5 FF                  call 0x140995fb0
00B38622  8B D8                           mov ebx, eax
00B38624  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B38629  74 14                           je 0x140b3863f
00B3862B  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B38630  74 0D                           je 0x140b3863f
00B38632  85 C0                           test eax, eax
00B38634  0F 88 80 F1 EE FF               js 0x140a277ba
00B3863A  E9 F2 EF EE FF                  jmp 0x140a27631
00B3863F  8B D6                           mov edx, esi
00B38641  48 8B CF                        mov rcx, rdi
00B38644  E8 FF 39 DC FF                  call 0x1408fc048
00B38649  90                              nop
00B3864A  E9 E2 EF EE FF                  jmp 0x140a27631
00B3864F  4D 85 FF                        test r15, r15
00B38652  0F 84 32 F0 EE FF               je 0x140a2768a
00B38658  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
00B3865D  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00B38662  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00B38667  BE 04 00 00 00                  mov esi, 4
00B3866C  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00B38670  48 8B 0D 21 DD 32 00            mov rcx, qword ptr [rip + 0x32dd21]
00B38677  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B3867C  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00B38681  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B38686  44 8D 7E 07                     lea r15d, [rsi + 7]
00B3868A  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00B3868F  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
00B38693  45 8B CF                        mov r9d, r15d
00B38696  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B3869B  E8 D0 51 DB FF                  call 0x1408ed870
00B386A0  85 C0                           test eax, eax
00B386A2  0F 88 E2 EF EE FF               js 0x140a2768a
00B386A8  39 74 24 70                     cmp dword ptr [rsp + 0x70], esi
00B386AC  0F 85 D8 EF EE FF               jne 0x140a2768a
00B386B2  39 74 24 64                     cmp dword ptr [rsp + 0x64], esi
00B386B6  0F 85 CE EF EE FF               jne 0x140a2768a
00B386BC  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00B386C0  0F BA E0 13                     bt eax, 0x13
00B386C4  0F 83 C0 EF EE FF               jae 0x140a2768a
00B386CA  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
00B386CF  0F BA F0 13                     btr eax, 0x13
00B386D3  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00B386D8  45 8B CF                        mov r9d, r15d
00B386DB  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00B386DF  48 8B 0D B2 DC 32 00            mov rcx, qword ptr [rip + 0x32dcb2]
00B386E6  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
00B386EA  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00B386EF  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00B386F3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B386F8  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00B386FC  E8 8B 4F DC FF                  call 0x1408fd68c
00B38701  90                              nop
00B38702  E9 83 EF EE FF                  jmp 0x140a2768a
00B38707  48 8D 75 F0                     lea rsi, [rbp - 0x10]
00B3870B  45 33 FF                        xor r15d, r15d
00B3870E  48 8B 3E                        mov rdi, qword ptr [rsi]
00B38711  48 85 FF                        test rdi, rdi
00B38714  74 33                           je 0x140b38749
00B38716  44 38 3D 27 DB 32 00            cmp byte ptr [rip + 0x32db27], r15b
00B3871D  4C 8B F7                        mov r14, rdi
00B38720  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
00B38724  74 08                           je 0x140b3872e
00B38726  49 8B 0E                        mov rcx, qword ptr [r14]
00B38729  E8 BA F9 F6 FF                  call 0x140aa80e8
00B3872E  49 8B 0E                        mov rcx, qword ptr [r14]
00B38731  E8 1A 0C 7C FF                  call 0x1402f9350
00B38736  33 D2                           xor edx, edx
00B38738  49 8B CE                        mov rcx, r14
00B3873B  E8 30 A1 04 00                  call 0x140b82870
00B38740  48 85 FF                        test rdi, rdi
00B38743  75 D1                           jne 0x140b38716
00B38745  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00B38749  48 83 C6 08                     add rsi, 8
00B3874D  48 83 E8 01                     sub rax, 1
00B38751  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00B38755  75 B7                           jne 0x140b3870e
00B38757  E9 8E F0 EE FF                  jmp 0x140a277ea
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B3807C(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p50 = (unsigned int)(v_r14);
    v_stack_p48 = v_stack_p64;
    v_stack_p40 = (unsigned int)(v_rbx);
    v_stack_p38 = v_rbp - 128;
    v_stack_p30 = v_rbp - 120;
    v_stack_p28 = v_rip - 11601006;
    v_stack_p20 = v_r14;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 3334913), *(unsigned __int64 *)(v_rdi + 48), 1, a15);
    if (sign_flag) goto loc_00B380E7;
    if ((*(unsigned int *)(v_rbp - 120)) != 7) goto loc_00B380E7;
    if (v_stack_p64 != ((unsigned int)(v_rbx))) goto loc_00B380E7;
loc_00B380E7:
    goto loc_00B380F5;
loc_00B380F5:
    a4 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B3807C(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, int64_t Arg15)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint32_t v_stack_p60;
    uint64_t v_stack_p64;
    uint64_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p50 = (uint32_t)(local_r14);
    v_stack_p48 = v_stack_p64;
    v_stack_p40 = (uint32_t)(local_rbx);
    v_stack_p38 = local_rbp - 128;
    v_stack_p30 = local_rbp - 120;
    v_stack_p28 = v_rip - 11601006;
    v_stack_p20 = local_r14;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x32E301), *(uint64_t *)(local_rdi + 0x30), 1, Arg15);
    if (sign_flag) goto loc_00B380E7;
    if ((*(uint32_t *)(local_rbp - 0x78)) != 7) goto loc_00B380E7;
    if (v_stack_p64 != ((uint32_t)(local_rbx))) goto loc_00B380E7;
loc_00B380E7:
    goto loc_00B380F5;
loc_00B380F5:
    Arg4 = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B3807C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
