# sub_008C76F3

- RVA: `0x008C76F3`–`0x008C7704` (길이 `17` bytes)
- VA: `0x00000001408C76F3`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00083F18`
- 디코드: `6`개 명령, `17/17` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008C76FA` → [sub_008C7665 + 0x4C](Unknown_function_008C7665.md) (`tail-transfer`)
  - `0x008C7702` → [sub_008C7665 + 0x59](Unknown_function_008C7665.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008C76F3  49 8B 57 38                     mov rdx, qword ptr [r15 + 0x38]
008C76F7  48 85 D2                        test rdx, rdx
008C76FA  74 B5                           je 0x1408c76b1
008C76FC  48 3B C2                        cmp rax, rdx
008C76FF  0F 94 C0                        sete al
008C7702  EB BA                           jmp 0x1408c76be
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008C76F3(void)
{
    __int64 result;

    result = (result == (*(unsigned __int64 *)(v_r15 + 56))) ? 1 : 0;
}
```

## 5. (Beta) C Style

```c
void sub_008C76F3(void)
{
    int64_t result;

    result = (result == (*(uint64_t *)(local_r15 + 0x38))) ? 1 : 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C76F3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C76F3[BB_008C76F3]
  bb_008C76FC[BB_008C76FC]
  bb_008C76F3 -->|fallthrough| bb_008C76FC
```
