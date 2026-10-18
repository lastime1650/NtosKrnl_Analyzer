# IoQueueWorkItemToNode

- RVA: `0x0043C960`–`0x0043C9A7` (길이 `71` bytes)
- VA: `0x000000014043C960`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B95C`
- 디코드: `24`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0043C975` → [IopQueueWorkItemProlog](IopQueueWorkItemProlog_function_0043C9B0.md) (function, `0x0043C9B0`)
- `0x0043C984` → [ExQueueWorkItemExFromIo](ExQueueWorkItemExFromIo_function_0043CB58.md) (function, `0x0043CB58`)
- `0x0043C9A0` → [IopQueueWorkItemNotInsertedEpilog](../59/IopQueueWorkItemNotInsertedEpilog_function_00598404.md) (function, `0x00598404`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043C960  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0043C965  57                              push rdi
0043C966  48 83 EC 20                     sub rsp, 0x20
0043C96A  41 8B D8                        mov ebx, r8d
0043C96D  48 8B F9                        mov rdi, rcx
0043C970  4C 8B C2                        mov r8, rdx
0043C973  8B D3                           mov edx, ebx
0043C975  E8 36 00 00 00                  call 0x14043c9b0
0043C97A  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
0043C97F  8B D3                           mov edx, ebx
0043C981  48 8B C8                        mov rcx, rax
0043C984  E8 CF 01 00 00                  call 0x14043cb58
0043C989  8A D8                           mov bl, al
0043C98B  84 C0                           test al, al
0043C98D  74 0E                           je 0x14043c99d
0043C98F  8A C3                           mov al, bl
0043C991  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0043C996  48 83 C4 20                     add rsp, 0x20
0043C99A  5F                              pop rdi
0043C99B  C3                              ret
0043C99C  CC                              int3
0043C99D  48 8B CF                        mov rcx, rdi
0043C9A0  E8 5F BA 15 00                  call 0x140598404
0043C9A5  EB E8                           jmp 0x14043c98f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoQueueWorkItemToNode(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = IopQueueWorkItemProlog(a1, (unsigned int)((unsigned int)((unsigned int)(a3))), a2, a4);
    result = ExQueueWorkItemExFromIo(result, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)(a5), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0043C99D;
loc_0043C98F:
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)((unsigned __int8)(result));
loc_0043C99D:
    result = IopQueueWorkItemNotInsertedEpilog(a1, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)(a5), a4);
    goto loc_0043C98F;
}
```

## 5. (Beta) C Style

```c
int64_t IoQueueWorkItemToNode(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = IopQueueWorkItemProlog(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg2, Arg4);
    result = ExQueueWorkItemExFromIo(result, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)(Arg5), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0043C99D;
loc_0043C98F:
    local_rsp = (local_rsp) + (32);
    return (uint8_t)((uint8_t)(result));
loc_0043C99D:
    result = IopQueueWorkItemNotInsertedEpilog(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)(Arg5), Arg4);
    goto loc_0043C98F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043C960&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043C960[BB_0043C960]
  bb_0043C98F[BB_0043C98F]
  bb_0043C99C[BB_0043C99C]
  bb_0043C99D[BB_0043C99D]
  bb_0043C960 -->|branch| bb_0043C99D
  bb_0043C960 -->|fallthrough| bb_0043C98F
  bb_0043C99C -->|flow| bb_0043C99D
  bb_0043C99D -->|branch| bb_0043C98F
```
