# FsRtlpOplockBreakByCacheFlags

- RVA: `0x004E4990`–`0x004E6EC0` (길이 `9,520` bytes)
- VA: `0x00000001404E4990`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5EF4`
- 디코드: `1,656`개 명령, `9,520/9,520` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **74**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **28**

### Outgoing calls
- `0x004E4B10` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E4B74` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004E4C5E` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E4C9E` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E4E80` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E4FC1` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E500F` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E512B` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x004E519D` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E51C9` → [FsRtlpCheckSharingAgainstOplockOwner](../4B/FsRtlpCheckSharingAgainstOplockOwner_function_004BA718.md) (function, `0x004BA718`)
- `0x004E529F` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E52B5` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004E52CE` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x004E5333` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004E538E` → [FsRtlpCheckSharingAgainstOplockOwner](../4B/FsRtlpCheckSharingAgainstOplockOwner_function_004BA718.md) (function, `0x004BA718`)
- `0x004E53E4` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004E53FB` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x004E548A` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004E54B9` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004E54D2` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x004E5530` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004E560F` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E562A` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004E5643` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x004E56A1` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004E56CD` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004E56E6` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x004E56FD` → [FsRtlpModifyThreadPriorities](../48/FsRtlpModifyThreadPriorities_function_0048B098.md) (function, `0x0048B098`)
- `0x004E5707` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x004E5733` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004E5744` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004E576F` → [FsRtlpRemoveAndCompleteWaitingIrp](../42/FsRtlpRemoveAndCompleteWaitingIrp_function_00425FC0.md) (function, `0x00425FC0`)
- `0x004E57C9` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004E58B3` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E5908` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E5936` → [FsRtlpRemoveAndCompleteReadOnlyIrp](../4B/FsRtlpRemoveAndCompleteReadOnlyIrp_function_004B495C.md) (function, `0x004B495C`)
- `0x004E5B00` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E5B59` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E5B96` → [FsRtlpCheckSharingAgainstOplockOwner](../4B/FsRtlpCheckSharingAgainstOplockOwner_function_004BA718.md) (function, `0x004BA718`)
- `0x004E5C8C` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E5CA4` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (function, `0x007158B4`)
- `0x004E5D1B` → [FsRtlpRemoveAndCompleteRHIrp](../42/FsRtlpRemoveAndCompleteRHIrp_function_00425964.md) (function, `0x00425964`)
- `0x004E5D4C` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (function, `0x007158B4`)
- `0x004E5E80` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E5FDB` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E6010` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (function, `0x007158B4`)
- `0x004E6047` → [FsRtlpRemoveAndCompleteRHIrp](../42/FsRtlpRemoveAndCompleteRHIrp_function_00425964.md) (function, `0x00425964`)
- `0x004E606B` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (function, `0x007158B4`)
- `0x004E6176` → [FsRtlpReleaseIrpsWaitingForRH](../42/FsRtlpReleaseIrpsWaitingForRH_function_00425CBC.md) (function, `0x00425CBC`)
- `0x004E61BF` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E61E3` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x004E61F5` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x004E62C6` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E640C` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E64ED` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E65BB` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E65F1` → [FsRtlpCheckSharingAgainstOplockOwner](../4B/FsRtlpCheckSharingAgainstOplockOwner_function_004BA718.md) (function, `0x004BA718`)
- `0x004E66D5` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E67A3` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E68FA` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E6922` → [FsRtlpCheckSharingAgainstOplockOwner](../4B/FsRtlpCheckSharingAgainstOplockOwner_function_004BA718.md) (function, `0x004BA718`)
- `0x004E6A06` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E6A47` → [FsRtlpCheckSharingAgainstOplockOwner](../4B/FsRtlpCheckSharingAgainstOplockOwner_function_004BA718.md) (function, `0x004BA718`)
- `0x004E6B4E` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E6BB8` → [FsRtlpCheckSharingAgainstOplockOwner](../4B/FsRtlpCheckSharingAgainstOplockOwner_function_004BA718.md) (function, `0x004BA718`)
- `0x004E6CA1` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E6CB5` → [Feature_Servicing_CloseOplockTimeoutGap__private_IsEnabledDeviceUsageNoInline](../58/Feature_Servicing_CloseOplockTimeoutGap__private_IsEnabledDeviceUsageNoInline_function_00581DD8.md) (function, `0x00581DD8`)
- `0x004E6CE8` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (function, `0x007158B4`)
- `0x004E6D04` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (function, `0x007158B4`)
- `0x004E6D18` → [FsRtlpModifyThreadPriorities](../48/FsRtlpModifyThreadPriorities_function_0048B098.md) (function, `0x0048B098`)
- `0x004E6D22` → [FsRtlpOplockSendModernAppTermination](../49/FsRtlpOplockSendModernAppTermination_function_0049F22C.md) (function, `0x0049F22C`)
- `0x004E6D9E` → [FsRtlpWaitOnIrp](FsRtlpWaitOnIrp_function_004E7998.md) (function, `0x004E7998`)
- `0x004E6E8D` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E6EA7` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [FsRtlCheckOplockEx2](../3F/FsRtlCheckOplockEx2_function_003F2BC0.md) at `0x003F358B`
- [FsRtlOplockBreakToNoneEx](../58/FsRtlOplockBreakToNoneEx_function_00581F40.md) at `0x00582073`
- [FsRtlCheckUpperOplock](../../page/71/FsRtlCheckUpperOplock_function_007145F0.md) at `0x007148EA`
- [FsRtlCheckUpperOplock](../../page/71/FsRtlCheckUpperOplock_function_007145F0.md) at `0x00714A79`
- [FsRtlCheckOplockForFsFilterCallback](../../page/9F/FsRtlCheckOplockForFsFilterCallback_function_009F67A0.md) at `0x009F69F3`
- [FsRtlOplockBreakH2](../../page/A4/FsRtlOplockBreakH2_function_00A44550.md) at `0x00A446D5`

### Static image references
- `0x004E49A5` → RVA `0x00E0A740` (`.data`; read)
- `0x004E4A57` → RVA `0x00E06C50` (`.data`; read)
- `0x004E4B02` → RVA `0x00044EA4` (`.rdata`; read)
- `0x004E4C50` → RVA `0x00044E39` (`.rdata`; read)
- `0x004E4D73` → RVA `0x00044F04` (`.rdata`; read)
- `0x004E4E5F` → RVA `0x00044CFA` (`.rdata`; read)
- `0x004E4FB3` → RVA `0x00045060` (`.rdata`; read)
- `0x004E511C` → RVA `0x00044FF5` (`.rdata`; read)
- `0x004E5291` → RVA `0x000447F4` (`.rdata`; read)
- `0x004E5601` → RVA `0x0004485E` (`.rdata`; read)
- `0x004E58A5` → RVA `0x00044C92` (`.rdata`; read)
- `0x004E5A0D` → RVA `0x00044DCE` (`.rdata`; read)
- `0x004E5AF2` → RVA `0x00044D65` (`.rdata`; read)
- `0x004E5C7E` → RVA `0x000451A6` (`.rdata`; read)
- `0x004E5E30` → RVA `0x00045217` (`.rdata`; read)
- `0x004E5F99` → RVA `0x000452ED` (`.rdata`; read)
- `0x004E615D` → RVA `0x00045282` (`.rdata`; read)
- `0x004E62B8` → RVA `0x00044936` (`.rdata`; read)
- `0x004E63FE` → RVA `0x00044B46` (`.rdata`; read)
- `0x004E64DF` → RVA `0x00044AD9` (`.rdata`; read)
- `0x004E65AD` → RVA `0x00044717` (`.rdata`; read)
- `0x004E66C7` → RVA `0x000448C7` (`.rdata`; read)
- `0x004E6795` → RVA `0x00045137` (`.rdata`; read)
- `0x004E689A` → RVA `0x000450CC` (`.rdata`; read)
- `0x004E69F8` → RVA `0x0004463B` (`.rdata`; read)
- `0x004E6B40` → RVA `0x000446A9` (`.rdata`; read)
- `0x004E6C93` → RVA `0x00044787` (`.rdata`; read)
- `0x004E6E6C` → RVA `0x00044F7B` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x004E5CA4` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (`.text` → `PAGE`)
  - `0x004E5D4C` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (`.text` → `PAGE`)
  - `0x004E6010` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (`.text` → `PAGE`)
  - `0x004E606B` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (`.text` → `PAGE`)
  - `0x004E6CE8` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (`.text` → `PAGE`)
  - `0x004E6D04` → [FsRtlpOplockTryStartBreakAckTimeout](../../page/71/FsRtlpOplockTryStartBreakAckTimeout_function_007158B4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E4990  4C 8B DC                        mov r11, rsp
004E4993  53                              push rbx
004E4994  56                              push rsi
004E4995  57                              push rdi
004E4996  41 54                           push r12
004E4998  41 55                           push r13
004E499A  41 56                           push r14
004E499C  41 57                           push r15
004E499E  48 81 EC 70 0C 00 00            sub rsp, 0xc70
004E49A5  48 8B 05 94 5D 92 00            mov rax, qword ptr [rip + 0x925d94]
004E49AC  48 33 C4                        xor rax, rsp
004E49AF  48 89 84 24 60 0C 00 00         mov qword ptr [rsp + 0xc60], rax
004E49B7  45 8B F9                        mov r15d, r9d
004E49BA  49 8B C0                        mov rax, r8
004E49BD  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004E49C2  4C 8B CA                        mov r9, rdx
004E49C5  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
004E49CD  48 8B D9                        mov rbx, rcx
004E49D0  8B B4 24 D8 0C 00 00            mov esi, dword ptr [rsp + 0xcd8]
004E49D7  48 8B 8C 24 F0 0C 00 00         mov rcx, qword ptr [rsp + 0xcf0]
004E49DF  48 89 8C 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rcx
004E49E7  48 8B 8C 24 10 0D 00 00         mov rcx, qword ptr [rsp + 0xd10]
004E49EF  48 89 8C 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rcx
004E49F7  48 8B 8C 24 20 0D 00 00         mov rcx, qword ptr [rsp + 0xd20]
004E49FF  48 89 8C 24 00 02 00 00         mov qword ptr [rsp + 0x200], rcx
004E4A07  48 8B 8C 24 28 0D 00 00         mov rcx, qword ptr [rsp + 0xd28]
004E4A0F  48 89 8C 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rcx
004E4A17  33 D2                           xor edx, edx
004E4A19  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
004E4A1D  0F 57 C0                        xorps xmm0, xmm0
004E4A20  33 C9                           xor ecx, ecx
004E4A22  0F 11 84 24 A0 02 00 00         movups xmmword ptr [rsp + 0x2a0], xmm0
004E4A2A  49 89 8B 08 F6 FF FF            mov qword ptr [r11 - 0x9f8], rcx
004E4A31  88 54 24 60                     mov byte ptr [rsp + 0x60], dl
004E4A35  88 54 24 70                     mov byte ptr [rsp + 0x70], dl
004E4A39  88 54 24 72                     mov byte ptr [rsp + 0x72], dl
004E4A3D  44 8D 42 01                     lea r8d, [rdx + 1]
004E4A41  44 88 44 24 71                  mov byte ptr [rsp + 0x71], r8b
004E4A46  41 8B CF                        mov ecx, r15d
004E4A49  83 E1 08                        and ecx, 8
004E4A4C  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
004E4A50  4C 8D AB 90 00 00 00            lea r13, [rbx + 0x90]
004E4A57  83 3D F2 21 92 00 05            cmp dword ptr [rip + 0x9221f2], 5
004E4A5E  0F 86 C8 00 00 00               jbe 0x1404e4b2c
004E4A64  45 89 BB F0 F3 FF FF            mov dword ptr [r11 - 0xc10], r15d
004E4A6B  49 8D 83 F0 F3 FF FF            lea rax, [r11 - 0xc10]
004E4A72  49 89 83 38 F6 FF FF            mov qword ptr [r11 - 0x9c8], rax
004E4A79  49 C7 83 40 F6 FF FF 04 00 00 00  mov qword ptr [r11 - 0x9c0], 4
004E4A84  89 B4 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], esi
004E4A8B  49 8D 83 F4 F3 FF FF            lea rax, [r11 - 0xc0c]
004E4A92  49 89 83 48 F6 FF FF            mov qword ptr [r11 - 0x9b8], rax
004E4A99  49 C7 83 50 F6 FF FF 04 00 00 00  mov qword ptr [r11 - 0x9b0], 4
004E4AA4  49 89 9B 20 F5 FF FF            mov qword ptr [r11 - 0xae0], rbx
004E4AAB  49 8D 83 20 F5 FF FF            lea rax, [r11 - 0xae0]
004E4AB2  49 89 83 58 F6 FF FF            mov qword ptr [r11 - 0x9a8], rax
004E4AB9  49 C7 83 60 F6 FF FF 08 00 00 00  mov qword ptr [r11 - 0x9a0], 8
004E4AC4  41 8B 45 00                     mov eax, dword ptr [r13]
004E4AC8  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
004E4ACF  49 8D 83 F8 F3 FF FF            lea rax, [r11 - 0xc08]
004E4AD6  49 89 83 68 F6 FF FF            mov qword ptr [r11 - 0x998], rax
004E4ADD  49 C7 83 70 F6 FF FF 04 00 00 00  mov qword ptr [r11 - 0x990], 4
004E4AE8  49 8D 83 18 F6 FF FF            lea rax, [r11 - 0x9e8]
004E4AEF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E4AF4  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E4AFC  45 33 C9                        xor r9d, r9d
004E4AFF  45 33 C0                        xor r8d, r8d
004E4B02  48 8D 15 9B 03 B6 FF            lea rdx, [rip - 0x49fc65]
004E4B09  48 8D 0D 40 21 92 00            lea rcx, [rip + 0x922140]
004E4B10  E8 CB 15 F4 FF                  call 0x1404260e0
004E4B15  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
004E4B19  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
004E4B21  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
004E4B26  33 D2                           xor edx, edx
004E4B28  44 8D 42 01                     lea r8d, [rdx + 1]
004E4B2C  41 BC 00 50 00 00               mov r12d, 0x5000
004E4B32  41 BE 00 40 00 00               mov r14d, 0x4000
004E4B38  81 FE 00 70 00 00               cmp esi, 0x7000
004E4B3E  0F 84 29 01 00 00               je 0x1404e4c6d
004E4B44  41 3B F4                        cmp esi, r12d
004E4B47  0F 84 20 01 00 00               je 0x1404e4c6d
004E4B4D  41 3B F6                        cmp esi, r14d
004E4B50  0F 84 17 01 00 00               je 0x1404e4c6d
004E4B56  81 FE 00 20 00 00               cmp esi, 0x2000
004E4B5C  0F 84 0B 01 00 00               je 0x1404e4c6d
004E4B62  48 85 C0                        test rax, rax
004E4B65  74 12                           je 0x1404e4b79
004E4B67  C7 40 30 E3 00 00 C0            mov dword ptr [rax + 0x30], 0xc00000e3
004E4B6E  41 8A D0                        mov dl, r8b
004E4B71  48 8B C8                        mov rcx, rax
004E4B74  E8 47 6A DB FF                  call 0x14029b5c0
004E4B79  83 3D D0 20 92 00 03            cmp dword ptr [rip + 0x9220d0], 3
004E4B80  0F 86 DD 00 00 00               jbe 0x1404e4c63
004E4B86  C7 84 24 A0 00 00 00 E3 00 00 C0  mov dword ptr [rsp + 0xa0], 0xc00000e3
004E4B91  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
004E4B99  48 89 84 24 40 03 00 00         mov qword ptr [rsp + 0x340], rax
004E4BA1  48 C7 84 24 48 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x348], 4
004E4BAD  44 89 BC 24 9C 00 00 00         mov dword ptr [rsp + 0x9c], r15d
004E4BB5  48 8D 84 24 9C 00 00 00         lea rax, [rsp + 0x9c]
004E4BBD  48 89 84 24 50 03 00 00         mov qword ptr [rsp + 0x350], rax
004E4BC5  48 C7 84 24 58 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x358], 4
004E4BD1  89 B4 24 98 00 00 00            mov dword ptr [rsp + 0x98], esi
004E4BD8  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
004E4BE0  48 89 84 24 60 03 00 00         mov qword ptr [rsp + 0x360], rax
004E4BE8  48 C7 84 24 68 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x368], 4
004E4BF4  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
004E4BF9  48 8D 44 24 68                  lea rax, [rsp + 0x68]
004E4BFE  48 89 84 24 70 03 00 00         mov qword ptr [rsp + 0x370], rax
004E4C06  48 C7 84 24 78 03 00 00 08 00 00 00  mov qword ptr [rsp + 0x378], 8
004E4C12  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E4C18  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
004E4C1C  48 8D 44 24 78                  lea rax, [rsp + 0x78]
004E4C21  48 89 84 24 80 03 00 00         mov qword ptr [rsp + 0x380], rax
004E4C29  48 C7 84 24 88 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x388], 4
004E4C35  48 8D 84 24 20 03 00 00         lea rax, [rsp + 0x320]
004E4C3D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E4C42  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
004E4C4A  45 33 C9                        xor r9d, r9d
004E4C4D  45 33 C0                        xor r8d, r8d
004E4C50  48 8D 15 E2 01 B6 FF            lea rdx, [rip - 0x49fe1e]
004E4C57  48 8D 0D F2 1F 92 00            lea rcx, [rip + 0x921ff2]
004E4C5E  E8 7D 14 F4 FF                  call 0x1404260e0
004E4C63  B8 E3 00 00 C0                  mov eax, 0xc00000e3
004E4C68  E9 2F 22 00 00                  jmp 0x1404e6e9c
004E4C6D  48 85 DB                        test rbx, rbx
004E4C70  0F 84 22 22 00 00               je 0x1404e6e98
004E4C76  41 8B 45 00                     mov eax, dword ptr [r13]
004E4C7A  41 3B C0                        cmp eax, r8d
004E4C7D  0F 84 29 21 00 00               je 0x1404e6dac
004E4C83  85 C6                           test esi, eax
004E4C85  0F 84 21 21 00 00               je 0x1404e6dac
004E4C8B  85 C9                           test ecx, ecx
004E4C8D  0F 85 EC 00 00 00               jne 0x1404e4d7f
004E4C93  45 8B C7                        mov r8d, r15d
004E4C96  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
004E4C9A  49 8B 49 30                     mov rcx, qword ptr [r9 + 0x30]
004E4C9E  E8 0D DA F0 FF                  call 0x1403f26b0
004E4CA3  33 D2                           xor edx, edx
004E4CA5  84 C0                           test al, al
004E4CA7  0F 84 D2 00 00 00               je 0x1404e4d7f
004E4CAD  83 3D 9C 1F 92 00 05            cmp dword ptr [rip + 0x921f9c], 5
004E4CB4  0F 86 DA 21 00 00               jbe 0x1404e6e94
004E4CBA  89 94 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edx
004E4CC1  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
004E4CC9  48 89 84 24 90 04 00 00         mov qword ptr [rsp + 0x490], rax
004E4CD1  48 C7 84 24 98 04 00 00 04 00 00 00  mov qword ptr [rsp + 0x498], 4
004E4CDD  44 89 BC 24 9C 00 00 00         mov dword ptr [rsp + 0x9c], r15d
004E4CE5  48 8D 84 24 9C 00 00 00         lea rax, [rsp + 0x9c]
004E4CED  48 89 84 24 A0 04 00 00         mov qword ptr [rsp + 0x4a0], rax
004E4CF5  48 C7 84 24 A8 04 00 00 04 00 00 00  mov qword ptr [rsp + 0x4a8], 4
004E4D01  89 B4 24 98 00 00 00            mov dword ptr [rsp + 0x98], esi
004E4D08  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
004E4D10  48 89 84 24 B0 04 00 00         mov qword ptr [rsp + 0x4b0], rax
004E4D18  48 C7 84 24 B8 04 00 00 04 00 00 00  mov qword ptr [rsp + 0x4b8], 4
004E4D24  48 89 9C 24 20 02 00 00         mov qword ptr [rsp + 0x220], rbx
004E4D2C  48 8D 84 24 20 02 00 00         lea rax, [rsp + 0x220]
004E4D34  48 89 84 24 C0 04 00 00         mov qword ptr [rsp + 0x4c0], rax
004E4D3C  48 C7 84 24 C8 04 00 00 08 00 00 00  mov qword ptr [rsp + 0x4c8], 8
004E4D48  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E4D4E  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
004E4D52  48 8D 44 24 78                  lea rax, [rsp + 0x78]
004E4D57  48 89 84 24 D0 04 00 00         mov qword ptr [rsp + 0x4d0], rax
004E4D5F  48 C7 84 24 D8 04 00 00 04 00 00 00  mov qword ptr [rsp + 0x4d8], 4
004E4D6B  48 8D 84 24 70 04 00 00         lea rax, [rsp + 0x470]
004E4D73  48 8D 15 8A 01 B6 FF            lea rdx, [rip - 0x49fe76]
004E4D7A  E9 F4 20 00 00                  jmp 0x1404e6e73
004E4D7F  8B 8B 90 00 00 00               mov ecx, dword ptr [rbx + 0x90]
004E4D85  F6 C1 40                        test cl, 0x40
004E4D88  0F 84 04 01 00 00               je 0x1404e4e92
004E4D8E  41 F7 C7 00 00 01 10            test r15d, 0x10010000
004E4D95  0F 84 F7 00 00 00               je 0x1404e4e92
004E4D9B  83 3D AE 1E 92 00 03            cmp dword ptr [rip + 0x921eae], 3
004E4DA2  0F 86 DD 00 00 00               jbe 0x1404e4e85
004E4DA8  C7 44 24 74 09 09 00 C0         mov dword ptr [rsp + 0x74], 0xc0000909
004E4DB0  48 8D 44 24 74                  lea rax, [rsp + 0x74]
004E4DB5  48 89 84 24 00 05 00 00         mov qword ptr [rsp + 0x500], rax
004E4DBD  48 C7 84 24 08 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x508], 4
004E4DC9  44 89 BC 24 D0 01 00 00         mov dword ptr [rsp + 0x1d0], r15d
004E4DD1  48 8D 84 24 D0 01 00 00         lea rax, [rsp + 0x1d0]
004E4DD9  48 89 84 24 10 05 00 00         mov qword ptr [rsp + 0x510], rax
004E4DE1  48 C7 84 24 18 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x518], 4
004E4DED  89 B4 24 D8 01 00 00            mov dword ptr [rsp + 0x1d8], esi
004E4DF4  48 8D 84 24 D8 01 00 00         lea rax, [rsp + 0x1d8]
004E4DFC  48 89 84 24 20 05 00 00         mov qword ptr [rsp + 0x520], rax
004E4E04  48 C7 84 24 28 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x528], 4
004E4E10  48 89 9C 24 30 02 00 00         mov qword ptr [rsp + 0x230], rbx
004E4E18  48 8D 84 24 30 02 00 00         lea rax, [rsp + 0x230]
004E4E20  48 89 84 24 30 05 00 00         mov qword ptr [rsp + 0x530], rax
004E4E28  48 C7 84 24 38 05 00 00 08 00 00 00  mov qword ptr [rsp + 0x538], 8
004E4E34  89 8C 24 DC 01 00 00            mov dword ptr [rsp + 0x1dc], ecx
004E4E3B  48 8D 84 24 DC 01 00 00         lea rax, [rsp + 0x1dc]
004E4E43  48 89 84 24 40 05 00 00         mov qword ptr [rsp + 0x540], rax
004E4E4B  48 C7 84 24 48 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x548], 4
004E4E57  48 8D 84 24 E0 04 00 00         lea rax, [rsp + 0x4e0]
004E4E5F  48 8D 15 94 FE B5 FF            lea rdx, [rip - 0x4a016c]
004E4E66  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E4E6B  45 33 C9                        xor r9d, r9d
004E4E6E  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
004E4E76  45 33 C0                        xor r8d, r8d
004E4E79  48 8D 0D D0 1D 92 00            lea rcx, [rip + 0x921dd0]
004E4E80  E8 5B 12 F4 FF                  call 0x1404260e0
004E4E85  C7 44 24 74 09 09 00 C0         mov dword ptr [rsp + 0x74], 0xc0000909
004E4E8D  E9 06 20 00 00                  jmp 0x1404e6e98
004E4E92  8B C1                           mov eax, ecx
004E4E94  25 DF FF F0 01                  and eax, 0x1f0ffdf
004E4E99  41 B8 40 50 10 00               mov r8d, 0x105040
004E4E9F  41 3B C0                        cmp eax, r8d
004E4EA2  0F 87 54 14 00 00               ja 0x1404e62fc
004E4EA8  0F 84 54 13 00 00               je 0x1404e6202
004E4EAE  41 BD 00 10 00 00               mov r13d, 0x1000
004E4EB4  41 2B C5                        sub eax, r13d
004E4EB7  0F 84 32 09 00 00               je 0x1404e57ef
004E4EBD  83 E8 10                        sub eax, 0x10
004E4EC0  0F 84 29 09 00 00               je 0x1404e57ef
004E4EC6  2D F0 1F 00 00                  sub eax, 0x1ff0
004E4ECB  0F 84 68 0B 00 00               je 0x1404e5a39
004E4ED1  2D 40 20 00 00                  sub eax, 0x2040
004E4ED6  0F 84 6F 06 00 00               je 0x1404e554b
004E4EDC  2D 00 20 00 00                  sub eax, 0x2000
004E4EE1  0F 84 F4 02 00 00               je 0x1404e51db
004E4EE7  2D C0 3F 00 00                  sub eax, 0x3fc0
004E4EEC  0F 84 FD 08 00 00               je 0x1404e57ef
004E4EF2  2D 00 80 0F 00                  sub eax, 0xf8000
004E4EF7  0F 85 41 14 00 00               jne 0x1404e633e
004E4EFD  83 3D 4C 1D 92 00 05            cmp dword ptr [rip + 0x921d4c], 5
004E4F04  0F 86 BC 00 00 00               jbe 0x1404e4fc6
004E4F0A  44 89 BC 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r15d
004E4F12  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
004E4F1A  48 89 84 24 E0 02 00 00         mov qword ptr [rsp + 0x2e0], rax
004E4F22  48 C7 84 24 E8 02 00 00 04 00 00 00  mov qword ptr [rsp + 0x2e8], 4
004E4F2E  89 B4 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], esi
004E4F35  48 8D 84 24 B4 00 00 00         lea rax, [rsp + 0xb4]
004E4F3D  48 89 84 24 F0 02 00 00         mov qword ptr [rsp + 0x2f0], rax
004E4F45  48 C7 84 24 F8 02 00 00 04 00 00 00  mov qword ptr [rsp + 0x2f8], 4
004E4F51  48 89 9C 24 38 02 00 00         mov qword ptr [rsp + 0x238], rbx
004E4F59  48 8D 84 24 38 02 00 00         lea rax, [rsp + 0x238]
004E4F61  48 89 84 24 00 03 00 00         mov qword ptr [rsp + 0x300], rax
004E4F69  48 C7 84 24 08 03 00 00 08 00 00 00  mov qword ptr [rsp + 0x308], 8
004E4F75  89 8C 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ecx
004E4F7C  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
004E4F84  48 89 84 24 10 03 00 00         mov qword ptr [rsp + 0x310], rax
004E4F8C  48 C7 84 24 18 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x318], 4
004E4F98  48 8D 84 24 C0 02 00 00         lea rax, [rsp + 0x2c0]
004E4FA0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E4FA5  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E4FAD  45 33 C9                        xor r9d, r9d
004E4FB0  45 33 C0                        xor r8d, r8d
004E4FB3  48 8D 15 A6 00 B6 FF            lea rdx, [rip - 0x49ff5a]
004E4FBA  48 8D 0D 8F 1C 92 00            lea rcx, [rip + 0x921c8f]
004E4FC1  E8 1A 11 F4 FF                  call 0x1404260e0
004E4FC6  33 C9                           xor ecx, ecx
004E4FC8  44 8A E1                        mov r12b, cl
004E4FCB  88 8C 24 88 00 00 00            mov byte ptr [rsp + 0x88], cl
004E4FD2  8B C6                           mov eax, esi
004E4FD4  41 23 C5                        and eax, r13d
004E4FD7  0F 84 58 01 00 00               je 0x1404e5135
004E4FDD  4C 8B 73 48                     mov r14, qword ptr [rbx + 0x48]
004E4FE1  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
004E4FE9  48 8D 43 48                     lea rax, [rbx + 0x48]
004E4FED  4C 3B F0                        cmp r14, rax
004E4FF0  0F 84 32 01 00 00               je 0x1404e5128
004E4FF6  39 4C 24 78                     cmp dword ptr [rsp + 0x78], ecx
004E4FFA  75 1E                           jne 0x1404e501a
004E4FFC  45 8B C7                        mov r8d, r15d
004E4FFF  49 8B 56 18                     mov rdx, qword ptr [r14 + 0x18]
004E5003  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
004E500B  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
004E500F  E8 9C D6 F0 FF                  call 0x1403f26b0
004E5014  33 C9                           xor ecx, ecx
004E5016  84 C0                           test al, al
004E5018  75 2D                           jne 0x1404e5047
004E501A  B8 01 00 00 00                  mov eax, 1
004E501F  44 8A E0                        mov r12b, al
004E5022  88 84 24 88 00 00 00            mov byte ptr [rsp + 0x88], al
004E5029  41 F7 C7 00 00 01 10            test r15d, 0x10010000
004E5030  75 1A                           jne 0x1404e504c
004E5032  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
004E5036  25 FF FF 0F FF                  and eax, 0xff0fffff
004E503B  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
004E503F  0F BA E8 17                     bts eax, 0x17
004E5043  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
004E5047  4D 8B 36                        mov r14, qword ptr [r14]
004E504A  EB 95                           jmp 0x1404e4fe1
004E504C  83 3D FD 1B 92 00 03            cmp dword ptr [rip + 0x921bfd], 3
004E5053  0F 86 2C FE FF FF               jbe 0x1404e4e85
004E5059  C7 84 24 BC 00 00 00 09 09 00 C0  mov dword ptr [rsp + 0xbc], 0xc0000909
004E5064  48 8D 84 24 BC 00 00 00         lea rax, [rsp + 0xbc]
004E506C  48 89 84 24 70 05 00 00         mov qword ptr [rsp + 0x570], rax
004E5074  48 C7 84 24 78 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x578], 4
004E5080  44 89 BC 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r15d
004E5088  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
004E5090  48 89 84 24 80 05 00 00         mov qword ptr [rsp + 0x580], rax
004E5098  48 C7 84 24 88 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x588], 4
004E50A4  89 B4 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], esi
004E50AB  48 8D 84 24 C4 00 00 00         lea rax, [rsp + 0xc4]
004E50B3  48 89 84 24 90 05 00 00         mov qword ptr [rsp + 0x590], rax
004E50BB  48 C7 84 24 98 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x598], 4
004E50C7  48 89 9C 24 40 02 00 00         mov qword ptr [rsp + 0x240], rbx
004E50CF  48 8D 84 24 40 02 00 00         lea rax, [rsp + 0x240]
004E50D7  48 89 84 24 A0 05 00 00         mov qword ptr [rsp + 0x5a0], rax
004E50DF  48 C7 84 24 A8 05 00 00 08 00 00 00  mov qword ptr [rsp + 0x5a8], 8
004E50EB  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E50F1  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
004E50F8  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
004E5100  48 89 84 24 B0 05 00 00         mov qword ptr [rsp + 0x5b0], rax
004E5108  48 C7 84 24 B8 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x5b8], 4
004E5114  48 8D 84 24 50 05 00 00         lea rax, [rsp + 0x550]
004E511C  48 8D 15 D2 FE B5 FF            lea rdx, [rip - 0x4a012e]
004E5123  E9 3E FD FF FF                  jmp 0x1404e4e66
004E5128  48 8B CB                        mov rcx, rbx
004E512B  E8 BC 05 F4 FF                  call 0x1404256ec
004E5130  8B C6                           mov eax, esi
004E5132  41 23 C5                        and eax, r13d
004E5135  45 33 ED                        xor r13d, r13d
004E5138  0F BA E6 0D                     bt esi, 0xd
004E513C  0F 83 58 02 00 00               jae 0x1404e539a
004E5142  45 84 E4                        test r12b, r12b
004E5145  0F 85 BB 14 00 00               jne 0x1404e6606
004E514B  85 C0                           test eax, eax
004E514D  0F 85 47 02 00 00               jne 0x1404e539a
004E5153  48 8B 7B 48                     mov rdi, qword ptr [rbx + 0x48]
004E5157  41 BE 80 00 00 40               mov r14d, 0x40000080
004E515D  4C 8B A4 24 E8 0C 00 00         mov r12, qword ptr [rsp + 0xce8]
004E5165  4C 8B AC 24 E0 0C 00 00         mov r13, qword ptr [rsp + 0xce0]
004E516D  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
004E5175  48 8D 43 48                     lea rax, [rbx + 0x48]
004E5179  48 3B F8                        cmp rdi, rax
004E517C  0F 84 78 10 00 00               je 0x1404e61fa
004E5182  33 C0                           xor eax, eax
004E5184  39 44 24 78                     cmp dword ptr [rsp + 0x78], eax
004E5188  75 1E                           jne 0x1404e51a8
004E518A  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
004E518E  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
004E5196  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
004E519A  45 33 C0                        xor r8d, r8d
004E519D  E8 0E D5 F0 FF                  call 0x1403f26b0
004E51A2  84 C0                           test al, al
004E51A4  74 02                           je 0x1404e51a8
004E51A6  EB 2E                           jmp 0x1404e51d6
004E51A8  41 8B C7                        mov eax, r15d
004E51AB  41 23 C6                        and eax, r14d
004E51AE  41 3B C6                        cmp eax, r14d
004E51B1  0F 85 5A 12 00 00               jne 0x1404e6411
004E51B7  45 0F B7 0C 24                  movzx r9d, word ptr [r12]
004E51BC  45 8B 45 00                     mov r8d, dword ptr [r13]
004E51C0  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
004E51C4  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004E51C9  E8 4A 55 FD FF                  call 0x1404ba718
004E51CE  85 C0                           test eax, eax
004E51D0  0F 88 3B 12 00 00               js 0x1404e6411
004E51D6  48 8B 3F                        mov rdi, qword ptr [rdi]
004E51D9  EB 92                           jmp 0x1404e516d
004E51DB  83 3D 6E 1A 92 00 05            cmp dword ptr [rip + 0x921a6e], 5
004E51E2  0F 86 BC 00 00 00               jbe 0x1404e52a4
004E51E8  44 89 BC 24 CC 00 00 00         mov dword ptr [rsp + 0xcc], r15d
004E51F0  48 8D 84 24 CC 00 00 00         lea rax, [rsp + 0xcc]
004E51F8  48 89 84 24 E0 09 00 00         mov qword ptr [rsp + 0x9e0], rax
004E5200  48 C7 84 24 E8 09 00 00 04 00 00 00  mov qword ptr [rsp + 0x9e8], 4
004E520C  89 B4 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], esi
004E5213  48 8D 84 24 D0 00 00 00         lea rax, [rsp + 0xd0]
004E521B  48 89 84 24 F0 09 00 00         mov qword ptr [rsp + 0x9f0], rax
004E5223  48 C7 84 24 F8 09 00 00 04 00 00 00  mov qword ptr [rsp + 0x9f8], 4
004E522F  48 89 9C 24 78 02 00 00         mov qword ptr [rsp + 0x278], rbx
004E5237  48 8D 84 24 78 02 00 00         lea rax, [rsp + 0x278]
004E523F  48 89 84 24 00 0A 00 00         mov qword ptr [rsp + 0xa00], rax
004E5247  48 C7 84 24 08 0A 00 00 08 00 00 00  mov qword ptr [rsp + 0xa08], 8
004E5253  89 8C 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], ecx
004E525A  48 8D 84 24 D4 00 00 00         lea rax, [rsp + 0xd4]
004E5262  48 89 84 24 10 0A 00 00         mov qword ptr [rsp + 0xa10], rax
004E526A  48 C7 84 24 18 0A 00 00 04 00 00 00  mov qword ptr [rsp + 0xa18], 4
004E5276  48 8D 84 24 C0 09 00 00         lea rax, [rsp + 0x9c0]
004E527E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E5283  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E528B  45 33 C9                        xor r9d, r9d
004E528E  45 33 C0                        xor r8d, r8d
004E5291  48 8D 15 5C F5 B5 FF            lea rdx, [rip - 0x4a0aa4]
004E5298  48 8D 0D B1 19 92 00            lea rcx, [rip + 0x9219b1]
004E529F  E8 3C 0E F4 FF                  call 0x1404260e0
004E52A4  41 3B F6                        cmp esi, r14d
004E52A7  0F 85 A1 00 00 00               jne 0x1404e534e
004E52AD  48 8B 3B                        mov rdi, qword ptr [rbx]
004E52B0  B9 07 00 00 00                  mov ecx, 7
004E52B5  E8 C6 EA D8 FF                  call 0x140273d80
004E52BA  88 47 45                        mov byte ptr [rdi + 0x45], al
004E52BD  45 33 ED                        xor r13d, r13d
004E52C0  41 8B C5                        mov eax, r13d
004E52C3  48 87 47 68                     xchg qword ptr [rdi + 0x68], rax
004E52C7  8A 57 45                        mov dl, byte ptr [rdi + 0x45]
004E52CA  41 8D 4D 07                     lea ecx, [r13 + 7]
004E52CE  E8 6D D2 D8 FF                  call 0x140272540
004E52D3  44 38 6F 44                     cmp byte ptr [rdi + 0x44], r13b
004E52D7  0F 85 18 04 00 00               jne 0x1404e56f5
004E52DD  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
004E52E1  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
004E52E9  0F 57 C0                        xorps xmm0, xmm0
004E52EC  33 C0                           xor eax, eax
004E52EE  0F 11 01                        movups xmmword ptr [rcx], xmm0
004E52F1  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
004E52F5  45 8D 75 01                     lea r14d, [r13 + 1]
004E52F9  C7 01 01 00 18 00               mov dword ptr [rcx], 0x180001
004E52FF  45 8D 45 18                     lea r8d, [r13 + 0x18]
004E5303  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E5309  C1 E8 0C                        shr eax, 0xc
004E530C  83 E0 07                        and eax, 7
004E530F  89 41 04                        mov dword ptr [rcx + 4], eax
004E5312  C7 41 08 03 00 00 00            mov dword ptr [rcx + 8], 3
004E5319  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
004E531C  41 0B C6                        or eax, r14d
004E531F  89 41 0C                        mov dword ptr [rcx + 0xc], eax
004E5322  4C 89 47 38                     mov qword ptr [rdi + 0x38], r8
004E5326  48 8B 03                        mov rax, qword ptr [rbx]
004E5329  44 89 68 30                     mov dword ptr [rax + 0x30], r13d
004E532D  41 8A D6                        mov dl, r14b
004E5330  48 8B 0B                        mov rcx, qword ptr [rbx]
004E5333  E8 88 62 DB FF                  call 0x14029b5c0
004E5338  4C 89 2B                        mov qword ptr [rbx], r13
004E533B  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E5341  83 E0 20                        and eax, 0x20
004E5344  0D 40 70 50 00                  or eax, 0x507040
004E5349  E9 91 04 00 00                  jmp 0x1404e57df
004E534E  81 FE 00 20 00 00               cmp esi, 0x2000
004E5354  0F 85 4B 01 00 00               jne 0x1404e54a5
004E535A  48 8B 3B                        mov rdi, qword ptr [rbx]
004E535D  41 8B C7                        mov eax, r15d
004E5360  41 BE 80 00 00 40               mov r14d, 0x40000080
004E5366  41 23 C6                        and eax, r14d
004E5369  41 3B C6                        cmp eax, r14d
004E536C  75 6E                           jne 0x1404e53dc
004E536E  4C 8B 8C 24 E8 0C 00 00         mov r9, qword ptr [rsp + 0xce8]
004E5376  45 0F B7 09                     movzx r9d, word ptr [r9]
004E537A  4C 8B 84 24 E0 0C 00 00         mov r8, qword ptr [rsp + 0xce0]
004E5382  45 8B 00                        mov r8d, dword ptr [r8]
004E5385  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
004E5389  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004E538E  E8 85 53 FD FF                  call 0x1404ba718
004E5393  45 33 ED                        xor r13d, r13d
004E5396  85 C0                           test eax, eax
004E5398  78 45                           js 0x1404e53df
004E539A  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
004E539F  41 BE 01 00 00 00               mov r14d, 1
004E53A5  44 38 6C 24 60                  cmp byte ptr [rsp + 0x60], r13b
004E53AA  0F 84 E8 1A 00 00               je 0x1404e6e98
004E53B0  45 84 FE                        test r14b, r15b
004E53B3  0F 84 FC 18 00 00               je 0x1404e6cb5
004E53B9  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E53BF  0F BA E0 10                     bt eax, 0x10
004E53C3  73 0A                           jae 0x1404e53cf
004E53C5  0F BA E8 11                     bts eax, 0x11
004E53C9  89 83 90 00 00 00               mov dword ptr [rbx + 0x90], eax
004E53CF  C7 44 24 74 08 01 00 00         mov dword ptr [rsp + 0x74], 0x108
004E53D7  E9 BC 1A 00 00                  jmp 0x1404e6e98
004E53DC  45 33 ED                        xor r13d, r13d
004E53DF  B9 07 00 00 00                  mov ecx, 7
004E53E4  E8 97 E9 D8 FF                  call 0x140273d80
004E53E9  88 47 45                        mov byte ptr [rdi + 0x45], al
004E53EC  49 8B C5                        mov rax, r13
004E53EF  48 87 47 68                     xchg qword ptr [rdi + 0x68], rax
004E53F3  8A 57 45                        mov dl, byte ptr [rdi + 0x45]
004E53F6  B9 07 00 00 00                  mov ecx, 7
004E53FB  E8 40 D1 D8 FF                  call 0x140272540
004E5400  44 38 6F 44                     cmp byte ptr [rdi + 0x44], r13b
004E5404  0F 85 EB 02 00 00               jne 0x1404e56f5
004E540A  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
004E540E  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
004E5416  0F 57 C0                        xorps xmm0, xmm0
004E5419  33 C0                           xor eax, eax
004E541B  0F 11 02                        movups xmmword ptr [rdx], xmm0
004E541E  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
004E5422  44 8D 70 01                     lea r14d, [rax + 1]
004E5426  C7 02 01 00 18 00               mov dword ptr [rdx], 0x180001
004E542C  44 8D 40 18                     lea r8d, [rax + 0x18]
004E5430  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E5436  C1 E8 0C                        shr eax, 0xc
004E5439  83 E0 07                        and eax, 7
004E543C  89 42 04                        mov dword ptr [rdx + 4], eax
004E543F  C7 42 08 05 00 00 00            mov dword ptr [rdx + 8], 5
004E5446  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
004E5449  41 0B C6                        or eax, r14d
004E544C  89 42 0C                        mov dword ptr [rdx + 0xc], eax
004E544F  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
004E5457  45 38 29                        cmp byte ptr [r9], r13b
004E545A  75 1D                           jne 0x1404e5479
004E545C  83 C8 02                        or eax, 2
004E545F  89 42 0C                        mov dword ptr [rdx + 0xc], eax
004E5462  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
004E5466  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
004E546A  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
004E546D  89 42 10                        mov dword ptr [rdx + 0x10], eax
004E5470  41 0F B7 41 1A                  movzx eax, word ptr [r9 + 0x1a]
004E5475  66 89 42 14                     mov word ptr [rdx + 0x14], ax
004E5479  4C 89 47 38                     mov qword ptr [rdi + 0x38], r8
004E547D  48 8B 03                        mov rax, qword ptr [rbx]
004E5480  44 89 68 30                     mov dword ptr [rax + 0x30], r13d
004E5484  41 8A D6                        mov dl, r14b
004E5487  48 8B 0B                        mov rcx, qword ptr [rbx]
004E548A  E8 31 61 DB FF                  call 0x14029b5c0
004E548F  4C 89 2B                        mov qword ptr [rbx], r13
004E5492  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E5498  83 E0 20                        and eax, 0x20
004E549B  0D 40 70 30 00                  or eax, 0x307040
004E54A0  E9 3A 03 00 00                  jmp 0x1404e57df
004E54A5  41 23 F4                        and esi, r12d
004E54A8  41 3B F4                        cmp esi, r12d
004E54AB  0F 85 49 0D 00 00               jne 0x1404e61fa
004E54B1  48 8B 3B                        mov rdi, qword ptr [rbx]
004E54B4  B9 07 00 00 00                  mov ecx, 7
004E54B9  E8 C2 E8 D8 FF                  call 0x140273d80
004E54BE  88 47 45                        mov byte ptr [rdi + 0x45], al
004E54C1  45 33 ED                        xor r13d, r13d
004E54C4  41 8B C5                        mov eax, r13d
004E54C7  48 87 47 68                     xchg qword ptr [rdi + 0x68], rax
004E54CB  8A 57 45                        mov dl, byte ptr [rdi + 0x45]
004E54CE  41 8D 4D 07                     lea ecx, [r13 + 7]
004E54D2  E8 69 D0 D8 FF                  call 0x140272540
004E54D7  44 38 6F 44                     cmp byte ptr [rdi + 0x44], r13b
004E54DB  0F 85 14 02 00 00               jne 0x1404e56f5
004E54E1  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
004E54E5  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
004E54ED  0F 57 C0                        xorps xmm0, xmm0
004E54F0  33 C0                           xor eax, eax
004E54F2  0F 11 01                        movups xmmword ptr [rcx], xmm0
004E54F5  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
004E54F9  45 8D 75 01                     lea r14d, [r13 + 1]
004E54FD  C7 01 01 00 18 00               mov dword ptr [rcx], 0x180001
004E5503  45 8D 45 18                     lea r8d, [r13 + 0x18]
004E5507  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E550D  C1 E8 0C                        shr eax, 0xc
004E5510  83 E0 07                        and eax, 7
004E5513  89 41 04                        mov dword ptr [rcx + 4], eax
004E5516  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
004E5519  41 0B C6                        or eax, r14d
004E551C  89 41 0C                        mov dword ptr [rcx + 0xc], eax
004E551F  4C 89 47 38                     mov qword ptr [rdi + 0x38], r8
004E5523  48 8B 03                        mov rax, qword ptr [rbx]
004E5526  44 89 68 30                     mov dword ptr [rax + 0x30], r13d
004E552A  41 8A D6                        mov dl, r14b
004E552D  48 8B 0B                        mov rcx, qword ptr [rbx]
004E5530  E8 8B 60 DB FF                  call 0x14029b5c0
004E5535  4C 89 2B                        mov qword ptr [rbx], r13
004E5538  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E553E  83 E0 20                        and eax, 0x20
004E5541  0D 40 70 80 00                  or eax, 0x807040
004E5546  E9 94 02 00 00                  jmp 0x1404e57df
004E554B  83 3D FE 16 92 00 05            cmp dword ptr [rip + 0x9216fe], 5
004E5552  0F 86 BC 00 00 00               jbe 0x1404e5614
004E5558  44 89 BC 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r15d
004E5560  48 8D 84 24 D8 00 00 00         lea rax, [rsp + 0xd8]
004E5568  48 89 84 24 60 08 00 00         mov qword ptr [rsp + 0x860], rax
004E5570  48 C7 84 24 68 08 00 00 04 00 00 00  mov qword ptr [rsp + 0x868], 4
004E557C  89 B4 24 DC 00 00 00            mov dword ptr [rsp + 0xdc], esi
004E5583  48 8D 84 24 DC 00 00 00         lea rax, [rsp + 0xdc]
004E558B  48 89 84 24 70 08 00 00         mov qword ptr [rsp + 0x870], rax
004E5593  48 C7 84 24 78 08 00 00 04 00 00 00  mov qword ptr [rsp + 0x878], 4
004E559F  48 89 9C 24 08 02 00 00         mov qword ptr [rsp + 0x208], rbx
004E55A7  48 8D 84 24 08 02 00 00         lea rax, [rsp + 0x208]
004E55AF  48 89 84 24 80 08 00 00         mov qword ptr [rsp + 0x880], rax
004E55B7  48 C7 84 24 88 08 00 00 08 00 00 00  mov qword ptr [rsp + 0x888], 8
004E55C3  89 8C 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], ecx
004E55CA  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
004E55D2  48 89 84 24 90 08 00 00         mov qword ptr [rsp + 0x890], rax
004E55DA  48 C7 84 24 98 08 00 00 04 00 00 00  mov qword ptr [rsp + 0x898], 4
004E55E6  48 8D 84 24 40 08 00 00         lea rax, [rsp + 0x840]
004E55EE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E55F3  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E55FB  45 33 C9                        xor r9d, r9d
004E55FE  45 33 C0                        xor r8d, r8d
004E5601  48 8D 15 56 F2 B5 FF            lea rdx, [rip - 0x4a0daa]
004E5608  48 8D 0D 41 16 92 00            lea rcx, [rip + 0x921641]
004E560F  E8 CC 0A F4 FF                  call 0x1404260e0
004E5614  8B C6                           mov eax, esi
004E5616  41 23 C4                        and eax, r12d
004E5619  41 3B C4                        cmp eax, r12d
004E561C  0F 85 9A 00 00 00               jne 0x1404e56bc
004E5622  48 8B 3B                        mov rdi, qword ptr [rbx]
004E5625  B9 07 00 00 00                  mov ecx, 7
004E562A  E8 51 E7 D8 FF                  call 0x140273d80
004E562F  88 47 45                        mov byte ptr [rdi + 0x45], al
004E5632  45 33 ED                        xor r13d, r13d
004E5635  41 8B C5                        mov eax, r13d
004E5638  48 87 47 68                     xchg qword ptr [rdi + 0x68], rax
004E563C  8A 57 45                        mov dl, byte ptr [rdi + 0x45]
004E563F  41 8D 4D 07                     lea ecx, [r13 + 7]
004E5643  E8 F8 CE D8 FF                  call 0x140272540
004E5648  44 38 6F 44                     cmp byte ptr [rdi + 0x44], r13b
004E564C  0F 85 A3 00 00 00               jne 0x1404e56f5
004E5652  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
004E5656  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
004E565E  0F 57 C0                        xorps xmm0, xmm0
004E5661  33 C0                           xor eax, eax
004E5663  0F 11 01                        movups xmmword ptr [rcx], xmm0
004E5666  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
004E566A  45 8D 75 01                     lea r14d, [r13 + 1]
004E566E  C7 01 01 00 18 00               mov dword ptr [rcx], 0x180001
004E5674  45 8D 45 18                     lea r8d, [r13 + 0x18]
004E5678  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E567E  C1 E8 0C                        shr eax, 0xc
004E5681  83 E0 07                        and eax, 7
004E5684  89 41 04                        mov dword ptr [rcx + 4], eax
004E5687  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
004E568A  41 0B C6                        or eax, r14d
004E568D  89 41 0C                        mov dword ptr [rcx + 0xc], eax
004E5690  4C 89 47 38                     mov qword ptr [rdi + 0x38], r8
004E5694  48 8B 03                        mov rax, qword ptr [rbx]
004E5697  44 89 68 30                     mov dword ptr [rax + 0x30], r13d
004E569B  41 8A D6                        mov dl, r14b
004E569E  48 8B 0B                        mov rcx, qword ptr [rbx]
004E56A1  E8 1A 5F DB FF                  call 0x14029b5c0
004E56A6  4C 89 2B                        mov qword ptr [rbx], r13
004E56A9  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E56AF  83 E0 20                        and eax, 0x20
004E56B2  0D 40 50 80 00                  or eax, 0x805040
004E56B7  E9 23 01 00 00                  jmp 0x1404e57df
004E56BC  41 85 F6                        test r14d, esi
004E56BF  0F 84 35 0B 00 00               je 0x1404e61fa
004E56C5  48 8B 3B                        mov rdi, qword ptr [rbx]
004E56C8  B9 07 00 00 00                  mov ecx, 7
004E56CD  E8 AE E6 D8 FF                  call 0x140273d80
004E56D2  88 47 45                        mov byte ptr [rdi + 0x45], al
004E56D5  45 33 ED                        xor r13d, r13d
004E56D8  41 8B C5                        mov eax, r13d
004E56DB  48 87 47 68                     xchg qword ptr [rdi + 0x68], rax
004E56DF  8A 57 45                        mov dl, byte ptr [rdi + 0x45]
004E56E2  41 8D 4D 07                     lea ecx, [r13 + 7]
004E56E6  E8 55 CE D8 FF                  call 0x140272540
004E56EB  44 38 6F 44                     cmp byte ptr [rdi + 0x44], r13b
004E56EF  0F 84 81 00 00 00               je 0x1404e5776
004E56F5  45 33 C0                        xor r8d, r8d
004E56F8  33 D2                           xor edx, edx
004E56FA  48 8B CB                        mov rcx, rbx
004E56FD  E8 96 59 FA FF                  call 0x14048b098
004E5702  33 D2                           xor edx, edx
004E5704  48 8B CB                        mov rcx, rbx
004E5707  E8 DC 04 D8 FF                  call 0x140265be8
004E570C  44 88 6B 20                     mov byte ptr [rbx + 0x20], r13b
004E5710  48 8B 03                        mov rax, qword ptr [rbx]
004E5713  48 39 58 38                     cmp qword ptr [rax + 0x38], rbx
004E5717  75 04                           jne 0x1404e571d
004E5719  4C 89 68 38                     mov qword ptr [rax + 0x38], r13
004E571D  48 8B 03                        mov rax, qword ptr [rbx]
004E5720  41 BE 01 00 00 00               mov r14d, 1
004E5726  C7 40 30 20 01 00 C0            mov dword ptr [rax + 0x30], 0xc0000120
004E572D  41 8A D6                        mov dl, r14b
004E5730  48 8B 0B                        mov rcx, qword ptr [rbx]
004E5733  E8 88 5E DB FF                  call 0x14029b5c0
004E5738  4C 89 2B                        mov qword ptr [rbx], r13
004E573B  BA 44 66 6C 74                  mov edx, 0x746c6644
004E5740  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
004E5744  E8 97 21 E1 FF                  call 0x1402f78e0
004E5749  4C 89 6B 08                     mov qword ptr [rbx + 8], r13
004E574D  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E5753  83 E0 20                        and eax, 0x20
004E5756  41 0B C6                        or eax, r14d
004E5759  89 83 90 00 00 00               mov dword ptr [rbx + 0x90], eax
004E575F  48 8D 43 58                     lea rax, [rbx + 0x58]
004E5763  48 8B 08                        mov rcx, qword ptr [rax]
004E5766  48 3B C8                        cmp rcx, rax
004E5769  0F 84 79 0A 00 00               je 0x1404e61e8
004E576F  E8 4C 08 F4 FF                  call 0x140425fc0
004E5774  EB E9                           jmp 0x1404e575f
004E5776  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
004E577A  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
004E5782  0F 57 C0                        xorps xmm0, xmm0
004E5785  33 C0                           xor eax, eax
004E5787  0F 11 01                        movups xmmword ptr [rcx], xmm0
004E578A  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
004E578E  44 8D 70 01                     lea r14d, [rax + 1]
004E5792  C7 01 01 00 18 00               mov dword ptr [rcx], 0x180001
004E5798  44 8D 40 18                     lea r8d, [rax + 0x18]
004E579C  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E57A2  C1 E8 0C                        shr eax, 0xc
004E57A5  83 E0 07                        and eax, 7
004E57A8  89 41 04                        mov dword ptr [rcx + 4], eax
004E57AB  44 89 71 08                     mov dword ptr [rcx + 8], r14d
004E57AF  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
004E57B2  41 0B C6                        or eax, r14d
004E57B5  89 41 0C                        mov dword ptr [rcx + 0xc], eax
004E57B8  4C 89 47 38                     mov qword ptr [rdi + 0x38], r8
004E57BC  48 8B 03                        mov rax, qword ptr [rbx]
004E57BF  44 89 68 30                     mov dword ptr [rax + 0x30], r13d
004E57C3  41 8A D6                        mov dl, r14b
004E57C6  48 8B 0B                        mov rcx, qword ptr [rbx]
004E57C9  E8 F2 5D DB FF                  call 0x14029b5c0
004E57CE  4C 89 2B                        mov qword ptr [rbx], r13
004E57D1  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E57D7  83 E0 20                        and eax, 0x20
004E57DA  0D 40 50 10 00                  or eax, 0x105040
004E57DF  89 83 90 00 00 00               mov dword ptr [rbx + 0x90], eax
004E57E5  44 88 74 24 60                  mov byte ptr [rsp + 0x60], r14b
004E57EA  E9 F9 09 00 00                  jmp 0x1404e61e8
004E57EF  83 3D 5A 14 92 00 05            cmp dword ptr [rip + 0x92145a], 5
004E57F6  0F 86 BC 00 00 00               jbe 0x1404e58b8
004E57FC  44 89 BC 24 E4 00 00 00         mov dword ptr [rsp + 0xe4], r15d
004E5804  48 8D 84 24 E4 00 00 00         lea rax, [rsp + 0xe4]
004E580C  48 89 84 24 C0 08 00 00         mov qword ptr [rsp + 0x8c0], rax
004E5814  48 C7 84 24 C8 08 00 00 04 00 00 00  mov qword ptr [rsp + 0x8c8], 4
004E5820  89 B4 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], esi
004E5827  48 8D 84 24 E8 00 00 00         lea rax, [rsp + 0xe8]
004E582F  48 89 84 24 D0 08 00 00         mov qword ptr [rsp + 0x8d0], rax
004E5837  48 C7 84 24 D8 08 00 00 04 00 00 00  mov qword ptr [rsp + 0x8d8], 4
004E5843  48 89 9C 24 10 02 00 00         mov qword ptr [rsp + 0x210], rbx
004E584B  48 8D 84 24 10 02 00 00         lea rax, [rsp + 0x210]
004E5853  48 89 84 24 E0 08 00 00         mov qword ptr [rsp + 0x8e0], rax
004E585B  48 C7 84 24 E8 08 00 00 08 00 00 00  mov qword ptr [rsp + 0x8e8], 8
004E5867  89 8C 24 EC 00 00 00            mov dword ptr [rsp + 0xec], ecx
004E586E  48 8D 84 24 EC 00 00 00         lea rax, [rsp + 0xec]
004E5876  48 89 84 24 F0 08 00 00         mov qword ptr [rsp + 0x8f0], rax
004E587E  48 C7 84 24 F8 08 00 00 04 00 00 00  mov qword ptr [rsp + 0x8f8], 4
004E588A  48 8D 84 24 A0 08 00 00         lea rax, [rsp + 0x8a0]
004E5892  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E5897  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E589F  45 33 C9                        xor r9d, r9d
004E58A2  45 33 C0                        xor r8d, r8d
004E58A5  48 8D 15 E6 F3 B5 FF            lea rdx, [rip - 0x4a0c1a]
004E58AC  48 8D 0D 9D 13 92 00            lea rcx, [rip + 0x92139d]
004E58B3  E8 28 08 F4 FF                  call 0x1404260e0
004E58B8  41 85 F5                        test r13d, esi
004E58BB  0F 84 60 01 00 00               je 0x1404e5a21
004E58C1  4C 8B 73 28                     mov r14, qword ptr [rbx + 0x28]
004E58C5  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
004E58CD  48 8D 43 28                     lea rax, [rbx + 0x28]
004E58D1  4C 3B F0                        cmp r14, rax
004E58D4  0F 84 47 01 00 00               je 0x1404e5a21
004E58DA  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
004E58DE  81 7A 18 40 02 09 00            cmp dword ptr [rdx + 0x18], 0x90240
004E58E5  0F 85 2E 01 00 00               jne 0x1404e5a19
004E58EB  45 33 ED                        xor r13d, r13d
004E58EE  44 39 6C 24 78                  cmp dword ptr [rsp + 0x78], r13d
004E58F3  75 21                           jne 0x1404e5916
004E58F5  45 8B C7                        mov r8d, r15d
004E58F8  48 8B 52 30                     mov rdx, qword ptr [rdx + 0x30]
004E58FC  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
004E5904  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
004E5908  E8 A3 CD F0 FF                  call 0x1403f26b0
004E590D  84 C0                           test al, al
004E590F  74 05                           je 0x1404e5916
004E5911  E9 03 01 00 00                  jmp 0x1404e5a19
004E5916  41 F7 C7 00 00 01 10            test r15d, 0x10010000
004E591D  75 1E                           jne 0x1404e593d
004E591F  4D 8B 76 08                     mov r14, qword ptr [r14 + 8]
004E5923  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
004E592B  4C 8B CB                        mov r9, rbx
004E592E  45 33 C0                        xor r8d, r8d
004E5931  33 D2                           xor edx, edx
004E5933  49 8B 0E                        mov rcx, qword ptr [r14]
004E5936  E8 21 F0 FC FF                  call 0x1404b495c
004E593B  EB D4                           jmp 0x1404e5911
004E593D  83 3D 0C 13 92 00 03            cmp dword ptr [rip + 0x92130c], 3
004E5944  0F 86 3B F5 FF FF               jbe 0x1404e4e85
004E594A  C7 84 24 F0 00 00 00 09 09 00 C0  mov dword ptr [rsp + 0xf0], 0xc0000909
004E5955  48 8D 84 24 F0 00 00 00         lea rax, [rsp + 0xf0]
004E595D  48 89 84 24 20 04 00 00         mov qword ptr [rsp + 0x420], rax
004E5965  48 C7 84 24 28 04 00 00 04 00 00 00  mov qword ptr [rsp + 0x428], 4
004E5971  44 89 BC 24 F4 00 00 00         mov dword ptr [rsp + 0xf4], r15d
004E5979  48 8D 84 24 F4 00 00 00         lea rax, [rsp + 0xf4]
004E5981  48 89 84 24 30 04 00 00         mov qword ptr [rsp + 0x430], rax
004E5989  48 C7 84 24 38 04 00 00 04 00 00 00  mov qword ptr [rsp + 0x438], 4
004E5995  89 B4 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], esi
004E599C  48 8D 84 24 F8 00 00 00         lea rax, [rsp + 0xf8]
004E59A4  48 89 84 24 40 04 00 00         mov qword ptr [rsp + 0x440], rax
004E59AC  48 C7 84 24 48 04 00 00 04 00 00 00  mov qword ptr [rsp + 0x448], 4
004E59B8  48 89 9C 24 18 02 00 00         mov qword ptr [rsp + 0x218], rbx
004E59C0  48 8D 84 24 18 02 00 00         lea rax, [rsp + 0x218]
004E59C8  48 89 84 24 50 04 00 00         mov qword ptr [rsp + 0x450], rax
004E59D0  48 C7 84 24 58 04 00 00 08 00 00 00  mov qword ptr [rsp + 0x458], 8
004E59DC  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E59E2  89 84 24 FC 00 00 00            mov dword ptr [rsp + 0xfc], eax
004E59E9  48 8D 84 24 FC 00 00 00         lea rax, [rsp + 0xfc]
004E59F1  48 89 84 24 60 04 00 00         mov qword ptr [rsp + 0x460], rax
004E59F9  48 C7 84 24 68 04 00 00 04 00 00 00  mov qword ptr [rsp + 0x468], 4
004E5A05  48 8D 84 24 00 04 00 00         lea rax, [rsp + 0x400]
004E5A0D  48 8D 15 BA F3 B5 FF            lea rdx, [rip - 0x4a0c46]
004E5A14  E9 4D F4 FF FF                  jmp 0x1404e4e66
004E5A19  4D 8B 36                        mov r14, qword ptr [r14]
004E5A1C  E9 A4 FE FF FF                  jmp 0x1404e58c5
004E5A21  8B 8B 90 00 00 00               mov ecx, dword ptr [rbx + 0x90]
004E5A27  8B C1                           mov eax, ecx
004E5A29  25 DF FF F0 01                  and eax, 0x1f0ffdf
004E5A2E  3D 00 B0 00 00                  cmp eax, 0xb000
004E5A33  0F 85 B9 07 00 00               jne 0x1404e61f2
004E5A39  83 3D 10 12 92 00 05            cmp dword ptr [rip + 0x921210], 5
004E5A40  0F 86 C1 00 00 00               jbe 0x1404e5b07
004E5A46  44 89 BC 24 00 01 00 00         mov dword ptr [rsp + 0x100], r15d
004E5A4E  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
004E5A56  48 89 84 24 20 09 00 00         mov qword ptr [rsp + 0x920], rax
004E5A5E  48 C7 84 24 28 09 00 00 04 00 00 00  mov qword ptr [rsp + 0x928], 4
004E5A6A  45 33 ED                        xor r13d, r13d
004E5A6D  89 B4 24 04 01 00 00            mov dword ptr [rsp + 0x104], esi
004E5A74  48 8D 84 24 04 01 00 00         lea rax, [rsp + 0x104]
004E5A7C  48 89 84 24 30 09 00 00         mov qword ptr [rsp + 0x930], rax
004E5A84  48 C7 84 24 38 09 00 00 04 00 00 00  mov qword ptr [rsp + 0x938], 4
004E5A90  48 89 9C 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rbx
004E5A98  48 8D 84 24 E0 01 00 00         lea rax, [rsp + 0x1e0]
004E5AA0  48 89 84 24 40 09 00 00         mov qword ptr [rsp + 0x940], rax
004E5AA8  48 C7 84 24 48 09 00 00 08 00 00 00  mov qword ptr [rsp + 0x948], 8
004E5AB4  89 8C 24 08 01 00 00            mov dword ptr [rsp + 0x108], ecx
004E5ABB  48 8D 84 24 08 01 00 00         lea rax, [rsp + 0x108]
004E5AC3  48 89 84 24 50 09 00 00         mov qword ptr [rsp + 0x950], rax
004E5ACB  48 C7 84 24 58 09 00 00 04 00 00 00  mov qword ptr [rsp + 0x958], 4
004E5AD7  48 8D 84 24 00 09 00 00         lea rax, [rsp + 0x900]
004E5ADF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E5AE4  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E5AEC  45 33 C9                        xor r9d, r9d
004E5AEF  45 33 C0                        xor r8d, r8d
004E5AF2  48 8D 15 6C F2 B5 FF            lea rdx, [rip - 0x4a0d94]
004E5AF9  48 8D 0D 50 11 92 00            lea rcx, [rip + 0x921150]
004E5B00  E8 DB 05 F4 FF                  call 0x1404260e0
004E5B05  EB 03                           jmp 0x1404e5b0a
004E5B07  45 33 ED                        xor r13d, r13d
004E5B0A  81 FE 00 20 00 00               cmp esi, 0x2000
004E5B10  0F 85 26 03 00 00               jne 0x1404e5e3c
004E5B16  4C 8B 63 38                     mov r12, qword ptr [rbx + 0x38]
004E5B1A  41 BE 80 00 00 40               mov r14d, 0x40000080
004E5B20  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
004E5B28  48 8D 43 38                     lea rax, [rbx + 0x38]
004E5B2C  4C 3B E0                        cmp r12, rax
004E5B2F  0F 84 37 06 00 00               je 0x1404e616c
004E5B35  4C 89 A4 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], r12
004E5B3D  33 C0                           xor eax, eax
004E5B3F  39 44 24 78                     cmp dword ptr [rsp + 0x78], eax
004E5B43  75 25                           jne 0x1404e5b6a
004E5B45  49 8B 54 24 18                  mov rdx, qword ptr [r12 + 0x18]
004E5B4A  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
004E5B52  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
004E5B56  45 33 C0                        xor r8d, r8d
004E5B59  E8 52 CB F0 FF                  call 0x1403f26b0
004E5B5E  84 C0                           test al, al
004E5B60  74 08                           je 0x1404e5b6a
004E5B62  45 33 ED                        xor r13d, r13d
004E5B65  E9 ED 01 00 00                  jmp 0x1404e5d57
004E5B6A  41 8B C7                        mov eax, r15d
004E5B6D  41 23 C6                        and eax, r14d
004E5B70  41 3B C6                        cmp eax, r14d
004E5B73  75 32                           jne 0x1404e5ba7
004E5B75  48 8B 84 24 E8 0C 00 00         mov rax, qword ptr [rsp + 0xce8]
004E5B7D  44 0F B7 08                     movzx r9d, word ptr [rax]
004E5B81  48 8B 84 24 E0 0C 00 00         mov rax, qword ptr [rsp + 0xce0]
004E5B89  44 8B 00                        mov r8d, dword ptr [rax]
004E5B8C  49 8B 54 24 18                  mov rdx, qword ptr [r12 + 0x18]
004E5B91  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004E5B96  E8 7D 4B FD FF                  call 0x1404ba718
004E5B9B  45 33 ED                        xor r13d, r13d
004E5B9E  85 C0                           test eax, eax
004E5BA0  78 08                           js 0x1404e5baa
004E5BA2  E9 B0 01 00 00                  jmp 0x1404e5d57
004E5BA7  45 33 ED                        xor r13d, r13d
004E5BAA  41 F7 C7 00 00 01 10            test r15d, 0x10010000
004E5BB1  0F 85 A9 01 00 00               jne 0x1404e5d60
004E5BB7  4D 39 6C 24 38                  cmp qword ptr [r12 + 0x38], r13
004E5BBC  0F 84 EC 00 00 00               je 0x1404e5cae
004E5BC2  83 3D 87 10 92 00 05            cmp dword ptr [rip + 0x921087], 5
004E5BC9  0F 86 C2 00 00 00               jbe 0x1404e5c91
004E5BCF  44 89 BC 24 0C 01 00 00         mov dword ptr [rsp + 0x10c], r15d
004E5BD7  48 8D 84 24 0C 01 00 00         lea rax, [rsp + 0x10c]
004E5BDF  48 89 84 24 80 09 00 00         mov qword ptr [rsp + 0x980], rax
004E5BE7  48 C7 84 24 88 09 00 00 04 00 00 00  mov qword ptr [rsp + 0x988], 4
004E5BF3  89 B4 24 10 01 00 00            mov dword ptr [rsp + 0x110], esi
004E5BFA  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
004E5C02  48 89 84 24 90 09 00 00         mov qword ptr [rsp + 0x990], rax
004E5C0A  48 C7 84 24 98 09 00 00 04 00 00 00  mov qword ptr [rsp + 0x998], 4
004E5C16  48 89 9C 24 28 02 00 00         mov qword ptr [rsp + 0x228], rbx
004E5C1E  48 8D 84 24 28 02 00 00         lea rax, [rsp + 0x228]
004E5C26  48 89 84 24 A0 09 00 00         mov qword ptr [rsp + 0x9a0], rax
004E5C2E  48 C7 84 24 A8 09 00 00 08 00 00 00  mov qword ptr [rsp + 0x9a8], 8
004E5C3A  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E5C40  89 84 24 14 01 00 00            mov dword ptr [rsp + 0x114], eax
004E5C47  48 8D 84 24 14 01 00 00         lea rax, [rsp + 0x114]
004E5C4F  48 89 84 24 B0 09 00 00         mov qword ptr [rsp + 0x9b0], rax
004E5C57  48 C7 84 24 B8 09 00 00 04 00 00 00  mov qword ptr [rsp + 0x9b8], 4
004E5C63  48 8D 84 24 60 09 00 00         lea rax, [rsp + 0x960]
004E5C6B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E5C70  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E5C78  45 33 C9                        xor r9d, r9d
004E5C7B  45 33 C0                        xor r8d, r8d
004E5C7E  48 8D 15 21 F5 B5 FF            lea rdx, [rip - 0x4a0adf]
004E5C85  48 8D 0D C4 0F 92 00            lea rcx, [rip + 0x920fc4]
004E5C8C  E8 4F 04 F4 FF                  call 0x1404260e0
004E5C91  B8 01 00 00 00                  mov eax, 1
004E5C96  88 44 24 60                     mov byte ptr [rsp + 0x60], al
004E5C9A  49 8D 4C 24 48                  lea rcx, [r12 + 0x48]
004E5C9F  49 8B 54 24 58                  mov rdx, qword ptr [r12 + 0x58]
004E5CA4  E8 0B FC 22 00                  call 0x1407158b4
004E5CA9  E9 F4 FE FF FF                  jmp 0x1404e5ba2
004E5CAE  4D 8B 64 24 08                  mov r12, qword ptr [r12 + 8]
004E5CB3  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
004E5CBB  B8 01 00 00 00                  mov eax, 1
004E5CC0  8B D0                           mov edx, eax
004E5CC2  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
004E5CC9  41 8B C5                        mov eax, r13d
004E5CCC  41 0F B7 CD                     movzx ecx, r13w
004E5CD0  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
004E5CD8  45 38 28                        cmp byte ptr [r8], r13b
004E5CDB  75 1C                           jne 0x1404e5cf9
004E5CDD  BA 03 00 00 00                  mov edx, 3
004E5CE2  89 94 24 18 01 00 00            mov dword ptr [rsp + 0x118], edx
004E5CE9  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
004E5CED  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
004E5CF1  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
004E5CF4  41 0F B7 48 1A                  movzx ecx, word ptr [r8 + 0x1a]
004E5CF9  44 88 6C 24 38                  mov byte ptr [rsp + 0x38], r13b
004E5CFE  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
004E5D03  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
004E5D07  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
004E5D0B  41 B9 00 10 00 00               mov r9d, 0x1000
004E5D11  45 33 C0                        xor r8d, r8d
004E5D14  48 8B D3                        mov rdx, rbx
004E5D17  49 8B 0C 24                     mov rcx, qword ptr [r12]
004E5D1B  E8 44 FC F3 FF                  call 0x140425964
004E5D20  84 C0                           test al, al
004E5D22  B8 01 00 00 00                  mov eax, 1
004E5D27  74 2A                           je 0x1404e5d53
004E5D29  44 88 6C 24 71                  mov byte ptr [rsp + 0x71], r13b
004E5D2E  88 44 24 60                     mov byte ptr [rsp + 0x60], al
004E5D32  44 39 6C 24 78                  cmp dword ptr [rsp + 0x78], r13d
004E5D37  0F 95 44 24 72                  setne byte ptr [rsp + 0x72]
004E5D3C  48 8B 84 24 E0 01 00 00         mov rax, qword ptr [rsp + 0x1e0]
004E5D44  48 8D 48 48                     lea rcx, [rax + 0x48]
004E5D48  48 8B 50 58                     mov rdx, qword ptr [rax + 0x58]
004E5D4C  E8 63 FB 22 00                  call 0x1407158b4
004E5D51  EB 04                           jmp 0x1404e5d57
004E5D53  88 44 24 70                     mov byte ptr [rsp + 0x70], al
004E5D57  4D 8B 24 24                     mov r12, qword ptr [r12]
004E5D5B  E9 C0 FD FF FF                  jmp 0x1404e5b20
004E5D60  83 3D E9 0E 92 00 03            cmp dword ptr [rip + 0x920ee9], 3
004E5D67  0F 86 18 F1 FF FF               jbe 0x1404e4e85
004E5D6D  C7 84 24 1C 01 00 00 09 09 00 C0  mov dword ptr [rsp + 0x11c], 0xc0000909
004E5D78  48 8D 84 24 1C 01 00 00         lea rax, [rsp + 0x11c]
004E5D80  48 89 84 24 E0 05 00 00         mov qword ptr [rsp + 0x5e0], rax
004E5D88  48 C7 84 24 E8 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x5e8], 4
004E5D94  44 89 BC 24 20 01 00 00         mov dword ptr [rsp + 0x120], r15d
004E5D9C  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
004E5DA4  48 89 84 24 F0 05 00 00         mov qword ptr [rsp + 0x5f0], rax
004E5DAC  48 C7 84 24 F8 05 00 00 04 00 00 00  mov qword ptr [rsp + 0x5f8], 4
004E5DB8  89 B4 24 24 01 00 00            mov dword ptr [rsp + 0x124], esi
004E5DBF  48 8D 84 24 24 01 00 00         lea rax, [rsp + 0x124]
004E5DC7  48 89 84 24 00 06 00 00         mov qword ptr [rsp + 0x600], rax
004E5DCF  48 C7 84 24 08 06 00 00 04 00 00 00  mov qword ptr [rsp + 0x608], 4
004E5DDB  48 89 9C 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rbx
004E5DE3  48 8D 84 24 E8 01 00 00         lea rax, [rsp + 0x1e8]
004E5DEB  48 89 84 24 10 06 00 00         mov qword ptr [rsp + 0x610], rax
004E5DF3  48 C7 84 24 18 06 00 00 08 00 00 00  mov qword ptr [rsp + 0x618], 8
004E5DFF  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E5E05  89 84 24 28 01 00 00            mov dword ptr [rsp + 0x128], eax
004E5E0C  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
004E5E14  48 89 84 24 20 06 00 00         mov qword ptr [rsp + 0x620], rax
004E5E1C  48 C7 84 24 28 06 00 00 04 00 00 00  mov qword ptr [rsp + 0x628], 4
004E5E28  48 8D 84 24 C0 05 00 00         lea rax, [rsp + 0x5c0]
004E5E30  48 8D 15 E0 F3 B5 FF            lea rdx, [rip - 0x4a0c20]
004E5E37  E9 2A F0 FF FF                  jmp 0x1404e4e66
004E5E3C  8B C6                           mov eax, esi
004E5E3E  41 23 C4                        and eax, r12d
004E5E41  41 3B C4                        cmp eax, r12d
004E5E44  0F 85 22 03 00 00               jne 0x1404e616c
004E5E4A  4C 8B 73 48                     mov r14, qword ptr [rbx + 0x48]
004E5E4E  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
004E5E56  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
004E5E5B  48 8D 43 48                     lea rax, [rbx + 0x48]
004E5E5F  4C 3B F0                        cmp r14, rax
004E5E62  0F 84 3D 01 00 00               je 0x1404e5fa5
004E5E68  45 85 E4                        test r12d, r12d
004E5E6B  75 1C                           jne 0x1404e5e89
004E5E6D  45 8B C7                        mov r8d, r15d
004E5E70  49 8B 56 18                     mov rdx, qword ptr [r14 + 0x18]
004E5E74  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
004E5E7C  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
004E5E80  E8 2B C8 F0 FF                  call 0x1403f26b0
004E5E85  84 C0                           test al, al
004E5E87  75 33                           jne 0x1404e5ebc
004E5E89  41 F7 C7 00 00 01 10            test r15d, 0x10010000
004E5E90  75 37                           jne 0x1404e5ec9
004E5E92  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
004E5E96  25 FF FF 0F FF                  and eax, 0xff0fffff
004E5E9B  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
004E5E9F  0F BA E8 17                     bts eax, 0x17
004E5EA3  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
004E5EA7  0F BA E6 0D                     bt esi, 0xd
004E5EAB  0F B6 44 24 60                  movzx eax, byte ptr [rsp + 0x60]
004E5EB0  B9 01 00 00 00                  mov ecx, 1
004E5EB5  0F 42 C1                        cmovb eax, ecx
004E5EB8  88 44 24 60                     mov byte ptr [rsp + 0x60], al
004E5EBC  4D 8B 36                        mov r14, qword ptr [r14]
004E5EBF  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
004E5EC7  EB 92                           jmp 0x1404e5e5b
004E5EC9  83 3D 80 0D 92 00 03            cmp dword ptr [rip + 0x920d80], 3
004E5ED0  0F 86 AF EF FF FF               jbe 0x1404e4e85
004E5ED6  C7 84 24 2C 01 00 00 09 09 00 C0  mov dword ptr [rsp + 0x12c], 0xc0000909
004E5EE1  48 8D 84 24 2C 01 00 00         lea rax, [rsp + 0x12c]
004E5EE9  48 89 84 24 50 06 00 00         mov qword ptr [rsp + 0x650], rax
004E5EF1  48 C7 84 24 58 06 00 00 04 00 00 00  mov qword ptr [rsp + 0x658], 4
004E5EFD  44 89 BC 24 30 01 00 00         mov dword ptr [rsp + 0x130], r15d
004E5F05  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
004E5F0D  48 89 84 24 60 06 00 00         mov qword ptr [rsp + 0x660], rax
004E5F15  48 C7 84 24 68 06 00 00 04 00 00 00  mov qword ptr [rsp + 0x668], 4
004E5F21  89 B4 24 34 01 00 00            mov dword ptr [rsp + 0x134], esi
004E5F28  48 8D 84 24 34 01 00 00         lea rax, [rsp + 0x134]
004E5F30  48 89 84 24 70 06 00 00         mov qword ptr [rsp + 0x670], rax
004E5F38  48 C7 84 24 78 06 00 00 04 00 00 00  mov qword ptr [rsp + 0x678], 4
004E5F44  48 89 9C 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rbx
004E5F4C  48 8D 84 24 F0 01 00 00         lea rax, [rsp + 0x1f0]
004E5F54  48 89 84 24 80 06 00 00         mov qword ptr [rsp + 0x680], rax
004E5F5C  48 C7 84 24 88 06 00 00 08 00 00 00  mov qword ptr [rsp + 0x688], 8
004E5F68  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E5F6E  89 84 24 38 01 00 00            mov dword ptr [rsp + 0x138], eax
004E5F75  48 8D 84 24 38 01 00 00         lea rax, [rsp + 0x138]
004E5F7D  48 89 84 24 90 06 00 00         mov qword ptr [rsp + 0x690], rax
004E5F85  48 C7 84 24 98 06 00 00 04 00 00 00  mov qword ptr [rsp + 0x698], 4
004E5F91  48 8D 84 24 30 06 00 00         lea rax, [rsp + 0x630]
004E5F99  48 8D 15 4D F3 B5 FF            lea rdx, [rip - 0x4a0cb3]
004E5FA0  E9 C1 EE FF FF                  jmp 0x1404e4e66
004E5FA5  4C 8B 73 38                     mov r14, qword ptr [rbx + 0x38]
004E5FA9  33 C9                           xor ecx, ecx
004E5FAB  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
004E5FB3  48 8D 43 38                     lea rax, [rbx + 0x38]
004E5FB7  4C 3B F0                        cmp r14, rax
004E5FBA  0F 84 A9 01 00 00               je 0x1404e6169
004E5FC0  4D 8B EE                        mov r13, r14
004E5FC3  45 85 E4                        test r12d, r12d
004E5FC6  75 1E                           jne 0x1404e5fe6
004E5FC8  45 8B C7                        mov r8d, r15d
004E5FCB  49 8B 56 18                     mov rdx, qword ptr [r14 + 0x18]
004E5FCF  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
004E5FD7  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
004E5FDB  E8 D0 C6 F0 FF                  call 0x1403f26b0
004E5FE0  33 C9                           xor ecx, ecx
004E5FE2  84 C0                           test al, al
004E5FE4  75 31                           jne 0x1404e6017
004E5FE6  41 F7 C7 00 00 01 10            test r15d, 0x10010000
004E5FED  0F 85 9A 00 00 00               jne 0x1404e608d
004E5FF3  49 39 4E 38                     cmp qword ptr [r14 + 0x38], rcx
004E5FF7  74 20                           je 0x1404e6019
004E5FF9  0F BA E6 0D                     bt esi, 0xd
004E5FFD  73 18                           jae 0x1404e6017
004E5FFF  B8 01 00 00 00                  mov eax, 1
004E6004  88 44 24 60                     mov byte ptr [rsp + 0x60], al
004E6008  49 8D 4E 48                     lea rcx, [r14 + 0x48]
004E600C  49 8B 56 58                     mov rdx, qword ptr [r14 + 0x58]
004E6010  E8 9F F8 22 00                  call 0x1407158b4
004E6015  33 C9                           xor ecx, ecx
004E6017  EB 6C                           jmp 0x1404e6085
004E6019  4D 8B 76 08                     mov r14, qword ptr [r14 + 8]
004E601D  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
004E6025  88 4C 24 38                     mov byte ptr [rsp + 0x38], cl
004E6029  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
004E602E  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
004E6032  B8 01 00 00 00                  mov eax, 1
004E6037  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
004E603B  45 33 C9                        xor r9d, r9d
004E603E  45 33 C0                        xor r8d, r8d
004E6041  48 8B D3                        mov rdx, rbx
004E6044  49 8B 0E                        mov rcx, qword ptr [r14]
004E6047  E8 18 F9 F3 FF                  call 0x140425964
004E604C  33 C9                           xor ecx, ecx
004E604E  84 C0                           test al, al
004E6050  74 2A                           je 0x1404e607c
004E6052  88 4C 24 71                     mov byte ptr [rsp + 0x71], cl
004E6056  0F BA E6 0D                     bt esi, 0xd
004E605A  73 16                           jae 0x1404e6072
004E605C  8D 41 01                        lea eax, [rcx + 1]
004E605F  88 44 24 60                     mov byte ptr [rsp + 0x60], al
004E6063  49 8D 4D 48                     lea rcx, [r13 + 0x48]
004E6067  49 8B 55 58                     mov rdx, qword ptr [r13 + 0x58]
004E606B  E8 44 F8 22 00                  call 0x1407158b4
004E6070  33 C9                           xor ecx, ecx
004E6072  45 85 E4                        test r12d, r12d
004E6075  0F 95 44 24 72                  setne byte ptr [rsp + 0x72]
004E607A  EB 09                           jmp 0x1404e6085
004E607C  B8 01 00 00 00                  mov eax, 1
004E6081  88 44 24 70                     mov byte ptr [rsp + 0x70], al
004E6085  4D 8B 36                        mov r14, qword ptr [r14]
004E6088  E9 1E FF FF FF                  jmp 0x1404e5fab
004E608D  83 3D BC 0B 92 00 03            cmp dword ptr [rip + 0x920bbc], 3
004E6094  0F 86 EB ED FF FF               jbe 0x1404e4e85
004E609A  C7 84 24 3C 01 00 00 09 09 00 C0  mov dword ptr [rsp + 0x13c], 0xc0000909
004E60A5  48 8D 84 24 3C 01 00 00         lea rax, [rsp + 0x13c]
004E60AD  48 89 84 24 C0 06 00 00         mov qword ptr [rsp + 0x6c0], rax
004E60B5  48 C7 84 24 C8 06 00 00 04 00 00 00  mov qword ptr [rsp + 0x6c8], 4
004E60C1  44 89 BC 24 40 01 00 00         mov dword ptr [rsp + 0x140], r15d
004E60C9  48 8D 84 24 40 01 00 00         lea rax, [rsp + 0x140]
004E60D1  48 89 84 24 D0 06 00 00         mov qword ptr [rsp + 0x6d0], rax
004E60D9  48 C7 84 24 D8 06 00 00 04 00 00 00  mov qword ptr [rsp + 0x6d8], 4
004E60E5  89 B4 24 44 01 00 00            mov dword ptr [rsp + 0x144], esi
004E60EC  48 8D 84 24 44 01 00 00         lea rax, [rsp + 0x144]
004E60F4  48 89 84 24 E0 06 00 00         mov qword ptr [rsp + 0x6e0], rax
004E60FC  48 C7 84 24 E8 06 00 00 04 00 00 00  mov qword ptr [rsp + 0x6e8], 4
004E6108  48 89 9C 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rbx
004E6110  48 8D 84 24 F8 01 00 00         lea rax, [rsp + 0x1f8]
004E6118  48 89 84 24 F0 06 00 00         mov qword ptr [rsp + 0x6f0], rax
004E6120  48 C7 84 24 F8 06 00 00 08 00 00 00  mov qword ptr [rsp + 0x6f8], 8
004E612C  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E6132  89 84 24 48 01 00 00            mov dword ptr [rsp + 0x148], eax
004E6139  48 8D 84 24 48 01 00 00         lea rax, [rsp + 0x148]
004E6141  48 89 84 24 00 07 00 00         mov qword ptr [rsp + 0x700], rax
004E6149  48 C7 84 24 08 07 00 00 04 00 00 00  mov qword ptr [rsp + 0x708], 4
004E6155  48 8D 84 24 A0 06 00 00         lea rax, [rsp + 0x6a0]
004E615D  48 8D 15 1E F1 B5 FF            lea rdx, [rip - 0x4a0ee2]
004E6164  E9 FD EC FF FF                  jmp 0x1404e4e66
004E6169  45 33 ED                        xor r13d, r13d
004E616C  44 38 6C 24 70                  cmp byte ptr [rsp + 0x70], r13b
004E6171  74 08                           je 0x1404e617b
004E6173  48 8B CB                        mov rcx, rbx
004E6176  E8 41 FB F3 FF                  call 0x140425cbc
004E617B  44 38 6C 24 60                  cmp byte ptr [rsp + 0x60], r13b
004E6180  75 58                           jne 0x1404e61da
004E6182  48 8D 43 48                     lea rax, [rbx + 0x48]
004E6186  48 8B 38                        mov rdi, qword ptr [rax]
004E6189  48 3B F8                        cmp rdi, rax
004E618C  74 4C                           je 0x1404e61da
004E618E  0F BA E6 0D                     bt esi, 0xd
004E6192  73 46                           jae 0x1404e61da
004E6194  44 39 6C 24 78                  cmp dword ptr [rsp + 0x78], r13d
004E6199  75 2D                           jne 0x1404e61c8
004E619B  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
004E61A3  48 8D 43 48                     lea rax, [rbx + 0x48]
004E61A7  48 3B F8                        cmp rdi, rax
004E61AA  74 2E                           je 0x1404e61da
004E61AC  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
004E61B4  48 8B 50 30                     mov rdx, qword ptr [rax + 0x30]
004E61B8  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
004E61BC  45 33 C0                        xor r8d, r8d
004E61BF  E8 EC C4 F0 FF                  call 0x1403f26b0
004E61C4  84 C0                           test al, al
004E61C6  75 0D                           jne 0x1404e61d5
004E61C8  41 BE 01 00 00 00               mov r14d, 1
004E61CE  44 88 74 24 60                  mov byte ptr [rsp + 0x60], r14b
004E61D3  EB 0B                           jmp 0x1404e61e0
004E61D5  48 8B 3F                        mov rdi, qword ptr [rdi]
004E61D8  EB C1                           jmp 0x1404e619b
004E61DA  41 BE 01 00 00 00               mov r14d, 1
004E61E0  48 8B CB                        mov rcx, rbx
004E61E3  E8 04 F5 F3 FF                  call 0x1404256ec
004E61E8  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
004E61ED  E9 B3 F1 FF FF                  jmp 0x1404e53a5
004E61F2  48 8B CB                        mov rcx, rbx
004E61F5  E8 F2 F4 F3 FF                  call 0x1404256ec
004E61FA  45 33 ED                        xor r13d, r13d
004E61FD  E9 98 F1 FF FF                  jmp 0x1404e539a
004E6202  83 3D 47 0A 92 00 05            cmp dword ptr [rip + 0x920a47], 5
004E6209  0F 86 BC 00 00 00               jbe 0x1404e62cb
004E620F  44 89 BC 24 8C 01 00 00         mov dword ptr [rsp + 0x18c], r15d
004E6217  48 8D 84 24 8C 01 00 00         lea rax, [rsp + 0x18c]
004E621F  48 89 84 24 20 0C 00 00         mov qword ptr [rsp + 0xc20], rax
004E6227  48 C7 84 24 28 0C 00 00 04 00 00 00  mov qword ptr [rsp + 0xc28], 4
004E6233  89 B4 24 4C 01 00 00            mov dword ptr [rsp + 0x14c], esi
004E623A  48 8D 84 24 4C 01 00 00         lea rax, [rsp + 0x14c]
004E6242  48 89 84 24 30 0C 00 00         mov qword ptr [rsp + 0xc30], rax
004E624A  48 C7 84 24 38 0C 00 00 04 00 00 00  mov qword ptr [rsp + 0xc38], 4
004E6256  48 89 9C 24 48 02 00 00         mov qword ptr [rsp + 0x248], rbx
004E625E  48 8D 84 24 48 02 00 00         lea rax, [rsp + 0x248]
004E6266  48 89 84 24 40 0C 00 00         mov qword ptr [rsp + 0xc40], rax
004E626E  48 C7 84 24 48 0C 00 00 08 00 00 00  mov qword ptr [rsp + 0xc48], 8
004E627A  89 8C 24 50 01 00 00            mov dword ptr [rsp + 0x150], ecx
004E6281  48 8D 84 24 50 01 00 00         lea rax, [rsp + 0x150]
004E6289  48 89 84 24 50 0C 00 00         mov qword ptr [rsp + 0xc50], rax
004E6291  48 C7 84 24 58 0C 00 00 04 00 00 00  mov qword ptr [rsp + 0xc58], 4
004E629D  48 8D 84 24 00 0C 00 00         lea rax, [rsp + 0xc00]
004E62A5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E62AA  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E62B2  45 33 C9                        xor r9d, r9d
004E62B5  45 33 C0                        xor r8d, r8d
004E62B8  48 8D 15 77 E6 B5 FF            lea rdx, [rip - 0x4a1989]
004E62BF  48 8D 0D 8A 09 92 00            lea rcx, [rip + 0x92098a]
004E62C6  E8 15 FE F3 FF                  call 0x1404260e0
004E62CB  0F BA E6 0C                     bt esi, 0xc
004E62CF  73 14                           jae 0x1404e62e5
004E62D1  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E62D7  83 E0 20                        and eax, 0x20
004E62DA  0D 40 50 80 00                  or eax, 0x805040
004E62DF  89 83 90 00 00 00               mov dword ptr [rbx + 0x90], eax
004E62E5  41 BE 01 00 00 00               mov r14d, 1
004E62EB  45 33 ED                        xor r13d, r13d
004E62EE  41 85 F4                        test r12d, esi
004E62F1  0F 84 F1 FE FF FF               je 0x1404e61e8
004E62F7  E9 E9 F4 FF FF                  jmp 0x1404e57e5
004E62FC  3D 40 70 10 00                  cmp eax, 0x107040
004E6301  0F 84 D6 08 00 00               je 0x1404e6bdd
004E6307  3D 40 70 30 00                  cmp eax, 0x307040
004E630C  0F 84 78 07 00 00               je 0x1404e6a8a
004E6312  3D 40 70 50 00                  cmp eax, 0x507040
004E6317  0F 84 25 06 00 00               je 0x1404e6942
004E631D  3D 00 30 80 00                  cmp eax, 0x803000
004E6322  0F 84 B7 03 00 00               je 0x1404e66df
004E6328  3D 40 50 80 00                  cmp eax, 0x805040
004E632D  0F 84 DE 02 00 00               je 0x1404e6611
004E6333  3D 40 70 80 00                  cmp eax, 0x807040
004E6338  0F 84 B9 01 00 00               je 0x1404e64f7
004E633E  0F BA E1 18                     bt ecx, 0x18
004E6342  0F 83 E1 00 00 00               jae 0x1404e6429
004E6348  83 3D 01 09 92 00 05            cmp dword ptr [rip + 0x920901], 5
004E634F  0F 86 BC 00 00 00               jbe 0x1404e6411
004E6355  44 89 BC 24 54 01 00 00         mov dword ptr [rsp + 0x154], r15d
004E635D  48 8D 84 24 54 01 00 00         lea rax, [rsp + 0x154]
004E6365  48 89 84 24 A0 0A 00 00         mov qword ptr [rsp + 0xaa0], rax
004E636D  48 C7 84 24 A8 0A 00 00 04 00 00 00  mov qword ptr [rsp + 0xaa8], 4
004E6379  89 B4 24 58 01 00 00            mov dword ptr [rsp + 0x158], esi
004E6380  48 8D 84 24 58 01 00 00         lea rax, [rsp + 0x158]
004E6388  48 89 84 24 B0 0A 00 00         mov qword ptr [rsp + 0xab0], rax
004E6390  48 C7 84 24 B8 0A 00 00 04 00 00 00  mov qword ptr [rsp + 0xab8], 4
004E639C  48 89 9C 24 50 02 00 00         mov qword ptr [rsp + 0x250], rbx
004E63A4  48 8D 84 24 50 02 00 00         lea rax, [rsp + 0x250]
004E63AC  48 89 84 24 C0 0A 00 00         mov qword ptr [rsp + 0xac0], rax
004E63B4  48 C7 84 24 C8 0A 00 00 08 00 00 00  mov qword ptr [rsp + 0xac8], 8
004E63C0  89 8C 24 5C 01 00 00            mov dword ptr [rsp + 0x15c], ecx
004E63C7  48 8D 84 24 5C 01 00 00         lea rax, [rsp + 0x15c]
004E63CF  48 89 84 24 D0 0A 00 00         mov qword ptr [rsp + 0xad0], rax
004E63D7  48 C7 84 24 D8 0A 00 00 04 00 00 00  mov qword ptr [rsp + 0xad8], 4
004E63E3  48 8D 84 24 80 0A 00 00         lea rax, [rsp + 0xa80]
004E63EB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E63F0  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E63F8  45 33 C9                        xor r9d, r9d
004E63FB  45 33 C0                        xor r8d, r8d
004E63FE  48 8D 15 41 E7 B5 FF            lea rdx, [rip - 0x4a18bf]
004E6405  48 8D 0D 44 08 92 00            lea rcx, [rip + 0x920844]
004E640C  E8 CF FC F3 FF                  call 0x1404260e0
004E6411  41 BE 01 00 00 00               mov r14d, 1
004E6417  44 88 74 24 60                  mov byte ptr [rsp + 0x60], r14b
004E641C  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
004E6421  45 33 ED                        xor r13d, r13d
004E6424  E9 7C EF FF FF                  jmp 0x1404e53a5
004E6429  83 3D 20 08 92 00 02            cmp dword ptr [rip + 0x920820], 2
004E6430  0F 86 C4 FD FF FF               jbe 0x1404e61fa
004E6436  44 89 BC 24 60 01 00 00         mov dword ptr [rsp + 0x160], r15d
004E643E  48 8D 84 24 60 01 00 00         lea rax, [rsp + 0x160]
004E6446  48 89 84 24 00 0B 00 00         mov qword ptr [rsp + 0xb00], rax
004E644E  48 C7 84 24 08 0B 00 00 04 00 00 00  mov qword ptr [rsp + 0xb08], 4
004E645A  89 B4 24 64 01 00 00            mov dword ptr [rsp + 0x164], esi
004E6461  48 8D 84 24 64 01 00 00         lea rax, [rsp + 0x164]
004E6469  48 89 84 24 10 0B 00 00         mov qword ptr [rsp + 0xb10], rax
004E6471  48 C7 84 24 18 0B 00 00 04 00 00 00  mov qword ptr [rsp + 0xb18], 4
004E647D  48 89 9C 24 58 02 00 00         mov qword ptr [rsp + 0x258], rbx
004E6485  48 8D 84 24 58 02 00 00         lea rax, [rsp + 0x258]
004E648D  48 89 84 24 20 0B 00 00         mov qword ptr [rsp + 0xb20], rax
004E6495  48 C7 84 24 28 0B 00 00 08 00 00 00  mov qword ptr [rsp + 0xb28], 8
004E64A1  89 8C 24 68 01 00 00            mov dword ptr [rsp + 0x168], ecx
004E64A8  48 8D 84 24 68 01 00 00         lea rax, [rsp + 0x168]
004E64B0  48 89 84 24 30 0B 00 00         mov qword ptr [rsp + 0xb30], rax
004E64B8  48 C7 84 24 38 0B 00 00 04 00 00 00  mov qword ptr [rsp + 0xb38], 4
004E64C4  48 8D 84 24 E0 0A 00 00         lea rax, [rsp + 0xae0]
004E64CC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E64D1  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E64D9  45 33 C9                        xor r9d, r9d
004E64DC  45 33 C0                        xor r8d, r8d
004E64DF  48 8D 15 F3 E5 B5 FF            lea rdx, [rip - 0x4a1a0d]
004E64E6  48 8D 0D 63 07 92 00            lea rcx, [rip + 0x920763]
004E64ED  E8 EE FB F3 FF                  call 0x1404260e0
004E64F2  E9 03 FD FF FF                  jmp 0x1404e61fa
004E64F7  83 3D 52 07 92 00 05            cmp dword ptr [rip + 0x920752], 5
004E64FE  0F 86 BC 00 00 00               jbe 0x1404e65c0
004E6504  44 89 BC 24 6C 01 00 00         mov dword ptr [rsp + 0x16c], r15d
004E650C  48 8D 84 24 6C 01 00 00         lea rax, [rsp + 0x16c]
004E6514  48 89 84 24 60 0B 00 00         mov qword ptr [rsp + 0xb60], rax
004E651C  48 C7 84 24 68 0B 00 00 04 00 00 00  mov qword ptr [rsp + 0xb68], 4
004E6528  89 B4 24 70 01 00 00            mov dword ptr [rsp + 0x170], esi
004E652F  48 8D 84 24 70 01 00 00         lea rax, [rsp + 0x170]
004E6537  48 89 84 24 70 0B 00 00         mov qword ptr [rsp + 0xb70], rax
004E653F  48 C7 84 24 78 0B 00 00 04 00 00 00  mov qword ptr [rsp + 0xb78], 4
004E654B  48 89 9C 24 60 02 00 00         mov qword ptr [rsp + 0x260], rbx
004E6553  48 8D 84 24 60 02 00 00         lea rax, [rsp + 0x260]
004E655B  48 89 84 24 80 0B 00 00         mov qword ptr [rsp + 0xb80], rax
004E6563  48 C7 84 24 88 0B 00 00 08 00 00 00  mov qword ptr [rsp + 0xb88], 8
004E656F  89 8C 24 74 01 00 00            mov dword ptr [rsp + 0x174], ecx
004E6576  48 8D 84 24 74 01 00 00         lea rax, [rsp + 0x174]
004E657E  48 89 84 24 90 0B 00 00         mov qword ptr [rsp + 0xb90], rax
004E6586  48 C7 84 24 98 0B 00 00 04 00 00 00  mov qword ptr [rsp + 0xb98], 4
004E6592  48 8D 84 24 40 0B 00 00         lea rax, [rsp + 0xb40]
004E659A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E659F  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E65A7  45 33 C9                        xor r9d, r9d
004E65AA  45 33 C0                        xor r8d, r8d
004E65AD  48 8D 15 63 E1 B5 FF            lea rdx, [rip - 0x4a1e9d]
004E65B4  48 8D 0D 95 06 92 00            lea rcx, [rip + 0x920695]
004E65BB  E8 20 FB F3 FF                  call 0x1404260e0
004E65C0  41 8B C7                        mov eax, r15d
004E65C3  41 BE 80 00 00 40               mov r14d, 0x40000080
004E65C9  41 23 C6                        and eax, r14d
004E65CC  41 3B C6                        cmp eax, r14d
004E65CF  75 32                           jne 0x1404e6603
004E65D1  4C 8B 8C 24 E8 0C 00 00         mov r9, qword ptr [rsp + 0xce8]
004E65D9  45 0F B7 09                     movzx r9d, word ptr [r9]
004E65DD  4C 8B 84 24 E0 0C 00 00         mov r8, qword ptr [rsp + 0xce0]
004E65E5  45 8B 00                        mov r8d, dword ptr [r8]
004E65E8  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
004E65EC  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004E65F1  E8 22 41 FD FF                  call 0x1404ba718
004E65F6  45 33 ED                        xor r13d, r13d
004E65F9  85 C0                           test eax, eax
004E65FB  0F 89 99 ED FF FF               jns 0x1404e539a
004E6601  EB 03                           jmp 0x1404e6606
004E6603  45 33 ED                        xor r13d, r13d
004E6606  41 BE 01 00 00 00               mov r14d, 1
004E660C  E9 D4 F1 FF FF                  jmp 0x1404e57e5
004E6611  83 3D 38 06 92 00 05            cmp dword ptr [rip + 0x920638], 5
004E6618  0F 86 C7 FC FF FF               jbe 0x1404e62e5
004E661E  44 89 BC 24 78 01 00 00         mov dword ptr [rsp + 0x178], r15d
004E6626  48 8D 84 24 78 01 00 00         lea rax, [rsp + 0x178]
004E662E  48 89 84 24 C0 0B 00 00         mov qword ptr [rsp + 0xbc0], rax
004E6636  48 C7 84 24 C8 0B 00 00 04 00 00 00  mov qword ptr [rsp + 0xbc8], 4
004E6642  89 B4 24 7C 01 00 00            mov dword ptr [rsp + 0x17c], esi
004E6649  48 8D 84 24 7C 01 00 00         lea rax, [rsp + 0x17c]
004E6651  48 89 84 24 D0 0B 00 00         mov qword ptr [rsp + 0xbd0], rax
004E6659  48 C7 84 24 D8 0B 00 00 04 00 00 00  mov qword ptr [rsp + 0xbd8], 4
004E6665  48 89 9C 24 68 02 00 00         mov qword ptr [rsp + 0x268], rbx
004E666D  48 8D 84 24 68 02 00 00         lea rax, [rsp + 0x268]
004E6675  48 89 84 24 E0 0B 00 00         mov qword ptr [rsp + 0xbe0], rax
004E667D  48 C7 84 24 E8 0B 00 00 08 00 00 00  mov qword ptr [rsp + 0xbe8], 8
004E6689  89 8C 24 80 01 00 00            mov dword ptr [rsp + 0x180], ecx
004E6690  48 8D 84 24 80 01 00 00         lea rax, [rsp + 0x180]
004E6698  48 89 84 24 F0 0B 00 00         mov qword ptr [rsp + 0xbf0], rax
004E66A0  48 C7 84 24 F8 0B 00 00 04 00 00 00  mov qword ptr [rsp + 0xbf8], 4
004E66AC  48 8D 84 24 A0 0B 00 00         lea rax, [rsp + 0xba0]
004E66B4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E66B9  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E66C1  45 33 C9                        xor r9d, r9d
004E66C4  45 33 C0                        xor r8d, r8d
004E66C7  48 8D 15 F9 E1 B5 FF            lea rdx, [rip - 0x4a1e07]
004E66CE  48 8D 0D 7B 05 92 00            lea rcx, [rip + 0x92057b]
004E66D5  E8 06 FA F3 FF                  call 0x1404260e0
004E66DA  E9 06 FC FF FF                  jmp 0x1404e62e5
004E66DF  83 3D 6A 05 92 00 05            cmp dword ptr [rip + 0x92056a], 5
004E66E6  0F 86 BC 00 00 00               jbe 0x1404e67a8
004E66EC  44 89 BC 24 84 01 00 00         mov dword ptr [rsp + 0x184], r15d
004E66F4  48 8D 84 24 84 01 00 00         lea rax, [rsp + 0x184]
004E66FC  48 89 84 24 A0 07 00 00         mov qword ptr [rsp + 0x7a0], rax
004E6704  48 C7 84 24 A8 07 00 00 04 00 00 00  mov qword ptr [rsp + 0x7a8], 4
004E6710  89 B4 24 88 01 00 00            mov dword ptr [rsp + 0x188], esi
004E6717  48 8D 84 24 88 01 00 00         lea rax, [rsp + 0x188]
004E671F  48 89 84 24 B0 07 00 00         mov qword ptr [rsp + 0x7b0], rax
004E6727  48 C7 84 24 B8 07 00 00 04 00 00 00  mov qword ptr [rsp + 0x7b8], 4
004E6733  48 89 9C 24 70 02 00 00         mov qword ptr [rsp + 0x270], rbx
004E673B  48 8D 84 24 70 02 00 00         lea rax, [rsp + 0x270]
004E6743  48 89 84 24 C0 07 00 00         mov qword ptr [rsp + 0x7c0], rax
004E674B  48 C7 84 24 C8 07 00 00 08 00 00 00  mov qword ptr [rsp + 0x7c8], 8
004E6757  89 8C 24 D4 01 00 00            mov dword ptr [rsp + 0x1d4], ecx
004E675E  48 8D 84 24 D4 01 00 00         lea rax, [rsp + 0x1d4]
004E6766  48 89 84 24 D0 07 00 00         mov qword ptr [rsp + 0x7d0], rax
004E676E  48 C7 84 24 D8 07 00 00 04 00 00 00  mov qword ptr [rsp + 0x7d8], 4
004E677A  48 8D 84 24 80 07 00 00         lea rax, [rsp + 0x780]
004E6782  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E6787  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E678F  45 33 C9                        xor r9d, r9d
004E6792  45 33 C0                        xor r8d, r8d
004E6795  48 8D 15 9B E9 B5 FF            lea rdx, [rip - 0x4a1665]
004E679C  48 8D 0D AD 04 92 00            lea rcx, [rip + 0x9204ad]
004E67A3  E8 38 F9 F3 FF                  call 0x1404260e0
004E67A8  F7 C6 00 30 00 00               test esi, 0x3000
004E67AE  0F 84 46 FA FF FF               je 0x1404e61fa
004E67B4  45 84 FF                        test r15b, r15b
004E67B7  0F 88 E9 00 00 00               js 0x1404e68a6
004E67BD  41 F7 C7 00 00 01 10            test r15d, 0x10010000
004E67C4  0F 84 DC 00 00 00               je 0x1404e68a6
004E67CA  83 3D 7F 04 92 00 03            cmp dword ptr [rip + 0x92047f], 3
004E67D1  0F 86 AE E6 FF FF               jbe 0x1404e4e85
004E67D7  C7 84 24 90 01 00 00 09 09 00 C0  mov dword ptr [rsp + 0x190], 0xc0000909
004E67E2  48 8D 84 24 90 01 00 00         lea rax, [rsp + 0x190]
004E67EA  48 89 84 24 30 07 00 00         mov qword ptr [rsp + 0x730], rax
004E67F2  48 C7 84 24 38 07 00 00 04 00 00 00  mov qword ptr [rsp + 0x738], 4
004E67FE  44 89 BC 24 94 01 00 00         mov dword ptr [rsp + 0x194], r15d
004E6806  48 8D 84 24 94 01 00 00         lea rax, [rsp + 0x194]
004E680E  48 89 84 24 40 07 00 00         mov qword ptr [rsp + 0x740], rax
004E6816  48 C7 84 24 48 07 00 00 04 00 00 00  mov qword ptr [rsp + 0x748], 4
004E6822  89 B4 24 98 01 00 00            mov dword ptr [rsp + 0x198], esi
004E6829  48 8D 84 24 98 01 00 00         lea rax, [rsp + 0x198]
004E6831  48 89 84 24 50 07 00 00         mov qword ptr [rsp + 0x750], rax
004E6839  48 C7 84 24 58 07 00 00 04 00 00 00  mov qword ptr [rsp + 0x758], 4
004E6845  48 89 9C 24 00 02 00 00         mov qword ptr [rsp + 0x200], rbx
004E684D  48 8D 84 24 00 02 00 00         lea rax, [rsp + 0x200]
004E6855  48 89 84 24 60 07 00 00         mov qword ptr [rsp + 0x760], rax
004E685D  48 C7 84 24 68 07 00 00 08 00 00 00  mov qword ptr [rsp + 0x768], 8
004E6869  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E686F  89 84 24 9C 01 00 00            mov dword ptr [rsp + 0x19c], eax
004E6876  48 8D 84 24 9C 01 00 00         lea rax, [rsp + 0x19c]
004E687E  48 89 84 24 70 07 00 00         mov qword ptr [rsp + 0x770], rax
004E6886  48 C7 84 24 78 07 00 00 04 00 00 00  mov qword ptr [rsp + 0x778], 4
004E6892  48 8D 84 24 10 07 00 00         lea rax, [rsp + 0x710]
004E689A  48 8D 15 2B E8 B5 FF            lea rdx, [rip - 0x4a17d5]
004E68A1  E9 C0 E5 FF FF                  jmp 0x1404e4e66
004E68A6  0F BA E6 0D                     bt esi, 0xd
004E68AA  0F 83 4A F9 FF FF               jae 0x1404e61fa
004E68B0  48 8B 7B 48                     mov rdi, qword ptr [rbx + 0x48]
004E68B4  41 BE 80 00 00 40               mov r14d, 0x40000080
004E68BA  4C 8B A4 24 E8 0C 00 00         mov r12, qword ptr [rsp + 0xce8]
004E68C2  4C 8B AC 24 E0 0C 00 00         mov r13, qword ptr [rsp + 0xce0]
004E68CA  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
004E68D2  48 8D 43 48                     lea rax, [rbx + 0x48]
004E68D6  48 3B F8                        cmp rdi, rax
004E68D9  0F 84 1B F9 FF FF               je 0x1404e61fa
004E68DF  33 C0                           xor eax, eax
004E68E1  39 44 24 78                     cmp dword ptr [rsp + 0x78], eax
004E68E5  75 1E                           jne 0x1404e6905
004E68E7  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
004E68EB  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
004E68F3  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
004E68F7  45 33 C0                        xor r8d, r8d
004E68FA  E8 B1 BD F0 FF                  call 0x1403f26b0
004E68FF  84 C0                           test al, al
004E6901  74 02                           je 0x1404e6905
004E6903  EB 26                           jmp 0x1404e692b
004E6905  41 8B C7                        mov eax, r15d
004E6908  41 23 C6                        and eax, r14d
004E690B  41 3B C6                        cmp eax, r14d
004E690E  75 20                           jne 0x1404e6930
004E6910  45 0F B7 0C 24                  movzx r9d, word ptr [r12]
004E6915  45 8B 45 00                     mov r8d, dword ptr [r13]
004E6919  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
004E691D  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004E6922  E8 F1 3D FD FF                  call 0x1404ba718
004E6927  85 C0                           test eax, eax
004E6929  78 05                           js 0x1404e6930
004E692B  48 8B 3F                        mov rdi, qword ptr [rdi]
004E692E  EB 9A                           jmp 0x1404e68ca
004E6930  41 F7 C7 00 00 01 10            test r15d, 0x10010000
004E6937  0F 85 48 E5 FF FF               jne 0x1404e4e85
004E693D  E9 CF FA FF FF                  jmp 0x1404e6411
004E6942  83 3D 07 03 92 00 05            cmp dword ptr [rip + 0x920307], 5
004E6949  0F 86 BC 00 00 00               jbe 0x1404e6a0b
004E694F  44 89 BC 24 A0 01 00 00         mov dword ptr [rsp + 0x1a0], r15d
004E6957  48 8D 84 24 A0 01 00 00         lea rax, [rsp + 0x1a0]
004E695F  48 89 84 24 00 08 00 00         mov qword ptr [rsp + 0x800], rax
004E6967  48 C7 84 24 08 08 00 00 04 00 00 00  mov qword ptr [rsp + 0x808], 4
004E6973  89 B4 24 A4 01 00 00            mov dword ptr [rsp + 0x1a4], esi
004E697A  48 8D 84 24 A4 01 00 00         lea rax, [rsp + 0x1a4]
004E6982  48 89 84 24 10 08 00 00         mov qword ptr [rsp + 0x810], rax
004E698A  48 C7 84 24 18 08 00 00 04 00 00 00  mov qword ptr [rsp + 0x818], 4
004E6996  48 89 9C 24 80 02 00 00         mov qword ptr [rsp + 0x280], rbx
004E699E  48 8D 84 24 80 02 00 00         lea rax, [rsp + 0x280]
004E69A6  48 89 84 24 20 08 00 00         mov qword ptr [rsp + 0x820], rax
004E69AE  48 C7 84 24 28 08 00 00 08 00 00 00  mov qword ptr [rsp + 0x828], 8
004E69BA  89 8C 24 A8 01 00 00            mov dword ptr [rsp + 0x1a8], ecx
004E69C1  48 8D 84 24 A8 01 00 00         lea rax, [rsp + 0x1a8]
004E69C9  48 89 84 24 30 08 00 00         mov qword ptr [rsp + 0x830], rax
004E69D1  48 C7 84 24 38 08 00 00 04 00 00 00  mov qword ptr [rsp + 0x838], 4
004E69DD  48 8D 84 24 E0 07 00 00         lea rax, [rsp + 0x7e0]
004E69E5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E69EA  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E69F2  45 33 C9                        xor r9d, r9d
004E69F5  45 33 C0                        xor r8d, r8d
004E69F8  48 8D 15 3C DC B5 FF            lea rdx, [rip - 0x4a23c4]
004E69FF  48 8D 0D 4A 02 92 00            lea rcx, [rip + 0x92024a]
004E6A06  E8 D5 F6 F3 FF                  call 0x1404260e0
004E6A0B  81 FE 00 20 00 00               cmp esi, 0x2000
004E6A11  75 54                           jne 0x1404e6a67
004E6A13  41 8B C7                        mov eax, r15d
004E6A16  41 BE 80 00 00 40               mov r14d, 0x40000080
004E6A1C  41 23 C6                        and eax, r14d
004E6A1F  41 3B C6                        cmp eax, r14d
004E6A22  75 33                           jne 0x1404e6a57
004E6A24  4C 8B 8C 24 E8 0C 00 00         mov r9, qword ptr [rsp + 0xce8]
004E6A2C  45 0F B7 09                     movzx r9d, word ptr [r9]
004E6A30  4C 8B 84 24 E0 0C 00 00         mov r8, qword ptr [rsp + 0xce0]
004E6A38  45 8B 00                        mov r8d, dword ptr [r8]
004E6A3B  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
004E6A3F  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
004E6A44  48 8B CE                        mov rcx, rsi
004E6A47  E8 CC 3C FD FF                  call 0x1404ba718
004E6A4C  45 33 ED                        xor r13d, r13d
004E6A4F  85 C0                           test eax, eax
004E6A51  0F 89 48 E9 FF FF               jns 0x1404e539f
004E6A57  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E6A5D  83 E0 20                        and eax, 0x20
004E6A60  0D 40 70 10 00                  or eax, 0x107040
004E6A65  EB 18                           jmp 0x1404e6a7f
004E6A67  0F BA E6 0C                     bt esi, 0xc
004E6A6B  0F 83 A0 F9 FF FF               jae 0x1404e6411
004E6A71  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E6A77  83 E0 20                        and eax, 0x20
004E6A7A  0D 40 70 80 00                  or eax, 0x807040
004E6A7F  89 83 90 00 00 00               mov dword ptr [rbx + 0x90], eax
004E6A85  E9 87 F9 FF FF                  jmp 0x1404e6411
004E6A8A  83 3D BF 01 92 00 05            cmp dword ptr [rip + 0x9201bf], 5
004E6A91  0F 86 BC 00 00 00               jbe 0x1404e6b53
004E6A97  44 89 BC 24 AC 01 00 00         mov dword ptr [rsp + 0x1ac], r15d
004E6A9F  48 8D 84 24 AC 01 00 00         lea rax, [rsp + 0x1ac]
004E6AA7  48 89 84 24 40 0A 00 00         mov qword ptr [rsp + 0xa40], rax
004E6AAF  48 C7 84 24 48 0A 00 00 04 00 00 00  mov qword ptr [rsp + 0xa48], 4
004E6ABB  89 B4 24 B0 01 00 00            mov dword ptr [rsp + 0x1b0], esi
004E6AC2  48 8D 84 24 B0 01 00 00         lea rax, [rsp + 0x1b0]
004E6ACA  48 89 84 24 50 0A 00 00         mov qword ptr [rsp + 0xa50], rax
004E6AD2  48 C7 84 24 58 0A 00 00 04 00 00 00  mov qword ptr [rsp + 0xa58], 4
004E6ADE  48 89 9C 24 88 02 00 00         mov qword ptr [rsp + 0x288], rbx
004E6AE6  48 8D 84 24 88 02 00 00         lea rax, [rsp + 0x288]
004E6AEE  48 89 84 24 60 0A 00 00         mov qword ptr [rsp + 0xa60], rax
004E6AF6  48 C7 84 24 68 0A 00 00 08 00 00 00  mov qword ptr [rsp + 0xa68], 8
004E6B02  89 8C 24 B4 01 00 00            mov dword ptr [rsp + 0x1b4], ecx
004E6B09  48 8D 84 24 B4 01 00 00         lea rax, [rsp + 0x1b4]
004E6B11  48 89 84 24 70 0A 00 00         mov qword ptr [rsp + 0xa70], rax
004E6B19  48 C7 84 24 78 0A 00 00 04 00 00 00  mov qword ptr [rsp + 0xa78], 4
004E6B25  48 8D 84 24 20 0A 00 00         lea rax, [rsp + 0xa20]
004E6B2D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E6B32  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E6B3A  45 33 C9                        xor r9d, r9d
004E6B3D  45 33 C0                        xor r8d, r8d
004E6B40  48 8D 15 62 DB B5 FF            lea rdx, [rip - 0x4a249e]
004E6B47  48 8D 0D 02 01 92 00            lea rcx, [rip + 0x920102]
004E6B4E  E8 8D F5 F3 FF                  call 0x1404260e0
004E6B53  41 3B F6                        cmp esi, r14d
004E6B56  75 10                           jne 0x1404e6b68
004E6B58  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E6B5E  83 E0 20                        and eax, 0x20
004E6B61  0D 40 70 10 00                  or eax, 0x107040
004E6B66  EB 16                           jmp 0x1404e6b7e
004E6B68  41 23 F4                        and esi, r12d
004E6B6B  41 3B F4                        cmp esi, r12d
004E6B6E  75 14                           jne 0x1404e6b84
004E6B70  8B 83 90 00 00 00               mov eax, dword ptr [rbx + 0x90]
004E6B76  83 E0 20                        and eax, 0x20
004E6B79  0D 40 70 80 00                  or eax, 0x807040
004E6B7E  89 83 90 00 00 00               mov dword ptr [rbx + 0x90], eax
004E6B84  41 8B C7                        mov eax, r15d
004E6B87  41 BE 80 00 00 40               mov r14d, 0x40000080
004E6B8D  41 23 C6                        and eax, r14d
004E6B90  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
004E6B95  41 3B C6                        cmp eax, r14d
004E6B98  75 30                           jne 0x1404e6bca
004E6B9A  4C 8B 8C 24 E8 0C 00 00         mov r9, qword ptr [rsp + 0xce8]
004E6BA2  45 0F B7 09                     movzx r9d, word ptr [r9]
004E6BA6  4C 8B 84 24 E0 0C 00 00         mov r8, qword ptr [rsp + 0xce0]
004E6BAE  45 8B 00                        mov r8d, dword ptr [r8]
004E6BB1  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
004E6BB5  48 8B CE                        mov rcx, rsi
004E6BB8  E8 5B 3B FD FF                  call 0x1404ba718
004E6BBD  45 33 ED                        xor r13d, r13d
004E6BC0  85 C0                           test eax, eax
004E6BC2  0F 89 D7 E7 FF FF               jns 0x1404e539f
004E6BC8  EB 03                           jmp 0x1404e6bcd
004E6BCA  45 33 ED                        xor r13d, r13d
004E6BCD  41 BE 01 00 00 00               mov r14d, 1
004E6BD3  44 88 74 24 60                  mov byte ptr [rsp + 0x60], r14b
004E6BD8  E9 C8 E7 FF FF                  jmp 0x1404e53a5
004E6BDD  83 3D 6C 00 92 00 05            cmp dword ptr [rip + 0x92006c], 5
004E6BE4  0F 86 BC 00 00 00               jbe 0x1404e6ca6
004E6BEA  44 89 BC 24 B8 01 00 00         mov dword ptr [rsp + 0x1b8], r15d
004E6BF2  48 8D 84 24 B8 01 00 00         lea rax, [rsp + 0x1b8]
004E6BFA  48 89 84 24 40 03 00 00         mov qword ptr [rsp + 0x340], rax
004E6C02  48 C7 84 24 48 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x348], 4
004E6C0E  89 B4 24 BC 01 00 00            mov dword ptr [rsp + 0x1bc], esi
004E6C15  48 8D 84 24 BC 01 00 00         lea rax, [rsp + 0x1bc]
004E6C1D  48 89 84 24 50 03 00 00         mov qword ptr [rsp + 0x350], rax
004E6C25  48 C7 84 24 58 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x358], 4
004E6C31  48 89 9C 24 90 02 00 00         mov qword ptr [rsp + 0x290], rbx
004E6C39  48 8D 84 24 90 02 00 00         lea rax, [rsp + 0x290]
004E6C41  48 89 84 24 60 03 00 00         mov qword ptr [rsp + 0x360], rax
004E6C49  48 C7 84 24 68 03 00 00 08 00 00 00  mov qword ptr [rsp + 0x368], 8
004E6C55  89 8C 24 C0 01 00 00            mov dword ptr [rsp + 0x1c0], ecx
004E6C5C  48 8D 84 24 C0 01 00 00         lea rax, [rsp + 0x1c0]
004E6C64  48 89 84 24 70 03 00 00         mov qword ptr [rsp + 0x370], rax
004E6C6C  48 C7 84 24 78 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x378], 4
004E6C78  48 8D 84 24 20 03 00 00         lea rax, [rsp + 0x320]
004E6C80  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E6C85  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E6C8D  45 33 C9                        xor r9d, r9d
004E6C90  45 33 C0                        xor r8d, r8d
004E6C93  48 8D 15 ED DA B5 FF            lea rdx, [rip - 0x4a2513]
004E6C9A  48 8D 0D AF FF 91 00            lea rcx, [rip + 0x91ffaf]
004E6CA1  E8 3A F4 F3 FF                  call 0x1404260e0
004E6CA6  0F BA E6 0C                     bt esi, 0xc
004E6CAA  0F 83 D4 FE FF FF               jae 0x1404e6b84
004E6CB0  E9 BB FE FF FF                  jmp 0x1404e6b70
004E6CB5  E8 1E B1 09 00                  call 0x140581dd8
004E6CBA  8B 8B 90 00 00 00               mov ecx, dword ptr [rbx + 0x90]
004E6CC0  83 E1 40                        and ecx, 0x40
004E6CC3  85 C0                           test eax, eax
004E6CC5  74 2B                           je 0x1404e6cf2
004E6CC7  85 C9                           test ecx, ecx
004E6CC9  75 2B                           jne 0x1404e6cf6
004E6CCB  48 8D 43 48                     lea rax, [rbx + 0x48]
004E6CCF  48 8B 38                        mov rdi, qword ptr [rax]
004E6CD2  48 3B F8                        cmp rdi, rax
004E6CD5  74 32                           je 0x1404e6d09
004E6CD7  48 8D 43 48                     lea rax, [rbx + 0x48]
004E6CDB  48 3B F8                        cmp rdi, rax
004E6CDE  74 29                           je 0x1404e6d09
004E6CE0  48 8D 4F 48                     lea rcx, [rdi + 0x48]
004E6CE4  48 8B 57 58                     mov rdx, qword ptr [rdi + 0x58]
004E6CE8  E8 C7 EB 22 00                  call 0x1407158b4
004E6CED  48 8B 3F                        mov rdi, qword ptr [rdi]
004E6CF0  EB E5                           jmp 0x1404e6cd7
004E6CF2  85 C9                           test ecx, ecx
004E6CF4  74 13                           je 0x1404e6d09
004E6CF6  48 8B 93 B8 00 00 00            mov rdx, qword ptr [rbx + 0xb8]
004E6CFD  48 8D 8B A8 00 00 00            lea rcx, [rbx + 0xa8]
004E6D04  E8 AB EB 22 00                  call 0x1407158b4
004E6D09  44 38 6C 24 71                  cmp byte ptr [rsp + 0x71], r13b
004E6D0E  74 17                           je 0x1404e6d27
004E6D10  45 8A C6                        mov r8b, r14b
004E6D13  33 D2                           xor edx, edx
004E6D15  48 8B CB                        mov rcx, rbx
004E6D18  E8 7B 43 FA FF                  call 0x14048b098
004E6D1D  33 D2                           xor edx, edx
004E6D1F  48 8B CB                        mov rcx, rbx
004E6D22  E8 05 85 FB FF                  call 0x14049f22c
004E6D27  48 8B 84 24 00 02 00 00         mov rax, qword ptr [rsp + 0x200]
004E6D2F  44 88 28                        mov byte ptr [rax], r13b
004E6D32  48 8B 84 24 F8 01 00 00         mov rax, qword ptr [rsp + 0x1f8]
004E6D3A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004E6D3F  48 8B 84 24 18 0D 00 00         mov rax, qword ptr [rsp + 0xd18]
004E6D47  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004E6D4C  48 8B 84 24 F0 01 00 00         mov rax, qword ptr [rsp + 0x1f0]
004E6D54  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004E6D59  48 8B 84 24 08 0D 00 00         mov rax, qword ptr [rsp + 0xd08]
004E6D61  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004E6D66  8A 44 24 72                     mov al, byte ptr [rsp + 0x72]
004E6D6A  88 44 24 30                     mov byte ptr [rsp + 0x30], al
004E6D6E  48 8D 84 24 A0 02 00 00         lea rax, [rsp + 0x2a0]
004E6D76  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E6D7B  48 8B 84 24 00 0D 00 00         mov rax, qword ptr [rsp + 0xd00]
004E6D83  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004E6D88  4C 8B 8C 24 F8 0C 00 00         mov r9, qword ptr [rsp + 0xcf8]
004E6D90  4C 8B 84 24 E8 01 00 00         mov r8, qword ptr [rsp + 0x1e8]
004E6D98  48 8B D6                        mov rdx, rsi
004E6D9B  48 8B CB                        mov rcx, rbx
004E6D9E  E8 F5 0B 00 00                  call 0x1404e7998
004E6DA3  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
004E6DA7  E9 EC 00 00 00                  jmp 0x1404e6e98
004E6DAC  83 3D 9D FE 91 00 05            cmp dword ptr [rip + 0x91fe9d], 5
004E6DB3  0F 86 DB 00 00 00               jbe 0x1404e6e94
004E6DB9  89 94 24 C4 01 00 00            mov dword ptr [rsp + 0x1c4], edx
004E6DC0  48 8D 8C 24 C4 01 00 00         lea rcx, [rsp + 0x1c4]
004E6DC8  48 89 8C 24 B0 03 00 00         mov qword ptr [rsp + 0x3b0], rcx
004E6DD0  48 C7 84 24 B8 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x3b8], 4
004E6DDC  44 89 BC 24 C8 01 00 00         mov dword ptr [rsp + 0x1c8], r15d
004E6DE4  48 8D 8C 24 C8 01 00 00         lea rcx, [rsp + 0x1c8]
004E6DEC  48 89 8C 24 C0 03 00 00         mov qword ptr [rsp + 0x3c0], rcx
004E6DF4  48 C7 84 24 C8 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x3c8], 4
004E6E00  89 B4 24 90 00 00 00            mov dword ptr [rsp + 0x90], esi
004E6E07  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
004E6E0F  48 89 8C 24 D0 03 00 00         mov qword ptr [rsp + 0x3d0], rcx
004E6E17  48 C7 84 24 D8 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x3d8], 4
004E6E23  48 89 9C 24 98 02 00 00         mov qword ptr [rsp + 0x298], rbx
004E6E2B  48 8D 8C 24 98 02 00 00         lea rcx, [rsp + 0x298]
004E6E33  48 89 8C 24 E0 03 00 00         mov qword ptr [rsp + 0x3e0], rcx
004E6E3B  48 C7 84 24 E8 03 00 00 08 00 00 00  mov qword ptr [rsp + 0x3e8], 8
004E6E47  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
004E6E4B  48 8D 44 24 68                  lea rax, [rsp + 0x68]
004E6E50  48 89 84 24 F0 03 00 00         mov qword ptr [rsp + 0x3f0], rax
004E6E58  48 C7 84 24 F8 03 00 00 04 00 00 00  mov qword ptr [rsp + 0x3f8], 4
004E6E64  48 8D 84 24 90 03 00 00         lea rax, [rsp + 0x390]
004E6E6C  48 8D 15 08 E1 B5 FF            lea rdx, [rip - 0x4a1ef8]
004E6E73  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E6E78  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
004E6E80  45 33 C9                        xor r9d, r9d
004E6E83  45 33 C0                        xor r8d, r8d
004E6E86  48 8D 0D C3 FD 91 00            lea rcx, [rip + 0x91fdc3]
004E6E8D  E8 4E F2 F3 FF                  call 0x1404260e0
004E6E92  33 D2                           xor edx, edx
004E6E94  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
004E6E98  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
004E6E9C  48 8B 8C 24 60 0C 00 00         mov rcx, qword ptr [rsp + 0xc60]
004E6EA4  48 33 CC                        xor rcx, rsp
004E6EA7  E8 94 57 1C 00                  call 0x1406ac640
004E6EAC  48 81 C4 70 0C 00 00            add rsp, 0xc70
004E6EB3  41 5F                           pop r15
004E6EB5  41 5E                           pop r14
004E6EB7  41 5D                           pop r13
004E6EB9  41 5C                           pop r12
004E6EBB  5F                              pop rdi
004E6EBC  5E                              pop rsi
004E6EBD  5B                              pop rbx
004E6EBE  C3                              ret
004E6EBF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpOplockBreakByCacheFlags(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m350;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned __int64 v_stack_m370;
    unsigned __int64 v_stack_m378;
    unsigned __int64 v_stack_m380;
    unsigned __int64 v_stack_m388;
    unsigned __int64 v_stack_m3A8;
    unsigned __int64 v_stack_m3B0;
    unsigned __int64 v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned __int64 v_stack_m3E8;
    unsigned __int64 v_stack_m408;
    unsigned __int64 v_stack_m410;
    unsigned __int64 v_stack_m418;
    unsigned __int64 v_stack_m420;
    unsigned __int64 v_stack_m428;
    unsigned __int64 v_stack_m430;
    unsigned __int64 v_stack_m438;
    unsigned __int64 v_stack_m440;
    unsigned __int64 v_stack_m448;
    unsigned __int64 v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned __int64 v_stack_m490;
    unsigned __int64 v_stack_m498;
    unsigned __int64 v_stack_m4A0;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m4C8;
    unsigned __int64 v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned __int64 v_stack_m4E0;
    unsigned __int64 v_stack_m4E8;
    unsigned __int64 v_stack_m4F0;
    unsigned __int64 v_stack_m4F8;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m500;
    unsigned __int64 v_stack_m508;
    unsigned __int64 v_stack_m528;
    unsigned __int64 v_stack_m530;
    unsigned __int64 v_stack_m538;
    unsigned __int64 v_stack_m540;
    unsigned __int64 v_stack_m548;
    unsigned __int64 v_stack_m550;
    unsigned __int64 v_stack_m558;
    unsigned __int64 v_stack_m560;
    unsigned __int64 v_stack_m568;
    unsigned __int64 v_stack_m570;
    unsigned __int64 v_stack_m578;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m598;
    unsigned __int64 v_stack_m5A0;
    unsigned __int64 v_stack_m5A8;
    unsigned __int64 v_stack_m5B0;
    unsigned __int64 v_stack_m5B8;
    unsigned __int64 v_stack_m5C0;
    unsigned __int64 v_stack_m5C8;
    unsigned __int64 v_stack_m5D0;
    unsigned __int64 v_stack_m5D8;
    unsigned __int64 v_stack_m5E0;
    unsigned __int64 v_stack_m5E8;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m608;
    unsigned __int64 v_stack_m610;
    unsigned __int64 v_stack_m618;
    unsigned __int64 v_stack_m620;
    unsigned __int64 v_stack_m628;
    unsigned __int64 v_stack_m630;
    unsigned __int64 v_stack_m638;
    unsigned __int64 v_stack_m640;
    unsigned __int64 v_stack_m648;
    unsigned __int64 v_stack_m650;
    unsigned __int64 v_stack_m658;
    unsigned __int64 v_stack_m678;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m680;
    unsigned __int64 v_stack_m688;
    unsigned __int64 v_stack_m690;
    unsigned __int64 v_stack_m698;
    unsigned __int64 v_stack_m6A0;
    unsigned __int64 v_stack_m6A8;
    unsigned __int64 v_stack_m6B0;
    unsigned __int64 v_stack_m6B8;
    unsigned __int64 v_stack_m6C0;
    unsigned __int64 v_stack_m6C8;
    unsigned __int64 v_stack_m6E8;
    unsigned __int64 v_stack_m6F0;
    unsigned __int64 v_stack_m6F8;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m700;
    unsigned __int64 v_stack_m708;
    unsigned __int64 v_stack_m710;
    unsigned __int64 v_stack_m718;
    unsigned __int64 v_stack_m720;
    unsigned __int64 v_stack_m728;
    unsigned __int64 v_stack_m730;
    unsigned __int64 v_stack_m738;
    unsigned __int64 v_stack_m758;
    unsigned __int64 v_stack_m760;
    unsigned __int64 v_stack_m768;
    unsigned __int64 v_stack_m770;
    unsigned __int64 v_stack_m778;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m780;
    unsigned __int64 v_stack_m788;
    unsigned __int64 v_stack_m790;
    unsigned __int64 v_stack_m798;
    unsigned __int64 v_stack_m7A0;
    unsigned __int64 v_stack_m7A8;
    unsigned __int64 v_stack_m7C8;
    unsigned __int64 v_stack_m7D0;
    unsigned __int64 v_stack_m7D8;
    unsigned __int64 v_stack_m7E0;
    unsigned __int64 v_stack_m7E8;
    unsigned __int64 v_stack_m7F0;
    unsigned __int64 v_stack_m7F8;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m800;
    unsigned __int64 v_stack_m808;
    unsigned __int64 v_stack_m810;
    unsigned __int64 v_stack_m818;
    unsigned __int64 v_stack_m838;
    unsigned __int64 v_stack_m840;
    unsigned __int64 v_stack_m848;
    unsigned __int64 v_stack_m850;
    unsigned __int64 v_stack_m858;
    unsigned __int64 v_stack_m860;
    unsigned __int64 v_stack_m868;
    unsigned __int64 v_stack_m870;
    unsigned __int64 v_stack_m878;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m880;
    unsigned __int64 v_stack_m888;
    unsigned __int64 v_stack_m8A8;
    unsigned __int64 v_stack_m8B0;
    unsigned __int64 v_stack_m8B8;
    unsigned __int64 v_stack_m8C0;
    unsigned __int64 v_stack_m8C8;
    unsigned __int64 v_stack_m8D0;
    unsigned __int64 v_stack_m8D8;
    unsigned __int64 v_stack_m8E0;
    unsigned __int64 v_stack_m8E8;
    unsigned __int64 v_stack_m8F0;
    unsigned __int64 v_stack_m8F8;
    unsigned __int64 v_stack_m918;
    unsigned __int64 v_stack_m920;
    unsigned __int64 v_stack_m928;
    unsigned __int64 v_stack_m930;
    unsigned __int64 v_stack_m938;
    unsigned __int64 v_stack_m940;
    unsigned __int64 v_stack_m948;
    unsigned __int64 v_stack_m950;
    unsigned __int64 v_stack_m958;
    unsigned __int64 v_stack_m960;
    unsigned __int64 v_stack_m968;
    unsigned __int64 v_stack_m988;
    unsigned __int64 v_stack_m990;
    unsigned __int64 v_stack_m998;
    unsigned __int64 v_stack_m9A0;
    unsigned __int64 v_stack_m9A8;
    unsigned __int64 v_stack_m9B0;
    unsigned __int64 v_stack_m9B8;
    unsigned __int64 v_stack_m9C0;
    unsigned __int64 v_stack_m9C8;
    unsigned __int64 v_stack_m9E8;
    unsigned __int64 v_stack_mA08;
    unsigned __int64 v_stack_mA10;
    unsigned __int64 v_stack_mA18;
    unsigned __int64 v_stack_mA20;
    unsigned __int64 v_stack_mA28;
    unsigned __int64 v_stack_mA30;
    unsigned __int64 v_stack_mA38;
    unsigned __int64 v_stack_mA40;
    unsigned __int64 v_stack_mA48;
    unsigned __int64 v_stack_mA50;
    unsigned __int64 v_stack_mA58;
    unsigned __int64 v_stack_mA60;
    unsigned __int64 v_stack_mA68;
    unsigned __int64 v_stack_mA70;
    unsigned __int64 v_stack_mA78;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mA80;
    unsigned __int64 v_stack_mA88;
    unsigned __int64 v_stack_mA90;
    unsigned __int64 v_stack_mA98;
    unsigned __int64 v_stack_mAA0;
    unsigned __int64 v_stack_mAA8;
    unsigned __int64 v_stack_mAB0;
    unsigned __int64 v_stack_mAB8;
    unsigned __int64 v_stack_mAC0;
    unsigned __int64 v_stack_mAC8;
    unsigned int v_stack_mACC;
    unsigned int v_stack_mAD0;
    unsigned int v_stack_mAD4;
    unsigned int v_stack_mAD8;
    unsigned int v_stack_mAE0;
    unsigned int v_stack_mAE4;
    unsigned int v_stack_mAE8;
    unsigned int v_stack_mAEC;
    unsigned int v_stack_mAF0;
    unsigned int v_stack_mAF4;
    unsigned int v_stack_mAF8;
    unsigned int v_stack_mAFC;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB00;
    unsigned int v_stack_mB04;
    unsigned int v_stack_mB08;
    unsigned int v_stack_mB0C;
    unsigned int v_stack_mB10;
    unsigned int v_stack_mB14;
    unsigned int v_stack_mB18;
    unsigned int v_stack_mB1C;
    unsigned int v_stack_mB20;
    unsigned int v_stack_mB24;
    unsigned int v_stack_mB28;
    unsigned int v_stack_mB2C;
    unsigned int v_stack_mB30;
    unsigned int v_stack_mB34;
    unsigned int v_stack_mB38;
    unsigned int v_stack_mB3C;
    unsigned int v_stack_mB40;
    unsigned int v_stack_mB44;
    unsigned int v_stack_mB48;
    unsigned int v_stack_mB4C;
    unsigned int v_stack_mB50;
    unsigned int v_stack_mB54;
    unsigned int v_stack_mB58;
    unsigned int v_stack_mB5C;
    unsigned int v_stack_mB60;
    unsigned int v_stack_mB64;
    unsigned int v_stack_mB68;
    unsigned int v_stack_mB6C;
    unsigned int v_stack_mB70;
    unsigned int v_stack_mB74;
    unsigned int v_stack_mB78;
    unsigned int v_stack_mB7C;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mB80;
    unsigned int v_stack_mB84;
    unsigned int v_stack_mB88;
    unsigned int v_stack_mB8C;
    unsigned int v_stack_mB90;
    unsigned int v_stack_mB94;
    unsigned int v_stack_mB98;
    unsigned int v_stack_mB9C;
    unsigned int v_stack_mBA0;
    unsigned int v_stack_mBA4;
    unsigned int v_stack_mBA8;
    unsigned int v_stack_mBAC;
    unsigned int v_stack_mBB0;
    unsigned int v_stack_mBB4;
    unsigned int v_stack_mBB8;
    unsigned int v_stack_mBBC;
    unsigned int v_stack_mBC0;
    unsigned int v_stack_mBC4;
    unsigned int v_stack_mBC8;
    unsigned int v_stack_mBCC;
    unsigned int v_stack_mBD0;
    unsigned int v_stack_mBD4;
    unsigned int v_stack_mBD8;
    unsigned int v_stack_mBDC;
    unsigned int v_stack_mBE0;
    unsigned int v_stack_mBE4;
    unsigned int v_stack_mBE8;
    unsigned int v_stack_mBEC;
    unsigned int v_stack_mBF0;
    unsigned int v_stack_mBF4;
    unsigned int v_stack_mBF8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC00;
    unsigned int v_stack_mC08;
    unsigned int v_stack_mC0C;
    unsigned int v_stack_mC10;
    unsigned __int64 v_stack_mC18;
    unsigned __int8 v_stack_mC20;
    unsigned __int64 v_stack_mC28;
    unsigned int v_stack_mC30;
    unsigned int v_stack_mC34;
    unsigned __int8 v_stack_mC36;
    unsigned __int8 v_stack_mC37;
    unsigned __int8 v_stack_mC38;
    unsigned __int64 v_stack_mC40;
    unsigned __int8 v_stack_mC48;
    unsigned __int64 v_stack_mC58;
    unsigned __int64 v_stack_mC60;
    unsigned __int64 v_stack_mC68;
    unsigned __int8 v_stack_mC70;
    unsigned __int16 v_stack_mC78;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mC80;
    unsigned int v_stack_mC88;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;

    v_rsp = (v_rsp) - (0xC70ULL);
    result = (*(unsigned __int64 *)(v_rip + 9592212)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mC40 = a3;
    v_stack_mC18 = a2;
    v_stack_mAC0 = a9;
    v_stack_mAB8 = a13;
    v_stack_mAA8 = a15;
    v_stack_mAB0 = a16;
    a2 = 0;
    v_stack_mC34 = 0;
    a1 = 0;
    v_stack_mA08 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 2552) = 0;
    v_stack_mC48 = 0;
    v_stack_mC38 = 0;
    v_stack_mC36 = 0;
    v_stack_mC37 = (unsigned __int8)(a2 + 1);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (8));
    v_stack_mC30 = (unsigned int)(a1);
    result = a3;
    if ((*(unsigned int *)(v_rip + 9576946)) >= = 5) {
        *(unsigned int *)(v_rsp - 3088) = (unsigned int)((unsigned int)(a4));
        result = v_rsp - 3088;
        *(unsigned __int64 *)(v_rsp - 2504) = result;
        *(unsigned __int64 *)(v_rsp - 2496) = 4;
        v_stack_mC0C = (unsigned int)((unsigned int)(a6));
        result = v_rsp - 3084;
        *(unsigned __int64 *)(v_rsp - 2488) = result;
        *(unsigned __int64 *)(v_rsp - 2480) = 4;
        *(unsigned __int64 *)(v_rsp - 2784) = a1;
        result = v_rsp - 2784;
        *(unsigned __int64 *)(v_rsp - 2472) = result;
        *(unsigned __int64 *)(v_rsp - 2464) = 8;
        result = *(unsigned int *)(a1 + 144);
        v_stack_mC08 = (unsigned int)(result);
        result = v_rsp - 3080;
        *(unsigned __int64 *)(v_rsp - 2456) = result;
        *(unsigned __int64 *)(v_rsp - 2448) = 4;
        result = v_rsp - 2536;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4848741;
        a1 = v_rip + 9576768;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
        a1 = v_stack_mC30;
        a4 = v_stack_mC18;
        result = v_stack_mC40;
        a2 = 0;
        a3 = a2 + 1;
    }
    if (((unsigned int)((unsigned int)(a6))) == 0x7000ULL) goto loc_004E4C6D;
    if (((unsigned int)((unsigned int)(a6))) == ((unsigned int)((unsigned int)(0x5000ULL)))) goto loc_004E4C6D;
    if (((unsigned int)((unsigned int)(a6))) == ((unsigned int)((unsigned int)(0x4000ULL)))) goto loc_004E4C6D;
    if (((unsigned int)((unsigned int)(a6))) == 0x2000ULL) goto loc_004E4C6D;
    if (result != 0) {
        *(unsigned int *)(result + 48) = 0xC00000E3ULL;
        a2 = (unsigned __int8)(a3);
        a1 = result;
        result = IofCompleteRequest(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 9576656)) >= = 3) {
        v_stack_mC08 = 0xC00000E3ULL;
        result = v_stack_mC08;
        v_stack_m968 = result;
        v_stack_m960 = 4;
        v_stack_mC0C = (unsigned int)((unsigned int)(a4));
        result = v_stack_mC0C;
        v_stack_m958 = result;
        v_stack_m950 = 4;
        v_stack_mC10 = (unsigned int)((unsigned int)(a6));
        result = v_stack_mC10;
        v_stack_m948 = result;
        v_stack_m940 = 4;
        v_stack_mC40 = a1;
        result = v_stack_mC40;
        v_stack_m938 = result;
        v_stack_m930 = 8;
        result = *(unsigned int *)(a1 + 144);
        v_stack_mC30 = (unsigned int)(result);
        result = v_stack_mC30;
        v_stack_m928 = result;
        v_stack_m920 = 4;
        result = v_stack_m988;
        v_stack_mC80 = result;
        v_stack_mC88 = 7;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4849182;
        a1 = v_rip + 9576434;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    goto loc_004E6E9C;
loc_004E4C6D:
    if (a1 == 0) goto loc_004E6E98;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)))) == 0) goto loc_004E6DAC;
    if ((((unsigned int)((unsigned int)(a6))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144))))) == 0) goto loc_004E6DAC;
    if ((unsigned int)(a1) != 0) goto loc_004E4D7F;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(a4 + 48), *(unsigned __int64 *)(a1 + 8), (unsigned int)((unsigned int)((unsigned int)(a4))), a4);
    a2 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_004E4D7F;
    if ((*(unsigned int *)(v_rip + 9576348)) <= 5) goto loc_004E6E94;
    v_stack_mC08 = 0;
    v_stack_m818 = v_stack_mC08;
    v_stack_m810 = 4;
    v_stack_mC0C = (unsigned int)((unsigned int)(a4));
    v_stack_m808 = v_stack_mC0C;
    v_stack_m800 = 4;
    v_stack_mC10 = (unsigned int)((unsigned int)(a6));
    v_stack_m7F8 = v_stack_mC10;
    v_stack_m7F0 = 4;
    v_stack_mA88 = a1;
    v_stack_m7E8 = v_stack_mA88;
    v_stack_m7E0 = 8;
    v_stack_mC30 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_m7D8 = v_stack_mC30;
    v_stack_m7D0 = 4;
    goto loc_004E6E73;
loc_004E4D7F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 144)))) & (64)) == 0) goto loc_004E4E92;
    if ((((unsigned int)((unsigned int)(a4))) & (0x10010000ULL)) == 0) goto loc_004E4E92;
    if ((*(unsigned int *)(v_rip + 9576110)) <= 3) goto loc_004E4E85;
    v_stack_mC34 = 0xC0000909ULL;
    v_stack_m7A8 = v_stack_mC34;
    v_stack_m7A0 = 4;
    v_stack_mAD8 = (unsigned int)((unsigned int)(a4));
    v_stack_m798 = v_stack_mAD8;
    v_stack_m790 = 4;
    v_stack_mAD0 = (unsigned int)((unsigned int)(a6));
    v_stack_m788 = v_stack_mAD0;
    v_stack_m780 = 4;
    v_stack_mA78 = a1;
    v_stack_m778 = v_stack_mA78;
    v_stack_m770 = 8;
    v_stack_mACC = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_m768 = v_stack_mACC;
    v_stack_m760 = 4;
loc_004E4E66:
    v_stack_mC80 = v_stack_m7C8;
    a4 = 0;
    v_stack_mC88 = 7;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9575888, v_rip - 4850028, a3, a4);
loc_004E4E85:
    v_stack_mC34 = 0xC0000909ULL;
    goto loc_004E6E98;
loc_004E4E92:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rip + 9575888))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(0x105040ULL)))) goto loc_004E62FC;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x105040ULL)))) goto loc_004E6202;
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(0x1000ULL))));
    if (condition_is_equal) goto loc_004E57EF;
    result = (unsigned int)((result) - (16));
    if (condition_is_equal) goto loc_004E57EF;
    result = (unsigned int)((result) - (0x1FF0ULL));
    if (condition_is_equal) goto loc_004E5A39;
    result = (unsigned int)((result) - (0x2040ULL));
    if (condition_is_equal) goto loc_004E554B;
    result = (unsigned int)((result) - (0x2000ULL));
    if (condition_is_equal) goto loc_004E51DB;
    result = (unsigned int)((result) - (0x3FC0ULL));
    if (condition_is_equal) goto loc_004E57EF;
    result = (unsigned int)((result) - (0xF8000ULL));
    if (condition_is_not_equal) goto loc_004E633E;
    if ((*(unsigned int *)(v_rip + 9575756)) >= = 5) {
        v_stack_mBF8 = (unsigned int)((unsigned int)(a4));
        result = v_stack_mBF8;
        v_stack_m9C8 = result;
        v_stack_m9C0 = 4;
        v_stack_mBF4 = (unsigned int)((unsigned int)(a6));
        result = v_stack_mBF4;
        v_stack_m9B8 = result;
        v_stack_m9B0 = 4;
        v_stack_mA70 = a1;
        result = v_stack_mA70;
        v_stack_m9A8 = result;
        v_stack_m9A0 = 8;
        v_stack_mBF0 = (unsigned int)(v_rip + 9575888);
        result = v_stack_mBF0;
        v_stack_m998 = result;
        v_stack_m990 = 4;
        result = v_stack_m9E8;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4849498;
        a1 = v_rip + 9575567;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = 0;
    v_stack_mC20 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & ((unsigned int)((unsigned int)(0x1000ULL))));
    if (condition_is_equal) goto loc_004E5135;
loc_004E4FE1:
    v_stack_mC28 = *(unsigned __int64 *)(a1 + 72);
    if ((*(unsigned __int64 *)(a1 + 72)) == (a1 + 72)) goto loc_004E5128;
    if (v_stack_mC30 != 0) goto loc_004E501A;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_mC18 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 24), (unsigned int)((unsigned int)((unsigned int)(a4))), a4);
    a1 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_004E5047;
loc_004E501A:
    v_stack_mC20 = 1;
    if ((((unsigned int)((unsigned int)(a4))) & (0x10010000ULL)) != 0) goto loc_004E504C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48))) & (0xFF0FFFFFULL));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48) = (unsigned int)(result);
loc_004E5047:
    goto loc_004E4FE1;
loc_004E504C:
    if ((*(unsigned int *)(v_rip + 9575421)) <= 3) goto loc_004E4E85;
    v_stack_mBEC = 0xC0000909ULL;
    v_stack_m738 = v_stack_mBEC;
    v_stack_m730 = 4;
    v_stack_mBE8 = (unsigned int)((unsigned int)(a4));
    v_stack_m728 = v_stack_mBE8;
    v_stack_m720 = 4;
    v_stack_mBE4 = (unsigned int)((unsigned int)(a6));
    v_stack_m718 = v_stack_mBE4;
    v_stack_m710 = 4;
    v_stack_mA68 = 0;
    v_stack_m708 = v_stack_mA68;
    v_stack_m700 = 8;
    v_stack_mBE0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_m6F8 = v_stack_mBE0;
    v_stack_m6F0 = 4;
    goto loc_004E4E66;
loc_004E5128:
    result = FsRtlpComputeShareableOplockState(0, v_rip - 4849966, (unsigned int)((unsigned int)((unsigned int)(a4))), a4);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & ((unsigned int)((unsigned int)(0x1000ULL))));
loc_004E5135:
    v_r13 = 0;
    if (condition_is_above_or_equal) goto loc_004E539A;
    if (1 != 0) goto loc_004E6606;
    if ((unsigned int)(result) != 0) goto loc_004E539A;
loc_004E516D:
    v_stack_mC28 = *(unsigned __int64 *)(a1 + 72);
    if ((*(unsigned __int64 *)(a1 + 72)) == (a1 + 72)) goto loc_004E61FA;
    result = 0;
    if (v_stack_mC30 != 0) goto loc_004E51A8;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_mC18 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 24), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004E51A8;
    goto loc_004E51D6;
loc_004E51A8:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & ((unsigned int)((unsigned int)(0x40000080ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x40000080ULL)))) goto loc_004E6411;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 24), (unsigned int)(*(unsigned int *)(a7)), *(unsigned __int16 *)(a8));
    if (sign_flag) goto loc_004E6411;
loc_004E51D6:
    goto loc_004E516D;
loc_004E51DB:
    if ((*(unsigned int *)(v_rip + 9575022)) >= = 5) {
        v_stack_mBDC = (unsigned int)((unsigned int)(a4));
        result = v_stack_mBDC;
        v_stack_m2C8 = result;
        v_stack_m2C0 = 4;
        v_stack_mBD8 = (unsigned int)((unsigned int)(a6));
        result = v_stack_mBD8;
        v_stack_m2B8 = result;
        v_stack_m2B0 = 4;
        v_stack_mA30 = 0;
        result = v_stack_mA30;
        v_stack_m2A8 = result;
        v_stack_m2A0 = 8;
        v_stack_mBD4 = (unsigned int)(v_stack_mC40);
        result = v_stack_mBD4;
        v_stack_m298 = result;
        v_stack_m290 = 4;
        result = v_stack_m2E8;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4852388;
        a1 = v_rip + 9574833;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(a6))) != ((unsigned int)((unsigned int)(0x40000080ULL)))) goto loc_004E534E;
    result = KeAcquireQueuedSpinLock(7, a2, a3, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69) = (unsigned __int8)(result);
    v_r13 = 0;
    result = KeReleaseQueuedSpinLock(v_r13 + 7, *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69), a3, a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 68)) != 0) goto loc_004E56F5;
    v_stack_mC00 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24);
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = 0x180001ULL;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) >> (12));
    result = (unsigned int)((result) & (7));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 4) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 8) = 3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12))) | ((unsigned int)(v_r13 + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) = v_r13 + 24;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 48) = 0;
    result = IofCompleteRequest(*(unsigned __int64 *)(a1), (unsigned __int8)(v_r13 + 1), v_r13 + 24, a4);
    *(unsigned __int64 *)(a1) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (0x507040ULL));
    goto loc_004E57DF;
loc_004E534E:
    if (((unsigned int)((unsigned int)(a6))) != 0x2000ULL) goto loc_004E54A5;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & ((unsigned int)((unsigned int)(0x40000080ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x40000080ULL)))) goto loc_004E53DC;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(a7)), *(unsigned __int16 *)(a8));
    v_r13 = 0;
    if (sign_flag) goto loc_004E53DF;
loc_004E539A:
loc_004E539F:
loc_004E53A5:
    if (v_stack_mC48 == 0) goto loc_004E6E98;
    if (((1) & ((unsigned __int8)((unsigned int)(a4)))) == 0) goto loc_004E6CB5;
    if (!(condition_is_above_or_equal)) {
        *(unsigned int *)(a1 + 144) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    }
    v_stack_mC34 = 264;
    goto loc_004E6E98;
loc_004E53DC:
    v_r13 = 0;
loc_004E53DF:
    result = KeAcquireQueuedSpinLock(7, *(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(a7)), *(unsigned __int16 *)(a8));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69) = (unsigned __int8)(result);
    result = KeReleaseQueuedSpinLock(7, *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69), (unsigned int)(*(unsigned int *)(a7)), *(unsigned __int16 *)(a8));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 68)) != 0) goto loc_004E56F5;
    v_stack_mC00 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24);
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = 0x180001ULL;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) >> (12));
    result = (unsigned int)((result) & (7));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 4) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 8) = 5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12))) | ((unsigned int)(result + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12) = (unsigned int)(result);
    if ((*(unsigned __int8 *)(v_stack_mC18)) == 0) {
        result = (unsigned int)((result) | (2));
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12) = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_stack_mC18 + 8);
        a1 = *(unsigned __int64 *)(result + 8);
        result = *(unsigned int *)(a1 + 20);
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 16) = (unsigned int)(result);
        result = *(unsigned __int16 *)(v_stack_mC18 + 26);
        *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 20) = (unsigned __int16)(result);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) = result + 24;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 48) = 0;
    result = IofCompleteRequest(*(unsigned __int64 *)(a1), (unsigned __int8)(result + 1), result + 24, v_stack_mC18);
    *(unsigned __int64 *)(a1) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (0x307040ULL));
    goto loc_004E57DF;
loc_004E54A5:
    v_rsi = (unsigned int)((v_stack_mC40) & ((unsigned int)(a8)));
    if (((unsigned int)(v_rsi)) != ((unsigned int)(a8))) goto loc_004E61FA;
    result = KeAcquireQueuedSpinLock(7, (unsigned __int8)(result + 1), result + 24, v_stack_mC18);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69) = (unsigned __int8)(result);
    v_r13 = 0;
    result = KeReleaseQueuedSpinLock(v_r13 + 7, *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69), result + 24, v_stack_mC18);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 68)) != 0) goto loc_004E56F5;
    v_stack_mC00 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24);
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = 0x180001ULL;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) >> (12));
    result = (unsigned int)((result) & (7));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 4) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12))) | ((unsigned int)(v_r13 + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) = v_r13 + 24;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 48) = 0;
    result = IofCompleteRequest(*(unsigned __int64 *)(a1), (unsigned __int8)(v_r13 + 1), v_r13 + 24, v_stack_mC18);
    *(unsigned __int64 *)(a1) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (0x807040ULL));
    goto loc_004E57DF;
loc_004E554B:
    if ((*(unsigned int *)(v_rip + 9574142)) >= = 5) {
        v_stack_mBD0 = (unsigned int)((unsigned int)(a4));
        result = v_stack_mBD0;
        v_stack_m448 = result;
        v_stack_m440 = 4;
        v_stack_mBCC = (unsigned int)(v_rsi);
        result = v_stack_mBCC;
        v_stack_m438 = result;
        v_stack_m430 = 4;
        v_stack_mAA0 = a1;
        result = v_stack_mAA0;
        v_stack_m428 = result;
        v_stack_m420 = 8;
        v_stack_mBC8 = (unsigned int)(*(unsigned __int64 *)(a1));
        result = v_stack_mBC8;
        v_stack_m418 = result;
        v_stack_m410 = 4;
        result = v_stack_m468;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4853162;
        a1 = v_rip + 9573953;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & ((unsigned int)(a8)));
    if (((unsigned int)(result)) != ((unsigned int)(a8))) goto loc_004E56BC;
    result = KeAcquireQueuedSpinLock(7, a2, a3, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69) = (unsigned __int8)(result);
    v_r13 = 0;
    result = KeReleaseQueuedSpinLock(v_r13 + 7, *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69), a3, a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 68)) != 0) goto loc_004E56F5;
    v_stack_mC00 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24);
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = 0x180001ULL;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) >> (12));
    result = (unsigned int)((result) & (7));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 4) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12))) | ((unsigned int)(v_r13 + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) = v_r13 + 24;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 48) = 0;
    result = IofCompleteRequest(*(unsigned __int64 *)(a1), (unsigned __int8)(v_r13 + 1), v_r13 + 24, a4);
    *(unsigned __int64 *)(a1) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (0x805040ULL));
    goto loc_004E57DF;
loc_004E56BC:
    if ((((unsigned int)(v_r13 + 1)) & ((unsigned int)(v_rsi))) == 0) goto loc_004E61FA;
    result = KeAcquireQueuedSpinLock(7, (unsigned __int8)(v_r13 + 1), v_r13 + 24, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69) = (unsigned __int8)(result);
    v_r13 = 0;
    result = KeReleaseQueuedSpinLock(v_r13 + 7, *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69), v_r13 + 24, a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 68)) == 0) goto loc_004E5776;
loc_004E56F5:
    a3 = 0;
    a2 = 0;
    result = FsRtlpModifyThreadPriorities(a1, a2, a3, a4);
    a2 = 0;
    result = FsRtlpClearOwner(a1, a2, a3, a4);
    *(unsigned __int8 *)(a1 + 32) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56)) == a1) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) = 0;
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 48) = 0xC0000120ULL;
    result = IofCompleteRequest(*(unsigned __int64 *)(a1), 1, a3, a4);
    *(unsigned __int64 *)(a1) = 0;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 8), (unsigned int)(0x746C6644ULL), a3, a4);
    *(unsigned __int64 *)(a1 + 8) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(a1 + 144) = (unsigned int)(result);
loc_004E575F:
    if ((*(unsigned __int64 *)(a1 + 88)) == (a1 + 88)) goto loc_004E61E8;
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(unsigned __int64 *)(a1 + 88), (unsigned int)(0x746C6644ULL), a3, a4);
    goto loc_004E575F;
loc_004E5776:
    v_stack_mC00 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24);
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = 0x180001ULL;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) >> (12));
    result = (unsigned int)((result) & (7));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 4) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 8) = (unsigned int)(result + 1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12))) | ((unsigned int)(result + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 12) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) = result + 24;
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 48) = 0;
    result = IofCompleteRequest(*(unsigned __int64 *)(a1), (unsigned __int8)(result + 1), result + 24, a4);
    *(unsigned __int64 *)(a1) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (0x105040ULL));
loc_004E57DF:
    *(unsigned int *)(a1 + 144) = (unsigned int)(result);
loc_004E57E5:
    v_stack_mC48 = (unsigned __int8)(result + 1);
    goto loc_004E61E8;
loc_004E57EF:
    if ((*(unsigned int *)(v_rip + 9573466)) >= = 5) {
        v_stack_mBC4 = (unsigned int)((unsigned int)(a4));
        result = v_stack_mBC4;
        v_stack_m3E8 = result;
        v_stack_m3E0 = 4;
        v_stack_mBC0 = (unsigned int)(v_rsi);
        result = v_stack_mBC0;
        v_stack_m3D8 = result;
        v_stack_m3D0 = 4;
        v_stack_mA98 = a1;
        result = v_stack_mA98;
        v_stack_m3C8 = result;
        v_stack_m3C0 = 8;
        v_stack_mBBC = (unsigned int)(*(unsigned __int64 *)(a1));
        result = v_stack_mBBC;
        v_stack_m3B8 = result;
        v_stack_m3B0 = 4;
        result = v_stack_m408;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4852762;
        a1 = v_rip + 9573277;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if (((0) & ((unsigned int)(v_rsi))) == 0) goto loc_004E5A21;
loc_004E58C5:
    v_stack_mC28 = *(unsigned __int64 *)(a1 + 40);
    if ((*(unsigned __int64 *)(a1 + 40)) == (a1 + 40)) goto loc_004E5A21;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 16) + 24)) != 0x90240ULL) goto loc_004E5A19;
    v_r13 = 0;
    if (v_stack_mC30 != 0) goto loc_004E5916;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_mC18 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 16) + 48), (unsigned int)((unsigned int)((unsigned int)(a4))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004E5916;
loc_004E5911:
    goto loc_004E5A19;
loc_004E5916:
    if ((((unsigned int)((unsigned int)(a4))) & (0x10010000ULL)) != 0) goto loc_004E593D;
    v_stack_mC28 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8);
    a3 = 0;
    a2 = 0;
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 8)), a2, a3, a1);
    goto loc_004E5911;
loc_004E593D:
    if ((*(unsigned int *)(v_rip + 9573132)) <= 3) goto loc_004E4E85;
    v_stack_mBB8 = 0xC0000909ULL;
    v_stack_m888 = v_stack_mBB8;
    v_stack_m880 = 4;
    v_stack_mBB4 = (unsigned int)((unsigned int)(a4));
    v_stack_m878 = v_stack_mBB4;
    v_stack_m870 = 4;
    v_stack_mBB0 = (unsigned int)(v_rsi);
    v_stack_m868 = v_stack_mBB0;
    v_stack_m860 = 4;
    v_stack_mA90 = a1;
    v_stack_m858 = v_stack_mA90;
    v_stack_m850 = 8;
    v_stack_mBAC = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_m848 = v_stack_mBAC;
    v_stack_m840 = 4;
    goto loc_004E4E66;
loc_004E5A19:
    goto loc_004E58C5;
loc_004E5A21:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144))))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) != 0xB000ULL) goto loc_004E61F2;
loc_004E5A39:
    if ((*(unsigned int *)(v_rip + 9572880)) <= 5) goto loc_004E5B07;
    v_stack_mBA8 = (unsigned int)((unsigned int)(a4));
    v_stack_m388 = v_stack_mBA8;
    v_stack_m380 = 4;
    v_r13 = 0;
    v_stack_mBA4 = (unsigned int)(v_rsi);
    v_stack_m378 = v_stack_mBA4;
    v_stack_m370 = 4;
    v_stack_mAC8 = a1;
    v_stack_m368 = v_stack_mAC8;
    v_stack_m360 = 8;
    v_stack_mBA0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_m358 = v_stack_mBA0;
    v_stack_m350 = 4;
    v_stack_mC80 = v_stack_m3A8;
    v_stack_mC88 = 6;
    a4 = 0;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9572688, v_rip - 4853140, a3, a4);
    goto loc_004E5B0A;
loc_004E5B07:
    v_r13 = 0;
loc_004E5B0A:
    if (((unsigned int)(v_rsi)) != 0x2000ULL) goto loc_004E5E3C;
loc_004E5B20:
    v_stack_mC28 = *(unsigned __int64 *)(a1 + 56);
    if ((*(unsigned __int64 *)(a1 + 56)) == (a1 + 56)) goto loc_004E616C;
    v_stack_mAC8 = *(unsigned __int64 *)(a1 + 56);
    result = 0;
    if (v_stack_mC30 != 0) goto loc_004E5B6A;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_mC18 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 24), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004E5B6A;
    v_r13 = 0;
    goto loc_004E5D57;
loc_004E5B6A:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & ((unsigned int)((unsigned int)(0x40000080ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x40000080ULL)))) goto loc_004E5BA7;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 24), (unsigned int)(*(unsigned int *)(a7)), *(unsigned __int16 *)(a8));
    v_r13 = 0;
    if (sign_flag) goto loc_004E5BAA;
loc_004E5BA2:
    goto loc_004E5D57;
loc_004E5BA7:
    v_r13 = 0;
loc_004E5BAA:
    if ((((unsigned int)((unsigned int)(a4))) & (0x10010000ULL)) != 0) goto loc_004E5D60;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 56)) == 0) goto loc_004E5CAE;
    if ((*(unsigned int *)(v_rip + 9572487)) >= = 5) {
        v_stack_mB9C = (unsigned int)((unsigned int)(a4));
        result = v_stack_mB9C;
        v_stack_m328 = result;
        v_stack_m320 = 4;
        v_stack_mB98 = (unsigned int)(v_rsi);
        result = v_stack_mB98;
        v_stack_m318 = result;
        v_stack_m310 = 4;
        v_stack_mA80 = a1;
        result = v_stack_mA80;
        v_stack_m308 = result;
        v_stack_m300 = 8;
        result = *(unsigned int *)(a1 + 144);
        v_stack_mB94 = (unsigned int)(result);
        result = v_stack_mB94;
        v_stack_m2F8 = result;
        v_stack_m2F0 = 4;
        result = v_stack_m348;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4852447;
        a1 = v_rip + 9572292;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    v_stack_mC48 = 1;
    result = FsRtlpOplockTryStartBreakAckTimeout(*(unsigned __int64 *)(a1 + 56) + 72, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 88), a3, a4);
    goto loc_004E5BA2;
loc_004E5CAE:
    v_stack_mC28 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 8);
    v_stack_mB90 = 1;
    result = 0;
    if ((*(unsigned __int8 *)(v_stack_mC18)) == 0) {
        a2 = 3;
        v_stack_mB90 = (unsigned int)(a2);
        result = *(unsigned __int64 *)(v_stack_mC18 + 8);
        a1 = *(unsigned __int64 *)(result + 8);
        result = *(unsigned int *)(a1 + 20);
        a1 = *(unsigned __int16 *)(v_stack_mC18 + 26);
    }
    v_stack_mC70 = 0;
    v_stack_mC78 = (unsigned __int16)(a1);
    v_stack_mC80 = (unsigned int)(result);
    v_stack_mC88 = (unsigned int)(a2);
    a3 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 8)), a1, a3, (unsigned int)(0x1000ULL));
    if ((unsigned __int8)(result) == 0) goto loc_004E5D53;
    v_stack_mC37 = 0;
    v_stack_mC48 = 1;
    result = FsRtlpOplockTryStartBreakAckTimeout(v_stack_mAC8 + 72, *(unsigned __int64 *)(v_stack_mAC8 + 88), a3, (unsigned int)(0x1000ULL));
    goto loc_004E5D57;
loc_004E5D53:
    v_stack_mC38 = (unsigned __int8)(result);
loc_004E5D57:
    goto loc_004E5B20;
loc_004E5D60:
    if ((*(unsigned int *)(v_rip + 9572073)) <= 3) goto loc_004E4E85;
    v_stack_mB8C = 0xC0000909ULL;
    v_stack_m6C8 = v_stack_mB8C;
    v_stack_m6C0 = 4;
    v_stack_mB88 = (unsigned int)((unsigned int)(a4));
    v_stack_m6B8 = v_stack_mB88;
    v_stack_m6B0 = 4;
    v_stack_mB84 = (unsigned int)(v_rsi);
    v_stack_m6A8 = v_stack_mB84;
    v_stack_m6A0 = 4;
    v_stack_mAC0 = a1;
    v_stack_m698 = v_stack_mAC0;
    v_stack_m690 = 8;
    v_stack_mB80 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_m688 = v_stack_mB80;
    v_stack_m680 = 4;
    goto loc_004E4E66;
loc_004E5E3C:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 8)))));
    if (((unsigned int)(result)) != ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 8))))) goto loc_004E616C;
    v_stack_mC28 = *(unsigned __int64 *)(a1 + 72);
loc_004E5E5B:
    if ((*(unsigned __int64 *)(a1 + 72)) == (a1 + 72)) goto loc_004E5FA5;
    if ((unsigned int)((unsigned int)(v_stack_mC30)) != 0) goto loc_004E5E89;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_mC18 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 24), (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(0x1000ULL));
    if ((unsigned __int8)(result) != 0) goto loc_004E5EBC;
loc_004E5E89:
    if ((((unsigned int)((unsigned int)(a4))) & (0x10010000ULL)) != 0) goto loc_004E5EC9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48))) & (0xFF0FFFFFULL));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48) = (unsigned int)(result);
    result = v_stack_mC48;
    if (condition_is_below) { result = 1; }
    v_stack_mC48 = (unsigned __int8)(result);
loc_004E5EBC:
    v_stack_mC28 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72));
    goto loc_004E5E5B;
loc_004E5EC9:
    if ((*(unsigned int *)(v_rip + 9571712)) <= 3) goto loc_004E4E85;
    v_stack_mB7C = 0xC0000909ULL;
    v_stack_m658 = v_stack_mB7C;
    v_stack_m650 = 4;
    v_stack_mB78 = (unsigned int)((unsigned int)(a4));
    v_stack_m648 = v_stack_mB78;
    v_stack_m640 = 4;
    v_stack_mB74 = (unsigned int)(v_rsi);
    v_stack_m638 = v_stack_mB74;
    v_stack_m630 = 4;
    v_stack_mAB8 = a1;
    v_stack_m628 = v_stack_mAB8;
    v_stack_m620 = 8;
    v_stack_mB70 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_m618 = v_stack_mB70;
    v_stack_m610 = 4;
    goto loc_004E4E66;
loc_004E5FA5:
    a1 = 0;
loc_004E5FAB:
    v_stack_mC28 = *(unsigned __int64 *)(a1 + 56);
    if ((*(unsigned __int64 *)(a1 + 56)) == (a1 + 56)) goto loc_004E6169;
    if ((unsigned int)((unsigned int)(v_stack_mC30)) != 0) goto loc_004E5FE6;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_mC18 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 24), (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(0x1000ULL));
    a1 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_004E6017;
loc_004E5FE6:
    if ((((unsigned int)((unsigned int)(a4))) & (0x10010000ULL)) != 0) goto loc_004E608D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 56)) == 0) goto loc_004E6019;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 56)) < 0) {
        result = 1;
        v_stack_mC48 = (unsigned __int8)(result);
        a1 = *(unsigned __int64 *)(a1 + 56) + 72;
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 88);
        result = FsRtlpOplockTryStartBreakAckTimeout(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(0x1000ULL));
        a1 = 0;
    }
    goto loc_004E6085;
loc_004E6019:
    v_stack_mC28 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 8);
    v_stack_mC70 = 0;
    v_stack_mC78 = 0;
    v_stack_mC80 = 0;
    v_stack_mC88 = 1;
    a4 = 0;
    a3 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 8)), 0, a3, a4);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_004E607C;
    v_stack_mC37 = 0;
    if (!(condition_is_above_or_equal)) {
        result = a1 + 1;
        v_stack_mC48 = (unsigned __int8)(result);
        a1 = *(unsigned __int64 *)(a1 + 56) + 72;
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 88);
        result = FsRtlpOplockTryStartBreakAckTimeout(a1, a2, a3, a4);
        a1 = 0;
    }
    goto loc_004E6085;
loc_004E607C:
    v_stack_mC38 = 1;
loc_004E6085:
    goto loc_004E5FAB;
loc_004E608D:
    if ((*(unsigned int *)(v_rip + 9571260)) <= 3) goto loc_004E4E85;
    v_stack_mB6C = 0xC0000909ULL;
    v_stack_m5E8 = v_stack_mB6C;
    v_stack_m5E0 = 4;
    v_stack_mB68 = (unsigned int)((unsigned int)(a4));
    v_stack_m5D8 = v_stack_mB68;
    v_stack_m5D0 = 4;
    v_stack_mB64 = (unsigned int)(v_rsi);
    v_stack_m5C8 = v_stack_mB64;
    v_stack_m5C0 = 4;
    v_stack_mAB0 = 0;
    v_stack_m5B8 = v_stack_mAB0;
    v_stack_m5B0 = 8;
    v_stack_mB60 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_m5A8 = v_stack_mB60;
    v_stack_m5A0 = 4;
    goto loc_004E4E66;
loc_004E6169:
    v_r13 = 0;
loc_004E616C:
    result = v_stack_m608;
    if (v_stack_mC38 != 0) {
        a1 = 0;
        result = FsRtlpReleaseIrpsWaitingForRH(a1, v_rip - 4853474, a3, a4);
    }
    if (v_stack_mC48 != 0) goto loc_004E61DA;
    if ((*(unsigned __int64 *)(a1 + 72)) == (a1 + 72)) goto loc_004E61DA;
    if ((*(unsigned __int64 *)(a1 + 72)) >= (a1 + 72)) goto loc_004E61DA;
    if (v_stack_mC30 != 0) goto loc_004E61C8;
loc_004E619B:
    v_stack_mC28 = *(unsigned __int64 *)(a1 + 72);
    if ((*(unsigned __int64 *)(a1 + 72)) == (a1 + 72)) goto loc_004E61DA;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 24), *(unsigned __int64 *)(v_stack_mC18 + 48), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_004E61D5;
loc_004E61C8:
    v_stack_mC48 = 1;
    goto loc_004E61E0;
loc_004E61D5:
    goto loc_004E619B;
loc_004E61DA:
loc_004E61E0:
    result = FsRtlpComputeShareableOplockState(a1, *(unsigned __int64 *)(v_stack_mC18 + 48), a3, a4);
loc_004E61E8:
    goto loc_004E53A5;
loc_004E61F2:
    result = FsRtlpComputeShareableOplockState(a1, *(unsigned __int64 *)(v_stack_mC18 + 48), a3, a4);
loc_004E61FA:
    v_r13 = 0;
    goto loc_004E539A;
loc_004E6202:
    if ((*(unsigned int *)(v_rip + 9570887)) >= = 5) {
        v_stack_mB1C = (unsigned int)((unsigned int)(a4));
        result = v_stack_mB1C;
        v_stack_m88 = result;
        v_stack_m80 = 4;
        v_stack_mB5C = (unsigned int)(v_stack_mC40);
        result = v_stack_mB5C;
        v_stack_m78 = result;
        v_stack_m70 = 4;
        v_stack_mA60 = a1;
        result = v_stack_mA60;
        v_stack_m68 = result;
        v_stack_m60 = 8;
        v_stack_mB58 = (unsigned int)(a1);
        result = v_stack_mB58;
        v_stack_m58 = result;
        v_stack_m50 = 4;
        result = v_stack_mA8;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4856201;
        a1 = v_rip + 9570698;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned int *)(a1 + 144);
        result = (unsigned int)((result) & (32));
        result = (unsigned int)((result) | (0x805040ULL));
        *(unsigned int *)(a1 + 144) = (unsigned int)(result);
    }
    v_r13 = 0;
    if ((((unsigned int)((unsigned int)(v_stack_mC30))) & ((unsigned int)(v_stack_mC40))) == 0) goto loc_004E61E8;
    goto loc_004E57E5;
loc_004E62FC:
    if (((unsigned int)(result)) == 0x107040ULL) goto loc_004E6BDD;
    if (((unsigned int)(result)) == 0x307040ULL) goto loc_004E6A8A;
    if (((unsigned int)(result)) == 0x507040ULL) goto loc_004E6942;
    if (((unsigned int)(result)) == 0x803000ULL) goto loc_004E66DF;
    if (((unsigned int)(result)) == 0x805040ULL) goto loc_004E6611;
    if (((unsigned int)(result)) == 0x807040ULL) goto loc_004E64F7;
loc_004E633E:
    if (((unsigned int)(result)) >= 0x807040ULL) goto loc_004E6429;
    if ((*(unsigned int *)(v_rip + 9570561)) >= = 5) {
        v_stack_mB54 = (unsigned int)((unsigned int)(a4));
        result = v_stack_mB54;
        v_stack_m208 = result;
        v_stack_m200 = 4;
        v_stack_mB50 = (unsigned int)(v_stack_mC40);
        result = v_stack_mB50;
        v_stack_m1F8 = result;
        v_stack_m1F0 = 4;
        v_stack_mA58 = a1;
        result = v_stack_mA58;
        v_stack_m1E8 = result;
        v_stack_m1E0 = 8;
        v_stack_mB4C = (unsigned int)(a1);
        result = v_stack_mB4C;
        v_stack_m1D8 = result;
        v_stack_m1D0 = 4;
        result = v_stack_m228;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4855999;
        a1 = v_rip + 9570372;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    v_stack_mC48 = 1;
    v_r13 = 0;
    goto loc_004E53A5;
loc_004E6429:
    if ((*(unsigned int *)(v_rip + 9570336)) <= 2) goto loc_004E61FA;
    v_stack_mB48 = (unsigned int)((unsigned int)(a4));
    v_stack_m1A8 = v_stack_mB48;
    v_stack_m1A0 = 4;
    v_stack_mB44 = (unsigned int)(v_stack_mC40);
    v_stack_m198 = v_stack_mB44;
    v_stack_m190 = 4;
    v_stack_mA50 = a1;
    v_stack_m188 = v_stack_mA50;
    v_stack_m180 = 8;
    v_stack_mB40 = (unsigned int)(a1);
    v_stack_m178 = v_stack_mB40;
    v_stack_m170 = 4;
    v_stack_mC80 = v_stack_m1C8;
    v_stack_mC88 = 6;
    a4 = 0;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9570147, v_rip - 4856333, a3, a4);
    goto loc_004E61FA;
loc_004E64F7:
    if ((*(unsigned int *)(v_rip + 9570130)) >= = 5) {
        v_stack_mB3C = (unsigned int)((unsigned int)(a4));
        result = v_stack_mB3C;
        v_stack_m148 = result;
        v_stack_m140 = 4;
        v_stack_mB38 = (unsigned int)(v_stack_mC40);
        result = v_stack_mB38;
        v_stack_m138 = result;
        v_stack_m130 = 4;
        v_stack_mA48 = a1;
        result = v_stack_mA48;
        v_stack_m128 = result;
        v_stack_m120 = 8;
        v_stack_mB34 = (unsigned int)(v_rip + 9570147);
        result = v_stack_mB34;
        v_stack_m118 = result;
        v_stack_m110 = 4;
        result = v_stack_m168;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4857501;
        a1 = v_rip + 9569941;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & ((unsigned int)((unsigned int)(0x40000080ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x40000080ULL)))) goto loc_004E6603;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(a7)), *(unsigned __int16 *)(a8));
    v_r13 = 0;
    if (!sign_flag) goto loc_004E539A;
    goto loc_004E6606;
loc_004E6603:
    v_r13 = 0;
loc_004E6606:
    goto loc_004E57E5;
loc_004E6611:
    if ((*(unsigned int *)(v_rip + 9569848)) <= 5) goto loc_004E62E5;
    v_stack_mB30 = (unsigned int)((unsigned int)(a4));
    v_stack_mE8 = v_stack_mB30;
    v_stack_mE0 = 4;
    v_stack_mB2C = (unsigned int)(v_stack_mC40);
    v_stack_mD8 = v_stack_mB2C;
    v_stack_mD0 = 4;
    v_stack_mA40 = a1;
    v_stack_mC8 = v_stack_mA40;
    v_stack_mC0 = 8;
    v_stack_mB28 = (unsigned int)(v_stack_mC40);
    v_stack_mB8 = v_stack_mB28;
    v_stack_mB0 = 4;
    v_stack_mC80 = v_stack_m108;
    v_stack_mC88 = 6;
    a4 = 0;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9569659, v_rip - 4857351, a3, a4);
    goto loc_004E62E5;
loc_004E66DF:
    if ((*(unsigned int *)(v_rip + 9569642)) >= = 5) {
        v_stack_mB24 = (unsigned int)((unsigned int)(a4));
        result = v_stack_mB24;
        v_stack_m508 = result;
        v_stack_m500 = 4;
        v_stack_mB20 = (unsigned int)(v_stack_mC40);
        result = v_stack_mB20;
        v_stack_m4F8 = result;
        v_stack_m4F0 = 4;
        v_stack_mA38 = a1;
        result = v_stack_mA38;
        v_stack_m4E8 = result;
        v_stack_m4E0 = 8;
        v_stack_mAD4 = (unsigned int)(v_rip + 9569659);
        result = v_stack_mAD4;
        v_stack_m4D8 = result;
        v_stack_m4D0 = 4;
        result = v_stack_m528;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4855397;
        a1 = v_rip + 9569453;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if ((((unsigned int)(v_stack_mC40)) & (0x3000ULL)) == 0) goto loc_004E61FA;
    if (sign_flag) goto loc_004E68A6;
    if ((((unsigned int)((unsigned int)(a4))) & (0x10010000ULL)) == 0) goto loc_004E68A6;
    if ((*(unsigned int *)(v_rip + 9569407)) <= 3) goto loc_004E4E85;
    v_stack_mB18 = 0xC0000909ULL;
    v_stack_m578 = v_stack_mB18;
    v_stack_m570 = 4;
    v_stack_mB14 = (unsigned int)((unsigned int)(a4));
    v_stack_m568 = v_stack_mB14;
    v_stack_m560 = 4;
    v_stack_mB10 = (unsigned int)(v_stack_mC40);
    v_stack_m558 = v_stack_mB10;
    v_stack_m550 = 4;
    v_stack_mAA8 = a1;
    v_stack_m548 = v_stack_mAA8;
    v_stack_m540 = 8;
    v_stack_mB0C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_m538 = v_stack_mB0C;
    v_stack_m530 = 4;
    goto loc_004E4E66;
loc_004E68A6:
    if ((*(unsigned int *)(v_rip + 9569407)) >= 3) goto loc_004E61FA;
loc_004E68CA:
    v_stack_mC28 = *(unsigned __int64 *)(a1 + 72);
    if ((*(unsigned __int64 *)(a1 + 72)) == (a1 + 72)) goto loc_004E61FA;
    result = 0;
    if (v_stack_mC30 != 0) goto loc_004E6905;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_mC18 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 24), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004E6905;
    goto loc_004E692B;
loc_004E6905:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & ((unsigned int)((unsigned int)(0x40000080ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x40000080ULL)))) goto loc_004E6930;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 24), (unsigned int)(*(unsigned int *)(a7)), *(unsigned __int16 *)(a8));
    if (sign_flag) goto loc_004E6930;
loc_004E692B:
    goto loc_004E68CA;
loc_004E6930:
    if ((((unsigned int)((unsigned int)(a4))) & (0x10010000ULL)) != 0) goto loc_004E4E85;
    goto loc_004E6411;
loc_004E6942:
    if ((*(unsigned int *)(v_rip + 9569031)) >= = 5) {
        v_stack_mB08 = (unsigned int)((unsigned int)(a4));
        result = v_stack_mB08;
        v_stack_m4A8 = result;
        v_stack_m4A0 = 4;
        v_stack_mB04 = (unsigned int)(v_stack_mC40);
        result = v_stack_mB04;
        v_stack_m498 = result;
        v_stack_m490 = 4;
        v_stack_mA28 = a1;
        result = v_stack_mA28;
        v_stack_m488 = result;
        v_stack_m480 = 8;
        v_stack_mB00 = (unsigned int)(v_stack_mC40);
        result = v_stack_mB00;
        v_stack_m478 = result;
        v_stack_m470 = 4;
        result = v_stack_m4C8;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4858820;
        a1 = v_rip + 9568842;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if (((unsigned int)(v_stack_mC40)) != 0x2000ULL) goto loc_004E6A67;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & ((unsigned int)((unsigned int)(0x40000080ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x40000080ULL)))) goto loc_004E6A57;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(a7)), *(unsigned __int16 *)(a8));
    v_r13 = 0;
    if (!sign_flag) goto loc_004E539F;
loc_004E6A57:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (0x107040ULL));
    goto loc_004E6A7F;
loc_004E6A67:
    if (condition_is_above_or_equal) goto loc_004E6411;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (0x807040ULL));
loc_004E6A7F:
    *(unsigned int *)(a1 + 144) = (unsigned int)(result);
    goto loc_004E6411;
loc_004E6A8A:
    if ((*(unsigned int *)(v_rip + 9568703)) >= = 5) {
        v_stack_mAFC = (unsigned int)((unsigned int)(a4));
        result = v_stack_mAFC;
        v_stack_m268 = result;
        v_stack_m260 = 4;
        v_stack_mAF8 = (unsigned int)(v_stack_mC40);
        result = v_stack_mAF8;
        v_stack_m258 = result;
        v_stack_m250 = 4;
        v_stack_mA20 = a1;
        result = v_stack_mA20;
        v_stack_m248 = result;
        v_stack_m240 = 8;
        v_stack_mAF4 = (unsigned int)(v_stack_mC40);
        result = v_stack_mAF4;
        v_stack_m238 = result;
        v_stack_m230 = 4;
        result = v_stack_m288;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4859038;
        a1 = v_rip + 9568514;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if (((unsigned int)(v_stack_mC40)) != ((unsigned int)((unsigned int)(0x40000080ULL)))) goto loc_004E6B68;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (0x107040ULL));
    goto loc_004E6B7E;
loc_004E6B68:
    v_rsi = (unsigned int)((v_stack_mC40) & ((unsigned int)(a8)));
    if (((unsigned int)(v_rsi)) != ((unsigned int)(a8))) goto loc_004E6B84;
loc_004E6B70:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (0x807040ULL));
loc_004E6B7E:
    *(unsigned int *)(a1 + 144) = (unsigned int)(result);
loc_004E6B84:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & ((unsigned int)((unsigned int)(0x40000080ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x40000080ULL)))) goto loc_004E6BCA;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(a7)), *(unsigned __int16 *)(a8));
    v_r13 = 0;
    if (!sign_flag) goto loc_004E539F;
    goto loc_004E6BCD;
loc_004E6BCA:
    v_r13 = 0;
loc_004E6BCD:
    v_stack_mC48 = 1;
    goto loc_004E53A5;
loc_004E6BDD:
    if ((*(unsigned int *)(v_rip + 9568364)) >= = 5) {
        v_stack_mAF0 = (unsigned int)((unsigned int)(a4));
        result = v_stack_mAF0;
        v_stack_m968 = result;
        v_stack_m960 = 4;
        v_stack_mAEC = (unsigned int)(v_stack_mC40);
        result = v_stack_mAEC;
        v_stack_m958 = result;
        v_stack_m950 = 4;
        v_stack_mA18 = a1;
        result = v_stack_mA18;
        v_stack_m948 = result;
        v_stack_m940 = 8;
        v_stack_mAE8 = (unsigned int)(v_stack_mC40);
        result = v_stack_mAE8;
        v_stack_m938 = result;
        v_stack_m930 = 4;
        result = v_stack_m988;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4859155;
        a1 = v_rip + 9568175;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if (condition_is_above_or_equal) goto loc_004E6B84;
    goto loc_004E6B70;
loc_004E6CB5:
    result = Feature_Servicing_CloseOplockTimeoutGap__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (64));
    if ((unsigned int)(result) == 0) goto loc_004E6CF2;
    if ((unsigned int)(a1) != 0) goto loc_004E6CF6;
    if ((*(unsigned __int64 *)(a1 + 72)) == (a1 + 72)) goto loc_004E6D09;
loc_004E6CD7:
    if ((*(unsigned __int64 *)(a1 + 72)) == (a1 + 72)) goto loc_004E6D09;
    result = FsRtlpOplockTryStartBreakAckTimeout(*(unsigned __int64 *)(a1 + 72) + 72, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 88), a3, a4);
    goto loc_004E6CD7;
loc_004E6CF2:
    if ((unsigned int)(*(unsigned __int64 *)(a1 + 72) + 72) != 0) {
        a2 = *(unsigned __int64 *)(a1 + 184);
        a1 = a1 + 168;
        result = FsRtlpOplockTryStartBreakAckTimeout(a1, a2, a3, a4);
    }
    if (v_stack_mC37 != 0) {
        a3 = 1;
        a2 = 0;
        a1 = a1;
        result = FsRtlpModifyThreadPriorities(a1, a2, a3, a4);
        a2 = 0;
        a1 = a1;
        result = FsRtlpOplockSendModernAppTermination(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(v_stack_mAA8) = 0;
    v_stack_mC58 = v_stack_mAB0;
    v_stack_mC60 = a14;
    v_stack_mC68 = v_stack_mAB8;
    v_stack_mC70 = a12;
    v_stack_mC78 = (unsigned __int8)(v_stack_mC36);
    v_stack_mC80 = v_stack_mA08;
    v_stack_mC88 = a11;
    result = FsRtlpWaitOnIrp(a1, v_stack_mC40, v_stack_mAC0, a10);
    v_stack_mC34 = (unsigned int)(result);
    goto loc_004E6E98;
loc_004E6DAC:
    if ((*(unsigned int *)(v_rip + 9567901)) <= 5) goto loc_004E6E94;
    v_stack_mAE4 = (unsigned int)(v_stack_mC40);
    v_stack_m8F8 = v_stack_mAE4;
    v_stack_m8F0 = 4;
    v_stack_mAE0 = (unsigned int)((unsigned int)(a4));
    v_stack_m8E8 = v_stack_mAE0;
    v_stack_m8E0 = 4;
    v_stack_mC18 = (unsigned int)(v_stack_mC40);
    v_stack_m8D8 = v_stack_mC18;
    v_stack_m8D0 = 4;
    v_stack_mA10 = a1;
    v_stack_m8C8 = v_stack_mA10;
    v_stack_m8C0 = 8;
    v_stack_mC40 = (unsigned int)(result);
    v_stack_m8B8 = v_stack_mC40;
    v_stack_m8B0 = 4;
loc_004E6E73:
    v_stack_mC80 = v_stack_m918;
    v_stack_mC88 = 7;
    a4 = 0;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9567683, v_rip - 4857592, a3, a4);
    a2 = 0;
loc_004E6E94:
    v_stack_mC34 = 0;
loc_004E6E98:
loc_004E6E9C:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (0xC70ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpOplockBreakByCacheFlags(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, uint32_t Arg6, void *Arg7, void *Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, int64_t Arg14, int64_t Arg15, int64_t Arg16)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r13;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint64_t v_stack_m348;
    uint64_t v_stack_m350;
    uint64_t v_stack_m358;
    uint64_t v_stack_m360;
    uint64_t v_stack_m368;
    uint64_t v_stack_m370;
    uint64_t v_stack_m378;
    uint64_t v_stack_m380;
    uint64_t v_stack_m388;
    uint64_t v_stack_m3A8;
    uint64_t v_stack_m3B0;
    uint64_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint64_t v_stack_m3E8;
    uint64_t v_stack_m408;
    uint64_t v_stack_m410;
    uint64_t v_stack_m418;
    uint64_t v_stack_m420;
    uint64_t v_stack_m428;
    uint64_t v_stack_m430;
    uint64_t v_stack_m438;
    uint64_t v_stack_m440;
    uint64_t v_stack_m448;
    uint64_t v_stack_m468;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint64_t v_stack_m488;
    uint64_t v_stack_m490;
    uint64_t v_stack_m498;
    uint64_t v_stack_m4A0;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m4C8;
    uint64_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint64_t v_stack_m4E0;
    uint64_t v_stack_m4E8;
    uint64_t v_stack_m4F0;
    uint64_t v_stack_m4F8;
    uint64_t v_stack_m50;
    uint64_t v_stack_m500;
    uint64_t v_stack_m508;
    uint64_t v_stack_m528;
    uint64_t v_stack_m530;
    uint64_t v_stack_m538;
    uint64_t v_stack_m540;
    uint64_t v_stack_m548;
    uint64_t v_stack_m550;
    uint64_t v_stack_m558;
    uint64_t v_stack_m560;
    uint64_t v_stack_m568;
    uint64_t v_stack_m570;
    uint64_t v_stack_m578;
    uint64_t v_stack_m58;
    uint64_t v_stack_m598;
    uint64_t v_stack_m5A0;
    uint64_t v_stack_m5A8;
    uint64_t v_stack_m5B0;
    uint64_t v_stack_m5B8;
    uint64_t v_stack_m5C0;
    uint64_t v_stack_m5C8;
    uint64_t v_stack_m5D0;
    uint64_t v_stack_m5D8;
    uint64_t v_stack_m5E0;
    uint64_t v_stack_m5E8;
    uint64_t v_stack_m60;
    uint64_t v_stack_m608;
    uint64_t v_stack_m610;
    uint64_t v_stack_m618;
    uint64_t v_stack_m620;
    uint64_t v_stack_m628;
    uint64_t v_stack_m630;
    uint64_t v_stack_m638;
    uint64_t v_stack_m640;
    uint64_t v_stack_m648;
    uint64_t v_stack_m650;
    uint64_t v_stack_m658;
    uint64_t v_stack_m678;
    uint64_t v_stack_m68;
    uint64_t v_stack_m680;
    uint64_t v_stack_m688;
    uint64_t v_stack_m690;
    uint64_t v_stack_m698;
    uint64_t v_stack_m6A0;
    uint64_t v_stack_m6A8;
    uint64_t v_stack_m6B0;
    uint64_t v_stack_m6B8;
    uint64_t v_stack_m6C0;
    uint64_t v_stack_m6C8;
    uint64_t v_stack_m6E8;
    uint64_t v_stack_m6F0;
    uint64_t v_stack_m6F8;
    uint64_t v_stack_m70;
    uint64_t v_stack_m700;
    uint64_t v_stack_m708;
    uint64_t v_stack_m710;
    uint64_t v_stack_m718;
    uint64_t v_stack_m720;
    uint64_t v_stack_m728;
    uint64_t v_stack_m730;
    uint64_t v_stack_m738;
    uint64_t v_stack_m758;
    uint64_t v_stack_m760;
    uint64_t v_stack_m768;
    uint64_t v_stack_m770;
    uint64_t v_stack_m778;
    uint64_t v_stack_m78;
    uint64_t v_stack_m780;
    uint64_t v_stack_m788;
    uint64_t v_stack_m790;
    uint64_t v_stack_m798;
    uint64_t v_stack_m7A0;
    uint64_t v_stack_m7A8;
    uint64_t v_stack_m7C8;
    uint64_t v_stack_m7D0;
    uint64_t v_stack_m7D8;
    uint64_t v_stack_m7E0;
    uint64_t v_stack_m7E8;
    uint64_t v_stack_m7F0;
    uint64_t v_stack_m7F8;
    uint64_t v_stack_m80;
    uint64_t v_stack_m800;
    uint64_t v_stack_m808;
    uint64_t v_stack_m810;
    uint64_t v_stack_m818;
    uint64_t v_stack_m838;
    uint64_t v_stack_m840;
    uint64_t v_stack_m848;
    uint64_t v_stack_m850;
    uint64_t v_stack_m858;
    uint64_t v_stack_m860;
    uint64_t v_stack_m868;
    uint64_t v_stack_m870;
    uint64_t v_stack_m878;
    uint64_t v_stack_m88;
    uint64_t v_stack_m880;
    uint64_t v_stack_m888;
    uint64_t v_stack_m8A8;
    uint64_t v_stack_m8B0;
    uint64_t v_stack_m8B8;
    uint64_t v_stack_m8C0;
    uint64_t v_stack_m8C8;
    uint64_t v_stack_m8D0;
    uint64_t v_stack_m8D8;
    uint64_t v_stack_m8E0;
    uint64_t v_stack_m8E8;
    uint64_t v_stack_m8F0;
    uint64_t v_stack_m8F8;
    uint64_t v_stack_m918;
    uint64_t v_stack_m920;
    uint64_t v_stack_m928;
    uint64_t v_stack_m930;
    uint64_t v_stack_m938;
    uint64_t v_stack_m940;
    uint64_t v_stack_m948;
    uint64_t v_stack_m950;
    uint64_t v_stack_m958;
    uint64_t v_stack_m960;
    uint64_t v_stack_m968;
    uint64_t v_stack_m988;
    uint64_t v_stack_m990;
    uint64_t v_stack_m998;
    uint64_t v_stack_m9A0;
    uint64_t v_stack_m9A8;
    uint64_t v_stack_m9B0;
    uint64_t v_stack_m9B8;
    uint64_t v_stack_m9C0;
    uint64_t v_stack_m9C8;
    uint64_t v_stack_m9E8;
    uint64_t v_stack_mA08;
    uint64_t v_stack_mA10;
    uint64_t v_stack_mA18;
    uint64_t v_stack_mA20;
    uint64_t v_stack_mA28;
    uint64_t v_stack_mA30;
    uint64_t v_stack_mA38;
    uint64_t v_stack_mA40;
    uint64_t v_stack_mA48;
    uint64_t v_stack_mA50;
    uint64_t v_stack_mA58;
    uint64_t v_stack_mA60;
    uint64_t v_stack_mA68;
    uint64_t v_stack_mA70;
    uint64_t v_stack_mA78;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mA80;
    uint64_t v_stack_mA88;
    uint64_t v_stack_mA90;
    uint64_t v_stack_mA98;
    uint64_t v_stack_mAA0;
    uint64_t v_stack_mAA8;
    uint64_t v_stack_mAB0;
    uint64_t v_stack_mAB8;
    uint64_t v_stack_mAC0;
    uint64_t v_stack_mAC8;
    uint32_t v_stack_mACC;
    uint32_t v_stack_mAD0;
    uint32_t v_stack_mAD4;
    uint32_t v_stack_mAD8;
    uint32_t v_stack_mAE0;
    uint32_t v_stack_mAE4;
    uint32_t v_stack_mAE8;
    uint32_t v_stack_mAEC;
    uint32_t v_stack_mAF0;
    uint32_t v_stack_mAF4;
    uint32_t v_stack_mAF8;
    uint32_t v_stack_mAFC;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB00;
    uint32_t v_stack_mB04;
    uint32_t v_stack_mB08;
    uint32_t v_stack_mB0C;
    uint32_t v_stack_mB10;
    uint32_t v_stack_mB14;
    uint32_t v_stack_mB18;
    uint32_t v_stack_mB1C;
    uint32_t v_stack_mB20;
    uint32_t v_stack_mB24;
    uint32_t v_stack_mB28;
    uint32_t v_stack_mB2C;
    uint32_t v_stack_mB30;
    uint32_t v_stack_mB34;
    uint32_t v_stack_mB38;
    uint32_t v_stack_mB3C;
    uint32_t v_stack_mB40;
    uint32_t v_stack_mB44;
    uint32_t v_stack_mB48;
    uint32_t v_stack_mB4C;
    uint32_t v_stack_mB50;
    uint32_t v_stack_mB54;
    uint32_t v_stack_mB58;
    uint32_t v_stack_mB5C;
    uint32_t v_stack_mB60;
    uint32_t v_stack_mB64;
    uint32_t v_stack_mB68;
    uint32_t v_stack_mB6C;
    uint32_t v_stack_mB70;
    uint32_t v_stack_mB74;
    uint32_t v_stack_mB78;
    uint32_t v_stack_mB7C;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mB80;
    uint32_t v_stack_mB84;
    uint32_t v_stack_mB88;
    uint32_t v_stack_mB8C;
    uint32_t v_stack_mB90;
    uint32_t v_stack_mB94;
    uint32_t v_stack_mB98;
    uint32_t v_stack_mB9C;
    uint32_t v_stack_mBA0;
    uint32_t v_stack_mBA4;
    uint32_t v_stack_mBA8;
    uint32_t v_stack_mBAC;
    uint32_t v_stack_mBB0;
    uint32_t v_stack_mBB4;
    uint32_t v_stack_mBB8;
    uint32_t v_stack_mBBC;
    uint32_t v_stack_mBC0;
    uint32_t v_stack_mBC4;
    uint32_t v_stack_mBC8;
    uint32_t v_stack_mBCC;
    uint32_t v_stack_mBD0;
    uint32_t v_stack_mBD4;
    uint32_t v_stack_mBD8;
    uint32_t v_stack_mBDC;
    uint32_t v_stack_mBE0;
    uint32_t v_stack_mBE4;
    uint32_t v_stack_mBE8;
    uint32_t v_stack_mBEC;
    uint32_t v_stack_mBF0;
    uint32_t v_stack_mBF4;
    uint32_t v_stack_mBF8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC00;
    uint32_t v_stack_mC08;
    uint32_t v_stack_mC0C;
    uint32_t v_stack_mC10;
    uint64_t v_stack_mC18;
    uint8_t v_stack_mC20;
    uint64_t v_stack_mC28;
    uint32_t v_stack_mC30;
    uint32_t v_stack_mC34;
    uint8_t v_stack_mC36;
    uint8_t v_stack_mC37;
    uint8_t v_stack_mC38;
    uint64_t v_stack_mC40;
    uint8_t v_stack_mC48;
    uint64_t v_stack_mC58;
    uint64_t v_stack_mC60;
    uint64_t v_stack_mC68;
    uint8_t v_stack_mC70;
    uint16_t v_stack_mC78;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mC80;
    uint32_t v_stack_mC88;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;

    local_rsp = (local_rsp) - (0xC70ULL);
    result = (*(uint64_t *)(v_rip + 0x925D94)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mC40 = Arg3;
    v_stack_mC18 = Arg2;
    v_stack_mAC0 = Arg9;
    v_stack_mAB8 = Arg13;
    v_stack_mAA8 = Arg15;
    v_stack_mAB0 = Arg16;
    Arg2 = 0;
    v_stack_mC34 = 0;
    Arg1 = 0;
    v_stack_mA08 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x9F8) = 0;
    v_stack_mC48 = 0;
    v_stack_mC38 = 0;
    v_stack_mC36 = 0;
    v_stack_mC37 = (uint8_t)(Arg2 + 1);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (8));
    v_stack_mC30 = (uint32_t)(Arg1);
    result = Arg3;
    if ((*(uint32_t *)(v_rip + 0x9221F2)) >= = 5) {
        *(uint32_t *)(local_rsp - 0xC10) = (uint32_t)((uint32_t)(Arg4));
        result = local_rsp - 3088;
        *(uint64_t *)(local_rsp - 0x9C8) = result;
        *(uint64_t *)(local_rsp - 0x9C0) = 4;
        v_stack_mC0C = (uint32_t)((uint32_t)(Arg6));
        result = local_rsp - 3084;
        *(uint64_t *)(local_rsp - 0x9B8) = result;
        *(uint64_t *)(local_rsp - 0x9B0) = 4;
        *(void **)(local_rsp - 0xAE0) = Arg1;
        result = local_rsp - 2784;
        *(uint64_t *)(local_rsp - 0x9A8) = result;
        *(uint64_t *)(local_rsp - 0x9A0) = 8;
        result = *(uint32_t *)(arg1 + 0x90);
        v_stack_mC08 = (uint32_t)(result);
        result = local_rsp - 3080;
        *(uint64_t *)(local_rsp - 0x998) = result;
        *(uint64_t *)(local_rsp - 0x990) = 4;
        result = local_rsp - 2536;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4848741;
        Arg1 = v_rip + 9576768;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_mC30;
        Arg4 = v_stack_mC18;
        result = v_stack_mC40;
        Arg2 = 0;
        Arg3 = Arg2 + 1;
    }
    if (((uint32_t)((uint32_t)(Arg6))) == 0x7000ULL) goto loc_004E4C6D;
    if (((uint32_t)((uint32_t)(Arg6))) == ((uint32_t)((uint32_t)(0x5000ULL)))) goto loc_004E4C6D;
    if (((uint32_t)((uint32_t)(Arg6))) == ((uint32_t)((uint32_t)(0x4000ULL)))) goto loc_004E4C6D;
    if (((uint32_t)((uint32_t)(Arg6))) == 0x2000ULL) goto loc_004E4C6D;
    if (result != 0) {
        *(uint32_t *)(result + 0x30) = 0xC00000E3ULL;
        Arg2 = (uint8_t)(Arg3);
        Arg1 = result;
        result = IofCompleteRequest(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x9220D0)) >= = 3) {
        v_stack_mC08 = 0xC00000E3ULL;
        result = v_stack_mC08;
        v_stack_m968 = result;
        v_stack_m960 = 4;
        v_stack_mC0C = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mC0C;
        v_stack_m958 = result;
        v_stack_m950 = 4;
        v_stack_mC10 = (uint32_t)((uint32_t)(Arg6));
        result = v_stack_mC10;
        v_stack_m948 = result;
        v_stack_m940 = 4;
        v_stack_mC40 = Arg1;
        result = v_stack_mC40;
        v_stack_m938 = result;
        v_stack_m930 = 8;
        result = *(uint32_t *)(arg1 + 0x90);
        v_stack_mC30 = (uint32_t)(result);
        result = v_stack_mC30;
        v_stack_m928 = result;
        v_stack_m920 = 4;
        result = v_stack_m988;
        v_stack_mC80 = result;
        v_stack_mC88 = 7;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4849182;
        Arg1 = v_rip + 9576434;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_004E6E9C;
loc_004E4C6D:
    if (Arg1 == NULL) goto loc_004E6E98;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)))) == 0) goto loc_004E6DAC;
    if ((((uint32_t)((uint32_t)(Arg6))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90))))) == 0) goto loc_004E6DAC;
    if ((uint32_t)(Arg1) != 0) goto loc_004E4D7F;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(Arg4 + 0x30), *(uint64_t *)(arg1 + 0x8), (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg4);
    Arg2 = 0;
    if ((uint8_t)(result) == 0) goto loc_004E4D7F;
    if ((*(uint32_t *)(v_rip + 0x921F9C)) <= 5) goto loc_004E6E94;
    v_stack_mC08 = 0;
    v_stack_m818 = v_stack_mC08;
    v_stack_m810 = 4;
    v_stack_mC0C = (uint32_t)((uint32_t)(Arg4));
    v_stack_m808 = v_stack_mC0C;
    v_stack_m800 = 4;
    v_stack_mC10 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m7F8 = v_stack_mC10;
    v_stack_m7F0 = 4;
    v_stack_mA88 = Arg1;
    v_stack_m7E8 = v_stack_mA88;
    v_stack_m7E0 = 8;
    v_stack_mC30 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_m7D8 = v_stack_mC30;
    v_stack_m7D0 = 4;
    goto loc_004E6E73;
loc_004E4D7F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)))) & (64)) == 0) goto loc_004E4E92;
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x10010000ULL)) == 0) goto loc_004E4E92;
    if ((*(uint32_t *)(v_rip + 0x921EAE)) <= 3) goto loc_004E4E85;
    v_stack_mC34 = 0xC0000909ULL;
    v_stack_m7A8 = v_stack_mC34;
    v_stack_m7A0 = 4;
    v_stack_mAD8 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m798 = v_stack_mAD8;
    v_stack_m790 = 4;
    v_stack_mAD0 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m788 = v_stack_mAD0;
    v_stack_m780 = 4;
    v_stack_mA78 = Arg1;
    v_stack_m778 = v_stack_mA78;
    v_stack_m770 = 8;
    v_stack_mACC = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_m768 = v_stack_mACC;
    v_stack_m760 = 4;
loc_004E4E66:
    v_stack_mC80 = v_stack_m7C8;
    Arg4 = 0;
    v_stack_mC88 = 7;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9575888, v_rip - 4850028, Arg3, Arg4);
loc_004E4E85:
    v_stack_mC34 = 0xC0000909ULL;
    goto loc_004E6E98;
loc_004E4E92:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_rip + 9575888))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(0x105040ULL)))) goto loc_004E62FC;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x105040ULL)))) goto loc_004E6202;
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(0x1000ULL))));
    if (condition_is_equal) goto loc_004E57EF;
    result = (uint32_t)((result) - (16));
    if (condition_is_equal) goto loc_004E57EF;
    result = (uint32_t)((result) - (0x1FF0ULL));
    if (condition_is_equal) goto loc_004E5A39;
    result = (uint32_t)((result) - (0x2040ULL));
    if (condition_is_equal) goto loc_004E554B;
    result = (uint32_t)((result) - (0x2000ULL));
    if (condition_is_equal) goto loc_004E51DB;
    result = (uint32_t)((result) - (0x3FC0ULL));
    if (condition_is_equal) goto loc_004E57EF;
    result = (uint32_t)((result) - (0xF8000ULL));
    if (condition_is_not_equal) goto loc_004E633E;
    if ((*(uint32_t *)(v_rip + 0x921D4C)) >= = 5) {
        v_stack_mBF8 = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mBF8;
        v_stack_m9C8 = result;
        v_stack_m9C0 = 4;
        v_stack_mBF4 = (uint32_t)((uint32_t)(Arg6));
        result = v_stack_mBF4;
        v_stack_m9B8 = result;
        v_stack_m9B0 = 4;
        v_stack_mA70 = Arg1;
        result = v_stack_mA70;
        v_stack_m9A8 = result;
        v_stack_m9A0 = 8;
        v_stack_mBF0 = (uint32_t)(v_rip + 9575888);
        result = v_stack_mBF0;
        v_stack_m998 = result;
        v_stack_m990 = 4;
        result = v_stack_m9E8;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4849498;
        Arg1 = v_rip + 9575567;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = 0;
    v_stack_mC20 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & ((uint32_t)((uint32_t)(0x1000ULL))));
    if (condition_is_equal) goto loc_004E5135;
loc_004E4FE1:
    v_stack_mC28 = *(uint64_t *)(arg1 + 0x48);
    if ((*(uint64_t *)(arg1 + 0x48)) == (Arg1 + 72)) goto loc_004E5128;
    if (v_stack_mC30 != 0) goto loc_004E501A;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_mC18 + 0x30), *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18), (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg4);
    Arg1 = 0;
    if ((uint8_t)(result) != 0) goto loc_004E5047;
loc_004E501A:
    v_stack_mC20 = 1;
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x10010000ULL)) != 0) goto loc_004E504C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30))) & (0xFF0FFFFFULL));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30) = (uint32_t)(result);
loc_004E5047:
    goto loc_004E4FE1;
loc_004E504C:
    if ((*(uint32_t *)(v_rip + 0x921BFD)) <= 3) goto loc_004E4E85;
    v_stack_mBEC = 0xC0000909ULL;
    v_stack_m738 = v_stack_mBEC;
    v_stack_m730 = 4;
    v_stack_mBE8 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m728 = v_stack_mBE8;
    v_stack_m720 = 4;
    v_stack_mBE4 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m718 = v_stack_mBE4;
    v_stack_m710 = 4;
    v_stack_mA68 = 0;
    v_stack_m708 = v_stack_mA68;
    v_stack_m700 = 8;
    v_stack_mBE0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_m6F8 = v_stack_mBE0;
    v_stack_m6F0 = 4;
    goto loc_004E4E66;
loc_004E5128:
    result = FsRtlpComputeShareableOplockState(0, v_rip - 4849966, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg4);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & ((uint32_t)((uint32_t)(0x1000ULL))));
loc_004E5135:
    local_r13 = 0;
    if (condition_is_above_or_equal) goto loc_004E539A;
    if (1 != 0) goto loc_004E6606;
    if ((uint32_t)(result) != 0) goto loc_004E539A;
loc_004E516D:
    v_stack_mC28 = *(uint64_t *)(arg1 + 0x48);
    if ((*(uint64_t *)(arg1 + 0x48)) == (Arg1 + 72)) goto loc_004E61FA;
    result = 0;
    if (v_stack_mC30 != 0) goto loc_004E51A8;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_mC18 + 0x30), *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004E51A8;
    goto loc_004E51D6;
loc_004E51A8:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & ((uint32_t)((uint32_t)(0x40000080ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x40000080ULL)))) goto loc_004E6411;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18), (uint32_t)(*(uint32_t *)(arg7)), *(uint16_t *)(arg8));
    if (sign_flag) goto loc_004E6411;
loc_004E51D6:
    goto loc_004E516D;
loc_004E51DB:
    if ((*(uint32_t *)(v_rip + 0x921A6E)) >= = 5) {
        v_stack_mBDC = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mBDC;
        v_stack_m2C8 = result;
        v_stack_m2C0 = 4;
        v_stack_mBD8 = (uint32_t)((uint32_t)(Arg6));
        result = v_stack_mBD8;
        v_stack_m2B8 = result;
        v_stack_m2B0 = 4;
        v_stack_mA30 = 0;
        result = v_stack_mA30;
        v_stack_m2A8 = result;
        v_stack_m2A0 = 8;
        v_stack_mBD4 = (uint32_t)(v_stack_mC40);
        result = v_stack_mBD4;
        v_stack_m298 = result;
        v_stack_m290 = 4;
        result = v_stack_m2E8;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4852388;
        Arg1 = v_rip + 9574833;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)(Arg6))) != ((uint32_t)((uint32_t)(0x40000080ULL)))) goto loc_004E534E;
    result = KeAcquireQueuedSpinLock(7, Arg2, Arg3, Arg4);
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x45) = (uint8_t)(result);
    local_r13 = 0;
    result = KeReleaseQueuedSpinLock(local_r13 + 7, *(uint8_t *)(*(uint64_t *)(arg1) + 0x45), Arg3, Arg4);
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x44)) != 0) goto loc_004E56F5;
    v_stack_mC00 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x18);
    result = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = 0x180001ULL;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) >> (12));
    result = (uint32_t)((result) & (7));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x4) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x8) = 3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC))) | ((uint32_t)(local_r13 + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x38) = local_r13 + 24;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x30) = 0;
    result = IofCompleteRequest(*(uint64_t *)(arg1), (uint8_t)(local_r13 + 1), local_r13 + 24, Arg4);
    *(uint64_t *)(arg1) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (0x507040ULL));
    goto loc_004E57DF;
loc_004E534E:
    if (((uint32_t)((uint32_t)(Arg6))) != 0x2000ULL) goto loc_004E54A5;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & ((uint32_t)((uint32_t)(0x40000080ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x40000080ULL)))) goto loc_004E53DC;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(arg7)), *(uint16_t *)(arg8));
    local_r13 = 0;
    if (sign_flag) goto loc_004E53DF;
loc_004E539A:
loc_004E539F:
loc_004E53A5:
    if (v_stack_mC48 == 0) goto loc_004E6E98;
    if (((1) & ((uint8_t)((uint32_t)(Arg4)))) == 0) goto loc_004E6CB5;
    if (!(condition_is_above_or_equal)) {
        *(uint32_t *)(arg1 + 0x90) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    }
    v_stack_mC34 = 264;
    goto loc_004E6E98;
loc_004E53DC:
    local_r13 = 0;
loc_004E53DF:
    result = KeAcquireQueuedSpinLock(7, *(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(arg7)), *(uint16_t *)(arg8));
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x45) = (uint8_t)(result);
    result = KeReleaseQueuedSpinLock(7, *(uint8_t *)(*(uint64_t *)(arg1) + 0x45), (uint32_t)(*(uint32_t *)(arg7)), *(uint16_t *)(arg8));
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x44)) != 0) goto loc_004E56F5;
    v_stack_mC00 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x18);
    result = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = 0x180001ULL;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) >> (12));
    result = (uint32_t)((result) & (7));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x4) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x8) = 5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC))) | ((uint32_t)(result + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC) = (uint32_t)(result);
    if ((*(uint8_t *)(v_stack_mC18)) == 0) {
        result = (uint32_t)((result) | (2));
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC) = (uint32_t)(result);
        result = *(uint64_t *)(v_stack_mC18 + 0x8);
        Arg1 = *(uint64_t *)(result + 0x8);
        result = *(uint32_t *)(arg1 + 0x14);
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x10) = (uint32_t)(result);
        result = *(uint16_t *)(v_stack_mC18 + 0x1A);
        *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x14) = (uint16_t)(result);
    }
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x38) = result + 24;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x30) = 0;
    result = IofCompleteRequest(*(uint64_t *)(arg1), (uint8_t)(result + 1), result + 24, v_stack_mC18);
    *(uint64_t *)(arg1) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (0x307040ULL));
    goto loc_004E57DF;
loc_004E54A5:
    local_rsi = (uint32_t)((v_stack_mC40) & ((uint32_t)(Arg8)));
    if (((uint32_t)(local_rsi)) != ((uint32_t)(Arg8))) goto loc_004E61FA;
    result = KeAcquireQueuedSpinLock(7, (uint8_t)(result + 1), result + 24, v_stack_mC18);
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x45) = (uint8_t)(result);
    local_r13 = 0;
    result = KeReleaseQueuedSpinLock(local_r13 + 7, *(uint8_t *)(*(uint64_t *)(arg1) + 0x45), result + 24, v_stack_mC18);
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x44)) != 0) goto loc_004E56F5;
    v_stack_mC00 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x18);
    result = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = 0x180001ULL;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) >> (12));
    result = (uint32_t)((result) & (7));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x4) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC))) | ((uint32_t)(local_r13 + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x38) = local_r13 + 24;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x30) = 0;
    result = IofCompleteRequest(*(uint64_t *)(arg1), (uint8_t)(local_r13 + 1), local_r13 + 24, v_stack_mC18);
    *(uint64_t *)(arg1) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (0x807040ULL));
    goto loc_004E57DF;
loc_004E554B:
    if ((*(uint32_t *)(v_rip + 0x9216FE)) >= = 5) {
        v_stack_mBD0 = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mBD0;
        v_stack_m448 = result;
        v_stack_m440 = 4;
        v_stack_mBCC = (uint32_t)(local_rsi);
        result = v_stack_mBCC;
        v_stack_m438 = result;
        v_stack_m430 = 4;
        v_stack_mAA0 = Arg1;
        result = v_stack_mAA0;
        v_stack_m428 = result;
        v_stack_m420 = 8;
        v_stack_mBC8 = (uint32_t)(*(uint64_t *)(arg1));
        result = v_stack_mBC8;
        v_stack_m418 = result;
        v_stack_m410 = 4;
        result = v_stack_m468;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4853162;
        Arg1 = v_rip + 9573953;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & ((uint32_t)(Arg8)));
    if (((uint32_t)(result)) != ((uint32_t)(Arg8))) goto loc_004E56BC;
    result = KeAcquireQueuedSpinLock(7, Arg2, Arg3, Arg4);
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x45) = (uint8_t)(result);
    local_r13 = 0;
    result = KeReleaseQueuedSpinLock(local_r13 + 7, *(uint8_t *)(*(uint64_t *)(arg1) + 0x45), Arg3, Arg4);
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x44)) != 0) goto loc_004E56F5;
    v_stack_mC00 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x18);
    result = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = 0x180001ULL;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) >> (12));
    result = (uint32_t)((result) & (7));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x4) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC))) | ((uint32_t)(local_r13 + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x38) = local_r13 + 24;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x30) = 0;
    result = IofCompleteRequest(*(uint64_t *)(arg1), (uint8_t)(local_r13 + 1), local_r13 + 24, Arg4);
    *(uint64_t *)(arg1) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (0x805040ULL));
    goto loc_004E57DF;
loc_004E56BC:
    if ((((uint32_t)(local_r13 + 1)) & ((uint32_t)(local_rsi))) == 0) goto loc_004E61FA;
    result = KeAcquireQueuedSpinLock(7, (uint8_t)(local_r13 + 1), local_r13 + 24, Arg4);
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x45) = (uint8_t)(result);
    local_r13 = 0;
    result = KeReleaseQueuedSpinLock(local_r13 + 7, *(uint8_t *)(*(uint64_t *)(arg1) + 0x45), local_r13 + 24, Arg4);
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x44)) == 0) goto loc_004E5776;
loc_004E56F5:
    Arg3 = 0;
    Arg2 = 0;
    result = FsRtlpModifyThreadPriorities(Arg1, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = FsRtlpClearOwner(Arg1, Arg2, Arg3, Arg4);
    *(uint8_t *)(arg1 + 0x20) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x38)) == Arg1) {
        *(uint64_t *)(*(uint64_t *)(arg1) + 0x38) = 0;
    }
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x30) = 0xC0000120ULL;
    result = IofCompleteRequest(*(uint64_t *)(arg1), 1, Arg3, Arg4);
    *(uint64_t *)(arg1) = 0;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x8), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    *(uint64_t *)(arg1 + 0x8) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(arg1 + 0x90) = (uint32_t)(result);
loc_004E575F:
    if ((*(uint64_t *)(arg1 + 0x58)) == (Arg1 + 88)) goto loc_004E61E8;
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(uint64_t *)(arg1 + 0x58), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    goto loc_004E575F;
loc_004E5776:
    v_stack_mC00 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x18);
    result = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = 0x180001ULL;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) >> (12));
    result = (uint32_t)((result) & (7));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x4) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x8) = (uint32_t)(result + 1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC))) | ((uint32_t)(result + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0xC) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x38) = result + 24;
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x30) = 0;
    result = IofCompleteRequest(*(uint64_t *)(arg1), (uint8_t)(result + 1), result + 24, Arg4);
    *(uint64_t *)(arg1) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (0x105040ULL));
loc_004E57DF:
    *(uint32_t *)(arg1 + 0x90) = (uint32_t)(result);
loc_004E57E5:
    v_stack_mC48 = (uint8_t)(result + 1);
    goto loc_004E61E8;
loc_004E57EF:
    if ((*(uint32_t *)(v_rip + 0x92145A)) >= = 5) {
        v_stack_mBC4 = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mBC4;
        v_stack_m3E8 = result;
        v_stack_m3E0 = 4;
        v_stack_mBC0 = (uint32_t)(local_rsi);
        result = v_stack_mBC0;
        v_stack_m3D8 = result;
        v_stack_m3D0 = 4;
        v_stack_mA98 = Arg1;
        result = v_stack_mA98;
        v_stack_m3C8 = result;
        v_stack_m3C0 = 8;
        v_stack_mBBC = (uint32_t)(*(uint64_t *)(arg1));
        result = v_stack_mBBC;
        v_stack_m3B8 = result;
        v_stack_m3B0 = 4;
        result = v_stack_m408;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4852762;
        Arg1 = v_rip + 9573277;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    if (((0) & ((uint32_t)(local_rsi))) == 0) goto loc_004E5A21;
loc_004E58C5:
    v_stack_mC28 = *(uint64_t *)(arg1 + 0x28);
    if ((*(uint64_t *)(arg1 + 0x28)) == (Arg1 + 40)) goto loc_004E5A21;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10) + 0x18)) != 0x90240ULL) goto loc_004E5A19;
    local_r13 = 0;
    if (v_stack_mC30 != 0) goto loc_004E5916;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_mC18 + 0x30), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10) + 0x30), (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_004E5916;
loc_004E5911:
    goto loc_004E5A19;
loc_004E5916:
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x10010000ULL)) != 0) goto loc_004E593D;
    v_stack_mC28 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8);
    Arg3 = 0;
    Arg2 = 0;
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)), Arg2, Arg3, Arg1);
    goto loc_004E5911;
loc_004E593D:
    if ((*(uint32_t *)(v_rip + 0x92130C)) <= 3) goto loc_004E4E85;
    v_stack_mBB8 = 0xC0000909ULL;
    v_stack_m888 = v_stack_mBB8;
    v_stack_m880 = 4;
    v_stack_mBB4 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m878 = v_stack_mBB4;
    v_stack_m870 = 4;
    v_stack_mBB0 = (uint32_t)(local_rsi);
    v_stack_m868 = v_stack_mBB0;
    v_stack_m860 = 4;
    v_stack_mA90 = Arg1;
    v_stack_m858 = v_stack_mA90;
    v_stack_m850 = 8;
    v_stack_mBAC = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_m848 = v_stack_mBAC;
    v_stack_m840 = 4;
    goto loc_004E4E66;
loc_004E5A19:
    goto loc_004E58C5;
loc_004E5A21:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90))))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) != 0xB000ULL) goto loc_004E61F2;
loc_004E5A39:
    if ((*(uint32_t *)(v_rip + 0x921210)) <= 5) goto loc_004E5B07;
    v_stack_mBA8 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m388 = v_stack_mBA8;
    v_stack_m380 = 4;
    local_r13 = 0;
    v_stack_mBA4 = (uint32_t)(local_rsi);
    v_stack_m378 = v_stack_mBA4;
    v_stack_m370 = 4;
    v_stack_mAC8 = Arg1;
    v_stack_m368 = v_stack_mAC8;
    v_stack_m360 = 8;
    v_stack_mBA0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_m358 = v_stack_mBA0;
    v_stack_m350 = 4;
    v_stack_mC80 = v_stack_m3A8;
    v_stack_mC88 = 6;
    Arg4 = 0;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9572688, v_rip - 4853140, Arg3, Arg4);
    goto loc_004E5B0A;
loc_004E5B07:
    local_r13 = 0;
loc_004E5B0A:
    if (((uint32_t)(local_rsi)) != 0x2000ULL) goto loc_004E5E3C;
loc_004E5B20:
    v_stack_mC28 = *(uint64_t *)(arg1 + 0x38);
    if ((*(uint64_t *)(arg1 + 0x38)) == (Arg1 + 56)) goto loc_004E616C;
    v_stack_mAC8 = *(uint64_t *)(arg1 + 0x38);
    result = 0;
    if (v_stack_mC30 != 0) goto loc_004E5B6A;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_mC18 + 0x30), *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x18), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004E5B6A;
    local_r13 = 0;
    goto loc_004E5D57;
loc_004E5B6A:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & ((uint32_t)((uint32_t)(0x40000080ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x40000080ULL)))) goto loc_004E5BA7;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x18), (uint32_t)(*(uint32_t *)(arg7)), *(uint16_t *)(arg8));
    local_r13 = 0;
    if (sign_flag) goto loc_004E5BAA;
loc_004E5BA2:
    goto loc_004E5D57;
loc_004E5BA7:
    local_r13 = 0;
loc_004E5BAA:
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x10010000ULL)) != 0) goto loc_004E5D60;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x38)) == 0) goto loc_004E5CAE;
    if ((*(uint32_t *)(v_rip + 0x921087)) >= = 5) {
        v_stack_mB9C = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mB9C;
        v_stack_m328 = result;
        v_stack_m320 = 4;
        v_stack_mB98 = (uint32_t)(local_rsi);
        result = v_stack_mB98;
        v_stack_m318 = result;
        v_stack_m310 = 4;
        v_stack_mA80 = Arg1;
        result = v_stack_mA80;
        v_stack_m308 = result;
        v_stack_m300 = 8;
        result = *(uint32_t *)(arg1 + 0x90);
        v_stack_mB94 = (uint32_t)(result);
        result = v_stack_mB94;
        v_stack_m2F8 = result;
        v_stack_m2F0 = 4;
        result = v_stack_m348;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4852447;
        Arg1 = v_rip + 9572292;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mC48 = 1;
    result = FsRtlpOplockTryStartBreakAckTimeout(*(uint64_t *)(arg1 + 0x38) + 72, *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x58), Arg3, Arg4);
    goto loc_004E5BA2;
loc_004E5CAE:
    v_stack_mC28 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x8);
    v_stack_mB90 = 1;
    result = 0;
    if ((*(uint8_t *)(v_stack_mC18)) == 0) {
        Arg2 = 3;
        v_stack_mB90 = (uint32_t)(Arg2);
        result = *(uint64_t *)(v_stack_mC18 + 0x8);
        Arg1 = *(uint64_t *)(result + 0x8);
        result = *(uint32_t *)(arg1 + 0x14);
        Arg1 = *(uint16_t *)(v_stack_mC18 + 0x1A);
    }
    v_stack_mC70 = 0;
    v_stack_mC78 = (uint16_t)(Arg1);
    v_stack_mC80 = (uint32_t)(result);
    v_stack_mC88 = (uint32_t)(Arg2);
    Arg3 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x8)), Arg1, Arg3, (uint32_t)(0x1000ULL));
    if ((uint8_t)(result) == 0) goto loc_004E5D53;
    v_stack_mC37 = 0;
    v_stack_mC48 = 1;
    result = FsRtlpOplockTryStartBreakAckTimeout(v_stack_mAC8 + 72, *(uint64_t *)(v_stack_mAC8 + 0x58), Arg3, (uint32_t)(0x1000ULL));
    goto loc_004E5D57;
loc_004E5D53:
    v_stack_mC38 = (uint8_t)(result);
loc_004E5D57:
    goto loc_004E5B20;
loc_004E5D60:
    if ((*(uint32_t *)(v_rip + 0x920EE9)) <= 3) goto loc_004E4E85;
    v_stack_mB8C = 0xC0000909ULL;
    v_stack_m6C8 = v_stack_mB8C;
    v_stack_m6C0 = 4;
    v_stack_mB88 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m6B8 = v_stack_mB88;
    v_stack_m6B0 = 4;
    v_stack_mB84 = (uint32_t)(local_rsi);
    v_stack_m6A8 = v_stack_mB84;
    v_stack_m6A0 = 4;
    v_stack_mAC0 = Arg1;
    v_stack_m698 = v_stack_mAC0;
    v_stack_m690 = 8;
    v_stack_mB80 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_m688 = v_stack_mB80;
    v_stack_m680 = 4;
    goto loc_004E4E66;
loc_004E5E3C:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x8)))));
    if (((uint32_t)(result)) != ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x8))))) goto loc_004E616C;
    v_stack_mC28 = *(uint64_t *)(arg1 + 0x48);
loc_004E5E5B:
    if ((*(uint64_t *)(arg1 + 0x48)) == (Arg1 + 72)) goto loc_004E5FA5;
    if ((uint32_t)((uint32_t)(v_stack_mC30)) != 0) goto loc_004E5E89;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_mC18 + 0x30), *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18), (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(0x1000ULL));
    if ((uint8_t)(result) != 0) goto loc_004E5EBC;
loc_004E5E89:
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x10010000ULL)) != 0) goto loc_004E5EC9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30))) & (0xFF0FFFFFULL));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30) = (uint32_t)(result);
    result = v_stack_mC48;
    if (condition_is_below) { result = 1; }
    v_stack_mC48 = (uint8_t)(result);
loc_004E5EBC:
    v_stack_mC28 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x48));
    goto loc_004E5E5B;
loc_004E5EC9:
    if ((*(uint32_t *)(v_rip + 0x920D80)) <= 3) goto loc_004E4E85;
    v_stack_mB7C = 0xC0000909ULL;
    v_stack_m658 = v_stack_mB7C;
    v_stack_m650 = 4;
    v_stack_mB78 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m648 = v_stack_mB78;
    v_stack_m640 = 4;
    v_stack_mB74 = (uint32_t)(local_rsi);
    v_stack_m638 = v_stack_mB74;
    v_stack_m630 = 4;
    v_stack_mAB8 = Arg1;
    v_stack_m628 = v_stack_mAB8;
    v_stack_m620 = 8;
    v_stack_mB70 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_m618 = v_stack_mB70;
    v_stack_m610 = 4;
    goto loc_004E4E66;
loc_004E5FA5:
    Arg1 = 0;
loc_004E5FAB:
    v_stack_mC28 = *(uint64_t *)(arg1 + 0x38);
    if ((*(uint64_t *)(arg1 + 0x38)) == (Arg1 + 56)) goto loc_004E6169;
    if ((uint32_t)((uint32_t)(v_stack_mC30)) != 0) goto loc_004E5FE6;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_mC18 + 0x30), *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x18), (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(0x1000ULL));
    Arg1 = 0;
    if ((uint8_t)(result) != 0) goto loc_004E6017;
loc_004E5FE6:
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x10010000ULL)) != 0) goto loc_004E608D;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x38)) == 0) goto loc_004E6019;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x38)) < 0) {
        result = 1;
        v_stack_mC48 = (uint8_t)(result);
        Arg1 = *(uint64_t *)(arg1 + 0x38) + 72;
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x58);
        result = FsRtlpOplockTryStartBreakAckTimeout(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(0x1000ULL));
        Arg1 = 0;
    }
    goto loc_004E6085;
loc_004E6019:
    v_stack_mC28 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x8);
    v_stack_mC70 = 0;
    v_stack_mC78 = 0;
    v_stack_mC80 = 0;
    v_stack_mC88 = 1;
    Arg4 = 0;
    Arg3 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x8)), 0, Arg3, Arg4);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_004E607C;
    v_stack_mC37 = 0;
    if (!(condition_is_above_or_equal)) {
        result = Arg1 + 1;
        v_stack_mC48 = (uint8_t)(result);
        Arg1 = *(uint64_t *)(arg1 + 0x38) + 72;
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x58);
        result = FsRtlpOplockTryStartBreakAckTimeout(Arg1, Arg2, Arg3, Arg4);
        Arg1 = 0;
    }
    goto loc_004E6085;
loc_004E607C:
    v_stack_mC38 = 1;
loc_004E6085:
    goto loc_004E5FAB;
loc_004E608D:
    if ((*(uint32_t *)(v_rip + 0x920BBC)) <= 3) goto loc_004E4E85;
    v_stack_mB6C = 0xC0000909ULL;
    v_stack_m5E8 = v_stack_mB6C;
    v_stack_m5E0 = 4;
    v_stack_mB68 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m5D8 = v_stack_mB68;
    v_stack_m5D0 = 4;
    v_stack_mB64 = (uint32_t)(local_rsi);
    v_stack_m5C8 = v_stack_mB64;
    v_stack_m5C0 = 4;
    v_stack_mAB0 = 0;
    v_stack_m5B8 = v_stack_mAB0;
    v_stack_m5B0 = 8;
    v_stack_mB60 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_m5A8 = v_stack_mB60;
    v_stack_m5A0 = 4;
    goto loc_004E4E66;
loc_004E6169:
    local_r13 = 0;
loc_004E616C:
    result = v_stack_m608;
    if (v_stack_mC38 != 0) {
        Arg1 = 0;
        result = FsRtlpReleaseIrpsWaitingForRH(Arg1, v_rip - 4853474, Arg3, Arg4);
    }
    if (v_stack_mC48 != 0) goto loc_004E61DA;
    if ((*(uint64_t *)(arg1 + 0x48)) == (Arg1 + 72)) goto loc_004E61DA;
    if ((*(uint64_t *)(arg1 + 0x48)) >= (Arg1 + 72)) goto loc_004E61DA;
    if (v_stack_mC30 != 0) goto loc_004E61C8;
loc_004E619B:
    v_stack_mC28 = *(uint64_t *)(arg1 + 0x48);
    if ((*(uint64_t *)(arg1 + 0x48)) == (Arg1 + 72)) goto loc_004E61DA;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18), *(uint64_t *)(v_stack_mC18 + 0x30), Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_004E61D5;
loc_004E61C8:
    v_stack_mC48 = 1;
    goto loc_004E61E0;
loc_004E61D5:
    goto loc_004E619B;
loc_004E61DA:
loc_004E61E0:
    result = FsRtlpComputeShareableOplockState(Arg1, *(uint64_t *)(v_stack_mC18 + 0x30), Arg3, Arg4);
loc_004E61E8:
    goto loc_004E53A5;
loc_004E61F2:
    result = FsRtlpComputeShareableOplockState(Arg1, *(uint64_t *)(v_stack_mC18 + 0x30), Arg3, Arg4);
loc_004E61FA:
    local_r13 = 0;
    goto loc_004E539A;
loc_004E6202:
    if ((*(uint32_t *)(v_rip + 0x920A47)) >= = 5) {
        v_stack_mB1C = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mB1C;
        v_stack_m88 = result;
        v_stack_m80 = 4;
        v_stack_mB5C = (uint32_t)(v_stack_mC40);
        result = v_stack_mB5C;
        v_stack_m78 = result;
        v_stack_m70 = 4;
        v_stack_mA60 = Arg1;
        result = v_stack_mA60;
        v_stack_m68 = result;
        v_stack_m60 = 8;
        v_stack_mB58 = (uint32_t)(Arg1);
        result = v_stack_mB58;
        v_stack_m58 = result;
        v_stack_m50 = 4;
        result = v_stack_mA8;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4856201;
        Arg1 = v_rip + 9570698;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    if (!(condition_is_above_or_equal)) {
        result = *(uint32_t *)(arg1 + 0x90);
        result = (uint32_t)((result) & (32));
        result = (uint32_t)((result) | (0x805040ULL));
        *(uint32_t *)(arg1 + 0x90) = (uint32_t)(result);
    }
    local_r13 = 0;
    if ((((uint32_t)((uint32_t)(v_stack_mC30))) & ((uint32_t)(v_stack_mC40))) == 0) goto loc_004E61E8;
    goto loc_004E57E5;
loc_004E62FC:
    if (((uint32_t)(result)) == 0x107040ULL) goto loc_004E6BDD;
    if (((uint32_t)(result)) == 0x307040ULL) goto loc_004E6A8A;
    if (((uint32_t)(result)) == 0x507040ULL) goto loc_004E6942;
    if (((uint32_t)(result)) == 0x803000ULL) goto loc_004E66DF;
    if (((uint32_t)(result)) == 0x805040ULL) goto loc_004E6611;
    if (((uint32_t)(result)) == 0x807040ULL) goto loc_004E64F7;
loc_004E633E:
    if (((uint32_t)(result)) >= 0x807040ULL) goto loc_004E6429;
    if ((*(uint32_t *)(v_rip + 0x920901)) >= = 5) {
        v_stack_mB54 = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mB54;
        v_stack_m208 = result;
        v_stack_m200 = 4;
        v_stack_mB50 = (uint32_t)(v_stack_mC40);
        result = v_stack_mB50;
        v_stack_m1F8 = result;
        v_stack_m1F0 = 4;
        v_stack_mA58 = Arg1;
        result = v_stack_mA58;
        v_stack_m1E8 = result;
        v_stack_m1E0 = 8;
        v_stack_mB4C = (uint32_t)(Arg1);
        result = v_stack_mB4C;
        v_stack_m1D8 = result;
        v_stack_m1D0 = 4;
        result = v_stack_m228;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4855999;
        Arg1 = v_rip + 9570372;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mC48 = 1;
    local_r13 = 0;
    goto loc_004E53A5;
loc_004E6429:
    if ((*(uint32_t *)(v_rip + 0x920820)) <= 2) goto loc_004E61FA;
    v_stack_mB48 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m1A8 = v_stack_mB48;
    v_stack_m1A0 = 4;
    v_stack_mB44 = (uint32_t)(v_stack_mC40);
    v_stack_m198 = v_stack_mB44;
    v_stack_m190 = 4;
    v_stack_mA50 = Arg1;
    v_stack_m188 = v_stack_mA50;
    v_stack_m180 = 8;
    v_stack_mB40 = (uint32_t)(Arg1);
    v_stack_m178 = v_stack_mB40;
    v_stack_m170 = 4;
    v_stack_mC80 = v_stack_m1C8;
    v_stack_mC88 = 6;
    Arg4 = 0;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9570147, v_rip - 4856333, Arg3, Arg4);
    goto loc_004E61FA;
loc_004E64F7:
    if ((*(uint32_t *)(v_rip + 0x920752)) >= = 5) {
        v_stack_mB3C = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mB3C;
        v_stack_m148 = result;
        v_stack_m140 = 4;
        v_stack_mB38 = (uint32_t)(v_stack_mC40);
        result = v_stack_mB38;
        v_stack_m138 = result;
        v_stack_m130 = 4;
        v_stack_mA48 = Arg1;
        result = v_stack_mA48;
        v_stack_m128 = result;
        v_stack_m120 = 8;
        v_stack_mB34 = (uint32_t)(v_rip + 9570147);
        result = v_stack_mB34;
        v_stack_m118 = result;
        v_stack_m110 = 4;
        result = v_stack_m168;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4857501;
        Arg1 = v_rip + 9569941;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & ((uint32_t)((uint32_t)(0x40000080ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x40000080ULL)))) goto loc_004E6603;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(arg7)), *(uint16_t *)(arg8));
    local_r13 = 0;
    if (!sign_flag) goto loc_004E539A;
    goto loc_004E6606;
loc_004E6603:
    local_r13 = 0;
loc_004E6606:
    goto loc_004E57E5;
loc_004E6611:
    if ((*(uint32_t *)(v_rip + 0x920638)) <= 5) goto loc_004E62E5;
    v_stack_mB30 = (uint32_t)((uint32_t)(Arg4));
    v_stack_mE8 = v_stack_mB30;
    v_stack_mE0 = 4;
    v_stack_mB2C = (uint32_t)(v_stack_mC40);
    v_stack_mD8 = v_stack_mB2C;
    v_stack_mD0 = 4;
    v_stack_mA40 = Arg1;
    v_stack_mC8 = v_stack_mA40;
    v_stack_mC0 = 8;
    v_stack_mB28 = (uint32_t)(v_stack_mC40);
    v_stack_mB8 = v_stack_mB28;
    v_stack_mB0 = 4;
    v_stack_mC80 = v_stack_m108;
    v_stack_mC88 = 6;
    Arg4 = 0;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9569659, v_rip - 4857351, Arg3, Arg4);
    goto loc_004E62E5;
loc_004E66DF:
    if ((*(uint32_t *)(v_rip + 0x92056A)) >= = 5) {
        v_stack_mB24 = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mB24;
        v_stack_m508 = result;
        v_stack_m500 = 4;
        v_stack_mB20 = (uint32_t)(v_stack_mC40);
        result = v_stack_mB20;
        v_stack_m4F8 = result;
        v_stack_m4F0 = 4;
        v_stack_mA38 = Arg1;
        result = v_stack_mA38;
        v_stack_m4E8 = result;
        v_stack_m4E0 = 8;
        v_stack_mAD4 = (uint32_t)(v_rip + 9569659);
        result = v_stack_mAD4;
        v_stack_m4D8 = result;
        v_stack_m4D0 = 4;
        result = v_stack_m528;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4855397;
        Arg1 = v_rip + 9569453;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint32_t)(v_stack_mC40)) & (0x3000ULL)) == 0) goto loc_004E61FA;
    if (sign_flag) goto loc_004E68A6;
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x10010000ULL)) == 0) goto loc_004E68A6;
    if ((*(uint32_t *)(v_rip + 0x92047F)) <= 3) goto loc_004E4E85;
    v_stack_mB18 = 0xC0000909ULL;
    v_stack_m578 = v_stack_mB18;
    v_stack_m570 = 4;
    v_stack_mB14 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m568 = v_stack_mB14;
    v_stack_m560 = 4;
    v_stack_mB10 = (uint32_t)(v_stack_mC40);
    v_stack_m558 = v_stack_mB10;
    v_stack_m550 = 4;
    v_stack_mAA8 = Arg1;
    v_stack_m548 = v_stack_mAA8;
    v_stack_m540 = 8;
    v_stack_mB0C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_m538 = v_stack_mB0C;
    v_stack_m530 = 4;
    goto loc_004E4E66;
loc_004E68A6:
    if ((*(uint32_t *)(v_rip + 0x92047F)) >= 3) goto loc_004E61FA;
loc_004E68CA:
    v_stack_mC28 = *(uint64_t *)(arg1 + 0x48);
    if ((*(uint64_t *)(arg1 + 0x48)) == (Arg1 + 72)) goto loc_004E61FA;
    result = 0;
    if (v_stack_mC30 != 0) goto loc_004E6905;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_mC18 + 0x30), *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004E6905;
    goto loc_004E692B;
loc_004E6905:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & ((uint32_t)((uint32_t)(0x40000080ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x40000080ULL)))) goto loc_004E6930;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18), (uint32_t)(*(uint32_t *)(arg7)), *(uint16_t *)(arg8));
    if (sign_flag) goto loc_004E6930;
loc_004E692B:
    goto loc_004E68CA;
loc_004E6930:
    if ((((uint32_t)((uint32_t)(Arg4))) & (0x10010000ULL)) != 0) goto loc_004E4E85;
    goto loc_004E6411;
loc_004E6942:
    if ((*(uint32_t *)(v_rip + 0x920307)) >= = 5) {
        v_stack_mB08 = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mB08;
        v_stack_m4A8 = result;
        v_stack_m4A0 = 4;
        v_stack_mB04 = (uint32_t)(v_stack_mC40);
        result = v_stack_mB04;
        v_stack_m498 = result;
        v_stack_m490 = 4;
        v_stack_mA28 = Arg1;
        result = v_stack_mA28;
        v_stack_m488 = result;
        v_stack_m480 = 8;
        v_stack_mB00 = (uint32_t)(v_stack_mC40);
        result = v_stack_mB00;
        v_stack_m478 = result;
        v_stack_m470 = 4;
        result = v_stack_m4C8;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4858820;
        Arg1 = v_rip + 9568842;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)(v_stack_mC40)) != 0x2000ULL) goto loc_004E6A67;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & ((uint32_t)((uint32_t)(0x40000080ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x40000080ULL)))) goto loc_004E6A57;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(arg7)), *(uint16_t *)(arg8));
    local_r13 = 0;
    if (!sign_flag) goto loc_004E539F;
loc_004E6A57:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (0x107040ULL));
    goto loc_004E6A7F;
loc_004E6A67:
    if (condition_is_above_or_equal) goto loc_004E6411;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (0x807040ULL));
loc_004E6A7F:
    *(uint32_t *)(arg1 + 0x90) = (uint32_t)(result);
    goto loc_004E6411;
loc_004E6A8A:
    if ((*(uint32_t *)(v_rip + 0x9201BF)) >= = 5) {
        v_stack_mAFC = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mAFC;
        v_stack_m268 = result;
        v_stack_m260 = 4;
        v_stack_mAF8 = (uint32_t)(v_stack_mC40);
        result = v_stack_mAF8;
        v_stack_m258 = result;
        v_stack_m250 = 4;
        v_stack_mA20 = Arg1;
        result = v_stack_mA20;
        v_stack_m248 = result;
        v_stack_m240 = 8;
        v_stack_mAF4 = (uint32_t)(v_stack_mC40);
        result = v_stack_mAF4;
        v_stack_m238 = result;
        v_stack_m230 = 4;
        result = v_stack_m288;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4859038;
        Arg1 = v_rip + 9568514;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)(v_stack_mC40)) != ((uint32_t)((uint32_t)(0x40000080ULL)))) goto loc_004E6B68;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (0x107040ULL));
    goto loc_004E6B7E;
loc_004E6B68:
    local_rsi = (uint32_t)((v_stack_mC40) & ((uint32_t)(Arg8)));
    if (((uint32_t)(local_rsi)) != ((uint32_t)(Arg8))) goto loc_004E6B84;
loc_004E6B70:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (0x807040ULL));
loc_004E6B7E:
    *(uint32_t *)(arg1 + 0x90) = (uint32_t)(result);
loc_004E6B84:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & ((uint32_t)((uint32_t)(0x40000080ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x40000080ULL)))) goto loc_004E6BCA;
    result = FsRtlpCheckSharingAgainstOplockOwner(v_stack_mC40, *(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(arg7)), *(uint16_t *)(arg8));
    local_r13 = 0;
    if (!sign_flag) goto loc_004E539F;
    goto loc_004E6BCD;
loc_004E6BCA:
    local_r13 = 0;
loc_004E6BCD:
    v_stack_mC48 = 1;
    goto loc_004E53A5;
loc_004E6BDD:
    if ((*(uint32_t *)(v_rip + 0x92006C)) >= = 5) {
        v_stack_mAF0 = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_mAF0;
        v_stack_m968 = result;
        v_stack_m960 = 4;
        v_stack_mAEC = (uint32_t)(v_stack_mC40);
        result = v_stack_mAEC;
        v_stack_m958 = result;
        v_stack_m950 = 4;
        v_stack_mA18 = Arg1;
        result = v_stack_mA18;
        v_stack_m948 = result;
        v_stack_m940 = 8;
        v_stack_mAE8 = (uint32_t)(v_stack_mC40);
        result = v_stack_mAE8;
        v_stack_m938 = result;
        v_stack_m930 = 4;
        result = v_stack_m988;
        v_stack_mC80 = result;
        v_stack_mC88 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4859155;
        Arg1 = v_rip + 9568175;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    if (condition_is_above_or_equal) goto loc_004E6B84;
    goto loc_004E6B70;
loc_004E6CB5:
    result = Feature_Servicing_CloseOplockTimeoutGap__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (64));
    if ((uint32_t)(result) == 0) goto loc_004E6CF2;
    if ((uint32_t)(Arg1) != 0) goto loc_004E6CF6;
    if ((*(uint64_t *)(arg1 + 0x48)) == (Arg1 + 72)) goto loc_004E6D09;
loc_004E6CD7:
    if ((*(uint64_t *)(arg1 + 0x48)) == (Arg1 + 72)) goto loc_004E6D09;
    result = FsRtlpOplockTryStartBreakAckTimeout(*(uint64_t *)(arg1 + 0x48) + 72, *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x58), Arg3, Arg4);
    goto loc_004E6CD7;
loc_004E6CF2:
    if ((uint32_t)(*(uint64_t *)(arg1 + 0x48) + 72) != 0) {
        Arg2 = *(uint64_t *)(arg1 + 0xB8);
        Arg1 = Arg1 + 168;
        result = FsRtlpOplockTryStartBreakAckTimeout(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_mC37 != 0) {
        Arg3 = 1;
        Arg2 = 0;
        Arg1 = Arg1;
        result = FsRtlpModifyThreadPriorities(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 0;
        Arg1 = Arg1;
        result = FsRtlpOplockSendModernAppTermination(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(v_stack_mAA8) = 0;
    v_stack_mC58 = v_stack_mAB0;
    v_stack_mC60 = Arg14;
    v_stack_mC68 = v_stack_mAB8;
    v_stack_mC70 = Arg12;
    v_stack_mC78 = (uint8_t)(v_stack_mC36);
    v_stack_mC80 = v_stack_mA08;
    v_stack_mC88 = Arg11;
    result = FsRtlpWaitOnIrp(Arg1, v_stack_mC40, v_stack_mAC0, Arg10);
    v_stack_mC34 = (uint32_t)(result);
    goto loc_004E6E98;
loc_004E6DAC:
    if ((*(uint32_t *)(v_rip + 0x91FE9D)) <= 5) goto loc_004E6E94;
    v_stack_mAE4 = (uint32_t)(v_stack_mC40);
    v_stack_m8F8 = v_stack_mAE4;
    v_stack_m8F0 = 4;
    v_stack_mAE0 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m8E8 = v_stack_mAE0;
    v_stack_m8E0 = 4;
    v_stack_mC18 = (uint32_t)(v_stack_mC40);
    v_stack_m8D8 = v_stack_mC18;
    v_stack_m8D0 = 4;
    v_stack_mA10 = Arg1;
    v_stack_m8C8 = v_stack_mA10;
    v_stack_m8C0 = 8;
    v_stack_mC40 = (uint32_t)(result);
    v_stack_m8B8 = v_stack_mC40;
    v_stack_m8B0 = 4;
loc_004E6E73:
    v_stack_mC80 = v_stack_m918;
    v_stack_mC88 = 7;
    Arg4 = 0;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 9567683, v_rip - 4857592, Arg3, Arg4);
    Arg2 = 0;
loc_004E6E94:
    v_stack_mC34 = 0;
loc_004E6E98:
loc_004E6E9C:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (0xC70ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x90` | `32` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg7` | `+ 0x0` | `32` | `R` |
| `Arg8` | `+ 0x0` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E4990&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
