# XmCwdOp

- RVA: `0x00578250`–`0x00578291` (길이 `65` bytes)
- VA: `0x0000000140578250`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00578286` → [XmStoreResult](../47/XmStoreResult_function_004739FC.md) (function, `0x004739FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00578250  48 83 EC 28                     sub rsp, 0x28
00578254  80 B9 8A 00 00 00 00            cmp byte ptr [rcx + 0x8a], 0
0057825B  48 8D 41 20                     lea rax, [rcx + 0x20]
0057825F  48 89 41 58                     mov qword ptr [rcx + 0x58], rax
00578263  74 0F                           je 0x140578274
00578265  C7 41 78 03 00 00 00            mov dword ptr [rcx + 0x78], 3
0057826C  8B 51 18                        mov edx, dword ptr [rcx + 0x18]
0057826F  C1 FA 1F                        sar edx, 0x1f
00578272  EB 12                           jmp 0x140578286
00578274  0F B7 41 18                     movzx eax, word ptr [rcx + 0x18]
00578278  66 C1 F8 0F                     sar ax, 0xf
0057827C  0F B7 D0                        movzx edx, ax
0057827F  C7 41 78 01 00 00 00            mov dword ptr [rcx + 0x78], 1
00578286  E8 71 B7 EF FF                  call 0x1404739fc
0057828B  48 83 C4 28                     add rsp, 0x28
0057828F  C3                              ret
00578290  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmCwdOp(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(a1 + 88) = a1 + 32;
    if ((*(unsigned __int8 *)(a1 + 138)) == 0) goto loc_00578274;
    *(unsigned int *)(a1 + 120) = 3;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) >> (31));
    goto loc_00578286;
loc_00578274:
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 24)) >> (15));
    *(unsigned int *)(a1 + 120) = 1;
loc_00578286:
    result = XmStoreResult(a1, (unsigned __int16)(result), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t XmCwdOp(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(void **)(arg1 + 0x58) = Arg1 + 32;
    if ((*(uint8_t *)(arg1 + 0x8A)) == 0) goto loc_00578274;
    *(uint32_t *)(arg1 + 0x78) = 3;
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) >> (31));
    goto loc_00578286;
loc_00578274:
    result = (uint16_t)((*(uint16_t *)(arg1 + 0x18)) >> (15));
    *(uint32_t *)(arg1 + 0x78) = 1;
loc_00578286:
    result = XmStoreResult(Arg1, (uint16_t)(result), a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `16` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x78` | `32` | `W` |
| `Arg1` | `+ 0x8A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00578250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00578250[BB_00578250]
  bb_00578265[BB_00578265]
  bb_00578274[BB_00578274]
  bb_00578286[BB_00578286]
  bb_00578290[BB_00578290]
  bb_00578250 -->|branch| bb_00578274
  bb_00578250 -->|fallthrough| bb_00578265
  bb_00578265 -->|branch| bb_00578286
  bb_00578274 -->|flow| bb_00578286
```
