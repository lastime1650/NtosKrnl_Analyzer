# CmSetAcpiHwProfile

- RVA: `0x007E2584`–`0x007E2DBE` (길이 `2,106` bytes)
- VA: `0x00000001407E2584`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D6A58`
- 디코드: `495`개 명령, `2,106/2,106` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x007E2635` → [CmpOpenDevicesControlSet](../7D/CmpOpenDevicesControlSet_function_007DC5B0.md) (function, `0x007DC5B0`)
- `0x007E267E` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E26B8` → [CmpGetAcpiProfileInformation](CmpGetAcpiProfileInformation_function_007E3D7C.md) (function, `0x007E3D7C`)
- `0x007E26F8` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E2719` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E2752` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E2773` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E279F` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E27C9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E27F0` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E280A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007E2832` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007E2843` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E286A` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E28A5` → [CmpFilterAcpiDockingState](CmpFilterAcpiDockingState_function_007E3B1C.md) (function, `0x007E3B1C`)
- `0x007E28C3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x007E2911` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E296A` → [CmpMoveBiosAliasTable](CmpMoveBiosAliasTable_function_007E4578.md) (function, `0x007E4578`)
- `0x007E2997` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E29D7` → [CmpCloneHwProfile](CmpCloneHwProfile_function_007E303C.md) (function, `0x007E303C`)
- `0x007E29F6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E2A13` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007E2A24` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E2A60` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E2A76` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E2ACD` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x007E2AEC` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E2B14` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x007E2B30` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E2B3E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E2B4D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E2B5C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E2B6A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E2B79` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E2BA7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E2BC3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E2BF3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E2C0F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E2C20` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x007E2C5B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E2C7E` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x007E2C8F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E2CBB` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x007E2CDC` → [CmpAddAcpiAliasEntry](CmpAddAcpiAliasEntry_function_007E2DC4.md) (function, `0x007E2DC4`)
- `0x007E2D3A` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x007E2D72` → [RtlUnicodeStringPrintf](../../text/48/RtlUnicodeStringPrintf_function_0048B984.md) (function, `0x0048B984`)
- `0x007E2D9E` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)

### Direct callers
- [IopExecuteHardwareProfileChange](../74/IopExecuteHardwareProfileChange_function_00744024.md) at `0x007441B5`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C576ED`

### Static image references
- `0x007E25A3` → RVA `0x00E0A740` (`.data`; read)
- `0x007E2648` → RVA `0x00B4AFA8` (`CmpControlIdConfigDbString`; read)
- `0x007E26C7` → RVA `0x00B4AF20` (`CmpHardwareProfilesCurrentString`; read)
- `0x007E270D` → RVA `0x00AFF6C0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E2767` → RVA `0x00B092B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E27B9` → RVA `0x00B09250` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E2837` → RVA `0x00B09220` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E28DD` → RVA `0x00B4AFB8` (`CmpHardwareProfilesString`; read)
- `0x007E2A00` → RVA `0x00B09240` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E2D4B` → RVA `0x00B09180` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E2D7C` → RVA `0x00FD9C00` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **41**
  - `0x007E267E` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E26F8` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E2719` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E2752` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E2773` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E279F` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E27C9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E27F0` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E280A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007E2832` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007E2843` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E286A` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E28C3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x007E2911` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E2997` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E29F6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E2A13` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007E2A24` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E2A60` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E2A76` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E2ACD` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x007E2AEC` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E2B14` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x007E2B30` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E2B3E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E2B4D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E2B5C` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E2B6A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E2B79` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E2BA7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E2BC3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E2BF3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E2C0F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E2C20` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x007E2C5B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E2C7E` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x007E2C8F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E2CBB` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x007E2D3A` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x007E2D72` → [RtlUnicodeStringPrintf](../../text/48/RtlUnicodeStringPrintf_function_0048B984.md) (`PAGE` → `.text`)
  - `0x007E2D9E` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E2584  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
007E2589  55                              push rbp
007E258A  56                              push rsi
007E258B  57                              push rdi
007E258C  41 54                           push r12
007E258E  41 55                           push r13
007E2590  41 56                           push r14
007E2592  41 57                           push r15
007E2594  48 8D AC 24 00 FE FF FF         lea rbp, [rsp - 0x200]
007E259C  48 81 EC 00 03 00 00            sub rsp, 0x300
007E25A3  48 8B 05 96 81 62 00            mov rax, qword ptr [rip + 0x628196]
007E25AA  48 33 C4                        xor rax, rsp
007E25AD  48 89 85 F0 01 00 00            mov qword ptr [rbp + 0x1f0], rax
007E25B4  4C 8B AD 60 02 00 00            mov r13, qword ptr [rbp + 0x260]
007E25BB  4C 8D 45 E0                     lea r8, [rbp - 0x20]
007E25BF  48 83 65 D0 00                  and qword ptr [rbp - 0x30], 0
007E25C4  0F 57 C0                        xorps xmm0, xmm0
007E25C7  48 83 64 24 60 00               and qword ptr [rsp + 0x60], 0
007E25CD  33 C0                           xor eax, eax
007E25CF  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
007E25D5  4C 8B F2                        mov r14, rdx
007E25D8  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
007E25DE  48 8D 55 D0                     lea rdx, [rbp - 0x30]
007E25E2  48 83 65 C8 00                  and qword ptr [rbp - 0x38], 0
007E25E7  0F 57 C9                        xorps xmm1, xmm1
007E25EA  48 83 65 B8 00                  and qword ptr [rbp - 0x48], 0
007E25EF  33 FF                           xor edi, edi
007E25F1  83 64 24 70 00                  and dword ptr [rsp + 0x70], 0
007E25F6  4C 8B E1                        mov r12, rcx
007E25F9  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
007E25FE  83 64 24 74 00                  and dword ptr [rsp + 0x74], 0
007E2603  83 64 24 40 00                  and dword ptr [rsp + 0x40], 0
007E2608  83 65 B0 00                     and dword ptr [rbp - 0x50], 0
007E260C  48 21 7D C0                     and qword ptr [rbp - 0x40], rdi
007E2610  48 21 7D A8                     and qword ptr [rbp - 0x58], rdi
007E2614  41 88 45 00                     mov byte ptr [r13], al
007E2618  4C 89 4D D8                     mov qword ptr [rbp - 0x28], r9
007E261C  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
007E2620  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
007E2624  0F 11 4C 24 50                  movups xmmword ptr [rsp + 0x50], xmm1
007E2629  89 45 A0                        mov dword ptr [rbp - 0x60], eax
007E262C  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
007E2631  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
007E2635  E8 76 9F FF FF                  call 0x1407dc5b0
007E263A  8B D8                           mov ebx, eax
007E263C  85 C0                           test eax, eax
007E263E  0F 88 E2 04 00 00               js 0x1407e2b26
007E2644  4C 8B 7D D0                     mov r15, qword ptr [rbp - 0x30]
007E2648  48 8D 05 59 89 36 00            lea rax, [rip + 0x368959]
007E264F  0F 57 C0                        xorps xmm0, xmm0
007E2652  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
007E2656  BE 40 02 00 00                  mov esi, 0x240
007E265B  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
007E265F  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007E2664  89 75 90                        mov dword ptr [rbp - 0x70], esi
007E2667  BA 19 00 02 00                  mov edx, 0x20019
007E266C  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
007E2674  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
007E2679  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
007E267E  E8 8D AC EC FF                  call 0x1406ad310
007E2683  8B D8                           mov ebx, eax
007E2685  85 C0                           test eax, eax
007E2687  79 0A                           jns 0x1407e2693
007E2689  48 21 7C 24 60                  and qword ptr [rsp + 0x60], rdi
007E268E  E9 93 04 00 00                  jmp 0x1407e2b26
007E2693  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007E2698  48 8D 45 F0                     lea rax, [rbp - 0x10]
007E269C  C7 44 24 28 00 01 00 00         mov dword ptr [rsp + 0x28], 0x100
007E26A4  4C 8D 8D F0 00 00 00            lea r9, [rbp + 0xf0]
007E26AB  4C 8D 45 C0                     lea r8, [rbp - 0x40]
007E26AF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E26B4  48 8D 55 A8                     lea rdx, [rbp - 0x58]
007E26B8  E8 BF 16 00 00                  call 0x1407e3d7c
007E26BD  8B D8                           mov ebx, eax
007E26BF  85 C0                           test eax, eax
007E26C1  0F 88 5F 04 00 00               js 0x1407e2b26
007E26C7  48 8D 05 52 88 36 00            lea rax, [rip + 0x368852]
007E26CE  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
007E26D6  0F 57 C0                        xorps xmm0, xmm0
007E26D9  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
007E26DD  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007E26E2  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
007E26E6  BA 19 00 02 00                  mov edx, 0x20019
007E26EB  89 75 90                        mov dword ptr [rbp - 0x70], esi
007E26EE  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007E26F3  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
007E26F8  E8 13 AC EC FF                  call 0x1406ad310
007E26FD  8B D8                           mov ebx, eax
007E26FF  85 C0                           test eax, eax
007E2701  79 0A                           jns 0x1407e270d
007E2703  48 21 7C 24 68                  and qword ptr [rsp + 0x68], rdi
007E2708  E9 19 04 00 00                  jmp 0x1407e2b26
007E270D  48 8D 15 AC CF 31 00            lea rdx, [rip + 0x31cfac]
007E2714  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E2719  E8 62 80 C4 FF                  call 0x14042a780
007E271E  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
007E2723  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007E2728  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
007E272C  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
007E2731  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007E2736  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
007E273E  0F 57 C0                        xorps xmm0, xmm0
007E2741  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
007E2745  BA 19 00 02 00                  mov edx, 0x20019
007E274A  89 75 90                        mov dword ptr [rbp - 0x70], esi
007E274D  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
007E2752  E8 B9 AB EC FF                  call 0x1406ad310
007E2757  8B D8                           mov ebx, eax
007E2759  85 C0                           test eax, eax
007E275B  79 0A                           jns 0x1407e2767
007E275D  48 21 7C 24 48                  and qword ptr [rsp + 0x48], rdi
007E2762  E9 BF 03 00 00                  jmp 0x1407e2b26
007E2767  48 8D 15 42 6B 32 00            lea rdx, [rip + 0x326b42]
007E276E  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E2773  E8 08 80 C4 FF                  call 0x14042a780
007E2778  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007E277D  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007E2782  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E2787  4C 8D 4D F0                     lea r9, [rbp - 0x10]
007E278B  BE 00 01 00 00                  mov esi, 0x100
007E2790  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E2795  41 B8 01 00 00 00               mov r8d, 1
007E279B  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
007E279F  E8 0C AC EC FF                  call 0x1406ad3b0
007E27A4  85 C0                           test eax, eax
007E27A6  0F 88 75 03 00 00               js 0x1407e2b21
007E27AC  83 7D F4 04                     cmp dword ptr [rbp - 0xc], 4
007E27B0  0F 85 6B 03 00 00               jne 0x1407e2b21
007E27B6  8B 45 F8                        mov eax, dword ptr [rbp - 8]
007E27B9  48 8D 15 90 6A 32 00            lea rdx, [rip + 0x326a90]
007E27C0  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E27C5  8B 5C 05 F0                     mov ebx, dword ptr [rbp + rax - 0x10]
007E27C9  E8 B2 7F C4 FF                  call 0x14042a780
007E27CE  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007E27D3  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007E27D8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E27DD  4C 8D 4D F0                     lea r9, [rbp - 0x10]
007E27E1  41 B8 01 00 00 00               mov r8d, 1
007E27E7  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
007E27EB  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E27F0  E8 BB AB EC FF                  call 0x1406ad3b0
007E27F5  85 C0                           test eax, eax
007E27F7  78 3E                           js 0x1407e2837
007E27F9  83 7D F4 03                     cmp dword ptr [rbp - 0xc], 3
007E27FD  75 38                           jne 0x1407e2837
007E27FF  8B 55 FC                        mov edx, dword ptr [rbp - 4]
007E2802  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007E2808  8B CE                           mov ecx, esi
007E280A  E8 E1 F8 39 00                  call 0x140b820f0
007E280F  48 8B F8                        mov rdi, rax
007E2812  48 85 C0                        test rax, rax
007E2815  75 0A                           jne 0x1407e2821
007E2817  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007E281C  E9 05 03 00 00                  jmp 0x1407e2b26
007E2821  8B 45 F8                        mov eax, dword ptr [rbp - 8]
007E2824  48 8D 55 F0                     lea rdx, [rbp - 0x10]
007E2828  44 8B 45 FC                     mov r8d, dword ptr [rbp - 4]
007E282C  48 03 D0                        add rdx, rax
007E282F  48 8B CF                        mov rcx, rdi
007E2832  E8 09 40 EE FF                  call 0x1406c6840
007E2837  48 8D 15 E2 69 32 00            lea rdx, [rip + 0x3269e2]
007E283E  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E2843  E8 38 7F C4 FF                  call 0x14042a780
007E2848  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007E284D  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007E2852  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E2857  4C 8D 4D F0                     lea r9, [rbp - 0x10]
007E285B  41 B8 01 00 00 00               mov r8d, 1
007E2861  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
007E2865  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E286A  E8 41 AB EC FF                  call 0x1406ad3b0
007E286F  85 C0                           test eax, eax
007E2871  0F 88 AA 02 00 00               js 0x1407e2b21
007E2877  83 7D F4 04                     cmp dword ptr [rbp - 0xc], 4
007E287B  0F 85 A0 02 00 00               jne 0x1407e2b21
007E2881  8B 45 F8                        mov eax, dword ptr [rbp - 8]
007E2884  4C 8B C7                        mov r8, rdi
007E2887  8B D3                           mov edx, ebx
007E2889  49 8B CC                        mov rcx, r12
007E288C  8B 74 05 F0                     mov esi, dword ptr [rbp + rax - 0x10]
007E2890  44 8B CE                        mov r9d, esi
007E2893  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
007E2897  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E289C  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
007E28A0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E28A5  E8 72 12 00 00                  call 0x1407e3b1c
007E28AA  8B D8                           mov ebx, eax
007E28AC  85 C0                           test eax, eax
007E28AE  0F 88 72 02 00 00               js 0x1407e2b26
007E28B4  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
007E28B8  48 8D 54 24 74                  lea rdx, [rsp + 0x74]
007E28BD  45 33 C0                        xor r8d, r8d
007E28C0  49 8B C6                        mov rax, r14
007E28C3  E8 08 82 ED FF                  call 0x1406baad0
007E28C8  83 7C 24 74 FF                  cmp dword ptr [rsp + 0x74], -1
007E28CD  8B D8                           mov ebx, eax
007E28CF  0F 84 D0 04 00 00               je 0x1407e2da5
007E28D5  85 C0                           test eax, eax
007E28D7  0F 88 49 02 00 00               js 0x1407e2b26
007E28DD  48 8D 05 D4 86 36 00            lea rax, [rip + 0x3686d4]
007E28E4  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
007E28EC  0F 57 C0                        xorps xmm0, xmm0
007E28EF  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
007E28F3  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007E28F8  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
007E28FC  BA 19 00 02 00                  mov edx, 0x20019
007E2901  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
007E2908  48 8D 4D B8                     lea rcx, [rbp - 0x48]
007E290C  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
007E2911  E8 FA A9 EC FF                  call 0x1406ad310
007E2916  8B D8                           mov ebx, eax
007E2918  85 C0                           test eax, eax
007E291A  79 0A                           jns 0x1407e2926
007E291C  48 83 65 B8 00                  and qword ptr [rbp - 0x48], 0
007E2921  E9 00 02 00 00                  jmp 0x1407e2b26
007E2926  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
007E292A  8B 4C 24 74                     mov ecx, dword ptr [rsp + 0x74]
007E292E  48 C1 E1 05                     shl rcx, 5
007E2932  44 8B 74 01 20                  mov r14d, dword ptr [rcx + rax + 0x20]
007E2937  8B 54 01 1C                     mov edx, dword ptr [rcx + rax + 0x1c]
007E293B  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
007E293F  41 F6 C6 08                     test r14b, 8
007E2943  74 38                           je 0x1407e297d
007E2945  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007E294A  48 8D 45 F0                     lea rax, [rbp - 0x10]
007E294E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007E2953  44 8B CA                        mov r9d, edx
007E2956  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
007E295B  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
007E2962  44 8B C6                        mov r8d, esi
007E2965  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E296A  E8 09 1C 00 00                  call 0x1407e4578
007E296F  8B D8                           mov ebx, eax
007E2971  85 C0                           test eax, eax
007E2973  0F 88 AD 01 00 00               js 0x1407e2b26
007E2979  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
007E297D  41 8B DE                        mov ebx, r14d
007E2980  83 E3 04                        and ebx, 4
007E2983  75 08                           jne 0x1407e298d
007E2985  3B D6                           cmp edx, esi
007E2987  0F 84 B4 02 00 00               je 0x1407e2c41
007E298D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007E2992  41 C6 45 00 01                  mov byte ptr [r13], 1
007E2997  E8 14 A9 EC FF                  call 0x1406ad2b0
007E299C  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
007E29A2  85 DB                           test ebx, ebx
007E29A4  74 4B                           je 0x1407e29f1
007E29A6  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
007E29AB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E29B0  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
007E29B5  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
007E29B9  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007E29BE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007E29C3  48 8D 44 24 68                  lea rax, [rsp + 0x68]
007E29C8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E29CD  41 0F B7 04 24                  movzx eax, word ptr [r12]
007E29D2  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
007E29D7  E8 60 06 00 00                  call 0x1407e303c
007E29DC  8B D8                           mov ebx, eax
007E29DE  85 C0                           test eax, eax
007E29E0  0F 89 84 00 00 00               jns 0x1407e2a6a
007E29E6  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
007E29EC  E9 35 01 00 00                  jmp 0x1407e2b26
007E29F1  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007E29F6  E8 B5 A8 EC FF                  call 0x1406ad2b0
007E29FB  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
007E2A00  4C 8D 05 39 68 32 00            lea r8, [rip + 0x326839]
007E2A07  BA 80 00 00 00                  mov edx, 0x80
007E2A0C  48 8D 8D F0 00 00 00            lea rcx, [rbp + 0xf0]
007E2A13  E8 08 21 D2 FF                  call 0x140504b20
007E2A18  48 8D 95 F0 00 00 00            lea rdx, [rbp + 0xf0]
007E2A1F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E2A24  E8 57 7D C4 FF                  call 0x14042a780
007E2A29  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
007E2A2D  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007E2A32  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
007E2A36  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007E2A3B  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007E2A40  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
007E2A48  0F 57 C0                        xorps xmm0, xmm0
007E2A4B  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
007E2A4F  BA 19 00 02 00                  mov edx, 0x20019
007E2A54  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
007E2A5B  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
007E2A60  E8 AB A8 EC FF                  call 0x1406ad310
007E2A65  E9 72 FF FF FF                  jmp 0x1407e29dc
007E2A6A  48 8D 15 4F CC 31 00            lea rdx, [rip + 0x31cc4f]
007E2A71  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E2A76  E8 05 7D C4 FF                  call 0x14042a780
007E2A7B  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
007E2A80  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007E2A85  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
007E2A89  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
007E2A8E  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007E2A93  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
007E2A9B  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
007E2A9F  0F 57 C0                        xorps xmm0, xmm0
007E2AA2  48 8D 45 B0                     lea rax, [rbp - 0x50]
007E2AA6  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
007E2AAD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007E2AB2  45 33 C9                        xor r9d, r9d
007E2AB5  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
007E2ABD  BA 1F 00 02 00                  mov edx, 0x2001f
007E2AC2  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007E2AC8  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
007E2ACD  E8 9E A9 EC FF                  call 0x1406ad470
007E2AD2  8B D8                           mov ebx, eax
007E2AD4  85 C0                           test eax, eax
007E2AD6  79 08                           jns 0x1407e2ae0
007E2AD8  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
007E2ADE  EB 46                           jmp 0x1407e2b26
007E2AE0  48 8D 15 39 67 32 00            lea rdx, [rip + 0x326739]
007E2AE7  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E2AEC  E8 8F 7C C4 FF                  call 0x14042a780
007E2AF1  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007E2AF6  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E2AFB  BB 04 00 00 00                  mov ebx, 4
007E2B00  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E2B05  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
007E2B09  44 8B CB                        mov r9d, ebx
007E2B0C  45 33 C0                        xor r8d, r8d
007E2B0F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E2B14  E8 B7 B1 EC FF                  call 0x1406adcd0
007E2B19  85 C0                           test eax, eax
007E2B1B  0F 89 25 01 00 00               jns 0x1407e2c46
007E2B21  BB 4C 01 00 C0                  mov ebx, 0xc000014c
007E2B26  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007E2B2B  48 85 C9                        test rcx, rcx
007E2B2E  74 05                           je 0x1407e2b35
007E2B30  E8 7B A7 EC FF                  call 0x1406ad2b0
007E2B35  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
007E2B39  48 85 C9                        test rcx, rcx
007E2B3C  74 05                           je 0x1407e2b43
007E2B3E  E8 6D A7 EC FF                  call 0x1406ad2b0
007E2B43  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007E2B48  48 85 C9                        test rcx, rcx
007E2B4B  74 05                           je 0x1407e2b52
007E2B4D  E8 5E A7 EC FF                  call 0x1406ad2b0
007E2B52  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007E2B57  48 85 C9                        test rcx, rcx
007E2B5A  74 05                           je 0x1407e2b61
007E2B5C  E8 4F A7 EC FF                  call 0x1406ad2b0
007E2B61  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
007E2B65  48 85 C9                        test rcx, rcx
007E2B68  74 05                           je 0x1407e2b6f
007E2B6A  E8 41 A7 EC FF                  call 0x1406ad2b0
007E2B6F  48 85 FF                        test rdi, rdi
007E2B72  74 0A                           je 0x1407e2b7e
007E2B74  33 D2                           xor edx, edx
007E2B76  48 8B CF                        mov rcx, rdi
007E2B79  E8 F2 FC 39 00                  call 0x140b82870
007E2B7E  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
007E2B82  48 85 C9                        test rcx, rcx
007E2B85  74 41                           je 0x1407e2bc8
007E2B87  33 D2                           xor edx, edx
007E2B89  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
007E2B8D  39 51 04                        cmp dword ptr [rcx + 4], edx
007E2B90  76 2F                           jbe 0x1407e2bc1
007E2B92  33 C0                           xor eax, eax
007E2B94  48 C1 E0 05                     shl rax, 5
007E2B98  4C 8B 44 08 10                  mov r8, qword ptr [rax + rcx + 0x10]
007E2B9D  4D 85 C0                        test r8, r8
007E2BA0  74 12                           je 0x1407e2bb4
007E2BA2  33 D2                           xor edx, edx
007E2BA4  49 8B C8                        mov rcx, r8
007E2BA7  E8 C4 FC 39 00                  call 0x140b82870
007E2BAC  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
007E2BB0  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
007E2BB4  FF C2                           inc edx
007E2BB6  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
007E2BBA  8B C2                           mov eax, edx
007E2BBC  3B 51 04                        cmp edx, dword ptr [rcx + 4]
007E2BBF  72 D3                           jb 0x1407e2b94
007E2BC1  33 D2                           xor edx, edx
007E2BC3  E8 A8 FC 39 00                  call 0x140b82870
007E2BC8  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
007E2BCC  48 85 C9                        test rcx, rcx
007E2BCF  74 43                           je 0x1407e2c14
007E2BD1  33 D2                           xor edx, edx
007E2BD3  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
007E2BD7  39 51 04                        cmp dword ptr [rcx + 4], edx
007E2BDA  76 31                           jbe 0x1407e2c0d
007E2BDC  33 C0                           xor eax, eax
007E2BDE  48 FF C0                        inc rax
007E2BE1  48 8D 04 40                     lea rax, [rax + rax*2]
007E2BE5  4C 8B 04 C1                     mov r8, qword ptr [rcx + rax*8]
007E2BE9  4D 85 C0                        test r8, r8
007E2BEC  74 12                           je 0x1407e2c00
007E2BEE  33 D2                           xor edx, edx
007E2BF0  49 8B C8                        mov rcx, r8
007E2BF3  E8 78 FC 39 00                  call 0x140b82870
007E2BF8  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
007E2BFC  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
007E2C00  FF C2                           inc edx
007E2C02  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
007E2C06  8B C2                           mov eax, edx
007E2C08  3B 51 04                        cmp edx, dword ptr [rcx + 4]
007E2C0B  72 D1                           jb 0x1407e2bde
007E2C0D  33 D2                           xor edx, edx
007E2C0F  E8 5C FC 39 00                  call 0x140b82870
007E2C14  8B C3                           mov eax, ebx
007E2C16  48 8B 8D F0 01 00 00            mov rcx, qword ptr [rbp + 0x1f0]
007E2C1D  48 33 CC                        xor rcx, rsp
007E2C20  E8 1B 9A EC FF                  call 0x1406ac640
007E2C25  48 8B 9C 24 50 03 00 00         mov rbx, qword ptr [rsp + 0x350]
007E2C2D  48 81 C4 00 03 00 00            add rsp, 0x300
007E2C34  41 5F                           pop r15
007E2C36  41 5E                           pop r14
007E2C38  41 5D                           pop r13
007E2C3A  41 5C                           pop r12
007E2C3C  5F                              pop rdi
007E2C3D  5E                              pop rsi
007E2C3E  5D                              pop rbp
007E2C3F  C3                              ret
007E2C40  CC                              int3
007E2C41  BB 04 00 00 00                  mov ebx, 4
007E2C46  41 0F B7 04 24                  movzx eax, word ptr [r12]
007E2C4B  48 8D 15 5E 66 32 00            lea rdx, [rip + 0x32665e]
007E2C52  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E2C57  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
007E2C5B  E8 20 7B C4 FF                  call 0x14042a780
007E2C60  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007E2C65  48 8D 44 24 44                  lea rax, [rsp + 0x44]
007E2C6A  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
007E2C6E  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E2C73  44 8B CB                        mov r9d, ebx
007E2C76  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E2C7B  45 33 C0                        xor r8d, r8d
007E2C7E  E8 4D B0 EC FF                  call 0x1406adcd0
007E2C83  48 8D 15 C6 65 32 00            lea rdx, [rip + 0x3265c6]
007E2C8A  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E2C8F  E8 EC 7A C4 FF                  call 0x14042a780
007E2C94  41 0F B7 44 24 02               movzx eax, word ptr [r12 + 2]
007E2C9A  49 8D 4C 24 04                  lea rcx, [r12 + 4]
007E2C9F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007E2CA3  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E2CA8  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
007E2CAD  41 B9 03 00 00 00               mov r9d, 3
007E2CB3  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007E2CB8  45 33 C0                        xor r8d, r8d
007E2CBB  E8 10 B0 EC FF                  call 0x1406adcd0
007E2CC0  8B D8                           mov ebx, eax
007E2CC2  41 F6 C6 02                     test r14b, 2
007E2CC6  75 1B                           jne 0x1407e2ce3
007E2CC8  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
007E2CCD  4C 8D 8D F0 00 00 00            lea r9, [rbp + 0xf0]
007E2CD4  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007E2CD9  49 8B D4                        mov rdx, r12
007E2CDC  E8 E3 00 00 00                  call 0x1407e2dc4
007E2CE1  8B D8                           mov ebx, eax
007E2CE3  39 74 24 40                     cmp dword ptr [rsp + 0x40], esi
007E2CE7  0F 84 B8 00 00 00               je 0x1407e2da5
007E2CED  48 8D 05 2C 82 36 00            lea rax, [rip + 0x36822c]
007E2CF4  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
007E2CFC  45 33 C9                        xor r9d, r9d
007E2CFF  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
007E2D03  48 8D 45 B0                     lea rax, [rbp - 0x50]
007E2D07  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
007E2D0B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007E2D10  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007E2D15  0F 57 C0                        xorps xmm0, xmm0
007E2D18  C7 44 24 28 08 00 00 00         mov dword ptr [rsp + 0x28], 8
007E2D20  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007E2D26  41 8D 51 20                     lea edx, [r9 + 0x20]
007E2D2A  48 8D 4D C8                     lea rcx, [rbp - 0x38]
007E2D2E  C7 45 90 40 03 00 00            mov dword ptr [rbp - 0x70], 0x340
007E2D35  F3 0F 7F 45 98                  movdqu xmmword ptr [rbp - 0x68], xmm0
007E2D3A  E8 31 A7 EC FF                  call 0x1406ad470
007E2D3F  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
007E2D44  4C 8D 45 E0                     lea r8, [rbp - 0x20]
007E2D48  0F 57 C0                        xorps xmm0, xmm0
007E2D4B  48 8D 15 2E 64 32 00            lea rdx, [rip + 0x32642e]
007E2D52  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
007E2D57  B8 00 01 00 00                  mov eax, 0x100
007E2D5C  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E2D61  66 89 44 24 52                  mov word ptr [rsp + 0x52], ax
007E2D66  48 8D 85 F0 00 00 00            lea rax, [rbp + 0xf0]
007E2D6D  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007E2D72  E8 0D 8C CA FF                  call 0x14048b984
007E2D77  0F B7 44 24 50                  movzx eax, word ptr [rsp + 0x50]
007E2D7C  48 8D 15 7D 6E 7F 00            lea rdx, [rip + 0x7f6e7d]
007E2D83  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
007E2D87  41 B9 06 00 00 00               mov r9d, 6
007E2D8D  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007E2D91  45 33 C0                        xor r8d, r8d
007E2D94  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
007E2D99  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E2D9E  E8 2D AF EC FF                  call 0x1406adcd0
007E2DA3  8B D8                           mov ebx, eax
007E2DA5  85 DB                           test ebx, ebx
007E2DA7  0F 88 79 FD FF FF               js 0x1407e2b26
007E2DAD  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
007E2DB1  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
007E2DB6  48 89 01                        mov qword ptr [rcx], rax
007E2DB9  E9 77 FD FF FF                  jmp 0x1407e2b35
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSetAcpiHwProfile(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m238;
    unsigned int v_stack_m23C;
    unsigned int v_stack_m240;
    unsigned int v_stack_m244;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned int v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned int v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned int v_stack_m2C4;
    unsigned int v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned int v_stack_m2F4;
    unsigned int v_stack_m2F8;
    unsigned __int64 v_stack_m308;
    unsigned int v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int16 v_stack_p52;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (768);
    result = (*(unsigned __int64 *)(v_rip + 6455702)) ^ (v_rsp);
    v_stack_m48 = result;
    result = 0;
    v_rdi = 0;
    *(unsigned __int8 *)(a5) = 0;
    v_stack_m260 = a4;
    v_stack_m258 = v_xmm0;
    v_stack_m2A0 = 0;
    v_stack_m2E8 = v_xmm1;
    v_stack_m298 = 0;
    v_stack_m2C0 = v_xmm0;
    v_stack_m2B0 = v_xmm0;
    result = CmpOpenDevicesControlSet(a1, v_stack_m268, v_stack_m258, a4);
    if (sign_flag) goto loc_007E2B26;
    v_stack_m2B8 = v_stack_m268;
    v_stack_m2B0 = v_rip + 3574105;
    v_stack_m2A8 = 576;
    v_stack_m2C0 = 48;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m2D8, (unsigned int)(0x20019ULL), v_stack_m2C0, a4);
    if (!sign_flag) goto loc_007E2693;
    goto loc_007E2B26;
loc_007E2693:
    v_stack_m310 = 256;
    v_stack_m318 = v_stack_m248;
    result = CmpGetAcpiProfileInformation(v_stack_m2D8, v_stack_m290, v_stack_m278, v_stack_m148);
    if (sign_flag) goto loc_007E2B26;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_rip + 3573842;
    v_stack_m2B8 = v_stack_m268;
    v_stack_m2A8 = 576;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m2D0, (unsigned int)(0x20019ULL), v_stack_m2C0, v_stack_m148);
    if (!sign_flag) goto loc_007E270D;
    goto loc_007E2B26;
loc_007E270D:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3264428, v_stack_m2C0, v_stack_m148);
    v_stack_m2B8 = v_stack_m2D8;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_stack_m2E8;
    v_stack_m2A8 = 576;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m2F0, (unsigned int)(0x20019ULL), v_stack_m2C0, v_stack_m148);
    if (!sign_flag) goto loc_007E2767;
    goto loc_007E2B26;
loc_007E2767:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3304258, v_stack_m2C0, v_stack_m148);
    v_stack_m310 = v_stack_m2C8;
    v_stack_m318 = 256;
    result = ZwQueryValueKey(v_stack_m2F0, v_stack_m2E8, 1, v_stack_m248);
    if (sign_flag) goto loc_007E2B21;
    if (v_stack_m244 != 4) goto loc_007E2B21;
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3304080, 1, v_stack_m248);
    v_stack_m310 = v_stack_m2C8;
    v_stack_m318 = 256;
    result = ZwQueryValueKey(v_stack_m2F0, v_stack_m2E8, 1, v_stack_m248);
    if (sign_flag) goto loc_007E2837;
    if (v_stack_m244 != 3) goto loc_007E2837;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m23C), (unsigned int)(0x20204D43ULL), v_stack_m248);
    if (result != 0) goto loc_007E2821;
    goto loc_007E2B26;
loc_007E2821:
    a2 = (v_stack_m248) + ((unsigned int)(v_stack_m240));
    result = memcpy(result, a2, (unsigned int)(v_stack_m23C), v_stack_m248);
loc_007E2837:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3303906, (unsigned int)(v_stack_m23C), v_stack_m248);
    v_stack_m310 = v_stack_m2C8;
    v_stack_m318 = 256;
    result = ZwQueryValueKey(v_stack_m2D8, v_stack_m2E8, 1, v_stack_m248);
    if (sign_flag) goto loc_007E2B21;
    if (v_stack_m244 != 4) goto loc_007E2B21;
    v_stack_m310 = v_stack_m278;
    v_stack_m318 = v_stack_m290;
    result = CmpFilterAcpiDockingState(a1, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m238 + (unsigned int)(v_stack_m240) * 1 - 16)))));
    if (sign_flag) goto loc_007E2B26;
    a3 = 0;
    result = guard_dispatch_icall(v_stack_m290, v_stack_m2C4, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m238 + (unsigned int)(v_stack_m240) * 1 - 16)))));
    if (v_stack_m2C4 == -1) goto loc_007E2DA5;
    if (sign_flag) goto loc_007E2B26;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_rip + 3573460;
    v_stack_m2B8 = v_stack_m268;
    v_stack_m2A8 = 576;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m280, (unsigned int)(0x20019ULL), v_stack_m2C0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m238 + (unsigned int)(v_stack_m240) * 1 - 16)))));
    if (!sign_flag) goto loc_007E2926;
    goto loc_007E2B26;
loc_007E2926:
    a1 = ((unsigned int)(v_stack_m2C4)) << (5);
    v_stack_m2F8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_stack_m290 * 1 + 28)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + v_stack_m290 * 1 + 32)))) & (8)) == 0) goto loc_007E297D;
    v_stack_m308 = v_stack_m248;
    v_stack_m318 = v_stack_m148;
    result = CmpMoveBiosAliasTable(v_stack_m2D8, v_stack_m2F0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m238 + (unsigned int)(v_stack_m240) * 1 - 16)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_stack_m290 * 1 + 28)))));
    if (sign_flag) goto loc_007E2B26;
loc_007E297D:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_stack_m290 * 1 + 32))))) & (4));
    if (condition_is_not_equal) goto loc_007E298D;
    if (((unsigned int)((unsigned int)(v_stack_m2F8))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m238 + (unsigned int)(v_stack_m240) * 1 - 16))))) goto loc_007E2C41;
loc_007E298D:
    *(unsigned __int8 *)(a5) = 1;
    result = ZwClose(v_stack_m2F0, (unsigned int)(v_stack_m2F8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m238 + (unsigned int)(v_stack_m240) * 1 - 16)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_stack_m290 * 1 + 28)))));
    if ((unsigned int)(v_rbx) == 0) goto loc_007E29F1;
    v_stack_m308 = v_stack_m2F8;
    v_stack_m310 = v_stack_m2D0;
    v_stack_m318 = (unsigned __int16)(*(unsigned __int16 *)(a1));
    result = CmpCloneHwProfile(v_stack_m2D8, v_stack_m280, v_stack_m2D0, (unsigned int)(v_stack_m2F8));
loc_007E29DC:
    if (!sign_flag) goto loc_007E2A6A;
    goto loc_007E2B26;
loc_007E29F1:
    result = ZwClose(v_stack_m2D0, v_stack_m280, v_stack_m2D0, (unsigned int)(v_stack_m2F8));
    result = swprintf_s(v_stack_m148, 128, v_rip + 3303481, (unsigned int)(v_stack_m2F8));
    result = RtlInitUnicodeString(v_stack_m2E8, v_stack_m148, v_rip + 3303481, (unsigned int)(v_stack_m2F8));
    v_stack_m2B8 = v_stack_m280;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_stack_m2E8;
    v_stack_m2A8 = 576;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m2D0, (unsigned int)(0x20019ULL), v_stack_m2C0, (unsigned int)(v_stack_m2F8));
    goto loc_007E29DC;
loc_007E2A6A:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3263567, v_stack_m2C0, (unsigned int)(v_stack_m2F8));
    v_stack_m2B8 = v_stack_m2D8;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_stack_m2E8;
    v_stack_m2A8 = 576;
    v_stack_m308 = v_stack_m288;
    a4 = 0;
    v_stack_m310 = 1;
    v_stack_m2A0 = v_xmm0;
    result = ZwCreateKey(v_stack_m2F0, (unsigned int)(0x2001FULL), v_stack_m2C0, a4);
    if (!sign_flag) goto loc_007E2AE0;
    goto loc_007E2B26;
loc_007E2AE0:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3303225, v_stack_m2C0, a4);
    v_stack_m310 = 4;
    a3 = 0;
    v_stack_m318 = v_stack_m2F8;
    result = ZwSetValueKey(v_stack_m2D8, v_stack_m2E8, a3, 4);
    if (!sign_flag) goto loc_007E2C46;
loc_007E2B21:
loc_007E2B26:
    if (v_stack_m2D0 != 0) {
        result = ZwClose(v_stack_m2D0, v_stack_m2E8, a3, 4);
    }
    if (v_stack_m270 != 0) {
        result = ZwClose(v_stack_m270, v_stack_m2E8, a3, 4);
    }
    if (v_stack_m2D8 != 0) {
        result = ZwClose(v_stack_m2D8, v_stack_m2E8, a3, 4);
    }
    if (v_stack_m2F0 != 0) {
        result = ZwClose(v_stack_m2F0, v_stack_m2E8, a3, 4);
    }
    if (v_stack_m280 != 0) {
        result = ZwClose(v_stack_m280, v_stack_m2E8, a3, 4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, 4);
    }
    if (v_stack_m290 == 0) goto loc_007E2BC8;
    a2 = 0;
    v_stack_m2F4 = 0;
    if ((*(unsigned int *)(v_stack_m290 + 4)) <= 0) goto loc_007E2BC1;
    result = 0;
loc_007E2B94:
    result = (result) << (5);
    if (*(unsigned __int64 *)(result + v_stack_m290 * 1 + 16) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(result + v_stack_m290 * 1 + 16);
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(result + v_stack_m290 * 1 + 16), 4);
        a2 = v_stack_m2F4;
        a1 = v_stack_m290;
    }
    a2 = (unsigned int)((a2) + 1);
    v_stack_m2F4 = (unsigned int)(a2);
    if (((unsigned int)(a2)) < (*(unsigned int *)(a1 + 4))) goto loc_007E2B94;
loc_007E2BC1:
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(result + v_stack_m290 * 1 + 16), 4);
loc_007E2BC8:
    if (v_stack_m278 == 0) goto loc_007E2C14;
    a2 = 0;
    v_stack_m2F4 = 0;
    if ((*(unsigned int *)(v_stack_m278 + 4)) <= 0) goto loc_007E2C0D;
    result = 0;
loc_007E2BDE:
    result = (result) + 1;
    result = result + result * 2;
    if (*(unsigned __int64 *)(v_stack_m278 + result + result * 2 * 8) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_m278 + result + result * 2 * 8);
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(v_stack_m278 + result + result * 2 * 8), 4);
        a2 = v_stack_m2F4;
        a1 = v_stack_m278;
    }
    a2 = (unsigned int)((a2) + 1);
    v_stack_m2F4 = (unsigned int)(a2);
    if (((unsigned int)(a2)) < (*(unsigned int *)(a1 + 4))) goto loc_007E2BDE;
loc_007E2C0D:
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(v_stack_m278 + result + result * 2 * 8), 4);
loc_007E2C14:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_stack_m278 + result + result * 2 * 8), 4);
    v_rsp = (v_rsp) + (768);
    return result;
loc_007E2C41:
loc_007E2C46:
    v_stack_p44 = (unsigned int)(*(unsigned __int16 *)(a1));
    result = RtlInitUnicodeString(v_stack_p50, v_rip + 3303006, *(unsigned __int64 *)(v_stack_m278 + result + result * 2 * 8), 4);
    v_stack_p28 = 4;
    v_stack_p20 = v_stack_p44;
    a3 = 0;
    result = ZwSetValueKey(v_stack_p48, v_stack_p50, a3, 4);
    result = RtlInitUnicodeString(v_stack_p50, v_rip + 3302854, a3, 4);
    v_stack_p28 = (unsigned int)(*(unsigned __int16 *)(a1 + 2));
    v_stack_p20 = a1 + 4;
    a3 = 0;
    result = ZwSetValueKey(v_stack_p48, v_stack_p50, a3, 3);
    v_rbx = (unsigned int)((unsigned int)(result));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + v_stack_m290 * 1 + 32)))) & (2)) == 0) {
        a3 = v_stack_p40;
        a4 = v_stack_m148;
        a1 = v_stack_p60;
        a2 = a1;
        result = CmpAddAcpiAliasEntry(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (v_stack_p40 != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m238 + (unsigned int)(v_stack_m240) * 1 - 16))))) {
        result = v_rip + 3572268;
        v_stack_p78 = 48;
        a4 = 0;
        v_stack_m2B0 = result;
        result = v_stack_m288;
        v_stack_m2B8 = v_stack_m268;
        v_stack_p30 = result;
        a3 = v_stack_p78;
        v_stack_p28 = 8;
        a2 = a4 + 32;
        a1 = v_stack_m270;
        v_stack_m2A8 = 832;
        v_stack_m2A0 = v_xmm0;
        result = ZwCreateKey(a1, a2, a3, a4);
        a4 = v_stack_p40;
        a3 = v_stack_m258;
        a2 = v_rip + 3302446;
        v_stack_p50 = v_xmm0;
        result = 256;
        a1 = v_stack_p50;
        v_stack_p52 = (unsigned __int16)(result);
        result = v_stack_m148;
        v_stack_p58 = result;
        result = RtlUnicodeStringPrintf(a1, a2, a3, a4);
        result = v_stack_p50;
        a2 = v_rip + 8351357;
        a1 = v_stack_m270;
        a4 = 6;
        v_stack_p28 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_p58;
        v_stack_p20 = result;
        result = ZwSetValueKey(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (sign_flag) goto loc_007E2B26;
    *(unsigned __int64 *)(v_stack_m260) = v_stack_p68;
    goto loc_007E2B35;
}
```

## 5. (Beta) C Style

```c
int64_t CmSetAcpiHwProfile(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m238;
    uint32_t v_stack_m23C;
    uint32_t v_stack_m240;
    uint32_t v_stack_m244;
    uint64_t v_stack_m248;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint32_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint32_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint32_t v_stack_m2C4;
    uint32_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint32_t v_stack_m2F4;
    uint32_t v_stack_m2F8;
    uint64_t v_stack_m308;
    uint32_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m48;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint16_t v_stack_p52;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (768);
    result = (*(uint64_t *)(v_rip + 0x628196)) ^ (local_rsp);
    v_stack_m48 = result;
    result = 0;
    local_rdi = 0;
    *(uint8_t *)(arg5) = 0;
    v_stack_m260 = Arg4;
    v_stack_m258 = v_xmm0;
    v_stack_m2A0 = 0;
    v_stack_m2E8 = v_xmm1;
    v_stack_m298 = 0;
    v_stack_m2C0 = v_xmm0;
    v_stack_m2B0 = v_xmm0;
    result = CmpOpenDevicesControlSet(Arg1, v_stack_m268, v_stack_m258, Arg4);
    if (sign_flag) goto loc_007E2B26;
    v_stack_m2B8 = v_stack_m268;
    v_stack_m2B0 = v_rip + 3574105;
    v_stack_m2A8 = 576;
    v_stack_m2C0 = 48;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m2D8, (uint32_t)(0x20019ULL), v_stack_m2C0, Arg4);
    if (!sign_flag) goto loc_007E2693;
    goto loc_007E2B26;
loc_007E2693:
    v_stack_m310 = 256;
    v_stack_m318 = v_stack_m248;
    result = CmpGetAcpiProfileInformation(v_stack_m2D8, v_stack_m290, v_stack_m278, v_stack_m148);
    if (sign_flag) goto loc_007E2B26;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_rip + 3573842;
    v_stack_m2B8 = v_stack_m268;
    v_stack_m2A8 = 576;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m2D0, (uint32_t)(0x20019ULL), v_stack_m2C0, v_stack_m148);
    if (!sign_flag) goto loc_007E270D;
    goto loc_007E2B26;
loc_007E270D:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3264428, v_stack_m2C0, v_stack_m148);
    v_stack_m2B8 = v_stack_m2D8;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_stack_m2E8;
    v_stack_m2A8 = 576;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m2F0, (uint32_t)(0x20019ULL), v_stack_m2C0, v_stack_m148);
    if (!sign_flag) goto loc_007E2767;
    goto loc_007E2B26;
loc_007E2767:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3304258, v_stack_m2C0, v_stack_m148);
    v_stack_m310 = v_stack_m2C8;
    v_stack_m318 = 256;
    result = ZwQueryValueKey(v_stack_m2F0, v_stack_m2E8, 1, v_stack_m248);
    if (sign_flag) goto loc_007E2B21;
    if (v_stack_m244 != 4) goto loc_007E2B21;
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3304080, 1, v_stack_m248);
    v_stack_m310 = v_stack_m2C8;
    v_stack_m318 = 256;
    result = ZwQueryValueKey(v_stack_m2F0, v_stack_m2E8, 1, v_stack_m248);
    if (sign_flag) goto loc_007E2837;
    if (v_stack_m244 != 3) goto loc_007E2837;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m23C), (uint32_t)(0x20204D43ULL), v_stack_m248);
    if (result != 0) goto loc_007E2821;
    goto loc_007E2B26;
loc_007E2821:
    Arg2 = (v_stack_m248) + ((uint32_t)(v_stack_m240));
    result = memcpy(result, Arg2, (uint32_t)(v_stack_m23C), v_stack_m248);
loc_007E2837:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3303906, (uint32_t)(v_stack_m23C), v_stack_m248);
    v_stack_m310 = v_stack_m2C8;
    v_stack_m318 = 256;
    result = ZwQueryValueKey(v_stack_m2D8, v_stack_m2E8, 1, v_stack_m248);
    if (sign_flag) goto loc_007E2B21;
    if (v_stack_m244 != 4) goto loc_007E2B21;
    v_stack_m310 = v_stack_m278;
    v_stack_m318 = v_stack_m290;
    result = CmpFilterAcpiDockingState(Arg1, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m238 + (uint32_t)(v_stack_m240) * 1 - 0x10)))));
    if (sign_flag) goto loc_007E2B26;
    Arg3 = 0;
    result = guard_dispatch_icall(v_stack_m290, v_stack_m2C4, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m238 + (uint32_t)(v_stack_m240) * 1 - 0x10)))));
    if (v_stack_m2C4 == -1) goto loc_007E2DA5;
    if (sign_flag) goto loc_007E2B26;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_rip + 3573460;
    v_stack_m2B8 = v_stack_m268;
    v_stack_m2A8 = 576;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m280, (uint32_t)(0x20019ULL), v_stack_m2C0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m238 + (uint32_t)(v_stack_m240) * 1 - 0x10)))));
    if (!sign_flag) goto loc_007E2926;
    goto loc_007E2B26;
loc_007E2926:
    Arg1 = ((uint32_t)(v_stack_m2C4)) << (5);
    v_stack_m2F8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + v_stack_m290 * 1 + 0x1C)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + v_stack_m290 * 1 + 0x20)))) & (8)) == 0) goto loc_007E297D;
    v_stack_m308 = v_stack_m248;
    v_stack_m318 = v_stack_m148;
    result = CmpMoveBiosAliasTable(v_stack_m2D8, v_stack_m2F0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m238 + (uint32_t)(v_stack_m240) * 1 - 0x10)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + v_stack_m290 * 1 + 0x1C)))));
    if (sign_flag) goto loc_007E2B26;
loc_007E297D:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + v_stack_m290 * 1 + 0x20))))) & (4));
    if (condition_is_not_equal) goto loc_007E298D;
    if (((uint32_t)((uint32_t)(v_stack_m2F8))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m238 + (uint32_t)(v_stack_m240) * 1 - 0x10))))) goto loc_007E2C41;
loc_007E298D:
    *(uint8_t *)(arg5) = 1;
    result = ZwClose(v_stack_m2F0, (uint32_t)(v_stack_m2F8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m238 + (uint32_t)(v_stack_m240) * 1 - 0x10)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + v_stack_m290 * 1 + 0x1C)))));
    if ((uint32_t)(local_rbx) == 0) goto loc_007E29F1;
    v_stack_m308 = v_stack_m2F8;
    v_stack_m310 = v_stack_m2D0;
    v_stack_m318 = (uint16_t)(*(uint16_t *)(arg1));
    result = CmpCloneHwProfile(v_stack_m2D8, v_stack_m280, v_stack_m2D0, (uint32_t)(v_stack_m2F8));
loc_007E29DC:
    if (!sign_flag) goto loc_007E2A6A;
    goto loc_007E2B26;
loc_007E29F1:
    result = ZwClose(v_stack_m2D0, v_stack_m280, v_stack_m2D0, (uint32_t)(v_stack_m2F8));
    result = swprintf_s(v_stack_m148, 128, v_rip + 3303481, (uint32_t)(v_stack_m2F8));
    result = RtlInitUnicodeString(v_stack_m2E8, v_stack_m148, v_rip + 3303481, (uint32_t)(v_stack_m2F8));
    v_stack_m2B8 = v_stack_m280;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_stack_m2E8;
    v_stack_m2A8 = 576;
    v_stack_m2A0 = v_xmm0;
    result = ZwOpenKey(v_stack_m2D0, (uint32_t)(0x20019ULL), v_stack_m2C0, (uint32_t)(v_stack_m2F8));
    goto loc_007E29DC;
loc_007E2A6A:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3263567, v_stack_m2C0, (uint32_t)(v_stack_m2F8));
    v_stack_m2B8 = v_stack_m2D8;
    v_stack_m2C0 = 48;
    v_stack_m2B0 = v_stack_m2E8;
    v_stack_m2A8 = 576;
    v_stack_m308 = v_stack_m288;
    Arg4 = 0;
    v_stack_m310 = 1;
    v_stack_m2A0 = v_xmm0;
    result = ZwCreateKey(v_stack_m2F0, (uint32_t)(0x2001FULL), v_stack_m2C0, Arg4);
    if (!sign_flag) goto loc_007E2AE0;
    goto loc_007E2B26;
loc_007E2AE0:
    result = RtlInitUnicodeString(v_stack_m2E8, v_rip + 3303225, v_stack_m2C0, Arg4);
    v_stack_m310 = 4;
    Arg3 = 0;
    v_stack_m318 = v_stack_m2F8;
    result = ZwSetValueKey(v_stack_m2D8, v_stack_m2E8, Arg3, 4);
    if (!sign_flag) goto loc_007E2C46;
loc_007E2B21:
loc_007E2B26:
    if (v_stack_m2D0 != 0) {
        result = ZwClose(v_stack_m2D0, v_stack_m2E8, Arg3, 4);
    }
    if (v_stack_m270 != 0) {
        result = ZwClose(v_stack_m270, v_stack_m2E8, Arg3, 4);
    }
    if (v_stack_m2D8 != 0) {
        result = ZwClose(v_stack_m2D8, v_stack_m2E8, Arg3, 4);
    }
    if (v_stack_m2F0 != 0) {
        result = ZwClose(v_stack_m2F0, v_stack_m2E8, Arg3, 4);
    }
    if (v_stack_m280 != 0) {
        result = ZwClose(v_stack_m280, v_stack_m2E8, Arg3, 4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, 4);
    }
    if (v_stack_m290 == 0) goto loc_007E2BC8;
    Arg2 = 0;
    v_stack_m2F4 = 0;
    if ((*(uint32_t *)(v_stack_m290 + 0x4)) <= 0) goto loc_007E2BC1;
    result = 0;
loc_007E2B94:
    result = (result) << (5);
    if (*(uint64_t *)(result + v_stack_m290 * 1 + 0x10) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(result + v_stack_m290 * 1 + 0x10);
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(result + v_stack_m290 * 1 + 0x10), 4);
        Arg2 = v_stack_m2F4;
        Arg1 = v_stack_m290;
    }
    Arg2 = (uint32_t)((Arg2) + 1);
    v_stack_m2F4 = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) < (*(uint32_t *)(arg1 + 0x4))) goto loc_007E2B94;
loc_007E2BC1:
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(result + v_stack_m290 * 1 + 0x10), 4);
loc_007E2BC8:
    if (v_stack_m278 == 0) goto loc_007E2C14;
    Arg2 = 0;
    v_stack_m2F4 = 0;
    if ((*(uint32_t *)(v_stack_m278 + 0x4)) <= 0) goto loc_007E2C0D;
    result = 0;
loc_007E2BDE:
    result = (result) + 1;
    result = result + result * 2;
    if (*(uint64_t *)(v_stack_m278 + result + result * 2 * 8) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_m278 + result + result * 2 * 8);
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(v_stack_m278 + result + result * 2 * 8), 4);
        Arg2 = v_stack_m2F4;
        Arg1 = v_stack_m278;
    }
    Arg2 = (uint32_t)((Arg2) + 1);
    v_stack_m2F4 = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) < (*(uint32_t *)(arg1 + 0x4))) goto loc_007E2BDE;
loc_007E2C0D:
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(v_stack_m278 + result + result * 2 * 8), 4);
loc_007E2C14:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(v_stack_m278 + result + result * 2 * 8), 4);
    local_rsp = (local_rsp) + (768);
    return result;
loc_007E2C41:
loc_007E2C46:
    v_stack_p44 = (uint32_t)(*(uint16_t *)(arg1));
    result = RtlInitUnicodeString(v_stack_p50, v_rip + 3303006, *(uint64_t *)(v_stack_m278 + result + result * 2 * 8), 4);
    v_stack_p28 = 4;
    v_stack_p20 = v_stack_p44;
    Arg3 = 0;
    result = ZwSetValueKey(v_stack_p48, v_stack_p50, Arg3, 4);
    result = RtlInitUnicodeString(v_stack_p50, v_rip + 3302854, Arg3, 4);
    v_stack_p28 = (uint32_t)(*(uint16_t *)(arg1 + 0x2));
    v_stack_p20 = Arg1 + 4;
    Arg3 = 0;
    result = ZwSetValueKey(v_stack_p48, v_stack_p50, Arg3, 3);
    local_rbx = (uint32_t)((uint32_t)(result));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + v_stack_m290 * 1 + 0x20)))) & (2)) == 0) {
        Arg3 = v_stack_p40;
        Arg4 = v_stack_m148;
        Arg1 = v_stack_p60;
        Arg2 = Arg1;
        result = CmpAddAcpiAliasEntry(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (v_stack_p40 != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m238 + (uint32_t)(v_stack_m240) * 1 - 0x10))))) {
        result = v_rip + 3572268;
        v_stack_p78 = 48;
        Arg4 = 0;
        v_stack_m2B0 = result;
        result = v_stack_m288;
        v_stack_m2B8 = v_stack_m268;
        v_stack_p30 = result;
        Arg3 = v_stack_p78;
        v_stack_p28 = 8;
        Arg2 = Arg4 + 32;
        Arg1 = v_stack_m270;
        v_stack_m2A8 = 832;
        v_stack_m2A0 = v_xmm0;
        result = ZwCreateKey(Arg1, Arg2, Arg3, Arg4);
        Arg4 = v_stack_p40;
        Arg3 = v_stack_m258;
        Arg2 = v_rip + 3302446;
        v_stack_p50 = v_xmm0;
        result = 256;
        Arg1 = v_stack_p50;
        v_stack_p52 = (uint16_t)(result);
        result = v_stack_m148;
        v_stack_p58 = result;
        result = RtlUnicodeStringPrintf(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_p50;
        Arg2 = v_rip + 8351357;
        Arg1 = v_stack_m270;
        Arg4 = 6;
        v_stack_p28 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_p58;
        v_stack_p20 = result;
        result = ZwSetValueKey(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (sign_flag) goto loc_007E2B26;
    *(uint64_t *)(v_stack_m260) = v_stack_p68;
    goto loc_007E2B35;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x4` | `64` | `R` |
| `Arg5` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E2584&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
