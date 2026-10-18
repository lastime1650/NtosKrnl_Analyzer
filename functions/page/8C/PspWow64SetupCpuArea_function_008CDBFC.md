# PspWow64SetupCpuArea

- RVA: `0x008CDBFC`–`0x008CDC92` (길이 `150` bytes)
- VA: `0x00000001408CDBFC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008474C`
- 디코드: `43`개 명령, `150/150` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008CDC12` → [PsWow64GetProcessMachine](../8D/PsWow64GetProcessMachine_function_008D2130.md) (function, `0x008D2130`)
- `0x008CDC1A` → [RtlpArchContextFlagFromMachine](RtlpArchContextFlagFromMachine_function_008CDF68.md) (function, `0x008CDF68`)
- `0x008CDC30` → [RtlpGetLegacyContextLength](../../text/4B/RtlpGetLegacyContextLength_function_004B6060.md) (function, `0x004B6060`)
- `0x008CDC3A` → [RtlWow64GetCpuAreaEnabledFeatures](RtlWow64GetCpuAreaEnabledFeatures_function_008CDFB4.md) (function, `0x008CDFB4`)
- `0x008CDC4B` → [RtlGetExtendedContextLength2](../../text/49/RtlGetExtendedContextLength2_function_00493FE0.md) (function, `0x00493FE0`)

### Direct callers
- [PspSetupUserStack](PspSetupUserStack_function_008CD794.md) at `0x008CD8E7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008CDC30` → [RtlpGetLegacyContextLength](../../text/4B/RtlpGetLegacyContextLength_function_004B6060.md) (`PAGE` → `.text`)
  - `0x008CDC4B` → [RtlGetExtendedContextLength2](../../text/49/RtlGetExtendedContextLength2_function_00493FE0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008CDBFC  40 53                           push rbx
008CDBFE  48 83 EC 30                     sub rsp, 0x30
008CDC02  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
008CDC07  48 8B D9                        mov rbx, rcx
008CDC0A  83 64 24 58 00                  and dword ptr [rsp + 0x58], 0
008CDC0F  48 8B CA                        mov rcx, rdx
008CDC12  E8 19 45 00 00                  call 0x1408d2130
008CDC17  0F B7 C8                        movzx ecx, ax
008CDC1A  E8 49 03 00 00                  call 0x1408cdf68
008CDC1F  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CDC23  85 C0                           test eax, eax
008CDC25  74 64                           je 0x1408cdc8b
008CDC27  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
008CDC2C  33 D2                           xor edx, edx
008CDC2E  8B C8                           mov ecx, eax
008CDC30  E8 2B 84 BE FF                  call 0x1404b6060
008CDC35  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
008CDC3A  E8 75 03 00 00                  call 0x1408cdfb4
008CDC3F  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
008CDC43  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
008CDC48  4C 8B C0                        mov r8, rax
008CDC4B  E8 90 63 BC FF                  call 0x140493fe0
008CDC50  48 8B 0B                        mov rcx, qword ptr [rbx]
008CDC53  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
008CDC57  48 83 E9 04                     sub rcx, 4
008CDC5B  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
008CDC5F  48 83 E9 05                     sub rcx, 5
008CDC63  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
008CDC67  48 2B C8                        sub rcx, rax
008CDC6A  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
008CDC6E  48 FF C8                        dec rax
008CDC71  48 F7 D0                        not rax
008CDC74  48 23 C8                        and rcx, rax
008CDC77  48 83 E9 04                     sub rcx, 4
008CDC7B  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
008CDC7F  48 89 0B                        mov qword ptr [rbx], rcx
008CDC82  33 C0                           xor eax, eax
008CDC84  48 83 C4 30                     add rsp, 0x30
008CDC88  5B                              pop rbx
008CDC89  C3                              ret
008CDC8A  CC                              int3
008CDC8B  B8 0D 00 00 C0                  mov eax, 0xc000000d
008CDC90  EB F2                           jmp 0x1408cdc84
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspWow64SetupCpuArea(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;

    v_rsp = (v_rsp) - (48);
    result = PsWow64GetProcessMachine(a2, a2, a3, a4);
    result = RtlpArchContextFlagFromMachine((unsigned __int16)(result), a2, a3, a4);
    v_stack_p18 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_008CDC8B;
    a2 = 0;
    result = RtlpGetLegacyContextLength((unsigned int)((unsigned int)(result)), a2, v_stack_m18, a4);
    result = RtlWow64GetCpuAreaEnabledFeatures(v_stack_p18, a2, v_stack_m18, a4);
    result = RtlGetExtendedContextLength2((unsigned int)(v_stack_p18), v_stack_p20, result, a4);
    a1 = (*(unsigned __int64 *)(a1)) - (4);
    a1 = (a1) & (-4);
    a1 = (a1) - (5);
    a1 = (a1) & (-8);
    a1 = (a1) - ((unsigned int)(v_stack_p20));
    result = ((unsigned int)(v_stack_m18)) - 1;
    result = ~(result);
    a1 = (a1) & (result);
    a1 = (a1) - (4);
    a1 = (a1) & (-16);
    *(unsigned __int64 *)(a1) = a1;
    result = 0;
loc_008CDC84:
    v_rsp = (v_rsp) + (48);
    return result;
loc_008CDC8B:
    goto loc_008CDC84;
}
```

## 5. (Beta) C Style

```c
int64_t PspWow64SetupCpuArea(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;

    local_rsp = (local_rsp) - (48);
    result = PsWow64GetProcessMachine(Arg2, Arg2, a3, a4);
    result = RtlpArchContextFlagFromMachine((uint16_t)(result), Arg2, a3, a4);
    v_stack_p18 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_008CDC8B;
    Arg2 = 0;
    result = RtlpGetLegacyContextLength((uint32_t)((uint32_t)(result)), Arg2, v_stack_m18, a4);
    result = RtlWow64GetCpuAreaEnabledFeatures(v_stack_p18, Arg2, v_stack_m18, a4);
    result = RtlGetExtendedContextLength2((uint32_t)(v_stack_p18), v_stack_p20, result, a4);
    Arg1 = (*(uint64_t *)(arg1)) - (4);
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) - (5);
    Arg1 = (Arg1) & (-8);
    Arg1 = (Arg1) - ((uint32_t)(v_stack_p20));
    result = ((uint32_t)(v_stack_m18)) - 1;
    result = ~(result);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) - (4);
    Arg1 = (Arg1) & (-16);
    *(void **)(arg1) = Arg1;
    result = 0;
loc_008CDC84:
    local_rsp = (local_rsp) + (48);
    return result;
loc_008CDC8B:
    goto loc_008CDC84;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008CDBFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008CDBFC[BB_008CDBFC]
  bb_008CDC27[BB_008CDC27]
  bb_008CDC84[BB_008CDC84]
  bb_008CDC8A[BB_008CDC8A]
  bb_008CDC8B[BB_008CDC8B]
  bb_008CDBFC -->|branch| bb_008CDC8B
  bb_008CDBFC -->|fallthrough| bb_008CDC27
  bb_008CDC27 -->|flow| bb_008CDC84
  bb_008CDC8A -->|flow| bb_008CDC8B
  bb_008CDC8B -->|branch| bb_008CDC84
```
