# DefaultInitializeProfiling

- RVA: `0x00B5CA40`–`0x00B5CA5F` (길이 `31` bytes)
- VA: `0x0000000140B5CA40`
- 실행 섹션: `PAGELK`
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
- `0x00B5CA44` → [Feature_Test52061194__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test52061194__private_IsEnabledDeviceUsageNoInline_function_004F74D4.md) (function, `0x004F74D4`)
- `0x00B5CA4D` → [DefaultInitializeProfilingEnhanced](DefaultInitializeProfilingEnhanced_function_00B5CA68.md) (function, `0x00B5CA68`)
- `0x00B5CA54` → [DefaultInitializeProfilingOriginal](DefaultInitializeProfilingOriginal_function_00B5CB30.md) (function, `0x00B5CB30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B5CA44` → [Feature_Test52061194__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test52061194__private_IsEnabledDeviceUsageNoInline_function_004F74D4.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B5CA40  48 83 EC 28                     sub rsp, 0x28
00B5CA44  E8 8B AA 99 FF                  call 0x1404f74d4
00B5CA49  85 C0                           test eax, eax
00B5CA4B  74 07                           je 0x140b5ca54
00B5CA4D  E8 16 00 00 00                  call 0x140b5ca68
00B5CA52  EB 05                           jmp 0x140b5ca59
00B5CA54  E8 D7 00 00 00                  call 0x140b5cb30
00B5CA59  48 83 C4 28                     add rsp, 0x28
00B5CA5D  C3                              ret
00B5CA5E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DefaultInitializeProfiling(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = Feature_Test52061194__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00B5CA54;
    result = DefaultInitializeProfilingEnhanced(a1, a2, a3, a4);
    goto loc_00B5CA59;
loc_00B5CA54:
    result = DefaultInitializeProfilingOriginal(a1, a2, a3, a4);
loc_00B5CA59:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void DefaultInitializeProfiling(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Feature_Test52061194__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_00B5CA54;
    result = DefaultInitializeProfilingEnhanced(a1, a2, a3, a4);
    goto loc_00B5CA59;
loc_00B5CA54:
    result = DefaultInitializeProfilingOriginal(a1, a2, a3, a4);
loc_00B5CA59:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B5CA40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B5CA40[BB_00B5CA40]
  bb_00B5CA4D[BB_00B5CA4D]
  bb_00B5CA54[BB_00B5CA54]
  bb_00B5CA59[BB_00B5CA59]
  bb_00B5CA5E[BB_00B5CA5E]
  bb_00B5CA40 -->|branch| bb_00B5CA54
  bb_00B5CA40 -->|fallthrough| bb_00B5CA4D
  bb_00B5CA4D -->|branch| bb_00B5CA59
  bb_00B5CA54 -->|flow| bb_00B5CA59
```
