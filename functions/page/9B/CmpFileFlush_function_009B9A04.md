# CmpFileFlush

- RVA: `0x009B9A04`–`0x009B9A26` (길이 `34` bytes)
- VA: `0x00000001409B9A04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009B9A17` → [CmpDoFileFlush](../../text/49/CmpDoFileFlush_function_0049BFE8.md) (function, `0x0049BFE8`)

### Direct callers
- [CmpSaveKeyByFileCopy](../7D/CmpSaveKeyByFileCopy_function_007DEFC0.md) at `0x007DF11D`
- [CmpSaveKeyByFileCopy](../7D/CmpSaveKeyByFileCopy_function_007DEFC0.md) at `0x007DF183`
- [CmpFileFlushAndPurge](CmpFileFlushAndPurge_function_009B2BAC.md) at `0x009B2D38`
- [HvLoadHive](HvLoadHive_function_009B8138.md) at `0x009B842C`
- [HvWriteExternal](../A8/HvWriteExternal_function_00A83C20.md) at `0x00A83E66`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009B9A17` → [CmpDoFileFlush](../../text/49/CmpDoFileFlush_function_0049BFE8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009B9A04  48 83 EC 28                     sub rsp, 0x28
009B9A08  8B C2                           mov eax, edx
009B9A0A  48 8B 8C C1 08 06 00 00         mov rcx, qword ptr [rcx + rax*8 + 0x608]
009B9A12  48 85 C9                        test rcx, rcx
009B9A15  74 0B                           je 0x1409b9a22
009B9A17  E8 CC 25 AE FF                  call 0x14049bfe8
009B9A1C  48 83 C4 28                     add rsp, 0x28
009B9A20  C3                              ret
009B9A21  CC                              int3
009B9A22  33 C0                           xor eax, eax
009B9A24  EB F6                           jmp 0x1409b9a1c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFileFlush(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + (unsigned int)(a2) * 8 + 1544) == 0) goto loc_009B9A22;
    result = CmpDoFileFlush(*(unsigned __int64 *)(a1 + (unsigned int)(a2) * 8 + 1544), a2, a3, a4);
loc_009B9A1C:
    v_rsp = (v_rsp) + (40);
    return result;
loc_009B9A22:
    result = 0;
    goto loc_009B9A1C;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFileFlush(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + (uint32_t)(Arg2) * 8 + 0x608) == 0) goto loc_009B9A22;
    result = CmpDoFileFlush(*(uint64_t *)(arg1 + (uint32_t)(Arg2) * 8 + 0x608), Arg2, a3, a4);
loc_009B9A1C:
    local_rsp = (local_rsp) + (40);
    return result;
loc_009B9A22:
    result = 0;
    goto loc_009B9A1C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x608 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B9A04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009B9A04[BB_009B9A04]
  bb_009B9A17[BB_009B9A17]
  bb_009B9A1C[BB_009B9A1C]
  bb_009B9A21[BB_009B9A21]
  bb_009B9A22[BB_009B9A22]
  bb_009B9A04 -->|branch| bb_009B9A22
  bb_009B9A04 -->|fallthrough| bb_009B9A17
  bb_009B9A17 -->|flow| bb_009B9A1C
  bb_009B9A21 -->|flow| bb_009B9A22
  bb_009B9A22 -->|branch| bb_009B9A1C
```
