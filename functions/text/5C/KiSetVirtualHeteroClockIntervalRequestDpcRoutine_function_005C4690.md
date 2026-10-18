# KiSetVirtualHeteroClockIntervalRequestDpcRoutine

- RVA: `0x005C4690`–`0x005C46AA` (길이 `26` bytes)
- VA: `0x00000001405C4690`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005C469F` → [KiSetVirtualHeteroClockIntervalRequest](KiSetVirtualHeteroClockIntervalRequest_function_005C45F8.md) (function, `0x005C45F8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005C4694` → RVA `0x00E66894` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C4690  48 83 EC 28                     sub rsp, 0x28
005C4694  8B 05 FA 21 8A 00               mov eax, dword ptr [rip + 0x8a21fa]
005C469A  85 C0                           test eax, eax
005C469C  0F 94 C1                        sete cl
005C469F  E8 54 FF FF FF                  call 0x1405c45f8
005C46A4  48 83 C4 28                     add rsp, 0x28
005C46A8  C3                              ret
005C46A9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSetVirtualHeteroClockIntervalRequestDpcRoutine(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9052666))) == 0) ? 1 : 0;
    result = KiSetVirtualHeteroClockIntervalRequest(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void KiSetVirtualHeteroClockIntervalRequestDpcRoutine(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    a1 = ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8A21FA))) == 0) ? 1 : 0;
    result = KiSetVirtualHeteroClockIntervalRequest(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C4690&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C4690[BB_005C4690]
  bb_005C46A9[BB_005C46A9]
```
