# sub_002B7C26

- RVA: `0x002B7C26`–`0x002B7C3E` (길이 `24` bytes)
- VA: `0x00000001402B7C26`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006DB28`
- 디코드: `4`개 명령, `24/24` bytes 표시
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
  - `0x002B7C39` → [sub_006DBB22](../6D/Unknown_function_006DBB22.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002B7C26  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
002B7C2B  48 8D 34 08                     lea rsi, [rax + rcx]
002B7C2F  48 BD FE FF FF FF FE FF FF FF   movabs rbp, 0xfffffffefffffffe
002B7C39  E9 E4 3E 42 00                  jmp 0x1406dbb22
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002B7C26(__int64 a1)
{
    unsigned __int64 v_stack_p30;

    v_stack_p30 = v_rbp;
}
```

## 5. (Beta) C Style

```c
void sub_002B7C26(int64_t Arg1)
{
    uint64_t v_stack_p30;

    v_stack_p30 = local_rbp;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B7C26&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002B7C26[BB_002B7C26]
```
