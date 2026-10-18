# Feature_ExpToc__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0066BE20`–`0x0066BE52` (길이 `50` bytes)
- VA: `0x000000014066BE20`
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
- `0x0066BE47` → [Feature_ExpToc__private_IsEnabledFallback](Feature_ExpToc__private_IsEnabledFallback_function_0066BE58.md) (function, `0x0066BE58`)

### Direct callers
- [Feature_ExpToc_IsEnabledWithReporting](Feature_ExpToc_IsEnabledWithReporting_function_0066BDA0.md) at `0x0066BDC6`

### Static image references
- `0x0066BE2A` → RVA `0x00FC4570` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066BE20  48 83 EC 28                     sub rsp, 0x28
0066BE24  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0066BE2A  8B 05 40 87 95 00               mov eax, dword ptr [rip + 0x958740]
0066BE30  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0066BE34  A8 10                           test al, 0x10
0066BE36  74 05                           je 0x14066be3d
0066BE38  83 E0 01                        and eax, 1
0066BE3B  EB 0F                           jmp 0x14066be4c
0066BE3D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0066BE42  BA 03 00 00 00                  mov edx, 3
0066BE47  E8 0C 00 00 00                  call 0x14066be58
0066BE4C  48 83 C4 28                     add rsp, 0x28
0066BE50  C3                              ret
0066BE51  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ExpToc__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9799488)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9799488)))) & (16)) == 0) goto loc_0066BE3D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9799488))) & (1));
    goto loc_0066BE4C;
loc_0066BE3D:
    result = Feature_ExpToc__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0066BE4C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_ExpToc__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x958740)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x958740)))) & (16)) == 0) goto loc_0066BE3D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x958740))) & (1));
    goto loc_0066BE4C;
loc_0066BE3D:
    result = Feature_ExpToc__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0066BE4C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066BE20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066BE20[BB_0066BE20]
  bb_0066BE38[BB_0066BE38]
  bb_0066BE3D[BB_0066BE3D]
  bb_0066BE4C[BB_0066BE4C]
  bb_0066BE51[BB_0066BE51]
  bb_0066BE20 -->|branch| bb_0066BE3D
  bb_0066BE20 -->|fallthrough| bb_0066BE38
  bb_0066BE38 -->|branch| bb_0066BE4C
  bb_0066BE3D -->|flow| bb_0066BE4C
```
