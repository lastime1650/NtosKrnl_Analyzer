# KsepPoolAllocatePaged

- RVA: `0x004A9EFC`–`0x004A9F50` (길이 `84` bytes)
- VA: `0x00000001404A9EFC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `24`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **22**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004A9F17` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004A9F33` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [KsepEvntLogShimsApplied](../5C/KsepEvntLogShimsApplied_function_005CBBE4.md) at `0x005CBC6F`
- [KsepEvntLogShimsApplied](../5C/KsepEvntLogShimsApplied_function_005CBBE4.md) at `0x005CBD00`
- [KsepDbGetShimInfo](../../page/74/KsepDbGetShimInfo_function_00748E94.md) at `0x00748EEC`
- [KsepDbQueryRegistryDeviceDataList](../../page/74/KsepDbQueryRegistryDeviceDataList_function_007490B4.md) at `0x0074914C`
- [KsepDbQueryRegistryDeviceDataList](../../page/74/KsepDbQueryRegistryDeviceDataList_function_007490B4.md) at `0x00749167`
- [KseRegisterShimEx](../../page/74/KseRegisterShimEx_function_007494D0.md) at `0x007495BF`
- [KsepSdbBootInitialize](../../page/74/KsepSdbBootInitialize_function_0074A7EC.md) at `0x0074A80E`
- [KsepGetLoadedModulesList](../../page/74/KsepGetLoadedModulesList_function_0074A960.md) at `0x0074A98E`
- [KsepStringSplitMultiString](../../page/74/KsepStringSplitMultiString_function_0074AB48.md) at `0x0074AC42`
- [KsepCacheDeviceInsertData](../../page/74/KsepCacheDeviceInsertData_function_0074AD9C.md) at `0x0074ADC5`
- [KsepCacheDeviceInsertData](../../page/74/KsepCacheDeviceInsertData_function_0074AD9C.md) at `0x0074ADF1`
- [KsepCacheInitialize](../../page/74/KsepCacheInitialize_function_0074AE7C.md) at `0x0074AE9E`
- [KsepCacheInitialize](../../page/74/KsepCacheInitialize_function_0074AE7C.md) at `0x0074AED5`
- [KsepRegistryEnumValue](../../page/74/KsepRegistryEnumValue_function_0074B24C.md) at `0x0074B2A3`
- [KsepRegistryQueryKeyInformation](../../page/74/KsepRegistryQueryKeyInformation_function_0074B498.md) at `0x0074B4EC`
- [KsepRegistryQuerySZ](../../page/74/KsepRegistryQuerySZ_function_0074B58C.md) at `0x0074B755`
- [KsepRegistryQueryValue](../../page/74/KsepRegistryQueryValue_function_0074B7F8.md) at `0x0074B9C1`
- [KsepGetShimsForDriver](../../page/95/KsepGetShimsForDriver_function_00958A78.md) at `0x00958B8A`
- [KsepStringDuplicateUnicode](../../page/95/KsepStringDuplicateUnicode_function_00958D78.md) at `0x00958DAF`
- [KsepEngineGetShimsFromRegistry](../../page/95/KsepEngineGetShimsFromRegistry_function_0095907C.md) at `0x009590BE`
- [KsepEngineGetShimsFromRegistry](../../page/95/KsepEngineGetShimsFromRegistry_function_0095907C.md) at `0x0095914D`
- [KseAddHardwareId](../../page/95/KseAddHardwareId_function_00959254.md) at `0x009592ED`
- [KsepDbGetDriverShimsInternal](../../page/95/KsepDbGetDriverShimsInternal_function_009597C4.md) at `0x009598A4`
- [KsepStringConcatenate](../../page/95/KsepStringConcatenate_function_0095A8A0.md) at `0x0095A966`
- [KsepDbCacheReadDevice](../../page/95/KsepDbCacheReadDevice_function_0095AAC8.md) at `0x0095AAEF`
- [KsepStringDuplicate](../../page/95/KsepStringDuplicate_function_0095B454.md) at `0x0095B4C9`
- [sub_00B2755C](../../page/B2/Unknown_function_00B2755C.md) at `0x00B27577`

### Static image references
- `0x004A9F24` → RVA `0x00F10160` (`.data`; read/write)
- `0x004A9F47` → RVA `0x00F10170` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004A9F17` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A9EFC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004A9F01  57                              push rdi
004A9F02  48 83 EC 20                     sub rsp, 0x20
004A9F06  48 8B F9                        mov rdi, rcx
004A9F09  48 8B D1                        mov rdx, rcx
004A9F0C  B9 00 01 00 00                  mov ecx, 0x100
004A9F11  41 B8 4B 53 45 61               mov r8d, 0x6145534b
004A9F17  E8 D4 81 6D 00                  call 0x140b820f0
004A9F1C  48 8B D8                        mov rbx, rax
004A9F1F  48 85 C0                        test rax, rax
004A9F22  74 23                           je 0x1404a9f47
004A9F24  F0 FF 05 35 62 A6 00            lock inc dword ptr [rip + 0xa66235]
004A9F2B  4C 8B C7                        mov r8, rdi
004A9F2E  33 D2                           xor edx, edx
004A9F30  48 8B C8                        mov rcx, rax
004A9F33  E8 08 CD 21 00                  call 0x1406c6c40
004A9F38  48 8B C3                        mov rax, rbx
004A9F3B  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004A9F40  48 83 C4 20                     add rsp, 0x20
004A9F44  5F                              pop rdi
004A9F45  C3                              ret
004A9F46  CC                              int3
004A9F47  F0 FF 05 22 62 A6 00            lock inc dword ptr [rip + 0xa66222]
004A9F4E  EB E8                           jmp 0x1404a9f38
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepPoolAllocatePaged(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(256, a1, (unsigned int)(0x6145534BULL), a4);
    if (result == 0) goto loc_004A9F47;
    a2 = 0;
    result = memset(result, a2, a1, a4);
loc_004A9F38:
    v_rsp = (v_rsp) + (32);
    return result;
loc_004A9F47:
    goto loc_004A9F38;
}
```

## 5. (Beta) C Style

```c
int64_t KsepPoolAllocatePaged(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(256, Arg1, (uint32_t)(0x6145534BULL), a4);
    if (result == 0) goto loc_004A9F47;
    a2 = 0;
    result = memset(result, a2, Arg1, a4);
loc_004A9F38:
    local_rsp = (local_rsp) + (32);
    return result;
loc_004A9F47:
    goto loc_004A9F38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A9EFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A9EFC[BB_004A9EFC]
  bb_004A9F24[BB_004A9F24]
  bb_004A9F38[BB_004A9F38]
  bb_004A9F46[BB_004A9F46]
  bb_004A9F47[BB_004A9F47]
  bb_004A9EFC -->|branch| bb_004A9F47
  bb_004A9EFC -->|fallthrough| bb_004A9F24
  bb_004A9F24 -->|flow| bb_004A9F38
  bb_004A9F46 -->|flow| bb_004A9F47
  bb_004A9F47 -->|branch| bb_004A9F38
```
