# AslFileMappingGetViewBase

- RVA: `0x0081AB84`–`0x0081AB93` (길이 `15` bytes)
- VA: `0x000000014081AB84`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SdbOpenDatabaseEx](SdbOpenDatabaseEx_function_00812284.md) at `0x00812468`
- [SdbpCheckMatchingTextEntry](SdbpCheckMatchingTextEntry_function_00814A70.md) at `0x00814C17`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0081AB84  48 85 C9                        test rcx, rcx
0081AB87  75 04                           jne 0x14081ab8d
0081AB89  33 C0                           xor eax, eax
0081AB8B  C3                              ret
0081AB8C  CC                              int3
0081AB8D  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
0081AB91  C3                              ret
0081AB92  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AslFileMappingGetViewBase(__int64 a1)
{
    __int64 result;

    if (a1 != 0) goto loc_0081AB8D;
    result = 0;
    return result;
loc_0081AB8D:
    return *(unsigned __int64 *)(a1 + 32);
}
```

## 5. (Beta) C Style

```c
int64_t AslFileMappingGetViewBase(int64_t Arg1)
{
    int64_t result;

    if (Arg1 != 0) goto loc_0081AB8D;
    result = 0;
    return result;
loc_0081AB8D:
    return *(uint64_t *)(Arg1 + 0x20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0081AB84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0081AB84[BB_0081AB84]
  bb_0081AB89[BB_0081AB89]
  bb_0081AB8C[BB_0081AB8C]
  bb_0081AB8D[BB_0081AB8D]
  bb_0081AB92[BB_0081AB92]
  bb_0081AB84 -->|branch| bb_0081AB8D
  bb_0081AB84 -->|fallthrough| bb_0081AB89
  bb_0081AB8C -->|flow| bb_0081AB8D
```
