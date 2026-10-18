# MmMarkImageForHiberPhase

- RVA: `0x00B748EC`–`0x00B7496A` (길이 `126` bytes)
- VA: `0x0000000140B748EC`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `37`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B748FE` → [MmLockLoadedModuleListShared](../../text/2F/MmLockLoadedModuleListShared_function_002F21E4.md) (function, `0x002F21E4`)
- `0x00B74909` → [MmFindDataTableEntryByAddress](../../text/2A/MmFindDataTableEntryByAddress_function_002A3C0C.md) (function, `0x002A3C0C`)
- `0x00B74914` → [MmUnlockLoadedModuleListShared](../../text/2F/MmUnlockLoadedModuleListShared_function_002F2230.md) (function, `0x002F2230`)
- `0x00B74921` → [MmGetLoadedModuleImageAdditionalTablesAddress](../../text/3D/MmGetLoadedModuleImageAdditionalTablesAddress_function_003D4CF0.md) (function, `0x003D4CF0`)
- `0x00B74938` → [MiMarkNonPagedHiberPhasePages](MiMarkNonPagedHiberPhasePages_function_00B73FEC.md) (function, `0x00B73FEC`)
- `0x00B74951` → [MiMarkNonPagedHiberPhasePages](MiMarkNonPagedHiberPhasePages_function_00B73FEC.md) (function, `0x00B73FEC`)
- `0x00B74959` → [MiMarkHotPatchesForHiberPhase](MiMarkHotPatchesForHiberPhase_function_00B74C10.md) (function, `0x00B74C10`)

### Direct callers
- [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) at `0x0047C6FF`
- [MiMarkHiberProtectedImages](../../text/67/MiMarkHiberProtectedImages_function_00678AAC.md) at `0x00678ADE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00B748FE` → [MmLockLoadedModuleListShared](../../text/2F/MmLockLoadedModuleListShared_function_002F21E4.md) (`PAGELK` → `.text`)
  - `0x00B74909` → [MmFindDataTableEntryByAddress](../../text/2A/MmFindDataTableEntryByAddress_function_002A3C0C.md) (`PAGELK` → `.text`)
  - `0x00B74914` → [MmUnlockLoadedModuleListShared](../../text/2F/MmUnlockLoadedModuleListShared_function_002F2230.md) (`PAGELK` → `.text`)
  - `0x00B74921` → [MmGetLoadedModuleImageAdditionalTablesAddress](../../text/3D/MmGetLoadedModuleImageAdditionalTablesAddress_function_003D4CF0.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B748EC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B748F1  57                              push rdi
00B748F2  48 83 EC 20                     sub rsp, 0x20
00B748F6  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
00B748FB  48 8B D9                        mov rbx, rcx
00B748FE  E8 E1 D8 77 FF                  call 0x1402f21e4
00B74903  48 8B CB                        mov rcx, rbx
00B74906  44 8A D8                        mov r11b, al
00B74909  E8 FE F2 72 FF                  call 0x1402a3c0c
00B7490E  41 8A CB                        mov cl, r11b
00B74911  48 8B F8                        mov rdi, rax
00B74914  E8 17 D9 77 FF                  call 0x1402f2230
00B74919  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00B7491E  48 8B CF                        mov rcx, rdi
00B74921  E8 CA 03 86 FF                  call 0x1403d4cf0
00B74926  8B 57 40                        mov edx, dword ptr [rdi + 0x40]
00B74929  45 33 C0                        xor r8d, r8d
00B7492C  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00B74930  FF CA                           dec edx
00B74932  48 03 D1                        add rdx, rcx
00B74935  48 8B D8                        mov rbx, rax
00B74938  E8 AF F6 FF FF                  call 0x140b73fec
00B7493D  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
00B74941  85 C9                           test ecx, ecx
00B74943  74 19                           je 0x140b7495e
00B74945  8D 51 FF                        lea edx, [rcx - 1]
00B74948  45 33 C0                        xor r8d, r8d
00B7494B  48 03 D3                        add rdx, rbx
00B7494E  48 8B CB                        mov rcx, rbx
00B74951  E8 96 F6 FF FF                  call 0x140b73fec
00B74956  48 8B CF                        mov rcx, rdi
00B74959  E8 B2 02 00 00                  call 0x140b74c10
00B7495E  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00B74963  48 83 C4 20                     add rsp, 0x20
00B74967  5F                              pop rdi
00B74968  C3                              ret
00B74969  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmMarkImageForHiberPhase(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = MmLockLoadedModuleListShared(a1, a2, a3, a4);
    result = MmFindDataTableEntryByAddress(a1, a2, a3, a4);
    result = MmUnlockLoadedModuleListShared((unsigned __int8)((unsigned __int8)(result)), a2, a3, a4);
    result = MmGetLoadedModuleImageAdditionalTablesAddress(result, v_stack_p10, a3, a4);
    a3 = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 64))) - 1);
    a2 = (a2) + (*(unsigned __int64 *)(result + 48));
    result = MiMarkNonPagedHiberPhasePages(*(unsigned __int64 *)(result + 48), a2, a3, a4);
    if ((unsigned int)((unsigned int)(v_stack_p10)) != 0) {
        a2 = (unsigned int)(v_stack_p10) - 1;
        a3 = 0;
        a2 = (a2) + (result);
        a1 = result;
        result = MiMarkNonPagedHiberPhasePages(a1, a2, a3, a4);
        a1 = result;
        result = MiMarkHotPatchesForHiberPhase(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmMarkImageForHiberPhase(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = MmLockLoadedModuleListShared(Arg1, Arg2, Arg3, a4);
    result = MmFindDataTableEntryByAddress(Arg1, Arg2, Arg3, a4);
    result = MmUnlockLoadedModuleListShared((uint8_t)((uint8_t)(result)), Arg2, Arg3, a4);
    result = MmGetLoadedModuleImageAdditionalTablesAddress(result, v_stack_p10, Arg3, a4);
    Arg3 = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x40))) - 1);
    Arg2 = (Arg2) + (*(uint64_t *)(result + 0x30));
    result = MiMarkNonPagedHiberPhasePages(*(uint64_t *)(result + 0x30), Arg2, Arg3, a4);
    if ((uint32_t)((uint32_t)(v_stack_p10)) != 0) {
        Arg2 = (uint32_t)(v_stack_p10) - 1;
        Arg3 = 0;
        Arg2 = (Arg2) + (result);
        Arg1 = result;
        result = MiMarkNonPagedHiberPhasePages(Arg1, Arg2, Arg3, a4);
        Arg1 = result;
        result = MiMarkHotPatchesForHiberPhase(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B748EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B748EC[BB_00B748EC]
  bb_00B74945[BB_00B74945]
  bb_00B7495E[BB_00B7495E]
  bb_00B74969[BB_00B74969]
  bb_00B748EC -->|branch| bb_00B7495E
  bb_00B748EC -->|fallthrough| bb_00B74945
  bb_00B74945 -->|flow| bb_00B7495E
```
