# sub_006DD98E

- RVA: `0x006DD98E`–`0x006DD9A0` (길이 `18` bytes)
- VA: `0x00000001406DD98E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F990`
- 디코드: `6`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DD99B` → [HalpInterruptApplyOverrides + 0x73](../2D/HalpInterruptApplyOverrides_function_002D2CE0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DD98E  48 85 F6                        test rsi, rsi
006DD991  74 05                           je 0x1406dd998
006DD993  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
006DD996  89 06                           mov dword ptr [rsi], eax
006DD998  40 B7 01                        mov dil, 1
006DD99B  E9 B3 53 BF FF                  jmp 0x1402d2d53
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DD98E(__int64 a1, __int64 a2)
{
    __int64 result;

    if (v_rsi != 0) {
        result = *(unsigned int *)(a2 + 32);
        *(unsigned int *)(v_rsi) = (unsigned int)(result);
    }
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DD98E(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (local_rsi != 0) {
        result = *(uint32_t *)(arg2 + 0x20);
        *(uint32_t *)(local_rsi) = (uint32_t)(result);
    }
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DD98E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DD98E[BB_006DD98E]
  bb_006DD993[BB_006DD993]
  bb_006DD998[BB_006DD998]
  bb_006DD98E -->|branch| bb_006DD998
  bb_006DD98E -->|fallthrough| bb_006DD993
  bb_006DD993 -->|flow| bb_006DD998
```
