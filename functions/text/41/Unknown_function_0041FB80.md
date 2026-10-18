# sub_0041FB80

- RVA: `0x0041FB80`–`0x0041FB99` (길이 `25` bytes)
- VA: `0x000000014041FB80`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009FF2C`
- 디코드: `8`개 명령, `25/25` bytes 표시
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
  - `0x0041FB83` → [sub_006ED9E6](../6E/Unknown_function_006ED9E6.md) (`tail-transfer`)
  - `0x0041FB8B` → [sub_0041FB22 + 0x1C](Unknown_function_0041FB22.md) (`tail-transfer`)
  - `0x0041FB97` → [sub_0041FB22 + 0x2A](Unknown_function_0041FB22.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0041FB80  48 8B 0E                        mov rcx, qword ptr [rsi]
0041FB83  E9 5E DE 2C 00                  jmp 0x1406ed9e6
0041FB88  48 8B 00                        mov rax, qword ptr [rax]
0041FB8B  EB B1                           jmp 0x14041fb3e
0041FB8D  48 8B 0E                        mov rcx, qword ptr [rsi]
0041FB90  48 3B CE                        cmp rcx, rsi
0041FB93  48 0F 45 E9                     cmovne rbp, rcx
0041FB97  EB B3                           jmp 0x14041fb4c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0041FB80(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_0041FB80(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041FB80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041FB80[BB_0041FB80]
  bb_0041FB88[BB_0041FB88]
  bb_0041FB8D[BB_0041FB8D]
```
