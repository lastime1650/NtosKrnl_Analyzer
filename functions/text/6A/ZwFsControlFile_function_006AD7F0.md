# ZwFsControlFile

- RVA: `0x006AD7F0`–`0x006AD80F` (길이 `31` bytes)
- VA: `0x00000001406AD7F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C013C`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiTrimUnusedPageFileRegionsWorker](../2A/MiTrimUnusedPageFileRegionsWorker_function_002AA320.md) at `0x002AA5EF`
- [DifZwFsControlFileWrapper](../64/DifZwFsControlFileWrapper_function_00642680.md) at `0x006427D0`
- [FsRtlpRegisterProviderWithMUP](../../page/71/FsRtlpRegisterProviderWithMUP_function_007143D4.md) at `0x00714484`
- [PfpQueryFileExtentsRequest](../../page/75/PfpQueryFileExtentsRequest_function_007508E8.md) at `0x00750D34`
- [PopClearHiberFileSignature](../../page/75/PopClearHiberFileSignature_function_0075CD90.md) at `0x0075CE25`
- [PopCreateHiberFile](../../page/75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D0AB`
- [PopCreateHiberFile](../../page/75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D29A`
- [SmKmStoreFileGetExtents](../../page/7A/SmKmStoreFileGetExtents_function_007A971C.md) at `0x007A97F8`
- [CmpHiveCacheAcknowledgeOplockBreak](../../page/7F/CmpHiveCacheAcknowledgeOplockBreak_function_007F585C.md) at `0x007F5925`
- [CmpRequestOplockOnHiveFile](../../page/7F/CmpRequestOplockOnHiveFile_function_007F63E8.md) at `0x007F6479`
- [CmpRequestOplockOnHiveFile](../../page/7F/CmpRequestOplockOnHiveFile_function_007F63E8.md) at `0x007F6507`
- [CmpRequestOplockOnHiveFile](../../page/7F/CmpRequestOplockOnHiveFile_function_007F63E8.md) at `0x007F6598`
- [CmpOpenHiveFile](../../page/87/CmpOpenHiveFile_function_0087A71C.md) at `0x0087AA4C`
- [RtlUnlockBootStatusData](../../page/A4/RtlUnlockBootStatusData_function_00A4CAF0.md) at `0x00A4CB79`
- [PopSanityCheckHiberFile](../../page/A9/PopSanityCheckHiberFile_function_00A90840.md) at `0x00A90897`
- [sub_00B1833E](../../page/B1/Unknown_function_00B1833E.md) at `0x00B18416`

### Static image references
- `0x006AD7FC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD809` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD7F0  48 8B C4                        mov rax, rsp
006AD7F3  FA                              cli
006AD7F4  48 83 EC 10                     sub rsp, 0x10
006AD7F8  50                              push rax
006AD7F9  9C                              pushfq
006AD7FA  6A 10                           push 0x10
006AD7FC  48 8D 05 5D 5C 00 00            lea rax, [rip + 0x5c5d]
006AD803  50                              push rax
006AD804  B8 39 00 00 00                  mov eax, 0x39
006AD809  E9 B2 71 01 00                  jmp 0x1406c49c0
006AD80E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwFsControlFile(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwFsControlFile(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD7F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD7F0[BB_006AD7F0]
  bb_006AD80E[BB_006AD80E]
```
