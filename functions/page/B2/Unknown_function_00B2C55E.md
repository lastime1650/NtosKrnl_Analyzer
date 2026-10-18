# sub_00B2C55E

- RVA: `0x00B2C55E`–`0x00B2C56E` (길이 `16` bytes)
- VA: `0x0000000140B2C55E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000992B4`
- 디코드: `4`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B2C562` → [VfDriverProcessUnload](../../text/61/VfDriverProcessUnload_function_0061306C.md) (function, `0x0061306C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B2C562` → [VfDriverProcessUnload](../../text/61/VfDriverProcessUnload_function_0061306C.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B2C569` → [IopLoadUnloadDriver + 0x9B](../99/IopLoadUnloadDriver_function_00996B80.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B2C55E  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
00B2C562  E8 05 6B AE FF                  call 0x14061306c
00B2C567  33 DB                           xor ebx, ebx
00B2C569  E9 AD A6 E6 FF                  jmp 0x140996c1b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B2C55E(void)
{
    __int64 result;
    __int64 v_rbx;

    result = VfDriverProcessUnload(*(unsigned __int64 *)(v_rdi + 56), a2, a3, a4);
    v_rbx = 0;
}
```

## 5. (Beta) C Style

```c
void sub_00B2C55E(void)
{
    int64_t result;
    int64_t local_rbx;

    result = VfDriverProcessUnload(*(uint64_t *)(local_rdi + 0x38), a2, a3, a4);
    local_rbx = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B2C55E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B2C55E[BB_00B2C55E]
```
