# DifZwPrepareCompleteWrapper

- RVA: `0x00645800`–`0x00645964` (길이 `356` bytes)
- VA: `0x0000000140645800`
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
- `0x0064582E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00645856` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00645889` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006458B0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006458C9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006458D4` → [ZwPrepareComplete](../6A/ZwPrepareComplete_function_006AF8F0.md) (function, `0x006AF8F0`)
- `0x00645901` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645928` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645941` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00645868` → RVA `0x00F048B8` (`.data`; read)
- `0x00645876` → RVA `0x00F04980` (`.data`; read)
- `0x00645882` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00645800  48 8B C4                        mov rax, rsp
00645803  48 89 58 08                     mov qword ptr [rax + 8], rbx
00645807  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0064580B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064580F  57                              push rdi
00645810  41 56                           push r14
00645812  41 57                           push r15
00645814  48 83 EC 40                     sub rsp, 0x40
00645818  0F 57 C0                        xorps xmm0, xmm0
0064581B  4C 8B F9                        mov r15, rcx
0064581E  B9 41 00 00 00                  mov ecx, 0x41
00645823  4C 8B F2                        mov r14, rdx
00645826  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0064582A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0064582E  E8 01 02 E5 FF                  call 0x140495a34
00645833  48 8B F0                        mov rsi, rax
00645836  48 85 C0                        test rax, rax
00645839  0F 84 8F 00 00 00               je 0x1406458ce
0064583F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00645842  A8 18                           test al, 0x18
00645844  74 0C                           je 0x140645852
00645846  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0064584B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00645850  EB 0E                           jmp 0x140645860
00645852  A8 04                           test al, 4
00645854  74 0A                           je 0x140645860
00645856  E8 AD E3 E8 FF                  call 0x1404d3c08
0064585B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00645860  40 32 ED                        xor bpl, bpl
00645863  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00645868  40 38 2D 49 F0 8B 00            cmp byte ptr [rip + 0x8bf049], bpl
0064586F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00645874  75 0C                           jne 0x140645882
00645876  F7 05 00 F1 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf100], 0x800
00645880  74 13                           je 0x140645895
00645882  48 8D 0D F7 E5 8B 00            lea rcx, [rip + 0x8be5f7]
00645889  E8 92 0D BD FF                  call 0x140216620
0064588E  40 8A E8                        mov bpl, al
00645891  84 C0                           test al, al
00645893  74 39                           je 0x1406458ce
00645895  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00645899  48 8B 1F                        mov rbx, qword ptr [rdi]
0064589C  EB 1A                           jmp 0x1406458b8
0064589E  48 8D 43 F0                     lea rax, [rbx - 0x10]
006458A2  48 85 C0                        test rax, rax
006458A5  74 0E                           je 0x1406458b5
006458A7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006458AB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006458B0  E8 1B 52 07 00                  call 0x1406baad0
006458B5  48 8B 1B                        mov rbx, qword ptr [rbx]
006458B8  48 3B DF                        cmp rbx, rdi
006458BB  75 E1                           jne 0x14064589e
006458BD  40 84 ED                        test bpl, bpl
006458C0  74 0C                           je 0x1406458ce
006458C2  48 8D 0D B7 E5 8B 00            lea rcx, [rip + 0x8be5b7]
006458C9  E8 B2 45 D0 FF                  call 0x140349e80
006458CE  49 8B D6                        mov rdx, r14
006458D1  49 8B CF                        mov rcx, r15
006458D4  E8 17 A0 06 00                  call 0x1406af8f0
006458D9  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
006458DD  48 85 F6                        test rsi, rsi
006458E0  74 64                           je 0x140645946
006458E2  40 32 FF                        xor dil, dil
006458E5  40 38 3D CC EF 8B 00            cmp byte ptr [rip + 0x8befcc], dil
006458EC  75 0C                           jne 0x1406458fa
006458EE  F7 05 88 F0 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf088], 0x800
006458F8  74 13                           je 0x14064590d
006458FA  48 8D 0D 7F E5 8B 00            lea rcx, [rip + 0x8be57f]
00645901  E8 1A 0D BD FF                  call 0x140216620
00645906  40 8A F8                        mov dil, al
00645909  84 C0                           test al, al
0064590B  74 39                           je 0x140645946
0064590D  48 83 C6 30                     add rsi, 0x30
00645911  48 8B 1E                        mov rbx, qword ptr [rsi]
00645914  EB 1A                           jmp 0x140645930
00645916  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064591A  48 85 C0                        test rax, rax
0064591D  74 0E                           je 0x14064592d
0064591F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00645923  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00645928  E8 A3 51 07 00                  call 0x1406baad0
0064592D  48 8B 1B                        mov rbx, qword ptr [rbx]
00645930  48 3B DE                        cmp rbx, rsi
00645933  75 E1                           jne 0x140645916
00645935  40 84 FF                        test dil, dil
00645938  74 0C                           je 0x140645946
0064593A  48 8D 0D 3F E5 8B 00            lea rcx, [rip + 0x8be53f]
00645941  E8 3A 45 D0 FF                  call 0x140349e80
00645946  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0064594A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0064594F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00645954  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00645959  48 83 C4 40                     add rsp, 0x40
0064595D  41 5F                           pop r15
0064595F  41 5E                           pop r14
00645961  5F                              pop rdi
00645962  C3                              ret
00645963  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwPrepareCompleteWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(65, a2, a3, a4);
    if (result == 0) goto loc_006458CE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00645852;
    v_stack_m38 = v_stack_p0;
    goto loc_00645860;
loc_00645852:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9171017)) != 0) goto loc_00645882;
    if (((*(unsigned int *)(v_rip + 9171200)) & (0x800ULL)) == 0) goto loc_00645895;
loc_00645882:
    result = ExAcquireRundownProtection(v_rip + 9168375, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006458CE;
loc_00645895:
    goto loc_006458B8;
loc_0064589E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006458B8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064589E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9168311;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwPrepareComplete(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00645946;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9170892)) != 0) goto loc_006458FA;
    if (((*(unsigned int *)(v_rip + 9171080)) & (0x800ULL)) == 0) goto loc_0064590D;
loc_006458FA:
    result = ExAcquireRundownProtection(v_rip + 9168255, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00645946;
loc_0064590D:
    v_rsi = (result) + (48);
    goto loc_00645930;
loc_00645916:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00645930:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00645916;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9168191;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwPrepareCompleteWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(65, Arg2, a3, a4);
    if (result == 0) goto loc_006458CE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00645852;
    v_stack_m38 = v_stack_p0;
    goto loc_00645860;
loc_00645852:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8BF049)) != 0) goto loc_00645882;
    if (((*(uint32_t *)(v_rip + 0x8BF100)) & (0x800ULL)) == 0) goto loc_00645895;
loc_00645882:
    result = ExAcquireRundownProtection(v_rip + 9168375, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006458CE;
loc_00645895:
    goto loc_006458B8;
loc_0064589E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006458B8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064589E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9168311;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwPrepareComplete(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00645946;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BEFCC)) != 0) goto loc_006458FA;
    if (((*(uint32_t *)(v_rip + 0x8BF088)) & (0x800ULL)) == 0) goto loc_0064590D;
loc_006458FA:
    result = ExAcquireRundownProtection(v_rip + 9168255, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00645946;
loc_0064590D:
    local_rsi = (result) + (48);
    goto loc_00645930;
loc_00645916:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00645930:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00645916;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9168191;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00645800&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00645800[BB_00645800]
  bb_0064583F[BB_0064583F]
  bb_00645846[BB_00645846]
  bb_00645852[BB_00645852]
  bb_00645856[BB_00645856]
  bb_00645860[BB_00645860]
  bb_00645876[BB_00645876]
  bb_00645882[BB_00645882]
  bb_00645895[BB_00645895]
  bb_0064589E[BB_0064589E]
  bb_006458A7[BB_006458A7]
  bb_006458B5[BB_006458B5]
  bb_006458B8[BB_006458B8]
  bb_006458BD[BB_006458BD]
  bb_006458C2[BB_006458C2]
  bb_006458CE[BB_006458CE]
  bb_006458E2[BB_006458E2]
  bb_006458EE[BB_006458EE]
  bb_006458FA[BB_006458FA]
  bb_0064590D[BB_0064590D]
  bb_00645916[BB_00645916]
  bb_0064591F[BB_0064591F]
  bb_0064592D[BB_0064592D]
  bb_00645930[BB_00645930]
  bb_00645935[BB_00645935]
  bb_0064593A[BB_0064593A]
  bb_00645946[BB_00645946]
  bb_00645963[BB_00645963]
  bb_00645800 -->|branch| bb_006458CE
  bb_00645800 -->|fallthrough| bb_0064583F
  bb_0064583F -->|branch| bb_00645852
  bb_0064583F -->|fallthrough| bb_00645846
  bb_00645846 -->|branch| bb_00645860
  bb_00645852 -->|branch| bb_00645860
  bb_00645852 -->|fallthrough| bb_00645856
  bb_00645856 -->|flow| bb_00645860
  bb_00645860 -->|branch| bb_00645882
  bb_00645860 -->|fallthrough| bb_00645876
  bb_00645876 -->|branch| bb_00645895
  bb_00645876 -->|fallthrough| bb_00645882
  bb_00645882 -->|branch| bb_006458CE
  bb_00645882 -->|fallthrough| bb_00645895
  bb_00645895 -->|branch| bb_006458B8
  bb_0064589E -->|branch| bb_006458B5
  bb_0064589E -->|fallthrough| bb_006458A7
  bb_006458A7 -->|flow| bb_006458B5
  bb_006458B5 -->|flow| bb_006458B8
  bb_006458B8 -->|branch| bb_0064589E
  bb_006458B8 -->|fallthrough| bb_006458BD
  bb_006458BD -->|branch| bb_006458CE
  bb_006458BD -->|fallthrough| bb_006458C2
  bb_006458C2 -->|flow| bb_006458CE
  bb_006458CE -->|branch| bb_00645946
  bb_006458CE -->|fallthrough| bb_006458E2
  bb_006458E2 -->|branch| bb_006458FA
  bb_006458E2 -->|fallthrough| bb_006458EE
  bb_006458EE -->|branch| bb_0064590D
  bb_006458EE -->|fallthrough| bb_006458FA
  bb_006458FA -->|branch| bb_00645946
  bb_006458FA -->|fallthrough| bb_0064590D
  bb_0064590D -->|branch| bb_00645930
  bb_00645916 -->|branch| bb_0064592D
  bb_00645916 -->|fallthrough| bb_0064591F
  bb_0064591F -->|flow| bb_0064592D
  bb_0064592D -->|flow| bb_00645930
  bb_00645930 -->|branch| bb_00645916
  bb_00645930 -->|fallthrough| bb_00645935
  bb_00645935 -->|branch| bb_00645946
  bb_00645935 -->|fallthrough| bb_0064593A
  bb_0064593A -->|flow| bb_00645946
```
