# EtwpGetProcessStartKey

- RVA: `0x00459180`–`0x00459199` (길이 `25` bytes)
- VA: `0x0000000140459180`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwpInitStateChangeInfo](../../page/8A/EtwpInitStateChangeInfo_function_008A48D4.md) at `0x008A493B`
- [EtwQueryProcessTelemetryInfo](../../page/8A/EtwQueryProcessTelemetryInfo_function_008A51A0.md) at `0x008A53A0`
- [EtwpWriteProcessStarted](../../page/A4/EtwpWriteProcessStarted_function_00A487A4.md) at `0x00A488B7`
- [EtwpWriteAppStateChangeWithStats](../../page/A5/EtwpWriteAppStateChangeWithStats_function_00A55F7C.md) at `0x00A55FFA`
- [NtTerminateProcess](../../page/AE/NtTerminateProcess_function_00AEC320.md) at `0x00AEC3FE`
- [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) at `0x00AF3FDC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00459180  48 B8 C4 02 00 00 80 F7 FF FF   movabs rax, 0xfffff780000002c4
0045918A  8B 00                           mov eax, dword ptr [rax]
0045918C  48 C1 E0 30                     shl rax, 0x30
00459190  48 0B 81 78 06 00 00            or rax, qword ptr [rcx + 0x678]
00459197  C3                              ret
00459198  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpGetProcessStartKey(__int64 a1)
{
    __int64 result;

    result = ((unsigned int)(*(unsigned int *)(result))) << (48);
    result = (result) | (*(unsigned __int64 *)(a1 + 1656));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpGetProcessStartKey(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = ((uint32_t)(*(uint32_t *)(result))) << (48);
    result = (result) | (*(uint64_t *)(arg1 + 0x678));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x678` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00459180&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00459180[BB_00459180]
  bb_00459198[BB_00459198]
```
