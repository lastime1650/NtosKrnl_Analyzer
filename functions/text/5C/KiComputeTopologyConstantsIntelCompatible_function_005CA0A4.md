# KiComputeTopologyConstantsIntelCompatible

- RVA: `0x005CA0A4`–`0x005CA457` (길이 `947` bytes)
- VA: `0x00000001405CA0A4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB250`
- 디코드: `307`개 명령, `947/947` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005CA26F` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (function, `0x004F40E0`)
- `0x005CA27D` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (function, `0x004F40E0`)
- `0x005CA389` → [Feature_PpmParkEx__private_IsEnabledNoReportingNoInline](../4F/Feature_PpmParkEx__private_IsEnabledNoReportingNoInline_function_004F40E0.md) (function, `0x004F40E0`)
- `0x005CA439` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KiComputeTopologyConstants](KiComputeTopologyConstants_function_005C9CB8.md) at `0x005C9D22`

### Static image references
- `0x005CA0BB` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CA0A4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005CA0A9  55                              push rbp
005CA0AA  56                              push rsi
005CA0AB  57                              push rdi
005CA0AC  41 54                           push r12
005CA0AE  41 55                           push r13
005CA0B0  41 56                           push r14
005CA0B2  41 57                           push r15
005CA0B4  48 8B EC                        mov rbp, rsp
005CA0B7  48 83 EC 60                     sub rsp, 0x60
005CA0BB  48 8B 05 7E 06 84 00            mov rax, qword ptr [rip + 0x84067e]
005CA0C2  48 33 C4                        xor rax, rsp
005CA0C5  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
005CA0C9  33 C0                           xor eax, eax
005CA0CB  4D 8B E0                        mov r12, r8
005CA0CE  0F 57 C0                        xorps xmm0, xmm0
005CA0D1  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
005CA0D5  49 8B F9                        mov rdi, r9
005CA0D8  44 8B FA                        mov r15d, edx
005CA0DB  44 8B E9                        mov r13d, ecx
005CA0DE  44 8D 40 1F                     lea r8d, [rax + 0x1f]
005CA0E2  8D 70 01                        lea esi, [rax + 1]
005CA0E5  44 8D 70 04                     lea r14d, [rax + 4]
005CA0E9  44 8D 50 0B                     lea r10d, [rax + 0xb]
005CA0ED  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
005CA0F1  41 3B D0                        cmp edx, r8d
005CA0F4  72 10                           jb 0x1405ca106
005CA0F6  33 C9                           xor ecx, ecx
005CA0F8  41 8B C0                        mov eax, r8d
005CA0FB  0F A2                           cpuid
005CA0FD  85 DB                           test ebx, ebx
005CA0FF  74 0E                           je 0x1405ca10f
005CA101  45 8B D0                        mov r10d, r8d
005CA104  EB 18                           jmp 0x1405ca11e
005CA106  45 3B FA                        cmp r15d, r10d
005CA109  0F 82 05 01 00 00               jb 0x1405ca214
005CA10F  33 C9                           xor ecx, ecx
005CA111  41 8B C2                        mov eax, r10d
005CA114  0F A2                           cpuid
005CA116  85 DB                           test ebx, ebx
005CA118  0F 84 FB 00 00 00               je 0x1405ca219
005CA11E  41 83 09 10                     or dword ptr [r9], 0x10
005CA122  45 33 DB                        xor r11d, r11d
005CA125  41 89 51 18                     mov dword ptr [r9 + 0x18], edx
005CA129  45 33 C9                        xor r9d, r9d
005CA12C  41 8B CB                        mov ecx, r11d
005CA12F  41 8B C2                        mov eax, r10d
005CA132  0F A2                           cpuid
005CA134  C1 E9 08                        shr ecx, 8
005CA137  44 03 DE                        add r11d, esi
005CA13A  44 8B C0                        mov r8d, eax
005CA13D  0F B6 C1                        movzx eax, cl
005CA140  84 C9                           test cl, cl
005CA142  0F 84 AF 00 00 00               je 0x1405ca1f7
005CA148  2B C6                           sub eax, esi
005CA14A  0F 84 91 00 00 00               je 0x1405ca1e1
005CA150  2B C6                           sub eax, esi
005CA152  74 77                           je 0x1405ca1cb
005CA154  2B C6                           sub eax, esi
005CA156  74 50                           je 0x1405ca1a8
005CA158  2B C6                           sub eax, esi
005CA15A  74 39                           je 0x1405ca195
005CA15C  41 83 E0 1F                     and r8d, 0x1f
005CA160  3B C6                           cmp eax, esi
005CA162  41 8A C8                        mov cl, r8b
005CA165  41 8B C1                        mov eax, r9d
005CA168  74 0D                           je 0x1405ca177
005CA16A  8B D6                           mov edx, esi
005CA16C  D3 E2                           shl edx, cl
005CA16E  89 54 85 D8                     mov dword ptr [rbp + rax*4 - 0x28], edx
005CA172  E9 80 00 00 00                  jmp 0x1405ca1f7
005CA177  8B 44 85 D8                     mov eax, dword ptr [rbp + rax*4 - 0x28]
005CA17B  33 D2                           xor edx, edx
005CA17D  F7 77 08                        div dword ptr [rdi + 8]
005CA180  44 09 37                        or dword ptr [rdi], r14d
005CA183  41 B9 05 00 00 00               mov r9d, 5
005CA189  89 47 10                        mov dword ptr [rdi + 0x10], eax
005CA18C  8B C6                           mov eax, esi
005CA18E  D3 E0                           shl eax, cl
005CA190  89 45 EC                        mov dword ptr [rbp - 0x14], eax
005CA193  EB 62                           jmp 0x1405ca1f7
005CA195  41 83 E0 1F                     and r8d, 0x1f
005CA199  8B C6                           mov eax, esi
005CA19B  41 8A C8                        mov cl, r8b
005CA19E  45 8B CE                        mov r9d, r14d
005CA1A1  D3 E0                           shl eax, cl
005CA1A3  89 45 E8                        mov dword ptr [rbp - 0x18], eax
005CA1A6  EB 4F                           jmp 0x1405ca1f7
005CA1A8  83 0F 08                        or dword ptr [rdi], 8
005CA1AB  41 83 E0 1F                     and r8d, 0x1f
005CA1AF  41 8B C1                        mov eax, r9d
005CA1B2  41 B9 03 00 00 00               mov r9d, 3
005CA1B8  8B 4C 85 D8                     mov ecx, dword ptr [rbp + rax*4 - 0x28]
005CA1BC  8B C6                           mov eax, esi
005CA1BE  89 4F 14                        mov dword ptr [rdi + 0x14], ecx
005CA1C1  41 8A C8                        mov cl, r8b
005CA1C4  D3 E0                           shl eax, cl
005CA1C6  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
005CA1C9  EB 2C                           jmp 0x1405ca1f7
005CA1CB  41 83 E0 1F                     and r8d, 0x1f
005CA1CF  8B C6                           mov eax, esi
005CA1D1  41 8A C8                        mov cl, r8b
005CA1D4  41 B9 02 00 00 00               mov r9d, 2
005CA1DA  D3 E0                           shl eax, cl
005CA1DC  89 45 E0                        mov dword ptr [rbp - 0x20], eax
005CA1DF  EB 16                           jmp 0x1405ca1f7
005CA1E1  41 83 E0 1F                     and r8d, 0x1f
005CA1E5  8B C6                           mov eax, esi
005CA1E7  41 8A C8                        mov cl, r8b
005CA1EA  44 8B CE                        mov r9d, esi
005CA1ED  D3 E0                           shl eax, cl
005CA1EF  09 37                           or dword ptr [rdi], esi
005CA1F1  89 47 08                        mov dword ptr [rdi + 8], eax
005CA1F4  89 45 DC                        mov dword ptr [rbp - 0x24], eax
005CA1F7  66 85 DB                        test bx, bx
005CA1FA  0F 85 2C FF FF FF               jne 0x1405ca12c
005CA200  33 D2                           xor edx, edx
005CA202  41 8B C1                        mov eax, r9d
005CA205  8B 44 85 D8                     mov eax, dword ptr [rbp + rax*4 - 0x28]
005CA209  F7 77 08                        div dword ptr [rdi + 8]
005CA20C  83 0F 02                        or dword ptr [rdi], 2
005CA20F  89 47 0C                        mov dword ptr [rdi + 0xc], eax
005CA212  EB 69                           jmp 0x1405ca27d
005CA214  45 3B FE                        cmp r15d, r14d
005CA217  72 24                           jb 0x1405ca23d
005CA219  83 65 C0 00                     and dword ptr [rbp - 0x40], 0
005CA21D  33 C9                           xor ecx, ecx
005CA21F  41 8B C6                        mov eax, r14d
005CA222  0F A2                           cpuid
005CA224  C1 E8 1A                        shr eax, 0x1a
005CA227  8D 04 45 01 00 00 00            lea eax, [rax*2 + 1]
005CA22E  0F BD C8                        bsr ecx, eax
005CA231  8B C6                           mov eax, esi
005CA233  D3 E0                           shl eax, cl
005CA235  41 83 09 02                     or dword ptr [r9], 2
005CA239  41 89 41 0C                     mov dword ptr [r9 + 0xc], eax
005CA23D  41 F7 44 24 0C 00 00 00 10      test dword ptr [r12 + 0xc], 0x10000000
005CA246  74 27                           je 0x1405ca26f
005CA248  41 0F B6 44 24 06               movzx eax, byte ptr [r12 + 6]
005CA24E  33 D2                           xor edx, edx
005CA250  83 65 C0 00                     and dword ptr [rbp - 0x40], 0
005CA254  8D 04 45 FF FF FF FF            lea eax, [rax*2 - 1]
005CA25B  0F BD C8                        bsr ecx, eax
005CA25E  8B C6                           mov eax, esi
005CA260  D3 E0                           shl eax, cl
005CA262  41 F7 71 0C                     div dword ptr [r9 + 0xc]
005CA266  41 09 31                        or dword ptr [r9], esi
005CA269  41 89 41 08                     mov dword ptr [r9 + 8], eax
005CA26D  EB 0E                           jmp 0x1405ca27d
005CA26F  E8 6C 9E F2 FF                  call 0x1404f40e0
005CA274  85 C0                           test eax, eax
005CA276  74 05                           je 0x1405ca27d
005CA278  09 37                           or dword ptr [rdi], esi
005CA27A  89 77 08                        mov dword ptr [rdi + 8], esi
005CA27D  E8 5E 9E F2 FF                  call 0x1404f40e0
005CA282  85 C0                           test eax, eax
005CA284  0F 84 9D 00 00 00               je 0x1405ca327
005CA28A  41 83 FD 02                     cmp r13d, 2
005CA28E  0F 85 93 00 00 00               jne 0x1405ca327
005CA294  44 8B 0F                        mov r9d, dword ptr [rdi]
005CA297  45 84 CE                        test r14b, r9b
005CA29A  0F 85 87 00 00 00               jne 0x1405ca327
005CA2A0  41 8B 04 24                     mov eax, dword ptr [r12]
005CA2A4  8B D8                           mov ebx, eax
005CA2A6  C1 EB 08                        shr ebx, 8
005CA2A9  44 8B C3                        mov r8d, ebx
005CA2AC  41 83 E0 0F                     and r8d, 0xf
005CA2B0  41 83 F8 0F                     cmp r8d, 0xf
005CA2B4  75 22                           jne 0x1405ca2d8
005CA2B6  81 E3 00 0F 00 00               and ebx, 0xf00
005CA2BC  8B C8                           mov ecx, eax
005CA2BE  C1 E9 14                        shr ecx, 0x14
005CA2C1  25 F0 00 00 00                  and eax, 0xf0
005CA2C6  0B D8                           or ebx, eax
005CA2C8  0F B6 D1                        movzx edx, cl
005CA2CB  41 03 D0                        add edx, r8d
005CA2CE  C1 EB 04                        shr ebx, 4
005CA2D1  83 FA 06                        cmp edx, 6
005CA2D4  75 51                           jne 0x1405ca327
005CA2D6  EB 16                           jmp 0x1405ca2ee
005CA2D8  41 83 F8 06                     cmp r8d, 6
005CA2DC  75 49                           jne 0x1405ca327
005CA2DE  81 E3 00 0F 00 00               and ebx, 0xf00
005CA2E4  25 F0 00 00 00                  and eax, 0xf0
005CA2E9  0B D8                           or ebx, eax
005CA2EB  C1 EB 04                        shr ebx, 4
005CA2EE  81 FB AD 00 00 00               cmp ebx, 0xad
005CA2F4  75 31                           jne 0x1405ca327
005CA2F6  B9 17 00 00 00                  mov ecx, 0x17
005CA2FB  0F 32                           rdmsr
005CA2FD  48 C1 E2 20                     shl rdx, 0x20
005CA301  48 0B C2                        or rax, rdx
005CA304  48 C1 E8 32                     shr rax, 0x32
005CA308  24 07                           and al, 7
005CA30A  40 3A C6                        cmp al, sil
005CA30D  75 18                           jne 0x1405ca327
005CA30F  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
005CA312  45 0B CE                        or r9d, r14d
005CA315  C7 47 10 40 00 00 00            mov dword ptr [rdi + 0x10], 0x40
005CA31C  44 89 0F                        mov dword ptr [rdi], r9d
005CA31F  83 F8 40                        cmp eax, 0x40
005CA322  73 03                           jae 0x1405ca327
005CA324  89 47 10                        mov dword ptr [rdi + 0x10], eax
005CA327  8B 07                           mov eax, dword ptr [rdi]
005CA329  41 BC FF 0F 00 00               mov r12d, 0xfff
005CA32F  A8 08                           test al, 8
005CA331  75 56                           jne 0x1405ca389
005CA333  41 83 FD 02                     cmp r13d, 2
005CA337  75 50                           jne 0x1405ca389
005CA339  45 3B FE                        cmp r15d, r14d
005CA33C  72 4B                           jb 0x1405ca389
005CA33E  45 33 C9                        xor r9d, r9d
005CA341  41 8B C6                        mov eax, r14d
005CA344  41 8B C9                        mov ecx, r9d
005CA347  0F A2                           cpuid
005CA349  44 8B C0                        mov r8d, eax
005CA34C  C1 E0 1B                        shl eax, 0x1b
005CA34F  C1 F8 1B                        sar eax, 0x1b
005CA352  85 C0                           test eax, eax
005CA354  74 33                           je 0x1405ca389
005CA356  83 F8 03                        cmp eax, 3
005CA359  75 09                           jne 0x1405ca364
005CA35B  41 8B C0                        mov eax, r8d
005CA35E  24 E0                           and al, 0xe0
005CA360  3C 40                           cmp al, 0x40
005CA362  74 05                           je 0x1405ca369
005CA364  44 03 CE                        add r9d, esi
005CA367  EB D8                           jmp 0x1405ca341
005CA369  83 65 C0 00                     and dword ptr [rbp - 0x40], 0
005CA36D  41 C1 E8 0E                     shr r8d, 0xe
005CA371  45 23 C4                        and r8d, r12d
005CA374  42 8D 04 45 01 00 00 00         lea eax, [r8*2 + 1]
005CA37C  0F BD C8                        bsr ecx, eax
005CA37F  8B C6                           mov eax, esi
005CA381  D3 E0                           shl eax, cl
005CA383  83 0F 08                        or dword ptr [rdi], 8
005CA386  89 47 14                        mov dword ptr [rdi + 0x14], eax
005CA389  E8 52 9D F2 FF                  call 0x1404f40e0
005CA38E  85 C0                           test eax, eax
005CA390  0F 84 9C 00 00 00               je 0x1405ca432
005CA396  8B 07                           mov eax, dword ptr [rdi]
005CA398  A8 20                           test al, 0x20
005CA39A  0F 85 92 00 00 00               jne 0x1405ca432
005CA3A0  45 3B FE                        cmp r15d, r14d
005CA3A3  0F 82 89 00 00 00               jb 0x1405ca432
005CA3A9  45 33 C9                        xor r9d, r9d
005CA3AC  33 C9                           xor ecx, ecx
005CA3AE  EB 38                           jmp 0x1405ca3e8
005CA3B0  83 F9 03                        cmp ecx, 3
005CA3B3  75 2D                           jne 0x1405ca3e2
005CA3B5  41 8B C0                        mov eax, r8d
005CA3B8  25 E0 00 00 00                  and eax, 0xe0
005CA3BD  83 F8 60                        cmp eax, 0x60
005CA3C0  77 20                           ja 0x1405ca3e2
005CA3C2  83 65 C0 00                     and dword ptr [rbp - 0x40], 0
005CA3C6  41 C1 E8 0E                     shr r8d, 0xe
005CA3CA  45 23 C4                        and r8d, r12d
005CA3CD  42 8D 04 45 01 00 00 00         lea eax, [r8*2 + 1]
005CA3D5  0F BD C8                        bsr ecx, eax
005CA3D8  8B C6                           mov eax, esi
005CA3DA  D3 E0                           shl eax, cl
005CA3DC  83 0F 20                        or dword ptr [rdi], 0x20
005CA3DF  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
005CA3E2  44 03 CE                        add r9d, esi
005CA3E5  41 8B C9                        mov ecx, r9d
005CA3E8  41 8B C6                        mov eax, r14d
005CA3EB  0F A2                           cpuid
005CA3ED  8B C8                           mov ecx, eax
005CA3EF  44 8B C0                        mov r8d, eax
005CA3F2  C1 E1 1B                        shl ecx, 0x1b
005CA3F5  C1 F9 1B                        sar ecx, 0x1b
005CA3F8  85 C9                           test ecx, ecx
005CA3FA  75 B4                           jne 0x1405ca3b0
005CA3FC  8B 0F                           mov ecx, dword ptr [rdi]
005CA3FE  F6 C1 20                        test cl, 0x20
005CA401  74 2F                           je 0x1405ca432
005CA403  8B C1                           mov eax, ecx
005CA405  83 E0 05                        and eax, 5
005CA408  3C 05                           cmp al, 5
005CA40A  75 0F                           jne 0x1405ca41b
005CA40C  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
005CA40F  0F AF 47 08                     imul eax, dword ptr [rdi + 8]
005CA413  39 47 1C                        cmp dword ptr [rdi + 0x1c], eax
005CA416  76 03                           jbe 0x1405ca41b
005CA418  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
005CA41B  83 E1 03                        and ecx, 3
005CA41E  80 F9 03                        cmp cl, 3
005CA421  75 0F                           jne 0x1405ca432
005CA423  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
005CA426  0F AF 47 08                     imul eax, dword ptr [rdi + 8]
005CA42A  39 47 1C                        cmp dword ptr [rdi + 0x1c], eax
005CA42D  76 03                           jbe 0x1405ca432
005CA42F  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
005CA432  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
005CA436  48 33 CC                        xor rcx, rsp
005CA439  E8 02 22 0E 00                  call 0x1406ac640
005CA43E  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
005CA446  48 83 C4 60                     add rsp, 0x60
005CA44A  41 5F                           pop r15
005CA44C  41 5E                           pop r14
005CA44E  41 5D                           pop r13
005CA450  41 5C                           pop r12
005CA452  5F                              pop rdi
005CA453  5E                              pop rsi
005CA454  5D                              pop rbp
005CA455  C3                              ret
005CA456  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiComputeTopologyConstantsIntelCompatible(int a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 8652414)) ^ (v_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m50 = 0;
    v_stack_m60 = v_xmm0;
    if (a2 < ((unsigned int)(result + 31))) goto loc_005CA106;
    a1 = 0;
    if ((unsigned int)(v_rbx) == 0) goto loc_005CA10F;
    goto loc_005CA11E;
loc_005CA106:
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)((unsigned int)((unsigned int)(result + 31))))) goto loc_005CA214;
loc_005CA10F:
    a1 = 0;
    if ((unsigned int)(v_rbx) == 0) goto loc_005CA219;
loc_005CA11E:
    v_r11 = 0;
    *(unsigned int *)(a4 + 24) = a2;
    a4 = 0;
loc_005CA12C:
    a1 = (unsigned int)((0) >> (8));
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(result + 1)));
    if ((unsigned __int8)(a1) == 0) goto loc_005CA1F7;
    result = (unsigned int)(((unsigned __int8)(a1)) - ((unsigned int)(result + 1)));
    if (condition_is_equal) goto loc_005CA1E1;
    result = (unsigned int)((result) - ((unsigned int)(result + 1)));
    if (condition_is_equal) goto loc_005CA1CB;
    result = (unsigned int)((result) - ((unsigned int)(result + 1)));
    if (condition_is_equal) goto loc_005CA1A8;
    result = (unsigned int)((result) - ((unsigned int)(result + 1)));
    if (condition_is_equal) goto loc_005CA195;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 31))))))) & (31));
    if (((unsigned int)(result)) == ((unsigned int)(result + 1))) goto loc_005CA177;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << ((unsigned __int8)((unsigned __int8)(a3))));
    *(unsigned int *)(v_rsp + 0 * 4 - 40) = a2;
    goto loc_005CA1F7;
loc_005CA177:
    a2 = 0;
    *(unsigned int *)(a4 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 * 4 - 40)));
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << ((unsigned __int8)((unsigned __int8)(a3))));
    v_stack_m4C = (unsigned int)(result);
    goto loc_005CA1F7;
loc_005CA195:
    a3 = (unsigned int)((a3) & (31));
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << ((unsigned __int8)((unsigned __int8)(a3))));
    v_stack_m50 = (unsigned int)(result);
    goto loc_005CA1F7;
loc_005CA1A8:
    a3 = (unsigned int)((a3) & (31));
    *(unsigned int *)(a4 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 4)))) * 4 - 40)));
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << ((unsigned __int8)((unsigned __int8)(a3))));
    v_stack_m54 = (unsigned int)(result);
    goto loc_005CA1F7;
loc_005CA1CB:
    a3 = (unsigned int)((a3) & (31));
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << ((unsigned __int8)((unsigned __int8)(a3))));
    v_stack_m58 = (unsigned int)(result);
    goto loc_005CA1F7;
loc_005CA1E1:
    a3 = (unsigned int)((a3) & (31));
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << ((unsigned __int8)((unsigned __int8)(a3))));
    *(unsigned int *)(a4 + 8) = (unsigned int)(result);
    v_stack_m5C = (unsigned int)(result);
loc_005CA1F7:
    if ((unsigned __int16)(v_rbx) != 0) goto loc_005CA12C;
    a2 = 0;
    *(unsigned int *)(a4 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 1)))) * 4 - 40)));
    goto loc_005CA27D;
loc_005CA214:
    result = (unsigned int)(*(unsigned int *)(v_rsp + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 1)))) * 4 - 40));
    if (((unsigned int)((unsigned int)(a2))) >= ((unsigned int)(result + 4))) {
        a1 = 0;
        result = (unsigned int)(result + 4);
        result = (unsigned int)((result) >> (26));
        result = result * 2 + 1;
        result = (unsigned int)(result + 1);
        result = (unsigned int)((result) << (0));
        *(unsigned int *)((unsigned int)((unsigned int)(result + 1)) + 12) = (unsigned int)(result);
    }
    if (((*(unsigned int *)(a3 + 12)) & (0x10000000ULL)) == 0) goto loc_005CA26F;
    a2 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << (0));
    *(unsigned int *)((unsigned int)((unsigned int)(result + 1)) + 8) = (unsigned int)(result);
    goto loc_005CA27D;
loc_005CA26F:
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(a1, a2, a3, (unsigned int)((unsigned int)(result + 1)));
    if ((unsigned int)(result) != 0) {
        *(unsigned int *)(a4 + 8) = (unsigned int)(result + 1);
    }
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(a1, a2, a3, (unsigned int)((unsigned int)(result + 1)));
    if ((unsigned int)(result) == 0) goto loc_005CA327;
    if (((unsigned int)((unsigned int)(a1))) != 2) goto loc_005CA327;
    if ((((unsigned __int8)(result + 4)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a4))))) != 0) goto loc_005CA327;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) >> (8));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (15));
    if (((unsigned int)(a3)) != 15) goto loc_005CA2D8;
    v_rbx = (unsigned int)((v_rbx) & (0xF00ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) >> (20));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) & (240));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    a2 = (unsigned int)(((unsigned __int8)(a1)) + ((unsigned int)(a3)));
    v_rbx = (unsigned int)((v_rbx) >> (4));
    if (a2 != 6) goto loc_005CA327;
    goto loc_005CA2EE;
loc_005CA2D8:
    if (((unsigned int)(a3)) != 6) goto loc_005CA327;
    v_rbx = (unsigned int)((v_rbx) & (0xF00ULL));
    result = (unsigned int)((result) & (240));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    v_rbx = (unsigned int)((v_rbx) >> (4));
loc_005CA2EE:
    if (((unsigned int)(v_rbx)) != 173) goto loc_005CA327;
    a2 = (a2) << (32);
    result = (result) | (a2);
    result = (result) >> (50);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != ((unsigned __int8)(result + 1))) goto loc_005CA327;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | ((unsigned int)(result + 4)));
    *(unsigned int *)(a4 + 16) = 64;
    *(unsigned int *)(a4) = (unsigned int)(a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12)))) < 64) {
        *(unsigned int *)(a4 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12)));
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4)))) & (8)) != 0) goto loc_005CA389;
    if (((unsigned int)((unsigned int)(a1))) != 2) goto loc_005CA389;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)(result + 4))) goto loc_005CA389;
    a4 = 0;
loc_005CA341:
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 4))) << (27));
    result = (unsigned int)((result) >> (27));
    if ((unsigned int)(result) == 0) goto loc_005CA389;
    if (((unsigned int)(result)) != 3) goto loc_005CA364;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 4))))))) & (224));
    if (((unsigned __int8)(result)) == 64) goto loc_005CA369;
loc_005CA364:
    a4 = (unsigned int)((a4) + ((unsigned int)(result + 1)));
    goto loc_005CA341;
loc_005CA369:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 4))))) >> (14));
    a3 = (unsigned int)((a3) & ((unsigned int)((unsigned int)(0xFFFULL))));
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1))) << (0));
    *(unsigned int *)(a4 + 20) = (unsigned int)(result);
loc_005CA389:
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(0, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_005CA432;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4)))) & (32)) != 0) goto loc_005CA432;
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)(result + 4))) goto loc_005CA432;
    a4 = 0;
    a1 = 0;
    goto loc_005CA3E8;
loc_005CA3B0:
    if (0 != 3) goto loc_005CA3E2;
    result = (unsigned int)(((unsigned int)((unsigned int)(a3))) & (224));
    if (((unsigned int)(result)) <= 96) {
        a3 = (unsigned int)((a3) >> (14));
        a3 = (unsigned int)((a3) & ((unsigned int)((unsigned int)(0xFFFULL))));
        result = a3 * 2 + 1;
        result = (unsigned int)(result + 1);
        result = (unsigned int)((result) << (0));
        *(unsigned int *)(a4 + 28) = (unsigned int)(result);
    }
    a4 = (unsigned int)((a4) + ((unsigned int)(result + 1)));
loc_005CA3E8:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 4))))) << (27));
    a1 = (unsigned int)((a1) >> (27));
    if (a1 != 0) goto loc_005CA3B0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4)))) & (32)) == 0) goto loc_005CA432;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) & (5));
    if (((unsigned __int8)(result)) != 5) goto loc_005CA41B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 16))) * (*(unsigned int *)(a4 + 8)));
    if ((*(unsigned int *)(a4 + 28)) >= = ((unsigned int)(result))) {
        *(unsigned int *)(a4 + 28) = (unsigned int)(result);
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) & (3));
    if (((unsigned __int8)(a1)) != 3) goto loc_005CA432;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 12))) * (*(unsigned int *)(a4 + 8)));
    if ((*(unsigned int *)(a4 + 28)) >= = ((unsigned int)(result))) {
        *(unsigned int *)(a4 + 28) = (unsigned int)(result);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result + 4)))), a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiComputeTopologyConstantsIntelCompatible(int32_t Arg1, int32_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint32_t v_stack_m78;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x84067E)) ^ (local_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m50 = 0;
    v_stack_m60 = v_xmm0;
    if (Arg2 < ((uint32_t)(result + 31))) goto loc_005CA106;
    Arg1 = 0;
    if ((uint32_t)(local_rbx) == 0) goto loc_005CA10F;
    goto loc_005CA11E;
loc_005CA106:
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)((uint32_t)((uint32_t)(result + 31))))) goto loc_005CA214;
loc_005CA10F:
    Arg1 = 0;
    if ((uint32_t)(local_rbx) == 0) goto loc_005CA219;
loc_005CA11E:
    local_r11 = 0;
    *(uint32_t *)(arg4 + 0x18) = Arg2;
    Arg4 = 0;
loc_005CA12C:
    Arg1 = (uint32_t)((0) >> (8));
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(result + 1)));
    if ((uint8_t)(Arg1) == 0) goto loc_005CA1F7;
    result = (uint32_t)(((uint8_t)(Arg1)) - ((uint32_t)(result + 1)));
    if (condition_is_equal) goto loc_005CA1E1;
    result = (uint32_t)((result) - ((uint32_t)(result + 1)));
    if (condition_is_equal) goto loc_005CA1CB;
    result = (uint32_t)((result) - ((uint32_t)(result + 1)));
    if (condition_is_equal) goto loc_005CA1A8;
    result = (uint32_t)((result) - ((uint32_t)(result + 1)));
    if (condition_is_equal) goto loc_005CA195;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 31))))))) & (31));
    if (((uint32_t)(result)) == ((uint32_t)(result + 1))) goto loc_005CA177;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << ((uint8_t)((uint8_t)(Arg3))));
    *(uint32_t *)(local_rsp + 0x0 * 4 - 0x28) = Arg2;
    goto loc_005CA1F7;
loc_005CA177:
    Arg2 = 0;
    *(uint32_t *)(arg4 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 4 - 0x28)));
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << ((uint8_t)((uint8_t)(Arg3))));
    v_stack_m4C = (uint32_t)(result);
    goto loc_005CA1F7;
loc_005CA195:
    Arg3 = (uint32_t)((Arg3) & (31));
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << ((uint8_t)((uint8_t)(Arg3))));
    v_stack_m50 = (uint32_t)(result);
    goto loc_005CA1F7;
loc_005CA1A8:
    Arg3 = (uint32_t)((Arg3) & (31));
    *(uint32_t *)(arg4 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 0x4)))) * 4 - 0x28)));
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << ((uint8_t)((uint8_t)(Arg3))));
    v_stack_m54 = (uint32_t)(result);
    goto loc_005CA1F7;
loc_005CA1CB:
    Arg3 = (uint32_t)((Arg3) & (31));
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << ((uint8_t)((uint8_t)(Arg3))));
    v_stack_m58 = (uint32_t)(result);
    goto loc_005CA1F7;
loc_005CA1E1:
    Arg3 = (uint32_t)((Arg3) & (31));
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << ((uint8_t)((uint8_t)(Arg3))));
    *(uint32_t *)(arg4 + 0x8) = (uint32_t)(result);
    v_stack_m5C = (uint32_t)(result);
loc_005CA1F7:
    if ((uint16_t)(local_rbx) != 0) goto loc_005CA12C;
    Arg2 = 0;
    *(uint32_t *)(arg4 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 0x1)))) * 4 - 0x28)));
    goto loc_005CA27D;
loc_005CA214:
    result = (uint32_t)(*(uint32_t *)(local_rsp + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 0x1)))) * 4 - 0x28));
    if (((uint32_t)((uint32_t)(Arg2))) >= ((uint32_t)(result + 4))) {
        Arg1 = 0;
        result = (uint32_t)(result + 4);
        result = (uint32_t)((result) >> (26));
        result = result * 2 + 1;
        result = (uint32_t)(result + 1);
        result = (uint32_t)((result) << (0));
        *(uint32_t *)((uint32_t)((uint32_t)(result + 0x1)) + 0xC) = (uint32_t)(result);
    }
    if (((*(uint32_t *)(arg3 + 0xC)) & (0x10000000ULL)) == 0) goto loc_005CA26F;
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << (0));
    *(uint32_t *)((uint32_t)((uint32_t)(result + 0x1)) + 0x8) = (uint32_t)(result);
    goto loc_005CA27D;
loc_005CA26F:
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(result + 1)));
    if ((uint32_t)(result) != 0) {
        *(uint32_t *)(arg4 + 0x8) = (uint32_t)(result + 1);
    }
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(result + 1)));
    if ((uint32_t)(result) == 0) goto loc_005CA327;
    if (((uint32_t)((uint32_t)(Arg1))) != 2) goto loc_005CA327;
    if ((((uint8_t)(result + 4)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg4))))) != 0) goto loc_005CA327;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3))))) >> (8));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (15));
    if (((uint32_t)(Arg3)) != 15) goto loc_005CA2D8;
    local_rbx = (uint32_t)((local_rbx) & (0xF00ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3))))) >> (20));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3))) & (240));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    Arg2 = (uint32_t)(((uint8_t)(Arg1)) + ((uint32_t)(Arg3)));
    local_rbx = (uint32_t)((local_rbx) >> (4));
    if (Arg2 != 6) goto loc_005CA327;
    goto loc_005CA2EE;
loc_005CA2D8:
    if (((uint32_t)(Arg3)) != 6) goto loc_005CA327;
    local_rbx = (uint32_t)((local_rbx) & (0xF00ULL));
    result = (uint32_t)((result) & (240));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    local_rbx = (uint32_t)((local_rbx) >> (4));
loc_005CA2EE:
    if (((uint32_t)(local_rbx)) != 173) goto loc_005CA327;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    result = (result) >> (50);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != ((uint8_t)(result + 1))) goto loc_005CA327;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) | ((uint32_t)(result + 4)));
    *(uint32_t *)(arg4 + 0x10) = 64;
    *(uint32_t *)(arg4) = (uint32_t)(Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC)))) < 64) {
        *(uint32_t *)(arg4 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC)));
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg4)))) & (8)) != 0) goto loc_005CA389;
    if (((uint32_t)((uint32_t)(Arg1))) != 2) goto loc_005CA389;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)(result + 4))) goto loc_005CA389;
    Arg4 = 0;
loc_005CA341:
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 4))) << (27));
    result = (uint32_t)((result) >> (27));
    if ((uint32_t)(result) == 0) goto loc_005CA389;
    if (((uint32_t)(result)) != 3) goto loc_005CA364;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 4))))))) & (224));
    if (((uint8_t)(result)) == 64) goto loc_005CA369;
loc_005CA364:
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(result + 1)));
    goto loc_005CA341;
loc_005CA369:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 4))))) >> (14));
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)((uint32_t)(0xFFFULL))));
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1))) << (0));
    *(uint32_t *)(arg4 + 0x14) = (uint32_t)(result);
loc_005CA389:
    result = Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(0, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_005CA432;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg4)))) & (32)) != 0) goto loc_005CA432;
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)(result + 4))) goto loc_005CA432;
    Arg4 = 0;
    Arg1 = 0;
    goto loc_005CA3E8;
loc_005CA3B0:
    if (0 != 3) goto loc_005CA3E2;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) & (224));
    if (((uint32_t)(result)) <= 96) {
        Arg3 = (uint32_t)((Arg3) >> (14));
        Arg3 = (uint32_t)((Arg3) & ((uint32_t)((uint32_t)(0xFFFULL))));
        result = Arg3 * 2 + 1;
        result = (uint32_t)(result + 1);
        result = (uint32_t)((result) << (0));
        *(uint32_t *)(arg4 + 0x1C) = (uint32_t)(result);
    }
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(result + 1)));
loc_005CA3E8:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 4))))) << (27));
    Arg1 = (uint32_t)((Arg1) >> (27));
    if (Arg1 != 0) goto loc_005CA3B0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg4)))) & (32)) == 0) goto loc_005CA432;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) & (5));
    if (((uint8_t)(result)) != 5) goto loc_005CA41B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x10))) * (*(uint32_t *)(arg4 + 0x8)));
    if ((*(uint32_t *)(arg4 + 0x1C)) >= = ((uint32_t)(result))) {
        *(uint32_t *)(arg4 + 0x1C) = (uint32_t)(result);
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) & (3));
    if (((uint8_t)(Arg1)) != 3) goto loc_005CA432;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0xC))) * (*(uint32_t *)(arg4 + 0x8)));
    if ((*(uint32_t *)(arg4 + 0x1C)) >= = ((uint32_t)(result))) {
        *(uint32_t *)(arg4 + 0x1C) = (uint32_t)(result);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result + 4)))), Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x6` | `8` | `R` |
| `Arg3` | `+ 0xC` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x8` | `32` | `R` |
| `Arg4` | `+ 0x8` | `32` | `W` |
| `Arg4` | `+ 0xC` | `32` | `R` |
| `Arg4` | `+ 0xC` | `32` | `W` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg4` | `+ 0x10` | `32` | `W` |
| `Arg4` | `+ 0x14` | `32` | `W` |
| `Arg4` | `+ 0x18` | `32` | `W` |
| `Arg4` | `+ 0x1C` | `32` | `R` |
| `Arg4` | `+ 0x1C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CA0A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
