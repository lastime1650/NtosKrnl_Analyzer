# PopRecordSleepCheckpointSource

- RVA: `0x007545F4`–`0x0075463B` (길이 `71` bytes)
- VA: `0x00000001407545F4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `19`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00754603` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00754623` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (function, `0x004B27A0`)
- `0x0075462F` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- [PopCheckShutdownMarker](../../init/C3/PopCheckShutdownMarker_function_00C3DAD4.md) at `0x00C3DF61`
- [PopCheckShutdownMarker](../../init/C3/PopCheckShutdownMarker_function_00C3DAD4.md) at `0x00C3DF8D`

### Static image references
- `0x007545FC` → RVA `0x00F0F1E0` (`.data`; read)
- `0x00754608` → RVA `0x00E673F1` (`.data`; read)
- `0x0075461D` → RVA `0x00E673F1` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00754603` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00754623` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (`PAGE` → `.text`)
  - `0x0075462F` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007545F4  40 53                           push rbx
007545F6  48 83 EC 20                     sub rsp, 0x20
007545FA  8B D9                           mov ebx, ecx
007545FC  48 8D 0D DD AB 7B 00            lea rcx, [rip + 0x7babdd]
00754603  E8 3C C5 CD FF                  call 0x140430b44
00754608  8A 05 E3 2D 71 00               mov al, byte ptr [rip + 0x712de3]
0075460E  80 E3 03                        and bl, 3
00754611  24 F3                           and al, 0xf3
00754613  C0 E3 02                        shl bl, 2
00754616  0A D8                           or bl, al
00754618  B9 0A 00 00 00                  mov ecx, 0xa
0075461D  88 1D CE 2D 71 00               mov byte ptr [rip + 0x712dce], bl
00754623  E8 78 E1 D5 FF                  call 0x1404b27a0
00754628  48 8D 0D B1 AB 7B 00            lea rcx, [rip + 0x7babb1]
0075462F  E8 88 B5 B8 FF                  call 0x1402dfbbc
00754634  48 83 C4 20                     add rsp, 0x20
00754638  5B                              pop rbx
00754639  C3                              ret
0075463A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopRecordSleepCheckpointSource(int a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PopAcquireRwLockExclusive(v_rip + 8104925, a2, a3, a4);
    v_rbx = (unsigned __int8)(((unsigned int)(a1)) & (3));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 7417315)) & (243));
    v_rbx = (unsigned __int8)((v_rbx) << (2));
    v_rbx = (unsigned __int8)((v_rbx) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_rip + 7417294) = (unsigned __int8)(v_rbx);
    result = PopBsdHandleRequest(10, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 8104881, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopRecordSleepCheckpointSource(int32_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PopAcquireRwLockExclusive(v_rip + 8104925, a2, a3, a4);
    local_rbx = (uint8_t)(((uint32_t)(Arg1)) & (3));
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x712DE3)) & (243));
    local_rbx = (uint8_t)((local_rbx) << (2));
    local_rbx = (uint8_t)((local_rbx) | ((uint8_t)(result)));
    *(uint8_t *)(v_rip + 0x712DCE) = (uint8_t)(local_rbx);
    result = PopBsdHandleRequest(10, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 8104881, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007545F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007545F4[BB_007545F4]
  bb_0075463A[BB_0075463A]
```
