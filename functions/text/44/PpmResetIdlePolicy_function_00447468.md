# PpmResetIdlePolicy

- RVA: `0x00447468`–`0x004474A0` (길이 `56` bytes)
- VA: `0x0000000140447468`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00092364`
- 디코드: `18`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0044747E` → [PpmApplyIdlePolicy](PpmApplyIdlePolicy_function_004474A8.md) (function, `0x004474A8`)
- `0x00447486` → [PpmScaleIdleStateValues](PpmScaleIdleStateValues_function_00447674.md) (function, `0x00447674`)
- `0x0044748D` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00447499` → [PpmResetProcessorIdleAccounting](PpmResetProcessorIdleAccounting_function_00447594.md) (function, `0x00447594`)

### Direct callers
- [PpmApplyIdlePolicyChanges](PpmApplyIdlePolicyChanges_function_00446E60.md) at `0x00446E6B`
- [PpmInstallNewIdleStates](PpmInstallNewIdleStates_function_00446E80.md) at `0x00447236`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00447468  40 53                           push rbx
0044746A  48 83 EC 20                     sub rsp, 0x20
0044746E  48 83 39 00                     cmp qword ptr [rcx], 0
00447472  48 8B D9                        mov rbx, rcx
00447475  75 07                           jne 0x14044747e
00447477  48 83 C4 20                     add rsp, 0x20
0044747B  5B                              pop rbx
0044747C  C3                              ret
0044747D  CC                              int3
0044747E  E8 25 00 00 00                  call 0x1404474a8
00447483  48 8B CB                        mov rcx, rbx
00447486  E8 E9 01 00 00                  call 0x140447674
0044748B  33 C9                           xor ecx, ecx
0044748D  E8 4E 73 F3 FF                  call 0x14037e7e0
00447492  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00447496  48 8B D0                        mov rdx, rax
00447499  E8 F6 00 00 00                  call 0x140447594
0044749E  EB D7                           jmp 0x140447477
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmResetIdlePolicy(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int64 *)(a1)) != 0) goto loc_0044747E;
loc_00447477:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0044747E:
    result = PpmApplyIdlePolicy(a1, a2, a3, a4);
    result = PpmScaleIdleStateValues(a1, a2, a3, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    result = PpmResetProcessorIdleAccounting(*(unsigned __int64 *)(a1 + 8), result, a3, a4);
    goto loc_00447477;
}
```

## 5. (Beta) C Style

```c
int64_t PpmResetIdlePolicy(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint64_t *)(arg1)) != 0) goto loc_0044747E;
loc_00447477:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0044747E:
    result = PpmApplyIdlePolicy(Arg1, a2, a3, a4);
    result = PpmScaleIdleStateValues(Arg1, a2, a3, a4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, a2, a3, a4);
    result = PpmResetProcessorIdleAccounting(*(uint64_t *)(arg1 + 0x8), result, a3, a4);
    goto loc_00447477;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00447468&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00447468[BB_00447468]
  bb_00447477[BB_00447477]
  bb_0044747D[BB_0044747D]
  bb_0044747E[BB_0044747E]
  bb_00447468 -->|branch| bb_0044747E
  bb_00447468 -->|fallthrough| bb_00447477
  bb_0044747D -->|flow| bb_0044747E
  bb_0044747E -->|branch| bb_00447477
```
