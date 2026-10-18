# MiDeleteVad

- RVA: `0x00888C80`–`0x0088921C` (길이 `1,436` bytes)
- VA: `0x0000000140888C80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007CEA4`
- 디코드: `367`개 명령, `1,436/1,436` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00888D10` → [MiIsVadLargePrivate](../../text/32/MiIsVadLargePrivate_function_0032F720.md) (function, `0x0032F720`)
- `0x00888D78` → [MiSetVadDeleted](../../text/29/MiSetVadDeleted_function_00296E00.md) (function, `0x00296E00`)
- `0x00888DAD` → [MiIsVadLargePrivate](../../text/32/MiIsVadLargePrivate_function_0032F720.md) (function, `0x0032F720`)
- `0x00888DEB` → [MiDeleteVirtualAddresses](../../text/2A/MiDeleteVirtualAddresses_function_002A9640.md) (function, `0x002A9640`)
- `0x00888E57` → [MiGetProtoPteAddress](../../text/32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x00888E5F` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (function, `0x00452C1C`)
- `0x00888E81` → [MiGetProtoPteAddress](../../text/32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x00888E99` → [MiDrainSystemAccessLog](../../text/47/MiDrainSystemAccessLog_function_00474144.md) (function, `0x00474144`)
- `0x00888EDF` → [MiLockAddressSpaceToo](../../text/2A/MiLockAddressSpaceToo_function_002A5670.md) (function, `0x002A5670`)
- `0x00888EFD` → [MiRemoveVad](../../text/29/MiRemoveVad_function_00295C78.md) (function, `0x00295C78`)
- `0x00888F50` → [MiFinishVadDeletion](../../text/43/MiFinishVadDeletion_function_00430ED0.md) (function, `0x00430ED0`)
- `0x00888F88` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00888FB1` → [MiRemoveSharedCommitNode](MiRemoveSharedCommitNode_function_008889A0.md) (function, `0x008889A0`)
- `0x00888FC4` → [MiManageSubsectionView](../../text/2E/MiManageSubsectionView_function_002E2570.md) (function, `0x002E2570`)
- `0x00888FF6` → [MiUnmapViewSubsections](../../text/28/MiUnmapViewSubsections_function_00285E20.md) (function, `0x00285E20`)
- `0x00889056` → [MiGetProtoPteAddress](../../text/32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x00889073` → [MiGetProtoPteAddress](../../text/32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x00889098` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008890B7` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (function, `0x00452C1C`)
- `0x008890D1` → [MiControlAreaRequiresCharge](../../text/3B/MiControlAreaRequiresCharge_function_003B36CC.md) (function, `0x003B36CC`)
- `0x008890E4` → [MiReturnCrossPartitionControlAreaCharges](../../text/4D/MiReturnCrossPartitionControlAreaCharges_function_004D6184.md) (function, `0x004D6184`)
- `0x008890F1` → [MiDereferenceControlArea](../../text/47/MiDereferenceControlArea_function_00479A20.md) (function, `0x00479A20`)
- `0x00889143` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00889153` → [MiDereferenceExtendInfo](../../text/48/MiDereferenceExtendInfo_function_0048EFA4.md) (function, `0x0048EFA4`)
- `0x0088916D` → [MiDeleteEnclavePages](../../pagelk/B7/MiDeleteEnclavePages_function_00B7E228.md) (function, `0x00B7E228`)
- `0x0088917A` → [MiRemoveUserPhysicalPagesView](../../text/68/MiRemoveUserPhysicalPagesView_function_00689658.md) (function, `0x00689658`)
- `0x008891DF` → [MiReturnFullProcessCharges](../../text/2C/MiReturnFullProcessCharges_function_002C2E70.md) (function, `0x002C2E70`)
- `0x008891F8` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00889202` → [MiDereferencePerSessionProtos](../A2/MiDereferencePerSessionProtos_function_00A2EDE8.md) (function, `0x00A2EDE8`)
- `0x00889212` → [MiDecrementLargeSubsections](../../text/4D/MiDecrementLargeSubsections_function_004D2BE0.md) (function, `0x004D2BE0`)

### Direct callers
- [MiFreeVadRange](../../text/2A/MiFreeVadRange_function_002A77AC.md) at `0x002A785B`
- [MiDeletePartialVad](../../text/2A/MiDeletePartialVad_function_002A7A30.md) at `0x002A7B06`
- [MiCreateEnclave](../80/MiCreateEnclave_function_008083E4.md) at `0x008084CD`
- [MiDeleteInsertedCloneVads](../81/MiDeleteInsertedCloneVads_function_00811564.md) at `0x0081162D`
- [MiFreeToSubAllocatedRegion](../87/MiFreeToSubAllocatedRegion_function_0087FB7C.md) at `0x0087FCF4`
- [MiCoalescePlaceholderAllocations](MiCoalescePlaceholderAllocations_function_0088095C.md) at `0x00880AF0`
- [MiReserveUserMemory](MiReserveUserMemory_function_00884498.md) at `0x00884B37`
- [MiReserveUserMemory](MiReserveUserMemory_function_00884498.md) at `0x00884B89`
- [sub_00885634](Unknown_function_00885634.md) at `0x0088579F`
- [MiCleanVad](MiCleanVad_function_00889224.md) at `0x0088925D`
- [MiUnmapVad](MiUnmapVad_function_00889280.md) at `0x008892C4`
- [MiUnmapViewOfSection](MiUnmapViewOfSection_function_0088A4C4.md) at `0x0088A7B4`
- [MiMapViewOfPhysicalSection](../97/MiMapViewOfPhysicalSection_function_0097F984.md) at `0x0097FC85`
- [MiMapLockedPagesInUserSpace](../97/MiMapLockedPagesInUserSpace_function_0097FE04.md) at `0x00980221`
- [MiUnmapLockedPagesInUserSpace](../A7/MiUnmapLockedPagesInUserSpace_function_00A78E54.md) at `0x00A78F47`
- [MiFinishPlaceholderVadReplacement](../A8/MiFinishPlaceholderVadReplacement_function_00A87630.md) at `0x00A8766E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **28**
  - `0x00888D10` → [MiIsVadLargePrivate](../../text/32/MiIsVadLargePrivate_function_0032F720.md) (`PAGE` → `.text`)
  - `0x00888D78` → [MiSetVadDeleted](../../text/29/MiSetVadDeleted_function_00296E00.md) (`PAGE` → `.text`)
  - `0x00888DAD` → [MiIsVadLargePrivate](../../text/32/MiIsVadLargePrivate_function_0032F720.md) (`PAGE` → `.text`)
  - `0x00888DEB` → [MiDeleteVirtualAddresses](../../text/2A/MiDeleteVirtualAddresses_function_002A9640.md) (`PAGE` → `.text`)
  - `0x00888E57` → [MiGetProtoPteAddress](../../text/32/MiGetProtoPteAddress_function_0032E970.md) (`PAGE` → `.text`)
  - `0x00888E5F` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (`PAGE` → `.text`)
  - `0x00888E81` → [MiGetProtoPteAddress](../../text/32/MiGetProtoPteAddress_function_0032E970.md) (`PAGE` → `.text`)
  - `0x00888E99` → [MiDrainSystemAccessLog](../../text/47/MiDrainSystemAccessLog_function_00474144.md) (`PAGE` → `.text`)
  - `0x00888EDF` → [MiLockAddressSpaceToo](../../text/2A/MiLockAddressSpaceToo_function_002A5670.md) (`PAGE` → `.text`)
  - `0x00888EFD` → [MiRemoveVad](../../text/29/MiRemoveVad_function_00295C78.md) (`PAGE` → `.text`)
  - `0x00888F50` → [MiFinishVadDeletion](../../text/43/MiFinishVadDeletion_function_00430ED0.md) (`PAGE` → `.text`)
  - `0x00888F88` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00888FC4` → [MiManageSubsectionView](../../text/2E/MiManageSubsectionView_function_002E2570.md) (`PAGE` → `.text`)
  - `0x00888FF6` → [MiUnmapViewSubsections](../../text/28/MiUnmapViewSubsections_function_00285E20.md) (`PAGE` → `.text`)
  - `0x00889056` → [MiGetProtoPteAddress](../../text/32/MiGetProtoPteAddress_function_0032E970.md) (`PAGE` → `.text`)
  - `0x00889073` → [MiGetProtoPteAddress](../../text/32/MiGetProtoPteAddress_function_0032E970.md) (`PAGE` → `.text`)
  - `0x00889098` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008890B7` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (`PAGE` → `.text`)
  - `0x008890D1` → [MiControlAreaRequiresCharge](../../text/3B/MiControlAreaRequiresCharge_function_003B36CC.md) (`PAGE` → `.text`)
  - `0x008890E4` → [MiReturnCrossPartitionControlAreaCharges](../../text/4D/MiReturnCrossPartitionControlAreaCharges_function_004D6184.md) (`PAGE` → `.text`)
  - `0x008890F1` → [MiDereferenceControlArea](../../text/47/MiDereferenceControlArea_function_00479A20.md) (`PAGE` → `.text`)
  - `0x00889143` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00889153` → [MiDereferenceExtendInfo](../../text/48/MiDereferenceExtendInfo_function_0048EFA4.md) (`PAGE` → `.text`)
  - `0x0088916D` → [MiDeleteEnclavePages](../../pagelk/B7/MiDeleteEnclavePages_function_00B7E228.md) (`PAGE` → `PAGELK`)
  - `0x0088917A` → [MiRemoveUserPhysicalPagesView](../../text/68/MiRemoveUserPhysicalPagesView_function_00689658.md) (`PAGE` → `.text`)
  - `0x008891DF` → [MiReturnFullProcessCharges](../../text/2C/MiReturnFullProcessCharges_function_002C2E70.md) (`PAGE` → `.text`)
  - `0x008891F8` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00889212` → [MiDecrementLargeSubsections](../../text/4D/MiDecrementLargeSubsections_function_004D2BE0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00888F1D` → [sub_00B190F2 + 0x66](../B1/Unknown_function_00B190F2.md) (`tail-transfer`)
  - `0x008891CE` → [sub_00B190F2](../B1/Unknown_function_00B190F2.md) (`tail-transfer`)
  - `0x008891E8` → [sub_00B190F2](../B1/Unknown_function_00B190F2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00888C80  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00888C85  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00888C8A  55                              push rbp
00888C8B  56                              push rsi
00888C8C  57                              push rdi
00888C8D  41 54                           push r12
00888C8F  41 55                           push r13
00888C91  41 56                           push r14
00888C93  41 57                           push r15
00888C95  48 8B EC                        mov rbp, rsp
00888C98  48 83 EC 70                     sub rsp, 0x70
00888C9C  33 C0                           xor eax, eax
00888C9E  0F 57 C0                        xorps xmm0, xmm0
00888CA1  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00888CA5  33 F6                           xor esi, esi
00888CA7  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
00888CAB  4C 8B FA                        mov r15, rdx
00888CAE  48 8B F9                        mov rdi, rcx
00888CB1  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00888CB5  44 8B EE                        mov r13d, esi
00888CB8  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00888CBC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00888CC5  44 0F B6 61 20                  movzx r12d, byte ptr [rcx + 0x20]
00888CCA  44 0F B6 71 21                  movzx r14d, byte ptr [rcx + 0x21]
00888CCF  49 C1 E6 20                     shl r14, 0x20
00888CD3  4C 8B 80 B8 00 00 00            mov r8, qword ptr [rax + 0xb8]
00888CDA  49 C1 E4 20                     shl r12, 0x20
00888CDE  4C 89 45 40                     mov qword ptr [rbp + 0x40], r8
00888CE2  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
00888CE6  49 8D 80 00 04 00 00            lea rax, [r8 + 0x400]
00888CED  48 89 75 58                     mov qword ptr [rbp + 0x58], rsi
00888CF1  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00888CF5  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00888CF8  4C 0B E0                        or r12, rax
00888CFB  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
00888CFE  4C 0B F0                        or r14, rax
00888D01  49 C1 E4 0C                     shl r12, 0xc
00888D05  49 C1 E6 0C                     shl r14, 0xc
00888D09  49 81 CE FF 0F 00 00            or r14, 0xfff
00888D10  E8 0B 6A AA FF                  call 0x14032f720
00888D15  F7 D8                           neg eax
00888D17  1B DB                           sbb ebx, ebx
00888D19  83 E3 40                        and ebx, 0x40
00888D1C  F7 41 30 00 00 20 00            test dword ptr [rcx + 0x30], 0x200000
00888D23  0F 84 4A 02 00 00               je 0x140888f73
00888D29  8B 4F 30                        mov ecx, dword ptr [rdi + 0x30]
00888D2C  8B C1                           mov eax, ecx
00888D2E  25 00 00 20 04                  and eax, 0x4200000
00888D33  3D 00 00 20 00                  cmp eax, 0x200000
00888D38  0F 84 1F 04 00 00               je 0x14088915d
00888D3E  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00888D41  83 E0 70                        and eax, 0x70
00888D44  3C 30                           cmp al, 0x30
00888D46  0F 84 2B 04 00 00               je 0x140889177
00888D4C  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
00888D4F  48 B8 FD FF FF FF 07 00 00 00   movabs rax, 0x7fffffffd
00888D59  0F B6 57 22                     movzx edx, byte ptr [rdi + 0x22]
00888D5D  48 C1 E2 20                     shl rdx, 0x20
00888D61  48 0B D1                        or rdx, rcx
00888D64  48 3B D0                        cmp rdx, rax
00888D67  0F 84 B5 03 00 00               je 0x140889122
00888D6D  81 FB 80 00 00 00               cmp ebx, 0x80
00888D73  73 08                           jae 0x140888d7d
00888D75  48 8B CF                        mov rcx, rdi
00888D78  E8 83 E0 A0 FF                  call 0x140296e00
00888D7D  8B 4F 30                        mov ecx, dword ptr [rdi + 0x30]
00888D80  BA 10 00 00 00                  mov edx, 0x10
00888D85  0F BA E1 15                     bt ecx, 0x15
00888D89  0F 82 71 02 00 00               jb 0x140889000
00888D8F  8B 4D 50                        mov ecx, dword ptr [rbp + 0x50]
00888D92  44 8B C1                        mov r8d, ecx
00888D95  41 C1 F8 1F                     sar r8d, 0x1f
00888D99  41 83 E0 01                     and r8d, 1
00888D9D  41 83 C0 02                     add r8d, 2
00888DA1  F6 C1 01                        test cl, 1
00888DA4  74 04                           je 0x140888daa
00888DA6  41 83 C8 04                     or r8d, 4
00888DAA  48 8B CF                        mov rcx, rdi
00888DAD  E8 6E 69 AA FF                  call 0x14032f720
00888DB2  41 8B F0                        mov esi, r8d
00888DB5  0F BA EE 0B                     bts esi, 0xb
00888DB9  85 C0                           test eax, eax
00888DBB  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00888DBE  41 0F 44 F0                     cmove esi, r8d
00888DC2  25 00 00 20 04                  and eax, 0x4200000
00888DC7  3D 00 00 20 04                  cmp eax, 0x4200000
00888DCC  0F 84 D9 03 00 00               je 0x1408891ab
00888DD2  81 FB 80 00 00 00               cmp ebx, 0x80
00888DD8  73 20                           jae 0x140888dfa
00888DDA  4C 8D 4D C8                     lea r9, [rbp - 0x38]
00888DDE  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
00888DE2  44 8B C6                        mov r8d, esi
00888DE5  49 8B D6                        mov rdx, r14
00888DE8  49 8B CC                        mov rcx, r12
00888DEB  E8 50 08 A2 FF                  call 0x1402a9640
00888DF0  0F BA E6 0B                     bt esi, 0xb
00888DF4  0F 82 BA 03 00 00               jb 0x1408891b4
00888DFA  40 F6 C6 02                     test sil, 2
00888DFE  0F 84 CE 00 00 00               je 0x140888ed2
00888E04  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
00888E08  8B 4F 30                        mov ecx, dword ptr [rdi + 0x30]
00888E0B  4C 8B 28                        mov r13, qword ptr [rax]
00888E0E  8B C1                           mov eax, ecx
00888E10  24 70                           and al, 0x70
00888E12  3C 20                           cmp al, 0x20
00888E14  0F 84 9A 02 00 00               je 0x1408890b4
00888E1A  49 83 7D 40 00                  cmp qword ptr [r13 + 0x40], 0
00888E1F  74 65                           je 0x140888e86
00888E21  81 E1 80 0F 00 00               and ecx, 0xf80
00888E27  81 F9 00 02 00 00               cmp ecx, 0x200
00888E2D  0F 84 02 03 00 00               je 0x140889135
00888E33  81 F9 00 03 00 00               cmp ecx, 0x300
00888E39  0F 84 F6 02 00 00               je 0x140889135
00888E3F  0F B6 57 20                     movzx edx, byte ptr [rdi + 0x20]
00888E43  4C 8D 4D B0                     lea r9, [rbp - 0x50]
00888E47  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
00888E4A  45 33 C0                        xor r8d, r8d
00888E4D  48 C1 E2 20                     shl rdx, 0x20
00888E51  48 8B CF                        mov rcx, rdi
00888E54  48 0B D0                        or rdx, rax
00888E57  E8 14 5B AA FF                  call 0x14032e970
00888E5C  48 8B CF                        mov rcx, rdi
00888E5F  E8 B8 9D BC FF                  call 0x140452c1c
00888E64  A8 01                           test al, 1
00888E66  0F 85 81 03 00 00               jne 0x1408891ed
00888E6C  0F B6 57 21                     movzx edx, byte ptr [rdi + 0x21]
00888E70  4C 8D 4D 58                     lea r9, [rbp + 0x58]
00888E74  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
00888E77  45 33 C0                        xor r8d, r8d
00888E7A  48 C1 E2 20                     shl rdx, 0x20
00888E7E  48 0B D0                        or rdx, rax
00888E81  E8 EA 5A AA FF                  call 0x14032e970
00888E86  F6 C3 08                        test bl, 8
00888E89  75 47                           jne 0x140888ed2
00888E8B  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
00888E8E  83 E0 70                        and eax, 0x70
00888E91  3C 50                           cmp al, 0x50
00888E93  74 29                           je 0x140888ebe
00888E95  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00888E99  E8 A6 B2 BE FF                  call 0x140474144
00888E9E  8B 4F 30                        mov ecx, dword ptr [rdi + 0x30]
00888EA1  8B C1                           mov eax, ecx
00888EA3  24 70                           and al, 0x70
00888EA5  3C 20                           cmp al, 0x20
00888EA7  0F 84 F5 01 00 00               je 0x1408890a2
00888EAD  0F BA E1 15                     bt ecx, 0x15
00888EB1  72 0B                           jb 0x140888ebe
00888EB3  49 83 7D 40 00                  cmp qword ptr [r13 + 0x40], 0
00888EB8  0F 84 80 01 00 00               je 0x14088903e
00888EBE  48 8B 47 78                     mov rax, qword ptr [rdi + 0x78]
00888EC2  8B CB                           mov ecx, ebx
00888EC4  83 C9 01                        or ecx, 1
00888EC7  48 85 C0                        test rax, rax
00888ECA  0F 49 CB                        cmovns ecx, ebx
00888ECD  8B D9                           mov ebx, ecx
00888ECF  83 CB 08                        or ebx, 8
00888ED2  48 8B 75 40                     mov rsi, qword ptr [rbp + 0x40]
00888ED6  4D 8B C7                        mov r8, r15
00888ED9  48 8B CE                        mov rcx, rsi
00888EDC  48 8B D7                        mov rdx, rdi
00888EDF  E8 8C C7 A1 FF                  call 0x1402a5670
00888EE4  84 DB                           test bl, bl
00888EE6  78 23                           js 0x140888f0b
00888EE8  B8 00 00 00 00                  mov eax, 0
00888EED  4D 85 FF                        test r15, r15
00888EF0  4D 8B C7                        mov r8, r15
00888EF3  48 8B CF                        mov rcx, rdi
00888EF6  4C 0F 44 C0                     cmove r8, rax
00888EFA  8D 50 01                        lea edx, [rax + 1]
00888EFD  E8 76 CD A0 FF                  call 0x140295c78
00888F02  4D 85 FF                        test r15, r15
00888F05  0F 85 72 01 00 00               jne 0x14088907d
00888F0B  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00888F0F  48 89 47 08                     mov qword ptr [rdi + 8], rax
00888F13  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00888F17  48 89 07                        mov qword ptr [rdi], rax
00888F1A  F6 C3 40                        test bl, 0x40
00888F1D  0F 85 35 02 29 00               jne 0x140b19158
00888F23  F6 C3 01                        test bl, 1
00888F26  0F 85 21 02 00 00               jne 0x14088914d
00888F2C  F6 C3 08                        test bl, 8
00888F2F  75 65                           jne 0x140888f96
00888F31  4D 85 FF                        test r15, r15
00888F34  0F 85 DE 01 00 00               jne 0x140889118
00888F3A  84 DB                           test bl, bl
00888F3C  0F 88 D6 01 00 00               js 0x140889118
00888F42  33 C0                           xor eax, eax
00888F44  44 8B C8                        mov r9d, eax
00888F47  4D 8B C6                        mov r8, r14
00888F4A  49 8B D4                        mov rdx, r12
00888F4D  48 8B CF                        mov rcx, rdi
00888F50  E8 7B 7F BA FF                  call 0x140430ed0
00888F55  4D 85 ED                        test r13, r13
00888F58  75 74                           jne 0x140888fce
00888F5A  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
00888F62  48 83 C4 70                     add rsp, 0x70
00888F66  41 5F                           pop r15
00888F68  41 5E                           pop r14
00888F6A  41 5D                           pop r13
00888F6C  41 5C                           pop r12
00888F6E  5F                              pop rdi
00888F6F  5E                              pop rsi
00888F70  5D                              pop rbp
00888F71  C3                              ret
00888F72  CC                              int3
00888F73  48 8B 89 80 00 00 00            mov rcx, qword ptr [rcx + 0x80]
00888F7A  48 85 C9                        test rcx, rcx
00888F7D  0F 84 A6 FD FF FF               je 0x140888d29
00888F83  BA 4D 6D 53 63                  mov edx, 0x63536d4d
00888F88  E8 53 E9 A6 FF                  call 0x1402f78e0
00888F8D  4C 8B 45 40                     mov r8, qword ptr [rbp + 0x40]
00888F91  E9 93 FD FF FF                  jmp 0x140888d29
00888F96  F6 C3 02                        test bl, 2
00888F99  0F 85 56 02 00 00               jne 0x1408891f5
00888F9F  F6 C3 04                        test bl, 4
00888FA2  0F 85 24 01 00 00               jne 0x1408890cc
00888FA8  45 33 C0                        xor r8d, r8d
00888FAB  48 8B D6                        mov rdx, rsi
00888FAE  49 8B CD                        mov rcx, r13
00888FB1  E8 EA F9 FF FF                  call 0x1408889a0
00888FB6  48 8B 4F 48                     mov rcx, qword ptr [rdi + 0x48]
00888FBA  48 8D 57 60                     lea rdx, [rdi + 0x60]
00888FBE  41 B8 04 00 00 00               mov r8d, 4
00888FC4  E8 A7 95 A5 FF                  call 0x1402e2570
00888FC9  E9 63 FF FF FF                  jmp 0x140888f31
00888FCE  F6 C3 10                        test bl, 0x10
00888FD1  0F 85 17 01 00 00               jne 0x1408890ee
00888FD7  48 8B 7D B0                     mov rdi, qword ptr [rbp - 0x50]
00888FDB  48 8B 75 58                     mov rsi, qword ptr [rbp + 0x58]
00888FDF  48 85 FF                        test rdi, rdi
00888FE2  74 09                           je 0x140888fed
00888FE4  F6 C3 20                        test bl, 0x20
00888FE7  0F 85 1F 02 00 00               jne 0x14088920c
00888FED  4C 8B C6                        mov r8, rsi
00888FF0  48 8B D7                        mov rdx, rdi
00888FF3  49 8B CD                        mov rcx, r13
00888FF6  E8 25 CE 9F FF                  call 0x140285e20
00888FFB  E9 5A FF FF FF                  jmp 0x140888f5a
00889000  8B C1                           mov eax, ecx
00889002  83 E0 70                        and eax, 0x70
00889005  83 F8 30                        cmp eax, 0x30
00889008  0F 84 7A 01 00 00               je 0x140889188
0088900E  3B C2                           cmp eax, edx
00889010  0F 84 EA 00 00 00               je 0x140889100
00889016  44 8B C6                        mov r8d, esi
00889019  83 F8 40                        cmp eax, 0x40
0088901C  0F 84 7E 01 00 00               je 0x1408891a0
00889022  81 E1 00 00 20 14               and ecx, 0x14200000
00889028  81 F9 00 00 20 10               cmp ecx, 0x10200000
0088902E  0F 85 76 FD FF FF               jne 0x140888daa
00889034  41 0F BA E8 0A                  bts r8d, 0xa
00889039  E9 6C FD FF FF                  jmp 0x140888daa
0088903E  0F B6 57 20                     movzx edx, byte ptr [rdi + 0x20]
00889042  4C 8D 4D B0                     lea r9, [rbp - 0x50]
00889046  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
00889049  45 33 C0                        xor r8d, r8d
0088904C  48 C1 E2 20                     shl rdx, 0x20
00889050  48 8B CF                        mov rcx, rdi
00889053  48 0B D0                        or rdx, rax
00889056  E8 15 59 AA FF                  call 0x14032e970
0088905B  0F B6 57 21                     movzx edx, byte ptr [rdi + 0x21]
0088905F  4C 8D 4D 58                     lea r9, [rbp + 0x58]
00889063  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
00889066  45 33 C0                        xor r8d, r8d
00889069  48 C1 E2 20                     shl rdx, 0x20
0088906D  48 8B CF                        mov rcx, rdi
00889070  48 0B D0                        or rdx, rax
00889073  E8 F8 58 AA FF                  call 0x14032e970
00889078  E9 41 FE FF FF                  jmp 0x140888ebe
0088907D  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00889084  F0 49 0F C1 47 28               lock xadd qword ptr [r15 + 0x28], rax
0088908A  24 06                           and al, 6
0088908C  3C 02                           cmp al, 2
0088908E  0F 84 AB 00 00 00               je 0x14088913f
00889094  49 8D 4F 28                     lea rcx, [r15 + 0x28]
00889098  E8 63 85 A5 FF                  call 0x1402e1600
0088909D  E9 69 FE FF FF                  jmp 0x140888f0b
008890A2  41 F7 45 38 00 00 00 08         test dword ptr [r13 + 0x38], 0x8000000
008890AA  75 4F                           jne 0x1408890fb
008890AC  83 CB 04                        or ebx, 4
008890AF  E9 0A FE FF FF                  jmp 0x140888ebe
008890B4  48 8B CF                        mov rcx, rdi
008890B7  E8 60 9B BC FF                  call 0x140452c1c
008890BC  A8 01                           test al, 1
008890BE  0F 84 C2 FD FF FF               je 0x140888e86
008890C4  83 CB 18                        or ebx, 0x18
008890C7  E9 BA FD FF FF                  jmp 0x140888e86
008890CC  33 D2                           xor edx, edx
008890CE  49 8B CD                        mov rcx, r13
008890D1  E8 F6 A5 B2 FF                  call 0x1403b36cc
008890D6  A9 FD FF FF FF                  test eax, 0xfffffffd
008890DB  0F 85 C7 FE FF FF               jne 0x140888fa8
008890E1  49 8B CD                        mov rcx, r13
008890E4  E8 9B D0 C4 FF                  call 0x1404d6184
008890E9  E9 BA FE FF FF                  jmp 0x140888fa8
008890EE  49 8B CD                        mov rcx, r13
008890F1  E8 2A 09 BF FF                  call 0x140479a20
008890F6  E9 5F FE FF FF                  jmp 0x140888f5a
008890FB  83 CB 02                        or ebx, 2
008890FE  EB AC                           jmp 0x1408890ac
00889100  0F BA E1 1D                     bt ecx, 0x1d
00889104  B8 40 00 00 00                  mov eax, 0x40
00889109  41 B8 20 00 00 00               mov r8d, 0x20
0088910F  44 0F 42 C0                     cmovb r8d, eax
00889113  E9 0A FF FF FF                  jmp 0x140889022
00889118  B8 01 00 00 00                  mov eax, 1
0088911D  E9 22 FE FF FF                  jmp 0x140888f44
00889122  8B C3                           mov eax, ebx
00889124  0F BA EB 07                     bts ebx, 7
00889128  48 83 7F 10 FE                  cmp qword ptr [rdi + 0x10], -2
0088912D  0F 45 D8                        cmovne ebx, eax
00889130  E9 38 FC FF FF                  jmp 0x140888d6d
00889135  F0 41 FF 4D 5C                  lock dec dword ptr [r13 + 0x5c]
0088913A  E9 00 FD FF FF                  jmp 0x140888e3f
0088913F  49 8D 4F 28                     lea rcx, [r15 + 0x28]
00889143  E8 88 CC 9D FF                  call 0x140265dd0
00889148  E9 47 FF FF FF                  jmp 0x140889094
0088914D  49 8B D5                        mov rdx, r13
00889150  48 8B CF                        mov rcx, rdi
00889153  E8 4C 5E C0 FF                  call 0x14048efa4
00889158  E9 CF FD FF FF                  jmp 0x140888f2c
0088915D  0F BA E1 1B                     bt ecx, 0x1b
00889161  0F 83 D7 FB FF FF               jae 0x140888d3e
00889167  48 8B D7                        mov rdx, rdi
0088916A  49 8B C8                        mov rcx, r8
0088916D  E8 B6 50 2F 00                  call 0x140b7e228
00889172  E9 C7 FB FF FF                  jmp 0x140888d3e
00889177  48 8B CF                        mov rcx, rdi
0088917A  E8 D9 04 E0 FF                  call 0x140689658
0088917F  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00889183  E9 C4 FB FF FF                  jmp 0x140888d4c
00889188  8B C1                           mov eax, ecx
0088918A  44 8B C6                        mov r8d, esi
0088918D  25 00 00 20 0C                  and eax, 0xc200000
00889192  3D 00 00 20 08                  cmp eax, 0x8200000
00889197  44 0F 45 C2                     cmovne r8d, edx
0088919B  E9 82 FE FF FF                  jmp 0x140889022
008891A0  41 B8 08 00 00 00               mov r8d, 8
008891A6  E9 FF FB FF FF                  jmp 0x140888daa
008891AB  0F BA EE 0C                     bts esi, 0xc
008891AF  E9 1E FC FF FF                  jmp 0x140888dd2
008891B4  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
008891B7  0F B6 57 22                     movzx edx, byte ptr [rdi + 0x22]
008891BB  4C 8B 45 F8                     mov r8, qword ptr [rbp - 8]
008891BF  48 C1 E2 20                     shl rdx, 0x20
008891C3  48 0B D1                        or rdx, rcx
008891C6  48 89 55 B8                     mov qword ptr [rbp - 0x48], rdx
008891CA  4C 39 6D F8                     cmp qword ptr [rbp - 8], r13
008891CE  0F 84 1E FF 28 00               je 0x140b190f2
008891D4  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
008891D8  49 8B D0                        mov rdx, r8
008891DB  4C 89 6D F8                     mov qword ptr [rbp - 8], r13
008891DF  E8 8C 9C A3 FF                  call 0x1402c2e70
008891E4  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
008891E8  E9 05 FF 28 00                  jmp 0x140b190f2
008891ED  83 CB 20                        or ebx, 0x20
008891F0  E9 77 FC FF FF                  jmp 0x140888e6c
008891F5  48 8B CE                        mov rcx, rsi
008891F8  E8 F3 66 9A FF                  call 0x14022f8f0
008891FD  8B D0                           mov edx, eax
008891FF  49 8B CD                        mov rcx, r13
00889202  E8 E1 5B 1A 00                  call 0x140a2ede8
00889207  E9 93 FD FF FF                  jmp 0x140888f9f
0088920C  48 8B D6                        mov rdx, rsi
0088920F  48 8B CF                        mov rcx, rdi
00889212  E8 C9 99 C4 FF                  call 0x1404d2be0
00889217  E9 D1 FD FF FF                  jmp 0x140888fed
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeleteVad(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m40 = 0;
    v_rsi = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    v_r14 = (*(unsigned __int8 *)(a1 + 33)) << (32);
    v_r12 = (*(unsigned __int8 *)(a1 + 32)) << (32);
    v_stack_p8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m88 = 0;
    v_stack_p20 = 0;
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    v_r12 = (v_r12) | ((unsigned int)(*(unsigned int *)(a1 + 24)));
    v_r14 = (v_r14) | ((unsigned int)(*(unsigned int *)(a1 + 28)));
    v_r12 = (v_r12) << (12);
    v_r14 = (v_r14) << (12);
    v_r14 = (v_r14) | (0xFFFULL);
    result = MiIsVadLargePrivate(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    result = (unsigned int)(-(result));
    v_rbx = (unsigned int)((v_rbx) & (64));
    if (((*(unsigned int *)(a1 + 48)) & (0x200000ULL)) == 0) goto loc_00888F73;
loc_00888D29:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (0x4200000ULL));
    if (((unsigned int)(result)) == 0x200000ULL) goto loc_0088915D;
loc_00888D3E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (112));
    if (((unsigned __int8)(result)) == 48) goto loc_00889177;
loc_00888D4C:
    a2 = (*(unsigned __int8 *)(a1 + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(a1 + 52)));
    if (a2 == result) goto loc_00889122;
loc_00888D6D:
    if (((unsigned int)(v_rbx)) < 128) {
        a1 = a1;
        result = MiSetVadDeleted(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
    }
    if (((unsigned int)(v_rbx)) < 128) goto loc_00889000;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) >> (31));
    a3 = (unsigned int)((a3) & (1));
    a3 = (unsigned int)((a3) + (2));
    if ((((unsigned __int8)((unsigned int)(v_stack_p18))) & (1)) != 0) {
        a3 = (unsigned int)((a3) | (4));
    }
    result = MiIsVadLargePrivate(a1, 16, a3, a4);
    v_rsi = (unsigned int)(a3);
    if ((unsigned int)(result) == 0) { v_rsi = a3; }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (0x4200000ULL));
    if (((unsigned int)(result)) == 0x4200000ULL) goto loc_008891AB;
loc_00888DD2:
    if (((unsigned int)(v_rbx)) >= 128) goto loc_00888DFA;
    v_stack_m50 = a1;
    result = MiDeleteVirtualAddresses(v_r12, v_r14, (unsigned int)((unsigned int)(v_rsi)), v_stack_m70);
    if (((unsigned int)(v_rbx)) < 128) goto loc_008891B4;
loc_00888DFA:
    if ((((unsigned __int8)(v_rsi)) & (2)) == 0) goto loc_00888ED2;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (112));
    if (((unsigned __int8)(result)) == 32) goto loc_008890B4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 64)) == 0) goto loc_00888E86;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (0xF80ULL));
    if (((unsigned int)(a1)) == 512) goto loc_00889135;
    if (((unsigned int)(a1)) == 768) goto loc_00889135;
loc_00888E3F:
    a3 = 0;
    a2 = (*(unsigned __int8 *)(a1 + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(a1 + 24)));
    result = MiGetProtoPteAddress(a1, a2, a3, v_stack_m88);
    result = MiReadVadFlags2(a1, a2, a3, v_stack_m88);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_008891ED;
loc_00888E6C:
    a3 = 0;
    a2 = (*(unsigned __int8 *)(a1 + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(a1 + 28)));
    result = MiGetProtoPteAddress(a1, a2, a3, v_stack_p20);
loc_00888E86:
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) goto loc_00888ED2;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (112));
    if (((unsigned __int8)(result)) == 80) goto loc_00888EBE;
    result = MiDrainSystemAccessLog(v_stack_m78, a2, a3, v_stack_p20);
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (112));
    if (((unsigned __int8)(result)) == 32) goto loc_008890A2;
    if (((unsigned __int8)(result)) < 32) goto loc_00888EBE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 64)) == 0) goto loc_0088903E;
loc_00888EBE:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) | (1));
    if (!sign_flag) { a1 = (unsigned int)(v_rbx); }
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (8));
loc_00888ED2:
    result = MiLockAddressSpaceToo(v_stack_p8, a1, a2, v_stack_p20);
    if (sign_flag) goto loc_00888F0B;
    if (a2 == 0) { a2 = 0; }
    result = MiRemoveVad(a1, 0 + 1, a2, v_stack_p20);
    if (a2 != 0) goto loc_0088907D;
loc_00888F0B:
    *(unsigned __int64 *)(a1 + 8) = v_stack_m68;
    *(unsigned __int64 *)(a1) = v_stack_m60;
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_0088914D;
loc_00888F2C:
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) goto loc_00888F96;
loc_00888F31:
    if (a2 != 0) goto loc_00889118;
    if (sign_flag) goto loc_00889118;
    result = 0;
loc_00888F44:
    result = MiFinishVadDeletion(a1, v_r12, v_r14, 0);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) != 0) goto loc_00888FCE;
loc_00888F5A:
    v_rsp = (v_rsp) + (112);
    return result;
loc_00888F73:
    if (*(unsigned __int64 *)(a1 + 128) == 0) goto loc_00888D29;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 128), (unsigned int)(0x63536D4DULL), v_r14, 0);
    goto loc_00888D29;
loc_00888F96:
    if ((((unsigned __int8)(v_stack_p10)) & (2)) != 0) goto loc_008891F5;
loc_00888F9F:
    if ((((unsigned __int8)(v_stack_p10)) & (4)) != 0) goto loc_008890CC;
loc_00888FA8:
    a3 = 0;
    result = MiRemoveSharedCommitNode(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)), v_stack_p8, a3, 0);
    result = MiManageSubsectionView(*(unsigned __int64 *)(a1 + 72), a1 + 96, 4, 0);
    goto loc_00888F31;
loc_00888FCE:
    if ((((unsigned __int8)(v_stack_p10)) & (16)) != 0) goto loc_008890EE;
    if (v_stack_m88 == 0) goto loc_00888FED;
    if ((((unsigned __int8)(v_stack_p10)) & (32)) != 0) goto loc_0088920C;
loc_00888FED:
    result = MiUnmapViewSubsections(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)), v_stack_m88, v_stack_p20, 0);
    goto loc_00888F5A;
loc_00889000:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72))))) & (112));
    if (((unsigned int)(result)) == 48) goto loc_00889188;
    if (((unsigned int)(result)) == ((unsigned int)(v_stack_m88))) goto loc_00889100;
    if (((unsigned int)(result)) == 64) goto loc_008891A0;
loc_00889022:
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72))) & (0x14200000ULL));
    if (((unsigned int)(a1)) != 0x10200000ULL) goto loc_00888DAA;
    goto loc_00888DAA;
loc_0088903E:
    a3 = 0;
    a2 = (*(unsigned __int8 *)(v_stack_m88 + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_stack_m88 + 24)));
    result = MiGetProtoPteAddress(v_stack_m88, a2, a3, v_stack_m88);
    a3 = 0;
    a2 = (*(unsigned __int8 *)(v_stack_m88 + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_stack_m88 + 28)));
    result = MiGetProtoPteAddress(v_stack_m88, a2, a3, v_stack_p20);
    goto loc_00888EBE;
loc_0088907D:
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0088913F;
loc_00889094:
    result = KeAbPostRelease(a2 + 40, a2, a3, v_stack_p20);
    goto loc_00888F0B;
loc_008890A2:
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) + 56)) & (0x8000000ULL)) != 0) goto loc_008890FB;
loc_008890AC:
    v_rbx = (unsigned int)((v_stack_p10) | (4));
    goto loc_00888EBE;
loc_008890B4:
    result = MiReadVadFlags2(v_stack_m88, a2, a3, v_stack_p20);
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00888E86;
    v_rbx = (unsigned int)((v_rbx) | (24));
    goto loc_00888E86;
loc_008890CC:
    a2 = 0;
    result = MiControlAreaRequiresCharge(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)), a2, a3, v_stack_p20);
    if ((((unsigned int)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_00888FA8;
    result = MiReturnCrossPartitionControlAreaCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)), a2, a3, v_stack_p20);
    goto loc_00888FA8;
loc_008890EE:
    result = MiDereferenceControlArea(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)), a2, a3, v_stack_p20);
    goto loc_00888F5A;
loc_008890FB:
    v_rbx = (unsigned int)((v_rbx) | (2));
    goto loc_008890AC;
loc_00889100:
    a3 = 32;
    if (condition_is_below) { a3 = 64; }
    goto loc_00889022;
loc_00889118:
    goto loc_00888F44;
loc_00889122:
    if ((*(unsigned __int64 *)(v_stack_m88 + 16)) != -2) { v_rbx = (unsigned int)((unsigned int)((unsigned int)(v_rbx))); }
    goto loc_00888D6D;
loc_00889135:
    goto loc_00888E3F;
loc_0088913F:
    result = ExfTryToWakePushLock(a2 + 40, a2, a3, v_stack_p20);
    goto loc_00889094;
loc_0088914D:
    result = MiDereferenceExtendInfo(v_stack_m88, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)), a3, v_stack_p20);
    goto loc_00888F2C;
loc_0088915D:
    if ((*(unsigned __int64 *)(v_stack_m88 + 16)) >= -2) goto loc_00888D3E;
    result = MiDeleteEnclavePages(a3, v_stack_m88, a3, v_stack_p20);
    goto loc_00888D3E;
loc_00889177:
    result = MiRemoveUserPhysicalPagesView(v_stack_m88, v_stack_m88, a3, v_stack_p20);
    v_stack_m48 = result;
    goto loc_00888D4C;
loc_00889188:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m88))) & (0xC200000ULL));
    a3 = (unsigned int)((unsigned int)(v_stack_p20));
    if (((unsigned int)(result)) != 0x8200000ULL) { a3 = (unsigned int)(v_stack_m88); }
    goto loc_00889022;
loc_008891A0:
    goto loc_00888DAA;
loc_008891AB:
    goto loc_00888DD2;
loc_008891B4:
    a2 = (*(unsigned __int8 *)(v_stack_m88 + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_stack_m88 + 52)));
    v_stack_m80 = a2;
    v_stack_m40 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72));
    result = MiReturnFullProcessCharges(v_stack_p8, v_stack_m40, v_stack_m40, v_stack_p20);
loc_008891ED:
    v_rbx = (unsigned int)((v_rbx) | (32));
    goto loc_00888E6C;
loc_008891F5:
    result = PsGetProcessSessionIdEx(v_stack_p20, v_stack_m80, v_stack_m40, v_stack_p20);
    result = MiDereferencePerSessionProtos(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)), (unsigned int)((unsigned int)(result)), v_stack_m40, v_stack_p20);
    goto loc_00888F9F;
loc_0088920C:
    result = MiDecrementLargeSubsections(v_stack_m88, v_stack_p20, v_stack_m40, v_stack_p20);
    goto loc_00888FED;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeleteVad(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m40 = 0;
    local_rsi = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    local_r14 = (*(uint8_t *)(arg1 + 0x21)) << (32);
    local_r12 = (*(uint8_t *)(arg1 + 0x20)) << (32);
    v_stack_p8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m88 = 0;
    v_stack_p20 = 0;
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    local_r12 = (local_r12) | ((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    local_r14 = (local_r14) | ((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    local_r12 = (local_r12) << (12);
    local_r14 = (local_r14) << (12);
    local_r14 = (local_r14) | (0xFFFULL);
    result = MiIsVadLargePrivate(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), a4);
    result = (uint32_t)(-(result));
    local_rbx = (uint32_t)((local_rbx) & (64));
    if (((*(uint32_t *)(arg1 + 0x30)) & (0x200000ULL)) == 0) goto loc_00888F73;
loc_00888D29:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (0x4200000ULL));
    if (((uint32_t)(result)) == 0x200000ULL) goto loc_0088915D;
loc_00888D3E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (112));
    if (((uint8_t)(result)) == 48) goto loc_00889177;
loc_00888D4C:
    Arg2 = (*(uint8_t *)(arg1 + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(arg1 + 0x34)));
    if (Arg2 == result) goto loc_00889122;
loc_00888D6D:
    if (((uint32_t)(local_rbx)) < 128) {
        Arg1 = Arg1;
        result = MiSetVadDeleted(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), a4);
    }
    if (((uint32_t)(local_rbx)) < 128) goto loc_00889000;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) >> (31));
    Arg3 = (uint32_t)((Arg3) & (1));
    Arg3 = (uint32_t)((Arg3) + (2));
    if ((((uint8_t)((uint32_t)(v_stack_p18))) & (1)) != 0) {
        Arg3 = (uint32_t)((Arg3) | (4));
    }
    result = MiIsVadLargePrivate(Arg1, 16, Arg3, a4);
    local_rsi = (uint32_t)(Arg3);
    if ((uint32_t)(result) == 0) { local_rsi = Arg3; }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (0x4200000ULL));
    if (((uint32_t)(result)) == 0x4200000ULL) goto loc_008891AB;
loc_00888DD2:
    if (((uint32_t)(local_rbx)) >= 128) goto loc_00888DFA;
    v_stack_m50 = Arg1;
    result = MiDeleteVirtualAddresses(local_r12, local_r14, (uint32_t)((uint32_t)(local_rsi)), v_stack_m70);
    if (((uint32_t)(local_rbx)) < 128) goto loc_008891B4;
loc_00888DFA:
    if ((((uint8_t)(local_rsi)) & (2)) == 0) goto loc_00888ED2;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (112));
    if (((uint8_t)(result)) == 32) goto loc_008890B4;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x40)) == 0) goto loc_00888E86;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (0xF80ULL));
    if (((uint32_t)(Arg1)) == 512) goto loc_00889135;
    if (((uint32_t)(Arg1)) == 768) goto loc_00889135;
loc_00888E3F:
    Arg3 = 0;
    Arg2 = (*(uint8_t *)(arg1 + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    result = MiGetProtoPteAddress(Arg1, Arg2, Arg3, v_stack_m88);
    result = MiReadVadFlags2(Arg1, Arg2, Arg3, v_stack_m88);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_008891ED;
loc_00888E6C:
    Arg3 = 0;
    Arg2 = (*(uint8_t *)(arg1 + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    result = MiGetProtoPteAddress(Arg1, Arg2, Arg3, v_stack_p20);
loc_00888E86:
    if ((((uint8_t)(local_rbx)) & (8)) != 0) goto loc_00888ED2;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (112));
    if (((uint8_t)(result)) == 80) goto loc_00888EBE;
    result = MiDrainSystemAccessLog(v_stack_m78, Arg2, Arg3, v_stack_p20);
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (112));
    if (((uint8_t)(result)) == 32) goto loc_008890A2;
    if (((uint8_t)(result)) < 32) goto loc_00888EBE;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x40)) == 0) goto loc_0088903E;
loc_00888EBE:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) | (1));
    if (!sign_flag) { Arg1 = (uint32_t)(local_rbx); }
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (8));
loc_00888ED2:
    result = MiLockAddressSpaceToo(v_stack_p8, Arg1, Arg2, v_stack_p20);
    if (sign_flag) goto loc_00888F0B;
    if (Arg2 == 0) { Arg2 = 0; }
    result = MiRemoveVad(Arg1, 0 + 1, Arg2, v_stack_p20);
    if (Arg2 != 0) goto loc_0088907D;
loc_00888F0B:
    *(uint64_t *)(arg1 + 0x8) = v_stack_m68;
    *(uint64_t *)(arg1) = v_stack_m60;
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_0088914D;
loc_00888F2C:
    if ((((uint8_t)(local_rbx)) & (8)) != 0) goto loc_00888F96;
loc_00888F31:
    if (Arg2 != 0) goto loc_00889118;
    if (sign_flag) goto loc_00889118;
    result = 0;
loc_00888F44:
    result = MiFinishVadDeletion(Arg1, local_r12, local_r14, 0);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) != 0) goto loc_00888FCE;
loc_00888F5A:
    local_rsp = (local_rsp) + (112);
    return result;
loc_00888F73:
    if (*(uint64_t *)(arg1 + 0x80) == 0) goto loc_00888D29;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x80), (uint32_t)(0x63536D4DULL), local_r14, 0);
    goto loc_00888D29;
loc_00888F96:
    if ((((uint8_t)(v_stack_p10)) & (2)) != 0) goto loc_008891F5;
loc_00888F9F:
    if ((((uint8_t)(v_stack_p10)) & (4)) != 0) goto loc_008890CC;
loc_00888FA8:
    Arg3 = 0;
    result = MiRemoveSharedCommitNode(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)), v_stack_p8, Arg3, 0);
    result = MiManageSubsectionView(*(uint64_t *)(arg1 + 0x48), Arg1 + 96, 4, 0);
    goto loc_00888F31;
loc_00888FCE:
    if ((((uint8_t)(v_stack_p10)) & (16)) != 0) goto loc_008890EE;
    if (v_stack_m88 == 0) goto loc_00888FED;
    if ((((uint8_t)(v_stack_p10)) & (32)) != 0) goto loc_0088920C;
loc_00888FED:
    result = MiUnmapViewSubsections(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)), v_stack_m88, v_stack_p20, 0);
    goto loc_00888F5A;
loc_00889000:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48))))) & (112));
    if (((uint32_t)(result)) == 48) goto loc_00889188;
    if (((uint32_t)(result)) == ((uint32_t)(v_stack_m88))) goto loc_00889100;
    if (((uint32_t)(result)) == 64) goto loc_008891A0;
loc_00889022:
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x48))) & (0x14200000ULL));
    if (((uint32_t)(Arg1)) != 0x10200000ULL) goto loc_00888DAA;
    goto loc_00888DAA;
loc_0088903E:
    Arg3 = 0;
    Arg2 = (*(uint8_t *)(v_stack_m88 + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x18)));
    result = MiGetProtoPteAddress(v_stack_m88, Arg2, Arg3, v_stack_m88);
    Arg3 = 0;
    Arg2 = (*(uint8_t *)(v_stack_m88 + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x1C)));
    result = MiGetProtoPteAddress(v_stack_m88, Arg2, Arg3, v_stack_p20);
    goto loc_00888EBE;
loc_0088907D:
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0088913F;
loc_00889094:
    result = KeAbPostRelease(Arg2 + 40, Arg2, Arg3, v_stack_p20);
    goto loc_00888F0B;
loc_008890A2:
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) + 0x38)) & (0x8000000ULL)) != 0) goto loc_008890FB;
loc_008890AC:
    local_rbx = (uint32_t)((v_stack_p10) | (4));
    goto loc_00888EBE;
loc_008890B4:
    result = MiReadVadFlags2(v_stack_m88, Arg2, Arg3, v_stack_p20);
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00888E86;
    local_rbx = (uint32_t)((local_rbx) | (24));
    goto loc_00888E86;
loc_008890CC:
    Arg2 = 0;
    result = MiControlAreaRequiresCharge(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)), Arg2, Arg3, v_stack_p20);
    if ((((uint32_t)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_00888FA8;
    result = MiReturnCrossPartitionControlAreaCharges(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)), Arg2, Arg3, v_stack_p20);
    goto loc_00888FA8;
loc_008890EE:
    result = MiDereferenceControlArea(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)), Arg2, Arg3, v_stack_p20);
    goto loc_00888F5A;
loc_008890FB:
    local_rbx = (uint32_t)((local_rbx) | (2));
    goto loc_008890AC;
loc_00889100:
    Arg3 = 32;
    if (condition_is_below) { Arg3 = 64; }
    goto loc_00889022;
loc_00889118:
    goto loc_00888F44;
loc_00889122:
    if ((*(uint64_t *)(v_stack_m88 + 0x10)) != -2) { local_rbx = (uint32_t)((uint32_t)((uint32_t)(local_rbx))); }
    goto loc_00888D6D;
loc_00889135:
    goto loc_00888E3F;
loc_0088913F:
    result = ExfTryToWakePushLock(Arg2 + 40, Arg2, Arg3, v_stack_p20);
    goto loc_00889094;
loc_0088914D:
    result = MiDereferenceExtendInfo(v_stack_m88, *(uint64_t *)(*(uint64_t *)(arg1 + 0x48)), Arg3, v_stack_p20);
    goto loc_00888F2C;
loc_0088915D:
    if ((*(uint64_t *)(v_stack_m88 + 0x10)) >= -2) goto loc_00888D3E;
    result = MiDeleteEnclavePages(Arg3, v_stack_m88, Arg3, v_stack_p20);
    goto loc_00888D3E;
loc_00889177:
    result = MiRemoveUserPhysicalPagesView(v_stack_m88, v_stack_m88, Arg3, v_stack_p20);
    v_stack_m48 = result;
    goto loc_00888D4C;
loc_00889188:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m88))) & (0xC200000ULL));
    Arg3 = (uint32_t)((uint32_t)(v_stack_p20));
    if (((uint32_t)(result)) != 0x8200000ULL) { Arg3 = (uint32_t)(v_stack_m88); }
    goto loc_00889022;
loc_008891A0:
    goto loc_00888DAA;
loc_008891AB:
    goto loc_00888DD2;
loc_008891B4:
    Arg2 = (*(uint8_t *)(v_stack_m88 + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x34)));
    v_stack_m80 = Arg2;
    v_stack_m40 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x48));
    result = MiReturnFullProcessCharges(v_stack_p8, v_stack_m40, v_stack_m40, v_stack_p20);
loc_008891ED:
    local_rbx = (uint32_t)((local_rbx) | (32));
    goto loc_00888E6C;
loc_008891F5:
    result = PsGetProcessSessionIdEx(v_stack_p20, v_stack_m80, v_stack_m40, v_stack_p20);
    result = MiDereferencePerSessionProtos(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48)), (uint32_t)((uint32_t)(result)), v_stack_m40, v_stack_p20);
    goto loc_00888F9F;
loc_0088920C:
    result = MiDecrementLargeSubsections(v_stack_m88, v_stack_p20, v_stack_m40, v_stack_p20);
    goto loc_00888FED;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0x22` | `8` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00888C80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
