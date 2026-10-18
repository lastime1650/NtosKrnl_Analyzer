# NtOpenSection

- RVA: `0x009FF390`–`0x009FF446` (길이 `182` bytes)
- VA: `0x00000001409FF390`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A7864`
- 디코드: `46`개 명령, `182/182` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009FF3E9` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (function, `0x004094A0`)
- `0x009FF414` → [ObOpenObjectByNameEx](../89/ObOpenObjectByNameEx_function_0089A8A0.md) (function, `0x0089A8A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009FF3E2` → RVA `0x00FC6BD8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009FF3E9` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009FF390  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009FF395  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
009FF39A  57                              push rdi
009FF39B  41 56                           push r14
009FF39D  41 57                           push r15
009FF39F  48 83 EC 50                     sub rsp, 0x50
009FF3A3  4D 8B F0                        mov r14, r8
009FF3A6  44 8B FA                        mov r15d, edx
009FF3A9  48 8B F9                        mov rdi, rcx
009FF3AC  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
009FF3B2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009FF3BB  40 8A B0 32 02 00 00            mov sil, byte ptr [rax + 0x232]
009FF3C2  40 84 F6                        test sil, sil
009FF3C5  74 1B                           je 0x1409ff3e2
009FF3C7  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009FF3D1  48 3B CA                        cmp rcx, rdx
009FF3D4  48 0F 42 D1                     cmovb rdx, rcx
009FF3D8  48 8B 02                        mov rax, qword ptr [rdx]
009FF3DB  48 89 02                        mov qword ptr [rdx], rax
009FF3DE  EB 02                           jmp 0x1409ff3e2
009FF3E0  EB 4F                           jmp 0x1409ff431
009FF3E2  48 8B 1D EF 77 5C 00            mov rbx, qword ptr [rip + 0x5c77ef]
009FF3E9  E8 B2 A0 A0 FF                  call 0x1404094a0
009FF3EE  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
009FF3F3  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
009FF3F8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009FF3FD  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
009FF403  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
009FF408  45 33 C9                        xor r9d, r9d
009FF40B  44 8A C6                        mov r8b, sil
009FF40E  48 8B D3                        mov rdx, rbx
009FF411  49 8B CE                        mov rcx, r14
009FF414  E8 87 B4 E9 FF                  call 0x14089a8a0
009FF419  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
009FF420  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009FF425  48 89 0F                        mov qword ptr [rdi], rcx
009FF428  EB 07                           jmp 0x1409ff431
009FF42A  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
009FF431  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
009FF436  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
009FF43B  48 83 C4 50                     add rsp, 0x50
009FF43F  41 5F                           pop r15
009FF441  41 5E                           pop r14
009FF443  5F                              pop rdi
009FF444  C3                              ret
009FF445  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtOpenSection(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (80);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_009FF3E2;
    if (a1 < a2) { a2 = a1; }
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(a2);
    goto loc_009FF3E2;
loc_009FF3E2:
    result = PsGetCurrentSilo(a1, a2, a3, a4);
    v_stack_m30 = v_stack_m28;
    v_stack_m38 = result;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    a4 = 0;
    result = ObOpenObjectByNameEx(a3, *(unsigned __int64 *)(v_rip + 6060015), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    v_stack_p20 = (unsigned int)(result);
    *(unsigned __int64 *)(a1) = v_stack_m28;
    goto loc_009FF431;
loc_009FF431:
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtOpenSection(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (80);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_009FF3E2;
    if (Arg1 < Arg2) { Arg2 = Arg1; }
    *(uint64_t *)(Arg2) = *(uint64_t *)(Arg2);
    goto loc_009FF3E2;
loc_009FF3E2:
    result = PsGetCurrentSilo(Arg1, Arg2, Arg3, Arg4);
    v_stack_m30 = v_stack_m28;
    v_stack_m38 = result;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    Arg4 = 0;
    result = ObOpenObjectByNameEx(Arg3, *(uint64_t *)(v_rip + 0x5C77EF), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    v_stack_p20 = (uint32_t)(result);
    *(uint64_t *)(arg1) = v_stack_m28;
    goto loc_009FF431;
loc_009FF431:
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009FF390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009FF390[BB_009FF390]
  bb_009FF3C7[BB_009FF3C7]
  bb_009FF3E0[BB_009FF3E0]
  bb_009FF3E2[BB_009FF3E2]
  bb_009FF42A[BB_009FF42A]
  bb_009FF431[BB_009FF431]
  bb_009FF445[BB_009FF445]
  bb_009FF390 -->|branch| bb_009FF3E2
  bb_009FF390 -->|fallthrough| bb_009FF3C7
  bb_009FF3C7 -->|branch| bb_009FF3E2
  bb_009FF3E0 -->|branch| bb_009FF431
  bb_009FF3E2 -->|branch| bb_009FF431
  bb_009FF42A -->|flow| bb_009FF431
```
