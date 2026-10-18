# Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0054EB38`–`0x0054EB6A` (길이 `50` bytes)
- VA: `0x000000014054EB38`
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
- `0x0054EB5F` → [Feature_DmaAdapterStage1DirectAttach__private_IsEnabledFallback](Feature_DmaAdapterStage1DirectAttach__private_IsEnabledFallback_function_0054EB70.md) (function, `0x0054EB70`)

### Direct callers
- [IommupDomainAttachPasidDevice](IommupDomainAttachPasidDevice_function_0054F984.md) at `0x0054F9FA`
- [IommupDomainAttachPasidDevice](IommupDomainAttachPasidDevice_function_0054F984.md) at `0x0054FAD0`
- [IommupDomainAttachPasidDevice](IommupDomainAttachPasidDevice_function_0054F984.md) at `0x0054FB87`
- [IommupDomainAttachPasidDevice](IommupDomainAttachPasidDevice_function_0054F984.md) at `0x0054FC60`
- [IommupDomainDetachPasidDevice](IommupDomainDetachPasidDevice_function_0054FD50.md) at `0x0054FE3E`
- [IommupPasidDeviceCreate](IommupPasidDeviceCreate_function_0054FEEC.md) at `0x0054FF3E`
- [IommuDomainAttachDeviceEx](../56/IommuDomainAttachDeviceEx_function_00567B60.md) at `0x00567BEF`

### Static image references
- `0x0054EB42` → RVA `0x00FC46A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054EB38  48 83 EC 28                     sub rsp, 0x28
0054EB3C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0054EB42  8B 05 58 5B A7 00               mov eax, dword ptr [rip + 0xa75b58]
0054EB48  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0054EB4C  A8 10                           test al, 0x10
0054EB4E  74 05                           je 0x14054eb55
0054EB50  83 E0 01                        and eax, 1
0054EB53  EB 0F                           jmp 0x14054eb64
0054EB55  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054EB5A  BA 03 00 00 00                  mov edx, 3
0054EB5F  E8 0C 00 00 00                  call 0x14054eb70
0054EB64  48 83 C4 28                     add rsp, 0x28
0054EB68  C3                              ret
0054EB69  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10967896)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10967896)))) & (16)) == 0) goto loc_0054EB55;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10967896))) & (1));
    goto loc_0054EB64;
loc_0054EB55:
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0054EB64:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_DmaAdapterStage1DirectAttach__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA75B58)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA75B58)))) & (16)) == 0) goto loc_0054EB55;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA75B58))) & (1));
    goto loc_0054EB64;
loc_0054EB55:
    result = Feature_DmaAdapterStage1DirectAttach__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0054EB64:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054EB38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054EB38[BB_0054EB38]
  bb_0054EB50[BB_0054EB50]
  bb_0054EB55[BB_0054EB55]
  bb_0054EB64[BB_0054EB64]
  bb_0054EB69[BB_0054EB69]
  bb_0054EB38 -->|branch| bb_0054EB55
  bb_0054EB38 -->|fallthrough| bb_0054EB50
  bb_0054EB50 -->|branch| bb_0054EB64
  bb_0054EB55 -->|flow| bb_0054EB64
```
