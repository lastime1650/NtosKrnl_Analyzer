# IopProbeAndLockPages

- RVA: `0x00479708`–`0x00479750` (길이 `72` bytes)
- VA: `0x0000000140479708`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000682BC`
- 디코드: `22`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0047971B` → [MmProbeAndLockPages](../23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x00479749` → [MmUpdateMdlTracker](../45/MmUpdateMdlTracker_function_00456468.md) (function, `0x00456468`)

### Direct callers
- [IopAllocateAndPopulateWriteIrp](../40/IopAllocateAndPopulateWriteIrp_function_004011F4.md) at `0x0040140B`

### Static image references
- `0x00479720` → RVA `0x00FC6BBC` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00479708  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0047970D  57                              push rdi
0047970E  48 83 EC 20                     sub rsp, 0x20
00479712  45 33 C0                        xor r8d, r8d
00479715  49 8B D9                        mov rbx, r9
00479718  48 8B F9                        mov rdi, rcx
0047971B  E8 70 22 DC FF                  call 0x14023b990
00479720  8B 05 96 D4 B4 00               mov eax, dword ptr [rip + 0xb4d496]
00479726  A8 01                           test al, 1
00479728  75 0C                           jne 0x140479736
0047972A  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0047972F  48 83 C4 20                     add rsp, 0x20
00479733  5F                              pop rdi
00479734  C3                              ret
00479735  CC                              int3
00479736  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0047973A  4C 8B C3                        mov r8, rbx
0047973D  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00479741  48 8B CF                        mov rcx, rdi
00479744  48 8B 54 C2 70                  mov rdx, qword ptr [rdx + rax*8 + 0x70]
00479749  E8 1A CD FD FF                  call 0x140456468
0047974E  EB DA                           jmp 0x14047972a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopProbeAndLockPages(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    result = MmProbeAndLockPages(a1, a2, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11850902)))) & (1)) != 0) goto loc_00479736;
loc_0047972A:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(*(unsigned int *)(v_rip + 11850902));
loc_00479736:
    result = MmUpdateMdlTracker(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + (unsigned int)(a5) * 8 + 112), v_stack_p8, a4);
    goto loc_0047972A;
}
```

## 5. (Beta) C Style

```c
int64_t IopProbeAndLockPages(int64_t Arg1, int64_t Arg2, int32_t Arg3, void *Arg4, uint32_t Arg5)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    result = MmProbeAndLockPages(Arg1, Arg2, Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB4D496)))) & (1)) != 0) goto loc_00479736;
loc_0047972A:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(*(uint32_t *)(v_rip + 0xB4D496));
loc_00479736:
    result = MmUpdateMdlTracker(Arg1, *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + (uint32_t)(Arg5) * 8 + 0x70), v_stack_p8, Arg4);
    goto loc_0047972A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00479708&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00479708[BB_00479708]
  bb_0047972A[BB_0047972A]
  bb_00479735[BB_00479735]
  bb_00479736[BB_00479736]
  bb_00479708 -->|branch| bb_00479736
  bb_00479708 -->|fallthrough| bb_0047972A
  bb_00479735 -->|flow| bb_00479736
  bb_00479736 -->|branch| bb_0047972A
```
