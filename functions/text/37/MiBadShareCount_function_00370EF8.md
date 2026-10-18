# MiBadShareCount

- RVA: `0x00370EF8`–`0x00370F48` (길이 `80` bytes)
- VA: `0x0000000140370EF8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000622F0`
- 디코드: `16`개 명령, `80/80` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00370F42` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x002853BF`
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x002853D6`
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x0028540F`
- [MiCompletePrivateZeroFault](../33/MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331E28`
- [sub_0033435D](../33/Unknown_function_0033435D.md) at `0x0033435D`
- [MiDeleteClusterPage](../34/MiDeleteClusterPage_function_00346CB0.md) at `0x00347057`
- [MiDecommitPrivatePageTail](../36/MiDecommitPrivatePageTail_function_0036F564.md) at `0x0036F8CF`
- [MiDecommitSharedPageTail](MiDecommitSharedPageTail_function_00370240.md) at `0x00370411`
- [sub_00370DA5](Unknown_function_00370DA5.md) at `0x00370DA8`
- [MiReduceShareCount](MiReduceShareCount_function_00370E90.md) at `0x00370EA1`
- [MiDeleteSectionCluster](MiDeleteSectionCluster_function_00373DF0.md) at `0x00374394`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00370EF8  48 83 EC 38                     sub rsp, 0x38
00370EFC  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00370F00  48 BA FF FF FF FF FF FF FF 3F   movabs rdx, 0x3fffffffffffffff
00370F0A  44 0F B6 49 22                  movzx r9d, byte ptr [rcx + 0x22]
00370F0F  48 23 C2                        and rax, rdx
00370F12  41 83 E1 07                     and r9d, 7
00370F16  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
00370F20  48 2B CA                        sub rcx, rdx
00370F23  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00370F28  48 C1 F9 04                     sar rcx, 4
00370F2C  BA 99 00 00 00                  mov edx, 0x99
00370F31  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
00370F3B  4C 0F AF C1                     imul r8, rcx
00370F3F  8D 4A B5                        lea ecx, [rdx - 0x4b]
00370F42  E8 19 C7 18 00                  call 0x1404fd660
00370F47  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiBadShareCount(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = (*(unsigned __int64 *)(a1 + 24)) & (a2);
    a4 = (unsigned int)((*(unsigned __int8 *)(a1 + 34)) & (7));
    a1 = (a1) - (a2);
    v_stack_m18 = result;
    a1 = (a1) >> (4);
    a3 = (a3) * (a1);
    result = KeBugCheckEx(153 - 75, 153, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiBadShareCount(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = (*(uint64_t *)(arg1 + 0x18)) & (a2);
    a4 = (uint32_t)((*(uint8_t *)(arg1 + 0x22)) & (7));
    Arg1 = (Arg1) - (a2);
    v_stack_m18 = result;
    Arg1 = (Arg1) >> (4);
    a3 = (a3) * (Arg1);
    result = KeBugCheckEx(153 - 75, 153, a3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x22` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00370EF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00370EF8[BB_00370EF8]
```
