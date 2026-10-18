# PopPowerRequestHandleExecutionEnablementUpdate

- RVA: `0x00A4A624`–`0x00A4A65C` (길이 `56` bytes)
- VA: `0x0000000140A4A624`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `16`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A4A63C` → [PopPowerRequestEvaluateExecutionRequiredStatus](PopPowerRequestEvaluateExecutionRequiredStatus_function_00A4A664.md) (function, `0x00A4A664`)
- `0x00A4A64A` → [PopPowerRequestRevokeRequests](../../text/4C/PopPowerRequestRevokeRequests_function_004C0158.md) (function, `0x004C0158`)
- `0x00A4A655` → [PopPowerRequestUnrevokeRequests](../../text/4B/PopPowerRequestUnrevokeRequests_function_004BF3D0.md) (function, `0x004BF3D0`)

### Direct callers
- [PopPowerRequestExecutionRequiredTimeoutWorker](../75/PopPowerRequestExecutionRequiredTimeoutWorker_function_00754AF0.md) at `0x00754AFB`
- [PopPowerRequestNotifyMobileHotspotChanged](../75/PopPowerRequestNotifyMobileHotspotChanged_function_00754BBC.md) at `0x00754BE5`
- [PopWnfAudioCallback](PopWnfAudioCallback_function_00A4A0E0.md) at `0x00A4A1B1`
- [PopPowerRequestExecutionRequiredSettingCallback](../AC/PopPowerRequestExecutionRequiredSettingCallback_function_00AC4EB0.md) at `0x00AC4F1F`
- [sub_00B39B90](../B3/Unknown_function_00B39B90.md) at `0x00B39BA5`

### Static image references
- `0x00A4A628` → RVA `0x00FD8114` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A4A64A` → [PopPowerRequestRevokeRequests](../../text/4C/PopPowerRequestRevokeRequests_function_004C0158.md) (`PAGE` → `.text`)
  - `0x00A4A655` → [PopPowerRequestUnrevokeRequests](../../text/4B/PopPowerRequestUnrevokeRequests_function_004BF3D0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4A624  48 83 EC 28                     sub rsp, 0x28
00A4A628  83 3D E5 DA 58 00 00            cmp dword ptr [rip + 0x58dae5], 0
00A4A62F  B8 0A 00 00 00                  mov eax, 0xa
00A4A634  44 8D 48 FE                     lea r9d, [rax - 2]
00A4A638  44 0F 45 C8                     cmovne r9d, eax
00A4A63C  E8 23 00 00 00                  call 0x140a4a664
00A4A641  41 8B C9                        mov ecx, r9d
00A4A644  84 C0                           test al, al
00A4A646  75 0D                           jne 0x140a4a655
00A4A648  33 D2                           xor edx, edx
00A4A64A  E8 09 5B A7 FF                  call 0x1404c0158
00A4A64F  48 83 C4 28                     add rsp, 0x28
00A4A653  C3                              ret
00A4A654  CC                              int3
00A4A655  E8 76 4D A7 FF                  call 0x1404bf3d0
00A4A65A  EB F3                           jmp 0x140a4a64f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerRequestHandleExecutionEnablementUpdate(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 10 - 2;
    if ((*(unsigned int *)(v_rip + 5823205)) != 0) { a4 = 10; }
    result = PopPowerRequestEvaluateExecutionRequiredStatus(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A4A655;
    a2 = 0;
    result = PopPowerRequestRevokeRequests((unsigned int)((unsigned int)(a4)), a2, a3, a4);
loc_00A4A64F:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A4A655:
    result = PopPowerRequestUnrevokeRequests((unsigned int)((unsigned int)(a4)), a2, a3, a4);
    goto loc_00A4A64F;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerRequestHandleExecutionEnablementUpdate(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    a4 = 10 - 2;
    if ((*(uint32_t *)(v_rip + 0x58DAE5)) != 0) { a4 = 10; }
    result = PopPowerRequestEvaluateExecutionRequiredStatus(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00A4A655;
    Arg2 = 0;
    result = PopPowerRequestRevokeRequests((uint32_t)((uint32_t)(a4)), Arg2, a3, a4);
loc_00A4A64F:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A4A655:
    result = PopPowerRequestUnrevokeRequests((uint32_t)((uint32_t)(a4)), Arg2, a3, a4);
    goto loc_00A4A64F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4A624&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4A624[BB_00A4A624]
  bb_00A4A648[BB_00A4A648]
  bb_00A4A64F[BB_00A4A64F]
  bb_00A4A654[BB_00A4A654]
  bb_00A4A655[BB_00A4A655]
  bb_00A4A624 -->|branch| bb_00A4A655
  bb_00A4A624 -->|fallthrough| bb_00A4A648
  bb_00A4A648 -->|flow| bb_00A4A64F
  bb_00A4A654 -->|flow| bb_00A4A655
  bb_00A4A655 -->|branch| bb_00A4A64F
```
