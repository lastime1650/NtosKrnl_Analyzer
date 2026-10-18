# HalpCorrectGenericErrSrc

- RVA: `0x00555B10`–`0x00555B2D` (길이 `29` bytes)
- VA: `0x0000000140555B10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpCorrectErrSrc](../../pagelk/B5/HalpCorrectErrSrc_function_00B5B820.md) at `0x00B5B863`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00555B10  80 79 40 00                     cmp byte ptr [rcx + 0x40], 0
00555B14  75 04                           jne 0x140555b1a
00555B16  83 61 14 00                     and dword ptr [rcx + 0x14], 0
00555B1A  44 8B 41 2C                     mov r8d, dword ptr [rcx + 0x2c]
00555B1E  33 C0                           xor eax, eax
00555B20  8B 49 10                        mov ecx, dword ptr [rcx + 0x10]
00555B23  83 C1 50                        add ecx, 0x50
00555B26  41 03 C8                        add ecx, r8d
00555B29  89 0A                           mov dword ptr [rdx], ecx
00555B2B  C3                              ret
00555B2C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpCorrectGenericErrSrc(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned __int8 *)(a1 + 64)) == 0) {
    }
    result = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) + (80));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44)))));
    *(unsigned int *)(a2) = (unsigned int)(a1);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpCorrectGenericErrSrc(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint8_t *)(arg1 + 0x40)) == 0) {
    }
    result = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) + (80));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)))));
    *(uint32_t *)(arg2) = (uint32_t)(Arg1);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R/W` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x40` | `8` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00555B10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00555B10[BB_00555B10]
  bb_00555B16[BB_00555B16]
  bb_00555B1A[BB_00555B1A]
  bb_00555B2C[BB_00555B2C]
  bb_00555B10 -->|branch| bb_00555B1A
  bb_00555B10 -->|fallthrough| bb_00555B16
  bb_00555B16 -->|flow| bb_00555B1A
```
