# sub_00215D69

- RVA: `0x00215D69`–`0x00215D82` (길이 `25` bytes)
- VA: `0x0000000140215D69`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E22C`
- 디코드: `6`개 명령, `25/25` bytes 표시
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
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00215D69  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00215D6E  48 8D 5D 60                     lea rbx, [rbp + 0x60]
00215D72  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00215D77  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00215D7C  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00215D81  90                              nop
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00215D69(void)
{
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p78;

    v_stack_p78 = v_rbx;
    v_stack_p28 = v_rbp + 96;
    v_stack_p48 = v_r13;
    v_stack_p20 = v_r12;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_00215D69(void)
{
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p48;
    uint64_t v_stack_p78;

    v_stack_p78 = local_rbx;
    v_stack_p28 = local_rbp + 96;
    v_stack_p48 = local_r13;
    v_stack_p20 = local_r12;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00215D69&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00215D69[BB_00215D69]
```
