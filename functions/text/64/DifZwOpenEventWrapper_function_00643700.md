# DifZwOpenEventWrapper

- RVA: `0x00643700`–`0x00643875` (길이 `373` bytes)
- VA: `0x0000000140643700`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `373/373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064373C` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00643762` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00643796` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006437BC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006437D5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006437E3` → [ZwOpenEvent](../6A/ZwOpenEvent_function_006AD8D0.md) (function, `0x006AD8D0`)
- `0x0064380F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00643835` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064384E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00643772` → RVA `0x00F048B8` (`.data`; read)
- `0x00643783` → RVA `0x00F04980` (`.data`; read)
- `0x0064378F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00643700  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00643705  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0064370A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0064370F  55                              push rbp
00643710  41 54                           push r12
00643712  41 55                           push r13
00643714  41 56                           push r14
00643716  41 57                           push r15
00643718  48 8B EC                        mov rbp, rsp
0064371B  48 83 EC 50                     sub rsp, 0x50
0064371F  33 C0                           xor eax, eax
00643721  0F 57 C0                        xorps xmm0, xmm0
00643724  4C 8B E9                        mov r13, rcx
00643727  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064372B  4D 8B F8                        mov r15, r8
0064372E  44 8B E2                        mov r12d, edx
00643731  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00643735  8D 48 56                        lea ecx, [rax + 0x56]
00643738  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0064373C  E8 F3 22 E5 FF                  call 0x140495a34
00643741  48 8B F0                        mov rsi, rax
00643744  48 85 C0                        test rax, rax
00643747  0F 84 8D 00 00 00               je 0x1406437da
0064374D  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00643750  A8 18                           test al, 0x18
00643752  74 0A                           je 0x14064375e
00643754  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00643758  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0064375C  EB 0D                           jmp 0x14064376b
0064375E  A8 04                           test al, 4
00643760  74 09                           je 0x14064376b
00643762  E8 A1 04 E9 FF                  call 0x1404d3c08
00643767  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064376B  45 32 F6                        xor r14b, r14b
0064376E  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00643772  44 38 35 3F 11 8C 00            cmp byte ptr [rip + 0x8c113f], r14b
00643779  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
0064377D  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00643781  75 0C                           jne 0x14064378f
00643783  F7 05 F3 11 8C 00 00 08 00 00   test dword ptr [rip + 0x8c11f3], 0x800
0064378D  74 13                           je 0x1406437a2
0064378F  48 8D 0D EA 06 8C 00            lea rcx, [rip + 0x8c06ea]
00643796  E8 85 2E BD FF                  call 0x140216620
0064379B  44 8A F0                        mov r14b, al
0064379E  84 C0                           test al, al
006437A0  74 38                           je 0x1406437da
006437A2  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006437A6  48 8B 1F                        mov rbx, qword ptr [rdi]
006437A9  EB 19                           jmp 0x1406437c4
006437AB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006437AF  48 85 C0                        test rax, rax
006437B2  74 0D                           je 0x1406437c1
006437B4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006437B8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006437BC  E8 0F 73 07 00                  call 0x1406baad0
006437C1  48 8B 1B                        mov rbx, qword ptr [rbx]
006437C4  48 3B DF                        cmp rbx, rdi
006437C7  75 E2                           jne 0x1406437ab
006437C9  45 84 F6                        test r14b, r14b
006437CC  74 0C                           je 0x1406437da
006437CE  48 8D 0D AB 06 8C 00            lea rcx, [rip + 0x8c06ab]
006437D5  E8 A6 66 D0 FF                  call 0x140349e80
006437DA  4D 8B C7                        mov r8, r15
006437DD  41 8B D4                        mov edx, r12d
006437E0  49 8B CD                        mov rcx, r13
006437E3  E8 E8 A0 06 00                  call 0x1406ad8d0
006437E8  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006437EB  48 85 F6                        test rsi, rsi
006437EE  74 63                           je 0x140643853
006437F0  40 32 FF                        xor dil, dil
006437F3  40 38 3D BE 10 8C 00            cmp byte ptr [rip + 0x8c10be], dil
006437FA  75 0C                           jne 0x140643808
006437FC  F7 05 7A 11 8C 00 00 08 00 00   test dword ptr [rip + 0x8c117a], 0x800
00643806  74 13                           je 0x14064381b
00643808  48 8D 0D 71 06 8C 00            lea rcx, [rip + 0x8c0671]
0064380F  E8 0C 2E BD FF                  call 0x140216620
00643814  40 8A F8                        mov dil, al
00643817  84 C0                           test al, al
00643819  74 38                           je 0x140643853
0064381B  48 83 C6 30                     add rsi, 0x30
0064381F  48 8B 1E                        mov rbx, qword ptr [rsi]
00643822  EB 19                           jmp 0x14064383d
00643824  48 8D 43 F0                     lea rax, [rbx - 0x10]
00643828  48 85 C0                        test rax, rax
0064382B  74 0D                           je 0x14064383a
0064382D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00643831  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00643835  E8 96 72 07 00                  call 0x1406baad0
0064383A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064383D  48 3B DE                        cmp rbx, rsi
00643840  75 E2                           jne 0x140643824
00643842  40 84 FF                        test dil, dil
00643845  74 0C                           je 0x140643853
00643847  48 8D 0D 32 06 8C 00            lea rcx, [rip + 0x8c0632]
0064384E  E8 2D 66 D0 FF                  call 0x140349e80
00643853  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00643856  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064385B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0064385F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00643863  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00643867  49 8B E3                        mov rsp, r11
0064386A  41 5F                           pop r15
0064386C  41 5E                           pop r14
0064386E  41 5D                           pop r13
00643870  41 5C                           pop r12
00643872  5D                              pop rbp
00643873  C3                              ret
00643874  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenEventWrapper(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 86, a2, a3, a4);
    if (result == 0) goto loc_006437DA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064375E;
    v_stack_m58 = v_stack_p0;
    goto loc_0064376B;
loc_0064375E:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9179455)) != 0) goto loc_0064378F;
    if (((*(unsigned int *)(v_rip + 9179635)) & (0x800ULL)) == 0) goto loc_006437A2;
loc_0064378F:
    result = ExAcquireRundownProtection(v_rip + 9176810, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006437DA;
loc_006437A2:
    goto loc_006437C4;
loc_006437AB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006437C4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006437AB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9176747;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenEvent(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00643853;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9179326)) != 0) goto loc_00643808;
    if (((*(unsigned int *)(v_rip + 9179514)) & (0x800ULL)) == 0) goto loc_0064381B;
loc_00643808:
    result = ExAcquireRundownProtection(v_rip + 9176689, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00643853;
loc_0064381B:
    v_rsi = (result) + (48);
    goto loc_0064383D;
loc_00643824:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0064383D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00643824;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9176626;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenEventWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 86, Arg2, Arg3, a4);
    if (result == 0) goto loc_006437DA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064375E;
    v_stack_m58 = v_stack_p0;
    goto loc_0064376B;
loc_0064375E:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C113F)) != 0) goto loc_0064378F;
    if (((*(uint32_t *)(v_rip + 0x8C11F3)) & (0x800ULL)) == 0) goto loc_006437A2;
loc_0064378F:
    result = ExAcquireRundownProtection(v_rip + 9176810, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006437DA;
loc_006437A2:
    goto loc_006437C4;
loc_006437AB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_006437C4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006437AB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9176747;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwOpenEvent(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00643853;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C10BE)) != 0) goto loc_00643808;
    if (((*(uint32_t *)(v_rip + 0x8C117A)) & (0x800ULL)) == 0) goto loc_0064381B;
loc_00643808:
    result = ExAcquireRundownProtection(v_rip + 9176689, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00643853;
loc_0064381B:
    local_rsi = (result) + (48);
    goto loc_0064383D;
loc_00643824:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_0064383D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00643824;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9176626;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00643700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00643700[BB_00643700]
  bb_0064374D[BB_0064374D]
  bb_00643754[BB_00643754]
  bb_0064375E[BB_0064375E]
  bb_00643762[BB_00643762]
  bb_0064376B[BB_0064376B]
  bb_00643783[BB_00643783]
  bb_0064378F[BB_0064378F]
  bb_006437A2[BB_006437A2]
  bb_006437AB[BB_006437AB]
  bb_006437B4[BB_006437B4]
  bb_006437C1[BB_006437C1]
  bb_006437C4[BB_006437C4]
  bb_006437C9[BB_006437C9]
  bb_006437CE[BB_006437CE]
  bb_006437DA[BB_006437DA]
  bb_006437F0[BB_006437F0]
  bb_006437FC[BB_006437FC]
  bb_00643808[BB_00643808]
  bb_0064381B[BB_0064381B]
  bb_00643824[BB_00643824]
  bb_0064382D[BB_0064382D]
  bb_0064383A[BB_0064383A]
  bb_0064383D[BB_0064383D]
  bb_00643842[BB_00643842]
  bb_00643847[BB_00643847]
  bb_00643853[BB_00643853]
  bb_00643874[BB_00643874]
  bb_00643700 -->|branch| bb_006437DA
  bb_00643700 -->|fallthrough| bb_0064374D
  bb_0064374D -->|branch| bb_0064375E
  bb_0064374D -->|fallthrough| bb_00643754
  bb_00643754 -->|branch| bb_0064376B
  bb_0064375E -->|branch| bb_0064376B
  bb_0064375E -->|fallthrough| bb_00643762
  bb_00643762 -->|flow| bb_0064376B
  bb_0064376B -->|branch| bb_0064378F
  bb_0064376B -->|fallthrough| bb_00643783
  bb_00643783 -->|branch| bb_006437A2
  bb_00643783 -->|fallthrough| bb_0064378F
  bb_0064378F -->|branch| bb_006437DA
  bb_0064378F -->|fallthrough| bb_006437A2
  bb_006437A2 -->|branch| bb_006437C4
  bb_006437AB -->|branch| bb_006437C1
  bb_006437AB -->|fallthrough| bb_006437B4
  bb_006437B4 -->|flow| bb_006437C1
  bb_006437C1 -->|flow| bb_006437C4
  bb_006437C4 -->|branch| bb_006437AB
  bb_006437C4 -->|fallthrough| bb_006437C9
  bb_006437C9 -->|branch| bb_006437DA
  bb_006437C9 -->|fallthrough| bb_006437CE
  bb_006437CE -->|flow| bb_006437DA
  bb_006437DA -->|branch| bb_00643853
  bb_006437DA -->|fallthrough| bb_006437F0
  bb_006437F0 -->|branch| bb_00643808
  bb_006437F0 -->|fallthrough| bb_006437FC
  bb_006437FC -->|branch| bb_0064381B
  bb_006437FC -->|fallthrough| bb_00643808
  bb_00643808 -->|branch| bb_00643853
  bb_00643808 -->|fallthrough| bb_0064381B
  bb_0064381B -->|branch| bb_0064383D
  bb_00643824 -->|branch| bb_0064383A
  bb_00643824 -->|fallthrough| bb_0064382D
  bb_0064382D -->|flow| bb_0064383A
  bb_0064383A -->|flow| bb_0064383D
  bb_0064383D -->|branch| bb_00643824
  bb_0064383D -->|fallthrough| bb_00643842
  bb_00643842 -->|branch| bb_00643853
  bb_00643842 -->|fallthrough| bb_00643847
  bb_00643847 -->|flow| bb_00643853
```
