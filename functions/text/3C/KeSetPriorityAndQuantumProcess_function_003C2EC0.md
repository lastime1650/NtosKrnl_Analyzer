# KeSetPriorityAndQuantumProcess

- RVA: `0x003C2EC0`–`0x003C3434` (길이 `1,396` bytes)
- VA: `0x00000001403C2EC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008E2AC`
- 디코드: `350`개 명령, `1,396/1,396` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x003C2F6F` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x003C2FAF` → [KeFlushProcessWriteBuffers](../2C/KeFlushProcessWriteBuffers_function_002CE4FC.md) (function, `0x002CE4FC`)
- `0x003C3029` → [KeSetQuantumProcess](KeSetQuantumProcess_function_003C1EF0.md) (function, `0x003C1EF0`)
- `0x003C3042` → [KiSetForegroundBoost](KiSetForegroundBoost_function_003C343C.md) (function, `0x003C343C`)
- `0x003C30CE` → [KiUpdateTotalCyclesCurrentThread](../37/KiUpdateTotalCyclesCurrentThread_function_0037DE40.md) (function, `0x0037DE40`)
- `0x003C30F3` → [KiQueryQuantumReset](../21/KiQueryQuantumReset_function_0021F6B4.md) (function, `0x0021F6B4`)
- `0x003C3127` → [KiSetBasePriorityAndClearDecrement](KiSetBasePriorityAndClearDecrement_function_003C6B9C.md) (function, `0x003C6B9C`)
- `0x003C3139` → [KiComputeThreadPriority](KiComputeThreadPriority_function_003C45F4.md) (function, `0x003C45F4`)
- `0x003C315A` → [KiSetPriorityThread](../22/KiSetPriorityThread_function_00220E78.md) (function, `0x00220E78`)
- `0x003C3197` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x003C31A8` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x003C31CF` → [KiClearForegroundBoost](KiClearForegroundBoost_function_003C20D8.md) (function, `0x003C20D8`)
- `0x003C3204` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003C3213` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003C322A` → [KiPriQueueThreadPriorityChanged](KiPriQueueThreadPriorityChanged_function_003C4640.md) (function, `0x003C4640`)
- `0x003C3255` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x003C32C8` → [KiSetForegroundBoost](KiSetForegroundBoost_function_003C343C.md) (function, `0x003C343C`)
- `0x003C3317` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003C3340` → [EtwTracePriority](EtwTracePriority_function_003C41A4.md) (function, `0x003C41A4`)
- `0x003C336E` → [EtwTracePriority](EtwTracePriority_function_003C41A4.md) (function, `0x003C41A4`)
- `0x003C3393` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003C339E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003C33D7` → [KiClearForegroundBoost](KiClearForegroundBoost_function_003C20D8.md) (function, `0x003C20D8`)
- `0x003C3414` → [EtwTracePriority](EtwTracePriority_function_003C41A4.md) (function, `0x003C41A4`)

### Direct callers
- [PspSetProcessPriorityByClass](../4E/PspSetProcessPriorityByClass_function_004E9754.md) at `0x004E9799`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5925`
- [PspSetProcessPriorityByClassIgnoreForegroundBoost](../../page/AE/PspSetProcessPriorityByClassIgnoreForegroundBoost_function_00AEA1CC.md) at `0x00AEA1F1`

### Static image references
- `0x003C2EFE` → RVA `0x00FCFF00` (`CACHEALI`; read)
- `0x003C2F0E` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x003C2F4A` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003C2FFE` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003C30F8` → RVA `0x00FC5098` (`ALMOSTRO`; read)
- `0x003C31F6` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x003C32DE` → [sub_006E7EC2 + 0x7](../6E/Unknown_function_006E7EC2.md) (`tail-transfer`)
  - `0x003C33E3` → [sub_006E7EC2](../6E/Unknown_function_006E7EC2.md) (`tail-transfer`)
  - `0x003C33EC` → [sub_006E7EC2 + 0x7](../6E/Unknown_function_006E7EC2.md) (`tail-transfer`)
  - `0x003C33F5` → [sub_006E7EC2 + 0x10A](../6E/Unknown_function_006E7EC2.md) (`tail-transfer`)
  - `0x003C341A` → [sub_006E7EC2 + 0x10A](../6E/Unknown_function_006E7EC2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003C2EC0  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
003C2EC5  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
003C2ECA  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003C2ECF  55                              push rbp
003C2ED0  53                              push rbx
003C2ED1  56                              push rsi
003C2ED2  57                              push rdi
003C2ED3  41 54                           push r12
003C2ED5  41 55                           push r13
003C2ED7  41 56                           push r14
003C2ED9  41 57                           push r15
003C2EDB  48 8B EC                        mov rbp, rsp
003C2EDE  48 83 EC 78                     sub rsp, 0x78
003C2EE2  0F BE 81 90 00 00 00            movsx eax, byte ptr [rcx + 0x90]
003C2EE9  8B DA                           mov ebx, edx
003C2EEB  33 D2                           xor edx, edx
003C2EED  45 8A E8                        mov r13b, r8b
003C2EF0  89 55 B8                        mov dword ptr [rbp - 0x48], edx
003C2EF3  4C 8B F9                        mov r15, rcx
003C2EF6  3B C3                           cmp eax, ebx
003C2EF8  0F 84 19 01 00 00               je 0x1403c3017
003C2EFE  48 8D 0D FB CF C0 00            lea rcx, [rip + 0xc0cffb]
003C2F05  4C 3B F9                        cmp r15, rcx
003C2F08  0F 84 A2 02 00 00               je 0x1403c31b0
003C2F0E  8B 05 F0 3B C0 00               mov eax, dword ptr [rip + 0xc03bf0]
003C2F14  85 DB                           test ebx, ebx
003C2F16  BF 01 00 00 00                  mov edi, 1
003C2F1B  89 55 BC                        mov dword ptr [rbp - 0x44], edx
003C2F1E  0F 45 FB                        cmovne edi, ebx
003C2F21  88 55 50                        mov byte ptr [rbp + 0x50], dl
003C2F24  25 00 20 00 00                  and eax, 0x2000
003C2F29  48 89 55 D0                     mov qword ptr [rbp - 0x30], rdx
003C2F2D  89 45 C8                        mov dword ptr [rbp - 0x38], eax
003C2F30  44 8B F2                        mov r14d, edx
003C2F33  44 8B E2                        mov r12d, edx
003C2F36  40 8A F2                        mov sil, dl
003C2F39  44 0F 20 C0                     mov rax, cr8
003C2F3D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
003C2F41  B9 02 00 00 00                  mov ecx, 2
003C2F46  44 0F 22 C1                     mov cr8, rcx
003C2F4A  39 15 D0 3D C0 00               cmp dword ptr [rip + 0xc03dd0], edx
003C2F50  0F 85 BD 03 00 00               jne 0x1403c3313
003C2F56  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003C2F5F  49 8D 4F 40                     lea rcx, [r15 + 0x40]
003C2F63  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
003C2F67  48 8B 40 08                     mov rax, qword ptr [rax + 8]
003C2F6B  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
003C2F6F  E8 0C 5F E8 FF                  call 0x140248e80
003C2F74  45 84 ED                        test r13b, r13b
003C2F77  74 07                           je 0x1403c2f80
003C2F79  45 88 AF 91 00 00 00            mov byte ptr [r15 + 0x91], r13b
003C2F80  44 39 65 68                     cmp dword ptr [rbp + 0x68], r12d
003C2F84  0F 84 D5 02 00 00               je 0x1403c325f
003C2F8A  F0 41 0F BA AF 88 00 00 00 0D   lock bts dword ptr [r15 + 0x88], 0xd
003C2F94  41 0F BE 87 90 00 00 00         movsx eax, byte ptr [r15 + 0x90]
003C2F9C  8B CF                           mov ecx, edi
003C2F9E  2B C8                           sub ecx, eax
003C2FA0  89 45 C0                        mov dword ptr [rbp - 0x40], eax
003C2FA3  89 4D C4                        mov dword ptr [rbp - 0x3c], ecx
003C2FA6  B1 01                           mov cl, 1
003C2FA8  41 88 BF 90 00 00 00            mov byte ptr [r15 + 0x90], dil
003C2FAF  E8 48 B5 F0 FF                  call 0x1402ce4fc
003C2FB4  49 8D 47 30                     lea rax, [r15 + 0x30]
003C2FB8  4C 8B 28                        mov r13, qword ptr [rax]
003C2FBB  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
003C2FBF  4C 3B E8                        cmp r13, rax
003C2FC2  0F 84 CB 01 00 00               je 0x1403c3193
003C2FC8  44 8A 7D 58                     mov r15b, byte ptr [rbp + 0x58]
003C2FCC  41 B8 10 00 00 00               mov r8d, 0x10
003C2FD2  41 3B F8                        cmp edi, r8d
003C2FD5  0F 8D 9D 02 00 00               jge 0x1403c3278
003C2FDB  49 8D 9D 08 FD FF FF            lea rbx, [r13 - 0x2f8]
003C2FE2  45 84 FF                        test r15b, r15b
003C2FE5  74 07                           je 0x1403c2fee
003C2FE7  44 88 BB 8B 02 00 00            mov byte ptr [rbx + 0x28b], r15b
003C2FEE  33 FF                           xor edi, edi
003C2FF0  8D 77 01                        lea esi, [rdi + 1]
003C2FF3  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
003C2FFA  73 39                           jae 0x1403c3035
003C2FFC  03 FE                           add edi, esi
003C2FFE  85 3D A8 22 C0 00               test dword ptr [rip + 0xc022a8], edi
003C3004  0F 84 EC 01 00 00               je 0x1403c31f6
003C300A  F3 90                           pause
003C300C  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
003C3010  48 85 C0                        test rax, rax
003C3013  74 DE                           je 0x1403c2ff3
003C3015  EB E5                           jmp 0x1403c2ffc
003C3017  44 3B 4D 68                     cmp r9d, dword ptr [rbp + 0x68]
003C301B  0F 85 DD FE FF FF               jne 0x1403c2efe
003C3021  45 84 ED                        test r13b, r13b
003C3024  74 08                           je 0x1403c302e
003C3026  41 8A D5                        mov dl, r13b
003C3029  E8 C2 EE FF FF                  call 0x1403c1ef0
003C302E  8B C3                           mov eax, ebx
003C3030  E9 7B 01 00 00                  jmp 0x1403c31b0
003C3035  83 7D 68 00                     cmp dword ptr [rbp + 0x68], 0
003C3039  0F 84 83 01 00 00               je 0x1403c31c2
003C303F  48 8B CB                        mov rcx, rbx
003C3042  E8 F5 03 00 00                  call 0x1403c343c
003C3047  44 0F BE B3 33 02 00 00         movsx r14d, byte ptr [rbx + 0x233]
003C304F  41 B8 10 00 00 00               mov r8d, 0x10
003C3055  8B 4D C0                        mov ecx, dword ptr [rbp - 0x40]
003C3058  44 3B F1                        cmp r14d, ecx
003C305B  7E 12                           jle 0x1403c306f
003C305D  45 3B F0                        cmp r14d, r8d
003C3060  7C 0D                           jl 0x1403c306f
003C3062  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
003C306A  E9 12 01 00 00                  jmp 0x1403c3181
003C306F  8B 7D C4                        mov edi, dword ptr [rbp - 0x3c]
003C3072  41 03 FE                        add edi, r14d
003C3075  41 3B F8                        cmp edi, r8d
003C3078  0F 8D A1 03 00 00               jge 0x1403c341f
003C307E  85 FF                           test edi, edi
003C3080  0F 4E FE                        cmovle edi, esi
003C3083  8A 83 85 02 00 00               mov al, byte ptr [rbx + 0x285]
003C3089  89 7D B8                        mov dword ptr [rbp - 0x48], edi
003C308C  84 C0                           test al, al
003C308E  74 1C                           je 0x1403c30ac
003C3090  41 3B C8                        cmp ecx, r8d
003C3093  7D 08                           jge 0x1403c309d
003C3095  40 32 F6                        xor sil, sil
003C3098  E9 D2 00 00 00                  jmp 0x1403c316f
003C309D  84 C0                           test al, al
003C309F  0F 8E 84 03 00 00               jle 0x1403c3429
003C30A5  C7 45 B8 0F 00 00 00            mov dword ptr [rbp - 0x48], 0xf
003C30AC  48 3B 5D E0                     cmp rbx, qword ptr [rbp - 0x20]
003C30B0  0F 85 23 01 00 00               jne 0x1403c31d9
003C30B6  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
003C30BA  80 78 20 00                     cmp byte ptr [rax + 0x20], 0
003C30BE  0F 85 15 01 00 00               jne 0x1403c31d9
003C30C4  FA                              cli
003C30C5  45 33 C0                        xor r8d, r8d
003C30C8  48 8B D3                        mov rdx, rbx
003C30CB  48 8B C8                        mov rcx, rax
003C30CE  E8 6D AD FB FF                  call 0x14037de40
003C30D3  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003C30DC  48 8B F8                        mov rdi, rax
003C30DF  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
003C30E6  4D 85 C0                        test r8, r8
003C30E9  0F 85 48 01 00 00               jne 0x1403c3237
003C30EF  FB                              sti
003C30F0  48 8B CB                        mov rcx, rbx
003C30F3  E8 BC C5 E5 FF                  call 0x14021f6b4
003C30F8  0F AF 05 99 1F C0 00            imul eax, dword ptr [rip + 0xc01f99]
003C30FF  8B C8                           mov ecx, eax
003C3101  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
003C3104  48 03 CF                        add rcx, rdi
003C3107  A8 20                           test al, 0x20
003C3109  74 06                           je 0x1403c3111
003C310B  F0 0F BA 73 78 05               lock btr dword ptr [rbx + 0x78], 5
003C3111  8B 7D B8                        mov edi, dword ptr [rbp - 0x48]
003C3114  40 32 F6                        xor sil, sil
003C3117  48 89 4B 20                     mov qword ptr [rbx + 0x20], rcx
003C311B  41 3B FE                        cmp edi, r14d
003C311E  74 11                           je 0x1403c3131
003C3120  48 8D 55 B8                     lea rdx, [rbp - 0x48]
003C3124  48 8B CB                        mov rcx, rbx
003C3127  E8 70 3A 00 00                  call 0x1403c6b9c
003C312C  BE 01 00 00 00                  mov esi, 1
003C3131  45 33 C0                        xor r8d, r8d
003C3134  33 D2                           xor edx, edx
003C3136  48 8B CB                        mov rcx, rbx
003C3139  E8 B6 14 00 00                  call 0x1403c45f4
003C313E  44 8B E0                        mov r12d, eax
003C3141  0F BE 83 C3 00 00 00            movsx eax, byte ptr [rbx + 0xc3]
003C3148  44 3B E0                        cmp r12d, eax
003C314B  74 1D                           je 0x1403c316a
003C314D  45 8B C4                        mov r8d, r12d
003C3150  89 45 BC                        mov dword ptr [rbp - 0x44], eax
003C3153  48 8D 55 D0                     lea rdx, [rbp - 0x30]
003C3157  48 8B CB                        mov rcx, rbx
003C315A  E8 19 DD E5 FF                  call 0x140220e78
003C315F  44 0F BE A3 C3 00 00 00         movsx r12d, byte ptr [rbx + 0xc3]
003C3167  88 45 50                        mov byte ptr [rbp + 0x50], al
003C316A  40 84 F6                        test sil, sil
003C316D  75 73                           jne 0x1403c31e2
003C316F  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
003C3177  83 7D C8 00                     cmp dword ptr [rbp - 0x38], 0
003C317B  0F 85 A0 01 00 00               jne 0x1403c3321
003C3181  4D 8B 6D 00                     mov r13, qword ptr [r13]
003C3185  4C 3B 6D E8                     cmp r13, qword ptr [rbp - 0x18]
003C3189  0F 85 4C FE FF FF               jne 0x1403c2fdb
003C318F  4C 8B 7D 48                     mov r15, qword ptr [rbp + 0x48]
003C3193  49 8D 4F 40                     lea rcx, [r15 + 0x40]
003C3197  E8 44 66 E8 FF                  call 0x1402497e0
003C319C  44 8A 45 F0                     mov r8b, byte ptr [rbp - 0x10]
003C31A0  48 8D 55 D0                     lea rdx, [rbp - 0x30]
003C31A4  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
003C31A8  E8 53 D6 E8 FF                  call 0x140250800
003C31AD  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
003C31B0  48 83 C4 78                     add rsp, 0x78
003C31B4  41 5F                           pop r15
003C31B6  41 5E                           pop r14
003C31B8  41 5D                           pop r13
003C31BA  41 5C                           pop r12
003C31BC  5F                              pop rdi
003C31BD  5E                              pop rsi
003C31BE  5B                              pop rbx
003C31BF  5D                              pop rbp
003C31C0  C3                              ret
003C31C1  CC                              int3
003C31C2  83 7D 60 00                     cmp dword ptr [rbp + 0x60], 0
003C31C6  0F 84 7B FE FF FF               je 0x1403c3047
003C31CC  48 8B CB                        mov rcx, rbx
003C31CF  E8 04 EF FF FF                  call 0x1403c20d8
003C31D4  E9 6E FE FF FF                  jmp 0x1403c3047
003C31D9  48 8B 7B 48                     mov rdi, qword ptr [rbx + 0x48]
003C31DD  E9 0E FF FF FF                  jmp 0x1403c30f0
003C31E2  48 8B 8B E8 00 00 00            mov rcx, qword ptr [rbx + 0xe8]
003C31E9  48 85 C9                        test rcx, rcx
003C31EC  75 2F                           jne 0x1403c321d
003C31EE  8B 7D B8                        mov edi, dword ptr [rbp - 0x48]
003C31F1  E9 79 FF FF FF                  jmp 0x1403c316f
003C31F6  8B 05 BC 38 C0 00               mov eax, dword ptr [rip + 0xc038bc]
003C31FC  A8 40                           test al, 0x40
003C31FE  0F 84 06 FE FF FF               je 0x1403c300a
003C3204  E8 87 C2 F4 FF                  call 0x14030f490
003C3209  84 C0                           test al, al
003C320B  0F 84 F9 FD FF FF               je 0x1403c300a
003C3211  8B CF                           mov ecx, edi
003C3213  E8 48 C2 F4 FF                  call 0x14030f460
003C3218  E9 EF FD FF FF                  jmp 0x1403c300c
003C321D  8A 11                           mov dl, byte ptr [rcx]
003C321F  80 E2 7F                        and dl, 0x7f
003C3222  80 FA 15                        cmp dl, 0x15
003C3225  75 C7                           jne 0x1403c31ee
003C3227  48 8B D3                        mov rdx, rbx
003C322A  E8 11 14 00 00                  call 0x1403c4640
003C322F  8B 7D B8                        mov edi, dword ptr [rbp - 0x48]
003C3232  E9 40 FF FF FF                  jmp 0x1403c3177
003C3237  41 0F 0D 08                     prefetchw byte ptr [r8]
003C323B  41 8B 00                        mov eax, dword ptr [r8]
003C323E  8B D0                           mov edx, eax
003C3240  0F BA F2 15                     btr edx, 0x15
003C3244  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
003C3249  75 F3                           jne 0x1403c323e
003C324B  0F BA E0 15                     bt eax, 0x15
003C324F  0F 83 9A FE FF FF               jae 0x1403c30ef
003C3255  E8 76 FF E9 FF                  call 0x1402631d0
003C325A  E9 90 FE FF FF                  jmp 0x1403c30ef
003C325F  44 39 65 60                     cmp dword ptr [rbp + 0x60], r12d
003C3263  0F 84 2B FD FF FF               je 0x1403c2f94
003C3269  F0 41 0F BA B7 88 00 00 00 0D   lock btr dword ptr [r15 + 0x88], 0xd
003C3273  E9 1C FD FF FF                  jmp 0x1403c2f94
003C3278  49 8D 9D 08 FD FF FF            lea rbx, [r13 - 0x2f8]
003C327F  45 84 FF                        test r15b, r15b
003C3282  0F 85 1D 01 00 00               jne 0x1403c33a5
003C3288  33 FF                           xor edi, edi
003C328A  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
003C3291  0F 82 E1 00 00 00               jb 0x1403c3378
003C3297  0F BE BB 33 02 00 00            movsx edi, byte ptr [rbx + 0x233]
003C329E  41 B8 10 00 00 00               mov r8d, 0x10
003C32A4  03 7D C4                        add edi, dword ptr [rbp - 0x3c]
003C32A7  41 8D 50 0F                     lea edx, [r8 + 0xf]
003C32AB  41 3B F8                        cmp edi, r8d
003C32AE  0F 8D 09 01 00 00               jge 0x1403c33bd
003C32B4  41 8B F8                        mov edi, r8d
003C32B7  44 89 45 B8                     mov dword ptr [rbp - 0x48], r8d
003C32BB  83 7D 68 00                     cmp dword ptr [rbp + 0x68], 0
003C32BF  0F 84 05 01 00 00               je 0x1403c33ca
003C32C5  48 8B CB                        mov rcx, rbx
003C32C8  E8 6F 01 00 00                  call 0x1403c343c
003C32CD  BA 1F 00 00 00                  mov edx, 0x1f
003C32D2  44 8D 42 F1                     lea r8d, [rdx - 0xf]
003C32D6  8A 83 85 02 00 00               mov al, byte ptr [rbx + 0x285]
003C32DC  84 C0                           test al, al
003C32DE  0F 84 E5 4B 32 00               je 0x1406e7ec9
003C32E4  44 39 45 C0                     cmp dword ptr [rbp - 0x40], r8d
003C32E8  0F 8C F3 00 00 00               jl 0x1403c33e1
003C32EE  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
003C32F6  83 7D C8 00                     cmp dword ptr [rbp - 0x38], 0
003C32FA  0F 85 F1 00 00 00               jne 0x1403c33f1
003C3300  4D 8B 6D 00                     mov r13, qword ptr [r13]
003C3304  4C 3B 6D E8                     cmp r13, qword ptr [rbp - 0x18]
003C3308  0F 84 81 FE FF FF               je 0x1403c318f
003C330E  E9 65 FF FF FF                  jmp 0x1403c3278
003C3313  8A D1                           mov dl, cl
003C3315  8A C8                           mov cl, al
003C3317  E8 E0 23 13 00                  call 0x1404f56fc
003C331C  E9 35 FC FF FF                  jmp 0x1403c2f56
003C3321  80 7D 50 00                     cmp byte ptr [rbp + 0x50], 0
003C3325  74 1E                           je 0x1403c3345
003C3327  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
003C332D  BA 30 05 00 00                  mov edx, 0x530
003C3332  44 8B 45 BC                     mov r8d, dword ptr [rbp - 0x44]
003C3336  45 8B CC                        mov r9d, r12d
003C3339  48 8B CB                        mov rcx, rbx
003C333C  C6 45 50 00                     mov byte ptr [rbp + 0x50], 0
003C3340  E8 5F 0E 00 00                  call 0x1403c41a4
003C3345  40 84 F6                        test sil, sil
003C3348  0F 84 33 FE FF FF               je 0x1403c3181
003C334E  44 3B F7                        cmp r14d, edi
003C3351  0F 84 2A FE FF FF               je 0x1403c3181
003C3357  48 8D 45 B8                     lea rax, [rbp - 0x48]
003C335B  BA 31 05 00 00                  mov edx, 0x531
003C3360  44 8B CF                        mov r9d, edi
003C3363  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003C3368  45 8B C6                        mov r8d, r14d
003C336B  48 8B CB                        mov rcx, rbx
003C336E  E8 31 0E 00 00                  call 0x1403c41a4
003C3373  E9 09 FE FF FF                  jmp 0x1403c3181
003C3378  FF C7                           inc edi
003C337A  85 3D 2C 1F C0 00               test dword ptr [rip + 0xc01f2c], edi
003C3380  74 2F                           je 0x1403c33b1
003C3382  F3 90                           pause
003C3384  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
003C3388  48 85 C0                        test rax, rax
003C338B  0F 84 F9 FE FF FF               je 0x1403c328a
003C3391  EB E5                           jmp 0x1403c3378
003C3393  E8 F8 C0 F4 FF                  call 0x14030f490
003C3398  84 C0                           test al, al
003C339A  74 E6                           je 0x1403c3382
003C339C  8B CF                           mov ecx, edi
003C339E  E8 BD C0 F4 FF                  call 0x14030f460
003C33A3  EB DF                           jmp 0x1403c3384
003C33A5  44 88 BB 8B 02 00 00            mov byte ptr [rbx + 0x28b], r15b
003C33AC  E9 D7 FE FF FF                  jmp 0x1403c3288
003C33B1  8B 05 01 37 C0 00               mov eax, dword ptr [rip + 0xc03701]
003C33B7  A8 40                           test al, 0x40
003C33B9  74 C7                           je 0x1403c3382
003C33BB  EB D6                           jmp 0x1403c3393
003C33BD  3B FA                           cmp edi, edx
003C33BF  0F 4F FA                        cmovg edi, edx
003C33C2  89 7D B8                        mov dword ptr [rbp - 0x48], edi
003C33C5  E9 F1 FE FF FF                  jmp 0x1403c32bb
003C33CA  83 7D 60 00                     cmp dword ptr [rbp + 0x60], 0
003C33CE  0F 84 02 FF FF FF               je 0x1403c32d6
003C33D4  48 8B CB                        mov rcx, rbx
003C33D7  E8 FC EC FF FF                  call 0x1403c20d8
003C33DC  E9 F5 FE FF FF                  jmp 0x1403c32d6
003C33E1  84 C0                           test al, al
003C33E3  0F 8E D9 4A 32 00               jle 0x1406e7ec2
003C33E9  89 55 B8                        mov dword ptr [rbp - 0x48], edx
003C33EC  E9 D8 4A 32 00                  jmp 0x1406e7ec9
003C33F1  80 7D 50 00                     cmp byte ptr [rbp + 0x50], 0
003C33F5  0F 84 D1 4B 32 00               je 0x1406e7fcc
003C33FB  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
003C3401  BA 30 05 00 00                  mov edx, 0x530
003C3406  44 8B 45 BC                     mov r8d, dword ptr [rbp - 0x44]
003C340A  45 8B CC                        mov r9d, r12d
003C340D  48 8B CB                        mov rcx, rbx
003C3410  C6 45 50 00                     mov byte ptr [rbp + 0x50], 0
003C3414  E8 8B 0D 00 00                  call 0x1403c41a4
003C3419  90                              nop
003C341A  E9 AD 4B 32 00                  jmp 0x1406e7fcc
003C341F  BF 0F 00 00 00                  mov edi, 0xf
003C3424  E9 5A FC FF FF                  jmp 0x1403c3083
003C3429  0F 48 FE                        cmovs edi, esi
003C342C  89 7D B8                        mov dword ptr [rbp - 0x48], edi
003C342F  E9 78 FC FF FF                  jmp 0x1403c30ac
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSetPriorityAndQuantumProcess(__int64 a1, int a2, unsigned __int8 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    a2 = 0;
    v_stack_m88 = 0;
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(a1 + 144)))) == ((unsigned int)((unsigned int)(a2)))) goto loc_003C3017;
loc_003C2EFE:
    if (a1 == (v_rip + 12636155)) goto loc_003C31B0;
    v_stack_m84 = 0;
    v_rdi = 1;
    if ((unsigned int)((unsigned int)(a2)) != 0) { v_rdi = (unsigned int)((unsigned int)(a2)); }
    v_stack_p10 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12598256))) & (0x2000ULL));
    v_stack_m70 = 0;
    v_stack_m78 = (unsigned int)(result);
    v_stack_m50 = v_cr8;
    if ((*(unsigned int *)(v_rip + 12598736)) != 0) goto loc_003C3313;
loc_003C2F56:
    v_stack_m68 = *(unsigned __int64 *)(gs_base + (0 + 32));
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a1 + 64, a2, a3, a4);
    if (a3 != 0) {
        *(unsigned __int8 *)(a1 + 145) = a3;
    }
    if (a5 == 0) goto loc_003C325F;
loc_003C2F94:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)((__int8)(*(unsigned __int8 *)(a1 + 144)))));
    v_stack_m80 = (unsigned int)((__int8)(*(unsigned __int8 *)(a1 + 144)));
    v_stack_m7C = (unsigned int)(a1);
    *(unsigned __int8 *)(a1 + 144) = (unsigned __int8)(v_rdi);
    result = KeFlushProcessWriteBuffers(1, a2, a3, a4);
    v_stack_m58 = a1 + 48;
    if ((*(unsigned __int64 *)(a1 + 48)) == (a1 + 48)) goto loc_003C3193;
    if (((unsigned int)(v_rdi)) >= 16) goto loc_003C3278;
loc_003C2FDB:
    if ((unsigned __int8)(v_stack_p18) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 651) = (unsigned __int8)(v_stack_p18);
    }
    v_rdi = 0;
loc_003C2FF3:
    if (condition_is_above_or_equal) goto loc_003C3035;
loc_003C2FFC:
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rdi + 1)));
    if (((*(unsigned int *)(v_rip + 12591784)) & ((unsigned int)(v_rdi))) == 0) goto loc_003C31F6;
loc_003C300A:
loc_003C300C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 64) == 0) goto loc_003C2FF3;
    goto loc_003C2FFC;
loc_003C3017:
    if (a4 != a5) goto loc_003C2EFE;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 64);
    if ((unsigned __int8)(*(unsigned __int64 *)(a1 + 48)) != 0) {
        a2 = (unsigned __int8)(*(unsigned __int64 *)(a1 + 48));
        result = KeSetQuantumProcess(1, a2, 16, a4);
    }
    goto loc_003C31B0;
loc_003C3035:
    if (a5 == 0) goto loc_003C31C2;
    result = KiSetForegroundBoost(*(unsigned __int64 *)(a1 + 48) - 760, a2, 16, a4);
loc_003C3047:
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 563)))) <= ((unsigned int)((unsigned int)(v_stack_m80)))) goto loc_003C306F;
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 563)))) < 16) goto loc_003C306F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 64) = 0;
    goto loc_003C3181;
loc_003C306F:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m7C)) + ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 563)))));
    if (((unsigned int)(v_rdi)) >= 16) goto loc_003C341F;
    if (condition_is_less_or_equal) { v_rdi = (unsigned int)(v_rdi + 1); }
loc_003C3083:
    v_stack_m88 = (unsigned int)(v_rdi);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 645)) == 0) goto loc_003C30AC;
    if (((unsigned int)((unsigned int)(v_stack_m80))) >= 16) goto loc_003C309D;
    v_rsi = 0;
    goto loc_003C316F;
loc_003C309D:
    if (condition_is_less_or_equal) goto loc_003C3429;
    v_stack_m88 = 15;
loc_003C30AC:
    if ((*(unsigned __int64 *)(a1 + 48) - 760) != v_stack_m60) goto loc_003C31D9;
    if ((*(unsigned __int8 *)(v_stack_m68 + 32)) != 0) goto loc_003C31D9;
    a3 = 0;
    result = KiUpdateTotalCyclesCurrentThread(v_stack_m68, *(unsigned __int64 *)(a1 + 48) - 760, a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_003C3237;
loc_003C30EF:
loc_003C30F0:
    result = KiQueryQuantumReset(*(unsigned __int64 *)(a1 + 48) - 760, *(unsigned __int64 *)(a1 + 48) - 760, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    result = (unsigned int)((result) * (*(unsigned int *)(v_rip + 12591001)));
    a1 = ((unsigned int)((unsigned int)(result))) + (result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) - 760 + 120)))) & (32)) != 0) {
    }
    v_rsi = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 32) = a1;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) - 760 + 120));
    if (((unsigned int)((unsigned int)(v_stack_m88))) != ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 563))))) {
        a2 = v_stack_m88;
        a1 = *(unsigned __int64 *)(a1 + 48) - 760;
        result = KiSetBasePriorityAndClearDecrement(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
        v_rsi = 1;
    }
    a3 = 0;
    a2 = 0;
    result = KiComputeThreadPriority(*(unsigned __int64 *)(a1 + 48) - 760, a2, a3, a4);
    result = (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 195));
    v_r12 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 195))))) {
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_m84 = (unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 195)));
        a2 = v_stack_m70;
        a1 = *(unsigned __int64 *)(a1 + 48) - 760;
        result = KiSetPriorityThread(a1, a2, a3, a4);
        v_r12 = (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 195));
        v_stack_p10 = (unsigned __int8)(result);
    }
    if ((unsigned __int8)(v_rsi) != 0) goto loc_003C31E2;
loc_003C316F:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 64) = 0;
loc_003C3177:
    if (v_stack_m78 != 0) goto loc_003C3321;
loc_003C3181:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48))) != v_stack_m58) goto loc_003C2FDB;
loc_003C318F:
loc_003C3193:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_p8 + 64, a2, a3, a4);
    result = KiProcessDeferredReadyList(v_stack_m68, v_stack_m70, v_stack_m50, a4);
loc_003C31B0:
    v_rsp = (v_rsp) + (120);
    return (unsigned int)(v_stack_m80);
loc_003C31C2:
    if (v_stack_p20 == 0) goto loc_003C3047;
    result = KiClearForegroundBoost(*(unsigned __int64 *)(a1 + 48) - 760, v_stack_m70, v_stack_m50, a4);
    goto loc_003C3047;
loc_003C31D9:
    goto loc_003C30F0;
loc_003C31E2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 232) != 0) goto loc_003C321D;
loc_003C31EE:
    goto loc_003C316F;
loc_003C31F6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12597436)))) & (64)) == 0) goto loc_003C300A;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 232), v_stack_m70, v_stack_m50, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003C300A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(v_stack_m88))), v_stack_m70, v_stack_m50, a4);
    goto loc_003C300C;
loc_003C321D:
    a2 = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m88))))) & (127));
    if (((unsigned __int8)(a2)) != 21) goto loc_003C31EE;
    result = KiPriQueueThreadPriorityChanged((unsigned int)((unsigned int)((unsigned int)(v_stack_m88))), *(unsigned __int64 *)(a1 + 48) - 760, v_stack_m50, a4);
    goto loc_003C3177;
loc_003C3237:
loc_003C323E:
    if (((unsigned __int8)(a2)) != 21) goto loc_003C323E;
    if (((unsigned __int8)(a2)) >= 21) goto loc_003C30EF;
    result = KiRemoveSystemWorkPriorityKick((unsigned int)((unsigned int)((unsigned int)(v_stack_m88))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50)))), v_stack_m50, a4);
    goto loc_003C30EF;
loc_003C325F:
    if (v_stack_p20 == ((unsigned int)(v_r12))) goto loc_003C2F94;
    goto loc_003C2F94;
loc_003C3278:
    if ((unsigned __int8)(v_stack_p8) != 0) goto loc_003C33A5;
loc_003C3288:
    v_rdi = 0;
loc_003C328A:
    if (condition_is_below) goto loc_003C3378;
    v_rdi = (unsigned int)(((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760 + 563))) + (v_stack_m7C));
    if (((unsigned int)(v_rdi)) >= 16) goto loc_003C33BD;
    v_stack_m88 = 16;
loc_003C32BB:
    if (a5 == 0) goto loc_003C33CA;
    result = KiSetForegroundBoost(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760, 16 + 15, 16, a4);
loc_003C32D6:
    if (v_stack_m80 < ((unsigned int)(31 - 15))) goto loc_003C33E1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760 + 64) = 0;
    if (v_stack_m78 != 0) goto loc_003C33F1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)))) == v_stack_m58) goto loc_003C318F;
    goto loc_003C3278;
loc_003C3313:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760 + 645)), (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760), 31 - 15, a4);
    goto loc_003C2F56;
loc_003C3321:
    if (v_stack_p10 != 0) {
        a2 = 0x530ULL;
        a3 = v_stack_m84;
        a4 = (unsigned int)(v_r12);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760;
        v_stack_p10 = 0;
        result = EtwTracePriority(a1, a2, a3, a4);
    }
    if ((unsigned __int8)(v_rsi) == 0) goto loc_003C3181;
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 563)))) == 16) goto loc_003C3181;
    v_stack_p20 = v_stack_m88;
    result = EtwTracePriority(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760, (unsigned int)(0x531ULL), (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 563)))), 16);
    goto loc_003C3181;
loc_003C3378:
    v_rdi = (unsigned int)((16) + 1);
    if (((*(unsigned int *)(v_rip + 12590892)) & ((unsigned int)(v_rdi))) == 0) goto loc_003C33B1;
loc_003C3382:
loc_003C3384:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760 + 64) == 0) goto loc_003C328A;
    goto loc_003C3378;
loc_003C3393:
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760, (unsigned int)(0x531ULL), (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 563)))), 16);
    if ((unsigned __int8)(result) == 0) goto loc_003C3382;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x531ULL), (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 563)))), 16);
    goto loc_003C3384;
loc_003C33A5:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760 + 651) = (unsigned __int8)(v_stack_p8);
    goto loc_003C3288;
loc_003C33B1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12596993)))) & (64)) == 0) goto loc_003C3382;
    goto loc_003C3393;
loc_003C33BD:
    if (((unsigned int)(v_rdi)) > ((unsigned int)((unsigned int)(0x531ULL)))) { v_rdi = (unsigned int)((unsigned int)(0x531ULL)); }
    v_stack_m88 = (unsigned int)(v_rdi);
    goto loc_003C32BB;
loc_003C33CA:
    if (v_stack_p20 == 0) goto loc_003C32D6;
    result = KiClearForegroundBoost(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760, (unsigned int)(0x531ULL), (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 48) - 760 + 563)))), 16);
    goto loc_003C32D6;
loc_003C33E1:
    v_stack_m88 = (unsigned int)((unsigned int)(0x531ULL));
loc_003C33F1:
    v_stack_p10 = 0;
    result = EtwTracePriority(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48)) - 760, (unsigned int)(0x530ULL), (unsigned int)(v_stack_m84), (unsigned int)((unsigned int)(v_r12)));
loc_003C341F:
    goto loc_003C3083;
loc_003C3429:
    v_rdi = 15;
    if (sign_flag) { v_rdi = (unsigned int)(v_rsi); }
    v_stack_m88 = (unsigned int)(v_rdi);
    goto loc_003C30AC;
}
```

## 5. (Beta) C Style

```c
int64_t KeSetPriorityAndQuantumProcess(void *Arg1, int32_t Arg2, uint8_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    Arg2 = 0;
    v_stack_m88 = 0;
    if (((uint32_t)((int8_t)(*(uint8_t *)(arg1 + 0x90)))) == ((uint32_t)((uint32_t)(Arg2)))) goto loc_003C3017;
loc_003C2EFE:
    if (Arg1 == (v_rip + 12636155)) goto loc_003C31B0;
    v_stack_m84 = 0;
    local_rdi = 1;
    if ((uint32_t)((uint32_t)(Arg2)) != 0) { local_rdi = (uint32_t)((uint32_t)(Arg2)); }
    v_stack_p10 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC03BF0))) & (0x2000ULL));
    v_stack_m70 = 0;
    v_stack_m78 = (uint32_t)(result);
    v_stack_m50 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xC03DD0)) != 0) goto loc_003C3313;
loc_003C2F56:
    v_stack_m68 = *(uint64_t *)(gs_base + (0 + 0x20));
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1 + 64, Arg2, Arg3, Arg4);
    if (Arg3 != 0) {
        *(uint8_t *)(arg1 + 0x91) = Arg3;
    }
    if (Arg5 == 0) goto loc_003C325F;
loc_003C2F94:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)((int8_t)(*(uint8_t *)(arg1 + 0x90)))));
    v_stack_m80 = (uint32_t)((int8_t)(*(uint8_t *)(arg1 + 0x90)));
    v_stack_m7C = (uint32_t)(Arg1);
    *(uint8_t *)(arg1 + 0x90) = (uint8_t)(local_rdi);
    result = KeFlushProcessWriteBuffers(1, Arg2, Arg3, Arg4);
    v_stack_m58 = Arg1 + 48;
    if ((*(uint64_t *)(arg1 + 0x30)) == (Arg1 + 48)) goto loc_003C3193;
    if (((uint32_t)(local_rdi)) >= 16) goto loc_003C3278;
loc_003C2FDB:
    if ((uint8_t)(v_stack_p18) != 0) {
        *(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x28B) = (uint8_t)(v_stack_p18);
    }
    local_rdi = 0;
loc_003C2FF3:
    if (condition_is_above_or_equal) goto loc_003C3035;
loc_003C2FFC:
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rdi + 1)));
    if (((*(uint32_t *)(v_rip + 0xC022A8)) & ((uint32_t)(local_rdi))) == 0) goto loc_003C31F6;
loc_003C300A:
loc_003C300C:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x40) == 0) goto loc_003C2FF3;
    goto loc_003C2FFC;
loc_003C3017:
    if (Arg4 != Arg5) goto loc_003C2EFE;
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x40);
    if ((uint8_t)(*(uint64_t *)(arg1 + 0x30)) != 0) {
        Arg2 = (uint8_t)(*(uint64_t *)(arg1 + 0x30));
        result = KeSetQuantumProcess(1, Arg2, 16, Arg4);
    }
    goto loc_003C31B0;
loc_003C3035:
    if (Arg5 == 0) goto loc_003C31C2;
    result = KiSetForegroundBoost(*(uint64_t *)(arg1 + 0x30) - 760, Arg2, 16, Arg4);
loc_003C3047:
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x233)))) <= ((uint32_t)((uint32_t)(v_stack_m80)))) goto loc_003C306F;
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x233)))) < 16) goto loc_003C306F;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x40) = 0;
    goto loc_003C3181;
loc_003C306F:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m7C)) + ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x233)))));
    if (((uint32_t)(local_rdi)) >= 16) goto loc_003C341F;
    if (condition_is_less_or_equal) { local_rdi = (uint32_t)(local_rdi + 1); }
loc_003C3083:
    v_stack_m88 = (uint32_t)(local_rdi);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x285)) == 0) goto loc_003C30AC;
    if (((uint32_t)((uint32_t)(v_stack_m80))) >= 16) goto loc_003C309D;
    local_rsi = 0;
    goto loc_003C316F;
loc_003C309D:
    if (condition_is_less_or_equal) goto loc_003C3429;
    v_stack_m88 = 15;
loc_003C30AC:
    if ((*(uint64_t *)(arg1 + 0x30) - 760) != v_stack_m60) goto loc_003C31D9;
    if ((*(uint8_t *)(v_stack_m68 + 0x20)) != 0) goto loc_003C31D9;
    Arg3 = 0;
    result = KiUpdateTotalCyclesCurrentThread(v_stack_m68, *(uint64_t *)(arg1 + 0x30) - 760, Arg3, Arg4);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_003C3237;
loc_003C30EF:
loc_003C30F0:
    result = KiQueryQuantumReset(*(uint64_t *)(arg1 + 0x30) - 760, *(uint64_t *)(arg1 + 0x30) - 760, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    result = (uint32_t)((result) * (*(uint32_t *)(v_rip + 0xC01F99)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x78)))) & (32)) != 0) {
    }
    local_rsi = 0;
    *(void **)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x20) = Arg1;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x78));
    if (((uint32_t)((uint32_t)(v_stack_m88))) != ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x233))))) {
        Arg2 = v_stack_m88;
        Arg1 = *(uint64_t *)(arg1 + 0x30) - 760;
        result = KiSetBasePriorityAndClearDecrement(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
        local_rsi = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KiComputeThreadPriority(*(uint64_t *)(arg1 + 0x30) - 760, Arg2, Arg3, Arg4);
    result = (int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0xC3));
    local_r12 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0xC3))))) {
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_m84 = (uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0xC3)));
        Arg2 = v_stack_m70;
        Arg1 = *(uint64_t *)(arg1 + 0x30) - 760;
        result = KiSetPriorityThread(Arg1, Arg2, Arg3, Arg4);
        local_r12 = (int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0xC3));
        v_stack_p10 = (uint8_t)(result);
    }
    if ((uint8_t)(local_rsi) != 0) goto loc_003C31E2;
loc_003C316F:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x40) = 0;
loc_003C3177:
    if (v_stack_m78 != 0) goto loc_003C3321;
loc_003C3181:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x30))) != v_stack_m58) goto loc_003C2FDB;
loc_003C318F:
loc_003C3193:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_p8 + 64, Arg2, Arg3, Arg4);
    result = KiProcessDeferredReadyList(v_stack_m68, v_stack_m70, v_stack_m50, Arg4);
loc_003C31B0:
    local_rsp = (local_rsp) + (120);
    return (uint32_t)(v_stack_m80);
loc_003C31C2:
    if (v_stack_p20 == 0) goto loc_003C3047;
    result = KiClearForegroundBoost(*(uint64_t *)(arg1 + 0x30) - 760, v_stack_m70, v_stack_m50, Arg4);
    goto loc_003C3047;
loc_003C31D9:
    goto loc_003C30F0;
loc_003C31E2:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0xE8) != 0) goto loc_003C321D;
loc_003C31EE:
    goto loc_003C316F;
loc_003C31F6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC038BC)))) & (64)) == 0) goto loc_003C300A;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0xE8), v_stack_m70, v_stack_m50, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003C300A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(v_stack_m88))), v_stack_m70, v_stack_m50, Arg4);
    goto loc_003C300C;
loc_003C321D:
    Arg2 = (uint8_t)((*(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m88))))) & (127));
    if (((uint8_t)(Arg2)) != 21) goto loc_003C31EE;
    result = KiPriQueueThreadPriorityChanged((uint32_t)((uint32_t)((uint32_t)(v_stack_m88))), *(uint64_t *)(arg1 + 0x30) - 760, v_stack_m50, Arg4);
    goto loc_003C3177;
loc_003C3237:
loc_003C323E:
    if (((uint8_t)(Arg2)) != 21) goto loc_003C323E;
    if (((uint8_t)(Arg2)) >= 21) goto loc_003C30EF;
    result = KiRemoveSystemWorkPriorityKick((uint32_t)((uint32_t)((uint32_t)(v_stack_m88))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50)))), v_stack_m50, Arg4);
    goto loc_003C30EF;
loc_003C325F:
    if (v_stack_p20 == ((uint32_t)(local_r12))) goto loc_003C2F94;
    goto loc_003C2F94;
loc_003C3278:
    if ((uint8_t)(v_stack_p8) != 0) goto loc_003C33A5;
loc_003C3288:
    local_rdi = 0;
loc_003C328A:
    if (condition_is_below) goto loc_003C3378;
    local_rdi = (uint32_t)(((int8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 0x2F8 + 0x233))) + (v_stack_m7C));
    if (((uint32_t)(local_rdi)) >= 16) goto loc_003C33BD;
    v_stack_m88 = 16;
loc_003C32BB:
    if (Arg5 == 0) goto loc_003C33CA;
    result = KiSetForegroundBoost(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 760, 16 + 15, 16, Arg4);
loc_003C32D6:
    if (v_stack_m80 < ((uint32_t)(31 - 15))) goto loc_003C33E1;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 0x2F8 + 0x40) = 0;
    if (v_stack_m78 != 0) goto loc_003C33F1;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)))) == v_stack_m58) goto loc_003C318F;
    goto loc_003C3278;
loc_003C3313:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 0x2F8 + 0x285)), (uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 760), 31 - 15, Arg4);
    goto loc_003C2F56;
loc_003C3321:
    if (v_stack_p10 != 0) {
        Arg2 = 0x530ULL;
        Arg3 = v_stack_m84;
        Arg4 = (uint32_t)(local_r12);
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 760;
        v_stack_p10 = 0;
        result = EtwTracePriority(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint8_t)(local_rsi) == 0) goto loc_003C3181;
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x233)))) == 16) goto loc_003C3181;
    v_stack_p20 = v_stack_m88;
    result = EtwTracePriority(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 760, (uint32_t)(0x531ULL), (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x233)))), 16);
    goto loc_003C3181;
loc_003C3378:
    local_rdi = (uint32_t)((16) + 1);
    if (((*(uint32_t *)(v_rip + 0xC01F2C)) & ((uint32_t)(local_rdi))) == 0) goto loc_003C33B1;
loc_003C3382:
loc_003C3384:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 0x2F8 + 0x40) == 0) goto loc_003C328A;
    goto loc_003C3378;
loc_003C3393:
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 760, (uint32_t)(0x531ULL), (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x233)))), 16);
    if ((uint8_t)(result) == 0) goto loc_003C3382;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x531ULL), (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x233)))), 16);
    goto loc_003C3384;
loc_003C33A5:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 0x2F8 + 0x28B) = (uint8_t)(v_stack_p8);
    goto loc_003C3288;
loc_003C33B1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC03701)))) & (64)) == 0) goto loc_003C3382;
    goto loc_003C3393;
loc_003C33BD:
    if (((uint32_t)(local_rdi)) > ((uint32_t)((uint32_t)(0x531ULL)))) { local_rdi = (uint32_t)((uint32_t)(0x531ULL)); }
    v_stack_m88 = (uint32_t)(local_rdi);
    goto loc_003C32BB;
loc_003C33CA:
    if (v_stack_p20 == 0) goto loc_003C32D6;
    result = KiClearForegroundBoost(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 760, (uint32_t)(0x531ULL), (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x30) - 0x2F8 + 0x233)))), 16);
    goto loc_003C32D6;
loc_003C33E1:
    v_stack_m88 = (uint32_t)((uint32_t)(0x531ULL));
loc_003C33F1:
    v_stack_p10 = 0;
    result = EtwTracePriority(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30)) - 760, (uint32_t)(0x530ULL), (uint32_t)(v_stack_m84), (uint32_t)((uint32_t)(local_r12)));
loc_003C341F:
    goto loc_003C3083;
loc_003C3429:
    local_rdi = 15;
    if (sign_flag) { local_rdi = (uint32_t)(local_rsi); }
    v_stack_m88 = (uint32_t)(local_rdi);
    goto loc_003C30AC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x90` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C2EC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
