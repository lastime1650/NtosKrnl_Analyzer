# IopProbeAndLockPages

- RVA: `0x004B1188`–`0x004B11D3` (길이 `75` bytes)
- VA: `0x00000001404B1188`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000682BC`
- 디코드: `22`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B119E` → [MmProbeAndLockPages](../23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x004B11CC` → [MmUpdateMdlTracker](../45/MmUpdateMdlTracker_function_00456468.md) (function, `0x00456468`)

### Direct callers
- [sub_00B1D822](../../page/B1/Unknown_function_00B1D822.md) at `0x00B1D85D`
- [sub_00B3738C](../../page/B3/Unknown_function_00B3738C.md) at `0x00B373DA`

### Static image references
- `0x004B11A3` → RVA `0x00FC6BBC` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B1188  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004B118D  57                              push rdi
004B118E  48 83 EC 20                     sub rsp, 0x20
004B1192  41 B8 01 00 00 00               mov r8d, 1
004B1198  49 8B D9                        mov rbx, r9
004B119B  48 8B F9                        mov rdi, rcx
004B119E  E8 ED A7 D8 FF                  call 0x14023b990
004B11A3  8B 05 13 5A B1 00               mov eax, dword ptr [rip + 0xb15a13]
004B11A9  A8 01                           test al, 1
004B11AB  75 0C                           jne 0x1404b11b9
004B11AD  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004B11B2  48 83 C4 20                     add rsp, 0x20
004B11B6  5F                              pop rdi
004B11B7  C3                              ret
004B11B8  CC                              int3
004B11B9  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
004B11BD  4C 8B C3                        mov r8, rbx
004B11C0  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
004B11C4  48 8B CF                        mov rcx, rdi
004B11C7  48 8B 54 C2 70                  mov rdx, qword ptr [rdx + rax*8 + 0x70]
004B11CC  E8 97 52 FA FF                  call 0x140456468
004B11D1  EB DA                           jmp 0x1404b11ad
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopProbeAndLockPages(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = MmProbeAndLockPages(a1, a2, 1, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11622931)))) & (1)) != 0) goto loc_004B11B9;
loc_004B11AD:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(*(unsigned int *)(v_rip + 11622931));
loc_004B11B9:
    result = MmUpdateMdlTracker(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + (unsigned int)(a5) * 8 + 112), v_stack_p8, a4);
    goto loc_004B11AD;
}
```

## 5. (Beta) C Style

```c
int64_t IopProbeAndLockPages(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = MmProbeAndLockPages(Arg1, Arg2, 1, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB15A13)))) & (1)) != 0) goto loc_004B11B9;
loc_004B11AD:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(*(uint32_t *)(v_rip + 0xB15A13));
loc_004B11B9:
    result = MmUpdateMdlTracker(Arg1, *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + (uint32_t)(Arg5) * 8 + 0x70), v_stack_p8, Arg4);
    goto loc_004B11AD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B1188&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B1188[BB_004B1188]
  bb_004B11AD[BB_004B11AD]
  bb_004B11B8[BB_004B11B8]
  bb_004B11B9[BB_004B11B9]
  bb_004B1188 -->|branch| bb_004B11B9
  bb_004B1188 -->|fallthrough| bb_004B11AD
  bb_004B11B8 -->|flow| bb_004B11B9
  bb_004B11B9 -->|branch| bb_004B11AD
```
