# PnpProcessCustomDeviceEvent

- RVA: `0x00954734`–`0x00954789` (길이 `85` bytes)
- VA: `0x0000000140954734`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `23`개 명령, `85/85` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00954757` → [PiDcHandleCustomDeviceEvent](PiDcHandleCustomDeviceEvent_function_00954C14.md) (function, `0x00954C14`)
- `0x0095475F` → [PiUEventNotifyUserMode](PiUEventNotifyUserMode_function_00954CB4.md) (function, `0x00954CB4`)
- `0x00954771` → [PnpNotifyTargetDeviceChange](PnpNotifyTargetDeviceChange_function_00954790.md) (function, `0x00954790`)

### Direct callers
- [PnpDeviceEventWorker](PnpDeviceEventWorker_function_009556B0.md) at `0x009558EC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00954734  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00954739  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0095473E  57                              push rdi
0095473F  48 83 EC 20                     sub rsp, 0x20
00954743  48 8B 19                        mov rbx, qword ptr [rcx]
00954746  48 8B CB                        mov rcx, rbx
00954749  48 8B B3 A0 00 00 00            mov rsi, qword ptr [rbx + 0xa0]
00954750  48 8B BB A8 00 00 00            mov rdi, qword ptr [rbx + 0xa8]
00954757  E8 B8 04 00 00                  call 0x140954c14
0095475C  48 8B CB                        mov rcx, rbx
0095475F  E8 50 05 00 00                  call 0x140954cb4
00954764  48 8D 4F 04                     lea rcx, [rdi + 4]
00954768  45 33 C9                        xor r9d, r9d
0095476B  4C 8B C7                        mov r8, rdi
0095476E  48 8B D6                        mov rdx, rsi
00954771  E8 1A 00 00 00                  call 0x140954790
00954776  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0095477B  33 C0                           xor eax, eax
0095477D  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00954782  48 83 C4 20                     add rsp, 0x20
00954786  5F                              pop rdi
00954787  C3                              ret
00954788  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpProcessCustomDeviceEvent(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = PiDcHandleCustomDeviceEvent(*(unsigned __int64 *)(a1), a2, a3, a4);
    result = PiUEventNotifyUserMode(*(unsigned __int64 *)(a1), a2, a3, a4);
    a4 = 0;
    result = PnpNotifyTargetDeviceChange(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 168) + 4, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 160), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 168), a4);
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpProcessCustomDeviceEvent(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = PiDcHandleCustomDeviceEvent(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
    result = PiUEventNotifyUserMode(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
    Arg4 = 0;
    result = PnpNotifyTargetDeviceChange(*(uint64_t *)(*(uint64_t *)(arg1) + 0xA8) + 4, *(uint64_t *)(*(uint64_t *)(arg1) + 0xA0), *(uint64_t *)(*(uint64_t *)(arg1) + 0xA8), Arg4);
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00954734&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00954734[BB_00954734]
  bb_00954788[BB_00954788]
```
