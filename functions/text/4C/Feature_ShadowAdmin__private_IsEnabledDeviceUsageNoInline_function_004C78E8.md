# Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004C78E8`–`0x004C791A` (길이 `50` bytes)
- VA: `0x00000001404C78E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004C7913` → [Feature_ShadowAdmin__private_IsEnabledFallback](../4F/Feature_ShadowAdmin__private_IsEnabledFallback_function_004FD1BC.md) (function, `0x004FD1BC`)

### Direct callers
- [SepMandatorySubProcessToken](SepMandatorySubProcessToken_function_004C0B88.md) at `0x004C0D3F`
- [SepCreateAppContainerToken](../4F/SepCreateAppContainerToken_function_004F43AC.md) at `0x004F4A75`
- [SepOneWayLinkLogonSessions](../60/SepOneWayLinkLogonSessions_function_006068D8.md) at `0x00606930`
- [SepLogonSystemManagedAdmin](../../page/70/SepLogonSystemManagedAdmin_function_00704DA4.md) at `0x00704DBE`
- [PsBootPhaseComplete](../../page/77/PsBootPhaseComplete_function_0077EA18.md) at `0x0077ECA4`
- [SeSubProcessToken](../../page/AA/SeSubProcessToken_function_00AAD570.md) at `0x00AAD7CE`
- [SeSubProcessToken](../../page/AA/SeSubProcessToken_function_00AAD570.md) at `0x00AADB3D`
- [NtCreateLowBoxToken](../../page/AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00ABA10A`
- [NtQueryInformationToken](../../page/AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AED5B7`
- [NtQueryInformationToken](../../page/AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE554`
- [NtQueryInformationToken](../../page/AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE5B7`
- [NtQueryInformationToken](../../page/AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE75F`
- [NtQueryInformationToken](../../page/AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE967`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF05EB`
- [SepDeReferenceLogonSession](../../page/AF/SepDeReferenceLogonSession_function_00AF25EC.md) at `0x00AF26B6`
- [sub_00B2884E](../../page/B2/Unknown_function_00B2884E.md) at `0x00B2884E`

### Static image references
- `0x004C78F2` → RVA `0x00FC4B30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C78E8  48 83 EC 28                     sub rsp, 0x28
004C78EC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004C78F2  8B 05 38 D2 AF 00               mov eax, dword ptr [rip + 0xafd238]
004C78F8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004C78FC  A8 10                           test al, 0x10
004C78FE  74 09                           je 0x1404c7909
004C7900  83 E0 01                        and eax, 1
004C7903  48 83 C4 28                     add rsp, 0x28
004C7907  C3                              ret
004C7908  CC                              int3
004C7909  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004C790E  BA 03 00 00 00                  mov edx, 3
004C7913  E8 A4 58 03 00                  call 0x1404fd1bc
004C7918  EB E9                           jmp 0x1404c7903
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11522616)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11522616)))) & (16)) == 0) goto loc_004C7909;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11522616))) & (1));
loc_004C7903:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004C7909:
    result = Feature_ShadowAdmin__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_004C7903;
}
```

## 5. (Beta) C Style

```c
void Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAFD238)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAFD238)))) & (16)) == 0) goto loc_004C7909;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAFD238))) & (1));
loc_004C7903:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004C7909:
    result = Feature_ShadowAdmin__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_004C7903;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C78E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C78E8[BB_004C78E8]
  bb_004C7900[BB_004C7900]
  bb_004C7903[BB_004C7903]
  bb_004C7908[BB_004C7908]
  bb_004C7909[BB_004C7909]
  bb_004C78E8 -->|branch| bb_004C7909
  bb_004C78E8 -->|fallthrough| bb_004C7900
  bb_004C7900 -->|flow| bb_004C7903
  bb_004C7908 -->|flow| bb_004C7909
  bb_004C7909 -->|branch| bb_004C7903
```
