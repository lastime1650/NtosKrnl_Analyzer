# DifExAcquireFastResourceExclusiveWrapper

- RVA: `0x0061D760`–`0x0061D8D7` (길이 `375` bytes)
- VA: `0x000000014061D760`
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
- `0x0061D79E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061D7C4` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061D7F8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061D81E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061D837` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061D845` → [ExAcquireFastResourceExclusive](../3B/ExAcquireFastResourceExclusive_function_003BDFF0.md) (function, `0x003BDFF0`)
- `0x0061D871` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061D897` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061D8B0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061D7D4` → RVA `0x00F048B8` (`.data`; read)
- `0x0061D7E5` → RVA `0x00F04980` (`.data`; read)
- `0x0061D7F1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061D760  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0061D765  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0061D76A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0061D76F  55                              push rbp
0061D770  41 54                           push r12
0061D772  41 55                           push r13
0061D774  41 56                           push r14
0061D776  41 57                           push r15
0061D778  48 8B EC                        mov rbp, rsp
0061D77B  48 83 EC 50                     sub rsp, 0x50
0061D77F  0F 57 C0                        xorps xmm0, xmm0
0061D782  33 C0                           xor eax, eax
0061D784  4C 8B E9                        mov r13, rcx
0061D787  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0061D78B  B9 BA 01 00 00                  mov ecx, 0x1ba
0061D790  45 8A F8                        mov r15b, r8b
0061D793  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0061D797  4C 8B E2                        mov r12, rdx
0061D79A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0061D79E  E8 91 82 E7 FF                  call 0x140495a34
0061D7A3  48 8B F0                        mov rsi, rax
0061D7A6  48 85 C0                        test rax, rax
0061D7A9  0F 84 8D 00 00 00               je 0x14061d83c
0061D7AF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061D7B2  A8 18                           test al, 0x18
0061D7B4  74 0A                           je 0x14061d7c0
0061D7B6  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0061D7BA  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0061D7BE  EB 0D                           jmp 0x14061d7cd
0061D7C0  A8 04                           test al, 4
0061D7C2  74 09                           je 0x14061d7cd
0061D7C4  E8 3F 64 EB FF                  call 0x1404d3c08
0061D7C9  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0061D7CD  45 32 F6                        xor r14b, r14b
0061D7D0  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0061D7D4  44 38 35 DD 70 8E 00            cmp byte ptr [rip + 0x8e70dd], r14b
0061D7DB  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0061D7DF  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0061D7E3  75 0C                           jne 0x14061d7f1
0061D7E5  F7 05 91 71 8E 00 00 08 00 00   test dword ptr [rip + 0x8e7191], 0x800
0061D7EF  74 13                           je 0x14061d804
0061D7F1  48 8D 0D 88 66 8E 00            lea rcx, [rip + 0x8e6688]
0061D7F8  E8 23 8E BF FF                  call 0x140216620
0061D7FD  44 8A F0                        mov r14b, al
0061D800  84 C0                           test al, al
0061D802  74 38                           je 0x14061d83c
0061D804  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0061D808  48 8B 1F                        mov rbx, qword ptr [rdi]
0061D80B  EB 19                           jmp 0x14061d826
0061D80D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061D811  48 85 C0                        test rax, rax
0061D814  74 0D                           je 0x14061d823
0061D816  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061D81A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061D81E  E8 AD D2 09 00                  call 0x1406baad0
0061D823  48 8B 1B                        mov rbx, qword ptr [rbx]
0061D826  48 3B DF                        cmp rbx, rdi
0061D829  75 E2                           jne 0x14061d80d
0061D82B  45 84 F6                        test r14b, r14b
0061D82E  74 0C                           je 0x14061d83c
0061D830  48 8D 0D 49 66 8E 00            lea rcx, [rip + 0x8e6649]
0061D837  E8 44 C6 D2 FF                  call 0x140349e80
0061D83C  45 8A C7                        mov r8b, r15b
0061D83F  49 8B D4                        mov rdx, r12
0061D842  49 8B CD                        mov rcx, r13
0061D845  E8 A6 07 DA FF                  call 0x1403bdff0
0061D84A  88 45 F0                        mov byte ptr [rbp - 0x10], al
0061D84D  48 85 F6                        test rsi, rsi
0061D850  74 63                           je 0x14061d8b5
0061D852  40 32 FF                        xor dil, dil
0061D855  40 38 3D 5C 70 8E 00            cmp byte ptr [rip + 0x8e705c], dil
0061D85C  75 0C                           jne 0x14061d86a
0061D85E  F7 05 18 71 8E 00 00 08 00 00   test dword ptr [rip + 0x8e7118], 0x800
0061D868  74 13                           je 0x14061d87d
0061D86A  48 8D 0D 0F 66 8E 00            lea rcx, [rip + 0x8e660f]
0061D871  E8 AA 8D BF FF                  call 0x140216620
0061D876  40 8A F8                        mov dil, al
0061D879  84 C0                           test al, al
0061D87B  74 38                           je 0x14061d8b5
0061D87D  48 83 C6 30                     add rsi, 0x30
0061D881  48 8B 1E                        mov rbx, qword ptr [rsi]
0061D884  EB 19                           jmp 0x14061d89f
0061D886  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061D88A  48 85 C0                        test rax, rax
0061D88D  74 0D                           je 0x14061d89c
0061D88F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061D893  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061D897  E8 34 D2 09 00                  call 0x1406baad0
0061D89C  48 8B 1B                        mov rbx, qword ptr [rbx]
0061D89F  48 3B DE                        cmp rbx, rsi
0061D8A2  75 E2                           jne 0x14061d886
0061D8A4  40 84 FF                        test dil, dil
0061D8A7  74 0C                           je 0x14061d8b5
0061D8A9  48 8D 0D D0 65 8E 00            lea rcx, [rip + 0x8e65d0]
0061D8B0  E8 CB C5 D2 FF                  call 0x140349e80
0061D8B5  8A 45 F0                        mov al, byte ptr [rbp - 0x10]
0061D8B8  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0061D8BD  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0061D8C1  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0061D8C5  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0061D8C9  49 8B E3                        mov rsp, r11
0061D8CC  41 5F                           pop r15
0061D8CE  41 5E                           pop r14
0061D8D0  41 5D                           pop r13
0061D8D2  41 5C                           pop r12
0061D8D4  5D                              pop rbp
0061D8D5  C3                              ret
0061D8D6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExAcquireFastResourceExclusiveWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
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
    unsigned __int8 v_stack_m50;
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
    result = DifGetAPIThunkContextById(442, a2, a3, a4);
    if (result == 0) goto loc_0061D83C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061D7C0;
    v_stack_m58 = v_stack_p0;
    goto loc_0061D7CD;
loc_0061D7C0:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9335005)) != 0) goto loc_0061D7F1;
    if (((*(unsigned int *)(v_rip + 9335185)) & (0x800ULL)) == 0) goto loc_0061D804;
loc_0061D7F1:
    result = ExAcquireRundownProtection(v_rip + 9332360, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061D83C;
loc_0061D804:
    goto loc_0061D826;
loc_0061D80D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061D826:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061D80D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9332297;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExAcquireFastResourceExclusive(a1, a2, a3, a4);
    v_stack_m38 = (unsigned __int8)(result);
    if (result == 0) goto loc_0061D8B5;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9334876)) != 0) goto loc_0061D86A;
    if (((*(unsigned int *)(v_rip + 9335064)) & (0x800ULL)) == 0) goto loc_0061D87D;
loc_0061D86A:
    result = ExAcquireRundownProtection(v_rip + 9332239, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061D8B5;
loc_0061D87D:
    v_rsi = (result) + (48);
    goto loc_0061D89F;
loc_0061D886:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061D89F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061D886;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9332176;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifExAcquireFastResourceExclusiveWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
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
    uint8_t v_stack_m50;
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
    result = DifGetAPIThunkContextById(442, Arg2, Arg3, a4);
    if (result == 0) goto loc_0061D83C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061D7C0;
    v_stack_m58 = v_stack_p0;
    goto loc_0061D7CD;
loc_0061D7C0:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8E70DD)) != 0) goto loc_0061D7F1;
    if (((*(uint32_t *)(v_rip + 0x8E7191)) & (0x800ULL)) == 0) goto loc_0061D804;
loc_0061D7F1:
    result = ExAcquireRundownProtection(v_rip + 9332360, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061D83C;
loc_0061D804:
    goto loc_0061D826;
loc_0061D80D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0061D826:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061D80D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9332297;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ExAcquireFastResourceExclusive(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint8_t)(result);
    if (result == 0) goto loc_0061D8B5;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E705C)) != 0) goto loc_0061D86A;
    if (((*(uint32_t *)(v_rip + 0x8E7118)) & (0x800ULL)) == 0) goto loc_0061D87D;
loc_0061D86A:
    result = ExAcquireRundownProtection(v_rip + 9332239, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061D8B5;
loc_0061D87D:
    local_rsi = (result) + (48);
    goto loc_0061D89F;
loc_0061D886:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0061D89F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061D886;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9332176;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061D760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061D760[BB_0061D760]
  bb_0061D7AF[BB_0061D7AF]
  bb_0061D7B6[BB_0061D7B6]
  bb_0061D7C0[BB_0061D7C0]
  bb_0061D7C4[BB_0061D7C4]
  bb_0061D7CD[BB_0061D7CD]
  bb_0061D7E5[BB_0061D7E5]
  bb_0061D7F1[BB_0061D7F1]
  bb_0061D804[BB_0061D804]
  bb_0061D80D[BB_0061D80D]
  bb_0061D816[BB_0061D816]
  bb_0061D823[BB_0061D823]
  bb_0061D826[BB_0061D826]
  bb_0061D82B[BB_0061D82B]
  bb_0061D830[BB_0061D830]
  bb_0061D83C[BB_0061D83C]
  bb_0061D852[BB_0061D852]
  bb_0061D85E[BB_0061D85E]
  bb_0061D86A[BB_0061D86A]
  bb_0061D87D[BB_0061D87D]
  bb_0061D886[BB_0061D886]
  bb_0061D88F[BB_0061D88F]
  bb_0061D89C[BB_0061D89C]
  bb_0061D89F[BB_0061D89F]
  bb_0061D8A4[BB_0061D8A4]
  bb_0061D8A9[BB_0061D8A9]
  bb_0061D8B5[BB_0061D8B5]
  bb_0061D8D6[BB_0061D8D6]
  bb_0061D760 -->|branch| bb_0061D83C
  bb_0061D760 -->|fallthrough| bb_0061D7AF
  bb_0061D7AF -->|branch| bb_0061D7C0
  bb_0061D7AF -->|fallthrough| bb_0061D7B6
  bb_0061D7B6 -->|branch| bb_0061D7CD
  bb_0061D7C0 -->|branch| bb_0061D7CD
  bb_0061D7C0 -->|fallthrough| bb_0061D7C4
  bb_0061D7C4 -->|flow| bb_0061D7CD
  bb_0061D7CD -->|branch| bb_0061D7F1
  bb_0061D7CD -->|fallthrough| bb_0061D7E5
  bb_0061D7E5 -->|branch| bb_0061D804
  bb_0061D7E5 -->|fallthrough| bb_0061D7F1
  bb_0061D7F1 -->|branch| bb_0061D83C
  bb_0061D7F1 -->|fallthrough| bb_0061D804
  bb_0061D804 -->|branch| bb_0061D826
  bb_0061D80D -->|branch| bb_0061D823
  bb_0061D80D -->|fallthrough| bb_0061D816
  bb_0061D816 -->|flow| bb_0061D823
  bb_0061D823 -->|flow| bb_0061D826
  bb_0061D826 -->|branch| bb_0061D80D
  bb_0061D826 -->|fallthrough| bb_0061D82B
  bb_0061D82B -->|branch| bb_0061D83C
  bb_0061D82B -->|fallthrough| bb_0061D830
  bb_0061D830 -->|flow| bb_0061D83C
  bb_0061D83C -->|branch| bb_0061D8B5
  bb_0061D83C -->|fallthrough| bb_0061D852
  bb_0061D852 -->|branch| bb_0061D86A
  bb_0061D852 -->|fallthrough| bb_0061D85E
  bb_0061D85E -->|branch| bb_0061D87D
  bb_0061D85E -->|fallthrough| bb_0061D86A
  bb_0061D86A -->|branch| bb_0061D8B5
  bb_0061D86A -->|fallthrough| bb_0061D87D
  bb_0061D87D -->|branch| bb_0061D89F
  bb_0061D886 -->|branch| bb_0061D89C
  bb_0061D886 -->|fallthrough| bb_0061D88F
  bb_0061D88F -->|flow| bb_0061D89C
  bb_0061D89C -->|flow| bb_0061D89F
  bb_0061D89F -->|branch| bb_0061D886
  bb_0061D89F -->|fallthrough| bb_0061D8A4
  bb_0061D8A4 -->|branch| bb_0061D8B5
  bb_0061D8A4 -->|fallthrough| bb_0061D8A9
  bb_0061D8A9 -->|flow| bb_0061D8B5
```
