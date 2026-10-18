# MI_SET_SLAB_STANDBY_PAGE_SLAB_ENTRY

- RVA: `0x002AF708`–`0x002AF766` (길이 `94` bytes)
- VA: `0x00000001402AF708`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `26`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002AF730` → [MiSetPfnNodeBlinkLow](MiSetPfnNodeBlinkLow_function_002AF2A0.md) (function, `0x002AF2A0`)
- `0x002AF750` → [MiSetNextStandbyPageSecondaryNoLockAsserts](MiSetNextStandbyPageSecondaryNoLockAsserts_function_002AF300.md) (function, `0x002AF300`)

### Direct callers
- [MiGetSlabRepurposedStandbyListWorker](MiGetSlabRepurposedStandbyListWorker_function_002AF534.md) at `0x002AF620`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002AF708  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002AF70D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
002AF712  57                              push rdi
002AF713  48 83 EC 20                     sub rsp, 0x20
002AF717  48 8B DA                        mov rbx, rdx
002AF71A  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002AF724  48 23 D8                        and rbx, rax
002AF727  48 8B FA                        mov rdi, rdx
002AF72A  48 8B D3                        mov rdx, rbx
002AF72D  48 8B F1                        mov rsi, rcx
002AF730  E8 6B FB FF FF                  call 0x1402af2a0
002AF735  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
002AF738  48 8B CE                        mov rcx, rsi
002AF73B  25 00 00 E0 FF                  and eax, 0xffe00000
002AF740  48 C1 EB 13                     shr rbx, 0x13
002AF744  48 C1 EF 28                     shr rdi, 0x28
002AF748  0B D8                           or ebx, eax
002AF74A  48 8B D7                        mov rdx, rdi
002AF74D  89 5E 24                        mov dword ptr [rsi + 0x24], ebx
002AF750  E8 AB FB FF FF                  call 0x1402af300
002AF755  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002AF75A  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
002AF75F  48 83 C4 20                     add rsp, 0x20
002AF763  5F                              pop rdi
002AF764  C3                              ret
002AF765  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MI_SET_SLAB_STANDBY_PAGE_SLAB_ENTRY(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rbx = (a2) & (result);
    result = MiSetPfnNodeBlinkLow(a1, v_rbx, a3, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 36))) & (0xFFE00000ULL));
    v_rbx = (v_rbx) >> (19);
    v_rdi = (a2) >> (40);
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    *(unsigned int *)(a1 + 36) = (unsigned int)(v_rbx);
    result = MiSetNextStandbyPageSecondaryNoLockAsserts(a1, v_rdi, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MI_SET_SLAB_STANDBY_PAGE_SLAB_ENTRY(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rbx = (Arg2) & (result);
    result = MiSetPfnNodeBlinkLow(Arg1, local_rbx, a3, a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x24))) & (0xFFE00000ULL));
    local_rbx = (local_rbx) >> (19);
    local_rdi = (Arg2) >> (40);
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    *(uint32_t *)(arg1 + 0x24) = (uint32_t)(local_rbx);
    result = MiSetNextStandbyPageSecondaryNoLockAsserts(Arg1, local_rdi, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x24` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002AF708&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002AF708[BB_002AF708]
  bb_002AF765[BB_002AF765]
```
