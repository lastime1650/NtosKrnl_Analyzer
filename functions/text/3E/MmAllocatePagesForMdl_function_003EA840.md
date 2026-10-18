# MmAllocatePagesForMdl

- RVA: `0x003EA840`–`0x003EA8B9` (길이 `121` bytes)
- VA: `0x00000001403EA840`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C2A4`
- 디코드: `23`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003EA8AE` → [MiAllocatePagesForMdl](MiAllocatePagesForMdl_function_003EABEC.md) (function, `0x003EABEC`)

### Direct callers
- [DifMmAllocatePagesForMdlWrapper](../63/DifMmAllocatePagesForMdlWrapper_function_00634A40.md) at `0x00634B33`
- [HalpDmaAllocateScatterMemory](../../page/AA/HalpDmaAllocateScatterMemory_function_00AA2D70.md) at `0x00AA2DB6`

### Static image references
- `0x003EA84D` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x003EA8A7` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EA840  48 83 EC 58                     sub rsp, 0x58
003EA844  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003EA84D  4C 8D 15 EC E3 BD 00            lea r10, [rip + 0xbde3ec]
003EA854  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
003EA85A  8B 80 4C 02 00 00               mov eax, dword ptr [rax + 0x24c]
003EA860  49 8B 04 C2                     mov rax, qword ptr [r10 + rax*8]
003EA864  4C 8B 90 C0 00 00 00            mov r10, qword ptr [rax + 0xc0]
003EA86B  41 0F B7 82 8A 00 00 00         movzx eax, word ptr [r10 + 0x8a]
003EA873  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
003EA87C  4D 8B 9A B8 00 00 00            mov r11, qword ptr [r10 + 0xb8]
003EA883  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
003EA888  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
003EA88D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
003EA891  C7 44 24 28 03 00 00 00         mov dword ptr [rsp + 0x28], 3
003EA899  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003EA89E  4D 8B C8                        mov r9, r8
003EA8A1  4C 8B C2                        mov r8, rdx
003EA8A4  48 8B D1                        mov rdx, rcx
003EA8A7  48 8D 0D 52 E4 A4 00            lea rcx, [rip + 0xa4e452]
003EA8AE  E8 39 03 00 00                  call 0x1403eabec
003EA8B3  48 83 C4 58                     add rsp, 0x58
003EA8B7  C3                              ret
003EA8B8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmAllocatePagesForMdl(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    v_stack_m18 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m28 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12444652 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8) + 192) + 138));
    v_stack_m30 = 3;
    v_stack_m38 = a4;
    result = MiAllocatePagesForMdl(v_rip + 10806354, a1, a2, a3);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmAllocatePagesForMdl(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    v_stack_m18 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m28 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBDE3EC + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8) + 0xC0) + 0x8A));
    v_stack_m30 = 3;
    v_stack_m38 = Arg4;
    result = MiAllocatePagesForMdl(v_rip + 10806354, Arg1, Arg2, Arg3);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EA840&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EA840[BB_003EA840]
  bb_003EA8B8[BB_003EA8B8]
```
