# sub_0085800D

- RVA: `0x0085800D`–`0x00858022` (길이 `21` bytes)
- VA: `0x000000014085800D`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A790`
- 디코드: `5`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00858018` → [CmpUnlockHashEntryByKcb](../86/CmpUnlockHashEntryByKcb_function_00864370.md) (function, `0x00864370`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00858010` → [sub_00857CAB + 0x15](Unknown_function_00857CAB.md) (`tail-transfer`)
  - `0x0085801D` → [sub_00857CAB + 0x96](Unknown_function_00857CAB.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085800D  41 B6 01                        mov r14b, 1
00858010  E9 AB FC FF FF                  jmp 0x140857cc0
00858015  49 8B CF                        mov rcx, r15
00858018  E8 53 C3 00 00                  call 0x140864370
0085801D  E9 1F FD FF FF                  jmp 0x140857d41
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0085800D(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_0085800D(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085800D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085800D[BB_0085800D]
  bb_00858015[BB_00858015]
```
