# DifProbeForWriteWrapper

- RVA: `0x0063A770`–`0x0063A8E2` (길이 `370` bytes)
- VA: `0x000000014063A770`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `101`개 명령, `370/370` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063A7A6` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063A7CE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063A806` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063A82D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063A846` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063A854` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x0063A87D` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063A8A4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063A8BD` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063A7E0` → RVA `0x00F048B8` (`.data`; read)
- `0x0063A7F3` → RVA `0x00F04980` (`.data`; read)
- `0x0063A7FF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063A854` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063A770  48 8B C4                        mov rax, rsp
0063A773  48 89 58 08                     mov qword ptr [rax + 8], rbx
0063A777  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063A77B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063A77F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063A783  41 54                           push r12
0063A785  41 56                           push r14
0063A787  41 57                           push r15
0063A789  48 83 EC 40                     sub rsp, 0x40
0063A78D  0F 57 C0                        xorps xmm0, xmm0
0063A790  4C 8B E1                        mov r12, rcx
0063A793  B9 B0 00 00 00                  mov ecx, 0xb0
0063A798  45 8B F0                        mov r14d, r8d
0063A79B  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063A79F  4C 8B FA                        mov r15, rdx
0063A7A2  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0063A7A6  E8 89 B2 E5 FF                  call 0x140495a34
0063A7AB  48 8B F0                        mov rsi, rax
0063A7AE  48 85 C0                        test rax, rax
0063A7B1  0F 84 94 00 00 00               je 0x14063a84b
0063A7B7  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063A7BA  A8 18                           test al, 0x18
0063A7BC  74 0C                           je 0x14063a7ca
0063A7BE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063A7C3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063A7C8  EB 0E                           jmp 0x14063a7d8
0063A7CA  A8 04                           test al, 4
0063A7CC  74 0A                           je 0x14063a7d8
0063A7CE  E8 35 94 E9 FF                  call 0x1404d3c08
0063A7D3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063A7D8  40 32 ED                        xor bpl, bpl
0063A7DB  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0063A7E0  40 38 2D D1 A0 8C 00            cmp byte ptr [rip + 0x8ca0d1], bpl
0063A7E7  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0063A7EC  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0063A7F1  75 0C                           jne 0x14063a7ff
0063A7F3  F7 05 83 A1 8C 00 00 08 00 00   test dword ptr [rip + 0x8ca183], 0x800
0063A7FD  74 13                           je 0x14063a812
0063A7FF  48 8D 0D 7A 96 8C 00            lea rcx, [rip + 0x8c967a]
0063A806  E8 15 BE BD FF                  call 0x140216620
0063A80B  40 8A E8                        mov bpl, al
0063A80E  84 C0                           test al, al
0063A810  74 39                           je 0x14063a84b
0063A812  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063A816  48 8B 1F                        mov rbx, qword ptr [rdi]
0063A819  EB 1A                           jmp 0x14063a835
0063A81B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063A81F  48 85 C0                        test rax, rax
0063A822  74 0E                           je 0x14063a832
0063A824  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063A828  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063A82D  E8 9E 02 08 00                  call 0x1406baad0
0063A832  48 8B 1B                        mov rbx, qword ptr [rbx]
0063A835  48 3B DF                        cmp rbx, rdi
0063A838  75 E1                           jne 0x14063a81b
0063A83A  40 84 ED                        test bpl, bpl
0063A83D  74 0C                           je 0x14063a84b
0063A83F  48 8D 0D 3A 96 8C 00            lea rcx, [rip + 0x8c963a]
0063A846  E8 35 F6 D0 FF                  call 0x140349e80
0063A84B  45 8B C6                        mov r8d, r14d
0063A84E  49 8B D7                        mov rdx, r15
0063A851  49 8B CC                        mov rcx, r12
0063A854  E8 67 E9 2A 00                  call 0x1408e91c0
0063A859  48 85 F6                        test rsi, rsi
0063A85C  74 64                           je 0x14063a8c2
0063A85E  40 32 FF                        xor dil, dil
0063A861  40 38 3D 50 A0 8C 00            cmp byte ptr [rip + 0x8ca050], dil
0063A868  75 0C                           jne 0x14063a876
0063A86A  F7 05 0C A1 8C 00 00 08 00 00   test dword ptr [rip + 0x8ca10c], 0x800
0063A874  74 13                           je 0x14063a889
0063A876  48 8D 0D 03 96 8C 00            lea rcx, [rip + 0x8c9603]
0063A87D  E8 9E BD BD FF                  call 0x140216620
0063A882  40 8A F8                        mov dil, al
0063A885  84 C0                           test al, al
0063A887  74 39                           je 0x14063a8c2
0063A889  48 83 C6 30                     add rsi, 0x30
0063A88D  48 8B 1E                        mov rbx, qword ptr [rsi]
0063A890  EB 1A                           jmp 0x14063a8ac
0063A892  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063A896  48 85 C0                        test rax, rax
0063A899  74 0E                           je 0x14063a8a9
0063A89B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063A89F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063A8A4  E8 27 02 08 00                  call 0x1406baad0
0063A8A9  48 8B 1B                        mov rbx, qword ptr [rbx]
0063A8AC  48 3B DE                        cmp rbx, rsi
0063A8AF  75 E1                           jne 0x14063a892
0063A8B1  40 84 FF                        test dil, dil
0063A8B4  74 0C                           je 0x14063a8c2
0063A8B6  48 8D 0D C3 95 8C 00            lea rcx, [rip + 0x8c95c3]
0063A8BD  E8 BE F5 D0 FF                  call 0x140349e80
0063A8C2  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063A8C7  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0063A8CC  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0063A8D1  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0063A8D6  48 83 C4 40                     add rsp, 0x40
0063A8DA  41 5F                           pop r15
0063A8DC  41 5E                           pop r14
0063A8DE  41 5C                           pop r12
0063A8E0  C3                              ret
0063A8E1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifProbeForWriteWrapper(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
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
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(176, a2, a3, a4);
    if (result == 0) goto loc_0063A84B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063A7CA;
    v_stack_m38 = v_stack_p0;
    goto loc_0063A7D8;
loc_0063A7CA:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = a1;
    v_stack_m28 = a2;
    v_stack_m30 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9216209)) != 0) goto loc_0063A7FF;
    if (((*(unsigned int *)(v_rip + 9216387)) & (0x800ULL)) == 0) goto loc_0063A812;
loc_0063A7FF:
    result = ExAcquireRundownProtection(v_rip + 9213562, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063A84B;
loc_0063A812:
    goto loc_0063A835;
loc_0063A81B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063A835:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063A81B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9213498;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ProbeForWrite(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if (result == 0) goto loc_0063A8C2;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9216080)) != 0) goto loc_0063A876;
    if (((*(unsigned int *)(v_rip + 9216268)) & (0x800ULL)) == 0) goto loc_0063A889;
loc_0063A876:
    result = ExAcquireRundownProtection(v_rip + 9213443, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063A8C2;
loc_0063A889:
    v_rsi = (result) + (48);
    goto loc_0063A8AC;
loc_0063A892:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0063A8AC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063A892;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9213379;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifProbeForWriteWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
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
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(176, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063A84B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063A7CA;
    v_stack_m38 = v_stack_p0;
    goto loc_0063A7D8;
loc_0063A7CA:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = Arg1;
    v_stack_m28 = Arg2;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8CA0D1)) != 0) goto loc_0063A7FF;
    if (((*(uint32_t *)(v_rip + 0x8CA183)) & (0x800ULL)) == 0) goto loc_0063A812;
loc_0063A7FF:
    result = ExAcquireRundownProtection(v_rip + 9213562, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063A84B;
loc_0063A812:
    goto loc_0063A835;
loc_0063A81B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063A835:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063A81B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9213498;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ProbeForWrite(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if (result == 0) goto loc_0063A8C2;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CA050)) != 0) goto loc_0063A876;
    if (((*(uint32_t *)(v_rip + 0x8CA10C)) & (0x800ULL)) == 0) goto loc_0063A889;
loc_0063A876:
    result = ExAcquireRundownProtection(v_rip + 9213443, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint8_t)(result) == 0) goto loc_0063A8C2;
loc_0063A889:
    local_rsi = (result) + (48);
    goto loc_0063A8AC;
loc_0063A892:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
loc_0063A8AC:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063A892;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9213379;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063A770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063A770[BB_0063A770]
  bb_0063A7B7[BB_0063A7B7]
  bb_0063A7BE[BB_0063A7BE]
  bb_0063A7CA[BB_0063A7CA]
  bb_0063A7CE[BB_0063A7CE]
  bb_0063A7D8[BB_0063A7D8]
  bb_0063A7F3[BB_0063A7F3]
  bb_0063A7FF[BB_0063A7FF]
  bb_0063A812[BB_0063A812]
  bb_0063A81B[BB_0063A81B]
  bb_0063A824[BB_0063A824]
  bb_0063A832[BB_0063A832]
  bb_0063A835[BB_0063A835]
  bb_0063A83A[BB_0063A83A]
  bb_0063A83F[BB_0063A83F]
  bb_0063A84B[BB_0063A84B]
  bb_0063A85E[BB_0063A85E]
  bb_0063A86A[BB_0063A86A]
  bb_0063A876[BB_0063A876]
  bb_0063A889[BB_0063A889]
  bb_0063A892[BB_0063A892]
  bb_0063A89B[BB_0063A89B]
  bb_0063A8A9[BB_0063A8A9]
  bb_0063A8AC[BB_0063A8AC]
  bb_0063A8B1[BB_0063A8B1]
  bb_0063A8B6[BB_0063A8B6]
  bb_0063A8C2[BB_0063A8C2]
  bb_0063A8E1[BB_0063A8E1]
  bb_0063A770 -->|branch| bb_0063A84B
  bb_0063A770 -->|fallthrough| bb_0063A7B7
  bb_0063A7B7 -->|branch| bb_0063A7CA
  bb_0063A7B7 -->|fallthrough| bb_0063A7BE
  bb_0063A7BE -->|branch| bb_0063A7D8
  bb_0063A7CA -->|branch| bb_0063A7D8
  bb_0063A7CA -->|fallthrough| bb_0063A7CE
  bb_0063A7CE -->|flow| bb_0063A7D8
  bb_0063A7D8 -->|branch| bb_0063A7FF
  bb_0063A7D8 -->|fallthrough| bb_0063A7F3
  bb_0063A7F3 -->|branch| bb_0063A812
  bb_0063A7F3 -->|fallthrough| bb_0063A7FF
  bb_0063A7FF -->|branch| bb_0063A84B
  bb_0063A7FF -->|fallthrough| bb_0063A812
  bb_0063A812 -->|branch| bb_0063A835
  bb_0063A81B -->|branch| bb_0063A832
  bb_0063A81B -->|fallthrough| bb_0063A824
  bb_0063A824 -->|flow| bb_0063A832
  bb_0063A832 -->|flow| bb_0063A835
  bb_0063A835 -->|branch| bb_0063A81B
  bb_0063A835 -->|fallthrough| bb_0063A83A
  bb_0063A83A -->|branch| bb_0063A84B
  bb_0063A83A -->|fallthrough| bb_0063A83F
  bb_0063A83F -->|flow| bb_0063A84B
  bb_0063A84B -->|branch| bb_0063A8C2
  bb_0063A84B -->|fallthrough| bb_0063A85E
  bb_0063A85E -->|branch| bb_0063A876
  bb_0063A85E -->|fallthrough| bb_0063A86A
  bb_0063A86A -->|branch| bb_0063A889
  bb_0063A86A -->|fallthrough| bb_0063A876
  bb_0063A876 -->|branch| bb_0063A8C2
  bb_0063A876 -->|fallthrough| bb_0063A889
  bb_0063A889 -->|branch| bb_0063A8AC
  bb_0063A892 -->|branch| bb_0063A8A9
  bb_0063A892 -->|fallthrough| bb_0063A89B
  bb_0063A89B -->|flow| bb_0063A8A9
  bb_0063A8A9 -->|flow| bb_0063A8AC
  bb_0063A8AC -->|branch| bb_0063A892
  bb_0063A8AC -->|fallthrough| bb_0063A8B1
  bb_0063A8B1 -->|branch| bb_0063A8C2
  bb_0063A8B1 -->|fallthrough| bb_0063A8B6
  bb_0063A8B6 -->|flow| bb_0063A8C2
```
