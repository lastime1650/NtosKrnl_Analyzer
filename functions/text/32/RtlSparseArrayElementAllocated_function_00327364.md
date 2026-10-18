# RtlSparseArrayElementAllocated

- RVA: `0x00327364`–`0x003273B7` (길이 `83` bytes)
- VA: `0x0000000140327364`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065BB8`
- 디코드: `26`개 명령, `83/83` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0032738F` → [RtlCSparseBitmapFindBitSetCapped](RtlCSparseBitmapFindBitSetCapped_function_003274AC.md) (function, `0x003274AC`)

### Direct callers
- [RtlpHpVaMgrCtxFree](../2E/RtlpHpVaMgrCtxFree_function_002ED734.md) at `0x002ED76F`
- [RtlpHpVaMgrCtxFree](../2E/RtlpHpVaMgrCtxFree_function_002ED734.md) at `0x002ED7E2`
- [RtlpHpVaMgrRangeFind](../2E/RtlpHpVaMgrRangeFind_function_002EDD78.md) at `0x002EDE71`
- [RtlpHpVaMgrRangeCommitProcess](../49/RtlpHpVaMgrRangeCommitProcess_function_0049A444.md) at `0x0049A479`
- [RtlpHpVaMgrCtxCommit](../60/RtlpHpVaMgrCtxCommit_function_00603D44.md) at `0x00603D70`
- [RtlpHpVaMgrCtxDecommit](../60/RtlpHpVaMgrCtxDecommit_function_00603DC0.md) at `0x00603DE4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00327364  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00327369  57                              push rdi
0032736A  48 83 EC 20                     sub rsp, 0x20
0032736E  48 8B F9                        mov rdi, rcx
00327371  48 8B DA                        mov rbx, rdx
00327374  8B 49 08                        mov ecx, dword ptr [rcx + 8]
00327377  41 B8 01 00 00 00               mov r8d, 1
0032737D  49 D3 E0                        shl r8, cl
00327380  48 D3 E2                        shl rdx, cl
00327383  48 8D 4F 10                     lea rcx, [rdi + 0x10]
00327387  49 C1 E0 03                     shl r8, 3
0032738B  48 C1 E2 03                     shl rdx, 3
0032738F  E8 18 01 00 00                  call 0x1403274ac
00327394  48 83 F8 FF                     cmp rax, -1
00327398  74 19                           je 0x1403273b3
0032739A  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
0032739D  48 D3 E3                        shl rbx, cl
003273A0  48 03 5F 18                     add rbx, qword ptr [rdi + 0x18]
003273A4  48 8B C3                        mov rax, rbx
003273A7  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003273AC  48 83 C4 20                     add rsp, 0x20
003273B0  5F                              pop rdi
003273B1  C3                              ret
003273B2  CC                              int3
003273B3  33 C0                           xor eax, eax
003273B5  EB F0                           jmp 0x1403273a7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlSparseArrayElementAllocated(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = (1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 8))));
    a2 = (a2) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 8))));
    a3 = (a3) << (3);
    a2 = (a2) << (3);
    result = RtlCSparseBitmapFindBitSetCapped(a1 + 16, a2, a3, a4);
    if (result == -1) goto loc_003273B3;
    v_rbx = (a2) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 8))));
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(a1 + 24));
loc_003273A7:
    v_rsp = (v_rsp) + (32);
    return v_rbx;
loc_003273B3:
    result = 0;
    goto loc_003273A7;
}
```

## 5. (Beta) C Style

```c
int64_t RtlSparseArrayElementAllocated(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    a3 = (1) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))));
    Arg2 = (Arg2) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))));
    a3 = (a3) << (3);
    Arg2 = (Arg2) << (3);
    result = RtlCSparseBitmapFindBitSetCapped(Arg1 + 16, Arg2, a3, a4);
    if (result == -1) goto loc_003273B3;
    local_rbx = (Arg2) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))));
    local_rbx = (local_rbx) + (*(uint64_t *)(arg1 + 0x18));
loc_003273A7:
    local_rsp = (local_rsp) + (32);
    return local_rbx;
loc_003273B3:
    result = 0;
    goto loc_003273A7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00327364&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00327364[BB_00327364]
  bb_0032739A[BB_0032739A]
  bb_003273A7[BB_003273A7]
  bb_003273B2[BB_003273B2]
  bb_003273B3[BB_003273B3]
  bb_00327364 -->|branch| bb_003273B3
  bb_00327364 -->|fallthrough| bb_0032739A
  bb_0032739A -->|flow| bb_003273A7
  bb_003273B2 -->|flow| bb_003273B3
  bb_003273B3 -->|branch| bb_003273A7
```
