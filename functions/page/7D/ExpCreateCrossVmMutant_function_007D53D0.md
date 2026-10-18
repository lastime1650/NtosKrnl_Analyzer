# ExpCreateCrossVmMutant

- RVA: `0x007D53D0`–`0x007D548E` (길이 `190` bytes)
- VA: `0x00000001407D53D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EE78`
- 디코드: `52`개 명령, `190/190` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007D5416` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x007D5456` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x007D546C` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)

### Direct callers
- [NtCreateCrossVmMutant](NtCreateCrossVmMutant_function_007D27E0.md) at `0x007D284D`

### Static image references
- `0x007D53F0` → RVA `0x00EFA120` (`.data`; read)
- `0x007D540B` → RVA `0x00EFA118` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007D5416` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x007D5456` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x007D546C` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D53D0  48 8B C4                        mov rax, rsp
007D53D3  48 89 58 08                     mov qword ptr [rax + 8], rbx
007D53D7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
007D53DB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
007D53DF  57                              push rdi
007D53E0  41 56                           push r14
007D53E2  41 57                           push r15
007D53E4  48 83 EC 50                     sub rsp, 0x50
007D53E8  48 83 60 D8 00                  and qword ptr [rax - 0x28], 0
007D53ED  48 8B F1                        mov rsi, rcx
007D53F0  48 8B 3D 29 4D 72 00            mov rdi, qword ptr [rip + 0x724d29]
007D53F7  41 8B E9                        mov ebp, r9d
007D53FA  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
007D5402  4D 8B F0                        mov r14, r8
007D5405  48 85 DB                        test rbx, rbx
007D5408  44 8B FA                        mov r15d, edx
007D540B  48 0F 44 3D 05 4D 72 00         cmove rdi, qword ptr [rip + 0x724d05]
007D5413  48 8B CF                        mov rcx, rdi
007D5416  E8 F9 33 C5 FF                  call 0x140428814
007D541B  48 85 C0                        test rax, rax
007D541E  75 07                           jne 0x1407d5427
007D5420  BB 02 00 00 C0                  mov ebx, 0xc0000002
007D5425  EB 4A                           jmp 0x1407d5471
007D5427  8A 8C 24 A0 00 00 00            mov cl, byte ptr [rsp + 0xa0]
007D542E  44 8B CD                        mov r9d, ebp
007D5431  48 8B 40 48                     mov rax, qword ptr [rax + 0x48]
007D5435  4D 8B C6                        mov r8, r14
007D5438  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
007D543C  41 8B D7                        mov edx, r15d
007D543F  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
007D5447  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
007D544C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
007D5451  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007D5456  E8 75 56 EE FF                  call 0x1406baad0
007D545B  8B D8                           mov ebx, eax
007D545D  85 C0                           test eax, eax
007D545F  78 08                           js 0x1407d5469
007D5461  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
007D5466  48 89 16                        mov qword ptr [rsi], rdx
007D5469  48 8B CF                        mov rcx, rdi
007D546C  E8 4F 19 C8 FF                  call 0x140456dc0
007D5471  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
007D5476  8B C3                           mov eax, ebx
007D5478  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
007D547C  49 8B 6B 28                     mov rbp, qword ptr [r11 + 0x28]
007D5480  49 8B 73 30                     mov rsi, qword ptr [r11 + 0x30]
007D5484  49 8B E3                        mov rsp, r11
007D5487  41 5F                           pop r15
007D5489  41 5E                           pop r14
007D548B  5F                              pop rdi
007D548C  C3                              ret
007D548D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpCreateCrossVmMutant(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6, unsigned __int8 a7)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (80);
    v_rdi = *(unsigned __int64 *)(v_rip + 7490857);
    if (a6 == 0) { v_rdi = *(unsigned __int64 *)(v_rip + 7490821); }
    result = ExGetExtensionTable(v_rdi, a2, a3, a4);
    if (result != 0) goto loc_007D5427;
    goto loc_007D5471;
loc_007D5427:
    v_stack_m38 = a7;
    v_stack_m40 = (unsigned int)(0xC0000002ULL);
    v_stack_m48 = a5;
    result = guard_dispatch_icall(v_stack_m28, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (!(sign_flag)) {
        a2 = v_stack_m28;
        *(unsigned __int64 *)(a1) = a2;
    }
    result = ExReleaseExtensionTable(v_rdi, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
loc_007D5471:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t ExpCreateCrossVmMutant(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, uint8_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint8_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (80);
    local_rdi = *(uint64_t *)(v_rip + 0x724D29);
    if (Arg6 == 0) { local_rdi = *(uint64_t *)(v_rip + 0x724D05); }
    result = ExGetExtensionTable(local_rdi, Arg2, Arg3, Arg4);
    if (result != 0) goto loc_007D5427;
    goto loc_007D5471;
loc_007D5427:
    v_stack_m38 = Arg7;
    v_stack_m40 = (uint32_t)(0xC0000002ULL);
    v_stack_m48 = Arg5;
    result = guard_dispatch_icall(v_stack_m28, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (!(sign_flag)) {
        Arg2 = v_stack_m28;
        *(uint64_t *)(arg1) = Arg2;
    }
    result = ExReleaseExtensionTable(local_rdi, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
loc_007D5471:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D53D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D53D0[BB_007D53D0]
  bb_007D5420[BB_007D5420]
  bb_007D5427[BB_007D5427]
  bb_007D5461[BB_007D5461]
  bb_007D5469[BB_007D5469]
  bb_007D5471[BB_007D5471]
  bb_007D548D[BB_007D548D]
  bb_007D53D0 -->|branch| bb_007D5427
  bb_007D53D0 -->|fallthrough| bb_007D5420
  bb_007D5420 -->|branch| bb_007D5471
  bb_007D5427 -->|branch| bb_007D5469
  bb_007D5427 -->|fallthrough| bb_007D5461
  bb_007D5461 -->|flow| bb_007D5469
  bb_007D5469 -->|flow| bb_007D5471
```
