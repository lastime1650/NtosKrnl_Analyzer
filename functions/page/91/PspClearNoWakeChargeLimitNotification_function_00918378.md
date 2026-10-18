# PspClearNoWakeChargeLimitNotification

- RVA: `0x00918378`–`0x009183D4` (길이 `92` bytes)
- VA: `0x0000000140918378`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008AB40`
- 디코드: `20`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009183B4` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x009183C5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [PspEnforceLimits](PspEnforceLimits_function_00919FC0.md) at `0x00919FFB`

### Static image references
- `0x0091837C` → RVA `0x00FD9DA0` (`PAGEDATA`; read)
- `0x0091839B` → RVA `0x00020BA0` (`.rdata`; read)
- `0x009183CA` → RVA `0x00FD9DA0` (`PAGEDATA`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009183B4` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x009183C5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00918378  48 83 EC 48                     sub rsp, 0x48
0091837C  48 83 3D 1C 1A 6C 00 00         cmp qword ptr [rip + 0x6c1a1c], 0
00918384  75 06                           jne 0x14091838c
00918386  48 83 C4 48                     add rsp, 0x48
0091838A  C3                              ret
0091838B  CC                              int3
0091838C  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
00918391  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00918396  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
0091839B  48 8D 0D FE 87 70 FF            lea rcx, [rip - 0x8f7802]
009183A2  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
009183A7  45 33 C9                        xor r9d, r9d
009183AA  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
009183B0  45 8D 41 04                     lea r8d, [r9 + 4]
009183B4  E8 57 89 D9 FF                  call 0x1406b0d10
009183B9  48 8B 0D E0 19 6C 00            mov rcx, qword ptr [rip + 0x6c19e0]
009183C0  BA 50 73 4A 62                  mov edx, 0x624a7350
009183C5  E8 16 F5 9D FF                  call 0x1402f78e0
009183CA  48 83 25 CE 19 6C 00 00         and qword ptr [rip + 0x6c19ce], 0
009183D2  EB B2                           jmp 0x140918386
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspClearNoWakeChargeLimitNotification(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p50;

    v_rsp = (v_rsp) - (72);
    if ((*(unsigned __int64 *)(v_rip + 7084572)) != 0) goto loc_0091838C;
loc_00918386:
    v_rsp = (v_rsp) + (72);
    return result;
loc_0091838C:
    a4 = 0;
    result = ZwUpdateWnfStateData(v_rip - 9402370, v_stack_p50, a4 + 4, a4);
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_rip + 7084512), (unsigned int)(0x624A7350ULL), a4 + 4, a4);
    goto loc_00918386;
}
```

## 5. (Beta) C Style

```c
int64_t PspClearNoWakeChargeLimitNotification(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p50;

    local_rsp = (local_rsp) - (72);
    if ((*(uint64_t *)(v_rip + 0x6C1A1C)) != 0) goto loc_0091838C;
loc_00918386:
    local_rsp = (local_rsp) + (72);
    return result;
loc_0091838C:
    Arg4 = 0;
    result = ZwUpdateWnfStateData(v_rip - 9402370, v_stack_p50, Arg4 + 4, Arg4);
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_rip + 0x6C19E0), (uint32_t)(0x624A7350ULL), Arg4 + 4, Arg4);
    goto loc_00918386;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00918378&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00918378[BB_00918378]
  bb_00918386[BB_00918386]
  bb_0091838B[BB_0091838B]
  bb_0091838C[BB_0091838C]
  bb_00918378 -->|branch| bb_0091838C
  bb_00918378 -->|fallthrough| bb_00918386
  bb_0091838B -->|flow| bb_0091838C
  bb_0091838C -->|branch| bb_00918386
```
