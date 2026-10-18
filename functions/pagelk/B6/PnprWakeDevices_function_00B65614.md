# PnprWakeDevices

- RVA: `0x00B65614`–`0x00B6568B` (길이 `119` bytes)
- VA: `0x0000000140B65614`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `31`개 명령, `119/119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B65623` → [PnprGetMillisecondCounter](PnprGetMillisecondCounter_function_00B63FD4.md) (function, `0x00B63FD4`)
- `0x00B6563D` → [PoBroadcastSystemState](../B7/PoBroadcastSystemState_function_00B761B0.md) (function, `0x00B761B0`)
- `0x00B65642` → [PoClearBroadcast](../../page/AA/PoClearBroadcast_function_00AA3CE8.md) (function, `0x00AA3CE8`)
- `0x00B65651` → [PoEndPartitionReplace](../../page/75/PoEndPartitionReplace_function_0075E554.md) (function, `0x0075E554`)
- `0x00B65659` → [PoEndPowerStateTasks](../../page/70/PoEndPowerStateTasks_function_00702130.md) (function, `0x00702130`)
- `0x00B65664` → [PoUnblockConsoleSwitch](../../page/AD/PoUnblockConsoleSwitch_function_00ADB8A0.md) (function, `0x00ADB8A0`)
- `0x00B6566B` → [PnprGetMillisecondCounter](PnprGetMillisecondCounter_function_00B63FD4.md) (function, `0x00B63FD4`)

### Direct callers
- [PnpReplacePartitionUnit](../../page/73/PnpReplacePartitionUnit_function_00738550.md) at `0x00738AFB`
- [PnprQuiesceWorker](PnprQuiesceWorker_function_00B654E0.md) at `0x00B655BA`

### Static image references
- `0x00B65628` → RVA `0x00F8AC38` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00B65642` → [PoClearBroadcast](../../page/AA/PoClearBroadcast_function_00AA3CE8.md) (`PAGELK` → `PAGE`)
  - `0x00B65651` → [PoEndPartitionReplace](../../page/75/PoEndPartitionReplace_function_0075E554.md) (`PAGELK` → `PAGE`)
  - `0x00B65659` → [PoEndPowerStateTasks](../../page/70/PoEndPowerStateTasks_function_00702130.md) (`PAGELK` → `PAGE`)
  - `0x00B65664` → [PoUnblockConsoleSwitch](../../page/AD/PoUnblockConsoleSwitch_function_00ADB8A0.md) (`PAGELK` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B65614  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B65619  57                              push rdi
00B6561A  48 83 EC 20                     sub rsp, 0x20
00B6561E  48 8B F9                        mov rdi, rcx
00B65621  33 C9                           xor ecx, ecx
00B65623  E8 AC E9 FF FF                  call 0x140b63fd4
00B65628  48 8B 15 09 56 42 00            mov rdx, qword ptr [rip + 0x425609]
00B6562F  48 8D 4F 04                     lea rcx, [rdi + 4]
00B65633  89 82 38 82 00 00               mov dword ptr [rdx + 0x8238], eax
00B65639  C6 47 1D 01                     mov byte ptr [rdi + 0x1d], 1
00B6563D  E8 6E 0B 01 00                  call 0x140b761b0
00B65642  E8 A1 E6 F3 FF                  call 0x140aa3ce8
00B65647  8B 57 20                        mov edx, dword ptr [rdi + 0x20]
00B6564A  48 8D 5F 28                     lea rbx, [rdi + 0x28]
00B6564E  48 8B CB                        mov rcx, rbx
00B65651  E8 FE 8E BF FF                  call 0x14075e554
00B65656  48 8B CB                        mov rcx, rbx
00B65659  E8 D2 CA B9 FF                  call 0x140702130
00B6565E  8B 57 20                        mov edx, dword ptr [rdi + 0x20]
00B65661  48 8B CB                        mov rcx, rbx
00B65664  E8 37 62 F7 FF                  call 0x140adb8a0
00B65669  33 C9                           xor ecx, ecx
00B6566B  E8 64 E9 FF FF                  call 0x140b63fd4
00B65670  48 8B 0D C1 55 42 00            mov rcx, qword ptr [rip + 0x4255c1]
00B65677  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00B6567C  89 81 3C 82 00 00               mov dword ptr [rcx + 0x823c], eax
00B65682  33 C0                           xor eax, eax
00B65684  48 83 C4 20                     add rsp, 0x20
00B65688  5F                              pop rdi
00B65689  C3                              ret
00B6568A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnprWakeDevices(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = PnprGetMillisecondCounter(a1, a2, a3, a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4347401) + 33336) = (unsigned int)(result);
    *(unsigned __int8 *)(a1 + 29) = 1;
    result = PoBroadcastSystemState(a1 + 4, *(unsigned __int64 *)(v_rip + 4347401), a3, a4);
    result = PoClearBroadcast(a1 + 4, *(unsigned __int64 *)(v_rip + 4347401), a3, a4);
    result = PoEndPartitionReplace(a1 + 40, (unsigned int)(*(unsigned int *)(a1 + 32)), a3, a4);
    result = PoEndPowerStateTasks(a1 + 40, (unsigned int)(*(unsigned int *)(a1 + 32)), a3, a4);
    result = PoUnblockConsoleSwitch(a1 + 40, (unsigned int)(*(unsigned int *)(a1 + 32)), a3, a4);
    a1 = 0;
    result = PnprGetMillisecondCounter(a1, (unsigned int)(*(unsigned int *)(a1 + 32)), a3, a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4347329) + 33340) = (unsigned int)(result);
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnprWakeDevices(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = PnprGetMillisecondCounter(Arg1, a2, a3, a4);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x425609) + 0x8238) = (uint32_t)(result);
    *(uint8_t *)(arg1 + 0x1D) = 1;
    result = PoBroadcastSystemState(Arg1 + 4, *(uint64_t *)(v_rip + 0x425609), a3, a4);
    result = PoClearBroadcast(Arg1 + 4, *(uint64_t *)(v_rip + 0x425609), a3, a4);
    result = PoEndPartitionReplace(Arg1 + 40, (uint32_t)(*(uint32_t *)(arg1 + 0x20)), a3, a4);
    result = PoEndPowerStateTasks(Arg1 + 40, (uint32_t)(*(uint32_t *)(arg1 + 0x20)), a3, a4);
    result = PoUnblockConsoleSwitch(Arg1 + 40, (uint32_t)(*(uint32_t *)(arg1 + 0x20)), a3, a4);
    Arg1 = 0;
    result = PnprGetMillisecondCounter(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x20)), a3, a4);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x4255C1) + 0x823C) = (uint32_t)(result);
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `64` | `R` |
| `Arg1` | `+ 0x1D` | `8` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B65614&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B65614[BB_00B65614]
  bb_00B6568A[BB_00B6568A]
```
