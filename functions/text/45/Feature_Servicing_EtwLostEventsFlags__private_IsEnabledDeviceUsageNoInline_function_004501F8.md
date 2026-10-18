# Feature_Servicing_EtwLostEventsFlags__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004501F8`–`0x0045022A` (길이 `50` bytes)
- VA: `0x00000001404501F8`
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
- `0x00450223` → [Feature_Servicing_EtwLostEventsFlags__private_IsEnabledFallback](../4F/Feature_Servicing_EtwLostEventsFlags__private_IsEnabledFallback_function_004FD1A0.md) (function, `0x004FD1A0`)

### Direct callers
- [EtwpEventWriteFull](../22/EtwpEventWriteFull_function_00225C10.md) at `0x00226894`

### Static image references
- `0x00450202` → RVA `0x00FC4BE8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004501F8  48 83 EC 28                     sub rsp, 0x28
004501FC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00450202  8B 05 E0 49 B7 00               mov eax, dword ptr [rip + 0xb749e0]
00450208  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0045020C  A8 10                           test al, 0x10
0045020E  74 09                           je 0x140450219
00450210  83 E0 01                        and eax, 1
00450213  48 83 C4 28                     add rsp, 0x28
00450217  C3                              ret
00450218  CC                              int3
00450219  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0045021E  BA 03 00 00 00                  mov edx, 3
00450223  E8 78 CF 0A 00                  call 0x1404fd1a0
00450228  EB E9                           jmp 0x140450213
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_EtwLostEventsFlags__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12012000)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12012000)))) & (16)) == 0) goto loc_00450219;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12012000))) & (1));
loc_00450213:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00450219:
    result = Feature_Servicing_EtwLostEventsFlags__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_00450213;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_EtwLostEventsFlags__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB749E0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB749E0)))) & (16)) == 0) goto loc_00450219;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB749E0))) & (1));
loc_00450213:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00450219:
    result = Feature_Servicing_EtwLostEventsFlags__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_00450213;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004501F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004501F8[BB_004501F8]
  bb_00450210[BB_00450210]
  bb_00450213[BB_00450213]
  bb_00450218[BB_00450218]
  bb_00450219[BB_00450219]
  bb_004501F8 -->|branch| bb_00450219
  bb_004501F8 -->|fallthrough| bb_00450210
  bb_00450210 -->|flow| bb_00450213
  bb_00450218 -->|flow| bb_00450219
  bb_00450219 -->|branch| bb_00450213
```
