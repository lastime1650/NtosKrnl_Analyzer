# VfConfigureAdapterChannel

- RVA: `0x00B960E0`–`0x00B9611B` (길이 `59` bytes)
- VA: `0x0000000140B960E0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `18`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B960EF` → [ViGetRealDmaAdapter](ViGetRealDmaAdapter_function_00B990DC.md) (function, `0x00B990DC`)
- `0x00B9610A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B9610A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B960E0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B960E5  57                              push rdi
00B960E6  48 83 EC 20                     sub rsp, 0x20
00B960EA  49 8B D8                        mov rbx, r8
00B960ED  8B FA                           mov edi, edx
00B960EF  E8 E8 2F 00 00                  call 0x140b990dc
00B960F4  4C 8B C8                        mov r9, rax
00B960F7  4C 8B C3                        mov r8, rbx
00B960FA  8B D7                           mov edx, edi
00B960FC  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00B96100  48 8B 81 A8 00 00 00            mov rax, qword ptr [rcx + 0xa8]
00B96107  49 8B C9                        mov rcx, r9
00B9610A  E8 C1 49 B2 FF                  call 0x1406baad0
00B9610F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00B96114  48 83 C4 20                     add rsp, 0x20
00B96118  5F                              pop rdi
00B96119  C3                              ret
00B9611A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfConfigureAdapterChannel(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ViGetRealDmaAdapter(a1, a2, a3, a4);
    result = guard_dispatch_icall(result, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, result);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfConfigureAdapterChannel(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ViGetRealDmaAdapter(Arg1, Arg2, Arg3, a4);
    result = guard_dispatch_icall(result, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, result);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B960E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B960E0[BB_00B960E0]
  bb_00B9611A[BB_00B9611A]
```
