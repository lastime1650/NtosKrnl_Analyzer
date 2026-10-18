# MiFreePhysicalRange

- RVA: `0x00688CD0`–`0x00688D2C` (길이 `92` bytes)
- VA: `0x0000000140688CD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D8B4C`
- 디코드: `23`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00688D21` → [MmFreeMemoryRanges](../../page/7F/MmFreeMemoryRanges_function_007FC320.md) (function, `0x007FC320`)

### Direct callers
- [MiFreePhysicalPageChain](../2A/MiFreePhysicalPageChain_function_002A9F1C.md) at `0x002A9FD9`
- [MiFreeAwePagesFromMdl](MiFreeAwePagesFromMdl_function_00688984.md) at `0x006889C9`
- [MiFreeContiguousLargePageRun](MiFreeContiguousLargePageRun_function_00688A34.md) at `0x00688A7C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00688D21` → [MmFreeMemoryRanges](../../page/7F/MmFreeMemoryRanges_function_007FC320.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00688CD0  4C 8B DC                        mov r11, rsp
00688CD3  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
00688CD7  48 83 EC 68                     sub rsp, 0x68
00688CDB  83 64 24 34 00                  and dword ptr [rsp + 0x34], 0
00688CE0  B9 01 00 00 00                  mov ecx, 1
00688CE5  0F 57 C0                        xorps xmm0, xmm0
00688CE8  48 C1 E2 0C                     shl rdx, 0xc
00688CEC  F3 0F 7F 44 24 24               movdqu xmmword ptr [rsp + 0x24], xmm0
00688CF2  49 83 63 D8 00                  and qword ptr [r11 - 0x28], 0
00688CF7  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00688CFB  66 0F 7E C0                     movd eax, xmm0
00688CFF  49 89 53 08                     mov qword ptr [r11 + 8], rdx
00688D03  0B C1                           or eax, ecx
00688D05  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00688D09  49 8D 43 08                     lea rax, [r11 + 8]
00688D0D  49 89 4B E0                     mov qword ptr [r11 - 0x20], rcx
00688D11  49 8D 4B B8                     lea rcx, [r11 - 0x48]
00688D15  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00688D19  49 C7 43 D0 00 00 00 40         mov qword ptr [r11 - 0x30], 0x40000000
00688D21  E8 FA 35 17 00                  call 0x1407fc320
00688D26  48 83 C4 68                     add rsp, 0x68
00688D2A  C3                              ret
00688D2B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreePhysicalRange(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m44;
    unsigned int v_stack_m48;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (104);
    a2 = (a2) << (12);
    v_stack_m44 = v_xmm0;
    v_stack_m48 = 1;
    *(unsigned __int64 *)(v_rsp + 8) = a2;
    result = (unsigned int)((result) | (1));
    v_stack_m44 = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 32) = 1;
    *(unsigned __int64 *)(v_rsp - 24) = v_rsp + 8;
    *(unsigned __int64 *)(v_rsp - 48) = 0x40000000ULL;
    result = MmFreeMemoryRanges(v_rsp - 72, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiFreePhysicalRange(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m34;
    uint64_t v_stack_m44;
    uint32_t v_stack_m48;

    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (104);
    Arg2 = (Arg2) << (12);
    v_stack_m44 = v_xmm0;
    v_stack_m48 = 1;
    *(uint64_t *)(local_rsp + 0x8) = Arg2;
    result = (uint32_t)((result) | (1));
    v_stack_m44 = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x20) = 1;
    *(uint64_t *)(local_rsp - 0x18) = local_rsp + 8;
    *(uint64_t *)(local_rsp - 0x30) = 0x40000000ULL;
    result = MmFreeMemoryRanges(local_rsp - 72, Arg2, a3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00688CD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00688CD0[BB_00688CD0]
  bb_00688D2B[BB_00688D2B]
```
