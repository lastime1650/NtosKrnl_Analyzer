# sub_008A0B2F

- RVA: `0x008A0B2F`–`0x008A0B40` (길이 `17` bytes)
- VA: `0x00000001408A0B2F`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E96C`
- 디코드: `4`개 명령, `17/17` bytes 표시
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
  - `0x008A0B33` → [sub_008A095D + 0x46](Unknown_function_008A095D.md) (`tail-transfer`)
  - `0x008A0B3B` → [sub_008A0A32 + 0x8](Unknown_function_008A0A32.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008A0B2F  83 7B 28 02                     cmp dword ptr [rbx + 0x28], 2
008A0B33  0F 8D 6A FE FF FF               jge 0x1408a09a3
008A0B39  8B FD                           mov edi, ebp
008A0B3B  E9 FA FE FF FF                  jmp 0x1408a0a3a
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_008A0B2F(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_008A0B2F(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A0B2F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008A0B2F[BB_008A0B2F]
  bb_008A0B39[BB_008A0B39]
  bb_008A0B2F -->|fallthrough| bb_008A0B39
```
