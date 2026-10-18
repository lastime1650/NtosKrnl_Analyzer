# sub_0031EF0D

- RVA: `0x0031EF0D`–`0x0031EF1F` (길이 `18` bytes)
- VA: `0x000000014031EF0D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075300`
- 디코드: `4`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0031EF15` → [MiUnlockPage](MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0031EF1A` → [sub_0031EDB1 + 0x1A](Unknown_function_0031EDB1.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031EF0D  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
0031EF12  0F B6 D0                        movzx edx, al
0031EF15  E8 C6 B4 FF FF                  call 0x14031a3e0
0031EF1A  E9 AC FE FF FF                  jmp 0x14031edcb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0031EF0D(void)
{
    __int64 result;
    unsigned __int64 v_stack_p20;

    result = MiUnlockPage(v_stack_p20, (unsigned __int8)(result), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0031EF0D(void)
{
    int64_t result;
    uint64_t v_stack_p20;

    result = MiUnlockPage(v_stack_p20, (uint8_t)(result), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031EF0D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0031EF0D[BB_0031EF0D]
```
