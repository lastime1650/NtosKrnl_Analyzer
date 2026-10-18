# PerfInfoLogUnexpectedInterrupt

- RVA: `0x006513E0`–`0x00651444` (길이 `100` bytes)
- VA: `0x00000001406513E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD25C`
- 디코드: `21`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0065142C` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00651439` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KxIsrLinkage](../6B/KxIsrLinkage_function_006B5680.md) at `0x006B5A4E`

### Static image references
- `0x006513E8` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006513E0  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
006513E4  48 83 EC 58                     sub rsp, 0x58
006513E8  48 8B 05 51 93 7B 00            mov rax, qword ptr [rip + 0x7b9351]
006513EF  48 33 C4                        xor rax, rsp
006513F2  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
006513F7  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
006513FC  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00651401  41 B9 5C 0F 00 00               mov r9d, 0xf5c
00651407  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0065140C  BA 01 00 00 00                  mov edx, 1
00651411  C7 44 24 38 02 00 00 00         mov dword ptr [rsp + 0x38], 2
00651419  41 B8 00 40 00 20               mov r8d, 0x20004000
0065141F  C7 44 24 20 02 0A 50 00         mov dword ptr [rsp + 0x20], 0x500a02
00651427  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0065142C  E8 1F 3F BE FF                  call 0x140235350
00651431  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00651436  48 33 CC                        xor rcx, rsp
00651439  E8 02 B2 05 00                  call 0x1406ac640
0065143E  48 83 C4 58                     add rsp, 0x58
00651442  C3                              ret
00651443  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PerfInfoLogUnexpectedInterrupt(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m38;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 8098641)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_stack_p8;
    v_stack_m20 = 2;
    v_stack_m38 = 0x500A02ULL;
    result = EtwTraceKernelEvent(v_stack_m28, 1, (unsigned int)(0x20004000ULL), (unsigned int)(0xF5CULL));
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0x20004000ULL), (unsigned int)(0xF5CULL));
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PerfInfoLogUnexpectedInterrupt(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m38;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x7B9351)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_stack_p8;
    v_stack_m20 = 2;
    v_stack_m38 = 0x500A02ULL;
    result = EtwTraceKernelEvent(v_stack_m28, 1, (uint32_t)(0x20004000ULL), (uint32_t)(0xF5CULL));
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0x20004000ULL), (uint32_t)(0xF5CULL));
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006513E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006513E0[BB_006513E0]
  bb_00651443[BB_00651443]
```
