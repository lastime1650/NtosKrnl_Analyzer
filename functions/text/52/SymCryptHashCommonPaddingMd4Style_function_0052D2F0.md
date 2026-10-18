# SymCryptHashCommonPaddingMd4Style

- RVA: `0x0052D2F0`–`0x0052D3AE` (길이 `190` bytes)
- VA: `0x000000014052D2F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C34BC`
- 디코드: `55`개 명령, `190/190` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0052D338` → [SymCryptWipe](../51/SymCryptWipe_function_0051F914.md) (function, `0x0051F914`)
- `0x0052D353` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0052D367` → [SymCryptWipe](../51/SymCryptWipe_function_0051F914.md) (function, `0x0051F914`)
- `0x0052D38E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0052D39B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SymCryptMd5Result](SymCryptMd5Result_function_0052A8B0.md) at `0x0052A8CA`

### Static image references
- `0x0052D2FC` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052D2F0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0052D2F5  55                              push rbp
0052D2F6  56                              push rsi
0052D2F7  57                              push rdi
0052D2F8  48 83 EC 40                     sub rsp, 0x40
0052D2FC  48 8B 05 3D D4 8D 00            mov rax, qword ptr [rip + 0x8dd43d]
0052D303  48 33 C4                        xor rax, rsp
0052D306  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0052D30B  8B 02                           mov eax, dword ptr [rdx]
0052D30D  48 8B DA                        mov rbx, rdx
0052D310  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0052D316  48 8B F9                        mov rdi, rcx
0052D319  BD 40 00 00 00                  mov ebp, 0x40
0052D31E  C6 44 02 20 80                  mov byte ptr [rdx + rax + 0x20], 0x80
0052D323  48 FF C0                        inc rax
0052D326  48 83 F8 38                     cmp rax, 0x38
0052D32A  76 2E                           jbe 0x14052d35a
0052D32C  8B D5                           mov edx, ebp
0052D32E  48 8D 4B 20                     lea rcx, [rbx + 0x20]
0052D332  48 2B D0                        sub rdx, rax
0052D335  48 03 C8                        add rcx, rax
0052D338  E8 D7 25 FF FF                  call 0x14051f914
0052D33D  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
0052D340  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
0052D345  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0052D349  48 8D 53 20                     lea rdx, [rbx + 0x20]
0052D34D  48 03 CB                        add rcx, rbx
0052D350  44 8B C5                        mov r8d, ebp
0052D353  E8 78 D7 18 00                  call 0x1406baad0
0052D358  33 C0                           xor eax, eax
0052D35A  48 8B D5                        mov rdx, rbp
0052D35D  48 8D 4B 20                     lea rcx, [rbx + 0x20]
0052D361  48 2B D0                        sub rdx, rax
0052D364  48 03 C8                        add rcx, rax
0052D367  E8 A8 25 FF FF                  call 0x14051f914
0052D36C  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0052D370  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
0052D375  48 C1 E0 03                     shl rax, 3
0052D379  48 8D 53 20                     lea rdx, [rbx + 0x20]
0052D37D  48 89 43 58                     mov qword ptr [rbx + 0x58], rax
0052D381  4C 8B C5                        mov r8, rbp
0052D384  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
0052D387  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0052D38B  48 03 CB                        add rcx, rbx
0052D38E  E8 3D D7 18 00                  call 0x1406baad0
0052D393  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0052D398  48 33 CC                        xor rcx, rsp
0052D39B  E8 A0 F2 17 00                  call 0x1406ac640
0052D3A0  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0052D3A5  48 83 C4 40                     add rsp, 0x40
0052D3A9  5F                              pop rdi
0052D3AA  5E                              pop rsi
0052D3AB  5D                              pop rbp
0052D3AC  C3                              ret
0052D3AD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptHashCommonPaddingMd4Style(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (64);
    result = (*(unsigned __int64 *)(v_rip + 9294909)) ^ (v_rsp);
    v_stack_m20 = result;
    *(unsigned __int8 *)(a2 + (unsigned int)(*(unsigned int *)(a2)) * 1 + 32) = 128;
    result = ((unsigned int)(*(unsigned int *)(a2))) + 1;
    if (result >= = 56) {
        a2 = 64;
        a1 = a2 + 32;
        a2 = (a2) - (result);
        a1 = (a1) + (result);
        result = SymCryptWipe(a1, a2, a3, a4);
        a1 = *(unsigned int *)(a1 + 52);
        a4 = v_stack_m28;
        result = *(unsigned __int64 *)(a1 + 24);
        a2 = a2 + 32;
        a1 = (a1) + (a2);
        a3 = 64;
        result = guard_dispatch_icall(a1, a2, a3, a4);
        result = 0;
    }
    a2 = (64) - (0);
    a1 = (a2 + 32) + (0);
    result = SymCryptWipe(a1, a2, a3, a4);
    result = (*(unsigned __int64 *)(a2 + 16)) << (3);
    *(unsigned __int64 *)(a2 + 88) = result;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 52))) + (a2);
    result = guard_dispatch_icall(a1, a2 + 32, 64, v_stack_m28);
    a1 = (v_stack_m20) ^ (v_rsp);
    result = _security_check_cookie(a1, a2 + 32, 64, v_stack_m28);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptHashCommonPaddingMd4Style(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (64);
    result = (*(uint64_t *)(v_rip + 0x8DD43D)) ^ (local_rsp);
    v_stack_m20 = result;
    *(uint8_t *)(arg2 + (uint32_t)(*(uint32_t *)(arg2)) * 1 + 0x20) = 128;
    result = ((uint32_t)(*(uint32_t *)(arg2))) + 1;
    if (result >= = 56) {
        Arg2 = 64;
        Arg1 = Arg2 + 32;
        Arg2 = (Arg2) - (result);
        Arg1 = (Arg1) + (result);
        result = SymCryptWipe(Arg1, Arg2, a3, a4);
        Arg1 = *(uint32_t *)(arg1 + 0x34);
        a4 = v_stack_m28;
        result = *(uint64_t *)(arg1 + 0x18);
        Arg2 = Arg2 + 32;
        Arg1 = (Arg1) + (Arg2);
        a3 = 64;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
        result = 0;
    }
    Arg2 = (64) - (0);
    Arg1 = (Arg2 + 32) + (0);
    result = SymCryptWipe(Arg1, Arg2, a3, a4);
    result = (*(uint64_t *)(arg2 + 0x10)) << (3);
    *(uint64_t *)(arg2 + 0x58) = result;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x34))) + (Arg2);
    result = guard_dispatch_icall(Arg1, Arg2 + 32, 64, v_stack_m28);
    Arg1 = (v_stack_m20) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2 + 32, 64, v_stack_m28);
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x34` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x20 + rax*1` | `8` | `W` |
| `Arg2` | `+ 0x58` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052D2F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052D2F0[BB_0052D2F0]
  bb_0052D32C[BB_0052D32C]
  bb_0052D35A[BB_0052D35A]
  bb_0052D3AD[BB_0052D3AD]
  bb_0052D2F0 -->|branch| bb_0052D35A
  bb_0052D2F0 -->|fallthrough| bb_0052D32C
  bb_0052D32C -->|flow| bb_0052D35A
```
