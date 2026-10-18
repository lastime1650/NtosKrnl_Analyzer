# RtlHandleBMI2Override

- RVA: `0x00B72340`–`0x00B72351` (길이 `17` bytes)
- VA: `0x0000000140B72340`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `17/17` bytes 표시
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
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B72340  80 79 04 01                     cmp byte ptr [rcx + 4], 1
00B72344  75 09                           jne 0x140b7234f
00B72346  83 79 08 19                     cmp dword ptr [rcx + 8], 0x19
00B7234A  73 03                           jae 0x140b7234f
00B7234C  83 22 00                        and dword ptr [rdx], 0
00B7234F  C3                              ret
00B72350  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall RtlHandleBMI2Override(__int64 a1, __int64 a2)
{
    if ((*(unsigned __int8 *)(a1 + 4)) != 1) goto loc_00B7234F;
    if ((*(unsigned int *)(a1 + 8)) < 25) {
    }
    return;
}
```

## 5. (Beta) C Style

```c
void RtlHandleBMI2Override(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    if ((*(uint8_t *)(arg1 + 0x4)) != 1) goto loc_00B7234F;
    if ((*(uint32_t *)(arg1 + 0x8)) < 25) {
    }
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B72340&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B72340[BB_00B72340]
  bb_00B72346[BB_00B72346]
  bb_00B7234C[BB_00B7234C]
  bb_00B7234F[BB_00B7234F]
  bb_00B72350[BB_00B72350]
  bb_00B72340 -->|branch| bb_00B7234F
  bb_00B72340 -->|fallthrough| bb_00B72346
  bb_00B72346 -->|branch| bb_00B7234F
  bb_00B72346 -->|fallthrough| bb_00B7234C
  bb_00B7234C -->|flow| bb_00B7234F
```
