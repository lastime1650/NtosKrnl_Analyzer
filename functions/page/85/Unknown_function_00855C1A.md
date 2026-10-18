# sub_00855C1A

- RVA: `0x00855C1A`–`0x00855C2E` (길이 `20` bytes)
- VA: `0x0000000140855C1A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A210`
- 디코드: `4`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00855C24` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00855C1F` → [sub_00855A5C + 0x79](Unknown_function_00855A5C.md) (`tail-transfer`)
  - `0x00855C29` → [sub_00855A5C + 0x117](Unknown_function_00855A5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00855C1A  49 8B 7C C4 F0                  mov rdi, qword ptr [r12 + rax*8 - 0x10]
00855C1F  E9 B1 FE FF FF                  jmp 0x140855ad5
00855C24  E8 F7 6F 00 00                  call 0x14085cc20
00855C29  E9 45 FF FF FF                  jmp 0x140855b73
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00855C1A(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_00855C1A(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00855C1A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00855C1A[BB_00855C1A]
  bb_00855C24[BB_00855C24]
```
