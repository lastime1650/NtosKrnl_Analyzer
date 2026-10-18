# Feature_TestUxGate_IsEnabledWithReporting

- RVA: `0x0066D000`–`0x0066D040` (길이 `64` bytes)
- VA: `0x000000014066D000`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `24`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0066D018` → [Feature_TestUxGate__private_IsEnabledOtherReporting](Feature_TestUxGate__private_IsEnabledOtherReporting_function_0066D10C.md) (function, `0x0066D10C`)
- `0x0066D01F` → [Feature_TestUxGate__private_IsEnabledDeviceOpportunityNoInline](Feature_TestUxGate__private_IsEnabledDeviceOpportunityNoInline_function_0066D048.md) (function, `0x0066D048`)
- `0x0066D026` → [Feature_TestUxGate__private_IsEnabledDeviceUsageNoInline](Feature_TestUxGate__private_IsEnabledDeviceUsageNoInline_function_0066D080.md) (function, `0x0066D080`)
- `0x0066D02D` → [Feature_TestUxGate__private_IsEnabledNoReportingNoInline](Feature_TestUxGate__private_IsEnabledNoReportingNoInline_function_0066D0D4.md) (function, `0x0066D0D4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066D000  40 53                           push rbx
0066D002  48 83 EC 20                     sub rsp, 0x20
0066D006  33 DB                           xor ebx, ebx
0066D008  8B D1                           mov edx, ecx
0066D00A  85 C9                           test ecx, ecx
0066D00C  74 1F                           je 0x14066d02d
0066D00E  83 EA 03                        sub edx, 3
0066D011  74 13                           je 0x14066d026
0066D013  83 FA 01                        cmp edx, 1
0066D016  74 07                           je 0x14066d01f
0066D018  E8 EF 00 00 00                  call 0x14066d10c
0066D01D  EB 13                           jmp 0x14066d032
0066D01F  E8 24 00 00 00                  call 0x14066d048
0066D024  EB 0C                           jmp 0x14066d032
0066D026  E8 55 00 00 00                  call 0x14066d080
0066D02B  EB 05                           jmp 0x14066d032
0066D02D  E8 A2 00 00 00                  call 0x14066d0d4
0066D032  85 C0                           test eax, eax
0066D034  0F 95 C3                        setne bl
0066D037  8B C3                           mov eax, ebx
0066D039  48 83 C4 20                     add rsp, 0x20
0066D03D  5B                              pop rbx
0066D03E  C3                              ret
0066D03F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_TestUxGate_IsEnabledWithReporting(int a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    if (a1 == 0) goto loc_0066D02D;
    a2 = (unsigned int)(((unsigned int)(a1)) - (3));
    if (condition_is_equal) goto loc_0066D026;
    if (((unsigned int)(a2)) == 1) goto loc_0066D01F;
    result = Feature_TestUxGate__private_IsEnabledOtherReporting(a1, a2, a3, a4);
    goto loc_0066D032;
loc_0066D01F:
    result = Feature_TestUxGate__private_IsEnabledDeviceOpportunityNoInline(a1, a2, a3, a4);
    goto loc_0066D032;
loc_0066D026:
    result = Feature_TestUxGate__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    goto loc_0066D032;
loc_0066D02D:
    result = Feature_TestUxGate__private_IsEnabledNoReportingNoInline(a1, a2, a3, a4);
loc_0066D032:
    v_rbx = ((unsigned int)(result) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t Feature_TestUxGate_IsEnabledWithReporting(int32_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    if (Arg1 == 0) goto loc_0066D02D;
    a2 = (uint32_t)(((uint32_t)(Arg1)) - (3));
    if (condition_is_equal) goto loc_0066D026;
    if (((uint32_t)(a2)) == 1) goto loc_0066D01F;
    result = Feature_TestUxGate__private_IsEnabledOtherReporting(Arg1, a2, a3, a4);
    goto loc_0066D032;
loc_0066D01F:
    result = Feature_TestUxGate__private_IsEnabledDeviceOpportunityNoInline(Arg1, a2, a3, a4);
    goto loc_0066D032;
loc_0066D026:
    result = Feature_TestUxGate__private_IsEnabledDeviceUsageNoInline(Arg1, a2, a3, a4);
    goto loc_0066D032;
loc_0066D02D:
    result = Feature_TestUxGate__private_IsEnabledNoReportingNoInline(Arg1, a2, a3, a4);
loc_0066D032:
    local_rbx = ((uint32_t)(result) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066D000&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066D000[BB_0066D000]
  bb_0066D00E[BB_0066D00E]
  bb_0066D013[BB_0066D013]
  bb_0066D018[BB_0066D018]
  bb_0066D01F[BB_0066D01F]
  bb_0066D026[BB_0066D026]
  bb_0066D02D[BB_0066D02D]
  bb_0066D032[BB_0066D032]
  bb_0066D03F[BB_0066D03F]
  bb_0066D000 -->|branch| bb_0066D02D
  bb_0066D000 -->|fallthrough| bb_0066D00E
  bb_0066D00E -->|branch| bb_0066D026
  bb_0066D00E -->|fallthrough| bb_0066D013
  bb_0066D013 -->|branch| bb_0066D01F
  bb_0066D013 -->|fallthrough| bb_0066D018
  bb_0066D018 -->|branch| bb_0066D032
  bb_0066D01F -->|branch| bb_0066D032
  bb_0066D026 -->|branch| bb_0066D032
  bb_0066D02D -->|flow| bb_0066D032
```
