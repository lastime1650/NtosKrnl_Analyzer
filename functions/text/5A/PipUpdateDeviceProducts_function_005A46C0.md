# PipUpdateDeviceProducts

- RVA: `0x005A46C0`–`0x005A4D5F` (길이 `1,695` bytes)
- VA: `0x00000001405A46C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5294`
- 디코드: `414`개 명령, `1,695/1,695` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x005A4745` → [_PnpCtxGetCachedContextBaseKey](../../page/8E/_PnpCtxGetCachedContextBaseKey_function_008EFB2C.md) (function, `0x008EFB2C`)
- `0x005A4773` → [PnpCtxRegOpenKey](../../page/8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x005A47A8` → [RtlGetPersistedStateLocation](../../page/8C/RtlGetPersistedStateLocation_function_008C8DE0.md) (function, `0x008C8DE0`)
- `0x005A47C8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005A4802` → [RtlGetPersistedStateLocation](../../page/8C/RtlGetPersistedStateLocation_function_008C8DE0.md) (function, `0x008C8DE0`)
- `0x005A4834` → [PnpCtxRegCreateTree](../../page/93/PnpCtxRegCreateTree_function_00931CA0.md) (function, `0x00931CA0`)
- `0x005A484D` → [KeQueryBootTimeValues](../49/KeQueryBootTimeValues_function_0049F444.md) (function, `0x0049F444`)
- `0x005A4875` → [PnpCtxRegQueryInfoKey](../../page/99/PnpCtxRegQueryInfoKey_function_009945FC.md) (function, `0x009945FC`)
- `0x005A48A7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005A48D5` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (function, `0x00A22E0C`)
- `0x005A48F2` → [PnpCtxRegEnumKey](../../page/99/PnpCtxRegEnumKey_function_009929C0.md) (function, `0x009929C0`)
- `0x005A491C` → [PnpCtxRegOpenKey](../../page/8E/PnpCtxRegOpenKey_function_008EF7B8.md) (function, `0x008EF7B8`)
- `0x005A4951` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x005A4979` → [wcsicmp](../50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x005A49A2` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x005A49BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A49E4` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x005A4A00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005A4A2A` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x005A4A52` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A4A7B` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x005A4A9F` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x005A4AAF` → [PnpCtxRegDeleteValue](../../page/8F/PnpCtxRegDeleteValue_function_008FE5E0.md) (function, `0x008FE5E0`)
- `0x005A4AE6` → [PnpCtxRegQueryInfoKey](../../page/99/PnpCtxRegQueryInfoKey_function_009945FC.md) (function, `0x009945FC`)
- `0x005A4B16` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005A4B45` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (function, `0x00A22E0C`)
- `0x005A4B74` → [PnpCtxRegEnumValue](../../page/99/PnpCtxRegEnumValue_function_0099364C.md) (function, `0x0099364C`)
- `0x005A4BAD` → [PnpCtxRegCreateKey](../../page/A6/PnpCtxRegCreateKey_function_00A692E4.md) (function, `0x00A692E4`)
- `0x005A4BE2` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x005A4C08` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x005A4C39` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x005A4C64` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x005A4C87` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x005A4CB7` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (function, `0x00A22E0C`)
- `0x005A4CC5` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (function, `0x00A22E0C`)
- `0x005A4CD3` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (function, `0x00A22E0C`)
- `0x005A4CE1` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (function, `0x00A22E0C`)
- `0x005A4CF0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A4CFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A4D0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A4D1D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A4D2C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005A4D38` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005A46E3` → RVA `0x00E0A740` (`.data`; read)
- `0x005A46FE` → RVA `0x00E66398` (`.data`; read)
- `0x005A475F` → RVA `0x006CB1B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A478F` → RVA `0x006CB1E0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A479A` → RVA `0x006CB2B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A48C1` → RVA `0x006CB160` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A4945` → RVA `0x006CB150` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A49D8` → RVA `0x006CB170` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A4A69` → RVA `0x006CB180` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A4A89` → RVA `0x006CB2F0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A4BD0` → RVA `0x006CB320` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A4C18` → RVA `0x006CB340` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A4C52` → RVA `0x006CB350` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **40**
  - `0x005A4745` → [_PnpCtxGetCachedContextBaseKey](../../page/8E/_PnpCtxGetCachedContextBaseKey_function_008EFB2C.md) (`.text` → `PAGE`)
  - `0x005A4773` → [PnpCtxRegOpenKey](../../page/8E/PnpCtxRegOpenKey_function_008EF7B8.md) (`.text` → `PAGE`)
  - `0x005A47A8` → [RtlGetPersistedStateLocation](../../page/8C/RtlGetPersistedStateLocation_function_008C8DE0.md) (`.text` → `PAGE`)
  - `0x005A47C8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005A4802` → [RtlGetPersistedStateLocation](../../page/8C/RtlGetPersistedStateLocation_function_008C8DE0.md) (`.text` → `PAGE`)
  - `0x005A4834` → [PnpCtxRegCreateTree](../../page/93/PnpCtxRegCreateTree_function_00931CA0.md) (`.text` → `PAGE`)
  - `0x005A4875` → [PnpCtxRegQueryInfoKey](../../page/99/PnpCtxRegQueryInfoKey_function_009945FC.md) (`.text` → `PAGE`)
  - `0x005A48A7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005A48D5` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (`.text` → `PAGE`)
  - `0x005A48F2` → [PnpCtxRegEnumKey](../../page/99/PnpCtxRegEnumKey_function_009929C0.md) (`.text` → `PAGE`)
  - `0x005A491C` → [PnpCtxRegOpenKey](../../page/8E/PnpCtxRegOpenKey_function_008EF7B8.md) (`.text` → `PAGE`)
  - `0x005A4951` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (`.text` → `PAGE`)
  - `0x005A49A2` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (`.text` → `PAGE`)
  - `0x005A49BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x005A49E4` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (`.text` → `PAGE`)
  - `0x005A4A00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005A4A2A` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (`.text` → `PAGE`)
  - `0x005A4A52` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x005A4A7B` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (`.text` → `PAGE`)
  - `0x005A4A9F` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (`.text` → `PAGE`)
  - `0x005A4AAF` → [PnpCtxRegDeleteValue](../../page/8F/PnpCtxRegDeleteValue_function_008FE5E0.md) (`.text` → `PAGE`)
  - `0x005A4AE6` → [PnpCtxRegQueryInfoKey](../../page/99/PnpCtxRegQueryInfoKey_function_009945FC.md) (`.text` → `PAGE`)
  - `0x005A4B16` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005A4B45` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (`.text` → `PAGE`)
  - `0x005A4B74` → [PnpCtxRegEnumValue](../../page/99/PnpCtxRegEnumValue_function_0099364C.md) (`.text` → `PAGE`)
  - `0x005A4BAD` → [PnpCtxRegCreateKey](../../page/A6/PnpCtxRegCreateKey_function_00A692E4.md) (`.text` → `PAGE`)
  - `0x005A4BE2` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (`.text` → `PAGE`)
  - `0x005A4C08` → [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) (`.text` → `PAGE`)
  - `0x005A4C39` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (`.text` → `PAGE`)
  - `0x005A4C64` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (`.text` → `PAGE`)
  - `0x005A4C87` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (`.text` → `PAGE`)
  - `0x005A4CB7` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (`.text` → `PAGE`)
  - `0x005A4CC5` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (`.text` → `PAGE`)
  - `0x005A4CD3` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (`.text` → `PAGE`)
  - `0x005A4CE1` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (`.text` → `PAGE`)
  - `0x005A4CF0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x005A4CFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x005A4D0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x005A4D1D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x005A4D2C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A46C0  48 8B C4                        mov rax, rsp
005A46C3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
005A46C7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
005A46CB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
005A46CF  55                              push rbp
005A46D0  41 54                           push r12
005A46D2  41 55                           push r13
005A46D4  41 56                           push r14
005A46D6  41 57                           push r15
005A46D8  48 8D 68 A1                     lea rbp, [rax - 0x5f]
005A46DC  48 81 EC D0 00 00 00            sub rsp, 0xd0
005A46E3  48 8B 05 56 60 86 00            mov rax, qword ptr [rip + 0x866056]
005A46EA  48 33 C4                        xor rax, rsp
005A46ED  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
005A46F1  33 F6                           xor esi, esi
005A46F3  48 89 4D BF                     mov qword ptr [rbp - 0x41], rcx
005A46F7  48 8B D9                        mov rbx, rcx
005A46FA  48 89 75 DF                     mov qword ptr [rbp - 0x21], rsi
005A46FE  48 8B 0D 93 1C 8C 00            mov rcx, qword ptr [rip + 0x8c1c93]
005A4705  4C 8D 45 07                     lea r8, [rbp + 7]
005A4709  48 89 75 0F                     mov qword ptr [rbp + 0xf], rsi
005A470D  8B FE                           mov edi, esi
005A470F  8D 56 0F                        lea edx, [rsi + 0xf]
005A4712  48 89 75 E7                     mov qword ptr [rbp - 0x19], rsi
005A4716  44 8B FE                        mov r15d, esi
005A4719  48 89 75 C7                     mov qword ptr [rbp - 0x39], rsi
005A471D  48 89 75 07                     mov qword ptr [rbp + 7], rsi
005A4721  44 8B E6                        mov r12d, esi
005A4724  48 89 75 D7                     mov qword ptr [rbp - 0x29], rsi
005A4728  48 89 75 FF                     mov qword ptr [rbp - 1], rsi
005A472C  89 75 A7                        mov dword ptr [rbp - 0x59], esi
005A472F  89 75 CF                        mov dword ptr [rbp - 0x31], esi
005A4732  89 75 D3                        mov dword ptr [rbp - 0x2d], esi
005A4735  89 75 EF                        mov dword ptr [rbp - 0x11], esi
005A4738  89 75 F3                        mov dword ptr [rbp - 0xd], esi
005A473B  89 75 F7                        mov dword ptr [rbp - 9], esi
005A473E  89 75 AF                        mov dword ptr [rbp - 0x51], esi
005A4741  48 89 75 B7                     mov qword ptr [rbp - 0x49], rsi
005A4745  E8 E2 B3 34 00                  call 0x1408efb2c
005A474A  85 C0                           test eax, eax
005A474C  0F 88 4A 05 00 00               js 0x1405a4c9c
005A4752  48 8B 55 07                     mov rdx, qword ptr [rbp + 7]
005A4756  48 8D 45 FF                     lea rax, [rbp - 1]
005A475A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005A475F  4C 8D 05 4A 6A 12 00            lea r8, [rip + 0x126a4a]
005A4766  45 33 C9                        xor r9d, r9d
005A4769  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
005A4771  33 C9                           xor ecx, ecx
005A4773  E8 40 B0 34 00                  call 0x1408ef7b8
005A4778  3D 34 00 00 C0                  cmp eax, 0xc0000034
005A477D  0F 84 19 05 00 00               je 0x1405a4c9c
005A4783  48 8D 45 A7                     lea rax, [rbp - 0x59]
005A4787  45 33 C9                        xor r9d, r9d
005A478A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005A478F  4C 8D 05 4A 6A 12 00            lea r8, [rip + 0x126a4a]
005A4796  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
005A479A  48 8D 0D 0F 6B 12 00            lea rcx, [rip + 0x126b0f]
005A47A1  33 D2                           xor edx, edx
005A47A3  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
005A47A8  E8 33 46 32 00                  call 0x1408c8de0
005A47AD  3D 05 00 00 80                  cmp eax, 0x80000005
005A47B2  0F 85 E4 04 00 00               jne 0x1405a4c9c
005A47B8  8B 5D A7                        mov ebx, dword ptr [rbp - 0x59]
005A47BB  B9 00 01 00 00                  mov ecx, 0x100
005A47C0  8B D3                           mov edx, ebx
005A47C2  41 B8 50 70 69 6E               mov r8d, 0x6e697050
005A47C8  E8 23 D9 5D 00                  call 0x140b820f0
005A47CD  48 89 45 07                     mov qword ptr [rbp + 7], rax
005A47D1  4C 8B F8                        mov r15, rax
005A47D4  48 85 C0                        test rax, rax
005A47D7  0F 84 C4 04 00 00               je 0x1405a4ca1
005A47DD  48 8D 45 A7                     lea rax, [rbp - 0x59]
005A47E1  45 33 C9                        xor r9d, r9d
005A47E4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005A47E9  4C 8D 05 F0 69 12 00            lea r8, [rip + 0x1269f0]
005A47F0  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
005A47F4  48 8D 0D B5 6A 12 00            lea rcx, [rip + 0x126ab5]
005A47FB  33 D2                           xor edx, edx
005A47FD  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
005A4802  E8 D9 45 32 00                  call 0x1408c8de0
005A4807  85 C0                           test eax, eax
005A4809  0F 88 92 04 00 00               js 0x1405a4ca1
005A480F  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
005A4814  48 8D 45 E7                     lea rax, [rbp - 0x19]
005A4818  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005A481D  45 33 C9                        xor r9d, r9d
005A4820  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
005A4825  4D 8B C7                        mov r8, r15
005A4828  33 D2                           xor edx, edx
005A482A  C7 44 24 20 1F 00 02 00         mov dword ptr [rsp + 0x20], 0x2001f
005A4832  33 C9                           xor ecx, ecx
005A4834  E8 67 D4 38 00                  call 0x140931ca0
005A4839  85 C0                           test eax, eax
005A483B  0F 85 60 04 00 00               jne 0x1405a4ca1
005A4841  4C 8D 45 0F                     lea r8, [rbp + 0xf]
005A4845  48 8D 55 DF                     lea rdx, [rbp - 0x21]
005A4849  48 8D 4D A7                     lea rcx, [rbp - 0x59]
005A484D  E8 F2 AB EF FF                  call 0x14049f444
005A4852  48 8B 45 0F                     mov rax, qword ptr [rbp + 0xf]
005A4856  4C 8D 4D CF                     lea r9, [rbp - 0x31]
005A485A  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
005A485E  4C 8D 45 EF                     lea r8, [rbp - 0x11]
005A4862  48 29 45 DF                     sub qword ptr [rbp - 0x21], rax
005A4866  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
005A486B  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
005A4870  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
005A4875  E8 82 FD 3E 00                  call 0x1409945fc
005A487A  85 C0                           test eax, eax
005A487C  0F 85 1F 04 00 00               jne 0x1405a4ca1
005A4882  44 8B 75 EF                     mov r14d, dword ptr [rbp - 0x11]
005A4886  45 85 F6                        test r14d, r14d
005A4889  0F 84 36 02 00 00               je 0x1405a4ac5
005A488F  44 8B 6D CF                     mov r13d, dword ptr [rbp - 0x31]
005A4893  B9 00 01 00 00                  mov ecx, 0x100
005A4898  41 FF C5                        inc r13d
005A489B  41 B8 50 70 69 6E               mov r8d, 0x6e697050
005A48A1  41 8B D5                        mov edx, r13d
005A48A4  48 03 D2                        add rdx, rdx
005A48A7  E8 44 D8 5D 00                  call 0x140b820f0
005A48AC  4C 8B E0                        mov r12, rax
005A48AF  48 85 C0                        test rax, rax
005A48B2  0F 84 E9 03 00 00               je 0x1405a4ca1
005A48B8  45 85 F6                        test r14d, r14d
005A48BB  0F 84 04 02 00 00               je 0x1405a4ac5
005A48C1  4C 8D 3D 98 68 12 00            lea r15, [rip + 0x126898]
005A48C8  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
005A48CC  44 89 6D CF                     mov dword ptr [rbp - 0x31], r13d
005A48D0  48 85 D2                        test rdx, rdx
005A48D3  74 0A                           je 0x1405a48df
005A48D5  E8 32 E5 47 00                  call 0x140a22e0c
005A48DA  48 83 65 C7 00                  and qword ptr [rbp - 0x39], 0
005A48DF  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
005A48E3  48 8D 45 CF                     lea rax, [rbp - 0x31]
005A48E7  4D 8B CC                        mov r9, r12
005A48EA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A48EF  44 8B C6                        mov r8d, esi
005A48F2  E8 C9 E0 3E 00                  call 0x1409929c0
005A48F7  85 C0                           test eax, eax
005A48F9  0F 88 B5 01 00 00               js 0x1405a4ab4
005A48FF  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
005A4903  48 8D 45 C7                     lea rax, [rbp - 0x39]
005A4907  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005A490C  45 33 C9                        xor r9d, r9d
005A490F  4D 8B C4                        mov r8, r12
005A4912  C7 44 24 20 1F 00 02 00         mov dword ptr [rsp + 0x20], 0x2001f
005A491A  33 C9                           xor ecx, ecx
005A491C  E8 97 AE 34 00                  call 0x1408ef7b8
005A4921  85 C0                           test eax, eax
005A4923  0F 88 8B 01 00 00               js 0x1405a4ab4
005A4929  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
005A492D  48 8D 45 A7                     lea rax, [rbp - 0x59]
005A4931  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005A4936  4C 8D 4D AF                     lea r9, [rbp - 0x51]
005A493A  48 8D 45 17                     lea rax, [rbp + 0x17]
005A493E  C7 45 A7 0E 00 00 00            mov dword ptr [rbp - 0x59], 0xe
005A4945  4C 8D 05 04 68 12 00            lea r8, [rip + 0x126804]
005A494C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A4951  E8 A6 F7 3E 00                  call 0x1409940fc
005A4956  85 C0                           test eax, eax
005A4958  0F 88 56 01 00 00               js 0x1405a4ab4
005A495E  83 7D AF 01                     cmp dword ptr [rbp - 0x51], 1
005A4962  0F 85 4C 01 00 00               jne 0x1405a4ab4
005A4968  83 7D A7 0E                     cmp dword ptr [rbp - 0x59], 0xe
005A496C  0F 85 42 01 00 00               jne 0x1405a4ab4
005A4972  49 8B D7                        mov rdx, r15
005A4975  48 8D 4D 17                     lea rcx, [rbp + 0x17]
005A4979  E8 02 B7 F5 FF                  call 0x140500080
005A497E  85 C0                           test eax, eax
005A4980  0F 85 2E 01 00 00               jne 0x1405a4ab4
005A4986  21 45 A7                        and dword ptr [rbp - 0x59], eax
005A4989  45 33 C9                        xor r9d, r9d
005A498C  48 8B 55 FF                     mov rdx, qword ptr [rbp - 1]
005A4990  48 8D 45 A7                     lea rax, [rbp - 0x59]
005A4994  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005A4999  4D 8B C4                        mov r8, r12
005A499C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005A49A2  E8 55 F7 3E 00                  call 0x1409940fc
005A49A7  3D 34 00 00 C0                  cmp eax, 0xc0000034
005A49AC  0F 85 02 01 00 00               jne 0x1405a4ab4
005A49B2  48 85 FF                        test rdi, rdi
005A49B5  74 0C                           je 0x1405a49c3
005A49B7  33 D2                           xor edx, edx
005A49B9  48 8B CF                        mov rcx, rdi
005A49BC  E8 AF DE 5D 00                  call 0x140b82870
005A49C1  33 FF                           xor edi, edi
005A49C3  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
005A49C7  48 8D 45 A7                     lea rax, [rbp - 0x59]
005A49CB  83 65 A7 00                     and dword ptr [rbp - 0x59], 0
005A49CF  4C 8D 4D AF                     lea r9, [rbp - 0x51]
005A49D3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005A49D8  4C 8D 05 91 67 12 00            lea r8, [rip + 0x126791]
005A49DF  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
005A49E4  E8 13 F7 3E 00                  call 0x1409940fc
005A49E9  3D 23 00 00 C0                  cmp eax, 0xc0000023
005A49EE  75 3F                           jne 0x1405a4a2f
005A49F0  8B 5D A7                        mov ebx, dword ptr [rbp - 0x59]
005A49F3  B9 00 01 00 00                  mov ecx, 0x100
005A49F8  8B D3                           mov edx, ebx
005A49FA  41 B8 50 70 69 6E               mov r8d, 0x6e697050
005A4A00  E8 EB D6 5D 00                  call 0x140b820f0
005A4A05  48 8B F8                        mov rdi, rax
005A4A08  48 85 C0                        test rax, rax
005A4A0B  74 4C                           je 0x1405a4a59
005A4A0D  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
005A4A11  48 8D 45 A7                     lea rax, [rbp - 0x59]
005A4A15  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005A4A1A  4C 8D 4D AF                     lea r9, [rbp - 0x51]
005A4A1E  4C 8D 05 4B 67 12 00            lea r8, [rip + 0x12674b]
005A4A25  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
005A4A2A  E8 CD F6 3E 00                  call 0x1409940fc
005A4A2F  3D 34 00 00 C0                  cmp eax, 0xc0000034
005A4A34  74 7E                           je 0x1405a4ab4
005A4A36  8B 5D A7                        mov ebx, dword ptr [rbp - 0x59]
005A4A39  85 C0                           test eax, eax
005A4A3B  78 0B                           js 0x1405a4a48
005A4A3D  83 7D AF 01                     cmp dword ptr [rbp - 0x51], 1
005A4A41  75 05                           jne 0x1405a4a48
005A4A43  83 FB 02                        cmp ebx, 2
005A4A46  73 11                           jae 0x1405a4a59
005A4A48  48 85 FF                        test rdi, rdi
005A4A4B  74 0C                           je 0x1405a4a59
005A4A4D  33 D2                           xor edx, edx
005A4A4F  48 8B CF                        mov rcx, rdi
005A4A52  E8 19 DE 5D 00                  call 0x140b82870
005A4A57  33 FF                           xor edi, edi
005A4A59  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
005A4A5D  48 8D 45 DF                     lea rax, [rbp - 0x21]
005A4A61  C7 44 24 28 08 00 00 00         mov dword ptr [rsp + 0x28], 8
005A4A69  4C 8D 05 10 67 12 00            lea r8, [rip + 0x126710]
005A4A70  41 B9 03 00 00 00               mov r9d, 3
005A4A76  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A4A7B  E8 0C D1 3E 00                  call 0x140991b8c
005A4A80  48 85 FF                        test rdi, rdi
005A4A83  74 1F                           je 0x1405a4aa4
005A4A85  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
005A4A89  4C 8D 05 60 68 12 00            lea r8, [rip + 0x126860]
005A4A90  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
005A4A94  41 B9 01 00 00 00               mov r9d, 1
005A4A9A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
005A4A9F  E8 E8 D0 3E 00                  call 0x140991b8c
005A4AA4  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
005A4AA8  4C 8D 05 C1 66 12 00            lea r8, [rip + 0x1266c1]
005A4AAF  E8 2C 9B 35 00                  call 0x1408fe5e0
005A4AB4  FF C6                           inc esi
005A4AB6  41 3B F6                        cmp esi, r14d
005A4AB9  0F 82 09 FE FF FF               jb 0x1405a48c8
005A4ABF  4C 8B 7D 07                     mov r15, qword ptr [rbp + 7]
005A4AC3  33 F6                           xor esi, esi
005A4AC5  48 8B 55 FF                     mov rdx, qword ptr [rbp - 1]
005A4AC9  48 8D 45 D3                     lea rax, [rbp - 0x2d]
005A4ACD  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
005A4AD2  45 33 C9                        xor r9d, r9d
005A4AD5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005A4ADA  45 33 C0                        xor r8d, r8d
005A4ADD  48 8D 45 F3                     lea rax, [rbp - 0xd]
005A4AE1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A4AE6  E8 11 FB 3E 00                  call 0x1409945fc
005A4AEB  85 C0                           test eax, eax
005A4AED  0F 85 B3 01 00 00               jne 0x1405a4ca6
005A4AF3  8B 75 F3                        mov esi, dword ptr [rbp - 0xd]
005A4AF6  85 F6                           test esi, esi
005A4AF8  0F 84 A8 01 00 00               je 0x1405a4ca6
005A4AFE  44 8B 75 D3                     mov r14d, dword ptr [rbp - 0x2d]
005A4B02  B9 00 01 00 00                  mov ecx, 0x100
005A4B07  41 FF C6                        inc r14d
005A4B0A  41 B8 50 70 69 6E               mov r8d, 0x6e697050
005A4B10  41 8B D6                        mov edx, r14d
005A4B13  48 03 D2                        add rdx, rdx
005A4B16  E8 D5 D5 5D 00                  call 0x140b820f0
005A4B1B  4C 8B E8                        mov r13, rax
005A4B1E  48 85 C0                        test rax, rax
005A4B21  0F 84 83 01 00 00               je 0x1405a4caa
005A4B27  33 DB                           xor ebx, ebx
005A4B29  85 F6                           test esi, esi
005A4B2B  0F 84 79 01 00 00               je 0x1405a4caa
005A4B31  4C 8D 3D 28 66 12 00            lea r15, [rip + 0x126628]
005A4B38  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
005A4B3C  44 89 75 D3                     mov dword ptr [rbp - 0x2d], r14d
005A4B40  48 85 D2                        test rdx, rdx
005A4B43  74 0A                           je 0x1405a4b4f
005A4B45  E8 C2 E2 47 00                  call 0x140a22e0c
005A4B4A  48 83 65 D7 00                  and qword ptr [rbp - 0x29], 0
005A4B4F  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
005A4B55  48 8D 45 D3                     lea rax, [rbp - 0x2d]
005A4B59  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005A4B5F  4D 8B CD                        mov r9, r13
005A4B62  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005A4B68  44 8B C3                        mov r8d, ebx
005A4B6B  48 8B 55 FF                     mov rdx, qword ptr [rbp - 1]
005A4B6F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A4B74  E8 D3 EA 3E 00                  call 0x14099364c
005A4B79  85 C0                           test eax, eax
005A4B7B  0F 88 0B 01 00 00               js 0x1405a4c8c
005A4B81  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
005A4B85  48 8D 45 F7                     lea rax, [rbp - 9]
005A4B89  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005A4B8E  45 33 C9                        xor r9d, r9d
005A4B91  48 8D 45 D7                     lea rax, [rbp - 0x29]
005A4B95  4D 8B C5                        mov r8, r13
005A4B98  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005A4B9D  33 C9                           xor ecx, ecx
005A4B9F  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005A4BA5  C7 44 24 20 06 00 02 00         mov dword ptr [rsp + 0x20], 0x20006
005A4BAD  E8 32 47 4C 00                  call 0x140a692e4
005A4BB2  85 C0                           test eax, eax
005A4BB4  0F 88 D2 00 00 00               js 0x1405a4c8c
005A4BBA  83 7D F7 01                     cmp dword ptr [rbp - 9], 1
005A4BBE  75 27                           jne 0x1405a4be7
005A4BC0  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
005A4BC4  48 8D 45 DF                     lea rax, [rbp - 0x21]
005A4BC8  C7 44 24 28 08 00 00 00         mov dword ptr [rsp + 0x28], 8
005A4BD0  4C 8D 05 49 67 12 00            lea r8, [rip + 0x126749]
005A4BD7  41 B9 03 00 00 00               mov r9d, 3
005A4BDD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A4BE2  E8 A5 CF 3E 00                  call 0x140991b8c
005A4BE7  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
005A4BEB  48 8D 45 A7                     lea rax, [rbp - 0x59]
005A4BEF  83 65 A7 00                     and dword ptr [rbp - 0x59], 0
005A4BF3  4C 8D 05 76 65 12 00            lea r8, [rip + 0x126576]
005A4BFA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005A4BFF  45 33 C9                        xor r9d, r9d
005A4C02  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005A4C08  E8 EF F4 3E 00                  call 0x1409940fc
005A4C0D  3D 34 00 00 C0                  cmp eax, 0xc0000034
005A4C12  75 78                           jne 0x1405a4c8c
005A4C14  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
005A4C18  48 8D 05 21 67 12 00            lea rax, [rip + 0x126721]
005A4C1F  C7 44 24 28 10 00 00 00         mov dword ptr [rsp + 0x28], 0x10
005A4C27  4C 8D 05 42 65 12 00            lea r8, [rip + 0x126542]
005A4C2E  41 B9 01 00 00 00               mov r9d, 1
005A4C34  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A4C39  E8 4E CF 3E 00                  call 0x140991b8c
005A4C3E  85 C0                           test eax, eax
005A4C40  78 4A                           js 0x1405a4c8c
005A4C42  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
005A4C46  48 8D 45 DF                     lea rax, [rbp - 0x21]
005A4C4A  C7 44 24 28 08 00 00 00         mov dword ptr [rsp + 0x28], 8
005A4C52  4C 8D 05 F7 66 12 00            lea r8, [rip + 0x1266f7]
005A4C59  41 B9 03 00 00 00               mov r9d, 3
005A4C5F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A4C64  E8 23 CF 3E 00                  call 0x140991b8c
005A4C69  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
005A4C6D  4C 8D 05 DC 64 12 00            lea r8, [rip + 0x1264dc]
005A4C74  41 B9 01 00 00 00               mov r9d, 1
005A4C7A  C7 44 24 28 0E 00 00 00         mov dword ptr [rsp + 0x28], 0xe
005A4C82  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
005A4C87  E8 00 CF 3E 00                  call 0x140991b8c
005A4C8C  FF C3                           inc ebx
005A4C8E  3B DE                           cmp ebx, esi
005A4C90  0F 82 A2 FE FF FF               jb 0x1405a4b38
005A4C96  4C 8B 7D 07                     mov r15, qword ptr [rbp + 7]
005A4C9A  EB 0E                           jmp 0x1405a4caa
005A4C9C  4C 8B EE                        mov r13, rsi
005A4C9F  EB 0D                           jmp 0x1405a4cae
005A4CA1  4C 8B EE                        mov r13, rsi
005A4CA4  EB 04                           jmp 0x1405a4caa
005A4CA6  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
005A4CAA  48 8B 5D BF                     mov rbx, qword ptr [rbp - 0x41]
005A4CAE  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
005A4CB2  48 85 D2                        test rdx, rdx
005A4CB5  74 05                           je 0x1405a4cbc
005A4CB7  E8 50 E1 47 00                  call 0x140a22e0c
005A4CBC  48 8B 55 FF                     mov rdx, qword ptr [rbp - 1]
005A4CC0  48 85 D2                        test rdx, rdx
005A4CC3  74 05                           je 0x1405a4cca
005A4CC5  E8 42 E1 47 00                  call 0x140a22e0c
005A4CCA  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
005A4CCE  48 85 D2                        test rdx, rdx
005A4CD1  74 05                           je 0x1405a4cd8
005A4CD3  E8 34 E1 47 00                  call 0x140a22e0c
005A4CD8  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
005A4CDC  48 85 D2                        test rdx, rdx
005A4CDF  74 05                           je 0x1405a4ce6
005A4CE1  E8 26 E1 47 00                  call 0x140a22e0c
005A4CE6  4D 85 ED                        test r13, r13
005A4CE9  74 0A                           je 0x1405a4cf5
005A4CEB  33 D2                           xor edx, edx
005A4CED  49 8B CD                        mov rcx, r13
005A4CF0  E8 7B DB 5D 00                  call 0x140b82870
005A4CF5  4D 85 E4                        test r12, r12
005A4CF8  74 0A                           je 0x1405a4d04
005A4CFA  33 D2                           xor edx, edx
005A4CFC  49 8B CC                        mov rcx, r12
005A4CFF  E8 6C DB 5D 00                  call 0x140b82870
005A4D04  48 85 FF                        test rdi, rdi
005A4D07  74 0A                           je 0x1405a4d13
005A4D09  33 D2                           xor edx, edx
005A4D0B  48 8B CF                        mov rcx, rdi
005A4D0E  E8 5D DB 5D 00                  call 0x140b82870
005A4D13  4D 85 FF                        test r15, r15
005A4D16  74 0A                           je 0x1405a4d22
005A4D18  33 D2                           xor edx, edx
005A4D1A  49 8B CF                        mov rcx, r15
005A4D1D  E8 4E DB 5D 00                  call 0x140b82870
005A4D22  48 85 DB                        test rbx, rbx
005A4D25  74 0A                           je 0x1405a4d31
005A4D27  33 D2                           xor edx, edx
005A4D29  48 8B CB                        mov rcx, rbx
005A4D2C  E8 3F DB 5D 00                  call 0x140b82870
005A4D31  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
005A4D35  48 33 CC                        xor rcx, rsp
005A4D38  E8 03 79 10 00                  call 0x1406ac640
005A4D3D  4C 8D 9C 24 D0 00 00 00         lea r11, [rsp + 0xd0]
005A4D45  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
005A4D49  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
005A4D4D  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
005A4D51  49 8B E3                        mov rsp, r11
005A4D54  41 5F                           pop r15
005A4D56  41 5E                           pop r14
005A4D58  41 5D                           pop r13
005A4D5A  41 5C                           pop r12
005A4D5C  5D                              pop rbp
005A4D5D  C3                              ret
005A4D5E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipUpdateDeviceProducts(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 8806486)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = a1;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 25) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 57) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = 0;
    *(unsigned int *)(v_rsp - 95 - 89) = 0;
    *(unsigned int *)(v_rsp - 95 - 49) = 0;
    *(unsigned int *)(v_rsp - 95 - 45) = 0;
    *(unsigned int *)(v_rsp - 95 - 17) = 0;
    *(unsigned int *)(v_rsp - 95 - 13) = 0;
    *(unsigned int *)(v_rsp - 95 - 9) = 0;
    *(unsigned int *)(v_rsp - 95 - 81) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 73) = 0;
    result = _PnpCtxGetCachedContextBaseKey(*(unsigned __int64 *)(v_rip + 9182355), v_rsi + 15, v_rsp - 95 + 7, a4);
    if (sign_flag) goto loc_005A4C9C;
    v_stack_mD0 = v_rsp - 95 - 1;
    a4 = 0;
    v_stack_mD8 = 0x20019ULL;
    a1 = 0;
    result = PnpCtxRegOpenKey(a1, *(unsigned __int64 *)(v_rsp - 95 + 7), v_rip + 1206858, a4);
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_005A4C9C;
    a4 = 0;
    v_stack_mC8 = v_rsp - 95 - 89;
    v_stack_mD0 = 0;
    a2 = 0;
    v_stack_mD8 = 0;
    result = RtlGetPersistedStateLocation(v_rip + 1207055, a2, v_rip + 1206858, a4);
    if (((unsigned int)(result)) != 0x80000005ULL) goto loc_005A4C9C;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))), (unsigned int)(0x6E697050ULL), a4);
    *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
    if (result == 0) goto loc_005A4CA1;
    a4 = 0;
    v_stack_mC8 = v_rsp - 95 - 89;
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)));
    a2 = 0;
    v_stack_mD8 = result;
    result = RtlGetPersistedStateLocation(v_rip + 1206965, a2, v_rip + 1206768, a4);
    if (sign_flag) goto loc_005A4CA1;
    v_stack_mC0 = 0;
    v_stack_mC8 = v_rsp - 95 - 25;
    a4 = 0;
    v_stack_mD0 = 0;
    a2 = 0;
    v_stack_mD8 = 0x2001FULL;
    a1 = 0;
    result = PnpCtxRegCreateTree(a1, a2, result, a4);
    if ((unsigned int)(result) != 0) goto loc_005A4CA1;
    result = KeQueryBootTimeValues(v_rsp - 95 - 89, v_rsp - 95 - 33, v_rsp - 95 + 15, a4);
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    result = PnpCtxRegQueryInfoKey(v_rsp - 95 - 89, *(unsigned __int64 *)(v_rsp - 95 - 25), v_rsp - 95 - 17, v_rsp - 95 - 49);
    if ((unsigned int)(result) != 0) goto loc_005A4CA1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17))) == 0) goto loc_005A4AC5;
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 49))) + 1);
    a2 = ((unsigned int)((unsigned int)(v_r13))) + ((unsigned int)((unsigned int)(v_r13)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x6E697050ULL), v_rsp - 95 - 49);
    if (result == 0) goto loc_005A4CA1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17))) == 0) goto loc_005A4AC5;
loc_005A48C8:
    *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)(v_r13);
    if (*(unsigned __int64 *)(v_rsp - 95 - 57) != 0) {
        result = PnpCtxRegCloseKey(256, *(unsigned __int64 *)(v_rsp - 95 - 57), (unsigned int)(0x6E697050ULL), v_rsp - 95 - 49);
    }
    v_stack_mD8 = v_rsp - 95 - 49;
    result = PnpCtxRegEnumKey(256, *(unsigned __int64 *)(v_rsp - 95 - 25), 0, result);
    if (sign_flag) goto loc_005A4AB4;
    v_stack_mD0 = v_rsp - 95 - 57;
    a4 = 0;
    v_stack_mD8 = 0x2001FULL;
    a1 = 0;
    result = PnpCtxRegOpenKey(a1, *(unsigned __int64 *)(v_rsp - 95 - 25), result, a4);
    if (sign_flag) goto loc_005A4AB4;
    v_stack_mD0 = v_rsp - 95 - 89;
    *(unsigned int *)(v_rsp - 95 - 89) = 14;
    v_stack_mD8 = v_rsp - 95 + 23;
    result = PnpCtxRegQueryValue(a1, *(unsigned __int64 *)(v_rsp - 95 - 57), v_rip + 1206276, v_rsp - 95 - 81);
    if (sign_flag) goto loc_005A4AB4;
    if ((*(unsigned int *)(v_rsp - 95 - 81)) != 1) goto loc_005A4AB4;
    if ((*(unsigned int *)(v_rsp - 95 - 89)) != 14) goto loc_005A4AB4;
    result = wcsicmp(v_rsp - 95 + 23, v_rip + 1206424, v_rip + 1206276, v_rsp - 95 - 81);
    if ((unsigned int)(result) != 0) goto loc_005A4AB4;
    a4 = 0;
    v_stack_mD0 = v_rsp - 95 - 89;
    result = PnpCtxRegQueryValue(v_rsp - 95 + 23, *(unsigned __int64 *)(v_rsp - 95 - 1), result, a4);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_005A4AB4;
    v_rdi = 0;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, result, a4);
        v_rdi = 0;
    }
    v_stack_mD0 = v_rsp - 95 - 89;
    v_stack_mD8 = 0;
    result = PnpCtxRegQueryValue(a1, *(unsigned __int64 *)(v_rsp - 95 - 57), v_rip + 1206161, v_rsp - 95 - 81);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_005A4A2F;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))), (unsigned int)(0x6E697050ULL), v_rsp - 95 - 81);
    if (result == 0) goto loc_005A4A59;
    v_stack_mD0 = v_rsp - 95 - 89;
    v_stack_mD8 = result;
    result = PnpCtxRegQueryValue(256, *(unsigned __int64 *)(v_rsp - 95 - 57), v_rip + 1206091, v_rsp - 95 - 81);
loc_005A4A2F:
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_005A4AB4;
    if (sign_flag) goto loc_005A4A48;
    if ((*(unsigned int *)(v_rsp - 95 - 81)) != 1) goto loc_005A4A48;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)))) >= 2) goto loc_005A4A59;
loc_005A4A48:
    v_rdi = result;
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_rip + 1206091, v_rsp - 95 - 81);
        v_rdi = 0;
    }
    v_stack_mD0 = 8;
    v_stack_mD8 = v_rsp - 95 - 33;
    result = PnpCtxRegSetValue(a1, *(unsigned __int64 *)(v_rsp - 95 - 57), v_rip + 1206032, 3);
    if (0 != 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 95 - 57);
        a3 = v_rip + 1206368;
        v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 89)));
        a4 = 1;
        v_stack_mD8 = 0;
        result = PnpCtxRegSetValue(a1, a2, a3, a4);
    }
    result = PnpCtxRegDeleteValue(a1, *(unsigned __int64 *)(v_rsp - 95 - 57), v_rip + 1205953, a4);
loc_005A4AB4:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17))))) goto loc_005A48C8;
    v_rsi = 0;
loc_005A4AC5:
    v_stack_mC8 = 0;
    a4 = 0;
    v_stack_mD0 = v_rsp - 95 - 45;
    a3 = 0;
    v_stack_mD8 = v_rsp - 95 - 13;
    result = PnpCtxRegQueryInfoKey(a1, *(unsigned __int64 *)(v_rsp - 95 - 1), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_005A4CA6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 13))) == 0) goto loc_005A4CA6;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 45))) + 1);
    a2 = ((unsigned int)((unsigned int)(v_r14))) + ((unsigned int)((unsigned int)(v_r14)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x6E697050ULL), a4);
    if (result == 0) goto loc_005A4CAA;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 13))) == 0) goto loc_005A4CAA;
loc_005A4B38:
    *(unsigned int *)(v_rsp - 95 - 45) = (unsigned int)(v_r14);
    if (*(unsigned __int64 *)(v_rsp - 95 - 41) != 0) {
        result = PnpCtxRegCloseKey(256, *(unsigned __int64 *)(v_rsp - 95 - 41), (unsigned int)(0x6E697050ULL), a4);
    }
    v_stack_mD8 = v_rsp - 95 - 45;
    result = PnpCtxRegEnumValue(256, *(unsigned __int64 *)(v_rsp - 95 - 1), 0, result);
    if (sign_flag) goto loc_005A4C8C;
    v_stack_mC0 = v_rsp - 95 - 9;
    a4 = 0;
    v_stack_mC8 = v_rsp - 95 - 41;
    a1 = 0;
    v_stack_mD8 = 0x20006ULL;
    result = PnpCtxRegCreateKey(a1, *(unsigned __int64 *)(v_rsp - 95 - 25), result, a4);
    if (sign_flag) goto loc_005A4C8C;
    if ((*(unsigned int *)(v_rsp - 95 - 9)) == 1) {
        a2 = *(unsigned __int64 *)(v_rsp - 95 - 41);
        result = v_rsp - 95 - 33;
        v_stack_mD0 = 8;
        a3 = v_rip + 1206089;
        a4 = 3;
        v_stack_mD8 = result;
        result = PnpCtxRegSetValue(a1, a2, a3, a4);
    }
    v_stack_mD0 = v_rsp - 95 - 89;
    a4 = 0;
    result = PnpCtxRegQueryValue(a1, *(unsigned __int64 *)(v_rsp - 95 - 41), v_rip + 1205622, a4);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_005A4C8C;
    v_stack_mD0 = 16;
    v_stack_mD8 = v_rip + 1206049;
    result = PnpCtxRegSetValue(a1, *(unsigned __int64 *)(v_rsp - 95 - 41), v_rip + 1205570, 1);
    if (!(sign_flag)) {
        a2 = *(unsigned __int64 *)(v_rsp - 95 - 41);
        result = v_rsp - 95 - 33;
        v_stack_mD0 = 8;
        a3 = v_rip + 1206007;
        a4 = 3;
        v_stack_mD8 = result;
        result = PnpCtxRegSetValue(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(v_rsp - 95 - 41);
        a3 = v_rip + 1205468;
        a4 = 1;
        v_stack_mD0 = 14;
        v_stack_mD8 = v_rip + 1205800;
        result = PnpCtxRegSetValue(a1, a2, a3, a4);
    }
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 13))))) goto loc_005A4B38;
    goto loc_005A4CAA;
loc_005A4C9C:
    goto loc_005A4CAE;
loc_005A4CA1:
    goto loc_005A4CAA;
loc_005A4CA6:
loc_005A4CAA:
loc_005A4CAE:
    if (*(unsigned __int64 *)(v_rsp - 95 - 41) != 0) {
        result = PnpCtxRegCloseKey(a1, *(unsigned __int64 *)(v_rsp - 95 - 41), a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 1) != 0) {
        result = PnpCtxRegCloseKey(a1, *(unsigned __int64 *)(v_rsp - 95 - 1), a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 57) != 0) {
        result = PnpCtxRegCloseKey(a1, *(unsigned __int64 *)(v_rsp - 95 - 57), a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 25) != 0) {
        result = PnpCtxRegCloseKey(a1, *(unsigned __int64 *)(v_rsp - 95 - 25), a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 73) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 73);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 + 7) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 95 + 7);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 95 - 65) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsp - 95 - 65);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 39)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipUpdateDeviceProducts(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x866056)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = Arg1;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x2D) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0xD) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x9) = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x51) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x49) = 0;
    result = _PnpCtxGetCachedContextBaseKey(*(uint64_t *)(v_rip + 0x8C1C93), local_rsi + 15, local_rsp - 95 + 7, Arg4);
    if (sign_flag) goto loc_005A4C9C;
    v_stack_mD0 = local_rsp - 95 - 1;
    Arg4 = 0;
    v_stack_mD8 = 0x20019ULL;
    Arg1 = 0;
    result = PnpCtxRegOpenKey(Arg1, *(uint64_t *)(local_rsp - 0x5F + 0x7), v_rip + 1206858, Arg4);
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_005A4C9C;
    Arg4 = 0;
    v_stack_mC8 = local_rsp - 95 - 89;
    v_stack_mD0 = 0;
    Arg2 = 0;
    v_stack_mD8 = 0;
    result = RtlGetPersistedStateLocation(v_rip + 1207055, Arg2, v_rip + 1206858, Arg4);
    if (((uint32_t)(result)) != 0x80000005ULL) goto loc_005A4C9C;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))), (uint32_t)(0x6E697050ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
    if (result == 0) goto loc_005A4CA1;
    Arg4 = 0;
    v_stack_mC8 = local_rsp - 95 - 89;
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)));
    Arg2 = 0;
    v_stack_mD8 = result;
    result = RtlGetPersistedStateLocation(v_rip + 1206965, Arg2, v_rip + 1206768, Arg4);
    if (sign_flag) goto loc_005A4CA1;
    v_stack_mC0 = 0;
    v_stack_mC8 = local_rsp - 95 - 25;
    Arg4 = 0;
    v_stack_mD0 = 0;
    Arg2 = 0;
    v_stack_mD8 = 0x2001FULL;
    Arg1 = 0;
    result = PnpCtxRegCreateTree(Arg1, Arg2, result, Arg4);
    if ((uint32_t)(result) != 0) goto loc_005A4CA1;
    result = KeQueryBootTimeValues(local_rsp - 95 - 89, local_rsp - 95 - 33, local_rsp - 95 + 15, Arg4);
    v_stack_mC8 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    result = PnpCtxRegQueryInfoKey(local_rsp - 95 - 89, *(uint64_t *)(local_rsp - 0x5F - 0x19), local_rsp - 95 - 17, local_rsp - 95 - 49);
    if ((uint32_t)(result) != 0) goto loc_005A4CA1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11))) == 0) goto loc_005A4AC5;
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x31))) + 1);
    Arg2 = ((uint32_t)((uint32_t)(local_r13))) + ((uint32_t)((uint32_t)(local_r13)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x6E697050ULL), local_rsp - 95 - 49);
    if (result == 0) goto loc_005A4CA1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11))) == 0) goto loc_005A4AC5;
loc_005A48C8:
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)(local_r13);
    if (*(uint64_t *)(local_rsp - 0x5F - 0x39) != 0) {
        result = PnpCtxRegCloseKey(256, *(uint64_t *)(local_rsp - 0x5F - 0x39), (uint32_t)(0x6E697050ULL), local_rsp - 95 - 49);
    }
    v_stack_mD8 = local_rsp - 95 - 49;
    result = PnpCtxRegEnumKey(256, *(uint64_t *)(local_rsp - 0x5F - 0x19), 0, result);
    if (sign_flag) goto loc_005A4AB4;
    v_stack_mD0 = local_rsp - 95 - 57;
    Arg4 = 0;
    v_stack_mD8 = 0x2001FULL;
    Arg1 = 0;
    result = PnpCtxRegOpenKey(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x19), result, Arg4);
    if (sign_flag) goto loc_005A4AB4;
    v_stack_mD0 = local_rsp - 95 - 89;
    *(uint32_t *)(local_rsp - 0x5F - 0x59) = 14;
    v_stack_mD8 = local_rsp - 95 + 23;
    result = PnpCtxRegQueryValue(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x39), v_rip + 1206276, local_rsp - 95 - 81);
    if (sign_flag) goto loc_005A4AB4;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x51)) != 1) goto loc_005A4AB4;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x59)) != 14) goto loc_005A4AB4;
    result = wcsicmp(local_rsp - 95 + 23, v_rip + 1206424, v_rip + 1206276, local_rsp - 95 - 81);
    if ((uint32_t)(result) != 0) goto loc_005A4AB4;
    Arg4 = 0;
    v_stack_mD0 = local_rsp - 95 - 89;
    result = PnpCtxRegQueryValue(local_rsp - 95 + 23, *(uint64_t *)(local_rsp - 0x5F - 0x1), result, Arg4);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_005A4AB4;
    local_rdi = 0;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, result, Arg4);
        local_rdi = 0;
    }
    v_stack_mD0 = local_rsp - 95 - 89;
    v_stack_mD8 = 0;
    result = PnpCtxRegQueryValue(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x39), v_rip + 1206161, local_rsp - 95 - 81);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_005A4A2F;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))), (uint32_t)(0x6E697050ULL), local_rsp - 95 - 81);
    if (result == 0) goto loc_005A4A59;
    v_stack_mD0 = local_rsp - 95 - 89;
    v_stack_mD8 = result;
    result = PnpCtxRegQueryValue(256, *(uint64_t *)(local_rsp - 0x5F - 0x39), v_rip + 1206091, local_rsp - 95 - 81);
loc_005A4A2F:
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_005A4AB4;
    if (sign_flag) goto loc_005A4A48;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x51)) != 1) goto loc_005A4A48;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)))) >= 2) goto loc_005A4A59;
loc_005A4A48:
    local_rdi = result;
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_rip + 1206091, local_rsp - 95 - 81);
        local_rdi = 0;
    }
    v_stack_mD0 = 8;
    v_stack_mD8 = local_rsp - 95 - 33;
    result = PnpCtxRegSetValue(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x39), v_rip + 1206032, 3);
    if (0 != 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x39);
        Arg3 = v_rip + 1206368;
        v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x59)));
        Arg4 = 1;
        v_stack_mD8 = 0;
        result = PnpCtxRegSetValue(Arg1, Arg2, Arg3, Arg4);
    }
    result = PnpCtxRegDeleteValue(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x39), v_rip + 1205953, Arg4);
loc_005A4AB4:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11))))) goto loc_005A48C8;
    local_rsi = 0;
loc_005A4AC5:
    v_stack_mC8 = 0;
    Arg4 = 0;
    v_stack_mD0 = local_rsp - 95 - 45;
    Arg3 = 0;
    v_stack_mD8 = local_rsp - 95 - 13;
    result = PnpCtxRegQueryInfoKey(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x1), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_005A4CA6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0xD))) == 0) goto loc_005A4CA6;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x2D))) + 1);
    Arg2 = ((uint32_t)((uint32_t)(local_r14))) + ((uint32_t)((uint32_t)(local_r14)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x6E697050ULL), Arg4);
    if (result == 0) goto loc_005A4CAA;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0xD))) == 0) goto loc_005A4CAA;
loc_005A4B38:
    *(uint32_t *)(local_rsp - 0x5F - 0x2D) = (uint32_t)(local_r14);
    if (*(uint64_t *)(local_rsp - 0x5F - 0x29) != 0) {
        result = PnpCtxRegCloseKey(256, *(uint64_t *)(local_rsp - 0x5F - 0x29), (uint32_t)(0x6E697050ULL), Arg4);
    }
    v_stack_mD8 = local_rsp - 95 - 45;
    result = PnpCtxRegEnumValue(256, *(uint64_t *)(local_rsp - 0x5F - 0x1), 0, result);
    if (sign_flag) goto loc_005A4C8C;
    v_stack_mC0 = local_rsp - 95 - 9;
    Arg4 = 0;
    v_stack_mC8 = local_rsp - 95 - 41;
    Arg1 = 0;
    v_stack_mD8 = 0x20006ULL;
    result = PnpCtxRegCreateKey(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x19), result, Arg4);
    if (sign_flag) goto loc_005A4C8C;
    if ((*(uint32_t *)(local_rsp - 0x5F - 0x9)) == 1) {
        Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x29);
        result = local_rsp - 95 - 33;
        v_stack_mD0 = 8;
        Arg3 = v_rip + 1206089;
        Arg4 = 3;
        v_stack_mD8 = result;
        result = PnpCtxRegSetValue(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mD0 = local_rsp - 95 - 89;
    Arg4 = 0;
    result = PnpCtxRegQueryValue(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x29), v_rip + 1205622, Arg4);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_005A4C8C;
    v_stack_mD0 = 16;
    v_stack_mD8 = v_rip + 1206049;
    result = PnpCtxRegSetValue(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x29), v_rip + 1205570, 1);
    if (!(sign_flag)) {
        Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x29);
        result = local_rsp - 95 - 33;
        v_stack_mD0 = 8;
        Arg3 = v_rip + 1206007;
        Arg4 = 3;
        v_stack_mD8 = result;
        result = PnpCtxRegSetValue(Arg1, Arg2, Arg3, Arg4);
        Arg2 = *(uint64_t *)(local_rsp - 0x5F - 0x29);
        Arg3 = v_rip + 1205468;
        Arg4 = 1;
        v_stack_mD0 = 14;
        v_stack_mD8 = v_rip + 1205800;
        result = PnpCtxRegSetValue(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0xD))))) goto loc_005A4B38;
    goto loc_005A4CAA;
loc_005A4C9C:
    goto loc_005A4CAE;
loc_005A4CA1:
    goto loc_005A4CAA;
loc_005A4CA6:
loc_005A4CAA:
loc_005A4CAE:
    if (*(uint64_t *)(local_rsp - 0x5F - 0x29) != 0) {
        result = PnpCtxRegCloseKey(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x29), Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x1) != 0) {
        result = PnpCtxRegCloseKey(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x1), Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x39) != 0) {
        result = PnpCtxRegCloseKey(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x39), Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x19) != 0) {
        result = PnpCtxRegCloseKey(Arg1, *(uint64_t *)(local_rsp - 0x5F - 0x19), Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x49) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x5F - 0x49);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x5F + 0x7) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x5F + 0x7);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x5F - 0x41) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsp - 0x5F - 0x41);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x27)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A46C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
