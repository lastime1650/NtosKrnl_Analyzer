# sub_002C5596

- RVA: `0x002C5596`–`0x002C55A2` (길이 `12` bytes)
- VA: `0x00000001402C5596`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EAB8`
- 디코드: `2`개 명령, `12/12` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002C559B` → RVA `0x00010990` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C5596  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
002C559B  48 8D 05 EE B3 D4 FF            lea rax, [rip - 0x2b4c12]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002C5596(void)
{
    unsigned __int64 v_stack_p30;

    v_stack_p30 = v_rbx;
    return v_rip - 2837522;
}
```

## 5. (Beta) C Style

```c
void sub_002C5596(void)
{
    uint64_t v_stack_p30;

    v_stack_p30 = local_rbx;
    return v_rip - 2837522;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C5596&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C5596[BB_002C5596]
```
