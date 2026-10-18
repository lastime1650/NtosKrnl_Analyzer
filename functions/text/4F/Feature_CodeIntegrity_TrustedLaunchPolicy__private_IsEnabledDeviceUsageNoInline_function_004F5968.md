# Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F5968`–`0x004F599A` (길이 `50` bytes)
- VA: `0x00000001404F5968`
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
- `0x004F598F` → [Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledFallback](Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledFallback_function_004F59A0.md) (function, `0x004F59A0`)

### Direct callers
- [SeQuerySigningPolicyWorker](../../page/A1/SeQuerySigningPolicyWorker_function_00A13788.md) at `0x00A137F2`
- [SeQuerySigningPolicyWorker](../../page/A1/SeQuerySigningPolicyWorker_function_00A13788.md) at `0x00A13910`
- [SeQuerySigningPolicyWorker](../../page/A1/SeQuerySigningPolicyWorker_function_00A13788.md) at `0x00A13AC1`

### Static image references
- `0x004F5972` → RVA `0x00FC4AA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F5968  48 83 EC 28                     sub rsp, 0x28
004F596C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F5972  8B 05 30 F1 AC 00               mov eax, dword ptr [rip + 0xacf130]
004F5978  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F597C  A8 10                           test al, 0x10
004F597E  74 05                           je 0x1404f5985
004F5980  83 E0 01                        and eax, 1
004F5983  EB 0F                           jmp 0x1404f5994
004F5985  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F598A  BA 03 00 00 00                  mov edx, 3
004F598F  E8 0C 00 00 00                  call 0x1404f59a0
004F5994  48 83 C4 28                     add rsp, 0x28
004F5998  C3                              ret
004F5999  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11333936)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11333936)))) & (16)) == 0) goto loc_004F5985;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11333936))) & (1));
    goto loc_004F5994;
loc_004F5985:
    result = Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5994:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACF130)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACF130)))) & (16)) == 0) goto loc_004F5985;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACF130))) & (1));
    goto loc_004F5994;
loc_004F5985:
    result = Feature_CodeIntegrity_TrustedLaunchPolicy__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5994:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F5968&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F5968[BB_004F5968]
  bb_004F5980[BB_004F5980]
  bb_004F5985[BB_004F5985]
  bb_004F5994[BB_004F5994]
  bb_004F5999[BB_004F5999]
  bb_004F5968 -->|branch| bb_004F5985
  bb_004F5968 -->|fallthrough| bb_004F5980
  bb_004F5980 -->|branch| bb_004F5994
  bb_004F5985 -->|flow| bb_004F5994
```
