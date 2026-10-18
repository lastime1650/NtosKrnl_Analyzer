# KiSrcuCheckQuiescent

- RVA: `0x0043C700`–`0x0043C71A` (길이 `26` bytes)
- VA: `0x000000014043C700`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A4558`
- 디코드: `9`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiSrcuNotifyGracePeriodStartedOnCpu](../5C/KiSrcuNotifyGracePeriodStartedOnCpu_function_005C2788.md) at `0x005C2849`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0043C711` → [sub_0043C71A](Unknown_function_0043C71A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0043C700  40 53                           push rbx
0043C702  48 83 EC 20                     sub rsp, 0x20
0043C706  48 83 B9 F8 38 00 00 00         cmp qword ptr [rcx + 0x38f8], 0
0043C70E  48 8B D9                        mov rbx, rcx
0043C711  75 07                           jne 0x14043c71a
0043C713  48 83 C4 20                     add rsp, 0x20
0043C717  5B                              pop rbx
0043C718  C3                              ret
0043C719  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiSrcuCheckQuiescent(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_rsp = (v_rsp) + (32);
    return;
}
```

## 5. (Beta) C Style

```c
void KiSrcuCheckQuiescent(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_rsp = (local_rsp) + (32);
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38F8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043C700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043C700[BB_0043C700]
  bb_0043C713[BB_0043C713]
  bb_0043C719[BB_0043C719]
  bb_0043C700 -->|fallthrough| bb_0043C713
```
