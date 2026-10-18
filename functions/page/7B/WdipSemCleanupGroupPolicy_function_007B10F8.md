# WdipSemCleanupGroupPolicy

- RVA: `0x007B10F8`–`0x007B111D` (길이 `37` bytes)
- VA: `0x00000001407B10F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007B110A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [WdipSemCleanStart](../7A/WdipSemCleanStart_function_007AF590.md) at `0x007AF5D4`
- [WdipSemLoadGroupPolicy](WdipSemLoadGroupPolicy_function_007B1124.md) at `0x007B1198`

### Static image references
- `0x007B10FC` → RVA `0x00F01E10` (`.data`; read)
- `0x007B110F` → RVA `0x00F01E10` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007B110A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B10F8  48 83 EC 28                     sub rsp, 0x28
007B10FC  48 8B 0D 0D 0D 75 00            mov rcx, qword ptr [rip + 0x750d0d]
007B1103  48 85 C9                        test rcx, rcx
007B1106  74 0F                           je 0x1407b1117
007B1108  33 D2                           xor edx, edx
007B110A  E8 61 17 3D 00                  call 0x140b82870
007B110F  48 83 25 F9 0C 75 00 00         and qword ptr [rip + 0x750cf9], 0
007B1117  48 83 C4 28                     add rsp, 0x28
007B111B  C3                              ret
007B111C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WdipSemCleanupGroupPolicy(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 7671053) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 7671053), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WdipSemCleanupGroupPolicy(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x750D0D) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x750D0D), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B10F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B10F8[BB_007B10F8]
  bb_007B1108[BB_007B1108]
  bb_007B1117[BB_007B1117]
  bb_007B111C[BB_007B111C]
  bb_007B10F8 -->|branch| bb_007B1117
  bb_007B10F8 -->|fallthrough| bb_007B1108
  bb_007B1108 -->|flow| bb_007B1117
```
