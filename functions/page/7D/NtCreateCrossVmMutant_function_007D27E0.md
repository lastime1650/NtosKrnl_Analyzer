# NtCreateCrossVmMutant

- RVA: `0x007D27E0`–`0x007D2887` (길이 `167` bytes)
- VA: `0x00000001407D27E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D5A48`
- 디코드: `44`개 명령, `167/167` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007D284D` → [ExpCreateCrossVmMutant](ExpCreateCrossVmMutant_function_007D53D0.md) (function, `0x007D53D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D27E0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007D27E5  57                              push rdi
007D27E6  48 83 EC 50                     sub rsp, 0x50
007D27EA  44 8B D2                        mov r10d, edx
007D27ED  48 8B D9                        mov rbx, rcx
007D27F0  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
007D27F6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007D27FF  40 8A B8 32 02 00 00            mov dil, byte ptr [rax + 0x232]
007D2806  40 84 FF                        test dil, dil
007D2809  74 1B                           je 0x1407d2826
007D280B  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
007D2815  48 3B CA                        cmp rcx, rdx
007D2818  48 0F 42 D1                     cmovb rdx, rcx
007D281C  48 8B 02                        mov rax, qword ptr [rdx]
007D281F  48 89 02                        mov qword ptr [rdx], rax
007D2822  EB 02                           jmp 0x1407d2826
007D2824  EB 55                           jmp 0x1407d287b
007D2826  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
007D282B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
007D2833  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007D2838  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007D2840  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007D2845  41 8B D2                        mov edx, r10d
007D2848  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
007D284D  E8 7E 2B 00 00                  call 0x1407d53d0
007D2852  8B D0                           mov edx, eax
007D2854  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007D2858  85 C0                           test eax, eax
007D285A  78 1D                           js 0x1407d2879
007D285C  40 84 FF                        test dil, dil
007D285F  74 10                           je 0x1407d2871
007D2861  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007D2866  48 89 0B                        mov qword ptr [rbx], rcx
007D2869  EB 0E                           jmp 0x1407d2879
007D286B  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
007D286F  EB 08                           jmp 0x1407d2879
007D2871  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
007D2876  48 89 03                        mov qword ptr [rbx], rax
007D2879  8B C2                           mov eax, edx
007D287B  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
007D2880  48 83 C4 50                     add rsp, 0x50
007D2884  5F                              pop rdi
007D2885  C3                              ret
007D2886  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCreateCrossVmMutant(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int8 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_007D2826;
    if (a1 < a2) { a2 = a1; }
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(a2);
    goto loc_007D2826;
loc_007D2826:
    v_stack_m28 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m30 = a6;
    v_stack_m38 = a5;
    result = ExpCreateCrossVmMutant(v_stack_m10, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (sign_flag) goto loc_007D2879;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_007D2871;
    *(unsigned __int64 *)(a1) = v_stack_m10;
    goto loc_007D2879;
loc_007D2871:
    *(unsigned __int64 *)(a1) = v_stack_m10;
loc_007D2879:
loc_007D287B:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t NtCreateCrossVmMutant(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint8_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_007D2826;
    if (Arg1 < Arg2) { Arg2 = Arg1; }
    *(uint64_t *)(Arg2) = *(uint64_t *)(Arg2);
    goto loc_007D2826;
loc_007D2826:
    v_stack_m28 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m30 = Arg6;
    v_stack_m38 = Arg5;
    result = ExpCreateCrossVmMutant(v_stack_m10, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m18 = (uint32_t)(result);
    if (sign_flag) goto loc_007D2879;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_007D2871;
    *(uint64_t *)(arg1) = v_stack_m10;
    goto loc_007D2879;
loc_007D2871:
    *(uint64_t *)(arg1) = v_stack_m10;
loc_007D2879:
loc_007D287B:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D27E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D27E0[BB_007D27E0]
  bb_007D280B[BB_007D280B]
  bb_007D2824[BB_007D2824]
  bb_007D2826[BB_007D2826]
  bb_007D285C[BB_007D285C]
  bb_007D2861[BB_007D2861]
  bb_007D286B[BB_007D286B]
  bb_007D2871[BB_007D2871]
  bb_007D2879[BB_007D2879]
  bb_007D287B[BB_007D287B]
  bb_007D2886[BB_007D2886]
  bb_007D27E0 -->|branch| bb_007D2826
  bb_007D27E0 -->|fallthrough| bb_007D280B
  bb_007D280B -->|branch| bb_007D2826
  bb_007D2824 -->|branch| bb_007D287B
  bb_007D2826 -->|branch| bb_007D2879
  bb_007D2826 -->|fallthrough| bb_007D285C
  bb_007D285C -->|branch| bb_007D2871
  bb_007D285C -->|fallthrough| bb_007D2861
  bb_007D2861 -->|branch| bb_007D2879
  bb_007D286B -->|branch| bb_007D2879
  bb_007D2871 -->|flow| bb_007D2879
  bb_007D2879 -->|flow| bb_007D287B
```
