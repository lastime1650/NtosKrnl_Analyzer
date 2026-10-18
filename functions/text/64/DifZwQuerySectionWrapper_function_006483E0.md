# DifZwQuerySectionWrapper

- RVA: `0x006483E0`–`0x0064857C` (길이 `412` bytes)
- VA: `0x00000001406483E0`
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
- `0x00648424` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064844C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00648490` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006484B6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006484CF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006484EA` → [ZwQuerySection](../6A/ZwQuerySection_function_006ADAF0.md) (function, `0x006ADAF0`)
- `0x00648516` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064853C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00648555` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064845C` → RVA `0x00F048B8` (`.data`; read)
- `0x0064847D` → RVA `0x00F04980` (`.data`; read)
- `0x00648489` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006483E0  48 8B C4                        mov rax, rsp
006483E3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006483E7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006483EB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006483EF  48 89 48 08                     mov qword ptr [rax + 8], rcx
006483F3  55                              push rbp
006483F4  41 54                           push r12
006483F6  41 55                           push r13
006483F8  41 56                           push r14
006483FA  41 57                           push r15
006483FC  48 8B EC                        mov rbp, rsp
006483FF  48 83 EC 70                     sub rsp, 0x70
00648403  33 C0                           xor eax, eax
00648405  0F 57 C0                        xorps xmm0, xmm0
00648408  4D 8B F9                        mov r15, r9
0064840B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064840F  4D 8B E0                        mov r12, r8
00648412  44 8B EA                        mov r13d, edx
00648415  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00648419  8D 48 26                        lea ecx, [rax + 0x26]
0064841C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00648420  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00648424  E8 0B D6 E4 FF                  call 0x140495a34
00648429  4C 8B F0                        mov r14, rax
0064842C  48 85 C0                        test rax, rax
0064842F  0F 84 9F 00 00 00               je 0x1406484d4
00648435  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00648438  F6 C1 18                        test cl, 0x18
0064843B  74 0A                           je 0x140648447
0064843D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00648441  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00648445  EB 0E                           jmp 0x140648455
00648447  F6 C1 04                        test cl, 4
0064844A  74 09                           je 0x140648455
0064844C  E8 B7 B7 E8 FF                  call 0x1404d3c08
00648451  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00648455  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00648459  40 32 F6                        xor sil, sil
0064845C  40 38 35 55 C4 8B 00            cmp byte ptr [rip + 0x8bc455], sil
00648463  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00648467  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064846B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0064846F  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00648473  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00648477  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
0064847B  75 0C                           jne 0x140648489
0064847D  F7 05 F9 C4 8B 00 00 08 00 00   test dword ptr [rip + 0x8bc4f9], 0x800
00648487  74 13                           je 0x14064849c
00648489  48 8D 0D F0 B9 8B 00            lea rcx, [rip + 0x8bb9f0]
00648490  E8 8B E1 BC FF                  call 0x140216620
00648495  40 8A F0                        mov sil, al
00648498  84 C0                           test al, al
0064849A  74 38                           je 0x1406484d4
0064849C  49 8D 7E 20                     lea rdi, [r14 + 0x20]
006484A0  48 8B 1F                        mov rbx, qword ptr [rdi]
006484A3  EB 19                           jmp 0x1406484be
006484A5  48 8D 43 F0                     lea rax, [rbx - 0x10]
006484A9  48 85 C0                        test rax, rax
006484AC  74 0D                           je 0x1406484bb
006484AE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006484B2  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006484B6  E8 15 26 07 00                  call 0x1406baad0
006484BB  48 8B 1B                        mov rbx, qword ptr [rbx]
006484BE  48 3B DF                        cmp rbx, rdi
006484C1  75 E2                           jne 0x1406484a5
006484C3  40 84 F6                        test sil, sil
006484C6  74 0C                           je 0x1406484d4
006484C8  48 8D 0D B1 B9 8B 00            lea rcx, [rip + 0x8bb9b1]
006484CF  E8 AC 19 D0 FF                  call 0x140349e80
006484D4  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
006484D8  4D 8B CF                        mov r9, r15
006484DB  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006484DF  4D 8B C4                        mov r8, r12
006484E2  41 8B D5                        mov edx, r13d
006484E5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006484EA  E8 01 56 06 00                  call 0x1406adaf0
006484EF  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006484F2  4D 85 F6                        test r14, r14
006484F5  74 63                           je 0x14064855a
006484F7  40 32 FF                        xor dil, dil
006484FA  40 38 3D B7 C3 8B 00            cmp byte ptr [rip + 0x8bc3b7], dil
00648501  75 0C                           jne 0x14064850f
00648503  F7 05 73 C4 8B 00 00 08 00 00   test dword ptr [rip + 0x8bc473], 0x800
0064850D  74 13                           je 0x140648522
0064850F  48 8D 0D 6A B9 8B 00            lea rcx, [rip + 0x8bb96a]
00648516  E8 05 E1 BC FF                  call 0x140216620
0064851B  40 8A F8                        mov dil, al
0064851E  84 C0                           test al, al
00648520  74 38                           je 0x14064855a
00648522  49 8D 76 30                     lea rsi, [r14 + 0x30]
00648526  48 8B 1E                        mov rbx, qword ptr [rsi]
00648529  EB 19                           jmp 0x140648544
0064852B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064852F  48 85 C0                        test rax, rax
00648532  74 0D                           je 0x140648541
00648534  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00648538  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0064853C  E8 8F 25 07 00                  call 0x1406baad0
00648541  48 8B 1B                        mov rbx, qword ptr [rbx]
00648544  48 3B DE                        cmp rbx, rsi
00648547  75 E2                           jne 0x14064852b
00648549  40 84 FF                        test dil, dil
0064854C  74 0C                           je 0x14064855a
0064854E  48 8D 0D 2B B9 8B 00            lea rcx, [rip + 0x8bb92b]
00648555  E8 26 19 D0 FF                  call 0x140349e80
0064855A  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0064855D  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00648562  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00648566  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064856A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064856E  49 8B E3                        mov rsp, r11
00648571  41 5F                           pop r15
00648573  41 5E                           pop r14
00648575  41 5D                           pop r13
00648577  41 5C                           pop r12
00648579  5D                              pop rbp
0064857A  C3                              ret
0064857B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQuerySectionWrapper(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5)
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
    result = DifGetAPIThunkContextById(result + 38, a2, a3, a4);
    if (result == 0) goto loc_006484D4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00648447;
    v_stack_m68 = v_stack_p0;
    goto loc_00648455;
loc_00648447:
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
    if ((*(unsigned __int8 *)(v_rip + 9159765)) != 0) goto loc_00648489;
    if (((*(unsigned int *)(v_rip + 9159929)) & (0x800ULL)) == 0) goto loc_0064849C;
loc_00648489:
    result = ExAcquireRundownProtection(v_rip + 9157104, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006484D4;
loc_0064849C:
    goto loc_006484BE;
loc_006484A5:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006484BE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006484A5;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9157041;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwQuerySection(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0064855A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9159607)) != 0) goto loc_0064850F;
    if (((*(unsigned int *)(v_rip + 9159795)) & (0x800ULL)) == 0) goto loc_00648522;
loc_0064850F:
    result = ExAcquireRundownProtection(v_rip + 9156970, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064855A;
loc_00648522:
    goto loc_00648544;
loc_0064852B:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00648544:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0064852B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9156907;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQuerySectionWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
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
    result = DifGetAPIThunkContextById(result + 38, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006484D4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00648447;
    v_stack_m68 = v_stack_p0;
    goto loc_00648455;
loc_00648447:
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
    if ((*(uint8_t *)(v_rip + 0x8BC455)) != 0) goto loc_00648489;
    if (((*(uint32_t *)(v_rip + 0x8BC4F9)) & (0x800ULL)) == 0) goto loc_0064849C;
loc_00648489:
    result = ExAcquireRundownProtection(v_rip + 9157104, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006484D4;
loc_0064849C:
    goto loc_006484BE;
loc_006484A5:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006484BE:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006484A5;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9157041;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwQuerySection(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0064855A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BC3B7)) != 0) goto loc_0064850F;
    if (((*(uint32_t *)(v_rip + 0x8BC473)) & (0x800ULL)) == 0) goto loc_00648522;
loc_0064850F:
    result = ExAcquireRundownProtection(v_rip + 9156970, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0064855A;
loc_00648522:
    goto loc_00648544;
loc_0064852B:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_00648544:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0064852B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9156907;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006483E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006483E0[BB_006483E0]
  bb_00648435[BB_00648435]
  bb_0064843D[BB_0064843D]
  bb_00648447[BB_00648447]
  bb_0064844C[BB_0064844C]
  bb_00648455[BB_00648455]
  bb_0064847D[BB_0064847D]
  bb_00648489[BB_00648489]
  bb_0064849C[BB_0064849C]
  bb_006484A5[BB_006484A5]
  bb_006484AE[BB_006484AE]
  bb_006484BB[BB_006484BB]
  bb_006484BE[BB_006484BE]
  bb_006484C3[BB_006484C3]
  bb_006484C8[BB_006484C8]
  bb_006484D4[BB_006484D4]
  bb_006484F7[BB_006484F7]
  bb_00648503[BB_00648503]
  bb_0064850F[BB_0064850F]
  bb_00648522[BB_00648522]
  bb_0064852B[BB_0064852B]
  bb_00648534[BB_00648534]
  bb_00648541[BB_00648541]
  bb_00648544[BB_00648544]
  bb_00648549[BB_00648549]
  bb_0064854E[BB_0064854E]
  bb_0064855A[BB_0064855A]
  bb_0064857B[BB_0064857B]
  bb_006483E0 -->|branch| bb_006484D4
  bb_006483E0 -->|fallthrough| bb_00648435
  bb_00648435 -->|branch| bb_00648447
  bb_00648435 -->|fallthrough| bb_0064843D
  bb_0064843D -->|branch| bb_00648455
  bb_00648447 -->|branch| bb_00648455
  bb_00648447 -->|fallthrough| bb_0064844C
  bb_0064844C -->|flow| bb_00648455
  bb_00648455 -->|branch| bb_00648489
  bb_00648455 -->|fallthrough| bb_0064847D
  bb_0064847D -->|branch| bb_0064849C
  bb_0064847D -->|fallthrough| bb_00648489
  bb_00648489 -->|branch| bb_006484D4
  bb_00648489 -->|fallthrough| bb_0064849C
  bb_0064849C -->|branch| bb_006484BE
  bb_006484A5 -->|branch| bb_006484BB
  bb_006484A5 -->|fallthrough| bb_006484AE
  bb_006484AE -->|flow| bb_006484BB
  bb_006484BB -->|flow| bb_006484BE
  bb_006484BE -->|branch| bb_006484A5
  bb_006484BE -->|fallthrough| bb_006484C3
  bb_006484C3 -->|branch| bb_006484D4
  bb_006484C3 -->|fallthrough| bb_006484C8
  bb_006484C8 -->|flow| bb_006484D4
  bb_006484D4 -->|branch| bb_0064855A
  bb_006484D4 -->|fallthrough| bb_006484F7
  bb_006484F7 -->|branch| bb_0064850F
  bb_006484F7 -->|fallthrough| bb_00648503
  bb_00648503 -->|branch| bb_00648522
  bb_00648503 -->|fallthrough| bb_0064850F
  bb_0064850F -->|branch| bb_0064855A
  bb_0064850F -->|fallthrough| bb_00648522
  bb_00648522 -->|branch| bb_00648544
  bb_0064852B -->|branch| bb_00648541
  bb_0064852B -->|fallthrough| bb_00648534
  bb_00648534 -->|flow| bb_00648541
  bb_00648541 -->|flow| bb_00648544
  bb_00648544 -->|branch| bb_0064852B
  bb_00648544 -->|fallthrough| bb_00648549
  bb_00648549 -->|branch| bb_0064855A
  bb_00648549 -->|fallthrough| bb_0064854E
  bb_0064854E -->|flow| bb_0064855A
```
