# DifZwQueryInformationResourceManagerWrapper

- RVA: `0x006474F0`–`0x0064768C` (길이 `412` bytes)
- VA: `0x00000001406474F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `118`개 명령, `412/412` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00647534` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064755C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006475A0` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006475C6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006475DF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006475FA` → [ZwQueryInformationResourceManager](../6A/ZwQueryInformationResourceManager_function_006AFBF0.md) (function, `0x006AFBF0`)
- `0x00647626` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064764C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00647665` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064756C` → RVA `0x00F048B8` (`.data`; read)
- `0x0064758D` → RVA `0x00F04980` (`.data`; read)
- `0x00647599` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006474F0  48 8B C4                        mov rax, rsp
006474F3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006474F7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006474FB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006474FF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00647503  55                              push rbp
00647504  41 54                           push r12
00647506  41 55                           push r13
00647508  41 56                           push r14
0064750A  41 57                           push r15
0064750C  48 8B EC                        mov rbp, rsp
0064750F  48 83 EC 70                     sub rsp, 0x70
00647513  33 C0                           xor eax, eax
00647515  0F 57 C0                        xorps xmm0, xmm0
00647518  45 8B F9                        mov r15d, r9d
0064751B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064751F  4D 8B E0                        mov r12, r8
00647522  44 8B EA                        mov r13d, edx
00647525  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00647529  8D 48 2F                        lea ecx, [rax + 0x2f]
0064752C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00647530  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00647534  E8 FB E4 E4 FF                  call 0x140495a34
00647539  4C 8B F0                        mov r14, rax
0064753C  48 85 C0                        test rax, rax
0064753F  0F 84 9F 00 00 00               je 0x1406475e4
00647545  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00647548  F6 C1 18                        test cl, 0x18
0064754B  74 0A                           je 0x140647557
0064754D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00647551  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00647555  EB 0E                           jmp 0x140647565
00647557  F6 C1 04                        test cl, 4
0064755A  74 09                           je 0x140647565
0064755C  E8 A7 C6 E8 FF                  call 0x1404d3c08
00647561  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00647565  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00647569  40 32 F6                        xor sil, sil
0064756C  40 38 35 45 D3 8B 00            cmp byte ptr [rip + 0x8bd345], sil
00647573  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00647577  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064757B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0064757F  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00647583  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00647587  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
0064758B  75 0C                           jne 0x140647599
0064758D  F7 05 E9 D3 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd3e9], 0x800
00647597  74 13                           je 0x1406475ac
00647599  48 8D 0D E0 C8 8B 00            lea rcx, [rip + 0x8bc8e0]
006475A0  E8 7B F0 BC FF                  call 0x140216620
006475A5  40 8A F0                        mov sil, al
006475A8  84 C0                           test al, al
006475AA  74 38                           je 0x1406475e4
006475AC  49 8D 7E 20                     lea rdi, [r14 + 0x20]
006475B0  48 8B 1F                        mov rbx, qword ptr [rdi]
006475B3  EB 19                           jmp 0x1406475ce
006475B5  48 8D 43 F0                     lea rax, [rbx - 0x10]
006475B9  48 85 C0                        test rax, rax
006475BC  74 0D                           je 0x1406475cb
006475BE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006475C2  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006475C6  E8 05 35 07 00                  call 0x1406baad0
006475CB  48 8B 1B                        mov rbx, qword ptr [rbx]
006475CE  48 3B DF                        cmp rbx, rdi
006475D1  75 E2                           jne 0x1406475b5
006475D3  40 84 F6                        test sil, sil
006475D6  74 0C                           je 0x1406475e4
006475D8  48 8D 0D A1 C8 8B 00            lea rcx, [rip + 0x8bc8a1]
006475DF  E8 9C 28 D0 FF                  call 0x140349e80
006475E4  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
006475E8  45 8B CF                        mov r9d, r15d
006475EB  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006475EF  4D 8B C4                        mov r8, r12
006475F2  41 8B D5                        mov edx, r13d
006475F5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006475FA  E8 F1 85 06 00                  call 0x1406afbf0
006475FF  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00647602  4D 85 F6                        test r14, r14
00647605  74 63                           je 0x14064766a
00647607  40 32 FF                        xor dil, dil
0064760A  40 38 3D A7 D2 8B 00            cmp byte ptr [rip + 0x8bd2a7], dil
00647611  75 0C                           jne 0x14064761f
00647613  F7 05 63 D3 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd363], 0x800
0064761D  74 13                           je 0x140647632
0064761F  48 8D 0D 5A C8 8B 00            lea rcx, [rip + 0x8bc85a]
00647626  E8 F5 EF BC FF                  call 0x140216620
0064762B  40 8A F8                        mov dil, al
0064762E  84 C0                           test al, al
00647630  74 38                           je 0x14064766a
00647632  49 8D 76 30                     lea rsi, [r14 + 0x30]
00647636  48 8B 1E                        mov rbx, qword ptr [rsi]
00647639  EB 19                           jmp 0x140647654
0064763B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064763F  48 85 C0                        test rax, rax
00647642  74 0D                           je 0x140647651
00647644  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647648  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0064764C  E8 7F 34 07 00                  call 0x1406baad0
00647651  48 8B 1B                        mov rbx, qword ptr [rbx]
00647654  48 3B DE                        cmp rbx, rsi
00647657  75 E2                           jne 0x14064763b
00647659  40 84 FF                        test dil, dil
0064765C  74 0C                           je 0x14064766a
0064765E  48 8D 0D 1B C8 8B 00            lea rcx, [rip + 0x8bc81b]
00647665  E8 16 28 D0 FF                  call 0x140349e80
0064766A  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0064766D  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00647672  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00647676  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064767A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064767E  49 8B E3                        mov rsp, r11
00647681  41 5F                           pop r15
00647683  41 5E                           pop r14
00647685  41 5D                           pop r13
00647687  41 5C                           pop r12
00647689  5D                              pop rbp
0064768A  C3                              ret
0064768B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryInformationResourceManagerWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 47, a2, a3, a4);
    if (result == 0) goto loc_006475E4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00647557;
    v_stack_m68 = v_stack_p0;
    goto loc_00647565;
loc_00647557:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = a5;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    v_stack_m58 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9163589)) != 0) goto loc_00647599;
    if (((*(unsigned int *)(v_rip + 9163753)) & (0x800ULL)) == 0) goto loc_006475AC;
loc_00647599:
    result = ExAcquireRundownProtection(v_rip + 9160928, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006475E4;
loc_006475AC:
    goto loc_006475CE;
loc_006475B5:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006475CE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006475B5;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9160865;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwQueryInformationResourceManager(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0064766A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9163431)) != 0) goto loc_0064761F;
    if (((*(unsigned int *)(v_rip + 9163619)) & (0x800ULL)) == 0) goto loc_00647632;
loc_0064761F:
    result = ExAcquireRundownProtection(v_rip + 9160794, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0064766A;
loc_00647632:
    goto loc_00647654;
loc_0064763B:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_00647654:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0064763B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9160731;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryInformationResourceManagerWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 47, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006475E4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00647557;
    v_stack_m68 = v_stack_p0;
    goto loc_00647565;
loc_00647557:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = Arg5;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8BD345)) != 0) goto loc_00647599;
    if (((*(uint32_t *)(v_rip + 0x8BD3E9)) & (0x800ULL)) == 0) goto loc_006475AC;
loc_00647599:
    result = ExAcquireRundownProtection(v_rip + 9160928, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006475E4;
loc_006475AC:
    goto loc_006475CE;
loc_006475B5:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006475CE:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006475B5;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9160865;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwQueryInformationResourceManager(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0064766A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BD2A7)) != 0) goto loc_0064761F;
    if (((*(uint32_t *)(v_rip + 0x8BD363)) & (0x800ULL)) == 0) goto loc_00647632;
loc_0064761F:
    result = ExAcquireRundownProtection(v_rip + 9160794, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0064766A;
loc_00647632:
    goto loc_00647654;
loc_0064763B:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_00647654:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0064763B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9160731;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006474F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006474F0[BB_006474F0]
  bb_00647545[BB_00647545]
  bb_0064754D[BB_0064754D]
  bb_00647557[BB_00647557]
  bb_0064755C[BB_0064755C]
  bb_00647565[BB_00647565]
  bb_0064758D[BB_0064758D]
  bb_00647599[BB_00647599]
  bb_006475AC[BB_006475AC]
  bb_006475B5[BB_006475B5]
  bb_006475BE[BB_006475BE]
  bb_006475CB[BB_006475CB]
  bb_006475CE[BB_006475CE]
  bb_006475D3[BB_006475D3]
  bb_006475D8[BB_006475D8]
  bb_006475E4[BB_006475E4]
  bb_00647607[BB_00647607]
  bb_00647613[BB_00647613]
  bb_0064761F[BB_0064761F]
  bb_00647632[BB_00647632]
  bb_0064763B[BB_0064763B]
  bb_00647644[BB_00647644]
  bb_00647651[BB_00647651]
  bb_00647654[BB_00647654]
  bb_00647659[BB_00647659]
  bb_0064765E[BB_0064765E]
  bb_0064766A[BB_0064766A]
  bb_0064768B[BB_0064768B]
  bb_006474F0 -->|branch| bb_006475E4
  bb_006474F0 -->|fallthrough| bb_00647545
  bb_00647545 -->|branch| bb_00647557
  bb_00647545 -->|fallthrough| bb_0064754D
  bb_0064754D -->|branch| bb_00647565
  bb_00647557 -->|branch| bb_00647565
  bb_00647557 -->|fallthrough| bb_0064755C
  bb_0064755C -->|flow| bb_00647565
  bb_00647565 -->|branch| bb_00647599
  bb_00647565 -->|fallthrough| bb_0064758D
  bb_0064758D -->|branch| bb_006475AC
  bb_0064758D -->|fallthrough| bb_00647599
  bb_00647599 -->|branch| bb_006475E4
  bb_00647599 -->|fallthrough| bb_006475AC
  bb_006475AC -->|branch| bb_006475CE
  bb_006475B5 -->|branch| bb_006475CB
  bb_006475B5 -->|fallthrough| bb_006475BE
  bb_006475BE -->|flow| bb_006475CB
  bb_006475CB -->|flow| bb_006475CE
  bb_006475CE -->|branch| bb_006475B5
  bb_006475CE -->|fallthrough| bb_006475D3
  bb_006475D3 -->|branch| bb_006475E4
  bb_006475D3 -->|fallthrough| bb_006475D8
  bb_006475D8 -->|flow| bb_006475E4
  bb_006475E4 -->|branch| bb_0064766A
  bb_006475E4 -->|fallthrough| bb_00647607
  bb_00647607 -->|branch| bb_0064761F
  bb_00647607 -->|fallthrough| bb_00647613
  bb_00647613 -->|branch| bb_00647632
  bb_00647613 -->|fallthrough| bb_0064761F
  bb_0064761F -->|branch| bb_0064766A
  bb_0064761F -->|fallthrough| bb_00647632
  bb_00647632 -->|branch| bb_00647654
  bb_0064763B -->|branch| bb_00647651
  bb_0064763B -->|fallthrough| bb_00647644
  bb_00647644 -->|flow| bb_00647651
  bb_00647651 -->|flow| bb_00647654
  bb_00647654 -->|branch| bb_0064763B
  bb_00647654 -->|fallthrough| bb_00647659
  bb_00647659 -->|branch| bb_0064766A
  bb_00647659 -->|fallthrough| bb_0064765E
  bb_0064765E -->|flow| bb_0064766A
```
