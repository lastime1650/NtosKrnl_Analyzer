# FsRtlNumberOfRunsInBaseMcb

- RVA: `0x004574D0`–`0x004574D5` (길이 `5` bytes)
- VA: `0x00000001404574D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `5/5` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptCrtGenerateForTwoCoprimes](../52/SymCryptCrtGenerateForTwoCoprimes_function_0052A950.md) at `0x0052A976`
- [SymCryptCrtGenerateForTwoCoprimes](../52/SymCryptCrtGenerateForTwoCoprimes_function_0052A950.md) at `0x0052A980`
- [SymCryptCrtGenerateForTwoCoprimes](../52/SymCryptCrtGenerateForTwoCoprimes_function_0052A950.md) at `0x0052A98E`
- [SymCryptCrtSolve](../52/SymCryptCrtSolve_function_0052AB54.md) at `0x0052AB78`
- [SymCryptCrtSolve](../52/SymCryptCrtSolve_function_0052AB54.md) at `0x0052AB83`
- [SymCryptCrtSolve](../52/SymCryptCrtSolve_function_0052AB54.md) at `0x0052AB95`
- [SymCryptIntExtendedGcd](../52/SymCryptIntExtendedGcd_function_0052AD54.md) at `0x0052AD7F`
- [SymCryptIntExtendedGcd](../52/SymCryptIntExtendedGcd_function_0052AD54.md) at `0x0052AD89`
- [SymCryptIntExtendedGcd](../52/SymCryptIntExtendedGcd_function_0052AD54.md) at `0x0052AD97`
- [KiTpBuildExcludedKernelTracepointBitmap](../../page/74/KiTpBuildExcludedKernelTracepointBitmap_function_007485B0.md) at `0x00748649`
- [KiTpBuildExcludedKernelTracepointBitmap](../../page/74/KiTpBuildExcludedKernelTracepointBitmap_function_007485B0.md) at `0x0074873F`
- [KiTpBuildExcludedKernelTracepointBitmap](../../page/74/KiTpBuildExcludedKernelTracepointBitmap_function_007485B0.md) at `0x00748785`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004574D0  8B 41 04                        mov eax, dword ptr [rcx + 4]
004574D3  C3                              ret
004574D4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlNumberOfRunsInBaseMcb(__int64 a1)
{
    return (unsigned int)(*(unsigned int *)(a1 + 4));
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlNumberOfRunsInBaseMcb(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    return (uint32_t)(*(uint32_t *)(arg1 + 0x4));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004574D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004574D0[BB_004574D0]
  bb_004574D4[BB_004574D4]
```
