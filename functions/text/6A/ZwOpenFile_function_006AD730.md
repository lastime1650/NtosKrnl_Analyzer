# ZwOpenFile

- RVA: `0x006AD730`–`0x006AD74F` (길이 `31` bytes)
- VA: `0x00000001406AD730`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C00F4`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **63**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DbgkPostModuleMessage](../49/DbgkPostModuleMessage_function_004913C4.md) at `0x004914AB`
- [EtwpGetDriverDataDosPath](../4D/EtwpGetDriverDataDosPath_function_004DDF10.md) at `0x004DDFB2`
- [SecureDump_LoadCertAndProvisionKey](../5A/SecureDump_LoadCertAndProvisionKey_function_005A2E04.md) at `0x005A2F03`
- [DifZwOpenFileWrapper](../64/DifZwOpenFileWrapper_function_00643880.md) at `0x00643993`
- [BiLogFileOwnerProcess](../69/BiLogFileOwnerProcess_function_0069E404.md) at `0x0069E4BD`
- [HalpAcquirePccInterface](../../page/70/HalpAcquirePccInterface_function_0070D524.md) at `0x0070D5A0`
- [IopIsNotNativeDriverImage](../../page/71/IopIsNotNativeDriverImage_function_0071B914.md) at `0x0071B99B`
- [IopValidateJunctionTarget](../../page/71/IopValidateJunctionTarget_function_0071C808.md) at `0x0071C9EC`
- [IoAttachDevice](../../page/71/IoAttachDevice_function_0071CE80.md) at `0x0071CEF3`
- [PiOpenDirectoryWithRoot](../../page/72/PiOpenDirectoryWithRoot_function_00729198.md) at `0x00729262`
- [PpLastGoodDeleteFilesCallback](../../page/72/PpLastGoodDeleteFilesCallback_function_0072BD10.md) at `0x0072BD90`
- [IopFileUtilClearAttributes](../../page/73/IopFileUtilClearAttributes_function_0073FA1C.md) at `0x0073FA9E`
- [IopFileUtilWalkDirectoryTreeHelper](../../page/73/IopFileUtilWalkDirectoryTreeHelper_function_0073FD40.md) at `0x0073FDCF`
- [PiDrvDbQuerySystemPathWin32](../../page/74/PiDrvDbQuerySystemPathWin32_function_007421F4.md) at `0x007422C2`
- [PopLoadFileInMemory](../../page/75/PopLoadFileInMemory_function_007540E4.md) at `0x0075416A`
- [PspLocateSystemDll](../../page/77/PspLocateSystemDll_function_0077F0D0.md) at `0x0077F190`
- [PsCheckProcessFileSigningLevel](../../page/78/PsCheckProcessFileSigningLevel_function_00783800.md) at `0x00783913`
- [EtwpUpdateFileInfoDriverRegistration](../../page/7B/EtwpUpdateFileInfoDriverRegistration_function_007B8B1C.md) at `0x007B8BB8`
- [ExpTranslateNtPath](../../page/7C/ExpTranslateNtPath_function_007CCEF4.md) at `0x007CD05D`
- [CMFFlushHitsFile](../../page/7D/CMFFlushHitsFile_function_007D3140.md) at `0x007D32B3`
- [CMFSystemThreadRoutine](../../page/7D/CMFSystemThreadRoutine_function_007D3A70.md) at `0x007D3C24`
- [ApiSetpLoadSchemaImage](../../page/7D/ApiSetpLoadSchemaImage_function_007D9C54.md) at `0x007D9CE7`
- [AslDoesDirectoryExistNtPath](../../page/81/AslDoesDirectoryExistNtPath_function_00819B38.md) at `0x00819BB1`
- [AslDoesFileExistNtPath](../../page/81/AslDoesFileExistNtPath_function_00819BF4.md) at `0x00819C71`
- [AslpPathWildcardAllocMatchNode](../../page/81/AslpPathWildcardAllocMatchNode_function_0081C620.md) at `0x0081C7EE`
- [BiCreatePartitionDevice](../../page/82/BiCreatePartitionDevice_function_00824D10.md) at `0x00824FB9`
- [BiCreateVhdRamdiskBootDevice](../../page/82/BiCreateVhdRamdiskBootDevice_function_0082518C.md) at `0x00825237`
- [BiGetNtPartitionPath](../../page/82/BiGetNtPartitionPath_function_0082546C.md) at `0x008257AE`
- [BiIsBootRamdisk](../../page/82/BiIsBootRamdisk_function_00825AF4.md) at `0x00825B90`
- [CmpOpenHiveFile](../../page/87/CmpOpenHiveFile_function_0087A71C.md) at `0x0087AD97`
- [CmpLogHiveFileInaccessible](../../page/87/CmpLogHiveFileInaccessible_function_0087AEAC.md) at `0x0087B2FB`
- [IoGetDeviceObjectPointer](../../page/95/IoGetDeviceObjectPointer_function_00953220.md) at `0x009532AB`
- [KsepSdbMapToMemory](../../page/95/KsepSdbMapToMemory_function_0095B81C.md) at `0x0095B8AB`
- [ExpGetGlobalLocaleSection](../../page/98/ExpGetGlobalLocaleSection_function_00980DD4.md) at `0x00980E84`
- [PiInitializeDDB](../../page/99/PiInitializeDDB_function_0099ADE4.md) at `0x0099AE7F`
- [DbgkSendSystemDllMessages](../../page/A1/DbgkSendSystemDllMessages_function_00A10C04.md) at `0x00A10E1F`
- [NtGetNlsSectionPtr](../../page/A1/NtGetNlsSectionPtr_function_00A195B0.md) at `0x00A199CD`
- [MiCreateSectionForDriver](../../page/A2/MiCreateSectionForDriver_function_00A2477C.md) at `0x00A2497E`
- [SiOpenDevice](../../page/A6/SiOpenDevice_function_00A68B48.md) at `0x00A68BC3`
- [PiGetDriverImageDirectory](../../page/A6/PiGetDriverImageDirectory_function_00A6F2C4.md) at `0x00A6F3B3`
- [KsepShimDatabaseTime](../../page/A7/KsepShimDatabaseTime_function_00A79684.md) at `0x00A79725`
- [ExpGetPartitionTableInfo](../../page/A7/ExpGetPartitionTableInfo_function_00A7B7D4.md) at `0x00A7B85B`
- [PopValidateHiberFileSize](../../page/A9/PopValidateHiberFileSize_function_00A90678.md) at `0x00A90768`
- [DbgkpSectionToFileHandle](../../page/A9/DbgkpSectionToFileHandle_function_00A9AE08.md) at `0x00A9AE85`
- [BiGetPartitionVhdFilePathFromUnicodeString](../../page/A9/BiGetPartitionVhdFilePathFromUnicodeString_function_00A9E624.md) at `0x00A9E694`
- [BiGetDriveLayoutInformation](../../page/AA/BiGetDriveLayoutInformation_function_00AA1174.md) at `0x00AA11F6`
- [PopBootStatRestoreDefaults](../../page/AC/PopBootStatRestoreDefaults_function_00AC38E8.md) at `0x00AC3A0C`
- [BiIsVolumePartitionInformationRetained](../../page/AC/BiIsVolumePartitionInformationRetained_function_00AC6CFC.md) at `0x00AC6D78`
- [ExpGetDriveGeometry](../../page/AC/ExpGetDriveGeometry_function_00ACA760.md) at `0x00ACA824`
- [BiGetPhysicalDriveName](../../page/AC/BiGetPhysicalDriveName_function_00ACD5BC.md) at `0x00ACD645`
- [sub_00B3B9F4](../../page/B3/Unknown_function_00B3B9F4.md) at `0x00B3BB16`
- [sub_00B3BB7A](../../page/B3/Unknown_function_00B3BB7A.md) at `0x00B3BCA1`
- [sub_00B47492](../../page/B4/Unknown_function_00B47492.md) at `0x00B474F2`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2BE04`
- [IopMarkBootPartition](../../init/C2/IopMarkBootPartition_function_00C2CFA0.md) at `0x00C2D095`
- [IopApplySystemPartitionProt](../../init/C2/IopApplySystemPartitionProt_function_00C2E398.md) at `0x00C2E57D`
- [PipCriticalDeviceWaitCallback](../../init/C3/PipCriticalDeviceWaitCallback_function_00C30890.md) at `0x00C3097E`
- [IopFileUtilRename](../../init/C3/IopFileUtilRename_function_00C3662C.md) at `0x00C366D7`
- [PopPdcCsCheckSystemVolumeDevice](../../init/C4/PopPdcCsCheckSystemVolumeDevice_function_00C42D9C.md) at `0x00C42E54`
- [VhdiGetVolumeNumber](../../init/C6/VhdiGetVolumeNumber_function_00C6E014.md) at `0x00C6E0F9`
- [VhdiInitializeBootDisk](../../init/C6/VhdiInitializeBootDisk_function_00C6E190.md) at `0x00C6E2F4`
- [CimfsInitializeBootDisk](../../init/C6/CimfsInitializeBootDisk_function_00C6E9D0.md) at `0x00C6EB29`
- [CimfsInitializeBootDisk](../../init/C6/CimfsInitializeBootDisk_function_00C6E9D0.md) at `0x00C6ED6E`
- [RamdiskStart](../../init/C6/RamdiskStart_function_00C6EF68.md) at `0x00C6F199`

### Static image references
- `0x006AD73C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD749` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD730  48 8B C4                        mov rax, rsp
006AD733  FA                              cli
006AD734  48 83 EC 10                     sub rsp, 0x10
006AD738  50                              push rax
006AD739  9C                              pushfq
006AD73A  6A 10                           push 0x10
006AD73C  48 8D 05 1D 5D 00 00            lea rax, [rip + 0x5d1d]
006AD743  50                              push rax
006AD744  B8 33 00 00 00                  mov eax, 0x33
006AD749  E9 72 72 01 00                  jmp 0x1406c49c0
006AD74E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwOpenFile(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwOpenFile(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD730&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD730[BB_006AD730]
  bb_006AD74E[BB_006AD74E]
```
