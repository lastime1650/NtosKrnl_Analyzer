# DifIoIsWdmVersionAvailableWrapper

- RVA: `0x0062B760`–`0x0062B8C0` (길이 `352` bytes)
- VA: `0x000000014062B760`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084C9C`
- 디코드: `97`개 명령, `352/352` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062B78A` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062B7B2` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062B7E5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062B80C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062B825` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062B830` → [IoIsWdmVersionAvailable](../../page/A8/IoIsWdmVersionAvailable_function_00A878E0.md) (function, `0x00A878E0`)
- `0x0062B85D` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062B884` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062B89D` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062B7C4` → RVA `0x00F048B8` (`.data`; read)
- `0x0062B7D2` → RVA `0x00F04980` (`.data`; read)
- `0x0062B7DE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062B830` → [IoIsWdmVersionAvailable](../../page/A8/IoIsWdmVersionAvailable_function_00A878E0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062B760  48 8B C4                        mov rax, rsp
0062B763  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062B767  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062B76B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062B76F  57                              push rdi
0062B770  41 56                           push r14
0062B772  41 57                           push r15
0062B774  48 83 EC 30                     sub rsp, 0x30
0062B778  44 8A F9                        mov r15b, cl
0062B77B  0F 57 C0                        xorps xmm0, xmm0
0062B77E  B9 47 01 00 00                  mov ecx, 0x147
0062B783  44 8A F2                        mov r14b, dl
0062B786  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062B78A  E8 A5 A2 E6 FF                  call 0x140495a34
0062B78F  48 8B F0                        mov rsi, rax
0062B792  48 85 C0                        test rax, rax
0062B795  0F 84 8F 00 00 00               je 0x14062b82a
0062B79B  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062B79E  A8 18                           test al, 0x18
0062B7A0  74 0C                           je 0x14062b7ae
0062B7A2  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062B7A7  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062B7AC  EB 0E                           jmp 0x14062b7bc
0062B7AE  A8 04                           test al, 4
0062B7B0  74 0A                           je 0x14062b7bc
0062B7B2  E8 51 84 EA FF                  call 0x1404d3c08
0062B7B7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062B7BC  40 32 ED                        xor bpl, bpl
0062B7BF  44 88 7C 24 29                  mov byte ptr [rsp + 0x29], r15b
0062B7C4  40 38 2D ED 90 8D 00            cmp byte ptr [rip + 0x8d90ed], bpl
0062B7CB  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
0062B7D0  75 0C                           jne 0x14062b7de
0062B7D2  F7 05 A4 91 8D 00 00 08 00 00   test dword ptr [rip + 0x8d91a4], 0x800
0062B7DC  74 13                           je 0x14062b7f1
0062B7DE  48 8D 0D 9B 86 8D 00            lea rcx, [rip + 0x8d869b]
0062B7E5  E8 36 AE BE FF                  call 0x140216620
0062B7EA  40 8A E8                        mov bpl, al
0062B7ED  84 C0                           test al, al
0062B7EF  74 39                           je 0x14062b82a
0062B7F1  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062B7F5  48 8B 1F                        mov rbx, qword ptr [rdi]
0062B7F8  EB 1A                           jmp 0x14062b814
0062B7FA  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062B7FE  48 85 C0                        test rax, rax
0062B801  74 0E                           je 0x14062b811
0062B803  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062B807  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062B80C  E8 BF F2 08 00                  call 0x1406baad0
0062B811  48 8B 1B                        mov rbx, qword ptr [rbx]
0062B814  48 3B DF                        cmp rbx, rdi
0062B817  75 E1                           jne 0x14062b7fa
0062B819  40 84 ED                        test bpl, bpl
0062B81C  74 0C                           je 0x14062b82a
0062B81E  48 8D 0D 5B 86 8D 00            lea rcx, [rip + 0x8d865b]
0062B825  E8 56 E6 D1 FF                  call 0x140349e80
0062B82A  41 8A D6                        mov dl, r14b
0062B82D  41 8A CF                        mov cl, r15b
0062B830  E8 AB C0 45 00                  call 0x140a878e0
0062B835  88 44 24 2A                     mov byte ptr [rsp + 0x2a], al
0062B839  48 85 F6                        test rsi, rsi
0062B83C  74 64                           je 0x14062b8a2
0062B83E  40 32 FF                        xor dil, dil
0062B841  40 38 3D 70 90 8D 00            cmp byte ptr [rip + 0x8d9070], dil
0062B848  75 0C                           jne 0x14062b856
0062B84A  F7 05 2C 91 8D 00 00 08 00 00   test dword ptr [rip + 0x8d912c], 0x800
0062B854  74 13                           je 0x14062b869
0062B856  48 8D 0D 23 86 8D 00            lea rcx, [rip + 0x8d8623]
0062B85D  E8 BE AD BE FF                  call 0x140216620
0062B862  40 8A F8                        mov dil, al
0062B865  84 C0                           test al, al
0062B867  74 39                           je 0x14062b8a2
0062B869  48 83 C6 30                     add rsi, 0x30
0062B86D  48 8B 1E                        mov rbx, qword ptr [rsi]
0062B870  EB 1A                           jmp 0x14062b88c
0062B872  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062B876  48 85 C0                        test rax, rax
0062B879  74 0E                           je 0x14062b889
0062B87B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062B87F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062B884  E8 47 F2 08 00                  call 0x1406baad0
0062B889  48 8B 1B                        mov rbx, qword ptr [rbx]
0062B88C  48 3B DE                        cmp rbx, rsi
0062B88F  75 E1                           jne 0x14062b872
0062B891  40 84 FF                        test dil, dil
0062B894  74 0C                           je 0x14062b8a2
0062B896  48 8D 0D E3 85 8D 00            lea rcx, [rip + 0x8d85e3]
0062B89D  E8 DE E5 D1 FF                  call 0x140349e80
0062B8A2  8A 44 24 2A                     mov al, byte ptr [rsp + 0x2a]
0062B8A6  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062B8AB  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062B8B0  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0062B8B5  48 83 C4 30                     add rsp, 0x30
0062B8B9  41 5F                           pop r15
0062B8BB  41 5E                           pop r14
0062B8BD  5F                              pop rdi
0062B8BE  C3                              ret
0062B8BF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoIsWdmVersionAvailableWrapper(unsigned __int8 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m1E;
    unsigned __int8 v_stack_m1F;
    unsigned __int8 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(327, a2, a3, a4);
    if (result == 0) goto loc_0062B82A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062B7AE;
    v_stack_m28 = v_stack_p0;
    goto loc_0062B7BC;
loc_0062B7AE:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rbp = 0;
    v_stack_m1F = a1;
    v_stack_m20 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9277677)) != 0) goto loc_0062B7DE;
    if (((*(unsigned int *)(v_rip + 9277860)) & (0x800ULL)) == 0) goto loc_0062B7F1;
loc_0062B7DE:
    result = ExAcquireRundownProtection(v_rip + 9275035, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062B82A;
loc_0062B7F1:
    goto loc_0062B814;
loc_0062B7FA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062B814:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062B7FA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9274971;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoIsWdmVersionAvailable(a1, a2, a3, a4);
    v_stack_m1E = (unsigned __int8)(result);
    if (result == 0) goto loc_0062B8A2;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9277552)) != 0) goto loc_0062B856;
    if (((*(unsigned int *)(v_rip + 9277740)) & (0x800ULL)) == 0) goto loc_0062B869;
loc_0062B856:
    result = ExAcquireRundownProtection(v_rip + 9274915, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062B8A2;
loc_0062B869:
    v_rsi = (result) + (48);
    goto loc_0062B88C;
loc_0062B872:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062B88C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062B872;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9274851;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return v_stack_m1E;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoIsWdmVersionAvailableWrapper(uint8_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m1E;
    uint8_t v_stack_m1F;
    uint8_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(327, Arg2, a3, a4);
    if (result == 0) goto loc_0062B82A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062B7AE;
    v_stack_m28 = v_stack_p0;
    goto loc_0062B7BC;
loc_0062B7AE:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m28 = result;
    }
    local_rbp = 0;
    v_stack_m1F = Arg1;
    v_stack_m20 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8D90ED)) != 0) goto loc_0062B7DE;
    if (((*(uint32_t *)(v_rip + 0x8D91A4)) & (0x800ULL)) == 0) goto loc_0062B7F1;
loc_0062B7DE:
    result = ExAcquireRundownProtection(v_rip + 9275035, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062B82A;
loc_0062B7F1:
    goto loc_0062B814;
loc_0062B7FA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062B814:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062B7FA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9274971;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = IoIsWdmVersionAvailable(Arg1, Arg2, a3, a4);
    v_stack_m1E = (uint8_t)(result);
    if (result == 0) goto loc_0062B8A2;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D9070)) != 0) goto loc_0062B856;
    if (((*(uint32_t *)(v_rip + 0x8D912C)) & (0x800ULL)) == 0) goto loc_0062B869;
loc_0062B856:
    result = ExAcquireRundownProtection(v_rip + 9274915, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062B8A2;
loc_0062B869:
    local_rsi = (result) + (48);
    goto loc_0062B88C;
loc_0062B872:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062B88C:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062B872;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9274851;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return v_stack_m1E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062B760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062B760[BB_0062B760]
  bb_0062B79B[BB_0062B79B]
  bb_0062B7A2[BB_0062B7A2]
  bb_0062B7AE[BB_0062B7AE]
  bb_0062B7B2[BB_0062B7B2]
  bb_0062B7BC[BB_0062B7BC]
  bb_0062B7D2[BB_0062B7D2]
  bb_0062B7DE[BB_0062B7DE]
  bb_0062B7F1[BB_0062B7F1]
  bb_0062B7FA[BB_0062B7FA]
  bb_0062B803[BB_0062B803]
  bb_0062B811[BB_0062B811]
  bb_0062B814[BB_0062B814]
  bb_0062B819[BB_0062B819]
  bb_0062B81E[BB_0062B81E]
  bb_0062B82A[BB_0062B82A]
  bb_0062B83E[BB_0062B83E]
  bb_0062B84A[BB_0062B84A]
  bb_0062B856[BB_0062B856]
  bb_0062B869[BB_0062B869]
  bb_0062B872[BB_0062B872]
  bb_0062B87B[BB_0062B87B]
  bb_0062B889[BB_0062B889]
  bb_0062B88C[BB_0062B88C]
  bb_0062B891[BB_0062B891]
  bb_0062B896[BB_0062B896]
  bb_0062B8A2[BB_0062B8A2]
  bb_0062B8BF[BB_0062B8BF]
  bb_0062B760 -->|branch| bb_0062B82A
  bb_0062B760 -->|fallthrough| bb_0062B79B
  bb_0062B79B -->|branch| bb_0062B7AE
  bb_0062B79B -->|fallthrough| bb_0062B7A2
  bb_0062B7A2 -->|branch| bb_0062B7BC
  bb_0062B7AE -->|branch| bb_0062B7BC
  bb_0062B7AE -->|fallthrough| bb_0062B7B2
  bb_0062B7B2 -->|flow| bb_0062B7BC
  bb_0062B7BC -->|branch| bb_0062B7DE
  bb_0062B7BC -->|fallthrough| bb_0062B7D2
  bb_0062B7D2 -->|branch| bb_0062B7F1
  bb_0062B7D2 -->|fallthrough| bb_0062B7DE
  bb_0062B7DE -->|branch| bb_0062B82A
  bb_0062B7DE -->|fallthrough| bb_0062B7F1
  bb_0062B7F1 -->|branch| bb_0062B814
  bb_0062B7FA -->|branch| bb_0062B811
  bb_0062B7FA -->|fallthrough| bb_0062B803
  bb_0062B803 -->|flow| bb_0062B811
  bb_0062B811 -->|flow| bb_0062B814
  bb_0062B814 -->|branch| bb_0062B7FA
  bb_0062B814 -->|fallthrough| bb_0062B819
  bb_0062B819 -->|branch| bb_0062B82A
  bb_0062B819 -->|fallthrough| bb_0062B81E
  bb_0062B81E -->|flow| bb_0062B82A
  bb_0062B82A -->|branch| bb_0062B8A2
  bb_0062B82A -->|fallthrough| bb_0062B83E
  bb_0062B83E -->|branch| bb_0062B856
  bb_0062B83E -->|fallthrough| bb_0062B84A
  bb_0062B84A -->|branch| bb_0062B869
  bb_0062B84A -->|fallthrough| bb_0062B856
  bb_0062B856 -->|branch| bb_0062B8A2
  bb_0062B856 -->|fallthrough| bb_0062B869
  bb_0062B869 -->|branch| bb_0062B88C
  bb_0062B872 -->|branch| bb_0062B889
  bb_0062B872 -->|fallthrough| bb_0062B87B
  bb_0062B87B -->|flow| bb_0062B889
  bb_0062B889 -->|flow| bb_0062B88C
  bb_0062B88C -->|branch| bb_0062B872
  bb_0062B88C -->|fallthrough| bb_0062B891
  bb_0062B891 -->|branch| bb_0062B8A2
  bb_0062B891 -->|fallthrough| bb_0062B896
  bb_0062B896 -->|flow| bb_0062B8A2
```
