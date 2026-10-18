# PopClearConnectedStandbyMarker

- RVA: `0x00AB38D8`–`0x00AB394E` (길이 `118` bytes)
- VA: `0x0000000140AB38D8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCAAC`
- 디코드: `30`개 명령, `118/118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00AB38F7` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AB393B` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (function, `0x004B27A0`)
- `0x00AB3947` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- [PopCaptureSleepStudyStatistics](../../text/43/PopCaptureSleepStudyStatistics_function_004399F4.md) at `0x00439FC3`

### Static image references
- `0x00AB38DE` → RVA `0x00F0F1F0` (`.data`; read)
- `0x00AB38F0` → RVA `0x00F0F1E0` (`.data`; read)
- `0x00AB38FC` → RVA `0x00E6741B` (`.data`; read)
- `0x00AB3904` → RVA `0x00E67410` (`.data`; read/write)
- `0x00AB390E` → RVA `0x00E67418` (`.data`; read/write)
- `0x00AB391D` → RVA `0x00E67407` (`.data`; read)
- `0x00AB392F` → RVA `0x00E6741B` (`.data`; write)
- `0x00AB3935` → RVA `0x00E67407` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AB38F7` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AB393B` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (`PAGE` → `.text`)
  - `0x00AB3947` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB38D8  40 53                           push rbx
00AB38DA  48 83 EC 20                     sub rsp, 0x20
00AB38DE  80 3D 0B B9 45 00 00            cmp byte ptr [rip + 0x45b90b], 0
00AB38E5  8B D9                           mov ebx, ecx
00AB38E7  74 07                           je 0x140ab38f0
00AB38E9  48 83 C4 20                     add rsp, 0x20
00AB38ED  5B                              pop rbx
00AB38EE  C3                              ret
00AB38EF  CC                              int3
00AB38F0  48 8D 0D E9 B8 45 00            lea rcx, [rip + 0x45b8e9]
00AB38F7  E8 48 D2 97 FF                  call 0x140430b44
00AB38FC  8A 15 19 3B 3B 00               mov dl, byte ptr [rip + 0x3b3b19]
00AB3902  8A C3                           mov al, bl
00AB3904  48 83 25 04 3B 3B 00 00         and qword ptr [rip + 0x3b3b04], 0
00AB390C  24 3F                           and al, 0x3f
00AB390E  80 25 03 3B 3B 00 FD            and byte ptr [rip + 0x3b3b03], 0xfd
00AB3915  80 E2 C0                        and dl, 0xc0
00AB3918  0A D0                           or dl, al
00AB391A  C1 EB 18                        shr ebx, 0x18
00AB391D  8A 05 E4 3A 3B 00               mov al, byte ptr [rip + 0x3b3ae4]
00AB3923  B9 03 00 00 00                  mov ecx, 3
00AB3928  24 0F                           and al, 0xf
00AB392A  C0 E3 04                        shl bl, 4
00AB392D  0A D8                           or bl, al
00AB392F  88 15 E6 3A 3B 00               mov byte ptr [rip + 0x3b3ae6], dl
00AB3935  88 1D CC 3A 3B 00               mov byte ptr [rip + 0x3b3acc], bl
00AB393B  E8 60 EE 9F FF                  call 0x1404b27a0
00AB3940  48 8D 0D 99 B8 45 00            lea rcx, [rip + 0x45b899]
00AB3947  E8 70 C2 82 FF                  call 0x1402dfbbc
00AB394C  EB 9B                           jmp 0x140ab38e9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopClearConnectedStandbyMarker(int a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int8 *)(v_rip + 4569355)) == 0) goto loc_00AB38F0;
loc_00AB38E9:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00AB38F0:
    result = PopAcquireRwLockExclusive(v_rip + 4569321, a2, a3, a4);
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(a1))) & (63));
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 3881753)) & (192));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    v_rbx = (unsigned int)(((unsigned int)(a1)) >> (24));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 3881700)) & (15));
    v_rbx = (unsigned __int8)((v_rbx) << (4));
    v_rbx = (unsigned __int8)((v_rbx) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_rip + 3881702) = (unsigned __int8)(a2);
    *(unsigned __int8 *)(v_rip + 3881676) = (unsigned __int8)(v_rbx);
    result = PopBsdHandleRequest(3, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4569241, a2, a3, a4);
    goto loc_00AB38E9;
}
```

## 5. (Beta) C Style

```c
int64_t PopClearConnectedStandbyMarker(int32_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint8_t *)(v_rip + 0x45B90B)) == 0) goto loc_00AB38F0;
loc_00AB38E9:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00AB38F0:
    result = PopAcquireRwLockExclusive(v_rip + 4569321, a2, a3, a4);
    result = (uint8_t)(((uint8_t)((uint32_t)(Arg1))) & (63));
    a2 = (uint8_t)((*(uint8_t *)(v_rip + 0x3B3B19)) & (192));
    a2 = (uint8_t)((a2) | ((uint8_t)(result)));
    local_rbx = (uint32_t)(((uint32_t)(Arg1)) >> (24));
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x3B3AE4)) & (15));
    local_rbx = (uint8_t)((local_rbx) << (4));
    local_rbx = (uint8_t)((local_rbx) | ((uint8_t)(result)));
    *(uint8_t *)(v_rip + 0x3B3AE6) = (uint8_t)(a2);
    *(uint8_t *)(v_rip + 0x3B3ACC) = (uint8_t)(local_rbx);
    result = PopBsdHandleRequest(3, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4569241, a2, a3, a4);
    goto loc_00AB38E9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB38D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB38D8[BB_00AB38D8]
  bb_00AB38E9[BB_00AB38E9]
  bb_00AB38EF[BB_00AB38EF]
  bb_00AB38F0[BB_00AB38F0]
  bb_00AB38D8 -->|branch| bb_00AB38F0
  bb_00AB38D8 -->|fallthrough| bb_00AB38E9
  bb_00AB38EF -->|flow| bb_00AB38F0
  bb_00AB38F0 -->|branch| bb_00AB38E9
```
