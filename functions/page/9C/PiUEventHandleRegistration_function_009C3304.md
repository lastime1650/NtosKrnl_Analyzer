# PiUEventHandleRegistration

- RVA: `0x009C3304`–`0x009C3704` (길이 `1,024` bytes)
- VA: `0x00000001409C3304`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009F7F4`
- 디코드: `270`개 명령, `1,024/1,024` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x009C334E` → [PiUEventInitClientRegistrationContext](../91/PiUEventInitClientRegistrationContext_function_00916A54.md) (function, `0x00916A54`)
- `0x009C3365` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (function, `0x00433560`)
- `0x009C3372` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x009C3384` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (function, `0x00435A70`)
- `0x009C33D9` → [PiUEventFreeClientRegistrationContext](PiUEventFreeClientRegistrationContext_function_009C3A2C.md) (function, `0x009C3A2C`)
- `0x009C341C` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (function, `0x00435A70`)
- `0x009C343B` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (function, `0x00435A70`)
- `0x009C348E` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)
- `0x009C34C0` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)
- `0x009C34D1` → [Feature_2986240315__private_IsEnabledDeviceUsageNoInline](../../text/5A/Feature_2986240315__private_IsEnabledDeviceUsageNoInline_function_005A721C.md) (function, `0x005A721C`)
- `0x009C34E6` → [PiUEventGetDmObjectFromUserHandle](../72/PiUEventGetDmObjectFromUserHandle_function_0072DF88.md) (function, `0x0072DF88`)
- `0x009C34F2` → [PiUEventGetDeviceInstanceIdFromUserHandle](../A3/PiUEventGetDeviceInstanceIdFromUserHandle_function_00A38954.md) (function, `0x00A38954`)
- `0x009C3511` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)
- `0x009C356B` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x009C35B3` → [PiUEventHashStringIntoBucket](../../text/48/PiUEventHashStringIntoBucket_function_00486690.md) (function, `0x00486690`)
- `0x009C3602` → [PiUEventHashStringIntoBucket](../../text/48/PiUEventHashStringIntoBucket_function_00486690.md) (function, `0x00486690`)
- `0x009C3645` → [PiUEventHashStringIntoBucket](../../text/48/PiUEventHashStringIntoBucket_function_00486690.md) (function, `0x00486690`)
- `0x009C368D` → [PiUEventHashGuidIntoBucket](../../text/49/PiUEventHashGuidIntoBucket_function_00497CEC.md) (function, `0x00497CEC`)
- `0x009C36D0` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)

### Direct callers
- [PiUEventHandleIoctl](PiUEventHandleIoctl_function_009C2B74.md) at `0x009C2BE8`

### Static image references
- `0x009C3551` → RVA `0x00F8C760` (`.data`; read)
- `0x009C35BA` → RVA `0x00F8C7A0` (`.data`; read)
- `0x009C35D5` → RVA `0x00E6633C` (`.data`; read/write)
- `0x009C3609` → RVA `0x00F8C880` (`.data`; read)
- `0x009C3624` → RVA `0x00E66340` (`.data`; read/write)
- `0x009C364C` → RVA `0x00F8C960` (`.data`; read)
- `0x009C3663` → RVA `0x00E66338` (`.data`; read/write)
- `0x009C3694` → RVA `0x00F8C680` (`.data`; read)
- `0x009C36B2` → RVA `0x00E66344` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x009C3365` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (`PAGE` → `.text`)
  - `0x009C3384` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (`PAGE` → `.text`)
  - `0x009C341C` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (`PAGE` → `.text`)
  - `0x009C343B` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (`PAGE` → `.text`)
  - `0x009C34D1` → [Feature_2986240315__private_IsEnabledDeviceUsageNoInline](../../text/5A/Feature_2986240315__private_IsEnabledDeviceUsageNoInline_function_005A721C.md) (`PAGE` → `.text`)
  - `0x009C356B` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x009C35B3` → [PiUEventHashStringIntoBucket](../../text/48/PiUEventHashStringIntoBucket_function_00486690.md) (`PAGE` → `.text`)
  - `0x009C3602` → [PiUEventHashStringIntoBucket](../../text/48/PiUEventHashStringIntoBucket_function_00486690.md) (`PAGE` → `.text`)
  - `0x009C3645` → [PiUEventHashStringIntoBucket](../../text/48/PiUEventHashStringIntoBucket_function_00486690.md) (`PAGE` → `.text`)
  - `0x009C368D` → [PiUEventHashGuidIntoBucket](../../text/49/PiUEventHashGuidIntoBucket_function_00497CEC.md) (`PAGE` → `.text`)
  - `0x009C36D0` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C3304  48 8B C4                        mov rax, rsp
009C3307  48 89 58 08                     mov qword ptr [rax + 8], rbx
009C330B  48 89 68 18                     mov qword ptr [rax + 0x18], rbp
009C330F  56                              push rsi
009C3310  57                              push rdi
009C3311  41 55                           push r13
009C3313  41 56                           push r14
009C3315  41 57                           push r15
009C3317  48 83 EC 30                     sub rsp, 0x30
009C331B  48 83 60 D0 00                  and qword ptr [rax - 0x30], 0
009C3320  45 32 FF                        xor r15b, r15b
009C3323  48 83 60 10 00                  and qword ptr [rax + 0x10], 0
009C3328  48 8B F2                        mov rsi, rdx
009C332B  4C 8B E9                        mov r13, rcx
009C332E  48 85 D2                        test rdx, rdx
009C3331  0F 84 A8 03 00 00               je 0x1409c36df
009C3337  41 81 F8 A8 03 00 00            cmp r8d, 0x3a8
009C333E  0F 85 9B 03 00 00               jne 0x1409c36df
009C3344  41 83 F9 08                     cmp r9d, 8
009C3348  0F 85 91 03 00 00               jne 0x1409c36df
009C334E  E8 01 37 F5 FF                  call 0x140916a54
009C3353  48 8B F8                        mov rdi, rax
009C3356  48 85 C0                        test rax, rax
009C3359  75 0A                           jne 0x1409c3365
009C335B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
009C3360  E9 7F 03 00 00                  jmp 0x1409c36e4
009C3365  E8 F6 01 A7 FF                  call 0x140433560
009C336A  48 8D 4F 38                     lea rcx, [rdi + 0x38]
009C336E  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
009C3372  E8 A9 84 EA FF                  call 0x14086b820
009C3377  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009C337C  BA 04 01 00 00                  mov edx, 0x104
009C3381  48 8B CE                        mov rcx, rsi
009C3384  E8 E7 26 A7 FF                  call 0x140435a70
009C3389  8B D8                           mov ebx, eax
009C338B  85 C0                           test eax, eax
009C338D  78 3F                           js 0x1409c33ce
009C338F  81 BE 08 02 00 00 A0 01 00 00   cmp dword ptr [rsi + 0x208], 0x1a0
009C3399  75 33                           jne 0x1409c33ce
009C339B  8B 8E 10 02 00 00               mov ecx, dword ptr [rsi + 0x210]
009C33A1  83 F9 04                        cmp ecx, 4
009C33A4  7D 28                           jge 0x1409c33ce
009C33A6  8B 86 0C 02 00 00               mov eax, dword ptr [rsi + 0x20c]
009C33AC  A9 FC FF FF FF                  test eax, 0xfffffffc
009C33B1  75 1B                           jne 0x1409c33ce
009C33B3  41 BA 01 00 00 00               mov r10d, 1
009C33B9  41 84 C2                        test r10b, al
009C33BC  74 04                           je 0x1409c33c2
009C33BE  85 C9                           test ecx, ecx
009C33C0  75 0C                           jne 0x1409c33ce
009C33C2  A8 02                           test al, 2
009C33C4  74 1D                           je 0x1409c33e3
009C33C6  8D 41 FE                        lea eax, [rcx - 2]
009C33C9  41 3B C2                        cmp eax, r10d
009C33CC  76 31                           jbe 0x1409c33ff
009C33CE  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C33D3  41 8A D7                        mov dl, r15b
009C33D6  48 8B CF                        mov rcx, rdi
009C33D9  E8 4E 06 00 00                  call 0x1409c3a2c
009C33DE  E9 01 03 00 00                  jmp 0x1409c36e4
009C33E3  41 3B CA                        cmp ecx, r10d
009C33E6  75 17                           jne 0x1409c33ff
009C33E8  4C 8D B6 18 02 00 00            lea r14, [rsi + 0x218]
009C33EF  49 8B 06                        mov rax, qword ptr [r14]
009C33F2  48 85 C0                        test rax, rax
009C33F5  74 D7                           je 0x1409c33ce
009C33F7  48 83 F8 FF                     cmp rax, -1
009C33FB  75 09                           jne 0x1409c3406
009C33FD  EB CF                           jmp 0x1409c33ce
009C33FF  4C 8D B6 18 02 00 00            lea r14, [rsi + 0x218]
009C3406  41 BB C8 00 00 00               mov r11d, 0xc8
009C340C  83 F9 02                        cmp ecx, 2
009C340F  75 16                           jne 0x1409c3427
009C3411  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009C3416  41 8B D3                        mov edx, r11d
009C3419  49 8B CE                        mov rcx, r14
009C341C  E8 4F 26 A7 FF                  call 0x140435a70
009C3421  8B D8                           mov ebx, eax
009C3423  85 C0                           test eax, eax
009C3425  78 A7                           js 0x1409c33ce
009C3427  83 BE 10 02 00 00 03            cmp dword ptr [rsi + 0x210], 3
009C342E  75 1D                           jne 0x1409c344d
009C3430  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
009C3435  49 8B D3                        mov rdx, r11
009C3438  49 8B CE                        mov rcx, r14
009C343B  E8 30 26 A7 FF                  call 0x140435a70
009C3440  8B D8                           mov ebx, eax
009C3442  85 C0                           test eax, eax
009C3444  78 88                           js 0x1409c33ce
009C3446  4C 8D B6 18 02 00 00            lea r14, [rsi + 0x218]
009C344D  8B 86 10 02 00 00               mov eax, dword ptr [rsi + 0x210]
009C3453  89 87 84 00 00 00               mov dword ptr [rdi + 0x84], eax
009C3459  8B 8E 10 02 00 00               mov ecx, dword ptr [rsi + 0x210]
009C345F  85 C9                           test ecx, ecx
009C3461  0F 84 CF 00 00 00               je 0x1409c3536
009C3467  41 2B CA                        sub ecx, r10d
009C346A  74 65                           je 0x1409c34d1
009C346C  41 2B CA                        sub ecx, r10d
009C346F  74 34                           je 0x1409c34a5
009C3471  41 3B CA                        cmp ecx, r10d
009C3474  0F 85 54 FF FF FF               jne 0x1409c33ce
009C347A  8B 86 0C 02 00 00               mov eax, dword ptr [rsi + 0x20c]
009C3480  A8 02                           test al, 2
009C3482  75 19                           jne 0x1409c349d
009C3484  4C 8D 47 18                     lea r8, [rdi + 0x18]
009C3488  49 8B D6                        mov rdx, r14
009C348B  41 8B CA                        mov ecx, r10d
009C348E  E8 4D C6 F1 FF                  call 0x1408dfae0
009C3493  8B D8                           mov ebx, eax
009C3495  85 C0                           test eax, eax
009C3497  0F 88 36 FF FF FF               js 0x1409c33d3
009C349D  49 8B EE                        mov rbp, r14
009C34A0  E9 A8 00 00 00                  jmp 0x1409c354d
009C34A5  8B 86 0C 02 00 00               mov eax, dword ptr [rsi + 0x20c]
009C34AB  49 8B EE                        mov rbp, r14
009C34AE  A8 02                           test al, 2
009C34B0  0F 85 97 00 00 00               jne 0x1409c354d
009C34B6  4C 8D 47 18                     lea r8, [rdi + 0x18]
009C34BA  49 8B D6                        mov rdx, r14
009C34BD  41 8B CA                        mov ecx, r10d
009C34C0  E8 1B C6 F1 FF                  call 0x1408dfae0
009C34C5  8B D8                           mov ebx, eax
009C34C7  85 C0                           test eax, eax
009C34C9  0F 88 04 FF FF FF               js 0x1409c33d3
009C34CF  EB 5C                           jmp 0x1409c352d
009C34D1  E8 46 3D BE FF                  call 0x1405a721c
009C34D6  49 8B 0E                        mov rcx, qword ptr [r14]
009C34D9  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
009C34DE  85 C0                           test eax, eax
009C34E0  74 0B                           je 0x1409c34ed
009C34E2  48 8D 57 18                     lea rdx, [rdi + 0x18]
009C34E6  E8 9D AA D6 FF                  call 0x14072df88
009C34EB  EB 29                           jmp 0x1409c3516
009C34ED  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
009C34F2  E8 5D 54 07 00                  call 0x140a38954
009C34F7  85 C0                           test eax, eax
009C34F9  0F 88 CF FE FF FF               js 0x1409c33ce
009C34FF  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
009C3504  4C 8D 47 18                     lea r8, [rdi + 0x18]
009C3508  B9 01 00 00 00                  mov ecx, 1
009C350D  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
009C3511  E8 CA C5 F1 FF                  call 0x1408dfae0
009C3516  8B D8                           mov ebx, eax
009C3518  85 C0                           test eax, eax
009C351A  0F 88 B3 FE FF FF               js 0x1409c33d3
009C3520  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
009C3525  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
009C3529  44 88 7F 28                     mov byte ptr [rdi + 0x28], r15b
009C352D  48 8D AE 18 02 00 00            lea rbp, [rsi + 0x218]
009C3534  EB 17                           jmp 0x1409c354d
009C3536  8B 86 0C 02 00 00               mov eax, dword ptr [rsi + 0x20c]
009C353C  49 8B EE                        mov rbp, r14
009C353F  41 84 C2                        test r10b, al
009C3542  75 09                           jne 0x1409c354d
009C3544  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
009C3548  F3 0F 7F 47 18                  movdqu xmmword ptr [rdi + 0x18], xmm0
009C354D  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
009C3551  48 8D 0D 08 92 5C 00            lea rcx, [rip + 0x5c9208]
009C3558  48 89 06                        mov qword ptr [rsi], rax
009C355B  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
009C3563  48 C7 40 08 08 00 00 00         mov qword ptr [rax + 8], 8
009C356B  E8 30 B0 84 FF                  call 0x14020e5a0
009C3570  8B 8E 10 02 00 00               mov ecx, dword ptr [rsi + 0x210]
009C3576  85 C9                           test ecx, ecx
009C3578  0F 84 FB 00 00 00               je 0x1409c3679
009C357E  83 E9 01                        sub ecx, 1
009C3581  0F 84 B6 00 00 00               je 0x1409c363d
009C3587  83 E9 01                        sub ecx, 1
009C358A  74 62                           je 0x1409c35ee
009C358C  83 F9 01                        cmp ecx, 1
009C358F  74 0A                           je 0x1409c359b
009C3591  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C3596  E9 2E 01 00 00                  jmp 0x1409c36c9
009C359B  8B 86 0C 02 00 00               mov eax, dword ptr [rsi + 0x20c]
009C35A1  A8 02                           test al, 2
009C35A3  74 07                           je 0x1409c35ac
009C35A5  B8 0D 00 00 00                  mov eax, 0xd
009C35AA  EB 0C                           jmp 0x1409c35b8
009C35AC  48 8D 8E 18 02 00 00            lea rcx, [rsi + 0x218]
009C35B3  E8 D8 30 AC FF                  call 0x140486690
009C35B8  8B C8                           mov ecx, eax
009C35BA  48 8D 05 DF 91 5C 00            lea rax, [rip + 0x5c91df]
009C35C1  48 C1 E1 04                     shl rcx, 4
009C35C5  48 03 C8                        add rcx, rax
009C35C8  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
009C35CC  48 39 08                        cmp qword ptr [rax], rcx
009C35CF  0F 85 D6 00 00 00               jne 0x1409c36ab
009C35D5  FF 05 61 2D 4A 00               inc dword ptr [rip + 0x4a2d61]
009C35DB  48 89 0F                        mov qword ptr [rdi], rcx
009C35DE  48 89 47 08                     mov qword ptr [rdi + 8], rax
009C35E2  48 89 38                        mov qword ptr [rax], rdi
009C35E5  48 89 79 08                     mov qword ptr [rcx + 8], rdi
009C35E9  E9 D8 00 00 00                  jmp 0x1409c36c6
009C35EE  8B 86 0C 02 00 00               mov eax, dword ptr [rsi + 0x20c]
009C35F4  A8 02                           test al, 2
009C35F6  74 07                           je 0x1409c35ff
009C35F8  B8 0D 00 00 00                  mov eax, 0xd
009C35FD  EB 08                           jmp 0x1409c3607
009C35FF  48 8B CD                        mov rcx, rbp
009C3602  E8 89 30 AC FF                  call 0x140486690
009C3607  8B C8                           mov ecx, eax
009C3609  48 8D 05 70 92 5C 00            lea rax, [rip + 0x5c9270]
009C3610  48 C1 E1 04                     shl rcx, 4
009C3614  48 03 C8                        add rcx, rax
009C3617  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
009C361B  48 39 08                        cmp qword ptr [rax], rcx
009C361E  0F 85 87 00 00 00               jne 0x1409c36ab
009C3624  FF 05 16 2D 4A 00               inc dword ptr [rip + 0x4a2d16]
009C362A  48 89 0F                        mov qword ptr [rdi], rcx
009C362D  48 89 47 08                     mov qword ptr [rdi + 8], rax
009C3631  48 89 38                        mov qword ptr [rax], rdi
009C3634  48 89 79 08                     mov qword ptr [rcx + 8], rdi
009C3638  E9 89 00 00 00                  jmp 0x1409c36c6
009C363D  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
009C3641  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
009C3645  E8 46 30 AC FF                  call 0x140486690
009C364A  8B C0                           mov eax, eax
009C364C  48 8D 0D 0D 93 5C 00            lea rcx, [rip + 0x5c930d]
009C3653  48 C1 E0 04                     shl rax, 4
009C3657  48 03 C1                        add rax, rcx
009C365A  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
009C365E  48 39 01                        cmp qword ptr [rcx], rax
009C3661  75 48                           jne 0x1409c36ab
009C3663  FF 05 CF 2C 4A 00               inc dword ptr [rip + 0x4a2ccf]
009C3669  48 89 07                        mov qword ptr [rdi], rax
009C366C  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
009C3670  48 89 39                        mov qword ptr [rcx], rdi
009C3673  48 89 78 08                     mov qword ptr [rax + 8], rdi
009C3677  EB 4D                           jmp 0x1409c36c6
009C3679  8B 86 0C 02 00 00               mov eax, dword ptr [rsi + 0x20c]
009C367F  A8 01                           test al, 1
009C3681  74 07                           je 0x1409c368a
009C3683  B8 0D 00 00 00                  mov eax, 0xd
009C3688  EB 08                           jmp 0x1409c3692
009C368A  48 8B CD                        mov rcx, rbp
009C368D  E8 5A 46 AD FF                  call 0x140497cec
009C3692  8B D0                           mov edx, eax
009C3694  48 8D 05 E5 8F 5C 00            lea rax, [rip + 0x5c8fe5]
009C369B  48 C1 E2 04                     shl rdx, 4
009C369F  48 03 D0                        add rdx, rax
009C36A2  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
009C36A6  48 39 10                        cmp qword ptr [rax], rdx
009C36A9  74 07                           je 0x1409c36b2
009C36AB  B9 03 00 00 00                  mov ecx, 3
009C36B0  CD 29                           int 0x29
009C36B2  FF 05 8C 2C 4A 00               inc dword ptr [rip + 0x4a2c8c]
009C36B8  48 89 17                        mov qword ptr [rdi], rdx
009C36BB  48 89 47 08                     mov qword ptr [rdi + 8], rax
009C36BF  48 89 38                        mov qword ptr [rax], rdi
009C36C2  48 89 7A 08                     mov qword ptr [rdx + 8], rdi
009C36C6  41 B7 01                        mov r15b, 1
009C36C9  48 8D 0D 90 90 5C 00            lea rcx, [rip + 0x5c9090]
009C36D0  E8 EB E2 88 FF                  call 0x1402519c0
009C36D5  85 DB                           test ebx, ebx
009C36D7  0F 88 F6 FC FF FF               js 0x1409c33d3
009C36DD  EB 07                           jmp 0x1409c36e6
009C36DF  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C36E4  33 FF                           xor edi, edi
009C36E6  49 89 7D 20                     mov qword ptr [r13 + 0x20], rdi
009C36EA  8B C3                           mov eax, ebx
009C36EC  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009C36F1  48 8B 6C 24 70                  mov rbp, qword ptr [rsp + 0x70]
009C36F6  48 83 C4 30                     add rsp, 0x30
009C36FA  41 5F                           pop r15
009C36FC  41 5E                           pop r14
009C36FE  41 5D                           pop r13
009C3700  5F                              pop rdi
009C3701  5E                              pop rsi
009C3702  C3                              ret
009C3703  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiUEventHandleRegistration(__int64 a1, __int64 a2, int a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rbp;
    v_rsp = (v_rsp) - (48);
    v_r15 = 0;
    if (a2 == 0) goto loc_009C36DF;
    if (a3 != 936) goto loc_009C36DF;
    if (a4 != 8) goto loc_009C36DF;
    result = PiUEventInitClientRegistrationContext(a1, a2, a3, a4);
    if (result != 0) goto loc_009C3365;
    goto loc_009C36E4;
loc_009C3365:
    result = PsGetCurrentProcessId(a1, a2, a3, a4);
    *(unsigned __int64 *)(result + 48) = result;
    result = SeCaptureSubjectContext(result + 56, a2, a3, a4);
    result = RtlStringCchLengthW(a2, 260, v_stack_m38, a4);
    if (sign_flag) goto loc_009C33CE;
    if ((*(unsigned int *)(a2 + 520)) != 416) goto loc_009C33CE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 528)))) >= 4) goto loc_009C33CE;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 524)))) & (0xFFFFFFFCULL)) != 0) goto loc_009C33CE;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 524))))) == 0) goto loc_009C33C2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 528))) != 0) goto loc_009C33CE;
loc_009C33C2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 524)))) & (2)) == 0) goto loc_009C33E3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 528)) - 2)) <= 1) goto loc_009C33FF;
loc_009C33CE:
loc_009C33D3:
    result = PiUEventFreeClientRegistrationContext(result, 0, v_stack_m38, a4);
    goto loc_009C36E4;
loc_009C33E3:
    if (((unsigned int)(result)) != 1) goto loc_009C33FF;
    if (*(unsigned __int64 *)(a2 + 536) == 0) goto loc_009C33CE;
    if ((*(unsigned __int64 *)(a2 + 536)) != -1) goto loc_009C3406;
    goto loc_009C33CE;
loc_009C33FF:
loc_009C3406:
    if (((unsigned int)(result)) != 2) goto loc_009C3427;
    result = RtlStringCchLengthW(a2 + 536, 200, v_stack_m38, a4);
    if (sign_flag) goto loc_009C33CE;
loc_009C3427:
    if ((*(unsigned int *)(a2 + 528)) != 3) goto loc_009C344D;
    result = RtlStringCchLengthW(a2 + 536, 200, v_stack_m38, a4);
    if (sign_flag) goto loc_009C33CE;
loc_009C344D:
    *(unsigned int *)(result + 132) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 528)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 528))) == 0) goto loc_009C3536;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 528))) - (1));
    if (condition_is_equal) goto loc_009C34D1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009C34A5;
    if (((unsigned int)(a1)) != 1) goto loc_009C33CE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 524)))) & (2)) != 0) goto loc_009C349D;
    result = PiDmGetObject(1, a2 + 536, result + 24, a4);
    if (sign_flag) goto loc_009C33D3;
loc_009C349D:
    goto loc_009C354D;
loc_009C34A5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 524)))) & (2)) != 0) goto loc_009C354D;
    result = PiDmGetObject(1, a2 + 536, result + 24, a4);
    if (sign_flag) goto loc_009C33D3;
    goto loc_009C352D;
loc_009C34D1:
    result = Feature_2986240315__private_IsEnabledDeviceUsageNoInline(1, a2 + 536, result + 24, a4);
    if ((unsigned int)(result) == 0) goto loc_009C34ED;
    result = PiUEventGetDmObjectFromUserHandle(*(unsigned __int64 *)(a2 + 536), result + 24, v_stack_p10, a4);
    goto loc_009C3516;
loc_009C34ED:
    result = PiUEventGetDeviceInstanceIdFromUserHandle(*(unsigned __int64 *)(a2 + 536), v_stack_m30, v_stack_p10, a4);
    if (sign_flag) goto loc_009C33CE;
    result = PiDmGetObject(1, *(unsigned __int64 *)(v_stack_m30 + 8), result + 24, a4);
loc_009C3516:
    if (sign_flag) goto loc_009C33D3;
    *(unsigned __int64 *)(result + 32) = v_stack_p10;
    *(unsigned __int8 *)(result + 40) = 0;
loc_009C352D:
    goto loc_009C354D;
loc_009C3536:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 524))))) == 0) {
        *(unsigned __int64 *)(result + 24) = v_xmm0;
    }
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(result + 88);
    *(unsigned __int64 *)(a5 + 8) = 8;
    result = ExAcquireFastMutex(v_rip + 6066696, *(unsigned __int64 *)(v_stack_m30 + 8), result + 24, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 528))) == 0) goto loc_009C3679;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 528))) - (1));
    if (condition_is_equal) goto loc_009C363D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009C35EE;
    if (((unsigned int)(a1)) == 1) goto loc_009C359B;
    goto loc_009C36C9;
loc_009C359B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 524)))) & (2)) == 0) goto loc_009C35AC;
    goto loc_009C35B8;
loc_009C35AC:
    result = PiUEventHashStringIntoBucket(a2 + 536, *(unsigned __int64 *)(v_stack_m30 + 8), result + 24, a4);
loc_009C35B8:
    a1 = ((unsigned int)((unsigned int)(result))) << (4);
    a1 = (a1) + (v_rip + 6066655);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != a1) goto loc_009C36AB;
    *(unsigned __int64 *)(result) = a1;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) = result;
    *(unsigned __int64 *)(a1 + 8) = result;
    goto loc_009C36C6;
loc_009C35EE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 524)))) & (2)) == 0) goto loc_009C35FF;
    goto loc_009C3607;
loc_009C35FF:
    result = PiUEventHashStringIntoBucket(a2 + 536, *(unsigned __int64 *)(v_stack_m30 + 8), result + 24, a4);
loc_009C3607:
    a1 = ((unsigned int)((unsigned int)(result))) << (4);
    a1 = (a1) + (v_rip + 6066800);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != a1) goto loc_009C36AB;
    *(unsigned __int64 *)(result) = a1;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) = result;
    *(unsigned __int64 *)(a1 + 8) = result;
    goto loc_009C36C6;
loc_009C363D:
    result = PiUEventHashStringIntoBucket(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16), *(unsigned __int64 *)(v_stack_m30 + 8), result + 24, a4);
    result = ((unsigned int)((unsigned int)(result))) << (4);
    result = (result) + (v_rip + 6066957);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_009C36AB;
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = result;
    *(unsigned __int64 *)(result + 8) = result;
    goto loc_009C36C6;
loc_009C3679:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 524)))) & (1)) == 0) goto loc_009C368A;
    goto loc_009C3692;
loc_009C368A:
    result = PiUEventHashGuidIntoBucket(a2 + 536, *(unsigned __int64 *)(v_stack_m30 + 8), result + 24, a4);
loc_009C3692:
    a2 = ((unsigned int)((unsigned int)(result))) << (4);
    a2 = (a2) + (v_rip + 6066149);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) != a2) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result) = a2;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) = result;
    *(unsigned __int64 *)(a2 + 8) = result;
loc_009C36C6:
loc_009C36C9:
    result = ExReleaseFastMutex(v_rip + 6066320, a2, result + 24, a4);
    if (sign_flag) goto loc_009C33D3;
    goto loc_009C36E6;
loc_009C36DF:
loc_009C36E4:
    v_rdi = 0;
loc_009C36E6:
    *(unsigned __int64 *)(a1 + 32) = 0;
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t PiUEventHandleRegistration(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rbp;
    local_rsp = (local_rsp) - (48);
    local_r15 = 0;
    if (Arg2 == NULL) goto loc_009C36DF;
    if (Arg3 != 936) goto loc_009C36DF;
    if (Arg4 != 8) goto loc_009C36DF;
    result = PiUEventInitClientRegistrationContext(Arg1, Arg2, Arg3, Arg4);
    if (result != 0) goto loc_009C3365;
    goto loc_009C36E4;
loc_009C3365:
    result = PsGetCurrentProcessId(Arg1, Arg2, Arg3, Arg4);
    *(uint64_t *)(result + 0x30) = result;
    result = SeCaptureSubjectContext(result + 56, Arg2, Arg3, Arg4);
    result = RtlStringCchLengthW(Arg2, 260, v_stack_m38, Arg4);
    if (sign_flag) goto loc_009C33CE;
    if ((*(uint32_t *)(arg2 + 0x208)) != 416) goto loc_009C33CE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x210)))) >= 4) goto loc_009C33CE;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20C)))) & (0xFFFFFFFCULL)) != 0) goto loc_009C33CE;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20C))))) == 0) goto loc_009C33C2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x210))) != 0) goto loc_009C33CE;
loc_009C33C2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20C)))) & (2)) == 0) goto loc_009C33E3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x210)) - 2)) <= 1) goto loc_009C33FF;
loc_009C33CE:
loc_009C33D3:
    result = PiUEventFreeClientRegistrationContext(result, 0, v_stack_m38, Arg4);
    goto loc_009C36E4;
loc_009C33E3:
    if (((uint32_t)(result)) != 1) goto loc_009C33FF;
    if (*(uint64_t *)(arg2 + 0x218) == 0) goto loc_009C33CE;
    if ((*(uint64_t *)(arg2 + 0x218)) != -1) goto loc_009C3406;
    goto loc_009C33CE;
loc_009C33FF:
loc_009C3406:
    if (((uint32_t)(result)) != 2) goto loc_009C3427;
    result = RtlStringCchLengthW(Arg2 + 536, 200, v_stack_m38, Arg4);
    if (sign_flag) goto loc_009C33CE;
loc_009C3427:
    if ((*(uint32_t *)(arg2 + 0x210)) != 3) goto loc_009C344D;
    result = RtlStringCchLengthW(Arg2 + 536, 200, v_stack_m38, Arg4);
    if (sign_flag) goto loc_009C33CE;
loc_009C344D:
    *(uint32_t *)(result + 0x84) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x210)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x210))) == 0) goto loc_009C3536;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x210))) - (1));
    if (condition_is_equal) goto loc_009C34D1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009C34A5;
    if (((uint32_t)(Arg1)) != 1) goto loc_009C33CE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20C)))) & (2)) != 0) goto loc_009C349D;
    result = PiDmGetObject(1, Arg2 + 536, result + 24, Arg4);
    if (sign_flag) goto loc_009C33D3;
loc_009C349D:
    goto loc_009C354D;
loc_009C34A5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20C)))) & (2)) != 0) goto loc_009C354D;
    result = PiDmGetObject(1, Arg2 + 536, result + 24, Arg4);
    if (sign_flag) goto loc_009C33D3;
    goto loc_009C352D;
loc_009C34D1:
    result = Feature_2986240315__private_IsEnabledDeviceUsageNoInline(1, Arg2 + 536, result + 24, Arg4);
    if ((uint32_t)(result) == 0) goto loc_009C34ED;
    result = PiUEventGetDmObjectFromUserHandle(*(uint64_t *)(arg2 + 0x218), result + 24, v_stack_p10, Arg4);
    goto loc_009C3516;
loc_009C34ED:
    result = PiUEventGetDeviceInstanceIdFromUserHandle(*(uint64_t *)(arg2 + 0x218), v_stack_m30, v_stack_p10, Arg4);
    if (sign_flag) goto loc_009C33CE;
    result = PiDmGetObject(1, *(uint64_t *)(v_stack_m30 + 0x8), result + 24, Arg4);
loc_009C3516:
    if (sign_flag) goto loc_009C33D3;
    *(uint64_t *)(result + 0x20) = v_stack_p10;
    *(uint8_t *)(result + 0x28) = 0;
loc_009C352D:
    goto loc_009C354D;
loc_009C3536:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20C))))) == 0) {
        *(uint64_t *)(result + 0x18) = v_xmm0;
    }
    *(uint64_t *)(arg2) = *(uint64_t *)(result + 0x58);
    *(uint64_t *)(arg5 + 0x8) = 8;
    result = ExAcquireFastMutex(v_rip + 6066696, *(uint64_t *)(v_stack_m30 + 0x8), result + 24, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x210))) == 0) goto loc_009C3679;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x210))) - (1));
    if (condition_is_equal) goto loc_009C363D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009C35EE;
    if (((uint32_t)(Arg1)) == 1) goto loc_009C359B;
    goto loc_009C36C9;
loc_009C359B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20C)))) & (2)) == 0) goto loc_009C35AC;
    goto loc_009C35B8;
loc_009C35AC:
    result = PiUEventHashStringIntoBucket(Arg2 + 536, *(uint64_t *)(v_stack_m30 + 0x8), result + 24, Arg4);
loc_009C35B8:
    Arg1 = ((uint32_t)((uint32_t)(result))) << (4);
    Arg1 = (Arg1) + (v_rip + 6066655);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != Arg1) goto loc_009C36AB;
    *(void **)(result) = Arg1;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg1 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) = result;
    *(uint64_t *)(arg1 + 0x8) = result;
    goto loc_009C36C6;
loc_009C35EE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20C)))) & (2)) == 0) goto loc_009C35FF;
    goto loc_009C3607;
loc_009C35FF:
    result = PiUEventHashStringIntoBucket(Arg2 + 536, *(uint64_t *)(v_stack_m30 + 0x8), result + 24, Arg4);
loc_009C3607:
    Arg1 = ((uint32_t)((uint32_t)(result))) << (4);
    Arg1 = (Arg1) + (v_rip + 6066800);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != Arg1) goto loc_009C36AB;
    *(void **)(result) = Arg1;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg1 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) = result;
    *(uint64_t *)(arg1 + 0x8) = result;
    goto loc_009C36C6;
loc_009C363D:
    result = PiUEventHashStringIntoBucket(*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10), *(uint64_t *)(v_stack_m30 + 0x8), result + 24, Arg4);
    result = ((uint32_t)((uint32_t)(result))) << (4);
    result = (result) + (v_rip + 6066957);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_009C36AB;
    *(uint64_t *)(result) = result;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = result;
    *(uint64_t *)(result + 0x8) = result;
    goto loc_009C36C6;
loc_009C3679:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20C)))) & (1)) == 0) goto loc_009C368A;
    goto loc_009C3692;
loc_009C368A:
    result = PiUEventHashGuidIntoBucket(Arg2 + 536, *(uint64_t *)(v_stack_m30 + 0x8), result + 24, Arg4);
loc_009C3692:
    Arg2 = ((uint32_t)((uint32_t)(result))) << (4);
    Arg2 = (Arg2) + (v_rip + 6066149);
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8))) != Arg2) {
        Arg1 = 3;
    }
    *(void **)(result) = Arg2;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg2 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x8)) = result;
    *(uint64_t *)(arg2 + 0x8) = result;
loc_009C36C6:
loc_009C36C9:
    result = ExReleaseFastMutex(v_rip + 6066320, Arg2, result + 24, Arg4);
    if (sign_flag) goto loc_009C33D3;
    goto loc_009C36E6;
loc_009C36DF:
loc_009C36E4:
    local_rdi = 0;
loc_009C36E6:
    *(uint64_t *)(arg1 + 0x20) = 0;
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x208` | `32` | `R` |
| `Arg2` | `+ 0x20C` | `32` | `R` |
| `Arg2` | `+ 0x210` | `32` | `R` |
| `Arg2` | `+ 0x218` | `64` | `R` |
| `Arg5` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C3304&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
