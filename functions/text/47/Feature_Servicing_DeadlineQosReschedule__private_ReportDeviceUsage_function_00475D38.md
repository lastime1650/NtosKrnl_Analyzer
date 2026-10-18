# Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage

- RVA: `0x00475D38`–`0x00475D67` (길이 `47` bytes)
- VA: `0x0000000140475D38`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `13`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00475D60` → [Feature_Servicing_DeadlineQosReschedule__private_ReportUsageFallback](../5C/Feature_Servicing_DeadlineQosReschedule__private_ReportUsageFallback_function_005C350C.md) (function, `0x005C350C`)

### Direct callers
- [KeUpdateThreadTag](KeUpdateThreadTag_function_00475770.md) at `0x00475913`
- [KeUpdateThreadTag](KeUpdateThreadTag_function_00475770.md) at `0x0047592A`
- [KeUpdateThreadTag](KeUpdateThreadTag_function_00475770.md) at `0x00475A8E`
- [KeUpdateThreadTag](KeUpdateThreadTag_function_00475770.md) at `0x00475ABE`

### Static image references
- `0x00475D42` → RVA `0x00FC49E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00475D38  48 83 EC 28                     sub rsp, 0x28
00475D3C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00475D42  8B 05 A0 EC B4 00               mov eax, dword ptr [rip + 0xb4eca0]
00475D48  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00475D4C  A8 10                           test al, 0x10
00475D4E  74 06                           je 0x140475d56
00475D50  48 83 C4 28                     add rsp, 0x28
00475D54  C3                              ret
00475D55  CC                              int3
00475D56  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00475D5B  BA 03 00 00 00                  mov edx, 3
00475D60  E8 A7 D7 14 00                  call 0x1405c350c
00475D65  EB E9                           jmp 0x140475d50
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11857056)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11857056)))) & (16)) == 0) goto loc_00475D56;
loc_00475D50:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(v_rip + 11857056));
loc_00475D56:
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportUsageFallback(v_stack_p30, 3, a3, a4);
    goto loc_00475D50;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_DeadlineQosReschedule__private_ReportDeviceUsage(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB4ECA0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB4ECA0)))) & (16)) == 0) goto loc_00475D56;
loc_00475D50:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(v_rip + 0xB4ECA0));
loc_00475D56:
    result = Feature_Servicing_DeadlineQosReschedule__private_ReportUsageFallback(v_stack_p30, 3, a3, a4);
    goto loc_00475D50;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00475D38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00475D38[BB_00475D38]
  bb_00475D50[BB_00475D50]
  bb_00475D55[BB_00475D55]
  bb_00475D56[BB_00475D56]
  bb_00475D38 -->|branch| bb_00475D56
  bb_00475D38 -->|fallthrough| bb_00475D50
  bb_00475D55 -->|flow| bb_00475D56
  bb_00475D56 -->|branch| bb_00475D50
```
