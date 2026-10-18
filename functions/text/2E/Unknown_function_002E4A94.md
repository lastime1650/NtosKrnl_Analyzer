# sub_002E4A94

- RVA: `0x002E4A94`–`0x002E4AA6` (길이 `18` bytes)
- VA: `0x00000001402E4A94`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071068`
- 디코드: `5`개 명령, `18/18` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002E4AA1` → [sub_002E4705 + 0xB9](Unknown_function_002E4705.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E4A94  48 8B C6                        mov rax, rsi
002E4A97  48 33 C7                        xor rax, rdi
002E4A9A  48 85 F6                        test rsi, rsi
002E4A9D  4C 0F 45 F8                     cmovne r15, rax
002E4AA1  E9 18 FD FF FF                  jmp 0x1402e47be
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E4A94(void)
{
    __int64 result;
    __int64 v_r15;

    result = (v_rsi) ^ (v_rdi);
    if (v_rsi != 0) { v_r15 = result; }
}
```

## 5. (Beta) C Style

```c
void sub_002E4A94(void)
{
    int64_t result;
    int64_t local_r15;

    result = (local_rsi) ^ (local_rdi);
    if (local_rsi != 0) { local_r15 = result; }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E4A94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E4A94[BB_002E4A94]
```
