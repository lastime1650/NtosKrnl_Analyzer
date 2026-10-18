# IopCreateFile

- RVA: `0x008AB298`–`0x008AC02F` (길이 `3,479` bytes)
- VA: `0x00000001408AB298`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007F6A8`
- 디코드: `795`개 명령, `3,479/3,479` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **50**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **16**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008AB32E` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x008AB352` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x008AB378` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008AB412` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x008AB41C` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008AB49C` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008AB5E5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AB603` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008AB615` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008AB708` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (function, `0x004094A0`)
- `0x008AB769` → [ObOpenObjectByNameEx](../89/ObOpenObjectByNameEx_function_0089A8A0.md) (function, `0x0089A8A0`)
- `0x008AB78F` → [IopCleanupExtraCreateParameters](IopCleanupExtraCreateParameters_function_008A11E0.md) (function, `0x008A11E0`)
- `0x008AB819` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AB825` → [FsRtlFreeExtraCreateParameterList](FsRtlFreeExtraCreateParameterList_function_008A1420.md) (function, `0x008A1420`)
- `0x008AB86E` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008AB94B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008AB9AD` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008ABAEF` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008ABAF9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008ABB03` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008ABB22` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008ABB99` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008ABBA3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008ABBAD` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008ABBFB` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008ABC05` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008ABC80` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008ABC8A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008ABC94` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008ABCB6` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008ABD34` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008ABD40` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008ABD4F` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008ABD88` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008ABD9E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008ABDB7` → [IoCheckEaBufferValidity](../A2/IoCheckEaBufferValidity_function_00A2B9F0.md) (function, `0x00A2B9F0`)
- `0x008ABDCF` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x008ABDD4` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008ABE08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ABE5D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008ABE64` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008ABE71` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008ABE8F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ABED0` → [IopCleanupExtraCreateParameters](IopCleanupExtraCreateParameters_function_008A11E0.md) (function, `0x008A11E0`)
- `0x008ABF61` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008ABF6E` → [FsRtlFreeExtraCreateParameter](FsRtlFreeExtraCreateParameter_function_008A1760.md) (function, `0x008A1760`)
- `0x008ABF7A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ABF96` → [FsRtlFreeExtraCreateParameterList](FsRtlFreeExtraCreateParameterList_function_008A1420.md) (function, `0x008A1420`)
- `0x008ABFB8` → [ObCloseHandle](ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x008AC01A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PopCreateHiberFile](../75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D006`
- [PopCreateHiberFile](../75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D232`
- [RtlCreateSystemVolumeInformationFolder](../79/RtlCreateSystemVolumeInformationFolder_function_00791010.md) at `0x007911DC`
- [RtlCreateSystemVolumeInformationFolder](../79/RtlCreateSystemVolumeInformationFolder_function_00791010.md) at `0x00791243`
- [RtlCreateSystemVolumeInformationFolder](../79/RtlCreateSystemVolumeInformationFolder_function_00791010.md) at `0x007912AC`
- [RtlpSysVolTakeOwnership](../79/RtlpSysVolTakeOwnership_function_007917C8.md) at `0x007918EB`
- [SmKmStoreFileCreateForIoType](../7A/SmKmStoreFileCreateForIoType_function_007A93C8.md) at `0x007A950A`
- [MiCreatePagingFile](../7F/MiCreatePagingFile_function_007FEFF4.md) at `0x007FF4FD`
- [MiCreatePagingFile](../7F/MiCreatePagingFile_function_007FEFF4.md) at `0x007FF820`
- [PfSnIsVolumeMounted](PfSnIsVolumeMounted_function_008AAACC.md) at `0x008AAB8D`
- [IopOpenLinkOrRenameTarget](IopOpenLinkOrRenameTarget_function_008AAC04.md) at `0x008AAE0F`
- [IoCreateFile](IoCreateFile_function_008AAF60.md) at `0x008AAFE5`
- [IoCreateFileEx](IoCreateFileEx_function_008AB000.md) at `0x008AB138`
- [NtOpenFile](NtOpenFile_function_008AB1A0.md) at `0x008AB1F3`
- [NtCreateFile](NtCreateFile_function_008AB210.md) at `0x008AB284`
- [PfSnGetPrefetchInstructions](PfSnGetPrefetchInstructions_function_008AEBE4.md) at `0x008AED59`
- [PfpVolumeOpenAndVerify](../93/PfpVolumeOpenAndVerify_function_009381F4.md) at `0x00938305`
- [NtCreateNamedPipeFile](../A3/NtCreateNamedPipeFile_function_00A3AF30.md) at `0x00A3B07C`
- [NtCreateMailslotFile](../A9/NtCreateMailslotFile_function_00A945C0.md) at `0x00A946C2`
- [MiOpenHotPatchFile](../AB/MiOpenHotPatchFile_function_00AB5684.md) at `0x00AB5854`

### Static image references
- `0x008AB487` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x008AB6E1` → RVA `0x00E0A9C8` (`.data`; read)
- `0x008AB75F` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **36**
  - `0x008AB32E` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x008AB352` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x008AB378` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008AB412` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
  - `0x008AB49C` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008AB5E5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AB603` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008AB615` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008AB708` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (`PAGE` → `.text`)
  - `0x008AB819` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AB86E` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008AB94B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008AB9AD` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008ABAEF` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008ABAF9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008ABB03` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008ABB99` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008ABBA3` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008ABBAD` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008ABC80` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008ABC8A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008ABC94` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008ABD34` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008ABD40` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008ABD4F` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008ABD88` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008ABD9E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008ABDCF` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
  - `0x008ABE08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008ABE5D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008ABE64` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008ABE71` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008ABE8F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008ABF61` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008ABF7A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008AC01A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **21**
  - `0x008AB5ED` → [sub_00B19FF6 + 0x258](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB63D` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB64B` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB658` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB679` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB68D` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB6AD` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB6BF` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB6D1` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB6FA` → [sub_00B19FF6 + 0x6B](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB8ED` → [sub_00B19FF6 + 0x16B](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB95C` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB974` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AB9EA` → [sub_00B19FF6](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008ABEDF` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008ABEEE` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008ABF00` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008ABF18` → [sub_00B19FF6 + 0xC1](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AC004` → [sub_00B19FF6 + 0x3CE](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AC00E` → [sub_00B19FF6 + 0x3B7](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)
  - `0x008AC020` → [sub_00B19FF6 + 0x3B7](../B1/Unknown_function_00B19FF6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008AB298  48 8B C4                        mov rax, rsp
008AB29B  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
008AB29F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
008AB2A3  89 50 10                        mov dword ptr [rax + 0x10], edx
008AB2A6  48 89 48 08                     mov qword ptr [rax + 8], rcx
008AB2AA  53                              push rbx
008AB2AB  56                              push rsi
008AB2AC  57                              push rdi
008AB2AD  41 54                           push r12
008AB2AF  41 55                           push r13
008AB2B1  41 56                           push r14
008AB2B3  41 57                           push r15
008AB2B5  48 81 EC 90 00 00 00            sub rsp, 0x90
008AB2BC  8B 8C 24 38 01 00 00            mov ecx, dword ptr [rsp + 0x138]
008AB2C3  89 8C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ecx
008AB2CA  44 8B AC 24 10 01 00 00         mov r13d, dword ptr [rsp + 0x110]
008AB2D2  4C 8B A4 24 F0 00 00 00         mov r12, qword ptr [rsp + 0xf0]
008AB2DA  33 FF                           xor edi, edi
008AB2DC  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
008AB2E0  48 89 78 98                     mov qword ptr [rax - 0x68], rdi
008AB2E4  48 89 78 A8                     mov qword ptr [rax - 0x58], rdi
008AB2E8  48 89 78 A0                     mov qword ptr [rax - 0x60], rdi
008AB2EC  89 78 80                        mov dword ptr [rax - 0x80], edi
008AB2EF  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
008AB2F3  48 89 78 B0                     mov qword ptr [rax - 0x50], rdi
008AB2F7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AB300  0F BA E1 08                     bt ecx, 8
008AB304  8B CF                           mov ecx, edi
008AB306  0F B6 80 32 02 00 00            movzx eax, byte ptr [rax + 0x232]
008AB30D  0F 43 C8                        cmovae ecx, eax
008AB310  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
008AB314  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
008AB31D  4D 8B B7 80 08 00 00            mov r14, qword ptr [r15 + 0x880]
008AB324  8D 77 01                        lea esi, [rdi + 1]
008AB327  41 01 76 14                     add dword ptr [r14 + 0x14], esi
008AB32B  49 8B CE                        mov rcx, r14
008AB32E  E8 3D F2 E0 FF                  call 0x1406ba570
008AB333  48 8B D8                        mov rbx, rax
008AB336  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008AB33B  48 85 C0                        test rax, rax
008AB33E  75 45                           jne 0x1408ab385
008AB340  41 01 76 18                     add dword ptr [r14 + 0x18], esi
008AB344  4D 8B B7 88 08 00 00            mov r14, qword ptr [r15 + 0x888]
008AB34B  41 01 76 14                     add dword ptr [r14 + 0x14], esi
008AB34F  49 8B CE                        mov rcx, r14
008AB352  E8 19 F2 E0 FF                  call 0x1406ba570
008AB357  48 8B D8                        mov rbx, rax
008AB35A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008AB35F  48 85 C0                        test rax, rax
008AB362  75 21                           jne 0x1408ab385
008AB364  41 01 76 18                     add dword ptr [r14 + 0x18], esi
008AB368  41 8B 56 2C                     mov edx, dword ptr [r14 + 0x2c]
008AB36C  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
008AB370  45 8B 46 28                     mov r8d, dword ptr [r14 + 0x28]
008AB374  41 8B 4E 24                     mov ecx, dword ptr [r14 + 0x24]
008AB378  E8 53 F7 E0 FF                  call 0x1406baad0
008AB37D  48 8B D8                        mov rbx, rax
008AB380  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008AB385  48 85 DB                        test rbx, rbx
008AB388  0F 84 97 0C 00 00               je 0x1408ac025
008AB38E  41 8B 47 24                     mov eax, dword ptr [r15 + 0x24]
008AB392  89 03                           mov dword ptr [rbx], eax
008AB394  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
008AB399  45 84 C0                        test r8b, r8b
008AB39C  0F 85 7D 02 00 00               jne 0x1408ab61f
008AB3A2  F7 84 24 38 01 00 00 00 02 00 00  test dword ptr [rsp + 0x138], 0x200
008AB3AD  0F 85 6C 02 00 00               jne 0x1408ab61f
008AB3B3  45 84 C0                        test r8b, r8b
008AB3B6  0F 84 CF 04 00 00               je 0x1408ab88b
008AB3BC  49 BA 00 00 FF FF FF 7F 00 00   movabs r10, 0x7fffffff0000
008AB3C6  49 8B CA                        mov rcx, r10
008AB3C9  4C 39 94 24 D0 00 00 00         cmp qword ptr [rsp + 0xd0], r10
008AB3D1  48 0F 42 8C 24 D0 00 00 00      cmovb rcx, qword ptr [rsp + 0xd0]
008AB3DA  48 8B 01                        mov rax, qword ptr [rcx]
008AB3DD  48 89 01                        mov qword ptr [rcx], rax
008AB3E0  49 8B CA                        mov rcx, r10
008AB3E3  4C 39 94 24 E8 00 00 00         cmp qword ptr [rsp + 0xe8], r10
008AB3EB  48 0F 42 8C 24 E8 00 00 00      cmovb rcx, qword ptr [rsp + 0xe8]
008AB3F4  8B 01                           mov eax, dword ptr [rcx]
008AB3F6  89 01                           mov dword ptr [rcx], eax
008AB3F8  41 B1 03                        mov r9b, 3
008AB3FB  4D 85 E4                        test r12, r12
008AB3FE  75 17                           jne 0x1408ab417
008AB400  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
008AB405  48 8B C7                        mov rax, rdi
008AB408  48 85 C0                        test rax, rax
008AB40B  79 2D                           jns 0x1408ab43a
008AB40D  B9 0D 00 00 C0                  mov ecx, 0xc000000d
008AB412  E8 39 B6 A4 FF                  call 0x1402f6a50
008AB417  45 84 E1                        test r9b, r12b
008AB41A  74 06                           je 0x1408ab422
008AB41C  E8 AF EB FE FF                  call 0x140899fd0
008AB421  CC                              int3
008AB422  49 8B C2                        mov rax, r10
008AB425  4D 3B E2                        cmp r12, r10
008AB428  49 0F 42 C4                     cmovb rax, r12
008AB42C  90                              nop
008AB42D  8A 00                           mov al, byte ptr [rax]
008AB42F  49 8B 04 24                     mov rax, qword ptr [r12]
008AB433  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008AB438  EB CE                           jmp 0x1408ab408
008AB43A  EB 6C                           jmp 0x1408ab4a8
008AB43C  8B D8                           mov ebx, eax
008AB43E  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008AB447  4C 8B 82 80 08 00 00            mov r8, qword ptr [rdx + 0x880]
008AB44E  41 FF 40 1C                     inc dword ptr [r8 + 0x1c]
008AB452  41 0F B7 48 10                  movzx ecx, word ptr [r8 + 0x10]
008AB457  66 41 39 08                     cmp word ptr [r8], cx
008AB45B  0F 82 AC 01 00 00               jb 0x1408ab60d
008AB461  41 FF 40 20                     inc dword ptr [r8 + 0x20]
008AB465  4C 8B 82 88 08 00 00            mov r8, qword ptr [rdx + 0x888]
008AB46C  41 FF 40 1C                     inc dword ptr [r8 + 0x1c]
008AB470  41 0F B7 40 10                  movzx eax, word ptr [r8 + 0x10]
008AB475  66 41 39 00                     cmp word ptr [r8], ax
008AB479  0F 82 8E 01 00 00               jb 0x1408ab60d
008AB47F  41 FF 40 20                     inc dword ptr [r8 + 0x20]
008AB483  49 8B 40 38                     mov rax, qword ptr [r8 + 0x38]
008AB487  48 8D 0D C2 73 2D 00            lea rcx, [rip + 0x2d73c2]
008AB48E  48 3B C1                        cmp rax, rcx
008AB491  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008AB496  0F 85 67 01 00 00               jne 0x1408ab603
008AB49C  E8 AF 73 2D 00                  call 0x140b82850
008AB4A1  8B C3                           mov eax, ebx
008AB4A3  E9 CF 03 00 00                  jmp 0x1408ab877
008AB4A8  41 0F BA E5 1C                  bt r13d, 0x1c
008AB4AD  0F 82 3C 05 00 00               jb 0x1408ab9ef
008AB4B3  48 89 BB D8 00 00 00            mov qword ptr [rbx + 0xd8], rdi
008AB4BA  4C 8B B4 24 18 01 00 00         mov r14, qword ptr [rsp + 0x118]
008AB4C2  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
008AB4C7  44 8B BC 24 20 01 00 00         mov r15d, dword ptr [rsp + 0x120]
008AB4CF  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
008AB4D4  48 89 7B 48                     mov qword ptr [rbx + 0x48], rdi
008AB4D8  4D 85 F6                        test r14, r14
008AB4DB  0F 85 75 08 00 00               jne 0x1408abd56
008AB4E1  8B 94 24 38 01 00 00            mov edx, dword ptr [rsp + 0x138]
008AB4E8  4C 8B A4 24 E8 00 00 00         mov r12, qword ptr [rsp + 0xe8]
008AB4F0  89 7B 50                        mov dword ptr [rbx + 0x50], edi
008AB4F3  C7 03 08 00 E0 00               mov dword ptr [rbx], 0xe00008
008AB4F9  89 7B 20                        mov dword ptr [rbx + 0x20], edi
008AB4FC  48 89 7B 18                     mov qword ptr [rbx + 0x18], rdi
008AB500  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008AB505  48 89 43 38                     mov qword ptr [rbx + 0x38], rax
008AB509  41 81 E5 FF FF FF 00            and r13d, 0xffffff
008AB510  44 89 6B 40                     mov dword ptr [rbx + 0x40], r13d
008AB514  0F B7 84 24 F8 00 00 00         movzx eax, word ptr [rsp + 0xf8]
008AB51C  66 89 43 44                     mov word ptr [rbx + 0x44], ax
008AB520  0F B7 84 24 00 01 00 00         movzx eax, word ptr [rsp + 0x100]
008AB528  66 89 43 46                     mov word ptr [rbx + 0x46], ax
008AB52C  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
008AB533  89 43 58                        mov dword ptr [rbx + 0x58], eax
008AB536  66 89 BB 88 00 00 00            mov word ptr [rbx + 0x88], di
008AB53D  40 88 BB 8A 00 00 00            mov byte ptr [rbx + 0x8a], dil
008AB544  89 53 54                        mov dword ptr [rbx + 0x54], edx
008AB547  48 89 7B 28                     mov qword ptr [rbx + 0x28], rdi
008AB54B  4C 8B B4 24 E0 00 00 00         mov r14, qword ptr [rsp + 0xe0]
008AB553  4C 89 73 30                     mov qword ptr [rbx + 0x30], r14
008AB557  8B 84 24 28 01 00 00            mov eax, dword ptr [rsp + 0x128]
008AB55E  89 43 78                        mov dword ptr [rbx + 0x78], eax
008AB561  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
008AB569  48 89 83 80 00 00 00            mov qword ptr [rbx + 0x80], rax
008AB570  8B 84 24 40 01 00 00            mov eax, dword ptr [rsp + 0x140]
008AB577  89 83 98 00 00 00               mov dword ptr [rbx + 0x98], eax
008AB57D  44 8B 6C 24 58                  mov r13d, dword ptr [rsp + 0x58]
008AB582  44 88 AB 9C 00 00 00            mov byte ptr [rbx + 0x9c], r13b
008AB589  48 8D 8B A0 00 00 00            lea rcx, [rbx + 0xa0]
008AB590  0F 57 C0                        xorps xmm0, xmm0
008AB593  0F 11 01                        movups xmmword ptr [rcx], xmm0
008AB596  0F 11 41 10                     movups xmmword ptr [rcx + 0x10], xmm0
008AB59A  B8 28 00 00 00                  mov eax, 0x28
008AB59F  66 89 01                        mov word ptr [rcx], ax
008AB5A2  48 89 71 20                     mov qword ptr [rcx + 0x20], rsi
008AB5A6  48 8B 94 24 48 01 00 00         mov rdx, qword ptr [rsp + 0x148]
008AB5AE  48 85 D2                        test rdx, rdx
008AB5B1  0F 85 89 03 00 00               jne 0x1408ab940
008AB5B7  48 39 7C 24 70                  cmp qword ptr [rsp + 0x70], rdi
008AB5BC  0F 84 3D 01 00 00               je 0x1408ab6ff
008AB5C2  48 8B 83 A8 00 00 00            mov rax, qword ptr [rbx + 0xa8]
008AB5C9  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008AB5CE  4C 8B F7                        mov r14, rdi
008AB5D1  41 B8 49 6F 53 6A               mov r8d, 0x6a536f49
008AB5D7  41 BF 6C 00 00 00               mov r15d, 0x6c
008AB5DD  41 8B D7                        mov edx, r15d
008AB5E0  B9 00 01 00 00                  mov ecx, 0x100
008AB5E5  E8 06 6B 2D 00                  call 0x140b820f0
008AB5EA  48 85 C0                        test rax, rax
008AB5ED  0F 85 5B EC 26 00               jne 0x140b1a24e
008AB5F3  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
008AB5F9  44 89 7C 24 40                  mov dword ptr [rsp + 0x40], r15d
008AB5FE  E9 C0 08 00 00                  jmp 0x1408abec3
008AB603  E8 C8 F4 E0 FF                  call 0x1406baad0
008AB608  E9 94 FE FF FF                  jmp 0x1408ab4a1
008AB60D  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
008AB612  49 8B C8                        mov rcx, r8
008AB615  E8 96 EF E0 FF                  call 0x1406ba5b0
008AB61A  E9 82 FE FF FF                  jmp 0x1408ab4a1
008AB61F  F7 84 24 00 01 00 00 F8 FF FF FF  test dword ptr [rsp + 0x100], 0xfffffff8
008AB62A  0F 94 C1                        sete cl
008AB62D  F7 84 24 F8 00 00 00 48 00 A5 FF  test dword ptr [rsp + 0xf8], 0xffa50048
008AB638  0F 94 C0                        sete al
008AB63B  84 C8                           test al, cl
008AB63D  0F 84 74 EA 26 00               je 0x140b1a0b7
008AB643  83 BC 24 08 01 00 00 05         cmp dword ptr [rsp + 0x108], 5
008AB64B  0F 87 66 EA 26 00               ja 0x140b1a0b7
008AB651  41 F7 C5 00 00 00 EF            test r13d, 0xef000000
008AB658  0F 85 59 EA 26 00               jne 0x140b1a0b7
008AB65E  41 8B D5                        mov edx, r13d
008AB661  83 E2 30                        and edx, 0x30
008AB664  0F 95 C1                        setne cl
008AB667  44 8B 8C 24 D8 00 00 00         mov r9d, dword ptr [rsp + 0xd8]
008AB66F  41 0F BA E1 14                  bt r9d, 0x14
008AB674  0F 93 C0                        setae al
008AB677  84 C8                           test al, cl
008AB679  0F 85 38 EA 26 00               jne 0x140b1a0b7
008AB67F  41 0F BA E5 0C                  bt r13d, 0xc
008AB684  0F 82 50 08 00 00               jb 0x1408abeda
008AB68A  83 FA 30                        cmp edx, 0x30
008AB68D  0F 84 24 EA 26 00               je 0x140b1a0b7
008AB693  41 8B C5                        mov eax, r13d
008AB696  24 41                           and al, 0x41
008AB698  40 3A C6                        cmp al, sil
008AB69B  0F 84 B4 02 00 00               je 0x1408ab955
008AB6A1  41 8B C5                        mov eax, r13d
008AB6A4  B9 00 01 10 00                  mov ecx, 0x100100
008AB6A9  23 C1                           and eax, ecx
008AB6AB  3B C1                           cmp eax, ecx
008AB6AD  0F 84 04 EA 26 00               je 0x140b1a0b7
008AB6B3  41 8B C5                        mov eax, r13d
008AB6B6  B9 00 01 01 00                  mov ecx, 0x10100
008AB6BB  23 C1                           and eax, ecx
008AB6BD  3B C1                           cmp eax, ecx
008AB6BF  0F 84 F2 E9 26 00               je 0x140b1a0b7
008AB6C5  41 8B C5                        mov eax, r13d
008AB6C8  B9 00 00 11 00                  mov ecx, 0x110000
008AB6CD  23 C1                           and eax, ecx
008AB6CF  3B C1                           cmp eax, ecx
008AB6D1  0F 84 E0 E9 26 00               je 0x140b1a0b7
008AB6D7  41 F6 C5 08                     test r13b, 8
008AB6DB  0F 85 09 08 00 00               jne 0x1408abeea
008AB6E1  39 3D E1 F2 55 00               cmp dword ptr [rip + 0x55f2e1], edi
008AB6E7  0F 85 F4 02 00 00               jne 0x1408ab9e1
008AB6ED  39 BC 24 28 01 00 00            cmp dword ptr [rsp + 0x128], edi
008AB6F4  0F 84 B9 FC FF FF               je 0x1408ab3b3
008AB6FA  E9 62 E9 26 00                  jmp 0x140b1a061
008AB6FF  48 39 B3 C0 00 00 00            cmp qword ptr [rbx + 0xc0], rsi
008AB706  75 0C                           jne 0x1408ab714
008AB708  E8 93 DD B5 FF                  call 0x1404094a0
008AB70D  48 89 83 C0 00 00 00            mov qword ptr [rbx + 0xc0], rax
008AB714  89 7B 10                        mov dword ptr [rbx + 0x10], edi
008AB717  48 89 7B 08                     mov qword ptr [rbx + 8], rdi
008AB71B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AB724  48 01 B0 90 03 00 00            add qword ptr [rax + 0x390], rsi
008AB72B  65 FF 04 25 E4 2E 00 00         inc dword ptr gs:[0x2ee4]
008AB733  48 8D 44 24 78                  lea rax, [rsp + 0x78]
008AB738  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008AB73D  48 8B 83 C0 00 00 00            mov rax, qword ptr [rbx + 0xc0]
008AB744  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008AB749  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
008AB74E  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
008AB755  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008AB759  45 33 C9                        xor r9d, r9d
008AB75C  45 8A C5                        mov r8b, r13b
008AB75F  48 8B 15 7A B3 71 00            mov rdx, qword ptr [rip + 0x71b37a]
008AB766  49 8B CE                        mov rcx, r14
008AB769  E8 32 F1 FE FF                  call 0x14089a8a0
008AB76E  44 8B F0                        mov r14d, eax
008AB771  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008AB775  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
008AB779  48 85 C9                        test rcx, rcx
008AB77C  0F 85 0B 07 00 00               jne 0x1408abe8d
008AB782  39 7C 24 5C                     cmp dword ptr [rsp + 0x5c], edi
008AB786  0F 85 05 08 00 00               jne 0x1408abf91
008AB78C  48 8B CB                        mov rcx, rbx
008AB78F  E8 4C 5A FF FF                  call 0x1408a11e0
008AB794  44 8B 7B 20                     mov r15d, dword ptr [rbx + 0x20]
008AB798  44 89 BC 24 38 01 00 00         mov dword ptr [rsp + 0x138], r15d
008AB7A0  45 85 F6                        test r14d, r14d
008AB7A3  0F 88 53 01 00 00               js 0x1408ab8fc
008AB7A9  41 81 FF 51 02 AA BE            cmp r15d, 0xbeaa0251
008AB7B0  0F 85 F1 07 00 00               jne 0x1408abfa7
008AB7B6  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008AB7BA  0F BA 68 50 12                  bts dword ptr [rax + 0x50], 0x12
008AB7BF  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008AB7C3  0F BA 70 50 19                  btr dword ptr [rax + 0x50], 0x19
008AB7C8  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008AB7CD  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
008AB7D5  48 89 01                        mov qword ptr [rcx], rax
008AB7D8  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
008AB7DC  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
008AB7E1  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
008AB7E4  41 89 04 24                     mov dword ptr [r12], eax
008AB7E8  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
008AB7EB  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008AB7EF  EB 16                           jmp 0x1408ab807
008AB7F1  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008AB7F5  BE 01 00 00 00                  mov esi, 1
008AB7FA  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
008AB7FF  44 8B BC 24 38 01 00 00         mov r15d, dword ptr [rsp + 0x138]
008AB807  41 81 FF 51 02 AA BE            cmp r15d, 0xbeaa0251
008AB80E  75 3B                           jne 0x1408ab84b
008AB810  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008AB814  48 85 C9                        test rcx, rcx
008AB817  74 32                           je 0x1408ab84b
008AB819  E8 32 DB A4 FF                  call 0x1402f9350
008AB81E  EB 2B                           jmp 0x1408ab84b
008AB820  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008AB825  E8 F6 5B FF FF                  call 0x1408a1420
008AB82A  48 89 BB A8 00 00 00            mov qword ptr [rbx + 0xa8], rdi
008AB831  4D 85 F6                        test r14, r14
008AB834  0F 85 31 07 00 00               jne 0x1408abf6b
008AB83A  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
008AB83E  48 85 C9                        test rcx, rcx
008AB841  0F 85 31 07 00 00               jne 0x1408abf78
008AB847  45 89 3C 24                     mov dword ptr [r12], r15d
008AB84B  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008AB854  48 8B 8A 80 08 00 00            mov rcx, qword ptr [rdx + 0x880]
008AB85B  01 71 1C                        add dword ptr [rcx + 0x1c], esi
008AB85E  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008AB862  66 39 01                        cmp word ptr [rcx], ax
008AB865  0F 83 0E 01 00 00               jae 0x1408ab979
008AB86B  48 8B D3                        mov rdx, rbx
008AB86E  E8 3D ED E0 FF                  call 0x1406ba5b0
008AB873  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
008AB877  48 81 C4 90 00 00 00            add rsp, 0x90
008AB87E  41 5F                           pop r15
008AB880  41 5E                           pop r14
008AB882  41 5D                           pop r13
008AB884  41 5C                           pop r12
008AB886  5F                              pop rdi
008AB887  5E                              pop rsi
008AB888  5B                              pop rbx
008AB889  C3                              ret
008AB88A  CC                              int3
008AB88B  41 8B C5                        mov eax, r13d
008AB88E  41 0F BA F5 1F                  btr r13d, 0x1f
008AB893  85 C0                           test eax, eax
008AB895  44 0F 49 E8                     cmovns r13d, eax
008AB899  8B 94 24 84 00 00 00            mov edx, dword ptr [rsp + 0x84]
008AB8A0  0F BA EA 0A                     bts edx, 0xa
008AB8A4  85 C0                           test eax, eax
008AB8A6  0F 49 94 24 84 00 00 00         cmovns edx, dword ptr [rsp + 0x84]
008AB8AE  89 94 24 38 01 00 00            mov dword ptr [rsp + 0x138], edx
008AB8B5  4D 85 E4                        test r12, r12
008AB8B8  0F 85 3B 06 00 00               jne 0x1408abef9
008AB8BE  41 0F BA E5 1C                  bt r13d, 0x1c
008AB8C3  0F 82 47 06 00 00               jb 0x1408abf10
008AB8C9  48 89 BB D8 00 00 00            mov qword ptr [rbx + 0xd8], rdi
008AB8D0  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
008AB8D8  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
008AB8DD  44 8B B4 24 20 01 00 00         mov r14d, dword ptr [rsp + 0x120]
008AB8E5  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
008AB8EA  4D 85 FF                        test r15, r15
008AB8ED  0F 85 6E E8 26 00               jne 0x140b1a161
008AB8F3  48 89 7B 48                     mov qword ptr [rbx + 0x48], rdi
008AB8F7  E9 EC FB FF FF                  jmp 0x1408ab4e8
008AB8FC  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
008AB8FF  85 C9                           test ecx, ecx
008AB901  0F 88 B0 00 00 00               js 0x1408ab9b7
008AB907  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008AB90B  48 85 C9                        test rcx, rcx
008AB90E  0F 85 E9 06 00 00               jne 0x1408abffd
008AB914  41 81 FE 34 00 00 C0            cmp r14d, 0xc0000034
008AB91B  0F 85 E6 FE FF FF               jne 0x1408ab807
008AB921  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
008AB925  B9 03 00 00 A0                  mov ecx, 0xa0000003
008AB92A  48 3B C1                        cmp rax, rcx
008AB92D  0F 85 66 05 00 00               jne 0x1408abe99
008AB933  C7 44 24 40 80 02 00 C0         mov dword ptr [rsp + 0x40], 0xc0000280
008AB93B  E9 C7 FE FF FF                  jmp 0x1408ab807
008AB940  4C 0F BF 02                     movsx r8, word ptr [rdx]
008AB944  4C 3B C0                        cmp r8, rax
008AB947  4C 0F 47 C0                     cmova r8, rax
008AB94B  E8 F0 AE E1 FF                  call 0x1406c6840
008AB950  E9 62 FC FF FF                  jmp 0x1408ab5b7
008AB955  41 F7 C5 CC 0A 5C EF            test r13d, 0xef5c0acc
008AB95C  0F 85 55 E7 26 00               jne 0x140b1a0b7
008AB962  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
008AB969  FF C8                           dec eax
008AB96B  83 F8 02                        cmp eax, 2
008AB96E  0F 86 2D FD FF FF               jbe 0x1408ab6a1
008AB974  E9 3E E7 26 00                  jmp 0x140b1a0b7
008AB979  01 71 20                        add dword ptr [rcx + 0x20], esi
008AB97C  48 8B 8A 88 08 00 00            mov rcx, qword ptr [rdx + 0x888]
008AB983  01 71 1C                        add dword ptr [rcx + 0x1c], esi
008AB986  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008AB98A  66 39 01                        cmp word ptr [rcx], ax
008AB98D  0F 82 D8 FE FF FF               jb 0x1408ab86b
008AB993  01 71 20                        add dword ptr [rcx + 0x20], esi
008AB996  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
008AB99A  48 8D 05 AF 6E 2D 00            lea rax, [rip + 0x2d6eaf]
008AB9A1  48 8B CB                        mov rcx, rbx
008AB9A4  48 3B D0                        cmp rdx, rax
008AB9A7  0F 85 B1 05 00 00               jne 0x1408abf5e
008AB9AD  E8 9E 6E 2D 00                  call 0x140b82850
008AB9B2  E9 BC FE FF FF                  jmp 0x1408ab873
008AB9B7  44 8B F1                        mov r14d, ecx
008AB9BA  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
008AB9BE  8B C1                           mov eax, ecx
008AB9C0  25 00 00 00 C0                  and eax, 0xc0000000
008AB9C5  3D 00 00 00 80                  cmp eax, 0x80000000
008AB9CA  0F 84 FD 05 00 00               je 0x1408abfcd
008AB9D0  81 F9 79 02 00 C0               cmp ecx, 0xc0000279
008AB9D6  0F 85 38 FF FF FF               jne 0x1408ab914
008AB9DC  E9 EC 05 00 00                  jmp 0x1408abfcd
008AB9E1  45 85 C9                        test r9d, r9d
008AB9E4  0F 85 03 FD FF FF               jne 0x1408ab6ed
008AB9EA  E9 07 E6 26 00                  jmp 0x140b19ff6
008AB9EF  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
008AB9F7  48 85 C9                        test rcx, rcx
008AB9FA  0F 84 93 00 00 00               je 0x1408aba93
008ABA00  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008ABA09  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
008ABA11  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
008ABA18  48 39 B8 10 03 00 00            cmp qword ptr [rax + 0x310], rdi
008ABA1F  75 42                           jne 0x1408aba63
008ABA21  8B 94 24 20 01 00 00            mov edx, dword ptr [rsp + 0x120]
008ABA28  85 D2                           test edx, edx
008ABA2A  0F 85 D0 01 00 00               jne 0x1408abc00
008ABA30  83 FA 18                        cmp edx, 0x18
008ABA33  0F 82 EB 01 00 00               jb 0x1408abc24
008ABA39  48 8B 01                        mov rax, qword ptr [rcx]
008ABA3C  48 89 83 D8 00 00 00            mov qword ptr [rbx + 0xd8], rax
008ABA43  4C 8B 71 08                     mov r14, qword ptr [rcx + 8]
008ABA47  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
008ABA4C  44 8B 79 10                     mov r15d, dword ptr [rcx + 0x10]
008ABA50  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
008ABA55  83 FA 20                        cmp edx, 0x20
008ABA58  0F 83 45 02 00 00               jae 0x1408abca3
008ABA5E  E9 78 02 00 00                  jmp 0x1408abcdb
008ABA63  0F B7 80 EC 06 00 00            movzx eax, word ptr [rax + 0x6ec]
008ABA6A  BA 4C 01 00 00                  mov edx, 0x14c
008ABA6F  66 3B C2                        cmp ax, dx
008ABA72  75 10                           jne 0x1408aba84
008ABA74  40 8A C6                        mov al, sil
008ABA77  88 44 24 4C                     mov byte ptr [rsp + 0x4c], al
008ABA7B  84 C0                           test al, al
008ABA7D  74 A2                           je 0x1408aba21
008ABA7F  E9 8E 00 00 00                  jmp 0x1408abb12
008ABA84  BA C4 01 00 00                  mov edx, 0x1c4
008ABA89  66 3B C2                        cmp ax, dx
008ABA8C  40 8A C7                        mov al, dil
008ABA8F  75 E6                           jne 0x1408aba77
008ABA91  EB E1                           jmp 0x1408aba74
008ABA93  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008ABA9C  48 8B 8A 80 08 00 00            mov rcx, qword ptr [rdx + 0x880]
008ABAA3  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
008ABAA6  03 C6                           add eax, esi
008ABAA8  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
008ABAAB  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008ABAAF  66 39 01                        cmp word ptr [rcx], ax
008ABAB2  72 4C                           jb 0x1408abb00
008ABAB4  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
008ABAB7  03 C6                           add eax, esi
008ABAB9  89 41 20                        mov dword ptr [rcx + 0x20], eax
008ABABC  48 8B 8A 88 08 00 00            mov rcx, qword ptr [rdx + 0x888]
008ABAC3  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
008ABAC6  03 C6                           add eax, esi
008ABAC8  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
008ABACB  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008ABACF  66 39 01                        cmp word ptr [rcx], ax
008ABAD2  72 2C                           jb 0x1408abb00
008ABAD4  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
008ABAD7  03 C6                           add eax, esi
008ABAD9  89 41 20                        mov dword ptr [rcx + 0x20], eax
008ABADC  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
008ABAE0  48 8D 05 69 6D 2D 00            lea rax, [rip + 0x2d6d69]
008ABAE7  48 8B CB                        mov rcx, rbx
008ABAEA  48 3B D0                        cmp rdx, rax
008ABAED  75 07                           jne 0x1408abaf6
008ABAEF  E8 5C 6D 2D 00                  call 0x140b82850
008ABAF4  EB 12                           jmp 0x1408abb08
008ABAF6  48 8B C2                        mov rax, rdx
008ABAF9  E8 D2 EF E0 FF                  call 0x1406baad0
008ABAFE  EB 08                           jmp 0x1408abb08
008ABB00  48 8B D3                        mov rdx, rbx
008ABB03  E8 A8 EA E0 FF                  call 0x1406ba5b0
008ABB08  B8 0D 00 00 C0                  mov eax, 0xc000000d
008ABB0D  E9 65 FD FF FF                  jmp 0x1408ab877
008ABB12  8B 94 24 20 01 00 00            mov edx, dword ptr [rsp + 0x120]
008ABB19  85 D2                           test edx, edx
008ABB1B  74 1B                           je 0x1408abb38
008ABB1D  41 84 C9                        test r9b, cl
008ABB20  74 05                           je 0x1408abb27
008ABB22  E8 A9 E4 FE FF                  call 0x140899fd0
008ABB27  4C 8D 04 11                     lea r8, [rcx + rdx]
008ABB2B  4D 3B C2                        cmp r8, r10
008ABB2E  77 05                           ja 0x1408abb35
008ABB30  4C 3B C1                        cmp r8, rcx
008ABB33  73 03                           jae 0x1408abb38
008ABB35  41 8A 02                        mov al, byte ptr [r10]
008ABB38  83 FA 10                        cmp edx, 0x10
008ABB3B  73 7F                           jae 0x1408abbbc
008ABB3D  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008ABB46  48 8B 8A 80 08 00 00            mov rcx, qword ptr [rdx + 0x880]
008ABB4D  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
008ABB50  03 C6                           add eax, esi
008ABB52  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
008ABB55  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008ABB59  66 39 01                        cmp word ptr [rcx], ax
008ABB5C  72 4C                           jb 0x1408abbaa
008ABB5E  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
008ABB61  03 C6                           add eax, esi
008ABB63  89 41 20                        mov dword ptr [rcx + 0x20], eax
008ABB66  48 8B 8A 88 08 00 00            mov rcx, qword ptr [rdx + 0x888]
008ABB6D  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
008ABB70  03 C6                           add eax, esi
008ABB72  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
008ABB75  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008ABB79  66 39 01                        cmp word ptr [rcx], ax
008ABB7C  72 2C                           jb 0x1408abbaa
008ABB7E  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
008ABB81  03 C6                           add eax, esi
008ABB83  89 41 20                        mov dword ptr [rcx + 0x20], eax
008ABB86  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
008ABB8A  48 8D 05 BF 6C 2D 00            lea rax, [rip + 0x2d6cbf]
008ABB91  48 8B CB                        mov rcx, rbx
008ABB94  48 3B D0                        cmp rdx, rax
008ABB97  75 07                           jne 0x1408abba0
008ABB99  E8 B2 6C 2D 00                  call 0x140b82850
008ABB9E  EB 12                           jmp 0x1408abbb2
008ABBA0  48 8B C2                        mov rax, rdx
008ABBA3  E8 28 EF E0 FF                  call 0x1406baad0
008ABBA8  EB 08                           jmp 0x1408abbb2
008ABBAA  48 8B D3                        mov rdx, rbx
008ABBAD  E8 FE E9 E0 FF                  call 0x1406ba5b0
008ABBB2  B8 0D 00 00 C0                  mov eax, 0xc000000d
008ABBB7  E9 BB FC FF FF                  jmp 0x1408ab877
008ABBBC  48 8B 01                        mov rax, qword ptr [rcx]
008ABBBF  48 89 83 D8 00 00 00            mov qword ptr [rbx + 0xd8], rax
008ABBC6  44 8B 71 08                     mov r14d, dword ptr [rcx + 8]
008ABBCA  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
008ABBCF  44 8B 79 0C                     mov r15d, dword ptr [rcx + 0xc]
008ABBD3  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
008ABBD8  83 FA 18                        cmp edx, 0x18
008ABBDB  0F 82 FA 00 00 00               jb 0x1408abcdb
008ABBE1  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
008ABBE4  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008ABBE9  48 85 C0                        test rax, rax
008ABBEC  0F 84 E9 00 00 00               je 0x1408abcdb
008ABBF2  41 84 C1                        test r9b, al
008ABBF5  0F 84 C0 00 00 00               je 0x1408abcbb
008ABBFB  E8 D0 E3 FE FF                  call 0x140899fd0
008ABC00  41 84 C9                        test r9b, cl
008ABC03  74 05                           je 0x1408abc0a
008ABC05  E8 C6 E3 FE FF                  call 0x140899fd0
008ABC0A  4C 8D 04 11                     lea r8, [rcx + rdx]
008ABC0E  4D 3B C2                        cmp r8, r10
008ABC11  77 09                           ja 0x1408abc1c
008ABC13  4C 3B C1                        cmp r8, rcx
008ABC16  0F 83 14 FE FF FF               jae 0x1408aba30
008ABC1C  41 8A 02                        mov al, byte ptr [r10]
008ABC1F  E9 0C FE FF FF                  jmp 0x1408aba30
008ABC24  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008ABC2D  48 8B 8A 80 08 00 00            mov rcx, qword ptr [rdx + 0x880]
008ABC34  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
008ABC37  03 C6                           add eax, esi
008ABC39  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
008ABC3C  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008ABC40  66 39 01                        cmp word ptr [rcx], ax
008ABC43  72 4C                           jb 0x1408abc91
008ABC45  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
008ABC48  03 C6                           add eax, esi
008ABC4A  89 41 20                        mov dword ptr [rcx + 0x20], eax
008ABC4D  48 8B 8A 88 08 00 00            mov rcx, qword ptr [rdx + 0x888]
008ABC54  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
008ABC57  03 C6                           add eax, esi
008ABC59  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
008ABC5C  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008ABC60  66 39 01                        cmp word ptr [rcx], ax
008ABC63  72 2C                           jb 0x1408abc91
008ABC65  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
008ABC68  03 C6                           add eax, esi
008ABC6A  89 41 20                        mov dword ptr [rcx + 0x20], eax
008ABC6D  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
008ABC71  48 8D 05 D8 6B 2D 00            lea rax, [rip + 0x2d6bd8]
008ABC78  48 8B CB                        mov rcx, rbx
008ABC7B  48 3B D0                        cmp rdx, rax
008ABC7E  75 07                           jne 0x1408abc87
008ABC80  E8 CB 6B 2D 00                  call 0x140b82850
008ABC85  EB 12                           jmp 0x1408abc99
008ABC87  48 8B C2                        mov rax, rdx
008ABC8A  E8 41 EE E0 FF                  call 0x1406baad0
008ABC8F  EB 08                           jmp 0x1408abc99
008ABC91  48 8B D3                        mov rdx, rbx
008ABC94  E8 17 E9 E0 FF                  call 0x1406ba5b0
008ABC99  B8 0D 00 00 C0                  mov eax, 0xc000000d
008ABC9E  E9 D4 FB FF FF                  jmp 0x1408ab877
008ABCA3  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
008ABCA7  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008ABCAC  48 85 C0                        test rax, rax
008ABCAF  74 2A                           je 0x1408abcdb
008ABCB1  41 84 C1                        test r9b, al
008ABCB4  74 05                           je 0x1408abcbb
008ABCB6  E8 15 E3 FE FF                  call 0x140899fd0
008ABCBB  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008ABCC0  48 8D 48 20                     lea rcx, [rax + 0x20]
008ABCC4  49 3B CA                        cmp rcx, r10
008ABCC7  77 05                           ja 0x1408abcce
008ABCC9  48 3B C8                        cmp rcx, rax
008ABCCC  73 0D                           jae 0x1408abcdb
008ABCCE  41 8A 02                        mov al, byte ptr [r10]
008ABCD1  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
008ABCD6  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
008ABCDB  E9 F4 F7 FF FF                  jmp 0x1408ab4d4
008ABCE0  8B D8                           mov ebx, eax
008ABCE2  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008ABCEB  4C 8B 82 80 08 00 00            mov r8, qword ptr [rdx + 0x880]
008ABCF2  41 FF 40 1C                     inc dword ptr [r8 + 0x1c]
008ABCF6  41 0F B7 48 10                  movzx ecx, word ptr [r8 + 0x10]
008ABCFB  66 41 39 08                     cmp word ptr [r8], cx
008ABCFF  72 46                           jb 0x1408abd47
008ABD01  41 FF 40 20                     inc dword ptr [r8 + 0x20]
008ABD05  4C 8B 82 88 08 00 00            mov r8, qword ptr [rdx + 0x888]
008ABD0C  41 FF 40 1C                     inc dword ptr [r8 + 0x1c]
008ABD10  41 0F B7 40 10                  movzx eax, word ptr [r8 + 0x10]
008ABD15  66 41 39 00                     cmp word ptr [r8], ax
008ABD19  72 2C                           jb 0x1408abd47
008ABD1B  41 FF 40 20                     inc dword ptr [r8 + 0x20]
008ABD1F  49 8B 40 38                     mov rax, qword ptr [r8 + 0x38]
008ABD23  48 8D 0D 26 6B 2D 00            lea rcx, [rip + 0x2d6b26]
008ABD2A  48 3B C1                        cmp rax, rcx
008ABD2D  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008ABD32  75 0C                           jne 0x1408abd40
008ABD34  E8 17 6B 2D 00                  call 0x140b82850
008ABD39  8B C3                           mov eax, ebx
008ABD3B  E9 37 FB FF FF                  jmp 0x1408ab877
008ABD40  E8 8B ED E0 FF                  call 0x1406baad0
008ABD45  EB F2                           jmp 0x1408abd39
008ABD47  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
008ABD4C  49 8B C8                        mov rcx, r8
008ABD4F  E8 5C E8 E0 FF                  call 0x1406ba5b0
008ABD54  EB E3                           jmp 0x1408abd39
008ABD56  45 85 FF                        test r15d, r15d
008ABD59  0F 84 82 F7 FF FF               je 0x1408ab4e1
008ABD5F  40 88 7C 24 44                  mov byte ptr [rsp + 0x44], dil
008ABD64  45 84 F1                        test r9b, r14b
008ABD67  75 6B                           jne 0x1408abdd4
008ABD69  45 8B E7                        mov r12d, r15d
008ABD6C  4B 8D 04 34                     lea rax, [r12 + r14]
008ABD70  49 3B C2                        cmp rax, r10
008ABD73  77 64                           ja 0x1408abdd9
008ABD75  49 3B C6                        cmp rax, r14
008ABD78  72 5F                           jb 0x1408abdd9
008ABD7A  41 B8 49 6F 45 61               mov r8d, 0x61456f49
008ABD80  49 8B D4                        mov rdx, r12
008ABD83  B9 63 00 00 00                  mov ecx, 0x63
008ABD88  E8 63 63 2D 00                  call 0x140b820f0
008ABD8D  48 89 43 48                     mov qword ptr [rbx + 0x48], rax
008ABD91  44 89 7B 50                     mov dword ptr [rbx + 0x50], r15d
008ABD95  4D 8B C4                        mov r8, r12
008ABD98  49 8B D6                        mov rdx, r14
008ABD9B  48 8B C8                        mov rcx, rax
008ABD9E  E8 9D AA E1 FF                  call 0x1406c6840
008ABDA3  4C 8B A4 24 E8 00 00 00         mov r12, qword ptr [rsp + 0xe8]
008ABDAB  4D 8D 44 24 08                  lea r8, [r12 + 8]
008ABDB0  41 8B D7                        mov edx, r15d
008ABDB3  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
008ABDB7  E8 34 FC 17 00                  call 0x140a2b9f0
008ABDBC  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008ABDC0  85 C0                           test eax, eax
008ABDC2  79 24                           jns 0x1408abde8
008ABDC4  40 88 74 24 44                  mov byte ptr [rsp + 0x44], sil
008ABDC9  41 89 04 24                     mov dword ptr [r12], eax
008ABDCD  8B C8                           mov ecx, eax
008ABDCF  E8 7C AC A4 FF                  call 0x1402f6a50
008ABDD4  E8 F7 E1 FE FF                  call 0x140899fd0
008ABDD9  41 8A 02                        mov al, byte ptr [r10]
008ABDDC  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
008ABDE1  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
008ABDE6  EB 92                           jmp 0x1408abd7a
008ABDE8  8B 94 24 38 01 00 00            mov edx, dword ptr [rsp + 0x138]
008ABDEF  E9 FF F6 FF FF                  jmp 0x1408ab4f3
008ABDF4  8B F8                           mov edi, eax
008ABDF6  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
008ABDFB  48 83 7B 48 00                  cmp qword ptr [rbx + 0x48], 0
008ABE00  74 0B                           je 0x1408abe0d
008ABE02  33 D2                           xor edx, edx
008ABE04  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
008ABE08  E8 63 6A 2D 00                  call 0x140b82870
008ABE0D  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008ABE16  4C 8B 82 80 08 00 00            mov r8, qword ptr [rdx + 0x880]
008ABE1D  41 FF 40 1C                     inc dword ptr [r8 + 0x1c]
008ABE21  41 0F B7 40 10                  movzx eax, word ptr [r8 + 0x10]
008ABE26  66 41 39 00                     cmp word ptr [r8], ax
008ABE2A  72 3F                           jb 0x1408abe6b
008ABE2C  41 FF 40 20                     inc dword ptr [r8 + 0x20]
008ABE30  4C 8B 82 88 08 00 00            mov r8, qword ptr [rdx + 0x888]
008ABE37  41 FF 40 1C                     inc dword ptr [r8 + 0x1c]
008ABE3B  41 0F B7 40 10                  movzx eax, word ptr [r8 + 0x10]
008ABE40  66 41 39 00                     cmp word ptr [r8], ax
008ABE44  72 25                           jb 0x1408abe6b
008ABE46  41 FF 40 20                     inc dword ptr [r8 + 0x20]
008ABE4A  49 8B 40 38                     mov rax, qword ptr [r8 + 0x38]
008ABE4E  48 8D 0D FB 69 2D 00            lea rcx, [rip + 0x2d69fb]
008ABE55  48 3B C1                        cmp rax, rcx
008ABE58  48 8B CB                        mov rcx, rbx
008ABE5B  75 07                           jne 0x1408abe64
008ABE5D  E8 EE 69 2D 00                  call 0x140b82850
008ABE62  EB 12                           jmp 0x1408abe76
008ABE64  E8 67 EC E0 FF                  call 0x1406baad0
008ABE69  EB 0B                           jmp 0x1408abe76
008ABE6B  48 8B D3                        mov rdx, rbx
008ABE6E  49 8B C8                        mov rcx, r8
008ABE71  E8 3A E7 E0 FF                  call 0x1406ba5b0
008ABE76  80 7C 24 44 00                  cmp byte ptr [rsp + 0x44], 0
008ABE7B  74 09                           je 0x1408abe86
008ABE7D  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
008ABE81  E9 F1 F9 FF FF                  jmp 0x1408ab877
008ABE86  8B C7                           mov eax, edi
008ABE88  E9 EA F9 FF FF                  jmp 0x1408ab877
008ABE8D  33 D2                           xor edx, edx
008ABE8F  E8 DC 69 2D 00                  call 0x140b82870
008ABE94  E9 E9 F8 FF FF                  jmp 0x1408ab782
008ABE99  B9 0C 00 00 A0                  mov ecx, 0xa000000c
008ABE9E  48 3B C1                        cmp rax, rcx
008ABEA1  0F 84 8C FA FF FF               je 0x1408ab933
008ABEA7  B9 19 00 00 A0                  mov ecx, 0xa0000019
008ABEAC  48 3B C1                        cmp rax, rcx
008ABEAF  0F 85 52 F9 FF FF               jne 0x1408ab807
008ABEB5  E9 79 FA FF FF                  jmp 0x1408ab933
008ABEBA  45 85 FF                        test r15d, r15d
008ABEBD  0F 89 C1 00 00 00               jns 0x1408abf84
008ABEC3  39 7C 24 5C                     cmp dword ptr [rsp + 0x5c], edi
008ABEC7  0F 85 53 F9 FF FF               jne 0x1408ab820
008ABECD  48 8B CB                        mov rcx, rbx
008ABED0  E8 0B 53 FF FF                  call 0x1408a11e0
008ABED5  E9 57 F9 FF FF                  jmp 0x1408ab831
008ABEDA  41 0F BA E1 10                  bt r9d, 0x10
008ABEDF  0F 83 D2 E1 26 00               jae 0x140b1a0b7
008ABEE5  E9 A0 F7 FF FF                  jmp 0x1408ab68a
008ABEEA  41 F6 C1 04                     test r9b, 4
008ABEEE  0F 85 C3 E1 26 00               jne 0x140b1a0b7
008ABEF4  E9 E8 F7 FF FF                  jmp 0x1408ab6e1
008ABEF9  49 8B 04 24                     mov rax, qword ptr [r12]
008ABEFD  48 85 C0                        test rax, rax
008ABF00  0F 88 B1 E1 26 00               js 0x140b1a0b7
008ABF06  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008ABF0B  E9 AE F9 FF FF                  jmp 0x1408ab8be
008ABF10  83 BC 24 20 01 00 00 18         cmp dword ptr [rsp + 0x120], 0x18
008ABF18  0F 82 99 E1 26 00               jb 0x140b1a0b7
008ABF1E  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
008ABF26  48 8B 01                        mov rax, qword ptr [rcx]
008ABF29  48 89 83 D8 00 00 00            mov qword ptr [rbx + 0xd8], rax
008ABF30  4C 8B 79 08                     mov r15, qword ptr [rcx + 8]
008ABF34  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
008ABF39  44 8B 71 10                     mov r14d, dword ptr [rcx + 0x10]
008ABF3D  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
008ABF42  83 BC 24 20 01 00 00 20         cmp dword ptr [rsp + 0x120], 0x20
008ABF4A  0F 82 9A F9 FF FF               jb 0x1408ab8ea
008ABF50  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
008ABF54  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008ABF59  E9 8C F9 FF FF                  jmp 0x1408ab8ea
008ABF5E  48 8B C2                        mov rax, rdx
008ABF61  E8 6A EB E0 FF                  call 0x1406baad0
008ABF66  E9 08 F9 FF FF                  jmp 0x1408ab873
008ABF6B  49 8B CE                        mov rcx, r14
008ABF6E  E8 ED 57 FF FF                  call 0x1408a1760
008ABF73  E9 C2 F8 FF FF                  jmp 0x1408ab83a
008ABF78  33 D2                           xor edx, edx
008ABF7A  E8 F1 68 2D 00                  call 0x140b82870
008ABF7F  E9 C3 F8 FF FF                  jmp 0x1408ab847
008ABF84  4C 8B B4 24 E0 00 00 00         mov r14, qword ptr [rsp + 0xe0]
008ABF8C  E9 6E F7 FF FF                  jmp 0x1408ab6ff
008ABF91  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008ABF96  E8 85 54 FF FF                  call 0x1408a1420
008ABF9B  48 89 BB A8 00 00 00            mov qword ptr [rbx + 0xa8], rdi
008ABFA2  E9 ED F7 FF FF                  jmp 0x1408ab794
008ABFA7  45 85 F6                        test r14d, r14d
008ABFAA  0F 88 4C F9 FF FF               js 0x1408ab8fc
008ABFB0  41 8A D5                        mov dl, r13b
008ABFB3  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
008ABFB8  E8 B3 58 FF FF                  call 0x1408a1870
008ABFBD  41 BE 24 00 00 C0               mov r14d, 0xc0000024
008ABFC3  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
008ABFC8  E9 2F F9 FF FF                  jmp 0x1408ab8fc
008ABFCD  41 89 0C 24                     mov dword ptr [r12], ecx
008ABFD1  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
008ABFD5  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
008ABFDA  E9 35 F9 FF FF                  jmp 0x1408ab914
008ABFDF  44 8B F0                        mov r14d, eax
008ABFE2  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008ABFE6  BE 01 00 00 00                  mov esi, 1
008ABFEB  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
008ABFF0  44 8B BC 24 38 01 00 00         mov r15d, dword ptr [rsp + 0x138]
008ABFF8  E9 17 F9 FF FF                  jmp 0x1408ab914
008ABFFD  41 81 FF 51 02 AA BE            cmp r15d, 0xbeaa0251
008AC004  0F 84 BA E3 26 00               je 0x140b1a3c4
008AC00A  66 39 79 58                     cmp word ptr [rcx + 0x58], di
008AC00E  0F 84 99 E3 26 00               je 0x140b1a3ad
008AC014  33 D2                           xor edx, edx
008AC016  48 8B 49 60                     mov rcx, qword ptr [rcx + 0x60]
008AC01A  E8 51 68 2D 00                  call 0x140b82870
008AC01F  90                              nop
008AC020  E9 88 E3 26 00                  jmp 0x140b1a3ad
008AC025  B8 9A 00 00 C0                  mov eax, 0xc000009a
008AC02A  E9 48 F8 FF FF                  jmp 0x1408ab877
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopCreateFile(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int16 a6, unsigned __int16 a7, unsigned int a8, unsigned int a9, __int64 a10, unsigned int a11, unsigned int a12, __int64 a13, unsigned int a14, unsigned int a15, __int64 a16)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p138;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p44;
    unsigned int v_stack_p48;
    unsigned __int8 v_stack_p4C;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p5C;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_p84;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    v_stack_m44 = (unsigned int)((unsigned int)(a14));
    v_rdi = 0;
    v_stack_m88 = 0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    *(unsigned int *)(v_rsp - 128) = 0;
    v_stack_m6C = 0;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    a1 = 0;
    if (condition_is_above_or_equal) { a1 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)); }
    v_stack_m70 = (unsigned int)(a1);
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176), a2, a3, a4);
    v_stack_m78 = result;
    if (result != 0) goto loc_008AB385;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184), a2, a3, a4);
    v_stack_m78 = result;
    v_rbx = result;
    if (result == 0) {
        a2 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 44);
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 48);
        a3 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 40);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 36);
        result = guard_dispatch_icall(a1, a2, a3, a4);
        v_rbx = result;
        v_stack_m78 = result;
    }
    if (v_rbx == 0) goto loc_008AC025;
    *(unsigned int *)(v_rbx) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)));
    if ((unsigned __int8)((unsigned int)(v_stack_m70)) != 0) goto loc_008AB61F;
    if (((a14) & (512)) != 0) goto loc_008AB61F;
loc_008AB3B3:
    if ((unsigned __int8)((unsigned int)(v_stack_m70)) == 0) goto loc_008AB88B;
    a1 = v_r10;
    if (v_stack_p8 < v_r10) { a1 = v_stack_p8; }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    a1 = v_r10;
    if (v_stack_p20 < v_r10) { a1 = v_stack_p20; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if (a5 != 0) goto loc_008AB417;
    v_stack_m50 = 0;
loc_008AB408:
    if (!sign_flag) goto loc_008AB43A;
    result = RtlRaiseStatus((unsigned int)(0xC000000DULL), a2, (unsigned int)(v_stack_m70), 3);
loc_008AB417:
    if (((3) & ((unsigned __int8)(a5))) != 0) {
        result = ExRaiseDatatypeMisalignment((unsigned int)(0xC000000DULL), a2, (unsigned int)(v_stack_m70), 3);
    }
    result = v_r10;
    if (a5 < v_r10) { result = a5; }
    v_stack_m50 = *(unsigned __int64 *)(a5);
    goto loc_008AB408;
loc_008AB43A:
    goto loc_008AB4A8;
loc_008AB4A8:
    if (a5 < v_r10) goto loc_008AB9EF;
    *(unsigned __int64 *)(v_rbx + 216) = 0;
    v_stack_m68 = a10;
    v_stack_m80 = (unsigned int)((unsigned int)(a11));
loc_008AB4D4:
    *(unsigned __int64 *)(v_rbx + 72) = 0;
    if (a10 != 0) goto loc_008ABD56;
loc_008AB4E1:
loc_008AB4E8:
    *(unsigned int *)(v_rbx + 80) = 0;
loc_008AB4F3:
    *(unsigned int *)(v_rbx) = 0xE00008ULL;
    *(unsigned int *)(v_rbx + 32) = 0;
    *(unsigned __int64 *)(v_rbx + 24) = 0;
    *(unsigned __int64 *)(v_rbx + 56) = v_stack_m50;
    v_r13 = (unsigned int)(((unsigned int)(a9)) & (0xFFFFFFULL));
    *(unsigned int *)(v_rbx + 64) = (unsigned int)(v_r13);
    *(unsigned __int16 *)(v_rbx + 68) = a6;
    *(unsigned __int16 *)(v_rbx + 70) = a7;
    *(unsigned int *)(v_rbx + 88) = (unsigned int)((unsigned int)(a8));
    *(unsigned __int16 *)(v_rbx + 136) = 0;
    *(unsigned __int8 *)(v_rbx + 138) = 0;
    *(unsigned int *)(v_rbx + 84) = (unsigned int)((unsigned int)(a14));
    *(unsigned __int64 *)(v_rbx + 40) = 0;
    *(unsigned __int64 *)(v_rbx + 48) = v_stack_p18;
    *(unsigned int *)(v_rbx + 120) = (unsigned int)((unsigned int)(a12));
    *(unsigned __int64 *)(v_rbx + 128) = a13;
    *(unsigned int *)(v_rbx + 152) = (unsigned int)((unsigned int)(a15));
    *(unsigned __int8 *)(v_rbx + 156) = (unsigned __int8)((unsigned int)(v_stack_m70));
    *(unsigned __int64 *)(v_rbx + 160) = v_xmm0;
    *(unsigned __int64 *)(v_rbx + 160 + 16) = v_xmm0;
    *(unsigned __int16 *)(v_rbx + 160) = 40;
    *(unsigned __int64 *)(v_rbx + 160 + 32) = v_rdi + 1;
    if (a16 != 0) goto loc_008AB940;
loc_008AB5B7:
    if (v_stack_m58 == 0) goto loc_008AB6FF;
    v_stack_m60 = *(unsigned __int64 *)(v_rbx + 168);
    result = ExAllocatePool2(256, 108, (unsigned int)(0x6A536F49ULL), 3);
    v_stack_m88 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_008ABEC3;
loc_008AB61F:
    a1 = (((a7) & (0xFFFFFFF8ULL)) == 0) ? 1 : 0;
    result = (((a6) & (0xFFA50048ULL)) == 0) ? 1 : 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m70)))) & (48));
    a1 = (condition_is_not_equal) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if (condition_is_below) goto loc_008ABEDA;
loc_008AB68A:
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m70)))) & (65));
    if (((unsigned __int8)(result)) == ((unsigned __int8)(v_rdi + 1))) goto loc_008AB955;
loc_008AB6A1:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m70)))) & ((unsigned int)((unsigned int)(0x100100ULL))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m70)))) & ((unsigned int)((unsigned int)(0x10100ULL))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m70)))) & ((unsigned int)((unsigned int)(0x110000ULL))));
    if ((((unsigned __int8)((unsigned int)(v_stack_m70))) & (8)) != 0) goto loc_008ABEEA;
loc_008AB6E1:
    if ((*(unsigned int *)(v_rip + 5632737)) != 0) goto loc_008AB9E1;
loc_008AB6ED:
    if (a12 == 0) goto loc_008AB3B3;
loc_008AB6FF:
    if ((*(unsigned __int64 *)(v_rbx + 192)) == (v_rdi + 1)) {
        result = PsGetCurrentSilo((unsigned int)(0x110000ULL), a2, (unsigned int)(0x6A536F49ULL), (unsigned int)(v_stack_p10));
        *(unsigned __int64 *)(v_rbx + 192) = result;
    }
    *(unsigned int *)(v_rbx + 16) = 0;
    *(unsigned __int64 *)(v_rbx + 8) = 0;
    v_stack_m90 = v_stack_m50;
    v_stack_m98 = *(unsigned __int64 *)(v_rbx + 192);
    v_stack_mA0 = v_rbx;
    v_stack_mA8 = (unsigned int)((unsigned int)(v_stack_p10));
    a4 = 0;
    result = ObOpenObjectByNameEx(0, *(unsigned __int64 *)(v_rip + 7451514), (unsigned __int8)((unsigned int)(v_stack_m70)), a4);
    v_stack_m88 = (unsigned int)(result);
    if (*(unsigned __int64 *)(v_rbx + 72) != 0) goto loc_008ABE8D;
loc_008AB782:
    if (v_stack_m6C != 0) goto loc_008ABF91;
    result = IopCleanupExtraCreateParameters(v_rbx, *(unsigned __int64 *)(v_rip + 7451514), (unsigned __int8)((unsigned int)(v_stack_m70)), a4);
loc_008AB794:
    v_stack_p70 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    if (sign_flag) goto loc_008AB8FC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)))) != 0xBEAA0251ULL) goto loc_008ABFA7;
    *(unsigned __int64 *)(v_stack_p8) = v_stack_m50;
    *(unsigned __int64 *)(v_stack_p20 + 8) = *(unsigned __int64 *)(v_rbx + 24);
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 16)));
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 16)));
    goto loc_008AB807;
loc_008AB807:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)))) != 0xBEAA0251ULL) goto loc_008AB84B;
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_008AB84B;
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_rbx + 8), *(unsigned __int64 *)(v_rip + 7451514), (unsigned __int8)((unsigned int)(v_stack_m70)), a4);
    goto loc_008AB84B;
loc_008AB820:
    result = FsRtlFreeExtraCreateParameterList(v_stack_m60, *(unsigned __int64 *)(v_rip + 7451514), (unsigned __int8)((unsigned int)(v_stack_m70)), a4);
    *(unsigned __int64 *)(v_rbx + 168) = 0;
loc_008AB831:
    if ((unsigned int)((unsigned int)(result)) != 0) goto loc_008ABF6B;
loc_008AB83A:
    if (*(unsigned __int64 *)(v_rbx + 72) != 0) goto loc_008ABF78;
loc_008AB847:
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
loc_008AB84B:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 16)))) goto loc_008AB979;
loc_008AB86B:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176), v_rbx, (unsigned __int8)((unsigned int)(v_stack_m70)), a4);
loc_008AB873:
loc_008AB877:
    v_rsp = (v_rsp) + (144);
    return (unsigned int)(v_stack_m88);
loc_008AB88B:
    v_r13 = (unsigned int)(v_stack_m70);
    if (!sign_flag) { v_r13 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m70)))); }
    a2 = (unsigned int)(v_stack_p84);
    if (!sign_flag) { a2 = v_stack_p84; }
    v_stack_p138 = a2;
    if (v_stack_p20 != 0) goto loc_008ABEF9;
loc_008AB8BE:
    if (condition_is_below) goto loc_008ABF10;
    *(unsigned __int64 *)(v_rbx + 216) = 0;
    v_stack_p60 = a10;
    v_stack_p48 = (unsigned int)((unsigned int)(a11));
loc_008AB8EA:
    *(unsigned __int64 *)(v_rbx + 72) = 0;
    goto loc_008AB4E8;
loc_008AB8FC:
    if (sign_flag) goto loc_008AB9B7;
    if (*(unsigned __int64 *)(v_rbx + 8) != 0) goto loc_008ABFFD;
loc_008AB914:
    if (((unsigned int)((unsigned int)(a11))) != 0xC0000034ULL) goto loc_008AB807;
    if ((*(unsigned __int64 *)(v_rbx + 24)) != ((unsigned int)(0xA0000003ULL))) goto loc_008ABE99;
loc_008AB933:
    v_stack_p40 = 0xC0000280ULL;
    goto loc_008AB807;
loc_008AB940:
    a3 = (__int16)(*(unsigned __int16 *)(a2));
    if (((__int16)(*(unsigned __int16 *)(a2))) > (*(unsigned __int64 *)(v_rbx + 24))) { a3 = *(unsigned __int64 *)(v_rbx + 24); }
    result = memcpy((unsigned int)(0xA0000003ULL), a2, a3, a4);
    goto loc_008AB5B7;
loc_008AB955:
    result = (unsigned int)(((unsigned int)(a8)) - 1);
    if (((unsigned int)(result)) <= 2) goto loc_008AB6A1;
loc_008AB979:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2184))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2184) + 16)))) goto loc_008AB86B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2184) + 56)) != (v_rip + 2977455)) goto loc_008ABF5E;
    result = ExFreePool(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2184) + 56), a3, a4);
    goto loc_008AB873;
loc_008AB9B7:
    v_stack_p40 = (unsigned int)(v_rbx);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == 0x80000000ULL) goto loc_008ABFCD;
    if (((unsigned int)(v_rbx)) != 0xC0000279ULL) goto loc_008AB914;
    goto loc_008ABFCD;
loc_008AB9E1:
    if (0 != 0) goto loc_008AB6ED;
loc_008AB9EF:
    if (a10 == 0) goto loc_008ABA93;
    v_stack_p88 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) != 0) goto loc_008ABA63;
loc_008ABA21:
    if ((unsigned int)((unsigned int)(a11)) != 0) goto loc_008ABC00;
loc_008ABA30:
    if (((unsigned int)((unsigned int)(a11))) < 24) goto loc_008ABC24;
    *(unsigned __int64 *)(v_rbx + 216) = *(unsigned __int64 *)(a10);
    v_stack_p60 = *(unsigned __int64 *)(a10 + 8);
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(a10 + 16)));
    if (((unsigned int)((unsigned int)(a11))) >= 32) goto loc_008ABCA3;
    goto loc_008ABCDB;
loc_008ABA63:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a10) + 1772))) != 332) goto loc_008ABA84;
loc_008ABA74:
loc_008ABA77:
    v_stack_p4C = (unsigned __int8)((unsigned __int8)(v_rdi + 1));
    if ((unsigned __int8)((unsigned __int8)(v_rdi + 1)) == 0) goto loc_008ABA21;
    goto loc_008ABB12;
loc_008ABA84:
    if (((unsigned __int16)((unsigned __int8)(v_rdi + 1))) != 452) goto loc_008ABA77;
    goto loc_008ABA74;
loc_008ABA93:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 28))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 28) = (unsigned int)(result);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 16)))) goto loc_008ABB00;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 32))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 32) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 28))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 28) = (unsigned int)(result);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 16)))) goto loc_008ABB00;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 32))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 32) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56)) != (v_rip + 2977129)) goto loc_008ABAF6;
    result = ExFreePool(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56), a3, a4);
    goto loc_008ABB08;
loc_008ABAF6:
    result = guard_dispatch_icall(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56), a3, a4);
    goto loc_008ABB08;
loc_008ABB00:
    result = ExpInterlockedPushEntrySList(v_rbx, v_rbx, a3, a4);
loc_008ABB08:
    goto loc_008AB877;
loc_008ABB12:
    if ((unsigned int)((unsigned int)(a11)) == 0) goto loc_008ABB38;
    result = (unsigned int)(0xC000000DULL);
    if (((0) & ((unsigned __int8)(v_rbx))) != 0) {
        result = ExRaiseDatatypeMisalignment(v_rbx, (unsigned int)(a11), a3, a4);
    }
    if ((v_rbx + (unsigned int)(a11) * 1) > v_r10) goto loc_008ABB35;
    if ((v_rbx + (unsigned int)(a11) * 1) < v_rbx) {
        result = *(unsigned __int8 *)(v_r10);
    }
    if (((unsigned int)((unsigned int)(a11))) >= 16) goto loc_008ABBBC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 28))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 28) = (unsigned int)(result);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 16)))) goto loc_008ABBAA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 32))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 32) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 28))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 28) = (unsigned int)(result);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 16)))) goto loc_008ABBAA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 32))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 32) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56)) != (v_rip + 2976959)) goto loc_008ABBA0;
    result = ExFreePool(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56), v_rbx + (unsigned int)(a11) * 1, a4);
    goto loc_008ABBB2;
loc_008ABBA0:
    result = guard_dispatch_icall(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56), v_rbx + (unsigned int)(a11) * 1, a4);
    goto loc_008ABBB2;
loc_008ABBAA:
    result = ExpInterlockedPushEntrySList(v_rbx, v_rbx, v_rbx + (unsigned int)(a11) * 1, a4);
loc_008ABBB2:
    goto loc_008AB877;
loc_008ABBBC:
    *(unsigned __int64 *)(v_rbx + 216) = *(unsigned __int64 *)(v_rbx);
    v_stack_p60 = (unsigned int)(*(unsigned int *)(v_rbx + 8));
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 12)));
    if (((unsigned int)(v_rbx)) < 24) goto loc_008ABCDB;
    v_stack_p70 = (unsigned int)(*(unsigned int *)(v_rbx + 16));
    if ((unsigned int)(*(unsigned int *)(v_rbx + 16)) == 0) goto loc_008ABCDB;
    if (((0) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 16))))) == 0) goto loc_008ABCBB;
    result = ExRaiseDatatypeMisalignment(v_rbx, v_rbx, v_rbx + (unsigned int)(a11) * 1, a4);
loc_008ABC00:
    if (((0) & ((unsigned __int8)(v_rbx))) != 0) {
        result = ExRaiseDatatypeMisalignment(v_rbx, v_rbx, v_rbx + (unsigned int)(a11) * 1, a4);
    }
    if ((v_rbx + v_rbx * 1) > v_r10) goto loc_008ABC1C;
    if ((v_rbx + v_rbx * 1) >= v_rbx) goto loc_008ABA30;
loc_008ABC1C:
    goto loc_008ABA30;
loc_008ABC24:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 28))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 28) = (unsigned int)(result);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 16)))) goto loc_008ABC91;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 32))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 32) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 28))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 28) = (unsigned int)(result);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 16)))) goto loc_008ABC91;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 32))) + ((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 32) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56)) != (v_rip + 2976728)) goto loc_008ABC87;
    result = ExFreePool(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56), v_rbx + v_rbx * 1, a4);
    goto loc_008ABC99;
loc_008ABC87:
    result = guard_dispatch_icall(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56), v_rbx + v_rbx * 1, a4);
    goto loc_008ABC99;
loc_008ABC91:
    result = ExpInterlockedPushEntrySList(v_rbx, v_rbx, v_rbx + v_rbx * 1, a4);
loc_008ABC99:
    goto loc_008AB877;
loc_008ABCA3:
    v_stack_p70 = *(unsigned __int64 *)(v_rbx + 24);
    if (*(unsigned __int64 *)(v_rbx + 24) == 0) goto loc_008ABCDB;
    result = *(unsigned __int64 *)(v_rbx + 24);
    if (((0) & ((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 24)))) != 0) {
        result = ExRaiseDatatypeMisalignment(v_rbx, v_rbx, v_rbx + v_rbx * 1, a4);
    }
    if ((v_stack_p70 + 32) > v_r10) goto loc_008ABCCE;
    result = v_stack_p70;
    v_r14 = (unsigned int)(*(unsigned int *)(v_rbx + 8));
    v_r15 = (unsigned int)(*(unsigned int *)(v_rbx + 12));
    if ((v_stack_p70 + 32) < v_stack_p70) {
        result = *(unsigned __int8 *)(v_r10);
        v_r15 = v_stack_p48;
        v_r14 = v_stack_p60;
    }
    goto loc_008AB4D4;
loc_008ABD56:
    if ((unsigned int)(v_r15) == 0) goto loc_008AB4E1;
    v_stack_p44 = 0;
    if (((0) & ((unsigned __int8)(v_r14))) != 0) goto loc_008ABDD4;
    if (((unsigned int)((unsigned int)(v_r15)) + v_r14 * 1) > v_r10) goto loc_008ABDD9;
    if (((unsigned int)((unsigned int)(v_r15)) + v_r14 * 1) < v_r14) goto loc_008ABDD9;
loc_008ABD7A:
    result = ExAllocatePool2(99, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x61456F49ULL), a4);
    *(unsigned __int64 *)(v_rbx + 72) = result;
    *(unsigned int *)(v_rbx + 80) = (unsigned int)(v_r15);
    result = memcpy(result, v_r14, (unsigned int)((unsigned int)(v_r15)), a4);
    result = IoCheckEaBufferValidity(*(unsigned __int64 *)(v_rbx + 72), (unsigned int)((unsigned int)(v_r15)), v_stack_pE8 + 8, a4);
    v_stack_p40 = (unsigned int)(result);
    if (!sign_flag) goto loc_008ABDE8;
    v_stack_p44 = (unsigned __int8)(v_rdi + 1);
    *(unsigned int *)(v_stack_pE8) = (unsigned int)(result);
    result = RtlRaiseStatus((unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r15)), v_stack_pE8 + 8, a4);
loc_008ABDD4:
    result = ExRaiseDatatypeMisalignment((unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r15)), v_stack_pE8 + 8, a4);
loc_008ABDD9:
    goto loc_008ABD7A;
loc_008ABDE8:
    goto loc_008AB4F3;
loc_008ABE8D:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(result)), a2, v_stack_pE8 + 8, a4);
    goto loc_008AB782;
loc_008ABE99:
    if (result == ((unsigned int)(0xA000000CULL))) goto loc_008AB933;
    if (result != ((unsigned int)(0xA0000019ULL))) goto loc_008AB807;
    goto loc_008AB933;
loc_008ABEC3:
    if (v_stack_p5C != 0) goto loc_008AB820;
    result = IopCleanupExtraCreateParameters(v_rbx, a2, v_stack_pE8 + 8, a4);
    goto loc_008AB831;
loc_008ABEDA:
    goto loc_008AB68A;
loc_008ABEEA:
    goto loc_008AB6E1;
loc_008ABEF9:
    v_stack_p78 = *(unsigned __int64 *)(v_stack_pE8);
    goto loc_008AB8BE;
loc_008ABF10:
    *(unsigned __int64 *)(v_rbx + 216) = *(unsigned __int64 *)(a10);
    v_stack_p60 = *(unsigned __int64 *)(a10 + 8);
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(a10 + 16)));
    if (a11 < 32) goto loc_008AB8EA;
    v_stack_p70 = *(unsigned __int64 *)(a10 + 24);
    goto loc_008AB8EA;
loc_008ABF5E:
    result = guard_dispatch_icall(a10, a2, v_stack_pE8 + 8, a4);
    goto loc_008AB873;
loc_008ABF6B:
    result = FsRtlFreeExtraCreateParameter((unsigned int)(*(unsigned int *)(a10 + 16)), a2, v_stack_pE8 + 8, a4);
    goto loc_008AB83A;
loc_008ABF78:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(*(unsigned int *)(a10 + 16)), a2, v_stack_pE8 + 8, a4);
    goto loc_008AB847;
loc_008ABF91:
    result = FsRtlFreeExtraCreateParameterList(v_stack_p68, a2, v_stack_pE8 + 8, a4);
    *(unsigned __int64 *)(v_rbx + 168) = 0;
    goto loc_008AB794;
loc_008ABFA7:
    if (sign_flag) goto loc_008AB8FC;
    result = ObCloseHandle(v_stack_p78, (unsigned __int8)(v_r13), v_stack_pE8 + 8, a4);
    v_stack_p40 = (unsigned int)((unsigned int)(0xC0000024ULL));
    goto loc_008AB8FC;
loc_008ABFCD:
    *(unsigned int *)(v_stack_pE8) = (unsigned int)(v_stack_p78);
    *(unsigned __int64 *)(v_stack_pE8 + 8) = *(unsigned __int64 *)(v_rbx + 24);
    goto loc_008AB914;
loc_008ABFFD:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p78 + 96), a2, v_stack_pE8 + 8, a4);
loc_008AC025:
    goto loc_008AB877;
}
```

## 5. (Beta) C Style

```c
int64_t IopCreateFile(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint16_t Arg6, uint16_t Arg7, uint32_t Arg8, uint32_t Arg9, void *Arg10, uint32_t Arg11, uint32_t Arg12, int64_t Arg13, uint32_t Arg14, uint32_t Arg15, int64_t Arg16)
{
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m44;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p138;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p40;
    uint8_t v_stack_p44;
    uint32_t v_stack_p48;
    uint8_t v_stack_p4C;
    uint64_t v_stack_p50;
    uint32_t v_stack_p5C;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint32_t v_stack_p84;
    uint64_t v_stack_p88;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    v_stack_m44 = (uint32_t)((uint32_t)(Arg14));
    local_rdi = 0;
    v_stack_m88 = 0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x60) = 0;
    *(uint32_t *)(local_rsp - 0x80) = 0;
    v_stack_m6C = 0;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    Arg1 = 0;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)); }
    v_stack_m70 = (uint32_t)(Arg1);
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880), Arg2, Arg3, Arg4);
    v_stack_m78 = result;
    if (result != 0) goto loc_008AB385;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888), Arg2, Arg3, Arg4);
    v_stack_m78 = result;
    local_rbx = result;
    if (result == 0) {
        Arg2 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x2C);
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x30);
        Arg3 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x28);
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x24);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        local_rbx = result;
        v_stack_m78 = result;
    }
    if (local_rbx == 0) goto loc_008AC025;
    *(uint32_t *)(local_rbx) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)));
    if ((uint8_t)((uint32_t)(v_stack_m70)) != 0) goto loc_008AB61F;
    if (((Arg14) & (512)) != 0) goto loc_008AB61F;
loc_008AB3B3:
    if ((uint8_t)((uint32_t)(v_stack_m70)) == 0) goto loc_008AB88B;
    Arg1 = local_r10;
    if (v_stack_p8 < local_r10) { Arg1 = v_stack_p8; }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    Arg1 = local_r10;
    if (v_stack_p20 < local_r10) { Arg1 = v_stack_p20; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if (Arg5 != 0) goto loc_008AB417;
    v_stack_m50 = 0;
loc_008AB408:
    if (!sign_flag) goto loc_008AB43A;
    result = RtlRaiseStatus((uint32_t)(0xC000000DULL), Arg2, (uint32_t)(v_stack_m70), 3);
loc_008AB417:
    if (((3) & ((uint8_t)(Arg5))) != 0) {
        result = ExRaiseDatatypeMisalignment((uint32_t)(0xC000000DULL), Arg2, (uint32_t)(v_stack_m70), 3);
    }
    result = local_r10;
    if (Arg5 < local_r10) { result = Arg5; }
    v_stack_m50 = *(uint64_t *)(Arg5);
    goto loc_008AB408;
loc_008AB43A:
    goto loc_008AB4A8;
loc_008AB4A8:
    if (Arg5 < local_r10) goto loc_008AB9EF;
    *(uint64_t *)(local_rbx + 0xD8) = 0;
    v_stack_m68 = Arg10;
    v_stack_m80 = (uint32_t)((uint32_t)(Arg11));
loc_008AB4D4:
    *(uint64_t *)(local_rbx + 0x48) = 0;
    if (Arg10 != NULL) goto loc_008ABD56;
loc_008AB4E1:
loc_008AB4E8:
    *(uint32_t *)(local_rbx + 0x50) = 0;
loc_008AB4F3:
    *(uint32_t *)(local_rbx) = 0xE00008ULL;
    *(uint32_t *)(local_rbx + 0x20) = 0;
    *(uint64_t *)(local_rbx + 0x18) = 0;
    *(uint64_t *)(local_rbx + 0x38) = v_stack_m50;
    local_r13 = (uint32_t)(((uint32_t)(Arg9)) & (0xFFFFFFULL));
    *(uint32_t *)(local_rbx + 0x40) = (uint32_t)(local_r13);
    *(uint16_t *)(local_rbx + 0x44) = Arg6;
    *(uint16_t *)(local_rbx + 0x46) = Arg7;
    *(uint32_t *)(local_rbx + 0x58) = (uint32_t)((uint32_t)(Arg8));
    *(uint16_t *)(local_rbx + 0x88) = 0;
    *(uint8_t *)(local_rbx + 0x8A) = 0;
    *(uint32_t *)(local_rbx + 0x54) = (uint32_t)((uint32_t)(Arg14));
    *(uint64_t *)(local_rbx + 0x28) = 0;
    *(uint64_t *)(local_rbx + 0x30) = v_stack_p18;
    *(uint32_t *)(local_rbx + 0x78) = (uint32_t)((uint32_t)(Arg12));
    *(uint64_t *)(local_rbx + 0x80) = Arg13;
    *(uint32_t *)(local_rbx + 0x98) = (uint32_t)((uint32_t)(Arg15));
    *(uint8_t *)(local_rbx + 0x9C) = (uint8_t)((uint32_t)(v_stack_m70));
    *(uint64_t *)(local_rbx + 0xA0) = v_xmm0;
    *(uint64_t *)(local_rbx + 0xA0 + 0x10) = v_xmm0;
    *(uint16_t *)(local_rbx + 0xA0) = 40;
    *(uint64_t *)(local_rbx + 0xA0 + 0x20) = local_rdi + 1;
    if (Arg16 != 0) goto loc_008AB940;
loc_008AB5B7:
    if (v_stack_m58 == 0) goto loc_008AB6FF;
    v_stack_m60 = *(uint64_t *)(local_rbx + 0xA8);
    result = ExAllocatePool2(256, 108, (uint32_t)(0x6A536F49ULL), 3);
    v_stack_m88 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_008ABEC3;
loc_008AB61F:
    Arg1 = (((Arg7) & (0xFFFFFFF8ULL)) == 0) ? 1 : 0;
    result = (((Arg6) & (0xFFA50048ULL)) == 0) ? 1 : 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m70)))) & (48));
    Arg1 = (condition_is_not_equal) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if (condition_is_below) goto loc_008ABEDA;
loc_008AB68A:
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m70)))) & (65));
    if (((uint8_t)(result)) == ((uint8_t)(local_rdi + 1))) goto loc_008AB955;
loc_008AB6A1:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m70)))) & ((uint32_t)((uint32_t)(0x100100ULL))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m70)))) & ((uint32_t)((uint32_t)(0x10100ULL))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m70)))) & ((uint32_t)((uint32_t)(0x110000ULL))));
    if ((((uint8_t)((uint32_t)(v_stack_m70))) & (8)) != 0) goto loc_008ABEEA;
loc_008AB6E1:
    if ((*(uint32_t *)(v_rip + 0x55F2E1)) != 0) goto loc_008AB9E1;
loc_008AB6ED:
    if (Arg12 == 0) goto loc_008AB3B3;
loc_008AB6FF:
    if ((*(uint64_t *)(local_rbx + 0xC0)) == (local_rdi + 1)) {
        result = PsGetCurrentSilo((uint32_t)(0x110000ULL), Arg2, (uint32_t)(0x6A536F49ULL), (uint32_t)(v_stack_p10));
        *(uint64_t *)(local_rbx + 0xC0) = result;
    }
    *(uint32_t *)(local_rbx + 0x10) = 0;
    *(uint64_t *)(local_rbx + 0x8) = 0;
    v_stack_m90 = v_stack_m50;
    v_stack_m98 = *(uint64_t *)(local_rbx + 0xC0);
    v_stack_mA0 = local_rbx;
    v_stack_mA8 = (uint32_t)((uint32_t)(v_stack_p10));
    Arg4 = 0;
    result = ObOpenObjectByNameEx(0, *(uint64_t *)(v_rip + 0x71B37A), (uint8_t)((uint32_t)(v_stack_m70)), Arg4);
    v_stack_m88 = (uint32_t)(result);
    if (*(uint64_t *)(local_rbx + 0x48) != 0) goto loc_008ABE8D;
loc_008AB782:
    if (v_stack_m6C != 0) goto loc_008ABF91;
    result = IopCleanupExtraCreateParameters(local_rbx, *(uint64_t *)(v_rip + 0x71B37A), (uint8_t)((uint32_t)(v_stack_m70)), Arg4);
loc_008AB794:
    v_stack_p70 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    if (sign_flag) goto loc_008AB8FC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)))) != 0xBEAA0251ULL) goto loc_008ABFA7;
    *(uint64_t *)(v_stack_p8) = v_stack_m50;
    *(uint64_t *)(v_stack_p20 + 0x8) = *(uint64_t *)(local_rbx + 0x18);
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x10)));
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x10)));
    goto loc_008AB807;
loc_008AB807:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)))) != 0xBEAA0251ULL) goto loc_008AB84B;
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_008AB84B;
    result = ObfDereferenceObject(*(uint64_t *)(local_rbx + 0x8), *(uint64_t *)(v_rip + 0x71B37A), (uint8_t)((uint32_t)(v_stack_m70)), Arg4);
    goto loc_008AB84B;
loc_008AB820:
    result = FsRtlFreeExtraCreateParameterList(v_stack_m60, *(uint64_t *)(v_rip + 0x71B37A), (uint8_t)((uint32_t)(v_stack_m70)), Arg4);
    *(uint64_t *)(local_rbx + 0xA8) = 0;
loc_008AB831:
    if ((uint32_t)((uint32_t)(result)) != 0) goto loc_008ABF6B;
loc_008AB83A:
    if (*(uint64_t *)(local_rbx + 0x48) != 0) goto loc_008ABF78;
loc_008AB847:
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
loc_008AB84B:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x10)))) goto loc_008AB979;
loc_008AB86B:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880), local_rbx, (uint8_t)((uint32_t)(v_stack_m70)), Arg4);
loc_008AB873:
loc_008AB877:
    local_rsp = (local_rsp) + (144);
    return (uint32_t)(v_stack_m88);
loc_008AB88B:
    local_r13 = (uint32_t)(v_stack_m70);
    if (!sign_flag) { local_r13 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m70)))); }
    Arg2 = (uint32_t)(v_stack_p84);
    if (!sign_flag) { Arg2 = v_stack_p84; }
    v_stack_p138 = Arg2;
    if (v_stack_p20 != 0) goto loc_008ABEF9;
loc_008AB8BE:
    if (condition_is_below) goto loc_008ABF10;
    *(uint64_t *)(local_rbx + 0xD8) = 0;
    v_stack_p60 = Arg10;
    v_stack_p48 = (uint32_t)((uint32_t)(Arg11));
loc_008AB8EA:
    *(uint64_t *)(local_rbx + 0x48) = 0;
    goto loc_008AB4E8;
loc_008AB8FC:
    if (sign_flag) goto loc_008AB9B7;
    if (*(uint64_t *)(local_rbx + 0x8) != 0) goto loc_008ABFFD;
loc_008AB914:
    if (((uint32_t)((uint32_t)(Arg11))) != 0xC0000034ULL) goto loc_008AB807;
    if ((*(uint64_t *)(local_rbx + 0x18)) != ((uint32_t)(0xA0000003ULL))) goto loc_008ABE99;
loc_008AB933:
    v_stack_p40 = 0xC0000280ULL;
    goto loc_008AB807;
loc_008AB940:
    Arg3 = (int16_t)(*(uint16_t *)(Arg2));
    if (((int16_t)(*(uint16_t *)(Arg2))) > (*(uint64_t *)(local_rbx + 0x18))) { Arg3 = *(uint64_t *)(local_rbx + 0x18); }
    result = memcpy((uint32_t)(0xA0000003ULL), Arg2, Arg3, Arg4);
    goto loc_008AB5B7;
loc_008AB955:
    result = (uint32_t)(((uint32_t)(Arg8)) - 1);
    if (((uint32_t)(result)) <= 2) goto loc_008AB6A1;
loc_008AB979:
    if ((*(uint16_t *)(*(uint64_t *)(Arg2 + 0x888))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg2 + 0x888) + 0x10)))) goto loc_008AB86B;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x888) + 0x38)) != (v_rip + 2977455)) goto loc_008ABF5E;
    result = ExFreePool(local_rbx, *(uint64_t *)(*(uint64_t *)(Arg2 + 0x888) + 0x38), Arg3, Arg4);
    goto loc_008AB873;
loc_008AB9B7:
    v_stack_p40 = (uint32_t)(local_rbx);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == 0x80000000ULL) goto loc_008ABFCD;
    if (((uint32_t)(local_rbx)) != 0xC0000279ULL) goto loc_008AB914;
    goto loc_008ABFCD;
loc_008AB9E1:
    if (0 != 0) goto loc_008AB6ED;
loc_008AB9EF:
    if (Arg10 == NULL) goto loc_008ABA93;
    v_stack_p88 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) != 0) goto loc_008ABA63;
loc_008ABA21:
    if ((uint32_t)((uint32_t)(Arg11)) != 0) goto loc_008ABC00;
loc_008ABA30:
    if (((uint32_t)((uint32_t)(Arg11))) < 24) goto loc_008ABC24;
    *(uint64_t *)(local_rbx + 0xD8) = *(uint64_t *)(arg10);
    v_stack_p60 = *(uint64_t *)(arg10 + 0x8);
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x10)));
    if (((uint32_t)((uint32_t)(Arg11))) >= 32) goto loc_008ABCA3;
    goto loc_008ABCDB;
loc_008ABA63:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg10) + 0x6EC))) != 332) goto loc_008ABA84;
loc_008ABA74:
loc_008ABA77:
    v_stack_p4C = (uint8_t)((uint8_t)(local_rdi + 1));
    if ((uint8_t)((uint8_t)(local_rdi + 1)) == 0) goto loc_008ABA21;
    goto loc_008ABB12;
loc_008ABA84:
    if (((uint16_t)((uint8_t)(local_rdi + 1))) != 452) goto loc_008ABA77;
    goto loc_008ABA74;
loc_008ABA93:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x1C))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x1C) = (uint32_t)(result);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x10)))) goto loc_008ABB00;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x20))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x20) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x1C))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x1C) = (uint32_t)(result);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x10)))) goto loc_008ABB00;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x20))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x20) = (uint32_t)(result);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38)) != (v_rip + 2977129)) goto loc_008ABAF6;
    result = ExFreePool(local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38), Arg3, Arg4);
    goto loc_008ABB08;
loc_008ABAF6:
    result = guard_dispatch_icall(local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38), Arg3, Arg4);
    goto loc_008ABB08;
loc_008ABB00:
    result = ExpInterlockedPushEntrySList(local_rbx, local_rbx, Arg3, Arg4);
loc_008ABB08:
    goto loc_008AB877;
loc_008ABB12:
    if ((uint32_t)((uint32_t)(Arg11)) == 0) goto loc_008ABB38;
    result = (uint32_t)(0xC000000DULL);
    if (((0) & ((uint8_t)(local_rbx))) != 0) {
        result = ExRaiseDatatypeMisalignment(local_rbx, (uint32_t)(Arg11), Arg3, Arg4);
    }
    if ((local_rbx + (uint32_t)(Arg11) * 1) > local_r10) goto loc_008ABB35;
    if ((local_rbx + (uint32_t)(Arg11) * 1) < local_rbx) {
        result = *(uint8_t *)(local_r10);
    }
    if (((uint32_t)((uint32_t)(Arg11))) >= 16) goto loc_008ABBBC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x1C))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x1C) = (uint32_t)(result);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x10)))) goto loc_008ABBAA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x20))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x20) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x1C))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x1C) = (uint32_t)(result);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x10)))) goto loc_008ABBAA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x20))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x20) = (uint32_t)(result);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38)) != (v_rip + 2976959)) goto loc_008ABBA0;
    result = ExFreePool(local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38), local_rbx + (uint32_t)(Arg11) * 1, Arg4);
    goto loc_008ABBB2;
loc_008ABBA0:
    result = guard_dispatch_icall(local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38), local_rbx + (uint32_t)(Arg11) * 1, Arg4);
    goto loc_008ABBB2;
loc_008ABBAA:
    result = ExpInterlockedPushEntrySList(local_rbx, local_rbx, local_rbx + (uint32_t)(Arg11) * 1, Arg4);
loc_008ABBB2:
    goto loc_008AB877;
loc_008ABBBC:
    *(uint64_t *)(local_rbx + 0xD8) = *(uint64_t *)(local_rbx);
    v_stack_p60 = (uint32_t)(*(uint32_t *)(local_rbx + 0x8));
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xC)));
    if (((uint32_t)(local_rbx)) < 24) goto loc_008ABCDB;
    v_stack_p70 = (uint32_t)(*(uint32_t *)(local_rbx + 0x10));
    if ((uint32_t)(*(uint32_t *)(local_rbx + 0x10)) == 0) goto loc_008ABCDB;
    if (((0) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x10))))) == 0) goto loc_008ABCBB;
    result = ExRaiseDatatypeMisalignment(local_rbx, local_rbx, local_rbx + (uint32_t)(Arg11) * 1, Arg4);
loc_008ABC00:
    if (((0) & ((uint8_t)(local_rbx))) != 0) {
        result = ExRaiseDatatypeMisalignment(local_rbx, local_rbx, local_rbx + (uint32_t)(Arg11) * 1, Arg4);
    }
    if ((local_rbx + local_rbx * 1) > local_r10) goto loc_008ABC1C;
    if ((local_rbx + local_rbx * 1) >= local_rbx) goto loc_008ABA30;
loc_008ABC1C:
    goto loc_008ABA30;
loc_008ABC24:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x1C))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x1C) = (uint32_t)(result);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x10)))) goto loc_008ABC91;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x20))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x20) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x1C))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x1C) = (uint32_t)(result);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x10)))) goto loc_008ABC91;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x20))) + ((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x20) = (uint32_t)(result);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38)) != (v_rip + 2976728)) goto loc_008ABC87;
    result = ExFreePool(local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38), local_rbx + local_rbx * 1, Arg4);
    goto loc_008ABC99;
loc_008ABC87:
    result = guard_dispatch_icall(local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38), local_rbx + local_rbx * 1, Arg4);
    goto loc_008ABC99;
loc_008ABC91:
    result = ExpInterlockedPushEntrySList(local_rbx, local_rbx, local_rbx + local_rbx * 1, Arg4);
loc_008ABC99:
    goto loc_008AB877;
loc_008ABCA3:
    v_stack_p70 = *(uint64_t *)(local_rbx + 0x18);
    if (*(uint64_t *)(local_rbx + 0x18) == 0) goto loc_008ABCDB;
    result = *(uint64_t *)(local_rbx + 0x18);
    if (((0) & ((uint8_t)(*(uint64_t *)(local_rbx + 0x18)))) != 0) {
        result = ExRaiseDatatypeMisalignment(local_rbx, local_rbx, local_rbx + local_rbx * 1, Arg4);
    }
    if ((v_stack_p70 + 32) > local_r10) goto loc_008ABCCE;
    result = v_stack_p70;
    local_r14 = (uint32_t)(*(uint32_t *)(local_rbx + 0x8));
    local_r15 = (uint32_t)(*(uint32_t *)(local_rbx + 0xC));
    if ((v_stack_p70 + 32) < v_stack_p70) {
        result = *(uint8_t *)(local_r10);
        local_r15 = v_stack_p48;
        local_r14 = v_stack_p60;
    }
    goto loc_008AB4D4;
loc_008ABD56:
    if ((uint32_t)(local_r15) == 0) goto loc_008AB4E1;
    v_stack_p44 = 0;
    if (((0) & ((uint8_t)(local_r14))) != 0) goto loc_008ABDD4;
    if (((uint32_t)((uint32_t)(local_r15)) + local_r14 * 1) > local_r10) goto loc_008ABDD9;
    if (((uint32_t)((uint32_t)(local_r15)) + local_r14 * 1) < local_r14) goto loc_008ABDD9;
loc_008ABD7A:
    result = ExAllocatePool2(99, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x61456F49ULL), Arg4);
    *(uint64_t *)(local_rbx + 0x48) = result;
    *(uint32_t *)(local_rbx + 0x50) = (uint32_t)(local_r15);
    result = memcpy(result, local_r14, (uint32_t)((uint32_t)(local_r15)), Arg4);
    result = IoCheckEaBufferValidity(*(uint64_t *)(local_rbx + 0x48), (uint32_t)((uint32_t)(local_r15)), v_stack_pE8 + 8, Arg4);
    v_stack_p40 = (uint32_t)(result);
    if (!sign_flag) goto loc_008ABDE8;
    v_stack_p44 = (uint8_t)(local_rdi + 1);
    *(uint32_t *)(v_stack_pE8) = (uint32_t)(result);
    result = RtlRaiseStatus((uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r15)), v_stack_pE8 + 8, Arg4);
loc_008ABDD4:
    result = ExRaiseDatatypeMisalignment((uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r15)), v_stack_pE8 + 8, Arg4);
loc_008ABDD9:
    goto loc_008ABD7A;
loc_008ABDE8:
    goto loc_008AB4F3;
loc_008ABE8D:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(result)), Arg2, v_stack_pE8 + 8, Arg4);
    goto loc_008AB782;
loc_008ABE99:
    if (result == ((uint32_t)(0xA000000CULL))) goto loc_008AB933;
    if (result != ((uint32_t)(0xA0000019ULL))) goto loc_008AB807;
    goto loc_008AB933;
loc_008ABEC3:
    if (v_stack_p5C != 0) goto loc_008AB820;
    result = IopCleanupExtraCreateParameters(local_rbx, Arg2, v_stack_pE8 + 8, Arg4);
    goto loc_008AB831;
loc_008ABEDA:
    goto loc_008AB68A;
loc_008ABEEA:
    goto loc_008AB6E1;
loc_008ABEF9:
    v_stack_p78 = *(uint64_t *)(v_stack_pE8);
    goto loc_008AB8BE;
loc_008ABF10:
    *(uint64_t *)(local_rbx + 0xD8) = *(uint64_t *)(arg10);
    v_stack_p60 = *(uint64_t *)(arg10 + 0x8);
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x10)));
    if (Arg11 < 32) goto loc_008AB8EA;
    v_stack_p70 = *(uint64_t *)(arg10 + 0x18);
    goto loc_008AB8EA;
loc_008ABF5E:
    result = guard_dispatch_icall(Arg10, Arg2, v_stack_pE8 + 8, Arg4);
    goto loc_008AB873;
loc_008ABF6B:
    result = FsRtlFreeExtraCreateParameter((uint32_t)(*(uint32_t *)(arg10 + 0x10)), Arg2, v_stack_pE8 + 8, Arg4);
    goto loc_008AB83A;
loc_008ABF78:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(*(uint32_t *)(arg10 + 0x10)), Arg2, v_stack_pE8 + 8, Arg4);
    goto loc_008AB847;
loc_008ABF91:
    result = FsRtlFreeExtraCreateParameterList(v_stack_p68, Arg2, v_stack_pE8 + 8, Arg4);
    *(uint64_t *)(local_rbx + 0xA8) = 0;
    goto loc_008AB794;
loc_008ABFA7:
    if (sign_flag) goto loc_008AB8FC;
    result = ObCloseHandle(v_stack_p78, (uint8_t)(local_r13), v_stack_pE8 + 8, Arg4);
    v_stack_p40 = (uint32_t)((uint32_t)(0xC0000024ULL));
    goto loc_008AB8FC;
loc_008ABFCD:
    *(uint32_t *)(v_stack_pE8) = (uint32_t)(v_stack_p78);
    *(uint64_t *)(v_stack_pE8 + 0x8) = *(uint64_t *)(local_rbx + 0x18);
    goto loc_008AB914;
loc_008ABFFD:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p78 + 0x60), Arg2, v_stack_pE8 + 8, Arg4);
loc_008AC025:
    goto loc_008AB877;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg10` | `+ 0x0` | `64` | `R` |
| `Arg10` | `+ 0x8` | `64` | `R` |
| `Arg10` | `+ 0x10` | `32` | `R` |
| `Arg10` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AB298&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
