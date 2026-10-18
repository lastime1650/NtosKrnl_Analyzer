# MmCreateSection

- RVA: `0x009838B0`–`0x0098394F` (길이 `159` bytes)
- VA: `0x00000001409838B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097A24`
- 디코드: `38`개 명령, `159/159` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00983917` → [MmCreateSectionEx](MmCreateSectionEx_function_009839CC.md) (function, `0x009839CC`)

### Direct callers
- [DifMmCreateSectionWrapper](../../text/63/DifMmCreateSectionWrapper_function_00634EB0.md) at `0x00634FE1`
- [EtwpCoverageEnsureContext](../70/EtwpCoverageEnsureContext_function_007028E4.md) at `0x00702B11`
- [NtCreateIoRing](../72/NtCreateIoRing_function_00720530.md) at `0x00720824`
- [PspApiSetCopyToSystemSpace](../77/PspApiSetCopyToSystemSpace_function_0077F648.md) at `0x0077F6A7`
- [PspSiloInitializeUserSharedData](../78/PspSiloInitializeUserSharedData_function_00780684.md) at `0x007806D6`
- [MiInitializeCfg](../../init/C6/MiInitializeCfg_function_00C69958.md) at `0x00C699A2`
- [MiInitializeCfg](../../init/C6/MiInitializeCfg_function_00C69958.md) at `0x00C69A0C`
- [MiInitializeApiSets](../../init/C6/MiInitializeApiSets_function_00C6BA2C.md) at `0x00C6BA7E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009838B0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009838B5  57                              push rdi
009838B6  48 83 EC 70                     sub rsp, 0x70
009838BA  8B 94 24 A8 00 00 00            mov edx, dword ptr [rsp + 0xa8]
009838C1  45 33 D2                        xor r10d, r10d
009838C4  8B C2                           mov eax, edx
009838C6  45 33 DB                        xor r11d, r11d
009838C9  0F 57 C0                        xorps xmm0, xmm0
009838CC  49 8B D9                        mov rbx, r9
009838CF  49 8B F8                        mov rdi, r8
009838D2  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
009838D7  83 E0 7F                        and eax, 0x7f
009838DA  75 4F                           jne 0x14098392b
009838DC  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
009838E4  44 8B 8C 24 A0 00 00 00         mov r9d, dword ptr [rsp + 0xa0]
009838EC  4C 8B 03                        mov r8, qword ptr [rbx]
009838EF  44 89 54 24 50                  mov dword ptr [rsp + 0x50], r10d
009838F4  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
009838F9  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
009838FE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00983903  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0098390B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00983910  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00983914  48 8B D7                        mov rdx, rdi
00983917  E8 B0 00 00 00                  call 0x1409839cc
0098391C  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00983924  48 83 C4 70                     add rsp, 0x70
00983928  5F                              pop rdi
00983929  C3                              ret
0098392A  CC                              int3
0098392B  44 21 54 24 6C                  and dword ptr [rsp + 0x6c], r10d
00983930  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00983935  83 E2 80                        and edx, 0xffffff80
00983938  48 C7 44 24 60 02 00 00 00      mov qword ptr [rsp + 0x60], 2
00983941  FF C8                           dec eax
00983943  41 BA 01 00 00 00               mov r10d, 1
00983949  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0098394D  EB 8D                           jmp 0x1409838dc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmCreateSection(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (112);
    v_r10 = 0;
    v_r11 = 0;
    v_stack_m18 = v_xmm0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (127));
    if (condition_is_not_equal) goto loc_0098392B;
loc_009838DC:
    v_stack_m28 = 0;
    v_stack_m30 = 0;
    v_stack_m48 = a8;
    v_stack_m50 = a7;
    v_stack_m58 = (unsigned int)((unsigned int)(a6));
    result = MmCreateSectionEx(a1, a3, *(unsigned __int64 *)(a4), (unsigned int)(a5));
    v_rsp = (v_rsp) + (112);
    return result;
loc_0098392B:
    a2 = (unsigned int)((a3) & (0xFFFFFF80ULL));
    v_stack_p60 = 2;
    result = (unsigned int)((result) - 1);
    v_stack_p68 = (unsigned int)(result);
    goto loc_009838DC;
}
```

## 5. (Beta) C Style

```c
int64_t MmCreateSection(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (112);
    local_r10 = 0;
    local_r11 = 0;
    v_stack_m18 = v_xmm0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (127));
    if (condition_is_not_equal) goto loc_0098392B;
loc_009838DC:
    v_stack_m28 = 0;
    v_stack_m30 = 0;
    v_stack_m48 = Arg8;
    v_stack_m50 = Arg7;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg6));
    result = MmCreateSectionEx(Arg1, Arg3, *(uint64_t *)(arg4), (uint32_t)(Arg5));
    local_rsp = (local_rsp) + (112);
    return result;
loc_0098392B:
    Arg2 = (uint32_t)((Arg3) & (0xFFFFFF80ULL));
    v_stack_p60 = 2;
    result = (uint32_t)((result) - 1);
    v_stack_p68 = (uint32_t)(result);
    goto loc_009838DC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009838B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009838B0[BB_009838B0]
  bb_009838DC[BB_009838DC]
  bb_0098392A[BB_0098392A]
  bb_0098392B[BB_0098392B]
  bb_009838B0 -->|branch| bb_0098392B
  bb_009838B0 -->|fallthrough| bb_009838DC
  bb_0098392A -->|flow| bb_0098392B
  bb_0098392B -->|branch| bb_009838DC
```
