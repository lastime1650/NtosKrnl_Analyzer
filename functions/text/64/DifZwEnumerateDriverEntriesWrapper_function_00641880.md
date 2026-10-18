# DifZwEnumerateDriverEntriesWrapper

- RVA: `0x00641880`–`0x006419E4` (길이 `356` bytes)
- VA: `0x0000000140641880`
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
- `0x006418AE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006418D6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00641909` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00641930` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641949` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00641954` → [ZwEnumerateDriverEntries](../6A/ZwEnumerateDriverEntries_function_006AEDD0.md) (function, `0x006AEDD0`)
- `0x00641981` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006419A8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006419C1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006418E8` → RVA `0x00F048B8` (`.data`; read)
- `0x006418F6` → RVA `0x00F04980` (`.data`; read)
- `0x00641902` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00641880  48 8B C4                        mov rax, rsp
00641883  48 89 58 08                     mov qword ptr [rax + 8], rbx
00641887  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0064188B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064188F  57                              push rdi
00641890  41 56                           push r14
00641892  41 57                           push r15
00641894  48 83 EC 40                     sub rsp, 0x40
00641898  0F 57 C0                        xorps xmm0, xmm0
0064189B  4C 8B F9                        mov r15, rcx
0064189E  B9 69 00 00 00                  mov ecx, 0x69
006418A3  4C 8B F2                        mov r14, rdx
006418A6  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
006418AA  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
006418AE  E8 81 41 E5 FF                  call 0x140495a34
006418B3  48 8B F0                        mov rsi, rax
006418B6  48 85 C0                        test rax, rax
006418B9  0F 84 8F 00 00 00               je 0x14064194e
006418BF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006418C2  A8 18                           test al, 0x18
006418C4  74 0C                           je 0x1406418d2
006418C6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006418CB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006418D0  EB 0E                           jmp 0x1406418e0
006418D2  A8 04                           test al, 4
006418D4  74 0A                           je 0x1406418e0
006418D6  E8 2D 23 E9 FF                  call 0x1404d3c08
006418DB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006418E0  40 32 ED                        xor bpl, bpl
006418E3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
006418E8  40 38 2D C9 2F 8C 00            cmp byte ptr [rip + 0x8c2fc9], bpl
006418EF  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
006418F4  75 0C                           jne 0x140641902
006418F6  F7 05 80 30 8C 00 00 08 00 00   test dword ptr [rip + 0x8c3080], 0x800
00641900  74 13                           je 0x140641915
00641902  48 8D 0D 77 25 8C 00            lea rcx, [rip + 0x8c2577]
00641909  E8 12 4D BD FF                  call 0x140216620
0064190E  40 8A E8                        mov bpl, al
00641911  84 C0                           test al, al
00641913  74 39                           je 0x14064194e
00641915  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00641919  48 8B 1F                        mov rbx, qword ptr [rdi]
0064191C  EB 1A                           jmp 0x140641938
0064191E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00641922  48 85 C0                        test rax, rax
00641925  74 0E                           je 0x140641935
00641927  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064192B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00641930  E8 9B 91 07 00                  call 0x1406baad0
00641935  48 8B 1B                        mov rbx, qword ptr [rbx]
00641938  48 3B DF                        cmp rbx, rdi
0064193B  75 E1                           jne 0x14064191e
0064193D  40 84 ED                        test bpl, bpl
00641940  74 0C                           je 0x14064194e
00641942  48 8D 0D 37 25 8C 00            lea rcx, [rip + 0x8c2537]
00641949  E8 32 85 D0 FF                  call 0x140349e80
0064194E  49 8B D6                        mov rdx, r14
00641951  49 8B CF                        mov rcx, r15
00641954  E8 77 D4 06 00                  call 0x1406aedd0
00641959  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0064195D  48 85 F6                        test rsi, rsi
00641960  74 64                           je 0x1406419c6
00641962  40 32 FF                        xor dil, dil
00641965  40 38 3D 4C 2F 8C 00            cmp byte ptr [rip + 0x8c2f4c], dil
0064196C  75 0C                           jne 0x14064197a
0064196E  F7 05 08 30 8C 00 00 08 00 00   test dword ptr [rip + 0x8c3008], 0x800
00641978  74 13                           je 0x14064198d
0064197A  48 8D 0D FF 24 8C 00            lea rcx, [rip + 0x8c24ff]
00641981  E8 9A 4C BD FF                  call 0x140216620
00641986  40 8A F8                        mov dil, al
00641989  84 C0                           test al, al
0064198B  74 39                           je 0x1406419c6
0064198D  48 83 C6 30                     add rsi, 0x30
00641991  48 8B 1E                        mov rbx, qword ptr [rsi]
00641994  EB 1A                           jmp 0x1406419b0
00641996  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064199A  48 85 C0                        test rax, rax
0064199D  74 0E                           je 0x1406419ad
0064199F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006419A3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006419A8  E8 23 91 07 00                  call 0x1406baad0
006419AD  48 8B 1B                        mov rbx, qword ptr [rbx]
006419B0  48 3B DE                        cmp rbx, rsi
006419B3  75 E1                           jne 0x140641996
006419B5  40 84 FF                        test dil, dil
006419B8  74 0C                           je 0x1406419c6
006419BA  48 8D 0D BF 24 8C 00            lea rcx, [rip + 0x8c24bf]
006419C1  E8 BA 84 D0 FF                  call 0x140349e80
006419C6  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
006419CA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006419CF  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
006419D4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
006419D9  48 83 C4 40                     add rsp, 0x40
006419DD  41 5F                           pop r15
006419DF  41 5E                           pop r14
006419E1  5F                              pop rdi
006419E2  C3                              ret
006419E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwEnumerateDriverEntriesWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(105, a2, a3, a4);
    if (result == 0) goto loc_0064194E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006418D2;
    v_stack_m38 = v_stack_p0;
    goto loc_006418E0;
loc_006418D2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9187273)) != 0) goto loc_00641902;
    if (((*(unsigned int *)(v_rip + 9187456)) & (0x800ULL)) == 0) goto loc_00641915;
loc_00641902:
    result = ExAcquireRundownProtection(v_rip + 9184631, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064194E;
loc_00641915:
    goto loc_00641938;
loc_0064191E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00641938:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064191E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9184567;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwEnumerateDriverEntries(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_006419C6;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9187148)) != 0) goto loc_0064197A;
    if (((*(unsigned int *)(v_rip + 9187336)) & (0x800ULL)) == 0) goto loc_0064198D;
loc_0064197A:
    result = ExAcquireRundownProtection(v_rip + 9184511, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006419C6;
loc_0064198D:
    v_rsi = (result) + (48);
    goto loc_006419B0;
loc_00641996:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006419B0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00641996;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9184447;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwEnumerateDriverEntriesWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(105, Arg2, a3, a4);
    if (result == 0) goto loc_0064194E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006418D2;
    v_stack_m38 = v_stack_p0;
    goto loc_006418E0;
loc_006418D2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8C2FC9)) != 0) goto loc_00641902;
    if (((*(uint32_t *)(v_rip + 0x8C3080)) & (0x800ULL)) == 0) goto loc_00641915;
loc_00641902:
    result = ExAcquireRundownProtection(v_rip + 9184631, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064194E;
loc_00641915:
    goto loc_00641938;
loc_0064191E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00641938:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064191E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9184567;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwEnumerateDriverEntries(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_006419C6;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C2F4C)) != 0) goto loc_0064197A;
    if (((*(uint32_t *)(v_rip + 0x8C3008)) & (0x800ULL)) == 0) goto loc_0064198D;
loc_0064197A:
    result = ExAcquireRundownProtection(v_rip + 9184511, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006419C6;
loc_0064198D:
    local_rsi = (result) + (48);
    goto loc_006419B0;
loc_00641996:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006419B0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00641996;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9184447;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00641880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00641880[BB_00641880]
  bb_006418BF[BB_006418BF]
  bb_006418C6[BB_006418C6]
  bb_006418D2[BB_006418D2]
  bb_006418D6[BB_006418D6]
  bb_006418E0[BB_006418E0]
  bb_006418F6[BB_006418F6]
  bb_00641902[BB_00641902]
  bb_00641915[BB_00641915]
  bb_0064191E[BB_0064191E]
  bb_00641927[BB_00641927]
  bb_00641935[BB_00641935]
  bb_00641938[BB_00641938]
  bb_0064193D[BB_0064193D]
  bb_00641942[BB_00641942]
  bb_0064194E[BB_0064194E]
  bb_00641962[BB_00641962]
  bb_0064196E[BB_0064196E]
  bb_0064197A[BB_0064197A]
  bb_0064198D[BB_0064198D]
  bb_00641996[BB_00641996]
  bb_0064199F[BB_0064199F]
  bb_006419AD[BB_006419AD]
  bb_006419B0[BB_006419B0]
  bb_006419B5[BB_006419B5]
  bb_006419BA[BB_006419BA]
  bb_006419C6[BB_006419C6]
  bb_006419E3[BB_006419E3]
  bb_00641880 -->|branch| bb_0064194E
  bb_00641880 -->|fallthrough| bb_006418BF
  bb_006418BF -->|branch| bb_006418D2
  bb_006418BF -->|fallthrough| bb_006418C6
  bb_006418C6 -->|branch| bb_006418E0
  bb_006418D2 -->|branch| bb_006418E0
  bb_006418D2 -->|fallthrough| bb_006418D6
  bb_006418D6 -->|flow| bb_006418E0
  bb_006418E0 -->|branch| bb_00641902
  bb_006418E0 -->|fallthrough| bb_006418F6
  bb_006418F6 -->|branch| bb_00641915
  bb_006418F6 -->|fallthrough| bb_00641902
  bb_00641902 -->|branch| bb_0064194E
  bb_00641902 -->|fallthrough| bb_00641915
  bb_00641915 -->|branch| bb_00641938
  bb_0064191E -->|branch| bb_00641935
  bb_0064191E -->|fallthrough| bb_00641927
  bb_00641927 -->|flow| bb_00641935
  bb_00641935 -->|flow| bb_00641938
  bb_00641938 -->|branch| bb_0064191E
  bb_00641938 -->|fallthrough| bb_0064193D
  bb_0064193D -->|branch| bb_0064194E
  bb_0064193D -->|fallthrough| bb_00641942
  bb_00641942 -->|flow| bb_0064194E
  bb_0064194E -->|branch| bb_006419C6
  bb_0064194E -->|fallthrough| bb_00641962
  bb_00641962 -->|branch| bb_0064197A
  bb_00641962 -->|fallthrough| bb_0064196E
  bb_0064196E -->|branch| bb_0064198D
  bb_0064196E -->|fallthrough| bb_0064197A
  bb_0064197A -->|branch| bb_006419C6
  bb_0064197A -->|fallthrough| bb_0064198D
  bb_0064198D -->|branch| bb_006419B0
  bb_00641996 -->|branch| bb_006419AD
  bb_00641996 -->|fallthrough| bb_0064199F
  bb_0064199F -->|flow| bb_006419AD
  bb_006419AD -->|flow| bb_006419B0
  bb_006419B0 -->|branch| bb_00641996
  bb_006419B0 -->|fallthrough| bb_006419B5
  bb_006419B5 -->|branch| bb_006419C6
  bb_006419B5 -->|fallthrough| bb_006419BA
  bb_006419BA -->|flow| bb_006419C6
```
