# PcwAddInstance

- RVA: `0x00A0E530`–`0x00A0E5AF` (길이 `127` bytes)
- VA: `0x0000000140A0E530`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000898D0`
- 디코드: `35`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A0E557` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x00A0E57B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A0E589` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)
- `0x00A0E5A6` → [ExpPcwDisabledStatus](../A6/ExpPcwDisabledStatus_function_00A611E0.md) (function, `0x00A611E0`)

### Direct callers
- [EtwpEventTracingCounterSetCallback](EtwpEventTracingCounterSetCallback_function_00A0E0C0.md) at `0x00A0E30E`
- [PoThermalCounterSetCallback](PoThermalCounterSetCallback_function_00A0E350.md) at `0x00A0E4DE`
- [FsRtlDiskIOCounterSetCallback](../A6/FsRtlDiskIOCounterSetCallback_function_00A61540.md) at `0x00A615A9`
- [sub_00B41970](../B4/Unknown_function_00B41970.md) at `0x00B419CB`

### Static image references
- `0x00A0E54A` → RVA `0x00FD8080` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A0E557` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x00A0E57B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A0E589` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A0E530  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A0E535  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00A0E53A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00A0E53F  57                              push rdi
00A0E540  48 83 EC 30                     sub rsp, 0x30
00A0E544  48 8B E9                        mov rbp, rcx
00A0E547  41 8B D9                        mov ebx, r9d
00A0E54A  48 8B 0D 2F 9B 5C 00            mov rcx, qword ptr [rip + 0x5c9b2f]
00A0E551  41 8B F8                        mov edi, r8d
00A0E554  48 8B F2                        mov rsi, rdx
00A0E557  E8 B8 A2 A1 FF                  call 0x140428814
00A0E55C  48 85 C0                        test rax, rax
00A0E55F  74 45                           je 0x140a0e5a6
00A0E561  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00A0E566  44 8B CB                        mov r9d, ebx
00A0E569  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00A0E56D  44 8B C7                        mov r8d, edi
00A0E570  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A0E575  48 8B D6                        mov rdx, rsi
00A0E578  48 8B CD                        mov rcx, rbp
00A0E57B  E8 50 C5 CA FF                  call 0x1406baad0
00A0E580  48 8B 0D F9 9A 5C 00            mov rcx, qword ptr [rip + 0x5c9af9]
00A0E587  8B D8                           mov ebx, eax
00A0E589  E8 32 88 A4 FF                  call 0x140456dc0
00A0E58E  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00A0E593  8B C3                           mov eax, ebx
00A0E595  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A0E59A  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00A0E59F  48 83 C4 30                     add rsp, 0x30
00A0E5A3  5F                              pop rdi
00A0E5A4  C3                              ret
00A0E5A5  CC                              int3
00A0E5A6  E8 35 2C 05 00                  call 0x140a611e0
00A0E5AB  8B D8                           mov ebx, eax
00A0E5AD  EB DF                           jmp 0x140a0e58e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PcwAddInstance(__int64 a1, __int64 a2, int a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    result = ExGetExtensionTable(*(unsigned __int64 *)(v_rip + 6069039), a2, a3, a4);
    if (result == 0) goto loc_00A0E5A6;
    v_stack_m18 = a5;
    result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    result = ExReleaseExtensionTable(*(unsigned __int64 *)(v_rip + 6068985), a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
loc_00A0E58E:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A0E5A6:
    result = ExpPcwDisabledStatus(*(unsigned __int64 *)(v_rip + 6068985), a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    goto loc_00A0E58E;
}
```

## 5. (Beta) C Style

```c
int64_t PcwAddInstance(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    result = ExGetExtensionTable(*(uint64_t *)(v_rip + 0x5C9B2F), Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00A0E5A6;
    v_stack_m18 = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    result = ExReleaseExtensionTable(*(uint64_t *)(v_rip + 0x5C9AF9), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
loc_00A0E58E:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A0E5A6:
    result = ExpPcwDisabledStatus(*(uint64_t *)(v_rip + 0x5C9AF9), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    goto loc_00A0E58E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0E530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A0E530[BB_00A0E530]
  bb_00A0E561[BB_00A0E561]
  bb_00A0E58E[BB_00A0E58E]
  bb_00A0E5A5[BB_00A0E5A5]
  bb_00A0E5A6[BB_00A0E5A6]
  bb_00A0E530 -->|branch| bb_00A0E5A6
  bb_00A0E530 -->|fallthrough| bb_00A0E561
  bb_00A0E561 -->|flow| bb_00A0E58E
  bb_00A0E5A5 -->|flow| bb_00A0E5A6
  bb_00A0E5A6 -->|branch| bb_00A0E58E
```
