# PopSetPowerSettingValueAcDc

- RVA: `0x00914D6C`–`0x00914DDD` (길이 `113` bytes)
- VA: `0x0000000140914D6C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085980`
- 디코드: `36`개 명령, `113/113` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **16**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00914D95` → [PopSetPowerSettingValue](PopSetPowerSettingValue_function_00914E54.md) (function, `0x00914E54`)
- `0x00914DB5` → [PopSetPowerSettingValue](PopSetPowerSettingValue_function_00914E54.md) (function, `0x00914E54`)

### Direct callers
- [PopScanIdleList](../../text/49/PopScanIdleList_function_00497F04.md) at `0x00498243`
- [PdcPoLowPower](../../text/4D/PdcPoLowPower_function_004D3F20.md) at `0x004D3F41`
- [PopErratumUpdateCallback](../../text/5D/PopErratumUpdateCallback_function_005D4760.md) at `0x005D4795`
- [PopWnfMixedRealityCallback](../75/PopWnfMixedRealityCallback_function_007585B0.md) at `0x00758610`
- [PopSetAwayModeStatus](../75/PopSetAwayModeStatus_function_0075EE84.md) at `0x0075EED9`
- [PdcPoLidReliabilityUpdateCallback](../75/PdcPoLidReliabilityUpdateCallback_function_0075F110.md) at `0x0075F13A`
- [PopEsPublishStateV2](../76/PopEsPublishStateV2_function_00769908.md) at `0x007699F7`
- [PopEsPublishStateV2](../76/PopEsPublishStateV2_function_00769908.md) at `0x00769A30`
- [PopSessionWinlogonNotification](../76/PopSessionWinlogonNotification_function_0076BF60.md) at `0x0076C017`
- [PopWnfSprActiveSessionChangeCallback](../90/PopWnfSprActiveSessionChangeCallback_function_0090C930.md) at `0x0090C9E0`
- [PopUpdateDiskIdleTimeoutSetting](PopUpdateDiskIdleTimeoutSetting_function_00912E30.md) at `0x00912E69`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00957033`
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8C20F`
- [PopMonitorProcessBrightnessAction](../A9/PopMonitorProcessBrightnessAction_function_00A97340.md) at `0x00A973A8`
- [PopBatteryApplyCompositeState](../AE/PopBatteryApplyCompositeState_function_00AE0CD0.md) at `0x00AE0D88`
- [PopBatteryApplyCompositeState](../AE/PopBatteryApplyCompositeState_function_00AE0CD0.md) at `0x00AE0E81`
- [PopBatteryWorker](../AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE2116`
- [sub_00B218E0](../B2/Unknown_function_00B218E0.md) at `0x00B2192F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00914D6C  48 8B C4                        mov rax, rsp
00914D6F  48 89 58 08                     mov qword ptr [rax + 8], rbx
00914D73  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00914D77  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00914D7B  57                              push rdi
00914D7C  48 83 EC 30                     sub rsp, 0x30
00914D80  49 8B D8                        mov rbx, r8
00914D83  8B FA                           mov edi, edx
00914D85  44 8B CA                        mov r9d, edx
00914D88  48 89 58 E8                     mov qword ptr [rax - 0x18], rbx
00914D8C  45 33 C0                        xor r8d, r8d
00914D8F  83 CA FF                        or edx, 0xffffffff
00914D92  48 8B F1                        mov rsi, rcx
00914D95  E8 BA 00 00 00                  call 0x140914e54
00914D9A  33 ED                           xor ebp, ebp
00914D9C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00914DA1  85 C0                           test eax, eax
00914DA3  44 8B CF                        mov r9d, edi
00914DA6  41 B8 01 00 00 00               mov r8d, 1
00914DAC  48 8B CE                        mov rcx, rsi
00914DAF  0F 48 E8                        cmovs ebp, eax
00914DB2  83 CA FF                        or edx, 0xffffffff
00914DB5  E8 9A 00 00 00                  call 0x140914e54
00914DBA  85 C0                           test eax, eax
00914DBC  78 18                           js 0x140914dd6
00914DBE  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00914DC3  8B C5                           mov eax, ebp
00914DC5  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00914DCA  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00914DCF  48 83 C4 30                     add rsp, 0x30
00914DD3  5F                              pop rdi
00914DD4  C3                              ret
00914DD5  CC                              int3
00914DD6  85 ED                           test ebp, ebp
00914DD8  0F 49 E8                        cmovns ebp, eax
00914DDB  EB E1                           jmp 0x140914dbe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSetPowerSettingValueAcDc(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = a3;
    a3 = 0;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = PopSetPowerSettingValue(a1, a2, a3, (unsigned int)(a2));
    v_rbp = 0;
    v_stack_m18 = 0;
    if (sign_flag) { v_rbp = (unsigned int)(result); }
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = PopSetPowerSettingValue(a1, a2, 1, (unsigned int)((unsigned int)((unsigned int)(a2))));
    if (sign_flag) goto loc_00914DD6;
loc_00914DBE:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)(v_rbp));
loc_00914DD6:
    v_rbp = v_stack_p10;
    if (!sign_flag) { v_rbp = (unsigned int)((unsigned int)((unsigned int)(v_rbp))); }
    goto loc_00914DBE;
}
```

## 5. (Beta) C Style

```c
int64_t PopSetPowerSettingValueAcDc(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = Arg3;
    Arg3 = 0;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = PopSetPowerSettingValue(Arg1, Arg2, Arg3, (uint32_t)(Arg2));
    local_rbp = 0;
    v_stack_m18 = 0;
    if (sign_flag) { local_rbp = (uint32_t)(result); }
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = PopSetPowerSettingValue(Arg1, Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(Arg2))));
    if (sign_flag) goto loc_00914DD6;
loc_00914DBE:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)(local_rbp));
loc_00914DD6:
    local_rbp = v_stack_p10;
    if (!sign_flag) { local_rbp = (uint32_t)((uint32_t)((uint32_t)(local_rbp))); }
    goto loc_00914DBE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00914D6C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00914D6C[BB_00914D6C]
  bb_00914DBE[BB_00914DBE]
  bb_00914DD5[BB_00914DD5]
  bb_00914DD6[BB_00914DD6]
  bb_00914D6C -->|branch| bb_00914DD6
  bb_00914D6C -->|fallthrough| bb_00914DBE
  bb_00914DD5 -->|flow| bb_00914DD6
  bb_00914DD6 -->|branch| bb_00914DBE
```
