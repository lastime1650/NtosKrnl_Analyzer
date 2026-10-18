# DifZwQueryInformationTokenWrapper

- RVA: `0x00647850`–`0x006479EC` (길이 `412` bytes)
- VA: `0x0000000140647850`
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
- `0x00647894` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006478BC` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00647900` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647926` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064793F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064795A` → [ZwQueryInformationToken](../6A/ZwQueryInformationToken_function_006AD4F0.md) (function, `0x006AD4F0`)
- `0x00647986` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006479AC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006479C5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006478CC` → RVA `0x00F048B8` (`.data`; read)
- `0x006478ED` → RVA `0x00F04980` (`.data`; read)
- `0x006478F9` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00647850  48 8B C4                        mov rax, rsp
00647853  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00647857  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064785B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064785F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00647863  55                              push rbp
00647864  41 54                           push r12
00647866  41 55                           push r13
00647868  41 56                           push r14
0064786A  41 57                           push r15
0064786C  48 8B EC                        mov rbp, rsp
0064786F  48 83 EC 70                     sub rsp, 0x70
00647873  33 C0                           xor eax, eax
00647875  0F 57 C0                        xorps xmm0, xmm0
00647878  45 8B F9                        mov r15d, r9d
0064787B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064787F  4D 8B E0                        mov r12, r8
00647882  44 8B EA                        mov r13d, edx
00647885  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00647889  8D 48 2D                        lea ecx, [rax + 0x2d]
0064788C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00647890  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00647894  E8 9B E1 E4 FF                  call 0x140495a34
00647899  4C 8B F0                        mov r14, rax
0064789C  48 85 C0                        test rax, rax
0064789F  0F 84 9F 00 00 00               je 0x140647944
006478A5  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
006478A8  F6 C1 18                        test cl, 0x18
006478AB  74 0A                           je 0x1406478b7
006478AD  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006478B1  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
006478B5  EB 0E                           jmp 0x1406478c5
006478B7  F6 C1 04                        test cl, 4
006478BA  74 09                           je 0x1406478c5
006478BC  E8 47 C3 E8 FF                  call 0x1404d3c08
006478C1  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
006478C5  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
006478C9  40 32 F6                        xor sil, sil
006478CC  40 38 35 E5 CF 8B 00            cmp byte ptr [rip + 0x8bcfe5], sil
006478D3  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
006478D7  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
006478DB  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
006478DF  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
006478E3  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
006478E7  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
006478EB  75 0C                           jne 0x1406478f9
006478ED  F7 05 89 D0 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd089], 0x800
006478F7  74 13                           je 0x14064790c
006478F9  48 8D 0D 80 C5 8B 00            lea rcx, [rip + 0x8bc580]
00647900  E8 1B ED BC FF                  call 0x140216620
00647905  40 8A F0                        mov sil, al
00647908  84 C0                           test al, al
0064790A  74 38                           je 0x140647944
0064790C  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00647910  48 8B 1F                        mov rbx, qword ptr [rdi]
00647913  EB 19                           jmp 0x14064792e
00647915  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647919  48 85 C0                        test rax, rax
0064791C  74 0D                           je 0x14064792b
0064791E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647922  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00647926  E8 A5 31 07 00                  call 0x1406baad0
0064792B  48 8B 1B                        mov rbx, qword ptr [rbx]
0064792E  48 3B DF                        cmp rbx, rdi
00647931  75 E2                           jne 0x140647915
00647933  40 84 F6                        test sil, sil
00647936  74 0C                           je 0x140647944
00647938  48 8D 0D 41 C5 8B 00            lea rcx, [rip + 0x8bc541]
0064793F  E8 3C 25 D0 FF                  call 0x140349e80
00647944  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00647948  45 8B CF                        mov r9d, r15d
0064794B  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064794F  4D 8B C4                        mov r8, r12
00647952  41 8B D5                        mov edx, r13d
00647955  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0064795A  E8 91 5B 06 00                  call 0x1406ad4f0
0064795F  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00647962  4D 85 F6                        test r14, r14
00647965  74 63                           je 0x1406479ca
00647967  40 32 FF                        xor dil, dil
0064796A  40 38 3D 47 CF 8B 00            cmp byte ptr [rip + 0x8bcf47], dil
00647971  75 0C                           jne 0x14064797f
00647973  F7 05 03 D0 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd003], 0x800
0064797D  74 13                           je 0x140647992
0064797F  48 8D 0D FA C4 8B 00            lea rcx, [rip + 0x8bc4fa]
00647986  E8 95 EC BC FF                  call 0x140216620
0064798B  40 8A F8                        mov dil, al
0064798E  84 C0                           test al, al
00647990  74 38                           je 0x1406479ca
00647992  49 8D 76 30                     lea rsi, [r14 + 0x30]
00647996  48 8B 1E                        mov rbx, qword ptr [rsi]
00647999  EB 19                           jmp 0x1406479b4
0064799B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064799F  48 85 C0                        test rax, rax
006479A2  74 0D                           je 0x1406479b1
006479A4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006479A8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006479AC  E8 1F 31 07 00                  call 0x1406baad0
006479B1  48 8B 1B                        mov rbx, qword ptr [rbx]
006479B4  48 3B DE                        cmp rbx, rsi
006479B7  75 E2                           jne 0x14064799b
006479B9  40 84 FF                        test dil, dil
006479BC  74 0C                           je 0x1406479ca
006479BE  48 8D 0D BB C4 8B 00            lea rcx, [rip + 0x8bc4bb]
006479C5  E8 B6 24 D0 FF                  call 0x140349e80
006479CA  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
006479CD  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
006479D2  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
006479D6  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
006479DA  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
006479DE  49 8B E3                        mov rsp, r11
006479E1  41 5F                           pop r15
006479E3  41 5E                           pop r14
006479E5  41 5D                           pop r13
006479E7  41 5C                           pop r12
006479E9  5D                              pop rbp
006479EA  C3                              ret
006479EB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryInformationTokenWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
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
    result = DifGetAPIThunkContextById(result + 45, a2, a3, a4);
    if (result == 0) goto loc_00647944;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006478B7;
    v_stack_m68 = v_stack_p0;
    goto loc_006478C5;
loc_006478B7:
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
    if ((*(unsigned __int8 *)(v_rip + 9162725)) != 0) goto loc_006478F9;
    if (((*(unsigned int *)(v_rip + 9162889)) & (0x800ULL)) == 0) goto loc_0064790C;
loc_006478F9:
    result = ExAcquireRundownProtection(v_rip + 9160064, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00647944;
loc_0064790C:
    goto loc_0064792E;
loc_00647915:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064792E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00647915;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9160001;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwQueryInformationToken(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_006479CA;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9162567)) != 0) goto loc_0064797F;
    if (((*(unsigned int *)(v_rip + 9162755)) & (0x800ULL)) == 0) goto loc_00647992;
loc_0064797F:
    result = ExAcquireRundownProtection(v_rip + 9159930, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_006479CA;
loc_00647992:
    goto loc_006479B4;
loc_0064799B:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_006479B4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0064799B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9159867;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryInformationTokenWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
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
    result = DifGetAPIThunkContextById(result + 45, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00647944;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006478B7;
    v_stack_m68 = v_stack_p0;
    goto loc_006478C5;
loc_006478B7:
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
    if ((*(uint8_t *)(v_rip + 0x8BCFE5)) != 0) goto loc_006478F9;
    if (((*(uint32_t *)(v_rip + 0x8BD089)) & (0x800ULL)) == 0) goto loc_0064790C;
loc_006478F9:
    result = ExAcquireRundownProtection(v_rip + 9160064, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00647944;
loc_0064790C:
    goto loc_0064792E;
loc_00647915:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064792E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00647915;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9160001;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwQueryInformationToken(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_006479CA;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BCF47)) != 0) goto loc_0064797F;
    if (((*(uint32_t *)(v_rip + 0x8BD003)) & (0x800ULL)) == 0) goto loc_00647992;
loc_0064797F:
    result = ExAcquireRundownProtection(v_rip + 9159930, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_006479CA;
loc_00647992:
    goto loc_006479B4;
loc_0064799B:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_006479B4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0064799B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9159867;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00647850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00647850[BB_00647850]
  bb_006478A5[BB_006478A5]
  bb_006478AD[BB_006478AD]
  bb_006478B7[BB_006478B7]
  bb_006478BC[BB_006478BC]
  bb_006478C5[BB_006478C5]
  bb_006478ED[BB_006478ED]
  bb_006478F9[BB_006478F9]
  bb_0064790C[BB_0064790C]
  bb_00647915[BB_00647915]
  bb_0064791E[BB_0064791E]
  bb_0064792B[BB_0064792B]
  bb_0064792E[BB_0064792E]
  bb_00647933[BB_00647933]
  bb_00647938[BB_00647938]
  bb_00647944[BB_00647944]
  bb_00647967[BB_00647967]
  bb_00647973[BB_00647973]
  bb_0064797F[BB_0064797F]
  bb_00647992[BB_00647992]
  bb_0064799B[BB_0064799B]
  bb_006479A4[BB_006479A4]
  bb_006479B1[BB_006479B1]
  bb_006479B4[BB_006479B4]
  bb_006479B9[BB_006479B9]
  bb_006479BE[BB_006479BE]
  bb_006479CA[BB_006479CA]
  bb_006479EB[BB_006479EB]
  bb_00647850 -->|branch| bb_00647944
  bb_00647850 -->|fallthrough| bb_006478A5
  bb_006478A5 -->|branch| bb_006478B7
  bb_006478A5 -->|fallthrough| bb_006478AD
  bb_006478AD -->|branch| bb_006478C5
  bb_006478B7 -->|branch| bb_006478C5
  bb_006478B7 -->|fallthrough| bb_006478BC
  bb_006478BC -->|flow| bb_006478C5
  bb_006478C5 -->|branch| bb_006478F9
  bb_006478C5 -->|fallthrough| bb_006478ED
  bb_006478ED -->|branch| bb_0064790C
  bb_006478ED -->|fallthrough| bb_006478F9
  bb_006478F9 -->|branch| bb_00647944
  bb_006478F9 -->|fallthrough| bb_0064790C
  bb_0064790C -->|branch| bb_0064792E
  bb_00647915 -->|branch| bb_0064792B
  bb_00647915 -->|fallthrough| bb_0064791E
  bb_0064791E -->|flow| bb_0064792B
  bb_0064792B -->|flow| bb_0064792E
  bb_0064792E -->|branch| bb_00647915
  bb_0064792E -->|fallthrough| bb_00647933
  bb_00647933 -->|branch| bb_00647944
  bb_00647933 -->|fallthrough| bb_00647938
  bb_00647938 -->|flow| bb_00647944
  bb_00647944 -->|branch| bb_006479CA
  bb_00647944 -->|fallthrough| bb_00647967
  bb_00647967 -->|branch| bb_0064797F
  bb_00647967 -->|fallthrough| bb_00647973
  bb_00647973 -->|branch| bb_00647992
  bb_00647973 -->|fallthrough| bb_0064797F
  bb_0064797F -->|branch| bb_006479CA
  bb_0064797F -->|fallthrough| bb_00647992
  bb_00647992 -->|branch| bb_006479B4
  bb_0064799B -->|branch| bb_006479B1
  bb_0064799B -->|fallthrough| bb_006479A4
  bb_006479A4 -->|flow| bb_006479B1
  bb_006479B1 -->|flow| bb_006479B4
  bb_006479B4 -->|branch| bb_0064799B
  bb_006479B4 -->|fallthrough| bb_006479B9
  bb_006479B9 -->|branch| bb_006479CA
  bb_006479B9 -->|fallthrough| bb_006479BE
  bb_006479BE -->|flow| bb_006479CA
```
