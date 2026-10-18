# sub_0033A09C

- RVA: `0x0033A09C`–`0x0033A0AF` (길이 `19` bytes)
- VA: `0x000000014033A09C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076C28`
- 디코드: `4`개 명령, `19/19` bytes 표시
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
  - `0x0033A0A2` → [sub_00339916 + 0x23A](Unknown_function_00339916.md) (`tail-transfer`)
  - `0x0033A0AA` → [sub_00339916 + 0x292](Unknown_function_00339916.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0033A09C  41 BC 09 00 00 00               mov r12d, 9
0033A0A2  E9 A9 FA FF FF                  jmp 0x140339b50
0033A0A7  8D 4A FF                        lea ecx, [rdx - 1]
0033A0AA  E9 F9 FA FF FF                  jmp 0x140339ba8
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0033A09C(__int64 a1, __int64 a2)
{
}
```

## 5. (Beta) C Style

```c
void sub_0033A09C(int64_t Arg1, int64_t Arg2)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033A09C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0033A09C[BB_0033A09C]
  bb_0033A0A7[BB_0033A0A7]
```
