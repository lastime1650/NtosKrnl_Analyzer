# sub_002471AF

- RVA: `0x002471AF`–`0x002471C0` (길이 `17` bytes)
- VA: `0x00000001402471AF`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006234C`
- 디코드: `5`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002471B5` → [MiUnmapLockedPagesInUserSpace](../../page/A7/MiUnmapLockedPagesInUserSpace_function_00A78E54.md) (function, `0x00A78E54`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x002471B5` → [MiUnmapLockedPagesInUserSpace](../../page/A7/MiUnmapLockedPagesInUserSpace_function_00A78E54.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002471BA` → [sub_0024711D](Unknown_function_0024711D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002471AF  48 8B D7                        mov rdx, rdi
002471B2  48 8B CD                        mov rcx, rbp
002471B5  E8 9A 1C 83 00                  call 0x140a78e54
002471BA  E9 5E FF FF FF                  jmp 0x14024711d
002471BF  90                              nop
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002471AF(void)
{
    __int64 result;

    result = MiUnmapLockedPagesInUserSpace(v_rbp, v_rdi, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_002471AF(void)
{
    int64_t result;

    result = MiUnmapLockedPagesInUserSpace(local_rbp, local_rdi, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002471AF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002471AF[BB_002471AF]
  bb_002471BF[BB_002471BF]
```
