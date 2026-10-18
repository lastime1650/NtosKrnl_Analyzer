# CmFcpIncrementChangeStamp

- RVA: `0x00704338`–`0x00704347` (길이 `15` bytes)
- VA: `0x0000000140704338`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmFcManagerStartBootPhase](../../init/C5/CmFcManagerStartBootPhase_function_00C5DB98.md) at `0x00C5DBBF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00704338  48 83 C1 01                     add rcx, 1
0070433C  B8 01 00 00 00                  mov eax, 1
00704341  48 0F 45 C1                     cmovne rax, rcx
00704345  C3                              ret
00704346  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmFcpIncrementChangeStamp(__int64 a1)
{
    __int64 result;

    a1 = (a1) + (1);
    result = 1;
    if (condition_is_not_equal) { result = a1; }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmFcpIncrementChangeStamp(int64_t Arg1)
{
    int64_t result;

    Arg1 = (Arg1) + (1);
    result = 1;
    if (condition_is_not_equal) { result = Arg1; }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00704338&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00704338[BB_00704338]
  bb_00704346[BB_00704346]
```
