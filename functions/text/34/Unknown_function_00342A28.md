# sub_00342A28

- RVA: `0x00342A28`–`0x00342A4A` (길이 `34` bytes)
- VA: `0x0000000140342A28`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000778CC`
- 디코드: `6`개 명령, `34/34` bytes 표시
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
  - `0x00342A2B` → [sub_003422B4 + 0x1FD](Unknown_function_003422B4.md) (`tail-transfer`)
  - `0x00342A3F` → [sub_003422B4 + 0x1FD](Unknown_function_003422B4.md) (`tail-transfer`)
  - `0x00342A45` → [sub_003422B4 + 0x1B2](Unknown_function_003422B4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00342A28  49 3B C7                        cmp rax, r15
00342A2B  0F 85 80 FA FF FF               jne 0x1403424b1
00342A31  49 8B 87 10 05 00 00            mov rax, qword ptr [r15 + 0x510]
00342A38  48 39 83 B8 01 00 00            cmp qword ptr [rbx + 0x1b8], rax
00342A3F  0F 85 6C FA FF FF               jne 0x1403424b1
00342A45  E9 1C FA FF FF                  jmp 0x140342466
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00342A28(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_00342A28(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00342A28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00342A28[BB_00342A28]
  bb_00342A31[BB_00342A31]
  bb_00342A45[BB_00342A45]
  bb_00342A28 -->|fallthrough| bb_00342A31
  bb_00342A31 -->|fallthrough| bb_00342A45
```
