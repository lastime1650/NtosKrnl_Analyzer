# Feature_SdbValidateRootTagsOnOpen__private_IsEnabledDeviceUsageNoInline

- RVA: `0x00494B18`–`0x00494B4A` (길이 `50` bytes)
- VA: `0x0000000140494B18`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00494B43` → [Feature_SdbValidateRootTagsOnOpen__private_IsEnabledFallback](../69/Feature_SdbValidateRootTagsOnOpen__private_IsEnabledFallback_function_0069C044.md) (function, `0x0069C044`)

### Direct callers
- [SdbpOpenDatabaseInMemory](../../page/95/SdbpOpenDatabaseInMemory_function_0095A574.md) at `0x0095A633`
- [SdbpOpenDatabaseInMemory](../../page/95/SdbpOpenDatabaseInMemory_function_0095A574.md) at `0x0095A6A6`
- [SdbpGetNextTagId](../../page/95/SdbpGetNextTagId_function_0095D740.md) at `0x0095D7DE`
- [SdbGetTagDataSize](../../page/95/SdbGetTagDataSize_function_0095E230.md) at `0x0095E25A`
- [SdbGetNextChild](../../page/95/SdbGetNextChild_function_0095E520.md) at `0x0095E563`
- [SdbGetNextChild](../../page/95/SdbGetNextChild_function_0095E520.md) at `0x0095E57F`
- [SdbGetFirstChild](../../page/95/SdbGetFirstChild_function_0095E610.md) at `0x0095E64B`
- [SdbpGetTagHeadSize](../../page/95/SdbpGetTagHeadSize_function_0095E6B0.md) at `0x0095E6CF`
- [SdbpValidateAndApplyCompatFlags](../../page/AF/SdbpValidateAndApplyCompatFlags_function_00AF93D8.md) at `0x00AF947C`

### Static image references
- `0x00494B22` → RVA `0x00FC4E20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00494B18  48 83 EC 28                     sub rsp, 0x28
00494B1C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00494B22  8B 05 F8 02 B3 00               mov eax, dword ptr [rip + 0xb302f8]
00494B28  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00494B2C  A8 10                           test al, 0x10
00494B2E  74 09                           je 0x140494b39
00494B30  83 E0 01                        and eax, 1
00494B33  48 83 C4 28                     add rsp, 0x28
00494B37  C3                              ret
00494B38  CC                              int3
00494B39  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00494B3E  BA 03 00 00 00                  mov edx, 3
00494B43  E8 FC 74 20 00                  call 0x14069c044
00494B48  EB E9                           jmp 0x140494b33
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_SdbValidateRootTagsOnOpen__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11731704)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11731704)))) & (16)) == 0) goto loc_00494B39;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11731704))) & (1));
loc_00494B33:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00494B39:
    result = Feature_SdbValidateRootTagsOnOpen__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_00494B33;
}
```

## 5. (Beta) C Style

```c
void Feature_SdbValidateRootTagsOnOpen__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB302F8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB302F8)))) & (16)) == 0) goto loc_00494B39;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB302F8))) & (1));
loc_00494B33:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00494B39:
    result = Feature_SdbValidateRootTagsOnOpen__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_00494B33;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00494B18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00494B18[BB_00494B18]
  bb_00494B30[BB_00494B30]
  bb_00494B33[BB_00494B33]
  bb_00494B38[BB_00494B38]
  bb_00494B39[BB_00494B39]
  bb_00494B18 -->|branch| bb_00494B39
  bb_00494B18 -->|fallthrough| bb_00494B30
  bb_00494B30 -->|flow| bb_00494B33
  bb_00494B38 -->|flow| bb_00494B39
  bb_00494B39 -->|branch| bb_00494B33
```
