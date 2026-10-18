# Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004B7A58`–`0x004B7A8A` (길이 `50` bytes)
- VA: `0x00000001404B7A58`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B7A83` → [Feature_ForegroundBoost_ApiRemoval__private_IsEnabledFallback](../5E/Feature_ForegroundBoost_ApiRemoval__private_IsEnabledFallback_function_005E31F4.md) (function, `0x005E31F4`)

### Direct callers
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5A7A`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5C16`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5D4D`

### Static image references
- `0x004B7A62` → RVA `0x00FC4818` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B7A58  48 83 EC 28                     sub rsp, 0x28
004B7A5C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004B7A62  8B 05 B0 CD B0 00               mov eax, dword ptr [rip + 0xb0cdb0]
004B7A68  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004B7A6C  A8 10                           test al, 0x10
004B7A6E  74 09                           je 0x1404b7a79
004B7A70  83 E0 01                        and eax, 1
004B7A73  48 83 C4 28                     add rsp, 0x28
004B7A77  C3                              ret
004B7A78  CC                              int3
004B7A79  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004B7A7E  BA 03 00 00 00                  mov edx, 3
004B7A83  E8 6C B7 12 00                  call 0x1405e31f4
004B7A88  EB E9                           jmp 0x1404b7a73
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11586992)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11586992)))) & (16)) == 0) goto loc_004B7A79;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11586992))) & (1));
loc_004B7A73:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004B7A79:
    result = Feature_ForegroundBoost_ApiRemoval__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_004B7A73;
}
```

## 5. (Beta) C Style

```c
void Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0CDB0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0CDB0)))) & (16)) == 0) goto loc_004B7A79;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB0CDB0))) & (1));
loc_004B7A73:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004B7A79:
    result = Feature_ForegroundBoost_ApiRemoval__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_004B7A73;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B7A58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B7A58[BB_004B7A58]
  bb_004B7A70[BB_004B7A70]
  bb_004B7A73[BB_004B7A73]
  bb_004B7A78[BB_004B7A78]
  bb_004B7A79[BB_004B7A79]
  bb_004B7A58 -->|branch| bb_004B7A79
  bb_004B7A58 -->|fallthrough| bb_004B7A70
  bb_004B7A70 -->|flow| bb_004B7A73
  bb_004B7A78 -->|flow| bb_004B7A79
  bb_004B7A79 -->|branch| bb_004B7A73
```
