# EmonAllocateCounterOriginal

- RVA: `0x0055C24C`–`0x0055C325` (길이 `217` bytes)
- VA: `0x000000014055C24C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `59`개 명령, `217/217` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0055C274` → [HalpAllocateHalCounters](../53/HalpAllocateHalCounters_function_0053FF88.md) (function, `0x0053FF88`)
- `0x0055C2C3` → [EmonFindCounterToAllocateOriginal](EmonFindCounterToAllocateOriginal_function_0055CCA4.md) (function, `0x0055CCA4`)
- `0x0055C2E0` → [EmonAllocateCounterInternal](EmonAllocateCounterInternal_function_0055C190.md) (function, `0x0055C190`)

### Direct callers
- [EmonEnableMonitoringOriginal](EmonEnableMonitoringOriginal_function_0055CA40.md) at `0x0055CB02`

### Static image references
- `0x0055C297` → RVA `0x00FC8C40` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0055C24C  48 8B C4                        mov rax, rsp
0055C24F  48 89 58 08                     mov qword ptr [rax + 8], rbx
0055C253  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0055C257  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0055C25B  57                              push rdi
0055C25C  41 56                           push r14
0055C25E  41 57                           push r15
0055C260  48 83 EC 40                     sub rsp, 0x40
0055C264  83 60 D8 00                     and dword ptr [rax - 0x28], 0
0055C268  4D 8B F1                        mov r14, r9
0055C26B  41 8B E8                        mov ebp, r8d
0055C26E  48 8B FA                        mov rdi, rdx
0055C271  44 8B F9                        mov r15d, ecx
0055C274  E8 0F 3D FE FF                  call 0x14053ff88
0055C279  85 C0                           test eax, eax
0055C27B  0F 88 85 00 00 00               js 0x14055c306
0055C281  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0055C289  48 85 D2                        test rdx, rdx
0055C28C  74 1E                           je 0x14055c2ac
0055C28E  80 BA 3C 01 00 00 00            cmp byte ptr [rdx + 0x13c], 0
0055C295  74 15                           je 0x14055c2ac
0055C297  48 8D 0D A2 C9 A6 00            lea rcx, [rip + 0xa6c9a2]
0055C29E  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0055C2A2  48 8B 70 58                     mov rsi, qword ptr [rax + 0x58]
0055C2A6  48 83 C6 18                     add rsi, 0x18
0055C2AA  EB 0F                           jmp 0x14055c2bb
0055C2AC  48 8D 0D 8D C9 A6 00            lea rcx, [rip + 0xa6c98d]
0055C2B3  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0055C2B7  48 8B 70 58                     mov rsi, qword ptr [rax + 0x58]
0055C2BB  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
0055C2C0  48 8B CE                        mov rcx, rsi
0055C2C3  E8 DC 09 00 00                  call 0x14055cca4
0055C2C8  84 C0                           test al, al
0055C2CA  74 2C                           je 0x14055c2f8
0055C2CC  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
0055C2D0  44 8B CD                        mov r9d, ebp
0055C2D3  4C 8B C7                        mov r8, rdi
0055C2D6  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0055C2DA  41 8B D7                        mov edx, r15d
0055C2DD  48 8B CE                        mov rcx, rsi
0055C2E0  E8 AB FE FF FF                  call 0x14055c190
0055C2E5  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0055C2ED  8B 0E                           mov ecx, dword ptr [rsi]
0055C2EF  41 89 1E                        mov dword ptr [r14], ebx
0055C2F2  89 08                           mov dword ptr [rax], ecx
0055C2F4  33 C0                           xor eax, eax
0055C2F6  EB 13                           jmp 0x14055c30b
0055C2F8  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0055C301  F0 83 40 60 FE                  lock add dword ptr [rax + 0x60], -2
0055C306  B8 11 00 00 80                  mov eax, 0x80000011
0055C30B  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0055C310  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0055C315  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0055C31A  48 83 C4 40                     add rsp, 0x40
0055C31E  41 5F                           pop r15
0055C320  41 5E                           pop r14
0055C322  5F                              pop rdi
0055C323  C3                              ret
0055C324  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmonAllocateCounterOriginal(int a1, __int64 a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = HalpAllocateHalCounters(a1, a2, a3, a4);
    if (sign_flag) goto loc_0055C306;
    if (a2 == 0) goto loc_0055C2AC;
    if ((*(unsigned __int8 *)(a2 + 316)) == 0) goto loc_0055C2AC;
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10930594 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8) + 88)) + (24);
    goto loc_0055C2BB;
loc_0055C2AC:
loc_0055C2BB:
    result = EmonFindCounterToAllocateOriginal(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10930573 + *(unsigned __int64 *)(v_rip + 10930594 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8) * 8) + 88), a2, v_stack_m28, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0055C2F8;
    v_stack_m38 = (unsigned int)((unsigned int)(v_stack_m28));
    result = EmonAllocateCounterInternal(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10930573 + *(unsigned __int64 *)(v_rip + 10930594 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8) * 8) + 88), (unsigned int)((unsigned int)((unsigned int)(a1))), a2, (unsigned int)((unsigned int)((unsigned int)(a3))));
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(v_stack_m28));
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10930573 + *(unsigned __int64 *)(v_rip + 10930594 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8) * 8) + 88))));
    result = 0;
    goto loc_0055C30B;
loc_0055C2F8:
loc_0055C306:
loc_0055C30B:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(0x80000011ULL);
}
```

## 5. (Beta) C Style

```c
int64_t EmonAllocateCounterOriginal(int32_t Arg1, int64_t Arg2, int32_t Arg3, void *Arg4, void *Arg5)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = HalpAllocateHalCounters(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0055C306;
    if (Arg2 == 0) goto loc_0055C2AC;
    if ((*(uint8_t *)(Arg2 + 0x13C)) == 0) goto loc_0055C2AC;
    local_rsi = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA6C9A2 + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8) + 0x58)) + (24);
    goto loc_0055C2BB;
loc_0055C2AC:
loc_0055C2BB:
    result = EmonFindCounterToAllocateOriginal(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA6C98D + *(uint64_t *)(v_rip + 0xA6C9A2 + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8) * 8) + 0x58), Arg2, v_stack_m28, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0055C2F8;
    v_stack_m38 = (uint32_t)((uint32_t)(v_stack_m28));
    result = EmonAllocateCounterInternal(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA6C98D + *(uint64_t *)(v_rip + 0xA6C9A2 + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8) * 8) + 0x58), (uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(v_stack_m28));
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA6C98D + *(uint64_t *)(v_rip + 0xA6C9A2 + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8) * 8) + 0x58))));
    result = 0;
    goto loc_0055C30B;
loc_0055C2F8:
loc_0055C306:
loc_0055C30B:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(0x80000011ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0055C24C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0055C24C[BB_0055C24C]
  bb_0055C281[BB_0055C281]
  bb_0055C28E[BB_0055C28E]
  bb_0055C297[BB_0055C297]
  bb_0055C2AC[BB_0055C2AC]
  bb_0055C2BB[BB_0055C2BB]
  bb_0055C2CC[BB_0055C2CC]
  bb_0055C2F8[BB_0055C2F8]
  bb_0055C306[BB_0055C306]
  bb_0055C30B[BB_0055C30B]
  bb_0055C324[BB_0055C324]
  bb_0055C24C -->|branch| bb_0055C306
  bb_0055C24C -->|fallthrough| bb_0055C281
  bb_0055C281 -->|branch| bb_0055C2AC
  bb_0055C281 -->|fallthrough| bb_0055C28E
  bb_0055C28E -->|branch| bb_0055C2AC
  bb_0055C28E -->|fallthrough| bb_0055C297
  bb_0055C297 -->|branch| bb_0055C2BB
  bb_0055C2AC -->|flow| bb_0055C2BB
  bb_0055C2BB -->|branch| bb_0055C2F8
  bb_0055C2BB -->|fallthrough| bb_0055C2CC
  bb_0055C2CC -->|branch| bb_0055C30B
  bb_0055C2F8 -->|flow| bb_0055C306
  bb_0055C306 -->|flow| bb_0055C30B
```
