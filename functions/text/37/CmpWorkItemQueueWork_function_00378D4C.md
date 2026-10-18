# CmpWorkItemQueueWork

- RVA: `0x00378D4C`–`0x00378D7C` (길이 `48` bytes)
- VA: `0x0000000140378D4C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **14**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00378D65` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00378D70` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [CmFcManagerNotifyFeatureUsage](CmFcManagerNotifyFeatureUsage_function_00378598.md) at `0x00378623`
- [CmFcpManagerDrainUsageNotificationsDpc](../4B/CmFcpManagerDrainUsageNotificationsDpc_function_004B97A0.md) at `0x004B97AB`
- [CmFcpManagerFlushUsageTimerRoutine](../4D/CmFcpManagerFlushUsageTimerRoutine_function_004DCA90.md) at `0x004DCAC0`
- [CmpNotifyMachineHiveLoaded](../66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) at `0x0066A4D0`
- [CmFcpManagerPublishFeatureUsageDataIfNearCapacityDpc](../66/CmFcpManagerPublishFeatureUsageDataIfNearCapacityDpc_function_0066B350.md) at `0x0066B383`
- [CmFcpManagerPublishUsageTimerRoutine](../66/CmFcpManagerPublishUsageTimerRoutine_function_0066B3A0.md) at `0x0066B3AB`
- [CmFcpManagerRetryUsageNotificationsTimerRoutine](../66/CmFcpManagerRetryUsageNotificationsTimerRoutine_function_0066B3C0.md) at `0x0066B3CB`
- [sub_006F7E00](../6F/Unknown_function_006F7E00.md) at `0x006F7E3C`
- [CmRegisterMachineHiveLoadedNotification](../../page/7E/CmRegisterMachineHiveLoadedNotification_function_007E1A90.md) at `0x007E1BD5`
- [CmFcpManagerPublishChangeNotifications](../../page/A4/CmFcpManagerPublishChangeNotifications_function_00A44E94.md) at `0x00A44F88`
- [CmFcManagerRegisterFeatureConfigurationChangeNotification](../../page/AB/CmFcManagerRegisterFeatureConfigurationChangeNotification_function_00AB91CC.md) at `0x00AB92B6`
- [CmFcpManagerPublishFeatureUsageData](../../page/AB/CmFcpManagerPublishFeatureUsageData_function_00ABC468.md) at `0x00ABC5B5`
- [CmFcManagerFlushFeatureUsage](../../page/AC/CmFcManagerFlushFeatureUsage_function_00AC1814.md) at `0x00AC187E`
- [CmFcManagerFlushFeatureUsage](../../page/AC/CmFcManagerFlushFeatureUsage_function_00AC1814.md) at `0x00AC18FC`
- [CmFcpManagerProcessUsageDataProviders](../../page/AF/CmFcpManagerProcessUsageDataProviders_function_00AF7B6C.md) at `0x00AF7C90`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00378D4C  40 53                           push rbx
00378D4E  48 83 EC 20                     sub rsp, 0x20
00378D52  B8 03 00 00 00                  mov eax, 3
00378D57  48 8B D9                        mov rbx, rcx
00378D5A  87 41 28                        xchg dword ptr [rcx + 0x28], eax
00378D5D  A8 01                           test al, 1
00378D5F  75 14                           jne 0x140378d75
00378D61  48 83 C1 20                     add rcx, 0x20
00378D65  E8 B6 D8 E9 FF                  call 0x140216620
00378D6A  8B 53 2C                        mov edx, dword ptr [rbx + 0x2c]
00378D6D  48 8B CB                        mov rcx, rbx
00378D70  E8 AB 07 F8 FF                  call 0x1402f9520
00378D75  48 83 C4 20                     add rsp, 0x20
00378D79  5B                              pop rbx
00378D7A  C3                              ret
00378D7B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpWorkItemQueueWork(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = 3;
    if (((3) & (1)) == 0) {
        a1 = (a1) + (32);
        result = ExAcquireRundownProtection(a1, a2, a3, a4);
        a2 = *(unsigned int *)(a1 + 44);
        a1 = a1;
        result = ExQueueWorkItem(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpWorkItemQueueWork(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = 3;
    if (((3) & (1)) == 0) {
        Arg1 = (Arg1) + (32);
        result = ExAcquireRundownProtection(Arg1, a2, a3, a4);
        a2 = *(uint32_t *)(arg1 + 0x2C);
        Arg1 = Arg1;
        result = ExQueueWorkItem(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `32` | `R/W` |
| `Arg1` | `+ 0x2C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00378D4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00378D4C[BB_00378D4C]
  bb_00378D61[BB_00378D61]
  bb_00378D75[BB_00378D75]
  bb_00378D7B[BB_00378D7B]
  bb_00378D4C -->|branch| bb_00378D75
  bb_00378D4C -->|fallthrough| bb_00378D61
  bb_00378D61 -->|flow| bb_00378D75
```
