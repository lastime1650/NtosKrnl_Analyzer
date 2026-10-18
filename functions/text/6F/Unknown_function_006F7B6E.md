# sub_006F7B6E

- RVA: `0x006F7B6E`–`0x006F7B81` (길이 `19` bytes)
- VA: `0x00000001406F7B6E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B489C`
- 디코드: `5`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F7B76` → [EtwpCCSwapStop](../../page/7C/EtwpCCSwapStop_function_007C307C.md) (function, `0x007C307C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006F7B76` → [EtwpCCSwapStop](../../page/7C/EtwpCCSwapStop_function_007C307C.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F7B7C` → [EtwpUpdateSelectedGroupMasks + 0x130](../49/EtwpUpdateSelectedGroupMasks_function_0049B114.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F7B6E  8B 8B C8 00 00 00               mov ecx, dword ptr [rbx + 0xc8]
006F7B74  B2 01                           mov dl, 1
006F7B76  E8 01 B5 0C 00                  call 0x1407c307c
006F7B7B  90                              nop
006F7B7C  E9 C3 36 DA FF                  jmp 0x14049b244
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F7B6E(void)
{
    __int64 result;

    result = EtwpCCSwapStop((unsigned int)(*(unsigned int *)(v_rbx + 200)), 1, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006F7B6E(void)
{
    int64_t result;

    result = EtwpCCSwapStop((uint32_t)(*(uint32_t *)(local_rbx + 0xC8)), 1, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F7B6E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F7B6E[BB_006F7B6E]
```
