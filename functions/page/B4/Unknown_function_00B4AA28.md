# sub_00B4AA28

- RVA: `0x00B4AA28`–`0x00B4AA8A` (길이 `98` bytes)
- VA: `0x0000000140B4AA28`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCD18`
- 디코드: `19`개 명령, `98/98` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B4AA36` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00B4AA7F` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B4AA28` → RVA `0x00F0B408` (`.data`; read)
- `0x00B4AA2F` → RVA `0x00021688` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B4AA36` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00B4AA7F` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B4AA3D` → [PopDiagTraceKernelQueriesAllowed + 0x25](../AB/PopDiagTraceKernelQueriesAllowed_function_00AB5C04.md) (`tail-transfer`)
  - `0x00B4AA85` → [PopDiagTraceKernelQueriesAllowed + 0x25](../AB/PopDiagTraceKernelQueriesAllowed_function_00AB5C04.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B4AA28  48 8B 0D D9 09 3C 00            mov rcx, qword ptr [rip + 0x3c09d9]
00B4AA2F  48 8D 15 52 6C 4D FF            lea rdx, [rip - 0xb293ae]
00B4AA36  E8 15 7A 84 FF                  call 0x140392450
00B4AA3B  84 C0                           test al, al
00B4AA3D  0F 84 E6 B1 F6 FF               je 0x140ab5c29
00B4AA43  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
00B4AA48  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00B4AA4D  48 8B 0D B4 09 3C 00            mov rcx, qword ptr [rip + 0x3c09b4]
00B4AA54  48 8D 15 2D 6C 4D FF            lea rdx, [rip - 0xb293d3]
00B4AA5B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B4AA60  41 B9 01 00 00 00               mov r9d, 1
00B4AA66  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00B4AA6B  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00B4AA6F  45 33 C0                        xor r8d, r8d
00B4AA72  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B4AA77  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B4AA7F  E8 9C 1C 8D FF                  call 0x14041c720
00B4AA84  90                              nop
00B4AA85  E9 9F B1 F6 FF                  jmp 0x140ab5c29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B4AA28(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;

    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 3934681), v_rip - 11703214, a3, a4);
    v_stack_p38 = a6;
    v_stack_p30 = (unsigned int)(v_rbx);
    a3 = 0;
    v_stack_p20 = a7;
    v_stack_p40 = 4;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 3934644), v_rip - 11703251, a3, 1);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B4AA28(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, int64_t Arg7)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;

    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x3C09D9), v_rip - 11703214, Arg3, Arg4);
    v_stack_p38 = Arg6;
    v_stack_p30 = (uint32_t)(local_rbx);
    Arg3 = 0;
    v_stack_p20 = Arg7;
    v_stack_p40 = 4;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x3C09B4), v_rip - 11703251, Arg3, 1);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B4AA28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B4AA28[BB_00B4AA28]
  bb_00B4AA43[BB_00B4AA43]
  bb_00B4AA28 -->|fallthrough| bb_00B4AA43
```
