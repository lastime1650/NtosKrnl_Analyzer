# sub_0024AF7F

- RVA: `0x0024AF7F`–`0x0024AF91` (길이 `18` bytes)
- VA: `0x000000014024AF7F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062BB8`
- 디코드: `3`개 명령, `18/18` bytes 표시
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
  - `0x0024AF87` → [sub_0024B01B + 0x42](Unknown_function_0024B01B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0024AF7F  4C 89 B4 24 38 01 00 00         mov qword ptr [rsp + 0x138], r14
0024AF87  0F 84 D0 00 00 00               je 0x14024b05d
0024AF8D  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0024AF7F(void)
{
    unsigned __int64 v_stack_p138;

    v_stack_p138 = v_r14;
    return *(unsigned __int64 *)(v_rbx + 16);
}
```

## 5. (Beta) C Style

```c
void sub_0024AF7F(void)
{
    uint64_t v_stack_p138;

    v_stack_p138 = local_r14;
    return *(uint64_t *)(local_rbx + 0x10);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024AF7F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0024AF7F[BB_0024AF7F]
  bb_0024AF8D[BB_0024AF8D]
  bb_0024AF7F -->|fallthrough| bb_0024AF8D
```
