# HalpDmaAllocateContiguousPagesFromContiguousPool

- RVA: `0x003E024C`–`0x003E0299` (길이 `77` bytes)
- VA: `0x00000001403E024C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068878`
- 디코드: `21`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E0253` → [HalpDmaGetAdapterVersion](../3D/HalpDmaGetAdapterVersion_function_003DEC8C.md) (function, `0x003DEC8C`)
- `0x003E0272` → [HalpDmaAllocateContiguousPagesFromContiguousPoolV2](HalpDmaAllocateContiguousPagesFromContiguousPoolV2_function_003E02A0.md) (function, `0x003E02A0`)
- `0x003E0292` → [HalpDmaAllocateContiguousPagesFromContiguousPoolV3](../53/HalpDmaAllocateContiguousPagesFromContiguousPoolV3_function_0053DE24.md) (function, `0x0053DE24`)

### Direct callers
- [sub_006EA22C](../6E/Unknown_function_006EA22C.md) at `0x006EA269`
- [HalpDmaAllocateLocalContiguousPool](../../page/70/HalpDmaAllocateLocalContiguousPool_function_00708EE4.md) at `0x00709099`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E024C  48 83 EC 38                     sub rsp, 0x38
003E0250  4C 8B D2                        mov r10, rdx
003E0253  E8 34 EA FF FF                  call 0x1403dec8c
003E0258  49 8B D2                        mov rdx, r10
003E025B  83 E8 02                        sub eax, 2
003E025E  75 1D                           jne 0x1403e027d
003E0260  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003E0265  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003E026A  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
003E026E  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003E0272  E8 29 00 00 00                  call 0x1403e02a0
003E0277  48 83 C4 38                     add rsp, 0x38
003E027B  C3                              ret
003E027C  CC                              int3
003E027D  83 F8 01                        cmp eax, 1
003E0280  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003E0285  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003E028A  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
003E028E  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003E0292  E8 8D DB 15 00                  call 0x14053de24
003E0297  EB DE                           jmp 0x1403e0277
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpDmaAllocateContiguousPagesFromContiguousPool(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int8 v_stack_m18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;

    v_rsp = (v_rsp) - (56);
    result = HalpDmaGetAdapterVersion(a1, a2, a3, a4);
    result = (unsigned int)((result) - (2));
    if (condition_is_not_equal) goto loc_003E027D;
    v_stack_m10 = a6;
    v_stack_m18 = a5;
    result = HalpDmaAllocateContiguousPagesFromContiguousPoolV2(a1, a2, a3, a4);
loc_003E0277:
    v_rsp = (v_rsp) + (56);
    return result;
loc_003E027D:
    v_stack_p28 = a6;
    v_stack_p20 = a5;
    result = HalpDmaAllocateContiguousPagesFromContiguousPoolV3(a1, a2, a3, a4);
    goto loc_003E0277;
}
```

## 5. (Beta) C Style

```c
int64_t HalpDmaAllocateContiguousPagesFromContiguousPool(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint8_t v_stack_m18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;

    local_rsp = (local_rsp) - (56);
    result = HalpDmaGetAdapterVersion(Arg1, Arg2, Arg3, Arg4);
    result = (uint32_t)((result) - (2));
    if (condition_is_not_equal) goto loc_003E027D;
    v_stack_m10 = Arg6;
    v_stack_m18 = Arg5;
    result = HalpDmaAllocateContiguousPagesFromContiguousPoolV2(Arg1, Arg2, Arg3, Arg4);
loc_003E0277:
    local_rsp = (local_rsp) + (56);
    return result;
loc_003E027D:
    v_stack_p28 = Arg6;
    v_stack_p20 = Arg5;
    result = HalpDmaAllocateContiguousPagesFromContiguousPoolV3(Arg1, Arg2, Arg3, Arg4);
    goto loc_003E0277;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E024C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E024C[BB_003E024C]
  bb_003E0260[BB_003E0260]
  bb_003E0277[BB_003E0277]
  bb_003E027C[BB_003E027C]
  bb_003E027D[BB_003E027D]
  bb_003E024C -->|branch| bb_003E027D
  bb_003E024C -->|fallthrough| bb_003E0260
  bb_003E0260 -->|flow| bb_003E0277
  bb_003E027C -->|flow| bb_003E027D
  bb_003E027D -->|branch| bb_003E0277
```
