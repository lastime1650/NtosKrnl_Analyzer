# PpmUpdatePerformanceFeedback

- RVA: `0x002DE580`–`0x002DEFC6` (길이 `2,630` bytes)
- VA: `0x00000001402DE580`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000709AC`
- 디코드: `582`개 명령, `2,630/2,630` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x002DE647` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x002DE664` → [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x002DE690` → [KiAcquireSpinLockInstrumented](../20/KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x002DE6C4` → [HvlGetReferenceTimeUsingTscPage](HvlGetReferenceTimeUsingTscPage_function_002DDBC0.md) (function, `0x002DDBC0`)
- `0x002DE747` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002DE780` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x002DE8FE` → [HvlGetReferenceTimeUsingTscPage](HvlGetReferenceTimeUsingTscPage_function_002DDBC0.md) (function, `0x002DDBC0`)
- `0x002DE949` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002DEA58` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002DED2C` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x002DED6A` → [HvlGetReferenceTimeUsingTscPage](HvlGetReferenceTimeUsingTscPage_function_002DDBC0.md) (function, `0x002DDBC0`)
- `0x002DEDB5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002DEE5D` → [HvlGetReferenceTime](HvlGetReferenceTime_function_002DDB88.md) (function, `0x002DDB88`)
- `0x002DEEF6` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x002DEF18` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x002DEF8A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002DEF9E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PpmEndActiveTimeAccumulation](PpmEndActiveTimeAccumulation_function_002D17F0.md) at `0x002D1819`
- [PpmContinueTimeAccumulation](PpmContinueTimeAccumulation_function_002DC5A8.md) at `0x002DC5F4`
- [PpmContinueActiveTimeAccumulation](PpmContinueActiveTimeAccumulation_function_002DDB54.md) at `0x002DDB76`
- [PpmSnapPerformanceAccumulation](PpmSnapPerformanceAccumulation_function_002DE090.md) at `0x002DE23E`
- [sub_002DF06B](Unknown_function_002DF06B.md) at `0x002DF18A`

### Static image references
- `0x002DE59F` → RVA `0x00E0A740` (`.data`; read)
- `0x002DE607` → RVA `0x00E3EDD8` (`.data`; read)
- `0x002DE64C` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002DE683` → RVA `0x00F0DE58` (`.data`; read)
- `0x002DE6B2` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002DE6C9` → RVA `0x00E3EDD4` (`.data`; read)
- `0x002DE6E5` → RVA `0x00E3EDE0` (`.data`; read)
- `0x002DE8A6` → RVA `0x00E3EDDC` (`.data`; read)
- `0x002DE8D8` → RVA `0x00E3EDE4` (`.data`; read)
- `0x002DEB48` → RVA `0x00E076A0` (`.data`; read)
- `0x002DEB59` → RVA `0x00048E18` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002DE580  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
002DE585  55                              push rbp
002DE586  56                              push rsi
002DE587  57                              push rdi
002DE588  41 54                           push r12
002DE58A  41 55                           push r13
002DE58C  41 56                           push r14
002DE58E  41 57                           push r15
002DE590  48 8D AC 24 F0 FE FF FF         lea rbp, [rsp - 0x110]
002DE598  48 81 EC 10 02 00 00            sub rsp, 0x210
002DE59F  48 8B 05 9A C1 B2 00            mov rax, qword ptr [rip + 0xb2c19a]
002DE5A6  48 33 C4                        xor rax, rsp
002DE5A9  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
002DE5B0  33 C0                           xor eax, eax
002DE5B2  88 54 24 30                     mov byte ptr [rsp + 0x30], dl
002DE5B6  83 B9 20 89 00 00 03            cmp dword ptr [rcx + 0x8920], 3
002DE5BD  0F B6 FA                        movzx edi, dl
002DE5C0  48 8B 95 70 01 00 00            mov rdx, qword ptr [rbp + 0x170]
002DE5C7  45 0F B6 D1                     movzx r10d, r9b
002DE5CB  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
002DE5CF  45 0F B6 D8                     movzx r11d, r8b
002DE5D3  44 88 44 24 31                  mov byte ptr [rsp + 0x31], r8b
002DE5D8  48 8B F1                        mov rsi, rcx
002DE5DB  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002DE5DF  44 8B E8                        mov r13d, eax
002DE5E2  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
002DE5E7  44 8B E0                        mov r12d, eax
002DE5EA  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002DE5EE  44 8B C8                        mov r9d, eax
002DE5F1  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002DE5F6  44 8B F0                        mov r14d, eax
002DE5F9  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
002DE5FE  44 8B F8                        mov r15d, eax
002DE601  0F 85 7C 08 00 00               jne 0x1402dee83
002DE607  8B 0D CB 07 B6 00               mov ecx, dword ptr [rip + 0xb607cb]
002DE60D  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DE614  C6 44 24 32 01                  mov byte ptr [rsp + 0x32], 1
002DE619  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
002DE61D  48 D1 E9                        shr rcx, 1
002DE620  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
002DE624  48 8D 9E 90 88 00 00            lea rbx, [rsi + 0x8890]
002DE62B  40 84 FF                        test dil, dil
002DE62E  0F 84 4E 02 00 00               je 0x1402de882
002DE634  45 32 C0                        xor r8b, r8b
002DE637  33 C9                           xor ecx, ecx
002DE639  83 F9 02                        cmp ecx, 2
002DE63C  72 2D                           jb 0x1402de66b
002DE63E  45 84 C0                        test r8b, r8b
002DE641  0F 84 EA 04 00 00               je 0x1402deb31
002DE647  E8 94 95 F3 FF                  call 0x140217be0
002DE64C  F6 05 B3 84 CE 00 21            test byte ptr [rip + 0xce84b3], 0x21
002DE653  88 44 24 33                     mov byte ptr [rsp + 0x33], al
002DE657  75 2A                           jne 0x1402de683
002DE659  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
002DE65F  73 34                           jae 0x1402de695
002DE661  48 8B CB                        mov rcx, rbx
002DE664  E8 57 9F F2 FF                  call 0x1402085c0
002DE669  EB 2A                           jmp 0x1402de695
002DE66B  48 8B 54 CB 18                  mov rdx, qword ptr [rbx + rcx*8 + 0x18]
002DE670  48 85 D2                        test rdx, rdx
002DE673  74 0A                           je 0x1402de67f
002DE675  44 38 4A 20                     cmp byte ptr [rdx + 0x20], r9b
002DE679  0F 85 4C 08 00 00               jne 0x1402deecb
002DE67F  FF C1                           inc ecx
002DE681  EB B6                           jmp 0x1402de639
002DE683  8B 05 CF F7 C2 00               mov eax, dword ptr [rip + 0xc2f7cf]
002DE689  85 C0                           test eax, eax
002DE68B  75 CC                           jne 0x1402de659
002DE68D  48 8B CB                        mov rcx, rbx
002DE690  E8 5B 9E F2 FF                  call 0x1402084f0
002DE695  4C 87 73 38                     xchg qword ptr [rbx + 0x38], r14
002DE699  44 38 64 24 32                  cmp byte ptr [rsp + 0x32], r12b
002DE69E  74 6F                           je 0x1402de70f
002DE6A0  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002DE6A9  48 3B F0                        cmp rsi, rax
002DE6AC  0F 84 F4 01 00 00               je 0x1402de8a6
002DE6B2  F7 05 FC 83 CE 00 00 01 00 00   test dword ptr [rip + 0xce83fc], 0x100
002DE6BC  0F 84 93 06 00 00               je 0x1402ded55
002DE6C2  33 C9                           xor ecx, ecx
002DE6C4  E8 F7 F4 FF FF                  call 0x1402ddbc0
002DE6C9  8B 0D 05 07 B6 00               mov ecx, dword ptr [rip + 0xb60705]
002DE6CF  4C 8B C8                        mov r9, rax
002DE6D2  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002DE6D7  4D 8B F9                        mov r15, r9
002DE6DA  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DE6E1  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
002DE6E5  8B 0D F5 06 B6 00               mov ecx, dword ptr [rip + 0xb606f5]
002DE6EB  4C 2B FA                        sub r15, rdx
002DE6EE  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DE6F5  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
002DE6F9  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
002DE6FE  49 8B C1                        mov rax, r9
002DE701  49 2B C7                        sub rax, r15
002DE704  4C 8B F0                        mov r14, rax
002DE707  4C 2B 73 70                     sub r14, qword ptr [rbx + 0x70]
002DE70B  48 89 43 70                     mov qword ptr [rbx + 0x70], rax
002DE70F  4C 01 73 30                     add qword ptr [rbx + 0x30], r14
002DE713  48 8B 8E B8 89 00 00            mov rcx, qword ptr [rsi + 0x89b8]
002DE71A  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
002DE71E  48 85 C9                        test rcx, rcx
002DE721  0F 84 8A 00 00 00               je 0x1402de7b1
002DE727  44 8B A1 98 00 00 00            mov r12d, dword ptr [rcx + 0x98]
002DE72E  33 D2                           xor edx, edx
002DE730  48 81 C1 A0 00 00 00            add rcx, 0xa0
002DE737  49 C1 E4 07                     shl r12, 7
002DE73B  4C 03 E1                        add r12, rcx
002DE73E  41 B8 80 00 00 00               mov r8d, 0x80
002DE744  49 8B CC                        mov rcx, r12
002DE747  E8 F4 84 3E 00                  call 0x1406c6c40
002DE74C  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002DE750  FF 81 98 00 00 00               inc dword ptr [rcx + 0x98]
002DE756  83 B9 98 00 00 00 08            cmp dword ptr [rcx + 0x98], 8
002DE75D  75 07                           jne 0x1402de766
002DE75F  44 89 A9 98 00 00 00            mov dword ptr [rcx + 0x98], r13d
002DE766  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
002DE76E  48 8D 4D C0                     lea rcx, [rbp - 0x40]
002DE772  41 89 04 24                     mov dword ptr [r12], eax
002DE776  41 88 7C 24 05                  mov byte ptr [r12 + 5], dil
002DE77B  45 88 6C 24 04                  mov byte ptr [r12 + 4], r13b
002DE780  E8 3B BD F2 FF                  call 0x14020a4c0
002DE785  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
002DE78A  0F B6 44 24 31                  movzx eax, byte ptr [rsp + 0x31]
002DE78F  41 88 44 24 06                  mov byte ptr [r12 + 6], al
002DE794  4D 89 74 24 10                  mov qword ptr [r12 + 0x10], r14
002DE799  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
002DE79D  49 89 44 24 18                  mov qword ptr [r12 + 0x18], rax
002DE7A2  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
002DE7A7  49 89 44 24 68                  mov qword ptr [r12 + 0x68], rax
002DE7AC  4D 89 7C 24 70                  mov qword ptr [r12 + 0x70], r15
002DE7B1  48 8B 7B 18                     mov rdi, qword ptr [rbx + 0x18]
002DE7B5  48 85 FF                        test rdi, rdi
002DE7B8  0F 85 5F 01 00 00               jne 0x1402de91d
002DE7BE  48 8B 7B 20                     mov rdi, qword ptr [rbx + 0x20]
002DE7C2  48 85 FF                        test rdi, rdi
002DE7C5  0F 85 61 02 00 00               jne 0x1402dea2c
002DE7CB  4D 85 E4                        test r12, r12
002DE7CE  0F 85 74 03 00 00               jne 0x1402deb48
002DE7D4  80 BB 88 00 00 00 02            cmp byte ptr [rbx + 0x88], 2
002DE7DB  75 08                           jne 0x1402de7e5
002DE7DD  49 6B C6 64                     imul rax, r14, 0x64
002DE7E1  48 01 43 50                     add qword ptr [rbx + 0x50], rax
002DE7E5  8B 96 48 86 00 00               mov edx, dword ptr [rsi + 0x8648]
002DE7EB  44 8B CA                        mov r9d, edx
002DE7EE  44 8B 86 44 86 00 00            mov r8d, dword ptr [rsi + 0x8644]
002DE7F5  41 8B C0                        mov eax, r8d
002DE7F8  44 2B 4B 60                     sub r9d, dword ptr [rbx + 0x60]
002DE7FC  2B 43 64                        sub eax, dword ptr [rbx + 0x64]
002DE7FF  44 03 C8                        add r9d, eax
002DE802  0F 85 CE 05 00 00               jne 0x1402dedd6
002DE808  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
002DE80C  48 89 43 68                     mov qword ptr [rbx + 0x68], rax
002DE810  F6 05 EF 82 CE 00 01            test byte ptr [rip + 0xce82ef], 1
002DE817  0F 85 E3 06 00 00               jne 0x1402def00
002DE81D  F0 48 83 23 00                  lock and qword ptr [rbx], 0
002DE822  80 7C 24 33 00                  cmp byte ptr [rsp + 0x33], 0
002DE827  0F 85 09 05 00 00               jne 0x1402ded36
002DE82D  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
002DE832  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
002DE837  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
002DE83B  48 85 D2                        test rdx, rdx
002DE83E  0F 84 65 05 00 00               je 0x1402deda9
002DE844  4D 85 C9                        test r9, r9
002DE847  0F 85 51 05 00 00               jne 0x1402ded9e
002DE84D  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002DE856  48 3B F0                        cmp rsi, rax
002DE859  0F 84 BD 05 00 00               je 0x1402dee1c
002DE85F  F7 05 4F 82 CE 00 00 01 00 00   test dword ptr [rip + 0xce824f], 0x100
002DE869  0F 85 F9 04 00 00               jne 0x1402ded68
002DE86F  B9 20 00 00 40                  mov ecx, 0x40000020
002DE874  0F 32                           rdmsr
002DE876  48 C1 E2 20                     shl rdx, 0x20
002DE87A  48 0B C2                        or rax, rdx
002DE87D  E9 ED 04 00 00                  jmp 0x1402ded6f
002DE882  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
002DE886  48 85 C0                        test rax, rax
002DE889  0F 84 00 06 00 00               je 0x1402dee8f
002DE88F  45 84 D2                        test r10b, r10b
002DE892  0F 84 9C FD FF FF               je 0x1402de634
002DE898  44 38 8B 8A 00 00 00            cmp byte ptr [rbx + 0x8a], r9b
002DE89F  75 9A                           jne 0x1402de83b
002DE8A1  E9 8E FD FF FF                  jmp 0x1402de634
002DE8A6  8B 0D 30 05 B6 00               mov ecx, dword ptr [rip + 0xb60530]
002DE8AC  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DE8B3  4C 8D 04 C8                     lea r8, [rax + rcx*8]
002DE8B7  49 8B 10                        mov rdx, qword ptr [r8]
002DE8BA  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DE8C1  8B 0D 19 05 B6 00               mov ecx, dword ptr [rip + 0xb60519]
002DE8C7  4C 8B 14 C8                     mov r10, qword ptr [rax + rcx*8]
002DE8CB  49 8B 00                        mov rax, qword ptr [r8]
002DE8CE  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
002DE8D3  48 3B D0                        cmp rdx, rax
002DE8D6  75 DF                           jne 0x1402de8b7
002DE8D8  8B 0D 06 05 B6 00               mov ecx, dword ptr [rip + 0xb60506]
002DE8DE  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DE8E5  48 8D 3C C8                     lea rdi, [rax + rcx*8]
002DE8E9  4C 8B 3F                        mov r15, qword ptr [rdi]
002DE8EC  F7 05 C2 81 CE 00 00 01 00 00   test dword ptr [rip + 0xce81c2], 0x100
002DE8F6  0F 84 0D 05 00 00               je 0x1402dee09
002DE8FC  33 C9                           xor ecx, ecx
002DE8FE  E8 BD F2 FF FF                  call 0x1402ddbc0
002DE903  4C 8B C8                        mov r9, rax
002DE906  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002DE90B  48 8B 07                        mov rax, qword ptr [rdi]
002DE90E  4C 3B F8                        cmp r15, rax
002DE911  75 D6                           jne 0x1402de8e9
002DE913  0F B6 7C 24 30                  movzx edi, byte ptr [rsp + 0x30]
002DE918  E9 E1 FD FF FF                  jmp 0x1402de6fe
002DE91D  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
002DE921  33 C0                           xor eax, eax
002DE923  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002DE928  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002DE92D  48 8B 07                        mov rax, qword ptr [rdi]
002DE930  44 38 6F 21                     cmp byte ptr [rdi + 0x21], r13b
002DE934  0F 84 4B 06 00 00               je 0x1402def85
002DE93A  0F B6 54 24 30                  movzx edx, byte ptr [rsp + 0x30]
002DE93F  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
002DE944  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
002DE949  E8 82 C1 3D 00                  call 0x1406baad0
002DE94E  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
002DE953  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
002DE958  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
002DE95D  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
002DE962  75 25                           jne 0x1402de989
002DE964  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
002DE968  4C 3B E8                        cmp r13, rax
002DE96B  74 24                           je 0x1402de991
002DE96D  4D 8B C5                        mov r8, r13
002DE970  49 8B C9                        mov rcx, r9
002DE973  48 2B 4F 08                     sub rcx, qword ptr [rdi + 8]
002DE977  4C 2B C0                        sub r8, rax
002DE97A  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
002DE97D  33 D2                           xor edx, edx
002DE97F  48 0F AF C1                     imul rax, rcx
002DE983  49 F7 F0                        div r8
002DE986  89 47 18                        mov dword ptr [rdi + 0x18], eax
002DE989  4C 89 4F 08                     mov qword ptr [rdi + 8], r9
002DE98D  4C 89 6F 10                     mov qword ptr [rdi + 0x10], r13
002DE991  44 8B 4F 18                     mov r9d, dword ptr [rdi + 0x18]
002DE995  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
002DE99A  80 7F 21 00                     cmp byte ptr [rdi + 0x21], 0
002DE99E  0F 84 C9 05 00 00               je 0x1402def6d
002DE9A4  41 8B C9                        mov ecx, r9d
002DE9A7  49 0F AF CE                     imul rcx, r14
002DE9AB  48 85 C9                        test rcx, rcx
002DE9AE  0F 84 BF 04 00 00               je 0x1402dee73
002DE9B4  B8 64 00 00 00                  mov eax, 0x64
002DE9B9  48 C7 44 24 70 00 00 00 00      mov qword ptr [rsp + 0x70], 0
002DE9C2  48 F7 E1                        mul rcx
002DE9C5  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
002DE9CA  4C 8B C0                        mov r8, rax
002DE9CD  48 85 D2                        test rdx, rdx
002DE9D0  0F 85 53 05 00 00               jne 0x1402def29
002DE9D6  49 C1 E8 10                     shr r8, 0x10
002DE9DA  4C 01 43 40                     add qword ptr [rbx + 0x40], r8
002DE9DE  4D 85 E4                        test r12, r12
002DE9E1  74 33                           je 0x1402dea16
002DE9E3  80 7F 21 00                     cmp byte ptr [rdi + 0x21], 0
002DE9E7  0F 84 C5 05 00 00               je 0x1402defb2
002DE9ED  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002DE9F2  45 89 4C 24 20                  mov dword ptr [r12 + 0x20], r9d
002DE9F7  49 89 44 24 38                  mov qword ptr [r12 + 0x38], rax
002DE9FC  4D 89 6C 24 28                  mov qword ptr [r12 + 0x28], r13
002DEA01  4D 89 44 24 48                  mov qword ptr [r12 + 0x48], r8
002DEA06  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
002DEA0A  49 89 44 24 58                  mov qword ptr [r12 + 0x58], rax
002DEA0F  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
002DEA12  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002DEA16  80 BB 88 00 00 00 00            cmp byte ptr [rbx + 0x88], 0
002DEA1D  0F 85 9B FD FF FF               jne 0x1402de7be
002DEA23  4C 01 43 50                     add qword ptr [rbx + 0x50], r8
002DEA27  E9 92 FD FF FF                  jmp 0x1402de7be
002DEA2C  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
002DEA30  33 C0                           xor eax, eax
002DEA32  80 7F 21 00                     cmp byte ptr [rdi + 0x21], 0
002DEA36  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002DEA3B  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002DEA40  48 8B 07                        mov rax, qword ptr [rdi]
002DEA43  0F 84 50 05 00 00               je 0x1402def99
002DEA49  0F B6 54 24 30                  movzx edx, byte ptr [rsp + 0x30]
002DEA4E  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
002DEA53  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
002DEA58  E8 73 C0 3D 00                  call 0x1406baad0
002DEA5D  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
002DEA62  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
002DEA67  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
002DEA6C  75 25                           jne 0x1402dea93
002DEA6E  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
002DEA72  4C 3B E8                        cmp r13, rax
002DEA75  74 24                           je 0x1402dea9b
002DEA77  4D 8B C5                        mov r8, r13
002DEA7A  49 8B CA                        mov rcx, r10
002DEA7D  48 2B 4F 08                     sub rcx, qword ptr [rdi + 8]
002DEA81  4C 2B C0                        sub r8, rax
002DEA84  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
002DEA87  33 D2                           xor edx, edx
002DEA89  48 0F AF C1                     imul rax, rcx
002DEA8D  49 F7 F0                        div r8
002DEA90  89 47 18                        mov dword ptr [rdi + 0x18], eax
002DEA93  4C 89 6F 10                     mov qword ptr [rdi + 0x10], r13
002DEA97  4C 89 57 08                     mov qword ptr [rdi + 8], r10
002DEA9B  44 8B 4F 18                     mov r9d, dword ptr [rdi + 0x18]
002DEA9F  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
002DEAA4  80 7F 21 00                     cmp byte ptr [rdi + 0x21], 0
002DEAA8  0F 84 CB 04 00 00               je 0x1402def79
002DEAAE  41 8B C9                        mov ecx, r9d
002DEAB1  49 0F AF CE                     imul rcx, r14
002DEAB5  48 85 C9                        test rcx, rcx
002DEAB8  0F 84 BD 03 00 00               je 0x1402dee7b
002DEABE  B8 64 00 00 00                  mov eax, 0x64
002DEAC3  48 C7 44 24 70 00 00 00 00      mov qword ptr [rsp + 0x70], 0
002DEACC  48 F7 E1                        mul rcx
002DEACF  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
002DEAD4  4C 8B C0                        mov r8, rax
002DEAD7  48 85 D2                        test rdx, rdx
002DEADA  0F 85 6B 04 00 00               jne 0x1402def4b
002DEAE0  49 C1 E8 10                     shr r8, 0x10
002DEAE4  4C 01 43 48                     add qword ptr [rbx + 0x48], r8
002DEAE8  4D 85 E4                        test r12, r12
002DEAEB  74 2E                           je 0x1402deb1b
002DEAED  80 7F 21 00                     cmp byte ptr [rdi + 0x21], 0
002DEAF1  0F 84 C5 04 00 00               je 0x1402defbc
002DEAF7  45 89 4C 24 24                  mov dword ptr [r12 + 0x24], r9d
002DEAFC  4D 89 6C 24 30                  mov qword ptr [r12 + 0x30], r13
002DEB01  4D 89 54 24 40                  mov qword ptr [r12 + 0x40], r10
002DEB06  4D 89 44 24 50                  mov qword ptr [r12 + 0x50], r8
002DEB0B  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
002DEB0F  49 89 44 24 60                  mov qword ptr [r12 + 0x60], rax
002DEB14  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
002DEB17  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
002DEB1B  80 BB 88 00 00 00 01            cmp byte ptr [rbx + 0x88], 1
002DEB22  0F 85 A3 FC FF FF               jne 0x1402de7cb
002DEB28  4C 01 43 50                     add qword ptr [rbx + 0x50], r8
002DEB2C  E9 9A FC FF FF                  jmp 0x1402de7cb
002DEB31  40 84 FF                        test dil, dil
002DEB34  0F 85 0D FB FF FF               jne 0x1402de647
002DEB3A  45 84 D2                        test r10b, r10b
002DEB3D  0F 84 04 FB FF FF               je 0x1402de647
002DEB43  E9 EF FC FF FF                  jmp 0x1402de837
002DEB48  83 3D 51 8B B2 00 05            cmp dword ptr [rip + 0xb28b51], 5
002DEB4F  0F 86 7F FC FF FF               jbe 0x1402de7d4
002DEB55  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
002DEB59  48 8D 15 B8 A2 D6 FF            lea rdx, [rip - 0x295d48]
002DEB60  45 33 C9                        xor r9d, r9d
002DEB63  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
002DEB6B  48 C7 45 08 04 00 00 00         mov qword ptr [rbp + 8], 4
002DEB73  48 8D 0D 26 8B B2 00            lea rcx, [rip + 0xb28b26]
002DEB7A  48 C7 45 18 08 00 00 00         mov qword ptr [rbp + 0x18], 8
002DEB82  45 33 C0                        xor r8d, r8d
002DEB85  8B 80 98 00 00 00               mov eax, dword ptr [rax + 0x98]
002DEB8B  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
002DEB8F  48 8D 44 24 58                  lea rax, [rsp + 0x58]
002DEB94  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
002DEB98  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
002DEB9B  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
002DEB9F  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
002DEBA4  48 89 45 00                     mov qword ptr [rbp], rax
002DEBA8  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
002DEBAD  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
002DEBB1  48 8D 45 98                     lea rax, [rbp - 0x68]
002DEBB5  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
002DEBB9  41 8B 04 24                     mov eax, dword ptr [r12]
002DEBBD  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
002DEBC1  48 8D 44 24 60                  lea rax, [rsp + 0x60]
002DEBC6  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
002DEBCA  41 0F B6 44 24 05               movzx eax, byte ptr [r12 + 5]
002DEBD0  88 44 24 31                     mov byte ptr [rsp + 0x31], al
002DEBD4  48 8D 44 24 31                  lea rax, [rsp + 0x31]
002DEBD9  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
002DEBDD  41 0F B6 44 24 06               movzx eax, byte ptr [r12 + 6]
002DEBE3  88 44 24 30                     mov byte ptr [rsp + 0x30], al
002DEBE7  48 8D 44 24 30                  lea rax, [rsp + 0x30]
002DEBEC  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
002DEBF0  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
002DEBF5  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
002DEBF9  48 8D 45 A0                     lea rax, [rbp - 0x60]
002DEBFD  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
002DEC01  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
002DEC06  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
002DEC0A  48 8D 45 A8                     lea rax, [rbp - 0x58]
002DEC0E  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
002DEC12  49 8B 44 24 68                  mov rax, qword ptr [r12 + 0x68]
002DEC17  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
002DEC1B  48 8D 45 B0                     lea rax, [rbp - 0x50]
002DEC1F  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
002DEC23  49 8B 44 24 70                  mov rax, qword ptr [r12 + 0x70]
002DEC28  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
002DEC2C  48 8D 45 B8                     lea rax, [rbp - 0x48]
002DEC30  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
002DEC37  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
002DEC3B  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
002DEC3F  48 8D 44 24 64                  lea rax, [rsp + 0x64]
002DEC44  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
002DEC4B  49 8D 44 24 20                  lea rax, [r12 + 0x20]
002DEC50  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
002DEC57  49 8D 44 24 28                  lea rax, [r12 + 0x28]
002DEC5C  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
002DEC63  49 8D 44 24 38                  lea rax, [r12 + 0x38]
002DEC68  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
002DEC6F  49 8D 44 24 48                  lea rax, [r12 + 0x48]
002DEC74  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
002DEC7B  49 8D 44 24 58                  lea rax, [r12 + 0x58]
002DEC80  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
002DEC87  49 8D 44 24 78                  lea rax, [r12 + 0x78]
002DEC8C  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
002DEC93  48 8D 45 D0                     lea rax, [rbp - 0x30]
002DEC97  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002DEC9C  C7 44 24 20 13 00 00 00         mov dword ptr [rsp + 0x20], 0x13
002DECA4  48 C7 45 28 04 00 00 00         mov qword ptr [rbp + 0x28], 4
002DECAC  48 C7 45 38 01 00 00 00         mov qword ptr [rbp + 0x38], 1
002DECB4  48 C7 45 48 01 00 00 00         mov qword ptr [rbp + 0x48], 1
002DECBC  48 C7 45 58 08 00 00 00         mov qword ptr [rbp + 0x58], 8
002DECC4  48 C7 45 68 08 00 00 00         mov qword ptr [rbp + 0x68], 8
002DECCC  48 C7 45 78 08 00 00 00         mov qword ptr [rbp + 0x78], 8
002DECD4  48 C7 85 88 00 00 00 08 00 00 00  mov qword ptr [rbp + 0x88], 8
002DECDF  48 C7 85 98 00 00 00 04 00 00 00  mov qword ptr [rbp + 0x98], 4
002DECEA  48 C7 85 A8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xa8], 8
002DECF5  48 C7 85 B8 00 00 00 10 00 00 00  mov qword ptr [rbp + 0xb8], 0x10
002DED00  48 C7 85 C8 00 00 00 10 00 00 00  mov qword ptr [rbp + 0xc8], 0x10
002DED0B  48 C7 85 D8 00 00 00 10 00 00 00  mov qword ptr [rbp + 0xd8], 0x10
002DED16  48 C7 85 E8 00 00 00 10 00 00 00  mov qword ptr [rbp + 0xe8], 0x10
002DED21  48 C7 85 F8 00 00 00 08 00 00 00  mov qword ptr [rbp + 0xf8], 8
002DED2C  E8 AF 73 14 00                  call 0x1404260e0
002DED31  E9 9E FA FF FF                  jmp 0x1402de7d4
002DED36  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002DED3F  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
002DED46  4D 85 C0                        test r8, r8
002DED49  0F 85 89 01 00 00               jne 0x1402deed8
002DED4F  FB                              sti
002DED50  E9 D8 FA FF FF                  jmp 0x1402de82d
002DED55  B9 20 00 00 40                  mov ecx, 0x40000020
002DED5A  0F 32                           rdmsr
002DED5C  48 C1 E2 20                     shl rdx, 0x20
002DED60  48 0B C2                        or rax, rdx
002DED63  E9 61 F9 FF FF                  jmp 0x1402de6c9
002DED68  33 C9                           xor ecx, ecx
002DED6A  E8 51 EE FF FF                  call 0x1402ddbc0
002DED6F  8B 0D 5F 00 B6 00               mov ecx, dword ptr [rip + 0xb6005f]
002DED75  4C 8B C8                        mov r9, rax
002DED78  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DED7F  4D 8B F9                        mov r15, r9
002DED82  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
002DED86  48 8B 8E D0 8B 00 00            mov rcx, qword ptr [rsi + 0x8bd0]
002DED8D  4C 2B FA                        sub r15, rdx
002DED90  8B 15 4A 00 B6 00               mov edx, dword ptr [rip + 0xb6004a]
002DED96  4C 8B 34 D1                     mov r14, qword ptr [rcx + rdx*8]
002DED9A  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
002DED9E  4C 89 0A                        mov qword ptr [rdx], r9
002DEDA1  4C 89 7A 08                     mov qword ptr [rdx + 8], r15
002DEDA5  4C 89 72 10                     mov qword ptr [rdx + 0x10], r14
002DEDA9  B0 01                           mov al, 1
002DEDAB  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
002DEDB2  48 33 CC                        xor rcx, rsp
002DEDB5  E8 86 D8 3C 00                  call 0x1406ac640
002DEDBA  48 8B 9C 24 60 02 00 00         mov rbx, qword ptr [rsp + 0x260]
002DEDC2  48 81 C4 10 02 00 00            add rsp, 0x210
002DEDC9  41 5F                           pop r15
002DEDCB  41 5E                           pop r14
002DEDCD  41 5D                           pop r13
002DEDCF  41 5C                           pop r12
002DEDD1  5F                              pop rdi
002DEDD2  5E                              pop rsi
002DEDD3  5D                              pop rbp
002DEDD4  C3                              ret
002DEDD5  CC                              int3
002DEDD6  4C 8B 53 50                     mov r10, qword ptr [rbx + 0x50]
002DEDDA  48 C7 43 50 00 00 00 00         mov qword ptr [rbx + 0x50], 0
002DEDE2  89 53 60                        mov dword ptr [rbx + 0x60], edx
002DEDE5  44 89 43 64                     mov dword ptr [rbx + 0x64], r8d
002DEDE9  85 C0                           test eax, eax
002DEDEB  0F 84 17 FA FF FF               je 0x1402de808
002DEDF1  33 D2                           xor edx, edx
002DEDF3  41 F7 F1                        div r9d
002DEDF6  8B C8                           mov ecx, eax
002DEDF8  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
002DEDFC  49 0F AF CA                     imul rcx, r10
002DEE00  48 01 4B 58                     add qword ptr [rbx + 0x58], rcx
002DEE04  E9 FF F9 FF FF                  jmp 0x1402de808
002DEE09  B9 20 00 00 40                  mov ecx, 0x40000020
002DEE0E  0F 32                           rdmsr
002DEE10  48 C1 E2 20                     shl rdx, 0x20
002DEE14  48 0B C2                        or rax, rdx
002DEE17  E9 E7 FA FF FF                  jmp 0x1402de903
002DEE1C  8B 0D BA FF B5 00               mov ecx, dword ptr [rip + 0xb5ffba]
002DEE22  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DEE29  4C 8D 04 C8                     lea r8, [rax + rcx*8]
002DEE2D  49 8B 10                        mov rdx, qword ptr [r8]
002DEE30  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DEE37  8B 0D A3 FF B5 00               mov ecx, dword ptr [rip + 0xb5ffa3]
002DEE3D  4C 8B 34 C8                     mov r14, qword ptr [rax + rcx*8]
002DEE41  49 8B 00                        mov rax, qword ptr [r8]
002DEE44  48 3B D0                        cmp rdx, rax
002DEE47  75 E4                           jne 0x1402dee2d
002DEE49  8B 0D 95 FF B5 00               mov ecx, dword ptr [rip + 0xb5ff95]
002DEE4F  48 8B 86 D0 8B 00 00            mov rax, qword ptr [rsi + 0x8bd0]
002DEE56  48 8D 1C C8                     lea rbx, [rax + rcx*8]
002DEE5A  4C 8B 3B                        mov r15, qword ptr [rbx]
002DEE5D  E8 26 ED FF FF                  call 0x1402ddb88
002DEE62  4C 8B C8                        mov r9, rax
002DEE65  48 8B 03                        mov rax, qword ptr [rbx]
002DEE68  4C 3B F8                        cmp r15, rax
002DEE6B  0F 84 29 FF FF FF               je 0x1402ded9a
002DEE71  EB E7                           jmp 0x1402dee5a
002DEE73  45 33 C0                        xor r8d, r8d
002DEE76  E9 5F FB FF FF                  jmp 0x1402de9da
002DEE7B  45 33 C0                        xor r8d, r8d
002DEE7E  E9 61 FC FF FF                  jmp 0x1402deae4
002DEE83  88 44 24 32                     mov byte ptr [rsp + 0x32], al
002DEE87  48 8B C8                        mov rcx, rax
002DEE8A  E9 91 F7 FF FF                  jmp 0x1402de620
002DEE8F  4C 39 4B 50                     cmp qword ptr [rbx + 0x50], r9
002DEE93  74 1E                           je 0x1402deeb3
002DEE95  8B 43 60                        mov eax, dword ptr [rbx + 0x60]
002DEE98  39 86 48 86 00 00               cmp dword ptr [rsi + 0x8648], eax
002DEE9E  0F 85 EB F9 FF FF               jne 0x1402de88f
002DEEA4  8B 43 64                        mov eax, dword ptr [rbx + 0x64]
002DEEA7  39 86 44 86 00 00               cmp dword ptr [rsi + 0x8644], eax
002DEEAD  0F 85 DC F9 FF FF               jne 0x1402de88f
002DEEB3  45 84 DB                        test r11b, r11b
002DEEB6  0F 84 7F F9 FF FF               je 0x1402de83b
002DEEBC  48 3B 4B 68                     cmp rcx, qword ptr [rbx + 0x68]
002DEEC0  0F 84 75 F9 FF FF               je 0x1402de83b
002DEEC6  E9 C4 F9 FF FF                  jmp 0x1402de88f
002DEECB  45 84 DB                        test r11b, r11b
002DEECE  75 52                           jne 0x1402def22
002DEED0  41 B0 01                        mov r8b, 1
002DEED3  E9 A7 F7 FF FF                  jmp 0x1402de67f
002DEED8  41 0F 0D 08                     prefetchw byte ptr [r8]
002DEEDC  41 8B 00                        mov eax, dword ptr [r8]
002DEEDF  8B D0                           mov edx, eax
002DEEE1  0F BA F2 15                     btr edx, 0x15
002DEEE5  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
002DEEEA  75 F3                           jne 0x1402deedf
002DEEEC  0F BA E0 15                     bt eax, 0x15
002DEEF0  0F 83 59 FE FF FF               jae 0x1402ded4f
002DEEF6  E8 D5 42 F8 FF                  call 0x1402631d0
002DEEFB  E9 4F FE FF FF                  jmp 0x1402ded4f
002DEF00  8B 05 52 EF C2 00               mov eax, dword ptr [rip + 0xc2ef52]
002DEF06  85 C0                           test eax, eax
002DEF08  0F 85 0F F9 FF FF               jne 0x1402de81d
002DEF0E  48 8B 95 48 01 00 00            mov rdx, qword ptr [rbp + 0x148]
002DEF15  48 8B CB                        mov rcx, rbx
002DEF18  E8 D3 3F 0B 00                  call 0x140392ef0
002DEF1D  E9 00 F9 FF FF                  jmp 0x1402de822
002DEF22  32 C0                           xor al, al
002DEF24  E9 82 FE FF FF                  jmp 0x1402dedab
002DEF29  48 8B C1                        mov rax, rcx
002DEF2C  48 C1 E8 10                     shr rax, 0x10
002DEF30  4C 6B C0 64                     imul r8, rax, 0x64
002DEF34  48 C1 E0 10                     shl rax, 0x10
002DEF38  48 2B C8                        sub rcx, rax
002DEF3B  48 6B C1 64                     imul rax, rcx, 0x64
002DEF3F  48 C1 E8 10                     shr rax, 0x10
002DEF43  4C 03 C0                        add r8, rax
002DEF46  E9 8F FA FF FF                  jmp 0x1402de9da
002DEF4B  48 8B C1                        mov rax, rcx
002DEF4E  48 C1 E8 10                     shr rax, 0x10
002DEF52  4C 6B C0 64                     imul r8, rax, 0x64
002DEF56  48 C1 E0 10                     shl rax, 0x10
002DEF5A  48 2B C8                        sub rcx, rax
002DEF5D  48 6B C1 64                     imul rax, rcx, 0x64
002DEF61  48 C1 E8 10                     shr rax, 0x10
002DEF65  4C 03 C0                        add r8, rax
002DEF68  E9 77 FB FF FF                  jmp 0x1402deae4
002DEF6D  45 8B C1                        mov r8d, r9d
002DEF70  4D 0F AF C6                     imul r8, r14
002DEF74  E9 61 FA FF FF                  jmp 0x1402de9da
002DEF79  45 8B C1                        mov r8d, r9d
002DEF7C  4D 0F AF C6                     imul r8, r14
002DEF80  E9 5F FB FF FF                  jmp 0x1402deae4
002DEF85  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
002DEF8A  E8 41 BB 3D 00                  call 0x1406baad0
002DEF8F  44 8B 4C 24 34                  mov r9d, dword ptr [rsp + 0x34]
002DEF94  E9 01 FA FF FF                  jmp 0x1402de99a
002DEF99  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
002DEF9E  E8 2D BB 3D 00                  call 0x1406baad0
002DEFA3  44 8B 4C 24 34                  mov r9d, dword ptr [rsp + 0x34]
002DEFA8  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
002DEFAD  E9 F2 FA FF FF                  jmp 0x1402deaa4
002DEFB2  45 89 4C 24 78                  mov dword ptr [r12 + 0x78], r9d
002DEFB7  E9 5A FA FF FF                  jmp 0x1402dea16
002DEFBC  45 89 4C 24 7C                  mov dword ptr [r12 + 0x7c], r9d
002DEFC1  E9 55 FB FF FF                  jmp 0x1402deb1b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmUpdatePerformanceFeedback(__int64 a1, unsigned __int8 a2, unsigned __int8 a3, unsigned __int8 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned int v_stack_m1E8;
    unsigned int v_stack_m1EC;
    unsigned int v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned int v_stack_m214;
    unsigned __int8 v_stack_m215;
    unsigned __int8 v_stack_m216;
    unsigned __int8 v_stack_m217;
    unsigned __int8 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
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
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p32;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p68;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (528);
    result = (*(unsigned __int64 *)(v_rip + 11714970)) ^ (v_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m218 = a2;
    v_stack_m1C8 = a5;
    v_stack_m217 = a3;
    v_stack_m214 = 0;
    v_stack_m1E0 = 0;
    v_stack_m210 = 0;
    v_stack_m208 = 0;
    v_stack_m1D0 = 0;
    if ((*(unsigned int *)(a1 + 35104)) != 3) goto loc_002DEE83;
    v_stack_m216 = 1;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11929547)) * 8)) >> (1);
loc_002DE620:
    v_stack_m1B8 = a1;
    if (a2 == 0) goto loc_002DE882;
loc_002DE634:
    a3 = 0;
    a1 = 0;
loc_002DE639:
    if (0 < 2) goto loc_002DE66B;
    if (0 == 0) goto loc_002DEB31;
loc_002DE647:
    result = KeDisableInterrupts(a1, a5, a3, 0);
    v_stack_m215 = (unsigned __int8)(result);
    if (((*(unsigned __int8 *)(v_rip + 13534387)) & (33)) != 0) goto loc_002DE683;
loc_002DE659:
    if (condition_is_above_or_equal) goto loc_002DE695;
    result = KxWaitForSpinLockAndAcquire(a1 + 34960, a5, a3, 0);
    goto loc_002DE695;
loc_002DE66B:
    if (*(unsigned __int64 *)(a1 + 34960 + a1 + 34960 * 8 + 24) == 0) goto loc_002DE67F;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 34960 + a1 + 34960 * 8 + 24) + 32)) != 0) goto loc_002DEECB;
loc_002DE67F:
    a1 = (unsigned int)((a1 + 34960) + 1);
    goto loc_002DE639;
loc_002DE683:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12777423))) != 0) goto loc_002DE659;
    result = KiAcquireSpinLockInstrumented(a1 + 34960, *(unsigned __int64 *)(a1 + 34960 + a1 + 34960 * 8 + 24), a3, 0);
loc_002DE695:
    if (v_stack_m216 == 0) goto loc_002DE70F;
    if (a1 == (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_002DE8A6;
    if (((*(unsigned int *)(v_rip + 13534204)) & (256)) == 0) goto loc_002DED55;
    a1 = 0;
    result = HvlGetReferenceTimeUsingTscPage(a1, *(unsigned __int64 *)(a1 + 34960 + a1 + 34960 * 8 + 24), a3, 0);
loc_002DE6C9:
    v_stack_m208 = result;
    v_r15 = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11929349)) * 8));
    v_stack_m1D0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11929333)) * 8);
loc_002DE6FE:
    result = (result) - (v_r15);
    v_r14 = (result) - (*(unsigned __int64 *)(a1 + 34960 + 112));
    *(unsigned __int64 *)(a1 + 34960 + 112) = result;
loc_002DE70F:
    v_stack_m1C0 = *(unsigned __int64 *)(a1 + 35256);
    if (*(unsigned __int64 *)(a1 + 35256) == 0) goto loc_002DE7B1;
    a2 = 0;
    a1 = (*(unsigned __int64 *)(a1 + 35256)) + (160);
    v_r12 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 152))) << (7);
    v_r12 = (v_r12) + (a1);
    result = memset(v_r12, a2, 128, result);
    if ((*(unsigned int *)(v_stack_m1C0 + 152)) == 8) {
        *(unsigned int *)(v_stack_m1C0 + 152) = 0;
    }
    *(unsigned int *)(v_r12) = (unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))));
    *(unsigned __int8 *)(v_r12 + 5) = 0;
    *(unsigned __int8 *)(v_r12 + 4) = 0;
    result = RtlGetInterruptTimePrecise(v_stack_m188, a2, 128, result);
    *(unsigned __int64 *)(v_r12 + 8) = result;
    *(unsigned __int8 *)(v_r12 + 6) = (unsigned __int8)(v_stack_m217);
    *(unsigned __int64 *)(v_r12 + 16) = v_r14;
    *(unsigned __int64 *)(v_r12 + 24) = *(unsigned __int64 *)(a1 + 34960 + 48);
    *(unsigned __int64 *)(v_r12 + 104) = v_stack_m208;
    *(unsigned __int64 *)(v_r12 + 112) = v_r15;
loc_002DE7B1:
    if (*(unsigned __int64 *)(a1 + 34960 + 24) != 0) goto loc_002DE91D;
loc_002DE7BE:
    if (*(unsigned __int64 *)(a1 + 34960 + 32) != 0) goto loc_002DEA2C;
loc_002DE7CB:
    if (v_r12 != 0) goto loc_002DEB48;
loc_002DE7D4:
    result = v_stack_m208;
    if ((*(unsigned __int8 *)(a1 + 34960 + 136)) == 2) {
        result = (v_stack_m208) * (v_r14);
    }
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 34376))))) - (*(unsigned int *)(a1 + 34960 + 96)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 34372))))) - (*(unsigned int *)(a1 + 34960 + 100)));
    a4 = (unsigned int)((a4) + ((unsigned int)(result)));
    if (condition_is_not_equal) goto loc_002DEDD6;
loc_002DE808:
    *(unsigned __int64 *)(a1 + 34960 + 104) = v_stack_m1B8;
    if (((*(unsigned __int8 *)(v_rip + 13533935)) & (1)) != 0) goto loc_002DEF00;
loc_002DE81D:
loc_002DE822:
    if (v_stack_m215 != 0) goto loc_002DED36;
loc_002DE82D:
loc_002DE837:
loc_002DE83B:
    if (v_stack_m1C8 == 0) goto loc_002DEDA9;
    if (v_stack_m208 != 0) goto loc_002DED9E;
    if (a1 == (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_002DEE1C;
    if (((*(unsigned int *)(v_rip + 13533775)) & (256)) != 0) goto loc_002DED68;
    a2 = (v_stack_m1C8) << (32);
    result = (*(unsigned __int64 *)(gs_base + (0 + 32))) | (a2);
    goto loc_002DED6F;
loc_002DE882:
    if (*(unsigned __int64 *)(a1 + 34960 + 56) == 0) goto loc_002DEE8F;
loc_002DE88F:
    if (a4 == 0) goto loc_002DE634;
    if ((*(unsigned __int8 *)(a1 + 34960 + 138)) != ((unsigned __int8)(v_stack_m208))) goto loc_002DE83B;
    goto loc_002DE634;
loc_002DE8A6:
loc_002DE8B7:
    v_stack_m1D0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11928857)) * 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11928880)) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11928880)) * 8))) goto loc_002DE8B7;
loc_002DE8E9:
    if (((*(unsigned int *)(v_rip + 13533634)) & (256)) == 0) goto loc_002DEE09;
    a1 = 0;
    result = HvlGetReferenceTimeUsingTscPage(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11928880)) * 8), *(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11928880)) * 8, v_stack_m208);
loc_002DE903:
    v_stack_m208 = result;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11928838)) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11928838)) * 8))) goto loc_002DE8E9;
    goto loc_002DE6FE;
loc_002DE91D:
    result = 0;
    v_stack_m200 = 0;
    v_stack_m1F8 = 0;
    if ((*(unsigned __int8 *)(v_stack_m218 + 33)) == 0) goto loc_002DEF85;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_m218 + 40), v_stack_m218, v_stack_m1F8, v_stack_m200);
    v_stack_m1E0 = v_stack_m200;
    if (v_stack_m218 != 0) goto loc_002DE989;
    if (v_stack_m1F8 == (*(unsigned __int64 *)(v_stack_m218 + 16))) goto loc_002DE991;
    a1 = (v_stack_m200) - (*(unsigned __int64 *)(v_stack_m218 + 8));
    a3 = (v_stack_m1F8) - (*(unsigned __int64 *)(v_stack_m218 + 16));
    a2 = 0;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m218 + 36))) * (a1);
    *(unsigned int *)(v_stack_m218 + 24) = (unsigned int)(result);
loc_002DE989:
    *(unsigned __int64 *)(v_stack_m218 + 8) = v_stack_m200;
    *(unsigned __int64 *)(v_stack_m218 + 16) = v_stack_m1F8;
loc_002DE991:
    v_stack_m214 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218 + 24)));
loc_002DE99A:
    if ((*(unsigned __int8 *)(v_stack_m218 + 33)) == 0) goto loc_002DEF6D;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218 + 24))))) * (v_stack_m1D0);
    if (a1 == 0) goto loc_002DEE73;
    v_stack_m1D8 = 0;
    v_stack_m1D8 = 0;
    if (0 != 0) goto loc_002DEF29;
    a3 = (100) >> (16);
loc_002DE9DA:
    if (v_r12 == 0) goto loc_002DEA16;
    if ((*(unsigned __int8 *)(v_stack_m218 + 33)) == 0) goto loc_002DEFB2;
    *(unsigned int *)(v_r12 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218 + 24)));
    *(unsigned __int64 *)(v_r12 + 56) = v_stack_m1E0;
    *(unsigned __int64 *)(v_r12 + 40) = v_stack_m1F8;
    *(unsigned __int64 *)(v_r12 + 72) = a3;
    *(unsigned __int64 *)(v_r12 + 88) = *(unsigned __int64 *)(a1 + 34960 + 64);
    v_stack_m210 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218 + 36)));
loc_002DEA16:
    if ((*(unsigned __int8 *)(a1 + 34960 + 136)) != 0) goto loc_002DE7BE;
    goto loc_002DE7BE;
loc_002DEA2C:
    result = 0;
    v_stack_m200 = 0;
    v_stack_m1F8 = 0;
    if ((*(unsigned __int8 *)(v_stack_m218 + 33)) == 0) goto loc_002DEF99;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_m218 + 40), v_stack_m218, v_stack_m1F8, v_stack_m200);
    if (v_stack_m218 != 0) goto loc_002DEA93;
    if (v_stack_m1F8 == (*(unsigned __int64 *)(v_stack_m218 + 16))) goto loc_002DEA9B;
    a1 = (v_stack_m200) - (*(unsigned __int64 *)(v_stack_m218 + 8));
    a3 = (v_stack_m1F8) - (*(unsigned __int64 *)(v_stack_m218 + 16));
    a2 = 0;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m218 + 36))) * (a1);
    *(unsigned int *)(v_stack_m218 + 24) = (unsigned int)(result);
loc_002DEA93:
    *(unsigned __int64 *)(v_stack_m218 + 16) = v_stack_m1F8;
    *(unsigned __int64 *)(v_stack_m218 + 8) = v_stack_m200;
loc_002DEA9B:
    v_stack_m214 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218 + 24)));
loc_002DEAA4:
    if ((*(unsigned __int8 *)(v_stack_m218 + 33)) == 0) goto loc_002DEF79;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218 + 24))))) * (v_stack_m1D0);
    if (a1 == 0) goto loc_002DEE7B;
    v_stack_m1D8 = 0;
    v_stack_m1D8 = 0;
    if (0 != 0) goto loc_002DEF4B;
    a3 = (100) >> (16);
loc_002DEAE4:
    if (v_r12 == 0) goto loc_002DEB1B;
    if ((*(unsigned __int8 *)(v_stack_m218 + 33)) == 0) goto loc_002DEFBC;
    *(unsigned int *)(v_r12 + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218 + 24)));
    *(unsigned __int64 *)(v_r12 + 48) = v_stack_m1F8;
    *(unsigned __int64 *)(v_r12 + 64) = v_stack_m200;
    *(unsigned __int64 *)(v_r12 + 80) = a3;
    *(unsigned __int64 *)(v_r12 + 96) = *(unsigned __int64 *)(a1 + 34960 + 72);
    v_stack_m210 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m218 + 36)));
loc_002DEB1B:
    if ((*(unsigned __int8 *)(a1 + 34960 + 136)) != 1) goto loc_002DE7CB;
    goto loc_002DE7CB;
loc_002DEB31:
    if ((unsigned __int8)(v_stack_m218) != 0) goto loc_002DE647;
    if ((unsigned __int8)(v_stack_m200) == 0) goto loc_002DE647;
    goto loc_002DE837;
loc_002DEB48:
    if ((*(unsigned int *)(v_rip + 11701073)) <= 5) goto loc_002DE7D4;
    a4 = 0;
    v_stack_m150 = 4;
    v_stack_m140 = 4;
    v_stack_m130 = 8;
    a3 = 0;
    v_stack_m1F0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1C0 + 152)));
    v_stack_m158 = v_stack_m1F0;
    v_stack_m1EC = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36)));
    v_stack_m148 = v_stack_m1EC;
    v_stack_m1B0 = *(unsigned __int64 *)(v_r12 + 8);
    v_stack_m138 = v_stack_m1B0;
    v_stack_m1E8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12)));
    v_stack_m128 = v_stack_m1E8;
    v_stack_m217 = (unsigned __int8)(*(unsigned __int8 *)(v_r12 + 5));
    v_stack_m118 = v_stack_m217;
    v_stack_m218 = (unsigned __int8)(*(unsigned __int8 *)(v_r12 + 6));
    v_stack_m108 = v_stack_m218;
    v_stack_m1A8 = *(unsigned __int64 *)(v_r12 + 16);
    v_stack_mF8 = v_stack_m1A8;
    v_stack_m1A0 = *(unsigned __int64 *)(v_r12 + 24);
    v_stack_mE8 = v_stack_m1A0;
    v_stack_m198 = *(unsigned __int64 *)(v_r12 + 104);
    v_stack_mD8 = v_stack_m198;
    v_stack_m190 = *(unsigned __int64 *)(v_r12 + 112);
    v_stack_mC8 = v_stack_m190;
    v_stack_m1E4 = (unsigned int)((unsigned int)(v_stack_m210));
    v_stack_mB8 = v_stack_m1E4;
    v_stack_mA8 = v_r12 + 32;
    v_stack_m98 = v_r12 + 40;
    v_stack_m88 = v_r12 + 56;
    v_stack_m78 = v_r12 + 72;
    v_stack_m68 = v_r12 + 88;
    v_stack_m58 = v_r12 + 120;
    v_stack_m220 = v_stack_m178;
    v_stack_m228 = 19;
    v_stack_m120 = 4;
    v_stack_m110 = 1;
    v_stack_m100 = 1;
    v_stack_mF0 = 8;
    v_stack_mE0 = 8;
    v_stack_mD0 = 8;
    v_stack_mC0 = 8;
    v_stack_mB0 = 4;
    v_stack_mA0 = 8;
    v_stack_m90 = 16;
    v_stack_m80 = 16;
    v_stack_m70 = 16;
    v_stack_m60 = 16;
    v_stack_m50 = 8;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 11701030, v_rip - 2710856, a3, a4);
    goto loc_002DE7D4;
loc_002DED36:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_002DEED8;
loc_002DED4F:
    goto loc_002DE82D;
loc_002DED55:
    a2 = (v_rip - 2710856) << (32);
    result = (result) | (a2);
    goto loc_002DE6C9;
loc_002DED68:
    a1 = 0;
    result = HvlGetReferenceTimeUsingTscPage(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_002DED6F:
    v_r15 = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927647)) * 8));
loc_002DED9A:
loc_002DED9E:
    *(unsigned __int64 *)(v_stack_m1C8) = result;
    *(unsigned __int64 *)(v_stack_m1C8 + 8) = v_r15;
    *(unsigned __int64 *)(v_stack_m1C8 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927626)) * 8);
loc_002DEDA9:
loc_002DEDAB:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m1C8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), result);
    v_rsp = (v_rsp) + (528);
    return result;
loc_002DEDD6:
    *(unsigned __int64 *)(v_stack_p18 + 80) = 0;
    *(unsigned int *)(v_stack_p18 + 96) = (unsigned int)(v_stack_m1C8);
    *(unsigned int *)(v_stack_p18 + 100) = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536));
    if ((unsigned int)(result) == 0) goto loc_002DE808;
    a2 = 0;
    v_stack_p34 = (unsigned int)((unsigned int)((unsigned int)(result)));
    a1 = ((unsigned int)((unsigned int)(result))) * (*(unsigned __int64 *)(v_stack_p18 + 80));
    goto loc_002DE808;
loc_002DEE09:
    a2 = (a2) << (32);
    result = (result) | (a2);
    goto loc_002DE903;
loc_002DEE1C:
loc_002DEE2D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927482)) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927482)) * 8))) goto loc_002DEE2D;
loc_002DEE5A:
    result = HvlGetReferenceTime((unsigned int)(*(unsigned int *)(v_rip + 11927445)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927482)) * 8), *(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927482)) * 8, result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8))) goto loc_002DED9A;
    goto loc_002DEE5A;
loc_002DEE73:
    a3 = 0;
    goto loc_002DE9DA;
loc_002DEE7B:
    a3 = 0;
    goto loc_002DEAE4;
loc_002DEE83:
    v_stack_p32 = (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8));
    goto loc_002DE620;
loc_002DEE8F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8 + 80)) == result) goto loc_002DEEB3;
    if ((*(unsigned int *)(a1 + 34376)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8 + 96))))) goto loc_002DE88F;
    if ((*(unsigned int *)(a1 + 34372)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8 + 100))))) goto loc_002DE88F;
loc_002DEEB3:
    if (0 == 0) goto loc_002DE83B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8 + 104))) goto loc_002DE83B;
    goto loc_002DE88F;
loc_002DEECB:
    if (0 != 0) goto loc_002DEF22;
    goto loc_002DE67F;
loc_002DEED8:
loc_002DEEDF:
    if (0 != 0) goto loc_002DEEDF;
    if (condition_is_above_or_equal) goto loc_002DED4F;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(1)))), 1, result);
    goto loc_002DED4F;
loc_002DEF00:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12775250))) != 0) goto loc_002DE81D;
    result = KiReleaseSpinLockInstrumented(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8, v_stack_p0, 1, result);
    goto loc_002DE822;
loc_002DEF22:
    result = 0;
    goto loc_002DEDAB;
loc_002DEF29:
    result = (*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8) >> (16);
    a3 = (1) * (result);
    result = (result) << (16);
    a1 = (*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927445)) * 8) - (result);
    result = (result) * (a1);
    result = (result) >> (16);
    a3 = (a3) + (result);
    goto loc_002DE9DA;
loc_002DEF4B:
    result = (a1) >> (16);
    a3 = (a3) * (result);
    result = (result) << (16);
    a1 = (a1) - (result);
    result = (result) * (a1);
    result = (result) >> (16);
    a3 = (a3) + (result);
    goto loc_002DEAE4;
loc_002DEF6D:
    a3 = ((unsigned int)((unsigned int)(result))) * (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927459)) * 8));
    goto loc_002DE9DA;
loc_002DEF79:
    a3 = ((unsigned int)((unsigned int)(result))) * (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35792) + (unsigned int)(*(unsigned int *)(v_rip + 11927459)) * 8));
    goto loc_002DEAE4;
loc_002DEF85:
    result = guard_dispatch_icall(a1, v_stack_p34, a3, result);
    goto loc_002DE99A;
loc_002DEF99:
    result = guard_dispatch_icall(a1, v_stack_p34, a3, (unsigned int)(v_stack_p34));
    goto loc_002DEAA4;
loc_002DEFB2:
    *(unsigned int *)(v_r12 + 120) = (unsigned int)((unsigned int)(v_stack_p34));
    goto loc_002DEA16;
loc_002DEFBC:
    *(unsigned int *)(v_r12 + 124) = (unsigned int)((unsigned int)(v_stack_p34));
    goto loc_002DEB1B;
}
```

## 5. (Beta) C Style

```c
int64_t PpmUpdatePerformanceFeedback(void *Arg1, uint8_t Arg2, uint8_t Arg3, uint8_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m178;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint32_t v_stack_m1E8;
    uint32_t v_stack_m1EC;
    uint32_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint32_t v_stack_m214;
    uint8_t v_stack_m215;
    uint8_t v_stack_m216;
    uint8_t v_stack_m217;
    uint8_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
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
    uint64_t v_stack_mF8;
    uint64_t v_stack_p0;
    uint64_t v_stack_p18;
    uint8_t v_stack_p32;
    uint32_t v_stack_p34;
    uint64_t v_stack_p68;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (528);
    result = (*(uint64_t *)(v_rip + 0xB2C19A)) ^ (local_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m218 = Arg2;
    v_stack_m1C8 = Arg5;
    v_stack_m217 = Arg3;
    v_stack_m214 = 0;
    v_stack_m1E0 = 0;
    v_stack_m210 = 0;
    v_stack_m208 = 0;
    v_stack_m1D0 = 0;
    if ((*(uint32_t *)(arg1 + 0x8920)) != 3) goto loc_002DEE83;
    v_stack_m216 = 1;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB607CB)) * 8)) >> (1);
loc_002DE620:
    v_stack_m1B8 = Arg1;
    if (Arg2 == 0) goto loc_002DE882;
loc_002DE634:
    Arg3 = 0;
    Arg1 = 0;
loc_002DE639:
    if (0 < 2) goto loc_002DE66B;
    if (0 == 0) goto loc_002DEB31;
loc_002DE647:
    result = KeDisableInterrupts(Arg1, Arg5, Arg3, 0);
    v_stack_m215 = (uint8_t)(result);
    if (((*(uint8_t *)(v_rip + 0xCE84B3)) & (33)) != 0) goto loc_002DE683;
loc_002DE659:
    if (condition_is_above_or_equal) goto loc_002DE695;
    result = KxWaitForSpinLockAndAcquire(Arg1 + 34960, Arg5, Arg3, 0);
    goto loc_002DE695;
loc_002DE66B:
    if (*(uint64_t *)(arg1 + 0x8890 + arg1 + 0x8890 * 8 + 0x18) == 0) goto loc_002DE67F;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8890 + arg1 + 0x8890 * 8 + 0x18) + 0x20)) != 0) goto loc_002DEECB;
loc_002DE67F:
    Arg1 = (uint32_t)((Arg1 + 34960) + 1);
    goto loc_002DE639;
loc_002DE683:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2F7CF))) != 0) goto loc_002DE659;
    result = KiAcquireSpinLockInstrumented(Arg1 + 34960, *(uint64_t *)(arg1 + 0x8890 + arg1 + 0x8890 * 8 + 0x18), Arg3, 0);
loc_002DE695:
    if (v_stack_m216 == 0) goto loc_002DE70F;
    if (Arg1 == (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_002DE8A6;
    if (((*(uint32_t *)(v_rip + 0xCE83FC)) & (256)) == 0) goto loc_002DED55;
    Arg1 = 0;
    result = HvlGetReferenceTimeUsingTscPage(Arg1, *(uint64_t *)(arg1 + 0x8890 + arg1 + 0x8890 * 8 + 0x18), Arg3, 0);
loc_002DE6C9:
    v_stack_m208 = result;
    local_r15 = (result) - (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60705)) * 8));
    v_stack_m1D0 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB606F5)) * 8);
loc_002DE6FE:
    result = (result) - (local_r15);
    local_r14 = (result) - (*(uint64_t *)(arg1 + 0x8890 + 0x70));
    *(uint64_t *)(arg1 + 0x8890 + 0x70) = result;
loc_002DE70F:
    v_stack_m1C0 = *(uint64_t *)(arg1 + 0x89B8);
    if (*(uint64_t *)(arg1 + 0x89B8) == 0) goto loc_002DE7B1;
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(arg1 + 0x89B8)) + (160);
    local_r12 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x98))) << (7);
    local_r12 = (local_r12) + (Arg1);
    result = memset(local_r12, Arg2, 128, result);
    if ((*(uint32_t *)(v_stack_m1C0 + 0x98)) == 8) {
        *(uint32_t *)(v_stack_m1C0 + 0x98) = 0;
    }
    *(uint32_t *)(local_r12) = (uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))));
    *(uint8_t *)(local_r12 + 0x5) = 0;
    *(uint8_t *)(local_r12 + 0x4) = 0;
    result = RtlGetInterruptTimePrecise(v_stack_m188, Arg2, 128, result);
    *(uint64_t *)(local_r12 + 0x8) = result;
    *(uint8_t *)(local_r12 + 0x6) = (uint8_t)(v_stack_m217);
    *(uint64_t *)(local_r12 + 0x10) = local_r14;
    *(uint64_t *)(local_r12 + 0x18) = *(uint64_t *)(arg1 + 0x8890 + 0x30);
    *(uint64_t *)(local_r12 + 0x68) = v_stack_m208;
    *(uint64_t *)(local_r12 + 0x70) = local_r15;
loc_002DE7B1:
    if (*(uint64_t *)(arg1 + 0x8890 + 0x18) != 0) goto loc_002DE91D;
loc_002DE7BE:
    if (*(uint64_t *)(arg1 + 0x8890 + 0x20) != 0) goto loc_002DEA2C;
loc_002DE7CB:
    if (local_r12 != 0) goto loc_002DEB48;
loc_002DE7D4:
    result = v_stack_m208;
    if ((*(uint8_t *)(arg1 + 0x8890 + 0x88)) == 2) {
        result = (v_stack_m208) * (local_r14);
    }
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8648))))) - (*(uint32_t *)(arg1 + 0x8890 + 0x60)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8644))))) - (*(uint32_t *)(arg1 + 0x8890 + 0x64)));
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(result)));
    if (condition_is_not_equal) goto loc_002DEDD6;
loc_002DE808:
    *(uint64_t *)(arg1 + 0x8890 + 0x68) = v_stack_m1B8;
    if (((*(uint8_t *)(v_rip + 0xCE82EF)) & (1)) != 0) goto loc_002DEF00;
loc_002DE81D:
loc_002DE822:
    if (v_stack_m215 != 0) goto loc_002DED36;
loc_002DE82D:
loc_002DE837:
loc_002DE83B:
    if (v_stack_m1C8 == 0) goto loc_002DEDA9;
    if (v_stack_m208 != 0) goto loc_002DED9E;
    if (Arg1 == (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_002DEE1C;
    if (((*(uint32_t *)(v_rip + 0xCE824F)) & (256)) != 0) goto loc_002DED68;
    Arg2 = (v_stack_m1C8) << (32);
    result = (*(uint64_t *)(gs_base + (0 + 0x20))) | (Arg2);
    goto loc_002DED6F;
loc_002DE882:
    if (*(uint64_t *)(arg1 + 0x8890 + 0x38) == 0) goto loc_002DEE8F;
loc_002DE88F:
    if (Arg4 == 0) goto loc_002DE634;
    if ((*(uint8_t *)(arg1 + 0x8890 + 0x8A)) != ((uint8_t)(v_stack_m208))) goto loc_002DE83B;
    goto loc_002DE634;
loc_002DE8A6:
loc_002DE8B7:
    v_stack_m1D0 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60519)) * 8);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60530)) * 8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60530)) * 8))) goto loc_002DE8B7;
loc_002DE8E9:
    if (((*(uint32_t *)(v_rip + 0xCE81C2)) & (256)) == 0) goto loc_002DEE09;
    Arg1 = 0;
    result = HvlGetReferenceTimeUsingTscPage(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60530)) * 8), *(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60530)) * 8, v_stack_m208);
loc_002DE903:
    v_stack_m208 = result;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60506)) * 8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB60506)) * 8))) goto loc_002DE8E9;
    goto loc_002DE6FE;
loc_002DE91D:
    result = 0;
    v_stack_m200 = 0;
    v_stack_m1F8 = 0;
    if ((*(uint8_t *)(v_stack_m218 + 0x21)) == 0) goto loc_002DEF85;
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_m218 + 0x28), v_stack_m218, v_stack_m1F8, v_stack_m200);
    v_stack_m1E0 = v_stack_m200;
    if (v_stack_m218 != 0) goto loc_002DE989;
    if (v_stack_m1F8 == (*(uint64_t *)(v_stack_m218 + 0x10))) goto loc_002DE991;
    Arg1 = (v_stack_m200) - (*(uint64_t *)(v_stack_m218 + 0x8));
    Arg3 = (v_stack_m1F8) - (*(uint64_t *)(v_stack_m218 + 0x10));
    Arg2 = 0;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x24))) * (Arg1);
    *(uint32_t *)(v_stack_m218 + 0x18) = (uint32_t)(result);
loc_002DE989:
    *(uint64_t *)(v_stack_m218 + 0x8) = v_stack_m200;
    *(uint64_t *)(v_stack_m218 + 0x10) = v_stack_m1F8;
loc_002DE991:
    v_stack_m214 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x18)));
loc_002DE99A:
    if ((*(uint8_t *)(v_stack_m218 + 0x21)) == 0) goto loc_002DEF6D;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x18))))) * (v_stack_m1D0);
    if (Arg1 == NULL) goto loc_002DEE73;
    v_stack_m1D8 = 0;
    v_stack_m1D8 = 0;
    if (0 != 0) goto loc_002DEF29;
    Arg3 = (100) >> (16);
loc_002DE9DA:
    if (local_r12 == 0) goto loc_002DEA16;
    if ((*(uint8_t *)(v_stack_m218 + 0x21)) == 0) goto loc_002DEFB2;
    *(uint32_t *)(local_r12 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x18)));
    *(uint64_t *)(local_r12 + 0x38) = v_stack_m1E0;
    *(uint64_t *)(local_r12 + 0x28) = v_stack_m1F8;
    *(uint64_t *)(local_r12 + 0x48) = Arg3;
    *(uint64_t *)(local_r12 + 0x58) = *(uint64_t *)(arg1 + 0x8890 + 0x40);
    v_stack_m210 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x24)));
loc_002DEA16:
    if ((*(uint8_t *)(arg1 + 0x8890 + 0x88)) != 0) goto loc_002DE7BE;
    goto loc_002DE7BE;
loc_002DEA2C:
    result = 0;
    v_stack_m200 = 0;
    v_stack_m1F8 = 0;
    if ((*(uint8_t *)(v_stack_m218 + 0x21)) == 0) goto loc_002DEF99;
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_m218 + 0x28), v_stack_m218, v_stack_m1F8, v_stack_m200);
    if (v_stack_m218 != 0) goto loc_002DEA93;
    if (v_stack_m1F8 == (*(uint64_t *)(v_stack_m218 + 0x10))) goto loc_002DEA9B;
    Arg1 = (v_stack_m200) - (*(uint64_t *)(v_stack_m218 + 0x8));
    Arg3 = (v_stack_m1F8) - (*(uint64_t *)(v_stack_m218 + 0x10));
    Arg2 = 0;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x24))) * (Arg1);
    *(uint32_t *)(v_stack_m218 + 0x18) = (uint32_t)(result);
loc_002DEA93:
    *(uint64_t *)(v_stack_m218 + 0x10) = v_stack_m1F8;
    *(uint64_t *)(v_stack_m218 + 0x8) = v_stack_m200;
loc_002DEA9B:
    v_stack_m214 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x18)));
loc_002DEAA4:
    if ((*(uint8_t *)(v_stack_m218 + 0x21)) == 0) goto loc_002DEF79;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x18))))) * (v_stack_m1D0);
    if (Arg1 == NULL) goto loc_002DEE7B;
    v_stack_m1D8 = 0;
    v_stack_m1D8 = 0;
    if (0 != 0) goto loc_002DEF4B;
    Arg3 = (100) >> (16);
loc_002DEAE4:
    if (local_r12 == 0) goto loc_002DEB1B;
    if ((*(uint8_t *)(v_stack_m218 + 0x21)) == 0) goto loc_002DEFBC;
    *(uint32_t *)(local_r12 + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x18)));
    *(uint64_t *)(local_r12 + 0x30) = v_stack_m1F8;
    *(uint64_t *)(local_r12 + 0x40) = v_stack_m200;
    *(uint64_t *)(local_r12 + 0x50) = Arg3;
    *(uint64_t *)(local_r12 + 0x60) = *(uint64_t *)(arg1 + 0x8890 + 0x48);
    v_stack_m210 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x24)));
loc_002DEB1B:
    if ((*(uint8_t *)(arg1 + 0x8890 + 0x88)) != 1) goto loc_002DE7CB;
    goto loc_002DE7CB;
loc_002DEB31:
    if ((uint8_t)(v_stack_m218) != 0) goto loc_002DE647;
    if ((uint8_t)(v_stack_m200) == 0) goto loc_002DE647;
    goto loc_002DE837;
loc_002DEB48:
    if ((*(uint32_t *)(v_rip + 0xB28B51)) <= 5) goto loc_002DE7D4;
    Arg4 = 0;
    v_stack_m150 = 4;
    v_stack_m140 = 4;
    v_stack_m130 = 8;
    Arg3 = 0;
    v_stack_m1F0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1C0 + 0x98)));
    v_stack_m158 = v_stack_m1F0;
    v_stack_m1EC = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x24)));
    v_stack_m148 = v_stack_m1EC;
    v_stack_m1B0 = *(uint64_t *)(local_r12 + 0x8);
    v_stack_m138 = v_stack_m1B0;
    v_stack_m1E8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12)));
    v_stack_m128 = v_stack_m1E8;
    v_stack_m217 = (uint8_t)(*(uint8_t *)(local_r12 + 0x5));
    v_stack_m118 = v_stack_m217;
    v_stack_m218 = (uint8_t)(*(uint8_t *)(local_r12 + 0x6));
    v_stack_m108 = v_stack_m218;
    v_stack_m1A8 = *(uint64_t *)(local_r12 + 0x10);
    v_stack_mF8 = v_stack_m1A8;
    v_stack_m1A0 = *(uint64_t *)(local_r12 + 0x18);
    v_stack_mE8 = v_stack_m1A0;
    v_stack_m198 = *(uint64_t *)(local_r12 + 0x68);
    v_stack_mD8 = v_stack_m198;
    v_stack_m190 = *(uint64_t *)(local_r12 + 0x70);
    v_stack_mC8 = v_stack_m190;
    v_stack_m1E4 = (uint32_t)((uint32_t)(v_stack_m210));
    v_stack_mB8 = v_stack_m1E4;
    v_stack_mA8 = local_r12 + 32;
    v_stack_m98 = local_r12 + 40;
    v_stack_m88 = local_r12 + 56;
    v_stack_m78 = local_r12 + 72;
    v_stack_m68 = local_r12 + 88;
    v_stack_m58 = local_r12 + 120;
    v_stack_m220 = v_stack_m178;
    v_stack_m228 = 19;
    v_stack_m120 = 4;
    v_stack_m110 = 1;
    v_stack_m100 = 1;
    v_stack_mF0 = 8;
    v_stack_mE0 = 8;
    v_stack_mD0 = 8;
    v_stack_mC0 = 8;
    v_stack_mB0 = 4;
    v_stack_mA0 = 8;
    v_stack_m90 = 16;
    v_stack_m80 = 16;
    v_stack_m70 = 16;
    v_stack_m60 = 16;
    v_stack_m50 = 8;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 11701030, v_rip - 2710856, Arg3, Arg4);
    goto loc_002DE7D4;
loc_002DED36:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_002DEED8;
loc_002DED4F:
    goto loc_002DE82D;
loc_002DED55:
    Arg2 = (v_rip - 2710856) << (32);
    result = (result) | (Arg2);
    goto loc_002DE6C9;
loc_002DED68:
    Arg1 = 0;
    result = HvlGetReferenceTimeUsingTscPage(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
loc_002DED6F:
    local_r15 = (result) - (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB6005F)) * 8));
loc_002DED9A:
loc_002DED9E:
    *(uint64_t *)(v_stack_m1C8) = result;
    *(uint64_t *)(v_stack_m1C8 + 0x8) = local_r15;
    *(uint64_t *)(v_stack_m1C8 + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB6004A)) * 8);
loc_002DEDA9:
loc_002DEDAB:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m1C8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), result);
    local_rsp = (local_rsp) + (528);
    return result;
loc_002DEDD6:
    *(uint64_t *)(v_stack_p18 + 0x50) = 0;
    *(uint32_t *)(v_stack_p18 + 0x60) = (uint32_t)(v_stack_m1C8);
    *(uint32_t *)(v_stack_p18 + 0x64) = (uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8));
    if ((uint32_t)(result) == 0) goto loc_002DE808;
    Arg2 = 0;
    v_stack_p34 = (uint32_t)((uint32_t)((uint32_t)(result)));
    Arg1 = ((uint32_t)((uint32_t)(result))) * (*(uint64_t *)(v_stack_p18 + 0x50));
    goto loc_002DE808;
loc_002DEE09:
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    goto loc_002DE903;
loc_002DEE1C:
loc_002DEE2D:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FFBA)) * 8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FFBA)) * 8))) goto loc_002DEE2D;
loc_002DEE5A:
    result = HvlGetReferenceTime((uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FFBA)) * 8), *(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FFBA)) * 8, result);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8))) goto loc_002DED9A;
    goto loc_002DEE5A;
loc_002DEE73:
    Arg3 = 0;
    goto loc_002DE9DA;
loc_002DEE7B:
    Arg3 = 0;
    goto loc_002DEAE4;
loc_002DEE83:
    v_stack_p32 = (uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8));
    goto loc_002DE620;
loc_002DEE8F:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8 + 0x50)) == result) goto loc_002DEEB3;
    if ((*(uint32_t *)(arg1 + 0x8648)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8 + 0x60))))) goto loc_002DE88F;
    if ((*(uint32_t *)(arg1 + 0x8644)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8 + 0x64))))) goto loc_002DE88F;
loc_002DEEB3:
    if (0 == 0) goto loc_002DE83B;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8 + 0x68))) goto loc_002DE83B;
    goto loc_002DE88F;
loc_002DEECB:
    if (0 != 0) goto loc_002DEF22;
    goto loc_002DE67F;
loc_002DEED8:
loc_002DEEDF:
    if (0 != 0) goto loc_002DEEDF;
    if (condition_is_above_or_equal) goto loc_002DED4F;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(1)))), 1, result);
    goto loc_002DED4F;
loc_002DEF00:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2EF52))) != 0) goto loc_002DE81D;
    result = KiReleaseSpinLockInstrumented(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8, v_stack_p0, 1, result);
    goto loc_002DE822;
loc_002DEF22:
    result = 0;
    goto loc_002DEDAB;
loc_002DEF29:
    result = (*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8) >> (16);
    Arg3 = (1) * (result);
    result = (result) << (16);
    Arg1 = (*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FF95)) * 8) - (result);
    result = (result) * (Arg1);
    result = (result) >> (16);
    Arg3 = (Arg3) + (result);
    goto loc_002DE9DA;
loc_002DEF4B:
    result = (Arg1) >> (16);
    Arg3 = (Arg3) * (result);
    result = (result) << (16);
    Arg1 = (Arg1) - (result);
    result = (result) * (Arg1);
    result = (result) >> (16);
    Arg3 = (Arg3) + (result);
    goto loc_002DEAE4;
loc_002DEF6D:
    Arg3 = ((uint32_t)((uint32_t)(result))) * (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FFA3)) * 8));
    goto loc_002DE9DA;
loc_002DEF79:
    Arg3 = ((uint32_t)((uint32_t)(result))) * (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8BD0) + (uint32_t)(*(uint32_t *)(v_rip + 0xB5FFA3)) * 8));
    goto loc_002DEAE4;
loc_002DEF85:
    result = guard_dispatch_icall(Arg1, v_stack_p34, Arg3, result);
    goto loc_002DE99A;
loc_002DEF99:
    result = guard_dispatch_icall(Arg1, v_stack_p34, Arg3, (uint32_t)(v_stack_p34));
    goto loc_002DEAA4;
loc_002DEFB2:
    *(uint32_t *)(local_r12 + 0x78) = (uint32_t)((uint32_t)(v_stack_p34));
    goto loc_002DEA16;
loc_002DEFBC:
    *(uint32_t *)(local_r12 + 0x7C) = (uint32_t)((uint32_t)(v_stack_p34));
    goto loc_002DEB1B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18 + rcx*8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R/W` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R/W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R/W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R/W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R/W` |
| `Arg1` | `+ 0x50` | `64` | `W` |
| `Arg1` | `+ 0x58` | `64` | `R/W` |
| `Arg1` | `+ 0x60` | `32` | `R` |
| `Arg1` | `+ 0x60` | `32` | `W` |
| `Arg1` | `+ 0x64` | `32` | `R` |
| `Arg1` | `+ 0x64` | `32` | `W` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `W` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `W` |
| `Arg1` | `+ 0x88` | `8` | `R` |
| `Arg1` | `+ 0x8A` | `8` | `R` |
| `Arg1` | `+ 0x8644` | `32` | `R` |
| `Arg1` | `+ 0x8648` | `32` | `R` |
| `Arg1` | `+ 0x8890` | `64` | `R` |
| `Arg1` | `+ 0x8920` | `32` | `R` |
| `Arg1` | `+ 0x8BD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002DE580&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
