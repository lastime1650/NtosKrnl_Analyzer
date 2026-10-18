# PfPrefetchRequestPrepareForVerify

- RVA: `0x00938C20`–`0x00938F6B` (길이 `843` bytes)
- VA: `0x0000000140938C20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008FBF4`
- 디코드: `210`개 명령, `843/843` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PfPrefetchRequestVerify](PfPrefetchRequestVerify_function_009387EC.md) at `0x0093888B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00938C20  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00938C25  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00938C2A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00938C2F  0F 57 C0                        xorps xmm0, xmm0
00938C32  44 8B D2                        mov r10d, edx
00938C35  41 0F 11 00                     movups xmmword ptr [r8], xmm0
00938C39  33 C0                           xor eax, eax
00938C3B  4C 8B D9                        mov r11, rcx
00938C3E  41 0F 11 40 10                  movups xmmword ptr [r8 + 0x10], xmm0
00938C43  41 B9 80 00 00 00               mov r9d, 0x80
00938C49  48 BE CD CC CC CC CC CC CC CC   movabs rsi, 0xcccccccccccccccd
00938C53  41 0F 11 40 20                  movups xmmword ptr [r8 + 0x20], xmm0
00938C58  49 89 40 30                     mov qword ptr [r8 + 0x30], rax
00938C5C  41 89 40 38                     mov dword ptr [r8 + 0x38], eax
00938C60  8B 79 08                        mov edi, dword ptr [rcx + 8]
00938C63  8B 59 20                        mov ebx, dword ptr [rcx + 0x20]
00938C66  85 FF                           test edi, edi
00938C68  0F 84 28 02 00 00               je 0x140938e96
00938C6E  85 DB                           test ebx, ebx
00938C70  0F 84 04 02 00 00               je 0x140938e7a
00938C76  41 3B D9                        cmp ebx, r9d
00938C79  0F 82 02 02 00 00               jb 0x140938e81
00938C7F  48 8B C6                        mov rax, rsi
00938C82  49 F7 E2                        mul r10
00938C85  48 C1 EA 05                     shr rdx, 5
00938C89  48 3B FA                        cmp rdi, rdx
00938C8C  0F 87 F6 01 00 00               ja 0x140938e88
00938C92  8D 0C BF                        lea ecx, [rdi + rdi*4]
00938C95  C1 E1 03                        shl ecx, 3
00938C98  41 3B DA                        cmp ebx, r10d
00938C9B  0F 83 EE 01 00 00               jae 0x140938e8f
00938CA1  41 3B CA                        cmp ecx, r10d
00938CA4  0F 83 E5 01 00 00               jae 0x140938e8f
00938CAA  41 8B C2                        mov eax, r10d
00938CAD  2B C1                           sub eax, ecx
00938CAF  3B D8                           cmp ebx, eax
00938CB1  0F 87 D8 01 00 00               ja 0x140938e8f
00938CB7  44 8D 0C 0B                     lea r9d, [rbx + rcx]
00938CBB  41 89 18                        mov dword ptr [r8], ebx
00938CBE  45 89 48 04                     mov dword ptr [r8 + 4], r9d
00938CC2  41 8B 43 08                     mov eax, dword ptr [r11 + 8]
00938CC6  41 89 40 08                     mov dword ptr [r8 + 8], eax
00938CCA  41 8B 7B 0C                     mov edi, dword ptr [r11 + 0xc]
00938CCE  41 8B 5B 28                     mov ebx, dword ptr [r11 + 0x28]
00938CD2  85 FF                           test edi, edi
00938CD4  0F 84 E7 01 00 00               je 0x140938ec1
00938CDA  85 DB                           test ebx, ebx
00938CDC  0F 84 C3 01 00 00               je 0x140938ea5
00938CE2  41 3B D9                        cmp ebx, r9d
00938CE5  0F 82 C1 01 00 00               jb 0x140938eac
00938CEB  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00938CF5  49 F7 E2                        mul r10
00938CF8  48 C1 EA 05                     shr rdx, 5
00938CFC  48 3B FA                        cmp rdi, rdx
00938CFF  0F 87 AE 01 00 00               ja 0x140938eb3
00938D05  8D 0C 7F                        lea ecx, [rdi + rdi*2]
00938D08  C1 E1 04                        shl ecx, 4
00938D0B  41 3B DA                        cmp ebx, r10d
00938D0E  0F 83 A6 01 00 00               jae 0x140938eba
00938D14  41 3B CA                        cmp ecx, r10d
00938D17  0F 83 9D 01 00 00               jae 0x140938eba
00938D1D  41 8B C2                        mov eax, r10d
00938D20  2B C1                           sub eax, ecx
00938D22  3B D8                           cmp ebx, eax
00938D24  0F 87 90 01 00 00               ja 0x140938eba
00938D2A  44 8D 0C 0B                     lea r9d, [rbx + rcx]
00938D2E  41 89 58 0C                     mov dword ptr [r8 + 0xc], ebx
00938D32  45 89 48 10                     mov dword ptr [r8 + 0x10], r9d
00938D36  41 8B 43 0C                     mov eax, dword ptr [r11 + 0xc]
00938D3A  41 89 40 14                     mov dword ptr [r8 + 0x14], eax
00938D3E  41 8B 4B 10                     mov ecx, dword ptr [r11 + 0x10]
00938D42  41 8B 53 30                     mov edx, dword ptr [r11 + 0x30]
00938D46  85 C9                           test ecx, ecx
00938D48  0F 84 A1 01 00 00               je 0x140938eef
00938D4E  85 D2                           test edx, edx
00938D50  0F 84 7A 01 00 00               je 0x140938ed0
00938D56  41 3B D1                        cmp edx, r9d
00938D59  0F 82 78 01 00 00               jb 0x140938ed7
00938D5F  41 8B C2                        mov eax, r10d
00938D62  C1 E8 04                        shr eax, 4
00938D65  3B C8                           cmp ecx, eax
00938D67  0F 87 71 01 00 00               ja 0x140938ede
00938D6D  C1 E1 04                        shl ecx, 4
00938D70  41 3B D2                        cmp edx, r10d
00938D73  0F 83 6C 01 00 00               jae 0x140938ee5
00938D79  41 3B CA                        cmp ecx, r10d
00938D7C  0F 83 63 01 00 00               jae 0x140938ee5
00938D82  41 8B C2                        mov eax, r10d
00938D85  2B C1                           sub eax, ecx
00938D87  3B D0                           cmp edx, eax
00938D89  0F 87 56 01 00 00               ja 0x140938ee5
00938D8F  44 8D 0C 0A                     lea r9d, [rdx + rcx]
00938D93  41 89 50 18                     mov dword ptr [r8 + 0x18], edx
00938D97  45 89 48 1C                     mov dword ptr [r8 + 0x1c], r9d
00938D9B  41 8B 43 10                     mov eax, dword ptr [r11 + 0x10]
00938D9F  41 89 40 20                     mov dword ptr [r8 + 0x20], eax
00938DA3  41 8B 7B 14                     mov edi, dword ptr [r11 + 0x14]
00938DA7  41 8B 5B 38                     mov ebx, dword ptr [r11 + 0x38]
00938DAB  85 FF                           test edi, edi
00938DAD  0F 84 76 01 00 00               je 0x140938f29
00938DB3  85 DB                           test ebx, ebx
00938DB5  0F 84 46 01 00 00               je 0x140938f01
00938DBB  41 3B D9                        cmp ebx, r9d
00938DBE  0F 82 47 01 00 00               jb 0x140938f0b
00938DC4  48 8B C6                        mov rax, rsi
00938DC7  49 F7 E2                        mul r10
00938DCA  48 C1 EA 05                     shr rdx, 5
00938DCE  48 3B FA                        cmp rdi, rdx
00938DD1  0F 87 3E 01 00 00               ja 0x140938f15
00938DD7  8D 0C BF                        lea ecx, [rdi + rdi*4]
00938DDA  C1 E1 03                        shl ecx, 3
00938DDD  41 3B DA                        cmp ebx, r10d
00938DE0  0F 83 39 01 00 00               jae 0x140938f1f
00938DE6  41 3B CA                        cmp ecx, r10d
00938DE9  0F 83 30 01 00 00               jae 0x140938f1f
00938DEF  41 8B C2                        mov eax, r10d
00938DF2  2B C1                           sub eax, ecx
00938DF4  3B D8                           cmp ebx, eax
00938DF6  0F 87 23 01 00 00               ja 0x140938f1f
00938DFC  44 8D 0C 0B                     lea r9d, [rbx + rcx]
00938E00  41 89 58 24                     mov dword ptr [r8 + 0x24], ebx
00938E04  45 89 48 28                     mov dword ptr [r8 + 0x28], r9d
00938E08  41 8B 43 14                     mov eax, dword ptr [r11 + 0x14]
00938E0C  41 89 40 2C                     mov dword ptr [r8 + 0x2c], eax
00938E10  41 8B 53 18                     mov edx, dword ptr [r11 + 0x18]
00938E14  41 8B 4B 40                     mov ecx, dword ptr [r11 + 0x40]
00938E18  85 D2                           test edx, edx
00938E1A  0F 84 39 01 00 00               je 0x140938f59
00938E20  85 C9                           test ecx, ecx
00938E22  0F 84 13 01 00 00               je 0x140938f3b
00938E28  41 3B C9                        cmp ecx, r9d
00938E2B  0F 82 14 01 00 00               jb 0x140938f45
00938E31  41 3B CA                        cmp ecx, r10d
00938E34  0F 83 15 01 00 00               jae 0x140938f4f
00938E3A  41 3B D2                        cmp edx, r10d
00938E3D  0F 83 0C 01 00 00               jae 0x140938f4f
00938E43  41 8B C2                        mov eax, r10d
00938E46  2B C2                           sub eax, edx
00938E48  3B C8                           cmp ecx, eax
00938E4A  0F 87 FF 00 00 00               ja 0x140938f4f
00938E50  44 8D 0C 11                     lea r9d, [rcx + rdx]
00938E54  41 89 48 30                     mov dword ptr [r8 + 0x30], ecx
00938E58  45 89 48 34                     mov dword ptr [r8 + 0x34], r9d
00938E5C  45 2B CA                        sub r9d, r10d
00938E5F  41 F7 D9                        neg r9d
00938E62  1B C0                           sbb eax, eax
00938E64  25 28 23 00 00                  and eax, 0x2328
00938E69  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
00938E6E  48 8B 74 24 10                  mov rsi, qword ptr [rsp + 0x10]
00938E73  48 8B 7C 24 18                  mov rdi, qword ptr [rsp + 0x18]
00938E78  C3                              ret
00938E79  CC                              int3
00938E7A  B8 A0 0F 00 00                  mov eax, 0xfa0
00938E7F  EB E8                           jmp 0x140938e69
00938E81  B8 68 10 00 00                  mov eax, 0x1068
00938E86  EB E1                           jmp 0x140938e69
00938E88  B8 CC 10 00 00                  mov eax, 0x10cc
00938E8D  EB DA                           jmp 0x140938e69
00938E8F  B8 30 11 00 00                  mov eax, 0x1130
00938E94  EB D3                           jmp 0x140938e69
00938E96  85 DB                           test ebx, ebx
00938E98  0F 84 2C FE FF FF               je 0x140938cca
00938E9E  B8 04 10 00 00                  mov eax, 0x1004
00938EA3  EB C4                           jmp 0x140938e69
00938EA5  B8 88 13 00 00                  mov eax, 0x1388
00938EAA  EB BD                           jmp 0x140938e69
00938EAC  B8 50 14 00 00                  mov eax, 0x1450
00938EB1  EB B6                           jmp 0x140938e69
00938EB3  B8 B4 14 00 00                  mov eax, 0x14b4
00938EB8  EB AF                           jmp 0x140938e69
00938EBA  B8 18 15 00 00                  mov eax, 0x1518
00938EBF  EB A8                           jmp 0x140938e69
00938EC1  85 DB                           test ebx, ebx
00938EC3  0F 84 75 FE FF FF               je 0x140938d3e
00938EC9  B8 EC 13 00 00                  mov eax, 0x13ec
00938ECE  EB 99                           jmp 0x140938e69
00938ED0  B8 70 17 00 00                  mov eax, 0x1770
00938ED5  EB 92                           jmp 0x140938e69
00938ED7  B8 38 18 00 00                  mov eax, 0x1838
00938EDC  EB 8B                           jmp 0x140938e69
00938EDE  B8 9C 18 00 00                  mov eax, 0x189c
00938EE3  EB 84                           jmp 0x140938e69
00938EE5  B8 00 19 00 00                  mov eax, 0x1900
00938EEA  E9 7A FF FF FF                  jmp 0x140938e69
00938EEF  85 D2                           test edx, edx
00938EF1  0F 84 AC FE FF FF               je 0x140938da3
00938EF7  B8 D4 17 00 00                  mov eax, 0x17d4
00938EFC  E9 68 FF FF FF                  jmp 0x140938e69
00938F01  B8 58 1B 00 00                  mov eax, 0x1b58
00938F06  E9 5E FF FF FF                  jmp 0x140938e69
00938F0B  B8 20 1C 00 00                  mov eax, 0x1c20
00938F10  E9 54 FF FF FF                  jmp 0x140938e69
00938F15  B8 84 1C 00 00                  mov eax, 0x1c84
00938F1A  E9 4A FF FF FF                  jmp 0x140938e69
00938F1F  B8 E8 1C 00 00                  mov eax, 0x1ce8
00938F24  E9 40 FF FF FF                  jmp 0x140938e69
00938F29  85 DB                           test ebx, ebx
00938F2B  0F 84 DF FE FF FF               je 0x140938e10
00938F31  B8 BC 1B 00 00                  mov eax, 0x1bbc
00938F36  E9 2E FF FF FF                  jmp 0x140938e69
00938F3B  B8 40 1F 00 00                  mov eax, 0x1f40
00938F40  E9 24 FF FF FF                  jmp 0x140938e69
00938F45  B8 08 20 00 00                  mov eax, 0x2008
00938F4A  E9 1A FF FF FF                  jmp 0x140938e69
00938F4F  B8 6C 20 00 00                  mov eax, 0x206c
00938F54  E9 10 FF FF FF                  jmp 0x140938e69
00938F59  85 C9                           test ecx, ecx
00938F5B  0F 84 FB FE FF FF               je 0x140938e5c
00938F61  B8 A4 1F 00 00                  mov eax, 0x1fa4
00938F66  E9 FE FE FF FF                  jmp 0x140938e69
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfPrefetchRequestPrepareForVerify(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    *(unsigned __int64 *)(a3) = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(a3 + 16) = v_xmm0;
    *(unsigned __int64 *)(a3 + 32) = v_xmm0;
    *(unsigned __int64 *)(a3 + 48) = 0;
    *(unsigned int *)(a3 + 56) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))) == 0) goto loc_00938E96;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))) == 0) goto loc_00938E7A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) < 128) goto loc_00938E81;
    a2 = (a2) >> (5);
    if (((unsigned int)(*(unsigned int *)(a1 + 8))) > a2) goto loc_00938E88;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8)) + (unsigned int)(*(unsigned int *)(a1 + 8)) * 4) << (3));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938E8F;
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938E8F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) - ((unsigned int)(a1)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) > ((unsigned int)(result))) goto loc_00938E8F;
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)) + a1 * 1);
    *(unsigned int *)(a3 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
loc_00938CCA:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))) == 0) goto loc_00938EC1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))) == 0) goto loc_00938EA5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)) + a1 * 1))) goto loc_00938EAC;
    a2 = (a2) >> (5);
    if (((unsigned int)(*(unsigned int *)(a1 + 12))) > a2) goto loc_00938EB3;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 12)) + (unsigned int)(*(unsigned int *)(a1 + 12)) * 2) << (4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938EBA;
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938EBA;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) - ((unsigned int)(a1)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) > ((unsigned int)(result))) goto loc_00938EBA;
    *(unsigned int *)(a3 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    *(unsigned int *)(a3 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)) + a1 * 1);
    *(unsigned int *)(a3 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)));
loc_00938D3E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))) == 0) goto loc_00938EEF;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))) == 0) goto loc_00938ED0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)) + a1 * 1))) goto loc_00938ED7;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) >> (4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) > ((unsigned int)(result))) goto loc_00938EDE;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) << (4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938EE5;
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938EE5;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) - ((unsigned int)(a1)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) > ((unsigned int)(result))) goto loc_00938EE5;
    *(unsigned int *)(a3 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    *(unsigned int *)(a3 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)) + a1 * 1);
    *(unsigned int *)(a3 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
loc_00938DA3:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20))) == 0) goto loc_00938F29;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56))) == 0) goto loc_00938F01;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)) + a1 * 1))) goto loc_00938F0B;
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 48))) >> (5);
    if (((unsigned int)(*(unsigned int *)(a1 + 20))) > a2) goto loc_00938F15;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 20)) + (unsigned int)(*(unsigned int *)(a1 + 20)) * 4) << (3));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)))) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938F1F;
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938F1F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) - ((unsigned int)(a1)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)))) > ((unsigned int)(result))) goto loc_00938F1F;
    *(unsigned int *)(a3 + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)));
    *(unsigned int *)(a3 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)) + a1 * 1);
    *(unsigned int *)(a3 + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)));
loc_00938E10:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))) == 0) goto loc_00938F59;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64))) == 0) goto loc_00938F3B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)) + a1 * 1))) goto loc_00938F45;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938F4F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_00938F4F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))) > ((unsigned int)(result))) goto loc_00938F4F;
    *(unsigned int *)(a3 + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)));
    *(unsigned int *)(a3 + 52) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)) + (unsigned int)(*(unsigned int *)(a1 + 24)) * 1);
loc_00938E5C:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 64)) + (unsigned int)(*(unsigned int *)(a1 + 24)) * 1) - ((unsigned int)((unsigned int)((unsigned int)(a2)))));
    a4 = (unsigned int)(-(a4));
    result = (unsigned int)((result) & (0x2328ULL));
loc_00938E69:
    return result;
loc_00938E7A:
    goto loc_00938E69;
loc_00938E81:
    goto loc_00938E69;
loc_00938E88:
    goto loc_00938E69;
loc_00938E8F:
    goto loc_00938E69;
loc_00938E96:
    if ((unsigned int)(v_stack_p8) == 0) goto loc_00938CCA;
    goto loc_00938E69;
loc_00938EA5:
    goto loc_00938E69;
loc_00938EAC:
    goto loc_00938E69;
loc_00938EB3:
    goto loc_00938E69;
loc_00938EBA:
    goto loc_00938E69;
loc_00938EC1:
    if ((unsigned int)(v_stack_p8) == 0) goto loc_00938D3E;
    goto loc_00938E69;
loc_00938ED0:
    goto loc_00938E69;
loc_00938ED7:
    goto loc_00938E69;
loc_00938EDE:
    goto loc_00938E69;
loc_00938EE5:
    goto loc_00938E69;
loc_00938EEF:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))) == 0) goto loc_00938DA3;
    goto loc_00938E69;
loc_00938F01:
    goto loc_00938E69;
loc_00938F0B:
    goto loc_00938E69;
loc_00938F15:
    goto loc_00938E69;
loc_00938F1F:
    goto loc_00938E69;
loc_00938F29:
    if ((unsigned int)(v_stack_p8) == 0) goto loc_00938E10;
    goto loc_00938E69;
loc_00938F3B:
    goto loc_00938E69;
loc_00938F45:
    goto loc_00938E69;
loc_00938F4F:
    goto loc_00938E69;
loc_00938F59:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64))) == 0) goto loc_00938E5C;
    goto loc_00938E69;
}
```

## 5. (Beta) C Style

```c
int64_t PfPrefetchRequestPrepareForVerify(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    *(uint64_t *)(arg3) = v_xmm0;
    result = 0;
    *(uint64_t *)(arg3 + 0x10) = v_xmm0;
    *(uint64_t *)(arg3 + 0x20) = v_xmm0;
    *(uint64_t *)(arg3 + 0x30) = 0;
    *(uint32_t *)(arg3 + 0x38) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))) == 0) goto loc_00938E96;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))) == 0) goto loc_00938E7A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) < 128) goto loc_00938E81;
    Arg2 = (Arg2) >> (5);
    if (((uint32_t)(*(uint32_t *)(arg1 + 0x8))) > Arg2) goto loc_00938E88;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8)) + (uint32_t)(*(uint32_t *)(arg1 + 0x8)) * 4) << (3));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938E8F;
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938E8F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) - ((uint32_t)(Arg1)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) > ((uint32_t)(result))) goto loc_00938E8F;
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    *(uint32_t *)(arg3 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)) + Arg1 * 1);
    *(uint32_t *)(arg3 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
loc_00938CCA:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC))) == 0) goto loc_00938EC1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))) == 0) goto loc_00938EA5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)) + Arg1 * 1))) goto loc_00938EAC;
    Arg2 = (Arg2) >> (5);
    if (((uint32_t)(*(uint32_t *)(arg1 + 0xC))) > Arg2) goto loc_00938EB3;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC)) + (uint32_t)(*(uint32_t *)(arg1 + 0xC)) * 2) << (4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938EBA;
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938EBA;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) - ((uint32_t)(Arg1)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) > ((uint32_t)(result))) goto loc_00938EBA;
    *(uint32_t *)(arg3 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    *(uint32_t *)(arg3 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)) + Arg1 * 1);
    *(uint32_t *)(arg3 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)));
loc_00938D3E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))) == 0) goto loc_00938EEF;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))) == 0) goto loc_00938ED0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)) + Arg1 * 1))) goto loc_00938ED7;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) >> (4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) > ((uint32_t)(result))) goto loc_00938EDE;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) << (4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938EE5;
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938EE5;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) - ((uint32_t)(Arg1)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) > ((uint32_t)(result))) goto loc_00938EE5;
    *(uint32_t *)(arg3 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    *(uint32_t *)(arg3 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)) + Arg1 * 1);
    *(uint32_t *)(arg3 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
loc_00938DA3:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14))) == 0) goto loc_00938F29;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38))) == 0) goto loc_00938F01;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)) + Arg1 * 1))) goto loc_00938F0B;
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (5);
    if (((uint32_t)(*(uint32_t *)(arg1 + 0x14))) > Arg2) goto loc_00938F15;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x14)) + (uint32_t)(*(uint32_t *)(arg1 + 0x14)) * 4) << (3));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938F1F;
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938F1F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) - ((uint32_t)(Arg1)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) > ((uint32_t)(result))) goto loc_00938F1F;
    *(uint32_t *)(arg3 + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)));
    *(uint32_t *)(arg3 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)) + Arg1 * 1);
    *(uint32_t *)(arg3 + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)));
loc_00938E10:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18))) == 0) goto loc_00938F59;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40))) == 0) goto loc_00938F3B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)) + Arg1 * 1))) goto loc_00938F45;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938F4F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_00938F4F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))) > ((uint32_t)(result))) goto loc_00938F4F;
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)));
    *(uint32_t *)(arg3 + 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)) + (uint32_t)(*(uint32_t *)(arg1 + 0x18)) * 1);
loc_00938E5C:
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x40)) + (uint32_t)(*(uint32_t *)(arg1 + 0x18)) * 1) - ((uint32_t)((uint32_t)((uint32_t)(Arg2)))));
    a4 = (uint32_t)(-(a4));
    result = (uint32_t)((result) & (0x2328ULL));
loc_00938E69:
    return result;
loc_00938E7A:
    goto loc_00938E69;
loc_00938E81:
    goto loc_00938E69;
loc_00938E88:
    goto loc_00938E69;
loc_00938E8F:
    goto loc_00938E69;
loc_00938E96:
    if ((uint32_t)(v_stack_p8) == 0) goto loc_00938CCA;
    goto loc_00938E69;
loc_00938EA5:
    goto loc_00938E69;
loc_00938EAC:
    goto loc_00938E69;
loc_00938EB3:
    goto loc_00938E69;
loc_00938EBA:
    goto loc_00938E69;
loc_00938EC1:
    if ((uint32_t)(v_stack_p8) == 0) goto loc_00938D3E;
    goto loc_00938E69;
loc_00938ED0:
    goto loc_00938E69;
loc_00938ED7:
    goto loc_00938E69;
loc_00938EDE:
    goto loc_00938E69;
loc_00938EE5:
    goto loc_00938E69;
loc_00938EEF:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18))) == 0) goto loc_00938DA3;
    goto loc_00938E69;
loc_00938F01:
    goto loc_00938E69;
loc_00938F0B:
    goto loc_00938E69;
loc_00938F15:
    goto loc_00938E69;
loc_00938F1F:
    goto loc_00938E69;
loc_00938F29:
    if ((uint32_t)(v_stack_p8) == 0) goto loc_00938E10;
    goto loc_00938E69;
loc_00938F3B:
    goto loc_00938E69;
loc_00938F45:
    goto loc_00938E69;
loc_00938F4F:
    goto loc_00938E69;
loc_00938F59:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40))) == 0) goto loc_00938E5C;
    goto loc_00938E69;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x0` | `128` | `R` |
| `Arg3` | `+ 0x4` | `32` | `W` |
| `Arg3` | `+ 0x8` | `32` | `W` |
| `Arg3` | `+ 0xC` | `32` | `W` |
| `Arg3` | `+ 0x10` | `32` | `W` |
| `Arg3` | `+ 0x10` | `128` | `R` |
| `Arg3` | `+ 0x14` | `32` | `W` |
| `Arg3` | `+ 0x18` | `32` | `W` |
| `Arg3` | `+ 0x1C` | `32` | `W` |
| `Arg3` | `+ 0x20` | `32` | `W` |
| `Arg3` | `+ 0x20` | `128` | `R` |
| `Arg3` | `+ 0x24` | `32` | `W` |
| `Arg3` | `+ 0x28` | `32` | `W` |
| `Arg3` | `+ 0x2C` | `32` | `W` |
| `Arg3` | `+ 0x30` | `32` | `W` |
| `Arg3` | `+ 0x30` | `64` | `W` |
| `Arg3` | `+ 0x34` | `32` | `W` |
| `Arg3` | `+ 0x38` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00938C20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
