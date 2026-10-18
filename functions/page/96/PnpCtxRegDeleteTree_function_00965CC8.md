# PnpCtxRegDeleteTree

- RVA: `0x00965CC8`–`0x00965CFE` (길이 `54` bytes)
- VA: `0x0000000140965CC8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **23**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00965CF3` → [RegRtlDeleteTreeInternal](../99/RegRtlDeleteTreeInternal_function_00994700.md) (function, `0x00994700`)

### Direct callers
- [CmDeleteCommonClassRegKeyWorker](../82/CmDeleteCommonClassRegKeyWorker_function_008298F8.md) at `0x00829AF5`
- [CmDeleteCommonClassRegKeyWorker](../82/CmDeleteCommonClassRegKeyWorker_function_008298F8.md) at `0x00829B48`
- [CmDeleteDeviceInterfaceRegKeyWorker](../82/CmDeleteDeviceInterfaceRegKeyWorker_function_00829E1C.md) at `0x0082A03A`
- [CmDeleteDeviceContainerRegKeyWorker](../82/CmDeleteDeviceContainerRegKeyWorker_function_0082B15C.md) at `0x0082B30E`
- [CmRemoveDeviceFromContainerWorker](../82/CmRemoveDeviceFromContainerWorker_function_0082C080.md) at `0x0082C1AF`
- [CmDeleteDevicePanelRegKeyWorker](../82/CmDeleteDevicePanelRegKeyWorker_function_0082E554.md) at `0x0082E709`
- [CmRemovePanelDeviceWorker](../82/CmRemovePanelDeviceWorker_function_0082F470.md) at `0x0082F582`
- [DrvDbDeleteObjectSubKey](../83/DrvDbDeleteObjectSubKey_function_00832EEC.md) at `0x00832F3A`
- [PiDevCfgFreeVariable](PiDevCfgFreeVariable_function_00964E80.md) at `0x00964EB8`
- [PiDevCfgInitResolveContext](PiDevCfgInitResolveContext_function_00965178.md) at `0x009652AA`
- [PiDevCfgConfigureSoftwareDevices](PiDevCfgConfigureSoftwareDevices_function_009652EC.md) at `0x0096541B`
- [PpDevCfgProcessDeviceReset](PpDevCfgProcessDeviceReset_function_00965498.md) at `0x00965671`
- [PpDevCfgProcessDeviceReset](PpDevCfgProcessDeviceReset_function_00965498.md) at `0x00965687`
- [PiDqDeleteUserObject](PiDqDeleteUserObject_function_00965B24.md) at `0x00965B98`
- [PipHardwareConfigActivateService](PipHardwareConfigActivateService_function_00965BFC.md) at `0x00965C90`
- [PiDevCfgResetDeviceDriverSettings](PiDevCfgResetDeviceDriverSettings_function_00966168.md) at `0x009663C6`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00978A0F`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00978A25`
- [PnpSetPropertyWorker](../99/PnpSetPropertyWorker_function_00991C08.md) at `0x009920ED`
- [PnpSetPropertyWorker](../99/PnpSetPropertyWorker_function_00991C08.md) at `0x0099210C`
- [PiDevCfgCopyDeviceKey](../99/PiDevCfgCopyDeviceKey_function_00997374.md) at `0x00997AA8`
- [sub_00B47098](../B4/Unknown_function_00B47098.md) at `0x00B471B6`
- [sub_00B47D18](../B4/Unknown_function_00B47D18.md) at `0x00B47D74`
- [PipMigrateCleanService](../../init/C3/PipMigrateCleanService_function_00C31674.md) at `0x00C3178F`
- [PipCommitPendingOsExtensionResource](../../init/C3/PipCommitPendingOsExtensionResource_function_00C35960.md) at `0x00C35ACF`
- [PipCommitPendingService](../../init/C3/PipCommitPendingService_function_00C35B70.md) at `0x00C35DC0`
- [PipCommitPendingService](../../init/C3/PipCommitPendingService_function_00C35B70.md) at `0x00C35E0C`
- [PipInitComputerIds](../../init/C7/PipInitComputerIds_function_00C74734.md) at `0x00C7480C`
- [PipInitComputerIds](../../init/C7/PipInitComputerIds_function_00C74734.md) at `0x00C7485B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00965CC8  48 83 EC 28                     sub rsp, 0x28
00965CCC  4D 8B D0                        mov r10, r8
00965CCF  4C 8B DA                        mov r11, rdx
00965CD2  45 33 C0                        xor r8d, r8d
00965CD5  48 85 C9                        test rcx, rcx
00965CD8  74 10                           je 0x140965cea
00965CDA  48 8B 81 E0 00 00 00            mov rax, qword ptr [rcx + 0xe0]
00965CE1  48 85 C0                        test rax, rax
00965CE4  74 04                           je 0x140965cea
00965CE6  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
00965CEA  45 33 C9                        xor r9d, r9d
00965CED  49 8B D2                        mov rdx, r10
00965CF0  49 8B CB                        mov rcx, r11
00965CF3  E8 08 EA 02 00                  call 0x140994700
00965CF8  48 83 C4 28                     add rsp, 0x28
00965CFC  C3                              ret
00965CFD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpCtxRegDeleteTree(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = 0;
    if (a1 == 0) goto loc_00965CEA;
    if (*(unsigned __int64 *)(a1 + 224) != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 8);
    }
    a4 = 0;
    result = RegRtlDeleteTreeInternal(a2, a3, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpCtxRegDeleteTree(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = 0;
    if (Arg1 == 0) goto loc_00965CEA;
    if (*(uint64_t *)(Arg1 + 0xE0) != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0xE0) + 0x8);
    }
    Arg4 = 0;
    result = RegRtlDeleteTreeInternal(Arg2, Arg3, Arg3, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00965CC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00965CC8[BB_00965CC8]
  bb_00965CDA[BB_00965CDA]
  bb_00965CE6[BB_00965CE6]
  bb_00965CEA[BB_00965CEA]
  bb_00965CFD[BB_00965CFD]
  bb_00965CC8 -->|branch| bb_00965CEA
  bb_00965CC8 -->|fallthrough| bb_00965CDA
  bb_00965CDA -->|branch| bb_00965CEA
  bb_00965CDA -->|fallthrough| bb_00965CE6
  bb_00965CE6 -->|flow| bb_00965CEA
```
