# VmpConvertPortionVpnRangeToGpnRange

- RVA: `0x003147F0`–`0x00314AED` (길이 `765` bytes)
- VA: `0x00000001403147F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00074864`
- 디코드: `210`개 명령, `765/765` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00314AC9` → [VmpVaMemoryRangeGetNext](../4A/VmpVaMemoryRangeGetNext_function_004ACEEC.md) (function, `0x004ACEEC`)

### Direct callers
- [VmpFlushTb](VmpFlushTb_function_00311BD0.md) at `0x00311C8D`
- [VmpFlushTb](VmpFlushTb_function_00311BD0.md) at `0x00311E25`
- [VmpFlushTb](VmpFlushTb_function_00311BD0.md) at `0x00311EC7`
- [sub_003142E3](Unknown_function_003142E3.md) at `0x0031438B`
- [VmpQueryAccessedState](../42/VmpQueryAccessedState_function_004290A8.md) at `0x00429185`
- [VmpFillGpnRanges](../42/VmpFillGpnRanges_function_0042A5D4.md) at `0x0042A635`
- [VmpUpdateCommitStateMemoryRange](../64/VmpUpdateCommitStateMemoryRange_function_0064D5D0.md) at `0x0064D6E7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00314A7B` → [sub_006E128A](../6E/Unknown_function_006E128A.md) (`tail-transfer`)
  - `0x00314A8A` → [sub_006E128A](../6E/Unknown_function_006E128A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003147F0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
003147F5  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
003147FA  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003147FF  55                              push rbp
00314800  56                              push rsi
00314801  57                              push rdi
00314802  41 54                           push r12
00314804  41 55                           push r13
00314806  41 56                           push r14
00314808  41 57                           push r15
0031480A  48 83 EC 30                     sub rsp, 0x30
0031480E  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00314814  49 8B F1                        mov rsi, r9
00314817  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0031481D  4D 8B E8                        mov r13, r8
00314820  4C 8B D2                        mov r10, rdx
00314823  4C 8B D9                        mov r11, rcx
00314826  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0031482E  45 33 E4                        xor r12d, r12d
00314831  48 8B AC 24 98 00 00 00         mov rbp, qword ptr [rsp + 0x98]
00314839  4D 8B 72 08                     mov r14, qword ptr [r10 + 8]
0031483D  49 8B 1A                        mov rbx, qword ptr [r10]
00314840  49 FF CE                        dec r14
00314843  4C 21 60 08                     and qword ptr [rax + 8], r12
00314847  4C 03 F3                        add r14, rbx
0031484A  44 21 65 00                     and dword ptr [rbp], r12d
0031484E  48 8B 3E                        mov rdi, qword ptr [rsi]
00314851  48 85 FF                        test rdi, rdi
00314854  74 13                           je 0x140314869
00314856  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0031485A  48 85 C0                        test rax, rax
0031485D  0F 85 CB 01 00 00               jne 0x140314a2e
00314863  48 3B 5F 18                     cmp rbx, qword ptr [rdi + 0x18]
00314867  73 52                           jae 0x1403148bb
00314869  49 8D 53 18                     lea rdx, [r11 + 0x18]
0031486D  F6 42 08 01                     test byte ptr [rdx + 8], 1
00314871  48 8B 0A                        mov rcx, qword ptr [rdx]
00314874  0F 85 86 01 00 00               jne 0x140314a00
0031487A  44 0F B6 42 08                  movzx r8d, byte ptr [rdx + 8]
0031487F  41 83 E0 01                     and r8d, 1
00314883  33 FF                           xor edi, edi
00314885  48 85 C9                        test rcx, rcx
00314888  0F 84 5A 01 00 00               je 0x1403149e8
0031488E  48 3B 59 20                     cmp rbx, qword ptr [rcx + 0x20]
00314892  0F 87 AC 01 00 00               ja 0x140314a44
00314898  48 8B F9                        mov rdi, rcx
0031489B  48 8B 01                        mov rax, qword ptr [rcx]
0031489E  48 3B 59 18                     cmp rbx, qword ptr [rcx + 0x18]
003148A2  0F 83 08 01 00 00               jae 0x1403149b0
003148A8  45 85 C0                        test r8d, r8d
003148AB  74 09                           je 0x1403148b6
003148AD  48 85 C0                        test rax, rax
003148B0  0F 85 5C 01 00 00               jne 0x140314a12
003148B6  48 8B C8                        mov rcx, rax
003148B9  EB CA                           jmp 0x140314885
003148BB  48 3B 5F 20                     cmp rbx, qword ptr [rdi + 0x20]
003148BF  77 A8                           ja 0x140314869
003148C1  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
003148C5  48 3B D9                        cmp rbx, rcx
003148C8  0F 82 25 01 00 00               jb 0x1403149f3
003148CE  48 89 3E                        mov qword ptr [rsi], rdi
003148D1  4D 85 E4                        test r12, r12
003148D4  75 04                           jne 0x1403148da
003148D6  4C 8B 67 28                     mov r12, qword ptr [rdi + 0x28]
003148DA  41 8B 44 24 40                  mov eax, dword ptr [r12 + 0x40]
003148DF  A8 01                           test al, 1
003148E1  0F 85 6F 01 00 00               jne 0x140314a56
003148E7  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
003148EC  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
003148F0  49 8B 44 24 30                  mov rax, qword ptr [r12 + 0x30]
003148F5  4C 8B 9C 24 90 00 00 00         mov r11, qword ptr [rsp + 0x90]
003148FD  48 2B C1                        sub rax, rcx
00314900  48 03 C3                        add rax, rbx
00314903  49 89 03                        mov qword ptr [r11], rax
00314906  49 8B C6                        mov rax, r14
00314909  48 2B C3                        sub rax, rbx
0031490C  48 FF C0                        inc rax
0031490F  49 3B C5                        cmp rax, r13
00314912  0F 87 77 01 00 00               ja 0x140314a8f
00314918  49 8B D6                        mov rdx, r14
0031491B  4C 8B 4F 20                     mov r9, qword ptr [rdi + 0x20]
0031491F  45 33 C0                        xor r8d, r8d
00314922  49 3B D1                        cmp rdx, r9
00314925  0F 83 70 01 00 00               jae 0x140314a9b
0031492B  48 8B C2                        mov rax, rdx
0031492E  48 2B C3                        sub rax, rbx
00314931  48 FF C0                        inc rax
00314934  49 89 43 08                     mov qword ptr [r11 + 8], rax
00314938  48 8D 42 01                     lea rax, [rdx + 1]
0031493C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00314941  49 3B D6                        cmp rdx, r14
00314944  0F 85 6C 01 00 00               jne 0x140314ab6
0031494A  41 B8 01 00 00 00               mov r8d, 1
00314950  4C 2B F0                        sub r14, rax
00314953  8B 47 48                        mov eax, dword ptr [rdi + 0x48]
00314956  4D 8D 4E 01                     lea r9, [r14 + 1]
0031495A  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
0031495F  A8 02                           test al, 2
00314961  74 04                           je 0x140314967
00314963  83 4D 00 02                     or dword ptr [rbp], 2
00314967  45 85 C0                        test r8d, r8d
0031496A  74 28                           je 0x140314994
0031496C  49 8B 14 24                     mov rdx, qword ptr [r12]
00314970  48 8D 47 28                     lea rax, [rdi + 0x28]
00314974  48 3B D0                        cmp rdx, rax
00314977  0F 85 59 01 00 00               jne 0x140314ad6
0031497D  4D 85 C9                        test r9, r9
00314980  0F 85 3D 01 00 00               jne 0x140314ac3
00314986  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0031498B  0F 10 44 24 20                  movups xmm0, xmmword ptr [rsp + 0x20]
00314990  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
00314994  48 8B C3                        mov rax, rbx
00314997  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
0031499F  48 83 C4 30                     add rsp, 0x30
003149A3  41 5F                           pop r15
003149A5  41 5E                           pop r14
003149A7  41 5D                           pop r13
003149A9  41 5C                           pop r12
003149AB  5F                              pop rdi
003149AC  5E                              pop rsi
003149AD  5D                              pop rbp
003149AE  C3                              ret
003149AF  CC                              int3
003149B0  45 85 C0                        test r8d, r8d
003149B3  75 65                           jne 0x140314a1a
003149B5  33 D2                           xor edx, edx
003149B7  48 85 C0                        test rax, rax
003149BA  74 2C                           je 0x1403149e8
003149BC  48 3B 58 20                     cmp rbx, qword ptr [rax + 0x20]
003149C0  0F 87 87 00 00 00               ja 0x140314a4d
003149C6  48 8B 08                        mov rcx, qword ptr [rax]
003149C9  48 3B 58 18                     cmp rbx, qword ptr [rax + 0x18]
003149CD  73 55                           jae 0x140314a24
003149CF  45 85 C0                        test r8d, r8d
003149D2  74 05                           je 0x1403149d9
003149D4  48 85 C9                        test rcx, rcx
003149D7  75 50                           jne 0x140314a29
003149D9  48 8B C1                        mov rax, rcx
003149DC  48 85 C0                        test rax, rax
003149DF  75 DB                           jne 0x1403149bc
003149E1  48 85 D2                        test rdx, rdx
003149E4  48 0F 45 FA                     cmovne rdi, rdx
003149E8  48 85 FF                        test rdi, rdi
003149EB  0F 85 D0 FE FF FF               jne 0x1403148c1
003149F1  EB 93                           jmp 0x140314986
003149F3  4C 3B F1                        cmp r14, rcx
003149F6  72 8E                           jb 0x140314986
003149F8  48 8B D9                        mov rbx, rcx
003149FB  E9 CE FE FF FF                  jmp 0x1403148ce
00314A00  48 85 C9                        test rcx, rcx
00314A03  74 08                           je 0x140314a0d
00314A05  48 33 CA                        xor rcx, rdx
00314A08  E9 6D FE FF FF                  jmp 0x14031487a
00314A0D  E9 68 FE FF FF                  jmp 0x14031487a
00314A12  48 33 C8                        xor rcx, rax
00314A15  E9 6B FE FF FF                  jmp 0x140314885
00314A1A  48 85 C0                        test rax, rax
00314A1D  74 96                           je 0x1403149b5
00314A1F  48 33 C1                        xor rax, rcx
00314A22  EB 91                           jmp 0x1403149b5
00314A24  48 8B D0                        mov rdx, rax
00314A27  EB A6                           jmp 0x1403149cf
00314A29  48 33 C1                        xor rax, rcx
00314A2C  EB AE                           jmp 0x1403149dc
00314A2E  48 83 66 08 00                  and qword ptr [rsi + 8], 0
00314A33  4C 8B E0                        mov r12, rax
00314A36  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
00314A3A  48 83 66 10 00                  and qword ptr [rsi + 0x10], 0
00314A3F  E9 7D FE FF FF                  jmp 0x1403148c1
00314A44  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00314A48  E9 5B FE FF FF                  jmp 0x1403148a8
00314A4D  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00314A51  E9 79 FF FF FF                  jmp 0x1403149cf
00314A56  F6 84 24 A0 00 00 00 02         test byte ptr [rsp + 0xa0], 2
00314A5E  0F 85 83 FE FF FF               jne 0x1403148e7
00314A64  49 8B 6C 24 30                  mov rbp, qword ptr [r12 + 0x30]
00314A69  4D 8B 7C 24 38                  mov r15, qword ptr [r12 + 0x38]
00314A6E  48 2B E9                        sub rbp, rcx
00314A71  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00314A75  48 03 EB                        add rbp, rbx
00314A78  4C 3B F1                        cmp r14, rcx
00314A7B  0F 83 09 C8 3C 00               jae 0x1406e128a
00314A81  49 8B C6                        mov rax, r14
00314A84  48 2B C1                        sub rax, rcx
00314A87  4C 03 F8                        add r15, rax
00314A8A  E9 FB C7 3C 00                  jmp 0x1406e128a
00314A8F  49 8D 55 FF                     lea rdx, [r13 - 1]
00314A93  48 03 D3                        add rdx, rbx
00314A96  E9 80 FE FF FF                  jmp 0x14031491b
00314A9B  49 8B C1                        mov rax, r9
00314A9E  48 2B C3                        sub rax, rbx
00314AA1  48 FF C0                        inc rax
00314AA4  49 89 43 08                     mov qword ptr [r11 + 8], rax
00314AA8  49 8D 41 01                     lea rax, [r9 + 1]
00314AAC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00314AB1  E9 94 FE FF FF                  jmp 0x14031494a
00314AB6  4C 89 66 08                     mov qword ptr [rsi + 8], r12
00314ABA  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
00314ABE  E9 8D FE FF FF                  jmp 0x140314950
00314AC3  48 8B D7                        mov rdx, rdi
00314AC6  49 8B CF                        mov rcx, r15
00314AC9  E8 1E 84 19 00                  call 0x1404aceec
00314ACE  48 89 06                        mov qword ptr [rsi], rax
00314AD1  E9 B0 FE FF FF                  jmp 0x140314986
00314AD6  49 8B 02                        mov rax, qword ptr [r10]
00314AD9  48 3B C1                        cmp rax, rcx
00314ADC  48 89 56 08                     mov qword ptr [rsi + 8], rdx
00314AE0  48 0F 47 C8                     cmova rcx, rax
00314AE4  48 89 4E 10                     mov qword ptr [rsi + 0x10], rcx
00314AE8  E9 A7 FE FF FF                  jmp 0x140314994
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpConvertPortionVpnRangeToGpnRange(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned __int8 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (48);
    v_r12 = 0;
    v_r14 = (*(unsigned __int64 *)(a2 + 8)) - 1;
    v_r14 = (v_r14) + (*(unsigned __int64 *)(a2));
    if (*(unsigned __int64 *)(a4) == 0) goto loc_00314869;
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00314A2E;
    if ((*(unsigned __int64 *)(a2)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 24))) goto loc_003148BB;
loc_00314869:
    if (((*(unsigned __int8 *)(a1 + 24 + 8)) & (1)) != 0) goto loc_00314A00;
loc_0031487A:
    a3 = (unsigned int)((*(unsigned __int8 *)(a1 + 24 + 8)) & (1));
    v_rdi = 0;
loc_00314885:
    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_003149E8;
    if ((*(unsigned __int64 *)(a2)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32))) goto loc_00314A44;
    if ((*(unsigned __int64 *)(a2)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 24))) goto loc_003149B0;
loc_003148A8:
    if ((unsigned int)(a3) == 0) goto loc_003148B6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)) != 0) goto loc_00314A12;
loc_003148B6:
    goto loc_00314885;
loc_003148BB:
    if ((*(unsigned __int64 *)(a2)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32))) goto loc_00314869;
loc_003148C1:
    if ((*(unsigned __int64 *)(a2)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 24))) goto loc_003149F3;
loc_003148CE:
    *(unsigned __int64 *)(a4) = *(unsigned __int64 *)(a1 + 24);
    if (0 == 0) {
        v_r12 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r12 + 64)))) & (1)) != 0) goto loc_00314A56;
loc_003148E7:
    result = (*(unsigned __int64 *)(v_r12 + 48)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 24));
    result = (result) + (*(unsigned __int64 *)(a2));
    *(unsigned __int64 *)(a5) = result;
    result = (v_r14) - (*(unsigned __int64 *)(a2));
    result = (result) + 1;
    if (result > a3) goto loc_00314A8F;
loc_0031491B:
    a3 = 0;
    if (v_r14 >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32))) goto loc_00314A9B;
    result = (v_r14) - (*(unsigned __int64 *)(a2));
    result = (result) + 1;
    *(unsigned __int64 *)(a5 + 8) = result;
    v_stack_m48 = v_r14 + 1;
    if (v_r14 != v_r14) goto loc_00314AB6;
loc_0031494A:
loc_00314950:
    v_r14 = (v_r14) - (v_r14 + 1);
    v_stack_m40 = v_r14 + 1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 24) + 72)))) & (2)) != 0) {
    }
    if (1 == 0) goto loc_00314994;
    if ((*(unsigned __int64 *)(v_r12)) != (*(unsigned __int64 *)(a1 + 24) + 40)) goto loc_00314AD6;
    if (v_r14 + 1 != 0) goto loc_00314AC3;
loc_00314986:
    *(unsigned __int64 *)(v_stack_p10) = v_xmm0;
loc_00314994:
    v_rsp = (v_rsp) + (48);
    return *(unsigned __int64 *)(a2);
loc_003149B0:
    if (1 != 0) goto loc_00314A1A;
loc_003149B5:
    a2 = 0;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_003149E8;
loc_003149BC:
    if (v_stack_p18 > (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 32))) goto loc_00314A4D;
    if (v_stack_p18 >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 24))) goto loc_00314A24;
loc_003149CF:
    if (1 == 0) goto loc_003149D9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) != 0) goto loc_00314A29;
loc_003149D9:
loc_003149DC:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) != 0) goto loc_003149BC;
    v_rdi = *(unsigned __int64 *)(a1 + 24);
    if (0 != 0) { v_rdi = 0; }
loc_003149E8:
    if (v_rdi != 0) goto loc_003148C1;
    goto loc_00314986;
loc_003149F3:
    if (v_r14 < (*(unsigned __int64 *)(*(unsigned __int64 *)(a2)))) goto loc_00314986;
    goto loc_003148CE;
loc_00314A00:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) == 0) goto loc_00314A0D;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2))) ^ (0);
    goto loc_0031487A;
loc_00314A0D:
    goto loc_0031487A;
loc_00314A12:
    a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(a2)));
    goto loc_00314885;
loc_00314A1A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) == 0) goto loc_003149B5;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2))) ^ (a1);
    goto loc_003149B5;
loc_00314A24:
    goto loc_003149CF;
loc_00314A29:
    result = (result) ^ (a1);
    goto loc_003149DC;
loc_00314A2E:
    goto loc_003148C1;
loc_00314A44:
    goto loc_003148A8;
loc_00314A4D:
    goto loc_003149CF;
loc_00314A56:
    if (((a7) & (2)) != 0) goto loc_003148E7;
    v_rbp = (*(unsigned __int64 *)(result + 48)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8));
    v_rbp = (v_rbp) + (*(unsigned __int64 *)(a4 + 16));
    result = (v_r14) - (*(unsigned __int64 *)(v_rdi + 32));
    v_r15 = (*(unsigned __int64 *)(result + 56)) + (result);
loc_00314A8F:
    a2 = (a3 - 1) + (*(unsigned __int64 *)(a4 + 16));
    goto loc_0031491B;
loc_00314A9B:
    result = (v_r14 + 1) - (*(unsigned __int64 *)(a4 + 16));
    result = (result) + 1;
    *(unsigned __int64 *)(a5 + 8) = result;
    v_stack_p20 = v_r14 + 1 + 1;
    goto loc_0031494A;
loc_00314AB6:
    *(unsigned __int64 *)(a4 + 8) = result;
    *(unsigned __int64 *)(a4 + 16) = v_r14 + 1 + 1;
    goto loc_00314950;
loc_00314AC3:
    result = VmpVaMemoryRangeGetNext(v_r15, v_rdi, 1, v_r14 + 1);
    *(unsigned __int64 *)(a4) = result;
    goto loc_00314986;
loc_00314AD6:
    *(unsigned __int64 *)(a4 + 8) = v_rdi;
    a1 = v_r15;
    if ((*(unsigned __int64 *)(a2)) > v_r15) { a1 = *(unsigned __int64 *)(a2); }
    *(unsigned __int64 *)(a4 + 16) = a1;
    goto loc_00314994;
}
```

## 5. (Beta) C Style

```c
int64_t VmpConvertPortionVpnRangeToGpnRange(void *Arg1, void *Arg2, void *Arg3, void *Arg4, void *Arg5, void *Arg6, uint8_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (48);
    local_r12 = 0;
    local_r14 = (*(uint64_t *)(arg2 + 0x8)) - 1;
    local_r14 = (local_r14) + (*(uint64_t *)(arg2));
    if (*(uint64_t *)(arg4) == 0) goto loc_00314869;
    if (*(uint64_t *)(arg4 + 0x8) != 0) goto loc_00314A2E;
    if ((*(uint64_t *)(arg2)) >= (*(uint64_t *)(*(uint64_t *)(arg4) + 0x18))) goto loc_003148BB;
loc_00314869:
    if (((*(uint8_t *)(arg1 + 0x18 + 0x8)) & (1)) != 0) goto loc_00314A00;
loc_0031487A:
    Arg3 = (uint32_t)((*(uint8_t *)(arg1 + 0x18 + 0x8)) & (1));
    local_rdi = 0;
loc_00314885:
    if (*(uint64_t *)(arg1 + 0x18) == 0) goto loc_003149E8;
    if ((*(uint64_t *)(arg2)) > (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20))) goto loc_00314A44;
    if ((*(uint64_t *)(arg2)) >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x18))) goto loc_003149B0;
loc_003148A8:
    if ((uint32_t)(Arg3) == 0) goto loc_003148B6;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)) != 0) goto loc_00314A12;
loc_003148B6:
    goto loc_00314885;
loc_003148BB:
    if ((*(uint64_t *)(arg2)) > (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20))) goto loc_00314869;
loc_003148C1:
    if ((*(uint64_t *)(arg2)) < (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x18))) goto loc_003149F3;
loc_003148CE:
    *(uint64_t *)(arg4) = *(uint64_t *)(arg1 + 0x18);
    if (0 == 0) {
        local_r12 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x40)))) & (1)) != 0) goto loc_00314A56;
loc_003148E7:
    result = (*(uint64_t *)(local_r12 + 0x30)) - (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x18));
    result = (result) + (*(uint64_t *)(arg2));
    *(uint64_t *)(arg5) = result;
    result = (local_r14) - (*(uint64_t *)(arg2));
    result = (result) + 1;
    if (result > Arg3) goto loc_00314A8F;
loc_0031491B:
    Arg3 = 0;
    if (local_r14 >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20))) goto loc_00314A9B;
    result = (local_r14) - (*(uint64_t *)(arg2));
    result = (result) + 1;
    *(uint64_t *)(arg5 + 0x8) = result;
    v_stack_m48 = local_r14 + 1;
    if (local_r14 != local_r14) goto loc_00314AB6;
loc_0031494A:
loc_00314950:
    local_r14 = (local_r14) - (local_r14 + 1);
    v_stack_m40 = local_r14 + 1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x18) + 0x48)))) & (2)) != 0) {
    }
    if (1 == 0) goto loc_00314994;
    if ((*(uint64_t *)(local_r12)) != (*(uint64_t *)(arg1 + 0x18) + 40)) goto loc_00314AD6;
    if (local_r14 + 1 != 0) goto loc_00314AC3;
loc_00314986:
    *(uint64_t *)(v_stack_p10) = v_xmm0;
loc_00314994:
    local_rsp = (local_rsp) + (48);
    return *(uint64_t *)(arg2);
loc_003149B0:
    if (1 != 0) goto loc_00314A1A;
loc_003149B5:
    Arg2 = 0;
    if (*(uint64_t *)(arg2) == 0) goto loc_003149E8;
loc_003149BC:
    if (v_stack_p18 > (*(uint64_t *)(*(uint64_t *)(arg2) + 0x20))) goto loc_00314A4D;
    if (v_stack_p18 >= (*(uint64_t *)(*(uint64_t *)(arg2) + 0x18))) goto loc_00314A24;
loc_003149CF:
    if (1 == 0) goto loc_003149D9;
    if (*(uint64_t *)(*(uint64_t *)(arg2)) != 0) goto loc_00314A29;
loc_003149D9:
loc_003149DC:
    if (*(uint64_t *)(*(uint64_t *)(arg2)) != 0) goto loc_003149BC;
    local_rdi = *(uint64_t *)(arg1 + 0x18);
    if (0 != 0) { local_rdi = 0; }
loc_003149E8:
    if (local_rdi != 0) goto loc_003148C1;
    goto loc_00314986;
loc_003149F3:
    if (local_r14 < (*(uint64_t *)(*(uint64_t *)(arg2)))) goto loc_00314986;
    goto loc_003148CE;
loc_00314A00:
    if (*(uint64_t *)(*(uint64_t *)(arg2)) == 0) goto loc_00314A0D;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg2))) ^ (0);
    goto loc_0031487A;
loc_00314A0D:
    goto loc_0031487A;
loc_00314A12:
    Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(arg2)));
    goto loc_00314885;
loc_00314A1A:
    if (*(uint64_t *)(*(uint64_t *)(arg2)) == 0) goto loc_003149B5;
    result = (*(uint64_t *)(*(uint64_t *)(arg2))) ^ (Arg1);
    goto loc_003149B5;
loc_00314A24:
    goto loc_003149CF;
loc_00314A29:
    result = (result) ^ (Arg1);
    goto loc_003149DC;
loc_00314A2E:
    goto loc_003148C1;
loc_00314A44:
    goto loc_003148A8;
loc_00314A4D:
    goto loc_003149CF;
loc_00314A56:
    if (((Arg7) & (2)) != 0) goto loc_003148E7;
    local_rbp = (*(uint64_t *)(result + 0x30)) - (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8));
    local_rbp = (local_rbp) + (*(uint64_t *)(arg4 + 0x10));
    result = (local_r14) - (*(uint64_t *)(local_rdi + 0x20));
    local_r15 = (*(uint64_t *)(result + 0x38)) + (result);
loc_00314A8F:
    Arg2 = (Arg3 - 1) + (*(uint64_t *)(arg4 + 0x10));
    goto loc_0031491B;
loc_00314A9B:
    result = (local_r14 + 1) - (*(uint64_t *)(arg4 + 0x10));
    result = (result) + 1;
    *(uint64_t *)(arg5 + 0x8) = result;
    v_stack_p20 = local_r14 + 1 + 1;
    goto loc_0031494A;
loc_00314AB6:
    *(uint64_t *)(arg4 + 0x8) = result;
    *(uint64_t *)(arg4 + 0x10) = local_r14 + 1 + 1;
    goto loc_00314950;
loc_00314AC3:
    result = VmpVaMemoryRangeGetNext(local_r15, local_rdi, 1, local_r14 + 1);
    *(uint64_t *)(arg4) = result;
    goto loc_00314986;
loc_00314AD6:
    *(uint64_t *)(arg4 + 0x8) = local_rdi;
    Arg1 = local_r15;
    if ((*(uint64_t *)(arg2)) > local_r15) { Arg1 = *(uint64_t *)(arg2); }
    *(void **)(arg4 + 0x10) = Arg1;
    goto loc_00314994;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg3` | `- 0x1` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R/W` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R/W` |
| `Arg4` | `+ 0x10` | `64` | `W` |
| `Arg5` | `+ 0x0` | `64` | `W` |
| `Arg5` | `+ 0x8` | `64` | `R/W` |
| `Arg5` | `+ 0x8` | `64` | `W` |
| `Arg6` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003147F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
