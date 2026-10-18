# Feature_2735186232__private_IsEnabledDeviceUsageNoInline

- RVA: `0x005CD914`–`0x005CD946` (길이 `50` bytes)
- VA: `0x00000001405CD914`
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
- `0x005CD93B` → [Feature_2735186232__private_IsEnabledFallback](Feature_2735186232__private_IsEnabledFallback_function_005CD94C.md) (function, `0x005CD94C`)

### Direct callers
- [ObpCreateSymbolicLinkName](../../page/74/ObpCreateSymbolicLinkName_function_0074EB80.md) at `0x0074ED3E`
- [ObpCreateSymbolicLinkName](../../page/74/ObpCreateSymbolicLinkName_function_0074EB80.md) at `0x0074EF51`

### Static image references
- `0x005CD91E` → RVA `0x00FC4A20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CD914  48 83 EC 28                     sub rsp, 0x28
005CD918  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005CD91E  8B 05 FC 70 9F 00               mov eax, dword ptr [rip + 0x9f70fc]
005CD924  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005CD928  A8 10                           test al, 0x10
005CD92A  74 05                           je 0x1405cd931
005CD92C  83 E0 01                        and eax, 1
005CD92F  EB 0F                           jmp 0x1405cd940
005CD931  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005CD936  BA 03 00 00 00                  mov edx, 3
005CD93B  E8 0C 00 00 00                  call 0x1405cd94c
005CD940  48 83 C4 28                     add rsp, 0x28
005CD944  C3                              ret
005CD945  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_2735186232__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10449148)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10449148)))) & (16)) == 0) goto loc_005CD931;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10449148))) & (1));
    goto loc_005CD940;
loc_005CD931:
    result = Feature_2735186232__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005CD940:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_2735186232__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9F70FC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9F70FC)))) & (16)) == 0) goto loc_005CD931;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9F70FC))) & (1));
    goto loc_005CD940;
loc_005CD931:
    result = Feature_2735186232__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005CD940:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CD914&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CD914[BB_005CD914]
  bb_005CD92C[BB_005CD92C]
  bb_005CD931[BB_005CD931]
  bb_005CD940[BB_005CD940]
  bb_005CD945[BB_005CD945]
  bb_005CD914 -->|branch| bb_005CD931
  bb_005CD914 -->|fallthrough| bb_005CD92C
  bb_005CD92C -->|branch| bb_005CD940
  bb_005CD931 -->|flow| bb_005CD940
```
