# BiLogMessage

- RVA: `0x00A3D3A8`–`0x00A3D3B6` (길이 `14` bytes)
- VA: `0x0000000140A3D3A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `14/14` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **49**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [BiMapEfiDeviceForSpaces](../../text/4C/BiMapEfiDeviceForSpaces_function_004C06F4.md) at `0x004C07B2`
- [BiLogFileOwnerProcess](../../text/69/BiLogFileOwnerProcess_function_0069E404.md) at `0x0069E47C`
- [BiLogFileOwnerProcess](../../text/69/BiLogFileOwnerProcess_function_0069E404.md) at `0x0069E501`
- [BiLogFileOwnerProcess](../../text/69/BiLogFileOwnerProcess_function_0069E404.md) at `0x0069E554`
- [BiLogFileOwnerProcess](../../text/69/BiLogFileOwnerProcess_function_0069E404.md) at `0x0069E646`
- [BiLogFileOwnerProcess](../../text/69/BiLogFileOwnerProcess_function_0069E404.md) at `0x0069E698`
- [BiSpacesUpdatePhysicalDevicePath](../../text/69/BiSpacesUpdatePhysicalDevicePath_function_0069E6F8.md) at `0x0069E737`
- [BiSpacesUpdatePhysicalDevicePath](../../text/69/BiSpacesUpdatePhysicalDevicePath_function_0069E6F8.md) at `0x0069E776`
- [BiSpacesUpdatePhysicalDevicePath](../../text/69/BiSpacesUpdatePhysicalDevicePath_function_0069E6F8.md) at `0x0069E866`
- [BcdFlushStore](../82/BcdFlushStore_function_00823294.md) at `0x008232C3`
- [BcdForciblyUnloadStore](../82/BcdForciblyUnloadStore_function_008232FC.md) at `0x00823330`
- [BcdForciblyUnloadStore](../82/BcdForciblyUnloadStore_function_008232FC.md) at `0x0082335E`
- [BcdForciblyUnloadStore](../82/BcdForciblyUnloadStore_function_008232FC.md) at `0x0082338E`
- [BcdOpenSystemStore](../82/BcdOpenSystemStore_function_00823428.md) at `0x0082344B`
- [BcdSetSystemStore](../82/BcdSetSystemStore_function_00823478.md) at `0x008234B3`
- [BiAddBootEntry](../82/BiAddBootEntry_function_00826260.md) at `0x008262AF`
- [BiCreateBootEntry](../82/BiCreateBootEntry_function_00826510.md) at `0x00826582`
- [BiCreateBootEntry](../82/BiCreateBootEntry_function_00826510.md) at `0x008265B6`
- [BiCreateBootEntry](../82/BiCreateBootEntry_function_00826510.md) at `0x008265EE`
- [BiCreateEfiEntry](../82/BiCreateEfiEntry_function_008268C4.md) at `0x00826972`
- [BiCreateEfiEntry](../82/BiCreateEfiEntry_function_008268C4.md) at `0x00826A08`
- [BiCreateEfiEntry](../82/BiCreateEfiEntry_function_008268C4.md) at `0x00826A68`
- [BiDeleteBootEntry](../82/BiDeleteBootEntry_function_00826AB0.md) at `0x00826AD1`
- [BiDeleteBootEntry](../82/BiDeleteBootEntry_function_00826AB0.md) at `0x00826B0A`
- [BiExportBcdObjects](../82/BiExportBcdObjects_function_00826B30.md) at `0x00826C2E`
- [BiExportStoreAlterationsToEfi](../82/BiExportStoreAlterationsToEfi_function_00826C58.md) at `0x00826C76`
- [BiExportStoreAlterationsToEfi](../82/BiExportStoreAlterationsToEfi_function_00826C58.md) at `0x00826CDE`
- [BiModifyBootEntry](../82/BiModifyBootEntry_function_00826E80.md) at `0x00826EC9`
- [BiSetBootOptions](../82/BiSetBootOptions_function_00826FD0.md) at `0x0082701D`
- [BiTranslateObjectIdentifier](../82/BiTranslateObjectIdentifier_function_00827048.md) at `0x008270A3`
- [BiUpdateBcdObject](../82/BiUpdateBcdObject_function_008270D0.md) at `0x0082736F`
- [BcdOpenObject](../91/BcdOpenObject_function_00916704.md) at `0x0091678D`
- [BcdOpenObject](../91/BcdOpenObject_function_00916704.md) at `0x009167C0`
- [BcdOpenObject](../91/BcdOpenObject_function_00916704.md) at `0x0091685E`
- [BiLoadSystemStore](BiLoadSystemStore_function_00A3C198.md) at `0x00A3C267`
- [BiLoadSystemStore](BiLoadSystemStore_function_00A3C198.md) at `0x00A3C2B8`
- [BiLoadSystemStore](BiLoadSystemStore_function_00A3C198.md) at `0x00A3C2E5`
- [BcdGetSystemStorePath](BcdGetSystemStorePath_function_00A3C340.md) at `0x00A3C400`
- [BcdGetSystemStorePath](BcdGetSystemStorePath_function_00A3C340.md) at `0x00A3C430`
- [BcdGetSystemStorePath](BcdGetSystemStorePath_function_00A3C340.md) at `0x00A3C459`
- [BcdGetSystemStorePath](BcdGetSystemStorePath_function_00A3C340.md) at `0x00A3C47D`
- [BcdGetSystemStorePath](BcdGetSystemStorePath_function_00A3C340.md) at `0x00A3C4A0`
- [BiCloseStore](BiCloseStore_function_00A3C5D8.md) at `0x00A3C60E`
- [BiCloseStore](BiCloseStore_function_00A3C5D8.md) at `0x00A3C63C`
- [BcdCloseStore](BcdCloseStore_function_00A3C68C.md) at `0x00A3C6D2`
- [BcdCloseStore](BcdCloseStore_function_00A3C68C.md) at `0x00A3C70B`
- [BiTranslateBootEntryId](BiTranslateBootEntryId_function_00A3CBDC.md) at `0x00A3CC34`
- [BiSetBootEntryOrder](BiSetBootEntryOrder_function_00A3CC48.md) at `0x00A3CCB2`
- [BiUpdateEfiEntry](BiUpdateEfiEntry_function_00A3CCC0.md) at `0x00A3CDE2`
- [BiUpdateEfiEntry](BiUpdateEfiEntry_function_00A3CCC0.md) at `0x00A3CE37`
- [BiCreateObject](BiCreateObject_function_00A3D92C.md) at `0x00A3D995`
- [BiCreateObject](BiCreateObject_function_00A3D92C.md) at `0x00A3DA23`
- [BiQueryBootOptions](BiQueryBootOptions_function_00A3DB04.md) at `0x00A3DB5C`
- [BiQueryBootEntryOrder](BiQueryBootEntryOrder_function_00A3DBD4.md) at `0x00A3DC67`
- [BiBindEfiBootManager](BiBindEfiBootManager_function_00A3DCB0.md) at `0x00A3DF71`
- [BiDeleteElement](BiDeleteElement_function_00A3E0F8.md) at `0x00A3E14C`
- [BiDeleteElement](BiDeleteElement_function_00A3E0F8.md) at `0x00A3E242`
- [BiDeleteElement](BiDeleteElement_function_00A3E0F8.md) at `0x00A3E26F`
- [BiDeleteElement](BiDeleteElement_function_00A3E0F8.md) at `0x00A3E295`
- [BiBuildIdentifierList](BiBuildIdentifierList_function_00A3E584.md) at `0x00A3EBD2`
- [BcdGetElementDataWithFlags](BcdGetElementDataWithFlags_function_00A3EBE4.md) at `0x00A3EE19`
- [BcdGetElementDataWithFlags](BcdGetElementDataWithFlags_function_00A3EBE4.md) at `0x00A3EE35`
- [BcdGetElementDataWithFlags](BcdGetElementDataWithFlags_function_00A3EBE4.md) at `0x00A3EE4B`
- [BcdGetElementDataWithFlags](BcdGetElementDataWithFlags_function_00A3EBE4.md) at `0x00A3EE86`
- [BcdSetElementDataWithFlags](BcdSetElementDataWithFlags_function_00A3F080.md) at `0x00A3F103`
- [BcdSetElementDataWithFlags](BcdSetElementDataWithFlags_function_00A3F080.md) at `0x00A3F1FA`
- [BcdSetElementDataWithFlags](BcdSetElementDataWithFlags_function_00A3F080.md) at `0x00A3F2A1`
- [BcdSetElementDataWithFlags](BcdSetElementDataWithFlags_function_00A3F080.md) at `0x00A3F2DC`
- [BiGetRegistryValue](BiGetRegistryValue_function_00A3F3CC.md) at `0x00A3F5F5`
- [BiConvertRegistryDataToElement](BiConvertRegistryDataToElement_function_00A3F804.md) at `0x00A3F99E`
- [BiEnumerateBootEntries](../A4/BiEnumerateBootEntries_function_00A4074C.md) at `0x00A40801`
- [BiOpenSystemStore](../A4/BiOpenSystemStore_function_00A40844.md) at `0x00A4088C`
- [BiOpenSystemStore](../A4/BiOpenSystemStore_function_00A40844.md) at `0x00A40987`
- [BiOpenSystemStore](../A4/BiOpenSystemStore_function_00A40844.md) at `0x00A40A3F`
- [BiOpenSystemStore](../A4/BiOpenSystemStore_function_00A40844.md) at `0x00A40AE5`
- [BiOpenSystemStore](../A4/BiOpenSystemStore_function_00A40844.md) at `0x00A40B02`
- [BiAddStoreFromFile](../A4/BiAddStoreFromFile_function_00A40C54.md) at `0x00A40CED`
- [BiAddStoreFromFile](../A4/BiAddStoreFromFile_function_00A40C54.md) at `0x00A40D6F`
- [BiAddStoreFromFile](../A4/BiAddStoreFromFile_function_00A40C54.md) at `0x00A40E3E`
- [BiAddStoreFromFile](../A4/BiAddStoreFromFile_function_00A40C54.md) at `0x00A40E85`
- [BiBindEfiNamespaceObjects](../A4/BiBindEfiNamespaceObjects_function_00A40EB4.md) at `0x00A40ECD`
- [BiBindEfiNamespaceObjects](../A4/BiBindEfiNamespaceObjects_function_00A40EB4.md) at `0x00A40F2E`
- [BcdOpenStore](../A4/BcdOpenStore_function_00A4116C.md) at `0x00A411BA`
- [BcdOpenStore](../A4/BcdOpenStore_function_00A4116C.md) at `0x00A411D5`
- [BcdOpenStore](../A4/BcdOpenStore_function_00A4116C.md) at `0x00A411F6`
- [BcdOpenStore](../A4/BcdOpenStore_function_00A4116C.md) at `0x00A4121B`
- [BiLoadHive](../A4/BiLoadHive_function_00A412F4.md) at `0x00A413C1`
- [BiLoadHive](../A4/BiLoadHive_function_00A412F4.md) at `0x00A41480`
- [BiLoadHive](../A4/BiLoadHive_function_00A412F4.md) at `0x00A4150F`
- [BiLoadHive](../A4/BiLoadHive_function_00A412F4.md) at `0x00A41571`
- [BiBindEfiEntries](../AB/BiBindEfiEntries_function_00AB09C4.md) at `0x00AB0A16`
- [BiBindEfiEntries](../AB/BiBindEfiEntries_function_00AB09C4.md) at `0x00AB0AFA`
- [BiExportEfiBootManager](../AC/BiExportEfiBootManager_function_00ACB13C.md) at `0x00ACB480`
- [sub_00B21A3E](../B2/Unknown_function_00B21A3E.md) at `0x00B21A7E`
- [sub_00B3A4AA](../B3/Unknown_function_00B3A4AA.md) at `0x00B3A4BC`
- [sub_00B3A518](../B3/Unknown_function_00B3A518.md) at `0x00B3A528`
- [sub_00B3A622](../B3/Unknown_function_00B3A622.md) at `0x00B3A68C`
- [sub_00B3A622](../B3/Unknown_function_00B3A622.md) at `0x00B3A6E3`
- [sub_00B3A622](../B3/Unknown_function_00B3A622.md) at `0x00B3A756`
- [sub_00B3A892](../B3/Unknown_function_00B3A892.md) at `0x00B3A9CA`
- [sub_00B3A892](../B3/Unknown_function_00B3A892.md) at `0x00B3AA1D`
- [sub_00B3AA4C](../B3/Unknown_function_00B3AA4C.md) at `0x00B3AA62`
- [sub_00B3AA4C](../B3/Unknown_function_00B3AA4C.md) at `0x00B3AA93`
- [sub_00B3AA4C](../B3/Unknown_function_00B3AA4C.md) at `0x00B3AAB6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A3D3A8  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00A3D3AD  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00A3D3B2  33 C0                           xor eax, eax
00A3D3B4  C3                              ret
00A3D3B5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiLogMessage(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = a3;
    v_stack_p20 = a4;
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BiLogMessage(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = Arg3;
    v_stack_p20 = Arg4;
    result = 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A3D3A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A3D3A8[BB_00A3D3A8]
  bb_00A3D3B5[BB_00A3D3B5]
```
