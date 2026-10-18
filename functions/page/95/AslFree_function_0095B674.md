# AslFree

- RVA: `0x0095B674`–`0x0095B693` (길이 `31` bytes)
- VA: `0x000000014095B674`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **49**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0095B688` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SdbGetMergeRedirectPath](../81/SdbGetMergeRedirectPath_function_0081210C.md) at `0x0081220F`
- [SdbGetMergeRedirectPath](../81/SdbGetMergeRedirectPath_function_0081210C.md) at `0x00812258`
- [SdbOpenDatabaseEx](../81/SdbOpenDatabaseEx_function_00812284.md) at `0x008123E5`
- [SdbOpenDatabaseEx](../81/SdbOpenDatabaseEx_function_00812284.md) at `0x00812539`
- [SdbpGetManifestedMergeStubAlloc](../81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x00812ABF`
- [SdbpGetManifestedMergeStubAlloc](../81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x00812ACC`
- [SdbpGetManifestedMergeStubAlloc](../81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x00812AD9`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812E26`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812E33`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812E40`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812E51`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812E62`
- [SdbpSafeAllocAndConcatW](../81/SdbpSafeAllocAndConcatW_function_00813198.md) at `0x00813308`
- [SdbQueryDataExTagID](../81/SdbQueryDataExTagID_function_008136E0.md) at `0x00813AC4`
- [SdbpCheckMatchingDir](../81/SdbpCheckMatchingDir_function_00813EF0.md) at `0x0081400C`
- [SdbpCheckMatchingFiles](../81/SdbpCheckMatchingFiles_function_00814080.md) at `0x0081422E`
- [SdbpCheckMatchingFiles](../81/SdbpCheckMatchingFiles_function_00814080.md) at `0x00814273`
- [SdbpCheckMatchingFiles](../81/SdbpCheckMatchingFiles_function_00814080.md) at `0x008142C3`
- [SdbpCheckMatchingRegistryValue](../81/SdbpCheckMatchingRegistryValue_function_0081462C.md) at `0x00814886`
- [SdbpCheckMatchingRegistryValue](../81/SdbpCheckMatchingRegistryValue_function_0081462C.md) at `0x00814893`
- [SdbpCheckMatchingRegistryValue](../81/SdbpCheckMatchingRegistryValue_function_0081462C.md) at `0x008148A0`
- [SdbpCheckMatchingText](../81/SdbpCheckMatchingText_function_00814950.md) at `0x00814A4B`
- [SdbpCheckMatchingTextEntry](../81/SdbpCheckMatchingTextEntry_function_00814A70.md) at `0x00814BAD`
- [SdbpCheckMatchingTextEntry](../81/SdbpCheckMatchingTextEntry_function_00814A70.md) at `0x00814D2C`
- [SdbpCheckMatchingTextEntry](../81/SdbpCheckMatchingTextEntry_function_00814A70.md) at `0x00814DF7`
- [SdbpCheckMatchingWildcardFiles](../81/SdbpCheckMatchingWildcardFiles_function_00814E30.md) at `0x00815062`
- [SdbpCheckMatchingWildcardFiles](../81/SdbpCheckMatchingWildcardFiles_function_00814E30.md) at `0x008150C6`
- [SdbpFreeAppAttributes](../81/SdbpFreeAppAttributes_function_0081587C.md) at `0x00815960`
- [SdbpGetMatchingTextAttributes](../81/SdbpGetMatchingTextAttributes_function_00815B38.md) at `0x00815D39`
- [SdbpResolveMatchingFile](../81/SdbpResolveMatchingFile_function_00816A20.md) at `0x00816CD0`
- [SdbpResolveMatchingFile](../81/SdbpResolveMatchingFile_function_00816A20.md) at `0x00816CED`
- [SdbResolveDatabaseEx](../81/SdbResolveDatabaseEx_function_00817A54.md) at `0x00817D5C`
- [SdbpOpenCompressedDatabase](../81/SdbpOpenCompressedDatabase_function_00818524.md) at `0x0081864E`
- [SdbpCheckAllAttributes](../81/SdbpCheckAllAttributes_function_008187EC.md) at `0x00818A71`
- [AslGuidToString_UStr](../81/AslGuidToString_UStr_function_008196DC.md) at `0x008197F6`
- [AslStringAnsiToUnicode](../81/AslStringAnsiToUnicode_function_00819824.md) at `0x00819928`
- [AslUnicodeStringFree](../81/AslUnicodeStringFree_function_00819AB8.md) at `0x00819AE1`
- [AslRegistryGetKey](../81/AslRegistryGetKey_function_00819F64.md) at `0x0081A060`
- [AslRegistryGetString](../81/AslRegistryGetString_function_0081A084.md) at `0x0081A207`
- [AslPathToNetworkPathNt](../81/AslPathToNetworkPathNt_function_0081B2A4.md) at `0x0081B347`
- [AslPathWildcardFindFirst](../81/AslPathWildcardFindFirst_function_0081B534.md) at `0x0081BAE2`
- [AslPathWildcardFindNext](../81/AslPathWildcardFindNext_function_0081BB2C.md) at `0x0081C251`
- [AslRegWildcardFindClose](../81/AslRegWildcardFindClose_function_0081C27C.md) at `0x0081C2B4`
- [AslRegWildcardFindClose](../81/AslRegWildcardFindClose_function_0081C27C.md) at `0x0081C2CA`
- [AslRegWildcardFindClose](../81/AslRegWildcardFindClose_function_0081C27C.md) at `0x0081C2D2`
- [AslpPathWildcardFreeFindContext](../81/AslpPathWildcardFreeFindContext_function_0081C844.md) at `0x0081C8E9`
- [AslpPathWildcardFreeFindContext](../81/AslpPathWildcardFreeFindContext_function_0081C844.md) at `0x0081C8F6`
- [AslpPathWildcardFreeMatchNode](../81/AslpPathWildcardFreeMatchNode_function_0081C918.md) at `0x0081C941`
- [AslpProcessMatchRegNode](../81/AslpProcessMatchRegNode_function_0081CB08.md) at `0x0081CC45`
- [AslHashFree](../81/AslHashFree_function_0081CC70.md) at `0x0081CCAE`
- [AslHashFree](../81/AslHashFree_function_0081CC70.md) at `0x0081CCC9`
- [AslHashFree](../81/AslHashFree_function_0081CC70.md) at `0x0081CCD1`
- [AslEnvExpandStrings2](../81/AslEnvExpandStrings2_function_0081CECC.md) at `0x0081D08A`
- [AslFileFreeAttributes](../81/AslFileFreeAttributes_function_0081DE28.md) at `0x0081DE5C`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FF6F`
- [AslpFileGetVersionBlockImageOnly](../82/AslpFileGetVersionBlockImageOnly_function_00820260.md) at `0x008204E1`
- [AslpFileLargeMapDelete](../82/AslpFileLargeMapDelete_function_00821CF0.md) at `0x00821D2D`
- [SdbpReleaseSearchDBContext](SdbpReleaseSearchDBContext_function_00958118.md) at `0x0095813C`
- [SdbpReleaseSearchDBContext](SdbpReleaseSearchDBContext_function_00958118.md) at `0x0095814F`
- [SdbpReleaseSearchDBContext](SdbpReleaseSearchDBContext_function_00958118.md) at `0x009581A8`
- [SdbpReleaseSearchDBContext](SdbpReleaseSearchDBContext_function_00958118.md) at `0x009581BE`
- [SdbpReleaseSearchDBContext](SdbpReleaseSearchDBContext_function_00958118.md) at `0x009581D1`
- [SdbpReleaseSearchDBContext](SdbpReleaseSearchDBContext_function_00958118.md) at `0x009581E4`
- [SdbpReleaseSearchDBContext](SdbpReleaseSearchDBContext_function_00958118.md) at `0x009581F7`
- [AslStringDuplicate](AslStringDuplicate_function_00958604.md) at `0x009586B8`
- [AslStringUpcaseToMultiByteN](AslStringUpcaseToMultiByteN_function_0095965C.md) at `0x00959731`
- [SdbpOpenDatabaseInMemory](SdbpOpenDatabaseInMemory_function_0095A574.md) at `0x0095A616`
- [SdbpRemoveSDBLookupEntry](SdbpRemoveSDBLookupEntry_function_0095A6D8.md) at `0x0095A714`
- [SdbCloseDatabaseRead](SdbCloseDatabaseRead_function_0095A728.md) at `0x0095A752`
- [SdbCloseDatabaseRead](SdbCloseDatabaseRead_function_0095A728.md) at `0x0095A771`
- [SdbCloseDatabaseRead](SdbCloseDatabaseRead_function_0095A728.md) at `0x0095A785`
- [SdbReleaseDatabase](SdbReleaseDatabase_function_0095B57C.md) at `0x0095B5DF`
- [AslFileMappingDelete](AslFileMappingDelete_function_0095B728.md) at `0x0095B749`
- [AslFileMappingDelete](AslFileMappingDelete_function_0095B728.md) at `0x0095B75F`
- [AslpFileVerQueryBlock](../AF/AslpFileVerQueryBlock_function_00AF9694.md) at `0x00AF9887`
- [sub_00B2765C](../B2/Unknown_function_00B2765C.md) at `0x00B27663`
- [sub_00B2788A](../B2/Unknown_function_00B2788A.md) at `0x00B2788D`
- [sub_00B2795A](../B2/Unknown_function_00B2795A.md) at `0x00B2795D`
- [sub_00B488F0](../B4/Unknown_function_00B488F0.md) at `0x00B48A0B`
- [sub_00B488F0](../B4/Unknown_function_00B488F0.md) at `0x00B48A1C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0095B688` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0095B674  48 83 EC 28                     sub rsp, 0x28
0095B678  48 8B C2                        mov rax, rdx
0095B67B  48 85 D2                        test rdx, rdx
0095B67E  74 0D                           je 0x14095b68d
0095B680  BA 41 50 70 74                  mov edx, 0x74705041
0095B685  48 8B C8                        mov rcx, rax
0095B688  E8 E3 71 22 00                  call 0x140b82870
0095B68D  48 83 C4 28                     add rsp, 0x28
0095B691  C3                              ret
0095B692  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AslFree(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = a2;
    if (a2 != 0) {
        a2 = 0x74705041ULL;
        a1 = a2;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AslFree(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Arg2;
    if (Arg2 != 0) {
        Arg2 = 0x74705041ULL;
        Arg1 = Arg2;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0095B674&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0095B674[BB_0095B674]
  bb_0095B680[BB_0095B680]
  bb_0095B68D[BB_0095B68D]
  bb_0095B692[BB_0095B692]
  bb_0095B674 -->|branch| bb_0095B68D
  bb_0095B674 -->|fallthrough| bb_0095B680
  bb_0095B680 -->|flow| bb_0095B68D
```
