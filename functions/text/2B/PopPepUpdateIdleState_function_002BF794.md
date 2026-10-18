# PopPepUpdateIdleState

- RVA: `0x002BF794`–`0x002BF7EF` (길이 `91` bytes)
- VA: `0x00000001402BF794`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067AA4`
- 디코드: `26`개 명령, `91/91` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002BF7AF` → [PopPepGetComponentPreferedIdleState](PopPepGetComponentPreferedIdleState_function_002BF800.md) (function, `0x002BF800`)
- `0x002BF7E8` → [PopPepTriggerActivity](../24/PopPepTriggerActivity_function_0024CDB0.md) (function, `0x0024CDB0`)

### Direct callers
- [PopPepUpdateConstraints](../26/PopPepUpdateConstraints_function_0026F5C8.md) at `0x0026F730`
- [PopPepIdleTimeoutRoutine](../45/PopPepIdleTimeoutRoutine_function_00458E10.md) at `0x00459027`
- [PopPepComponentSetResidency](../5D/PopPepComponentSetResidency_function_005DC9A4.md) at `0x005DCA44`
- [PopPepComponentSetWakeHint](../5D/PopPepComponentSetWakeHint_function_005DCAA0.md) at `0x005DCB37`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002BF794  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002BF799  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
002BF79E  57                              push rdi
002BF79F  48 83 EC 20                     sub rsp, 0x20
002BF7A3  48 8B F1                        mov rsi, rcx
002BF7A6  41 8A F8                        mov dil, r8b
002BF7A9  48 8B CA                        mov rcx, rdx
002BF7AC  48 8B DA                        mov rbx, rdx
002BF7AF  E8 4C 00 00 00                  call 0x1402bf800
002BF7B4  3B 83 B0 00 00 00               cmp eax, dword ptr [rbx + 0xb0]
002BF7BA  75 11                           jne 0x1402bf7cd
002BF7BC  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002BF7C1  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
002BF7C6  48 83 C4 20                     add rsp, 0x20
002BF7CA  5F                              pop rdi
002BF7CB  C3                              ret
002BF7CC  CC                              int3
002BF7CD  44 8B C8                        mov r9d, eax
002BF7D0  41 B8 01 00 00 00               mov r8d, 1
002BF7D6  41 0F BA E9 1F                  bts r9d, 0x1f
002BF7DB  48 8B D3                        mov rdx, rbx
002BF7DE  40 84 FF                        test dil, dil
002BF7E1  48 8B CE                        mov rcx, rsi
002BF7E4  44 0F 44 C8                     cmove r9d, eax
002BF7E8  E8 C3 D5 F8 FF                  call 0x14024cdb0
002BF7ED  EB CD                           jmp 0x1402bf7bc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPepUpdateIdleState(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = PopPepGetComponentPreferedIdleState(a2, a2, a3, a4);
    if (((unsigned int)(result)) != (*(unsigned int *)(a2 + 176))) goto loc_002BF7CD;
loc_002BF7BC:
    v_rsp = (v_rsp) + (32);
    return result;
loc_002BF7CD:
    a4 = (unsigned int)((unsigned int)(result));
    if (a3 == 0) { a4 = (unsigned int)(result); }
    result = PopPepTriggerActivity(v_stack_p10, v_stack_p8, 1, a4);
    goto loc_002BF7BC;
}
```

## 5. (Beta) C Style

```c
int64_t PopPepUpdateIdleState(int64_t Arg1, void *Arg2, uint8_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = PopPepGetComponentPreferedIdleState(Arg2, Arg2, Arg3, a4);
    if (((uint32_t)(result)) != (*(uint32_t *)(arg2 + 0xB0))) goto loc_002BF7CD;
loc_002BF7BC:
    local_rsp = (local_rsp) + (32);
    return result;
loc_002BF7CD:
    a4 = (uint32_t)((uint32_t)(result));
    if (Arg3 == 0) { a4 = (uint32_t)(result); }
    result = PopPepTriggerActivity(v_stack_p10, v_stack_p8, 1, a4);
    goto loc_002BF7BC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xB0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002BF794&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002BF794[BB_002BF794]
  bb_002BF7BC[BB_002BF7BC]
  bb_002BF7CC[BB_002BF7CC]
  bb_002BF7CD[BB_002BF7CD]
  bb_002BF794 -->|branch| bb_002BF7CD
  bb_002BF794 -->|fallthrough| bb_002BF7BC
  bb_002BF7CC -->|flow| bb_002BF7CD
  bb_002BF7CD -->|branch| bb_002BF7BC
```
