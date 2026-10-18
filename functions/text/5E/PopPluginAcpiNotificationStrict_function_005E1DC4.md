# PopPluginAcpiNotificationStrict

- RVA: `0x005E1DC4`–`0x005E1E08` (길이 `68` bytes)
- VA: `0x00000001405E1DC4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `22`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005E1DDB` → [PopPluginAcpiNotification](../4D/PopPluginAcpiNotification_function_004D9820.md) (function, `0x004D9820`)
- `0x005E1DF1` → [PopFxBugCheck](../2B/PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)

### Direct callers
- [PopFxAcpiDispatchNotification](../5D/PopFxAcpiDispatchNotification_function_005DD450.md) at `0x005DD50D`
- [PopFxAcpiPrepareDevice](../5D/PopFxAcpiPrepareDevice_function_005DD5F4.md) at `0x005DD6B3`
- [PopFxAcpiRegisterDevice](../5D/PopFxAcpiRegisterDevice_function_005DD724.md) at `0x005DD7A6`
- [PopFxAcpiUnregisterDevice](../5D/PopFxAcpiUnregisterDevice_function_005DD830.md) at `0x005DD8A7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E1DC4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005E1DC9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
005E1DCE  57                              push rdi
005E1DCF  48 83 EC 20                     sub rsp, 0x20
005E1DD3  49 8B D8                        mov rbx, r8
005E1DD6  8B FA                           mov edi, edx
005E1DD8  48 8B F1                        mov rsi, rcx
005E1DDB  E8 40 7A EF FF                  call 0x1404d9820
005E1DE0  84 C0                           test al, al
005E1DE2  75 13                           jne 0x1405e1df7
005E1DE4  8B D7                           mov edx, edi
005E1DE6  4C 8B CB                        mov r9, rbx
005E1DE9  4C 8B C6                        mov r8, rsi
005E1DEC  B9 68 06 00 00                  mov ecx, 0x668
005E1DF1  E8 76 DE CD FF                  call 0x1402bfc6c
005E1DF6  CC                              int3
005E1DF7  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005E1DFC  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
005E1E01  48 83 C4 20                     add rsp, 0x20
005E1E05  5F                              pop rdi
005E1E06  C3                              ret
005E1E07  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPluginAcpiNotificationStrict(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = PopPluginAcpiNotification(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a2 = (unsigned int)((unsigned int)(a2));
        a4 = a3;
        a3 = a1;
        a1 = 0x668ULL;
        result = PopFxBugCheck(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPluginAcpiNotificationStrict(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = PopPluginAcpiNotification(Arg1, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) {
        Arg2 = (uint32_t)((uint32_t)(Arg2));
        a4 = Arg3;
        Arg3 = Arg1;
        Arg1 = 0x668ULL;
        result = PopFxBugCheck(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E1DC4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E1DC4[BB_005E1DC4]
  bb_005E1DE4[BB_005E1DE4]
  bb_005E1DF7[BB_005E1DF7]
  bb_005E1E07[BB_005E1E07]
  bb_005E1DC4 -->|branch| bb_005E1DF7
  bb_005E1DC4 -->|fallthrough| bb_005E1DE4
  bb_005E1DE4 -->|flow| bb_005E1DF7
```
