# sub_00500D66

- RVA: `0x00500D66`–`0x00500D7E` (길이 `24` bytes)
- VA: `0x0000000140500D66`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C26CC`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00500D77` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00500D7C` → [sub_00500D9E](Unknown_function_00500D9E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00500D66  33 C0                           xor eax, eax
00500D68  45 33 C9                        xor r9d, r9d
00500D6B  45 33 C0                        xor r8d, r8d
00500D6E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00500D73  33 D2                           xor edx, edx
00500D75  33 C9                           xor ecx, ecx
00500D77  E8 D4 D7 F9 FF                  call 0x14049e550
00500D7C  EB 20                           jmp 0x140500d9e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00500D66(int a1, int a2, int a3, int a4)
{
    __int64 result;
    unsigned __int64 v_stack_p20;

    result = 0;
    a4 = 0;
    a3 = 0;
    v_stack_p20 = 0;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00500D66(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    uint64_t v_stack_p20;

    result = 0;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00500D66&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00500D66[BB_00500D66]
```
