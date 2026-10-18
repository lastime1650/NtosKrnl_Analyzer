# PopFxEnablePlatformStates

- RVA: `0x005D2A98`–`0x005D2AC4` (길이 `44` bytes)
- VA: `0x00000001405D2A98`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005D2AA0` → [PopPepPlatformStateRegistered](PopPepPlatformStateRegistered_function_005DCDB8.md) (function, `0x005DCDB8`)
- `0x005D2AA5` → [PpmGetDeepSleepPlatformStateIndex](../4B/PpmGetDeepSleepPlatformStateIndex_function_004B09F0.md) (function, `0x004B09F0`)
- `0x005D2AB9` → [PopFxInitializeSocSubsystemStaticInfo](../../page/75/PopFxInitializeSocSubsystemStaticInfo_function_00758EC8.md) (function, `0x00758EC8`)

### Direct callers
- [PpmEnableCoordinatedIdleStates](../../page/75/PpmEnableCoordinatedIdleStates_function_00754CD0.md) at `0x00754CF4`

### Static image references
- `0x005D2AB1` → RVA `0x00E27EC0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005D2AB9` → [PopFxInitializeSocSubsystemStaticInfo](../../page/75/PopFxInitializeSocSubsystemStaticInfo_function_00758EC8.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D2A98  48 83 EC 28                     sub rsp, 0x28
005D2A9C  85 C9                           test ecx, ecx
005D2A9E  74 1E                           je 0x1405d2abe
005D2AA0  E8 13 A3 00 00                  call 0x1405dcdb8
005D2AA5  E8 46 DF ED FF                  call 0x1404b09f0
005D2AAA  83 F8 FF                        cmp eax, -1
005D2AAD  74 0F                           je 0x1405d2abe
005D2AAF  8B C8                           mov ecx, eax
005D2AB1  87 0D 09 54 85 00               xchg dword ptr [rip + 0x855409], ecx
005D2AB7  8B C8                           mov ecx, eax
005D2AB9  E8 0A 64 18 00                  call 0x140758ec8
005D2ABE  48 83 C4 28                     add rsp, 0x28
005D2AC2  C3                              ret
005D2AC3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxEnablePlatformStates(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 0) goto loc_005D2ABE;
    result = PopPepPlatformStateRegistered(a1, a2, a3, a4);
    result = PpmGetDeepSleepPlatformStateIndex(a1, a2, a3, a4);
    if (((unsigned int)(result)) != -1) {
        a1 = (unsigned int)(result);
        a1 = (unsigned int)(result);
        result = PopFxInitializeSocSubsystemStaticInfo(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxEnablePlatformStates(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 0) goto loc_005D2ABE;
    result = PopPepPlatformStateRegistered(Arg1, a2, a3, a4);
    result = PpmGetDeepSleepPlatformStateIndex(Arg1, a2, a3, a4);
    if (((uint32_t)(result)) != -1) {
        Arg1 = (uint32_t)(result);
        Arg1 = (uint32_t)(result);
        result = PopFxInitializeSocSubsystemStaticInfo(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D2A98&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D2A98[BB_005D2A98]
  bb_005D2AA0[BB_005D2AA0]
  bb_005D2AAF[BB_005D2AAF]
  bb_005D2ABE[BB_005D2ABE]
  bb_005D2AC3[BB_005D2AC3]
  bb_005D2A98 -->|branch| bb_005D2ABE
  bb_005D2A98 -->|fallthrough| bb_005D2AA0
  bb_005D2AA0 -->|branch| bb_005D2ABE
  bb_005D2AA0 -->|fallthrough| bb_005D2AAF
  bb_005D2AAF -->|flow| bb_005D2ABE
```
