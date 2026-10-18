# IopWheaSelLogError

- RVA: `0x00596760`–`0x005967A4` (길이 `68` bytes)
- VA: `0x0000000140596760`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFA7C`
- 디코드: `17`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0059678C` → [WheaSelLogError](../65/WheaSelLogError_function_0065D8A8.md) (function, `0x0065D8A8`)
- `0x00596799` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00596764` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00596760  48 83 EC 48                     sub rsp, 0x48
00596764  48 8B 05 D5 3F 87 00            mov rax, qword ptr [rip + 0x873fd5]
0059676B  48 33 C4                        xor rax, rsp
0059676E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00596773  33 C0                           xor eax, eax
00596775  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0059677A  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
0059677F  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
00596784  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00596788  89 4C 24 26                     mov dword ptr [rsp + 0x26], ecx
0059678C  E8 17 71 0C 00                  call 0x14065d8a8
00596791  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00596796  48 33 CC                        xor rcx, rsp
00596799  E8 A2 5E 11 00                  call 0x1406ac640
0059679E  48 83 C4 48                     add rsp, 0x48
005967A2  C3                              ret
005967A3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopWheaSelLogError(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m22;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    result = (*(unsigned __int64 *)(v_rip + 8863701)) ^ (v_rsp);
    v_stack_m18 = result;
    result = 0;
    v_stack_m28 = 0;
    v_stack_m28 = a3;
    v_stack_m20 = 0;
    v_stack_m22 = a1;
    result = WheaSelLogError(a1, a2, v_stack_m28, a4);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m28, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopWheaSelLogError(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m22;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    result = (*(uint64_t *)(v_rip + 0x873FD5)) ^ (local_rsp);
    v_stack_m18 = result;
    result = 0;
    v_stack_m28 = 0;
    v_stack_m28 = Arg3;
    v_stack_m20 = 0;
    v_stack_m22 = Arg1;
    result = WheaSelLogError(Arg1, Arg2, v_stack_m28, a4);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m28, a4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00596760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00596760[BB_00596760]
  bb_005967A3[BB_005967A3]
```
