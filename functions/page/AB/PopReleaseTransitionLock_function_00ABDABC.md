# PopReleaseTransitionLock

- RVA: `0x00ABDABC`–`0x00ABDAFC` (길이 `64` bytes)
- VA: `0x0000000140ABDABC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EE6C`
- 디코드: `19`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00ABDADF` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00ABDAF5` → [PopDirectedDripsNotify](../A8/PopDirectedDripsNotify_function_00A80850.md) (function, `0x00A80850`)

### Direct callers
- [PoInitHiberServices](../75/PoInitHiberServices_function_007537C4.md) at `0x0075383A`
- [PopWnfHibernatePolicyCallback](../75/PopWnfHibernatePolicyCallback_function_0075E3C0.md) at `0x0075E41B`
- [PopNotifyPolicyDevice](../76/PopNotifyPolicyDevice_function_00765FF0.md) at `0x0076605F`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00956627`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x0095733C`
- [PopDirectedDripsReleaseTransitionLock](../A4/PopDirectedDripsReleaseTransitionLock_function_00A4DC0C.md) at `0x00A4DC2F`
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8B97A`
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8C8C4`
- [PopUnlockAfterSleepWorker](../../pagelk/B7/PopUnlockAfterSleepWorker_function_00B782A0.md) at `0x00B783AC`

### Static image references
- `0x00ABDAC2` → RVA `0x00F0B7D8` (`.data`; read/write)
- `0x00ABDACC` → RVA `0x00F0B7D0` (`.data`; read/write)
- `0x00ABDAD3` → RVA `0x00F0B900` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00ABDADF` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABDABC  40 53                           push rbx
00ABDABE  48 83 EC 20                     sub rsp, 0x20
00ABDAC2  48 83 25 0E DD 44 00 00         and qword ptr [rip + 0x44dd0e], 0
00ABDACA  8B D9                           mov ebx, ecx
00ABDACC  83 25 FD DC 44 00 00            and dword ptr [rip + 0x44dcfd], 0
00ABDAD3  48 8D 0D 26 DE 44 00            lea rcx, [rip + 0x44de26]
00ABDADA  45 33 C0                        xor r8d, r8d
00ABDADD  33 D2                           xor edx, edx
00ABDADF  E8 2C 18 88 FF                  call 0x14033f310
00ABDAE4  83 FB 07                        cmp ebx, 7
00ABDAE7  75 07                           jne 0x140abdaf0
00ABDAE9  48 83 C4 20                     add rsp, 0x20
00ABDAED  5B                              pop rbx
00ABDAEE  C3                              ret
00ABDAEF  CC                              int3
00ABDAF0  33 D2                           xor edx, edx
00ABDAF2  8D 4A 09                        lea ecx, [rdx + 9]
00ABDAF5  E8 56 2D FC FF                  call 0x140a80850
00ABDAFA  EB ED                           jmp 0x140abdae9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopReleaseTransitionLock(int a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 4513318, a2, a3, a4);
    if (((unsigned int)((unsigned int)(a1))) != 7) goto loc_00ABDAF0;
loc_00ABDAE9:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00ABDAF0:
    a2 = 0;
    result = PopDirectedDripsNotify(a2 + 9, a2, a3, a4);
    goto loc_00ABDAE9;
}
```

## 5. (Beta) C Style

```c
int64_t PopReleaseTransitionLock(int32_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 4513318, Arg2, Arg3, a4);
    if (((uint32_t)((uint32_t)(Arg1))) != 7) goto loc_00ABDAF0;
loc_00ABDAE9:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00ABDAF0:
    Arg2 = 0;
    result = PopDirectedDripsNotify(Arg2 + 9, Arg2, Arg3, a4);
    goto loc_00ABDAE9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABDABC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ABDABC[BB_00ABDABC]
  bb_00ABDAE9[BB_00ABDAE9]
  bb_00ABDAEF[BB_00ABDAEF]
  bb_00ABDAF0[BB_00ABDAF0]
  bb_00ABDABC -->|branch| bb_00ABDAF0
  bb_00ABDABC -->|fallthrough| bb_00ABDAE9
  bb_00ABDAEF -->|flow| bb_00ABDAF0
  bb_00ABDAF0 -->|branch| bb_00ABDAE9
```
