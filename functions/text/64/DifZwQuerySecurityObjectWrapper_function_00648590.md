# DifZwQuerySecurityObjectWrapper

- RVA: `0x00648590`–`0x0064872C` (길이 `412` bytes)
- VA: `0x0000000140648590`
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
- `0x006485D4` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006485FC` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00648640` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00648666` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064867F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064869A` → [ZwQuerySecurityObject](../6A/ZwQuerySecurityObject_function_006AFDF0.md) (function, `0x006AFDF0`)
- `0x006486C6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006486EC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00648705` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064860C` → RVA `0x00F048B8` (`.data`; read)
- `0x0064862D` → RVA `0x00F04980` (`.data`; read)
- `0x00648639` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00648590  48 8B C4                        mov rax, rsp
00648593  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00648597  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064859B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064859F  48 89 48 08                     mov qword ptr [rax + 8], rcx
006485A3  55                              push rbp
006485A4  41 54                           push r12
006485A6  41 55                           push r13
006485A8  41 56                           push r14
006485AA  41 57                           push r15
006485AC  48 8B EC                        mov rbp, rsp
006485AF  48 83 EC 70                     sub rsp, 0x70
006485B3  33 C0                           xor eax, eax
006485B5  0F 57 C0                        xorps xmm0, xmm0
006485B8  45 8B F9                        mov r15d, r9d
006485BB  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006485BF  4D 8B E0                        mov r12, r8
006485C2  44 8B EA                        mov r13d, edx
006485C5  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
006485C9  8D 48 25                        lea ecx, [rax + 0x25]
006485CC  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006485D0  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006485D4  E8 5B D4 E4 FF                  call 0x140495a34
006485D9  4C 8B F0                        mov r14, rax
006485DC  48 85 C0                        test rax, rax
006485DF  0F 84 9F 00 00 00               je 0x140648684
006485E5  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
006485E8  F6 C1 18                        test cl, 0x18
006485EB  74 0A                           je 0x1406485f7
006485ED  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006485F1  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
006485F5  EB 0E                           jmp 0x140648605
006485F7  F6 C1 04                        test cl, 4
006485FA  74 09                           je 0x140648605
006485FC  E8 07 B6 E8 FF                  call 0x1404d3c08
00648601  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00648605  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00648609  40 32 F6                        xor sil, sil
0064860C  40 38 35 A5 C2 8B 00            cmp byte ptr [rip + 0x8bc2a5], sil
00648613  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00648617  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064861B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0064861F  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00648623  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00648627  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
0064862B  75 0C                           jne 0x140648639
0064862D  F7 05 49 C3 8B 00 00 08 00 00   test dword ptr [rip + 0x8bc349], 0x800
00648637  74 13                           je 0x14064864c
00648639  48 8D 0D 40 B8 8B 00            lea rcx, [rip + 0x8bb840]
00648640  E8 DB DF BC FF                  call 0x140216620
00648645  40 8A F0                        mov sil, al
00648648  84 C0                           test al, al
0064864A  74 38                           je 0x140648684
0064864C  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00648650  48 8B 1F                        mov rbx, qword ptr [rdi]
00648653  EB 19                           jmp 0x14064866e
00648655  48 8D 43 F0                     lea rax, [rbx - 0x10]
00648659  48 85 C0                        test rax, rax
0064865C  74 0D                           je 0x14064866b
0064865E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00648662  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00648666  E8 65 24 07 00                  call 0x1406baad0
0064866B  48 8B 1B                        mov rbx, qword ptr [rbx]
0064866E  48 3B DF                        cmp rbx, rdi
00648671  75 E2                           jne 0x140648655
00648673  40 84 F6                        test sil, sil
00648676  74 0C                           je 0x140648684
00648678  48 8D 0D 01 B8 8B 00            lea rcx, [rip + 0x8bb801]
0064867F  E8 FC 17 D0 FF                  call 0x140349e80
00648684  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00648688  45 8B CF                        mov r9d, r15d
0064868B  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064868F  4D 8B C4                        mov r8, r12
00648692  41 8B D5                        mov edx, r13d
00648695  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0064869A  E8 51 77 06 00                  call 0x1406afdf0
0064869F  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006486A2  4D 85 F6                        test r14, r14
006486A5  74 63                           je 0x14064870a
006486A7  40 32 FF                        xor dil, dil
006486AA  40 38 3D 07 C2 8B 00            cmp byte ptr [rip + 0x8bc207], dil
006486B1  75 0C                           jne 0x1406486bf
006486B3  F7 05 C3 C2 8B 00 00 08 00 00   test dword ptr [rip + 0x8bc2c3], 0x800
006486BD  74 13                           je 0x1406486d2
006486BF  48 8D 0D BA B7 8B 00            lea rcx, [rip + 0x8bb7ba]
006486C6  E8 55 DF BC FF                  call 0x140216620
006486CB  40 8A F8                        mov dil, al
006486CE  84 C0                           test al, al
006486D0  74 38                           je 0x14064870a
006486D2  49 8D 76 30                     lea rsi, [r14 + 0x30]
006486D6  48 8B 1E                        mov rbx, qword ptr [rsi]
006486D9  EB 19                           jmp 0x1406486f4
006486DB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006486DF  48 85 C0                        test rax, rax
006486E2  74 0D                           je 0x1406486f1
006486E4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006486E8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006486EC  E8 DF 23 07 00                  call 0x1406baad0
006486F1  48 8B 1B                        mov rbx, qword ptr [rbx]
006486F4  48 3B DE                        cmp rbx, rsi
006486F7  75 E2                           jne 0x1406486db
006486F9  40 84 FF                        test dil, dil
006486FC  74 0C                           je 0x14064870a
006486FE  48 8D 0D 7B B7 8B 00            lea rcx, [rip + 0x8bb77b]
00648705  E8 76 17 D0 FF                  call 0x140349e80
0064870A  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0064870D  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00648712  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00648716  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064871A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064871E  49 8B E3                        mov rsp, r11
00648721  41 5F                           pop r15
00648723  41 5E                           pop r14
00648725  41 5D                           pop r13
00648727  41 5C                           pop r12
00648729  5D                              pop rbp
0064872A  C3                              ret
0064872B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQuerySecurityObjectWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
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
    result = DifGetAPIThunkContextById(result + 37, a2, a3, a4);
    if (result == 0) goto loc_00648684;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006485F7;
    v_stack_m68 = v_stack_p0;
    goto loc_00648605;
loc_006485F7:
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
    if ((*(unsigned __int8 *)(v_rip + 9159333)) != 0) goto loc_00648639;
    if (((*(unsigned int *)(v_rip + 9159497)) & (0x800ULL)) == 0) goto loc_0064864C;
loc_00648639:
    result = ExAcquireRundownProtection(v_rip + 9156672, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00648684;
loc_0064864C:
    goto loc_0064866E;
loc_00648655:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064866E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00648655;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9156609;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwQuerySecurityObject(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0064870A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9159175)) != 0) goto loc_006486BF;
    if (((*(unsigned int *)(v_rip + 9159363)) & (0x800ULL)) == 0) goto loc_006486D2;
loc_006486BF:
    result = ExAcquireRundownProtection(v_rip + 9156538, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0064870A;
loc_006486D2:
    goto loc_006486F4;
loc_006486DB:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_006486F4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006486DB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9156475;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQuerySecurityObjectWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
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
    result = DifGetAPIThunkContextById(result + 37, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00648684;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006485F7;
    v_stack_m68 = v_stack_p0;
    goto loc_00648605;
loc_006485F7:
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
    if ((*(uint8_t *)(v_rip + 0x8BC2A5)) != 0) goto loc_00648639;
    if (((*(uint32_t *)(v_rip + 0x8BC349)) & (0x800ULL)) == 0) goto loc_0064864C;
loc_00648639:
    result = ExAcquireRundownProtection(v_rip + 9156672, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00648684;
loc_0064864C:
    goto loc_0064866E;
loc_00648655:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064866E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00648655;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9156609;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwQuerySecurityObject(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0064870A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BC207)) != 0) goto loc_006486BF;
    if (((*(uint32_t *)(v_rip + 0x8BC2C3)) & (0x800ULL)) == 0) goto loc_006486D2;
loc_006486BF:
    result = ExAcquireRundownProtection(v_rip + 9156538, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0064870A;
loc_006486D2:
    goto loc_006486F4;
loc_006486DB:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_006486F4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006486DB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9156475;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00648590&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00648590[BB_00648590]
  bb_006485E5[BB_006485E5]
  bb_006485ED[BB_006485ED]
  bb_006485F7[BB_006485F7]
  bb_006485FC[BB_006485FC]
  bb_00648605[BB_00648605]
  bb_0064862D[BB_0064862D]
  bb_00648639[BB_00648639]
  bb_0064864C[BB_0064864C]
  bb_00648655[BB_00648655]
  bb_0064865E[BB_0064865E]
  bb_0064866B[BB_0064866B]
  bb_0064866E[BB_0064866E]
  bb_00648673[BB_00648673]
  bb_00648678[BB_00648678]
  bb_00648684[BB_00648684]
  bb_006486A7[BB_006486A7]
  bb_006486B3[BB_006486B3]
  bb_006486BF[BB_006486BF]
  bb_006486D2[BB_006486D2]
  bb_006486DB[BB_006486DB]
  bb_006486E4[BB_006486E4]
  bb_006486F1[BB_006486F1]
  bb_006486F4[BB_006486F4]
  bb_006486F9[BB_006486F9]
  bb_006486FE[BB_006486FE]
  bb_0064870A[BB_0064870A]
  bb_0064872B[BB_0064872B]
  bb_00648590 -->|branch| bb_00648684
  bb_00648590 -->|fallthrough| bb_006485E5
  bb_006485E5 -->|branch| bb_006485F7
  bb_006485E5 -->|fallthrough| bb_006485ED
  bb_006485ED -->|branch| bb_00648605
  bb_006485F7 -->|branch| bb_00648605
  bb_006485F7 -->|fallthrough| bb_006485FC
  bb_006485FC -->|flow| bb_00648605
  bb_00648605 -->|branch| bb_00648639
  bb_00648605 -->|fallthrough| bb_0064862D
  bb_0064862D -->|branch| bb_0064864C
  bb_0064862D -->|fallthrough| bb_00648639
  bb_00648639 -->|branch| bb_00648684
  bb_00648639 -->|fallthrough| bb_0064864C
  bb_0064864C -->|branch| bb_0064866E
  bb_00648655 -->|branch| bb_0064866B
  bb_00648655 -->|fallthrough| bb_0064865E
  bb_0064865E -->|flow| bb_0064866B
  bb_0064866B -->|flow| bb_0064866E
  bb_0064866E -->|branch| bb_00648655
  bb_0064866E -->|fallthrough| bb_00648673
  bb_00648673 -->|branch| bb_00648684
  bb_00648673 -->|fallthrough| bb_00648678
  bb_00648678 -->|flow| bb_00648684
  bb_00648684 -->|branch| bb_0064870A
  bb_00648684 -->|fallthrough| bb_006486A7
  bb_006486A7 -->|branch| bb_006486BF
  bb_006486A7 -->|fallthrough| bb_006486B3
  bb_006486B3 -->|branch| bb_006486D2
  bb_006486B3 -->|fallthrough| bb_006486BF
  bb_006486BF -->|branch| bb_0064870A
  bb_006486BF -->|fallthrough| bb_006486D2
  bb_006486D2 -->|branch| bb_006486F4
  bb_006486DB -->|branch| bb_006486F1
  bb_006486DB -->|fallthrough| bb_006486E4
  bb_006486E4 -->|flow| bb_006486F1
  bb_006486F1 -->|flow| bb_006486F4
  bb_006486F4 -->|branch| bb_006486DB
  bb_006486F4 -->|fallthrough| bb_006486F9
  bb_006486F9 -->|branch| bb_0064870A
  bb_006486F9 -->|fallthrough| bb_006486FE
  bb_006486FE -->|flow| bb_0064870A
```
