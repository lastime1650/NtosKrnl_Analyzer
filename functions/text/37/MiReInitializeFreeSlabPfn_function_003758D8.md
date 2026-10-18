# MiReInitializeFreeSlabPfn

- RVA: `0x003758D8`–`0x0037594D` (길이 `117` bytes)
- VA: `0x00000001403758D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `31`개 명령, `117/117` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00375927` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)

### Direct callers
- [MiFreePageToSlabAllocator](../2A/MiFreePageToSlabAllocator_function_002A0A60.md) at `0x002A0B46`
- [MiCreateSlabEntry](MiCreateSlabEntry_function_00374DEC.md) at `0x003751AB`
- [MiGetRepurposedSlabStandbyPage](MiGetRepurposedSlabStandbyPage_function_003755A8.md) at `0x0037569A`
- [MiRepurposeStandbySlabPage](../38/MiRepurposeStandbySlabPage_function_00385780.md) at `0x00385968`

### Static image references
- `0x00375913` → RVA `0x00010880` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003758D8  48 83 EC 28                     sub rsp, 0x28
003758DC  33 C0                           xor eax, eax
003758DE  4C 8B C1                        mov r8, rcx
003758E1  83 BA 80 00 00 00 02            cmp dword ptr [rdx + 0x80], 2
003758E8  0F 95 C0                        setne al
003758EB  48 83 C0 FE                     add rax, -2
003758EF  48 89 41 08                     mov qword ptr [rcx + 8], rax
003758F3  48 C7 01 00 00 00 00            mov qword ptr [rcx], 0
003758FA  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
003758FE  48 B9 00 00 00 00 00 FF FF FF   movabs rcx, 0xffffff0000000000
00375908  48 23 C1                        and rax, rcx
0037590B  49 8D 48 10                     lea rcx, [r8 + 0x10]
0037590F  49 89 40 18                     mov qword ptr [r8 + 0x18], rax
00375913  48 8B 05 66 AF C9 FF            mov rax, qword ptr [rip - 0x36509a]
0037591A  48 89 01                        mov qword ptr [rcx], rax
0037591D  41 8A 40 22                     mov al, byte ptr [r8 + 0x22]
00375921  24 07                           and al, 7
00375923  3C 01                           cmp al, 1
00375925  75 05                           jne 0x14037592c
00375927  E8 70 50 F1 FF                  call 0x14028a99c
0037592C  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
00375930  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00375934  C1 E8 10                        shr eax, 0x10
00375937  24 FD                           and al, 0xfd
00375939  0C 05                           or al, 5
0037593B  88 44 24 32                     mov byte ptr [rsp + 0x32], al
0037593F  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00375943  41 89 40 20                     mov dword ptr [r8 + 0x20], eax
00375947  48 83 C4 28                     add rsp, 0x28
0037594B  C3                              ret
0037594C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReInitializeFreeSlabPfn(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p8;
    unsigned __int8 v_stack_pA;

    v_rsp = (v_rsp) - (40);
    result = 0;
    result = ((*(unsigned int *)(a2 + 128)) != 2) ? 1 : 0;
    result = (result) + (-2);
    *(unsigned __int64 *)(a1 + 8) = result;
    *(unsigned __int64 *)(a1) = 0;
    result = (*(unsigned __int64 *)(a1 + 24)) & (a1);
    *(unsigned __int64 *)(a1 + 24) = result;
    *(unsigned __int64 *)(a1 + 16) = *(unsigned __int64 *)(v_rip - 3559578);
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 34)) & (7));
    if (((unsigned __int8)(result)) == 1) {
        result = MiSetOriginalPtePfnFromFreeList(a1 + 16, a2, a1, a4);
    }
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_pA = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(v_stack_p8);
}
```

## 5. (Beta) C Style

```c
int64_t MiReInitializeFreeSlabPfn(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p8;
    uint8_t v_stack_pA;

    local_rsp = (local_rsp) - (40);
    result = 0;
    result = ((*(uint32_t *)(arg2 + 0x80)) != 2) ? 1 : 0;
    result = (result) + (-2);
    *(uint64_t *)(arg1 + 0x8) = result;
    *(uint64_t *)(arg1) = 0;
    result = (*(uint64_t *)(arg1 + 0x18)) & (Arg1);
    *(uint64_t *)(arg1 + 0x18) = result;
    *(uint64_t *)(arg1 + 0x10) = *(uint64_t *)(v_rip - 0x36509A);
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x22)) & (7));
    if (((uint8_t)(result)) == 1) {
        result = MiSetOriginalPtePfnFromFreeList(Arg1 + 16, Arg2, Arg1, a4);
    }
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_pA = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(v_stack_p8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x22` | `8` | `R` |
| `Arg2` | `+ 0x80` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003758D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003758D8[BB_003758D8]
  bb_00375927[BB_00375927]
  bb_0037592C[BB_0037592C]
  bb_0037594C[BB_0037594C]
  bb_003758D8 -->|branch| bb_0037592C
  bb_003758D8 -->|fallthrough| bb_00375927
  bb_00375927 -->|flow| bb_0037592C
```
