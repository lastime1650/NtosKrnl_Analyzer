# EmClientRuleRegisterNotification

- RVA: `0x00712DC0`–`0x00712DDB` (길이 `27` bytes)
- VA: `0x0000000140712DC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00712DD0` → [EmpClientRuleRegisterNotification](EmpClientRuleRegisterNotification_function_00712DE4.md) (function, `0x00712DE4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00712DC0  48 83 EC 28                     sub rsp, 0x28
00712DC4  48 85 C9                        test rcx, rcx
00712DC7  75 07                           jne 0x140712dd0
00712DC9  B8 0D 00 00 C0                  mov eax, 0xc000000d
00712DCE  EB 05                           jmp 0x140712dd5
00712DD0  E8 0F 00 00 00                  call 0x140712de4
00712DD5  48 83 C4 28                     add rsp, 0x28
00712DD9  C3                              ret
00712DDA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmClientRuleRegisterNotification(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_00712DD0;
    goto loc_00712DD5;
loc_00712DD0:
    result = EmpClientRuleRegisterNotification(a1, a2, a3, a4);
loc_00712DD5:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EmClientRuleRegisterNotification(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_00712DD0;
    goto loc_00712DD5;
loc_00712DD0:
    result = EmpClientRuleRegisterNotification(Arg1, a2, a3, a4);
loc_00712DD5:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00712DC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00712DC0[BB_00712DC0]
  bb_00712DC9[BB_00712DC9]
  bb_00712DD0[BB_00712DD0]
  bb_00712DD5[BB_00712DD5]
  bb_00712DDA[BB_00712DDA]
  bb_00712DC0 -->|branch| bb_00712DD0
  bb_00712DC0 -->|fallthrough| bb_00712DC9
  bb_00712DC9 -->|branch| bb_00712DD5
  bb_00712DD0 -->|flow| bb_00712DD5
```
