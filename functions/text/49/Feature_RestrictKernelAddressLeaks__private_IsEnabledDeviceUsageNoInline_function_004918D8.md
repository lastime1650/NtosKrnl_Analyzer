# Feature_RestrictKernelAddressLeaks__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004918D8`–`0x0049190A` (길이 `50` bytes)
- VA: `0x00000001404918D8`
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
- `0x00491903` → [Feature_RestrictKernelAddressLeaks__private_IsEnabledFallback](../4F/Feature_RestrictKernelAddressLeaks__private_IsEnabledFallback_function_004FD168.md) (function, `0x004FD168`)

### Direct callers
- [ExIsRestrictedCaller](../../page/A2/ExIsRestrictedCaller_function_00A217E8.md) at `0x00A21826`

### Static image references
- `0x004918E2` → RVA `0x00FC4820` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004918D8  48 83 EC 28                     sub rsp, 0x28
004918DC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004918E2  8B 05 38 2F B3 00               mov eax, dword ptr [rip + 0xb32f38]
004918E8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004918EC  A8 10                           test al, 0x10
004918EE  74 09                           je 0x1404918f9
004918F0  83 E0 01                        and eax, 1
004918F3  48 83 C4 28                     add rsp, 0x28
004918F7  C3                              ret
004918F8  CC                              int3
004918F9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004918FE  BA 03 00 00 00                  mov edx, 3
00491903  E8 60 B8 06 00                  call 0x1404fd168
00491908  EB E9                           jmp 0x1404918f3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_RestrictKernelAddressLeaks__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11743032)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11743032)))) & (16)) == 0) goto loc_004918F9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11743032))) & (1));
loc_004918F3:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004918F9:
    result = Feature_RestrictKernelAddressLeaks__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_004918F3;
}
```

## 5. (Beta) C Style

```c
void Feature_RestrictKernelAddressLeaks__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB32F38)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB32F38)))) & (16)) == 0) goto loc_004918F9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB32F38))) & (1));
loc_004918F3:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004918F9:
    result = Feature_RestrictKernelAddressLeaks__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_004918F3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004918D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004918D8[BB_004918D8]
  bb_004918F0[BB_004918F0]
  bb_004918F3[BB_004918F3]
  bb_004918F8[BB_004918F8]
  bb_004918F9[BB_004918F9]
  bb_004918D8 -->|branch| bb_004918F9
  bb_004918D8 -->|fallthrough| bb_004918F0
  bb_004918F0 -->|flow| bb_004918F3
  bb_004918F8 -->|flow| bb_004918F9
  bb_004918F9 -->|branch| bb_004918F3
```
