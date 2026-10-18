# ExQueryWnfStateData

- RVA: `0x00A4A480`–`0x00A4A515` (길이 `149` bytes)
- VA: `0x0000000140A4A480`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C994`
- 디코드: `42`개 명령, `149/149` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **17**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A4A4B6` → [ExpWnfAcquireSubscriptionNameInstance](ExpWnfAcquireSubscriptionNameInstance_function_00A4A51C.md) (function, `0x00A4A51C`)
- `0x00A4A4D6` → [ExpWnfReadStateData](../90/ExpWnfReadStateData_function_00909C50.md) (function, `0x00909C50`)
- `0x00A4A4E1` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00A4A4EB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [PopWnfAirplaneModeCallback](../../text/5D/PopWnfAirplaneModeCallback_function_005D13D0.md) at `0x005D1405`
- [PopWnfBluetoothChargingCallback](../../text/5D/PopWnfBluetoothChargingCallback_function_005D1460.md) at `0x005D147F`
- [PopWnfMobileHotspotCallback](../../text/5D/PopWnfMobileHotspotCallback_function_005D14F0.md) at `0x005D151C`
- [PopErratumUpdateCallback](../../text/5D/PopErratumUpdateCallback_function_005D4760.md) at `0x005D477A`
- [CmFcpWnfScmStateChangeNotificationCallback](../../text/66/CmFcpWnfScmStateChangeNotificationCallback_function_0066B560.md) at `0x0066B57E`
- [PipUpdateSetupOobeCompleteWnfCallback](../72/PipUpdateSetupOobeCompleteWnfCallback_function_007239C0.md) at `0x007239DE`
- [PopWnfMixedRealityCallback](../75/PopWnfMixedRealityCallback_function_007585B0.md) at `0x007585DC`
- [PopWnfUserAwayPredictionCallback](../75/PopWnfUserAwayPredictionCallback_function_00758640.md) at `0x00758660`
- [PopWnfEffectivePowerModeCallback](../75/PopWnfEffectivePowerModeCallback_function_0075C3B0.md) at `0x0075C408`
- [PopWnfUsb4DisplayPresenceCallback](../76/PopWnfUsb4DisplayPresenceCallback_function_007656E0.md) at `0x00765752`
- [PopWnfInSupCallback](../76/PopWnfInSupCallback_function_00765B50.md) at `0x00765B8B`
- [PopBatteryChargeLimitSettingWnfCallback](../76/PopBatteryChargeLimitSettingWnfCallback_function_00766670.md) at `0x007666B1`
- [PopPowerAdapterRecOverrideWnfCallback](../76/PopPowerAdapterRecOverrideWnfCallback_function_00767D30.md) at `0x00767D63`
- [PopUsbErrorWNFNotificationCallback](../76/PopUsbErrorWNFNotificationCallback_function_00768470.md) at `0x007684A8`
- [PopAdaptiveWnfCallback](../76/PopAdaptiveWnfCallback_function_0076BAB0.md) at `0x0076BAF2`
- [PopAdaptiveStandbyWnfCallback](../76/PopAdaptiveStandbyWnfCallback_function_0076F910.md) at `0x0076FA1E`
- [PopAdaptiveStandbyWnfCallback](../76/PopAdaptiveStandbyWnfCallback_function_0076F910.md) at `0x0076FC77`
- [PopAdaptiveStandbyWnfCallback](../76/PopAdaptiveStandbyWnfCallback_function_0076F910.md) at `0x0076FD1B`
- [TtmpWnfInactivityTimeoutCallback](../77/TtmpWnfInactivityTimeoutCallback_function_0077D990.md) at `0x0077D9AF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A4A4E1` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00A4A4EB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4A480  48 8B C4                        mov rax, rsp
00A4A483  48 89 58 08                     mov qword ptr [rax + 8], rbx
00A4A487  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00A4A48B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00A4A48F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00A4A493  41 56                           push r14
00A4A495  48 83 EC 30                     sub rsp, 0x30
00A4A499  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A4A4A2  4C 8B F2                        mov r14, rdx
00A4A4A5  48 8B D1                        mov rdx, rcx
00A4A4A8  49 8B D9                        mov rbx, r9
00A4A4AB  49 8B E8                        mov rbp, r8
00A4A4AE  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A4A4B5  90                              nop
00A4A4B6  E8 61 00 00 00                  call 0x140a4a51c
00A4A4BB  33 FF                           xor edi, edi
00A4A4BD  48 8B F0                        mov rsi, rax
00A4A4C0  48 85 C0                        test rax, rax
00A4A4C3  74 49                           je 0x140a4a50e
00A4A4C5  44 8B 0B                        mov r9d, dword ptr [rbx]
00A4A4C8  4C 8B C5                        mov r8, rbp
00A4A4CB  49 8B D6                        mov rdx, r14
00A4A4CE  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A4A4D3  48 8B C8                        mov rcx, rax
00A4A4D6  E8 75 F7 EB FF                  call 0x140909c50
00A4A4DB  8B D8                           mov ebx, eax
00A4A4DD  48 8D 4E 08                     lea rcx, [rsi + 8]
00A4A4E1  E8 9A F9 8F FF                  call 0x140349e80
00A4A4E6  85 DB                           test ebx, ebx
00A4A4E8  0F 48 FB                        cmovs edi, ebx
00A4A4EB  E8 C0 33 81 FF                  call 0x14025d8b0
00A4A4F0  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A4A4F5  8B C7                           mov eax, edi
00A4A4F7  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00A4A4FC  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00A4A501  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00A4A506  48 83 C4 30                     add rsp, 0x30
00A4A50A  41 5E                           pop r14
00A4A50C  C3                              ret
00A4A50D  CC                              int3
00A4A50E  BF 34 00 00 C0                  mov edi, 0xc0000034
00A4A513  EB D6                           jmp 0x140a4a4eb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExQueryWnfStateData(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    result = ExpWnfAcquireSubscriptionNameInstance(a1, a1, a3, a4);
    v_rdi = 0;
    if (result == 0) goto loc_00A4A50E;
    v_stack_m18 = a4;
    result = ExpWnfReadStateData(result, a2, a3, (unsigned int)(*(unsigned int *)(a4)));
    result = ExReleaseRundownProtection(result + 8, a2, a3, (unsigned int)(*(unsigned int *)(a4)));
    if (sign_flag) { v_rdi = (unsigned int)((unsigned int)((unsigned int)(result))); }
loc_00A4A4EB:
    result = KeLeaveCriticalRegion(result + 8, a2, a3, (unsigned int)(*(unsigned int *)(a4)));
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)(v_rdi));
loc_00A4A50E:
    goto loc_00A4A4EB;
}
```

## 5. (Beta) C Style

```c
int64_t ExQueryWnfStateData(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    result = ExpWnfAcquireSubscriptionNameInstance(Arg1, Arg1, Arg3, Arg4);
    local_rdi = 0;
    if (result == 0) goto loc_00A4A50E;
    v_stack_m18 = Arg4;
    result = ExpWnfReadStateData(result, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg4)));
    result = ExReleaseRundownProtection(result + 8, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg4)));
    if (sign_flag) { local_rdi = (uint32_t)((uint32_t)((uint32_t)(result))); }
loc_00A4A4EB:
    result = KeLeaveCriticalRegion(result + 8, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg4)));
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)(local_rdi));
loc_00A4A50E:
    goto loc_00A4A4EB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4A480&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4A480[BB_00A4A480]
  bb_00A4A4C5[BB_00A4A4C5]
  bb_00A4A4EB[BB_00A4A4EB]
  bb_00A4A50D[BB_00A4A50D]
  bb_00A4A50E[BB_00A4A50E]
  bb_00A4A480 -->|branch| bb_00A4A50E
  bb_00A4A480 -->|fallthrough| bb_00A4A4C5
  bb_00A4A4C5 -->|flow| bb_00A4A4EB
  bb_00A4A50D -->|flow| bb_00A4A50E
  bb_00A4A50E -->|branch| bb_00A4A4EB
```
