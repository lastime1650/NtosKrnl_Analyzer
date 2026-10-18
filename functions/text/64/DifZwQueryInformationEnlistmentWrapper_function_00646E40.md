# DifZwQueryInformationEnlistmentWrapper

- RVA: `0x00646E40`–`0x00646FDC` (길이 `412` bytes)
- VA: `0x0000000140646E40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `118`개 명령, `412/412` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00646E84` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00646EAC` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00646EF0` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00646F16` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00646F2F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00646F4A` → [ZwQueryInformationEnlistment](../6A/ZwQueryInformationEnlistment_function_006AFB90.md) (function, `0x006AFB90`)
- `0x00646F76` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00646F9C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00646FB5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00646EBC` → RVA `0x00F048B8` (`.data`; read)
- `0x00646EDD` → RVA `0x00F04980` (`.data`; read)
- `0x00646EE9` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00646E40  48 8B C4                        mov rax, rsp
00646E43  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00646E47  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00646E4B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00646E4F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00646E53  55                              push rbp
00646E54  41 54                           push r12
00646E56  41 55                           push r13
00646E58  41 56                           push r14
00646E5A  41 57                           push r15
00646E5C  48 8B EC                        mov rbp, rsp
00646E5F  48 83 EC 70                     sub rsp, 0x70
00646E63  33 C0                           xor eax, eax
00646E65  0F 57 C0                        xorps xmm0, xmm0
00646E68  45 8B F9                        mov r15d, r9d
00646E6B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00646E6F  4D 8B E0                        mov r12, r8
00646E72  44 8B EA                        mov r13d, edx
00646E75  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00646E79  8D 48 33                        lea ecx, [rax + 0x33]
00646E7C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00646E80  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00646E84  E8 AB EB E4 FF                  call 0x140495a34
00646E89  4C 8B F0                        mov r14, rax
00646E8C  48 85 C0                        test rax, rax
00646E8F  0F 84 9F 00 00 00               je 0x140646f34
00646E95  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00646E98  F6 C1 18                        test cl, 0x18
00646E9B  74 0A                           je 0x140646ea7
00646E9D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00646EA1  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00646EA5  EB 0E                           jmp 0x140646eb5
00646EA7  F6 C1 04                        test cl, 4
00646EAA  74 09                           je 0x140646eb5
00646EAC  E8 57 CD E8 FF                  call 0x1404d3c08
00646EB1  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00646EB5  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00646EB9  40 32 F6                        xor sil, sil
00646EBC  40 38 35 F5 D9 8B 00            cmp byte ptr [rip + 0x8bd9f5], sil
00646EC3  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00646EC7  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00646ECB  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00646ECF  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00646ED3  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00646ED7  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
00646EDB  75 0C                           jne 0x140646ee9
00646EDD  F7 05 99 DA 8B 00 00 08 00 00   test dword ptr [rip + 0x8bda99], 0x800
00646EE7  74 13                           je 0x140646efc
00646EE9  48 8D 0D 90 CF 8B 00            lea rcx, [rip + 0x8bcf90]
00646EF0  E8 2B F7 BC FF                  call 0x140216620
00646EF5  40 8A F0                        mov sil, al
00646EF8  84 C0                           test al, al
00646EFA  74 38                           je 0x140646f34
00646EFC  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00646F00  48 8B 1F                        mov rbx, qword ptr [rdi]
00646F03  EB 19                           jmp 0x140646f1e
00646F05  48 8D 43 F0                     lea rax, [rbx - 0x10]
00646F09  48 85 C0                        test rax, rax
00646F0C  74 0D                           je 0x140646f1b
00646F0E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00646F12  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00646F16  E8 B5 3B 07 00                  call 0x1406baad0
00646F1B  48 8B 1B                        mov rbx, qword ptr [rbx]
00646F1E  48 3B DF                        cmp rbx, rdi
00646F21  75 E2                           jne 0x140646f05
00646F23  40 84 F6                        test sil, sil
00646F26  74 0C                           je 0x140646f34
00646F28  48 8D 0D 51 CF 8B 00            lea rcx, [rip + 0x8bcf51]
00646F2F  E8 4C 2F D0 FF                  call 0x140349e80
00646F34  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00646F38  45 8B CF                        mov r9d, r15d
00646F3B  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00646F3F  4D 8B C4                        mov r8, r12
00646F42  41 8B D5                        mov edx, r13d
00646F45  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00646F4A  E8 41 8C 06 00                  call 0x1406afb90
00646F4F  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00646F52  4D 85 F6                        test r14, r14
00646F55  74 63                           je 0x140646fba
00646F57  40 32 FF                        xor dil, dil
00646F5A  40 38 3D 57 D9 8B 00            cmp byte ptr [rip + 0x8bd957], dil
00646F61  75 0C                           jne 0x140646f6f
00646F63  F7 05 13 DA 8B 00 00 08 00 00   test dword ptr [rip + 0x8bda13], 0x800
00646F6D  74 13                           je 0x140646f82
00646F6F  48 8D 0D 0A CF 8B 00            lea rcx, [rip + 0x8bcf0a]
00646F76  E8 A5 F6 BC FF                  call 0x140216620
00646F7B  40 8A F8                        mov dil, al
00646F7E  84 C0                           test al, al
00646F80  74 38                           je 0x140646fba
00646F82  49 8D 76 30                     lea rsi, [r14 + 0x30]
00646F86  48 8B 1E                        mov rbx, qword ptr [rsi]
00646F89  EB 19                           jmp 0x140646fa4
00646F8B  48 8D 43 F0                     lea rax, [rbx - 0x10]
00646F8F  48 85 C0                        test rax, rax
00646F92  74 0D                           je 0x140646fa1
00646F94  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00646F98  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00646F9C  E8 2F 3B 07 00                  call 0x1406baad0
00646FA1  48 8B 1B                        mov rbx, qword ptr [rbx]
00646FA4  48 3B DE                        cmp rbx, rsi
00646FA7  75 E2                           jne 0x140646f8b
00646FA9  40 84 FF                        test dil, dil
00646FAC  74 0C                           je 0x140646fba
00646FAE  48 8D 0D CB CE 8B 00            lea rcx, [rip + 0x8bcecb]
00646FB5  E8 C6 2E D0 FF                  call 0x140349e80
00646FBA  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00646FBD  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00646FC2  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00646FC6  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00646FCA  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00646FCE  49 8B E3                        mov rsp, r11
00646FD1  41 5F                           pop r15
00646FD3  41 5E                           pop r14
00646FD5  41 5D                           pop r13
00646FD7  41 5C                           pop r12
00646FD9  5D                              pop rbp
00646FDA  C3                              ret
00646FDB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryInformationEnlistmentWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
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
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
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
    result = DifGetAPIThunkContextById(result + 51, a2, a3, a4);
    if (result == 0) goto loc_00646F34;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00646EA7;
    v_stack_m68 = v_stack_p0;
    goto loc_00646EB5;
loc_00646EA7:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = a5;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    v_stack_m58 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9165301)) != 0) goto loc_00646EE9;
    if (((*(unsigned int *)(v_rip + 9165465)) & (0x800ULL)) == 0) goto loc_00646EFC;
loc_00646EE9:
    result = ExAcquireRundownProtection(v_rip + 9162640, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00646F34;
loc_00646EFC:
    goto loc_00646F1E;
loc_00646F05:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00646F1E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00646F05;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9162577;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwQueryInformationEnlistment(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00646FBA;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9165143)) != 0) goto loc_00646F6F;
    if (((*(unsigned int *)(v_rip + 9165331)) & (0x800ULL)) == 0) goto loc_00646F82;
loc_00646F6F:
    result = ExAcquireRundownProtection(v_rip + 9162506, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00646FBA;
loc_00646F82:
    goto loc_00646FA4;
loc_00646F8B:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_00646FA4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00646F8B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9162443;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryInformationEnlistmentWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
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
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
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
    result = DifGetAPIThunkContextById(result + 51, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00646F34;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00646EA7;
    v_stack_m68 = v_stack_p0;
    goto loc_00646EB5;
loc_00646EA7:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = Arg5;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8BD9F5)) != 0) goto loc_00646EE9;
    if (((*(uint32_t *)(v_rip + 0x8BDA99)) & (0x800ULL)) == 0) goto loc_00646EFC;
loc_00646EE9:
    result = ExAcquireRundownProtection(v_rip + 9162640, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00646F34;
loc_00646EFC:
    goto loc_00646F1E;
loc_00646F05:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00646F1E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00646F05;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9162577;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwQueryInformationEnlistment(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00646FBA;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BD957)) != 0) goto loc_00646F6F;
    if (((*(uint32_t *)(v_rip + 0x8BDA13)) & (0x800ULL)) == 0) goto loc_00646F82;
loc_00646F6F:
    result = ExAcquireRundownProtection(v_rip + 9162506, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00646FBA;
loc_00646F82:
    goto loc_00646FA4;
loc_00646F8B:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_00646FA4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00646F8B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9162443;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00646E40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00646E40[BB_00646E40]
  bb_00646E95[BB_00646E95]
  bb_00646E9D[BB_00646E9D]
  bb_00646EA7[BB_00646EA7]
  bb_00646EAC[BB_00646EAC]
  bb_00646EB5[BB_00646EB5]
  bb_00646EDD[BB_00646EDD]
  bb_00646EE9[BB_00646EE9]
  bb_00646EFC[BB_00646EFC]
  bb_00646F05[BB_00646F05]
  bb_00646F0E[BB_00646F0E]
  bb_00646F1B[BB_00646F1B]
  bb_00646F1E[BB_00646F1E]
  bb_00646F23[BB_00646F23]
  bb_00646F28[BB_00646F28]
  bb_00646F34[BB_00646F34]
  bb_00646F57[BB_00646F57]
  bb_00646F63[BB_00646F63]
  bb_00646F6F[BB_00646F6F]
  bb_00646F82[BB_00646F82]
  bb_00646F8B[BB_00646F8B]
  bb_00646F94[BB_00646F94]
  bb_00646FA1[BB_00646FA1]
  bb_00646FA4[BB_00646FA4]
  bb_00646FA9[BB_00646FA9]
  bb_00646FAE[BB_00646FAE]
  bb_00646FBA[BB_00646FBA]
  bb_00646FDB[BB_00646FDB]
  bb_00646E40 -->|branch| bb_00646F34
  bb_00646E40 -->|fallthrough| bb_00646E95
  bb_00646E95 -->|branch| bb_00646EA7
  bb_00646E95 -->|fallthrough| bb_00646E9D
  bb_00646E9D -->|branch| bb_00646EB5
  bb_00646EA7 -->|branch| bb_00646EB5
  bb_00646EA7 -->|fallthrough| bb_00646EAC
  bb_00646EAC -->|flow| bb_00646EB5
  bb_00646EB5 -->|branch| bb_00646EE9
  bb_00646EB5 -->|fallthrough| bb_00646EDD
  bb_00646EDD -->|branch| bb_00646EFC
  bb_00646EDD -->|fallthrough| bb_00646EE9
  bb_00646EE9 -->|branch| bb_00646F34
  bb_00646EE9 -->|fallthrough| bb_00646EFC
  bb_00646EFC -->|branch| bb_00646F1E
  bb_00646F05 -->|branch| bb_00646F1B
  bb_00646F05 -->|fallthrough| bb_00646F0E
  bb_00646F0E -->|flow| bb_00646F1B
  bb_00646F1B -->|flow| bb_00646F1E
  bb_00646F1E -->|branch| bb_00646F05
  bb_00646F1E -->|fallthrough| bb_00646F23
  bb_00646F23 -->|branch| bb_00646F34
  bb_00646F23 -->|fallthrough| bb_00646F28
  bb_00646F28 -->|flow| bb_00646F34
  bb_00646F34 -->|branch| bb_00646FBA
  bb_00646F34 -->|fallthrough| bb_00646F57
  bb_00646F57 -->|branch| bb_00646F6F
  bb_00646F57 -->|fallthrough| bb_00646F63
  bb_00646F63 -->|branch| bb_00646F82
  bb_00646F63 -->|fallthrough| bb_00646F6F
  bb_00646F6F -->|branch| bb_00646FBA
  bb_00646F6F -->|fallthrough| bb_00646F82
  bb_00646F82 -->|branch| bb_00646FA4
  bb_00646F8B -->|branch| bb_00646FA1
  bb_00646F8B -->|fallthrough| bb_00646F94
  bb_00646F94 -->|flow| bb_00646FA1
  bb_00646FA1 -->|flow| bb_00646FA4
  bb_00646FA4 -->|branch| bb_00646F8B
  bb_00646FA4 -->|fallthrough| bb_00646FA9
  bb_00646FA9 -->|branch| bb_00646FBA
  bb_00646FA9 -->|fallthrough| bb_00646FAE
  bb_00646FAE -->|flow| bb_00646FBA
```
