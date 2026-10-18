# ZwSetInformationFile

- RVA: `0x006AD5B0`–`0x006AD5CF` (길이 `31` bytes)
- VA: `0x00000001406AD5B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0064`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **24**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SepAppIdentityFromImageHash](../60/SepAppIdentityFromImageHash_function_00607AA4.md) at `0x00607BBF`
- [SepAppIdentityFromImageHash](../60/SepAppIdentityFromImageHash_function_00607AA4.md) at `0x00607D10`
- [DifZwSetInformationFileWrapper](../64/DifZwSetInformationFileWrapper_function_0064A2F0.md) at `0x0064A3F0`
- [CmpDeleteCorruptedFile](../66/CmpDeleteCorruptedFile_function_0066DF74.md) at `0x0066E00B`
- [PpLastGoodDeleteFilesCallback](../../page/72/PpLastGoodDeleteFilesCallback_function_0072BD10.md) at `0x0072BDB7`
- [IopFileUtilClearAttributes](../../page/73/IopFileUtilClearAttributes_function_0073FA1C.md) at `0x0073FB0A`
- [PopCreateHiberFile](../../page/75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D0D1`
- [PopCreateHiberFile](../../page/75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D140`
- [PopCreateHiberFile](../../page/75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D19A`
- [SmKmStoreFileCreate](../../page/7A/SmKmStoreFileCreate_function_007A8F14.md) at `0x007A90A8`
- [SmKmStoreFileCreate](../../page/7A/SmKmStoreFileCreate_function_007A8F14.md) at `0x007A9112`
- [SmKmStoreFileDelete](../../page/7A/SmKmStoreFileDelete_function_007A9680.md) at `0x007A96C4`
- [EtwpSavePersistedLogger](../../page/7B/EtwpSavePersistedLogger_function_007BF374.md) at `0x007BF591`
- [CmpCmdRenameHive](../../page/7E/CmpCmdRenameHive_function_007E5910.md) at `0x007E59B3`
- [CmpFlushBackupHive](../../page/7E/CmpFlushBackupHive_function_007EC1A8.md) at `0x007EC468`
- [CmpWriteOffsetArrayToFile](../../page/7E/CmpWriteOffsetArrayToFile_function_007EC82C.md) at `0x007EC86A`
- [MiCreatePagingFile](../../page/7F/MiCreatePagingFile_function_007FEFF4.md) at `0x007FF588`
- [CmpOpenHiveFile](../../page/87/CmpOpenHiveFile_function_0087A71C.md) at `0x0087A9FE`
- [CmpDoFileSetSizeEx](../../page/9B/CmpDoFileSetSizeEx_function_009B2A4C.md) at `0x009B2B1D`
- [CmpCmdHiveClose](../../page/9B/CmpCmdHiveClose_function_009B3948.md) at `0x009B3A15`
- [EtwpRealtimeSaveState](../../page/9B/EtwpRealtimeSaveState_function_009BCBD4.md) at `0x009BCD23`
- [EtwpRealtimeZeroTruncateLogfile](../../page/9B/EtwpRealtimeZeroTruncateLogfile_function_009BDE0C.md) at `0x009BDE4A`
- [EtwpRealtimeZeroTruncateLogfile](../../page/9B/EtwpRealtimeZeroTruncateLogfile_function_009BDE0C.md) at `0x009BDE75`
- [EtwpCreateLogFile](../../page/9C/EtwpCreateLogFile_function_009C035C.md) at `0x009C0521`
- [EtwpUpdateFileHeader](../../page/9C/EtwpUpdateFileHeader_function_009C082C.md) at `0x009C095E`
- [PopResizeHiberFile](../../page/A9/PopResizeHiberFile_function_00A90410.md) at `0x00A9049F`
- [PopResizeHiberFile](../../page/A9/PopResizeHiberFile_function_00A90410.md) at `0x00A904D7`
- [sub_00B1833E](../../page/B1/Unknown_function_00B1833E.md) at `0x00B18359`
- [sub_00B2ED96](../../page/B2/Unknown_function_00B2ED96.md) at `0x00B2EDCD`
- [IopFileUtilRename](../../init/C3/IopFileUtilRename_function_00C3662C.md) at `0x00C36728`

### Static image references
- `0x006AD5BC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD5C9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD5B0  48 8B C4                        mov rax, rsp
006AD5B3  FA                              cli
006AD5B4  48 83 EC 10                     sub rsp, 0x10
006AD5B8  50                              push rax
006AD5B9  9C                              pushfq
006AD5BA  6A 10                           push 0x10
006AD5BC  48 8D 05 9D 5E 00 00            lea rax, [rip + 0x5e9d]
006AD5C3  50                              push rax
006AD5C4  B8 27 00 00 00                  mov eax, 0x27
006AD5C9  E9 F2 73 01 00                  jmp 0x1406c49c0
006AD5CE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwSetInformationFile(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwSetInformationFile(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD5B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD5B0[BB_006AD5B0]
  bb_006AD5CE[BB_006AD5CE]
```
