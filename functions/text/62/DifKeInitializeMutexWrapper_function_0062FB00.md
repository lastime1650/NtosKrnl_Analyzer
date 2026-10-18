# DifKeInitializeMutexWrapper

- RVA: `0x0062FB00`–`0x0062FC65` (길이 `357` bytes)
- VA: `0x000000014062FB00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `97`개 명령, `357/357` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062FB31` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062FB59` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062FB8B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062FBB2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062FBCB` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062FBDB` → [KiInitializeMutant](../45/KiInitializeMutant_function_00456E9C.md) (function, `0x00456E9C`)
- `0x0062FC04` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062FC2B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062FC44` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062FB6B` → RVA `0x00F048B8` (`.data`; read)
- `0x0062FB78` → RVA `0x00F04980` (`.data`; read)
- `0x0062FB84` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062FB00  4C 8B DC                        mov r11, rsp
0062FB03  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062FB07  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062FB0B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062FB0F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062FB13  41 56                           push r14
0062FB15  48 83 EC 40                     sub rsp, 0x40
0062FB19  33 C0                           xor eax, eax
0062FB1B  0F 57 C0                        xorps xmm0, xmm0
0062FB1E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062FB23  4C 8B F1                        mov r14, rcx
0062FB26  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062FB2A  B9 19 01 00 00                  mov ecx, 0x119
0062FB2F  8B DA                           mov ebx, edx
0062FB31  E8 FE 5E E6 FF                  call 0x140495a34
0062FB36  48 8B F0                        mov rsi, rax
0062FB39  48 85 C0                        test rax, rax
0062FB3C  0F 84 8E 00 00 00               je 0x14062fbd0
0062FB42  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062FB45  A8 18                           test al, 0x18
0062FB47  74 0C                           je 0x14062fb55
0062FB49  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062FB4E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062FB53  EB 0E                           jmp 0x14062fb63
0062FB55  A8 04                           test al, 4
0062FB57  74 0A                           je 0x14062fb63
0062FB59  E8 AA 40 EA FF                  call 0x1404d3c08
0062FB5E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062FB63  40 32 ED                        xor bpl, bpl
0062FB66  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
0062FB6B  40 38 2D 46 4D 8D 00            cmp byte ptr [rip + 0x8d4d46], bpl
0062FB72  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
0062FB76  75 0C                           jne 0x14062fb84
0062FB78  F7 05 FE 4D 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4dfe], 0x800
0062FB82  74 13                           je 0x14062fb97
0062FB84  48 8D 0D F5 42 8D 00            lea rcx, [rip + 0x8d42f5]
0062FB8B  E8 90 6A BE FF                  call 0x140216620
0062FB90  40 8A E8                        mov bpl, al
0062FB93  84 C0                           test al, al
0062FB95  74 39                           je 0x14062fbd0
0062FB97  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062FB9B  48 8B 1F                        mov rbx, qword ptr [rdi]
0062FB9E  EB 1A                           jmp 0x14062fbba
0062FBA0  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062FBA4  48 85 C0                        test rax, rax
0062FBA7  74 0E                           je 0x14062fbb7
0062FBA9  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062FBAD  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062FBB2  E8 19 AF 08 00                  call 0x1406baad0
0062FBB7  48 8B 1B                        mov rbx, qword ptr [rbx]
0062FBBA  48 3B DF                        cmp rbx, rdi
0062FBBD  75 E1                           jne 0x14062fba0
0062FBBF  40 84 ED                        test bpl, bpl
0062FBC2  74 0C                           je 0x14062fbd0
0062FBC4  48 8D 0D B5 42 8D 00            lea rcx, [rip + 0x8d42b5]
0062FBCB  E8 B0 A2 D1 FF                  call 0x140349e80
0062FBD0  45 33 C9                        xor r9d, r9d
0062FBD3  41 B0 01                        mov r8b, 1
0062FBD6  33 D2                           xor edx, edx
0062FBD8  49 8B CE                        mov rcx, r14
0062FBDB  E8 BC 72 E2 FF                  call 0x140456e9c
0062FBE0  48 85 F6                        test rsi, rsi
0062FBE3  74 64                           je 0x14062fc49
0062FBE5  40 32 FF                        xor dil, dil
0062FBE8  40 38 3D C9 4C 8D 00            cmp byte ptr [rip + 0x8d4cc9], dil
0062FBEF  75 0C                           jne 0x14062fbfd
0062FBF1  F7 05 85 4D 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4d85], 0x800
0062FBFB  74 13                           je 0x14062fc10
0062FBFD  48 8D 0D 7C 42 8D 00            lea rcx, [rip + 0x8d427c]
0062FC04  E8 17 6A BE FF                  call 0x140216620
0062FC09  40 8A F8                        mov dil, al
0062FC0C  84 C0                           test al, al
0062FC0E  74 39                           je 0x14062fc49
0062FC10  48 83 C6 30                     add rsi, 0x30
0062FC14  48 8B 1E                        mov rbx, qword ptr [rsi]
0062FC17  EB 1A                           jmp 0x14062fc33
0062FC19  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062FC1D  48 85 C0                        test rax, rax
0062FC20  74 0E                           je 0x14062fc30
0062FC22  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062FC26  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062FC2B  E8 A0 AE 08 00                  call 0x1406baad0
0062FC30  48 8B 1B                        mov rbx, qword ptr [rbx]
0062FC33  48 3B DE                        cmp rbx, rsi
0062FC36  75 E1                           jne 0x14062fc19
0062FC38  40 84 FF                        test dil, dil
0062FC3B  74 0C                           je 0x14062fc49
0062FC3D  48 8D 0D 3C 42 8D 00            lea rcx, [rip + 0x8d423c]
0062FC44  E8 37 A2 D1 FF                  call 0x140349e80
0062FC49  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062FC4E  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062FC53  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0062FC58  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0062FC5D  48 83 C4 40                     add rsp, 0x40
0062FC61  41 5E                           pop r14
0062FC63  C3                              ret
0062FC64  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeInitializeMutexWrapper(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
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
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(281, a2, a3, a4);
    if (result == 0) goto loc_0062FBD0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062FB55;
    v_stack_m28 = v_stack_p0;
    goto loc_0062FB63;
loc_0062FB55:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rbp = 0;
    v_stack_m18 = a1;
    v_stack_m20 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9260358)) != 0) goto loc_0062FB84;
    if (((*(unsigned int *)(v_rip + 9260542)) & (0x800ULL)) == 0) goto loc_0062FB97;
loc_0062FB84:
    result = ExAcquireRundownProtection(v_rip + 9257717, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062FBD0;
loc_0062FB97:
    goto loc_0062FBBA;
loc_0062FBA0:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062FBBA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062FBA0;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9257653;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    a4 = 0;
    a2 = 0;
    result = KiInitializeMutant(a1, a2, 1, a4);
    if (result == 0) goto loc_0062FC49;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9260233)) != 0) goto loc_0062FBFD;
    if (((*(unsigned int *)(v_rip + 9260421)) & (0x800ULL)) == 0) goto loc_0062FC10;
loc_0062FBFD:
    result = ExAcquireRundownProtection(v_rip + 9257596, a2, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062FC49;
loc_0062FC10:
    v_rsi = (result) + (48);
    goto loc_0062FC33;
loc_0062FC19:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, 1, a4);
    }
loc_0062FC33:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062FC19;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9257532;
        result = ExReleaseRundownProtection(a1, a2, 1, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeInitializeMutexWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
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
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(281, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062FBD0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062FB55;
    v_stack_m28 = v_stack_p0;
    goto loc_0062FB63;
loc_0062FB55:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m28 = result;
    }
    local_rbp = 0;
    v_stack_m18 = Arg1;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8D4D46)) != 0) goto loc_0062FB84;
    if (((*(uint32_t *)(v_rip + 0x8D4DFE)) & (0x800ULL)) == 0) goto loc_0062FB97;
loc_0062FB84:
    result = ExAcquireRundownProtection(v_rip + 9257717, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062FBD0;
loc_0062FB97:
    goto loc_0062FBBA;
loc_0062FBA0:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062FBBA:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062FBA0;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9257653;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    Arg2 = 0;
    result = KiInitializeMutant(Arg1, Arg2, 1, Arg4);
    if (result == 0) goto loc_0062FC49;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D4CC9)) != 0) goto loc_0062FBFD;
    if (((*(uint32_t *)(v_rip + 0x8D4D85)) & (0x800ULL)) == 0) goto loc_0062FC10;
loc_0062FBFD:
    result = ExAcquireRundownProtection(v_rip + 9257596, Arg2, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062FC49;
loc_0062FC10:
    local_rsi = (result) + (48);
    goto loc_0062FC33;
loc_0062FC19:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, 1, Arg4);
    }
loc_0062FC33:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062FC19;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9257532;
        result = ExReleaseRundownProtection(Arg1, Arg2, 1, Arg4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062FB00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062FB00[BB_0062FB00]
  bb_0062FB42[BB_0062FB42]
  bb_0062FB49[BB_0062FB49]
  bb_0062FB55[BB_0062FB55]
  bb_0062FB59[BB_0062FB59]
  bb_0062FB63[BB_0062FB63]
  bb_0062FB78[BB_0062FB78]
  bb_0062FB84[BB_0062FB84]
  bb_0062FB97[BB_0062FB97]
  bb_0062FBA0[BB_0062FBA0]
  bb_0062FBA9[BB_0062FBA9]
  bb_0062FBB7[BB_0062FBB7]
  bb_0062FBBA[BB_0062FBBA]
  bb_0062FBBF[BB_0062FBBF]
  bb_0062FBC4[BB_0062FBC4]
  bb_0062FBD0[BB_0062FBD0]
  bb_0062FBE5[BB_0062FBE5]
  bb_0062FBF1[BB_0062FBF1]
  bb_0062FBFD[BB_0062FBFD]
  bb_0062FC10[BB_0062FC10]
  bb_0062FC19[BB_0062FC19]
  bb_0062FC22[BB_0062FC22]
  bb_0062FC30[BB_0062FC30]
  bb_0062FC33[BB_0062FC33]
  bb_0062FC38[BB_0062FC38]
  bb_0062FC3D[BB_0062FC3D]
  bb_0062FC49[BB_0062FC49]
  bb_0062FC64[BB_0062FC64]
  bb_0062FB00 -->|branch| bb_0062FBD0
  bb_0062FB00 -->|fallthrough| bb_0062FB42
  bb_0062FB42 -->|branch| bb_0062FB55
  bb_0062FB42 -->|fallthrough| bb_0062FB49
  bb_0062FB49 -->|branch| bb_0062FB63
  bb_0062FB55 -->|branch| bb_0062FB63
  bb_0062FB55 -->|fallthrough| bb_0062FB59
  bb_0062FB59 -->|flow| bb_0062FB63
  bb_0062FB63 -->|branch| bb_0062FB84
  bb_0062FB63 -->|fallthrough| bb_0062FB78
  bb_0062FB78 -->|branch| bb_0062FB97
  bb_0062FB78 -->|fallthrough| bb_0062FB84
  bb_0062FB84 -->|branch| bb_0062FBD0
  bb_0062FB84 -->|fallthrough| bb_0062FB97
  bb_0062FB97 -->|branch| bb_0062FBBA
  bb_0062FBA0 -->|branch| bb_0062FBB7
  bb_0062FBA0 -->|fallthrough| bb_0062FBA9
  bb_0062FBA9 -->|flow| bb_0062FBB7
  bb_0062FBB7 -->|flow| bb_0062FBBA
  bb_0062FBBA -->|branch| bb_0062FBA0
  bb_0062FBBA -->|fallthrough| bb_0062FBBF
  bb_0062FBBF -->|branch| bb_0062FBD0
  bb_0062FBBF -->|fallthrough| bb_0062FBC4
  bb_0062FBC4 -->|flow| bb_0062FBD0
  bb_0062FBD0 -->|branch| bb_0062FC49
  bb_0062FBD0 -->|fallthrough| bb_0062FBE5
  bb_0062FBE5 -->|branch| bb_0062FBFD
  bb_0062FBE5 -->|fallthrough| bb_0062FBF1
  bb_0062FBF1 -->|branch| bb_0062FC10
  bb_0062FBF1 -->|fallthrough| bb_0062FBFD
  bb_0062FBFD -->|branch| bb_0062FC49
  bb_0062FBFD -->|fallthrough| bb_0062FC10
  bb_0062FC10 -->|branch| bb_0062FC33
  bb_0062FC19 -->|branch| bb_0062FC30
  bb_0062FC19 -->|fallthrough| bb_0062FC22
  bb_0062FC22 -->|flow| bb_0062FC30
  bb_0062FC30 -->|flow| bb_0062FC33
  bb_0062FC33 -->|branch| bb_0062FC19
  bb_0062FC33 -->|fallthrough| bb_0062FC38
  bb_0062FC38 -->|branch| bb_0062FC49
  bb_0062FC38 -->|fallthrough| bb_0062FC3D
  bb_0062FC3D -->|flow| bb_0062FC49
```
