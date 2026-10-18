# MiZeroThreadContextPrepareToWait

- RVA: `0x0031E6D8`–`0x0031E712` (길이 `58` bytes)
- VA: `0x000000014031E6D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068804`
- 디코드: `16`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0031E6F0` → [MiFlushZeroPageHeatBatch](../47/MiFlushZeroPageHeatBatch_function_0047445C.md) (function, `0x0047445C`)
- `0x0031E703` → [MiFreeHardwareDescriptor](../4B/MiFreeHardwareDescriptor_function_004B6078.md) (function, `0x004B6078`)

### Direct callers
- [MiBackgroundZeroLocalPages](MiBackgroundZeroLocalPages_function_0031EF30.md) at `0x0031F553`
- [MiBackgroundZeroLocalPages](MiBackgroundZeroLocalPages_function_0031EF30.md) at `0x0031F5C5`
- [MiBackgroundZeroLocalPages](MiBackgroundZeroLocalPages_function_0031EF30.md) at `0x0031F77A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0031E6D8  40 53                           push rbx
0031E6DA  48 83 EC 20                     sub rsp, 0x20
0031E6DE  48 8B 91 A8 02 00 00            mov rdx, qword ptr [rcx + 0x2a8]
0031E6E5  48 8B D9                        mov rbx, rcx
0031E6E8  48 85 D2                        test rdx, rdx
0031E6EB  75 0F                           jne 0x14031e6fc
0031E6ED  48 8B CB                        mov rcx, rbx
0031E6F0  E8 67 5D 15 00                  call 0x14047445c
0031E6F5  48 83 C4 20                     add rsp, 0x20
0031E6F9  5B                              pop rbx
0031E6FA  C3                              ret
0031E6FB  CC                              int3
0031E6FC  48 8B 89 50 01 00 00            mov rcx, qword ptr [rcx + 0x150]
0031E703  E8 70 79 19 00                  call 0x1404b6078
0031E708  48 83 A3 A8 02 00 00 00         and qword ptr [rbx + 0x2a8], 0
0031E710  EB DB                           jmp 0x14031e6ed
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiZeroThreadContextPrepareToWait(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 680) != 0) goto loc_0031E6FC;
loc_0031E6ED:
    result = MiFlushZeroPageHeatBatch(a1, *(unsigned __int64 *)(a1 + 680), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_0031E6FC:
    result = MiFreeHardwareDescriptor(*(unsigned __int64 *)(a1 + 336), *(unsigned __int64 *)(a1 + 680), a3, a4);
    goto loc_0031E6ED;
}
```

## 5. (Beta) C Style

```c
int64_t MiZeroThreadContextPrepareToWait(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x2A8) != 0) goto loc_0031E6FC;
loc_0031E6ED:
    result = MiFlushZeroPageHeatBatch(Arg1, *(uint64_t *)(arg1 + 0x2A8), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_0031E6FC:
    result = MiFreeHardwareDescriptor(*(uint64_t *)(arg1 + 0x150), *(uint64_t *)(arg1 + 0x2A8), a3, a4);
    goto loc_0031E6ED;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x150` | `64` | `R` |
| `Arg1` | `+ 0x2A8` | `64` | `R` |
| `Arg1` | `+ 0x2A8` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031E6D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0031E6D8[BB_0031E6D8]
  bb_0031E6ED[BB_0031E6ED]
  bb_0031E6FB[BB_0031E6FB]
  bb_0031E6FC[BB_0031E6FC]
  bb_0031E6D8 -->|branch| bb_0031E6FC
  bb_0031E6D8 -->|fallthrough| bb_0031E6ED
  bb_0031E6FB -->|flow| bb_0031E6FC
  bb_0031E6FC -->|branch| bb_0031E6ED
```
