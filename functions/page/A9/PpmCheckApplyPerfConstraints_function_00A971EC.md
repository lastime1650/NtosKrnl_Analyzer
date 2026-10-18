# PpmCheckApplyPerfConstraints

- RVA: `0x00A971EC`–`0x00A97203` (길이 `23` bytes)
- VA: `0x0000000140A971EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A971F8` → [PpmCheckCustomRun](../../text/3B/PpmCheckCustomRun_function_003BEC2C.md) (function, `0x003BEC2C`)

### Direct callers
- [PpmRegisterPerfCap](../../text/42/PpmRegisterPerfCap_function_0042B0D0.md) at `0x0042B19F`
- [PpmPerfUpdateDomainPolicy](PpmPerfUpdateDomainPolicy_function_00A97030.md) at `0x00A971C9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A971F8` → [PpmCheckCustomRun](../../text/3B/PpmCheckCustomRun_function_003BEC2C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A971EC  48 83 EC 28                     sub rsp, 0x28
00A971F0  F6 D9                           neg cl
00A971F2  1B C9                           sbb ecx, ecx
00A971F4  F7 D9                           neg ecx
00A971F6  FF C1                           inc ecx
00A971F8  E8 2F 7A 92 FF                  call 0x1403bec2c
00A971FD  48 83 C4 28                     add rsp, 0x28
00A97201  C3                              ret
00A97202  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmCheckApplyPerfConstraints(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (unsigned __int8)(-(a1));
    a1 = (unsigned int)(-(a1));
    a1 = (unsigned int)((a1) + 1);
    result = PpmCheckCustomRun(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmCheckApplyPerfConstraints(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (uint8_t)(-(Arg1));
    Arg1 = (uint32_t)(-(Arg1));
    Arg1 = (uint32_t)((Arg1) + 1);
    result = PpmCheckCustomRun(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A971EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A971EC[BB_00A971EC]
  bb_00A97202[BB_00A97202]
```
