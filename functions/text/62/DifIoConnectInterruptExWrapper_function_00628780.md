# DifIoConnectInterruptExWrapper

- RVA: `0x00628780`–`0x006288DF` (길이 `351` bytes)
- VA: `0x0000000140628780`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006287AF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006287D7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00628805` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062882C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00628845` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062884D` → [IoConnectInterruptEx](../../page/90/IoConnectInterruptEx_function_009001F0.md) (function, `0x009001F0`)
- `0x0062887A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006288A1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006288BA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006287E9` → RVA `0x00F048B8` (`.data`; read)
- `0x006287F2` → RVA `0x00F04980` (`.data`; read)
- `0x006287FE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062884D` → [IoConnectInterruptEx](../../page/90/IoConnectInterruptEx_function_009001F0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00628780  4C 8B DC                        mov r11, rsp
00628783  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00628787  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062878B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062878F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00628793  41 56                           push r14
00628795  48 83 EC 40                     sub rsp, 0x40
00628799  33 C0                           xor eax, eax
0062879B  0F 57 C0                        xorps xmm0, xmm0
0062879E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006287A3  48 8B E9                        mov rbp, rcx
006287A6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
006287AA  B9 65 01 00 00                  mov ecx, 0x165
006287AF  E8 80 D2 E6 FF                  call 0x140495a34
006287B4  48 8B F0                        mov rsi, rax
006287B7  48 85 C0                        test rax, rax
006287BA  0F 84 8A 00 00 00               je 0x14062884a
006287C0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006287C3  A8 18                           test al, 0x18
006287C5  74 0C                           je 0x1406287d3
006287C7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006287CC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006287D1  EB 0E                           jmp 0x1406287e1
006287D3  A8 04                           test al, 4
006287D5  74 0A                           je 0x1406287e1
006287D7  E8 2C B4 EA FF                  call 0x1404d3c08
006287DC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006287E1  40 32 FF                        xor dil, dil
006287E4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006287E9  40 38 3D C8 C0 8D 00            cmp byte ptr [rip + 0x8dc0c8], dil
006287F0  75 0C                           jne 0x1406287fe
006287F2  F7 05 84 C1 8D 00 00 08 00 00   test dword ptr [rip + 0x8dc184], 0x800
006287FC  74 13                           je 0x140628811
006287FE  48 8D 0D 7B B6 8D 00            lea rcx, [rip + 0x8db67b]
00628805  E8 16 DE BE FF                  call 0x140216620
0062880A  40 8A F8                        mov dil, al
0062880D  84 C0                           test al, al
0062880F  74 39                           je 0x14062884a
00628811  4C 8D 76 20                     lea r14, [rsi + 0x20]
00628815  49 8B 1E                        mov rbx, qword ptr [r14]
00628818  EB 1A                           jmp 0x140628834
0062881A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062881E  48 85 C0                        test rax, rax
00628821  74 0E                           je 0x140628831
00628823  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00628827  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062882C  E8 9F 22 09 00                  call 0x1406baad0
00628831  48 8B 1B                        mov rbx, qword ptr [rbx]
00628834  49 3B DE                        cmp rbx, r14
00628837  75 E1                           jne 0x14062881a
00628839  40 84 FF                        test dil, dil
0062883C  74 0C                           je 0x14062884a
0062883E  48 8D 0D 3B B6 8D 00            lea rcx, [rip + 0x8db63b]
00628845  E8 36 16 D2 FF                  call 0x140349e80
0062884A  48 8B CD                        mov rcx, rbp
0062884D  E8 9E 79 2D 00                  call 0x1409001f0
00628852  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00628856  48 85 F6                        test rsi, rsi
00628859  74 64                           je 0x1406288bf
0062885B  40 32 FF                        xor dil, dil
0062885E  40 38 3D 53 C0 8D 00            cmp byte ptr [rip + 0x8dc053], dil
00628865  75 0C                           jne 0x140628873
00628867  F7 05 0F C1 8D 00 00 08 00 00   test dword ptr [rip + 0x8dc10f], 0x800
00628871  74 13                           je 0x140628886
00628873  48 8D 0D 06 B6 8D 00            lea rcx, [rip + 0x8db606]
0062887A  E8 A1 DD BE FF                  call 0x140216620
0062887F  40 8A F8                        mov dil, al
00628882  84 C0                           test al, al
00628884  74 39                           je 0x1406288bf
00628886  48 83 C6 30                     add rsi, 0x30
0062888A  48 8B 1E                        mov rbx, qword ptr [rsi]
0062888D  EB 1A                           jmp 0x1406288a9
0062888F  48 8D 43 F0                     lea rax, [rbx - 0x10]
00628893  48 85 C0                        test rax, rax
00628896  74 0E                           je 0x1406288a6
00628898  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062889C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006288A1  E8 2A 22 09 00                  call 0x1406baad0
006288A6  48 8B 1B                        mov rbx, qword ptr [rbx]
006288A9  48 3B DE                        cmp rbx, rsi
006288AC  75 E1                           jne 0x14062888f
006288AE  40 84 FF                        test dil, dil
006288B1  74 0C                           je 0x1406288bf
006288B3  48 8D 0D C6 B5 8D 00            lea rcx, [rip + 0x8db5c6]
006288BA  E8 C1 15 D2 FF                  call 0x140349e80
006288BF  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
006288C3  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006288C8  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006288CD  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006288D2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006288D7  48 83 C4 40                     add rsp, 0x40
006288DB  41 5E                           pop r14
006288DD  C3                              ret
006288DE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoConnectInterruptExWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
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
    result = DifGetAPIThunkContextById(357, a2, a3, a4);
    if (result == 0) goto loc_0062884A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006287D3;
    v_stack_m28 = v_stack_p0;
    goto loc_006287E1;
loc_006287D3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9289928)) != 0) goto loc_006287FE;
    if (((*(unsigned int *)(v_rip + 9290116)) & (0x800ULL)) == 0) goto loc_00628811;
loc_006287FE:
    result = ExAcquireRundownProtection(v_rip + 9287291, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062884A;
loc_00628811:
    goto loc_00628834;
loc_0062881A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00628834:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062881A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9287227;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoConnectInterruptEx(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_006288BF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9289811)) != 0) goto loc_00628873;
    if (((*(unsigned int *)(v_rip + 9289999)) & (0x800ULL)) == 0) goto loc_00628886;
loc_00628873:
    result = ExAcquireRundownProtection(v_rip + 9287174, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006288BF;
loc_00628886:
    v_rsi = (result) + (48);
    goto loc_006288A9;
loc_0062888F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006288A9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062888F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9287110;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoConnectInterruptExWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
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
    result = DifGetAPIThunkContextById(357, a2, a3, a4);
    if (result == 0) goto loc_0062884A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006287D3;
    v_stack_m28 = v_stack_p0;
    goto loc_006287E1;
loc_006287D3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8DC0C8)) != 0) goto loc_006287FE;
    if (((*(uint32_t *)(v_rip + 0x8DC184)) & (0x800ULL)) == 0) goto loc_00628811;
loc_006287FE:
    result = ExAcquireRundownProtection(v_rip + 9287291, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062884A;
loc_00628811:
    goto loc_00628834;
loc_0062881A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00628834:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062881A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9287227;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = IoConnectInterruptEx(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_006288BF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DC053)) != 0) goto loc_00628873;
    if (((*(uint32_t *)(v_rip + 0x8DC10F)) & (0x800ULL)) == 0) goto loc_00628886;
loc_00628873:
    result = ExAcquireRundownProtection(v_rip + 9287174, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006288BF;
loc_00628886:
    local_rsi = (result) + (48);
    goto loc_006288A9;
loc_0062888F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006288A9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062888F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9287110;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00628780&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00628780[BB_00628780]
  bb_006287C0[BB_006287C0]
  bb_006287C7[BB_006287C7]
  bb_006287D3[BB_006287D3]
  bb_006287D7[BB_006287D7]
  bb_006287E1[BB_006287E1]
  bb_006287F2[BB_006287F2]
  bb_006287FE[BB_006287FE]
  bb_00628811[BB_00628811]
  bb_0062881A[BB_0062881A]
  bb_00628823[BB_00628823]
  bb_00628831[BB_00628831]
  bb_00628834[BB_00628834]
  bb_00628839[BB_00628839]
  bb_0062883E[BB_0062883E]
  bb_0062884A[BB_0062884A]
  bb_0062885B[BB_0062885B]
  bb_00628867[BB_00628867]
  bb_00628873[BB_00628873]
  bb_00628886[BB_00628886]
  bb_0062888F[BB_0062888F]
  bb_00628898[BB_00628898]
  bb_006288A6[BB_006288A6]
  bb_006288A9[BB_006288A9]
  bb_006288AE[BB_006288AE]
  bb_006288B3[BB_006288B3]
  bb_006288BF[BB_006288BF]
  bb_006288DE[BB_006288DE]
  bb_00628780 -->|branch| bb_0062884A
  bb_00628780 -->|fallthrough| bb_006287C0
  bb_006287C0 -->|branch| bb_006287D3
  bb_006287C0 -->|fallthrough| bb_006287C7
  bb_006287C7 -->|branch| bb_006287E1
  bb_006287D3 -->|branch| bb_006287E1
  bb_006287D3 -->|fallthrough| bb_006287D7
  bb_006287D7 -->|flow| bb_006287E1
  bb_006287E1 -->|branch| bb_006287FE
  bb_006287E1 -->|fallthrough| bb_006287F2
  bb_006287F2 -->|branch| bb_00628811
  bb_006287F2 -->|fallthrough| bb_006287FE
  bb_006287FE -->|branch| bb_0062884A
  bb_006287FE -->|fallthrough| bb_00628811
  bb_00628811 -->|branch| bb_00628834
  bb_0062881A -->|branch| bb_00628831
  bb_0062881A -->|fallthrough| bb_00628823
  bb_00628823 -->|flow| bb_00628831
  bb_00628831 -->|flow| bb_00628834
  bb_00628834 -->|branch| bb_0062881A
  bb_00628834 -->|fallthrough| bb_00628839
  bb_00628839 -->|branch| bb_0062884A
  bb_00628839 -->|fallthrough| bb_0062883E
  bb_0062883E -->|flow| bb_0062884A
  bb_0062884A -->|branch| bb_006288BF
  bb_0062884A -->|fallthrough| bb_0062885B
  bb_0062885B -->|branch| bb_00628873
  bb_0062885B -->|fallthrough| bb_00628867
  bb_00628867 -->|branch| bb_00628886
  bb_00628867 -->|fallthrough| bb_00628873
  bb_00628873 -->|branch| bb_006288BF
  bb_00628873 -->|fallthrough| bb_00628886
  bb_00628886 -->|branch| bb_006288A9
  bb_0062888F -->|branch| bb_006288A6
  bb_0062888F -->|fallthrough| bb_00628898
  bb_00628898 -->|flow| bb_006288A6
  bb_006288A6 -->|flow| bb_006288A9
  bb_006288A9 -->|branch| bb_0062888F
  bb_006288A9 -->|fallthrough| bb_006288AE
  bb_006288AE -->|branch| bb_006288BF
  bb_006288AE -->|fallthrough| bb_006288B3
  bb_006288B3 -->|flow| bb_006288BF
```
