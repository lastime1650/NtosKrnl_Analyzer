# PopSetSleepMarker

- RVA: `0x00AA86FC`–`0x00AA8782` (길이 `134` bytes)
- VA: `0x0000000140AA86FC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `34`개 명령, `134/134` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00AA8708` → [PopGetTransitionsToOnCount](../../text/42/PopGetTransitionsToOnCount_function_0042FDE0.md) (function, `0x0042FDE0`)
- `0x00AA871D` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AA875C` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (function, `0x004B27A0`)
- `0x00AA8768` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00AA8779` → [PopGetTransitionsToOnCount](../../text/42/PopGetTransitionsToOnCount_function_0042FDE0.md) (function, `0x0042FDE0`)

### Direct callers
- [PopIssueActionRequest](../A9/PopIssueActionRequest_function_00A9CE54.md) at `0x00A9D0A4`
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7ED6E`

### Static image references
- `0x00AA8716` → RVA `0x00F0F1E0` (`.data`; read)
- `0x00AA8722` → RVA `0x00F0C2E8` (`.data`; read)
- `0x00AA872D` → RVA `0x00E67418` (`.data`; read)
- `0x00AA873F` → RVA `0x00E6741C` (`.data`; write)
- `0x00AA8746` → RVA `0x00E67418` (`.data`; write)
- `0x00AA874C` → RVA `0x00E6741E` (`.data`; read)
- `0x00AA8756` → RVA `0x00E6741E` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00AA8708` → [PopGetTransitionsToOnCount](../../text/42/PopGetTransitionsToOnCount_function_0042FDE0.md) (`PAGE` → `.text`)
  - `0x00AA871D` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AA875C` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (`PAGE` → `.text`)
  - `0x00AA8768` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00AA8779` → [PopGetTransitionsToOnCount](../../text/42/PopGetTransitionsToOnCount_function_0042FDE0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA86FC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AA8701  57                              push rdi
00AA8702  48 83 EC 20                     sub rsp, 0x20
00AA8706  8B F9                           mov edi, ecx
00AA8708  E8 D3 76 98 FF                  call 0x14042fde0
00AA870D  BB FF FF 00 00                  mov ebx, 0xffff
00AA8712  3B C3                           cmp eax, ebx
00AA8714  72 63                           jb 0x140aa8779
00AA8716  48 8D 0D C3 6A 46 00            lea rcx, [rip + 0x466ac3]
00AA871D  E8 22 84 98 FF                  call 0x140430b44
00AA8722  8B 15 C0 3B 46 00               mov edx, dword ptr [rip + 0x463bc0]
00AA8728  B9 09 00 00 00                  mov ecx, 9
00AA872D  8A 05 E5 EC 3B 00               mov al, byte ptr [rip + 0x3bece5]
00AA8733  80 E2 0F                        and dl, 0xf
00AA8736  24 0F                           and al, 0xf
00AA8738  40 C0 E7 04                     shl dil, 4
00AA873C  40 0A C7                        or al, dil
00AA873F  66 89 1D D6 EC 3B 00            mov word ptr [rip + 0x3becd6], bx
00AA8746  88 05 CC EC 3B 00               mov byte ptr [rip + 0x3beccc], al
00AA874C  8A 05 CC EC 3B 00               mov al, byte ptr [rip + 0x3beccc]
00AA8752  24 F0                           and al, 0xf0
00AA8754  0A C2                           or al, dl
00AA8756  88 05 C2 EC 3B 00               mov byte ptr [rip + 0x3becc2], al
00AA875C  E8 3F A0 A0 FF                  call 0x1404b27a0
00AA8761  48 8D 0D 78 6A 46 00            lea rcx, [rip + 0x466a78]
00AA8768  E8 4F 74 83 FF                  call 0x1402dfbbc
00AA876D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00AA8772  48 83 C4 20                     add rsp, 0x20
00AA8776  5F                              pop rdi
00AA8777  C3                              ret
00AA8778  CC                              int3
00AA8779  E8 62 76 98 FF                  call 0x14042fde0
00AA877E  8B D8                           mov ebx, eax
00AA8780  EB 94                           jmp 0x140aa8716
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSetSleepMarker(int a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = PopGetTransitionsToOnCount(a1, a2, a3, a4);
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_00AA8779;
loc_00AA8716:
    result = PopAcquireRwLockExclusive(v_rip + 4614851, a2, a3, a4);
    a2 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rip + 4602816))) & (15));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 3927269)) & (15));
    v_rdi = (unsigned __int8)(((unsigned int)(a1)) << (4));
    result = (unsigned __int8)((result) | ((unsigned __int8)(v_rdi)));
    *(unsigned __int16 *)(v_rip + 3927254) = (unsigned __int16)((unsigned int)(0xFFFFULL));
    *(unsigned __int8 *)(v_rip + 3927244) = (unsigned __int8)(result);
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 3927244)) & (240));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a2)));
    *(unsigned __int8 *)(v_rip + 3927234) = (unsigned __int8)(result);
    result = PopBsdHandleRequest(9, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4614776, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00AA8779:
    result = PopGetTransitionsToOnCount(v_rip + 4614776, a2, a3, a4);
    goto loc_00AA8716;
}
```

## 5. (Beta) C Style

```c
int64_t PopSetSleepMarker(int32_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = PopGetTransitionsToOnCount(Arg1, a2, a3, a4);
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_00AA8779;
loc_00AA8716:
    result = PopAcquireRwLockExclusive(v_rip + 4614851, a2, a3, a4);
    a2 = (uint8_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x463BC0))) & (15));
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x3BECE5)) & (15));
    local_rdi = (uint8_t)(((uint32_t)(Arg1)) << (4));
    result = (uint8_t)((result) | ((uint8_t)(local_rdi)));
    *(uint16_t *)(v_rip + 0x3BECD6) = (uint16_t)((uint32_t)(0xFFFFULL));
    *(uint8_t *)(v_rip + 0x3BECCC) = (uint8_t)(result);
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x3BECCC)) & (240));
    result = (uint8_t)((result) | ((uint8_t)(a2)));
    *(uint8_t *)(v_rip + 0x3BECC2) = (uint8_t)(result);
    result = PopBsdHandleRequest(9, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4614776, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00AA8779:
    result = PopGetTransitionsToOnCount(v_rip + 4614776, a2, a3, a4);
    goto loc_00AA8716;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA86FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA86FC[BB_00AA86FC]
  bb_00AA8716[BB_00AA8716]
  bb_00AA8778[BB_00AA8778]
  bb_00AA8779[BB_00AA8779]
  bb_00AA86FC -->|branch| bb_00AA8779
  bb_00AA86FC -->|fallthrough| bb_00AA8716
  bb_00AA8778 -->|flow| bb_00AA8779
  bb_00AA8779 -->|branch| bb_00AA8716
```
