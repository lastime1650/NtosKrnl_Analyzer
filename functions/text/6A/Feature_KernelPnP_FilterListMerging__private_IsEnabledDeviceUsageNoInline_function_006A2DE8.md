# Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline

- RVA: `0x006A2DE8`–`0x006A2E1A` (길이 `50` bytes)
- VA: `0x00000001406A2DE8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006A2E0F` → [Feature_KernelPnP_FilterListMerging__private_IsEnabledFallback](Feature_KernelPnP_FilterListMerging__private_IsEnabledFallback_function_006A2E20.md) (function, `0x006A2E20`)

### Direct callers
- [CmGetInstallerClassCompoundFiltersWorker](../../page/83/CmGetInstallerClassCompoundFiltersWorker_function_00830130.md) at `0x008305C6`
- [CmGetDeviceCompoundFiltersWorker](../../page/AF/CmGetDeviceCompoundFiltersWorker_function_00AF9CE8.md) at `0x00AFA189`
- [CmMergeFilterLists](../../page/AF/CmMergeFilterLists_function_00AFA2CC.md) at `0x00AFA308`
- [CmMergeFilterLists](../../page/AF/CmMergeFilterLists_function_00AFA2CC.md) at `0x00AFA3DF`
- [CmMergeFilterLists](../../page/AF/CmMergeFilterLists_function_00AFA2CC.md) at `0x00AFA3EF`
- [CmMergeFilterLists](../../page/AF/CmMergeFilterLists_function_00AFA2CC.md) at `0x00AFA4C2`
- [CmMergeFilterLists](../../page/AF/CmMergeFilterLists_function_00AFA2CC.md) at `0x00AFA4D2`
- [CmMergeFilterLists](../../page/AF/CmMergeFilterLists_function_00AFA2CC.md) at `0x00AFA595`
- [CmMergeFilterLists](../../page/AF/CmMergeFilterLists_function_00AFA2CC.md) at `0x00AFA5A5`

### Static image references
- `0x006A2DF2` → RVA `0x00FC4890` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A2DE8  48 83 EC 28                     sub rsp, 0x28
006A2DEC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
006A2DF2  8B 05 98 1A 92 00               mov eax, dword ptr [rip + 0x921a98]
006A2DF8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006A2DFC  A8 10                           test al, 0x10
006A2DFE  74 05                           je 0x1406a2e05
006A2E00  83 E0 01                        and eax, 1
006A2E03  EB 0F                           jmp 0x1406a2e14
006A2E05  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
006A2E0A  BA 03 00 00 00                  mov edx, 3
006A2E0F  E8 0C 00 00 00                  call 0x1406a2e20
006A2E14  48 83 C4 28                     add rsp, 0x28
006A2E18  C3                              ret
006A2E19  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9575064)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9575064)))) & (16)) == 0) goto loc_006A2E05;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9575064))) & (1));
    goto loc_006A2E14;
loc_006A2E05:
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_006A2E14:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_KernelPnP_FilterListMerging__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x921A98)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x921A98)))) & (16)) == 0) goto loc_006A2E05;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x921A98))) & (1));
    goto loc_006A2E14;
loc_006A2E05:
    result = Feature_KernelPnP_FilterListMerging__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_006A2E14:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A2DE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A2DE8[BB_006A2DE8]
  bb_006A2E00[BB_006A2E00]
  bb_006A2E05[BB_006A2E05]
  bb_006A2E14[BB_006A2E14]
  bb_006A2E19[BB_006A2E19]
  bb_006A2DE8 -->|branch| bb_006A2E05
  bb_006A2DE8 -->|fallthrough| bb_006A2E00
  bb_006A2E00 -->|branch| bb_006A2E14
  bb_006A2E05 -->|flow| bb_006A2E14
```
