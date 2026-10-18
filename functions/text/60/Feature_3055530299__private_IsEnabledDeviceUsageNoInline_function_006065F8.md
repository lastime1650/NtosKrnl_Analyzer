# Feature_3055530299__private_IsEnabledDeviceUsageNoInline

- RVA: `0x006065F8`–`0x0060662A` (길이 `50` bytes)
- VA: `0x00000001406065F8`
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
- `0x0060661F` → [Feature_3055530299__private_IsEnabledFallback](Feature_3055530299__private_IsEnabledFallback_function_00606630.md) (function, `0x00606630`)

### Direct callers
- [SepAdjustPrivileges](../../page/9C/SepAdjustPrivileges_function_009C8DFC.md) at `0x009C8FA9`
- [SepAdjustPrivileges](../../page/9C/SepAdjustPrivileges_function_009C8DFC.md) at `0x009C91B4`
- [SepAdjustPrivileges](../../page/9C/SepAdjustPrivileges_function_009C8DFC.md) at `0x009C9301`
- [SepAdjustPrivileges](../../page/9C/SepAdjustPrivileges_function_009C8DFC.md) at `0x009C936E`

### Static image references
- `0x00606602` → RVA `0x00FC4B80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006065F8  48 83 EC 28                     sub rsp, 0x28
006065FC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00606602  8B 05 78 E5 9B 00               mov eax, dword ptr [rip + 0x9be578]
00606608  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0060660C  A8 10                           test al, 0x10
0060660E  74 05                           je 0x140606615
00606610  83 E0 01                        and eax, 1
00606613  EB 0F                           jmp 0x140606624
00606615  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0060661A  BA 03 00 00 00                  mov edx, 3
0060661F  E8 0C 00 00 00                  call 0x140606630
00606624  48 83 C4 28                     add rsp, 0x28
00606628  C3                              ret
00606629  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_3055530299__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10216824)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10216824)))) & (16)) == 0) goto loc_00606615;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10216824))) & (1));
    goto loc_00606624;
loc_00606615:
    result = Feature_3055530299__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00606624:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_3055530299__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9BE578)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9BE578)))) & (16)) == 0) goto loc_00606615;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9BE578))) & (1));
    goto loc_00606624;
loc_00606615:
    result = Feature_3055530299__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00606624:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006065F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006065F8[BB_006065F8]
  bb_00606610[BB_00606610]
  bb_00606615[BB_00606615]
  bb_00606624[BB_00606624]
  bb_00606629[BB_00606629]
  bb_006065F8 -->|branch| bb_00606615
  bb_006065F8 -->|fallthrough| bb_00606610
  bb_00606610 -->|branch| bb_00606624
  bb_00606615 -->|flow| bb_00606624
```
