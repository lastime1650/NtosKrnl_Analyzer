# HvlpStartPageListIteration

- RVA: `0x0058D8E4`–`0x0058D902` (길이 `30` bytes)
- VA: `0x000000014058D8E4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0058D8E8` → [HvlpSetupPageListIteration](HvlpSetupPageListIteration_function_0058D85C.md) (function, `0x0058D85C`)
- `0x0058D8F7` → [HvlpInvokeGetPageListHypercall](HvlpInvokeGetPageListHypercall_function_0058D7AC.md) (function, `0x0058D7AC`)

### Direct callers
- [HvlpMarkHypervisorPagesForHibernation](HvlpMarkHypervisorPagesForHibernation_function_0058AE08.md) at `0x0058AE21`
- [HvlAddPagesCallbackRoutine](HvlAddPagesCallbackRoutine_function_0058AF50.md) at `0x0058AFEF`
- [HvlpGetEncryptedDataFromHypervisor](HvlpGetEncryptedDataFromHypervisor_function_0058B984.md) at `0x0058B9FF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058D8E4  48 83 EC 28                     sub rsp, 0x28
0058D8E8  E8 6F FF FF FF                  call 0x14058d85c
0058D8ED  48 85 C0                        test rax, rax
0058D8F0  74 0A                           je 0x14058d8fc
0058D8F2  33 D2                           xor edx, edx
0058D8F4  48 8B C8                        mov rcx, rax
0058D8F7  E8 B0 FE FF FF                  call 0x14058d7ac
0058D8FC  48 83 C4 28                     add rsp, 0x28
0058D900  C3                              ret
0058D901  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpStartPageListIteration(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HvlpSetupPageListIteration(a1, a2, a3, a4);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = HvlpInvokeGetPageListHypercall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlpStartPageListIteration(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HvlpSetupPageListIteration(Arg1, Arg2, a3, a4);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = HvlpInvokeGetPageListHypercall(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058D8E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058D8E4[BB_0058D8E4]
  bb_0058D8F2[BB_0058D8F2]
  bb_0058D8FC[BB_0058D8FC]
  bb_0058D901[BB_0058D901]
  bb_0058D8E4 -->|branch| bb_0058D8FC
  bb_0058D8E4 -->|fallthrough| bb_0058D8F2
  bb_0058D8F2 -->|flow| bb_0058D8FC
```
