# DifZwOpenThreadTokenWrapper

- RVA: `0x00644CF0`–`0x00644E77` (길이 `391` bytes)
- VA: `0x0000000140644CF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `113`개 명령, `391/391` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00644D30` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00644D58` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00644D94` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00644DBA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00644DD3` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00644DE5` → [ZwOpenThreadToken](../6A/ZwOpenThreadToken_function_006AD550.md) (function, `0x006AD550`)
- `0x00644E11` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00644E37` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00644E50` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00644D68` → RVA `0x00F048B8` (`.data`; read)
- `0x00644D81` → RVA `0x00F04980` (`.data`; read)
- `0x00644D8D` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00644CF0  48 8B C4                        mov rax, rsp
00644CF3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00644CF7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00644CFB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00644CFF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00644D03  55                              push rbp
00644D04  41 54                           push r12
00644D06  41 55                           push r13
00644D08  41 56                           push r14
00644D0A  41 57                           push r15
00644D0C  48 8B EC                        mov rbp, rsp
00644D0F  48 83 EC 50                     sub rsp, 0x50
00644D13  33 C0                           xor eax, eax
00644D15  0F 57 C0                        xorps xmm0, xmm0
00644D18  4D 8B F9                        mov r15, r9
00644D1B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00644D1F  45 8A E0                        mov r12b, r8b
00644D22  44 8B EA                        mov r13d, edx
00644D25  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00644D29  8D 48 48                        lea ecx, [rax + 0x48]
00644D2C  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00644D30  E8 FF 0C E5 FF                  call 0x140495a34
00644D35  4C 8B F0                        mov r14, rax
00644D38  48 85 C0                        test rax, rax
00644D3B  0F 84 97 00 00 00               je 0x140644dd8
00644D41  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00644D44  F6 C1 18                        test cl, 0x18
00644D47  74 0A                           je 0x140644d53
00644D49  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00644D4D  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00644D51  EB 0E                           jmp 0x140644d61
00644D53  F6 C1 04                        test cl, 4
00644D56  74 09                           je 0x140644d61
00644D58  E8 AB EE E8 FF                  call 0x1404d3c08
00644D5D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00644D61  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00644D65  40 32 F6                        xor sil, sil
00644D68  40 38 35 49 FB 8B 00            cmp byte ptr [rip + 0x8bfb49], sil
00644D6F  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00644D73  44 89 6D E4                     mov dword ptr [rbp - 0x1c], r13d
00644D77  44 88 65 E0                     mov byte ptr [rbp - 0x20], r12b
00644D7B  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00644D7F  75 0C                           jne 0x140644d8d
00644D81  F7 05 F5 FB 8B 00 00 08 00 00   test dword ptr [rip + 0x8bfbf5], 0x800
00644D8B  74 13                           je 0x140644da0
00644D8D  48 8D 0D EC F0 8B 00            lea rcx, [rip + 0x8bf0ec]
00644D94  E8 87 18 BD FF                  call 0x140216620
00644D99  40 8A F0                        mov sil, al
00644D9C  84 C0                           test al, al
00644D9E  74 38                           je 0x140644dd8
00644DA0  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00644DA4  48 8B 1F                        mov rbx, qword ptr [rdi]
00644DA7  EB 19                           jmp 0x140644dc2
00644DA9  48 8D 43 F0                     lea rax, [rbx - 0x10]
00644DAD  48 85 C0                        test rax, rax
00644DB0  74 0D                           je 0x140644dbf
00644DB2  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644DB6  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00644DBA  E8 11 5D 07 00                  call 0x1406baad0
00644DBF  48 8B 1B                        mov rbx, qword ptr [rbx]
00644DC2  48 3B DF                        cmp rbx, rdi
00644DC5  75 E2                           jne 0x140644da9
00644DC7  40 84 F6                        test sil, sil
00644DCA  74 0C                           je 0x140644dd8
00644DCC  48 8D 0D AD F0 8B 00            lea rcx, [rip + 0x8bf0ad]
00644DD3  E8 A8 50 D0 FF                  call 0x140349e80
00644DD8  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00644DDC  4D 8B CF                        mov r9, r15
00644DDF  45 8A C4                        mov r8b, r12b
00644DE2  41 8B D5                        mov edx, r13d
00644DE5  E8 66 87 06 00                  call 0x1406ad550
00644DEA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00644DED  4D 85 F6                        test r14, r14
00644DF0  74 63                           je 0x140644e55
00644DF2  40 32 FF                        xor dil, dil
00644DF5  40 38 3D BC FA 8B 00            cmp byte ptr [rip + 0x8bfabc], dil
00644DFC  75 0C                           jne 0x140644e0a
00644DFE  F7 05 78 FB 8B 00 00 08 00 00   test dword ptr [rip + 0x8bfb78], 0x800
00644E08  74 13                           je 0x140644e1d
00644E0A  48 8D 0D 6F F0 8B 00            lea rcx, [rip + 0x8bf06f]
00644E11  E8 0A 18 BD FF                  call 0x140216620
00644E16  40 8A F8                        mov dil, al
00644E19  84 C0                           test al, al
00644E1B  74 38                           je 0x140644e55
00644E1D  49 8D 76 30                     lea rsi, [r14 + 0x30]
00644E21  48 8B 1E                        mov rbx, qword ptr [rsi]
00644E24  EB 19                           jmp 0x140644e3f
00644E26  48 8D 43 F0                     lea rax, [rbx - 0x10]
00644E2A  48 85 C0                        test rax, rax
00644E2D  74 0D                           je 0x140644e3c
00644E2F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644E33  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00644E37  E8 94 5C 07 00                  call 0x1406baad0
00644E3C  48 8B 1B                        mov rbx, qword ptr [rbx]
00644E3F  48 3B DE                        cmp rbx, rsi
00644E42  75 E2                           jne 0x140644e26
00644E44  40 84 FF                        test dil, dil
00644E47  74 0C                           je 0x140644e55
00644E49  48 8D 0D 30 F0 8B 00            lea rcx, [rip + 0x8bf030]
00644E50  E8 2B 50 D0 FF                  call 0x140349e80
00644E55  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00644E58  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00644E5D  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00644E61  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00644E65  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00644E69  49 8B E3                        mov rsp, r11
00644E6C  41 5F                           pop r15
00644E6E  41 5E                           pop r14
00644E70  41 5D                           pop r13
00644E72  41 5C                           pop r12
00644E74  5D                              pop rbp
00644E75  C3                              ret
00644E76  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenThreadTokenWrapper(__int64 a1, int a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 72, a2, a3, a4);
    if (result == 0) goto loc_00644DD8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00644D53;
    v_stack_m58 = v_stack_p0;
    goto loc_00644D61;
loc_00644D53:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m44 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9173833)) != 0) goto loc_00644D8D;
    if (((*(unsigned int *)(v_rip + 9174005)) & (0x800ULL)) == 0) goto loc_00644DA0;
loc_00644D8D:
    result = ExAcquireRundownProtection(v_rip + 9171180, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00644DD8;
loc_00644DA0:
    goto loc_00644DC2;
loc_00644DA9:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00644DC2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00644DA9;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9171117;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenThreadToken(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00644E55;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9173692)) != 0) goto loc_00644E0A;
    if (((*(unsigned int *)(v_rip + 9173880)) & (0x800ULL)) == 0) goto loc_00644E1D;
loc_00644E0A:
    result = ExAcquireRundownProtection(v_rip + 9171055, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00644E55;
loc_00644E1D:
    goto loc_00644E3F;
loc_00644E26:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00644E3F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00644E26;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9170992;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenThreadTokenWrapper(int64_t Arg1, int32_t Arg2, uint8_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 72, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00644DD8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00644D53;
    v_stack_m58 = v_stack_p0;
    goto loc_00644D61;
loc_00644D53:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m44 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8BFB49)) != 0) goto loc_00644D8D;
    if (((*(uint32_t *)(v_rip + 0x8BFBF5)) & (0x800ULL)) == 0) goto loc_00644DA0;
loc_00644D8D:
    result = ExAcquireRundownProtection(v_rip + 9171180, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00644DD8;
loc_00644DA0:
    goto loc_00644DC2;
loc_00644DA9:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00644DC2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00644DA9;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9171117;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwOpenThreadToken(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00644E55;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BFABC)) != 0) goto loc_00644E0A;
    if (((*(uint32_t *)(v_rip + 0x8BFB78)) & (0x800ULL)) == 0) goto loc_00644E1D;
loc_00644E0A:
    result = ExAcquireRundownProtection(v_rip + 9171055, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00644E55;
loc_00644E1D:
    goto loc_00644E3F;
loc_00644E26:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_00644E3F:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00644E26;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9170992;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00644CF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00644CF0[BB_00644CF0]
  bb_00644D41[BB_00644D41]
  bb_00644D49[BB_00644D49]
  bb_00644D53[BB_00644D53]
  bb_00644D58[BB_00644D58]
  bb_00644D61[BB_00644D61]
  bb_00644D81[BB_00644D81]
  bb_00644D8D[BB_00644D8D]
  bb_00644DA0[BB_00644DA0]
  bb_00644DA9[BB_00644DA9]
  bb_00644DB2[BB_00644DB2]
  bb_00644DBF[BB_00644DBF]
  bb_00644DC2[BB_00644DC2]
  bb_00644DC7[BB_00644DC7]
  bb_00644DCC[BB_00644DCC]
  bb_00644DD8[BB_00644DD8]
  bb_00644DF2[BB_00644DF2]
  bb_00644DFE[BB_00644DFE]
  bb_00644E0A[BB_00644E0A]
  bb_00644E1D[BB_00644E1D]
  bb_00644E26[BB_00644E26]
  bb_00644E2F[BB_00644E2F]
  bb_00644E3C[BB_00644E3C]
  bb_00644E3F[BB_00644E3F]
  bb_00644E44[BB_00644E44]
  bb_00644E49[BB_00644E49]
  bb_00644E55[BB_00644E55]
  bb_00644E76[BB_00644E76]
  bb_00644CF0 -->|branch| bb_00644DD8
  bb_00644CF0 -->|fallthrough| bb_00644D41
  bb_00644D41 -->|branch| bb_00644D53
  bb_00644D41 -->|fallthrough| bb_00644D49
  bb_00644D49 -->|branch| bb_00644D61
  bb_00644D53 -->|branch| bb_00644D61
  bb_00644D53 -->|fallthrough| bb_00644D58
  bb_00644D58 -->|flow| bb_00644D61
  bb_00644D61 -->|branch| bb_00644D8D
  bb_00644D61 -->|fallthrough| bb_00644D81
  bb_00644D81 -->|branch| bb_00644DA0
  bb_00644D81 -->|fallthrough| bb_00644D8D
  bb_00644D8D -->|branch| bb_00644DD8
  bb_00644D8D -->|fallthrough| bb_00644DA0
  bb_00644DA0 -->|branch| bb_00644DC2
  bb_00644DA9 -->|branch| bb_00644DBF
  bb_00644DA9 -->|fallthrough| bb_00644DB2
  bb_00644DB2 -->|flow| bb_00644DBF
  bb_00644DBF -->|flow| bb_00644DC2
  bb_00644DC2 -->|branch| bb_00644DA9
  bb_00644DC2 -->|fallthrough| bb_00644DC7
  bb_00644DC7 -->|branch| bb_00644DD8
  bb_00644DC7 -->|fallthrough| bb_00644DCC
  bb_00644DCC -->|flow| bb_00644DD8
  bb_00644DD8 -->|branch| bb_00644E55
  bb_00644DD8 -->|fallthrough| bb_00644DF2
  bb_00644DF2 -->|branch| bb_00644E0A
  bb_00644DF2 -->|fallthrough| bb_00644DFE
  bb_00644DFE -->|branch| bb_00644E1D
  bb_00644DFE -->|fallthrough| bb_00644E0A
  bb_00644E0A -->|branch| bb_00644E55
  bb_00644E0A -->|fallthrough| bb_00644E1D
  bb_00644E1D -->|branch| bb_00644E3F
  bb_00644E26 -->|branch| bb_00644E3C
  bb_00644E26 -->|fallthrough| bb_00644E2F
  bb_00644E2F -->|flow| bb_00644E3C
  bb_00644E3C -->|flow| bb_00644E3F
  bb_00644E3F -->|branch| bb_00644E26
  bb_00644E3F -->|fallthrough| bb_00644E44
  bb_00644E44 -->|branch| bb_00644E55
  bb_00644E44 -->|fallthrough| bb_00644E49
  bb_00644E49 -->|flow| bb_00644E55
```
