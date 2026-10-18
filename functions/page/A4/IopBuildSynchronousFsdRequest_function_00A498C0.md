# IopBuildSynchronousFsdRequest

- RVA: `0x00A498C0`–`0x00A49914` (길이 `84` bytes)
- VA: `0x0000000140A498C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AFE8C`
- 디코드: `22`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A498EA` → [IopBuildAsynchronousFsdRequest](../../text/29/IopBuildAsynchronousFsdRequest_function_0029DD40.md) (function, `0x0029DD40`)
- `0x00A49903` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (function, `0x002075C0`)

### Direct callers
- [IoBuildSynchronousFsdRequest](IoBuildSynchronousFsdRequest_function_00A49880.md) at `0x00A498AE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A498EA` → [IopBuildAsynchronousFsdRequest](../../text/29/IopBuildAsynchronousFsdRequest_function_0029DD40.md) (`PAGE` → `.text`)
  - `0x00A49903` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A498C0  40 53                           push rbx
00A498C2  48 83 EC 40                     sub rsp, 0x40
00A498C6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00A498CE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A498D3  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00A498DB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A498E0  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A498E5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A498EA  E8 51 44 85 FF                  call 0x14029dd40
00A498EF  48 8B D8                        mov rbx, rax
00A498F2  48 85 C0                        test rax, rax
00A498F5  74 1B                           je 0x140a49912
00A498F7  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00A498FC  48 8B CB                        mov rcx, rbx
00A498FF  48 89 43 50                     mov qword ptr [rbx + 0x50], rax
00A49903  E8 B8 DC 7B FF                  call 0x1402075c0
00A49908  48 8B C3                        mov rax, rbx
00A4990B  48 83 C4 40                     add rsp, 0x40
00A4990F  5B                              pop rbx
00A49910  C3                              ret
00A49911  CC                              int3
00A49912  EB F7                           jmp 0x140a4990b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopBuildSynchronousFsdRequest(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (64);
    v_stack_m18 = a8;
    v_stack_m20 = a7;
    v_stack_m28 = a5;
    result = IopBuildAsynchronousFsdRequest(a1, a2, a3, a4);
    if (result == 0) goto loc_00A49912;
    *(unsigned __int64 *)(result + 80) = a6;
    result = IopQueueThreadIrp(result, a2, a3, a4);
loc_00A4990B:
    v_rsp = (v_rsp) + (64);
    return result;
loc_00A49912:
    goto loc_00A4990B;
}
```

## 5. (Beta) C Style

```c
int64_t IopBuildSynchronousFsdRequest(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    v_stack_m18 = Arg8;
    v_stack_m20 = Arg7;
    v_stack_m28 = Arg5;
    result = IopBuildAsynchronousFsdRequest(Arg1, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00A49912;
    *(uint64_t *)(result + 0x50) = Arg6;
    result = IopQueueThreadIrp(result, Arg2, Arg3, Arg4);
loc_00A4990B:
    local_rsp = (local_rsp) + (64);
    return result;
loc_00A49912:
    goto loc_00A4990B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A498C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A498C0[BB_00A498C0]
  bb_00A498F7[BB_00A498F7]
  bb_00A4990B[BB_00A4990B]
  bb_00A49911[BB_00A49911]
  bb_00A49912[BB_00A49912]
  bb_00A498C0 -->|branch| bb_00A49912
  bb_00A498C0 -->|fallthrough| bb_00A498F7
  bb_00A498F7 -->|flow| bb_00A4990B
  bb_00A49911 -->|flow| bb_00A49912
  bb_00A49912 -->|branch| bb_00A4990B
```
