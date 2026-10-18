# DifNtOpenFileWrapper

- RVA: `0x00637980`–`0x00637B27` (길이 `423` bytes)
- VA: `0x0000000140637980`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `122`개 명령, `423/423` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006379C6` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006379EE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00637A36` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00637A5C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00637A75` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00637A95` → [NtOpenFile](../../page/8A/NtOpenFile_function_008AB1A0.md) (function, `0x008AB1A0`)
- `0x00637AC1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00637AE7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00637B00` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006379FE` → RVA `0x00F048B8` (`.data`; read)
- `0x00637A23` → RVA `0x00F04980` (`.data`; read)
- `0x00637A2F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00637A95` → [NtOpenFile](../../page/8A/NtOpenFile_function_008AB1A0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00637980  48 8B C4                        mov rax, rsp
00637983  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00637987  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063798B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063798F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00637993  55                              push rbp
00637994  41 54                           push r12
00637996  41 55                           push r13
00637998  41 56                           push r14
0063799A  41 57                           push r15
0063799C  48 8B EC                        mov rbp, rsp
0063799F  48 83 EC 70                     sub rsp, 0x70
006379A3  0F 57 C0                        xorps xmm0, xmm0
006379A6  33 C0                           xor eax, eax
006379A8  B9 CE 00 00 00                  mov ecx, 0xce
006379AD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006379B1  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
006379B5  4D 8B F9                        mov r15, r9
006379B8  4D 8B E0                        mov r12, r8
006379BB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006379BF  44 8B EA                        mov r13d, edx
006379C2  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006379C6  E8 69 E0 E5 FF                  call 0x140495a34
006379CB  4C 8B F0                        mov r14, rax
006379CE  48 85 C0                        test rax, rax
006379D1  0F 84 A3 00 00 00               je 0x140637a7a
006379D7  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
006379DA  F6 C1 18                        test cl, 0x18
006379DD  74 0A                           je 0x1406379e9
006379DF  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006379E3  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
006379E7  EB 0E                           jmp 0x1406379f7
006379E9  F6 C1 04                        test cl, 4
006379EC  74 09                           je 0x1406379f7
006379EE  E8 15 C2 E9 FF                  call 0x1404d3c08
006379F3  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
006379F7  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
006379FB  40 32 F6                        xor sil, sil
006379FE  40 38 35 B3 CE 8C 00            cmp byte ptr [rip + 0x8cceb3], sil
00637A05  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00637A09  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00637A0C  89 45 CC                        mov dword ptr [rbp - 0x34], eax
00637A0F  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00637A12  89 45 C8                        mov dword ptr [rbp - 0x38], eax
00637A15  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00637A19  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00637A1D  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
00637A21  75 0C                           jne 0x140637a2f
00637A23  F7 05 53 CF 8C 00 00 08 00 00   test dword ptr [rip + 0x8ccf53], 0x800
00637A2D  74 13                           je 0x140637a42
00637A2F  48 8D 0D 4A C4 8C 00            lea rcx, [rip + 0x8cc44a]
00637A36  E8 E5 EB BD FF                  call 0x140216620
00637A3B  40 8A F0                        mov sil, al
00637A3E  84 C0                           test al, al
00637A40  74 38                           je 0x140637a7a
00637A42  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00637A46  48 8B 1F                        mov rbx, qword ptr [rdi]
00637A49  EB 19                           jmp 0x140637a64
00637A4B  48 8D 43 F0                     lea rax, [rbx - 0x10]
00637A4F  48 85 C0                        test rax, rax
00637A52  74 0D                           je 0x140637a61
00637A54  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00637A58  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00637A5C  E8 6F 30 08 00                  call 0x1406baad0
00637A61  48 8B 1B                        mov rbx, qword ptr [rbx]
00637A64  48 3B DF                        cmp rbx, rdi
00637A67  75 E2                           jne 0x140637a4b
00637A69  40 84 F6                        test sil, sil
00637A6C  74 0C                           je 0x140637a7a
00637A6E  48 8D 0D 0B C4 8C 00            lea rcx, [rip + 0x8cc40b]
00637A75  E8 06 24 D1 FF                  call 0x140349e80
00637A7A  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00637A7D  4D 8B CF                        mov r9, r15
00637A80  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00637A84  4D 8B C4                        mov r8, r12
00637A87  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00637A8B  41 8B D5                        mov edx, r13d
00637A8E  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00637A91  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00637A95  E8 06 37 27 00                  call 0x1408ab1a0
00637A9A  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00637A9D  4D 85 F6                        test r14, r14
00637AA0  74 63                           je 0x140637b05
00637AA2  40 32 FF                        xor dil, dil
00637AA5  40 38 3D 0C CE 8C 00            cmp byte ptr [rip + 0x8cce0c], dil
00637AAC  75 0C                           jne 0x140637aba
00637AAE  F7 05 C8 CE 8C 00 00 08 00 00   test dword ptr [rip + 0x8ccec8], 0x800
00637AB8  74 13                           je 0x140637acd
00637ABA  48 8D 0D BF C3 8C 00            lea rcx, [rip + 0x8cc3bf]
00637AC1  E8 5A EB BD FF                  call 0x140216620
00637AC6  40 8A F8                        mov dil, al
00637AC9  84 C0                           test al, al
00637ACB  74 38                           je 0x140637b05
00637ACD  49 8D 76 30                     lea rsi, [r14 + 0x30]
00637AD1  48 8B 1E                        mov rbx, qword ptr [rsi]
00637AD4  EB 19                           jmp 0x140637aef
00637AD6  48 8D 43 F0                     lea rax, [rbx - 0x10]
00637ADA  48 85 C0                        test rax, rax
00637ADD  74 0D                           je 0x140637aec
00637ADF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00637AE3  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00637AE7  E8 E4 2F 08 00                  call 0x1406baad0
00637AEC  48 8B 1B                        mov rbx, qword ptr [rbx]
00637AEF  48 3B DE                        cmp rbx, rsi
00637AF2  75 E2                           jne 0x140637ad6
00637AF4  40 84 FF                        test dil, dil
00637AF7  74 0C                           je 0x140637b05
00637AF9  48 8D 0D 80 C3 8C 00            lea rcx, [rip + 0x8cc380]
00637B00  E8 7B 23 D1 FF                  call 0x140349e80
00637B05  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00637B08  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00637B0D  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00637B11  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00637B15  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00637B19  49 8B E3                        mov rsp, r11
00637B1C  41 5F                           pop r15
00637B1E  41 5E                           pop r14
00637B20  41 5D                           pop r13
00637B22  41 5C                           pop r12
00637B24  5D                              pop rbp
00637B25  C3                              ret
00637B26  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifNtOpenFileWrapper(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(206, a2, a3, a4);
    if (result == 0) goto loc_00637A7A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006379E9;
    v_stack_m68 = v_stack_p0;
    goto loc_006379F7;
loc_006379E9:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m5C = (unsigned int)((unsigned int)(a5));
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    v_stack_m58 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9227955)) != 0) goto loc_00637A2F;
    if (((*(unsigned int *)(v_rip + 9228115)) & (0x800ULL)) == 0) goto loc_00637A42;
loc_00637A2F:
    result = ExAcquireRundownProtection(v_rip + 9225290, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00637A7A;
loc_00637A42:
    goto loc_00637A64;
loc_00637A4B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00637A64:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00637A4B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9225227;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = (unsigned int)((unsigned int)(a6));
    v_stack_m78 = (unsigned int)((unsigned int)(a5));
    result = NtOpenFile(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00637B05;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9227788)) != 0) goto loc_00637ABA;
    if (((*(unsigned int *)(v_rip + 9227976)) & (0x800ULL)) == 0) goto loc_00637ACD;
loc_00637ABA:
    result = ExAcquireRundownProtection(v_rip + 9225151, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00637B05;
loc_00637ACD:
    goto loc_00637AEF;
loc_00637AD6:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00637AEF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00637AD6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9225088;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifNtOpenFileWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(206, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00637A7A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006379E9;
    v_stack_m68 = v_stack_p0;
    goto loc_006379F7;
loc_006379E9:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m5C = (uint32_t)((uint32_t)(Arg5));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    v_stack_m58 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8CCEB3)) != 0) goto loc_00637A2F;
    if (((*(uint32_t *)(v_rip + 0x8CCF53)) & (0x800ULL)) == 0) goto loc_00637A42;
loc_00637A2F:
    result = ExAcquireRundownProtection(v_rip + 9225290, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00637A7A;
loc_00637A42:
    goto loc_00637A64;
loc_00637A4B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00637A64:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00637A4B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9225227;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m78 = (uint32_t)((uint32_t)(Arg5));
    result = NtOpenFile(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00637B05;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CCE0C)) != 0) goto loc_00637ABA;
    if (((*(uint32_t *)(v_rip + 0x8CCEC8)) & (0x800ULL)) == 0) goto loc_00637ACD;
loc_00637ABA:
    result = ExAcquireRundownProtection(v_rip + 9225151, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00637B05;
loc_00637ACD:
    goto loc_00637AEF;
loc_00637AD6:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_00637AEF:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00637AD6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9225088;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00637980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00637980[BB_00637980]
  bb_006379D7[BB_006379D7]
  bb_006379DF[BB_006379DF]
  bb_006379E9[BB_006379E9]
  bb_006379EE[BB_006379EE]
  bb_006379F7[BB_006379F7]
  bb_00637A23[BB_00637A23]
  bb_00637A2F[BB_00637A2F]
  bb_00637A42[BB_00637A42]
  bb_00637A4B[BB_00637A4B]
  bb_00637A54[BB_00637A54]
  bb_00637A61[BB_00637A61]
  bb_00637A64[BB_00637A64]
  bb_00637A69[BB_00637A69]
  bb_00637A6E[BB_00637A6E]
  bb_00637A7A[BB_00637A7A]
  bb_00637AA2[BB_00637AA2]
  bb_00637AAE[BB_00637AAE]
  bb_00637ABA[BB_00637ABA]
  bb_00637ACD[BB_00637ACD]
  bb_00637AD6[BB_00637AD6]
  bb_00637ADF[BB_00637ADF]
  bb_00637AEC[BB_00637AEC]
  bb_00637AEF[BB_00637AEF]
  bb_00637AF4[BB_00637AF4]
  bb_00637AF9[BB_00637AF9]
  bb_00637B05[BB_00637B05]
  bb_00637B26[BB_00637B26]
  bb_00637980 -->|branch| bb_00637A7A
  bb_00637980 -->|fallthrough| bb_006379D7
  bb_006379D7 -->|branch| bb_006379E9
  bb_006379D7 -->|fallthrough| bb_006379DF
  bb_006379DF -->|branch| bb_006379F7
  bb_006379E9 -->|branch| bb_006379F7
  bb_006379E9 -->|fallthrough| bb_006379EE
  bb_006379EE -->|flow| bb_006379F7
  bb_006379F7 -->|branch| bb_00637A2F
  bb_006379F7 -->|fallthrough| bb_00637A23
  bb_00637A23 -->|branch| bb_00637A42
  bb_00637A23 -->|fallthrough| bb_00637A2F
  bb_00637A2F -->|branch| bb_00637A7A
  bb_00637A2F -->|fallthrough| bb_00637A42
  bb_00637A42 -->|branch| bb_00637A64
  bb_00637A4B -->|branch| bb_00637A61
  bb_00637A4B -->|fallthrough| bb_00637A54
  bb_00637A54 -->|flow| bb_00637A61
  bb_00637A61 -->|flow| bb_00637A64
  bb_00637A64 -->|branch| bb_00637A4B
  bb_00637A64 -->|fallthrough| bb_00637A69
  bb_00637A69 -->|branch| bb_00637A7A
  bb_00637A69 -->|fallthrough| bb_00637A6E
  bb_00637A6E -->|flow| bb_00637A7A
  bb_00637A7A -->|branch| bb_00637B05
  bb_00637A7A -->|fallthrough| bb_00637AA2
  bb_00637AA2 -->|branch| bb_00637ABA
  bb_00637AA2 -->|fallthrough| bb_00637AAE
  bb_00637AAE -->|branch| bb_00637ACD
  bb_00637AAE -->|fallthrough| bb_00637ABA
  bb_00637ABA -->|branch| bb_00637B05
  bb_00637ABA -->|fallthrough| bb_00637ACD
  bb_00637ACD -->|branch| bb_00637AEF
  bb_00637AD6 -->|branch| bb_00637AEC
  bb_00637AD6 -->|fallthrough| bb_00637ADF
  bb_00637ADF -->|flow| bb_00637AEC
  bb_00637AEC -->|flow| bb_00637AEF
  bb_00637AEF -->|branch| bb_00637AD6
  bb_00637AEF -->|fallthrough| bb_00637AF4
  bb_00637AF4 -->|branch| bb_00637B05
  bb_00637AF4 -->|fallthrough| bb_00637AF9
  bb_00637AF9 -->|flow| bb_00637B05
```
