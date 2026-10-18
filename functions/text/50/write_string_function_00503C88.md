# write_string

- RVA: `0x00503C88`–`0x00503CF3` (길이 `107` bytes)
- VA: `0x0000000140503C88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006F978`
- 디코드: `35`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00503CCB` → [write_char](write_char_function_00503BE0.md) (function, `0x00503BE0`)

### Direct callers
- [output_l](output_l_function_00503368.md) at `0x00503891`
- [output_l](output_l_function_00503368.md) at `0x00503909`
- [output_l](output_l_function_00503368.md) at `0x0050392F`
- [output_s](output_s_function_00506854.md) at `0x00506D8C`
- [output_s](output_s_function_00506854.md) at `0x00506E05`
- [output_s](output_s_function_00506854.md) at `0x00506E2D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00503C88  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00503C8D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00503C92  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00503C97  41 56                           push r14
00503C99  48 83 EC 20                     sub rsp, 0x20
00503C9D  41 8B 40 18                     mov eax, dword ptr [r8 + 0x18]
00503CA1  49 8B F9                        mov rdi, r9
00503CA4  49 8B F0                        mov rsi, r8
00503CA7  8B DA                           mov ebx, edx
00503CA9  4C 8B F1                        mov r14, rcx
00503CAC  A8 40                           test al, 0x40
00503CAE  74 0C                           je 0x140503cbc
00503CB0  49 83 78 10 00                  cmp qword ptr [r8 + 0x10], 0
00503CB5  75 05                           jne 0x140503cbc
00503CB7  41 01 11                        add dword ptr [r9], edx
00503CBA  EB 20                           jmp 0x140503cdc
00503CBC  85 D2                           test edx, edx
00503CBE  7E 1C                           jle 0x140503cdc
00503CC0  41 8A 0E                        mov cl, byte ptr [r14]
00503CC3  4C 8B C7                        mov r8, rdi
00503CC6  48 8B D6                        mov rdx, rsi
00503CC9  FF CB                           dec ebx
00503CCB  E8 10 FF FF FF                  call 0x140503be0
00503CD0  49 FF C6                        inc r14
00503CD3  83 3F FF                        cmp dword ptr [rdi], -1
00503CD6  74 04                           je 0x140503cdc
00503CD8  85 DB                           test ebx, ebx
00503CDA  7F E4                           jg 0x140503cc0
00503CDC  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00503CE1  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00503CE6  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00503CEB  48 83 C4 20                     add rsp, 0x20
00503CEF  41 5E                           pop r14
00503CF1  C3                              ret
00503CF2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall write_string(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (32);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 24)))) & (64)) == 0) goto loc_00503CBC;
    if ((*(unsigned __int64 *)(a3 + 16)) != 0) goto loc_00503CBC;
    goto loc_00503CDC;
loc_00503CBC:
    if (condition_is_less_or_equal) goto loc_00503CDC;
loc_00503CC0:
    v_rbx = (unsigned int)(((unsigned int)(a2)) - 1);
    result = write_char(*(unsigned __int8 *)(a1), a3, a4, a4);
    v_r14 = (a1) + 1;
    if ((*(unsigned int *)(a4)) == -1) goto loc_00503CDC;
    if (condition_is_greater) goto loc_00503CC0;
loc_00503CDC:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t write_string(int64_t Arg1, int32_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (32);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x18)))) & (64)) == 0) goto loc_00503CBC;
    if ((*(uint64_t *)(arg3 + 0x10)) != 0) goto loc_00503CBC;
    goto loc_00503CDC;
loc_00503CBC:
    if (condition_is_less_or_equal) goto loc_00503CDC;
loc_00503CC0:
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) - 1);
    result = write_char(*(uint8_t *)(Arg1), Arg3, Arg4, Arg4);
    local_r14 = (Arg1) + 1;
    if ((*(uint32_t *)(arg4)) == -1) goto loc_00503CDC;
    if (condition_is_greater) goto loc_00503CC0;
loc_00503CDC:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00503C88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00503C88[BB_00503C88]
  bb_00503CB0[BB_00503CB0]
  bb_00503CB7[BB_00503CB7]
  bb_00503CBC[BB_00503CBC]
  bb_00503CC0[BB_00503CC0]
  bb_00503CD8[BB_00503CD8]
  bb_00503CDC[BB_00503CDC]
  bb_00503CF2[BB_00503CF2]
  bb_00503C88 -->|branch| bb_00503CBC
  bb_00503C88 -->|fallthrough| bb_00503CB0
  bb_00503CB0 -->|branch| bb_00503CBC
  bb_00503CB0 -->|fallthrough| bb_00503CB7
  bb_00503CB7 -->|branch| bb_00503CDC
  bb_00503CBC -->|branch| bb_00503CDC
  bb_00503CBC -->|fallthrough| bb_00503CC0
  bb_00503CC0 -->|branch| bb_00503CDC
  bb_00503CC0 -->|fallthrough| bb_00503CD8
  bb_00503CD8 -->|branch| bb_00503CC0
  bb_00503CD8 -->|fallthrough| bb_00503CDC
```
