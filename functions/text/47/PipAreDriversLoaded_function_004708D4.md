# PipAreDriversLoaded

- RVA: `0x004708D4`–`0x004708F2` (길이 `30` bytes)
- VA: `0x00000001404708D4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004708E7` → [PipAreDriversLoadedWorker](PipAreDriversLoadedWorker_function_004708F8.md) (function, `0x004708F8`)

### Direct callers
- [IoReportDetectedDevice](../../page/72/IoReportDetectedDevice_function_00725CD0.md) at `0x007264AF`
- [PiDevCfgProcessDeviceCallback](../../page/73/PiDevCfgProcessDeviceCallback_function_00734080.md) at `0x007341FF`
- [PiControlGetUserFlagsFromDeviceNode](../../page/8E/PiControlGetUserFlagsFromDeviceNode_function_008E5888.md) at `0x008E589D`
- [PnpProcessQueryRemoveAndEject](../../page/A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) at `0x00A0558C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004708D4  48 83 EC 28                     sub rsp, 0x28
004708D8  48 8B D1                        mov rdx, rcx
004708DB  8B 89 2C 01 00 00               mov ecx, dword ptr [rcx + 0x12c]
004708E1  8B 92 30 01 00 00               mov edx, dword ptr [rdx + 0x130]
004708E7  E8 0C 00 00 00                  call 0x1404708f8
004708EC  48 83 C4 28                     add rsp, 0x28
004708F0  C3                              ret
004708F1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipAreDriversLoaded(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PipAreDriversLoadedWorker((unsigned int)(*(unsigned int *)(a1 + 300)), (unsigned int)(*(unsigned int *)(a1 + 304)), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipAreDriversLoaded(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PipAreDriversLoadedWorker((uint32_t)(*(uint32_t *)(arg1 + 0x12C)), (uint32_t)(*(uint32_t *)(arg1 + 0x130)), a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x12C` | `32` | `R` |
| `Arg1` | `+ 0x130` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004708D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004708D4[BB_004708D4]
  bb_004708F1[BB_004708F1]
```
