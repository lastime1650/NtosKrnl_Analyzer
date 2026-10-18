# ApiSetIsSchemaSealed

- RVA: `0x00662D48`–`0x00662D71` (길이 `41` bytes)
- VA: `0x0000000140662D48`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `17`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ApiSetComposeSchema_V7](ApiSetComposeSchema_V7_function_00663CCC.md) at `0x00663D05`
- [ApiSetLoadSchemaWithExtensions](../../page/7D/ApiSetLoadSchemaWithExtensions_function_007D9810.md) at `0x007D9876`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00662D48  32 C0                           xor al, al
00662D4A  83 39 06                        cmp dword ptr [rcx], 6
00662D4D  75 16                           jne 0x140662d65
00662D4F  83 79 10 08                     cmp dword ptr [rcx + 0x10], 8
00662D53  76 0B                           jbe 0x140662d60
00662D55  80 79 1C 07                     cmp byte ptr [rcx + 0x1c], 7
00662D59  75 05                           jne 0x140662d60
00662D5B  8A 41 1E                        mov al, byte ptr [rcx + 0x1e]
00662D5E  EB 0D                           jmp 0x140662d6d
00662D60  8A 41 08                        mov al, byte ptr [rcx + 8]
00662D63  EB 08                           jmp 0x140662d6d
00662D65  80 39 07                        cmp byte ptr [rcx], 7
00662D68  75 05                           jne 0x140662d6f
00662D6A  8A 41 02                        mov al, byte ptr [rcx + 2]
00662D6D  24 01                           and al, 1
00662D6F  C3                              ret
00662D70  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ApiSetIsSchemaSealed(__int64 a1)
{
    __int64 result;

    result = 0;
    if ((*(unsigned int *)(a1)) != 6) goto loc_00662D65;
    if ((*(unsigned int *)(a1 + 16)) <= 8) goto loc_00662D60;
    if ((*(unsigned __int8 *)(a1 + 28)) != 7) goto loc_00662D60;
    goto loc_00662D6D;
loc_00662D60:
    goto loc_00662D6D;
loc_00662D65:
    if ((*(unsigned __int8 *)(a1)) != 7) goto loc_00662D6F;
loc_00662D6D:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 2)) & (1));
loc_00662D6F:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ApiSetIsSchemaSealed(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 0;
    if ((*(uint32_t *)(arg1)) != 6) goto loc_00662D65;
    if ((*(uint32_t *)(arg1 + 0x10)) <= 8) goto loc_00662D60;
    if ((*(uint8_t *)(arg1 + 0x1C)) != 7) goto loc_00662D60;
    goto loc_00662D6D;
loc_00662D60:
    goto loc_00662D6D;
loc_00662D65:
    if ((*(uint8_t *)(arg1)) != 7) goto loc_00662D6F;
loc_00662D6D:
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x2)) & (1));
loc_00662D6F:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `8` | `R` |
| `Arg1` | `+ 0x1E` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00662D48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00662D48[BB_00662D48]
  bb_00662D4F[BB_00662D4F]
  bb_00662D55[BB_00662D55]
  bb_00662D5B[BB_00662D5B]
  bb_00662D60[BB_00662D60]
  bb_00662D65[BB_00662D65]
  bb_00662D6A[BB_00662D6A]
  bb_00662D6D[BB_00662D6D]
  bb_00662D6F[BB_00662D6F]
  bb_00662D70[BB_00662D70]
  bb_00662D48 -->|branch| bb_00662D65
  bb_00662D48 -->|fallthrough| bb_00662D4F
  bb_00662D4F -->|branch| bb_00662D60
  bb_00662D4F -->|fallthrough| bb_00662D55
  bb_00662D55 -->|branch| bb_00662D60
  bb_00662D55 -->|fallthrough| bb_00662D5B
  bb_00662D5B -->|branch| bb_00662D6D
  bb_00662D60 -->|branch| bb_00662D6D
  bb_00662D65 -->|branch| bb_00662D6F
  bb_00662D65 -->|fallthrough| bb_00662D6A
  bb_00662D6A -->|flow| bb_00662D6D
  bb_00662D6D -->|flow| bb_00662D6F
```
