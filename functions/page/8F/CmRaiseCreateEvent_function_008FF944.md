# CmRaiseCreateEvent

- RVA: `0x008FF944`–`0x008FF9C3` (길이 `127` bytes)
- VA: `0x00000001408FF944`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000883BC`
- 디코드: `35`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008FF96C` → [_CmMapCmObjectTypeToPnpObjectType](_CmMapCmObjectTypeToPnpObjectType_function_008FF060.md) (function, `0x008FF060`)
- `0x008FF977` → [PnpObjectRaiseCreateEvent](PnpObjectRaiseCreateEvent_function_008FF9CC.md) (function, `0x008FF9CC`)
- `0x008FF9BC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [CmCreateInstallerClassWorker](../82/CmCreateInstallerClassWorker_function_00829700.md) at `0x0082977E`
- [CmCreateDevicePanelWorker](../82/CmCreateDevicePanelWorker_function_0082E240.md) at `0x0082E2BE`
- [_CmCreateDeviceContainerWorker](_CmCreateDeviceContainerWorker_function_008FF898.md) at `0x008FF935`
- [CmCreateDeviceWorker](CmCreateDeviceWorker_function_008FFC3C.md) at `0x008FFCD5`
- [CmCreateDeviceInterfaceWorker](../90/CmCreateDeviceInterfaceWorker_function_009016E4.md) at `0x009017DA`
- [_CmCreateInterfaceClassWorker](../90/_CmCreateInterfaceClassWorker_function_009019CC.md) at `0x00901A70`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008FF9BC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008FF944  48 8B C4                        mov rax, rsp
008FF947  48 89 58 08                     mov qword ptr [rax + 8], rbx
008FF94B  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
008FF94F  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
008FF953  57                              push rdi
008FF954  48 83 EC 40                     sub rsp, 0x40
008FF958  48 83 60 F0 00                  and qword ptr [rax - 0x10], 0
008FF95D  48 8B D9                        mov rbx, rcx
008FF960  41 8B C8                        mov ecx, r8d
008FF963  49 8B F9                        mov rdi, r9
008FF966  41 8B F0                        mov esi, r8d
008FF969  48 8B EA                        mov rbp, rdx
008FF96C  E8 EF F6 FF FF                  call 0x1408ff060
008FF971  44 8B C0                        mov r8d, eax
008FF974  48 8B CB                        mov rcx, rbx
008FF977  E8 50 00 00 00                  call 0x1408ff9cc
008FF97C  48 8B 83 00 02 00 00            mov rax, qword ptr [rbx + 0x200]
008FF983  48 85 C0                        test rax, rax
008FF986  75 16                           jne 0x1408ff99e
008FF988  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
008FF98D  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
008FF992  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
008FF997  48 83 C4 40                     add rsp, 0x40
008FF99B  5F                              pop rdi
008FF99C  C3                              ret
008FF99D  CC                              int3
008FF99E  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
008FF9A3  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008FF9A8  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008FF9AD  41 B9 02 00 00 00               mov r9d, 2
008FF9B3  48 8B CB                        mov rcx, rbx
008FF9B6  44 8B C6                        mov r8d, esi
008FF9B9  48 8B D5                        mov rdx, rbp
008FF9BC  E8 0F B1 DB FF                  call 0x1406baad0
008FF9C1  EB C5                           jmp 0x1408ff988
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmRaiseCreateEvent(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = _CmMapCmObjectTypeToPnpObjectType((unsigned int)(a3), a2, a3, a4);
    result = PnpObjectRaiseCreateEvent(a1, a2, (unsigned int)((unsigned int)(result)), a4);
    if (*(unsigned __int64 *)(a1 + 512) != 0) goto loc_008FF99E;
loc_008FF988:
    v_rsp = (v_rsp) + (64);
    return *(unsigned __int64 *)(a1 + 512);
loc_008FF99E:
    v_stack_p30 = a4;
    v_stack_p20 = v_stack_p30;
    result = guard_dispatch_icall(v_stack_p8, v_stack_p10, (unsigned int)((unsigned int)(v_stack_p18)), 2);
    goto loc_008FF988;
}
```

## 5. (Beta) C Style

```c
int64_t CmRaiseCreateEvent(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = _CmMapCmObjectTypeToPnpObjectType((uint32_t)(Arg3), Arg2, Arg3, Arg4);
    result = PnpObjectRaiseCreateEvent(Arg1, Arg2, (uint32_t)((uint32_t)(result)), Arg4);
    if (*(uint64_t *)(arg1 + 0x200) != 0) goto loc_008FF99E;
loc_008FF988:
    local_rsp = (local_rsp) + (64);
    return *(uint64_t *)(arg1 + 0x200);
loc_008FF99E:
    v_stack_p30 = Arg4;
    v_stack_p20 = v_stack_p30;
    result = guard_dispatch_icall(v_stack_p8, v_stack_p10, (uint32_t)((uint32_t)(v_stack_p18)), 2);
    goto loc_008FF988;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x200` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008FF944&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008FF944[BB_008FF944]
  bb_008FF988[BB_008FF988]
  bb_008FF99D[BB_008FF99D]
  bb_008FF99E[BB_008FF99E]
  bb_008FF944 -->|branch| bb_008FF99E
  bb_008FF944 -->|fallthrough| bb_008FF988
  bb_008FF99D -->|flow| bb_008FF99E
  bb_008FF99E -->|branch| bb_008FF988
```
