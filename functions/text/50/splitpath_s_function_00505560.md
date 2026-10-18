# splitpath_s

- RVA: `0x00505560`–`0x005057EE` (길이 `654` bytes)
- VA: `0x0000000140505560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C28E4`
- 디코드: `200`개 명령, `654/654` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00505644` → [strncpy_s](strncpy_s_function_00506140.md) (function, `0x00506140`)
- `0x005056B7` → [strncpy_s](strncpy_s_function_00506140.md) (function, `0x00506140`)
- `0x005056F9` → [strncpy_s](strncpy_s_function_00506140.md) (function, `0x00506140`)
- `0x00505723` → [strncpy_s](strncpy_s_function_00506140.md) (function, `0x00506140`)
- `0x0050574D` → [strncpy_s](strncpy_s_function_00506140.md) (function, `0x00506140`)
- `0x005057CE` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00505560  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00505565  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0050556A  55                              push rbp
0050556B  56                              push rsi
0050556C  57                              push rdi
0050556D  41 54                           push r12
0050556F  41 55                           push r13
00505571  41 56                           push r14
00505573  41 57                           push r15
00505575  48 83 EC 30                     sub rsp, 0x30
00505579  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
00505581  48 8B F9                        mov rdi, rcx
00505584  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
0050558C  4C 8B E2                        mov r12, rdx
0050558F  33 D2                           xor edx, edx
00505591  4D 8B E9                        mov r13, r9
00505594  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
00505598  49 8B F0                        mov rsi, r8
0050559B  8B CA                           mov ecx, edx
0050559D  48 85 FF                        test rdi, rdi
005055A0  74 0A                           je 0x1405055ac
005055A2  4D 85 E4                        test r12, r12
005055A5  75 0F                           jne 0x1405055b6
005055A7  4D 85 C0                        test r8, r8
005055AA  74 0F                           je 0x1405055bb
005055AC  B9 01 00 00 00                  mov ecx, 1
005055B1  E9 B6 01 00 00                  jmp 0x14050576c
005055B6  48 85 F6                        test rsi, rsi
005055B9  74 F1                           je 0x1405055ac
005055BB  4D 85 ED                        test r13, r13
005055BE  75 0C                           jne 0x1405055cc
005055C0  48 39 94 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rdx
005055C8  75 E2                           jne 0x1405055ac
005055CA  EB 0A                           jmp 0x1405055d6
005055CC  48 39 94 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rdx
005055D4  74 D6                           je 0x1405055ac
005055D6  4D 85 FF                        test r15, r15
005055D9  75 0C                           jne 0x1405055e7
005055DB  48 39 94 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rdx
005055E3  75 C7                           jne 0x1405055ac
005055E5  EB 0A                           jmp 0x1405055f1
005055E7  48 39 94 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rdx
005055EF  74 BB                           je 0x1405055ac
005055F1  4D 85 F6                        test r14, r14
005055F4  75 0C                           jne 0x140505602
005055F6  48 39 94 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdx
005055FE  75 AC                           jne 0x1405055ac
00505600  EB 0A                           jmp 0x14050560c
00505602  48 39 94 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdx
0050560A  74 A0                           je 0x1405055ac
0050560C  B8 01 00 00 00                  mov eax, 1
00505611  48 8B DF                        mov rbx, rdi
00505614  38 13                           cmp byte ptr [rbx], dl
00505616  74 09                           je 0x140505621
00505618  48 FF C3                        inc rbx
0050561B  48 83 E8 01                     sub rax, 1
0050561F  75 F3                           jne 0x140505614
00505621  80 3B 3A                        cmp byte ptr [rbx], 0x3a
00505624  75 2F                           jne 0x140505655
00505626  4D 85 E4                        test r12, r12
00505629  74 24                           je 0x14050564f
0050562B  48 83 FE 03                     cmp rsi, 3
0050562F  0F 82 3C 01 00 00               jb 0x140505771
00505635  41 B9 02 00 00 00               mov r9d, 2
0050563B  4C 8B C7                        mov r8, rdi
0050563E  48 8B D6                        mov rdx, rsi
00505641  49 8B CC                        mov rcx, r12
00505644  E8 F7 0A 00 00                  call 0x140506140
00505649  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
0050564D  33 D2                           xor edx, edx
0050564F  48 8D 7B 01                     lea rdi, [rbx + 1]
00505653  EB 09                           jmp 0x14050565e
00505655  4D 85 E4                        test r12, r12
00505658  74 04                           je 0x14050565e
0050565A  41 88 14 24                     mov byte ptr [r12], dl
0050565E  8A 07                           mov al, byte ptr [rdi]
00505660  48 8B EA                        mov rbp, rdx
00505663  48 8B F2                        mov rsi, rdx
00505666  48 8B DF                        mov rbx, rdi
00505669  84 C0                           test al, al
0050566B  74 56                           je 0x1405056c3
0050566D  3C 2F                           cmp al, 0x2f
0050566F  74 0D                           je 0x14050567e
00505671  3C 5C                           cmp al, 0x5c
00505673  74 09                           je 0x14050567e
00505675  3C 2E                           cmp al, 0x2e
00505677  75 09                           jne 0x140505682
00505679  48 8B F3                        mov rsi, rbx
0050567C  EB 04                           jmp 0x140505682
0050567E  48 8D 6B 01                     lea rbp, [rbx + 1]
00505682  48 FF C3                        inc rbx
00505685  8A 03                           mov al, byte ptr [rbx]
00505687  84 C0                           test al, al
00505689  75 E2                           jne 0x14050566d
0050568B  48 85 ED                        test rbp, rbp
0050568E  74 33                           je 0x1405056c3
00505690  4D 85 ED                        test r13, r13
00505693  74 29                           je 0x1405056be
00505695  4C 8B CD                        mov r9, rbp
00505698  4C 2B CF                        sub r9, rdi
0050569B  4C 39 8C 24 90 00 00 00         cmp qword ptr [rsp + 0x90], r9
005056A3  0F 86 BB 00 00 00               jbe 0x140505764
005056A9  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
005056B1  4C 8B C7                        mov r8, rdi
005056B4  49 8B CD                        mov rcx, r13
005056B7  E8 84 0A 00 00                  call 0x140506140
005056BC  33 D2                           xor edx, edx
005056BE  48 8B FD                        mov rdi, rbp
005056C1  EB 09                           jmp 0x1405056cc
005056C3  4D 85 ED                        test r13, r13
005056C6  74 04                           je 0x1405056cc
005056C8  41 88 55 00                     mov byte ptr [r13], dl
005056CC  48 85 F6                        test rsi, rsi
005056CF  74 59                           je 0x14050572a
005056D1  48 3B F7                        cmp rsi, rdi
005056D4  72 54                           jb 0x14050572a
005056D6  4D 85 FF                        test r15, r15
005056D9  74 25                           je 0x140505700
005056DB  4C 8B CE                        mov r9, rsi
005056DE  4C 2B CF                        sub r9, rdi
005056E1  4C 39 8C 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], r9
005056E9  76 75                           jbe 0x140505760
005056EB  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
005056F3  4C 8B C7                        mov r8, rdi
005056F6  49 8B CF                        mov rcx, r15
005056F9  E8 42 0A 00 00                  call 0x140506140
005056FE  33 D2                           xor edx, edx
00505700  4D 85 F6                        test r14, r14
00505703  74 57                           je 0x14050575c
00505705  48 2B DE                        sub rbx, rsi
00505708  48 39 9C 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rbx
00505710  76 4E                           jbe 0x140505760
00505712  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
0050571A  4C 8B CB                        mov r9, rbx
0050571D  4C 8B C6                        mov r8, rsi
00505720  49 8B CE                        mov rcx, r14
00505723  E8 18 0A 00 00                  call 0x140506140
00505728  EB 32                           jmp 0x14050575c
0050572A  4D 85 FF                        test r15, r15
0050572D  74 25                           je 0x140505754
0050572F  48 2B DF                        sub rbx, rdi
00505732  48 39 9C 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rbx
0050573A  76 24                           jbe 0x140505760
0050573C  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
00505744  4C 8B CB                        mov r9, rbx
00505747  4C 8B C7                        mov r8, rdi
0050574A  49 8B CF                        mov rcx, r15
0050574D  E8 EE 09 00 00                  call 0x140506140
00505752  33 D2                           xor edx, edx
00505754  4D 85 F6                        test r14, r14
00505757  74 03                           je 0x14050575c
00505759  41 88 16                        mov byte ptr [r14], dl
0050575C  33 C0                           xor eax, eax
0050575E  EB 78                           jmp 0x1405057d8
00505760  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
00505764  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
0050576C  4D 85 E4                        test r12, r12
0050576F  74 09                           je 0x14050577a
00505771  48 85 F6                        test rsi, rsi
00505774  74 04                           je 0x14050577a
00505776  41 88 14 24                     mov byte ptr [r12], dl
0050577A  4D 85 ED                        test r13, r13
0050577D  74 0E                           je 0x14050578d
0050577F  48 39 94 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rdx
00505787  76 04                           jbe 0x14050578d
00505789  41 88 55 00                     mov byte ptr [r13], dl
0050578D  4D 85 FF                        test r15, r15
00505790  74 0D                           je 0x14050579f
00505792  48 39 94 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rdx
0050579A  76 03                           jbe 0x14050579f
0050579C  41 88 17                        mov byte ptr [r15], dl
0050579F  4D 85 F6                        test r14, r14
005057A2  74 0D                           je 0x1405057b1
005057A4  48 39 94 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdx
005057AC  76 03                           jbe 0x1405057b1
005057AE  41 88 16                        mov byte ptr [r14], dl
005057B1  48 85 FF                        test rdi, rdi
005057B4  74 09                           je 0x1405057bf
005057B6  85 C9                           test ecx, ecx
005057B8  75 05                           jne 0x1405057bf
005057BA  8D 41 22                        lea eax, [rcx + 0x22]
005057BD  EB 19                           jmp 0x1405057d8
005057BF  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
005057C4  45 33 C9                        xor r9d, r9d
005057C7  33 D2                           xor edx, edx
005057C9  45 33 C0                        xor r8d, r8d
005057CC  33 C9                           xor ecx, ecx
005057CE  E8 7D 8D F9 FF                  call 0x14049e550
005057D3  B8 16 00 00 00                  mov eax, 0x16
005057D8  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
005057DD  48 83 C4 30                     add rsp, 0x30
005057E1  41 5F                           pop r15
005057E3  41 5E                           pop r14
005057E5  41 5D                           pop r13
005057E7  41 5C                           pop r12
005057E9  5F                              pop rdi
005057EA  5E                              pop rsi
005057EB  5D                              pop rbp
005057EC  C3                              ret
005057ED  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall splitpath_s(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (48);
    a2 = 0;
    v_stack_p8 = 0;
    if (a1 == 0) goto loc_005055AC;
    if (0 != 0) goto loc_005055B6;
    if (a3 == 0) goto loc_005055BB;
loc_005055AC:
    goto loc_0050576C;
loc_005055B6:
    if (a3 == 0) goto loc_005055AC;
loc_005055BB:
    if (a4 != 0) goto loc_005055CC;
    if (a5 != 0) goto loc_005055AC;
    goto loc_005055D6;
loc_005055CC:
    if (a5 == 0) goto loc_005055AC;
loc_005055D6:
    if (a6 != 0) goto loc_005055E7;
    if (a7 != 0) goto loc_005055AC;
    goto loc_005055F1;
loc_005055E7:
    if (a7 == 0) goto loc_005055AC;
loc_005055F1:
    if (a8 != 0) goto loc_00505602;
    if (a9 != 0) goto loc_005055AC;
    goto loc_0050560C;
loc_00505602:
    if (a9 == 0) goto loc_005055AC;
loc_0050560C:
loc_00505614:
    if ((*(unsigned __int8 *)(a1)) == 0) goto loc_00505621;
    v_rbx = (a1) + 1;
    result = (1) - (1);
    if (condition_is_not_equal) goto loc_00505614;
loc_00505621:
    if ((*(unsigned __int8 *)(v_rbx)) != 58) goto loc_00505655;
    if (0 == 0) goto loc_0050564F;
    if (a3 < 3) goto loc_00505771;
    result = strncpy_s(0, a3, a1, 2);
    a2 = 0;
loc_0050564F:
    goto loc_0050565E;
loc_00505655:
    if (0 != 0) {
        *(unsigned __int8 *)(a2) = 0;
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 1)) == 0) goto loc_005056C3;
loc_0050566D:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 1))) == 47) goto loc_0050567E;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 1))) == 92) goto loc_0050567E;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 1))) != 46) goto loc_00505682;
    goto loc_00505682;
loc_0050567E:
loc_00505682:
    v_rbx = (v_rbx + 1) + 1;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx)) != 0) goto loc_0050566D;
    if (v_rbx + 1 + 1 == 0) goto loc_005056C3;
    if (a4 == 0) goto loc_005056BE;
    a4 = (v_rbx + 1 + 1) - (v_rbx + 1);
    if (a5 <= a4) goto loc_00505764;
    result = strncpy_s(a4, a5, v_rbx + 1, a4);
    a2 = 0;
loc_005056BE:
    goto loc_005056CC;
loc_005056C3:
    if (a4 != 0) {
        *(unsigned __int8 *)(a4) = 0;
    }
    if (v_rbx + 1 == 0) goto loc_0050572A;
    if ((v_rbx + 1) < (v_rbx + 1 + 1)) goto loc_0050572A;
    if (a6 == 0) goto loc_00505700;
    a4 = (v_rbx + 1) - (v_rbx + 1 + 1);
    if (a7 <= a4) goto loc_00505760;
    result = strncpy_s(a6, a7, v_rbx + 1 + 1, a4);
    a2 = 0;
loc_00505700:
    if (a8 == 0) goto loc_0050575C;
    v_rbx = (v_rbx) - (v_rbx + 1);
    if (a9 <= v_rbx) goto loc_00505760;
    result = strncpy_s(a8, a9, v_rbx + 1, v_rbx);
    goto loc_0050575C;
loc_0050572A:
    if (a6 == 0) goto loc_00505754;
    v_rbx = (v_rbx) - (v_rbx + 1 + 1);
    if (a7 <= v_rbx) goto loc_00505760;
    result = strncpy_s(a6, a7, v_rbx + 1 + 1, v_rbx);
    a2 = 0;
loc_00505754:
    if (a8 != 0) {
        *(unsigned __int8 *)(a8) = 0;
    }
    result = 0;
    goto loc_005057D8;
loc_00505760:
loc_00505764:
loc_0050576C:
    if (0 == 0) goto loc_0050577A;
loc_00505771:
    if (v_stack_p18 != 0) {
        *(unsigned __int8 *)(a2) = 0;
    }
    if (a4 == 0) goto loc_0050578D;
    if (a5 >= = 0) {
        *(unsigned __int8 *)(a4) = 0;
    }
    if (a6 == 0) goto loc_0050579F;
    if (a7 >= = 0) {
        *(unsigned __int8 *)(a6) = 0;
    }
    if (a8 == 0) goto loc_005057B1;
    if (a9 >= = 0) {
        *(unsigned __int8 *)(a8) = 0;
    }
    if (v_rbx + 1 + 1 == 0) goto loc_005057BF;
    if ((unsigned int)((unsigned int)(v_stack_p8)) != 0) goto loc_005057BF;
    goto loc_005057D8;
loc_005057BF:
    v_stack_m48 = 0;
    a4 = 0;
    a2 = 0;
    a3 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
loc_005057D8:
    v_rsp = (v_rsp) + (48);
    return 22;
}
```

## 5. (Beta) C Style

```c
int64_t splitpath_s(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (48);
    Arg2 = 0;
    v_stack_p8 = 0;
    if (Arg1 == 0) goto loc_005055AC;
    if (0 != 0) goto loc_005055B6;
    if (Arg3 == 0) goto loc_005055BB;
loc_005055AC:
    goto loc_0050576C;
loc_005055B6:
    if (Arg3 == 0) goto loc_005055AC;
loc_005055BB:
    if (Arg4 != 0) goto loc_005055CC;
    if (Arg5 != 0) goto loc_005055AC;
    goto loc_005055D6;
loc_005055CC:
    if (Arg5 == 0) goto loc_005055AC;
loc_005055D6:
    if (Arg6 != 0) goto loc_005055E7;
    if (Arg7 != 0) goto loc_005055AC;
    goto loc_005055F1;
loc_005055E7:
    if (Arg7 == 0) goto loc_005055AC;
loc_005055F1:
    if (Arg8 != 0) goto loc_00505602;
    if (Arg9 != 0) goto loc_005055AC;
    goto loc_0050560C;
loc_00505602:
    if (Arg9 == 0) goto loc_005055AC;
loc_0050560C:
loc_00505614:
    if ((*(uint8_t *)(Arg1)) == 0) goto loc_00505621;
    local_rbx = (Arg1) + 1;
    result = (1) - (1);
    if (condition_is_not_equal) goto loc_00505614;
loc_00505621:
    if ((*(uint8_t *)(local_rbx)) != 58) goto loc_00505655;
    if (0 == 0) goto loc_0050564F;
    if (Arg3 < 3) goto loc_00505771;
    result = strncpy_s(0, Arg3, Arg1, 2);
    Arg2 = 0;
loc_0050564F:
    goto loc_0050565E;
loc_00505655:
    if (0 != 0) {
        *(uint8_t *)(Arg2) = 0;
    }
    if ((uint8_t)(*(uint8_t *)(local_rbx + 0x1)) == 0) goto loc_005056C3;
loc_0050566D:
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x1))) == 47) goto loc_0050567E;
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x1))) == 92) goto loc_0050567E;
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x1))) != 46) goto loc_00505682;
    goto loc_00505682;
loc_0050567E:
loc_00505682:
    local_rbx = (local_rbx + 1) + 1;
    if ((uint8_t)(*(uint8_t *)(local_rbx)) != 0) goto loc_0050566D;
    if (local_rbx + 1 + 1 == 0) goto loc_005056C3;
    if (Arg4 == 0) goto loc_005056BE;
    Arg4 = (local_rbx + 1 + 1) - (local_rbx + 1);
    if (Arg5 <= Arg4) goto loc_00505764;
    result = strncpy_s(Arg4, Arg5, local_rbx + 1, Arg4);
    Arg2 = 0;
loc_005056BE:
    goto loc_005056CC;
loc_005056C3:
    if (Arg4 != 0) {
        *(uint8_t *)(Arg4) = 0;
    }
    if (local_rbx + 1 == 0) goto loc_0050572A;
    if ((local_rbx + 1) < (local_rbx + 1 + 1)) goto loc_0050572A;
    if (Arg6 == 0) goto loc_00505700;
    Arg4 = (local_rbx + 1) - (local_rbx + 1 + 1);
    if (Arg7 <= Arg4) goto loc_00505760;
    result = strncpy_s(Arg6, Arg7, local_rbx + 1 + 1, Arg4);
    Arg2 = 0;
loc_00505700:
    if (Arg8 == 0) goto loc_0050575C;
    local_rbx = (local_rbx) - (local_rbx + 1);
    if (Arg9 <= local_rbx) goto loc_00505760;
    result = strncpy_s(Arg8, Arg9, local_rbx + 1, local_rbx);
    goto loc_0050575C;
loc_0050572A:
    if (Arg6 == 0) goto loc_00505754;
    local_rbx = (local_rbx) - (local_rbx + 1 + 1);
    if (Arg7 <= local_rbx) goto loc_00505760;
    result = strncpy_s(Arg6, Arg7, local_rbx + 1 + 1, local_rbx);
    Arg2 = 0;
loc_00505754:
    if (Arg8 != 0) {
        *(uint8_t *)(Arg8) = 0;
    }
    result = 0;
    goto loc_005057D8;
loc_00505760:
loc_00505764:
loc_0050576C:
    if (0 == 0) goto loc_0050577A;
loc_00505771:
    if (v_stack_p18 != 0) {
        *(uint8_t *)(Arg2) = 0;
    }
    if (Arg4 == 0) goto loc_0050578D;
    if (Arg5 >= = 0) {
        *(uint8_t *)(Arg4) = 0;
    }
    if (Arg6 == 0) goto loc_0050579F;
    if (Arg7 >= = 0) {
        *(uint8_t *)(Arg6) = 0;
    }
    if (Arg8 == 0) goto loc_005057B1;
    if (Arg9 >= = 0) {
        *(uint8_t *)(Arg8) = 0;
    }
    if (local_rbx + 1 + 1 == 0) goto loc_005057BF;
    if ((uint32_t)((uint32_t)(v_stack_p8)) != 0) goto loc_005057BF;
    goto loc_005057D8;
loc_005057BF:
    v_stack_m48 = 0;
    Arg4 = 0;
    Arg2 = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, Arg4);
loc_005057D8:
    local_rsp = (local_rsp) + (48);
    return 22;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00505560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
