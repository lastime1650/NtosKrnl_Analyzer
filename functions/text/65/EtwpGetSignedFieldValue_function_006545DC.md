# EtwpGetSignedFieldValue

- RVA: `0x006545DC`–`0x0065462B` (길이 `79` bytes)
- VA: `0x00000001406545DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000D3FDC`
- 디코드: `28`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_006EAEDE](../6E/Unknown_function_006EAEDE.md) at `0x006EAF07`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006545DC  48 83 EC 38                     sub rsp, 0x38
006545E0  41 B1 01                        mov r9b, 1
006545E3  83 EA 01                        sub edx, 1
006545E6  74 29                           je 0x140654611
006545E8  83 EA 01                        sub edx, 1
006545EB  74 1E                           je 0x14065460b
006545ED  83 EA 02                        sub edx, 2
006545F0  74 14                           je 0x140654606
006545F2  83 FA 04                        cmp edx, 4
006545F5  74 0A                           je 0x140654601
006545F7  45 32 C9                        xor r9b, r9b
006545FA  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
006545FF  EB 17                           jmp 0x140654618
00654601  48 8B 01                        mov rax, qword ptr [rcx]
00654604  EB 0F                           jmp 0x140654615
00654606  48 63 01                        movsxd rax, dword ptr [rcx]
00654609  EB 0A                           jmp 0x140654615
0065460B  48 0F BF 01                     movsx rax, word ptr [rcx]
0065460F  EB 04                           jmp 0x140654615
00654611  48 0F BE 01                     movsx rax, byte ptr [rcx]
00654615  49 89 00                        mov qword ptr [r8], rax
00654618  EB 08                           jmp 0x140654622
0065461A  45 32 C9                        xor r9b, r9b
0065461D  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
00654622  41 8A C1                        mov al, r9b
00654625  48 83 C4 38                     add rsp, 0x38
00654629  C3                              ret
0065462A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpGetSignedFieldValue(__int64 a1, int a2, __int64 a3)
{
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00654611;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0065460B;
    a2 = (unsigned int)((a2) - (2));
    if (condition_is_equal) goto loc_00654606;
    if (a2 == 4) goto loc_00654601;
    a4 = 0;
    v_stack_m18 = 0;
    goto loc_00654618;
loc_00654601:
    goto loc_00654615;
loc_00654606:
    goto loc_00654615;
loc_0065460B:
    goto loc_00654615;
loc_00654611:
loc_00654615:
    *(unsigned __int64 *)(a3) = (__int8)(*(unsigned __int8 *)(a1));
loc_00654618:
    goto loc_00654622;
loc_00654622:
    v_rsp = (v_rsp) + (56);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpGetSignedFieldValue(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t local_rsp;
    uint8_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00654611;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0065460B;
    Arg2 = (uint32_t)((Arg2) - (2));
    if (condition_is_equal) goto loc_00654606;
    if (Arg2 == 4) goto loc_00654601;
    a4 = 0;
    v_stack_m18 = 0;
    goto loc_00654618;
loc_00654601:
    goto loc_00654615;
loc_00654606:
    goto loc_00654615;
loc_0065460B:
    goto loc_00654615;
loc_00654611:
loc_00654615:
    *(uint64_t *)(arg3) = (int8_t)(*(uint8_t *)(arg1));
loc_00654618:
    goto loc_00654622;
loc_00654622:
    local_rsp = (local_rsp) + (56);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006545DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006545DC[BB_006545DC]
  bb_006545E8[BB_006545E8]
  bb_006545ED[BB_006545ED]
  bb_006545F2[BB_006545F2]
  bb_006545F7[BB_006545F7]
  bb_00654601[BB_00654601]
  bb_00654606[BB_00654606]
  bb_0065460B[BB_0065460B]
  bb_00654611[BB_00654611]
  bb_00654615[BB_00654615]
  bb_00654618[BB_00654618]
  bb_0065461A[BB_0065461A]
  bb_00654622[BB_00654622]
  bb_0065462A[BB_0065462A]
  bb_006545DC -->|branch| bb_00654611
  bb_006545DC -->|fallthrough| bb_006545E8
  bb_006545E8 -->|branch| bb_0065460B
  bb_006545E8 -->|fallthrough| bb_006545ED
  bb_006545ED -->|branch| bb_00654606
  bb_006545ED -->|fallthrough| bb_006545F2
  bb_006545F2 -->|branch| bb_00654601
  bb_006545F2 -->|fallthrough| bb_006545F7
  bb_006545F7 -->|branch| bb_00654618
  bb_00654601 -->|branch| bb_00654615
  bb_00654606 -->|branch| bb_00654615
  bb_0065460B -->|branch| bb_00654615
  bb_00654611 -->|flow| bb_00654615
  bb_00654615 -->|flow| bb_00654618
  bb_00654618 -->|branch| bb_00654622
  bb_0065461A -->|flow| bb_00654622
```
