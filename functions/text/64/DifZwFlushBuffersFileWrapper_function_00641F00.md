# DifZwFlushBuffersFileWrapper

- RVA: `0x00641F00`–`0x00642064` (길이 `356` bytes)
- VA: `0x0000000140641F00`
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
- `0x00641F2E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00641F56` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00641F89` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00641FB0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641FC9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00641FD4` → [ZwFlushBuffersFile](../6A/ZwFlushBuffersFile_function_006ADA30.md) (function, `0x006ADA30`)
- `0x00642001` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00642028` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00642041` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00641F68` → RVA `0x00F048B8` (`.data`; read)
- `0x00641F76` → RVA `0x00F04980` (`.data`; read)
- `0x00641F82` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00641F00  48 8B C4                        mov rax, rsp
00641F03  48 89 58 08                     mov qword ptr [rax + 8], rbx
00641F07  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00641F0B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00641F0F  57                              push rdi
00641F10  41 56                           push r14
00641F12  41 57                           push r15
00641F14  48 83 EC 40                     sub rsp, 0x40
00641F18  0F 57 C0                        xorps xmm0, xmm0
00641F1B  4C 8B F9                        mov r15, rcx
00641F1E  B9 66 00 00 00                  mov ecx, 0x66
00641F23  4C 8B F2                        mov r14, rdx
00641F26  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
00641F2A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00641F2E  E8 01 3B E5 FF                  call 0x140495a34
00641F33  48 8B F0                        mov rsi, rax
00641F36  48 85 C0                        test rax, rax
00641F39  0F 84 8F 00 00 00               je 0x140641fce
00641F3F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00641F42  A8 18                           test al, 0x18
00641F44  74 0C                           je 0x140641f52
00641F46  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00641F4B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00641F50  EB 0E                           jmp 0x140641f60
00641F52  A8 04                           test al, 4
00641F54  74 0A                           je 0x140641f60
00641F56  E8 AD 1C E9 FF                  call 0x1404d3c08
00641F5B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00641F60  40 32 ED                        xor bpl, bpl
00641F63  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00641F68  40 38 2D 49 29 8C 00            cmp byte ptr [rip + 0x8c2949], bpl
00641F6F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00641F74  75 0C                           jne 0x140641f82
00641F76  F7 05 00 2A 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2a00], 0x800
00641F80  74 13                           je 0x140641f95
00641F82  48 8D 0D F7 1E 8C 00            lea rcx, [rip + 0x8c1ef7]
00641F89  E8 92 46 BD FF                  call 0x140216620
00641F8E  40 8A E8                        mov bpl, al
00641F91  84 C0                           test al, al
00641F93  74 39                           je 0x140641fce
00641F95  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00641F99  48 8B 1F                        mov rbx, qword ptr [rdi]
00641F9C  EB 1A                           jmp 0x140641fb8
00641F9E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00641FA2  48 85 C0                        test rax, rax
00641FA5  74 0E                           je 0x140641fb5
00641FA7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00641FAB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00641FB0  E8 1B 8B 07 00                  call 0x1406baad0
00641FB5  48 8B 1B                        mov rbx, qword ptr [rbx]
00641FB8  48 3B DF                        cmp rbx, rdi
00641FBB  75 E1                           jne 0x140641f9e
00641FBD  40 84 ED                        test bpl, bpl
00641FC0  74 0C                           je 0x140641fce
00641FC2  48 8D 0D B7 1E 8C 00            lea rcx, [rip + 0x8c1eb7]
00641FC9  E8 B2 7E D0 FF                  call 0x140349e80
00641FCE  49 8B D6                        mov rdx, r14
00641FD1  49 8B CF                        mov rcx, r15
00641FD4  E8 57 BA 06 00                  call 0x1406ada30
00641FD9  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00641FDD  48 85 F6                        test rsi, rsi
00641FE0  74 64                           je 0x140642046
00641FE2  40 32 FF                        xor dil, dil
00641FE5  40 38 3D CC 28 8C 00            cmp byte ptr [rip + 0x8c28cc], dil
00641FEC  75 0C                           jne 0x140641ffa
00641FEE  F7 05 88 29 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2988], 0x800
00641FF8  74 13                           je 0x14064200d
00641FFA  48 8D 0D 7F 1E 8C 00            lea rcx, [rip + 0x8c1e7f]
00642001  E8 1A 46 BD FF                  call 0x140216620
00642006  40 8A F8                        mov dil, al
00642009  84 C0                           test al, al
0064200B  74 39                           je 0x140642046
0064200D  48 83 C6 30                     add rsi, 0x30
00642011  48 8B 1E                        mov rbx, qword ptr [rsi]
00642014  EB 1A                           jmp 0x140642030
00642016  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064201A  48 85 C0                        test rax, rax
0064201D  74 0E                           je 0x14064202d
0064201F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00642023  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00642028  E8 A3 8A 07 00                  call 0x1406baad0
0064202D  48 8B 1B                        mov rbx, qword ptr [rbx]
00642030  48 3B DE                        cmp rbx, rsi
00642033  75 E1                           jne 0x140642016
00642035  40 84 FF                        test dil, dil
00642038  74 0C                           je 0x140642046
0064203A  48 8D 0D 3F 1E 8C 00            lea rcx, [rip + 0x8c1e3f]
00642041  E8 3A 7E D0 FF                  call 0x140349e80
00642046  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0064204A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0064204F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00642054  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00642059  48 83 C4 40                     add rsp, 0x40
0064205D  41 5F                           pop r15
0064205F  41 5E                           pop r14
00642061  5F                              pop rdi
00642062  C3                              ret
00642063  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwFlushBuffersFileWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
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
    result = DifGetAPIThunkContextById(102, a2, a3, a4);
    if (result == 0) goto loc_00641FCE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00641F52;
    v_stack_m38 = v_stack_p0;
    goto loc_00641F60;
loc_00641F52:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9185609)) != 0) goto loc_00641F82;
    if (((*(unsigned int *)(v_rip + 9185792)) & (0x800ULL)) == 0) goto loc_00641F95;
loc_00641F82:
    result = ExAcquireRundownProtection(v_rip + 9182967, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00641FCE;
loc_00641F95:
    goto loc_00641FB8;
loc_00641F9E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00641FB8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00641F9E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9182903;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwFlushBuffersFile(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00642046;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9185484)) != 0) goto loc_00641FFA;
    if (((*(unsigned int *)(v_rip + 9185672)) & (0x800ULL)) == 0) goto loc_0064200D;
loc_00641FFA:
    result = ExAcquireRundownProtection(v_rip + 9182847, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00642046;
loc_0064200D:
    v_rsi = (result) + (48);
    goto loc_00642030;
loc_00642016:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00642030:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00642016;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9182783;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwFlushBuffersFileWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
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
    result = DifGetAPIThunkContextById(102, Arg2, a3, a4);
    if (result == 0) goto loc_00641FCE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00641F52;
    v_stack_m38 = v_stack_p0;
    goto loc_00641F60;
loc_00641F52:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8C2949)) != 0) goto loc_00641F82;
    if (((*(uint32_t *)(v_rip + 0x8C2A00)) & (0x800ULL)) == 0) goto loc_00641F95;
loc_00641F82:
    result = ExAcquireRundownProtection(v_rip + 9182967, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00641FCE;
loc_00641F95:
    goto loc_00641FB8;
loc_00641F9E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00641FB8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00641F9E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9182903;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwFlushBuffersFile(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00642046;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C28CC)) != 0) goto loc_00641FFA;
    if (((*(uint32_t *)(v_rip + 0x8C2988)) & (0x800ULL)) == 0) goto loc_0064200D;
loc_00641FFA:
    result = ExAcquireRundownProtection(v_rip + 9182847, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00642046;
loc_0064200D:
    local_rsi = (result) + (48);
    goto loc_00642030;
loc_00642016:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00642030:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00642016;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9182783;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00641F00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00641F00[BB_00641F00]
  bb_00641F3F[BB_00641F3F]
  bb_00641F46[BB_00641F46]
  bb_00641F52[BB_00641F52]
  bb_00641F56[BB_00641F56]
  bb_00641F60[BB_00641F60]
  bb_00641F76[BB_00641F76]
  bb_00641F82[BB_00641F82]
  bb_00641F95[BB_00641F95]
  bb_00641F9E[BB_00641F9E]
  bb_00641FA7[BB_00641FA7]
  bb_00641FB5[BB_00641FB5]
  bb_00641FB8[BB_00641FB8]
  bb_00641FBD[BB_00641FBD]
  bb_00641FC2[BB_00641FC2]
  bb_00641FCE[BB_00641FCE]
  bb_00641FE2[BB_00641FE2]
  bb_00641FEE[BB_00641FEE]
  bb_00641FFA[BB_00641FFA]
  bb_0064200D[BB_0064200D]
  bb_00642016[BB_00642016]
  bb_0064201F[BB_0064201F]
  bb_0064202D[BB_0064202D]
  bb_00642030[BB_00642030]
  bb_00642035[BB_00642035]
  bb_0064203A[BB_0064203A]
  bb_00642046[BB_00642046]
  bb_00642063[BB_00642063]
  bb_00641F00 -->|branch| bb_00641FCE
  bb_00641F00 -->|fallthrough| bb_00641F3F
  bb_00641F3F -->|branch| bb_00641F52
  bb_00641F3F -->|fallthrough| bb_00641F46
  bb_00641F46 -->|branch| bb_00641F60
  bb_00641F52 -->|branch| bb_00641F60
  bb_00641F52 -->|fallthrough| bb_00641F56
  bb_00641F56 -->|flow| bb_00641F60
  bb_00641F60 -->|branch| bb_00641F82
  bb_00641F60 -->|fallthrough| bb_00641F76
  bb_00641F76 -->|branch| bb_00641F95
  bb_00641F76 -->|fallthrough| bb_00641F82
  bb_00641F82 -->|branch| bb_00641FCE
  bb_00641F82 -->|fallthrough| bb_00641F95
  bb_00641F95 -->|branch| bb_00641FB8
  bb_00641F9E -->|branch| bb_00641FB5
  bb_00641F9E -->|fallthrough| bb_00641FA7
  bb_00641FA7 -->|flow| bb_00641FB5
  bb_00641FB5 -->|flow| bb_00641FB8
  bb_00641FB8 -->|branch| bb_00641F9E
  bb_00641FB8 -->|fallthrough| bb_00641FBD
  bb_00641FBD -->|branch| bb_00641FCE
  bb_00641FBD -->|fallthrough| bb_00641FC2
  bb_00641FC2 -->|flow| bb_00641FCE
  bb_00641FCE -->|branch| bb_00642046
  bb_00641FCE -->|fallthrough| bb_00641FE2
  bb_00641FE2 -->|branch| bb_00641FFA
  bb_00641FE2 -->|fallthrough| bb_00641FEE
  bb_00641FEE -->|branch| bb_0064200D
  bb_00641FEE -->|fallthrough| bb_00641FFA
  bb_00641FFA -->|branch| bb_00642046
  bb_00641FFA -->|fallthrough| bb_0064200D
  bb_0064200D -->|branch| bb_00642030
  bb_00642016 -->|branch| bb_0064202D
  bb_00642016 -->|fallthrough| bb_0064201F
  bb_0064201F -->|flow| bb_0064202D
  bb_0064202D -->|flow| bb_00642030
  bb_00642030 -->|branch| bb_00642016
  bb_00642030 -->|fallthrough| bb_00642035
  bb_00642035 -->|branch| bb_00642046
  bb_00642035 -->|fallthrough| bb_0064203A
  bb_0064203A -->|flow| bb_00642046
```
