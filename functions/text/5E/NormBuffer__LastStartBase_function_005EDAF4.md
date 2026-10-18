# NormBuffer__LastStartBase

- RVA: `0x005EDAF4`–`0x005EDB1A` (길이 `38` bytes)
- VA: `0x00000001405EDAF4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005EDB0B` → [Normalization__GetFirstDecomposedCharPlane0](../../page/79/Normalization__GetFirstDecomposedCharPlane0_function_007931B0.md) (function, `0x007931B0`)

### Direct callers
- [NormBuffer__LastStartBasePair](NormBuffer__LastStartBasePair_function_005EDB20.md) at `0x005EDB45`
- [Normalization__NormalizeCharacter](../../page/79/Normalization__NormalizeCharacter_function_00793D34.md) at `0x0079429F`
- [Normalization__NormalizeCharacter](../../page/79/Normalization__NormalizeCharacter_function_00793D34.md) at `0x007943E3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005EDB0B` → [Normalization__GetFirstDecomposedCharPlane0](../../page/79/Normalization__GetFirstDecomposedCharPlane0_function_007931B0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005EDAF4  40 53                           push rbx
005EDAF6  48 83 EC 20                     sub rsp, 0x20
005EDAFA  8B 41 60                        mov eax, dword ptr [rcx + 0x60]
005EDAFD  48 8B D9                        mov rbx, rcx
005EDB00  85 C0                           test eax, eax
005EDB02  75 0F                           jne 0x1405edb13
005EDB04  8B 51 58                        mov edx, dword ptr [rcx + 0x58]
005EDB07  48 8B 49 70                     mov rcx, qword ptr [rcx + 0x70]
005EDB0B  E8 A0 56 1A 00                  call 0x1407931b0
005EDB10  89 43 60                        mov dword ptr [rbx + 0x60], eax
005EDB13  48 83 C4 20                     add rsp, 0x20
005EDB17  5B                              pop rbx
005EDB18  C3                              ret
005EDB19  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NormBuffer__LastStartBase(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned int)(*(unsigned int *)(a1 + 96));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 96))) == 0) {
        a2 = *(unsigned int *)(a1 + 88);
        a1 = *(unsigned __int64 *)(a1 + 112);
        result = Normalization__GetFirstDecomposedCharPlane0(a1, a2, a3, a4);
        *(unsigned int *)(a1 + 96) = (unsigned int)(result);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NormBuffer__LastStartBase(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x60));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x60))) == 0) {
        a2 = *(uint32_t *)(arg1 + 0x58);
        Arg1 = *(uint64_t *)(arg1 + 0x70);
        result = Normalization__GetFirstDecomposedCharPlane0(Arg1, a2, a3, a4);
        *(uint32_t *)(arg1 + 0x60) = (uint32_t)(result);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x58` | `32` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R` |
| `Arg1` | `+ 0x60` | `32` | `W` |
| `Arg1` | `+ 0x70` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EDAF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005EDAF4[BB_005EDAF4]
  bb_005EDB04[BB_005EDB04]
  bb_005EDB13[BB_005EDB13]
  bb_005EDB19[BB_005EDB19]
  bb_005EDAF4 -->|branch| bb_005EDB13
  bb_005EDAF4 -->|fallthrough| bb_005EDB04
  bb_005EDB04 -->|flow| bb_005EDB13
```
