# ViRaiseIrqlToDpcLevel

- RVA: `0x006162B0`–`0x006162E2` (길이 `50` bytes)
- VA: `0x00000001406162B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006162D4` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [ViDeadlockRemoveMemoryRangeResources](ViDeadlockRemoveMemoryRangeResources_function_00615FE8.md) at `0x00616023`
- [ViDeadlockRemoveMemoryRangeThreads](ViDeadlockRemoveMemoryRangeThreads_function_00616148.md) at `0x0061617E`
- [VfDeadlockInitializeResource](../../pagevrfy/BA/VfDeadlockInitializeResource_function_00BA80A0.md) at `0x00BA816E`
- [ViDeadlockDetectionApplySettings](../../pagevrfy/BA/ViDeadlockDetectionApplySettings_function_00BA9178.md) at `0x00BA9182`
- [ViDeadlockEmptyDatabase](../../pagevrfy/BA/ViDeadlockEmptyDatabase_function_00BA922C.md) at `0x00BA924C`
- [ViIsThreadInsidePagingCodePaths](../../pagevrfy/BA/ViIsThreadInsidePagingCodePaths_function_00BAA2D4.md) at `0x00BAA2EE`
- [VfDeadlockReleaseResource](../../pagevrfy/BB/VfDeadlockReleaseResource_function_00BB759C.md) at `0x00BB7670`
- [VfDeadlockAcquireResource](../../pagevrfy/BB/VfDeadlockAcquireResource_function_00BB83B4.md) at `0x00BB8509`

### Static image references
- `0x006162CB` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006162B0  40 53                           push rbx
006162B2  48 83 EC 20                     sub rsp, 0x20
006162B6  44 0F 20 C3                     mov rbx, cr8
006162BA  BA 02 00 00 00                  mov edx, 2
006162BF  3A DA                           cmp bl, dl
006162C1  73 16                           jae 0x1406162d9
006162C3  44 0F 20 C1                     mov rcx, cr8
006162C7  44 0F 22 C2                     mov cr8, rdx
006162CB  83 3D 4E 0A 9B 00 00            cmp dword ptr [rip + 0x9b0a4e], 0
006162D2  74 05                           je 0x1406162d9
006162D4  E8 23 F4 ED FF                  call 0x1404f56fc
006162D9  8A C3                           mov al, bl
006162DB  48 83 C4 20                     add rsp, 0x20
006162DF  5B                              pop rbx
006162E0  C3                              ret
006162E1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViRaiseIrqlToDpcLevel(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_006162D9;
    if ((*(unsigned int *)(v_rip + 10160718)) != 0) {
        result = KiRaiseIrqlProcessIrqlFlags(v_cr8, 2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
}
```

## 5. (Beta) C Style

```c
void ViRaiseIrqlToDpcLevel(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (((uint8_t)(v_cr8)) >= 2) goto loc_006162D9;
    if ((*(uint32_t *)(v_rip + 0x9B0A4E)) != 0) {
        result = KiRaiseIrqlProcessIrqlFlags(v_cr8, 2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006162B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006162B0[BB_006162B0]
  bb_006162C3[BB_006162C3]
  bb_006162D4[BB_006162D4]
  bb_006162D9[BB_006162D9]
  bb_006162E1[BB_006162E1]
  bb_006162B0 -->|branch| bb_006162D9
  bb_006162B0 -->|fallthrough| bb_006162C3
  bb_006162C3 -->|branch| bb_006162D9
  bb_006162C3 -->|fallthrough| bb_006162D4
  bb_006162D4 -->|flow| bb_006162D9
```
