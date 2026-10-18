# MiUnlockLoadedDataTableEntry

- RVA: `0x002A385C`–`0x002A3894` (길이 `56` bytes)
- VA: `0x00000001402A385C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068784`
- 디코드: `16`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A3869` → [MiUnlockLoaderEntry](MiUnlockLoaderEntry_function_002A3E28.md) (function, `0x002A3E28`)
- `0x002A387E` → [MiReleaseLoadLock](MiReleaseLoadLock_function_002A3CD0.md) (function, `0x002A3CD0`)

### Direct callers
- [LdrpKrnGetDataTableEntry](../45/LdrpKrnGetDataTableEntry_function_004563B4.md) at `0x004563D8`
- [MmVerifyCallbackFunctionCheckFlags](../4F/MmVerifyCallbackFunctionCheckFlags_function_004F7360.md) at `0x004F7391`
- [MmProtectDriverSection](../67/MmProtectDriverSection_function_00670A80.md) at `0x00670C49`
- [MmWriteSystemImageTracepoint](../68/MmWriteSystemImageTracepoint_function_00684150.md) at `0x00684264`
- [MmDiscardDriverSection](../../init/C6/MmDiscardDriverSection_function_00C6C8D0.md) at `0x00C6C962`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A385C  48 83 EC 28                     sub rsp, 0x28
002A3860  F7 DA                           neg edx
002A3862  1B D2                           sbb edx, edx
002A3864  F7 D2                           not edx
002A3866  83 E2 02                        and edx, 2
002A3869  E8 BA 05 00 00                  call 0x1402a3e28
002A386E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002A3877  48 85 C9                        test rcx, rcx
002A387A  74 0D                           je 0x1402a3889
002A387C  33 D2                           xor edx, edx
002A387E  E8 4D 04 00 00                  call 0x1402a3cd0
002A3883  48 83 C4 28                     add rsp, 0x28
002A3887  C3                              ret
002A3888  CC                              int3
002A3889  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002A3892  EB E8                           jmp 0x1402a387c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlockLoadedDataTableEntry(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (unsigned int)(-(a2));
    a2 = (unsigned int)(~(a2));
    a2 = (unsigned int)((a2) & (2));
    result = MiUnlockLoaderEntry(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) == 0) goto loc_002A3889;
loc_002A387C:
    a2 = 0;
    result = MiReleaseLoadLock(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_002A3889:
    goto loc_002A387C;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlockLoadedDataTableEntry(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = (uint32_t)(-(Arg2));
    Arg2 = (uint32_t)(~(Arg2));
    Arg2 = (uint32_t)((Arg2) & (2));
    result = MiUnlockLoaderEntry(Arg1, Arg2, a3, a4);
    if (*(uint64_t *)(gs_base + (0 + 0x188)) == 0) goto loc_002A3889;
loc_002A387C:
    Arg2 = 0;
    result = MiReleaseLoadLock(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_002A3889:
    goto loc_002A387C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A385C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A385C[BB_002A385C]
  bb_002A387C[BB_002A387C]
  bb_002A3888[BB_002A3888]
  bb_002A3889[BB_002A3889]
  bb_002A385C -->|branch| bb_002A3889
  bb_002A385C -->|fallthrough| bb_002A387C
  bb_002A3888 -->|flow| bb_002A3889
  bb_002A3889 -->|branch| bb_002A387C
```
