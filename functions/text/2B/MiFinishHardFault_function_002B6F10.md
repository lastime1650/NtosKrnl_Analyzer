# MiFinishHardFault

- RVA: `0x002B6F10`–`0x002B780B` (길이 `2,299` bytes)
- VA: `0x00000001402B6F10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006DA28`
- 디코드: `522`개 명령, `2,299/2,299` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x002B6F5B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002B6F6A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002B7062` → [MiInvalidateCollidedIos](../38/MiInvalidateCollidedIos_function_00386110.md) (function, `0x00386110`)
- `0x002B7096` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x002B714F` → [MiInPageSkipPage](MiInPageSkipPage_function_002B7820.md) (function, `0x002B7820`)
- `0x002B7178` → [MiAddPageToInsertList](../24/MiAddPageToInsertList_function_0024A950.md) (function, `0x0024A950`)
- `0x002B7193` → [MiInsertPagesInList](../33/MiInsertPagesInList_function_0033E270.md) (function, `0x0033E270`)
- `0x002B71E8` → [MiHardFaultPageRelease](MiHardFaultPageRelease_function_002B5728.md) (function, `0x002B5728`)
- `0x002B7259` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x002B7272` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x002B72AC` → [MiFreeInPageSupportBlock](MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)
- `0x002B7314` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x002B7325` → [MiRelockFaultState](../36/MiRelockFaultState_function_0036A230.md) (function, `0x0036A230`)
- `0x002B7382` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B7401` → [MiCreateDecayPfn](MiCreateDecayPfn_function_002B8764.md) (function, `0x002B8764`)
- `0x002B742C` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x002B7447` → [MiRelockProtoPoolPage](../31/MiRelockProtoPoolPage_function_0031826C.md) (function, `0x0031826C`)
- `0x002B7468` → [MiIsFaultPteIntact](../32/MiIsFaultPteIntact_function_003288A0.md) (function, `0x003288A0`)
- `0x002B748D` → [MiDecayPfnFullyInitialized](../44/MiDecayPfnFullyInitialized_function_00447748.md) (function, `0x00447748`)
- `0x002B74B9` → [MmCheckCachedPageStates](../2F/MmCheckCachedPageStates_function_002F6C60.md) (function, `0x002F6C60`)
- `0x002B7546` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002B7579` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x002B7586` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002B7595` → [MiInPageGapPage](../38/MiInPageGapPage_function_003818A0.md) (function, `0x003818A0`)
- `0x002B7619` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x002B7654` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002B7693` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B76A2` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B76BA` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B76CA` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B7713` → [MiReturnPfnReferenceCountAtDpc](../36/MiReturnPfnReferenceCountAtDpc_function_00364010.md) (function, `0x00364010`)
- `0x002B7728` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B7738` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B777A` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002B77A7` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x002B77C5` → [MiIsRetryIoStatus](../40/MiIsRetryIoStatus_function_00408640.md) (function, `0x00408640`)
- `0x002B77F7` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)

### Direct callers
- [MiPfCompleteInPageSupport](../36/MiPfCompleteInPageSupport_function_0036D738.md) at `0x0036D7F1`
- [MiIssueHardFault](../38/MiIssueHardFault_function_00380074.md) at `0x0038033A`

### Static image references
- `0x002B72F0` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002B7352` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002B75D1` → RVA `0x00E30088` (`.data`; read)
- `0x002B7685` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x002B776C` → [sub_006DBADA](../6D/Unknown_function_006DBADA.md) (`tail-transfer`)
  - `0x002B7780` → [sub_006DBADA](../6D/Unknown_function_006DBADA.md) (`tail-transfer`)
  - `0x002B77A1` → [sub_006DBADA + 0x30](../6D/Unknown_function_006DBADA.md) (`tail-transfer`)
  - `0x002B77AD` → [sub_006DBADA + 0x35](../6D/Unknown_function_006DBADA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002B6F10  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
002B6F15  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
002B6F1A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
002B6F1F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
002B6F24  55                              push rbp
002B6F25  53                              push rbx
002B6F26  56                              push rsi
002B6F27  57                              push rdi
002B6F28  41 54                           push r12
002B6F2A  41 55                           push r13
002B6F2C  41 56                           push r14
002B6F2E  41 57                           push r15
002B6F30  48 8D 6C 24 B8                  lea rbp, [rsp - 0x48]
002B6F35  48 81 EC 48 01 00 00            sub rsp, 0x148
002B6F3C  33 C0                           xor eax, eax
002B6F3E  49 8B F8                        mov rdi, r8
002B6F41  4C 8B E1                        mov r12, rcx
002B6F44  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002B6F49  0F 57 C0                        xorps xmm0, xmm0
002B6F4C  48 8D 4D D0                     lea rcx, [rbp - 0x30]
002B6F50  33 D2                           xor edx, edx
002B6F52  44 8D 40 68                     lea r8d, [rax + 0x68]
002B6F56  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
002B6F5B  E8 E0 FC 40 00                  call 0x1406c6c40
002B6F60  33 D2                           xor edx, edx
002B6F62  48 8D 4D 80                     lea rcx, [rbp - 0x80]
002B6F66  44 8D 42 40                     lea r8d, [rdx + 0x40]
002B6F6A  E8 D1 FC 40 00                  call 0x1406c6c40
002B6F6F  48 8B 87 E8 00 00 00            mov rax, qword ptr [rdi + 0xe8]
002B6F76  4C 8D 87 10 01 00 00            lea r8, [rdi + 0x110]
002B6F7D  49 8B 54 24 38                  mov rdx, qword ptr [r12 + 0x38]
002B6F82  4C 8B BF 98 00 00 00            mov r15, qword ptr [rdi + 0x98]
002B6F89  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
002B6F8D  48 8B 87 00 01 00 00            mov rax, qword ptr [rdi + 0x100]
002B6F94  48 85 C0                        test rax, rax
002B6F97  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
002B6F9C  4C 0F 45 C0                     cmovne r8, rax
002B6FA0  45 33 ED                        xor r13d, r13d
002B6FA3  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
002B6FA8  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
002B6FAD  41 8B 48 2C                     mov ecx, dword ptr [r8 + 0x2c]
002B6FB1  49 8D 70 30                     lea rsi, [r8 + 0x30]
002B6FB5  49 03 48 20                     add rcx, qword ptr [r8 + 0x20]
002B6FB9  41 8B 40 28                     mov eax, dword ptr [r8 + 0x28]
002B6FBD  81 E1 FF 0F 00 00               and ecx, 0xfff
002B6FC3  48 05 FF 0F 00 00               add rax, 0xfff
002B6FC9  48 03 C1                        add rax, rcx
002B6FCC  48 C1 E8 0C                     shr rax, 0xc
002B6FD0  48 FF C8                        dec rax
002B6FD3  48 8D 04 C6                     lea rax, [rsi + rax*8]
002B6FD7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002B6FDC  8B 87 BC 00 00 00               mov eax, dword ptr [rdi + 0xbc]
002B6FE2  83 F8 FF                        cmp eax, -1
002B6FE5  0F 85 E9 06 00 00               jne 0x1402b76d4
002B6FEB  48 C7 45 98 FF FF FF FF         mov qword ptr [rbp - 0x68], 0xffffffffffffffff
002B6FF3  48 8B 87 E0 00 00 00            mov rax, qword ptr [rdi + 0xe0]
002B6FFA  4C 8B B7 A0 00 00 00            mov r14, qword ptr [rdi + 0xa0]
002B7001  8B 9F C0 00 00 00               mov ebx, dword ptr [rdi + 0xc0]
002B7007  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002B700C  B8 01 00 00 00                  mov eax, 1
002B7011  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
002B7015  0F BA E3 15                     bt ebx, 0x15
002B7019  0F 83 A9 02 00 00               jae 0x1402b72c8
002B701F  C7 45 88 34 04 00 C0            mov dword ptr [rbp - 0x78], 0xc0000434
002B7026  C6 44 24 20 11                  mov byte ptr [rsp + 0x20], 0x11
002B702B  48 85 D2                        test rdx, rdx
002B702E  0F 85 AF 02 00 00               jne 0x1402b72e3
002B7034  B0 11                           mov al, 0x11
002B7036  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002B703B  4D 85 F6                        test r14, r14
002B703E  0F 85 F5 03 00 00               jne 0x1402b7439
002B7044  8B 87 B4 00 00 00               mov eax, dword ptr [rdi + 0xb4]
002B704A  85 C0                           test eax, eax
002B704C  0F 85 F0 06 00 00               jne 0x1402b7742
002B7052  44 8B 67 50                     mov r12d, dword ptr [rdi + 0x50]
002B7056  48 8D 47 10                     lea rax, [rdi + 0x10]
002B705A  48 39 00                        cmp qword ptr [rax], rax
002B705D  74 19                           je 0x1402b7078
002B705F  48 8B CF                        mov rcx, rdi
002B7062  E8 A9 F0 0C 00                  call 0x140386110
002B7067  88 45 A9                        mov byte ptr [rbp - 0x57], al
002B706A  84 C0                           test al, al
002B706C  0F 84 6F 06 00 00               je 0x1402b76e1
002B7072  8B 87 C0 00 00 00               mov eax, dword ptr [rdi + 0xc0]
002B7078  8B 9F C0 00 00 00               mov ebx, dword ptr [rdi + 0xc0]
002B707E  4D 85 F6                        test r14, r14
002B7081  74 27                           je 0x1402b70aa
002B7083  45 8B FD                        mov r15d, r13d
002B7086  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
002B708D  0F 82 FD 02 00 00               jb 0x1402b7390
002B7093  49 8B CE                        mov rcx, r14
002B7096  E8 35 E9 F8 FF                  call 0x1402459d0
002B709B  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B70A5  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
002B70AA  0F BA E3 1A                     bt ebx, 0x1a
002B70AE  0F 82 12 05 00 00               jb 0x1402b75c6
002B70B4  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
002B70B9  44 8B 7D 88                     mov r15d, dword ptr [rbp - 0x78]
002B70BD  45 85 FF                        test r15d, r15d
002B70C0  0F 89 8B 03 00 00               jns 0x1402b7451
002B70C6  45 85 E4                        test r12d, r12d
002B70C9  0F 89 E2 02 00 00               jns 0x1402b73b1
002B70CF  49 8B CD                        mov rcx, r13
002B70D2  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
002B70D6  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
002B70DD  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
002B70E2  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
002B70E7  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
002B70EB  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
002B70EF  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
002B70F3  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
002B70FA  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
002B70FE  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
002B7108  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
002B710C  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
002B7110  B8 02 00 00 00                  mov eax, 2
002B7115  89 45 30                        mov dword ptr [rbp + 0x30], eax
002B7118  44 89 6D F0                     mov dword ptr [rbp - 0x10], r13d
002B711C  48 89 4D 28                     mov qword ptr [rbp + 0x28], rcx
002B7120  48 3B 74 24 28                  cmp rsi, qword ptr [rsp + 0x28]
002B7125  77 66                           ja 0x1402b718d
002B7127  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
002B712C  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
002B7131  49 BD 00 00 00 00 00 DE FF FF   movabs r13, 0xffffde0000000000
002B713B  48 8B 06                        mov rax, qword ptr [rsi]
002B713E  48 8D 14 40                     lea rdx, [rax + rax*2]
002B7142  48 C1 E2 04                     shl rdx, 4
002B7146  49 8B C5                        mov rax, r13
002B7149  48 03 D0                        add rdx, rax
002B714C  48 8B CA                        mov rcx, rdx
002B714F  E8 CC 06 00 00                  call 0x1402b7820
002B7154  85 C0                           test eax, eax
002B7156  0F 85 39 04 00 00               jne 0x1402b7595
002B715C  48 3B 97 F8 00 00 00            cmp rdx, qword ptr [rdi + 0xf8]
002B7163  0F 84 D5 01 00 00               je 0x1402b733e
002B7169  4C 8B 06                        mov r8, qword ptr [rsi]
002B716C  48 8D 55 80                     lea rdx, [rbp - 0x80]
002B7170  48 8D 4D D0                     lea rcx, [rbp - 0x30]
002B7174  48 89 75 90                     mov qword ptr [rbp - 0x70], rsi
002B7178  E8 D3 37 F9 FF                  call 0x14024a950
002B717D  48 83 C6 08                     add rsi, 8
002B7181  49 3B F6                        cmp rsi, r14
002B7184  76 B5                           jbe 0x1402b713b
002B7186  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
002B718A  45 33 ED                        xor r13d, r13d
002B718D  33 D2                           xor edx, edx
002B718F  48 8D 4D D0                     lea rcx, [rbp - 0x30]
002B7193  E8 D8 70 08 00                  call 0x14033e270
002B7198  48 85 DB                        test rbx, rbx
002B719B  0F 85 50 05 00 00               jne 0x1402b76f1
002B71A1  48 8B 9F F8 00 00 00            mov rbx, qword ptr [rdi + 0xf8]
002B71A8  41 8B F5                        mov esi, r13d
002B71AB  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
002B71B2  0F 82 98 01 00 00               jb 0x1402b7350
002B71B8  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
002B71BB  48 8D 4D 80                     lea rcx, [rbp - 0x80]
002B71BF  89 85 A8 00 00 00               mov dword ptr [rbp + 0xa8], eax
002B71C5  48 8B D3                        mov rdx, rbx
002B71C8  C1 E8 10                        shr eax, 0x10
002B71CB  24 DF                           and al, 0xdf
002B71CD  88 85 AA 00 00 00               mov byte ptr [rbp + 0xaa], al
002B71D3  8B 85 A8 00 00 00               mov eax, dword ptr [rbp + 0xa8]
002B71D9  89 43 20                        mov dword ptr [rbx + 0x20], eax
002B71DC  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
002B71E1  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
002B71E5  4C 89 2B                        mov qword ptr [rbx], r13
002B71E8  E8 3B E5 FF FF                  call 0x1402b5728
002B71ED  8B 77 50                        mov esi, dword ptr [rdi + 0x50]
002B71F0  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
002B71FA  48 8B 87 F8 00 00 00            mov rax, qword ptr [rdi + 0xf8]
002B7201  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
002B7205  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
002B720A  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
002B720F  4D 85 F6                        test r14, r14
002B7212  0F 85 57 01 00 00               jne 0x1402b736f
002B7218  8B 87 C0 00 00 00               mov eax, dword ptr [rdi + 0xc0]
002B721E  0F BA E0 11                     bt eax, 0x11
002B7222  0F 82 6F 02 00 00               jb 0x1402b7497
002B7228  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
002B722C  48 85 C9                        test rcx, rcx
002B722F  0F 85 4C 02 00 00               jne 0x1402b7481
002B7235  48 83 7C 24 68 00               cmp qword ptr [rsp + 0x68], 0
002B723B  8B 9F C0 00 00 00               mov ebx, dword ptr [rdi + 0xc0]
002B7241  0F 85 CB 01 00 00               jne 0x1402b7412
002B7247  0F BA E3 16                     bt ebx, 0x16
002B724B  72 11                           jb 0x1402b725e
002B724D  48 8B 8F C8 00 00 00            mov rcx, qword ptr [rdi + 0xc8]
002B7254  BA 4D 6D 53 63                  mov edx, 0x63536d4d
002B7259  E8 42 CC FA FF                  call 0x140263ea0
002B725E  8B 87 B0 00 00 00               mov eax, dword ptr [rdi + 0xb0]
002B7264  83 F8 01                        cmp eax, 1
002B7267  7E 0E                           jle 0x1402b7277
002B7269  48 8D 4F 38                     lea rcx, [rdi + 0x38]
002B726D  45 33 C0                        xor r8d, r8d
002B7270  33 D2                           xor edx, edx
002B7272  E8 99 80 08 00                  call 0x14033f310
002B7277  48 8B 4F 68                     mov rcx, qword ptr [rdi + 0x68]
002B727B  48 85 C9                        test rcx, rcx
002B727E  0F 85 01 05 00 00               jne 0x1402b7785
002B7284  85 F6                           test esi, esi
002B7286  0F 88 26 05 00 00               js 0x1402b77b2
002B728C  80 7D A8 00                     cmp byte ptr [rbp - 0x58], 0
002B7290  B8 34 04 00 C0                  mov eax, 0xc0000434
002B7295  8B 75 88                        mov esi, dword ptr [rbp - 0x78]
002B7298  0F 44 F0                        cmove esi, eax
002B729B  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
002B72A0  48 85 C9                        test rcx, rcx
002B72A3  0F 85 3C 05 00 00               jne 0x1402b77e5
002B72A9  48 8B CF                        mov rcx, rdi
002B72AC  E8 4F E6 FF FF                  call 0x1402b5900
002B72B1  8B C6                           mov eax, esi
002B72B3  48 81 C4 48 01 00 00            add rsp, 0x148
002B72BA  41 5F                           pop r15
002B72BC  41 5E                           pop r14
002B72BE  41 5D                           pop r13
002B72C0  41 5C                           pop r12
002B72C2  5F                              pop rdi
002B72C3  5E                              pop rsi
002B72C4  5B                              pop rbx
002B72C5  5D                              pop rbp
002B72C6  C3                              ret
002B72C7  CC                              int3
002B72C8  48 85 D2                        test rdx, rdx
002B72CB  0F 84 4E FD FF FF               je 0x1402b701f
002B72D1  F6 C3 20                        test bl, 0x20
002B72D4  0F 85 45 FD FF FF               jne 0x1402b701f
002B72DA  44 89 6D 88                     mov dword ptr [rbp - 0x78], r13d
002B72DE  C6 44 24 20 11                  mov byte ptr [rsp + 0x20], 0x11
002B72E3  44 0F 20 C1                     mov rcx, cr8
002B72E7  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
002B72EC  44 0F 22 C0                     mov cr8, rax
002B72F0  44 39 2D 29 FA D0 00            cmp dword ptr [rip + 0xd0fa29], r13d
002B72F7  0F 85 86 02 00 00               jne 0x1402b7583
002B72FD  0F BA E3 19                     bt ebx, 0x19
002B7301  72 16                           jb 0x1402b7319
002B7303  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
002B7309  A8 0F                           test al, 0xf
002B730B  0F 85 47 02 00 00               jne 0x1402b7558
002B7311  49 8B CF                        mov rcx, r15
002B7314  E8 D7 7C FA FF                  call 0x14025eff0
002B7319  48 8B 95 98 00 00 00            mov rdx, qword ptr [rbp + 0x98]
002B7320  49 8D 4C 24 38                  lea rcx, [r12 + 0x38]
002B7325  E8 06 2F 0B 00                  call 0x14036a230
002B732A  48 8B 8D 90 00 00 00            mov rcx, qword ptr [rbp + 0x90]
002B7331  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
002B7336  88 41 44                        mov byte ptr [rcx + 0x44], al
002B7339  E9 FD FC FF FF                  jmp 0x1402b703b
002B733E  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
002B7343  E9 35 FE FF FF                  jmp 0x1402b717d
002B7348  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002B7350  FF C6                           inc esi
002B7352  85 35 54 DF D0 00               test dword ptr [rip + 0xd0df54], esi
002B7358  0F 84 27 03 00 00               je 0x1402b7685
002B735E  F3 90                           pause
002B7360  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
002B7364  48 85 C0                        test rax, rax
002B7367  0F 89 3E FE FF FF               jns 0x1402b71ab
002B736D  EB E1                           jmp 0x1402b7350
002B736F  0F B6 54 24 20                  movzx edx, byte ptr [rsp + 0x20]
002B7374  41 80 FF 11                     cmp r15b, 0x11
002B7378  74 05                           je 0x1402b737f
002B737A  BA 11 00 00 00                  mov edx, 0x11
002B737F  49 8B CE                        mov rcx, r14
002B7382  E8 09 ED F8 FF                  call 0x140246090
002B7387  E9 8C FE FF FF                  jmp 0x1402b7218
002B738C  0F 1F 40 00                     nop dword ptr [rax]
002B7390  41 FF C7                        inc r15d
002B7393  44 85 3D 12 DF D0 00            test dword ptr [rip + 0xd0df12], r15d
002B739A  0F 84 0C 03 00 00               je 0x1402b76ac
002B73A0  F3 90                           pause
002B73A2  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B73A6  48 85 C0                        test rax, rax
002B73A9  0F 89 D7 FC FF FF               jns 0x1402b7086
002B73AF  EB DF                           jmp 0x1402b7390
002B73B1  F6 C3 20                        test bl, 0x20
002B73B4  75 2B                           jne 0x1402b73e1
002B73B6  4C 39 AF 00 01 00 00            cmp qword ptr [rdi + 0x100], r13
002B73BD  75 22                           jne 0x1402b73e1
002B73BF  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
002B73C4  48 8D 41 30                     lea rax, [rcx + 0x30]
002B73C8  48 39 44 24 28                  cmp qword ptr [rsp + 0x28], rax
002B73CD  0F 84 FC FC FF FF               je 0x1402b70cf
002B73D3  48 8D 41 38                     lea rax, [rcx + 0x38]
002B73D7  48 39 45 98                     cmp qword ptr [rbp - 0x68], rax
002B73DB  0F 86 EE FC FF FF               jbe 0x1402b70cf
002B73E1  F7 C3 00 38 00 00               test ebx, 0x3800
002B73E7  0F 95 C1                        setne cl
002B73EA  81 E3 00 00 12 00               and ebx, 0x120000
002B73F0  81 FB 00 00 10 00               cmp ebx, 0x100000
002B73F6  0F 94 C0                        sete al
002B73F9  84 C8                           test al, cl
002B73FB  0F 84 CE FC FF FF               je 0x1402b70cf
002B7401  E8 5E 13 00 00                  call 0x1402b8764
002B7406  48 8B C8                        mov rcx, rax
002B7409  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
002B740D  E9 C4 FC FF FF                  jmp 0x1402b70d6
002B7412  0F BA E3 19                     bt ebx, 0x19
002B7416  0F 83 2B FE FF FF               jae 0x1402b7247
002B741C  48 8B 8D 90 00 00 00            mov rcx, qword ptr [rbp + 0x90]
002B7423  45 33 C0                        xor r8d, r8d
002B7426  48 83 C1 38                     add rcx, 0x38
002B742A  B2 11                           mov dl, 0x11
002B742C  E8 5F 5E FC FF                  call 0x14027d290
002B7431  41 B7 11                        mov r15b, 0x11
002B7434  E9 0E FE FF FF                  jmp 0x1402b7247
002B7439  3C 11                           cmp al, 0x11
002B743B  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
002B7440  49 8B CE                        mov rcx, r14
002B7443  49 0F 45 D5                     cmovne rdx, r13
002B7447  E8 20 0E 06 00                  call 0x14031826c
002B744C  E9 F3 FB FF FF                  jmp 0x1402b7044
002B7451  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
002B7455  4C 8D 8F A8 00 00 00            lea r9, [rdi + 0xa8]
002B745C  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
002B7461  48 8B 8D 90 00 00 00            mov rcx, qword ptr [rbp + 0x90]
002B7468  E8 33 14 07 00                  call 0x1403288a0
002B746D  85 C0                           test eax, eax
002B746F  B8 34 04 00 C0                  mov eax, 0xc0000434
002B7474  44 0F 44 F8                     cmove r15d, eax
002B7478  44 89 7D 88                     mov dword ptr [rbp - 0x78], r15d
002B747C  E9 45 FC FF FF                  jmp 0x1402b70c6
002B7481  41 80 FF 11                     cmp r15b, 0x11
002B7485  BA 00 00 00 00                  mov edx, 0
002B748A  0F 95 C2                        setne dl
002B748D  E8 B6 02 19 00                  call 0x140447748
002B7492  E9 9E FD FF FF                  jmp 0x1402b7235
002B7497  8B 4F 60                        mov ecx, dword ptr [rdi + 0x60]
002B749A  41 BC 02 00 00 00               mov r12d, 2
002B74A0  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
002B74A5  81 E1 FF FF 03 00               and ecx, 0x3ffff
002B74AB  48 03 4C 24 60                  add rcx, qword ptr [rsp + 0x60]
002B74B0  45 33 C9                        xor r9d, r9d
002B74B3  45 8B C4                        mov r8d, r12d
002B74B6  8B 53 28                        mov edx, dword ptr [rbx + 0x28]
002B74B9  E8 A2 F7 03 00                  call 0x1402f6c60
002B74BE  48 83 C3 30                     add rbx, 0x30
002B74C2  44 89 AD A8 00 00 00            mov dword ptr [rbp + 0xa8], r13d
002B74C9  41 80 FF 11                     cmp r15b, 0x11
002B74CD  0F 85 AA 01 00 00               jne 0x1402b767d
002B74D3  45 0F 20 C6                     mov r14, cr8
002B74D7  45 0F 22 C4                     mov cr8, r12
002B74DB  83 3D 3E F8 D0 00 00            cmp dword ptr [rip + 0xd0f83e], 0
002B74E2  0F 85 64 01 00 00               jne 0x1402b764c
002B74E8  48 3B 5C 24 28                  cmp rbx, qword ptr [rsp + 0x28]
002B74ED  77 3C                           ja 0x1402b752b
002B74EF  48 8B 74 24 28                  mov rsi, qword ptr [rsp + 0x28]
002B74F4  4C 8D 63 08                     lea r12, [rbx + 8]
002B74F8  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
002B7502  48 8B 03                        mov rax, qword ptr [rbx]
002B7505  48 85 C0                        test rax, rax
002B7508  0F 88 E1 00 00 00               js 0x1402b75ef
002B750E  48 83 C3 08                     add rbx, 8
002B7512  49 83 C4 08                     add r12, 8
002B7516  48 3B DE                        cmp rbx, rsi
002B7519  76 E7                           jbe 0x1402b7502
002B751B  48 8B BD A0 00 00 00            mov rdi, qword ptr [rbp + 0xa0]
002B7522  8B 74 24 38                     mov esi, dword ptr [rsp + 0x38]
002B7526  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
002B752B  41 80 FE 11                     cmp r14b, 0x11
002B752F  0F 84 F3 FC FF FF               je 0x1402b7228
002B7535  83 3D E4 F7 D0 00 00            cmp dword ptr [rip + 0xd0f7e4], 0
002B753C  74 0D                           je 0x1402b754b
002B753E  44 0F 20 C1                     mov rcx, cr8
002B7542  41 0F B6 D6                     movzx edx, r14b
002B7546  E8 4D E1 23 00                  call 0x1404f5698
002B754B  41 0F B6 C6                     movzx eax, r14b
002B754F  44 0F 22 C0                     mov cr8, rax
002B7553  E9 D0 FC FF FF                  jmp 0x1402b7228
002B7558  90                              nop
002B7559  66 41 83 87 E6 01 00 00 01      add word ptr [r15 + 0x1e6], 1
002B7562  0F 85 B1 FD FF FF               jne 0x1402b7319
002B7568  49 8D 87 98 00 00 00            lea rax, [r15 + 0x98]
002B756F  90                              nop
002B7570  48 39 00                        cmp qword ptr [rax], rax
002B7573  0F 84 A0 FD FF FF               je 0x1402b7319
002B7579  E8 02 B7 02 00                  call 0x1402e2c80
002B757E  E9 96 FD FF FF                  jmp 0x1402b7319
002B7583  0F B6 D0                        movzx edx, al
002B7586  E8 71 E1 23 00                  call 0x1404f56fc
002B758B  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002B7590  E9 68 FD FF FF                  jmp 0x1402b72fd
002B7595  E8 06 A3 0C 00                  call 0x1403818a0
002B759A  85 C0                           test eax, eax
002B759C  0F 84 DB FB FF FF               je 0x1402b717d
002B75A2  4D 85 FF                        test r15, r15
002B75A5  4C 89 22                        mov qword ptr [rdx], r12
002B75A8  4C 8B E2                        mov r12, rdx
002B75AB  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
002B75B0  4C 0F 44 FA                     cmove r15, rdx
002B75B4  48 FF C3                        inc rbx
002B75B7  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
002B75BC  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
002B75C1  E9 B7 FB FF FF                  jmp 0x1402b717d
002B75C6  48 8B 87 F8 00 00 00            mov rax, qword ptr [rdi + 0xf8]
002B75CD  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
002B75D1  48 8B 0D B0 8A B7 00            mov rcx, qword ptr [rip + 0xb78ab0]
002B75D8  48 C1 E8 2B                     shr rax, 0x2b
002B75DC  25 FF 03 00 00                  and eax, 0x3ff
002B75E1  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
002B75E5  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
002B75EA  E9 CA FA FF FF                  jmp 0x1402b70b9
002B75EF  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
002B75F9  48 23 C1                        and rax, rcx
002B75FC  48 89 03                        mov qword ptr [rbx], rax
002B75FF  4C 8D 3C 40                     lea r15, [rax + rax*2]
002B7603  49 C1 E7 04                     shl r15, 4
002B7607  48 8B C7                        mov rax, rdi
002B760A  4C 03 F8                        add r15, rax
002B760D  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002B7614  72 4A                           jb 0x1402b7660
002B7616  49 8B CF                        mov rcx, r15
002B7619  E8 B2 E3 F8 FF                  call 0x1402459d0
002B761E  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B7628  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
002B762D  8B 8D A8 00 00 00               mov ecx, dword ptr [rbp + 0xa8]
002B7633  FF C1                           inc ecx
002B7635  89 8D A8 00 00 00               mov dword ptr [rbp + 0xa8], ecx
002B763B  F6 C1 3F                        test cl, 0x3f
002B763E  0F 84 0E 01 00 00               je 0x1402b7752
002B7644  45 33 ED                        xor r13d, r13d
002B7647  E9 C2 FE FF FF                  jmp 0x1402b750e
002B764C  41 0F B6 D4                     movzx edx, r12b
002B7650  41 0F B6 CE                     movzx ecx, r14b
002B7654  E8 A3 E0 23 00                  call 0x1404f56fc
002B7659  E9 8A FE FF FF                  jmp 0x1402b74e8
002B765E  66 90                           nop
002B7660  41 FF C5                        inc r13d
002B7663  44 85 2D 42 DC D0 00            test dword ptr [rip + 0xd0dc42], r13d
002B766A  0F 84 AA 00 00 00               je 0x1402b771a
002B7670  F3 90                           pause
002B7672  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B7676  48 85 C0                        test rax, rax
002B7679  79 92                           jns 0x1402b760d
002B767B  EB E3                           jmp 0x1402b7660
002B767D  41 B6 11                        mov r14b, 0x11
002B7680  E9 63 FE FF FF                  jmp 0x1402b74e8
002B7685  8B 05 2D F4 D0 00               mov eax, dword ptr [rip + 0xd0f42d]
002B768B  A8 40                           test al, 0x40
002B768D  0F 84 CB FC FF FF               je 0x1402b735e
002B7693  E8 F8 7D 05 00                  call 0x14030f490
002B7698  84 C0                           test al, al
002B769A  0F 84 BE FC FF FF               je 0x1402b735e
002B76A0  8B CE                           mov ecx, esi
002B76A2  E8 B9 7D 05 00                  call 0x14030f460
002B76A7  E9 B4 FC FF FF                  jmp 0x1402b7360
002B76AC  8B 05 06 F4 D0 00               mov eax, dword ptr [rip + 0xd0f406]
002B76B2  A8 40                           test al, 0x40
002B76B4  0F 84 E6 FC FF FF               je 0x1402b73a0
002B76BA  E8 D1 7D 05 00                  call 0x14030f490
002B76BF  84 C0                           test al, al
002B76C1  0F 84 D9 FC FF FF               je 0x1402b73a0
002B76C7  41 8B CF                        mov ecx, r15d
002B76CA  E8 91 7D 05 00                  call 0x14030f460
002B76CF  E9 CE FC FF FF                  jmp 0x1402b73a2
002B76D4  48 8D 0C C6                     lea rcx, [rsi + rax*8]
002B76D8  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
002B76DC  E9 12 F9 FF FF                  jmp 0x1402b6ff3
002B76E1  C7 47 50 17 00 00 C0            mov dword ptr [rdi + 0x50], 0xc0000017
002B76E8  4C 89 6F 58                     mov qword ptr [rdi + 0x58], r13
002B76EC  E9 87 F9 FF FF                  jmp 0x1402b7078
002B76F1  49 8B CC                        mov rcx, r12
002B76F4  4D 85 E4                        test r12, r12
002B76F7  0F 84 A4 FA FF FF               je 0x1402b71a1
002B76FD  4D 8B 24 24                     mov r12, qword ptr [r12]
002B7701  48 83 6C 24 50 01               sub qword ptr [rsp + 0x50], 1
002B7707  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
002B770C  75 05                           jne 0x1402b7713
002B770E  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
002B7713  E8 F8 C8 0A 00                  call 0x140364010
002B7718  EB D7                           jmp 0x1402b76f1
002B771A  8B 05 98 F3 D0 00               mov eax, dword ptr [rip + 0xd0f398]
002B7720  A8 40                           test al, 0x40
002B7722  0F 84 48 FF FF FF               je 0x1402b7670
002B7728  E8 63 7D 05 00                  call 0x14030f490
002B772D  84 C0                           test al, al
002B772F  0F 84 3B FF FF FF               je 0x1402b7670
002B7735  41 8B CD                        mov ecx, r13d
002B7738  E8 23 7D 05 00                  call 0x14030f460
002B773D  E9 30 FF FF FF                  jmp 0x1402b7672
002B7742  C7 47 50 9A 00 00 C0            mov dword ptr [rdi + 0x50], 0xc000009a
002B7749  4C 89 6F 58                     mov qword ptr [rdi + 0x58], r13
002B774D  E9 00 F9 FF FF                  jmp 0x1402b7052
002B7752  4C 3B E6                        cmp r12, rsi
002B7755  0F 87 E9 FE FF FF               ja 0x1402b7644
002B775B  41 80 FE 11                     cmp r14b, 0x11
002B775F  0F 84 DF FE FF FF               je 0x1402b7644
002B7765  83 3D B4 F5 D0 00 00            cmp dword ptr [rip + 0xd0f5b4], 0
002B776C  0F 84 68 43 42 00               je 0x1406dbada
002B7772  44 0F 20 C1                     mov rcx, cr8
002B7776  41 0F B6 D6                     movzx edx, r14b
002B777A  E8 19 DF 23 00                  call 0x1404f5698
002B777F  90                              nop
002B7780  E9 55 43 42 00                  jmp 0x1406dbada
002B7785  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
002B7789  48 8B 15 F8 88 B7 00            mov rdx, qword ptr [rip + 0xb788f8]
002B7790  48 C1 E8 2B                     shr rax, 0x2b
002B7794  25 FF 03 00 00                  and eax, 0x3ff
002B7799  48 8B 1C C2                     mov rbx, qword ptr [rdx + rax*8]
002B779D  41 80 FF 11                     cmp r15b, 0x11
002B77A1  0F 84 63 43 42 00               je 0x1406dbb0a
002B77A7  E8 A4 D3 07 00                  call 0x140334b50
002B77AC  90                              nop
002B77AD  E9 5D 43 42 00                  jmp 0x1406dbb0f
002B77B2  8B 5F 70                        mov ebx, dword ptr [rdi + 0x70]
002B77B5  F6 C3 01                        test bl, 1
002B77B8  0F 84 DD FA FF FF               je 0x1402b729b
002B77BE  BA 00 10 00 00                  mov edx, 0x1000
002B77C3  8B CE                           mov ecx, esi
002B77C5  E8 76 0E 15 00                  call 0x140408640
002B77CA  85 C0                           test eax, eax
002B77CC  0F 84 C9 FA FF FF               je 0x1402b729b
002B77D2  F6 C3 02                        test bl, 2
002B77D5  0F 85 C0 FA FF FF               jne 0x1402b729b
002B77DB  BE 34 04 00 C0                  mov esi, 0xc0000434
002B77E0  E9 B6 FA FF FF                  jmp 0x1402b729b
002B77E5  8B 9F C0 00 00 00               mov ebx, dword ptr [rdi + 0xc0]
002B77EB  BA 4D 6D 49 70                  mov edx, 0x70496d4d
002B77F0  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
002B77F7  E8 74 B6 08 00                  call 0x140342e70
002B77FC  0F BA F3 1A                     btr ebx, 0x1a
002B7800  89 9F C0 00 00 00               mov dword ptr [rdi + 0xc0], ebx
002B7806  E9 9E FA FF FF                  jmp 0x1402b72a9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFinishHardFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int8 v_stack_m168;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int8 v_stack_mDF;
    unsigned __int8 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p22;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (328);
    result = 0;
    v_stack_m138 = 0;
    a2 = 0;
    v_stack_m148 = v_xmm0;
    result = memset(v_stack_mB8, a2, result + 104, a4);
    a2 = 0;
    result = memset(v_stack_m108, a2, a2 + 64, a4);
    v_stack_mC8 = *(unsigned __int64 *)(a3 + 232);
    v_stack_m120 = *(unsigned __int64 *)(a1 + 56);
    a3 = a3 + 272;
    if (*(unsigned __int64 *)(a3 + 256) != 0) { a3 = *(unsigned __int64 *)(a3 + 256); }
    v_r13 = 0;
    v_stack_m130 = a3;
    v_stack_m150 = 0;
    a1 = ((unsigned int)(*(unsigned int *)(a3 + 44))) + (*(unsigned __int64 *)(a3 + 32));
    a1 = (unsigned int)((a1) & (0xFFFULL));
    result = ((unsigned int)(*(unsigned int *)(a3 + 40))) + (0xFFFULL);
    result = (result) + (a1);
    result = (result) >> (12);
    result = (result) - 1;
    v_stack_m160 = a3 + 48 + result * 8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 188)))) != -1) goto loc_002B76D4;
    v_stack_mF0 = -1;
loc_002B6FF3:
    v_stack_m128 = *(unsigned __int64 *)(a3 + 224);
    v_stack_mC0 = *(unsigned __int64 *)(a3 + 160);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 188)))) >= -1) goto loc_002B72C8;
loc_002B701F:
    v_stack_m100 = 0xC0000434ULL;
    v_stack_m168 = 17;
    if (*(unsigned __int64 *)(a1 + 56) != 0) goto loc_002B72E3;
    v_stack_m158 = 17;
loc_002B703B:
    if (*(unsigned __int64 *)(a3 + 160) != 0) goto loc_002B7439;
loc_002B7044:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 180))) != 0) goto loc_002B7742;
loc_002B7052:
    if ((*(unsigned __int64 *)(a3 + 16)) == (a3 + 16)) goto loc_002B7078;
    result = MiInvalidateCollidedIos(a3, *(unsigned __int64 *)(a1 + 56), a3, a4);
    v_stack_mDF = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_002B76E1;
loc_002B7078:
    if (*(unsigned __int64 *)(a3 + 160) == 0) goto loc_002B70AA;
loc_002B7086:
    if (condition_is_below) goto loc_002B7390;
    result = MiRemoveLockedPageChargeAndDecRef(*(unsigned __int64 *)(a3 + 160), *(unsigned __int64 *)(a1 + 56), a3, a4);
loc_002B70AA:
    if (condition_is_below) goto loc_002B75C6;
    v_stack_m118 = 0;
loc_002B70B9:
    if (!sign_flag) goto loc_002B7451;
loc_002B70C6:
    if (!sign_flag) goto loc_002B73B1;
loc_002B70CF:
    v_stack_mD0 = 0;
loc_002B70D6:
    v_stack_m108 = a3;
    v_stack_mE8 = *(unsigned __int64 *)(v_stack_p8 + 56);
    v_stack_mD8 = v_stack_p20;
    v_stack_mA8 = v_stack_p20;
    v_stack_mA0 = v_stack_p20;
    v_stack_m58 = 2;
    v_stack_m98 = 0;
    v_stack_m60 = 0;
    if ((a3 + 48) > v_stack_m160) goto loc_002B718D;
loc_002B713B:
    a2 = (*(unsigned __int64 *)(a3 + 48) + *(unsigned __int64 *)(a3 + 48) * 2) << (4);
    a2 = (a2) + (0);
    result = MiInPageSkipPage(a2, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_002B7595;
    if (a2 == (*(unsigned __int64 *)(a3 + 248))) goto loc_002B733E;
    v_stack_mF8 = a3 + 48;
    result = MiAddPageToInsertList(v_stack_mB8, v_stack_m108, *(unsigned __int64 *)(a3 + 48), a4);
loc_002B717D:
    v_rsi = (a3 + 48) + (8);
    if (v_rsi <= v_stack_m160) goto loc_002B713B;
    v_r13 = 0;
loc_002B718D:
    a2 = 0;
    result = MiInsertPagesInList(v_stack_mB8, a2, *(unsigned __int64 *)(a3 + 48), a4);
    if (v_stack_m138 != 0) goto loc_002B76F1;
loc_002B71A1:
loc_002B71AB:
    if (condition_is_below) goto loc_002B7350;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 248) + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 248) + 32))) >> (16));
    result = (unsigned __int8)((result) & (223));
    v_stack_p22 = (unsigned __int8)(result);
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 248) + 32) = (unsigned int)((unsigned int)(v_stack_p20));
    v_stack_mF8 = v_stack_m150;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 248)) = 0;
    result = MiHardFaultPageRelease(v_stack_m108, *(unsigned __int64 *)(a3 + 248), *(unsigned __int64 *)(a3 + 48), a4);
    v_stack_m150 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 80)));
    if (v_stack_mC0 != 0) goto loc_002B736F;
loc_002B7218:
    if (condition_is_below) goto loc_002B7497;
loc_002B7228:
    if (v_stack_mD0 != 0) goto loc_002B7481;
loc_002B7235:
    if (v_stack_m120 != 0) goto loc_002B7412;
loc_002B7247:
    result = (unsigned int)(*(unsigned int *)(a3 + 192));
    if (v_stack_m120 >= 0) {
        a1 = *(unsigned __int64 *)(a3 + 200);
        a2 = 0x63536D4DULL;
        result = ObDereferenceObjectDeferDeleteWithTag(a1, a2, *(unsigned __int64 *)(a3 + 48), a4);
    }
    result = (unsigned int)(*(unsigned int *)(a3 + 176));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 176)))) >= = 1) {
        a1 = a3 + 56;
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a3 + 104) != 0) goto loc_002B7785;
    if (sign_flag) goto loc_002B77B2;
    v_rsi = (unsigned int)(v_stack_m100);
    if (v_stack_mE0 == 0) { v_rsi = (unsigned int)((unsigned int)(0xC0000434ULL)); }
loc_002B729B:
    if (v_stack_m118 != 0) goto loc_002B77E5;
loc_002B72A9:
    result = MiFreeInPageSupportBlock(0, a2, a3, a4);
    v_rsp = (v_rsp) + (328);
    return (unsigned int)((unsigned int)(v_rsi));
loc_002B72C8:
    if (0 == 0) goto loc_002B701F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 192)))) & (32)) != 0) goto loc_002B701F;
    v_stack_m100 = 0;
    v_stack_p20 = 17;
loc_002B72E3:
    v_stack_p30 = v_cr8;
    if ((*(unsigned int *)(v_rip + 13695529)) != 0) goto loc_002B7583;
loc_002B72FD:
    if ((*(unsigned int *)(v_rip + 13695529)) < 0) goto loc_002B7319;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 184)))) & (15)) != 0) goto loc_002B7558;
    result = KeLeaveCriticalRegionThread(v_stack_m158, a2, a3, a4);
loc_002B7319:
    result = MiRelockFaultState(v_stack_m148 + 56, v_stack_p10, a3, a4);
    *(unsigned __int8 *)(v_stack_p8 + 68) = (unsigned __int8)(v_stack_p30);
    goto loc_002B703B;
loc_002B733E:
    v_stack_p38 = v_rsi;
    goto loc_002B717D;
loc_002B7350:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 13688660)) & ((unsigned int)(v_rsi))) == 0) goto loc_002B7685;
loc_002B735E:
loc_002B7360:
    if (!sign_flag) goto loc_002B71AB;
    goto loc_002B7350;
loc_002B736F:
    if (((unsigned __int8)(v_stack_m158)) != 17) {
        a2 = 17;
    }
    result = MiUnlockProtoPoolPage(v_stack_mC0, a2, a3, a4);
    goto loc_002B7218;
loc_002B7390:
    v_r15 = (unsigned int)((v_stack_m158) + 1);
    if (((*(unsigned int *)(v_rip + 13688594)) & ((unsigned int)(v_r15))) == 0) goto loc_002B76AC;
loc_002B73A0:
loc_002B73A2:
    if (!sign_flag) goto loc_002B7086;
    goto loc_002B7390;
loc_002B73B1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 192)))) & (32)) != 0) goto loc_002B73E1;
    if ((*(unsigned __int64 *)(a3 + 256)) != 0) goto loc_002B73E1;
    if (v_stack_p28 == (v_stack_p58 + 48)) goto loc_002B70CF;
    if (v_stack_mF0 <= (v_stack_p58 + 56)) goto loc_002B70CF;
loc_002B73E1:
    a1 = ((((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 192)))) & (0x3800ULL)) != 0) ? 1 : 0;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 192))) & (0x120000ULL));
    result = (((unsigned int)(v_rbx)) == 0x100000ULL) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002B70CF;
    result = MiCreateDecayPfn(a1, a2, a3, a4);
    v_stack_mD0 = result;
    goto loc_002B70D6;
loc_002B7412:
    if (condition_is_above_or_equal) goto loc_002B7247;
    a3 = 0;
    a1 = (v_stack_p8) + (56);
    result = MiReleaseFaultState(a1, 17, a3, a4);
    goto loc_002B7247;
loc_002B7439:
    a2 = v_stack_p20;
    if (((unsigned __int8)(result)) != 17) { a2 = 0; }
    result = MiRelockProtoPoolPage(v_stack_mC0, a2, a3, a4);
    goto loc_002B7044;
loc_002B7451:
    result = MiIsFaultPteIntact(v_stack_p8, v_stack_p60, v_stack_mC8, a3 + 168);
    v_r15 = 17;
    if ((unsigned int)(result) == 0) { v_r15 = (unsigned int)((unsigned int)(0xC0000434ULL)); }
    v_stack_m100 = (unsigned int)(v_r15);
    goto loc_002B70C6;
loc_002B7481:
    a2 = (((unsigned __int8)(v_r15)) != 17) ? 1 : 0;
    result = MiDecayPfnFullyInitialized(v_stack_p8, a2, v_stack_mC8, a3 + 168);
    goto loc_002B7235;
loc_002B7497:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 96))) & (0x3FFFFULL));
    a1 = (a1) + (v_stack_p60);
    a4 = 0;
    result = MmCheckCachedPageStates(a1, (unsigned int)(*(unsigned int *)(v_stack_p58 + 40)), 2, a4);
    v_rbx = (v_stack_p58) + (48);
    v_stack_p20 = 0;
    if (((unsigned __int8)(v_r15)) != 17) goto loc_002B767D;
    if ((*(unsigned int *)(v_rip + 13695038)) != 0) goto loc_002B764C;
loc_002B74E8:
    if (v_rbx > v_stack_p28) goto loc_002B752B;
loc_002B7502:
    if (sign_flag) goto loc_002B75EF;
loc_002B750E:
    v_rbx = (v_rbx) + (8);
    v_r12 = (v_rbx + 8) + (8);
    if (v_rbx <= v_stack_p28) goto loc_002B7502;
loc_002B752B:
    if (((unsigned __int8)((unsigned int)((unsigned int)(v_rsi)))) == 17) goto loc_002B7228;
    result = *(unsigned __int64 *)(v_rbx);
    if ((*(unsigned int *)(v_rip + 13694948)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)((unsigned int)((unsigned int)(v_rsi)));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 2, a4);
    }
    goto loc_002B7228;
loc_002B7558:
    if ((*(unsigned int *)(v_rip + 13694948)) != 0) goto loc_002B7319;
    if ((*(unsigned __int64 *)(v_stack_p30 + 152)) == (v_stack_p30 + 152)) goto loc_002B7319;
    result = KiCheckForKernelApcDelivery(a1, a2, 2, a4);
    goto loc_002B7319;
loc_002B7583:
    result = KiRaiseIrqlProcessIrqlFlags(a1, (unsigned __int8)(result), 2, a4);
    goto loc_002B72FD;
loc_002B7595:
    result = MiInPageGapPage(a1, v_stack_p68, 2, a4);
    if ((unsigned int)(result) == 0) goto loc_002B717D;
    *(unsigned __int64 *)(v_stack_p68) = v_r12;
    v_stack_p40 = v_stack_p68;
    v_r15 = v_stack_p30;
    if (v_stack_p30 == 0) { v_r15 = v_stack_p68; }
    v_rbx = (v_rbx) + 1;
    v_stack_p50 = v_rbx;
    v_stack_p48 = v_r15;
    goto loc_002B717D;
loc_002B75C6:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 248) + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_p70 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12028592) + result * 8);
    goto loc_002B70B9;
loc_002B75EF:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12028592) + result * 8)) & (*(unsigned __int64 *)(v_rip + 12028592));
    *(unsigned __int64 *)(v_rbx) = result;
    v_r15 = (result + result * 2) << (4);
    v_r15 = (v_r15) + (v_stack_p18);
loc_002B760D:
    if (condition_is_below) goto loc_002B7660;
    result = MiRemoveLockedPageChargeAndDecRef(v_r15, v_stack_p68, 2, a4);
    a1 = (unsigned int)(((unsigned int)(v_stack_p20)) + 1);
    v_stack_p20 = (unsigned int)(a1);
    if ((((unsigned __int8)(a1)) & (63)) == 0) goto loc_002B7752;
loc_002B7644:
    v_r13 = 0;
    goto loc_002B750E;
loc_002B764C:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))), (unsigned __int8)(v_stack_p68), 2, a4);
    goto loc_002B74E8;
loc_002B7660:
    v_r13 = (unsigned int)((v_r13) + 1);
    if (((*(unsigned int *)(v_rip + 13687874)) & ((unsigned int)(v_r13))) == 0) goto loc_002B771A;
loc_002B7670:
loc_002B7672:
    if (!sign_flag) goto loc_002B760D;
    goto loc_002B7660;
loc_002B767D:
    goto loc_002B74E8;
loc_002B7685:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13693997)))) & (64)) == 0) goto loc_002B735E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))), (unsigned __int8)(v_stack_p68), 2, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002B735E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(v_stack_p38))), (unsigned __int8)(v_stack_p68), 2, a4);
    goto loc_002B7360;
loc_002B76AC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13693958)))) & (64)) == 0) goto loc_002B73A0;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)((unsigned int)(v_stack_p38))), (unsigned __int8)(v_stack_p68), 2, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002B73A0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), (unsigned __int8)(v_stack_p68), 2, a4);
    goto loc_002B73A2;
loc_002B76D4:
    v_stack_mF0 = (unsigned int)(v_stack_p38) + result * 8;
    goto loc_002B6FF3;
loc_002B76E1:
    *(unsigned int *)(v_stack_p18 + 80) = 0xC0000017ULL;
    *(unsigned __int64 *)(v_stack_p18 + 88) = v_r13;
    goto loc_002B7078;
loc_002B76F1:
    if (v_stack_p68 == 0) goto loc_002B71A1;
    v_stack_p40 = *(unsigned __int64 *)(v_stack_p68);
    if (v_stack_p68 == 0) {
        v_stack_p48 = v_r13;
    }
    result = MiReturnPfnReferenceCountAtDpc(v_stack_p68, (unsigned __int8)(v_stack_p68), 2, a4);
    goto loc_002B76F1;
loc_002B771A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13693848)))) & (64)) == 0) goto loc_002B7670;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p68, (unsigned __int8)(v_stack_p68), 2, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002B7670;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r13)), (unsigned __int8)(v_stack_p68), 2, a4);
    goto loc_002B7672;
loc_002B7742:
    *(unsigned int *)(v_stack_p18 + 80) = 0xC000009AULL;
    *(unsigned __int64 *)(v_stack_p18 + 88) = v_r13;
    goto loc_002B7052;
loc_002B7752:
    if ((*(unsigned __int64 *)(v_stack_p68)) > ((unsigned int)(v_stack_p38))) goto loc_002B7644;
    if (17 == 17) goto loc_002B7644;
    result = KiLowerIrqlProcessIrqlFlags((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))), 17, 2, a4);
loc_002B7785:
    result = (*(unsigned __int64 *)((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))) + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    result = MiReleaseFreshPageAtDpc((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))), *(unsigned __int64 *)(v_rip + 12028152), 2, a4);
loc_002B77B2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18 + 112)))) & (1)) == 0) goto loc_002B729B;
    result = MiIsRetryIoStatus((unsigned int)((unsigned int)((unsigned int)(v_stack_p38))), (unsigned int)(0x1000ULL), 2, a4);
    if ((unsigned int)(result) == 0) goto loc_002B729B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18 + 112)))) & (2)) != 0) goto loc_002B729B;
    goto loc_002B729B;
loc_002B77E5:
    result = PsDereferencePartition(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p38))) + 184), (unsigned int)(0x70496D4DULL), 2, a4);
    *(unsigned int *)(v_stack_p18 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 192)));
    goto loc_002B72A9;
}
```

## 5. (Beta) C Style

```c
int64_t MiFinishHardFault(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint8_t v_stack_m168;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m88;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint8_t v_stack_mDF;
    uint8_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p22;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (328);
    result = 0;
    v_stack_m138 = 0;
    Arg2 = 0;
    v_stack_m148 = v_xmm0;
    result = memset(v_stack_mB8, Arg2, result + 104, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m108, Arg2, Arg2 + 64, Arg4);
    v_stack_mC8 = *(uint64_t *)(arg3 + 0xE8);
    v_stack_m120 = *(uint64_t *)(arg1 + 0x38);
    Arg3 = Arg3 + 272;
    if (*(uint64_t *)(arg3 + 0x100) != 0) { Arg3 = *(uint64_t *)(arg3 + 0x100); }
    local_r13 = 0;
    v_stack_m130 = Arg3;
    v_stack_m150 = 0;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg3 + 0x2C))) + (*(uint64_t *)(arg3 + 0x20));
    Arg1 = (uint32_t)((Arg1) & (0xFFFULL));
    result = ((uint32_t)(*(uint32_t *)(arg3 + 0x28))) + (0xFFFULL);
    result = (result) + (Arg1);
    result = (result) >> (12);
    result = (result) - 1;
    v_stack_m160 = Arg3 + 48 + result * 8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xBC)))) != -1) goto loc_002B76D4;
    v_stack_mF0 = -1;
loc_002B6FF3:
    v_stack_m128 = *(uint64_t *)(arg3 + 0xE0);
    v_stack_mC0 = *(uint64_t *)(arg3 + 0xA0);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xBC)))) >= -1) goto loc_002B72C8;
loc_002B701F:
    v_stack_m100 = 0xC0000434ULL;
    v_stack_m168 = 17;
    if (*(uint64_t *)(arg1 + 0x38) != 0) goto loc_002B72E3;
    v_stack_m158 = 17;
loc_002B703B:
    if (*(uint64_t *)(arg3 + 0xA0) != 0) goto loc_002B7439;
loc_002B7044:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xB4))) != 0) goto loc_002B7742;
loc_002B7052:
    if ((*(uint64_t *)(arg3 + 0x10)) == (Arg3 + 16)) goto loc_002B7078;
    result = MiInvalidateCollidedIos(Arg3, *(uint64_t *)(arg1 + 0x38), Arg3, Arg4);
    v_stack_mDF = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_002B76E1;
loc_002B7078:
    if (*(uint64_t *)(arg3 + 0xA0) == 0) goto loc_002B70AA;
loc_002B7086:
    if (condition_is_below) goto loc_002B7390;
    result = MiRemoveLockedPageChargeAndDecRef(*(uint64_t *)(arg3 + 0xA0), *(uint64_t *)(arg1 + 0x38), Arg3, Arg4);
loc_002B70AA:
    if (condition_is_below) goto loc_002B75C6;
    v_stack_m118 = 0;
loc_002B70B9:
    if (!sign_flag) goto loc_002B7451;
loc_002B70C6:
    if (!sign_flag) goto loc_002B73B1;
loc_002B70CF:
    v_stack_mD0 = 0;
loc_002B70D6:
    v_stack_m108 = Arg3;
    v_stack_mE8 = *(uint64_t *)(v_stack_p8 + 0x38);
    v_stack_mD8 = v_stack_p20;
    v_stack_mA8 = v_stack_p20;
    v_stack_mA0 = v_stack_p20;
    v_stack_m58 = 2;
    v_stack_m98 = 0;
    v_stack_m60 = 0;
    if ((Arg3 + 48) > v_stack_m160) goto loc_002B718D;
loc_002B713B:
    Arg2 = (*(uint64_t *)(arg3 + 0x30) + *(uint64_t *)(arg3 + 0x30) * 2) << (4);
    Arg2 = (Arg2) + (0);
    result = MiInPageSkipPage(Arg2, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002B7595;
    if (Arg2 == (*(uint64_t *)(arg3 + 0xF8))) goto loc_002B733E;
    v_stack_mF8 = Arg3 + 48;
    result = MiAddPageToInsertList(v_stack_mB8, v_stack_m108, *(uint64_t *)(arg3 + 0x30), Arg4);
loc_002B717D:
    local_rsi = (Arg3 + 48) + (8);
    if (local_rsi <= v_stack_m160) goto loc_002B713B;
    local_r13 = 0;
loc_002B718D:
    Arg2 = 0;
    result = MiInsertPagesInList(v_stack_mB8, Arg2, *(uint64_t *)(arg3 + 0x30), Arg4);
    if (v_stack_m138 != 0) goto loc_002B76F1;
loc_002B71A1:
loc_002B71AB:
    if (condition_is_below) goto loc_002B7350;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0xF8) + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0xF8) + 0x20))) >> (16));
    result = (uint8_t)((result) & (223));
    v_stack_p22 = (uint8_t)(result);
    *(uint32_t *)(*(uint64_t *)(arg3 + 0xF8) + 0x20) = (uint32_t)((uint32_t)(v_stack_p20));
    v_stack_mF8 = v_stack_m150;
    *(uint64_t *)(*(uint64_t *)(arg3 + 0xF8)) = 0;
    result = MiHardFaultPageRelease(v_stack_m108, *(uint64_t *)(arg3 + 0xF8), *(uint64_t *)(arg3 + 0x30), Arg4);
    v_stack_m150 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x50)));
    if (v_stack_mC0 != 0) goto loc_002B736F;
loc_002B7218:
    if (condition_is_below) goto loc_002B7497;
loc_002B7228:
    if (v_stack_mD0 != 0) goto loc_002B7481;
loc_002B7235:
    if (v_stack_m120 != 0) goto loc_002B7412;
loc_002B7247:
    result = (uint32_t)(*(uint32_t *)(arg3 + 0xC0));
    if (v_stack_m120 >= 0) {
        Arg1 = *(uint64_t *)(arg3 + 0xC8);
        Arg2 = 0x63536D4DULL;
        result = ObDereferenceObjectDeferDeleteWithTag(Arg1, Arg2, *(uint64_t *)(arg3 + 0x30), Arg4);
    }
    result = (uint32_t)(*(uint32_t *)(arg3 + 0xB0));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xB0)))) >= = 1) {
        Arg1 = Arg3 + 56;
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(arg3 + 0x68) != 0) goto loc_002B7785;
    if (sign_flag) goto loc_002B77B2;
    local_rsi = (uint32_t)(v_stack_m100);
    if (v_stack_mE0 == 0) { local_rsi = (uint32_t)((uint32_t)(0xC0000434ULL)); }
loc_002B729B:
    if (v_stack_m118 != 0) goto loc_002B77E5;
loc_002B72A9:
    result = MiFreeInPageSupportBlock(0, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (328);
    return (uint32_t)((uint32_t)(local_rsi));
loc_002B72C8:
    if (0 == 0) goto loc_002B701F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC0)))) & (32)) != 0) goto loc_002B701F;
    v_stack_m100 = 0;
    v_stack_p20 = 17;
loc_002B72E3:
    v_stack_p30 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xD0FA29)) != 0) goto loc_002B7583;
loc_002B72FD:
    if ((*(uint32_t *)(v_rip + 0xD0FA29)) < 0) goto loc_002B7319;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg2 + 0xB8)))) & (15)) != 0) goto loc_002B7558;
    result = KeLeaveCriticalRegionThread(v_stack_m158, Arg2, Arg3, Arg4);
loc_002B7319:
    result = MiRelockFaultState(v_stack_m148 + 56, v_stack_p10, Arg3, Arg4);
    *(uint8_t *)(v_stack_p8 + 0x44) = (uint8_t)(v_stack_p30);
    goto loc_002B703B;
loc_002B733E:
    v_stack_p38 = local_rsi;
    goto loc_002B717D;
loc_002B7350:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xD0DF54)) & ((uint32_t)(local_rsi))) == 0) goto loc_002B7685;
loc_002B735E:
loc_002B7360:
    if (!sign_flag) goto loc_002B71AB;
    goto loc_002B7350;
loc_002B736F:
    if (((uint8_t)(v_stack_m158)) != 17) {
        Arg2 = 17;
    }
    result = MiUnlockProtoPoolPage(v_stack_mC0, Arg2, Arg3, Arg4);
    goto loc_002B7218;
loc_002B7390:
    local_r15 = (uint32_t)((v_stack_m158) + 1);
    if (((*(uint32_t *)(v_rip + 0xD0DF12)) & ((uint32_t)(local_r15))) == 0) goto loc_002B76AC;
loc_002B73A0:
loc_002B73A2:
    if (!sign_flag) goto loc_002B7086;
    goto loc_002B7390;
loc_002B73B1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC0)))) & (32)) != 0) goto loc_002B73E1;
    if ((*(uint64_t *)(arg3 + 0x100)) != 0) goto loc_002B73E1;
    if (v_stack_p28 == (v_stack_p58 + 48)) goto loc_002B70CF;
    if (v_stack_mF0 <= (v_stack_p58 + 56)) goto loc_002B70CF;
loc_002B73E1:
    Arg1 = ((((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC0)))) & (0x3800ULL)) != 0) ? 1 : 0;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3 + 0xC0))) & (0x120000ULL));
    result = (((uint32_t)(local_rbx)) == 0x100000ULL) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002B70CF;
    result = MiCreateDecayPfn(Arg1, Arg2, Arg3, Arg4);
    v_stack_mD0 = result;
    goto loc_002B70D6;
loc_002B7412:
    if (condition_is_above_or_equal) goto loc_002B7247;
    Arg3 = 0;
    Arg1 = (v_stack_p8) + (56);
    result = MiReleaseFaultState(Arg1, 17, Arg3, Arg4);
    goto loc_002B7247;
loc_002B7439:
    Arg2 = v_stack_p20;
    if (((uint8_t)(result)) != 17) { Arg2 = 0; }
    result = MiRelockProtoPoolPage(v_stack_mC0, Arg2, Arg3, Arg4);
    goto loc_002B7044;
loc_002B7451:
    result = MiIsFaultPteIntact(v_stack_p8, v_stack_p60, v_stack_mC8, Arg3 + 168);
    local_r15 = 17;
    if ((uint32_t)(result) == 0) { local_r15 = (uint32_t)((uint32_t)(0xC0000434ULL)); }
    v_stack_m100 = (uint32_t)(local_r15);
    goto loc_002B70C6;
loc_002B7481:
    Arg2 = (((uint8_t)(local_r15)) != 17) ? 1 : 0;
    result = MiDecayPfnFullyInitialized(v_stack_p8, Arg2, v_stack_mC8, Arg3 + 168);
    goto loc_002B7235;
loc_002B7497:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3 + 0x60))) & (0x3FFFFULL));
    Arg1 = (Arg1) + (v_stack_p60);
    Arg4 = 0;
    result = MmCheckCachedPageStates(Arg1, (uint32_t)(*(uint32_t *)(v_stack_p58 + 0x28)), 2, Arg4);
    local_rbx = (v_stack_p58) + (48);
    v_stack_p20 = 0;
    if (((uint8_t)(local_r15)) != 17) goto loc_002B767D;
    if ((*(uint32_t *)(v_rip + 0xD0F83E)) != 0) goto loc_002B764C;
loc_002B74E8:
    if (local_rbx > v_stack_p28) goto loc_002B752B;
loc_002B7502:
    if (sign_flag) goto loc_002B75EF;
loc_002B750E:
    local_rbx = (local_rbx) + (8);
    local_r12 = (local_rbx + 8) + (8);
    if (local_rbx <= v_stack_p28) goto loc_002B7502;
loc_002B752B:
    if (((uint8_t)((uint32_t)((uint32_t)(local_rsi)))) == 17) goto loc_002B7228;
    result = *(uint64_t *)(local_rbx);
    if ((*(uint32_t *)(v_rip + 0xD0F7E4)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)((uint32_t)((uint32_t)(local_rsi)));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 2, Arg4);
    }
    goto loc_002B7228;
loc_002B7558:
    if ((*(uint32_t *)(v_rip + 0xD0F7E4)) != 0) goto loc_002B7319;
    if ((*(uint64_t *)(v_stack_p30 + 0x98)) == (v_stack_p30 + 152)) goto loc_002B7319;
    result = KiCheckForKernelApcDelivery(Arg1, Arg2, 2, Arg4);
    goto loc_002B7319;
loc_002B7583:
    result = KiRaiseIrqlProcessIrqlFlags(Arg1, (uint8_t)(result), 2, Arg4);
    goto loc_002B72FD;
loc_002B7595:
    result = MiInPageGapPage(Arg1, v_stack_p68, 2, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B717D;
    *(uint64_t *)(v_stack_p68) = local_r12;
    v_stack_p40 = v_stack_p68;
    local_r15 = v_stack_p30;
    if (v_stack_p30 == 0) { local_r15 = v_stack_p68; }
    local_rbx = (local_rbx) + 1;
    v_stack_p50 = local_rbx;
    v_stack_p48 = local_r15;
    goto loc_002B717D;
loc_002B75C6:
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0xF8) + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_p70 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB78AB0) + result * 8);
    goto loc_002B70B9;
loc_002B75EF:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB78AB0) + result * 8)) & (*(uint64_t *)(v_rip + 0xB78AB0));
    *(uint64_t *)(local_rbx) = result;
    local_r15 = (result + result * 2) << (4);
    local_r15 = (local_r15) + (v_stack_p18);
loc_002B760D:
    if (condition_is_below) goto loc_002B7660;
    result = MiRemoveLockedPageChargeAndDecRef(local_r15, v_stack_p68, 2, Arg4);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p20)) + 1);
    v_stack_p20 = (uint32_t)(Arg1);
    if ((((uint8_t)(Arg1)) & (63)) == 0) goto loc_002B7752;
loc_002B7644:
    local_r13 = 0;
    goto loc_002B750E;
loc_002B764C:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint32_t)((uint32_t)(local_rsi))), (uint8_t)(v_stack_p68), 2, Arg4);
    goto loc_002B74E8;
loc_002B7660:
    local_r13 = (uint32_t)((local_r13) + 1);
    if (((*(uint32_t *)(v_rip + 0xD0DC42)) & ((uint32_t)(local_r13))) == 0) goto loc_002B771A;
loc_002B7670:
loc_002B7672:
    if (!sign_flag) goto loc_002B760D;
    goto loc_002B7660;
loc_002B767D:
    goto loc_002B74E8;
loc_002B7685:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0F42D)))) & (64)) == 0) goto loc_002B735E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint8_t)((uint32_t)((uint32_t)(local_rsi))), (uint8_t)(v_stack_p68), 2, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002B735E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(v_stack_p38))), (uint8_t)(v_stack_p68), 2, Arg4);
    goto loc_002B7360;
loc_002B76AC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0F406)))) & (64)) == 0) goto loc_002B73A0;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)((uint32_t)(v_stack_p38))), (uint8_t)(v_stack_p68), 2, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002B73A0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), (uint8_t)(v_stack_p68), 2, Arg4);
    goto loc_002B73A2;
loc_002B76D4:
    v_stack_mF0 = (uint32_t)(v_stack_p38) + result * 8;
    goto loc_002B6FF3;
loc_002B76E1:
    *(uint32_t *)(v_stack_p18 + 0x50) = 0xC0000017ULL;
    *(uint64_t *)(v_stack_p18 + 0x58) = local_r13;
    goto loc_002B7078;
loc_002B76F1:
    if (v_stack_p68 == 0) goto loc_002B71A1;
    v_stack_p40 = *(uint64_t *)(v_stack_p68);
    if (v_stack_p68 == 0) {
        v_stack_p48 = local_r13;
    }
    result = MiReturnPfnReferenceCountAtDpc(v_stack_p68, (uint8_t)(v_stack_p68), 2, Arg4);
    goto loc_002B76F1;
loc_002B771A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0F398)))) & (64)) == 0) goto loc_002B7670;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p68, (uint8_t)(v_stack_p68), 2, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002B7670;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r13)), (uint8_t)(v_stack_p68), 2, Arg4);
    goto loc_002B7672;
loc_002B7742:
    *(uint32_t *)(v_stack_p18 + 0x50) = 0xC000009AULL;
    *(uint64_t *)(v_stack_p18 + 0x58) = local_r13;
    goto loc_002B7052;
loc_002B7752:
    if ((*(uint64_t *)(v_stack_p68)) > ((uint32_t)(v_stack_p38))) goto loc_002B7644;
    if (17 == 17) goto loc_002B7644;
    result = KiLowerIrqlProcessIrqlFlags((uint8_t)((uint32_t)((uint32_t)(local_rsi))), 17, 2, Arg4);
loc_002B7785:
    result = (*(uint64_t *)((uint8_t)((uint32_t)((uint32_t)(local_rsi))) + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    result = MiReleaseFreshPageAtDpc((uint8_t)((uint32_t)((uint32_t)(local_rsi))), *(uint64_t *)(v_rip + 0xB788F8), 2, Arg4);
loc_002B77B2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x70)))) & (1)) == 0) goto loc_002B729B;
    result = MiIsRetryIoStatus((uint32_t)((uint32_t)((uint32_t)(v_stack_p38))), (uint32_t)(0x1000ULL), 2, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B729B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x70)))) & (2)) != 0) goto loc_002B729B;
    goto loc_002B729B;
loc_002B77E5:
    result = PsDereferencePartition(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p38))) + 0xB8), (uint32_t)(0x70496D4DULL), 2, Arg4);
    *(uint32_t *)(v_stack_p18 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xC0)));
    goto loc_002B72A9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x50` | `32` | `R` |
| `Arg3` | `+ 0x50` | `32` | `W` |
| `Arg3` | `+ 0x58` | `64` | `W` |
| `Arg3` | `+ 0x60` | `32` | `R` |
| `Arg3` | `+ 0x98` | `64` | `R` |
| `Arg3` | `+ 0xA0` | `64` | `R` |
| `Arg3` | `+ 0xA8` | `64` | `R` |
| `Arg3` | `+ 0xB4` | `32` | `R` |
| `Arg3` | `+ 0xBC` | `32` | `R` |
| `Arg3` | `+ 0xC0` | `32` | `R` |
| `Arg3` | `+ 0xE0` | `64` | `R` |
| `Arg3` | `+ 0xE8` | `64` | `R` |
| `Arg3` | `+ 0xF8` | `64` | `R` |
| `Arg3` | `+ 0x100` | `64` | `R` |
| `Arg3` | `+ 0x110` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B6F10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
