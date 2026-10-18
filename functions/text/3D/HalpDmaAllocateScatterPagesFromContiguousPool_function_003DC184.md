# HalpDmaAllocateScatterPagesFromContiguousPool

- RVA: `0x003DC184`–`0x003DC1D4` (길이 `80` bytes)
- VA: `0x00000001403DC184`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068878`
- 디코드: `22`개 명령, `80/80` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003DC18E` → [HalpDmaGetMasterAdapterVersion](HalpDmaGetMasterAdapterVersion_function_003DC5B0.md) (function, `0x003DC5B0`)
- `0x003DC1AD` → [HalpDmaAllocateScatterPagesFromContiguousPoolV2](../3E/HalpDmaAllocateScatterPagesFromContiguousPoolV2_function_003E1DC4.md) (function, `0x003E1DC4`)
- `0x003DC1CD` → [HalpDmaAllocateScatterPagesFromContiguousPoolV3](../4E/HalpDmaAllocateScatterPagesFromContiguousPoolV3_function_004E380C.md) (function, `0x004E380C`)

### Direct callers
- [sub_006F79F4](../6F/Unknown_function_006F79F4.md) at `0x006F7A38`
- [HalpDmaAllocateLocalScatterPool](../../page/70/HalpDmaAllocateLocalScatterPool_function_007091D4.md) at `0x00709372`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003DC184  48 83 EC 38                     sub rsp, 0x38
003DC188  48 8B CA                        mov rcx, rdx
003DC18B  4C 8B D2                        mov r10, rdx
003DC18E  E8 1D 04 00 00                  call 0x1403dc5b0
003DC193  49 8B D2                        mov rdx, r10
003DC196  83 E8 02                        sub eax, 2
003DC199  75 1D                           jne 0x1403dc1b8
003DC19B  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003DC1A0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003DC1A5  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
003DC1A9  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003DC1AD  E8 12 5C 00 00                  call 0x1403e1dc4
003DC1B2  48 83 C4 38                     add rsp, 0x38
003DC1B6  C3                              ret
003DC1B7  CC                              int3
003DC1B8  83 F8 01                        cmp eax, 1
003DC1BB  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003DC1C0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003DC1C5  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
003DC1C9  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003DC1CD  E8 3A 76 10 00                  call 0x1404e380c
003DC1D2  EB DE                           jmp 0x1403dc1b2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpDmaAllocateScatterPagesFromContiguousPool(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int8 v_stack_m18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;

    v_rsp = (v_rsp) - (56);
    result = HalpDmaGetMasterAdapterVersion(a2, a2, a3, a4);
    result = (unsigned int)((result) - (2));
    if (condition_is_not_equal) goto loc_003DC1B8;
    v_stack_m10 = a6;
    v_stack_m18 = a5;
    result = HalpDmaAllocateScatterPagesFromContiguousPoolV2(a2, a2, a3, a4);
loc_003DC1B2:
    v_rsp = (v_rsp) + (56);
    return result;
loc_003DC1B8:
    v_stack_p28 = a6;
    v_stack_p20 = a5;
    result = HalpDmaAllocateScatterPagesFromContiguousPoolV3(a2, a2, a3, a4);
    goto loc_003DC1B2;
}
```

## 5. (Beta) C Style

```c
int64_t HalpDmaAllocateScatterPagesFromContiguousPool(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint8_t v_stack_m18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;

    local_rsp = (local_rsp) - (56);
    result = HalpDmaGetMasterAdapterVersion(Arg2, Arg2, Arg3, Arg4);
    result = (uint32_t)((result) - (2));
    if (condition_is_not_equal) goto loc_003DC1B8;
    v_stack_m10 = Arg6;
    v_stack_m18 = Arg5;
    result = HalpDmaAllocateScatterPagesFromContiguousPoolV2(Arg2, Arg2, Arg3, Arg4);
loc_003DC1B2:
    local_rsp = (local_rsp) + (56);
    return result;
loc_003DC1B8:
    v_stack_p28 = Arg6;
    v_stack_p20 = Arg5;
    result = HalpDmaAllocateScatterPagesFromContiguousPoolV3(Arg2, Arg2, Arg3, Arg4);
    goto loc_003DC1B2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DC184&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DC184[BB_003DC184]
  bb_003DC19B[BB_003DC19B]
  bb_003DC1B2[BB_003DC1B2]
  bb_003DC1B7[BB_003DC1B7]
  bb_003DC1B8[BB_003DC1B8]
  bb_003DC184 -->|branch| bb_003DC1B8
  bb_003DC184 -->|fallthrough| bb_003DC19B
  bb_003DC19B -->|flow| bb_003DC1B2
  bb_003DC1B7 -->|flow| bb_003DC1B8
  bb_003DC1B8 -->|branch| bb_003DC1B2
```
