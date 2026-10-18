# HalGetScatterGatherList

- RVA: `0x003DFAC0`–`0x003DFB8D` (길이 `205` bytes)
- VA: `0x00000001403DFAC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000948A4`
- 디코드: `46`개 명령, `205/205` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003DFACD` → [HalpDmaGetAdapterVersion](HalpDmaGetAdapterVersion_function_003DEC8C.md) (function, `0x003DEC8C`)
- `0x003DFB18` → [HalBuildScatterGatherListV2](HalBuildScatterGatherListV2_function_003DD120.md) (function, `0x003DD120`)
- `0x003DFB86` → [HalpBuildScatterGatherList](HalpBuildScatterGatherList_function_003DBAF8.md) (function, `0x003DBAF8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003DFAC0  48 81 EC 88 00 00 00            sub rsp, 0x88
003DFAC7  4C 8B DA                        mov r11, rdx
003DFACA  4C 8B D1                        mov r10, rcx
003DFACD  E8 BA F1 FF FF                  call 0x1403dec8c
003DFAD2  49 8B D3                        mov rdx, r11
003DFAD5  83 E8 02                        sub eax, 2
003DFAD8  75 4C                           jne 0x1403dfb26
003DFADA  8A 84 24 C8 00 00 00            mov al, byte ptr [rsp + 0xc8]
003DFAE1  33 C9                           xor ecx, ecx
003DFAE3  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
003DFAE7  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
003DFAEC  49 8B CA                        mov rcx, r10
003DFAEF  88 44 24 38                     mov byte ptr [rsp + 0x38], al
003DFAF3  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
003DFAFB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003DFB00  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
003DFB08  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003DFB0D  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
003DFB14  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003DFB18  E8 03 D6 FF FF                  call 0x1403dd120
003DFB1D  48 81 C4 88 00 00 00            add rsp, 0x88
003DFB24  C3                              ret
003DFB25  CC                              int3
003DFB26  33 C9                           xor ecx, ecx
003DFB28  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
003DFB2D  83 F8 01                        cmp eax, 1
003DFB30  41 8B 40 2C                     mov eax, dword ptr [r8 + 0x2c]
003DFB34  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
003DFB38  4C 2B C8                        sub r9, rax
003DFB3B  4D 2B 48 20                     sub r9, qword ptr [r8 + 0x20]
003DFB3F  8A 84 24 C8 00 00 00            mov al, byte ptr [rsp + 0xc8]
003DFB46  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
003DFB4B  88 44 24 48                     mov byte ptr [rsp + 0x48], al
003DFB4F  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
003DFB57  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003DFB5C  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
003DFB64  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003DFB69  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
003DFB70  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
003DFB74  49 8B CA                        mov rcx, r10
003DFB77  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003DFB7B  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003DFB80  4D 8B C8                        mov r9, r8
003DFB83  45 33 C0                        xor r8d, r8d
003DFB86  E8 6D BF FF FF                  call 0x1403dbaf8
003DFB8B  EB 90                           jmp 0x1403dfb1d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalGetScatterGatherList(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, unsigned __int8 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p70;

    v_rsp = (v_rsp) - (136);
    result = HalpDmaGetAdapterVersion(a1, a2, a3, a4);
    result = (unsigned int)((result) - (2));
    if (condition_is_not_equal) goto loc_003DFB26;
    a1 = 0;
    v_stack_m40 = 0;
    v_stack_m48 = 0;
    v_stack_m50 = a8;
    v_stack_m58 = a7;
    v_stack_m60 = a6;
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = HalBuildScatterGatherListV2(0, a2, a3, a4);
loc_003DFB1D:
    v_rsp = (v_rsp) + (136);
    return result;
loc_003DFB26:
    a1 = 0;
    v_stack_p70 = 0;
    v_stack_p58 = 0;
    a4 = (a4) - ((unsigned int)(*(unsigned int *)(a3 + 44)));
    a4 = (a4) - (*(unsigned __int64 *)(a3 + 32));
    v_stack_p50 = 0;
    v_stack_p48 = a8;
    v_stack_p40 = a7;
    v_stack_p38 = a6;
    v_stack_p30 = 0;
    v_stack_p28 = (unsigned int)((unsigned int)(a5));
    v_stack_p20 = a4;
    a3 = 0;
    result = HalpBuildScatterGatherList(0, a2, a3, a3);
    goto loc_003DFB1D;
}
```

## 5. (Beta) C Style

```c
int64_t HalGetScatterGatherList(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, int64_t Arg7, uint8_t Arg8)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p70;

    local_rsp = (local_rsp) - (136);
    result = HalpDmaGetAdapterVersion(Arg1, Arg2, Arg3, Arg4);
    result = (uint32_t)((result) - (2));
    if (condition_is_not_equal) goto loc_003DFB26;
    Arg1 = 0;
    v_stack_m40 = 0;
    v_stack_m48 = 0;
    v_stack_m50 = Arg8;
    v_stack_m58 = Arg7;
    v_stack_m60 = Arg6;
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = HalBuildScatterGatherListV2(0, Arg2, Arg3, Arg4);
loc_003DFB1D:
    local_rsp = (local_rsp) + (136);
    return result;
loc_003DFB26:
    Arg1 = 0;
    v_stack_p70 = 0;
    v_stack_p58 = 0;
    Arg4 = (Arg4) - ((uint32_t)(*(uint32_t *)(Arg3 + 0x2C)));
    Arg4 = (Arg4) - (*(uint64_t *)(Arg3 + 0x20));
    v_stack_p50 = 0;
    v_stack_p48 = Arg8;
    v_stack_p40 = Arg7;
    v_stack_p38 = Arg6;
    v_stack_p30 = 0;
    v_stack_p28 = (uint32_t)((uint32_t)(Arg5));
    v_stack_p20 = Arg4;
    Arg3 = 0;
    result = HalpBuildScatterGatherList(0, Arg2, Arg3, Arg3);
    goto loc_003DFB1D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DFAC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DFAC0[BB_003DFAC0]
  bb_003DFADA[BB_003DFADA]
  bb_003DFB1D[BB_003DFB1D]
  bb_003DFB25[BB_003DFB25]
  bb_003DFB26[BB_003DFB26]
  bb_003DFAC0 -->|branch| bb_003DFB26
  bb_003DFAC0 -->|fallthrough| bb_003DFADA
  bb_003DFADA -->|flow| bb_003DFB1D
  bb_003DFB25 -->|flow| bb_003DFB26
  bb_003DFB26 -->|branch| bb_003DFB1D
```
