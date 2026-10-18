# DifMmMapLockedPagesSpecifyCacheWrapper

- RVA: `0x00635D60`–`0x00635F03` (길이 `419` bytes)
- VA: `0x0000000140635D60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `120`개 명령, `419/419` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00635DA0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00635DC8` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00635E10` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00635E36` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00635E4F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00635E6F` → [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x00635E9C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00635EC2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00635EDB` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00635DD8` → RVA `0x00F048B8` (`.data`; read)
- `0x00635DFD` → RVA `0x00F04980` (`.data`; read)
- `0x00635E09` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00635D60  48 8B C4                        mov rax, rsp
00635D63  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00635D67  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00635D6B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00635D6F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00635D73  55                              push rbp
00635D74  41 54                           push r12
00635D76  41 55                           push r13
00635D78  41 56                           push r14
00635D7A  41 57                           push r15
00635D7C  48 8B EC                        mov rbp, rsp
00635D7F  48 83 EC 60                     sub rsp, 0x60
00635D83  0F 57 C0                        xorps xmm0, xmm0
00635D86  B9 DB 00 00 00                  mov ecx, 0xdb
00635D8B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00635D8F  4D 8B F9                        mov r15, r9
00635D92  45 8B E0                        mov r12d, r8d
00635D95  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00635D99  44 8A EA                        mov r13b, dl
00635D9C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00635DA0  E8 8F FC E5 FF                  call 0x140495a34
00635DA5  48 8B F0                        mov rsi, rax
00635DA8  48 85 C0                        test rax, rax
00635DAB  0F 84 A3 00 00 00               je 0x140635e54
00635DB1  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00635DB4  F6 C1 18                        test cl, 0x18
00635DB7  74 0A                           je 0x140635dc3
00635DB9  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00635DBD  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00635DC1  EB 0E                           jmp 0x140635dd1
00635DC3  F6 C1 04                        test cl, 4
00635DC6  74 09                           je 0x140635dd1
00635DC8  E8 3B DE E9 FF                  call 0x1404d3c08
00635DCD  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00635DD1  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00635DD5  45 32 F6                        xor r14b, r14b
00635DD8  44 38 35 D9 EA 8C 00            cmp byte ptr [rip + 0x8cead9], r14b
00635DDF  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00635DE3  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00635DE6  89 45 DC                        mov dword ptr [rbp - 0x24], eax
00635DE9  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00635DEC  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00635DEF  44 88 6D EC                     mov byte ptr [rbp - 0x14], r13b
00635DF3  44 89 65 E8                     mov dword ptr [rbp - 0x18], r12d
00635DF7  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
00635DFB  75 0C                           jne 0x140635e09
00635DFD  F7 05 79 EB 8C 00 00 08 00 00   test dword ptr [rip + 0x8ceb79], 0x800
00635E07  74 13                           je 0x140635e1c
00635E09  48 8D 0D 70 E0 8C 00            lea rcx, [rip + 0x8ce070]
00635E10  E8 0B 08 BE FF                  call 0x140216620
00635E15  44 8A F0                        mov r14b, al
00635E18  84 C0                           test al, al
00635E1A  74 38                           je 0x140635e54
00635E1C  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00635E20  48 8B 1F                        mov rbx, qword ptr [rdi]
00635E23  EB 19                           jmp 0x140635e3e
00635E25  48 8D 43 F0                     lea rax, [rbx - 0x10]
00635E29  48 85 C0                        test rax, rax
00635E2C  74 0D                           je 0x140635e3b
00635E2E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635E32  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00635E36  E8 95 4C 08 00                  call 0x1406baad0
00635E3B  48 8B 1B                        mov rbx, qword ptr [rbx]
00635E3E  48 3B DF                        cmp rbx, rdi
00635E41  75 E2                           jne 0x140635e25
00635E43  45 84 F6                        test r14b, r14b
00635E46  74 0C                           je 0x140635e54
00635E48  48 8D 0D 31 E0 8C 00            lea rcx, [rip + 0x8ce031]
00635E4F  E8 2C 40 D1 FF                  call 0x140349e80
00635E54  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00635E57  4D 8B CF                        mov r9, r15
00635E5A  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00635E5E  45 8B C4                        mov r8d, r12d
00635E61  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00635E65  41 8A D5                        mov dl, r13b
00635E68  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00635E6B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00635E6F  E8 8C 29 CE FF                  call 0x140318800
00635E74  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00635E78  48 85 F6                        test rsi, rsi
00635E7B  74 63                           je 0x140635ee0
00635E7D  40 32 FF                        xor dil, dil
00635E80  40 38 3D 31 EA 8C 00            cmp byte ptr [rip + 0x8cea31], dil
00635E87  75 0C                           jne 0x140635e95
00635E89  F7 05 ED EA 8C 00 00 08 00 00   test dword ptr [rip + 0x8ceaed], 0x800
00635E93  74 13                           je 0x140635ea8
00635E95  48 8D 0D E4 DF 8C 00            lea rcx, [rip + 0x8cdfe4]
00635E9C  E8 7F 07 BE FF                  call 0x140216620
00635EA1  40 8A F8                        mov dil, al
00635EA4  84 C0                           test al, al
00635EA6  74 38                           je 0x140635ee0
00635EA8  48 83 C6 30                     add rsi, 0x30
00635EAC  48 8B 1E                        mov rbx, qword ptr [rsi]
00635EAF  EB 19                           jmp 0x140635eca
00635EB1  48 8D 43 F0                     lea rax, [rbx - 0x10]
00635EB5  48 85 C0                        test rax, rax
00635EB8  74 0D                           je 0x140635ec7
00635EBA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635EBE  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00635EC2  E8 09 4C 08 00                  call 0x1406baad0
00635EC7  48 8B 1B                        mov rbx, qword ptr [rbx]
00635ECA  48 3B DE                        cmp rbx, rsi
00635ECD  75 E2                           jne 0x140635eb1
00635ECF  40 84 FF                        test dil, dil
00635ED2  74 0C                           je 0x140635ee0
00635ED4  48 8D 0D A5 DF 8C 00            lea rcx, [rip + 0x8cdfa5]
00635EDB  E8 A0 3F D1 FF                  call 0x140349e80
00635EE0  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00635EE4  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00635EE9  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00635EED  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00635EF1  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00635EF5  49 8B E3                        mov rsp, r11
00635EF8  41 5F                           pop r15
00635EFA  41 5E                           pop r14
00635EFC  41 5D                           pop r13
00635EFE  41 5C                           pop r12
00635F00  5D                              pop rbp
00635F01  C3                              ret
00635F02  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmMapLockedPagesSpecifyCacheWrapper(__int64 a1, unsigned __int8 a2, int a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(219, a2, a3, a4);
    if (result == 0) goto loc_00635E54;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00635DC3;
    v_stack_m58 = v_stack_p0;
    goto loc_00635DD1;
loc_00635DC3:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m4C = (unsigned int)((unsigned int)(a5));
    v_stack_m50 = (unsigned int)((unsigned int)(a6));
    v_stack_m3C = a2;
    v_stack_m40 = (unsigned int)((unsigned int)(a3));
    v_stack_m48 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9235161)) != 0) goto loc_00635E09;
    if (((*(unsigned int *)(v_rip + 9235321)) & (0x800ULL)) == 0) goto loc_00635E1C;
loc_00635E09:
    result = ExAcquireRundownProtection(v_rip + 9232496, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00635E54;
loc_00635E1C:
    goto loc_00635E3E;
loc_00635E25:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00635E3E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00635E25;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9232433;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = MmMapLockedPagesSpecifyCache(v_stack_p8, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m30 = result;
    if (result == 0) goto loc_00635EE0;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9234993)) != 0) goto loc_00635E95;
    if (((*(unsigned int *)(v_rip + 9235181)) & (0x800ULL)) == 0) goto loc_00635EA8;
loc_00635E95:
    result = ExAcquireRundownProtection(v_rip + 9232356, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00635EE0;
loc_00635EA8:
    v_rsi = (result) + (48);
    goto loc_00635ECA;
loc_00635EB1:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_00635ECA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00635EB1;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9232293;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return v_stack_m30;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmMapLockedPagesSpecifyCacheWrapper(int64_t Arg1, uint8_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint8_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(219, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00635E54;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00635DC3;
    v_stack_m58 = v_stack_p0;
    goto loc_00635DD1;
loc_00635DC3:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m4C = (uint32_t)((uint32_t)(Arg5));
    v_stack_m50 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m3C = Arg2;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m48 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8CEAD9)) != 0) goto loc_00635E09;
    if (((*(uint32_t *)(v_rip + 0x8CEB79)) & (0x800ULL)) == 0) goto loc_00635E1C;
loc_00635E09:
    result = ExAcquireRundownProtection(v_rip + 9232496, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00635E54;
loc_00635E1C:
    goto loc_00635E3E;
loc_00635E25:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00635E3E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00635E25;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9232433;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = MmMapLockedPagesSpecifyCache(v_stack_p8, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m30 = result;
    if (result == 0) goto loc_00635EE0;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CEA31)) != 0) goto loc_00635E95;
    if (((*(uint32_t *)(v_rip + 0x8CEAED)) & (0x800ULL)) == 0) goto loc_00635EA8;
loc_00635E95:
    result = ExAcquireRundownProtection(v_rip + 9232356, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00635EE0;
loc_00635EA8:
    local_rsi = (result) + (48);
    goto loc_00635ECA;
loc_00635EB1:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_00635ECA:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00635EB1;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9232293;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return v_stack_m30;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00635D60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00635D60[BB_00635D60]
  bb_00635DB1[BB_00635DB1]
  bb_00635DB9[BB_00635DB9]
  bb_00635DC3[BB_00635DC3]
  bb_00635DC8[BB_00635DC8]
  bb_00635DD1[BB_00635DD1]
  bb_00635DFD[BB_00635DFD]
  bb_00635E09[BB_00635E09]
  bb_00635E1C[BB_00635E1C]
  bb_00635E25[BB_00635E25]
  bb_00635E2E[BB_00635E2E]
  bb_00635E3B[BB_00635E3B]
  bb_00635E3E[BB_00635E3E]
  bb_00635E43[BB_00635E43]
  bb_00635E48[BB_00635E48]
  bb_00635E54[BB_00635E54]
  bb_00635E7D[BB_00635E7D]
  bb_00635E89[BB_00635E89]
  bb_00635E95[BB_00635E95]
  bb_00635EA8[BB_00635EA8]
  bb_00635EB1[BB_00635EB1]
  bb_00635EBA[BB_00635EBA]
  bb_00635EC7[BB_00635EC7]
  bb_00635ECA[BB_00635ECA]
  bb_00635ECF[BB_00635ECF]
  bb_00635ED4[BB_00635ED4]
  bb_00635EE0[BB_00635EE0]
  bb_00635F02[BB_00635F02]
  bb_00635D60 -->|branch| bb_00635E54
  bb_00635D60 -->|fallthrough| bb_00635DB1
  bb_00635DB1 -->|branch| bb_00635DC3
  bb_00635DB1 -->|fallthrough| bb_00635DB9
  bb_00635DB9 -->|branch| bb_00635DD1
  bb_00635DC3 -->|branch| bb_00635DD1
  bb_00635DC3 -->|fallthrough| bb_00635DC8
  bb_00635DC8 -->|flow| bb_00635DD1
  bb_00635DD1 -->|branch| bb_00635E09
  bb_00635DD1 -->|fallthrough| bb_00635DFD
  bb_00635DFD -->|branch| bb_00635E1C
  bb_00635DFD -->|fallthrough| bb_00635E09
  bb_00635E09 -->|branch| bb_00635E54
  bb_00635E09 -->|fallthrough| bb_00635E1C
  bb_00635E1C -->|branch| bb_00635E3E
  bb_00635E25 -->|branch| bb_00635E3B
  bb_00635E25 -->|fallthrough| bb_00635E2E
  bb_00635E2E -->|flow| bb_00635E3B
  bb_00635E3B -->|flow| bb_00635E3E
  bb_00635E3E -->|branch| bb_00635E25
  bb_00635E3E -->|fallthrough| bb_00635E43
  bb_00635E43 -->|branch| bb_00635E54
  bb_00635E43 -->|fallthrough| bb_00635E48
  bb_00635E48 -->|flow| bb_00635E54
  bb_00635E54 -->|branch| bb_00635EE0
  bb_00635E54 -->|fallthrough| bb_00635E7D
  bb_00635E7D -->|branch| bb_00635E95
  bb_00635E7D -->|fallthrough| bb_00635E89
  bb_00635E89 -->|branch| bb_00635EA8
  bb_00635E89 -->|fallthrough| bb_00635E95
  bb_00635E95 -->|branch| bb_00635EE0
  bb_00635E95 -->|fallthrough| bb_00635EA8
  bb_00635EA8 -->|branch| bb_00635ECA
  bb_00635EB1 -->|branch| bb_00635EC7
  bb_00635EB1 -->|fallthrough| bb_00635EBA
  bb_00635EBA -->|flow| bb_00635EC7
  bb_00635EC7 -->|flow| bb_00635ECA
  bb_00635ECA -->|branch| bb_00635EB1
  bb_00635ECA -->|fallthrough| bb_00635ECF
  bb_00635ECF -->|branch| bb_00635EE0
  bb_00635ECF -->|fallthrough| bb_00635ED4
  bb_00635ED4 -->|flow| bb_00635EE0
```
