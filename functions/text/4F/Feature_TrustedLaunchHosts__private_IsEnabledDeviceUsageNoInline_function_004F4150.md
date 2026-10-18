# Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F4150`–`0x004F4182` (길이 `50` bytes)
- VA: `0x00000001404F4150`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F4177` → [Feature_TrustedLaunchHosts__private_IsEnabledFallback](../5E/Feature_TrustedLaunchHosts__private_IsEnabledFallback_function_005E3468.md) (function, `0x005E3468`)

### Direct callers
- [SepVerifyDesktopAppxImage](../60/SepVerifyDesktopAppxImage_function_0060885C.md) at `0x006088BD`
- [SepVerifyDesktopAppxImage](../60/SepVerifyDesktopAppxImage_function_0060885C.md) at `0x00608A48`
- [MiInitializeCreateSectionPacket](../../page/98/MiInitializeCreateSectionPacket_function_00984130.md) at `0x009842D5`
- [MiCreateNewSection](../../page/98/MiCreateNewSection_function_00985DB0.md) at `0x009860E8`
- [MiValidateExistingImage](../../page/98/MiValidateExistingImage_function_009864B4.md) at `0x0098661E`
- [MmCreateSpecialImageSection](../../page/AB/MmCreateSpecialImageSection_function_00AB7360.md) at `0x00AB73C4`
- [NtCreateUserProcess](../../page/AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEADA4`

### Static image references
- `0x004F415A` → RVA `0x00FC4A98` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F4150  48 83 EC 28                     sub rsp, 0x28
004F4154  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F415A  8B 05 38 09 AD 00               mov eax, dword ptr [rip + 0xad0938]
004F4160  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F4164  A8 10                           test al, 0x10
004F4166  74 05                           je 0x1404f416d
004F4168  83 E0 01                        and eax, 1
004F416B  EB 0F                           jmp 0x1404f417c
004F416D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F4172  BA 03 00 00 00                  mov edx, 3
004F4177  E8 EC F2 0E 00                  call 0x1405e3468
004F417C  48 83 C4 28                     add rsp, 0x28
004F4180  C3                              ret
004F4181  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11340088)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11340088)))) & (16)) == 0) goto loc_004F416D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11340088))) & (1));
    goto loc_004F417C;
loc_004F416D:
    result = Feature_TrustedLaunchHosts__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F417C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD0938)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD0938)))) & (16)) == 0) goto loc_004F416D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAD0938))) & (1));
    goto loc_004F417C;
loc_004F416D:
    result = Feature_TrustedLaunchHosts__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F417C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F4150&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F4150[BB_004F4150]
  bb_004F4168[BB_004F4168]
  bb_004F416D[BB_004F416D]
  bb_004F417C[BB_004F417C]
  bb_004F4181[BB_004F4181]
  bb_004F4150 -->|branch| bb_004F416D
  bb_004F4150 -->|fallthrough| bb_004F4168
  bb_004F4168 -->|branch| bb_004F417C
  bb_004F416D -->|flow| bb_004F417C
```
