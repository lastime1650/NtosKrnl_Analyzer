# MiAddLoaderHalIoMappings

- RVA: `0x00C5E568`–`0x00C5E5FD` (길이 `149` bytes)
- VA: `0x0000000140C5E568`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7694`
- 디코드: `34`개 명령, `149/149` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C5E58D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C5E597` → [MiGetAnyMultiplexedVm](../../text/44/MiGetAnyMultiplexedVm_function_00448BD0.md) (function, `0x00448BD0`)
- `0x00C5E5C8` → [MiLockWorkingSetShared](../../text/27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00C5E5D6` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (function, `0x002C2710`)
- `0x00C5E5E2` → [MiUnlockWorkingSetShared](../../text/27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)

### Direct callers
- [MiInitSystem](MiInitSystem_function_00C5E6C0.md) at `0x00C5E81C`
- [MiInitSystem](MiInitSystem_function_00C5E6C0.md) at `0x00C5E835`

### Static image references
- `0x00C5E5A7` → RVA `0x00C5E610` (`MiAddLoaderHalIoPte`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00C5E58D` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C5E597` → [MiGetAnyMultiplexedVm](../../text/44/MiGetAnyMultiplexedVm_function_00448BD0.md) (`INIT` → `.text`)
  - `0x00C5E5C8` → [MiLockWorkingSetShared](../../text/27/MiLockWorkingSetShared_function_0027CBF0.md) (`INIT` → `.text`)
  - `0x00C5E5D6` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (`INIT` → `.text`)
  - `0x00C5E5E2` → [MiUnlockWorkingSetShared](../../text/27/MiUnlockWorkingSetShared_function_0027D690.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C5E568  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C5E56D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00C5E572  57                              push rdi
00C5E573  48 81 EC E0 00 00 00            sub rsp, 0xe0
00C5E57A  48 8B FA                        mov rdi, rdx
00C5E57D  48 8B D9                        mov rbx, rcx
00C5E580  33 D2                           xor edx, edx
00C5E582  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00C5E587  41 B8 C0 00 00 00               mov r8d, 0xc0
00C5E58D  E8 AE 86 A6 FF                  call 0x1406c6c40
00C5E592  B9 01 00 00 00                  mov ecx, 1
00C5E597  E8 34 A6 7E FF                  call 0x140448bd0
00C5E59C  48 8B F0                        mov rsi, rax
00C5E59F  C7 44 24 20 07 20 00 00         mov dword ptr [rsp + 0x20], 0x2007
00C5E5A7  48 8D 05 62 00 00 00            lea rax, [rip + 0x62]
00C5E5AE  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00C5E5B3  48 8B CE                        mov rcx, rsi
00C5E5B6  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00C5E5BE  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00C5E5C3  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
00C5E5C8  E8 23 E6 61 FF                  call 0x14027cbf0
00C5E5CD  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00C5E5D2  88 44 24 29                     mov byte ptr [rsp + 0x29], al
00C5E5D6  E8 35 41 66 FF                  call 0x1402c2710
00C5E5DB  8A 54 24 29                     mov dl, byte ptr [rsp + 0x29]
00C5E5DF  48 8B CE                        mov rcx, rsi
00C5E5E2  E8 A9 F0 61 FF                  call 0x14027d690
00C5E5E7  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
00C5E5EF  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00C5E5F3  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00C5E5F7  49 8B E3                        mov rsp, r11
00C5E5FA  5F                              pop rdi
00C5E5FB  C3                              ret
00C5E5FC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAddLoaderHalIoMappings(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int8 v_stack_mBF;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (224);
    a2 = 0;
    result = memset(v_stack_mC8, a2, 192, a4);
    result = MiGetAnyMultiplexedVm(1, a2, 192, a4);
    v_stack_mC8 = 0x2007ULL;
    v_stack_mA0 = a1;
    v_stack_m20 = v_rip + 98;
    v_stack_m98 = 0;
    v_stack_mA8 = result;
    result = MiLockWorkingSetShared(result, a2, 192, a4);
    v_stack_mBF = (unsigned __int8)(result);
    result = MiWalkPageTables(v_stack_mC8, a2, 192, a4);
    result = MiUnlockWorkingSetShared(result, v_stack_mBF, 192, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiAddLoaderHalIoMappings(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m8;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint8_t v_stack_mBF;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (224);
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, 192, a4);
    result = MiGetAnyMultiplexedVm(1, Arg2, 192, a4);
    v_stack_mC8 = 0x2007ULL;
    v_stack_mA0 = Arg1;
    v_stack_m20 = v_rip + 98;
    v_stack_m98 = 0;
    v_stack_mA8 = result;
    result = MiLockWorkingSetShared(result, Arg2, 192, a4);
    v_stack_mBF = (uint8_t)(result);
    result = MiWalkPageTables(v_stack_mC8, Arg2, 192, a4);
    result = MiUnlockWorkingSetShared(result, v_stack_mBF, 192, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C5E568&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C5E568[BB_00C5E568]
  bb_00C5E5FC[BB_00C5E5FC]
```
