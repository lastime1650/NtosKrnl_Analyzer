# VerifierZwCreateKey

- RVA: `0x00BB2A80`–`0x00BB2AB7` (길이 `55` bytes)
- VA: `0x0000000140BB2A80`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `12`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BB2AAC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BB2A8C` → RVA `0x00FFE000` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BB2AAC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB2A80  48 83 EC 48                     sub rsp, 0x48
00BB2A84  4C 8B 94 24 80 00 00 00         mov r10, qword ptr [rsp + 0x80]
00BB2A8C  48 8B 05 6D B5 44 00            mov rax, qword ptr [rip + 0x44b56d]
00BB2A93  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00BB2A98  44 8B 54 24 78                  mov r10d, dword ptr [rsp + 0x78]
00BB2A9D  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
00BB2AA2  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
00BB2AA7  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00BB2AAC  E8 1F 80 B0 FF                  call 0x1406baad0
00BB2AB1  48 83 C4 48                     add rsp, 0x48
00BB2AB5  C3                              ret
00BB2AB6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierZwCreateKey(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = a7;
    v_stack_m20 = (unsigned int)((unsigned int)(a6));
    v_stack_m28 = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierZwCreateKey(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = Arg7;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m28 = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB2A80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB2A80[BB_00BB2A80]
  bb_00BB2AB6[BB_00BB2AB6]
```
