# PpmIdleInstallConcurrency

- RVA: `0x00485440`–`0x004854B6` (길이 `118` bytes)
- VA: `0x0000000140485440`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078640`
- 디코드: `34`개 명령, `118/118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0048545F` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00485473` → [PpmIdleUpdateConcurrency](PpmIdleUpdateConcurrency_function_004854C0.md) (function, `0x004854C0`)
- `0x004854A8` → [PpmIdleUpdateConcurrency](PpmIdleUpdateConcurrency_function_004854C0.md) (function, `0x004854C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00485440  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00485445  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0048544A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0048544F  57                              push rdi
00485450  48 83 EC 20                     sub rsp, 0x20
00485454  48 8B F1                        mov rsi, rcx
00485457  49 8B F8                        mov rdi, r8
0048545A  33 C9                           xor ecx, ecx
0048545C  48 8B DA                        mov rbx, rdx
0048545F  E8 7C 93 EF FF                  call 0x14037e7e0
00485464  45 33 C9                        xor r9d, r9d
00485467  45 33 C0                        xor r8d, r8d
0048546A  48 8B D0                        mov rdx, rax
0048546D  48 8B CB                        mov rcx, rbx
00485470  48 8B E8                        mov rbp, rax
00485473  E8 48 00 00 00                  call 0x1404854c0
00485478  48 89 9E F8 89 00 00            mov qword ptr [rsi + 0x89f8], rbx
0048547F  48 85 FF                        test rdi, rdi
00485482  75 18                           jne 0x14048549c
00485484  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00485489  33 C0                           xor eax, eax
0048548B  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00485490  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00485495  48 83 C4 20                     add rsp, 0x20
00485499  5F                              pop rdi
0048549A  C3                              ret
0048549B  CC                              int3
0048549C  45 33 C9                        xor r9d, r9d
0048549F  45 33 C0                        xor r8d, r8d
004854A2  48 8B D5                        mov rdx, rbp
004854A5  48 8B CF                        mov rcx, rdi
004854A8  E8 13 00 00 00                  call 0x1404854c0
004854AD  48 89 BE 00 8A 00 00            mov qword ptr [rsi + 0x8a00], rdi
004854B4  EB CE                           jmp 0x140485484
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmIdleInstallConcurrency(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    a4 = 0;
    a3 = 0;
    result = PpmIdleUpdateConcurrency(a2, result, a3, a4);
    *(unsigned __int64 *)(a1 + 35320) = a2;
    if (0 != 0) goto loc_0048549C;
loc_00485484:
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
loc_0048549C:
    a4 = 0;
    a3 = 0;
    result = PpmIdleUpdateConcurrency(0, v_stack_p10, a3, a4);
    *(unsigned __int64 *)(v_stack_p18 + 35328) = 0;
    goto loc_00485484;
}
```

## 5. (Beta) C Style

```c
int64_t PpmIdleInstallConcurrency(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = PpmIdleUpdateConcurrency(Arg2, result, Arg3, Arg4);
    *(uint64_t *)(arg1 + 0x89F8) = Arg2;
    if (0 != 0) goto loc_0048549C;
loc_00485484:
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
loc_0048549C:
    Arg4 = 0;
    Arg3 = 0;
    result = PpmIdleUpdateConcurrency(0, v_stack_p10, Arg3, Arg4);
    *(uint64_t *)(v_stack_p18 + 0x8A00) = 0;
    goto loc_00485484;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x89F8` | `64` | `W` |
| `Arg1` | `+ 0x8A00` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00485440&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00485440[BB_00485440]
  bb_00485484[BB_00485484]
  bb_0048549B[BB_0048549B]
  bb_0048549C[BB_0048549C]
  bb_00485440 -->|branch| bb_0048549C
  bb_00485440 -->|fallthrough| bb_00485484
  bb_0048549B -->|flow| bb_0048549C
  bb_0048549C -->|branch| bb_00485484
```
