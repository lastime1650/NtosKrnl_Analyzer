# sub_00B82933

- RVA: `0x00B82933`–`0x00B82950` (길이 `29` bytes)
- VA: `0x0000000140B82933`
- 실행 섹션: `POOLCODE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007BDFC`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B8294A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B8294A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B82933  BA 99 00 00 00                  mov edx, 0x99
00B82938  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
00B82941  45 33 C9                        xor r9d, r9d
00B82944  4D 8B C5                        mov r8, r13
00B82947  8D 4A 29                        lea ecx, [rdx + 0x29]
00B8294A  E8 11 AD 97 FF                  call 0x1404fd660
00B8294F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B82933(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(153 + 41, 153, v_r13, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B82933(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    uint64_t v_stack_p20;

    v_stack_p20 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(153 + 41, 153, local_r13, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=poolcode&rva=0x00B82933&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B82933[BB_00B82933]
```
