# sub_0034DBAE

- RVA: `0x0034DBAE`–`0x0034DBC7` (길이 `25` bytes)
- VA: `0x000000014034DBAE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078AB8`
- 디코드: `6`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0034DBBD` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0034DBB1` → [sub_0034DA7E + 0x5F](Unknown_function_0034DA7E.md) (`tail-transfer`)
  - `0x0034DBC2` → [sub_0034DA7E + 0x24](Unknown_function_0034DA7E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0034DBAE  49 8B FE                        mov rdi, r14
0034DBB1  E9 27 FF FF FF                  jmp 0x14034dadd
0034DBB6  0F B6 D0                        movzx edx, al
0034DBB9  40 0F B6 CE                     movzx ecx, sil
0034DBBD  E8 3A 7B 1A 00                  call 0x1404f56fc
0034DBC2  E9 DB FE FF FF                  jmp 0x14034daa2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0034DBAE(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_0034DBAE(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034DBAE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0034DBAE[BB_0034DBAE]
  bb_0034DBB6[BB_0034DBB6]
```
