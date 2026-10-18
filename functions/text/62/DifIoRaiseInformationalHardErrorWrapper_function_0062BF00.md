# DifIoRaiseInformationalHardErrorWrapper

- RVA: `0x0062BF00`–`0x0062C07A` (길이 `378` bytes)
- VA: `0x000000014062BF00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `103`개 명령, `378/378` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062BF36` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062BF5E` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062BF96` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062BFBD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062BFD6` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062BFE4` → [IoRaiseInformationalHardError](../4B/IoRaiseInformationalHardError_function_004B82B0.md) (function, `0x004B82B0`)
- `0x0062C011` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062C038` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062C051` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062BF70` → RVA `0x00F048B8` (`.data`; read)
- `0x0062BF83` → RVA `0x00F04980` (`.data`; read)
- `0x0062BF8F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062BF00  48 8B C4                        mov rax, rsp
0062BF03  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062BF07  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062BF0B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062BF0F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062BF13  41 54                           push r12
0062BF15  41 56                           push r14
0062BF17  41 57                           push r15
0062BF19  48 83 EC 40                     sub rsp, 0x40
0062BF1D  0F 57 C0                        xorps xmm0, xmm0
0062BF20  44 8B E1                        mov r12d, ecx
0062BF23  B9 42 01 00 00                  mov ecx, 0x142
0062BF28  4D 8B F0                        mov r14, r8
0062BF2B  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062BF2F  4C 8B FA                        mov r15, rdx
0062BF32  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062BF36  E8 F9 9A E6 FF                  call 0x140495a34
0062BF3B  48 8B F0                        mov rsi, rax
0062BF3E  48 85 C0                        test rax, rax
0062BF41  0F 84 94 00 00 00               je 0x14062bfdb
0062BF47  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062BF4A  A8 18                           test al, 0x18
0062BF4C  74 0C                           je 0x14062bf5a
0062BF4E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062BF53  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062BF58  EB 0E                           jmp 0x14062bf68
0062BF5A  A8 04                           test al, 4
0062BF5C  74 0A                           je 0x14062bf68
0062BF5E  E8 A5 7C EA FF                  call 0x1404d3c08
0062BF63  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062BF68  40 32 ED                        xor bpl, bpl
0062BF6B  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
0062BF70  40 38 2D 41 89 8D 00            cmp byte ptr [rip + 0x8d8941], bpl
0062BF77  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062BF7C  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0062BF81  75 0C                           jne 0x14062bf8f
0062BF83  F7 05 F3 89 8D 00 00 08 00 00   test dword ptr [rip + 0x8d89f3], 0x800
0062BF8D  74 13                           je 0x14062bfa2
0062BF8F  48 8D 0D EA 7E 8D 00            lea rcx, [rip + 0x8d7eea]
0062BF96  E8 85 A6 BE FF                  call 0x140216620
0062BF9B  40 8A E8                        mov bpl, al
0062BF9E  84 C0                           test al, al
0062BFA0  74 39                           je 0x14062bfdb
0062BFA2  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062BFA6  48 8B 1F                        mov rbx, qword ptr [rdi]
0062BFA9  EB 1A                           jmp 0x14062bfc5
0062BFAB  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062BFAF  48 85 C0                        test rax, rax
0062BFB2  74 0E                           je 0x14062bfc2
0062BFB4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062BFB8  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062BFBD  E8 0E EB 08 00                  call 0x1406baad0
0062BFC2  48 8B 1B                        mov rbx, qword ptr [rbx]
0062BFC5  48 3B DF                        cmp rbx, rdi
0062BFC8  75 E1                           jne 0x14062bfab
0062BFCA  40 84 ED                        test bpl, bpl
0062BFCD  74 0C                           je 0x14062bfdb
0062BFCF  48 8D 0D AA 7E 8D 00            lea rcx, [rip + 0x8d7eaa]
0062BFD6  E8 A5 DE D1 FF                  call 0x140349e80
0062BFDB  4D 8B C6                        mov r8, r14
0062BFDE  49 8B D7                        mov rdx, r15
0062BFE1  41 8B CC                        mov ecx, r12d
0062BFE4  E8 C7 C2 E8 FF                  call 0x1404b82b0
0062BFE9  88 44 24 3C                     mov byte ptr [rsp + 0x3c], al
0062BFED  48 85 F6                        test rsi, rsi
0062BFF0  74 64                           je 0x14062c056
0062BFF2  40 32 FF                        xor dil, dil
0062BFF5  40 38 3D BC 88 8D 00            cmp byte ptr [rip + 0x8d88bc], dil
0062BFFC  75 0C                           jne 0x14062c00a
0062BFFE  F7 05 78 89 8D 00 00 08 00 00   test dword ptr [rip + 0x8d8978], 0x800
0062C008  74 13                           je 0x14062c01d
0062C00A  48 8D 0D 6F 7E 8D 00            lea rcx, [rip + 0x8d7e6f]
0062C011  E8 0A A6 BE FF                  call 0x140216620
0062C016  40 8A F8                        mov dil, al
0062C019  84 C0                           test al, al
0062C01B  74 39                           je 0x14062c056
0062C01D  48 83 C6 30                     add rsi, 0x30
0062C021  48 8B 1E                        mov rbx, qword ptr [rsi]
0062C024  EB 1A                           jmp 0x14062c040
0062C026  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062C02A  48 85 C0                        test rax, rax
0062C02D  74 0E                           je 0x14062c03d
0062C02F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062C033  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062C038  E8 93 EA 08 00                  call 0x1406baad0
0062C03D  48 8B 1B                        mov rbx, qword ptr [rbx]
0062C040  48 3B DE                        cmp rbx, rsi
0062C043  75 E1                           jne 0x14062c026
0062C045  40 84 FF                        test dil, dil
0062C048  74 0C                           je 0x14062c056
0062C04A  48 8D 0D 2F 7E 8D 00            lea rcx, [rip + 0x8d7e2f]
0062C051  E8 2A DE D1 FF                  call 0x140349e80
0062C056  8A 44 24 3C                     mov al, byte ptr [rsp + 0x3c]
0062C05A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062C05F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062C064  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062C069  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0062C06E  48 83 C4 40                     add rsp, 0x40
0062C072  41 5F                           pop r15
0062C074  41 5E                           pop r14
0062C076  41 5C                           pop r12
0062C078  C3                              ret
0062C079  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoRaiseInformationalHardErrorWrapper(int a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(322, a2, a3, a4);
    if (result == 0) goto loc_0062BFDB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062BF5A;
    v_stack_m38 = v_stack_p0;
    goto loc_0062BF68;
loc_0062BF5A:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = (unsigned int)((unsigned int)(a1));
    v_stack_m28 = a2;
    v_stack_m30 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9275713)) != 0) goto loc_0062BF8F;
    if (((*(unsigned int *)(v_rip + 9275891)) & (0x800ULL)) == 0) goto loc_0062BFA2;
loc_0062BF8F:
    result = ExAcquireRundownProtection(v_rip + 9273066, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062BFDB;
loc_0062BFA2:
    goto loc_0062BFC5;
loc_0062BFAB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062BFC5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062BFAB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9273002;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoRaiseInformationalHardError((unsigned int)((unsigned int)((unsigned int)(a1))), a2, a3, a4);
    v_stack_m1C = (unsigned __int8)(result);
    if (result == 0) goto loc_0062C056;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9275580)) != 0) goto loc_0062C00A;
    if (((*(unsigned int *)(v_rip + 9275768)) & (0x800ULL)) == 0) goto loc_0062C01D;
loc_0062C00A:
    result = ExAcquireRundownProtection(v_rip + 9272943, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062C056;
loc_0062C01D:
    v_rsi = (result) + (48);
    goto loc_0062C040;
loc_0062C026:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062C040:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062C026;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9272879;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m1C;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoRaiseInformationalHardErrorWrapper(int32_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(322, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062BFDB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062BF5A;
    v_stack_m38 = v_stack_p0;
    goto loc_0062BF68;
loc_0062BF5A:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg1));
    v_stack_m28 = Arg2;
    v_stack_m30 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D8941)) != 0) goto loc_0062BF8F;
    if (((*(uint32_t *)(v_rip + 0x8D89F3)) & (0x800ULL)) == 0) goto loc_0062BFA2;
loc_0062BF8F:
    result = ExAcquireRundownProtection(v_rip + 9273066, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062BFDB;
loc_0062BFA2:
    goto loc_0062BFC5;
loc_0062BFAB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062BFC5:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062BFAB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9273002;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = IoRaiseInformationalHardError((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, Arg3, a4);
    v_stack_m1C = (uint8_t)(result);
    if (result == 0) goto loc_0062C056;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D88BC)) != 0) goto loc_0062C00A;
    if (((*(uint32_t *)(v_rip + 0x8D8978)) & (0x800ULL)) == 0) goto loc_0062C01D;
loc_0062C00A:
    result = ExAcquireRundownProtection(v_rip + 9272943, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062C056;
loc_0062C01D:
    local_rsi = (result) + (48);
    goto loc_0062C040;
loc_0062C026:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062C040:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062C026;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9272879;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m1C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062BF00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062BF00[BB_0062BF00]
  bb_0062BF47[BB_0062BF47]
  bb_0062BF4E[BB_0062BF4E]
  bb_0062BF5A[BB_0062BF5A]
  bb_0062BF5E[BB_0062BF5E]
  bb_0062BF68[BB_0062BF68]
  bb_0062BF83[BB_0062BF83]
  bb_0062BF8F[BB_0062BF8F]
  bb_0062BFA2[BB_0062BFA2]
  bb_0062BFAB[BB_0062BFAB]
  bb_0062BFB4[BB_0062BFB4]
  bb_0062BFC2[BB_0062BFC2]
  bb_0062BFC5[BB_0062BFC5]
  bb_0062BFCA[BB_0062BFCA]
  bb_0062BFCF[BB_0062BFCF]
  bb_0062BFDB[BB_0062BFDB]
  bb_0062BFF2[BB_0062BFF2]
  bb_0062BFFE[BB_0062BFFE]
  bb_0062C00A[BB_0062C00A]
  bb_0062C01D[BB_0062C01D]
  bb_0062C026[BB_0062C026]
  bb_0062C02F[BB_0062C02F]
  bb_0062C03D[BB_0062C03D]
  bb_0062C040[BB_0062C040]
  bb_0062C045[BB_0062C045]
  bb_0062C04A[BB_0062C04A]
  bb_0062C056[BB_0062C056]
  bb_0062C079[BB_0062C079]
  bb_0062BF00 -->|branch| bb_0062BFDB
  bb_0062BF00 -->|fallthrough| bb_0062BF47
  bb_0062BF47 -->|branch| bb_0062BF5A
  bb_0062BF47 -->|fallthrough| bb_0062BF4E
  bb_0062BF4E -->|branch| bb_0062BF68
  bb_0062BF5A -->|branch| bb_0062BF68
  bb_0062BF5A -->|fallthrough| bb_0062BF5E
  bb_0062BF5E -->|flow| bb_0062BF68
  bb_0062BF68 -->|branch| bb_0062BF8F
  bb_0062BF68 -->|fallthrough| bb_0062BF83
  bb_0062BF83 -->|branch| bb_0062BFA2
  bb_0062BF83 -->|fallthrough| bb_0062BF8F
  bb_0062BF8F -->|branch| bb_0062BFDB
  bb_0062BF8F -->|fallthrough| bb_0062BFA2
  bb_0062BFA2 -->|branch| bb_0062BFC5
  bb_0062BFAB -->|branch| bb_0062BFC2
  bb_0062BFAB -->|fallthrough| bb_0062BFB4
  bb_0062BFB4 -->|flow| bb_0062BFC2
  bb_0062BFC2 -->|flow| bb_0062BFC5
  bb_0062BFC5 -->|branch| bb_0062BFAB
  bb_0062BFC5 -->|fallthrough| bb_0062BFCA
  bb_0062BFCA -->|branch| bb_0062BFDB
  bb_0062BFCA -->|fallthrough| bb_0062BFCF
  bb_0062BFCF -->|flow| bb_0062BFDB
  bb_0062BFDB -->|branch| bb_0062C056
  bb_0062BFDB -->|fallthrough| bb_0062BFF2
  bb_0062BFF2 -->|branch| bb_0062C00A
  bb_0062BFF2 -->|fallthrough| bb_0062BFFE
  bb_0062BFFE -->|branch| bb_0062C01D
  bb_0062BFFE -->|fallthrough| bb_0062C00A
  bb_0062C00A -->|branch| bb_0062C056
  bb_0062C00A -->|fallthrough| bb_0062C01D
  bb_0062C01D -->|branch| bb_0062C040
  bb_0062C026 -->|branch| bb_0062C03D
  bb_0062C026 -->|fallthrough| bb_0062C02F
  bb_0062C02F -->|flow| bb_0062C03D
  bb_0062C03D -->|flow| bb_0062C040
  bb_0062C040 -->|branch| bb_0062C026
  bb_0062C040 -->|fallthrough| bb_0062C045
  bb_0062C045 -->|branch| bb_0062C056
  bb_0062C045 -->|fallthrough| bb_0062C04A
  bb_0062C04A -->|flow| bb_0062C056
```
