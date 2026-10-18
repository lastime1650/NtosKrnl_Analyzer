# MiUnlockVad

- RVA: `0x002A59C8`–`0x002A5A31` (길이 `105` bytes)
- VA: `0x00000001402A59C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `30`개 명령, `105/105` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **30**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A59FB` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x002A5A03` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x002A5A20` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- [MiMapImageScpCfgPages](../29/MiMapImageScpCfgPages_function_00294FA4.md) at `0x002950D7`
- [MiDeleteEmptyPageTables](MiDeleteEmptyPageTables_function_002A5220.md) at `0x002A54A4`
- [MiLockAddressSpaceToo](MiLockAddressSpaceToo_function_002A5670.md) at `0x002A5712`
- [MiInsertViewOfPhysicalSection](MiInsertViewOfPhysicalSection_function_002A57E0.md) at `0x002A5934`
- [MiEmptyWorkingSetPrivatePagesByVa](MiEmptyWorkingSetPrivatePagesByVa_function_002A6AC0.md) at `0x002A6BAD`
- [MiFindPlaceholderVadToReplace](MiFindPlaceholderVadToReplace_function_002A7280.md) at `0x002A72EF`
- [MiFindPlaceholderVadToReplace](MiFindPlaceholderVadToReplace_function_002A7280.md) at `0x002A73A1`
- [MiUnlockAndDereferenceVad](../31/MiUnlockAndDereferenceVad_function_00316E60.md) at `0x00316E93`
- [MiUnlockAndDereferenceVad](../31/MiUnlockAndDereferenceVad_function_00316E60.md) at `0x00316E9A`
- [MiUnlockAndDereferenceVad](../31/MiUnlockAndDereferenceVad_function_00316E60.md) at `0x00316EB2`
- [MiWaitForVadDeletion](../31/MiWaitForVadDeletion_function_00316F1C.md) at `0x00316F8D`
- [MiReleaseOutSwappedProcessCommit](../3C/MiReleaseOutSwappedProcessCommit_function_003C8320.md) at `0x003C8470`
- [MiReleaseOutSwappedProcessCommit](../3C/MiReleaseOutSwappedProcessCommit_function_003C8320.md) at `0x003C84A4`
- [MiReleaseCommitForResetPages](../66/MiReleaseCommitForResetPages_function_0066FAF8.md) at `0x0066FB99`
- [MiCanDeleteEnclave](../68/MiCanDeleteEnclave_function_00686D18.md) at `0x00686DBF`
- [MiStoreDiscardPoisonedPage](../69/MiStoreDiscardPoisonedPage_function_00692858.md) at `0x00692D00`
- [MiApplyImageHotPatchRequest](../../page/80/MiApplyImageHotPatchRequest_function_008025AC.md) at `0x00802842`
- [MiApplyImageHotPatchRequest](../../page/80/MiApplyImageHotPatchRequest_function_008025AC.md) at `0x0080289B`
- [MiApplyImageHotPatchRequest](../../page/80/MiApplyImageHotPatchRequest_function_008025AC.md) at `0x008028D8`
- [MiPrepareToHotPatchVad](../../page/80/MiPrepareToHotPatchVad_function_00806E70.md) at `0x00806EFB`
- [MiProcessPatchImageCfg](../../page/80/MiProcessPatchImageCfg_function_00806F9C.md) at `0x008071CF`
- [MiInitializeVsmEnclave](../../page/80/MiInitializeVsmEnclave_function_00808AE0.md) at `0x00808B3C`
- [MiTerminateEnclave](../../page/80/MiTerminateEnclave_function_00808C18.md) at `0x00808C79`
- [sub_0087F5A3](../../page/87/Unknown_function_0087F5A3.md) at `0x0087F5EE`
- [MiCoalescePlaceholderAllocations](../../page/88/MiCoalescePlaceholderAllocations_function_0088095C.md) at `0x00880B4A`
- [MiCommitFileBackedSection](../../page/88/MiCommitFileBackedSection_function_00882238.md) at `0x00882300`
- [MiReserveUserMemory](../../page/88/MiReserveUserMemory_function_00884498.md) at `0x00884805`
- [MiReserveUserMemory](../../page/88/MiReserveUserMemory_function_00884498.md) at `0x00884D97`
- [sub_00884EE1](../../page/88/Unknown_function_00884EE1.md) at `0x0088531E`
- [sub_0088535F](../../page/88/Unknown_function_0088535F.md) at `0x0088545E`
- [MiMapViewOfImageSection](../../page/97/MiMapViewOfImageSection_function_0097E92C.md) at `0x0097F078`
- [MiMapViewOfPhysicalSection](../../page/97/MiMapViewOfPhysicalSection_function_0097F984.md) at `0x0097FD7E`
- [MiAllocateNewSubAllocatedRegion](../../page/98/MiAllocateNewSubAllocatedRegion_function_00981EC0.md) at `0x0098212A`
- [MmCleanProcessAddressSpace](../../page/A1/MmCleanProcessAddressSpace_function_00A17EC0.md) at `0x00A17FF9`
- [MmCleanProcessAddressSpace](../../page/A1/MmCleanProcessAddressSpace_function_00A17EC0.md) at `0x00A180FB`
- [MiLoadSectionIntoVsmEnclave](../../page/AB/MiLoadSectionIntoVsmEnclave_function_00AB1D4C.md) at `0x00AB1DA3`
- [MiDeleteVadHotPatchState](../../page/AC/MiDeleteVadHotPatchState_function_00ACA608.md) at `0x00ACA65D`
- [sub_00B2A146](../../page/B2/Unknown_function_00B2A146.md) at `0x00B2A352`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A59C8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002A59CD  57                              push rdi
002A59CE  48 83 EC 20                     sub rsp, 0x20
002A59D2  8B 81 A8 05 00 00               mov eax, dword ptr [rcx + 0x5a8]
002A59D8  48 8D 7A 28                     lea rdi, [rdx + 0x28]
002A59DC  0F BA F0 07                     btr eax, 7
002A59E0  48 8B D9                        mov rbx, rcx
002A59E3  89 81 A8 05 00 00               mov dword ptr [rcx + 0x5a8], eax
002A59E9  48 83 C8 FF                     or rax, 0xffffffffffffffff
002A59ED  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
002A59F2  24 06                           and al, 6
002A59F4  3C 02                           cmp al, 2
002A59F6  75 08                           jne 0x1402a5a00
002A59F8  48 8B CF                        mov rcx, rdi
002A59FB  E8 D0 03 FC FF                  call 0x140265dd0
002A5A00  48 8B CF                        mov rcx, rdi
002A5A03  E8 F8 BB 03 00                  call 0x1402e1600
002A5A08  90                              nop
002A5A09  66 83 83 E6 01 00 00 01         add word ptr [rbx + 0x1e6], 1
002A5A11  75 12                           jne 0x1402a5a25
002A5A13  48 8D 83 98 00 00 00            lea rax, [rbx + 0x98]
002A5A1A  90                              nop
002A5A1B  48 39 00                        cmp qword ptr [rax], rax
002A5A1E  74 05                           je 0x1402a5a25
002A5A20  E8 5B D2 03 00                  call 0x1402e2c80
002A5A25  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002A5A2A  48 83 C4 20                     add rsp, 0x20
002A5A2E  5F                              pop rdi
002A5A2F  C3                              ret
002A5A30  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlockVad(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    *(unsigned int *)(a1 + 1448) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1448)));
    result = ((unsigned int)(*(unsigned int *)(a1 + 1448))) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a2 + 40;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a2 + 40, a2, a3, a4);
    if (((unsigned __int8)(result)) != 2) goto loc_002A5A25;
    result = a1 + 152;
    if ((*(unsigned __int64 *)(a1 + 152)) != (a1 + 152)) {
        result = KiCheckForKernelApcDelivery(a2 + 40, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlockVad(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    *(uint32_t *)(arg1 + 0x5A8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5A8)));
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x5A8))) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg2 + 40;
        result = ExfTryToWakePushLock(Arg1, Arg2, a3, a4);
    }
    result = KeAbPostRelease(Arg2 + 40, Arg2, a3, a4);
    if (((uint8_t)(result)) != 2) goto loc_002A5A25;
    result = Arg1 + 152;
    if ((*(uint64_t *)(arg1 + 0x98)) != (Arg1 + 152)) {
        result = KiCheckForKernelApcDelivery(Arg2 + 40, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0x1E6` | `16` | `R/W` |
| `Arg1` | `+ 0x5A8` | `32` | `R` |
| `Arg1` | `+ 0x5A8` | `32` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A59C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A59C8[BB_002A59C8]
  bb_002A59F8[BB_002A59F8]
  bb_002A5A00[BB_002A5A00]
  bb_002A5A13[BB_002A5A13]
  bb_002A5A20[BB_002A5A20]
  bb_002A5A25[BB_002A5A25]
  bb_002A5A30[BB_002A5A30]
  bb_002A59C8 -->|branch| bb_002A5A00
  bb_002A59C8 -->|fallthrough| bb_002A59F8
  bb_002A59F8 -->|flow| bb_002A5A00
  bb_002A5A00 -->|branch| bb_002A5A25
  bb_002A5A00 -->|fallthrough| bb_002A5A13
  bb_002A5A13 -->|branch| bb_002A5A25
  bb_002A5A13 -->|fallthrough| bb_002A5A20
  bb_002A5A20 -->|flow| bb_002A5A25
```
