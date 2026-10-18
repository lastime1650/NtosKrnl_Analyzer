# DifIoCheckShareAccessWrapper

- RVA: `0x006285E0`–`0x0062876E` (길이 `398` bytes)
- VA: `0x00000001406285E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2C24`
- 디코드: `116`개 명령, `398/398` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062861F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00628645` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00628685` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006286AB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006286C4` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006286DC` → [IoCheckShareAccess](../../page/9A/IoCheckShareAccess_function_009A4150.md) (function, `0x009A4150`)
- `0x00628708` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062872E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00628747` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00628654` → RVA `0x00F048B8` (`.data`; read)
- `0x00628672` → RVA `0x00F04980` (`.data`; read)
- `0x0062867E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006286DC` → [IoCheckShareAccess](../../page/9A/IoCheckShareAccess_function_009A4150.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006285E0  48 8B C4                        mov rax, rsp
006285E3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006285E7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006285EB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006285EF  89 48 08                        mov dword ptr [rax + 8], ecx
006285F2  55                              push rbp
006285F3  41 54                           push r12
006285F5  41 55                           push r13
006285F7  41 56                           push r14
006285F9  41 57                           push r15
006285FB  48 8B EC                        mov rbp, rsp
006285FE  48 83 EC 60                     sub rsp, 0x60
00628602  0F 57 C0                        xorps xmm0, xmm0
00628605  B9 67 01 00 00                  mov ecx, 0x167
0062860A  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062860E  4D 8B F9                        mov r15, r9
00628611  4D 8B E0                        mov r12, r8
00628614  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00628618  44 8B EA                        mov r13d, edx
0062861B  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0062861F  E8 10 D4 E6 FF                  call 0x140495a34
00628624  48 8B F0                        mov rsi, rax
00628627  48 85 C0                        test rax, rax
0062862A  0F 84 99 00 00 00               je 0x1406286c9
00628630  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00628633  A8 18                           test al, 0x18
00628635  74 0A                           je 0x140628641
00628637  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062863B  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0062863F  EB 0D                           jmp 0x14062864e
00628641  A8 04                           test al, 4
00628643  74 09                           je 0x14062864e
00628645  E8 BE B5 EA FF                  call 0x1404d3c08
0062864A  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062864E  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
00628651  45 32 F6                        xor r14b, r14b
00628654  44 38 35 5D C2 8D 00            cmp byte ptr [rip + 0x8dc25d], r14b
0062865B  89 45 F4                        mov dword ptr [rbp - 0xc], eax
0062865E  8A 45 50                        mov al, byte ptr [rbp + 0x50]
00628661  88 45 D8                        mov byte ptr [rbp - 0x28], al
00628664  44 89 6D F0                     mov dword ptr [rbp - 0x10], r13d
00628668  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
0062866C  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
00628670  75 0C                           jne 0x14062867e
00628672  F7 05 04 C3 8D 00 00 08 00 00   test dword ptr [rip + 0x8dc304], 0x800
0062867C  74 13                           je 0x140628691
0062867E  48 8D 0D FB B7 8D 00            lea rcx, [rip + 0x8db7fb]
00628685  E8 96 DF BE FF                  call 0x140216620
0062868A  44 8A F0                        mov r14b, al
0062868D  84 C0                           test al, al
0062868F  74 38                           je 0x1406286c9
00628691  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00628695  48 8B 1F                        mov rbx, qword ptr [rdi]
00628698  EB 19                           jmp 0x1406286b3
0062869A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062869E  48 85 C0                        test rax, rax
006286A1  74 0D                           je 0x1406286b0
006286A3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006286A7  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006286AB  E8 20 24 09 00                  call 0x1406baad0
006286B0  48 8B 1B                        mov rbx, qword ptr [rbx]
006286B3  48 3B DF                        cmp rbx, rdi
006286B6  75 E2                           jne 0x14062869a
006286B8  45 84 F6                        test r14b, r14b
006286BB  74 0C                           je 0x1406286c9
006286BD  48 8D 0D BC B7 8D 00            lea rcx, [rip + 0x8db7bc]
006286C4  E8 B7 17 D2 FF                  call 0x140349e80
006286C9  8A 45 50                        mov al, byte ptr [rbp + 0x50]
006286CC  4D 8B CF                        mov r9, r15
006286CF  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
006286D2  4D 8B C4                        mov r8, r12
006286D5  41 8B D5                        mov edx, r13d
006286D8  88 44 24 20                     mov byte ptr [rsp + 0x20], al
006286DC  E8 6F BA 37 00                  call 0x1409a4150
006286E1  89 45 F8                        mov dword ptr [rbp - 8], eax
006286E4  48 85 F6                        test rsi, rsi
006286E7  74 63                           je 0x14062874c
006286E9  40 32 FF                        xor dil, dil
006286EC  40 38 3D C5 C1 8D 00            cmp byte ptr [rip + 0x8dc1c5], dil
006286F3  75 0C                           jne 0x140628701
006286F5  F7 05 81 C2 8D 00 00 08 00 00   test dword ptr [rip + 0x8dc281], 0x800
006286FF  74 13                           je 0x140628714
00628701  48 8D 0D 78 B7 8D 00            lea rcx, [rip + 0x8db778]
00628708  E8 13 DF BE FF                  call 0x140216620
0062870D  40 8A F8                        mov dil, al
00628710  84 C0                           test al, al
00628712  74 38                           je 0x14062874c
00628714  48 83 C6 30                     add rsi, 0x30
00628718  48 8B 1E                        mov rbx, qword ptr [rsi]
0062871B  EB 19                           jmp 0x140628736
0062871D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00628721  48 85 C0                        test rax, rax
00628724  74 0D                           je 0x140628733
00628726  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062872A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062872E  E8 9D 23 09 00                  call 0x1406baad0
00628733  48 8B 1B                        mov rbx, qword ptr [rbx]
00628736  48 3B DE                        cmp rbx, rsi
00628739  75 E2                           jne 0x14062871d
0062873B  40 84 FF                        test dil, dil
0062873E  74 0C                           je 0x14062874c
00628740  48 8D 0D 39 B7 8D 00            lea rcx, [rip + 0x8db739]
00628747  E8 34 17 D2 FF                  call 0x140349e80
0062874C  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0062874F  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00628754  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00628758  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0062875C  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00628760  49 8B E3                        mov rsp, r11
00628763  41 5F                           pop r15
00628765  41 5E                           pop r14
00628767  41 5D                           pop r13
00628769  41 5C                           pop r12
0062876B  5D                              pop rbp
0062876C  C3                              ret
0062876D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoCheckShareAccessWrapper(int a1, int a2, __int64 a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(359, a2, a3, a4);
    if (result == 0) goto loc_006286C9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00628641;
    v_stack_m58 = v_stack_p0;
    goto loc_0062864E;
loc_00628641:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m34 = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_m50 = a5;
    v_stack_m38 = (unsigned int)((unsigned int)(a2));
    v_stack_m40 = a3;
    v_stack_m48 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9290333)) != 0) goto loc_0062867E;
    if (((*(unsigned int *)(v_rip + 9290500)) & (0x800ULL)) == 0) goto loc_00628691;
loc_0062867E:
    result = ExAcquireRundownProtection(v_rip + 9287675, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006286C9;
loc_00628691:
    goto loc_006286B3;
loc_0062869A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006286B3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062869A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9287612;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = a5;
    result = IoCheckShareAccess((unsigned int)(v_stack_p8), (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0062874C;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9290181)) != 0) goto loc_00628701;
    if (((*(unsigned int *)(v_rip + 9290369)) & (0x800ULL)) == 0) goto loc_00628714;
loc_00628701:
    result = ExAcquireRundownProtection(v_rip + 9287544, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062874C;
loc_00628714:
    v_rsi = (result) + (48);
    goto loc_00628736;
loc_0062871D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00628736:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062871D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9287481;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoCheckShareAccessWrapper(int32_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m34;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint8_t v_stack_m68;
    uint64_t v_stack_p0;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(359, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006286C9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00628641;
    v_stack_m58 = v_stack_p0;
    goto loc_0062864E;
loc_00628641:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m34 = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_m50 = Arg5;
    v_stack_m38 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m40 = Arg3;
    v_stack_m48 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8DC25D)) != 0) goto loc_0062867E;
    if (((*(uint32_t *)(v_rip + 0x8DC304)) & (0x800ULL)) == 0) goto loc_00628691;
loc_0062867E:
    result = ExAcquireRundownProtection(v_rip + 9287675, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006286C9;
loc_00628691:
    goto loc_006286B3;
loc_0062869A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006286B3:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062869A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9287612;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = Arg5;
    result = IoCheckShareAccess((uint32_t)(v_stack_p8), (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0062874C;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DC1C5)) != 0) goto loc_00628701;
    if (((*(uint32_t *)(v_rip + 0x8DC281)) & (0x800ULL)) == 0) goto loc_00628714;
loc_00628701:
    result = ExAcquireRundownProtection(v_rip + 9287544, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062874C;
loc_00628714:
    local_rsi = (result) + (48);
    goto loc_00628736;
loc_0062871D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_00628736:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062871D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9287481;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006285E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006285E0[BB_006285E0]
  bb_00628630[BB_00628630]
  bb_00628637[BB_00628637]
  bb_00628641[BB_00628641]
  bb_00628645[BB_00628645]
  bb_0062864E[BB_0062864E]
  bb_00628672[BB_00628672]
  bb_0062867E[BB_0062867E]
  bb_00628691[BB_00628691]
  bb_0062869A[BB_0062869A]
  bb_006286A3[BB_006286A3]
  bb_006286B0[BB_006286B0]
  bb_006286B3[BB_006286B3]
  bb_006286B8[BB_006286B8]
  bb_006286BD[BB_006286BD]
  bb_006286C9[BB_006286C9]
  bb_006286E9[BB_006286E9]
  bb_006286F5[BB_006286F5]
  bb_00628701[BB_00628701]
  bb_00628714[BB_00628714]
  bb_0062871D[BB_0062871D]
  bb_00628726[BB_00628726]
  bb_00628733[BB_00628733]
  bb_00628736[BB_00628736]
  bb_0062873B[BB_0062873B]
  bb_00628740[BB_00628740]
  bb_0062874C[BB_0062874C]
  bb_0062876D[BB_0062876D]
  bb_006285E0 -->|branch| bb_006286C9
  bb_006285E0 -->|fallthrough| bb_00628630
  bb_00628630 -->|branch| bb_00628641
  bb_00628630 -->|fallthrough| bb_00628637
  bb_00628637 -->|branch| bb_0062864E
  bb_00628641 -->|branch| bb_0062864E
  bb_00628641 -->|fallthrough| bb_00628645
  bb_00628645 -->|flow| bb_0062864E
  bb_0062864E -->|branch| bb_0062867E
  bb_0062864E -->|fallthrough| bb_00628672
  bb_00628672 -->|branch| bb_00628691
  bb_00628672 -->|fallthrough| bb_0062867E
  bb_0062867E -->|branch| bb_006286C9
  bb_0062867E -->|fallthrough| bb_00628691
  bb_00628691 -->|branch| bb_006286B3
  bb_0062869A -->|branch| bb_006286B0
  bb_0062869A -->|fallthrough| bb_006286A3
  bb_006286A3 -->|flow| bb_006286B0
  bb_006286B0 -->|flow| bb_006286B3
  bb_006286B3 -->|branch| bb_0062869A
  bb_006286B3 -->|fallthrough| bb_006286B8
  bb_006286B8 -->|branch| bb_006286C9
  bb_006286B8 -->|fallthrough| bb_006286BD
  bb_006286BD -->|flow| bb_006286C9
  bb_006286C9 -->|branch| bb_0062874C
  bb_006286C9 -->|fallthrough| bb_006286E9
  bb_006286E9 -->|branch| bb_00628701
  bb_006286E9 -->|fallthrough| bb_006286F5
  bb_006286F5 -->|branch| bb_00628714
  bb_006286F5 -->|fallthrough| bb_00628701
  bb_00628701 -->|branch| bb_0062874C
  bb_00628701 -->|fallthrough| bb_00628714
  bb_00628714 -->|branch| bb_00628736
  bb_0062871D -->|branch| bb_00628733
  bb_0062871D -->|fallthrough| bb_00628726
  bb_00628726 -->|flow| bb_00628733
  bb_00628733 -->|flow| bb_00628736
  bb_00628736 -->|branch| bb_0062871D
  bb_00628736 -->|fallthrough| bb_0062873B
  bb_0062873B -->|branch| bb_0062874C
  bb_0062873B -->|fallthrough| bb_00628740
  bb_00628740 -->|flow| bb_0062874C
```
