# RtlFindSetBitsAndClear

- RVA: `0x004B9070`–`0x004B9448` (길이 `984` bytes)
- VA: `0x00000001404B9070`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A3178`
- 디코드: `294`개 명령, `984/984` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B942F` → [RtlClearBits](../3E/RtlClearBits_function_003E1A90.md) (function, `0x003E1A90`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B9070  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
004B9075  53                              push rbx
004B9076  55                              push rbp
004B9077  56                              push rsi
004B9078  57                              push rdi
004B9079  41 54                           push r12
004B907B  41 55                           push r13
004B907D  41 56                           push r14
004B907F  41 57                           push r15
004B9081  48 83 EC 38                     sub rsp, 0x38
004B9085  44 8B 29                        mov r13d, dword ptr [rcx]
004B9088  44 8B DA                        mov r11d, edx
004B908B  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
004B908F  45 3B C5                        cmp r8d, r13d
004B9092  4C 8B E1                        mov r12, rcx
004B9095  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
004B909A  1B DB                           sbb ebx, ebx
004B909C  41 23 D8                        and ebx, r8d
004B909F  45 8D 4D FF                     lea r9d, [r13 - 1]
004B90A3  85 D2                           test edx, edx
004B90A5  75 08                           jne 0x1404b90af
004B90A7  83 E3 F8                        and ebx, 0xfffffff8
004B90AA  E9 73 03 00 00                  jmp 0x1404b9422
004B90AF  48 8B CF                        mov rcx, rdi
004B90B2  83 E1 04                        and ecx, 4
004B90B5  8B C1                           mov eax, ecx
004B90B7  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
004B90BF  48 F7 D8                        neg rax
004B90C2  8B C3                           mov eax, ebx
004B90C4  45 1B FF                        sbb r15d, r15d
004B90C7  41 83 E7 20                     and r15d, 0x20
004B90CB  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
004B90D3  41 8D 14 07                     lea edx, [r15 + rax]
004B90D7  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
004B90DE  47 8D 14 0F                     lea r10d, [r15 + r9]
004B90E2  48 8B C1                        mov rax, rcx
004B90E5  4C 8B F7                        mov r14, rdi
004B90E8  48 F7 D8                        neg rax
004B90EB  BB 40 00 00 00                  mov ebx, 0x40
004B90F0  41 8B C2                        mov eax, r10d
004B90F3  48 1B C9                        sbb rcx, rcx
004B90F6  2B C2                           sub eax, edx
004B90F8  83 E1 04                        and ecx, 4
004B90FB  FF C0                           inc eax
004B90FD  4C 2B F1                        sub r14, rcx
004B9100  41 3B C3                        cmp eax, r11d
004B9103  73 08                           jae 0x1404b910d
004B9105  83 CB FF                        or ebx, 0xffffffff
004B9108  E9 64 02 00 00                  jmp 0x1404b9371
004B910D  BF 3F 00 00 00                  mov edi, 0x3f
004B9112  8B CA                           mov ecx, edx
004B9114  40 22 CF                        and cl, dil
004B9117  41 8B EA                        mov ebp, r10d
004B911A  41 2B EB                        sub ebp, r11d
004B911D  FF C5                           inc ebp
004B911F  8B C5                           mov eax, ebp
004B9121  44 8D 47 C2                     lea r8d, [rdi - 0x3e]
004B9125  48 C1 E8 06                     shr rax, 6
004B9129  49 D3 E0                        shl r8, cl
004B912C  49 FF C8                        dec r8
004B912F  49 8D 34 C6                     lea rsi, [r14 + rax*8]
004B9133  8B C2                           mov eax, edx
004B9135  48 C1 E8 06                     shr rax, 6
004B9139  49 8D 14 C6                     lea rdx, [r14 + rax*8]
004B913D  48 8B 02                        mov rax, qword ptr [rdx]
004B9140  48 F7 D0                        not rax
004B9143  4C 0B C0                        or r8, rax
004B9146  41 83 FB 7F                     cmp r11d, 0x7f
004B914A  0F 86 E3 00 00 00               jbe 0x1404b9233
004B9150  40 84 EF                        test dil, bpl
004B9153  4C 8D 4E 08                     lea r9, [rsi + 8]
004B9157  4C 0F 44 CE                     cmove r9, rsi
004B915B  4D 85 C0                        test r8, r8
004B915E  75 04                           jne 0x1404b9164
004B9160  33 C9                           xor ecx, ecx
004B9162  EB 5F                           jmp 0x1404b91c3
004B9164  48 83 C2 08                     add rdx, 8
004B9168  48 8B 02                        mov rax, qword ptr [rdx]
004B916B  48 F7 D0                        not rax
004B916E  48 85 C0                        test rax, rax
004B9171  75 1C                           jne 0x1404b918f
004B9173  21 84 24 80 00 00 00            and dword ptr [rsp + 0x80], eax
004B917A  49 0F BD C0                     bsr rax, r8
004B917E  75 04                           jne 0x1404b9184
004B9180  8B CB                           mov ecx, ebx
004B9182  EB 3F                           jmp 0x1404b91c3
004B9184  8B CF                           mov ecx, edi
004B9186  2B C8                           sub ecx, eax
004B9188  EB 39                           jmp 0x1404b91c3
004B918A  BB 40 00 00 00                  mov ebx, 0x40
004B918F  48 8B CA                        mov rcx, rdx
004B9192  49 3B D1                        cmp rdx, r9
004B9195  0F 87 4C 02 00 00               ja 0x1404b93e7
004B919B  48 83 C2 08                     add rdx, 8
004B919F  48 8B 02                        mov rax, qword ptr [rdx]
004B91A2  48 F7 D0                        not rax
004B91A5  48 85 C0                        test rax, rax
004B91A8  75 E5                           jne 0x1404b918f
004B91AA  48 8B 01                        mov rax, qword ptr [rcx]
004B91AD  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
004B91B5  48 F7 D0                        not rax
004B91B8  4C 0F BD C0                     bsr r8, rax
004B91BC  74 C2                           je 0x1404b9180
004B91BE  8B CF                           mov ecx, edi
004B91C0  41 2B C8                        sub ecx, r8d
004B91C3  48 8B DA                        mov rbx, rdx
004B91C6  49 2B DE                        sub rbx, r14
004B91C9  48 C1 FB 03                     sar rbx, 3
004B91CD  C1 E3 06                        shl ebx, 6
004B91D0  2B D9                           sub ebx, ecx
004B91D2  3B DD                           cmp ebx, ebp
004B91D4  0F 87 0D 02 00 00               ja 0x1404b93e7
004B91DA  41 8B C3                        mov eax, r11d
004B91DD  2B C1                           sub eax, ecx
004B91DF  44 8B C0                        mov r8d, eax
004B91E2  48 C1 E8 06                     shr rax, 6
004B91E6  48 8D 0C C2                     lea rcx, [rdx + rax*8]
004B91EA  48 83 C2 08                     add rdx, 8
004B91EE  48 3B D1                        cmp rdx, rcx
004B91F1  74 0D                           je 0x1404b9200
004B91F3  48 8B 02                        mov rax, qword ptr [rdx]
004B91F6  48 F7 D0                        not rax
004B91F9  48 85 C0                        test rax, rax
004B91FC  75 8C                           jne 0x1404b918a
004B91FE  EB EA                           jmp 0x1404b91ea
004B9200  44 23 C7                        and r8d, edi
004B9203  0F 84 57 01 00 00               je 0x1404b9360
004B9209  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
004B9211  48 8B 02                        mov rax, qword ptr [rdx]
004B9214  48 F7 D0                        not rax
004B9217  48 0F BC C8                     bsf rcx, rax
004B921B  B8 40 00 00 00                  mov eax, 0x40
004B9220  0F 44 C8                        cmove ecx, eax
004B9223  41 3B C8                        cmp ecx, r8d
004B9226  0F 83 34 01 00 00               jae 0x1404b9360
004B922C  8B D8                           mov ebx, eax
004B922E  E9 5C FF FF FF                  jmp 0x1404b918f
004B9233  44 3B DB                        cmp r11d, ebx
004B9236  0F 83 89 00 00 00               jae 0x1404b92c5
004B923C  41 83 FB 01                     cmp r11d, 1
004B9240  0F 86 A9 01 00 00               jbe 0x1404b93ef
004B9246  33 DB                           xor ebx, ebx
004B9248  41 8B C2                        mov eax, r10d
004B924B  48 C1 E8 06                     shr rax, 6
004B924F  49 8D 3C C6                     lea rdi, [r14 + rax*8]
004B9253  49 83 F8 FF                     cmp r8, -1
004B9257  75 1B                           jne 0x1404b9274
004B9259  48 83 C2 08                     add rdx, 8
004B925D  48 3B D6                        cmp rdx, rsi
004B9260  0F 87 81 01 00 00               ja 0x1404b93e7
004B9266  4C 8B 02                        mov r8, qword ptr [rdx]
004B9269  49 F7 D0                        not r8
004B926C  49 83 F8 FF                     cmp r8, -1
004B9270  74 E7                           je 0x1404b9259
004B9272  33 DB                           xor ebx, ebx
004B9274  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
004B927C  B9 40 00 00 00                  mov ecx, 0x40
004B9281  49 0F BC C0                     bsf rax, r8
004B9285  0F 44 C1                        cmove eax, ecx
004B9288  03 C3                           add eax, ebx
004B928A  41 3B C3                        cmp eax, r11d
004B928D  0F 83 3E 01 00 00               jae 0x1404b93d1
004B9293  4D 8B C8                        mov r9, r8
004B9296  45 8B D3                        mov r10d, r11d
004B9299  49 F7 D1                        not r9
004B929C  49 8B C1                        mov rax, r9
004B929F  41 8B CA                        mov ecx, r10d
004B92A2  D1 E9                           shr ecx, 1
004B92A4  48 D3 E8                        shr rax, cl
004B92A7  4C 23 C8                        and r9, rax
004B92AA  0F 84 F1 00 00 00               je 0x1404b93a1
004B92B0  44 2B D1                        sub r10d, ecx
004B92B3  41 83 FA 01                     cmp r10d, 1
004B92B7  77 E3                           ja 0x1404b929c
004B92B9  49 0F BC D9                     bsf rbx, r9
004B92BD  E9 11 01 00 00                  jmp 0x1404b93d3
004B92C2  41 8B D9                        mov ebx, r9d
004B92C5  4D 85 C0                        test r8, r8
004B92C8  79 15                           jns 0x1404b92df
004B92CA  48 83 C2 08                     add rdx, 8
004B92CE  48 3B D6                        cmp rdx, rsi
004B92D1  0F 87 10 01 00 00               ja 0x1404b93e7
004B92D7  4C 8B 02                        mov r8, qword ptr [rdx]
004B92DA  49 F7 D0                        not r8
004B92DD  EB E6                           jmp 0x1404b92c5
004B92DF  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
004B92E7  49 0F BD C0                     bsr rax, r8
004B92EB  75 05                           jne 0x1404b92f2
004B92ED  44 8B C3                        mov r8d, ebx
004B92F0  EB 06                           jmp 0x1404b92f8
004B92F2  44 8B C7                        mov r8d, edi
004B92F5  44 2B C0                        sub r8d, eax
004B92F8  48 8B C2                        mov rax, rdx
004B92FB  49 2B C6                        sub rax, r14
004B92FE  48 C1 F8 03                     sar rax, 3
004B9302  FF C0                           inc eax
004B9304  C1 E0 06                        shl eax, 6
004B9307  41 2B C0                        sub eax, r8d
004B930A  8B D8                           mov ebx, eax
004B930C  3B C5                           cmp eax, ebp
004B930E  0F 87 D3 00 00 00               ja 0x1404b93e7
004B9314  41 8B CB                        mov ecx, r11d
004B9317  41 2B C8                        sub ecx, r8d
004B931A  74 44                           je 0x1404b9360
004B931C  48 83 C2 08                     add rdx, 8
004B9320  41 B9 40 00 00 00               mov r9d, 0x40
004B9326  48 8B 02                        mov rax, qword ptr [rdx]
004B9329  48 F7 D0                        not rax
004B932C  4C 8B C0                        mov r8, rax
004B932F  41 3B C9                        cmp ecx, r9d
004B9332  72 14                           jb 0x1404b9348
004B9334  48 85 C0                        test rax, rax
004B9337  75 89                           jne 0x1404b92c2
004B9339  83 C1 C0                        add ecx, -0x40
004B933C  74 22                           je 0x1404b9360
004B933E  48 83 C2 08                     add rdx, 8
004B9342  4C 8B 02                        mov r8, qword ptr [rdx]
004B9345  49 F7 D0                        not r8
004B9348  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
004B9350  49 0F BC C0                     bsf rax, r8
004B9354  41 0F 44 C1                     cmove eax, r9d
004B9358  3B C1                           cmp eax, ecx
004B935A  0F 82 62 FF FF FF               jb 0x1404b92c2
004B9360  83 FB FF                        cmp ebx, -1
004B9363  0F 85 B6 00 00 00               jne 0x1404b941f
004B9369  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
004B9371  83 BC 24 88 00 00 00 00         cmp dword ptr [rsp + 0x88], 0
004B9379  0F 84 A3 00 00 00               je 0x1404b9422
004B937F  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
004B9387  47 8D 0C 03                     lea r9d, [r11 + r8]
004B938B  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
004B9390  45 3B CD                        cmp r9d, r13d
004B9393  45 0F 47 CD                     cmova r9d, r13d
004B9397  41 FF C9                        dec r9d
004B939A  33 C0                           xor eax, eax
004B939C  E9 2A FD FF FF                  jmp 0x1404b90cb
004B93A1  48 3B D7                        cmp rdx, rdi
004B93A4  74 41                           je 0x1404b93e7
004B93A6  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
004B93AE  49 0F BD C0                     bsr rax, r8
004B93B2  75 07                           jne 0x1404b93bb
004B93B4  BB 40 00 00 00                  mov ebx, 0x40
004B93B9  EB 07                           jmp 0x1404b93c2
004B93BB  BB 3F 00 00 00                  mov ebx, 0x3f
004B93C0  2B D8                           sub ebx, eax
004B93C2  48 83 C2 08                     add rdx, 8
004B93C6  4C 8B 02                        mov r8, qword ptr [rdx]
004B93C9  49 F7 D0                        not r8
004B93CC  E9 82 FE FF FF                  jmp 0x1404b9253
004B93D1  F7 DB                           neg ebx
004B93D3  49 2B D6                        sub rdx, r14
004B93D6  48 C1 FA 03                     sar rdx, 3
004B93DA  C1 E2 06                        shl edx, 6
004B93DD  03 DA                           add ebx, edx
004B93DF  3B DD                           cmp ebx, ebp
004B93E1  0F 86 79 FF FF FF               jbe 0x1404b9360
004B93E7  83 CB FF                        or ebx, 0xffffffff
004B93EA  E9 7A FF FF FF                  jmp 0x1404b9369
004B93EF  49 83 F8 FF                     cmp r8, -1
004B93F3  75 11                           jne 0x1404b9406
004B93F5  48 83 C2 08                     add rdx, 8
004B93F9  48 3B D6                        cmp rdx, rsi
004B93FC  77 E9                           ja 0x1404b93e7
004B93FE  4C 8B 02                        mov r8, qword ptr [rdx]
004B9401  49 F7 D0                        not r8
004B9404  EB E9                           jmp 0x1404b93ef
004B9406  49 2B D6                        sub rdx, r14
004B9409  49 F7 D0                        not r8
004B940C  48 C1 FA 03                     sar rdx, 3
004B9410  49 0F BC C0                     bsf rax, r8
004B9414  C1 E2 06                        shl edx, 6
004B9417  03 D0                           add edx, eax
004B9419  8B DA                           mov ebx, edx
004B941B  3B D5                           cmp edx, ebp
004B941D  EB C2                           jmp 0x1404b93e1
004B941F  41 2B DF                        sub ebx, r15d
004B9422  83 FB FF                        cmp ebx, -1
004B9425  74 0D                           je 0x1404b9434
004B9427  45 8B C3                        mov r8d, r11d
004B942A  8B D3                           mov edx, ebx
004B942C  49 8B CC                        mov rcx, r12
004B942F  E8 5C 86 F2 FF                  call 0x1403e1a90
004B9434  8B C3                           mov eax, ebx
004B9436  48 83 C4 38                     add rsp, 0x38
004B943A  41 5F                           pop r15
004B943C  41 5E                           pop r14
004B943E  41 5D                           pop r13
004B9440  41 5C                           pop r12
004B9442  5F                              pop rdi
004B9443  5E                              pop rsi
004B9444  5D                              pop rbp
004B9445  5B                              pop rbx
004B9446  C3                              ret
004B9447  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlFindSetBitsAndClear(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (56);
    v_stack_m58 = *(unsigned __int64 *)(a1 + 8);
    v_rbx = (unsigned int)((v_rbx) & (a3));
    if (a2 != 0) goto loc_004B90AF;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFF8ULL));
    goto loc_004B9422;
loc_004B90AF:
    a1 = (unsigned int)((*(unsigned __int64 *)(a1 + 8)) & (4));
    v_stack_p20 = a1;
    result = -((unsigned int)((unsigned int)(a1)));
    v_r15 = (unsigned int)((v_r15) & (32));
loc_004B90CB:
    v_stack_p10 = (unsigned int)((unsigned int)((unsigned int)(v_rbx)));
    result = -(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15 + (unsigned int)(*(unsigned int *)(a1)) - 1 * 1))) - ((unsigned int)(v_r15 + (unsigned int)((unsigned int)(v_rbx)) * 1)));
    a1 = (unsigned int)((a1) & (4));
    result = (unsigned int)((result) + 1);
    v_r14 = (*(unsigned __int64 *)(a1 + 8)) - (a1);
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(a2)))) goto loc_004B910D;
    v_rbx = (unsigned int)((64) | (0xFFFFFFFFULL));
    goto loc_004B9371;
loc_004B910D:
    a1 = (unsigned __int8)(((unsigned int)((unsigned int)(v_r15 + (unsigned int)((unsigned int)(v_rbx)) * 1))) & (63));
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(v_r15 + (unsigned int)(*(unsigned int *)(a1)) - 1 * 1))) - ((unsigned int)((unsigned int)(a2))));
    v_rbp = (unsigned int)((v_rbp) + 1);
    result = ((unsigned int)((unsigned int)(v_rbp))) >> (6);
    a3 = (63 - 62) << ((unsigned __int8)(a1));
    a3 = (a3) - 1;
    result = ((unsigned int)((unsigned int)(v_r15 + (unsigned int)((unsigned int)(v_rbx)) * 1))) >> (6);
    result = ~(*(unsigned __int64 *)(v_r14 + result * 8));
    a3 = (a3) | (result);
    if (((unsigned int)((unsigned int)(a2))) <= 127) goto loc_004B9233;
    a4 = v_r14 + result * 8 + 8;
    if (((63) & ((unsigned __int8)(v_rbp))) == 0) { a4 = v_r14 + result * 8; }
    if (a3 != 0) goto loc_004B9164;
    a1 = 0;
    goto loc_004B91C3;
loc_004B9164:
    a2 = (v_r14 + result * 8) + (8);
    result = ~(*(unsigned __int64 *)(a2));
    if (result != 0) goto loc_004B918F;
    if (result != 0) goto loc_004B9184;
loc_004B9180:
    goto loc_004B91C3;
loc_004B9184:
    a1 = (unsigned int)((63) - ((unsigned int)(result)));
    goto loc_004B91C3;
loc_004B918A:
loc_004B918F:
    if (a2 > a4) goto loc_004B93E7;
    a2 = (a2) + (8);
    result = ~(*(unsigned __int64 *)(a2));
    if (result != 0) goto loc_004B918F;
    result = ~(*(unsigned __int64 *)(a2));
    if (result == 0) goto loc_004B9180;
    a1 = (unsigned int)((63) - (a3));
loc_004B91C3:
    v_rbx = (a2) - (v_r14);
    v_rbx = (v_rbx) >> (3);
    v_rbx = (unsigned int)((v_rbx) << (6));
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(a1)));
    if (((unsigned int)(v_rbx)) > ((unsigned int)(v_rbp))) goto loc_004B93E7;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)(a1)));
    result = (result) >> (6);
loc_004B91EA:
    a2 = (a2) + (8);
    if (a2 == (a2 + result * 8)) goto loc_004B9200;
    result = ~(*(unsigned __int64 *)(a2));
    if (result != 0) goto loc_004B918A;
    goto loc_004B91EA;
loc_004B9200:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (63));
    if (condition_is_equal) goto loc_004B9360;
    result = ~(*(unsigned __int64 *)(a2));
    a1 = a2 + result * 8;
    if (condition_is_equal) { a1 = 64; }
    if (((unsigned int)(a1)) >= a3) goto loc_004B9360;
    goto loc_004B918F;
loc_004B9233:
    if (((unsigned int)((unsigned int)(a2))) >= 64) goto loc_004B92C5;
    if (((unsigned int)((unsigned int)(a2))) <= 1) goto loc_004B93EF;
    v_rbx = 0;
    result = ((unsigned int)((unsigned int)(v_r15 + (unsigned int)(*(unsigned int *)(a1)) - 1 * 1))) >> (6);
loc_004B9253:
    if (a3 != -1) goto loc_004B9274;
loc_004B9259:
    a2 = (a2) + (8);
    if (a2 > (v_r14 + result * 8)) goto loc_004B93E7;
    a3 = ~(*(unsigned __int64 *)(a2));
    if (a3 == -1) goto loc_004B9259;
    v_rbx = 0;
loc_004B9274:
    if (condition_is_equal) { result = 64; }
    result = (unsigned int)((result) + (0));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(a2)))) goto loc_004B93D1;
    a4 = ~(a3);
loc_004B929C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2)))))) >> (1));
    result = (a4) >> ((unsigned __int8)(a1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_004B93A1;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)(a1)));
    if (((unsigned int)(v_r10)) > 1) goto loc_004B929C;
    goto loc_004B93D3;
loc_004B92C2:
loc_004B92C5:
    if (!sign_flag) goto loc_004B92DF;
    a2 = (a2) + (8);
    if (a2 > (v_r14 + result * 8)) goto loc_004B93E7;
    a3 = ~(*(unsigned __int64 *)(a2));
    goto loc_004B92C5;
loc_004B92DF:
    if (a2 != (v_r14 + result * 8)) goto loc_004B92F2;
    goto loc_004B92F8;
loc_004B92F2:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r14 + result * 8))) - ((unsigned int)(result)));
loc_004B92F8:
    result = (a2) - (v_r14);
    result = (result) >> (3);
    result = (unsigned int)((result) + 1);
    result = (unsigned int)((result) << (6));
    result = (unsigned int)((result) - (a3));
    if (((unsigned int)(result)) > ((unsigned int)(v_rbp))) goto loc_004B93E7;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - (a3));
    if (condition_is_equal) goto loc_004B9360;
    a2 = (a2) + (8);
    result = ~(*(unsigned __int64 *)(a2));
    if (((unsigned int)(a1)) < 64) goto loc_004B9348;
    if (result != 0) goto loc_004B92C2;
    a1 = (unsigned int)((a1) + (-64));
    if (condition_is_equal) goto loc_004B9360;
    a2 = (a2) + (8);
    a3 = ~(*(unsigned __int64 *)(a2));
loc_004B9348:
    if (condition_is_equal) { result = 64; }
    if (((unsigned int)(result)) < ((unsigned int)(a1))) goto loc_004B92C2;
loc_004B9360:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != -1) goto loc_004B941F;
loc_004B9369:
loc_004B9371:
    if (v_stack_p10 == 0) goto loc_004B9422;
    a4 = (unsigned int)(a2) + (unsigned int)(v_stack_p18) * 1;
    if (((unsigned int)((unsigned int)(a2) + (unsigned int)(v_stack_p18) * 1)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(a1))); }
    a4 = (unsigned int)((a4) - 1);
    result = 0;
    goto loc_004B90CB;
loc_004B93A1:
    if (a2 == v_stack_m58) goto loc_004B93E7;
    if (a2 != v_stack_m58) goto loc_004B93BB;
    goto loc_004B93C2;
loc_004B93BB:
    v_rbx = (unsigned int)((63) - (0));
loc_004B93C2:
    a2 = (a2) + (8);
    a3 = ~(*(unsigned __int64 *)(a2));
    goto loc_004B9253;
loc_004B93D1:
    v_rbx = (unsigned int)(-(v_rbx));
loc_004B93D3:
    a2 = (a2) - (v_r14);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) << (6));
    v_rbx = (unsigned int)((v_rbx) + (a2));
loc_004B93E1:
    if (((unsigned int)(v_rbx)) <= ((unsigned int)(v_rbp))) goto loc_004B9360;
loc_004B93E7:
    v_rbx = (unsigned int)((v_rbx) | (0xFFFFFFFFULL));
    goto loc_004B9369;
loc_004B93EF:
    if (a3 != -1) goto loc_004B9406;
    a2 = (a2) + (8);
    if (a2 > (v_r14 + result * 8)) goto loc_004B93E7;
    a3 = ~(*(unsigned __int64 *)(a2));
    goto loc_004B93EF;
loc_004B9406:
    a2 = (a2) - (v_r14);
    a3 = ~(a3);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) << (6));
    a2 = (unsigned int)((a2) + (0));
    goto loc_004B93E1;
loc_004B941F:
    v_rbx = (unsigned int)(((unsigned int)(a2)) - ((unsigned int)(v_r15)));
loc_004B9422:
    if (((unsigned int)(v_rbx)) != -1) {
        a3 = (unsigned int)((unsigned int)(a2));
        a2 = (unsigned int)(v_rbx);
        a1 = a1;
        result = RtlClearBits(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t RtlFindSetBitsAndClear(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (56);
    v_stack_m58 = *(uint64_t *)(arg1 + 0x8);
    local_rbx = (uint32_t)((local_rbx) & (Arg3));
    if (Arg2 != 0) goto loc_004B90AF;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFF8ULL));
    goto loc_004B9422;
loc_004B90AF:
    Arg1 = (uint32_t)((*(uint64_t *)(arg1 + 0x8)) & (4));
    v_stack_p20 = Arg1;
    result = -((uint32_t)((uint32_t)(Arg1)));
    local_r15 = (uint32_t)((local_r15) & (32));
loc_004B90CB:
    v_stack_p10 = (uint32_t)((uint32_t)((uint32_t)(local_rbx)));
    result = -(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15 + (uint32_t)(*(uint32_t *)(arg1)) - 1 * 1))) - ((uint32_t)(local_r15 + (uint32_t)((uint32_t)(local_rbx)) * 1)));
    Arg1 = (uint32_t)((Arg1) & (4));
    result = (uint32_t)((result) + 1);
    local_r14 = (*(uint64_t *)(arg1 + 0x8)) - (Arg1);
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_004B910D;
    local_rbx = (uint32_t)((64) | (0xFFFFFFFFULL));
    goto loc_004B9371;
loc_004B910D:
    Arg1 = (uint8_t)(((uint32_t)((uint32_t)(local_r15 + (uint32_t)((uint32_t)(local_rbx)) * 1))) & (63));
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(local_r15 + (uint32_t)(*(uint32_t *)(arg1)) - 1 * 1))) - ((uint32_t)((uint32_t)(Arg2))));
    local_rbp = (uint32_t)((local_rbp) + 1);
    result = ((uint32_t)((uint32_t)(local_rbp))) >> (6);
    Arg3 = (63 - 62) << ((uint8_t)(Arg1));
    Arg3 = (Arg3) - 1;
    result = ((uint32_t)((uint32_t)(local_r15 + (uint32_t)((uint32_t)(local_rbx)) * 1))) >> (6);
    result = ~(*(uint64_t *)(local_r14 + result * 8));
    Arg3 = (Arg3) | (result);
    if (((uint32_t)((uint32_t)(Arg2))) <= 127) goto loc_004B9233;
    a4 = local_r14 + result * 8 + 8;
    if (((63) & ((uint8_t)(local_rbp))) == 0) { a4 = local_r14 + result * 8; }
    if (Arg3 != 0) goto loc_004B9164;
    Arg1 = 0;
    goto loc_004B91C3;
loc_004B9164:
    Arg2 = (local_r14 + result * 8) + (8);
    result = ~(*(uint64_t *)(Arg2));
    if (result != 0) goto loc_004B918F;
    if (result != 0) goto loc_004B9184;
loc_004B9180:
    goto loc_004B91C3;
loc_004B9184:
    Arg1 = (uint32_t)((63) - ((uint32_t)(result)));
    goto loc_004B91C3;
loc_004B918A:
loc_004B918F:
    if (Arg2 > a4) goto loc_004B93E7;
    Arg2 = (Arg2) + (8);
    result = ~(*(uint64_t *)(Arg2));
    if (result != 0) goto loc_004B918F;
    result = ~(*(uint64_t *)(Arg2));
    if (result == 0) goto loc_004B9180;
    Arg1 = (uint32_t)((63) - (Arg3));
loc_004B91C3:
    local_rbx = (Arg2) - (local_r14);
    local_rbx = (local_rbx) >> (3);
    local_rbx = (uint32_t)((local_rbx) << (6));
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_rbx)) > ((uint32_t)(local_rbp))) goto loc_004B93E7;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)(Arg1)));
    result = (result) >> (6);
loc_004B91EA:
    Arg2 = (Arg2) + (8);
    if (Arg2 == (Arg2 + result * 8)) goto loc_004B9200;
    result = ~(*(uint64_t *)(Arg2));
    if (result != 0) goto loc_004B918A;
    goto loc_004B91EA;
loc_004B9200:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (63));
    if (condition_is_equal) goto loc_004B9360;
    result = ~(*(uint64_t *)(Arg2));
    Arg1 = Arg2 + result * 8;
    if (condition_is_equal) { Arg1 = 64; }
    if (((uint32_t)(Arg1)) >= Arg3) goto loc_004B9360;
    goto loc_004B918F;
loc_004B9233:
    if (((uint32_t)((uint32_t)(Arg2))) >= 64) goto loc_004B92C5;
    if (((uint32_t)((uint32_t)(Arg2))) <= 1) goto loc_004B93EF;
    local_rbx = 0;
    result = ((uint32_t)((uint32_t)(local_r15 + (uint32_t)(*(uint32_t *)(arg1)) - 1 * 1))) >> (6);
loc_004B9253:
    if (Arg3 != -1) goto loc_004B9274;
loc_004B9259:
    Arg2 = (Arg2) + (8);
    if (Arg2 > (local_r14 + result * 8)) goto loc_004B93E7;
    Arg3 = ~(*(uint64_t *)(Arg2));
    if (Arg3 == -1) goto loc_004B9259;
    local_rbx = 0;
loc_004B9274:
    if (condition_is_equal) { result = 64; }
    result = (uint32_t)((result) + (0));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_004B93D1;
    a4 = ~(Arg3);
loc_004B929C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2)))))) >> (1));
    result = (a4) >> ((uint8_t)(Arg1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_004B93A1;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_r10)) > 1) goto loc_004B929C;
    goto loc_004B93D3;
loc_004B92C2:
loc_004B92C5:
    if (!sign_flag) goto loc_004B92DF;
    Arg2 = (Arg2) + (8);
    if (Arg2 > (local_r14 + result * 8)) goto loc_004B93E7;
    Arg3 = ~(*(uint64_t *)(Arg2));
    goto loc_004B92C5;
loc_004B92DF:
    if (Arg2 != (local_r14 + result * 8)) goto loc_004B92F2;
    goto loc_004B92F8;
loc_004B92F2:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r14 + result * 8))) - ((uint32_t)(result)));
loc_004B92F8:
    result = (Arg2) - (local_r14);
    result = (result) >> (3);
    result = (uint32_t)((result) + 1);
    result = (uint32_t)((result) << (6));
    result = (uint32_t)((result) - (Arg3));
    if (((uint32_t)(result)) > ((uint32_t)(local_rbp))) goto loc_004B93E7;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - (Arg3));
    if (condition_is_equal) goto loc_004B9360;
    Arg2 = (Arg2) + (8);
    result = ~(*(uint64_t *)(Arg2));
    if (((uint32_t)(Arg1)) < 64) goto loc_004B9348;
    if (result != 0) goto loc_004B92C2;
    Arg1 = (uint32_t)((Arg1) + (-64));
    if (condition_is_equal) goto loc_004B9360;
    Arg2 = (Arg2) + (8);
    Arg3 = ~(*(uint64_t *)(Arg2));
loc_004B9348:
    if (condition_is_equal) { result = 64; }
    if (((uint32_t)(result)) < ((uint32_t)(Arg1))) goto loc_004B92C2;
loc_004B9360:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != -1) goto loc_004B941F;
loc_004B9369:
loc_004B9371:
    if (v_stack_p10 == 0) goto loc_004B9422;
    a4 = (uint32_t)(Arg2) + (uint32_t)(v_stack_p18) * 1;
    if (((uint32_t)((uint32_t)(Arg2) + (uint32_t)(v_stack_p18) * 1)) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) { a4 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1))); }
    a4 = (uint32_t)((a4) - 1);
    result = 0;
    goto loc_004B90CB;
loc_004B93A1:
    if (Arg2 == v_stack_m58) goto loc_004B93E7;
    if (Arg2 != v_stack_m58) goto loc_004B93BB;
    goto loc_004B93C2;
loc_004B93BB:
    local_rbx = (uint32_t)((63) - (0));
loc_004B93C2:
    Arg2 = (Arg2) + (8);
    Arg3 = ~(*(uint64_t *)(Arg2));
    goto loc_004B9253;
loc_004B93D1:
    local_rbx = (uint32_t)(-(local_rbx));
loc_004B93D3:
    Arg2 = (Arg2) - (local_r14);
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) << (6));
    local_rbx = (uint32_t)((local_rbx) + (Arg2));
loc_004B93E1:
    if (((uint32_t)(local_rbx)) <= ((uint32_t)(local_rbp))) goto loc_004B9360;
loc_004B93E7:
    local_rbx = (uint32_t)((local_rbx) | (0xFFFFFFFFULL));
    goto loc_004B9369;
loc_004B93EF:
    if (Arg3 != -1) goto loc_004B9406;
    Arg2 = (Arg2) + (8);
    if (Arg2 > (local_r14 + result * 8)) goto loc_004B93E7;
    Arg3 = ~(*(uint64_t *)(Arg2));
    goto loc_004B93EF;
loc_004B9406:
    Arg2 = (Arg2) - (local_r14);
    Arg3 = ~(Arg3);
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) << (6));
    Arg2 = (uint32_t)((Arg2) + (0));
    goto loc_004B93E1;
loc_004B941F:
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) - ((uint32_t)(local_r15)));
loc_004B9422:
    if (((uint32_t)(local_rbx)) != -1) {
        Arg3 = (uint32_t)((uint32_t)(Arg2));
        Arg2 = (uint32_t)(local_rbx);
        Arg1 = Arg1;
        result = RtlClearBits(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (56);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B9070&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
