# DifZwPowerInformationWrapper

- RVA: `0x006454F0`–`0x0064567E` (길이 `398` bytes)
- VA: `0x00000001406454F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2C24`
- 디코드: `116`개 명령, `398/398` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064552F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00645555` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00645595` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006455BB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006455D4` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006455EC` → [ZwPowerInformation](../6A/ZwPowerInformation_function_006ADCB0.md) (function, `0x006ADCB0`)
- `0x00645618` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064563E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645657` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00645564` → RVA `0x00F048B8` (`.data`; read)
- `0x00645582` → RVA `0x00F04980` (`.data`; read)
- `0x0064558E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006454F0  48 8B C4                        mov rax, rsp
006454F3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006454F7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006454FB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006454FF  89 48 08                        mov dword ptr [rax + 8], ecx
00645502  55                              push rbp
00645503  41 54                           push r12
00645505  41 55                           push r13
00645507  41 56                           push r14
00645509  41 57                           push r15
0064550B  48 8B EC                        mov rbp, rsp
0064550E  48 83 EC 60                     sub rsp, 0x60
00645512  0F 57 C0                        xorps xmm0, xmm0
00645515  B9 43 00 00 00                  mov ecx, 0x43
0064551A  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064551E  4D 8B F9                        mov r15, r9
00645521  45 8B E0                        mov r12d, r8d
00645524  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00645528  4C 8B EA                        mov r13, rdx
0064552B  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0064552F  E8 00 05 E5 FF                  call 0x140495a34
00645534  48 8B F0                        mov rsi, rax
00645537  48 85 C0                        test rax, rax
0064553A  0F 84 99 00 00 00               je 0x1406455d9
00645540  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00645543  A8 18                           test al, 0x18
00645545  74 0A                           je 0x140645551
00645547  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064554B  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0064554F  EB 0D                           jmp 0x14064555e
00645551  A8 04                           test al, 4
00645553  74 09                           je 0x14064555e
00645555  E8 AE E6 E8 FF                  call 0x1404d3c08
0064555A  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064555E  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
00645561  45 32 F6                        xor r14b, r14b
00645564  44 38 35 4D F3 8B 00            cmp byte ptr [rip + 0x8bf34d], r14b
0064556B  89 45 F8                        mov dword ptr [rbp - 8], eax
0064556E  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00645571  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00645574  4C 89 6D F0                     mov qword ptr [rbp - 0x10], r13
00645578  44 89 65 E8                     mov dword ptr [rbp - 0x18], r12d
0064557C  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
00645580  75 0C                           jne 0x14064558e
00645582  F7 05 F4 F3 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf3f4], 0x800
0064558C  74 13                           je 0x1406455a1
0064558E  48 8D 0D EB E8 8B 00            lea rcx, [rip + 0x8be8eb]
00645595  E8 86 10 BD FF                  call 0x140216620
0064559A  44 8A F0                        mov r14b, al
0064559D  84 C0                           test al, al
0064559F  74 38                           je 0x1406455d9
006455A1  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006455A5  48 8B 1F                        mov rbx, qword ptr [rdi]
006455A8  EB 19                           jmp 0x1406455c3
006455AA  48 8D 43 F0                     lea rax, [rbx - 0x10]
006455AE  48 85 C0                        test rax, rax
006455B1  74 0D                           je 0x1406455c0
006455B3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006455B7  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006455BB  E8 10 55 07 00                  call 0x1406baad0
006455C0  48 8B 1B                        mov rbx, qword ptr [rbx]
006455C3  48 3B DF                        cmp rbx, rdi
006455C6  75 E2                           jne 0x1406455aa
006455C8  45 84 F6                        test r14b, r14b
006455CB  74 0C                           je 0x1406455d9
006455CD  48 8D 0D AC E8 8B 00            lea rcx, [rip + 0x8be8ac]
006455D4  E8 A7 48 D0 FF                  call 0x140349e80
006455D9  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
006455DC  4D 8B CF                        mov r9, r15
006455DF  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
006455E2  45 8B C4                        mov r8d, r12d
006455E5  49 8B D5                        mov rdx, r13
006455E8  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
006455EC  E8 BF 86 06 00                  call 0x1406adcb0
006455F1  89 45 FC                        mov dword ptr [rbp - 4], eax
006455F4  48 85 F6                        test rsi, rsi
006455F7  74 63                           je 0x14064565c
006455F9  40 32 FF                        xor dil, dil
006455FC  40 38 3D B5 F2 8B 00            cmp byte ptr [rip + 0x8bf2b5], dil
00645603  75 0C                           jne 0x140645611
00645605  F7 05 71 F3 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf371], 0x800
0064560F  74 13                           je 0x140645624
00645611  48 8D 0D 68 E8 8B 00            lea rcx, [rip + 0x8be868]
00645618  E8 03 10 BD FF                  call 0x140216620
0064561D  40 8A F8                        mov dil, al
00645620  84 C0                           test al, al
00645622  74 38                           je 0x14064565c
00645624  48 83 C6 30                     add rsi, 0x30
00645628  48 8B 1E                        mov rbx, qword ptr [rsi]
0064562B  EB 19                           jmp 0x140645646
0064562D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00645631  48 85 C0                        test rax, rax
00645634  74 0D                           je 0x140645643
00645636  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064563A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064563E  E8 8D 54 07 00                  call 0x1406baad0
00645643  48 8B 1B                        mov rbx, qword ptr [rbx]
00645646  48 3B DE                        cmp rbx, rsi
00645649  75 E2                           jne 0x14064562d
0064564B  40 84 FF                        test dil, dil
0064564E  74 0C                           je 0x14064565c
00645650  48 8D 0D 29 E8 8B 00            lea rcx, [rip + 0x8be829]
00645657  E8 24 48 D0 FF                  call 0x140349e80
0064565C  8B 45 FC                        mov eax, dword ptr [rbp - 4]
0064565F  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00645664  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00645668  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064566C  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00645670  49 8B E3                        mov rsp, r11
00645673  41 5F                           pop r15
00645675  41 5E                           pop r14
00645677  41 5D                           pop r13
00645679  41 5C                           pop r12
0064567B  5D                              pop rbp
0064567C  C3                              ret
0064567D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwPowerInformationWrapper(int a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(67, a2, a3, a4);
    if (result == 0) goto loc_006455D9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00645551;
    v_stack_m58 = v_stack_p0;
    goto loc_0064555E;
loc_00645551:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m30 = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_m50 = (unsigned int)((unsigned int)(a5));
    v_stack_m38 = a2;
    v_stack_m40 = (unsigned int)((unsigned int)(a3));
    v_stack_m48 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9171789)) != 0) goto loc_0064558E;
    if (((*(unsigned int *)(v_rip + 9171956)) & (0x800ULL)) == 0) goto loc_006455A1;
loc_0064558E:
    result = ExAcquireRundownProtection(v_rip + 9169131, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006455D9;
loc_006455A1:
    goto loc_006455C3;
loc_006455AA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006455C3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006455AA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9169068;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = ZwPowerInformation((unsigned int)(v_stack_p8), a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m2C = (unsigned int)(result);
    if (result == 0) goto loc_0064565C;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9171637)) != 0) goto loc_00645611;
    if (((*(unsigned int *)(v_rip + 9171825)) & (0x800ULL)) == 0) goto loc_00645624;
loc_00645611:
    result = ExAcquireRundownProtection(v_rip + 9169000, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064565C;
loc_00645624:
    v_rsi = (result) + (48);
    goto loc_00645646;
loc_0064562D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_00645646:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064562D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9168937;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m2C);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwPowerInformationWrapper(int32_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_p0;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(67, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006455D9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00645551;
    v_stack_m58 = v_stack_p0;
    goto loc_0064555E;
loc_00645551:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m30 = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_m50 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m38 = Arg2;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m48 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8BF34D)) != 0) goto loc_0064558E;
    if (((*(uint32_t *)(v_rip + 0x8BF3F4)) & (0x800ULL)) == 0) goto loc_006455A1;
loc_0064558E:
    result = ExAcquireRundownProtection(v_rip + 9169131, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006455D9;
loc_006455A1:
    goto loc_006455C3;
loc_006455AA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006455C3:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006455AA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9169068;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = ZwPowerInformation((uint32_t)(v_stack_p8), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m2C = (uint32_t)(result);
    if (result == 0) goto loc_0064565C;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BF2B5)) != 0) goto loc_00645611;
    if (((*(uint32_t *)(v_rip + 0x8BF371)) & (0x800ULL)) == 0) goto loc_00645624;
loc_00645611:
    result = ExAcquireRundownProtection(v_rip + 9169000, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0064565C;
loc_00645624:
    local_rsi = (result) + (48);
    goto loc_00645646;
loc_0064562D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_00645646:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064562D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9168937;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m2C);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006454F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006454F0[BB_006454F0]
  bb_00645540[BB_00645540]
  bb_00645547[BB_00645547]
  bb_00645551[BB_00645551]
  bb_00645555[BB_00645555]
  bb_0064555E[BB_0064555E]
  bb_00645582[BB_00645582]
  bb_0064558E[BB_0064558E]
  bb_006455A1[BB_006455A1]
  bb_006455AA[BB_006455AA]
  bb_006455B3[BB_006455B3]
  bb_006455C0[BB_006455C0]
  bb_006455C3[BB_006455C3]
  bb_006455C8[BB_006455C8]
  bb_006455CD[BB_006455CD]
  bb_006455D9[BB_006455D9]
  bb_006455F9[BB_006455F9]
  bb_00645605[BB_00645605]
  bb_00645611[BB_00645611]
  bb_00645624[BB_00645624]
  bb_0064562D[BB_0064562D]
  bb_00645636[BB_00645636]
  bb_00645643[BB_00645643]
  bb_00645646[BB_00645646]
  bb_0064564B[BB_0064564B]
  bb_00645650[BB_00645650]
  bb_0064565C[BB_0064565C]
  bb_0064567D[BB_0064567D]
  bb_006454F0 -->|branch| bb_006455D9
  bb_006454F0 -->|fallthrough| bb_00645540
  bb_00645540 -->|branch| bb_00645551
  bb_00645540 -->|fallthrough| bb_00645547
  bb_00645547 -->|branch| bb_0064555E
  bb_00645551 -->|branch| bb_0064555E
  bb_00645551 -->|fallthrough| bb_00645555
  bb_00645555 -->|flow| bb_0064555E
  bb_0064555E -->|branch| bb_0064558E
  bb_0064555E -->|fallthrough| bb_00645582
  bb_00645582 -->|branch| bb_006455A1
  bb_00645582 -->|fallthrough| bb_0064558E
  bb_0064558E -->|branch| bb_006455D9
  bb_0064558E -->|fallthrough| bb_006455A1
  bb_006455A1 -->|branch| bb_006455C3
  bb_006455AA -->|branch| bb_006455C0
  bb_006455AA -->|fallthrough| bb_006455B3
  bb_006455B3 -->|flow| bb_006455C0
  bb_006455C0 -->|flow| bb_006455C3
  bb_006455C3 -->|branch| bb_006455AA
  bb_006455C3 -->|fallthrough| bb_006455C8
  bb_006455C8 -->|branch| bb_006455D9
  bb_006455C8 -->|fallthrough| bb_006455CD
  bb_006455CD -->|flow| bb_006455D9
  bb_006455D9 -->|branch| bb_0064565C
  bb_006455D9 -->|fallthrough| bb_006455F9
  bb_006455F9 -->|branch| bb_00645611
  bb_006455F9 -->|fallthrough| bb_00645605
  bb_00645605 -->|branch| bb_00645624
  bb_00645605 -->|fallthrough| bb_00645611
  bb_00645611 -->|branch| bb_0064565C
  bb_00645611 -->|fallthrough| bb_00645624
  bb_00645624 -->|branch| bb_00645646
  bb_0064562D -->|branch| bb_00645643
  bb_0064562D -->|fallthrough| bb_00645636
  bb_00645636 -->|flow| bb_00645643
  bb_00645643 -->|flow| bb_00645646
  bb_00645646 -->|branch| bb_0064562D
  bb_00645646 -->|fallthrough| bb_0064564B
  bb_0064564B -->|branch| bb_0064565C
  bb_0064564B -->|fallthrough| bb_00645650
  bb_00645650 -->|flow| bb_0064565C
```
