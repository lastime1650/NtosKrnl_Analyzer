# sub_002E3422

- RVA: `0x002E3422`–`0x002E3430` (길이 `14` bytes)
- VA: `0x00000001402E3422`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070E18`
- 디코드: `3`개 명령, `14/14` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002E3426` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002E342B` → [sub_002E3191 + 0x25](Unknown_function_002E3191.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E3422  48 8D 4F 40                     lea rcx, [rdi + 0x40]
002E3426  E8 A5 29 F8 FF                  call 0x140265dd0
002E342B  E9 86 FD FF FF                  jmp 0x1402e31b6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E3422(void)
{
    __int64 result;

    result = ExfTryToWakePushLock(v_rdi + 64, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_002E3422(void)
{
    int64_t result;

    result = ExfTryToWakePushLock(local_rdi + 64, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E3422&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E3422[BB_002E3422]
```
