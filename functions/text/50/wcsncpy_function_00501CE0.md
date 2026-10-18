# wcsncpy

- RVA: `0x00501CE0`–`0x00501D58` (길이 `120` bytes)
- VA: `0x0000000140501CE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F3F8`
- 디코드: `35`개 명령, `120/120` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00501D08` → [wcsnlen](wcsnlen_function_00501D60.md) (function, `0x00501D60`)
- `0x00501D1D` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00501D34` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00501CE0  48 8B C4                        mov rax, rsp
00501CE3  48 89 58 08                     mov qword ptr [rax + 8], rbx
00501CE7  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00501CEB  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00501CEF  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
00501CF3  41 57                           push r15
00501CF5  48 83 EC 20                     sub rsp, 0x20
00501CF9  48 8B DA                        mov rbx, rdx
00501CFC  48 8B F1                        mov rsi, rcx
00501CFF  48 8B CB                        mov rcx, rbx
00501D02  49 8B D0                        mov rdx, r8
00501D05  49 8B F8                        mov rdi, r8
00501D08  E8 53 00 00 00                  call 0x140501d60
00501D0D  48 8B D3                        mov rdx, rbx
00501D10  48 8B CE                        mov rcx, rsi
00501D13  4C 8B F0                        mov r14, rax
00501D16  4C 8D 3C 00                     lea r15, [rax + rax]
00501D1A  4D 8B C7                        mov r8, r15
00501D1D  E8 1E 4B 1C 00                  call 0x1406c6840
00501D22  4C 3B F7                        cmp r14, rdi
00501D25  73 12                           jae 0x140501d39
00501D27  49 2B FE                        sub rdi, r14
00501D2A  49 8D 0C 37                     lea rcx, [r15 + rsi]
00501D2E  33 D2                           xor edx, edx
00501D30  4C 8D 04 3F                     lea r8, [rdi + rdi]
00501D34  E8 07 4F 1C 00                  call 0x1406c6c40
00501D39  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00501D3E  48 8B C6                        mov rax, rsi
00501D41  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00501D46  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00501D4B  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00501D50  48 83 C4 20                     add rsp, 0x20
00501D54  41 5F                           pop r15
00501D56  C3                              ret
00501D57  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall wcsncpy(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (32);
    result = wcsnlen(a2, a3, a3, a4);
    result = memcpy(a1, a2, result + result * 1, a4);
    v_rdi = a3;
    if (result < a3) {
        v_rdi = (a3) - (result);
        a1 = result + result * 1 + a1 * 1;
        a2 = 0;
        a3 = v_rdi + v_rdi * 1;
        result = memset(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return a1;
}
```

## 5. (Beta) C Style

```c
int64_t wcsncpy(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (32);
    result = wcsnlen(Arg2, Arg3, Arg3, a4);
    result = memcpy(Arg1, Arg2, result + result * 1, a4);
    local_rdi = Arg3;
    if (result < Arg3) {
        local_rdi = (Arg3) - (result);
        Arg1 = result + result * 1 + Arg1 * 1;
        Arg2 = 0;
        Arg3 = local_rdi + local_rdi * 1;
        result = memset(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return Arg1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0 + rdi*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00501CE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00501CE0[BB_00501CE0]
  bb_00501D27[BB_00501D27]
  bb_00501D39[BB_00501D39]
  bb_00501D57[BB_00501D57]
  bb_00501CE0 -->|branch| bb_00501D39
  bb_00501CE0 -->|fallthrough| bb_00501D27
  bb_00501D27 -->|flow| bb_00501D39
```
