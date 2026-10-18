# VfShutdownScheduleWatchdog

- RVA: `0x00615F18`–`0x00615F31` (길이 `25` bytes)
- VA: `0x0000000140615F18`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00615F26` → [ViShutdownScheduleWatchdog](../../pagevrfy/BA/ViShutdownScheduleWatchdog_function_00BA4DF0.md) (function, `0x00BA4DF0`)

### Direct callers
- [PopGracefulShutdown](../../pagelk/B6/PopGracefulShutdown_function_00B6BEC8.md) at `0x00B6BF2C`

### Static image references
- `0x00615F1C` → RVA `0x00E681A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00615F26` → [ViShutdownScheduleWatchdog](../../pagevrfy/BA/ViShutdownScheduleWatchdog_function_00BA4DF0.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00615F18  48 83 EC 28                     sub rsp, 0x28
00615F1C  8B 05 7E 22 85 00               mov eax, dword ptr [rip + 0x85227e]
00615F22  A8 10                           test al, 0x10
00615F24  74 05                           je 0x140615f2b
00615F26  E8 C5 EE 58 00                  call 0x140ba4df0
00615F2B  48 83 C4 28                     add rsp, 0x28
00615F2F  C3                              ret
00615F30  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfShutdownScheduleWatchdog(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(*(unsigned int *)(v_rip + 8725118));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 8725118)))) & (16)) != 0) {
        result = ViShutdownScheduleWatchdog(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void VfShutdownScheduleWatchdog(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x85227E));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x85227E)))) & (16)) != 0) {
        result = ViShutdownScheduleWatchdog(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00615F18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00615F18[BB_00615F18]
  bb_00615F26[BB_00615F26]
  bb_00615F2B[BB_00615F2B]
  bb_00615F30[BB_00615F30]
  bb_00615F18 -->|branch| bb_00615F2B
  bb_00615F18 -->|fallthrough| bb_00615F26
  bb_00615F26 -->|flow| bb_00615F2B
```
