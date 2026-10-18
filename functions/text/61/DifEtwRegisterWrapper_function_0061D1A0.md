# DifEtwRegisterWrapper

- RVA: `0x0061D1A0`–`0x0061D325` (길이 `389` bytes)
- VA: `0x000000014061D1A0`
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
- `0x0061D1E0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061D206` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061D242` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061D268` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061D281` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061D293` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x0061D2BF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061D2E5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061D2FE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061D216` → RVA `0x00F048B8` (`.data`; read)
- `0x0061D22F` → RVA `0x00F04980` (`.data`; read)
- `0x0061D23B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0061D293` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061D1A0  48 8B C4                        mov rax, rsp
0061D1A3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0061D1A7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0061D1AB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0061D1AF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0061D1B3  55                              push rbp
0061D1B4  41 54                           push r12
0061D1B6  41 55                           push r13
0061D1B8  41 56                           push r14
0061D1BA  41 57                           push r15
0061D1BC  48 8B EC                        mov rbp, rsp
0061D1BF  48 83 EC 50                     sub rsp, 0x50
0061D1C3  0F 57 C0                        xorps xmm0, xmm0
0061D1C6  B9 AB 01 00 00                  mov ecx, 0x1ab
0061D1CB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0061D1CF  4D 8B F9                        mov r15, r9
0061D1D2  4D 8B E0                        mov r12, r8
0061D1D5  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0061D1D9  4C 8B EA                        mov r13, rdx
0061D1DC  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0061D1E0  E8 4F 88 E7 FF                  call 0x140495a34
0061D1E5  48 8B F0                        mov rsi, rax
0061D1E8  48 85 C0                        test rax, rax
0061D1EB  0F 84 95 00 00 00               je 0x14061d286
0061D1F1  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061D1F4  A8 18                           test al, 0x18
0061D1F6  74 0A                           je 0x14061d202
0061D1F8  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0061D1FC  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0061D200  EB 0D                           jmp 0x14061d20f
0061D202  A8 04                           test al, 4
0061D204  74 09                           je 0x14061d20f
0061D206  E8 FD 69 EB FF                  call 0x1404d3c08
0061D20B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0061D20F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0061D213  45 32 F6                        xor r14b, r14b
0061D216  44 38 35 9B 76 8E 00            cmp byte ptr [rip + 0x8e769b], r14b
0061D21D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0061D221  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0061D225  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0061D229  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0061D22D  75 0C                           jne 0x14061d23b
0061D22F  F7 05 47 77 8E 00 00 08 00 00   test dword ptr [rip + 0x8e7747], 0x800
0061D239  74 13                           je 0x14061d24e
0061D23B  48 8D 0D 3E 6C 8E 00            lea rcx, [rip + 0x8e6c3e]
0061D242  E8 D9 93 BF FF                  call 0x140216620
0061D247  44 8A F0                        mov r14b, al
0061D24A  84 C0                           test al, al
0061D24C  74 38                           je 0x14061d286
0061D24E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0061D252  48 8B 1F                        mov rbx, qword ptr [rdi]
0061D255  EB 19                           jmp 0x14061d270
0061D257  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061D25B  48 85 C0                        test rax, rax
0061D25E  74 0D                           je 0x14061d26d
0061D260  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061D264  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061D268  E8 63 D8 09 00                  call 0x1406baad0
0061D26D  48 8B 1B                        mov rbx, qword ptr [rbx]
0061D270  48 3B DF                        cmp rbx, rdi
0061D273  75 E2                           jne 0x14061d257
0061D275  45 84 F6                        test r14b, r14b
0061D278  74 0C                           je 0x14061d286
0061D27A  48 8D 0D FF 6B 8E 00            lea rcx, [rip + 0x8e6bff]
0061D281  E8 FA CB D2 FF                  call 0x140349e80
0061D286  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0061D28A  4D 8B CF                        mov r9, r15
0061D28D  4D 8B C4                        mov r8, r12
0061D290  49 8B D5                        mov rdx, r13
0061D293  E8 C8 36 30 00                  call 0x140920960
0061D298  89 45 F8                        mov dword ptr [rbp - 8], eax
0061D29B  48 85 F6                        test rsi, rsi
0061D29E  74 63                           je 0x14061d303
0061D2A0  40 32 FF                        xor dil, dil
0061D2A3  40 38 3D 0E 76 8E 00            cmp byte ptr [rip + 0x8e760e], dil
0061D2AA  75 0C                           jne 0x14061d2b8
0061D2AC  F7 05 CA 76 8E 00 00 08 00 00   test dword ptr [rip + 0x8e76ca], 0x800
0061D2B6  74 13                           je 0x14061d2cb
0061D2B8  48 8D 0D C1 6B 8E 00            lea rcx, [rip + 0x8e6bc1]
0061D2BF  E8 5C 93 BF FF                  call 0x140216620
0061D2C4  40 8A F8                        mov dil, al
0061D2C7  84 C0                           test al, al
0061D2C9  74 38                           je 0x14061d303
0061D2CB  48 83 C6 30                     add rsi, 0x30
0061D2CF  48 8B 1E                        mov rbx, qword ptr [rsi]
0061D2D2  EB 19                           jmp 0x14061d2ed
0061D2D4  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061D2D8  48 85 C0                        test rax, rax
0061D2DB  74 0D                           je 0x14061d2ea
0061D2DD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061D2E1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061D2E5  E8 E6 D7 09 00                  call 0x1406baad0
0061D2EA  48 8B 1B                        mov rbx, qword ptr [rbx]
0061D2ED  48 3B DE                        cmp rbx, rsi
0061D2F0  75 E2                           jne 0x14061d2d4
0061D2F2  40 84 FF                        test dil, dil
0061D2F5  74 0C                           je 0x14061d303
0061D2F7  48 8D 0D 82 6B 8E 00            lea rcx, [rip + 0x8e6b82]
0061D2FE  E8 7D CB D2 FF                  call 0x140349e80
0061D303  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0061D306  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0061D30B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0061D30F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0061D313  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0061D317  49 8B E3                        mov rsp, r11
0061D31A  41 5F                           pop r15
0061D31C  41 5E                           pop r14
0061D31E  41 5D                           pop r13
0061D320  41 5C                           pop r12
0061D322  5D                              pop rbp
0061D323  C3                              ret
0061D324  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifEtwRegisterWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    result = DifGetAPIThunkContextById(427, a2, a3, a4);
    if (result == 0) goto loc_0061D286;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061D202;
    v_stack_m58 = v_stack_p0;
    goto loc_0061D20F;
loc_0061D202:
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
    if ((*(unsigned __int8 *)(v_rip + 9336475)) != 0) goto loc_0061D23B;
    if (((*(unsigned int *)(v_rip + 9336647)) & (0x800ULL)) == 0) goto loc_0061D24E;
loc_0061D23B:
    result = ExAcquireRundownProtection(v_rip + 9333822, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061D286;
loc_0061D24E:
    goto loc_0061D270;
loc_0061D257:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061D270:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061D257;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9333759;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = EtwRegister(v_stack_p8, a2, a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0061D303;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9336334)) != 0) goto loc_0061D2B8;
    if (((*(unsigned int *)(v_rip + 9336522)) & (0x800ULL)) == 0) goto loc_0061D2CB;
loc_0061D2B8:
    result = ExAcquireRundownProtection(v_rip + 9333697, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061D303;
loc_0061D2CB:
    v_rsi = (result) + (48);
    goto loc_0061D2ED;
loc_0061D2D4:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061D2ED:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061D2D4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9333634;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifEtwRegisterWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
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
    result = DifGetAPIThunkContextById(427, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0061D286;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061D202;
    v_stack_m58 = v_stack_p0;
    goto loc_0061D20F;
loc_0061D202:
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
    if ((*(uint8_t *)(v_rip + 0x8E769B)) != 0) goto loc_0061D23B;
    if (((*(uint32_t *)(v_rip + 0x8E7747)) & (0x800ULL)) == 0) goto loc_0061D24E;
loc_0061D23B:
    result = ExAcquireRundownProtection(v_rip + 9333822, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061D286;
loc_0061D24E:
    goto loc_0061D270;
loc_0061D257:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0061D270:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061D257;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9333759;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = EtwRegister(v_stack_p8, Arg2, Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0061D303;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E760E)) != 0) goto loc_0061D2B8;
    if (((*(uint32_t *)(v_rip + 0x8E76CA)) & (0x800ULL)) == 0) goto loc_0061D2CB;
loc_0061D2B8:
    result = ExAcquireRundownProtection(v_rip + 9333697, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061D303;
loc_0061D2CB:
    local_rsi = (result) + (48);
    goto loc_0061D2ED;
loc_0061D2D4:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0061D2ED:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061D2D4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9333634;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061D1A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061D1A0[BB_0061D1A0]
  bb_0061D1F1[BB_0061D1F1]
  bb_0061D1F8[BB_0061D1F8]
  bb_0061D202[BB_0061D202]
  bb_0061D206[BB_0061D206]
  bb_0061D20F[BB_0061D20F]
  bb_0061D22F[BB_0061D22F]
  bb_0061D23B[BB_0061D23B]
  bb_0061D24E[BB_0061D24E]
  bb_0061D257[BB_0061D257]
  bb_0061D260[BB_0061D260]
  bb_0061D26D[BB_0061D26D]
  bb_0061D270[BB_0061D270]
  bb_0061D275[BB_0061D275]
  bb_0061D27A[BB_0061D27A]
  bb_0061D286[BB_0061D286]
  bb_0061D2A0[BB_0061D2A0]
  bb_0061D2AC[BB_0061D2AC]
  bb_0061D2B8[BB_0061D2B8]
  bb_0061D2CB[BB_0061D2CB]
  bb_0061D2D4[BB_0061D2D4]
  bb_0061D2DD[BB_0061D2DD]
  bb_0061D2EA[BB_0061D2EA]
  bb_0061D2ED[BB_0061D2ED]
  bb_0061D2F2[BB_0061D2F2]
  bb_0061D2F7[BB_0061D2F7]
  bb_0061D303[BB_0061D303]
  bb_0061D324[BB_0061D324]
  bb_0061D1A0 -->|branch| bb_0061D286
  bb_0061D1A0 -->|fallthrough| bb_0061D1F1
  bb_0061D1F1 -->|branch| bb_0061D202
  bb_0061D1F1 -->|fallthrough| bb_0061D1F8
  bb_0061D1F8 -->|branch| bb_0061D20F
  bb_0061D202 -->|branch| bb_0061D20F
  bb_0061D202 -->|fallthrough| bb_0061D206
  bb_0061D206 -->|flow| bb_0061D20F
  bb_0061D20F -->|branch| bb_0061D23B
  bb_0061D20F -->|fallthrough| bb_0061D22F
  bb_0061D22F -->|branch| bb_0061D24E
  bb_0061D22F -->|fallthrough| bb_0061D23B
  bb_0061D23B -->|branch| bb_0061D286
  bb_0061D23B -->|fallthrough| bb_0061D24E
  bb_0061D24E -->|branch| bb_0061D270
  bb_0061D257 -->|branch| bb_0061D26D
  bb_0061D257 -->|fallthrough| bb_0061D260
  bb_0061D260 -->|flow| bb_0061D26D
  bb_0061D26D -->|flow| bb_0061D270
  bb_0061D270 -->|branch| bb_0061D257
  bb_0061D270 -->|fallthrough| bb_0061D275
  bb_0061D275 -->|branch| bb_0061D286
  bb_0061D275 -->|fallthrough| bb_0061D27A
  bb_0061D27A -->|flow| bb_0061D286
  bb_0061D286 -->|branch| bb_0061D303
  bb_0061D286 -->|fallthrough| bb_0061D2A0
  bb_0061D2A0 -->|branch| bb_0061D2B8
  bb_0061D2A0 -->|fallthrough| bb_0061D2AC
  bb_0061D2AC -->|branch| bb_0061D2CB
  bb_0061D2AC -->|fallthrough| bb_0061D2B8
  bb_0061D2B8 -->|branch| bb_0061D303
  bb_0061D2B8 -->|fallthrough| bb_0061D2CB
  bb_0061D2CB -->|branch| bb_0061D2ED
  bb_0061D2D4 -->|branch| bb_0061D2EA
  bb_0061D2D4 -->|fallthrough| bb_0061D2DD
  bb_0061D2DD -->|flow| bb_0061D2EA
  bb_0061D2EA -->|flow| bb_0061D2ED
  bb_0061D2ED -->|branch| bb_0061D2D4
  bb_0061D2ED -->|fallthrough| bb_0061D2F2
  bb_0061D2F2 -->|branch| bb_0061D303
  bb_0061D2F2 -->|fallthrough| bb_0061D2F7
  bb_0061D2F7 -->|flow| bb_0061D303
```
