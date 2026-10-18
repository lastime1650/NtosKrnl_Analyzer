# HvlpGetPageListIterator

- RVA: `0x0058D790`–`0x0058D7A4` (길이 `20` bytes)
- VA: `0x000000014058D790`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HvlpMarkHypervisorPagesForHibernation](HvlpMarkHypervisorPagesForHibernation_function_0058AE08.md) at `0x0058AE67`
- [HvlAddPagesCallbackRoutine](HvlAddPagesCallbackRoutine_function_0058AF50.md) at `0x0058B037`
- [HvlpGetEncryptedDataFromHypervisor](HvlpGetEncryptedDataFromHypervisor_function_0058B984.md) at `0x0058BA3C`
- [HvlpEndSecurePageListIteration](HvlpEndSecurePageListIteration_function_0058D610.md) at `0x0058D63B`
- [HvlpGetPageList](HvlpGetPageList_function_0058D6D8.md) at `0x0058D6FE`
- [HvlpSetupPageListIteration](HvlpSetupPageListIteration_function_0058D85C.md) at `0x0058D868`
- [HvlpStartSecurePageListIteration](HvlpStartSecurePageListIteration_function_0058D908.md) at `0x0058DA0C`

### Static image references
- `0x0058D790` → RVA `0x00F8EC80` (`.data`; read)
- `0x0058D79B` → RVA `0x00F8EC60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058D790  48 8D 05 E9 14 A0 00            lea rax, [rip + 0xa014e9]
0058D797  85 C9                           test ecx, ecx
0058D799  75 07                           jne 0x14058d7a2
0058D79B  48 8D 05 BE 14 A0 00            lea rax, [rip + 0xa014be]
0058D7A2  C3                              ret
0058D7A3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpGetPageListIterator(int a1)
{
    __int64 result;

    result = v_rip + 10491113;
    if (a1 == 0) {
        result = v_rip + 10491070;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlpGetPageListIterator(int32_t Arg1)
{
    int64_t result;

    result = v_rip + 10491113;
    if (Arg1 == 0) {
        result = v_rip + 10491070;
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058D790&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058D790[BB_0058D790]
  bb_0058D79B[BB_0058D79B]
  bb_0058D7A2[BB_0058D7A2]
  bb_0058D7A3[BB_0058D7A3]
  bb_0058D790 -->|branch| bb_0058D7A2
  bb_0058D790 -->|fallthrough| bb_0058D79B
  bb_0058D79B -->|flow| bb_0058D7A2
```
