# itow_s

- RVA: `0x00504EE0`–`0x00504F03` (길이 `35` bytes)
- VA: `0x0000000140504EE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `12`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00504EF8` → [xtow_s](xtow_s_function_00505090.md) (function, `0x00505090`)

### Direct callers
- [RtlpFindRegTziForCurrentYear](../5E/RtlpFindRegTziForCurrentYear_function_005E7754.md) at `0x005E77A5`
- [RtlpFindRegTziForCurrentYear](../5E/RtlpFindRegTziForCurrentYear_function_005E7754.md) at `0x005E788B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00504EE0  48 83 EC 38                     sub rsp, 0x38
00504EE4  33 C0                           xor eax, eax
00504EE6  41 83 F9 0A                     cmp r9d, 0xa
00504EEA  75 08                           jne 0x140504ef4
00504EEC  85 C9                           test ecx, ecx
00504EEE  79 04                           jns 0x140504ef4
00504EF0  41 8D 41 F7                     lea eax, [r9 - 9]
00504EF4  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00504EF8  E8 93 01 00 00                  call 0x140505090
00504EFD  48 83 C4 38                     add rsp, 0x38
00504F01  C3                              ret
00504F02  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall itow_s(int a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = 0;
    if (((unsigned int)(a4)) != 10) goto loc_00504EF4;
    if (sign_flag) {
        result = a4 - 9;
    }
    v_stack_m18 = (unsigned int)(result);
    result = xtow_s(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t itow_s(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = 0;
    if (((uint32_t)(Arg4)) != 10) goto loc_00504EF4;
    if (sign_flag) {
        result = Arg4 - 9;
    }
    v_stack_m18 = (uint32_t)(result);
    result = xtow_s(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00504EE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00504EE0[BB_00504EE0]
  bb_00504EEC[BB_00504EEC]
  bb_00504EF0[BB_00504EF0]
  bb_00504EF4[BB_00504EF4]
  bb_00504F02[BB_00504F02]
  bb_00504EE0 -->|branch| bb_00504EF4
  bb_00504EE0 -->|fallthrough| bb_00504EEC
  bb_00504EEC -->|branch| bb_00504EF4
  bb_00504EEC -->|fallthrough| bb_00504EF0
  bb_00504EF0 -->|flow| bb_00504EF4
```
