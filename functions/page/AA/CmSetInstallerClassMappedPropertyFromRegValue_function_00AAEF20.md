# CmSetInstallerClassMappedPropertyFromRegValue

- RVA: `0x00AAEF20`–`0x00AAF249` (길이 `809` bytes)
- VA: `0x0000000140AAEF20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00092598`
- 디코드: `223`개 명령, `809/809` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- `0x00AAEFED` → [CmOpenInstallerClassRegKey](../9D/CmOpenInstallerClassRegKey_function_009D4474.md) (function, `0x009D4474`)
- `0x00AAF107` → [PnpCtxRegSetValue](../99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x00AAF1A2` → [_PnpOpenPropertiesKey](../99/_PnpOpenPropertiesKey_function_009938A0.md) (function, `0x009938A0`)
- `0x00AAF202` → [PnpCtxRegSetValue](../99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x00AAF215` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00AAF223` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [CmSetInstallerClassMappedProperty](../83/CmSetInstallerClassMappedProperty_function_008310E8.md) at `0x0083120A`

### Static image references
- `0x00AAEF4F` → RVA `0x00B4D320` (`PAGE`; read)
- `0x00AAF00E` → RVA `0x00014350` (`.rdata`; read)
- `0x00AAF01B` → RVA `0x00014358` (`.rdata`; read)
- `0x00AAF033` → RVA `0x00027DA0` (`.rdata`; read)
- `0x00AAF040` → RVA `0x00027DA8` (`.rdata`; read)
- `0x00AAF054` → RVA `0x00027D10` (`.rdata`; read)
- `0x00AAF061` → RVA `0x00027D18` (`.rdata`; read)
- `0x00AAF075` → RVA `0x00014398` (`.rdata`; read)
- `0x00AAF082` → RVA `0x000143A0` (`.rdata`; read)
- `0x00AAF09D` → RVA `0x00021EF0` (`.rdata`; read)
- `0x00AAF0AA` → RVA `0x00021EF8` (`.rdata`; read)
- `0x00AAF0D5` → RVA `0x00AFCCD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AAF0E2` → RVA `0x00B06E20` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AAF138` → RVA `0x00027CC8` (`.rdata`; read)
- `0x00AAF145` → RVA `0x00027CD0` (`.rdata`; read)
- `0x00AAF1C2` → RVA `0x00027DD0` (`.rdata`; read)
- `0x00AAF1CF` → RVA `0x00027DD8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AAF215` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00AAF223` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAEF20  48 8B C4                        mov rax, rsp
00AAEF23  48 89 58 08                     mov qword ptr [rax + 8], rbx
00AAEF27  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00AAEF2B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00AAEF2F  4C 89 60 20                     mov qword ptr [rax + 0x20], r12
00AAEF33  55                              push rbp
00AAEF34  41 56                           push r14
00AAEF36  41 57                           push r15
00AAEF38  48 8B EC                        mov rbp, rsp
00AAEF3B  48 83 EC 60                     sub rsp, 0x60
00AAEF3F  45 8B 59 10                     mov r11d, dword ptr [r9 + 0x10]
00AAEF43  33 DB                           xor ebx, ebx
00AAEF45  21 5D E0                        and dword ptr [rbp - 0x20], ebx
00AAEF48  49 8B F9                        mov rdi, r9
00AAEF4B  48 21 5D E8                     and qword ptr [rbp - 0x18], rbx
00AAEF4F  4C 8D 0D CA E3 09 00            lea r9, [rip + 0x9e3ca]
00AAEF56  48 21 5D F0                     and qword ptr [rbp - 0x10], rbx
00AAEF5A  4D 8B F8                        mov r15, r8
00AAEF5D  45 33 D2                        xor r10d, r10d
00AAEF60  4C 8B F2                        mov r14, rdx
00AAEF63  4C 8B E1                        mov r12, rcx
00AAEF66  49 8B 11                        mov rdx, qword ptr [r9]
00AAEF69  49 8B F1                        mov rsi, r9
00AAEF6C  44 3B 5A 10                     cmp r11d, dword ptr [rdx + 0x10]
00AAEF70  75 15                           jne 0x140aaef87
00AAEF72  48 8B 0F                        mov rcx, qword ptr [rdi]
00AAEF75  48 2B 0A                        sub rcx, qword ptr [rdx]
00AAEF78  75 08                           jne 0x140aaef82
00AAEF7A  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00AAEF7E  48 2B 4A 08                     sub rcx, qword ptr [rdx + 8]
00AAEF82  48 85 C9                        test rcx, rcx
00AAEF85  74 0F                           je 0x140aaef96
00AAEF87  33 F6                           xor esi, esi
00AAEF89  41 FF C2                        inc r10d
00AAEF8C  49 83 C1 20                     add r9, 0x20
00AAEF90  41 83 FA 0D                     cmp r10d, 0xd
00AAEF94  72 D0                           jb 0x140aaef66
00AAEF96  48 85 F6                        test rsi, rsi
00AAEF99  75 0A                           jne 0x140aaefa5
00AAEF9B  BB 16 00 00 C0                  mov ebx, 0xc0000016
00AAEFA0  E9 83 02 00 00                  jmp 0x140aaf228
00AAEFA5  8B 4E 08                        mov ecx, dword ptr [rsi + 8]
00AAEFA8  8B 45 40                        mov eax, dword ptr [rbp + 0x40]
00AAEFAB  3B C1                           cmp eax, ecx
00AAEFAD  74 19                           je 0x140aaefc8
00AAEFAF  83 F8 19                        cmp eax, 0x19
00AAEFB2  75 0F                           jne 0x140aaefc3
00AAEFB4  83 F9 12                        cmp ecx, 0x12
00AAEFB7  74 0F                           je 0x140aaefc8
00AAEFB9  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AAEFBE  E9 65 02 00 00                  jmp 0x140aaf228
00AAEFC3  83 F8 02                        cmp eax, 2
00AAEFC6  73 F1                           jae 0x140aaefb9
00AAEFC8  4D 85 FF                        test r15, r15
00AAEFCB  75 2F                           jne 0x140aaeffc
00AAEFCD  48 21 5C 24 38                  and qword ptr [rsp + 0x38], rbx
00AAEFD2  48 8D 45 E8                     lea rax, [rbp - 0x18]
00AAEFD6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AAEFDB  49 8B D6                        mov rdx, r14
00AAEFDE  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
00AAEFE2  49 8B CC                        mov rcx, r12
00AAEFE5  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
00AAEFED  E8 82 54 F2 FF                  call 0x1409d4474
00AAEFF2  8B D8                           mov ebx, eax
00AAEFF4  85 C0                           test eax, eax
00AAEFF6  0F 88 10 02 00 00               js 0x140aaf20c
00AAEFFC  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00AAEFFF  4C 8B 76 10                     mov r14, qword ptr [rsi + 0x10]
00AAF003  8B 76 18                        mov esi, dword ptr [rsi + 0x18]
00AAF006  83 F8 07                        cmp eax, 7
00AAF009  75 20                           jne 0x140aaf02b
00AAF00B  48 8B 0F                        mov rcx, qword ptr [rdi]
00AAF00E  48 2B 0D 3B 53 56 FF            sub rcx, qword ptr [rip - 0xa9acc5]
00AAF015  75 0B                           jne 0x140aaf022
00AAF017  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00AAF01B  48 2B 0D 36 53 56 FF            sub rcx, qword ptr [rip - 0xa9acca]
00AAF022  48 85 C9                        test rcx, rcx
00AAF025  0F 84 8F 00 00 00               je 0x140aaf0ba
00AAF02B  83 F8 08                        cmp eax, 8
00AAF02E  75 1C                           jne 0x140aaf04c
00AAF030  48 8B 0F                        mov rcx, qword ptr [rdi]
00AAF033  48 2B 0D 66 8D 57 FF            sub rcx, qword ptr [rip - 0xa8729a]
00AAF03A  75 0B                           jne 0x140aaf047
00AAF03C  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00AAF040  48 2B 0D 61 8D 57 FF            sub rcx, qword ptr [rip - 0xa8729f]
00AAF047  48 85 C9                        test rcx, rcx
00AAF04A  74 6E                           je 0x140aaf0ba
00AAF04C  83 F8 09                        cmp eax, 9
00AAF04F  75 1C                           jne 0x140aaf06d
00AAF051  48 8B 0F                        mov rcx, qword ptr [rdi]
00AAF054  48 2B 0D B5 8C 57 FF            sub rcx, qword ptr [rip - 0xa8734b]
00AAF05B  75 0B                           jne 0x140aaf068
00AAF05D  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00AAF061  48 2B 0D B0 8C 57 FF            sub rcx, qword ptr [rip - 0xa87350]
00AAF068  48 85 C9                        test rcx, rcx
00AAF06B  74 4D                           je 0x140aaf0ba
00AAF06D  83 F8 0A                        cmp eax, 0xa
00AAF070  75 1C                           jne 0x140aaf08e
00AAF072  48 8B 0F                        mov rcx, qword ptr [rdi]
00AAF075  48 2B 0D 1C 53 56 FF            sub rcx, qword ptr [rip - 0xa9ace4]
00AAF07C  75 0B                           jne 0x140aaf089
00AAF07E  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00AAF082  48 2B 0D 17 53 56 FF            sub rcx, qword ptr [rip - 0xa9ace9]
00AAF089  48 85 C9                        test rcx, rcx
00AAF08C  74 2C                           je 0x140aaf0ba
00AAF08E  8B 4D 50                        mov ecx, dword ptr [rbp + 0x50]
00AAF091  83 F8 0F                        cmp eax, 0xf
00AAF094  0F 85 92 00 00 00               jne 0x140aaf12c
00AAF09A  48 8B 07                        mov rax, qword ptr [rdi]
00AAF09D  48 2B 05 4C 2E 57 FF            sub rax, qword ptr [rip - 0xa8d1b4]
00AAF0A4  75 0B                           jne 0x140aaf0b1
00AAF0A6  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00AAF0AA  48 2B 05 47 2E 57 FF            sub rax, qword ptr [rip - 0xa8d1b9]
00AAF0B1  48 85 C0                        test rax, rax
00AAF0B4  0F 85 2A 01 00 00               jne 0x140aaf1e4
00AAF0BA  83 7D 50 01                     cmp dword ptr [rbp + 0x50], 1
00AAF0BE  73 0A                           jae 0x140aaf0ca
00AAF0C0  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AAF0C5  E9 42 01 00 00                  jmp 0x140aaf20c
00AAF0CA  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00AAF0CE  8A 08                           mov cl, byte ptr [rax]
00AAF0D0  80 F9 FF                        cmp cl, 0xff
00AAF0D3  75 09                           jne 0x140aaf0de
00AAF0D5  48 8D 05 F4 DB 04 00            lea rax, [rip + 0x4dbf4]
00AAF0DC  EB 0B                           jmp 0x140aaf0e9
00AAF0DE  84 C9                           test cl, cl
00AAF0E0  75 DE                           jne 0x140aaf0c0
00AAF0E2  48 8D 05 37 7D 05 00            lea rax, [rip + 0x57d37]
00AAF0E9  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00AAF0ED  4D 85 FF                        test r15, r15
00AAF0F0  49 0F 45 D7                     cmovne rdx, r15
00AAF0F4  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
00AAF0FC  44 8B CE                        mov r9d, esi
00AAF0FF  4D 8B C6                        mov r8, r14
00AAF102  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AAF107  E8 80 2A EE FF                  call 0x140991b8c
00AAF10C  3D 7C 01 00 C0                  cmp eax, 0xc000017c
00AAF111  75 0A                           jne 0x140aaf11d
00AAF113  BB 34 00 00 C0                  mov ebx, 0xc0000034
00AAF118  E9 EF 00 00 00                  jmp 0x140aaf20c
00AAF11D  85 C0                           test eax, eax
00AAF11F  0F 89 E7 00 00 00               jns 0x140aaf20c
00AAF125  8B D8                           mov ebx, eax
00AAF127  E9 E0 00 00 00                  jmp 0x140aaf20c
00AAF12C  83 F8 02                        cmp eax, 2
00AAF12F  0F 85 85 00 00 00               jne 0x140aaf1ba
00AAF135  48 8B 07                        mov rax, qword ptr [rdi]
00AAF138  48 2B 05 89 8B 57 FF            sub rax, qword ptr [rip - 0xa87477]
00AAF13F  75 0B                           jne 0x140aaf14c
00AAF141  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00AAF145  48 2B 05 84 8B 57 FF            sub rax, qword ptr [rip - 0xa8747c]
00AAF14C  48 85 C0                        test rax, rax
00AAF14F  0F 85 8F 00 00 00               jne 0x140aaf1e4
00AAF155  83 F9 01                        cmp ecx, 1
00AAF158  0F 82 62 FF FF FF               jb 0x140aaf0c0
00AAF15E  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00AAF162  8A 08                           mov cl, byte ptr [rax]
00AAF164  80 F9 FF                        cmp cl, 0xff
00AAF167  75 07                           jne 0x140aaf170
00AAF169  B8 01 00 00 00                  mov eax, 1
00AAF16E  EB 0A                           jmp 0x140aaf17a
00AAF170  84 C9                           test cl, cl
00AAF172  0F 85 48 FF FF FF               jne 0x140aaf0c0
00AAF178  33 C0                           xor eax, eax
00AAF17A  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00AAF17E  4D 85 FF                        test r15, r15
00AAF181  89 45 E0                        mov dword ptr [rbp - 0x20], eax
00AAF184  41 B9 02 00 00 00               mov r9d, 2
00AAF18A  48 8D 45 F0                     lea rax, [rbp - 0x10]
00AAF18E  49 0F 45 D7                     cmovne rdx, r15
00AAF192  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AAF197  45 33 C0                        xor r8d, r8d
00AAF19A  49 8B CC                        mov rcx, r12
00AAF19D  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00AAF1A2  E8 F9 46 EE FF                  call 0x1409938a0
00AAF1A7  8B D8                           mov ebx, eax
00AAF1A9  85 C0                           test eax, eax
00AAF1AB  78 5F                           js 0x140aaf20c
00AAF1AD  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00AAF1B1  48 8D 45 E0                     lea rax, [rbp - 0x20]
00AAF1B5  E9 3A FF FF FF                  jmp 0x140aaf0f4
00AAF1BA  83 F8 03                        cmp eax, 3
00AAF1BD  75 25                           jne 0x140aaf1e4
00AAF1BF  48 8B 07                        mov rax, qword ptr [rdi]
00AAF1C2  48 2B 05 07 8C 57 FF            sub rax, qword ptr [rip - 0xa873f9]
00AAF1C9  75 0B                           jne 0x140aaf1d6
00AAF1CB  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00AAF1CF  48 2B 05 02 8C 57 FF            sub rax, qword ptr [rip - 0xa873fe]
00AAF1D6  48 85 C0                        test rax, rax
00AAF1D9  75 09                           jne 0x140aaf1e4
00AAF1DB  83 F9 40                        cmp ecx, 0x40
00AAF1DE  0F 87 DC FE FF FF               ja 0x140aaf0c0
00AAF1E4  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00AAF1E8  4D 85 FF                        test r15, r15
00AAF1EB  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00AAF1EF  44 8B CE                        mov r9d, esi
00AAF1F2  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00AAF1F6  49 0F 45 D7                     cmovne rdx, r15
00AAF1FA  4D 8B C6                        mov r8, r14
00AAF1FD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AAF202  E8 85 29 EE FF                  call 0x140991b8c
00AAF207  85 C0                           test eax, eax
00AAF209  0F 48 D8                        cmovs ebx, eax
00AAF20C  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00AAF210  48 85 C9                        test rcx, rcx
00AAF213  74 05                           je 0x140aaf21a
00AAF215  E8 96 E0 BF FF                  call 0x1406ad2b0
00AAF21A  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00AAF21E  48 85 C9                        test rcx, rcx
00AAF221  74 05                           je 0x140aaf228
00AAF223  E8 88 E0 BF FF                  call 0x1406ad2b0
00AAF228  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00AAF22D  8B C3                           mov eax, ebx
00AAF22F  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
00AAF233  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
00AAF237  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
00AAF23B  4D 8B 63 38                     mov r12, qword ptr [r11 + 0x38]
00AAF23F  49 8B E3                        mov rsp, r11
00AAF242  41 5F                           pop r15
00AAF244  41 5E                           pop r14
00AAF246  5D                              pop rbp
00AAF247  C3                              ret
00AAF248  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSetInstallerClassMappedPropertyFromRegValue(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned int v_stack_m58;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r12;
    v_rsp = (v_rsp) - (96);
    v_rbx = 0;
    v_r10 = 0;
loc_00AAEF66:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 648138) + 16))) goto loc_00AAEF87;
    a1 = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 648138)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a4 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 648138) + 8));
    }
    if (a1 == 0) goto loc_00AAEF96;
loc_00AAEF87:
    v_rsi = 0;
    v_r10 = (unsigned int)((v_r10) + 1);
    a4 = (v_rip + 648138) + (32);
    if (((unsigned int)(v_r10)) < 13) goto loc_00AAEF66;
loc_00AAEF96:
    if (0 != 0) goto loc_00AAEFA5;
    goto loc_00AAF228;
loc_00AAEFA5:
    if (((unsigned int)((unsigned int)(a5))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 8))))) goto loc_00AAEFC8;
    if (((unsigned int)((unsigned int)(a5))) != 25) goto loc_00AAEFC3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 8)))) == 18) goto loc_00AAEFC8;
loc_00AAEFB9:
    goto loc_00AAF228;
loc_00AAEFC3:
    if (((unsigned int)((unsigned int)(a5))) >= 2) goto loc_00AAEFB9;
loc_00AAEFC8:
    if (a3 != 0) goto loc_00AAEFFC;
    v_stack_m48 = v_stack_m30;
    v_stack_m50 = (unsigned __int8)((unsigned int)(0xC000000DULL));
    v_stack_m58 = 3;
    result = CmOpenInstallerClassRegKey(a1, a2, a3, a4);
    if (sign_flag) goto loc_00AAF20C;
loc_00AAEFFC:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 7) goto loc_00AAF02B;
    a1 = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 11119813));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a4 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 11119818));
    }
    if (a1 == 0) goto loc_00AAF0BA;
loc_00AAF02B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 8) goto loc_00AAF04C;
    a1 = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 11039386));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a4 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 11039391));
    }
    if (a1 == 0) goto loc_00AAF0BA;
loc_00AAF04C:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 9) goto loc_00AAF06D;
    a1 = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 11039563));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a4 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 11039568));
    }
    if (a1 == 0) goto loc_00AAF0BA;
loc_00AAF06D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 10) goto loc_00AAF08E;
    a1 = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 11119844));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(a4 + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 11119849));
    }
    if (a1 == 0) goto loc_00AAF0BA;
loc_00AAF08E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 15) goto loc_00AAF12C;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 11063732));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 11063737));
    }
    if (result != 0) goto loc_00AAF1E4;
loc_00AAF0BA:
    if (a7 >= 1) goto loc_00AAF0CA;
loc_00AAF0C0:
    goto loc_00AAF20C;
loc_00AAF0CA:
    if (((unsigned __int8)(*(unsigned __int8 *)(a6))) != 255) goto loc_00AAF0DE;
    goto loc_00AAF0E9;
loc_00AAF0DE:
    if ((unsigned __int8)(*(unsigned __int8 *)(a6)) != 0) goto loc_00AAF0C0;
loc_00AAF0E9:
    a2 = v_stack_m30;
    if (a3 != 0) { a2 = a3; }
loc_00AAF0F4:
    v_stack_m50 = 4;
    v_stack_m58 = v_rip + 359735;
    result = PnpCtxRegSetValue(*(unsigned __int8 *)(a6), a2, *(unsigned __int64 *)(v_rsi + 16), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 24)))));
    if (((unsigned int)(result)) != 0xC000017CULL) goto loc_00AAF11D;
    goto loc_00AAF20C;
loc_00AAF11D:
    if (!sign_flag) goto loc_00AAF20C;
    goto loc_00AAF20C;
loc_00AAF12C:
    if (((unsigned int)(result)) != 2) goto loc_00AAF1BA;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 11039863));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 11039868));
    }
    if (result != 0) goto loc_00AAF1E4;
    if (((unsigned int)(*(unsigned __int8 *)(a6))) < 1) goto loc_00AAF0C0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a6))) != 255) goto loc_00AAF170;
    goto loc_00AAF17A;
loc_00AAF170:
    if ((unsigned __int8)(*(unsigned __int8 *)(a6)) != 0) goto loc_00AAF0C0;
    result = 0;
loc_00AAF17A:
    v_stack_m38 = 0;
    a2 = v_stack_m30;
    if (a3 != 0) { a2 = a3; }
    v_stack_m48 = v_stack_m28;
    a3 = 0;
    v_stack_m58 = 1;
    result = _PnpOpenPropertiesKey(a1, a2, a3, 2);
    if (sign_flag) goto loc_00AAF20C;
    goto loc_00AAF0F4;
loc_00AAF1BA:
    if (((unsigned int)(v_stack_m38)) != 3) goto loc_00AAF1E4;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 11039737));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 11039742));
    }
    if (result != 0) goto loc_00AAF1E4;
    if (((unsigned int)(a1)) > 64) goto loc_00AAF0C0;
loc_00AAF1E4:
    v_stack_m50 = (unsigned int)(a1);
    a2 = v_stack_m30;
    if (0 != 0) { a2 = 0; }
    v_stack_m58 = a6;
    result = PnpCtxRegSetValue(a1, a2, *(unsigned __int64 *)(v_rsi + 16), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 24)))));
    v_rbx = (unsigned int)((unsigned int)(result));
    if (sign_flag) { v_rbx = (unsigned int)(result); }
loc_00AAF20C:
    if (v_stack_m28 != 0) {
        result = ZwClose(v_stack_m28, a2, *(unsigned __int64 *)(v_rsi + 16), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 24)))));
    }
    if (v_stack_m30 != 0) {
        result = ZwClose(v_stack_m30, a2, *(unsigned __int64 *)(v_rsi + 16), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 24)))));
    }
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t CmSetInstallerClassMappedPropertyFromRegValue(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, void *Arg6, uint32_t Arg7)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint32_t v_stack_m58;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r12;
    local_rsp = (local_rsp) - (96);
    local_rbx = 0;
    local_r10 = 0;
loc_00AAEF66:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != (*(uint32_t *)(*(uint64_t *)(v_rip + 0x9E3CA) + 0x10))) goto loc_00AAEF87;
    Arg1 = (*(uint64_t *)(arg4)) - (*(uint64_t *)(*(uint64_t *)(v_rip + 0x9E3CA)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg4 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(v_rip + 0x9E3CA) + 0x8));
    }
    if (Arg1 == 0) goto loc_00AAEF96;
loc_00AAEF87:
    local_rsi = 0;
    local_r10 = (uint32_t)((local_r10) + 1);
    Arg4 = (v_rip + 648138) + (32);
    if (((uint32_t)(local_r10)) < 13) goto loc_00AAEF66;
loc_00AAEF96:
    if (0 != 0) goto loc_00AAEFA5;
    goto loc_00AAF228;
loc_00AAEFA5:
    if (((uint32_t)((uint32_t)(Arg5))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x8))))) goto loc_00AAEFC8;
    if (((uint32_t)((uint32_t)(Arg5))) != 25) goto loc_00AAEFC3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x8)))) == 18) goto loc_00AAEFC8;
loc_00AAEFB9:
    goto loc_00AAF228;
loc_00AAEFC3:
    if (((uint32_t)((uint32_t)(Arg5))) >= 2) goto loc_00AAEFB9;
loc_00AAEFC8:
    if (Arg3 != 0) goto loc_00AAEFFC;
    v_stack_m48 = v_stack_m30;
    v_stack_m50 = (uint8_t)((uint32_t)(0xC000000DULL));
    v_stack_m58 = 3;
    result = CmOpenInstallerClassRegKey(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00AAF20C;
loc_00AAEFFC:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 7) goto loc_00AAF02B;
    Arg1 = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0xA9ACC5));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg4 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0xA9ACCA));
    }
    if (Arg1 == 0) goto loc_00AAF0BA;
loc_00AAF02B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 8) goto loc_00AAF04C;
    Arg1 = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0xA8729A));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg4 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0xA8729F));
    }
    if (Arg1 == 0) goto loc_00AAF0BA;
loc_00AAF04C:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 9) goto loc_00AAF06D;
    Arg1 = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0xA8734B));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg4 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0xA87350));
    }
    if (Arg1 == 0) goto loc_00AAF0BA;
loc_00AAF06D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 10) goto loc_00AAF08E;
    Arg1 = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0xA9ACE4));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(arg4 + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0xA9ACE9));
    }
    if (Arg1 == 0) goto loc_00AAF0BA;
loc_00AAF08E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 15) goto loc_00AAF12C;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0xA8D1B4));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0xA8D1B9));
    }
    if (result != 0) goto loc_00AAF1E4;
loc_00AAF0BA:
    if (Arg7 >= 1) goto loc_00AAF0CA;
loc_00AAF0C0:
    goto loc_00AAF20C;
loc_00AAF0CA:
    if (((uint8_t)(*(uint8_t *)(arg6))) != 255) goto loc_00AAF0DE;
    goto loc_00AAF0E9;
loc_00AAF0DE:
    if ((uint8_t)(*(uint8_t *)(arg6)) != 0) goto loc_00AAF0C0;
loc_00AAF0E9:
    Arg2 = v_stack_m30;
    if (Arg3 != 0) { Arg2 = Arg3; }
loc_00AAF0F4:
    v_stack_m50 = 4;
    v_stack_m58 = v_rip + 359735;
    result = PnpCtxRegSetValue(*(uint8_t *)(arg6), Arg2, *(uint64_t *)(local_rsi + 0x10), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x18)))));
    if (((uint32_t)(result)) != 0xC000017CULL) goto loc_00AAF11D;
    goto loc_00AAF20C;
loc_00AAF11D:
    if (!sign_flag) goto loc_00AAF20C;
    goto loc_00AAF20C;
loc_00AAF12C:
    if (((uint32_t)(result)) != 2) goto loc_00AAF1BA;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0xA87477));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0xA8747C));
    }
    if (result != 0) goto loc_00AAF1E4;
    if (((uint32_t)(*(uint8_t *)(arg6))) < 1) goto loc_00AAF0C0;
    if (((uint8_t)(*(uint8_t *)(arg6))) != 255) goto loc_00AAF170;
    goto loc_00AAF17A;
loc_00AAF170:
    if ((uint8_t)(*(uint8_t *)(arg6)) != 0) goto loc_00AAF0C0;
    result = 0;
loc_00AAF17A:
    v_stack_m38 = 0;
    Arg2 = v_stack_m30;
    if (Arg3 != 0) { Arg2 = Arg3; }
    v_stack_m48 = v_stack_m28;
    Arg3 = 0;
    v_stack_m58 = 1;
    result = _PnpOpenPropertiesKey(Arg1, Arg2, Arg3, 2);
    if (sign_flag) goto loc_00AAF20C;
    goto loc_00AAF0F4;
loc_00AAF1BA:
    if (((uint32_t)(v_stack_m38)) != 3) goto loc_00AAF1E4;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0xA873F9));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0xA873FE));
    }
    if (result != 0) goto loc_00AAF1E4;
    if (((uint32_t)(Arg1)) > 64) goto loc_00AAF0C0;
loc_00AAF1E4:
    v_stack_m50 = (uint32_t)(Arg1);
    Arg2 = v_stack_m30;
    if (0 != 0) { Arg2 = 0; }
    v_stack_m58 = Arg6;
    result = PnpCtxRegSetValue(Arg1, Arg2, *(uint64_t *)(local_rsi + 0x10), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x18)))));
    local_rbx = (uint32_t)((uint32_t)(result));
    if (sign_flag) { local_rbx = (uint32_t)(result); }
loc_00AAF20C:
    if (v_stack_m28 != 0) {
        result = ZwClose(v_stack_m28, Arg2, *(uint64_t *)(local_rsi + 0x10), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x18)))));
    }
    if (v_stack_m30 != 0) {
        result = ZwClose(v_stack_m30, Arg2, *(uint64_t *)(local_rsi + 0x10), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x18)))));
    }
    return (uint32_t)((uint32_t)(local_rbx));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg6` | `+ 0x0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAEF20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
