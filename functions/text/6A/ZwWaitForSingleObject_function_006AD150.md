# ZwWaitForSingleObject

- RVA: `0x006AD150`–`0x006AD16F` (길이 `31` bytes)
- VA: `0x00000001406AD150`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFEC0`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **17**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CcDeletePrivateVolumeCacheMap](../3C/CcDeletePrivateVolumeCacheMap_function_003CE950.md) at `0x003CEBE3`
- [CcDeletePartition](../57/CcDeletePartition_function_0057DE9C.md) at `0x0057DEF6`
- [PiDrvDbUnloadNodeWaitWorkerCallback](../5A/PiDrvDbUnloadNodeWaitWorkerCallback_function_005AA910.md) at `0x005AA92E`
- [DifZwWaitForSingleObjectWrapper](../64/DifZwWaitForSingleObjectWrapper_function_0064BD80.md) at `0x0064BE63`
- [MiZeroPageThread](../69/MiZeroPageThread_function_00696D80.md) at `0x00696F15`
- [FsRtlpRegisterProviderWithMUP](../../page/71/FsRtlpRegisterProviderWithMUP_function_007143D4.md) at `0x0071449A`
- [PnpHardwareConfigCreateBootDriverFlags](../../page/72/PnpHardwareConfigCreateBootDriverFlags_function_00723B88.md) at `0x00723CF7`
- [PnpHardwareConfigCreateBootDriverFlags](../../page/72/PnpHardwareConfigCreateBootDriverFlags_function_00723B88.md) at `0x00723D93`
- [IopFileUtilWalkDirectoryTreeHelper](../../page/73/IopFileUtilWalkDirectoryTreeHelper_function_0073FD40.md) at `0x0073FE42`
- [PspShutdownCsrProcess](../../page/78/PspShutdownCsrProcess_function_00780214.md) at `0x007803BF`
- [ExpPartitionDestroy](../../page/7C/ExpPartitionDestroy_function_007CF9B8.md) at `0x007CFA36`
- [CMFFlushHitsFile](../../page/7D/CMFFlushHitsFile_function_007D3140.md) at `0x007D33DE`
- [CMFSystemThreadRoutine](../../page/7D/CMFSystemThreadRoutine_function_007D3A70.md) at `0x007D3CCE`
- [CMFSystemThreadRoutine](../../page/7D/CMFSystemThreadRoutine_function_007D3A70.md) at `0x007D3F43`
- [MiDeletePartitionResources](../../page/80/MiDeletePartitionResources_function_0080D074.md) at `0x0080D0DB`
- [BiAcquireBcdSyncMutant](../../page/91/BiAcquireBcdSyncMutant_function_00916898.md) at `0x009168DF`
- [PiDrvDbLoadNode](../../page/93/PiDrvDbLoadNode_function_00931AB0.md) at `0x00931BA2`
- [PfSnVolumeCheckIsSdBus](../../page/A6/PfSnVolumeCheckIsSdBus_function_00A6AF38.md) at `0x00A6AFE6`
- [PfSnVolumeCheckSeekPenalty](../../page/A6/PfSnVolumeCheckSeekPenalty_function_00A6ECB4.md) at `0x00A6ED99`

### Static image references
- `0x006AD15C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD169` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD150  48 8B C4                        mov rax, rsp
006AD153  FA                              cli
006AD154  48 83 EC 10                     sub rsp, 0x10
006AD158  50                              push rax
006AD159  9C                              pushfq
006AD15A  6A 10                           push 0x10
006AD15C  48 8D 05 FD 62 00 00            lea rax, [rip + 0x62fd]
006AD163  50                              push rax
006AD164  B8 04 00 00 00                  mov eax, 4
006AD169  E9 52 78 01 00                  jmp 0x1406c49c0
006AD16E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwWaitForSingleObject(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwWaitForSingleObject(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD150&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD150[BB_006AD150]
  bb_006AD16E[BB_006AD16E]
```
