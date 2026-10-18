# PnpDeleteDeviceActionRequest

- RVA: `0x00955284`–`0x009552BC` (길이 `56` bytes)
- VA: `0x0000000140955284`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0095529E` → [PiPdcDeactivate](PiPdcDeactivate_function_009552C4.md) (function, `0x009552C4`)
- `0x009552B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PnpDeviceActionWorker](../../text/47/PnpDeviceActionWorker_function_00478400.md) at `0x00478824`
- [PnpRemoveDeviceActionRequests](../../text/4E/PnpRemoveDeviceActionRequests_function_004E89A4.md) at `0x004E8B67`
- [PnpRemoveDeviceActionRequestFromQueue](../../text/5A/PnpRemoveDeviceActionRequestFromQueue_function_005A83E0.md) at `0x005A84F3`
- [PiCMDeviceAction](../96/PiCMDeviceAction_function_0096488C.md) at `0x00964AB6`
- [PiQueueDeviceRequest](../AD/PiQueueDeviceRequest_function_00AD1878.md) at `0x00AD19AC`
- [sub_00B1D2FE](../B1/Unknown_function_00B1D2FE.md) at `0x00B1D458`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009552B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00955284  40 53                           push rbx
00955286  48 83 EC 20                     sub rsp, 0x20
0095528A  48 8B D9                        mov rbx, rcx
0095528D  83 C8 FF                        or eax, 0xffffffff
00955290  F0 0F C1 41 50                  lock xadd dword ptr [rcx + 0x50], eax
00955295  83 F8 01                        cmp eax, 1
00955298  75 1B                           jne 0x1409552b5
0095529A  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
0095529E  E8 21 00 00 00                  call 0x1409552c4
009552A3  48 83 63 20 00                  and qword ptr [rbx + 0x20], 0
009552A8  BA 50 6E 70 32                  mov edx, 0x32706e50
009552AD  48 8B CB                        mov rcx, rbx
009552B0  E8 BB D5 22 00                  call 0x140b82870
009552B5  48 83 C4 20                     add rsp, 0x20
009552B9  5B                              pop rbx
009552BA  C3                              ret
009552BB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpDeleteDeviceActionRequest(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) == 1) {
        a1 = *(unsigned __int64 *)(a1 + 32);
        result = PiPdcDeactivate(a1, a2, a3, a4);
        a2 = 0x32706E50ULL;
        a1 = a1;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpDeleteDeviceActionRequest(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) == 1) {
        Arg1 = *(uint64_t *)(arg1 + 0x20);
        result = PiPdcDeactivate(Arg1, a2, a3, a4);
        a2 = 0x32706E50ULL;
        Arg1 = Arg1;
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R/W` |
| `Arg1` | `+ 0x50` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00955284&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00955284[BB_00955284]
  bb_0095529A[BB_0095529A]
  bb_009552B5[BB_009552B5]
  bb_009552BB[BB_009552BB]
  bb_00955284 -->|branch| bb_009552B5
  bb_00955284 -->|fallthrough| bb_0095529A
  bb_0095529A -->|flow| bb_009552B5
```
