# DifZwOpenKeyWrapper

- RVA: `0x00644080`–`0x006441F5` (길이 `373` bytes)
- VA: `0x0000000140644080`
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
- `0x006440BC` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006440E2` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00644116` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064413C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00644155` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00644163` → [ZwOpenKey](../6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x0064418F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006441B5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006441CE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006440F2` → RVA `0x00F048B8` (`.data`; read)
- `0x00644103` → RVA `0x00F04980` (`.data`; read)
- `0x0064410F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00644080  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00644085  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0064408A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0064408F  55                              push rbp
00644090  41 54                           push r12
00644092  41 55                           push r13
00644094  41 56                           push r14
00644096  41 57                           push r15
00644098  48 8B EC                        mov rbp, rsp
0064409B  48 83 EC 50                     sub rsp, 0x50
0064409F  33 C0                           xor eax, eax
006440A1  0F 57 C0                        xorps xmm0, xmm0
006440A4  4C 8B E9                        mov r13, rcx
006440A7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006440AB  4D 8B F8                        mov r15, r8
006440AE  44 8B E2                        mov r12d, edx
006440B1  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006440B5  8D 48 53                        lea ecx, [rax + 0x53]
006440B8  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006440BC  E8 73 19 E5 FF                  call 0x140495a34
006440C1  48 8B F0                        mov rsi, rax
006440C4  48 85 C0                        test rax, rax
006440C7  0F 84 8D 00 00 00               je 0x14064415a
006440CD  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006440D0  A8 18                           test al, 0x18
006440D2  74 0A                           je 0x1406440de
006440D4  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006440D8  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
006440DC  EB 0D                           jmp 0x1406440eb
006440DE  A8 04                           test al, 4
006440E0  74 09                           je 0x1406440eb
006440E2  E8 21 FB E8 FF                  call 0x1404d3c08
006440E7  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006440EB  45 32 F6                        xor r14b, r14b
006440EE  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
006440F2  44 38 35 BF 07 8C 00            cmp byte ptr [rip + 0x8c07bf], r14b
006440F9  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
006440FD  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00644101  75 0C                           jne 0x14064410f
00644103  F7 05 73 08 8C 00 00 08 00 00   test dword ptr [rip + 0x8c0873], 0x800
0064410D  74 13                           je 0x140644122
0064410F  48 8D 0D 6A FD 8B 00            lea rcx, [rip + 0x8bfd6a]
00644116  E8 05 25 BD FF                  call 0x140216620
0064411B  44 8A F0                        mov r14b, al
0064411E  84 C0                           test al, al
00644120  74 38                           je 0x14064415a
00644122  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00644126  48 8B 1F                        mov rbx, qword ptr [rdi]
00644129  EB 19                           jmp 0x140644144
0064412B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064412F  48 85 C0                        test rax, rax
00644132  74 0D                           je 0x140644141
00644134  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644138  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064413C  E8 8F 69 07 00                  call 0x1406baad0
00644141  48 8B 1B                        mov rbx, qword ptr [rbx]
00644144  48 3B DF                        cmp rbx, rdi
00644147  75 E2                           jne 0x14064412b
00644149  45 84 F6                        test r14b, r14b
0064414C  74 0C                           je 0x14064415a
0064414E  48 8D 0D 2B FD 8B 00            lea rcx, [rip + 0x8bfd2b]
00644155  E8 26 5D D0 FF                  call 0x140349e80
0064415A  4D 8B C7                        mov r8, r15
0064415D  41 8B D4                        mov edx, r12d
00644160  49 8B CD                        mov rcx, r13
00644163  E8 A8 91 06 00                  call 0x1406ad310
00644168  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0064416B  48 85 F6                        test rsi, rsi
0064416E  74 63                           je 0x1406441d3
00644170  40 32 FF                        xor dil, dil
00644173  40 38 3D 3E 07 8C 00            cmp byte ptr [rip + 0x8c073e], dil
0064417A  75 0C                           jne 0x140644188
0064417C  F7 05 FA 07 8C 00 00 08 00 00   test dword ptr [rip + 0x8c07fa], 0x800
00644186  74 13                           je 0x14064419b
00644188  48 8D 0D F1 FC 8B 00            lea rcx, [rip + 0x8bfcf1]
0064418F  E8 8C 24 BD FF                  call 0x140216620
00644194  40 8A F8                        mov dil, al
00644197  84 C0                           test al, al
00644199  74 38                           je 0x1406441d3
0064419B  48 83 C6 30                     add rsi, 0x30
0064419F  48 8B 1E                        mov rbx, qword ptr [rsi]
006441A2  EB 19                           jmp 0x1406441bd
006441A4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006441A8  48 85 C0                        test rax, rax
006441AB  74 0D                           je 0x1406441ba
006441AD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006441B1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006441B5  E8 16 69 07 00                  call 0x1406baad0
006441BA  48 8B 1B                        mov rbx, qword ptr [rbx]
006441BD  48 3B DE                        cmp rbx, rsi
006441C0  75 E2                           jne 0x1406441a4
006441C2  40 84 FF                        test dil, dil
006441C5  74 0C                           je 0x1406441d3
006441C7  48 8D 0D B2 FC 8B 00            lea rcx, [rip + 0x8bfcb2]
006441CE  E8 AD 5C D0 FF                  call 0x140349e80
006441D3  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
006441D6  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
006441DB  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
006441DF  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
006441E3  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
006441E7  49 8B E3                        mov rsp, r11
006441EA  41 5F                           pop r15
006441EC  41 5E                           pop r14
006441EE  41 5D                           pop r13
006441F0  41 5C                           pop r12
006441F2  5D                              pop rbp
006441F3  C3                              ret
006441F4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenKeyWrapper(__int64 a1, int a2, __int64 a3)
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
    result = DifGetAPIThunkContextById(result + 83, a2, a3, a4);
    if (result == 0) goto loc_0064415A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006440DE;
    v_stack_m58 = v_stack_p0;
    goto loc_006440EB;
loc_006440DE:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9177023)) != 0) goto loc_0064410F;
    if (((*(unsigned int *)(v_rip + 9177203)) & (0x800ULL)) == 0) goto loc_00644122;
loc_0064410F:
    result = ExAcquireRundownProtection(v_rip + 9174378, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064415A;
loc_00644122:
    goto loc_00644144;
loc_0064412B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00644144:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064412B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9174315;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenKey(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_006441D3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9176894)) != 0) goto loc_00644188;
    if (((*(unsigned int *)(v_rip + 9177082)) & (0x800ULL)) == 0) goto loc_0064419B;
loc_00644188:
    result = ExAcquireRundownProtection(v_rip + 9174257, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006441D3;
loc_0064419B:
    v_rsi = (result) + (48);
    goto loc_006441BD;
loc_006441A4:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_006441BD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006441A4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9174194;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenKeyWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
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
    result = DifGetAPIThunkContextById(result + 83, Arg2, Arg3, a4);
    if (result == 0) goto loc_0064415A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006440DE;
    v_stack_m58 = v_stack_p0;
    goto loc_006440EB;
loc_006440DE:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C07BF)) != 0) goto loc_0064410F;
    if (((*(uint32_t *)(v_rip + 0x8C0873)) & (0x800ULL)) == 0) goto loc_00644122;
loc_0064410F:
    result = ExAcquireRundownProtection(v_rip + 9174378, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064415A;
loc_00644122:
    goto loc_00644144;
loc_0064412B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00644144:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064412B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9174315;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwOpenKey(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_006441D3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C073E)) != 0) goto loc_00644188;
    if (((*(uint32_t *)(v_rip + 0x8C07FA)) & (0x800ULL)) == 0) goto loc_0064419B;
loc_00644188:
    result = ExAcquireRundownProtection(v_rip + 9174257, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006441D3;
loc_0064419B:
    local_rsi = (result) + (48);
    goto loc_006441BD;
loc_006441A4:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_006441BD:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006441A4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9174194;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00644080&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00644080[BB_00644080]
  bb_006440CD[BB_006440CD]
  bb_006440D4[BB_006440D4]
  bb_006440DE[BB_006440DE]
  bb_006440E2[BB_006440E2]
  bb_006440EB[BB_006440EB]
  bb_00644103[BB_00644103]
  bb_0064410F[BB_0064410F]
  bb_00644122[BB_00644122]
  bb_0064412B[BB_0064412B]
  bb_00644134[BB_00644134]
  bb_00644141[BB_00644141]
  bb_00644144[BB_00644144]
  bb_00644149[BB_00644149]
  bb_0064414E[BB_0064414E]
  bb_0064415A[BB_0064415A]
  bb_00644170[BB_00644170]
  bb_0064417C[BB_0064417C]
  bb_00644188[BB_00644188]
  bb_0064419B[BB_0064419B]
  bb_006441A4[BB_006441A4]
  bb_006441AD[BB_006441AD]
  bb_006441BA[BB_006441BA]
  bb_006441BD[BB_006441BD]
  bb_006441C2[BB_006441C2]
  bb_006441C7[BB_006441C7]
  bb_006441D3[BB_006441D3]
  bb_006441F4[BB_006441F4]
  bb_00644080 -->|branch| bb_0064415A
  bb_00644080 -->|fallthrough| bb_006440CD
  bb_006440CD -->|branch| bb_006440DE
  bb_006440CD -->|fallthrough| bb_006440D4
  bb_006440D4 -->|branch| bb_006440EB
  bb_006440DE -->|branch| bb_006440EB
  bb_006440DE -->|fallthrough| bb_006440E2
  bb_006440E2 -->|flow| bb_006440EB
  bb_006440EB -->|branch| bb_0064410F
  bb_006440EB -->|fallthrough| bb_00644103
  bb_00644103 -->|branch| bb_00644122
  bb_00644103 -->|fallthrough| bb_0064410F
  bb_0064410F -->|branch| bb_0064415A
  bb_0064410F -->|fallthrough| bb_00644122
  bb_00644122 -->|branch| bb_00644144
  bb_0064412B -->|branch| bb_00644141
  bb_0064412B -->|fallthrough| bb_00644134
  bb_00644134 -->|flow| bb_00644141
  bb_00644141 -->|flow| bb_00644144
  bb_00644144 -->|branch| bb_0064412B
  bb_00644144 -->|fallthrough| bb_00644149
  bb_00644149 -->|branch| bb_0064415A
  bb_00644149 -->|fallthrough| bb_0064414E
  bb_0064414E -->|flow| bb_0064415A
  bb_0064415A -->|branch| bb_006441D3
  bb_0064415A -->|fallthrough| bb_00644170
  bb_00644170 -->|branch| bb_00644188
  bb_00644170 -->|fallthrough| bb_0064417C
  bb_0064417C -->|branch| bb_0064419B
  bb_0064417C -->|fallthrough| bb_00644188
  bb_00644188 -->|branch| bb_006441D3
  bb_00644188 -->|fallthrough| bb_0064419B
  bb_0064419B -->|branch| bb_006441BD
  bb_006441A4 -->|branch| bb_006441BA
  bb_006441A4 -->|fallthrough| bb_006441AD
  bb_006441AD -->|flow| bb_006441BA
  bb_006441BA -->|flow| bb_006441BD
  bb_006441BD -->|branch| bb_006441A4
  bb_006441BD -->|fallthrough| bb_006441C2
  bb_006441C2 -->|branch| bb_006441D3
  bb_006441C2 -->|fallthrough| bb_006441C7
  bb_006441C7 -->|flow| bb_006441D3
```
