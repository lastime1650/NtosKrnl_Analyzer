# PopRecordAcDcState

- RVA: `0x00AB96DC`–`0x00AB9720` (길이 `68` bytes)
- VA: `0x0000000140AB96DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `18`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00AB96EB` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AB9708` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (function, `0x004B27A0`)
- `0x00AB9714` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- [PopBatteryApplyCompositeState](../AE/PopBatteryApplyCompositeState_function_00AE0CD0.md) at `0x00AE0D43`

### Static image references
- `0x00AB96E4` → RVA `0x00F0F1E0` (`.data`; read)
- `0x00AB96F0` → RVA `0x00E6741F` (`.data`; read)
- `0x00AB9702` → RVA `0x00E6741F` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AB96EB` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AB9708` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (`PAGE` → `.text`)
  - `0x00AB9714` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB96DC  40 53                           push rbx
00AB96DE  48 83 EC 20                     sub rsp, 0x20
00AB96E2  8B D9                           mov ebx, ecx
00AB96E4  48 8D 0D F5 5A 45 00            lea rcx, [rip + 0x455af5]
00AB96EB  E8 54 74 97 FF                  call 0x140430b44
00AB96F0  8A 05 29 DD 3A 00               mov al, byte ptr [rip + 0x3add29]
00AB96F6  B9 01 00 00 00                  mov ecx, 1
00AB96FB  24 7F                           and al, 0x7f
00AB96FD  C0 E3 07                        shl bl, 7
00AB9700  0A C3                           or al, bl
00AB9702  88 05 17 DD 3A 00               mov byte ptr [rip + 0x3add17], al
00AB9708  E8 93 90 9F FF                  call 0x1404b27a0
00AB970D  48 8D 0D CC 5A 45 00            lea rcx, [rip + 0x455acc]
00AB9714  E8 A3 64 82 FF                  call 0x1402dfbbc
00AB9719  48 83 C4 20                     add rsp, 0x20
00AB971D  5B                              pop rbx
00AB971E  C3                              ret
00AB971F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopRecordAcDcState(int a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PopAcquireRwLockExclusive(v_rip + 4545269, a2, a3, a4);
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 3857705)) & (127));
    v_rbx = (unsigned __int8)(((unsigned int)(a1)) << (7));
    result = (unsigned __int8)((result) | ((unsigned __int8)(v_rbx)));
    *(unsigned __int8 *)(v_rip + 3857687) = (unsigned __int8)(result);
    result = PopBsdHandleRequest(1, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4545228, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopRecordAcDcState(int32_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PopAcquireRwLockExclusive(v_rip + 4545269, a2, a3, a4);
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x3ADD29)) & (127));
    local_rbx = (uint8_t)(((uint32_t)(Arg1)) << (7));
    result = (uint8_t)((result) | ((uint8_t)(local_rbx)));
    *(uint8_t *)(v_rip + 0x3ADD17) = (uint8_t)(result);
    result = PopBsdHandleRequest(1, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4545228, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB96DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB96DC[BB_00AB96DC]
  bb_00AB971F[BB_00AB971F]
```
