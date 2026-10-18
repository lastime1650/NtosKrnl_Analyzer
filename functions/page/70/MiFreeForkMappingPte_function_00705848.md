# MiFreeForkMappingPte

- RVA: `0x00705848`–`0x00705877` (길이 `47` bytes)
- VA: `0x0000000140705848`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00705858` → [MiUnmapSinglePage](../../text/4D/MiUnmapSinglePage_function_004D4B00.md) (function, `0x004D4B00`)
- `0x0070586C` → [MiDeleteUltraThreadContext](../../text/32/MiDeleteUltraThreadContext_function_00322C90.md) (function, `0x00322C90`)

### Direct callers
- [MiCloneVads](../../text/22/MiCloneVads_function_0022DC1C.md) at `0x0022E1B3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00705858` → [MiUnmapSinglePage](../../text/4D/MiUnmapSinglePage_function_004D4B00.md) (`PAGE` → `.text`)
  - `0x0070586C` → [MiDeleteUltraThreadContext](../../text/32/MiDeleteUltraThreadContext_function_00322C90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00705848  48 83 EC 28                     sub rsp, 0x28
0070584C  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00705850  48 85 C0                        test rax, rax
00705853  74 0A                           je 0x14070585f
00705855  48 8B C8                        mov rcx, rax
00705858  E8 A3 F2 DC FF                  call 0x1404d4b00
0070585D  EB 12                           jmp 0x140705871
0070585F  80 B9 C0 00 00 00 00            cmp byte ptr [rcx + 0xc0], 0
00705866  74 09                           je 0x140705871
00705868  48 83 C1 48                     add rcx, 0x48
0070586C  E8 1F D4 C1 FF                  call 0x140322c90
00705871  48 83 C4 28                     add rsp, 0x28
00705875  C3                              ret
00705876  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreeForkMappingPte(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + 56) == 0) goto loc_0070585F;
    result = MiUnmapSinglePage(*(unsigned __int64 *)(a1 + 56), a2, a3, a4);
    goto loc_00705871;
loc_0070585F:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56) + 192)) != 0) {
        a1 = (*(unsigned __int64 *)(a1 + 56)) + (72);
        result = MiDeleteUltraThreadContext(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiFreeForkMappingPte(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + 0x38) == 0) goto loc_0070585F;
    result = MiUnmapSinglePage(*(uint64_t *)(arg1 + 0x38), a2, a3, a4);
    goto loc_00705871;
loc_0070585F:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x38) + 0xC0)) != 0) {
        Arg1 = (*(uint64_t *)(arg1 + 0x38)) + (72);
        result = MiDeleteUltraThreadContext(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00705848&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00705848[BB_00705848]
  bb_00705855[BB_00705855]
  bb_0070585F[BB_0070585F]
  bb_00705868[BB_00705868]
  bb_00705871[BB_00705871]
  bb_00705876[BB_00705876]
  bb_00705848 -->|branch| bb_0070585F
  bb_00705848 -->|fallthrough| bb_00705855
  bb_00705855 -->|branch| bb_00705871
  bb_0070585F -->|branch| bb_00705871
  bb_0070585F -->|fallthrough| bb_00705868
  bb_00705868 -->|flow| bb_00705871
```
