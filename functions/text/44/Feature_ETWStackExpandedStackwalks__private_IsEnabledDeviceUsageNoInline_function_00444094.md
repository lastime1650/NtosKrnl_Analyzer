# Feature_ETWStackExpandedStackwalks__private_IsEnabledDeviceUsageNoInline

- RVA: `0x00444094`–`0x004440C6` (길이 `50` bytes)
- VA: `0x0000000140444094`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004440BF` → [Feature_ETWStackExpandedStackwalks__private_IsEnabledFallback](../4F/Feature_ETWStackExpandedStackwalks__private_IsEnabledFallback_function_004FD184.md) (function, `0x004FD184`)

### Direct callers
- [sub_002F8E26](../2F/Unknown_function_002F8E26.md) at `0x002F8EA2`
- [sub_002F90AE](../2F/Unknown_function_002F90AE.md) at `0x002F9142`
- [EtwpExpandStackAndWalkFrameChain](EtwpExpandStackAndWalkFrameChain_function_00443F80.md) at `0x00443FBE`

### Static image references
- `0x0044409E` → RVA `0x00FC4BF8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00444094  48 83 EC 28                     sub rsp, 0x28
00444098  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0044409E  8B 05 54 0B B8 00               mov eax, dword ptr [rip + 0xb80b54]
004440A4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004440A8  A8 10                           test al, 0x10
004440AA  74 09                           je 0x1404440b5
004440AC  83 E0 01                        and eax, 1
004440AF  48 83 C4 28                     add rsp, 0x28
004440B3  C3                              ret
004440B4  CC                              int3
004440B5  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004440BA  BA 03 00 00 00                  mov edx, 3
004440BF  E8 C0 90 0B 00                  call 0x1404fd184
004440C4  EB E9                           jmp 0x1404440af
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ETWStackExpandedStackwalks__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12061524)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12061524)))) & (16)) == 0) goto loc_004440B5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12061524))) & (1));
loc_004440AF:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004440B5:
    result = Feature_ETWStackExpandedStackwalks__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_004440AF;
}
```

## 5. (Beta) C Style

```c
void Feature_ETWStackExpandedStackwalks__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB80B54)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB80B54)))) & (16)) == 0) goto loc_004440B5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB80B54))) & (1));
loc_004440AF:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004440B5:
    result = Feature_ETWStackExpandedStackwalks__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_004440AF;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00444094&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00444094[BB_00444094]
  bb_004440AC[BB_004440AC]
  bb_004440AF[BB_004440AF]
  bb_004440B4[BB_004440B4]
  bb_004440B5[BB_004440B5]
  bb_00444094 -->|branch| bb_004440B5
  bb_00444094 -->|fallthrough| bb_004440AC
  bb_004440AC -->|flow| bb_004440AF
  bb_004440B4 -->|flow| bb_004440B5
  bb_004440B5 -->|branch| bb_004440AF
```
