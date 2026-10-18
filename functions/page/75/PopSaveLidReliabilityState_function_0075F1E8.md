# PopSaveLidReliabilityState

- RVA: `0x0075F1E8`–`0x0075F25A` (길이 `114` bytes)
- VA: `0x000000014075F1E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `26`개 명령, `114/114` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0075F1FF` → [PopOpenPersistedRegistryKey](PopOpenPersistedRegistryKey_function_00754260.md) (function, `0x00754260`)
- `0x0075F214` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0075F23D` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x0075F24F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7ED7A`

### Static image references
- `0x0075F208` → RVA `0x00029360` (`.rdata`; read)
- `0x0075F21E` → RVA `0x00E0B570` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0075F214` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0075F23D` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x0075F24F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0075F1E8  48 83 EC 48                     sub rsp, 0x48
0075F1EC  48 83 64 24 50 00               and qword ptr [rsp + 0x50], 0
0075F1F2  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
0075F1F7  0F 57 C0                        xorps xmm0, xmm0
0075F1FA  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0075F1FF  E8 5C 50 FF FF                  call 0x140754260
0075F204  85 C0                           test eax, eax
0075F206  78 4C                           js 0x14075f254
0075F208  48 8D 15 51 A1 8C FF            lea rdx, [rip - 0x735eaf]
0075F20F  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0075F214  E8 67 B5 CC FF                  call 0x14042a780
0075F219  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0075F21E  48 8D 05 4B C3 6A 00            lea rax, [rip + 0x6ac34b]
0075F225  41 B9 04 00 00 00               mov r9d, 4
0075F22B  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0075F230  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
0075F235  45 33 C0                        xor r8d, r8d
0075F238  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0075F23D  E8 8E EA F4 FF                  call 0x1406adcd0
0075F242  48 83 7C 24 50 00               cmp qword ptr [rsp + 0x50], 0
0075F248  74 0A                           je 0x14075f254
0075F24A  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0075F24F  E8 5C E0 F4 FF                  call 0x1406ad2b0
0075F254  48 83 C4 48                     add rsp, 0x48
0075F258  C3                              ret
0075F259  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSaveLidReliabilityState(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = v_xmm0;
    result = PopOpenPersistedRegistryKey(a1, v_stack_p8, a3, a4);
    if (sign_flag) goto loc_0075F254;
    result = RtlInitUnicodeString(v_stack_m18, v_rip - 7560879, a3, a4);
    v_stack_m20 = 4;
    a3 = 0;
    v_stack_m28 = v_rip + 6996811;
    result = ZwSetValueKey(v_stack_p8, v_stack_m18, a3, 4);
    if (v_stack_p8 != 0) {
        a1 = v_stack_p8;
        result = ZwClose(a1, v_stack_m18, a3, 4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopSaveLidReliabilityState(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = v_xmm0;
    result = PopOpenPersistedRegistryKey(Arg1, v_stack_p8, Arg3, a4);
    if (sign_flag) goto loc_0075F254;
    result = RtlInitUnicodeString(v_stack_m18, v_rip - 7560879, Arg3, a4);
    v_stack_m20 = 4;
    Arg3 = 0;
    v_stack_m28 = v_rip + 6996811;
    result = ZwSetValueKey(v_stack_p8, v_stack_m18, Arg3, 4);
    if (v_stack_p8 != 0) {
        Arg1 = v_stack_p8;
        result = ZwClose(Arg1, v_stack_m18, Arg3, 4);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0075F1E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0075F1E8[BB_0075F1E8]
  bb_0075F208[BB_0075F208]
  bb_0075F24A[BB_0075F24A]
  bb_0075F254[BB_0075F254]
  bb_0075F259[BB_0075F259]
  bb_0075F1E8 -->|branch| bb_0075F254
  bb_0075F1E8 -->|fallthrough| bb_0075F208
  bb_0075F208 -->|branch| bb_0075F254
  bb_0075F208 -->|fallthrough| bb_0075F24A
  bb_0075F24A -->|flow| bb_0075F254
```
