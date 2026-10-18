# PopPdcDisengagePhases

- RVA: `0x00989D5C`–`0x00989D81` (길이 `37` bytes)
- VA: `0x0000000140989D5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F758`
- 디코드: `11`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00989D7A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PopPowerAggregatorModernStandbyExitStateHandler](PopPowerAggregatorModernStandbyExitStateHandler_function_00989D90.md) at `0x00989DBF`
- [PopPowerAggregatorEnterScreenOff](PopPowerAggregatorEnterScreenOff_function_00989F38.md) at `0x00989FDD`

### Static image references
- `0x00989D60` → RVA `0x00E677E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00989D7A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00989D5C  48 83 EC 28                     sub rsp, 0x28
00989D60  48 8B 0D 79 DA 4D 00            mov rcx, qword ptr [rip + 0x4dda79]
00989D67  B8 02 00 00 C0                  mov eax, 0xc0000002
00989D6C  48 85 C9                        test rcx, rcx
00989D6F  75 06                           jne 0x140989d77
00989D71  48 83 C4 28                     add rsp, 0x28
00989D75  C3                              ret
00989D76  CC                              int3
00989D77  48 8B C1                        mov rax, rcx
00989D7A  E8 51 0D D3 FF                  call 0x1406baad0
00989D7F  EB F0                           jmp 0x140989d71
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPdcDisengagePhases(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 5102201) != 0) goto loc_00989D77;
loc_00989D71:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC0000002ULL);
loc_00989D77:
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 5102201), a2, a3, a4);
    goto loc_00989D71;
}
```

## 5. (Beta) C Style

```c
void PopPdcDisengagePhases(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x4DDA79) != 0) goto loc_00989D77;
loc_00989D71:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC0000002ULL);
loc_00989D77:
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x4DDA79), a2, a3, a4);
    goto loc_00989D71;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00989D5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00989D5C[BB_00989D5C]
  bb_00989D71[BB_00989D71]
  bb_00989D76[BB_00989D76]
  bb_00989D77[BB_00989D77]
  bb_00989D5C -->|branch| bb_00989D77
  bb_00989D5C -->|fallthrough| bb_00989D71
  bb_00989D76 -->|flow| bb_00989D77
  bb_00989D77 -->|branch| bb_00989D71
```
