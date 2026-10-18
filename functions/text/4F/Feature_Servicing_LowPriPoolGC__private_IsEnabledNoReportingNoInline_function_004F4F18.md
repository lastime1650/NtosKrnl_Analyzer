# Feature_Servicing_LowPriPoolGC__private_IsEnabledNoReportingNoInline

- RVA: `0x004F4F18`–`0x004F4F47` (길이 `47` bytes)
- VA: `0x00000001404F4F18`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F4F3C` → [Feature_Servicing_LowPriPoolGC__private_IsEnabledFallback](Feature_Servicing_LowPriPoolGC__private_IsEnabledFallback_function_004F4F50.md) (function, `0x004F4F50`)

### Direct callers
- [ExpHpGCTimerCallback](../3A/ExpHpGCTimerCallback_function_003A3040.md) at `0x003A3075`

### Static image references
- `0x004F4F22` → RVA `0x00FC4C40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F4F18  48 83 EC 28                     sub rsp, 0x28
004F4F1C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F4F22  8B 05 18 FD AC 00               mov eax, dword ptr [rip + 0xacfd18]
004F4F28  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F4F2C  A8 02                           test al, 2
004F4F2E  74 05                           je 0x1404f4f35
004F4F30  83 E0 01                        and eax, 1
004F4F33  EB 0C                           jmp 0x1404f4f41
004F4F35  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F4F3A  33 D2                           xor edx, edx
004F4F3C  E8 0F 00 00 00                  call 0x1404f4f50
004F4F41  48 83 C4 28                     add rsp, 0x28
004F4F45  C3                              ret
004F4F46  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_LowPriPoolGC__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11336984)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11336984)))) & (2)) == 0) goto loc_004F4F35;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11336984))) & (1));
    goto loc_004F4F41;
loc_004F4F35:
    a2 = 0;
    result = Feature_Servicing_LowPriPoolGC__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_004F4F41:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Servicing_LowPriPoolGC__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACFD18)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACFD18)))) & (2)) == 0) goto loc_004F4F35;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACFD18))) & (1));
    goto loc_004F4F41;
loc_004F4F35:
    Arg2 = 0;
    result = Feature_Servicing_LowPriPoolGC__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_004F4F41:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F4F18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F4F18[BB_004F4F18]
  bb_004F4F30[BB_004F4F30]
  bb_004F4F35[BB_004F4F35]
  bb_004F4F41[BB_004F4F41]
  bb_004F4F46[BB_004F4F46]
  bb_004F4F18 -->|branch| bb_004F4F35
  bb_004F4F18 -->|fallthrough| bb_004F4F30
  bb_004F4F30 -->|branch| bb_004F4F41
  bb_004F4F35 -->|flow| bb_004F4F41
```
