# Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F5DA0`–`0x004F5DD2` (길이 `50` bytes)
- VA: `0x00000001404F5DA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F5DC7` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledFallback](Feature_Servicing_PDCAgentSessions__private_IsEnabledFallback_function_004F5DD8.md) (function, `0x004F5DD8`)

### Direct callers
- [PopSessionConnected](../../page/76/PopSessionConnected_function_0076BC74.md) at `0x0076BC8B`
- [PopSessionConnectionChange](../../page/76/PopSessionConnectionChange_function_0076BDEC.md) at `0x0076BE0D`
- [NtPowerInformation](../../page/95/NtPowerInformation_function_00955D80.md) at `0x0095738B`
- [NtPowerInformation](../../page/95/NtPowerInformation_function_00955D80.md) at `0x009573FE`
- [PopPowerInformationInternal](../../page/A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8B882`
- [PopPowerInformationInternal](../../page/A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8D312`
- [PopPowerInformationInternal](../../page/A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8D3EB`

### Static image references
- `0x004F5DAA` → RVA `0x00FC4700` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F5DA0  48 83 EC 28                     sub rsp, 0x28
004F5DA4  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F5DAA  8B 05 50 E9 AC 00               mov eax, dword ptr [rip + 0xace950]
004F5DB0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F5DB4  A8 10                           test al, 0x10
004F5DB6  74 05                           je 0x1404f5dbd
004F5DB8  83 E0 01                        and eax, 1
004F5DBB  EB 0F                           jmp 0x1404f5dcc
004F5DBD  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F5DC2  BA 03 00 00 00                  mov edx, 3
004F5DC7  E8 0C 00 00 00                  call 0x1404f5dd8
004F5DCC  48 83 C4 28                     add rsp, 0x28
004F5DD0  C3                              ret
004F5DD1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11331920)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11331920)))) & (16)) == 0) goto loc_004F5DBD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11331920))) & (1));
    goto loc_004F5DCC;
loc_004F5DBD:
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5DCC:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACE950)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACE950)))) & (16)) == 0) goto loc_004F5DBD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACE950))) & (1));
    goto loc_004F5DCC;
loc_004F5DBD:
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5DCC:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F5DA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F5DA0[BB_004F5DA0]
  bb_004F5DB8[BB_004F5DB8]
  bb_004F5DBD[BB_004F5DBD]
  bb_004F5DCC[BB_004F5DCC]
  bb_004F5DD1[BB_004F5DD1]
  bb_004F5DA0 -->|branch| bb_004F5DBD
  bb_004F5DA0 -->|fallthrough| bb_004F5DB8
  bb_004F5DB8 -->|branch| bb_004F5DCC
  bb_004F5DBD -->|flow| bb_004F5DCC
```
