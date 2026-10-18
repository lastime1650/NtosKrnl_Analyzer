# SymCryptFdefIntMulMixedSize

- RVA: `0x0052D88C`–`0x0052D926` (길이 `154` bytes)
- VA: `0x000000014052D88C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084C9C`
- 디코드: `45`개 명령, `154/154` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0052D8C8` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)
- `0x0052D8E4` → [SymCryptFdefRawMul](SymCryptFdefRawMul_function_0052DF1C.md) (function, `0x0052DF1C`)
- `0x0052D907` → [SymCryptWipe](../51/SymCryptWipe_function_0051F914.md) (function, `0x0051F914`)

### Direct callers
- [SymCryptIntMulMixedSize](SymCryptIntMulMixedSize_function_005256F8.md) at `0x00525706`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052D88C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0052D891  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0052D896  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0052D89B  57                              push rdi
0052D89C  41 56                           push r14
0052D89E  41 57                           push r15
0052D8A0  48 83 EC 30                     sub rsp, 0x30
0052D8A4  41 8B 70 04                     mov esi, dword ptr [r8 + 4]
0052D8A8  49 8B E8                        mov rbp, r8
0052D8AB  44 8B 71 04                     mov r14d, dword ptr [rcx + 4]
0052D8AF  44 8B C6                        mov r8d, esi
0052D8B2  44 8B 7A 04                     mov r15d, dword ptr [rdx + 4]
0052D8B6  48 8B DA                        mov rbx, rdx
0052D8B9  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0052D8BE  48 8B F9                        mov rdi, rcx
0052D8C1  41 C1 E0 04                     shl r8d, 4
0052D8C5  49 8B C9                        mov rcx, r9
0052D8C8  E8 83 0C F7 FF                  call 0x14049e550
0052D8CD  48 8D 45 20                     lea rax, [rbp + 0x20]
0052D8D1  45 8B CF                        mov r9d, r15d
0052D8D4  4C 8D 43 20                     lea r8, [rbx + 0x20]
0052D8D8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0052D8DD  48 8D 4F 20                     lea rcx, [rdi + 0x20]
0052D8E1  41 8B D6                        mov edx, r14d
0052D8E4  E8 33 06 00 00                  call 0x14052df1c
0052D8E9  43 8D 04 37                     lea eax, [r15 + r14]
0052D8ED  3B C6                           cmp eax, esi
0052D8EF  73 1B                           jae 0x14052d90c
0052D8F1  41 2B F7                        sub esi, r15d
0052D8F4  C1 E0 04                        shl eax, 4
0052D8F7  41 2B F6                        sub esi, r14d
0052D8FA  48 8D 4D 20                     lea rcx, [rbp + 0x20]
0052D8FE  C1 E6 06                        shl esi, 6
0052D901  8B D6                           mov edx, esi
0052D903  48 8D 0C 81                     lea rcx, [rcx + rax*4]
0052D907  E8 08 20 FF FF                  call 0x14051f914
0052D90C  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0052D911  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0052D916  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0052D91B  48 83 C4 30                     add rsp, 0x30
0052D91F  41 5F                           pop r15
0052D921  41 5E                           pop r14
0052D923  5F                              pop rdi
0052D924  C3                              ret
0052D925  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefIntMulMixedSize(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4))))) << (4));
    result = EmpCheckErrataList(a4, a5, a3, a4);
    v_stack_m28 = a3 + 32;
    result = SymCryptFdefRawMul(a1 + 32, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))), a2 + 32, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))));
    result = (unsigned int)(*(unsigned int *)(a2 + 4)) + (unsigned int)(*(unsigned int *)(a1 + 4)) * 1;
    v_rsi = (unsigned int)(*(unsigned int *)(a3 + 4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)) + (unsigned int)(*(unsigned int *)(a1 + 4)) * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4))))) {
        v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 4))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))));
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4)) + (unsigned int)(*(unsigned int *)(a1 + 4)) * 1) << (4));
        v_rsi = (unsigned int)((v_rsi) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
        a1 = a3 + 32;
        v_rsi = (unsigned int)((v_rsi) << (6));
        a2 = (unsigned int)(v_rsi);
        a1 = a1 + result * 4;
        result = SymCryptWipe(a1, a2, a2 + 32, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))));
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefIntMulMixedSize(void *Arg1, void *Arg2, void *Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4))))) << (4));
    result = EmpCheckErrataList(Arg4, Arg5, Arg3, Arg4);
    v_stack_m28 = Arg3 + 32;
    result = SymCryptFdefRawMul(Arg1 + 32, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))), Arg2 + 32, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))));
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x4)) + (uint32_t)(*(uint32_t *)(arg1 + 0x4)) * 1;
    local_rsi = (uint32_t)(*(uint32_t *)(arg3 + 0x4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)) + (uint32_t)(*(uint32_t *)(arg1 + 0x4)) * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4))))) {
        local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3 + 0x4))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))));
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4)) + (uint32_t)(*(uint32_t *)(arg1 + 0x4)) * 1) << (4));
        local_rsi = (uint32_t)((local_rsi) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
        Arg1 = Arg3 + 32;
        local_rsi = (uint32_t)((local_rsi) << (6));
        Arg2 = (uint32_t)(local_rsi);
        Arg1 = Arg1 + result * 4;
        result = SymCryptWipe(Arg1, Arg2, Arg2 + 32, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))));
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x0 + rax*4` | `64` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052D88C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052D88C[BB_0052D88C]
  bb_0052D8F1[BB_0052D8F1]
  bb_0052D90C[BB_0052D90C]
  bb_0052D925[BB_0052D925]
  bb_0052D88C -->|branch| bb_0052D90C
  bb_0052D88C -->|fallthrough| bb_0052D8F1
  bb_0052D8F1 -->|flow| bb_0052D90C
```
