# DifKeInsertQueueDpcWrapper

- RVA: `0x006303F0`–`0x00630567` (길이 `375` bytes)
- VA: `0x00000001406303F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063042E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00630454` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00630488` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006304AE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006304C7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006304D5` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x00630501` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00630527` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00630540` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00630464` → RVA `0x00F048B8` (`.data`; read)
- `0x00630475` → RVA `0x00F04980` (`.data`; read)
- `0x00630481` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006303F0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
006303F5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
006303FA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
006303FF  55                              push rbp
00630400  41 54                           push r12
00630402  41 55                           push r13
00630404  41 56                           push r14
00630406  41 57                           push r15
00630408  48 8B EC                        mov rbp, rsp
0063040B  48 83 EC 50                     sub rsp, 0x50
0063040F  0F 57 C0                        xorps xmm0, xmm0
00630412  33 C0                           xor eax, eax
00630414  4C 8B E9                        mov r13, rcx
00630417  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063041B  B9 13 01 00 00                  mov ecx, 0x113
00630420  4D 8B F8                        mov r15, r8
00630423  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00630427  4C 8B E2                        mov r12, rdx
0063042A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063042E  E8 01 56 E6 FF                  call 0x140495a34
00630433  48 8B F0                        mov rsi, rax
00630436  48 85 C0                        test rax, rax
00630439  0F 84 8D 00 00 00               je 0x1406304cc
0063043F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00630442  A8 18                           test al, 0x18
00630444  74 0A                           je 0x140630450
00630446  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063044A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063044E  EB 0D                           jmp 0x14063045d
00630450  A8 04                           test al, 4
00630452  74 09                           je 0x14063045d
00630454  E8 AF 37 EA FF                  call 0x1404d3c08
00630459  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063045D  45 32 F6                        xor r14b, r14b
00630460  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00630464  44 38 35 4D 44 8D 00            cmp byte ptr [rip + 0x8d444d], r14b
0063046B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063046F  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00630473  75 0C                           jne 0x140630481
00630475  F7 05 01 45 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4501], 0x800
0063047F  74 13                           je 0x140630494
00630481  48 8D 0D F8 39 8D 00            lea rcx, [rip + 0x8d39f8]
00630488  E8 93 61 BE FF                  call 0x140216620
0063048D  44 8A F0                        mov r14b, al
00630490  84 C0                           test al, al
00630492  74 38                           je 0x1406304cc
00630494  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00630498  48 8B 1F                        mov rbx, qword ptr [rdi]
0063049B  EB 19                           jmp 0x1406304b6
0063049D  48 8D 43 F0                     lea rax, [rbx - 0x10]
006304A1  48 85 C0                        test rax, rax
006304A4  74 0D                           je 0x1406304b3
006304A6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006304AA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006304AE  E8 1D A6 08 00                  call 0x1406baad0
006304B3  48 8B 1B                        mov rbx, qword ptr [rbx]
006304B6  48 3B DF                        cmp rbx, rdi
006304B9  75 E2                           jne 0x14063049d
006304BB  45 84 F6                        test r14b, r14b
006304BE  74 0C                           je 0x1406304cc
006304C0  48 8D 0D B9 39 8D 00            lea rcx, [rip + 0x8d39b9]
006304C7  E8 B4 99 D1 FF                  call 0x140349e80
006304CC  4D 8B C7                        mov r8, r15
006304CF  49 8B D4                        mov rdx, r12
006304D2  49 8B CD                        mov rcx, r13
006304D5  E8 76 77 BD FF                  call 0x140207c50
006304DA  88 45 F0                        mov byte ptr [rbp - 0x10], al
006304DD  48 85 F6                        test rsi, rsi
006304E0  74 63                           je 0x140630545
006304E2  40 32 FF                        xor dil, dil
006304E5  40 38 3D CC 43 8D 00            cmp byte ptr [rip + 0x8d43cc], dil
006304EC  75 0C                           jne 0x1406304fa
006304EE  F7 05 88 44 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4488], 0x800
006304F8  74 13                           je 0x14063050d
006304FA  48 8D 0D 7F 39 8D 00            lea rcx, [rip + 0x8d397f]
00630501  E8 1A 61 BE FF                  call 0x140216620
00630506  40 8A F8                        mov dil, al
00630509  84 C0                           test al, al
0063050B  74 38                           je 0x140630545
0063050D  48 83 C6 30                     add rsi, 0x30
00630511  48 8B 1E                        mov rbx, qword ptr [rsi]
00630514  EB 19                           jmp 0x14063052f
00630516  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063051A  48 85 C0                        test rax, rax
0063051D  74 0D                           je 0x14063052c
0063051F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00630523  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00630527  E8 A4 A5 08 00                  call 0x1406baad0
0063052C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063052F  48 3B DE                        cmp rbx, rsi
00630532  75 E2                           jne 0x140630516
00630534  40 84 FF                        test dil, dil
00630537  74 0C                           je 0x140630545
00630539  48 8D 0D 40 39 8D 00            lea rcx, [rip + 0x8d3940]
00630540  E8 3B 99 D1 FF                  call 0x140349e80
00630545  8A 45 F0                        mov al, byte ptr [rbp - 0x10]
00630548  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063054D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00630551  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00630555  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00630559  49 8B E3                        mov rsp, r11
0063055C  41 5F                           pop r15
0063055E  41 5E                           pop r14
00630560  41 5D                           pop r13
00630562  41 5C                           pop r12
00630564  5D                              pop rbp
00630565  C3                              ret
00630566  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeInsertQueueDpcWrapper(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(275, a2, a3, a4);
    if (result == 0) goto loc_006304CC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00630450;
    v_stack_m58 = v_stack_p0;
    goto loc_0063045D;
loc_00630450:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9258061)) != 0) goto loc_00630481;
    if (((*(unsigned int *)(v_rip + 9258241)) & (0x800ULL)) == 0) goto loc_00630494;
loc_00630481:
    result = ExAcquireRundownProtection(v_rip + 9255416, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006304CC;
loc_00630494:
    goto loc_006304B6;
loc_0063049D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006304B6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063049D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9255353;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeInsertQueueDpc(a1, a2, a3, a4);
    v_stack_m38 = (unsigned __int8)(result);
    if (result == 0) goto loc_00630545;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9257932)) != 0) goto loc_006304FA;
    if (((*(unsigned int *)(v_rip + 9258120)) & (0x800ULL)) == 0) goto loc_0063050D;
loc_006304FA:
    result = ExAcquireRundownProtection(v_rip + 9255295, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00630545;
loc_0063050D:
    v_rsi = (result) + (48);
    goto loc_0063052F;
loc_00630516:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063052F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00630516;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9255232;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeInsertQueueDpcWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(275, Arg2, Arg3, a4);
    if (result == 0) goto loc_006304CC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00630450;
    v_stack_m58 = v_stack_p0;
    goto loc_0063045D;
loc_00630450:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D444D)) != 0) goto loc_00630481;
    if (((*(uint32_t *)(v_rip + 0x8D4501)) & (0x800ULL)) == 0) goto loc_00630494;
loc_00630481:
    result = ExAcquireRundownProtection(v_rip + 9255416, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006304CC;
loc_00630494:
    goto loc_006304B6;
loc_0063049D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_006304B6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063049D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9255353;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = KeInsertQueueDpc(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint8_t)(result);
    if (result == 0) goto loc_00630545;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D43CC)) != 0) goto loc_006304FA;
    if (((*(uint32_t *)(v_rip + 0x8D4488)) & (0x800ULL)) == 0) goto loc_0063050D;
loc_006304FA:
    result = ExAcquireRundownProtection(v_rip + 9255295, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00630545;
loc_0063050D:
    local_rsi = (result) + (48);
    goto loc_0063052F;
loc_00630516:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063052F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00630516;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9255232;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006303F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006303F0[BB_006303F0]
  bb_0063043F[BB_0063043F]
  bb_00630446[BB_00630446]
  bb_00630450[BB_00630450]
  bb_00630454[BB_00630454]
  bb_0063045D[BB_0063045D]
  bb_00630475[BB_00630475]
  bb_00630481[BB_00630481]
  bb_00630494[BB_00630494]
  bb_0063049D[BB_0063049D]
  bb_006304A6[BB_006304A6]
  bb_006304B3[BB_006304B3]
  bb_006304B6[BB_006304B6]
  bb_006304BB[BB_006304BB]
  bb_006304C0[BB_006304C0]
  bb_006304CC[BB_006304CC]
  bb_006304E2[BB_006304E2]
  bb_006304EE[BB_006304EE]
  bb_006304FA[BB_006304FA]
  bb_0063050D[BB_0063050D]
  bb_00630516[BB_00630516]
  bb_0063051F[BB_0063051F]
  bb_0063052C[BB_0063052C]
  bb_0063052F[BB_0063052F]
  bb_00630534[BB_00630534]
  bb_00630539[BB_00630539]
  bb_00630545[BB_00630545]
  bb_00630566[BB_00630566]
  bb_006303F0 -->|branch| bb_006304CC
  bb_006303F0 -->|fallthrough| bb_0063043F
  bb_0063043F -->|branch| bb_00630450
  bb_0063043F -->|fallthrough| bb_00630446
  bb_00630446 -->|branch| bb_0063045D
  bb_00630450 -->|branch| bb_0063045D
  bb_00630450 -->|fallthrough| bb_00630454
  bb_00630454 -->|flow| bb_0063045D
  bb_0063045D -->|branch| bb_00630481
  bb_0063045D -->|fallthrough| bb_00630475
  bb_00630475 -->|branch| bb_00630494
  bb_00630475 -->|fallthrough| bb_00630481
  bb_00630481 -->|branch| bb_006304CC
  bb_00630481 -->|fallthrough| bb_00630494
  bb_00630494 -->|branch| bb_006304B6
  bb_0063049D -->|branch| bb_006304B3
  bb_0063049D -->|fallthrough| bb_006304A6
  bb_006304A6 -->|flow| bb_006304B3
  bb_006304B3 -->|flow| bb_006304B6
  bb_006304B6 -->|branch| bb_0063049D
  bb_006304B6 -->|fallthrough| bb_006304BB
  bb_006304BB -->|branch| bb_006304CC
  bb_006304BB -->|fallthrough| bb_006304C0
  bb_006304C0 -->|flow| bb_006304CC
  bb_006304CC -->|branch| bb_00630545
  bb_006304CC -->|fallthrough| bb_006304E2
  bb_006304E2 -->|branch| bb_006304FA
  bb_006304E2 -->|fallthrough| bb_006304EE
  bb_006304EE -->|branch| bb_0063050D
  bb_006304EE -->|fallthrough| bb_006304FA
  bb_006304FA -->|branch| bb_00630545
  bb_006304FA -->|fallthrough| bb_0063050D
  bb_0063050D -->|branch| bb_0063052F
  bb_00630516 -->|branch| bb_0063052C
  bb_00630516 -->|fallthrough| bb_0063051F
  bb_0063051F -->|flow| bb_0063052C
  bb_0063052C -->|flow| bb_0063052F
  bb_0063052F -->|branch| bb_00630516
  bb_0063052F -->|fallthrough| bb_00630534
  bb_00630534 -->|branch| bb_00630545
  bb_00630534 -->|fallthrough| bb_00630539
  bb_00630539 -->|flow| bb_00630545
```
