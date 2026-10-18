# EtwDereferenceSpinLockCounters

- RVA: `0x007BC2E8`–`0x007BC33D` (길이 `85` bytes)
- VA: `0x00000001407BC2E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `20`개 명령, `85/85` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007BC301` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x007BC324` → [EtwpUpdateGlobalGroupMasks](../A4/EtwpUpdateGlobalGroupMasks_function_00A4F55C.md) (function, `0x00A4F55C`)
- `0x007BC332` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (function, `0x00396810`)

### Direct callers
- [KiSynchCounterSetCallback](../A5/KiSynchCounterSetCallback_function_00A5F5B0.md) at `0x00A5F6E5`
- [KiSynchNumaCounterSetCallback](../A7/KiSynchNumaCounterSetCallback_function_00A77BE0.md) at `0x00A7819B`

### Static image references
- `0x007BC2F2` → RVA `0x00EFF7E0` (`.data`; read)
- `0x007BC306` → RVA `0x00FD80D4` (`PAGEDATA`; read/write)
- `0x007BC30F` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007BC301` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x007BC332` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007BC2E8  48 83 EC 38                     sub rsp, 0x38
007BC2EC  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007BC2F2  48 8D 0D E7 34 74 00            lea rcx, [rip + 0x7434e7]
007BC2F9  45 33 C9                        xor r9d, r9d
007BC2FC  45 33 C0                        xor r8d, r8d
007BC2FF  33 D2                           xor edx, edx
007BC301  E8 AA 23 A5 FF                  call 0x14020e6b0
007BC306  83 2D C7 BD 81 00 01            sub dword ptr [rip + 0x81bdc7], 1
007BC30D  75 1A                           jne 0x1407bc329
007BC30F  48 8B 0D 92 A7 80 00            mov rcx, qword ptr [rip + 0x80a792]
007BC316  33 D2                           xor edx, edx
007BC318  0F BA B1 D0 12 00 00 15         btr dword ptr [rcx + 0x12d0], 0x15
007BC320  44 8D 42 08                     lea r8d, [rdx + 8]
007BC324  E8 33 32 29 00                  call 0x140a4f55c
007BC329  33 D2                           xor edx, edx
007BC32B  48 8D 0D AE 34 74 00            lea rcx, [rip + 0x7434ae]
007BC332  E8 D9 A4 BD FF                  call 0x140396810
007BC337  48 83 C4 38                     add rsp, 0x38
007BC33B  C3                              ret
007BC33C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwDereferenceSpinLockCounters(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 7615719, a2, a3, a4);
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rip + 8431506);
        a2 = 0;
        a3 = a2 + 8;
        result = EtwpUpdateGlobalGroupMasks(a1, a2, a3, a4);
    }
    a2 = 0;
    result = KeReleaseMutex(v_rip + 7615662, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwDereferenceSpinLockCounters(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 7615719, Arg2, Arg3, Arg4);
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(v_rip + 0x80A792);
        Arg2 = 0;
        Arg3 = Arg2 + 8;
        result = EtwpUpdateGlobalGroupMasks(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = KeReleaseMutex(v_rip + 7615662, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007BC2E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007BC2E8[BB_007BC2E8]
  bb_007BC30F[BB_007BC30F]
  bb_007BC329[BB_007BC329]
  bb_007BC33C[BB_007BC33C]
  bb_007BC2E8 -->|branch| bb_007BC329
  bb_007BC2E8 -->|fallthrough| bb_007BC30F
  bb_007BC30F -->|flow| bb_007BC329
```
