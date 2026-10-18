# PopPepWork

- RVA: `0x002BCBC0`–`0x002BD11C` (길이 `1,372` bytes)
- VA: `0x00000001402BCBC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E1AC`
- 디코드: `320`개 명령, `1,372/1,372` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x002BCC11` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002BCC3E` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x002BCC68` → [PopDiagTraceFxDefaultPepWorkerStart](PopDiagTraceFxDefaultPepWorkerStart_function_002BD168.md) (function, `0x002BD168`)
- `0x002BCCE3` → [TRY_ACQUIRE_EXLOCK_EXCLUSIVE](TRY_ACQUIRE_EXLOCK_EXCLUSIVE_function_002BD130.md) (function, `0x002BD130`)
- `0x002BCD99` → [ExpTryAcquireSpinLockExclusiveAtDpcLevelInstrumented](ExpTryAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_002BE6A0.md) (function, `0x002BE6A0`)
- `0x002BCDFD` → [PopPepStartComponentActivatingActivity](PopPepStartComponentActivatingActivity_function_002BE740.md) (function, `0x002BE740`)
- `0x002BCE25` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002BCE4C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002BCE7C` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x002BCE88` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x002BCE96` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x002BCEAE` → [PopDiagTraceFxDefaultPepWorkerEnd](../44/PopDiagTraceFxDefaultPepWorkerEnd_function_004451E8.md) (function, `0x004451E8`)
- `0x002BCF01` → [PopPepStartDevicePowerOnActivity](PopPepStartDevicePowerOnActivity_function_002BE770.md) (function, `0x002BE770`)
- `0x002BCF5E` → [PopPepStartComponentActivatingActivity](PopPepStartComponentActivatingActivity_function_002BE740.md) (function, `0x002BE740`)
- `0x002BCF86` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002BCFB1` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002BCFF4` → [PopPepStartActivity](../24/PopPepStartActivity_function_0024D6E0.md) (function, `0x0024D6E0`)
- `0x002BD004` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002BD04F` → [PopPepStartDevicePowerOffActivity](PopPepStartDevicePowerOffActivity_function_002BE790.md) (function, `0x002BE790`)
- `0x002BD068` → [PopPepStartDevicePowerOnActivity](PopPepStartDevicePowerOnActivity_function_002BE770.md) (function, `0x002BE770`)
- `0x002BD08C` → [PopPepStartDevicePowerOffActivity](PopPepStartDevicePowerOffActivity_function_002BE790.md) (function, `0x002BE790`)
- `0x002BD09A` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002BD0CB` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x002BD0DE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002BD104` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PopFxDispatchPluginWorkOnce](PopFxDispatchPluginWorkOnce_function_002BC69C.md) at `0x002BC789`

### Static image references
- `0x002BCBF1` → RVA `0x00F07678` (`.data`; read)
- `0x002BCC4C` → RVA `0x00E08388` (`.data`; read)
- `0x002BCC53` → RVA `0x00F07680` (`.data`; read)
- `0x002BCC7F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002BCCD2` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002BCD87` → RVA `0x00F0DE58` (`.data`; read)
- `0x002BCDC9` → RVA `0x00001030` (`.rdata`; read)
- `0x002BCDEA` → RVA `0x002BE740` (`PopPepStartComponentActivatingActivity`; read)
- `0x002BCE5E` → RVA `0x00E08388` (`.data`; read/write)
- `0x002BCEEE` → RVA `0x002BE770` (`PopPepStartDevicePowerOnActivity`; read)
- `0x002BD03C` → RVA `0x002BE790` (`PopPepStartDevicePowerOffActivity`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002BCBC0  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
002BCBC5  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
002BCBC9  53                              push rbx
002BCBCA  55                              push rbp
002BCBCB  56                              push rsi
002BCBCC  57                              push rdi
002BCBCD  41 54                           push r12
002BCBCF  41 55                           push r13
002BCBD1  41 56                           push r14
002BCBD3  41 57                           push r15
002BCBD5  48 83 EC 48                     sub rsp, 0x48
002BCBD9  33 C0                           xor eax, eax
002BCBDB  44 8B F1                        mov r14d, ecx
002BCBDE  8B D8                           mov ebx, eax
002BCBE0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002BCBE4  8B F8                           mov edi, eax
002BCBE6  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
002BCBED  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002BCBF1  48 8D 0D 80 AA C4 00            lea rcx, [rip + 0xc4aa80]
002BCBF8  44 8B E8                        mov r13d, eax
002BCBFB  45 33 C0                        xor r8d, r8d
002BCBFE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002BCC07  33 D2                           xor edx, edx
002BCC09  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
002BCC10  90                              nop
002BCC11  E8 1A 36 F5 FF                  call 0x140210230
002BCC16  48 8B F0                        mov rsi, rax
002BCC19  B9 11 00 00 00                  mov ecx, 0x11
002BCC1E  33 C0                           xor eax, eax
002BCC20  F0 48 0F B1 0D 4F AA C4 00      lock cmpxchg qword ptr [rip + 0xc4aa4f], rcx
002BCC29  74 18                           je 0x1402bcc43
002BCC2B  4C 8D 0D 46 AA C4 00            lea r9, [rip + 0xc4aa46]
002BCC32  4C 8B C6                        mov r8, rsi
002BCC35  33 D2                           xor edx, edx
002BCC37  48 8D 0D 3A AA C4 00            lea rcx, [rip + 0xc4aa3a]
002BCC3E  E8 09 38 F5 FF                  call 0x14021044c
002BCC43  48 85 F6                        test rsi, rsi
002BCC46  74 04                           je 0x1402bcc4c
002BCC48  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
002BCC4C  4C 8B 25 35 B7 B4 00            mov r12, qword ptr [rip + 0xb4b735]
002BCC53  48 8D 05 26 AA C4 00            lea rax, [rip + 0xc4aa26]
002BCC5A  4C 3B E0                        cmp r12, rax
002BCC5D  0F 84 85 04 00 00               je 0x1402bd0e8
002BCC63  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
002BCC68  E8 FB 04 00 00                  call 0x1402bd168
002BCC6D  45 0F 20 C7                     mov r15, cr8
002BCC71  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
002BCC76  B8 02 00 00 00                  mov eax, 2
002BCC7B  44 0F 22 C0                     mov cr8, rax
002BCC7F  39 1D 9B A0 D0 00               cmp dword ptr [rip + 0xd0a09b], ebx
002BCC85  0F 85 1F 03 00 00               jne 0x1402bcfaa
002BCC8B  33 C9                           xor ecx, ecx
002BCC8D  8B F1                           mov esi, ecx
002BCC8F  89 B4 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], esi
002BCC96  83 FE 03                        cmp esi, 3
002BCC99  0F 83 43 02 00 00               jae 0x1402bcee2
002BCC9F  41 8B EE                        mov ebp, r14d
002BCCA2  49 8B DC                        mov rbx, r12
002BCCA5  83 E5 01                        and ebp, 1
002BCCA8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002BCCB0  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
002BCCB3  4C 8B E9                        mov r13, rcx
002BCCB6  83 E0 20                        and eax, 0x20
002BCCB9  85 ED                           test ebp, ebp
002BCCBB  0F 85 4D 04 00 00               jne 0x1402bd10e
002BCCC1  48 85 C0                        test rax, rax
002BCCC4  0F 85 93 00 00 00               jne 0x1402bcd5d
002BCCCA  85 F6                           test esi, esi
002BCCCC  0F 85 C4 03 00 00               jne 0x1402bd096
002BCCD2  F6 05 2D 9E D0 00 21            test byte ptr [rip + 0xd09e2d], 0x21
002BCCD9  0F 85 A8 00 00 00               jne 0x1402bcd87
002BCCDF  48 8D 4B 40                     lea rcx, [rbx + 0x40]
002BCCE3  E8 48 04 00 00                  call 0x1402bd130
002BCCE8  85 C0                           test eax, eax
002BCCEA  0F 84 E7 03 00 00               je 0x1402bd0d7
002BCCF0  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
002BCCF4  48 85 C0                        test rax, rax
002BCCF7  74 04                           je 0x1402bccfd
002BCCF9  4C 8B 68 30                     mov r13, qword ptr [rax + 0x30]
002BCCFD  44 8B 43 78                     mov r8d, dword ptr [rbx + 0x78]
002BCD01  4C 8D 53 78                     lea r10, [rbx + 0x78]
002BCD05  45 85 C0                        test r8d, r8d
002BCD08  0F 85 FD 01 00 00               jne 0x1402bcf0b
002BCD0E  8B 93 B4 00 00 00               mov edx, dword ptr [rbx + 0xb4]
002BCD14  45 33 F6                        xor r14d, r14d
002BCD17  41 8B FE                        mov edi, r14d
002BCD1A  3B FA                           cmp edi, edx
002BCD1C  73 1D                           jae 0x1402bcd3b
002BCD1E  8B C7                           mov eax, edi
002BCD20  48 69 F0 D0 00 00 00            imul rsi, rax, 0xd0
002BCD27  48 81 C6 C0 00 00 00            add rsi, 0xc0
002BCD2E  48 03 F3                        add rsi, rbx
002BCD31  44 39 76 68                     cmp dword ptr [rsi + 0x68], r14d
002BCD35  77 6C                           ja 0x1402bcda3
002BCD37  FF C7                           inc edi
002BCD39  EB DF                           jmp 0x1402bcd1a
002BCD3B  45 85 C0                        test r8d, r8d
002BCD3E  0F 85 77 02 00 00               jne 0x1402bcfbb
002BCD44  F6 05 BB 9D D0 00 01            test byte ptr [rip + 0xd09dbb], 1
002BCD4B  0F 85 60 03 00 00               jne 0x1402bd0b1
002BCD51  8B B4 24 A8 00 00 00            mov esi, dword ptr [rsp + 0xa8]
002BCD58  33 C9                           xor ecx, ecx
002BCD5A  89 4B 40                        mov dword ptr [rbx + 0x40], ecx
002BCD5D  48 8B 1B                        mov rbx, qword ptr [rbx]
002BCD60  48 8D 05 19 A9 C4 00            lea rax, [rip + 0xc4a919]
002BCD67  48 3B D8                        cmp rbx, rax
002BCD6A  75 03                           jne 0x1402bcd6f
002BCD6C  48 8B 1B                        mov rbx, qword ptr [rbx]
002BCD6F  49 3B DC                        cmp rbx, r12
002BCD72  0F 85 38 FF FF FF               jne 0x1402bccb0
002BCD78  44 8B B4 24 90 00 00 00         mov r14d, dword ptr [rsp + 0x90]
002BCD80  FF C6                           inc esi
002BCD82  E9 08 FF FF FF                  jmp 0x1402bcc8f
002BCD87  8B 05 CB 10 C5 00               mov eax, dword ptr [rip + 0xc510cb]
002BCD8D  85 C0                           test eax, eax
002BCD8F  0F 85 4A FF FF FF               jne 0x1402bccdf
002BCD95  48 8D 4B 40                     lea rcx, [rbx + 0x40]
002BCD99  E8 02 19 00 00                  call 0x1402be6a0
002BCD9E  E9 45 FF FF FF                  jmp 0x1402bcce8
002BCDA3  41 B8 01 00 00 00               mov r8d, 1
002BCDA9  48 8D 4E 40                     lea rcx, [rsi + 0x40]
002BCDAD  41 83 F8 03                     cmp r8d, 3
002BCDB1  0F 8F E8 01 00 00               jg 0x1402bcf9f
002BCDB7  48 8B 01                        mov rax, qword ptr [rcx]
002BCDBA  8B 10                           mov edx, dword ptr [rax]
002BCDBC  F6 C2 02                        test dl, 2
002BCDBF  0F 84 08 01 00 00               je 0x1402bcecd
002BCDC5  F0 FF 4E 68                     lock dec dword ptr [rsi + 0x68]
002BCDC9  48 8D 0D 60 42 D4 FF            lea rcx, [rip - 0x2bbda0]
002BCDD0  49 63 E8                        movsxd rbp, r8d
002BCDD3  48 8B D6                        mov rdx, rsi
002BCDD6  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
002BCDDE  48 69 C5 88 00 00 00            imul rax, rbp, 0x88
002BCDE5  48 8B 44 08 78                  mov rax, qword ptr [rax + rcx + 0x78]
002BCDEA  48 8D 0D 4F 19 00 00            lea rcx, [rip + 0x194f]
002BCDF1  48 3B C1                        cmp rax, rcx
002BCDF4  0F 85 F4 00 00 00               jne 0x1402bceee
002BCDFA  48 8B CB                        mov rcx, rbx
002BCDFD  E8 3E 19 00 00                  call 0x1402be740
002BCE02  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
002BCE09  48 8D 4B 40                     lea rcx, [rbx + 0x40]
002BCE0D  48 8B 44 EE 38                  mov rax, qword ptr [rsi + rbp*8 + 0x38]
002BCE12  83 20 FD                        and dword ptr [rax], 0xfffffffd
002BCE15  48 8B 44 EE 38                  mov rax, qword ptr [rsi + rbp*8 + 0x38]
002BCE1A  83 20 F7                        and dword ptr [rax], 0xfffffff7
002BCE1D  48 8B 44 EE 38                  mov rax, qword ptr [rsi + rbp*8 + 0x38]
002BCE22  83 08 04                        or dword ptr [rax], 4
002BCE25  E8 B6 C9 F8 FF                  call 0x1402497e0
002BCE2A  8B B4 24 A8 00 00 00            mov esi, dword ptr [rsp + 0xa8]
002BCE31  BD 02 00 00 00                  mov ebp, 2
002BCE36  83 3D E3 9E D0 00 00            cmp dword ptr [rip + 0xd09ee3], 0
002BCE3D  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
002BCE42  74 0D                           je 0x1402bce51
002BCE44  44 0F 20 C1                     mov rcx, cr8
002BCE48  41 0F B6 D7                     movzx edx, r15b
002BCE4C  E8 47 88 23 00                  call 0x1404f5698
002BCE51  41 0F B6 CF                     movzx ecx, r15b
002BCE55  44 0F 22 C1                     mov cr8, rcx
002BCE59  49 3B DC                        cmp rbx, r12
002BCE5C  74 07                           je 0x1402bce65
002BCE5E  48 87 1D 23 B5 B4 00            xchg qword ptr [rip + 0xb4b523], rbx
002BCE65  B8 11 00 00 00                  mov eax, 0x11
002BCE6A  F0 4C 0F B1 35 05 A8 C4 00      lock cmpxchg qword ptr [rip + 0xc4a805], r14
002BCE73  74 0C                           je 0x1402bce81
002BCE75  48 8D 0D FC A7 C4 00            lea rcx, [rip + 0xc4a7fc]
002BCE7C  E8 BF 65 FA FF                  call 0x140263440
002BCE81  48 8D 0D F0 A7 C4 00            lea rcx, [rip + 0xc4a7f0]
002BCE88  E8 73 47 02 00                  call 0x1402e1600
002BCE8D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002BCE96  E8 55 21 FA FF                  call 0x14025eff0
002BCE9B  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002BCE9F  44 8B CE                        mov r9d, esi
002BCEA2  44 8B C7                        mov r8d, edi
002BCEA5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002BCEA9  8B D5                           mov edx, ebp
002BCEAB  49 8B CD                        mov rcx, r13
002BCEAE  E8 35 83 18 00                  call 0x1404451e8
002BCEB3  0F B6 84 24 A0 00 00 00         movzx eax, byte ptr [rsp + 0xa0]
002BCEBB  48 83 C4 48                     add rsp, 0x48
002BCEBF  41 5F                           pop r15
002BCEC1  41 5E                           pop r14
002BCEC3  41 5D                           pop r13
002BCEC5  41 5C                           pop r12
002BCEC7  5F                              pop rdi
002BCEC8  5E                              pop rsi
002BCEC9  5D                              pop rbp
002BCECA  5B                              pop rbx
002BCECB  C3                              ret
002BCECC  CC                              int3
002BCECD  F6 C2 08                        test dl, 8
002BCED0  0F 85 EF FE FF FF               jne 0x1402bcdc5
002BCED6  41 FF C0                        inc r8d
002BCED9  48 83 C1 08                     add rcx, 8
002BCEDD  E9 CB FE FF FF                  jmp 0x1402bcdad
002BCEE2  8B 6C 24 34                     mov ebp, dword ptr [rsp + 0x34]
002BCEE6  45 33 F6                        xor r14d, r14d
002BCEE9  E9 48 FF FF FF                  jmp 0x1402bce36
002BCEEE  48 8D 0D 7B 18 00 00            lea rcx, [rip + 0x187b]
002BCEF5  48 3B C1                        cmp rax, rcx
002BCEF8  0F 85 3E 01 00 00               jne 0x1402bd03c
002BCEFE  48 8B CB                        mov rcx, rbx
002BCF01  E8 6A 18 00 00                  call 0x1402be770
002BCF06  E9 F7 FE FF FF                  jmp 0x1402bce02
002BCF0B  33 C9                           xor ecx, ecx
002BCF0D  4C 8D 4B 48                     lea r9, [rbx + 0x48]
002BCF11  85 C9                           test ecx, ecx
002BCF13  0F 8F F5 FD FF FF               jg 0x1402bcd0e
002BCF19  49 8B 01                        mov rax, qword ptr [r9]
002BCF1C  8B 10                           mov edx, dword ptr [rax]
002BCF1E  F6 C2 02                        test dl, 2
002BCF21  0F 84 F3 00 00 00               je 0x1402bd01a
002BCF27  F0 41 FF 0A                     lock dec dword ptr [r10]
002BCF2B  33 D2                           xor edx, edx
002BCF2D  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
002BCF35  48 63 F1                        movsxd rsi, ecx
002BCF38  48 8D 0D F1 40 D4 FF            lea rcx, [rip - 0x2bbf0f]
002BCF3F  48 69 C6 88 00 00 00            imul rax, rsi, 0x88
002BCF46  48 8B 44 08 78                  mov rax, qword ptr [rax + rcx + 0x78]
002BCF4B  48 8D 0D EE 17 00 00            lea rcx, [rip + 0x17ee]
002BCF52  48 3B C1                        cmp rax, rcx
002BCF55  0F 85 FE 00 00 00               jne 0x1402bd059
002BCF5B  48 8B CB                        mov rcx, rbx
002BCF5E  E8 DD 17 00 00                  call 0x1402be740
002BCF63  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
002BCF6A  48 8D 4B 40                     lea rcx, [rbx + 0x40]
002BCF6E  48 8B 44 F3 48                  mov rax, qword ptr [rbx + rsi*8 + 0x48]
002BCF73  83 20 FD                        and dword ptr [rax], 0xfffffffd
002BCF76  48 8B 44 F3 48                  mov rax, qword ptr [rbx + rsi*8 + 0x48]
002BCF7B  83 20 F7                        and dword ptr [rax], 0xfffffff7
002BCF7E  48 8B 44 F3 48                  mov rax, qword ptr [rbx + rsi*8 + 0x48]
002BCF83  83 08 04                        or dword ptr [rax], 4
002BCF86  E8 55 C8 F8 FF                  call 0x1402497e0
002BCF8B  8B B4 24 A8 00 00 00            mov esi, dword ptr [rsp + 0xa8]
002BCF92  45 33 F6                        xor r14d, r14d
002BCF95  BD 01 00 00 00                  mov ebp, 1
002BCF9A  E9 97 FE FF FF                  jmp 0x1402bce36
002BCF9F  41 B8 06 00 00 00               mov r8d, 6
002BCFA5  E9 1B FE FF FF                  jmp 0x1402bcdc5
002BCFAA  0F B6 D0                        movzx edx, al
002BCFAD  41 0F B6 CF                     movzx ecx, r15b
002BCFB1  E8 46 87 23 00                  call 0x1404f56fc
002BCFB6  E9 D0 FC FF FF                  jmp 0x1402bcc8b
002BCFBB  41 B9 04 00 00 00               mov r9d, 4
002BCFC1  48 8D 4B 68                     lea rcx, [rbx + 0x68]
002BCFC5  41 83 F9 05                     cmp r9d, 5
002BCFC9  0F 8F A3 00 00 00               jg 0x1402bd072
002BCFCF  48 8B 01                        mov rax, qword ptr [rcx]
002BCFD2  8B 10                           mov edx, dword ptr [rax]
002BCFD4  F6 C2 02                        test dl, 2
002BCFD7  74 55                           je 0x1402bd02e
002BCFD9  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
002BCFE1  4C 8D 43 48                     lea r8, [rbx + 0x48]
002BCFE5  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002BCFEA  33 D2                           xor edx, edx
002BCFEC  48 8B CB                        mov rcx, rbx
002BCFEF  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
002BCFF4  E8 E7 06 F9 FF                  call 0x14024d6e0
002BCFF9  48 8D 4B 40                     lea rcx, [rbx + 0x40]
002BCFFD  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
002BD004  E8 D7 C7 F8 FF                  call 0x1402497e0
002BD009  8B B4 24 A8 00 00 00            mov esi, dword ptr [rsp + 0xa8]
002BD010  BD 03 00 00 00                  mov ebp, 3
002BD015  E9 1C FE FF FF                  jmp 0x1402bce36
002BD01A  F6 C2 08                        test dl, 8
002BD01D  0F 85 04 FF FF FF               jne 0x1402bcf27
002BD023  FF C1                           inc ecx
002BD025  49 83 C1 08                     add r9, 8
002BD029  E9 E3 FE FF FF                  jmp 0x1402bcf11
002BD02E  F6 C2 08                        test dl, 8
002BD031  75 A6                           jne 0x1402bcfd9
002BD033  41 FF C1                        inc r9d
002BD036  48 83 C1 08                     add rcx, 8
002BD03A  EB 89                           jmp 0x1402bcfc5
002BD03C  48 8D 0D 4D 17 00 00            lea rcx, [rip + 0x174d]
002BD043  48 3B C1                        cmp rax, rcx
002BD046  48 8B CB                        mov rcx, rbx
002BD049  0F 85 8F 00 00 00               jne 0x1402bd0de
002BD04F  E8 3C 17 00 00                  call 0x1402be790
002BD054  E9 A9 FD FF FF                  jmp 0x1402bce02
002BD059  48 8D 0D 10 17 00 00            lea rcx, [rip + 0x1710]
002BD060  48 3B C1                        cmp rax, rcx
002BD063  75 18                           jne 0x1402bd07d
002BD065  48 8B CB                        mov rcx, rbx
002BD068  E8 03 17 00 00                  call 0x1402be770
002BD06D  E9 F1 FE FF FF                  jmp 0x1402bcf63
002BD072  41 B9 06 00 00 00               mov r9d, 6
002BD078  E9 5C FF FF FF                  jmp 0x1402bcfd9
002BD07D  48 8D 0D 0C 17 00 00            lea rcx, [rip + 0x170c]
002BD084  48 3B C1                        cmp rax, rcx
002BD087  48 8B CB                        mov rcx, rbx
002BD08A  75 78                           jne 0x1402bd104
002BD08C  E8 FF 16 00 00                  call 0x1402be790
002BD091  E9 CD FE FF FF                  jmp 0x1402bcf63
002BD096  48 8D 4B 40                     lea rcx, [rbx + 0x40]
002BD09A  E8 E1 BD F8 FF                  call 0x140248e80
002BD09F  83 FE 02                        cmp esi, 2
002BD0A2  0F 85 48 FC FF FF               jne 0x1402bccf0
002BD0A8  FF 44 24 30                     inc dword ptr [rsp + 0x30]
002BD0AC  E9 3F FC FF FF                  jmp 0x1402bccf0
002BD0B1  8B 05 A1 0D C5 00               mov eax, dword ptr [rip + 0xc50da1]
002BD0B7  85 C0                           test eax, eax
002BD0B9  0F 85 92 FC FF FF               jne 0x1402bcd51
002BD0BF  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
002BD0C7  48 8D 4B 40                     lea rcx, [rbx + 0x40]
002BD0CB  E8 74 3E 00 00                  call 0x1402c0f44
002BD0D0  8B B4 24 A8 00 00 00            mov esi, dword ptr [rsp + 0xa8]
002BD0D7  33 C9                           xor ecx, ecx
002BD0D9  E9 7F FC FF FF                  jmp 0x1402bcd5d
002BD0DE  E8 ED D9 3F 00                  call 0x1406baad0
002BD0E3  E9 1A FD FF FF                  jmp 0x1402bce02
002BD0E8  49 8B 0C 24                     mov rcx, qword ptr [r12]
002BD0EC  49 8B C4                        mov rax, r12
002BD0EF  F0 48 0F B1 0D 90 B2 B4 00      lock cmpxchg qword ptr [rip + 0xb4b290], rcx
002BD0F8  4C 8B 25 89 B2 B4 00            mov r12, qword ptr [rip + 0xb4b289]
002BD0FF  E9 5F FB FF FF                  jmp 0x1402bcc63
002BD104  E8 C7 D9 3F 00                  call 0x1406baad0
002BD109  E9 55 FE FF FF                  jmp 0x1402bcf63
002BD10E  48 85 C0                        test rax, rax
002BD111  0F 84 46 FC FF FF               je 0x1402bcd5d
002BD117  E9 AE FB FF FF                  jmp 0x1402bccca
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPepWork(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p98;
    unsigned __int8 v_stack_pA0;
    unsigned int v_stack_pA8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (72);
    result = 0;
    v_stack_m58 = 0;
    v_stack_p18 = 0;
    v_stack_m54 = 0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 12888704, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 12888646;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 12888634;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_rip + 11843381)) == (v_rip + 12888614)) goto loc_002BD0E8;
loc_002BCC63:
    result = PopDiagTraceFxDefaultPepWorkerStart(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11843381) + 32), a2, a3, a4);
    v_stack_m50 = v_cr8;
    if ((*(unsigned int *)(v_rip + 13672603)) != 0) goto loc_002BCFAA;
loc_002BCC8B:
    a1 = 0;
loc_002BCC8F:
    v_stack_p20 = 0;
    if (0 >= 3) goto loc_002BCEE2;
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) & (1));
loc_002BCCB0:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11843381) + 24))) & (32));
    if ((unsigned int)(v_rbp) != 0) goto loc_002BD10E;
    if (result != 0) goto loc_002BCD5D;
loc_002BCCCA:
    if (0 != 0) goto loc_002BD096;
    if (((*(unsigned __int8 *)(v_rip + 13671981)) & (33)) != 0) goto loc_002BCD87;
loc_002BCCDF:
    result = TRY_ACQUIRE_EXLOCK_EXCLUSIVE(*(unsigned __int64 *)(v_rip + 11843381) + 64, a2, a3, a4);
loc_002BCCE8:
    if ((unsigned int)(result) == 0) goto loc_002BD0D7;
loc_002BCCF0:
    v_r13 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11843381) + 32) != 0) {
        v_r13 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11843381) + 32) + 48);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11843381) + 120))) != 0) goto loc_002BCF0B;
loc_002BCD0E:
    v_r14 = 0;
loc_002BCD1A:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11843381) + 180))))) goto loc_002BCD3B;
    v_rsi = (0) * (0);
    v_rsi = (v_rsi) + (192);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip + 11843381));
    if ((*(unsigned int *)(v_rsi + 104)) > 0) goto loc_002BCDA3;
    v_rdi = (unsigned int)((0) + 1);
    goto loc_002BCD1A;
loc_002BCD3B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11843381) + 120))) != 0) goto loc_002BCFBB;
    if (((*(unsigned __int8 *)(v_rip + 13671867)) & (1)) != 0) goto loc_002BD0B1;
loc_002BCD51:
    a1 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 11843381) + 64) = 0;
loc_002BCD5D:
    v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11843381));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11843381))) == (v_rip + 12888345)) {
        v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11843381)));
    }
    if (v_rbx != (*(unsigned __int64 *)(v_rip + 11843381))) goto loc_002BCCB0;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_p20)) + 1);
    goto loc_002BCC8F;
loc_002BCD87:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12914891))) != 0) goto loc_002BCCDF;
    result = ExpTryAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_rbx + 64, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11843381) + 180)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11843381) + 120)), a4);
    goto loc_002BCCE8;
loc_002BCDA3:
loc_002BCDAD:
    if (1 > 3) goto loc_002BCF9F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 64))))) & (2)) == 0) goto loc_002BCECD;
loc_002BCDC5:
    result = (*(unsigned __int64 *)(v_rsi + 64)) * ((int)(1));
    if ((*(unsigned __int64 *)(result + v_rip - 2866592 * 1 + 120)) != (v_rip + 6479)) goto loc_002BCEEE;
    result = PopPepStartComponentActivatingActivity(v_rbx, v_rsi, v_stack_p10, a4);
loc_002BCE02:
    v_stack_p18 = (unsigned __int8)(result);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rbx + 64, v_rsi, v_stack_p10, a4);
loc_002BCE36:
    if ((*(unsigned int *)(v_rip + 13672163)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m50);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_p10, a4);
    }
    if (v_rbx != (*(unsigned __int64 *)(v_rip + 11843381))) {
    }
    result = 17;
    if (v_rbx != (*(unsigned __int64 *)(v_rip + 11843381))) {
        a1 = v_rip + 12888060;
        result = ExfReleasePushLockShared(a1, a2, v_stack_p10, a4);
    }
    result = KeAbPostRelease(v_rip + 12888048, a2, v_stack_p10, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p10, a4);
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m58));
    result = PopDiagTraceFxDefaultPepWorkerEnd(v_r13, 2, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))));
    v_rsp = (v_rsp) + (72);
    return v_stack_p18;
loc_002BCECD:
    if (((2) & (8)) != 0) goto loc_002BCDC5;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    a1 = (v_r13) + (8);
    goto loc_002BCDAD;
loc_002BCEE2:
    v_r14 = 0;
    goto loc_002BCE36;
loc_002BCEEE:
    if (v_stack_p18 != (v_rip + 6267)) goto loc_002BD03C;
    result = PopPepStartDevicePowerOnActivity(v_rbx, 2, a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))));
    goto loc_002BCE02;
loc_002BCF0B:
    a1 = 0;
loc_002BCF11:
    if (condition_is_greater) goto loc_002BCD0E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 72))))) & (2)) == 0) goto loc_002BD01A;
loc_002BCF27:
    a2 = 0;
    result = (*(unsigned __int64 *)(v_rbx + 72)) * ((int)(0));
    if ((*(unsigned __int64 *)(result + v_rip - 2866959 * 1 + 120)) != (v_rip + 6126)) goto loc_002BD059;
    result = PopPepStartComponentActivatingActivity(v_rbx, a2, v_stack_p98, v_rbx + 72);
loc_002BCF63:
    v_stack_pA0 = (unsigned __int8)(result);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rbx + 64, a2, v_stack_p98, v_rbx + 72);
    v_r14 = 0;
    goto loc_002BCE36;
loc_002BCF9F:
    goto loc_002BCDC5;
loc_002BCFAA:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_m50), (unsigned __int8)(result), 6, v_rbx + 72);
    goto loc_002BCC8B;
loc_002BCFBB:
loc_002BCFC5:
    if (4 > 5) goto loc_002BD072;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 104))))) & (2)) == 0) goto loc_002BD02E;
loc_002BCFD9:
    v_stack_p28 = v_stack_p98;
    a2 = 0;
    v_stack_p20 = *(unsigned __int64 *)(v_rip + 11843381) + 120;
    result = PopPepStartActivity(v_rbx, a2, v_rbx + 72, 4);
    v_stack_pA0 = (unsigned __int8)(result);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rbx + 64, a2, v_rbx + 72, 4);
    goto loc_002BCE36;
loc_002BD01A:
    if (((0) & (8)) != 0) goto loc_002BCF27;
    a1 = (unsigned int)((v_rbx + 64) + 1);
    a4 = (4) + (8);
    goto loc_002BCF11;
loc_002BD02E:
    if (((0) & (8)) != 0) goto loc_002BCFD9;
    a4 = (unsigned int)((a4) + 1);
    a1 = (a1) + (8);
    goto loc_002BCFC5;
loc_002BD03C:
    if (result != (v_rip + 5965)) goto loc_002BD0DE;
    result = PopPepStartDevicePowerOffActivity(v_rbx, a2, v_rbx + 72, a4);
    goto loc_002BCE02;
loc_002BD059:
    if (result != (v_rip + 5904)) goto loc_002BD07D;
    result = PopPepStartDevicePowerOnActivity(v_rbx, a2, v_rbx + 72, a4);
    goto loc_002BCF63;
loc_002BD072:
    goto loc_002BCFD9;
loc_002BD07D:
    if (result != (v_rip + 5900)) goto loc_002BD104;
    result = PopPepStartDevicePowerOffActivity(v_rbx, a2, v_rbx + 72, 6);
    goto loc_002BCF63;
loc_002BD096:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rbx + 64, a2, v_rbx + 72, 6);
    if (((unsigned int)((unsigned int)(v_stack_pA8))) != 2) goto loc_002BCCF0;
    goto loc_002BCCF0;
loc_002BD0B1:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12914081))) != 0) goto loc_002BCD51;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rbx + 64, v_stack_p88, v_rbx + 72, 6);
loc_002BD0D7:
    a1 = 0;
    goto loc_002BCD5D;
loc_002BD0DE:
    result = guard_dispatch_icall(a1, v_stack_p88, v_rbx + 72, 6);
    goto loc_002BCE02;
loc_002BD0E8:
    goto loc_002BCC63;
loc_002BD104:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11843381)), v_stack_p88, v_rbx + 72, 6);
    goto loc_002BCF63;
loc_002BD10E:
    if (result == 0) goto loc_002BCD5D;
    goto loc_002BCCCA;
}
```

## 5. (Beta) C Style

```c
int64_t PopPepWork(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p8;
    uint64_t v_stack_p88;
    uint64_t v_stack_p98;
    uint8_t v_stack_pA0;
    uint32_t v_stack_pA8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (72);
    result = 0;
    v_stack_m58 = 0;
    v_stack_p18 = 0;
    v_stack_m54 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 12888704, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 12888646;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 12888634;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(v_rip + 0xB4B735)) == (v_rip + 12888614)) goto loc_002BD0E8;
loc_002BCC63:
    result = PopDiagTraceFxDefaultPepWorkerStart(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0x20), Arg2, Arg3, a4);
    v_stack_m50 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xD0A09B)) != 0) goto loc_002BCFAA;
loc_002BCC8B:
    Arg1 = 0;
loc_002BCC8F:
    v_stack_p20 = 0;
    if (0 >= 3) goto loc_002BCEE2;
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) & (1));
loc_002BCCB0:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0x18))) & (32));
    if ((uint32_t)(local_rbp) != 0) goto loc_002BD10E;
    if (result != 0) goto loc_002BCD5D;
loc_002BCCCA:
    if (0 != 0) goto loc_002BD096;
    if (((*(uint8_t *)(v_rip + 0xD09E2D)) & (33)) != 0) goto loc_002BCD87;
loc_002BCCDF:
    result = TRY_ACQUIRE_EXLOCK_EXCLUSIVE(*(uint64_t *)(v_rip + 0xB4B735) + 64, Arg2, Arg3, a4);
loc_002BCCE8:
    if ((uint32_t)(result) == 0) goto loc_002BD0D7;
loc_002BCCF0:
    local_r13 = 0;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0x20) != 0) {
        local_r13 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0x20) + 0x30);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0x78))) != 0) goto loc_002BCF0B;
loc_002BCD0E:
    local_r14 = 0;
loc_002BCD1A:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0xB4))))) goto loc_002BCD3B;
    local_rsi = (0) * (0);
    local_rsi = (local_rsi) + (192);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip + 0xB4B735));
    if ((*(uint32_t *)(local_rsi + 0x68)) > 0) goto loc_002BCDA3;
    local_rdi = (uint32_t)((0) + 1);
    goto loc_002BCD1A;
loc_002BCD3B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0x78))) != 0) goto loc_002BCFBB;
    if (((*(uint8_t *)(v_rip + 0xD09DBB)) & (1)) != 0) goto loc_002BD0B1;
loc_002BCD51:
    Arg1 = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0x40) = 0;
loc_002BCD5D:
    local_rbx = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB4B735));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB4B735))) == (v_rip + 12888345)) {
        local_rbx = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB4B735)));
    }
    if (local_rbx != (*(uint64_t *)(v_rip + 0xB4B735))) goto loc_002BCCB0;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_p20)) + 1);
    goto loc_002BCC8F;
loc_002BCD87:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC510CB))) != 0) goto loc_002BCCDF;
    result = ExpTryAcquireSpinLockExclusiveAtDpcLevelInstrumented(local_rbx + 64, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0xB4)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB4B735) + 0x78)), a4);
    goto loc_002BCCE8;
loc_002BCDA3:
loc_002BCDAD:
    if (1 > 3) goto loc_002BCF9F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x40))))) & (2)) == 0) goto loc_002BCECD;
loc_002BCDC5:
    result = (*(uint64_t *)(local_rsi + 0x40)) * ((int32_t)(1));
    if ((*(uint64_t *)(result + v_rip - 0x2BBDA0 * 1 + 0x78)) != (v_rip + 6479)) goto loc_002BCEEE;
    result = PopPepStartComponentActivatingActivity(local_rbx, local_rsi, v_stack_p10, a4);
loc_002BCE02:
    v_stack_p18 = (uint8_t)(result);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(local_rbx + 64, local_rsi, v_stack_p10, a4);
loc_002BCE36:
    if ((*(uint32_t *)(v_rip + 0xD09EE3)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m50);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p10, a4);
    }
    if (local_rbx != (*(uint64_t *)(v_rip + 0xB4B735))) {
    }
    result = 17;
    if (local_rbx != (*(uint64_t *)(v_rip + 0xB4B735))) {
        Arg1 = v_rip + 12888060;
        result = ExfReleasePushLockShared(Arg1, Arg2, v_stack_p10, a4);
    }
    result = KeAbPostRelease(v_rip + 12888048, Arg2, v_stack_p10, a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p10, a4);
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m58));
    result = PopDiagTraceFxDefaultPepWorkerEnd(local_r13, 2, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))));
    local_rsp = (local_rsp) + (72);
    return v_stack_p18;
loc_002BCECD:
    if (((2) & (8)) != 0) goto loc_002BCDC5;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    Arg1 = (local_r13) + (8);
    goto loc_002BCDAD;
loc_002BCEE2:
    local_r14 = 0;
    goto loc_002BCE36;
loc_002BCEEE:
    if (v_stack_p18 != (v_rip + 6267)) goto loc_002BD03C;
    result = PopPepStartDevicePowerOnActivity(local_rbx, 2, Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))));
    goto loc_002BCE02;
loc_002BCF0B:
    Arg1 = 0;
loc_002BCF11:
    if (condition_is_greater) goto loc_002BCD0E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x48))))) & (2)) == 0) goto loc_002BD01A;
loc_002BCF27:
    Arg2 = 0;
    result = (*(uint64_t *)(local_rbx + 0x48)) * ((int32_t)(0));
    if ((*(uint64_t *)(result + v_rip - 0x2BBF0F * 1 + 0x78)) != (v_rip + 6126)) goto loc_002BD059;
    result = PopPepStartComponentActivatingActivity(local_rbx, Arg2, v_stack_p98, local_rbx + 72);
loc_002BCF63:
    v_stack_pA0 = (uint8_t)(result);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(local_rbx + 64, Arg2, v_stack_p98, local_rbx + 72);
    local_r14 = 0;
    goto loc_002BCE36;
loc_002BCF9F:
    goto loc_002BCDC5;
loc_002BCFAA:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_m50), (uint8_t)(result), 6, local_rbx + 72);
    goto loc_002BCC8B;
loc_002BCFBB:
loc_002BCFC5:
    if (4 > 5) goto loc_002BD072;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0x68))))) & (2)) == 0) goto loc_002BD02E;
loc_002BCFD9:
    v_stack_p28 = v_stack_p98;
    Arg2 = 0;
    v_stack_p20 = *(uint64_t *)(v_rip + 0xB4B735) + 120;
    result = PopPepStartActivity(local_rbx, Arg2, local_rbx + 72, 4);
    v_stack_pA0 = (uint8_t)(result);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(local_rbx + 64, Arg2, local_rbx + 72, 4);
    goto loc_002BCE36;
loc_002BD01A:
    if (((0) & (8)) != 0) goto loc_002BCF27;
    Arg1 = (uint32_t)((local_rbx + 64) + 1);
    a4 = (4) + (8);
    goto loc_002BCF11;
loc_002BD02E:
    if (((0) & (8)) != 0) goto loc_002BCFD9;
    a4 = (uint32_t)((a4) + 1);
    Arg1 = (Arg1) + (8);
    goto loc_002BCFC5;
loc_002BD03C:
    if (result != (v_rip + 5965)) goto loc_002BD0DE;
    result = PopPepStartDevicePowerOffActivity(local_rbx, Arg2, local_rbx + 72, a4);
    goto loc_002BCE02;
loc_002BD059:
    if (result != (v_rip + 5904)) goto loc_002BD07D;
    result = PopPepStartDevicePowerOnActivity(local_rbx, Arg2, local_rbx + 72, a4);
    goto loc_002BCF63;
loc_002BD072:
    goto loc_002BCFD9;
loc_002BD07D:
    if (result != (v_rip + 5900)) goto loc_002BD104;
    result = PopPepStartDevicePowerOffActivity(local_rbx, Arg2, local_rbx + 72, 6);
    goto loc_002BCF63;
loc_002BD096:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(local_rbx + 64, Arg2, local_rbx + 72, 6);
    if (((uint32_t)((uint32_t)(v_stack_pA8))) != 2) goto loc_002BCCF0;
    goto loc_002BCCF0;
loc_002BD0B1:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC50DA1))) != 0) goto loc_002BCD51;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(local_rbx + 64, v_stack_p88, local_rbx + 72, 6);
loc_002BD0D7:
    Arg1 = 0;
    goto loc_002BCD5D;
loc_002BD0DE:
    result = guard_dispatch_icall(Arg1, v_stack_p88, local_rbx + 72, 6);
    goto loc_002BCE02;
loc_002BD0E8:
    goto loc_002BCC63;
loc_002BD104:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB4B735)), v_stack_p88, local_rbx + 72, 6);
    goto loc_002BCF63;
loc_002BD10E:
    if (result == 0) goto loc_002BCD5D;
    goto loc_002BCCCA;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002BCBC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
