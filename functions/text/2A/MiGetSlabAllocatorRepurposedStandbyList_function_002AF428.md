# MiGetSlabAllocatorRepurposedStandbyList

- RVA: `0x002AF428`–`0x002AF4AC` (길이 `132` bytes)
- VA: `0x00000001402AF428`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006D4EC`
- 디코드: `34`개 명령, `132/132` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002AF443` → [MI_GET_SLAB_STANDBY_PAGE_SLAB_ENTRY](MI_GET_SLAB_STANDBY_PAGE_SLAB_ENTRY_function_002AF4B4.md) (function, `0x002AF4B4`)
- `0x002AF47C` → [MI_NODE_FROM_PFN](../2B/MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x002AF4A5` → [MiGetSlabRepurposedStandbyListWorker](MiGetSlabRepurposedStandbyListWorker_function_002AF534.md) (function, `0x002AF534`)

### Direct callers
- [sub_00287E84](../28/Unknown_function_00287E84.md) at `0x00287EA2`
- [MiUpdatePageAttributeStamp](../48/MiUpdatePageAttributeStamp_function_00482364.md) at `0x00482516`

### Static image references
- `0x002AF465` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002AF428  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002AF42D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
002AF432  57                              push rdi
002AF433  48 83 EC 20                     sub rsp, 0x20
002AF437  48 63 F2                        movsxd rsi, edx
002AF43A  48 8B F9                        mov rdi, rcx
002AF43D  41 F6 C0 01                     test r8b, 1
002AF441  75 1E                           jne 0x1402af461
002AF443  E8 6C 00 00 00                  call 0x1402af4b4
002AF448  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
002AF44C  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
002AF450  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002AF455  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
002AF45A  48 83 C4 20                     add rsp, 0x20
002AF45E  5F                              pop rdi
002AF45F  C3                              ret
002AF460  CC                              int3
002AF461  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
002AF465  48 8B 0D 1C 0C B8 00            mov rcx, qword ptr [rip + 0xb80c1c]
002AF46C  48 C1 E8 2B                     shr rax, 0x2b
002AF470  25 FF 03 00 00                  and eax, 0x3ff
002AF475  48 8B 1C C1                     mov rbx, qword ptr [rcx + rax*8]
002AF479  48 8B CF                        mov rcx, rdi
002AF47C  E8 AF 1A 00 00                  call 0x1402b0f30
002AF481  8B C8                           mov ecx, eax
002AF483  48 69 D1 80 DF 00 00            imul rdx, rcx, 0xdf80
002AF48A  48 69 CE E8 00 00 00            imul rcx, rsi, 0xe8
002AF491  48 03 D1                        add rdx, rcx
002AF494  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
002AF498  48 81 C2 50 3D 00 00            add rdx, 0x3d50
002AF49F  48 03 CA                        add rcx, rdx
002AF4A2  48 8B D7                        mov rdx, rdi
002AF4A5  E8 8A 00 00 00                  call 0x1402af534
002AF4AA  EB A4                           jmp 0x1402af450
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetSlabAllocatorRepurposedStandbyList(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (((a3) & (1)) != 0) goto loc_002AF461;
    result = MI_GET_SLAB_STANDBY_PAGE_SLAB_ENTRY(a1, a2, a3, a4);
loc_002AF450:
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(*(unsigned __int64 *)(result + 56) + 80);
loc_002AF461:
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    result = MI_NODE_FROM_PFN(a1, a2, a3, a4);
    a2 = (a2) * ((unsigned int)((unsigned int)(result)));
    a1 = ((unsigned int)((unsigned int)(result))) * (v_stack_p10);
    a2 = (a2) + (a1);
    a2 = (a2) + (0x3D50ULL);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12061724) + result * 8) + 16)) + (a2);
    result = MiGetSlabRepurposedStandbyListWorker(a1, a1, a3, a4);
    goto loc_002AF450;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetSlabAllocatorRepurposedStandbyList(void *Arg1, int32_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (((Arg3) & (1)) != 0) goto loc_002AF461;
    result = MI_GET_SLAB_STANDBY_PAGE_SLAB_ENTRY(Arg1, Arg2, Arg3, a4);
loc_002AF450:
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(*(uint64_t *)(result + 0x38) + 0x50);
loc_002AF461:
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    result = MI_NODE_FROM_PFN(Arg1, Arg2, Arg3, a4);
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(result)));
    Arg1 = ((uint32_t)((uint32_t)(result))) * (v_stack_p10);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) + (0x3D50ULL);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB80C1C) + result * 8) + 0x10)) + (Arg2);
    result = MiGetSlabRepurposedStandbyListWorker(Arg1, Arg1, Arg3, a4);
    goto loc_002AF450;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002AF428&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002AF428[BB_002AF428]
  bb_002AF443[BB_002AF443]
  bb_002AF450[BB_002AF450]
  bb_002AF460[BB_002AF460]
  bb_002AF461[BB_002AF461]
  bb_002AF428 -->|branch| bb_002AF461
  bb_002AF428 -->|fallthrough| bb_002AF443
  bb_002AF443 -->|flow| bb_002AF450
  bb_002AF460 -->|flow| bb_002AF461
  bb_002AF461 -->|branch| bb_002AF450
```
