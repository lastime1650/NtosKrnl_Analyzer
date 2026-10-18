# ExpCrossVmWnfPush

- RVA: `0x00A85A14`–`0x00A85A9C` (길이 `136` bytes)
- VA: `0x0000000140A85A14`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008F464`
- 디코드: `38`개 명령, `136/136` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A85A44` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x00A85A8B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A85A95` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)

### Direct callers
- [ExpNtDeleteWnfStateData](../7C/ExpNtDeleteWnfStateData_function_007CF1A8.md) at `0x007CF33E`
- [ExpNtDeleteWnfStateData](../7C/ExpNtDeleteWnfStateData_function_007CF1A8.md) at `0x007CF4D6`

### Static image references
- `0x00A85A28` → RVA `0x00EFA120` (`.data`; read)
- `0x00A85A37` → RVA `0x00EFA118` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A85A44` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x00A85A8B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A85A95` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A85A14  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A85A19  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00A85A1E  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00A85A23  57                              push rdi
00A85A24  48 83 EC 40                     sub rsp, 0x40
00A85A28  48 8B 3D F1 46 47 00            mov rdi, qword ptr [rip + 0x4746f1]
00A85A2F  85 D2                           test edx, edx
00A85A31  41 8B F1                        mov esi, r9d
00A85A34  49 8B E8                        mov rbp, r8
00A85A37  48 0F 45 3D D9 46 47 00         cmovne rdi, qword ptr [rip + 0x4746d9]
00A85A3F  8B DA                           mov ebx, edx
00A85A41  48 8B CF                        mov rcx, rdi
00A85A44  E8 CB 2D 9A FF                  call 0x140428814
00A85A49  48 85 C0                        test rax, rax
00A85A4C  75 1D                           jne 0x140a85a6b
00A85A4E  BB 02 00 00 C0                  mov ebx, 0xc0000002
00A85A53  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00A85A58  8B C3                           mov eax, ebx
00A85A5A  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00A85A5F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00A85A64  48 83 C4 40                     add rsp, 0x40
00A85A68  5F                              pop rdi
00A85A69  C3                              ret
00A85A6A  CC                              int3
00A85A6B  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
00A85A6F  44 8B CE                        mov r9d, esi
00A85A72  48 8B 40 70                     mov rax, qword ptr [rax + 0x70]
00A85A76  4C 8B C5                        mov r8, rbp
00A85A79  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00A85A7D  33 C9                           xor ecx, ecx
00A85A7F  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00A85A84  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A85A89  8B D3                           mov edx, ebx
00A85A8B  E8 40 50 C3 FF                  call 0x1406baad0
00A85A90  8B D8                           mov ebx, eax
00A85A92  48 8B CF                        mov rcx, rdi
00A85A95  E8 26 13 9D FF                  call 0x140456dc0
00A85A9A  EB B7                           jmp 0x140a85a53
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpCrossVmWnfPush(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (64);
    v_rdi = *(unsigned __int64 *)(v_rip + 4671217);
    if (a2 != 0) { v_rdi = *(unsigned __int64 *)(v_rip + 4671193); }
    result = ExGetExtensionTable(v_rdi, a2, a3, a4);
    if (result != 0) goto loc_00A85A6B;
loc_00A85A53:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000002ULL)));
loc_00A85A6B:
    v_stack_p28 = (unsigned int)((unsigned int)(a6));
    a1 = 0;
    v_stack_p20 = a5;
    result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)(v_stack_p8)), v_stack_p10, (unsigned int)((unsigned int)(v_stack_p18)));
    result = ExReleaseExtensionTable(v_rdi, (unsigned int)((unsigned int)(v_stack_p8)), v_stack_p10, (unsigned int)((unsigned int)(v_stack_p18)));
    goto loc_00A85A53;
}
```

## 5. (Beta) C Style

```c
int64_t ExpCrossVmWnfPush(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (64);
    local_rdi = *(uint64_t *)(v_rip + 0x4746F1);
    if (Arg2 != 0) { local_rdi = *(uint64_t *)(v_rip + 0x4746D9); }
    result = ExGetExtensionTable(local_rdi, Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00A85A6B;
loc_00A85A53:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000002ULL)));
loc_00A85A6B:
    v_stack_p28 = (uint32_t)((uint32_t)(Arg6));
    Arg1 = 0;
    v_stack_p20 = Arg5;
    result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)(v_stack_p8)), v_stack_p10, (uint32_t)((uint32_t)(v_stack_p18)));
    result = ExReleaseExtensionTable(local_rdi, (uint32_t)((uint32_t)(v_stack_p8)), v_stack_p10, (uint32_t)((uint32_t)(v_stack_p18)));
    goto loc_00A85A53;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A85A14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A85A14[BB_00A85A14]
  bb_00A85A4E[BB_00A85A4E]
  bb_00A85A53[BB_00A85A53]
  bb_00A85A6A[BB_00A85A6A]
  bb_00A85A6B[BB_00A85A6B]
  bb_00A85A14 -->|branch| bb_00A85A6B
  bb_00A85A14 -->|fallthrough| bb_00A85A4E
  bb_00A85A4E -->|flow| bb_00A85A53
  bb_00A85A6A -->|flow| bb_00A85A6B
  bb_00A85A6B -->|branch| bb_00A85A53
```
