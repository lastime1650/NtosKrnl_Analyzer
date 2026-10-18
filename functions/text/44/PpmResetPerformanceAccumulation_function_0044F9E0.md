# PpmResetPerformanceAccumulation

- RVA: `0x0044F9E0`–`0x0044FA2E` (길이 `78` bytes)
- VA: `0x000000014044F9E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0044FA1B` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)

### Direct callers
- [PpmResetPerfTimes](PpmResetPerfTimes_function_0044F8EC.md) at `0x0044F929`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044F9E0  40 53                           push rbx
0044F9E2  48 83 EC 20                     sub rsp, 0x20
0044F9E6  48 0F BA A1 A0 8F 00 00 27      bt qword ptr [rcx + 0x8fa0], 0x27
0044F9EF  48 8B D9                        mov rbx, rcx
0044F9F2  73 15                           jae 0x14044fa09
0044F9F4  B9 B2 0D 00 00                  mov ecx, 0xdb2
0044F9F9  0F 32                           rdmsr
0044F9FB  48 C1 E2 20                     shl rdx, 0x20
0044F9FF  48 0B C2                        or rax, rdx
0044FA02  48 89 83 08 89 00 00            mov qword ptr [rbx + 0x8908], rax
0044FA09  0F 31                           rdtsc
0044FA0B  48 C1 E2 20                     shl rdx, 0x20
0044FA0F  33 C9                           xor ecx, ecx
0044FA11  48 0B C2                        or rax, rdx
0044FA14  48 89 83 98 88 00 00            mov qword ptr [rbx + 0x8898], rax
0044FA1B  E8 C0 ED F2 FF                  call 0x14037e7e0
0044FA20  48 89 83 B8 88 00 00            mov qword ptr [rbx + 0x88b8], rax
0044FA27  48 83 C4 20                     add rsp, 0x20
0044FA2B  5B                              pop rbx
0044FA2C  C3                              ret
0044FA2D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmResetPerformanceAccumulation(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (!(condition_is_above_or_equal)) {
        a1 = 0xDB2ULL;
        a2 = (a2) << (32);
        result = (result) | (a2);
        *(unsigned __int64 *)(a1 + 35080) = result;
    }
    a2 = (a2) << (32);
    a1 = 0;
    result = (result) | (a2);
    *(unsigned __int64 *)(a1 + 34968) = result;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(a1 + 35000) = result;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmResetPerformanceAccumulation(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (!(condition_is_above_or_equal)) {
        Arg1 = 0xDB2ULL;
        Arg2 = (Arg2) << (32);
        result = (result) | (Arg2);
        *(uint64_t *)(arg1 + 0x8908) = result;
    }
    Arg2 = (Arg2) << (32);
    Arg1 = 0;
    result = (result) | (Arg2);
    *(uint64_t *)(arg1 + 0x8898) = result;
    result = KeQueryPerformanceCounter(Arg1, Arg2, a3, a4);
    *(uint64_t *)(arg1 + 0x88B8) = result;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8898` | `64` | `W` |
| `Arg1` | `+ 0x88B8` | `64` | `W` |
| `Arg1` | `+ 0x8908` | `64` | `W` |
| `Arg1` | `+ 0x8FA0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044F9E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044F9E0[BB_0044F9E0]
  bb_0044F9F4[BB_0044F9F4]
  bb_0044FA09[BB_0044FA09]
  bb_0044FA2D[BB_0044FA2D]
  bb_0044F9E0 -->|branch| bb_0044FA09
  bb_0044F9E0 -->|fallthrough| bb_0044F9F4
  bb_0044F9F4 -->|flow| bb_0044FA09
```
