# sub_00B25312

- RVA: `0x00B25312`–`0x00B2532F` (길이 `29` bytes)
- VA: `0x0000000140B25312`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00090064`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B25315` → [MiControlAreaHasHostRelocationsApplied](../../text/38/MiControlAreaHasHostRelocationsApplied_function_003843A4.md) (function, `0x003843A4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B25315` → [MiControlAreaHasHostRelocationsApplied](../../text/38/MiControlAreaHasHostRelocationsApplied_function_003843A4.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B2531C` → [MiValidateImagePfn + 0xF6](../93/MiValidateImagePfn_function_0093EA08.md) (`tail-transfer`)
  - `0x00B2532A` → [MiValidateImagePfn + 0xDC](../93/MiValidateImagePfn_function_0093EA08.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B25312  49 8B CF                        mov rcx, r15
00B25315  E8 8A F0 85 FF                  call 0x1403843a4
00B2531A  85 C0                           test eax, eax
00B2531C  0F 84 DC 97 E1 FF               je 0x14093eafe
00B25322  45 8B C2                        mov r8d, r10d
00B25325  44 89 54 24 30                  mov dword ptr [rsp + 0x30], r10d
00B2532A  E9 B5 97 E1 FF                  jmp 0x14093eae4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B25312(void)
{
    __int64 result;
    unsigned int v_stack_p30;

    result = MiControlAreaHasHostRelocationsApplied(v_r15, a2, a3, a4);
    v_stack_p30 = (unsigned int)(v_r10);
}
```

## 5. (Beta) C Style

```c
void sub_00B25312(void)
{
    int64_t result;
    uint32_t v_stack_p30;

    result = MiControlAreaHasHostRelocationsApplied(local_r15, a2, a3, a4);
    v_stack_p30 = (uint32_t)(local_r10);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B25312&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B25312[BB_00B25312]
  bb_00B25322[BB_00B25322]
  bb_00B25312 -->|fallthrough| bb_00B25322
```
