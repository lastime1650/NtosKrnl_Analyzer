# IopResourceRequirementsChanged

- RVA: `0x00ADB7D0`–`0x00ADB806` (길이 `54` bytes)
- VA: `0x0000000140ADB7D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `16`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00ADB7FB` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (function, `0x00477FF8`)

### Direct callers
- [PiProcessQueryDeviceState](../8F/PiProcessQueryDeviceState_function_008FA0F8.md) at `0x008FA2CA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00ADB7FB` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ADB7D0  4C 8B DC                        mov r11, rsp
00ADB7D3  48 83 EC 58                     sub rsp, 0x58
00ADB7D7  33 C0                           xor eax, eax
00ADB7D9  4D 8D 4B E8                     lea r9, [r11 - 0x18]
00ADB7DD  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00ADB7E1  0F 57 C0                        xorps xmm0, xmm0
00ADB7E4  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00ADB7E9  88 54 24 48                     mov byte ptr [rsp + 0x48], dl
00ADB7ED  45 33 C0                        xor r8d, r8d
00ADB7F0  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
00ADB7F4  8D 50 0D                        lea edx, [rax + 0xd]
00ADB7F7  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
00ADB7FB  E8 F8 C7 99 FF                  call 0x140477ff8
00ADB800  48 83 C4 58                     add rsp, 0x58
00ADB804  C3                              ret
00ADB805  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopResourceRequirementsChanged(__int64 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (88);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    v_stack_m18 = v_xmm0;
    v_stack_m10 = a2;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    *(unsigned __int64 *)(v_rsp - 56) = 0;
    result = PnpRequestDeviceAction(a1, result + 13, a3, v_rsp - 24);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopResourceRequirementsChanged(int64_t Arg1, uint8_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (88);
    result = 0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    v_stack_m18 = v_xmm0;
    v_stack_m10 = Arg2;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x38) = 0;
    result = PnpRequestDeviceAction(Arg1, result + 13, Arg3, local_rsp - 24);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ADB7D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ADB7D0[BB_00ADB7D0]
  bb_00ADB805[BB_00ADB805]
```
