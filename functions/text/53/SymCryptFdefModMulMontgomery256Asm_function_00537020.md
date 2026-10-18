# SymCryptFdefModMulMontgomery256Asm

- RVA: `0x00537020`–`0x00537367` (길이 `839` bytes)
- VA: `0x0000000140537020`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C34F8`
- 디코드: `255`개 명령, `839/839` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00537020  48 56                           push rsi
00537022  57                              push rdi
00537023  55                              push rbp
00537024  53                              push rbx
00537025  41 54                           push r12
00537027  41 55                           push r13
00537029  41 56                           push r14
0053702B  41 57                           push r15
0053702D  4C 8B D2                        mov r10, rdx
00537030  4D 8B 1A                        mov r11, qword ptr [r10]
00537033  48 33 ED                        xor rbp, rbp
00537036  48 33 DB                        xor rbx, rbx
00537039  4D 33 E4                        xor r12, r12
0053703C  49 8B 00                        mov rax, qword ptr [r8]
0053703F  49 F7 E3                        mul r11
00537042  48 8B F0                        mov rsi, rax
00537045  48 8B FA                        mov rdi, rdx
00537048  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
0053704C  49 F7 E3                        mul r11
0053704F  48 03 F8                        add rdi, rax
00537052  48 13 EA                        adc rbp, rdx
00537055  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
00537059  49 F7 E3                        mul r11
0053705C  48 03 E8                        add rbp, rax
0053705F  48 13 DA                        adc rbx, rdx
00537062  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00537066  49 F7 E3                        mul r11
00537069  48 03 D8                        add rbx, rax
0053706C  4C 13 E2                        adc r12, rdx
0053706F  4D 8B 5A 08                     mov r11, qword ptr [r10 + 8]
00537073  49 8B 00                        mov rax, qword ptr [r8]
00537076  49 F7 E3                        mul r11
00537079  48 03 F8                        add rdi, rax
0053707C  48 83 D2 00                     adc rdx, 0
00537080  4C 8B FA                        mov r15, rdx
00537083  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
00537087  49 F7 E3                        mul r11
0053708A  48 03 E8                        add rbp, rax
0053708D  48 83 D2 00                     adc rdx, 0
00537091  49 03 EF                        add rbp, r15
00537094  48 83 D2 00                     adc rdx, 0
00537098  4C 8B FA                        mov r15, rdx
0053709B  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
0053709F  49 F7 E3                        mul r11
005370A2  48 03 D8                        add rbx, rax
005370A5  48 83 D2 00                     adc rdx, 0
005370A9  49 03 DF                        add rbx, r15
005370AC  48 83 D2 00                     adc rdx, 0
005370B0  4C 8B FA                        mov r15, rdx
005370B3  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
005370B7  49 F7 E3                        mul r11
005370BA  4C 03 E0                        add r12, rax
005370BD  48 83 D2 00                     adc rdx, 0
005370C1  4D 03 E7                        add r12, r15
005370C4  48 83 D2 00                     adc rdx, 0
005370C8  4C 8B EA                        mov r13, rdx
005370CB  4D 8B 5A 10                     mov r11, qword ptr [r10 + 0x10]
005370CF  49 8B 00                        mov rax, qword ptr [r8]
005370D2  49 F7 E3                        mul r11
005370D5  48 03 E8                        add rbp, rax
005370D8  48 83 D2 00                     adc rdx, 0
005370DC  4C 8B FA                        mov r15, rdx
005370DF  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
005370E3  49 F7 E3                        mul r11
005370E6  48 03 D8                        add rbx, rax
005370E9  48 83 D2 00                     adc rdx, 0
005370ED  49 03 DF                        add rbx, r15
005370F0  48 83 D2 00                     adc rdx, 0
005370F4  4C 8B FA                        mov r15, rdx
005370F7  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
005370FB  49 F7 E3                        mul r11
005370FE  4C 03 E0                        add r12, rax
00537101  48 83 D2 00                     adc rdx, 0
00537105  4D 03 E7                        add r12, r15
00537108  48 83 D2 00                     adc rdx, 0
0053710C  4C 8B FA                        mov r15, rdx
0053710F  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00537113  49 F7 E3                        mul r11
00537116  4C 03 E8                        add r13, rax
00537119  48 83 D2 00                     adc rdx, 0
0053711D  4D 03 EF                        add r13, r15
00537120  48 83 D2 00                     adc rdx, 0
00537124  4C 8B F2                        mov r14, rdx
00537127  4D 8B 5A 18                     mov r11, qword ptr [r10 + 0x18]
0053712B  49 8B 00                        mov rax, qword ptr [r8]
0053712E  49 F7 E3                        mul r11
00537131  48 03 D8                        add rbx, rax
00537134  48 83 D2 00                     adc rdx, 0
00537138  4C 8B FA                        mov r15, rdx
0053713B  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
0053713F  49 F7 E3                        mul r11
00537142  4C 03 E0                        add r12, rax
00537145  48 83 D2 00                     adc rdx, 0
00537149  4D 03 E7                        add r12, r15
0053714C  48 83 D2 00                     adc rdx, 0
00537150  4C 8B FA                        mov r15, rdx
00537153  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
00537157  49 F7 E3                        mul r11
0053715A  4C 03 E8                        add r13, rax
0053715D  48 83 D2 00                     adc rdx, 0
00537161  4D 03 EF                        add r13, r15
00537164  48 83 D2 00                     adc rdx, 0
00537168  4C 8B FA                        mov r15, rdx
0053716B  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
0053716F  49 F7 E3                        mul r11
00537172  4C 03 F0                        add r14, rax
00537175  48 83 D2 00                     adc rdx, 0
00537179  4D 03 F7                        add r14, r15
0053717C  48 83 D2 00                     adc rdx, 0
00537180  4C 8B FA                        mov r15, rdx
00537183  4C 8B 41 18                     mov r8, qword ptr [rcx + 0x18]
00537187  48 81 C1 80 00 00 00            add rcx, 0x80
0053718E  4C 8B DE                        mov r11, rsi
00537191  4D 0F AF D8                     imul r11, r8
00537195  48 8B 01                        mov rax, qword ptr [rcx]
00537198  49 F7 E3                        mul r11
0053719B  48 83 C6 FF                     add rsi, -1
0053719F  48 83 D2 00                     adc rdx, 0
005371A3  48 8B F2                        mov rsi, rdx
005371A6  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
005371AA  49 F7 E3                        mul r11
005371AD  48 03 F8                        add rdi, rax
005371B0  48 83 D2 00                     adc rdx, 0
005371B4  48 03 FE                        add rdi, rsi
005371B7  48 83 D2 00                     adc rdx, 0
005371BB  48 8B F2                        mov rsi, rdx
005371BE  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
005371C2  49 F7 E3                        mul r11
005371C5  48 03 E8                        add rbp, rax
005371C8  48 83 D2 00                     adc rdx, 0
005371CC  48 03 EE                        add rbp, rsi
005371CF  48 83 D2 00                     adc rdx, 0
005371D3  48 8B F2                        mov rsi, rdx
005371D6  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
005371DA  49 F7 E3                        mul r11
005371DD  48 03 D8                        add rbx, rax
005371E0  48 83 D2 00                     adc rdx, 0
005371E4  48 03 DE                        add rbx, rsi
005371E7  48 83 D2 00                     adc rdx, 0
005371EB  48 8B F2                        mov rsi, rdx
005371EE  4C 8B DF                        mov r11, rdi
005371F1  4D 0F AF D8                     imul r11, r8
005371F5  48 8B 01                        mov rax, qword ptr [rcx]
005371F8  49 F7 E3                        mul r11
005371FB  48 83 C7 FF                     add rdi, -1
005371FF  48 83 D2 00                     adc rdx, 0
00537203  48 8B FA                        mov rdi, rdx
00537206  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0053720A  49 F7 E3                        mul r11
0053720D  48 03 E8                        add rbp, rax
00537210  48 83 D2 00                     adc rdx, 0
00537214  48 03 EF                        add rbp, rdi
00537217  48 83 D2 00                     adc rdx, 0
0053721B  48 8B FA                        mov rdi, rdx
0053721E  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00537222  49 F7 E3                        mul r11
00537225  48 03 D8                        add rbx, rax
00537228  48 83 D2 00                     adc rdx, 0
0053722C  48 03 DF                        add rbx, rdi
0053722F  48 83 D2 00                     adc rdx, 0
00537233  48 8B FA                        mov rdi, rdx
00537236  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0053723A  49 F7 E3                        mul r11
0053723D  4C 03 E0                        add r12, rax
00537240  48 83 D2 00                     adc rdx, 0
00537244  4C 03 E7                        add r12, rdi
00537247  48 83 D2 00                     adc rdx, 0
0053724B  48 8B FA                        mov rdi, rdx
0053724E  4C 8B DD                        mov r11, rbp
00537251  4D 0F AF D8                     imul r11, r8
00537255  48 8B 01                        mov rax, qword ptr [rcx]
00537258  49 F7 E3                        mul r11
0053725B  48 83 C5 FF                     add rbp, -1
0053725F  48 83 D2 00                     adc rdx, 0
00537263  48 8B EA                        mov rbp, rdx
00537266  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0053726A  49 F7 E3                        mul r11
0053726D  48 03 D8                        add rbx, rax
00537270  48 83 D2 00                     adc rdx, 0
00537274  48 03 DD                        add rbx, rbp
00537277  48 83 D2 00                     adc rdx, 0
0053727B  48 8B EA                        mov rbp, rdx
0053727E  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00537282  49 F7 E3                        mul r11
00537285  4C 03 E0                        add r12, rax
00537288  48 83 D2 00                     adc rdx, 0
0053728C  4C 03 E5                        add r12, rbp
0053728F  48 83 D2 00                     adc rdx, 0
00537293  48 8B EA                        mov rbp, rdx
00537296  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0053729A  49 F7 E3                        mul r11
0053729D  4C 03 E8                        add r13, rax
005372A0  48 83 D2 00                     adc rdx, 0
005372A4  4C 03 ED                        add r13, rbp
005372A7  48 83 D2 00                     adc rdx, 0
005372AB  48 8B EA                        mov rbp, rdx
005372AE  4C 8B DB                        mov r11, rbx
005372B1  4D 0F AF D8                     imul r11, r8
005372B5  48 8B 01                        mov rax, qword ptr [rcx]
005372B8  49 F7 E3                        mul r11
005372BB  48 83 C3 FF                     add rbx, -1
005372BF  48 83 D2 00                     adc rdx, 0
005372C3  48 8B DA                        mov rbx, rdx
005372C6  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
005372CA  49 F7 E3                        mul r11
005372CD  4C 03 E0                        add r12, rax
005372D0  48 83 D2 00                     adc rdx, 0
005372D4  4C 03 E3                        add r12, rbx
005372D7  48 83 D2 00                     adc rdx, 0
005372DB  48 8B DA                        mov rbx, rdx
005372DE  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
005372E2  49 F7 E3                        mul r11
005372E5  4C 03 E8                        add r13, rax
005372E8  48 83 D2 00                     adc rdx, 0
005372EC  4C 03 EB                        add r13, rbx
005372EF  48 83 D2 00                     adc rdx, 0
005372F3  48 8B DA                        mov rbx, rdx
005372F6  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
005372FA  49 F7 E3                        mul r11
005372FD  4C 03 F0                        add r14, rax
00537300  48 83 D2 00                     adc rdx, 0
00537304  4C 03 F3                        add r14, rbx
00537307  48 83 D2 00                     adc rdx, 0
0053730B  4C 03 E6                        add r12, rsi
0053730E  4C 13 EF                        adc r13, rdi
00537311  4C 13 F5                        adc r14, rbp
00537314  4C 13 FA                        adc r15, rdx
00537317  4D 1B DB                        sbb r11, r11
0053731A  49 8B F4                        mov rsi, r12
0053731D  48 2B 31                        sub rsi, qword ptr [rcx]
00537320  49 8B FD                        mov rdi, r13
00537323  48 1B 79 08                     sbb rdi, qword ptr [rcx + 8]
00537327  49 8B EE                        mov rbp, r14
0053732A  48 1B 69 10                     sbb rbp, qword ptr [rcx + 0x10]
0053732E  49 8B DF                        mov rbx, r15
00537331  48 1B 59 18                     sbb rbx, qword ptr [rcx + 0x18]
00537335  48 1B C9                        sbb rcx, rcx
00537338  49 33 CB                        xor rcx, r11
0053733B  4C 0F 44 E6                     cmove r12, rsi
0053733F  4C 0F 44 EF                     cmove r13, rdi
00537343  4C 0F 44 F5                     cmove r14, rbp
00537347  4C 0F 44 FB                     cmove r15, rbx
0053734B  4D 89 21                        mov qword ptr [r9], r12
0053734E  4D 89 69 08                     mov qword ptr [r9 + 8], r13
00537352  4D 89 71 10                     mov qword ptr [r9 + 0x10], r14
00537356  4D 89 79 18                     mov qword ptr [r9 + 0x18], r15
0053735A  41 5F                           pop r15
0053735C  41 5E                           pop r14
0053735E  41 5D                           pop r13
00537360  41 5C                           pop r12
00537362  5B                              pop rbx
00537363  5D                              pop rbp
00537364  5F                              pop rdi
00537365  5E                              pop rsi
00537366  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModMulMontgomery256Asm(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;

    v_rbp = 0;
    v_rbx = 0;
    v_r12 = 0;
    v_rdi = (a2) + (*(unsigned __int64 *)(a3 + 8));
    v_rbp = (v_rbp) + (*(unsigned __int64 *)(a3 + 16));
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(a3 + 24));
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a3));
    v_rbp = (v_rbp) + (*(unsigned __int64 *)(a3 + 8));
    v_rbp = (v_rbp) + (a2);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(a3 + 16));
    v_rbx = (v_rbx) + (a2);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(a3 + 24));
    v_r12 = (v_r12) + (a2);
    v_rbp = (v_rbp) + (*(unsigned __int64 *)(a3));
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(a3 + 8));
    v_rbx = (v_rbx) + (a2);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(a3 + 16));
    v_r12 = (v_r12) + (a2);
    v_r13 = (a2) + (*(unsigned __int64 *)(a3 + 24));
    v_r13 = (v_r13) + (a2);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(a3));
    v_r12 = (v_r12) + (*(unsigned __int64 *)(a3 + 8));
    v_r12 = (v_r12) + (a2);
    v_r13 = (v_r13) + (*(unsigned __int64 *)(a3 + 16));
    v_r13 = (v_r13) + (a2);
    v_r14 = (a2) + (*(unsigned __int64 *)(a3 + 24));
    v_r14 = (v_r14) + (a2);
    a1 = (a1) + (128);
    v_r11 = (*(unsigned __int64 *)(a3)) * (*(unsigned __int64 *)(a1 + 24));
    v_rsi = (*(unsigned __int64 *)(a3)) + (-1);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a1 + 8));
    v_rdi = (v_rdi) + (a2);
    v_rbp = (v_rbp) + (*(unsigned __int64 *)(a1 + 16));
    v_rbp = (v_rbp) + (a2);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(a1 + 24));
    v_rbx = (v_rbx) + (a2);
    v_r11 = (v_rdi) * (*(unsigned __int64 *)(a1 + 24));
    v_rdi = (v_rdi) + (-1);
    v_rbp = (v_rbp) + (*(unsigned __int64 *)(a1 + 8));
    v_rbp = (v_rbp) + (a2);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(a1 + 16));
    v_rbx = (v_rbx) + (a2);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(a1 + 24));
    v_r12 = (v_r12) + (a2);
    v_r11 = (v_rbp) * (*(unsigned __int64 *)(a1 + 24));
    v_rbp = (v_rbp) + (-1);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(a1 + 8));
    v_rbx = (v_rbx) + (a2);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(a1 + 16));
    v_r12 = (v_r12) + (a2);
    v_r13 = (v_r13) + (*(unsigned __int64 *)(a1 + 24));
    v_r13 = (v_r13) + (a2);
    v_r11 = (v_rbx) * (*(unsigned __int64 *)(a1 + 24));
    v_rbx = (v_rbx) + (-1);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(a1 + 8));
    v_r12 = (v_r12) + (a2);
    v_r13 = (v_r13) + (*(unsigned __int64 *)(a1 + 16));
    v_r13 = (v_r13) + (a2);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(a1 + 24));
    v_r14 = (v_r14) + (a2);
    v_r12 = (v_r12) + (a2);
    v_rsi = (v_r12) - (*(unsigned __int64 *)(a1));
    a1 = (a1) ^ (v_r11);
    if (condition_is_equal) {
        v_r12 = v_rsi;
        v_r13 = v_r13;
        v_r14 = v_r14;
        a2 = a2;
    }
    *(unsigned __int64 *)(a4) = v_r12;
    *(unsigned __int64 *)(a4 + 8) = v_r13;
    *(unsigned __int64 *)(a4 + 16) = v_r14;
    *(unsigned __int64 *)(a4 + 24) = a2;
    return *(unsigned __int64 *)(a1 + 24);
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModMulMontgomery256Asm(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;

    local_rbp = 0;
    local_rbx = 0;
    local_r12 = 0;
    local_rdi = (Arg2) + (*(uint64_t *)(arg3 + 0x8));
    local_rbp = (local_rbp) + (*(uint64_t *)(arg3 + 0x10));
    local_rbx = (local_rbx) + (*(uint64_t *)(arg3 + 0x18));
    local_rdi = (local_rdi) + (*(uint64_t *)(arg3));
    local_rbp = (local_rbp) + (*(uint64_t *)(arg3 + 0x8));
    local_rbp = (local_rbp) + (Arg2);
    local_rbx = (local_rbx) + (*(uint64_t *)(arg3 + 0x10));
    local_rbx = (local_rbx) + (Arg2);
    local_r12 = (local_r12) + (*(uint64_t *)(arg3 + 0x18));
    local_r12 = (local_r12) + (Arg2);
    local_rbp = (local_rbp) + (*(uint64_t *)(arg3));
    local_rbx = (local_rbx) + (*(uint64_t *)(arg3 + 0x8));
    local_rbx = (local_rbx) + (Arg2);
    local_r12 = (local_r12) + (*(uint64_t *)(arg3 + 0x10));
    local_r12 = (local_r12) + (Arg2);
    local_r13 = (Arg2) + (*(uint64_t *)(arg3 + 0x18));
    local_r13 = (local_r13) + (Arg2);
    local_rbx = (local_rbx) + (*(uint64_t *)(arg3));
    local_r12 = (local_r12) + (*(uint64_t *)(arg3 + 0x8));
    local_r12 = (local_r12) + (Arg2);
    local_r13 = (local_r13) + (*(uint64_t *)(arg3 + 0x10));
    local_r13 = (local_r13) + (Arg2);
    local_r14 = (Arg2) + (*(uint64_t *)(arg3 + 0x18));
    local_r14 = (local_r14) + (Arg2);
    Arg1 = (Arg1) + (128);
    local_r11 = (*(uint64_t *)(arg3)) * (*(uint64_t *)(arg1 + 0x18));
    local_rsi = (*(uint64_t *)(arg3)) + (-1);
    local_rdi = (local_rdi) + (*(uint64_t *)(arg1 + 0x8));
    local_rdi = (local_rdi) + (Arg2);
    local_rbp = (local_rbp) + (*(uint64_t *)(arg1 + 0x10));
    local_rbp = (local_rbp) + (Arg2);
    local_rbx = (local_rbx) + (*(uint64_t *)(arg1 + 0x18));
    local_rbx = (local_rbx) + (Arg2);
    local_r11 = (local_rdi) * (*(uint64_t *)(arg1 + 0x18));
    local_rdi = (local_rdi) + (-1);
    local_rbp = (local_rbp) + (*(uint64_t *)(arg1 + 0x8));
    local_rbp = (local_rbp) + (Arg2);
    local_rbx = (local_rbx) + (*(uint64_t *)(arg1 + 0x10));
    local_rbx = (local_rbx) + (Arg2);
    local_r12 = (local_r12) + (*(uint64_t *)(arg1 + 0x18));
    local_r12 = (local_r12) + (Arg2);
    local_r11 = (local_rbp) * (*(uint64_t *)(arg1 + 0x18));
    local_rbp = (local_rbp) + (-1);
    local_rbx = (local_rbx) + (*(uint64_t *)(arg1 + 0x8));
    local_rbx = (local_rbx) + (Arg2);
    local_r12 = (local_r12) + (*(uint64_t *)(arg1 + 0x10));
    local_r12 = (local_r12) + (Arg2);
    local_r13 = (local_r13) + (*(uint64_t *)(arg1 + 0x18));
    local_r13 = (local_r13) + (Arg2);
    local_r11 = (local_rbx) * (*(uint64_t *)(arg1 + 0x18));
    local_rbx = (local_rbx) + (-1);
    local_r12 = (local_r12) + (*(uint64_t *)(arg1 + 0x8));
    local_r12 = (local_r12) + (Arg2);
    local_r13 = (local_r13) + (*(uint64_t *)(arg1 + 0x10));
    local_r13 = (local_r13) + (Arg2);
    local_r14 = (local_r14) + (*(uint64_t *)(arg1 + 0x18));
    local_r14 = (local_r14) + (Arg2);
    local_r12 = (local_r12) + (Arg2);
    local_rsi = (local_r12) - (*(uint64_t *)(arg1));
    Arg1 = (Arg1) ^ (local_r11);
    if (condition_is_equal) {
        local_r12 = local_rsi;
        local_r13 = local_r13;
        local_r14 = local_r14;
        Arg2 = Arg2;
    }
    *(uint64_t *)(arg4) = local_r12;
    *(uint64_t *)(arg4 + 0x8) = local_r13;
    *(uint64_t *)(arg4 + 0x10) = local_r14;
    *(void **)(arg4 + 0x18) = Arg2;
    return *(uint64_t *)(arg1 + 0x18);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x18` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00537020&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00537020[BB_00537020]
```
