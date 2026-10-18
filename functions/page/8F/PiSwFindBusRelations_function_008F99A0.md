# PiSwFindBusRelations

- RVA: `0x008F99A0`–`0x008F99DB` (길이 `59` bytes)
- VA: `0x00000001408F99A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087C64`
- 디코드: `17`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008F99CC` → [RtlLookupElementGenericTableAvl](../../text/3F/RtlLookupElementGenericTableAvl_function_003FEFB0.md) (function, `0x003FEFB0`)

### Direct callers
- [PiSwFindChildren](PiSwFindChildren_function_008F8ED0.md) at `0x008F8ED4`
- [PiSwCloseDescendants](../A9/PiSwCloseDescendants_function_00A9E564.md) at `0x00A9E57E`

### Static image references
- `0x008F99C0` → RVA `0x00F8ABA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008F99CC` → [RtlLookupElementGenericTableAvl](../../text/3F/RtlLookupElementGenericTableAvl_function_003FEFB0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F99A0  48 8B C4                        mov rax, rsp
008F99A3  48 83 EC 48                     sub rsp, 0x48
008F99A7  48 83 79 08 00                  cmp qword ptr [rcx + 8], 0
008F99AC  0F 57 C0                        xorps xmm0, xmm0
008F99AF  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
008F99B3  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
008F99B7  74 1E                           je 0x1408f99d7
008F99B9  0F 10 01                        movups xmm0, xmmword ptr [rcx]
008F99BC  48 8D 50 D8                     lea rdx, [rax - 0x28]
008F99C0  48 8D 0D D9 11 69 00            lea rcx, [rip + 0x6911d9]
008F99C7  F3 0F 7F 40 D8                  movdqu xmmword ptr [rax - 0x28], xmm0
008F99CC  E8 DF 55 B0 FF                  call 0x1403fefb0
008F99D1  48 83 C4 48                     add rsp, 0x48
008F99D5  C3                              ret
008F99D6  CC                              int3
008F99D7  33 C0                           xor eax, eax
008F99D9  EB F6                           jmp 0x1408f99d1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwFindBusRelations(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    if ((*(unsigned __int64 *)(a1 + 8)) == 0) goto loc_008F99D7;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = RtlLookupElementGenericTableAvl(v_rip + 6885849, v_rsp - 40, a3, a4);
loc_008F99D1:
    v_rsp = (v_rsp) + (72);
    return result;
loc_008F99D7:
    result = 0;
    goto loc_008F99D1;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwFindBusRelations(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    if ((*(uint64_t *)(arg1 + 0x8)) == 0) goto loc_008F99D7;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = RtlLookupElementGenericTableAvl(v_rip + 6885849, local_rsp - 40, a3, a4);
loc_008F99D1:
    local_rsp = (local_rsp) + (72);
    return result;
loc_008F99D7:
    result = 0;
    goto loc_008F99D1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F99A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008F99A0[BB_008F99A0]
  bb_008F99B9[BB_008F99B9]
  bb_008F99D1[BB_008F99D1]
  bb_008F99D6[BB_008F99D6]
  bb_008F99D7[BB_008F99D7]
  bb_008F99A0 -->|branch| bb_008F99D7
  bb_008F99A0 -->|fallthrough| bb_008F99B9
  bb_008F99B9 -->|flow| bb_008F99D1
  bb_008F99D6 -->|flow| bb_008F99D7
  bb_008F99D7 -->|branch| bb_008F99D1
```
