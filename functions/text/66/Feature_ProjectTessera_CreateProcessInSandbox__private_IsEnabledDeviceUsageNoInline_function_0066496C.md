# Feature_ProjectTessera_CreateProcessInSandbox__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0066496C`–`0x0066499E` (길이 `50` bytes)
- VA: `0x000000014066496C`
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
- `0x00664993` → [Feature_ProjectTessera_CreateProcessInSandbox__private_IsEnabledFallback](Feature_ProjectTessera_CreateProcessInSandbox__private_IsEnabledFallback_function_006649A4.md) (function, `0x006649A4`)

### Direct callers
- [IsFeatureEnabled](IsFeatureEnabled_function_006649C0.md) at `0x006649E7`

### Static image references
- `0x00664976` → RVA `0x00FC4A80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066496C  48 83 EC 28                     sub rsp, 0x28
00664970  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00664976  8B 05 04 01 96 00               mov eax, dword ptr [rip + 0x960104]
0066497C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00664980  A8 10                           test al, 0x10
00664982  74 05                           je 0x140664989
00664984  83 E0 01                        and eax, 1
00664987  EB 0F                           jmp 0x140664998
00664989  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0066498E  BA 03 00 00 00                  mov edx, 3
00664993  E8 0C 00 00 00                  call 0x1406649a4
00664998  48 83 C4 28                     add rsp, 0x28
0066499C  C3                              ret
0066499D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ProjectTessera_CreateProcessInSandbox__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9830660)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9830660)))) & (16)) == 0) goto loc_00664989;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9830660))) & (1));
    goto loc_00664998;
loc_00664989:
    result = Feature_ProjectTessera_CreateProcessInSandbox__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00664998:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_ProjectTessera_CreateProcessInSandbox__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x960104)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x960104)))) & (16)) == 0) goto loc_00664989;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x960104))) & (1));
    goto loc_00664998;
loc_00664989:
    result = Feature_ProjectTessera_CreateProcessInSandbox__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00664998:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066496C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066496C[BB_0066496C]
  bb_00664984[BB_00664984]
  bb_00664989[BB_00664989]
  bb_00664998[BB_00664998]
  bb_0066499D[BB_0066499D]
  bb_0066496C -->|branch| bb_00664989
  bb_0066496C -->|fallthrough| bb_00664984
  bb_00664984 -->|branch| bb_00664998
  bb_00664989 -->|flow| bb_00664998
```
