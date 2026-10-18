# MiLockPoolCommitWs

- RVA: `0x00469EC0`–`0x00469F06` (길이 `70` bytes)
- VA: `0x0000000140469EC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B95C`
- 디코드: `20`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00469EEB` → [MiLockWorkingSetSharedAtDpc](../23/MiLockWorkingSetSharedAtDpc_function_00239574.md) (function, `0x00239574`)
- `0x00469EFF` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [MiCommitPoolMemory](../32/MiCommitPoolMemory_function_00329520.md) at `0x00329567`
- [MiCommitPoolMemory](../32/MiCommitPoolMemory_function_00329520.md) at `0x00329699`
- [MiCommitPoolMemory](../32/MiCommitPoolMemory_function_00329520.md) at `0x00329704`
- [sub_00344F15](../34/Unknown_function_00344F15.md) at `0x003450B9`

### Static image references
- `0x00469EDA` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00469EC0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00469EC5  57                              push rdi
00469EC6  48 83 EC 20                     sub rsp, 0x20
00469ECA  48 8B D9                        mov rbx, rcx
00469ECD  44 0F 20 C7                     mov rdi, cr8
00469ED1  BA 02 00 00 00                  mov edx, 2
00469ED6  44 0F 22 C2                     mov cr8, rdx
00469EDA  83 3D 3F CE B5 00 00            cmp dword ptr [rip + 0xb5ce3f], 0
00469EE1  75 19                           jne 0x140469efc
00469EE3  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
00469EE7  40 88 7B 67                     mov byte ptr [rbx + 0x67], dil
00469EEB  E8 84 F6 DC FF                  call 0x140239574
00469EF0  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00469EF5  48 83 C4 20                     add rsp, 0x20
00469EF9  5F                              pop rdi
00469EFA  C3                              ret
00469EFB  CC                              int3
00469EFC  40 8A CF                        mov cl, dil
00469EFF  E8 F8 B7 08 00                  call 0x1404f56fc
00469F04  EB DD                           jmp 0x140469ee3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockPoolCommitWs(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 11914815)) != 0) goto loc_00469EFC;
loc_00469EE3:
    *(unsigned __int8 *)(a1 + 103) = (unsigned __int8)(v_cr8);
    result = MiLockWorkingSetSharedAtDpc(*(unsigned __int64 *)(a1 + 72), 2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00469EFC:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 2, a3, a4);
    goto loc_00469EE3;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockPoolCommitWs(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xB5CE3F)) != 0) goto loc_00469EFC;
loc_00469EE3:
    *(uint8_t *)(arg1 + 0x67) = (uint8_t)(v_cr8);
    result = MiLockWorkingSetSharedAtDpc(*(uint64_t *)(arg1 + 0x48), 2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00469EFC:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), 2, a3, a4);
    goto loc_00469EE3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x67` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00469EC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00469EC0[BB_00469EC0]
  bb_00469EE3[BB_00469EE3]
  bb_00469EFB[BB_00469EFB]
  bb_00469EFC[BB_00469EFC]
  bb_00469EC0 -->|branch| bb_00469EFC
  bb_00469EC0 -->|fallthrough| bb_00469EE3
  bb_00469EFB -->|flow| bb_00469EFC
  bb_00469EFC -->|branch| bb_00469EE3
```
