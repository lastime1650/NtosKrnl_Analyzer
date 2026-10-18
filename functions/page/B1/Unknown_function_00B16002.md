# sub_00B16002

- RVA: `0x00B16002`–`0x00B1600F` (길이 `13` bytes)
- VA: `0x0000000140B16002`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069068`
- 디코드: `3`개 명령, `13/13` bytes 표시
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
  - `0x00B1600A` → [CmpLogCheckpoint + 0x71](../84/CmpLogCheckpoint_function_00842F04.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B16002  49 8B 06                        mov rax, qword ptr [r14]
00B16005  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00B1600A  E9 66 CF D2 FF                  jmp 0x140842f75
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B16002(void)
{
    unsigned __int64 v_stack_p40;

    v_stack_p40 = *(unsigned __int64 *)(v_r14);
}
```

## 5. (Beta) C Style

```c
void sub_00B16002(void)
{
    uint64_t v_stack_p40;

    v_stack_p40 = *(uint64_t *)(local_r14);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B16002&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B16002[BB_00B16002]
```
