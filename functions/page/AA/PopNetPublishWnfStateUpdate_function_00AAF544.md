# PopNetPublishWnfStateUpdate

- RVA: `0x00AAF544`–`0x00AAF59D` (길이 `89` bytes)
- VA: `0x0000000140AAF544`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC3DC`
- 디코드: `24`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AAF586` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)

### Direct callers
- [PopNetEvaluationWorkerCallback](../../text/4B/PopNetEvaluationWorkerCallback_function_004BE0B0.md) at `0x004BE120`
- [PopNetInitialize](../../init/C4/PopNetInitialize_function_00C423AC.md) at `0x00C42514`

### Static image references
- `0x00AAF566` → RVA `0x0001E130` (`.rdata`; read)
- `0x00AAF58B` → RVA `0x00F0887D` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AAF586` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAF544  48 83 EC 48                     sub rsp, 0x48
00AAF548  33 D2                           xor edx, edx
00AAF54A  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
00AAF54F  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00AAF553  83 4C 24 5C FF                  or dword ptr [rsp + 0x5c], 0xffffffff
00AAF558  83 C8 01                        or eax, 1
00AAF55B  84 C9                           test cl, cl
00AAF55D  74 39                           je 0x140aaf598
00AAF55F  83 C8 02                        or eax, 2
00AAF562  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00AAF566  48 8D 0D C3 EB 56 FF            lea rcx, [rip - 0xa9143d]
00AAF56D  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00AAF571  45 33 C9                        xor r9d, r9d
00AAF574  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00AAF579  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00AAF57E  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AAF582  45 8D 41 08                     lea r8d, [r9 + 8]
00AAF586  E8 85 17 C0 FF                  call 0x1406b0d10
00AAF58B  C6 05 EB 92 45 00 01            mov byte ptr [rip + 0x4592eb], 1
00AAF592  48 83 C4 48                     add rsp, 0x48
00AAF596  C3                              ret
00AAF597  CC                              int3
00AAF598  83 E0 FD                        and eax, 0xfffffffd
00AAF59B  EB C5                           jmp 0x140aaf562
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopNetPublishWnfStateUpdate(unsigned __int8 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p14;

    v_rsp = (v_rsp) - (72);
    a2 = 0;
    v_stack_p10 = 0;
    result = (unsigned int)(((unsigned int)(v_stack_p10)) | (1));
    if (a1 == 0) goto loc_00AAF598;
    result = (unsigned int)((result) | (2));
loc_00AAF562:
    v_stack_m18 = 0;
    v_stack_m20 = 0;
    a4 = 0;
    v_stack_m28 = 0;
    v_stack_p10 = (unsigned int)(result);
    result = ZwUpdateWnfStateData(v_rip - 11080765, v_stack_p10, a4 + 8, a4);
    *(unsigned __int8 *)(v_rip + 4559595) = 1;
    v_rsp = (v_rsp) + (72);
    return result;
loc_00AAF598:
    result = (unsigned int)((result) & (0xFFFFFFFDULL));
    goto loc_00AAF562;
}
```

## 5. (Beta) C Style

```c
int64_t PopNetPublishWnfStateUpdate(uint8_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint32_t v_stack_p14;

    local_rsp = (local_rsp) - (72);
    Arg2 = 0;
    v_stack_p10 = 0;
    result = (uint32_t)(((uint32_t)(v_stack_p10)) | (1));
    if (Arg1 == 0) goto loc_00AAF598;
    result = (uint32_t)((result) | (2));
loc_00AAF562:
    v_stack_m18 = 0;
    v_stack_m20 = 0;
    Arg4 = 0;
    v_stack_m28 = 0;
    v_stack_p10 = (uint32_t)(result);
    result = ZwUpdateWnfStateData(v_rip - 11080765, v_stack_p10, Arg4 + 8, Arg4);
    *(uint8_t *)(v_rip + 0x4592EB) = 1;
    local_rsp = (local_rsp) + (72);
    return result;
loc_00AAF598:
    result = (uint32_t)((result) & (0xFFFFFFFDULL));
    goto loc_00AAF562;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAF544&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AAF544[BB_00AAF544]
  bb_00AAF55F[BB_00AAF55F]
  bb_00AAF562[BB_00AAF562]
  bb_00AAF597[BB_00AAF597]
  bb_00AAF598[BB_00AAF598]
  bb_00AAF544 -->|branch| bb_00AAF598
  bb_00AAF544 -->|fallthrough| bb_00AAF55F
  bb_00AAF55F -->|flow| bb_00AAF562
  bb_00AAF597 -->|flow| bb_00AAF598
  bb_00AAF598 -->|branch| bb_00AAF562
```
