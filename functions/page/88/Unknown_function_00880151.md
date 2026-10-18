# sub_00880151

- RVA: `0x00880151`–`0x0088016C` (길이 `27` bytes)
- VA: `0x0000000140880151`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007C410`
- 디코드: `7`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0088015F` → [MiCoalescePlaceholderAllocations](MiCoalescePlaceholderAllocations_function_0088095C.md) (function, `0x0088095C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00880167` → [sub_0087FFB4 + 0xEA](../87/Unknown_function_0087FFB4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00880151  44 0F B6 4D 77                  movzx r9d, byte ptr [rbp + 0x77]
00880156  4D 8B C7                        mov r8, r15
00880159  48 8B D7                        mov rdx, rdi
0088015C  49 8B CD                        mov rcx, r13
0088015F  E8 F8 07 00 00                  call 0x14088095c
00880164  89 45 87                        mov dword ptr [rbp - 0x79], eax
00880167  E9 32 FF FF FF                  jmp 0x14088009e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00880151(void)
{
    __int64 result;

    result = MiCoalescePlaceholderAllocations(v_r13, v_rdi, v_r15, *(unsigned __int8 *)(v_rbp + 119));
    *(unsigned int *)(v_rbp - 121) = (unsigned int)(result);
}
```

## 5. (Beta) C Style

```c
void sub_00880151(void)
{
    int64_t result;

    result = MiCoalescePlaceholderAllocations(local_r13, local_rdi, local_r15, *(uint8_t *)(local_rbp + 0x77));
    *(uint32_t *)(local_rbp - 0x79) = (uint32_t)(result);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00880151&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00880151[BB_00880151]
```
