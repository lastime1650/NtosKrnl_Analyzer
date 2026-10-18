# SymCryptMontgomeryDoubleAndAdd

- RVA: `0x0053A5AC`–`0x0053A866` (길이 `698` bytes)
- VA: `0x000000014053A5AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00095AEC`
- 디코드: `170`개 명령, `698/698` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0053A609` → [SymCryptModAdd](../52/SymCryptModAdd_function_00525868.md) (function, `0x00525868`)
- `0x0053A624` → [SymCryptModSub](../52/SymCryptModSub_function_00525CB8.md) (function, `0x00525CB8`)
- `0x0053A654` → [SymCryptModAdd](../52/SymCryptModAdd_function_00525868.md) (function, `0x00525868`)
- `0x0053A67C` → [SymCryptModSub](../52/SymCryptModSub_function_00525CB8.md) (function, `0x00525CB8`)
- `0x0053A6A4` → [SymCryptModMul](../52/SymCryptModMul_function_00525BA8.md) (function, `0x00525BA8`)
- `0x0053A6C7` → [SymCryptModMul](../52/SymCryptModMul_function_00525BA8.md) (function, `0x00525BA8`)
- `0x0053A6E2` → [SymCryptModSquare](../52/SymCryptModSquare_function_00525C84.md) (function, `0x00525C84`)
- `0x0053A6FD` → [SymCryptModSquare](../52/SymCryptModSquare_function_00525C84.md) (function, `0x00525C84`)
- `0x0053A720` → [SymCryptModSub](../52/SymCryptModSub_function_00525CB8.md) (function, `0x00525CB8`)
- `0x0053A743` → [SymCryptModMul](../52/SymCryptModMul_function_00525BA8.md) (function, `0x00525BA8`)
- `0x0053A766` → [SymCryptModMul](../52/SymCryptModMul_function_00525BA8.md) (function, `0x00525BA8`)
- `0x0053A781` → [SymCryptModAdd](../52/SymCryptModAdd_function_00525868.md) (function, `0x00525868`)
- `0x0053A79C` → [SymCryptModMul](../52/SymCryptModMul_function_00525BA8.md) (function, `0x00525BA8`)
- `0x0053A7BF` → [SymCryptModAdd](../52/SymCryptModAdd_function_00525868.md) (function, `0x00525868`)
- `0x0053A7DA` → [SymCryptModSub](../52/SymCryptModSub_function_00525CB8.md) (function, `0x00525CB8`)
- `0x0053A7F0` → [SymCryptModSquare](../52/SymCryptModSquare_function_00525C84.md) (function, `0x00525C84`)
- `0x0053A818` → [SymCryptModMul](../52/SymCryptModMul_function_00525BA8.md) (function, `0x00525BA8`)
- `0x0053A82E` → [SymCryptModSquare](../52/SymCryptModSquare_function_00525C84.md) (function, `0x00525C84`)
- `0x0053A84B` → [SymCryptModMul](../52/SymCryptModMul_function_00525BA8.md) (function, `0x00525BA8`)

### Direct callers
- [SymCryptMontgomeryPointScalarMul](SymCryptMontgomeryPointScalarMul_function_0053AB50.md) at `0x0053AE3F`
- [SymCryptMontgomeryPointScalarMul](SymCryptMontgomeryPointScalarMul_function_0053AB50.md) at `0x0053AEE8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053A5AC  48 8B C4                        mov rax, rsp
0053A5AF  48 89 58 08                     mov qword ptr [rax + 8], rbx
0053A5B3  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0053A5B7  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0053A5BB  55                              push rbp
0053A5BC  56                              push rsi
0053A5BD  57                              push rdi
0053A5BE  41 54                           push r12
0053A5C0  41 55                           push r13
0053A5C2  41 56                           push r14
0053A5C4  41 57                           push r15
0053A5C6  48 83 EC 30                     sub rsp, 0x30
0053A5CA  4C 8B AC 24 C8 00 00 00         mov r13, qword ptr [rsp + 0xc8]
0053A5D2  49 8B F1                        mov rsi, r9
0053A5D5  4C 8B B4 24 B0 00 00 00         mov r14, qword ptr [rsp + 0xb0]
0053A5DD  4C 8B E1                        mov r12, rcx
0053A5E0  48 8B AC 24 98 00 00 00         mov rbp, qword ptr [rsp + 0x98]
0053A5E8  4D 8B CE                        mov r9, r14
0053A5EB  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0053A5F3  4C 8B C5                        mov r8, rbp
0053A5F6  48 8B BC 24 C0 00 00 00         mov rdi, qword ptr [rsp + 0xc0]
0053A5FE  48 8B D3                        mov rdx, rbx
0053A601  4C 89 68 C0                     mov qword ptr [rax - 0x40], r13
0053A605  48 89 78 B8                     mov qword ptr [rax - 0x48], rdi
0053A609  E8 5A B2 FE FF                  call 0x140525868
0053A60E  4C 8B CD                        mov r9, rbp
0053A611  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A616  4C 8B C5                        mov r8, rbp
0053A619  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0053A61E  48 8B D3                        mov rdx, rbx
0053A621  49 8B CC                        mov rcx, r12
0053A624  E8 8F B6 FE FF                  call 0x140525cb8
0053A629  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
0053A631  49 8B CC                        mov rcx, r12
0053A634  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
0053A63C  4D 8B C7                        mov r8, r15
0053A63F  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A644  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0053A649  48 8B BC 24 B8 00 00 00         mov rdi, qword ptr [rsp + 0xb8]
0053A651  4C 8B CF                        mov r9, rdi
0053A654  E8 0F B2 FE FF                  call 0x140525868
0053A659  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0053A661  4D 8B CF                        mov r9, r15
0053A664  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
0053A66C  4D 8B C7                        mov r8, r15
0053A66F  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A674  49 8B CC                        mov rcx, r12
0053A677  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0053A67C  E8 37 B6 FE FF                  call 0x140525cb8
0053A681  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0053A689  4C 8B C5                        mov r8, rbp
0053A68C  4C 8B 8C 24 A0 00 00 00         mov r9, qword ptr [rsp + 0xa0]
0053A694  48 8B D7                        mov rdx, rdi
0053A697  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A69C  49 8B CC                        mov rcx, r12
0053A69F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0053A6A4  E8 FF B4 FE FF                  call 0x140525ba8
0053A6A9  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0053A6B1  4D 8B CF                        mov r9, r15
0053A6B4  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A6B9  4D 8B C6                        mov r8, r14
0053A6BC  49 8B D7                        mov rdx, r15
0053A6BF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0053A6C4  49 8B CC                        mov rcx, r12
0053A6C7  E8 DC B4 FE FF                  call 0x140525ba8
0053A6CC  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
0053A6D4  4C 8B C3                        mov r8, rbx
0053A6D7  49 8B D6                        mov rdx, r14
0053A6DA  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0053A6DF  49 8B CC                        mov rcx, r12
0053A6E2  E8 9D B5 FE FF                  call 0x140525c84
0053A6E7  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
0053A6EF  4D 8B C6                        mov r8, r14
0053A6F2  48 8B D5                        mov rdx, rbp
0053A6F5  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0053A6FA  49 8B CC                        mov rcx, r12
0053A6FD  E8 82 B5 FE FF                  call 0x140525c84
0053A702  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0053A70A  4C 8B CF                        mov r9, rdi
0053A70D  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A712  4D 8B C6                        mov r8, r14
0053A715  48 8B D3                        mov rdx, rbx
0053A718  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0053A71D  49 8B CC                        mov rcx, r12
0053A720  E8 93 B5 FE FF                  call 0x140525cb8
0053A725  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0053A72D  4C 8B CB                        mov r9, rbx
0053A730  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A735  4D 8B C6                        mov r8, r14
0053A738  48 8B D3                        mov rdx, rbx
0053A73B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0053A740  49 8B CC                        mov rcx, r12
0053A743  E8 60 B4 FE FF                  call 0x140525ba8
0053A748  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
0053A750  4C 8B CD                        mov r9, rbp
0053A753  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A758  4C 8B C7                        mov r8, rdi
0053A75B  48 8B D6                        mov rdx, rsi
0053A75E  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0053A763  49 8B CC                        mov rcx, r12
0053A766  E8 3D B4 FE FF                  call 0x140525ba8
0053A76B  4C 8B CD                        mov r9, rbp
0053A76E  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A773  4C 8B C5                        mov r8, rbp
0053A776  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0053A77B  49 8B D6                        mov rdx, r14
0053A77E  49 8B CC                        mov rcx, r12
0053A781  E8 E2 B0 FE FF                  call 0x140525868
0053A786  4C 8B CD                        mov r9, rbp
0053A789  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A78E  4C 8B C5                        mov r8, rbp
0053A791  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0053A796  48 8B D7                        mov rdx, rdi
0053A799  49 8B CC                        mov rcx, r12
0053A79C  E8 07 B4 FE FF                  call 0x140525ba8
0053A7A1  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
0053A7A9  4D 8B CE                        mov r9, r14
0053A7AC  4C 8B C7                        mov r8, rdi
0053A7AF  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A7B4  49 8B D7                        mov rdx, r15
0053A7B7  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0053A7BC  49 8B CC                        mov rcx, r12
0053A7BF  E8 A4 B0 FE FF                  call 0x140525868
0053A7C4  4D 8B CF                        mov r9, r15
0053A7C7  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A7CC  4C 8B C7                        mov r8, rdi
0053A7CF  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0053A7D4  49 8B D7                        mov rdx, r15
0053A7D7  49 8B CC                        mov rcx, r12
0053A7DA  E8 D9 B4 FE FF                  call 0x140525cb8
0053A7DF  4C 8B CB                        mov r9, rbx
0053A7E2  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0053A7E7  4C 8B C7                        mov r8, rdi
0053A7EA  49 8B D6                        mov rdx, r14
0053A7ED  49 8B CC                        mov rcx, r12
0053A7F0  E8 8F B4 FE FF                  call 0x140525c84
0053A7F5  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0053A7FD  48 85 C0                        test rax, rax
0053A800  74 1B                           je 0x14053a81d
0053A802  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A807  4C 8B CF                        mov r9, rdi
0053A80A  4C 8B C7                        mov r8, rdi
0053A80D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0053A812  48 8B D0                        mov rdx, rax
0053A815  49 8B CC                        mov rcx, r12
0053A818  E8 8B B3 FE FF                  call 0x140525ba8
0053A81D  4C 8B CB                        mov r9, rbx
0053A820  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0053A825  4D 8B C7                        mov r8, r15
0053A828  49 8B D7                        mov rdx, r15
0053A82B  49 8B CC                        mov rcx, r12
0053A82E  E8 51 B4 FE FF                  call 0x140525c84
0053A833  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0053A838  4D 8B CF                        mov r9, r15
0053A83B  4D 8B C7                        mov r8, r15
0053A83E  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0053A843  49 8B CC                        mov rcx, r12
0053A846  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0053A84B  E8 58 B3 FE FF                  call 0x140525ba8
0053A850  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0053A855  48 83 C4 30                     add rsp, 0x30
0053A859  41 5F                           pop r15
0053A85B  41 5E                           pop r14
0053A85D  41 5D                           pop r13
0053A85F  41 5C                           pop r12
0053A861  5F                              pop rdi
0053A862  5E                              pop rsi
0053A863  5D                              pop rbp
0053A864  C3                              ret
0053A865  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptMontgomeryDoubleAndAdd(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 64) = a12;
    *(unsigned __int64 *)(v_rsp - 72) = a11;
    result = SymCryptModAdd(a1, a5, a6, a9);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModSub(a1, a5, a6, a6);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModAdd(a1, a7, a8, a10);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModSub(a1, a7, a8, a8);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModMul(a1, a10, a6, a7);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModMul(a1, a8, a9, a8);
    v_stack_m48 = a12;
    result = SymCryptModSquare(a1, a9, a5, a11);
    v_stack_m48 = a12;
    result = SymCryptModSquare(a1, a6, a9, a11);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModSub(a1, a5, a9, a10);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModMul(a1, a5, a9, a5);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModMul(a1, a4, a10, a6);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModAdd(a1, a9, a6, a6);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModMul(a1, a10, a6, a6);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModAdd(a1, a8, a7, a9);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModSub(a1, a8, a7, a8);
    v_stack_m48 = a12;
    result = SymCryptModSquare(a1, a9, a7, a11);
    result = v_stack_p18;
    if (v_stack_p18 != 0) {
        v_stack_m40 = a12;
        a4 = a7;
        a3 = a7;
        v_stack_m48 = a11;
        a2 = v_stack_p18;
        a1 = a1;
        result = SymCryptModMul(a1, a2, a3, a4);
    }
    v_stack_m48 = a12;
    result = SymCryptModSquare(a1, a8, a8, a11);
    v_stack_m40 = a12;
    v_stack_m48 = a11;
    result = SymCryptModMul(a1, v_stack_p10, a8, a8);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptMontgomeryDoubleAndAdd(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x40) = Arg12;
    *(uint64_t *)(local_rsp - 0x48) = Arg11;
    result = SymCryptModAdd(Arg1, Arg5, Arg6, Arg9);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModSub(Arg1, Arg5, Arg6, Arg6);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModAdd(Arg1, Arg7, Arg8, Arg10);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModSub(Arg1, Arg7, Arg8, Arg8);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModMul(Arg1, Arg10, Arg6, Arg7);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModMul(Arg1, Arg8, Arg9, Arg8);
    v_stack_m48 = Arg12;
    result = SymCryptModSquare(Arg1, Arg9, Arg5, Arg11);
    v_stack_m48 = Arg12;
    result = SymCryptModSquare(Arg1, Arg6, Arg9, Arg11);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModSub(Arg1, Arg5, Arg9, Arg10);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModMul(Arg1, Arg5, Arg9, Arg5);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModMul(Arg1, Arg4, Arg10, Arg6);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModAdd(Arg1, Arg9, Arg6, Arg6);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModMul(Arg1, Arg10, Arg6, Arg6);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModAdd(Arg1, Arg8, Arg7, Arg9);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModSub(Arg1, Arg8, Arg7, Arg8);
    v_stack_m48 = Arg12;
    result = SymCryptModSquare(Arg1, Arg9, Arg7, Arg11);
    result = v_stack_p18;
    if (v_stack_p18 != 0) {
        v_stack_m40 = Arg12;
        Arg4 = Arg7;
        Arg3 = Arg7;
        v_stack_m48 = Arg11;
        Arg2 = v_stack_p18;
        Arg1 = Arg1;
        result = SymCryptModMul(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m48 = Arg12;
    result = SymCryptModSquare(Arg1, Arg8, Arg8, Arg11);
    v_stack_m40 = Arg12;
    v_stack_m48 = Arg11;
    result = SymCryptModMul(Arg1, v_stack_p10, Arg8, Arg8);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053A5AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0053A5AC[BB_0053A5AC]
  bb_0053A802[BB_0053A802]
  bb_0053A81D[BB_0053A81D]
  bb_0053A865[BB_0053A865]
  bb_0053A5AC -->|branch| bb_0053A81D
  bb_0053A5AC -->|fallthrough| bb_0053A802
  bb_0053A802 -->|flow| bb_0053A81D
```
