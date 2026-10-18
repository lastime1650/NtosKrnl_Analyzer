# sub_0033D464

- RVA: `0x0033D464`–`0x0033D47A` (길이 `22` bytes)
- VA: `0x000000014033D464`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007714C`
- 디코드: `6`개 명령, `22/22` bytes 표시
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
  - `0x0033D46A` → [sub_0033D3B7 + 0x32](Unknown_function_0033D3B7.md) (`tail-transfer`)
  - `0x0033D475` → [sub_0033D3B7 + 0x3B](Unknown_function_0033D3B7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0033D464  49 89 06                        mov qword ptr [r14], rax
0033D467  4D 8B E6                        mov r12, r14
0033D46A  E9 7A FF FF FF                  jmp 0x14033d3e9
0033D46F  4C 8B F1                        mov r14, rcx
0033D472  48 8B 09                        mov rcx, qword ptr [rcx]
0033D475  E9 78 FF FF FF                  jmp 0x14033d3f2
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0033D464(__int64 a1)
{
    *(unsigned __int64 *)(v_r14) = result;
}
```

## 5. (Beta) C Style

```c
void sub_0033D464(int64_t Arg1)
{
    *(uint64_t *)(local_r14) = result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033D464&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0033D464[BB_0033D464]
  bb_0033D46F[BB_0033D46F]
```
