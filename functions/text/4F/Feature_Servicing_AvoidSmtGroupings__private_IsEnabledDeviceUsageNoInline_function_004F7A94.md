# Feature_Servicing_AvoidSmtGroupings__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F7A94`–`0x004F7AC6` (길이 `50` bytes)
- VA: `0x00000001404F7A94`
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
- `0x004F7ABB` → [Feature_Servicing_AvoidSmtGroupings__private_IsEnabledFallback](Feature_Servicing_AvoidSmtGroupings__private_IsEnabledFallback_function_004F7ACC.md) (function, `0x004F7ACC`)

### Direct callers
- [KiInitializeVelocity](../../init/BE/KiInitializeVelocity_function_00BEEDB8.md) at `0x00BEEDF4`

### Static image references
- `0x004F7A9E` → RVA `0x00FC49A8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F7A94  48 83 EC 28                     sub rsp, 0x28
004F7A98  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F7A9E  8B 05 04 CF AC 00               mov eax, dword ptr [rip + 0xaccf04]
004F7AA4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F7AA8  A8 10                           test al, 0x10
004F7AAA  74 05                           je 0x1404f7ab1
004F7AAC  83 E0 01                        and eax, 1
004F7AAF  EB 0F                           jmp 0x1404f7ac0
004F7AB1  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F7AB6  BA 03 00 00 00                  mov edx, 3
004F7ABB  E8 0C 00 00 00                  call 0x1404f7acc
004F7AC0  48 83 C4 28                     add rsp, 0x28
004F7AC4  C3                              ret
004F7AC5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_AvoidSmtGroupings__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11325188)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11325188)))) & (16)) == 0) goto loc_004F7AB1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11325188))) & (1));
    goto loc_004F7AC0;
loc_004F7AB1:
    result = Feature_Servicing_AvoidSmtGroupings__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7AC0:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_AvoidSmtGroupings__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACCF04)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACCF04)))) & (16)) == 0) goto loc_004F7AB1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACCF04))) & (1));
    goto loc_004F7AC0;
loc_004F7AB1:
    result = Feature_Servicing_AvoidSmtGroupings__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7AC0:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F7A94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F7A94[BB_004F7A94]
  bb_004F7AAC[BB_004F7AAC]
  bb_004F7AB1[BB_004F7AB1]
  bb_004F7AC0[BB_004F7AC0]
  bb_004F7AC5[BB_004F7AC5]
  bb_004F7A94 -->|branch| bb_004F7AB1
  bb_004F7A94 -->|fallthrough| bb_004F7AAC
  bb_004F7AAC -->|branch| bb_004F7AC0
  bb_004F7AB1 -->|flow| bb_004F7AC0
```
