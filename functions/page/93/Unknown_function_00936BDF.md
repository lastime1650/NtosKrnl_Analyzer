# sub_00936BDF

- RVA: `0x00936BDF`–`0x00936BFB` (길이 `28` bytes)
- VA: `0x0000000140936BDF`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008F404`
- 디코드: `6`개 명령, `28/28` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00936BE4` → [sub_0093691A + 0x1C0](Unknown_function_0093691A.md) (`tail-transfer`)
  - `0x00936BEE` → [sub_0093691A + 0x1C0](Unknown_function_0093691A.md) (`tail-transfer`)
  - `0x00936BF6` → [sub_0093691A + 0x1BD](Unknown_function_0093691A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00936BDF  BE F0 00 00 C0                  mov esi, 0xc00000f0
00936BE4  E9 F1 FE FF FF                  jmp 0x140936ada
00936BE9  BE 9A 00 00 C0                  mov esi, 0xc000009a
00936BEE  E9 E7 FE FF FF                  jmp 0x140936ada
00936BF3  4C 89 26                        mov qword ptr [rsi], r12
00936BF6  E9 DC FE FF FF                  jmp 0x140936ad7
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00936BDF(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_00936BDF(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00936BDF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00936BDF[BB_00936BDF]
  bb_00936BE9[BB_00936BE9]
  bb_00936BF3[BB_00936BF3]
```
