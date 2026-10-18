# sub_006E1EC7

- RVA: `0x006E1EC7`–`0x006E1ED9` (길이 `18` bytes)
- VA: `0x00000001406E1EC7`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000761D4`
- 디코드: `4`개 명령, `18/18` bytes 표시
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
  - `0x006E1ECB` → [sub_0032BD21 + 0x50C](../32/Unknown_function_0032BD21.md) (`tail-transfer`)
  - `0x006E1ED4` → [sub_0032BD21 + 0x50C](../32/Unknown_function_0032BD21.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E1EC7  41 83 F8 01                     cmp r8d, 1
006E1ECB  0F 85 5C A3 C4 FF               jne 0x14032c22d
006E1ED1  83 C9 08                        or ecx, 8
006E1ED4  E9 54 A3 C4 FF                  jmp 0x14032c22d
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006E1EC7(int a1, __int64 a2, int a3)
{
    a1 = (unsigned int)((a1) | (8));
}
```

## 5. (Beta) C Style

```c
void sub_006E1EC7(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    Arg1 = (uint32_t)((Arg1) | (8));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E1EC7&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E1EC7[BB_006E1EC7]
  bb_006E1ED1[BB_006E1ED1]
  bb_006E1EC7 -->|fallthrough| bb_006E1ED1
```
