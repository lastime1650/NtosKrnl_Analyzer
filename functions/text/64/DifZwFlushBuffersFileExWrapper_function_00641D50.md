# DifZwFlushBuffersFileExWrapper

- RVA: `0x00641D50`–`0x00641EEC` (길이 `412` bytes)
- VA: `0x0000000140641D50`
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
- `0x00641D94` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00641DBC` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00641E00` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00641E26` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641E3F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00641E5A` → [ZwFlushBuffersFileEx](../6A/ZwFlushBuffersFileEx_function_006AEEB0.md) (function, `0x006AEEB0`)
- `0x00641E86` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00641EAC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641EC5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00641DCC` → RVA `0x00F048B8` (`.data`; read)
- `0x00641DED` → RVA `0x00F04980` (`.data`; read)
- `0x00641DF9` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00641D50  48 8B C4                        mov rax, rsp
00641D53  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00641D57  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00641D5B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00641D5F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00641D63  55                              push rbp
00641D64  41 54                           push r12
00641D66  41 55                           push r13
00641D68  41 56                           push r14
00641D6A  41 57                           push r15
00641D6C  48 8B EC                        mov rbp, rsp
00641D6F  48 83 EC 70                     sub rsp, 0x70
00641D73  33 C0                           xor eax, eax
00641D75  0F 57 C0                        xorps xmm0, xmm0
00641D78  45 8B F9                        mov r15d, r9d
00641D7B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00641D7F  4D 8B E0                        mov r12, r8
00641D82  44 8B EA                        mov r13d, edx
00641D85  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00641D89  8D 48 65                        lea ecx, [rax + 0x65]
00641D8C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00641D90  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00641D94  E8 9B 3C E5 FF                  call 0x140495a34
00641D99  4C 8B F0                        mov r14, rax
00641D9C  48 85 C0                        test rax, rax
00641D9F  0F 84 9F 00 00 00               je 0x140641e44
00641DA5  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00641DA8  F6 C1 18                        test cl, 0x18
00641DAB  74 0A                           je 0x140641db7
00641DAD  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00641DB1  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00641DB5  EB 0E                           jmp 0x140641dc5
00641DB7  F6 C1 04                        test cl, 4
00641DBA  74 09                           je 0x140641dc5
00641DBC  E8 47 1E E9 FF                  call 0x1404d3c08
00641DC1  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00641DC5  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00641DC9  40 32 F6                        xor sil, sil
00641DCC  40 38 35 E5 2A 8C 00            cmp byte ptr [rip + 0x8c2ae5], sil
00641DD3  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00641DD7  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00641DDB  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00641DDF  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00641DE3  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00641DE7  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
00641DEB  75 0C                           jne 0x140641df9
00641DED  F7 05 89 2B 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2b89], 0x800
00641DF7  74 13                           je 0x140641e0c
00641DF9  48 8D 0D 80 20 8C 00            lea rcx, [rip + 0x8c2080]
00641E00  E8 1B 48 BD FF                  call 0x140216620
00641E05  40 8A F0                        mov sil, al
00641E08  84 C0                           test al, al
00641E0A  74 38                           je 0x140641e44
00641E0C  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00641E10  48 8B 1F                        mov rbx, qword ptr [rdi]
00641E13  EB 19                           jmp 0x140641e2e
00641E15  48 8D 43 F0                     lea rax, [rbx - 0x10]
00641E19  48 85 C0                        test rax, rax
00641E1C  74 0D                           je 0x140641e2b
00641E1E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00641E22  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00641E26  E8 A5 8C 07 00                  call 0x1406baad0
00641E2B  48 8B 1B                        mov rbx, qword ptr [rbx]
00641E2E  48 3B DF                        cmp rbx, rdi
00641E31  75 E2                           jne 0x140641e15
00641E33  40 84 F6                        test sil, sil
00641E36  74 0C                           je 0x140641e44
00641E38  48 8D 0D 41 20 8C 00            lea rcx, [rip + 0x8c2041]
00641E3F  E8 3C 80 D0 FF                  call 0x140349e80
00641E44  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00641E48  45 8B CF                        mov r9d, r15d
00641E4B  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00641E4F  4D 8B C4                        mov r8, r12
00641E52  41 8B D5                        mov edx, r13d
00641E55  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00641E5A  E8 51 D0 06 00                  call 0x1406aeeb0
00641E5F  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00641E62  4D 85 F6                        test r14, r14
00641E65  74 63                           je 0x140641eca
00641E67  40 32 FF                        xor dil, dil
00641E6A  40 38 3D 47 2A 8C 00            cmp byte ptr [rip + 0x8c2a47], dil
00641E71  75 0C                           jne 0x140641e7f
00641E73  F7 05 03 2B 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2b03], 0x800
00641E7D  74 13                           je 0x140641e92
00641E7F  48 8D 0D FA 1F 8C 00            lea rcx, [rip + 0x8c1ffa]
00641E86  E8 95 47 BD FF                  call 0x140216620
00641E8B  40 8A F8                        mov dil, al
00641E8E  84 C0                           test al, al
00641E90  74 38                           je 0x140641eca
00641E92  49 8D 76 30                     lea rsi, [r14 + 0x30]
00641E96  48 8B 1E                        mov rbx, qword ptr [rsi]
00641E99  EB 19                           jmp 0x140641eb4
00641E9B  48 8D 43 F0                     lea rax, [rbx - 0x10]
00641E9F  48 85 C0                        test rax, rax
00641EA2  74 0D                           je 0x140641eb1
00641EA4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00641EA8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00641EAC  E8 1F 8C 07 00                  call 0x1406baad0
00641EB1  48 8B 1B                        mov rbx, qword ptr [rbx]
00641EB4  48 3B DE                        cmp rbx, rsi
00641EB7  75 E2                           jne 0x140641e9b
00641EB9  40 84 FF                        test dil, dil
00641EBC  74 0C                           je 0x140641eca
00641EBE  48 8D 0D BB 1F 8C 00            lea rcx, [rip + 0x8c1fbb]
00641EC5  E8 B6 7F D0 FF                  call 0x140349e80
00641ECA  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00641ECD  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00641ED2  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00641ED6  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00641EDA  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00641EDE  49 8B E3                        mov rsp, r11
00641EE1  41 5F                           pop r15
00641EE3  41 5E                           pop r14
00641EE5  41 5D                           pop r13
00641EE7  41 5C                           pop r12
00641EE9  5D                              pop rbp
00641EEA  C3                              ret
00641EEB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwFlushBuffersFileExWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
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
    result = DifGetAPIThunkContextById(result + 101, a2, a3, a4);
    if (result == 0) goto loc_00641E44;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00641DB7;
    v_stack_m68 = v_stack_p0;
    goto loc_00641DC5;
loc_00641DB7:
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
    if ((*(unsigned __int8 *)(v_rip + 9186021)) != 0) goto loc_00641DF9;
    if (((*(unsigned int *)(v_rip + 9186185)) & (0x800ULL)) == 0) goto loc_00641E0C;
loc_00641DF9:
    result = ExAcquireRundownProtection(v_rip + 9183360, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00641E44;
loc_00641E0C:
    goto loc_00641E2E;
loc_00641E15:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00641E2E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00641E15;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9183297;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwFlushBuffersFileEx(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00641ECA;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9185863)) != 0) goto loc_00641E7F;
    if (((*(unsigned int *)(v_rip + 9186051)) & (0x800ULL)) == 0) goto loc_00641E92;
loc_00641E7F:
    result = ExAcquireRundownProtection(v_rip + 9183226, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00641ECA;
loc_00641E92:
    goto loc_00641EB4;
loc_00641E9B:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_00641EB4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00641E9B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9183163;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwFlushBuffersFileExWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
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
    result = DifGetAPIThunkContextById(result + 101, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00641E44;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00641DB7;
    v_stack_m68 = v_stack_p0;
    goto loc_00641DC5;
loc_00641DB7:
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
    if ((*(uint8_t *)(v_rip + 0x8C2AE5)) != 0) goto loc_00641DF9;
    if (((*(uint32_t *)(v_rip + 0x8C2B89)) & (0x800ULL)) == 0) goto loc_00641E0C;
loc_00641DF9:
    result = ExAcquireRundownProtection(v_rip + 9183360, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00641E44;
loc_00641E0C:
    goto loc_00641E2E;
loc_00641E15:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00641E2E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00641E15;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9183297;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwFlushBuffersFileEx(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00641ECA;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C2A47)) != 0) goto loc_00641E7F;
    if (((*(uint32_t *)(v_rip + 0x8C2B03)) & (0x800ULL)) == 0) goto loc_00641E92;
loc_00641E7F:
    result = ExAcquireRundownProtection(v_rip + 9183226, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00641ECA;
loc_00641E92:
    goto loc_00641EB4;
loc_00641E9B:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_00641EB4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00641E9B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9183163;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00641D50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00641D50[BB_00641D50]
  bb_00641DA5[BB_00641DA5]
  bb_00641DAD[BB_00641DAD]
  bb_00641DB7[BB_00641DB7]
  bb_00641DBC[BB_00641DBC]
  bb_00641DC5[BB_00641DC5]
  bb_00641DED[BB_00641DED]
  bb_00641DF9[BB_00641DF9]
  bb_00641E0C[BB_00641E0C]
  bb_00641E15[BB_00641E15]
  bb_00641E1E[BB_00641E1E]
  bb_00641E2B[BB_00641E2B]
  bb_00641E2E[BB_00641E2E]
  bb_00641E33[BB_00641E33]
  bb_00641E38[BB_00641E38]
  bb_00641E44[BB_00641E44]
  bb_00641E67[BB_00641E67]
  bb_00641E73[BB_00641E73]
  bb_00641E7F[BB_00641E7F]
  bb_00641E92[BB_00641E92]
  bb_00641E9B[BB_00641E9B]
  bb_00641EA4[BB_00641EA4]
  bb_00641EB1[BB_00641EB1]
  bb_00641EB4[BB_00641EB4]
  bb_00641EB9[BB_00641EB9]
  bb_00641EBE[BB_00641EBE]
  bb_00641ECA[BB_00641ECA]
  bb_00641EEB[BB_00641EEB]
  bb_00641D50 -->|branch| bb_00641E44
  bb_00641D50 -->|fallthrough| bb_00641DA5
  bb_00641DA5 -->|branch| bb_00641DB7
  bb_00641DA5 -->|fallthrough| bb_00641DAD
  bb_00641DAD -->|branch| bb_00641DC5
  bb_00641DB7 -->|branch| bb_00641DC5
  bb_00641DB7 -->|fallthrough| bb_00641DBC
  bb_00641DBC -->|flow| bb_00641DC5
  bb_00641DC5 -->|branch| bb_00641DF9
  bb_00641DC5 -->|fallthrough| bb_00641DED
  bb_00641DED -->|branch| bb_00641E0C
  bb_00641DED -->|fallthrough| bb_00641DF9
  bb_00641DF9 -->|branch| bb_00641E44
  bb_00641DF9 -->|fallthrough| bb_00641E0C
  bb_00641E0C -->|branch| bb_00641E2E
  bb_00641E15 -->|branch| bb_00641E2B
  bb_00641E15 -->|fallthrough| bb_00641E1E
  bb_00641E1E -->|flow| bb_00641E2B
  bb_00641E2B -->|flow| bb_00641E2E
  bb_00641E2E -->|branch| bb_00641E15
  bb_00641E2E -->|fallthrough| bb_00641E33
  bb_00641E33 -->|branch| bb_00641E44
  bb_00641E33 -->|fallthrough| bb_00641E38
  bb_00641E38 -->|flow| bb_00641E44
  bb_00641E44 -->|branch| bb_00641ECA
  bb_00641E44 -->|fallthrough| bb_00641E67
  bb_00641E67 -->|branch| bb_00641E7F
  bb_00641E67 -->|fallthrough| bb_00641E73
  bb_00641E73 -->|branch| bb_00641E92
  bb_00641E73 -->|fallthrough| bb_00641E7F
  bb_00641E7F -->|branch| bb_00641ECA
  bb_00641E7F -->|fallthrough| bb_00641E92
  bb_00641E92 -->|branch| bb_00641EB4
  bb_00641E9B -->|branch| bb_00641EB1
  bb_00641E9B -->|fallthrough| bb_00641EA4
  bb_00641EA4 -->|flow| bb_00641EB1
  bb_00641EB1 -->|flow| bb_00641EB4
  bb_00641EB4 -->|branch| bb_00641E9B
  bb_00641EB4 -->|fallthrough| bb_00641EB9
  bb_00641EB9 -->|branch| bb_00641ECA
  bb_00641EB9 -->|fallthrough| bb_00641EBE
  bb_00641EBE -->|flow| bb_00641ECA
```
