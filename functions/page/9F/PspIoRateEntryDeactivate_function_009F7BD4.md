# PspIoRateEntryDeactivate

- RVA: `0x009F7BD4`–`0x009F7C19` (길이 `69` bytes)
- VA: `0x00000001409F7BD4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C670`
- 디코드: `20`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009F7BE1` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (function, `0x002A4CB0`)
- `0x009F7BEA` → [IoStopIoRateControl](../../text/42/IoStopIoRateControl_function_0042867C.md) (function, `0x0042867C`)
- `0x009F7C04` → [IoStopDiskIoAttributionForContext](../../text/2A/IoStopDiskIoAttributionForContext_function_002A5614.md) (function, `0x002A5614`)
- `0x009F7C0D` → [IoDiskIoAttributionDereference](../../text/34/IoDiskIoAttributionDereference_function_00349978.md) (function, `0x00349978`)

### Direct callers
- [PspSetJobIoRateControl](PspSetJobIoRateControl_function_009F78EC.md) at `0x009F7A53`
- [PspSetJobIoRateControlForVolume](PspSetJobIoRateControlForVolume_function_009F80A0.md) at `0x009F8136`
- [PspSetJobIoRateControlForVolume](PspSetJobIoRateControlForVolume_function_009F80A0.md) at `0x009F8178`
- [PspIoRateEntryActivate](PspIoRateEntryActivate_function_009F8398.md) at `0x009F848F`
- [PspJobIoRateControlDisable](../A7/PspJobIoRateControlDisable_function_00A76854.md) at `0x00A768B1`
- [PspJobIoRateControlDisable](../A7/PspJobIoRateControlDisable_function_00A76854.md) at `0x00A768EA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x009F7BE1` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (`PAGE` → `.text`)
  - `0x009F7BEA` → [IoStopIoRateControl](../../text/42/IoStopIoRateControl_function_0042867C.md) (`PAGE` → `.text`)
  - `0x009F7C04` → [IoStopDiskIoAttributionForContext](../../text/2A/IoStopDiskIoAttributionForContext_function_002A5614.md) (`PAGE` → `.text`)
  - `0x009F7C0D` → [IoDiskIoAttributionDereference](../../text/34/IoDiskIoAttributionDereference_function_00349978.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F7BD4  40 53                           push rbx
009F7BD6  48 83 EC 20                     sub rsp, 0x20
009F7BDA  48 8B D9                        mov rbx, rcx
009F7BDD  48 83 C1 20                     add rcx, 0x20
009F7BE1  E8 CA D0 8A FF                  call 0x1402a4cb0
009F7BE6  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
009F7BEA  E8 8D 0A A3 FF                  call 0x14042867c
009F7BEF  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
009F7BF3  48 83 63 28 00                  and qword ptr [rbx + 0x28], 0
009F7BF8  48 85 C9                        test rcx, rcx
009F7BFB  75 07                           jne 0x1409f7c04
009F7BFD  48 83 C4 20                     add rsp, 0x20
009F7C01  5B                              pop rbx
009F7C02  C3                              ret
009F7C03  CC                              int3
009F7C04  E8 0B DA 8A FF                  call 0x1402a5614
009F7C09  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
009F7C0D  E8 66 1D 95 FF                  call 0x140349978
009F7C12  48 83 63 30 00                  and qword ptr [rbx + 0x30], 0
009F7C17  EB E4                           jmp 0x1409f7bfd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspIoRateEntryDeactivate(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (32);
    result = ExWaitForRundownProtectionRelease(a1, a2, a3, a4);
    result = IoStopIoRateControl(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 48) != 0) goto loc_009F7C04;
loc_009F7BFD:
    v_rsp = (v_rsp) + (32);
    return result;
loc_009F7C04:
    result = IoStopDiskIoAttributionForContext(*(unsigned __int64 *)(a1 + 48), a2, a3, a4);
    result = IoDiskIoAttributionDereference(*(unsigned __int64 *)(a1 + 48), a2, a3, a4);
    goto loc_009F7BFD;
}
```

## 5. (Beta) C Style

```c
int64_t PspIoRateEntryDeactivate(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (32);
    result = ExWaitForRundownProtectionRelease(Arg1, a2, a3, a4);
    result = IoStopIoRateControl(*(uint64_t *)(arg1 + 0x28), a2, a3, a4);
    if (*(uint64_t *)(arg1 + 0x30) != 0) goto loc_009F7C04;
loc_009F7BFD:
    local_rsp = (local_rsp) + (32);
    return result;
loc_009F7C04:
    result = IoStopDiskIoAttributionForContext(*(uint64_t *)(arg1 + 0x30), a2, a3, a4);
    result = IoDiskIoAttributionDereference(*(uint64_t *)(arg1 + 0x30), a2, a3, a4);
    goto loc_009F7BFD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R/W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F7BD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009F7BD4[BB_009F7BD4]
  bb_009F7BFD[BB_009F7BFD]
  bb_009F7C03[BB_009F7C03]
  bb_009F7C04[BB_009F7C04]
  bb_009F7BD4 -->|branch| bb_009F7C04
  bb_009F7BD4 -->|fallthrough| bb_009F7BFD
  bb_009F7C03 -->|flow| bb_009F7C04
  bb_009F7C04 -->|branch| bb_009F7BFD
```
