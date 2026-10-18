# sub_006DDBE2

- RVA: `0x006DDBE2`–`0x006DDBFA` (길이 `24` bytes)
- VA: `0x00000001406DDBE2`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006FDBC`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DDBE8` → [KiIntSteerLogState](../2D/KiIntSteerLogState_function_002D57BC.md) (function, `0x002D57BC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DDBF5` → [KiIntSteerLogStatus + 0x8B](../2D/KiIntSteerLogStatus_function_002D6400.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DDBE2  49 8B D6                        mov rdx, r14
006DDBE5  48 8B CF                        mov rcx, rdi
006DDBE8  E8 CF 7B BF FF                  call 0x1402d57bc
006DDBED  48 8B 3F                        mov rdi, qword ptr [rdi]
006DDBF0  48 3B FE                        cmp rdi, rsi
006DDBF3  75 ED                           jne 0x1406ddbe2
006DDBF5  E9 91 88 BF FF                  jmp 0x1402d648b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DDBE2(void)
{
    __int64 result;

    result = KiIntSteerLogState(v_rdi, v_r14, a3, a4);
    if ((*(unsigned __int64 *)(v_rdi)) != v_rsi) goto loc_006DDBE2;
}
```

## 5. (Beta) C Style

```c
void sub_006DDBE2(void)
{
    int64_t result;

    result = KiIntSteerLogState(local_rdi, local_r14, a3, a4);
    if ((*(uint64_t *)(local_rdi)) != local_rsi) goto loc_006DDBE2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DDBE2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DDBE2[BB_006DDBE2]
  bb_006DDBF5[BB_006DDBF5]
  bb_006DDBE2 -->|branch| bb_006DDBE2
  bb_006DDBE2 -->|fallthrough| bb_006DDBF5
```
