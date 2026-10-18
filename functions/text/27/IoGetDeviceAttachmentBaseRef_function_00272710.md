# IoGetDeviceAttachmentBaseRef

- RVA: `0x00272710`–`0x0027277F` (길이 `111` bytes)
- VA: `0x0000000140272710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `28`개 명령, `111/111` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00272722` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x0027272D` → [IopGetDeviceAttachmentBase](IopGetDeviceAttachmentBase_function_002726E0.md) (function, `0x002726E0`)
- `0x0027273D` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00272752` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00272767` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- [PipSetDevNodeStateFlags](../../page/72/PipSetDevNodeStateFlags_function_0072DB98.md) at `0x0072DBAE`
- [PipSendQueryRemoveIrpAndCheckOpenHandles](../../page/74/PipSendQueryRemoveIrpAndCheckOpenHandles_function_007443E8.md) at `0x0074452B`
- [PopRegisterTargetDeviceProtection](../../page/75/PopRegisterTargetDeviceProtection_function_00756A94.md) at `0x00756AD5`
- [PopRegisterCoolingExtensionProtection](../../page/75/PopRegisterCoolingExtensionProtection_function_007575D0.md) at `0x00757623`
- [FsRtlReleaseFile](../../page/98/FsRtlReleaseFile_function_00985B70.md) at `0x00985D7A`
- [FsRtlAcquireFileForCcFlushEx](../../page/9D/FsRtlAcquireFileForCcFlushEx_function_009D72F0.md) at `0x009D7406`
- [FsRtlReleaseFileForCcFlush](../../page/9D/FsRtlReleaseFileForCcFlush_function_009D75A0.md) at `0x009D769A`
- [FsRtlAcquireFileExclusiveCommon](../../page/9D/FsRtlAcquireFileExclusiveCommon_function_009D8E50.md) at `0x009D9051`
- [IoWMIDeviceObjectToInstanceName](../../page/A8/IoWMIDeviceObjectToInstanceName_function_00A873C0.md) at `0x00A873EC`

### Static image references
- `0x00272757` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00272710  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00272715  57                              push rdi
00272716  48 83 EC 20                     sub rsp, 0x20
0027271A  48 8B D9                        mov rbx, rcx
0027271D  B9 0A 00 00 00                  mov ecx, 0xa
00272722  E8 59 16 00 00                  call 0x140273d80
00272727  48 8B CB                        mov rcx, rbx
0027272A  0F B6 F8                        movzx edi, al
0027272D  E8 AE FF FF FF                  call 0x1402726e0
00272732  BA 44 66 6C 74                  mov edx, 0x746c6644
00272737  48 8B C8                        mov rcx, rax
0027273A  48 8B D8                        mov rbx, rax
0027273D  E8 CE DF F9 FF                  call 0x140210710
00272742  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
0027274B  48 81 C1 A0 00 00 00            add rcx, 0xa0
00272752  E8 59 4A FA FF                  call 0x1402171b0
00272757  83 3D C2 45 D5 00 00            cmp dword ptr [rip + 0xd545c2], 0
0027275E  74 0C                           je 0x14027276c
00272760  44 0F 20 C1                     mov rcx, cr8
00272764  40 8A D7                        mov dl, dil
00272767  E8 2C 2F 28 00                  call 0x1404f5698
0027276C  44 0F 22 C7                     mov cr8, rdi
00272770  48 8B C3                        mov rax, rbx
00272773  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00272778  48 83 C4 20                     add rsp, 0x20
0027277C  5F                              pop rdi
0027277D  C3                              ret
0027277E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetDeviceAttachmentBaseRef(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireQueuedSpinLock(10, a2, a3, a4);
    result = IopGetDeviceAttachmentBase(a1, a2, a3, a4);
    result = ObfReferenceObjectWithTag(result, (unsigned int)(0x746C6644ULL), a3, a4);
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (160);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, (unsigned int)(0x746C6644ULL), a3, a4);
    if ((*(unsigned int *)(v_rip + 13977026)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoGetDeviceAttachmentBaseRef(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireQueuedSpinLock(10, a2, a3, a4);
    result = IopGetDeviceAttachmentBase(Arg1, a2, a3, a4);
    result = ObfReferenceObjectWithTag(result, (uint32_t)(0x746C6644ULL), a3, a4);
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (160);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, (uint32_t)(0x746C6644ULL), a3, a4);
    if ((*(uint32_t *)(v_rip + 0xD545C2)) != 0) {
        Arg1 = v_cr8;
        a2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00272710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00272710[BB_00272710]
  bb_00272760[BB_00272760]
  bb_0027276C[BB_0027276C]
  bb_0027277E[BB_0027277E]
  bb_00272710 -->|branch| bb_0027276C
  bb_00272710 -->|fallthrough| bb_00272760
  bb_00272760 -->|flow| bb_0027276C
```
