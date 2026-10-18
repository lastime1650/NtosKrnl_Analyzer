# sub_003FF6D6

- RVA: `0x003FF6D6`–`0x003FF6F4` (길이 `30` bytes)
- VA: `0x00000001403FF6D6`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A0B4`
- 디코드: `7`개 명령, `30/30` bytes 표시
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
  - `0x003FF6D9` → [sub_003FF566 + 0xF4](Unknown_function_003FF566.md) (`tail-transfer`)
  - `0x003FF6EF` → [sub_003FF566 + 0xF4](Unknown_function_003FF566.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003FF6D6  45 85 DB                        test r11d, r11d
003FF6D9  0F 84 7B FF FF FF               je 0x1403ff65a
003FF6DF  41 8D 4B FF                     lea ecx, [r11 - 1]
003FF6E3  48 8D 49 01                     lea rcx, [rcx + 1]
003FF6E7  48 8D 04 49                     lea rax, [rcx + rcx*2]
003FF6EB  44 01 04 C6                     add dword ptr [rsi + rax*8], r8d
003FF6EF  E9 66 FF FF FF                  jmp 0x1403ff65a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003FF6D6(__int64 a1, __int64 a2, int a3)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_003FF6D6(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FF6D6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FF6D6[BB_003FF6D6]
  bb_003FF6DF[BB_003FF6DF]
  bb_003FF6D6 -->|fallthrough| bb_003FF6DF
```
