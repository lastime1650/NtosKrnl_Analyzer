# DpxReleaseSimpleRundown

- RVA: `0x005B04C0`–`0x005B04DD` (길이 `29` bytes)
- VA: `0x00000001405B04C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DpxEndpointWrappedCall](../../drvprx/BC/DpxEndpointWrappedCall_function_00BCF010.md) at `0x00BCF0A4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B04C0  65 8B 14 25 A4 01 00 00         mov edx, dword ptr gs:[0x1a4]
005B04C8  8B 41 08                        mov eax, dword ptr [rcx + 8]
005B04CB  FF C8                           dec eax
005B04CD  23 C2                           and eax, edx
005B04CF  0F AF 41 0C                     imul eax, dword ptr [rcx + 0xc]
005B04D3  48 03 01                        add rax, qword ptr [rcx]
005B04D6  F0 48 83 00 FE                  lock add qword ptr [rax], -2
005B04DB  C3                              ret
005B04DC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DpxReleaseSimpleRundown(__int64 a1)
{
    __int64 result;

    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) - 1);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))));
    result = (unsigned int)((result) * (*(unsigned int *)(a1 + 12)));
    result = (result) + (*(unsigned __int64 *)(a1));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DpxReleaseSimpleRundown(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) - 1);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))));
    result = (uint32_t)((result) * (*(uint32_t *)(arg1 + 0xC)));
    result = (result) + (*(uint64_t *)(arg1));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B04C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B04C0[BB_005B04C0]
  bb_005B04DC[BB_005B04DC]
```
