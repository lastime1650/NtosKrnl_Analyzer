# SymCryptFdefIntNeg

- RVA: `0x0052D92C`–`0x0052D949` (길이 `29` bytes)
- VA: `0x000000014052D92C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0052D93E` → [SymCryptFdefRawNeg](SymCryptFdefRawNeg_function_0052E028.md) (function, `0x0052E028`)

### Direct callers
- [SymCryptIntNeg](SymCryptIntNeg_function_00525718.md) at `0x0052571C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052D92C  48 83 EC 28                     sub rsp, 0x28
0052D930  44 8B 4A 04                     mov r9d, dword ptr [rdx + 4]
0052D934  4C 8D 42 20                     lea r8, [rdx + 0x20]
0052D938  33 D2                           xor edx, edx
0052D93A  48 83 C1 20                     add rcx, 0x20
0052D93E  E8 E5 06 00 00                  call 0x14052e028
0052D943  48 83 C4 28                     add rsp, 0x28
0052D947  C3                              ret
0052D948  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefIntNeg(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    a1 = (a1) + (32);
    result = SymCryptFdefRawNeg(a1, a2, a2 + 32, (unsigned int)(*(unsigned int *)(a2 + 4)));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefIntNeg(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    Arg1 = (Arg1) + (32);
    result = SymCryptFdefRawNeg(Arg1, Arg2, Arg2 + 32, (uint32_t)(*(uint32_t *)(arg2 + 0x4)));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052D92C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052D92C[BB_0052D92C]
  bb_0052D948[BB_0052D948]
```
