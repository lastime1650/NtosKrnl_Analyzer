# KeQueryAuxiliaryCounterFrequency

- RVA: `0x005B1990`–`0x005B19A6` (길이 `22` bytes)
- VA: `0x00000001405B1990`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005B199B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [NtQueryAuxiliaryCounterFrequency](../../page/7D/NtQueryAuxiliaryCounterFrequency_function_007D2190.md) at `0x007D21C5`
- [NtQueryAuxiliaryCounterFrequency](../../page/7D/NtQueryAuxiliaryCounterFrequency_function_007D2190.md) at `0x007D21DC`

### Static image references
- `0x005B1994` → RVA `0x00E00B90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B1990  48 83 EC 28                     sub rsp, 0x28
005B1994  48 8B 05 F5 F1 84 00            mov rax, qword ptr [rip + 0x84f1f5]
005B199B  E8 30 91 10 00                  call 0x1406baad0
005B19A0  48 83 C4 28                     add rsp, 0x28
005B19A4  C3                              ret
005B19A5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeQueryAuxiliaryCounterFrequency(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void KeQueryAuxiliaryCounterFrequency(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = guard_dispatch_icall(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B1990&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B1990[BB_005B1990]
  bb_005B19A5[BB_005B19A5]
```
