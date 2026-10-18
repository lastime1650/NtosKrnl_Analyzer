# MiMapViewOfImageSection

- RVA: `0x0097E92C`–`0x0097F97D` (길이 `4,177` bytes)
- VA: `0x000000014097E92C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000975EC`
- 디코드: `967`개 명령, `4,177/4,177` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **53**; 고유 호출 대상: **44**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0097E972` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0097EBA4` → [MiCheckPurgeAndUpMapCount](../../text/41/MiCheckPurgeAndUpMapCount_function_004186B0.md) (function, `0x004186B0`)
- `0x0097EBC2` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0097EC36` → [MiReferenceFileObjectForMap](../88/MiReferenceFileObjectForMap_function_00885C00.md) (function, `0x00885C00`)
- `0x0097ECC4` → [MiWriteVadFlags2](../../text/41/MiWriteVadFlags2_function_0041C020.md) (function, `0x0041C020`)
- `0x0097ECEA` → [LOCK_ADDRESS_SPACE](../../text/2A/LOCK_ADDRESS_SPACE_function_002A4944.md) (function, `0x002A4944`)
- `0x0097ED31` → [MiIsVaRangeAvailable](MiIsVaRangeAvailable_function_0097FD90.md) (function, `0x0097FD90`)
- `0x0097ED88` → [MiUpdateVadStartVpn](../../text/45/MiUpdateVadStartVpn_function_00450ED4.md) (function, `0x00450ED4`)
- `0x0097EE15` → [MiInsertSharedCommitNode](../88/MiInsertSharedCommitNode_function_00887210.md) (function, `0x00887210`)
- `0x0097EE3D` → [MiControlAreaRequiresCharge](../../text/3B/MiControlAreaRequiresCharge_function_003B36CC.md) (function, `0x003B36CC`)
- `0x0097EE59` → [MiInsertVadCharges](../88/MiInsertVadCharges_function_00886AA8.md) (function, `0x00886AA8`)
- `0x0097EE7A` → [MiInsertVad](../../text/26/MiInsertVad_function_00265540.md) (function, `0x00265540`)
- `0x0097EF17` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (function, `0x00452C1C`)
- `0x0097EF56` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x0097EFF4` → [MiIsVaRangeAvailable](MiIsVaRangeAvailable_function_0097FD90.md) (function, `0x0097FD90`)
- `0x0097F011` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (function, `0x00295810`)
- `0x0097F01E` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x0097F029` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (function, `0x00452C1C`)
- `0x0097F078` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (function, `0x002A59C8`)
- `0x0097F08F` → [PsCallImageNotifyRoutines](../8D/PsCallImageNotifyRoutines_function_008D6C20.md) (function, `0x008D6C20`)
- `0x0097F09C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0097F0B9` → [MmUnsecureVirtualMemory](../88/MmUnsecureVirtualMemory_function_0088A2A0.md) (function, `0x0088A2A0`)
- `0x0097F0CB` → [MiAdvanceVadHint](../88/MiAdvanceVadHint_function_00886C40.md) (function, `0x00886C40`)
- `0x0097F103` → [PsIsImageNotifyEnabled](PsIsImageNotifyEnabled_function_0097FDE0.md) (function, `0x0097FDE0`)
- `0x0097F173` → [MiReferenceControlAreaFile](../../text/43/MiReferenceControlAreaFile_function_00431554.md) (function, `0x00431554`)
- `0x0097F1A0` → [MiCommitVadMetadataBits](../8D/MiCommitVadMetadataBits_function_008D1A00.md) (function, `0x008D1A00`)
- `0x0097F1B7` → [MiDoesImageContainFunctionOverrideFixups](../8D/MiDoesImageContainFunctionOverrideFixups_function_008D05D8.md) (function, `0x008D05D8`)
- `0x0097F22D` → [MiAllowImageMap](../8C/MiAllowImageMap_function_008C8B10.md) (function, `0x008C8B10`)
- `0x0097F2DA` → [MiSelectUserAddress](../88/MiSelectUserAddress_function_00885C40.md) (function, `0x00885C40`)
- `0x0097F324` → [ExGenRandom](../../text/41/ExGenRandom_function_0041B010.md) (function, `0x0041B010`)
- `0x0097F370` → [MiAddSecureEntry](../98/MiAddSecureEntry_function_00980250.md) (function, `0x00980250`)
- `0x0097F38B` → [MiReferenceVad](../../text/29/MiReferenceVad_function_00295890.md) (function, `0x00295890`)
- `0x0097F3A1` → [MiUnmapVad](../88/MiUnmapVad_function_00889280.md) (function, `0x00889280`)
- `0x0097F452` → [MiDoesImageContainFunctionOverrideFixups](../8D/MiDoesImageContainFunctionOverrideFixups_function_008D05D8.md) (function, `0x008D05D8`)
- `0x0097F465` → [MiMapImageScpCfgPages](../../text/29/MiMapImageScpCfgPages_function_00294FA4.md) (function, `0x00294FA4`)
- `0x0097F4DC` → [MiLogMapFileEvent](MiLogMapFileEvent_function_0097E0FC.md) (function, `0x0097E0FC`)
- `0x0097F57F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0097F5E0` → [MiArbitraryCodeBlocked](MiArbitraryCodeBlocked_function_0097D7CC.md) (function, `0x0097D7CC`)
- `0x0097F64D` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (function, `0x0048FDC0`)
- `0x0097F745` → [MiDereferenceControlArea](../../text/47/MiDereferenceControlArea_function_00479A20.md) (function, `0x00479A20`)
- `0x0097F7E6` → [MiInitializeFixupVad](../9E/MiInitializeFixupVad_function_009E5528.md) (function, `0x009E5528`)
- `0x0097F806` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0097F810` → [MiCreatePerSessionProtos](../A6/MiCreatePerSessionProtos_function_00A666D8.md) (function, `0x00A666D8`)
- `0x0097F836` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0097F840` → [MiDereferencePerSessionProtos](../A2/MiDereferencePerSessionProtos_function_00A2EDE8.md) (function, `0x00A2EDE8`)
- `0x0097F862` → [MiReferenceActiveSubsection](../../text/32/MiReferenceActiveSubsection_function_00325060.md) (function, `0x00325060`)
- `0x0097F87E` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (function, `0x00295810`)
- `0x0097F88E` → [MiMapUserLargePages](../../text/3D/MiMapUserLargePages_function_003D26F4.md) (function, `0x003D26F4`)
- `0x0097F8A5` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x0097F8F7` → [MiUpdatePrivateDemandZeroView](../../text/4C/MiUpdatePrivateDemandZeroView_function_004CCC2C.md) (function, `0x004CCC2C`)
- `0x0097F903` → [MiRemoveVadEvent](../../text/67/MiRemoveVadEvent_function_0067E41C.md) (function, `0x0067E41C`)
- `0x0097F94F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0097F964` → [MiSoftFaultMappedView](../../text/36/MiSoftFaultMappedView_function_00365364.md) (function, `0x00365364`)

### Direct callers
- [MiFinalizeLagePageImageMapping](../7F/MiFinalizeLagePageImageMapping_function_007FE454.md) at `0x007FE4A1`
- [MiMapImageInSystemProcess](../7F/MiMapImageInSystemProcess_function_007FE4F8.md) at `0x007FE5F4`
- [MiMapViewOfSection](../89/MiMapViewOfSection_function_00898F10.md) at `0x00899356`

### Static image references
- `0x0097E99E` → RVA `0x00E2D878` (`.data`; read)
- `0x0097EA9E` → RVA `0x00E2D8AC` (`.data`; read)
- `0x0097EB66` → RVA `0x00FC6CB8` (`ALMOSTRO`; read)
- `0x0097EED1` → RVA `0x00FC6B00` (`ALMOSTRO`; read)
- `0x0097EEFF` → RVA `0x00FC42C0` (`.data`; read)
- `0x0097F0B2` → RVA `0x00E2DB80` (`.data`; read)
- `0x0097F5F2` → RVA `0x00E2D87C` (`.data`; read)
- `0x0097F602` → RVA `0x00E2D880` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **32**
  - `0x0097E972` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0097EBA4` → [MiCheckPurgeAndUpMapCount](../../text/41/MiCheckPurgeAndUpMapCount_function_004186B0.md) (`PAGE` → `.text`)
  - `0x0097EBC2` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x0097ECC4` → [MiWriteVadFlags2](../../text/41/MiWriteVadFlags2_function_0041C020.md) (`PAGE` → `.text`)
  - `0x0097ECEA` → [LOCK_ADDRESS_SPACE](../../text/2A/LOCK_ADDRESS_SPACE_function_002A4944.md) (`PAGE` → `.text`)
  - `0x0097ED88` → [MiUpdateVadStartVpn](../../text/45/MiUpdateVadStartVpn_function_00450ED4.md) (`PAGE` → `.text`)
  - `0x0097EE3D` → [MiControlAreaRequiresCharge](../../text/3B/MiControlAreaRequiresCharge_function_003B36CC.md) (`PAGE` → `.text`)
  - `0x0097EE7A` → [MiInsertVad](../../text/26/MiInsertVad_function_00265540.md) (`PAGE` → `.text`)
  - `0x0097EF17` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (`PAGE` → `.text`)
  - `0x0097EF56` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x0097F011` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (`PAGE` → `.text`)
  - `0x0097F01E` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x0097F029` → [MiReadVadFlags2](../../text/45/MiReadVadFlags2_function_00452C1C.md) (`PAGE` → `.text`)
  - `0x0097F078` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (`PAGE` → `.text`)
  - `0x0097F09C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0097F173` → [MiReferenceControlAreaFile](../../text/43/MiReferenceControlAreaFile_function_00431554.md) (`PAGE` → `.text`)
  - `0x0097F324` → [ExGenRandom](../../text/41/ExGenRandom_function_0041B010.md) (`PAGE` → `.text`)
  - `0x0097F38B` → [MiReferenceVad](../../text/29/MiReferenceVad_function_00295890.md) (`PAGE` → `.text`)
  - `0x0097F465` → [MiMapImageScpCfgPages](../../text/29/MiMapImageScpCfgPages_function_00294FA4.md) (`PAGE` → `.text`)
  - `0x0097F57F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x0097F64D` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (`PAGE` → `.text`)
  - `0x0097F745` → [MiDereferenceControlArea](../../text/47/MiDereferenceControlArea_function_00479A20.md) (`PAGE` → `.text`)
  - `0x0097F806` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0097F836` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0097F862` → [MiReferenceActiveSubsection](../../text/32/MiReferenceActiveSubsection_function_00325060.md) (`PAGE` → `.text`)
  - `0x0097F87E` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (`PAGE` → `.text`)
  - `0x0097F88E` → [MiMapUserLargePages](../../text/3D/MiMapUserLargePages_function_003D26F4.md) (`PAGE` → `.text`)
  - `0x0097F8A5` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x0097F8F7` → [MiUpdatePrivateDemandZeroView](../../text/4C/MiUpdatePrivateDemandZeroView_function_004CCC2C.md) (`PAGE` → `.text`)
  - `0x0097F903` → [MiRemoveVadEvent](../../text/67/MiRemoveVadEvent_function_0067E41C.md) (`PAGE` → `.text`)
  - `0x0097F94F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0097F964` → [MiSoftFaultMappedView](../../text/36/MiSoftFaultMappedView_function_00365364.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **25**
  - `0x0097ECB3` → [sub_00B2A146 + 0x3E](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097EE06` → [sub_00B2A146 + 0x1A9](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F1D1` → [sub_00B2A146 + 0x1B](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F1F0` → [sub_00B2A146 + 0x1B](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F2F0` → [sub_00B2A146 + 0xA8](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F319` → [sub_00B2A146 + 0x11F](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F343` → [sub_00B2A146 + 0x11F](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F3DA` → [sub_00B2A146 + 0x218](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F3E9` → [sub_00B2A146 + 0x218](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F3F3` → [sub_00B2A146 + 0x218](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F48D` → [sub_00B2A146 + 0xA8](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F58A` → [sub_00B2A146 + 0x140](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F654` → [sub_00B2A146](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F6AD` → [sub_00B2A146 + 0x2C](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F6FA` → [sub_00B2A146 + 0x36](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F709` → [sub_00B2A146 + 0x2C](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F799` → [sub_00B2A146 + 0x113](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F82D` → [sub_00B2A146 + 0x2C6](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F846` → [sub_00B2A146 + 0x2C6](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F89C` → [sub_00B2A146 + 0x209](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F8BB` → [sub_00B2A146 + 0x22F](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F8D5` → [sub_00B2A146 + 0x22F](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F91D` → [sub_00B2A146 + 0x282](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F92A` → [sub_00B2A146 + 0x282](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)
  - `0x0097F937` → [sub_00B2A146 + 0x282](../B2/Unknown_function_00B2A146.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0097E92C  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0097E931  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0097E936  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0097E93B  55                              push rbp
0097E93C  53                              push rbx
0097E93D  56                              push rsi
0097E93E  57                              push rdi
0097E93F  41 54                           push r12
0097E941  41 55                           push r13
0097E943  41 56                           push r14
0097E945  41 57                           push r15
0097E947  48 8D 6C 24 88                  lea rbp, [rsp - 0x78]
0097E94C  48 81 EC 78 01 00 00            sub rsp, 0x178
0097E953  33 DB                           xor ebx, ebx
0097E955  4C 8B E2                        mov r12, rdx
0097E958  48 8B F1                        mov rsi, rcx
0097E95B  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0097E960  33 D2                           xor edx, edx
0097E962  48 89 5D A8                     mov qword ptr [rbp - 0x58], rbx
0097E966  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0097E96A  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
0097E96E  44 8D 43 58                     lea r8d, [rbx + 0x58]
0097E972  E8 C9 82 D4 FF                  call 0x1406c6c40
0097E977  4C 8B 1E                        mov r11, qword ptr [rsi]
0097E97A  0F 57 C0                        xorps xmm0, xmm0
0097E97D  41 8B 54 24 28                  mov edx, dword ptr [r12 + 0x28]
0097E982  33 C0                           xor eax, eax
0097E984  4C 8B 76 60                     mov r14, qword ptr [rsi + 0x60]
0097E988  44 8B FB                        mov r15d, ebx
0097E98B  4D 8B 6C 24 58                  mov r13, qword ptr [r12 + 0x58]
0097E990  49 83 E6 F8                     and r14, 0xfffffffffffffff8
0097E994  C1 EA 16                        shr edx, 0x16
0097E997  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0097E99B  83 E2 02                        and edx, 2
0097E99E  8B 05 D4 EE 4A 00               mov eax, dword ptr [rip + 0x4aeed4]
0097E9A4  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
0097E9A8  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
0097E9AD  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
0097E9B1  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0097E9B5  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
0097E9B9  4D 8B 4B 38                     mov r9, qword ptr [r11 + 0x38]
0097E9BD  4C 89 4D B8                     mov qword ptr [rbp - 0x48], r9
0097E9C1  85 C0                           test eax, eax
0097E9C3  0F 85 29 0C 00 00               jne 0x14097f5f2
0097E9C9  F7 46 38 00 00 00 20            test dword ptr [rsi + 0x38], 0x20000000
0097E9D0  49 8B 43 30                     mov rax, qword ptr [r11 + 0x30]
0097E9D4  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
0097E9D8  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0097E9DC  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
0097E9E0  0F 85 35 0C 00 00               jne 0x14097f61b
0097E9E6  41 F7 85 FC 05 00 00 00 20 00 00  test dword ptr [r13 + 0x5fc], 0x2000
0097E9F1  8B DA                           mov ebx, edx
0097E9F3  0F 85 22 0C 00 00               jne 0x14097f61b
0097E9F9  41 0F B7 54 24 3A               movzx edx, word ptr [r12 + 0x3a]
0097E9FF  41 0F B7 8D EC 06 00 00         movzx ecx, word ptr [r13 + 0x6ec]
0097EA07  44 0F B7 C2                     movzx r8d, dx
0097EA0B  66 89 4D 90                     mov word ptr [rbp - 0x70], cx
0097EA0F  66 89 95 C8 00 00 00            mov word ptr [rbp + 0xc8], dx
0097EA16  66 85 D2                        test dx, dx
0097EA19  0F 84 D6 07 00 00               je 0x14097f1f5
0097EA1F  41 0F B7 49 30                  movzx ecx, word ptr [r9 + 0x30]
0097EA24  66 44 3B C1                     cmp r8w, cx
0097EA28  0F 85 1F 0C 00 00               jne 0x14097f64d
0097EA2E  B9 04 00 00 00                  mov ecx, 4
0097EA33  41 F6 85 70 01 00 00 01         test byte ptr [r13 + 0x170], 1
0097EA3B  0F 85 2E 0C 00 00               jne 0x14097f66f
0097EA41  4D 8B 44 24 10                  mov r8, qword ptr [r12 + 0x10]
0097EA46  48 B8 00 00 00 00 01 00 00 00   movabs rax, 0x100000000
0097EA50  4D 8B 54 24 18                  mov r10, qword ptr [r12 + 0x18]
0097EA55  41 8B 54 24 28                  mov edx, dword ptr [r12 + 0x28]
0097EA5A  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
0097EA5E  4C 89 55 88                     mov qword ptr [rbp - 0x78], r10
0097EA62  0F BA E2 1D                     bt edx, 0x1d
0097EA66  0F 82 1C 0C 00 00               jb 0x14097f688
0097EA6C  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
0097EA73  48 85 C0                        test rax, rax
0097EA76  74 15                           je 0x14097ea8d
0097EA78  F7 40 38 00 00 08 00            test dword ptr [rax + 0x38], 0x80000
0097EA7F  0F 94 C1                        sete cl
0097EA82  0F BA E2 12                     bt edx, 0x12
0097EA86  0F 93 C0                        setae al
0097EA89  84 C8                           test al, cl
0097EA8B  75 11                           jne 0x14097ea9e
0097EA8D  83 BD F0 00 00 00 01            cmp dword ptr [rbp + 0xf0], 1
0097EA94  0F 85 3A 0C 00 00               jne 0x14097f6d4
0097EA9A  0F BA EB 0A                     bts ebx, 0xa
0097EA9E  8B 05 08 EE 4A 00               mov eax, dword ptr [rip + 0x4aee08]
0097EAA4  33 C9                           xor ecx, ecx
0097EAA6  4D 8B 4B 38                     mov r9, qword ptr [r11 + 0x38]
0097EAAA  8B F9                           mov edi, ecx
0097EAAC  8B D0                           mov edx, eax
0097EAAE  85 C0                           test eax, eax
0097EAB0  74 7B                           je 0x14097eb2d
0097EAB2  41 F6 41 4C 40                  test byte ptr [r9 + 0x4c], 0x40
0097EAB7  0F 95 C1                        setne cl
0097EABA  0F BA E3 0A                     bt ebx, 0xa
0097EABE  0F 93 C0                        setae al
0097EAC1  84 C8                           test al, cl
0097EAC3  74 68                           je 0x14097eb2d
0097EAC5  49 81 F8 00 00 20 00            cmp r8, 0x200000
0097EACC  74 5F                           je 0x14097eb2d
0097EACE  49 F7 C2 FF 0F 00 00            test r10, 0xfff
0097EAD5  8B CF                           mov ecx, edi
0097EAD7  49 8B C2                        mov rax, r10
0097EADA  44 8B C7                        mov r8d, edi
0097EADD  0F 95 C1                        setne cl
0097EAE0  48 C1 E8 0C                     shr rax, 0xc
0097EAE4  48 03 C8                        add rcx, rax
0097EAE7  41 8B 43 08                     mov eax, dword ptr [r11 + 8]
0097EAEB  48 3B C8                        cmp rcx, rax
0097EAEE  0F 85 C0 06 00 00               jne 0x14097f1b4
0097EAF4  B9 04 00 00 00                  mov ecx, 4
0097EAF9  41 84 8D DC 07 00 00            test byte ptr [r13 + 0x7dc], cl
0097EB00  0F 94 C1                        sete cl
0097EB03  F6 85 F8 00 00 00 10            test byte ptr [rbp + 0xf8], 0x10
0097EB0A  0F 94 C0                        sete al
0097EB0D  84 C8                           test al, cl
0097EB0F  0F 84 9F 06 00 00               je 0x14097f1b4
0097EB15  4A 8D 04 12                     lea rax, [rdx + r10]
0097EB19  49 3B C2                        cmp rax, r10
0097EB1C  0F 82 BC 0B 00 00               jb 0x14097f6de
0097EB22  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0097EB26  BF 20 00 00 00                  mov edi, 0x20
0097EB2B  EB 03                           jmp 0x14097eb30
0097EB2D  45 33 C0                        xor r8d, r8d
0097EB30  81 FB 00 04 00 00               cmp ebx, 0x400
0097EB36  0F 82 E0 06 00 00               jb 0x14097f21c
0097EB3C  41 B9 04 00 00 00               mov r9d, 4
0097EB42  0F BA E3 0A                     bt ebx, 0xa
0097EB46  0F 82 D1 0B 00 00               jb 0x14097f71d
0097EB4C  66 41 0F BA 63 0C 0E            bt word ptr [r11 + 0xc], 0xe
0097EB53  0F 82 B5 0B 00 00               jb 0x14097f70e
0097EB59  44 84 8D F8 00 00 00            test byte ptr [rbp + 0xf8], r9b
0097EB60  0F 85 C2 0B 00 00               jne 0x14097f728
0097EB66  4C 3B 2D 4B 81 64 00            cmp r13, qword ptr [rip + 0x64814b]
0097EB6D  0F 84 B5 0B 00 00               je 0x14097f728
0097EB73  4D 39 46 20                     cmp qword ptr [r14 + 0x20], r8
0097EB77  0F 84 F2 08 00 00               je 0x14097f46f
0097EB7D  0F BA 66 38 0B                  bt dword ptr [rsi + 0x38], 0xb
0097EB82  0F 82 E7 08 00 00               jb 0x14097f46f
0097EB88  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
0097EB8C  0F BA E3 0A                     bt ebx, 0xa
0097EB90  0F 83 25 0A 00 00               jae 0x14097f5bb
0097EB96  48 8D 86 80 00 00 00            lea rax, [rsi + 0x80]
0097EB9D  48 8B CE                        mov rcx, rsi
0097EBA0  48 89 45 00                     mov qword ptr [rbp], rax
0097EBA4  E8 07 9B A9 FF                  call 0x1404186b0
0097EBA9  45 85 FF                        test r15d, r15d
0097EBAC  0F 85 DF 03 00 00               jne 0x14097ef91
0097EBB2  BA 88 00 00 00                  mov edx, 0x88
0097EBB7  41 B8 56 61 64 20               mov r8d, 0x20646156
0097EBBD  B9 40 00 00 00                  mov ecx, 0x40
0097EBC2  E8 79 C9 9D FF                  call 0x14035b540
0097EBC7  4C 8B F0                        mov r14, rax
0097EBCA  48 85 C0                        test rax, rax
0097EBCD  0F 84 6F 0B 00 00               je 0x14097f742
0097EBD3  45 85 FF                        test r15d, r15d
0097EBD6  0F 85 78 0B 00 00               jne 0x14097f754
0097EBDC  48 8B B5 E0 00 00 00            mov rsi, qword ptr [rbp + 0xe0]
0097EBE3  45 33 FF                        xor r15d, r15d
0097EBE6  83 BD E8 00 00 00 01            cmp dword ptr [rbp + 0xe8], 1
0097EBED  48 C7 C0 FE FF FF FF            mov rax, 0xfffffffffffffffe
0097EBF4  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
0097EBF8  49 89 06                        mov qword ptr [r14], rax
0097EBFB  49 89 46 08                     mov qword ptr [r14 + 8], rax
0097EBFF  41 8D 4F 04                     lea ecx, [r15 + 4]
0097EC03  41 8B C7                        mov eax, r15d
0097EC06  0F 44 C1                        cmove eax, ecx
0097EC09  41 8B 4E 30                     mov ecx, dword ptr [r14 + 0x30]
0097EC0D  0B F8                           or edi, eax
0097EC0F  83 E1 AF                        and ecx, 0xffffffaf
0097EC12  83 C9 20                        or ecx, 0x20
0097EC15  41 89 4E 30                     mov dword ptr [r14 + 0x30], ecx
0097EC19  41 8B 44 24 34                  mov eax, dword ptr [r12 + 0x34]
0097EC1E  C1 E0 0C                        shl eax, 0xc
0097EC21  33 C1                           xor eax, ecx
0097EC23  25 00 F0 07 00                  and eax, 0x7f000
0097EC28  33 C1                           xor eax, ecx
0097EC2A  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
0097EC2E  48 85 F6                        test rsi, rsi
0097EC31  74 19                           je 0x14097ec4c
0097EC33  48 8B CE                        mov rcx, rsi
0097EC36  E8 C5 6F F0 FF                  call 0x140885c00
0097EC3B  49 89 86 80 00 00 00            mov qword ptr [r14 + 0x80], rax
0097EC42  44 39 7E 3C                     cmp dword ptr [rsi + 0x3c], r15d
0097EC46  0F 8C 10 0B 00 00               jl 0x14097f75c
0097EC4C  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
0097EC50  8B CF                           mov ecx, edi
0097EC52  25 FF F0 FF FF                  and eax, 0xfffff0ff
0097EC57  4D 89 7E 28                     mov qword ptr [r14 + 0x28], r15
0097EC5B  0F BA E8 07                     bts eax, 7
0097EC5F  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
0097EC63  0F BA E3 0A                     bt ebx, 0xa
0097EC67  0F 83 3A 08 00 00               jae 0x14097f4a7
0097EC6D  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
0097EC76  41 8B 44 24 3C                  mov eax, dword ptr [r12 + 0x3c]
0097EC7B  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0097EC7F  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
0097EC84  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
0097EC89  A8 01                           test al, 1
0097EC8B  0F 85 D3 0A 00 00               jne 0x14097f764
0097EC91  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0097EC98  44 8B 38                        mov r15d, dword ptr [rax]
0097EC9B  4C 03 7D A0                     add r15, qword ptr [rbp - 0x60]
0097EC9F  49 8B C7                        mov rax, r15
0097ECA2  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0097ECA7  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0097ECAC  48 81 F9 00 00 20 00            cmp rcx, 0x200000
0097ECB3  0F 84 CB B4 1A 00               je 0x140b2a184
0097ECB9  41 B8 01 00 00 00               mov r8d, 1
0097ECBF  8B D7                           mov edx, edi
0097ECC1  49 8B CE                        mov rcx, r14
0097ECC4  E8 57 D3 A9 FF                  call 0x14041c020
0097ECC9  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
0097ECCD  25 80 0F 00 00                  and eax, 0xf80
0097ECD2  3D 80 03 00 00                  cmp eax, 0x380
0097ECD7  0F 84 F8 03 00 00               je 0x14097f0d5
0097ECDD  49 8B D5                        mov rdx, r13
0097ECE0  C7 45 60 20 00 00 00            mov dword ptr [rbp + 0x60], 0x20
0097ECE7  48 8B CE                        mov rcx, rsi
0097ECEA  E8 55 5C 92 FF                  call 0x1402a4944
0097ECEF  41 8B 85 F4 01 00 00            mov eax, dword ptr [r13 + 0x1f4]
0097ECF6  A8 20                           test al, 0x20
0097ECF8  0F 85 8C 0A 00 00               jne 0x14097f78a
0097ECFE  41 8B 44 24 3C                  mov eax, dword ptr [r12 + 0x3c]
0097ED03  A8 01                           test al, 1
0097ED05  0F 84 B2 02 00 00               je 0x14097efbd
0097ED0B  48 81 7D 80 00 00 20 00         cmp qword ptr [rbp - 0x80], 0x200000
0097ED13  0F 84 A4 02 00 00               je 0x14097efbd
0097ED19  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0097ED1E  49 8B D7                        mov rdx, r15
0097ED21  4D 8B 0C 24                     mov r9, qword ptr [r12]
0097ED25  49 8B CD                        mov rcx, r13
0097ED28  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
0097ED2C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0097ED31  E8 5A 10 00 00                  call 0x14097fd90
0097ED36  85 C0                           test eax, eax
0097ED38  0F 84 60 0A 00 00               je 0x14097f79e
0097ED3E  4C 8B 85 D8 00 00 00            mov r8, qword ptr [rbp + 0xd8]
0097ED45  4D 8B FE                        mov r15, r14
0097ED48  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0097ED4D  48 8B CA                        mov rcx, rdx
0097ED50  41 8B 00                        mov eax, dword ptr [r8]
0097ED53  48 2B C8                        sub rcx, rax
0097ED56  48 3B 4D A0                     cmp rcx, qword ptr [rbp - 0x60]
0097ED5A  0F 85 D6 07 00 00               jne 0x14097f536
0097ED60  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
0097ED65  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0097ED69  48 8B CA                        mov rcx, rdx
0097ED6C  48 C1 E9 0C                     shr rcx, 0xc
0097ED70  48 FF C8                        dec rax
0097ED73  48 03 C2                        add rax, rdx
0097ED76  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
0097ED7A  48 8B D1                        mov rdx, rcx
0097ED7D  48 C1 E8 0C                     shr rax, 0xc
0097ED81  49 8B CF                        mov rcx, r15
0097ED84  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0097ED88  E8 47 21 AD FF                  call 0x140450ed4
0097ED8D  48 8B 55 00                     mov rdx, qword ptr [rbp]
0097ED91  41 89 47 1C                     mov dword ptr [r15 + 0x1c], eax
0097ED95  48 C1 E8 20                     shr rax, 0x20
0097ED99  41 88 47 21                     mov byte ptr [r15 + 0x21], al
0097ED9D  49 8B 08                        mov rcx, qword ptr [r8]
0097EDA0  48 C1 E9 0C                     shr rcx, 0xc
0097EDA4  8B 42 2C                        mov eax, dword ptr [rdx + 0x2c]
0097EDA7  48 3B C8                        cmp rcx, rax
0097EDAA  0F 83 15 0A 00 00               jae 0x14097f7c5
0097EDB0  49 89 57 48                     mov qword ptr [r15 + 0x48], rdx
0097EDB4  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0097EDB8  48 8D 0C C8                     lea rcx, [rax + rcx*8]
0097EDBC  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0097EDC1  49 89 4F 50                     mov qword ptr [r15 + 0x50], rcx
0097EDC5  8B 48 08                        mov ecx, dword ptr [rax + 8]
0097EDC8  48 8B 40 40                     mov rax, qword ptr [rax + 0x40]
0097EDCC  48 FF C9                        dec rcx
0097EDCF  48 8D 0C C8                     lea rcx, [rax + rcx*8]
0097EDD3  49 89 4F 58                     mov qword ptr [r15 + 0x58], rcx
0097EDD7  F6 C3 08                        test bl, 8
0097EDDA  0F 85 F1 09 00 00               jne 0x14097f7d1
0097EDE0  33 C0                           xor eax, eax
0097EDE2  41 39 44 24 34                  cmp dword ptr [r12 + 0x34], eax
0097EDE7  0F 85 03 0A 00 00               jne 0x14097f7f0
0097EDED  4C 8B B5 C0 00 00 00            mov r14, qword ptr [rbp + 0xc0]
0097EDF4  41 F7 46 38 00 00 00 08         test dword ptr [r14 + 0x38], 0x8000000
0097EDFC  0F 85 01 0A 00 00               jne 0x14097f803
0097EE02  40 F6 C7 10                     test dil, 0x10
0097EE06  0F 85 E3 B4 1A 00               jne 0x140b2a2ef
0097EE0C  45 33 C0                        xor r8d, r8d
0097EE0F  49 8B D5                        mov rdx, r13
0097EE12  49 8B CE                        mov rcx, r14
0097EE15  E8 F6 83 F0 FF                  call 0x140887210
0097EE1A  45 33 C9                        xor r9d, r9d
0097EE1D  8B F0                           mov esi, eax
0097EE1F  85 C0                           test eax, eax
0097EE21  0F 88 02 0A 00 00               js 0x14097f829
0097EE27  8B B5 F8 00 00 00               mov esi, dword ptr [rbp + 0xf8]
0097EE2D  41 8B D1                        mov edx, r9d
0097EE30  0F BA EB 07                     bts ebx, 7
0097EE34  49 8B CE                        mov rcx, r14
0097EE37  83 E6 08                        and esi, 8
0097EE3A  0F 95 C2                        setne dl
0097EE3D  E8 8A 48 A3 FF                  call 0x1403b36cc
0097EE42  85 C0                           test eax, eax
0097EE44  0F 84 DA 09 00 00               je 0x14097f824
0097EE4A  83 F8 02                        cmp eax, 2
0097EE4D  0F 84 F8 09 00 00               je 0x14097f84b
0097EE53  49 8B D5                        mov rdx, r13
0097EE56  49 8B CF                        mov rcx, r15
0097EE59  E8 4A 7C F0 FF                  call 0x140886aa8
0097EE5E  8B F0                           mov esi, eax
0097EE60  85 C0                           test eax, eax
0097EE62  0F 88 C1 09 00 00               js 0x14097f829
0097EE68  F6 C3 08                        test bl, 8
0097EE6B  0F 85 75 06 00 00               jne 0x14097f4e6
0097EE71  45 33 C0                        xor r8d, r8d
0097EE74  49 8B D5                        mov rdx, r13
0097EE77  49 8B CF                        mov rcx, r15
0097EE7A  E8 C1 66 8E FF                  call 0x140265540
0097EE7F  33 F6                           xor esi, esi
0097EE81  48 81 7D 80 00 00 20 00         cmp qword ptr [rbp - 0x80], 0x200000
0097EE89  44 8B F6                        mov r14d, esi
0097EE8C  0F 84 E4 09 00 00               je 0x14097f876
0097EE92  4C 8B 45 A8                     mov r8, qword ptr [rbp - 0x58]
0097EE96  4D 85 C0                        test r8, r8
0097EE99  0F 85 24 02 00 00               jne 0x14097f0c3
0097EE9F  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0097EEA4  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0097EEA8  48 C1 E1 10                     shl rcx, 0x10
0097EEAC  48 03 C1                        add rax, rcx
0097EEAF  48 8B 8D D0 00 00 00            mov rcx, qword ptr [rbp + 0xd0]
0097EEB6  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0097EEBB  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0097EEC0  48 89 01                        mov qword ptr [rcx], rax
0097EEC3  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
0097EEC7  40 38 70 32                     cmp byte ptr [rax + 0x32], sil
0097EECB  0F 85 EA 04 00 00               jne 0x14097f3bb
0097EED1  F7 05 25 7C 64 00 00 80 00 00   test dword ptr [rip + 0x647c25], 0x8000
0097EEDB  0F 85 F3 05 00 00               jne 0x14097f4d4
0097EEE1  48 8B B5 C0 00 00 00            mov rsi, qword ptr [rbp + 0xc0]
0097EEE8  40 F6 C7 20                     test dil, 0x20
0097EEEC  0F 85 5D 05 00 00               jne 0x14097f44f
0097EEF2  83 CB 10                        or ebx, 0x10
0097EEF5  0F BA E3 0A                     bt ebx, 0xa
0097EEF9  0F 82 E5 09 00 00               jb 0x14097f8e4
0097EEFF  F7 05 B7 53 64 00 00 00 04 00   test dword ptr [rip + 0x6453b7], 0x40000
0097EF09  0F 85 A0 09 00 00               jne 0x14097f8af
0097EF0F  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0097EF14  49 8B CF                        mov rcx, r15
0097EF17  E8 00 3D AD FF                  call 0x140452c1c
0097EF1C  41 B9 00 08 00 00               mov r9d, 0x800
0097EF22  8B F8                           mov edi, eax
0097EF24  41 85 D9                        test r9d, ebx
0097EF27  0F 85 EC 01 00 00               jne 0x14097f119
0097EF2D  33 F6                           xor esi, esi
0097EF2F  41 39 74 24 78                  cmp dword ptr [r12 + 0x78], esi
0097EF34  0F 84 BE 04 00 00               je 0x14097f3f8
0097EF3A  83 CB 20                        or ebx, 0x20
0097EF3D  F6 C3 20                        test bl, 0x20
0097EF40  0F 85 C3 00 00 00               jne 0x14097f009
0097EF46  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
0097EF4B  F6 C3 10                        test bl, 0x10
0097EF4E  74 0B                           je 0x14097ef5b
0097EF50  49 8B D5                        mov rdx, r13
0097EF53  49 8B CF                        mov rcx, r15
0097EF56  E8 E9 58 92 FF                  call 0x1402a4844
0097EF5B  0F BA E3 0A                     bt ebx, 0xa
0097EF5F  72 17                           jb 0x14097ef78
0097EF61  48 39 B5 E0 00 00 00            cmp qword ptr [rbp + 0xe0], rsi
0097EF68  74 0E                           je 0x14097ef78
0097EF6A  41 F6 85 70 01 00 00 01         test byte ptr [r13 + 0x170], 1
0097EF72  0F 84 F6 09 00 00               je 0x14097f96e
0097EF78  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0097EF7C  48 81 C4 78 01 00 00            add rsp, 0x178
0097EF83  41 5F                           pop r15
0097EF85  41 5E                           pop r14
0097EF87  41 5D                           pop r13
0097EF89  41 5C                           pop r12
0097EF8B  5F                              pop rdi
0097EF8C  5E                              pop rsi
0097EF8D  5B                              pop rbx
0097EF8E  5D                              pop rbp
0097EF8F  C3                              ret
0097EF90  CC                              int3
0097EF91  48 8B 06                        mov rax, qword ptr [rsi]
0097EF94  41 B8 56 61 64 49               mov r8d, 0x49646156
0097EF9A  8B 48 08                        mov ecx, dword ptr [rax + 8]
0097EF9D  8B C1                           mov eax, ecx
0097EF9F  24 3F                           and al, 0x3f
0097EFA1  F6 D8                           neg al
0097EFA3  48 1B D2                        sbb rdx, rdx
0097EFA6  48 C1 E9 06                     shr rcx, 6
0097EFAA  48 F7 DA                        neg rdx
0097EFAD  48 83 C2 15                     add rdx, 0x15
0097EFB1  48 03 D1                        add rdx, rcx
0097EFB4  48 C1 E2 03                     shl rdx, 3
0097EFB8  E9 00 FC FF FF                  jmp 0x14097ebbd
0097EFBD  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0097EFC1  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
0097EFCB  48 3B F0                        cmp rsi, rax
0097EFCE  0F 87 BD 07 00 00               ja 0x14097f791
0097EFD4  F6 C3 01                        test bl, 1
0097EFD7  0F 85 7E 02 00 00               jne 0x14097f25b
0097EFDD  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0097EFE2  4C 8B C6                        mov r8, rsi
0097EFE5  4D 8B 0C 24                     mov r9, qword ptr [r12]
0097EFE9  49 8B D7                        mov rdx, r15
0097EFEC  49 8B CD                        mov rcx, r13
0097EFEF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0097EFF4  E8 97 0D 00 00                  call 0x14097fd90
0097EFF9  45 33 C9                        xor r9d, r9d
0097EFFC  85 C0                           test eax, eax
0097EFFE  0F 85 3A FD FF FF               jne 0x14097ed3e
0097F004  E9 55 02 00 00                  jmp 0x14097f25e
0097F009  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0097F00E  49 8B D7                        mov rdx, r15
0097F011  E8 FA 67 91 FF                  call 0x140295810
0097F016  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0097F01B  49 8B D5                        mov rdx, r13
0097F01E  E8 21 58 92 FF                  call 0x1402a4844
0097F023  49 8B CF                        mov rcx, r15
0097F026  83 E3 EF                        and ebx, 0xffffffef
0097F029  E8 EE 3B AD FF                  call 0x140452c1c
0097F02E  A8 10                           test al, 0x10
0097F030  0F 85 B5 08 00 00               jne 0x14097f8eb
0097F036  33 FF                           xor edi, edi
0097F038  0F BA E3 0A                     bt ebx, 0xa
0097F03C  0F 83 4B 01 00 00               jae 0x14097f18d
0097F042  49 39 7C 24 48                  cmp qword ptr [r12 + 0x48], rdi
0097F047  0F 85 C3 08 00 00               jne 0x14097f910
0097F04D  48 8B 7D C0                     mov rdi, qword ptr [rbp - 0x40]
0097F051  8B F3                           mov esi, ebx
0097F053  B8 00 08 00 00                  mov eax, 0x800
0097F058  23 F0                           and esi, eax
0097F05A  0F 85 E8 02 00 00               jne 0x14097f348
0097F060  41 8B 44 24 40                  mov eax, dword ptr [r12 + 0x40]
0097F065  A8 02                           test al, 2
0097F067  0F 85 F4 08 00 00               jne 0x14097f961
0097F06D  49 8B D7                        mov rdx, r15
0097F070  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
0097F075  49 8B CF                        mov rcx, r15
0097F078  E8 4B 69 92 FF                  call 0x1402a59c8
0097F07D  85 F6                           test esi, esi
0097F07F  74 20                           je 0x14097f0a1
0097F081  49 8D 4E 58                     lea rcx, [r14 + 0x58]
0097F085  4D 8B CE                        mov r9, r14
0097F088  4C 8D 45 C8                     lea r8, [rbp - 0x38]
0097F08C  49 8B D5                        mov rdx, r13
0097F08F  E8 8C 7B F5 FF                  call 0x1408d6c20
0097F094  BA 4D 6D 53 63                  mov edx, 0x63536d4d
0097F099  49 8B CE                        mov rcx, r14
0097F09C  E8 3F 88 97 FF                  call 0x1402f78e0
0097F0A1  33 F6                           xor esi, esi
0097F0A3  48 85 FF                        test rdi, rdi
0097F0A6  0F 84 9F FE FF FF               je 0x14097ef4b
0097F0AC  49 8B CD                        mov rcx, r13
0097F0AF  48 33 CF                        xor rcx, rdi
0097F0B2  48 33 0D C7 EA 4A 00            xor rcx, qword ptr [rip + 0x4aeac7]
0097F0B9  E8 E2 B1 F0 FF                  call 0x14088a2a0
0097F0BE  E9 88 FE FF FF                  jmp 0x14097ef4b
0097F0C3  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
0097F0C7  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
0097F0CB  E8 70 7B F0 FF                  call 0x140886c40
0097F0D0  E9 CA FD FF FF                  jmp 0x14097ee9f
0097F0D5  33 D2                           xor edx, edx
0097F0D7  49 39 95 D0 01 00 00            cmp qword ptr [r13 + 0x1d0], rdx
0097F0DE  0F 84 F9 FB FF FF               je 0x14097ecdd
0097F0E4  41 F7 85 FC 05 00 00 00 10 00 00  test dword ptr [r13 + 0x5fc], 0x1000
0097F0EF  0F 85 E8 FB FF FF               jne 0x14097ecdd
0097F0F5  41 F6 85 70 01 00 00 01         test byte ptr [r13 + 0x170], 1
0097F0FD  0F 85 DA FB FF FF               jne 0x14097ecdd
0097F103  E8 D8 0C 00 00                  call 0x14097fde0
0097F108  84 C0                           test al, al
0097F10A  0F 84 CD FB FF FF               je 0x14097ecdd
0097F110  0F BA EB 0B                     bts ebx, 0xb
0097F114  E9 C4 FB FF FF                  jmp 0x14097ecdd
0097F119  C6 45 D0 03                     mov byte ptr [rbp - 0x30], 3
0097F11D  40 F6 C7 08                     test dil, 8
0097F121  0F 84 F8 02 00 00               je 0x14097f41f
0097F127  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
0097F12A  81 E2 FF 0F F8 FF               and edx, 0xfff80fff
0097F130  8B C3                           mov eax, ebx
0097F132  D1 E8                           shr eax, 1
0097F134  33 C2                           xor eax, edx
0097F136  41 23 C1                        and eax, r9d
0097F139  33 C2                           xor eax, edx
0097F13B  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0097F13E  48 83 C9 FF                     or rcx, 0xffffffffffffffff
0097F142  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0097F147  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0097F14B  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
0097F150  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0097F154  48 8B C1                        mov rax, rcx
0097F157  F0 49 0F B1 48 18               lock cmpxchg qword ptr [r8 + 0x18], rcx
0097F15D  49 39 44 24 18                  cmp qword ptr [r12 + 0x18], rax
0097F162  0F 85 72 07 00 00               jne 0x14097f8da
0097F168  33 C0                           xor eax, eax
0097F16A  48 8B CE                        mov rcx, rsi
0097F16D  89 45 E0                        mov dword ptr [rbp - 0x20], eax
0097F170  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0097F173  E8 DC 23 AB FF                  call 0x140431554
0097F178  4C 8B F0                        mov r14, rax
0097F17B  83 CB 20                        or ebx, 0x20
0097F17E  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0097F183  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0097F188  E9 A0 FD FF FF                  jmp 0x14097ef2d
0097F18D  45 8B 44 24 78                  mov r8d, dword ptr [r12 + 0x78]
0097F192  45 85 C0                        test r8d, r8d
0097F195  0F 84 A7 FE FF FF               je 0x14097f042
0097F19B  33 D2                           xor edx, edx
0097F19D  49 8B CF                        mov rcx, r15
0097F1A0  E8 5B 28 F5 FF                  call 0x1408d1a00
0097F1A5  8B F0                           mov esi, eax
0097F1A7  85 C0                           test eax, eax
0097F1A9  0F 89 93 FE FF FF               jns 0x14097f042
0097F1AF  E9 D4 01 00 00                  jmp 0x14097f388
0097F1B4  48 8B CE                        mov rcx, rsi
0097F1B7  E8 1C 14 F5 FF                  call 0x1408d05d8
0097F1BC  45 33 C0                        xor r8d, r8d
0097F1BF  85 C0                           test eax, eax
0097F1C1  0F 84 69 F9 FF FF               je 0x14097eb30
0097F1C7  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0097F1CE  4C 39 00                        cmp qword ptr [rax], r8
0097F1D1  0F 85 8A AF 1A 00               jne 0x140b2a161
0097F1D7  41 8B 41 40                     mov eax, dword ptr [r9 + 0x40]
0097F1DB  48 05 FF 0F 00 00               add rax, 0xfff
0097F1E1  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0097F1E7  4C 3B D0                        cmp r10, rax
0097F1EA  0F 86 40 F9 FF FF               jbe 0x14097eb30
0097F1F0  E9 6C AF 1A 00                  jmp 0x140b2a161
0097F1F5  41 8B 85 FC 05 00 00            mov eax, dword ptr [r13 + 0x5fc]
0097F1FC  0F BA E0 0C                     bt eax, 0xc
0097F200  72 08                           jb 0x14097f20a
0097F202  A8 01                           test al, 1
0097F204  0F 84 33 04 00 00               je 0x14097f63d
0097F20A  45 0F B7 41 30                  movzx r8d, word ptr [r9 + 0x30]
0097F20F  66 44 89 85 C8 00 00 00         mov word ptr [rbp + 0xc8], r8w
0097F217  E9 03 F8 FF FF                  jmp 0x14097ea1f
0097F21C  4C 8B 4D B8                     mov r9, qword ptr [rbp - 0x48]
0097F220  4C 8B C6                        mov r8, rsi
0097F223  48 8B 95 E0 00 00 00            mov rdx, qword ptr [rbp + 0xe0]
0097F22A  49 8B CD                        mov rcx, r13
0097F22D  E8 DE 98 F4 FF                  call 0x1408c8b10
0097F232  45 33 C0                        xor r8d, r8d
0097F235  85 C0                           test eax, eax
0097F237  0F 88 3F FD FF FF               js 0x14097ef7c
0097F23D  41 8B 8D 50 07 00 00            mov ecx, dword ptr [r13 + 0x750]
0097F244  45 8D 48 04                     lea r9d, [r8 + 4]
0097F248  F6 C1 10                        test cl, 0x10
0097F24B  0F 85 97 04 00 00               jne 0x14097f6e8
0097F251  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
0097F256  E9 E7 F8 FF FF                  jmp 0x14097eb42
0097F25B  45 33 C9                        xor r9d, r9d
0097F25E  4D 8B 7C 24 08                  mov r15, qword ptr [r12 + 8]
0097F263  49 B8 00 00 00 00 01 00 00 00   movabs r8, 0x100000000
0097F26D  49 8B C9                        mov rcx, r9
0097F270  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0097F275  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
0097F279  4C 39 45 A0                     cmp qword ptr [rbp - 0x60], r8
0097F27D  0F 82 22 05 00 00               jb 0x14097f7a5
0097F283  66 44 39 48 0C                  cmp word ptr [rax + 0xc], r9w
0097F288  0F 8C 04 02 00 00               jl 0x14097f492
0097F28E  49 8B 14 24                     mov rdx, qword ptr [r12]
0097F292  49 3B D7                        cmp rdx, r15
0097F295  0F 83 ED 01 00 00               jae 0x14097f488
0097F29B  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
0097F29F  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
0097F2A4  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
0097F2A9  4C 8D 45 A8                     lea r8, [rbp - 0x58]
0097F2AD  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
0097F2B2  4D 8B C7                        mov r8, r15
0097F2B5  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
0097F2BA  4C 8B CE                        mov r9, rsi
0097F2BD  C1 E8 07                        shr eax, 7
0097F2C0  83 E0 1F                        and eax, 0x1f
0097F2C3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0097F2C7  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
0097F2CB  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0097F2D0  41 8B 4C 24 28                  mov ecx, dword ptr [r12 + 0x28]
0097F2D5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0097F2DA  E8 61 69 F0 FF                  call 0x140885c40
0097F2DF  45 33 C9                        xor r9d, r9d
0097F2E2  8B F0                           mov esi, eax
0097F2E4  85 C0                           test eax, eax
0097F2E6  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0097F2EB  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0097F2F0  0F 88 F8 AE 1A 00               js 0x140b2a1ee
0097F2F6  48 81 7D 80 00 00 20 00         cmp qword ptr [rbp - 0x80], 0x200000
0097F2FE  0F 85 3A FA FF FF               jne 0x14097ed3e
0097F304  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0097F308  4D 8B 44 24 18                  mov r8, qword ptr [r12 + 0x18]
0097F30D  48 8B C6                        mov rax, rsi
0097F310  49 2B C0                        sub rax, r8
0097F313  48 3D 00 00 01 00               cmp rax, 0x10000
0097F319  0F 82 46 AF 1A 00               jb 0x140b2a265
0097F31F  B9 01 00 00 00                  mov ecx, 1
0097F324  E8 E7 BC A9 FF                  call 0x14041b010
0097F329  4D 8B 44 24 18                  mov r8, qword ptr [r12 + 0x18]
0097F32E  48 8B CE                        mov rcx, rsi
0097F331  49 2B C8                        sub rcx, r8
0097F334  8B C0                           mov eax, eax
0097F336  48 C1 E9 10                     shr rcx, 0x10
0097F33A  33 D2                           xor edx, edx
0097F33C  48 F7 F1                        div rcx
0097F33F  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
0097F343  E9 1D AF 1A 00                  jmp 0x140b2a265
0097F348  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
0097F34C  45 33 C9                        xor r9d, r9d
0097F34F  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
0097F353  49 8B CF                        mov rcx, r15
0097F356  49 C1 E0 0C                     shl r8, 0xc
0097F35A  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0097F35F  49 81 C8 FF 0F 00 00            or r8, 0xfff
0097F366  48 C1 E2 0C                     shl rdx, 0xc
0097F36A  41 B9 01 00 00 80               mov r9d, 0x80000001
0097F370  E8 DB 0E 00 00                  call 0x140980250
0097F375  48 8B F8                        mov rdi, rax
0097F378  48 85 C0                        test rax, rax
0097F37B  0F 85 DF FC FF FF               jne 0x14097f060
0097F381  BE 9A 00 00 C0                  mov esi, 0xc000009a
0097F386  33 FF                           xor edi, edi
0097F388  49 8B CF                        mov rcx, r15
0097F38B  E8 00 65 91 FF                  call 0x140295890
0097F390  4D 85 F6                        test r14, r14
0097F393  0F 85 AE 05 00 00               jne 0x14097f947
0097F399  45 33 C0                        xor r8d, r8d
0097F39C  33 D2                           xor edx, edx
0097F39E  49 8B CF                        mov rcx, r15
0097F3A1  E8 DA 9E F0 FF                  call 0x140889280
0097F3A6  49 8B 44 24 48                  mov rax, qword ptr [r12 + 0x48]
0097F3AB  48 85 C0                        test rax, rax
0097F3AE  0F 85 A5 05 00 00               jne 0x14097f959
0097F3B4  8B C6                           mov eax, esi
0097F3B6  E9 C1 FB FF FF                  jmp 0x14097ef7c
0097F3BB  0F B7 4D 90                     movzx ecx, word ptr [rbp - 0x70]
0097F3BF  66 39 8D C8 00 00 00            cmp word ptr [rbp + 0xc8], cx
0097F3C6  0F 84 05 FB FF FF               je 0x14097eed1
0097F3CC  BA 00 10 00 00                  mov edx, 0x1000
0097F3D1  0B DA                           or ebx, edx
0097F3D3  49 39 B5 10 03 00 00            cmp qword ptr [r13 + 0x310], rsi
0097F3DA  0F 84 7E AF 1A 00               je 0x140b2a35e
0097F3E0  B9 64 86 00 00                  mov ecx, 0x8664
0097F3E5  66 39 48 30                     cmp word ptr [rax + 0x30], cx
0097F3E9  0F 85 6F AF 1A 00               jne 0x140b2a35e
0097F3EF  0F BA F3 0C                     btr ebx, 0xc
0097F3F3  E9 66 AF 1A 00                  jmp 0x140b2a35e
0097F3F8  40 F6 C7 10                     test dil, 0x10
0097F3FC  0F 85 38 FB FF FF               jne 0x14097ef3a
0097F402  49 39 74 24 48                  cmp qword ptr [r12 + 0x48], rsi
0097F407  0F 85 2D FB FF FF               jne 0x14097ef3a
0097F40D  41 8B 44 24 40                  mov eax, dword ptr [r12 + 0x40]
0097F412  A8 02                           test al, 2
0097F414  0F 84 23 FB FF FF               je 0x14097ef3d
0097F41A  E9 1B FB FF FF                  jmp 0x14097ef3a
0097F41F  41 0F B6 48 0F                  movzx ecx, byte ptr [r8 + 0xf]
0097F424  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
0097F427  C1 E1 0C                        shl ecx, 0xc
0097F42A  33 C1                           xor eax, ecx
0097F42C  25 00 F0 00 00                  and eax, 0xf000
0097F431  33 45 D0                        xor eax, dword ptr [rbp - 0x30]
0097F434  8B D0                           mov edx, eax
0097F436  33 D1                           xor edx, ecx
0097F438  81 E2 00 00 07 00               and edx, 0x70000
0097F43E  33 D0                           xor edx, eax
0097F440  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0097F445  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0097F44A  E9 E1 FC FF FF                  jmp 0x14097f130
0097F44F  48 8B CE                        mov rcx, rsi
0097F452  E8 81 11 F5 FF                  call 0x1408d05d8
0097F457  85 C0                           test eax, eax
0097F459  0F 84 93 FA FF FF               je 0x14097eef2
0097F45F  49 8B D7                        mov rdx, r15
0097F462  49 8B CD                        mov rcx, r13
0097F465  E8 3A 5B 91 FF                  call 0x140294fa4
0097F46A  E9 83 FA FF FF                  jmp 0x14097eef2
0097F46F  41 84 D9                        test r9b, bl
0097F472  0F 85 C0 02 00 00               jne 0x14097f738
0097F478  45 8B F8                        mov r15d, r8d
0097F47B  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
0097F480  83 E3 FD                        and ebx, 0xfffffffd
0097F483  E9 00 F7 FF FF                  jmp 0x14097eb88
0097F488  BE 17 00 00 C0                  mov esi, 0xc0000017
0097F48D  E9 5C AD 1A 00                  jmp 0x140b2a1ee
0097F492  4D 39 8D 10 03 00 00            cmp qword ptr [r13 + 0x310], r9
0097F499  75 72                           jne 0x14097f50d
0097F49B  49 8B C8                        mov rcx, r8
0097F49E  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
0097F4A2  E9 E7 FD FF FF                  jmp 0x14097f28e
0097F4A7  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
0097F4AB  0D 80 03 00 00                  or eax, 0x380
0097F4B0  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
0097F4B4  83 CF 10                        or edi, 0x10
0097F4B7  49 8B 85 70 01 00 00            mov rax, qword ptr [r13 + 0x170]
0097F4BE  41 89 56 34                     mov dword ptr [r14 + 0x34], edx
0097F4C2  48 C1 EA 20                     shr rdx, 0x20
0097F4C6  A8 01                           test al, 1
0097F4C8  41 88 56 22                     mov byte ptr [r14 + 0x22], dl
0097F4CC  0F 44 F9                        cmove edi, ecx
0097F4CF  E9 99 F7 FF FF                  jmp 0x14097ec6d
0097F4D4  BA 25 04 00 00                  mov edx, 0x425
0097F4D9  49 8B CF                        mov rcx, r15
0097F4DC  E8 1B EC FF FF                  call 0x14097e0fc
0097F4E1  E9 FB F9 FF FF                  jmp 0x14097eee1
0097F4E6  49 8B 8D 10 04 00 00            mov rcx, qword ptr [r13 + 0x410]
0097F4ED  48 8B 81 40 04 00 00            mov rax, qword ptr [rcx + 0x440]
0097F4F4  48 FF C0                        inc rax
0097F4F7  48 89 81 40 04 00 00            mov qword ptr [rcx + 0x440], rax
0097F4FE  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0097F503  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0097F508  E9 64 F9 FF FF                  jmp 0x14097ee71
0097F50D  41 0F B7 85 EC 06 00 00         movzx eax, word ptr [r13 + 0x6ec]
0097F515  BA 4C 01 00 00                  mov edx, 0x14c
0097F51A  66 3B C2                        cmp ax, dx
0097F51D  0F 84 6B FD FF FF               je 0x14097f28e
0097F523  BA C4 01 00 00                  mov edx, 0x1c4
0097F528  66 3B C2                        cmp ax, dx
0097F52B  0F 84 5D FD FF FF               je 0x14097f28e
0097F531  E9 65 FF FF FF                  jmp 0x14097f49b
0097F536  C7 44 24 60 03 00 00 40         mov dword ptr [rsp + 0x60], 0x40000003
0097F53E  F6 C3 02                        test bl, 2
0097F541  0F 84 19 F8 FF FF               je 0x14097ed60
0097F547  F6 C3 08                        test bl, 8
0097F54A  75 59                           jne 0x14097f5a5
0097F54C  48 8B 85 C0 00 00 00            mov rax, qword ptr [rbp + 0xc0]
0097F553  41 B8 56 61 64 49               mov r8d, 0x49646156
0097F559  48 8B 00                        mov rax, qword ptr [rax]
0097F55C  8B 48 08                        mov ecx, dword ptr [rax + 8]
0097F55F  8B C1                           mov eax, ecx
0097F561  24 3F                           and al, 0x3f
0097F563  F6 D8                           neg al
0097F565  48 1B D2                        sbb rdx, rdx
0097F568  48 C1 E9 06                     shr rcx, 6
0097F56C  48 F7 DA                        neg rdx
0097F56F  48 83 C2 15                     add rdx, 0x15
0097F573  48 03 D1                        add rdx, rcx
0097F576  B9 40 00 00 00                  mov ecx, 0x40
0097F57B  48 C1 E2 03                     shl rdx, 3
0097F57F  E8 BC BF 9D FF                  call 0x14035b540
0097F584  48 8B F0                        mov rsi, rax
0097F587  48 85 C0                        test rax, rax
0097F58A  0F 85 F6 AC 1A 00               jne 0x140b2a286
0097F590  4C 8B 85 D8 00 00 00            mov r8, qword ptr [rbp + 0xd8]
0097F597  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0097F59C  F6 C3 08                        test bl, 8
0097F59F  0F 84 BB F7 FF FF               je 0x14097ed60
0097F5A5  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
0097F5AA  41 83 C9 01                     or r9d, 1
0097F5AE  C7 44 24 60 36 00 00 40         mov dword ptr [rsp + 0x60], 0x40000036
0097F5B6  E9 AA F7 FF FF                  jmp 0x14097ed65
0097F5BB  48 8D 8E 80 00 00 00            lea rcx, [rsi + 0x80]
0097F5C2  48 85 C9                        test rcx, rcx
0097F5C5  0F 84 CB F5 FF FF               je 0x14097eb96
0097F5CB  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
0097F5CE  83 E0 0E                        and eax, 0xe
0097F5D1  3C 0C                           cmp al, 0xc
0097F5D3  73 06                           jae 0x14097f5db
0097F5D5  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0097F5D9  EB E7                           jmp 0x14097f5c2
0097F5DB  49 8B 4C 24 60                  mov rcx, qword ptr [r12 + 0x60]
0097F5E0  E8 E7 E1 FF FF                  call 0x14097d7cc
0097F5E5  85 C0                           test eax, eax
0097F5E7  0F 88 8F F9 FF FF               js 0x14097ef7c
0097F5ED  E9 A4 F5 FF FF                  jmp 0x14097eb96
0097F5F2  8B 05 84 E2 4A 00               mov eax, dword ptr [rip + 0x4ae284]
0097F5F8  41 3B 41 3C                     cmp eax, dword ptr [r9 + 0x3c]
0097F5FC  0F 85 C7 F3 FF FF               jne 0x14097e9c9
0097F602  8B 0D 78 E2 4A 00               mov ecx, dword ptr [rip + 0x4ae278]
0097F608  49 8B 43 38                     mov rax, qword ptr [r11 + 0x38]
0097F60C  3B 48 44                        cmp ecx, dword ptr [rax + 0x44]
0097F60F  0F 85 B4 F3 FF FF               jne 0x14097e9c9
0097F615  CC                              int3
0097F616  E9 AE F3 FF FF                  jmp 0x14097e9c9
0097F61B  66 41 0F BA 63 0C 0E            bt word ptr [r11 + 0xc], 0xe
0097F622  8B DA                           mov ebx, edx
0097F624  0F 82 CF F3 FF FF               jb 0x14097e9f9
0097F62A  41 BF 01 00 00 00               mov r15d, 1
0097F630  83 CB 05                        or ebx, 5
0097F633  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
0097F638  E9 BC F3 FF FF                  jmp 0x14097e9f9
0097F63D  44 0F B7 C1                     movzx r8d, cx
0097F641  66 89 8D C8 00 00 00            mov word ptr [rbp + 0xc8], cx
0097F648  E9 D2 F3 FF FF                  jmp 0x14097ea1f
0097F64D  E8 6E 07 B1 FF                  call 0x14048fdc0
0097F652  85 C0                           test eax, eax
0097F654  0F 84 EC AA 1A 00               je 0x140b2a146
0097F65A  B9 04 00 00 00                  mov ecx, 4
0097F65F  0B D9                           or ebx, ecx
0097F661  41 83 CF 02                     or r15d, 2
0097F665  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
0097F66A  E9 C4 F3 FF FF                  jmp 0x14097ea33
0097F66F  41 F7 44 24 40 00 00 00 02      test dword ptr [r12 + 0x40], 0x2000000
0097F678  0F 85 C3 F3 FF FF               jne 0x14097ea41
0097F67E  B8 22 00 00 C0                  mov eax, 0xc0000022
0097F683  E9 F4 F8 FF FF                  jmp 0x14097ef7c
0097F688  48 3B F8                        cmp rdi, rax
0097F68B  0F 82 A7 00 00 00               jb 0x14097f738
0097F691  3B D9                           cmp ebx, ecx
0097F693  0F 83 9F 00 00 00               jae 0x14097f738
0097F699  33 C0                           xor eax, eax
0097F69B  83 E3 FD                        and ebx, 0xfffffffd
0097F69E  83 CB 01                        or ebx, 1
0097F6A1  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0097F6A5  41 F6 41 2C 01                  test byte ptr [r9 + 0x2c], 1
0097F6AA  44 8B F8                        mov r15d, eax
0097F6AD  0F 85 BF AA 1A 00               jne 0x140b2a172
0097F6B3  49 81 C2 FF FF 1F 00            add r10, 0x1fffff
0097F6BA  41 B8 00 00 20 00               mov r8d, 0x200000
0097F6C0  49 81 E2 00 00 E0 FF            and r10, 0xffffffffffe00000
0097F6C7  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
0097F6CB  4C 89 55 88                     mov qword ptr [rbp - 0x78], r10
0097F6CF  E9 98 F3 FF FF                  jmp 0x14097ea6c
0097F6D4  B8 45 00 00 C0                  mov eax, 0xc0000045
0097F6D9  E9 9E F8 FF FF                  jmp 0x14097ef7c
0097F6DE  B8 1F 00 00 C0                  mov eax, 0xc000001f
0097F6E3  E9 94 F8 FF FF                  jmp 0x14097ef7c
0097F6E8  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
0097F6EC  44 84 4A 33                     test byte ptr [rdx + 0x33], r9b
0097F6F0  0F 85 5B FB FF FF               jne 0x14097f251
0097F6F6  F6 42 2C 01                     test byte ptr [rdx + 0x2c], 1
0097F6FA  0F 84 7C AA 1A 00               je 0x140b2a17c
0097F700  F6 C1 08                        test cl, 8
0097F703  0F 84 48 FB FF FF               je 0x14097f251
0097F709  E9 64 AA 1A 00                  jmp 0x140b2a172
0097F70E  41 8B 85 50 07 00 00            mov eax, dword ptr [r13 + 0x750]
0097F715  A8 40                           test al, 0x40
0097F717  0F 85 3C F4 FF FF               jne 0x14097eb59
0097F71D  83 E3 FD                        and ebx, 0xfffffffd
0097F720  83 CB 01                        or ebx, 1
0097F723  E9 31 F4 FF FF                  jmp 0x14097eb59
0097F728  45 8B F8                        mov r15d, r8d
0097F72B  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
0097F730  83 E3 F9                        and ebx, 0xfffffff9
0097F733  E9 3B F4 FF FF                  jmp 0x14097eb73
0097F738  B8 18 00 00 C0                  mov eax, 0xc0000018
0097F73D  E9 3A F8 FF FF                  jmp 0x14097ef7c
0097F742  48 8B CE                        mov rcx, rsi
0097F745  E8 D6 A2 AF FF                  call 0x140479a20
0097F74A  B8 9A 00 00 C0                  mov eax, 0xc000009a
0097F74F  E9 28 F8 FF FF                  jmp 0x14097ef7c
0097F754  83 CB 08                        or ebx, 8
0097F757  E9 80 F4 FF FF                  jmp 0x14097ebdc
0097F75C  83 CF 08                        or edi, 8
0097F75F  E9 E8 F4 FF FF                  jmp 0x14097ec4c
0097F764  48 81 F9 00 00 20 00            cmp rcx, 0x200000
0097F76B  0F 84 20 F5 FF FF               je 0x14097ec91
0097F771  48 8B 85 D0 00 00 00            mov rax, qword ptr [rbp + 0xd0]
0097F778  4C 8B 38                        mov r15, qword ptr [rax]
0097F77B  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0097F780  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
0097F785  E9 2F F5 FF FF                  jmp 0x14097ecb9
0097F78A  BE 0A 01 00 C0                  mov esi, 0xc000010a
0097F78F  EB 05                           jmp 0x14097f796
0097F791  BE 17 00 00 C0                  mov esi, 0xc0000017
0097F796  4D 8B FE                        mov r15, r14
0097F799  E9 BB AA 1A 00                  jmp 0x140b2a259
0097F79E  BE 18 00 00 C0                  mov esi, 0xc0000018
0097F7A3  EB F1                           jmp 0x14097f796
0097F7A5  4D 3B F8                        cmp r15, r8
0097F7A8  0F 82 D5 FA FF FF               jb 0x14097f283
0097F7AE  BA 00 40 00 00                  mov edx, 0x4000
0097F7B3  66 85 50 0C                     test word ptr [rax + 0xc], dx
0097F7B7  BA FF FF FF FF                  mov edx, 0xffffffff
0097F7BC  4C 0F 44 FA                     cmove r15, rdx
0097F7C0  E9 BE FA FF FF                  jmp 0x14097f283
0097F7C5  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
0097F7C9  48 2B C8                        sub rcx, rax
0097F7CC  E9 D3 F5 FF FF                  jmp 0x14097eda4
0097F7D1  45 8B 85 FC 05 00 00            mov r8d, dword ptr [r13 + 0x5fc]
0097F7D8  41 8B D1                        mov edx, r9d
0097F7DB  41 C1 E8 0D                     shr r8d, 0xd
0097F7DF  49 8B CF                        mov rcx, r15
0097F7E2  41 83 E0 01                     and r8d, 1
0097F7E6  E8 3D 5D 06 00                  call 0x1409e5528
0097F7EB  E9 F0 F5 FF FF                  jmp 0x14097ede0
0097F7F0  49 8B 85 10 04 00 00            mov rax, qword ptr [r13 + 0x410]
0097F7F7  C6 80 24 04 00 00 01            mov byte ptr [rax + 0x424], 1
0097F7FE  E9 EA F5 FF FF                  jmp 0x14097eded
0097F803  49 8B CD                        mov rcx, r13
0097F806  E8 E5 00 8B FF                  call 0x14022f8f0
0097F80B  8B D0                           mov edx, eax
0097F80D  49 8B CE                        mov rcx, r14
0097F810  E8 C3 6E 0E 00                  call 0x140a666d8
0097F815  8B F0                           mov esi, eax
0097F817  85 C0                           test eax, eax
0097F819  78 0E                           js 0x14097f829
0097F81B  0F BA EB 08                     bts ebx, 8
0097F81F  E9 DE F5 FF FF                  jmp 0x14097ee02
0097F824  BE 0B 06 00 C0                  mov esi, 0xc000060b
0097F829  0F BA E3 08                     bt ebx, 8
0097F82D  0F 83 D9 AB 1A 00               jae 0x140b2a40c
0097F833  49 8B CD                        mov rcx, r13
0097F836  E8 B5 00 8B FF                  call 0x14022f8f0
0097F83B  8B D0                           mov edx, eax
0097F83D  49 8B CE                        mov rcx, r14
0097F840  E8 A3 F5 0A 00                  call 0x140a2ede8
0097F845  90                              nop
0097F846  E9 C1 AB 1A 00                  jmp 0x140b2a40c
0097F84B  F7 DE                           neg esi
0097F84D  49 8D 8E 80 00 00 00            lea rcx, [r14 + 0x80]
0097F854  41 B0 11                        mov r8b, 0x11
0097F857  1B D2                           sbb edx, edx
0097F859  81 E2 00 01 00 00               and edx, 0x100
0097F85F  83 C2 08                        add edx, 8
0097F862  E8 F9 57 9A FF                  call 0x140325060
0097F867  8B F0                           mov esi, eax
0097F869  85 C0                           test eax, eax
0097F86B  78 BC                           js 0x14097f829
0097F86D  0F BA EB 09                     bts ebx, 9
0097F871  E9 DD F5 FF FF                  jmp 0x14097ee53
0097F876  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0097F87B  49 8B D7                        mov rdx, r15
0097F87E  E8 8D 5F 91 FF                  call 0x140295810
0097F883  45 33 C9                        xor r9d, r9d
0097F886  45 33 C0                        xor r8d, r8d
0097F889  8B D6                           mov edx, esi
0097F88B  49 8B CF                        mov rcx, r15
0097F88E  E8 61 2E A5 FF                  call 0x1403d26f4
0097F893  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0097F898  8B F0                           mov esi, eax
0097F89A  85 C0                           test eax, eax
0097F89C  0F 89 AD AA 1A 00               jns 0x140b2a34f
0097F8A2  49 8B D5                        mov rdx, r13
0097F8A5  E8 9A 4F 92 FF                  call 0x1402a4844
0097F8AA  E9 D7 FA FF FF                  jmp 0x14097f386
0097F8AF  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0097F8B3  05 FD FF FF BF                  add eax, 0xbffffffd
0097F8B8  83 F8 33                        cmp eax, 0x33
0097F8BB  0F 87 B4 AA 1A 00               ja 0x140b2a375
0097F8C1  48 B9 01 08 00 00 00 00 08 00   movabs rcx, 0x8000000000801
0097F8CB  48 0F A3 C1                     bt rcx, rax
0097F8CF  0F 82 3A F6 FF FF               jb 0x14097ef0f
0097F8D5  E9 9B AA 1A 00                  jmp 0x140b2a375
0097F8DA  0F BA 6D D0 13                  bts dword ptr [rbp - 0x30], 0x13
0097F8DF  E9 84 F8 FF FF                  jmp 0x14097f168
0097F8E4  33 F6                           xor esi, esi
0097F8E6  E9 52 F6 FF FF                  jmp 0x14097ef3d
0097F8EB  41 B8 01 00 00 00               mov r8d, 1
0097F8F1  49 8B D7                        mov rdx, r15
0097F8F4  49 8B CD                        mov rcx, r13
0097F8F7  E8 30 D3 B4 FF                  call 0x1404ccc2c
0097F8FC  48 8D 55 10                     lea rdx, [rbp + 0x10]
0097F900  49 8B CF                        mov rcx, r15
0097F903  E8 14 EB CF FF                  call 0x14067e41c
0097F908  83 E3 BF                        and ebx, 0xffffffbf
0097F90B  E9 26 F7 FF FF                  jmp 0x14097f036
0097F910  45 8B 4C 24 44                  mov r9d, dword ptr [r12 + 0x44]
0097F915  B8 04 00 00 00                  mov eax, 4
0097F91A  44 3B C8                        cmp r9d, eax
0097F91D  0F 84 A5 AA 1A 00               je 0x140b2a3c8
0097F923  41 8D 41 FF                     lea eax, [r9 - 1]
0097F927  83 F8 01                        cmp eax, 1
0097F92A  0F 86 98 AA 1A 00               jbe 0x140b2a3c8
0097F930  41 81 F9 01 00 00 80            cmp r9d, 0x80000001
0097F937  0F 84 8B AA 1A 00               je 0x140b2a3c8
0097F93D  BE 45 00 00 C0                  mov esi, 0xc0000045
0097F942  E9 41 FA FF FF                  jmp 0x14097f388
0097F947  BA 4D 6D 53 63                  mov edx, 0x63536d4d
0097F94C  49 8B CE                        mov rcx, r14
0097F94F  E8 8C 7F 97 FF                  call 0x1402f78e0
0097F954  E9 40 FA FF FF                  jmp 0x14097f399
0097F959  48 89 38                        mov qword ptr [rax], rdi
0097F95C  E9 53 FA FF FF                  jmp 0x14097f3b4
0097F961  49 8B CF                        mov rcx, r15
0097F964  E8 FB 59 9E FF                  call 0x140365364
0097F969  E9 FF F6 FF FF                  jmp 0x14097f06d
0097F96E  B8 04 00 00 00                  mov eax, 4
0097F973  41 09 44 24 3C                  or dword ptr [r12 + 0x3c], eax
0097F978  E9 FB F5 FF FF                  jmp 0x14097ef78
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMapViewOfImageSection(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned __int8 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int16 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int16 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (376);
    v_rbx = 0;
    v_stack_m148 = 0;
    a2 = 0;
    v_stack_m110 = 0;
    v_stack_mF8 = 0;
    result = memset(v_stack_mA8, a2, v_rbx + 88, a4);
    result = 0;
    v_r14 = (*(unsigned __int64 *)(a1 + 96)) & (-8);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 40))) >> (22));
    v_stack_mC0 = 0;
    a2 = (unsigned int)((a2) & (2));
    v_stack_m168 = 0;
    v_stack_m150 = *(unsigned __int64 *)(a1);
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    v_stack_m100 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4910804))) != 0) goto loc_0097F5F2;
loc_0097E9C9:
    v_stack_m120 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 48);
    v_stack_m118 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32);
    if (((*(unsigned int *)(a1 + 56)) & (0x20000000ULL)) != 0) goto loc_0097F61B;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a2 + 88) + 1532)) & (0x2000ULL)) != 0) goto loc_0097F61B;
loc_0097E9F9:
    v_stack_m128 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 88) + 1772));
    v_stack_p10 = (unsigned __int16)(*(unsigned __int16 *)(a2 + 58));
    if ((unsigned __int16)(*(unsigned __int16 *)(a2 + 58)) == 0) goto loc_0097F1F5;
loc_0097EA1F:
    if (((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(a2 + 58)))) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) + 48)))) goto loc_0097F64D;
loc_0097EA33:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 88) + 368)) & (1)) != 0) goto loc_0097F66F;
loc_0097EA41:
    v_stack_m138 = *(unsigned __int64 *)(a2 + 16);
    v_stack_m130 = *(unsigned __int64 *)(a2 + 24);
    if (condition_is_below) goto loc_0097F688;
loc_0097EA6C:
    if (a5 == 0) goto loc_0097EA8D;
    a1 = (((*(unsigned int *)(a5 + 56)) & (0x80000ULL)) == 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0097EA9E;
loc_0097EA8D:
    if (a7 != 1) goto loc_0097F6D4;
loc_0097EA9E:
    a1 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4910600))) == 0) goto loc_0097EB2D;
    a1 = (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) + 76)) & (64)) != 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0097EB2D;
    if ((*(unsigned __int64 *)(a2 + 16)) == 0x200000ULL) goto loc_0097EB2D;
    a1 = (((*(unsigned __int64 *)(a2 + 24)) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (*(unsigned __int64 *)(a2 + 24)) >> (12);
    a1 = (a1) + (result);
    if (a1 != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)))) goto loc_0097F1B4;
    a1 = (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 88) + 2012)) & (4)) == 0) ? 1 : 0;
    result = (((a8) & (16)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0097F1B4;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4910600)))) + *(unsigned __int64 *)(a2 + 24) * 1) < (*(unsigned __int64 *)(a2 + 24))) goto loc_0097F6DE;
    v_stack_m130 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4910600)))) + *(unsigned __int64 *)(a2 + 24) * 1;
    goto loc_0097EB30;
loc_0097EB2D:
    a3 = 0;
loc_0097EB30:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) < 0x400ULL) goto loc_0097F21C;
loc_0097EB42:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) < 0x400ULL) goto loc_0097F71D;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) < 0x400ULL) goto loc_0097F70E;
loc_0097EB59:
    if (((v_stack_p40) & (4)) != 0) goto loc_0097F728;
    if ((*(unsigned __int64 *)(a2 + 88)) == (*(unsigned __int64 *)(v_rip + 6586699))) goto loc_0097F728;
loc_0097EB73:
    if ((*(unsigned __int64 *)(v_r14 + 32)) == 0) goto loc_0097F46F;
    if ((*(unsigned __int64 *)(v_r14 + 32)) < 0) goto loc_0097F46F;
loc_0097EB88:
    v_stack_m108 = 0;
    if ((*(unsigned __int64 *)(v_r14 + 32)) >= 0) goto loc_0097F5BB;
loc_0097EB96:
    v_stack_mB8 = a1 + 128;
    result = MiCheckPurgeAndUpMapCount(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4910600)))), a3, 4);
    if (0 != 0) goto loc_0097EF91;
loc_0097EBBD:
    result = MiAllocatePool(64, 136, (unsigned int)(0x20646156ULL), 4);
    if (result == 0) goto loc_0097F742;
    if (0 != 0) goto loc_0097F754;
loc_0097EBDC:
    v_r15 = 0;
    *(unsigned __int64 *)(result + 16) = -2;
    *(unsigned __int64 *)(result) = -2;
    *(unsigned __int64 *)(result + 8) = -2;
    result = 0;
    if (a6 == 1) { result = (unsigned int)(v_r15 + 4); }
    v_rdi = (unsigned int)((32) | ((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xFFFFFFAFULL));
    a1 = (unsigned int)((a1) | (32));
    *(unsigned int *)(result + 48) = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 52))) << (12));
    result = (unsigned int)((result) ^ ((unsigned int)(a1)));
    result = (unsigned int)((result) & (0x7F000ULL));
    result = (unsigned int)((result) ^ ((unsigned int)(a1)));
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    if (a5 == 0) goto loc_0097EC4C;
    result = MiReferenceFileObjectForMap(a5, 136, (unsigned int)(0x20646156ULL), 4);
    *(unsigned __int64 *)(result + 128) = result;
    if ((*(unsigned int *)(a5 + 60)) < 0) goto loc_0097F75C;
loc_0097EC4C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xFFFFF0FFULL));
    *(unsigned __int64 *)(result + 40) = 0;
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    if (condition_is_above_or_equal) goto loc_0097F4A7;
loc_0097EC6D:
    v_stack_m158 = 0;
    v_stack_m140 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 60)))) & (1)) != 0) goto loc_0097F764;
loc_0097EC91:
    v_r15 = ((unsigned int)(*(unsigned int *)(v_stack_p20))) + (v_stack_m118);
    v_stack_m160 = v_r15;
    v_stack_m148 = v_r15;
loc_0097ECB9:
    result = MiWriteVadFlags2(result, (unsigned int)((unsigned int)(v_rdi)), 1, 4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xF80ULL));
    if (((unsigned int)(result)) == 896) goto loc_0097F0D5;
loc_0097ECDD:
    v_stack_m58 = 32;
    result = LOCK_ADDRESS_SPACE(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a2 + 88), 1, 4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 88) + 500)))) & (32)) != 0) goto loc_0097F78A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 60)))) & (1)) == 0) goto loc_0097EFBD;
    if (v_stack_m138 == 0x200000ULL) goto loc_0097EFBD;
    v_stack_m198 = *(unsigned __int64 *)(a2 + 8);
    result = MiIsVaRangeAvailable(*(unsigned __int64 *)(a2 + 88), v_r15, v_stack_m130, *(unsigned __int64 *)(a2));
    if ((unsigned int)(result) == 0) goto loc_0097F79E;
loc_0097ED3E:
    a1 = (v_stack_m160) - ((unsigned int)(*(unsigned int *)(v_stack_p20)));
    if (a1 != v_stack_m118) goto loc_0097F536;
loc_0097ED60:
loc_0097ED65:
    a1 = (v_stack_m160) >> (12);
    result = (v_stack_m130) - 1;
    result = (result) + (v_stack_m160);
    v_stack_m118 = a1;
    result = (result) >> (12);
    v_stack_m120 = result;
    result = MiUpdateVadStartVpn(result, a1, v_stack_p20, (unsigned int)(v_stack_m168));
    *(unsigned int *)(result + 28) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned __int8 *)(result + 33) = (unsigned __int8)(result);
    a1 = (*(unsigned __int64 *)(v_stack_p20)) >> (12);
loc_0097EDA4:
    if (a1 >= ((unsigned int)(*(unsigned int *)(v_stack_mB8 + 44)))) goto loc_0097F7C5;
    *(unsigned __int64 *)(result + 72) = v_stack_mB8;
    *(unsigned __int64 *)(result + 80) = *(unsigned __int64 *)(v_stack_mB8 + 8) + a1 * 8;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m150 + 8))) - 1;
    *(unsigned __int64 *)(result + 88) = *(unsigned __int64 *)(v_stack_m150 + 64) + a1 * 8;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(a2)))) & (8)) != 0) goto loc_0097F7D1;
loc_0097EDE0:
    result = 0;
    if ((*(unsigned int *)(a2 + 52)) != 0) goto loc_0097F7F0;
loc_0097EDED:
    if (((*(unsigned int *)(v_stack_p8 + 56)) & (0x8000000ULL)) != 0) goto loc_0097F803;
loc_0097EE02:
    a3 = 0;
    result = MiInsertSharedCommitNode(v_stack_p8, *(unsigned __int64 *)(a2 + 88), a3, (unsigned int)(v_stack_m168));
    a4 = 0;
    if (sign_flag) goto loc_0097F829;
    v_rsi = (unsigned int)(((unsigned int)(a8)) & (8));
    a2 = (condition_is_not_equal) ? 1 : 0;
    result = MiControlAreaRequiresCharge(v_stack_p8, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0097F824;
    if (((unsigned int)(result)) == 2) goto loc_0097F84B;
loc_0097EE53:
    result = MiInsertVadCharges(result, *(unsigned __int64 *)(a2 + 88), a3, a4);
    if (sign_flag) goto loc_0097F829;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(a2)))) & (8)) != 0) goto loc_0097F4E6;
loc_0097EE71:
    a3 = 0;
    result = MiInsertVad(result, *(unsigned __int64 *)(a2 + 88), a3, a4);
    v_rsi = 0;
    if (v_stack_m138 == 0x200000ULL) goto loc_0097F876;
    if (v_stack_m110 != 0) goto loc_0097F0C3;
loc_0097EE9F:
    a1 = (v_stack_m108) << (16);
    result = (v_stack_m160) + (a1);
    v_stack_m160 = result;
    v_stack_m148 = result;
    *(unsigned __int64 *)(v_stack_p18) = result;
    if ((*(unsigned __int8 *)(v_stack_m100 + 50)) != 0) goto loc_0097F3BB;
loc_0097EED1:
    if (((*(unsigned int *)(v_rip + 6585381)) & (0x8000ULL)) != 0) goto loc_0097F4D4;
loc_0097EEE1:
    if ((((unsigned __int8)(v_rdi)) & (32)) != 0) goto loc_0097F44F;
loc_0097EEF2:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (16));
    if (condition_is_below) goto loc_0097F8E4;
    if (((*(unsigned int *)(v_rip + 6575031)) & (0x40000ULL)) != 0) goto loc_0097F8AF;
loc_0097EF0F:
    result = MiReadVadFlags2(result, *(unsigned __int64 *)(a2 + 88), v_stack_m150, a4);
    if ((((unsigned int)((unsigned int)(0x800ULL))) & ((unsigned int)(v_rbx))) != 0) goto loc_0097F119;
loc_0097EF2D:
    v_rsi = 0;
    if ((*(unsigned int *)(a2 + 120)) == 0) goto loc_0097F3F8;
loc_0097EF3A:
    v_rbx = (unsigned int)((v_rbx) | (32));
loc_0097EF3D:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_0097F009;
loc_0097EF4B:
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) {
        a2 = *(unsigned __int64 *)(a2 + 88);
        a1 = v_stack_m140;
        result = UNLOCK_ADDRESS_SPACE(a1, a2, v_stack_m150, (unsigned int)(0x800ULL));
    }
    if (condition_is_below) goto loc_0097EF78;
    if (a5 == 0) goto loc_0097EF78;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 88) + 368)) & (1)) == 0) goto loc_0097F96E;
loc_0097EF78:
loc_0097EF7C:
    v_rsp = (v_rsp) + (376);
    return (unsigned int)(v_stack_m158);
loc_0097EF91:
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi) + 8))))) & (63));
    result = (unsigned __int8)(-(result));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi) + 8))) >> (6);
    a2 = -(a2);
    a2 = (a2) + (21);
    a2 = (a2) + (a1);
    a2 = (a2) << (3);
    goto loc_0097EBBD;
loc_0097EFBD:
    if (v_stack_m130 > result) goto loc_0097F791;
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_0097F25B;
    v_stack_p20 = *(unsigned __int64 *)(a2 + 8);
    result = MiIsVaRangeAvailable(*(unsigned __int64 *)(a2 + 88), v_stack_m140, v_stack_m130, *(unsigned __int64 *)(a2));
    a4 = 0;
    if ((unsigned int)(result) != 0) goto loc_0097ED3E;
    goto loc_0097F25E;
loc_0097F009:
    result = MiLockVad(v_stack_p78, v_stack_m140, v_stack_m130, a4);
    result = UNLOCK_ADDRESS_SPACE(v_stack_p78, *(unsigned __int64 *)(a2 + 88), v_stack_m130, a4);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFEFULL));
    result = MiReadVadFlags2(v_stack_m140, *(unsigned __int64 *)(a2 + 88), v_stack_m130, a4);
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_0097F8EB;
loc_0097F036:
    v_rdi = 0;
    if (condition_is_above_or_equal) goto loc_0097F18D;
loc_0097F042:
    if ((*(unsigned __int64 *)(a2 + 72)) != 0) goto loc_0097F910;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & ((unsigned int)((unsigned int)(0x800ULL))));
    if (condition_is_not_equal) goto loc_0097F348;
loc_0097F060:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 64)))) & (2)) != 0) goto loc_0097F961;
loc_0097F06D:
    result = MiUnlockVad(v_stack_p78, v_stack_m140, v_stack_m130, a4);
    if ((unsigned int)(v_rsi) != 0) {
        a1 = 0 + 88;
        a4 = 0;
        a3 = v_stack_mF0;
        a2 = *(unsigned __int64 *)(a2 + 88);
        result = PsCallImageNotifyRoutines(a1, a2, a3, a4);
        a2 = 0x63536D4DULL;
        a1 = 0;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, a4);
    }
    v_rsi = 0;
    if (v_stack_mF8 == 0) goto loc_0097EF4B;
    a1 = (*(unsigned __int64 *)(a2 + 88)) ^ (v_stack_mF8);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rip + 4909767));
    result = MmUnsecureVirtualMemory(a1, a2, a3, a4);
    goto loc_0097EF4B;
loc_0097F0C3:
    result = MiAdvanceVadHint(v_stack_m118, v_stack_m120, a3, a4);
    goto loc_0097EE9F;
loc_0097F0D5:
    a2 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 88) + 464)) == 0) goto loc_0097ECDD;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a2 + 88) + 1532)) & (0x1000ULL)) != 0) goto loc_0097ECDD;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 88) + 368)) & (1)) != 0) goto loc_0097ECDD;
    result = PsIsImageNotifyEnabled(v_stack_m118, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0097ECDD;
    goto loc_0097ECDD;
loc_0097F119:
    v_stack_mE8 = 3;
    if ((((unsigned __int8)(v_stack_mF8)) & (8)) == 0) goto loc_0097F41F;
    a2 = (unsigned int)(((unsigned int)(v_stack_mE8)) & (0xFFF80FFFULL));
loc_0097F130:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (1));
    result = (unsigned int)((result) ^ ((unsigned int)(a2)));
    result = (unsigned int)((result) & ((unsigned int)(a4)));
    result = (unsigned int)((result) ^ ((unsigned int)(a2)));
    v_stack_mE8 = (unsigned int)(result);
    a1 = (v_stack_m118) | (-1);
    v_stack_mE0 = v_stack_p58;
    v_stack_mD0 = *(unsigned __int64 *)(a2 + 24);
    if ((*(unsigned __int64 *)(a2 + 24)) != a1) goto loc_0097F8DA;
loc_0097F168:
    result = 0;
    v_stack_mD8 = 0;
    v_stack_mC8 = 0;
    result = MiReferenceControlAreaFile(0, a2, a3, a4);
    v_rbx = (unsigned int)((v_rbx) | (32));
    v_stack_p58 = v_stack_p70;
    goto loc_0097EF2D;
loc_0097F18D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 120))) == 0) goto loc_0097F042;
    a2 = 0;
    result = MiCommitVadMetadataBits(v_stack_p78, a2, (unsigned int)(*(unsigned int *)(a2 + 120)), a4);
    if (!sign_flag) goto loc_0097F042;
    goto loc_0097F388;
loc_0097F1B4:
    result = MiDoesImageContainFunctionOverrideFixups((unsigned int)((unsigned int)(result)), a2, (unsigned int)(*(unsigned int *)(a2 + 120)), a4);
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_0097EB30;
    result = ((unsigned int)(*(unsigned int *)(a4 + 64))) + (0xFFFULL);
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    if ((*(unsigned __int64 *)(a2 + 24)) <= result) goto loc_0097EB30;
loc_0097F1F5:
    if ((*(unsigned __int64 *)(a2 + 24)) < result) goto loc_0097F20A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 88) + 1532)))) & (1)) == 0) goto loc_0097F63D;
loc_0097F20A:
    v_stack_p10 = (unsigned __int16)(*(unsigned __int16 *)(a4 + 48));
    goto loc_0097EA1F;
loc_0097F21C:
    result = MiAllowImageMap(*(unsigned __int64 *)(a2 + 88), a5, (unsigned int)((unsigned int)(result)), v_stack_m100);
    a3 = 0;
    if (sign_flag) goto loc_0097EF7C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 88) + 1872)))) & (16)) != 0) goto loc_0097F6E8;
loc_0097F251:
    goto loc_0097EB42;
loc_0097F25B:
    a4 = 0;
loc_0097F25E:
    v_stack_m120 = 0;
    if (v_stack_m118 < 0) goto loc_0097F7A5;
loc_0097F283:
    if ((*(unsigned __int16 *)(v_stack_p68 + 12)) < 0) goto loc_0097F492;
loc_0097F28E:
    if ((*(unsigned __int64 *)(a2)) >= (*(unsigned __int64 *)(a2 + 8))) goto loc_0097F488;
    v_stack_p48 = v_stack_p70;
    v_stack_p40 = v_stack_m110;
    v_stack_p38 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) >> (7));
    result = (unsigned int)((result) & (31));
    v_stack_p30 = (unsigned int)(result);
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_m138;
    result = MiSelectUserAddress((unsigned int)(*(unsigned int *)(a2 + 40)), *(unsigned __int64 *)(a2), *(unsigned __int64 *)(a2 + 8), (unsigned int)((unsigned int)(result)));
    a4 = 0;
    v_stack_p58 = v_stack_p70;
    if (v_stack_m138 != 0x200000ULL) goto loc_0097ED3E;
    result = (v_stack_m130) - (*(unsigned __int64 *)(a2 + 24));
    result = ExGenRandom(1, *(unsigned __int64 *)(a2), *(unsigned __int64 *)(a2 + 24), a4);
    a1 = (v_stack_m130) - (*(unsigned __int64 *)(a2 + 24));
    a1 = (a1) >> (16);
    a2 = 0;
    v_stack_m108 = 0;
loc_0097F348:
    a4 = 0;
    a3 = (v_stack_m120) << (12);
    v_stack_p20 = 0;
    a3 = (a3) | (0xFFFULL);
    a2 = (v_stack_m118) << (12);
    result = MiAddSecureEntry(*(unsigned __int64 *)(a2 + 8), a2, a3, (unsigned int)(0x80000001ULL));
    if (result != 0) goto loc_0097F060;
loc_0097F386:
    v_rdi = 0;
loc_0097F388:
    result = MiReferenceVad(*(unsigned __int64 *)(a2 + 8), a2, a3, (unsigned int)(0x80000001ULL));
    if (result != 0) goto loc_0097F947;
loc_0097F399:
    a3 = 0;
    a2 = 0;
    result = MiUnmapVad(*(unsigned __int64 *)(a2 + 8), a2, a3, (unsigned int)(0x80000001ULL));
    if (*(unsigned __int64 *)(a2 + 72) != 0) goto loc_0097F959;
loc_0097F3B4:
    goto loc_0097EF7C;
loc_0097F3BB:
    if (v_stack_p10 == ((unsigned __int16)(v_stack_m128))) goto loc_0097EED1;
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)((unsigned int)(0x1000ULL))));
loc_0097F3F8:
    if (((0) & (16)) != 0) goto loc_0097EF3A;
    if ((*(unsigned __int64 *)(a2 + 72)) != ((unsigned int)(0xC000009AULL))) goto loc_0097EF3A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 64)))) & (2)) == 0) goto loc_0097EF3D;
    goto loc_0097EF3A;
loc_0097F41F:
    a1 = (unsigned int)((*(unsigned __int8 *)(a3 + 15)) << (12));
    result = (unsigned int)(((unsigned int)(v_stack_mE8)) ^ ((unsigned int)(a1)));
    result = (unsigned int)((result) & (0xF000ULL));
    result = (unsigned int)((result) ^ (v_stack_mE8));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) ^ ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) & (0x70000ULL));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
    v_stack_p58 = v_stack_p70;
    goto loc_0097F130;
loc_0097F44F:
    result = MiDoesImageContainFunctionOverrideFixups((unsigned int)(0xC000009AULL), a2, a3, (unsigned int)(0x80000001ULL));
    if ((unsigned int)(result) == 0) goto loc_0097EEF2;
    result = MiMapImageScpCfgPages(*(unsigned __int64 *)(a2 + 88), *(unsigned __int64 *)(a2 + 8), a3, (unsigned int)(0x80000001ULL));
    goto loc_0097EEF2;
loc_0097F46F:
    if ((((unsigned __int8)((unsigned int)(0x80000001ULL))) & ((unsigned __int8)(v_rbx))) != 0) goto loc_0097F738;
    v_stack_p50 = 0;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFDULL));
    goto loc_0097EB88;
loc_0097F488:
loc_0097F492:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 88) + 784)) != ((unsigned int)(0x80000001ULL))) goto loc_0097F50D;
loc_0097F49B:
    v_stack_m120 = 0;
    goto loc_0097F28E;
loc_0097F4A7:
    result = (unsigned int)((result) | (896));
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    v_rdi = (unsigned int)((v_rdi) | (16));
    *(unsigned int *)(result + 52) = (unsigned int)(v_stack_m120);
    a2 = (v_stack_m120) >> (32);
    *(unsigned __int8 *)(result + 34) = (unsigned __int8)(a2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 88) + 368))) & (1)) == 0) { v_rdi = 0; }
    goto loc_0097EC6D;
loc_0097F4D4:
    result = MiLogMapFileEvent(0, (unsigned int)(0x425ULL), a3, (unsigned int)(0x80000001ULL));
    goto loc_0097EEE1;
loc_0097F4E6:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 88) + 1040) + 1088)) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 88) + 1040) + 1088) = result;
    v_stack_p58 = v_stack_p70;
    goto loc_0097EE71;
loc_0097F50D:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 88) + 1772))) == 332) goto loc_0097F28E;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 88) + 1772))) == 452) goto loc_0097F28E;
    goto loc_0097F49B;
loc_0097F536:
    v_stack_p60 = 0x40000003ULL;
    if ((((unsigned __int8)(v_rbx)) & (2)) == 0) goto loc_0097ED60;
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) goto loc_0097F5A5;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8) + 8))))) & (63));
    result = (unsigned __int8)(-(result));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8) + 8))) >> (6);
    a2 = -(452);
    a2 = (a2) + (21);
    a2 = (a2) + (a1);
    a2 = (a2) << (3);
    result = MiAllocatePool(64, a2, (unsigned int)(0x49646156ULL), (unsigned int)(0x80000001ULL));
    if ((((unsigned __int8)(v_rbx)) & (8)) == 0) goto loc_0097ED60;
loc_0097F5A5:
    a4 = (unsigned int)(((unsigned int)(v_stack_p50)) | (1));
    v_stack_p60 = 0x40000036ULL;
    goto loc_0097ED65;
loc_0097F5BB:
loc_0097F5C2:
    if (result + 128 == 0) goto loc_0097EB96;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 128 + 32))) & (14));
    if (((unsigned __int8)(result)) >= 12) goto loc_0097F5DB;
    goto loc_0097F5C2;
loc_0097F5DB:
    result = MiArbitraryCodeBlocked(*(unsigned __int64 *)(a2 + 96), v_stack_p58, v_stack_p20, a4);
    if (sign_flag) goto loc_0097EF7C;
    goto loc_0097EB96;
loc_0097F5F2:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4907652)))) != (*(unsigned int *)(a4 + 60))) goto loc_0097E9C9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4907640)))) != (*(unsigned int *)(*(unsigned __int64 *)(v_stack_p68 + 56) + 68))) goto loc_0097E9C9;
    goto loc_0097E9C9;
loc_0097F61B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4907640)))) < (*(unsigned int *)(*(unsigned __int64 *)(v_stack_p68 + 56) + 68))) goto loc_0097E9F9;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p58))) | (5));
    v_stack_p50 = 1;
    goto loc_0097E9F9;
loc_0097F63D:
    v_stack_p10 = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 4907640)));
    goto loc_0097EA1F;
loc_0097F64D:
    result = HalAdjustResourceList((unsigned int)(*(unsigned int *)(v_rip + 4907640)), v_stack_p58, (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 4907640))), a4);
    v_rbx = (unsigned int)((v_rbx) | (4));
    v_r15 = (unsigned int)((1) | (2));
    v_stack_p50 = (unsigned int)(v_r15);
    goto loc_0097EA33;
loc_0097F66F:
    if (((*(unsigned int *)(a2 + 64)) & (0x2000000ULL)) != 0) goto loc_0097EA41;
    goto loc_0097EF7C;
loc_0097F688:
    if (v_rdi < ((unsigned int)(0xC0000022ULL))) goto loc_0097F738;
    if (((unsigned int)(v_rbx)) >= 4) goto loc_0097F738;
    result = 0;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFDULL));
    v_rbx = (unsigned int)((v_rbx) | (1));
    v_stack_p50 = 0;
    v_r10 = (*(unsigned __int64 *)(a2 + 24)) + (0x1FFFFFULL);
    v_r10 = (v_r10) & (0xFFFFFFFFFFE00000ULL);
    v_stack_m138 = (unsigned int)(0x200000ULL);
    v_stack_m130 = v_r10;
    goto loc_0097EA6C;
loc_0097F6D4:
    goto loc_0097EF7C;
loc_0097F6DE:
    goto loc_0097EF7C;
loc_0097F6E8:
    if (((*(unsigned __int8 *)(v_stack_m100 + 51)) & ((unsigned __int8)(a4))) != 0) goto loc_0097F251;
    if (((4) & (8)) == 0) goto loc_0097F251;
loc_0097F70E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 88) + 1872)))) & (64)) != 0) goto loc_0097EB59;
loc_0097F71D:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFDULL));
    v_rbx = (unsigned int)((v_rbx) | (1));
    goto loc_0097EB59;
loc_0097F728:
    v_stack_p50 = (unsigned int)((unsigned int)(0x200000ULL));
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFF9ULL));
    goto loc_0097EB73;
loc_0097F738:
    goto loc_0097EF7C;
loc_0097F742:
    result = MiDereferenceControlArea(0, v_stack_m100, (unsigned int)(0x200000ULL), a4);
    goto loc_0097EF7C;
loc_0097F754:
    v_rbx = (unsigned int)((v_rbx) | (8));
    goto loc_0097EBDC;
loc_0097F75C:
    v_rdi = (unsigned int)((v_rdi) | (8));
    goto loc_0097EC4C;
loc_0097F764:
    if (0 == 0x200000ULL) goto loc_0097EC91;
    v_stack_p58 = *(unsigned __int64 *)(v_stack_p18);
    v_stack_p70 = *(unsigned __int64 *)(v_stack_p18);
    goto loc_0097ECB9;
loc_0097F78A:
    goto loc_0097F796;
loc_0097F791:
loc_0097F796:
loc_0097F79E:
    goto loc_0097F796;
loc_0097F7A5:
    if (result < ((unsigned int)(0x200000ULL))) goto loc_0097F283;
    v_r15 = result;
    if (((*(unsigned __int16 *)(v_stack_p18 + 12)) & ((unsigned __int16)((unsigned int)(0x4000ULL)))) == 0) { v_r15 = (unsigned int)(0xFFFFFFFFULL); }
    goto loc_0097F283;
loc_0097F7C5:
    a1 = (0) - (v_stack_p18);
    goto loc_0097EDA4;
loc_0097F7D1:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 88) + 1532))) >> (13));
    a3 = (unsigned int)((a3) & (1));
    result = MiInitializeFixupVad(v_r15, (unsigned int)((unsigned int)(a4)), a3, a4);
    goto loc_0097EDE0;
loc_0097F7F0:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 88) + 1040) + 1060) = 1;
    goto loc_0097EDED;
loc_0097F803:
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(a2 + 88), (unsigned int)((unsigned int)(a4)), a3, a4);
    result = MiCreatePerSessionProtos(result, (unsigned int)((unsigned int)(result)), a3, a4);
    if (sign_flag) goto loc_0097F829;
    goto loc_0097EE02;
loc_0097F824:
loc_0097F829:
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(a2 + 88), (unsigned int)((unsigned int)(result)), a3, a4);
    result = MiDereferencePerSessionProtos(result, (unsigned int)((unsigned int)(result)), a3, a4);
loc_0097F84B:
    v_rsi = (unsigned int)(-((unsigned int)(0xC000060BULL)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (256));
    a2 = (unsigned int)((a2) + (8));
    result = MiReferenceActiveSubsection(result + 128, a2, 17, a4);
    if (sign_flag) goto loc_0097F829;
    goto loc_0097EE53;
loc_0097F876:
    result = MiLockVad(v_stack_p78, v_r15, 17, a4);
    a4 = 0;
    a3 = 0;
    result = MiMapUserLargePages(v_r15, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    result = UNLOCK_ADDRESS_SPACE(v_stack_p78, *(unsigned __int64 *)(a2 + 88), a3, a4);
    goto loc_0097F386;
loc_0097F8AF:
    result = (unsigned int)(((unsigned int)(v_stack_p60)) + (0xBFFFFFFDULL));
    if (((unsigned int)(result)) < 51) goto loc_0097EF0F;
loc_0097F8DA:
    goto loc_0097F168;
loc_0097F8E4:
    v_rsi = 0;
    goto loc_0097EF3D;
loc_0097F8EB:
    result = MiUpdatePrivateDemandZeroView(*(unsigned __int64 *)(a2 + 88), v_r15, 1, a4);
    result = MiRemoveVadEvent(v_r15, v_stack_mA8, 1, a4);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFBFULL));
    goto loc_0097F036;
loc_0097F910:
    goto loc_0097F388;
loc_0097F947:
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x63536D4DULL), 1, (unsigned int)(*(unsigned int *)(a2 + 68)));
    goto loc_0097F399;
loc_0097F959:
    *(unsigned __int64 *)(result) = v_rdi;
    goto loc_0097F3B4;
loc_0097F961:
    result = MiSoftFaultMappedView(v_r15, (unsigned int)(0x63536D4DULL), 1, (unsigned int)(*(unsigned int *)(a2 + 68)));
    goto loc_0097F06D;
loc_0097F96E:
    goto loc_0097EF78;
}
```

## 5. (Beta) C Style

```c
int64_t MiMapViewOfImageSection(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint8_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint16_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m198;
    uint32_t v_stack_m58;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint8_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint16_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint8_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (376);
    local_rbx = 0;
    v_stack_m148 = 0;
    Arg2 = 0;
    v_stack_m110 = 0;
    v_stack_mF8 = 0;
    result = memset(v_stack_mA8, Arg2, local_rbx + 88, Arg4);
    result = 0;
    local_r14 = (*(uint64_t *)(arg1 + 0x60)) & (-8);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x28))) >> (22));
    v_stack_mC0 = 0;
    Arg2 = (uint32_t)((Arg2) & (2));
    v_stack_m168 = 0;
    v_stack_m150 = *(uint64_t *)(arg1);
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    v_stack_m100 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x38);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AEED4))) != 0) goto loc_0097F5F2;
loc_0097E9C9:
    v_stack_m120 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x30);
    v_stack_m118 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x20);
    if (((*(uint32_t *)(arg1 + 0x38)) & (0x20000000ULL)) != 0) goto loc_0097F61B;
    if (((*(uint32_t *)(*(uint64_t *)(arg2 + 0x58) + 0x5FC)) & (0x2000ULL)) != 0) goto loc_0097F61B;
loc_0097E9F9:
    v_stack_m128 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x58) + 0x6EC));
    v_stack_p10 = (uint16_t)(*(uint16_t *)(arg2 + 0x3A));
    if ((uint16_t)(*(uint16_t *)(arg2 + 0x3A)) == 0) goto loc_0097F1F5;
loc_0097EA1F:
    if (((uint16_t)((uint16_t)(*(uint16_t *)(arg2 + 0x3A)))) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x38) + 0x30)))) goto loc_0097F64D;
loc_0097EA33:
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x58) + 0x170)) & (1)) != 0) goto loc_0097F66F;
loc_0097EA41:
    v_stack_m138 = *(uint64_t *)(arg2 + 0x10);
    v_stack_m130 = *(uint64_t *)(arg2 + 0x18);
    if (condition_is_below) goto loc_0097F688;
loc_0097EA6C:
    if (Arg5 == 0) goto loc_0097EA8D;
    Arg1 = (((*(uint32_t *)(Arg5 + 0x38)) & (0x80000ULL)) == 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0097EA9E;
loc_0097EA8D:
    if (Arg7 != 1) goto loc_0097F6D4;
loc_0097EA9E:
    Arg1 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AEE08))) == 0) goto loc_0097EB2D;
    Arg1 = (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x38) + 0x4C)) & (64)) != 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0097EB2D;
    if ((*(uint64_t *)(arg2 + 0x10)) == 0x200000ULL) goto loc_0097EB2D;
    Arg1 = (((*(uint64_t *)(arg2 + 0x18)) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (*(uint64_t *)(arg2 + 0x18)) >> (12);
    Arg1 = (Arg1) + (result);
    if (Arg1 != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)))) goto loc_0097F1B4;
    Arg1 = (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x58) + 0x7DC)) & (4)) == 0) ? 1 : 0;
    result = (((Arg8) & (16)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0097F1B4;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AEE08)))) + *(uint64_t *)(arg2 + 0x18) * 1) < (*(uint64_t *)(arg2 + 0x18))) goto loc_0097F6DE;
    v_stack_m130 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AEE08)))) + *(uint64_t *)(arg2 + 0x18) * 1;
    goto loc_0097EB30;
loc_0097EB2D:
    Arg3 = 0;
loc_0097EB30:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) < 0x400ULL) goto loc_0097F21C;
loc_0097EB42:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) < 0x400ULL) goto loc_0097F71D;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) < 0x400ULL) goto loc_0097F70E;
loc_0097EB59:
    if (((v_stack_p40) & (4)) != 0) goto loc_0097F728;
    if ((*(uint64_t *)(arg2 + 0x58)) == (*(uint64_t *)(v_rip + 0x64814B))) goto loc_0097F728;
loc_0097EB73:
    if ((*(uint64_t *)(local_r14 + 0x20)) == 0) goto loc_0097F46F;
    if ((*(uint64_t *)(local_r14 + 0x20)) < 0) goto loc_0097F46F;
loc_0097EB88:
    v_stack_m108 = 0;
    if ((*(uint64_t *)(local_r14 + 0x20)) >= 0) goto loc_0097F5BB;
loc_0097EB96:
    v_stack_mB8 = Arg1 + 128;
    result = MiCheckPurgeAndUpMapCount(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AEE08)))), Arg3, 4);
    if (0 != 0) goto loc_0097EF91;
loc_0097EBBD:
    result = MiAllocatePool(64, 136, (uint32_t)(0x20646156ULL), 4);
    if (result == 0) goto loc_0097F742;
    if (0 != 0) goto loc_0097F754;
loc_0097EBDC:
    local_r15 = 0;
    *(uint64_t *)(result + 0x10) = -2;
    *(uint64_t *)(result) = -2;
    *(uint64_t *)(result + 0x8) = -2;
    result = 0;
    if (Arg6 == 1) { result = (uint32_t)(local_r15 + 4); }
    local_rdi = (uint32_t)((32) | ((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xFFFFFFAFULL));
    Arg1 = (uint32_t)((Arg1) | (32));
    *(uint32_t *)(result + 0x30) = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x34))) << (12));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
    result = (uint32_t)((result) & (0x7F000ULL));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    if (Arg5 == 0) goto loc_0097EC4C;
    result = MiReferenceFileObjectForMap(Arg5, 136, (uint32_t)(0x20646156ULL), 4);
    *(uint64_t *)(result + 0x80) = result;
    if ((*(uint32_t *)(Arg5 + 0x3C)) < 0) goto loc_0097F75C;
loc_0097EC4C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xFFFFF0FFULL));
    *(uint64_t *)(result + 0x28) = 0;
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    if (condition_is_above_or_equal) goto loc_0097F4A7;
loc_0097EC6D:
    v_stack_m158 = 0;
    v_stack_m140 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x3C)))) & (1)) != 0) goto loc_0097F764;
loc_0097EC91:
    local_r15 = ((uint32_t)(*(uint32_t *)(v_stack_p20))) + (v_stack_m118);
    v_stack_m160 = local_r15;
    v_stack_m148 = local_r15;
loc_0097ECB9:
    result = MiWriteVadFlags2(result, (uint32_t)((uint32_t)(local_rdi)), 1, 4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xF80ULL));
    if (((uint32_t)(result)) == 896) goto loc_0097F0D5;
loc_0097ECDD:
    v_stack_m58 = 32;
    result = LOCK_ADDRESS_SPACE(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg2 + 0x58), 1, 4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x58) + 0x1F4)))) & (32)) != 0) goto loc_0097F78A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x3C)))) & (1)) == 0) goto loc_0097EFBD;
    if (v_stack_m138 == 0x200000ULL) goto loc_0097EFBD;
    v_stack_m198 = *(uint64_t *)(arg2 + 0x8);
    result = MiIsVaRangeAvailable(*(uint64_t *)(arg2 + 0x58), local_r15, v_stack_m130, *(uint64_t *)(arg2));
    if ((uint32_t)(result) == 0) goto loc_0097F79E;
loc_0097ED3E:
    Arg1 = (v_stack_m160) - ((uint32_t)(*(uint32_t *)(v_stack_p20)));
    if (Arg1 != v_stack_m118) goto loc_0097F536;
loc_0097ED60:
loc_0097ED65:
    Arg1 = (v_stack_m160) >> (12);
    result = (v_stack_m130) - 1;
    result = (result) + (v_stack_m160);
    v_stack_m118 = Arg1;
    result = (result) >> (12);
    v_stack_m120 = result;
    result = MiUpdateVadStartVpn(result, Arg1, v_stack_p20, (uint32_t)(v_stack_m168));
    *(uint32_t *)(result + 0x1C) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint8_t *)(result + 0x21) = (uint8_t)(result);
    Arg1 = (*(uint64_t *)(v_stack_p20)) >> (12);
loc_0097EDA4:
    if (Arg1 >= ((uint32_t)(*(uint32_t *)(v_stack_mB8 + 0x2C)))) goto loc_0097F7C5;
    *(uint64_t *)(result + 0x48) = v_stack_mB8;
    *(uint64_t *)(result + 0x50) = *(uint64_t *)(v_stack_mB8 + 0x8) + Arg1 * 8;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x8))) - 1;
    *(uint64_t *)(result + 0x58) = *(uint64_t *)(v_stack_m150 + 0x40) + Arg1 * 8;
    if ((((uint8_t)((uint32_t)((uint32_t)(Arg2)))) & (8)) != 0) goto loc_0097F7D1;
loc_0097EDE0:
    result = 0;
    if ((*(uint32_t *)(arg2 + 0x34)) != 0) goto loc_0097F7F0;
loc_0097EDED:
    if (((*(uint32_t *)(v_stack_p8 + 0x38)) & (0x8000000ULL)) != 0) goto loc_0097F803;
loc_0097EE02:
    Arg3 = 0;
    result = MiInsertSharedCommitNode(v_stack_p8, *(uint64_t *)(arg2 + 0x58), Arg3, (uint32_t)(v_stack_m168));
    Arg4 = 0;
    if (sign_flag) goto loc_0097F829;
    local_rsi = (uint32_t)(((uint32_t)(Arg8)) & (8));
    Arg2 = (condition_is_not_equal) ? 1 : 0;
    result = MiControlAreaRequiresCharge(v_stack_p8, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0097F824;
    if (((uint32_t)(result)) == 2) goto loc_0097F84B;
loc_0097EE53:
    result = MiInsertVadCharges(result, *(uint64_t *)(arg2 + 0x58), Arg3, Arg4);
    if (sign_flag) goto loc_0097F829;
    if ((((uint8_t)((uint32_t)((uint32_t)(Arg2)))) & (8)) != 0) goto loc_0097F4E6;
loc_0097EE71:
    Arg3 = 0;
    result = MiInsertVad(result, *(uint64_t *)(arg2 + 0x58), Arg3, Arg4);
    local_rsi = 0;
    if (v_stack_m138 == 0x200000ULL) goto loc_0097F876;
    if (v_stack_m110 != 0) goto loc_0097F0C3;
loc_0097EE9F:
    Arg1 = (v_stack_m108) << (16);
    result = (v_stack_m160) + (Arg1);
    v_stack_m160 = result;
    v_stack_m148 = result;
    *(uint64_t *)(v_stack_p18) = result;
    if ((*(uint8_t *)(v_stack_m100 + 0x32)) != 0) goto loc_0097F3BB;
loc_0097EED1:
    if (((*(uint32_t *)(v_rip + 0x647C25)) & (0x8000ULL)) != 0) goto loc_0097F4D4;
loc_0097EEE1:
    if ((((uint8_t)(local_rdi)) & (32)) != 0) goto loc_0097F44F;
loc_0097EEF2:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | (16));
    if (condition_is_below) goto loc_0097F8E4;
    if (((*(uint32_t *)(v_rip + 0x6453B7)) & (0x40000ULL)) != 0) goto loc_0097F8AF;
loc_0097EF0F:
    result = MiReadVadFlags2(result, *(uint64_t *)(arg2 + 0x58), v_stack_m150, Arg4);
    if ((((uint32_t)((uint32_t)(0x800ULL))) & ((uint32_t)(local_rbx))) != 0) goto loc_0097F119;
loc_0097EF2D:
    local_rsi = 0;
    if ((*(uint32_t *)(arg2 + 0x78)) == 0) goto loc_0097F3F8;
loc_0097EF3A:
    local_rbx = (uint32_t)((local_rbx) | (32));
loc_0097EF3D:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_0097F009;
loc_0097EF4B:
    if ((((uint8_t)(local_rbx)) & (16)) != 0) {
        Arg2 = *(uint64_t *)(arg2 + 0x58);
        Arg1 = v_stack_m140;
        result = UNLOCK_ADDRESS_SPACE(Arg1, Arg2, v_stack_m150, (uint32_t)(0x800ULL));
    }
    if (condition_is_below) goto loc_0097EF78;
    if (Arg5 == 0) goto loc_0097EF78;
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x58) + 0x170)) & (1)) == 0) goto loc_0097F96E;
loc_0097EF78:
loc_0097EF7C:
    local_rsp = (local_rsp) + (376);
    return (uint32_t)(v_stack_m158);
loc_0097EF91:
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi) + 0x8))))) & (63));
    result = (uint8_t)(-(result));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi) + 0x8))) >> (6);
    Arg2 = -(Arg2);
    Arg2 = (Arg2) + (21);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) << (3);
    goto loc_0097EBBD;
loc_0097EFBD:
    if (v_stack_m130 > result) goto loc_0097F791;
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_0097F25B;
    v_stack_p20 = *(uint64_t *)(arg2 + 0x8);
    result = MiIsVaRangeAvailable(*(uint64_t *)(arg2 + 0x58), v_stack_m140, v_stack_m130, *(uint64_t *)(arg2));
    Arg4 = 0;
    if ((uint32_t)(result) != 0) goto loc_0097ED3E;
    goto loc_0097F25E;
loc_0097F009:
    result = MiLockVad(v_stack_p78, v_stack_m140, v_stack_m130, Arg4);
    result = UNLOCK_ADDRESS_SPACE(v_stack_p78, *(uint64_t *)(arg2 + 0x58), v_stack_m130, Arg4);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFEFULL));
    result = MiReadVadFlags2(v_stack_m140, *(uint64_t *)(arg2 + 0x58), v_stack_m130, Arg4);
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_0097F8EB;
loc_0097F036:
    local_rdi = 0;
    if (condition_is_above_or_equal) goto loc_0097F18D;
loc_0097F042:
    if ((*(uint64_t *)(arg2 + 0x48)) != 0) goto loc_0097F910;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & ((uint32_t)((uint32_t)(0x800ULL))));
    if (condition_is_not_equal) goto loc_0097F348;
loc_0097F060:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40)))) & (2)) != 0) goto loc_0097F961;
loc_0097F06D:
    result = MiUnlockVad(v_stack_p78, v_stack_m140, v_stack_m130, Arg4);
    if ((uint32_t)(local_rsi) != 0) {
        Arg1 = 0 + 88;
        Arg4 = 0;
        Arg3 = v_stack_mF0;
        Arg2 = *(uint64_t *)(arg2 + 0x58);
        result = PsCallImageNotifyRoutines(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 0x63536D4DULL;
        Arg1 = 0;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = 0;
    if (v_stack_mF8 == 0) goto loc_0097EF4B;
    Arg1 = (*(uint64_t *)(arg2 + 0x58)) ^ (v_stack_mF8);
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_rip + 0x4AEAC7));
    result = MmUnsecureVirtualMemory(Arg1, Arg2, Arg3, Arg4);
    goto loc_0097EF4B;
loc_0097F0C3:
    result = MiAdvanceVadHint(v_stack_m118, v_stack_m120, Arg3, Arg4);
    goto loc_0097EE9F;
loc_0097F0D5:
    Arg2 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x58) + 0x1D0)) == 0) goto loc_0097ECDD;
    if (((*(uint32_t *)(*(uint64_t *)(arg2 + 0x58) + 0x5FC)) & (0x1000ULL)) != 0) goto loc_0097ECDD;
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x58) + 0x170)) & (1)) != 0) goto loc_0097ECDD;
    result = PsIsImageNotifyEnabled(v_stack_m118, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0097ECDD;
    goto loc_0097ECDD;
loc_0097F119:
    v_stack_mE8 = 3;
    if ((((uint8_t)(v_stack_mF8)) & (8)) == 0) goto loc_0097F41F;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mE8)) & (0xFFF80FFFULL));
loc_0097F130:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (1));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg2)));
    result = (uint32_t)((result) & ((uint32_t)(Arg4)));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg2)));
    v_stack_mE8 = (uint32_t)(result);
    Arg1 = (v_stack_m118) | (-1);
    v_stack_mE0 = v_stack_p58;
    v_stack_mD0 = *(uint64_t *)(arg2 + 0x18);
    if ((*(uint64_t *)(arg2 + 0x18)) != Arg1) goto loc_0097F8DA;
loc_0097F168:
    result = 0;
    v_stack_mD8 = 0;
    v_stack_mC8 = 0;
    result = MiReferenceControlAreaFile(0, Arg2, Arg3, Arg4);
    local_rbx = (uint32_t)((local_rbx) | (32));
    v_stack_p58 = v_stack_p70;
    goto loc_0097EF2D;
loc_0097F18D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x78))) == 0) goto loc_0097F042;
    Arg2 = 0;
    result = MiCommitVadMetadataBits(v_stack_p78, Arg2, (uint32_t)(*(uint32_t *)(arg2 + 0x78)), Arg4);
    if (!sign_flag) goto loc_0097F042;
    goto loc_0097F388;
loc_0097F1B4:
    result = MiDoesImageContainFunctionOverrideFixups((uint32_t)((uint32_t)(result)), Arg2, (uint32_t)(*(uint32_t *)(arg2 + 0x78)), Arg4);
    Arg3 = 0;
    if ((uint32_t)(result) == 0) goto loc_0097EB30;
    result = ((uint32_t)(*(uint32_t *)(Arg4 + 0x40))) + (0xFFFULL);
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    if ((*(uint64_t *)(arg2 + 0x18)) <= result) goto loc_0097EB30;
loc_0097F1F5:
    if ((*(uint64_t *)(arg2 + 0x18)) < result) goto loc_0097F20A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x58) + 0x5FC)))) & (1)) == 0) goto loc_0097F63D;
loc_0097F20A:
    v_stack_p10 = (uint16_t)(*(uint16_t *)(Arg4 + 0x30));
    goto loc_0097EA1F;
loc_0097F21C:
    result = MiAllowImageMap(*(uint64_t *)(arg2 + 0x58), Arg5, (uint32_t)((uint32_t)(result)), v_stack_m100);
    Arg3 = 0;
    if (sign_flag) goto loc_0097EF7C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x58) + 0x750)))) & (16)) != 0) goto loc_0097F6E8;
loc_0097F251:
    goto loc_0097EB42;
loc_0097F25B:
    Arg4 = 0;
loc_0097F25E:
    v_stack_m120 = 0;
    if (v_stack_m118 < 0) goto loc_0097F7A5;
loc_0097F283:
    if ((*(uint16_t *)(v_stack_p68 + 0xC)) < 0) goto loc_0097F492;
loc_0097F28E:
    if ((*(uint64_t *)(arg2)) >= (*(uint64_t *)(arg2 + 0x8))) goto loc_0097F488;
    v_stack_p48 = v_stack_p70;
    v_stack_p40 = v_stack_m110;
    v_stack_p38 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) >> (7));
    result = (uint32_t)((result) & (31));
    v_stack_p30 = (uint32_t)(result);
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_m138;
    result = MiSelectUserAddress((uint32_t)(*(uint32_t *)(arg2 + 0x28)), *(uint64_t *)(arg2), *(uint64_t *)(arg2 + 0x8), (uint32_t)((uint32_t)(result)));
    Arg4 = 0;
    v_stack_p58 = v_stack_p70;
    if (v_stack_m138 != 0x200000ULL) goto loc_0097ED3E;
    result = (v_stack_m130) - (*(uint64_t *)(arg2 + 0x18));
    result = ExGenRandom(1, *(uint64_t *)(arg2), *(uint64_t *)(arg2 + 0x18), Arg4);
    Arg1 = (v_stack_m130) - (*(uint64_t *)(arg2 + 0x18));
    Arg1 = (Arg1) >> (16);
    Arg2 = 0;
    v_stack_m108 = 0;
loc_0097F348:
    Arg4 = 0;
    Arg3 = (v_stack_m120) << (12);
    v_stack_p20 = 0;
    Arg3 = (Arg3) | (0xFFFULL);
    Arg2 = (v_stack_m118) << (12);
    result = MiAddSecureEntry(*(uint64_t *)(arg2 + 0x8), Arg2, Arg3, (uint32_t)(0x80000001ULL));
    if (result != 0) goto loc_0097F060;
loc_0097F386:
    local_rdi = 0;
loc_0097F388:
    result = MiReferenceVad(*(uint64_t *)(arg2 + 0x8), Arg2, Arg3, (uint32_t)(0x80000001ULL));
    if (result != 0) goto loc_0097F947;
loc_0097F399:
    Arg3 = 0;
    Arg2 = 0;
    result = MiUnmapVad(*(uint64_t *)(arg2 + 0x8), Arg2, Arg3, (uint32_t)(0x80000001ULL));
    if (*(uint64_t *)(arg2 + 0x48) != 0) goto loc_0097F959;
loc_0097F3B4:
    goto loc_0097EF7C;
loc_0097F3BB:
    if (v_stack_p10 == ((uint16_t)(v_stack_m128))) goto loc_0097EED1;
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)((uint32_t)(0x1000ULL))));
loc_0097F3F8:
    if (((0) & (16)) != 0) goto loc_0097EF3A;
    if ((*(uint64_t *)(arg2 + 0x48)) != ((uint32_t)(0xC000009AULL))) goto loc_0097EF3A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40)))) & (2)) == 0) goto loc_0097EF3D;
    goto loc_0097EF3A;
loc_0097F41F:
    Arg1 = (uint32_t)((*(uint8_t *)(Arg3 + 0xF)) << (12));
    result = (uint32_t)(((uint32_t)(v_stack_mE8)) ^ ((uint32_t)(Arg1)));
    result = (uint32_t)((result) & (0xF000ULL));
    result = (uint32_t)((result) ^ (v_stack_mE8));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) ^ ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) & (0x70000ULL));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
    v_stack_p58 = v_stack_p70;
    goto loc_0097F130;
loc_0097F44F:
    result = MiDoesImageContainFunctionOverrideFixups((uint32_t)(0xC000009AULL), Arg2, Arg3, (uint32_t)(0x80000001ULL));
    if ((uint32_t)(result) == 0) goto loc_0097EEF2;
    result = MiMapImageScpCfgPages(*(uint64_t *)(arg2 + 0x58), *(uint64_t *)(arg2 + 0x8), Arg3, (uint32_t)(0x80000001ULL));
    goto loc_0097EEF2;
loc_0097F46F:
    if ((((uint8_t)((uint32_t)(0x80000001ULL))) & ((uint8_t)(local_rbx))) != 0) goto loc_0097F738;
    v_stack_p50 = 0;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFDULL));
    goto loc_0097EB88;
loc_0097F488:
loc_0097F492:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x58) + 0x310)) != ((uint32_t)(0x80000001ULL))) goto loc_0097F50D;
loc_0097F49B:
    v_stack_m120 = 0;
    goto loc_0097F28E;
loc_0097F4A7:
    result = (uint32_t)((result) | (896));
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    local_rdi = (uint32_t)((local_rdi) | (16));
    *(uint32_t *)(result + 0x34) = (uint32_t)(v_stack_m120);
    Arg2 = (v_stack_m120) >> (32);
    *(uint8_t *)(result + 0x22) = (uint8_t)(Arg2);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x58) + 0x170))) & (1)) == 0) { local_rdi = 0; }
    goto loc_0097EC6D;
loc_0097F4D4:
    result = MiLogMapFileEvent(0, (uint32_t)(0x425ULL), Arg3, (uint32_t)(0x80000001ULL));
    goto loc_0097EEE1;
loc_0097F4E6:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x58) + 0x410) + 0x440)) + 1;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x58) + 0x410) + 0x440) = result;
    v_stack_p58 = v_stack_p70;
    goto loc_0097EE71;
loc_0097F50D:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x58) + 0x6EC))) == 332) goto loc_0097F28E;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x58) + 0x6EC))) == 452) goto loc_0097F28E;
    goto loc_0097F49B;
loc_0097F536:
    v_stack_p60 = 0x40000003ULL;
    if ((((uint8_t)(local_rbx)) & (2)) == 0) goto loc_0097ED60;
    if ((((uint8_t)(local_rbx)) & (8)) != 0) goto loc_0097F5A5;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8) + 0x8))))) & (63));
    result = (uint8_t)(-(result));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8) + 0x8))) >> (6);
    Arg2 = -(452);
    Arg2 = (Arg2) + (21);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) << (3);
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x49646156ULL), (uint32_t)(0x80000001ULL));
    if ((((uint8_t)(local_rbx)) & (8)) == 0) goto loc_0097ED60;
loc_0097F5A5:
    Arg4 = (uint32_t)(((uint32_t)(v_stack_p50)) | (1));
    v_stack_p60 = 0x40000036ULL;
    goto loc_0097ED65;
loc_0097F5BB:
loc_0097F5C2:
    if (result + 128 == 0) goto loc_0097EB96;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x80 + 0x20))) & (14));
    if (((uint8_t)(result)) >= 12) goto loc_0097F5DB;
    goto loc_0097F5C2;
loc_0097F5DB:
    result = MiArbitraryCodeBlocked(*(uint64_t *)(arg2 + 0x60), v_stack_p58, v_stack_p20, Arg4);
    if (sign_flag) goto loc_0097EF7C;
    goto loc_0097EB96;
loc_0097F5F2:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AE284)))) != (*(uint32_t *)(Arg4 + 0x3C))) goto loc_0097E9C9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AE278)))) != (*(uint32_t *)(*(uint64_t *)(v_stack_p68 + 0x38) + 0x44))) goto loc_0097E9C9;
    goto loc_0097E9C9;
loc_0097F61B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AE278)))) < (*(uint32_t *)(*(uint64_t *)(v_stack_p68 + 0x38) + 0x44))) goto loc_0097E9F9;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p58))) | (5));
    v_stack_p50 = 1;
    goto loc_0097E9F9;
loc_0097F63D:
    v_stack_p10 = (uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AE278)));
    goto loc_0097EA1F;
loc_0097F64D:
    result = HalAdjustResourceList((uint32_t)(*(uint32_t *)(v_rip + 0x4AE278)), v_stack_p58, (uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4AE278))), Arg4);
    local_rbx = (uint32_t)((local_rbx) | (4));
    local_r15 = (uint32_t)((1) | (2));
    v_stack_p50 = (uint32_t)(local_r15);
    goto loc_0097EA33;
loc_0097F66F:
    if (((*(uint32_t *)(arg2 + 0x40)) & (0x2000000ULL)) != 0) goto loc_0097EA41;
    goto loc_0097EF7C;
loc_0097F688:
    if (local_rdi < ((uint32_t)(0xC0000022ULL))) goto loc_0097F738;
    if (((uint32_t)(local_rbx)) >= 4) goto loc_0097F738;
    result = 0;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFDULL));
    local_rbx = (uint32_t)((local_rbx) | (1));
    v_stack_p50 = 0;
    local_r10 = (*(uint64_t *)(arg2 + 0x18)) + (0x1FFFFFULL);
    local_r10 = (local_r10) & (0xFFFFFFFFFFE00000ULL);
    v_stack_m138 = (uint32_t)(0x200000ULL);
    v_stack_m130 = local_r10;
    goto loc_0097EA6C;
loc_0097F6D4:
    goto loc_0097EF7C;
loc_0097F6DE:
    goto loc_0097EF7C;
loc_0097F6E8:
    if (((*(uint8_t *)(v_stack_m100 + 0x33)) & ((uint8_t)(Arg4))) != 0) goto loc_0097F251;
    if (((4) & (8)) == 0) goto loc_0097F251;
loc_0097F70E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x58) + 0x750)))) & (64)) != 0) goto loc_0097EB59;
loc_0097F71D:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFDULL));
    local_rbx = (uint32_t)((local_rbx) | (1));
    goto loc_0097EB59;
loc_0097F728:
    v_stack_p50 = (uint32_t)((uint32_t)(0x200000ULL));
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFF9ULL));
    goto loc_0097EB73;
loc_0097F738:
    goto loc_0097EF7C;
loc_0097F742:
    result = MiDereferenceControlArea(0, v_stack_m100, (uint32_t)(0x200000ULL), Arg4);
    goto loc_0097EF7C;
loc_0097F754:
    local_rbx = (uint32_t)((local_rbx) | (8));
    goto loc_0097EBDC;
loc_0097F75C:
    local_rdi = (uint32_t)((local_rdi) | (8));
    goto loc_0097EC4C;
loc_0097F764:
    if (0 == 0x200000ULL) goto loc_0097EC91;
    v_stack_p58 = *(uint64_t *)(v_stack_p18);
    v_stack_p70 = *(uint64_t *)(v_stack_p18);
    goto loc_0097ECB9;
loc_0097F78A:
    goto loc_0097F796;
loc_0097F791:
loc_0097F796:
loc_0097F79E:
    goto loc_0097F796;
loc_0097F7A5:
    if (result < ((uint32_t)(0x200000ULL))) goto loc_0097F283;
    local_r15 = result;
    if (((*(uint16_t *)(v_stack_p18 + 0xC)) & ((uint16_t)((uint32_t)(0x4000ULL)))) == 0) { local_r15 = (uint32_t)(0xFFFFFFFFULL); }
    goto loc_0097F283;
loc_0097F7C5:
    Arg1 = (0) - (v_stack_p18);
    goto loc_0097EDA4;
loc_0097F7D1:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x58) + 0x5FC))) >> (13));
    Arg3 = (uint32_t)((Arg3) & (1));
    result = MiInitializeFixupVad(local_r15, (uint32_t)((uint32_t)(Arg4)), Arg3, Arg4);
    goto loc_0097EDE0;
loc_0097F7F0:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x58) + 0x410) + 0x424) = 1;
    goto loc_0097EDED;
loc_0097F803:
    result = PsGetProcessSessionIdEx(*(uint64_t *)(arg2 + 0x58), (uint32_t)((uint32_t)(Arg4)), Arg3, Arg4);
    result = MiCreatePerSessionProtos(result, (uint32_t)((uint32_t)(result)), Arg3, Arg4);
    if (sign_flag) goto loc_0097F829;
    goto loc_0097EE02;
loc_0097F824:
loc_0097F829:
    result = PsGetProcessSessionIdEx(*(uint64_t *)(arg2 + 0x58), (uint32_t)((uint32_t)(result)), Arg3, Arg4);
    result = MiDereferencePerSessionProtos(result, (uint32_t)((uint32_t)(result)), Arg3, Arg4);
loc_0097F84B:
    local_rsi = (uint32_t)(-((uint32_t)(0xC000060BULL)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (256));
    Arg2 = (uint32_t)((Arg2) + (8));
    result = MiReferenceActiveSubsection(result + 128, Arg2, 17, Arg4);
    if (sign_flag) goto loc_0097F829;
    goto loc_0097EE53;
loc_0097F876:
    result = MiLockVad(v_stack_p78, local_r15, 17, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = MiMapUserLargePages(local_r15, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    result = UNLOCK_ADDRESS_SPACE(v_stack_p78, *(uint64_t *)(arg2 + 0x58), Arg3, Arg4);
    goto loc_0097F386;
loc_0097F8AF:
    result = (uint32_t)(((uint32_t)(v_stack_p60)) + (0xBFFFFFFDULL));
    if (((uint32_t)(result)) < 51) goto loc_0097EF0F;
loc_0097F8DA:
    goto loc_0097F168;
loc_0097F8E4:
    local_rsi = 0;
    goto loc_0097EF3D;
loc_0097F8EB:
    result = MiUpdatePrivateDemandZeroView(*(uint64_t *)(arg2 + 0x58), local_r15, 1, Arg4);
    result = MiRemoveVadEvent(local_r15, v_stack_mA8, 1, Arg4);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFBFULL));
    goto loc_0097F036;
loc_0097F910:
    goto loc_0097F388;
loc_0097F947:
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x63536D4DULL), 1, (uint32_t)(*(uint32_t *)(arg2 + 0x44)));
    goto loc_0097F399;
loc_0097F959:
    *(uint64_t *)(result) = local_rdi;
    goto loc_0097F3B4;
loc_0097F961:
    result = MiSoftFaultMappedView(local_r15, (uint32_t)(0x63536D4DULL), 1, (uint32_t)(*(uint32_t *)(arg2 + 0x44)));
    goto loc_0097F06D;
loc_0097F96E:
    goto loc_0097EF78;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R` |
| `Arg2` | `+ 0x34` | `32` | `R` |
| `Arg2` | `+ 0x3A` | `16` | `R` |
| `Arg2` | `+ 0x3C` | `32` | `R` |
| `Arg2` | `+ 0x3C` | `32` | `R/W` |
| `Arg2` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x44` | `32` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x78` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097E92C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
