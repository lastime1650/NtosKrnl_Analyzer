# Feature_DriverSetup_ReofferFingerprinting_v2__private_IsEnabledDeviceUsageNoInline

- RVA: `0x006648C4`–`0x006648F6` (길이 `50` bytes)
- VA: `0x00000001406648C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006648EB` → [Feature_DriverSetup_ReofferFingerprinting_v2__private_IsEnabledFallback](Feature_DriverSetup_ReofferFingerprinting_v2__private_IsEnabledFallback_function_006648FC.md) (function, `0x006648FC`)

### Direct callers
- [IsFeatureEnabled](IsFeatureEnabled_function_006649C0.md) at `0x006649EE`

### Static image references
- `0x006648CE` → RVA `0x00FC4C60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006648C4  48 83 EC 28                     sub rsp, 0x28
006648C8  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
006648CE  8B 05 8C 03 96 00               mov eax, dword ptr [rip + 0x96038c]
006648D4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006648D8  A8 10                           test al, 0x10
006648DA  74 05                           je 0x1406648e1
006648DC  83 E0 01                        and eax, 1
006648DF  EB 0F                           jmp 0x1406648f0
006648E1  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
006648E6  BA 03 00 00 00                  mov edx, 3
006648EB  E8 0C 00 00 00                  call 0x1406648fc
006648F0  48 83 C4 28                     add rsp, 0x28
006648F4  C3                              ret
006648F5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_DriverSetup_ReofferFingerprinting_v2__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9831308)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9831308)))) & (16)) == 0) goto loc_006648E1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9831308))) & (1));
    goto loc_006648F0;
loc_006648E1:
    result = Feature_DriverSetup_ReofferFingerprinting_v2__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_006648F0:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_DriverSetup_ReofferFingerprinting_v2__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96038C)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96038C)))) & (16)) == 0) goto loc_006648E1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x96038C))) & (1));
    goto loc_006648F0;
loc_006648E1:
    result = Feature_DriverSetup_ReofferFingerprinting_v2__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_006648F0:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006648C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006648C4[BB_006648C4]
  bb_006648DC[BB_006648DC]
  bb_006648E1[BB_006648E1]
  bb_006648F0[BB_006648F0]
  bb_006648F5[BB_006648F5]
  bb_006648C4 -->|branch| bb_006648E1
  bb_006648C4 -->|fallthrough| bb_006648DC
  bb_006648DC -->|branch| bb_006648F0
  bb_006648E1 -->|flow| bb_006648F0
```
