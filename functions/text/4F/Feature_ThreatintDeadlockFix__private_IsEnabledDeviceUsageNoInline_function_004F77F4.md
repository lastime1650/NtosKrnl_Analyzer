# Feature_ThreatintDeadlockFix__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F77F4`–`0x004F7826` (길이 `50` bytes)
- VA: `0x00000001404F77F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F781B` → [Feature_ThreatintDeadlockFix__private_IsEnabledFallback](Feature_ThreatintDeadlockFix__private_IsEnabledFallback_function_004F782C.md) (function, `0x004F782C`)

### Direct callers
- [EtwTimLogBlockNonCetBinaries](../../page/7B/EtwTimLogBlockNonCetBinaries_function_007BA5B8.md) at `0x007BA7EB`
- [EtwTimLogProhibitLowILImageMap](../../page/7B/EtwTimLogProhibitLowILImageMap_function_007BB1F4.md) at `0x007BB3D1`
- [EtwTimLogProhibitNonMicrosoftBinaries](../../page/7B/EtwTimLogProhibitNonMicrosoftBinaries_function_007BB550.md) at `0x007BB772`
- [EtwpTimLogMitigationForProcess](../../page/A8/EtwpTimLogMitigationForProcess_function_00A81E6C.md) at `0x00A81FA4`

### Static image references
- `0x004F77FE` → RVA `0x00FC4C00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F77F4  48 83 EC 28                     sub rsp, 0x28
004F77F8  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F77FE  8B 05 FC D3 AC 00               mov eax, dword ptr [rip + 0xacd3fc]
004F7804  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F7808  A8 10                           test al, 0x10
004F780A  74 05                           je 0x1404f7811
004F780C  83 E0 01                        and eax, 1
004F780F  EB 0F                           jmp 0x1404f7820
004F7811  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F7816  BA 03 00 00 00                  mov edx, 3
004F781B  E8 0C 00 00 00                  call 0x1404f782c
004F7820  48 83 C4 28                     add rsp, 0x28
004F7824  C3                              ret
004F7825  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ThreatintDeadlockFix__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11326460)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11326460)))) & (16)) == 0) goto loc_004F7811;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11326460))) & (1));
    goto loc_004F7820;
loc_004F7811:
    result = Feature_ThreatintDeadlockFix__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7820:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_ThreatintDeadlockFix__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACD3FC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACD3FC)))) & (16)) == 0) goto loc_004F7811;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACD3FC))) & (1));
    goto loc_004F7820;
loc_004F7811:
    result = Feature_ThreatintDeadlockFix__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7820:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F77F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F77F4[BB_004F77F4]
  bb_004F780C[BB_004F780C]
  bb_004F7811[BB_004F7811]
  bb_004F7820[BB_004F7820]
  bb_004F7825[BB_004F7825]
  bb_004F77F4 -->|branch| bb_004F7811
  bb_004F77F4 -->|fallthrough| bb_004F780C
  bb_004F780C -->|branch| bb_004F7820
  bb_004F7811 -->|flow| bb_004F7820
```
