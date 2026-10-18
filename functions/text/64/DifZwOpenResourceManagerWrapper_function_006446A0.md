# DifZwOpenResourceManagerWrapper

- RVA: `0x006446A0`–`0x0064483C` (길이 `412` bytes)
- VA: `0x00000001406446A0`
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
- `0x006446E4` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064470C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00644750` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00644776` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064478F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006447AA` → [ZwOpenResourceManager](../6A/ZwOpenResourceManager_function_006AF790.md) (function, `0x006AF790`)
- `0x006447D6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006447FC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00644815` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064471C` → RVA `0x00F048B8` (`.data`; read)
- `0x0064473D` → RVA `0x00F04980` (`.data`; read)
- `0x00644749` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006446A0  48 8B C4                        mov rax, rsp
006446A3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006446A7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006446AB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006446AF  48 89 48 08                     mov qword ptr [rax + 8], rcx
006446B3  55                              push rbp
006446B4  41 54                           push r12
006446B6  41 55                           push r13
006446B8  41 56                           push r14
006446BA  41 57                           push r15
006446BC  48 8B EC                        mov rbp, rsp
006446BF  48 83 EC 70                     sub rsp, 0x70
006446C3  33 C0                           xor eax, eax
006446C5  0F 57 C0                        xorps xmm0, xmm0
006446C8  4D 8B F9                        mov r15, r9
006446CB  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006446CF  4D 8B E0                        mov r12, r8
006446D2  44 8B EA                        mov r13d, edx
006446D5  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
006446D9  8D 48 4C                        lea ecx, [rax + 0x4c]
006446DC  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006446E0  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006446E4  E8 4B 13 E5 FF                  call 0x140495a34
006446E9  4C 8B F0                        mov r14, rax
006446EC  48 85 C0                        test rax, rax
006446EF  0F 84 9F 00 00 00               je 0x140644794
006446F5  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
006446F8  F6 C1 18                        test cl, 0x18
006446FB  74 0A                           je 0x140644707
006446FD  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00644701  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00644705  EB 0E                           jmp 0x140644715
00644707  F6 C1 04                        test cl, 4
0064470A  74 09                           je 0x140644715
0064470C  E8 F7 F4 E8 FF                  call 0x1404d3c08
00644711  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00644715  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00644719  40 32 F6                        xor sil, sil
0064471C  40 38 35 95 01 8C 00            cmp byte ptr [rip + 0x8c0195], sil
00644723  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00644727  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064472B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0064472F  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00644733  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00644737  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
0064473B  75 0C                           jne 0x140644749
0064473D  F7 05 39 02 8C 00 00 08 00 00   test dword ptr [rip + 0x8c0239], 0x800
00644747  74 13                           je 0x14064475c
00644749  48 8D 0D 30 F7 8B 00            lea rcx, [rip + 0x8bf730]
00644750  E8 CB 1E BD FF                  call 0x140216620
00644755  40 8A F0                        mov sil, al
00644758  84 C0                           test al, al
0064475A  74 38                           je 0x140644794
0064475C  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00644760  48 8B 1F                        mov rbx, qword ptr [rdi]
00644763  EB 19                           jmp 0x14064477e
00644765  48 8D 43 F0                     lea rax, [rbx - 0x10]
00644769  48 85 C0                        test rax, rax
0064476C  74 0D                           je 0x14064477b
0064476E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644772  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00644776  E8 55 63 07 00                  call 0x1406baad0
0064477B  48 8B 1B                        mov rbx, qword ptr [rbx]
0064477E  48 3B DF                        cmp rbx, rdi
00644781  75 E2                           jne 0x140644765
00644783  40 84 F6                        test sil, sil
00644786  74 0C                           je 0x140644794
00644788  48 8D 0D F1 F6 8B 00            lea rcx, [rip + 0x8bf6f1]
0064478F  E8 EC 56 D0 FF                  call 0x140349e80
00644794  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00644798  4D 8B CF                        mov r9, r15
0064479B  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064479F  4D 8B C4                        mov r8, r12
006447A2  41 8B D5                        mov edx, r13d
006447A5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006447AA  E8 E1 AF 06 00                  call 0x1406af790
006447AF  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006447B2  4D 85 F6                        test r14, r14
006447B5  74 63                           je 0x14064481a
006447B7  40 32 FF                        xor dil, dil
006447BA  40 38 3D F7 00 8C 00            cmp byte ptr [rip + 0x8c00f7], dil
006447C1  75 0C                           jne 0x1406447cf
006447C3  F7 05 B3 01 8C 00 00 08 00 00   test dword ptr [rip + 0x8c01b3], 0x800
006447CD  74 13                           je 0x1406447e2
006447CF  48 8D 0D AA F6 8B 00            lea rcx, [rip + 0x8bf6aa]
006447D6  E8 45 1E BD FF                  call 0x140216620
006447DB  40 8A F8                        mov dil, al
006447DE  84 C0                           test al, al
006447E0  74 38                           je 0x14064481a
006447E2  49 8D 76 30                     lea rsi, [r14 + 0x30]
006447E6  48 8B 1E                        mov rbx, qword ptr [rsi]
006447E9  EB 19                           jmp 0x140644804
006447EB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006447EF  48 85 C0                        test rax, rax
006447F2  74 0D                           je 0x140644801
006447F4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006447F8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006447FC  E8 CF 62 07 00                  call 0x1406baad0
00644801  48 8B 1B                        mov rbx, qword ptr [rbx]
00644804  48 3B DE                        cmp rbx, rsi
00644807  75 E2                           jne 0x1406447eb
00644809  40 84 FF                        test dil, dil
0064480C  74 0C                           je 0x14064481a
0064480E  48 8D 0D 6B F6 8B 00            lea rcx, [rip + 0x8bf66b]
00644815  E8 66 56 D0 FF                  call 0x140349e80
0064481A  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0064481D  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00644822  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00644826  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064482A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064482E  49 8B E3                        mov rsp, r11
00644831  41 5F                           pop r15
00644833  41 5E                           pop r14
00644835  41 5D                           pop r13
00644837  41 5C                           pop r12
00644839  5D                              pop rbp
0064483A  C3                              ret
0064483B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenResourceManagerWrapper(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5)
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
    result = DifGetAPIThunkContextById(result + 76, a2, a3, a4);
    if (result == 0) goto loc_00644794;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00644707;
    v_stack_m68 = v_stack_p0;
    goto loc_00644715;
loc_00644707:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = a5;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    v_stack_m58 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9175445)) != 0) goto loc_00644749;
    if (((*(unsigned int *)(v_rip + 9175609)) & (0x800ULL)) == 0) goto loc_0064475C;
loc_00644749:
    result = ExAcquireRundownProtection(v_rip + 9172784, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00644794;
loc_0064475C:
    goto loc_0064477E;
loc_00644765:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064477E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00644765;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9172721;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwOpenResourceManager(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0064481A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9175287)) != 0) goto loc_006447CF;
    if (((*(unsigned int *)(v_rip + 9175475)) & (0x800ULL)) == 0) goto loc_006447E2;
loc_006447CF:
    result = ExAcquireRundownProtection(v_rip + 9172650, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064481A;
loc_006447E2:
    goto loc_00644804;
loc_006447EB:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00644804:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006447EB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9172587;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenResourceManagerWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
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
    result = DifGetAPIThunkContextById(result + 76, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00644794;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00644707;
    v_stack_m68 = v_stack_p0;
    goto loc_00644715;
loc_00644707:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = Arg5;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    v_stack_m58 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C0195)) != 0) goto loc_00644749;
    if (((*(uint32_t *)(v_rip + 0x8C0239)) & (0x800ULL)) == 0) goto loc_0064475C;
loc_00644749:
    result = ExAcquireRundownProtection(v_rip + 9172784, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00644794;
loc_0064475C:
    goto loc_0064477E;
loc_00644765:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064477E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00644765;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9172721;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwOpenResourceManager(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0064481A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C00F7)) != 0) goto loc_006447CF;
    if (((*(uint32_t *)(v_rip + 0x8C01B3)) & (0x800ULL)) == 0) goto loc_006447E2;
loc_006447CF:
    result = ExAcquireRundownProtection(v_rip + 9172650, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0064481A;
loc_006447E2:
    goto loc_00644804;
loc_006447EB:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_00644804:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006447EB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9172587;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006446A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006446A0[BB_006446A0]
  bb_006446F5[BB_006446F5]
  bb_006446FD[BB_006446FD]
  bb_00644707[BB_00644707]
  bb_0064470C[BB_0064470C]
  bb_00644715[BB_00644715]
  bb_0064473D[BB_0064473D]
  bb_00644749[BB_00644749]
  bb_0064475C[BB_0064475C]
  bb_00644765[BB_00644765]
  bb_0064476E[BB_0064476E]
  bb_0064477B[BB_0064477B]
  bb_0064477E[BB_0064477E]
  bb_00644783[BB_00644783]
  bb_00644788[BB_00644788]
  bb_00644794[BB_00644794]
  bb_006447B7[BB_006447B7]
  bb_006447C3[BB_006447C3]
  bb_006447CF[BB_006447CF]
  bb_006447E2[BB_006447E2]
  bb_006447EB[BB_006447EB]
  bb_006447F4[BB_006447F4]
  bb_00644801[BB_00644801]
  bb_00644804[BB_00644804]
  bb_00644809[BB_00644809]
  bb_0064480E[BB_0064480E]
  bb_0064481A[BB_0064481A]
  bb_0064483B[BB_0064483B]
  bb_006446A0 -->|branch| bb_00644794
  bb_006446A0 -->|fallthrough| bb_006446F5
  bb_006446F5 -->|branch| bb_00644707
  bb_006446F5 -->|fallthrough| bb_006446FD
  bb_006446FD -->|branch| bb_00644715
  bb_00644707 -->|branch| bb_00644715
  bb_00644707 -->|fallthrough| bb_0064470C
  bb_0064470C -->|flow| bb_00644715
  bb_00644715 -->|branch| bb_00644749
  bb_00644715 -->|fallthrough| bb_0064473D
  bb_0064473D -->|branch| bb_0064475C
  bb_0064473D -->|fallthrough| bb_00644749
  bb_00644749 -->|branch| bb_00644794
  bb_00644749 -->|fallthrough| bb_0064475C
  bb_0064475C -->|branch| bb_0064477E
  bb_00644765 -->|branch| bb_0064477B
  bb_00644765 -->|fallthrough| bb_0064476E
  bb_0064476E -->|flow| bb_0064477B
  bb_0064477B -->|flow| bb_0064477E
  bb_0064477E -->|branch| bb_00644765
  bb_0064477E -->|fallthrough| bb_00644783
  bb_00644783 -->|branch| bb_00644794
  bb_00644783 -->|fallthrough| bb_00644788
  bb_00644788 -->|flow| bb_00644794
  bb_00644794 -->|branch| bb_0064481A
  bb_00644794 -->|fallthrough| bb_006447B7
  bb_006447B7 -->|branch| bb_006447CF
  bb_006447B7 -->|fallthrough| bb_006447C3
  bb_006447C3 -->|branch| bb_006447E2
  bb_006447C3 -->|fallthrough| bb_006447CF
  bb_006447CF -->|branch| bb_0064481A
  bb_006447CF -->|fallthrough| bb_006447E2
  bb_006447E2 -->|branch| bb_00644804
  bb_006447EB -->|branch| bb_00644801
  bb_006447EB -->|fallthrough| bb_006447F4
  bb_006447F4 -->|flow| bb_00644801
  bb_00644801 -->|flow| bb_00644804
  bb_00644804 -->|branch| bb_006447EB
  bb_00644804 -->|fallthrough| bb_00644809
  bb_00644809 -->|branch| bb_0064481A
  bb_00644809 -->|fallthrough| bb_0064480E
  bb_0064480E -->|flow| bb_0064481A
```
