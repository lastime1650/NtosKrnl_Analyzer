# Amd64InitializeProfiling

- RVA: `0x00B612F0`–`0x00B6130F` (길이 `31` bytes)
- VA: `0x0000000140B612F0`
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
- `0x00B612F4` → [Feature_Test52061194__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test52061194__private_IsEnabledDeviceUsageNoInline_function_004F74D4.md) (function, `0x004F74D4`)
- `0x00B612FD` → [Amd64InitializeProfilingEnhanced](Amd64InitializeProfilingEnhanced_function_00B61318.md) (function, `0x00B61318`)
- `0x00B61304` → [Amd64InitializeProfilingOriginal](Amd64InitializeProfilingOriginal_function_00B618D8.md) (function, `0x00B618D8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B612F4` → [Feature_Test52061194__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Test52061194__private_IsEnabledDeviceUsageNoInline_function_004F74D4.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B612F0  48 83 EC 28                     sub rsp, 0x28
00B612F4  E8 DB 61 99 FF                  call 0x1404f74d4
00B612F9  85 C0                           test eax, eax
00B612FB  74 07                           je 0x140b61304
00B612FD  E8 16 00 00 00                  call 0x140b61318
00B61302  EB 05                           jmp 0x140b61309
00B61304  E8 CF 05 00 00                  call 0x140b618d8
00B61309  48 83 C4 28                     add rsp, 0x28
00B6130D  C3                              ret
00B6130E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Amd64InitializeProfiling(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = Feature_Test52061194__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00B61304;
    result = Amd64InitializeProfilingEnhanced(a1, a2, a3, a4);
    goto loc_00B61309;
loc_00B61304:
    result = Amd64InitializeProfilingOriginal(a1, a2, a3, a4);
loc_00B61309:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Amd64InitializeProfiling(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Feature_Test52061194__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_00B61304;
    result = Amd64InitializeProfilingEnhanced(a1, a2, a3, a4);
    goto loc_00B61309;
loc_00B61304:
    result = Amd64InitializeProfilingOriginal(a1, a2, a3, a4);
loc_00B61309:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B612F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B612F0[BB_00B612F0]
  bb_00B612FD[BB_00B612FD]
  bb_00B61304[BB_00B61304]
  bb_00B61309[BB_00B61309]
  bb_00B6130E[BB_00B6130E]
  bb_00B612F0 -->|branch| bb_00B61304
  bb_00B612F0 -->|fallthrough| bb_00B612FD
  bb_00B612FD -->|branch| bb_00B61309
  bb_00B61304 -->|flow| bb_00B61309
```
