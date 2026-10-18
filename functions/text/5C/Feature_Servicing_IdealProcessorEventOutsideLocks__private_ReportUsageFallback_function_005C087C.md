# Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportUsageFallback

- RVA: `0x005C087C`–`0x005C08C9` (길이 `77` bytes)
- VA: `0x00000001405C087C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000805BC`
- 디코드: `21`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005C08A2` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x005C08BD` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)

### Direct callers
- [Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportDeviceUsage](../30/Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportDeviceUsage_function_00305020.md) at `0x00305048`

### Static image references
- `0x005C088B` → RVA `0x000DE708` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C087C  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005C0881  53                              push rbx
005C0882  48 83 EC 20                     sub rsp, 0x20
005C0886  83 4C 24 30 01                  or dword ptr [rsp + 0x30], 1
005C088B  48 8D 0D 76 DE B1 FF            lea rcx, [rip - 0x4e218a]
005C0892  8B DA                           mov ebx, edx
005C0894  44 8B C2                        mov r8d, edx
005C0897  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
005C089C  41 B9 01 00 00 00               mov r9d, 1
005C08A2  E8 3D DE F7 FF                  call 0x14053e6e4
005C08A7  8D 43 FD                        lea eax, [rbx - 3]
005C08AA  83 F8 01                        cmp eax, 1
005C08AD  77 13                           ja 0x1405c08c2
005C08AF  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005C08B4  4C 8D 05 4D DE B1 FF            lea r8, [rip - 0x4e21b3]
005C08BB  8B D3                           mov edx, ebx
005C08BD  E8 B2 DE F7 FF                  call 0x14053e774
005C08C2  48 83 C4 20                     add rsp, 0x20
005C08C6  5B                              pop rbx
005C08C7  C3                              ret
005C08C8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportUsageFallback(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (32);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5120394, v_stack_p8, (unsigned int)(a2), 1);
    result = (unsigned int)(a2) - 3;
    if (((unsigned int)((unsigned int)(a2) - 3)) <= 1) {
        a1 = v_stack_p8;
        a3 = v_rip - 5120435;
        a2 = (unsigned int)((unsigned int)(a2));
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(a1, a2, a3, 1);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportUsageFallback(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (32);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5120394, v_stack_p8, (uint32_t)(Arg2), 1);
    result = (uint32_t)(Arg2) - 3;
    if (((uint32_t)((uint32_t)(Arg2) - 3)) <= 1) {
        Arg1 = v_stack_p8;
        a3 = v_rip - 5120435;
        Arg2 = (uint32_t)((uint32_t)(Arg2));
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(Arg1, Arg2, a3, 1);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x3` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C087C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C087C[BB_005C087C]
  bb_005C08AF[BB_005C08AF]
  bb_005C08C2[BB_005C08C2]
  bb_005C08C8[BB_005C08C8]
  bb_005C087C -->|branch| bb_005C08C2
  bb_005C087C -->|fallthrough| bb_005C08AF
  bb_005C08AF -->|flow| bb_005C08C2
```
