# sub_003D1E45

- RVA: `0x003D1E45`–`0x003D1E61` (길이 `28` bytes)
- VA: `0x00000001403D1E45`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00091330`
- 디코드: `7`개 명령, `28/28` bytes 표시
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
  - `0x003D1E47` → [sub_003D1C93 + 0xFB](Unknown_function_003D1C93.md) (`tail-transfer`)
  - `0x003D1E5C` → [sub_003D1C93 + 0xFB](Unknown_function_003D1C93.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003D1E45  85 D2                           test edx, edx
003D1E47  0F 84 41 FF FF FF               je 0x1403d1d8e
003D1E4D  8D 4A FF                        lea ecx, [rdx - 1]
003D1E50  48 8D 49 01                     lea rcx, [rcx + 1]
003D1E54  48 8D 04 49                     lea rax, [rcx + rcx*2]
003D1E58  41 01 34 C7                     add dword ptr [r15 + rax*8], esi
003D1E5C  E9 2D FF FF FF                  jmp 0x1403d1d8e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003D1E45(__int64 a1, __int64 a2)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_003D1E45(int64_t Arg1, int64_t Arg2)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D1E45&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003D1E45[BB_003D1E45]
  bb_003D1E4D[BB_003D1E4D]
  bb_003D1E45 -->|fallthrough| bb_003D1E4D
```
