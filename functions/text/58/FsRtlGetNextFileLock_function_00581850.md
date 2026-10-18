# FsRtlGetNextFileLock

- RVA: `0x00581850`–`0x00581BC1` (길이 `881` bytes)
- VA: `0x0000000140581850`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5D9C`
- 디코드: `242`개 명령, `881/881` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005818C7` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x00581901` → [FsRtlFindFirstOverlappingExclusiveNode](../44/FsRtlFindFirstOverlappingExclusiveNode_function_0044F030.md) (function, `0x0044F030`)
- `0x005819AC` → [RtlRealSuccessor](../38/RtlRealSuccessor_function_0038DF40.md) (function, `0x0038DF40`)
- `0x005819BD` → [RtlRealSuccessor](../38/RtlRealSuccessor_function_0038DF40.md) (function, `0x0038DF40`)
- `0x005819F4` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00581A53` → [FsRtlFindFirstOverlappingSharedNode](../43/FsRtlFindFirstOverlappingSharedNode_function_0043D7E0.md) (function, `0x0043D7E0`)
- `0x00581A74` → [RtlRealSuccessor](../38/RtlRealSuccessor_function_0038DF40.md) (function, `0x0038DF40`)
- `0x00581B01` → [RtlRealSuccessor](../38/RtlRealSuccessor_function_0038DF40.md) (function, `0x0038DF40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00581850  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00581855  55                              push rbp
00581856  56                              push rsi
00581857  57                              push rdi
00581858  41 54                           push r12
0058185A  41 55                           push r13
0058185C  41 56                           push r14
0058185E  41 57                           push r15
00581860  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00581865  48 81 EC A0 00 00 00            sub rsp, 0xa0
0058186C  48 83 65 7F 00                  and qword ptr [rbp + 0x7f], 0
00581871  44 8A F2                        mov r14b, dl
00581874  48 8B 79 18                     mov rdi, qword ptr [rcx + 0x18]
00581878  4C 8B F9                        mov r15, rcx
0058187B  C6 45 67 00                     mov byte ptr [rbp + 0x67], 0
0058187F  48 85 FF                        test rdi, rdi
00581882  0F 84 1B 03 00 00               je 0x140581ba3
00581888  48 8B 59 50                     mov rbx, qword ptr [rcx + 0x50]
0058188C  4C 8D 61 20                     lea r12, [rcx + 0x20]
00581890  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
00581895  48 8D 47 18                     lea rax, [rdi + 0x18]
00581899  40 32 F6                        xor sil, sil
0058189C  48 8B C8                        mov rcx, rax
0058189F  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
005818A3  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
005818A7  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
005818AB  41 0F 10 44 24 10               movups xmm0, xmmword ptr [r12 + 0x10]
005818B1  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
005818B5  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
005818B9  41 0F 10 44 24 20               movups xmm0, xmmword ptr [r12 + 0x20]
005818BF  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
005818C3  0F 11 45 0F                     movups xmmword ptr [rbp + 0xf], xmm0
005818C7  E8 A4 6B C8 FF                  call 0x140208470
005818CC  88 45 77                        mov byte ptr [rbp + 0x77], al
005818CF  45 84 F6                        test r14b, r14b
005818D2  0F 85 5D 02 00 00               jne 0x140581b35
005818D8  0F 10 4D CF                     movups xmm1, xmmword ptr [rbp - 0x31]
005818DC  4C 8D 4D 7F                     lea r9, [rbp + 0x7f]
005818E0  4C 8D 45 17                     lea r8, [rbp + 0x17]
005818E4  66 0F 7E C8                     movd eax, xmm1
005818E8  48 8D 55 EF                     lea rdx, [rbp - 0x11]
005818EC  84 C0                           test al, al
005818EE  48 8D 45 67                     lea rax, [rbp + 0x67]
005818F2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005818F7  0F 84 52 01 00 00               je 0x140581a4f
005818FD  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
00581901  E8 2A D7 EC FF                  call 0x14044f030
00581906  48 85 C0                        test rax, rax
00581909  75 32                           jne 0x14058193d
0058190B  40 38 75 67                     cmp byte ptr [rbp + 0x67], sil
0058190F  74 09                           je 0x14058191a
00581911  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00581915  E9 A8 00 00 00                  jmp 0x1405819c2
0058191A  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
0058191E  48 85 C9                        test rcx, rcx
00581921  0F 85 96 00 00 00               jne 0x1405819bd
00581927  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0058192B  48 85 C0                        test rax, rax
0058192E  0F 84 B5 00 00 00               je 0x1405819e9
00581934  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00581938  E9 F3 00 00 00                  jmp 0x140581a30
0058193D  4C 8B 65 DF                     mov r12, qword ptr [rbp - 0x21]
00581941  66 0F 6F C1                     movdqa xmm0, xmm1
00581945  66 0F 73 D8 08                  psrldq xmm0, 8
0058194A  66 0F 73 D9 04                  psrldq xmm1, 4
0058194F  66 49 0F 7E C5                  movq r13, xmm0
00581954  66 0F 7E C9                     movd ecx, xmm1
00581958  0F 10 4D BF                     movups xmm1, xmmword ptr [rbp - 0x41]
0058195C  89 4D 67                        mov dword ptr [rbp + 0x67], ecx
0058195F  66 0F 6F C1                     movdqa xmm0, xmm1
00581963  66 48 0F 7E CA                  movq rdx, xmm1
00581968  66 0F 73 D8 08                  psrldq xmm0, 8
0058196D  66 49 0F 7E C6                  movq r14, xmm0
00581972  48 89 55 7F                     mov qword ptr [rbp + 0x7f], rdx
00581976  48 85 C0                        test rax, rax
00581979  74 AC                           je 0x140581927
0058197B  48 3B D8                        cmp rbx, rax
0058197E  75 1D                           jne 0x14058199d
00581980  48 3B 50 18                     cmp rdx, qword ptr [rax + 0x18]
00581984  75 17                           jne 0x14058199d
00581986  4C 3B 70 20                     cmp r14, qword ptr [rax + 0x20]
0058198A  75 11                           jne 0x14058199d
0058198C  3B 48 2C                        cmp ecx, dword ptr [rax + 0x2c]
0058198F  75 0C                           jne 0x14058199d
00581991  4C 3B 68 30                     cmp r13, qword ptr [rax + 0x30]
00581995  75 06                           jne 0x14058199d
00581997  4C 3B 60 38                     cmp r12, qword ptr [rax + 0x38]
0058199B  74 1D                           je 0x1405819ba
0058199D  48 83 78 20 00                  cmp qword ptr [rax + 0x20], 0
005819A2  75 27                           jne 0x1405819cb
005819A4  4D 85 F6                        test r14, r14
005819A7  75 22                           jne 0x1405819cb
005819A9  48 8B C8                        mov rcx, rax
005819AC  E8 8F C5 E0 FF                  call 0x14038df40
005819B1  8B 4D 67                        mov ecx, dword ptr [rbp + 0x67]
005819B4  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
005819B8  EB BC                           jmp 0x140581976
005819BA  48 8B C8                        mov rcx, rax
005819BD  E8 7E C5 E0 FF                  call 0x14038df40
005819C2  48 85 C0                        test rax, rax
005819C5  0F 84 5C FF FF FF               je 0x140581927
005819CB  0F 10 40 18                     movups xmm0, xmmword ptr [rax + 0x18]
005819CF  48 8B D8                        mov rbx, rax
005819D2  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
005819D6  0F 10 40 28                     movups xmm0, xmmword ptr [rax + 0x28]
005819DA  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
005819DE  0F 10 40 38                     movups xmm0, xmmword ptr [rax + 0x38]
005819E2  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
005819E6  40 B6 01                        mov sil, 1
005819E9  4D 8D 67 20                     lea r12, [r15 + 0x20]
005819ED  8A 55 77                        mov dl, byte ptr [rbp + 0x77]
005819F0  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
005819F4  E8 A7 11 E1 FF                  call 0x140392ba0
005819F9  40 84 F6                        test sil, sil
005819FC  0F 84 A1 01 00 00               je 0x140581ba3
00581A02  0F 10 45 BF                     movups xmm0, xmmword ptr [rbp - 0x41]
00581A06  49 89 5F 50                     mov qword ptr [r15 + 0x50], rbx
00581A0A  49 8B C4                        mov rax, r12
00581A0D  41 0F 11 47 20                  movups xmmword ptr [r15 + 0x20], xmm0
00581A12  0F 10 45 CF                     movups xmm0, xmmword ptr [rbp - 0x31]
00581A16  41 0F 11 47 30                  movups xmmword ptr [r15 + 0x30], xmm0
00581A1B  0F 10 45 DF                     movups xmm0, xmmword ptr [rbp - 0x21]
00581A1F  41 0F 11 47 40                  movups xmmword ptr [r15 + 0x40], xmm0
00581A24  E9 7C 01 00 00                  jmp 0x140581ba5
00581A29  48 8B C1                        mov rax, rcx
00581A2C  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00581A30  48 85 C9                        test rcx, rcx
00581A33  75 F4                           jne 0x140581a29
00581A35  48 8B 58 E8                     mov rbx, qword ptr [rax - 0x18]
00581A39  0F 10 43 08                     movups xmm0, xmmword ptr [rbx + 8]
00581A3D  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00581A41  0F 10 43 18                     movups xmm0, xmmword ptr [rbx + 0x18]
00581A45  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
00581A49  0F 10 43 28                     movups xmm0, xmmword ptr [rbx + 0x28]
00581A4D  EB 93                           jmp 0x1405819e2
00581A4F  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00581A53  E8 88 BD EB FF                  call 0x14043d7e0
00581A58  48 8B C8                        mov rcx, rax
00581A5B  48 85 C0                        test rax, rax
00581A5E  75 29                           jne 0x140581a89
00581A60  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00581A64  48 85 C9                        test rcx, rcx
00581A67  74 84                           je 0x1405819ed
00581A69  40 38 75 67                     cmp byte ptr [rbp + 0x67], sil
00581A6D  74 05                           je 0x140581a74
00581A6F  48 8B C1                        mov rax, rcx
00581A72  EB 15                           jmp 0x140581a89
00581A74  E8 C7 C4 E0 FF                  call 0x14038df40
00581A79  48 8B C8                        mov rcx, rax
00581A7C  48 85 C0                        test rax, rax
00581A7F  0F 84 68 FF FF FF               je 0x1405819ed
00581A85  0F 10 4D CF                     movups xmm1, xmmword ptr [rbp - 0x31]
00581A89  48 83 C0 E8                     add rax, -0x18
00581A8D  0F 84 5A FF FF FF               je 0x1405819ed
00581A93  4C 8B 45 DF                     mov r8, qword ptr [rbp - 0x21]
00581A97  66 0F 6F C1                     movdqa xmm0, xmm1
00581A9B  66 0F 73 D8 08                  psrldq xmm0, 8
00581AA0  66 0F 73 D9 04                  psrldq xmm1, 4
00581AA5  66 49 0F 7E C1                  movq r9, xmm0
00581AAA  66 41 0F 7E CA                  movd r10d, xmm1
00581AAF  0F 10 4D BF                     movups xmm1, xmmword ptr [rbp - 0x41]
00581AB3  66 0F 6F C1                     movdqa xmm0, xmm1
00581AB7  66 48 0F 7E CA                  movq rdx, xmm1
00581ABC  66 0F 73 D8 08                  psrldq xmm0, 8
00581AC1  66 49 0F 7E C3                  movq r11, xmm0
00581AC6  48 8B 00                        mov rax, qword ptr [rax]
00581AC9  48 85 C0                        test rax, rax
00581ACC  74 33                           je 0x140581b01
00581ACE  48 3B D8                        cmp rbx, rax
00581AD1  75 1E                           jne 0x140581af1
00581AD3  48 3B 50 08                     cmp rdx, qword ptr [rax + 8]
00581AD7  75 1C                           jne 0x140581af5
00581AD9  4C 3B 58 10                     cmp r11, qword ptr [rax + 0x10]
00581ADD  75 12                           jne 0x140581af1
00581ADF  44 3B 50 1C                     cmp r10d, dword ptr [rax + 0x1c]
00581AE3  75 0C                           jne 0x140581af1
00581AE5  4C 3B 48 20                     cmp r9, qword ptr [rax + 0x20]
00581AE9  75 06                           jne 0x140581af1
00581AEB  4C 3B 40 28                     cmp r8, qword ptr [rax + 0x28]
00581AEF  74 08                           je 0x140581af9
00581AF1  48 3B 50 08                     cmp rdx, qword ptr [rax + 8]
00581AF5  72 25                           jb 0x140581b1c
00581AF7  EB CD                           jmp 0x140581ac6
00581AF9  48 8B 00                        mov rax, qword ptr [rax]
00581AFC  48 85 C0                        test rax, rax
00581AFF  75 1B                           jne 0x140581b1c
00581B01  E8 3A C4 E0 FF                  call 0x14038df40
00581B06  48 85 C0                        test rax, rax
00581B09  0F 84 DE FE FF FF               je 0x1405819ed
00581B0F  48 8B 40 E8                     mov rax, qword ptr [rax - 0x18]
00581B13  48 85 C0                        test rax, rax
00581B16  0F 84 D1 FE FF FF               je 0x1405819ed
00581B1C  0F 10 40 08                     movups xmm0, xmmword ptr [rax + 8]
00581B20  48 8B D8                        mov rbx, rax
00581B23  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00581B27  0F 10 40 18                     movups xmm0, xmmword ptr [rax + 0x18]
00581B2B  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
00581B2F  0F 10 40 28                     movups xmm0, xmmword ptr [rax + 0x28]
00581B33  EB 29                           jmp 0x140581b5e
00581B35  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00581B39  48 85 C0                        test rax, rax
00581B3C  74 2C                           je 0x140581b6a
00581B3E  48 8B D8                        mov rbx, rax
00581B41  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00581B45  48 85 C0                        test rax, rax
00581B48  75 F4                           jne 0x140581b3e
00581B4A  0F 10 43 18                     movups xmm0, xmmword ptr [rbx + 0x18]
00581B4E  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00581B52  0F 10 43 28                     movups xmm0, xmmword ptr [rbx + 0x28]
00581B56  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
00581B5A  0F 10 43 38                     movups xmm0, xmmword ptr [rbx + 0x38]
00581B5E  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
00581B62  40 B6 01                        mov sil, 1
00581B65  E9 83 FE FF FF                  jmp 0x1405819ed
00581B6A  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00581B6E  48 85 C0                        test rax, rax
00581B71  0F 84 76 FE FF FF               je 0x1405819ed
00581B77  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00581B7B  EB 07                           jmp 0x140581b84
00581B7D  48 8B C1                        mov rax, rcx
00581B80  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00581B84  48 85 C9                        test rcx, rcx
00581B87  75 F4                           jne 0x140581b7d
00581B89  48 8B 58 E8                     mov rbx, qword ptr [rax - 0x18]
00581B8D  0F 10 43 08                     movups xmm0, xmmword ptr [rbx + 8]
00581B91  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00581B95  0F 10 43 18                     movups xmm0, xmmword ptr [rbx + 0x18]
00581B99  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
00581B9D  0F 10 43 28                     movups xmm0, xmmword ptr [rbx + 0x28]
00581BA1  EB BB                           jmp 0x140581b5e
00581BA3  33 C0                           xor eax, eax
00581BA5  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00581BAD  48 81 C4 A0 00 00 00            add rsp, 0xa0
00581BB4  41 5F                           pop r15
00581BB6  41 5E                           pop r14
00581BB8  41 5D                           pop r13
00581BBA  41 5C                           pop r12
00581BBC  5F                              pop rdi
00581BBD  5E                              pop rsi
00581BBE  5D                              pop rbp
00581BBF  C3                              ret
00581BC0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlGetNextFileLock(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (160);
    v_stack_p8 = 0;
    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_00581BA3;
    v_rsi = 0;
    v_stack_mA8 = *(unsigned __int64 *)(a1 + 24) + 24;
    v_stack_mA0 = v_xmm0;
    v_stack_m70 = v_xmm0;
    v_stack_m90 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(a1 + 24) + 24, a2, a3, a4);
    v_stack_p18 = (unsigned __int8)(result);
    if (a2 != 0) goto loc_00581B35;
    v_stack_mB8 = v_stack_p8;
    if ((unsigned __int8)(result) == 0) goto loc_00581A4F;
    result = FsRtlFindFirstOverlappingExclusiveNode(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40), v_stack_m70, v_stack_m48, v_stack_p20);
    if (result != 0) goto loc_0058193D;
    if (v_stack_p8 == 0) goto loc_0058191A;
    goto loc_005819C2;
loc_0058191A:
    if (v_stack_p20 != 0) goto loc_005819BD;
loc_00581927:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) == 0) goto loc_005819E9;
    goto loc_00581A30;
loc_0058193D:
    v_stack_p8 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 8));
    v_stack_p20 = v_stack_m70;
loc_00581976:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) == 0) goto loc_00581927;
    if ((*(unsigned __int64 *)(a1 + 80)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32))) goto loc_0058199D;
    if (v_stack_m70 != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 24))) goto loc_0058199D;
    if (a2 != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 32))) goto loc_0058199D;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 8))) != (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 44))) goto loc_0058199D;
    if (v_r13 != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 48))) goto loc_0058199D;
    if (v_stack_m80 == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 56))) goto loc_005819BA;
loc_0058199D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 32)) != 0) goto loc_005819CB;
    if (a2 != 0) goto loc_005819CB;
    result = RtlRealSuccessor(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32), v_stack_m70, v_stack_m48, v_stack_p20);
    goto loc_00581976;
loc_005819BA:
loc_005819BD:
    result = RtlRealSuccessor(result, v_stack_p20, v_stack_m48, v_stack_p20);
loc_005819C2:
    if (result == 0) goto loc_00581927;
loc_005819CB:
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
loc_005819E2:
    v_stack_m80 = v_xmm0;
loc_005819E9:
loc_005819ED:
    result = KeReleaseSpinLock(v_stack_mA8, v_stack_p18, v_stack_m48, v_stack_p20);
    if (1 == 0) goto loc_00581BA3;
    *(unsigned __int64 *)(a1 + 80) = result;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + 48) = v_xmm0;
    *(unsigned __int64 *)(a1 + 64) = v_xmm0;
    goto loc_00581BA5;
loc_00581A29:
loc_00581A30:
    if (*(unsigned __int64 *)(v_stack_mA8 + 8) != 0) goto loc_00581A29;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    goto loc_005819E2;
loc_00581A4F:
    result = FsRtlFindFirstOverlappingSharedNode(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32), v_stack_p18, v_stack_m48, v_stack_p20);
    if (result != 0) goto loc_00581A89;
    if (v_stack_p20 == 0) goto loc_005819ED;
    if (v_stack_p8 == 1) goto loc_00581A74;
    goto loc_00581A89;
loc_00581A74:
    result = RtlRealSuccessor(v_stack_p20, v_stack_p18, v_stack_m48, v_stack_p20);
    if (result == 0) goto loc_005819ED;
loc_00581A89:
    result = (result) + (-24);
    if (condition_is_equal) goto loc_005819ED;
loc_00581AC6:
    if (*(unsigned __int64 *)(result) == 0) goto loc_00581B01;
    if ((*(unsigned __int64 *)(v_stack_mA8 - 24)) != (*(unsigned __int64 *)(result))) goto loc_00581AF1;
    if (v_stack_p18 != (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8))) goto loc_00581AF5;
    if (v_r11 != (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 16))) goto loc_00581AF1;
    if (((unsigned int)(v_r10)) != (*(unsigned int *)(*(unsigned __int64 *)(result) + 28))) goto loc_00581AF1;
    if (v_stack_p20 != (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 32))) goto loc_00581AF1;
    if (v_stack_m80 == (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 40))) goto loc_00581AF9;
loc_00581AF1:
loc_00581AF5:
    if (v_stack_p18 < (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8))) goto loc_00581B1C;
    goto loc_00581AC6;
loc_00581AF9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result)) != 0) goto loc_00581B1C;
loc_00581B01:
    result = RtlRealSuccessor(result, v_stack_p18, v_stack_m80, v_stack_p20);
    if (result == 0) goto loc_005819ED;
    if (*(unsigned __int64 *)(result - 24) == 0) goto loc_005819ED;
loc_00581B1C:
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    goto loc_00581B5E;
loc_00581B35:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40) == 0) goto loc_00581B6A;
loc_00581B3E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 40) + 8) != 0) goto loc_00581B3E;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
loc_00581B5E:
    v_stack_m80 = v_xmm0;
    goto loc_005819ED;
loc_00581B6A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) == 0) goto loc_005819ED;
    goto loc_00581B84;
loc_00581B7D:
loc_00581B84:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 32) + 8) + 8) != 0) goto loc_00581B7D;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    goto loc_00581B5E;
loc_00581BA3:
    result = 0;
loc_00581BA5:
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlGetNextFileLock(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (160);
    v_stack_p8 = 0;
    if (*(uint64_t *)(arg1 + 0x18) == 0) goto loc_00581BA3;
    local_rsi = 0;
    v_stack_mA8 = *(uint64_t *)(arg1 + 0x18) + 24;
    v_stack_mA0 = v_xmm0;
    v_stack_m70 = v_xmm0;
    v_stack_m90 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m80 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(arg1 + 0x18) + 24, Arg2, a3, a4);
    v_stack_p18 = (uint8_t)(result);
    if (Arg2 != 0) goto loc_00581B35;
    v_stack_mB8 = v_stack_p8;
    if ((uint8_t)(result) == 0) goto loc_00581A4F;
    result = FsRtlFindFirstOverlappingExclusiveNode(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28), v_stack_m70, v_stack_m48, v_stack_p20);
    if (result != 0) goto loc_0058193D;
    if (v_stack_p8 == 0) goto loc_0058191A;
    goto loc_005819C2;
loc_0058191A:
    if (v_stack_p20 != 0) goto loc_005819BD;
loc_00581927:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) == 0) goto loc_005819E9;
    goto loc_00581A30;
loc_0058193D:
    v_stack_p8 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x8));
    v_stack_p20 = v_stack_m70;
loc_00581976:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) == 0) goto loc_00581927;
    if ((*(uint64_t *)(arg1 + 0x50)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20))) goto loc_0058199D;
    if (v_stack_m70 != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x18))) goto loc_0058199D;
    if (Arg2 != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x20))) goto loc_0058199D;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x8))) != (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x2C))) goto loc_0058199D;
    if (local_r13 != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x30))) goto loc_0058199D;
    if (v_stack_m80 == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x38))) goto loc_005819BA;
loc_0058199D:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x20)) != 0) goto loc_005819CB;
    if (Arg2 != 0) goto loc_005819CB;
    result = RtlRealSuccessor(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20), v_stack_m70, v_stack_m48, v_stack_p20);
    goto loc_00581976;
loc_005819BA:
loc_005819BD:
    result = RtlRealSuccessor(result, v_stack_p20, v_stack_m48, v_stack_p20);
loc_005819C2:
    if (result == 0) goto loc_00581927;
loc_005819CB:
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
loc_005819E2:
    v_stack_m80 = v_xmm0;
loc_005819E9:
loc_005819ED:
    result = KeReleaseSpinLock(v_stack_mA8, v_stack_p18, v_stack_m48, v_stack_p20);
    if (1 == 0) goto loc_00581BA3;
    *(uint64_t *)(arg1 + 0x50) = result;
    *(uint64_t *)(arg1 + 0x20) = v_xmm0;
    *(uint64_t *)(arg1 + 0x30) = v_xmm0;
    *(uint64_t *)(arg1 + 0x40) = v_xmm0;
    goto loc_00581BA5;
loc_00581A29:
loc_00581A30:
    if (*(uint64_t *)(v_stack_mA8 + 0x8) != 0) goto loc_00581A29;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    goto loc_005819E2;
loc_00581A4F:
    result = FsRtlFindFirstOverlappingSharedNode(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20), v_stack_p18, v_stack_m48, v_stack_p20);
    if (result != 0) goto loc_00581A89;
    if (v_stack_p20 == 0) goto loc_005819ED;
    if (v_stack_p8 == 1) goto loc_00581A74;
    goto loc_00581A89;
loc_00581A74:
    result = RtlRealSuccessor(v_stack_p20, v_stack_p18, v_stack_m48, v_stack_p20);
    if (result == 0) goto loc_005819ED;
loc_00581A89:
    result = (result) + (-24);
    if (condition_is_equal) goto loc_005819ED;
loc_00581AC6:
    if (*(uint64_t *)(result) == 0) goto loc_00581B01;
    if ((*(uint64_t *)(v_stack_mA8 - 0x18)) != (*(uint64_t *)(result))) goto loc_00581AF1;
    if (v_stack_p18 != (*(uint64_t *)(*(uint64_t *)(result) + 0x8))) goto loc_00581AF5;
    if (local_r11 != (*(uint64_t *)(*(uint64_t *)(result) + 0x10))) goto loc_00581AF1;
    if (((uint32_t)(local_r10)) != (*(uint32_t *)(*(uint64_t *)(result) + 0x1C))) goto loc_00581AF1;
    if (v_stack_p20 != (*(uint64_t *)(*(uint64_t *)(result) + 0x20))) goto loc_00581AF1;
    if (v_stack_m80 == (*(uint64_t *)(*(uint64_t *)(result) + 0x28))) goto loc_00581AF9;
loc_00581AF1:
loc_00581AF5:
    if (v_stack_p18 < (*(uint64_t *)(*(uint64_t *)(result) + 0x8))) goto loc_00581B1C;
    goto loc_00581AC6;
loc_00581AF9:
    if (*(uint64_t *)(*(uint64_t *)(result)) != 0) goto loc_00581B1C;
loc_00581B01:
    result = RtlRealSuccessor(result, v_stack_p18, v_stack_m80, v_stack_p20);
    if (result == 0) goto loc_005819ED;
    if (*(uint64_t *)(result - 0x18) == 0) goto loc_005819ED;
loc_00581B1C:
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    goto loc_00581B5E;
loc_00581B35:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28) == 0) goto loc_00581B6A;
loc_00581B3E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x28) + 0x8) != 0) goto loc_00581B3E;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
loc_00581B5E:
    v_stack_m80 = v_xmm0;
    goto loc_005819ED;
loc_00581B6A:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) == 0) goto loc_005819ED;
    goto loc_00581B84;
loc_00581B7D:
loc_00581B84:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x20) + 0x8) + 0x8) != 0) goto loc_00581B7D;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    goto loc_00581B5E;
loc_00581BA3:
    result = 0;
loc_00581BA5:
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `128` | `R` |
| `Arg1` | `+ 0x30` | `128` | `R` |
| `Arg1` | `+ 0x40` | `128` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00581850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
