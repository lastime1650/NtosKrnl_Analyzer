# DifZwFlushVirtualMemoryWrapper

- RVA: `0x00642360`–`0x006424E5` (길이 `389` bytes)
- VA: `0x0000000140642360`
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
- `0x006423A0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006423C6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00642402` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00642428` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00642441` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00642453` → [ZwFlushVirtualMemory](../6A/ZwFlushVirtualMemory_function_006AEF50.md) (function, `0x006AEF50`)
- `0x0064247F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006424A5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006424BE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006423D6` → RVA `0x00F048B8` (`.data`; read)
- `0x006423EF` → RVA `0x00F04980` (`.data`; read)
- `0x006423FB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00642360  48 8B C4                        mov rax, rsp
00642363  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00642367  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064236B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064236F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00642373  55                              push rbp
00642374  41 54                           push r12
00642376  41 55                           push r13
00642378  41 56                           push r14
0064237A  41 57                           push r15
0064237C  48 8B EC                        mov rbp, rsp
0064237F  48 83 EC 50                     sub rsp, 0x50
00642383  0F 57 C0                        xorps xmm0, xmm0
00642386  B9 62 00 00 00                  mov ecx, 0x62
0064238B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064238F  4D 8B F9                        mov r15, r9
00642392  4D 8B E0                        mov r12, r8
00642395  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00642399  4C 8B EA                        mov r13, rdx
0064239C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
006423A0  E8 8F 36 E5 FF                  call 0x140495a34
006423A5  48 8B F0                        mov rsi, rax
006423A8  48 85 C0                        test rax, rax
006423AB  0F 84 95 00 00 00               je 0x140642446
006423B1  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006423B4  A8 18                           test al, 0x18
006423B6  74 0A                           je 0x1406423c2
006423B8  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006423BC  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
006423C0  EB 0D                           jmp 0x1406423cf
006423C2  A8 04                           test al, 4
006423C4  74 09                           je 0x1406423cf
006423C6  E8 3D 18 E9 FF                  call 0x1404d3c08
006423CB  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006423CF  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
006423D3  45 32 F6                        xor r14b, r14b
006423D6  44 38 35 DB 24 8C 00            cmp byte ptr [rip + 0x8c24db], r14b
006423DD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006423E1  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
006423E5  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
006423E9  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
006423ED  75 0C                           jne 0x1406423fb
006423EF  F7 05 87 25 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2587], 0x800
006423F9  74 13                           je 0x14064240e
006423FB  48 8D 0D 7E 1A 8C 00            lea rcx, [rip + 0x8c1a7e]
00642402  E8 19 42 BD FF                  call 0x140216620
00642407  44 8A F0                        mov r14b, al
0064240A  84 C0                           test al, al
0064240C  74 38                           je 0x140642446
0064240E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00642412  48 8B 1F                        mov rbx, qword ptr [rdi]
00642415  EB 19                           jmp 0x140642430
00642417  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064241B  48 85 C0                        test rax, rax
0064241E  74 0D                           je 0x14064242d
00642420  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00642424  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00642428  E8 A3 86 07 00                  call 0x1406baad0
0064242D  48 8B 1B                        mov rbx, qword ptr [rbx]
00642430  48 3B DF                        cmp rbx, rdi
00642433  75 E2                           jne 0x140642417
00642435  45 84 F6                        test r14b, r14b
00642438  74 0C                           je 0x140642446
0064243A  48 8D 0D 3F 1A 8C 00            lea rcx, [rip + 0x8c1a3f]
00642441  E8 3A 7A D0 FF                  call 0x140349e80
00642446  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064244A  4D 8B CF                        mov r9, r15
0064244D  4D 8B C4                        mov r8, r12
00642450  49 8B D5                        mov rdx, r13
00642453  E8 F8 CA 06 00                  call 0x1406aef50
00642458  89 45 F8                        mov dword ptr [rbp - 8], eax
0064245B  48 85 F6                        test rsi, rsi
0064245E  74 63                           je 0x1406424c3
00642460  40 32 FF                        xor dil, dil
00642463  40 38 3D 4E 24 8C 00            cmp byte ptr [rip + 0x8c244e], dil
0064246A  75 0C                           jne 0x140642478
0064246C  F7 05 0A 25 8C 00 00 08 00 00   test dword ptr [rip + 0x8c250a], 0x800
00642476  74 13                           je 0x14064248b
00642478  48 8D 0D 01 1A 8C 00            lea rcx, [rip + 0x8c1a01]
0064247F  E8 9C 41 BD FF                  call 0x140216620
00642484  40 8A F8                        mov dil, al
00642487  84 C0                           test al, al
00642489  74 38                           je 0x1406424c3
0064248B  48 83 C6 30                     add rsi, 0x30
0064248F  48 8B 1E                        mov rbx, qword ptr [rsi]
00642492  EB 19                           jmp 0x1406424ad
00642494  48 8D 43 F0                     lea rax, [rbx - 0x10]
00642498  48 85 C0                        test rax, rax
0064249B  74 0D                           je 0x1406424aa
0064249D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006424A1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006424A5  E8 26 86 07 00                  call 0x1406baad0
006424AA  48 8B 1B                        mov rbx, qword ptr [rbx]
006424AD  48 3B DE                        cmp rbx, rsi
006424B0  75 E2                           jne 0x140642494
006424B2  40 84 FF                        test dil, dil
006424B5  74 0C                           je 0x1406424c3
006424B7  48 8D 0D C2 19 8C 00            lea rcx, [rip + 0x8c19c2]
006424BE  E8 BD 79 D0 FF                  call 0x140349e80
006424C3  8B 45 F8                        mov eax, dword ptr [rbp - 8]
006424C6  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
006424CB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
006424CF  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
006424D3  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
006424D7  49 8B E3                        mov rsp, r11
006424DA  41 5F                           pop r15
006424DC  41 5E                           pop r14
006424DE  41 5D                           pop r13
006424E0  41 5C                           pop r12
006424E2  5D                              pop rbp
006424E3  C3                              ret
006424E4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwFlushVirtualMemoryWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
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
    result = DifGetAPIThunkContextById(98, a2, a3, a4);
    if (result == 0) goto loc_00642446;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006423C2;
    v_stack_m58 = v_stack_p0;
    goto loc_006423CF;
loc_006423C2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = a2;
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9184475)) != 0) goto loc_006423FB;
    if (((*(unsigned int *)(v_rip + 9184647)) & (0x800ULL)) == 0) goto loc_0064240E;
loc_006423FB:
    result = ExAcquireRundownProtection(v_rip + 9181822, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00642446;
loc_0064240E:
    goto loc_00642430;
loc_00642417:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00642430:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00642417;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9181759;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwFlushVirtualMemory(v_stack_p8, a2, a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_006424C3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9184334)) != 0) goto loc_00642478;
    if (((*(unsigned int *)(v_rip + 9184522)) & (0x800ULL)) == 0) goto loc_0064248B;
loc_00642478:
    result = ExAcquireRundownProtection(v_rip + 9181697, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006424C3;
loc_0064248B:
    v_rsi = (result) + (48);
    goto loc_006424AD;
loc_00642494:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006424AD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00642494;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9181634;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwFlushVirtualMemoryWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
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
    result = DifGetAPIThunkContextById(98, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00642446;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006423C2;
    v_stack_m58 = v_stack_p0;
    goto loc_006423CF;
loc_006423C2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = Arg2;
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C24DB)) != 0) goto loc_006423FB;
    if (((*(uint32_t *)(v_rip + 0x8C2587)) & (0x800ULL)) == 0) goto loc_0064240E;
loc_006423FB:
    result = ExAcquireRundownProtection(v_rip + 9181822, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00642446;
loc_0064240E:
    goto loc_00642430;
loc_00642417:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00642430:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00642417;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9181759;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwFlushVirtualMemory(v_stack_p8, Arg2, Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_006424C3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C244E)) != 0) goto loc_00642478;
    if (((*(uint32_t *)(v_rip + 0x8C250A)) & (0x800ULL)) == 0) goto loc_0064248B;
loc_00642478:
    result = ExAcquireRundownProtection(v_rip + 9181697, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006424C3;
loc_0064248B:
    local_rsi = (result) + (48);
    goto loc_006424AD;
loc_00642494:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006424AD:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00642494;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9181634;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00642360&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00642360[BB_00642360]
  bb_006423B1[BB_006423B1]
  bb_006423B8[BB_006423B8]
  bb_006423C2[BB_006423C2]
  bb_006423C6[BB_006423C6]
  bb_006423CF[BB_006423CF]
  bb_006423EF[BB_006423EF]
  bb_006423FB[BB_006423FB]
  bb_0064240E[BB_0064240E]
  bb_00642417[BB_00642417]
  bb_00642420[BB_00642420]
  bb_0064242D[BB_0064242D]
  bb_00642430[BB_00642430]
  bb_00642435[BB_00642435]
  bb_0064243A[BB_0064243A]
  bb_00642446[BB_00642446]
  bb_00642460[BB_00642460]
  bb_0064246C[BB_0064246C]
  bb_00642478[BB_00642478]
  bb_0064248B[BB_0064248B]
  bb_00642494[BB_00642494]
  bb_0064249D[BB_0064249D]
  bb_006424AA[BB_006424AA]
  bb_006424AD[BB_006424AD]
  bb_006424B2[BB_006424B2]
  bb_006424B7[BB_006424B7]
  bb_006424C3[BB_006424C3]
  bb_006424E4[BB_006424E4]
  bb_00642360 -->|branch| bb_00642446
  bb_00642360 -->|fallthrough| bb_006423B1
  bb_006423B1 -->|branch| bb_006423C2
  bb_006423B1 -->|fallthrough| bb_006423B8
  bb_006423B8 -->|branch| bb_006423CF
  bb_006423C2 -->|branch| bb_006423CF
  bb_006423C2 -->|fallthrough| bb_006423C6
  bb_006423C6 -->|flow| bb_006423CF
  bb_006423CF -->|branch| bb_006423FB
  bb_006423CF -->|fallthrough| bb_006423EF
  bb_006423EF -->|branch| bb_0064240E
  bb_006423EF -->|fallthrough| bb_006423FB
  bb_006423FB -->|branch| bb_00642446
  bb_006423FB -->|fallthrough| bb_0064240E
  bb_0064240E -->|branch| bb_00642430
  bb_00642417 -->|branch| bb_0064242D
  bb_00642417 -->|fallthrough| bb_00642420
  bb_00642420 -->|flow| bb_0064242D
  bb_0064242D -->|flow| bb_00642430
  bb_00642430 -->|branch| bb_00642417
  bb_00642430 -->|fallthrough| bb_00642435
  bb_00642435 -->|branch| bb_00642446
  bb_00642435 -->|fallthrough| bb_0064243A
  bb_0064243A -->|flow| bb_00642446
  bb_00642446 -->|branch| bb_006424C3
  bb_00642446 -->|fallthrough| bb_00642460
  bb_00642460 -->|branch| bb_00642478
  bb_00642460 -->|fallthrough| bb_0064246C
  bb_0064246C -->|branch| bb_0064248B
  bb_0064246C -->|fallthrough| bb_00642478
  bb_00642478 -->|branch| bb_006424C3
  bb_00642478 -->|fallthrough| bb_0064248B
  bb_0064248B -->|branch| bb_006424AD
  bb_00642494 -->|branch| bb_006424AA
  bb_00642494 -->|fallthrough| bb_0064249D
  bb_0064249D -->|flow| bb_006424AA
  bb_006424AA -->|flow| bb_006424AD
  bb_006424AD -->|branch| bb_00642494
  bb_006424AD -->|fallthrough| bb_006424B2
  bb_006424B2 -->|branch| bb_006424C3
  bb_006424B2 -->|fallthrough| bb_006424B7
  bb_006424B7 -->|flow| bb_006424C3
```
