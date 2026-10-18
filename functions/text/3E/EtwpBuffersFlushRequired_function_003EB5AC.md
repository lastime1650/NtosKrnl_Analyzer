# EtwpBuffersFlushRequired

- RVA: `0x003EB5AC`–`0x003EB5E4` (길이 `56` bytes)
- VA: `0x00000001403EB5AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000848A4`
- 디코드: `16`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003EB5C4` → [EtwpQueryUsedProcessorCount](EtwpQueryUsedProcessorCount_function_003EB940.md) (function, `0x003EB940`)

### Direct callers
- [EtwpReserveTraceBuffer](../2F/EtwpReserveTraceBuffer_function_002FC8C0.md) at `0x002FCC50`
- [EtwInitialize](../../page/7B/EtwInitialize_function_007B4D40.md) at `0x007B4E1D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EB5AC  48 83 EC 28                     sub rsp, 0x28
003EB5B0  83 B9 D4 00 00 00 00            cmp dword ptr [rcx + 0xd4], 0
003EB5B7  48 8B D1                        mov rdx, rcx
003EB5BA  75 08                           jne 0x1403eb5c4
003EB5BC  B0 01                           mov al, 1
003EB5BE  48 83 C4 28                     add rsp, 0x28
003EB5C2  C3                              ret
003EB5C3  CC                              int3
003EB5C4  E8 77 03 00 00                  call 0x1403eb940
003EB5C9  8B 89 E8 00 00 00               mov ecx, dword ptr [rcx + 0xe8]
003EB5CF  2B C8                           sub ecx, eax
003EB5D1  8B 82 E4 00 00 00               mov eax, dword ptr [rdx + 0xe4]
003EB5D7  2B C8                           sub ecx, eax
003EB5D9  3B 8A D4 00 00 00               cmp ecx, dword ptr [rdx + 0xd4]
003EB5DF  0F 9D C0                        setge al
003EB5E2  EB DA                           jmp 0x1403eb5be
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpBuffersFlushRequired(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(a1 + 212)) != 0) goto loc_003EB5C4;
loc_003EB5BE:
    v_rsp = (v_rsp) + (40);
    return 1;
loc_003EB5C4:
    result = EtwpQueryUsedProcessorCount(a1, a1, a3, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 232))) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)))));
    result = (((unsigned int)(a1)) >= (*(unsigned int *)(a1 + 212))) ? 1 : 0;
    goto loc_003EB5BE;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpBuffersFlushRequired(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(arg1 + 0xD4)) != 0) goto loc_003EB5C4;
loc_003EB5BE:
    local_rsp = (local_rsp) + (40);
    return 1;
loc_003EB5C4:
    result = EtwpQueryUsedProcessorCount(Arg1, Arg1, a3, a4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xE8))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)))));
    result = (((uint32_t)(Arg1)) >= (*(uint32_t *)(arg1 + 0xD4))) ? 1 : 0;
    goto loc_003EB5BE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EB5AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EB5AC[BB_003EB5AC]
  bb_003EB5BC[BB_003EB5BC]
  bb_003EB5BE[BB_003EB5BE]
  bb_003EB5C3[BB_003EB5C3]
  bb_003EB5C4[BB_003EB5C4]
  bb_003EB5AC -->|branch| bb_003EB5C4
  bb_003EB5AC -->|fallthrough| bb_003EB5BC
  bb_003EB5BC -->|flow| bb_003EB5BE
  bb_003EB5C3 -->|flow| bb_003EB5C4
  bb_003EB5C4 -->|branch| bb_003EB5BE
```
