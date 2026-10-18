# sub_0023FFB5

- RVA: `0x0023FFB5`–`0x0023FFC8` (길이 `19` bytes)
- VA: `0x000000014023FFB5`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000616A8`
- 디코드: `8`개 명령, `19/19` bytes 표시
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
  - `0x0023FFC4` → [MiCheckReservePageFileSpace + 0x39](MiCheckReservePageFileSpace_function_0023FF50.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0023FFB5  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0023FFBA  48 83 C4 20                     add rsp, 0x20
0023FFBE  5E                              pop rsi
0023FFBF  C3                              ret
0023FFC0  CC                              int3
0023FFC1  49 85 C1                        test r9, rax
0023FFC4  75 C3                           jne 0x14023ff89
0023FFC6  EB ED                           jmp 0x14023ffb5
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0023FFB5(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (32);
    return;
}
```

## 5. (Beta) C Style

```c
void sub_0023FFB5(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, int64_t Arg7)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (32);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0023FFB5&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0023FFB5[BB_0023FFB5]
  bb_0023FFC0[BB_0023FFC0]
  bb_0023FFC6[BB_0023FFC6]
  bb_0023FFC0 -->|fallthrough| bb_0023FFC6
  bb_0023FFC6 -->|branch| bb_0023FFB5
```
