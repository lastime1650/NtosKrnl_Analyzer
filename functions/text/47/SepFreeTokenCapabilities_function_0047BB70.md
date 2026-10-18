# SepFreeTokenCapabilities

- RVA: `0x0047BB70`–`0x0047BBA7` (길이 `55` bytes)
- VA: `0x000000014047BB70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070B1C`
- 디코드: `16`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0047BB8B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0047BBA0` → [SepDeReferenceSharedSidEntries](../../page/7A/SepDeReferenceSharedSidEntries_function_007A2D40.md) (function, `0x007A2D40`)

### Direct callers
- [SepSetTokenCapabilities](../../page/9C/SepSetTokenCapabilities_function_009C9AF4.md) at `0x009C9C82`
- [SepSetTokenCapabilities](../../page/9C/SepSetTokenCapabilities_function_009C9AF4.md) at `0x009C9CA6`
- [SepTokenDeleteMethod](../../page/AF/SepTokenDeleteMethod_function_00AF23D0.md) at `0x00AF2579`

### Static image references
- `0x0047BB76` → RVA `0x00E67BF1` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0047BB8B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0047BBA0` → [SepDeReferenceSharedSidEntries](../../page/7A/SepDeReferenceSharedSidEntries_function_007A2D40.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047BB70  40 53                           push rbx
0047BB72  48 83 EC 20                     sub rsp, 0x20
0047BB76  80 3D 74 C0 9E 00 00            cmp byte ptr [rip + 0x9ec074], 0
0047BB7D  48 8D 99 18 03 00 00            lea rbx, [rcx + 0x318]
0047BB84  75 11                           jne 0x14047bb97
0047BB86  48 8B 0B                        mov rcx, qword ptr [rbx]
0047BB89  33 D2                           xor edx, edx
0047BB8B  E8 E0 6C 70 00                  call 0x140b82870
0047BB90  48 83 C4 20                     add rsp, 0x20
0047BB94  5B                              pop rbx
0047BB95  C3                              ret
0047BB96  CC                              int3
0047BB97  8B 91 20 03 00 00               mov edx, dword ptr [rcx + 0x320]
0047BB9D  48 8B 0B                        mov rcx, qword ptr [rbx]
0047BBA0  E8 9B 71 32 00                  call 0x1407a2d40
0047BBA5  EB DF                           jmp 0x14047bb86
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepFreeTokenCapabilities(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int8 *)(v_rip + 10403956)) != 0) goto loc_0047BB97;
loc_0047BB86:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 792), a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_0047BB97:
    result = SepDeReferenceSharedSidEntries(*(unsigned __int64 *)(a1 + 792), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 792) + 800)), a3, a4);
    goto loc_0047BB86;
}
```

## 5. (Beta) C Style

```c
int64_t SepFreeTokenCapabilities(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint8_t *)(v_rip + 0x9EC074)) != 0) goto loc_0047BB97;
loc_0047BB86:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x318), Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_0047BB97:
    result = SepDeReferenceSharedSidEntries(*(uint64_t *)(arg1 + 0x318), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x318) + 0x320)), a3, a4);
    goto loc_0047BB86;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x318` | `64` | `R` |
| `Arg1` | `+ 0x320` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047BB70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047BB70[BB_0047BB70]
  bb_0047BB86[BB_0047BB86]
  bb_0047BB96[BB_0047BB96]
  bb_0047BB97[BB_0047BB97]
  bb_0047BB70 -->|branch| bb_0047BB97
  bb_0047BB70 -->|fallthrough| bb_0047BB86
  bb_0047BB96 -->|flow| bb_0047BB97
  bb_0047BB97 -->|branch| bb_0047BB86
```
