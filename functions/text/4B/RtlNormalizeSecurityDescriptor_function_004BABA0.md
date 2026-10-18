# RtlNormalizeSecurityDescriptor

- RVA: `0x004BABA0`–`0x004BAE3F` (길이 `671` bytes)
- VA: `0x00000001404BABA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB5F0`
- 디코드: `206`개 명령, `671/671` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BABDA` → [SeValidSecurityDescriptor](../../page/8B/SeValidSecurityDescriptor_function_008BED60.md) (function, `0x008BED60`)
- `0x004BAC0F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004BAC7F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004BACAC` → [RtlpNormalizeAcl](../../page/8B/RtlpNormalizeAcl_function_008BC950.md) (function, `0x008BC950`)
- `0x004BAD24` → [RtlpNormalizeAcl](../../page/8B/RtlpNormalizeAcl_function_008BC950.md) (function, `0x008BC950`)
- `0x004BAD6E` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x004BAD87` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004BADB9` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x004BADD2` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004BAE06` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x004BABDA` → [SeValidSecurityDescriptor](../../page/8B/SeValidSecurityDescriptor_function_008BED60.md) (`.text` → `PAGE`)
  - `0x004BAC0F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004BAC7F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004BACAC` → [RtlpNormalizeAcl](../../page/8B/RtlpNormalizeAcl_function_008BC950.md) (`.text` → `PAGE`)
  - `0x004BAD24` → [RtlpNormalizeAcl](../../page/8B/RtlpNormalizeAcl_function_008BC950.md) (`.text` → `PAGE`)
  - `0x004BAD6E` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`.text` → `PAGE`)
  - `0x004BADB9` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`.text` → `PAGE`)
  - `0x004BAE06` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BABA0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
004BABA5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
004BABAA  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
004BABAF  53                              push rbx
004BABB0  55                              push rbp
004BABB1  56                              push rsi
004BABB2  57                              push rdi
004BABB3  41 54                           push r12
004BABB5  41 55                           push r13
004BABB7  41 56                           push r14
004BABB9  41 57                           push r15
004BABBB  48 83 EC 28                     sub rsp, 0x28
004BABBF  48 8B 29                        mov rbp, qword ptr [rcx]
004BABC2  45 33 ED                        xor r13d, r13d
004BABC5  8B DA                           mov ebx, edx
004BABC7  4D 8B F8                        mov r15, r8
004BABCA  48 8B D5                        mov rdx, rbp
004BABCD  44 88 6C 24 78                  mov byte ptr [rsp + 0x78], r13b
004BABD2  8B CB                           mov ecx, ebx
004BABD4  41 8B FD                        mov edi, r13d
004BABD7  45 8A F5                        mov r14b, r13b
004BABDA  E8 81 41 40 00                  call 0x1408bed60
004BABDF  84 C0                           test al, al
004BABE1  0F 84 44 02 00 00               je 0x1404bae2b
004BABE7  40 8A B4 24 90 00 00 00         mov sil, byte ptr [rsp + 0x90]
004BABEF  40 84 F6                        test sil, sil
004BABF2  75 3E                           jne 0x1404bac32
004BABF4  4D 85 FF                        test r15, r15
004BABF7  74 08                           je 0x1404bac01
004BABF9  49 8B 3F                        mov rdi, qword ptr [r15]
004BABFC  48 85 FF                        test rdi, rdi
004BABFF  75 24                           jne 0x1404bac25
004BAC01  48 8B D3                        mov rdx, rbx
004BAC04  B9 00 01 00 00                  mov ecx, 0x100
004BAC09  41 B8 53 65 53 64               mov r8d, 0x64536553
004BAC0F  E8 DC 74 6C 00                  call 0x140b820f0
004BAC14  48 8B F8                        mov rdi, rax
004BAC17  48 85 C0                        test rax, rax
004BAC1A  0F 84 0B 02 00 00               je 0x1404bae2b
004BAC20  C6 44 24 78 01                  mov byte ptr [rsp + 0x78], 1
004BAC25  0F 10 45 00                     movups xmm0, xmmword ptr [rbp]
004BAC29  0F 11 07                        movups xmmword ptr [rdi], xmm0
004BAC2C  8B 4D 10                        mov ecx, dword ptr [rbp + 0x10]
004BAC2F  89 4F 10                        mov dword ptr [rdi + 0x10], ecx
004BAC32  8B 4D 0C                        mov ecx, dword ptr [rbp + 0xc]
004BAC35  BB 14 00 00 00                  mov ebx, 0x14
004BAC3A  85 C9                           test ecx, ecx
004BAC3C  0F 84 AB 00 00 00               je 0x1404baced
004BAC42  4C 8D 2C 29                     lea r13, [rcx + rbp]
004BAC46  41 0F B7 55 04                  movzx edx, word ptr [r13 + 4]
004BAC4B  0F B7 C2                        movzx eax, dx
004BAC4E  66 F7 D8                        neg ax
004BAC51  45 1B E4                        sbb r12d, r12d
004BAC54  44 23 E3                        and r12d, ebx
004BAC57  44 3B E1                        cmp r12d, ecx
004BAC5A  41 0F 95 C6                     setne r14b
004BAC5E  74 2C                           je 0x1404bac8c
004BAC60  33 C0                           xor eax, eax
004BAC62  40 84 F6                        test sil, sil
004BAC65  74 27                           je 0x1404bac8e
004BAC67  45 33 ED                        xor r13d, r13d
004BAC6A  45 84 F6                        test r14b, r14b
004BAC6D  0F 85 6F 01 00 00               jne 0x1404bade2
004BAC73  44 38 6C 24 78                  cmp byte ptr [rsp + 0x78], r13b
004BAC78  74 0A                           je 0x1404bac84
004BAC7A  33 D2                           xor edx, edx
004BAC7C  48 8B CF                        mov rcx, rdi
004BAC7F  E8 EC 7B 6C 00                  call 0x140b82870
004BAC84  41 8A C6                        mov al, r14b
004BAC87  E9 A1 01 00 00                  jmp 0x1404bae2d
004BAC8C  33 C0                           xor eax, eax
004BAC8E  66 85 D2                        test dx, dx
004BAC91  74 4B                           je 0x1404bacde
004BAC93  40 84 F6                        test sil, sil
004BAC96  74 05                           je 0x1404bac9d
004BAC98  4C 8B F8                        mov r15, rax
004BAC9B  EB 06                           jmp 0x1404baca3
004BAC9D  45 8B FC                        mov r15d, r12d
004BACA0  4C 03 FF                        add r15, rdi
004BACA3  45 33 C0                        xor r8d, r8d
004BACA6  49 8B D5                        mov rdx, r13
004BACA9  49 8B CF                        mov rcx, r15
004BACAC  E8 9F 1C 40 00                  call 0x1408bc950
004BACB1  44 0A F0                        or r14b, al
004BACB4  74 09                           je 0x1404bacbf
004BACB6  40 84 F6                        test sil, sil
004BACB9  0F 85 20 01 00 00               jne 0x1404baddf
004BACBF  40 84 F6                        test sil, sil
004BACC2  74 07                           je 0x1404baccb
004BACC4  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
004BACC9  EB 09                           jmp 0x1404bacd4
004BACCB  44 89 67 0C                     mov dword ptr [rdi + 0xc], r12d
004BACCF  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
004BACD4  0F B7 C0                        movzx eax, ax
004BACD7  03 D8                           add ebx, eax
004BACD9  45 33 ED                        xor r13d, r13d
004BACDC  EB 0F                           jmp 0x1404baced
004BACDE  45 33 ED                        xor r13d, r13d
004BACE1  41 B6 01                        mov r14b, 1
004BACE4  40 84 F6                        test sil, sil
004BACE7  75 8A                           jne 0x1404bac73
004BACE9  44 89 6F 0C                     mov dword ptr [rdi + 0xc], r13d
004BACED  8B 4D 10                        mov ecx, dword ptr [rbp + 0x10]
004BACF0  85 C9                           test ecx, ecx
004BACF2  74 5A                           je 0x1404bad4e
004BACF4  3B D9                           cmp ebx, ecx
004BACF6  0F 95 C0                        setne al
004BACF9  44 0A F0                        or r14b, al
004BACFC  74 09                           je 0x1404bad07
004BACFE  40 84 F6                        test sil, sil
004BAD01  0F 85 6C FF FF FF               jne 0x1404bac73
004BAD07  4C 8D 24 29                     lea r12, [rcx + rbp]
004BAD0B  40 84 F6                        test sil, sil
004BAD0E  74 05                           je 0x1404bad15
004BAD10  4D 8B FD                        mov r15, r13
004BAD13  EB 06                           jmp 0x1404bad1b
004BAD15  44 8B FB                        mov r15d, ebx
004BAD18  4C 03 FF                        add r15, rdi
004BAD1B  45 33 C0                        xor r8d, r8d
004BAD1E  49 8B D4                        mov rdx, r12
004BAD21  49 8B CF                        mov rcx, r15
004BAD24  E8 27 1C 40 00                  call 0x1408bc950
004BAD29  44 0A F0                        or r14b, al
004BAD2C  74 09                           je 0x1404bad37
004BAD2E  40 84 F6                        test sil, sil
004BAD31  0F 85 3C FF FF FF               jne 0x1404bac73
004BAD37  40 84 F6                        test sil, sil
004BAD3A  74 08                           je 0x1404bad44
004BAD3C  41 0F B7 44 24 02               movzx eax, word ptr [r12 + 2]
004BAD42  EB 08                           jmp 0x1404bad4c
004BAD44  89 5F 10                        mov dword ptr [rdi + 0x10], ebx
004BAD47  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
004BAD4C  03 D8                           add ebx, eax
004BAD4E  3B 5D 04                        cmp ebx, dword ptr [rbp + 4]
004BAD51  74 0F                           je 0x1404bad62
004BAD53  41 B6 01                        mov r14b, 1
004BAD56  40 84 F6                        test sil, sil
004BAD59  0F 85 14 FF FF FF               jne 0x1404bac73
004BAD5F  89 5F 04                        mov dword ptr [rdi + 4], ebx
004BAD62  44 8B 7D 04                     mov r15d, dword ptr [rbp + 4]
004BAD66  4C 03 FD                        add r15, rbp
004BAD69  41 0F B6 4F 01                  movzx ecx, byte ptr [r15 + 1]
004BAD6E  E8 5D F7 50 00                  call 0x1409ca4d0
004BAD73  44 8B E0                        mov r12d, eax
004BAD76  40 84 F6                        test sil, sil
004BAD79  75 11                           jne 0x1404bad8c
004BAD7B  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
004BAD7E  45 8B C4                        mov r8d, r12d
004BAD81  48 03 CF                        add rcx, rdi
004BAD84  49 8B D7                        mov rdx, r15
004BAD87  E8 B4 BA 20 00                  call 0x1406c6840
004BAD8C  8B 45 08                        mov eax, dword ptr [rbp + 8]
004BAD8F  41 03 DC                        add ebx, r12d
004BAD92  85 C0                           test eax, eax
004BAD94  0F 84 D0 FE FF FF               je 0x1404bac6a
004BAD9A  3B D8                           cmp ebx, eax
004BAD9C  74 0F                           je 0x1404badad
004BAD9E  41 B6 01                        mov r14b, 1
004BADA1  40 84 F6                        test sil, sil
004BADA4  0F 85 C9 FE FF FF               jne 0x1404bac73
004BADAA  89 5F 08                        mov dword ptr [rdi + 8], ebx
004BADAD  44 8B 7D 08                     mov r15d, dword ptr [rbp + 8]
004BADB1  4C 03 FD                        add r15, rbp
004BADB4  41 0F B6 4F 01                  movzx ecx, byte ptr [r15 + 1]
004BADB9  E8 12 F7 50 00                  call 0x1409ca4d0
004BADBE  44 8B E0                        mov r12d, eax
004BADC1  40 84 F6                        test sil, sil
004BADC4  75 11                           jne 0x1404badd7
004BADC6  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
004BADC9  45 8B C4                        mov r8d, r12d
004BADCC  48 03 CF                        add rcx, rdi
004BADCF  49 8B D7                        mov rdx, r15
004BADD2  E8 69 BA 20 00                  call 0x1406c6840
004BADD7  41 03 DC                        add ebx, r12d
004BADDA  E9 8B FE FF FF                  jmp 0x1404bac6a
004BADDF  45 33 ED                        xor r13d, r13d
004BADE2  40 84 F6                        test sil, sil
004BADE5  0F 85 88 FE FF FF               jne 0x1404bac73
004BADEB  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
004BADF3  48 85 C0                        test rax, rax
004BADF6  74 09                           je 0x1404bae01
004BADF8  44 38 6C 24 78                  cmp byte ptr [rsp + 0x78], r13b
004BADFD  75 11                           jne 0x1404bae10
004BADFF  EB 12                           jmp 0x1404bae13
004BAE01  33 D2                           xor edx, edx
004BAE03  48 8B CD                        mov rcx, rbp
004BAE06  E8 65 7A 6C 00                  call 0x140b82870
004BAE0B  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
004BAE10  48 89 38                        mov qword ptr [rax], rdi
004BAE13  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
004BAE1B  48 85 C0                        test rax, rax
004BAE1E  0F 84 60 FE FF FF               je 0x1404bac84
004BAE24  89 18                           mov dword ptr [rax], ebx
004BAE26  E9 59 FE FF FF                  jmp 0x1404bac84
004BAE2B  32 C0                           xor al, al
004BAE2D  48 83 C4 28                     add rsp, 0x28
004BAE31  41 5F                           pop r15
004BAE33  41 5E                           pop r14
004BAE35  41 5D                           pop r13
004BAE37  41 5C                           pop r12
004BAE39  5F                              pop rdi
004BAE3A  5E                              pop rsi
004BAE3B  5D                              pop rbp
004BAE3C  5B                              pop rbx
004BAE3D  C3                              ret
004BAE3E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlNormalizeSecurityDescriptor(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (40);
    v_r13 = 0;
    v_stack_p10 = 0;
    result = SeValidSecurityDescriptor((unsigned int)((unsigned int)((unsigned int)(a2))), *(unsigned __int64 *)(a1), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004BAE2B;
    if (a5 != 0) goto loc_004BAC32;
    if (a3 == 0) goto loc_004BAC01;
    if (*(unsigned __int64 *)(a3) != 0) goto loc_004BAC25;
loc_004BAC01:
    result = ExAllocatePool2(256, (unsigned int)(a2), (unsigned int)(0x64536553ULL), a4);
    if (result == 0) goto loc_004BAE2B;
    v_stack_p10 = 1;
loc_004BAC25:
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)));
loc_004BAC32:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12))) == 0) goto loc_004BACED;
    result = (unsigned __int16)(-((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12)) + *(unsigned __int64 *)(a1) * 1 + 4))));
    v_r12 = (unsigned int)((v_r12) & (20));
    v_r14 = (((unsigned int)(v_r12)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12))))) ? 1 : 0;
    if (((unsigned int)(v_r12)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 12))))) goto loc_004BAC8C;
    result = 0;
    if (a5 == 0) goto loc_004BAC8E;
    v_r13 = 0;
loc_004BAC6A:
    if ((unsigned __int8)(v_r14) != 0) goto loc_004BADE2;
loc_004BAC73:
    if (v_stack_p10 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x64536553ULL), a4);
    }
    goto loc_004BAE2D;
loc_004BAC8C:
    result = 0;
loc_004BAC8E:
    if (0 == 0) goto loc_004BACDE;
    if (a5 == 0) goto loc_004BAC9D;
    goto loc_004BACA3;
loc_004BAC9D:
    v_r15 = ((unsigned int)((unsigned int)(v_r12))) + (0);
loc_004BACA3:
    a3 = 0;
    result = RtlpNormalizeAcl(v_r15, 0, a3, a4);
    v_r14 = (unsigned __int8)((v_r14) | ((unsigned __int8)(result)));
    if (condition_is_equal) goto loc_004BACBF;
    if (a5 != 0) goto loc_004BADDF;
loc_004BACBF:
    if (a5 == 0) goto loc_004BACCB;
    goto loc_004BACD4;
loc_004BACCB:
    *(unsigned int *)(result + 12) = (unsigned int)(v_r12);
loc_004BACD4:
    v_rbx = (unsigned int)((20) + ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_r15 + 2)))));
    v_r13 = 0;
    goto loc_004BACED;
loc_004BACDE:
    v_r13 = 0;
    if (a5 != 0) goto loc_004BAC73;
    *(unsigned int *)(result + 12) = 0;
loc_004BACED:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16))) == 0) goto loc_004BAD4E;
    result = (((unsigned int)(v_rbx)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16))))) ? 1 : 0;
    v_r14 = (unsigned __int8)((1) | ((unsigned __int8)(result)));
    if (condition_is_equal) goto loc_004BAD07;
    if (a5 != 0) goto loc_004BAC73;
loc_004BAD07:
    if (a5 == 0) goto loc_004BAD15;
    goto loc_004BAD1B;
loc_004BAD15:
    v_r15 = ((unsigned int)((unsigned int)(v_rbx))) + (result);
loc_004BAD1B:
    a3 = 0;
    result = RtlpNormalizeAcl(v_r15, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + *(unsigned __int64 *)(a1) * 1, a3, a4);
    v_r14 = (unsigned __int8)((v_r14) | ((unsigned __int8)(result)));
    if (condition_is_equal) goto loc_004BAD37;
    if (a5 != 0) goto loc_004BAC73;
loc_004BAD37:
    if (a5 == 0) goto loc_004BAD44;
    goto loc_004BAD4C;
loc_004BAD44:
    *(unsigned int *)(result + 16) = (unsigned int)(v_rbx);
loc_004BAD4C:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(*(unsigned __int16 *)(v_r15 + 2))));
loc_004BAD4E:
    if (((unsigned int)(v_rbx)) == (*(unsigned int *)(*(unsigned __int64 *)(a1) + 4))) goto loc_004BAD62;
    if (a5 != 0) goto loc_004BAC73;
    *(unsigned int *)(result + 4) = (unsigned int)(v_rbx);
loc_004BAD62:
    v_r15 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 4))) + (*(unsigned __int64 *)(a1));
    result = RtlLengthRequiredSid(*(unsigned __int8 *)(v_r15 + 1), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 16)) + *(unsigned __int64 *)(a1) * 1, a3, a4);
    if (a5 == 0) {
        a1 = *(unsigned int *)(result + 4);
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = (a1) + (result);
        a2 = v_r15;
        result = memcpy(a1, a2, a3, a4);
    }
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8))) == 0) goto loc_004BAC6A;
    if (((unsigned int)(v_rbx)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8))))) goto loc_004BADAD;
    if (a5 != 0) goto loc_004BAC73;
    *(unsigned int *)(result + 8) = (unsigned int)(v_rbx);
loc_004BADAD:
    v_r15 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8))) + (*(unsigned __int64 *)(a1));
    result = RtlLengthRequiredSid(*(unsigned __int8 *)(v_r15 + 1), a2, a3, a4);
    if (a5 == 0) {
        a1 = *(unsigned int *)(result + 8);
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = (a1) + (result);
        a2 = v_r15;
        result = memcpy(a1, a2, a3, a4);
    }
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_004BAC6A;
loc_004BADDF:
    v_r13 = 0;
loc_004BADE2:
    if (a5 != 0) goto loc_004BAC73;
    if (v_stack_p18 == 0) goto loc_004BAE01;
    if (v_stack_p10 != 0) goto loc_004BAE10;
    goto loc_004BAE13;
loc_004BAE01:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1), a2, a3, a4);
loc_004BAE10:
    *(unsigned __int64 *)(v_stack_p8) = result;
loc_004BAE13:
    if (v_stack_p20 == 0) goto loc_004BAC84;
    *(unsigned int *)(v_stack_p20) = (unsigned int)(v_rbx);
    goto loc_004BAC84;
loc_004BAE2B:
    result = 0;
loc_004BAE2D:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlNormalizeSecurityDescriptor(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (40);
    local_r13 = 0;
    v_stack_p10 = 0;
    result = SeValidSecurityDescriptor((uint32_t)((uint32_t)((uint32_t)(Arg2))), *(uint64_t *)(arg1), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004BAE2B;
    if (Arg5 != 0) goto loc_004BAC32;
    if (Arg3 == 0) goto loc_004BAC01;
    if (*(uint64_t *)(Arg3) != 0) goto loc_004BAC25;
loc_004BAC01:
    result = ExAllocatePool2(256, (uint32_t)(Arg2), (uint32_t)(0x64536553ULL), Arg4);
    if (result == 0) goto loc_004BAE2B;
    v_stack_p10 = 1;
loc_004BAC25:
    *(uint64_t *)(result) = v_xmm0;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)));
loc_004BAC32:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC))) == 0) goto loc_004BACED;
    result = (uint16_t)(-((uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC)) + *(uint64_t *)(arg1) * 1 + 0x4))));
    local_r12 = (uint32_t)((local_r12) & (20));
    local_r14 = (((uint32_t)(local_r12)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC))))) ? 1 : 0;
    if (((uint32_t)(local_r12)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0xC))))) goto loc_004BAC8C;
    result = 0;
    if (Arg5 == 0) goto loc_004BAC8E;
    local_r13 = 0;
loc_004BAC6A:
    if ((uint8_t)(local_r14) != 0) goto loc_004BADE2;
loc_004BAC73:
    if (v_stack_p10 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x64536553ULL), Arg4);
    }
    goto loc_004BAE2D;
loc_004BAC8C:
    result = 0;
loc_004BAC8E:
    if (0 == 0) goto loc_004BACDE;
    if (Arg5 == 0) goto loc_004BAC9D;
    goto loc_004BACA3;
loc_004BAC9D:
    local_r15 = ((uint32_t)((uint32_t)(local_r12))) + (0);
loc_004BACA3:
    Arg3 = 0;
    result = RtlpNormalizeAcl(local_r15, 0, Arg3, Arg4);
    local_r14 = (uint8_t)((local_r14) | ((uint8_t)(result)));
    if (condition_is_equal) goto loc_004BACBF;
    if (Arg5 != 0) goto loc_004BADDF;
loc_004BACBF:
    if (Arg5 == 0) goto loc_004BACCB;
    goto loc_004BACD4;
loc_004BACCB:
    *(uint32_t *)(result + 0xC) = (uint32_t)(local_r12);
loc_004BACD4:
    local_rbx = (uint32_t)((20) + ((uint32_t)((uint16_t)(*(uint16_t *)(local_r15 + 0x2)))));
    local_r13 = 0;
    goto loc_004BACED;
loc_004BACDE:
    local_r13 = 0;
    if (Arg5 != 0) goto loc_004BAC73;
    *(uint32_t *)(result + 0xC) = 0;
loc_004BACED:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10))) == 0) goto loc_004BAD4E;
    result = (((uint32_t)(local_rbx)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10))))) ? 1 : 0;
    local_r14 = (uint8_t)((1) | ((uint8_t)(result)));
    if (condition_is_equal) goto loc_004BAD07;
    if (Arg5 != 0) goto loc_004BAC73;
loc_004BAD07:
    if (Arg5 == 0) goto loc_004BAD15;
    goto loc_004BAD1B;
loc_004BAD15:
    local_r15 = ((uint32_t)((uint32_t)(local_rbx))) + (result);
loc_004BAD1B:
    Arg3 = 0;
    result = RtlpNormalizeAcl(local_r15, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + *(uint64_t *)(arg1) * 1, Arg3, Arg4);
    local_r14 = (uint8_t)((local_r14) | ((uint8_t)(result)));
    if (condition_is_equal) goto loc_004BAD37;
    if (Arg5 != 0) goto loc_004BAC73;
loc_004BAD37:
    if (Arg5 == 0) goto loc_004BAD44;
    goto loc_004BAD4C;
loc_004BAD44:
    *(uint32_t *)(result + 0x10) = (uint32_t)(local_rbx);
loc_004BAD4C:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(*(uint16_t *)(local_r15 + 0x2))));
loc_004BAD4E:
    if (((uint32_t)(local_rbx)) == (*(uint32_t *)(*(uint64_t *)(arg1) + 0x4))) goto loc_004BAD62;
    if (Arg5 != 0) goto loc_004BAC73;
    *(uint32_t *)(result + 0x4) = (uint32_t)(local_rbx);
loc_004BAD62:
    local_r15 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x4))) + (*(uint64_t *)(arg1));
    result = RtlLengthRequiredSid(*(uint8_t *)(local_r15 + 0x1), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x10)) + *(uint64_t *)(arg1) * 1, Arg3, Arg4);
    if (Arg5 == 0) {
        Arg1 = *(uint32_t *)(result + 0x4);
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = (Arg1) + (result);
        Arg2 = local_r15;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8))) == 0) goto loc_004BAC6A;
    if (((uint32_t)(local_rbx)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8))))) goto loc_004BADAD;
    if (Arg5 != 0) goto loc_004BAC73;
    *(uint32_t *)(result + 0x8) = (uint32_t)(local_rbx);
loc_004BADAD:
    local_r15 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8))) + (*(uint64_t *)(arg1));
    result = RtlLengthRequiredSid(*(uint8_t *)(local_r15 + 0x1), Arg2, Arg3, Arg4);
    if (Arg5 == 0) {
        Arg1 = *(uint32_t *)(result + 0x8);
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = (Arg1) + (result);
        Arg2 = local_r15;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_004BAC6A;
loc_004BADDF:
    local_r13 = 0;
loc_004BADE2:
    if (Arg5 != 0) goto loc_004BAC73;
    if (v_stack_p18 == 0) goto loc_004BAE01;
    if (v_stack_p10 != 0) goto loc_004BAE10;
    goto loc_004BAE13;
loc_004BAE01:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
loc_004BAE10:
    *(uint64_t *)(v_stack_p8) = result;
loc_004BAE13:
    if (v_stack_p20 == 0) goto loc_004BAC84;
    *(uint32_t *)(v_stack_p20) = (uint32_t)(local_rbx);
    goto loc_004BAC84;
loc_004BAE2B:
    result = 0;
loc_004BAE2D:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BABA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
