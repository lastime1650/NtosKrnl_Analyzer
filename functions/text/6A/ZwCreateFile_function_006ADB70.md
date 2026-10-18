# ZwCreateFile

- RVA: `0x006ADB70`–`0x006ADB8F` (길이 `31` bytes)
- VA: `0x00000001406ADB70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C028C`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **27**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlFileMapInitializeByNtPath](../4D/RtlFileMapInitializeByNtPath_function_004D3F5C.md) at `0x004D3FE2`
- [LdrpMapResourceFile](../5E/LdrpMapResourceFile_function_005E5CBC.md) at `0x005E5DB9`
- [DifZwCreateFileWrapper](../63/DifZwCreateFileWrapper_function_0063F940.md) at `0x0063FA9E`
- [CmpDeleteCorruptedFile](../66/CmpDeleteCorruptedFile_function_0066DF74.md) at `0x0066DFE6`
- [FsRtlpOpenDev](../../page/71/FsRtlpOpenDev_function_0071430C.md) at `0x007143A8`
- [IopBootLogToFile](../../page/71/IopBootLogToFile_function_0071AD54.md) at `0x0071AE4C`
- [PiCreateDirectoryPath](../../page/72/PiCreateDirectoryPath_function_0072885C.md) at `0x00728946`
- [PiCreateDirectoryPath](../../page/72/PiCreateDirectoryPath_function_0072885C.md) at `0x00728A38`
- [PiCreateDirectoryPath](../../page/72/PiCreateDirectoryPath_function_0072885C.md) at `0x00728AF8`
- [PopGetPolicyDeviceObject](../../page/76/PopGetPolicyDeviceObject_function_00765EB8.md) at `0x00765F3D`
- [SmKmStoreFileOpenVolume](../../page/7A/SmKmStoreFileOpenVolume_function_007A9C14.md) at `0x007A9D11`
- [SmpUtilsGetControlDevice](../../page/7A/SmpUtilsGetControlDevice_function_007ACBE0.md) at `0x007ACC8A`
- [ExpGetSystemWriteConstraintInformation](../../page/7C/ExpGetSystemWriteConstraintInformation_function_007C4100.md) at `0x007C419B`
- [CmpVolumeContextStart](../../page/7E/CmpVolumeContextStart_function_007E88A4.md) at `0x007E89B0`
- [CmpVolumeManagerGetContextForFilePath](../../page/7E/CmpVolumeManagerGetContextForFilePath_function_007E8A6C.md) at `0x007E8AF1`
- [CmpInitBackupHive](../../page/7E/CmpInitBackupHive_function_007EC594.md) at `0x007EC695`
- [CmpIsFileInSystemConfig](../../page/7F/CmpIsFileInSystemConfig_function_007F1F80.md) at `0x007F2038`
- [SdbpGetFileTimestamp](../../page/81/SdbpGetFileTimestamp_function_00812558.md) at `0x0081266F`
- [VhdiMountVhdFile](../../page/83/VhdiMountVhdFile_function_0083BED0.md) at `0x0083C28E`
- [CmpOpenHiveFile](../../page/87/CmpOpenHiveFile_function_0087A71C.md) at `0x0087A91D`
- [EtwpDelayCreate](../../page/9C/EtwpDelayCreate_function_009C1188.md) at `0x009C12F6`
- [EtwpCreateDirectoryFile](../../page/A7/EtwpCreateDirectoryFile_function_00A705E0.md) at `0x00A706AB`
- [sub_00B1833E](../../page/B1/Unknown_function_00B1833E.md) at `0x00B183B9`
- [sub_00B31590](../../page/B3/Unknown_function_00B31590.md) at `0x00B315F6`
- [PopFlushVolumeWorker](../../pagelk/B7/PopFlushVolumeWorker_function_00B7AEB0.md) at `0x00B7B03E`
- [KdpCreateFileCallback](../../pagekd/B8/KdpCreateFileCallback_function_00B86830.md) at `0x00B868C5`
- [PiCreateDriverDataDirectoryRoot](../../init/C3/PiCreateDriverDataDirectoryRoot_function_00C329A8.md) at `0x00C32A99`
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C500FF`
- [EmInitSystem](../../init/C7/EmInitSystem_function_00C71150.md) at `0x00C71560`

### Static image references
- `0x006ADB7C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006ADB89` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006ADB70  48 8B C4                        mov rax, rsp
006ADB73  FA                              cli
006ADB74  48 83 EC 10                     sub rsp, 0x10
006ADB78  50                              push rax
006ADB79  9C                              pushfq
006ADB7A  6A 10                           push 0x10
006ADB7C  48 8D 05 DD 58 00 00            lea rax, [rip + 0x58dd]
006ADB83  50                              push rax
006ADB84  B8 55 00 00 00                  mov eax, 0x55
006ADB89  E9 32 6E 01 00                  jmp 0x1406c49c0
006ADB8E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwCreateFile(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwCreateFile(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ADB70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ADB70[BB_006ADB70]
  bb_006ADB8E[BB_006ADB8E]
```
