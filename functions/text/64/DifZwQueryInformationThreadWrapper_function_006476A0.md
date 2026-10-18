# DifZwQueryInformationThreadWrapper

- RVA: `0x006476A0`–`0x0064783C` (길이 `412` bytes)
- VA: `0x00000001406476A0`
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
- `0x006476E4` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064770C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00647750` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647776` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064778F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006477AA` → [ZwQueryInformationThread](../6A/ZwQueryInformationThread_function_006AD570.md) (function, `0x006AD570`)
- `0x006477D6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006477FC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00647815` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064771C` → RVA `0x00F048B8` (`.data`; read)
- `0x0064773D` → RVA `0x00F04980` (`.data`; read)
- `0x00647749` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006476A0  48 8B C4                        mov rax, rsp
006476A3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006476A7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006476AB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006476AF  48 89 48 08                     mov qword ptr [rax + 8], rcx
006476B3  55                              push rbp
006476B4  41 54                           push r12
006476B6  41 55                           push r13
006476B8  41 56                           push r14
006476BA  41 57                           push r15
006476BC  48 8B EC                        mov rbp, rsp
006476BF  48 83 EC 70                     sub rsp, 0x70
006476C3  33 C0                           xor eax, eax
006476C5  0F 57 C0                        xorps xmm0, xmm0
006476C8  45 8B F9                        mov r15d, r9d
006476CB  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006476CF  4D 8B E0                        mov r12, r8
006476D2  44 8B EA                        mov r13d, edx
006476D5  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
006476D9  8D 48 2E                        lea ecx, [rax + 0x2e]
006476DC  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006476E0  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006476E4  E8 4B E3 E4 FF                  call 0x140495a34
006476E9  4C 8B F0                        mov r14, rax
006476EC  48 85 C0                        test rax, rax
006476EF  0F 84 9F 00 00 00               je 0x140647794
006476F5  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
006476F8  F6 C1 18                        test cl, 0x18
006476FB  74 0A                           je 0x140647707
006476FD  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00647701  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00647705  EB 0E                           jmp 0x140647715
00647707  F6 C1 04                        test cl, 4
0064770A  74 09                           je 0x140647715
0064770C  E8 F7 C4 E8 FF                  call 0x1404d3c08
00647711  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00647715  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00647719  40 32 F6                        xor sil, sil
0064771C  40 38 35 95 D1 8B 00            cmp byte ptr [rip + 0x8bd195], sil
00647723  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00647727  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064772B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0064772F  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00647733  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00647737  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
0064773B  75 0C                           jne 0x140647749
0064773D  F7 05 39 D2 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd239], 0x800
00647747  74 13                           je 0x14064775c
00647749  48 8D 0D 30 C7 8B 00            lea rcx, [rip + 0x8bc730]
00647750  E8 CB EE BC FF                  call 0x140216620
00647755  40 8A F0                        mov sil, al
00647758  84 C0                           test al, al
0064775A  74 38                           je 0x140647794
0064775C  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00647760  48 8B 1F                        mov rbx, qword ptr [rdi]
00647763  EB 19                           jmp 0x14064777e
00647765  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647769  48 85 C0                        test rax, rax
0064776C  74 0D                           je 0x14064777b
0064776E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647772  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00647776  E8 55 33 07 00                  call 0x1406baad0
0064777B  48 8B 1B                        mov rbx, qword ptr [rbx]
0064777E  48 3B DF                        cmp rbx, rdi
00647781  75 E2                           jne 0x140647765
00647783  40 84 F6                        test sil, sil
00647786  74 0C                           je 0x140647794
00647788  48 8D 0D F1 C6 8B 00            lea rcx, [rip + 0x8bc6f1]
0064778F  E8 EC 26 D0 FF                  call 0x140349e80
00647794  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00647798  45 8B CF                        mov r9d, r15d
0064779B  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064779F  4D 8B C4                        mov r8, r12
006477A2  41 8B D5                        mov edx, r13d
006477A5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006477AA  E8 C1 5D 06 00                  call 0x1406ad570
006477AF  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006477B2  4D 85 F6                        test r14, r14
006477B5  74 63                           je 0x14064781a
006477B7  40 32 FF                        xor dil, dil
006477BA  40 38 3D F7 D0 8B 00            cmp byte ptr [rip + 0x8bd0f7], dil
006477C1  75 0C                           jne 0x1406477cf
006477C3  F7 05 B3 D1 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd1b3], 0x800
006477CD  74 13                           je 0x1406477e2
006477CF  48 8D 0D AA C6 8B 00            lea rcx, [rip + 0x8bc6aa]
006477D6  E8 45 EE BC FF                  call 0x140216620
006477DB  40 8A F8                        mov dil, al
006477DE  84 C0                           test al, al
006477E0  74 38                           je 0x14064781a
006477E2  49 8D 76 30                     lea rsi, [r14 + 0x30]
006477E6  48 8B 1E                        mov rbx, qword ptr [rsi]
006477E9  EB 19                           jmp 0x140647804
006477EB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006477EF  48 85 C0                        test rax, rax
006477F2  74 0D                           je 0x140647801
006477F4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006477F8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006477FC  E8 CF 32 07 00                  call 0x1406baad0
00647801  48 8B 1B                        mov rbx, qword ptr [rbx]
00647804  48 3B DE                        cmp rbx, rsi
00647807  75 E2                           jne 0x1406477eb
00647809  40 84 FF                        test dil, dil
0064780C  74 0C                           je 0x14064781a
0064780E  48 8D 0D 6B C6 8B 00            lea rcx, [rip + 0x8bc66b]
00647815  E8 66 26 D0 FF                  call 0x140349e80
0064781A  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0064781D  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00647822  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00647826  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064782A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064782E  49 8B E3                        mov rsp, r11
00647831  41 5F                           pop r15
00647833  41 5E                           pop r14
00647835  41 5D                           pop r13
00647837  41 5C                           pop r12
00647839  5D                              pop rbp
0064783A  C3                              ret
0064783B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryInformationThreadWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
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
    result = DifGetAPIThunkContextById(result + 46, a2, a3, a4);
    if (result == 0) goto loc_00647794;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00647707;
    v_stack_m68 = v_stack_p0;
    goto loc_00647715;
loc_00647707:
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
    if ((*(unsigned __int8 *)(v_rip + 9163157)) != 0) goto loc_00647749;
    if (((*(unsigned int *)(v_rip + 9163321)) & (0x800ULL)) == 0) goto loc_0064775C;
loc_00647749:
    result = ExAcquireRundownProtection(v_rip + 9160496, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00647794;
loc_0064775C:
    goto loc_0064777E;
loc_00647765:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064777E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00647765;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9160433;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwQueryInformationThread(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0064781A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9162999)) != 0) goto loc_006477CF;
    if (((*(unsigned int *)(v_rip + 9163187)) & (0x800ULL)) == 0) goto loc_006477E2;
loc_006477CF:
    result = ExAcquireRundownProtection(v_rip + 9160362, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0064781A;
loc_006477E2:
    goto loc_00647804;
loc_006477EB:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_00647804:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006477EB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9160299;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryInformationThreadWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
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
    result = DifGetAPIThunkContextById(result + 46, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00647794;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00647707;
    v_stack_m68 = v_stack_p0;
    goto loc_00647715;
loc_00647707:
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
    if ((*(uint8_t *)(v_rip + 0x8BD195)) != 0) goto loc_00647749;
    if (((*(uint32_t *)(v_rip + 0x8BD239)) & (0x800ULL)) == 0) goto loc_0064775C;
loc_00647749:
    result = ExAcquireRundownProtection(v_rip + 9160496, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00647794;
loc_0064775C:
    goto loc_0064777E;
loc_00647765:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064777E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00647765;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9160433;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwQueryInformationThread(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0064781A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BD0F7)) != 0) goto loc_006477CF;
    if (((*(uint32_t *)(v_rip + 0x8BD1B3)) & (0x800ULL)) == 0) goto loc_006477E2;
loc_006477CF:
    result = ExAcquireRundownProtection(v_rip + 9160362, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0064781A;
loc_006477E2:
    goto loc_00647804;
loc_006477EB:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_00647804:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006477EB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9160299;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006476A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006476A0[BB_006476A0]
  bb_006476F5[BB_006476F5]
  bb_006476FD[BB_006476FD]
  bb_00647707[BB_00647707]
  bb_0064770C[BB_0064770C]
  bb_00647715[BB_00647715]
  bb_0064773D[BB_0064773D]
  bb_00647749[BB_00647749]
  bb_0064775C[BB_0064775C]
  bb_00647765[BB_00647765]
  bb_0064776E[BB_0064776E]
  bb_0064777B[BB_0064777B]
  bb_0064777E[BB_0064777E]
  bb_00647783[BB_00647783]
  bb_00647788[BB_00647788]
  bb_00647794[BB_00647794]
  bb_006477B7[BB_006477B7]
  bb_006477C3[BB_006477C3]
  bb_006477CF[BB_006477CF]
  bb_006477E2[BB_006477E2]
  bb_006477EB[BB_006477EB]
  bb_006477F4[BB_006477F4]
  bb_00647801[BB_00647801]
  bb_00647804[BB_00647804]
  bb_00647809[BB_00647809]
  bb_0064780E[BB_0064780E]
  bb_0064781A[BB_0064781A]
  bb_0064783B[BB_0064783B]
  bb_006476A0 -->|branch| bb_00647794
  bb_006476A0 -->|fallthrough| bb_006476F5
  bb_006476F5 -->|branch| bb_00647707
  bb_006476F5 -->|fallthrough| bb_006476FD
  bb_006476FD -->|branch| bb_00647715
  bb_00647707 -->|branch| bb_00647715
  bb_00647707 -->|fallthrough| bb_0064770C
  bb_0064770C -->|flow| bb_00647715
  bb_00647715 -->|branch| bb_00647749
  bb_00647715 -->|fallthrough| bb_0064773D
  bb_0064773D -->|branch| bb_0064775C
  bb_0064773D -->|fallthrough| bb_00647749
  bb_00647749 -->|branch| bb_00647794
  bb_00647749 -->|fallthrough| bb_0064775C
  bb_0064775C -->|branch| bb_0064777E
  bb_00647765 -->|branch| bb_0064777B
  bb_00647765 -->|fallthrough| bb_0064776E
  bb_0064776E -->|flow| bb_0064777B
  bb_0064777B -->|flow| bb_0064777E
  bb_0064777E -->|branch| bb_00647765
  bb_0064777E -->|fallthrough| bb_00647783
  bb_00647783 -->|branch| bb_00647794
  bb_00647783 -->|fallthrough| bb_00647788
  bb_00647788 -->|flow| bb_00647794
  bb_00647794 -->|branch| bb_0064781A
  bb_00647794 -->|fallthrough| bb_006477B7
  bb_006477B7 -->|branch| bb_006477CF
  bb_006477B7 -->|fallthrough| bb_006477C3
  bb_006477C3 -->|branch| bb_006477E2
  bb_006477C3 -->|fallthrough| bb_006477CF
  bb_006477CF -->|branch| bb_0064781A
  bb_006477CF -->|fallthrough| bb_006477E2
  bb_006477E2 -->|branch| bb_00647804
  bb_006477EB -->|branch| bb_00647801
  bb_006477EB -->|fallthrough| bb_006477F4
  bb_006477F4 -->|flow| bb_00647801
  bb_00647801 -->|flow| bb_00647804
  bb_00647804 -->|branch| bb_006477EB
  bb_00647804 -->|fallthrough| bb_00647809
  bb_00647809 -->|branch| bb_0064781A
  bb_00647809 -->|fallthrough| bb_0064780E
  bb_0064780E -->|flow| bb_0064781A
```
