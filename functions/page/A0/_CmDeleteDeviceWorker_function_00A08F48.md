# _CmDeleteDeviceWorker

- RVA: `0x00A08F48`–`0x00A09514` (길이 `1,484` bytes)
- VA: `0x0000000140A08F48`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A8780`
- 디코드: `374`개 명령, `1,484/1,484` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00A08FD4` → [_CmOpenDeviceRegKey](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x00A0901C` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00A0907E` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A090DB` → [_CmGetMatchingFilteredDeviceInterfaceList](_CmGetMatchingFilteredDeviceInterfaceList_function_00A09610.md) (function, `0x00A09610`)
- `0x00A0912C` → [_CmGetMatchingDeviceList](_CmGetMatchingDeviceList_function_00A0951C.md) (function, `0x00A0951C`)
- `0x00A091B3` → [_CmGetDeviceMappedPropertyKeys](../9D/_CmGetDeviceMappedPropertyKeys_function_009D0D78.md) (function, `0x009D0D78`)
- `0x00A09205` → [_CmSetDeviceMappedProperty](_CmSetDeviceMappedProperty_function_00A0B098.md) (function, `0x00A0B098`)
- `0x00A09227` → [_CmDeleteDeviceRegKey](_CmDeleteDeviceRegKey_function_00A09A2C.md) (function, `0x00A09A2C`)
- `0x00A09257` → [CmDeleteDeviceInterface](CmDeleteDeviceInterface_function_00A09E98.md) (function, `0x00A09E98`)
- `0x00A092C5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A092F7` → [_CmDeleteDeviceRegKey](_CmDeleteDeviceRegKey_function_00A09A2C.md) (function, `0x00A09A2C`)
- `0x00A0930E` → [CmRaiseDeleteEvent](../82/CmRaiseDeleteEvent_function_0082DBE0.md) (function, `0x0082DBE0`)
- `0x00A0932D` → [_CmGetDeviceContainerIdFromBase](../8F/_CmGetDeviceContainerIdFromBase_function_008FD2B4.md) (function, `0x008FD2B4`)
- `0x00A0934A` → [CmRemoveDeviceFromContainer](../82/CmRemoveDeviceFromContainer_function_0082BF40.md) (function, `0x0082BF40`)
- `0x00A0936E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A093A9` → [CmRemovePanelDevice](../82/CmRemovePanelDevice_function_0082F32C.md) (function, `0x0082F32C`)
- `0x00A093E2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A09410` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A09482` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A094D3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A094E2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A094F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A09500` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A0950A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [CmDeleteDevice](../82/CmDeleteDevice_function_00829BB8.md) at `0x00829C44`

### Static image references
- `0x00A08F64` → RVA `0x00E0A740` (`.data`; read)
- `0x00A0906A` → RVA `0x000115A0` (`.rdata`; read)
- `0x00A0910A` → RVA `0x00A89E50` (`CmMatchLastKnownParentCallback`; read)
- `0x00A0915C` → RVA `0x00014DA0` (`.rdata`; read)
- `0x00A09168` → RVA `0x00014D90` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00A092C5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A0936E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A093E2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A09410` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A09482` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A094D3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A094E2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A094F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A09500` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A0950A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **17**
  - `0x00A090A5` → [sub_00B348F8 + 0x3A](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A09363` → [sub_00B348F8](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A09374` → [sub_00B348F8](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A0937D` → [sub_00B348F8 + 0x30](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A09388` → [sub_00B348F8 + 0x30](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A0939A` → [sub_00B348F8 + 0x30](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A093BA` → [sub_00B348F8 + 0x3A](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A093CE` → [sub_00B348F8 + 0x71](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A093D7` → [sub_00B348F8 + 0x42](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A093E8` → [sub_00B348F8 + 0x42](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A093FC` → [sub_00B348F8 + 0xA9](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A09405` → [sub_00B348F8 + 0x7B](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A09416` → [sub_00B348F8 + 0x7B](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A0942F` → [sub_00B348F8 + 0xB3](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A0946E` → [sub_00B348F8 + 0xA9](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A09477` → [sub_00B348F8 + 0x108](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)
  - `0x00A09488` → [sub_00B348F8 + 0x108](../B3/Unknown_function_00B348F8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A08F48  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A08F4D  55                              push rbp
00A08F4E  56                              push rsi
00A08F4F  57                              push rdi
00A08F50  41 54                           push r12
00A08F52  41 55                           push r13
00A08F54  41 56                           push r14
00A08F56  41 57                           push r15
00A08F58  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
00A08F5D  48 81 EC 70 01 00 00            sub rsp, 0x170
00A08F64  48 8B 05 D5 17 40 00            mov rax, qword ptr [rip + 0x4017d5]
00A08F6B  48 33 C4                        xor rax, rsp
00A08F6E  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00A08F72  4C 8B E1                        mov r12, rcx
00A08F75  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
00A08F79  33 C9                           xor ecx, ecx
00A08F7B  48 8B FA                        mov rdi, rdx
00A08F7E  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00A08F83  44 8B E9                        mov r13d, ecx
00A08F86  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00A08F8B  44 8B F1                        mov r14d, ecx
00A08F8E  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
00A08F92  8B F1                           mov esi, ecx
00A08F94  89 4C 24 6C                     mov dword ptr [rsp + 0x6c], ecx
00A08F98  44 8B F9                        mov r15d, ecx
00A08F9B  89 4D 8C                        mov dword ptr [rbp - 0x74], ecx
00A08F9E  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00A08FA2  89 4D 88                        mov dword ptr [rbp - 0x78], ecx
00A08FA5  66 45 85 C0                     test r8w, r8w
00A08FA9  0F 85 69 03 00 00               jne 0x140a09318
00A08FAF  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00A08FB4  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00A08FB9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A08FBE  44 8D 41 10                     lea r8d, [rcx + 0x10]
00A08FC2  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
00A08FC6  45 33 C9                        xor r9d, r9d
00A08FC9  49 8B CC                        mov rcx, r12
00A08FCC  C7 44 24 20 02 00 01 02         mov dword ptr [rsp + 0x20], 0x2010002
00A08FD4  E8 67 55 EE FF                  call 0x1408ee540
00A08FD9  33 C9                           xor ecx, ecx
00A08FDB  8B D8                           mov ebx, eax
00A08FDD  85 C0                           test eax, eax
00A08FDF  0F 88 C9 02 00 00               js 0x140a092ae
00A08FE5  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00A08FEA  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A08FEF  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00A08FF3  44 8D 4E 25                     lea r9d, [rsi + 0x25]
00A08FF7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A08FFC  48 8B D7                        mov rdx, rdi
00A08FFF  48 8D 45 C0                     lea rax, [rbp - 0x40]
00A09003  C7 44 24 60 4E 00 00 00         mov dword ptr [rsp + 0x60], 0x4e
00A0900B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A09010  49 8B CC                        mov rcx, r12
00A09013  48 8D 45 8C                     lea rax, [rbp - 0x74]
00A09017  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0901C  E8 4F 48 EE FF                  call 0x1408ed870
00A09021  33 C9                           xor ecx, ecx
00A09023  8B D8                           mov ebx, eax
00A09025  85 C0                           test eax, eax
00A09027  0F 89 F2 02 00 00               jns 0x140a0931f
00A0902D  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A09032  0F 85 76 02 00 00               jne 0x140a092ae
00A09038  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
00A0903D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A09042  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00A09046  41 B8 01 00 00 00               mov r8d, 1
00A0904C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A09051  48 8B D7                        mov rdx, rdi
00A09054  44 89 7C 24 40                  mov dword ptr [rsp + 0x40], r15d
00A09059  48 8D 45 88                     lea rax, [rbp - 0x78]
00A0905D  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00A09062  4C 8B FF                        mov r15, rdi
00A09065  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0906A  48 8D 05 2F 85 60 FF            lea rax, [rip - 0x9f7ad1]
00A09071  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A09076  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A0907B  49 8B CC                        mov rcx, r12
00A0907E  E8 FD 90 ED FF                  call 0x1408e2180
00A09083  8B D8                           mov ebx, eax
00A09085  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A0908A  0F 84 D0 02 00 00               je 0x140a09360
00A09090  33 C9                           xor ecx, ecx
00A09092  85 C0                           test eax, eax
00A09094  0F 89 DF 02 00 00               jns 0x140a09379
00A0909A  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A0909F  0F 85 00 02 00 00               jne 0x140a092a5
00A090A5  E9 88 B8 12 00                  jmp 0x140b34932
00A090AA  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A090AE  45 33 C9                        xor r9d, r9d
00A090B1  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00A090B6  4D 8B C7                        mov r8, r15
00A090B9  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00A090BE  33 D2                           xor edx, edx
00A090C0  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A090C4  49 8B CC                        mov rcx, r12
00A090C7  33 C0                           xor eax, eax
00A090C9  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00A090CE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A090D3  49 8B FD                        mov rdi, r13
00A090D6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A090DB  E8 30 05 00 00                  call 0x140a09610
00A090E0  8B D8                           mov ebx, eax
00A090E2  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A090E7  0F 84 D2 02 00 00               je 0x140a093bf
00A090ED  33 C9                           xor ecx, ecx
00A090EF  85 C0                           test eax, eax
00A090F1  0F 85 9C 01 00 00               jne 0x140a09293
00A090F7  39 4C 24 68                     cmp dword ptr [rsp + 0x68], ecx
00A090FB  0F 87 42 01 00 00               ja 0x140a09243
00A09101  8B C1                           mov eax, ecx
00A09103  4D 8B FE                        mov r15, r14
00A09106  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
00A0910A  48 8D 15 3F 0D 08 00            lea rdx, [rip + 0x80d3f]
00A09111  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00A09115  4D 8B CF                        mov r9, r15
00A09118  48 8D 4C 24 6C                  lea rcx, [rsp + 0x6c]
00A0911D  49 8B FF                        mov rdi, r15
00A09120  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A09125  49 8B CC                        mov rcx, r12
00A09128  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A0912C  E8 EB 03 00 00                  call 0x140a0951c
00A09131  8B D8                           mov ebx, eax
00A09133  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A09138  0F 84 AF 02 00 00               je 0x140a093ed
00A0913E  33 C9                           xor ecx, ecx
00A09140  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
00A09145  85 C0                           test eax, eax
00A09147  0F 85 38 01 00 00               jne 0x140a09285
00A0914D  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
00A09152  39 4C 24 6C                     cmp dword ptr [rsp + 0x6c], ecx
00A09156  0F 87 BF 02 00 00               ja 0x140a0941b
00A0915C  66 0F 6F 05 3C BC 60 FF         movdqa xmm0, xmmword ptr [rip - 0x9f43c4]
00A09164  4C 8D 7D 98                     lea r15, [rbp - 0x68]
00A09168  66 0F 6F 0D 20 BC 60 FF         movdqa xmm1, xmmword ptr [rip - 0x9f43e0]
00A09170  8B F9                           mov edi, ecx
00A09172  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
00A09177  F3 0F 7F 4D A8                  movdqu xmmword ptr [rbp - 0x58], xmm1
00A0917C  83 FF 08                        cmp edi, 8
00A0917F  0F 82 95 00 00 00               jb 0x140a0921a
00A09185  4C 8B 7D 80                     mov r15, qword ptr [rbp - 0x80]
00A09189  4C 8B F1                        mov r14, rcx
00A0918C  8B F9                           mov edi, ecx
00A0918E  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
00A09192  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00A09197  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00A0919C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A091A1  41 B1 01                        mov r9b, 1
00A091A4  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00A091A8  49 8B D7                        mov rdx, r15
00A091AB  49 8B CC                        mov rcx, r12
00A091AE  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00A091B3  E8 C0 7B FC FF                  call 0x1409d0d78
00A091B8  8B D8                           mov ebx, eax
00A091BA  3D 23 00 00 C0                  cmp eax, 0xc0000023
00A091BF  0F 84 95 02 00 00               je 0x140a0945a
00A091C5  33 D2                           xor edx, edx
00A091C7  85 C0                           test eax, eax
00A091C9  0F 85 BE 02 00 00               jne 0x140a0948d
00A091CF  8B FA                           mov edi, edx
00A091D1  3B 7C 24 64                     cmp edi, dword ptr [rsp + 0x64]
00A091D5  0F 83 0F 01 00 00               jae 0x140a092ea
00A091DB  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00A091E0  45 33 C9                        xor r9d, r9d
00A091E3  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00A091E7  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00A091EC  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00A091F0  49 8B D7                        mov rdx, r15
00A091F3  8B C7                           mov eax, edi
00A091F5  48 8D 0C 80                     lea rcx, [rax + rax*4]
00A091F9  49 8D 04 8E                     lea rax, [r14 + rcx*4]
00A091FD  49 8B CC                        mov rcx, r12
00A09200  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A09205  E8 8E 1E 00 00                  call 0x140a0b098
00A0920A  33 D2                           xor edx, edx
00A0920C  8B D8                           mov ebx, eax
00A0920E  85 C0                           test eax, eax
00A09210  0F 85 87 02 00 00               jne 0x140a0949d
00A09216  FF C7                           inc edi
00A09218  EB B7                           jmp 0x140a091d1
00A0921A  45 8B 07                        mov r8d, dword ptr [r15]
00A0921D  45 33 C9                        xor r9d, r9d
00A09220  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
00A09224  49 8B CC                        mov rcx, r12
00A09227  E8 00 08 00 00                  call 0x140a09a2c
00A0922C  33 C9                           xor ecx, ecx
00A0922E  8B D8                           mov ebx, eax
00A09230  85 C0                           test eax, eax
00A09232  0F 85 FC 01 00 00               jne 0x140a09434
00A09238  FF C7                           inc edi
00A0923A  49 83 C7 04                     add r15, 4
00A0923E  E9 39 FF FF FF                  jmp 0x140a0917c
00A09243  66 41 39 4D 00                  cmp word ptr [r13], cx
00A09248  0F 84 B3 FE FF FF               je 0x140a09101
00A0924E  45 33 C0                        xor r8d, r8d
00A09251  48 8B D7                        mov rdx, rdi
00A09254  49 8B CC                        mov rcx, r12
00A09257  E8 3C 0C 00 00                  call 0x140a09e98
00A0925C  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A09260  33 C9                           xor ecx, ecx
00A09262  48 FF C0                        inc rax
00A09265  66 39 0C 47                     cmp word ptr [rdi + rax*2], cx
00A09269  75 F7                           jne 0x140a09262
00A0926B  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00A0926F  48 83 C7 02                     add rdi, 2
00A09273  66 39 0F                        cmp word ptr [rdi], cx
00A09276  75 D6                           jne 0x140a0924e
00A09278  E9 84 FE FF FF                  jmp 0x140a09101
00A0927D  85 C0                           test eax, eax
00A0927F  0F 89 00 FF FF FF               jns 0x140a09185
00A09285  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A0928A  48 85 C0                        test rax, rax
00A0928D  0F 85 3B 02 00 00               jne 0x140a094ce
00A09293  4D 85 ED                        test r13, r13
00A09296  0F 85 41 02 00 00               jne 0x140a094dd
00A0929C  4D 85 F6                        test r14, r14
00A0929F  0F 85 47 02 00 00               jne 0x140a094ec
00A092A5  48 85 F6                        test rsi, rsi
00A092A8  0F 85 4D 02 00 00               jne 0x140a094fb
00A092AE  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00A092B3  48 85 C9                        test rcx, rcx
00A092B6  0F 85 4E 02 00 00               jne 0x140a0950a
00A092BC  8B C3                           mov eax, ebx
00A092BE  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00A092C2  48 33 CC                        xor rcx, rsp
00A092C5  E8 76 33 CA FF                  call 0x1406ac640
00A092CA  48 8B 9C 24 C0 01 00 00         mov rbx, qword ptr [rsp + 0x1c0]
00A092D2  48 81 C4 70 01 00 00            add rsp, 0x170
00A092D9  41 5F                           pop r15
00A092DB  41 5E                           pop r14
00A092DD  41 5D                           pop r13
00A092DF  41 5C                           pop r12
00A092E1  5F                              pop rdi
00A092E2  5E                              pop rsi
00A092E3  5D                              pop rbp
00A092E4  C3                              ret
00A092E5  CC                              int3
00A092E6  85 C0                           test eax, eax
00A092E8  78 9B                           js 0x140a09285
00A092EA  45 33 C9                        xor r9d, r9d
00A092ED  49 8B D7                        mov rdx, r15
00A092F0  49 8B CC                        mov rcx, r12
00A092F3  45 8D 41 10                     lea r8d, [r9 + 0x10]
00A092F7  E8 30 07 00 00                  call 0x140a09a2c
00A092FC  8B D8                           mov ebx, eax
00A092FE  85 C0                           test eax, eax
00A09300  78 83                           js 0x140a09285
00A09302  41 B8 01 00 00 00               mov r8d, 1
00A09308  49 8B D7                        mov rdx, r15
00A0930B  49 8B CC                        mov rcx, r12
00A0930E  E8 CD 48 E2 FF                  call 0x14082dbe0
00A09313  E9 6D FF FF FF                  jmp 0x140a09285
00A09318  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A0931D  EB 9D                           jmp 0x140a092bc
00A0931F  4C 8D 4D 10                     lea r9, [rbp + 0x10]
00A09323  48 8B D7                        mov rdx, rdi
00A09326  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00A0932A  49 8B CC                        mov rcx, r12
00A0932D  E8 82 3F EF FF                  call 0x1408fd2b4
00A09332  8B D8                           mov ebx, eax
00A09334  85 C0                           test eax, eax
00A09336  0F 88 72 FF FF FF               js 0x140a092ae
00A0933C  4C 8B CF                        mov r9, rdi
00A0933F  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00A09343  48 8D 55 10                     lea rdx, [rbp + 0x10]
00A09347  49 8B CC                        mov rcx, r12
00A0934A  E8 F1 2B E2 FF                  call 0x14082bf40
00A0934F  33 C9                           xor ecx, ecx
00A09351  8B D8                           mov ebx, eax
00A09353  85 C0                           test eax, eax
00A09355  0F 89 DD FC FF FF               jns 0x140a09038
00A0935B  E9 4E FF FF FF                  jmp 0x140a092ae
00A09360  48 85 F6                        test rsi, rsi
00A09363  0F 84 8F B5 12 00               je 0x140b348f8
00A09369  33 D2                           xor edx, edx
00A0936B  48 8B CE                        mov rcx, rsi
00A0936E  E8 FD 94 17 00                  call 0x140b82870
00A09373  90                              nop
00A09374  E9 7F B5 12 00                  jmp 0x140b348f8
00A09379  83 7D 88 12                     cmp dword ptr [rbp - 0x78], 0x12
00A0937D  0F 85 A5 B5 12 00               jne 0x140b34928
00A09383  83 7C 24 60 02                  cmp dword ptr [rsp + 0x60], 2
00A09388  0F 82 9A B5 12 00               jb 0x140b34928
00A0938E  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00A09392  48 D1 E8                        shr rax, 1
00A09395  66 39 4C 46 FE                  cmp word ptr [rsi + rax*2 - 2], cx
00A0939A  0F 85 88 B5 12 00               jne 0x140b34928
00A093A0  4D 8B C7                        mov r8, r15
00A093A3  48 8B D6                        mov rdx, rsi
00A093A6  49 8B CC                        mov rcx, r12
00A093A9  E8 7E 5F E2 FF                  call 0x14082f32c
00A093AE  33 C9                           xor ecx, ecx
00A093B0  8B D8                           mov ebx, eax
00A093B2  85 C0                           test eax, eax
00A093B4  0F 88 EB FE FF FF               js 0x140a092a5
00A093BA  E9 73 B5 12 00                  jmp 0x140b34932
00A093BF  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
00A093C3  B8 FF FF FF FF                  mov eax, 0xffffffff
00A093C8  48 03 DB                        add rbx, rbx
00A093CB  48 3B D8                        cmp rbx, rax
00A093CE  0F 87 95 B5 12 00               ja 0x140b34969
00A093D4  4D 85 ED                        test r13, r13
00A093D7  0F 84 5D B5 12 00               je 0x140b3493a
00A093DD  33 D2                           xor edx, edx
00A093DF  49 8B CD                        mov rcx, r13
00A093E2  E8 89 94 17 00                  call 0x140b82870
00A093E7  90                              nop
00A093E8  E9 4D B5 12 00                  jmp 0x140b3493a
00A093ED  8B 5C 24 6C                     mov ebx, dword ptr [rsp + 0x6c]
00A093F1  B8 FF FF FF FF                  mov eax, 0xffffffff
00A093F6  48 03 DB                        add rbx, rbx
00A093F9  48 3B D8                        cmp rbx, rax
00A093FC  0F 87 9F B5 12 00               ja 0x140b349a1
00A09402  4D 85 FF                        test r15, r15
00A09405  0F 84 68 B5 12 00               je 0x140b34973
00A0940B  33 D2                           xor edx, edx
00A0940D  49 8B CF                        mov rcx, r15
00A09410  E8 5B 94 17 00                  call 0x140b82870
00A09415  90                              nop
00A09416  E9 58 B5 12 00                  jmp 0x140b34973
00A0941B  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00A09420  66 41 39 0F                     cmp word ptr [r15], cx
00A09424  0F 84 32 FD FF FF               je 0x140a0915c
00A0942A  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00A0942F  E9 77 B5 12 00                  jmp 0x140b349ab
00A09434  3D 34 00 00 C0                  cmp eax, 0xc0000034
00A09439  0F 84 F9 FD FF FF               je 0x140a09238
00A0943F  3D 0D 00 00 C0                  cmp eax, 0xc000000d
00A09444  0F 84 EE FD FF FF               je 0x140a09238
00A0944A  3D BB 00 00 C0                  cmp eax, 0xc00000bb
00A0944F  0F 85 28 FE FF FF               jne 0x140a0927d
00A09455  E9 DE FD FF FF                  jmp 0x140a09238
00A0945A  8B 7C 24 64                     mov edi, dword ptr [rsp + 0x64]
00A0945E  B8 FF FF FF FF                  mov eax, 0xffffffff
00A09463  48 8D 1C BF                     lea rbx, [rdi + rdi*4]
00A09467  48 C1 E3 02                     shl rbx, 2
00A0946B  48 3B D8                        cmp rbx, rax
00A0946E  0F 87 2D B5 12 00               ja 0x140b349a1
00A09474  4D 85 F6                        test r14, r14
00A09477  0F 84 83 B5 12 00               je 0x140b34a00
00A0947D  33 D2                           xor edx, edx
00A0947F  49 8B CE                        mov rcx, r14
00A09482  E8 E9 93 17 00                  call 0x140b82870
00A09487  90                              nop
00A09488  E9 73 B5 12 00                  jmp 0x140b34a00
00A0948D  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A09492  0F 85 ED FD FF FF               jne 0x140a09285
00A09498  E9 32 FD FF FF                  jmp 0x140a091cf
00A0949D  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A094A2  0F 84 6E FD FF FF               je 0x140a09216
00A094A8  3D 22 00 00 C0                  cmp eax, 0xc0000022
00A094AD  0F 84 63 FD FF FF               je 0x140a09216
00A094B3  3D 16 00 00 C0                  cmp eax, 0xc0000016
00A094B8  0F 84 58 FD FF FF               je 0x140a09216
00A094BE  3D BB 00 00 C0                  cmp eax, 0xc00000bb
00A094C3  0F 85 1D FE FF FF               jne 0x140a092e6
00A094C9  E9 48 FD FF FF                  jmp 0x140a09216
00A094CE  33 D2                           xor edx, edx
00A094D0  48 8B C8                        mov rcx, rax
00A094D3  E8 98 93 17 00                  call 0x140b82870
00A094D8  E9 B6 FD FF FF                  jmp 0x140a09293
00A094DD  33 D2                           xor edx, edx
00A094DF  49 8B CD                        mov rcx, r13
00A094E2  E8 89 93 17 00                  call 0x140b82870
00A094E7  E9 B0 FD FF FF                  jmp 0x140a0929c
00A094EC  33 D2                           xor edx, edx
00A094EE  49 8B CE                        mov rcx, r14
00A094F1  E8 7A 93 17 00                  call 0x140b82870
00A094F6  E9 AA FD FF FF                  jmp 0x140a092a5
00A094FB  33 D2                           xor edx, edx
00A094FD  48 8B CE                        mov rcx, rsi
00A09500  E8 6B 93 17 00                  call 0x140b82870
00A09505  E9 A4 FD FF FF                  jmp 0x140a092ae
00A0950A  E8 A1 3D CA FF                  call 0x1406ad2b0
00A0950F  E9 A8 FD FF FF                  jmp 0x140a092bc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _CmDeleteDeviceWorker(__int64 a1, __int64 a2, unsigned __int16 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned int v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int8 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned __int64 v_stack_p70;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 4200405)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m128 = a2;
    a1 = 0;
    v_stack_m130 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    v_stack_m13C = 0;
    v_stack_m11C = 0;
    v_stack_m148 = 0;
    v_stack_m120 = 0;
    if (a3 != 0) goto loc_00A09318;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_m130;
    v_stack_m180 = 0;
    a4 = 0;
    v_stack_m188 = 0x2010002ULL;
    result = _CmOpenDeviceRegKey(0, a2, a1 + 16, a4);
    a1 = 0;
    if (sign_flag) goto loc_00A092AE;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_m148;
    v_stack_m148 = 78;
    v_stack_m180 = v_stack_mE8;
    v_stack_m188 = v_stack_m11C;
    result = CmGetDeviceRegProp(0, a2, v_stack_m130, 0 + 37);
    a1 = 0;
    if (!sign_flag) goto loc_00A0931F;
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00A092AE;
loc_00A09038:
    v_stack_m158 = 0;
    v_stack_m160 = v_stack_m148;
    v_stack_m168 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_m120;
    v_stack_m180 = v_rip - 10451665;
    v_stack_m188 = 0;
    result = PnpGetObjectProperty(0, a2, 1, v_stack_m130);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00A09360;
    a1 = 0;
    if (!sign_flag) goto loc_00A09379;
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_00A092A5;
loc_00A092A5:
    if (0 != 0) goto loc_00A094FB;
loc_00A092AE:
    if (v_stack_m130 != 0) goto loc_00A0950A;
loc_00A092BC:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, v_stack_m130);
    v_rsp = (v_rsp) + (368);
    return result;
loc_00A09318:
    goto loc_00A092BC;
loc_00A0931F:
    result = _CmGetDeviceContainerIdFromBase(a1, a2, v_stack_mE8, v_stack_m98);
    if (sign_flag) goto loc_00A092AE;
    result = CmRemoveDeviceFromContainer(a1, v_stack_m98, v_stack_mE8, a2);
    a1 = 0;
    if (!sign_flag) goto loc_00A09038;
    goto loc_00A092AE;
loc_00A09360:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, v_stack_mE8, a2);
loc_00A09379:
    result = ((unsigned int)(v_stack_p60)) >> (1);
    result = CmRemovePanelDevice(0, 0, 0, a2);
    a1 = 0;
    if (sign_flag) goto loc_00A092A5;
loc_00A094FB:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, 0, a2);
    goto loc_00A092AE;
loc_00A0950A:
    result = ZwClose(0, a2, 0, a2);
    goto loc_00A092BC;
}
```

## 5. (Beta) C Style

```c
int64_t _CmDeleteDeviceWorker(int64_t Arg1, int64_t Arg2, uint16_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint32_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint8_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m48;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint64_t v_stack_p70;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x4017D5)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m128 = Arg2;
    Arg1 = 0;
    v_stack_m130 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    v_stack_m13C = 0;
    v_stack_m11C = 0;
    v_stack_m148 = 0;
    v_stack_m120 = 0;
    if (Arg3 != 0) goto loc_00A09318;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_m130;
    v_stack_m180 = 0;
    Arg4 = 0;
    v_stack_m188 = 0x2010002ULL;
    result = _CmOpenDeviceRegKey(0, Arg2, Arg1 + 16, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00A092AE;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_m148;
    v_stack_m148 = 78;
    v_stack_m180 = v_stack_mE8;
    v_stack_m188 = v_stack_m11C;
    result = CmGetDeviceRegProp(0, Arg2, v_stack_m130, 0 + 37);
    Arg1 = 0;
    if (!sign_flag) goto loc_00A0931F;
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00A092AE;
loc_00A09038:
    v_stack_m158 = 0;
    v_stack_m160 = v_stack_m148;
    v_stack_m168 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_m120;
    v_stack_m180 = v_rip - 10451665;
    v_stack_m188 = 0;
    result = PnpGetObjectProperty(0, Arg2, 1, v_stack_m130);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00A09360;
    Arg1 = 0;
    if (!sign_flag) goto loc_00A09379;
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_00A092A5;
loc_00A092A5:
    if (0 != 0) goto loc_00A094FB;
loc_00A092AE:
    if (v_stack_m130 != 0) goto loc_00A0950A;
loc_00A092BC:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, v_stack_m130);
    local_rsp = (local_rsp) + (368);
    return result;
loc_00A09318:
    goto loc_00A092BC;
loc_00A0931F:
    result = _CmGetDeviceContainerIdFromBase(Arg1, Arg2, v_stack_mE8, v_stack_m98);
    if (sign_flag) goto loc_00A092AE;
    result = CmRemoveDeviceFromContainer(Arg1, v_stack_m98, v_stack_mE8, Arg2);
    Arg1 = 0;
    if (!sign_flag) goto loc_00A09038;
    goto loc_00A092AE;
loc_00A09360:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, v_stack_mE8, Arg2);
loc_00A09379:
    result = ((uint32_t)(v_stack_p60)) >> (1);
    result = CmRemovePanelDevice(0, 0, 0, Arg2);
    Arg1 = 0;
    if (sign_flag) goto loc_00A092A5;
loc_00A094FB:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, 0, Arg2);
    goto loc_00A092AE;
loc_00A0950A:
    result = ZwClose(0, Arg2, 0, Arg2);
    goto loc_00A092BC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A08F48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
