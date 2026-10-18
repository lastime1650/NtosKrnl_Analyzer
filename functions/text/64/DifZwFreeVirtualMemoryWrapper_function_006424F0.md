# DifZwFreeVirtualMemoryWrapper

- RVA: `0x006424F0`–`0x00642675` (길이 `389` bytes)
- VA: `0x00000001406424F0`
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
- `0x00642530` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00642556` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00642592` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006425B8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006425D1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006425E3` → [ZwFreeVirtualMemory](../6A/ZwFreeVirtualMemory_function_006AD490.md) (function, `0x006AD490`)
- `0x0064260F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00642635` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064264E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00642566` → RVA `0x00F048B8` (`.data`; read)
- `0x0064257F` → RVA `0x00F04980` (`.data`; read)
- `0x0064258B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006424F0  48 8B C4                        mov rax, rsp
006424F3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006424F7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006424FB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006424FF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00642503  55                              push rbp
00642504  41 54                           push r12
00642506  41 55                           push r13
00642508  41 56                           push r14
0064250A  41 57                           push r15
0064250C  48 8B EC                        mov rbp, rsp
0064250F  48 83 EC 50                     sub rsp, 0x50
00642513  0F 57 C0                        xorps xmm0, xmm0
00642516  B9 61 00 00 00                  mov ecx, 0x61
0064251B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064251F  45 8B F9                        mov r15d, r9d
00642522  4D 8B E0                        mov r12, r8
00642525  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00642529  4C 8B EA                        mov r13, rdx
0064252C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00642530  E8 FF 34 E5 FF                  call 0x140495a34
00642535  48 8B F0                        mov rsi, rax
00642538  48 85 C0                        test rax, rax
0064253B  0F 84 95 00 00 00               je 0x1406425d6
00642541  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00642544  A8 18                           test al, 0x18
00642546  74 0A                           je 0x140642552
00642548  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064254C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00642550  EB 0D                           jmp 0x14064255f
00642552  A8 04                           test al, 4
00642554  74 09                           je 0x14064255f
00642556  E8 AD 16 E9 FF                  call 0x1404d3c08
0064255B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064255F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00642563  45 32 F6                        xor r14b, r14b
00642566  44 38 35 4B 23 8C 00            cmp byte ptr [rip + 0x8c234b], r14b
0064256D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00642571  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00642575  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00642579  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0064257D  75 0C                           jne 0x14064258b
0064257F  F7 05 F7 23 8C 00 00 08 00 00   test dword ptr [rip + 0x8c23f7], 0x800
00642589  74 13                           je 0x14064259e
0064258B  48 8D 0D EE 18 8C 00            lea rcx, [rip + 0x8c18ee]
00642592  E8 89 40 BD FF                  call 0x140216620
00642597  44 8A F0                        mov r14b, al
0064259A  84 C0                           test al, al
0064259C  74 38                           je 0x1406425d6
0064259E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006425A2  48 8B 1F                        mov rbx, qword ptr [rdi]
006425A5  EB 19                           jmp 0x1406425c0
006425A7  48 8D 43 F0                     lea rax, [rbx - 0x10]
006425AB  48 85 C0                        test rax, rax
006425AE  74 0D                           je 0x1406425bd
006425B0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006425B4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006425B8  E8 13 85 07 00                  call 0x1406baad0
006425BD  48 8B 1B                        mov rbx, qword ptr [rbx]
006425C0  48 3B DF                        cmp rbx, rdi
006425C3  75 E2                           jne 0x1406425a7
006425C5  45 84 F6                        test r14b, r14b
006425C8  74 0C                           je 0x1406425d6
006425CA  48 8D 0D AF 18 8C 00            lea rcx, [rip + 0x8c18af]
006425D1  E8 AA 78 D0 FF                  call 0x140349e80
006425D6  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006425DA  45 8B CF                        mov r9d, r15d
006425DD  4D 8B C4                        mov r8, r12
006425E0  49 8B D5                        mov rdx, r13
006425E3  E8 A8 AE 06 00                  call 0x1406ad490
006425E8  89 45 F8                        mov dword ptr [rbp - 8], eax
006425EB  48 85 F6                        test rsi, rsi
006425EE  74 63                           je 0x140642653
006425F0  40 32 FF                        xor dil, dil
006425F3  40 38 3D BE 22 8C 00            cmp byte ptr [rip + 0x8c22be], dil
006425FA  75 0C                           jne 0x140642608
006425FC  F7 05 7A 23 8C 00 00 08 00 00   test dword ptr [rip + 0x8c237a], 0x800
00642606  74 13                           je 0x14064261b
00642608  48 8D 0D 71 18 8C 00            lea rcx, [rip + 0x8c1871]
0064260F  E8 0C 40 BD FF                  call 0x140216620
00642614  40 8A F8                        mov dil, al
00642617  84 C0                           test al, al
00642619  74 38                           je 0x140642653
0064261B  48 83 C6 30                     add rsi, 0x30
0064261F  48 8B 1E                        mov rbx, qword ptr [rsi]
00642622  EB 19                           jmp 0x14064263d
00642624  48 8D 43 F0                     lea rax, [rbx - 0x10]
00642628  48 85 C0                        test rax, rax
0064262B  74 0D                           je 0x14064263a
0064262D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00642631  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00642635  E8 96 84 07 00                  call 0x1406baad0
0064263A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064263D  48 3B DE                        cmp rbx, rsi
00642640  75 E2                           jne 0x140642624
00642642  40 84 FF                        test dil, dil
00642645  74 0C                           je 0x140642653
00642647  48 8D 0D 32 18 8C 00            lea rcx, [rip + 0x8c1832]
0064264E  E8 2D 78 D0 FF                  call 0x140349e80
00642653  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00642656  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064265B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064265F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00642663  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00642667  49 8B E3                        mov rsp, r11
0064266A  41 5F                           pop r15
0064266C  41 5E                           pop r14
0064266E  41 5D                           pop r13
00642670  41 5C                           pop r12
00642672  5D                              pop rbp
00642673  C3                              ret
00642674  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwFreeVirtualMemoryWrapper(__int64 a1, __int64 a2, __int64 a3, int a4)
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
    unsigned int v_stack_m50;
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
    result = DifGetAPIThunkContextById(97, a2, a3, a4);
    if (result == 0) goto loc_006425D6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00642552;
    v_stack_m58 = v_stack_p0;
    goto loc_0064255F;
loc_00642552:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = a2;
    v_stack_m48 = a3;
    v_stack_m50 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9184075)) != 0) goto loc_0064258B;
    if (((*(unsigned int *)(v_rip + 9184247)) & (0x800ULL)) == 0) goto loc_0064259E;
loc_0064258B:
    result = ExAcquireRundownProtection(v_rip + 9181422, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006425D6;
loc_0064259E:
    goto loc_006425C0;
loc_006425A7:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006425C0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006425A7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9181359;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwFreeVirtualMemory(v_stack_p8, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00642653;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9183934)) != 0) goto loc_00642608;
    if (((*(unsigned int *)(v_rip + 9184122)) & (0x800ULL)) == 0) goto loc_0064261B;
loc_00642608:
    result = ExAcquireRundownProtection(v_rip + 9181297, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00642653;
loc_0064261B:
    v_rsi = (result) + (48);
    goto loc_0064263D;
loc_00642624:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0064263D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00642624;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9181234;
        result = ExReleaseRundownProtection(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwFreeVirtualMemoryWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
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
    uint32_t v_stack_m50;
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
    result = DifGetAPIThunkContextById(97, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006425D6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00642552;
    v_stack_m58 = v_stack_p0;
    goto loc_0064255F;
loc_00642552:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = Arg2;
    v_stack_m48 = Arg3;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8C234B)) != 0) goto loc_0064258B;
    if (((*(uint32_t *)(v_rip + 0x8C23F7)) & (0x800ULL)) == 0) goto loc_0064259E;
loc_0064258B:
    result = ExAcquireRundownProtection(v_rip + 9181422, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006425D6;
loc_0064259E:
    goto loc_006425C0;
loc_006425A7:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006425C0:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006425A7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9181359;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwFreeVirtualMemory(v_stack_p8, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00642653;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C22BE)) != 0) goto loc_00642608;
    if (((*(uint32_t *)(v_rip + 0x8C237A)) & (0x800ULL)) == 0) goto loc_0064261B;
loc_00642608:
    result = ExAcquireRundownProtection(v_rip + 9181297, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00642653;
loc_0064261B:
    local_rsi = (result) + (48);
    goto loc_0064263D;
loc_00642624:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0064263D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00642624;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9181234;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006424F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006424F0[BB_006424F0]
  bb_00642541[BB_00642541]
  bb_00642548[BB_00642548]
  bb_00642552[BB_00642552]
  bb_00642556[BB_00642556]
  bb_0064255F[BB_0064255F]
  bb_0064257F[BB_0064257F]
  bb_0064258B[BB_0064258B]
  bb_0064259E[BB_0064259E]
  bb_006425A7[BB_006425A7]
  bb_006425B0[BB_006425B0]
  bb_006425BD[BB_006425BD]
  bb_006425C0[BB_006425C0]
  bb_006425C5[BB_006425C5]
  bb_006425CA[BB_006425CA]
  bb_006425D6[BB_006425D6]
  bb_006425F0[BB_006425F0]
  bb_006425FC[BB_006425FC]
  bb_00642608[BB_00642608]
  bb_0064261B[BB_0064261B]
  bb_00642624[BB_00642624]
  bb_0064262D[BB_0064262D]
  bb_0064263A[BB_0064263A]
  bb_0064263D[BB_0064263D]
  bb_00642642[BB_00642642]
  bb_00642647[BB_00642647]
  bb_00642653[BB_00642653]
  bb_00642674[BB_00642674]
  bb_006424F0 -->|branch| bb_006425D6
  bb_006424F0 -->|fallthrough| bb_00642541
  bb_00642541 -->|branch| bb_00642552
  bb_00642541 -->|fallthrough| bb_00642548
  bb_00642548 -->|branch| bb_0064255F
  bb_00642552 -->|branch| bb_0064255F
  bb_00642552 -->|fallthrough| bb_00642556
  bb_00642556 -->|flow| bb_0064255F
  bb_0064255F -->|branch| bb_0064258B
  bb_0064255F -->|fallthrough| bb_0064257F
  bb_0064257F -->|branch| bb_0064259E
  bb_0064257F -->|fallthrough| bb_0064258B
  bb_0064258B -->|branch| bb_006425D6
  bb_0064258B -->|fallthrough| bb_0064259E
  bb_0064259E -->|branch| bb_006425C0
  bb_006425A7 -->|branch| bb_006425BD
  bb_006425A7 -->|fallthrough| bb_006425B0
  bb_006425B0 -->|flow| bb_006425BD
  bb_006425BD -->|flow| bb_006425C0
  bb_006425C0 -->|branch| bb_006425A7
  bb_006425C0 -->|fallthrough| bb_006425C5
  bb_006425C5 -->|branch| bb_006425D6
  bb_006425C5 -->|fallthrough| bb_006425CA
  bb_006425CA -->|flow| bb_006425D6
  bb_006425D6 -->|branch| bb_00642653
  bb_006425D6 -->|fallthrough| bb_006425F0
  bb_006425F0 -->|branch| bb_00642608
  bb_006425F0 -->|fallthrough| bb_006425FC
  bb_006425FC -->|branch| bb_0064261B
  bb_006425FC -->|fallthrough| bb_00642608
  bb_00642608 -->|branch| bb_00642653
  bb_00642608 -->|fallthrough| bb_0064261B
  bb_0064261B -->|branch| bb_0064263D
  bb_00642624 -->|branch| bb_0064263A
  bb_00642624 -->|fallthrough| bb_0064262D
  bb_0064262D -->|flow| bb_0064263A
  bb_0064263A -->|flow| bb_0064263D
  bb_0064263D -->|branch| bb_00642624
  bb_0064263D -->|fallthrough| bb_00642642
  bb_00642642 -->|branch| bb_00642653
  bb_00642642 -->|fallthrough| bb_00642647
  bb_00642647 -->|flow| bb_00642653
```
