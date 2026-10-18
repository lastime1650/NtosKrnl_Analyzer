# PopIsMostRecentWakeAttended

- RVA: `0x00B7D6C8`–`0x00B7D6EE` (길이 `38` bytes)
- VA: `0x0000000140B7D6C8`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B7D6D0` → [PopGetMostRecentWakeInfo](../../text/4B/PopGetMostRecentWakeInfo_function_004BE4F8.md) (function, `0x004BE4F8`)
- `0x00B7D6E0` → [PopWakeInfoDereference](../../text/4C/PopWakeInfoDereference_function_004C74AC.md) (function, `0x004C74AC`)

### Direct callers
- [PopPowerAggregatorHandleSystemTransitionEndIntent](../../page/76/PopPowerAggregatorHandleSystemTransitionEndIntent_function_00764B30.md) at `0x00764B80`
- [PopTransitionSystemPowerStateEx](PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7FAC1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B7D6D0` → [PopGetMostRecentWakeInfo](../../text/4B/PopGetMostRecentWakeInfo_function_004BE4F8.md) (`PAGELK` → `.text`)
  - `0x00B7D6E0` → [PopWakeInfoDereference](../../text/4C/PopWakeInfoDereference_function_004C74AC.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B7D6C8  40 53                           push rbx
00B7D6CA  48 83 EC 20                     sub rsp, 0x20
00B7D6CE  B3 01                           mov bl, 1
00B7D6D0  E8 23 0E 94 FF                  call 0x1404be4f8
00B7D6D5  48 85 C0                        test rax, rax
00B7D6D8  74 0B                           je 0x140b7d6e5
00B7D6DA  8A 58 50                        mov bl, byte ptr [rax + 0x50]
00B7D6DD  48 8B C8                        mov rcx, rax
00B7D6E0  E8 C7 9D 94 FF                  call 0x1404c74ac
00B7D6E5  8A C3                           mov al, bl
00B7D6E7  48 83 C4 20                     add rsp, 0x20
00B7D6EB  5B                              pop rbx
00B7D6EC  C3                              ret
00B7D6ED  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopIsMostRecentWakeAttended(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PopGetMostRecentWakeInfo(a1, a2, a3, a4);
    v_rbx = 1;
    if (result != 0) {
        v_rbx = *(unsigned __int8 *)(result + 80);
        a1 = result;
        result = PopWakeInfoDereference(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rbx);
}
```

## 5. (Beta) C Style

```c
void PopIsMostRecentWakeAttended(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PopGetMostRecentWakeInfo(a1, a2, a3, a4);
    local_rbx = 1;
    if (result != 0) {
        local_rbx = *(uint8_t *)(result + 0x50);
        a1 = result;
        result = PopWakeInfoDereference(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rbx);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B7D6C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B7D6C8[BB_00B7D6C8]
  bb_00B7D6DA[BB_00B7D6DA]
  bb_00B7D6E5[BB_00B7D6E5]
  bb_00B7D6ED[BB_00B7D6ED]
  bb_00B7D6C8 -->|branch| bb_00B7D6E5
  bb_00B7D6C8 -->|fallthrough| bb_00B7D6DA
  bb_00B7D6DA -->|flow| bb_00B7D6E5
```
