# DifHalDmaAllocateCrashDumpRegistersExWrapper

- RVA: `0x00624330`–`0x006244C6` (길이 `406` bytes)
- VA: `0x0000000140624330`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `116`개 명령, `406/406` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00624370` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00624396` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006243DA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00624400` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00624419` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00624434` → [HalDmaAllocateCrashDumpRegistersEx](../53/HalDmaAllocateCrashDumpRegistersEx_function_0053F6D0.md) (function, `0x0053F6D0`)
- `0x00624460` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00624486` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062449F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006243A6` → RVA `0x00F048B8` (`.data`; read)
- `0x006243C7` → RVA `0x00F04980` (`.data`; read)
- `0x006243D3` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00624330  48 8B C4                        mov rax, rsp
00624333  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00624337  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062433B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062433F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00624343  55                              push rbp
00624344  41 54                           push r12
00624346  41 55                           push r13
00624348  41 56                           push r14
0062434A  41 57                           push r15
0062434C  48 8B EC                        mov rbp, rsp
0062434F  48 83 EC 60                     sub rsp, 0x60
00624353  0F 57 C0                        xorps xmm0, xmm0
00624356  B9 75 01 00 00                  mov ecx, 0x175
0062435B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062435F  4D 8B F9                        mov r15, r9
00624362  45 8B E0                        mov r12d, r8d
00624365  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00624369  44 8B EA                        mov r13d, edx
0062436C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00624370  E8 BF 16 E7 FF                  call 0x140495a34
00624375  48 8B F0                        mov rsi, rax
00624378  48 85 C0                        test rax, rax
0062437B  0F 84 9D 00 00 00               je 0x14062441e
00624381  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00624384  A8 18                           test al, 0x18
00624386  74 0A                           je 0x140624392
00624388  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062438C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00624390  EB 0D                           jmp 0x14062439f
00624392  A8 04                           test al, 4
00624394  74 09                           je 0x14062439f
00624396  E8 6D F8 EA FF                  call 0x1404d3c08
0062439B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062439F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
006243A3  45 32 F6                        xor r14b, r14b
006243A6  44 38 35 0B 05 8E 00            cmp byte ptr [rip + 0x8e050b], r14b
006243AD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006243B1  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
006243B5  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
006243B9  44 89 6D EC                     mov dword ptr [rbp - 0x14], r13d
006243BD  44 89 65 E8                     mov dword ptr [rbp - 0x18], r12d
006243C1  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
006243C5  75 0C                           jne 0x1406243d3
006243C7  F7 05 AF 05 8E 00 00 08 00 00   test dword ptr [rip + 0x8e05af], 0x800
006243D1  74 13                           je 0x1406243e6
006243D3  48 8D 0D A6 FA 8D 00            lea rcx, [rip + 0x8dfaa6]
006243DA  E8 41 22 BF FF                  call 0x140216620
006243DF  44 8A F0                        mov r14b, al
006243E2  84 C0                           test al, al
006243E4  74 38                           je 0x14062441e
006243E6  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006243EA  48 8B 1F                        mov rbx, qword ptr [rdi]
006243ED  EB 19                           jmp 0x140624408
006243EF  48 8D 43 F0                     lea rax, [rbx - 0x10]
006243F3  48 85 C0                        test rax, rax
006243F6  74 0D                           je 0x140624405
006243F8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006243FC  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00624400  E8 CB 66 09 00                  call 0x1406baad0
00624405  48 8B 1B                        mov rbx, qword ptr [rbx]
00624408  48 3B DF                        cmp rbx, rdi
0062440B  75 E2                           jne 0x1406243ef
0062440D  45 84 F6                        test r14b, r14b
00624410  74 0C                           je 0x14062441e
00624412  48 8D 0D 67 FA 8D 00            lea rcx, [rip + 0x8dfa67]
00624419  E8 62 5A D2 FF                  call 0x140349e80
0062441E  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00624422  4D 8B CF                        mov r9, r15
00624425  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00624429  45 8B C4                        mov r8d, r12d
0062442C  41 8B D5                        mov edx, r13d
0062442F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00624434  E8 97 B2 F1 FF                  call 0x14053f6d0
00624439  89 45 F8                        mov dword ptr [rbp - 8], eax
0062443C  48 85 F6                        test rsi, rsi
0062443F  74 63                           je 0x1406244a4
00624441  40 32 FF                        xor dil, dil
00624444  40 38 3D 6D 04 8E 00            cmp byte ptr [rip + 0x8e046d], dil
0062444B  75 0C                           jne 0x140624459
0062444D  F7 05 29 05 8E 00 00 08 00 00   test dword ptr [rip + 0x8e0529], 0x800
00624457  74 13                           je 0x14062446c
00624459  48 8D 0D 20 FA 8D 00            lea rcx, [rip + 0x8dfa20]
00624460  E8 BB 21 BF FF                  call 0x140216620
00624465  40 8A F8                        mov dil, al
00624468  84 C0                           test al, al
0062446A  74 38                           je 0x1406244a4
0062446C  48 83 C6 30                     add rsi, 0x30
00624470  48 8B 1E                        mov rbx, qword ptr [rsi]
00624473  EB 19                           jmp 0x14062448e
00624475  48 8D 43 F0                     lea rax, [rbx - 0x10]
00624479  48 85 C0                        test rax, rax
0062447C  74 0D                           je 0x14062448b
0062447E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00624482  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00624486  E8 45 66 09 00                  call 0x1406baad0
0062448B  48 8B 1B                        mov rbx, qword ptr [rbx]
0062448E  48 3B DE                        cmp rbx, rsi
00624491  75 E2                           jne 0x140624475
00624493  40 84 FF                        test dil, dil
00624496  74 0C                           je 0x1406244a4
00624498  48 8D 0D E1 F9 8D 00            lea rcx, [rip + 0x8df9e1]
0062449F  E8 DC 59 D2 FF                  call 0x140349e80
006244A4  8B 45 F8                        mov eax, dword ptr [rbp - 8]
006244A7  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
006244AC  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
006244B0  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
006244B4  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
006244B8  49 8B E3                        mov rsp, r11
006244BB  41 5F                           pop r15
006244BD  41 5E                           pop r14
006244BF  41 5D                           pop r13
006244C1  41 5C                           pop r12
006244C3  5D                              pop rbp
006244C4  C3                              ret
006244C5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifHalDmaAllocateCrashDumpRegistersExWrapper(__int64 a1, int a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(373, a2, a3, a4);
    if (result == 0) goto loc_0062441E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00624392;
    v_stack_m58 = v_stack_p0;
    goto loc_0062439F;
loc_00624392:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = a5;
    v_stack_m3C = (unsigned int)((unsigned int)(a2));
    v_stack_m40 = (unsigned int)((unsigned int)(a3));
    v_stack_m48 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9307403)) != 0) goto loc_006243D3;
    if (((*(unsigned int *)(v_rip + 9307567)) & (0x800ULL)) == 0) goto loc_006243E6;
loc_006243D3:
    result = ExAcquireRundownProtection(v_rip + 9304742, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062441E;
loc_006243E6:
    goto loc_00624408;
loc_006243EF:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00624408:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006243EF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9304679;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = a5;
    result = HalDmaAllocateCrashDumpRegistersEx(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_006244A4;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9307245)) != 0) goto loc_00624459;
    if (((*(unsigned int *)(v_rip + 9307433)) & (0x800ULL)) == 0) goto loc_0062446C;
loc_00624459:
    result = ExAcquireRundownProtection(v_rip + 9304608, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_006244A4;
loc_0062446C:
    v_rsi = (result) + (48);
    goto loc_0062448E;
loc_00624475:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0062448E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00624475;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9304545;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifHalDmaAllocateCrashDumpRegistersExWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(373, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062441E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00624392;
    v_stack_m58 = v_stack_p0;
    goto loc_0062439F;
loc_00624392:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = Arg5;
    v_stack_m3C = (uint32_t)((uint32_t)(Arg2));
    v_stack_m40 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m48 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8E050B)) != 0) goto loc_006243D3;
    if (((*(uint32_t *)(v_rip + 0x8E05AF)) & (0x800ULL)) == 0) goto loc_006243E6;
loc_006243D3:
    result = ExAcquireRundownProtection(v_rip + 9304742, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062441E;
loc_006243E6:
    goto loc_00624408;
loc_006243EF:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00624408:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006243EF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9304679;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = Arg5;
    result = HalDmaAllocateCrashDumpRegistersEx(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_006244A4;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E046D)) != 0) goto loc_00624459;
    if (((*(uint32_t *)(v_rip + 0x8E0529)) & (0x800ULL)) == 0) goto loc_0062446C;
loc_00624459:
    result = ExAcquireRundownProtection(v_rip + 9304608, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_006244A4;
loc_0062446C:
    local_rsi = (result) + (48);
    goto loc_0062448E;
loc_00624475:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_0062448E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00624475;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9304545;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00624330&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00624330[BB_00624330]
  bb_00624381[BB_00624381]
  bb_00624388[BB_00624388]
  bb_00624392[BB_00624392]
  bb_00624396[BB_00624396]
  bb_0062439F[BB_0062439F]
  bb_006243C7[BB_006243C7]
  bb_006243D3[BB_006243D3]
  bb_006243E6[BB_006243E6]
  bb_006243EF[BB_006243EF]
  bb_006243F8[BB_006243F8]
  bb_00624405[BB_00624405]
  bb_00624408[BB_00624408]
  bb_0062440D[BB_0062440D]
  bb_00624412[BB_00624412]
  bb_0062441E[BB_0062441E]
  bb_00624441[BB_00624441]
  bb_0062444D[BB_0062444D]
  bb_00624459[BB_00624459]
  bb_0062446C[BB_0062446C]
  bb_00624475[BB_00624475]
  bb_0062447E[BB_0062447E]
  bb_0062448B[BB_0062448B]
  bb_0062448E[BB_0062448E]
  bb_00624493[BB_00624493]
  bb_00624498[BB_00624498]
  bb_006244A4[BB_006244A4]
  bb_006244C5[BB_006244C5]
  bb_00624330 -->|branch| bb_0062441E
  bb_00624330 -->|fallthrough| bb_00624381
  bb_00624381 -->|branch| bb_00624392
  bb_00624381 -->|fallthrough| bb_00624388
  bb_00624388 -->|branch| bb_0062439F
  bb_00624392 -->|branch| bb_0062439F
  bb_00624392 -->|fallthrough| bb_00624396
  bb_00624396 -->|flow| bb_0062439F
  bb_0062439F -->|branch| bb_006243D3
  bb_0062439F -->|fallthrough| bb_006243C7
  bb_006243C7 -->|branch| bb_006243E6
  bb_006243C7 -->|fallthrough| bb_006243D3
  bb_006243D3 -->|branch| bb_0062441E
  bb_006243D3 -->|fallthrough| bb_006243E6
  bb_006243E6 -->|branch| bb_00624408
  bb_006243EF -->|branch| bb_00624405
  bb_006243EF -->|fallthrough| bb_006243F8
  bb_006243F8 -->|flow| bb_00624405
  bb_00624405 -->|flow| bb_00624408
  bb_00624408 -->|branch| bb_006243EF
  bb_00624408 -->|fallthrough| bb_0062440D
  bb_0062440D -->|branch| bb_0062441E
  bb_0062440D -->|fallthrough| bb_00624412
  bb_00624412 -->|flow| bb_0062441E
  bb_0062441E -->|branch| bb_006244A4
  bb_0062441E -->|fallthrough| bb_00624441
  bb_00624441 -->|branch| bb_00624459
  bb_00624441 -->|fallthrough| bb_0062444D
  bb_0062444D -->|branch| bb_0062446C
  bb_0062444D -->|fallthrough| bb_00624459
  bb_00624459 -->|branch| bb_006244A4
  bb_00624459 -->|fallthrough| bb_0062446C
  bb_0062446C -->|branch| bb_0062448E
  bb_00624475 -->|branch| bb_0062448B
  bb_00624475 -->|fallthrough| bb_0062447E
  bb_0062447E -->|flow| bb_0062448B
  bb_0062448B -->|flow| bb_0062448E
  bb_0062448E -->|branch| bb_00624475
  bb_0062448E -->|fallthrough| bb_00624493
  bb_00624493 -->|branch| bb_006244A4
  bb_00624493 -->|fallthrough| bb_00624498
  bb_00624498 -->|flow| bb_006244A4
```
