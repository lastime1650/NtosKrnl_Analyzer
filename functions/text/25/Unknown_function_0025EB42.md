# sub_0025EB42

- RVA: `0x0025EB42`–`0x0025EB5D` (길이 `27` bytes)
- VA: `0x000000014025EB42`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064140`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0025EB57` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0025EB42  33 F6                           xor esi, esi
0025EB44  45 33 C9                        xor r9d, r9d
0025EB47  4C 8B C7                        mov r8, rdi
0025EB4A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0025EB4F  B9 C6 01 00 00                  mov ecx, 0x1c6
0025EB54  8D 56 0F                        lea edx, [rsi + 0xf]
0025EB57  E8 04 EB 29 00                  call 0x1404fd660
0025EB5C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0025EB42(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;

    v_rsi = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, v_rsi + 15, v_rdi, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0025EB42(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsi;
    uint64_t v_stack_p20;

    local_rsi = 0;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, local_rsi + 15, local_rdi, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0025EB42&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0025EB42[BB_0025EB42]
```
