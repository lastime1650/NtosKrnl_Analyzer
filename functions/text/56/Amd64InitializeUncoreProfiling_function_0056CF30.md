# Amd64InitializeUncoreProfiling

- RVA: `0x0056CF30`–`0x0056CF4F` (길이 `31` bytes)
- VA: `0x000000014056CF30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0056CF34` → [Feature_Test52061194__private_IsEnabledDeviceUsageNoInline](../4F/Feature_Test52061194__private_IsEnabledDeviceUsageNoInline_function_004F74D4.md) (function, `0x004F74D4`)
- `0x0056CF3D` → [Amd64InitializeUncoreProfilingEnhanced](Amd64InitializeUncoreProfilingEnhanced_function_0056CF58.md) (function, `0x0056CF58`)
- `0x0056CF44` → [Amd64InitializeUncoreProfilingOriginal](Amd64InitializeUncoreProfilingOriginal_function_0056D068.md) (function, `0x0056D068`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056CF30  48 83 EC 28                     sub rsp, 0x28
0056CF34  E8 9B A5 F8 FF                  call 0x1404f74d4
0056CF39  85 C0                           test eax, eax
0056CF3B  74 07                           je 0x14056cf44
0056CF3D  E8 16 00 00 00                  call 0x14056cf58
0056CF42  EB 05                           jmp 0x14056cf49
0056CF44  E8 1F 01 00 00                  call 0x14056d068
0056CF49  48 83 C4 28                     add rsp, 0x28
0056CF4D  C3                              ret
0056CF4E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Amd64InitializeUncoreProfiling(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = Feature_Test52061194__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0056CF44;
    result = Amd64InitializeUncoreProfilingEnhanced(a1, a2, a3, a4);
    goto loc_0056CF49;
loc_0056CF44:
    result = Amd64InitializeUncoreProfilingOriginal(a1, a2, a3, a4);
loc_0056CF49:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Amd64InitializeUncoreProfiling(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Feature_Test52061194__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0056CF44;
    result = Amd64InitializeUncoreProfilingEnhanced(a1, a2, a3, a4);
    goto loc_0056CF49;
loc_0056CF44:
    result = Amd64InitializeUncoreProfilingOriginal(a1, a2, a3, a4);
loc_0056CF49:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056CF30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0056CF30[BB_0056CF30]
  bb_0056CF3D[BB_0056CF3D]
  bb_0056CF44[BB_0056CF44]
  bb_0056CF49[BB_0056CF49]
  bb_0056CF4E[BB_0056CF4E]
  bb_0056CF30 -->|branch| bb_0056CF44
  bb_0056CF30 -->|fallthrough| bb_0056CF3D
  bb_0056CF3D -->|branch| bb_0056CF49
  bb_0056CF44 -->|flow| bb_0056CF49
```
