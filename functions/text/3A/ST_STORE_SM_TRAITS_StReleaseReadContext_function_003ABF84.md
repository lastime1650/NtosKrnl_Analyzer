# ST_STORE&lt;SM_TRAITS&gt;::StReleaseReadContext

- RVA: `0x003ABF84`–`0x003ABFE4` (길이 `96` bytes)
- VA: `0x00000001403ABF84`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068790`
- 디코드: `25`개 명령, `96/96` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003ABF9F` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchResultDeref](B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC5D0.md) (function, `0x003AC5D0`)
- `0x003ABFB2` → [B_TREE<unsigned long,ST_STORE<SM_TRAITS>::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE<SM_TRAITS>::ST_REGION_ENTRY_COMPARATOR>::BTreeSearchResultDeref](B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003AD260.md) (function, `0x003AD260`)
- `0x003ABFC7` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x003ABFDD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStReadThread](../20/SMKM_STORE_SM_TRAITS_SmStReadThread_function_00203230.md) at `0x002033FA`
- [sub_003AA952](Unknown_function_003AA952.md) at `0x003AA958`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x003ABFDD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003ABF84  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003ABF89  57                              push rdi
003ABF8A  48 83 EC 20                     sub rsp, 0x20
003ABF8E  48 8B FA                        mov rdi, rdx
003ABF91  48 8B D9                        mov rbx, rcx
003ABF94  48 8B 92 A8 01 00 00            mov rdx, qword ptr [rdx + 0x1a8]
003ABF9B  48 83 C1 50                     add rcx, 0x50
003ABF9F  E8 2C 06 00 00                  call 0x1403ac5d0
003ABFA4  48 8B 97 B0 01 00 00            mov rdx, qword ptr [rdi + 0x1b0]
003ABFAB  48 8D 8B 90 00 00 00            lea rcx, [rbx + 0x90]
003ABFB2  E8 A9 12 00 00                  call 0x1403ad260
003ABFB7  48 8D 8B D0 12 00 00            lea rcx, [rbx + 0x12d0]
003ABFBE  66 83 39 10                     cmp word ptr [rcx], 0x10
003ABFC2  73 14                           jae 0x1403abfd8
003ABFC4  48 8B D7                        mov rdx, rdi
003ABFC7  E8 E4 E5 30 00                  call 0x1406ba5b0
003ABFCC  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003ABFD1  48 83 C4 20                     add rsp, 0x20
003ABFD5  5F                              pop rdi
003ABFD6  C3                              ret
003ABFD7  CC                              int3
003ABFD8  33 D2                           xor edx, edx
003ABFDA  48 8B CF                        mov rcx, rdi
003ABFDD  E8 8E 68 7D 00                  call 0x140b82870
003ABFE2  EB E8                           jmp 0x1403abfcc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___StReleaseReadContext(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (80);
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, *(unsigned __int64 *)(a2 + 424), a3, a4);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(a1 + 144, *(unsigned __int64 *)(a2 + 432), a3, a4);
    if ((*(unsigned __int16 *)(a1 + 4816)) >= 16) goto loc_003ABFD8;
    result = ExpInterlockedPushEntrySList(a1 + 4816, a2, a3, a4);
loc_003ABFCC:
    v_rsp = (v_rsp) + (32);
    return result;
loc_003ABFD8:
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, a3, a4);
    goto loc_003ABFCC;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___StReleaseReadContext(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (80);
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, *(uint64_t *)(arg2 + 0x1A8), a3, a4);
    result = B_TREE_unsigned_long_ST_STORE_SM_TRAITS____ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS___ST_R(Arg1 + 144, *(uint64_t *)(arg2 + 0x1B0), a3, a4);
    if ((*(uint16_t *)(arg1 + 0x12D0)) >= 16) goto loc_003ABFD8;
    result = ExpInterlockedPushEntrySList(Arg1 + 4816, Arg2, a3, a4);
loc_003ABFCC:
    local_rsp = (local_rsp) + (32);
    return result;
loc_003ABFD8:
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, a3, a4);
    goto loc_003ABFCC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg1` | `+ 0x12D0` | `64` | `R` |
| `Arg2` | `+ 0x1A8` | `64` | `R` |
| `Arg2` | `+ 0x1B0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003ABF84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003ABF84[BB_003ABF84]
  bb_003ABFC4[BB_003ABFC4]
  bb_003ABFCC[BB_003ABFCC]
  bb_003ABFD7[BB_003ABFD7]
  bb_003ABFD8[BB_003ABFD8]
  bb_003ABF84 -->|branch| bb_003ABFD8
  bb_003ABF84 -->|fallthrough| bb_003ABFC4
  bb_003ABFC4 -->|flow| bb_003ABFCC
  bb_003ABFD7 -->|flow| bb_003ABFD8
  bb_003ABFD8 -->|branch| bb_003ABFCC
```
