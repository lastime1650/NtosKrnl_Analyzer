# sub_0085EF76

- RVA: `0x0085EF76`–`0x0085EF90` (길이 `26` bytes)
- VA: `0x000000014085EF76`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B308`
- 디코드: `6`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0085EF79` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0085EF79` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0085EF80` → [sub_0085EBA1](Unknown_function_0085EBA1.md) (`tail-transfer`)
  - `0x0085EF8B` → [sub_0085EDFE + 0x11](Unknown_function_0085EDFE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085EF76  49 8B CE                        mov rcx, r14
0085EF79  E8 D2 D0 AE FF                  call 0x14034c050
0085EF7E  84 C0                           test al, al
0085EF80  0F 85 1B FC FF FF               jne 0x14085eba1
0085EF86  B8 80 00 00 C0                  mov eax, 0xc0000080
0085EF8B  E9 7F FE FF FF                  jmp 0x14085ee0f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0085EF76(void)
{
    __int64 result;

    result = ExfAcquireRundownProtection(v_r14, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0085EF76(void)
{
    int64_t result;

    result = ExfAcquireRundownProtection(local_r14, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085EF76&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085EF76[BB_0085EF76]
  bb_0085EF86[BB_0085EF86]
  bb_0085EF76 -->|fallthrough| bb_0085EF86
```
