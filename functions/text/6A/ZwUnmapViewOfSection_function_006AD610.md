# ZwUnmapViewOfSection

- RVA: `0x006AD610`–`0x006AD62F` (길이 `31` bytes)
- VA: `0x00000001406AD610`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0088`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmSiUnmapViewOfSection](../4A/CmSiUnmapViewOfSection_function_004A4738.md) at `0x004A4742`
- [RtlFileMapFree](../4B/RtlFileMapFree_function_004BF868.md) at `0x004BF8DE`
- [RtlFileMapMapView](../69/RtlFileMapMapView_function_0069D048.md) at `0x0069D1BF`
- [IopIsNotNativeDriverImage](../../page/71/IopIsNotNativeDriverImage_function_0071B914.md) at `0x0071BAC7`
- [ExpQueryElamCertInfo](../../page/7C/ExpQueryElamCertInfo_function_007C4564.md) at `0x007C47F2`
- [CMFReadCompressedSegment](../../page/7D/CMFReadCompressedSegment_function_007D3580.md) at `0x007D37E2`
- [CMFSystemThreadRoutine](../../page/7D/CMFSystemThreadRoutine_function_007D3A70.md) at `0x007D3F7F`
- [CMFSystemThreadRoutine](../../page/7D/CMFSystemThreadRoutine_function_007D3A70.md) at `0x007D3FF1`
- [ApiSetLoadSchemaEx](../../page/7D/ApiSetLoadSchemaEx_function_007D96F4.md) at `0x007D97E5`
- [AslpFilePartialViewFree](../../page/82/AslpFilePartialViewFree_function_00821D48.md) at `0x00821D74`
- [PiInitializeDDB](../../page/99/PiInitializeDDB_function_0099ADE4.md) at `0x0099AF75`
- [PiReleaseDDB](../../page/99/PiReleaseDDB_function_0099C4F4.md) at `0x0099C53B`
- [ExpQueryCodeIntegrityCertificateInfo](../../page/A8/ExpQueryCodeIntegrityCertificateInfo_function_00A8552C.md) at `0x00A85654`
- [CmpSetSystemBiosInformation](../../init/C5/CmpSetSystemBiosInformation_function_00C5A5D0.md) at `0x00C5A92E`
- [CmpSetVideoBiosInformation](../../init/C5/CmpSetVideoBiosInformation_function_00C5A970.md) at `0x00C5AA41`
- [CmpSetVideoBiosInformation](../../init/C5/CmpSetVideoBiosInformation_function_00C5A970.md) at `0x00C5AC1C`
- [EmpCacheBiosDate](../../init/C7/EmpCacheBiosDate_function_00C73258.md) at `0x00C73364`

### Static image references
- `0x006AD61C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD629` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD610  48 8B C4                        mov rax, rsp
006AD613  FA                              cli
006AD614  48 83 EC 10                     sub rsp, 0x10
006AD618  50                              push rax
006AD619  9C                              pushfq
006AD61A  6A 10                           push 0x10
006AD61C  48 8D 05 3D 5E 00 00            lea rax, [rip + 0x5e3d]
006AD623  50                              push rax
006AD624  B8 2A 00 00 00                  mov eax, 0x2a
006AD629  E9 92 73 01 00                  jmp 0x1406c49c0
006AD62E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwUnmapViewOfSection(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwUnmapViewOfSection(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD610&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD610[BB_006AD610]
  bb_006AD62E[BB_006AD62E]
```
