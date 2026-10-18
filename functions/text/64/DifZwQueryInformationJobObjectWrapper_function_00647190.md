# DifZwQueryInformationJobObjectWrapper

- RVA: `0x00647190`–`0x0064732C` (길이 `412` bytes)
- VA: `0x0000000140647190`
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
- `0x006471D4` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006471FC` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00647240` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647266` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064727F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064729A` → [ZwQueryInformationJobObject](../6A/ZwQueryInformationJobObject_function_006AFBB0.md) (function, `0x006AFBB0`)
- `0x006472C6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006472EC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00647305` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064720C` → RVA `0x00F048B8` (`.data`; read)
- `0x0064722D` → RVA `0x00F04980` (`.data`; read)
- `0x00647239` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00647190  48 8B C4                        mov rax, rsp
00647193  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00647197  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064719B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064719F  48 89 48 08                     mov qword ptr [rax + 8], rcx
006471A3  55                              push rbp
006471A4  41 54                           push r12
006471A6  41 55                           push r13
006471A8  41 56                           push r14
006471AA  41 57                           push r15
006471AC  48 8B EC                        mov rbp, rsp
006471AF  48 83 EC 70                     sub rsp, 0x70
006471B3  33 C0                           xor eax, eax
006471B5  0F 57 C0                        xorps xmm0, xmm0
006471B8  45 8B F9                        mov r15d, r9d
006471BB  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006471BF  4D 8B E0                        mov r12, r8
006471C2  44 8B EA                        mov r13d, edx
006471C5  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
006471C9  8D 48 31                        lea ecx, [rax + 0x31]
006471CC  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006471D0  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006471D4  E8 5B E8 E4 FF                  call 0x140495a34
006471D9  4C 8B F0                        mov r14, rax
006471DC  48 85 C0                        test rax, rax
006471DF  0F 84 9F 00 00 00               je 0x140647284
006471E5  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
006471E8  F6 C1 18                        test cl, 0x18
006471EB  74 0A                           je 0x1406471f7
006471ED  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006471F1  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
006471F5  EB 0E                           jmp 0x140647205
006471F7  F6 C1 04                        test cl, 4
006471FA  74 09                           je 0x140647205
006471FC  E8 07 CA E8 FF                  call 0x1404d3c08
00647201  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00647205  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00647209  40 32 F6                        xor sil, sil
0064720C  40 38 35 A5 D6 8B 00            cmp byte ptr [rip + 0x8bd6a5], sil
00647213  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00647217  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064721B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0064721F  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00647223  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00647227  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
0064722B  75 0C                           jne 0x140647239
0064722D  F7 05 49 D7 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd749], 0x800
00647237  74 13                           je 0x14064724c
00647239  48 8D 0D 40 CC 8B 00            lea rcx, [rip + 0x8bcc40]
00647240  E8 DB F3 BC FF                  call 0x140216620
00647245  40 8A F0                        mov sil, al
00647248  84 C0                           test al, al
0064724A  74 38                           je 0x140647284
0064724C  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00647250  48 8B 1F                        mov rbx, qword ptr [rdi]
00647253  EB 19                           jmp 0x14064726e
00647255  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647259  48 85 C0                        test rax, rax
0064725C  74 0D                           je 0x14064726b
0064725E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647262  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00647266  E8 65 38 07 00                  call 0x1406baad0
0064726B  48 8B 1B                        mov rbx, qword ptr [rbx]
0064726E  48 3B DF                        cmp rbx, rdi
00647271  75 E2                           jne 0x140647255
00647273  40 84 F6                        test sil, sil
00647276  74 0C                           je 0x140647284
00647278  48 8D 0D 01 CC 8B 00            lea rcx, [rip + 0x8bcc01]
0064727F  E8 FC 2B D0 FF                  call 0x140349e80
00647284  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00647288  45 8B CF                        mov r9d, r15d
0064728B  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064728F  4D 8B C4                        mov r8, r12
00647292  41 8B D5                        mov edx, r13d
00647295  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0064729A  E8 11 89 06 00                  call 0x1406afbb0
0064729F  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006472A2  4D 85 F6                        test r14, r14
006472A5  74 63                           je 0x14064730a
006472A7  40 32 FF                        xor dil, dil
006472AA  40 38 3D 07 D6 8B 00            cmp byte ptr [rip + 0x8bd607], dil
006472B1  75 0C                           jne 0x1406472bf
006472B3  F7 05 C3 D6 8B 00 00 08 00 00   test dword ptr [rip + 0x8bd6c3], 0x800
006472BD  74 13                           je 0x1406472d2
006472BF  48 8D 0D BA CB 8B 00            lea rcx, [rip + 0x8bcbba]
006472C6  E8 55 F3 BC FF                  call 0x140216620
006472CB  40 8A F8                        mov dil, al
006472CE  84 C0                           test al, al
006472D0  74 38                           je 0x14064730a
006472D2  49 8D 76 30                     lea rsi, [r14 + 0x30]
006472D6  48 8B 1E                        mov rbx, qword ptr [rsi]
006472D9  EB 19                           jmp 0x1406472f4
006472DB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006472DF  48 85 C0                        test rax, rax
006472E2  74 0D                           je 0x1406472f1
006472E4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006472E8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006472EC  E8 DF 37 07 00                  call 0x1406baad0
006472F1  48 8B 1B                        mov rbx, qword ptr [rbx]
006472F4  48 3B DE                        cmp rbx, rsi
006472F7  75 E2                           jne 0x1406472db
006472F9  40 84 FF                        test dil, dil
006472FC  74 0C                           je 0x14064730a
006472FE  48 8D 0D 7B CB 8B 00            lea rcx, [rip + 0x8bcb7b]
00647305  E8 76 2B D0 FF                  call 0x140349e80
0064730A  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0064730D  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00647312  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00647316  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064731A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064731E  49 8B E3                        mov rsp, r11
00647321  41 5F                           pop r15
00647323  41 5E                           pop r14
00647325  41 5D                           pop r13
00647327  41 5C                           pop r12
00647329  5D                              pop rbp
0064732A  C3                              ret
0064732B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryInformationJobObjectWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
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
    result = DifGetAPIThunkContextById(result + 49, a2, a3, a4);
    if (result == 0) goto loc_00647284;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006471F7;
    v_stack_m68 = v_stack_p0;
    goto loc_00647205;
loc_006471F7:
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
    if ((*(unsigned __int8 *)(v_rip + 9164453)) != 0) goto loc_00647239;
    if (((*(unsigned int *)(v_rip + 9164617)) & (0x800ULL)) == 0) goto loc_0064724C;
loc_00647239:
    result = ExAcquireRundownProtection(v_rip + 9161792, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00647284;
loc_0064724C:
    goto loc_0064726E;
loc_00647255:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064726E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00647255;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9161729;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwQueryInformationJobObject(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0064730A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9164295)) != 0) goto loc_006472BF;
    if (((*(unsigned int *)(v_rip + 9164483)) & (0x800ULL)) == 0) goto loc_006472D2;
loc_006472BF:
    result = ExAcquireRundownProtection(v_rip + 9161658, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0064730A;
loc_006472D2:
    goto loc_006472F4;
loc_006472DB:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_006472F4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006472DB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9161595;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryInformationJobObjectWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
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
    result = DifGetAPIThunkContextById(result + 49, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00647284;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006471F7;
    v_stack_m68 = v_stack_p0;
    goto loc_00647205;
loc_006471F7:
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
    if ((*(uint8_t *)(v_rip + 0x8BD6A5)) != 0) goto loc_00647239;
    if (((*(uint32_t *)(v_rip + 0x8BD749)) & (0x800ULL)) == 0) goto loc_0064724C;
loc_00647239:
    result = ExAcquireRundownProtection(v_rip + 9161792, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00647284;
loc_0064724C:
    goto loc_0064726E;
loc_00647255:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064726E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00647255;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9161729;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwQueryInformationJobObject(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0064730A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BD607)) != 0) goto loc_006472BF;
    if (((*(uint32_t *)(v_rip + 0x8BD6C3)) & (0x800ULL)) == 0) goto loc_006472D2;
loc_006472BF:
    result = ExAcquireRundownProtection(v_rip + 9161658, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0064730A;
loc_006472D2:
    goto loc_006472F4;
loc_006472DB:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_006472F4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006472DB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9161595;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00647190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00647190[BB_00647190]
  bb_006471E5[BB_006471E5]
  bb_006471ED[BB_006471ED]
  bb_006471F7[BB_006471F7]
  bb_006471FC[BB_006471FC]
  bb_00647205[BB_00647205]
  bb_0064722D[BB_0064722D]
  bb_00647239[BB_00647239]
  bb_0064724C[BB_0064724C]
  bb_00647255[BB_00647255]
  bb_0064725E[BB_0064725E]
  bb_0064726B[BB_0064726B]
  bb_0064726E[BB_0064726E]
  bb_00647273[BB_00647273]
  bb_00647278[BB_00647278]
  bb_00647284[BB_00647284]
  bb_006472A7[BB_006472A7]
  bb_006472B3[BB_006472B3]
  bb_006472BF[BB_006472BF]
  bb_006472D2[BB_006472D2]
  bb_006472DB[BB_006472DB]
  bb_006472E4[BB_006472E4]
  bb_006472F1[BB_006472F1]
  bb_006472F4[BB_006472F4]
  bb_006472F9[BB_006472F9]
  bb_006472FE[BB_006472FE]
  bb_0064730A[BB_0064730A]
  bb_0064732B[BB_0064732B]
  bb_00647190 -->|branch| bb_00647284
  bb_00647190 -->|fallthrough| bb_006471E5
  bb_006471E5 -->|branch| bb_006471F7
  bb_006471E5 -->|fallthrough| bb_006471ED
  bb_006471ED -->|branch| bb_00647205
  bb_006471F7 -->|branch| bb_00647205
  bb_006471F7 -->|fallthrough| bb_006471FC
  bb_006471FC -->|flow| bb_00647205
  bb_00647205 -->|branch| bb_00647239
  bb_00647205 -->|fallthrough| bb_0064722D
  bb_0064722D -->|branch| bb_0064724C
  bb_0064722D -->|fallthrough| bb_00647239
  bb_00647239 -->|branch| bb_00647284
  bb_00647239 -->|fallthrough| bb_0064724C
  bb_0064724C -->|branch| bb_0064726E
  bb_00647255 -->|branch| bb_0064726B
  bb_00647255 -->|fallthrough| bb_0064725E
  bb_0064725E -->|flow| bb_0064726B
  bb_0064726B -->|flow| bb_0064726E
  bb_0064726E -->|branch| bb_00647255
  bb_0064726E -->|fallthrough| bb_00647273
  bb_00647273 -->|branch| bb_00647284
  bb_00647273 -->|fallthrough| bb_00647278
  bb_00647278 -->|flow| bb_00647284
  bb_00647284 -->|branch| bb_0064730A
  bb_00647284 -->|fallthrough| bb_006472A7
  bb_006472A7 -->|branch| bb_006472BF
  bb_006472A7 -->|fallthrough| bb_006472B3
  bb_006472B3 -->|branch| bb_006472D2
  bb_006472B3 -->|fallthrough| bb_006472BF
  bb_006472BF -->|branch| bb_0064730A
  bb_006472BF -->|fallthrough| bb_006472D2
  bb_006472D2 -->|branch| bb_006472F4
  bb_006472DB -->|branch| bb_006472F1
  bb_006472DB -->|fallthrough| bb_006472E4
  bb_006472E4 -->|flow| bb_006472F1
  bb_006472F1 -->|flow| bb_006472F4
  bb_006472F4 -->|branch| bb_006472DB
  bb_006472F4 -->|fallthrough| bb_006472F9
  bb_006472F9 -->|branch| bb_0064730A
  bb_006472F9 -->|fallthrough| bb_006472FE
  bb_006472FE -->|flow| bb_0064730A
```
