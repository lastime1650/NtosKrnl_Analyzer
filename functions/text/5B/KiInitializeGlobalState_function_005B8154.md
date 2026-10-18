# KiInitializeGlobalState

- RVA: `0x005B8154`–`0x005B8172` (길이 `30` bytes)
- VA: `0x00000001405B8154`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiInitializeBootStructures](../../pagelk/B6/KiInitializeBootStructures_function_00B68530.md) at `0x00B685AB`

### Static image references
- `0x005B8154` → RVA `0x00F22FE0` (`.data`; read)
- `0x005B815B` → RVA `0x00F231B0` (`.data`; write)
- `0x005B8162` → RVA `0x00F22FE4` (`.data`; read)
- `0x005B8169` → RVA `0x00F231B8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B8154  48 8D 05 85 AE 96 00            lea rax, [rip + 0x96ae85]
005B815B  48 89 05 4E B0 96 00            mov qword ptr [rip + 0x96b04e], rax
005B8162  48 8D 05 7B AE 96 00            lea rax, [rip + 0x96ae7b]
005B8169  48 89 05 48 B0 96 00            mov qword ptr [rip + 0x96b048], rax
005B8170  C3                              ret
005B8171  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiInitializeGlobalState(void)
{
    *(unsigned __int64 *)(v_rip + 9875534) = v_rip + 9875077;
    *(unsigned __int64 *)(v_rip + 9875528) = v_rip + 9875067;
    return v_rip + 9875067;
}
```

## 5. (Beta) C Style

```c
void KiInitializeGlobalState(void)
{
    *(uint64_t *)(v_rip + 0x96B04E) = v_rip + 9875077;
    *(uint64_t *)(v_rip + 0x96B048) = v_rip + 9875067;
    return v_rip + 9875067;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B8154&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B8154[BB_005B8154]
  bb_005B8171[BB_005B8171]
```
