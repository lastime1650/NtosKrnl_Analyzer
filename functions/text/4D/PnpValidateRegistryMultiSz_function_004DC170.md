# PnpValidateRegistryMultiSz

- RVA: `0x004DC170`–`0x004DC19E` (길이 `46` bytes)
- VA: `0x00000001404DC170`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `16`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004DC189` → [PnpValidateMultiSzData](../4B/PnpValidateMultiSzData_function_004BD294.md) (function, `0x004BD294`)

### Direct callers
- [PiDevCfgQueryIncludedDriverNode](../../page/73/PiDevCfgQueryIncludedDriverNode_function_00734D88.md) at `0x00735150`
- [PiDevCfgResolveVariableFormatString](../../page/73/PiDevCfgResolveVariableFormatString_function_00735AB0.md) at `0x00735BEC`
- [PiDevCfgResolveVariableExpression](../../page/AA/PiDevCfgResolveVariableExpression_function_00AA8C00.md) at `0x00AA8C7B`
- [PiDevCfgResolveMultiSzValue](../../page/AB/PiDevCfgResolveMultiSzValue_function_00AB6894.md) at `0x00AB6934`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004DC170  48 83 EC 28                     sub rsp, 0x28
004DC174  45 32 C9                        xor r9b, r9b
004DC177  48 8B D1                        mov rdx, rcx
004DC17A  83 79 04 07                     cmp dword ptr [rcx + 4], 7
004DC17E  75 15                           jne 0x1404dc195
004DC180  8B 49 08                        mov ecx, dword ptr [rcx + 8]
004DC183  48 03 CA                        add rcx, rdx
004DC186  8B 52 0C                        mov edx, dword ptr [rdx + 0xc]
004DC189  E8 06 11 FE FF                  call 0x1404bd294
004DC18E  84 C0                           test al, al
004DC190  74 03                           je 0x1404dc195
004DC192  41 B1 01                        mov r9b, 1
004DC195  41 8A C1                        mov al, r9b
004DC198  48 83 C4 28                     add rsp, 0x28
004DC19C  C3                              ret
004DC19D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpValidateRegistryMultiSz(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 0;
    if ((*(unsigned int *)(a1 + 4)) != 7) goto loc_004DC195;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 8))) + (a1);
    result = PnpValidateMultiSzData(a1, (unsigned int)(*(unsigned int *)(a1 + 12)), a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a4 = 1;
    }
    v_rsp = (v_rsp) + (40);
    return a4;
}
```

## 5. (Beta) C Style

```c
int64_t PnpValidateRegistryMultiSz(void *Arg1, int64_t Arg2, int64_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg4 = 0;
    if ((*(uint32_t *)(arg1 + 0x4)) != 7) goto loc_004DC195;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x8))) + (Arg1);
    result = PnpValidateMultiSzData(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0xC)), Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg4 = 1;
    }
    local_rsp = (local_rsp) + (40);
    return Arg4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004DC170&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004DC170[BB_004DC170]
  bb_004DC180[BB_004DC180]
  bb_004DC192[BB_004DC192]
  bb_004DC195[BB_004DC195]
  bb_004DC19D[BB_004DC19D]
  bb_004DC170 -->|branch| bb_004DC195
  bb_004DC170 -->|fallthrough| bb_004DC180
  bb_004DC180 -->|branch| bb_004DC195
  bb_004DC180 -->|fallthrough| bb_004DC192
  bb_004DC192 -->|flow| bb_004DC195
```
