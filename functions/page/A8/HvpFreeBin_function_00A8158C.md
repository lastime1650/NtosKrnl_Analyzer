# HvpFreeBin

- RVA: `0x00A8158C`–`0x00A815E5` (길이 `89` bytes)
- VA: `0x0000000140A8158C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006383C`
- 디코드: `25`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A815BA` → [CmpProtectPool](../../text/26/CmpProtectPool_function_00267BB8.md) (function, `0x00267BB8`)
- `0x00A815C8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A815DE` → [MmFreeIndependentPages](../../text/2A/MmFreeIndependentPages_function_002A2510.md) (function, `0x002A2510`)

### Direct callers
- [HvpAddDummyBinToHive](../7E/HvpAddDummyBinToHive_function_007EF80C.md) at `0x007EF8AB`
- [HvpMapHiveImage](../7E/HvpMapHiveImage_function_007EF8D0.md) at `0x007EFA01`
- [HvHiveCleanup](../84/HvHiveCleanup_function_0084D918.md) at `0x0084DAF4`
- [HvpDropPagedBins](../9B/HvpDropPagedBins_function_009B7168.md) at `0x009B7315`
- [HvpRemapAndEnlistHiveBins](../9B/HvpRemapAndEnlistHiveBins_function_009B8E0C.md) at `0x009B94B6`
- [HvpAddBin](../AF/HvpAddBin_function_00AF7D48.md) at `0x00AF815A`
- [HvpAddBin](../AF/HvpAddBin_function_00AF7D48.md) at `0x00AF81BF`
- [sub_00B2E0F0](../B2/Unknown_function_00B2E0F0.md) at `0x00B2E2E7`
- [sub_00B3E78C](../B3/Unknown_function_00B3E78C.md) at `0x00B3E7FB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A815BA` → [CmpProtectPool](../../text/26/CmpProtectPool_function_00267BB8.md) (`PAGE` → `.text`)
  - `0x00A815C8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A815DE` → [MmFreeIndependentPages](../../text/2A/MmFreeIndependentPages_function_002A2510.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8158C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A81591  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00A81596  57                              push rdi
00A81597  48 83 EC 20                     sub rsp, 0x20
00A8159B  F7 81 A0 00 00 00 00 00 00 02   test dword ptr [rcx + 0xa0], 0x2000000
00A815A5  49 8B D8                        mov rbx, r8
00A815A8  8B FA                           mov edi, edx
00A815AA  48 8B F1                        mov rsi, rcx
00A815AD  48 8B CB                        mov rcx, rbx
00A815B0  8B D2                           mov edx, edx
00A815B2  75 2A                           jne 0x140a815de
00A815B4  41 B8 04 00 00 00               mov r8d, 4
00A815BA  E8 F9 65 7E FF                  call 0x140267bb8
00A815BF  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00A815C3  8B D7                           mov edx, edi
00A815C5  48 8B CB                        mov rcx, rbx
00A815C8  E8 03 95 C3 FF                  call 0x1406baad0
00A815CD  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A815D2  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00A815D7  48 83 C4 20                     add rsp, 0x20
00A815DB  5F                              pop rdi
00A815DC  C3                              ret
00A815DD  CC                              int3
00A815DE  E8 2D 0F 82 FF                  call 0x1402a2510
00A815E3  EB E8                           jmp 0x140a815cd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvpFreeBin(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (((*(unsigned int *)(a1 + 160)) & (0x2000000ULL)) != 0) goto loc_00A815DE;
    result = CmpProtectPool(a3, (unsigned int)(a2), 4, a4);
    result = guard_dispatch_icall(a3, (unsigned int)((unsigned int)((unsigned int)(a2))), 4, a4);
loc_00A815CD:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A815DE:
    result = MmFreeIndependentPages(a3, (unsigned int)((unsigned int)((unsigned int)(a2))), 4, a4);
    goto loc_00A815CD;
}
```

## 5. (Beta) C Style

```c
int64_t HvpFreeBin(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (((*(uint32_t *)(arg1 + 0xA0)) & (0x2000000ULL)) != 0) goto loc_00A815DE;
    result = CmpProtectPool(Arg3, (uint32_t)(Arg2), 4, a4);
    result = guard_dispatch_icall(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg2))), 4, a4);
loc_00A815CD:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A815DE:
    result = MmFreeIndependentPages(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg2))), 4, a4);
    goto loc_00A815CD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8158C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8158C[BB_00A8158C]
  bb_00A815B4[BB_00A815B4]
  bb_00A815CD[BB_00A815CD]
  bb_00A815DD[BB_00A815DD]
  bb_00A815DE[BB_00A815DE]
  bb_00A8158C -->|branch| bb_00A815DE
  bb_00A8158C -->|fallthrough| bb_00A815B4
  bb_00A815B4 -->|flow| bb_00A815CD
  bb_00A815DD -->|flow| bb_00A815DE
  bb_00A815DE -->|branch| bb_00A815CD
```
