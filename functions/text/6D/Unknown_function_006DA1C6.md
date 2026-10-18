# sub_006DA1C6

- RVA: `0x006DA1C6`–`0x006DA1ED` (길이 `39` bytes)
- VA: `0x00000001406DA1C6`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066860`
- 디코드: `9`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DA1D3` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x006DA1CB` → [MiResolveTransitionFault + 0xC05](../28/MiResolveTransitionFault_function_00282940.md) (`tail-transfer`)
  - `0x006DA1DE` → [MiResolveTransitionFault + 0x122](../28/MiResolveTransitionFault_function_00282940.md) (`tail-transfer`)
  - `0x006DA1E8` → [MiResolveTransitionFault + 0x465](../28/MiResolveTransitionFault_function_00282940.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DA1C6  BF 17 00 00 C0                  mov edi, 0xc0000017
006DA1CB  E9 75 93 BA FF                  jmp 0x140283545
006DA1D0  48 8B CB                        mov rcx, rbx
006DA1D3  E8 C8 86 BA FF                  call 0x1402828a0
006DA1D8  48 8B D8                        mov rbx, rax
006DA1DB  45 33 DB                        xor r11d, r11d
006DA1DE  E9 7F 88 BA FF                  jmp 0x140282a62
006DA1E3  B8 17 00 00 C0                  mov eax, 0xc0000017
006DA1E8  E9 B8 8B BA FF                  jmp 0x140282da5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DA1C6(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_006DA1C6(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DA1C6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DA1C6[BB_006DA1C6]
  bb_006DA1D0[BB_006DA1D0]
  bb_006DA1E3[BB_006DA1E3]
```
