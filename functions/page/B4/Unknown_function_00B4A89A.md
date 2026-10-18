# sub_00B4A89A

- RVA: `0x00B4A89A`–`0x00B4A8AE` (길이 `20` bytes)
- VA: `0x0000000140B4A89A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC414`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B4A8A3` → [PpmPerfResetHistory](../../text/40/PpmPerfResetHistory_function_0040AF08.md) (function, `0x0040AF08`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B4A8A3` → [PpmPerfResetHistory](../../text/40/PpmPerfResetHistory_function_0040AF08.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B4A8A9` → [PpmPerfResizeHistory + 0x4F](../AA/PpmPerfResizeHistory_function_00AAF9C8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B4A89A  89 18                           mov dword ptr [rax], ebx
00B4A89C  48 8B CE                        mov rcx, rsi
00B4A89F  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
00B4A8A3  E8 60 06 8C FF                  call 0x14040af08
00B4A8A8  90                              nop
00B4A8A9  E9 69 51 F6 FF                  jmp 0x140aafa17
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B4A89A(void)
{
    __int64 result;

    *(unsigned int *)(result) = (unsigned int)(v_rbx);
    *(unsigned __int64 *)(v_rsi + 32) = result;
    result = PpmPerfResetHistory(v_rsi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B4A89A(void)
{
    int64_t result;

    *(uint32_t *)(result) = (uint32_t)(local_rbx);
    *(uint64_t *)(local_rsi + 0x20) = result;
    result = PpmPerfResetHistory(local_rsi, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B4A89A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B4A89A[BB_00B4A89A]
```
