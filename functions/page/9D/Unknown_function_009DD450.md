# sub_009DD450

- RVA: `0x009DD450`–`0x009DD46E` (길이 `30` bytes)
- VA: `0x00000001409DD450`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A38EC`
- 디코드: `9`개 명령, `30/30` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x009DD455` → [sub_009DD363 + 0xBC](Unknown_function_009DD363.md) (`tail-transfer`)
  - `0x009DD45C` → [sub_009DD363 + 0xAB](Unknown_function_009DD363.md) (`tail-transfer`)
  - `0x009DD45E` → [sub_009DD363 + 0x83](Unknown_function_009DD363.md) (`tail-transfer`)
  - `0x009DD465` → [sub_009DD363 + 0xA0](Unknown_function_009DD363.md) (`tail-transfer`)
  - `0x009DD46C` → [sub_009DD363 + 0xBC](Unknown_function_009DD363.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009DD450  B8 95 00 00 C0                  mov eax, 0xc0000095
009DD455  EB C8                           jmp 0x1409dd41f
009DD457  3D 05 00 00 80                  cmp eax, 0x80000005
009DD45C  75 B0                           jne 0x1409dd40e
009DD45E  EB 86                           jmp 0x1409dd3e6
009DD460  BD 23 00 00 C0                  mov ebp, 0xc0000023
009DD465  EB 9C                           jmp 0x1409dd403
009DD467  B8 17 00 00 C0                  mov eax, 0xc0000017
009DD46C  EB B1                           jmp 0x1409dd41f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009DD450(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_009DD450(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009DD450&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009DD450[BB_009DD450]
  bb_009DD457[BB_009DD457]
  bb_009DD45E[BB_009DD45E]
  bb_009DD460[BB_009DD460]
  bb_009DD467[BB_009DD467]
  bb_009DD457 -->|fallthrough| bb_009DD45E
```
