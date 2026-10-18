# RtlGetSuiteMask

- RVA: `0x00A191E0`–`0x00A1920D` (길이 `45` bytes)
- VA: `0x0000000140A191E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `12`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A191E4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00A191FC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- [RtlGetVersion](RtlGetVersion_function_00A19110.md) at `0x00A1919C`
- [RtlGetVersion](RtlGetVersion_function_00A19110.md) at `0x00A191C5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A191E4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00A191FC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A191E0  48 83 EC 28                     sub rsp, 0x28
00A191E4  E8 F7 D0 A1 FF                  call 0x1404362e0
00A191E9  84 C0                           test al, al
00A191EB  75 0F                           jne 0x140a191fc
00A191ED  A1 D0 02 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000002d0]
00A191F6  48 83 C4 28                     add rsp, 0x28
00A191FA  C3                              ret
00A191FB  CC                              int3
00A191FC  E8 EF 4F 8E FF                  call 0x1402fe1f0
00A19201  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
00A19208  8B 40 14                        mov eax, dword ptr [rax + 0x14]
00A1920B  EB E9                           jmp 0x140a191f6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGetSuiteMask(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A191FC;
loc_00A191F6:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A191FC:
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    goto loc_00A191F6;
}
```

## 5. (Beta) C Style

```c
void RtlGetSuiteMask(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00A191FC;
loc_00A191F6:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A191FC:
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    goto loc_00A191F6;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A191E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A191E0[BB_00A191E0]
  bb_00A191ED[BB_00A191ED]
  bb_00A191F6[BB_00A191F6]
  bb_00A191FB[BB_00A191FB]
  bb_00A191FC[BB_00A191FC]
  bb_00A191E0 -->|branch| bb_00A191FC
  bb_00A191E0 -->|fallthrough| bb_00A191ED
  bb_00A191ED -->|flow| bb_00A191F6
  bb_00A191FB -->|flow| bb_00A191FC
  bb_00A191FC -->|branch| bb_00A191F6
```
