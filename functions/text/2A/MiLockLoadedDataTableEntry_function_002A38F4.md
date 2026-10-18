# MiLockLoadedDataTableEntry

- RVA: `0x002A38F4`–`0x002A3949` (길이 `85` bytes)
- VA: `0x00000001402A38F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068790`
- 디코드: `29`개 명령, `85/85` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A3905` → [MiAcquireLoadLock](MiAcquireLoadLock_function_002A3950.md) (function, `0x002A3950`)
- `0x002A3910` → [MmFindDataTableEntryByAddress](MmFindDataTableEntryByAddress_function_002A3C0C.md) (function, `0x002A3C0C`)
- `0x002A3929` → [MiLockLoaderEntry](MiLockLoaderEntry_function_002A3EE0.md) (function, `0x002A3EE0`)
- `0x002A3940` → [MmReleaseLoadLockShared](MmReleaseLoadLockShared_function_002A3FB0.md) (function, `0x002A3FB0`)

### Direct callers
- [MiLockLoadedDataTableEntryIfNecessary](MiLockLoadedDataTableEntryIfNecessary_function_002A38B4.md) at `0x002A38D6`
- [MmLockLoadedDataTableEntry](MmLockLoadedDataTableEntry_function_002A437C.md) at `0x002A4385`
- [LdrpKrnGetDataTableEntry](../45/LdrpKrnGetDataTableEntry_function_004563B4.md) at `0x004563BC`
- [MmLockLoadedDataTableEntryShared](../4B/MmLockLoadedDataTableEntryShared_function_004BD08C.md) at `0x004BD092`
- [MmVerifyCallbackFunctionCheckFlags](../4F/MmVerifyCallbackFunctionCheckFlags_function_004F7360.md) at `0x004F7371`
- [KasaniGetModuleFromAddress](../5A/KasaniGetModuleFromAddress_function_005AAFD0.md) at `0x005AAFFC`
- [MmWriteSystemImageTracepoint](../68/MmWriteSystemImageTracepoint_function_00684150.md) at `0x00684200`
- [MmDiscardDriverSection](../../init/C6/MmDiscardDriverSection_function_00C6C8D0.md) at `0x00C6C8F2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A38F4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002A38F9  57                              push rdi
002A38FA  48 83 EC 20                     sub rsp, 0x20
002A38FE  48 8B D9                        mov rbx, rcx
002A3901  8B FA                           mov edi, edx
002A3903  33 C9                           xor ecx, ecx
002A3905  E8 46 00 00 00                  call 0x1402a3950
002A390A  48 8B CB                        mov rcx, rbx
002A390D  4C 8B D8                        mov r11, rax
002A3910  E8 F7 02 00 00                  call 0x1402a3c0c
002A3915  48 8B D8                        mov rbx, rax
002A3918  48 85 C0                        test rax, rax
002A391B  74 20                           je 0x1402a393d
002A391D  F7 DF                           neg edi
002A391F  48 8B C8                        mov rcx, rax
002A3922  1B D2                           sbb edx, edx
002A3924  F7 D2                           not edx
002A3926  83 E2 02                        and edx, 2
002A3929  E8 B2 05 00 00                  call 0x1402a3ee0
002A392E  48 8B C3                        mov rax, rbx
002A3931  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002A3936  48 83 C4 20                     add rsp, 0x20
002A393A  5F                              pop rdi
002A393B  C3                              ret
002A393C  CC                              int3
002A393D  49 8B CB                        mov rcx, r11
002A3940  E8 6B 06 00 00                  call 0x1402a3fb0
002A3945  33 C0                           xor eax, eax
002A3947  EB E8                           jmp 0x1402a3931
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockLoadedDataTableEntry(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = MiAcquireLoadLock(a1, a2, a3, a4);
    result = MmFindDataTableEntryByAddress(0, a2, a3, a4);
    if (result == 0) goto loc_002A393D;
    v_rdi = (unsigned int)(-((unsigned int)(a2)));
    a2 = (unsigned int)(~(a2));
    a2 = (unsigned int)((a2) & (2));
    result = MiLockLoaderEntry(result, a2, a3, a4);
loc_002A3931:
    v_rsp = (v_rsp) + (32);
    return result;
loc_002A393D:
    result = MmReleaseLoadLockShared(result, a2, a3, a4);
    result = 0;
    goto loc_002A3931;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockLoadedDataTableEntry(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = MiAcquireLoadLock(Arg1, Arg2, a3, a4);
    result = MmFindDataTableEntryByAddress(0, Arg2, a3, a4);
    if (result == 0) goto loc_002A393D;
    local_rdi = (uint32_t)(-((uint32_t)(Arg2)));
    Arg2 = (uint32_t)(~(Arg2));
    Arg2 = (uint32_t)((Arg2) & (2));
    result = MiLockLoaderEntry(result, Arg2, a3, a4);
loc_002A3931:
    local_rsp = (local_rsp) + (32);
    return result;
loc_002A393D:
    result = MmReleaseLoadLockShared(result, Arg2, a3, a4);
    result = 0;
    goto loc_002A3931;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A38F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A38F4[BB_002A38F4]
  bb_002A391D[BB_002A391D]
  bb_002A3931[BB_002A3931]
  bb_002A393C[BB_002A393C]
  bb_002A393D[BB_002A393D]
  bb_002A38F4 -->|branch| bb_002A393D
  bb_002A38F4 -->|fallthrough| bb_002A391D
  bb_002A391D -->|flow| bb_002A3931
  bb_002A393C -->|flow| bb_002A393D
  bb_002A393D -->|branch| bb_002A3931
```
