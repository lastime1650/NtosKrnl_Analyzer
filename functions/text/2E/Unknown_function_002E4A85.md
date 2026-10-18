# sub_002E4A85

- RVA: `0x002E4A85`–`0x002E4A94` (길이 `15` bytes)
- VA: `0x00000001402E4A85`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071058`
- 디코드: `4`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002E4A8F` → [sub_002E46D4 + 0x11](Unknown_function_002E46D4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E4A85  4D 85 C9                        test r9, r9
002E4A88  49 8B C7                        mov rax, r15
002E4A8B  48 0F 45 C1                     cmovne rax, rcx
002E4A8F  E9 51 FC FF FF                  jmp 0x1402e46e5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E4A85(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;

    result = v_r15;
    if (a4 != 0) { result = a1; }
}
```

## 5. (Beta) C Style

```c
int64_t sub_002E4A85(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;

    result = local_r15;
    if (Arg4 != 0) { result = Arg1; }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E4A85&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E4A85[BB_002E4A85]
```
