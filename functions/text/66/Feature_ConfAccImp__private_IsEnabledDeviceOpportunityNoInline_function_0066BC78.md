# Feature_ConfAccImp__private_IsEnabledDeviceOpportunityNoInline

- RVA: `0x0066BC78`–`0x0066BCAA` (길이 `50` bytes)
- VA: `0x000000014066BC78`
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
- `0x0066BC9F` → [Feature_ConfAccImp__private_IsEnabledFallback](Feature_ConfAccImp__private_IsEnabledFallback_function_0066BCE8.md) (function, `0x0066BCE8`)

### Direct callers
- [Feature_ConfAccImp_IsEnabledWithReporting](Feature_ConfAccImp_IsEnabledWithReporting_function_0066BC30.md) at `0x0066BC4F`

### Static image references
- `0x0066BC82` → RVA `0x00FC4470` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066BC78  48 83 EC 28                     sub rsp, 0x28
0066BC7C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0066BC82  8B 05 E8 87 95 00               mov eax, dword ptr [rip + 0x9587e8]
0066BC88  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0066BC8C  A8 20                           test al, 0x20
0066BC8E  74 05                           je 0x14066bc95
0066BC90  83 E0 01                        and eax, 1
0066BC93  EB 0F                           jmp 0x14066bca4
0066BC95  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0066BC9A  BA 04 00 00 00                  mov edx, 4
0066BC9F  E8 44 00 00 00                  call 0x14066bce8
0066BCA4  48 83 C4 28                     add rsp, 0x28
0066BCA8  C3                              ret
0066BCA9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ConfAccImp__private_IsEnabledDeviceOpportunityNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9799656)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9799656)))) & (32)) == 0) goto loc_0066BC95;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9799656))) & (1));
    goto loc_0066BCA4;
loc_0066BC95:
    result = Feature_ConfAccImp__private_IsEnabledFallback(v_stack_p8, 4, a3, a4);
loc_0066BCA4:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_ConfAccImp__private_IsEnabledDeviceOpportunityNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9587E8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9587E8)))) & (32)) == 0) goto loc_0066BC95;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9587E8))) & (1));
    goto loc_0066BCA4;
loc_0066BC95:
    result = Feature_ConfAccImp__private_IsEnabledFallback(v_stack_p8, 4, a3, a4);
loc_0066BCA4:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066BC78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066BC78[BB_0066BC78]
  bb_0066BC90[BB_0066BC90]
  bb_0066BC95[BB_0066BC95]
  bb_0066BCA4[BB_0066BCA4]
  bb_0066BCA9[BB_0066BCA9]
  bb_0066BC78 -->|branch| bb_0066BC95
  bb_0066BC78 -->|fallthrough| bb_0066BC90
  bb_0066BC90 -->|branch| bb_0066BCA4
  bb_0066BC95 -->|flow| bb_0066BCA4
```
