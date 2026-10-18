# ExpCapabilityCheck

- RVA: `0x00A20300`–`0x00A2032E` (길이 `46` bytes)
- VA: `0x0000000140A20300`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F758`
- 디코드: `15`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A20313` → [RtlCapabilityCheck](RtlCapabilityCheck_function_00A20340.md) (function, `0x00A20340`)

### Direct callers
- [ExpFirmwareAccessAppContainerCheck](../AB/ExpFirmwareAccessAppContainerCheck_function_00AB7AFC.md) at `0x00AB7C38`
- [ExpFirmwareAccessAppContainerCheck](../AB/ExpFirmwareAccessAppContainerCheck_function_00AB7AFC.md) at `0x00AB7C46`
- [ExpFirmwareAccessAppContainerCheck](../AB/ExpFirmwareAccessAppContainerCheck_function_00AB7AFC.md) at `0x00AB7D36`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A20300  48 83 EC 28                     sub rsp, 0x28
00A20304  48 8B D1                        mov rdx, rcx
00A20307  C6 44 24 38 00                  mov byte ptr [rsp + 0x38], 0
00A2030C  33 C9                           xor ecx, ecx
00A2030E  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00A20313  E8 28 00 00 00                  call 0x140a20340
00A20318  85 C0                           test eax, eax
00A2031A  79 08                           jns 0x140a20324
00A2031C  32 C0                           xor al, al
00A2031E  48 83 C4 28                     add rsp, 0x28
00A20322  C3                              ret
00A20323  CC                              int3
00A20324  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A20329  0F 95 C0                        setne al
00A2032C  EB F0                           jmp 0x140a2031e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpCapabilityCheck(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p38;

    v_rsp = (v_rsp) - (40);
    v_stack_p10 = 0;
    a1 = 0;
    result = RtlCapabilityCheck(a1, a1, v_stack_p10, a4);
    if (!sign_flag) goto loc_00A20324;
    result = 0;
loc_00A2031E:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A20324:
    result = (v_stack_p38 != 0) ? 1 : 0;
    goto loc_00A2031E;
}
```

## 5. (Beta) C Style

```c
int64_t ExpCapabilityCheck(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_p10;
    uint8_t v_stack_p38;

    local_rsp = (local_rsp) - (40);
    v_stack_p10 = 0;
    Arg1 = 0;
    result = RtlCapabilityCheck(Arg1, Arg1, v_stack_p10, a4);
    if (!sign_flag) goto loc_00A20324;
    result = 0;
loc_00A2031E:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A20324:
    result = (v_stack_p38 != 0) ? 1 : 0;
    goto loc_00A2031E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A20300&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A20300[BB_00A20300]
  bb_00A2031C[BB_00A2031C]
  bb_00A2031E[BB_00A2031E]
  bb_00A20323[BB_00A20323]
  bb_00A20324[BB_00A20324]
  bb_00A20300 -->|branch| bb_00A20324
  bb_00A20300 -->|fallthrough| bb_00A2031C
  bb_00A2031C -->|flow| bb_00A2031E
  bb_00A20323 -->|flow| bb_00A20324
  bb_00A20324 -->|branch| bb_00A2031E
```
