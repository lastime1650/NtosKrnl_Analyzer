# HalpCorrectNMIErrSrc

- RVA: `0x00545980`–`0x005459A2` (길이 `34` bytes)
- VA: `0x0000000140545980`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpCorrectErrSrc](../../pagelk/B5/HalpCorrectErrSrc_function_00B5B820.md) at `0x00B5B86D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00545980  83 79 18 03                     cmp dword ptr [rcx + 0x18], 3
00545984  73 07                           jae 0x14054598d
00545986  C7 41 18 03 00 00 00            mov dword ptr [rcx + 0x18], 3
0054598D  41 B8 C0 00 00 00               mov r8d, 0xc0
00545993  44 89 02                        mov dword ptr [rdx], r8d
00545996  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
00545999  41 03 C0                        add eax, r8d
0054599C  89 02                           mov dword ptr [rdx], eax
0054599E  33 C0                           xor eax, eax
005459A0  C3                              ret
005459A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpCorrectNMIErrSrc(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 24)) < 3) {
        *(unsigned int *)(a1 + 24) = 3;
    }
    *(unsigned int *)(a2) = 192;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) + (192));
    *(unsigned int *)(a2) = (unsigned int)(result);
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpCorrectNMIErrSrc(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0x18)) < 3) {
        *(uint32_t *)(arg1 + 0x18) = 3;
    }
    *(uint32_t *)(arg2) = 192;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) + (192));
    *(uint32_t *)(arg2) = (uint32_t)(result);
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00545980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00545980[BB_00545980]
  bb_00545986[BB_00545986]
  bb_0054598D[BB_0054598D]
  bb_005459A1[BB_005459A1]
  bb_00545980 -->|branch| bb_0054598D
  bb_00545980 -->|fallthrough| bb_00545986
  bb_00545986 -->|flow| bb_0054598D
```
