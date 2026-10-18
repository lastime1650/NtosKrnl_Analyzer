# PsReturnProcessPagedPoolQuota

- RVA: `0x002A6860`–`0x002A687A` (길이 `26` bytes)
- VA: `0x00000001402A6860`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068AB8`
- 디코드: `7`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **19**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiPerformVadSplitting](MiPerformVadSplitting_function_002A5A80.md) at `0x002A5D5D`
- [FsRtlCancelNotify](../4E/FsRtlCancelNotify_function_004E7F90.md) at `0x004E8239`
- [FsRtlCancelNotify](../4E/FsRtlCancelNotify_function_004E7F90.md) at `0x004E82E3`
- [ExpFreeTablePagedPool](../../page/86/ExpFreeTablePagedPool_function_0086B410.md) at `0x0086B43B`
- [MiReturnVadCharges](../../page/88/MiReturnVadCharges_function_008875B8.md) at `0x008875F2`
- [AlpcSecurityDestroyProcedure](../../page/88/AlpcSecurityDestroyProcedure_function_0088B330.md) at `0x0088B4D0`
- [sub_0088B6F6](../../page/88/Unknown_function_0088B6F6.md) at `0x0088B6F6`
- [AlpcpSendMessage](../../page/88/AlpcpSendMessage_function_0088BD40.md) at `0x0088CADA`
- [AlpcpCaptureMessageDataSafe](../../page/88/AlpcpCaptureMessageDataSafe_function_0088F3B0.md) at `0x0088F572`
- [sub_00892B22](../../page/89/Unknown_function_00892B22.md) at `0x00892BA2`
- [ExpFreeHandleTable](../../page/90/ExpFreeHandleTable_function_00903B70.md) at `0x00903BD4`
- [LpcExitProcess](../../page/90/LpcExitProcess_function_00907920.md) at `0x0090793C`
- [sub_00922E92](../../page/92/Unknown_function_00922E92.md) at `0x00922E92`
- [AlpcpReleasePagedPoolQuota](../../page/92/AlpcpReleasePagedPoolQuota_function_00922EE8.md) at `0x00922F11`
- [ExpAllocateHandleTable](../../page/94/ExpAllocateHandleTable_function_0094C8F0.md) at `0x0094CA04`
- [MiReturnVadQuota](../../page/A1/MiReturnVadQuota_function_00A1E314.md) at `0x00A1E3B4`
- [FsRtlNotifyFilterReportChange](../../page/A1/FsRtlNotifyFilterReportChange_function_00A1E880.md) at `0x00A1EB94`
- [FsRtlNotifyFilterReportChange](../../page/A1/FsRtlNotifyFilterReportChange_function_00A1E880.md) at `0x00A1F239`
- [FsRtlNotifyFilterReportChangeLiteEx](../../page/A1/FsRtlNotifyFilterReportChangeLiteEx_function_00A1F2B0.md) at `0x00A1F82D`
- [FsRtlNotifyFilterReportChangeLiteEx](../../page/A1/FsRtlNotifyFilterReportChangeLiteEx_function_00A1F2B0.md) at `0x00A1F889`
- [FsRtlNotifyCompleteIrp](../../page/A1/FsRtlNotifyCompleteIrp_function_00A1FA28.md) at `0x00A1FB41`
- [FsRtlNotifyCleanupOneEntry](../../page/A3/FsRtlNotifyCleanupOneEntry_function_00A32908.md) at `0x00A32969`

### Static image references
- `0x002A6867` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002A6874` → [sub_002A692F](Unknown_function_002A692F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002A6860  40 53                           push rbx
002A6862  57                              push rdi
002A6863  48 83 EC 38                     sub rsp, 0x38
002A6867  48 3B 0D 42 02 D2 00            cmp rcx, qword ptr [rip + 0xd20242]
002A686E  48 8B FA                        mov rdi, rdx
002A6871  48 8B D9                        mov rbx, rcx
002A6874  0F 84 B5 00 00 00               je 0x1402a692f
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall PsReturnProcessPagedPoolQuota(__int64 a1, __int64 a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
}
```

## 5. (Beta) C Style

```c
void PsReturnProcessPagedPoolQuota(int64_t Arg1, int64_t Arg2)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A6860&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A6860[BB_002A6860]
```
