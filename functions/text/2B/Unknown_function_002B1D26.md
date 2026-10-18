# sub_002B1D26

- RVA: `0x002B1D26`–`0x002B1D4E` (길이 `40` bytes)
- VA: `0x00000001402B1D26`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006D69C`
- 디코드: `10`개 명령, `40/40` bytes 표시
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
  - `0x002B1D31` → [MiCopyPage + 0x9A](MiCopyPage_function_002B1B30.md) (`tail-transfer`)
  - `0x002B1D49` → [MiCopyPage + 0x82](MiCopyPage_function_002B1B30.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002B1D26  41 0F BA E7 08                  bt r15d, 8
002B1D2B  8B D3                           mov edx, ebx
002B1D2D  41 0F 42 D6                     cmovb edx, r14d
002B1D31  E9 94 FE FF FF                  jmp 0x1402b1bca
002B1D36  41 0F BA E7 08                  bt r15d, 8
002B1D3B  8B C3                           mov eax, ebx
002B1D3D  B9 40 00 00 00                  mov ecx, 0x40
002B1D42  0F 42 C1                        cmovb eax, ecx
002B1D45  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002B1D49  E9 64 FE FF FF                  jmp 0x1402b1bb2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002B1D26(void)
{
    unsigned int v_stack_p30;

    a2 = (unsigned int)((unsigned int)(v_rbx));
    if (condition_is_below) { a2 = (unsigned int)(v_r14); }
}
```

## 5. (Beta) C Style

```c
void sub_002B1D26(void)
{
    uint32_t v_stack_p30;

    a2 = (uint32_t)((uint32_t)(local_rbx));
    if (condition_is_below) { a2 = (uint32_t)(local_r14); }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B1D26&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002B1D26[BB_002B1D26]
  bb_002B1D36[BB_002B1D36]
```
