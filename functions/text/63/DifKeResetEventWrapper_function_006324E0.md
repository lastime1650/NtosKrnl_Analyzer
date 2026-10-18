# DifKeResetEventWrapper

- RVA: `0x006324E0`–`0x0063263F` (길이 `351` bytes)
- VA: `0x00000001406324E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063250F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00632537` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00632565` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063258C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006325A5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006325AD` → [KeResetEvent](../24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x006325DA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00632601` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063261A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00632549` → RVA `0x00F048B8` (`.data`; read)
- `0x00632552` → RVA `0x00F04980` (`.data`; read)
- `0x0063255E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006324E0  4C 8B DC                        mov r11, rsp
006324E3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006324E7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006324EB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006324EF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006324F3  41 56                           push r14
006324F5  48 83 EC 40                     sub rsp, 0x40
006324F9  33 C0                           xor eax, eax
006324FB  0F 57 C0                        xorps xmm0, xmm0
006324FE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00632503  48 8B E9                        mov rbp, rcx
00632506  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0063250A  B9 FC 00 00 00                  mov ecx, 0xfc
0063250F  E8 20 35 E6 FF                  call 0x140495a34
00632514  48 8B F0                        mov rsi, rax
00632517  48 85 C0                        test rax, rax
0063251A  0F 84 8A 00 00 00               je 0x1406325aa
00632520  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00632523  A8 18                           test al, 0x18
00632525  74 0C                           je 0x140632533
00632527  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0063252C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00632531  EB 0E                           jmp 0x140632541
00632533  A8 04                           test al, 4
00632535  74 0A                           je 0x140632541
00632537  E8 CC 16 EA FF                  call 0x1404d3c08
0063253C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00632541  40 32 FF                        xor dil, dil
00632544  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00632549  40 38 3D 68 23 8D 00            cmp byte ptr [rip + 0x8d2368], dil
00632550  75 0C                           jne 0x14063255e
00632552  F7 05 24 24 8D 00 00 08 00 00   test dword ptr [rip + 0x8d2424], 0x800
0063255C  74 13                           je 0x140632571
0063255E  48 8D 0D 1B 19 8D 00            lea rcx, [rip + 0x8d191b]
00632565  E8 B6 40 BE FF                  call 0x140216620
0063256A  40 8A F8                        mov dil, al
0063256D  84 C0                           test al, al
0063256F  74 39                           je 0x1406325aa
00632571  4C 8D 76 20                     lea r14, [rsi + 0x20]
00632575  49 8B 1E                        mov rbx, qword ptr [r14]
00632578  EB 1A                           jmp 0x140632594
0063257A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063257E  48 85 C0                        test rax, rax
00632581  74 0E                           je 0x140632591
00632583  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00632587  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063258C  E8 3F 85 08 00                  call 0x1406baad0
00632591  48 8B 1B                        mov rbx, qword ptr [rbx]
00632594  49 3B DE                        cmp rbx, r14
00632597  75 E1                           jne 0x14063257a
00632599  40 84 FF                        test dil, dil
0063259C  74 0C                           je 0x1406325aa
0063259E  48 8D 0D DB 18 8D 00            lea rcx, [rip + 0x8d18db]
006325A5  E8 D6 78 D1 FF                  call 0x140349e80
006325AA  48 8B CD                        mov rcx, rbp
006325AD  E8 9E 5D C1 FF                  call 0x140248350
006325B2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006325B6  48 85 F6                        test rsi, rsi
006325B9  74 64                           je 0x14063261f
006325BB  40 32 FF                        xor dil, dil
006325BE  40 38 3D F3 22 8D 00            cmp byte ptr [rip + 0x8d22f3], dil
006325C5  75 0C                           jne 0x1406325d3
006325C7  F7 05 AF 23 8D 00 00 08 00 00   test dword ptr [rip + 0x8d23af], 0x800
006325D1  74 13                           je 0x1406325e6
006325D3  48 8D 0D A6 18 8D 00            lea rcx, [rip + 0x8d18a6]
006325DA  E8 41 40 BE FF                  call 0x140216620
006325DF  40 8A F8                        mov dil, al
006325E2  84 C0                           test al, al
006325E4  74 39                           je 0x14063261f
006325E6  48 83 C6 30                     add rsi, 0x30
006325EA  48 8B 1E                        mov rbx, qword ptr [rsi]
006325ED  EB 1A                           jmp 0x140632609
006325EF  48 8D 43 F0                     lea rax, [rbx - 0x10]
006325F3  48 85 C0                        test rax, rax
006325F6  74 0E                           je 0x140632606
006325F8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006325FC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00632601  E8 CA 84 08 00                  call 0x1406baad0
00632606  48 8B 1B                        mov rbx, qword ptr [rbx]
00632609  48 3B DE                        cmp rbx, rsi
0063260C  75 E1                           jne 0x1406325ef
0063260E  40 84 FF                        test dil, dil
00632611  74 0C                           je 0x14063261f
00632613  48 8D 0D 66 18 8D 00            lea rcx, [rip + 0x8d1866]
0063261A  E8 61 78 D1 FF                  call 0x140349e80
0063261F  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00632623  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00632628  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0063262D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00632632  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00632637  48 83 C4 40                     add rsp, 0x40
0063263B  41 5E                           pop r14
0063263D  C3                              ret
0063263E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeResetEventWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(252, a2, a3, a4);
    if (result == 0) goto loc_006325AA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00632533;
    v_stack_m28 = v_stack_p0;
    goto loc_00632541;
loc_00632533:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9249640)) != 0) goto loc_0063255E;
    if (((*(unsigned int *)(v_rip + 9249828)) & (0x800ULL)) == 0) goto loc_00632571;
loc_0063255E:
    result = ExAcquireRundownProtection(v_rip + 9247003, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006325AA;
loc_00632571:
    goto loc_00632594;
loc_0063257A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00632594:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063257A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9246939;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeResetEvent(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0063261F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9249523)) != 0) goto loc_006325D3;
    if (((*(unsigned int *)(v_rip + 9249711)) & (0x800ULL)) == 0) goto loc_006325E6;
loc_006325D3:
    result = ExAcquireRundownProtection(v_rip + 9246886, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063261F;
loc_006325E6:
    v_rsi = (result) + (48);
    goto loc_00632609;
loc_006325EF:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00632609:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006325EF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9246822;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifKeResetEventWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(252, a2, a3, a4);
    if (result == 0) goto loc_006325AA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00632533;
    v_stack_m28 = v_stack_p0;
    goto loc_00632541;
loc_00632533:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D2368)) != 0) goto loc_0063255E;
    if (((*(uint32_t *)(v_rip + 0x8D2424)) & (0x800ULL)) == 0) goto loc_00632571;
loc_0063255E:
    result = ExAcquireRundownProtection(v_rip + 9247003, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006325AA;
loc_00632571:
    goto loc_00632594;
loc_0063257A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00632594:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063257A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9246939;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeResetEvent(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0063261F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D22F3)) != 0) goto loc_006325D3;
    if (((*(uint32_t *)(v_rip + 0x8D23AF)) & (0x800ULL)) == 0) goto loc_006325E6;
loc_006325D3:
    result = ExAcquireRundownProtection(v_rip + 9246886, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063261F;
loc_006325E6:
    local_rsi = (result) + (48);
    goto loc_00632609;
loc_006325EF:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00632609:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006325EF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9246822;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006324E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006324E0[BB_006324E0]
  bb_00632520[BB_00632520]
  bb_00632527[BB_00632527]
  bb_00632533[BB_00632533]
  bb_00632537[BB_00632537]
  bb_00632541[BB_00632541]
  bb_00632552[BB_00632552]
  bb_0063255E[BB_0063255E]
  bb_00632571[BB_00632571]
  bb_0063257A[BB_0063257A]
  bb_00632583[BB_00632583]
  bb_00632591[BB_00632591]
  bb_00632594[BB_00632594]
  bb_00632599[BB_00632599]
  bb_0063259E[BB_0063259E]
  bb_006325AA[BB_006325AA]
  bb_006325BB[BB_006325BB]
  bb_006325C7[BB_006325C7]
  bb_006325D3[BB_006325D3]
  bb_006325E6[BB_006325E6]
  bb_006325EF[BB_006325EF]
  bb_006325F8[BB_006325F8]
  bb_00632606[BB_00632606]
  bb_00632609[BB_00632609]
  bb_0063260E[BB_0063260E]
  bb_00632613[BB_00632613]
  bb_0063261F[BB_0063261F]
  bb_0063263E[BB_0063263E]
  bb_006324E0 -->|branch| bb_006325AA
  bb_006324E0 -->|fallthrough| bb_00632520
  bb_00632520 -->|branch| bb_00632533
  bb_00632520 -->|fallthrough| bb_00632527
  bb_00632527 -->|branch| bb_00632541
  bb_00632533 -->|branch| bb_00632541
  bb_00632533 -->|fallthrough| bb_00632537
  bb_00632537 -->|flow| bb_00632541
  bb_00632541 -->|branch| bb_0063255E
  bb_00632541 -->|fallthrough| bb_00632552
  bb_00632552 -->|branch| bb_00632571
  bb_00632552 -->|fallthrough| bb_0063255E
  bb_0063255E -->|branch| bb_006325AA
  bb_0063255E -->|fallthrough| bb_00632571
  bb_00632571 -->|branch| bb_00632594
  bb_0063257A -->|branch| bb_00632591
  bb_0063257A -->|fallthrough| bb_00632583
  bb_00632583 -->|flow| bb_00632591
  bb_00632591 -->|flow| bb_00632594
  bb_00632594 -->|branch| bb_0063257A
  bb_00632594 -->|fallthrough| bb_00632599
  bb_00632599 -->|branch| bb_006325AA
  bb_00632599 -->|fallthrough| bb_0063259E
  bb_0063259E -->|flow| bb_006325AA
  bb_006325AA -->|branch| bb_0063261F
  bb_006325AA -->|fallthrough| bb_006325BB
  bb_006325BB -->|branch| bb_006325D3
  bb_006325BB -->|fallthrough| bb_006325C7
  bb_006325C7 -->|branch| bb_006325E6
  bb_006325C7 -->|fallthrough| bb_006325D3
  bb_006325D3 -->|branch| bb_0063261F
  bb_006325D3 -->|fallthrough| bb_006325E6
  bb_006325E6 -->|branch| bb_00632609
  bb_006325EF -->|branch| bb_00632606
  bb_006325EF -->|fallthrough| bb_006325F8
  bb_006325F8 -->|flow| bb_00632606
  bb_00632606 -->|flow| bb_00632609
  bb_00632609 -->|branch| bb_006325EF
  bb_00632609 -->|fallthrough| bb_0063260E
  bb_0063260E -->|branch| bb_0063261F
  bb_0063260E -->|fallthrough| bb_00632613
  bb_00632613 -->|flow| bb_0063261F
```
