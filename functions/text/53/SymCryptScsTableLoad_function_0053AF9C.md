# SymCryptScsTableLoad

- RVA: `0x0053AF9C`–`0x0053AFBB` (길이 `31` bytes)
- VA: `0x000000014053AF9C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0053AFA9` → [SymCryptScsTableLoad128Xmm](SymCryptScsTableLoad128Xmm_function_0053AFC4.md) (function, `0x0053AFC4`)
- `0x0053AFB0` → [SymCryptScsTableLoadC](SymCryptScsTableLoadC_function_0053B138.md) (function, `0x0053B138`)

### Direct callers
- [SymCryptModExpWindowed](SymCryptModExpWindowed_function_00536188.md) at `0x00536389`
- [SymCryptModExpWindowed](SymCryptModExpWindowed_function_00536188.md) at `0x005363F0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053AF9C  48 83 EC 28                     sub rsp, 0x28
0053AFA0  81 79 0C 80 00 00 00            cmp dword ptr [rcx + 0xc], 0x80
0053AFA7  75 07                           jne 0x14053afb0
0053AFA9  E8 16 00 00 00                  call 0x14053afc4
0053AFAE  EB 05                           jmp 0x14053afb5
0053AFB0  E8 83 01 00 00                  call 0x14053b138
0053AFB5  48 83 C4 28                     add rsp, 0x28
0053AFB9  C3                              ret
0053AFBA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptScsTableLoad(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(a1 + 12)) != 128) goto loc_0053AFB0;
    result = SymCryptScsTableLoad128Xmm(a1, a2, a3, a4);
    goto loc_0053AFB5;
loc_0053AFB0:
    result = SymCryptScsTableLoadC(a1, a2, a3, a4);
loc_0053AFB5:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptScsTableLoad(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(arg1 + 0xC)) != 128) goto loc_0053AFB0;
    result = SymCryptScsTableLoad128Xmm(Arg1, a2, a3, a4);
    goto loc_0053AFB5;
loc_0053AFB0:
    result = SymCryptScsTableLoadC(Arg1, a2, a3, a4);
loc_0053AFB5:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053AF9C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0053AF9C[BB_0053AF9C]
  bb_0053AFA9[BB_0053AFA9]
  bb_0053AFB0[BB_0053AFB0]
  bb_0053AFB5[BB_0053AFB5]
  bb_0053AFBA[BB_0053AFBA]
  bb_0053AF9C -->|branch| bb_0053AFB0
  bb_0053AF9C -->|fallthrough| bb_0053AFA9
  bb_0053AFA9 -->|branch| bb_0053AFB5
  bb_0053AFB0 -->|flow| bb_0053AFB5
```
