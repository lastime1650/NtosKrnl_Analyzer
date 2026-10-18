# KsepPoolFreePaged

- RVA: `0x004B0E10`–`0x004B0E30` (길이 `32` bytes)
- VA: `0x00000001404B0E10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **30**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B0E1E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [KsepEvntLogShimsApplied](../5C/KsepEvntLogShimsApplied_function_005CBBE4.md) at `0x005CBDDF`
- [KsepEvntLogShimsApplied](../5C/KsepEvntLogShimsApplied_function_005CBBE4.md) at `0x005CBDF2`
- [KsepCacheHwIdFree](../5C/KsepCacheHwIdFree_function_005CBE30.md) at `0x005CBE49`
- [KsepDbGetShimInfo](../../page/74/KsepDbGetShimInfo_function_00748E94.md) at `0x00749084`
- [KsepDbQueryRegistryDeviceDataList](../../page/74/KsepDbQueryRegistryDeviceDataList_function_007490B4.md) at `0x007491EA`
- [KseRegisterShimEx](../../page/74/KseRegisterShimEx_function_007494D0.md) at `0x007496E3`
- [KseRegisterShimEx](../../page/74/KseRegisterShimEx_function_007494D0.md) at `0x007497D4`
- [KseUnregisterShim](../../page/74/KseUnregisterShim_function_00749800.md) at `0x00749A76`
- [KsepResolveApplicableShimsForDriver](../../page/74/KsepResolveApplicableShimsForDriver_function_0074A168.md) at `0x0074A609`
- [KsepSdbBootInitialize](../../page/74/KsepSdbBootInitialize_function_0074A7EC.md) at `0x0074A8E8`
- [KsepSdbBootRelease](../../page/74/KsepSdbBootRelease_function_0074A924.md) at `0x0074A947`
- [KsepGetLoadedModulesList](../../page/74/KsepGetLoadedModulesList_function_0074A960.md) at `0x0074A9C2`
- [KsepGetLoadedModulesList](../../page/74/KsepGetLoadedModulesList_function_0074A960.md) at `0x0074A9D2`
- [KsepStringSplitMultiString](../../page/74/KsepStringSplitMultiString_function_0074AB48.md) at `0x0074ACBD`
- [KsepCacheDeviceInsertData](../../page/74/KsepCacheDeviceInsertData_function_0074AD9C.md) at `0x0074AE11`
- [KsepCacheDeviceInsertData](../../page/74/KsepCacheDeviceInsertData_function_0074AD9C.md) at `0x0074AE19`
- [KsepCacheInitialize](../../page/74/KsepCacheInitialize_function_0074AE7C.md) at `0x0074AF0B`
- [KsepCacheInitialize](../../page/74/KsepCacheInitialize_function_0074AE7C.md) at `0x0074AF13`
- [KsepCacheUninitialize](../../page/74/KsepCacheUninitialize_function_0074AFB0.md) at `0x0074AFE4`
- [KsepCacheUninitialize](../../page/74/KsepCacheUninitialize_function_0074AFB0.md) at `0x0074AFEC`
- [KsepRegistryEnumValue](../../page/74/KsepRegistryEnumValue_function_0074B24C.md) at `0x0074B31F`
- [KsepRegistryQueryKeyInformation](../../page/74/KsepRegistryQueryKeyInformation_function_0074B498.md) at `0x0074B538`
- [KsepRegistryQuerySZ](../../page/74/KsepRegistryQuerySZ_function_0074B58C.md) at `0x0074B7CE`
- [KsepRegistryQueryValue](../../page/74/KsepRegistryQueryValue_function_0074B7F8.md) at `0x0074BA36`
- [KsepDbFreeDriverShims](../../page/95/KsepDbFreeDriverShims_function_00958754.md) at `0x009587BD`
- [KseDriverLoadImage](../../page/95/KseDriverLoadImage_function_009588C0.md) at `0x009589D3`
- [KseDriverLoadImage](../../page/95/KseDriverLoadImage_function_009588C0.md) at `0x009589E8`
- [KseShimDriverIoCallbacks](../../page/95/KseShimDriverIoCallbacks_function_00958BFC.md) at `0x00958C74`
- [KsepEngineGetShimsFromRegistry](../../page/95/KsepEngineGetShimsFromRegistry_function_0095907C.md) at `0x009590E4`
- [KsepEngineGetShimsFromRegistry](../../page/95/KsepEngineGetShimsFromRegistry_function_0095907C.md) at `0x0095910D`
- [KseAddHardwareId](../../page/95/KseAddHardwareId_function_00959254.md) at `0x00959380`
- [KsepRegistryQueryDriverShims](../../page/95/KsepRegistryQueryDriverShims_function_00959524.md) at `0x009595A0`
- [KsepStringFree](../../page/95/KsepStringFree_function_0095A1B8.md) at `0x0095A1CF`
- [KsepRegistryOpenKey](../../page/95/KsepRegistryOpenKey_function_0095A79C.md) at `0x0095A827`
- [KsepCacheDeviceFree](../../page/95/KsepCacheDeviceFree_function_0095AD00.md) at `0x0095AD40`
- [KsepCacheDeviceFree](../../page/95/KsepCacheDeviceFree_function_0095AD00.md) at `0x0095AD48`
- [KsepCacheDeviceFree](../../page/95/KsepCacheDeviceFree_function_0095AD00.md) at `0x0095AD5B`
- [KsepDbQueryRegistryDeviceData](../../page/95/KsepDbQueryRegistryDeviceData_function_0095B174.md) at `0x0095B1CC`
- [KsepDbQueryRegistryDeviceData](../../page/95/KsepDbQueryRegistryDeviceData_function_0095B174.md) at `0x0095B240`
- [sub_00B26BF6](../../page/B2/Unknown_function_00B26BF6.md) at `0x00B26DB0`
- [sub_00B26BF6](../../page/B2/Unknown_function_00B26BF6.md) at `0x00B26E27`
- [sub_00B27464](../../page/B2/Unknown_function_00B27464.md) at `0x00B2752B`

### Static image references
- `0x004B0E23` → RVA `0x00F10164` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004B0E1E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B0E10  48 83 EC 28                     sub rsp, 0x28
004B0E14  48 85 C9                        test rcx, rcx
004B0E17  74 11                           je 0x1404b0e2a
004B0E19  BA 4B 53 45 61                  mov edx, 0x6145534b
004B0E1E  E8 4D 1A 6D 00                  call 0x140b82870
004B0E23  F0 FF 05 3A F3 A5 00            lock inc dword ptr [rip + 0xa5f33a]
004B0E2A  48 83 C4 28                     add rsp, 0x28
004B0E2E  C3                              ret
004B0E2F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepPoolFreePaged(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) {
        a2 = 0x6145534BULL;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepPoolFreePaged(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) {
        a2 = 0x6145534BULL;
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B0E10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B0E10[BB_004B0E10]
  bb_004B0E19[BB_004B0E19]
  bb_004B0E2A[BB_004B0E2A]
  bb_004B0E2F[BB_004B0E2F]
  bb_004B0E10 -->|branch| bb_004B0E2A
  bb_004B0E10 -->|fallthrough| bb_004B0E19
  bb_004B0E19 -->|flow| bb_004B0E2A
```
