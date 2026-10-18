# DifIoCreateNotificationEventWrapper

- RVA: `0x00629500`–`0x00629666` (길이 `358` bytes)
- VA: `0x0000000140629500`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `358/358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062952E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00629556` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00629589` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006295B0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006295C9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006295D4` → [IoCreateNotificationEvent](../../page/A8/IoCreateNotificationEvent_function_00A80470.md) (function, `0x00A80470`)
- `0x00629602` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00629629` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00629642` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00629568` → RVA `0x00F048B8` (`.data`; read)
- `0x00629576` → RVA `0x00F04980` (`.data`; read)
- `0x00629582` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006295D4` → [IoCreateNotificationEvent](../../page/A8/IoCreateNotificationEvent_function_00A80470.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00629500  48 8B C4                        mov rax, rsp
00629503  48 89 58 08                     mov qword ptr [rax + 8], rbx
00629507  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062950B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062950F  57                              push rdi
00629510  41 56                           push r14
00629512  41 57                           push r15
00629514  48 83 EC 40                     sub rsp, 0x40
00629518  0F 57 C0                        xorps xmm0, xmm0
0062951B  4C 8B F9                        mov r15, rcx
0062951E  B9 5F 01 00 00                  mov ecx, 0x15f
00629523  4C 8B F2                        mov r14, rdx
00629526  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062952A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062952E  E8 01 C5 E6 FF                  call 0x140495a34
00629533  48 8B F0                        mov rsi, rax
00629536  48 85 C0                        test rax, rax
00629539  0F 84 8F 00 00 00               je 0x1406295ce
0062953F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00629542  A8 18                           test al, 0x18
00629544  74 0C                           je 0x140629552
00629546  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062954B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00629550  EB 0E                           jmp 0x140629560
00629552  A8 04                           test al, 4
00629554  74 0A                           je 0x140629560
00629556  E8 AD A6 EA FF                  call 0x1404d3c08
0062955B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00629560  40 32 ED                        xor bpl, bpl
00629563  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00629568  40 38 2D 49 B3 8D 00            cmp byte ptr [rip + 0x8db349], bpl
0062956F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00629574  75 0C                           jne 0x140629582
00629576  F7 05 00 B4 8D 00 00 08 00 00   test dword ptr [rip + 0x8db400], 0x800
00629580  74 13                           je 0x140629595
00629582  48 8D 0D F7 A8 8D 00            lea rcx, [rip + 0x8da8f7]
00629589  E8 92 D0 BE FF                  call 0x140216620
0062958E  40 8A E8                        mov bpl, al
00629591  84 C0                           test al, al
00629593  74 39                           je 0x1406295ce
00629595  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00629599  48 8B 1F                        mov rbx, qword ptr [rdi]
0062959C  EB 1A                           jmp 0x1406295b8
0062959E  48 8D 43 F0                     lea rax, [rbx - 0x10]
006295A2  48 85 C0                        test rax, rax
006295A5  74 0E                           je 0x1406295b5
006295A7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006295AB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006295B0  E8 1B 15 09 00                  call 0x1406baad0
006295B5  48 8B 1B                        mov rbx, qword ptr [rbx]
006295B8  48 3B DF                        cmp rbx, rdi
006295BB  75 E1                           jne 0x14062959e
006295BD  40 84 ED                        test bpl, bpl
006295C0  74 0C                           je 0x1406295ce
006295C2  48 8D 0D B7 A8 8D 00            lea rcx, [rip + 0x8da8b7]
006295C9  E8 B2 08 D2 FF                  call 0x140349e80
006295CE  49 8B D6                        mov rdx, r14
006295D1  49 8B CF                        mov rcx, r15
006295D4  E8 97 6E 45 00                  call 0x140a80470
006295D9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
006295DE  48 85 F6                        test rsi, rsi
006295E1  74 64                           je 0x140629647
006295E3  40 32 FF                        xor dil, dil
006295E6  40 38 3D CB B2 8D 00            cmp byte ptr [rip + 0x8db2cb], dil
006295ED  75 0C                           jne 0x1406295fb
006295EF  F7 05 87 B3 8D 00 00 08 00 00   test dword ptr [rip + 0x8db387], 0x800
006295F9  74 13                           je 0x14062960e
006295FB  48 8D 0D 7E A8 8D 00            lea rcx, [rip + 0x8da87e]
00629602  E8 19 D0 BE FF                  call 0x140216620
00629607  40 8A F8                        mov dil, al
0062960A  84 C0                           test al, al
0062960C  74 39                           je 0x140629647
0062960E  48 83 C6 30                     add rsi, 0x30
00629612  48 8B 1E                        mov rbx, qword ptr [rsi]
00629615  EB 1A                           jmp 0x140629631
00629617  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062961B  48 85 C0                        test rax, rax
0062961E  74 0E                           je 0x14062962e
00629620  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00629624  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00629629  E8 A2 14 09 00                  call 0x1406baad0
0062962E  48 8B 1B                        mov rbx, qword ptr [rbx]
00629631  48 3B DE                        cmp rbx, rsi
00629634  75 E1                           jne 0x140629617
00629636  40 84 FF                        test dil, dil
00629639  74 0C                           je 0x140629647
0062963B  48 8D 0D 3E A8 8D 00            lea rcx, [rip + 0x8da83e]
00629642  E8 39 08 D2 FF                  call 0x140349e80
00629647  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0062964C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00629651  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00629656  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062965B  48 83 C4 40                     add rsp, 0x40
0062965F  41 5F                           pop r15
00629661  41 5E                           pop r14
00629663  5F                              pop rdi
00629664  C3                              ret
00629665  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoCreateNotificationEventWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(351, a2, a3, a4);
    if (result == 0) goto loc_006295CE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00629552;
    v_stack_m38 = v_stack_p0;
    goto loc_00629560;
loc_00629552:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9286473)) != 0) goto loc_00629582;
    if (((*(unsigned int *)(v_rip + 9286656)) & (0x800ULL)) == 0) goto loc_00629595;
loc_00629582:
    result = ExAcquireRundownProtection(v_rip + 9283831, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006295CE;
loc_00629595:
    goto loc_006295B8;
loc_0062959E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006295B8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062959E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9283767;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoCreateNotificationEvent(a1, a2, a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00629647;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9286347)) != 0) goto loc_006295FB;
    if (((*(unsigned int *)(v_rip + 9286535)) & (0x800ULL)) == 0) goto loc_0062960E;
loc_006295FB:
    result = ExAcquireRundownProtection(v_rip + 9283710, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00629647;
loc_0062960E:
    v_rsi = (result) + (48);
    goto loc_00629631;
loc_00629617:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00629631:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00629617;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9283646;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m20;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoCreateNotificationEventWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(351, Arg2, a3, a4);
    if (result == 0) goto loc_006295CE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00629552;
    v_stack_m38 = v_stack_p0;
    goto loc_00629560;
loc_00629552:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8DB349)) != 0) goto loc_00629582;
    if (((*(uint32_t *)(v_rip + 0x8DB400)) & (0x800ULL)) == 0) goto loc_00629595;
loc_00629582:
    result = ExAcquireRundownProtection(v_rip + 9283831, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006295CE;
loc_00629595:
    goto loc_006295B8;
loc_0062959E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006295B8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062959E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9283767;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = IoCreateNotificationEvent(Arg1, Arg2, a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00629647;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DB2CB)) != 0) goto loc_006295FB;
    if (((*(uint32_t *)(v_rip + 0x8DB387)) & (0x800ULL)) == 0) goto loc_0062960E;
loc_006295FB:
    result = ExAcquireRundownProtection(v_rip + 9283710, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00629647;
loc_0062960E:
    local_rsi = (result) + (48);
    goto loc_00629631;
loc_00629617:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00629631:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00629617;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9283646;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00629500&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00629500[BB_00629500]
  bb_0062953F[BB_0062953F]
  bb_00629546[BB_00629546]
  bb_00629552[BB_00629552]
  bb_00629556[BB_00629556]
  bb_00629560[BB_00629560]
  bb_00629576[BB_00629576]
  bb_00629582[BB_00629582]
  bb_00629595[BB_00629595]
  bb_0062959E[BB_0062959E]
  bb_006295A7[BB_006295A7]
  bb_006295B5[BB_006295B5]
  bb_006295B8[BB_006295B8]
  bb_006295BD[BB_006295BD]
  bb_006295C2[BB_006295C2]
  bb_006295CE[BB_006295CE]
  bb_006295E3[BB_006295E3]
  bb_006295EF[BB_006295EF]
  bb_006295FB[BB_006295FB]
  bb_0062960E[BB_0062960E]
  bb_00629617[BB_00629617]
  bb_00629620[BB_00629620]
  bb_0062962E[BB_0062962E]
  bb_00629631[BB_00629631]
  bb_00629636[BB_00629636]
  bb_0062963B[BB_0062963B]
  bb_00629647[BB_00629647]
  bb_00629665[BB_00629665]
  bb_00629500 -->|branch| bb_006295CE
  bb_00629500 -->|fallthrough| bb_0062953F
  bb_0062953F -->|branch| bb_00629552
  bb_0062953F -->|fallthrough| bb_00629546
  bb_00629546 -->|branch| bb_00629560
  bb_00629552 -->|branch| bb_00629560
  bb_00629552 -->|fallthrough| bb_00629556
  bb_00629556 -->|flow| bb_00629560
  bb_00629560 -->|branch| bb_00629582
  bb_00629560 -->|fallthrough| bb_00629576
  bb_00629576 -->|branch| bb_00629595
  bb_00629576 -->|fallthrough| bb_00629582
  bb_00629582 -->|branch| bb_006295CE
  bb_00629582 -->|fallthrough| bb_00629595
  bb_00629595 -->|branch| bb_006295B8
  bb_0062959E -->|branch| bb_006295B5
  bb_0062959E -->|fallthrough| bb_006295A7
  bb_006295A7 -->|flow| bb_006295B5
  bb_006295B5 -->|flow| bb_006295B8
  bb_006295B8 -->|branch| bb_0062959E
  bb_006295B8 -->|fallthrough| bb_006295BD
  bb_006295BD -->|branch| bb_006295CE
  bb_006295BD -->|fallthrough| bb_006295C2
  bb_006295C2 -->|flow| bb_006295CE
  bb_006295CE -->|branch| bb_00629647
  bb_006295CE -->|fallthrough| bb_006295E3
  bb_006295E3 -->|branch| bb_006295FB
  bb_006295E3 -->|fallthrough| bb_006295EF
  bb_006295EF -->|branch| bb_0062960E
  bb_006295EF -->|fallthrough| bb_006295FB
  bb_006295FB -->|branch| bb_00629647
  bb_006295FB -->|fallthrough| bb_0062960E
  bb_0062960E -->|branch| bb_00629631
  bb_00629617 -->|branch| bb_0062962E
  bb_00629617 -->|fallthrough| bb_00629620
  bb_00629620 -->|flow| bb_0062962E
  bb_0062962E -->|flow| bb_00629631
  bb_00629631 -->|branch| bb_00629617
  bb_00629631 -->|fallthrough| bb_00629636
  bb_00629636 -->|branch| bb_00629647
  bb_00629636 -->|fallthrough| bb_0062963B
  bb_0062963B -->|flow| bb_00629647
```
