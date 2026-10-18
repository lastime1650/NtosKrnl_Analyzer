# IoLockUnlockPnpDeviceTree

- RVA: `0x00AB953C`–`0x00AB9575` (길이 `57` bytes)
- VA: `0x0000000140AB953C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00090138`
- 디코드: `15`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AB955E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AB9569` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AB956E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [PopFxBuildDripsBlockingDeviceList](../../text/49/PopFxBuildDripsBlockingDeviceList_function_0049B5B0.md) at `0x0049B659`
- [PopFxDestroyDripsBlockingDeviceList](../75/PopFxDestroyDripsBlockingDeviceList_function_00758DEC.md) at `0x00758EA6`
- [PopDirectedDripsUmMarkTestDevices](../AC/PopDirectedDripsUmMarkTestDevices_function_00ACF828.md) at `0x00ACF883`
- [PopDirectedDripsUmMarkTestDevices](../AC/PopDirectedDripsUmMarkTestDevices_function_00ACF828.md) at `0x00ACF909`

### Static image references
- `0x00AB9542` → RVA `0x00F8C560` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AB955E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AB9569` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AB956E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB953C  48 83 EC 28                     sub rsp, 0x28
00AB9540  84 C9                           test cl, cl
00AB9542  48 8D 0D 17 30 4D 00            lea rcx, [rip + 0x4d3017]
00AB9549  74 1E                           je 0x140ab9569
00AB954B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AB9554  B2 01                           mov dl, 1
00AB9556  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AB955D  90                              nop
00AB955E  E8 5D 86 75 FF                  call 0x140211bc0
00AB9563  48 83 C4 28                     add rsp, 0x28
00AB9567  C3                              ret
00AB9568  CC                              int3
00AB9569  E8 A2 64 7A FF                  call 0x14025fa10
00AB956E  E8 3D 43 7A FF                  call 0x14025d8b0
00AB9573  EB EE                           jmp 0x140ab9563
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoLockUnlockPnpDeviceTree(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 0) goto loc_00AB9569;
    result = ExAcquireResourceSharedLite(v_rip + 5058583, 1, a3, a4);
loc_00AB9563:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AB9569:
    result = ExReleaseResourceLite(v_rip + 5058583, 1, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 5058583, 1, a3, a4);
    goto loc_00AB9563;
}
```

## 5. (Beta) C Style

```c
int64_t IoLockUnlockPnpDeviceTree(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 0) goto loc_00AB9569;
    result = ExAcquireResourceSharedLite(v_rip + 5058583, 1, a3, a4);
loc_00AB9563:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AB9569:
    result = ExReleaseResourceLite(v_rip + 5058583, 1, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 5058583, 1, a3, a4);
    goto loc_00AB9563;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB953C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB953C[BB_00AB953C]
  bb_00AB954B[BB_00AB954B]
  bb_00AB9563[BB_00AB9563]
  bb_00AB9568[BB_00AB9568]
  bb_00AB9569[BB_00AB9569]
  bb_00AB953C -->|branch| bb_00AB9569
  bb_00AB953C -->|fallthrough| bb_00AB954B
  bb_00AB954B -->|flow| bb_00AB9563
  bb_00AB9568 -->|flow| bb_00AB9569
  bb_00AB9569 -->|branch| bb_00AB9563
```
