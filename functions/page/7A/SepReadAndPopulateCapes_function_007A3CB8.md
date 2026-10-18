# SepReadAndPopulateCapes

- RVA: `0x007A3CB8`–`0x007A43DB` (길이 `1,827` bytes)
- VA: `0x00000001407A3CB8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D16FC`
- 디코드: `454`개 명령, `1,827/1,827` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x007A3D2E` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (function, `0x006AD390`)
- `0x007A3D5A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007A3D96` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (function, `0x006AD390`)
- `0x007A3DD3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007A3E1A` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x007A3E38` → [SepRegOpenKey](../A3/SepRegOpenKey_function_00A3A6B4.md) (function, `0x00A3A6B4`)
- `0x007A3E61` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (function, `0x006AD390`)
- `0x007A3E90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007A3EA4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007A3ED9` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (function, `0x006AD390`)
- `0x007A3EFC` → [SepRmCapPoolExpand](../../text/60/SepRmCapPoolExpand_function_0060BAE8.md) (function, `0x0060BAE8`)
- `0x007A3F36` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007A3F74` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007A3FAD` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007A3FEC` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007A4009` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007A4038` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007A4051` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007A4094` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x007A40B2` → [SepRegOpenKey](../A3/SepRegOpenKey_function_00A3A6B4.md) (function, `0x00A3A6B4`)
- `0x007A40E8` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007A4137` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007A417D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007A41AF` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007A41EB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007A4225` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007A425D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007A4270` → [SeValidSecurityDescriptor](../8B/SeValidSecurityDescriptor_function_008BED60.md) (function, `0x008BED60`)
- `0x007A42A0` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007A42E0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007A42ED` → [SeValidSecurityDescriptor](../8B/SeValidSecurityDescriptor_function_008BED60.md) (function, `0x008BED60`)
- `0x007A430E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007A436E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007A4380` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007A439E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007A43B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007A43C1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SepBuildCapPolicyTable](../../text/60/SepBuildCapPolicyTable_function_0060B8F0.md) at `0x0060B97D`

### Static image references
- `0x007A3CD4` → RVA `0x00E0A740` (`.data`; read)
- `0x007A3DFE` → RVA `0x00B06270` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007A3E09` → RVA `0x00B06320` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007A3F20` → RVA `0x00FD82C0` (`PAGEDATA`; read)
- `0x007A3F54` → RVA `0x00FD8648` (`PAGEDATA`; read)
- `0x007A3F90` → RVA `0x00FD8638` (`PAGEDATA`; read)
- `0x007A3FCB` → RVA `0x00FD8628` (`PAGEDATA`; read)
- `0x007A40D0` → RVA `0x00FD8618` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **33**
  - `0x007A3D2E` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (`PAGE` → `.text`)
  - `0x007A3D5A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007A3D96` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (`PAGE` → `.text`)
  - `0x007A3DD3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007A3E1A` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
  - `0x007A3E61` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (`PAGE` → `.text`)
  - `0x007A3E90` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007A3EA4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007A3ED9` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (`PAGE` → `.text`)
  - `0x007A3EFC` → [SepRmCapPoolExpand](../../text/60/SepRmCapPoolExpand_function_0060BAE8.md) (`PAGE` → `.text`)
  - `0x007A3F36` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007A3F74` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007A3FAD` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007A3FEC` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007A4009` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007A4038` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007A4051` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007A4094` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
  - `0x007A40E8` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007A4137` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007A417D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007A41AF` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007A41EB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007A4225` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007A425D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007A42A0` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007A42E0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007A430E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007A436E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007A4380` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007A439E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007A43B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007A43C1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007A3CB8  40 55                           push rbp
007A3CBA  53                              push rbx
007A3CBB  56                              push rsi
007A3CBC  57                              push rdi
007A3CBD  41 54                           push r12
007A3CBF  41 55                           push r13
007A3CC1  41 56                           push r14
007A3CC3  41 57                           push r15
007A3CC5  48 8D AC 24 98 FB FF FF         lea rbp, [rsp - 0x468]
007A3CCD  48 81 EC 68 05 00 00            sub rsp, 0x568
007A3CD4  48 8B 05 65 6A 66 00            mov rax, qword ptr [rip + 0x666a65]
007A3CDB  48 33 C4                        xor rax, rsp
007A3CDE  48 89 85 50 04 00 00            mov qword ptr [rbp + 0x450], rax
007A3CE5  33 C0                           xor eax, eax
007A3CE7  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
007A3CEC  44 8B F0                        mov r14d, eax
007A3CEF  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
007A3CF3  88 44 24 30                     mov byte ptr [rsp + 0x30], al
007A3CF7  4C 8D BD 20 02 00 00            lea r15, [rbp + 0x220]
007A3CFE  8B F8                           mov edi, eax
007A3D00  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007A3D05  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
007A3D0A  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A3D0F  44 8B EA                        mov r13d, edx
007A3D12  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007A3D17  41 BC 30 02 00 00               mov r12d, 0x230
007A3D1D  41 8D 56 02                     lea edx, [r14 + 2]
007A3D21  45 8B CC                        mov r9d, r12d
007A3D24  4C 8D 85 20 02 00 00            lea r8, [rbp + 0x220]
007A3D2B  48 8B F1                        mov rsi, rcx
007A3D2E  E8 5D 96 F0 FF                  call 0x1406ad390
007A3D33  8B D8                           mov ebx, eax
007A3D35  85 C0                           test eax, eax
007A3D37  79 6C                           jns 0x1407a3da5
007A3D39  3D 05 00 00 80                  cmp eax, 0x80000005
007A3D3E  74 0B                           je 0x1407a3d4b
007A3D40  3D 23 00 00 C0                  cmp eax, 0xc0000023
007A3D45  0F 85 14 06 00 00               jne 0x1407a435f
007A3D4B  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
007A3D4F  B9 00 01 00 00                  mov ecx, 0x100
007A3D54  41 B8 53 65 53 70               mov r8d, 0x70536553
007A3D5A  E8 91 E3 3D 00                  call 0x140b820f0
007A3D5F  4C 8B F8                        mov r15, rax
007A3D62  48 85 C0                        test rax, rax
007A3D65  75 0D                           jne 0x1407a3d74
007A3D67  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007A3D6C  44 8A E7                        mov r12b, dil
007A3D6F  E9 F0 05 00 00                  jmp 0x1407a4364
007A3D74  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
007A3D79  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A3D7E  45 8B CC                        mov r9d, r12d
007A3D81  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007A3D86  4D 8B C7                        mov r8, r15
007A3D89  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
007A3D8E  BA 02 00 00 00                  mov edx, 2
007A3D93  48 8B CE                        mov rcx, rsi
007A3D96  E8 F5 95 F0 FF                  call 0x1406ad390
007A3D9B  8B D8                           mov ebx, eax
007A3D9D  85 C0                           test eax, eax
007A3D9F  0F 88 BA 05 00 00               js 0x1407a435f
007A3DA5  41 8B 47 14                     mov eax, dword ptr [r15 + 0x14]
007A3DA9  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
007A3DAD  85 C0                           test eax, eax
007A3DAF  75 0A                           jne 0x1407a3dbb
007A3DB1  45 33 ED                        xor r13d, r13d
007A3DB4  33 C0                           xor eax, eax
007A3DB6  E9 90 05 00 00                  jmp 0x1407a434b
007A3DBB  6B F0 38                        imul esi, eax, 0x38
007A3DBE  B9 00 01 00 00                  mov ecx, 0x100
007A3DC3  41 8D 45 12                     lea eax, [r13 + 0x12]
007A3DC7  41 B8 53 65 53 70               mov r8d, 0x70536553
007A3DCD  8B D0                           mov edx, eax
007A3DCF  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
007A3DD3  E8 18 E3 3D 00                  call 0x140b820f0
007A3DD8  48 8B F8                        mov rdi, rax
007A3DDB  48 85 C0                        test rax, rax
007A3DDE  75 0A                           jne 0x1407a3dea
007A3DE0  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007A3DE5  E9 75 05 00 00                  jmp 0x1407a435f
007A3DEA  44 8B 6C 24 4C                  mov r13d, dword ptr [rsp + 0x4c]
007A3DEF  33 C0                           xor eax, eax
007A3DF1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
007A3DF5  41 3B C5                        cmp eax, r13d
007A3DF8  0F 83 2A 02 00 00               jae 0x1407a4028
007A3DFE  4C 8D 0D 6B 24 36 00            lea r9, [rip + 0x36246b]
007A3E05  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A3E09  4C 8D 05 10 25 36 00            lea r8, [rip + 0x362510]
007A3E10  BA 57 01 00 00                  mov edx, 0x157
007A3E15  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
007A3E1A  E8 21 BD C6 FF                  call 0x14040fb40
007A3E1F  8B D8                           mov ebx, eax
007A3E21  85 C0                           test eax, eax
007A3E23  0F 88 36 05 00 00               js 0x1407a435f
007A3E29  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
007A3E2E  BA 01 02 00 00                  mov edx, 0x201
007A3E33  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
007A3E38  E8 77 68 29 00                  call 0x140a3a6b4
007A3E3D  8B D8                           mov ebx, eax
007A3E3F  85 C0                           test eax, eax
007A3E41  0F 88 18 05 00 00               js 0x1407a435f
007A3E47  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A3E4C  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A3E51  45 8B CC                        mov r9d, r12d
007A3E54  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007A3E59  4D 8B C7                        mov r8, r15
007A3E5C  BA 02 00 00 00                  mov edx, 2
007A3E61  E8 2A 95 F0 FF                  call 0x1406ad390
007A3E66  8B D8                           mov ebx, eax
007A3E68  85 C0                           test eax, eax
007A3E6A  79 7C                           jns 0x1407a3ee8
007A3E6C  3D 05 00 00 80                  cmp eax, 0x80000005
007A3E71  74 0B                           je 0x1407a3e7e
007A3E73  3D 23 00 00 C0                  cmp eax, 0xc0000023
007A3E78  0F 85 E1 04 00 00               jne 0x1407a435f
007A3E7E  44 8A 64 24 30                  mov r12b, byte ptr [rsp + 0x30]
007A3E83  45 84 E4                        test r12b, r12b
007A3E86  74 0D                           je 0x1407a3e95
007A3E88  BA 53 65 53 70                  mov edx, 0x70536553
007A3E8D  49 8B CF                        mov rcx, r15
007A3E90  E8 DB E9 3D 00                  call 0x140b82870
007A3E95  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
007A3E99  B9 00 01 00 00                  mov ecx, 0x100
007A3E9E  41 B8 53 65 53 70               mov r8d, 0x70536553
007A3EA4  E8 47 E2 3D 00                  call 0x140b820f0
007A3EA9  4C 8B F8                        mov r15, rax
007A3EAC  48 85 C0                        test rax, rax
007A3EAF  0F 84 69 01 00 00               je 0x1407a401e
007A3EB5  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
007A3EBA  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A3EBF  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A3EC4  45 8B CC                        mov r9d, r12d
007A3EC7  4D 8B C7                        mov r8, r15
007A3ECA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007A3ECF  BA 02 00 00 00                  mov edx, 2
007A3ED4  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
007A3ED9  E8 B2 94 F0 FF                  call 0x1406ad390
007A3EDE  8B D8                           mov ebx, eax
007A3EE0  85 C0                           test eax, eax
007A3EE2  0F 88 77 04 00 00               js 0x1407a435f
007A3EE8  41 8B 5F 28                     mov ebx, dword ptr [r15 + 0x28]
007A3EEC  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
007A3EF0  83 C3 12                        add ebx, 0x12
007A3EF3  3B D8                           cmp ebx, eax
007A3EF5  76 1C                           jbe 0x1407a3f13
007A3EF7  8B D3                           mov edx, ebx
007A3EF9  48 8B CF                        mov rcx, rdi
007A3EFC  E8 E7 7B E6 FF                  call 0x14060bae8
007A3F01  48 8B F8                        mov rdi, rax
007A3F04  48 85 C0                        test rax, rax
007A3F07  0F 84 D3 FE FF FF               je 0x1407a3de0
007A3F0D  8B C3                           mov eax, ebx
007A3F0F  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
007A3F13  48 8D 4C 24 34                  lea rcx, [rsp + 0x34]
007A3F18  4C 8B CF                        mov r9, rdi
007A3F1B  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
007A3F20  48 8D 15 99 43 83 00            lea rdx, [rip + 0x834399]
007A3F27  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A3F2C  41 B8 02 00 00 00               mov r8d, 2
007A3F32  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A3F36  E8 75 94 F0 FF                  call 0x1406ad3b0
007A3F3B  8B D8                           mov ebx, eax
007A3F3D  85 C0                           test eax, eax
007A3F3F  0F 88 1A 04 00 00               js 0x1407a435f
007A3F45  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A3F4A  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A3F4F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007A3F54  48 8D 15 ED 46 83 00            lea rdx, [rip + 0x8346ed]
007A3F5B  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
007A3F5F  FF C6                           inc esi
007A3F61  83 E6 FE                        and esi, 0xfffffffe
007A3F64  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A3F68  03 77 08                        add esi, dword ptr [rdi + 8]
007A3F6B  4C 8B CF                        mov r9, rdi
007A3F6E  41 B8 02 00 00 00               mov r8d, 2
007A3F74  E8 37 94 F0 FF                  call 0x1406ad3b0
007A3F79  8B D8                           mov ebx, eax
007A3F7B  85 C0                           test eax, eax
007A3F7D  0F 88 DC 03 00 00               js 0x1407a435f
007A3F83  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A3F88  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A3F8D  03 77 08                        add esi, dword ptr [rdi + 8]
007A3F90  48 8D 15 A1 46 83 00            lea rdx, [rip + 0x8346a1]
007A3F97  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007A3F9C  4C 8B CF                        mov r9, rdi
007A3F9F  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
007A3FA3  41 B8 02 00 00 00               mov r8d, 2
007A3FA9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A3FAD  E8 FE 93 F0 FF                  call 0x1406ad3b0
007A3FB2  8B D8                           mov ebx, eax
007A3FB4  85 C0                           test eax, eax
007A3FB6  0F 88 A3 03 00 00               js 0x1407a435f
007A3FBC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A3FC1  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A3FC6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007A3FCB  48 8D 15 56 46 83 00            lea rdx, [rip + 0x834656]
007A3FD2  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
007A3FD6  83 C6 07                        add esi, 7
007A3FD9  83 E6 F8                        and esi, 0xfffffff8
007A3FDC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A3FE0  03 77 08                        add esi, dword ptr [rdi + 8]
007A3FE3  4C 8B CF                        mov r9, rdi
007A3FE6  41 B8 02 00 00 00               mov r8d, 2
007A3FEC  E8 BF 93 F0 FF                  call 0x1406ad3b0
007A3FF1  8B D8                           mov ebx, eax
007A3FF3  85 C0                           test eax, eax
007A3FF5  0F 88 64 03 00 00               js 0x1407a435f
007A3FFB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A4000  83 C6 07                        add esi, 7
007A4003  83 E6 F8                        and esi, 0xfffffff8
007A4006  03 77 08                        add esi, dword ptr [rdi + 8]
007A4009  E8 A2 92 F0 FF                  call 0x1406ad2b0
007A400E  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
007A4012  4C 21 74 24 40                  and qword ptr [rsp + 0x40], r14
007A4017  FF C0                           inc eax
007A4019  E9 D3 FD FF FF                  jmp 0x1407a3df1
007A401E  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007A4023  E9 3C 03 00 00                  jmp 0x1407a4364
007A4028  41 B8 53 65 53 70               mov r8d, 0x70536553
007A402E  8B D6                           mov edx, esi
007A4030  B9 00 01 00 00                  mov ecx, 0x100
007A4035  44 8B E6                        mov r12d, esi
007A4038  E8 B3 E0 3D 00                  call 0x140b820f0
007A403D  4C 8B F0                        mov r14, rax
007A4040  48 85 C0                        test rax, rax
007A4043  0F 84 97 FD FF FF               je 0x1407a3de0
007A4049  45 8B C4                        mov r8d, r12d
007A404C  33 D2                           xor edx, edx
007A404E  48 8B C8                        mov rcx, rax
007A4051  E8 EA 2B F2 FF                  call 0x1406c6c40
007A4056  49 6B F5 38                     imul rsi, r13, 0x38
007A405A  4B 8D 04 34                     lea rax, [r12 + r14]
007A405E  49 03 F6                        add rsi, r14
007A4061  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
007A4066  45 33 E4                        xor r12d, r12d
007A4069  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
007A406E  45 3B E5                        cmp r12d, r13d
007A4071  0F 83 BD 02 00 00               jae 0x1407a4334
007A4077  4C 8D 0D F2 21 36 00            lea r9, [rip + 0x3621f2]
007A407E  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
007A4083  4C 8D 05 96 22 36 00            lea r8, [rip + 0x362296]
007A408A  BA 57 01 00 00                  mov edx, 0x157
007A408F  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
007A4094  E8 A7 BA C6 FF                  call 0x14040fb40
007A4099  8B D8                           mov ebx, eax
007A409B  85 C0                           test eax, eax
007A409D  0F 88 BC 02 00 00               js 0x1407a435f
007A40A3  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
007A40A8  BA 01 02 00 00                  mov edx, 0x201
007A40AD  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
007A40B2  E8 FD 65 29 00                  call 0x140a3a6b4
007A40B7  8B D8                           mov ebx, eax
007A40B9  85 C0                           test eax, eax
007A40BB  0F 88 9E 02 00 00               js 0x1407a435f
007A40C1  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A40C6  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A40CB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007A40D0  48 8D 15 41 45 83 00            lea rdx, [rip + 0x834541]
007A40D7  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
007A40DB  4C 8B CF                        mov r9, rdi
007A40DE  41 B8 02 00 00 00               mov r8d, 2
007A40E4  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A40E8  E8 C3 92 F0 FF                  call 0x1406ad3b0
007A40ED  8B D8                           mov ebx, eax
007A40EF  85 C0                           test eax, eax
007A40F1  0F 88 68 02 00 00               js 0x1407a435f
007A40F7  83 7F 08 04                     cmp dword ptr [rdi + 8], 4
007A40FB  0F 85 2C 02 00 00               jne 0x1407a432d
007A4101  41 8B C4                        mov eax, r12d
007A4104  48 8D 15 B5 41 83 00            lea rdx, [rip + 0x8341b5]
007A410B  4C 6B E0 38                     imul r12, rax, 0x38
007A410F  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007A4112  4C 8B CF                        mov r9, rdi
007A4115  41 B8 02 00 00 00               mov r8d, 2
007A411B  43 89 44 34 30                  mov dword ptr [r12 + r14 + 0x30], eax
007A4120  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A4125  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A412A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007A412F  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
007A4133  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A4137  E8 74 92 F0 FF                  call 0x1406ad3b0
007A413C  8B D8                           mov ebx, eax
007A413E  85 C0                           test eax, eax
007A4140  0F 88 19 02 00 00               js 0x1407a435f
007A4146  8B 47 08                        mov eax, dword ptr [rdi + 8]
007A4149  48 FF C6                        inc rsi
007A414C  48 83 E6 FE                     and rsi, 0xfffffffffffffffe
007A4150  48 03 C6                        add rax, rsi
007A4153  48 3B 44 24 50                  cmp rax, qword ptr [rsp + 0x50]
007A4158  0F 87 C8 01 00 00               ja 0x1407a4326
007A415E  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
007A4162  48 8D 57 0C                     lea rdx, [rdi + 0xc]
007A4166  66 43 89 44 34 02               mov word ptr [r12 + r14 + 2], ax
007A416C  48 8B CE                        mov rcx, rsi
007A416F  66 43 89 04 34                  mov word ptr [r12 + r14], ax
007A4174  4B 89 74 34 08                  mov qword ptr [r12 + r14 + 8], rsi
007A4179  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
007A417D  E8 BE 26 F2 FF                  call 0x1406c6840
007A4182  8B 47 08                        mov eax, dword ptr [rdi + 8]
007A4185  48 8D 15 BC 44 83 00            lea rdx, [rip + 0x8344bc]
007A418C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A4191  48 03 F0                        add rsi, rax
007A4194  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A4199  4C 8B CF                        mov r9, rdi
007A419C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007A41A1  41 B8 02 00 00 00               mov r8d, 2
007A41A7  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
007A41AB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A41AF  E8 FC 91 F0 FF                  call 0x1406ad3b0
007A41B4  8B D8                           mov ebx, eax
007A41B6  85 C0                           test eax, eax
007A41B8  0F 88 A1 01 00 00               js 0x1407a435f
007A41BE  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
007A41C1  48 8D 04 0E                     lea rax, [rsi + rcx]
007A41C5  48 3B 44 24 50                  cmp rax, qword ptr [rsp + 0x50]
007A41CA  0F 87 56 01 00 00               ja 0x1407a4326
007A41D0  43 89 4C 34 10                  mov dword ptr [r12 + r14 + 0x10], ecx
007A41D5  83 7F 08 00                     cmp dword ptr [rdi + 8], 0
007A41D9  74 17                           je 0x1407a41f2
007A41DB  4B 89 74 34 18                  mov qword ptr [r12 + r14 + 0x18], rsi
007A41E0  48 8D 57 0C                     lea rdx, [rdi + 0xc]
007A41E4  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
007A41E8  48 8B CE                        mov rcx, rsi
007A41EB  E8 50 26 F2 FF                  call 0x1406c6840
007A41F0  EB 06                           jmp 0x1407a41f8
007A41F2  4B 83 64 34 18 00               and qword ptr [r12 + r14 + 0x18], 0
007A41F8  8B 47 08                        mov eax, dword ptr [rdi + 8]
007A41FB  48 8D 15 36 44 83 00            lea rdx, [rip + 0x834436]
007A4202  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A4207  48 03 F0                        add rsi, rax
007A420A  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A420F  4C 8B CF                        mov r9, rdi
007A4212  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007A4217  41 B8 02 00 00 00               mov r8d, 2
007A421D  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
007A4221  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A4225  E8 86 91 F0 FF                  call 0x1406ad3b0
007A422A  8B D8                           mov ebx, eax
007A422C  85 C0                           test eax, eax
007A422E  0F 88 2B 01 00 00               js 0x1407a435f
007A4234  8B 47 08                        mov eax, dword ptr [rdi + 8]
007A4237  48 83 C6 07                     add rsi, 7
007A423B  48 83 E6 F8                     and rsi, 0xfffffffffffffff8
007A423F  48 03 C6                        add rax, rsi
007A4242  48 3B 44 24 50                  cmp rax, qword ptr [rsp + 0x50]
007A4247  0F 87 D9 00 00 00               ja 0x1407a4326
007A424D  4B 89 74 34 20                  mov qword ptr [r12 + r14 + 0x20], rsi
007A4252  48 8D 57 0C                     lea rdx, [rdi + 0xc]
007A4256  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
007A425A  48 8B CE                        mov rcx, rsi
007A425D  E8 DE 25 F2 FF                  call 0x1406c6840
007A4262  8B 47 08                        mov eax, dword ptr [rdi + 8]
007A4265  8B C8                           mov ecx, eax
007A4267  4B 8B 54 34 20                  mov rdx, qword ptr [r12 + r14 + 0x20]
007A426C  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
007A4270  E8 EB AA 11 00                  call 0x1408bed60
007A4275  84 C0                           test al, al
007A4277  74 7D                           je 0x1407a42f6
007A4279  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A427E  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007A4283  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007A4288  48 8D 15 99 43 83 00            lea rdx, [rip + 0x834399]
007A428F  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
007A4293  4C 8B CF                        mov r9, rdi
007A4296  41 B8 02 00 00 00               mov r8d, 2
007A429C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007A42A0  E8 0B 91 F0 FF                  call 0x1406ad3b0
007A42A5  8B D8                           mov ebx, eax
007A42A7  85 C0                           test eax, eax
007A42A9  0F 88 B0 00 00 00               js 0x1407a435f
007A42AF  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
007A42B3  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
007A42B6  48 83 C0 07                     add rax, 7
007A42BA  48 03 F0                        add rsi, rax
007A42BD  48 83 E6 F8                     and rsi, 0xfffffffffffffff8
007A42C1  48 8D 04 0E                     lea rax, [rsi + rcx]
007A42C5  48 3B 44 24 50                  cmp rax, qword ptr [rsp + 0x50]
007A42CA  77 5A                           ja 0x1407a4326
007A42CC  85 C9                           test ecx, ecx
007A42CE  74 2D                           je 0x1407a42fd
007A42D0  4B 89 74 34 28                  mov qword ptr [r12 + r14 + 0x28], rsi
007A42D5  48 8D 57 0C                     lea rdx, [rdi + 0xc]
007A42D9  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
007A42DD  48 8B CE                        mov rcx, rsi
007A42E0  E8 5B 25 F2 FF                  call 0x1406c6840
007A42E5  4B 8B 54 34 28                  mov rdx, qword ptr [r12 + r14 + 0x28]
007A42EA  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
007A42ED  E8 6E AA 11 00                  call 0x1408bed60
007A42F2  84 C0                           test al, al
007A42F4  75 0D                           jne 0x1407a4303
007A42F6  BB 79 00 00 C0                  mov ebx, 0xc0000079
007A42FB  EB 62                           jmp 0x1407a435f
007A42FD  4B 83 64 34 28 00               and qword ptr [r12 + r14 + 0x28], 0
007A4303  8B 47 08                        mov eax, dword ptr [rdi + 8]
007A4306  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A430B  48 03 F0                        add rsi, rax
007A430E  E8 9D 8F F0 FF                  call 0x1406ad2b0
007A4313  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
007A4319  44 8B 64 24 48                  mov r12d, dword ptr [rsp + 0x48]
007A431E  41 FF C4                        inc r12d
007A4321  E9 43 FD FF FF                  jmp 0x1407a4069
007A4326  BB 23 00 00 C0                  mov ebx, 0xc0000023
007A432B  EB 32                           jmp 0x1407a435f
007A432D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007A4332  EB 2B                           jmp 0x1407a435f
007A4334  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
007A4339  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007A433E  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
007A4343  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007A4348  49 8B C6                        mov rax, r14
007A434B  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007A4350  48 89 01                        mov qword ptr [rcx], rax
007A4353  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
007A4358  44 89 28                        mov dword ptr [rax], r13d
007A435B  85 DB                           test ebx, ebx
007A435D  79 28                           jns 0x1407a4387
007A435F  44 8A 64 24 30                  mov r12b, byte ptr [rsp + 0x30]
007A4364  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
007A4369  48 85 C9                        test rcx, rcx
007A436C  74 05                           je 0x1407a4373
007A436E  E8 3D 8F F0 FF                  call 0x1406ad2b0
007A4373  4D 85 F6                        test r14, r14
007A4376  74 14                           je 0x1407a438c
007A4378  BA 53 65 53 70                  mov edx, 0x70536553
007A437D  49 8B CE                        mov rcx, r14
007A4380  E8 EB E4 3D 00                  call 0x140b82870
007A4385  EB 05                           jmp 0x1407a438c
007A4387  44 8A 64 24 30                  mov r12b, byte ptr [rsp + 0x30]
007A438C  45 84 E4                        test r12b, r12b
007A438F  74 12                           je 0x1407a43a3
007A4391  4D 85 FF                        test r15, r15
007A4394  74 0D                           je 0x1407a43a3
007A4396  BA 53 65 53 70                  mov edx, 0x70536553
007A439B  49 8B CF                        mov rcx, r15
007A439E  E8 CD E4 3D 00                  call 0x140b82870
007A43A3  48 85 FF                        test rdi, rdi
007A43A6  74 0D                           je 0x1407a43b5
007A43A8  BA 53 65 53 70                  mov edx, 0x70536553
007A43AD  48 8B CF                        mov rcx, rdi
007A43B0  E8 BB E4 3D 00                  call 0x140b82870
007A43B5  8B C3                           mov eax, ebx
007A43B7  48 8B 8D 50 04 00 00            mov rcx, qword ptr [rbp + 0x450]
007A43BE  48 33 CC                        xor rcx, rsp
007A43C1  E8 7A 82 F0 FF                  call 0x1406ac640
007A43C6  48 81 C4 68 05 00 00            add rsp, 0x568
007A43CD  41 5F                           pop r15
007A43CF  41 5E                           pop r14
007A43D1  41 5D                           pop r13
007A43D3  41 5C                           pop r12
007A43D5  5F                              pop rdi
007A43D6  5E                              pop rsi
007A43D7  5B                              pop rbx
007A43D8  5D                              pop rbp
007A43D9  C3                              ret
007A43DA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepReadAndPopulateCapes(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m538;
    unsigned __int64 v_stack_m548;
    unsigned __int64 v_stack_m550;
    unsigned __int64 v_stack_m558;
    unsigned int v_stack_m55C;
    unsigned int v_stack_m560;
    unsigned __int64 v_stack_m568;
    unsigned int v_stack_m570;
    unsigned int v_stack_m574;
    unsigned __int8 v_stack_m578;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m580;
    unsigned __int64 v_stack_m588;

    v_rsp = (v_rsp) - (0x568ULL);
    result = (*(unsigned __int64 *)(v_rip + 6711909)) ^ (v_rsp);
    v_stack_m58 = result;
    result = 0;
    v_stack_m550 = a4;
    v_stack_m574 = 0;
    v_stack_m578 = 0;
    v_stack_m568 = 0;
    v_stack_m548 = a3;
    v_stack_m588 = v_stack_m574;
    result = ZwQueryKey(a1, 0 + 2, v_stack_m288, 560);
    if (!sign_flag) goto loc_007A3DA5;
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_007A3D4B;
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_007A435F;
loc_007A3D4B:
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m574), (unsigned int)(0x70536553ULL), 560);
    if (result != 0) goto loc_007A3D74;
    goto loc_007A4364;
loc_007A3D74:
    v_stack_m588 = v_stack_m574;
    v_stack_m578 = 1;
    result = ZwQueryKey(a1, 2, result, (unsigned int)((unsigned int)((unsigned int)(v_stack_m574))));
    if (sign_flag) goto loc_007A435F;
loc_007A3DA5:
    v_stack_m55C = (unsigned int)((unsigned int)(*(unsigned int *)(result + 20)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 20))) != 0) goto loc_007A3DBB;
    v_r13 = 0;
    result = 0;
    goto loc_007A434B;
loc_007A3DBB:
    v_rsi = (unsigned int)((a1) * (0));
    v_stack_m570 = (unsigned int)(v_r13 + 18);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r13 + 18)), (unsigned int)(0x70536553ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m574))));
    if (result != 0) goto loc_007A3DEA;
loc_007A3DE0:
    goto loc_007A435F;
loc_007A3DEA:
    result = 0;
loc_007A3DF1:
    v_stack_m560 = 0;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m55C)))) goto loc_007A4028;
    v_stack_m588 = 0;
    result = RtlStringCbPrintfW(v_stack_m538, 343, v_rip + 3548432, v_rip + 3548267);
    if (sign_flag) goto loc_007A435F;
    result = SepRegOpenKey(v_stack_m538, 513, v_stack_m568, v_rip + 3548267);
    if (sign_flag) goto loc_007A435F;
    v_stack_m588 = v_stack_m574;
    result = ZwQueryKey(v_stack_m568, 2, result, (unsigned int)((unsigned int)((unsigned int)(v_stack_m574))));
    if (!sign_flag) goto loc_007A3EE8;
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_007A3E7E;
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_007A435F;
loc_007A3E7E:
    if ((unsigned __int8)(v_stack_m578) != 0) {
        a2 = 0x70536553ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, result, (unsigned int)((unsigned int)((unsigned int)(v_stack_m574))));
    }
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m574), (unsigned int)(0x70536553ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m574))));
    if (result == 0) goto loc_007A401E;
    v_stack_m588 = v_stack_m574;
    v_stack_m578 = 1;
    result = ZwQueryKey(v_stack_m568, 2, result, (unsigned int)((unsigned int)((unsigned int)(v_stack_m574))));
    if (sign_flag) goto loc_007A435F;
loc_007A3EE8:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 40))) + (18));
    if (((unsigned int)(v_rbx)) <= ((unsigned int)((unsigned int)(v_stack_m570)))) goto loc_007A3F13;
    result = SepRmCapPoolExpand(result, (unsigned int)((unsigned int)(v_rbx)), result, (unsigned int)((unsigned int)((unsigned int)(v_stack_m574))));
    if (result == 0) goto loc_007A3DE0;
    v_stack_m570 = (unsigned int)(v_rbx);
loc_007A3F13:
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (unsigned int)((unsigned int)((unsigned int)(v_rbx)));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602521, 2, result);
    if (sign_flag) goto loc_007A435F;
    v_stack_m580 = v_stack_m574;
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFEULL));
    v_stack_m588 = (unsigned int)((unsigned int)(v_stack_m570));
    v_rsi = (unsigned int)((v_rsi) + (*(unsigned int *)(result + 8)));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8603373, 2, result);
    if (sign_flag) goto loc_007A435F;
    v_rsi = (unsigned int)((v_rsi) + (*(unsigned int *)(result + 8)));
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (unsigned int)((unsigned int)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8603297, 2, result);
    if (sign_flag) goto loc_007A435F;
    v_stack_m580 = v_stack_m574;
    v_rsi = (unsigned int)((v_rsi) + (7));
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFF8ULL));
    v_stack_m588 = (unsigned int)((unsigned int)(v_stack_m570));
    v_rsi = (unsigned int)((v_rsi) + (*(unsigned int *)(result + 8)));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8603222, 2, result);
    if (sign_flag) goto loc_007A435F;
    v_rsi = (unsigned int)((v_rsi) + (7));
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFF8ULL));
    v_rsi = (unsigned int)((v_rsi) + (*(unsigned int *)(result + 8)));
    result = ZwClose(v_stack_m568, v_rip + 8603222, 2, result);
    result = (unsigned int)(((unsigned int)(v_stack_m560)) + 1);
    goto loc_007A3DF1;
loc_007A401E:
    goto loc_007A4364;
loc_007A4028:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x70536553ULL), result);
    if (result == 0) goto loc_007A3DE0;
    a2 = 0;
    result = memset(result, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))), result);
    v_rsi = (v_rsi) * ((unsigned int)(v_stack_m55C));
    v_rsi = (v_rsi) + (result);
    v_stack_m558 = (unsigned int)((unsigned int)(v_rsi)) + result * 1;
    v_r12 = 0;
loc_007A4069:
    v_stack_m560 = 0;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m55C)))) goto loc_007A4334;
    v_stack_m588 = 0;
    result = RtlStringCbPrintfW(v_stack_m538, 343, v_rip + 3547798, v_rip + 3547634);
    if (sign_flag) goto loc_007A435F;
    result = SepRegOpenKey(v_stack_m538, 513, v_stack_m568, v_rip + 3547634);
    if (sign_flag) goto loc_007A435F;
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (unsigned int)((unsigned int)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602945, 2, result);
    if (sign_flag) goto loc_007A435F;
    if ((*(unsigned int *)(result + 8)) != 4) goto loc_007A432D;
    v_r12 = (v_r12) * (0);
    *(unsigned int *)(v_r12 + result * 1 + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)));
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (unsigned int)((unsigned int)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602037, 2, result);
    if (sign_flag) goto loc_007A435F;
    v_rsi = (v_rsi) + 1;
    v_rsi = (v_rsi) & (-2);
    result = ((unsigned int)(*(unsigned int *)(result + 8))) + (v_rsi);
    if (result > v_stack_m558) goto loc_007A4326;
    *(unsigned __int16 *)(v_r12 + result * 1 + 2) = (unsigned __int16)(*(unsigned __int16 *)(result + 8));
    *(unsigned __int16 *)(v_r12 + result * 1) = (unsigned __int16)(*(unsigned __int16 *)(result + 8));
    *(unsigned __int64 *)(v_r12 + result * 1 + 8) = v_rsi;
    result = memcpy(v_rsi, result + 12, (unsigned int)(*(unsigned int *)(result + 8)), result);
    v_rsi = (v_rsi) + ((unsigned int)(*(unsigned int *)(result + 8)));
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (unsigned int)((unsigned int)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602812, 2, result);
    if (sign_flag) goto loc_007A435F;
    if ((v_rsi + (unsigned int)(*(unsigned int *)(result + 8)) * 1) > v_stack_m558) goto loc_007A4326;
    *(unsigned int *)(v_r12 + result * 1 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    if ((*(unsigned int *)(result + 8)) == 0) goto loc_007A41F2;
    *(unsigned __int64 *)(v_r12 + result * 1 + 24) = v_rsi;
    result = memcpy(v_rsi, result + 12, (unsigned int)(*(unsigned int *)(result + 8)), result);
    goto loc_007A41F8;
loc_007A41F2:
loc_007A41F8:
    v_rsi = (v_rsi) + ((unsigned int)(*(unsigned int *)(result + 8)));
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (unsigned int)((unsigned int)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602678, 2, result);
    if (sign_flag) goto loc_007A435F;
    v_rsi = (v_rsi) + (7);
    v_rsi = (v_rsi) & (-8);
    result = ((unsigned int)(*(unsigned int *)(result + 8))) + (v_rsi);
    if (result > v_stack_m558) goto loc_007A4326;
    *(unsigned __int64 *)(v_r12 + result * 1 + 32) = v_rsi;
    result = memcpy(v_rsi, result + 12, (unsigned int)(*(unsigned int *)(result + 8)), result);
    v_stack_m55C = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    result = SeValidSecurityDescriptor((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))), *(unsigned __int64 *)(v_r12 + result * 1 + 32), (unsigned int)(*(unsigned int *)(result + 8)), result);
    if ((unsigned __int8)(result) == 0) goto loc_007A42F6;
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (unsigned int)((unsigned int)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602521, 2, result);
    if (sign_flag) goto loc_007A435F;
    result = ((unsigned int)(v_stack_m55C)) + (7);
    v_rsi = (v_rsi) + (result);
    v_rsi = (v_rsi) & (-8);
    if ((v_rsi + (unsigned int)(*(unsigned int *)(result + 8)) * 1) > v_stack_m558) goto loc_007A4326;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8))) == 0) goto loc_007A42FD;
    *(unsigned __int64 *)(v_r12 + result * 1 + 40) = v_rsi;
    result = memcpy(v_rsi, result + 12, (unsigned int)(*(unsigned int *)(result + 8)), result);
    result = SeValidSecurityDescriptor((unsigned int)(*(unsigned int *)(result + 8)), *(unsigned __int64 *)(v_r12 + result * 1 + 40), (unsigned int)(*(unsigned int *)(result + 8)), result);
    if ((unsigned __int8)(result) != 0) goto loc_007A4303;
loc_007A42F6:
    goto loc_007A435F;
loc_007A42FD:
loc_007A4303:
    v_rsi = (v_rsi) + ((unsigned int)(*(unsigned int *)(result + 8)));
    result = ZwClose(v_stack_m568, *(unsigned __int64 *)(v_r12 + result * 1 + 40), (unsigned int)(*(unsigned int *)(result + 8)), result);
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m560)) + 1);
    goto loc_007A4069;
loc_007A4326:
    goto loc_007A435F;
loc_007A432D:
    goto loc_007A435F;
loc_007A4334:
    v_stack_m548 = v_stack_m548;
    v_stack_m550 = v_stack_m550;
loc_007A434B:
    *(unsigned __int64 *)(v_stack_m550) = result;
    *(unsigned int *)(v_stack_m548) = (unsigned int)((unsigned int)(v_stack_m55C));
    if (!sign_flag) goto loc_007A4387;
loc_007A435F:
loc_007A4364:
    result = v_stack_m548;
    if (v_stack_m568 != 0) {
        result = ZwClose(v_stack_m568, *(unsigned __int64 *)(v_r12 + result * 1 + 40), (unsigned int)(*(unsigned int *)(result + 8)), result);
    }
    if (result == 0) goto loc_007A438C;
    result = ExFreePoolWithTag(result, (unsigned int)(0x70536553ULL), (unsigned int)(*(unsigned int *)(result + 8)), result);
    goto loc_007A438C;
loc_007A4387:
loc_007A438C:
    if ((unsigned __int8)(v_stack_m578) == 0) goto loc_007A43A3;
    if (result != 0) {
        a2 = 0x70536553ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(*(unsigned int *)(result + 8)), result);
    }
    if (result != 0) {
        a2 = 0x70536553ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(*(unsigned int *)(result + 8)), result);
    }
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(*(unsigned int *)(result + 8)), result);
    v_rsp = (v_rsp) + (0x568ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepReadAndPopulateCapes(int64_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m288;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m538;
    uint64_t v_stack_m548;
    uint64_t v_stack_m550;
    uint64_t v_stack_m558;
    uint32_t v_stack_m55C;
    uint32_t v_stack_m560;
    uint64_t v_stack_m568;
    uint32_t v_stack_m570;
    uint32_t v_stack_m574;
    uint8_t v_stack_m578;
    uint64_t v_stack_m58;
    uint64_t v_stack_m580;
    uint64_t v_stack_m588;

    local_rsp = (local_rsp) - (0x568ULL);
    result = (*(uint64_t *)(v_rip + 0x666A65)) ^ (local_rsp);
    v_stack_m58 = result;
    result = 0;
    v_stack_m550 = Arg4;
    v_stack_m574 = 0;
    v_stack_m578 = 0;
    v_stack_m568 = 0;
    v_stack_m548 = Arg3;
    v_stack_m588 = v_stack_m574;
    result = ZwQueryKey(Arg1, 0 + 2, v_stack_m288, 560);
    if (!sign_flag) goto loc_007A3DA5;
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_007A3D4B;
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_007A435F;
loc_007A3D4B:
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m574), (uint32_t)(0x70536553ULL), 560);
    if (result != 0) goto loc_007A3D74;
    goto loc_007A4364;
loc_007A3D74:
    v_stack_m588 = v_stack_m574;
    v_stack_m578 = 1;
    result = ZwQueryKey(Arg1, 2, result, (uint32_t)((uint32_t)((uint32_t)(v_stack_m574))));
    if (sign_flag) goto loc_007A435F;
loc_007A3DA5:
    v_stack_m55C = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x14)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x14))) != 0) goto loc_007A3DBB;
    local_r13 = 0;
    result = 0;
    goto loc_007A434B;
loc_007A3DBB:
    local_rsi = (uint32_t)((Arg1) * (0));
    v_stack_m570 = (uint32_t)(local_r13 + 18);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r13 + 18)), (uint32_t)(0x70536553ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m574))));
    if (result != 0) goto loc_007A3DEA;
loc_007A3DE0:
    goto loc_007A435F;
loc_007A3DEA:
    result = 0;
loc_007A3DF1:
    v_stack_m560 = 0;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m55C)))) goto loc_007A4028;
    v_stack_m588 = 0;
    result = RtlStringCbPrintfW(v_stack_m538, 343, v_rip + 3548432, v_rip + 3548267);
    if (sign_flag) goto loc_007A435F;
    result = SepRegOpenKey(v_stack_m538, 513, v_stack_m568, v_rip + 3548267);
    if (sign_flag) goto loc_007A435F;
    v_stack_m588 = v_stack_m574;
    result = ZwQueryKey(v_stack_m568, 2, result, (uint32_t)((uint32_t)((uint32_t)(v_stack_m574))));
    if (!sign_flag) goto loc_007A3EE8;
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_007A3E7E;
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_007A435F;
loc_007A3E7E:
    if ((uint8_t)(v_stack_m578) != 0) {
        Arg2 = 0x70536553ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, result, (uint32_t)((uint32_t)((uint32_t)(v_stack_m574))));
    }
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m574), (uint32_t)(0x70536553ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m574))));
    if (result == 0) goto loc_007A401E;
    v_stack_m588 = v_stack_m574;
    v_stack_m578 = 1;
    result = ZwQueryKey(v_stack_m568, 2, result, (uint32_t)((uint32_t)((uint32_t)(v_stack_m574))));
    if (sign_flag) goto loc_007A435F;
loc_007A3EE8:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x28))) + (18));
    if (((uint32_t)(local_rbx)) <= ((uint32_t)((uint32_t)(v_stack_m570)))) goto loc_007A3F13;
    result = SepRmCapPoolExpand(result, (uint32_t)((uint32_t)(local_rbx)), result, (uint32_t)((uint32_t)((uint32_t)(v_stack_m574))));
    if (result == 0) goto loc_007A3DE0;
    v_stack_m570 = (uint32_t)(local_rbx);
loc_007A3F13:
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (uint32_t)((uint32_t)((uint32_t)(local_rbx)));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602521, 2, result);
    if (sign_flag) goto loc_007A435F;
    v_stack_m580 = v_stack_m574;
    local_rsi = (uint32_t)((local_rsi) + 1);
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFEULL));
    v_stack_m588 = (uint32_t)((uint32_t)(v_stack_m570));
    local_rsi = (uint32_t)((local_rsi) + (*(uint32_t *)(result + 0x8)));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8603373, 2, result);
    if (sign_flag) goto loc_007A435F;
    local_rsi = (uint32_t)((local_rsi) + (*(uint32_t *)(result + 0x8)));
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (uint32_t)((uint32_t)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8603297, 2, result);
    if (sign_flag) goto loc_007A435F;
    v_stack_m580 = v_stack_m574;
    local_rsi = (uint32_t)((local_rsi) + (7));
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFF8ULL));
    v_stack_m588 = (uint32_t)((uint32_t)(v_stack_m570));
    local_rsi = (uint32_t)((local_rsi) + (*(uint32_t *)(result + 0x8)));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8603222, 2, result);
    if (sign_flag) goto loc_007A435F;
    local_rsi = (uint32_t)((local_rsi) + (7));
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFF8ULL));
    local_rsi = (uint32_t)((local_rsi) + (*(uint32_t *)(result + 0x8)));
    result = ZwClose(v_stack_m568, v_rip + 8603222, 2, result);
    result = (uint32_t)(((uint32_t)(v_stack_m560)) + 1);
    goto loc_007A3DF1;
loc_007A401E:
    goto loc_007A4364;
loc_007A4028:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x70536553ULL), result);
    if (result == 0) goto loc_007A3DE0;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))), result);
    local_rsi = (local_rsi) * ((uint32_t)(v_stack_m55C));
    local_rsi = (local_rsi) + (result);
    v_stack_m558 = (uint32_t)((uint32_t)(local_rsi)) + result * 1;
    local_r12 = 0;
loc_007A4069:
    v_stack_m560 = 0;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m55C)))) goto loc_007A4334;
    v_stack_m588 = 0;
    result = RtlStringCbPrintfW(v_stack_m538, 343, v_rip + 3547798, v_rip + 3547634);
    if (sign_flag) goto loc_007A435F;
    result = SepRegOpenKey(v_stack_m538, 513, v_stack_m568, v_rip + 3547634);
    if (sign_flag) goto loc_007A435F;
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (uint32_t)((uint32_t)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602945, 2, result);
    if (sign_flag) goto loc_007A435F;
    if ((*(uint32_t *)(result + 0x8)) != 4) goto loc_007A432D;
    local_r12 = (local_r12) * (0);
    *(uint32_t *)(local_r12 + result * 1 + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)));
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (uint32_t)((uint32_t)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602037, 2, result);
    if (sign_flag) goto loc_007A435F;
    local_rsi = (local_rsi) + 1;
    local_rsi = (local_rsi) & (-2);
    result = ((uint32_t)(*(uint32_t *)(result + 0x8))) + (local_rsi);
    if (result > v_stack_m558) goto loc_007A4326;
    *(uint16_t *)(local_r12 + result * 1 + 0x2) = (uint16_t)(*(uint16_t *)(result + 0x8));
    *(uint16_t *)(local_r12 + result * 1) = (uint16_t)(*(uint16_t *)(result + 0x8));
    *(uint64_t *)(local_r12 + result * 1 + 0x8) = local_rsi;
    result = memcpy(local_rsi, result + 12, (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    local_rsi = (local_rsi) + ((uint32_t)(*(uint32_t *)(result + 0x8)));
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (uint32_t)((uint32_t)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602812, 2, result);
    if (sign_flag) goto loc_007A435F;
    if ((local_rsi + (uint32_t)(*(uint32_t *)(result + 0x8)) * 1) > v_stack_m558) goto loc_007A4326;
    *(uint32_t *)(local_r12 + result * 1 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    if ((*(uint32_t *)(result + 0x8)) == 0) goto loc_007A41F2;
    *(uint64_t *)(local_r12 + result * 1 + 0x18) = local_rsi;
    result = memcpy(local_rsi, result + 12, (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    goto loc_007A41F8;
loc_007A41F2:
loc_007A41F8:
    local_rsi = (local_rsi) + ((uint32_t)(*(uint32_t *)(result + 0x8)));
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (uint32_t)((uint32_t)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602678, 2, result);
    if (sign_flag) goto loc_007A435F;
    local_rsi = (local_rsi) + (7);
    local_rsi = (local_rsi) & (-8);
    result = ((uint32_t)(*(uint32_t *)(result + 0x8))) + (local_rsi);
    if (result > v_stack_m558) goto loc_007A4326;
    *(uint64_t *)(local_r12 + result * 1 + 0x20) = local_rsi;
    result = memcpy(local_rsi, result + 12, (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    v_stack_m55C = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    result = SeValidSecurityDescriptor((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))), *(uint64_t *)(local_r12 + result * 1 + 0x20), (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    if ((uint8_t)(result) == 0) goto loc_007A42F6;
    v_stack_m580 = v_stack_m574;
    v_stack_m588 = (uint32_t)((uint32_t)(v_stack_m570));
    result = ZwQueryValueKey(v_stack_m568, v_rip + 8602521, 2, result);
    if (sign_flag) goto loc_007A435F;
    result = ((uint32_t)(v_stack_m55C)) + (7);
    local_rsi = (local_rsi) + (result);
    local_rsi = (local_rsi) & (-8);
    if ((local_rsi + (uint32_t)(*(uint32_t *)(result + 0x8)) * 1) > v_stack_m558) goto loc_007A4326;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8))) == 0) goto loc_007A42FD;
    *(uint64_t *)(local_r12 + result * 1 + 0x28) = local_rsi;
    result = memcpy(local_rsi, result + 12, (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    result = SeValidSecurityDescriptor((uint32_t)(*(uint32_t *)(result + 0x8)), *(uint64_t *)(local_r12 + result * 1 + 0x28), (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    if ((uint8_t)(result) != 0) goto loc_007A4303;
loc_007A42F6:
    goto loc_007A435F;
loc_007A42FD:
loc_007A4303:
    local_rsi = (local_rsi) + ((uint32_t)(*(uint32_t *)(result + 0x8)));
    result = ZwClose(v_stack_m568, *(uint64_t *)(local_r12 + result * 1 + 0x28), (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m560)) + 1);
    goto loc_007A4069;
loc_007A4326:
    goto loc_007A435F;
loc_007A432D:
    goto loc_007A435F;
loc_007A4334:
    v_stack_m548 = v_stack_m548;
    v_stack_m550 = v_stack_m550;
loc_007A434B:
    *(uint64_t *)(v_stack_m550) = result;
    *(uint32_t *)(v_stack_m548) = (uint32_t)((uint32_t)(v_stack_m55C));
    if (!sign_flag) goto loc_007A4387;
loc_007A435F:
loc_007A4364:
    result = v_stack_m548;
    if (v_stack_m568 != 0) {
        result = ZwClose(v_stack_m568, *(uint64_t *)(local_r12 + result * 1 + 0x28), (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    }
    if (result == 0) goto loc_007A438C;
    result = ExFreePoolWithTag(result, (uint32_t)(0x70536553ULL), (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    goto loc_007A438C;
loc_007A4387:
loc_007A438C:
    if ((uint8_t)(v_stack_m578) == 0) goto loc_007A43A3;
    if (result != 0) {
        Arg2 = 0x70536553ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    }
    if (result != 0) {
        Arg2 = 0x70536553ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    }
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(*(uint32_t *)(result + 0x8)), result);
    local_rsp = (local_rsp) + (0x568ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x12` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007A3CB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
