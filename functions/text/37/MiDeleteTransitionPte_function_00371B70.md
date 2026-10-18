# MiDeleteTransitionPte

- RVA: `0x00371B70`–`0x00371BDA` (길이 `106` bytes)
- VA: `0x0000000140371B70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A838`
- 디코드: `23`개 명령, `106/106` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00371BBB` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)

### Direct callers
- [MiDecommitHandleTransitionPte](../24/MiDecommitHandleTransitionPte_function_0024037C.md) at `0x00240539`
- [MiWalkEntireImage](../36/MiWalkEntireImage_function_00365D70.md) at `0x00366E6F`
- [MiTryDeleteTransitionPte](MiTryDeleteTransitionPte_function_003710DC.md) at `0x00371213`
- [MiPurgeSubsection](MiPurgeSubsection_function_003712F0.md) at `0x00371476`
- [MiDeletePerSessionProtos](../4A/MiDeletePerSessionProtos_function_004A0840.md) at `0x004A093D`
- [MiPurgeFileOnlyPfn](../68/MiPurgeFileOnlyPfn_function_00681CEC.md) at `0x00681EA8`
- [MiStoreDiscardPoisonedPage](../69/MiStoreDiscardPoisonedPage_function_00692858.md) at `0x00692C9F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00371BD4` → [sub_00371F65](Unknown_function_00371F65.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00371B70  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00371B75  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
00371B7A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00371B7F  53                              push rbx
00371B80  41 55                           push r13
00371B82  41 56                           push r14
00371B84  48 81 EC 90 00 00 00            sub rsp, 0x90
00371B8B  4C 8B F2                        mov r14, rdx
00371B8E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00371B98  48 8B D9                        mov rbx, rcx
00371B9B  48 8B C0                        mov rax, rax
00371B9E  4C 8B EA                        mov r13, rdx
00371BA1  4C 2B E8                        sub r13, rax
00371BA4  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00371BAE  49 C1 FD 04                     sar r13, 4
00371BB2  4C 0F AF E8                     imul r13, rax
00371BB6  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00371BBB  E8 E0 0C F1 FF                  call 0x1402828a0
00371BC0  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00371BC4  48 BA 00 00 00 00 00 00 00 80   movabs rdx, 0x8000000000000000
00371BCE  48 0B CA                        or rcx, rdx
00371BD1  48 3B CB                        cmp rcx, rbx
00371BD4  0F 85 8B 03 00 00               jne 0x140371f65
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeleteTransitionPte(__int64 a1, __int64 a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (144);
    v_r13 = (a2) - (result);
    v_r13 = (v_r13) >> (4);
    v_r13 = (v_r13) * (result);
    v_stack_m70 = v_r13;
    result = MI_READ_PTE_LOCK_FREE(a1, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(a2 + 8)) | (a2);
}
```

## 5. (Beta) C Style

```c
int64_t MiDeleteTransitionPte(int64_t Arg1, void *Arg2, uint8_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (144);
    local_r13 = (Arg2) - (result);
    local_r13 = (local_r13) >> (4);
    local_r13 = (local_r13) * (result);
    v_stack_m70 = local_r13;
    result = MI_READ_PTE_LOCK_FREE(Arg1, Arg2, Arg3, Arg4);
    Arg1 = (*(uint64_t *)(arg2 + 0x8)) | (Arg2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00371B70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00371B70[BB_00371B70]
```
