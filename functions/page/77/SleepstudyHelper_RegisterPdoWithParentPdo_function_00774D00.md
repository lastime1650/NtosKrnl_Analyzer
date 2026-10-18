# SleepstudyHelper_RegisterPdoWithParentPdo

- RVA: `0x00774D00`–`0x00774DC5` (길이 `197` bytes)
- VA: `0x0000000140774D00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDACC`
- 디코드: `60`개 명령, `197/197` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00774D48` → [SleepstudyHelperCreateBlockerFromDevice](../A2/SleepstudyHelperCreateBlockerFromDevice_function_00A2D5F0.md) (function, `0x00A2D5F0`)
- `0x00774D60` → [SleepstudyHelperBuildBlocker](../A2/SleepstudyHelperBuildBlocker_function_00A2DAD0.md) (function, `0x00A2DAD0`)
- `0x00774D86` → [SleepstudyHelperDestroyBlockerBuilder](../A2/SleepstudyHelperDestroyBlockerBuilder_function_00A2DE80.md) (function, `0x00A2DE80`)
- `0x00774D93` → [SleepstudyHelperDestroyBlocker](../../text/48/SleepstudyHelperDestroyBlocker_function_00486930.md) (function, `0x00486930`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00774DA0` → RVA `0x00F06B68` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00774D93` → [SleepstudyHelperDestroyBlocker](../../text/48/SleepstudyHelperDestroyBlocker_function_00486930.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00774D00  48 8B C4                        mov rax, rsp
00774D03  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00774D07  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00774D0B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00774D0F  41 56                           push r14
00774D11  48 83 EC 40                     sub rsp, 0x40
00774D15  33 F6                           xor esi, esi
00774D17  33 FF                           xor edi, edi
00774D19  48 89 70 08                     mov qword ptr [rax + 8], rsi
00774D1D  4D 8B F1                        mov r14, r9
00774D20  48 89 78 D8                     mov qword ptr [rax - 0x28], rdi
00774D24  48 85 C9                        test rcx, rcx
00774D27  74 50                           je 0x140774d79
00774D29  48 85 D2                        test rdx, rdx
00774D2C  74 4B                           je 0x140774d79
00774D2E  4D 85 C0                        test r8, r8
00774D31  74 46                           je 0x140774d79
00774D33  4D 85 C9                        test r9, r9
00774D36  74 41                           je 0x140774d79
00774D38  48 21 70 E8                     and qword ptr [rax - 0x18], rsi
00774D3C  4C 8D 48 D8                     lea r9, [rax - 0x28]
00774D40  48 89 50 E0                     mov qword ptr [rax - 0x20], rdx
00774D44  48 8D 50 E0                     lea rdx, [rax - 0x20]
00774D48  E8 A3 88 2B 00                  call 0x140a2d5f0
00774D4D  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
00774D52  8B D8                           mov ebx, eax
00774D54  85 C0                           test eax, eax
00774D56  78 26                           js 0x140774d7e
00774D58  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00774D5D  48 8B CF                        mov rcx, rdi
00774D60  E8 6B 8D 2B 00                  call 0x140a2dad0
00774D65  8B D8                           mov ebx, eax
00774D67  85 C0                           test eax, eax
00774D69  78 07                           js 0x140774d72
00774D6B  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00774D70  EB 37                           jmp 0x140774da9
00774D72  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00774D77  EB 05                           jmp 0x140774d7e
00774D79  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00774D7E  48 85 FF                        test rdi, rdi
00774D81  74 08                           je 0x140774d8b
00774D83  48 8B CF                        mov rcx, rdi
00774D86  E8 F5 90 2B 00                  call 0x140a2de80
00774D8B  48 85 F6                        test rsi, rsi
00774D8E  74 08                           je 0x140774d98
00774D90  48 8B CE                        mov rcx, rsi
00774D93  E8 98 1B D1 FF                  call 0x140486930
00774D98  81 FB BB 00 00 C0               cmp ebx, 0xc00000bb
00774D9E  75 0C                           jne 0x140774dac
00774DA0  48 8D 05 C1 1D 79 00            lea rax, [rip + 0x791dc1]
00774DA7  33 DB                           xor ebx, ebx
00774DA9  49 89 06                        mov qword ptr [r14], rax
00774DAC  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00774DB1  8B C3                           mov eax, ebx
00774DB3  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00774DB8  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00774DBD  48 83 C4 40                     add rsp, 0x40
00774DC1  41 5E                           pop r14
00774DC3  C3                              ret
00774DC4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SleepstudyHelper_RegisterPdoWithParentPdo(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    v_rsi = 0;
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp + 8) = 0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    if (a1 == 0) goto loc_00774D79;
    if (a2 == 0) goto loc_00774D79;
    if (a3 == 0) goto loc_00774D79;
    if (a4 == 0) goto loc_00774D79;
    *(unsigned __int64 *)(v_rsp - 32) = a2;
    result = SleepstudyHelperCreateBlockerFromDevice(a1, v_rsp - 32, a3, v_rsp - 40);
    if (sign_flag) goto loc_00774D7E;
    result = SleepstudyHelperBuildBlocker(v_stack_m28, v_stack_p8, a3, v_rsp - 40);
    if (sign_flag) goto loc_00774D72;
    goto loc_00774DA9;
loc_00774D72:
    goto loc_00774D7E;
loc_00774D79:
loc_00774D7E:
    result = v_stack_p8;
    if (v_stack_m28 != 0) {
        a1 = v_stack_m28;
        result = SleepstudyHelperDestroyBlockerBuilder(a1, v_stack_p8, a3, v_rsp - 40);
    }
    if (v_stack_p8 != 0) {
        a1 = v_stack_p8;
        result = SleepstudyHelperDestroyBlocker(a1, v_stack_p8, a3, v_rsp - 40);
    }
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 0xC00000BBULL) goto loc_00774DAC;
    v_rbx = 0;
loc_00774DA9:
    *(unsigned __int64 *)(a4) = v_rip + 7937473;
loc_00774DAC:
    v_rsp = (v_rsp) + (64);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t SleepstudyHelper_RegisterPdoWithParentPdo(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    local_rsi = 0;
    local_rdi = 0;
    *(uint64_t *)(local_rsp + 0x8) = 0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    if (Arg1 == 0) goto loc_00774D79;
    if (Arg2 == 0) goto loc_00774D79;
    if (Arg3 == 0) goto loc_00774D79;
    if (Arg4 == NULL) goto loc_00774D79;
    *(uint64_t *)(local_rsp - 0x20) = Arg2;
    result = SleepstudyHelperCreateBlockerFromDevice(Arg1, local_rsp - 32, Arg3, local_rsp - 40);
    if (sign_flag) goto loc_00774D7E;
    result = SleepstudyHelperBuildBlocker(v_stack_m28, v_stack_p8, Arg3, local_rsp - 40);
    if (sign_flag) goto loc_00774D72;
    goto loc_00774DA9;
loc_00774D72:
    goto loc_00774D7E;
loc_00774D79:
loc_00774D7E:
    result = v_stack_p8;
    if (v_stack_m28 != 0) {
        Arg1 = v_stack_m28;
        result = SleepstudyHelperDestroyBlockerBuilder(Arg1, v_stack_p8, Arg3, local_rsp - 40);
    }
    if (v_stack_p8 != 0) {
        Arg1 = v_stack_p8;
        result = SleepstudyHelperDestroyBlocker(Arg1, v_stack_p8, Arg3, local_rsp - 40);
    }
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 0xC00000BBULL) goto loc_00774DAC;
    local_rbx = 0;
loc_00774DA9:
    *(uint64_t *)(arg4) = v_rip + 7937473;
loc_00774DAC:
    local_rsp = (local_rsp) + (64);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00774D00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00774D00[BB_00774D00]
  bb_00774D29[BB_00774D29]
  bb_00774D2E[BB_00774D2E]
  bb_00774D33[BB_00774D33]
  bb_00774D38[BB_00774D38]
  bb_00774D58[BB_00774D58]
  bb_00774D6B[BB_00774D6B]
  bb_00774D72[BB_00774D72]
  bb_00774D79[BB_00774D79]
  bb_00774D7E[BB_00774D7E]
  bb_00774D83[BB_00774D83]
  bb_00774D8B[BB_00774D8B]
  bb_00774D90[BB_00774D90]
  bb_00774D98[BB_00774D98]
  bb_00774DA0[BB_00774DA0]
  bb_00774DA9[BB_00774DA9]
  bb_00774DAC[BB_00774DAC]
  bb_00774DC4[BB_00774DC4]
  bb_00774D00 -->|branch| bb_00774D79
  bb_00774D00 -->|fallthrough| bb_00774D29
  bb_00774D29 -->|branch| bb_00774D79
  bb_00774D29 -->|fallthrough| bb_00774D2E
  bb_00774D2E -->|branch| bb_00774D79
  bb_00774D2E -->|fallthrough| bb_00774D33
  bb_00774D33 -->|branch| bb_00774D79
  bb_00774D33 -->|fallthrough| bb_00774D38
  bb_00774D38 -->|branch| bb_00774D7E
  bb_00774D38 -->|fallthrough| bb_00774D58
  bb_00774D58 -->|branch| bb_00774D72
  bb_00774D58 -->|fallthrough| bb_00774D6B
  bb_00774D6B -->|branch| bb_00774DA9
  bb_00774D72 -->|branch| bb_00774D7E
  bb_00774D79 -->|flow| bb_00774D7E
  bb_00774D7E -->|branch| bb_00774D8B
  bb_00774D7E -->|fallthrough| bb_00774D83
  bb_00774D83 -->|flow| bb_00774D8B
  bb_00774D8B -->|branch| bb_00774D98
  bb_00774D8B -->|fallthrough| bb_00774D90
  bb_00774D90 -->|flow| bb_00774D98
  bb_00774D98 -->|branch| bb_00774DAC
  bb_00774D98 -->|fallthrough| bb_00774DA0
  bb_00774DA0 -->|flow| bb_00774DA9
  bb_00774DA9 -->|flow| bb_00774DAC
```
