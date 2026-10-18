# ViZwShouldCheck

- RVA: `0x00BA4DB4`–`0x00BA4DE8` (길이 `52` bytes)
- VA: `0x0000000140BA4DB4`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **51**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [VfZwAccessCheckAndAuditAlarm_Entry](VfZwAccessCheckAndAuditAlarm_Entry_function_00BA3C40.md) at `0x00BA3C49`
- [VfZwAddBootEntry_Entry](VfZwAddBootEntry_Entry_function_00BA3CC0.md) at `0x00BA3CC9`
- [VfZwAdjustPrivilegesToken_Entry](VfZwAdjustPrivilegesToken_Entry_function_00BA3D00.md) at `0x00BA3D09`
- [VfZwAllocateVirtualMemory_Entry](VfZwAllocateVirtualMemory_Entry_function_00BA3D50.md) at `0x00BA3D59`
- [VfZwAlpcAcceptConnectPort_Entry](VfZwAlpcAcceptConnectPort_Entry_function_00BA3D90.md) at `0x00BA3D99`
- [VfZwAlpcConnectPort_Entry](VfZwAlpcConnectPort_Entry_function_00BA3DF0.md) at `0x00BA3DF9`
- [VfZwAlpcCreatePort_Entry](VfZwAlpcCreatePort_Entry_function_00BA3E90.md) at `0x00BA3E99`
- [VfZwAlpcCreateResourceReserve_Entry](VfZwAlpcCreateResourceReserve_Entry_function_00BA3EE0.md) at `0x00BA3EE7`
- [VfZwAlpcQueryInformation_Entry](VfZwAlpcQueryInformation_Entry_function_00BA3F10.md) at `0x00BA3F19`
- [VfZwAlpcSendWaitReceivePort_Entry](VfZwAlpcSendWaitReceivePort_Entry_function_00BA3F50.md) at `0x00BA3F59`
- [VfZwAlpcSetInformation_Entry](VfZwAlpcSetInformation_Entry_function_00BA3FC0.md) at `0x00BA3FC7`
- [VfZwCloseObjectAuditAlarm_Entry](VfZwCloseObjectAuditAlarm_Entry_function_00BA3FF0.md) at `0x00BA3FF7`
- [VfZwConnectPort_Entry](VfZwConnectPort_Entry_function_00BA4020.md) at `0x00BA4029`
- [VfZwCreateDirectoryObject_Entry](VfZwCreateDirectoryObject_Entry_function_00BA40A0.md) at `0x00BA40A9`
- [VfZwCreateEnlistment_Entry](VfZwCreateEnlistment_Entry_function_00BA40E0.md) at `0x00BA40E9`
- [VfZwCreateEvent_Entry](VfZwCreateEvent_Entry_function_00BA4120.md) at `0x00BA4129`
- [VfZwCreateFile_Entry](VfZwCreateFile_Entry_function_00BA4160.md) at `0x00BA4169`
- [VfZwCreateKey_Entry](VfZwCreateKey_Entry_function_00BA41C0.md) at `0x00BA41C9`
- [VfZwCreateSection_Entry](VfZwCreateSection_Entry_function_00BA4210.md) at `0x00BA4219`
- [VfZwCreateSymbolicLinkObject_Entry](VfZwCreateSymbolicLinkObject_Entry_function_00BA4260.md) at `0x00BA4269`
- [VfZwCreateTransactionManager_Entry](VfZwCreateTransactionManager_Entry_function_00BA42B0.md) at `0x00BA42B9`
- [VfZwCreateTransaction_Entry](VfZwCreateTransaction_Entry_function_00BA4300.md) at `0x00BA4309`
- [VfZwDeleteBootEntry_Entry](VfZwDeleteBootEntry_Entry_function_00BA4360.md) at `0x00BA4367`
- [VfZwDeleteFile_Entry](VfZwDeleteFile_Entry_function_00BA4390.md) at `0x00BA4397`
- [VfZwDeleteValueKey_Entry](VfZwDeleteValueKey_Entry_function_00BA43C0.md) at `0x00BA43C7`
- [VfZwDeviceIoControlFile_Entry](VfZwDeviceIoControlFile_Entry_function_00BA43F0.md) at `0x00BA43F9`
- [VfZwDuplicateObject_Entry](VfZwDuplicateObject_Entry_function_00BA4460.md) at `0x00BA4467`
- [VfZwDuplicateToken_Entry](VfZwDuplicateToken_Entry_function_00BA4490.md) at `0x00BA4499`
- [VfZwFlushVirtualMemory_Entry](VfZwFlushVirtualMemory_Entry_function_00BA44D0.md) at `0x00BA44D9`
- [VfZwFreeVirtualMemory_Entry](VfZwFreeVirtualMemory_Entry_function_00BA4520.md) at `0x00BA4529`
- [VfZwLoadKey_Entry](VfZwLoadKey_Entry_function_00BA4560.md) at `0x00BA4569`
- [VfZwMapViewOfSection_Entry](VfZwMapViewOfSection_Entry_function_00BA45A0.md) at `0x00BA45A9`
- [VfZwNotifyChangeKey_Entry](VfZwNotifyChangeKey_Entry_function_00BA45F0.md) at `0x00BA45F9`
- [VfZwOpenEnlistment_Entry](VfZwOpenEnlistment_Entry_function_00BA4670.md) at `0x00BA4679`
- [VfZwOpenFile_Entry](VfZwOpenFile_Entry_function_00BA46B0.md) at `0x00BA46B9`
- [VfZwOpenProcess_Entry](VfZwOpenProcess_Entry_function_00BA4700.md) at `0x00BA4709`
- [VfZwOpenTransactionManager_Entry](VfZwOpenTransactionManager_Entry_function_00BA4750.md) at `0x00BA4759`
- [VfZwOpenTransaction_Entry](VfZwOpenTransaction_Entry_function_00BA47A0.md) at `0x00BA47A9`
- [VfZwProtectVirtualMemory_Entry](VfZwProtectVirtualMemory_Entry_function_00BA47F0.md) at `0x00BA47F9`
- [VfZwQueryDirectoryFileEx_Entry](VfZwQueryDirectoryFileEx_Entry_function_00BA4840.md) at `0x00BA4849`
- [VfZwQueryDirectoryFile_Entry](VfZwQueryDirectoryFile_Entry_function_00BA48B0.md) at `0x00BA48B9`
- [VfZwQueryEaFile_Entry](VfZwQueryEaFile_Entry_function_00BA4920.md) at `0x00BA4929`
- [VfZwQueryFullAttributesFile_Entry](VfZwQueryFullAttributesFile_Entry_function_00BA4970.md) at `0x00BA4979`
- [VfZwQueryLicenseValue_Entry](VfZwQueryLicenseValue_Entry_function_00BA49B0.md) at `0x00BA49B9`
- [VfZwQuerySymbolicLinkObject_Entry](VfZwQuerySymbolicLinkObject_Entry_function_00BA4A00.md) at `0x00BA4A09`
- [VfZwQueryValueKey_Entry](VfZwQueryValueKey_Entry_function_00BA4A40.md) at `0x00BA4A49`
- [VfZwReadFile_Entry](VfZwReadFile_Entry_function_00BA4A90.md) at `0x00BA4A99`
- [VfZwRemoveIoCompletionEx_Entry](VfZwRemoveIoCompletionEx_Entry_function_00BA4B00.md) at `0x00BA4B09`
- [VfZwReplaceKey_Entry](VfZwReplaceKey_Entry_function_00BA4B50.md) at `0x00BA4B59`
- [VfZwSetTimer_Entry](VfZwSetTimer_Entry_function_00BA4B90.md) at `0x00BA4B99`
- [VfZwSetValueKey_Entry](VfZwSetValueKey_Entry_function_00BA4BE0.md) at `0x00BA4BE9`

### Static image references
- `0x00BA4DC6` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x00BA4DD7` → RVA `0x00FC6B70` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA4DB4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00BA4DBD  33 C9                           xor ecx, ecx
00BA4DBF  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
00BA4DC6  48 8B 05 E3 1C 42 00            mov rax, qword ptr [rip + 0x421ce3]
00BA4DCD  48 85 C0                        test rax, rax
00BA4DD0  74 12                           je 0x140ba4de4
00BA4DD2  48 3B D0                        cmp rdx, rax
00BA4DD5  74 0D                           je 0x140ba4de4
00BA4DD7  48 3B 15 92 1D 42 00            cmp rdx, qword ptr [rip + 0x421d92]
00BA4DDE  8D 41 01                        lea eax, [rcx + 1]
00BA4DE1  0F 45 C8                        cmovne ecx, eax
00BA4DE4  8B C1                           mov eax, ecx
00BA4DE6  C3                              ret
00BA4DE7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViZwShouldCheck(int a1)
{
    __int64 result;

    a1 = 0;
    if (*(unsigned __int64 *)(v_rip + 4332771) == 0) goto loc_00BA4DE4;
    result = *(unsigned __int64 *)(v_rip + 4332771);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != (*(unsigned __int64 *)(v_rip + 4332771))) {
        result = a1 + 1;
        if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != (*(unsigned __int64 *)(v_rip + 4332946))) { a1 = (unsigned int)(result); }
    }
    return (unsigned int)(a1);
}
```

## 5. (Beta) C Style

```c
int64_t ViZwShouldCheck(int32_t Arg1)
{
    int64_t result;

    Arg1 = 0;
    if (*(uint64_t *)(v_rip + 0x421CE3) == 0) goto loc_00BA4DE4;
    result = *(uint64_t *)(v_rip + 0x421CE3);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != (*(uint64_t *)(v_rip + 0x421CE3))) {
        result = Arg1 + 1;
        if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != (*(uint64_t *)(v_rip + 0x421D92))) { Arg1 = (uint32_t)(result); }
    }
    return (uint32_t)(Arg1);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA4DB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA4DB4[BB_00BA4DB4]
  bb_00BA4DD2[BB_00BA4DD2]
  bb_00BA4DD7[BB_00BA4DD7]
  bb_00BA4DE4[BB_00BA4DE4]
  bb_00BA4DE7[BB_00BA4DE7]
  bb_00BA4DB4 -->|branch| bb_00BA4DE4
  bb_00BA4DB4 -->|fallthrough| bb_00BA4DD2
  bb_00BA4DD2 -->|branch| bb_00BA4DE4
  bb_00BA4DD2 -->|fallthrough| bb_00BA4DD7
  bb_00BA4DD7 -->|flow| bb_00BA4DE4
```
