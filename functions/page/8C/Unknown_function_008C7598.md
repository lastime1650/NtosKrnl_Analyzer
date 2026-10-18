# sub_008C7598

- RVA: `0x008C7598`–`0x008C75AB` (길이 `19` bytes)
- VA: `0x00000001408C7598`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00083E64`
- 디코드: `6`개 명령, `19/19` bytes 표시
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
  - `0x008C75A9` → [sub_008C7605](Unknown_function_008C7605.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008C7598  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
008C759D  4D 8B F0                        mov r14, r8
008C75A0  4C 8B FA                        mov r15, rdx
008C75A3  48 8B E9                        mov rbp, rcx
008C75A6  66 85 C0                        test ax, ax
008C75A9  78 5A                           js 0x1408c7605
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_008C7598(__int64 a1, __int64 a2, __int64 a3)
{
    unsigned __int64 v_stack_p48;

    v_stack_p48 = v_r14;
}
```

## 5. (Beta) C Style

```c
void sub_008C7598(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    uint64_t v_stack_p48;

    v_stack_p48 = local_r14;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C7598&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C7598[BB_008C7598]
```
