# vsnwprintf

- RVA: `0x004FEF30`–`0x004FEF47` (길이 `23` bytes)
- VA: `0x00000001404FEF30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `7`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FEF3C` → [vsnwprintf_l](vsnwprintf_l_function_004FEF50.md) (function, `0x004FEF50`)

### Direct callers
- [RtlStringCbPrintfW](../40/RtlStringCbPrintfW_function_0040FB40.md) at `0x0040FB75`
- [sub_0042B3EC](../42/Unknown_function_0042B3EC.md) at `0x0042B448`
- [RtlStringCbPrintfExW](../46/RtlStringCbPrintfExW_function_00461AD4.md) at `0x00461B6F`
- [StringCchPrintfW](../47/StringCchPrintfW_function_0047BAD0.md) at `0x0047BB02`
- [RtlStringCchPrintfW](../48/RtlStringCchPrintfW_function_00482D5C.md) at `0x00482D8E`
- [RtlUnicodeStringPrintf](../48/RtlUnicodeStringPrintf_function_0048B984.md) at `0x0048B9DD`
- [RtlUnicodeStringPrintfEx](../4A/RtlUnicodeStringPrintfEx_function_004A8FD0.md) at `0x004A9042`
- [StringCchPrintfExW](../69/StringCchPrintfExW_function_0069DE98.md) at `0x0069DFD7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FEF30  48 83 EC 38                     sub rsp, 0x38
004FEF34  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
004FEF39  45 33 C9                        xor r9d, r9d
004FEF3C  E8 0F 00 00 00                  call 0x1404fef50
004FEF41  48 83 C4 38                     add rsp, 0x38
004FEF45  C3                              ret
004FEF46  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall vsnwprintf(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = a4;
    a4 = 0;
    result = vsnwprintf_l(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t vsnwprintf(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = Arg4;
    Arg4 = 0;
    result = vsnwprintf_l(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FEF30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FEF30[BB_004FEF30]
  bb_004FEF46[BB_004FEF46]
```
