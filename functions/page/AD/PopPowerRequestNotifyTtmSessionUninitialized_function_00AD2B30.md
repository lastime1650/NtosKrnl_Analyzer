# PopPowerRequestNotifyTtmSessionUninitialized

- RVA: `0x00AD2B30`–`0x00AD2B76` (길이 `70` bytes)
- VA: `0x0000000140AD2B30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `17`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AD2B3B` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AD2B45` → [PopPowerRequestRevokeRequests](../../text/4C/PopPowerRequestRevokeRequests_function_004C0158.md) (function, `0x004C0158`)
- `0x00AD2B51` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00AD2B6B` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)

### Direct callers
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x0095755C`

### Static image references
- `0x00AD2B34` → RVA `0x00F0ED20` (`.data`; read)
- `0x00AD2B5C` → RVA `0x00E019D8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00AD2B3B` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AD2B45` → [PopPowerRequestRevokeRequests](../../text/4C/PopPowerRequestRevokeRequests_function_004C0158.md) (`PAGE` → `.text`)
  - `0x00AD2B51` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00AD2B6B` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD2B30  48 83 EC 38                     sub rsp, 0x38
00AD2B34  48 8D 0D E5 C1 43 00            lea rcx, [rip + 0x43c1e5]
00AD2B3B  E8 04 E0 95 FF                  call 0x140430b44
00AD2B40  33 D2                           xor edx, edx
00AD2B42  8D 4A 01                        lea ecx, [rdx + 1]
00AD2B45  E8 0E D6 9E FF                  call 0x1404c0158
00AD2B4A  48 8D 0D CF C1 43 00            lea rcx, [rip + 0x43c1cf]
00AD2B51  E8 66 D0 80 FF                  call 0x1402dfbbc
00AD2B56  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00AD2B5C  48 8D 0D 75 EE 32 00            lea rcx, [rip + 0x32ee75]
00AD2B63  45 33 C9                        xor r9d, r9d
00AD2B66  45 33 C0                        xor r8d, r8d
00AD2B69  33 D2                           xor edx, edx
00AD2B6B  E8 40 BB 73 FF                  call 0x14020e6b0
00AD2B70  48 83 C4 38                     add rsp, 0x38
00AD2B74  C3                              ret
00AD2B75  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerRequestNotifyTtmSessionUninitialized(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = PopAcquireRwLockExclusive(v_rip + 4440549, a2, a3, a4);
    a2 = 0;
    result = PopPowerRequestRevokeRequests(a2 + 1, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4440527, a2, a3, a4);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 3337845, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerRequestNotifyTtmSessionUninitialized(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = PopAcquireRwLockExclusive(v_rip + 4440549, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = PopPowerRequestRevokeRequests(Arg2 + 1, Arg2, Arg3, Arg4);
    result = PopReleaseRwLock(v_rip + 4440527, Arg2, Arg3, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 3337845, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD2B30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AD2B30[BB_00AD2B30]
  bb_00AD2B75[BB_00AD2B75]
```
