# sub_00B2795A

- RVA: `0x00B2795A`–`0x00B27968` (길이 `14` bytes)
- VA: `0x0000000140B2795A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00092C0C`
- 디코드: `4`개 명령, `14/14` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B2795D` → [AslFree](../95/AslFree_function_0095B674.md) (function, `0x0095B674`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B27963` → [SdbInitDatabaseInMemory + 0x42](../95/SdbInitDatabaseInMemory_function_0095BC5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B2795A  48 8B D3                        mov rdx, rbx
00B2795D  E8 12 3D E3 FF                  call 0x14095b674
00B27962  90                              nop
00B27963  E9 36 43 E3 FF                  jmp 0x14095bc9e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B2795A(void)
{
    __int64 result;

    result = AslFree(a1, v_rbx, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B2795A(void)
{
    int64_t result;

    result = AslFree(a1, local_rbx, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B2795A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B2795A[BB_00B2795A]
```
