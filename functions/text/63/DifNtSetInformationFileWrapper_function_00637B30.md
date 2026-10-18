# DifNtSetInformationFileWrapper

- RVA: `0x00637B30`–`0x00637CC2` (길이 `402` bytes)
- VA: `0x0000000140637B30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `116`개 명령, `402/402` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00637B70` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00637B96` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00637BD8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00637BFE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00637C17` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00637C30` → [NtSetInformationFile](../29/NtSetInformationFile_function_0029C5E0.md) (function, `0x0029C5E0`)
- `0x00637C5C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00637C82` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00637C9B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00637BA6` → RVA `0x00F048B8` (`.data`; read)
- `0x00637BC5` → RVA `0x00F04980` (`.data`; read)
- `0x00637BD1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00637B30  48 8B C4                        mov rax, rsp
00637B33  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00637B37  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00637B3B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00637B3F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00637B43  55                              push rbp
00637B44  41 54                           push r12
00637B46  41 55                           push r13
00637B48  41 56                           push r14
00637B4A  41 57                           push r15
00637B4C  48 8B EC                        mov rbp, rsp
00637B4F  48 83 EC 60                     sub rsp, 0x60
00637B53  0F 57 C0                        xorps xmm0, xmm0
00637B56  B9 CD 00 00 00                  mov ecx, 0xcd
00637B5B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00637B5F  45 8B F9                        mov r15d, r9d
00637B62  4D 8B E0                        mov r12, r8
00637B65  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00637B69  4C 8B EA                        mov r13, rdx
00637B6C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00637B70  E8 BF DE E5 FF                  call 0x140495a34
00637B75  48 8B F0                        mov rsi, rax
00637B78  48 85 C0                        test rax, rax
00637B7B  0F 84 9B 00 00 00               je 0x140637c1c
00637B81  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00637B84  A8 18                           test al, 0x18
00637B86  74 0A                           je 0x140637b92
00637B88  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00637B8C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00637B90  EB 0D                           jmp 0x140637b9f
00637B92  A8 04                           test al, 4
00637B94  74 09                           je 0x140637b9f
00637B96  E8 6D C0 E9 FF                  call 0x1404d3c08
00637B9B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00637B9F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00637BA3  45 32 F6                        xor r14b, r14b
00637BA6  44 38 35 0B CD 8C 00            cmp byte ptr [rip + 0x8ccd0b], r14b
00637BAD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00637BB1  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00637BB4  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00637BB7  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00637BBB  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00637BBF  44 89 7D DC                     mov dword ptr [rbp - 0x24], r15d
00637BC3  75 0C                           jne 0x140637bd1
00637BC5  F7 05 B1 CD 8C 00 00 08 00 00   test dword ptr [rip + 0x8ccdb1], 0x800
00637BCF  74 13                           je 0x140637be4
00637BD1  48 8D 0D A8 C2 8C 00            lea rcx, [rip + 0x8cc2a8]
00637BD8  E8 43 EA BD FF                  call 0x140216620
00637BDD  44 8A F0                        mov r14b, al
00637BE0  84 C0                           test al, al
00637BE2  74 38                           je 0x140637c1c
00637BE4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00637BE8  48 8B 1F                        mov rbx, qword ptr [rdi]
00637BEB  EB 19                           jmp 0x140637c06
00637BED  48 8D 43 F0                     lea rax, [rbx - 0x10]
00637BF1  48 85 C0                        test rax, rax
00637BF4  74 0D                           je 0x140637c03
00637BF6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00637BFA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00637BFE  E8 CD 2E 08 00                  call 0x1406baad0
00637C03  48 8B 1B                        mov rbx, qword ptr [rbx]
00637C06  48 3B DF                        cmp rbx, rdi
00637C09  75 E2                           jne 0x140637bed
00637C0B  45 84 F6                        test r14b, r14b
00637C0E  74 0C                           je 0x140637c1c
00637C10  48 8D 0D 69 C2 8C 00            lea rcx, [rip + 0x8cc269]
00637C17  E8 64 22 D1 FF                  call 0x140349e80
00637C1C  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00637C1F  45 8B CF                        mov r9d, r15d
00637C22  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00637C26  4D 8B C4                        mov r8, r12
00637C29  49 8B D5                        mov rdx, r13
00637C2C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00637C30  E8 AB 49 C6 FF                  call 0x14029c5e0
00637C35  89 45 F8                        mov dword ptr [rbp - 8], eax
00637C38  48 85 F6                        test rsi, rsi
00637C3B  74 63                           je 0x140637ca0
00637C3D  40 32 FF                        xor dil, dil
00637C40  40 38 3D 71 CC 8C 00            cmp byte ptr [rip + 0x8ccc71], dil
00637C47  75 0C                           jne 0x140637c55
00637C49  F7 05 2D CD 8C 00 00 08 00 00   test dword ptr [rip + 0x8ccd2d], 0x800
00637C53  74 13                           je 0x140637c68
00637C55  48 8D 0D 24 C2 8C 00            lea rcx, [rip + 0x8cc224]
00637C5C  E8 BF E9 BD FF                  call 0x140216620
00637C61  40 8A F8                        mov dil, al
00637C64  84 C0                           test al, al
00637C66  74 38                           je 0x140637ca0
00637C68  48 83 C6 30                     add rsi, 0x30
00637C6C  48 8B 1E                        mov rbx, qword ptr [rsi]
00637C6F  EB 19                           jmp 0x140637c8a
00637C71  48 8D 43 F0                     lea rax, [rbx - 0x10]
00637C75  48 85 C0                        test rax, rax
00637C78  74 0D                           je 0x140637c87
00637C7A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00637C7E  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00637C82  E8 49 2E 08 00                  call 0x1406baad0
00637C87  48 8B 1B                        mov rbx, qword ptr [rbx]
00637C8A  48 3B DE                        cmp rbx, rsi
00637C8D  75 E2                           jne 0x140637c71
00637C8F  40 84 FF                        test dil, dil
00637C92  74 0C                           je 0x140637ca0
00637C94  48 8D 0D E5 C1 8C 00            lea rcx, [rip + 0x8cc1e5]
00637C9B  E8 E0 21 D1 FF                  call 0x140349e80
00637CA0  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00637CA3  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00637CA8  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00637CAC  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00637CB0  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00637CB4  49 8B E3                        mov rsp, r11
00637CB7  41 5F                           pop r15
00637CB9  41 5E                           pop r14
00637CBB  41 5D                           pop r13
00637CBD  41 5C                           pop r12
00637CBF  5D                              pop rbp
00637CC0  C3                              ret
00637CC1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifNtSetInformationFileWrapper(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
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
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
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
    result = DifGetAPIThunkContextById(205, a2, a3, a4);
    if (result == 0) goto loc_00637C1C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00637B92;
    v_stack_m58 = v_stack_p0;
    goto loc_00637B9F;
loc_00637B92:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (unsigned int)((unsigned int)(a5));
    v_stack_m40 = a2;
    v_stack_m48 = a3;
    v_stack_m4C = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9227531)) != 0) goto loc_00637BD1;
    if (((*(unsigned int *)(v_rip + 9227697)) & (0x800ULL)) == 0) goto loc_00637BE4;
loc_00637BD1:
    result = ExAcquireRundownProtection(v_rip + 9224872, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00637C1C;
loc_00637BE4:
    goto loc_00637C06;
loc_00637BED:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00637C06:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00637BED;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9224809;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = NtSetInformationFile(v_stack_p8, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00637CA0;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9227377)) != 0) goto loc_00637C55;
    if (((*(unsigned int *)(v_rip + 9227565)) & (0x800ULL)) == 0) goto loc_00637C68;
loc_00637C55:
    result = ExAcquireRundownProtection(v_rip + 9224740, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00637CA0;
loc_00637C68:
    v_rsi = (result) + (48);
    goto loc_00637C8A;
loc_00637C71:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_00637C8A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00637C71;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9224677;
        result = ExReleaseRundownProtection(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifNtSetInformationFileWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
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
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
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
    result = DifGetAPIThunkContextById(205, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00637C1C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00637B92;
    v_stack_m58 = v_stack_p0;
    goto loc_00637B9F;
loc_00637B92:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m40 = Arg2;
    v_stack_m48 = Arg3;
    v_stack_m4C = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8CCD0B)) != 0) goto loc_00637BD1;
    if (((*(uint32_t *)(v_rip + 0x8CCDB1)) & (0x800ULL)) == 0) goto loc_00637BE4;
loc_00637BD1:
    result = ExAcquireRundownProtection(v_rip + 9224872, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00637C1C;
loc_00637BE4:
    goto loc_00637C06;
loc_00637BED:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00637C06:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00637BED;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9224809;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = NtSetInformationFile(v_stack_p8, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00637CA0;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CCC71)) != 0) goto loc_00637C55;
    if (((*(uint32_t *)(v_rip + 0x8CCD2D)) & (0x800ULL)) == 0) goto loc_00637C68;
loc_00637C55:
    result = ExAcquireRundownProtection(v_rip + 9224740, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00637CA0;
loc_00637C68:
    local_rsi = (result) + (48);
    goto loc_00637C8A;
loc_00637C71:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_00637C8A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00637C71;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9224677;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00637B30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00637B30[BB_00637B30]
  bb_00637B81[BB_00637B81]
  bb_00637B88[BB_00637B88]
  bb_00637B92[BB_00637B92]
  bb_00637B96[BB_00637B96]
  bb_00637B9F[BB_00637B9F]
  bb_00637BC5[BB_00637BC5]
  bb_00637BD1[BB_00637BD1]
  bb_00637BE4[BB_00637BE4]
  bb_00637BED[BB_00637BED]
  bb_00637BF6[BB_00637BF6]
  bb_00637C03[BB_00637C03]
  bb_00637C06[BB_00637C06]
  bb_00637C0B[BB_00637C0B]
  bb_00637C10[BB_00637C10]
  bb_00637C1C[BB_00637C1C]
  bb_00637C3D[BB_00637C3D]
  bb_00637C49[BB_00637C49]
  bb_00637C55[BB_00637C55]
  bb_00637C68[BB_00637C68]
  bb_00637C71[BB_00637C71]
  bb_00637C7A[BB_00637C7A]
  bb_00637C87[BB_00637C87]
  bb_00637C8A[BB_00637C8A]
  bb_00637C8F[BB_00637C8F]
  bb_00637C94[BB_00637C94]
  bb_00637CA0[BB_00637CA0]
  bb_00637CC1[BB_00637CC1]
  bb_00637B30 -->|branch| bb_00637C1C
  bb_00637B30 -->|fallthrough| bb_00637B81
  bb_00637B81 -->|branch| bb_00637B92
  bb_00637B81 -->|fallthrough| bb_00637B88
  bb_00637B88 -->|branch| bb_00637B9F
  bb_00637B92 -->|branch| bb_00637B9F
  bb_00637B92 -->|fallthrough| bb_00637B96
  bb_00637B96 -->|flow| bb_00637B9F
  bb_00637B9F -->|branch| bb_00637BD1
  bb_00637B9F -->|fallthrough| bb_00637BC5
  bb_00637BC5 -->|branch| bb_00637BE4
  bb_00637BC5 -->|fallthrough| bb_00637BD1
  bb_00637BD1 -->|branch| bb_00637C1C
  bb_00637BD1 -->|fallthrough| bb_00637BE4
  bb_00637BE4 -->|branch| bb_00637C06
  bb_00637BED -->|branch| bb_00637C03
  bb_00637BED -->|fallthrough| bb_00637BF6
  bb_00637BF6 -->|flow| bb_00637C03
  bb_00637C03 -->|flow| bb_00637C06
  bb_00637C06 -->|branch| bb_00637BED
  bb_00637C06 -->|fallthrough| bb_00637C0B
  bb_00637C0B -->|branch| bb_00637C1C
  bb_00637C0B -->|fallthrough| bb_00637C10
  bb_00637C10 -->|flow| bb_00637C1C
  bb_00637C1C -->|branch| bb_00637CA0
  bb_00637C1C -->|fallthrough| bb_00637C3D
  bb_00637C3D -->|branch| bb_00637C55
  bb_00637C3D -->|fallthrough| bb_00637C49
  bb_00637C49 -->|branch| bb_00637C68
  bb_00637C49 -->|fallthrough| bb_00637C55
  bb_00637C55 -->|branch| bb_00637CA0
  bb_00637C55 -->|fallthrough| bb_00637C68
  bb_00637C68 -->|branch| bb_00637C8A
  bb_00637C71 -->|branch| bb_00637C87
  bb_00637C71 -->|fallthrough| bb_00637C7A
  bb_00637C7A -->|flow| bb_00637C87
  bb_00637C87 -->|flow| bb_00637C8A
  bb_00637C8A -->|branch| bb_00637C71
  bb_00637C8A -->|fallthrough| bb_00637C8F
  bb_00637C8F -->|branch| bb_00637CA0
  bb_00637C8F -->|fallthrough| bb_00637C94
  bb_00637C94 -->|flow| bb_00637CA0
```
