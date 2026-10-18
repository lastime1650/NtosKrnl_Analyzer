# RtlpWalkFrameChain

- RVA: `0x002F3ED0`–`0x002F4EC8` (길이 `4,088` bytes)
- VA: `0x00000001402F3ED0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000720F8`
- 디코드: `869`개 명령, `4,088/4,088` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002F3FF4` → [RtlpValidateContextFlags2](../4E/RtlpValidateContextFlags2_function_004EF138.md) (function, `0x004EF138`)
- `0x002F4039` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x002F4056` → [RtlInitializeExtendedContext2](RtlInitializeExtendedContext2_function_002F5D40.md) (function, `0x002F5D40`)
- `0x002F405E` → [RtlpCaptureContext2](../4F/RtlpCaptureContext2_function_004FE6B0.md) (function, `0x004FE6B0`)
- `0x002F406F` → [RtlpGetStackLimits](RtlpGetStackLimits_function_002F5F50.md) (function, `0x002F5F50`)
- `0x002F40EE` → [PsWow64GetProcessMachine](../../page/8D/PsWow64GetProcessMachine_function_008D2130.md) (function, `0x008D2130`)
- `0x002F41E1` → [RtlpLookupFunctionEntryForStackWalks](RtlpLookupFunctionEntryForStackWalks_function_002F4ED0.md) (function, `0x002F4ED0`)
- `0x002F4272` → [RtlpxVirtualUnwind](RtlpxVirtualUnwind_function_002F5110.md) (function, `0x002F5110`)
- `0x002F460D` → [KeGetCurrentStackPointer](../6B/KeGetCurrentStackPointer_function_006B1070.md) (function, `0x006B1070`)
- `0x002F4627` → [KeQueryCurrentStackInformationEx](KeQueryCurrentStackInformationEx_function_002F7CD0.md) (function, `0x002F7CD0`)
- `0x002F4958` → [RtlpWalkWowStack](../40/RtlpWalkWowStack_function_004095B0.md) (function, `0x004095B0`)
- `0x002F4983` → [PsWow64GetProcessMachine](../../page/8D/PsWow64GetProcessMachine_function_008D2130.md) (function, `0x008D2130`)
- `0x002F49CA` → [RtlWow64GetCpuAreaInfo](../../page/8C/RtlWow64GetCpuAreaInfo_function_008CDE0C.md) (function, `0x008CDE0C`)
- `0x002F49E6` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002F4AC6` → [RtlpWalkWowStack](../40/RtlpWalkWowStack_function_004095B0.md) (function, `0x004095B0`)
- `0x002F4B3B` → [KeGetEffectiveIrql](KeGetEffectiveIrql_function_002F8030.md) (function, `0x002F8030`)
- `0x002F4DC6` → [RtlpGetEntireXStateAreaLength2](../4E/RtlpGetEntireXStateAreaLength2_function_004EF20C.md) (function, `0x004EF20C`)
- `0x002F4DEB` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002F4E4F` → [RtlpRemoveArchDisallowedXStateFeatures](RtlpRemoveArchDisallowedXStateFeatures_function_002F32FC.md) (function, `0x002F32FC`)

### Direct callers
- [RtlWalkFrameChain](RtlWalkFrameChain_function_002F85E0.md) at `0x002F866F`

### Static image references
- `0x002F3EFB` → RVA `0x00E0A740` (`.data`; read)
- `0x002F4166` → RVA `0x01200030` (`CFGRO`; read)
- `0x002F4174` → RVA `0x01200040` (`CFGRO`; read)
- `0x002F4B55` → RVA `0x00FC507C` (`ALMOSTRO`; read)
- `0x002F4BC7` → RVA `0x00FC51D4` (`ALMOSTRO`; read)
- `0x002F4E5D` → RVA `0x00FC51F4` (`ALMOSTRO`; read)
- `0x002F4E91` → RVA `0x00FC7500` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x002F40EE` → [PsWow64GetProcessMachine](../../page/8D/PsWow64GetProcessMachine_function_008D2130.md) (`.text` → `PAGE`)
  - `0x002F4983` → [PsWow64GetProcessMachine](../../page/8D/PsWow64GetProcessMachine_function_008D2130.md) (`.text` → `PAGE`)
  - `0x002F49CA` → [RtlWow64GetCpuAreaInfo](../../page/8C/RtlWow64GetCpuAreaInfo_function_008CDE0C.md) (`.text` → `PAGE`)
  - `0x002F49E6` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002F3ED0  40 55                           push rbp
002F3ED2  41 54                           push r12
002F3ED4  41 55                           push r13
002F3ED6  41 56                           push r14
002F3ED8  41 57                           push r15
002F3EDA  48 81 EC D0 01 00 00            sub rsp, 0x1d0
002F3EE1  48 8D 6C 24 60                  lea rbp, [rsp + 0x60]
002F3EE6  48 89 9D A0 01 00 00            mov qword ptr [rbp + 0x1a0], rbx
002F3EED  48 89 B5 A8 01 00 00            mov qword ptr [rbp + 0x1a8], rsi
002F3EF4  48 89 BD B0 01 00 00            mov qword ptr [rbp + 0x1b0], rdi
002F3EFB  48 8B 05 3E 68 B1 00            mov rax, qword ptr [rip + 0xb1683e]
002F3F02  48 33 C5                        xor rax, rbp
002F3F05  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
002F3F0C  44 89 4D 4C                     mov dword ptr [rbp + 0x4c], r9d
002F3F10  41 8B F8                        mov edi, r8d
002F3F13  89 55 50                        mov dword ptr [rbp + 0x50], edx
002F3F16  48 89 8D A8 00 00 00            mov qword ptr [rbp + 0xa8], rcx
002F3F1D  45 33 C0                        xor r8d, r8d
002F3F20  4C 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], r8
002F3F27  41 8B D8                        mov ebx, r8d
002F3F2A  4C 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], r8
002F3F31  4C 89 85 08 01 00 00            mov qword ptr [rbp + 0x108], r8
002F3F38  44 89 45 48                     mov dword ptr [rbp + 0x48], r8d
002F3F3C  4C 89 45 30                     mov qword ptr [rbp + 0x30], r8
002F3F40  0F 57 C0                        xorps xmm0, xmm0
002F3F43  0F 11 85 C0 00 00 00            movups xmmword ptr [rbp + 0xc0], xmm0
002F3F4A  0F 11 85 D0 00 00 00            movups xmmword ptr [rbp + 0xd0], xmm0
002F3F51  4C 89 45 18                     mov qword ptr [rbp + 0x18], r8
002F3F55  4C 89 45 60                     mov qword ptr [rbp + 0x60], r8
002F3F59  4C 89 45 58                     mov qword ptr [rbp + 0x58], r8
002F3F5D  C6 45 09 01                     mov byte ptr [rbp + 9], 1
002F3F61  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002F3F6A  F7 41 74 00 04 00 00            test dword ptr [rcx + 0x74], 0x400
002F3F71  0F 85 A0 0E 00 00               jne 0x1402f4e17
002F3F77  80 B9 4A 02 00 00 01            cmp byte ptr [rcx + 0x24a], 1
002F3F7E  0F 84 93 0E 00 00               je 0x1402f4e17
002F3F84  48 8B 81 F0 00 00 00            mov rax, qword ptr [rcx + 0xf0]
002F3F8B  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
002F3F92  4C 89 45 38                     mov qword ptr [rbp + 0x38], r8
002F3F96  44 89 45 0C                     mov dword ptr [rbp + 0xc], r8d
002F3F9A  49 8B D0                        mov rdx, r8
002F3F9D  48 89 95 88 00 00 00            mov qword ptr [rbp + 0x88], rdx
002F3FA4  44 8B F7                        mov r14d, edi
002F3FA7  41 83 E6 01                     and r14d, 1
002F3FAB  44 89 B5 A0 00 00 00            mov dword ptr [rbp + 0xa0], r14d
002F3FB2  0F 85 BF 0E 00 00               jne 0x1402f4e77
002F3FB8  48 8B C2                        mov rax, rdx
002F3FBB  48 F7 D8                        neg rax
002F3FBE  48 1B F6                        sbb rsi, rsi
002F3FC1  81 E6 00 08 00 00               and esi, 0x800
002F3FC7  48 8B C2                        mov rax, rdx
002F3FCA  48 F7 D8                        neg rax
002F3FCD  1B C9                           sbb ecx, ecx
002F3FCF  83 E1 40                        and ecx, 0x40
002F3FD2  44 8D B9 0B 00 10 00            lea r15d, [rcx + 0x10000b]
002F3FD9  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
002F3FE3  44 8B E6                        mov r12d, esi
002F3FE6  44 89 45 04                     mov dword ptr [rbp + 4], r8d
002F3FEA  4C 8B C0                        mov r8, rax
002F3FED  48 8D 55 04                     lea rdx, [rbp + 4]
002F3FF1  41 8B CF                        mov ecx, r15d
002F3FF4  E8 3F B1 1F 00                  call 0x1404ef138
002F3FF9  85 C0                           test eax, eax
002F3FFB  78 20                           js 0x1402f401d
002F3FFD  B8 F0 04 00 00                  mov eax, 0x4f0
002F4002  44 8B 5D 04                     mov r11d, dword ptr [rbp + 4]
002F4006  41 F6 C3 02                     test r11b, 2
002F400A  0F 85 99 0D 00 00               jne 0x1402f4da9
002F4010  41 F6 C3 04                     test r11b, 4
002F4014  8D 58 20                        lea ebx, [rax + 0x20]
002F4017  0F 44 D8                        cmove ebx, eax
002F401A  83 C3 0F                        add ebx, 0xf
002F401D  8B C3                           mov eax, ebx
002F401F  48 8D 48 0F                     lea rcx, [rax + 0xf]
002F4023  48 3B C8                        cmp rcx, rax
002F4026  77 0A                           ja 0x1402f4032
002F4028  48 B9 F0 FF FF FF FF FF FF 0F   movabs rcx, 0xffffffffffffff0
002F4032  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
002F4036  48 8B C1                        mov rax, rcx
002F4039  E8 22 69 3C 00                  call 0x1406ba960
002F403E  48 2B E1                        sub rsp, rcx
002F4041  4C 8D 6C 24 60                  lea r13, [rsp + 0x60]
002F4046  4C 8B CE                        mov r9, rsi
002F4049  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
002F4050  41 8B D7                        mov edx, r15d
002F4053  49 8B CD                        mov rcx, r13
002F4056  E8 E5 1C 00 00                  call 0x1402f5d40
002F405B  49 8B CD                        mov rcx, r13
002F405E  E8 4D A6 20 00                  call 0x1404fe6b0
002F4063  C6 45 08 00                     mov byte ptr [rbp + 8], 0
002F4067  48 8D 55 30                     lea rdx, [rbp + 0x30]
002F406B  48 8D 4D 18                     lea rcx, [rbp + 0x18]
002F406F  E8 DC 1E 00 00                  call 0x1402f5f50
002F4074  84 C0                           test al, al
002F4076  0F 84 45 0E 00 00               je 0x1402f4ec1
002F407C  45 33 DB                        xor r11d, r11d
002F407F  44 89 5D 04                     mov dword ptr [rbp + 4], r11d
002F4083  D1 EF                           shr edi, 1
002F4085  40 80 E7 01                     and dil, 1
002F4089  45 85 F6                        test r14d, r14d
002F408C  0F 84 CB 0D 00 00               je 0x1402f4e5d
002F4092  4C 89 9D 98 00 00 00            mov qword ptr [rbp + 0x98], r11
002F4099  4C 89 5D 68                     mov qword ptr [rbp + 0x68], r11
002F409D  45 85 F6                        test r14d, r14d
002F40A0  0F 84 D2 0C 00 00               je 0x1402f4d78
002F40A6  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
002F40AF  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
002F40B3  F6 40 08 01                     test byte ptr [rax + 8], 1
002F40B7  0F 85 76 02 00 00               jne 0x1402f4333
002F40BD  48 8D B0 70 FE FF FF            lea rsi, [rax - 0x190]
002F40C4  48 89 75 38                     mov qword ptr [rbp + 0x38], rsi
002F40C8  4C 8B BD 80 00 00 00            mov r15, qword ptr [rbp + 0x80]
002F40CF  4D 85 FF                        test r15, r15
002F40D2  74 0C                           je 0x1402f40e0
002F40D4  66 41 0F BA A7 EE 17 00 00 08   bt word ptr [r15 + 0x17ee], 8
002F40DE  73 07                           jae 0x1402f40e7
002F40E0  33 C0                           xor eax, eax
002F40E2  E9 FA 0C 00 00                  jmp 0x1402f4de1
002F40E7  48 8B 8B B8 00 00 00            mov rcx, qword ptr [rbx + 0xb8]
002F40EE  E8 3D E0 5D 00                  call 0x1408d2130
002F40F3  BA 4C 01 00 00                  mov edx, 0x14c
002F40F8  66 3B C2                        cmp ax, dx
002F40FB  0F 84 05 08 00 00               je 0x1402f4906
002F4101  48 8B 86 80 01 00 00            mov rax, qword ptr [rsi + 0x180]
002F4108  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
002F410F  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
002F4113  48 89 4D 68                     mov qword ptr [rbp + 0x68], rcx
002F4117  48 3B C8                        cmp rcx, rax
002F411A  0F 86 75 0B 00 00               jbe 0x1402f4c95
002F4120  48 3B C8                        cmp rcx, rax
002F4123  0F 85 74 07 00 00               jne 0x1402f489d
002F4129  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
002F412D  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
002F4131  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
002F4135  48 8B C1                        mov rax, rcx
002F4138  F6 41 08 01                     test byte ptr [rcx + 8], 1
002F413C  0F 85 17 0B 00 00               jne 0x1402f4c59
002F4142  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
002F4146  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
002F414A  48 89 4D 58                     mov qword ptr [rbp + 0x58], rcx
002F414E  0F B6 4B 7D                     movzx ecx, byte ptr [rbx + 0x7d]
002F4152  0F B6 C1                        movzx eax, cl
002F4155  C0 E8 02                        shr al, 2
002F4158  24 01                           and al, 1
002F415A  88 45 09                        mov byte ptr [rbp + 9], al
002F415D  80 C9 04                        or cl, 4
002F4160  88 4B 7D                        mov byte ptr [rbx + 0x7d], cl
002F4163  45 33 DB                        xor r11d, r11d
002F4166  0F 28 05 C3 BE F0 00            movaps xmm0, xmmword ptr [rip + 0xf0bec3]
002F416D  0F 11 85 28 01 00 00            movups xmmword ptr [rbp + 0x128], xmm0
002F4174  F2 0F 10 0D C4 BE F0 00         movsd xmm1, qword ptr [rip + 0xf0bec4]
002F417C  F2 0F 11 8D 38 01 00 00         movsd qword ptr [rbp + 0x138], xmm1
002F4184  40 88 7D 00                     mov byte ptr [rbp], dil
002F4188  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
002F418C  8B 75 0C                        mov esi, dword ptr [rbp + 0xc]
002F418F  49 B8 00 00 00 00 00 80 FF FF   movabs r8, 0xffff800000000000
002F4199  4C 8B 65 60                     mov r12, qword ptr [rbp + 0x60]
002F419D  49 8B 9D 98 00 00 00            mov rbx, qword ptr [r13 + 0x98]
002F41A4  4C 89 9D B8 00 00 00            mov qword ptr [rbp + 0xb8], r11
002F41AB  4C 89 9D B0 00 00 00            mov qword ptr [rbp + 0xb0], r11
002F41B2  44 89 5D 10                     mov dword ptr [rbp + 0x10], r11d
002F41B6  F6 C3 07                        test bl, 7
002F41B9  0F 85 D8 0B 00 00               jne 0x1402f4d97
002F41BF  48 3B 5D 18                     cmp rbx, qword ptr [rbp + 0x18]
002F41C3  0F 82 32 04 00 00               jb 0x1402f45fb
002F41C9  48 3B 5D 30                     cmp rbx, qword ptr [rbp + 0x30]
002F41CD  0F 83 28 04 00 00               jae 0x1402f45fb
002F41D3  48 8D 95 28 01 00 00            lea rdx, [rbp + 0x128]
002F41DA  49 8B 8D F8 00 00 00            mov rcx, qword ptr [r13 + 0xf8]
002F41E1  E8 EA 0C 00 00                  call 0x1402f4ed0
002F41E6  48 8B 95 30 01 00 00            mov rdx, qword ptr [rbp + 0x130]
002F41ED  48 85 C0                        test rax, rax
002F41F0  0F 84 AB 09 00 00               je 0x1402f4ba1
002F41F6  4D 8B 85 F8 00 00 00            mov r8, qword ptr [r13 + 0xf8]
002F41FD  0F 57 C0                        xorps xmm0, xmm0
002F4200  33 C9                           xor ecx, ecx
002F4202  0F 11 85 10 01 00 00            movups xmmword ptr [rbp + 0x110], xmm0
002F4209  48 89 8D 20 01 00 00            mov qword ptr [rbp + 0x120], rcx
002F4210  45 33 C9                        xor r9d, r9d
002F4213  4C 89 8D 20 01 00 00            mov qword ptr [rbp + 0x120], r9
002F421A  48 8D 4D 18                     lea rcx, [rbp + 0x18]
002F421E  48 89 8D 10 01 00 00            mov qword ptr [rbp + 0x110], rcx
002F4225  48 8D 4D 30                     lea rcx, [rbp + 0x30]
002F4229  48 89 8D 18 01 00 00            mov qword ptr [rbp + 0x118], rcx
002F4230  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
002F4235  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
002F423C  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
002F4241  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
002F4246  48 8D 8D 00 01 00 00            lea rcx, [rbp + 0x100]
002F424D  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
002F4252  48 8D 8D 08 01 00 00            lea rcx, [rbp + 0x108]
002F4259  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
002F425E  48 8D 4D 08                     lea rcx, [rbp + 8]
002F4262  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002F4267  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
002F426C  4C 8B C8                        mov r9, rax
002F426F  8B 4D 48                        mov ecx, dword ptr [rbp + 0x48]
002F4272  E8 99 0E 00 00                  call 0x1402f5110
002F4277  85 C0                           test eax, eax
002F4279  0F 88 1D 09 00 00               js 0x1402f4b9c
002F427F  0F B6 45 00                     movzx eax, byte ptr [rbp]
002F4283  80 7D 08 00                     cmp byte ptr [rbp + 8], 0
002F4287  41 BB 00 00 00 00               mov r11d, 0
002F428D  41 0F 45 C3                     cmovne eax, r11d
002F4291  88 45 00                        mov byte ptr [rbp], al
002F4294  83 FE 01                        cmp esi, 1
002F4297  75 16                           jne 0x1402f42af
002F4299  44 39 5D 04                     cmp dword ptr [rbp + 4], r11d
002F429D  76 10                           jbe 0x1402f42af
002F429F  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
002F42A6  48 85 C0                        test rax, rax
002F42A9  0F 85 27 02 00 00               jne 0x1402f44d6
002F42AF  49 8B 8D F8 00 00 00            mov rcx, qword ptr [r13 + 0xf8]
002F42B6  48 85 C9                        test rcx, rcx
002F42B9  0F 84 AB 06 00 00               je 0x1402f496a
002F42BF  85 F6                           test esi, esi
002F42C1  75 79                           jne 0x1402f433c
002F42C3  49 B8 00 00 00 00 00 80 FF FF   movabs r8, 0xffff800000000000
002F42CD  45 85 F6                        test r14d, r14d
002F42D0  75 1A                           jne 0x1402f42ec
002F42D2  49 3B C8                        cmp rcx, r8
002F42D5  0F 82 B5 09 00 00               jb 0x1402f4c90
002F42DB  45 85 F6                        test r14d, r14d
002F42DE  75 0C                           jne 0x1402f42ec
002F42E0  44 38 75 00                     cmp byte ptr [rbp], r14b
002F42E4  0F 85 C8 02 00 00               jne 0x1402f45b2
002F42EA  EB 13                           jmp 0x1402f42ff
002F42EC  49 3B C8                        cmp rcx, r8
002F42EF  0F 82 5C 04 00 00               jb 0x1402f4751
002F42F5  83 7D 04 00                     cmp dword ptr [rbp + 4], 0
002F42F9  0F 85 99 05 00 00               jne 0x1402f4898
002F42FF  8B 45 04                        mov eax, dword ptr [rbp + 4]
002F4302  8B 55 4C                        mov edx, dword ptr [rbp + 0x4c]
002F4305  3B C2                           cmp eax, edx
002F4307  72 14                           jb 0x1402f431d
002F4309  49 8B 8D F8 00 00 00            mov rcx, qword ptr [r13 + 0xf8]
002F4310  2B C2                           sub eax, edx
002F4312  48 8B 95 A8 00 00 00            mov rdx, qword ptr [rbp + 0xa8]
002F4319  48 89 0C C2                     mov qword ptr [rdx + rax*8], rcx
002F431D  8B 45 04                        mov eax, dword ptr [rbp + 4]
002F4320  FF C0                           inc eax
002F4322  89 45 04                        mov dword ptr [rbp + 4], eax
002F4325  3B 45 50                        cmp eax, dword ptr [rbp + 0x50]
002F4328  0F 83 7F 02 00 00               jae 0x1402f45ad
002F432E  E9 5C FE FF FF                  jmp 0x1402f418f
002F4333  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
002F4337  E9 77 FD FF FF                  jmp 0x1402f40b3
002F433C  8B D6                           mov edx, esi
002F433E  83 EA 01                        sub edx, 1
002F4341  0F 85 70 02 00 00               jne 0x1402f45b7
002F4347  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
002F4351  48 3B C8                        cmp rcx, rax
002F4354  0F 87 11 07 00 00               ja 0x1402f4a6b
002F435A  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
002F435E  48 85 D2                        test rdx, rdx
002F4361  74 9C                           je 0x1402f42ff
002F4363  48 3B 8F 68 01 00 00            cmp rcx, qword ptr [rdi + 0x168]
002F436A  75 93                           jne 0x1402f42ff
002F436C  BE 02 00 00 00                  mov esi, 2
002F4371  89 75 0C                        mov dword ptr [rbp + 0xc], esi
002F4374  48 8B 82 38 01 00 00            mov rax, qword ptr [rdx + 0x138]
002F437B  49 89 85 F8 00 00 00            mov qword ptr [r13 + 0xf8], rax
002F4382  48 8D 82 40 01 00 00            lea rax, [rdx + 0x140]
002F4389  49 89 85 98 00 00 00            mov qword ptr [r13 + 0x98], rax
002F4390  48 8B 82 F8 00 00 00            mov rax, qword ptr [rdx + 0xf8]
002F4397  49 89 85 A0 00 00 00            mov qword ptr [r13 + 0xa0], rax
002F439E  48 8B 82 00 01 00 00            mov rax, qword ptr [rdx + 0x100]
002F43A5  49 89 85 90 00 00 00            mov qword ptr [r13 + 0x90], rax
002F43AC  48 8B 82 08 01 00 00            mov rax, qword ptr [rdx + 0x108]
002F43B3  49 89 85 B0 00 00 00            mov qword ptr [r13 + 0xb0], rax
002F43BA  48 8B 82 10 01 00 00            mov rax, qword ptr [rdx + 0x110]
002F43C1  49 89 85 A8 00 00 00            mov qword ptr [r13 + 0xa8], rax
002F43C8  48 8B 82 18 01 00 00            mov rax, qword ptr [rdx + 0x118]
002F43CF  49 89 85 D8 00 00 00            mov qword ptr [r13 + 0xd8], rax
002F43D6  48 8B 82 20 01 00 00            mov rax, qword ptr [rdx + 0x120]
002F43DD  49 89 85 E0 00 00 00            mov qword ptr [r13 + 0xe0], rax
002F43E4  48 8B 82 28 01 00 00            mov rax, qword ptr [rdx + 0x128]
002F43EB  49 89 85 E8 00 00 00            mov qword ptr [r13 + 0xe8], rax
002F43F2  48 8B 82 30 01 00 00            mov rax, qword ptr [rdx + 0x130]
002F43F9  49 89 85 F0 00 00 00            mov qword ptr [r13 + 0xf0], rax
002F4400  48 83 BD 88 00 00 00 00         cmp qword ptr [rbp + 0x88], 0
002F4408  0F 84 15 08 00 00               je 0x1402f4c23
002F440E  44 89 5D 74                     mov dword ptr [rbp + 0x74], r11d
002F4412  44 89 5D 24                     mov dword ptr [rbp + 0x24], r11d
002F4416  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
002F4420  48 B9 08 07 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000708
002F442A  8B 09                           mov ecx, dword ptr [rcx]
002F442C  0B 08                           or ecx, dword ptr [rax]
002F442E  48 0F BA E1 0B                  bt rcx, 0xb
002F4433  0F 83 BC 08 00 00               jae 0x1402f4cf5
002F4439  A1 EC 03 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000003ec]
002F4442  A9 F8 FF FF FF                  test eax, 0xfffffff8
002F4447  0F 85 A8 08 00 00               jne 0x1402f4cf5
002F444D  4C 8B 95 90 00 00 00            mov r10, qword ptr [rbp + 0x90]
002F4454  41 8B 12                        mov edx, dword ptr [r10]
002F4457  4D 63 4A 10                     movsxd r9, dword ptr [r10 + 0x10]
002F445B  41 3B D1                        cmp edx, r9d
002F445E  0F 8F 91 08 00 00               jg 0x1402f4cf5
002F4464  45 8B 42 14                     mov r8d, dword ptr [r10 + 0x14]
002F4468  45 03 C1                        add r8d, r9d
002F446B  41 03 52 04                     add edx, dword ptr [r10 + 4]
002F446F  41 3B D0                        cmp edx, r8d
002F4472  0F 8C 7D 08 00 00               jl 0x1402f4cf5
002F4478  4D 8B C1                        mov r8, r9
002F447B  4D 03 C2                        add r8, r10
002F447E  0F 84 71 08 00 00               je 0x1402f4cf5
002F4484  40 84 C6                        test sil, al
002F4487  0F 84 D1 08 00 00               je 0x1402f4d5e
002F448D  49 8B 50 08                     mov rdx, qword ptr [r8 + 8]
002F4491  48 0F BA E2 0B                  bt rdx, 0xb
002F4496  0F 83 59 08 00 00               jae 0x1402f4cf5
002F449C  48 B8 F8 05 00 00 80 F7 FF FF   movabs rax, 0xfffff780000005f8
002F44A6  4C 8B 10                        mov r10, qword ptr [rax]
002F44A9  41 B9 40 02 00 00               mov r9d, 0x240
002F44AF  44 89 4D 24                     mov dword ptr [rbp + 0x24], r9d
002F44B3  8B CE                           mov ecx, esi
002F44B5  89 4D 74                        mov dword ptr [rbp + 0x74], ecx
002F44B8  83 F9 0B                        cmp ecx, 0xb
002F44BB  0F 83 40 07 00 00               jae 0x1402f4c01
002F44C1  B8 01 00 00 00                  mov eax, 1
002F44C6  48 D3 E0                        shl rax, cl
002F44C9  48 85 C2                        test rdx, rax
002F44CC  0F 85 62 08 00 00               jne 0x1402f4d34
002F44D2  FF C1                           inc ecx
002F44D4  EB DF                           jmp 0x1402f44b5
002F44D6  49 39 85 F8 00 00 00            cmp qword ptr [r13 + 0xf8], rax
002F44DD  0F 85 CC FD FF FF               jne 0x1402f42af
002F44E3  44 89 5D 70                     mov dword ptr [rbp + 0x70], r11d
002F44E7  44 89 5D 20                     mov dword ptr [rbp + 0x20], r11d
002F44EB  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
002F44F5  48 B9 08 07 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000708
002F44FF  8B 09                           mov ecx, dword ptr [rcx]
002F4501  0B 08                           or ecx, dword ptr [rax]
002F4503  48 0F BA E1 0B                  bt rcx, 0xb
002F4508  0F 83 84 06 00 00               jae 0x1402f4b92
002F450E  A1 EC 03 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000003ec]
002F4517  A9 F8 FF FF FF                  test eax, 0xfffffff8
002F451C  0F 85 70 06 00 00               jne 0x1402f4b92
002F4522  4C 8B 9D 90 00 00 00            mov r11, qword ptr [rbp + 0x90]
002F4529  41 8B 13                        mov edx, dword ptr [r11]
002F452C  4D 63 4B 10                     movsxd r9, dword ptr [r11 + 0x10]
002F4530  41 3B D1                        cmp edx, r9d
002F4533  0F 8F 56 06 00 00               jg 0x1402f4b8f
002F4539  45 8B 43 14                     mov r8d, dword ptr [r11 + 0x14]
002F453D  45 03 C1                        add r8d, r9d
002F4540  41 03 53 04                     add edx, dword ptr [r11 + 4]
002F4544  41 3B D0                        cmp edx, r8d
002F4547  0F 8C 42 06 00 00               jl 0x1402f4b8f
002F454D  4D 8B D1                        mov r10, r9
002F4550  4D 03 D3                        add r10, r11
002F4553  0F 84 36 06 00 00               je 0x1402f4b8f
002F4559  A8 02                           test al, 2
002F455B  0F 84 69 07 00 00               je 0x1402f4cca
002F4561  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
002F4565  48 0F BA E2 0B                  bt rdx, 0xb
002F456A  0F 83 1F 06 00 00               jae 0x1402f4b8f
002F4570  48 B8 F8 05 00 00 80 F7 FF FF   movabs rax, 0xfffff780000005f8
002F457A  4C 8B 08                        mov r9, qword ptr [rax]
002F457D  41 B8 40 02 00 00               mov r8d, 0x240
002F4583  44 89 45 20                     mov dword ptr [rbp + 0x20], r8d
002F4587  B9 02 00 00 00                  mov ecx, 2
002F458C  89 4D 70                        mov dword ptr [rbp + 0x70], ecx
002F458F  83 F9 0B                        cmp ecx, 0xb
002F4592  0F 83 CB 02 00 00               jae 0x1402f4863
002F4598  B8 01 00 00 00                  mov eax, 1
002F459D  48 D3 E0                        shl rax, cl
002F45A0  48 85 C2                        test rdx, rax
002F45A3  0F 85 BD 06 00 00               jne 0x1402f4c66
002F45A9  FF C1                           inc ecx
002F45AB  EB DF                           jmp 0x1402f458c
002F45AD  E9 23 08 00 00                  jmp 0x1402f4dd5
002F45B2  E9 E2 FB FF FF                  jmp 0x1402f4199
002F45B7  83 FA 01                        cmp edx, 1
002F45BA  0F 85 A6 04 00 00               jne 0x1402f4a66
002F45C0  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
002F45CA  48 3B C8                        cmp rcx, rax
002F45CD  0F 87 2C FD FF FF               ja 0x1402f42ff
002F45D3  48 3B 8F 68 01 00 00            cmp rcx, qword ptr [rdi + 0x168]
002F45DA  0F 85 AC 07 00 00               jne 0x1402f4d8c
002F45E0  48 8B 87 80 01 00 00            mov rax, qword ptr [rdi + 0x180]
002F45E7  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
002F45EE  A8 03                           test al, 3
002F45F0  0F 85 F0 03 00 00               jne 0x1402f49e6
002F45F6  E9 DD 04 00 00                  jmp 0x1402f4ad8
002F45FB  41 8B C3                        mov eax, r11d
002F45FE  4C 39 45 18                     cmp qword ptr [rbp + 0x18], r8
002F4602  0F 93 C0                        setae al
002F4605  85 C0                           test eax, eax
002F4607  0F 84 8A 07 00 00               je 0x1402f4d97
002F460D  E8 5E CA 3B 00                  call 0x1406b1070
002F4612  48 8B C8                        mov rcx, rax
002F4615  4C 8D 8D B8 00 00 00            lea r9, [rbp + 0xb8]
002F461C  4C 8D 85 B0 00 00 00            lea r8, [rbp + 0xb0]
002F4623  48 8D 55 10                     lea rdx, [rbp + 0x10]
002F4627  E8 A4 36 00 00                  call 0x1402f7cd0
002F462C  8B 45 10                        mov eax, dword ptr [rbp + 0x10]
002F462F  83 F8 09                        cmp eax, 9
002F4632  77 0E                           ja 0x1402f4642
002F4634  B9 A1 03 00 00                  mov ecx, 0x3a1
002F4639  0F A3 C1                        bt ecx, eax
002F463C  0F 82 55 07 00 00               jb 0x1402f4d97
002F4642  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
002F464B  8B 7D 10                        mov edi, dword ptr [rbp + 0x10]
002F464E  83 FF 01                        cmp edi, 1
002F4651  74 13                           je 0x1402f4666
002F4653  65 8A 04 25 3C 3A 00 00         mov al, byte ptr gs:[0x3a3c]
002F465B  A8 01                           test al, 1
002F465D  0F 85 57 05 00 00               jne 0x1402f4bba
002F4663  8B 7D 10                        mov edi, dword ptr [rbp + 0x10]
002F4666  83 FF 0A                        cmp edi, 0xa
002F4669  0F 85 CC 04 00 00               jne 0x1402f4b3b
002F466F  45 32 C0                        xor r8b, r8b
002F4672  48 8B 85 C0 00 00 00            mov rax, qword ptr [rbp + 0xc0]
002F4679  48 85 C0                        test rax, rax
002F467C  0F 85 9F 06 00 00               jne 0x1402f4d21
002F4682  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
002F4686  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
002F468D  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
002F4691  48 89 8D C8 00 00 00            mov qword ptr [rbp + 0xc8], rcx
002F4698  48 8B 46 58                     mov rax, qword ptr [rsi + 0x58]
002F469C  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
002F46A3  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
002F46A7  48 89 95 D8 00 00 00            mov qword ptr [rbp + 0xd8], rdx
002F46AE  48 8B 86 18 04 00 00            mov rax, qword ptr [rsi + 0x418]
002F46B5  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
002F46BC  48 8B 86 20 04 00 00            mov rax, qword ptr [rsi + 0x420]
002F46C3  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
002F46CA  48 8B 86 08 04 00 00            mov rax, qword ptr [rsi + 0x408]
002F46D1  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
002F46D8  48 8B 86 10 04 00 00            mov rax, qword ptr [rsi + 0x410]
002F46DF  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
002F46E6  41 B0 01                        mov r8b, 1
002F46E9  48 8B 85 C0 00 00 00            mov rax, qword ptr [rbp + 0xc0]
002F46F0  8B 7D 10                        mov edi, dword ptr [rbp + 0x10]
002F46F3  83 FF 0A                        cmp edi, 0xa
002F46F6  0F 87 F0 02 00 00               ja 0x1402f49ec
002F46FC  41 B9 42 04 00 00               mov r9d, 0x442
002F4702  41 0F A3 F9                     bt r9d, edi
002F4706  0F 83 E0 02 00 00               jae 0x1402f49ec
002F470C  45 84 C0                        test r8b, r8b
002F470F  0F 84 D7 02 00 00               je 0x1402f49ec
002F4715  48 89 8D B0 00 00 00            mov qword ptr [rbp + 0xb0], rcx
002F471C  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
002F4723  48 3B D9                        cmp rbx, rcx
002F4726  0F 82 6B 06 00 00               jb 0x1402f4d97
002F472C  48 3B D8                        cmp rbx, rax
002F472F  0F 83 62 06 00 00               jae 0x1402f4d97
002F4735  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
002F4739  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
002F473D  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
002F4741  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
002F4745  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
002F4749  8B 75 0C                        mov esi, dword ptr [rbp + 0xc]
002F474C  E9 82 FA FF FF                  jmp 0x1402f41d3
002F4751  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
002F475B  48 3B C8                        cmp rcx, rax
002F475E  0F 87 0C 03 00 00               ja 0x1402f4a70
002F4764  48 3B 8F 68 01 00 00            cmp rcx, qword ptr [rdi + 0x168]
002F476B  0F 85 F0 02 00 00               jne 0x1402f4a61
002F4771  BE 01 00 00 00                  mov esi, 1
002F4776  89 75 0C                        mov dword ptr [rbp + 0xc], esi
002F4779  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
002F477D  48 85 D2                        test rdx, rdx
002F4780  0F 85 B5 02 00 00               jne 0x1402f4a3b
002F4786  48 83 BD 88 00 00 00 00         cmp qword ptr [rbp + 0x88], 0
002F478E  0F 84 5A 01 00 00               je 0x1402f48ee
002F4794  41 8B 45 30                     mov eax, dword ptr [r13 + 0x30]
002F4798  0D 40 00 10 00                  or eax, 0x100040
002F479D  41 89 45 30                     mov dword ptr [r13 + 0x30], eax
002F47A1  44 89 5D 78                     mov dword ptr [rbp + 0x78], r11d
002F47A5  44 89 5D 28                     mov dword ptr [rbp + 0x28], r11d
002F47A9  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
002F47B3  48 B9 08 07 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000708
002F47BD  8B 09                           mov ecx, dword ptr [rcx]
002F47BF  0B 08                           or ecx, dword ptr [rax]
002F47C1  48 0F BA E1 0B                  bt rcx, 0xb
002F47C6  0F 83 E6 03 00 00               jae 0x1402f4bb2
002F47CC  A1 EC 03 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000003ec]
002F47D5  A9 F8 FF FF FF                  test eax, 0xfffffff8
002F47DA  0F 85 D2 03 00 00               jne 0x1402f4bb2
002F47E0  4C 8B 9D 90 00 00 00            mov r11, qword ptr [rbp + 0x90]
002F47E7  41 8B 13                        mov edx, dword ptr [r11]
002F47EA  4D 63 4B 10                     movsxd r9, dword ptr [r11 + 0x10]
002F47EE  41 3B D1                        cmp edx, r9d
002F47F1  0F 8F B8 03 00 00               jg 0x1402f4baf
002F47F7  45 8B 43 14                     mov r8d, dword ptr [r11 + 0x14]
002F47FB  45 03 C1                        add r8d, r9d
002F47FE  41 03 53 04                     add edx, dword ptr [r11 + 4]
002F4802  41 3B D0                        cmp edx, r8d
002F4805  0F 8C A4 03 00 00               jl 0x1402f4baf
002F480B  4D 8B D1                        mov r10, r9
002F480E  4D 03 D3                        add r10, r11
002F4811  0F 84 98 03 00 00               je 0x1402f4baf
002F4817  A8 02                           test al, 2
002F4819  0F 84 DE 04 00 00               je 0x1402f4cfd
002F481F  4D 8B 42 08                     mov r8, qword ptr [r10 + 8]
002F4823  49 0F BA E0 0B                  bt r8, 0xb
002F4828  0F 83 81 03 00 00               jae 0x1402f4baf
002F482E  48 B8 F8 05 00 00 80 F7 FF FF   movabs rax, 0xfffff780000005f8
002F4838  4C 8B 08                        mov r9, qword ptr [rax]
002F483B  BA 40 02 00 00                  mov edx, 0x240
002F4840  89 55 28                        mov dword ptr [rbp + 0x28], edx
002F4843  B9 02 00 00 00                  mov ecx, 2
002F4848  89 4D 78                        mov dword ptr [rbp + 0x78], ecx
002F484B  83 F9 0B                        cmp ecx, 0xb
002F484E  73 69                           jae 0x1402f48b9
002F4850  48 8B C6                        mov rax, rsi
002F4853  48 D3 E0                        shl rax, cl
002F4856  49 85 C0                        test r8, rax
002F4859  0F 85 45 04 00 00               jne 0x1402f4ca4
002F485F  FF C1                           inc ecx
002F4861  EB E5                           jmp 0x1402f4848
002F4863  49 0F BA E1 0B                  bt r9, 0xb
002F4868  73 0C                           jae 0x1402f4876
002F486A  41 83 C0 3F                     add r8d, 0x3f
002F486E  41 83 E0 C0                     and r8d, 0xffffffc0
002F4872  44 89 45 20                     mov dword ptr [rbp + 0x20], r8d
002F4876  41 8B C0                        mov eax, r8d
002F4879  48 05 08 FE FF FF               add rax, -0x1f8
002F487F  49 03 C2                        add rax, r10
002F4882  45 33 DB                        xor r11d, r11d
002F4885  48 8B 00                        mov rax, qword ptr [rax]
002F4888  48 8B 48 F8                     mov rcx, qword ptr [rax - 8]
002F488C  49 89 8D F8 00 00 00            mov qword ptr [r13 + 0xf8], rcx
002F4893  E9 17 FA FF FF                  jmp 0x1402f42af
002F4898  E9 FC F8 FF FF                  jmp 0x1402f4199
002F489D  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
002F48A7  49 3B C8                        cmp rcx, r8
002F48AA  0F 86 79 F8 FF FF               jbe 0x1402f4129
002F48B0  41 0F B6 00                     movzx eax, byte ptr [r8]
002F48B4  E9 70 F8 FF FF                  jmp 0x1402f4129
002F48B9  49 0F BA E1 0B                  bt r9, 0xb
002F48BE  73 09                           jae 0x1402f48c9
002F48C0  83 C2 3F                        add edx, 0x3f
002F48C3  83 E2 C0                        and edx, 0xffffffc0
002F48C6  89 55 28                        mov dword ptr [rbp + 0x28], edx
002F48C9  44 8B C2                        mov r8d, edx
002F48CC  49 81 C0 00 FE FF FF            add r8, -0x200
002F48D3  4D 03 C2                        add r8, r10
002F48D6  45 33 DB                        xor r11d, r11d
002F48D9  49 89 30                        mov qword ptr [r8], rsi
002F48DC  B9 A7 06 00 00                  mov ecx, 0x6a7
002F48E1  0F 32                           rdmsr
002F48E3  48 C1 E2 20                     shl rdx, 0x20
002F48E7  48 0B C2                        or rax, rdx
002F48EA  49 89 40 08                     mov qword ptr [r8 + 8], rax
002F48EE  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
002F48F5  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
002F48F9  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
002F48FD  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
002F4901  E9 F9 F9 FF FF                  jmp 0x1402f42ff
002F4906  80 7E 2B 02                     cmp byte ptr [rsi + 0x2b], 2
002F490A  0F 84 F1 F7 FF FF               je 0x1402f4101
002F4910  66 83 BE 70 01 00 00 23         cmp word ptr [rsi + 0x170], 0x23
002F4918  0F 85 E3 F7 FF FF               jne 0x1402f4101
002F491E  FF 45 04                        inc dword ptr [rbp + 4]
002F4921  48 8D 96 68 01 00 00            lea rdx, [rsi + 0x168]
002F4928  8B 86 80 01 00 00               mov eax, dword ptr [rsi + 0x180]
002F492E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002F4932  8B 86 58 01 00 00               mov eax, dword ptr [rsi + 0x158]
002F4938  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002F493C  8B 45 4C                        mov eax, dword ptr [rbp + 0x4c]
002F493F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
002F4943  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
002F4946  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002F494A  4C 8D 4D 04                     lea r9, [rbp + 4]
002F494E  4D 8B C7                        mov r8, r15
002F4951  48 8B 8D A8 00 00 00            mov rcx, qword ptr [rbp + 0xa8]
002F4958  E8 53 4C 11 00                  call 0x1404095b0
002F495D  84 C0                           test al, al
002F495F  0F 84 9C F7 FF FF               je 0x1402f4101
002F4965  E9 6B 04 00 00                  jmp 0x1402f4dd5
002F496A  45 85 F6                        test r14d, r14d
002F496D  0F 84 A9 03 00 00               je 0x1402f4d1c
002F4973  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002F497C  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
002F4983  E8 A8 D7 5D 00                  call 0x1408d2130
002F4988  B9 4C 01 00 00                  mov ecx, 0x14c
002F498D  66 3B C1                        cmp ax, cx
002F4990  0F 85 86 03 00 00               jne 0x1402f4d1c
002F4996  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
002F499A  80 78 2B 02                     cmp byte ptr [rax + 0x2b], 2
002F499E  0F 85 78 03 00 00               jne 0x1402f4d1c
002F49A4  0F 57 C0                        xorps xmm0, xmm0
002F49A7  0F 11 85 28 01 00 00            movups xmmword ptr [rbp + 0x128], xmm0
002F49AE  0F 11 85 38 01 00 00            movups xmmword ptr [rbp + 0x138], xmm0
002F49B5  0F 11 85 48 01 00 00            movups xmmword ptr [rbp + 0x148], xmm0
002F49BC  4C 8D 85 28 01 00 00            lea r8, [rbp + 0x128]
002F49C3  49 8B 8F 88 14 00 00            mov rcx, qword ptr [r15 + 0x1488]
002F49CA  E8 3D 94 5D 00                  call 0x1408cde0c
002F49CF  85 C0                           test eax, eax
002F49D1  0F 88 45 03 00 00               js 0x1402f4d1c
002F49D7  48 8B 85 28 01 00 00            mov rax, qword ptr [rbp + 0x128]
002F49DE  A8 03                           test al, 3
002F49E0  0F 84 8F 00 00 00               je 0x1402f4a75
002F49E6  E8 E5 55 5A 00                  call 0x140899fd0
002F49EB  CC                              int3
002F49EC  48 83 7A 10 00                  cmp qword ptr [rdx + 0x10], 0
002F49F1  0F 84 A0 03 00 00               je 0x1402f4d97
002F49F7  0F 10 52 10                     movups xmm2, xmmword ptr [rdx + 0x10]
002F49FB  0F 29 95 C0 00 00 00            movaps xmmword ptr [rbp + 0xc0], xmm2
002F4A02  0F 10 42 20                     movups xmm0, xmmword ptr [rdx + 0x20]
002F4A06  0F 29 85 D0 00 00 00            movaps xmmword ptr [rbp + 0xd0], xmm0
002F4A0D  0F 10 4A 30                     movups xmm1, xmmword ptr [rdx + 0x30]
002F4A11  0F 29 8D E0 00 00 00            movaps xmmword ptr [rbp + 0xe0], xmm1
002F4A18  0F 10 42 40                     movups xmm0, xmmword ptr [rdx + 0x40]
002F4A1C  0F 29 85 F0 00 00 00            movaps xmmword ptr [rbp + 0xf0], xmm0
002F4A23  66 0F 6F CA                     movdqa xmm1, xmm2
002F4A27  66 0F 73 D9 08                  psrldq xmm1, 8
002F4A2C  66 48 0F 7E C9                  movq rcx, xmm1
002F4A31  66 48 0F 7E D0                  movq rax, xmm2
002F4A36  E9 DA FC FF FF                  jmp 0x1402f4715
002F4A3B  48 8B BA D0 00 00 00            mov rdi, qword ptr [rdx + 0xd0]
002F4A42  48 89 7D 38                     mov qword ptr [rbp + 0x38], rdi
002F4A46  41 8B C3                        mov eax, r11d
002F4A49  49 3B F8                        cmp rdi, r8
002F4A4C  0F 93 C0                        setae al
002F4A4F  85 C0                           test eax, eax
002F4A51  0F 85 2F FD FF FF               jne 0x1402f4786
002F4A57  E9 79 03 00 00                  jmp 0x1402f4dd5
002F4A5C  E9 74 03 00 00                  jmp 0x1402f4dd5
002F4A61  E9 6F 03 00 00                  jmp 0x1402f4dd5
002F4A66  E9 6A 03 00 00                  jmp 0x1402f4dd5
002F4A6B  E9 65 03 00 00                  jmp 0x1402f4dd5
002F4A70  E9 60 03 00 00                  jmp 0x1402f4dd5
002F4A75  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
002F4A7F  48 3B C1                        cmp rax, rcx
002F4A82  48 0F 43 C1                     cmovae rax, rcx
002F4A86  90                              nop
002F4A87  0F B6 00                        movzx eax, byte ptr [rax]
002F4A8A  48 8B 8D 28 01 00 00            mov rcx, qword ptr [rbp + 0x128]
002F4A91  8B 81 C4 00 00 00               mov eax, dword ptr [rcx + 0xc4]
002F4A97  83 E8 04                        sub eax, 4
002F4A9A  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002F4A9E  8B 81 B4 00 00 00               mov eax, dword ptr [rcx + 0xb4]
002F4AA4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002F4AA8  8B 45 4C                        mov eax, dword ptr [rbp + 0x4c]
002F4AAB  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
002F4AAF  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
002F4AB2  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002F4AB6  4C 8D 4D 04                     lea r9, [rbp + 4]
002F4ABA  4D 8B C7                        mov r8, r15
002F4ABD  33 D2                           xor edx, edx
002F4ABF  48 8B 8D A8 00 00 00            mov rcx, qword ptr [rbp + 0xa8]
002F4AC6  E8 E5 4A 11 00                  call 0x1404095b0
002F4ACB  84 C0                           test al, al
002F4ACD  0F 84 49 02 00 00               je 0x1402f4d1c
002F4AD3  E9 FD 02 00 00                  jmp 0x1402f4dd5
002F4AD8  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
002F4AE2  49 3B C0                        cmp rax, r8
002F4AE5  49 0F 43 C0                     cmovae rax, r8
002F4AE9  90                              nop
002F4AEA  0F B6 00                        movzx eax, byte ptr [rax]
002F4AED  BE 01 00 00 00                  mov esi, 1
002F4AF2  89 75 0C                        mov dword ptr [rbp + 0xc], esi
002F4AF5  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
002F4AFC  48 8B 48 48                     mov rcx, qword ptr [rax + 0x48]
002F4B00  49 89 8D 98 00 00 00            mov qword ptr [r13 + 0x98], rcx
002F4B07  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
002F4B0E  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
002F4B12  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
002F4B16  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
002F4B1A  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
002F4B1E  48 89 55 40                     mov qword ptr [rbp + 0x40], rdx
002F4B22  48 85 D2                        test rdx, rdx
002F4B25  0F 84 63 02 00 00               je 0x1402f4d8e
002F4B2B  48 8B BA D0 00 00 00            mov rdi, qword ptr [rdx + 0xd0]
002F4B32  48 89 7D 38                     mov qword ptr [rbp + 0x38], rdi
002F4B36  E9 C4 F7 FF FF                  jmp 0x1402f42ff
002F4B3B  E8 F0 34 00 00                  call 0x1402f8030
002F4B40  3C 02                           cmp al, 2
002F4B42  0F 82 27 FB FF FF               jb 0x1402f466f
002F4B48  65 48 8B 0C 25 E8 88 00 00      mov rcx, qword ptr gs:[0x88e8]
002F4B51  48 83 C1 50                     add rcx, 0x50
002F4B55  8B 05 21 05 CD 00               mov eax, dword ptr [rip + 0xcd0521]
002F4B5B  48 8B D1                        mov rdx, rcx
002F4B5E  48 2B D0                        sub rdx, rax
002F4B61  48 3B D9                        cmp rbx, rcx
002F4B64  0F 83 32 01 00 00               jae 0x1402f4c9c
002F4B6A  48 3B D3                        cmp rdx, rbx
002F4B6D  0F 87 29 01 00 00               ja 0x1402f4c9c
002F4B73  48 89 4D 30                     mov qword ptr [rbp + 0x30], rcx
002F4B77  48 89 55 18                     mov qword ptr [rbp + 0x18], rdx
002F4B7B  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
002F4B7F  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
002F4B83  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
002F4B87  8B 75 0C                        mov esi, dword ptr [rbp + 0xc]
002F4B8A  E9 44 F6 FF FF                  jmp 0x1402f41d3
002F4B8F  45 33 DB                        xor r11d, r11d
002F4B92  B8 08 00 00 00                  mov eax, 8
002F4B97  E9 E9 FC FF FF                  jmp 0x1402f4885
002F4B9C  E9 34 02 00 00                  jmp 0x1402f4dd5
002F4BA1  48 85 D2                        test rdx, rdx
002F4BA4  0F 85 4C F6 FF FF               jne 0x1402f41f6
002F4BAA  E9 26 02 00 00                  jmp 0x1402f4dd5
002F4BAF  45 33 DB                        xor r11d, r11d
002F4BB2  4D 8B C3                        mov r8, r11
002F4BB5  E9 1F FD FF FF                  jmp 0x1402f48d9
002F4BBA  65 48 8B 0C 25 20 3A 00 00      mov rcx, qword ptr gs:[0x3a20]
002F4BC3  48 83 C1 50                     add rcx, 0x50
002F4BC7  8B 05 07 06 CD 00               mov eax, dword ptr [rip + 0xcd0607]
002F4BCD  48 8B D1                        mov rdx, rcx
002F4BD0  48 2B D0                        sub rdx, rax
002F4BD3  48 3B D3                        cmp rdx, rbx
002F4BD6  0F 87 87 FA FF FF               ja 0x1402f4663
002F4BDC  48 3B D9                        cmp rbx, rcx
002F4BDF  0F 83 7E FA FF FF               jae 0x1402f4663
002F4BE5  48 89 4D 30                     mov qword ptr [rbp + 0x30], rcx
002F4BE9  48 89 55 18                     mov qword ptr [rbp + 0x18], rdx
002F4BED  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
002F4BF1  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
002F4BF5  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
002F4BF9  8B 75 0C                        mov esi, dword ptr [rbp + 0xc]
002F4BFC  E9 D2 F5 FF FF                  jmp 0x1402f41d3
002F4C01  49 0F BA E2 0B                  bt r10, 0xb
002F4C06  73 0C                           jae 0x1402f4c14
002F4C08  41 83 C1 3F                     add r9d, 0x3f
002F4C0C  41 83 E1 C0                     and r9d, 0xffffffc0
002F4C10  44 89 4D 24                     mov dword ptr [rbp + 0x24], r9d
002F4C14  41 8B C1                        mov eax, r9d
002F4C17  48 05 00 FE FF FF               add rax, -0x200
002F4C1D  49 03 C0                        add rax, r8
002F4C20  4C 89 18                        mov qword ptr [rax], r11
002F4C23  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
002F4C28  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
002F4C2C  48 89 4D 58                     mov qword ptr [rbp + 0x58], rcx
002F4C30  49 8B 4C 24 28                  mov rcx, qword ptr [r12 + 0x28]
002F4C35  48 85 C9                        test rcx, rcx
002F4C38  0F 84 1E FE FF FF               je 0x1402f4a5c
002F4C3E  48 89 4D 60                     mov qword ptr [rbp + 0x60], rcx
002F4C42  49 8B 85 98 00 00 00            mov rax, qword ptr [r13 + 0x98]
002F4C49  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
002F4C4D  48 8B 01                        mov rax, qword ptr [rcx]
002F4C50  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
002F4C54  E9 A6 F6 FF FF                  jmp 0x1402f42ff
002F4C59  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
002F4C5D  48 89 4D 60                     mov qword ptr [rbp + 0x60], rcx
002F4C61  E9 CB F4 FF FF                  jmp 0x1402f4131
002F4C66  49 85 C1                        test r9, rax
002F4C69  74 0C                           je 0x1402f4c77
002F4C6B  41 83 C0 3F                     add r8d, 0x3f
002F4C6F  41 83 E0 C0                     and r8d, 0xffffffc0
002F4C73  44 89 45 20                     mov dword ptr [rbp + 0x20], r8d
002F4C77  8B C1                           mov eax, ecx
002F4C79  49 BB 04 06 00 00 80 F7 FF FF   movabs r11, 0xfffff78000000604
002F4C83  45 03 04 83                     add r8d, dword ptr [r11 + rax*4]
002F4C87  44 89 45 20                     mov dword ptr [rbp + 0x20], r8d
002F4C8B  E9 19 F9 FF FF                  jmp 0x1402f45a9
002F4C90  E9 40 01 00 00                  jmp 0x1402f4dd5
002F4C95  33 C0                           xor eax, eax
002F4C97  E9 45 01 00 00                  jmp 0x1402f4de1
002F4C9C  8B 7D 10                        mov edi, dword ptr [rbp + 0x10]
002F4C9F  E9 CB F9 FF FF                  jmp 0x1402f466f
002F4CA4  49 85 C1                        test r9, rax
002F4CA7  74 09                           je 0x1402f4cb2
002F4CA9  83 C2 3F                        add edx, 0x3f
002F4CAC  83 E2 C0                        and edx, 0xffffffc0
002F4CAF  89 55 28                        mov dword ptr [rbp + 0x28], edx
002F4CB2  8B C1                           mov eax, ecx
002F4CB4  49 BB 04 06 00 00 80 F7 FF FF   movabs r11, 0xfffff78000000604
002F4CBE  41 03 14 83                     add edx, dword ptr [r11 + rax*4]
002F4CC2  89 55 28                        mov dword ptr [rbp + 0x28], edx
002F4CC5  E9 95 FB FF FF                  jmp 0x1402f485f
002F4CCA  48 B8 48 04 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000448
002F4CD4  8B 00                           mov eax, dword ptr [rax]
002F4CD6  48 05 08 FE FF FF               add rax, -0x1f8
002F4CDC  49 03 C2                        add rax, r10
002F4CDF  45 33 DB                        xor r11d, r11d
002F4CE2  48 8B 00                        mov rax, qword ptr [rax]
002F4CE5  48 8B 48 F8                     mov rcx, qword ptr [rax - 8]
002F4CE9  49 89 8D F8 00 00 00            mov qword ptr [r13 + 0xf8], rcx
002F4CF0  E9 BA F5 FF FF                  jmp 0x1402f42af
002F4CF5  49 8B C3                        mov rax, r11
002F4CF8  E9 23 FF FF FF                  jmp 0x1402f4c20
002F4CFD  48 B8 48 04 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000448
002F4D07  44 8B 00                        mov r8d, dword ptr [rax]
002F4D0A  49 81 C0 00 FE FF FF            add r8, -0x200
002F4D11  4D 03 C2                        add r8, r10
002F4D14  45 33 DB                        xor r11d, r11d
002F4D17  E9 BD FB FF FF                  jmp 0x1402f48d9
002F4D1C  E9 B4 00 00 00                  jmp 0x1402f4dd5
002F4D21  48 8B 95 D8 00 00 00            mov rdx, qword ptr [rbp + 0xd8]
002F4D28  48 8B 8D C8 00 00 00            mov rcx, qword ptr [rbp + 0xc8]
002F4D2F  E9 BF F9 FF FF                  jmp 0x1402f46f3
002F4D34  49 85 C2                        test r10, rax
002F4D37  74 0C                           je 0x1402f4d45
002F4D39  41 83 C1 3F                     add r9d, 0x3f
002F4D3D  41 83 E1 C0                     and r9d, 0xffffffc0
002F4D41  44 89 4D 24                     mov dword ptr [rbp + 0x24], r9d
002F4D45  8B C1                           mov eax, ecx
002F4D47  48 BB 04 06 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000604
002F4D51  44 03 0C 83                     add r9d, dword ptr [rbx + rax*4]
002F4D55  44 89 4D 24                     mov dword ptr [rbp + 0x24], r9d
002F4D59  E9 74 F7 FF FF                  jmp 0x1402f44d2
002F4D5E  48 B8 48 04 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000448
002F4D68  8B 00                           mov eax, dword ptr [rax]
002F4D6A  48 05 00 FE FF FF               add rax, -0x200
002F4D70  49 03 C0                        add rax, r8
002F4D73  E9 A8 FE FF FF                  jmp 0x1402f4c20
002F4D78  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
002F4D7C  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
002F4D80  4C 8B BD 80 00 00 00            mov r15, qword ptr [rbp + 0x80]
002F4D87  E9 DA F3 FF FF                  jmp 0x1402f4166
002F4D8C  EB 47                           jmp 0x1402f4dd5
002F4D8E  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
002F4D92  E9 68 F5 FF FF                  jmp 0x1402f42ff
002F4D97  EB 3C                           jmp 0x1402f4dd5
002F4D99  C7 45 04 00 00 00 00            mov dword ptr [rbp + 4], 0
002F4DA0  44 8B B5 A0 00 00 00            mov r14d, dword ptr [rbp + 0xa0]
002F4DA7  EB 2C                           jmp 0x1402f4dd5
002F4DA9  A1 EC 03 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000003ec]
002F4DB2  49 B8 D8 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003d8
002F4DBC  A8 02                           test al, 2
002F4DBE  75 63                           jne 0x1402f4e23
002F4DC0  49 8B D0                        mov rdx, r8
002F4DC3  49 8B CC                        mov rcx, r12
002F4DC6  E8 41 A4 1F 00                  call 0x1404ef20c
002F4DCB  05 20 03 00 00                  add eax, 0x320
002F4DD0  E9 3B F2 FF FF                  jmp 0x1402f4010
002F4DD5  45 85 F6                        test r14d, r14d
002F4DD8  0F 85 C7 00 00 00               jne 0x1402f4ea5
002F4DDE  8B 45 04                        mov eax, dword ptr [rbp + 4]
002F4DE1  48 8B 8D 60 01 00 00            mov rcx, qword ptr [rbp + 0x160]
002F4DE8  48 33 CD                        xor rcx, rbp
002F4DEB  E8 50 78 3B 00                  call 0x1406ac640
002F4DF0  48 8B 9D A0 01 00 00            mov rbx, qword ptr [rbp + 0x1a0]
002F4DF7  48 8B B5 A8 01 00 00            mov rsi, qword ptr [rbp + 0x1a8]
002F4DFE  48 8B BD B0 01 00 00            mov rdi, qword ptr [rbp + 0x1b0]
002F4E05  48 8D A5 70 01 00 00            lea rsp, [rbp + 0x170]
002F4E0C  41 5F                           pop r15
002F4E0E  41 5E                           pop r14
002F4E10  41 5D                           pop r13
002F4E12  41 5C                           pop r12
002F4E14  5D                              pop rbp
002F4E15  C3                              ret
002F4E16  CC                              int3
002F4E17  4C 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], r8
002F4E1E  E9 6F F1 FF FF                  jmp 0x1402f3f92
002F4E23  49 BD 08 07 00 00 80 F7 FF FF   movabs r13, 0xfffff78000000708
002F4E2D  49 8B 08                        mov rcx, qword ptr [r8]
002F4E30  49 0B 4D 00                     or rcx, qword ptr [r13]
002F4E34  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
002F4E3E  48 0B C8                        or rcx, rax
002F4E41  48 23 CE                        and rcx, rsi
002F4E44  48 89 4D 68                     mov qword ptr [rbp + 0x68], rcx
002F4E48  48 8D 55 68                     lea rdx, [rbp + 0x68]
002F4E4C  41 8B CF                        mov ecx, r15d
002F4E4F  E8 A8 E4 FF FF                  call 0x1402f32fc
002F4E54  4C 8B 65 68                     mov r12, qword ptr [rbp + 0x68]
002F4E58  E9 63 FF FF FF                  jmp 0x1402f4dc0
002F4E5D  F6 05 90 03 CD 00 01            test byte ptr [rip + 0xcd0390], 1
002F4E64  41 8B C3                        mov eax, r11d
002F4E67  B9 00 00 00 80                  mov ecx, 0x80000000
002F4E6C  0F 44 C1                        cmove eax, ecx
002F4E6F  89 45 48                        mov dword ptr [rbp + 0x48], eax
002F4E72  E9 1B F2 FF FF                  jmp 0x1402f4092
002F4E77  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002F4E80  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002F4E87  F7 81 54 07 00 00 00 40 00 00   test dword ptr [rcx + 0x754], 0x4000
002F4E91  48 0F 45 15 67 26 CD 00         cmovne rdx, qword ptr [rip + 0xcd2667]
002F4E99  48 89 95 88 00 00 00            mov qword ptr [rbp + 0x88], rdx
002F4EA0  E9 13 F1 FF FF                  jmp 0x1402f3fb8
002F4EA5  80 7D 09 00                     cmp byte ptr [rbp + 9], 0
002F4EA9  0F 85 2F FF FF FF               jne 0x1402f4dde
002F4EAF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002F4EB8  80 60 7D FB                     and byte ptr [rax + 0x7d], 0xfb
002F4EBC  E9 1D FF FF FF                  jmp 0x1402f4dde
002F4EC1  33 C0                           xor eax, eax
002F4EC3  E9 19 FF FF FF                  jmp 0x1402f4de1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpWalkFrameChain(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m124;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned __int8 v_stack_m18F;
    unsigned __int8 v_stack_m190;
    unsigned int v_stack_m194;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (464);
    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    result = (*(unsigned __int64 *)(v_rip + 11626558)) ^ (v_stack_m198);
    v_stack_m38 = result;
    v_stack_m14C = a4;
    v_stack_m148 = a2;
    v_stack_mF0 = a1;
    a3 = 0;
    v_stack_m108 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_m150 = 0;
    v_stack_m168 = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_m180 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    v_stack_m18F = 1;
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x400ULL)) != 0) goto loc_002F4E17;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_002F4E17;
    v_stack_m118 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240);
loc_002F3F92:
    v_stack_m160 = 0;
    v_stack_m18C = 0;
    v_stack_m110 = 0;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (1));
    v_stack_mF8 = (unsigned int)(v_r14);
    if (condition_is_not_equal) goto loc_002F4E77;
loc_002F3FB8:
    result = -(0);
    v_rsi = (unsigned int)((v_rsi) & (0x800ULL));
    result = -(0);
    a1 = (unsigned int)((*(unsigned __int64 *)(gs_base + (0 + 392))) & (64));
    v_stack_m194 = 0;
    result = RtlpValidateContextFlags2((unsigned int)((unsigned int)(a1 + 1048587)), v_stack_m194, result, a4);
    if (sign_flag) goto loc_002F401D;
    if ((((unsigned __int8)((unsigned int)(v_stack_m194))) & (2)) != 0) goto loc_002F4DA9;
loc_002F4010:
    v_rbx = (unsigned int)(0x4F0ULL) + 32;
    if ((((unsigned __int8)((unsigned int)(v_stack_m194))) & (4)) == 0) { v_rbx = (unsigned int)((unsigned int)(0x4F0ULL)); }
    v_rbx = (unsigned int)((v_rbx) + (15));
loc_002F401D:
    if (((unsigned int)((unsigned int)(v_rbx)) + 15) <= ((unsigned int)((unsigned int)(v_rbx)))) {
    }
    a1 = ((unsigned int)((unsigned int)(v_rbx)) + 15) & (-16);
    result = _chkstk(a1, v_stack_m194, result, a4);
    v_rsp = (v_rsp) - (a1);
    result = RtlInitializeExtendedContext2(v_stack_m198, (unsigned int)((unsigned int)(a1 + 1048587)), v_stack_m108, v_rsi);
    result = RtlpCaptureContext2(v_stack_m198, (unsigned int)((unsigned int)(a1 + 1048587)), v_stack_m108, v_rsi);
    v_stack_m190 = 0;
    result = RtlpGetStackLimits(v_stack_m180, v_stack_m168, v_stack_m108, v_rsi);
    if ((unsigned __int8)(result) == 0) goto loc_002F4EC1;
    v_r11 = 0;
    v_stack_m194 = 0;
    v_rdi = (unsigned int)(((unsigned int)(a3)) >> (1));
    v_rdi = (unsigned __int8)((v_rdi) & (1));
    if ((unsigned int)(v_r14) == 0) goto loc_002F4E5D;
loc_002F4092:
    v_stack_m100 = 0;
    v_stack_m130 = 0;
    if ((unsigned int)(v_r14) == 0) goto loc_002F4D78;
loc_002F40B3:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40) + 8)) & (1)) != 0) goto loc_002F4333;
    v_stack_m160 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40) - 400;
    if (v_stack_m118 == 0) goto loc_002F40E0;
    if (condition_is_above_or_equal) goto loc_002F40E7;
loc_002F40E0:
    result = 0;
    goto loc_002F4DE1;
loc_002F40E7:
    result = PsWow64GetProcessMachine(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m168, v_stack_m108, v_rsi);
    if (((unsigned __int16)(result)) == 332) goto loc_002F4906;
loc_002F4101:
    v_stack_m100 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40) - 400 + 384);
    v_stack_m130 = *(unsigned __int64 *)(v_stack_m118 + 8);
    if ((*(unsigned __int64 *)(v_stack_m118 + 8)) <= (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40) - 400 + 384))) goto loc_002F4C95;
    if ((*(unsigned __int64 *)(v_stack_m118 + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40) - 400 + 384))) goto loc_002F489D;
loc_002F4129:
    v_stack_m138 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40);
loc_002F4131:
    if (((*(unsigned __int8 *)(v_stack_m138 + 8)) & (1)) != 0) goto loc_002F4C59;
    v_stack_m158 = *(unsigned __int64 *)(v_stack_m138 + 32);
    v_stack_m140 = *(unsigned __int64 *)(v_stack_m138 + 32);
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 125))) >> (2));
    result = (unsigned __int8)((result) & (1));
    v_stack_m18F = (unsigned __int8)(result);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 125)) | (4));
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 125) = (unsigned __int8)(a1);
    v_r11 = 0;
loc_002F4166:
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm1;
    v_stack_m198 = (unsigned __int8)(v_rdi);
loc_002F418F:
loc_002F4199:
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    v_stack_m188 = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m198 + 152))) & (7)) != 0) goto loc_002F4D97;
    if ((*(unsigned __int64 *)(v_stack_m198 + 152)) < v_stack_m180) goto loc_002F45FB;
    if ((*(unsigned __int64 *)(v_stack_m198 + 152)) >= v_stack_m168) goto loc_002F45FB;
loc_002F41D3:
    result = RtlpLookupFunctionEntryForStackWalks(*(unsigned __int64 *)(v_stack_m198 + 248), v_stack_m70, v_stack_m108, v_rsi);
    if (result == 0) goto loc_002F4BA1;
loc_002F41F6:
    a1 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = 0;
    a4 = 0;
    v_stack_m78 = 0;
    v_stack_m88 = v_stack_m180;
    v_stack_m80 = v_stack_m168;
    v_stack_m1A8 = 0;
    v_stack_m1B0 = v_stack_m88;
    v_stack_m1B8 = 0;
    v_stack_m1C0 = v_stack_m98;
    v_stack_m1C8 = v_stack_m90;
    v_stack_m1D0 = v_stack_m190;
    v_stack_m1D8 = v_stack_m198;
    result = RtlpxVirtualUnwind((unsigned int)(v_stack_m150), v_stack_m68, *(unsigned __int64 *)(v_stack_m198 + 248), result);
    if (sign_flag) goto loc_002F4B9C;
    result = v_stack_m198;
    if (v_stack_m190 != 0) { result = 0; }
    v_stack_m198 = (unsigned __int8)(result);
    if (((unsigned int)((unsigned int)(v_stack_m18C))) != 1) goto loc_002F42AF;
    if (v_stack_m194 <= 0) goto loc_002F42AF;
    if (v_stack_m110 != 0) goto loc_002F44D6;
loc_002F42AF:
    if (*(unsigned __int64 *)(v_stack_m198 + 248) == 0) goto loc_002F496A;
    if ((unsigned int)((unsigned int)(v_stack_m18C)) != 0) goto loc_002F433C;
    if ((unsigned int)(v_r14) != 0) goto loc_002F42EC;
    if ((*(unsigned __int64 *)(v_stack_m198 + 248)) < (*(unsigned __int64 *)(v_stack_m198 + 248))) goto loc_002F4C90;
    if ((unsigned int)(v_r14) != 0) goto loc_002F42EC;
    if (v_stack_m198 != ((unsigned __int8)(v_r14))) goto loc_002F45B2;
    goto loc_002F42FF;
loc_002F42EC:
    if ((*(unsigned __int64 *)(v_stack_m198 + 248)) < (*(unsigned __int64 *)(v_stack_m198 + 248))) goto loc_002F4751;
    if (v_stack_m194 != 0) goto loc_002F4898;
loc_002F42FF:
    result = (unsigned int)(v_stack_m194);
    if (((unsigned int)((unsigned int)(v_stack_m194))) >= ((unsigned int)((unsigned int)(v_stack_m14C)))) {
        a1 = *(unsigned __int64 *)(v_stack_m198 + 248);
        result = (unsigned int)(((unsigned int)(v_stack_m194)) - ((unsigned int)((unsigned int)(v_stack_m14C))));
        a2 = v_stack_mF0;
        *(unsigned __int64 *)(a2 + result * 8) = a1;
    }
    result = (unsigned int)(((unsigned int)(v_stack_m194)) + 1);
    v_stack_m194 = (unsigned int)(result);
    if (((unsigned int)(result)) >= v_stack_m148) goto loc_002F45AD;
    goto loc_002F418F;
loc_002F4333:
    goto loc_002F40B3;
loc_002F433C:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m18C)))) - (1));
    if (condition_is_not_equal) goto loc_002F45B7;
    if (a1 > (*(unsigned __int64 *)(result + 40))) goto loc_002F4A6B;
    if (v_stack_m158 == 0) goto loc_002F42FF;
    if (a1 != (*(unsigned __int64 *)(v_stack_m160 + 360))) goto loc_002F42FF;
    v_stack_m18C = 2;
    *(unsigned __int64 *)(v_stack_m198 + 248) = *(unsigned __int64 *)(v_stack_m158 + 312);
    *(unsigned __int64 *)(v_stack_m198 + 152) = v_stack_m158 + 320;
    *(unsigned __int64 *)(v_stack_m198 + 160) = *(unsigned __int64 *)(v_stack_m158 + 248);
    *(unsigned __int64 *)(v_stack_m198 + 144) = *(unsigned __int64 *)(v_stack_m158 + 256);
    *(unsigned __int64 *)(v_stack_m198 + 176) = *(unsigned __int64 *)(v_stack_m158 + 264);
    *(unsigned __int64 *)(v_stack_m198 + 168) = *(unsigned __int64 *)(v_stack_m158 + 272);
    *(unsigned __int64 *)(v_stack_m198 + 216) = *(unsigned __int64 *)(v_stack_m158 + 280);
    *(unsigned __int64 *)(v_stack_m198 + 224) = *(unsigned __int64 *)(v_stack_m158 + 288);
    *(unsigned __int64 *)(v_stack_m198 + 232) = *(unsigned __int64 *)(v_stack_m158 + 296);
    *(unsigned __int64 *)(v_stack_m198 + 240) = *(unsigned __int64 *)(v_stack_m158 + 304);
    if (v_stack_m110 == 0) goto loc_002F4C23;
    v_stack_m124 = 0;
    v_stack_m174 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) | (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m158 + 304))));
    if (condition_is_above_or_equal) goto loc_002F4CF5;
    if ((((unsigned int)(*(unsigned __int64 *)(v_stack_m158 + 304))) & (0xFFFFFFF8ULL)) != 0) goto loc_002F4CF5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m108)))) > ((unsigned int)((int)(*(unsigned int *)(v_stack_m108 + 16))))) goto loc_002F4CF5;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m108 + 20))) + ((unsigned int)((int)(*(unsigned int *)(v_stack_m108 + 16)))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m108))) + (*(unsigned int *)(v_stack_m108 + 4)));
    if (a2 < a3) goto loc_002F4CF5;
    a3 = ((int)(*(unsigned int *)(v_stack_m108 + 16))) + (v_stack_m108);
    if (condition_is_equal) goto loc_002F4CF5;
    if (((2) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m158 + 304)))) == 0) goto loc_002F4D5E;
    if (condition_is_above_or_equal) goto loc_002F4CF5;
    v_stack_m174 = 576;
loc_002F44B5:
    v_stack_m124 = 2;
    if (2 >= 11) goto loc_002F4C01;
    result = (1) << (2);
    if (((*(unsigned __int64 *)(a3 + 8)) & (result)) != 0) goto loc_002F4D34;
loc_002F44D2:
    a1 = (unsigned int)((2) + 1);
    goto loc_002F44B5;
loc_002F44D6:
    if ((*(unsigned __int64 *)(v_stack_m198 + 248)) != result) goto loc_002F42AF;
    v_stack_m128 = 0;
    v_stack_m178 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) | (*(unsigned int *)(result)));
    if (condition_is_above_or_equal) goto loc_002F4B92;
    if ((((unsigned int)(result)) & (0xFFFFFFF8ULL)) != 0) goto loc_002F4B92;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m108)))) > ((unsigned int)((int)(*(unsigned int *)(v_stack_m108 + 16))))) goto loc_002F4B8F;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m108 + 20))) + ((unsigned int)((int)(*(unsigned int *)(v_stack_m108 + 16)))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m108))) + (*(unsigned int *)(v_stack_m108 + 4)));
    if (a2 < a3) goto loc_002F4B8F;
    v_r10 = ((int)(*(unsigned int *)(v_stack_m108 + 16))) + (v_stack_m108);
    if (condition_is_equal) goto loc_002F4B8F;
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_002F4CCA;
    if (condition_is_above_or_equal) goto loc_002F4B8F;
    v_stack_m178 = 576;
loc_002F458C:
    v_stack_m128 = 2;
    if (2 >= 11) goto loc_002F4863;
    result = (1) << (2);
    if (((*(unsigned __int64 *)(v_r10 + 8)) & (result)) != 0) goto loc_002F4C66;
loc_002F45A9:
    a1 = (unsigned int)((2) + 1);
    goto loc_002F458C;
loc_002F45AD:
    goto loc_002F4DD5;
loc_002F45B2:
    goto loc_002F4199;
loc_002F45B7:
    if (((unsigned int)(*(unsigned __int64 *)(v_r10 + 8))) != 1) goto loc_002F4A66;
    if (a1 > result) goto loc_002F42FF;
    if (a1 != (*(unsigned __int64 *)(v_stack_m160 + 360))) goto loc_002F4D8C;
    v_stack_m118 = *(unsigned __int64 *)(v_stack_m160 + 384);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m160 + 384))) & (3)) != 0) goto loc_002F49E6;
    goto loc_002F4AD8;
loc_002F45FB:
    result = (v_stack_m180 >= 576) ? 1 : 0;
    if ((unsigned int)(result) == 0) goto loc_002F4D97;
    result = KeGetCurrentStackPointer(a1, *(unsigned __int64 *)(v_r10 + 8), 576, *(unsigned __int64 *)(result));
    result = KeQueryCurrentStackInformationEx(result, v_stack_m188, v_stack_mE8, v_stack_mE0);
    if (((unsigned int)((unsigned int)(v_stack_m188))) > 9) goto loc_002F4642;
    if (((unsigned int)((unsigned int)(v_stack_m188))) < 9) goto loc_002F4D97;
loc_002F4642:
    if (((unsigned int)((unsigned int)(v_stack_m188))) == 1) goto loc_002F4666;
    if ((((unsigned __int8)(*(unsigned __int8 *)(gs_base + (0 + 14908)))) & (1)) != 0) goto loc_002F4BBA;
loc_002F4663:
loc_002F4666:
    if (((unsigned int)((unsigned int)(v_stack_m188))) != 10) goto loc_002F4B3B;
loc_002F466F:
    a3 = 0;
    if (v_stack_mD8 != 0) goto loc_002F4D21;
    v_stack_mD8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 56);
    v_stack_mD0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 48);
    v_stack_mC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 88);
    v_stack_mC0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40);
    v_stack_mB8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1048);
    v_stack_mB0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1056);
    v_stack_mA8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1032);
    v_stack_mA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1040);
loc_002F46F3:
    if (((unsigned int)((unsigned int)(v_stack_m188))) > 10) goto loc_002F49EC;
    if (((unsigned int)((unsigned int)(v_stack_m188))) >= 10) goto loc_002F49EC;
    if (1 == 0) goto loc_002F49EC;
loc_002F4715:
    v_stack_mE8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 48);
    v_stack_mE0 = v_stack_mD8;
    if ((*(unsigned __int64 *)(v_stack_m198 + 152)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 48))) goto loc_002F4D97;
    if ((*(unsigned __int64 *)(v_stack_m198 + 152)) >= v_stack_mD8) goto loc_002F4D97;
    v_stack_m180 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 48);
    v_stack_m168 = v_stack_mD8;
    v_stack_m158 = v_stack_m140;
    goto loc_002F41D3;
loc_002F4751:
    if (v_stack_m140 > v_stack_mD8) goto loc_002F4A70;
    if (v_stack_m140 != (*(unsigned __int64 *)(v_stack_m160 + 360))) goto loc_002F4A61;
    v_stack_m18C = 1;
    if (v_stack_m158 != 0) goto loc_002F4A3B;
loc_002F4786:
    if (v_stack_m110 == 0) goto loc_002F48EE;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m198 + 48))) | (0x100040ULL));
    *(unsigned int *)(v_stack_m198 + 48) = (unsigned int)(result);
    v_stack_m120 = (unsigned int)(v_stack_m108);
    v_stack_m170 = (unsigned int)(v_stack_m108);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m140))) | (*(unsigned int *)(result)));
    if (condition_is_above_or_equal) goto loc_002F4BB2;
    if ((((unsigned int)(result)) & (0xFFFFFFF8ULL)) != 0) goto loc_002F4BB2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m108)))) > ((unsigned int)((int)(*(unsigned int *)(v_stack_m108 + 16))))) goto loc_002F4BAF;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m108 + 20))) + ((unsigned int)((int)(*(unsigned int *)(v_stack_m108 + 16)))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m108))) + (*(unsigned int *)(v_stack_m108 + 4)));
    if (a2 < a3) goto loc_002F4BAF;
    v_r10 = ((int)(*(unsigned int *)(v_stack_m108 + 16))) + (v_stack_m108);
    if (condition_is_equal) goto loc_002F4BAF;
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_002F4CFD;
    if (condition_is_above_or_equal) goto loc_002F4BAF;
    v_stack_m170 = 576;
loc_002F4848:
    v_stack_m120 = 2;
    if (2 >= 11) goto loc_002F48B9;
    result = (1) << (2);
    if (((*(unsigned __int64 *)(v_r10 + 8)) & (result)) != 0) goto loc_002F4CA4;
loc_002F485F:
    a1 = (unsigned int)((2) + 1);
    goto loc_002F4848;
loc_002F4863:
    if (!(condition_is_above_or_equal)) {
        a3 = (unsigned int)((*(unsigned __int64 *)(v_r10 + 8)) + (63));
        a3 = (unsigned int)((a3) & (0xFFFFFFC0ULL));
        v_stack_m178 = a3;
    }
    result = ((unsigned int)(a3)) + (-504);
    result = (result) + (v_r10);
    v_r11 = 0;
loc_002F4885:
    *(unsigned __int64 *)(v_stack_m198 + 248) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) - 8);
    goto loc_002F42AF;
loc_002F4898:
    goto loc_002F4199;
loc_002F489D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) - 8)) <= a3) goto loc_002F4129;
    goto loc_002F4129;
loc_002F48B9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) - 8)) < a3) {
        a2 = (unsigned int)((576) + (63));
        a2 = (unsigned int)((a2) & (0xFFFFFFC0ULL));
        v_stack_m170 = a2;
    }
    a3 = ((unsigned int)(a2)) + (-512);
    a3 = (a3) + (v_r10);
    v_r11 = 0;
loc_002F48D9:
    *(unsigned __int64 *)(a3) = 1;
    a2 = (a2) << (32);
    result = (*(unsigned __int8 *)(a3)) | (a2);
    *(unsigned __int64 *)(a3 + 8) = result;
loc_002F48EE:
    v_stack_m180 = v_stack_m100;
    v_stack_m168 = v_stack_m130;
    goto loc_002F42FF;
loc_002F4906:
    if ((*(unsigned __int8 *)(1 + 43)) == 2) goto loc_002F4101;
    if ((*(unsigned __int16 *)(1 + 368)) != 35) goto loc_002F4101;
    v_stack_m1C0 = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 384)));
    v_stack_m1C8 = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 344)));
    v_stack_m1D0 = (unsigned int)((unsigned int)(v_stack_m14C));
    v_stack_m1D8 = (unsigned int)((unsigned int)(v_stack_m148));
    result = RtlpWalkWowStack(v_stack_mF0, 1 + 360, v_stack_m118, v_stack_m194);
    if ((unsigned __int8)(result) == 0) goto loc_002F4101;
    goto loc_002F4DD5;
loc_002F496A:
    if ((unsigned int)(v_r14) == 0) goto loc_002F4D1C;
    result = PsWow64GetProcessMachine(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), 1 + 360, v_stack_m118, v_stack_m194);
    if (((unsigned __int16)(result)) != 332) goto loc_002F4D1C;
    if ((*(unsigned __int8 *)(v_stack_m160 + 43)) != 2) goto loc_002F4D1C;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = RtlWow64GetCpuAreaInfo(*(unsigned __int64 *)(v_stack_m118 + 5256), 1 + 360, v_stack_m70, v_stack_m194);
    if (sign_flag) goto loc_002F4D1C;
    if ((((unsigned __int8)(v_stack_m70)) & (3)) == 0) goto loc_002F4A75;
loc_002F49E6:
    result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(v_stack_m118 + 5256), 1 + 360, v_stack_m70, v_stack_m194);
loc_002F49EC:
    if ((*(unsigned __int64 *)(1 + 360 + 16)) == 0) goto loc_002F4D97;
    v_stack_mD8 = v_xmm2;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm1;
    v_stack_mA8 = v_xmm0;
    goto loc_002F4715;
loc_002F4A3B:
    v_stack_m160 = *(unsigned __int64 *)(1 + 360 + 208);
    result = ((*(unsigned __int64 *)(1 + 360 + 208)) >= v_stack_m70) ? 1 : 0;
    if ((unsigned int)(result) != 0) goto loc_002F4786;
    goto loc_002F4DD5;
loc_002F4A5C:
    goto loc_002F4DD5;
loc_002F4A61:
    goto loc_002F4DD5;
loc_002F4A66:
    goto loc_002F4DD5;
loc_002F4A6B:
    goto loc_002F4DD5;
loc_002F4A70:
    goto loc_002F4DD5;
loc_002F4A75:
    if (result >= (*(unsigned __int64 *)(v_stack_m118 + 5256))) { result = *(unsigned __int64 *)(v_stack_m118 + 5256); }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m70 + 196))) - (4));
    v_stack_m1C0 = (unsigned int)(result);
    v_stack_m1C8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70 + 180)));
    v_stack_m1D0 = (unsigned int)((unsigned int)(v_stack_m14C));
    v_stack_m1D8 = (unsigned int)((unsigned int)(v_stack_m148));
    a2 = 0;
    result = RtlpWalkWowStack(v_stack_mF0, a2, v_stack_m118, v_stack_m194);
    if ((unsigned __int8)(result) == 0) goto loc_002F4D1C;
    goto loc_002F4DD5;
loc_002F4AD8:
    if (result >= v_stack_m118) { result = v_stack_m118; }
    v_stack_m18C = 1;
    *(unsigned __int64 *)(v_stack_m198 + 152) = *(unsigned __int64 *)(v_stack_m118 + 72);
    v_stack_m180 = v_stack_m100;
    v_stack_m168 = v_stack_m130;
    v_stack_m158 = v_stack_m140;
    if (v_stack_m140 == 0) goto loc_002F4D8E;
    v_stack_m160 = *(unsigned __int64 *)(v_stack_m140 + 208);
    goto loc_002F42FF;
loc_002F4B3B:
    result = KeGetEffectiveIrql(*(unsigned __int64 *)(v_stack_m118 + 72), v_stack_m140, v_stack_m118, v_stack_m194);
    if (((unsigned __int8)(result)) < 2) goto loc_002F466F;
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 35048))) + (80);
    a2 = (a1) - ((unsigned int)(*(unsigned int *)(v_rip + 13436193)));
    if ((*(unsigned __int64 *)(v_stack_m198 + 152)) >= a1) goto loc_002F4C9C;
    if (a2 > (*(unsigned __int64 *)(v_stack_m198 + 152))) goto loc_002F4C9C;
    v_stack_m168 = a1;
    v_stack_m180 = a2;
    v_stack_m158 = v_stack_m140;
    goto loc_002F41D3;
loc_002F4B8F:
    v_r11 = 0;
loc_002F4B92:
    goto loc_002F4885;
loc_002F4B9C:
    goto loc_002F4DD5;
loc_002F4BA1:
    if (a2 != 0) goto loc_002F41F6;
    goto loc_002F4DD5;
loc_002F4BAF:
    v_r11 = 0;
loc_002F4BB2:
    goto loc_002F48D9;
loc_002F4BBA:
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 14880))) + (80);
    a2 = (a1) - ((unsigned int)(*(unsigned int *)(v_rip + 13436423)));
    if (a2 > (*(unsigned __int64 *)(v_stack_m198 + 152))) goto loc_002F4663;
    if ((*(unsigned __int64 *)(v_stack_m198 + 152)) >= a1) goto loc_002F4663;
    v_stack_m168 = a1;
    v_stack_m180 = a2;
    v_stack_m158 = v_stack_m140;
    goto loc_002F41D3;
loc_002F4C01:
    if ((*(unsigned __int64 *)(v_stack_m198 + 152)) < a1) {
        a4 = (unsigned int)((v_stack_m194) + (63));
        a4 = (unsigned int)((a4) & (0xFFFFFFC0ULL));
        v_stack_m174 = a4;
    }
    result = ((unsigned int)(a4)) + (-512);
    result = (result) + (0);
loc_002F4C20:
    *(unsigned __int64 *)(result) = 0;
loc_002F4C23:
    v_stack_m158 = *(unsigned __int64 *)(v_stack_m138 + 32);
    v_stack_m140 = *(unsigned __int64 *)(v_stack_m138 + 32);
    if (*(unsigned __int64 *)(v_stack_m138 + 40) == 0) goto loc_002F4A5C;
    v_stack_m138 = *(unsigned __int64 *)(v_stack_m138 + 40);
    v_stack_m180 = *(unsigned __int64 *)(v_stack_m198 + 152);
    v_stack_m168 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 40));
    goto loc_002F42FF;
loc_002F4C59:
    v_stack_m138 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 40)) + 40);
    goto loc_002F4131;
loc_002F4C66:
    if (((a4) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 40)))) != 0) {
        a3 = (unsigned int)((0) + (63));
        a3 = (unsigned int)((a3) & (0xFFFFFFC0ULL));
        v_stack_m178 = a3;
    }
    a3 = (unsigned int)((a3) + (*(unsigned int *)(v_r11 + (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 40)) + 40))) * 4)));
    v_stack_m178 = a3;
    goto loc_002F45A9;
loc_002F4C90:
    goto loc_002F4DD5;
loc_002F4C95:
    result = 0;
    goto loc_002F4DE1;
loc_002F4C9C:
    goto loc_002F466F;
loc_002F4CA4:
    if (((a4) & (0)) != 0) {
        a2 = (unsigned int)((a2) + (63));
        a2 = (unsigned int)((a2) & (0xFFFFFFC0ULL));
        v_stack_m170 = a2;
    }
    a2 = (unsigned int)((a2) + (*(unsigned int *)(v_r11 + (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 40)) + 40))) * 4)));
    v_stack_m170 = a2;
    goto loc_002F485F;
loc_002F4CCA:
    result = ((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 40)) + 40)))))) + (-504);
    result = (result) + (v_r10);
    v_r11 = 0;
    *(unsigned __int64 *)(v_stack_m198 + 248) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) - 8);
    goto loc_002F42AF;
loc_002F4CF5:
    goto loc_002F4C20;
loc_002F4CFD:
    a3 = ((unsigned int)(*(unsigned int *)(0))) + (-512);
    a3 = (a3) + (v_r10);
    v_r11 = 0;
    goto loc_002F48D9;
loc_002F4D1C:
    goto loc_002F4DD5;
loc_002F4D21:
    goto loc_002F46F3;
loc_002F4D34:
    if (((v_r10) & (0)) != 0) {
        a4 = (unsigned int)((a4) + (63));
        a4 = (unsigned int)((a4) & (0xFFFFFFC0ULL));
        v_stack_m174 = a4;
    }
    a4 = (unsigned int)((a4) + (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m198 + 152) + (unsigned int)((unsigned int)(v_stack_mD0)) * 4)));
    v_stack_m174 = a4;
    goto loc_002F44D2;
loc_002F4D5E:
    result = ((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_mD0))))) + (-512);
    result = (result) + (a3);
    goto loc_002F4C20;
loc_002F4D78:
    v_stack_m158 = v_stack_m140;
    goto loc_002F4166;
loc_002F4D8C:
    goto loc_002F4DD5;
loc_002F4D8E:
    goto loc_002F42FF;
loc_002F4D97:
    goto loc_002F4DD5;
loc_002F4DA9:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_002F4E23;
loc_002F4DC0:
    result = RtlpGetEntireXStateAreaLength2(v_stack_m138, a3, a3, a4);
    result = (unsigned int)((result) + (800));
    goto loc_002F4010;
loc_002F4DD5:
    if ((unsigned int)(v_r14) != 0) goto loc_002F4EA5;
loc_002F4DDE:
loc_002F4DE1:
    a1 = (v_stack_m38) ^ (v_stack_m198);
    result = _security_check_cookie(a1, a3, a3, a4);
    return result;
loc_002F4E17:
    v_stack_m118 = a3;
    goto loc_002F3F92;
loc_002F4E23:
    a1 = (*(unsigned __int64 *)(a3)) | (*(unsigned __int64 *)(v_stack_m198));
    a1 = (a1) | (result);
    a1 = (a1) & (v_stack_p10);
    v_stack_m130 = a1;
    result = RtlpRemoveArchDisallowedXStateFeatures((unsigned int)((unsigned int)(v_stack_m118)), v_stack_m130, a3, a4);
    goto loc_002F4DC0;
loc_002F4E5D:
    result = 0;
    if (((*(unsigned __int8 *)(v_rip + 13435792)) & (1)) == 0) { result = (unsigned int)((unsigned int)(0x80000000ULL)); }
    v_stack_m150 = (unsigned int)(result);
    goto loc_002F4092;
loc_002F4E77:
    a2 = v_stack_m130;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1876)) & (0x4000ULL)) != 0) { a2 = *(unsigned __int64 *)(v_rip + 13444711); }
    v_stack_m110 = a2;
    goto loc_002F3FB8;
loc_002F4EA5:
    if (v_stack_m18F != 0) goto loc_002F4DDE;
    goto loc_002F4DDE;
loc_002F4EC1:
    result = 0;
    goto loc_002F4DE1;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpWalkFrameChain(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m124;
    uint32_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint8_t v_stack_m18F;
    uint8_t v_stack_m190;
    uint32_t v_stack_m194;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (464);
    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    result = (*(uint64_t *)(v_rip + 0xB1683E)) ^ (v_stack_m198);
    v_stack_m38 = result;
    v_stack_m14C = Arg4;
    v_stack_m148 = Arg2;
    v_stack_mF0 = Arg1;
    Arg3 = 0;
    v_stack_m108 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_m150 = 0;
    v_stack_m168 = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_m180 = 0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    v_stack_m18F = 1;
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x400ULL)) != 0) goto loc_002F4E17;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_002F4E17;
    v_stack_m118 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0);
loc_002F3F92:
    v_stack_m160 = 0;
    v_stack_m18C = 0;
    v_stack_m110 = 0;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (1));
    v_stack_mF8 = (uint32_t)(local_r14);
    if (condition_is_not_equal) goto loc_002F4E77;
loc_002F3FB8:
    result = -(0);
    local_rsi = (uint32_t)((local_rsi) & (0x800ULL));
    result = -(0);
    Arg1 = (uint32_t)((*(uint64_t *)(gs_base + (0 + 0x188))) & (64));
    v_stack_m194 = 0;
    result = RtlpValidateContextFlags2((uint32_t)((uint32_t)(Arg1 + 1048587)), v_stack_m194, result, Arg4);
    if (sign_flag) goto loc_002F401D;
    if ((((uint8_t)((uint32_t)(v_stack_m194))) & (2)) != 0) goto loc_002F4DA9;
loc_002F4010:
    local_rbx = (uint32_t)(0x4F0ULL) + 32;
    if ((((uint8_t)((uint32_t)(v_stack_m194))) & (4)) == 0) { local_rbx = (uint32_t)((uint32_t)(0x4F0ULL)); }
    local_rbx = (uint32_t)((local_rbx) + (15));
loc_002F401D:
    if (((uint32_t)((uint32_t)(local_rbx)) + 15) <= ((uint32_t)((uint32_t)(local_rbx)))) {
    }
    Arg1 = ((uint32_t)((uint32_t)(local_rbx)) + 15) & (-16);
    result = _chkstk(Arg1, v_stack_m194, result, Arg4);
    local_rsp = (local_rsp) - (Arg1);
    result = RtlInitializeExtendedContext2(v_stack_m198, (uint32_t)((uint32_t)(Arg1 + 1048587)), v_stack_m108, local_rsi);
    result = RtlpCaptureContext2(v_stack_m198, (uint32_t)((uint32_t)(Arg1 + 1048587)), v_stack_m108, local_rsi);
    v_stack_m190 = 0;
    result = RtlpGetStackLimits(v_stack_m180, v_stack_m168, v_stack_m108, local_rsi);
    if ((uint8_t)(result) == 0) goto loc_002F4EC1;
    local_r11 = 0;
    v_stack_m194 = 0;
    local_rdi = (uint32_t)(((uint32_t)(Arg3)) >> (1));
    local_rdi = (uint8_t)((local_rdi) & (1));
    if ((uint32_t)(local_r14) == 0) goto loc_002F4E5D;
loc_002F4092:
    v_stack_m100 = 0;
    v_stack_m130 = 0;
    if ((uint32_t)(local_r14) == 0) goto loc_002F4D78;
loc_002F40B3:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28) + 0x8)) & (1)) != 0) goto loc_002F4333;
    v_stack_m160 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28) - 400;
    if (v_stack_m118 == 0) goto loc_002F40E0;
    if (condition_is_above_or_equal) goto loc_002F40E7;
loc_002F40E0:
    result = 0;
    goto loc_002F4DE1;
loc_002F40E7:
    result = PsWow64GetProcessMachine(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m168, v_stack_m108, local_rsi);
    if (((uint16_t)(result)) == 332) goto loc_002F4906;
loc_002F4101:
    v_stack_m100 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28) - 0x190 + 0x180);
    v_stack_m130 = *(uint64_t *)(v_stack_m118 + 0x8);
    if ((*(uint64_t *)(v_stack_m118 + 0x8)) <= (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28) - 0x190 + 0x180))) goto loc_002F4C95;
    if ((*(uint64_t *)(v_stack_m118 + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28) - 0x190 + 0x180))) goto loc_002F489D;
loc_002F4129:
    v_stack_m138 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28);
loc_002F4131:
    if (((*(uint8_t *)(v_stack_m138 + 0x8)) & (1)) != 0) goto loc_002F4C59;
    v_stack_m158 = *(uint64_t *)(v_stack_m138 + 0x20);
    v_stack_m140 = *(uint64_t *)(v_stack_m138 + 0x20);
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x7D))) >> (2));
    result = (uint8_t)((result) & (1));
    v_stack_m18F = (uint8_t)(result);
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x7D)) | (4));
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x7D) = (uint8_t)(Arg1);
    local_r11 = 0;
loc_002F4166:
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm1;
    v_stack_m198 = (uint8_t)(local_rdi);
loc_002F418F:
loc_002F4199:
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    v_stack_m188 = 0;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m198 + 0x98))) & (7)) != 0) goto loc_002F4D97;
    if ((*(uint64_t *)(v_stack_m198 + 0x98)) < v_stack_m180) goto loc_002F45FB;
    if ((*(uint64_t *)(v_stack_m198 + 0x98)) >= v_stack_m168) goto loc_002F45FB;
loc_002F41D3:
    result = RtlpLookupFunctionEntryForStackWalks(*(uint64_t *)(v_stack_m198 + 0xF8), v_stack_m70, v_stack_m108, local_rsi);
    if (result == 0) goto loc_002F4BA1;
loc_002F41F6:
    Arg1 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = 0;
    Arg4 = 0;
    v_stack_m78 = 0;
    v_stack_m88 = v_stack_m180;
    v_stack_m80 = v_stack_m168;
    v_stack_m1A8 = 0;
    v_stack_m1B0 = v_stack_m88;
    v_stack_m1B8 = 0;
    v_stack_m1C0 = v_stack_m98;
    v_stack_m1C8 = v_stack_m90;
    v_stack_m1D0 = v_stack_m190;
    v_stack_m1D8 = v_stack_m198;
    result = RtlpxVirtualUnwind((uint32_t)(v_stack_m150), v_stack_m68, *(uint64_t *)(v_stack_m198 + 0xF8), result);
    if (sign_flag) goto loc_002F4B9C;
    result = v_stack_m198;
    if (v_stack_m190 != 0) { result = 0; }
    v_stack_m198 = (uint8_t)(result);
    if (((uint32_t)((uint32_t)(v_stack_m18C))) != 1) goto loc_002F42AF;
    if (v_stack_m194 <= 0) goto loc_002F42AF;
    if (v_stack_m110 != 0) goto loc_002F44D6;
loc_002F42AF:
    if (*(uint64_t *)(v_stack_m198 + 0xF8) == 0) goto loc_002F496A;
    if ((uint32_t)((uint32_t)(v_stack_m18C)) != 0) goto loc_002F433C;
    if ((uint32_t)(local_r14) != 0) goto loc_002F42EC;
    if ((*(uint64_t *)(v_stack_m198 + 0xF8)) < (*(uint64_t *)(v_stack_m198 + 0xF8))) goto loc_002F4C90;
    if ((uint32_t)(local_r14) != 0) goto loc_002F42EC;
    if (v_stack_m198 != ((uint8_t)(local_r14))) goto loc_002F45B2;
    goto loc_002F42FF;
loc_002F42EC:
    if ((*(uint64_t *)(v_stack_m198 + 0xF8)) < (*(uint64_t *)(v_stack_m198 + 0xF8))) goto loc_002F4751;
    if (v_stack_m194 != 0) goto loc_002F4898;
loc_002F42FF:
    result = (uint32_t)(v_stack_m194);
    if (((uint32_t)((uint32_t)(v_stack_m194))) >= ((uint32_t)((uint32_t)(v_stack_m14C)))) {
        Arg1 = *(uint64_t *)(v_stack_m198 + 0xF8);
        result = (uint32_t)(((uint32_t)(v_stack_m194)) - ((uint32_t)((uint32_t)(v_stack_m14C))));
        Arg2 = v_stack_mF0;
        *(uint64_t *)(Arg2 + result * 8) = Arg1;
    }
    result = (uint32_t)(((uint32_t)(v_stack_m194)) + 1);
    v_stack_m194 = (uint32_t)(result);
    if (((uint32_t)(result)) >= v_stack_m148) goto loc_002F45AD;
    goto loc_002F418F;
loc_002F4333:
    goto loc_002F40B3;
loc_002F433C:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m18C)))) - (1));
    if (condition_is_not_equal) goto loc_002F45B7;
    if (Arg1 > (*(uint64_t *)(result + 0x28))) goto loc_002F4A6B;
    if (v_stack_m158 == 0) goto loc_002F42FF;
    if (Arg1 != (*(uint64_t *)(v_stack_m160 + 0x168))) goto loc_002F42FF;
    v_stack_m18C = 2;
    *(uint64_t *)(v_stack_m198 + 0xF8) = *(uint64_t *)(v_stack_m158 + 0x138);
    *(uint64_t *)(v_stack_m198 + 0x98) = v_stack_m158 + 320;
    *(uint64_t *)(v_stack_m198 + 0xA0) = *(uint64_t *)(v_stack_m158 + 0xF8);
    *(uint64_t *)(v_stack_m198 + 0x90) = *(uint64_t *)(v_stack_m158 + 0x100);
    *(uint64_t *)(v_stack_m198 + 0xB0) = *(uint64_t *)(v_stack_m158 + 0x108);
    *(uint64_t *)(v_stack_m198 + 0xA8) = *(uint64_t *)(v_stack_m158 + 0x110);
    *(uint64_t *)(v_stack_m198 + 0xD8) = *(uint64_t *)(v_stack_m158 + 0x118);
    *(uint64_t *)(v_stack_m198 + 0xE0) = *(uint64_t *)(v_stack_m158 + 0x120);
    *(uint64_t *)(v_stack_m198 + 0xE8) = *(uint64_t *)(v_stack_m158 + 0x128);
    *(uint64_t *)(v_stack_m198 + 0xF0) = *(uint64_t *)(v_stack_m158 + 0x130);
    if (v_stack_m110 == 0) goto loc_002F4C23;
    v_stack_m124 = 0;
    v_stack_m174 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1))) | (*(uint32_t *)(*(uint64_t *)(v_stack_m158 + 0x130))));
    if (condition_is_above_or_equal) goto loc_002F4CF5;
    if ((((uint32_t)(*(uint64_t *)(v_stack_m158 + 0x130))) & (0xFFFFFFF8ULL)) != 0) goto loc_002F4CF5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m108)))) > ((uint32_t)((int32_t)(*(uint32_t *)(v_stack_m108 + 0x10))))) goto loc_002F4CF5;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m108 + 0x14))) + ((uint32_t)((int32_t)(*(uint32_t *)(v_stack_m108 + 0x10)))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m108))) + (*(uint32_t *)(v_stack_m108 + 0x4)));
    if (Arg2 < Arg3) goto loc_002F4CF5;
    Arg3 = ((int32_t)(*(uint32_t *)(v_stack_m108 + 0x10))) + (v_stack_m108);
    if (condition_is_equal) goto loc_002F4CF5;
    if (((2) & ((uint8_t)(*(uint64_t *)(v_stack_m158 + 0x130)))) == 0) goto loc_002F4D5E;
    if (condition_is_above_or_equal) goto loc_002F4CF5;
    v_stack_m174 = 576;
loc_002F44B5:
    v_stack_m124 = 2;
    if (2 >= 11) goto loc_002F4C01;
    result = (1) << (2);
    if (((*(uint64_t *)(Arg3 + 0x8)) & (result)) != 0) goto loc_002F4D34;
loc_002F44D2:
    Arg1 = (uint32_t)((2) + 1);
    goto loc_002F44B5;
loc_002F44D6:
    if ((*(uint64_t *)(v_stack_m198 + 0xF8)) != result) goto loc_002F42AF;
    v_stack_m128 = 0;
    v_stack_m178 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1))) | (*(uint32_t *)(result)));
    if (condition_is_above_or_equal) goto loc_002F4B92;
    if ((((uint32_t)(result)) & (0xFFFFFFF8ULL)) != 0) goto loc_002F4B92;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m108)))) > ((uint32_t)((int32_t)(*(uint32_t *)(v_stack_m108 + 0x10))))) goto loc_002F4B8F;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m108 + 0x14))) + ((uint32_t)((int32_t)(*(uint32_t *)(v_stack_m108 + 0x10)))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m108))) + (*(uint32_t *)(v_stack_m108 + 0x4)));
    if (Arg2 < Arg3) goto loc_002F4B8F;
    local_r10 = ((int32_t)(*(uint32_t *)(v_stack_m108 + 0x10))) + (v_stack_m108);
    if (condition_is_equal) goto loc_002F4B8F;
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_002F4CCA;
    if (condition_is_above_or_equal) goto loc_002F4B8F;
    v_stack_m178 = 576;
loc_002F458C:
    v_stack_m128 = 2;
    if (2 >= 11) goto loc_002F4863;
    result = (1) << (2);
    if (((*(uint64_t *)(local_r10 + 0x8)) & (result)) != 0) goto loc_002F4C66;
loc_002F45A9:
    Arg1 = (uint32_t)((2) + 1);
    goto loc_002F458C;
loc_002F45AD:
    goto loc_002F4DD5;
loc_002F45B2:
    goto loc_002F4199;
loc_002F45B7:
    if (((uint32_t)(*(uint64_t *)(local_r10 + 0x8))) != 1) goto loc_002F4A66;
    if (Arg1 > result) goto loc_002F42FF;
    if (Arg1 != (*(uint64_t *)(v_stack_m160 + 0x168))) goto loc_002F4D8C;
    v_stack_m118 = *(uint64_t *)(v_stack_m160 + 0x180);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m160 + 0x180))) & (3)) != 0) goto loc_002F49E6;
    goto loc_002F4AD8;
loc_002F45FB:
    result = (v_stack_m180 >= 576) ? 1 : 0;
    if ((uint32_t)(result) == 0) goto loc_002F4D97;
    result = KeGetCurrentStackPointer(Arg1, *(uint64_t *)(local_r10 + 0x8), 576, *(uint64_t *)(result));
    result = KeQueryCurrentStackInformationEx(result, v_stack_m188, v_stack_mE8, v_stack_mE0);
    if (((uint32_t)((uint32_t)(v_stack_m188))) > 9) goto loc_002F4642;
    if (((uint32_t)((uint32_t)(v_stack_m188))) < 9) goto loc_002F4D97;
loc_002F4642:
    if (((uint32_t)((uint32_t)(v_stack_m188))) == 1) goto loc_002F4666;
    if ((((uint8_t)(*(uint8_t *)(gs_base + (0 + 0x3A3C)))) & (1)) != 0) goto loc_002F4BBA;
loc_002F4663:
loc_002F4666:
    if (((uint32_t)((uint32_t)(v_stack_m188))) != 10) goto loc_002F4B3B;
loc_002F466F:
    Arg3 = 0;
    if (v_stack_mD8 != 0) goto loc_002F4D21;
    v_stack_mD8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x38);
    v_stack_mD0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x30);
    v_stack_mC8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x58);
    v_stack_mC0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28);
    v_stack_mB8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x418);
    v_stack_mB0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x420);
    v_stack_mA8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x408);
    v_stack_mA0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x410);
loc_002F46F3:
    if (((uint32_t)((uint32_t)(v_stack_m188))) > 10) goto loc_002F49EC;
    if (((uint32_t)((uint32_t)(v_stack_m188))) >= 10) goto loc_002F49EC;
    if (1 == 0) goto loc_002F49EC;
loc_002F4715:
    v_stack_mE8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x30);
    v_stack_mE0 = v_stack_mD8;
    if ((*(uint64_t *)(v_stack_m198 + 0x98)) < (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x30))) goto loc_002F4D97;
    if ((*(uint64_t *)(v_stack_m198 + 0x98)) >= v_stack_mD8) goto loc_002F4D97;
    v_stack_m180 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x30);
    v_stack_m168 = v_stack_mD8;
    v_stack_m158 = v_stack_m140;
    goto loc_002F41D3;
loc_002F4751:
    if (v_stack_m140 > v_stack_mD8) goto loc_002F4A70;
    if (v_stack_m140 != (*(uint64_t *)(v_stack_m160 + 0x168))) goto loc_002F4A61;
    v_stack_m18C = 1;
    if (v_stack_m158 != 0) goto loc_002F4A3B;
loc_002F4786:
    if (v_stack_m110 == 0) goto loc_002F48EE;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x30))) | (0x100040ULL));
    *(uint32_t *)(v_stack_m198 + 0x30) = (uint32_t)(result);
    v_stack_m120 = (uint32_t)(v_stack_m108);
    v_stack_m170 = (uint32_t)(v_stack_m108);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m140))) | (*(uint32_t *)(result)));
    if (condition_is_above_or_equal) goto loc_002F4BB2;
    if ((((uint32_t)(result)) & (0xFFFFFFF8ULL)) != 0) goto loc_002F4BB2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m108)))) > ((uint32_t)((int32_t)(*(uint32_t *)(v_stack_m108 + 0x10))))) goto loc_002F4BAF;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m108 + 0x14))) + ((uint32_t)((int32_t)(*(uint32_t *)(v_stack_m108 + 0x10)))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m108))) + (*(uint32_t *)(v_stack_m108 + 0x4)));
    if (Arg2 < Arg3) goto loc_002F4BAF;
    local_r10 = ((int32_t)(*(uint32_t *)(v_stack_m108 + 0x10))) + (v_stack_m108);
    if (condition_is_equal) goto loc_002F4BAF;
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_002F4CFD;
    if (condition_is_above_or_equal) goto loc_002F4BAF;
    v_stack_m170 = 576;
loc_002F4848:
    v_stack_m120 = 2;
    if (2 >= 11) goto loc_002F48B9;
    result = (1) << (2);
    if (((*(uint64_t *)(local_r10 + 0x8)) & (result)) != 0) goto loc_002F4CA4;
loc_002F485F:
    Arg1 = (uint32_t)((2) + 1);
    goto loc_002F4848;
loc_002F4863:
    if (!(condition_is_above_or_equal)) {
        Arg3 = (uint32_t)((*(uint64_t *)(local_r10 + 0x8)) + (63));
        Arg3 = (uint32_t)((Arg3) & (0xFFFFFFC0ULL));
        v_stack_m178 = Arg3;
    }
    result = ((uint32_t)(Arg3)) + (-504);
    result = (result) + (local_r10);
    local_r11 = 0;
loc_002F4885:
    *(uint64_t *)(v_stack_m198 + 0xF8) = *(uint64_t *)(*(uint64_t *)(result) - 0x8);
    goto loc_002F42AF;
loc_002F4898:
    goto loc_002F4199;
loc_002F489D:
    if ((*(uint64_t *)(*(uint64_t *)(result) - 0x8)) <= Arg3) goto loc_002F4129;
    goto loc_002F4129;
loc_002F48B9:
    if ((*(uint64_t *)(*(uint64_t *)(result) - 0x8)) < Arg3) {
        Arg2 = (uint32_t)((576) + (63));
        Arg2 = (uint32_t)((Arg2) & (0xFFFFFFC0ULL));
        v_stack_m170 = Arg2;
    }
    Arg3 = ((uint32_t)(Arg2)) + (-512);
    Arg3 = (Arg3) + (local_r10);
    local_r11 = 0;
loc_002F48D9:
    *(uint64_t *)(Arg3) = 1;
    Arg2 = (Arg2) << (32);
    result = (*(uint8_t *)(Arg3)) | (Arg2);
    *(uint64_t *)(Arg3 + 0x8) = result;
loc_002F48EE:
    v_stack_m180 = v_stack_m100;
    v_stack_m168 = v_stack_m130;
    goto loc_002F42FF;
loc_002F4906:
    if ((*(uint8_t *)(1 + 0x2B)) == 2) goto loc_002F4101;
    if ((*(uint16_t *)(1 + 0x170)) != 35) goto loc_002F4101;
    v_stack_m1C0 = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x180)));
    v_stack_m1C8 = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x158)));
    v_stack_m1D0 = (uint32_t)((uint32_t)(v_stack_m14C));
    v_stack_m1D8 = (uint32_t)((uint32_t)(v_stack_m148));
    result = RtlpWalkWowStack(v_stack_mF0, 1 + 360, v_stack_m118, v_stack_m194);
    if ((uint8_t)(result) == 0) goto loc_002F4101;
    goto loc_002F4DD5;
loc_002F496A:
    if ((uint32_t)(local_r14) == 0) goto loc_002F4D1C;
    result = PsWow64GetProcessMachine(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), 1 + 360, v_stack_m118, v_stack_m194);
    if (((uint16_t)(result)) != 332) goto loc_002F4D1C;
    if ((*(uint8_t *)(v_stack_m160 + 0x2B)) != 2) goto loc_002F4D1C;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = RtlWow64GetCpuAreaInfo(*(uint64_t *)(v_stack_m118 + 0x1488), 1 + 360, v_stack_m70, v_stack_m194);
    if (sign_flag) goto loc_002F4D1C;
    if ((((uint8_t)(v_stack_m70)) & (3)) == 0) goto loc_002F4A75;
loc_002F49E6:
    result = ExRaiseDatatypeMisalignment(*(uint64_t *)(v_stack_m118 + 0x1488), 1 + 360, v_stack_m70, v_stack_m194);
loc_002F49EC:
    if ((*(uint64_t *)(1 + 0x168 + 0x10)) == 0) goto loc_002F4D97;
    v_stack_mD8 = v_xmm2;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm1;
    v_stack_mA8 = v_xmm0;
    goto loc_002F4715;
loc_002F4A3B:
    v_stack_m160 = *(uint64_t *)(1 + 0x168 + 0xD0);
    result = ((*(uint64_t *)(1 + 0x168 + 0xD0)) >= v_stack_m70) ? 1 : 0;
    if ((uint32_t)(result) != 0) goto loc_002F4786;
    goto loc_002F4DD5;
loc_002F4A5C:
    goto loc_002F4DD5;
loc_002F4A61:
    goto loc_002F4DD5;
loc_002F4A66:
    goto loc_002F4DD5;
loc_002F4A6B:
    goto loc_002F4DD5;
loc_002F4A70:
    goto loc_002F4DD5;
loc_002F4A75:
    if (result >= (*(uint64_t *)(v_stack_m118 + 0x1488))) { result = *(uint64_t *)(v_stack_m118 + 0x1488); }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m70 + 0xC4))) - (4));
    v_stack_m1C0 = (uint32_t)(result);
    v_stack_m1C8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0xB4)));
    v_stack_m1D0 = (uint32_t)((uint32_t)(v_stack_m14C));
    v_stack_m1D8 = (uint32_t)((uint32_t)(v_stack_m148));
    Arg2 = 0;
    result = RtlpWalkWowStack(v_stack_mF0, Arg2, v_stack_m118, v_stack_m194);
    if ((uint8_t)(result) == 0) goto loc_002F4D1C;
    goto loc_002F4DD5;
loc_002F4AD8:
    if (result >= v_stack_m118) { result = v_stack_m118; }
    v_stack_m18C = 1;
    *(uint64_t *)(v_stack_m198 + 0x98) = *(uint64_t *)(v_stack_m118 + 0x48);
    v_stack_m180 = v_stack_m100;
    v_stack_m168 = v_stack_m130;
    v_stack_m158 = v_stack_m140;
    if (v_stack_m140 == 0) goto loc_002F4D8E;
    v_stack_m160 = *(uint64_t *)(v_stack_m140 + 0xD0);
    goto loc_002F42FF;
loc_002F4B3B:
    result = KeGetEffectiveIrql(*(uint64_t *)(v_stack_m118 + 0x48), v_stack_m140, v_stack_m118, v_stack_m194);
    if (((uint8_t)(result)) < 2) goto loc_002F466F;
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x88E8))) + (80);
    Arg2 = (Arg1) - ((uint32_t)(*(uint32_t *)(v_rip + 0xCD0521)));
    if ((*(uint64_t *)(v_stack_m198 + 0x98)) >= Arg1) goto loc_002F4C9C;
    if (Arg2 > (*(uint64_t *)(v_stack_m198 + 0x98))) goto loc_002F4C9C;
    v_stack_m168 = Arg1;
    v_stack_m180 = Arg2;
    v_stack_m158 = v_stack_m140;
    goto loc_002F41D3;
loc_002F4B8F:
    local_r11 = 0;
loc_002F4B92:
    goto loc_002F4885;
loc_002F4B9C:
    goto loc_002F4DD5;
loc_002F4BA1:
    if (Arg2 != 0) goto loc_002F41F6;
    goto loc_002F4DD5;
loc_002F4BAF:
    local_r11 = 0;
loc_002F4BB2:
    goto loc_002F48D9;
loc_002F4BBA:
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x3A20))) + (80);
    Arg2 = (Arg1) - ((uint32_t)(*(uint32_t *)(v_rip + 0xCD0607)));
    if (Arg2 > (*(uint64_t *)(v_stack_m198 + 0x98))) goto loc_002F4663;
    if ((*(uint64_t *)(v_stack_m198 + 0x98)) >= Arg1) goto loc_002F4663;
    v_stack_m168 = Arg1;
    v_stack_m180 = Arg2;
    v_stack_m158 = v_stack_m140;
    goto loc_002F41D3;
loc_002F4C01:
    if ((*(uint64_t *)(v_stack_m198 + 0x98)) < Arg1) {
        Arg4 = (uint32_t)((v_stack_m194) + (63));
        Arg4 = (uint32_t)((Arg4) & (0xFFFFFFC0ULL));
        v_stack_m174 = Arg4;
    }
    result = ((uint32_t)(Arg4)) + (-512);
    result = (result) + (0);
loc_002F4C20:
    *(uint64_t *)(result) = 0;
loc_002F4C23:
    v_stack_m158 = *(uint64_t *)(v_stack_m138 + 0x20);
    v_stack_m140 = *(uint64_t *)(v_stack_m138 + 0x20);
    if (*(uint64_t *)(v_stack_m138 + 0x28) == 0) goto loc_002F4A5C;
    v_stack_m138 = *(uint64_t *)(v_stack_m138 + 0x28);
    v_stack_m180 = *(uint64_t *)(v_stack_m198 + 0x98);
    v_stack_m168 = *(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x28));
    goto loc_002F42FF;
loc_002F4C59:
    v_stack_m138 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x28)) + 0x28);
    goto loc_002F4131;
loc_002F4C66:
    if (((Arg4) & (*(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x28)))) != 0) {
        Arg3 = (uint32_t)((0) + (63));
        Arg3 = (uint32_t)((Arg3) & (0xFFFFFFC0ULL));
        v_stack_m178 = Arg3;
    }
    Arg3 = (uint32_t)((Arg3) + (*(uint32_t *)(local_r11 + (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x28)) + 0x28))) * 4)));
    v_stack_m178 = Arg3;
    goto loc_002F45A9;
loc_002F4C90:
    goto loc_002F4DD5;
loc_002F4C95:
    result = 0;
    goto loc_002F4DE1;
loc_002F4C9C:
    goto loc_002F466F;
loc_002F4CA4:
    if (((Arg4) & (0)) != 0) {
        Arg2 = (uint32_t)((Arg2) + (63));
        Arg2 = (uint32_t)((Arg2) & (0xFFFFFFC0ULL));
        v_stack_m170 = Arg2;
    }
    Arg2 = (uint32_t)((Arg2) + (*(uint32_t *)(local_r11 + (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x28)) + 0x28))) * 4)));
    v_stack_m170 = Arg2;
    goto loc_002F485F;
loc_002F4CCA:
    result = ((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x28)) + 0x28)))))) + (-504);
    result = (result) + (local_r10);
    local_r11 = 0;
    *(uint64_t *)(v_stack_m198 + 0xF8) = *(uint64_t *)(*(uint64_t *)(result) - 0x8);
    goto loc_002F42AF;
loc_002F4CF5:
    goto loc_002F4C20;
loc_002F4CFD:
    Arg3 = ((uint32_t)(*(uint32_t *)(0))) + (-512);
    Arg3 = (Arg3) + (local_r10);
    local_r11 = 0;
    goto loc_002F48D9;
loc_002F4D1C:
    goto loc_002F4DD5;
loc_002F4D21:
    goto loc_002F46F3;
loc_002F4D34:
    if (((local_r10) & (0)) != 0) {
        Arg4 = (uint32_t)((Arg4) + (63));
        Arg4 = (uint32_t)((Arg4) & (0xFFFFFFC0ULL));
        v_stack_m174 = Arg4;
    }
    Arg4 = (uint32_t)((Arg4) + (*(uint32_t *)(*(uint64_t *)(v_stack_m198 + 0x98) + (uint32_t)((uint32_t)(v_stack_mD0)) * 4)));
    v_stack_m174 = Arg4;
    goto loc_002F44D2;
loc_002F4D5E:
    result = ((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_mD0))))) + (-512);
    result = (result) + (Arg3);
    goto loc_002F4C20;
loc_002F4D78:
    v_stack_m158 = v_stack_m140;
    goto loc_002F4166;
loc_002F4D8C:
    goto loc_002F4DD5;
loc_002F4D8E:
    goto loc_002F42FF;
loc_002F4D97:
    goto loc_002F4DD5;
loc_002F4DA9:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_002F4E23;
loc_002F4DC0:
    result = RtlpGetEntireXStateAreaLength2(v_stack_m138, Arg3, Arg3, Arg4);
    result = (uint32_t)((result) + (800));
    goto loc_002F4010;
loc_002F4DD5:
    if ((uint32_t)(local_r14) != 0) goto loc_002F4EA5;
loc_002F4DDE:
loc_002F4DE1:
    Arg1 = (v_stack_m38) ^ (v_stack_m198);
    result = _security_check_cookie(Arg1, Arg3, Arg3, Arg4);
    return result;
loc_002F4E17:
    v_stack_m118 = Arg3;
    goto loc_002F3F92;
loc_002F4E23:
    Arg1 = (*(uint64_t *)(Arg3)) | (*(uint64_t *)(v_stack_m198));
    Arg1 = (Arg1) | (result);
    Arg1 = (Arg1) & (v_stack_p10);
    v_stack_m130 = Arg1;
    result = RtlpRemoveArchDisallowedXStateFeatures((uint32_t)((uint32_t)(v_stack_m118)), v_stack_m130, Arg3, Arg4);
    goto loc_002F4DC0;
loc_002F4E5D:
    result = 0;
    if (((*(uint8_t *)(v_rip + 0xCD0390)) & (1)) == 0) { result = (uint32_t)((uint32_t)(0x80000000ULL)); }
    v_stack_m150 = (uint32_t)(result);
    goto loc_002F4092;
loc_002F4E77:
    Arg2 = v_stack_m130;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x754)) & (0x4000ULL)) != 0) { Arg2 = *(uint64_t *)(v_rip + 0xCD2667); }
    v_stack_m110 = Arg2;
    goto loc_002F3FB8;
loc_002F4EA5:
    if (v_stack_m18F != 0) goto loc_002F4DDE;
    goto loc_002F4DDE;
loc_002F4EC1:
    result = 0;
    goto loc_002F4DE1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F3ED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
