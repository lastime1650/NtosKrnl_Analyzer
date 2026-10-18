# Feature_UxAccOptimization__private_IsEnabledDeviceOpportunityNoInline

- RVA: `0x0066D378`–`0x0066D3AA` (길이 `50` bytes)
- VA: `0x000000014066D378`
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
- `0x0066D39F` → [Feature_UxAccOptimization__private_IsEnabledFallback](Feature_UxAccOptimization__private_IsEnabledFallback_function_0066D3E8.md) (function, `0x0066D3E8`)

### Direct callers
- [Feature_UxAccOptimization_IsEnabledWithReporting](Feature_UxAccOptimization_IsEnabledWithReporting_function_0066D330.md) at `0x0066D34F`

### Static image references
- `0x0066D382` → RVA `0x00FC44B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066D378  48 83 EC 28                     sub rsp, 0x28
0066D37C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0066D382  8B 05 30 71 95 00               mov eax, dword ptr [rip + 0x957130]
0066D388  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0066D38C  A8 20                           test al, 0x20
0066D38E  74 05                           je 0x14066d395
0066D390  83 E0 01                        and eax, 1
0066D393  EB 0F                           jmp 0x14066d3a4
0066D395  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0066D39A  BA 04 00 00 00                  mov edx, 4
0066D39F  E8 44 00 00 00                  call 0x14066d3e8
0066D3A4  48 83 C4 28                     add rsp, 0x28
0066D3A8  C3                              ret
0066D3A9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_UxAccOptimization__private_IsEnabledDeviceOpportunityNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9793840)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9793840)))) & (32)) == 0) goto loc_0066D395;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9793840))) & (1));
    goto loc_0066D3A4;
loc_0066D395:
    result = Feature_UxAccOptimization__private_IsEnabledFallback(v_stack_p8, 4, a3, a4);
loc_0066D3A4:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_UxAccOptimization__private_IsEnabledDeviceOpportunityNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x957130)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x957130)))) & (32)) == 0) goto loc_0066D395;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x957130))) & (1));
    goto loc_0066D3A4;
loc_0066D395:
    result = Feature_UxAccOptimization__private_IsEnabledFallback(v_stack_p8, 4, a3, a4);
loc_0066D3A4:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066D378&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066D378[BB_0066D378]
  bb_0066D390[BB_0066D390]
  bb_0066D395[BB_0066D395]
  bb_0066D3A4[BB_0066D3A4]
  bb_0066D3A9[BB_0066D3A9]
  bb_0066D378 -->|branch| bb_0066D395
  bb_0066D378 -->|fallthrough| bb_0066D390
  bb_0066D390 -->|branch| bb_0066D3A4
  bb_0066D395 -->|flow| bb_0066D3A4
```
