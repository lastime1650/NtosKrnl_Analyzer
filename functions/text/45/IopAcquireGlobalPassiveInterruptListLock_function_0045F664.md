# IopAcquireGlobalPassiveInterruptListLock

- RVA: `0x0045F664`–`0x0045F6AA` (길이 `70` bytes)
- VA: `0x000000014045F664`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `20`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0045F690` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x0045F6A3` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [IopInsertPassiveInterruptBlock](IopInsertPassiveInterruptBlock_function_0045F310.md) at `0x0045F331`
- [IopFindPassiveInterruptBlock](IopFindPassiveInterruptBlock_function_0045F4BC.md) at `0x0045F4CE`
- [IopDereferencePassiveInterruptBlock](IopDereferencePassiveInterruptBlock_function_0045F52C.md) at `0x0045F54A`

### Static image references
- `0x0045F67E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0045F687` → RVA `0x00F8CC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045F664  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0045F669  57                              push rdi
0045F66A  48 83 EC 20                     sub rsp, 0x20
0045F66E  48 8B F9                        mov rdi, rcx
0045F671  44 0F 20 C3                     mov rbx, cr8
0045F675  BA 0C 00 00 00                  mov edx, 0xc
0045F67A  44 0F 22 C2                     mov cr8, rdx
0045F67E  83 3D 9B 76 B6 00 00            cmp dword ptr [rip + 0xb6769b], 0
0045F685  75 1A                           jne 0x14045f6a1
0045F687  48 8D 0D F2 D5 B2 00            lea rcx, [rip + 0xb2d5f2]
0045F68E  88 1F                           mov byte ptr [rdi], bl
0045F690  E8 9B 8D DA FF                  call 0x140208430
0045F695  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0045F69A  48 83 C4 20                     add rsp, 0x20
0045F69E  5F                              pop rdi
0045F69F  C3                              ret
0045F6A0  CC                              int3
0045F6A1  8A CB                           mov cl, bl
0045F6A3  E8 54 60 09 00                  call 0x1404f56fc
0045F6A8  EB DD                           jmp 0x14045f687
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopAcquireGlobalPassiveInterruptListLock(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 11957915)) != 0) goto loc_0045F6A1;
loc_0045F687:
    *(unsigned __int8 *)(a1) = (unsigned __int8)(v_cr8);
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 11720178, 12, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_0045F6A1:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p8), 12, a3, a4);
    goto loc_0045F687;
}
```

## 5. (Beta) C Style

```c
int64_t IopAcquireGlobalPassiveInterruptListLock(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xB6769B)) != 0) goto loc_0045F6A1;
loc_0045F687:
    *(uint8_t *)(arg1) = (uint8_t)(v_cr8);
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 11720178, 12, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_0045F6A1:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p8), 12, a3, a4);
    goto loc_0045F687;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045F664&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045F664[BB_0045F664]
  bb_0045F687[BB_0045F687]
  bb_0045F6A0[BB_0045F6A0]
  bb_0045F6A1[BB_0045F6A1]
  bb_0045F664 -->|branch| bb_0045F6A1
  bb_0045F664 -->|fallthrough| bb_0045F687
  bb_0045F6A0 -->|flow| bb_0045F6A1
  bb_0045F6A1 -->|branch| bb_0045F687
```
