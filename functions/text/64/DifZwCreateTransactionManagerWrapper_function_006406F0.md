# DifZwCreateTransactionManagerWrapper

- RVA: `0x006406F0`–`0x00640895` (길이 `421` bytes)
- VA: `0x00000001406406F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `122`개 명령, `421/421` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00640734` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064075C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006407A4` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006407CA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006407E3` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00640803` → [ZwCreateTransactionManager](../6A/ZwCreateTransactionManager_function_006AEAD0.md) (function, `0x006AEAD0`)
- `0x0064082F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00640855` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064086E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064076C` → RVA `0x00F048B8` (`.data`; read)
- `0x00640791` → RVA `0x00F04980` (`.data`; read)
- `0x0064079D` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006406F0  48 8B C4                        mov rax, rsp
006406F3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006406F7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006406FB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006406FF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00640703  55                              push rbp
00640704  41 54                           push r12
00640706  41 55                           push r13
00640708  41 56                           push r14
0064070A  41 57                           push r15
0064070C  48 8B EC                        mov rbp, rsp
0064070F  48 83 EC 70                     sub rsp, 0x70
00640713  33 C0                           xor eax, eax
00640715  0F 57 C0                        xorps xmm0, xmm0
00640718  4D 8B F9                        mov r15, r9
0064071B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064071F  4D 8B E0                        mov r12, r8
00640722  44 8B EA                        mov r13d, edx
00640725  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00640729  8D 48 73                        lea ecx, [rax + 0x73]
0064072C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00640730  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00640734  E8 FB 52 E5 FF                  call 0x140495a34
00640739  4C 8B F0                        mov r14, rax
0064073C  48 85 C0                        test rax, rax
0064073F  0F 84 A3 00 00 00               je 0x1406407e8
00640745  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00640748  F6 C1 18                        test cl, 0x18
0064074B  74 0A                           je 0x140640757
0064074D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00640751  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00640755  EB 0E                           jmp 0x140640765
00640757  F6 C1 04                        test cl, 4
0064075A  74 09                           je 0x140640765
0064075C  E8 A7 34 E9 FF                  call 0x1404d3c08
00640761  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00640765  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00640769  40 32 F6                        xor sil, sil
0064076C  40 38 35 45 41 8C 00            cmp byte ptr [rip + 0x8c4145], sil
00640773  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00640777  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
0064077A  89 45 CC                        mov dword ptr [rbp - 0x34], eax
0064077D  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00640780  89 45 C8                        mov dword ptr [rbp - 0x38], eax
00640783  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00640787  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
0064078B  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
0064078F  75 0C                           jne 0x14064079d
00640791  F7 05 E5 41 8C 00 00 08 00 00   test dword ptr [rip + 0x8c41e5], 0x800
0064079B  74 13                           je 0x1406407b0
0064079D  48 8D 0D DC 36 8C 00            lea rcx, [rip + 0x8c36dc]
006407A4  E8 77 5E BD FF                  call 0x140216620
006407A9  40 8A F0                        mov sil, al
006407AC  84 C0                           test al, al
006407AE  74 38                           je 0x1406407e8
006407B0  49 8D 7E 20                     lea rdi, [r14 + 0x20]
006407B4  48 8B 1F                        mov rbx, qword ptr [rdi]
006407B7  EB 19                           jmp 0x1406407d2
006407B9  48 8D 43 F0                     lea rax, [rbx - 0x10]
006407BD  48 85 C0                        test rax, rax
006407C0  74 0D                           je 0x1406407cf
006407C2  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006407C6  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006407CA  E8 01 A3 07 00                  call 0x1406baad0
006407CF  48 8B 1B                        mov rbx, qword ptr [rbx]
006407D2  48 3B DF                        cmp rbx, rdi
006407D5  75 E2                           jne 0x1406407b9
006407D7  40 84 F6                        test sil, sil
006407DA  74 0C                           je 0x1406407e8
006407DC  48 8D 0D 9D 36 8C 00            lea rcx, [rip + 0x8c369d]
006407E3  E8 98 96 D0 FF                  call 0x140349e80
006407E8  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
006407EB  4D 8B CF                        mov r9, r15
006407EE  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006407F2  4D 8B C4                        mov r8, r12
006407F5  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
006407F9  41 8B D5                        mov edx, r13d
006407FC  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
006407FF  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00640803  E8 C8 E2 06 00                  call 0x1406aead0
00640808  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0064080B  4D 85 F6                        test r14, r14
0064080E  74 63                           je 0x140640873
00640810  40 32 FF                        xor dil, dil
00640813  40 38 3D 9E 40 8C 00            cmp byte ptr [rip + 0x8c409e], dil
0064081A  75 0C                           jne 0x140640828
0064081C  F7 05 5A 41 8C 00 00 08 00 00   test dword ptr [rip + 0x8c415a], 0x800
00640826  74 13                           je 0x14064083b
00640828  48 8D 0D 51 36 8C 00            lea rcx, [rip + 0x8c3651]
0064082F  E8 EC 5D BD FF                  call 0x140216620
00640834  40 8A F8                        mov dil, al
00640837  84 C0                           test al, al
00640839  74 38                           je 0x140640873
0064083B  49 8D 76 30                     lea rsi, [r14 + 0x30]
0064083F  48 8B 1E                        mov rbx, qword ptr [rsi]
00640842  EB 19                           jmp 0x14064085d
00640844  48 8D 43 F0                     lea rax, [rbx - 0x10]
00640848  48 85 C0                        test rax, rax
0064084B  74 0D                           je 0x14064085a
0064084D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00640851  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00640855  E8 76 A2 07 00                  call 0x1406baad0
0064085A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064085D  48 3B DE                        cmp rbx, rsi
00640860  75 E2                           jne 0x140640844
00640862  40 84 FF                        test dil, dil
00640865  74 0C                           je 0x140640873
00640867  48 8D 0D 12 36 8C 00            lea rcx, [rip + 0x8c3612]
0064086E  E8 0D 96 D0 FF                  call 0x140349e80
00640873  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00640876  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0064087B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064087F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00640883  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00640887  49 8B E3                        mov rsp, r11
0064088A  41 5F                           pop r15
0064088C  41 5E                           pop r14
0064088E  41 5D                           pop r13
00640890  41 5C                           pop r12
00640892  5D                              pop rbp
00640893  C3                              ret
00640894  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwCreateTransactionManagerWrapper(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
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
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m78;
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
    result = DifGetAPIThunkContextById(result + 115, a2, a3, a4);
    if (result == 0) goto loc_006407E8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00640757;
    v_stack_m68 = v_stack_p0;
    goto loc_00640765;
loc_00640757:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m5C = (unsigned int)((unsigned int)(a5));
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    v_stack_m58 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9191749)) != 0) goto loc_0064079D;
    if (((*(unsigned int *)(v_rip + 9191909)) & (0x800ULL)) == 0) goto loc_006407B0;
loc_0064079D:
    result = ExAcquireRundownProtection(v_rip + 9189084, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006407E8;
loc_006407B0:
    goto loc_006407D2;
loc_006407B9:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006407D2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006407B9;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9189021;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = (unsigned int)((unsigned int)(a6));
    v_stack_m78 = (unsigned int)((unsigned int)(a5));
    result = ZwCreateTransactionManager(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00640873;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9191582)) != 0) goto loc_00640828;
    if (((*(unsigned int *)(v_rip + 9191770)) & (0x800ULL)) == 0) goto loc_0064083B;
loc_00640828:
    result = ExAcquireRundownProtection(v_rip + 9188945, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00640873;
loc_0064083B:
    goto loc_0064085D;
loc_00640844:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0064085D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00640844;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9188882;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwCreateTransactionManagerWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
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
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m78;
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
    result = DifGetAPIThunkContextById(result + 115, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006407E8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00640757;
    v_stack_m68 = v_stack_p0;
    goto loc_00640765;
loc_00640757:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m5C = (uint32_t)((uint32_t)(Arg5));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    v_stack_m58 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C4145)) != 0) goto loc_0064079D;
    if (((*(uint32_t *)(v_rip + 0x8C41E5)) & (0x800ULL)) == 0) goto loc_006407B0;
loc_0064079D:
    result = ExAcquireRundownProtection(v_rip + 9189084, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006407E8;
loc_006407B0:
    goto loc_006407D2;
loc_006407B9:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006407D2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006407B9;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9189021;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m78 = (uint32_t)((uint32_t)(Arg5));
    result = ZwCreateTransactionManager(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00640873;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C409E)) != 0) goto loc_00640828;
    if (((*(uint32_t *)(v_rip + 0x8C415A)) & (0x800ULL)) == 0) goto loc_0064083B;
loc_00640828:
    result = ExAcquireRundownProtection(v_rip + 9188945, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00640873;
loc_0064083B:
    goto loc_0064085D;
loc_00640844:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_0064085D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00640844;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9188882;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006406F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006406F0[BB_006406F0]
  bb_00640745[BB_00640745]
  bb_0064074D[BB_0064074D]
  bb_00640757[BB_00640757]
  bb_0064075C[BB_0064075C]
  bb_00640765[BB_00640765]
  bb_00640791[BB_00640791]
  bb_0064079D[BB_0064079D]
  bb_006407B0[BB_006407B0]
  bb_006407B9[BB_006407B9]
  bb_006407C2[BB_006407C2]
  bb_006407CF[BB_006407CF]
  bb_006407D2[BB_006407D2]
  bb_006407D7[BB_006407D7]
  bb_006407DC[BB_006407DC]
  bb_006407E8[BB_006407E8]
  bb_00640810[BB_00640810]
  bb_0064081C[BB_0064081C]
  bb_00640828[BB_00640828]
  bb_0064083B[BB_0064083B]
  bb_00640844[BB_00640844]
  bb_0064084D[BB_0064084D]
  bb_0064085A[BB_0064085A]
  bb_0064085D[BB_0064085D]
  bb_00640862[BB_00640862]
  bb_00640867[BB_00640867]
  bb_00640873[BB_00640873]
  bb_00640894[BB_00640894]
  bb_006406F0 -->|branch| bb_006407E8
  bb_006406F0 -->|fallthrough| bb_00640745
  bb_00640745 -->|branch| bb_00640757
  bb_00640745 -->|fallthrough| bb_0064074D
  bb_0064074D -->|branch| bb_00640765
  bb_00640757 -->|branch| bb_00640765
  bb_00640757 -->|fallthrough| bb_0064075C
  bb_0064075C -->|flow| bb_00640765
  bb_00640765 -->|branch| bb_0064079D
  bb_00640765 -->|fallthrough| bb_00640791
  bb_00640791 -->|branch| bb_006407B0
  bb_00640791 -->|fallthrough| bb_0064079D
  bb_0064079D -->|branch| bb_006407E8
  bb_0064079D -->|fallthrough| bb_006407B0
  bb_006407B0 -->|branch| bb_006407D2
  bb_006407B9 -->|branch| bb_006407CF
  bb_006407B9 -->|fallthrough| bb_006407C2
  bb_006407C2 -->|flow| bb_006407CF
  bb_006407CF -->|flow| bb_006407D2
  bb_006407D2 -->|branch| bb_006407B9
  bb_006407D2 -->|fallthrough| bb_006407D7
  bb_006407D7 -->|branch| bb_006407E8
  bb_006407D7 -->|fallthrough| bb_006407DC
  bb_006407DC -->|flow| bb_006407E8
  bb_006407E8 -->|branch| bb_00640873
  bb_006407E8 -->|fallthrough| bb_00640810
  bb_00640810 -->|branch| bb_00640828
  bb_00640810 -->|fallthrough| bb_0064081C
  bb_0064081C -->|branch| bb_0064083B
  bb_0064081C -->|fallthrough| bb_00640828
  bb_00640828 -->|branch| bb_00640873
  bb_00640828 -->|fallthrough| bb_0064083B
  bb_0064083B -->|branch| bb_0064085D
  bb_00640844 -->|branch| bb_0064085A
  bb_00640844 -->|fallthrough| bb_0064084D
  bb_0064084D -->|flow| bb_0064085A
  bb_0064085A -->|flow| bb_0064085D
  bb_0064085D -->|branch| bb_00640844
  bb_0064085D -->|fallthrough| bb_00640862
  bb_00640862 -->|branch| bb_00640873
  bb_00640862 -->|fallthrough| bb_00640867
  bb_00640867 -->|flow| bb_00640873
```
