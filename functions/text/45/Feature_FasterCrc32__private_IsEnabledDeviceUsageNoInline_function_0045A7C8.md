# Feature_FasterCrc32__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0045A7C8`–`0x0045A7FA` (길이 `50` bytes)
- VA: `0x000000014045A7C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0045A7F3` → [Feature_FasterCrc32__private_IsEnabledFallback](../4F/Feature_FasterCrc32__private_IsEnabledFallback_function_004FD1D8.md) (function, `0x004FD1D8`)

### Direct callers
- [RtlCrc32](RtlCrc32_function_0045A770.md) at `0x0045A788`

### Static image references
- `0x0045A7D2` → RVA `0x00FC4B68` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045A7C8  48 83 EC 28                     sub rsp, 0x28
0045A7CC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0045A7D2  8B 05 90 A3 B6 00               mov eax, dword ptr [rip + 0xb6a390]
0045A7D8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0045A7DC  A8 10                           test al, 0x10
0045A7DE  74 09                           je 0x14045a7e9
0045A7E0  83 E0 01                        and eax, 1
0045A7E3  48 83 C4 28                     add rsp, 0x28
0045A7E7  C3                              ret
0045A7E8  CC                              int3
0045A7E9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0045A7EE  BA 03 00 00 00                  mov edx, 3
0045A7F3  E8 E0 29 0A 00                  call 0x1404fd1d8
0045A7F8  EB E9                           jmp 0x14045a7e3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_FasterCrc32__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11969424)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11969424)))) & (16)) == 0) goto loc_0045A7E9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11969424))) & (1));
loc_0045A7E3:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0045A7E9:
    result = Feature_FasterCrc32__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_0045A7E3;
}
```

## 5. (Beta) C Style

```c
void Feature_FasterCrc32__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB6A390)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB6A390)))) & (16)) == 0) goto loc_0045A7E9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB6A390))) & (1));
loc_0045A7E3:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0045A7E9:
    result = Feature_FasterCrc32__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_0045A7E3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045A7C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045A7C8[BB_0045A7C8]
  bb_0045A7E0[BB_0045A7E0]
  bb_0045A7E3[BB_0045A7E3]
  bb_0045A7E8[BB_0045A7E8]
  bb_0045A7E9[BB_0045A7E9]
  bb_0045A7C8 -->|branch| bb_0045A7E9
  bb_0045A7C8 -->|fallthrough| bb_0045A7E0
  bb_0045A7E0 -->|flow| bb_0045A7E3
  bb_0045A7E8 -->|flow| bb_0045A7E9
  bb_0045A7E9 -->|branch| bb_0045A7E3
```
