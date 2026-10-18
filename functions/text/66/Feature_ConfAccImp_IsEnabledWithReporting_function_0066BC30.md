# Feature_ConfAccImp_IsEnabledWithReporting

- RVA: `0x0066BC30`–`0x0066BC70` (길이 `64` bytes)
- VA: `0x000000014066BC30`
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
- `0x0066BC48` → [Feature_ConfAccImp__private_IsEnabledOtherReporting](Feature_ConfAccImp__private_IsEnabledOtherReporting_function_0066BD3C.md) (function, `0x0066BD3C`)
- `0x0066BC4F` → [Feature_ConfAccImp__private_IsEnabledDeviceOpportunityNoInline](Feature_ConfAccImp__private_IsEnabledDeviceOpportunityNoInline_function_0066BC78.md) (function, `0x0066BC78`)
- `0x0066BC56` → [Feature_ConfAccImp__private_IsEnabledDeviceUsageNoInline](Feature_ConfAccImp__private_IsEnabledDeviceUsageNoInline_function_0066BCB0.md) (function, `0x0066BCB0`)
- `0x0066BC5D` → [Feature_ConfAccImp__private_IsEnabledNoReportingNoInline](Feature_ConfAccImp__private_IsEnabledNoReportingNoInline_function_0066BD04.md) (function, `0x0066BD04`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066BC30  40 53                           push rbx
0066BC32  48 83 EC 20                     sub rsp, 0x20
0066BC36  33 DB                           xor ebx, ebx
0066BC38  8B D1                           mov edx, ecx
0066BC3A  85 C9                           test ecx, ecx
0066BC3C  74 1F                           je 0x14066bc5d
0066BC3E  83 EA 03                        sub edx, 3
0066BC41  74 13                           je 0x14066bc56
0066BC43  83 FA 01                        cmp edx, 1
0066BC46  74 07                           je 0x14066bc4f
0066BC48  E8 EF 00 00 00                  call 0x14066bd3c
0066BC4D  EB 13                           jmp 0x14066bc62
0066BC4F  E8 24 00 00 00                  call 0x14066bc78
0066BC54  EB 0C                           jmp 0x14066bc62
0066BC56  E8 55 00 00 00                  call 0x14066bcb0
0066BC5B  EB 05                           jmp 0x14066bc62
0066BC5D  E8 A2 00 00 00                  call 0x14066bd04
0066BC62  85 C0                           test eax, eax
0066BC64  0F 95 C3                        setne bl
0066BC67  8B C3                           mov eax, ebx
0066BC69  48 83 C4 20                     add rsp, 0x20
0066BC6D  5B                              pop rbx
0066BC6E  C3                              ret
0066BC6F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ConfAccImp_IsEnabledWithReporting(int a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    if (a1 == 0) goto loc_0066BC5D;
    a2 = (unsigned int)(((unsigned int)(a1)) - (3));
    if (condition_is_equal) goto loc_0066BC56;
    if (((unsigned int)(a2)) == 1) goto loc_0066BC4F;
    result = Feature_ConfAccImp__private_IsEnabledOtherReporting(a1, a2, a3, a4);
    goto loc_0066BC62;
loc_0066BC4F:
    result = Feature_ConfAccImp__private_IsEnabledDeviceOpportunityNoInline(a1, a2, a3, a4);
    goto loc_0066BC62;
loc_0066BC56:
    result = Feature_ConfAccImp__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    goto loc_0066BC62;
loc_0066BC5D:
    result = Feature_ConfAccImp__private_IsEnabledNoReportingNoInline(a1, a2, a3, a4);
loc_0066BC62:
    v_rbx = ((unsigned int)(result) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t Feature_ConfAccImp_IsEnabledWithReporting(int32_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    if (Arg1 == 0) goto loc_0066BC5D;
    a2 = (uint32_t)(((uint32_t)(Arg1)) - (3));
    if (condition_is_equal) goto loc_0066BC56;
    if (((uint32_t)(a2)) == 1) goto loc_0066BC4F;
    result = Feature_ConfAccImp__private_IsEnabledOtherReporting(Arg1, a2, a3, a4);
    goto loc_0066BC62;
loc_0066BC4F:
    result = Feature_ConfAccImp__private_IsEnabledDeviceOpportunityNoInline(Arg1, a2, a3, a4);
    goto loc_0066BC62;
loc_0066BC56:
    result = Feature_ConfAccImp__private_IsEnabledDeviceUsageNoInline(Arg1, a2, a3, a4);
    goto loc_0066BC62;
loc_0066BC5D:
    result = Feature_ConfAccImp__private_IsEnabledNoReportingNoInline(Arg1, a2, a3, a4);
loc_0066BC62:
    local_rbx = ((uint32_t)(result) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066BC30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066BC30[BB_0066BC30]
  bb_0066BC3E[BB_0066BC3E]
  bb_0066BC43[BB_0066BC43]
  bb_0066BC48[BB_0066BC48]
  bb_0066BC4F[BB_0066BC4F]
  bb_0066BC56[BB_0066BC56]
  bb_0066BC5D[BB_0066BC5D]
  bb_0066BC62[BB_0066BC62]
  bb_0066BC6F[BB_0066BC6F]
  bb_0066BC30 -->|branch| bb_0066BC5D
  bb_0066BC30 -->|fallthrough| bb_0066BC3E
  bb_0066BC3E -->|branch| bb_0066BC56
  bb_0066BC3E -->|fallthrough| bb_0066BC43
  bb_0066BC43 -->|branch| bb_0066BC4F
  bb_0066BC43 -->|fallthrough| bb_0066BC48
  bb_0066BC48 -->|branch| bb_0066BC62
  bb_0066BC4F -->|branch| bb_0066BC62
  bb_0066BC56 -->|branch| bb_0066BC62
  bb_0066BC5D -->|flow| bb_0066BC62
```
