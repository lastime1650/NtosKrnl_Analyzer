# RtlEqualString

- RVA: `0x0048BDE0`–`0x0048BE00` (길이 `32` bytes)
- VA: `0x000000014048BDE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00090138`
- 디코드: `12`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0048BDF4` → [RtlCompareString](../../page/90/RtlCompareString_function_0090E880.md) (function, `0x0090E880`)

### Direct callers
- [SepImageHashFromEa](../60/SepImageHashFromEa_function_00608310.md) at `0x0060835B`
- [IopGetBootDiskInformation](../../init/C2/IopGetBootDiskInformation_function_00C2DAAC.md) at `0x00C2DE70`
- [IopGetBootDiskInformation](../../init/C2/IopGetBootDiskInformation_function_00C2DAAC.md) at `0x00C2DEAF`
- [IopInitializeBuiltinDriver](../../init/C7/IopInitializeBuiltinDriver_function_00C7625C.md) at `0x00C763DA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0048BDF4` → [RtlCompareString](../../page/90/RtlCompareString_function_0090E880.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048BDE0  48 83 EC 28                     sub rsp, 0x28
0048BDE4  0F B7 02                        movzx eax, word ptr [rdx]
0048BDE7  66 39 01                        cmp word ptr [rcx], ax
0048BDEA  74 08                           je 0x14048bdf4
0048BDEC  32 C0                           xor al, al
0048BDEE  48 83 C4 28                     add rsp, 0x28
0048BDF2  C3                              ret
0048BDF3  CC                              int3
0048BDF4  E8 87 2A 48 00                  call 0x14090e880
0048BDF9  85 C0                           test eax, eax
0048BDFB  0F 94 C0                        sete al
0048BDFE  EB EE                           jmp 0x14048bdee
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlEqualString(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int16 *)(a1)) == ((unsigned __int16)(*(unsigned __int16 *)(a2)))) goto loc_0048BDF4;
    result = 0;
loc_0048BDEE:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0048BDF4:
    result = RtlCompareString(a1, a2, a3, a4);
    result = ((unsigned int)(result) == 0) ? 1 : 0;
    goto loc_0048BDEE;
}
```

## 5. (Beta) C Style

```c
int64_t RtlEqualString(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint16_t *)(arg1)) == ((uint16_t)(*(uint16_t *)(arg2)))) goto loc_0048BDF4;
    result = 0;
loc_0048BDEE:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0048BDF4:
    result = RtlCompareString(Arg1, Arg2, a3, a4);
    result = ((uint32_t)(result) == 0) ? 1 : 0;
    goto loc_0048BDEE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048BDE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048BDE0[BB_0048BDE0]
  bb_0048BDEC[BB_0048BDEC]
  bb_0048BDEE[BB_0048BDEE]
  bb_0048BDF3[BB_0048BDF3]
  bb_0048BDF4[BB_0048BDF4]
  bb_0048BDE0 -->|branch| bb_0048BDF4
  bb_0048BDE0 -->|fallthrough| bb_0048BDEC
  bb_0048BDEC -->|flow| bb_0048BDEE
  bb_0048BDF3 -->|flow| bb_0048BDF4
  bb_0048BDF4 -->|branch| bb_0048BDEE
```
