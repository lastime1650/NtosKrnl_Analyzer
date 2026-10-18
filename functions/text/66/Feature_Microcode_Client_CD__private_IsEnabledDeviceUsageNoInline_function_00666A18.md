# Feature_Microcode_Client_CD__private_IsEnabledDeviceUsageNoInline

- RVA: `0x00666A18`–`0x00666A4A` (길이 `50` bytes)
- VA: `0x0000000140666A18`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00666A3F` → [Feature_Microcode_Client_CD__private_IsEnabledFallback](Feature_Microcode_Client_CD__private_IsEnabledFallback_function_00666A50.md) (function, `0x00666A50`)

### Direct callers
- [HalpMcUpdatePostUpdate](../4D/HalpMcUpdatePostUpdate_function_004D6670.md) at `0x004D6690`
- [PrExtApplyPatch](../4F/PrExtApplyPatch_function_004FB058.md) at `0x004FB08C`
- [PrExtExportRecordData](PrExtExportRecordData_function_00666B94.md) at `0x00666BB9`
- [PrExtExportRecordData](PrExtExportRecordData_function_00666B94.md) at `0x00666C0C`
- [PrExtGetRecord](PrExtGetRecord_function_00666CE8.md) at `0x00666D3F`
- [GetMicrocodePatchData](GetMicrocodePatchData_function_00666E48.md) at `0x00666E9F`
- [GetMicrocodePatchData](GetMicrocodePatchData_function_00666E48.md) at `0x00666F0A`
- [GetMicrocodePatchData](GetMicrocodePatchData_function_00666E48.md) at `0x00666F35`
- [MicrocodeGetRecord](MicrocodeGetRecord_function_00667060.md) at `0x00667160`
- [MicrocodeGetRecord](MicrocodeGetRecord_function_00667060.md) at `0x00667181`
- [MicrocodeUpdate](MicrocodeUpdate_function_00667480.md) at `0x006674E7`
- [AMDMicrocodeGetRecordData](AMDMicrocodeGetRecordData_function_00667CA0.md) at `0x00667CC0`
- [AMDMicrocodeMetaDataCheck](AMDMicrocodeMetaDataCheck_function_00667D40.md) at `0x00667D80`
- [AMDMicrocodeRecordSizeCheck](AMDMicrocodeRecordSizeCheck_function_00667E2C.md) at `0x00667E44`

### Static image references
- `0x00666A22` → RVA `0x00FC46D8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00666A18  48 83 EC 28                     sub rsp, 0x28
00666A1C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00666A22  8B 05 B0 DC 95 00               mov eax, dword ptr [rip + 0x95dcb0]
00666A28  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00666A2C  A8 10                           test al, 0x10
00666A2E  74 05                           je 0x140666a35
00666A30  83 E0 01                        and eax, 1
00666A33  EB 0F                           jmp 0x140666a44
00666A35  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00666A3A  BA 03 00 00 00                  mov edx, 3
00666A3F  E8 0C 00 00 00                  call 0x140666a50
00666A44  48 83 C4 28                     add rsp, 0x28
00666A48  C3                              ret
00666A49  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Microcode_Client_CD__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9821360)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9821360)))) & (16)) == 0) goto loc_00666A35;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9821360))) & (1));
    goto loc_00666A44;
loc_00666A35:
    result = Feature_Microcode_Client_CD__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00666A44:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Microcode_Client_CD__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x95DCB0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x95DCB0)))) & (16)) == 0) goto loc_00666A35;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x95DCB0))) & (1));
    goto loc_00666A44;
loc_00666A35:
    result = Feature_Microcode_Client_CD__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00666A44:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00666A18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00666A18[BB_00666A18]
  bb_00666A30[BB_00666A30]
  bb_00666A35[BB_00666A35]
  bb_00666A44[BB_00666A44]
  bb_00666A49[BB_00666A49]
  bb_00666A18 -->|branch| bb_00666A35
  bb_00666A18 -->|fallthrough| bb_00666A30
  bb_00666A30 -->|branch| bb_00666A44
  bb_00666A35 -->|flow| bb_00666A44
```
