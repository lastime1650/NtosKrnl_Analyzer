# Feature_Servicing_PrmSaveRestoreS4__private_IsEnabledNoReportingNoInline

- RVA: `0x0054E214`–`0x0054E243` (길이 `47` bytes)
- VA: `0x000000014054E214`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0054E238` → [Feature_Servicing_PrmSaveRestoreS4__private_IsEnabledFallback](Feature_Servicing_PrmSaveRestoreS4__private_IsEnabledFallback_function_0054E1F8.md) (function, `0x0054E1F8`)

### Direct callers
- [HaliLocateHiberRanges](../../pagelk/B5/HaliLocateHiberRanges_function_00B5CE50.md) at `0x00B5CF23`

### Static image references
- `0x0054E21E` → RVA `0x00FC46E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054E214  48 83 EC 28                     sub rsp, 0x28
0054E218  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0054E21E  8B 05 BC 64 A7 00               mov eax, dword ptr [rip + 0xa764bc]
0054E224  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0054E228  A8 02                           test al, 2
0054E22A  74 05                           je 0x14054e231
0054E22C  83 E0 01                        and eax, 1
0054E22F  EB 0C                           jmp 0x14054e23d
0054E231  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054E236  33 D2                           xor edx, edx
0054E238  E8 BB FF FF FF                  call 0x14054e1f8
0054E23D  48 83 C4 28                     add rsp, 0x28
0054E241  C3                              ret
0054E242  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_PrmSaveRestoreS4__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10970300)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10970300)))) & (2)) == 0) goto loc_0054E231;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10970300))) & (1));
    goto loc_0054E23D;
loc_0054E231:
    a2 = 0;
    result = Feature_Servicing_PrmSaveRestoreS4__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_0054E23D:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Servicing_PrmSaveRestoreS4__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA764BC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA764BC)))) & (2)) == 0) goto loc_0054E231;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA764BC))) & (1));
    goto loc_0054E23D;
loc_0054E231:
    Arg2 = 0;
    result = Feature_Servicing_PrmSaveRestoreS4__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_0054E23D:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054E214&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054E214[BB_0054E214]
  bb_0054E22C[BB_0054E22C]
  bb_0054E231[BB_0054E231]
  bb_0054E23D[BB_0054E23D]
  bb_0054E242[BB_0054E242]
  bb_0054E214 -->|branch| bb_0054E231
  bb_0054E214 -->|fallthrough| bb_0054E22C
  bb_0054E22C -->|branch| bb_0054E23D
  bb_0054E231 -->|flow| bb_0054E23D
```
