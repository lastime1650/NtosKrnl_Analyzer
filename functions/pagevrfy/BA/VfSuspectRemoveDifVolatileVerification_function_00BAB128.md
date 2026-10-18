# VfSuspectRemoveDifVolatileVerification

- RVA: `0x00BAB128`–`0x00BAB18B` (길이 `99` bytes)
- VA: `0x0000000140BAB128`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `28`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00BAB141` → [VfTargetRecoverIoCallbacks](../../text/61/VfTargetRecoverIoCallbacks_function_006131F0.md) (function, `0x006131F0`)
- `0x00BAB149` → [VfThunkApplyPristineToAllSession](VfThunkApplyPristineToAllSession_function_00BA7174.md) (function, `0x00BA7174`)
- `0x00BAB157` → [VfTargetDriversDisableVerifier](../B9/VfTargetDriversDisableVerifier_function_00B9B2CC.md) (function, `0x00B9B2CC`)
- `0x00BAB160` → [VfSuspectDifRemoveEntry](VfSuspectDifRemoveEntry_function_00BAA630.md) (function, `0x00BAA630`)

### Direct callers
- [VfDriverRemoveAllDifVerification](../../text/61/VfDriverRemoveAllDifVerification_function_006130E4.md) at `0x0061314A`
- [VfDriverRemoveDifVerification](../B9/VfDriverRemoveDifVerification_function_00B9A4E0.md) at `0x00B9A56F`

### Static image references
- `0x00BAB165` → RVA `0x00F04A58` (`.data`; read)
- `0x00BAB16D` → RVA `0x00F04A58` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BAB141` → [VfTargetRecoverIoCallbacks](../../text/61/VfTargetRecoverIoCallbacks_function_006131F0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAB128  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00BAB12D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00BAB132  57                              push rdi
00BAB133  48 83 EC 20                     sub rsp, 0x20
00BAB137  48 8B 71 30                     mov rsi, qword ptr [rcx + 0x30]
00BAB13B  48 8B D9                        mov rbx, rcx
00BAB13E  48 8B CE                        mov rcx, rsi
00BAB141  E8 AA 80 A6 FF                  call 0x1406131f0
00BAB146  48 8B CB                        mov rcx, rbx
00BAB149  E8 26 C0 FF FF                  call 0x140ba7174
00BAB14E  8B F8                           mov edi, eax
00BAB150  85 C0                           test eax, eax
00BAB152  78 24                           js 0x140bab178
00BAB154  48 8B CE                        mov rcx, rsi
00BAB157  E8 70 01 FF FF                  call 0x140b9b2cc
00BAB15C  48 8D 4B 58                     lea rcx, [rbx + 0x58]
00BAB160  E8 CB F4 FF FF                  call 0x140baa630
00BAB165  8B 0D ED 98 35 00               mov ecx, dword ptr [rip + 0x3598ed]
00BAB16B  FF C1                           inc ecx
00BAB16D  89 0D E5 98 35 00               mov dword ptr [rip + 0x3598e5], ecx
00BAB173  0F BA 73 68 19                  btr dword ptr [rbx + 0x68], 0x19
00BAB178  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BAB17D  8B C7                           mov eax, edi
00BAB17F  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00BAB184  48 83 C4 20                     add rsp, 0x20
00BAB188  5F                              pop rdi
00BAB189  C3                              ret
00BAB18A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfSuspectRemoveDifVolatileVerification(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = VfTargetRecoverIoCallbacks(*(unsigned __int64 *)(a1 + 48), a2, a3, a4);
    result = VfThunkApplyPristineToAllSession(a1, a2, a3, a4);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = VfTargetDriversDisableVerifier(a1, a2, a3, a4);
        a1 = a1 + 88;
        result = VfSuspectDifRemoveEntry(a1, a2, a3, a4);
        a1 = *(unsigned int *)(v_rip + 3512557);
        a1 = (unsigned int)((a1) + 1);
        *(unsigned int *)(v_rip + 3512549) = (unsigned int)(a1);
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t VfSuspectRemoveDifVolatileVerification(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = VfTargetRecoverIoCallbacks(*(uint64_t *)(arg1 + 0x30), a2, a3, a4);
    result = VfThunkApplyPristineToAllSession(Arg1, a2, a3, a4);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = VfTargetDriversDisableVerifier(Arg1, a2, a3, a4);
        Arg1 = Arg1 + 88;
        result = VfSuspectDifRemoveEntry(Arg1, a2, a3, a4);
        Arg1 = *(uint32_t *)(v_rip + 0x3598ED);
        Arg1 = (uint32_t)((Arg1) + 1);
        *(uint32_t *)(v_rip + 0x3598E5) = (uint32_t)(Arg1);
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAB128&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAB128[BB_00BAB128]
  bb_00BAB154[BB_00BAB154]
  bb_00BAB178[BB_00BAB178]
  bb_00BAB18A[BB_00BAB18A]
  bb_00BAB128 -->|branch| bb_00BAB178
  bb_00BAB128 -->|fallthrough| bb_00BAB154
  bb_00BAB154 -->|flow| bb_00BAB178
```
