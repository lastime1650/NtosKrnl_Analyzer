# Feature_ValUxPerf2__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0066DB40`–`0x0066DB72` (길이 `50` bytes)
- VA: `0x000000014066DB40`
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
- `0x0066DB67` → [Feature_ValUxPerf2__private_IsEnabledFallback](Feature_ValUxPerf2__private_IsEnabledFallback_function_0066DB78.md) (function, `0x0066DB78`)

### Direct callers
- [Feature_ValUxPerf2_IsEnabledWithReporting](Feature_ValUxPerf2_IsEnabledWithReporting_function_0066DAC0.md) at `0x0066DAE6`

### Static image references
- `0x0066DB4A` → RVA `0x00FC4528` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066DB40  48 83 EC 28                     sub rsp, 0x28
0066DB44  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0066DB4A  8B 05 D8 69 95 00               mov eax, dword ptr [rip + 0x9569d8]
0066DB50  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0066DB54  A8 10                           test al, 0x10
0066DB56  74 05                           je 0x14066db5d
0066DB58  83 E0 01                        and eax, 1
0066DB5B  EB 0F                           jmp 0x14066db6c
0066DB5D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0066DB62  BA 03 00 00 00                  mov edx, 3
0066DB67  E8 0C 00 00 00                  call 0x14066db78
0066DB6C  48 83 C4 28                     add rsp, 0x28
0066DB70  C3                              ret
0066DB71  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ValUxPerf2__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9791960)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9791960)))) & (16)) == 0) goto loc_0066DB5D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9791960))) & (1));
    goto loc_0066DB6C;
loc_0066DB5D:
    result = Feature_ValUxPerf2__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0066DB6C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_ValUxPerf2__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9569D8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9569D8)))) & (16)) == 0) goto loc_0066DB5D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9569D8))) & (1));
    goto loc_0066DB6C;
loc_0066DB5D:
    result = Feature_ValUxPerf2__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0066DB6C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066DB40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066DB40[BB_0066DB40]
  bb_0066DB58[BB_0066DB58]
  bb_0066DB5D[BB_0066DB5D]
  bb_0066DB6C[BB_0066DB6C]
  bb_0066DB71[BB_0066DB71]
  bb_0066DB40 -->|branch| bb_0066DB5D
  bb_0066DB40 -->|fallthrough| bb_0066DB58
  bb_0066DB58 -->|branch| bb_0066DB6C
  bb_0066DB5D -->|flow| bb_0066DB6C
```
