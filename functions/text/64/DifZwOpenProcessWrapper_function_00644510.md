# DifZwOpenProcessWrapper

- RVA: `0x00644510`–`0x00644695` (길이 `389` bytes)
- VA: `0x0000000140644510`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `112`개 명령, `389/389` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00644550` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00644576` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006445B2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006445D8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006445F1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00644603` → [ZwOpenProcess](../6A/ZwOpenProcess_function_006AD590.md) (function, `0x006AD590`)
- `0x0064462F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00644655` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064466E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00644586` → RVA `0x00F048B8` (`.data`; read)
- `0x0064459F` → RVA `0x00F04980` (`.data`; read)
- `0x006445AB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00644510  48 8B C4                        mov rax, rsp
00644513  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00644517  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064451B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064451F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00644523  55                              push rbp
00644524  41 54                           push r12
00644526  41 55                           push r13
00644528  41 56                           push r14
0064452A  41 57                           push r15
0064452C  48 8B EC                        mov rbp, rsp
0064452F  48 83 EC 50                     sub rsp, 0x50
00644533  0F 57 C0                        xorps xmm0, xmm0
00644536  B9 4F 00 00 00                  mov ecx, 0x4f
0064453B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064453F  4D 8B F9                        mov r15, r9
00644542  4D 8B E0                        mov r12, r8
00644545  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00644549  44 8B EA                        mov r13d, edx
0064454C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00644550  E8 DF 14 E5 FF                  call 0x140495a34
00644555  48 8B F0                        mov rsi, rax
00644558  48 85 C0                        test rax, rax
0064455B  0F 84 95 00 00 00               je 0x1406445f6
00644561  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00644564  A8 18                           test al, 0x18
00644566  74 0A                           je 0x140644572
00644568  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064456C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00644570  EB 0D                           jmp 0x14064457f
00644572  A8 04                           test al, 4
00644574  74 09                           je 0x14064457f
00644576  E8 8D F6 E8 FF                  call 0x1404d3c08
0064457B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064457F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00644583  45 32 F6                        xor r14b, r14b
00644586  44 38 35 2B 03 8C 00            cmp byte ptr [rip + 0x8c032b], r14b
0064458D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00644591  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
00644595  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00644599  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0064459D  75 0C                           jne 0x1406445ab
0064459F  F7 05 D7 03 8C 00 00 08 00 00   test dword ptr [rip + 0x8c03d7], 0x800
006445A9  74 13                           je 0x1406445be
006445AB  48 8D 0D CE F8 8B 00            lea rcx, [rip + 0x8bf8ce]
006445B2  E8 69 20 BD FF                  call 0x140216620
006445B7  44 8A F0                        mov r14b, al
006445BA  84 C0                           test al, al
006445BC  74 38                           je 0x1406445f6
006445BE  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006445C2  48 8B 1F                        mov rbx, qword ptr [rdi]
006445C5  EB 19                           jmp 0x1406445e0
006445C7  48 8D 43 F0                     lea rax, [rbx - 0x10]
006445CB  48 85 C0                        test rax, rax
006445CE  74 0D                           je 0x1406445dd
006445D0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006445D4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006445D8  E8 F3 64 07 00                  call 0x1406baad0
006445DD  48 8B 1B                        mov rbx, qword ptr [rbx]
006445E0  48 3B DF                        cmp rbx, rdi
006445E3  75 E2                           jne 0x1406445c7
006445E5  45 84 F6                        test r14b, r14b
006445E8  74 0C                           je 0x1406445f6
006445EA  48 8D 0D 8F F8 8B 00            lea rcx, [rip + 0x8bf88f]
006445F1  E8 8A 58 D0 FF                  call 0x140349e80
006445F6  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006445FA  4D 8B CF                        mov r9, r15
006445FD  4D 8B C4                        mov r8, r12
00644600  41 8B D5                        mov edx, r13d
00644603  E8 88 8F 06 00                  call 0x1406ad590
00644608  89 45 F8                        mov dword ptr [rbp - 8], eax
0064460B  48 85 F6                        test rsi, rsi
0064460E  74 63                           je 0x140644673
00644610  40 32 FF                        xor dil, dil
00644613  40 38 3D 9E 02 8C 00            cmp byte ptr [rip + 0x8c029e], dil
0064461A  75 0C                           jne 0x140644628
0064461C  F7 05 5A 03 8C 00 00 08 00 00   test dword ptr [rip + 0x8c035a], 0x800
00644626  74 13                           je 0x14064463b
00644628  48 8D 0D 51 F8 8B 00            lea rcx, [rip + 0x8bf851]
0064462F  E8 EC 1F BD FF                  call 0x140216620
00644634  40 8A F8                        mov dil, al
00644637  84 C0                           test al, al
00644639  74 38                           je 0x140644673
0064463B  48 83 C6 30                     add rsi, 0x30
0064463F  48 8B 1E                        mov rbx, qword ptr [rsi]
00644642  EB 19                           jmp 0x14064465d
00644644  48 8D 43 F0                     lea rax, [rbx - 0x10]
00644648  48 85 C0                        test rax, rax
0064464B  74 0D                           je 0x14064465a
0064464D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644651  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00644655  E8 76 64 07 00                  call 0x1406baad0
0064465A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064465D  48 3B DE                        cmp rbx, rsi
00644660  75 E2                           jne 0x140644644
00644662  40 84 FF                        test dil, dil
00644665  74 0C                           je 0x140644673
00644667  48 8D 0D 12 F8 8B 00            lea rcx, [rip + 0x8bf812]
0064466E  E8 0D 58 D0 FF                  call 0x140349e80
00644673  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00644676  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064467B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064467F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00644683  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00644687  49 8B E3                        mov rsp, r11
0064468A  41 5F                           pop r15
0064468C  41 5E                           pop r14
0064468E  41 5D                           pop r13
00644690  41 5C                           pop r12
00644692  5D                              pop rbp
00644693  C3                              ret
00644694  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenProcessWrapper(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
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
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(79, a2, a3, a4);
    if (result == 0) goto loc_006445F6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00644572;
    v_stack_m58 = v_stack_p0;
    goto loc_0064457F;
loc_00644572:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9175851)) != 0) goto loc_006445AB;
    if (((*(unsigned int *)(v_rip + 9176023)) & (0x800ULL)) == 0) goto loc_006445BE;
loc_006445AB:
    result = ExAcquireRundownProtection(v_rip + 9173198, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006445F6;
loc_006445BE:
    goto loc_006445E0;
loc_006445C7:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006445E0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006445C7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9173135;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenProcess(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00644673;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9175710)) != 0) goto loc_00644628;
    if (((*(unsigned int *)(v_rip + 9175898)) & (0x800ULL)) == 0) goto loc_0064463B;
loc_00644628:
    result = ExAcquireRundownProtection(v_rip + 9173073, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00644673;
loc_0064463B:
    v_rsi = (result) + (48);
    goto loc_0064465D;
loc_00644644:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0064465D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00644644;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9173010;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenProcessWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
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
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(79, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006445F6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00644572;
    v_stack_m58 = v_stack_p0;
    goto loc_0064457F;
loc_00644572:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C032B)) != 0) goto loc_006445AB;
    if (((*(uint32_t *)(v_rip + 0x8C03D7)) & (0x800ULL)) == 0) goto loc_006445BE;
loc_006445AB:
    result = ExAcquireRundownProtection(v_rip + 9173198, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006445F6;
loc_006445BE:
    goto loc_006445E0;
loc_006445C7:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006445E0:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006445C7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9173135;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwOpenProcess(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00644673;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C029E)) != 0) goto loc_00644628;
    if (((*(uint32_t *)(v_rip + 0x8C035A)) & (0x800ULL)) == 0) goto loc_0064463B;
loc_00644628:
    result = ExAcquireRundownProtection(v_rip + 9173073, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00644673;
loc_0064463B:
    local_rsi = (result) + (48);
    goto loc_0064465D;
loc_00644644:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_0064465D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00644644;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9173010;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00644510&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00644510[BB_00644510]
  bb_00644561[BB_00644561]
  bb_00644568[BB_00644568]
  bb_00644572[BB_00644572]
  bb_00644576[BB_00644576]
  bb_0064457F[BB_0064457F]
  bb_0064459F[BB_0064459F]
  bb_006445AB[BB_006445AB]
  bb_006445BE[BB_006445BE]
  bb_006445C7[BB_006445C7]
  bb_006445D0[BB_006445D0]
  bb_006445DD[BB_006445DD]
  bb_006445E0[BB_006445E0]
  bb_006445E5[BB_006445E5]
  bb_006445EA[BB_006445EA]
  bb_006445F6[BB_006445F6]
  bb_00644610[BB_00644610]
  bb_0064461C[BB_0064461C]
  bb_00644628[BB_00644628]
  bb_0064463B[BB_0064463B]
  bb_00644644[BB_00644644]
  bb_0064464D[BB_0064464D]
  bb_0064465A[BB_0064465A]
  bb_0064465D[BB_0064465D]
  bb_00644662[BB_00644662]
  bb_00644667[BB_00644667]
  bb_00644673[BB_00644673]
  bb_00644694[BB_00644694]
  bb_00644510 -->|branch| bb_006445F6
  bb_00644510 -->|fallthrough| bb_00644561
  bb_00644561 -->|branch| bb_00644572
  bb_00644561 -->|fallthrough| bb_00644568
  bb_00644568 -->|branch| bb_0064457F
  bb_00644572 -->|branch| bb_0064457F
  bb_00644572 -->|fallthrough| bb_00644576
  bb_00644576 -->|flow| bb_0064457F
  bb_0064457F -->|branch| bb_006445AB
  bb_0064457F -->|fallthrough| bb_0064459F
  bb_0064459F -->|branch| bb_006445BE
  bb_0064459F -->|fallthrough| bb_006445AB
  bb_006445AB -->|branch| bb_006445F6
  bb_006445AB -->|fallthrough| bb_006445BE
  bb_006445BE -->|branch| bb_006445E0
  bb_006445C7 -->|branch| bb_006445DD
  bb_006445C7 -->|fallthrough| bb_006445D0
  bb_006445D0 -->|flow| bb_006445DD
  bb_006445DD -->|flow| bb_006445E0
  bb_006445E0 -->|branch| bb_006445C7
  bb_006445E0 -->|fallthrough| bb_006445E5
  bb_006445E5 -->|branch| bb_006445F6
  bb_006445E5 -->|fallthrough| bb_006445EA
  bb_006445EA -->|flow| bb_006445F6
  bb_006445F6 -->|branch| bb_00644673
  bb_006445F6 -->|fallthrough| bb_00644610
  bb_00644610 -->|branch| bb_00644628
  bb_00644610 -->|fallthrough| bb_0064461C
  bb_0064461C -->|branch| bb_0064463B
  bb_0064461C -->|fallthrough| bb_00644628
  bb_00644628 -->|branch| bb_00644673
  bb_00644628 -->|fallthrough| bb_0064463B
  bb_0064463B -->|branch| bb_0064465D
  bb_00644644 -->|branch| bb_0064465A
  bb_00644644 -->|fallthrough| bb_0064464D
  bb_0064464D -->|flow| bb_0064465A
  bb_0064465A -->|flow| bb_0064465D
  bb_0064465D -->|branch| bb_00644644
  bb_0064465D -->|fallthrough| bb_00644662
  bb_00644662 -->|branch| bb_00644673
  bb_00644662 -->|fallthrough| bb_00644667
  bb_00644667 -->|flow| bb_00644673
```
