# KeGenericCallDpc

- RVA: `0x0049F980`–`0x0049F9D2` (길이 `82` bytes)
- VA: `0x000000014049F980`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A3E54`
- 디코드: `21`개 명령, `82/82` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0049F9BA` → [KeGenericProcessorCallback](../39/KeGenericProcessorCallback_function_00398C2C.md) (function, `0x00398C2C`)
- `0x0049F9CB` → [KiCpuPartitionCheckGenericDpc](../5C/KiCpuPartitionCheckGenericDpc_function_005C159C.md) (function, `0x005C159C`)

### Direct callers
- [MiDbgCopyMemory](../68/MiDbgCopyMemory_function_00684A18.md) at `0x00684BCC`
- [MiApplyImageHotPatch](../../page/80/MiApplyImageHotPatch_function_00802330.md) at `0x00802475`
- [EtwpFreeLoggerContext](../../page/9C/EtwpFreeLoggerContext_function_009C1688.md) at `0x009C172E`
- [EtwpUpdateGuidFilterData](../../page/9F/EtwpUpdateGuidFilterData_function_009FD214.md) at `0x009FD525`
- [KiInitializeDynamicProcessor](../../pagelk/B6/KiInitializeDynamicProcessor_function_00B679C8.md) at `0x00B679EB`

### Static image references
- `0x0049F98A` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0049F9B1` → RVA `0x002C9B60` (`KiGenericCallDpcInitiatorWorker`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049F980  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0049F985  57                              push rdi
0049F986  48 83 EC 30                     sub rsp, 0x30
0049F98A  F7 05 80 71 B2 00 00 02 00 00   test dword ptr [rip + 0xb27180], 0x200
0049F994  48 8B FA                        mov rdi, rdx
0049F997  48 8B D9                        mov rbx, rcx
0049F99A  75 2F                           jne 0x14049f9cb
0049F99C  41 B9 01 00 00 00               mov r9d, 1
0049F9A2  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0049F9A7  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
0049F9AC  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0049F9B1  48 8D 15 A8 A1 E2 FF            lea rdx, [rip - 0x1d5e58]
0049F9B8  33 C9                           xor ecx, ecx
0049F9BA  E8 6D 92 EF FF                  call 0x140398c2c
0049F9BF  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0049F9C4  48 83 C4 30                     add rsp, 0x30
0049F9C8  5F                              pop rdi
0049F9C9  C3                              ret
0049F9CA  CC                              int3
0049F9CB  E8 CC 1B 12 00                  call 0x1405c159c
0049F9D0  EB CA                           jmp 0x14049f99c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeGenericCallDpc(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    if (((*(unsigned int *)(v_rip + 11694464)) & (512)) != 0) goto loc_0049F9CB;
loc_0049F99C:
    v_stack_m18 = a1;
    v_stack_m10 = a2;
    a1 = 0;
    result = KeGenericProcessorCallback(a1, v_rip - 1924696, v_stack_m18, 1);
    v_rsp = (v_rsp) + (48);
    return result;
loc_0049F9CB:
    result = KiCpuPartitionCheckGenericDpc(a1, v_rip - 1924696, v_stack_m18, 1);
    goto loc_0049F99C;
}
```

## 5. (Beta) C Style

```c
int64_t KeGenericCallDpc(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    if (((*(uint32_t *)(v_rip + 0xB27180)) & (512)) != 0) goto loc_0049F9CB;
loc_0049F99C:
    v_stack_m18 = Arg1;
    v_stack_m10 = Arg2;
    Arg1 = 0;
    result = KeGenericProcessorCallback(Arg1, v_rip - 1924696, v_stack_m18, 1);
    local_rsp = (local_rsp) + (48);
    return result;
loc_0049F9CB:
    result = KiCpuPartitionCheckGenericDpc(Arg1, v_rip - 1924696, v_stack_m18, 1);
    goto loc_0049F99C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049F980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049F980[BB_0049F980]
  bb_0049F99C[BB_0049F99C]
  bb_0049F9CA[BB_0049F9CA]
  bb_0049F9CB[BB_0049F9CB]
  bb_0049F980 -->|branch| bb_0049F9CB
  bb_0049F980 -->|fallthrough| bb_0049F99C
  bb_0049F9CA -->|flow| bb_0049F9CB
  bb_0049F9CB -->|branch| bb_0049F99C
```
