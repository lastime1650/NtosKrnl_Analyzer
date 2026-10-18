# i64tow_s

- RVA: `0x00504EB0`–`0x00504ED4` (길이 `36` bytes)
- VA: `0x0000000140504EB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `12`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00504EC9` → [x64tow_s](x64tow_s_function_00504F4C.md) (function, `0x00504F4C`)

### Direct callers
- [LocalGetStringForRelativeAttribute](../../page/A0/LocalGetStringForRelativeAttribute_function_00A02C38.md) at `0x00A03037`
- [LocalGetStringForRelativeAttribute](../../page/A0/LocalGetStringForRelativeAttribute_function_00A02C38.md) at `0x00A033B1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00504EB0  48 83 EC 38                     sub rsp, 0x38
00504EB4  33 C0                           xor eax, eax
00504EB6  41 83 F9 0A                     cmp r9d, 0xa
00504EBA  75 09                           jne 0x140504ec5
00504EBC  48 85 C9                        test rcx, rcx
00504EBF  79 04                           jns 0x140504ec5
00504EC1  41 8D 41 F7                     lea eax, [r9 - 9]
00504EC5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00504EC9  E8 7E 00 00 00                  call 0x140504f4c
00504ECE  48 83 C4 38                     add rsp, 0x38
00504ED2  C3                              ret
00504ED3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall i64tow_s(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = 0;
    if (((unsigned int)(a4)) != 10) goto loc_00504EC5;
    if (sign_flag) {
        result = a4 - 9;
    }
    v_stack_m18 = (unsigned int)(result);
    result = x64tow_s(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t i64tow_s(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = 0;
    if (((uint32_t)(Arg4)) != 10) goto loc_00504EC5;
    if (sign_flag) {
        result = Arg4 - 9;
    }
    v_stack_m18 = (uint32_t)(result);
    result = x64tow_s(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00504EB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00504EB0[BB_00504EB0]
  bb_00504EBC[BB_00504EBC]
  bb_00504EC1[BB_00504EC1]
  bb_00504EC5[BB_00504EC5]
  bb_00504ED3[BB_00504ED3]
  bb_00504EB0 -->|branch| bb_00504EC5
  bb_00504EB0 -->|fallthrough| bb_00504EBC
  bb_00504EBC -->|branch| bb_00504EC5
  bb_00504EBC -->|fallthrough| bb_00504EC1
  bb_00504EC1 -->|flow| bb_00504EC5
```
