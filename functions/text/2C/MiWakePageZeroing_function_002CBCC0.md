# MiWakePageZeroing

- RVA: `0x002CBCC0`–`0x002CBCDC` (길이 `28` bytes)
- VA: `0x00000001402CBCC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F34C`
- 디코드: `8`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiInsertHugeRangeInList](../43/MiInsertHugeRangeInList_function_004371E8.md) at `0x00437488`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002CBCD6` → [sub_002CBDED](Unknown_function_002CBDED.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002CBCC0  40 56                           push rsi
002CBCC2  41 55                           push r13
002CBCC4  48 83 EC 38                     sub rsp, 0x38
002CBCC8  8B 81 30 42 00 00               mov eax, dword ptr [rcx + 0x4230]
002CBCCE  45 8B E8                        mov r13d, r8d
002CBCD1  48 8B F2                        mov rsi, rdx
002CBCD4  85 C0                           test eax, eax
002CBCD6  0F 85 11 01 00 00               jne 0x1402cbded
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWakePageZeroing(__int64 a1, __int64 a2, int a3)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
}
```

## 5. (Beta) C Style

```c
int64_t MiWakePageZeroing(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4230` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CBCC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002CBCC0[BB_002CBCC0]
```
