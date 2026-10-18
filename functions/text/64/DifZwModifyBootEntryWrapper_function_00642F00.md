# DifZwModifyBootEntryWrapper

- RVA: `0x00642F00`–`0x0064305D` (길이 `349` bytes)
- VA: `0x0000000140642F00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `349/349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00642F2D` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00642F55` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00642F83` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00642FAA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00642FC3` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00642FCB` → [ZwModifyBootEntry](../6A/ZwModifyBootEntry_function_006AF4D0.md) (function, `0x006AF4D0`)
- `0x00642FF8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064301F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00643038` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00642F67` → RVA `0x00F048B8` (`.data`; read)
- `0x00642F70` → RVA `0x00F04980` (`.data`; read)
- `0x00642F7C` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00642F00  4C 8B DC                        mov r11, rsp
00642F03  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00642F07  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00642F0B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00642F0F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00642F13  41 56                           push r14
00642F15  48 83 EC 40                     sub rsp, 0x40
00642F19  33 C0                           xor eax, eax
00642F1B  0F 57 C0                        xorps xmm0, xmm0
00642F1E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00642F23  48 8B E9                        mov rbp, rcx
00642F26  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00642F2A  8D 48 5B                        lea ecx, [rax + 0x5b]
00642F2D  E8 02 2B E5 FF                  call 0x140495a34
00642F32  48 8B F0                        mov rsi, rax
00642F35  48 85 C0                        test rax, rax
00642F38  0F 84 8A 00 00 00               je 0x140642fc8
00642F3E  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00642F41  A8 18                           test al, 0x18
00642F43  74 0C                           je 0x140642f51
00642F45  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00642F4A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00642F4F  EB 0E                           jmp 0x140642f5f
00642F51  A8 04                           test al, 4
00642F53  74 0A                           je 0x140642f5f
00642F55  E8 AE 0C E9 FF                  call 0x1404d3c08
00642F5A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00642F5F  40 32 FF                        xor dil, dil
00642F62  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00642F67  40 38 3D 4A 19 8C 00            cmp byte ptr [rip + 0x8c194a], dil
00642F6E  75 0C                           jne 0x140642f7c
00642F70  F7 05 06 1A 8C 00 00 08 00 00   test dword ptr [rip + 0x8c1a06], 0x800
00642F7A  74 13                           je 0x140642f8f
00642F7C  48 8D 0D FD 0E 8C 00            lea rcx, [rip + 0x8c0efd]
00642F83  E8 98 36 BD FF                  call 0x140216620
00642F88  40 8A F8                        mov dil, al
00642F8B  84 C0                           test al, al
00642F8D  74 39                           je 0x140642fc8
00642F8F  4C 8D 76 20                     lea r14, [rsi + 0x20]
00642F93  49 8B 1E                        mov rbx, qword ptr [r14]
00642F96  EB 1A                           jmp 0x140642fb2
00642F98  48 8D 43 F0                     lea rax, [rbx - 0x10]
00642F9C  48 85 C0                        test rax, rax
00642F9F  74 0E                           je 0x140642faf
00642FA1  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00642FA5  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00642FAA  E8 21 7B 07 00                  call 0x1406baad0
00642FAF  48 8B 1B                        mov rbx, qword ptr [rbx]
00642FB2  49 3B DE                        cmp rbx, r14
00642FB5  75 E1                           jne 0x140642f98
00642FB7  40 84 FF                        test dil, dil
00642FBA  74 0C                           je 0x140642fc8
00642FBC  48 8D 0D BD 0E 8C 00            lea rcx, [rip + 0x8c0ebd]
00642FC3  E8 B8 6E D0 FF                  call 0x140349e80
00642FC8  48 8B CD                        mov rcx, rbp
00642FCB  E8 00 C5 06 00                  call 0x1406af4d0
00642FD0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00642FD4  48 85 F6                        test rsi, rsi
00642FD7  74 64                           je 0x14064303d
00642FD9  40 32 FF                        xor dil, dil
00642FDC  40 38 3D D5 18 8C 00            cmp byte ptr [rip + 0x8c18d5], dil
00642FE3  75 0C                           jne 0x140642ff1
00642FE5  F7 05 91 19 8C 00 00 08 00 00   test dword ptr [rip + 0x8c1991], 0x800
00642FEF  74 13                           je 0x140643004
00642FF1  48 8D 0D 88 0E 8C 00            lea rcx, [rip + 0x8c0e88]
00642FF8  E8 23 36 BD FF                  call 0x140216620
00642FFD  40 8A F8                        mov dil, al
00643000  84 C0                           test al, al
00643002  74 39                           je 0x14064303d
00643004  48 83 C6 30                     add rsi, 0x30
00643008  48 8B 1E                        mov rbx, qword ptr [rsi]
0064300B  EB 1A                           jmp 0x140643027
0064300D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00643011  48 85 C0                        test rax, rax
00643014  74 0E                           je 0x140643024
00643016  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064301A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064301F  E8 AC 7A 07 00                  call 0x1406baad0
00643024  48 8B 1B                        mov rbx, qword ptr [rbx]
00643027  48 3B DE                        cmp rbx, rsi
0064302A  75 E1                           jne 0x14064300d
0064302C  40 84 FF                        test dil, dil
0064302F  74 0C                           je 0x14064303d
00643031  48 8D 0D 48 0E 8C 00            lea rcx, [rip + 0x8c0e48]
00643038  E8 43 6E D0 FF                  call 0x140349e80
0064303D  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00643041  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00643046  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0064304B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00643050  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00643055  48 83 C4 40                     add rsp, 0x40
00643059  41 5E                           pop r14
0064305B  C3                              ret
0064305C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwModifyBootEntryWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(result + 91, a2, a3, a4);
    if (result == 0) goto loc_00642FC8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00642F51;
    v_stack_m28 = v_stack_p0;
    goto loc_00642F5F;
loc_00642F51:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9181514)) != 0) goto loc_00642F7C;
    if (((*(unsigned int *)(v_rip + 9181702)) & (0x800ULL)) == 0) goto loc_00642F8F;
loc_00642F7C:
    result = ExAcquireRundownProtection(v_rip + 9178877, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00642FC8;
loc_00642F8F:
    goto loc_00642FB2;
loc_00642F98:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00642FB2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00642F98;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9178813;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwModifyBootEntry(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0064303D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9181397)) != 0) goto loc_00642FF1;
    if (((*(unsigned int *)(v_rip + 9181585)) & (0x800ULL)) == 0) goto loc_00643004;
loc_00642FF1:
    result = ExAcquireRundownProtection(v_rip + 9178760, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064303D;
loc_00643004:
    v_rsi = (result) + (48);
    goto loc_00643027;
loc_0064300D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00643027:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064300D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9178696;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwModifyBootEntryWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(result + 91, a2, a3, a4);
    if (result == 0) goto loc_00642FC8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00642F51;
    v_stack_m28 = v_stack_p0;
    goto loc_00642F5F;
loc_00642F51:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8C194A)) != 0) goto loc_00642F7C;
    if (((*(uint32_t *)(v_rip + 0x8C1A06)) & (0x800ULL)) == 0) goto loc_00642F8F;
loc_00642F7C:
    result = ExAcquireRundownProtection(v_rip + 9178877, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00642FC8;
loc_00642F8F:
    goto loc_00642FB2;
loc_00642F98:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00642FB2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00642F98;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9178813;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ZwModifyBootEntry(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0064303D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C18D5)) != 0) goto loc_00642FF1;
    if (((*(uint32_t *)(v_rip + 0x8C1991)) & (0x800ULL)) == 0) goto loc_00643004;
loc_00642FF1:
    result = ExAcquireRundownProtection(v_rip + 9178760, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064303D;
loc_00643004:
    local_rsi = (result) + (48);
    goto loc_00643027;
loc_0064300D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00643027:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064300D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9178696;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00642F00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00642F00[BB_00642F00]
  bb_00642F3E[BB_00642F3E]
  bb_00642F45[BB_00642F45]
  bb_00642F51[BB_00642F51]
  bb_00642F55[BB_00642F55]
  bb_00642F5F[BB_00642F5F]
  bb_00642F70[BB_00642F70]
  bb_00642F7C[BB_00642F7C]
  bb_00642F8F[BB_00642F8F]
  bb_00642F98[BB_00642F98]
  bb_00642FA1[BB_00642FA1]
  bb_00642FAF[BB_00642FAF]
  bb_00642FB2[BB_00642FB2]
  bb_00642FB7[BB_00642FB7]
  bb_00642FBC[BB_00642FBC]
  bb_00642FC8[BB_00642FC8]
  bb_00642FD9[BB_00642FD9]
  bb_00642FE5[BB_00642FE5]
  bb_00642FF1[BB_00642FF1]
  bb_00643004[BB_00643004]
  bb_0064300D[BB_0064300D]
  bb_00643016[BB_00643016]
  bb_00643024[BB_00643024]
  bb_00643027[BB_00643027]
  bb_0064302C[BB_0064302C]
  bb_00643031[BB_00643031]
  bb_0064303D[BB_0064303D]
  bb_0064305C[BB_0064305C]
  bb_00642F00 -->|branch| bb_00642FC8
  bb_00642F00 -->|fallthrough| bb_00642F3E
  bb_00642F3E -->|branch| bb_00642F51
  bb_00642F3E -->|fallthrough| bb_00642F45
  bb_00642F45 -->|branch| bb_00642F5F
  bb_00642F51 -->|branch| bb_00642F5F
  bb_00642F51 -->|fallthrough| bb_00642F55
  bb_00642F55 -->|flow| bb_00642F5F
  bb_00642F5F -->|branch| bb_00642F7C
  bb_00642F5F -->|fallthrough| bb_00642F70
  bb_00642F70 -->|branch| bb_00642F8F
  bb_00642F70 -->|fallthrough| bb_00642F7C
  bb_00642F7C -->|branch| bb_00642FC8
  bb_00642F7C -->|fallthrough| bb_00642F8F
  bb_00642F8F -->|branch| bb_00642FB2
  bb_00642F98 -->|branch| bb_00642FAF
  bb_00642F98 -->|fallthrough| bb_00642FA1
  bb_00642FA1 -->|flow| bb_00642FAF
  bb_00642FAF -->|flow| bb_00642FB2
  bb_00642FB2 -->|branch| bb_00642F98
  bb_00642FB2 -->|fallthrough| bb_00642FB7
  bb_00642FB7 -->|branch| bb_00642FC8
  bb_00642FB7 -->|fallthrough| bb_00642FBC
  bb_00642FBC -->|flow| bb_00642FC8
  bb_00642FC8 -->|branch| bb_0064303D
  bb_00642FC8 -->|fallthrough| bb_00642FD9
  bb_00642FD9 -->|branch| bb_00642FF1
  bb_00642FD9 -->|fallthrough| bb_00642FE5
  bb_00642FE5 -->|branch| bb_00643004
  bb_00642FE5 -->|fallthrough| bb_00642FF1
  bb_00642FF1 -->|branch| bb_0064303D
  bb_00642FF1 -->|fallthrough| bb_00643004
  bb_00643004 -->|branch| bb_00643027
  bb_0064300D -->|branch| bb_00643024
  bb_0064300D -->|fallthrough| bb_00643016
  bb_00643016 -->|flow| bb_00643024
  bb_00643024 -->|flow| bb_00643027
  bb_00643027 -->|branch| bb_0064300D
  bb_00643027 -->|fallthrough| bb_0064302C
  bb_0064302C -->|branch| bb_0064303D
  bb_0064302C -->|fallthrough| bb_00643031
  bb_00643031 -->|flow| bb_0064303D
```
