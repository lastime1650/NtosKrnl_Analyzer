# PspEnforceLimitsJobPostCallback

- RVA: `0x00919720`–`0x00919D95` (길이 `1,653` bytes)
- VA: `0x0000000140919720`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008AD08`
- 디코드: `391`개 명령, `1,653/1,653` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00919778` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00919798` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0091985B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0091987D` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00919987` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009199A0` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009199BD` → [PspAddAccountingValues](PspAddAccountingValues_function_00919D9C.md) (function, `0x00919D9C`)
- `0x009199CB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009199D4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009199F6` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00919A06` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00919A28` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00919A36` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00919A6B` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00919A7D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00919A88` → [PspUnlockJob](PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00919ABA` → [PspLockJobMemoryLimitsShared](PspLockJobMemoryLimitsShared_function_0091A394.md) (function, `0x0091A394`)
- `0x00919B0E` → [PspUnlockJobMemoryLimitsShared](PspUnlockJobMemoryLimitsShared_function_0091A420.md) (function, `0x0091A420`)
- `0x00919BA7` → [PspLockJobExclusive](PspLockJobExclusive_function_0091A4B8.md) (function, `0x0091A4B8`)
- `0x00919C10` → [PspRateControlLimitFlag](PspRateControlLimitFlag_function_0091A3FC.md) (function, `0x0091A3FC`)
- `0x00919C53` → [PspUnlockJob](PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00919C87` → [PspRateControlLimitFlag](PspRateControlLimitFlag_function_0091A3FC.md) (function, `0x0091A3FC`)
- `0x00919C9B` → [PspSendReliableJobNotification](PspSendReliableJobNotification_function_009171D4.md) (function, `0x009171D4`)
- `0x00919D6D` → [PspRemoveProcessFromJobChain](../90/PspRemoveProcessFromJobChain_function_00907288.md) (function, `0x00907288`)
- `0x00919D7A` → [PspSendNoWakeChargeLimitNotification](../78/PspSendNoWakeChargeLimitNotification_function_007853B0.md) (function, `0x007853B0`)
- `0x00919D8B` → [PspSendNoWakeChargeLimitNotification](../78/PspSendNoWakeChargeLimitNotification_function_007853B0.md) (function, `0x007853B0`)

### Direct callers
- [PspCallJobHierarchyCallbacks](PspCallJobHierarchyCallbacks_function_00918A34.md) at `0x00918B40`

### Static image references
- `0x0091973C` → RVA `0x00E0A740` (`.data`; read)
- `0x00919943` → RVA `0x00FC5160` (`ALMOSTRO`; read)
- `0x00919952` → RVA `0x00FC515C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00919778` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00919798` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0091985B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0091987D` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00919987` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009199A0` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009199CB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009199D4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009199F6` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00919A06` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00919A28` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00919A36` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00919A6B` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00919A7D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0091992A` → [sub_00B21AB8 + 0xF](../B2/Unknown_function_00B21AB8.md) (`tail-transfer`)
  - `0x00919D2F` → [sub_00B21AB8](../B2/Unknown_function_00B21AB8.md) (`tail-transfer`)
  - `0x00919D73` → [sub_00B21AB8](../B2/Unknown_function_00B21AB8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00919720  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00919725  55                              push rbp
00919726  56                              push rsi
00919727  57                              push rdi
00919728  41 54                           push r12
0091972A  41 55                           push r13
0091972C  41 56                           push r14
0091972E  41 57                           push r15
00919730  48 8D 6C 24 D0                  lea rbp, [rsp - 0x30]
00919735  48 81 EC 30 01 00 00            sub rsp, 0x130
0091973C  48 8B 05 FD 0F 4F 00            mov rax, qword ptr [rip + 0x4f0ffd]
00919743  48 33 C4                        xor rax, rsp
00919746  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0091974A  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
00919753  45 33 FF                        xor r15d, r15d
00919756  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
0091975B  48 8B D9                        mov rbx, rcx
0091975E  48 85 FF                        test rdi, rdi
00919761  74 08                           je 0x14091976b
00919763  66 FF 8F E6 01 00 00            dec word ptr [rdi + 0x1e6]
0091976A  90                              nop
0091976B  41 BC 01 00 00 00               mov r12d, 1
00919771  48 83 C1 38                     add rcx, 0x38
00919775  41 8A D4                        mov dl, r12b
00919778  E8 43 84 8F FF                  call 0x140211bc0
0091977D  48 8B 83 C0 04 00 00            mov rax, qword ptr [rbx + 0x4c0]
00919784  48 85 C0                        test rax, rax
00919787  0F 85 02 03 00 00               jne 0x140919a8f
0091978D  33 D2                           xor edx, edx
0091978F  45 8D 44 24 3F                  lea r8d, [r12 + 0x3f]
00919794  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00919798  E8 A3 D4 DA FF                  call 0x1406c6c40
0091979D  4C 8B B3 60 02 00 00            mov r14, qword ptr [rbx + 0x260]
009197A4  48 8D 83 48 05 00 00            lea rax, [rbx + 0x548]
009197AB  0F 10 00                        movups xmm0, xmmword ptr [rax]
009197AE  4C 8B AB 68 02 00 00            mov r13, qword ptr [rbx + 0x268]
009197B5  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
009197B9  0F 29 44 24 70                  movaps xmmword ptr [rsp + 0x70], xmm0
009197BE  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
009197C2  0F 29 4D 80                     movaps xmmword ptr [rbp - 0x80], xmm1
009197C6  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
009197CA  0F 29 45 90                     movaps xmmword ptr [rbp - 0x70], xmm0
009197CE  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
009197D2  0F 29 4D A0                     movaps xmmword ptr [rbp - 0x60], xmm1
009197D6  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
009197DA  0F 29 45 B0                     movaps xmmword ptr [rbp - 0x50], xmm0
009197DE  F2 0F 10 40 60                  movsd xmm0, qword ptr [rax + 0x60]
009197E3  48 8B 83 A0 00 00 00            mov rax, qword ptr [rbx + 0xa0]
009197EA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
009197EF  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
009197F6  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009197FB  8B 83 24 02 00 00               mov eax, dword ptr [rbx + 0x224]
00919801  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00919805  8B 83 00 01 00 00               mov eax, dword ptr [rbx + 0x100]
0091980B  0F 29 4D C0                     movaps xmmword ptr [rbp - 0x40], xmm1
0091980F  F2 0F 11 45 D0                  movsd qword ptr [rbp - 0x30], xmm0
00919814  A8 04                           test al, 4
00919816  0F 85 86 04 00 00               jne 0x140919ca2
0091981C  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00919821  8B 83 10 06 00 00               mov eax, dword ptr [rbx + 0x610]
00919827  41 B8 00 00 40 00               mov r8d, 0x400000
0091982D  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00919832  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00919837  0F BA E0 0B                     bt eax, 0xb
0091983B  73 0D                           jae 0x14091984a
0091983D  44 39 BB 28 04 00 00            cmp dword ptr [rbx + 0x428], r15d
00919844  0F 85 02 03 00 00               jne 0x140919b4c
0091984A  44 85 83 10 06 00 00            test dword ptr [rbx + 0x610], r8d
00919851  0F 85 D1 02 00 00               jne 0x140919b28
00919857  48 8D 4B 38                     lea rcx, [rbx + 0x38]
0091985B  E8 B0 61 94 FF                  call 0x14025fa10
00919860  48 85 FF                        test rdi, rdi
00919863  74 1D                           je 0x140919882
00919865  90                              nop
00919866  66 44 01 A7 E6 01 00 00         add word ptr [rdi + 0x1e6], r12w
0091986E  75 12                           jne 0x140919882
00919870  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
00919877  90                              nop
00919878  48 39 00                        cmp qword ptr [rax], rax
0091987B  74 05                           je 0x140919882
0091987D  E8 FE 93 9C FF                  call 0x1402e2c80
00919882  4C 8B 65 E0                     mov r12, qword ptr [rbp - 0x20]
00919886  41 8B F7                        mov esi, r15d
00919889  BA 00 00 01 00                  mov edx, 0x10000
0091988E  4D 85 E4                        test r12, r12
00919891  0F 85 1C 04 00 00               jne 0x140919cb3
00919897  4C 8B 7D E8                     mov r15, qword ptr [rbp - 0x18]
0091989B  4D 85 FF                        test r15, r15
0091989E  0F 85 21 04 00 00               jne 0x140919cc5
009198A4  4C 8B 75 F0                     mov r14, qword ptr [rbp - 0x10]
009198A8  4D 85 F6                        test r14, r14
009198AB  0F 85 2D 04 00 00               jne 0x140919cde
009198B1  4C 8B 6D 00                     mov r13, qword ptr [rbp]
009198B5  4D 85 ED                        test r13, r13
009198B8  0F 85 F6 01 00 00               jne 0x140919ab4
009198BE  4C 39 6D F8                     cmp qword ptr [rbp - 8], r13
009198C2  0F 85 EC 01 00 00               jne 0x140919ab4
009198C8  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
009198CD  4C 8D 4D 08                     lea r9, [rbp + 8]
009198D1  45 33 C0                        xor r8d, r8d
009198D4  4C 8D 55 E8                     lea r10, [rbp - 0x18]
009198D8  4C 2B C8                        sub r9, rax
009198DB  4C 2B D0                        sub r10, rax
009198DE  48 8D 50 2C                     lea rdx, [rax + 0x2c]
009198E2  41 8B 4C 11 D4                  mov ecx, dword ptr [r9 + rdx - 0x2c]
009198E7  85 C9                           test ecx, ecx
009198E9  0F 85 80 03 00 00               jne 0x140919c6f
009198EF  41 FF C0                        inc r8d
009198F2  48 83 C2 04                     add rdx, 4
009198F6  41 83 F8 03                     cmp r8d, 3
009198FA  7C E6                           jl 0x1409198e2
009198FC  85 F6                           test esi, esi
009198FE  0F 85 9D 02 00 00               jne 0x140919ba1
00919904  48 8B 74 24 28                  mov rsi, qword ptr [rsp + 0x28]
00919909  41 BF 44 00 00 C0               mov r15d, 0xc0000044
0091990F  41 BE 01 00 00 00               mov r14d, 1
00919915  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
00919919  48 85 C9                        test rcx, rcx
0091991C  0F 85 04 04 00 00               jne 0x140919d26
00919922  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00919927  48 85 D2                        test rdx, rdx
0091992A  0F 85 97 81 20 00               jne 0x140b21ac7
00919930  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00919935  48 03 4E 18                     add rcx, qword ptr [rsi + 0x18]
00919939  80 7E 38 00                     cmp byte ptr [rsi + 0x38], 0
0091993D  48 89 4E 18                     mov qword ptr [rsi + 0x18], rcx
00919941  75 20                           jne 0x140919963
00919943  8B 05 17 B8 6A 00               mov eax, dword ptr [rip + 0x6ab817]
00919949  48 3B C8                        cmp rcx, rax
0091994C  0F 83 26 04 00 00               jae 0x140919d78
00919952  8B 05 04 B8 6A 00               mov eax, dword ptr [rip + 0x6ab804]
00919958  48 39 44 24 40                  cmp qword ptr [rsp + 0x40], rax
0091995D  0F 83 25 04 00 00               jae 0x140919d88
00919963  48 8B 8B 18 05 00 00            mov rcx, qword ptr [rbx + 0x518]
0091996A  48 85 C9                        test rcx, rcx
0091996D  0F 84 E4 00 00 00               je 0x140919a57
00919973  48 85 FF                        test rdi, rdi
00919976  74 08                           je 0x140919980
00919978  66 FF 8F E6 01 00 00            dec word ptr [rdi + 0x1e6]
0091997F  90                              nop
00919980  48 83 C1 38                     add rcx, 0x38
00919984  41 8A D6                        mov dl, r14b
00919987  E8 94 B4 8F FF                  call 0x140214e20
0091998C  48 85 FF                        test rdi, rdi
0091998F  74 08                           je 0x140919999
00919991  66 FF 8F E6 01 00 00            dec word ptr [rdi + 0x1e6]
00919998  90                              nop
00919999  41 8A D6                        mov dl, r14b
0091999C  48 8D 4B 38                     lea rcx, [rbx + 0x38]
009199A0  E8 7B B4 8F FF                  call 0x140214e20
009199A5  48 8B 8B 18 05 00 00            mov rcx, qword ptr [rbx + 0x518]
009199AC  4C 8D 8B 48 05 00 00            lea r9, [rbx + 0x548]
009199B3  48 81 C1 48 05 00 00            add rcx, 0x548
009199BA  49 8B D1                        mov rdx, r9
009199BD  E8 DA 03 00 00                  call 0x140919d9c
009199C2  33 D2                           xor edx, edx
009199C4  49 8B C9                        mov rcx, r9
009199C7  44 8D 42 68                     lea r8d, [rdx + 0x68]
009199CB  E8 70 D2 DA FF                  call 0x1406c6c40
009199D0  48 8D 4B 38                     lea rcx, [rbx + 0x38]
009199D4  E8 37 60 94 FF                  call 0x14025fa10
009199D9  48 85 FF                        test rdi, rdi
009199DC  74 1D                           je 0x1409199fb
009199DE  90                              nop
009199DF  66 44 01 B7 E6 01 00 00         add word ptr [rdi + 0x1e6], r14w
009199E7  75 12                           jne 0x1409199fb
009199E9  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
009199F0  90                              nop
009199F1  48 39 00                        cmp qword ptr [rax], rax
009199F4  74 05                           je 0x1409199fb
009199F6  E8 85 92 9C FF                  call 0x1402e2c80
009199FB  48 8B 8B 18 05 00 00            mov rcx, qword ptr [rbx + 0x518]
00919A02  48 83 C1 38                     add rcx, 0x38
00919A06  E8 05 60 94 FF                  call 0x14025fa10
00919A0B  48 85 FF                        test rdi, rdi
00919A0E  74 1D                           je 0x140919a2d
00919A10  90                              nop
00919A11  66 44 01 B7 E6 01 00 00         add word ptr [rdi + 0x1e6], r14w
00919A19  75 12                           jne 0x140919a2d
00919A1B  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
00919A22  90                              nop
00919A23  48 39 00                        cmp qword ptr [rax], rax
00919A26  74 05                           je 0x140919a2d
00919A28  E8 53 92 9C FF                  call 0x1402e2c80
00919A2D  33 C0                           xor eax, eax
00919A2F  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00919A33  48 33 CC                        xor rcx, rsp
00919A36  E8 05 2C D9 FF                  call 0x1406ac640
00919A3B  48 8B 9C 24 80 01 00 00         mov rbx, qword ptr [rsp + 0x180]
00919A43  48 81 C4 30 01 00 00            add rsp, 0x130
00919A4A  41 5F                           pop r15
00919A4C  41 5E                           pop r14
00919A4E  41 5D                           pop r13
00919A50  41 5C                           pop r12
00919A52  5F                              pop rdi
00919A53  5E                              pop rsi
00919A54  5D                              pop rbp
00919A55  C3                              ret
00919A56  CC                              int3
00919A57  48 85 FF                        test rdi, rdi
00919A5A  74 08                           je 0x140919a64
00919A5C  66 FF 8F E6 01 00 00            dec word ptr [rdi + 0x1e6]
00919A63  90                              nop
00919A64  41 8A D6                        mov dl, r14b
00919A67  48 8D 4B 38                     lea rcx, [rbx + 0x38]
00919A6B  E8 B0 B3 8F FF                  call 0x140214e20
00919A70  33 D2                           xor edx, edx
00919A72  48 8D 8B 48 05 00 00            lea rcx, [rbx + 0x548]
00919A79  44 8D 42 68                     lea r8d, [rdx + 0x68]
00919A7D  E8 BE D1 DA FF                  call 0x1406c6c40
00919A82  48 8B D7                        mov rdx, rdi
00919A85  48 8B CB                        mov rcx, rbx
00919A88  E8 73 03 00 00                  call 0x140919e00
00919A8D  EB 9E                           jmp 0x140919a2d
00919A8F  0F 10 40 08                     movups xmm0, xmmword ptr [rax + 8]
00919A93  0F 10 48 18                     movups xmm1, xmmword ptr [rax + 0x18]
00919A97  0F 29 45 E0                     movaps xmmword ptr [rbp - 0x20], xmm0
00919A9B  0F 10 40 28                     movups xmm0, xmmword ptr [rax + 0x28]
00919A9F  0F 29 4D F0                     movaps xmmword ptr [rbp - 0x10], xmm1
00919AA3  0F 10 48 38                     movups xmm1, xmmword ptr [rax + 0x38]
00919AA7  0F 29 45 00                     movaps xmmword ptr [rbp], xmm0
00919AAB  0F 29 4D 10                     movaps xmmword ptr [rbp + 0x10], xmm1
00919AAF  E9 E9 FC FF FF                  jmp 0x14091979d
00919AB4  48 8B D7                        mov rdx, rdi
00919AB7  48 8B CB                        mov rcx, rbx
00919ABA  E8 D5 08 00 00                  call 0x14091a394
00919ABF  4C 8B 83 20 06 00 00            mov r8, qword ptr [rbx + 0x620]
00919AC6  4C 8B 8B C0 04 00 00            mov r9, qword ptr [rbx + 0x4c0]
00919ACD  48 8B 93 B8 04 00 00            mov rdx, qword ptr [rbx + 0x4b8]
00919AD4  41 F7 01 00 00 20 00            test dword ptr [r9], 0x200000
00919ADB  49 8B 49 28                     mov rcx, qword ptr [r9 + 0x28]
00919ADF  4E 8D 04 02                     lea r8, [rdx + r8]
00919AE3  4C 0F 44 C2                     cmove r8, rdx
00919AE7  33 C0                           xor eax, eax
00919AE9  48 85 C9                        test rcx, rcx
00919AEC  74 0B                           je 0x140919af9
00919AEE  4C 3B C1                        cmp r8, rcx
00919AF1  B9 00 02 00 00                  mov ecx, 0x200
00919AF6  0F 47 C1                        cmova eax, ecx
00919AF9  49 8B 49 20                     mov rcx, qword ptr [r9 + 0x20]
00919AFD  48 85 C9                        test rcx, rcx
00919B00  0F 85 57 01 00 00               jne 0x140919c5d
00919B06  0B F0                           or esi, eax
00919B08  48 8B D7                        mov rdx, rdi
00919B0B  48 8B CB                        mov rcx, rbx
00919B0E  E8 0D 09 00 00                  call 0x14091a420
00919B13  4C 8B 6D 00                     mov r13, qword ptr [rbp]
00919B17  4C 8B 75 F0                     mov r14, qword ptr [rbp - 0x10]
00919B1B  4C 8B 7D E8                     mov r15, qword ptr [rbp - 0x18]
00919B1F  4C 8B 65 E0                     mov r12, qword ptr [rbp - 0x20]
00919B23  E9 A0 FD FF FF                  jmp 0x1409198c8
00919B28  48 8B 83 18 05 00 00            mov rax, qword ptr [rbx + 0x518]
00919B2F  48 85 C0                        test rax, rax
00919B32  74 08                           je 0x140919b3c
00919B34  F0 44 09 80 10 06 00 00         lock or dword ptr [rax + 0x610], r8d
00919B3C  F0 81 A3 10 06 00 00 FF FF BF FF  lock and dword ptr [rbx + 0x610], 0xffbfffff
00919B47  E9 0B FD FF FF                  jmp 0x140919857
00919B4C  48 8B 93 98 04 00 00            mov rdx, qword ptr [rbx + 0x498]
00919B53  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00919B58  41 85 C0                        test r8d, eax
00919B5B  0F 85 E9 FC FF FF               jne 0x14091984a
00919B61  48 8B 8B 18 05 00 00            mov rcx, qword ptr [rbx + 0x518]
00919B68  48 85 C9                        test rcx, rcx
00919B6B  74 19                           je 0x140919b86
00919B6D  F7 81 10 06 00 00 00 10 00 00   test dword ptr [rcx + 0x610], 0x1000
00919B77  74 0D                           je 0x140919b86
00919B79  44 39 B9 28 04 00 00            cmp dword ptr [rcx + 0x428], r15d
00919B80  0F 85 C4 FC FF FF               jne 0x14091984a
00919B86  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00919B8B  48 85 C9                        test rcx, rcx
00919B8E  0F 84 B6 FC FF FF               je 0x14091984a
00919B94  F0 44 09 81 10 06 00 00         lock or dword ptr [rcx + 0x610], r8d
00919B9C  E9 A9 FC FF FF                  jmp 0x14091984a
00919BA1  48 8B D7                        mov rdx, rdi
00919BA4  48 8B CB                        mov rcx, rbx
00919BA7  E8 0C 09 00 00                  call 0x14091a4b8
00919BAC  48 8B 83 C0 04 00 00            mov rax, qword ptr [rbx + 0x4c0]
00919BB3  48 85 C0                        test rax, rax
00919BB6  74 70                           je 0x140919c28
00919BB8  09 70 04                        or dword ptr [rax + 4], esi
00919BBB  48 8B 83 C0 04 00 00            mov rax, qword ptr [rbx + 0x4c0]
00919BC2  48 83 C0 48                     add rax, 0x48
00919BC6  0F BA E6 10                     bt esi, 0x10
00919BCA  0F 82 29 01 00 00               jb 0x140919cf9
00919BD0  0F BA E6 11                     bt esi, 0x11
00919BD4  0F 82 27 01 00 00               jb 0x140919d01
00919BDA  40 F6 C6 04                     test sil, 4
00919BDE  0F 85 26 01 00 00               jne 0x140919d0a
00919BE4  0F BA E6 09                     bt esi, 9
00919BE8  73 04                           jae 0x140919bee
00919BEA  4C 89 68 20                     mov qword ptr [rax + 0x20], r13
00919BEE  0F BA E6 0F                     bt esi, 0xf
00919BF2  73 08                           jae 0x140919bfc
00919BF4  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00919BF8  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00919BFC  4C 8D 45 08                     lea r8, [rbp + 8]
00919C00  33 C9                           xor ecx, ecx
00919C02  4C 2B C0                        sub r8, rax
00919C05  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00919C09  4C 2B C8                        sub r9, rax
00919C0C  48 8D 50 34                     lea rdx, [rax + 0x34]
00919C10  E8 E7 07 00 00                  call 0x14091a3fc
00919C15  85 C6                           test esi, eax
00919C17  0F 85 F6 00 00 00               jne 0x140919d13
00919C1D  FF C1                           inc ecx
00919C1F  48 83 C2 04                     add rdx, 4
00919C23  83 F9 03                        cmp ecx, 3
00919C26  7C E8                           jl 0x140919c10
00919C28  48 83 BB 28 02 00 00 00         cmp qword ptr [rbx + 0x228], 0
00919C30  74 1B                           je 0x140919c4d
00919C32  F7 83 50 04 00 00 00 08 00 00   test dword ptr [rbx + 0x450], 0x800
00919C3C  0F 95 C1                        setne cl
00919C3F  F6 83 10 06 00 00 04            test byte ptr [rbx + 0x610], 4
00919C46  0F 94 C0                        sete al
00919C49  84 C8                           test al, cl
00919C4B  75 46                           jne 0x140919c93
00919C4D  48 8B D7                        mov rdx, rdi
00919C50  48 8B CB                        mov rcx, rbx
00919C53  E8 A8 01 00 00                  call 0x140919e00
00919C58  E9 A7 FC FF FF                  jmp 0x140919904
00919C5D  4C 3B C1                        cmp r8, rcx
00919C60  0F 83 A0 FE FF FF               jae 0x140919b06
00919C66  0F BA E8 0F                     bts eax, 0xf
00919C6A  E9 97 FE FF FF                  jmp 0x140919b06
00919C6F  41 8B 04 12                     mov eax, dword ptr [r10 + rdx]
00919C73  39 42 F4                        cmp dword ptr [rdx - 0xc], eax
00919C76  0F 85 73 FC FF FF               jne 0x1409198ef
00919C7C  39 0A                           cmp dword ptr [rdx], ecx
00919C7E  0F 82 6B FC FF FF               jb 0x1409198ef
00919C84  41 8B C8                        mov ecx, r8d
00919C87  E8 70 07 00 00                  call 0x14091a3fc
00919C8C  0B F0                           or esi, eax
00919C8E  E9 5C FC FF FF                  jmp 0x1409198ef
00919C93  BA 0B 00 00 00                  mov edx, 0xb
00919C98  48 8B CB                        mov rcx, rbx
00919C9B  E8 34 D5 FF FF                  call 0x1409171d4
00919CA0  EB AB                           jmp 0x140919c4d
00919CA2  48 8B 8B E8 00 00 00            mov rcx, qword ptr [rbx + 0xe8]
00919CA9  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00919CAE  E9 6E FB FF FF                  jmp 0x140919821
00919CB3  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00919CB7  49 03 CE                        add rcx, r14
00919CBA  49 3B CC                        cmp rcx, r12
00919CBD  0F 47 F2                        cmova esi, edx
00919CC0  E9 D2 FB FF FF                  jmp 0x140919897
00919CC5  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00919CC9  49 03 CD                        add rcx, r13
00919CCC  49 3B CF                        cmp rcx, r15
00919CCF  0F 86 CF FB FF FF               jbe 0x1409198a4
00919CD5  0F BA EE 11                     bts esi, 0x11
00919CD9  E9 C6 FB FF FF                  jmp 0x1409198a4
00919CDE  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00919CE3  48 03 4C 24 78                  add rcx, qword ptr [rsp + 0x78]
00919CE8  49 3B CE                        cmp rcx, r14
00919CEB  0F 86 C0 FB FF FF               jbe 0x1409198b1
00919CF1  83 CE 04                        or esi, 4
00919CF4  E9 B8 FB FF FF                  jmp 0x1409198b1
00919CF9  4C 89 20                        mov qword ptr [rax], r12
00919CFC  E9 CF FE FF FF                  jmp 0x140919bd0
00919D01  4C 89 78 08                     mov qword ptr [rax + 8], r15
00919D05  E9 D0 FE FF FF                  jmp 0x140919bda
00919D0A  4C 89 70 10                     mov qword ptr [rax + 0x10], r14
00919D0E  E9 D1 FE FF FF                  jmp 0x140919be4
00919D13  41 8B 44 10 CC                  mov eax, dword ptr [r8 + rdx - 0x34]
00919D18  89 42 F4                        mov dword ptr [rdx - 0xc], eax
00919D1B  41 8B 04 11                     mov eax, dword ptr [r9 + rdx]
00919D1F  89 02                           mov dword ptr [rdx], eax
00919D21  E9 F7 FE FF FF                  jmp 0x140919c1d
00919D26  8B 81 F0 01 00 00               mov eax, dword ptr [rcx + 0x1f0]
00919D2C  41 84 C6                        test r14b, al
00919D2F  0F 85 83 7D 20 00               jne 0x140b21ab8
00919D35  F0 83 A1 F0 01 00 00 DF         lock and dword ptr [rcx + 0x1f0], 0xffffffdf
00919D3D  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00919D41  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00919D46  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
00919D4A  45 8B CF                        mov r9d, r15d
00919D4D  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00919D52  41 B8 0E 00 00 00               mov r8d, 0xe
00919D58  48 C7 44 24 60 02 00 00 00      mov qword ptr [rsp + 0x60], 2
00919D61  48 8B 81 D0 01 00 00            mov rax, qword ptr [rcx + 0x1d0]
00919D68  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00919D6D  E8 16 D5 FE FF                  call 0x140907288
00919D72  90                              nop
00919D73  E9 40 7D 20 00                  jmp 0x140b21ab8
00919D78  33 C9                           xor ecx, ecx
00919D7A  E8 31 B6 E6 FF                  call 0x1407853b0
00919D7F  44 88 76 38                     mov byte ptr [rsi + 0x38], r14b
00919D83  E9 DB FB FF FF                  jmp 0x140919963
00919D88  48 8B CB                        mov rcx, rbx
00919D8B  E8 20 B6 E6 FF                  call 0x1407853b0
00919D90  E9 CE FB FF FF                  jmp 0x140919963
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspEnforceLimitsJobPostCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 5181437)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r15 = 0;
    v_stack_m140 = a2;
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) != 0) {
    }
    a1 = (a1) + (56);
    result = ExAcquireResourceSharedLite(a1, 1, a3, a4);
    if (*(unsigned __int64 *)(a1 + 1216) != 0) goto loc_00919A8F;
    a2 = 0;
    result = memset(v_stack_m88, a2, 1 + 63, a4);
loc_0091979D:
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm0;
    v_stack_m120 = *(unsigned __int64 *)(a1 + 160);
    v_stack_m118 = *(unsigned __int64 *)(a1 + 184);
    v_stack_m148 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 548)));
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 256)))) & (4)) != 0) goto loc_00919CA2;
    v_stack_m138 = 0;
loc_00919821:
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    if (condition_is_above_or_equal) goto loc_0091984A;
    if ((*(unsigned int *)(a1 + 1064)) != 0) goto loc_00919B4C;
loc_0091984A:
    if (((*(unsigned int *)(a1 + 1552)) & ((unsigned int)((unsigned int)(0x400000ULL)))) != 0) goto loc_00919B28;
loc_00919857:
    result = ExReleaseResourceLite(a1 + 56, a2, (unsigned int)(0x400000ULL), a4);
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) == 0) goto loc_00919882;
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) != 0) goto loc_00919882;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(a1 + 56, a2, (unsigned int)(0x400000ULL), a4);
    }
    if (v_stack_m88 != 0) goto loc_00919CB3;
loc_00919897:
    if (v_stack_m80 != 0) goto loc_00919CC5;
loc_009198A4:
    if (v_stack_m78 != 0) goto loc_00919CDE;
loc_009198B1:
    if (v_stack_m68 != 0) goto loc_00919AB4;
    if (v_stack_m70 != v_stack_m68) goto loc_00919AB4;
loc_009198C8:
    a3 = 0;
    a4 = (v_stack_m60) - (v_stack_m140);
    v_r10 = (v_stack_m80) - (v_stack_m140);
loc_009198E2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_stack_m140 + 44 * 1 - 44))) != 0) goto loc_00919C6F;
loc_009198EF:
    a3 = (unsigned int)((a3) + 1);
    a2 = (v_stack_m140 + 44) + (4);
    if (((unsigned int)(a3)) < 3) goto loc_009198E2;
    if (0 != 0) goto loc_00919BA1;
loc_00919904:
    if (*(unsigned __int64 *)(v_stack_m140 + 16) != 0) goto loc_00919D26;
    a1 = (v_stack_m130) + (*(unsigned __int64 *)(v_stack_m140 + 24));
    *(unsigned __int64 *)(v_stack_m140 + 24) = a1;
    if ((*(unsigned __int8 *)(v_stack_m140 + 56)) != 0) goto loc_00919963;
    if (a1 >= ((unsigned int)(*(unsigned int *)(v_rip + 6993943)))) goto loc_00919D78;
    if (v_stack_m128 >= ((unsigned int)(*(unsigned int *)(v_rip + 6993924)))) goto loc_00919D88;
loc_00919963:
    if (*(unsigned __int64 *)(a1 + 1304) == 0) goto loc_00919A57;
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) != 0) {
    }
    a1 = (*(unsigned __int64 *)(a1 + 1304)) + (56);
    result = ExAcquireResourceExclusiveLite(a1, 1, a3, a4);
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) != 0) {
    }
    result = ExAcquireResourceExclusiveLite(a1 + 56, 1, a3, a4);
    a1 = (*(unsigned __int64 *)(a1 + 1304)) + (0x548ULL);
    result = PspAddAccountingValues(a1, a1 + 1352, a3, a1 + 1352);
    a2 = 0;
    result = memset(a1 + 1352, a2, a2 + 104, a1 + 1352);
    result = ExReleaseResourceLite(a1 + 56, a2, a2 + 104, a1 + 1352);
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) == 0) goto loc_009199FB;
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) != 0) goto loc_009199FB;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(a1 + 56, a2, a2 + 104, a1 + 1352);
    }
    a1 = (*(unsigned __int64 *)(a1 + 1304)) + (56);
    result = ExReleaseResourceLite(a1, a2, a2 + 104, a1 + 1352);
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) == 0) goto loc_00919A2D;
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) != 0) goto loc_00919A2D;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(a1, a2, a2 + 104, a1 + 1352);
    }
    result = 0;
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a2 + 104, a1 + 1352);
    v_rsp = (v_rsp) + (304);
    return result;
loc_00919A57:
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) != 0) {
    }
    result = ExAcquireResourceExclusiveLite(v_stack_p18 + 56, 1, a2 + 104, a1 + 1352);
    a2 = 0;
    result = memset(v_stack_p18 + 1352, a2, a2 + 104, a1 + 1352);
    result = PspUnlockJob(v_stack_p18, *(unsigned __int64 *)(gs_base + (0 + 392)), a2 + 104, a1 + 1352);
    goto loc_00919A2D;
loc_00919A8F:
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm1;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm1;
    goto loc_0091979D;
loc_00919AB4:
    result = PspLockJobMemoryLimitsShared(v_stack_p18, *(unsigned __int64 *)(gs_base + (0 + 392)), a2 + 104, a1 + 1352);
    a3 = *(unsigned __int64 *)(v_stack_p18 + 1208) + *(unsigned __int64 *)(v_stack_p18 + 1568) * 1;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 1216))) & (0x200000ULL)) == 0) { a3 = *(unsigned __int64 *)(v_stack_p18 + 1208); }
    result = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 1216) + 40) != 0) {
        a1 = 512;
        if (a3 > (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 1216) + 40))) { result = (unsigned int)(a1); }
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 1216) + 32) != 0) goto loc_00919C5D;
loc_00919B06:
    v_rsi = (unsigned int)((v_stack_m140) | ((unsigned int)(result)));
    result = PspUnlockJobMemoryLimitsShared(v_stack_p18, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, *(unsigned __int64 *)(v_stack_p18 + 1216));
    goto loc_009198C8;
loc_00919B28:
    if (*(unsigned __int64 *)(v_stack_p18 + 1304) != 0) {
    }
    goto loc_00919857;
loc_00919B4C:
    v_stack_p40 = *(unsigned __int64 *)(v_stack_p18 + 1176);
    if ((((unsigned int)(a3)) & ((unsigned int)(*(unsigned __int64 *)(v_stack_p18 + 1304)))) != 0) goto loc_0091984A;
    if (*(unsigned __int64 *)(v_stack_p18 + 1304) == 0) goto loc_00919B86;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 1304) + 1552)) & (0x1000ULL)) == 0) goto loc_00919B86;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 1304) + 1064)) != ((unsigned int)(v_stack_m80))) goto loc_0091984A;
loc_00919B86:
    v_stack_p38 = *(unsigned __int64 *)(v_stack_p18 + 1176);
    if (*(unsigned __int64 *)(v_stack_p18 + 1304) == 0) goto loc_0091984A;
    goto loc_0091984A;
loc_00919BA1:
    result = PspLockJobExclusive(v_stack_p18, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, *(unsigned __int64 *)(v_stack_p18 + 1216));
    if (*(unsigned __int64 *)(v_stack_p18 + 1216) == 0) goto loc_00919C28;
    result = (*(unsigned __int64 *)(v_stack_p18 + 1216)) + (72);
    if (condition_is_below) goto loc_00919CF9;
loc_00919BD0:
    if (condition_is_below) goto loc_00919D01;
loc_00919BDA:
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) goto loc_00919D0A;
loc_00919BE4:
    if (!(condition_is_above_or_equal)) {
        *(unsigned __int64 *)(result + 32) = v_stack_m68;
    }
    if (!(condition_is_above_or_equal)) {
        a1 = v_stack_m70;
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a1 = 0;
    a3 = (v_stack_m60) - (result);
    a4 = (v_stack_m88) - (result);
loc_00919C10:
    result = PspRateControlLimitFlag(a1, result + 52, a3, a4);
    if ((((unsigned int)(v_rsi)) & ((unsigned int)(result))) != 0) goto loc_00919D13;
loc_00919C1D:
    a1 = (unsigned int)((a1) + 1);
    a2 = (result + 52) + (4);
    if (((unsigned int)(a1)) < 3) goto loc_00919C10;
loc_00919C28:
    if ((*(unsigned __int64 *)(v_stack_p18 + 552)) == 0) goto loc_00919C4D;
    a1 = (((*(unsigned int *)(v_stack_p18 + 1104)) & (0x800ULL)) != 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(v_stack_p18 + 1552)) & (4)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00919C93;
loc_00919C4D:
    result = PspUnlockJob(v_stack_p18, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    goto loc_00919904;
loc_00919C5D:
    if (a3 >= v_stack_p18) goto loc_00919B06;
    goto loc_00919B06;
loc_00919C6F:
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) - 12)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + *(unsigned __int64 *)(gs_base + (0 + 392)) * 1))))) goto loc_009198EF;
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) < ((unsigned int)(v_stack_p18))) goto loc_009198EF;
    result = PspRateControlLimitFlag((unsigned int)((unsigned int)(a3)), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    v_rsi = (unsigned int)((v_rsi) | ((unsigned int)(result)));
    goto loc_009198EF;
loc_00919C93:
    result = PspSendReliableJobNotification(v_stack_p18, 11, a3, a4);
    goto loc_00919C4D;
loc_00919CA2:
    v_stack_p30 = *(unsigned __int64 *)(v_stack_p18 + 232);
    goto loc_00919821;
loc_00919CB3:
    a1 = (v_stack_mB8) + (v_stack_m78);
    if (a1 > v_stack_m88) { v_rsi = 11; }
    goto loc_00919897;
loc_00919CC5:
    a1 = (v_stack_mB0) + (v_stack_m68);
    if (a1 <= v_stack_m80) goto loc_009198A4;
    goto loc_009198A4;
loc_00919CDE:
    a1 = (v_stack_p48) + (v_stack_p78);
    if (a1 <= v_stack_m78) goto loc_009198B1;
    v_rsi = (unsigned int)((v_rsi) | (4));
    goto loc_009198B1;
loc_00919CF9:
    *(unsigned __int64 *)(result) = v_stack_m88;
    goto loc_00919BD0;
loc_00919D01:
    *(unsigned __int64 *)(result + 8) = v_stack_m80;
    goto loc_00919BDA;
loc_00919D0A:
    *(unsigned __int64 *)(result + 16) = v_stack_m78;
    goto loc_00919BE4;
loc_00919D13:
    *(unsigned int *)(11 - 12) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 11 * 1 - 52)));
    *(unsigned int *)(11) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 11 * 1)));
    goto loc_00919C1D;
loc_00919D26:
    v_stack_p58 = *(unsigned __int64 *)(v_rsi + 8);
    v_stack_p60 = 2;
    v_stack_p68 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 464);
    result = PspRemoveProcessFromJobChain(*(unsigned __int64 *)(v_rsi + 16), v_stack_p58, 14, (unsigned int)((unsigned int)(v_stack_m80)));
loc_00919D78:
    a1 = 0;
    result = PspSendNoWakeChargeLimitNotification(a1, v_stack_p58, 14, (unsigned int)((unsigned int)(v_stack_m80)));
    *(unsigned __int8 *)(v_rsi + 56) = (unsigned __int8)(v_stack_m78);
    goto loc_00919963;
loc_00919D88:
    result = PspSendNoWakeChargeLimitNotification(v_stack_p18, v_stack_p58, 14, (unsigned int)((unsigned int)(v_stack_m80)));
    goto loc_00919963;
}
```

## 5. (Beta) C Style

```c
int64_t PspEnforceLimitsJobPostCallback(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x4F0FFD)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r15 = 0;
    v_stack_m140 = Arg2;
    if (*(uint64_t *)(gs_base + (0 + 0x188)) != 0) {
    }
    Arg1 = (Arg1) + (56);
    result = ExAcquireResourceSharedLite(Arg1, 1, a3, a4);
    if (*(uint64_t *)(arg1 + 0x4C0) != 0) goto loc_00919A8F;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, 1 + 63, a4);
loc_0091979D:
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm0;
    v_stack_m120 = *(uint64_t *)(arg1 + 0xA0);
    v_stack_m118 = *(uint64_t *)(arg1 + 0xB8);
    v_stack_m148 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x224)));
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x100)))) & (4)) != 0) goto loc_00919CA2;
    v_stack_m138 = 0;
loc_00919821:
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    if (condition_is_above_or_equal) goto loc_0091984A;
    if ((*(uint32_t *)(arg1 + 0x428)) != 0) goto loc_00919B4C;
loc_0091984A:
    if (((*(uint32_t *)(arg1 + 0x610)) & ((uint32_t)((uint32_t)(0x400000ULL)))) != 0) goto loc_00919B28;
loc_00919857:
    result = ExReleaseResourceLite(Arg1 + 56, Arg2, (uint32_t)(0x400000ULL), a4);
    if (*(uint64_t *)(gs_base + (0 + 0x188)) == 0) goto loc_00919882;
    if (*(uint64_t *)(gs_base + (0 + 0x188)) != 0) goto loc_00919882;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(Arg1 + 56, Arg2, (uint32_t)(0x400000ULL), a4);
    }
    if (v_stack_m88 != 0) goto loc_00919CB3;
loc_00919897:
    if (v_stack_m80 != 0) goto loc_00919CC5;
loc_009198A4:
    if (v_stack_m78 != 0) goto loc_00919CDE;
loc_009198B1:
    if (v_stack_m68 != 0) goto loc_00919AB4;
    if (v_stack_m70 != v_stack_m68) goto loc_00919AB4;
loc_009198C8:
    a3 = 0;
    a4 = (v_stack_m60) - (v_stack_m140);
    local_r10 = (v_stack_m80) - (v_stack_m140);
loc_009198E2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(a4 + v_stack_m140 + 0x2C * 1 - 0x2C))) != 0) goto loc_00919C6F;
loc_009198EF:
    a3 = (uint32_t)((a3) + 1);
    Arg2 = (v_stack_m140 + 44) + (4);
    if (((uint32_t)(a3)) < 3) goto loc_009198E2;
    if (0 != 0) goto loc_00919BA1;
loc_00919904:
    if (*(uint64_t *)(v_stack_m140 + 0x10) != 0) goto loc_00919D26;
    Arg1 = (v_stack_m130) + (*(uint64_t *)(v_stack_m140 + 0x18));
    *(void **)(v_stack_m140 + 0x18) = Arg1;
    if ((*(uint8_t *)(v_stack_m140 + 0x38)) != 0) goto loc_00919963;
    if (Arg1 >= ((uint32_t)(*(uint32_t *)(v_rip + 0x6AB817)))) goto loc_00919D78;
    if (v_stack_m128 >= ((uint32_t)(*(uint32_t *)(v_rip + 0x6AB804)))) goto loc_00919D88;
loc_00919963:
    if (*(uint64_t *)(arg1 + 0x518) == 0) goto loc_00919A57;
    if (*(uint64_t *)(gs_base + (0 + 0x188)) != 0) {
    }
    Arg1 = (*(uint64_t *)(arg1 + 0x518)) + (56);
    result = ExAcquireResourceExclusiveLite(Arg1, 1, a3, a4);
    if (*(uint64_t *)(gs_base + (0 + 0x188)) != 0) {
    }
    result = ExAcquireResourceExclusiveLite(Arg1 + 56, 1, a3, a4);
    Arg1 = (*(uint64_t *)(arg1 + 0x518)) + (0x548ULL);
    result = PspAddAccountingValues(Arg1, Arg1 + 1352, a3, Arg1 + 1352);
    Arg2 = 0;
    result = memset(Arg1 + 1352, Arg2, Arg2 + 104, Arg1 + 1352);
    result = ExReleaseResourceLite(Arg1 + 56, Arg2, Arg2 + 104, Arg1 + 1352);
    if (*(uint64_t *)(gs_base + (0 + 0x188)) == 0) goto loc_009199FB;
    if (*(uint64_t *)(gs_base + (0 + 0x188)) != 0) goto loc_009199FB;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(Arg1 + 56, Arg2, Arg2 + 104, Arg1 + 1352);
    }
    Arg1 = (*(uint64_t *)(arg1 + 0x518)) + (56);
    result = ExReleaseResourceLite(Arg1, Arg2, Arg2 + 104, Arg1 + 1352);
    if (*(uint64_t *)(gs_base + (0 + 0x188)) == 0) goto loc_00919A2D;
    if (*(uint64_t *)(gs_base + (0 + 0x188)) != 0) goto loc_00919A2D;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(Arg1, Arg2, Arg2 + 104, Arg1 + 1352);
    }
    result = 0;
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg2 + 104, Arg1 + 1352);
    local_rsp = (local_rsp) + (304);
    return result;
loc_00919A57:
    if (*(uint64_t *)(gs_base + (0 + 0x188)) != 0) {
    }
    result = ExAcquireResourceExclusiveLite(v_stack_p18 + 56, 1, Arg2 + 104, Arg1 + 1352);
    Arg2 = 0;
    result = memset(v_stack_p18 + 1352, Arg2, Arg2 + 104, Arg1 + 1352);
    result = PspUnlockJob(v_stack_p18, *(uint64_t *)(gs_base + (0 + 0x188)), Arg2 + 104, Arg1 + 1352);
    goto loc_00919A2D;
loc_00919A8F:
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm1;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm1;
    goto loc_0091979D;
loc_00919AB4:
    result = PspLockJobMemoryLimitsShared(v_stack_p18, *(uint64_t *)(gs_base + (0 + 0x188)), Arg2 + 104, Arg1 + 1352);
    a3 = *(uint64_t *)(v_stack_p18 + 0x4B8) + *(uint64_t *)(v_stack_p18 + 0x620) * 1;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x4C0))) & (0x200000ULL)) == 0) { a3 = *(uint64_t *)(v_stack_p18 + 0x4B8); }
    result = 0;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x4C0) + 0x28) != 0) {
        Arg1 = 512;
        if (a3 > (*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x4C0) + 0x28))) { result = (uint32_t)(Arg1); }
    }
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x4C0) + 0x20) != 0) goto loc_00919C5D;
loc_00919B06:
    local_rsi = (uint32_t)((v_stack_m140) | ((uint32_t)(result)));
    result = PspUnlockJobMemoryLimitsShared(v_stack_p18, *(uint64_t *)(gs_base + (0 + 0x188)), a3, *(uint64_t *)(v_stack_p18 + 0x4C0));
    goto loc_009198C8;
loc_00919B28:
    if (*(uint64_t *)(v_stack_p18 + 0x518) != 0) {
    }
    goto loc_00919857;
loc_00919B4C:
    v_stack_p40 = *(uint64_t *)(v_stack_p18 + 0x498);
    if ((((uint32_t)(a3)) & ((uint32_t)(*(uint64_t *)(v_stack_p18 + 0x518)))) != 0) goto loc_0091984A;
    if (*(uint64_t *)(v_stack_p18 + 0x518) == 0) goto loc_00919B86;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x518) + 0x610)) & (0x1000ULL)) == 0) goto loc_00919B86;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x518) + 0x428)) != ((uint32_t)(v_stack_m80))) goto loc_0091984A;
loc_00919B86:
    v_stack_p38 = *(uint64_t *)(v_stack_p18 + 0x498);
    if (*(uint64_t *)(v_stack_p18 + 0x518) == 0) goto loc_0091984A;
    goto loc_0091984A;
loc_00919BA1:
    result = PspLockJobExclusive(v_stack_p18, *(uint64_t *)(gs_base + (0 + 0x188)), a3, *(uint64_t *)(v_stack_p18 + 0x4C0));
    if (*(uint64_t *)(v_stack_p18 + 0x4C0) == 0) goto loc_00919C28;
    result = (*(uint64_t *)(v_stack_p18 + 0x4C0)) + (72);
    if (condition_is_below) goto loc_00919CF9;
loc_00919BD0:
    if (condition_is_below) goto loc_00919D01;
loc_00919BDA:
    if ((((uint8_t)(local_rsi)) & (4)) != 0) goto loc_00919D0A;
loc_00919BE4:
    if (!(condition_is_above_or_equal)) {
        *(uint64_t *)(result + 0x20) = v_stack_m68;
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = v_stack_m70;
        *(void **)(result + 0x18) = Arg1;
    }
    Arg1 = 0;
    a3 = (v_stack_m60) - (result);
    a4 = (v_stack_m88) - (result);
loc_00919C10:
    result = PspRateControlLimitFlag(Arg1, result + 52, a3, a4);
    if ((((uint32_t)(local_rsi)) & ((uint32_t)(result))) != 0) goto loc_00919D13;
loc_00919C1D:
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (result + 52) + (4);
    if (((uint32_t)(Arg1)) < 3) goto loc_00919C10;
loc_00919C28:
    if ((*(uint64_t *)(v_stack_p18 + 0x228)) == 0) goto loc_00919C4D;
    Arg1 = (((*(uint32_t *)(v_stack_p18 + 0x450)) & (0x800ULL)) != 0) ? 1 : 0;
    result = (((*(uint8_t *)(v_stack_p18 + 0x610)) & (4)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00919C93;
loc_00919C4D:
    result = PspUnlockJob(v_stack_p18, *(uint64_t *)(gs_base + (0 + 0x188)), a3, a4);
    goto loc_00919904;
loc_00919C5D:
    if (a3 >= v_stack_p18) goto loc_00919B06;
    goto loc_00919B06;
loc_00919C6F:
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) - 0xC)) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + *(uint64_t *)(gs_base + (0 + 0x188)) * 1))))) goto loc_009198EF;
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) < ((uint32_t)(v_stack_p18))) goto loc_009198EF;
    result = PspRateControlLimitFlag((uint32_t)((uint32_t)(a3)), *(uint64_t *)(gs_base + (0 + 0x188)), a3, a4);
    local_rsi = (uint32_t)((local_rsi) | ((uint32_t)(result)));
    goto loc_009198EF;
loc_00919C93:
    result = PspSendReliableJobNotification(v_stack_p18, 11, a3, a4);
    goto loc_00919C4D;
loc_00919CA2:
    v_stack_p30 = *(uint64_t *)(v_stack_p18 + 0xE8);
    goto loc_00919821;
loc_00919CB3:
    Arg1 = (v_stack_mB8) + (v_stack_m78);
    if (Arg1 > v_stack_m88) { local_rsi = 11; }
    goto loc_00919897;
loc_00919CC5:
    Arg1 = (v_stack_mB0) + (v_stack_m68);
    if (Arg1 <= v_stack_m80) goto loc_009198A4;
    goto loc_009198A4;
loc_00919CDE:
    Arg1 = (v_stack_p48) + (v_stack_p78);
    if (Arg1 <= v_stack_m78) goto loc_009198B1;
    local_rsi = (uint32_t)((local_rsi) | (4));
    goto loc_009198B1;
loc_00919CF9:
    *(uint64_t *)(result) = v_stack_m88;
    goto loc_00919BD0;
loc_00919D01:
    *(uint64_t *)(result + 0x8) = v_stack_m80;
    goto loc_00919BDA;
loc_00919D0A:
    *(uint64_t *)(result + 0x10) = v_stack_m78;
    goto loc_00919BE4;
loc_00919D13:
    *(uint32_t *)(11 - 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(a3 + 0xB * 1 - 0x34)));
    *(uint32_t *)(11) = (uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0xB * 1)));
    goto loc_00919C1D;
loc_00919D26:
    v_stack_p58 = *(uint64_t *)(local_rsi + 0x8);
    v_stack_p60 = 2;
    v_stack_p68 = *(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x1D0);
    result = PspRemoveProcessFromJobChain(*(uint64_t *)(local_rsi + 0x10), v_stack_p58, 14, (uint32_t)((uint32_t)(v_stack_m80)));
loc_00919D78:
    Arg1 = 0;
    result = PspSendNoWakeChargeLimitNotification(Arg1, v_stack_p58, 14, (uint32_t)((uint32_t)(v_stack_m80)));
    *(uint8_t *)(local_rsi + 0x38) = (uint8_t)(v_stack_m78);
    goto loc_00919963;
loc_00919D88:
    result = PspSendNoWakeChargeLimitNotification(v_stack_p18, v_stack_p58, 14, (uint32_t)((uint32_t)(v_stack_m80)));
    goto loc_00919963;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x20` | `128` | `R` |
| `Arg1` | `+ 0x30` | `128` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `128` | `R` |
| `Arg1` | `+ 0x50` | `128` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xE8` | `64` | `R` |
| `Arg1` | `+ 0x100` | `32` | `R` |
| `Arg1` | `+ 0x224` | `32` | `R` |
| `Arg1` | `+ 0x228` | `64` | `R` |
| `Arg1` | `+ 0x260` | `64` | `R` |
| `Arg1` | `+ 0x268` | `64` | `R` |
| `Arg1` | `+ 0x428` | `32` | `R` |
| `Arg1` | `+ 0x450` | `32` | `R` |
| `Arg1` | `+ 0x498` | `64` | `R` |
| `Arg1` | `+ 0x4B8` | `64` | `R` |
| `Arg1` | `+ 0x4C0` | `64` | `R` |
| `Arg1` | `+ 0x518` | `64` | `R` |
| `Arg1` | `+ 0x548` | `64` | `R` |
| `Arg1` | `+ 0x610` | `8` | `R` |
| `Arg1` | `+ 0x610` | `32` | `R` |
| `Arg1` | `+ 0x610` | `32` | `R/W` |
| `Arg1` | `+ 0x620` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00919720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
