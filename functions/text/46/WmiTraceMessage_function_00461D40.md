# WmiTraceMessage

- RVA: `0x00461D40`–`0x00461D64` (길이 `36` bytes)
- VA: `0x0000000140461D40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9F74`
- 디코드: `9`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00461D59` → [EtwpTraceMessageVa](../2F/EtwpTraceMessageVa_function_002FB2B0.md) (function, `0x002FB2B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00461D40  66 44 89 4C 24 20               mov word ptr [rsp + 0x20], r9w
00461D46  48 83 EC 48                     sub rsp, 0x48
00461D4A  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00461D4F  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
00461D54  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00461D59  E8 52 95 E9 FF                  call 0x1402fb2b0
00461D5E  48 83 C4 48                     add rsp, 0x48
00461D62  C3                              ret
00461D63  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmiTraceMessage(__int64 a1, __int64 a2, __int64 a3, unsigned __int16 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int16 v_stack_p20;

    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (72);
    v_stack_m20 = 0;
    v_stack_m28 = a5;
    result = EtwpTraceMessageVa(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WmiTraceMessage(int64_t Arg1, int64_t Arg2, int64_t Arg3, uint16_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m20;
    uint64_t v_stack_m28;
    uint16_t v_stack_p20;

    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (72);
    v_stack_m20 = 0;
    v_stack_m28 = Arg5;
    result = EtwpTraceMessageVa(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00461D40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00461D40[BB_00461D40]
  bb_00461D63[BB_00461D63]
```
