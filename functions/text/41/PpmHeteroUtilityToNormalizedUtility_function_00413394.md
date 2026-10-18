# PpmHeteroUtilityToNormalizedUtility

- RVA: `0x00413394`–`0x004133A5` (길이 `17` bytes)
- VA: `0x0000000140413394`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PpmHeteroComputeCoreParkingUtilities](PpmHeteroComputeCoreParkingUtilities_function_00412AE0.md) at `0x00412C11`
- [PpmHeteroComputeCoreParkingUtilities](PpmHeteroComputeCoreParkingUtilities_function_00412AE0.md) at `0x00412C1D`
- [PpmHeteroComputeCoreParkingUtilities](PpmHeteroComputeCoreParkingUtilities_function_00412AE0.md) at `0x00412CEA`
- [PpmParkDistributeUtility](PpmParkDistributeUtility_function_00412DE0.md) at `0x004132E1`
- [PpmParkDistributeUtilityEx](../4F/PpmParkDistributeUtilityEx_function_004F020C.md) at `0x004F03EF`
- [PpmParkDistributeUtilityEx](../4F/PpmParkDistributeUtilityEx_function_004F020C.md) at `0x004F0490`
- [PpmParkDistributeUtilityEx](../4F/PpmParkDistributeUtilityEx_function_004F020C.md) at `0x004F0671`
- [PpmParkDistributeUtilityEx](../4F/PpmParkDistributeUtilityEx_function_004F020C.md) at `0x004F07AF`
- [PpmHeteroComputeCoreParkingUtilitiesEx](../4F/PpmHeteroComputeCoreParkingUtilitiesEx_function_004F1E44.md) at `0x004F1FA8`
- [PpmHeteroComputeCoreParkingUtilitiesEx](../4F/PpmHeteroComputeCoreParkingUtilitiesEx_function_004F1E44.md) at `0x004F1FB4`
- [PpmHeteroComputeCoreParkingUtilitiesEx](../4F/PpmHeteroComputeCoreParkingUtilitiesEx_function_004F1E44.md) at `0x004F1FC9`
- [PpmCheckComputeHeteroResponseEx](../5D/PpmCheckComputeHeteroResponseEx_function_005DECA0.md) at `0x005DEE8E`
- [PpmCheckComputeHeteroResponseEx](../5D/PpmCheckComputeHeteroResponseEx_function_005DECA0.md) at `0x005DEE9A`
- [sub_006FA0AE](../6F/Unknown_function_006FA0AE.md) at `0x006FA155`
- [sub_006FA0AE](../6F/Unknown_function_006FA0AE.md) at `0x006FA165`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00413394  8B 41 40                        mov eax, dword ptr [rcx + 0x40]
00413397  85 C0                           test eax, eax
00413399  74 06                           je 0x1404133a1
0041339B  0F AF D0                        imul edx, eax
0041339E  C1 EA 10                        shr edx, 0x10
004133A1  8B C2                           mov eax, edx
004133A3  C3                              ret
004133A4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmHeteroUtilityToNormalizedUtility(__int64 a1, int a2)
{
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64))) != 0) {
        a2 = (unsigned int)((a2) * ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))));
        a2 = (unsigned int)((a2) >> (16));
    }
    return (unsigned int)(a2);
}
```

## 5. (Beta) C Style

```c
int64_t PpmHeteroUtilityToNormalizedUtility(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40))) != 0) {
        Arg2 = (uint32_t)((Arg2) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))));
        Arg2 = (uint32_t)((Arg2) >> (16));
    }
    return (uint32_t)(Arg2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00413394&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00413394[BB_00413394]
  bb_0041339B[BB_0041339B]
  bb_004133A1[BB_004133A1]
  bb_004133A4[BB_004133A4]
  bb_00413394 -->|branch| bb_004133A1
  bb_00413394 -->|fallthrough| bb_0041339B
  bb_0041339B -->|flow| bb_004133A1
```
