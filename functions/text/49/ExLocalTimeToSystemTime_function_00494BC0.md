# ExLocalTimeToSystemTime

- RVA: `0x00494BC0`–`0x00494BE6` (길이 `38` bytes)
- VA: `0x0000000140494BC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00494BC7` → [PsGetCurrentServerSiloGlobals](../2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- [HalpAcpiRealTimeToUtcTime](../../page/70/HalpAcpiRealTimeToUtcTime_function_007065D8.md) at `0x0070667B`
- [PopNetGetNextDueRefreshTime](../../page/76/PopNetGetNextDueRefreshTime_function_00768BD4.md) at `0x00768C70`
- [ExpRefreshSystemTime](../../page/7C/ExpRefreshSystemTime_function_007C6264.md) at `0x007C636E`
- [NtSetSystemTime](../../page/7C/NtSetSystemTime_function_007C65F0.md) at `0x007C6873`
- [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6B976`
- [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6B9DE`
- [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6BA2B`
- [ExUpdateSystemTimeFromCmos](../../pagelk/B7/ExUpdateSystemTimeFromCmos_function_00B7BD98.md) at `0x00B7BE2A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00494BC0  48 83 EC 28                     sub rsp, 0x28
00494BC4  4C 8B D1                        mov r10, rcx
00494BC7  E8 24 96 E6 FF                  call 0x1402fe1f0
00494BCC  4C 8B 80 C8 04 00 00            mov r8, qword ptr [rax + 0x4c8]
00494BD3  49 8B 88 B8 01 00 00            mov rcx, qword ptr [r8 + 0x1b8]
00494BDA  49 03 0A                        add rcx, qword ptr [r10]
00494BDD  48 89 0A                        mov qword ptr [rdx], rcx
00494BE0  48 83 C4 28                     add rsp, 0x28
00494BE4  C3                              ret
00494BE5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExLocalTimeToSystemTime(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 440)) + (*(unsigned __int64 *)(a1));
    *(unsigned __int64 *)(a2) = a1;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExLocalTimeToSystemTime(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, a3, a4);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B8)) + (*(uint64_t *)(Arg1));
    *(uint64_t *)(Arg2) = Arg1;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00494BC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00494BC0[BB_00494BC0]
  bb_00494BE5[BB_00494BE5]
```
