# Feature_2327208251__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0064E4B4`–`0x0064E4E6` (길이 `50` bytes)
- VA: `0x000000014064E4B4`
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
- `0x0064E4DB` → [Feature_2327208251__private_IsEnabledFallback](Feature_2327208251__private_IsEnabledFallback_function_0064E4EC.md) (function, `0x0064E4EC`)

### Direct callers
- [WmipReceiveNotifications](../4E/WmipReceiveNotifications_function_004EC280.md) at `0x004EC446`
- [WmipReceiveNotifications](../4E/WmipReceiveNotifications_function_004EC280.md) at `0x004EC4AB`
- [WmipReceiveNotifications](../4E/WmipReceiveNotifications_function_004EC280.md) at `0x004EC519`
- [WmipQuerySingleMultiple](../../page/7B/WmipQuerySingleMultiple_function_007B36F0.md) at `0x007B37A1`
- [WmipQuerySingleMultiple](../../page/7B/WmipQuerySingleMultiple_function_007B36F0.md) at `0x007B3A97`
- [WmipQuerySingleMultiple](../../page/7B/WmipQuerySingleMultiple_function_007B36F0.md) at `0x007B3ADF`
- [WmipQuerySingleMultiple](../../page/7B/WmipQuerySingleMultiple_function_007B36F0.md) at `0x007B3B45`
- [WmipQuerySingleMultiple](../../page/7B/WmipQuerySingleMultiple_function_007B36F0.md) at `0x007B3C2C`
- [WmipQueryAllDataMultiple](../../page/9D/WmipQueryAllDataMultiple_function_009DF11C.md) at `0x009DF1A9`
- [WmipQueryAllDataMultiple](../../page/9D/WmipQueryAllDataMultiple_function_009DF11C.md) at `0x009DF32F`
- [WmipQueryAllDataMultiple](../../page/9D/WmipQueryAllDataMultiple_function_009DF11C.md) at `0x009DF3BD`
- [WmipQueryAllDataMultiple](../../page/9D/WmipQueryAllDataMultiple_function_009DF11C.md) at `0x009DF403`
- [WmipQueryAllDataMultiple](../../page/9D/WmipQueryAllDataMultiple_function_009DF11C.md) at `0x009DF440`

### Static image references
- `0x0064E4BE` → RVA `0x00FC4BC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064E4B4  48 83 EC 28                     sub rsp, 0x28
0064E4B8  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0064E4BE  8B 05 FC 66 97 00               mov eax, dword ptr [rip + 0x9766fc]
0064E4C4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0064E4C8  A8 10                           test al, 0x10
0064E4CA  74 05                           je 0x14064e4d1
0064E4CC  83 E0 01                        and eax, 1
0064E4CF  EB 0F                           jmp 0x14064e4e0
0064E4D1  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0064E4D6  BA 03 00 00 00                  mov edx, 3
0064E4DB  E8 0C 00 00 00                  call 0x14064e4ec
0064E4E0  48 83 C4 28                     add rsp, 0x28
0064E4E4  C3                              ret
0064E4E5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_2327208251__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9922300)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9922300)))) & (16)) == 0) goto loc_0064E4D1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9922300))) & (1));
    goto loc_0064E4E0;
loc_0064E4D1:
    result = Feature_2327208251__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0064E4E0:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_2327208251__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9766FC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9766FC)))) & (16)) == 0) goto loc_0064E4D1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9766FC))) & (1));
    goto loc_0064E4E0;
loc_0064E4D1:
    result = Feature_2327208251__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0064E4E0:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064E4B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064E4B4[BB_0064E4B4]
  bb_0064E4CC[BB_0064E4CC]
  bb_0064E4D1[BB_0064E4D1]
  bb_0064E4E0[BB_0064E4E0]
  bb_0064E4E5[BB_0064E4E5]
  bb_0064E4B4 -->|branch| bb_0064E4D1
  bb_0064E4B4 -->|fallthrough| bb_0064E4CC
  bb_0064E4CC -->|branch| bb_0064E4E0
  bb_0064E4D1 -->|flow| bb_0064E4E0
```
