# CmpGetAcpiProfileInformation

- RVA: `0x007E3D7C`–`0x007E4572` (길이 `2,038` bytes)
- VA: `0x00000001407E3D7C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D6A10`
- 디코드: `515`개 명령, `2,038/2,038` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x007E3DF7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E3E2E` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E3E5E` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (function, `0x006AD390`)
- `0x007E3E8B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007E3EE7` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (function, `0x006AD710`)
- `0x007E3F50` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E3F68` → [RtlUnicodeStringToInteger](../99/RtlUnicodeStringToInteger_function_00993480.md) (function, `0x00993480`)
- `0x007E3F79` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E3F9F` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E3FC8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E3FEE` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E4009` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007E4048` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007E406E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007E4084` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E40AC` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E40D7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E4101` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E4179` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007E41A5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E41CF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E4205` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E423A` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (function, `0x006AD390`)
- `0x007E4261` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007E42AE` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (function, `0x006AD710`)
- `0x007E431A` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E4335` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E435F` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E439A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E43C2` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E43F2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E441A` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E444A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007E4480` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007E448A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E44A6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E44B7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E44C6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E44F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E4503` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E452F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E4540` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E4551` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmSetAcpiHwProfile](CmSetAcpiHwProfile_function_007E2584.md) at `0x007E26B8`

### Static image references
- `0x007E3D98` → RVA `0x00E0A740` (`.data`; read)
- `0x007E3DCA` → RVA `0x00B09130` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E3F6D` → RVA `0x00B09340` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E3FB9` → RVA `0x00B09360` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E402E` → RVA `0x00B09310` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E4075` → RVA `0x00B09320` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E40CB` → RVA `0x00B092D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E41C3` → RVA `0x00B092F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E4329` → RVA `0x00B09290` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E437D` → RVA `0x00B092B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E43DB` → RVA `0x00B09250` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **42**
  - `0x007E3DF7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E3E2E` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E3E5E` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (`PAGE` → `.text`)
  - `0x007E3E8B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007E3EE7` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (`PAGE` → `.text`)
  - `0x007E3F50` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E3F79` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E3F9F` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E3FC8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E3FEE` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E4009` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007E4048` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007E406E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007E4084` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E40AC` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E40D7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E4101` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E4179` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007E41A5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E41CF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E4205` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E423A` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (`PAGE` → `.text`)
  - `0x007E4261` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007E42AE` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (`PAGE` → `.text`)
  - `0x007E431A` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E4335` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E435F` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E439A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E43C2` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E43F2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E441A` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E444A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007E4480` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007E448A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E44A6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E44B7` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E44C6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E44F1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E4503` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E452F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E4540` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E4551` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E3D7C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
007E3D81  55                              push rbp
007E3D82  56                              push rsi
007E3D83  57                              push rdi
007E3D84  41 54                           push r12
007E3D86  41 55                           push r13
007E3D88  41 56                           push r14
007E3D8A  41 57                           push r15
007E3D8C  48 8D 6C 24 E9                  lea rbp, [rsp - 0x17]
007E3D91  48 81 EC 00 01 00 00            sub rsp, 0x100
007E3D98  48 8B 05 A1 69 62 00            mov rax, qword ptr [rip + 0x6269a1]
007E3D9F  48 33 C4                        xor rax, rsp
007E3DA2  48 89 45 07                     mov qword ptr [rbp + 7], rax
007E3DA6  48 8B 7D 77                     mov rdi, qword ptr [rbp + 0x77]
007E3DAA  33 F6                           xor esi, esi
007E3DAC  0F 57 C9                        xorps xmm1, xmm1
007E3DAF  48 89 32                        mov qword ptr [rdx], rsi
007E3DB2  4C 8B E2                        mov r12, rdx
007E3DB5  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
007E3DBA  4C 8B E9                        mov r13, rcx
007E3DBD  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
007E3DC2  0F 57 C0                        xorps xmm0, xmm0
007E3DC5  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007E3DCA  48 8D 15 5F 53 32 00            lea rdx, [rip + 0x32535f]
007E3DD1  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
007E3DD5  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E3DDA  89 75 9B                        mov dword ptr [rbp - 0x65], esi
007E3DDD  4D 8B F8                        mov r15, r8
007E3DE0  89 75 B3                        mov dword ptr [rbp - 0x4d], esi
007E3DE3  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
007E3DE8  49 89 30                        mov qword ptr [r8], rsi
007E3DEB  0F 11 4D D7                     movups xmmword ptr [rbp - 0x29], xmm1
007E3DEF  0F 11 4D E7                     movups xmmword ptr [rbp - 0x19], xmm1
007E3DF3  0F 11 4D F7                     movups xmmword ptr [rbp - 9], xmm1
007E3DF7  E8 84 69 C4 FF                  call 0x14042a780
007E3DFC  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E3E01  4C 89 6D 9F                     mov qword ptr [rbp - 0x61], r13
007E3E05  0F 57 C0                        xorps xmm0, xmm0
007E3E08  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
007E3E0C  44 8D 76 30                     lea r14d, [rsi + 0x30]
007E3E10  C7 45 AF 40 02 00 00            mov dword ptr [rbp - 0x51], 0x240
007E3E17  4C 8D 45 97                     lea r8, [rbp - 0x69]
007E3E1B  44 89 75 97                     mov dword ptr [rbp - 0x69], r14d
007E3E1F  BA 19 00 02 00                  mov edx, 0x20019
007E3E24  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
007E3E29  F3 0F 7F 45 B7                  movdqu xmmword ptr [rbp - 0x49], xmm0
007E3E2E  E8 DD 94 EC FF                  call 0x1406ad310
007E3E33  8B D8                           mov ebx, eax
007E3E35  85 C0                           test eax, eax
007E3E37  79 0A                           jns 0x1407e3e43
007E3E39  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
007E3E3E  E9 6A 06 00 00                  jmp 0x1407e44ad
007E3E43  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007E3E48  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E3E4D  45 8B CE                        mov r9d, r14d
007E3E50  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E3E55  4C 8D 45 D7                     lea r8, [rbp - 0x29]
007E3E59  BA 02 00 00 00                  mov edx, 2
007E3E5E  E8 2D 95 EC FF                  call 0x1406ad390
007E3E63  8B D8                           mov ebx, eax
007E3E65  85 C0                           test eax, eax
007E3E67  0F 88 40 06 00 00               js 0x1407e44ad
007E3E6D  8B 45 EB                        mov eax, dword ptr [rbp - 0x15]
007E3E70  BB 00 01 00 00                  mov ebx, 0x100
007E3E75  FF C8                           dec eax
007E3E77  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007E3E7D  C1 E0 05                        shl eax, 5
007E3E80  8B CB                           mov ecx, ebx
007E3E82  83 C0 28                        add eax, 0x28
007E3E85  8B D0                           mov edx, eax
007E3E87  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
007E3E8B  E8 60 E2 39 00                  call 0x140b820f0
007E3E90  49 89 04 24                     mov qword ptr [r12], rax
007E3E94  48 8B C8                        mov rcx, rax
007E3E97  48 85 C0                        test rax, rax
007E3E9A  75 0A                           jne 0x1407e3ea6
007E3E9C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007E3EA1  E9 07 06 00 00                  jmp 0x1407e44ad
007E3EA6  8B 45 EB                        mov eax, dword ptr [rbp - 0x15]
007E3EA9  44 8B F6                        mov r14d, esi
007E3EAC  89 01                           mov dword ptr [rcx], eax
007E3EAE  49 8B 04 24                     mov rax, qword ptr [r12]
007E3EB2  89 70 04                        mov dword ptr [rax + 4], esi
007E3EB5  44 3B 75 EB                     cmp r14d, dword ptr [rbp - 0x15]
007E3EB9  0F 83 04 03 00 00               jae 0x1407e41c3
007E3EBF  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007E3EC4  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E3EC9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E3ECE  4C 8B CF                        mov r9, rdi
007E3ED1  45 33 C0                        xor r8d, r8d
007E3ED4  C7 44 24 20 FE 00 00 00         mov dword ptr [rsp + 0x20], 0xfe
007E3EDC  41 8B D6                        mov edx, r14d
007E3EDF  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
007E3EE3  48 89 75 87                     mov qword ptr [rbp - 0x79], rsi
007E3EE7  E8 24 98 EC FF                  call 0x1406ad710
007E3EEC  85 C0                           test eax, eax
007E3EEE  0F 88 CF 02 00 00               js 0x1407e41c3
007E3EF4  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007E3EF7  4C 8D 45 97                     lea r8, [rbp - 0x69]
007E3EFB  48 D1 E8                        shr rax, 1
007E3EFE  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
007E3F03  0F 57 C0                        xorps xmm0, xmm0
007E3F06  BA 19 00 02 00                  mov edx, 0x20019
007E3F0B  66 89 74 47 10                  mov word ptr [rdi + rax*2 + 0x10], si
007E3F10  0F B7 47 0C                     movzx eax, word ptr [rdi + 0xc]
007E3F14  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
007E3F19  66 83 C0 02                     add ax, 2
007E3F1D  66 89 44 24 42                  mov word ptr [rsp + 0x42], ax
007E3F22  48 8D 47 10                     lea rax, [rdi + 0x10]
007E3F26  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007E3F2B  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
007E3F30  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
007E3F34  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E3F39  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
007E3F3D  C7 45 97 30 00 00 00            mov dword ptr [rbp - 0x69], 0x30
007E3F44  C7 45 AF 40 02 00 00            mov dword ptr [rbp - 0x51], 0x240
007E3F4B  F3 0F 7F 45 B7                  movdqu xmmword ptr [rbp - 0x49], xmm0
007E3F50  E8 BB 93 EC FF                  call 0x1406ad310
007E3F55  85 C0                           test eax, eax
007E3F57  0F 88 66 02 00 00               js 0x1407e41c3
007E3F5D  4C 8D 45 8B                     lea r8, [rbp - 0x75]
007E3F61  33 D2                           xor edx, edx
007E3F63  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E3F68  E8 13 F5 1A 00                  call 0x140993480
007E3F6D  48 8D 15 CC 53 32 00            lea rdx, [rip + 0x3253cc]
007E3F74  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E3F79  E8 02 68 C4 FF                  call 0x14042a780
007E3F7E  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E3F83  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E3F88  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E3F8D  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007E3F92  4C 8B CF                        mov r9, rdi
007E3F95  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
007E3F99  41 B8 01 00 00 00               mov r8d, 1
007E3F9F  E8 0C 94 EC FF                  call 0x1406ad3b0
007E3FA4  85 C0                           test eax, eax
007E3FA6  78 0E                           js 0x1407e3fb6
007E3FA8  83 7F 04 04                     cmp dword ptr [rdi + 4], 4
007E3FAC  75 08                           jne 0x1407e3fb6
007E3FAE  8B 47 08                        mov eax, dword ptr [rdi + 8]
007E3FB1  8B 34 38                        mov esi, dword ptr [rax + rdi]
007E3FB4  EB 03                           jmp 0x1407e3fb9
007E3FB6  83 CE FF                        or esi, 0xffffffff
007E3FB9  48 8D 15 A0 53 32 00            lea rdx, [rip + 0x3253a0]
007E3FC0  89 75 87                        mov dword ptr [rbp - 0x79], esi
007E3FC3  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E3FC8  E8 B3 67 C4 FF                  call 0x14042a780
007E3FCD  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E3FD2  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E3FD7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E3FDC  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007E3FE1  4C 8B CF                        mov r9, rdi
007E3FE4  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
007E3FE8  41 B8 01 00 00 00               mov r8d, 1
007E3FEE  E8 BD 93 EC FF                  call 0x1406ad3b0
007E3FF3  85 C0                           test eax, eax
007E3FF5  78 37                           js 0x1407e402e
007E3FF7  83 7F 04 01                     cmp dword ptr [rdi + 4], 1
007E3FFB  75 31                           jne 0x1407e402e
007E3FFD  8B 57 0C                        mov edx, dword ptr [rdi + 0xc]
007E4000  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007E4006  48 8B CB                        mov rcx, rbx
007E4009  E8 E2 E0 39 00                  call 0x140b820f0
007E400E  8B 4F 0C                        mov ecx, dword ptr [rdi + 0xc]
007E4011  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
007E4015  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
007E401A  48 85 C0                        test rax, rax
007E401D  0F 84 96 01 00 00               je 0x1407e41b9
007E4023  8B 57 08                        mov edx, dword ptr [rdi + 8]
007E4026  44 8B C1                        mov r8d, ecx
007E4029  48 03 D7                        add rdx, rdi
007E402C  EB 3D                           jmp 0x1407e406b
007E402E  0F 10 05 DB 52 32 00            movups xmm0, xmmword ptr [rip + 0x3252db]
007E4035  BA 10 00 00 00                  mov edx, 0x10
007E403A  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007E4040  48 8B CB                        mov rcx, rbx
007E4043  F3 0F 7F 45 C7                  movdqu xmmword ptr [rbp - 0x39], xmm0
007E4048  E8 A3 E0 39 00                  call 0x140b820f0
007E404D  C7 44 24 60 10 00 00 00         mov dword ptr [rsp + 0x60], 0x10
007E4055  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
007E405A  48 85 C0                        test rax, rax
007E405D  0F 84 56 01 00 00               je 0x1407e41b9
007E4063  44 8B 47 0C                     mov r8d, dword ptr [rdi + 0xc]
007E4067  48 8D 55 C7                     lea rdx, [rbp - 0x39]
007E406B  48 8B C8                        mov rcx, rax
007E406E  E8 CD 27 EE FF                  call 0x1406c6840
007E4073  33 DB                           xor ebx, ebx
007E4075  48 8D 15 A4 52 32 00            lea rdx, [rip + 0x3252a4]
007E407C  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E4081  89 5D 8F                        mov dword ptr [rbp - 0x71], ebx
007E4084  E8 F7 66 C4 FF                  call 0x14042a780
007E4089  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E408E  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E4093  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E4098  44 8D 43 01                     lea r8d, [rbx + 1]
007E409C  4C 8B CF                        mov r9, rdi
007E409F  C7 44 24 20 00 01 00 00         mov dword ptr [rsp + 0x20], 0x100
007E40A7  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007E40AC  E8 FF 92 EC FF                  call 0x1406ad3b0
007E40B1  85 C0                           test eax, eax
007E40B3  78 0E                           js 0x1407e40c3
007E40B5  83 7F 04 04                     cmp dword ptr [rdi + 4], 4
007E40B9  75 08                           jne 0x1407e40c3
007E40BB  8B 47 08                        mov eax, dword ptr [rdi + 8]
007E40BE  39 1C 38                        cmp dword ptr [rax + rdi], ebx
007E40C1  74 08                           je 0x1407e40cb
007E40C3  BB 01 00 00 00                  mov ebx, 1
007E40C8  89 5D 8F                        mov dword ptr [rbp - 0x71], ebx
007E40CB  48 8D 15 FE 51 32 00            lea rdx, [rip + 0x3251fe]
007E40D2  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E40D7  E8 A4 66 C4 FF                  call 0x14042a780
007E40DC  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E40E1  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E40E6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E40EB  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007E40F0  4C 8B CF                        mov r9, rdi
007E40F3  C7 44 24 20 00 01 00 00         mov dword ptr [rsp + 0x20], 0x100
007E40FB  41 B8 01 00 00 00               mov r8d, 1
007E4101  E8 AA 92 EC FF                  call 0x1406ad3b0
007E4106  B9 04 00 00 00                  mov ecx, 4
007E410B  85 C0                           test eax, eax
007E410D  78 12                           js 0x1407e4121
007E410F  39 4F 04                        cmp dword ptr [rdi + 4], ecx
007E4112  75 0D                           jne 0x1407e4121
007E4114  8B 47 08                        mov eax, dword ptr [rdi + 8]
007E4117  83 3C 38 00                     cmp dword ptr [rax + rdi], 0
007E411B  0F 45 D9                        cmovne ebx, ecx
007E411E  89 5D 8F                        mov dword ptr [rbp - 0x71], ebx
007E4121  83 7D 8B 00                     cmp dword ptr [rbp - 0x75], 0
007E4125  75 09                           jne 0x1407e4130
007E4127  83 CE FF                        or esi, 0xffffffff
007E412A  89 4D 8F                        mov dword ptr [rbp - 0x71], ecx
007E412D  89 75 87                        mov dword ptr [rbp - 0x79], esi
007E4130  4D 8B 14 24                     mov r10, qword ptr [r12]
007E4134  33 D2                           xor edx, edx
007E4136  41 8B 42 04                     mov eax, dword ptr [r10 + 4]
007E413A  8B DA                           mov ebx, edx
007E413C  3B D0                           cmp edx, eax
007E413E  73 3E                           jae 0x1407e417e
007E4140  44 8B CB                        mov r9d, ebx
007E4143  44 8D 5A 01                     lea r11d, [rdx + 1]
007E4147  49 C1 E1 05                     shl r9, 5
007E414B  43 39 74 11 18                  cmp dword ptr [r9 + r10 + 0x18], esi
007E4150  73 05                           jae 0x1407e4157
007E4152  41 8B D3                        mov edx, r11d
007E4155  EB E3                           jmp 0x1407e413a
007E4157  45 8B 02                        mov r8d, dword ptr [r10]
007E415A  49 8D 4A 08                     lea rcx, [r10 + 8]
007E415E  44 2B C2                        sub r8d, edx
007E4161  41 8B C3                        mov eax, r11d
007E4164  41 FF C8                        dec r8d
007E4167  48 C1 E0 05                     shl rax, 5
007E416B  49 8D 52 08                     lea rdx, [r10 + 8]
007E416F  49 C1 E0 05                     shl r8, 5
007E4173  49 03 D1                        add rdx, r9
007E4176  48 03 C8                        add rcx, rax
007E4179  E8 C2 26 EE FF                  call 0x1406c6840
007E417E  49 8B 04 24                     mov rax, qword ptr [r12]
007E4182  0F 10 44 24 60                  movups xmm0, xmmword ptr [rsp + 0x60]
007E4187  48 C1 E3 05                     shl rbx, 5
007E418B  0F 10 4D 87                     movups xmm1, xmmword ptr [rbp - 0x79]
007E418F  0F 11 44 03 08                  movups xmmword ptr [rbx + rax + 8], xmm0
007E4194  0F 11 4C 03 18                  movups xmmword ptr [rbx + rax + 0x18], xmm1
007E4199  49 8B 04 24                     mov rax, qword ptr [r12]
007E419D  FF 40 04                        inc dword ptr [rax + 4]
007E41A0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E41A5  E8 06 91 EC FF                  call 0x1406ad2b0
007E41AA  41 FF C6                        inc r14d
007E41AD  BB 00 01 00 00                  mov ebx, 0x100
007E41B2  33 F6                           xor esi, esi
007E41B4  E9 FC FC FF FF                  jmp 0x1407e3eb5
007E41B9  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007E41BE  E9 DE 02 00 00                  jmp 0x1407e44a1
007E41C3  48 8D 15 26 51 32 00            lea rdx, [rip + 0x325126]
007E41CA  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E41CF  E8 AC 65 C4 FF                  call 0x14042a780
007E41D4  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E41D9  C7 45 97 30 00 00 00            mov dword ptr [rbp - 0x69], 0x30
007E41E0  0F 57 C0                        xorps xmm0, xmm0
007E41E3  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
007E41E7  4C 8D 45 97                     lea r8, [rbp - 0x69]
007E41EB  4C 89 6D 9F                     mov qword ptr [rbp - 0x61], r13
007E41EF  BA 19 00 02 00                  mov edx, 0x20019
007E41F4  C7 45 AF 40 02 00 00            mov dword ptr [rbp - 0x51], 0x240
007E41FB  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E4200  F3 0F 7F 45 B7                  movdqu xmmword ptr [rbp - 0x49], xmm0
007E4205  E8 06 91 EC FF                  call 0x1406ad310
007E420A  85 C0                           test eax, eax
007E420C  79 0C                           jns 0x1407e421a
007E420E  8B DE                           mov ebx, esi
007E4210  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
007E4215  E9 A2 02 00 00                  jmp 0x1407e44bc
007E421A  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007E421F  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E4224  41 B9 30 00 00 00               mov r9d, 0x30
007E422A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E422F  4C 8D 45 D7                     lea r8, [rbp - 0x29]
007E4233  45 8D 71 D2                     lea r14d, [r9 - 0x2e]
007E4237  41 8B D6                        mov edx, r14d
007E423A  E8 51 91 EC FF                  call 0x1406ad390
007E423F  8B D8                           mov ebx, eax
007E4241  85 C0                           test eax, eax
007E4243  0F 88 64 02 00 00               js 0x1407e44ad
007E4249  8B 55 EB                        mov edx, dword ptr [rbp - 0x15]
007E424C  B9 00 01 00 00                  mov ecx, 0x100
007E4251  FF CA                           dec edx
007E4253  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007E4259  48 C1 E2 05                     shl rdx, 5
007E425D  48 83 C2 28                     add rdx, 0x28
007E4261  E8 8A DE 39 00                  call 0x140b820f0
007E4266  49 89 07                        mov qword ptr [r15], rax
007E4269  48 8B C8                        mov rcx, rax
007E426C  48 85 C0                        test rax, rax
007E426F  0F 84 27 FC FF FF               je 0x1407e3e9c
007E4275  8B 45 EB                        mov eax, dword ptr [rbp - 0x15]
007E4278  45 33 ED                        xor r13d, r13d
007E427B  89 41 04                        mov dword ptr [rcx + 4], eax
007E427E  49 8B 0F                        mov rcx, qword ptr [r15]
007E4281  8B 45 EB                        mov eax, dword ptr [rbp - 0x15]
007E4284  89 01                           mov dword ptr [rcx], eax
007E4286  3B 75 EB                        cmp esi, dword ptr [rbp - 0x15]
007E4289  0F 83 1C 02 00 00               jae 0x1407e44ab
007E428F  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007E4294  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E4299  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E429E  4C 8B CF                        mov r9, rdi
007E42A1  45 33 C0                        xor r8d, r8d
007E42A4  C7 44 24 20 FE 00 00 00         mov dword ptr [rsp + 0x20], 0xfe
007E42AC  8B D6                           mov edx, esi
007E42AE  E8 5D 94 EC FF                  call 0x1406ad710
007E42B3  8B D8                           mov ebx, eax
007E42B5  85 C0                           test eax, eax
007E42B7  0F 88 EE 01 00 00               js 0x1407e44ab
007E42BD  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007E42C0  4C 8D 45 97                     lea r8, [rbp - 0x69]
007E42C4  48 D1 E8                        shr rax, 1
007E42C7  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
007E42CC  0F 57 C0                        xorps xmm0, xmm0
007E42CF  BA 19 00 02 00                  mov edx, 0x20019
007E42D4  66 44 89 6C 47 10               mov word ptr [rdi + rax*2 + 0x10], r13w
007E42DA  0F B7 47 0C                     movzx eax, word ptr [rdi + 0xc]
007E42DE  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
007E42E3  66 41 03 C6                     add ax, r14w
007E42E7  66 89 44 24 42                  mov word ptr [rsp + 0x42], ax
007E42EC  48 8D 47 10                     lea rax, [rdi + 0x10]
007E42F0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007E42F5  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
007E42FA  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
007E42FE  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E4303  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
007E4307  C7 45 97 30 00 00 00            mov dword ptr [rbp - 0x69], 0x30
007E430E  C7 45 AF 40 02 00 00            mov dword ptr [rbp - 0x51], 0x240
007E4315  F3 0F 7F 45 B7                  movdqu xmmword ptr [rbp - 0x49], xmm0
007E431A  E8 F1 8F EC FF                  call 0x1406ad310
007E431F  8B D8                           mov ebx, eax
007E4321  85 C0                           test eax, eax
007E4323  0F 88 82 01 00 00               js 0x1407e44ab
007E4329  48 8D 15 60 4F 32 00            lea rdx, [rip + 0x324f60]
007E4330  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E4335  E8 46 64 C4 FF                  call 0x14042a780
007E433A  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E433F  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E4344  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E4349  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007E434E  4C 8B CF                        mov r9, rdi
007E4351  C7 44 24 20 00 01 00 00         mov dword ptr [rsp + 0x20], 0x100
007E4359  41 B8 01 00 00 00               mov r8d, 1
007E435F  E8 4C 90 EC FF                  call 0x1406ad3b0
007E4364  85 C0                           test eax, eax
007E4366  0F 88 30 01 00 00               js 0x1407e449c
007E436C  BB 04 00 00 00                  mov ebx, 4
007E4371  39 5F 04                        cmp dword ptr [rdi + 4], ebx
007E4374  0F 85 22 01 00 00               jne 0x1407e449c
007E437A  49 8B 0F                        mov rcx, qword ptr [r15]
007E437D  48 8D 15 2C 4F 32 00            lea rdx, [rip + 0x324f2c]
007E4384  8B C6                           mov eax, esi
007E4386  4C 8D 34 40                     lea r14, [rax + rax*2]
007E438A  8B 47 08                        mov eax, dword ptr [rdi + 8]
007E438D  8B 04 38                        mov eax, dword ptr [rax + rdi]
007E4390  42 89 44 F1 08                  mov dword ptr [rcx + r14*8 + 8], eax
007E4395  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E439A  E8 E1 63 C4 FF                  call 0x14042a780
007E439F  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E43A4  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E43A9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E43AE  44 8D 43 FD                     lea r8d, [rbx - 3]
007E43B2  4C 8B CF                        mov r9, rdi
007E43B5  C7 44 24 20 00 01 00 00         mov dword ptr [rsp + 0x20], 0x100
007E43BD  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007E43C2  E8 E9 8F EC FF                  call 0x1406ad3b0
007E43C7  85 C0                           test eax, eax
007E43C9  0F 88 CD 00 00 00               js 0x1407e449c
007E43CF  39 5F 04                        cmp dword ptr [rdi + 4], ebx
007E43D2  0F 85 C4 00 00 00               jne 0x1407e449c
007E43D8  8B 47 08                        mov eax, dword ptr [rdi + 8]
007E43DB  48 8D 15 6E 4E 32 00            lea rdx, [rip + 0x324e6e]
007E43E2  49 8B 0F                        mov rcx, qword ptr [r15]
007E43E5  8B 04 38                        mov eax, dword ptr [rax + rdi]
007E43E8  42 89 44 F1 0C                  mov dword ptr [rcx + r14*8 + 0xc], eax
007E43ED  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007E43F2  E8 89 63 C4 FF                  call 0x14042a780
007E43F7  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E43FC  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007E4401  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E4406  44 8D 43 FD                     lea r8d, [rbx - 3]
007E440A  4C 8B CF                        mov r9, rdi
007E440D  C7 44 24 20 00 01 00 00         mov dword ptr [rsp + 0x20], 0x100
007E4415  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007E441A  E8 91 8F EC FF                  call 0x1406ad3b0
007E441F  8B D8                           mov ebx, eax
007E4421  85 C0                           test eax, eax
007E4423  78 77                           js 0x1407e449c
007E4425  83 7F 04 03                     cmp dword ptr [rdi + 4], 3
007E4429  75 71                           jne 0x1407e449c
007E442B  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007E442E  49 8B 0F                        mov rcx, qword ptr [r15]
007E4431  42 89 44 F1 10                  mov dword ptr [rcx + r14*8 + 0x10], eax
007E4436  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007E4439  85 C0                           test eax, eax
007E443B  74 17                           je 0x1407e4454
007E443D  8B D0                           mov edx, eax
007E443F  B9 00 01 00 00                  mov ecx, 0x100
007E4444  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007E444A  E8 A1 DC 39 00                  call 0x140b820f0
007E444F  48 8B C8                        mov rcx, rax
007E4452  EB 03                           jmp 0x1407e4457
007E4454  49 8B CD                        mov rcx, r13
007E4457  49 8B 07                        mov rax, qword ptr [r15]
007E445A  4A 89 4C F0 18                  mov qword ptr [rax + r14*8 + 0x18], rcx
007E445F  8B 57 0C                        mov edx, dword ptr [rdi + 0xc]
007E4462  85 D2                           test edx, edx
007E4464  74 1F                           je 0x1407e4485
007E4466  49 8B 07                        mov rax, qword ptr [r15]
007E4469  4A 8B 4C F0 18                  mov rcx, qword ptr [rax + r14*8 + 0x18]
007E446E  48 85 C9                        test rcx, rcx
007E4471  0F 84 42 FD FF FF               je 0x1407e41b9
007E4477  44 8B C2                        mov r8d, edx
007E447A  8B 57 08                        mov edx, dword ptr [rdi + 8]
007E447D  48 03 D7                        add rdx, rdi
007E4480  E8 BB 23 EE FF                  call 0x1406c6840
007E4485  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E448A  E8 21 8E EC FF                  call 0x1406ad2b0
007E448F  FF C6                           inc esi
007E4491  41 BE 02 00 00 00               mov r14d, 2
007E4497  E9 EA FD FF FF                  jmp 0x1407e4286
007E449C  BB 4C 01 00 C0                  mov ebx, 0xc000014c
007E44A1  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
007E44A6  E8 05 8E EC FF                  call 0x1406ad2b0
007E44AB  33 F6                           xor esi, esi
007E44AD  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007E44B2  48 85 C9                        test rcx, rcx
007E44B5  74 05                           je 0x1407e44bc
007E44B7  E8 F4 8D EC FF                  call 0x1406ad2b0
007E44BC  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007E44C1  48 85 C9                        test rcx, rcx
007E44C4  74 05                           je 0x1407e44cb
007E44C6  E8 E5 8D EC FF                  call 0x1406ad2b0
007E44CB  85 DB                           test ebx, ebx
007E44CD  79 79                           jns 0x1407e4548
007E44CF  49 8B 0C 24                     mov rcx, qword ptr [r12]
007E44D3  48 85 C9                        test rcx, rcx
007E44D6  74 34                           je 0x1407e450c
007E44D8  8B FE                           mov edi, esi
007E44DA  39 71 04                        cmp dword ptr [rcx + 4], esi
007E44DD  76 22                           jbe 0x1407e4501
007E44DF  8B C7                           mov eax, edi
007E44E1  48 C1 E0 05                     shl rax, 5
007E44E5  48 8B 4C 08 10                  mov rcx, qword ptr [rax + rcx + 0x10]
007E44EA  48 85 C9                        test rcx, rcx
007E44ED  74 07                           je 0x1407e44f6
007E44EF  33 D2                           xor edx, edx
007E44F1  E8 7A E3 39 00                  call 0x140b82870
007E44F6  49 8B 0C 24                     mov rcx, qword ptr [r12]
007E44FA  FF C7                           inc edi
007E44FC  3B 79 04                        cmp edi, dword ptr [rcx + 4]
007E44FF  72 DE                           jb 0x1407e44df
007E4501  33 D2                           xor edx, edx
007E4503  E8 68 E3 39 00                  call 0x140b82870
007E4508  49 89 34 24                     mov qword ptr [r12], rsi
007E450C  49 8B 0F                        mov rcx, qword ptr [r15]
007E450F  48 85 C9                        test rcx, rcx
007E4512  74 34                           je 0x1407e4548
007E4514  8B FE                           mov edi, esi
007E4516  39 71 04                        cmp dword ptr [rcx + 4], esi
007E4519  76 23                           jbe 0x1407e453e
007E451B  8B C7                           mov eax, edi
007E451D  48 FF C0                        inc rax
007E4520  48 8D 04 40                     lea rax, [rax + rax*2]
007E4524  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
007E4528  48 85 C9                        test rcx, rcx
007E452B  74 07                           je 0x1407e4534
007E452D  33 D2                           xor edx, edx
007E452F  E8 3C E3 39 00                  call 0x140b82870
007E4534  49 8B 0F                        mov rcx, qword ptr [r15]
007E4537  FF C7                           inc edi
007E4539  3B 79 04                        cmp edi, dword ptr [rcx + 4]
007E453C  72 DD                           jb 0x1407e451b
007E453E  33 D2                           xor edx, edx
007E4540  E8 2B E3 39 00                  call 0x140b82870
007E4545  49 89 37                        mov qword ptr [r15], rsi
007E4548  8B C3                           mov eax, ebx
007E454A  48 8B 4D 07                     mov rcx, qword ptr [rbp + 7]
007E454E  48 33 CC                        xor rcx, rsp
007E4551  E8 EA 80 EC FF                  call 0x1406ac640
007E4556  48 8B 9C 24 58 01 00 00         mov rbx, qword ptr [rsp + 0x158]
007E455E  48 81 C4 00 01 00 00            add rsp, 0x100
007E4565  41 5F                           pop r15
007E4567  41 5E                           pop r14
007E4569  41 5D                           pop r13
007E456B  41 5C                           pop r12
007E456D  5F                              pop rdi
007E456E  5E                              pop rsi
007E456F  5D                              pop rbp
007E4570  C3                              ret
007E4571  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpGetAcpiProfileInformation(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m4F;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int16 v_stack_mF6;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 6449569)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    *(unsigned __int64 *)(a2) = 0;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_m100 = 0;
    v_stack_m108 = 0;
    v_stack_mB4 = 0;
    v_stack_m9C = 0;
    v_stack_mF8 = v_xmm0;
    *(unsigned __int64 *)(a3) = 0;
    v_stack_m78 = v_xmm1;
    v_stack_m68 = v_xmm1;
    v_stack_m58 = v_xmm1;
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3298143, a3, a4);
    v_stack_mB0 = a1;
    v_stack_mA8 = v_stack_mF8;
    v_stack_mA0 = 576;
    v_stack_mB8 = (unsigned int)(v_rsi + 48);
    v_stack_m98 = v_xmm0;
    result = ZwOpenKey(v_stack_mE0, (unsigned int)(0x20019ULL), v_stack_mB8, a4);
    if (!sign_flag) goto loc_007E3E43;
    v_stack_mE0 = 0;
    goto loc_007E44AD;
loc_007E3E43:
    v_stack_m118 = v_stack_m108;
    result = ZwQueryKey(v_stack_mE0, 2, v_stack_m78, (unsigned int)((unsigned int)(v_rsi + 48)));
    if (sign_flag) goto loc_007E44AD;
    result = (unsigned int)(((unsigned int)(v_stack_m64)) - 1);
    result = (unsigned int)((result) << (5));
    result = (unsigned int)((result) + (40));
    v_stack_m108 = (unsigned int)(result);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x20204D43ULL), (unsigned int)((unsigned int)(v_rsi + 48)));
    *(unsigned __int64 *)(a2) = result;
    if (result != 0) goto loc_007E3EA6;
loc_007E3E9C:
    goto loc_007E44AD;
loc_007E3EA6:
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(v_stack_m64));
    *(unsigned int *)(*(unsigned __int64 *)(a2) + 4) = 0;
loc_007E3EB5:
    if (0 >= v_stack_m64) goto loc_007E41C3;
    v_stack_m110 = v_stack_m108;
    a3 = 0;
    v_stack_m118 = 254;
    v_stack_mD4 = 0;
    v_stack_mC8 = 0;
    result = ZwEnumerateKey(v_stack_mE0, 0, a3, a5);
    if (sign_flag) goto loc_007E41C3;
    result = ((unsigned int)(*(unsigned int *)(a5 + 12))) >> (1);
    *(unsigned __int16 *)(a5 + result * 2 + 16) = 0;
    v_stack_mF8 = (unsigned __int16)(*(unsigned __int16 *)(a5 + 12));
    result = (unsigned __int16)((*(unsigned __int16 *)(a5 + 12)) + (2));
    v_stack_mF6 = (unsigned __int16)(result);
    v_stack_mF0 = a5 + 16;
    v_stack_mB0 = v_stack_mE0;
    v_stack_mA8 = v_stack_mF8;
    v_stack_mB8 = 48;
    v_stack_mA0 = 576;
    v_stack_m98 = v_xmm0;
    result = ZwOpenKey(v_stack_m100, (unsigned int)(0x20019ULL), v_stack_mB8, a5);
    if (sign_flag) goto loc_007E41C3;
    a2 = 0;
    result = RtlUnicodeStringToInteger(v_stack_mF8, a2, v_stack_mC4, a5);
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3298252, v_stack_mC4, a5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = (unsigned int)((unsigned int)(0xC000009AULL));
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 1, a5);
    if (sign_flag) goto loc_007E3FB6;
    if ((*(unsigned int *)(a5 + 4)) != 4) goto loc_007E3FB6;
    goto loc_007E3FB9;
loc_007E3FB6:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a5 + 8)) + a5 * 1))) | (0xFFFFFFFFULL));
loc_007E3FB9:
    v_stack_mC8 = (unsigned int)(v_rsi);
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3298208, 1, a5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = (unsigned int)((unsigned int)(0xC000009AULL));
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 1, a5);
    if (sign_flag) goto loc_007E402E;
    if ((*(unsigned int *)(a5 + 4)) != 1) goto loc_007E402E;
    result = ExAllocatePool2((unsigned int)(0xC000009AULL), (unsigned int)(*(unsigned int *)(a5 + 12)), (unsigned int)(0x20204D43ULL), a5);
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)));
    v_stack_mD0 = result;
    if (result == 0) goto loc_007E41B9;
    a2 = ((unsigned int)(*(unsigned int *)(a5 + 8))) + (a5);
    goto loc_007E406B;
loc_007E402E:
    v_stack_m88 = v_xmm0;
    result = ExAllocatePool2((unsigned int)(0xC000009AULL), 16, (unsigned int)(0x20204D43ULL), a5);
    v_stack_mD8 = 16;
    v_stack_mD0 = result;
    if (result == 0) goto loc_007E41B9;
loc_007E406B:
    result = memcpy(result, v_stack_m88, (unsigned int)(*(unsigned int *)(a5 + 12)), a5);
    v_rbx = 0;
    v_stack_mC0 = 0;
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297956, (unsigned int)(*(unsigned int *)(a5 + 12)), a5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, v_rbx + 1, a5);
    if (sign_flag) goto loc_007E40C3;
    if ((*(unsigned int *)(a5 + 4)) != 4) goto loc_007E40C3;
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(a5 + 8)) + a5 * 1)) != 0) {
        v_rbx = 1;
        v_stack_mC0 = (unsigned int)(v_rbx);
    }
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297790, v_rbx + 1, a5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 1, a5);
    if (sign_flag) goto loc_007E4121;
    if ((*(unsigned int *)(a5 + 4)) == 4) {
        result = *(unsigned int *)(a5 + 8);
        if ((*(unsigned int *)(result + a5 * 1)) != 0) { v_rbx = 4; }
        v_stack_mC0 = (unsigned int)(v_rbx);
    }
    if (v_stack_mC4 == 0) {
        v_rsi = (unsigned int)((v_rsi) | (0xFFFFFFFFULL));
        v_stack_mC0 = 4;
        v_stack_mC8 = (unsigned int)(v_rsi);
    }
    a2 = 0;
loc_007E413A:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 4))))) goto loc_007E417E;
    a4 = (0) << (5);
    if ((*(unsigned int *)(a4 + *(unsigned __int64 *)(a2) * 1 + 24)) >= ((unsigned int)(v_rsi))) goto loc_007E4157;
    goto loc_007E413A;
loc_007E4157:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2)))) - ((unsigned int)((unsigned int)((unsigned int)(a2 + 1)))));
    a3 = (unsigned int)((a3) - 1);
    result = ((unsigned int)((unsigned int)(a2 + 1))) << (5);
    a3 = (a3) << (5);
    a2 = (*(unsigned __int64 *)(a2) + 8) + (a4);
    a1 = (*(unsigned __int64 *)(a2) + 8) + (result);
    result = memcpy(a1, a2, a3, a4);
loc_007E417E:
    v_rbx = (0) << (5);
    *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(a2) * 1 + 8) = v_xmm0;
    *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(a2) * 1 + 24) = v_xmm1;
    result = ZwClose(v_stack_m100, a2, a3, a4);
    v_r14 = (unsigned int)((0) + 1);
    v_rsi = 0;
    goto loc_007E3EB5;
loc_007E41B9:
    goto loc_007E44A1;
loc_007E41C3:
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297574, a3, a4);
    v_stack_mB8 = 48;
    v_stack_mA8 = v_stack_mF8;
    v_stack_mB0 = a1;
    v_stack_mA0 = 576;
    v_stack_m98 = v_xmm0;
    result = ZwOpenKey(v_stack_mE8, (unsigned int)(0x20019ULL), v_stack_mB8, a4);
    if (!sign_flag) goto loc_007E421A;
    v_stack_mE8 = 0;
    goto loc_007E44BC;
loc_007E421A:
    v_stack_m118 = v_stack_m108;
    result = ZwQueryKey(v_stack_mE8, (unsigned int)((unsigned int)(48 - 46)), v_stack_m78, 48);
    if (sign_flag) goto loc_007E44AD;
    a2 = (unsigned int)(((unsigned int)(v_stack_m64)) - 1);
    a2 = (a2) << (5);
    a2 = (a2) + (40);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x20204D43ULL), 48);
    *(unsigned __int64 *)(a3) = result;
    if (result == 0) goto loc_007E3E9C;
    v_r13 = 0;
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(v_stack_m64));
    *(unsigned int *)(*(unsigned __int64 *)(a3)) = (unsigned int)((unsigned int)(v_stack_m64));
loc_007E4286:
    if (0 >= v_stack_m64) goto loc_007E44AB;
    v_stack_m110 = v_stack_m108;
    a3 = 0;
    v_stack_m118 = 254;
    result = ZwEnumerateKey(v_stack_mE8, 0, a3, a5);
    if (sign_flag) goto loc_007E44AB;
    result = ((unsigned int)(*(unsigned int *)(a5 + 12))) >> (1);
    *(unsigned __int16 *)(a5 + result * 2 + 16) = 0;
    v_stack_mF8 = (unsigned __int16)(*(unsigned __int16 *)(a5 + 12));
    result = (unsigned __int16)((*(unsigned __int16 *)(a5 + 12)) + ((unsigned __int16)(48 - 46)));
    v_stack_mF6 = (unsigned __int16)(result);
    v_stack_mF0 = a5 + 16;
    v_stack_mB0 = v_stack_mE8;
    v_stack_mA8 = v_stack_mF8;
    v_stack_mB8 = 48;
    v_stack_mA0 = 576;
    v_stack_m98 = v_xmm0;
    result = ZwOpenKey(v_stack_m100, (unsigned int)(0x20019ULL), v_stack_mB8, a5);
    if (sign_flag) goto loc_007E44AB;
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297120, v_stack_mB8, a5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 1, a5);
    if (sign_flag) goto loc_007E449C;
    if ((*(unsigned int *)(a5 + 4)) != 4) goto loc_007E449C;
    *(unsigned int *)(*(unsigned __int64 *)(a3) + 0 + 0 * 2 * 8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a5 + 8)) + a5 * 1)));
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297068, 1, a5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 4 - 3, a5);
    if (sign_flag) goto loc_007E449C;
    if ((*(unsigned int *)(a5 + 4)) != 4) goto loc_007E449C;
    *(unsigned int *)(*(unsigned __int64 *)(a3) + 0 + 0 * 2 * 8 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a5 + 8)) + a5 * 1)));
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3296878, 4 - 3, a5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 4 - 3, a5);
    if (sign_flag) goto loc_007E449C;
    if ((*(unsigned int *)(a5 + 4)) != 3) goto loc_007E449C;
    *(unsigned int *)(*(unsigned __int64 *)(a3) + 0 + 0 * 2 * 8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12))) == 0) goto loc_007E4454;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), (unsigned int)(0x20204D43ULL), a5);
    goto loc_007E4457;
loc_007E4454:
loc_007E4457:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 0 + 0 * 2 * 8 + 24) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12))) == 0) goto loc_007E4485;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 0 + 0 * 2 * 8 + 24) == 0) goto loc_007E41B9;
    a2 = ((unsigned int)(*(unsigned int *)(a5 + 8))) + (a5);
    result = memcpy(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 0 + 0 * 2 * 8 + 24), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
loc_007E4485:
    result = ZwClose(v_stack_m100, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_007E4286;
loc_007E449C:
loc_007E44A1:
    result = ZwClose(v_stack_m100, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
loc_007E44AB:
    v_rsi = 0;
loc_007E44AD:
    if (v_stack_mE8 != 0) {
        result = ZwClose(v_stack_mE8, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
    }
    if (v_stack_mE0 != 0) {
        result = ZwClose(v_stack_mE0, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
    }
    if (!sign_flag) goto loc_007E4548;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_007E450C;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2) + 4)) <= 0) goto loc_007E4501;
loc_007E44DF:
    result = (0) << (5);
    if (*(unsigned __int64 *)(result + *(unsigned __int64 *)(a2) * 1 + 16) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + *(unsigned __int64 *)(a2) * 1 + 16), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
    }
    v_rdi = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rdi)) < (*(unsigned int *)(*(unsigned __int64 *)(a2) + 4))) goto loc_007E44DF;
loc_007E4501:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a2), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
    *(unsigned __int64 *)(a2) = 0;
loc_007E450C:
    if (*(unsigned __int64 *)(a3) == 0) goto loc_007E4548;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a3) + 4)) <= 0) goto loc_007E453E;
loc_007E451B:
    result = (0) + 1;
    result = result + result * 2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + result + result * 2 * 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + result + result * 2 * 8), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
    }
    v_rdi = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rdi)) < (*(unsigned int *)(*(unsigned __int64 *)(a3) + 4))) goto loc_007E451B;
loc_007E453E:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a3), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
    *(unsigned __int64 *)(a3) = 0;
loc_007E4548:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 12)))), a5);
    v_rsp = (v_rsp) + (256);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpGetAcpiProfileInformation(int64_t Arg1, void *Arg2, void *Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m48;
    uint64_t v_stack_m4F;
    uint64_t v_stack_m58;
    uint32_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint16_t v_stack_mF6;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x6269A1)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    *(uint64_t *)(arg2) = 0;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_m100 = 0;
    v_stack_m108 = 0;
    v_stack_mB4 = 0;
    v_stack_m9C = 0;
    v_stack_mF8 = v_xmm0;
    *(uint64_t *)(arg3) = 0;
    v_stack_m78 = v_xmm1;
    v_stack_m68 = v_xmm1;
    v_stack_m58 = v_xmm1;
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3298143, Arg3, Arg4);
    v_stack_mB0 = Arg1;
    v_stack_mA8 = v_stack_mF8;
    v_stack_mA0 = 576;
    v_stack_mB8 = (uint32_t)(local_rsi + 48);
    v_stack_m98 = v_xmm0;
    result = ZwOpenKey(v_stack_mE0, (uint32_t)(0x20019ULL), v_stack_mB8, Arg4);
    if (!sign_flag) goto loc_007E3E43;
    v_stack_mE0 = 0;
    goto loc_007E44AD;
loc_007E3E43:
    v_stack_m118 = v_stack_m108;
    result = ZwQueryKey(v_stack_mE0, 2, v_stack_m78, (uint32_t)((uint32_t)(local_rsi + 48)));
    if (sign_flag) goto loc_007E44AD;
    result = (uint32_t)(((uint32_t)(v_stack_m64)) - 1);
    result = (uint32_t)((result) << (5));
    result = (uint32_t)((result) + (40));
    v_stack_m108 = (uint32_t)(result);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x20204D43ULL), (uint32_t)((uint32_t)(local_rsi + 48)));
    *(uint64_t *)(arg2) = result;
    if (result != 0) goto loc_007E3EA6;
loc_007E3E9C:
    goto loc_007E44AD;
loc_007E3EA6:
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(v_stack_m64));
    *(uint32_t *)(*(uint64_t *)(arg2) + 0x4) = 0;
loc_007E3EB5:
    if (0 >= v_stack_m64) goto loc_007E41C3;
    v_stack_m110 = v_stack_m108;
    Arg3 = 0;
    v_stack_m118 = 254;
    v_stack_mD4 = 0;
    v_stack_mC8 = 0;
    result = ZwEnumerateKey(v_stack_mE0, 0, Arg3, Arg5);
    if (sign_flag) goto loc_007E41C3;
    result = ((uint32_t)(*(uint32_t *)(arg5 + 0xC))) >> (1);
    *(uint16_t *)(arg5 + result * 2 + 0x10) = 0;
    v_stack_mF8 = (uint16_t)(*(uint16_t *)(arg5 + 0xC));
    result = (uint16_t)((*(uint16_t *)(arg5 + 0xC)) + (2));
    v_stack_mF6 = (uint16_t)(result);
    v_stack_mF0 = Arg5 + 16;
    v_stack_mB0 = v_stack_mE0;
    v_stack_mA8 = v_stack_mF8;
    v_stack_mB8 = 48;
    v_stack_mA0 = 576;
    v_stack_m98 = v_xmm0;
    result = ZwOpenKey(v_stack_m100, (uint32_t)(0x20019ULL), v_stack_mB8, Arg5);
    if (sign_flag) goto loc_007E41C3;
    Arg2 = 0;
    result = RtlUnicodeStringToInteger(v_stack_mF8, Arg2, v_stack_mC4, Arg5);
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3298252, v_stack_mC4, Arg5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = (uint32_t)((uint32_t)(0xC000009AULL));
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 1, Arg5);
    if (sign_flag) goto loc_007E3FB6;
    if ((*(uint32_t *)(arg5 + 0x4)) != 4) goto loc_007E3FB6;
    goto loc_007E3FB9;
loc_007E3FB6:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg5 + 0x8)) + arg5 * 1))) | (0xFFFFFFFFULL));
loc_007E3FB9:
    v_stack_mC8 = (uint32_t)(local_rsi);
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3298208, 1, Arg5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = (uint32_t)((uint32_t)(0xC000009AULL));
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 1, Arg5);
    if (sign_flag) goto loc_007E402E;
    if ((*(uint32_t *)(arg5 + 0x4)) != 1) goto loc_007E402E;
    result = ExAllocatePool2((uint32_t)(0xC000009AULL), (uint32_t)(*(uint32_t *)(arg5 + 0xC)), (uint32_t)(0x20204D43ULL), Arg5);
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)));
    v_stack_mD0 = result;
    if (result == 0) goto loc_007E41B9;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg5 + 0x8))) + (Arg5);
    goto loc_007E406B;
loc_007E402E:
    v_stack_m88 = v_xmm0;
    result = ExAllocatePool2((uint32_t)(0xC000009AULL), 16, (uint32_t)(0x20204D43ULL), Arg5);
    v_stack_mD8 = 16;
    v_stack_mD0 = result;
    if (result == 0) goto loc_007E41B9;
loc_007E406B:
    result = memcpy(result, v_stack_m88, (uint32_t)(*(uint32_t *)(arg5 + 0xC)), Arg5);
    local_rbx = 0;
    v_stack_mC0 = 0;
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297956, (uint32_t)(*(uint32_t *)(arg5 + 0xC)), Arg5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, local_rbx + 1, Arg5);
    if (sign_flag) goto loc_007E40C3;
    if ((*(uint32_t *)(arg5 + 0x4)) != 4) goto loc_007E40C3;
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(arg5 + 0x8)) + arg5 * 1)) != 0) {
        local_rbx = 1;
        v_stack_mC0 = (uint32_t)(local_rbx);
    }
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297790, local_rbx + 1, Arg5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 1, Arg5);
    if (sign_flag) goto loc_007E4121;
    if ((*(uint32_t *)(arg5 + 0x4)) == 4) {
        result = *(uint32_t *)(arg5 + 0x8);
        if ((*(uint32_t *)(result + arg5 * 1)) != 0) { local_rbx = 4; }
        v_stack_mC0 = (uint32_t)(local_rbx);
    }
    if (v_stack_mC4 == 0) {
        local_rsi = (uint32_t)((local_rsi) | (0xFFFFFFFFULL));
        v_stack_mC0 = 4;
        v_stack_mC8 = (uint32_t)(local_rsi);
    }
    Arg2 = 0;
loc_007E413A:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x4))))) goto loc_007E417E;
    Arg4 = (0) << (5);
    if ((*(uint32_t *)(Arg4 + *(uint64_t *)(arg2) * 1 + 0x18)) >= ((uint32_t)(local_rsi))) goto loc_007E4157;
    goto loc_007E413A;
loc_007E4157:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2)))) - ((uint32_t)((uint32_t)((uint32_t)(Arg2 + 1)))));
    Arg3 = (uint32_t)((Arg3) - 1);
    result = ((uint32_t)((uint32_t)(Arg2 + 1))) << (5);
    Arg3 = (Arg3) << (5);
    Arg2 = (*(uint64_t *)(arg2) + 8) + (Arg4);
    Arg1 = (*(uint64_t *)(arg2) + 8) + (result);
    result = memcpy(Arg1, Arg2, Arg3, Arg4);
loc_007E417E:
    local_rbx = (0) << (5);
    *(uint64_t *)(local_rbx + *(uint64_t *)(arg2) * 1 + 0x8) = v_xmm0;
    *(uint64_t *)(local_rbx + *(uint64_t *)(arg2) * 1 + 0x18) = v_xmm1;
    result = ZwClose(v_stack_m100, Arg2, Arg3, Arg4);
    local_r14 = (uint32_t)((0) + 1);
    local_rsi = 0;
    goto loc_007E3EB5;
loc_007E41B9:
    goto loc_007E44A1;
loc_007E41C3:
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297574, Arg3, Arg4);
    v_stack_mB8 = 48;
    v_stack_mA8 = v_stack_mF8;
    v_stack_mB0 = Arg1;
    v_stack_mA0 = 576;
    v_stack_m98 = v_xmm0;
    result = ZwOpenKey(v_stack_mE8, (uint32_t)(0x20019ULL), v_stack_mB8, Arg4);
    if (!sign_flag) goto loc_007E421A;
    v_stack_mE8 = 0;
    goto loc_007E44BC;
loc_007E421A:
    v_stack_m118 = v_stack_m108;
    result = ZwQueryKey(v_stack_mE8, (uint32_t)((uint32_t)(48 - 46)), v_stack_m78, 48);
    if (sign_flag) goto loc_007E44AD;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m64)) - 1);
    Arg2 = (Arg2) << (5);
    Arg2 = (Arg2) + (40);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x20204D43ULL), 48);
    *(uint64_t *)(arg3) = result;
    if (result == 0) goto loc_007E3E9C;
    local_r13 = 0;
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(v_stack_m64));
    *(uint32_t *)(*(uint64_t *)(arg3)) = (uint32_t)((uint32_t)(v_stack_m64));
loc_007E4286:
    if (0 >= v_stack_m64) goto loc_007E44AB;
    v_stack_m110 = v_stack_m108;
    Arg3 = 0;
    v_stack_m118 = 254;
    result = ZwEnumerateKey(v_stack_mE8, 0, Arg3, Arg5);
    if (sign_flag) goto loc_007E44AB;
    result = ((uint32_t)(*(uint32_t *)(arg5 + 0xC))) >> (1);
    *(uint16_t *)(arg5 + result * 2 + 0x10) = 0;
    v_stack_mF8 = (uint16_t)(*(uint16_t *)(arg5 + 0xC));
    result = (uint16_t)((*(uint16_t *)(arg5 + 0xC)) + ((uint16_t)(48 - 46)));
    v_stack_mF6 = (uint16_t)(result);
    v_stack_mF0 = Arg5 + 16;
    v_stack_mB0 = v_stack_mE8;
    v_stack_mA8 = v_stack_mF8;
    v_stack_mB8 = 48;
    v_stack_mA0 = 576;
    v_stack_m98 = v_xmm0;
    result = ZwOpenKey(v_stack_m100, (uint32_t)(0x20019ULL), v_stack_mB8, Arg5);
    if (sign_flag) goto loc_007E44AB;
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297120, v_stack_mB8, Arg5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 1, Arg5);
    if (sign_flag) goto loc_007E449C;
    if ((*(uint32_t *)(arg5 + 0x4)) != 4) goto loc_007E449C;
    *(uint32_t *)(*(uint64_t *)(arg3) + 0x0 + 0x0 * 2 * 8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg5 + 0x8)) + arg5 * 1)));
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3297068, 1, Arg5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 4 - 3, Arg5);
    if (sign_flag) goto loc_007E449C;
    if ((*(uint32_t *)(arg5 + 0x4)) != 4) goto loc_007E449C;
    *(uint32_t *)(*(uint64_t *)(arg3) + 0x0 + 0x0 * 2 * 8 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg5 + 0x8)) + arg5 * 1)));
    result = RtlInitUnicodeString(v_stack_mF8, v_rip + 3296878, 4 - 3, Arg5);
    v_stack_m110 = v_stack_m108;
    v_stack_m118 = 256;
    result = ZwQueryValueKey(v_stack_m100, v_stack_mF8, 4 - 3, Arg5);
    if (sign_flag) goto loc_007E449C;
    if ((*(uint32_t *)(arg5 + 0x4)) != 3) goto loc_007E449C;
    *(uint32_t *)(*(uint64_t *)(arg3) + 0x0 + 0x0 * 2 * 8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC))) == 0) goto loc_007E4454;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), (uint32_t)(0x20204D43ULL), Arg5);
    goto loc_007E4457;
loc_007E4454:
loc_007E4457:
    *(uint64_t *)(*(uint64_t *)(arg3) + 0x0 + 0x0 * 2 * 8 + 0x18) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC))) == 0) goto loc_007E4485;
    if (*(uint64_t *)(*(uint64_t *)(arg3) + 0x0 + 0x0 * 2 * 8 + 0x18) == 0) goto loc_007E41B9;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg5 + 0x8))) + (Arg5);
    result = memcpy(*(uint64_t *)(*(uint64_t *)(arg3) + 0x0 + 0x0 * 2 * 8 + 0x18), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
loc_007E4485:
    result = ZwClose(v_stack_m100, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_007E4286;
loc_007E449C:
loc_007E44A1:
    result = ZwClose(v_stack_m100, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
loc_007E44AB:
    local_rsi = 0;
loc_007E44AD:
    if (v_stack_mE8 != 0) {
        result = ZwClose(v_stack_mE8, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
    }
    if (v_stack_mE0 != 0) {
        result = ZwClose(v_stack_mE0, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
    }
    if (!sign_flag) goto loc_007E4548;
    if (*(uint64_t *)(arg2) == 0) goto loc_007E450C;
    if ((*(uint32_t *)(*(uint64_t *)(arg2) + 0x4)) <= 0) goto loc_007E4501;
loc_007E44DF:
    result = (0) << (5);
    if (*(uint64_t *)(result + *(uint64_t *)(arg2) * 1 + 0x10) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(result + *(uint64_t *)(arg2) * 1 + 0x10), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
    }
    local_rdi = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rdi)) < (*(uint32_t *)(*(uint64_t *)(arg2) + 0x4))) goto loc_007E44DF;
loc_007E4501:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg2), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
    *(uint64_t *)(arg2) = 0;
loc_007E450C:
    if (*(uint64_t *)(arg3) == 0) goto loc_007E4548;
    if ((*(uint32_t *)(*(uint64_t *)(arg3) + 0x4)) <= 0) goto loc_007E453E;
loc_007E451B:
    result = (0) + 1;
    result = result + result * 2;
    if (*(uint64_t *)(*(uint64_t *)(arg3) + result + result * 2 * 8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg3) + result + result * 2 * 8), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
    }
    local_rdi = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rdi)) < (*(uint32_t *)(*(uint64_t *)(arg3) + 0x4))) goto loc_007E451B;
loc_007E453E:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg3), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
    *(uint64_t *)(arg3) = 0;
loc_007E4548:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0xC)))), Arg5);
    local_rsp = (local_rsp) + (256);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg5` | `+ 0x4` | `32` | `R` |
| `Arg5` | `+ 0x8` | `32` | `R` |
| `Arg5` | `+ 0xC` | `16` | `R` |
| `Arg5` | `+ 0xC` | `32` | `R` |
| `Arg5` | `+ 0x10` | `64` | `R` |
| `Arg5` | `+ 0x10 + rax*2` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E3D7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
