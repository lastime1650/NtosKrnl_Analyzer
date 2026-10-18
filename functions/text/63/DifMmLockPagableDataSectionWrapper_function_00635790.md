# DifMmLockPagableDataSectionWrapper

- RVA: `0x00635790`–`0x006358F1` (길이 `353` bytes)
- VA: `0x0000000140635790`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006357BF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006357E7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00635815` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063583C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00635855` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063585D` → [MmLockPagableDataSection](../../page/A7/MmLockPagableDataSection_function_00A73E80.md) (function, `0x00A73E80`)
- `0x0063588B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006358B2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006358CB` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006357F9` → RVA `0x00F048B8` (`.data`; read)
- `0x00635802` → RVA `0x00F04980` (`.data`; read)
- `0x0063580E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063585D` → [MmLockPagableDataSection](../../page/A7/MmLockPagableDataSection_function_00A73E80.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00635790  4C 8B DC                        mov r11, rsp
00635793  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00635797  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063579B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063579F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006357A3  41 56                           push r14
006357A5  48 83 EC 40                     sub rsp, 0x40
006357A9  33 C0                           xor eax, eax
006357AB  0F 57 C0                        xorps xmm0, xmm0
006357AE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006357B3  48 8B E9                        mov rbp, rcx
006357B6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
006357BA  B9 DF 00 00 00                  mov ecx, 0xdf
006357BF  E8 70 02 E6 FF                  call 0x140495a34
006357C4  48 8B F0                        mov rsi, rax
006357C7  48 85 C0                        test rax, rax
006357CA  0F 84 8A 00 00 00               je 0x14063585a
006357D0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006357D3  A8 18                           test al, 0x18
006357D5  74 0C                           je 0x1406357e3
006357D7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006357DC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006357E1  EB 0E                           jmp 0x1406357f1
006357E3  A8 04                           test al, 4
006357E5  74 0A                           je 0x1406357f1
006357E7  E8 1C E4 E9 FF                  call 0x1404d3c08
006357EC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006357F1  40 32 FF                        xor dil, dil
006357F4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006357F9  40 38 3D B8 F0 8C 00            cmp byte ptr [rip + 0x8cf0b8], dil
00635800  75 0C                           jne 0x14063580e
00635802  F7 05 74 F1 8C 00 00 08 00 00   test dword ptr [rip + 0x8cf174], 0x800
0063580C  74 13                           je 0x140635821
0063580E  48 8D 0D 6B E6 8C 00            lea rcx, [rip + 0x8ce66b]
00635815  E8 06 0E BE FF                  call 0x140216620
0063581A  40 8A F8                        mov dil, al
0063581D  84 C0                           test al, al
0063581F  74 39                           je 0x14063585a
00635821  4C 8D 76 20                     lea r14, [rsi + 0x20]
00635825  49 8B 1E                        mov rbx, qword ptr [r14]
00635828  EB 1A                           jmp 0x140635844
0063582A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063582E  48 85 C0                        test rax, rax
00635831  74 0E                           je 0x140635841
00635833  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635837  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063583C  E8 8F 52 08 00                  call 0x1406baad0
00635841  48 8B 1B                        mov rbx, qword ptr [rbx]
00635844  49 3B DE                        cmp rbx, r14
00635847  75 E1                           jne 0x14063582a
00635849  40 84 FF                        test dil, dil
0063584C  74 0C                           je 0x14063585a
0063584E  48 8D 0D 2B E6 8C 00            lea rcx, [rip + 0x8ce62b]
00635855  E8 26 46 D1 FF                  call 0x140349e80
0063585A  48 8B CD                        mov rcx, rbp
0063585D  E8 1E E6 43 00                  call 0x140a73e80
00635862  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00635867  48 85 F6                        test rsi, rsi
0063586A  74 64                           je 0x1406358d0
0063586C  40 32 FF                        xor dil, dil
0063586F  40 38 3D 42 F0 8C 00            cmp byte ptr [rip + 0x8cf042], dil
00635876  75 0C                           jne 0x140635884
00635878  F7 05 FE F0 8C 00 00 08 00 00   test dword ptr [rip + 0x8cf0fe], 0x800
00635882  74 13                           je 0x140635897
00635884  48 8D 0D F5 E5 8C 00            lea rcx, [rip + 0x8ce5f5]
0063588B  E8 90 0D BE FF                  call 0x140216620
00635890  40 8A F8                        mov dil, al
00635893  84 C0                           test al, al
00635895  74 39                           je 0x1406358d0
00635897  48 83 C6 30                     add rsi, 0x30
0063589B  48 8B 1E                        mov rbx, qword ptr [rsi]
0063589E  EB 1A                           jmp 0x1406358ba
006358A0  48 8D 43 F0                     lea rax, [rbx - 0x10]
006358A4  48 85 C0                        test rax, rax
006358A7  74 0E                           je 0x1406358b7
006358A9  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006358AD  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006358B2  E8 19 52 08 00                  call 0x1406baad0
006358B7  48 8B 1B                        mov rbx, qword ptr [rbx]
006358BA  48 3B DE                        cmp rbx, rsi
006358BD  75 E1                           jne 0x1406358a0
006358BF  40 84 FF                        test dil, dil
006358C2  74 0C                           je 0x1406358d0
006358C4  48 8D 0D B5 E5 8C 00            lea rcx, [rip + 0x8ce5b5]
006358CB  E8 B0 45 D1 FF                  call 0x140349e80
006358D0  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
006358D5  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006358DA  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006358DF  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006358E4  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006358E9  48 83 C4 40                     add rsp, 0x40
006358ED  41 5E                           pop r14
006358EF  C3                              ret
006358F0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmLockPagableDataSectionWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
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
    result = DifGetAPIThunkContextById(223, a2, a3, a4);
    if (result == 0) goto loc_0063585A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006357E3;
    v_stack_m28 = v_stack_p0;
    goto loc_006357F1;
loc_006357E3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9236664)) != 0) goto loc_0063580E;
    if (((*(unsigned int *)(v_rip + 9236852)) & (0x800ULL)) == 0) goto loc_00635821;
loc_0063580E:
    result = ExAcquireRundownProtection(v_rip + 9234027, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063585A;
loc_00635821:
    goto loc_00635844;
loc_0063582A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00635844:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063582A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9233963;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmLockPagableDataSection(a1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_006358D0;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9236546)) != 0) goto loc_00635884;
    if (((*(unsigned int *)(v_rip + 9236734)) & (0x800ULL)) == 0) goto loc_00635897;
loc_00635884:
    result = ExAcquireRundownProtection(v_rip + 9233909, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006358D0;
loc_00635897:
    v_rsi = (result) + (48);
    goto loc_006358BA;
loc_006358A0:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006358BA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006358A0;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9233845;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmLockPagableDataSectionWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(223, a2, a3, a4);
    if (result == 0) goto loc_0063585A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006357E3;
    v_stack_m28 = v_stack_p0;
    goto loc_006357F1;
loc_006357E3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8CF0B8)) != 0) goto loc_0063580E;
    if (((*(uint32_t *)(v_rip + 0x8CF174)) & (0x800ULL)) == 0) goto loc_00635821;
loc_0063580E:
    result = ExAcquireRundownProtection(v_rip + 9234027, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063585A;
loc_00635821:
    goto loc_00635844;
loc_0063582A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00635844:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063582A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9233963;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = MmLockPagableDataSection(Arg1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_006358D0;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CF042)) != 0) goto loc_00635884;
    if (((*(uint32_t *)(v_rip + 0x8CF0FE)) & (0x800ULL)) == 0) goto loc_00635897;
loc_00635884:
    result = ExAcquireRundownProtection(v_rip + 9233909, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006358D0;
loc_00635897:
    local_rsi = (result) + (48);
    goto loc_006358BA;
loc_006358A0:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006358BA:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006358A0;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9233845;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00635790&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00635790[BB_00635790]
  bb_006357D0[BB_006357D0]
  bb_006357D7[BB_006357D7]
  bb_006357E3[BB_006357E3]
  bb_006357E7[BB_006357E7]
  bb_006357F1[BB_006357F1]
  bb_00635802[BB_00635802]
  bb_0063580E[BB_0063580E]
  bb_00635821[BB_00635821]
  bb_0063582A[BB_0063582A]
  bb_00635833[BB_00635833]
  bb_00635841[BB_00635841]
  bb_00635844[BB_00635844]
  bb_00635849[BB_00635849]
  bb_0063584E[BB_0063584E]
  bb_0063585A[BB_0063585A]
  bb_0063586C[BB_0063586C]
  bb_00635878[BB_00635878]
  bb_00635884[BB_00635884]
  bb_00635897[BB_00635897]
  bb_006358A0[BB_006358A0]
  bb_006358A9[BB_006358A9]
  bb_006358B7[BB_006358B7]
  bb_006358BA[BB_006358BA]
  bb_006358BF[BB_006358BF]
  bb_006358C4[BB_006358C4]
  bb_006358D0[BB_006358D0]
  bb_006358F0[BB_006358F0]
  bb_00635790 -->|branch| bb_0063585A
  bb_00635790 -->|fallthrough| bb_006357D0
  bb_006357D0 -->|branch| bb_006357E3
  bb_006357D0 -->|fallthrough| bb_006357D7
  bb_006357D7 -->|branch| bb_006357F1
  bb_006357E3 -->|branch| bb_006357F1
  bb_006357E3 -->|fallthrough| bb_006357E7
  bb_006357E7 -->|flow| bb_006357F1
  bb_006357F1 -->|branch| bb_0063580E
  bb_006357F1 -->|fallthrough| bb_00635802
  bb_00635802 -->|branch| bb_00635821
  bb_00635802 -->|fallthrough| bb_0063580E
  bb_0063580E -->|branch| bb_0063585A
  bb_0063580E -->|fallthrough| bb_00635821
  bb_00635821 -->|branch| bb_00635844
  bb_0063582A -->|branch| bb_00635841
  bb_0063582A -->|fallthrough| bb_00635833
  bb_00635833 -->|flow| bb_00635841
  bb_00635841 -->|flow| bb_00635844
  bb_00635844 -->|branch| bb_0063582A
  bb_00635844 -->|fallthrough| bb_00635849
  bb_00635849 -->|branch| bb_0063585A
  bb_00635849 -->|fallthrough| bb_0063584E
  bb_0063584E -->|flow| bb_0063585A
  bb_0063585A -->|branch| bb_006358D0
  bb_0063585A -->|fallthrough| bb_0063586C
  bb_0063586C -->|branch| bb_00635884
  bb_0063586C -->|fallthrough| bb_00635878
  bb_00635878 -->|branch| bb_00635897
  bb_00635878 -->|fallthrough| bb_00635884
  bb_00635884 -->|branch| bb_006358D0
  bb_00635884 -->|fallthrough| bb_00635897
  bb_00635897 -->|branch| bb_006358BA
  bb_006358A0 -->|branch| bb_006358B7
  bb_006358A0 -->|fallthrough| bb_006358A9
  bb_006358A9 -->|flow| bb_006358B7
  bb_006358B7 -->|flow| bb_006358BA
  bb_006358BA -->|branch| bb_006358A0
  bb_006358BA -->|fallthrough| bb_006358BF
  bb_006358BF -->|branch| bb_006358D0
  bb_006358BF -->|fallthrough| bb_006358C4
  bb_006358C4 -->|flow| bb_006358D0
```
