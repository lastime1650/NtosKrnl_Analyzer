# MiUpdateHugePageCounts

- RVA: `0x00677530`–`0x00677595` (길이 `101` bytes)
- VA: `0x0000000140677530`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `26`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00677555` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)

### Direct callers
- [MiInsertHugeRangeInList](../43/MiInsertHugeRangeInList_function_004371E8.md) at `0x0043735B`
- [MiAddPartitionHugeRange](MiAddPartitionHugeRange_function_006750D8.md) at `0x006752DA`
- [MiHotRemoveHugeRange](MiHotRemoveHugeRange_function_00675DD0.md) at `0x00675E77`
- [MiMoveBadHugeRangeCrossPartition](MiMoveBadHugeRangeCrossPartition_function_00676DD0.md) at `0x00676EAE`
- [MiMoveBadHugeRangeCrossPartition](MiMoveBadHugeRangeCrossPartition_function_00676DD0.md) at `0x00676EBF`
- [MiSetHugeRangePartitionId](MiSetHugeRangePartitionId_function_006773E4.md) at `0x006774B5`
- [MiSetHugeRangePartitionId](MiSetHugeRangePartitionId_function_006773E4.md) at `0x006774C9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00677530  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00677535  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0067753A  57                              push rdi
0067753B  48 83 EC 20                     sub rsp, 0x20
0067753F  81 E2 FF FF 3F 00               and edx, 0x3fffff
00677545  48 8B F9                        mov rdi, rcx
00677548  48 C1 E2 12                     shl rdx, 0x12
0067754C  41 8B D9                        mov ebx, r9d
0067754F  48 8B CA                        mov rcx, rdx
00677552  49 8B F0                        mov rsi, r8
00677555  E8 76 17 CC FF                  call 0x140338cd0
0067755A  48 8B D6                        mov rdx, rsi
0067755D  8B C8                           mov ecx, eax
0067755F  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00677563  48 F7 DA                        neg rdx
00677566  85 DB                           test ebx, ebx
00677568  48 0F 44 F2                     cmove rsi, rdx
0067756C  48 69 D1 80 DF 00 00            imul rdx, rcx, 0xdf80
00677573  F0 48 01 B4 02 90 3A 00 00      lock add qword ptr [rdx + rax + 0x3a90], rsi
0067757C  F0 48 01 B7 A8 01 00 00         lock add qword ptr [rdi + 0x1a8], rsi
00677584  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00677589  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0067758E  48 83 C4 20                     add rsp, 0x20
00677592  5F                              pop rdi
00677593  C3                              ret
00677594  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUpdateHugePageCounts(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a2 = (unsigned int)((a2) & (0x3FFFFFULL));
    a2 = (a2) << (18);
    result = MiPageToNode(a2, a2, a3, a4);
    a2 = -(a3);
    if ((unsigned int)((unsigned int)(a4)) == 0) { a3 = a2; }
    a2 = (a2) * ((unsigned int)((unsigned int)(result)));
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a1 + 16);
}
```

## 5. (Beta) C Style

```c
int64_t MiUpdateHugePageCounts(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg2 = (uint32_t)((Arg2) & (0x3FFFFFULL));
    Arg2 = (Arg2) << (18);
    result = MiPageToNode(Arg2, Arg2, Arg3, Arg4);
    Arg2 = -(Arg3);
    if ((uint32_t)((uint32_t)(Arg4)) == 0) { Arg3 = Arg2; }
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(result)));
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg1 + 0x10);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x1A8` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00677530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00677530[BB_00677530]
  bb_00677594[BB_00677594]
```
