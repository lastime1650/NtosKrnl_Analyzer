# EtwpUnreferenceDataBlock

- RVA: `0x008BFC5C`–`0x008BFC7A` (길이 `30` bytes)
- VA: `0x00000001408BFC5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008BFC6F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SendCaptureStateNotificationsWorker](../7B/SendCaptureStateNotificationsWorker_function_007BCF30.md) at `0x007BD181`
- [EtwpReceiveNotification](EtwpReceiveNotification_function_008BF9F0.md) at `0x008BFBE7`
- [EtwpRundownNotifications](../8C/EtwpRundownNotifications_function_008C1284.md) at `0x008C13E0`
- [EtwpClearSessionAndUnreferenceEntry](../8C/EtwpClearSessionAndUnreferenceEntry_function_008C1438.md) at `0x008C186A`
- [EtwpClearSessionAndUnreferenceEntry](../8C/EtwpClearSessionAndUnreferenceEntry_function_008C1438.md) at `0x008C18A6`
- [EtwpNotifyGuid](../8C/EtwpNotifyGuid_function_008C8110.md) at `0x008C8381`
- [EtwpNotifyGuid](../8C/EtwpNotifyGuid_function_008C8110.md) at `0x008C8393`
- [EtwpNotifyGuid](../8C/EtwpNotifyGuid_function_008C8110.md) at `0x008C8513`
- [EtwpNotifyDisallowedGuidChange](../9E/EtwpNotifyDisallowedGuidChange_function_009EAD14.md) at `0x009EAF81`
- [EtwpNotifyDisallowedGuidChange](../9E/EtwpNotifyDisallowedGuidChange_function_009EAD14.md) at `0x009EAFCC`
- [EtwpQueueReply](../9F/EtwpQueueReply_function_009FEDB0.md) at `0x009FEE2A`
- [EtwpEnableGuid](../A5/EtwpEnableGuid_function_00A5CD28.md) at `0x00A5D518`
- [EtwpEnableGuid](../A5/EtwpEnableGuid_function_00A5CD28.md) at `0x00A5D7D5`
- [EtwpEnableGuid](../A5/EtwpEnableGuid_function_00A5CD28.md) at `0x00A5D934`
- [EtwpEnableGuid](../A5/EtwpEnableGuid_function_00A5CD28.md) at `0x00A5D945`
- [EtwpReceiveReplyDataBlock](../A8/EtwpReceiveReplyDataBlock_function_00A87954.md) at `0x00A87A46`
- [sub_00B1AF32](../B1/Unknown_function_00B1AF32.md) at `0x00B1AF3C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008BFC6F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008BFC5C  48 83 EC 28                     sub rsp, 0x28
008BFC60  83 C8 FF                        or eax, 0xffffffff
008BFC63  F0 0F C1 41 08                  lock xadd dword ptr [rcx + 8], eax
008BFC68  83 F8 01                        cmp eax, 1
008BFC6B  75 07                           jne 0x1408bfc74
008BFC6D  33 D2                           xor edx, edx
008BFC6F  E8 FC 2B 2C 00                  call 0x140b82870
008BFC74  48 83 C4 28                     add rsp, 0x28
008BFC78  C3                              ret
008BFC79  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpUnreferenceDataBlock(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) == 1) {
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpUnreferenceDataBlock(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) == 1) {
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008BFC5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008BFC5C[BB_008BFC5C]
  bb_008BFC6D[BB_008BFC6D]
  bb_008BFC74[BB_008BFC74]
  bb_008BFC79[BB_008BFC79]
  bb_008BFC5C -->|branch| bb_008BFC74
  bb_008BFC5C -->|fallthrough| bb_008BFC6D
  bb_008BFC6D -->|flow| bb_008BFC74
```
