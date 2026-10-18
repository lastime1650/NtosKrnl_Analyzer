# MiCountWslesInPageTable

- RVA: `0x0040D5DC`–`0x0040D6DE` (길이 `258` bytes)
- VA: `0x000000014040D5DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009B180`
- 디코드: `62`개 명령, `258/258` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0040D662` → [MiCountWslesInPageTableRange](MiCountWslesInPageTableRange_function_0040D6F0.md) (function, `0x0040D6F0`)
- `0x0040D6CE` → [MiCountWslesInPageTableRange](MiCountWslesInPageTableRange_function_0040D6F0.md) (function, `0x0040D6F0`)

### Direct callers
- [MiRebuildPageTableAges](MiRebuildPageTableAges_function_0040D4E0.md) at `0x0040D565`

### Static image references
- `0x0040D67D` → RVA `0x00E2F380` (`.data`; read)
- `0x0040D69E` → RVA `0x00E2F390` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0040D5DC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0040D5E1  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0040D5E6  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0040D5EB  57                              push rdi
0040D5EC  48 83 EC 30                     sub rsp, 0x30
0040D5F0  48 8B DA                        mov rbx, rdx
0040D5F3  0F 57 C0                        xorps xmm0, xmm0
0040D5F6  41 0F 11 00                     movups xmmword ptr [r8], xmm0
0040D5FA  41 8B F1                        mov esi, r9d
0040D5FD  48 C1 EB 09                     shr rbx, 9
0040D601  49 B9 F8 FF FF FF 7F 00 00 00   movabs r9, 0x7ffffffff8
0040D60B  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
0040D615  41 0F 11 40 10                  movups xmmword ptr [r8 + 0x10], xmm0
0040D61A  49 8B F8                        mov rdi, r8
0040D61D  49 23 D9                        and rbx, r9
0040D620  41 B8 00 02 00 00               mov r8d, 0x200
0040D626  48 8B E9                        mov rbp, rcx
0040D629  48 8B C2                        mov rax, rdx
0040D62C  48 03 D8                        add rbx, rax
0040D62F  48 8B CB                        mov rcx, rbx
0040D632  48 C1 E9 09                     shr rcx, 9
0040D636  49 23 C9                        and rcx, r9
0040D639  48 8B C2                        mov rax, rdx
0040D63C  48 03 C8                        add rcx, rax
0040D63F  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0040D649  48 3B C8                        cmp rcx, rax
0040D64C  74 2F                           je 0x14040d67d
0040D64E  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
0040D655  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
0040D659  48 8B D3                        mov rdx, rbx
0040D65C  4C 8B CF                        mov r9, rdi
0040D65F  48 8B CD                        mov rcx, rbp
0040D662  E8 89 00 00 00                  call 0x14040d6f0
0040D667  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0040D66C  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0040D671  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0040D676  48 83 C4 30                     add rsp, 0x30
0040D67A  5F                              pop rdi
0040D67B  C3                              ret
0040D67C  CC                              int3
0040D67D  48 8B 0D FC 1C A2 00            mov rcx, qword ptr [rip + 0xa21cfc]
0040D684  41 B9 FF 01 00 00               mov r9d, 0x1ff
0040D68A  48 C1 E9 27                     shr rcx, 0x27
0040D68E  49 23 C9                        and rcx, r9
0040D691  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
0040D69B  49 8B C2                        mov rax, r10
0040D69E  4C 8B 05 EB 1C A2 00            mov r8, qword ptr [rip + 0xa21ceb]
0040D6A5  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0040D6A9  49 C1 E8 27                     shr r8, 0x27
0040D6AD  4D 23 C1                        and r8, r9
0040D6B0  49 C1 E0 03                     shl r8, 3
0040D6B4  4C 2B C2                        sub r8, rdx
0040D6B7  49 8B C2                        mov rax, r10
0040D6BA  4C 03 C0                        add r8, rax
0040D6BD  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
0040D6C1  49 C1 F8 03                     sar r8, 3
0040D6C5  4C 8B CF                        mov r9, rdi
0040D6C8  49 FF C0                        inc r8
0040D6CB  48 8B CD                        mov rcx, rbp
0040D6CE  E8 1D 00 00 00                  call 0x14040d6f0
0040D6D3  41 B8 00 01 00 00               mov r8d, 0x100
0040D6D9  E9 70 FF FF FF                  jmp 0x14040d64e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCountWslesInPageTable(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(a3) = v_xmm0;
    v_rbx = (a2) >> (9);
    *(unsigned __int64 *)(a3 + 16) = v_xmm0;
    v_rbx = (v_rbx) & (a4);
    v_rbx = (v_rbx) + (a2);
    a1 = (v_rbx) >> (9);
    a1 = (a1) & (a4);
    a1 = (a1) + (a2);
    if (a1 == a2) goto loc_0040D67D;
loc_0040D64E:
    v_rbx = (v_rbx) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m18 = (unsigned int)((unsigned int)(a4));
    result = MiCountWslesInPageTableRange(a1, v_rbx, 512, a3);
    v_rsp = (v_rsp) + (48);
    return result;
loc_0040D67D:
    a1 = (*(unsigned __int64 *)(v_rip + 10624252)) >> (39);
    a1 = (a1) & (511);
    a3 = (*(unsigned __int64 *)(v_rip + 10624235)) >> (39);
    a3 = (a3) & (511);
    a3 = (a3) << (3);
    a3 = (a3) - (v_r10 + a1 * 8);
    a3 = (a3) + (v_r10);
    v_stack_p20 = (unsigned int)(v_stack_p18);
    a3 = (a3) >> (3);
    a3 = (a3) + 1;
    result = MiCountWslesInPageTableRange(v_stack_p10, v_r10 + a1 * 8, a3, a3);
    goto loc_0040D64E;
}
```

## 5. (Beta) C Style

```c
int64_t MiCountWslesInPageTable(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(arg3) = v_xmm0;
    local_rbx = (Arg2) >> (9);
    *(uint64_t *)(arg3 + 0x10) = v_xmm0;
    local_rbx = (local_rbx) & (Arg4);
    local_rbx = (local_rbx) + (Arg2);
    Arg1 = (local_rbx) >> (9);
    Arg1 = (Arg1) & (Arg4);
    Arg1 = (Arg1) + (Arg2);
    if (Arg1 == Arg2) goto loc_0040D67D;
loc_0040D64E:
    local_rbx = (local_rbx) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m18 = (uint32_t)((uint32_t)(Arg4));
    result = MiCountWslesInPageTableRange(Arg1, local_rbx, 512, Arg3);
    local_rsp = (local_rsp) + (48);
    return result;
loc_0040D67D:
    Arg1 = (*(uint64_t *)(v_rip + 0xA21CFC)) >> (39);
    Arg1 = (Arg1) & (511);
    Arg3 = (*(uint64_t *)(v_rip + 0xA21CEB)) >> (39);
    Arg3 = (Arg3) & (511);
    Arg3 = (Arg3) << (3);
    Arg3 = (Arg3) - (local_r10 + Arg1 * 8);
    Arg3 = (Arg3) + (local_r10);
    v_stack_p20 = (uint32_t)(v_stack_p18);
    Arg3 = (Arg3) >> (3);
    Arg3 = (Arg3) + 1;
    result = MiCountWslesInPageTableRange(v_stack_p10, local_r10 + Arg1 * 8, Arg3, Arg3);
    goto loc_0040D64E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `128` | `R` |
| `Arg3` | `+ 0x10` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0040D5DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0040D5DC[BB_0040D5DC]
  bb_0040D64E[BB_0040D64E]
  bb_0040D67C[BB_0040D67C]
  bb_0040D67D[BB_0040D67D]
  bb_0040D5DC -->|branch| bb_0040D67D
  bb_0040D5DC -->|fallthrough| bb_0040D64E
  bb_0040D67C -->|flow| bb_0040D67D
  bb_0040D67D -->|branch| bb_0040D64E
```
