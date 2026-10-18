# sub_00855BF3

- RVA: `0x00855BF3`–`0x00855C12` (길이 `31` bytes)
- VA: `0x0000000140855BF3`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A1CC`
- 디코드: `7`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00855C08` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00855BFA` → [sub_00855A5C + 0x30](Unknown_function_00855A5C.md) (`tail-transfer`)
  - `0x00855C03` → [sub_00855A5C + 0x20](Unknown_function_00855A5C.md) (`tail-transfer`)
  - `0x00855C0D` → [sub_00855A5C + 0xBF](Unknown_function_00855A5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00855BF3  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00855BF7  48 85 C0                        test rax, rax
00855BFA  0F 84 8C FE FF FF               je 0x140855a8c
00855C00  48 8B E8                        mov rbp, rax
00855C03  E9 74 FE FF FF                  jmp 0x140855a7c
00855C08  E8 A3 F0 FF FF                  call 0x140854cb0
00855C0D  E9 09 FF FF FF                  jmp 0x140855b1b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00855BF3(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_00855BF3(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00855BF3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00855BF3[BB_00855BF3]
  bb_00855C00[BB_00855C00]
  bb_00855C08[BB_00855C08]
  bb_00855BF3 -->|fallthrough| bb_00855C00
```
