# PpmCheckComputeHeteroResponseEx

- RVA: `0x005DECA0`–`0x005DF57E` (길이 `2,270` bytes)
- VA: `0x00000001405DECA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CD960`
- 디코드: `528`개 명령, `2,270/2,270` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x005DED1C` → [PpmHeteroIsMultiClassParkingEnabled](../41/PpmHeteroIsMultiClassParkingEnabled_function_00414310.md) (function, `0x00414310`)
- `0x005DED28` → [PpmCheckComputeMultiClassHeteroResponseEx](../4F/PpmCheckComputeMultiClassHeteroResponseEx_function_004F14A4.md) (function, `0x004F14A4`)
- `0x005DEDD8` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x005DEE5E` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005DEE73` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x005DEE8E` → [PpmHeteroUtilityToNormalizedUtility](../41/PpmHeteroUtilityToNormalizedUtility_function_00413394.md) (function, `0x00413394`)
- `0x005DEE9A` → [PpmHeteroUtilityToNormalizedUtility](../41/PpmHeteroUtilityToNormalizedUtility_function_00413394.md) (function, `0x00413394`)
- `0x005DEEC2` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005DEEF3` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x005DEF0D` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x005DEF80` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x005DEFDC` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x005DF060` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](../41/PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x005DF079` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](../41/PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x005DF0C6` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x005DF19A` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](../41/PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x005DF1B4` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](../41/PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x005DF21A` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x005DF29F` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](../41/PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x005DF2B9` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](../41/PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x005DF301` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](../41/PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x005DF318` → [PpmHeteroUtilityGreaterThanOrEqualThreshold](../41/PpmHeteroUtilityGreaterThanOrEqualThreshold_function_004124A0.md) (function, `0x004124A0`)
- `0x005DF37F` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x005DF41A` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x005DF445` → [PpmEventTraceHeteroResponseEx](../4F/PpmEventTraceHeteroResponseEx_function_004F1B6C.md) (function, `0x004F1B6C`)
- `0x005DF47A` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x005DF4EE` → [Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline](../4F/Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline_function_004F4E1C.md) (function, `0x004F4E1C`)
- `0x005DF545` → [PpmEventTraceHeteroResponseExV1](../4F/PpmEventTraceHeteroResponseExV1_function_004F3DDC.md) (function, `0x004F3DDC`)
- `0x005DF561` → [PpmParkCalculateUnparkCount](../41/PpmParkCalculateUnparkCount_function_00413750.md) (function, `0x00413750`)

### Direct callers
- [PpmCheckComputeHeteroResponse](../4A/PpmCheckComputeHeteroResponse_function_004AACD0.md) at `0x004AAD22`

### Static image references
- `0x005DECB6` → RVA `0x00E08380` (`.data`; read)
- `0x005DECBF` → RVA `0x00F070A0` (`.data`; read)
- `0x005DECD3` → RVA `0x00F0CE0C` (`.data`; read)
- `0x005DECF2` → RVA `0x00FC5038` (`ALMOSTRO`; read)
- `0x005DECFE` → RVA `0x00F070A8` (`.data`; read)
- `0x005DED0A` → RVA `0x00F070B0` (`.data`; read)
- `0x005DED32` → RVA `0x00F083E0` (`.data`; read)
- `0x005DED58` → RVA `0x00F083D8` (`.data`; read)
- `0x005DED5F` → RVA `0x00FC6A86` (`ALMOSTRO`; read)
- `0x005DEDE3` → RVA `0x00F09168` (`.data`; read)
- `0x005DEDEB` → RVA `0x00E678A0` (`.data`; read)
- `0x005DEE78` → RVA `0x00F0B244` (`.data`; read)
- `0x005DEEE0` → RVA `0x0047F870` (`PpmUtilityComparer`; read)
- `0x005DF10E` → RVA `0x00E0B808` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DECA0  4C 8B DC                        mov r11, rsp
005DECA3  53                              push rbx
005DECA4  55                              push rbp
005DECA5  56                              push rsi
005DECA6  57                              push rdi
005DECA7  41 54                           push r12
005DECA9  41 55                           push r13
005DECAB  41 56                           push r14
005DECAD  41 57                           push r15
005DECAF  48 81 EC B8 00 00 00            sub rsp, 0xb8
005DECB6  48 8B 15 C3 96 82 00            mov rdx, qword ptr [rip + 0x8296c3]
005DECBD  33 C0                           xor eax, eax
005DECBF  4C 8B 35 DA 83 92 00            mov r14, qword ptr [rip + 0x9283da]
005DECC6  0F 57 C0                        xorps xmm0, xmm0
005DECC9  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
005DECCD  41 BF 01 00 00 00               mov r15d, 1
005DECD3  48 63 05 32 E1 92 00            movsxd rax, dword ptr [rip + 0x92e132]
005DECDA  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
005DECE1  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
005DECE6  48 8D 42 28                     lea rax, [rdx + 0x28]
005DECEA  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
005DECEF  48 03 C1                        add rax, rcx
005DECF2  83 3D 3F 63 9E 00 04            cmp dword ptr [rip + 0x9e633f], 4
005DECF9  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
005DECFE  48 8B 05 A3 83 92 00            mov rax, qword ptr [rip + 0x9283a3]
005DED05  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005DED0A  48 8B 05 9F 83 92 00            mov rax, qword ptr [rip + 0x92839f]
005DED11  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
005DED16  0F 85 45 08 00 00               jne 0x1405df561
005DED1C  E8 EF 55 E3 FF                  call 0x140414310
005DED21  45 33 E4                        xor r12d, r12d
005DED24  84 C0                           test al, al
005DED26  74 0A                           je 0x1405ded32
005DED28  E8 77 27 F1 FF                  call 0x1404f14a4
005DED2D  E9 34 08 00 00                  jmp 0x1405df566
005DED32  44 39 25 A7 96 92 00            cmp dword ptr [rip + 0x9296a7], r12d
005DED39  41 8B FC                        mov edi, r12d
005DED3C  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
005DED41  0F 84 1A 08 00 00               je 0x1405df561
005DED47  8B C7                           mov eax, edi
005DED49  41 8B EC                        mov ebp, r12d
005DED4C  48 69 F8 10 05 00 00            imul rdi, rax, 0x510
005DED53  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
005DED58  48 03 3D 79 96 92 00            add rdi, qword ptr [rip + 0x929679]
005DED5F  44 38 25 20 7D 9E 00            cmp byte ptr [rip + 0x9e7d20], r12b
005DED66  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
005DED6E  74 1E                           je 0x1405ded8e
005DED70  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
005DED77  66 44 39 A0 80 02 00 00         cmp word ptr [rax + 0x280], r12w
005DED7F  75 0D                           jne 0x1405ded8e
005DED81  44 39 25 B0 62 9E 00            cmp dword ptr [rip + 0x9e62b0], r12d
005DED88  0F 84 BC 07 00 00               je 0x1405df54a
005DED8E  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
005DED95  33 C9                           xor ecx, ecx
005DED97  44 8A E9                        mov r13b, cl
005DED9A  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
005DED9F  4D 8B FC                        mov r15, r12
005DEDA2  44 89 A4 24 88 00 00 00         mov dword ptr [rsp + 0x88], r12d
005DEDAA  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
005DEDB2  0F B7 B0 88 02 00 00            movzx esi, word ptr [rax + 0x288]
005DEDB9  89 B4 24 10 01 00 00            mov dword ptr [rsp + 0x110], esi
005DEDC0  89 8C 24 00 01 00 00            mov dword ptr [rsp + 0x100], ecx
005DEDC7  8B D9                           mov ebx, ecx
005DEDC9  44 89 AC 24 18 01 00 00         mov dword ptr [rsp + 0x118], r13d
005DEDD1  89 8C 24 08 01 00 00            mov dword ptr [rsp + 0x108], ecx
005DEDD8  E8 3F 60 F1 FF                  call 0x1404f4e1c
005DEDDD  33 D2                           xor edx, edx
005DEDDF  85 C0                           test eax, eax
005DEDE1  74 4B                           je 0x1405dee2e
005DEDE3  38 15 7F A3 92 00               cmp byte ptr [rip + 0x92a37f], dl
005DEDE9  74 43                           je 0x1405dee2e
005DEDEB  8B 0D AF 8A 88 00               mov ecx, dword ptr [rip + 0x888aaf]
005DEDF1  8D 41 FE                        lea eax, [rcx - 2]
005DEDF4  A9 F9 FF FF FF                  test eax, 0xfffffff9
005DEDF9  75 07                           jne 0x1405dee02
005DEDFB  B0 01                           mov al, 1
005DEDFD  83 F9 08                        cmp ecx, 8
005DEE00  75 02                           jne 0x1405dee04
005DEE02  8A C2                           mov al, dl
005DEE04  0F B6 B7 B0 04 00 00            movzx esi, byte ptr [rdi + 0x4b0]
005DEE0B  44 8B EA                        mov r13d, edx
005DEE0E  40 84 F6                        test sil, sil
005DEE11  0F B6 C0                        movzx eax, al
005DEE14  89 B4 24 08 01 00 00            mov dword ptr [rsp + 0x108], esi
005DEE1B  8B B4 24 10 01 00 00            mov esi, dword ptr [rsp + 0x110]
005DEE22  44 0F 45 E8                     cmovne r13d, eax
005DEE26  44 89 AC 24 18 01 00 00         mov dword ptr [rsp + 0x118], r13d
005DEE2E  48 8D 4F 30                     lea rcx, [rdi + 0x30]
005DEE32  66 89 94 24 A0 00 00 00         mov word ptr [rsp + 0xa0], dx
005DEE3A  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
005DEE3E  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
005DEE46  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
005DEE4E  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
005DEE56  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
005DEE5E  E8 1D 66 E3 FF                  call 0x140415480
005DEE63  85 C0                           test eax, eax
005DEE65  75 79                           jne 0x1405deee0
005DEE67  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
005DEE6C  8B 8C 24 00 01 00 00            mov ecx, dword ptr [rsp + 0x100]
005DEE73  E8 58 97 CF FF                  call 0x1402d85d0
005DEE78  83 3D C5 C3 92 00 05            cmp dword ptr [rip + 0x92c3c5], 5
005DEE7F  48 8D 88 B0 89 00 00            lea rcx, [rax + 0x89b0]
005DEE86  8B 51 28                        mov edx, dword ptr [rcx + 0x28]
005DEE89  74 03                           je 0x1405dee8e
005DEE8B  2B 51 30                        sub edx, dword ptr [rcx + 0x30]
005DEE8E  E8 01 45 E3 FF                  call 0x140413394
005DEE93  41 89 04 9E                     mov dword ptr [r14 + rbx*4], eax
005DEE97  8B 51 34                        mov edx, dword ptr [rcx + 0x34]
005DEE9A  E8 F5 44 E3 FF                  call 0x140413394
005DEE9F  8B C8                           mov ecx, eax
005DEEA1  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
005DEEA9  41 89 4C 9D 00                  mov dword ptr [r13 + rbx*4], ecx
005DEEAE  4C 03 F9                        add r15, rcx
005DEEB1  41 8B 04 9E                     mov eax, dword ptr [r14 + rbx*4]
005DEEB5  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
005DEEBD  4C 03 E0                        add r12, rax
005DEEC0  FF C3                           inc ebx
005DEEC2  E8 B9 65 E3 FF                  call 0x140415480
005DEEC7  85 C0                           test eax, eax
005DEEC9  74 A1                           je 0x1405dee6c
005DEECB  44 8B AC 24 18 01 00 00         mov r13d, dword ptr [rsp + 0x118]
005DEED3  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
005DEED8  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
005DEEE0  4C 8D 0D 89 09 EA FF            lea r9, [rip - 0x15f677]
005DEEE7  41 B8 04 00 00 00               mov r8d, 4
005DEEED  48 8B D3                        mov rdx, rbx
005DEEF0  49 8B CE                        mov rcx, r14
005DEEF3  E8 F8 1A F2 FF                  call 0x1405009f0
005DEEF8  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
005DEEFD  4C 8D 0D 6C 09 EA FF            lea r9, [rip - 0x15f694]
005DEF04  41 B8 04 00 00 00               mov r8d, 4
005DEF0A  48 8B D3                        mov rdx, rbx
005DEF0D  E8 DE 1A F2 FF                  call 0x1405009f0
005DEF12  0F B7 4F 0A                     movzx ecx, word ptr [rdi + 0xa]
005DEF16  33 DB                           xor ebx, ebx
005DEF18  48 8B 87 68 04 00 00            mov rax, qword ptr [rdi + 0x468]
005DEF1F  44 8B D3                        mov r10d, ebx
005DEF22  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
005DEF27  44 8B CB                        mov r9d, ebx
005DEF2A  85 C9                           test ecx, ecx
005DEF2C  74 35                           je 0x1405def63
005DEF2E  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
005DEF33  4C 8D 04 C8                     lea r8, [rax + rcx*8]
005DEF37  8B D1                           mov edx, ecx
005DEF39  49 8B C4                        mov rax, r12
005DEF3C  49 0F AF 00                     imul rax, qword ptr [r8]
005DEF40  4C 03 C8                        add r9, rax
005DEF43  48 8B C2                        mov rax, rdx
005DEF46  FF C9                           dec ecx
005DEF48  48 FF CA                        dec rdx
005DEF4B  4D 89 0C CB                     mov qword ptr [r11 + rcx*8], r9
005DEF4F  49 0F AF 00                     imul rax, qword ptr [r8]
005DEF53  4D 8D 40 F8                     lea r8, [r8 - 8]
005DEF57  4C 03 D0                        add r10, rax
005DEF5A  85 C9                           test ecx, ecx
005DEF5C  75 DB                           jne 0x1405def39
005DEF5E  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
005DEF63  85 F6                           test esi, esi
005DEF65  74 47                           je 0x1405defae
005DEF67  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
005DEF6C  49 8B DE                        mov rbx, r14
005DEF6F  49 2B F6                        sub rsi, r14
005DEF72  44 8B B4 24 10 01 00 00         mov r14d, dword ptr [rsp + 0x110]
005DEF7A  8B 04 1E                        mov eax, dword ptr [rsi + rbx]
005DEF7D  4C 2B F8                        sub r15, rax
005DEF80  E8 97 5E F1 FF                  call 0x1404f4e1c
005DEF85  85 C0                           test eax, eax
005DEF87  74 05                           je 0x1405def8e
005DEF89  8B 03                           mov eax, dword ptr [rbx]
005DEF8B  4C 2B E0                        sub r12, rax
005DEF8E  48 83 C3 04                     add rbx, 4
005DEF92  49 83 EE 01                     sub r14, 1
005DEF96  75 E2                           jne 0x1405def7a
005DEF98  8B B4 24 10 01 00 00            mov esi, dword ptr [rsp + 0x110]
005DEF9F  33 DB                           xor ebx, ebx
005DEFA1  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
005DEFA6  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
005DEFAE  38 1D D2 7A 9E 00               cmp byte ptr [rip + 0x9e7ad2], bl
005DEFB4  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
005DEFBB  44 0F B7 B0 80 02 00 00         movzx r14d, word ptr [rax + 0x280]
005DEFC3  66 44 89 B4 24 00 01 00 00      mov word ptr [rsp + 0x100], r14w
005DEFCC  74 0E                           je 0x1405defdc
005DEFCE  44 0F B7 77 0A                  movzx r14d, word ptr [rdi + 0xa]
005DEFD3  66 44 89 B4 24 00 01 00 00      mov word ptr [rsp + 0x100], r14w
005DEFDC  E8 3B 5E F1 FF                  call 0x1404f4e1c
005DEFE1  85 C0                           test eax, eax
005DEFE3  74 2A                           je 0x1405df00f
005DEFE5  B8 01 00 00 00                  mov eax, 1
005DEFEA  49 8B CC                        mov rcx, r12
005DEFED  4C 3B E0                        cmp r12, rax
005DEFF0  48 0F 42 C8                     cmovb rcx, rax
005DEFF4  33 D2                           xor edx, edx
005DEFF6  49 6B C7 64                     imul rax, r15, 0x64
005DEFFA  48 F7 F1                        div rcx
005DEFFD  B9 64 00 00 00                  mov ecx, 0x64
005DF002  3B C1                           cmp eax, ecx
005DF004  0F 47 C1                        cmova eax, ecx
005DF007  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
005DF00F  41 0F B7 DE                     movzx ebx, r14w
005DF013  39 9C 24 10 01 00 00            cmp dword ptr [rsp + 0x110], ebx
005DF01A  0F 83 A6 00 00 00               jae 0x1405df0c6
005DF020  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
005DF025  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
005DF02A  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
005DF02F  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
005DF034  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
005DF039  B8 3F 00 00 00                  mov eax, 0x3f
005DF03E  44 8B FE                        mov r15d, esi
005DF041  3B F0                           cmp esi, eax
005DF043  48 8B CF                        mov rcx, rdi
005DF046  0F 42 C6                        cmovb eax, esi
005DF049  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
005DF04E  43 8B 54 BD 00                  mov edx, dword ptr [r13 + r15*4]
005DF053  4F 8B 04 FE                     mov r8, qword ptr [r14 + r15*8]
005DF057  46 0F B6 8C 20 33 01 00 00      movzx r9d, byte ptr [rax + r12 + 0x133]
005DF060  E8 3B 34 E3 FF                  call 0x1404124a0
005DF065  85 C0                           test eax, eax
005DF067  74 33                           je 0x1405df09c
005DF069  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
005DF06E  45 33 C0                        xor r8d, r8d
005DF071  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
005DF076  48 8B CF                        mov rcx, rdi
005DF079  E8 22 34 E3 FF                  call 0x1404124a0
005DF07E  85 C0                           test eax, eax
005DF080  74 1A                           je 0x1405df09c
005DF082  42 8B 44 BD 00                  mov eax, dword ptr [rbp + r15*4]
005DF087  FF C6                           inc esi
005DF089  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
005DF08E  4C 2B F8                        sub r15, rax
005DF091  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
005DF096  3B F3                           cmp esi, ebx
005DF098  72 9F                           jb 0x1405df039
005DF09A  EB 05                           jmp 0x1405df0a1
005DF09C  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
005DF0A1  48 8B BC 24 A8 00 00 00         mov rdi, qword ptr [rsp + 0xa8]
005DF0A9  8B 6C 24 78                     mov ebp, dword ptr [rsp + 0x78]
005DF0AD  44 0F B7 B4 24 00 01 00 00      movzx r14d, word ptr [rsp + 0x100]
005DF0B6  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
005DF0BE  44 8B AC 24 18 01 00 00         mov r13d, dword ptr [rsp + 0x118]
005DF0C6  E8 51 5D F1 FF                  call 0x1404f4e1c
005DF0CB  85 C0                           test eax, eax
005DF0CD  0F 84 00 01 00 00               je 0x1405df1d3
005DF0D3  80 3D 8E A0 92 00 00            cmp byte ptr [rip + 0x92a08e], 0
005DF0DA  0F 84 F3 00 00 00               je 0x1405df1d3
005DF0E0  45 84 ED                        test r13b, r13b
005DF0E3  44 8B AC 24 10 01 00 00         mov r13d, dword ptr [rsp + 0x110]
005DF0EB  0F 85 EA 00 00 00               jne 0x1405df1db
005DF0F1  41 3B F5                        cmp esi, r13d
005DF0F4  0F 85 E1 00 00 00               jne 0x1405df1db
005DF0FA  41 0F B7 C6                     movzx eax, r14w
005DF0FE  3B F0                           cmp esi, eax
005DF100  0F 83 E7 00 00 00               jae 0x1405df1ed
005DF106  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
005DF10E  3B 05 F4 C6 82 00               cmp eax, dword ptr [rip + 0x82c6f4]
005DF114  0F 87 D3 00 00 00               ja 0x1405df1ed
005DF11A  49 81 FC E8 03 00 00            cmp r12, 0x3e8
005DF121  0F 82 C6 00 00 00               jb 0x1405df1ed
005DF127  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
005DF12C  B8 3F 00 00 00                  mov eax, 0x3f
005DF131  3B F0                           cmp esi, eax
005DF133  0F 42 C6                        cmovb eax, esi
005DF136  44 0F B6 8C 08 33 01 00 00      movzx r9d, byte ptr [rax + rcx + 0x133]
005DF13F  8B 05 5B 87 88 00               mov eax, dword ptr [rip + 0x88875b]
005DF145  83 E8 01                        sub eax, 1
005DF148  74 1B                           je 0x1405df165
005DF14A  83 E8 01                        sub eax, 1
005DF14D  74 16                           je 0x1405df165
005DF14F  83 E8 03                        sub eax, 3
005DF152  74 0B                           je 0x1405df15f
005DF154  83 F8 01                        cmp eax, 1
005DF157  74 06                           je 0x1405df15f
005DF159  41 6B C9 32                     imul ecx, r9d, 0x32
005DF15D  EB 0A                           jmp 0x1405df169
005DF15F  41 6B C9 1E                     imul ecx, r9d, 0x1e
005DF163  EB 04                           jmp 0x1405df169
005DF165  41 6B C9 46                     imul ecx, r9d, 0x46
005DF169  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
005DF16E  B8 1F 85 EB 51                  mov eax, 0x51eb851f
005DF173  F7 E1                           mul ecx
005DF175  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
005DF17A  45 33 E4                        xor r12d, r12d
005DF17D  8B DA                           mov ebx, edx
005DF17F  44 8B C6                        mov r8d, esi
005DF182  49 8B CE                        mov rcx, r14
005DF185  C1 EB 05                        shr ebx, 5
005DF188  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
005DF18D  42 8B 14 80                     mov edx, dword ptr [rax + r8*4]
005DF191  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
005DF196  4E 8B 04 C0                     mov r8, qword ptr [rax + r8*8]
005DF19A  E8 01 33 E3 FF                  call 0x1404124a0
005DF19F  85 C0                           test eax, eax
005DF1A1  74 4D                           je 0x1405df1f0
005DF1A3  44 8B CB                        mov r9d, ebx
005DF1A6  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
005DF1AB  45 33 C0                        xor r8d, r8d
005DF1AE  49 8B D7                        mov rdx, r15
005DF1B1  49 8B CE                        mov rcx, r14
005DF1B4  E8 E7 32 E3 FF                  call 0x1404124a0
005DF1B9  85 C0                           test eax, eax
005DF1BB  74 33                           je 0x1405df1f0
005DF1BD  41 8D 44 24 01                  lea eax, [r12 + 1]
005DF1C2  01 84 24 08 01 00 00            add dword ptr [rsp + 0x108], eax
005DF1C9  03 F0                           add esi, eax
005DF1CB  00 87 B1 04 00 00               add byte ptr [rdi + 0x4b1], al
005DF1D1  EB 0B                           jmp 0x1405df1de
005DF1D3  44 8B AC 24 10 01 00 00         mov r13d, dword ptr [rsp + 0x110]
005DF1DB  45 33 E4                        xor r12d, r12d
005DF1DE  41 3B F5                        cmp esi, r13d
005DF1E1  76 0D                           jbe 0x1405df1f0
005DF1E3  BB 02 00 00 00                  mov ebx, 2
005DF1E8  E9 56 01 00 00                  jmp 0x1405df343
005DF1ED  45 33 E4                        xor r12d, r12d
005DF1F0  85 F6                           test esi, esi
005DF1F2  0F 84 3E 01 00 00               je 0x1405df336
005DF1F8  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
005DF1FD  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
005DF202  BB 3F 00 00 00                  mov ebx, 0x3f
005DF207  44 8B E6                        mov r12d, esi
005DF20A  44 8B FE                        mov r15d, esi
005DF20D  FF CE                           dec esi
005DF20F  8B 04 B0                        mov eax, dword ptr [rax + rsi*4]
005DF212  4C 03 E8                        add r13, rax
005DF215  3B F3                           cmp esi, ebx
005DF217  0F 42 DE                        cmovb ebx, esi
005DF21A  E8 FD 5B F1 FF                  call 0x1404f4e1c
005DF21F  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
005DF224  44 0F B6 8C 13 B3 00 00 00      movzx r9d, byte ptr [rbx + rdx + 0xb3]
005DF22D  85 C0                           test eax, eax
005DF22F  0F 84 AB 00 00 00               je 0x1405df2e0
005DF235  44 8B BC 24 08 01 00 00         mov r15d, dword ptr [rsp + 0x108]
005DF23D  41 8B D9                        mov ebx, r9d
005DF240  45 85 FF                        test r15d, r15d
005DF243  74 3C                           je 0x1405df281
005DF245  80 3D 1C 9F 92 00 00            cmp byte ptr [rip + 0x929f1c], 0
005DF24C  74 33                           je 0x1405df281
005DF24E  8B 05 4C 86 88 00               mov eax, dword ptr [rip + 0x88864c]
005DF254  83 E8 01                        sub eax, 1
005DF257  74 19                           je 0x1405df272
005DF259  83 E8 01                        sub eax, 1
005DF25C  74 14                           je 0x1405df272
005DF25E  83 E8 03                        sub eax, 3
005DF261  74 0A                           je 0x1405df26d
005DF263  83 F8 01                        cmp eax, 1
005DF266  74 05                           je 0x1405df26d
005DF268  6B CB 32                        imul ecx, ebx, 0x32
005DF26B  EB 08                           jmp 0x1405df275
005DF26D  6B CB 1E                        imul ecx, ebx, 0x1e
005DF270  EB 03                           jmp 0x1405df275
005DF272  6B CB 46                        imul ecx, ebx, 0x46
005DF275  B8 1F 85 EB 51                  mov eax, 0x51eb851f
005DF27A  F7 E1                           mul ecx
005DF27C  8B DA                           mov ebx, edx
005DF27E  C1 EB 05                        shr ebx, 5
005DF281  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
005DF286  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
005DF28B  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
005DF290  49 8B CE                        mov rcx, r14
005DF293  8B 14 B0                        mov edx, dword ptr [rax + rsi*4]
005DF296  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
005DF29B  4C 8B 04 F0                     mov r8, qword ptr [rax + rsi*8]
005DF29F  E8 FC 31 E3 FF                  call 0x1404124a0
005DF2A4  85 C0                           test eax, eax
005DF2A6  74 1A                           je 0x1405df2c2
005DF2A8  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
005DF2AD  44 8B CB                        mov r9d, ebx
005DF2B0  45 33 C0                        xor r8d, r8d
005DF2B3  49 8B D5                        mov rdx, r13
005DF2B6  49 8B CE                        mov rcx, r14
005DF2B9  E8 E2 31 E3 FF                  call 0x1404124a0
005DF2BE  85 C0                           test eax, eax
005DF2C0  75 69                           jne 0x1405df32b
005DF2C2  45 33 E4                        xor r12d, r12d
005DF2C5  45 85 FF                        test r15d, r15d
005DF2C8  74 57                           je 0x1405df321
005DF2CA  44 38 25 97 9E 92 00            cmp byte ptr [rip + 0x929e97], r12b
005DF2D1  74 4E                           je 0x1405df321
005DF2D3  41 FF CF                        dec r15d
005DF2D6  44 89 BC 24 08 01 00 00         mov dword ptr [rsp + 0x108], r15d
005DF2DE  EB 41                           jmp 0x1405df321
005DF2E0  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
005DF2E5  45 33 E4                        xor r12d, r12d
005DF2E8  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
005DF2ED  49 8B CE                        mov rcx, r14
005DF2F0  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
005DF2F5  8B 14 B0                        mov edx, dword ptr [rax + rsi*4]
005DF2F8  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
005DF2FD  4C 8B 04 F0                     mov r8, qword ptr [rax + rsi*8]
005DF301  E8 9A 31 E3 FF                  call 0x1404124a0
005DF306  85 C0                           test eax, eax
005DF308  74 17                           je 0x1405df321
005DF30A  45 33 C0                        xor r8d, r8d
005DF30D  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
005DF312  49 8B D5                        mov rdx, r13
005DF315  49 8B CE                        mov rcx, r14
005DF318  E8 83 31 E3 FF                  call 0x1404124a0
005DF31D  85 C0                           test eax, eax
005DF31F  75 12                           jne 0x1405df333
005DF321  85 F6                           test esi, esi
005DF323  0F 85 D4 FE FF FF               jne 0x1405df1fd
005DF329  EB 0B                           jmp 0x1405df336
005DF32B  41 8B F4                        mov esi, r12d
005DF32E  45 33 E4                        xor r12d, r12d
005DF331  EB 03                           jmp 0x1405df336
005DF333  41 8B F7                        mov esi, r15d
005DF336  3B B4 24 10 01 00 00            cmp esi, dword ptr [rsp + 0x110]
005DF33D  41 8B DC                        mov ebx, r12d
005DF340  0F 92 C3                        setb bl
005DF343  0F BE 87 A4 04 00 00            movsx eax, byte ptr [rdi + 0x4a4]
005DF34A  41 BF 01 00 00 00               mov r15d, 1
005DF350  3B C3                           cmp eax, ebx
005DF352  75 16                           jne 0x1405df36a
005DF354  8A 87 A2 04 00 00               mov al, byte ptr [rdi + 0x4a2]
005DF35A  41 02 C7                        add al, r15b
005DF35D  44 0F B6 F0                     movzx r14d, al
005DF361  44 88 B7 A2 04 00 00            mov byte ptr [rdi + 0x4a2], r14b
005DF368  EB 41                           jmp 0x1405df3ab
005DF36A  88 9F A4 04 00 00               mov byte ptr [rdi + 0x4a4], bl
005DF370  45 8B F7                        mov r14d, r15d
005DF373  44 88 BF A2 04 00 00            mov byte ptr [rdi + 0x4a2], r15b
005DF37A  BD 04 00 00 00                  mov ebp, 4
005DF37F  E8 98 5A F1 FF                  call 0x1404f4e1c
005DF384  85 C0                           test eax, eax
005DF386  74 23                           je 0x1405df3ab
005DF388  83 FB 02                        cmp ebx, 2
005DF38B  74 1E                           je 0x1405df3ab
005DF38D  44 38 A7 B1 04 00 00            cmp byte ptr [rdi + 0x4b1], r12b
005DF394  76 15                           jbe 0x1405df3ab
005DF396  44 38 25 CB 9D 92 00            cmp byte ptr [rip + 0x929dcb], r12b
005DF39D  74 0C                           je 0x1405df3ab
005DF39F  44 88 A7 B1 04 00 00            mov byte ptr [rdi + 0x4b1], r12b
005DF3A6  BD 04 08 00 00                  mov ebp, 0x804
005DF3AB  83 3D 92 BE 92 00 05            cmp dword ptr [rip + 0x92be92], 5
005DF3B2  0F 85 97 00 00 00               jne 0x1405df44f
005DF3B8  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
005DF3BF  83 CD 10                        or ebp, 0x10
005DF3C2  66 89 B0 86 02 00 00            mov word ptr [rax + 0x286], si
005DF3C9  8B 9C 24 08 01 00 00            mov ebx, dword ptr [rsp + 0x108]
005DF3D0  8A 87 A0 04 00 00               mov al, byte ptr [rdi + 0x4a0]
005DF3D6  24 FD                           and al, 0xfd
005DF3D8  0C 04                           or al, 4
005DF3DA  44 38 25 A5 76 9E 00            cmp byte ptr [rip + 0x9e76a5], r12b
005DF3E1  88 87 A0 04 00 00               mov byte ptr [rdi + 0x4a0], al
005DF3E7  74 2E                           je 0x1405df417
005DF3E9  48 8B 8F 08 05 00 00            mov rcx, qword ptr [rdi + 0x508]
005DF3F0  0F BA ED 07                     bts ebp, 7
005DF3F4  0F B7 81 86 02 00 00            movzx eax, word ptr [rcx + 0x286]
005DF3FB  66 89 81 88 02 00 00            mov word ptr [rcx + 0x288], ax
005DF402  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
005DF409  0F B7 88 86 02 00 00            movzx ecx, word ptr [rax + 0x286]
005DF410  66 89 8F F0 04 00 00            mov word ptr [rdi + 0x4f0], cx
005DF417  41 0B EF                        or ebp, r15d
005DF41A  E8 FD 59 F1 FF                  call 0x1404f4e1c
005DF41F  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
005DF424  48 8B CF                        mov rcx, rdi
005DF427  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
005DF42C  49 8B D6                        mov rdx, r14
005DF42F  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
005DF434  85 C0                           test eax, eax
005DF436  0F 85 EF 00 00 00               jne 0x1405df52b
005DF43C  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
005DF440  66 89 74 24 20                  mov word ptr [rsp + 0x20], si
005DF445  E8 22 27 F1 FF                  call 0x1404f1b6c
005DF44A  E9 FB 00 00 00                  jmp 0x1405df54a
005DF44F  83 FB 02                        cmp ebx, 2
005DF452  75 6B                           jne 0x1405df4bf
005DF454  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
005DF459  0F B6 80 B2 00 00 00            movzx eax, byte ptr [rax + 0xb2]
005DF460  44 3B F0                        cmp r14d, eax
005DF463  0F 82 60 FF FF FF               jb 0x1405df3c9
005DF469  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
005DF470  83 CD 20                        or ebp, 0x20
005DF473  66 89 B0 86 02 00 00            mov word ptr [rax + 0x286], si
005DF47A  E8 9D 59 F1 FF                  call 0x1404f4e1c
005DF47F  85 C0                           test eax, eax
005DF481  0F 84 42 FF FF FF               je 0x1405df3c9
005DF487  44 38 A7 B1 04 00 00            cmp byte ptr [rdi + 0x4b1], r12b
005DF48E  0F 86 35 FF FF FF               jbe 0x1405df3c9
005DF494  44 38 25 CD 9C 92 00            cmp byte ptr [rip + 0x929ccd], r12b
005DF49B  8B 9C 24 08 01 00 00            mov ebx, dword ptr [rsp + 0x108]
005DF4A2  0F 84 28 FF FF FF               je 0x1405df3d0
005DF4A8  44 00 BF B0 04 00 00            add byte ptr [rdi + 0x4b0], r15b
005DF4AF  0F BA ED 09                     bts ebp, 9
005DF4B3  44 88 A7 B1 04 00 00            mov byte ptr [rdi + 0x4b1], r12b
005DF4BA  E9 11 FF FF FF                  jmp 0x1405df3d0
005DF4BF  41 3B DF                        cmp ebx, r15d
005DF4C2  0F 85 01 FF FF FF               jne 0x1405df3c9
005DF4C8  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
005DF4CD  0F B6 80 B1 00 00 00            movzx eax, byte ptr [rax + 0xb1]
005DF4D4  44 3B F0                        cmp r14d, eax
005DF4D7  0F 82 EC FE FF FF               jb 0x1405df3c9
005DF4DD  48 8B 87 08 05 00 00            mov rax, qword ptr [rdi + 0x508]
005DF4E4  83 CD 40                        or ebp, 0x40
005DF4E7  66 89 B0 86 02 00 00            mov word ptr [rax + 0x286], si
005DF4EE  E8 29 59 F1 FF                  call 0x1404f4e1c
005DF4F3  85 C0                           test eax, eax
005DF4F5  0F 84 CE FE FF FF               je 0x1405df3c9
005DF4FB  44 38 A7 B0 04 00 00            cmp byte ptr [rdi + 0x4b0], r12b
005DF502  0F 86 C1 FE FF FF               jbe 0x1405df3c9
005DF508  44 38 25 59 9C 92 00            cmp byte ptr [rip + 0x929c59], r12b
005DF50F  8B 9C 24 08 01 00 00            mov ebx, dword ptr [rsp + 0x108]
005DF516  0F 84 B4 FE FF FF               je 0x1405df3d0
005DF51C  88 9F B0 04 00 00               mov byte ptr [rdi + 0x4b0], bl
005DF522  0F BA ED 0A                     bts ebp, 0xa
005DF526  E9 A5 FE FF FF                  jmp 0x1405df3d0
005DF52B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
005DF533  66 89 5C 24 38                  mov word ptr [rsp + 0x38], bx
005DF538  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005DF53C  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
005DF540  66 89 74 24 20                  mov word ptr [rsp + 0x20], si
005DF545  E8 92 48 F1 FF                  call 0x1404f3ddc
005DF54A  8B 7C 24 60                     mov edi, dword ptr [rsp + 0x60]
005DF54E  41 03 FF                        add edi, r15d
005DF551  3B 3D 89 8E 92 00               cmp edi, dword ptr [rip + 0x928e89]
005DF557  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
005DF55B  0F 82 E6 F7 FF FF               jb 0x1405ded47
005DF561  E8 EA 41 E3 FF                  call 0x140413750
005DF566  41 8A C7                        mov al, r15b
005DF569  48 81 C4 B8 00 00 00            add rsp, 0xb8
005DF570  41 5F                           pop r15
005DF572  41 5E                           pop r14
005DF574  41 5D                           pop r13
005DF576  41 5C                           pop r12
005DF578  5F                              pop rdi
005DF579  5E                              pop rsi
005DF57A  5D                              pop rbp
005DF57B  5B                              pop rbx
005DF57C  C3                              ret
005DF57D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmCheckComputeHeteroResponseEx(void)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int16 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int16 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (184);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    a1 = (a1) * ((int)(*(unsigned int *)(v_rip + 9625906)));
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    v_stack_mA0 = *(unsigned __int64 *)(v_rip + 9602010);
    result = (*(unsigned __int64 *)(v_rip + 8558275) + 40) + (a1);
    v_stack_m88 = result;
    v_stack_mA8 = *(unsigned __int64 *)(v_rip + 9601955);
    v_stack_m90 = *(unsigned __int64 *)(v_rip + 9601951);
    if ((*(unsigned int *)(v_rip + 10380095)) != 4) goto loc_005DF561;
    result = PpmHeteroIsMultiClassParkingEnabled(a1, *(unsigned __int64 *)(v_rip + 8558275), a3, a4);
    v_r12 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_005DED32;
    result = PpmCheckComputeMultiClassHeteroResponseEx(a1, *(unsigned __int64 *)(v_rip + 8558275), a3, a4);
    goto loc_005DF566;
loc_005DED32:
    v_stack_m98 = 0;
    if ((*(unsigned int *)(v_rip + 9606823)) == 0) goto loc_005DF561;
loc_005DED47:
    v_rdi = (0) * (0);
    v_stack_m80 = 0;
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 9606777));
    v_stack_m50 = v_rdi;
    if ((*(unsigned __int8 *)(v_rip + 10386720)) == 0) goto loc_005DED8E;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 1288) + 640)) != 0) goto loc_005DED8E;
    if ((*(unsigned int *)(v_rip + 10379952)) == 0) goto loc_005DF54A;
loc_005DED8E:
    a1 = 0;
    v_stack_mB8 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_p18 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 1288) + 648));
    v_stack_p8 = 0;
    v_stack_p20 = 0;
    v_stack_p10 = 0;
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(a1, *(unsigned __int64 *)(v_rip + 8558275), a3, a4);
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_005DEE2E;
    if ((*(unsigned __int8 *)(v_rip + 9610111)) == 0) goto loc_005DEE2E;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8948399)) - 2)) & (0xFFFFFFF9ULL)) != 0) goto loc_005DEE02;
    result = 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8948399)))) == 8) {
        result = 0;
    }
    v_stack_p10 = (unsigned int)(*(unsigned __int8 *)(v_rdi + 1200));
    v_r13 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1200)) != 0) { v_r13 = (unsigned int)((unsigned __int8)(result)); }
    v_stack_p20 = (unsigned int)(v_r13);
loc_005DEE2E:
    v_stack_m58 = 0;
    v_stack_m68 = v_rdi + 48;
    v_stack_m60 = *(unsigned __int64 *)(v_rdi + 48 + 8);
    result = KeEnumerateNextProcessor(v_stack_p8, v_stack_m68, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_005DEEE0;
loc_005DEE6C:
    result = KeGetPrcb((unsigned int)(v_stack_p8), v_stack_m68, a3, a4);
    if ((*(unsigned int *)(v_rip + 9618373)) != 5) {
        a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 35248 + 40))) - (*(unsigned int *)(result + 35248 + 48)));
    }
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, a2, a3, a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 9602010) + 0 * 4) = (unsigned int)(result);
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, (unsigned int)(*(unsigned int *)(result + 35248 + 52)), a3, a4);
    *(unsigned int *)(v_stack_m90 + 0 * 4) = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_r15 = (0) + ((unsigned int)((unsigned int)(result)));
    v_r12 = (v_r12) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9602010) + 0 * 4)));
    v_rbx = (unsigned int)((0) + 1);
    result = KeEnumerateNextProcessor(v_stack_p8, v_stack_m68, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_005DEE6C;
    v_stack_mB8 = v_r15;
    v_stack_m78 = v_r12;
loc_005DEEE0:
    result = qsort(*(unsigned __int64 *)(v_rip + 9602010), v_rbx, 4, v_rip - 1439351);
    result = qsort(v_stack_m90, v_rbx, 4, v_rip - 1439380);
    v_rbx = 0;
    v_stack_mB0 = 0;
    if ((unsigned int)(*(unsigned __int16 *)(v_rdi + 10)) == 0) goto loc_005DEF63;
loc_005DEF39:
    result = (v_r12) * (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1128) + *(unsigned __int16 *)(v_rdi + 10) * 8));
    a4 = (0) + (result);
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rdi + 10)) - 1);
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rdi + 10)))) - 1;
    *(unsigned __int64 *)(v_stack_mA8 + a1 * 8) = a4;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rdi + 10)))) * (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1128) + *(unsigned __int16 *)(v_rdi + 10) * 8));
    v_r10 = (0) + (result);
    if ((unsigned int)(a1) != 0) goto loc_005DEF39;
    v_stack_mB0 = v_r10;
loc_005DEF63:
    if ((unsigned int)((unsigned int)(v_stack_p18)) == 0) goto loc_005DEFAE;
    v_rsi = (v_stack_m90) - (*(unsigned __int64 *)(v_rip + 9602010));
loc_005DEF7A:
    v_r15 = (v_r15) - ((unsigned int)(*(unsigned int *)(v_rsi + *(unsigned __int64 *)(v_rip + 9602010) * 1)));
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(a1, a2, *(unsigned __int64 *)(v_rdi + 1128) + *(unsigned __int16 *)(v_rdi + 10) * 8 - 8, a4);
    if ((unsigned int)(result) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 9602010));
        v_r12 = (v_r12) - (result);
    }
    v_rbx = (*(unsigned __int64 *)(v_rip + 9602010)) + (4);
    v_r14 = ((unsigned int)(v_stack_p18)) - (1);
    if (condition_is_not_equal) goto loc_005DEF7A;
    v_rbx = 0;
    v_stack_mB8 = v_r15;
    v_stack_m78 = v_r12;
loc_005DEFAE:
    v_stack_p8 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 1288) + 640));
    v_r14 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 1288) + 640);
    if ((*(unsigned __int8 *)(v_rip + 10386130)) != 0) {
        v_r14 = *(unsigned __int16 *)(v_rdi + 10);
        v_stack_p8 = (unsigned __int16)(v_r14);
    }
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(a1, a2, *(unsigned __int64 *)(v_rdi + 1128) + *(unsigned __int16 *)(v_rdi + 10) * 8 - 8, a4);
    if ((unsigned int)(result) != 0) {
        result = 1;
        a1 = v_r12;
        if (v_r12 < result) { a1 = result; }
        a2 = 0;
        result = (result) * (v_r15);
        a1 = 100;
        if (((unsigned int)(result)) > ((unsigned int)(a1))) { result = (unsigned int)(a1); }
        v_stack_m70 = result;
    }
    if (v_stack_p18 >= ((unsigned int)((unsigned __int16)(v_r14)))) goto loc_005DF0C6;
loc_005DF039:
    result = 63;
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 63) { result = (unsigned int)((unsigned int)(v_stack_p18)); }
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, (unsigned int)(*(unsigned int *)(v_stack_mA0 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))) * 4)), *(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))) * 8), *(unsigned __int8 *)(result + v_stack_m88 * 1 + 307));
    if ((unsigned int)(result) == 0) goto loc_005DF09C;
    a3 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, v_stack_mB8, a3, *(unsigned __int8 *)(result + v_stack_m88 * 1 + 307));
    if ((unsigned int)(result) == 0) goto loc_005DF09C;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_p18)) + 1);
    v_r15 = (v_stack_mB8) - ((unsigned int)(*(unsigned int *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))) * 4)));
    v_stack_mB8 = v_r15;
    if (((unsigned int)(v_rsi)) < ((unsigned int)((unsigned __int16)(v_r14)))) goto loc_005DF039;
    goto loc_005DF0A1;
loc_005DF09C:
loc_005DF0A1:
loc_005DF0C6:
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_mB0, v_stack_mB8, a3, *(unsigned __int8 *)(result + v_stack_m88 * 1 + 307));
    if ((unsigned int)(result) == 0) goto loc_005DF1D3;
    if ((*(unsigned __int8 *)(v_rip + 9609358)) == 0) goto loc_005DF1D3;
    if ((unsigned __int8)((unsigned int)(v_stack_p20)) != 0) goto loc_005DF1DB;
    if (((unsigned int)(v_rsi)) != ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_005DF1DB;
    if (((unsigned int)(v_rsi)) >= ((unsigned int)((unsigned __int16)(v_stack_p8)))) goto loc_005DF1ED;
    if (((unsigned int)(v_stack_m70)) > (*(unsigned int *)(v_rip + 8570612))) goto loc_005DF1ED;
    if (v_stack_m78 < 1000) goto loc_005DF1ED;
    result = 63;
    if (((unsigned int)(v_rsi)) < 63) { result = (unsigned int)(v_rsi); }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 8947547))) - (1));
    if (condition_is_equal) goto loc_005DF165;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_005DF165;
    result = (unsigned int)((result) - (3));
    if (condition_is_equal) goto loc_005DF15F;
    if (((unsigned int)(result)) == 1) goto loc_005DF15F;
    a1 = (unsigned int)((v_stack_m88) * ((unsigned int)(*(unsigned __int8 *)(result + v_stack_m88 * 1 + 307))));
    goto loc_005DF169;
loc_005DF15F:
    a1 = (unsigned int)((a1) * ((unsigned int)(*(unsigned __int8 *)(result + v_stack_m88 * 1 + 307))));
    goto loc_005DF169;
loc_005DF165:
    a1 = (unsigned int)((a1) * ((unsigned int)(*(unsigned __int8 *)(result + v_stack_m88 * 1 + 307))));
loc_005DF169:
    v_r12 = 0;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mB8))) >> (5));
    v_stack_mD8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, (unsigned int)(*(unsigned int *)(v_stack_mA0 + (unsigned int)((unsigned int)(v_rsi)) * 4)), *(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)(v_rsi)) * 8), *(unsigned __int8 *)(result + v_stack_m88 * 1 + 307));
    if ((unsigned int)(result) == 0) goto loc_005DF1F0;
    v_stack_mD8 = 0;
    a3 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, v_stack_mB8, a3, (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) == 0) goto loc_005DF1F0;
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_r12 + 1)));
    goto loc_005DF1DE;
loc_005DF1D3:
loc_005DF1DB:
    v_r12 = 0;
loc_005DF1DE:
    if (((unsigned int)(v_rsi)) <= ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_005DF1F0;
    goto loc_005DF343;
loc_005DF1ED:
    v_r12 = 0;
loc_005DF1F0:
    if ((unsigned int)(v_rsi) == 0) goto loc_005DF336;
loc_005DF1FD:
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_r13 = (v_stack_mB8) + ((unsigned int)(*(unsigned int *)(v_stack_m90 + v_rsi * 4)));
    v_rbx = 63;
    if (((unsigned int)(v_rsi)) < 63) { v_rbx = (unsigned int)(v_rsi); }
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_mB0, v_stack_mB8, a3, (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) == 0) goto loc_005DF2E0;
    if ((unsigned int)((unsigned int)(v_stack_p10)) == 0) goto loc_005DF281;
    if ((*(unsigned __int8 *)(v_rip + 9608988)) == 0) goto loc_005DF281;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 8947276))) - (1));
    if (condition_is_equal) goto loc_005DF272;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_005DF272;
    result = (unsigned int)((result) - (3));
    if (condition_is_equal) goto loc_005DF26D;
    if (((unsigned int)(result)) == 1) goto loc_005DF26D;
    a1 = (unsigned int)((v_stack_mB0) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rbx + v_stack_m88 * 1 + 179))))));
    goto loc_005DF275;
loc_005DF26D:
    a1 = (unsigned int)((a1) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rbx + v_stack_m88 * 1 + 179))))));
    goto loc_005DF275;
loc_005DF272:
    a1 = (unsigned int)((a1) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rbx + v_stack_m88 * 1 + 179))))));
loc_005DF275:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m88))) >> (5));
loc_005DF281:
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, (unsigned int)(*(unsigned int *)(v_stack_mA0 + v_rsi * 4)), *(unsigned __int64 *)(v_stack_mA8 + v_rsi * 8), *(unsigned __int8 *)(v_rbx + v_stack_m88 * 1 + 179));
    if ((unsigned int)(result) == 0) goto loc_005DF2C2;
    a3 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, v_r13, a3, (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) != 0) goto loc_005DF32B;
loc_005DF2C2:
    v_r12 = 0;
    if ((unsigned int)((unsigned int)(v_stack_p10)) == 0) goto loc_005DF321;
    if ((*(unsigned __int8 *)(v_rip + 9608855)) == 0) goto loc_005DF321;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p10)) - 1);
    v_stack_p10 = (unsigned int)(v_r15);
    goto loc_005DF321;
loc_005DF2E0:
    v_r12 = 0;
    v_stack_mD8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, (unsigned int)(*(unsigned int *)(v_stack_mA0 + v_rsi * 4)), *(unsigned __int64 *)(v_stack_mA8 + v_rsi * 8), (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) == 0) goto loc_005DF321;
    a3 = 0;
    v_stack_mD8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, v_r13, a3, (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) != 0) goto loc_005DF333;
loc_005DF321:
    if ((unsigned int)(v_rsi) != 0) goto loc_005DF1FD;
    goto loc_005DF336;
loc_005DF32B:
    v_r12 = 0;
    goto loc_005DF336;
loc_005DF333:
loc_005DF336:
    v_rbx = (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) < v_stack_p18) ? 1 : 0;
loc_005DF343:
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(v_stack_m50 + 1188)))) != ((unsigned int)(v_rbx))) goto loc_005DF36A;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m50 + 1186)) + (1));
    *(unsigned __int8 *)(v_stack_m50 + 1186) = (unsigned __int8)((unsigned __int8)(result));
    goto loc_005DF3AB;
loc_005DF36A:
    *(unsigned __int8 *)(v_stack_m50 + 1188) = (unsigned __int8)(v_rbx);
    *(unsigned __int8 *)(v_stack_m50 + 1186) = 1;
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_mB0, v_r13, a3, (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) == 0) goto loc_005DF3AB;
    if (((unsigned int)(v_rbx)) == 2) goto loc_005DF3AB;
    if ((*(unsigned __int8 *)(v_stack_m50 + 1201)) <= 0) goto loc_005DF3AB;
    v_rbp = 4;
    if ((*(unsigned __int8 *)(v_rip + 9608651)) != 0) {
        *(unsigned __int8 *)(v_stack_m50 + 1201) = 0;
        v_rbp = 0x804ULL;
    }
    if ((*(unsigned int *)(v_rip + 9617042)) != 5) goto loc_005DF44F;
    v_rbp = (unsigned int)((v_rbp) | (16));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m50 + 1288) + 646) = (unsigned __int16)((unsigned int)((unsigned int)(v_r15)));
loc_005DF3C9:
loc_005DF3D0:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m50 + 1184)) & (253));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(v_stack_m50 + 1184) = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(v_rip + 10385061)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m50 + 1288);
        result = *(unsigned __int16 *)(a1 + 646);
        *(unsigned __int16 *)(a1 + 648) = (unsigned __int16)(result);
        result = *(unsigned __int64 *)(v_stack_m50 + 1288);
        a1 = *(unsigned __int16 *)(result + 646);
        *(unsigned __int16 *)(v_stack_m50 + 1264) = (unsigned __int16)(a1);
    }
    v_rbp = (unsigned int)((v_rbp) | (1));
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(a1, v_r13, a3, (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) != 0) goto loc_005DF52B;
    v_stack_mD0 = (unsigned int)(v_rbp);
    v_stack_mD8 = (unsigned __int16)((unsigned int)((unsigned int)(v_r15)));
    result = PpmEventTraceHeteroResponseEx(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
    goto loc_005DF54A;
loc_005DF44F:
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 2) goto loc_005DF4BF;
    if (((unsigned int)(v_stack_mA0)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_m88 + 178)))) goto loc_005DF3C9;
    v_rbp = (unsigned int)((v_rbp) | (32));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m50 + 1288) + 646) = (unsigned __int16)((unsigned int)((unsigned int)(v_r15)));
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
    if ((unsigned int)(result) == 0) goto loc_005DF3C9;
    if ((*(unsigned __int8 *)(v_stack_m50 + 1201)) <= 0) goto loc_005DF3C9;
    if ((*(unsigned __int8 *)(v_rip + 9608397)) == 0) goto loc_005DF3D0;
    *(unsigned __int8 *)(v_stack_m50 + 1201) = 0;
    goto loc_005DF3D0;
loc_005DF4BF:
    if (((unsigned int)((unsigned int)(v_stack_p10))) != 1) goto loc_005DF3C9;
    if (((unsigned int)(v_stack_mA0)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_m88 + 177)))) goto loc_005DF3C9;
    v_rbp = (unsigned int)((v_rbp) | (64));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m50 + 1288) + 646) = (unsigned __int16)((unsigned int)((unsigned int)(v_r15)));
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
    if ((unsigned int)(result) == 0) goto loc_005DF3C9;
    if ((*(unsigned __int8 *)(v_stack_m50 + 1200)) <= 0) goto loc_005DF3C9;
    if ((*(unsigned __int8 *)(v_rip + 9608281)) == 0) goto loc_005DF3D0;
    *(unsigned __int8 *)(v_stack_m50 + 1200) = (unsigned __int8)((unsigned int)(v_stack_p10));
    goto loc_005DF3D0;
loc_005DF52B:
    v_stack_mC0 = (unsigned __int16)((unsigned int)(v_stack_p10));
    v_stack_mC8 = (unsigned int)(v_stack_m70);
    v_stack_mD0 = (unsigned int)(v_rbp);
    v_stack_mD8 = (unsigned __int16)((unsigned int)((unsigned int)(v_r15)));
    result = PpmEventTraceHeteroResponseExV1(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
loc_005DF54A:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m98)) + (1));
    v_stack_m98 = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) < (*(unsigned int *)(v_rip + 9604745))) goto loc_005DED47;
loc_005DF561:
    result = PpmParkCalculateUnparkCount(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
loc_005DF566:
    v_rsp = (v_rsp) + (184);
    return 1;
}
```

## 5. (Beta) C Style

```c
void PpmCheckComputeHeteroResponseEx(void)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint16_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint16_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (184);
    result = 0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    a1 = (a1) * ((int32_t)(*(uint32_t *)(v_rip + 0x92E132)));
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    v_stack_mA0 = *(uint64_t *)(v_rip + 0x9283DA);
    result = (*(uint64_t *)(v_rip + 0x8296C3) + 40) + (a1);
    v_stack_m88 = result;
    v_stack_mA8 = *(uint64_t *)(v_rip + 0x9283A3);
    v_stack_m90 = *(uint64_t *)(v_rip + 0x92839F);
    if ((*(uint32_t *)(v_rip + 0x9E633F)) != 4) goto loc_005DF561;
    result = PpmHeteroIsMultiClassParkingEnabled(a1, *(uint64_t *)(v_rip + 0x8296C3), a3, a4);
    local_r12 = 0;
    if ((uint8_t)(result) == 0) goto loc_005DED32;
    result = PpmCheckComputeMultiClassHeteroResponseEx(a1, *(uint64_t *)(v_rip + 0x8296C3), a3, a4);
    goto loc_005DF566;
loc_005DED32:
    v_stack_m98 = 0;
    if ((*(uint32_t *)(v_rip + 0x9296A7)) == 0) goto loc_005DF561;
loc_005DED47:
    local_rdi = (0) * (0);
    v_stack_m80 = 0;
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0x929679));
    v_stack_m50 = local_rdi;
    if ((*(uint8_t *)(v_rip + 0x9E7D20)) == 0) goto loc_005DED8E;
    if ((*(uint16_t *)(*(uint64_t *)(local_rdi + 0x508) + 0x280)) != 0) goto loc_005DED8E;
    if ((*(uint32_t *)(v_rip + 0x9E62B0)) == 0) goto loc_005DF54A;
loc_005DED8E:
    a1 = 0;
    v_stack_mB8 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    v_stack_p18 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rdi + 0x508) + 0x288));
    v_stack_p8 = 0;
    v_stack_p20 = 0;
    v_stack_p10 = 0;
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(a1, *(uint64_t *)(v_rip + 0x8296C3), a3, a4);
    a2 = 0;
    if ((uint32_t)(result) == 0) goto loc_005DEE2E;
    if ((*(uint8_t *)(v_rip + 0x92A37F)) == 0) goto loc_005DEE2E;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x888AAF)) - 2)) & (0xFFFFFFF9ULL)) != 0) goto loc_005DEE02;
    result = 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x888AAF)))) == 8) {
        result = 0;
    }
    v_stack_p10 = (uint32_t)(*(uint8_t *)(local_rdi + 0x4B0));
    local_r13 = 0;
    if ((uint8_t)(*(uint8_t *)(local_rdi + 0x4B0)) != 0) { local_r13 = (uint32_t)((uint8_t)(result)); }
    v_stack_p20 = (uint32_t)(local_r13);
loc_005DEE2E:
    v_stack_m58 = 0;
    v_stack_m68 = local_rdi + 48;
    v_stack_m60 = *(uint64_t *)(local_rdi + 0x30 + 0x8);
    result = KeEnumerateNextProcessor(v_stack_p8, v_stack_m68, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_005DEEE0;
loc_005DEE6C:
    result = KeGetPrcb((uint32_t)(v_stack_p8), v_stack_m68, a3, a4);
    if ((*(uint32_t *)(v_rip + 0x92C3C5)) != 5) {
        a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x89B0 + 0x28))) - (*(uint32_t *)(result + 0x89B0 + 0x30)));
    }
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, a2, a3, a4);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x9283DA) + 0x0 * 4) = (uint32_t)(result);
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, (uint32_t)(*(uint32_t *)(result + 0x89B0 + 0x34)), a3, a4);
    *(uint32_t *)(v_stack_m90 + 0x0 * 4) = (uint32_t)((uint32_t)((uint32_t)(result)));
    local_r15 = (0) + ((uint32_t)((uint32_t)(result)));
    local_r12 = (local_r12) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x9283DA) + 0x0 * 4)));
    local_rbx = (uint32_t)((0) + 1);
    result = KeEnumerateNextProcessor(v_stack_p8, v_stack_m68, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_005DEE6C;
    v_stack_mB8 = local_r15;
    v_stack_m78 = local_r12;
loc_005DEEE0:
    result = qsort(*(uint64_t *)(v_rip + 0x9283DA), local_rbx, 4, v_rip - 1439351);
    result = qsort(v_stack_m90, local_rbx, 4, v_rip - 1439380);
    local_rbx = 0;
    v_stack_mB0 = 0;
    if ((uint32_t)(*(uint16_t *)(local_rdi + 0xA)) == 0) goto loc_005DEF63;
loc_005DEF39:
    result = (local_r12) * (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x468) + *(uint16_t *)(local_rdi + 0xA) * 8));
    a4 = (0) + (result);
    a1 = (uint32_t)((*(uint16_t *)(local_rdi + 0xA)) - 1);
    a2 = ((uint32_t)((uint32_t)(*(uint16_t *)(local_rdi + 0xA)))) - 1;
    *(uint64_t *)(v_stack_mA8 + a1 * 8) = a4;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(local_rdi + 0xA)))) * (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x468) + *(uint16_t *)(local_rdi + 0xA) * 8));
    local_r10 = (0) + (result);
    if ((uint32_t)(a1) != 0) goto loc_005DEF39;
    v_stack_mB0 = local_r10;
loc_005DEF63:
    if ((uint32_t)((uint32_t)(v_stack_p18)) == 0) goto loc_005DEFAE;
    local_rsi = (v_stack_m90) - (*(uint64_t *)(v_rip + 0x9283DA));
loc_005DEF7A:
    local_r15 = (local_r15) - ((uint32_t)(*(uint32_t *)(local_rsi + *(uint64_t *)(v_rip + 0x9283DA) * 1)));
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(a1, a2, *(uint64_t *)(local_rdi + 0x468) + *(uint16_t *)(local_rdi + 0xA) * 8 - 8, a4);
    if ((uint32_t)(result) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x9283DA));
        local_r12 = (local_r12) - (result);
    }
    local_rbx = (*(uint64_t *)(v_rip + 0x9283DA)) + (4);
    local_r14 = ((uint32_t)(v_stack_p18)) - (1);
    if (condition_is_not_equal) goto loc_005DEF7A;
    local_rbx = 0;
    v_stack_mB8 = local_r15;
    v_stack_m78 = local_r12;
loc_005DEFAE:
    v_stack_p8 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rdi + 0x508) + 0x280));
    local_r14 = *(uint16_t *)(*(uint64_t *)(local_rdi + 0x508) + 0x280);
    if ((*(uint8_t *)(v_rip + 0x9E7AD2)) != 0) {
        local_r14 = *(uint16_t *)(local_rdi + 0xA);
        v_stack_p8 = (uint16_t)(local_r14);
    }
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(a1, a2, *(uint64_t *)(local_rdi + 0x468) + *(uint16_t *)(local_rdi + 0xA) * 8 - 8, a4);
    if ((uint32_t)(result) != 0) {
        result = 1;
        a1 = local_r12;
        if (local_r12 < result) { a1 = result; }
        a2 = 0;
        result = (result) * (local_r15);
        a1 = 100;
        if (((uint32_t)(result)) > ((uint32_t)(a1))) { result = (uint32_t)(a1); }
        v_stack_m70 = result;
    }
    if (v_stack_p18 >= ((uint32_t)((uint16_t)(local_r14)))) goto loc_005DF0C6;
loc_005DF039:
    result = 63;
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 63) { result = (uint32_t)((uint32_t)(v_stack_p18)); }
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, (uint32_t)(*(uint32_t *)(v_stack_mA0 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))) * 4)), *(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))) * 8), *(uint8_t *)(result + v_stack_m88 * 1 + 0x133));
    if ((uint32_t)(result) == 0) goto loc_005DF09C;
    a3 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, v_stack_mB8, a3, *(uint8_t *)(result + v_stack_m88 * 1 + 0x133));
    if ((uint32_t)(result) == 0) goto loc_005DF09C;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_p18)) + 1);
    local_r15 = (v_stack_mB8) - ((uint32_t)(*(uint32_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))) * 4)));
    v_stack_mB8 = local_r15;
    if (((uint32_t)(local_rsi)) < ((uint32_t)((uint16_t)(local_r14)))) goto loc_005DF039;
    goto loc_005DF0A1;
loc_005DF09C:
loc_005DF0A1:
loc_005DF0C6:
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_mB0, v_stack_mB8, a3, *(uint8_t *)(result + v_stack_m88 * 1 + 0x133));
    if ((uint32_t)(result) == 0) goto loc_005DF1D3;
    if ((*(uint8_t *)(v_rip + 0x92A08E)) == 0) goto loc_005DF1D3;
    if ((uint8_t)((uint32_t)(v_stack_p20)) != 0) goto loc_005DF1DB;
    if (((uint32_t)(local_rsi)) != ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_005DF1DB;
    if (((uint32_t)(local_rsi)) >= ((uint32_t)((uint16_t)(v_stack_p8)))) goto loc_005DF1ED;
    if (((uint32_t)(v_stack_m70)) > (*(uint32_t *)(v_rip + 0x82C6F4))) goto loc_005DF1ED;
    if (v_stack_m78 < 1000) goto loc_005DF1ED;
    result = 63;
    if (((uint32_t)(local_rsi)) < 63) { result = (uint32_t)(local_rsi); }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x88875B))) - (1));
    if (condition_is_equal) goto loc_005DF165;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_005DF165;
    result = (uint32_t)((result) - (3));
    if (condition_is_equal) goto loc_005DF15F;
    if (((uint32_t)(result)) == 1) goto loc_005DF15F;
    a1 = (uint32_t)((v_stack_m88) * ((uint32_t)(*(uint8_t *)(result + v_stack_m88 * 1 + 0x133))));
    goto loc_005DF169;
loc_005DF15F:
    a1 = (uint32_t)((a1) * ((uint32_t)(*(uint8_t *)(result + v_stack_m88 * 1 + 0x133))));
    goto loc_005DF169;
loc_005DF165:
    a1 = (uint32_t)((a1) * ((uint32_t)(*(uint8_t *)(result + v_stack_m88 * 1 + 0x133))));
loc_005DF169:
    local_r12 = 0;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mB8))) >> (5));
    v_stack_mD8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, (uint32_t)(*(uint32_t *)(v_stack_mA0 + (uint32_t)((uint32_t)(local_rsi)) * 4)), *(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)(local_rsi)) * 8), *(uint8_t *)(result + v_stack_m88 * 1 + 0x133));
    if ((uint32_t)(result) == 0) goto loc_005DF1F0;
    v_stack_mD8 = 0;
    a3 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, v_stack_mB8, a3, (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) == 0) goto loc_005DF1F0;
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_r12 + 1)));
    goto loc_005DF1DE;
loc_005DF1D3:
loc_005DF1DB:
    local_r12 = 0;
loc_005DF1DE:
    if (((uint32_t)(local_rsi)) <= ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_005DF1F0;
    goto loc_005DF343;
loc_005DF1ED:
    local_r12 = 0;
loc_005DF1F0:
    if ((uint32_t)(local_rsi) == 0) goto loc_005DF336;
loc_005DF1FD:
    local_rsi = (uint32_t)((local_rsi) - 1);
    local_r13 = (v_stack_mB8) + ((uint32_t)(*(uint32_t *)(v_stack_m90 + local_rsi * 4)));
    local_rbx = 63;
    if (((uint32_t)(local_rsi)) < 63) { local_rbx = (uint32_t)(local_rsi); }
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_mB0, v_stack_mB8, a3, (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) == 0) goto loc_005DF2E0;
    if ((uint32_t)((uint32_t)(v_stack_p10)) == 0) goto loc_005DF281;
    if ((*(uint8_t *)(v_rip + 0x929F1C)) == 0) goto loc_005DF281;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x88864C))) - (1));
    if (condition_is_equal) goto loc_005DF272;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_005DF272;
    result = (uint32_t)((result) - (3));
    if (condition_is_equal) goto loc_005DF26D;
    if (((uint32_t)(result)) == 1) goto loc_005DF26D;
    a1 = (uint32_t)((v_stack_mB0) * ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_rbx + v_stack_m88 * 1 + 0xB3))))));
    goto loc_005DF275;
loc_005DF26D:
    a1 = (uint32_t)((a1) * ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_rbx + v_stack_m88 * 1 + 0xB3))))));
    goto loc_005DF275;
loc_005DF272:
    a1 = (uint32_t)((a1) * ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_rbx + v_stack_m88 * 1 + 0xB3))))));
loc_005DF275:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m88))) >> (5));
loc_005DF281:
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, (uint32_t)(*(uint32_t *)(v_stack_mA0 + local_rsi * 4)), *(uint64_t *)(v_stack_mA8 + local_rsi * 8), *(uint8_t *)(local_rbx + v_stack_m88 * 1 + 0xB3));
    if ((uint32_t)(result) == 0) goto loc_005DF2C2;
    a3 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, local_r13, a3, (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) != 0) goto loc_005DF32B;
loc_005DF2C2:
    local_r12 = 0;
    if ((uint32_t)((uint32_t)(v_stack_p10)) == 0) goto loc_005DF321;
    if ((*(uint8_t *)(v_rip + 0x929E97)) == 0) goto loc_005DF321;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p10)) - 1);
    v_stack_p10 = (uint32_t)(local_r15);
    goto loc_005DF321;
loc_005DF2E0:
    local_r12 = 0;
    v_stack_mD8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, (uint32_t)(*(uint32_t *)(v_stack_mA0 + local_rsi * 4)), *(uint64_t *)(v_stack_mA8 + local_rsi * 8), (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) == 0) goto loc_005DF321;
    a3 = 0;
    v_stack_mD8 = 0;
    result = PpmHeteroUtilityGreaterThanOrEqualThreshold(v_stack_mB0, local_r13, a3, (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) != 0) goto loc_005DF333;
loc_005DF321:
    if ((uint32_t)(local_rsi) != 0) goto loc_005DF1FD;
    goto loc_005DF336;
loc_005DF32B:
    local_r12 = 0;
    goto loc_005DF336;
loc_005DF333:
loc_005DF336:
    local_rbx = (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) < v_stack_p18) ? 1 : 0;
loc_005DF343:
    if (((uint32_t)((int8_t)(*(uint8_t *)(v_stack_m50 + 0x4A4)))) != ((uint32_t)(local_rbx))) goto loc_005DF36A;
    result = (uint8_t)((*(uint8_t *)(v_stack_m50 + 0x4A2)) + (1));
    *(uint8_t *)(v_stack_m50 + 0x4A2) = (uint8_t)((uint8_t)(result));
    goto loc_005DF3AB;
loc_005DF36A:
    *(uint8_t *)(v_stack_m50 + 0x4A4) = (uint8_t)(local_rbx);
    *(uint8_t *)(v_stack_m50 + 0x4A2) = 1;
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_mB0, local_r13, a3, (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) == 0) goto loc_005DF3AB;
    if (((uint32_t)(local_rbx)) == 2) goto loc_005DF3AB;
    if ((*(uint8_t *)(v_stack_m50 + 0x4B1)) <= 0) goto loc_005DF3AB;
    local_rbp = 4;
    if ((*(uint8_t *)(v_rip + 0x929DCB)) != 0) {
        *(uint8_t *)(v_stack_m50 + 0x4B1) = 0;
        local_rbp = 0x804ULL;
    }
    if ((*(uint32_t *)(v_rip + 0x92BE92)) != 5) goto loc_005DF44F;
    local_rbp = (uint32_t)((local_rbp) | (16));
    *(uint16_t *)(*(uint64_t *)(v_stack_m50 + 0x508) + 0x286) = (uint16_t)((uint32_t)((uint32_t)(local_r15)));
loc_005DF3C9:
loc_005DF3D0:
    result = (uint8_t)((*(uint8_t *)(v_stack_m50 + 0x4A0)) & (253));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(v_stack_m50 + 0x4A0) = (uint8_t)(result);
    if ((*(uint8_t *)(v_rip + 0x9E76A5)) != 0) {
        a1 = *(uint64_t *)(v_stack_m50 + 0x508);
        result = *(uint16_t *)(a1 + 0x286);
        *(uint16_t *)(a1 + 0x288) = (uint16_t)(result);
        result = *(uint64_t *)(v_stack_m50 + 0x508);
        a1 = *(uint16_t *)(result + 0x286);
        *(uint16_t *)(v_stack_m50 + 0x4F0) = (uint16_t)(a1);
    }
    local_rbp = (uint32_t)((local_rbp) | (1));
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(a1, local_r13, a3, (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) != 0) goto loc_005DF52B;
    v_stack_mD0 = (uint32_t)(local_rbp);
    v_stack_mD8 = (uint16_t)((uint32_t)((uint32_t)(local_r15)));
    result = PpmEventTraceHeteroResponseEx(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
    goto loc_005DF54A;
loc_005DF44F:
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 2) goto loc_005DF4BF;
    if (((uint32_t)(v_stack_mA0)) < ((uint32_t)(*(uint8_t *)(v_stack_m88 + 0xB2)))) goto loc_005DF3C9;
    local_rbp = (uint32_t)((local_rbp) | (32));
    *(uint16_t *)(*(uint64_t *)(v_stack_m50 + 0x508) + 0x286) = (uint16_t)((uint32_t)((uint32_t)(local_r15)));
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
    if ((uint32_t)(result) == 0) goto loc_005DF3C9;
    if ((*(uint8_t *)(v_stack_m50 + 0x4B1)) <= 0) goto loc_005DF3C9;
    if ((*(uint8_t *)(v_rip + 0x929CCD)) == 0) goto loc_005DF3D0;
    *(uint8_t *)(v_stack_m50 + 0x4B1) = 0;
    goto loc_005DF3D0;
loc_005DF4BF:
    if (((uint32_t)((uint32_t)(v_stack_p10))) != 1) goto loc_005DF3C9;
    if (((uint32_t)(v_stack_mA0)) < ((uint32_t)(*(uint8_t *)(v_stack_m88 + 0xB1)))) goto loc_005DF3C9;
    local_rbp = (uint32_t)((local_rbp) | (64));
    *(uint16_t *)(*(uint64_t *)(v_stack_m50 + 0x508) + 0x286) = (uint16_t)((uint32_t)((uint32_t)(local_r15)));
    result = Feature_UnparkPCoresOnUnimportantUtility__private_IsEnabledDeviceUsageNoInline(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
    if ((uint32_t)(result) == 0) goto loc_005DF3C9;
    if ((*(uint8_t *)(v_stack_m50 + 0x4B0)) <= 0) goto loc_005DF3C9;
    if ((*(uint8_t *)(v_rip + 0x929C59)) == 0) goto loc_005DF3D0;
    *(uint8_t *)(v_stack_m50 + 0x4B0) = (uint8_t)((uint32_t)(v_stack_p10));
    goto loc_005DF3D0;
loc_005DF52B:
    v_stack_mC0 = (uint16_t)((uint32_t)(v_stack_p10));
    v_stack_mC8 = (uint32_t)(v_stack_m70);
    v_stack_mD0 = (uint32_t)(local_rbp);
    v_stack_mD8 = (uint16_t)((uint32_t)((uint32_t)(local_r15)));
    result = PpmEventTraceHeteroResponseExV1(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
loc_005DF54A:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m98)) + (1));
    v_stack_m98 = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) < (*(uint32_t *)(v_rip + 0x928E89))) goto loc_005DED47;
loc_005DF561:
    result = PpmParkCalculateUnparkCount(v_stack_m50, v_stack_mA0, v_stack_mA8, v_stack_mB0);
loc_005DF566:
    local_rsp = (local_rsp) + (184);
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DECA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
