# PpmHeteroUpdateHgsConfiguration

- RVA: `0x003BF344`–`0x003BFD1C` (길이 `2,520` bytes)
- VA: `0x00000001403BF344`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DF04`
- 디코드: `584`개 명령, `2,520/2,520` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **49**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **31**

### Outgoing calls
- `0x003BF392` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF3A3` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF3B6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF3C7` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF3D8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF3E9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF3FA` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF408` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF429` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x003BF44D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003BF48C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF4A8` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF4EC` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003BF543` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF55F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF57B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF591` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF5AD` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BF60B` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x003BF6E5` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x003BF7B2` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x003BF7C0` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x003BF86A` → [PPmHeteroHgsUpdateOrderValue](PPmHeteroHgsUpdateOrderValue_function_003BFD24.md) (function, `0x003BFD24`)
- `0x003BF886` → [PPmHeteroHgsUpdateOrderValue](PPmHeteroHgsUpdateOrderValue_function_003BFD24.md) (function, `0x003BFD24`)
- `0x003BF8AB` → [KiAndAffinityEx](../3C/KiAndAffinityEx_function_003C0680.md) (function, `0x003C0680`)
- `0x003BF8C7` → [KiAndAffinityEx](../3C/KiAndAffinityEx_function_003C0680.md) (function, `0x003C0680`)
- `0x003BF95A` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x003BF9AA` → [KeCheckProcessorAffinityEx](../30/KeCheckProcessorAffinityEx_function_00305150.md) (function, `0x00305150`)
- `0x003BFA59` → [KeIsForceParkingEnabled](../21/KeIsForceParkingEnabled_function_00218F20.md) (function, `0x00218F20`)
- `0x003BFA79` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x003BFA8B` → [RtlCompareMemory](../6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x003BFAA6` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003BFAAD` → [PpmEventHgsHardwareTableResonChanged](../4D/PpmEventHgsHardwareTableResonChanged_function_004D6D5C.md) (function, `0x004D6D5C`)
- `0x003BFADF` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BFB15` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BFB76` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x003BFBCB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BFBDA` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x003BFC0B` → [KiOrAffinityEx](../39/KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x003BFC32` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003BFC6C` → [PpmHeteroHgsGetContainmentType](../4C/PpmHeteroHgsGetContainmentType_function_004C0AE0.md) (function, `0x004C0AE0`)
- `0x003BFC80` → [PpmEventHgsContainmentHwUpdate](../4D/PpmEventHgsContainmentHwUpdate_function_004D5FFC.md) (function, `0x004D5FFC`)
- `0x003BFC96` → [PpmHeteroHgsDetectContainmentPresence](../5D/PpmHeteroHgsDetectContainmentPresence_function_005D8768.md) (function, `0x005D8768`)
- `0x003BFC9B` → [PpmHeteroHgsEvalAndRegisterContainmentGroups](../5D/PpmHeteroHgsEvalAndRegisterContainmentGroups_function_005D8B2C.md) (function, `0x005D8B2C`)
- `0x003BFCBF` → [PpmHeteroHgsUpdateContainmentGlobalHints](../4F/PpmHeteroHgsUpdateContainmentGlobalHints_function_004FCFF8.md) (function, `0x004FCFF8`)
- `0x003BFCC4` → [PpmHeteroHgsCheckContainmentDecision](PpmHeteroHgsCheckContainmentDecision_function_003BEFF8.md) (function, `0x003BEFF8`)
- `0x003BFCCB` → [PpmEventHgsHardwareTable](PpmEventHgsHardwareTable_function_003BF110.md) (function, `0x003BF110`)
- `0x003BFCDE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003BFCF5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopInitializeHeteroProcessors](../../page/A5/PopInitializeHeteroProcessors_function_00A53570.md) at `0x00A53654`

### Static image references
- `0x003BF36A` → RVA `0x00E0A740` (`.data`; read)
- `0x003BF40D` → RVA `0x00FC6A94` (`ALMOSTRO`; read)
- `0x003BF422` → RVA `0x00E0B5A0` (`.data`; read)
- `0x003BF436` → RVA `0x00F0B238` (`.data`; read)
- `0x003BF446` → RVA `0x00F0B210` (`.data`; read)
- `0x003BF460` → RVA `0x00FC6AFC` (`ALMOSTRO`; read)
- `0x003BF477` → RVA `0x00FC6AFC` (`ALMOSTRO`; write)
- `0x003BF494` → RVA `0x00E0B870` (`.data`; write)
- `0x003BF4A1` → RVA `0x00E0B878` (`.data`; read)
- `0x003BF4DC` → RVA `0x00E0B5A8` (`.data`; read)
- `0x003BF515` → RVA `0x00FC6BC8` (`ALMOSTRO`; read)
- `0x003BF5FF` → RVA `0x00F231B8` (`.data`; read)
- `0x003BF610` → RVA `0x00FC6EC0` (`ALMOSTRO`; read)
- `0x003BF622` → RVA `0x00FC6C84` (`ALMOSTRO`; read)
- `0x003BF641` → RVA `0x00FC5003` (`ALMOSTRO`; read)
- `0x003BF656` → RVA `0x00FC6C2C` (`ALMOSTRO`; read)
- `0x003BF65F` → RVA `0x00FC6E10` (`ALMOSTRO`; read)
- `0x003BF6A2` → RVA `0x00FC6AEF` (`ALMOSTRO`; read)
- `0x003BF6C2` → RVA `0x00FC6A96` (`ALMOSTRO`; read)
- `0x003BF6CB` → RVA `0x00FC6D48` (`ALMOSTRO`; read)
- `0x003BF71A` → RVA `0x00F231B0` (`.data`; read)
- `0x003BF9BB` → RVA `0x00FC6AF4` (`ALMOSTRO`; read)
- `0x003BF9C8` → RVA `0x00FC6AEE` (`ALMOSTRO`; read)
- `0x003BF9D5` → RVA `0x00F0B220` (`.data`; read)
- `0x003BF9E5` → RVA `0x00F0B228` (`.data`; read)
- `0x003BF9F2` → RVA `0x00E0B804` (`.data`; read)
- `0x003BFA20` → RVA `0x00F0B240` (`.data`; read)
- `0x003BFA66` → RVA `0x00E0B872` (`.data`; read)
- `0x003BFA72` → RVA `0x00E0B870` (`.data`; read)
- `0x003BFAB2` → RVA `0x00FC501C` (`ALMOSTRO`; read)
- `0x003BFCD0` → RVA `0x00F0B230` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003BF344  48 8B C4                        mov rax, rsp
003BF347  48 89 58 08                     mov qword ptr [rax + 8], rbx
003BF34B  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
003BF34F  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
003BF353  55                              push rbp
003BF354  41 54                           push r12
003BF356  41 55                           push r13
003BF358  41 56                           push r14
003BF35A  41 57                           push r15
003BF35C  48 8D A8 18 F8 FF FF            lea rbp, [rax - 0x7e8]
003BF363  48 81 EC C0 08 00 00            sub rsp, 0x8c0
003BF36A  48 8B 05 CF B3 A4 00            mov rax, qword ptr [rip + 0xa4b3cf]
003BF371  48 33 C4                        xor rax, rsp
003BF374  48 89 85 B0 07 00 00            mov qword ptr [rbp + 0x7b0], rax
003BF37B  BB 08 01 00 00                  mov ebx, 0x108
003BF380  48 8D 8D 80 04 00 00            lea rcx, [rbp + 0x480]
003BF387  33 FF                           xor edi, edi
003BF389  44 8B C3                        mov r8d, ebx
003BF38C  33 D2                           xor edx, edx
003BF38E  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
003BF392  E8 A9 78 30 00                  call 0x1406c6c40
003BF397  44 8B C3                        mov r8d, ebx
003BF39A  48 8D 8D 50 01 00 00            lea rcx, [rbp + 0x150]
003BF3A1  33 D2                           xor edx, edx
003BF3A3  E8 98 78 30 00                  call 0x1406c6c40
003BF3A8  44 8D 73 F8                     lea r14d, [rbx - 8]
003BF3AC  33 D2                           xor edx, edx
003BF3AE  45 8B C6                        mov r8d, r14d
003BF3B1  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
003BF3B6  E8 85 78 30 00                  call 0x1406c6c40
003BF3BB  44 8B C3                        mov r8d, ebx
003BF3BE  48 8D 8D 70 03 00 00            lea rcx, [rbp + 0x370]
003BF3C5  33 D2                           xor edx, edx
003BF3C7  E8 74 78 30 00                  call 0x1406c6c40
003BF3CC  44 8B C3                        mov r8d, ebx
003BF3CF  48 8D 8D 60 02 00 00            lea rcx, [rbp + 0x260]
003BF3D6  33 D2                           xor edx, edx
003BF3D8  E8 63 78 30 00                  call 0x1406c6c40
003BF3DD  45 8B C6                        mov r8d, r14d
003BF3E0  48 8D 8D A8 06 00 00            lea rcx, [rbp + 0x6a8]
003BF3E7  33 D2                           xor edx, edx
003BF3E9  E8 52 78 30 00                  call 0x1406c6c40
003BF3EE  44 8B C3                        mov r8d, ebx
003BF3F1  48 8D 8D 90 05 00 00            lea rcx, [rbp + 0x590]
003BF3F8  33 D2                           xor edx, edx
003BF3FA  E8 41 78 30 00                  call 0x1406c6c40
003BF3FF  44 8B C3                        mov r8d, ebx
003BF402  48 8D 4D 40                     lea rcx, [rbp + 0x40]
003BF406  33 D2                           xor edx, edx
003BF408  E8 33 78 30 00                  call 0x1406c6c40
003BF40D  40 38 3D 80 76 C0 00            cmp byte ptr [rip + 0xc07680], dil
003BF414  44 8A E7                        mov r12b, dil
003BF417  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
003BF41C  0F 84 C6 08 00 00               je 0x1403bfce8
003BF422  48 8D 0D 77 C1 A4 00            lea rcx, [rip + 0xa4c177]
003BF429  E8 52 21 F1 FF                  call 0x1402d1580
003BF42E  85 C0                           test eax, eax
003BF430  0F 85 B2 08 00 00               jne 0x1403bfce8
003BF436  48 8B 05 FB BD B4 00            mov rax, qword ptr [rip + 0xb4bdfb]
003BF43D  48 85 C0                        test rax, rax
003BF440  0F 84 A2 08 00 00               je 0x1403bfce8
003BF446  48 8B 0D C3 BD B4 00            mov rcx, qword ptr [rip + 0xb4bdc3]
003BF44D  E8 7E B6 2F 00                  call 0x1406baad0
003BF452  84 C0                           test al, al
003BF454  0F 84 8E 08 00 00               je 0x1403bfce8
003BF45A  8D 5F 01                        lea ebx, [rdi + 1]
003BF45D  45 33 E4                        xor r12d, r12d
003BF460  44 38 25 95 76 C0 00            cmp byte ptr [rip + 0xc07695], r12b
003BF467  8D 7B 1F                        lea edi, [rbx + 0x1f]
003BF46A  45 0F B6 EC                     movzx r13d, r12b
003BF46E  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
003BF473  44 0F 44 EB                     cmove r13d, ebx
003BF477  88 1D 7F 76 C0 00               mov byte ptr [rip + 0xc0767f], bl
003BF47D  33 D2                           xor edx, edx
003BF47F  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
003BF484  45 8B C6                        mov r8d, r14d
003BF487  66 89 7C 24 32                  mov word ptr [rsp + 0x32], di
003BF48C  E8 AF 77 30 00                  call 0x1406c6c40
003BF491  45 8B C6                        mov r8d, r14d
003BF494  48 C7 05 D1 C3 A4 00 01 00 20 00  mov qword ptr [rip + 0xa4c3d1], 0x200001
003BF49F  33 D2                           xor edx, edx
003BF4A1  48 8D 0D D0 C3 A4 00            lea rcx, [rip + 0xa4c3d0]
003BF4A8  E8 93 77 30 00                  call 0x1406c6c40
003BF4AD  0F B7 4C 24 32                  movzx ecx, word ptr [rsp + 0x32]
003BF4B2  41 0F B7 FC                     movzx edi, r12w
003BF4B6  66 39 0D E3 C0 A4 00            cmp word ptr [rip + 0xa4c0e3], cx
003BF4BD  0F B7 F1                        movzx esi, cx
003BF4C0  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
003BF4C5  66 0F 46 35 D3 C0 A4 00         cmovbe si, word ptr [rip + 0xa4c0d3]
003BF4CD  66 89 74 24 30                  mov word ptr [rsp + 0x30], si
003BF4D2  66 44 3B E6                     cmp r12w, si
003BF4D6  73 26                           jae 0x1403bf4fe
003BF4D8  44 0F B7 C6                     movzx r8d, si
003BF4DC  48 8D 15 C5 C0 A4 00            lea rdx, [rip + 0xa4c0c5]
003BF4E3  49 C1 E0 03                     shl r8, 3
003BF4E7  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
003BF4EC  E8 4F 73 30 00                  call 0x1406c6840
003BF4F1  66 03 FB                        add di, bx
003BF4F4  66 3B FE                        cmp di, si
003BF4F7  72 F8                           jb 0x1403bf4f1
003BF4F9  0F B7 4C 24 32                  movzx ecx, word ptr [rsp + 0x32]
003BF4FE  66 3B F9                        cmp di, cx
003BF501  73 12                           jae 0x1403bf515
003BF503  0F B7 C7                        movzx eax, di
003BF506  66 03 FB                        add di, bx
003BF509  4C 89 64 C4 38                  mov qword ptr [rsp + rax*8 + 0x38], r12
003BF50E  66 3B 7C 24 32                  cmp di, word ptr [rsp + 0x32]
003BF513  72 EE                           jb 0x1403bf503
003BF515  48 8B 05 AC 76 C0 00            mov rax, qword ptr [rip + 0xc076ac]
003BF51C  45 8B FC                        mov r15d, r12d
003BF51F  44 39 60 04                     cmp dword ptr [rax + 4], r12d
003BF523  0F 86 CD 03 00 00               jbe 0x1403bf8f6
003BF529  45 8A EC                        mov r13b, r12b
003BF52C  4D 8B C6                        mov r8, r14
003BF52F  48 C7 85 80 04 00 00 01 00 20 00  mov qword ptr [rbp + 0x480], 0x200001
003BF53A  33 D2                           xor edx, edx
003BF53C  48 8D 8D 88 04 00 00            lea rcx, [rbp + 0x488]
003BF543  E8 F8 76 30 00                  call 0x1406c6c40
003BF548  4D 8B C6                        mov r8, r14
003BF54B  48 C7 85 90 05 00 00 01 00 20 00  mov qword ptr [rbp + 0x590], 0x200001
003BF556  33 D2                           xor edx, edx
003BF558  48 8D 8D 98 05 00 00            lea rcx, [rbp + 0x598]
003BF55F  E8 DC 76 30 00                  call 0x1406c6c40
003BF564  4D 8B C6                        mov r8, r14
003BF567  48 C7 85 50 01 00 00 01 00 20 00  mov qword ptr [rbp + 0x150], 0x200001
003BF572  33 D2                           xor edx, edx
003BF574  48 8D 8D 58 01 00 00            lea rcx, [rbp + 0x158]
003BF57B  E8 C0 76 30 00                  call 0x1406c6c40
003BF580  4D 8B C6                        mov r8, r14
003BF583  48 C7 45 40 01 00 20 00         mov qword ptr [rbp + 0x40], 0x200001
003BF58B  33 D2                           xor edx, edx
003BF58D  48 8D 4D 48                     lea rcx, [rbp + 0x48]
003BF591  E8 AA 76 30 00                  call 0x1406c6c40
003BF596  4D 8B C6                        mov r8, r14
003BF599  48 C7 85 A0 06 00 00 01 00 20 00  mov qword ptr [rbp + 0x6a0], 0x200001
003BF5A4  33 D2                           xor edx, edx
003BF5A6  48 8D 8D A8 06 00 00            lea rcx, [rbp + 0x6a8]
003BF5AD  E8 8E 76 30 00                  call 0x1406c6c40
003BF5B2  45 0F B7 F4                     movzx r14d, r12w
003BF5B6  4C 8B 25 EB BF A4 00            mov r12, qword ptr [rip + 0xa4bfeb]
003BF5BD  0F B7 0D DC BF A4 00            movzx ecx, word ptr [rip + 0xa4bfdc]
003BF5C4  48 8D 15 D5 BF A4 00            lea rdx, [rip + 0xa4bfd5]
003BF5CB  4D 85 E4                        test r12, r12
003BF5CE  75 18                           jne 0x1403bf5e8
003BF5D0  66 44 03 F3                     add r14w, bx
003BF5D4  45 0F B7 F6                     movzx r14d, r14w
003BF5D8  44 3B F1                        cmp r14d, ecx
003BF5DB  0F 83 78 02 00 00               jae 0x1403bf859
003BF5E1  4E 8B 64 F2 08                  mov r12, qword ptr [rdx + r14*8 + 8]
003BF5E6  EB E3                           jmp 0x1403bf5cb
003BF5E8  49 0F BC D4                     bsf rdx, r12
003BF5EC  41 0F B7 CE                     movzx ecx, r14w
003BF5F0  0F B6 C2                        movzx eax, dl
003BF5F3  C1 E1 06                        shl ecx, 6
003BF5F6  49 0F B3 C4                     btr r12, rax
003BF5FA  0F B6 C2                        movzx eax, dl
003BF5FD  03 C8                           add ecx, eax
003BF5FF  48 8B 05 B2 3B B6 00            mov rax, qword ptr [rip + 0xb63bb2]
003BF606  8B 3C 88                        mov edi, dword ptr [rax + rcx*4]
003BF609  8B CF                           mov ecx, edi
003BF60B  E8 C0 8F F1 FF                  call 0x1402d85d0
003BF610  48 8B 15 A9 78 C0 00            mov rdx, qword ptr [rip + 0xc078a9]
003BF617  45 33 DB                        xor r11d, r11d
003BF61A  4C 8B C0                        mov r8, rax
003BF61D  48 85 D2                        test rdx, rdx
003BF620  74 1F                           je 0x1403bf641
003BF622  8B 0D 5C 76 C0 00               mov ecx, dword ptr [rip + 0xc0765c]
003BF628  F6 C1 02                        test cl, 2
003BF62B  74 14                           je 0x1403bf641
003BF62D  8B CF                           mov ecx, edi
003BF62F  0F AF 4A 04                     imul ecx, dword ptr [rdx + 4]
003BF633  41 03 CF                        add ecx, r15d
003BF636  40 8A 74 8A 18                  mov sil, byte ptr [rdx + rcx*4 + 0x18]
003BF63B  8A 54 8A 19                     mov dl, byte ptr [rdx + rcx*4 + 0x19]
003BF63F  EB 61                           jmp 0x1403bf6a2
003BF641  8A 05 BC 59 C0 00               mov al, byte ptr [rip + 0xc059bc]
003BF647  3C 02                           cmp al, 2
003BF649  75 25                           jne 0x1403bf670
003BF64B  41 0F B7 80 4A 8A 00 00         movzx eax, word ptr [r8 + 0x8a4a]
003BF653  41 8B CF                        mov ecx, r15d
003BF656  0F AF 0D CF 75 C0 00            imul ecx, dword ptr [rip + 0xc075cf]
003BF65D  03 C1                           add eax, ecx
003BF65F  48 8B 0D AA 77 C0 00            mov rcx, qword ptr [rip + 0xc077aa]
003BF666  40 8A 74 01 01                  mov sil, byte ptr [rcx + rax + 1]
003BF66B  8A 14 01                        mov dl, byte ptr [rcx + rax]
003BF66E  EB 32                           jmp 0x1403bf6a2
003BF670  3A C3                           cmp al, bl
003BF672  75 29                           jne 0x1403bf69d
003BF674  48 8B 05 95 77 C0 00            mov rax, qword ptr [rip + 0xc07795]
003BF67B  41 8B CF                        mov ecx, r15d
003BF67E  0F AF 0D A7 75 C0 00            imul ecx, dword ptr [rip + 0xc075a7]
003BF685  41 0F B7 90 4A 8A 00 00         movzx edx, word ptr [r8 + 0x8a4a]
003BF68D  C1 E1 02                        shl ecx, 2
003BF690  48 03 D0                        add rdx, rax
003BF693  40 8A 34 0A                     mov sil, byte ptr [rdx + rcx]
003BF697  8A 54 0A 04                     mov dl, byte ptr [rdx + rcx + 4]
003BF69B  EB 05                           jmp 0x1403bf6a2
003BF69D  40 8A F3                        mov sil, bl
003BF6A0  8A D3                           mov dl, bl
003BF6A2  44 38 1D 46 74 C0 00            cmp byte ptr [rip + 0xc07446], r11b
003BF6A9  49 8B 80 50 8A 00 00            mov rax, qword ptr [r8 + 0x8a50]
003BF6B0  41 8B CF                        mov ecx, r15d
003BF6B3  88 54 88 06                     mov byte ptr [rax + rcx*4 + 6], dl
003BF6B7  40 88 74 88 07                  mov byte ptr [rax + rcx*4 + 7], sil
003BF6BC  0F 84 08 01 00 00               je 0x1403bf7ca
003BF6C2  44 38 1D CD 73 C0 00            cmp byte ptr [rip + 0xc073cd], r11b
003BF6C9  74 3E                           je 0x1403bf709
003BF6CB  44 39 1D 76 76 C0 00            cmp dword ptr [rip + 0xc07676], r11d
003BF6D2  74 35                           je 0x1403bf709
003BF6D4  84 D2                           test dl, dl
003BF6D6  48 8D 8D 90 05 00 00            lea rcx, [rbp + 0x590]
003BF6DD  8B D7                           mov edx, edi
003BF6DF  74 04                           je 0x1403bf6e5
003BF6E1  48 8D 4D 40                     lea rcx, [rbp + 0x40]
003BF6E5  E8 06 C0 E9 FF                  call 0x14025b6f0
003BF6EA  8B D7                           mov edx, edi
003BF6EC  40 84 F6                        test sil, sil
003BF6EF  75 0C                           jne 0x1403bf6fd
003BF6F1  48 8D 8D 80 04 00 00            lea rcx, [rbp + 0x480]
003BF6F8  E9 C3 00 00 00                  jmp 0x1403bf7c0
003BF6FD  48 8D 8D 50 01 00 00            lea rcx, [rbp + 0x150]
003BF704  E9 B7 00 00 00                  jmp 0x1403bf7c0
003BF709  84 D2                           test dl, dl
003BF70B  0F 84 98 00 00 00               je 0x1403bf7a9
003BF711  40 84 F6                        test sil, sil
003BF714  0F 84 8F 00 00 00               je 0x1403bf7a9
003BF71A  4C 8B 15 8F 3A B6 00            mov r10, qword ptr [rip + 0xb63a8f]
003BF721  0F B7 85 50 01 00 00            movzx eax, word ptr [rbp + 0x150]
003BF728  45 8B 04 BA                     mov r8d, dword ptr [r10 + rdi*4]
003BF72C  41 8B C8                        mov ecx, r8d
003BF72F  C1 E9 06                        shr ecx, 6
003BF732  41 83 E0 3F                     and r8d, 0x3f
003BF736  3B C1                           cmp eax, ecx
003BF738  77 15                           ja 0x1403bf74f
003BF73A  0F B7 85 52 01 00 00            movzx eax, word ptr [rbp + 0x152]
003BF741  3B C1                           cmp eax, ecx
003BF743  76 23                           jbe 0x1403bf768
003BF745  8D 04 0B                        lea eax, [rbx + rcx]
003BF748  66 89 85 50 01 00 00            mov word ptr [rbp + 0x150], ax
003BF74F  8B D1                           mov edx, ecx
003BF751  48 8B 8C CD 58 01 00 00         mov rcx, qword ptr [rbp + rcx*8 + 0x158]
003BF759  41 8B C0                        mov eax, r8d
003BF75C  48 0F AB C1                     bts rcx, rax
003BF760  48 89 8C D5 58 01 00 00         mov qword ptr [rbp + rdx*8 + 0x158], rcx
003BF768  45 8B 04 BA                     mov r8d, dword ptr [r10 + rdi*4]
003BF76C  41 8B C8                        mov ecx, r8d
003BF76F  0F B7 45 40                     movzx eax, word ptr [rbp + 0x40]
003BF773  41 83 E0 3F                     and r8d, 0x3f
003BF777  C1 E9 06                        shr ecx, 6
003BF77A  3B C1                           cmp eax, ecx
003BF77C  77 13                           ja 0x1403bf791
003BF77E  0F B7 45 42                     movzx eax, word ptr [rbp + 0x42]
003BF782  3B C1                           cmp eax, ecx
003BF784  0F 86 33 FE FF FF               jbe 0x1403bf5bd
003BF78A  8D 04 0B                        lea eax, [rbx + rcx]
003BF78D  66 89 45 40                     mov word ptr [rbp + 0x40], ax
003BF791  8B D1                           mov edx, ecx
003BF793  48 8B 4C CD 48                  mov rcx, qword ptr [rbp + rcx*8 + 0x48]
003BF798  41 8B C0                        mov eax, r8d
003BF79B  48 0F AB C1                     bts rcx, rax
003BF79F  48 89 4C D5 48                  mov qword ptr [rbp + rdx*8 + 0x48], rcx
003BF7A4  E9 14 FE FF FF                  jmp 0x1403bf5bd
003BF7A9  8B D7                           mov edx, edi
003BF7AB  48 8D 8D 80 04 00 00            lea rcx, [rbp + 0x480]
003BF7B2  E8 39 BF E9 FF                  call 0x14025b6f0
003BF7B7  8B D7                           mov edx, edi
003BF7B9  48 8D 8D 90 05 00 00            lea rcx, [rbp + 0x590]
003BF7C0  E8 2B BF E9 FF                  call 0x14025b6f0
003BF7C5  E9 F3 FD FF FF                  jmp 0x1403bf5bd
003BF7CA  4C 8B 15 DF 39 B6 00            mov r10, qword ptr [rip + 0xb639df]
003BF7D1  0F B7 45 40                     movzx eax, word ptr [rbp + 0x40]
003BF7D5  45 8B 04 BA                     mov r8d, dword ptr [r10 + rdi*4]
003BF7D9  41 8B C8                        mov ecx, r8d
003BF7DC  C1 E9 06                        shr ecx, 6
003BF7DF  41 83 E0 3F                     and r8d, 0x3f
003BF7E3  3B C1                           cmp eax, ecx
003BF7E5  77 0F                           ja 0x1403bf7f6
003BF7E7  0F B7 45 42                     movzx eax, word ptr [rbp + 0x42]
003BF7EB  3B C1                           cmp eax, ecx
003BF7ED  76 1A                           jbe 0x1403bf809
003BF7EF  8D 04 0B                        lea eax, [rbx + rcx]
003BF7F2  66 89 45 40                     mov word ptr [rbp + 0x40], ax
003BF7F6  8B D1                           mov edx, ecx
003BF7F8  48 8B 4C CD 48                  mov rcx, qword ptr [rbp + rcx*8 + 0x48]
003BF7FD  41 8B C0                        mov eax, r8d
003BF800  48 0F AB C1                     bts rcx, rax
003BF804  48 89 4C D5 48                  mov qword ptr [rbp + rdx*8 + 0x48], rcx
003BF809  45 8B 04 BA                     mov r8d, dword ptr [r10 + rdi*4]
003BF80D  41 8B C8                        mov ecx, r8d
003BF810  0F B7 85 50 01 00 00            movzx eax, word ptr [rbp + 0x150]
003BF817  41 83 E0 3F                     and r8d, 0x3f
003BF81B  C1 E9 06                        shr ecx, 6
003BF81E  3B C1                           cmp eax, ecx
003BF820  77 19                           ja 0x1403bf83b
003BF822  0F B7 85 52 01 00 00            movzx eax, word ptr [rbp + 0x152]
003BF829  3B C1                           cmp eax, ecx
003BF82B  0F 86 8C FD FF FF               jbe 0x1403bf5bd
003BF831  8D 04 0B                        lea eax, [rbx + rcx]
003BF834  66 89 85 50 01 00 00            mov word ptr [rbp + 0x150], ax
003BF83B  8B D1                           mov edx, ecx
003BF83D  48 8B 8C CD 58 01 00 00         mov rcx, qword ptr [rbp + rcx*8 + 0x158]
003BF845  41 8B C0                        mov eax, r8d
003BF848  48 0F AB C1                     bts rcx, rax
003BF84C  48 89 8C D5 58 01 00 00         mov qword ptr [rbp + rdx*8 + 0x158], rcx
003BF854  E9 64 FD FF FF                  jmp 0x1403bf5bd
003BF859  44 8A CB                        mov r9b, bl
003BF85C  48 8D 95 90 05 00 00            lea rdx, [rbp + 0x590]
003BF863  45 8B C7                        mov r8d, r15d
003BF866  48 8D 4D 40                     lea rcx, [rbp + 0x40]
003BF86A  E8 B5 04 00 00                  call 0x1403bfd24
003BF86F  45 33 C9                        xor r9d, r9d
003BF872  48 8D 95 80 04 00 00            lea rdx, [rbp + 0x480]
003BF879  45 8B C7                        mov r8d, r15d
003BF87C  48 8D 8D 50 01 00 00            lea rcx, [rbp + 0x150]
003BF883  44 0A E8                        or r13b, al
003BF886  E8 99 04 00 00                  call 0x1403bfd24
003BF88B  44 0F B7 8D A2 06 00 00         movzx r9d, word ptr [rbp + 0x6a2]
003BF893  4C 8D 85 A0 06 00 00            lea r8, [rbp + 0x6a0]
003BF89A  48 8D 95 80 04 00 00            lea rdx, [rbp + 0x480]
003BF8A1  44 0A E8                        or r13b, al
003BF8A4  48 8D 8D 90 05 00 00            lea rcx, [rbp + 0x590]
003BF8AB  E8 D0 0D 00 00                  call 0x1403c0680
003BF8B0  44 0F B7 4C 24 32               movzx r9d, word ptr [rsp + 0x32]
003BF8B6  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
003BF8BB  48 8D 95 A0 06 00 00            lea rdx, [rbp + 0x6a0]
003BF8C2  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
003BF8C7  E8 B4 0D 00 00                  call 0x1403c0680
003BF8CC  48 8B 05 F5 72 C0 00            mov rax, qword ptr [rip + 0xc072f5]
003BF8D3  44 03 FB                        add r15d, ebx
003BF8D6  41 BC 00 00 00 00               mov r12d, 0
003BF8DC  41 BE 00 01 00 00               mov r14d, 0x100
003BF8E2  44 3B 78 04                     cmp r15d, dword ptr [rax + 4]
003BF8E6  0F 82 40 FC FF FF               jb 0x1403bf52c
003BF8EC  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
003BF8F1  44 8B 6C 24 24                  mov r13d, dword ptr [rsp + 0x24]
003BF8F6  44 38 25 F2 71 C0 00            cmp byte ptr [rip + 0xc071f2], r12b
003BF8FD  0F 84 B8 00 00 00               je 0x1403bf9bb
003BF903  48 8B 35 9E BC A4 00            mov rsi, qword ptr [rip + 0xa4bc9e]
003BF90A  41 0F B7 FC                     movzx edi, r12w
003BF90E  0F B7 0D 8B BC A4 00            movzx ecx, word ptr [rip + 0xa4bc8b]
003BF915  48 8D 15 84 BC A4 00            lea rdx, [rip + 0xa4bc84]
003BF91C  48 85 F6                        test rsi, rsi
003BF91F  75 15                           jne 0x1403bf936
003BF921  66 03 FB                        add di, bx
003BF924  0F B7 FF                        movzx edi, di
003BF927  3B F9                           cmp edi, ecx
003BF929  0F 83 8C 00 00 00               jae 0x1403bf9bb
003BF92F  48 8B 74 FA 08                  mov rsi, qword ptr [rdx + rdi*8 + 8]
003BF934  EB E6                           jmp 0x1403bf91c
003BF936  48 0F BC D6                     bsf rdx, rsi
003BF93A  0F B7 CF                        movzx ecx, di
003BF93D  0F B6 C2                        movzx eax, dl
003BF940  C1 E1 06                        shl ecx, 6
003BF943  48 0F B3 C6                     btr rsi, rax
003BF947  0F B6 C2                        movzx eax, dl
003BF94A  03 C8                           add ecx, eax
003BF94C  48 8B 05 65 38 B6 00            mov rax, qword ptr [rip + 0xb63865]
003BF953  44 8B 3C 88                     mov r15d, dword ptr [rax + rcx*4]
003BF957  41 8B CF                        mov ecx, r15d
003BF95A  E8 71 8C F1 FF                  call 0x1402d85d0
003BF95F  48 8B 0D 4A 38 B6 00            mov rcx, qword ptr [rip + 0xb6384a]
003BF966  4C 8B F0                        mov r14, rax
003BF969  46 8B 04 B9                     mov r8d, dword ptr [rcx + r15*4]
003BF96D  41 8B D0                        mov edx, r8d
003BF970  0F B7 4C 24 30                  movzx ecx, word ptr [rsp + 0x30]
003BF975  C1 EA 06                        shr edx, 6
003BF978  3B D1                           cmp edx, ecx
003BF97A  72 05                           jb 0x1403bf981
003BF97C  41 8A D4                        mov dl, r12b
003BF97F  EB 11                           jmp 0x1403bf992
003BF981  48 8B 54 D4 38                  mov rdx, qword ptr [rsp + rdx*8 + 0x38]
003BF986  41 83 E0 3F                     and r8d, 0x3f
003BF98A  41 8A C8                        mov cl, r8b
003BF98D  48 D3 EA                        shr rdx, cl
003BF990  22 D3                           and dl, bl
003BF992  38 90 4C 8A 00 00               cmp byte ptr [rax + 0x8a4c], dl
003BF998  0F 84 70 FF FF FF               je 0x1403bf90e
003BF99E  41 8B D7                        mov edx, r15d
003BF9A1  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
003BF9A5  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
003BF9AA  E8 A1 57 F4 FF                  call 0x140305150
003BF9AF  41 88 86 4C 8A 00 00            mov byte ptr [r14 + 0x8a4c], al
003BF9B6  E9 53 FF FF FF                  jmp 0x1403bf90e
003BF9BB  44 38 25 32 71 C0 00            cmp byte ptr [rip + 0xc07132], r12b
003BF9C2  0F 84 EA 00 00 00               je 0x1403bfab2
003BF9C8  44 38 25 1F 71 C0 00            cmp byte ptr [rip + 0xc0711f], r12b
003BF9CF  0F 84 DD 00 00 00               je 0x1403bfab2
003BF9D5  48 8B 3D 44 B8 B4 00            mov rdi, qword ptr [rip + 0xb4b844]
003BF9DC  48 85 FF                        test rdi, rdi
003BF9DF  0F 84 CD 00 00 00               je 0x1403bfab2
003BF9E5  4C 39 25 3C B8 B4 00            cmp qword ptr [rip + 0xb4b83c], r12
003BF9EC  0F 84 C0 00 00 00               je 0x1403bfab2
003BF9F2  8B 05 0C BE A4 00               mov eax, dword ptr [rip + 0xa4be0c]
003BF9F8  45 8B C4                        mov r8d, r12d
003BF9FB  45 8B CC                        mov r9d, r12d
003BF9FE  8D 34 00                        lea esi, [rax + rax]
003BFA01  85 C0                           test eax, eax
003BFA03  74 4E                           je 0x1403bfa53
003BFA05  48 8B 0D 04 74 C0 00            mov rcx, qword ptr [rip + 0xc07404]
003BFA0C  41 8B C1                        mov eax, r9d
003BFA0F  0F AF 05 16 72 C0 00            imul eax, dword ptr [rip + 0xc07216]
003BFA16  48 8B 3D 03 B8 B4 00            mov rdi, qword ptr [rip + 0xb4b803]
003BFA1D  41 8B D1                        mov edx, r9d
003BFA20  03 05 1A B8 B4 00               add eax, dword ptr [rip + 0xb4b81a]
003BFA26  48 03 C8                        add rcx, rax
003BFA29  8A 01                           mov al, byte ptr [rcx]
003BFA2B  88 04 57                        mov byte ptr [rdi + rdx*2], al
003BFA2E  8A 49 01                        mov cl, byte ptr [rcx + 1]
003BFA31  88 4C 57 01                     mov byte ptr [rdi + rdx*2 + 1], cl
003BFA35  22 C8                           and cl, al
003BFA37  F6 C1 02                        test cl, 2
003BFA3A  41 8D 40 01                     lea eax, [r8 + 1]
003BFA3E  41 0F 44 C0                     cmove eax, r8d
003BFA42  44 03 CB                        add r9d, ebx
003BFA45  44 8B C0                        mov r8d, eax
003BFA48  8B 05 B6 BD A4 00               mov eax, dword ptr [rip + 0xa4bdb6]
003BFA4E  44 3B C8                        cmp r9d, eax
003BFA51  72 B2                           jb 0x1403bfa05
003BFA53  44 3B C0                        cmp r8d, eax
003BFA56  0F 94 C1                        sete cl
003BFA59  E8 C2 94 E5 FF                  call 0x140218f20
003BFA5E  84 C0                           test al, al
003BFA60  74 1C                           je 0x1403bfa7e
003BFA62  84 C9                           test cl, cl
003BFA64  74 18                           je 0x1403bfa7e
003BFA66  0F B7 15 05 BE A4 00            movzx edx, word ptr [rip + 0xa4be05]
003BFA6D  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
003BFA72  48 8D 0D F7 BD A4 00            lea rcx, [rip + 0xa4bdf7]
003BFA79  E8 E2 ED F0 FF                  call 0x1402ce860
003BFA7E  48 8B 15 A3 B7 B4 00            mov rdx, qword ptr [rip + 0xb4b7a3]
003BFA85  4C 8B C6                        mov r8, rsi
003BFA88  48 8B CF                        mov rcx, rdi
003BFA8B  E8 E0 AB 2F 00                  call 0x1406ba670
003BFA90  48 3B C6                        cmp rax, rsi
003BFA93  74 1D                           je 0x1403bfab2
003BFA95  48 8B 15 84 B7 B4 00            mov rdx, qword ptr [rip + 0xb4b784]
003BFA9C  4C 8B C6                        mov r8, rsi
003BFA9F  48 8B 0D 82 B7 B4 00            mov rcx, qword ptr [rip + 0xb4b782]
003BFAA6  E8 95 6D 30 00                  call 0x1406c6840
003BFAAB  33 C9                           xor ecx, ecx
003BFAAD  E8 AA 72 11 00                  call 0x1404d6d5c
003BFAB2  8B 05 64 55 C0 00               mov eax, dword ptr [rip + 0xc05564]
003BFAB8  A8 04                           test al, 4
003BFABA  75 09                           jne 0x1403bfac5
003BFABC  45 84 ED                        test r13b, r13b
003BFABF  0F 84 04 02 00 00               je 0x1403bfcc9
003BFAC5  33 D2                           xor edx, edx
003BFAC7  48 C7 85 60 02 00 00 01 00 20 00  mov qword ptr [rbp + 0x260], 0x200001
003BFAD2  41 B8 00 01 00 00               mov r8d, 0x100
003BFAD8  48 8D 8D 68 02 00 00            lea rcx, [rbp + 0x268]
003BFADF  E8 5C 71 30 00                  call 0x1406c6c40
003BFAE4  45 8B F4                        mov r14d, r12d
003BFAE7  48 8B 05 DA 70 C0 00            mov rax, qword ptr [rip + 0xc070da]
003BFAEE  44 3B 70 04                     cmp r14d, dword ptr [rax + 4]
003BFAF2  0F 83 3F 01 00 00               jae 0x1403bfc37
003BFAF8  83 CE FF                        or esi, 0xffffffff
003BFAFB  48 C7 85 70 03 00 00 01 00 20 00  mov qword ptr [rbp + 0x370], 0x200001
003BFB06  33 D2                           xor edx, edx
003BFB08  48 8D 8D 78 03 00 00            lea rcx, [rbp + 0x378]
003BFB0F  41 B8 00 01 00 00               mov r8d, 0x100
003BFB15  E8 26 71 30 00                  call 0x1406c6c40
003BFB1A  4C 8B 3D 87 BA A4 00            mov r15, qword ptr [rip + 0xa4ba87]
003BFB21  41 0F B7 FC                     movzx edi, r12w
003BFB25  EB 03                           jmp 0x1403bfb2a
003BFB27  45 33 E4                        xor r12d, r12d
003BFB2A  0F B7 0D 6F BA A4 00            movzx ecx, word ptr [rip + 0xa4ba6f]
003BFB31  48 8D 15 68 BA A4 00            lea rdx, [rip + 0xa4ba68]
003BFB38  4D 85 FF                        test r15, r15
003BFB3B  75 15                           jne 0x1403bfb52
003BFB3D  66 03 FB                        add di, bx
003BFB40  0F B7 FF                        movzx edi, di
003BFB43  3B F9                           cmp edi, ecx
003BFB45  0F 83 99 00 00 00               jae 0x1403bfbe4
003BFB4B  4C 8B 7C FA 08                  mov r15, qword ptr [rdx + rdi*8 + 8]
003BFB50  EB E6                           jmp 0x1403bfb38
003BFB52  49 0F BC D7                     bsf rdx, r15
003BFB56  0F B7 CF                        movzx ecx, di
003BFB59  0F B6 C2                        movzx eax, dl
003BFB5C  C1 E1 06                        shl ecx, 6
003BFB5F  49 0F B3 C7                     btr r15, rax
003BFB63  0F B6 C2                        movzx eax, dl
003BFB66  03 C8                           add ecx, eax
003BFB68  48 8B 05 49 36 B6 00            mov rax, qword ptr [rip + 0xb63649]
003BFB6F  44 8B 24 88                     mov r12d, dword ptr [rax + rcx*4]
003BFB73  41 8B CC                        mov ecx, r12d
003BFB76  E8 55 8A F1 FF                  call 0x1402d85d0
003BFB7B  0F B7 88 4A 8A 00 00            movzx ecx, word ptr [rax + 0x8a4a]
003BFB82  41 8B C6                        mov eax, r14d
003BFB85  0F AF 05 A0 70 C0 00            imul eax, dword ptr [rip + 0xc070a0]
003BFB8C  03 C1                           add eax, ecx
003BFB8E  48 8B 0D 7B 72 C0 00            mov rcx, qword ptr [rip + 0xc0727b]
003BFB95  0F B6 44 01 01                  movzx eax, byte ptr [rcx + rax + 1]
003BFB9A  84 C0                           test al, al
003BFB9C  74 89                           je 0x1403bfb27
003BFB9E  83 FE FF                        cmp esi, -1
003BFBA1  74 0C                           je 0x1403bfbaf
003BFBA3  3B C6                           cmp eax, esi
003BFBA5  77 08                           ja 0x1403bfbaf
003BFBA7  0F 85 7A FF FF FF               jne 0x1403bfb27
003BFBAD  EB 21                           jmp 0x1403bfbd0
003BFBAF  33 D2                           xor edx, edx
003BFBB1  48 C7 85 70 03 00 00 01 00 20 00  mov qword ptr [rbp + 0x370], 0x200001
003BFBBC  41 B8 00 01 00 00               mov r8d, 0x100
003BFBC2  48 8D 8D 78 03 00 00            lea rcx, [rbp + 0x378]
003BFBC9  8B F0                           mov esi, eax
003BFBCB  E8 70 70 30 00                  call 0x1406c6c40
003BFBD0  41 8B D4                        mov edx, r12d
003BFBD3  48 8D 8D 70 03 00 00            lea rcx, [rbp + 0x370]
003BFBDA  E8 11 BB E9 FF                  call 0x14025b6f0
003BFBDF  E9 43 FF FF FF                  jmp 0x1403bfb27
003BFBE4  44 8B 6C 24 24                  mov r13d, dword ptr [rsp + 0x24]
003BFBE9  83 FE FF                        cmp esi, -1
003BFBEC  74 2A                           je 0x1403bfc18
003BFBEE  44 0F B7 8D 62 02 00 00         movzx r9d, word ptr [rbp + 0x262]
003BFBF6  4C 8D 85 60 02 00 00            lea r8, [rbp + 0x260]
003BFBFD  48 8D 95 70 03 00 00            lea rdx, [rbp + 0x370]
003BFC04  48 8D 8D 60 02 00 00            lea rcx, [rbp + 0x260]
003BFC0B  E8 3C AC FD FF                  call 0x14039a84c
003BFC10  44 03 F3                        add r14d, ebx
003BFC13  E9 CF FE FF FF                  jmp 0x1403bfae7
003BFC18  33 D2                           xor edx, edx
003BFC1A  48 C7 85 60 02 00 00 01 00 20 00  mov qword ptr [rbp + 0x260], 0x200001
003BFC25  41 B8 00 01 00 00               mov r8d, 0x100
003BFC2B  48 8D 8D 68 02 00 00            lea rcx, [rbp + 0x268]
003BFC32  E8 09 70 30 00                  call 0x1406c6c40
003BFC37  41 0F B7 CC                     movzx ecx, r12w
003BFC3B  66 3B 8D 60 02 00 00            cmp cx, word ptr [rbp + 0x260]
003BFC42  73 5C                           jae 0x1403bfca0
003BFC44  0F B7 C1                        movzx eax, cx
003BFC47  4C 39 A4 C5 68 02 00 00         cmp qword ptr [rbp + rax*8 + 0x268], r12
003BFC4F  75 05                           jne 0x1403bfc56
003BFC51  66 03 CB                        add cx, bx
003BFC54  EB E5                           jmp 0x1403bfc3b
003BFC56  8B 05 C0 53 C0 00               mov eax, dword ptr [rip + 0xc053c0]
003BFC5C  A8 04                           test al, 4
003BFC5E  74 27                           je 0x1403bfc87
003BFC60  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
003BFC65  48 8D 8D 60 02 00 00            lea rcx, [rbp + 0x260]
003BFC6C  E8 6F 0E 10 00                  call 0x1404c0ae0
003BFC71  45 33 C0                        xor r8d, r8d
003BFC74  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
003BFC79  48 8D 8D 60 02 00 00            lea rcx, [rbp + 0x260]
003BFC80  E8 77 63 11 00                  call 0x1404d5ffc
003BFC85  EB 19                           jmp 0x1403bfca0
003BFC87  45 84 ED                        test r13b, r13b
003BFC8A  74 14                           je 0x1403bfca0
003BFC8C  41 8A D5                        mov dl, r13b
003BFC8F  48 8D 8D 60 02 00 00            lea rcx, [rbp + 0x260]
003BFC96  E8 CD 8A 21 00                  call 0x1405d8768
003BFC9B  E8 8C 8E 21 00                  call 0x1405d8b2c
003BFCA0  41 0F B7 CC                     movzx ecx, r12w
003BFCA4  66 3B 4C 24 30                  cmp cx, word ptr [rsp + 0x30]
003BFCA9  73 0F                           jae 0x1403bfcba
003BFCAB  0F B7 C1                        movzx eax, cx
003BFCAE  4C 39 64 C4 38                  cmp qword ptr [rsp + rax*8 + 0x38], r12
003BFCB3  75 08                           jne 0x1403bfcbd
003BFCB5  66 03 CB                        add cx, bx
003BFCB8  EB EA                           jmp 0x1403bfca4
003BFCBA  41 8A DC                        mov bl, r12b
003BFCBD  8A CB                           mov cl, bl
003BFCBF  E8 34 D3 13 00                  call 0x1404fcff8
003BFCC4  E8 2F F3 FF FF                  call 0x1403beff8
003BFCC9  33 C9                           xor ecx, ecx
003BFCCB  E8 40 F4 FF FF                  call 0x1403bf110
003BFCD0  48 8B 05 59 B5 B4 00            mov rax, qword ptr [rip + 0xb4b559]
003BFCD7  48 8B 0D 32 B5 B4 00            mov rcx, qword ptr [rip + 0xb4b532]
003BFCDE  E8 ED AD 2F 00                  call 0x1406baad0
003BFCE3  44 8A 64 24 20                  mov r12b, byte ptr [rsp + 0x20]
003BFCE8  41 8A C4                        mov al, r12b
003BFCEB  48 8B 8D B0 07 00 00            mov rcx, qword ptr [rbp + 0x7b0]
003BFCF2  48 33 CC                        xor rcx, rsp
003BFCF5  E8 46 C9 2E 00                  call 0x1406ac640
003BFCFA  4C 8D 9C 24 C0 08 00 00         lea r11, [rsp + 0x8c0]
003BFD02  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
003BFD06  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
003BFD0A  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
003BFD0E  49 8B E3                        mov rsp, r11
003BFD11  41 5F                           pop r15
003BFD13  41 5E                           pop r14
003BFD15  41 5D                           pop r13
003BFD17  41 5C                           pop r12
003BFD19  5D                              pop rbp
003BFD1A  C3                              ret
003BFD1B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmHeteroUpdateHgsConfiguration(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m8B0;
    unsigned int v_stack_m8B4;
    unsigned __int16 v_stack_m8B6;
    unsigned __int16 v_stack_m8B8;
    unsigned int v_stack_m8C0;
    unsigned int v_stack_m8C4;
    unsigned __int8 v_stack_m8C8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (0x8C0ULL);
    result = (*(unsigned __int64 *)(v_rip + 10793935)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 2024 + 1968) = result;
    v_rdi = 0;
    a2 = 0;
    v_stack_m8C0 = 0;
    result = memset(v_rsp - 2024 + 1152, a2, 264, a4);
    a2 = 0;
    result = memset(v_rsp - 2024 + 336, a2, 264, a4);
    a2 = 0;
    result = memset(v_stack_m8B0, a2, (unsigned int)((unsigned int)(264 - 8)), a4);
    a2 = 0;
    result = memset(v_rsp - 2024 + 880, a2, 264, a4);
    a2 = 0;
    result = memset(v_rsp - 2024 + 608, a2, 264, a4);
    a2 = 0;
    result = memset(v_rsp - 2024 + 1704, a2, (unsigned int)((unsigned int)(264 - 8)), a4);
    a2 = 0;
    result = memset(v_rsp - 2024 + 1424, a2, 264, a4);
    a2 = 0;
    result = memset(v_rsp - 2024 + 64, a2, 264, a4);
    v_stack_m8C8 = 0;
    if ((*(unsigned __int8 *)(v_rip + 12613248)) == 0) goto loc_003BFCE8;
    result = KeIsEmptyAffinityEx(v_rip + 10797431, a2, 264, a4);
    if ((unsigned int)(result) != 0) goto loc_003BFCE8;
    if (*(unsigned __int64 *)(v_rip + 11845115) == 0) goto loc_003BFCE8;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 11845059), a2, 264, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003BFCE8;
    v_r12 = 0;
    v_r13 = 0;
    if ((*(unsigned __int8 *)(v_rip + 12613269)) == 0) { v_r13 = (unsigned int)(v_rdi + 1); }
    *(unsigned __int8 *)(v_rip + 12613247) = (unsigned __int8)(v_rdi + 1);
    a2 = 0;
    v_stack_m8C4 = (unsigned int)(v_r13);
    v_stack_m8B6 = (unsigned __int16)(v_rdi + 1 + 31);
    result = memset(v_stack_m8B0, a2, (unsigned int)((unsigned int)(264 - 8)), a4);
    *(unsigned __int64 *)(v_rip + 10798033) = 0x200001ULL;
    a2 = 0;
    result = memset(v_rip + 10798032, a2, (unsigned int)((unsigned int)(264 - 8)), a4);
    v_stack_m8B4 = 0;
    v_rsi = (unsigned __int16)(v_stack_m8B6);
    if ((*(unsigned __int16 *)(v_rip + 10797283)) <= ((unsigned __int16)(v_stack_m8B6))) { v_rsi = *(unsigned __int16 *)(v_rip + 10797267); }
    v_stack_m8B8 = (unsigned __int16)(v_rsi);
    if (0 >= ((unsigned __int16)(v_rsi))) goto loc_003BF4FE;
    a3 = ((unsigned __int16)(v_rsi)) << (3);
    result = memcpy(v_stack_m8B0, v_rip + 10797253, a3, a4);
loc_003BF4F1:
    v_rdi = (unsigned __int16)((0) + ((unsigned __int16)(v_rdi + 1)));
    if (((unsigned __int16)(v_rdi)) < ((unsigned __int16)(v_rsi))) goto loc_003BF4F1;
loc_003BF4FE:
    if (((unsigned __int16)(v_rdi)) >= ((unsigned __int16)(v_stack_m8B6))) goto loc_003BF515;
loc_003BF503:
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)(v_rdi + 1)));
    *(unsigned __int64 *)(v_rsp + (unsigned __int16)(v_rdi) * 8 + 56) = 0;
    if (((unsigned __int16)(v_rdi)) < v_stack_m8B6) goto loc_003BF503;
loc_003BF515:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12613292) + 4)) <= 0) goto loc_003BF8F6;
loc_003BF52C:
    *(unsigned __int64 *)(v_rsp - 2024 + 1152) = 0x200001ULL;
    a2 = 0;
    result = memset(v_rsp - 2024 + 1160, a2, 264 - 8, a4);
    *(unsigned __int64 *)(v_rsp - 2024 + 1424) = 0x200001ULL;
    a2 = 0;
    result = memset(v_rsp - 2024 + 1432, a2, 264 - 8, a4);
    *(unsigned __int64 *)(v_rsp - 2024 + 336) = 0x200001ULL;
    a2 = 0;
    result = memset(v_rsp - 2024 + 344, a2, 264 - 8, a4);
    *(unsigned __int64 *)(v_rsp - 2024 + 64) = 0x200001ULL;
    a2 = 0;
    result = memset(v_rsp - 2024 + 72, a2, 264 - 8, a4);
    *(unsigned __int64 *)(v_rsp - 2024 + 1696) = 0x200001ULL;
    a2 = 0;
    result = memset(v_rsp - 2024 + 1704, a2, 264 - 8, a4);
loc_003BF5BD:
loc_003BF5CB:
    if (*(unsigned __int64 *)(v_rip + 10797035) != 0) goto loc_003BF5E8;
    v_r14 = (unsigned __int16)((0) + ((unsigned __int16)(v_rdi + 1)));
    if (((unsigned int)((unsigned __int16)(v_r14))) >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 10797020)))) goto loc_003BF859;
    goto loc_003BF5CB;
loc_003BF5E8:
    a1 = (unsigned int)(((unsigned __int16)((unsigned __int16)(v_r14))) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)(v_rip + 10797013))));
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)))), v_rip + 10797013, 264 - 8, a4);
    v_r11 = 0;
    if (*(unsigned __int64 *)(v_rip + 12613801) == 0) goto loc_003BF641;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12613212)))) & (2)) == 0) goto loc_003BF641;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4))))) * (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12613801) + 4)));
    a1 = (unsigned int)((a1) + (0));
    goto loc_003BF6A2;
loc_003BF641:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 12605884))) != 2) goto loc_003BF670;
    a1 = (unsigned int)((0) * (*(unsigned int *)(v_rip + 12613071)));
    result = (unsigned int)((*(unsigned __int16 *)(result + 35402)) + ((unsigned int)(a1)));
    goto loc_003BF6A2;
loc_003BF670:
    if (((unsigned __int8)(result)) != ((unsigned __int8)(v_rdi + 1))) goto loc_003BF69D;
    a1 = (unsigned int)((0) * (*(unsigned int *)(v_rip + 12613031)));
    a1 = (unsigned int)((a1) << (2));
    a2 = (*(unsigned __int16 *)(result + 35402)) + (*(unsigned __int64 *)(v_rip + 12613525));
    goto loc_003BF6A2;
loc_003BF69D:
loc_003BF6A2:
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + 0 * 4 + 6) = (unsigned __int8)((unsigned __int8)(v_rdi + 1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + 0 * 4 + 7) = (unsigned __int8)((unsigned __int8)(v_rdi + 1));
    if ((*(unsigned __int8 *)(v_rip + 12612678)) == 0) goto loc_003BF7CA;
    if ((*(unsigned __int8 *)(v_rip + 12612557)) == 0) goto loc_003BF709;
    if ((*(unsigned int *)(v_rip + 12613238)) == 0) goto loc_003BF709;
    if ((unsigned __int8)((unsigned __int8)(v_rdi + 1)) != 0) {
        a1 = v_rsp - 2024 + 64;
    }
    result = KeAddProcessorAffinityEx(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)))), result, a4);
    if ((unsigned __int8)((unsigned __int8)(v_rdi + 1)) != 0) goto loc_003BF6FD;
    goto loc_003BF7C0;
loc_003BF6FD:
    goto loc_003BF7C0;
loc_003BF709:
    if ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4))))) == 0) goto loc_003BF7A9;
    if ((unsigned __int8)((unsigned __int8)(v_rdi + 1)) == 0) goto loc_003BF7A9;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942543) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)) * 4))))) >> (6));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942543) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)) * 4))) & (63));
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 2024 + 336))) > ((unsigned int)(a1))) goto loc_003BF74F;
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 2024 + 338))) <= ((unsigned int)(a1))) goto loc_003BF768;
    *(unsigned __int16 *)(v_rsp - 2024 + 336) = (unsigned __int16)(v_rdi + 1 + a1 * 1);
loc_003BF74F:
    *(unsigned __int64 *)(v_rsp - 2024 + (unsigned int)((unsigned int)(a1)) * 8 + 344) = *(unsigned __int64 *)(v_rsp - 2024 + a1 * 8 + 344);
loc_003BF768:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942543) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)) * 4))) & (63));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942543) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)) * 4))))) >> (6));
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 2024 + 64))) > ((unsigned int)(a1))) goto loc_003BF791;
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 2024 + 66))) <= ((unsigned int)(a1))) goto loc_003BF5BD;
    *(unsigned __int16 *)(v_rsp - 2024 + 64) = (unsigned __int16)(v_rdi + 1 + a1 * 1);
loc_003BF791:
    *(unsigned __int64 *)(v_rsp - 2024 + (unsigned int)((unsigned int)(a1)) * 8 + 72) = *(unsigned __int64 *)(v_rsp - 2024 + a1 * 8 + 72);
    goto loc_003BF5BD;
loc_003BF7A9:
    result = KeAddProcessorAffinityEx(v_rsp - 2024 + 1152, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)))), a3, a4);
loc_003BF7C0:
    result = KeAddProcessorAffinityEx(v_rsp - 2024 + 1424, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)))), a3, a4);
    goto loc_003BF5BD;
loc_003BF7CA:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942367) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)) * 4))))) >> (6));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942367) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)) * 4))) & (63));
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 2024 + 64))) > ((unsigned int)(a1))) goto loc_003BF7F6;
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 2024 + 66))) <= ((unsigned int)(a1))) goto loc_003BF809;
    *(unsigned __int16 *)(v_rsp - 2024 + 64) = (unsigned __int16)(v_rdi + 1 + a1 * 1);
loc_003BF7F6:
    *(unsigned __int64 *)(v_rsp - 2024 + (unsigned int)((unsigned int)(a1)) * 8 + 72) = *(unsigned __int64 *)(v_rsp - 2024 + a1 * 8 + 72);
loc_003BF809:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942367) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)) * 4))) & (63));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942367) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11942834) + a1 * 4)) * 4))))) >> (6));
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 2024 + 336))) > ((unsigned int)(a1))) goto loc_003BF83B;
    if (((unsigned int)(*(unsigned __int16 *)(v_rsp - 2024 + 338))) <= ((unsigned int)(a1))) goto loc_003BF5BD;
    *(unsigned __int16 *)(v_rsp - 2024 + 336) = (unsigned __int16)(v_rdi + 1 + a1 * 1);
loc_003BF83B:
    *(unsigned __int64 *)(v_rsp - 2024 + (unsigned int)((unsigned int)(a1)) * 8 + 344) = *(unsigned __int64 *)(v_rsp - 2024 + a1 * 8 + 344);
    goto loc_003BF5BD;
loc_003BF859:
    result = PPmHeteroHgsUpdateOrderValue(v_rsp - 2024 + 64, v_rsp - 2024 + 1424, 0, (unsigned __int8)(v_rdi + 1));
    a4 = 0;
    v_r13 = (unsigned __int8)((0) | ((unsigned __int8)(result)));
    result = PPmHeteroHgsUpdateOrderValue(v_rsp - 2024 + 336, v_rsp - 2024 + 1152, 0, a4);
    v_r13 = (unsigned __int8)((v_r13) | ((unsigned __int8)(result)));
    result = KiAndAffinityEx(v_rsp - 2024 + 1424, v_rsp - 2024 + 1152, v_rsp - 2024 + 1696, *(unsigned __int16 *)(v_rsp - 2024 + 1698));
    result = KiAndAffinityEx(v_stack_m8B8, v_rsp - 2024 + 1696, v_stack_m8B8, v_stack_m8B6);
    v_r15 = (unsigned int)((0) + ((unsigned int)(v_rdi + 1)));
    if (((unsigned int)(v_r15)) < (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12612341) + 4))) goto loc_003BF52C;
    v_stack_m8C8 = (unsigned __int8)(v_r13);
loc_003BF8F6:
    if ((*(unsigned __int8 *)(v_rip + 12612082)) == 0) goto loc_003BF9BB;
loc_003BF90E:
loc_003BF91C:
    if (*(unsigned __int64 *)(v_rip + 10796190) != 0) goto loc_003BF936;
    v_rdi = (unsigned __int16)((0) + ((unsigned __int16)(v_rdi + 1)));
    if (((unsigned int)((unsigned __int16)(v_rdi))) >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 10796171)))) goto loc_003BF9BB;
    goto loc_003BF91C;
loc_003BF936:
    a1 = (unsigned int)(((unsigned __int16)((unsigned __int16)(v_rdi))) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)(v_rip + 10796164))));
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941989) + a1 * 4)))), v_rip + 10796164, v_stack_m8B8, v_stack_m8B6);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941962) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941989) + a1 * 4)) * 4))))) >> (6));
    if (a2 < ((unsigned int)(v_stack_m8B8))) goto loc_003BF981;
    goto loc_003BF992;
loc_003BF981:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941962) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941989) + a1 * 4)) * 4))) & (63));
    a2 = (*(unsigned __int64 *)(v_rsp + 0 * 8 + 56)) >> ((unsigned __int8)((unsigned __int8)(a3)));
    a2 = (unsigned __int8)((a2) & ((unsigned __int8)(v_rdi + 1)));
loc_003BF992:
    if ((*(unsigned __int8 *)(result + 35404)) == ((unsigned __int8)(a2))) goto loc_003BF90E;
    v_stack_m8C8 = (unsigned __int8)(v_rdi + 1);
    result = KeCheckProcessorAffinityEx(v_stack_m8B8, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941989) + a1 * 4)))), a3, v_stack_m8B6);
    *(unsigned __int8 *)(result + 35404) = (unsigned __int8)(result);
    goto loc_003BF90E;
loc_003BF9BB:
    if ((*(unsigned __int8 *)(v_rip + 12611890)) == 0) goto loc_003BFAB2;
    if ((*(unsigned __int8 *)(v_rip + 12611871)) == 0) goto loc_003BFAB2;
    if (*(unsigned __int64 *)(v_rip + 11843652) == 0) goto loc_003BFAB2;
    if ((*(unsigned __int64 *)(v_rip + 11843644)) == 0) goto loc_003BFAB2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10796556))) == 0) goto loc_003BFA53;
loc_003BFA05:
    result = (unsigned int)((0) * (*(unsigned int *)(v_rip + 12612118)));
    result = (unsigned int)((result) + (*(unsigned int *)(v_rip + 11843610)));
    a1 = (*(unsigned __int64 *)(v_rip + 12612612)) + (result);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11843587) + 0 * 2) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11843587) + 0 * 2 + 1) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 1));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 1)) & ((unsigned __int8)(*(unsigned __int8 *)(a1))));
    result = 0 + 1;
    if ((((unsigned __int8)(a1)) & (2)) == 0) { result = 0; }
    a4 = (unsigned int)((0) + ((unsigned int)(v_rdi + 1)));
    if (((unsigned int)(a4)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10796470))))) goto loc_003BFA05;
loc_003BFA53:
    a1 = (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10796470))))) ? 1 : 0;
    result = KeIsForceParkingEnabled(a1, 0, (unsigned int)((unsigned int)(result)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_003BFA7E;
    if ((unsigned __int8)(a1) != 0) {
        a2 = *(unsigned __int16 *)(v_rip + 10796549);
        a3 = v_stack_m8B8;
        a1 = v_rip + 10796535;
        result = KiCopyAffinityEx(a1, a2, a3, a4);
    }
    result = RtlCompareMemory(*(unsigned __int64 *)(v_rip + 11843587), *(unsigned __int64 *)(v_rip + 11843491), (unsigned int)(*(unsigned int *)(v_rip + 10796556)) + (unsigned int)(*(unsigned int *)(v_rip + 10796556)) * 1, a4);
    if (result != ((unsigned int)(*(unsigned int *)(v_rip + 10796556)) + (unsigned int)(*(unsigned int *)(v_rip + 10796556)) * 1)) {
        a2 = *(unsigned __int64 *)(v_rip + 11843460);
        a3 = (unsigned int)(*(unsigned int *)(v_rip + 10796556)) + (unsigned int)(*(unsigned int *)(v_rip + 10796556)) * 1;
        a1 = *(unsigned __int64 *)(v_rip + 11843458);
        result = memcpy(a1, a2, a3, a4);
        a1 = 0;
        result = PpmEventHgsHardwareTableResonChanged(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12604772)))) & (4)) != 0) goto loc_003BFAC5;
    if ((unsigned __int8)((unsigned int)(v_stack_m8C4)) == 0) goto loc_003BFCC9;
loc_003BFAC5:
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 2024 + 608) = 0x200001ULL;
    result = memset(v_rsp - 2024 + 616, a2, 256, a4);
loc_003BFAE7:
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12611802) + 4))) goto loc_003BFC37;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10796556)) + (unsigned int)(*(unsigned int *)(v_rip + 10796556)) * 1) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rsp - 2024 + 880) = 0x200001ULL;
    a2 = 0;
    result = memset(v_rsp - 2024 + 888, a2, 256, a4);
    goto loc_003BFB2A;
loc_003BFB27:
    v_r12 = 0;
loc_003BFB2A:
loc_003BFB38:
    if (*(unsigned __int64 *)(v_rip + 10795655) != 0) goto loc_003BFB52;
    v_rdi = (unsigned __int16)((0) + ((unsigned __int16)(v_rdi + 1)));
    if (((unsigned int)((unsigned __int16)(v_rdi))) >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 10795631)))) goto loc_003BFBE4;
    goto loc_003BFB38;
loc_003BFB52:
    a1 = (unsigned int)(((unsigned __int16)((unsigned __int16)(v_rdi))) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)(v_rip + 10795624))));
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))), v_rip + 10795624, 256, a4);
    result = (unsigned int)((0) * (*(unsigned int *)(v_rip + 12611744)));
    result = (unsigned int)((result) + ((unsigned int)(*(unsigned __int16 *)(result + 35402))));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12612219) + result * 1 + 1)) == 0) goto loc_003BFB27;
    if (((unsigned int)(v_rsi)) == -1) goto loc_003BFBAF;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12612219) + result * 1 + 1))) > ((unsigned int)(v_rsi))) goto loc_003BFBAF;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12612219) + result * 1 + 1))) != ((unsigned int)(v_rsi))) goto loc_003BFB27;
    goto loc_003BFBD0;
loc_003BFBAF:
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 2024 + 880) = 0x200001ULL;
    result = memset(v_rsp - 2024 + 888, a2, 256, a4);
loc_003BFBD0:
    result = KeAddProcessorAffinityEx(v_rsp - 2024 + 880, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))), 256, a4);
    goto loc_003BFB27;
loc_003BFBE4:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12612219) + result * 1 + 1))))) == -1) goto loc_003BFC18;
    result = KiOrAffinityEx(v_rsp - 2024 + 608, v_rsp - 2024 + 880, v_rsp - 2024 + 608, *(unsigned __int16 *)(v_rsp - 2024 + 610));
    v_r14 = (unsigned int)((0) + ((unsigned int)(v_rdi + 1)));
    goto loc_003BFAE7;
loc_003BFC18:
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 2024 + 608) = 0x200001ULL;
    result = memset(v_rsp - 2024 + 616, a2, 256, *(unsigned __int16 *)(v_rsp - 2024 + 610));
loc_003BFC37:
loc_003BFC3B:
    if (((unsigned __int16)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4))))) >= (*(unsigned __int16 *)(v_rsp - 2024 + 608))) goto loc_003BFCA0;
    if ((*(unsigned __int64 *)(v_rsp - 2024 + (unsigned __int16)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))) * 8 + 616)) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))) goto loc_003BFC56;
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))) + ((unsigned __int16)(v_rdi + 1)));
    goto loc_003BFC3B;
loc_003BFC56:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12604352)))) & (4)) == 0) goto loc_003BFC87;
    result = PpmHeteroHgsGetContainmentType(v_rsp - 2024 + 608, v_stack_m8C0, 256, *(unsigned __int16 *)(v_rsp - 2024 + 610));
    a3 = 0;
    result = PpmEventHgsContainmentHwUpdate(v_rsp - 2024 + 608, v_stack_m8C0, a3, *(unsigned __int16 *)(v_rsp - 2024 + 610));
    goto loc_003BFCA0;
loc_003BFC87:
    if ((unsigned __int8)((unsigned int)(v_stack_m8C4)) != 0) {
        a2 = (unsigned __int8)((unsigned int)(v_stack_m8C4));
        a1 = v_rsp - 2024 + 608;
        result = PpmHeteroHgsDetectContainmentPresence(a1, a2, a3, *(unsigned __int16 *)(v_rsp - 2024 + 610));
        result = PpmHeteroHgsEvalAndRegisterContainmentGroups(a1, a2, a3, *(unsigned __int16 *)(v_rsp - 2024 + 610));
    }
loc_003BFCA4:
    if (((unsigned __int16)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4))))) >= v_stack_m8B8) goto loc_003BFCBA;
    if ((*(unsigned __int64 *)(v_rsp + (unsigned __int16)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))) * 8 + 56)) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))) goto loc_003BFCBD;
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))) + ((unsigned __int16)(v_rdi + 1)));
    goto loc_003BFCA4;
loc_003BFCBA:
loc_003BFCBD:
    result = PpmHeteroHgsUpdateContainmentGlobalHints((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))), a2, a3, *(unsigned __int16 *)(v_rsp - 2024 + 610));
    result = PpmHeteroHgsCheckContainmentDecision((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11941449) + a1 * 4)))), a2, a3, *(unsigned __int16 *)(v_rsp - 2024 + 610));
loc_003BFCC9:
    a1 = 0;
    result = PpmEventHgsHardwareTable(a1, a2, a3, *(unsigned __int16 *)(v_rsp - 2024 + 610));
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 11842866), a2, a3, *(unsigned __int16 *)(v_rsp - 2024 + 610));
loc_003BFCE8:
    a1 = (*(unsigned __int64 *)(v_rsp - 2024 + 1968)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, *(unsigned __int16 *)(v_rsp - 2024 + 610));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmHeteroUpdateHgsConfiguration(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m8B0;
    uint32_t v_stack_m8B4;
    uint16_t v_stack_m8B6;
    uint16_t v_stack_m8B8;
    uint32_t v_stack_m8C0;
    uint32_t v_stack_m8C4;
    uint8_t v_stack_m8C8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (0x8C0ULL);
    result = (*(uint64_t *)(v_rip + 0xA4B3CF)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x7E8 + 0x7B0) = result;
    local_rdi = 0;
    Arg2 = 0;
    v_stack_m8C0 = 0;
    result = memset(local_rsp - 2024 + 1152, Arg2, 264, a4);
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 336, Arg2, 264, a4);
    Arg2 = 0;
    result = memset(v_stack_m8B0, Arg2, (uint32_t)((uint32_t)(264 - 8)), a4);
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 880, Arg2, 264, a4);
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 608, Arg2, 264, a4);
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 1704, Arg2, (uint32_t)((uint32_t)(264 - 8)), a4);
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 1424, Arg2, 264, a4);
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 64, Arg2, 264, a4);
    v_stack_m8C8 = 0;
    if ((*(uint8_t *)(v_rip + 0xC07680)) == 0) goto loc_003BFCE8;
    result = KeIsEmptyAffinityEx(v_rip + 10797431, Arg2, 264, a4);
    if ((uint32_t)(result) != 0) goto loc_003BFCE8;
    if (*(uint64_t *)(v_rip + 0xB4BDFB) == 0) goto loc_003BFCE8;
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0xB4BDC3), Arg2, 264, a4);
    if ((uint8_t)(result) == 0) goto loc_003BFCE8;
    local_r12 = 0;
    local_r13 = 0;
    if ((*(uint8_t *)(v_rip + 0xC07695)) == 0) { local_r13 = (uint32_t)(local_rdi + 1); }
    *(uint8_t *)(v_rip + 0xC0767F) = (uint8_t)(local_rdi + 1);
    Arg2 = 0;
    v_stack_m8C4 = (uint32_t)(local_r13);
    v_stack_m8B6 = (uint16_t)(local_rdi + 1 + 31);
    result = memset(v_stack_m8B0, Arg2, (uint32_t)((uint32_t)(264 - 8)), a4);
    *(uint64_t *)(v_rip + 0xA4C3D1) = 0x200001ULL;
    Arg2 = 0;
    result = memset(v_rip + 10798032, Arg2, (uint32_t)((uint32_t)(264 - 8)), a4);
    v_stack_m8B4 = 0;
    local_rsi = (uint16_t)(v_stack_m8B6);
    if ((*(uint16_t *)(v_rip + 0xA4C0E3)) <= ((uint16_t)(v_stack_m8B6))) { local_rsi = *(uint16_t *)(v_rip + 0xA4C0D3); }
    v_stack_m8B8 = (uint16_t)(local_rsi);
    if (0 >= ((uint16_t)(local_rsi))) goto loc_003BF4FE;
    a3 = ((uint16_t)(local_rsi)) << (3);
    result = memcpy(v_stack_m8B0, v_rip + 10797253, a3, a4);
loc_003BF4F1:
    local_rdi = (uint16_t)((0) + ((uint16_t)(local_rdi + 1)));
    if (((uint16_t)(local_rdi)) < ((uint16_t)(local_rsi))) goto loc_003BF4F1;
loc_003BF4FE:
    if (((uint16_t)(local_rdi)) >= ((uint16_t)(v_stack_m8B6))) goto loc_003BF515;
loc_003BF503:
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)(local_rdi + 1)));
    *(uint64_t *)(local_rsp + (uint16_t)(local_rdi) * 8 + 0x38) = 0;
    if (((uint16_t)(local_rdi)) < v_stack_m8B6) goto loc_003BF503;
loc_003BF515:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xC076AC) + 0x4)) <= 0) goto loc_003BF8F6;
loc_003BF52C:
    *(uint64_t *)(local_rsp - 0x7E8 + 0x480) = 0x200001ULL;
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 1160, Arg2, 264 - 8, a4);
    *(uint64_t *)(local_rsp - 0x7E8 + 0x590) = 0x200001ULL;
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 1432, Arg2, 264 - 8, a4);
    *(uint64_t *)(local_rsp - 0x7E8 + 0x150) = 0x200001ULL;
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 344, Arg2, 264 - 8, a4);
    *(uint64_t *)(local_rsp - 0x7E8 + 0x40) = 0x200001ULL;
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 72, Arg2, 264 - 8, a4);
    *(uint64_t *)(local_rsp - 0x7E8 + 0x6A0) = 0x200001ULL;
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 1704, Arg2, 264 - 8, a4);
loc_003BF5BD:
loc_003BF5CB:
    if (*(uint64_t *)(v_rip + 0xA4BFEB) != 0) goto loc_003BF5E8;
    local_r14 = (uint16_t)((0) + ((uint16_t)(local_rdi + 1)));
    if (((uint32_t)((uint16_t)(local_r14))) >= ((uint32_t)(*(uint16_t *)(v_rip + 0xA4BFDC)))) goto loc_003BF859;
    goto loc_003BF5CB;
loc_003BF5E8:
    Arg1 = (uint32_t)(((uint16_t)((uint16_t)(local_r14))) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)(v_rip + 10797013))));
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)))), v_rip + 10797013, 264 - 8, a4);
    local_r11 = 0;
    if (*(uint64_t *)(v_rip + 0xC078A9) == 0) goto loc_003BF641;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC0765C)))) & (2)) == 0) goto loc_003BF641;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4))))) * (*(uint32_t *)(*(uint64_t *)(v_rip + 0xC078A9) + 0x4)));
    Arg1 = (uint32_t)((Arg1) + (0));
    goto loc_003BF6A2;
loc_003BF641:
    if (((uint8_t)(*(uint8_t *)(v_rip + 0xC059BC))) != 2) goto loc_003BF670;
    Arg1 = (uint32_t)((0) * (*(uint32_t *)(v_rip + 0xC075CF)));
    result = (uint32_t)((*(uint16_t *)(result + 0x8A4A)) + ((uint32_t)(Arg1)));
    goto loc_003BF6A2;
loc_003BF670:
    if (((uint8_t)(result)) != ((uint8_t)(local_rdi + 1))) goto loc_003BF69D;
    Arg1 = (uint32_t)((0) * (*(uint32_t *)(v_rip + 0xC075A7)));
    Arg1 = (uint32_t)((Arg1) << (2));
    Arg2 = (*(uint16_t *)(result + 0x8A4A)) + (*(uint64_t *)(v_rip + 0xC07795));
    goto loc_003BF6A2;
loc_003BF69D:
loc_003BF6A2:
    *(uint8_t *)(*(uint64_t *)(result + 0x8A50) + 0x0 * 4 + 0x6) = (uint8_t)((uint8_t)(local_rdi + 1));
    *(uint8_t *)(*(uint64_t *)(result + 0x8A50) + 0x0 * 4 + 0x7) = (uint8_t)((uint8_t)(local_rdi + 1));
    if ((*(uint8_t *)(v_rip + 0xC07446)) == 0) goto loc_003BF7CA;
    if ((*(uint8_t *)(v_rip + 0xC073CD)) == 0) goto loc_003BF709;
    if ((*(uint32_t *)(v_rip + 0xC07676)) == 0) goto loc_003BF709;
    if ((uint8_t)((uint8_t)(local_rdi + 1)) != 0) {
        Arg1 = local_rsp - 2024 + 64;
    }
    result = KeAddProcessorAffinityEx(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)))), result, a4);
    if ((uint8_t)((uint8_t)(local_rdi + 1)) != 0) goto loc_003BF6FD;
    goto loc_003BF7C0;
loc_003BF6FD:
    goto loc_003BF7C0;
loc_003BF709:
    if ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4))))) == 0) goto loc_003BF7A9;
    if ((uint8_t)((uint8_t)(local_rdi + 1)) == 0) goto loc_003BF7A9;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63A8F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)) * 4))))) >> (6));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63A8F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)) * 4))) & (63));
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x7E8 + 0x150))) > ((uint32_t)(Arg1))) goto loc_003BF74F;
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x7E8 + 0x152))) <= ((uint32_t)(Arg1))) goto loc_003BF768;
    *(uint16_t *)(local_rsp - 0x7E8 + 0x150) = (uint16_t)(local_rdi + 1 + Arg1 * 1);
loc_003BF74F:
    *(uint64_t *)(local_rsp - 0x7E8 + (uint32_t)((uint32_t)(Arg1)) * 8 + 0x158) = *(uint64_t *)(local_rsp - 0x7E8 + Arg1 * 8 + 0x158);
loc_003BF768:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63A8F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)) * 4))) & (63));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63A8F) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)) * 4))))) >> (6));
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x7E8 + 0x40))) > ((uint32_t)(Arg1))) goto loc_003BF791;
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x7E8 + 0x42))) <= ((uint32_t)(Arg1))) goto loc_003BF5BD;
    *(uint16_t *)(local_rsp - 0x7E8 + 0x40) = (uint16_t)(local_rdi + 1 + Arg1 * 1);
loc_003BF791:
    *(uint64_t *)(local_rsp - 0x7E8 + (uint32_t)((uint32_t)(Arg1)) * 8 + 0x48) = *(uint64_t *)(local_rsp - 0x7E8 + Arg1 * 8 + 0x48);
    goto loc_003BF5BD;
loc_003BF7A9:
    result = KeAddProcessorAffinityEx(local_rsp - 2024 + 1152, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)))), a3, a4);
loc_003BF7C0:
    result = KeAddProcessorAffinityEx(local_rsp - 2024 + 1424, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)))), a3, a4);
    goto loc_003BF5BD;
loc_003BF7CA:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB639DF) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)) * 4))))) >> (6));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB639DF) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)) * 4))) & (63));
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x7E8 + 0x40))) > ((uint32_t)(Arg1))) goto loc_003BF7F6;
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x7E8 + 0x42))) <= ((uint32_t)(Arg1))) goto loc_003BF809;
    *(uint16_t *)(local_rsp - 0x7E8 + 0x40) = (uint16_t)(local_rdi + 1 + Arg1 * 1);
loc_003BF7F6:
    *(uint64_t *)(local_rsp - 0x7E8 + (uint32_t)((uint32_t)(Arg1)) * 8 + 0x48) = *(uint64_t *)(local_rsp - 0x7E8 + Arg1 * 8 + 0x48);
loc_003BF809:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB639DF) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)) * 4))) & (63));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB639DF) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63BB2) + Arg1 * 4)) * 4))))) >> (6));
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x7E8 + 0x150))) > ((uint32_t)(Arg1))) goto loc_003BF83B;
    if (((uint32_t)(*(uint16_t *)(local_rsp - 0x7E8 + 0x152))) <= ((uint32_t)(Arg1))) goto loc_003BF5BD;
    *(uint16_t *)(local_rsp - 0x7E8 + 0x150) = (uint16_t)(local_rdi + 1 + Arg1 * 1);
loc_003BF83B:
    *(uint64_t *)(local_rsp - 0x7E8 + (uint32_t)((uint32_t)(Arg1)) * 8 + 0x158) = *(uint64_t *)(local_rsp - 0x7E8 + Arg1 * 8 + 0x158);
    goto loc_003BF5BD;
loc_003BF859:
    result = PPmHeteroHgsUpdateOrderValue(local_rsp - 2024 + 64, local_rsp - 2024 + 1424, 0, (uint8_t)(local_rdi + 1));
    a4 = 0;
    local_r13 = (uint8_t)((0) | ((uint8_t)(result)));
    result = PPmHeteroHgsUpdateOrderValue(local_rsp - 2024 + 336, local_rsp - 2024 + 1152, 0, a4);
    local_r13 = (uint8_t)((local_r13) | ((uint8_t)(result)));
    result = KiAndAffinityEx(local_rsp - 2024 + 1424, local_rsp - 2024 + 1152, local_rsp - 2024 + 1696, *(uint16_t *)(local_rsp - 0x7E8 + 0x6A2));
    result = KiAndAffinityEx(v_stack_m8B8, local_rsp - 2024 + 1696, v_stack_m8B8, v_stack_m8B6);
    local_r15 = (uint32_t)((0) + ((uint32_t)(local_rdi + 1)));
    if (((uint32_t)(local_r15)) < (*(uint32_t *)(*(uint64_t *)(v_rip + 0xC072F5) + 0x4))) goto loc_003BF52C;
    v_stack_m8C8 = (uint8_t)(local_r13);
loc_003BF8F6:
    if ((*(uint8_t *)(v_rip + 0xC071F2)) == 0) goto loc_003BF9BB;
loc_003BF90E:
loc_003BF91C:
    if (*(uint64_t *)(v_rip + 0xA4BC9E) != 0) goto loc_003BF936;
    local_rdi = (uint16_t)((0) + ((uint16_t)(local_rdi + 1)));
    if (((uint32_t)((uint16_t)(local_rdi))) >= ((uint32_t)(*(uint16_t *)(v_rip + 0xA4BC8B)))) goto loc_003BF9BB;
    goto loc_003BF91C;
loc_003BF936:
    Arg1 = (uint32_t)(((uint16_t)((uint16_t)(local_rdi))) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)(v_rip + 10796164))));
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63865) + Arg1 * 4)))), v_rip + 10796164, v_stack_m8B8, v_stack_m8B6);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB6384A) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63865) + Arg1 * 4)) * 4))))) >> (6));
    if (Arg2 < ((uint32_t)(v_stack_m8B8))) goto loc_003BF981;
    goto loc_003BF992;
loc_003BF981:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB6384A) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63865) + Arg1 * 4)) * 4))) & (63));
    Arg2 = (*(uint64_t *)(local_rsp + 0x0 * 8 + 0x38)) >> ((uint8_t)((uint8_t)(a3)));
    Arg2 = (uint8_t)((Arg2) & ((uint8_t)(local_rdi + 1)));
loc_003BF992:
    if ((*(uint8_t *)(result + 0x8A4C)) == ((uint8_t)(Arg2))) goto loc_003BF90E;
    v_stack_m8C8 = (uint8_t)(local_rdi + 1);
    result = KeCheckProcessorAffinityEx(v_stack_m8B8, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63865) + Arg1 * 4)))), a3, v_stack_m8B6);
    *(uint8_t *)(result + 0x8A4C) = (uint8_t)(result);
    goto loc_003BF90E;
loc_003BF9BB:
    if ((*(uint8_t *)(v_rip + 0xC07132)) == 0) goto loc_003BFAB2;
    if ((*(uint8_t *)(v_rip + 0xC0711F)) == 0) goto loc_003BFAB2;
    if (*(uint64_t *)(v_rip + 0xB4B844) == 0) goto loc_003BFAB2;
    if ((*(uint64_t *)(v_rip + 0xB4B83C)) == 0) goto loc_003BFAB2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA4BE0C))) == 0) goto loc_003BFA53;
loc_003BFA05:
    result = (uint32_t)((0) * (*(uint32_t *)(v_rip + 0xC07216)));
    result = (uint32_t)((result) + (*(uint32_t *)(v_rip + 0xB4B81A)));
    Arg1 = (*(uint64_t *)(v_rip + 0xC07404)) + (result);
    *(uint8_t *)(*(uint64_t *)(v_rip + 0xB4B803) + 0x0 * 2) = (uint8_t)(*(uint8_t *)(Arg1));
    *(uint8_t *)(*(uint64_t *)(v_rip + 0xB4B803) + 0x0 * 2 + 0x1) = (uint8_t)(*(uint8_t *)(Arg1 + 0x1));
    Arg1 = (uint8_t)((*(uint8_t *)(Arg1 + 0x1)) & ((uint8_t)(*(uint8_t *)(Arg1))));
    result = 0 + 1;
    if ((((uint8_t)(Arg1)) & (2)) == 0) { result = 0; }
    a4 = (uint32_t)((0) + ((uint32_t)(local_rdi + 1)));
    if (((uint32_t)(a4)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA4BDB6))))) goto loc_003BFA05;
loc_003BFA53:
    Arg1 = (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA4BDB6))))) ? 1 : 0;
    result = KeIsForceParkingEnabled(Arg1, 0, (uint32_t)((uint32_t)(result)), a4);
    if ((uint8_t)(result) == 0) goto loc_003BFA7E;
    if ((uint8_t)(Arg1) != 0) {
        Arg2 = *(uint16_t *)(v_rip + 0xA4BE05);
        a3 = v_stack_m8B8;
        Arg1 = v_rip + 10796535;
        result = KiCopyAffinityEx(Arg1, Arg2, a3, a4);
    }
    result = RtlCompareMemory(*(uint64_t *)(v_rip + 0xB4B803), *(uint64_t *)(v_rip + 0xB4B7A3), (uint32_t)(*(uint32_t *)(v_rip + 0xA4BE0C)) + (uint32_t)(*(uint32_t *)(v_rip + 0xA4BE0C)) * 1, a4);
    if (result != ((uint32_t)(*(uint32_t *)(v_rip + 0xA4BE0C)) + (uint32_t)(*(uint32_t *)(v_rip + 0xA4BE0C)) * 1)) {
        Arg2 = *(uint64_t *)(v_rip + 0xB4B784);
        a3 = (uint32_t)(*(uint32_t *)(v_rip + 0xA4BE0C)) + (uint32_t)(*(uint32_t *)(v_rip + 0xA4BE0C)) * 1;
        Arg1 = *(uint64_t *)(v_rip + 0xB4B782);
        result = memcpy(Arg1, Arg2, a3, a4);
        Arg1 = 0;
        result = PpmEventHgsHardwareTableResonChanged(Arg1, Arg2, a3, a4);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC05564)))) & (4)) != 0) goto loc_003BFAC5;
    if ((uint8_t)((uint32_t)(v_stack_m8C4)) == 0) goto loc_003BFCC9;
loc_003BFAC5:
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x7E8 + 0x260) = 0x200001ULL;
    result = memset(local_rsp - 2024 + 616, Arg2, 256, a4);
loc_003BFAE7:
    if (0 >= (*(uint32_t *)(*(uint64_t *)(v_rip + 0xC070DA) + 0x4))) goto loc_003BFC37;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA4BE0C)) + (uint32_t)(*(uint32_t *)(v_rip + 0xA4BE0C)) * 1) | (0xFFFFFFFFULL));
    *(uint64_t *)(local_rsp - 0x7E8 + 0x370) = 0x200001ULL;
    Arg2 = 0;
    result = memset(local_rsp - 2024 + 888, Arg2, 256, a4);
    goto loc_003BFB2A;
loc_003BFB27:
    local_r12 = 0;
loc_003BFB2A:
loc_003BFB38:
    if (*(uint64_t *)(v_rip + 0xA4BA87) != 0) goto loc_003BFB52;
    local_rdi = (uint16_t)((0) + ((uint16_t)(local_rdi + 1)));
    if (((uint32_t)((uint16_t)(local_rdi))) >= ((uint32_t)(*(uint16_t *)(v_rip + 0xA4BA6F)))) goto loc_003BFBE4;
    goto loc_003BFB38;
loc_003BFB52:
    Arg1 = (uint32_t)(((uint16_t)((uint16_t)(local_rdi))) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)(v_rip + 10795624))));
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))), v_rip + 10795624, 256, a4);
    result = (uint32_t)((0) * (*(uint32_t *)(v_rip + 0xC070A0)));
    result = (uint32_t)((result) + ((uint32_t)(*(uint16_t *)(result + 0x8A4A))));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xC0727B) + result * 1 + 0x1)) == 0) goto loc_003BFB27;
    if (((uint32_t)(local_rsi)) == -1) goto loc_003BFBAF;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xC0727B) + result * 1 + 0x1))) > ((uint32_t)(local_rsi))) goto loc_003BFBAF;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xC0727B) + result * 1 + 0x1))) != ((uint32_t)(local_rsi))) goto loc_003BFB27;
    goto loc_003BFBD0;
loc_003BFBAF:
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x7E8 + 0x370) = 0x200001ULL;
    result = memset(local_rsp - 2024 + 888, Arg2, 256, a4);
loc_003BFBD0:
    result = KeAddProcessorAffinityEx(local_rsp - 2024 + 880, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))), 256, a4);
    goto loc_003BFB27;
loc_003BFBE4:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xC0727B) + result * 1 + 0x1))))) == -1) goto loc_003BFC18;
    result = KiOrAffinityEx(local_rsp - 2024 + 608, local_rsp - 2024 + 880, local_rsp - 2024 + 608, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
    local_r14 = (uint32_t)((0) + ((uint32_t)(local_rdi + 1)));
    goto loc_003BFAE7;
loc_003BFC18:
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x7E8 + 0x260) = 0x200001ULL;
    result = memset(local_rsp - 2024 + 616, Arg2, 256, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
loc_003BFC37:
loc_003BFC3B:
    if (((uint16_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4))))) >= (*(uint16_t *)(local_rsp - 0x7E8 + 0x260))) goto loc_003BFCA0;
    if ((*(uint64_t *)(local_rsp - 0x7E8 + (uint16_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))) * 8 + 0x268)) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))) goto loc_003BFC56;
    Arg1 = (uint16_t)(((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))) + ((uint16_t)(local_rdi + 1)));
    goto loc_003BFC3B;
loc_003BFC56:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC053C0)))) & (4)) == 0) goto loc_003BFC87;
    result = PpmHeteroHgsGetContainmentType(local_rsp - 2024 + 608, v_stack_m8C0, 256, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
    a3 = 0;
    result = PpmEventHgsContainmentHwUpdate(local_rsp - 2024 + 608, v_stack_m8C0, a3, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
    goto loc_003BFCA0;
loc_003BFC87:
    if ((uint8_t)((uint32_t)(v_stack_m8C4)) != 0) {
        Arg2 = (uint8_t)((uint32_t)(v_stack_m8C4));
        Arg1 = local_rsp - 2024 + 608;
        result = PpmHeteroHgsDetectContainmentPresence(Arg1, Arg2, a3, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
        result = PpmHeteroHgsEvalAndRegisterContainmentGroups(Arg1, Arg2, a3, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
    }
loc_003BFCA4:
    if (((uint16_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4))))) >= v_stack_m8B8) goto loc_003BFCBA;
    if ((*(uint64_t *)(local_rsp + (uint16_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))) * 8 + 0x38)) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))) goto loc_003BFCBD;
    Arg1 = (uint16_t)(((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))) + ((uint16_t)(local_rdi + 1)));
    goto loc_003BFCA4;
loc_003BFCBA:
loc_003BFCBD:
    result = PpmHeteroHgsUpdateContainmentGlobalHints((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))), Arg2, a3, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
    result = PpmHeteroHgsCheckContainmentDecision((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63649) + Arg1 * 4)))), Arg2, a3, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
loc_003BFCC9:
    Arg1 = 0;
    result = PpmEventHgsHardwareTable(Arg1, Arg2, a3, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0xB4B532), Arg2, a3, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
loc_003BFCE8:
    Arg1 = (*(uint64_t *)(local_rsp - 0x7E8 + 0x7B0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, *(uint16_t *)(local_rsp - 0x7E8 + 0x262));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003BF344&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
