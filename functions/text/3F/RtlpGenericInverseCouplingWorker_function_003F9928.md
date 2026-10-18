# RtlpGenericInverseCouplingWorker

- RVA: `0x003F9928`–`0x003F9C41` (길이 `793` bytes)
- VA: `0x00000001403F9928`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00098434`
- 디코드: `219`개 명령, `793/793` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlScrubMemory](RtlScrubMemory_function_003F96DC.md) at `0x003F97AF`
- [RtlScrubMemory](RtlScrubMemory_function_003F96DC.md) at `0x003F97BF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F9928  48 8B C4                        mov rax, rsp
003F992B  48 89 58 08                     mov qword ptr [rax + 8], rbx
003F992F  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
003F9933  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
003F9937  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
003F993B  41 54                           push r12
003F993D  41 55                           push r13
003F993F  41 56                           push r14
003F9941  41 57                           push r15
003F9943  BD 00 04 00 00                  mov ebp, 0x400
003F9948  44 8B F2                        mov r14d, edx
003F994B  4D 8B F8                        mov r15, r8
003F994E  44 8B D1                        mov r10d, ecx
003F9951  4D 8B D8                        mov r11, r8
003F9954  44 8B CD                        mov r9d, ebp
003F9957  44 8D 6D FF                     lea r13d, [rbp - 1]
003F995B  41 83 E7 04                     and r15d, 4
003F995F  0F 85 94 02 00 00               jne 0x1403f9bf9
003F9965  4D 8B E2                        mov r12, r10
003F9968  49 8B C9                        mov rcx, r9
003F996B  49 C1 E4 20                     shl r12, 0x20
003F996F  49 8B FB                        mov rdi, r11
003F9972  4D 0B E2                        or r12, r10
003F9975  48 D1 E9                        shr rcx, 1
003F9978  49 8B C4                        mov rax, r12
003F997B  F3 48 AB                        rep stosq qword ptr [rdi], rax
003F997E  41 F6 C1 01                     test r9b, 1
003F9982  74 05                           je 0x1403f9989
003F9984  47 89 54 8B FC                  mov dword ptr [r11 + r9*4 - 4], r10d
003F9989  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003F9992  45 33 C9                        xor r9d, r9d
003F9995  8B 90 E8 00 00 00               mov edx, dword ptr [rax + 0xe8]
003F999B  48 85 D2                        test rdx, rdx
003F999E  74 23                           je 0x1403f99c3
003F99A0  F0 44 09 0C 24                  lock or dword ptr [rsp], r9d
003F99A5  48 8D 4A FF                     lea rcx, [rdx - 1]
003F99A9  48 F7 D1                        not rcx
003F99AC  49 8D B8 00 10 00 00            lea rdi, [r8 + 0x1000]
003F99B3  49 23 C8                        and rcx, r8
003F99B6  EB 06                           jmp 0x1403f99be
003F99B8  0F AE 39                        clflush byte ptr [rcx]
003F99BB  48 03 CA                        add rcx, rdx
003F99BE  48 3B CF                        cmp rcx, rdi
003F99C1  72 F5                           jb 0x1403f99b8
003F99C3  49 8B C8                        mov rcx, r8
003F99C6  4D 8D 98 00 10 00 00            lea r11, [r8 + 0x1000]
003F99CD  49 3B CB                        cmp rcx, r11
003F99D0  73 12                           jae 0x1403f99e4
003F99D2  44 39 11                        cmp dword ptr [rcx], r10d
003F99D5  0F 85 1A 02 00 00               jne 0x1403f9bf5
003F99DB  44 89 11                        mov dword ptr [rcx], r10d
003F99DE  48 83 C1 04                     add rcx, 4
003F99E2  EB E9                           jmp 0x1403f99cd
003F99E4  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003F99ED  8B 90 E8 00 00 00               mov edx, dword ptr [rax + 0xe8]
003F99F3  48 85 D2                        test rdx, rdx
003F99F6  74 1C                           je 0x1403f9a14
003F99F8  F0 44 09 0C 24                  lock or dword ptr [rsp], r9d
003F99FD  48 8D 4A FF                     lea rcx, [rdx - 1]
003F9A01  48 F7 D1                        not rcx
003F9A04  49 23 C8                        and rcx, r8
003F9A07  EB 06                           jmp 0x1403f9a0f
003F9A09  0F AE 39                        clflush byte ptr [rcx]
003F9A0C  48 03 CA                        add rcx, rdx
003F9A0F  49 3B CB                        cmp rcx, r11
003F9A12  72 F5                           jb 0x1403f9a09
003F9A14  49 8B C8                        mov rcx, r8
003F9A17  49 3B CB                        cmp rcx, r11
003F9A1A  73 0F                           jae 0x1403f9a2b
003F9A1C  44 39 11                        cmp dword ptr [rcx], r10d
003F9A1F  0F 85 D0 01 00 00               jne 0x1403f9bf5
003F9A25  48 83 C1 04                     add rcx, 4
003F9A29  EB EC                           jmp 0x1403f9a17
003F9A2B  49 8B D0                        mov rdx, r8
003F9A2E  4D 85 FF                        test r15, r15
003F9A31  0F 85 D1 01 00 00               jne 0x1403f9c08
003F9A37  B9 00 02 00 00                  mov ecx, 0x200
003F9A3C  49 8B F1                        mov rsi, r9
003F9A3F  BB FC 0F 00 00                  mov ebx, 0xffc
003F9A44  48 8B FA                        mov rdi, rdx
003F9A47  49 8B C4                        mov rax, r12
003F9A4A  F3 48 AB                        rep stosq qword ptr [rdi], rax
003F9A4D  48 85 F6                        test rsi, rsi
003F9A50  74 04                           je 0x1403f9a56
003F9A52  44 89 14 13                     mov dword ptr [rbx + rdx], r10d
003F9A56  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003F9A5F  8B 90 E8 00 00 00               mov edx, dword ptr [rax + 0xe8]
003F9A65  48 85 D2                        test rdx, rdx
003F9A68  74 1C                           je 0x1403f9a86
003F9A6A  F0 44 09 0C 24                  lock or dword ptr [rsp], r9d
003F9A6F  48 8D 4A FF                     lea rcx, [rdx - 1]
003F9A73  48 F7 D1                        not rcx
003F9A76  49 23 C8                        and rcx, r8
003F9A79  EB 06                           jmp 0x1403f9a81
003F9A7B  0F AE 39                        clflush byte ptr [rcx]
003F9A7E  48 03 CA                        add rcx, rdx
003F9A81  49 3B CB                        cmp rcx, r11
003F9A84  72 F5                           jb 0x1403f9a7b
003F9A86  49 8B D8                        mov rbx, r8
003F9A89  4C 8B DD                        mov r11, rbp
003F9A8C  4D 85 FF                        test r15, r15
003F9A8F  0F 85 8E 01 00 00               jne 0x1403f9c23
003F9A95  49 8B C6                        mov rax, r14
003F9A98  49 8B CB                        mov rcx, r11
003F9A9B  48 C1 E0 20                     shl rax, 0x20
003F9A9F  48 8B FB                        mov rdi, rbx
003F9AA2  49 0B C6                        or rax, r14
003F9AA5  48 D1 E9                        shr rcx, 1
003F9AA8  F3 48 AB                        rep stosq qword ptr [rdi], rax
003F9AAB  41 F6 C3 01                     test r11b, 1
003F9AAF  74 05                           je 0x1403f9ab6
003F9AB1  46 89 74 9B FC                  mov dword ptr [rbx + r11*4 - 4], r14d
003F9AB6  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003F9ABF  8B 90 E8 00 00 00               mov edx, dword ptr [rax + 0xe8]
003F9AC5  48 85 D2                        test rdx, rdx
003F9AC8  74 23                           je 0x1403f9aed
003F9ACA  F0 44 09 0C 24                  lock or dword ptr [rsp], r9d
003F9ACF  48 8D 4A FF                     lea rcx, [rdx - 1]
003F9AD3  48 F7 D1                        not rcx
003F9AD6  49 8D B8 00 10 00 00            lea rdi, [r8 + 0x1000]
003F9ADD  49 23 C8                        and rcx, r8
003F9AE0  EB 06                           jmp 0x1403f9ae8
003F9AE2  0F AE 39                        clflush byte ptr [rcx]
003F9AE5  48 03 CA                        add rcx, rdx
003F9AE8  48 3B CF                        cmp rcx, rdi
003F9AEB  72 F5                           jb 0x1403f9ae2
003F9AED  49 8B C8                        mov rcx, r8
003F9AF0  49 8D 90 00 10 00 00            lea rdx, [r8 + 0x1000]
003F9AF7  48 3B CA                        cmp rcx, rdx
003F9AFA  73 0F                           jae 0x1403f9b0b
003F9AFC  44 39 31                        cmp dword ptr [rcx], r14d
003F9AFF  0F 85 F0 00 00 00               jne 0x1403f9bf5
003F9B05  48 83 C1 04                     add rcx, 4
003F9B09  EB EC                           jmp 0x1403f9af7
003F9B0B  4D 8B D8                        mov r11, r8
003F9B0E  41 F6 C0 04                     test r8b, 4
003F9B12  0F 85 1A 01 00 00               jne 0x1403f9c32
003F9B18  49 8B C2                        mov rax, r10
003F9B1B  48 8B CD                        mov rcx, rbp
003F9B1E  48 C1 E0 20                     shl rax, 0x20
003F9B22  49 8B FB                        mov rdi, r11
003F9B25  49 0B C2                        or rax, r10
003F9B28  48 D1 E9                        shr rcx, 1
003F9B2B  F3 48 AB                        rep stosq qword ptr [rdi], rax
003F9B2E  40 F6 C5 01                     test bpl, 1
003F9B32  74 05                           je 0x1403f9b39
003F9B34  45 89 54 AB FC                  mov dword ptr [r11 + rbp*4 - 4], r10d
003F9B39  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003F9B42  8B 90 E8 00 00 00               mov edx, dword ptr [rax + 0xe8]
003F9B48  48 85 D2                        test rdx, rdx
003F9B4B  74 23                           je 0x1403f9b70
003F9B4D  F0 44 09 0C 24                  lock or dword ptr [rsp], r9d
003F9B52  48 8D 4A FF                     lea rcx, [rdx - 1]
003F9B56  48 F7 D1                        not rcx
003F9B59  49 8D B8 00 10 00 00            lea rdi, [r8 + 0x1000]
003F9B60  49 23 C8                        and rcx, r8
003F9B63  EB 06                           jmp 0x1403f9b6b
003F9B65  0F AE 39                        clflush byte ptr [rcx]
003F9B68  48 03 CA                        add rcx, rdx
003F9B6B  48 3B CF                        cmp rcx, rdi
003F9B6E  72 F5                           jb 0x1403f9b65
003F9B70  49 8D 80 00 10 00 00            lea rax, [r8 + 0x1000]
003F9B77  48 83 E8 04                     sub rax, 4
003F9B7B  44 89 30                        mov dword ptr [rax], r14d
003F9B7E  49 3B C0                        cmp rax, r8
003F9B81  75 F4                           jne 0x1403f9b77
003F9B83  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003F9B8C  8B 90 E8 00 00 00               mov edx, dword ptr [rax + 0xe8]
003F9B92  48 85 D2                        test rdx, rdx
003F9B95  74 23                           je 0x1403f9bba
003F9B97  F0 44 09 0C 24                  lock or dword ptr [rsp], r9d
003F9B9C  48 8D 4A FF                     lea rcx, [rdx - 1]
003F9BA0  48 F7 D1                        not rcx
003F9BA3  49 8D B8 00 10 00 00            lea rdi, [r8 + 0x1000]
003F9BAA  49 23 C8                        and rcx, r8
003F9BAD  EB 06                           jmp 0x1403f9bb5
003F9BAF  0F AE 39                        clflush byte ptr [rcx]
003F9BB2  48 03 CA                        add rcx, rdx
003F9BB5  48 3B CF                        cmp rcx, rdi
003F9BB8  72 F5                           jb 0x1403f9baf
003F9BBA  49 8D 80 00 10 00 00            lea rax, [r8 + 0x1000]
003F9BC1  4C 3B C0                        cmp r8, rax
003F9BC4  73 0B                           jae 0x1403f9bd1
003F9BC6  45 39 30                        cmp dword ptr [r8], r14d
003F9BC9  75 09                           jne 0x1403f9bd4
003F9BCB  49 83 C0 04                     add r8, 4
003F9BCF  EB F0                           jmp 0x1403f9bc1
003F9BD1  41 B1 01                        mov r9b, 1
003F9BD4  41 8A C1                        mov al, r9b
003F9BD7  48 8B 5C 24 28                  mov rbx, qword ptr [rsp + 0x28]
003F9BDC  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
003F9BE1  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003F9BE6  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
003F9BEB  41 5F                           pop r15
003F9BED  41 5E                           pop r14
003F9BEF  41 5D                           pop r13
003F9BF1  41 5C                           pop r12
003F9BF3  C3                              ret
003F9BF4  CC                              int3
003F9BF5  32 C0                           xor al, al
003F9BF7  EB DE                           jmp 0x1403f9bd7
003F9BF9  45 89 10                        mov dword ptr [r8], r10d
003F9BFC  4D 8D 58 04                     lea r11, [r8 + 4]
003F9C00  4D 8B CD                        mov r9, r13
003F9C03  E9 5D FD FF FF                  jmp 0x1403f9965
003F9C08  45 89 10                        mov dword ptr [r8], r10d
003F9C0B  49 8D 50 04                     lea rdx, [r8 + 4]
003F9C0F  B9 FF 01 00 00                  mov ecx, 0x1ff
003F9C14  BE 01 00 00 00                  mov esi, 1
003F9C19  BB F8 0F 00 00                  mov ebx, 0xff8
003F9C1E  E9 21 FE FF FF                  jmp 0x1403f9a44
003F9C23  45 89 30                        mov dword ptr [r8], r14d
003F9C26  49 8D 58 04                     lea rbx, [r8 + 4]
003F9C2A  4D 8B DD                        mov r11, r13
003F9C2D  E9 63 FE FF FF                  jmp 0x1403f9a95
003F9C32  45 89 10                        mov dword ptr [r8], r10d
003F9C35  4D 8D 58 04                     lea r11, [r8 + 4]
003F9C39  49 8B ED                        mov rbp, r13
003F9C3C  E9 D7 FE FF FF                  jmp 0x1403f9b18
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpGenericInverseCouplingWorker(int a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_r15 = (unsigned int)((a3) & (4));
    if (condition_is_not_equal) goto loc_003F9BF9;
loc_003F9965:
    v_r12 = ((unsigned int)(a1)) << (32);
    v_r12 = (v_r12) | ((unsigned int)(a1));
    a1 = ((unsigned int)((unsigned int)((unsigned int)(0x400ULL)))) >> (1);
    if ((((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(0x400ULL))))) & (1)) != 0) {
        *(unsigned int *)(a3 + (unsigned int)((unsigned int)((unsigned int)(0x400ULL))) * 4 - 4) = (unsigned int)((unsigned int)(a1));
    }
    a4 = 0;
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003F99C3;
    a1 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a1 = (a1) & (a3);
    goto loc_003F99BE;
loc_003F99B8:
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
loc_003F99BE:
    if (a1 < (a3 + 4096)) goto loc_003F99B8;
loc_003F99C3:
loc_003F99CD:
    if (a3 >= (a3 + 4096)) goto loc_003F99E4;
    if ((*(unsigned int *)(a3)) != ((unsigned int)((unsigned int)(a1)))) goto loc_003F9BF5;
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(a1));
    a1 = (a3) + (4);
    goto loc_003F99CD;
loc_003F99E4:
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003F9A14;
    a1 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a1 = (a1) & (a3);
    goto loc_003F9A0F;
loc_003F9A09:
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
loc_003F9A0F:
    if (a1 < (a3 + 4096)) goto loc_003F9A09;
loc_003F9A14:
loc_003F9A17:
    if (a3 >= (a3 + 4096)) goto loc_003F9A2B;
    if ((*(unsigned int *)(a3)) != ((unsigned int)((unsigned int)(a1)))) goto loc_003F9BF5;
    a1 = (a3) + (4);
    goto loc_003F9A17;
loc_003F9A2B:
    if (v_r15 != 0) goto loc_003F9C08;
loc_003F9A44:
    if (0 != 0) {
        *(unsigned int *)((unsigned int)(0xFFCULL) + a3 * 1) = (unsigned int)((unsigned int)(a1));
    }
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003F9A86;
    a1 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a1 = (a1) & (a3);
    goto loc_003F9A81;
loc_003F9A7B:
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
loc_003F9A81:
    if (a1 < (a3 + 4096)) goto loc_003F9A7B;
loc_003F9A86:
    if (v_r15 != 0) goto loc_003F9C23;
loc_003F9A95:
    result = ((unsigned int)(a2)) << (32);
    result = (result) | ((unsigned int)(a2));
    a1 = ((unsigned int)(0x400ULL)) >> (1);
    if ((((unsigned __int8)((unsigned int)(0x400ULL))) & (1)) != 0) {
        *(unsigned int *)(a3 + (unsigned int)(0x400ULL) * 4 - 4) = (unsigned int)((unsigned int)(a2));
    }
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003F9AED;
    a1 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a1 = (a1) & (a3);
    goto loc_003F9AE8;
loc_003F9AE2:
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
loc_003F9AE8:
    if (a1 < (a3 + 4096)) goto loc_003F9AE2;
loc_003F9AED:
loc_003F9AF7:
    if (a3 >= (a3 + 4096)) goto loc_003F9B0B;
    if ((*(unsigned int *)(a3)) != ((unsigned int)((unsigned int)(a2)))) goto loc_003F9BF5;
    a1 = (a3) + (4);
    goto loc_003F9AF7;
loc_003F9B0B:
    if ((((unsigned __int8)(a3)) & (4)) != 0) goto loc_003F9C32;
loc_003F9B18:
    result = ((unsigned int)(a1)) << (32);
    result = (result) | ((unsigned int)(a1));
    a1 = ((unsigned int)(0x400ULL)) >> (1);
    if ((((unsigned __int8)((unsigned int)(0x400ULL))) & (1)) != 0) {
        *(unsigned int *)(a3 + (unsigned int)(0x400ULL) * 4 - 4) = (unsigned int)((unsigned int)(a1));
    }
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003F9B70;
    a1 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a1 = (a1) & (a3);
    goto loc_003F9B6B;
loc_003F9B65:
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
loc_003F9B6B:
    if (a1 < (a3 + 4096)) goto loc_003F9B65;
loc_003F9B70:
loc_003F9B77:
    result = (a3 + 4096) - (4);
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(a2));
    if (result != a3) goto loc_003F9B77;
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003F9BBA;
    a1 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a1 = (a1) & (a3);
    goto loc_003F9BB5;
loc_003F9BAF:
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
loc_003F9BB5:
    if (a1 < (a3 + 4096)) goto loc_003F9BAF;
loc_003F9BBA:
loc_003F9BC1:
    if (a3 >= (a3 + 4096)) goto loc_003F9BD1;
    if ((*(unsigned int *)(a3)) != ((unsigned int)((unsigned int)(a2)))) goto loc_003F9BD4;
    a3 = (a3) + (4);
    goto loc_003F9BC1;
loc_003F9BD1:
loc_003F9BD4:
loc_003F9BD7:
    return 1;
loc_003F9BF5:
    result = 0;
    goto loc_003F9BD7;
loc_003F9BF9:
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(a1));
    goto loc_003F9965;
loc_003F9C08:
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(a1));
    goto loc_003F9A44;
loc_003F9C23:
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(a2));
    goto loc_003F9A95;
loc_003F9C32:
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(a1));
    goto loc_003F9B18;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpGenericInverseCouplingWorker(int32_t Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    uint32_t v_stack_m20;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_r15 = (uint32_t)((Arg3) & (4));
    if (condition_is_not_equal) goto loc_003F9BF9;
loc_003F9965:
    local_r12 = ((uint32_t)(Arg1)) << (32);
    local_r12 = (local_r12) | ((uint32_t)(Arg1));
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(0x400ULL)))) >> (1);
    if ((((uint8_t)((uint32_t)((uint32_t)((uint32_t)(0x400ULL))))) & (1)) != 0) {
        *(uint32_t *)(arg3 + (uint32_t)((uint32_t)((uint32_t)(0x400ULL))) * 4 - 0x4) = (uint32_t)((uint32_t)(Arg1));
    }
    a4 = 0;
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003F99C3;
    Arg1 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    Arg1 = (Arg1) & (Arg3);
    goto loc_003F99BE;
loc_003F99B8:
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
loc_003F99BE:
    if (Arg1 < (Arg3 + 4096)) goto loc_003F99B8;
loc_003F99C3:
loc_003F99CD:
    if (Arg3 >= (Arg3 + 4096)) goto loc_003F99E4;
    if ((*(uint32_t *)(arg3)) != ((uint32_t)((uint32_t)(Arg1)))) goto loc_003F9BF5;
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(Arg1));
    Arg1 = (Arg3) + (4);
    goto loc_003F99CD;
loc_003F99E4:
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003F9A14;
    Arg1 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    Arg1 = (Arg1) & (Arg3);
    goto loc_003F9A0F;
loc_003F9A09:
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
loc_003F9A0F:
    if (Arg1 < (Arg3 + 4096)) goto loc_003F9A09;
loc_003F9A14:
loc_003F9A17:
    if (Arg3 >= (Arg3 + 4096)) goto loc_003F9A2B;
    if ((*(uint32_t *)(arg3)) != ((uint32_t)((uint32_t)(Arg1)))) goto loc_003F9BF5;
    Arg1 = (Arg3) + (4);
    goto loc_003F9A17;
loc_003F9A2B:
    if (local_r15 != 0) goto loc_003F9C08;
loc_003F9A44:
    if (0 != 0) {
        *(uint32_t *)((uint32_t)(0xFFCULL) + arg3 * 1) = (uint32_t)((uint32_t)(Arg1));
    }
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003F9A86;
    Arg1 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    Arg1 = (Arg1) & (Arg3);
    goto loc_003F9A81;
loc_003F9A7B:
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
loc_003F9A81:
    if (Arg1 < (Arg3 + 4096)) goto loc_003F9A7B;
loc_003F9A86:
    if (local_r15 != 0) goto loc_003F9C23;
loc_003F9A95:
    result = ((uint32_t)(Arg2)) << (32);
    result = (result) | ((uint32_t)(Arg2));
    Arg1 = ((uint32_t)(0x400ULL)) >> (1);
    if ((((uint8_t)((uint32_t)(0x400ULL))) & (1)) != 0) {
        *(uint32_t *)(arg3 + (uint32_t)(0x400ULL) * 4 - 0x4) = (uint32_t)((uint32_t)(Arg2));
    }
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003F9AED;
    Arg1 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    Arg1 = (Arg1) & (Arg3);
    goto loc_003F9AE8;
loc_003F9AE2:
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
loc_003F9AE8:
    if (Arg1 < (Arg3 + 4096)) goto loc_003F9AE2;
loc_003F9AED:
loc_003F9AF7:
    if (Arg3 >= (Arg3 + 4096)) goto loc_003F9B0B;
    if ((*(uint32_t *)(arg3)) != ((uint32_t)((uint32_t)(Arg2)))) goto loc_003F9BF5;
    Arg1 = (Arg3) + (4);
    goto loc_003F9AF7;
loc_003F9B0B:
    if ((((uint8_t)(Arg3)) & (4)) != 0) goto loc_003F9C32;
loc_003F9B18:
    result = ((uint32_t)(Arg1)) << (32);
    result = (result) | ((uint32_t)(Arg1));
    Arg1 = ((uint32_t)(0x400ULL)) >> (1);
    if ((((uint8_t)((uint32_t)(0x400ULL))) & (1)) != 0) {
        *(uint32_t *)(arg3 + (uint32_t)(0x400ULL) * 4 - 0x4) = (uint32_t)((uint32_t)(Arg1));
    }
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003F9B70;
    Arg1 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    Arg1 = (Arg1) & (Arg3);
    goto loc_003F9B6B;
loc_003F9B65:
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
loc_003F9B6B:
    if (Arg1 < (Arg3 + 4096)) goto loc_003F9B65;
loc_003F9B70:
loc_003F9B77:
    result = (Arg3 + 4096) - (4);
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(Arg2));
    if (result != Arg3) goto loc_003F9B77;
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003F9BBA;
    Arg1 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    Arg1 = (Arg1) & (Arg3);
    goto loc_003F9BB5;
loc_003F9BAF:
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
loc_003F9BB5:
    if (Arg1 < (Arg3 + 4096)) goto loc_003F9BAF;
loc_003F9BBA:
loc_003F9BC1:
    if (Arg3 >= (Arg3 + 4096)) goto loc_003F9BD1;
    if ((*(uint32_t *)(arg3)) != ((uint32_t)((uint32_t)(Arg2)))) goto loc_003F9BD4;
    Arg3 = (Arg3) + (4);
    goto loc_003F9BC1;
loc_003F9BD1:
loc_003F9BD4:
loc_003F9BD7:
    return 1;
loc_003F9BF5:
    result = 0;
    goto loc_003F9BD7;
loc_003F9BF9:
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(Arg1));
    goto loc_003F9965;
loc_003F9C08:
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(Arg1));
    goto loc_003F9A44;
loc_003F9C23:
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(Arg2));
    goto loc_003F9A95;
loc_003F9C32:
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(Arg1));
    goto loc_003F9B18;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `- 0x4 + r11*4` | `32` | `W` |
| `Arg3` | `- 0x4 + r9*4` | `32` | `W` |
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x4` | `64` | `R` |
| `Arg3` | `+ 0x1000` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F9928&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
