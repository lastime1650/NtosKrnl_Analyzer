# sub_0031EE80

- RVA: `0x0031EE80`–`0x0031EEA5` (길이 `37` bytes)
- VA: `0x000000014031EE80`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000752CC`
- 디코드: `10`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0031EEA0` → [MiMapBackgroundPagesToZero + 0xBC](MiMapBackgroundPagesToZero_function_0031E940.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031EE80  B9 02 00 00 00                  mov ecx, 2
0031EE85  41 2B CE                        sub ecx, r14d
0031EE88  48 C1 EF 09                     shr rdi, 9
0031EE8C  49 23 F8                        and rdi, r8
0031EE8F  48 8B C2                        mov rax, rdx
0031EE92  48 03 F8                        add rdi, rax
0031EE95  48 83 E9 01                     sub rcx, 1
0031EE99  75 ED                           jne 0x14031ee88
0031EE9B  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0031EEA0  E9 57 FB FF FF                  jmp 0x14031e9fc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0031EE80(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 v_rdi;
    unsigned __int64 v_stack_p40;

    a1 = (unsigned int)((2) - ((unsigned int)(v_r14)));
loc_0031EE88:
    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & (a3);
    v_rdi = (v_rdi) + (a2);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_0031EE88;
    v_stack_p40 = v_rdi;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0031EE80(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t local_rdi;
    uint64_t v_stack_p40;

    Arg1 = (uint32_t)((2) - ((uint32_t)(local_r14)));
loc_0031EE88:
    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & (Arg3);
    local_rdi = (local_rdi) + (Arg2);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_0031EE88;
    v_stack_p40 = local_rdi;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031EE80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0031EE80[BB_0031EE80]
  bb_0031EE88[BB_0031EE88]
  bb_0031EE9B[BB_0031EE9B]
  bb_0031EE80 -->|flow| bb_0031EE88
  bb_0031EE88 -->|branch| bb_0031EE88
  bb_0031EE88 -->|fallthrough| bb_0031EE9B
```
