# DifExIsFastResourceHeldWrapper

- RVA: `0x00621510`–`0x0062166F` (길이 `351` bytes)
- VA: `0x0000000140621510`
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
- `0x0062153F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00621567` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00621595` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006215BC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006215D5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006215DD` → [ExIsFastResourceHeld](../40/ExIsFastResourceHeld_function_00401AE0.md) (function, `0x00401AE0`)
- `0x0062160A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00621631` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062164A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00621579` → RVA `0x00F048B8` (`.data`; read)
- `0x00621582` → RVA `0x00F04980` (`.data`; read)
- `0x0062158E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00621510  4C 8B DC                        mov r11, rsp
00621513  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00621517  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062151B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062151F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00621523  41 56                           push r14
00621525  48 83 EC 40                     sub rsp, 0x40
00621529  33 C0                           xor eax, eax
0062152B  0F 57 C0                        xorps xmm0, xmm0
0062152E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00621533  48 8B E9                        mov rbp, rcx
00621536  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062153A  B9 CB 01 00 00                  mov ecx, 0x1cb
0062153F  E8 F0 44 E7 FF                  call 0x140495a34
00621544  48 8B F0                        mov rsi, rax
00621547  48 85 C0                        test rax, rax
0062154A  0F 84 8A 00 00 00               je 0x1406215da
00621550  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00621553  A8 18                           test al, 0x18
00621555  74 0C                           je 0x140621563
00621557  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062155C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00621561  EB 0E                           jmp 0x140621571
00621563  A8 04                           test al, 4
00621565  74 0A                           je 0x140621571
00621567  E8 9C 26 EB FF                  call 0x1404d3c08
0062156C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00621571  40 32 FF                        xor dil, dil
00621574  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00621579  40 38 3D 38 33 8E 00            cmp byte ptr [rip + 0x8e3338], dil
00621580  75 0C                           jne 0x14062158e
00621582  F7 05 F4 33 8E 00 00 08 00 00   test dword ptr [rip + 0x8e33f4], 0x800
0062158C  74 13                           je 0x1406215a1
0062158E  48 8D 0D EB 28 8E 00            lea rcx, [rip + 0x8e28eb]
00621595  E8 86 50 BF FF                  call 0x140216620
0062159A  40 8A F8                        mov dil, al
0062159D  84 C0                           test al, al
0062159F  74 39                           je 0x1406215da
006215A1  4C 8D 76 20                     lea r14, [rsi + 0x20]
006215A5  49 8B 1E                        mov rbx, qword ptr [r14]
006215A8  EB 1A                           jmp 0x1406215c4
006215AA  48 8D 43 F0                     lea rax, [rbx - 0x10]
006215AE  48 85 C0                        test rax, rax
006215B1  74 0E                           je 0x1406215c1
006215B3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006215B7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006215BC  E8 0F 95 09 00                  call 0x1406baad0
006215C1  48 8B 1B                        mov rbx, qword ptr [rbx]
006215C4  49 3B DE                        cmp rbx, r14
006215C7  75 E1                           jne 0x1406215aa
006215C9  40 84 FF                        test dil, dil
006215CC  74 0C                           je 0x1406215da
006215CE  48 8D 0D AB 28 8E 00            lea rcx, [rip + 0x8e28ab]
006215D5  E8 A6 88 D2 FF                  call 0x140349e80
006215DA  48 8B CD                        mov rcx, rbp
006215DD  E8 FE 04 DE FF                  call 0x140401ae0
006215E2  88 44 24 30                     mov byte ptr [rsp + 0x30], al
006215E6  48 85 F6                        test rsi, rsi
006215E9  74 64                           je 0x14062164f
006215EB  40 32 FF                        xor dil, dil
006215EE  40 38 3D C3 32 8E 00            cmp byte ptr [rip + 0x8e32c3], dil
006215F5  75 0C                           jne 0x140621603
006215F7  F7 05 7F 33 8E 00 00 08 00 00   test dword ptr [rip + 0x8e337f], 0x800
00621601  74 13                           je 0x140621616
00621603  48 8D 0D 76 28 8E 00            lea rcx, [rip + 0x8e2876]
0062160A  E8 11 50 BF FF                  call 0x140216620
0062160F  40 8A F8                        mov dil, al
00621612  84 C0                           test al, al
00621614  74 39                           je 0x14062164f
00621616  48 83 C6 30                     add rsi, 0x30
0062161A  48 8B 1E                        mov rbx, qword ptr [rsi]
0062161D  EB 1A                           jmp 0x140621639
0062161F  48 8D 43 F0                     lea rax, [rbx - 0x10]
00621623  48 85 C0                        test rax, rax
00621626  74 0E                           je 0x140621636
00621628  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062162C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00621631  E8 9A 94 09 00                  call 0x1406baad0
00621636  48 8B 1B                        mov rbx, qword ptr [rbx]
00621639  48 3B DE                        cmp rbx, rsi
0062163C  75 E1                           jne 0x14062161f
0062163E  40 84 FF                        test dil, dil
00621641  74 0C                           je 0x14062164f
00621643  48 8D 0D 36 28 8E 00            lea rcx, [rip + 0x8e2836]
0062164A  E8 31 88 D2 FF                  call 0x140349e80
0062164F  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00621653  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00621658  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062165D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00621662  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00621667  48 83 C4 40                     add rsp, 0x40
0062166B  41 5E                           pop r14
0062166D  C3                              ret
0062166E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExIsFastResourceHeldWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
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
    result = DifGetAPIThunkContextById(459, a2, a3, a4);
    if (result == 0) goto loc_006215DA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00621563;
    v_stack_m28 = v_stack_p0;
    goto loc_00621571;
loc_00621563:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9319224)) != 0) goto loc_0062158E;
    if (((*(unsigned int *)(v_rip + 9319412)) & (0x800ULL)) == 0) goto loc_006215A1;
loc_0062158E:
    result = ExAcquireRundownProtection(v_rip + 9316587, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006215DA;
loc_006215A1:
    goto loc_006215C4;
loc_006215AA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006215C4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006215AA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9316523;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExIsFastResourceHeld(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_0062164F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9319107)) != 0) goto loc_00621603;
    if (((*(unsigned int *)(v_rip + 9319295)) & (0x800ULL)) == 0) goto loc_00621616;
loc_00621603:
    result = ExAcquireRundownProtection(v_rip + 9316470, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062164F;
loc_00621616:
    v_rsi = (result) + (48);
    goto loc_00621639;
loc_0062161F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621639:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062161F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9316406;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExIsFastResourceHeldWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(459, a2, a3, a4);
    if (result == 0) goto loc_006215DA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00621563;
    v_stack_m28 = v_stack_p0;
    goto loc_00621571;
loc_00621563:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E3338)) != 0) goto loc_0062158E;
    if (((*(uint32_t *)(v_rip + 0x8E33F4)) & (0x800ULL)) == 0) goto loc_006215A1;
loc_0062158E:
    result = ExAcquireRundownProtection(v_rip + 9316587, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006215DA;
loc_006215A1:
    goto loc_006215C4;
loc_006215AA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006215C4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006215AA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9316523;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExIsFastResourceHeld(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_0062164F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E32C3)) != 0) goto loc_00621603;
    if (((*(uint32_t *)(v_rip + 0x8E337F)) & (0x800ULL)) == 0) goto loc_00621616;
loc_00621603:
    result = ExAcquireRundownProtection(v_rip + 9316470, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062164F;
loc_00621616:
    local_rsi = (result) + (48);
    goto loc_00621639;
loc_0062161F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00621639:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062161F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9316406;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00621510&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00621510[BB_00621510]
  bb_00621550[BB_00621550]
  bb_00621557[BB_00621557]
  bb_00621563[BB_00621563]
  bb_00621567[BB_00621567]
  bb_00621571[BB_00621571]
  bb_00621582[BB_00621582]
  bb_0062158E[BB_0062158E]
  bb_006215A1[BB_006215A1]
  bb_006215AA[BB_006215AA]
  bb_006215B3[BB_006215B3]
  bb_006215C1[BB_006215C1]
  bb_006215C4[BB_006215C4]
  bb_006215C9[BB_006215C9]
  bb_006215CE[BB_006215CE]
  bb_006215DA[BB_006215DA]
  bb_006215EB[BB_006215EB]
  bb_006215F7[BB_006215F7]
  bb_00621603[BB_00621603]
  bb_00621616[BB_00621616]
  bb_0062161F[BB_0062161F]
  bb_00621628[BB_00621628]
  bb_00621636[BB_00621636]
  bb_00621639[BB_00621639]
  bb_0062163E[BB_0062163E]
  bb_00621643[BB_00621643]
  bb_0062164F[BB_0062164F]
  bb_0062166E[BB_0062166E]
  bb_00621510 -->|branch| bb_006215DA
  bb_00621510 -->|fallthrough| bb_00621550
  bb_00621550 -->|branch| bb_00621563
  bb_00621550 -->|fallthrough| bb_00621557
  bb_00621557 -->|branch| bb_00621571
  bb_00621563 -->|branch| bb_00621571
  bb_00621563 -->|fallthrough| bb_00621567
  bb_00621567 -->|flow| bb_00621571
  bb_00621571 -->|branch| bb_0062158E
  bb_00621571 -->|fallthrough| bb_00621582
  bb_00621582 -->|branch| bb_006215A1
  bb_00621582 -->|fallthrough| bb_0062158E
  bb_0062158E -->|branch| bb_006215DA
  bb_0062158E -->|fallthrough| bb_006215A1
  bb_006215A1 -->|branch| bb_006215C4
  bb_006215AA -->|branch| bb_006215C1
  bb_006215AA -->|fallthrough| bb_006215B3
  bb_006215B3 -->|flow| bb_006215C1
  bb_006215C1 -->|flow| bb_006215C4
  bb_006215C4 -->|branch| bb_006215AA
  bb_006215C4 -->|fallthrough| bb_006215C9
  bb_006215C9 -->|branch| bb_006215DA
  bb_006215C9 -->|fallthrough| bb_006215CE
  bb_006215CE -->|flow| bb_006215DA
  bb_006215DA -->|branch| bb_0062164F
  bb_006215DA -->|fallthrough| bb_006215EB
  bb_006215EB -->|branch| bb_00621603
  bb_006215EB -->|fallthrough| bb_006215F7
  bb_006215F7 -->|branch| bb_00621616
  bb_006215F7 -->|fallthrough| bb_00621603
  bb_00621603 -->|branch| bb_0062164F
  bb_00621603 -->|fallthrough| bb_00621616
  bb_00621616 -->|branch| bb_00621639
  bb_0062161F -->|branch| bb_00621636
  bb_0062161F -->|fallthrough| bb_00621628
  bb_00621628 -->|flow| bb_00621636
  bb_00621636 -->|flow| bb_00621639
  bb_00621639 -->|branch| bb_0062161F
  bb_00621639 -->|fallthrough| bb_0062163E
  bb_0062163E -->|branch| bb_0062164F
  bb_0062163E -->|fallthrough| bb_00621643
  bb_00621643 -->|flow| bb_0062164F
```
