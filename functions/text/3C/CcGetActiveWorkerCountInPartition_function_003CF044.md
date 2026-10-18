# CcGetActiveWorkerCountInPartition

- RVA: `0x003CF044`–`0x003CF069` (길이 `37` bytes)
- VA: `0x00000001403CF044`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003CF05C` → [CcForEachNumaNode](CcForEachNumaNode_function_003CF070.md) (function, `0x003CF070`)

### Direct callers
- [CcPrivateVolumeCacheMapTelemetryCallback](../../page/A7/CcPrivateVolumeCacheMapTelemetryCallback_function_00A78FF0.md) at `0x00A79048`
- [CcPartitionTelemetryCallback](../../page/A9/CcPartitionTelemetryCallback_function_00A95010.md) at `0x00A950B3`

### Static image references
- `0x003CF055` → RVA `0x004DB4F0` (`CcGetActiveWorkerCountPerNode`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003CF044  48 83 EC 28                     sub rsp, 0x28
003CF048  49 83 20 00                     and qword ptr [r8], 0
003CF04C  4D 8B C8                        mov r9, r8
003CF04F  4C 8B C2                        mov r8, rdx
003CF052  48 8B D1                        mov rdx, rcx
003CF055  48 8D 0D 94 C4 10 00            lea rcx, [rip + 0x10c494]
003CF05C  E8 0F 00 00 00                  call 0x1403cf070
003CF061  B0 01                           mov al, 1
003CF063  48 83 C4 28                     add rsp, 0x28
003CF067  C3                              ret
003CF068  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcGetActiveWorkerCountInPartition(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = CcForEachNumaNode(v_rip + 1098900, a1, a2, a3);
    v_rsp = (v_rsp) + (40);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t CcGetActiveWorkerCountInPartition(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = CcForEachNumaNode(v_rip + 1098900, Arg1, Arg2, Arg3);
    local_rsp = (local_rsp) + (40);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003CF044&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003CF044[BB_003CF044]
  bb_003CF068[BB_003CF068]
```
