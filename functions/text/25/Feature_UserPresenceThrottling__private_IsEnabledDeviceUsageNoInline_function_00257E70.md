# Feature_UserPresenceThrottling__private_IsEnabledDeviceUsageNoInline

- RVA: `0x00257E70`–`0x00257EA5` (길이 `53` bytes)
- VA: `0x0000000140257E70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `14`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00257E9E` → [Feature_UserPresenceThrottling__private_IsEnabledFallback](../4F/Feature_UserPresenceThrottling__private_IsEnabledFallback_function_004FD210.md) (function, `0x004FD210`)

### Direct callers
- [sub_00258083](Unknown_function_00258083.md) at `0x00258094`
- [PspSetProcessPpmPolicy](../../page/AE/PspSetProcessPpmPolicy_function_00AE34F0.md) at `0x00AE350D`

### Static image references
- `0x00257E74` → RVA `0x00FC49B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00257E70  48 83 EC 28                     sub rsp, 0x28
00257E74  8B 05 3E CB D6 00               mov eax, dword ptr [rip + 0xd6cb3e]
00257E7A  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
00257E83  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00257E87  A8 10                           test al, 0x10
00257E89  74 09                           je 0x140257e94
00257E8B  83 E0 01                        and eax, 1
00257E8E  48 83 C4 28                     add rsp, 0x28
00257E92  C3                              ret
00257E93  CC                              int3
00257E94  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00257E99  BA 03 00 00 00                  mov edx, 3
00257E9E  E8 6D 53 2A 00                  call 0x1404fd210
00257EA3  EB E9                           jmp 0x140257e8e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_UserPresenceThrottling__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = 0;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 14076734)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14076734)))) & (16)) == 0) goto loc_00257E94;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 14076734))) & (1));
loc_00257E8E:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00257E94:
    result = Feature_UserPresenceThrottling__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_00257E8E;
}
```

## 5. (Beta) C Style

```c
void Feature_UserPresenceThrottling__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = 0;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD6CB3E)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD6CB3E)))) & (16)) == 0) goto loc_00257E94;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xD6CB3E))) & (1));
loc_00257E8E:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00257E94:
    result = Feature_UserPresenceThrottling__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_00257E8E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00257E70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00257E70[BB_00257E70]
  bb_00257E8B[BB_00257E8B]
  bb_00257E8E[BB_00257E8E]
  bb_00257E93[BB_00257E93]
  bb_00257E94[BB_00257E94]
  bb_00257E70 -->|branch| bb_00257E94
  bb_00257E70 -->|fallthrough| bb_00257E8B
  bb_00257E8B -->|flow| bb_00257E8E
  bb_00257E93 -->|flow| bb_00257E94
  bb_00257E94 -->|branch| bb_00257E8E
```
