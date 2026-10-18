# sub_006D65FC

- RVA: `0x006D65FC`–`0x006D662C` (길이 `48` bytes)
- VA: `0x00000001406D65FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D5C8`
- 디코드: `11`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D6608` → [KeFirstGroupAffinityEx](../46/KeFirstGroupAffinityEx_function_00463810.md) (function, `0x00463810`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x006D660E` → [sub_002092A9 + 0x5C](../20/Unknown_function_002092A9.md) (`tail-transfer`)
  - `0x006D6616` → [sub_002092A9 + 0x5C](../20/Unknown_function_002092A9.md) (`tail-transfer`)
  - `0x006D6627` → [sub_002092A9 + 0x6E](../20/Unknown_function_002092A9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D65FC  48 8B 93 40 02 00 00            mov rdx, qword ptr [rbx + 0x240]
006D6603  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
006D6608  E8 03 D2 D8 FF                  call 0x140463810
006D660D  90                              nop
006D660E  E9 F2 2C B3 FF                  jmp 0x140209305
006D6613  40 84 ED                        test bpl, bpl
006D6616  0F 84 E9 2C B3 FF               je 0x140209305
006D661C  33 ED                           xor ebp, ebp
006D661E  44 88 61 12                     mov byte ptr [rcx + 0x12], r12b
006D6622  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
006D6627  E9 EB 2C B3 FF                  jmp 0x140209317
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D65FC(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12)
{
    __int64 result;
    unsigned __int64 v_stack_p38;

    result = KeFirstGroupAffinityEx(a12, *(unsigned __int64 *)(v_rbx + 576), a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006D65FC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, int64_t Arg12)
{
    int64_t result;
    uint64_t v_stack_p38;

    result = KeFirstGroupAffinityEx(Arg12, *(uint64_t *)(local_rbx + 0x240), Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D65FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D65FC[BB_006D65FC]
  bb_006D6613[BB_006D6613]
  bb_006D661C[BB_006D661C]
  bb_006D6613 -->|fallthrough| bb_006D661C
```
