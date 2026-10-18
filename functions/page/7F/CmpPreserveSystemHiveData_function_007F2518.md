# CmpPreserveSystemHiveData

- RVA: `0x007F2518`–`0x007F2DED` (길이 `2,261` bytes)
- VA: `0x00000001407F2518`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D732C`
- 디코드: `576`개 명령, `2,261/2,261` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **72**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x007F2653` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F265A` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F267B` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F2682` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F26BF` → [CmpWalkPath](CmpWalkPath_function_007F36BC.md) (function, `0x007F36BC`)
- `0x007F26D0` → [CmpWalkPath](CmpWalkPath_function_007F36BC.md) (function, `0x007F36BC`)
- `0x007F26FD` → [CmpCopySyncTree](CmpCopySyncTree_function_007F21A0.md) (function, `0x007F21A0`)
- `0x007F274C` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F275D` → [CmpWalkPath](CmpWalkPath_function_007F36BC.md) (function, `0x007F36BC`)
- `0x007F2786` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F278D` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F27AE` → [CmpFindValueByName](../84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x007F27C6` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F27CD` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F27F0` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F27F7` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F2826` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F282D` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F284D` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2857` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2875` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F287C` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F28A9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007F28CE` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F28D5` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F28F4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007F2909` → [CmpWalkPath](CmpWalkPath_function_007F36BC.md) (function, `0x007F36BC`)
- `0x007F2922` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2929` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F294E` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2955` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F297E` → [CmpWalkPath](CmpWalkPath_function_007F36BC.md) (function, `0x007F36BC`)
- `0x007F29B2` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F29B9` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F29D8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007F29E7` → [CmpFindValueByName](../84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x007F2A11` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F2A18` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F2A60` → [CmpGetValueData](../85/CmpGetValueData_function_00856DB0.md) (function, `0x00856DB0`)
- `0x007F2AA7` → [CmpFindSubKeyByNumber](../85/CmpFindSubKeyByNumber_function_0085C930.md) (function, `0x0085C930`)
- `0x007F2AC5` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F2ACC` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F2AF4` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2AFE` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2B1F` → [strnicmp](../../text/4F/strnicmp_function_004FFE30.md) (function, `0x004FFE30`)
- `0x007F2B2D` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x007F2B4A` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2B51` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2BA5` → [CmpWalkPath](CmpWalkPath_function_007F36BC.md) (function, `0x007F36BC`)
- `0x007F2BD6` → [CmpCopySyncTree](CmpCopySyncTree_function_007F21A0.md) (function, `0x007F21A0`)
- `0x007F2BF3` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F2BFA` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F2C12` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007F2C21` → [CmpFindValueByName](../84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x007F2C3C` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2C43` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2C66` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007F2C6D` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007F2CA9` → [CmpSetValueKeyExisting](../84/CmpSetValueKeyExisting_function_0084B53C.md) (function, `0x0084B53C`)
- `0x007F2CC1` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2CC8` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2CFB` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2D20` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2D27` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2D3E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007F2D5F` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2D66` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2D97` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2D9E` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2DBB` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007F2DC2` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007F2DD1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [CmReplaceKey](../7E/CmReplaceKey_function_007EA1C8.md) at `0x007EA2E0`

### Static image references
- `0x007F2531` → RVA `0x00B09B80` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007F2541` → RVA `0x00B09BE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007F255E` → RVA `0x00B09C10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007F2572` → RVA `0x00B09BB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007F2756` → RVA `0x00B00370` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007F27A1` → RVA `0x00FD9C00` (`PAGEDATA`; read)
- `0x007F2B18` → RVA `0x00B09BD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007F2B26` → RVA `0x00B09B90` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x007F28A9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007F28F4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007F29D8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007F2B1F` → [strnicmp](../../text/4F/strnicmp_function_004FFE30.md) (`PAGE` → `.text`)
  - `0x007F2B2D` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x007F2C12` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007F2D3E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007F2DD1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F2518  40 55                           push rbp
007F251A  53                              push rbx
007F251B  56                              push rsi
007F251C  57                              push rdi
007F251D  41 54                           push r12
007F251F  41 55                           push r13
007F2521  41 56                           push r14
007F2523  41 57                           push r15
007F2525  48 8D 6C 24 A8                  lea rbp, [rsp - 0x58]
007F252A  48 81 EC 58 01 00 00            sub rsp, 0x158
007F2531  48 8D 05 48 76 31 00            lea rax, [rip + 0x317648]
007F2538  48 8B F9                        mov rdi, rcx
007F253B  33 C9                           xor ecx, ecx
007F253D  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
007F2541  48 8D 05 98 76 31 00            lea rax, [rip + 0x317698]
007F2548  89 8D A0 00 00 00               mov dword ptr [rbp + 0xa0], ecx
007F254E  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
007F2552  48 8B F2                        mov rsi, rdx
007F2555  83 CA FF                        or edx, 0xffffffff
007F2558  89 8D BC 00 00 00               mov dword ptr [rbp + 0xbc], ecx
007F255E  48 8D 05 AB 76 31 00            lea rax, [rip + 0x3176ab]
007F2565  89 95 B8 00 00 00               mov dword ptr [rbp + 0xb8], edx
007F256B  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
007F256F  0F 57 C0                        xorps xmm0, xmm0
007F2572  48 8D 05 37 76 31 00            lea rax, [rip + 0x317637]
007F2579  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
007F257D  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
007F2581  44 8B E9                        mov r13d, ecx
007F2584  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
007F2588  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
007F258C  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
007F2590  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
007F2594  44 8B 60 24                     mov r12d, dword ptr [rax + 0x24]
007F2598  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
007F259C  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
007F25A0  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
007F25A4  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
007F25A8  44 8B 78 24                     mov r15d, dword ptr [rax + 0x24]
007F25AC  89 4C 24 4C                     mov dword ptr [rsp + 0x4c], ecx
007F25B0  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
007F25B4  89 4C 24 5C                     mov dword ptr [rsp + 0x5c], ecx
007F25B8  89 95 A8 00 00 00               mov dword ptr [rbp + 0xa8], edx
007F25BE  89 8D AC 00 00 00               mov dword ptr [rbp + 0xac], ecx
007F25C4  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
007F25C8  89 55 90                        mov dword ptr [rbp - 0x70], edx
007F25CB  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
007F25CF  89 55 A0                        mov dword ptr [rbp - 0x60], edx
007F25D2  89 4D A4                        mov dword ptr [rbp - 0x5c], ecx
007F25D5  89 55 A8                        mov dword ptr [rbp - 0x58], edx
007F25D8  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
007F25DC  89 55 B8                        mov dword ptr [rbp - 0x48], edx
007F25DF  89 4D BC                        mov dword ptr [rbp - 0x44], ecx
007F25E2  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
007F25E6  89 55 C8                        mov dword ptr [rbp - 0x38], edx
007F25E9  48 89 4D CC                     mov qword ptr [rbp - 0x34], rcx
007F25ED  88 4D D4                        mov byte ptr [rbp - 0x2c], cl
007F25F0  89 55 E8                        mov dword ptr [rbp - 0x18], edx
007F25F3  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
007F25F7  89 55 F8                        mov dword ptr [rbp - 8], edx
007F25FA  89 4D FC                        mov dword ptr [rbp - 4], ecx
007F25FD  89 55 00                        mov dword ptr [rbp], edx
007F2600  48 89 4D 08                     mov qword ptr [rbp + 8], rcx
007F2604  89 55 10                        mov dword ptr [rbp + 0x10], edx
007F2607  89 4D 14                        mov dword ptr [rbp + 0x14], ecx
007F260A  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
007F260E  89 55 20                        mov dword ptr [rbp + 0x20], edx
007F2611  48 89 4D 24                     mov qword ptr [rbp + 0x24], rcx
007F2615  88 4D 2C                        mov byte ptr [rbp + 0x2c], cl
007F2618  48 89 8D B0 00 00 00            mov qword ptr [rbp + 0xb0], rcx
007F261F  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
007F2624  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
007F2629  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
007F262D  44 3B E2                        cmp r12d, edx
007F2630  0F 84 BB 06 00 00               je 0x1407f2cf1
007F2636  44 3B FA                        cmp r15d, edx
007F2639  0F 84 B2 06 00 00               je 0x1407f2cf1
007F263F  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F2646  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
007F264B  41 8B D4                        mov edx, r12d
007F264E  48 8B CF                        mov rcx, rdi
007F2651  74 07                           je 0x1407f265a
007F2653  E8 08 26 06 00                  call 0x140854c60
007F2658  EB 05                           jmp 0x1407f265f
007F265A  E8 51 26 06 00                  call 0x140854cb0
007F265F  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
007F2666  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
007F266B  48 8B D8                        mov rbx, rax
007F266E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
007F2673  41 8B D7                        mov edx, r15d
007F2676  48 8B CE                        mov rcx, rsi
007F2679  74 07                           je 0x1407f2682
007F267B  E8 E0 25 06 00                  call 0x140854c60
007F2680  EB 05                           jmp 0x1407f2687
007F2682  E8 29 26 06 00                  call 0x140854cb0
007F2687  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
007F268C  48 8B C8                        mov rcx, rax
007F268F  48 85 DB                        test rbx, rbx
007F2692  0F 84 4F 06 00 00               je 0x1407f2ce7
007F2698  48 85 C0                        test rax, rax
007F269B  0F 84 46 06 00 00               je 0x1407f2ce7
007F26A1  45 8B F5                        mov r14d, r13d
007F26A4  41 8B D4                        mov edx, r12d
007F26A7  48 8B CF                        mov rcx, rdi
007F26AA  41 83 FE 01                     cmp r14d, 1
007F26AE  0F 83 A2 00 00 00               jae 0x1407f2756
007F26B4  41 8B C6                        mov eax, r14d
007F26B7  48 8B 5C C5 40                  mov rbx, qword ptr [rbp + rax*8 + 0x40]
007F26BC  4C 8B C3                        mov r8, rbx
007F26BF  E8 F8 0F 00 00                  call 0x1407f36bc
007F26C4  4C 8B C3                        mov r8, rbx
007F26C7  41 8B D7                        mov edx, r15d
007F26CA  48 8B CE                        mov rcx, rsi
007F26CD  44 8B E8                        mov r13d, eax
007F26D0  E8 E7 0F 00 00                  call 0x1407f36bc
007F26D5  83 C9 FF                        or ecx, 0xffffffff
007F26D8  44 3B E9                        cmp r13d, ecx
007F26DB  74 33                           je 0x1407f2710
007F26DD  3B C1                           cmp eax, ecx
007F26DF  74 2F                           je 0x1407f2710
007F26E1  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
007F26E9  44 8B C8                        mov r9d, eax
007F26EC  4C 8B C6                        mov r8, rsi
007F26EF  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
007F26F7  41 8B D5                        mov edx, r13d
007F26FA  48 8B CF                        mov rcx, rdi
007F26FD  E8 9E FA FF FF                  call 0x1407f21a0
007F2702  45 33 ED                        xor r13d, r13d
007F2705  8B D8                           mov ebx, eax
007F2707  85 C0                           test eax, eax
007F2709  78 11                           js 0x1407f271c
007F270B  41 FF C6                        inc r14d
007F270E  EB 94                           jmp 0x1407f26a4
007F2710  BB 4C 01 00 C0                  mov ebx, 0xc000014c
007F2715  4C 8B AD B0 00 00 00            mov r13, qword ptr [rbp + 0xb0]
007F271C  45 33 FF                        xor r15d, r15d
007F271F  4C 8D 75 B0                     lea r14, [rbp - 0x50]
007F2723  49 83 7E E8 00                  cmp qword ptr [r14 - 0x18], 0
007F2728  0F 84 D2 05 00 00               je 0x1407f2d00
007F272E  41 8B C7                        mov eax, r15d
007F2731  48 8D 55 A0                     lea rdx, [rbp - 0x60]
007F2735  48 6B C8 58                     imul rcx, rax, 0x58
007F2739  48 03 D1                        add rdx, rcx
007F273C  48 8B CF                        mov rcx, rdi
007F273F  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F2746  0F 84 AF 05 00 00               je 0x1407f2cfb
007F274C  E8 CF A4 06 00                  call 0x14085cc20
007F2751  E9 AA 05 00 00                  jmp 0x1407f2d00
007F2756  4C 8D 05 13 DC 30 00            lea r8, [rip + 0x30dc13]
007F275D  E8 5A 0F 00 00                  call 0x1407f36bc
007F2762  41 83 CF FF                     or r15d, 0xffffffff
007F2766  44 8B F0                        mov r14d, eax
007F2769  41 3B C7                        cmp eax, r15d
007F276C  75 05                           jne 0x1407f2773
007F276E  41 8B DD                        mov ebx, r13d
007F2771  EB A2                           jmp 0x1407f2715
007F2773  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F277A  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
007F277F  8B D0                           mov edx, eax
007F2781  48 8B CF                        mov rcx, rdi
007F2784  74 07                           je 0x1407f278d
007F2786  E8 D5 24 06 00                  call 0x140854c60
007F278B  EB 05                           jmp 0x1407f2792
007F278D  E8 1E 25 06 00                  call 0x140854cb0
007F2792  48 85 C0                        test rax, rax
007F2795  75 0A                           jne 0x1407f27a1
007F2797  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007F279C  E9 74 FF FF FF                  jmp 0x1407f2715
007F27A1  4C 8D 05 58 74 7E 00            lea r8, [rip + 0x7e7458]
007F27A8  48 8B D0                        mov rdx, rax
007F27AB  48 8B CF                        mov rcx, rdi
007F27AE  E8 69 26 05 00                  call 0x140844e1c
007F27B3  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F27BA  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
007F27BF  8B D8                           mov ebx, eax
007F27C1  48 8B CF                        mov rcx, rdi
007F27C4  74 07                           je 0x1407f27cd
007F27C6  E8 55 A4 06 00                  call 0x14085cc20
007F27CB  EB 05                           jmp 0x1407f27d2
007F27CD  E8 6E 37 06 00                  call 0x140855f40
007F27D2  41 3B DF                        cmp ebx, r15d
007F27D5  0F 84 7F 01 00 00               je 0x1407f295a
007F27DB  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F27E2  4C 8D 85 A8 00 00 00            lea r8, [rbp + 0xa8]
007F27E9  8B D3                           mov edx, ebx
007F27EB  48 8B CF                        mov rcx, rdi
007F27EE  74 07                           je 0x1407f27f7
007F27F0  E8 6B 24 06 00                  call 0x140854c60
007F27F5  EB 05                           jmp 0x1407f27fc
007F27F7  E8 B4 24 06 00                  call 0x140854cb0
007F27FC  48 8B D8                        mov rbx, rax
007F27FF  48 85 C0                        test rax, rax
007F2802  0F 84 52 01 00 00               je 0x1407f295a
007F2808  83 78 0C 06                     cmp dword ptr [rax + 0xc], 6
007F280C  48 8B CF                        mov rcx, rdi
007F280F  0F 85 29 01 00 00               jne 0x1407f293e
007F2815  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F281C  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
007F2821  8B 50 08                        mov edx, dword ptr [rax + 8]
007F2824  74 07                           je 0x1407f282d
007F2826  E8 35 24 06 00                  call 0x140854c60
007F282B  EB 05                           jmp 0x1407f2832
007F282D  E8 7E 24 06 00                  call 0x140854cb0
007F2832  48 8D 95 A8 00 00 00            lea rdx, [rbp + 0xa8]
007F2839  4C 8B F8                        mov r15, rax
007F283C  48 8B CF                        mov rcx, rdi
007F283F  48 85 C0                        test rax, rax
007F2842  75 1D                           jne 0x1407f2861
007F2844  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F284B  74 0A                           je 0x1407f2857
007F284D  E8 CE A3 06 00                  call 0x14085cc20
007F2852  E9 40 FF FF FF                  jmp 0x1407f2797
007F2857  E8 E4 36 06 00                  call 0x140855f40
007F285C  E9 36 FF FF FF                  jmp 0x1407f2797
007F2861  44 8B 73 04                     mov r14d, dword ptr [rbx + 4]
007F2865  49 83 C6 FE                     add r14, -2
007F2869  4D 03 F7                        add r14, r15
007F286C  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F2873  74 07                           je 0x1407f287c
007F2875  E8 A6 A3 06 00                  call 0x14085cc20
007F287A  EB 05                           jmp 0x1407f2881
007F287C  E8 BF 36 06 00                  call 0x140855f40
007F2881  41 8B DD                        mov ebx, r13d
007F2884  EB 0B                           jmp 0x1407f2891
007F2886  4D 3B F7                        cmp r14, r15
007F2889  72 0D                           jb 0x1407f2898
007F288B  FF C3                           inc ebx
007F288D  49 83 EE 02                     sub r14, 2
007F2891  66 41 83 3E 5C                  cmp word ptr [r14], 0x5c
007F2896  75 EE                           jne 0x1407f2886
007F2898  8D 53 01                        lea edx, [rbx + 1]
007F289B  B9 00 01 00 00                  mov ecx, 0x100
007F28A0  48 03 D2                        add rdx, rdx
007F28A3  41 B8 43 4D 50 68               mov r8d, 0x68504d43
007F28A9  E8 42 F8 38 00                  call 0x140b820f0
007F28AE  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
007F28B5  4C 8B E8                        mov r13, rax
007F28B8  48 85 C0                        test rax, rax
007F28BB  75 27                           jne 0x1407f28e4
007F28BD  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F28C4  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007F28C9  48 8B CF                        mov rcx, rdi
007F28CC  74 07                           je 0x1407f28d5
007F28CE  E8 4D A3 06 00                  call 0x14085cc20
007F28D3  EB 05                           jmp 0x1407f28da
007F28D5  E8 66 36 06 00                  call 0x140855f40
007F28DA  BB 17 00 00 C0                  mov ebx, 0xc0000017
007F28DF  E9 38 FE FF FF                  jmp 0x1407f271c
007F28E4  8B C3                           mov eax, ebx
007F28E6  49 8D 56 02                     lea rdx, [r14 + 2]
007F28EA  49 8B CD                        mov rcx, r13
007F28ED  48 8D 1C 00                     lea rbx, [rax + rax]
007F28F1  4C 8B C3                        mov r8, rbx
007F28F4  E8 47 3F ED FF                  call 0x1406c6840
007F28F9  33 C0                           xor eax, eax
007F28FB  4D 8B C5                        mov r8, r13
007F28FE  41 8B D4                        mov edx, r12d
007F2901  66 42 89 04 2B                  mov word ptr [rbx + r13], ax
007F2906  48 8B CF                        mov rcx, rdi
007F2909  E8 AE 0D 00 00                  call 0x1407f36bc
007F290E  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F2915  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007F291A  44 8B F0                        mov r14d, eax
007F291D  48 8B CF                        mov rcx, rdi
007F2920  74 07                           je 0x1407f2929
007F2922  E8 F9 A2 06 00                  call 0x14085cc20
007F2927  EB 05                           jmp 0x1407f292e
007F2929  E8 12 36 06 00                  call 0x140855f40
007F292E  41 83 CF FF                     or r15d, 0xffffffff
007F2932  45 3B F7                        cmp r14d, r15d
007F2935  75 23                           jne 0x1407f295a
007F2937  33 DB                           xor ebx, ebx
007F2939  E9 DE FD FF FF                  jmp 0x1407f271c
007F293E  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F2945  48 8D 95 A8 00 00 00            lea rdx, [rbp + 0xa8]
007F294C  74 07                           je 0x1407f2955
007F294E  E8 CD A2 06 00                  call 0x14085cc20
007F2953  EB 05                           jmp 0x1407f295a
007F2955  E8 E6 35 06 00                  call 0x140855f40
007F295A  33 DB                           xor ebx, ebx
007F295C  44 8A EB                        mov r13b, bl
007F295F  44 8B E3                        mov r12d, ebx
007F2962  41 83 FC 02                     cmp r12d, 2
007F2966  0F 83 0E 01 00 00               jae 0x1407f2a7a
007F296C  41 8B C4                        mov eax, r12d
007F296F  41 8B D6                        mov edx, r14d
007F2972  48 6B D8 58                     imul rbx, rax, 0x58
007F2976  48 8B CF                        mov rcx, rdi
007F2979  4C 8B 44 1D 80                  mov r8, qword ptr [rbp + rbx - 0x80]
007F297E  E8 39 0D 00 00                  call 0x1407f36bc
007F2983  89 44 1D 90                     mov dword ptr [rbp + rbx - 0x70], eax
007F2987  8B D0                           mov edx, eax
007F2989  41 3B C7                        cmp eax, r15d
007F298C  0F 84 E0 00 00 00               je 0x1407f2a72
007F2992  33 C0                           xor eax, eax
007F2994  48 39 44 1D 88                  cmp qword ptr [rbp + rbx - 0x78], rax
007F2999  0F 84 D0 00 00 00               je 0x1407f2a6f
007F299F  4C 8D 45 A0                     lea r8, [rbp - 0x60]
007F29A3  48 8B CF                        mov rcx, rdi
007F29A6  4C 03 C3                        add r8, rbx
007F29A9  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F29B0  74 07                           je 0x1407f29b9
007F29B2  E8 A9 22 06 00                  call 0x140854c60
007F29B7  EB 05                           jmp 0x1407f29be
007F29B9  E8 F2 22 06 00                  call 0x140854cb0
007F29BE  48 89 44 1D 98                  mov qword ptr [rbp + rbx - 0x68], rax
007F29C3  4C 8B F8                        mov r15, rax
007F29C6  48 85 C0                        test rax, rax
007F29C9  0F 84 C8 FD FF FF               je 0x1407f2797
007F29CF  48 8B 54 1D 88                  mov rdx, qword ptr [rbp + rbx - 0x78]
007F29D4  48 8D 4D 30                     lea rcx, [rbp + 0x30]
007F29D8  E8 A3 7D C3 FF                  call 0x14042a780
007F29DD  4C 8D 45 30                     lea r8, [rbp + 0x30]
007F29E1  49 8B D7                        mov rdx, r15
007F29E4  48 8B CF                        mov rcx, rdi
007F29E7  E8 30 24 05 00                  call 0x140844e1c
007F29EC  41 83 CF FF                     or r15d, 0xffffffff
007F29F0  89 44 1D A8                     mov dword ptr [rbp + rbx - 0x58], eax
007F29F4  8B D0                           mov edx, eax
007F29F6  41 3B C7                        cmp eax, r15d
007F29F9  74 77                           je 0x1407f2a72
007F29FB  4C 8D 45 B8                     lea r8, [rbp - 0x48]
007F29FF  41 B5 01                        mov r13b, 1
007F2A02  4C 03 C3                        add r8, rbx
007F2A05  48 8B CF                        mov rcx, rdi
007F2A08  44 84 AF 8C 00 00 00            test byte ptr [rdi + 0x8c], r13b
007F2A0F  74 07                           je 0x1407f2a18
007F2A11  E8 4A 22 06 00                  call 0x140854c60
007F2A16  EB 05                           jmp 0x1407f2a1d
007F2A18  E8 93 22 06 00                  call 0x140854cb0
007F2A1D  48 89 44 1D B0                  mov qword ptr [rbp + rbx - 0x50], rax
007F2A22  4C 8B C0                        mov r8, rax
007F2A25  48 85 C0                        test rax, rax
007F2A28  0F 84 69 FD FF FF               je 0x1407f2797
007F2A2E  48 8D 45 C8                     lea rax, [rbp - 0x38]
007F2A32  48 03 C3                        add rax, rbx
007F2A35  48 8D 4D D4                     lea rcx, [rbp - 0x2c]
007F2A39  48 03 CB                        add rcx, rbx
007F2A3C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007F2A41  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
007F2A46  48 8D 55 C0                     lea rdx, [rbp - 0x40]
007F2A4A  48 03 D3                        add rdx, rbx
007F2A4D  4C 8D 4D D0                     lea r9, [rbp - 0x30]
007F2A51  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
007F2A56  4C 03 CB                        add r9, rbx
007F2A59  8B 54 1D A8                     mov edx, dword ptr [rbp + rbx - 0x58]
007F2A5D  48 8B CF                        mov rcx, rdi
007F2A60  E8 4B 43 06 00                  call 0x140856db0
007F2A65  84 C0                           test al, al
007F2A67  0F 84 A3 FC FF FF               je 0x1407f2710
007F2A6D  EB 03                           jmp 0x1407f2a72
007F2A6F  41 B5 01                        mov r13b, 1
007F2A72  41 FF C4                        inc r12d
007F2A75  E9 E8 FE FF FF                  jmp 0x1407f2962
007F2A7A  33 DB                           xor ebx, ebx
007F2A7C  45 84 ED                        test r13b, r13b
007F2A7F  0F 84 90 FC FF FF               je 0x1407f2715
007F2A85  44 8B EB                        mov r13d, ebx
007F2A88  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007F2A8D  44 3B 69 14                     cmp r13d, dword ptr [rcx + 0x14]
007F2A91  0F 83 7E FC FF FF               jae 0x1407f2715
007F2A97  48 8B D1                        mov rdx, rcx
007F2A9A  4C 8D 8D A0 00 00 00            lea r9, [rbp + 0xa0]
007F2AA1  48 8B CE                        mov rcx, rsi
007F2AA4  45 8B C5                        mov r8d, r13d
007F2AA7  E8 84 9E 06 00                  call 0x14085c930
007F2AAC  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
007F2AB3  4C 8D 85 B8 00 00 00            lea r8, [rbp + 0xb8]
007F2ABA  8B 95 A0 00 00 00               mov edx, dword ptr [rbp + 0xa0]
007F2AC0  48 8B CE                        mov rcx, rsi
007F2AC3  74 07                           je 0x1407f2acc
007F2AC5  E8 96 21 06 00                  call 0x140854c60
007F2ACA  EB 05                           jmp 0x1407f2ad1
007F2ACC  E8 DF 21 06 00                  call 0x140854cb0
007F2AD1  48 85 C0                        test rax, rax
007F2AD4  0F 84 BD FC FF FF               je 0x1407f2797
007F2ADA  66 83 78 48 0D                  cmp word ptr [rax + 0x48], 0xd
007F2ADF  74 27                           je 0x1407f2b08
007F2AE1  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
007F2AE8  48 8D 95 B8 00 00 00            lea rdx, [rbp + 0xb8]
007F2AEF  48 8B CE                        mov rcx, rsi
007F2AF2  74 0A                           je 0x1407f2afe
007F2AF4  E8 27 A1 06 00                  call 0x14085cc20
007F2AF9  E9 E1 01 00 00                  jmp 0x1407f2cdf
007F2AFE  E8 3D 34 06 00                  call 0x140855f40
007F2B03  E9 D7 01 00 00                  jmp 0x1407f2cdf
007F2B08  F6 40 02 20                     test byte ptr [rax + 2], 0x20
007F2B0C  48 8D 48 4C                     lea rcx, [rax + 0x4c]
007F2B10  41 B8 0A 00 00 00               mov r8d, 0xa
007F2B16  74 0E                           je 0x1407f2b26
007F2B18  48 8D 15 B1 70 31 00            lea rdx, [rip + 0x3170b1]
007F2B1F  E8 0C D3 D0 FF                  call 0x1404ffe30
007F2B24  EB 0C                           jmp 0x1407f2b32
007F2B26  48 8D 15 63 70 31 00            lea rdx, [rip + 0x317063]
007F2B2D  E8 8E D6 D0 FF                  call 0x1405001c0
007F2B32  85 C0                           test eax, eax
007F2B34  48 8D 95 B8 00 00 00            lea rdx, [rbp + 0xb8]
007F2B3B  48 8B CE                        mov rcx, rsi
007F2B3E  0F 94 C3                        sete bl
007F2B41  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
007F2B48  74 07                           je 0x1407f2b51
007F2B4A  E8 D1 A0 06 00                  call 0x14085cc20
007F2B4F  EB 05                           jmp 0x1407f2b56
007F2B51  E8 EA 33 06 00                  call 0x140855f40
007F2B56  45 33 FF                        xor r15d, r15d
007F2B59  84 DB                           test bl, bl
007F2B5B  0F 84 7C 01 00 00               je 0x1407f2cdd
007F2B61  41 83 FF 02                     cmp r15d, 2
007F2B65  0F 83 72 01 00 00               jae 0x1407f2cdd
007F2B6B  41 8B C7                        mov eax, r15d
007F2B6E  48 6B D8 58                     imul rbx, rax, 0x58
007F2B72  83 C8 FF                        or eax, 0xffffffff
007F2B75  44 8B 74 1D 90                  mov r14d, dword ptr [rbp + rbx - 0x70]
007F2B7A  44 3B F0                        cmp r14d, eax
007F2B7D  0F 84 52 01 00 00               je 0x1407f2cd5
007F2B83  4C 8B 64 1D 88                  mov r12, qword ptr [rbp + rbx - 0x78]
007F2B88  4D 85 E4                        test r12, r12
007F2B8B  74 0A                           je 0x1407f2b97
007F2B8D  39 44 1D A8                     cmp dword ptr [rbp + rbx - 0x58], eax
007F2B91  0F 84 3E 01 00 00               je 0x1407f2cd5
007F2B97  4C 8B 44 1D 80                  mov r8, qword ptr [rbp + rbx - 0x80]
007F2B9C  48 8B CE                        mov rcx, rsi
007F2B9F  8B 95 A0 00 00 00               mov edx, dword ptr [rbp + 0xa0]
007F2BA5  E8 12 0B 00 00                  call 0x1407f36bc
007F2BAA  8B D0                           mov edx, eax
007F2BAC  83 F8 FF                        cmp eax, -1
007F2BAF  0F 84 20 01 00 00               je 0x1407f2cd5
007F2BB5  4D 85 E4                        test r12, r12
007F2BB8  75 26                           jne 0x1407f2be0
007F2BBA  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
007F2BC2  44 8B C8                        mov r9d, eax
007F2BC5  4C 8B C6                        mov r8, rsi
007F2BC8  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
007F2BD0  41 8B D6                        mov edx, r14d
007F2BD3  48 8B CF                        mov rcx, rdi
007F2BD6  E8 C5 F5 FF FF                  call 0x1407f21a0
007F2BDB  E9 F5 00 00 00                  jmp 0x1407f2cd5
007F2BE0  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
007F2BE7  4C 8D 85 B8 00 00 00            lea r8, [rbp + 0xb8]
007F2BEE  48 8B CE                        mov rcx, rsi
007F2BF1  74 07                           je 0x1407f2bfa
007F2BF3  E8 68 20 06 00                  call 0x140854c60
007F2BF8  EB 05                           jmp 0x1407f2bff
007F2BFA  E8 B1 20 06 00                  call 0x140854cb0
007F2BFF  4C 8B F0                        mov r14, rax
007F2C02  48 85 C0                        test rax, rax
007F2C05  0F 84 8C FB FF FF               je 0x1407f2797
007F2C0B  49 8B D4                        mov rdx, r12
007F2C0E  48 8D 4D 30                     lea rcx, [rbp + 0x30]
007F2C12  E8 69 7B C3 FF                  call 0x14042a780
007F2C17  4C 8D 45 30                     lea r8, [rbp + 0x30]
007F2C1B  49 8B D6                        mov rdx, r14
007F2C1E  48 8B CE                        mov rcx, rsi
007F2C21  E8 F6 21 05 00                  call 0x140844e1c
007F2C26  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
007F2C2D  48 8D 95 B8 00 00 00            lea rdx, [rbp + 0xb8]
007F2C34  44 8B F0                        mov r14d, eax
007F2C37  48 8B CE                        mov rcx, rsi
007F2C3A  74 07                           je 0x1407f2c43
007F2C3C  E8 DF 9F 06 00                  call 0x14085cc20
007F2C41  EB 05                           jmp 0x1407f2c48
007F2C43  E8 F8 32 06 00                  call 0x140855f40
007F2C48  41 83 FE FF                     cmp r14d, -1
007F2C4C  0F 84 83 00 00 00               je 0x1407f2cd5
007F2C52  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
007F2C59  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
007F2C5E  41 8B D6                        mov edx, r14d
007F2C61  48 8B CE                        mov rcx, rsi
007F2C64  74 07                           je 0x1407f2c6d
007F2C66  E8 F5 1F 06 00                  call 0x140854c60
007F2C6B  EB 05                           jmp 0x1407f2c72
007F2C6D  E8 3E 20 06 00                  call 0x140854cb0
007F2C72  4C 8B C0                        mov r8, rax
007F2C75  48 85 C0                        test rax, rax
007F2C78  0F 84 19 FB FF FF               je 0x1407f2797
007F2C7E  4C 8B 4C 1D B0                  mov r9, qword ptr [rbp + rbx - 0x50]
007F2C83  41 8B C6                        mov eax, r14d
007F2C86  C1 E8 1F                        shr eax, 0x1f
007F2C89  41 8B D6                        mov edx, r14d
007F2C8C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
007F2C90  48 8B CE                        mov rcx, rsi
007F2C93  8B 44 1D D0                     mov eax, dword ptr [rbp + rbx - 0x30]
007F2C97  45 8B 49 0C                     mov r9d, dword ptr [r9 + 0xc]
007F2C9B  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007F2C9F  48 8B 44 1D C0                  mov rax, qword ptr [rbp + rbx - 0x40]
007F2CA4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007F2CA9  E8 8E 88 05 00                  call 0x14084b53c
007F2CAE  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
007F2CB5  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007F2CBA  8B D8                           mov ebx, eax
007F2CBC  48 8B CE                        mov rcx, rsi
007F2CBF  74 07                           je 0x1407f2cc8
007F2CC1  E8 5A 9F 06 00                  call 0x14085cc20
007F2CC6  EB 05                           jmp 0x1407f2ccd
007F2CC8  E8 73 32 06 00                  call 0x140855f40
007F2CCD  85 DB                           test ebx, ebx
007F2CCF  0F 88 40 FA FF FF               js 0x1407f2715
007F2CD5  41 FF C7                        inc r15d
007F2CD8  E9 84 FE FF FF                  jmp 0x1407f2b61
007F2CDD  33 DB                           xor ebx, ebx
007F2CDF  41 FF C5                        inc r13d
007F2CE2  E9 A1 FD FF FF                  jmp 0x1407f2a88
007F2CE7  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007F2CEC  E9 2B FA FF FF                  jmp 0x1407f271c
007F2CF1  BB 4C 01 00 C0                  mov ebx, 0xc000014c
007F2CF6  E9 21 FA FF FF                  jmp 0x1407f271c
007F2CFB  E8 40 32 06 00                  call 0x140855f40
007F2D00  49 83 3E 00                     cmp qword ptr [r14], 0
007F2D04  74 26                           je 0x1407f2d2c
007F2D06  41 8B C7                        mov eax, r15d
007F2D09  48 8D 55 B8                     lea rdx, [rbp - 0x48]
007F2D0D  48 6B C8 58                     imul rcx, rax, 0x58
007F2D11  48 03 D1                        add rdx, rcx
007F2D14  48 8B CF                        mov rcx, rdi
007F2D17  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F2D1E  74 07                           je 0x1407f2d27
007F2D20  E8 FB 9E 06 00                  call 0x14085cc20
007F2D25  EB 05                           jmp 0x1407f2d2c
007F2D27  E8 14 32 06 00                  call 0x140855f40
007F2D2C  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
007F2D30  48 85 C9                        test rcx, rcx
007F2D33  74 36                           je 0x1407f2d6b
007F2D35  41 80 7E 24 00                  cmp byte ptr [r14 + 0x24], 0
007F2D3A  74 09                           je 0x1407f2d45
007F2D3C  33 D2                           xor edx, edx
007F2D3E  E8 2D FB 38 00                  call 0x140b82870
007F2D43  EB 26                           jmp 0x1407f2d6b
007F2D45  41 8B C7                        mov eax, r15d
007F2D48  48 8D 55 C8                     lea rdx, [rbp - 0x38]
007F2D4C  48 6B C8 58                     imul rcx, rax, 0x58
007F2D50  48 03 D1                        add rdx, rcx
007F2D53  48 8B CF                        mov rcx, rdi
007F2D56  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F2D5D  74 07                           je 0x1407f2d66
007F2D5F  E8 BC 9E 06 00                  call 0x14085cc20
007F2D64  EB 05                           jmp 0x1407f2d6b
007F2D66  E8 D5 31 06 00                  call 0x140855f40
007F2D6B  41 FF C7                        inc r15d
007F2D6E  49 83 C6 58                     add r14, 0x58
007F2D72  41 83 FF 02                     cmp r15d, 2
007F2D76  0F 82 A7 F9 FF FF               jb 0x1407f2723
007F2D7C  45 33 F6                        xor r14d, r14d
007F2D7F  4C 39 74 24 70                  cmp qword ptr [rsp + 0x70], r14
007F2D84  74 1D                           je 0x1407f2da3
007F2D86  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007F2D8D  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
007F2D92  48 8B CF                        mov rcx, rdi
007F2D95  74 07                           je 0x1407f2d9e
007F2D97  E8 84 9E 06 00                  call 0x14085cc20
007F2D9C  EB 05                           jmp 0x1407f2da3
007F2D9E  E8 9D 31 06 00                  call 0x140855f40
007F2DA3  4C 39 74 24 68                  cmp qword ptr [rsp + 0x68], r14
007F2DA8  74 1D                           je 0x1407f2dc7
007F2DAA  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
007F2DB1  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
007F2DB6  48 8B CE                        mov rcx, rsi
007F2DB9  74 07                           je 0x1407f2dc2
007F2DBB  E8 60 9E 06 00                  call 0x14085cc20
007F2DC0  EB 05                           jmp 0x1407f2dc7
007F2DC2  E8 79 31 06 00                  call 0x140855f40
007F2DC7  4D 85 ED                        test r13, r13
007F2DCA  74 0A                           je 0x1407f2dd6
007F2DCC  33 D2                           xor edx, edx
007F2DCE  49 8B CD                        mov rcx, r13
007F2DD1  E8 9A FA 38 00                  call 0x140b82870
007F2DD6  8B C3                           mov eax, ebx
007F2DD8  48 81 C4 58 01 00 00            add rsp, 0x158
007F2DDF  41 5F                           pop r15
007F2DE1  41 5E                           pop r14
007F2DE3  41 5D                           pop r13
007F2DE5  41 5C                           pop r12
007F2DE7  5F                              pop rdi
007F2DE8  5E                              pop rsi
007F2DE9  5B                              pop rbx
007F2DEA  5D                              pop rbp
007F2DEB  C3                              ret
007F2DEC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpPreserveSystemHiveData(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned int v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned int v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_m6C;
    unsigned __int64 v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p14;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p24;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (344);
    a1 = 0;
    v_stack_m58 = v_rip + 3241544;
    v_stack_p8 = 0;
    v_stack_m118 = v_rip + 3241624;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    v_stack_p24 = 0;
    v_stack_p20 = (unsigned int)(a2);
    v_stack_mC0 = v_rip + 3241643;
    v_stack_m138 = (unsigned int)(a2);
    v_stack_mB8 = v_rip + 3241527;
    v_stack_m134 = 0;
    v_stack_m148 = (unsigned int)(a2);
    v_stack_m144 = 0;
    v_stack_m158 = (unsigned int)(a2);
    v_stack_m154 = 0;
    v_stack_m150 = (unsigned int)(a2);
    v_stack_m14C = 0;
    v_stack_m140 = (unsigned int)(a2);
    v_stack_m13C = 0;
    v_stack_p10 = (unsigned int)(a2);
    v_stack_p14 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = (unsigned int)(a2);
    v_stack_m100 = 0;
    v_stack_mF8 = (unsigned int)(a2);
    v_stack_mF4 = 0;
    v_stack_mF0 = (unsigned int)(a2);
    v_stack_mE8 = 0;
    v_stack_mE0 = (unsigned int)(a2);
    v_stack_mDC = 0;
    v_stack_mD8 = 0;
    v_stack_mD0 = (unsigned int)(a2);
    v_stack_mCC = 0;
    v_stack_mC4 = 0;
    v_stack_mB0 = (unsigned int)(a2);
    v_stack_mA8 = 0;
    v_stack_mA0 = (unsigned int)(a2);
    v_stack_m9C = 0;
    v_stack_m98 = (unsigned int)(a2);
    v_stack_m90 = 0;
    v_stack_m88 = (unsigned int)(a2);
    v_stack_m84 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = (unsigned int)(a2);
    v_stack_m74 = 0;
    v_stack_m6C = 0;
    v_stack_p18 = 0;
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    v_stack_m68 = v_xmm0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)))) == ((unsigned int)(a2))) goto loc_007F2CF1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 36)))) == ((unsigned int)(a2))) goto loc_007F2CF1;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F265A;
    result = HvpGetCellFlat(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)))), v_stack_m140, a4);
    goto loc_007F265F;
loc_007F265A:
    result = HvpGetCellPaged(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)))), v_stack_m140, a4);
loc_007F265F:
    v_stack_m128 = result;
    if (((*(unsigned __int8 *)(a2 + 140)) & (1)) == 0) goto loc_007F2682;
    result = HvpGetCellFlat(a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 36)))), v_stack_m138, a4);
    goto loc_007F2687;
loc_007F2682:
    result = HvpGetCellPaged(a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 36)))), v_stack_m138, a4);
loc_007F2687:
    v_stack_m130 = result;
    if (result == 0) goto loc_007F2CE7;
    if (result == 0) goto loc_007F2CE7;
loc_007F26A4:
    if (0 >= 1) goto loc_007F2756;
    result = CmpWalkPath(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)))), *(unsigned __int64 *)(v_stack_m98 + 0 * 8 + 64), a4);
    result = CmpWalkPath(a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 36)))), *(unsigned __int64 *)(v_stack_m98 + 0 * 8 + 64), a4);
    a1 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(a1))) goto loc_007F2710;
    if (((unsigned int)(result)) == ((unsigned int)(a1))) goto loc_007F2710;
    v_stack_m170 = 1;
    v_stack_m178 = 2;
    result = CmpCopySyncTree(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2, (unsigned int)((unsigned int)(result)));
    v_r13 = 0;
    if (sign_flag) goto loc_007F271C;
    v_r14 = (unsigned int)((0) + 1);
    goto loc_007F26A4;
loc_007F2710:
loc_007F2715:
loc_007F271C:
    v_r15 = 0;
loc_007F2723:
    if ((*(unsigned __int64 *)(v_stack_mE8 - 24)) == 0) goto loc_007F2D00;
    a1 = (a1) * (0);
    a2 = (v_stack_mF8) + (a1);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F2CFB;
    result = HvpReleaseCellFlat(a1, a2, a2, (unsigned int)((unsigned int)(result)));
    goto loc_007F2D00;
loc_007F2756:
    result = CmpWalkPath(a1, a2, v_rip + 3202067, (unsigned int)((unsigned int)(result)));
    v_r15 = (unsigned int)((v_r15) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) != ((unsigned int)(v_r15))) goto loc_007F2773;
    goto loc_007F2715;
loc_007F2773:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F278D;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)(result)), v_stack_m150, (unsigned int)((unsigned int)(result)));
    goto loc_007F2792;
loc_007F278D:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)(result)), v_stack_m150, (unsigned int)((unsigned int)(result)));
loc_007F2792:
    if (result != 0) goto loc_007F27A1;
loc_007F2797:
    goto loc_007F2715;
loc_007F27A1:
    result = CmpFindValueByName(a1, result, v_rip + 8287320, (unsigned int)((unsigned int)(result)));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F27CD;
    result = HvpReleaseCellFlat(a1, v_stack_m150, v_rip + 8287320, (unsigned int)((unsigned int)(result)));
    goto loc_007F27D2;
loc_007F27CD:
    result = HvpReleaseCellPaged(a1, v_stack_m150, v_rip + 8287320, (unsigned int)((unsigned int)(result)));
loc_007F27D2:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(v_r15))) goto loc_007F295A;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F27F7;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_p10, (unsigned int)((unsigned int)(result)));
    goto loc_007F27FC;
loc_007F27F7:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_p10, (unsigned int)((unsigned int)(result)));
loc_007F27FC:
    if (result == 0) goto loc_007F295A;
    if ((*(unsigned int *)(result + 12)) != 6) goto loc_007F293E;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F282D;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(result + 8)), v_stack_m158, (unsigned int)((unsigned int)(result)));
    goto loc_007F2832;
loc_007F282D:
    result = HvpGetCellPaged(a1, (unsigned int)(*(unsigned int *)(result + 8)), v_stack_m158, (unsigned int)((unsigned int)(result)));
loc_007F2832:
    if (result != 0) goto loc_007F2861;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F2857;
    result = HvpReleaseCellFlat(a1, v_stack_p10, v_stack_m158, (unsigned int)((unsigned int)(result)));
    goto loc_007F2797;
loc_007F2857:
    result = HvpReleaseCellPaged(a1, v_stack_p10, v_stack_m158, (unsigned int)((unsigned int)(result)));
    goto loc_007F2797;
loc_007F2861:
    v_r14 = ((unsigned int)(*(unsigned int *)(result + 4))) + (-2);
    v_r14 = (v_r14) + (result);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F287C;
    result = HvpReleaseCellFlat(a1, v_stack_p10, v_stack_m158, (unsigned int)((unsigned int)(result)));
    goto loc_007F2881;
loc_007F287C:
    result = HvpReleaseCellPaged(a1, v_stack_p10, v_stack_m158, (unsigned int)((unsigned int)(result)));
loc_007F2881:
    goto loc_007F2891;
loc_007F2886:
    if (v_r14 < result) goto loc_007F2898;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) + 1);
    v_r14 = (v_r14) - (2);
loc_007F2891:
    if ((*(unsigned __int16 *)(v_r14)) != 92) goto loc_007F2886;
loc_007F2898:
    a2 = (v_rbx + 1) + (v_rbx + 1);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x68504D43ULL), (unsigned int)((unsigned int)(result)));
    v_stack_p18 = result;
    if (result != 0) goto loc_007F28E4;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F28D5;
    result = HvpReleaseCellFlat(a1, v_stack_m158, (unsigned int)(0x68504D43ULL), (unsigned int)((unsigned int)(result)));
    goto loc_007F28DA;
loc_007F28D5:
    result = HvpReleaseCellPaged(a1, v_stack_m158, (unsigned int)(0x68504D43ULL), (unsigned int)((unsigned int)(result)));
loc_007F28DA:
    goto loc_007F271C;
loc_007F28E4:
    result = memcpy(result, v_r14 + 2, (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))) + (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))) * 1, (unsigned int)((unsigned int)(result)));
    result = 0;
    *(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))) + (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))) * 1 + result * 1) = 0;
    result = CmpWalkPath(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)))), 0, (unsigned int)((unsigned int)(result)));
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F2929;
    result = HvpReleaseCellFlat(a1, v_stack_m158, 0, (unsigned int)((unsigned int)(result)));
    goto loc_007F292E;
loc_007F2929:
    result = HvpReleaseCellPaged(a1, v_stack_m158, 0, (unsigned int)((unsigned int)(result)));
loc_007F292E:
    v_r15 = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r15))) goto loc_007F295A;
    v_rbx = 0;
    goto loc_007F271C;
loc_007F293E:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F2955;
    result = HvpReleaseCellFlat(a1, v_stack_p10, 0, (unsigned int)((unsigned int)(result)));
    goto loc_007F295A;
loc_007F2955:
    result = HvpReleaseCellPaged(a1, v_stack_p10, 0, (unsigned int)((unsigned int)(result)));
loc_007F295A:
    v_rbx = 0;
loc_007F2962:
    if (0 >= 2) goto loc_007F2A7A;
    v_rbx = (v_rbx) * (0);
    result = CmpWalkPath(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 128), (unsigned int)((unsigned int)(result)));
    *(unsigned int *)(v_stack_m98 + v_rbx * 1 - 112) = (unsigned int)(result);
    if (((unsigned int)(result)) == ((unsigned int)(v_r15))) goto loc_007F2A72;
    result = 0;
    if ((*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 120)) == 0) goto loc_007F2A6F;
    a3 = (v_stack_mF8) + (v_rbx);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F29B9;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)(result)), a3, (unsigned int)((unsigned int)(result)));
    goto loc_007F29BE;
loc_007F29B9:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)(result)), a3, (unsigned int)((unsigned int)(result)));
loc_007F29BE:
    *(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 104) = result;
    if (result == 0) goto loc_007F2797;
    result = RtlInitUnicodeString(v_stack_m68, *(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 120), a3, (unsigned int)((unsigned int)(result)));
    result = CmpFindValueByName(a1, result, v_stack_m68, (unsigned int)((unsigned int)(result)));
    v_r15 = (unsigned int)((result) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_stack_m98 + v_rbx * 1 - 88) = (unsigned int)(result);
    if (((unsigned int)(result)) == ((unsigned int)(v_r15))) goto loc_007F2A72;
    a3 = (v_stack_mE0) + (v_rbx);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F2A18;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)(result)), a3, (unsigned int)((unsigned int)(result)));
    goto loc_007F2A1D;
loc_007F2A18:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)(result)), a3, (unsigned int)((unsigned int)(result)));
loc_007F2A1D:
    *(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) = result;
    if (result == 0) goto loc_007F2797;
    result = (v_stack_mD0) + (v_rbx);
    a1 = (v_stack_mC4) + (v_rbx);
    v_stack_m168 = result;
    v_stack_m170 = a1;
    a2 = (v_stack_mD8) + (v_rbx);
    v_stack_m178 = a2;
    a4 = (v_stack_mC8) + (v_rbx);
    result = CmpGetValueData(a1, (unsigned int)(*(unsigned int *)(v_stack_m98 + v_rbx * 1 - 88)), result, a4);
    if ((unsigned __int8)(result) == 0) goto loc_007F2710;
    goto loc_007F2A72;
loc_007F2A6F:
loc_007F2A72:
    v_r12 = (unsigned int)((0) + 1);
    goto loc_007F2962;
loc_007F2A7A:
    v_rbx = 0;
    if (1 == 0) goto loc_007F2715;
loc_007F2A88:
    if (0 >= (*(unsigned int *)(v_stack_m130 + 20))) goto loc_007F2715;
    result = CmpFindSubKeyByNumber(a2, v_stack_m130, 0, v_stack_p8);
    if (((*(unsigned __int8 *)(a2 + 140)) & (1)) == 0) goto loc_007F2ACC;
    result = HvpGetCellFlat(a2, (unsigned int)(v_stack_p8), v_stack_p20, v_stack_p8);
    goto loc_007F2AD1;
loc_007F2ACC:
    result = HvpGetCellPaged(a2, (unsigned int)(v_stack_p8), v_stack_p20, v_stack_p8);
loc_007F2AD1:
    if (result == 0) goto loc_007F2797;
    if ((*(unsigned __int16 *)(result + 72)) == 13) goto loc_007F2B08;
    if (((*(unsigned __int8 *)(a2 + 140)) & (1)) == 0) goto loc_007F2AFE;
    result = HvpReleaseCellFlat(a2, v_stack_p20, v_stack_p20, v_stack_p8);
    goto loc_007F2CDF;
loc_007F2AFE:
    result = HvpReleaseCellPaged(a2, v_stack_p20, v_stack_p20, v_stack_p8);
    goto loc_007F2CDF;
loc_007F2B08:
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_007F2B26;
    result = strnicmp(result + 76, v_rip + 3240113, 10, v_stack_p8);
    goto loc_007F2B32;
loc_007F2B26:
    result = wcsnicmp(result + 76, v_rip + 3240035, 10, v_stack_p8);
loc_007F2B32:
    v_rbx = ((unsigned int)(result) == 0) ? 1 : 0;
    if (((*(unsigned __int8 *)(a2 + 140)) & (1)) == 0) goto loc_007F2B51;
    result = HvpReleaseCellFlat(a2, v_stack_p20, 10, v_stack_p8);
    goto loc_007F2B56;
loc_007F2B51:
    result = HvpReleaseCellPaged(a2, v_stack_p20, 10, v_stack_p8);
loc_007F2B56:
    v_r15 = 0;
    if ((unsigned __int8)(v_rbx) == 0) goto loc_007F2CDD;
loc_007F2B61:
    if (0 >= 2) goto loc_007F2CDD;
    v_rbx = (v_rbx) * (0);
    result = (unsigned int)((0) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98 + v_rbx * 1 - 112)))) == ((unsigned int)(result))) goto loc_007F2CD5;
    if (*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 120) == 0) goto loc_007F2B97;
    if ((*(unsigned int *)(v_stack_m98 + v_rbx * 1 - 88)) == ((unsigned int)(result))) goto loc_007F2CD5;
loc_007F2B97:
    result = CmpWalkPath(a2, (unsigned int)(v_stack_p8), *(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 128), v_stack_p8);
    if (((unsigned int)(result)) == -1) goto loc_007F2CD5;
    if (*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 120) != 0) goto loc_007F2BE0;
    v_stack_m170 = 1;
    v_stack_m178 = 2;
    result = CmpCopySyncTree(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98 + v_rbx * 1 - 112)))), a2, (unsigned int)((unsigned int)(result)));
    goto loc_007F2CD5;
loc_007F2BE0:
    if (((*(unsigned __int8 *)(a2 + 140)) & (1)) == 0) goto loc_007F2BFA;
    result = HvpGetCellFlat(a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98 + v_rbx * 1 - 112)))), v_stack_p20, (unsigned int)((unsigned int)(result)));
    goto loc_007F2BFF;
loc_007F2BFA:
    result = HvpGetCellPaged(a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98 + v_rbx * 1 - 112)))), v_stack_p20, (unsigned int)((unsigned int)(result)));
loc_007F2BFF:
    if (result == 0) goto loc_007F2797;
    result = RtlInitUnicodeString(v_stack_m68, *(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 120), v_stack_p20, (unsigned int)((unsigned int)(result)));
    result = CmpFindValueByName(a2, result, v_stack_m68, (unsigned int)((unsigned int)(result)));
    if (((*(unsigned __int8 *)(a2 + 140)) & (1)) == 0) goto loc_007F2C43;
    result = HvpReleaseCellFlat(a2, v_stack_p20, v_stack_m68, (unsigned int)((unsigned int)(result)));
    goto loc_007F2C48;
loc_007F2C43:
    result = HvpReleaseCellPaged(a2, v_stack_p20, v_stack_m68, (unsigned int)((unsigned int)(result)));
loc_007F2C48:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == -1) goto loc_007F2CD5;
    if (((*(unsigned __int8 *)(a2 + 140)) & (1)) == 0) goto loc_007F2C6D;
    result = HvpGetCellFlat(a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m148, (unsigned int)((unsigned int)(result)));
    goto loc_007F2C72;
loc_007F2C6D:
    result = HvpGetCellPaged(a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m148, (unsigned int)((unsigned int)(result)));
loc_007F2C72:
    if (result == 0) goto loc_007F2797;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) >> (31));
    v_stack_m168 = (unsigned int)(result);
    v_stack_m170 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98 + v_rbx * 1 - 48)));
    v_stack_m178 = *(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 64);
    result = CmpSetValueKeyExisting(a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
    if (((*(unsigned __int8 *)(a2 + 140)) & (1)) == 0) goto loc_007F2CC8;
    result = HvpReleaseCellFlat(a2, v_stack_m148, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
    goto loc_007F2CCD;
loc_007F2CC8:
    result = HvpReleaseCellPaged(a2, v_stack_m148, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
loc_007F2CCD:
    if (sign_flag) goto loc_007F2715;
loc_007F2CD5:
    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_007F2B61;
loc_007F2CDD:
    v_rbx = 0;
loc_007F2CDF:
    v_r13 = (unsigned int)((0) + 1);
    goto loc_007F2A88;
loc_007F2CE7:
    goto loc_007F271C;
loc_007F2CF1:
    goto loc_007F271C;
loc_007F2CFB:
    result = HvpReleaseCellPaged(a2, v_stack_m148, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
loc_007F2D00:
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(result)))) == 0) goto loc_007F2D2C;
    a1 = (a2) * ((unsigned int)((unsigned int)(v_r15)));
    a2 = (v_stack_mE0) + (a1);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F2D27;
    result = HvpReleaseCellFlat(a1, a2, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
    goto loc_007F2D2C;
loc_007F2D27:
    result = HvpReleaseCellPaged(a1, a2, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
loc_007F2D2C:
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 16) == 0) goto loc_007F2D6B;
    if ((*(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + 36)) == 0) goto loc_007F2D45;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 16), a2, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
    goto loc_007F2D6B;
loc_007F2D45:
    a1 = (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 16)) * ((unsigned int)((unsigned int)(v_r15)));
    a2 = (v_stack_mD0) + (a1);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F2D66;
    result = HvpReleaseCellFlat(a1, a2, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
    goto loc_007F2D6B;
loc_007F2D66:
    result = HvpReleaseCellPaged(a1, a2, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
loc_007F2D6B:
    v_r15 = (unsigned int)((v_r15) + 1);
    v_r14 = ((unsigned int)((unsigned int)(result))) + (88);
    if (((unsigned int)(v_r15)) < 2) goto loc_007F2723;
    v_r14 = 0;
    if (v_stack_m128 == 0) goto loc_007F2DA3;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_007F2D9E;
    result = HvpReleaseCellFlat(a1, v_stack_m140, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
    goto loc_007F2DA3;
loc_007F2D9E:
    result = HvpReleaseCellPaged(a1, v_stack_m140, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
loc_007F2DA3:
    if (v_stack_m130 == 0) goto loc_007F2DC7;
    if (((*(unsigned __int8 *)(a2 + 140)) & (1)) == 0) goto loc_007F2DC2;
    result = HvpReleaseCellFlat(a2, v_stack_m138, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
    goto loc_007F2DC7;
loc_007F2DC2:
    result = HvpReleaseCellPaged(a2, v_stack_m138, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
loc_007F2DC7:
    if (v_r13 != 0) {
        a2 = 0;
        a1 = v_r13;
        result = ExFreePoolWithTag(a1, a2, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m98 + v_rbx * 1 - 80) + 12)));
    }
    v_rsp = (v_rsp) + (344);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL)));
}
```

## 5. (Beta) C Style

```c
int64_t CmpPreserveSystemHiveData(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint32_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint32_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint8_t v_stack_m6C;
    uint64_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p14;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p24;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (344);
    Arg1 = 0;
    v_stack_m58 = v_rip + 3241544;
    v_stack_p8 = 0;
    v_stack_m118 = v_rip + 3241624;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    v_stack_p24 = 0;
    v_stack_p20 = (uint32_t)(Arg2);
    v_stack_mC0 = v_rip + 3241643;
    v_stack_m138 = (uint32_t)(Arg2);
    v_stack_mB8 = v_rip + 3241527;
    v_stack_m134 = 0;
    v_stack_m148 = (uint32_t)(Arg2);
    v_stack_m144 = 0;
    v_stack_m158 = (uint32_t)(Arg2);
    v_stack_m154 = 0;
    v_stack_m150 = (uint32_t)(Arg2);
    v_stack_m14C = 0;
    v_stack_m140 = (uint32_t)(Arg2);
    v_stack_m13C = 0;
    v_stack_p10 = (uint32_t)(Arg2);
    v_stack_p14 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = (uint32_t)(Arg2);
    v_stack_m100 = 0;
    v_stack_mF8 = (uint32_t)(Arg2);
    v_stack_mF4 = 0;
    v_stack_mF0 = (uint32_t)(Arg2);
    v_stack_mE8 = 0;
    v_stack_mE0 = (uint32_t)(Arg2);
    v_stack_mDC = 0;
    v_stack_mD8 = 0;
    v_stack_mD0 = (uint32_t)(Arg2);
    v_stack_mCC = 0;
    v_stack_mC4 = 0;
    v_stack_mB0 = (uint32_t)(Arg2);
    v_stack_mA8 = 0;
    v_stack_mA0 = (uint32_t)(Arg2);
    v_stack_m9C = 0;
    v_stack_m98 = (uint32_t)(Arg2);
    v_stack_m90 = 0;
    v_stack_m88 = (uint32_t)(Arg2);
    v_stack_m84 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = (uint32_t)(Arg2);
    v_stack_m74 = 0;
    v_stack_m6C = 0;
    v_stack_p18 = 0;
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    v_stack_m68 = v_xmm0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)))) == ((uint32_t)(Arg2))) goto loc_007F2CF1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x24)))) == ((uint32_t)(Arg2))) goto loc_007F2CF1;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F265A;
    result = HvpGetCellFlat(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)))), v_stack_m140, a4);
    goto loc_007F265F;
loc_007F265A:
    result = HvpGetCellPaged(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)))), v_stack_m140, a4);
loc_007F265F:
    v_stack_m128 = result;
    if (((*(uint8_t *)(arg2 + 0x8C)) & (1)) == 0) goto loc_007F2682;
    result = HvpGetCellFlat(Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x24)))), v_stack_m138, a4);
    goto loc_007F2687;
loc_007F2682:
    result = HvpGetCellPaged(Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x24)))), v_stack_m138, a4);
loc_007F2687:
    v_stack_m130 = result;
    if (result == 0) goto loc_007F2CE7;
    if (result == 0) goto loc_007F2CE7;
loc_007F26A4:
    if (0 >= 1) goto loc_007F2756;
    result = CmpWalkPath(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)))), *(uint64_t *)(v_stack_m98 + 0x0 * 8 + 0x40), a4);
    result = CmpWalkPath(Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x24)))), *(uint64_t *)(v_stack_m98 + 0x0 * 8 + 0x40), a4);
    Arg1 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(Arg1))) goto loc_007F2710;
    if (((uint32_t)(result)) == ((uint32_t)(Arg1))) goto loc_007F2710;
    v_stack_m170 = 1;
    v_stack_m178 = 2;
    result = CmpCopySyncTree(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg2, (uint32_t)((uint32_t)(result)));
    local_r13 = 0;
    if (sign_flag) goto loc_007F271C;
    local_r14 = (uint32_t)((0) + 1);
    goto loc_007F26A4;
loc_007F2710:
loc_007F2715:
loc_007F271C:
    local_r15 = 0;
loc_007F2723:
    if ((*(uint64_t *)(v_stack_mE8 - 0x18)) == 0) goto loc_007F2D00;
    Arg1 = (Arg1) * (0);
    Arg2 = (v_stack_mF8) + (Arg1);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F2CFB;
    result = HvpReleaseCellFlat(Arg1, Arg2, Arg2, (uint32_t)((uint32_t)(result)));
    goto loc_007F2D00;
loc_007F2756:
    result = CmpWalkPath(Arg1, Arg2, v_rip + 3202067, (uint32_t)((uint32_t)(result)));
    local_r15 = (uint32_t)((local_r15) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) != ((uint32_t)(local_r15))) goto loc_007F2773;
    goto loc_007F2715;
loc_007F2773:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F278D;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)(result)), v_stack_m150, (uint32_t)((uint32_t)(result)));
    goto loc_007F2792;
loc_007F278D:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)(result)), v_stack_m150, (uint32_t)((uint32_t)(result)));
loc_007F2792:
    if (result != 0) goto loc_007F27A1;
loc_007F2797:
    goto loc_007F2715;
loc_007F27A1:
    result = CmpFindValueByName(Arg1, result, v_rip + 8287320, (uint32_t)((uint32_t)(result)));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F27CD;
    result = HvpReleaseCellFlat(Arg1, v_stack_m150, v_rip + 8287320, (uint32_t)((uint32_t)(result)));
    goto loc_007F27D2;
loc_007F27CD:
    result = HvpReleaseCellPaged(Arg1, v_stack_m150, v_rip + 8287320, (uint32_t)((uint32_t)(result)));
loc_007F27D2:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(local_r15))) goto loc_007F295A;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F27F7;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_p10, (uint32_t)((uint32_t)(result)));
    goto loc_007F27FC;
loc_007F27F7:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_p10, (uint32_t)((uint32_t)(result)));
loc_007F27FC:
    if (result == 0) goto loc_007F295A;
    if ((*(uint32_t *)(result + 0xC)) != 6) goto loc_007F293E;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F282D;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(result + 0x8)), v_stack_m158, (uint32_t)((uint32_t)(result)));
    goto loc_007F2832;
loc_007F282D:
    result = HvpGetCellPaged(Arg1, (uint32_t)(*(uint32_t *)(result + 0x8)), v_stack_m158, (uint32_t)((uint32_t)(result)));
loc_007F2832:
    if (result != 0) goto loc_007F2861;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F2857;
    result = HvpReleaseCellFlat(Arg1, v_stack_p10, v_stack_m158, (uint32_t)((uint32_t)(result)));
    goto loc_007F2797;
loc_007F2857:
    result = HvpReleaseCellPaged(Arg1, v_stack_p10, v_stack_m158, (uint32_t)((uint32_t)(result)));
    goto loc_007F2797;
loc_007F2861:
    local_r14 = ((uint32_t)(*(uint32_t *)(result + 0x4))) + (-2);
    local_r14 = (local_r14) + (result);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F287C;
    result = HvpReleaseCellFlat(Arg1, v_stack_p10, v_stack_m158, (uint32_t)((uint32_t)(result)));
    goto loc_007F2881;
loc_007F287C:
    result = HvpReleaseCellPaged(Arg1, v_stack_p10, v_stack_m158, (uint32_t)((uint32_t)(result)));
loc_007F2881:
    goto loc_007F2891;
loc_007F2886:
    if (local_r14 < result) goto loc_007F2898;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) + 1);
    local_r14 = (local_r14) - (2);
loc_007F2891:
    if ((*(uint16_t *)(local_r14)) != 92) goto loc_007F2886;
loc_007F2898:
    Arg2 = (local_rbx + 1) + (local_rbx + 1);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x68504D43ULL), (uint32_t)((uint32_t)(result)));
    v_stack_p18 = result;
    if (result != 0) goto loc_007F28E4;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F28D5;
    result = HvpReleaseCellFlat(Arg1, v_stack_m158, (uint32_t)(0x68504D43ULL), (uint32_t)((uint32_t)(result)));
    goto loc_007F28DA;
loc_007F28D5:
    result = HvpReleaseCellPaged(Arg1, v_stack_m158, (uint32_t)(0x68504D43ULL), (uint32_t)((uint32_t)(result)));
loc_007F28DA:
    goto loc_007F271C;
loc_007F28E4:
    result = memcpy(result, local_r14 + 2, (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))) + (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))) * 1, (uint32_t)((uint32_t)(result)));
    result = 0;
    *(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))) + (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))) * 1 + result * 1) = 0;
    result = CmpWalkPath(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)))), 0, (uint32_t)((uint32_t)(result)));
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F2929;
    result = HvpReleaseCellFlat(Arg1, v_stack_m158, 0, (uint32_t)((uint32_t)(result)));
    goto loc_007F292E;
loc_007F2929:
    result = HvpReleaseCellPaged(Arg1, v_stack_m158, 0, (uint32_t)((uint32_t)(result)));
loc_007F292E:
    local_r15 = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r15))) goto loc_007F295A;
    local_rbx = 0;
    goto loc_007F271C;
loc_007F293E:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F2955;
    result = HvpReleaseCellFlat(Arg1, v_stack_p10, 0, (uint32_t)((uint32_t)(result)));
    goto loc_007F295A;
loc_007F2955:
    result = HvpReleaseCellPaged(Arg1, v_stack_p10, 0, (uint32_t)((uint32_t)(result)));
loc_007F295A:
    local_rbx = 0;
loc_007F2962:
    if (0 >= 2) goto loc_007F2A7A;
    local_rbx = (local_rbx) * (0);
    result = CmpWalkPath(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x80), (uint32_t)((uint32_t)(result)));
    *(uint32_t *)(v_stack_m98 + local_rbx * 1 - 0x70) = (uint32_t)(result);
    if (((uint32_t)(result)) == ((uint32_t)(local_r15))) goto loc_007F2A72;
    result = 0;
    if ((*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x78)) == 0) goto loc_007F2A6F;
    a3 = (v_stack_mF8) + (local_rbx);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F29B9;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)(result)), a3, (uint32_t)((uint32_t)(result)));
    goto loc_007F29BE;
loc_007F29B9:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)(result)), a3, (uint32_t)((uint32_t)(result)));
loc_007F29BE:
    *(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x68) = result;
    if (result == 0) goto loc_007F2797;
    result = RtlInitUnicodeString(v_stack_m68, *(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x78), a3, (uint32_t)((uint32_t)(result)));
    result = CmpFindValueByName(Arg1, result, v_stack_m68, (uint32_t)((uint32_t)(result)));
    local_r15 = (uint32_t)((result) | (0xFFFFFFFFULL));
    *(uint32_t *)(v_stack_m98 + local_rbx * 1 - 0x58) = (uint32_t)(result);
    if (((uint32_t)(result)) == ((uint32_t)(local_r15))) goto loc_007F2A72;
    a3 = (v_stack_mE0) + (local_rbx);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F2A18;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)(result)), a3, (uint32_t)((uint32_t)(result)));
    goto loc_007F2A1D;
loc_007F2A18:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)(result)), a3, (uint32_t)((uint32_t)(result)));
loc_007F2A1D:
    *(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) = result;
    if (result == 0) goto loc_007F2797;
    result = (v_stack_mD0) + (local_rbx);
    Arg1 = (v_stack_mC4) + (local_rbx);
    v_stack_m168 = result;
    v_stack_m170 = Arg1;
    Arg2 = (v_stack_mD8) + (local_rbx);
    v_stack_m178 = Arg2;
    a4 = (v_stack_mC8) + (local_rbx);
    result = CmpGetValueData(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m98 + local_rbx * 1 - 0x58)), result, a4);
    if ((uint8_t)(result) == 0) goto loc_007F2710;
    goto loc_007F2A72;
loc_007F2A6F:
loc_007F2A72:
    local_r12 = (uint32_t)((0) + 1);
    goto loc_007F2962;
loc_007F2A7A:
    local_rbx = 0;
    if (1 == 0) goto loc_007F2715;
loc_007F2A88:
    if (0 >= (*(uint32_t *)(v_stack_m130 + 0x14))) goto loc_007F2715;
    result = CmpFindSubKeyByNumber(Arg2, v_stack_m130, 0, v_stack_p8);
    if (((*(uint8_t *)(arg2 + 0x8C)) & (1)) == 0) goto loc_007F2ACC;
    result = HvpGetCellFlat(Arg2, (uint32_t)(v_stack_p8), v_stack_p20, v_stack_p8);
    goto loc_007F2AD1;
loc_007F2ACC:
    result = HvpGetCellPaged(Arg2, (uint32_t)(v_stack_p8), v_stack_p20, v_stack_p8);
loc_007F2AD1:
    if (result == 0) goto loc_007F2797;
    if ((*(uint16_t *)(result + 0x48)) == 13) goto loc_007F2B08;
    if (((*(uint8_t *)(arg2 + 0x8C)) & (1)) == 0) goto loc_007F2AFE;
    result = HvpReleaseCellFlat(Arg2, v_stack_p20, v_stack_p20, v_stack_p8);
    goto loc_007F2CDF;
loc_007F2AFE:
    result = HvpReleaseCellPaged(Arg2, v_stack_p20, v_stack_p20, v_stack_p8);
    goto loc_007F2CDF;
loc_007F2B08:
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_007F2B26;
    result = strnicmp(result + 76, v_rip + 3240113, 10, v_stack_p8);
    goto loc_007F2B32;
loc_007F2B26:
    result = wcsnicmp(result + 76, v_rip + 3240035, 10, v_stack_p8);
loc_007F2B32:
    local_rbx = ((uint32_t)(result) == 0) ? 1 : 0;
    if (((*(uint8_t *)(arg2 + 0x8C)) & (1)) == 0) goto loc_007F2B51;
    result = HvpReleaseCellFlat(Arg2, v_stack_p20, 10, v_stack_p8);
    goto loc_007F2B56;
loc_007F2B51:
    result = HvpReleaseCellPaged(Arg2, v_stack_p20, 10, v_stack_p8);
loc_007F2B56:
    local_r15 = 0;
    if ((uint8_t)(local_rbx) == 0) goto loc_007F2CDD;
loc_007F2B61:
    if (0 >= 2) goto loc_007F2CDD;
    local_rbx = (local_rbx) * (0);
    result = (uint32_t)((0) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + local_rbx * 1 - 0x70)))) == ((uint32_t)(result))) goto loc_007F2CD5;
    if (*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x78) == 0) goto loc_007F2B97;
    if ((*(uint32_t *)(v_stack_m98 + local_rbx * 1 - 0x58)) == ((uint32_t)(result))) goto loc_007F2CD5;
loc_007F2B97:
    result = CmpWalkPath(Arg2, (uint32_t)(v_stack_p8), *(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x80), v_stack_p8);
    if (((uint32_t)(result)) == -1) goto loc_007F2CD5;
    if (*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x78) != 0) goto loc_007F2BE0;
    v_stack_m170 = 1;
    v_stack_m178 = 2;
    result = CmpCopySyncTree(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + local_rbx * 1 - 0x70)))), Arg2, (uint32_t)((uint32_t)(result)));
    goto loc_007F2CD5;
loc_007F2BE0:
    if (((*(uint8_t *)(arg2 + 0x8C)) & (1)) == 0) goto loc_007F2BFA;
    result = HvpGetCellFlat(Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + local_rbx * 1 - 0x70)))), v_stack_p20, (uint32_t)((uint32_t)(result)));
    goto loc_007F2BFF;
loc_007F2BFA:
    result = HvpGetCellPaged(Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + local_rbx * 1 - 0x70)))), v_stack_p20, (uint32_t)((uint32_t)(result)));
loc_007F2BFF:
    if (result == 0) goto loc_007F2797;
    result = RtlInitUnicodeString(v_stack_m68, *(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x78), v_stack_p20, (uint32_t)((uint32_t)(result)));
    result = CmpFindValueByName(Arg2, result, v_stack_m68, (uint32_t)((uint32_t)(result)));
    if (((*(uint8_t *)(arg2 + 0x8C)) & (1)) == 0) goto loc_007F2C43;
    result = HvpReleaseCellFlat(Arg2, v_stack_p20, v_stack_m68, (uint32_t)((uint32_t)(result)));
    goto loc_007F2C48;
loc_007F2C43:
    result = HvpReleaseCellPaged(Arg2, v_stack_p20, v_stack_m68, (uint32_t)((uint32_t)(result)));
loc_007F2C48:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == -1) goto loc_007F2CD5;
    if (((*(uint8_t *)(arg2 + 0x8C)) & (1)) == 0) goto loc_007F2C6D;
    result = HvpGetCellFlat(Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m148, (uint32_t)((uint32_t)(result)));
    goto loc_007F2C72;
loc_007F2C6D:
    result = HvpGetCellPaged(Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m148, (uint32_t)((uint32_t)(result)));
loc_007F2C72:
    if (result == 0) goto loc_007F2797;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) >> (31));
    v_stack_m168 = (uint32_t)(result);
    v_stack_m170 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + local_rbx * 1 - 0x30)));
    v_stack_m178 = *(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x40);
    result = CmpSetValueKeyExisting(Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
    if (((*(uint8_t *)(arg2 + 0x8C)) & (1)) == 0) goto loc_007F2CC8;
    result = HvpReleaseCellFlat(Arg2, v_stack_m148, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
    goto loc_007F2CCD;
loc_007F2CC8:
    result = HvpReleaseCellPaged(Arg2, v_stack_m148, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
loc_007F2CCD:
    if (sign_flag) goto loc_007F2715;
loc_007F2CD5:
    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_007F2B61;
loc_007F2CDD:
    local_rbx = 0;
loc_007F2CDF:
    local_r13 = (uint32_t)((0) + 1);
    goto loc_007F2A88;
loc_007F2CE7:
    goto loc_007F271C;
loc_007F2CF1:
    goto loc_007F271C;
loc_007F2CFB:
    result = HvpReleaseCellPaged(Arg2, v_stack_m148, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
loc_007F2D00:
    if ((*(uint64_t *)((uint32_t)((uint32_t)(result)))) == 0) goto loc_007F2D2C;
    Arg1 = (Arg2) * ((uint32_t)((uint32_t)(local_r15)));
    Arg2 = (v_stack_mE0) + (Arg1);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F2D27;
    result = HvpReleaseCellFlat(Arg1, Arg2, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
    goto loc_007F2D2C;
loc_007F2D27:
    result = HvpReleaseCellPaged(Arg1, Arg2, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
loc_007F2D2C:
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x10) == 0) goto loc_007F2D6B;
    if ((*(uint8_t *)((uint32_t)((uint32_t)(result)) + 0x24)) == 0) goto loc_007F2D45;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x10), Arg2, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
    goto loc_007F2D6B;
loc_007F2D45:
    Arg1 = (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x10)) * ((uint32_t)((uint32_t)(local_r15)));
    Arg2 = (v_stack_mD0) + (Arg1);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F2D66;
    result = HvpReleaseCellFlat(Arg1, Arg2, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
    goto loc_007F2D6B;
loc_007F2D66:
    result = HvpReleaseCellPaged(Arg1, Arg2, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
loc_007F2D6B:
    local_r15 = (uint32_t)((local_r15) + 1);
    local_r14 = ((uint32_t)((uint32_t)(result))) + (88);
    if (((uint32_t)(local_r15)) < 2) goto loc_007F2723;
    local_r14 = 0;
    if (v_stack_m128 == 0) goto loc_007F2DA3;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_007F2D9E;
    result = HvpReleaseCellFlat(Arg1, v_stack_m140, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
    goto loc_007F2DA3;
loc_007F2D9E:
    result = HvpReleaseCellPaged(Arg1, v_stack_m140, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
loc_007F2DA3:
    if (v_stack_m130 == 0) goto loc_007F2DC7;
    if (((*(uint8_t *)(arg2 + 0x8C)) & (1)) == 0) goto loc_007F2DC2;
    result = HvpReleaseCellFlat(Arg2, v_stack_m138, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
    goto loc_007F2DC7;
loc_007F2DC2:
    result = HvpReleaseCellPaged(Arg2, v_stack_m138, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
loc_007F2DC7:
    if (local_r13 != 0) {
        Arg2 = 0;
        Arg1 = local_r13;
        result = ExFreePoolWithTag(Arg1, Arg2, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m98 + local_rbx * 1 - 0x50) + 0xC)));
    }
    local_rsp = (local_rsp) + (344);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x8C` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F2518&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
