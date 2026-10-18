# ObpHandleRevocationBlockRemoveObject

- RVA: `0x009D7E30`–`0x009D7E4F` (길이 `31` bytes)
- VA: `0x00000001409D7E30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **18**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009D7E44` → [ObpHandleRevocationBlockRemoveInsertedObject](ObpHandleRevocationBlockRemoveInsertedObject_function_009D7E58.md) (function, `0x009D7E58`)

### Direct callers
- [IoRemoveIoCompletion](../../text/20/IoRemoveIoCompletion_function_0020B580.md) at `0x0020BBBD`
- [IoRemoveIoCompletion](../../text/20/IoRemoveIoCompletion_function_0020B580.md) at `0x0020BC44`
- [IoRemoveIoCompletion](../../text/20/IoRemoveIoCompletion_function_0020B580.md) at `0x0020BCCD`
- [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) at `0x00250E19`
- [NtSetInformationFile](../../text/29/NtSetInformationFile_function_0029C5E0.md) at `0x0029D1D6`
- [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) at `0x002F7A8B`
- [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) at `0x002F948D`
- [NtTraceEvent](../../text/2F/NtTraceEvent_function_002FA6C0.md) at `0x002FAE1F`
- [PfSnGetFileInformation](../../text/34/PfSnGetFileInformation_function_00343210.md) at `0x00343673`
- [sub_00343D34](../../text/34/Unknown_function_00343D34.md) at `0x00343DAE`
- [IopFreeWaitCompletionPacket](../../text/35/IopFreeWaitCompletionPacket_function_00351A50.md) at `0x00351D95`
- [IopFreeWaitCompletionPacket](../../text/35/IopFreeWaitCompletionPacket_function_00351A50.md) at `0x00351E13`
- [IopFreeWaitCompletionPacket](../../text/35/IopFreeWaitCompletionPacket_function_00351A50.md) at `0x00351E90`
- [sub_0038C58B](../../text/38/Unknown_function_0038C58B.md) at `0x0038C7B3`
- [sub_00393FDE](../../text/39/Unknown_function_00393FDE.md) at `0x00394087`
- [sub_00393FDE](../../text/39/Unknown_function_00393FDE.md) at `0x00394104`
- [NtWaitForWorkViaWorkerFactory](../../text/39/NtWaitForWorkViaWorkerFactory_function_00394270.md) at `0x00394E0D`
- [ObpDereferenceNamedObject](../../text/3A/ObpDereferenceNamedObject_function_003A0310.md) at `0x003A040B`
- [ExpSetTimerObject2](../../text/3A/ExpSetTimerObject2_function_003A0658.md) at `0x003A07BF`
- [NtSignalAndWaitForSingleObject](../../text/3A/NtSignalAndWaitForSingleObject_function_003A11D0.md) at `0x003A15D1`
- [NtSignalAndWaitForSingleObject](../../text/3A/NtSignalAndWaitForSingleObject_function_003A11D0.md) at `0x003A161F`
- [IopUnloadSafeCompletion](../../text/3A/IopUnloadSafeCompletion_function_003A16A0.md) at `0x003A17E8`
- [sub_003ED730](../../text/3E/Unknown_function_003ED730.md) at `0x003ED753`
- [ObpProcessRemoveObjectQueue](ObpProcessRemoveObjectQueue_function_009D7B40.md) at `0x009D7D04`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009D7E30  48 83 EC 28                     sub rsp, 0x28
009D7E34  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
009D7E38  48 83 FA 02                     cmp rdx, 2
009D7E3C  76 0B                           jbe 0x1409d7e49
009D7E3E  45 33 C9                        xor r9d, r9d
009D7E41  45 33 C0                        xor r8d, r8d
009D7E44  E8 0F 00 00 00                  call 0x1409d7e58
009D7E49  48 83 C4 28                     add rsp, 0x28
009D7E4D  C3                              ret
009D7E4E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpHandleRevocationBlockRemoveObject(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int64 *)(a1 + 16)) >= = 2) {
        a4 = 0;
        a3 = 0;
        result = ObpHandleRevocationBlockRemoveInsertedObject(a1, *(unsigned __int64 *)(a1 + 16), a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObpHandleRevocationBlockRemoveObject(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint64_t *)(arg1 + 0x10)) >= = 2) {
        Arg4 = 0;
        Arg3 = 0;
        result = ObpHandleRevocationBlockRemoveInsertedObject(Arg1, *(uint64_t *)(arg1 + 0x10), Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009D7E30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009D7E30[BB_009D7E30]
  bb_009D7E3E[BB_009D7E3E]
  bb_009D7E49[BB_009D7E49]
  bb_009D7E4E[BB_009D7E4E]
  bb_009D7E30 -->|branch| bb_009D7E49
  bb_009D7E30 -->|fallthrough| bb_009D7E3E
  bb_009D7E3E -->|flow| bb_009D7E49
```
