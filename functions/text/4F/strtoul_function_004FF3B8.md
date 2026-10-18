# strtoul

- RVA: `0x004FF3B8`–`0x004FF3E4` (길이 `44` bytes)
- VA: `0x00000001404FF3B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `11`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004FF3D9` → [strtoxlX](strtoxlX_function_004FF130.md) (function, `0x004FF130`)

### Direct callers
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1C936`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1C95F`
- [EmpParseCallbacks](../../init/C2/EmpParseCallbacks_function_00C2657C.md) at `0x00C26689`
- [EmpParseCallbacks](../../init/C2/EmpParseCallbacks_function_00C2657C.md) at `0x00C266C7`
- [EmpParseRuleTermArgMapping](../../init/C2/EmpParseRuleTermArgMapping_function_00C27140.md) at `0x00C2721F`
- [EmpParseRuleTermArgMapping](../../init/C2/EmpParseRuleTermArgMapping_function_00C27140.md) at `0x00C272DF`
- [EmpParseRuleTermArgMapping](../../init/C2/EmpParseRuleTermArgMapping_function_00C27140.md) at `0x00C273CC`
- [EmpParseRules](../../init/C2/EmpParseRules_function_00C2745C.md) at `0x00C27588`
- [EmpParseRules](../../init/C2/EmpParseRules_function_00C2745C.md) at `0x00C275BA`
- [CmpGetBiosDate](../../init/C5/CmpGetBiosDate_function_00C59C80.md) at `0x00C59D5C`
- [CmpGetBiosDate](../../init/C5/CmpGetBiosDate_function_00C59C80.md) at `0x00C59D6E`
- [CmpGetBiosDate](../../init/C5/CmpGetBiosDate_function_00C59C80.md) at `0x00C59D7F`
- [EmpCacheBiosDate](../../init/C7/EmpCacheBiosDate_function_00C73258.md) at `0x00C732E3`
- [EmpCacheBiosDate](../../init/C7/EmpCacheBiosDate_function_00C73258.md) at `0x00C73318`
- [EmpCacheBiosDate](../../init/C7/EmpCacheBiosDate_function_00C73258.md) at `0x00C73339`

### Static image references
- `0x004FF3D2` → RVA `0x00006698` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FF3B8  48 83 EC 38                     sub rsp, 0x38
004FF3BC  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
004FF3C1  45 8B C8                        mov r9d, r8d
004FF3C4  4C 8B C2                        mov r8, rdx
004FF3C7  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
004FF3CF  48 8B D1                        mov rdx, rcx
004FF3D2  48 8D 0D BF 72 B0 FF            lea rcx, [rip - 0x4f8d41]
004FF3D9  E8 52 FD FF FF                  call 0x1404ff130
004FF3DE  48 83 C4 38                     add rsp, 0x38
004FF3E2  C3                              ret
004FF3E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall strtoul(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = 1;
    result = strtoxlX(v_rip - 5213505, a1, a2, (unsigned int)(a3));
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t strtoul(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = 1;
    result = strtoxlX(v_rip - 5213505, Arg1, Arg2, (uint32_t)(Arg3));
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FF3B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FF3B8[BB_004FF3B8]
  bb_004FF3E3[BB_004FF3E3]
```
