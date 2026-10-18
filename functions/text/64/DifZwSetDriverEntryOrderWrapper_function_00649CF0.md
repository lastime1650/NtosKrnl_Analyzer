# DifZwSetDriverEntryOrderWrapper

- RVA: `0x00649CF0`–`0x00649E54` (길이 `356` bytes)
- VA: `0x0000000140649CF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `356/356` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00649D1E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00649D46` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00649D79` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00649DA0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00649DB9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00649DC4` → [ZwSetDriverEntryOrder](../6B/ZwSetDriverEntryOrder_function_006B04D0.md) (function, `0x006B04D0`)
- `0x00649DF1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00649E18` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00649E31` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00649D58` → RVA `0x00F048B8` (`.data`; read)
- `0x00649D66` → RVA `0x00F04980` (`.data`; read)
- `0x00649D72` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00649CF0  48 8B C4                        mov rax, rsp
00649CF3  48 89 58 08                     mov qword ptr [rax + 8], rbx
00649CF7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00649CFB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00649CFF  57                              push rdi
00649D00  41 56                           push r14
00649D02  41 57                           push r15
00649D04  48 83 EC 40                     sub rsp, 0x40
00649D08  0F 57 C0                        xorps xmm0, xmm0
00649D0B  4C 8B F9                        mov r15, rcx
00649D0E  B9 16 00 00 00                  mov ecx, 0x16
00649D13  44 8B F2                        mov r14d, edx
00649D16  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
00649D1A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00649D1E  E8 11 BD E4 FF                  call 0x140495a34
00649D23  48 8B F0                        mov rsi, rax
00649D26  48 85 C0                        test rax, rax
00649D29  0F 84 8F 00 00 00               je 0x140649dbe
00649D2F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00649D32  A8 18                           test al, 0x18
00649D34  74 0C                           je 0x140649d42
00649D36  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00649D3B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00649D40  EB 0E                           jmp 0x140649d50
00649D42  A8 04                           test al, 4
00649D44  74 0A                           je 0x140649d50
00649D46  E8 BD 9E E8 FF                  call 0x1404d3c08
00649D4B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00649D50  40 32 ED                        xor bpl, bpl
00649D53  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00649D58  40 38 2D 59 AB 8B 00            cmp byte ptr [rip + 0x8bab59], bpl
00649D5F  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00649D64  75 0C                           jne 0x140649d72
00649D66  F7 05 10 AC 8B 00 00 08 00 00   test dword ptr [rip + 0x8bac10], 0x800
00649D70  74 13                           je 0x140649d85
00649D72  48 8D 0D 07 A1 8B 00            lea rcx, [rip + 0x8ba107]
00649D79  E8 A2 C8 BC FF                  call 0x140216620
00649D7E  40 8A E8                        mov bpl, al
00649D81  84 C0                           test al, al
00649D83  74 39                           je 0x140649dbe
00649D85  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00649D89  48 8B 1F                        mov rbx, qword ptr [rdi]
00649D8C  EB 1A                           jmp 0x140649da8
00649D8E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00649D92  48 85 C0                        test rax, rax
00649D95  74 0E                           je 0x140649da5
00649D97  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00649D9B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00649DA0  E8 2B 0D 07 00                  call 0x1406baad0
00649DA5  48 8B 1B                        mov rbx, qword ptr [rbx]
00649DA8  48 3B DF                        cmp rbx, rdi
00649DAB  75 E1                           jne 0x140649d8e
00649DAD  40 84 ED                        test bpl, bpl
00649DB0  74 0C                           je 0x140649dbe
00649DB2  48 8D 0D C7 A0 8B 00            lea rcx, [rip + 0x8ba0c7]
00649DB9  E8 C2 00 D0 FF                  call 0x140349e80
00649DBE  41 8B D6                        mov edx, r14d
00649DC1  49 8B CF                        mov rcx, r15
00649DC4  E8 07 67 06 00                  call 0x1406b04d0
00649DC9  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00649DCD  48 85 F6                        test rsi, rsi
00649DD0  74 64                           je 0x140649e36
00649DD2  40 32 FF                        xor dil, dil
00649DD5  40 38 3D DC AA 8B 00            cmp byte ptr [rip + 0x8baadc], dil
00649DDC  75 0C                           jne 0x140649dea
00649DDE  F7 05 98 AB 8B 00 00 08 00 00   test dword ptr [rip + 0x8bab98], 0x800
00649DE8  74 13                           je 0x140649dfd
00649DEA  48 8D 0D 8F A0 8B 00            lea rcx, [rip + 0x8ba08f]
00649DF1  E8 2A C8 BC FF                  call 0x140216620
00649DF6  40 8A F8                        mov dil, al
00649DF9  84 C0                           test al, al
00649DFB  74 39                           je 0x140649e36
00649DFD  48 83 C6 30                     add rsi, 0x30
00649E01  48 8B 1E                        mov rbx, qword ptr [rsi]
00649E04  EB 1A                           jmp 0x140649e20
00649E06  48 8D 43 F0                     lea rax, [rbx - 0x10]
00649E0A  48 85 C0                        test rax, rax
00649E0D  74 0E                           je 0x140649e1d
00649E0F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00649E13  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00649E18  E8 B3 0C 07 00                  call 0x1406baad0
00649E1D  48 8B 1B                        mov rbx, qword ptr [rbx]
00649E20  48 3B DE                        cmp rbx, rsi
00649E23  75 E1                           jne 0x140649e06
00649E25  40 84 FF                        test dil, dil
00649E28  74 0C                           je 0x140649e36
00649E2A  48 8D 0D 4F A0 8B 00            lea rcx, [rip + 0x8ba04f]
00649E31  E8 4A 00 D0 FF                  call 0x140349e80
00649E36  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00649E3A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00649E3F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00649E44  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00649E49  48 83 C4 40                     add rsp, 0x40
00649E4D  41 5F                           pop r15
00649E4F  41 5E                           pop r14
00649E51  5F                              pop rdi
00649E52  C3                              ret
00649E53  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwSetDriverEntryOrderWrapper(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
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
    result = DifGetAPIThunkContextById(22, a2, a3, a4);
    if (result == 0) goto loc_00649DBE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00649D42;
    v_stack_m38 = v_stack_p0;
    goto loc_00649D50;
loc_00649D42:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9153369)) != 0) goto loc_00649D72;
    if (((*(unsigned int *)(v_rip + 9153552)) & (0x800ULL)) == 0) goto loc_00649D85;
loc_00649D72:
    result = ExAcquireRundownProtection(v_rip + 9150727, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00649DBE;
loc_00649D85:
    goto loc_00649DA8;
loc_00649D8E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00649DA8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00649D8E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9150663;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwSetDriverEntryOrder(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00649E36;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9153244)) != 0) goto loc_00649DEA;
    if (((*(unsigned int *)(v_rip + 9153432)) & (0x800ULL)) == 0) goto loc_00649DFD;
loc_00649DEA:
    result = ExAcquireRundownProtection(v_rip + 9150607, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00649E36;
loc_00649DFD:
    v_rsi = (result) + (48);
    goto loc_00649E20;
loc_00649E06:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00649E20:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00649E06;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9150543;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwSetDriverEntryOrderWrapper(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
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
    result = DifGetAPIThunkContextById(22, Arg2, a3, a4);
    if (result == 0) goto loc_00649DBE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00649D42;
    v_stack_m38 = v_stack_p0;
    goto loc_00649D50;
loc_00649D42:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8BAB59)) != 0) goto loc_00649D72;
    if (((*(uint32_t *)(v_rip + 0x8BAC10)) & (0x800ULL)) == 0) goto loc_00649D85;
loc_00649D72:
    result = ExAcquireRundownProtection(v_rip + 9150727, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00649DBE;
loc_00649D85:
    goto loc_00649DA8;
loc_00649D8E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00649DA8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00649D8E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9150663;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwSetDriverEntryOrder(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00649E36;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BAADC)) != 0) goto loc_00649DEA;
    if (((*(uint32_t *)(v_rip + 0x8BAB98)) & (0x800ULL)) == 0) goto loc_00649DFD;
loc_00649DEA:
    result = ExAcquireRundownProtection(v_rip + 9150607, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00649E36;
loc_00649DFD:
    local_rsi = (result) + (48);
    goto loc_00649E20;
loc_00649E06:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
loc_00649E20:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00649E06;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9150543;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00649CF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00649CF0[BB_00649CF0]
  bb_00649D2F[BB_00649D2F]
  bb_00649D36[BB_00649D36]
  bb_00649D42[BB_00649D42]
  bb_00649D46[BB_00649D46]
  bb_00649D50[BB_00649D50]
  bb_00649D66[BB_00649D66]
  bb_00649D72[BB_00649D72]
  bb_00649D85[BB_00649D85]
  bb_00649D8E[BB_00649D8E]
  bb_00649D97[BB_00649D97]
  bb_00649DA5[BB_00649DA5]
  bb_00649DA8[BB_00649DA8]
  bb_00649DAD[BB_00649DAD]
  bb_00649DB2[BB_00649DB2]
  bb_00649DBE[BB_00649DBE]
  bb_00649DD2[BB_00649DD2]
  bb_00649DDE[BB_00649DDE]
  bb_00649DEA[BB_00649DEA]
  bb_00649DFD[BB_00649DFD]
  bb_00649E06[BB_00649E06]
  bb_00649E0F[BB_00649E0F]
  bb_00649E1D[BB_00649E1D]
  bb_00649E20[BB_00649E20]
  bb_00649E25[BB_00649E25]
  bb_00649E2A[BB_00649E2A]
  bb_00649E36[BB_00649E36]
  bb_00649E53[BB_00649E53]
  bb_00649CF0 -->|branch| bb_00649DBE
  bb_00649CF0 -->|fallthrough| bb_00649D2F
  bb_00649D2F -->|branch| bb_00649D42
  bb_00649D2F -->|fallthrough| bb_00649D36
  bb_00649D36 -->|branch| bb_00649D50
  bb_00649D42 -->|branch| bb_00649D50
  bb_00649D42 -->|fallthrough| bb_00649D46
  bb_00649D46 -->|flow| bb_00649D50
  bb_00649D50 -->|branch| bb_00649D72
  bb_00649D50 -->|fallthrough| bb_00649D66
  bb_00649D66 -->|branch| bb_00649D85
  bb_00649D66 -->|fallthrough| bb_00649D72
  bb_00649D72 -->|branch| bb_00649DBE
  bb_00649D72 -->|fallthrough| bb_00649D85
  bb_00649D85 -->|branch| bb_00649DA8
  bb_00649D8E -->|branch| bb_00649DA5
  bb_00649D8E -->|fallthrough| bb_00649D97
  bb_00649D97 -->|flow| bb_00649DA5
  bb_00649DA5 -->|flow| bb_00649DA8
  bb_00649DA8 -->|branch| bb_00649D8E
  bb_00649DA8 -->|fallthrough| bb_00649DAD
  bb_00649DAD -->|branch| bb_00649DBE
  bb_00649DAD -->|fallthrough| bb_00649DB2
  bb_00649DB2 -->|flow| bb_00649DBE
  bb_00649DBE -->|branch| bb_00649E36
  bb_00649DBE -->|fallthrough| bb_00649DD2
  bb_00649DD2 -->|branch| bb_00649DEA
  bb_00649DD2 -->|fallthrough| bb_00649DDE
  bb_00649DDE -->|branch| bb_00649DFD
  bb_00649DDE -->|fallthrough| bb_00649DEA
  bb_00649DEA -->|branch| bb_00649E36
  bb_00649DEA -->|fallthrough| bb_00649DFD
  bb_00649DFD -->|branch| bb_00649E20
  bb_00649E06 -->|branch| bb_00649E1D
  bb_00649E06 -->|fallthrough| bb_00649E0F
  bb_00649E0F -->|flow| bb_00649E1D
  bb_00649E1D -->|flow| bb_00649E20
  bb_00649E20 -->|branch| bb_00649E06
  bb_00649E20 -->|fallthrough| bb_00649E25
  bb_00649E25 -->|branch| bb_00649E36
  bb_00649E25 -->|fallthrough| bb_00649E2A
  bb_00649E2A -->|flow| bb_00649E36
```
