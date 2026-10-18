# sub_00988CC0

- RVA: `0x00988CC0`–`0x00988CD4` (길이 `20` bytes)
- VA: `0x0000000140988CC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097EE4`
- 디코드: `5`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00988CCA` → [RtlClearBitsEx](../../text/29/RtlClearBitsEx_function_00297740.md) (function, `0x00297740`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00988CCA` → [RtlClearBitsEx](../../text/29/RtlClearBitsEx_function_00297740.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00988CCF` → [sub_00988BDE](Unknown_function_00988BDE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00988CC0  44 8B 43 08                     mov r8d, dword ptr [rbx + 8]
00988CC4  48 8B D7                        mov rdx, rdi
00988CC7  49 8B CF                        mov rcx, r15
00988CCA  E8 71 EA 90 FF                  call 0x140297740
00988CCF  E9 0A FF FF FF                  jmp 0x140988bde
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00988CC0(void)
{
    __int64 result;

    result = RtlClearBitsEx(v_r15, v_rdi, (unsigned int)(*(unsigned int *)(v_rbx + 8)), a4);
}
```

## 5. (Beta) C Style

```c
void sub_00988CC0(void)
{
    int64_t result;

    result = RtlClearBitsEx(local_r15, local_rdi, (uint32_t)(*(uint32_t *)(local_rbx + 0x8)), a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00988CC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00988CC0[BB_00988CC0]
```
