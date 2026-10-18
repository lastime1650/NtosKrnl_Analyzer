# MiMakeGlobalSubsectionPte

- RVA: `0x004DFEA8`–`0x004DFF08` (길이 `96` bytes)
- VA: `0x00000001404DFEA8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `29`개 명령, `96/96` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004DFEBA` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x004DFEFD` → [MiSwizzleInvalidPte](../28/MiSwizzleInvalidPte_function_0028F5E0.md) (function, `0x0028F5E0`)

### Direct callers
- [MiPurgeSubsection](../37/MiPurgeSubsection_function_003712F0.md) at `0x00371AA3`
- [MiPurgeSubsection](../37/MiPurgeSubsection_function_003712F0.md) at `0x00371AE9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004DFEA8  48 83 EC 28                     sub rsp, 0x28
004DFEAC  4C 8B C1                        mov r8, rcx
004DFEAF  4C 8B CA                        mov r9, rdx
004DFEB2  8B 49 20                        mov ecx, dword ptr [rcx + 0x20]
004DFEB5  D1 E9                           shr ecx, 1
004DFEB7  83 E1 1F                        and ecx, 0x1f
004DFEBA  E8 41 7B E5 FF                  call 0x140337a00
004DFEBF  41 83 78 24 00                  cmp dword ptr [r8 + 0x24], 0
004DFEC4  74 3C                           je 0x1404dff02
004DFEC6  4D 2B 48 08                     sub r9, qword ptr [r8 + 8]
004DFECA  41 8B 48 20                     mov ecx, dword ptr [r8 + 0x20]
004DFECE  41 8B 50 28                     mov edx, dword ptr [r8 + 0x28]
004DFED2  C1 E2 09                        shl edx, 9
004DFED5  49 C1 F9 03                     sar r9, 3
004DFED9  C1 E9 14                        shr ecx, 0x14
004DFEDC  0B D1                           or edx, ecx
004DFEDE  41 C1 E1 18                     shl r9d, 0x18
004DFEE2  44 3B CA                        cmp r9d, edx
004DFEE5  73 1B                           jae 0x1404dff02
004DFEE7  41 8B 48 20                     mov ecx, dword ptr [r8 + 0x20]
004DFEEB  83 E1 3E                        and ecx, 0x3e
004DFEEE  49 C1 E0 0C                     shl r8, 0xc
004DFEF2  49 0B C8                        or rcx, r8
004DFEF5  48 83 C9 40                     or rcx, 0x40
004DFEF9  48 C1 E1 04                     shl rcx, 4
004DFEFD  E8 DE F6 DA FF                  call 0x14028f5e0
004DFF02  48 83 C4 28                     add rsp, 0x28
004DFF06  C3                              ret
004DFF07  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMakeGlobalSubsectionPte(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (1));
    a1 = (unsigned int)((a1) & (31));
    result = MiMakeDemandZeroPte(a1, a2, a1, a2);
    if ((*(unsigned int *)(a1 + 36)) == 0) goto loc_004DFF02;
    a4 = (a2) - (*(unsigned __int64 *)(a1 + 8));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) << (9));
    a4 = (a4) >> (3);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (20));
    a2 = (unsigned int)((a2) | ((unsigned int)(a1)));
    a4 = (unsigned int)((a4) << (24));
    if (((unsigned int)(a4)) < ((unsigned int)(a2))) {
        a1 = *(unsigned int *)(a1 + 32);
        a1 = (unsigned int)((a1) & (62));
        a3 = (a1) << (12);
        a1 = (a1) | (a3);
        a1 = (a1) | (64);
        a1 = (a1) << (4);
        result = MiSwizzleInvalidPte(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiMakeGlobalSubsectionPte(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (1));
    Arg1 = (uint32_t)((Arg1) & (31));
    result = MiMakeDemandZeroPte(Arg1, Arg2, Arg1, Arg2);
    if ((*(uint32_t *)(arg1 + 0x24)) == 0) goto loc_004DFF02;
    a4 = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) << (9));
    a4 = (a4) >> (3);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (20));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(Arg1)));
    a4 = (uint32_t)((a4) << (24));
    if (((uint32_t)(a4)) < ((uint32_t)(Arg2))) {
        Arg1 = *(uint32_t *)(arg1 + 0x20);
        Arg1 = (uint32_t)((Arg1) & (62));
        a3 = (Arg1) << (12);
        Arg1 = (Arg1) | (a3);
        Arg1 = (Arg1) | (64);
        Arg1 = (Arg1) << (4);
        result = MiSwizzleInvalidPte(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004DFEA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004DFEA8[BB_004DFEA8]
  bb_004DFEC6[BB_004DFEC6]
  bb_004DFEE7[BB_004DFEE7]
  bb_004DFF02[BB_004DFF02]
  bb_004DFF07[BB_004DFF07]
  bb_004DFEA8 -->|branch| bb_004DFF02
  bb_004DFEA8 -->|fallthrough| bb_004DFEC6
  bb_004DFEC6 -->|branch| bb_004DFF02
  bb_004DFEC6 -->|fallthrough| bb_004DFEE7
  bb_004DFEE7 -->|flow| bb_004DFF02
```
