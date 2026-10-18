# DifIoAllocateErrorLogEntryWrapper

- RVA: `0x006276C0`–`0x00627826` (길이 `358` bytes)
- VA: `0x00000001406276C0`
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
- `0x006276EE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00627716` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00627749` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00627770` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00627789` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00627794` → [IoAllocateErrorLogEntry](../4A/IoAllocateErrorLogEntry_function_004ABF20.md) (function, `0x004ABF20`)
- `0x006277C2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006277E9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00627802` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00627728` → RVA `0x00F048B8` (`.data`; read)
- `0x00627736` → RVA `0x00F04980` (`.data`; read)
- `0x00627742` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006276C0  48 8B C4                        mov rax, rsp
006276C3  48 89 58 08                     mov qword ptr [rax + 8], rbx
006276C7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006276CB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006276CF  57                              push rdi
006276D0  41 56                           push r14
006276D2  41 57                           push r15
006276D4  48 83 EC 40                     sub rsp, 0x40
006276D8  0F 57 C0                        xorps xmm0, xmm0
006276DB  4C 8B F9                        mov r15, rcx
006276DE  B9 70 01 00 00                  mov ecx, 0x170
006276E3  44 8A F2                        mov r14b, dl
006276E6  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
006276EA  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
006276EE  E8 41 E3 E6 FF                  call 0x140495a34
006276F3  48 8B F0                        mov rsi, rax
006276F6  48 85 C0                        test rax, rax
006276F9  0F 84 8F 00 00 00               je 0x14062778e
006276FF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00627702  A8 18                           test al, 0x18
00627704  74 0C                           je 0x140627712
00627706  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062770B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00627710  EB 0E                           jmp 0x140627720
00627712  A8 04                           test al, 4
00627714  74 0A                           je 0x140627720
00627716  E8 ED C4 EA FF                  call 0x1404d3c08
0062771B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00627720  40 32 ED                        xor bpl, bpl
00627723  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00627728  40 38 2D 89 D1 8D 00            cmp byte ptr [rip + 0x8dd189], bpl
0062772F  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00627734  75 0C                           jne 0x140627742
00627736  F7 05 40 D2 8D 00 00 08 00 00   test dword ptr [rip + 0x8dd240], 0x800
00627740  74 13                           je 0x140627755
00627742  48 8D 0D 37 C7 8D 00            lea rcx, [rip + 0x8dc737]
00627749  E8 D2 EE BE FF                  call 0x140216620
0062774E  40 8A E8                        mov bpl, al
00627751  84 C0                           test al, al
00627753  74 39                           je 0x14062778e
00627755  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00627759  48 8B 1F                        mov rbx, qword ptr [rdi]
0062775C  EB 1A                           jmp 0x140627778
0062775E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00627762  48 85 C0                        test rax, rax
00627765  74 0E                           je 0x140627775
00627767  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062776B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00627770  E8 5B 33 09 00                  call 0x1406baad0
00627775  48 8B 1B                        mov rbx, qword ptr [rbx]
00627778  48 3B DF                        cmp rbx, rdi
0062777B  75 E1                           jne 0x14062775e
0062777D  40 84 ED                        test bpl, bpl
00627780  74 0C                           je 0x14062778e
00627782  48 8D 0D F7 C6 8D 00            lea rcx, [rip + 0x8dc6f7]
00627789  E8 F2 26 D2 FF                  call 0x140349e80
0062778E  41 8A D6                        mov dl, r14b
00627791  49 8B CF                        mov rcx, r15
00627794  E8 87 47 E8 FF                  call 0x1404abf20
00627799  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0062779E  48 85 F6                        test rsi, rsi
006277A1  74 64                           je 0x140627807
006277A3  40 32 FF                        xor dil, dil
006277A6  40 38 3D 0B D1 8D 00            cmp byte ptr [rip + 0x8dd10b], dil
006277AD  75 0C                           jne 0x1406277bb
006277AF  F7 05 C7 D1 8D 00 00 08 00 00   test dword ptr [rip + 0x8dd1c7], 0x800
006277B9  74 13                           je 0x1406277ce
006277BB  48 8D 0D BE C6 8D 00            lea rcx, [rip + 0x8dc6be]
006277C2  E8 59 EE BE FF                  call 0x140216620
006277C7  40 8A F8                        mov dil, al
006277CA  84 C0                           test al, al
006277CC  74 39                           je 0x140627807
006277CE  48 83 C6 30                     add rsi, 0x30
006277D2  48 8B 1E                        mov rbx, qword ptr [rsi]
006277D5  EB 1A                           jmp 0x1406277f1
006277D7  48 8D 43 F0                     lea rax, [rbx - 0x10]
006277DB  48 85 C0                        test rax, rax
006277DE  74 0E                           je 0x1406277ee
006277E0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006277E4  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006277E9  E8 E2 32 09 00                  call 0x1406baad0
006277EE  48 8B 1B                        mov rbx, qword ptr [rbx]
006277F1  48 3B DE                        cmp rbx, rsi
006277F4  75 E1                           jne 0x1406277d7
006277F6  40 84 FF                        test dil, dil
006277F9  74 0C                           je 0x140627807
006277FB  48 8D 0D 7E C6 8D 00            lea rcx, [rip + 0x8dc67e]
00627802  E8 79 26 D2 FF                  call 0x140349e80
00627807  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0062780C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00627811  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00627816  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062781B  48 83 C4 40                     add rsp, 0x40
0062781F  41 5F                           pop r15
00627821  41 5E                           pop r14
00627823  5F                              pop rdi
00627824  C3                              ret
00627825  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoAllocateErrorLogEntryWrapper(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
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
    result = DifGetAPIThunkContextById(368, a2, a3, a4);
    if (result == 0) goto loc_0062778E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00627712;
    v_stack_m38 = v_stack_p0;
    goto loc_00627720;
loc_00627712:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9294217)) != 0) goto loc_00627742;
    if (((*(unsigned int *)(v_rip + 9294400)) & (0x800ULL)) == 0) goto loc_00627755;
loc_00627742:
    result = ExAcquireRundownProtection(v_rip + 9291575, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062778E;
loc_00627755:
    goto loc_00627778;
loc_0062775E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00627778:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062775E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9291511;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoAllocateErrorLogEntry(a1, a2, a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00627807;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9294091)) != 0) goto loc_006277BB;
    if (((*(unsigned int *)(v_rip + 9294279)) & (0x800ULL)) == 0) goto loc_006277CE;
loc_006277BB:
    result = ExAcquireRundownProtection(v_rip + 9291454, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00627807;
loc_006277CE:
    v_rsi = (result) + (48);
    goto loc_006277F1;
loc_006277D7:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006277F1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006277D7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9291390;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m20;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoAllocateErrorLogEntryWrapper(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
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
    result = DifGetAPIThunkContextById(368, Arg2, a3, a4);
    if (result == 0) goto loc_0062778E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00627712;
    v_stack_m38 = v_stack_p0;
    goto loc_00627720;
loc_00627712:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8DD189)) != 0) goto loc_00627742;
    if (((*(uint32_t *)(v_rip + 0x8DD240)) & (0x800ULL)) == 0) goto loc_00627755;
loc_00627742:
    result = ExAcquireRundownProtection(v_rip + 9291575, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062778E;
loc_00627755:
    goto loc_00627778;
loc_0062775E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00627778:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062775E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9291511;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = IoAllocateErrorLogEntry(Arg1, Arg2, a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00627807;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DD10B)) != 0) goto loc_006277BB;
    if (((*(uint32_t *)(v_rip + 0x8DD1C7)) & (0x800ULL)) == 0) goto loc_006277CE;
loc_006277BB:
    result = ExAcquireRundownProtection(v_rip + 9291454, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00627807;
loc_006277CE:
    local_rsi = (result) + (48);
    goto loc_006277F1;
loc_006277D7:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006277F1:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006277D7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9291390;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006276C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006276C0[BB_006276C0]
  bb_006276FF[BB_006276FF]
  bb_00627706[BB_00627706]
  bb_00627712[BB_00627712]
  bb_00627716[BB_00627716]
  bb_00627720[BB_00627720]
  bb_00627736[BB_00627736]
  bb_00627742[BB_00627742]
  bb_00627755[BB_00627755]
  bb_0062775E[BB_0062775E]
  bb_00627767[BB_00627767]
  bb_00627775[BB_00627775]
  bb_00627778[BB_00627778]
  bb_0062777D[BB_0062777D]
  bb_00627782[BB_00627782]
  bb_0062778E[BB_0062778E]
  bb_006277A3[BB_006277A3]
  bb_006277AF[BB_006277AF]
  bb_006277BB[BB_006277BB]
  bb_006277CE[BB_006277CE]
  bb_006277D7[BB_006277D7]
  bb_006277E0[BB_006277E0]
  bb_006277EE[BB_006277EE]
  bb_006277F1[BB_006277F1]
  bb_006277F6[BB_006277F6]
  bb_006277FB[BB_006277FB]
  bb_00627807[BB_00627807]
  bb_00627825[BB_00627825]
  bb_006276C0 -->|branch| bb_0062778E
  bb_006276C0 -->|fallthrough| bb_006276FF
  bb_006276FF -->|branch| bb_00627712
  bb_006276FF -->|fallthrough| bb_00627706
  bb_00627706 -->|branch| bb_00627720
  bb_00627712 -->|branch| bb_00627720
  bb_00627712 -->|fallthrough| bb_00627716
  bb_00627716 -->|flow| bb_00627720
  bb_00627720 -->|branch| bb_00627742
  bb_00627720 -->|fallthrough| bb_00627736
  bb_00627736 -->|branch| bb_00627755
  bb_00627736 -->|fallthrough| bb_00627742
  bb_00627742 -->|branch| bb_0062778E
  bb_00627742 -->|fallthrough| bb_00627755
  bb_00627755 -->|branch| bb_00627778
  bb_0062775E -->|branch| bb_00627775
  bb_0062775E -->|fallthrough| bb_00627767
  bb_00627767 -->|flow| bb_00627775
  bb_00627775 -->|flow| bb_00627778
  bb_00627778 -->|branch| bb_0062775E
  bb_00627778 -->|fallthrough| bb_0062777D
  bb_0062777D -->|branch| bb_0062778E
  bb_0062777D -->|fallthrough| bb_00627782
  bb_00627782 -->|flow| bb_0062778E
  bb_0062778E -->|branch| bb_00627807
  bb_0062778E -->|fallthrough| bb_006277A3
  bb_006277A3 -->|branch| bb_006277BB
  bb_006277A3 -->|fallthrough| bb_006277AF
  bb_006277AF -->|branch| bb_006277CE
  bb_006277AF -->|fallthrough| bb_006277BB
  bb_006277BB -->|branch| bb_00627807
  bb_006277BB -->|fallthrough| bb_006277CE
  bb_006277CE -->|branch| bb_006277F1
  bb_006277D7 -->|branch| bb_006277EE
  bb_006277D7 -->|fallthrough| bb_006277E0
  bb_006277E0 -->|flow| bb_006277EE
  bb_006277EE -->|flow| bb_006277F1
  bb_006277F1 -->|branch| bb_006277D7
  bb_006277F1 -->|fallthrough| bb_006277F6
  bb_006277F6 -->|branch| bb_00627807
  bb_006277F6 -->|fallthrough| bb_006277FB
  bb_006277FB -->|flow| bb_00627807
```
