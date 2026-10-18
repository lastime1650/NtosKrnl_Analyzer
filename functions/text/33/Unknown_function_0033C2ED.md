# sub_0033C2ED

- RVA: `0x0033C2ED`–`0x0033C310` (길이 `35` bytes)
- VA: `0x000000014033C2ED`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076F64`
- 디코드: `9`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0033C302` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0033C2ED  CC                              int3
0033C2EE  45 33 C9                        xor r9d, r9d
0033C2F1  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0033C2F6  4C 8B C3                        mov r8, rbx
0033C2F9  BA 80 51 00 00                  mov edx, 0x5180
0033C2FE  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
0033C302  E8 59 13 1C 00                  call 0x1404fd660
0033C307  CC                              int3
0033C308  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0033C2ED(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    unsigned __int64 v_stack_p20;

    a4 = 0;
    v_stack_p20 = v_r13;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x5180ULL), v_rbx, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0033C2ED(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    uint64_t v_stack_p20;

    Arg4 = 0;
    v_stack_p20 = local_r13;
    result = KeBugCheckEx(Arg4 + 26, (uint32_t)(0x5180ULL), local_rbx, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033C2ED&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0033C2ED[BB_0033C2ED]
```
