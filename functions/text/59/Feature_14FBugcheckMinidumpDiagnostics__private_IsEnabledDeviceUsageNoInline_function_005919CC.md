# Feature_14FBugcheckMinidumpDiagnostics__private_IsEnabledDeviceUsageNoInline

- RVA: `0x005919CC`–`0x005919FE` (길이 `50` bytes)
- VA: `0x00000001405919CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005919F3` → [Feature_14FBugcheckMinidumpDiagnostics__private_IsEnabledFallback](Feature_14FBugcheckMinidumpDiagnostics__private_IsEnabledFallback_function_00591A04.md) (function, `0x00591A04`)

### Direct callers
- [IopAddBugcheckTriageDataFromParameters](IopAddBugcheckTriageDataFromParameters_function_00593E54.md) at `0x00593EEA`
- [KiCollectTriageDumpDataBlocks](../5B/KiCollectTriageDumpDataBlocks_function_005B43F8.md) at `0x005B470D`
- [PopPdcRegister](../../page/70/PopPdcRegister_function_00704AD0.md) at `0x00704C4F`

### Static image references
- `0x005919D6` → RVA `0x00FC4788` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005919CC  48 83 EC 28                     sub rsp, 0x28
005919D0  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005919D6  8B 05 AC 2D A3 00               mov eax, dword ptr [rip + 0xa32dac]
005919DC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005919E0  A8 10                           test al, 0x10
005919E2  74 05                           je 0x1405919e9
005919E4  83 E0 01                        and eax, 1
005919E7  EB 0F                           jmp 0x1405919f8
005919E9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005919EE  BA 03 00 00 00                  mov edx, 3
005919F3  E8 0C 00 00 00                  call 0x140591a04
005919F8  48 83 C4 28                     add rsp, 0x28
005919FC  C3                              ret
005919FD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_14FBugcheckMinidumpDiagnostics__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10694060)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10694060)))) & (16)) == 0) goto loc_005919E9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10694060))) & (1));
    goto loc_005919F8;
loc_005919E9:
    result = Feature_14FBugcheckMinidumpDiagnostics__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005919F8:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_14FBugcheckMinidumpDiagnostics__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA32DAC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA32DAC)))) & (16)) == 0) goto loc_005919E9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA32DAC))) & (1));
    goto loc_005919F8;
loc_005919E9:
    result = Feature_14FBugcheckMinidumpDiagnostics__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005919F8:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005919CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005919CC[BB_005919CC]
  bb_005919E4[BB_005919E4]
  bb_005919E9[BB_005919E9]
  bb_005919F8[BB_005919F8]
  bb_005919FD[BB_005919FD]
  bb_005919CC -->|branch| bb_005919E9
  bb_005919CC -->|fallthrough| bb_005919E4
  bb_005919E4 -->|branch| bb_005919F8
  bb_005919E9 -->|flow| bb_005919F8
```
