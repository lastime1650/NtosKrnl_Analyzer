# PspRequestProcessExecutionStateLegacy

- RVA: `0x005E42D8`–`0x005E42F3` (길이 `27` bytes)
- VA: `0x00000001405E42D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspSetProcessFreezeStateCallback](../4E/PspSetProcessFreezeStateCallback_function_004E98E0.md) at `0x004E99FC`
- [PsSwapProcessWorkingSet](../../page/78/PsSwapProcessWorkingSet_function_00781C24.md) at `0x00781CB7`
- [PspApplyJobChainLimitsToProcess](../../page/87/PspApplyJobChainLimitsToProcess_function_0087EB5C.md) at `0x0087EBEC`
- [PspRemoveProcessFromJobChain](../../page/90/PspRemoveProcessFromJobChain_function_00907288.md) at `0x0090752D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E42D8  8B 81 FC 05 00 00               mov eax, dword ptr [rcx + 0x5fc]
005E42DE  A8 01                           test al, 1
005E42E0  74 09                           je 0x1405e42eb
005E42E2  41 F6 C0 01                     test r8b, 1
005E42E6  75 03                           jne 0x1405e42eb
005E42E8  80 E2 FD                        and dl, 0xfd
005E42EB  88 91 FA 07 00 00               mov byte ptr [rcx + 0x7fa], dl
005E42F1  C3                              ret
005E42F2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspRequestProcessExecutionStateLegacy(__int64 a1, unsigned __int8 a2, unsigned __int8 a3)
{
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1532)))) & (1)) == 0) goto loc_005E42EB;
    if (((a3) & (1)) == 0) {
        a2 = (unsigned __int8)((a2) & (253));
    }
    *(unsigned __int8 *)(a1 + 2042) = a2;
    return (unsigned int)(*(unsigned int *)(a1 + 1532));
}
```

## 5. (Beta) C Style

```c
int64_t PspRequestProcessExecutionStateLegacy(void *Arg1, uint8_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5FC)))) & (1)) == 0) goto loc_005E42EB;
    if (((Arg3) & (1)) == 0) {
        Arg2 = (uint8_t)((Arg2) & (253));
    }
    *(uint8_t *)(arg1 + 0x7FA) = Arg2;
    return (uint32_t)(*(uint32_t *)(arg1 + 0x5FC));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x5FC` | `32` | `R` |
| `Arg1` | `+ 0x7FA` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E42D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E42D8[BB_005E42D8]
  bb_005E42E2[BB_005E42E2]
  bb_005E42E8[BB_005E42E8]
  bb_005E42EB[BB_005E42EB]
  bb_005E42F2[BB_005E42F2]
  bb_005E42D8 -->|branch| bb_005E42EB
  bb_005E42D8 -->|fallthrough| bb_005E42E2
  bb_005E42E2 -->|branch| bb_005E42EB
  bb_005E42E2 -->|fallthrough| bb_005E42E8
  bb_005E42E8 -->|flow| bb_005E42EB
```
