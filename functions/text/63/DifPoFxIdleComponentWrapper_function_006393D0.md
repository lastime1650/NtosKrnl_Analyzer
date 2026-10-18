# DifPoFxIdleComponentWrapper

- RVA: `0x006393D0`–`0x00639545` (길이 `373` bytes)
- VA: `0x00000001406393D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `102`개 명령, `373/373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00639409` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00639431` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00639469` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639490` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006394A9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006394B7` → [PoFxIdleComponent](../2C/PoFxIdleComponent_function_002C01A0.md) (function, `0x002C01A0`)
- `0x006394E0` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639507` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00639520` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00639443` → RVA `0x00F048B8` (`.data`; read)
- `0x00639456` → RVA `0x00F04980` (`.data`; read)
- `0x00639462` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006393D0  4C 8B DC                        mov r11, rsp
006393D3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006393D7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006393DB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006393DF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006393E3  41 54                           push r12
006393E5  41 56                           push r14
006393E7  41 57                           push r15
006393E9  48 83 EC 40                     sub rsp, 0x40
006393ED  33 C0                           xor eax, eax
006393EF  0F 57 C0                        xorps xmm0, xmm0
006393F2  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006393F7  4C 8B E1                        mov r12, rcx
006393FA  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
006393FE  B9 BD 00 00 00                  mov ecx, 0xbd
00639403  45 8B F0                        mov r14d, r8d
00639406  44 8B FA                        mov r15d, edx
00639409  E8 26 C6 E5 FF                  call 0x140495a34
0063940E  48 8B F0                        mov rsi, rax
00639411  48 85 C0                        test rax, rax
00639414  0F 84 94 00 00 00               je 0x1406394ae
0063941A  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063941D  A8 18                           test al, 0x18
0063941F  74 0C                           je 0x14063942d
00639421  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00639426  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063942B  EB 0E                           jmp 0x14063943b
0063942D  A8 04                           test al, 4
0063942F  74 0A                           je 0x14063943b
00639431  E8 D2 A7 E9 FF                  call 0x1404d3c08
00639436  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063943B  40 32 ED                        xor bpl, bpl
0063943E  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00639443  40 38 2D 6E B4 8C 00            cmp byte ptr [rip + 0x8cb46e], bpl
0063944A  44 89 7C 24 2C                  mov dword ptr [rsp + 0x2c], r15d
0063944F  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00639454  75 0C                           jne 0x140639462
00639456  F7 05 20 B5 8C 00 00 08 00 00   test dword ptr [rip + 0x8cb520], 0x800
00639460  74 13                           je 0x140639475
00639462  48 8D 0D 17 AA 8C 00            lea rcx, [rip + 0x8caa17]
00639469  E8 B2 D1 BD FF                  call 0x140216620
0063946E  40 8A E8                        mov bpl, al
00639471  84 C0                           test al, al
00639473  74 39                           je 0x1406394ae
00639475  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00639479  48 8B 1F                        mov rbx, qword ptr [rdi]
0063947C  EB 1A                           jmp 0x140639498
0063947E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639482  48 85 C0                        test rax, rax
00639485  74 0E                           je 0x140639495
00639487  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063948B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639490  E8 3B 16 08 00                  call 0x1406baad0
00639495  48 8B 1B                        mov rbx, qword ptr [rbx]
00639498  48 3B DF                        cmp rbx, rdi
0063949B  75 E1                           jne 0x14063947e
0063949D  40 84 ED                        test bpl, bpl
006394A0  74 0C                           je 0x1406394ae
006394A2  48 8D 0D D7 A9 8C 00            lea rcx, [rip + 0x8ca9d7]
006394A9  E8 D2 09 D1 FF                  call 0x140349e80
006394AE  45 8B C6                        mov r8d, r14d
006394B1  41 8B D7                        mov edx, r15d
006394B4  49 8B CC                        mov rcx, r12
006394B7  E8 E4 6C C8 FF                  call 0x1402c01a0
006394BC  48 85 F6                        test rsi, rsi
006394BF  74 64                           je 0x140639525
006394C1  40 32 FF                        xor dil, dil
006394C4  40 38 3D ED B3 8C 00            cmp byte ptr [rip + 0x8cb3ed], dil
006394CB  75 0C                           jne 0x1406394d9
006394CD  F7 05 A9 B4 8C 00 00 08 00 00   test dword ptr [rip + 0x8cb4a9], 0x800
006394D7  74 13                           je 0x1406394ec
006394D9  48 8D 0D A0 A9 8C 00            lea rcx, [rip + 0x8ca9a0]
006394E0  E8 3B D1 BD FF                  call 0x140216620
006394E5  40 8A F8                        mov dil, al
006394E8  84 C0                           test al, al
006394EA  74 39                           je 0x140639525
006394EC  48 83 C6 30                     add rsi, 0x30
006394F0  48 8B 1E                        mov rbx, qword ptr [rsi]
006394F3  EB 1A                           jmp 0x14063950f
006394F5  48 8D 43 F0                     lea rax, [rbx - 0x10]
006394F9  48 85 C0                        test rax, rax
006394FC  74 0E                           je 0x14063950c
006394FE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00639502  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639507  E8 C4 15 08 00                  call 0x1406baad0
0063950C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063950F  48 3B DE                        cmp rbx, rsi
00639512  75 E1                           jne 0x1406394f5
00639514  40 84 FF                        test dil, dil
00639517  74 0C                           je 0x140639525
00639519  48 8D 0D 60 A9 8C 00            lea rcx, [rip + 0x8ca960]
00639520  E8 5B 09 D1 FF                  call 0x140349e80
00639525  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063952A  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0063952F  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00639534  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00639539  48 83 C4 40                     add rsp, 0x40
0063953D  41 5F                           pop r15
0063953F  41 5E                           pop r14
00639541  41 5C                           pop r12
00639543  C3                              ret
00639544  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifPoFxIdleComponentWrapper(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
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
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(189, a2, a3, a4);
    if (result == 0) goto loc_006394AE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063942D;
    v_stack_m38 = v_stack_p0;
    goto loc_0063943B;
loc_0063942D:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m2C = (unsigned int)((unsigned int)(a2));
    v_stack_m30 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9221230)) != 0) goto loc_00639462;
    if (((*(unsigned int *)(v_rip + 9221408)) & (0x800ULL)) == 0) goto loc_00639475;
loc_00639462:
    result = ExAcquireRundownProtection(v_rip + 9218583, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006394AE;
loc_00639475:
    goto loc_00639498;
loc_0063947E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00639498:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063947E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9218519;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = PoFxIdleComponent(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if (result == 0) goto loc_00639525;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9221101)) != 0) goto loc_006394D9;
    if (((*(unsigned int *)(v_rip + 9221289)) & (0x800ULL)) == 0) goto loc_006394EC;
loc_006394D9:
    result = ExAcquireRundownProtection(v_rip + 9218464, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00639525;
loc_006394EC:
    v_rsi = (result) + (48);
    goto loc_0063950F;
loc_006394F5:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0063950F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006394F5;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9218400;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifPoFxIdleComponentWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
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
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(189, Arg2, Arg3, a4);
    if (result == 0) goto loc_006394AE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063942D;
    v_stack_m38 = v_stack_p0;
    goto loc_0063943B;
loc_0063942D:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m2C = (uint32_t)((uint32_t)(Arg2));
    v_stack_m30 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8CB46E)) != 0) goto loc_00639462;
    if (((*(uint32_t *)(v_rip + 0x8CB520)) & (0x800ULL)) == 0) goto loc_00639475;
loc_00639462:
    result = ExAcquireRundownProtection(v_rip + 9218583, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006394AE;
loc_00639475:
    goto loc_00639498;
loc_0063947E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00639498:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063947E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9218519;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = PoFxIdleComponent(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if (result == 0) goto loc_00639525;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CB3ED)) != 0) goto loc_006394D9;
    if (((*(uint32_t *)(v_rip + 0x8CB4A9)) & (0x800ULL)) == 0) goto loc_006394EC;
loc_006394D9:
    result = ExAcquireRundownProtection(v_rip + 9218464, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint8_t)(result) == 0) goto loc_00639525;
loc_006394EC:
    local_rsi = (result) + (48);
    goto loc_0063950F;
loc_006394F5:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
loc_0063950F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006394F5;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9218400;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006393D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006393D0[BB_006393D0]
  bb_0063941A[BB_0063941A]
  bb_00639421[BB_00639421]
  bb_0063942D[BB_0063942D]
  bb_00639431[BB_00639431]
  bb_0063943B[BB_0063943B]
  bb_00639456[BB_00639456]
  bb_00639462[BB_00639462]
  bb_00639475[BB_00639475]
  bb_0063947E[BB_0063947E]
  bb_00639487[BB_00639487]
  bb_00639495[BB_00639495]
  bb_00639498[BB_00639498]
  bb_0063949D[BB_0063949D]
  bb_006394A2[BB_006394A2]
  bb_006394AE[BB_006394AE]
  bb_006394C1[BB_006394C1]
  bb_006394CD[BB_006394CD]
  bb_006394D9[BB_006394D9]
  bb_006394EC[BB_006394EC]
  bb_006394F5[BB_006394F5]
  bb_006394FE[BB_006394FE]
  bb_0063950C[BB_0063950C]
  bb_0063950F[BB_0063950F]
  bb_00639514[BB_00639514]
  bb_00639519[BB_00639519]
  bb_00639525[BB_00639525]
  bb_00639544[BB_00639544]
  bb_006393D0 -->|branch| bb_006394AE
  bb_006393D0 -->|fallthrough| bb_0063941A
  bb_0063941A -->|branch| bb_0063942D
  bb_0063941A -->|fallthrough| bb_00639421
  bb_00639421 -->|branch| bb_0063943B
  bb_0063942D -->|branch| bb_0063943B
  bb_0063942D -->|fallthrough| bb_00639431
  bb_00639431 -->|flow| bb_0063943B
  bb_0063943B -->|branch| bb_00639462
  bb_0063943B -->|fallthrough| bb_00639456
  bb_00639456 -->|branch| bb_00639475
  bb_00639456 -->|fallthrough| bb_00639462
  bb_00639462 -->|branch| bb_006394AE
  bb_00639462 -->|fallthrough| bb_00639475
  bb_00639475 -->|branch| bb_00639498
  bb_0063947E -->|branch| bb_00639495
  bb_0063947E -->|fallthrough| bb_00639487
  bb_00639487 -->|flow| bb_00639495
  bb_00639495 -->|flow| bb_00639498
  bb_00639498 -->|branch| bb_0063947E
  bb_00639498 -->|fallthrough| bb_0063949D
  bb_0063949D -->|branch| bb_006394AE
  bb_0063949D -->|fallthrough| bb_006394A2
  bb_006394A2 -->|flow| bb_006394AE
  bb_006394AE -->|branch| bb_00639525
  bb_006394AE -->|fallthrough| bb_006394C1
  bb_006394C1 -->|branch| bb_006394D9
  bb_006394C1 -->|fallthrough| bb_006394CD
  bb_006394CD -->|branch| bb_006394EC
  bb_006394CD -->|fallthrough| bb_006394D9
  bb_006394D9 -->|branch| bb_00639525
  bb_006394D9 -->|fallthrough| bb_006394EC
  bb_006394EC -->|branch| bb_0063950F
  bb_006394F5 -->|branch| bb_0063950C
  bb_006394F5 -->|fallthrough| bb_006394FE
  bb_006394FE -->|flow| bb_0063950C
  bb_0063950C -->|flow| bb_0063950F
  bb_0063950F -->|branch| bb_006394F5
  bb_0063950F -->|fallthrough| bb_00639514
  bb_00639514 -->|branch| bb_00639525
  bb_00639514 -->|fallthrough| bb_00639519
  bb_00639519 -->|flow| bb_00639525
```
