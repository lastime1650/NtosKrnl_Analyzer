# PfIoPowerEventNotify

- RVA: `0x00750784`–`0x007507A4` (길이 `32` bytes)
- VA: `0x0000000140750784`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00750799` → [PfPowerActionNotify](../../pagelk/B7/PfPowerActionNotify_function_00B7AC98.md) (function, `0x00B7AC98`)

### Direct callers
- [PopUmpoProcessPowerMessage](../A2/PopUmpoProcessPowerMessage_function_00A2E9B4.md) at `0x00A2EA62`
- [PopUmpoSendLegacyEvent](../AA/PopUmpoSendLegacyEvent_function_00AA48E8.md) at `0x00AA4940`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00750799` → [PfPowerActionNotify](../../pagelk/B7/PfPowerActionNotify_function_00B7AC98.md) (`PAGE` → `PAGELK`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00750784  48 83 EC 28                     sub rsp, 0x28
00750788  41 8B C0                        mov eax, r8d
0075078B  83 F9 12                        cmp ecx, 0x12
0075078E  75 0E                           jne 0x14075079e
00750790  45 33 C0                        xor r8d, r8d
00750793  8B D0                           mov edx, eax
00750795  41 8D 48 05                     lea ecx, [r8 + 5]
00750799  E8 FA A4 42 00                  call 0x140b7ac98
0075079E  48 83 C4 28                     add rsp, 0x28
007507A2  C3                              ret
007507A3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfIoPowerEventNotify(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(a3);
    if (a1 == 18) {
        a3 = 0;
        a2 = (unsigned int)((unsigned int)(a3));
        a1 = a3 + 5;
        result = PfPowerActionNotify(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfIoPowerEventNotify(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(Arg3);
    if (Arg1 == 18) {
        Arg3 = 0;
        Arg2 = (uint32_t)((uint32_t)(Arg3));
        Arg1 = Arg3 + 5;
        result = PfPowerActionNotify(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00750784&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00750784[BB_00750784]
  bb_00750790[BB_00750790]
  bb_0075079E[BB_0075079E]
  bb_007507A3[BB_007507A3]
  bb_00750784 -->|branch| bb_0075079E
  bb_00750784 -->|fallthrough| bb_00750790
  bb_00750790 -->|flow| bb_0075079E
```
