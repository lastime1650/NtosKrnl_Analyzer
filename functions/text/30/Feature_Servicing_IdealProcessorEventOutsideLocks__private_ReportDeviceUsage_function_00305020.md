# Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportDeviceUsage

- RVA: `0x00305020`–`0x0030504F` (길이 `47` bytes)
- VA: `0x0000000140305020`
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
- `0x00305048` → [Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportUsageFallback](../5C/Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportUsageFallback_function_005C087C.md) (function, `0x005C087C`)

### Direct callers
- [KiUpdateGlobalCpuSetConfiguration](KiUpdateGlobalCpuSetConfiguration_function_00305AB8.md) at `0x00305AE5`

### Static image references
- `0x0030502A` → RVA `0x00FC49D8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00305020  48 83 EC 28                     sub rsp, 0x28
00305024  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0030502A  8B 05 A8 F9 CB 00               mov eax, dword ptr [rip + 0xcbf9a8]
00305030  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00305034  A8 10                           test al, 0x10
00305036  74 06                           je 0x14030503e
00305038  48 83 C4 28                     add rsp, 0x28
0030503C  C3                              ret
0030503D  CC                              int3
0030503E  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00305043  BA 03 00 00 00                  mov edx, 3
00305048  E8 2F B8 2B 00                  call 0x1405c087c
0030504D  EB E9                           jmp 0x140305038
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportDeviceUsage(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13367720)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13367720)))) & (16)) == 0) goto loc_0030503E;
loc_00305038:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(v_rip + 13367720));
loc_0030503E:
    result = Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportUsageFallback(v_stack_p30, 3, a3, a4);
    goto loc_00305038;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportDeviceUsage(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBF9A8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBF9A8)))) & (16)) == 0) goto loc_0030503E;
loc_00305038:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(v_rip + 0xCBF9A8));
loc_0030503E:
    result = Feature_Servicing_IdealProcessorEventOutsideLocks__private_ReportUsageFallback(v_stack_p30, 3, a3, a4);
    goto loc_00305038;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00305020&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00305020[BB_00305020]
  bb_00305038[BB_00305038]
  bb_0030503D[BB_0030503D]
  bb_0030503E[BB_0030503E]
  bb_00305020 -->|branch| bb_0030503E
  bb_00305020 -->|fallthrough| bb_00305038
  bb_0030503D -->|flow| bb_0030503E
  bb_0030503E -->|branch| bb_00305038
```
