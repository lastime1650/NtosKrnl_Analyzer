# DifIoRegisterDeviceInterfaceWrapper

- RVA: `0x0062C210`–`0x0062C395` (길이 `389` bytes)
- VA: `0x000000014062C210`
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
- `0x0062C250` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062C276` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062C2B2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062C2D8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062C2F1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062C303` → [IoRegisterDeviceInterface](../../page/94/IoRegisterDeviceInterface_function_0094F9A0.md) (function, `0x0094F9A0`)
- `0x0062C32F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062C355` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062C36E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062C286` → RVA `0x00F048B8` (`.data`; read)
- `0x0062C29F` → RVA `0x00F04980` (`.data`; read)
- `0x0062C2AB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062C303` → [IoRegisterDeviceInterface](../../page/94/IoRegisterDeviceInterface_function_0094F9A0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062C210  48 8B C4                        mov rax, rsp
0062C213  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0062C217  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062C21B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062C21F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0062C223  55                              push rbp
0062C224  41 54                           push r12
0062C226  41 55                           push r13
0062C228  41 56                           push r14
0062C22A  41 57                           push r15
0062C22C  48 8B EC                        mov rbp, rsp
0062C22F  48 83 EC 50                     sub rsp, 0x50
0062C233  0F 57 C0                        xorps xmm0, xmm0
0062C236  B9 40 01 00 00                  mov ecx, 0x140
0062C23B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062C23F  4D 8B F9                        mov r15, r9
0062C242  4D 8B E0                        mov r12, r8
0062C245  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0062C249  4C 8B EA                        mov r13, rdx
0062C24C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0062C250  E8 DF 97 E6 FF                  call 0x140495a34
0062C255  48 8B F0                        mov rsi, rax
0062C258  48 85 C0                        test rax, rax
0062C25B  0F 84 95 00 00 00               je 0x14062c2f6
0062C261  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062C264  A8 18                           test al, 0x18
0062C266  74 0A                           je 0x14062c272
0062C268  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062C26C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0062C270  EB 0D                           jmp 0x14062c27f
0062C272  A8 04                           test al, 4
0062C274  74 09                           je 0x14062c27f
0062C276  E8 8D 79 EA FF                  call 0x1404d3c08
0062C27B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062C27F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0062C283  45 32 F6                        xor r14b, r14b
0062C286  44 38 35 2B 86 8D 00            cmp byte ptr [rip + 0x8d862b], r14b
0062C28D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0062C291  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0062C295  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0062C299  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0062C29D  75 0C                           jne 0x14062c2ab
0062C29F  F7 05 D7 86 8D 00 00 08 00 00   test dword ptr [rip + 0x8d86d7], 0x800
0062C2A9  74 13                           je 0x14062c2be
0062C2AB  48 8D 0D CE 7B 8D 00            lea rcx, [rip + 0x8d7bce]
0062C2B2  E8 69 A3 BE FF                  call 0x140216620
0062C2B7  44 8A F0                        mov r14b, al
0062C2BA  84 C0                           test al, al
0062C2BC  74 38                           je 0x14062c2f6
0062C2BE  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062C2C2  48 8B 1F                        mov rbx, qword ptr [rdi]
0062C2C5  EB 19                           jmp 0x14062c2e0
0062C2C7  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062C2CB  48 85 C0                        test rax, rax
0062C2CE  74 0D                           je 0x14062c2dd
0062C2D0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062C2D4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062C2D8  E8 F3 E7 08 00                  call 0x1406baad0
0062C2DD  48 8B 1B                        mov rbx, qword ptr [rbx]
0062C2E0  48 3B DF                        cmp rbx, rdi
0062C2E3  75 E2                           jne 0x14062c2c7
0062C2E5  45 84 F6                        test r14b, r14b
0062C2E8  74 0C                           je 0x14062c2f6
0062C2EA  48 8D 0D 8F 7B 8D 00            lea rcx, [rip + 0x8d7b8f]
0062C2F1  E8 8A DB D1 FF                  call 0x140349e80
0062C2F6  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0062C2FA  4D 8B CF                        mov r9, r15
0062C2FD  4D 8B C4                        mov r8, r12
0062C300  49 8B D5                        mov rdx, r13
0062C303  E8 98 36 32 00                  call 0x14094f9a0
0062C308  89 45 F8                        mov dword ptr [rbp - 8], eax
0062C30B  48 85 F6                        test rsi, rsi
0062C30E  74 63                           je 0x14062c373
0062C310  40 32 FF                        xor dil, dil
0062C313  40 38 3D 9E 85 8D 00            cmp byte ptr [rip + 0x8d859e], dil
0062C31A  75 0C                           jne 0x14062c328
0062C31C  F7 05 5A 86 8D 00 00 08 00 00   test dword ptr [rip + 0x8d865a], 0x800
0062C326  74 13                           je 0x14062c33b
0062C328  48 8D 0D 51 7B 8D 00            lea rcx, [rip + 0x8d7b51]
0062C32F  E8 EC A2 BE FF                  call 0x140216620
0062C334  40 8A F8                        mov dil, al
0062C337  84 C0                           test al, al
0062C339  74 38                           je 0x14062c373
0062C33B  48 83 C6 30                     add rsi, 0x30
0062C33F  48 8B 1E                        mov rbx, qword ptr [rsi]
0062C342  EB 19                           jmp 0x14062c35d
0062C344  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062C348  48 85 C0                        test rax, rax
0062C34B  74 0D                           je 0x14062c35a
0062C34D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062C351  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062C355  E8 76 E7 08 00                  call 0x1406baad0
0062C35A  48 8B 1B                        mov rbx, qword ptr [rbx]
0062C35D  48 3B DE                        cmp rbx, rsi
0062C360  75 E2                           jne 0x14062c344
0062C362  40 84 FF                        test dil, dil
0062C365  74 0C                           je 0x14062c373
0062C367  48 8D 0D 12 7B 8D 00            lea rcx, [rip + 0x8d7b12]
0062C36E  E8 0D DB D1 FF                  call 0x140349e80
0062C373  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0062C376  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0062C37B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0062C37F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0062C383  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0062C387  49 8B E3                        mov rsp, r11
0062C38A  41 5F                           pop r15
0062C38C  41 5E                           pop r14
0062C38E  41 5D                           pop r13
0062C390  41 5C                           pop r12
0062C392  5D                              pop rbp
0062C393  C3                              ret
0062C394  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoRegisterDeviceInterfaceWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    result = DifGetAPIThunkContextById(320, a2, a3, a4);
    if (result == 0) goto loc_0062C2F6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062C272;
    v_stack_m58 = v_stack_p0;
    goto loc_0062C27F;
loc_0062C272:
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
    if ((*(unsigned __int8 *)(v_rip + 9274923)) != 0) goto loc_0062C2AB;
    if (((*(unsigned int *)(v_rip + 9275095)) & (0x800ULL)) == 0) goto loc_0062C2BE;
loc_0062C2AB:
    result = ExAcquireRundownProtection(v_rip + 9272270, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062C2F6;
loc_0062C2BE:
    goto loc_0062C2E0;
loc_0062C2C7:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062C2E0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062C2C7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9272207;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoRegisterDeviceInterface(v_stack_p8, a2, a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0062C373;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9274782)) != 0) goto loc_0062C328;
    if (((*(unsigned int *)(v_rip + 9274970)) & (0x800ULL)) == 0) goto loc_0062C33B;
loc_0062C328:
    result = ExAcquireRundownProtection(v_rip + 9272145, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062C373;
loc_0062C33B:
    v_rsi = (result) + (48);
    goto loc_0062C35D;
loc_0062C344:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062C35D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062C344;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9272082;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoRegisterDeviceInterfaceWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
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
    result = DifGetAPIThunkContextById(320, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062C2F6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062C272;
    v_stack_m58 = v_stack_p0;
    goto loc_0062C27F;
loc_0062C272:
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
    if ((*(uint8_t *)(v_rip + 0x8D862B)) != 0) goto loc_0062C2AB;
    if (((*(uint32_t *)(v_rip + 0x8D86D7)) & (0x800ULL)) == 0) goto loc_0062C2BE;
loc_0062C2AB:
    result = ExAcquireRundownProtection(v_rip + 9272270, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062C2F6;
loc_0062C2BE:
    goto loc_0062C2E0;
loc_0062C2C7:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062C2E0:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062C2C7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9272207;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = IoRegisterDeviceInterface(v_stack_p8, Arg2, Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0062C373;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D859E)) != 0) goto loc_0062C328;
    if (((*(uint32_t *)(v_rip + 0x8D865A)) & (0x800ULL)) == 0) goto loc_0062C33B;
loc_0062C328:
    result = ExAcquireRundownProtection(v_rip + 9272145, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062C373;
loc_0062C33B:
    local_rsi = (result) + (48);
    goto loc_0062C35D;
loc_0062C344:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062C35D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062C344;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9272082;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062C210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062C210[BB_0062C210]
  bb_0062C261[BB_0062C261]
  bb_0062C268[BB_0062C268]
  bb_0062C272[BB_0062C272]
  bb_0062C276[BB_0062C276]
  bb_0062C27F[BB_0062C27F]
  bb_0062C29F[BB_0062C29F]
  bb_0062C2AB[BB_0062C2AB]
  bb_0062C2BE[BB_0062C2BE]
  bb_0062C2C7[BB_0062C2C7]
  bb_0062C2D0[BB_0062C2D0]
  bb_0062C2DD[BB_0062C2DD]
  bb_0062C2E0[BB_0062C2E0]
  bb_0062C2E5[BB_0062C2E5]
  bb_0062C2EA[BB_0062C2EA]
  bb_0062C2F6[BB_0062C2F6]
  bb_0062C310[BB_0062C310]
  bb_0062C31C[BB_0062C31C]
  bb_0062C328[BB_0062C328]
  bb_0062C33B[BB_0062C33B]
  bb_0062C344[BB_0062C344]
  bb_0062C34D[BB_0062C34D]
  bb_0062C35A[BB_0062C35A]
  bb_0062C35D[BB_0062C35D]
  bb_0062C362[BB_0062C362]
  bb_0062C367[BB_0062C367]
  bb_0062C373[BB_0062C373]
  bb_0062C394[BB_0062C394]
  bb_0062C210 -->|branch| bb_0062C2F6
  bb_0062C210 -->|fallthrough| bb_0062C261
  bb_0062C261 -->|branch| bb_0062C272
  bb_0062C261 -->|fallthrough| bb_0062C268
  bb_0062C268 -->|branch| bb_0062C27F
  bb_0062C272 -->|branch| bb_0062C27F
  bb_0062C272 -->|fallthrough| bb_0062C276
  bb_0062C276 -->|flow| bb_0062C27F
  bb_0062C27F -->|branch| bb_0062C2AB
  bb_0062C27F -->|fallthrough| bb_0062C29F
  bb_0062C29F -->|branch| bb_0062C2BE
  bb_0062C29F -->|fallthrough| bb_0062C2AB
  bb_0062C2AB -->|branch| bb_0062C2F6
  bb_0062C2AB -->|fallthrough| bb_0062C2BE
  bb_0062C2BE -->|branch| bb_0062C2E0
  bb_0062C2C7 -->|branch| bb_0062C2DD
  bb_0062C2C7 -->|fallthrough| bb_0062C2D0
  bb_0062C2D0 -->|flow| bb_0062C2DD
  bb_0062C2DD -->|flow| bb_0062C2E0
  bb_0062C2E0 -->|branch| bb_0062C2C7
  bb_0062C2E0 -->|fallthrough| bb_0062C2E5
  bb_0062C2E5 -->|branch| bb_0062C2F6
  bb_0062C2E5 -->|fallthrough| bb_0062C2EA
  bb_0062C2EA -->|flow| bb_0062C2F6
  bb_0062C2F6 -->|branch| bb_0062C373
  bb_0062C2F6 -->|fallthrough| bb_0062C310
  bb_0062C310 -->|branch| bb_0062C328
  bb_0062C310 -->|fallthrough| bb_0062C31C
  bb_0062C31C -->|branch| bb_0062C33B
  bb_0062C31C -->|fallthrough| bb_0062C328
  bb_0062C328 -->|branch| bb_0062C373
  bb_0062C328 -->|fallthrough| bb_0062C33B
  bb_0062C33B -->|branch| bb_0062C35D
  bb_0062C344 -->|branch| bb_0062C35A
  bb_0062C344 -->|fallthrough| bb_0062C34D
  bb_0062C34D -->|flow| bb_0062C35A
  bb_0062C35A -->|flow| bb_0062C35D
  bb_0062C35D -->|branch| bb_0062C344
  bb_0062C35D -->|fallthrough| bb_0062C362
  bb_0062C362 -->|branch| bb_0062C373
  bb_0062C362 -->|fallthrough| bb_0062C367
  bb_0062C367 -->|flow| bb_0062C373
```
