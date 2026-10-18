# ZwWriteFile

- RVA: `0x006AD1D0`–`0x006AD1EF` (길이 `31` bytes)
- VA: `0x00000001406AD1D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFEF0`
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
- [IopLiveDumpWriteBuffer](../3F/IopLiveDumpWriteBuffer_function_003F6688.md) at `0x003F66FE`
- [DifZwWriteFileWrapper](../64/DifZwWriteFileWrapper_function_0064BF00.md) at `0x0064C043`
- [DbgkpWerWriteSecondaryData](../../page/71/DbgkpWerWriteSecondaryData_function_007126FC.md) at `0x00712789`
- [DbgkpWerWriteSecondaryData](../../page/71/DbgkpWerWriteSecondaryData_function_007126FC.md) at `0x007127E1`
- [DbgkpWerWriteSecondaryData](../../page/71/DbgkpWerWriteSecondaryData_function_007126FC.md) at `0x0071281A`
- [DbgkpWerWriteTriageDump](../../page/71/DbgkpWerWriteTriageDump_function_00712860.md) at `0x007128E5`
- [IopBootLogToFile](../../page/71/IopBootLogToFile_function_0071AD54.md) at `0x0071AE92`
- [IopBootLogToFile](../../page/71/IopBootLogToFile_function_0071AD54.md) at `0x0071AEDB`
- [RtlRestoreBootStatusDefaults](../../page/79/RtlRestoreBootStatusDefaults_function_00790758.md) at `0x00790822`
- [SmKmStoreFileWriteHeader](../../page/7A/SmKmStoreFileWriteHeader_function_007A9DB4.md) at `0x007A9F50`
- [EtwpSavePersistedLogger](../../page/7B/EtwpSavePersistedLogger_function_007BF374.md) at `0x007BF7FF`
- [EtwpWriteBufferCompressed](../../page/7B/EtwpWriteBufferCompressed_function_007BFB64.md) at `0x007BFCA5`
- [EtwpWriteRemainingCompressedData](../../page/7B/EtwpWriteRemainingCompressedData_function_007BFD34.md) at `0x007BFDA5`
- [CMFFlushHitsFile](../../page/7D/CMFFlushHitsFile_function_007D3140.md) at `0x007D33C6`
- [LkmdTelpWriteDumpFile](../../page/84/LkmdTelpWriteDumpFile_function_008417DC.md) at `0x008418B9`
- [LkmdTelpWriteDumpFile](../../page/84/LkmdTelpWriteDumpFile_function_008417DC.md) at `0x00841901`
- [LkmdTelpWriteDumpFile](../../page/84/LkmdTelpWriteDumpFile_function_008417DC.md) at `0x0084193C`
- [LkmdTelpWriteDumpFile](../../page/84/LkmdTelpWriteDumpFile_function_008417DC.md) at `0x00841976`
- [EtwpRealtimeSaveState](../../page/9B/EtwpRealtimeSaveState_function_009BCBD4.md) at `0x009BCCDC`
- [EtwpFlushBufferToLogfile](../../page/9B/EtwpFlushBufferToLogfile_function_009BFC08.md) at `0x009BFC76`
- [EtwpRealtimeSaveBuffer](../../page/9B/EtwpRealtimeSaveBuffer_function_009BFF48.md) at `0x009BFFCD`
- [EtwpUpdateFileHeader](../../page/9C/EtwpUpdateFileHeader_function_009C082C.md) at `0x009C0902`
- [EtwpUpdateFileHeader](../../page/9C/EtwpUpdateFileHeader_function_009C082C.md) at `0x009C0AE6`
- [EtwpFinalizeHeader](../../page/9C/EtwpFinalizeHeader_function_009C1EF0.md) at `0x009C2115`
- [RtlpGetSetBootStatusData](../../page/A4/RtlpGetSetBootStatusData_function_00A4CD64.md) at `0x00A4CE88`
- [CmpDoFileWrite](../../page/A6/CmpDoFileWrite_function_00A65880.md) at `0x00A659ED`
- [CmpDoFileWrite](../../page/A6/CmpDoFileWrite_function_00A65880.md) at `0x00A65A31`
- [SshpSessionManagerFlushControlEventBufferWorker](../../page/A7/SshpSessionManagerFlushControlEventBufferWorker_function_00A76CC0.md) at `0x00A77033`
- [SshpSessionManagerWriteBytes](../../page/A7/SshpSessionManagerWriteBytes_function_00A770AC.md) at `0x00A770EA`
- [EtwpRealtimeRestoreState](../../page/AC/EtwpRealtimeRestoreState_function_00AC6A74.md) at `0x00AC6C22`
- [KdpWriteFileCallback](../../pagekd/B8/KdpWriteFileCallback_function_00B86EC0.md) at `0x00B86F04`
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C5013B`

### Static image references
- `0x006AD1DC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD1E9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD1D0  48 8B C4                        mov rax, rsp
006AD1D3  FA                              cli
006AD1D4  48 83 EC 10                     sub rsp, 0x10
006AD1D8  50                              push rax
006AD1D9  9C                              pushfq
006AD1DA  6A 10                           push 0x10
006AD1DC  48 8D 05 7D 62 00 00            lea rax, [rip + 0x627d]
006AD1E3  50                              push rax
006AD1E4  B8 08 00 00 00                  mov eax, 8
006AD1E9  E9 D2 77 01 00                  jmp 0x1406c49c0
006AD1EE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwWriteFile(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwWriteFile(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD1D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD1D0[BB_006AD1D0]
  bb_006AD1EE[BB_006AD1EE]
```
