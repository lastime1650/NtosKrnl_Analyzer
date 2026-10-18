# RtlpHpInitializeLock

- RVA: `0x002E8054`–`0x002E8065` (길이 `17` bytes)
- VA: `0x00000001402E8054`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpHpLfhSubsegmentInitialize](RtlpHpLfhSubsegmentInitialize_function_002E806C.md) at `0x002E817E`
- [RtlpHpLfhOwnerInitialize](../4C/RtlpHpLfhOwnerInitialize_function_004CE0F4.md) at `0x004CE123`
- [RtlpHpHeapCreate](../60/RtlpHpHeapCreate_function_00602FDC.md) at `0x0060316E`
- [RtlpHpHeapCreate](../60/RtlpHpHeapCreate_function_00602FDC.md) at `0x0060318B`
- [RtlpHpFixedHeapCreate](../60/RtlpHpFixedHeapCreate_function_006038A0.md) at `0x00603A27`
- [RtlpHpVaMgrCtxAllocatorReference](../60/RtlpHpVaMgrCtxAllocatorReference_function_00603BC0.md) at `0x00603C8B`
- [RtlpHpSegContextInitialize](../60/RtlpHpSegContextInitialize_function_0060421C.md) at `0x006042CD`
- [RtlpHpLfhBucketInitialize](../60/RtlpHpLfhBucketInitialize_function_0060475C.md) at `0x00604780`
- [RtlpHpVsSlotCreate](../60/RtlpHpVsSlotCreate_function_006057C0.md) at `0x00605811`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002E8054  85 D2                           test edx, edx
002E8056  74 07                           je 0x1402e805f
002E8058  33 C0                           xor eax, eax
002E805A  48 89 01                        mov qword ptr [rcx], rax
002E805D  C3                              ret
002E805E  CC                              int3
002E805F  48 83 21 00                     and qword ptr [rcx], 0
002E8063  C3                              ret
002E8064  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpInitializeLock(__int64 a1, int a2)
{
    __int64 result;

    if (a2 == 0) goto loc_002E805F;
    result = 0;
    *(unsigned __int64 *)(a1) = 0;
    return result;
loc_002E805F:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpInitializeLock(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (Arg2 == 0) goto loc_002E805F;
    result = 0;
    *(uint64_t *)(arg1) = 0;
    return result;
loc_002E805F:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E8054&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E8054[BB_002E8054]
  bb_002E8058[BB_002E8058]
  bb_002E805E[BB_002E805E]
  bb_002E805F[BB_002E805F]
  bb_002E8064[BB_002E8064]
  bb_002E8054 -->|branch| bb_002E805F
  bb_002E8054 -->|fallthrough| bb_002E8058
  bb_002E805E -->|flow| bb_002E805F
```
