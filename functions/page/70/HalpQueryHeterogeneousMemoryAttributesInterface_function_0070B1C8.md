# HalpQueryHeterogeneousMemoryAttributesInterface

- RVA: `0x0070B1C8`–`0x0070B1EC` (길이 `36` bytes)
- VA: `0x000000014070B1C8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00B80AC2](../../pagelk/B8/Unknown_function_00B80AC2.md) at `0x00B80B6C`

### Static image references
- `0x0070B1C8` → RVA `0x0070B100` (`HalpNumaQueryMemorySideCacheInfo`; read)
- `0x0070B1D2` → RVA `0x00559550` (`HalpNumaQueryMemoryNumaAttributes`; read)
- `0x0070B1DD` → RVA `0x005597E0` (`HalpNumaQuerySystemLocalityLatencyAndBandwidthInfo`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0070B1C8  48 8D 05 31 FF FF FF            lea rax, [rip - 0xcf]
0070B1CF  48 89 01                        mov qword ptr [rcx], rax
0070B1D2  48 8D 05 77 E3 E4 FF            lea rax, [rip - 0x1b1c89]
0070B1D9  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
0070B1DD  48 8D 05 FC E5 E4 FF            lea rax, [rip - 0x1b1a04]
0070B1E4  48 89 41 08                     mov qword ptr [rcx + 8], rax
0070B1E8  33 C0                           xor eax, eax
0070B1EA  C3                              ret
0070B1EB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpQueryHeterogeneousMemoryAttributesInterface(__int64 a1)
{
    __int64 result;

    *(unsigned __int64 *)(a1) = v_rip - 207;
    *(unsigned __int64 *)(a1 + 16) = v_rip - 1776777;
    *(unsigned __int64 *)(a1 + 8) = v_rip - 1776132;
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpQueryHeterogeneousMemoryAttributesInterface(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    *(uint64_t *)(arg1) = v_rip - 207;
    *(uint64_t *)(arg1 + 0x10) = v_rip - 1776777;
    *(uint64_t *)(arg1 + 0x8) = v_rip - 1776132;
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0070B1C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0070B1C8[BB_0070B1C8]
  bb_0070B1EB[BB_0070B1EB]
```
