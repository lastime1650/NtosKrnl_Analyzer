# DifKeWaitForSingleObjectWrapper

- RVA: `0x006336D0`–`0x0063386A` (길이 `410` bytes)
- VA: `0x00000001406336D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `117`개 명령, `410/410` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00633712` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063373A` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063377E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006337A4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006337BD` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006337D8` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00633804` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063382A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00633843` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063374A` → RVA `0x00F048B8` (`.data`; read)
- `0x0063376B` → RVA `0x00F04980` (`.data`; read)
- `0x00633777` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006336D0  48 8B C4                        mov rax, rsp
006336D3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006336D7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006336DB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006336DF  48 89 48 08                     mov qword ptr [rax + 8], rcx
006336E3  55                              push rbp
006336E4  41 54                           push r12
006336E6  41 55                           push r13
006336E8  41 56                           push r14
006336EA  41 57                           push r15
006336EC  48 8B EC                        mov rbp, rsp
006336EF  48 83 EC 60                     sub rsp, 0x60
006336F3  0F 57 C0                        xorps xmm0, xmm0
006336F6  33 C0                           xor eax, eax
006336F8  B9 F0 00 00 00                  mov ecx, 0xf0
006336FD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00633701  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00633705  45 8A F9                        mov r15b, r9b
00633708  45 8A E0                        mov r12b, r8b
0063370B  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063370F  44 8B EA                        mov r13d, edx
00633712  E8 1D 23 E6 FF                  call 0x140495a34
00633717  4C 8B F0                        mov r14, rax
0063371A  48 85 C0                        test rax, rax
0063371D  0F 84 9F 00 00 00               je 0x1406337c2
00633723  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00633726  F6 C1 18                        test cl, 0x18
00633729  74 0A                           je 0x140633735
0063372B  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063372F  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00633733  EB 0E                           jmp 0x140633743
00633735  F6 C1 04                        test cl, 4
00633738  74 09                           je 0x140633743
0063373A  E8 C9 04 EA FF                  call 0x1404d3c08
0063373F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00633743  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00633747  40 32 F6                        xor sil, sil
0063374A  40 38 35 67 11 8D 00            cmp byte ptr [rip + 0x8d1167], sil
00633751  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00633755  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00633759  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0063375D  44 89 6D E4                     mov dword ptr [rbp - 0x1c], r13d
00633761  44 88 65 E1                     mov byte ptr [rbp - 0x1f], r12b
00633765  44 88 7D E0                     mov byte ptr [rbp - 0x20], r15b
00633769  75 0C                           jne 0x140633777
0063376B  F7 05 0B 12 8D 00 00 08 00 00   test dword ptr [rip + 0x8d120b], 0x800
00633775  74 13                           je 0x14063378a
00633777  48 8D 0D 02 07 8D 00            lea rcx, [rip + 0x8d0702]
0063377E  E8 9D 2E BE FF                  call 0x140216620
00633783  40 8A F0                        mov sil, al
00633786  84 C0                           test al, al
00633788  74 38                           je 0x1406337c2
0063378A  49 8D 7E 20                     lea rdi, [r14 + 0x20]
0063378E  48 8B 1F                        mov rbx, qword ptr [rdi]
00633791  EB 19                           jmp 0x1406337ac
00633793  48 8D 43 F0                     lea rax, [rbx - 0x10]
00633797  48 85 C0                        test rax, rax
0063379A  74 0D                           je 0x1406337a9
0063379C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006337A0  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006337A4  E8 27 73 08 00                  call 0x1406baad0
006337A9  48 8B 1B                        mov rbx, qword ptr [rbx]
006337AC  48 3B DF                        cmp rbx, rdi
006337AF  75 E2                           jne 0x140633793
006337B1  40 84 F6                        test sil, sil
006337B4  74 0C                           je 0x1406337c2
006337B6  48 8D 0D C3 06 8D 00            lea rcx, [rip + 0x8d06c3]
006337BD  E8 BE 66 D1 FF                  call 0x140349e80
006337C2  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
006337C6  45 8A CF                        mov r9b, r15b
006337C9  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006337CD  45 8A C4                        mov r8b, r12b
006337D0  41 8B D5                        mov edx, r13d
006337D3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006337D8  E8 D3 AE BD FF                  call 0x14020e6b0
006337DD  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006337E0  4D 85 F6                        test r14, r14
006337E3  74 63                           je 0x140633848
006337E5  40 32 FF                        xor dil, dil
006337E8  40 38 3D C9 10 8D 00            cmp byte ptr [rip + 0x8d10c9], dil
006337EF  75 0C                           jne 0x1406337fd
006337F1  F7 05 85 11 8D 00 00 08 00 00   test dword ptr [rip + 0x8d1185], 0x800
006337FB  74 13                           je 0x140633810
006337FD  48 8D 0D 7C 06 8D 00            lea rcx, [rip + 0x8d067c]
00633804  E8 17 2E BE FF                  call 0x140216620
00633809  40 8A F8                        mov dil, al
0063380C  84 C0                           test al, al
0063380E  74 38                           je 0x140633848
00633810  49 8D 76 30                     lea rsi, [r14 + 0x30]
00633814  48 8B 1E                        mov rbx, qword ptr [rsi]
00633817  EB 19                           jmp 0x140633832
00633819  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063381D  48 85 C0                        test rax, rax
00633820  74 0D                           je 0x14063382f
00633822  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00633826  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063382A  E8 A1 72 08 00                  call 0x1406baad0
0063382F  48 8B 1B                        mov rbx, qword ptr [rbx]
00633832  48 3B DE                        cmp rbx, rsi
00633835  75 E2                           jne 0x140633819
00633837  40 84 FF                        test dil, dil
0063383A  74 0C                           je 0x140633848
0063383C  48 8D 0D 3D 06 8D 00            lea rcx, [rip + 0x8d063d]
00633843  E8 38 66 D1 FF                  call 0x140349e80
00633848  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063384B  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00633850  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00633854  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00633858  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0063385C  49 8B E3                        mov rsp, r11
0063385F  41 5F                           pop r15
00633861  41 5E                           pop r14
00633863  41 5D                           pop r13
00633865  41 5C                           pop r12
00633867  5D                              pop rbp
00633868  C3                              ret
00633869  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeWaitForSingleObjectWrapper(__int64 a1, int a2, unsigned __int8 a3, unsigned __int8 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int8 v_stack_m47;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(240, a2, a3, a4);
    if (result == 0) goto loc_006337C2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00633735;
    v_stack_m58 = v_stack_p0;
    goto loc_00633743;
loc_00633735:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m50 = a5;
    v_stack_m44 = (unsigned int)((unsigned int)(a2));
    v_stack_m47 = a3;
    v_stack_m48 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9245031)) != 0) goto loc_00633777;
    if (((*(unsigned int *)(v_rip + 9245195)) & (0x800ULL)) == 0) goto loc_0063378A;
loc_00633777:
    result = ExAcquireRundownProtection(v_rip + 9242370, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006337C2;
loc_0063378A:
    goto loc_006337AC;
loc_00633793:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006337AC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00633793;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9242307;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = a5;
    result = KeWaitForSingleObject(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00633848;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9244873)) != 0) goto loc_006337FD;
    if (((*(unsigned int *)(v_rip + 9245061)) & (0x800ULL)) == 0) goto loc_00633810;
loc_006337FD:
    result = ExAcquireRundownProtection(v_rip + 9242236, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00633848;
loc_00633810:
    goto loc_00633832;
loc_00633819:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00633832:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00633819;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9242173;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifKeWaitForSingleObjectWrapper(int64_t Arg1, int32_t Arg2, uint8_t Arg3, uint8_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint8_t v_stack_m47;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(240, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006337C2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00633735;
    v_stack_m58 = v_stack_p0;
    goto loc_00633743;
loc_00633735:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m50 = Arg5;
    v_stack_m44 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m47 = Arg3;
    v_stack_m48 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8D1167)) != 0) goto loc_00633777;
    if (((*(uint32_t *)(v_rip + 0x8D120B)) & (0x800ULL)) == 0) goto loc_0063378A;
loc_00633777:
    result = ExAcquireRundownProtection(v_rip + 9242370, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006337C2;
loc_0063378A:
    goto loc_006337AC;
loc_00633793:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006337AC:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00633793;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9242307;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = Arg5;
    result = KeWaitForSingleObject(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00633848;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D10C9)) != 0) goto loc_006337FD;
    if (((*(uint32_t *)(v_rip + 0x8D1185)) & (0x800ULL)) == 0) goto loc_00633810;
loc_006337FD:
    result = ExAcquireRundownProtection(v_rip + 9242236, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00633848;
loc_00633810:
    goto loc_00633832;
loc_00633819:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_00633832:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00633819;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9242173;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006336D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006336D0[BB_006336D0]
  bb_00633723[BB_00633723]
  bb_0063372B[BB_0063372B]
  bb_00633735[BB_00633735]
  bb_0063373A[BB_0063373A]
  bb_00633743[BB_00633743]
  bb_0063376B[BB_0063376B]
  bb_00633777[BB_00633777]
  bb_0063378A[BB_0063378A]
  bb_00633793[BB_00633793]
  bb_0063379C[BB_0063379C]
  bb_006337A9[BB_006337A9]
  bb_006337AC[BB_006337AC]
  bb_006337B1[BB_006337B1]
  bb_006337B6[BB_006337B6]
  bb_006337C2[BB_006337C2]
  bb_006337E5[BB_006337E5]
  bb_006337F1[BB_006337F1]
  bb_006337FD[BB_006337FD]
  bb_00633810[BB_00633810]
  bb_00633819[BB_00633819]
  bb_00633822[BB_00633822]
  bb_0063382F[BB_0063382F]
  bb_00633832[BB_00633832]
  bb_00633837[BB_00633837]
  bb_0063383C[BB_0063383C]
  bb_00633848[BB_00633848]
  bb_00633869[BB_00633869]
  bb_006336D0 -->|branch| bb_006337C2
  bb_006336D0 -->|fallthrough| bb_00633723
  bb_00633723 -->|branch| bb_00633735
  bb_00633723 -->|fallthrough| bb_0063372B
  bb_0063372B -->|branch| bb_00633743
  bb_00633735 -->|branch| bb_00633743
  bb_00633735 -->|fallthrough| bb_0063373A
  bb_0063373A -->|flow| bb_00633743
  bb_00633743 -->|branch| bb_00633777
  bb_00633743 -->|fallthrough| bb_0063376B
  bb_0063376B -->|branch| bb_0063378A
  bb_0063376B -->|fallthrough| bb_00633777
  bb_00633777 -->|branch| bb_006337C2
  bb_00633777 -->|fallthrough| bb_0063378A
  bb_0063378A -->|branch| bb_006337AC
  bb_00633793 -->|branch| bb_006337A9
  bb_00633793 -->|fallthrough| bb_0063379C
  bb_0063379C -->|flow| bb_006337A9
  bb_006337A9 -->|flow| bb_006337AC
  bb_006337AC -->|branch| bb_00633793
  bb_006337AC -->|fallthrough| bb_006337B1
  bb_006337B1 -->|branch| bb_006337C2
  bb_006337B1 -->|fallthrough| bb_006337B6
  bb_006337B6 -->|flow| bb_006337C2
  bb_006337C2 -->|branch| bb_00633848
  bb_006337C2 -->|fallthrough| bb_006337E5
  bb_006337E5 -->|branch| bb_006337FD
  bb_006337E5 -->|fallthrough| bb_006337F1
  bb_006337F1 -->|branch| bb_00633810
  bb_006337F1 -->|fallthrough| bb_006337FD
  bb_006337FD -->|branch| bb_00633848
  bb_006337FD -->|fallthrough| bb_00633810
  bb_00633810 -->|branch| bb_00633832
  bb_00633819 -->|branch| bb_0063382F
  bb_00633819 -->|fallthrough| bb_00633822
  bb_00633822 -->|flow| bb_0063382F
  bb_0063382F -->|flow| bb_00633832
  bb_00633832 -->|branch| bb_00633819
  bb_00633832 -->|fallthrough| bb_00633837
  bb_00633837 -->|branch| bb_00633848
  bb_00633837 -->|fallthrough| bb_0063383C
  bb_0063383C -->|flow| bb_00633848
```
