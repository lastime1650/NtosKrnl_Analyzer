# sub_00B36C58

- RVA: `0x00B36C58`–`0x00B36C8C` (길이 `52` bytes)
- VA: `0x0000000140B36C58`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9338`
- 디코드: `11`개 명령, `52/52` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B36C6A` → [DbgkSendSystemDllMessages + 0x271](../A1/DbgkSendSystemDllMessages_function_00A10C04.md) (`tail-transfer`)
  - `0x00B36C87` → [DbgkSendSystemDllMessages + 0x271](../A1/DbgkSendSystemDllMessages_function_00A10C04.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B36C58  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
00B36C5D  4D 85 FF                        test r15, r15
00B36C60  74 08                           je 0x140b36c6a
00B36C62  49 C7 47 28 00 00 00 00         mov qword ptr [r15 + 0x28], 0
00B36C6A  E9 06 A2 ED FF                  jmp 0x140a10e75
00B36C6F  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
00B36C73  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00B36C78  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00B36C7D  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00B36C82  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
00B36C87  E9 E9 A1 ED FF                  jmp 0x140a10e75
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00B36C58(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;

    if (a7 != 0) {
        *(unsigned __int64 *)(a7 + 40) = 0;
    }
}
```

## 5. (Beta) C Style

```c
void sub_00B36C58(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, int64_t Arg7)
{
    uint32_t v_stack_p34;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;

    if (Arg7 != 0) {
        *(uint64_t *)(Arg7 + 0x28) = 0;
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B36C58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B36C58[BB_00B36C58]
  bb_00B36C62[BB_00B36C62]
  bb_00B36C6A[BB_00B36C6A]
  bb_00B36C6F[BB_00B36C6F]
  bb_00B36C58 -->|branch| bb_00B36C6A
  bb_00B36C58 -->|fallthrough| bb_00B36C62
  bb_00B36C62 -->|flow| bb_00B36C6A
```
