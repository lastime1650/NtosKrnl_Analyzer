# ST_STORE&lt;SM_TRAITS&gt;::StDmpSinglePageLookup

- RVA: `0x003ABFF0`–`0x003AC3BA` (길이 `970` bytes)
- VA: `0x00000001403ABFF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008BAEC`
- 디코드: `262`개 명령, `970/970` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003AC0C1` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchResultDeref](B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC5D0.md) (function, `0x003AC5D0`)
- `0x003AC0D3` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchResultDeref](B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AC5D0.md) (function, `0x003AC5D0`)
- `0x003AC328` → [B_TREE<_SM_PAGE_KEY,ST_STORE<SM_TRAITS>::_ST_PAGE_ENTRY,4096,NP_CONTEXT,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeFindLeafSiblingEx](B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS__ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PAGE_function_003AA60C.md) (function, `0x003AA60C`)
- `0x003AC367` → [NP_CONTEXT::NpLeafRefInternal](NP_CONTEXT_NpLeafRefInternal_function_003AA340.md) (function, `0x003AA340`)
- `0x003AC39A` → [SmArrayGrow](SmArrayGrow_function_003AC6C8.md) (function, `0x003AC6C8`)

### Direct callers
- [sub_004201AA](../42/Unknown_function_004201AA.md) at `0x004202C5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003ABFF0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003ABFF5  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
003ABFFA  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
003ABFFF  57                              push rdi
003AC000  41 54                           push r12
003AC002  41 55                           push r13
003AC004  41 56                           push r14
003AC006  41 57                           push r15
003AC008  48 83 EC 20                     sub rsp, 0x20
003AC00C  48 8B B2 A8 01 00 00            mov rsi, qword ptr [rdx + 0x1a8]
003AC013  45 33 ED                        xor r13d, r13d
003AC016  4D 8B E1                        mov r12, r9
003AC019  49 8B F8                        mov rdi, r8
003AC01C  48 8B EA                        mov rbp, rdx
003AC01F  4C 8B F1                        mov r14, rcx
003AC022  45 38 28                        cmp byte ptr [r8], r13b
003AC025  0F 84 8C 00 00 00               je 0x1403ac0b7
003AC02B  48 8B 81 20 03 00 00            mov rax, qword ptr [rcx + 0x320]
003AC032  4C 8B 88 C0 1A 00 00            mov r9, qword ptr [rax + 0x1ac0]
003AC039  4C 39 8A B8 01 00 00            cmp qword ptr [rdx + 0x1b8], r9
003AC040  75 75                           jne 0x1403ac0b7
003AC042  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
003AC045  85 C0                           test eax, eax
003AC047  74 4B                           je 0x1403ac094
003AC049  8D 58 FF                        lea ebx, [rax - 1]
003AC04C  48 C1 E3 04                     shl rbx, 4
003AC050  48 03 1E                        add rbx, qword ptr [rsi]
003AC053  4C 8B 03                        mov r8, qword ptr [rbx]
003AC056  4C 8B 4B 08                     mov r9, qword ptr [rbx + 8]
003AC05A  49 83 C1 08                     add r9, 8
003AC05E  4C 89 4B 08                     mov qword ptr [rbx + 8], r9
003AC062  41 8B 08                        mov ecx, dword ptr [r8]
003AC065  0F B7 D1                        movzx edx, cx
003AC068  48 83 C2 02                     add rdx, 2
003AC06C  49 8D 14 D0                     lea rdx, [r8 + rdx*8]
003AC070  4C 3B CA                        cmp r9, rdx
003AC073  0F 83 94 02 00 00               jae 0x1403ac30d
003AC079  49 83 F9 FF                     cmp r9, -1
003AC07D  0F 84 F5 02 00 00               je 0x1403ac378
003AC083  4D 85 C9                        test r9, r9
003AC086  74 0C                           je 0x1403ac094
003AC088  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
003AC08B  41 39 01                        cmp dword ptr [r9], eax
003AC08E  0F 84 BE 01 00 00               je 0x1403ac252
003AC094  B8 25 02 00 C0                  mov eax, 0xc0000225
003AC099  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
003AC09E  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
003AC0A3  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
003AC0A8  48 83 C4 20                     add rsp, 0x20
003AC0AC  41 5F                           pop r15
003AC0AE  41 5E                           pop r14
003AC0B0  41 5D                           pop r13
003AC0B2  41 5C                           pop r12
003AC0B4  5F                              pop rdi
003AC0B5  C3                              ret
003AC0B6  CC                              int3
003AC0B7  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
003AC0BA  A8 01                           test al, 1
003AC0BC  75 08                           jne 0x1403ac0c6
003AC0BE  48 8B D6                        mov rdx, rsi
003AC0C1  E8 0A 05 00 00                  call 0x1403ac5d0
003AC0C6  83 4E 20 01                     or dword ptr [rsi + 0x20], 1
003AC0CA  48 8B D6                        mov rdx, rsi
003AC0CD  8B 5F 10                        mov ebx, dword ptr [rdi + 0x10]
003AC0D0  49 8B CE                        mov rcx, r14
003AC0D3  E8 F8 04 00 00                  call 0x1403ac5d0
003AC0D8  83 7E 18 FF                     cmp dword ptr [rsi + 0x18], -1
003AC0DC  0F 84 1F 02 00 00               je 0x1403ac301
003AC0E2  49 8B 06                        mov rax, qword ptr [r14]
003AC0E5  41 BF 01 00 00 00               mov r15d, 1
003AC0EB  41 8B CD                        mov ecx, r13d
003AC0EE  48 85 C0                        test rax, rax
003AC0F1  74 04                           je 0x1403ac0f7
003AC0F3  0F B6 48 02                     movzx ecx, byte ptr [rax + 2]
003AC0F7  39 4E 1C                        cmp dword ptr [rsi + 0x1c], ecx
003AC0FA  4C 8D 46 1C                     lea r8, [rsi + 0x1c]
003AC0FE  0F 82 93 02 00 00               jb 0x1403ac397
003AC104  48 8B 3E                        mov rdi, qword ptr [rsi]
003AC107  4D 8B 16                        mov r10, qword ptr [r14]
003AC10A  4D 85 D2                        test r10, r10
003AC10D  0F 84 6F 02 00 00               je 0x1403ac382
003AC113  0F 1F 40 00                     nop dword ptr [rax]
003AC117  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
003AC120  41 8B 0A                        mov ecx, dword ptr [r10]
003AC123  BA FF FF FF FF                  mov edx, 0xffffffff
003AC128  0F B7 C1                        movzx eax, cx
003AC12B  C1 E9 18                        shr ecx, 0x18
003AC12E  84 C9                           test cl, cl
003AC130  75 7E                           jne 0x1403ac1b0
003AC132  85 C0                           test eax, eax
003AC134  74 28                           je 0x1403ac15e
003AC136  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
003AC140  8D 0C 10                        lea ecx, [rax + rdx]
003AC143  D1 E9                           shr ecx, 1
003AC145  44 8B C9                        mov r9d, ecx
003AC148  48 03 C9                        add rcx, rcx
003AC14B  41 39 5C CA 10                  cmp dword ptr [r10 + rcx*8 + 0x10], ebx
003AC150  72 02                           jb 0x1403ac154
003AC152  75 57                           jne 0x1403ac1ab
003AC154  41 8B D1                        mov edx, r9d
003AC157  8D 4A 01                        lea ecx, [rdx + 1]
003AC15A  3B C8                           cmp ecx, eax
003AC15C  75 E2                           jne 0x1403ac140
003AC15E  45 38 6A 03                     cmp byte ptr [r10 + 3], r13b
003AC162  75 7C                           jne 0x1403ac1e0
003AC164  45 85 FF                        test r15d, r15d
003AC167  74 17                           je 0x1403ac180
003AC169  8B C8                           mov ecx, eax
003AC16B  48 FF C1                        inc rcx
003AC16E  4C 89 17                        mov qword ptr [rdi], r10
003AC171  48 C1 E1 04                     shl rcx, 4
003AC175  49 03 CA                        add rcx, r10
003AC178  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
003AC17C  48 83 C7 10                     add rdi, 0x10
003AC180  85 C0                           test eax, eax
003AC182  0F 84 70 01 00 00               je 0x1403ac2f8
003AC188  8D 48 FF                        lea ecx, [rax - 1]
003AC18B  48 C1 E1 04                     shl rcx, 4
003AC18F  48 83 C1 18                     add rcx, 0x18
003AC193  49 03 CA                        add rcx, r10
003AC196  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
003AC19A  83 38 FF                        cmp dword ptr [rax], -1
003AC19D  0F 85 A6 01 00 00               jne 0x1403ac349
003AC1A3  4C 8B 11                        mov r10, qword ptr [rcx]
003AC1A6  E9 75 FF FF FF                  jmp 0x1403ac120
003AC1AB  41 8B C1                        mov eax, r9d
003AC1AE  EB A7                           jmp 0x1403ac157
003AC1B0  85 C0                           test eax, eax
003AC1B2  74 AA                           je 0x1403ac15e
003AC1B4  0F 1F 40 00                     nop dword ptr [rax]
003AC1B8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
003AC1C0  8D 0C 10                        lea ecx, [rax + rdx]
003AC1C3  D1 E9                           shr ecx, 1
003AC1C5  44 8B C1                        mov r8d, ecx
003AC1C8  41 39 5C CA 10                  cmp dword ptr [r10 + rcx*8 + 0x10], ebx
003AC1CD  72 0C                           jb 0x1403ac1db
003AC1CF  41 8B C0                        mov eax, r8d
003AC1D2  8D 4A 01                        lea ecx, [rdx + 1]
003AC1D5  3B C8                           cmp ecx, eax
003AC1D7  75 E7                           jne 0x1403ac1c0
003AC1D9  EB 83                           jmp 0x1403ac15e
003AC1DB  41 8B D0                        mov edx, r8d
003AC1DE  EB F2                           jmp 0x1403ac1d2
003AC1E0  44 8B C0                        mov r8d, eax
003AC1E3  49 83 C0 02                     add r8, 2
003AC1E7  4C 89 17                        mov qword ptr [rdi], r10
003AC1EA  4F 8D 04 C2                     lea r8, [r10 + r8*8]
003AC1EE  4C 89 47 08                     mov qword ptr [rdi + 8], r8
003AC1F2  45 85 FF                        test r15d, r15d
003AC1F5  74 0C                           je 0x1403ac203
003AC1F7  48 2B 3E                        sub rdi, qword ptr [rsi]
003AC1FA  48 C1 FF 04                     sar rdi, 4
003AC1FE  FF C7                           inc edi
003AC200  89 7E 18                        mov dword ptr [rsi + 0x18], edi
003AC203  41 8B 0A                        mov ecx, dword ptr [r10]
003AC206  0F B7 D1                        movzx edx, cx
003AC209  3B C2                           cmp eax, edx
003AC20B  0F 83 83 FE FF FF               jae 0x1403ac094
003AC211  41 39 18                        cmp dword ptr [r8], ebx
003AC214  0F 85 7A FE FF FF               jne 0x1403ac094
003AC21A  49 8B 86 20 03 00 00            mov rax, qword ptr [r14 + 0x320]
003AC221  48 8B 88 C0 1A 00 00            mov rcx, qword ptr [rax + 0x1ac0]
003AC228  48 89 8D B8 01 00 00            mov qword ptr [rbp + 0x1b8], rcx
003AC22F  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
003AC232  83 F8 FF                        cmp eax, -1
003AC235  0F 84 76 01 00 00               je 0x1403ac3b1
003AC23B  85 C0                           test eax, eax
003AC23D  0F 84 6E 01 00 00               je 0x1403ac3b1
003AC243  44 8D 48 FF                     lea r9d, [rax - 1]
003AC247  49 C1 E1 04                     shl r9, 4
003AC24B  4C 03 0E                        add r9, qword ptr [rsi]
003AC24E  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
003AC252  45 8B 49 04                     mov r9d, dword ptr [r9 + 4]
003AC256  BA 01 00 00 00                  mov edx, 1
003AC25B  45 8B 96 C8 01 00 00            mov r10d, dword ptr [r14 + 0x1c8]
003AC262  45 8B C1                        mov r8d, r9d
003AC265  45 8B 9E CC 01 00 00            mov r11d, dword ptr [r14 + 0x1cc]
003AC26C  41 8B CA                        mov ecx, r10d
003AC26F  41 8B 9E D0 01 00 00            mov ebx, dword ptr [r14 + 0x1d0]
003AC276  41 8B C3                        mov eax, r11d
003AC279  41 8B BE D8 01 00 00            mov edi, dword ptr [r14 + 0x1d8]
003AC280  41 23 C1                        and eax, r9d
003AC283  41 D3 E8                        shr r8d, cl
003AC286  41 0F BD C8                     bsr ecx, r8d
003AC28A  0F AF C3                        imul eax, ebx
003AC28D  D3 E2                           shl edx, cl
003AC28F  49 33 D0                        xor rdx, r8
003AC292  48 03 D2                        add rdx, rdx
003AC295  49 8B 8C CE C0 00 00 00         mov rcx, qword ptr [r14 + rcx*8 + 0xc0]
003AC29D  4C 8B 04 D1                     mov r8, qword ptr [rcx + rdx*8]
003AC2A1  4C 03 C0                        add r8, rax
003AC2A4  4C 03 C7                        add r8, rdi
003AC2A7  41 83 38 FF                     cmp dword ptr [r8], -1
003AC2AB  75 3F                           jne 0x1403ac2ec
003AC2AD  45 8B 48 04                     mov r9d, dword ptr [r8 + 4]
003AC2B1  41 8B CA                        mov ecx, r10d
003AC2B4  41 8B D1                        mov edx, r9d
003AC2B7  41 B8 01 00 00 00               mov r8d, 1
003AC2BD  D3 EA                           shr edx, cl
003AC2BF  0F BD CA                        bsr ecx, edx
003AC2C2  41 D3 E0                        shl r8d, cl
003AC2C5  4C 33 C2                        xor r8, rdx
003AC2C8  4D 03 C0                        add r8, r8
003AC2CB  49 8B 94 CE C0 00 00 00         mov rdx, qword ptr [r14 + rcx*8 + 0xc0]
003AC2D3  41 8B CB                        mov ecx, r11d
003AC2D6  41 23 C9                        and ecx, r9d
003AC2D9  0F AF CB                        imul ecx, ebx
003AC2DC  4E 8B 04 C2                     mov r8, qword ptr [rdx + r8*8]
003AC2E0  4C 03 C1                        add r8, rcx
003AC2E3  4C 03 C7                        add r8, rdi
003AC2E6  41 83 38 FF                     cmp dword ptr [r8], -1
003AC2EA  74 C1                           je 0x1403ac2ad
003AC2EC  4D 89 04 24                     mov qword ptr [r12], r8
003AC2F0  41 8B C5                        mov eax, r13d
003AC2F3  E9 A1 FD FF FF                  jmp 0x1403ac099
003AC2F8  49 8D 4A 08                     lea rcx, [r10 + 8]
003AC2FC  E9 95 FE FF FF                  jmp 0x1403ac196
003AC301  45 8B FD                        mov r15d, r13d
003AC304  48 8D 7E 08                     lea rdi, [rsi + 8]
003AC308  E9 FA FD FF FF                  jmp 0x1403ac107
003AC30D  0F B7 C1                        movzx eax, cx
003AC310  49 83 C0 10                     add r8, 0x10
003AC314  48 8D 4A F8                     lea rcx, [rdx - 8]
003AC318  85 C0                           test eax, eax
003AC31A  48 8B D6                        mov rdx, rsi
003AC31D  4C 0F 45 C1                     cmovne r8, rcx
003AC321  49 8B CE                        mov rcx, r14
003AC324  4C 89 43 08                     mov qword ptr [rbx + 8], r8
003AC328  E8 DF E2 FF FF                  call 0x1403aa60c
003AC32D  48 85 C0                        test rax, rax
003AC330  0F 84 5E FD FF FF               je 0x1403ac094
003AC336  48 83 F8 FF                     cmp rax, -1
003AC33A  74 3C                           je 0x1403ac378
003AC33C  4C 8D 48 10                     lea r9, [rax + 0x10]
003AC340  4C 89 4B 08                     mov qword ptr [rbx + 8], r9
003AC344  E9 30 FD FF FF                  jmp 0x1403ac079
003AC349  41 80 7A 02 02                  cmp byte ptr [r10 + 2], 2
003AC34E  0F 85 4F FE FF FF               jne 0x1403ac1a3
003AC354  44 0F B6 46 20                  movzx r8d, byte ptr [rsi + 0x20]
003AC359  48 8B D1                        mov rdx, rcx
003AC35C  41 83 E0 01                     and r8d, 1
003AC360  49 8D 4E 10                     lea rcx, [r14 + 0x10]
003AC364  45 03 C0                        add r8d, r8d
003AC367  E8 D4 DF FF FF                  call 0x1403aa340
003AC36C  4C 8B D0                        mov r10, rax
003AC36F  48 85 C0                        test rax, rax
003AC372  0F 85 A8 FD FF FF               jne 0x1403ac120
003AC378  B8 06 00 00 C0                  mov eax, 0xc0000006
003AC37D  E9 17 FD FF FF                  jmp 0x1403ac099
003AC382  45 85 FF                        test r15d, r15d
003AC385  0F 85 09 FD FF FF               jne 0x1403ac094
003AC38B  4C 89 2F                        mov qword ptr [rdi], r13
003AC38E  4C 89 6F 08                     mov qword ptr [rdi + 8], r13
003AC392  E9 FD FC FF FF                  jmp 0x1403ac094
003AC397  4C 8B CE                        mov r9, rsi
003AC39A  E8 29 03 00 00                  call 0x1403ac6c8
003AC39F  85 C0                           test eax, eax
003AC3A1  0F 85 5D FD FF FF               jne 0x1403ac104
003AC3A7  B8 9A 00 00 C0                  mov eax, 0xc000009a
003AC3AC  E9 E8 FC FF FF                  jmp 0x1403ac099
003AC3B1  4C 8D 4E 08                     lea r9, [rsi + 8]
003AC3B5  E9 94 FE FF FF                  jmp 0x1403ac24e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___StDmpSinglePageLookup(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_r13 = 0;
    if ((*(unsigned __int8 *)(a3)) == 0) goto loc_003AC0B7;
    if ((*(unsigned __int64 *)(a2 + 440)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 800) + 6848))) goto loc_003AC0B7;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 424) + 24))) == 0) goto loc_003AC094;
    v_rbx = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 424) + 24)) - 1) << (4);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 424)));
    a4 = (*(unsigned __int64 *)(v_rbx + 8)) + (8);
    *(unsigned __int64 *)(v_rbx + 8) = a4;
    a2 = ((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx))))) + (2);
    if (a4 >= (*(unsigned __int64 *)(v_rbx) + a2 * 8)) goto loc_003AC30D;
loc_003AC079:
    if (a4 == -1) goto loc_003AC378;
    if (a4 == 0) goto loc_003AC094;
    if ((*(unsigned int *)(a4)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) goto loc_003AC252;
loc_003AC094:
loc_003AC099:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(0xC0000225ULL);
loc_003AC0B7:
    result = (unsigned int)(*(unsigned int *)(v_stack_p20 + 32));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) & (1)) == 0) {
        a2 = v_stack_p20;
        result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx))), a2, *(unsigned __int64 *)(v_rbx), a4);
    }
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, v_stack_p20, *(unsigned __int64 *)(v_rbx), a4);
    if ((*(unsigned int *)(v_stack_p20 + 24)) == -1) goto loc_003AC301;
    if (*(unsigned __int64 *)(a1) != 0) {
        a1 = *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 2);
    }
    if ((*(unsigned int *)(v_stack_p20 + 28)) < ((unsigned int)(a1))) goto loc_003AC397;
loc_003AC104:
loc_003AC107:
    if (*(unsigned __int64 *)(a1) == 0) goto loc_003AC382;
loc_003AC120:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1)))) >> (24));
    if ((unsigned __int8)(a1) != 0) goto loc_003AC1B0;
    if ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))) == 0) goto loc_003AC15E;
loc_003AC140:
    a1 = (unsigned int)(((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1)))) + (unsigned int)(0xFFFFFFFFULL) * 1) >> (1));
    a1 = (a1) + (a1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + a1 * 8 + 16)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) goto loc_003AC154;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + a1 * 8 + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) goto loc_003AC1AB;
loc_003AC154:
loc_003AC157:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + 1)) != ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))))) goto loc_003AC140;
loc_003AC15E:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 3)) != 0) goto loc_003AC1E0;
    v_rdi = *(unsigned __int64 *)(v_stack_p20);
    if (1 != 0) {
        a1 = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1)))));
        a1 = (a1) + 1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20)) = *(unsigned __int64 *)(a1);
        a1 = (a1) << (4);
        a1 = (a1) + (*(unsigned __int64 *)(a1));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20) + 8) = a1;
        v_rdi = (*(unsigned __int64 *)(v_stack_p20)) + (16);
    }
    if ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))) == 0) goto loc_003AC2F8;
    a1 = ((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1)))) - 1) << (4);
    a1 = (a1) + (24);
    a1 = (a1) + (*(unsigned __int64 *)(a1));
loc_003AC196:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16))) != -1) goto loc_003AC349;
loc_003AC1A3:
    goto loc_003AC120;
loc_003AC1AB:
    goto loc_003AC157;
loc_003AC1B0:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))))) == 0) goto loc_003AC15E;
loc_003AC1C0:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) * 1) >> (1));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + a1 * 8 + 16)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) goto loc_003AC1DB;
loc_003AC1D2:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + 1)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))))))) goto loc_003AC1C0;
    goto loc_003AC15E;
loc_003AC1DB:
    goto loc_003AC1D2;
loc_003AC1E0:
    a3 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))))))) + (2);
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(a1) + a3 * 8;
    if (1 != 0) {
        v_rdi = (v_rdi) - (*(unsigned __int64 *)(v_stack_p20));
        v_rdi = (v_rdi) >> (4);
        v_rdi = (unsigned int)((v_rdi) + 1);
        *(unsigned int *)(v_stack_p20 + 24) = (unsigned int)(v_rdi);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))))) >= ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))))) goto loc_003AC094;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + a3 * 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) goto loc_003AC094;
    *(unsigned __int64 *)(v_stack_p18 + 440) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 800) + 6848);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 24)))) == -1) goto loc_003AC3B1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 24))) == 0) goto loc_003AC3B1;
    a4 = ((unsigned int)(*(unsigned int *)(v_stack_p20 + 24)) - 1) << (4);
    a4 = (a4) + (*(unsigned __int64 *)(v_stack_p20));
loc_003AC24E:
loc_003AC252:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 460))))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8) + 4)))));
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8) + 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 456)))))));
    result = (unsigned int)((result) * ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 464)))));
    a2 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 456)))))));
    a2 = (a2) ^ (a3);
    a2 = (a2) + (a2);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 456)))) * 8 + 192) + a2 * 8)) + (result);
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(a1 + 472)));
    if ((*(unsigned int *)(a3)) != -1) goto loc_003AC2EC;
loc_003AC2AD:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 456)))))));
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 456)))))));
    a3 = (a3) ^ (a2);
    a3 = (a3) + (a3);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 460))))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))));
    a1 = (unsigned int)((a1) * ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 464)))));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 456)))) * 8 + 192) + a3 * 8)) + (a1);
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(a1 + 472)));
    if ((*(unsigned int *)(a3)) == -1) goto loc_003AC2AD;
loc_003AC2EC:
    *(unsigned __int64 *)(a4) = a3;
    goto loc_003AC099;
loc_003AC2F8:
    goto loc_003AC196;
loc_003AC301:
    goto loc_003AC107;
loc_003AC30D:
    a3 = (a3) + (16);
    if ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(a1 + 456)) + 8)) != 0) { a3 = *(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 456)))) * 8 + 192) - 8; }
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 464)) + 8) = a3;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(a1, v_stack_p20, a3, (unsigned int)(*(unsigned int *)(a3 + 4)));
    if (result == 0) goto loc_003AC094;
    if (result == -1) goto loc_003AC378;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 464)) + 8) = result + 16;
    goto loc_003AC079;
loc_003AC349:
    if ((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 456)) + 2)) != 2) goto loc_003AC1A3;
    a3 = (unsigned int)((*(unsigned __int8 *)(v_stack_p20 + 32)) & (1));
    a3 = (unsigned int)((a3) + ((unsigned int)(a3)));
    result = NP_CONTEXT__NpLeafRefInternal(a1 + 16, a1, a3, result + 16);
    if (result != 0) goto loc_003AC120;
loc_003AC378:
    goto loc_003AC099;
loc_003AC382:
    if (0 != 0) goto loc_003AC094;
    *(unsigned __int64 *)(v_stack_p20 + 8) = 0;
    *(unsigned __int64 *)(v_stack_p20 + 8 + 8) = 0;
    goto loc_003AC094;
loc_003AC397:
    result = SmArrayGrow(a1 + 16, a1, a3, v_stack_p20);
    if ((unsigned int)(result) != 0) goto loc_003AC104;
    goto loc_003AC099;
loc_003AC3B1:
    goto loc_003AC24E;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___StDmpSinglePageLookup(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_r13 = 0;
    if ((*(uint8_t *)(arg3)) == 0) goto loc_003AC0B7;
    if ((*(uint64_t *)(arg2 + 0x1B8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1AC0))) goto loc_003AC0B7;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x1A8) + 0x18))) == 0) goto loc_003AC094;
    local_rbx = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x1A8) + 0x18)) - 1) << (4);
    local_rbx = (local_rbx) + (*(uint64_t *)(*(uint64_t *)(arg2 + 0x1A8)));
    Arg4 = (*(uint64_t *)(local_rbx + 0x8)) + (8);
    *(void **)(local_rbx + 0x8) = Arg4;
    Arg2 = ((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx))))) + (2);
    if (Arg4 >= (*(uint64_t *)(local_rbx) + Arg2 * 8)) goto loc_003AC30D;
loc_003AC079:
    if (Arg4 == -1) goto loc_003AC378;
    if (Arg4 == NULL) goto loc_003AC094;
    if ((*(uint32_t *)(arg4)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10))))) goto loc_003AC252;
loc_003AC094:
loc_003AC099:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(0xC0000225ULL);
loc_003AC0B7:
    result = (uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) & (1)) == 0) {
        Arg2 = v_stack_p20;
        result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx))), Arg2, *(uint64_t *)(local_rbx), Arg4);
    }
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, v_stack_p20, *(uint64_t *)(local_rbx), Arg4);
    if ((*(uint32_t *)(v_stack_p20 + 0x18)) == -1) goto loc_003AC301;
    if (*(uint64_t *)(arg1) != 0) {
        Arg1 = *(uint8_t *)(*(uint64_t *)(arg1) + 0x2);
    }
    if ((*(uint32_t *)(v_stack_p20 + 0x1C)) < ((uint32_t)(Arg1))) goto loc_003AC397;
loc_003AC104:
loc_003AC107:
    if (*(uint64_t *)(arg1) == 0) goto loc_003AC382;
loc_003AC120:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1)))) >> (24));
    if ((uint8_t)(Arg1) != 0) goto loc_003AC1B0;
    if ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))) == 0) goto loc_003AC15E;
loc_003AC140:
    Arg1 = (uint32_t)(((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1)))) + (uint32_t)(0xFFFFFFFFULL) * 1) >> (1));
    Arg1 = (Arg1) + (Arg1);
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + arg1 * 8 + 0x10)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10))))) goto loc_003AC154;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + arg1 * 8 + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10))))) goto loc_003AC1AB;
loc_003AC154:
loc_003AC157:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + 1)) != ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))))) goto loc_003AC140;
loc_003AC15E:
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3)) != 0) goto loc_003AC1E0;
    local_rdi = *(uint64_t *)(v_stack_p20);
    if (1 != 0) {
        Arg1 = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1)))));
        Arg1 = (Arg1) + 1;
        *(uint64_t *)(*(uint64_t *)(v_stack_p20)) = *(uint64_t *)(arg1);
        Arg1 = (Arg1) << (4);
        Arg1 = (Arg1) + (*(uint64_t *)(arg1));
        *(void **)(*(uint64_t *)(v_stack_p20) + 0x8) = Arg1;
        local_rdi = (*(uint64_t *)(v_stack_p20)) + (16);
    }
    if ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))) == 0) goto loc_003AC2F8;
    Arg1 = ((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1)))) - 1) << (4);
    Arg1 = (Arg1) + (24);
    Arg1 = (Arg1) + (*(uint64_t *)(arg1));
loc_003AC196:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10))) != -1) goto loc_003AC349;
loc_003AC1A3:
    goto loc_003AC120;
loc_003AC1AB:
    goto loc_003AC157;
loc_003AC1B0:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))))) == 0) goto loc_003AC15E;
loc_003AC1C0:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) * 1) >> (1));
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + arg1 * 8 + 0x10)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10))))) goto loc_003AC1DB;
loc_003AC1D2:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + 1)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))))))) goto loc_003AC1C0;
    goto loc_003AC15E;
loc_003AC1DB:
    goto loc_003AC1D2;
loc_003AC1E0:
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))))))) + (2);
    *(uint64_t *)(local_rdi) = *(uint64_t *)(arg1);
    *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(arg1) + Arg3 * 8;
    if (1 != 0) {
        local_rdi = (local_rdi) - (*(uint64_t *)(v_stack_p20));
        local_rdi = (local_rdi) >> (4);
        local_rdi = (uint32_t)((local_rdi) + 1);
        *(uint32_t *)(v_stack_p20 + 0x18) = (uint32_t)(local_rdi);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))))) >= ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))))) goto loc_003AC094;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + arg3 * 8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10))))) goto loc_003AC094;
    *(uint64_t *)(v_stack_p18 + 0x1B8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x320) + 0x1AC0);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x18)))) == -1) goto loc_003AC3B1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x18))) == 0) goto loc_003AC3B1;
    Arg4 = ((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x18)) - 1) << (4);
    Arg4 = (Arg4) + (*(uint64_t *)(v_stack_p20));
loc_003AC24E:
loc_003AC252:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1CC))))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8) + 0x4)))));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8) + 0x4))))) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))))));
    result = (uint32_t)((result) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1D0)))));
    Arg2 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))))));
    Arg2 = (Arg2) ^ (Arg3);
    Arg2 = (Arg2) + (Arg2);
    Arg3 = (*(uint64_t *)(*(uint64_t *)(arg1 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))) * 8 + 0xC0) + arg2 * 8)) + (result);
    Arg3 = (Arg3) + ((uint32_t)(*(uint32_t *)(arg1 + 0x1D8)));
    if ((*(uint32_t *)(arg3)) != -1) goto loc_003AC2EC;
loc_003AC2AD:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4))))) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))))));
    Arg3 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))))));
    Arg3 = (Arg3) ^ (Arg2);
    Arg3 = (Arg3) + (Arg3);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1CC))))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)))));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1D0)))));
    Arg3 = (*(uint64_t *)(*(uint64_t *)(arg1 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))) * 8 + 0xC0) + arg3 * 8)) + (Arg1);
    Arg3 = (Arg3) + ((uint32_t)(*(uint32_t *)(arg1 + 0x1D8)));
    if ((*(uint32_t *)(arg3)) == -1) goto loc_003AC2AD;
loc_003AC2EC:
    *(void **)(arg4) = Arg3;
    goto loc_003AC099;
loc_003AC2F8:
    goto loc_003AC196;
loc_003AC301:
    goto loc_003AC107;
loc_003AC30D:
    Arg3 = (Arg3) + (16);
    if ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)) + 8)) != 0) { Arg3 = *(uint64_t *)(arg1 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)))) * 8 + 0xC0) - 8; }
    *(void **)((uint32_t)(*(uint32_t *)(arg1 + 0x1D0)) + 0x8) = Arg3;
    result = B_TREE__SM_PAGE_KEY_ST_STORE_SM_TRAITS____ST_PAGE_ENTRY_4096_NP_CONTEXT_B_TREE_KEY_COMPARATOR__SM_PA(Arg1, v_stack_p20, Arg3, (uint32_t)(*(uint32_t *)(arg3 + 0x4)));
    if (result == 0) goto loc_003AC094;
    if (result == -1) goto loc_003AC378;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x1D0)) + 0x8) = result + 16;
    goto loc_003AC079;
loc_003AC349:
    if ((*(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x1C8)) + 0x2)) != 2) goto loc_003AC1A3;
    Arg3 = (uint32_t)((*(uint8_t *)(v_stack_p20 + 0x20)) & (1));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(Arg3)));
    result = NP_CONTEXT__NpLeafRefInternal(Arg1 + 16, Arg1, Arg3, result + 16);
    if (result != 0) goto loc_003AC120;
loc_003AC378:
    goto loc_003AC099;
loc_003AC382:
    if (0 != 0) goto loc_003AC094;
    *(uint64_t *)(v_stack_p20 + 0x8) = 0;
    *(uint64_t *)(v_stack_p20 + 0x8 + 0x8) = 0;
    goto loc_003AC094;
loc_003AC397:
    result = SmArrayGrow(Arg1 + 16, Arg1, Arg3, v_stack_p20);
    if ((uint32_t)(result) != 0) goto loc_003AC104;
    goto loc_003AC099;
loc_003AC3B1:
    goto loc_003AC24E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0xC0 + rcx*8` | `64` | `R` |
| `Arg1` | `+ 0x1C8` | `32` | `R` |
| `Arg1` | `+ 0x1CC` | `32` | `R` |
| `Arg1` | `+ 0x1D0` | `32` | `R` |
| `Arg1` | `+ 0x1D8` | `32` | `R` |
| `Arg1` | `+ 0x320` | `64` | `R` |
| `Arg2` | `+ 0x1A8` | `64` | `R` |
| `Arg2` | `+ 0x1B8` | `64` | `R` |
| `Arg2` | `+ 0x1B8` | `64` | `W` |
| `Arg3` | `+ 0x0` | `8` | `R` |
| `Arg3` | `+ 0x10` | `32` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003ABFF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
