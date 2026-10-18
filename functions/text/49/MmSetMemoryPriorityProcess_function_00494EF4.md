# MmSetMemoryPriorityProcess

- RVA: `0x00494EF4`–`0x00494F31` (길이 `61` bytes)
- VA: `0x0000000140494EF4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `16`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00494F0B` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00494F20` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [PspComputeQuantumAndPriority](../../page/A3/PspComputeQuantumAndPriority_function_00A3BFB0.md) at `0x00A3BFF9`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5933`

### Static image references
- `0x00494F04` → RVA `0x00E374C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00494EF4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00494EF9  57                              push rdi
00494EFA  48 83 EC 20                     sub rsp, 0x20
00494EFE  48 8B D9                        mov rbx, rcx
00494F01  40 8A FA                        mov dil, dl
00494F04  48 8D 0D B5 25 9A 00            lea rcx, [rip + 0x9a25b5]
00494F0B  E8 80 37 DB FF                  call 0x140248690
00494F10  8A D0                           mov dl, al
00494F12  40 88 BB BA 04 00 00            mov byte ptr [rbx + 0x4ba], dil
00494F19  48 8D 0D A0 25 9A 00            lea rcx, [rip + 0x9a25a0]
00494F20  E8 9B 33 DB FF                  call 0x1402482c0
00494F25  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00494F2A  48 83 C4 20                     add rsp, 0x20
00494F2E  5F                              pop rdi
00494F2F  C3                              ret
00494F30  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmSetMemoryPriorityProcess(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAcquireSpinLockExclusive(v_rip + 10102197, a2, a3, a4);
    *(unsigned __int8 *)(a1 + 1210) = a2;
    result = MiReleaseSpinLockExclusive(v_rip + 10102176, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmSetMemoryPriorityProcess(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAcquireSpinLockExclusive(v_rip + 10102197, Arg2, a3, a4);
    *(uint8_t *)(arg1 + 0x4BA) = Arg2;
    result = MiReleaseSpinLockExclusive(v_rip + 10102176, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4BA` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00494EF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00494EF4[BB_00494EF4]
  bb_00494F30[BB_00494F30]
```
