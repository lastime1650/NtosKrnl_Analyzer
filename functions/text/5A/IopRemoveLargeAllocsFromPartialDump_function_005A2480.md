# IopRemoveLargeAllocsFromPartialDump

- RVA: `0x005A2480`–`0x005A24CB` (길이 `75` bytes)
- VA: `0x00000001405A2480`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082420`
- 디코드: `20`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005A24C0` → [IopRemovePageDumpRange](../59/IopRemovePageDumpRange_function_00595EAC.md) (function, `0x00595EAC`)

### Direct callers
- [ExpHeapDumpEnumLargeAllocs](../65/ExpHeapDumpEnumLargeAllocs_function_0065C6CC.md) at `0x0065C75C`

### Static image references
- `0x005A248C` → RVA `0x00E66190` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A2480  4C 8B DC                        mov r11, rsp
005A2483  48 83 EC 48                     sub rsp, 0x48
005A2487  83 64 24 2C 00                  and dword ptr [rsp + 0x2c], 0
005A248C  8B 05 FE 3C 8C 00               mov eax, dword ptr [rip + 0x8c3cfe]
005A2492  85 C0                           test eax, eax
005A2494  74 2F                           je 0x1405a24c5
005A2496  48 C1 E0 14                     shl rax, 0x14
005A249A  48 3B D0                        cmp rdx, rax
005A249D  72 26                           jb 0x1405a24c5
005A249F  49 83 63 D8 00                  and qword ptr [r11 - 0x28], 0
005A24A4  48 C1 EA 0C                     shr rdx, 0xc
005A24A8  49 89 53 F0                     mov qword ptr [r11 - 0x10], rdx
005A24AC  49 8D 53 18                     lea rdx, [r11 + 0x18]
005A24B0  49 89 4B E8                     mov qword ptr [r11 - 0x18], rcx
005A24B4  49 8D 4B D8                     lea rcx, [r11 - 0x28]
005A24B8  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
005A24C0  E8 E7 39 FF FF                  call 0x140595eac
005A24C5  48 83 C4 48                     add rsp, 0x48
005A24C9  C3                              ret
005A24CA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopRemoveLargeAllocsFromPartialDump(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;

    v_rsp = (v_rsp) - (72);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9190654))) == 0) goto loc_005A24C5;
    result = ((unsigned int)(*(unsigned int *)(v_rip + 9190654))) << (20);
    if (a2 >= result) {
        a2 = (a2) >> (12);
        *(unsigned __int64 *)(v_rsp - 16) = a2;
        a2 = v_rsp + 24;
        *(unsigned __int64 *)(v_rsp - 24) = a1;
        a1 = v_rsp - 40;
        v_stack_m20 = 1;
        result = IopRemovePageDumpRange(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopRemoveLargeAllocsFromPartialDump(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;

    local_rsp = (local_rsp) - (72);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8C3CFE))) == 0) goto loc_005A24C5;
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x8C3CFE))) << (20);
    if (Arg2 >= result) {
        Arg2 = (Arg2) >> (12);
        *(uint64_t *)(local_rsp - 0x10) = Arg2;
        Arg2 = local_rsp + 24;
        *(uint64_t *)(local_rsp - 0x18) = Arg1;
        Arg1 = local_rsp - 40;
        v_stack_m20 = 1;
        result = IopRemovePageDumpRange(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A2480&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A2480[BB_005A2480]
  bb_005A2496[BB_005A2496]
  bb_005A249F[BB_005A249F]
  bb_005A24C5[BB_005A24C5]
  bb_005A24CA[BB_005A24CA]
  bb_005A2480 -->|branch| bb_005A24C5
  bb_005A2480 -->|fallthrough| bb_005A2496
  bb_005A2496 -->|branch| bb_005A24C5
  bb_005A2496 -->|fallthrough| bb_005A249F
  bb_005A249F -->|flow| bb_005A24C5
```
