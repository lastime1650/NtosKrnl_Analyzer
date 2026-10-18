# NLG_Notify

- RVA: `0x004FF910`–`0x004FF928` (길이 `24` bytes)
- VA: `0x00000001404FF910`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2628`
- 디코드: `5`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [_C_specific_handler](_C_specific_handler_function_004FD410.md) at `0x004FD4C5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x004FF926` → [_NLG_Dispatch2](_NLG_Dispatch2_function_004FF930.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
004FF910  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
004FF915  48 89 54 24 18                  mov qword ptr [rsp + 0x18], rdx
004FF91A  44 89 44 24 10                  mov dword ptr [rsp + 0x10], r8d
004FF91F  49 C7 C1 20 05 93 19            mov r9, 0x19930520
004FF926  EB 08                           jmp 0x1404ff930
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall NLG_Notify(__int64 a1, __int64 a2, int a3)
{
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_stack_p18 = a2;
    v_stack_p10 = a3;
}
```

## 5. (Beta) C Style

```c
void NLG_Notify(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    v_stack_p18 = Arg2;
    v_stack_p10 = Arg3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FF910&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FF910[BB_004FF910]
```
