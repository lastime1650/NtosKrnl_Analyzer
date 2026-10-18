# DifIoRaiseHardErrorWrapper

- RVA: `0x0062BD80`–`0x0062BEF2` (길이 `370` bytes)
- VA: `0x000000014062BD80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `101`개 명령, `370/370` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062BDB6` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062BDDE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062BE16` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062BE3D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062BE56` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062BE64` → [IoRaiseHardError](../22/IoRaiseHardError_function_002230D0.md) (function, `0x002230D0`)
- `0x0062BE8D` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062BEB4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062BECD` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062BDF0` → RVA `0x00F048B8` (`.data`; read)
- `0x0062BE03` → RVA `0x00F04980` (`.data`; read)
- `0x0062BE0F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062BD80  48 8B C4                        mov rax, rsp
0062BD83  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062BD87  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062BD8B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062BD8F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062BD93  41 54                           push r12
0062BD95  41 56                           push r14
0062BD97  41 57                           push r15
0062BD99  48 83 EC 40                     sub rsp, 0x40
0062BD9D  0F 57 C0                        xorps xmm0, xmm0
0062BDA0  4C 8B E1                        mov r12, rcx
0062BDA3  B9 43 01 00 00                  mov ecx, 0x143
0062BDA8  4D 8B F0                        mov r14, r8
0062BDAB  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062BDAF  4C 8B FA                        mov r15, rdx
0062BDB2  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062BDB6  E8 79 9C E6 FF                  call 0x140495a34
0062BDBB  48 8B F0                        mov rsi, rax
0062BDBE  48 85 C0                        test rax, rax
0062BDC1  0F 84 94 00 00 00               je 0x14062be5b
0062BDC7  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062BDCA  A8 18                           test al, 0x18
0062BDCC  74 0C                           je 0x14062bdda
0062BDCE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062BDD3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062BDD8  EB 0E                           jmp 0x14062bde8
0062BDDA  A8 04                           test al, 4
0062BDDC  74 0A                           je 0x14062bde8
0062BDDE  E8 25 7E EA FF                  call 0x1404d3c08
0062BDE3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062BDE8  40 32 ED                        xor bpl, bpl
0062BDEB  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0062BDF0  40 38 2D C1 8A 8D 00            cmp byte ptr [rip + 0x8d8ac1], bpl
0062BDF7  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062BDFC  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0062BE01  75 0C                           jne 0x14062be0f
0062BE03  F7 05 73 8B 8D 00 00 08 00 00   test dword ptr [rip + 0x8d8b73], 0x800
0062BE0D  74 13                           je 0x14062be22
0062BE0F  48 8D 0D 6A 80 8D 00            lea rcx, [rip + 0x8d806a]
0062BE16  E8 05 A8 BE FF                  call 0x140216620
0062BE1B  40 8A E8                        mov bpl, al
0062BE1E  84 C0                           test al, al
0062BE20  74 39                           je 0x14062be5b
0062BE22  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062BE26  48 8B 1F                        mov rbx, qword ptr [rdi]
0062BE29  EB 1A                           jmp 0x14062be45
0062BE2B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062BE2F  48 85 C0                        test rax, rax
0062BE32  74 0E                           je 0x14062be42
0062BE34  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062BE38  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062BE3D  E8 8E EC 08 00                  call 0x1406baad0
0062BE42  48 8B 1B                        mov rbx, qword ptr [rbx]
0062BE45  48 3B DF                        cmp rbx, rdi
0062BE48  75 E1                           jne 0x14062be2b
0062BE4A  40 84 ED                        test bpl, bpl
0062BE4D  74 0C                           je 0x14062be5b
0062BE4F  48 8D 0D 2A 80 8D 00            lea rcx, [rip + 0x8d802a]
0062BE56  E8 25 E0 D1 FF                  call 0x140349e80
0062BE5B  4D 8B C6                        mov r8, r14
0062BE5E  49 8B D7                        mov rdx, r15
0062BE61  49 8B CC                        mov rcx, r12
0062BE64  E8 67 72 BF FF                  call 0x1402230d0
0062BE69  48 85 F6                        test rsi, rsi
0062BE6C  74 64                           je 0x14062bed2
0062BE6E  40 32 FF                        xor dil, dil
0062BE71  40 38 3D 40 8A 8D 00            cmp byte ptr [rip + 0x8d8a40], dil
0062BE78  75 0C                           jne 0x14062be86
0062BE7A  F7 05 FC 8A 8D 00 00 08 00 00   test dword ptr [rip + 0x8d8afc], 0x800
0062BE84  74 13                           je 0x14062be99
0062BE86  48 8D 0D F3 7F 8D 00            lea rcx, [rip + 0x8d7ff3]
0062BE8D  E8 8E A7 BE FF                  call 0x140216620
0062BE92  40 8A F8                        mov dil, al
0062BE95  84 C0                           test al, al
0062BE97  74 39                           je 0x14062bed2
0062BE99  48 83 C6 30                     add rsi, 0x30
0062BE9D  48 8B 1E                        mov rbx, qword ptr [rsi]
0062BEA0  EB 1A                           jmp 0x14062bebc
0062BEA2  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062BEA6  48 85 C0                        test rax, rax
0062BEA9  74 0E                           je 0x14062beb9
0062BEAB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062BEAF  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062BEB4  E8 17 EC 08 00                  call 0x1406baad0
0062BEB9  48 8B 1B                        mov rbx, qword ptr [rbx]
0062BEBC  48 3B DE                        cmp rbx, rsi
0062BEBF  75 E1                           jne 0x14062bea2
0062BEC1  40 84 FF                        test dil, dil
0062BEC4  74 0C                           je 0x14062bed2
0062BEC6  48 8D 0D B3 7F 8D 00            lea rcx, [rip + 0x8d7fb3]
0062BECD  E8 AE DF D1 FF                  call 0x140349e80
0062BED2  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062BED7  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062BEDC  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062BEE1  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0062BEE6  48 83 C4 40                     add rsp, 0x40
0062BEEA  41 5F                           pop r15
0062BEEC  41 5E                           pop r14
0062BEEE  41 5C                           pop r12
0062BEF0  C3                              ret
0062BEF1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoRaiseHardErrorWrapper(__int64 a1, __int64 a2, __int64 a3)
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
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(323, a2, a3, a4);
    if (result == 0) goto loc_0062BE5B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062BDDA;
    v_stack_m38 = v_stack_p0;
    goto loc_0062BDE8;
loc_0062BDDA:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = a1;
    v_stack_m28 = a2;
    v_stack_m30 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9276097)) != 0) goto loc_0062BE0F;
    if (((*(unsigned int *)(v_rip + 9276275)) & (0x800ULL)) == 0) goto loc_0062BE22;
loc_0062BE0F:
    result = ExAcquireRundownProtection(v_rip + 9273450, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062BE5B;
loc_0062BE22:
    goto loc_0062BE45;
loc_0062BE2B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062BE45:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062BE2B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9273386;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoRaiseHardError(a1, a2, a3, a4);
    if (result == 0) goto loc_0062BED2;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9275968)) != 0) goto loc_0062BE86;
    if (((*(unsigned int *)(v_rip + 9276156)) & (0x800ULL)) == 0) goto loc_0062BE99;
loc_0062BE86:
    result = ExAcquireRundownProtection(v_rip + 9273331, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062BED2;
loc_0062BE99:
    v_rsi = (result) + (48);
    goto loc_0062BEBC;
loc_0062BEA2:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062BEBC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062BEA2;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9273267;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoRaiseHardErrorWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
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
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(323, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062BE5B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062BDDA;
    v_stack_m38 = v_stack_p0;
    goto loc_0062BDE8;
loc_0062BDDA:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = Arg1;
    v_stack_m28 = Arg2;
    v_stack_m30 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D8AC1)) != 0) goto loc_0062BE0F;
    if (((*(uint32_t *)(v_rip + 0x8D8B73)) & (0x800ULL)) == 0) goto loc_0062BE22;
loc_0062BE0F:
    result = ExAcquireRundownProtection(v_rip + 9273450, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062BE5B;
loc_0062BE22:
    goto loc_0062BE45;
loc_0062BE2B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062BE45:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062BE2B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9273386;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = IoRaiseHardError(Arg1, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062BED2;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D8A40)) != 0) goto loc_0062BE86;
    if (((*(uint32_t *)(v_rip + 0x8D8AFC)) & (0x800ULL)) == 0) goto loc_0062BE99;
loc_0062BE86:
    result = ExAcquireRundownProtection(v_rip + 9273331, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062BED2;
loc_0062BE99:
    local_rsi = (result) + (48);
    goto loc_0062BEBC;
loc_0062BEA2:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062BEBC:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062BEA2;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9273267;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062BD80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062BD80[BB_0062BD80]
  bb_0062BDC7[BB_0062BDC7]
  bb_0062BDCE[BB_0062BDCE]
  bb_0062BDDA[BB_0062BDDA]
  bb_0062BDDE[BB_0062BDDE]
  bb_0062BDE8[BB_0062BDE8]
  bb_0062BE03[BB_0062BE03]
  bb_0062BE0F[BB_0062BE0F]
  bb_0062BE22[BB_0062BE22]
  bb_0062BE2B[BB_0062BE2B]
  bb_0062BE34[BB_0062BE34]
  bb_0062BE42[BB_0062BE42]
  bb_0062BE45[BB_0062BE45]
  bb_0062BE4A[BB_0062BE4A]
  bb_0062BE4F[BB_0062BE4F]
  bb_0062BE5B[BB_0062BE5B]
  bb_0062BE6E[BB_0062BE6E]
  bb_0062BE7A[BB_0062BE7A]
  bb_0062BE86[BB_0062BE86]
  bb_0062BE99[BB_0062BE99]
  bb_0062BEA2[BB_0062BEA2]
  bb_0062BEAB[BB_0062BEAB]
  bb_0062BEB9[BB_0062BEB9]
  bb_0062BEBC[BB_0062BEBC]
  bb_0062BEC1[BB_0062BEC1]
  bb_0062BEC6[BB_0062BEC6]
  bb_0062BED2[BB_0062BED2]
  bb_0062BEF1[BB_0062BEF1]
  bb_0062BD80 -->|branch| bb_0062BE5B
  bb_0062BD80 -->|fallthrough| bb_0062BDC7
  bb_0062BDC7 -->|branch| bb_0062BDDA
  bb_0062BDC7 -->|fallthrough| bb_0062BDCE
  bb_0062BDCE -->|branch| bb_0062BDE8
  bb_0062BDDA -->|branch| bb_0062BDE8
  bb_0062BDDA -->|fallthrough| bb_0062BDDE
  bb_0062BDDE -->|flow| bb_0062BDE8
  bb_0062BDE8 -->|branch| bb_0062BE0F
  bb_0062BDE8 -->|fallthrough| bb_0062BE03
  bb_0062BE03 -->|branch| bb_0062BE22
  bb_0062BE03 -->|fallthrough| bb_0062BE0F
  bb_0062BE0F -->|branch| bb_0062BE5B
  bb_0062BE0F -->|fallthrough| bb_0062BE22
  bb_0062BE22 -->|branch| bb_0062BE45
  bb_0062BE2B -->|branch| bb_0062BE42
  bb_0062BE2B -->|fallthrough| bb_0062BE34
  bb_0062BE34 -->|flow| bb_0062BE42
  bb_0062BE42 -->|flow| bb_0062BE45
  bb_0062BE45 -->|branch| bb_0062BE2B
  bb_0062BE45 -->|fallthrough| bb_0062BE4A
  bb_0062BE4A -->|branch| bb_0062BE5B
  bb_0062BE4A -->|fallthrough| bb_0062BE4F
  bb_0062BE4F -->|flow| bb_0062BE5B
  bb_0062BE5B -->|branch| bb_0062BED2
  bb_0062BE5B -->|fallthrough| bb_0062BE6E
  bb_0062BE6E -->|branch| bb_0062BE86
  bb_0062BE6E -->|fallthrough| bb_0062BE7A
  bb_0062BE7A -->|branch| bb_0062BE99
  bb_0062BE7A -->|fallthrough| bb_0062BE86
  bb_0062BE86 -->|branch| bb_0062BED2
  bb_0062BE86 -->|fallthrough| bb_0062BE99
  bb_0062BE99 -->|branch| bb_0062BEBC
  bb_0062BEA2 -->|branch| bb_0062BEB9
  bb_0062BEA2 -->|fallthrough| bb_0062BEAB
  bb_0062BEAB -->|flow| bb_0062BEB9
  bb_0062BEB9 -->|flow| bb_0062BEBC
  bb_0062BEBC -->|branch| bb_0062BEA2
  bb_0062BEBC -->|fallthrough| bb_0062BEC1
  bb_0062BEC1 -->|branch| bb_0062BED2
  bb_0062BEC1 -->|fallthrough| bb_0062BEC6
  bb_0062BEC6 -->|flow| bb_0062BED2
```
