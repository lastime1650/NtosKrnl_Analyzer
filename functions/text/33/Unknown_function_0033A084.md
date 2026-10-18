# sub_0033A084

- RVA: `0x0033A084`–`0x0033A09C` (길이 `24` bytes)
- VA: `0x000000014033A084`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076C18`
- 디코드: `4`개 명령, `24/24` bytes 표시
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
  - `0x0033A08E` → [MiReplaceStandbyLookaside + 0xA4](MiReplaceStandbyLookaside_function_003397D0.md) (`tail-transfer`)
  - `0x0033A097` → [MiReplaceStandbyLookaside + 0xFA](MiReplaceStandbyLookaside_function_003397D0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0033A084  49 BC 10 00 00 00 00 DE FF FF   movabs r12, 0xffffde0000000010
0033A08E  E9 E1 F7 FF FF                  jmp 0x140339874
0033A093  41 8D 48 FF                     lea ecx, [r8 - 1]
0033A097  E9 2E F8 FF FF                  jmp 0x1403398ca
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0033A084(__int64 a1, __int64 a2, __int64 a3)
{
}
```

## 5. (Beta) C Style

```c
void sub_0033A084(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033A084&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0033A084[BB_0033A084]
  bb_0033A093[BB_0033A093]
```
