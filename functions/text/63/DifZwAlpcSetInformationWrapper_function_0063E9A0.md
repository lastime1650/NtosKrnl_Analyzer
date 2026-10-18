# DifZwAlpcSetInformationWrapper

- RVA: `0x0063E9A0`–`0x0063EB25` (길이 `389` bytes)
- VA: `0x000000014063E9A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `112`개 명령, `389/389` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063E9E0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063EA06` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063EA42` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063EA68` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063EA81` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063EA93` → [ZwAlpcSetInformation](../6A/ZwAlpcSetInformation_function_006AE2B0.md) (function, `0x006AE2B0`)
- `0x0063EABF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063EAE5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063EAFE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063EA16` → RVA `0x00F048B8` (`.data`; read)
- `0x0063EA2F` → RVA `0x00F04980` (`.data`; read)
- `0x0063EA3B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063E9A0  48 8B C4                        mov rax, rsp
0063E9A3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0063E9A7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063E9AB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063E9AF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0063E9B3  55                              push rbp
0063E9B4  41 54                           push r12
0063E9B6  41 55                           push r13
0063E9B8  41 56                           push r14
0063E9BA  41 57                           push r15
0063E9BC  48 8B EC                        mov rbp, rsp
0063E9BF  48 83 EC 50                     sub rsp, 0x50
0063E9C3  0F 57 C0                        xorps xmm0, xmm0
0063E9C6  B9 86 00 00 00                  mov ecx, 0x86
0063E9CB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063E9CF  45 8B F9                        mov r15d, r9d
0063E9D2  4D 8B E0                        mov r12, r8
0063E9D5  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063E9D9  44 8B EA                        mov r13d, edx
0063E9DC  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0063E9E0  E8 4F 70 E5 FF                  call 0x140495a34
0063E9E5  48 8B F0                        mov rsi, rax
0063E9E8  48 85 C0                        test rax, rax
0063E9EB  0F 84 95 00 00 00               je 0x14063ea86
0063E9F1  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063E9F4  A8 18                           test al, 0x18
0063E9F6  74 0A                           je 0x14063ea02
0063E9F8  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063E9FC  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063EA00  EB 0D                           jmp 0x14063ea0f
0063EA02  A8 04                           test al, 4
0063EA04  74 09                           je 0x14063ea0f
0063EA06  E8 FD 51 E9 FF                  call 0x1404d3c08
0063EA0B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063EA0F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0063EA13  45 32 F6                        xor r14b, r14b
0063EA16  44 38 35 9B 5E 8C 00            cmp byte ptr [rip + 0x8c5e9b], r14b
0063EA1D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063EA21  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
0063EA25  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063EA29  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0063EA2D  75 0C                           jne 0x14063ea3b
0063EA2F  F7 05 47 5F 8C 00 00 08 00 00   test dword ptr [rip + 0x8c5f47], 0x800
0063EA39  74 13                           je 0x14063ea4e
0063EA3B  48 8D 0D 3E 54 8C 00            lea rcx, [rip + 0x8c543e]
0063EA42  E8 D9 7B BD FF                  call 0x140216620
0063EA47  44 8A F0                        mov r14b, al
0063EA4A  84 C0                           test al, al
0063EA4C  74 38                           je 0x14063ea86
0063EA4E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063EA52  48 8B 1F                        mov rbx, qword ptr [rdi]
0063EA55  EB 19                           jmp 0x14063ea70
0063EA57  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063EA5B  48 85 C0                        test rax, rax
0063EA5E  74 0D                           je 0x14063ea6d
0063EA60  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063EA64  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063EA68  E8 63 C0 07 00                  call 0x1406baad0
0063EA6D  48 8B 1B                        mov rbx, qword ptr [rbx]
0063EA70  48 3B DF                        cmp rbx, rdi
0063EA73  75 E2                           jne 0x14063ea57
0063EA75  45 84 F6                        test r14b, r14b
0063EA78  74 0C                           je 0x14063ea86
0063EA7A  48 8D 0D FF 53 8C 00            lea rcx, [rip + 0x8c53ff]
0063EA81  E8 FA B3 D0 FF                  call 0x140349e80
0063EA86  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0063EA8A  45 8B CF                        mov r9d, r15d
0063EA8D  4D 8B C4                        mov r8, r12
0063EA90  41 8B D5                        mov edx, r13d
0063EA93  E8 18 F8 06 00                  call 0x1406ae2b0
0063EA98  89 45 F8                        mov dword ptr [rbp - 8], eax
0063EA9B  48 85 F6                        test rsi, rsi
0063EA9E  74 63                           je 0x14063eb03
0063EAA0  40 32 FF                        xor dil, dil
0063EAA3  40 38 3D 0E 5E 8C 00            cmp byte ptr [rip + 0x8c5e0e], dil
0063EAAA  75 0C                           jne 0x14063eab8
0063EAAC  F7 05 CA 5E 8C 00 00 08 00 00   test dword ptr [rip + 0x8c5eca], 0x800
0063EAB6  74 13                           je 0x14063eacb
0063EAB8  48 8D 0D C1 53 8C 00            lea rcx, [rip + 0x8c53c1]
0063EABF  E8 5C 7B BD FF                  call 0x140216620
0063EAC4  40 8A F8                        mov dil, al
0063EAC7  84 C0                           test al, al
0063EAC9  74 38                           je 0x14063eb03
0063EACB  48 83 C6 30                     add rsi, 0x30
0063EACF  48 8B 1E                        mov rbx, qword ptr [rsi]
0063EAD2  EB 19                           jmp 0x14063eaed
0063EAD4  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063EAD8  48 85 C0                        test rax, rax
0063EADB  74 0D                           je 0x14063eaea
0063EADD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063EAE1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063EAE5  E8 E6 BF 07 00                  call 0x1406baad0
0063EAEA  48 8B 1B                        mov rbx, qword ptr [rbx]
0063EAED  48 3B DE                        cmp rbx, rsi
0063EAF0  75 E2                           jne 0x14063ead4
0063EAF2  40 84 FF                        test dil, dil
0063EAF5  74 0C                           je 0x14063eb03
0063EAF7  48 8D 0D 82 53 8C 00            lea rcx, [rip + 0x8c5382]
0063EAFE  E8 7D B3 D0 FF                  call 0x140349e80
0063EB03  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0063EB06  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063EB0B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0063EB0F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0063EB13  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0063EB17  49 8B E3                        mov rsp, r11
0063EB1A  41 5F                           pop r15
0063EB1C  41 5E                           pop r14
0063EB1E  41 5D                           pop r13
0063EB20  41 5C                           pop r12
0063EB22  5D                              pop rbp
0063EB23  C3                              ret
0063EB24  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwAlpcSetInformationWrapper(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(134, a2, a3, a4);
    if (result == 0) goto loc_0063EA86;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063EA02;
    v_stack_m58 = v_stack_p0;
    goto loc_0063EA0F;
loc_0063EA02:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9199259)) != 0) goto loc_0063EA3B;
    if (((*(unsigned int *)(v_rip + 9199431)) & (0x800ULL)) == 0) goto loc_0063EA4E;
loc_0063EA3B:
    result = ExAcquireRundownProtection(v_rip + 9196606, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063EA86;
loc_0063EA4E:
    goto loc_0063EA70;
loc_0063EA57:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063EA70:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063EA57;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9196543;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwAlpcSetInformation(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0063EB03;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9199118)) != 0) goto loc_0063EAB8;
    if (((*(unsigned int *)(v_rip + 9199306)) & (0x800ULL)) == 0) goto loc_0063EACB;
loc_0063EAB8:
    result = ExAcquireRundownProtection(v_rip + 9196481, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0063EB03;
loc_0063EACB:
    v_rsi = (result) + (48);
    goto loc_0063EAED;
loc_0063EAD4:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0063EAED:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063EAD4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9196418;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwAlpcSetInformationWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(134, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0063EA86;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063EA02;
    v_stack_m58 = v_stack_p0;
    goto loc_0063EA0F;
loc_0063EA02:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8C5E9B)) != 0) goto loc_0063EA3B;
    if (((*(uint32_t *)(v_rip + 0x8C5F47)) & (0x800ULL)) == 0) goto loc_0063EA4E;
loc_0063EA3B:
    result = ExAcquireRundownProtection(v_rip + 9196606, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063EA86;
loc_0063EA4E:
    goto loc_0063EA70;
loc_0063EA57:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063EA70:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063EA57;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9196543;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwAlpcSetInformation(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0063EB03;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C5E0E)) != 0) goto loc_0063EAB8;
    if (((*(uint32_t *)(v_rip + 0x8C5ECA)) & (0x800ULL)) == 0) goto loc_0063EACB;
loc_0063EAB8:
    result = ExAcquireRundownProtection(v_rip + 9196481, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0063EB03;
loc_0063EACB:
    local_rsi = (result) + (48);
    goto loc_0063EAED;
loc_0063EAD4:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0063EAED:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063EAD4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9196418;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063E9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063E9A0[BB_0063E9A0]
  bb_0063E9F1[BB_0063E9F1]
  bb_0063E9F8[BB_0063E9F8]
  bb_0063EA02[BB_0063EA02]
  bb_0063EA06[BB_0063EA06]
  bb_0063EA0F[BB_0063EA0F]
  bb_0063EA2F[BB_0063EA2F]
  bb_0063EA3B[BB_0063EA3B]
  bb_0063EA4E[BB_0063EA4E]
  bb_0063EA57[BB_0063EA57]
  bb_0063EA60[BB_0063EA60]
  bb_0063EA6D[BB_0063EA6D]
  bb_0063EA70[BB_0063EA70]
  bb_0063EA75[BB_0063EA75]
  bb_0063EA7A[BB_0063EA7A]
  bb_0063EA86[BB_0063EA86]
  bb_0063EAA0[BB_0063EAA0]
  bb_0063EAAC[BB_0063EAAC]
  bb_0063EAB8[BB_0063EAB8]
  bb_0063EACB[BB_0063EACB]
  bb_0063EAD4[BB_0063EAD4]
  bb_0063EADD[BB_0063EADD]
  bb_0063EAEA[BB_0063EAEA]
  bb_0063EAED[BB_0063EAED]
  bb_0063EAF2[BB_0063EAF2]
  bb_0063EAF7[BB_0063EAF7]
  bb_0063EB03[BB_0063EB03]
  bb_0063EB24[BB_0063EB24]
  bb_0063E9A0 -->|branch| bb_0063EA86
  bb_0063E9A0 -->|fallthrough| bb_0063E9F1
  bb_0063E9F1 -->|branch| bb_0063EA02
  bb_0063E9F1 -->|fallthrough| bb_0063E9F8
  bb_0063E9F8 -->|branch| bb_0063EA0F
  bb_0063EA02 -->|branch| bb_0063EA0F
  bb_0063EA02 -->|fallthrough| bb_0063EA06
  bb_0063EA06 -->|flow| bb_0063EA0F
  bb_0063EA0F -->|branch| bb_0063EA3B
  bb_0063EA0F -->|fallthrough| bb_0063EA2F
  bb_0063EA2F -->|branch| bb_0063EA4E
  bb_0063EA2F -->|fallthrough| bb_0063EA3B
  bb_0063EA3B -->|branch| bb_0063EA86
  bb_0063EA3B -->|fallthrough| bb_0063EA4E
  bb_0063EA4E -->|branch| bb_0063EA70
  bb_0063EA57 -->|branch| bb_0063EA6D
  bb_0063EA57 -->|fallthrough| bb_0063EA60
  bb_0063EA60 -->|flow| bb_0063EA6D
  bb_0063EA6D -->|flow| bb_0063EA70
  bb_0063EA70 -->|branch| bb_0063EA57
  bb_0063EA70 -->|fallthrough| bb_0063EA75
  bb_0063EA75 -->|branch| bb_0063EA86
  bb_0063EA75 -->|fallthrough| bb_0063EA7A
  bb_0063EA7A -->|flow| bb_0063EA86
  bb_0063EA86 -->|branch| bb_0063EB03
  bb_0063EA86 -->|fallthrough| bb_0063EAA0
  bb_0063EAA0 -->|branch| bb_0063EAB8
  bb_0063EAA0 -->|fallthrough| bb_0063EAAC
  bb_0063EAAC -->|branch| bb_0063EACB
  bb_0063EAAC -->|fallthrough| bb_0063EAB8
  bb_0063EAB8 -->|branch| bb_0063EB03
  bb_0063EAB8 -->|fallthrough| bb_0063EACB
  bb_0063EACB -->|branch| bb_0063EAED
  bb_0063EAD4 -->|branch| bb_0063EAEA
  bb_0063EAD4 -->|fallthrough| bb_0063EADD
  bb_0063EADD -->|flow| bb_0063EAEA
  bb_0063EAEA -->|flow| bb_0063EAED
  bb_0063EAED -->|branch| bb_0063EAD4
  bb_0063EAED -->|fallthrough| bb_0063EAF2
  bb_0063EAF2 -->|branch| bb_0063EB03
  bb_0063EAF2 -->|fallthrough| bb_0063EAF7
  bb_0063EAF7 -->|flow| bb_0063EB03
```
