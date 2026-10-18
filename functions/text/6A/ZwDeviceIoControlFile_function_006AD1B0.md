# ZwDeviceIoControlFile

- RVA: `0x006AD1B0`–`0x006AD1CF` (길이 `31` bytes)
- VA: `0x00000001406AD1B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFEE4`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **28**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopFlushAndHold](../4D/PopFlushAndHold_function_004DF60C.md) at `0x004DF663`
- [DifZwDeviceIoControlFileWrapper](../64/DifZwDeviceIoControlFileWrapper_function_00641040.md) at `0x0064118F`
- [PnpHardwareConfigCreateBootDriverFlags](../../page/72/PnpHardwareConfigCreateBootDriverFlags_function_00723B88.md) at `0x00723CE0`
- [PnpHardwareConfigCreateBootDriverFlags](../../page/72/PnpHardwareConfigCreateBootDriverFlags_function_00723B88.md) at `0x00723D7C`
- [EtwpUpdateFileInfoDriverRegistration](../../page/7B/EtwpUpdateFileInfoDriverRegistration_function_007B8B1C.md) at `0x007B8C06`
- [ExpGetSystemWriteConstraintInformation](../../page/7C/ExpGetSystemWriteConstraintInformation_function_007C4100.md) at `0x007C425B`
- [ExpTranslateNtPath](../../page/7C/ExpTranslateNtPath_function_007CCEF4.md) at `0x007CD0A3`
- [ExpTranslateNtPath](../../page/7C/ExpTranslateNtPath_function_007CCEF4.md) at `0x007CD11C`
- [BiCreateVhdRamdiskBootDevice](../../page/82/BiCreateVhdRamdiskBootDevice_function_0082518C.md) at `0x0082527A`
- [BiGetVolumeDiskExtentsInformation](../../page/82/BiGetVolumeDiskExtentsInformation_function_008259FC.md) at `0x00825A7E`
- [BiIsBootRamdisk](../../page/82/BiIsBootRamdisk_function_00825AF4.md) at `0x00825BCC`
- [SiGetDeviceNumberInformation](../../page/82/SiGetDeviceNumberInformation_function_00827858.md) at `0x008278DA`
- [SiGetDriveLayoutInformation](../../page/82/SiGetDriveLayoutInformation_function_00827934.md) at `0x008279C5`
- [SiIssueSynchronousIoctl](../../page/82/SiIssueSynchronousIoctl_function_00827A34.md) at `0x00827AA7`
- [SiQueryProperty](../../page/A6/SiQueryProperty_function_00A6896C.md) at `0x00A68A32`
- [SiGetDiskPartitionInformation](../../page/A6/SiGetDiskPartitionInformation_function_00A68AB4.md) at `0x00A68B18`
- [PfSnVolumeCheckIsSdBus](../../page/A6/PfSnVolumeCheckIsSdBus_function_00A6AF38.md) at `0x00A6AFD2`
- [PfSnVolumeCheckSeekPenalty](../../page/A6/PfSnVolumeCheckSeekPenalty_function_00A6ECB4.md) at `0x00A6ED4E`
- [ExpGetPartitionTableInfo](../../page/A7/ExpGetPartitionTableInfo_function_00A7B7D4.md) at `0x00A7B8B4`
- [BiGetPartitionVhdFilePathFromUnicodeString](../../page/A9/BiGetPartitionVhdFilePathFromUnicodeString_function_00A9E624.md) at `0x00A9E6FD`
- [BiIssueGetDriveLayoutIoctl](../../page/AA/BiIssueGetDriveLayoutIoctl_function_00AA1240.md) at `0x00AA12C7`
- [BiIssueGetDriveLayoutIoctl](../../page/AA/BiIssueGetDriveLayoutIoctl_function_00AA1240.md) at `0x00AA1349`
- [BiIsVolumePartitionInformationRetained](../../page/AC/BiIsVolumePartitionInformationRetained_function_00AC6CFC.md) at `0x00AC6DBD`
- [ExpGetDriveGeometry](../../page/AC/ExpGetDriveGeometry_function_00ACA760.md) at `0x00ACA864`
- [BiGetPartitionInformation](../../page/AC/BiGetPartitionInformation_function_00ACE1C8.md) at `0x00ACE257`
- [BiGetPartitionInformation](../../page/AC/BiGetPartitionInformation_function_00ACE1C8.md) at `0x00ACE2A6`
- [PopPdcCsCheckSystemVolumeDevice](../../init/C4/PopPdcCsCheckSystemVolumeDevice_function_00C42D9C.md) at `0x00C42EA9`
- [VhdiGetVolumeNumber](../../init/C6/VhdiGetVolumeNumber_function_00C6E014.md) at `0x00C6E13E`
- [VhdiInitializeBootDisk](../../init/C6/VhdiInitializeBootDisk_function_00C6E190.md) at `0x00C6E386`
- [VhdiQueryVolumeVhdFilePath](../../init/C6/VhdiQueryVolumeVhdFilePath_function_00C6E4B4.md) at `0x00C6E52A`
- [CimfsInitializeBootDisk](../../init/C6/CimfsInitializeBootDisk_function_00C6E9D0.md) at `0x00C6EB9C`
- [RamdiskStart](../../init/C6/RamdiskStart_function_00C6EF68.md) at `0x00C6F1EC`

### Static image references
- `0x006AD1BC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD1C9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD1B0  48 8B C4                        mov rax, rsp
006AD1B3  FA                              cli
006AD1B4  48 83 EC 10                     sub rsp, 0x10
006AD1B8  50                              push rax
006AD1B9  9C                              pushfq
006AD1BA  6A 10                           push 0x10
006AD1BC  48 8D 05 9D 62 00 00            lea rax, [rip + 0x629d]
006AD1C3  50                              push rax
006AD1C4  B8 07 00 00 00                  mov eax, 7
006AD1C9  E9 F2 77 01 00                  jmp 0x1406c49c0
006AD1CE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwDeviceIoControlFile(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwDeviceIoControlFile(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD1B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD1B0[BB_006AD1B0]
  bb_006AD1CE[BB_006AD1CE]
```
