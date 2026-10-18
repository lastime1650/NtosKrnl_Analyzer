# MiPrivateFixup

- RVA: `0x003693E8`–`0x00369B41` (길이 `1,881` bytes)
- VA: `0x00000001403693E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007A1D8`
- 디코드: `447`개 명령, `1,881/1,881` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **33**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00369520` → [MiObtainFaultCharges](../28/MiObtainFaultCharges_function_0028AEB0.md) (function, `0x0028AEB0`)
- `0x00369531` → [MI_PAGE_TO_FULL_COLOR](../33/MI_PAGE_TO_FULL_COLOR_function_00337820.md) (function, `0x00337820`)
- `0x00369545` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0036957B` → [MiGetInPageSupportBlock](MiGetInPageSupportBlock_function_00362500.md) (function, `0x00362500`)
- `0x00369592` → [MiGetEffectivePagePriorityThread](MiGetEffectivePagePriorityThread_function_003626E0.md) (function, `0x003626E0`)
- `0x003695E0` → [MiInitializeReadInProgressPfn](../2B/MiInitializeReadInProgressPfn_function_002B6990.md) (function, `0x002B6990`)
- `0x00369622` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x00369643` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0036966B` → [MiCopyPage](../2B/MiCopyPage_function_002B1B30.md) (function, `0x002B1B30`)
- `0x00369685` → [MiReservePtes](../31/MiReservePtes_function_00318D20.md) (function, `0x00318D20`)
- `0x0036969E` → [MiMakeProtectionPfnCompatible](../22/MiMakeProtectionPfnCompatible_function_00229CD0.md) (function, `0x00229CD0`)
- `0x003696B1` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x00369728` → [MiRelocateImagePfn](../../page/93/MiRelocateImagePfn_function_0093F2A8.md) (function, `0x0093F2A8`)
- `0x0036974D` → [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) (function, `0x00247240`)
- `0x0036979C` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x003697A9` → [MiRelockFaultState](MiRelockFaultState_function_0036A230.md) (function, `0x0036A230`)
- `0x003697BC` → [MiIsFaultPteIntact](../32/MiIsFaultPteIntact_function_003288A0.md) (function, `0x003288A0`)
- `0x003697FB` → [MiSetPfnModified](MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x0036980D` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x00369846` → [MiFreeInPageSupportBlock](../2B/MiFreeInPageSupportBlock_function_002B5900.md) (function, `0x002B5900`)
- `0x0036987A` → [MiAddLockedPageCharge](../28/MiAddLockedPageCharge_function_0028B550.md) (function, `0x0028B550`)
- `0x003698FA` → [MiDeleteControlArea](MiDeleteControlArea_function_003691F4.md) (function, `0x003691F4`)
- `0x00369907` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00369949` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0036997C` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0036998B` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003699BE` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x003699D6` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003699EC` → [MiAllocateDriverPage](../../page/A8/MiAllocateDriverPage_function_00A80128.md) (function, `0x00A80128`)
- `0x00369A00` → [MiRelockFaultState](MiRelockFaultState_function_0036A230.md) (function, `0x0036A230`)
- `0x00369A14` → [MiIsFaultPteIntact](../32/MiIsFaultPteIntact_function_003288A0.md) (function, `0x003288A0`)
- `0x00369A58` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x00369AAF` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00369ACC` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00369AFF` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x00369B23` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00369B37` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) at `0x0034621E`

### Static image references
- `0x0036946E` → RVA `0x00E30088` (`.data`; read)
- `0x00369630` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0036967E` → RVA `0x00E37668` (`.data`; read)
- `0x003696B6` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0036972D` → RVA `0x00E2D720` (`.data`; read)
- `0x003698DD` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0036996E` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00369A97` → RVA `0x00E2D718` (`.data`; read)
- `0x00369AE9` → RVA `0x00010880` (`.rdata`; read)
- `0x00369B08` → RVA `0x00E2D718` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00369728` → [MiRelocateImagePfn](../../page/93/MiRelocateImagePfn_function_0093F2A8.md) (`.text` → `PAGE`)
  - `0x003699EC` → [MiAllocateDriverPage](../../page/A8/MiAllocateDriverPage_function_00A80128.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00369A3A` → [sub_006E3B0E](../6E/Unknown_function_006E3B0E.md) (`tail-transfer`)
  - `0x00369A5E` → [sub_006E3B0E](../6E/Unknown_function_006E3B0E.md) (`tail-transfer`)
  - `0x00369ABD` → [sub_006E3B0E + 0x17](../6E/Unknown_function_006E3B0E.md) (`tail-transfer`)
  - `0x00369AD2` → [sub_006E3B0E + 0x17](../6E/Unknown_function_006E3B0E.md) (`tail-transfer`)
  - `0x00369B16` → [sub_006E3B0E + 0x30](../6E/Unknown_function_006E3B0E.md) (`tail-transfer`)
  - `0x00369B29` → [sub_006E3B0E + 0x30](../6E/Unknown_function_006E3B0E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003693E8  48 8B C4                        mov rax, rsp
003693EB  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
003693EF  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
003693F3  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
003693F7  48 89 48 08                     mov qword ptr [rax + 8], rcx
003693FB  55                              push rbp
003693FC  53                              push rbx
003693FD  56                              push rsi
003693FE  57                              push rdi
003693FF  41 54                           push r12
00369401  41 55                           push r13
00369403  41 56                           push r14
00369405  41 57                           push r15
00369407  48 8D 68 B1                     lea rbp, [rax - 0x4f]
0036940B  48 81 EC A8 00 00 00            sub rsp, 0xa8
00369412  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
0036941B  48 8D 41 38                     lea rax, [rcx + 0x38]
0036941F  4C 8B 10                        mov r10, qword ptr [rax]
00369422  33 F6                           xor esi, esi
00369424  48 8B 11                        mov rdx, qword ptr [rcx]
00369427  4D 8B D9                        mov r11, r9
0036942A  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0036942E  4C 8B E9                        mov r13, rcx
00369431  49 8B 86 B8 00 00 00            mov rax, qword ptr [r14 + 0xb8]
00369438  41 8B 9A B8 00 00 00            mov ebx, dword ptr [r10 + 0xb8]
0036943F  40 88 75 A7                     mov byte ptr [rbp - 0x59], sil
00369443  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
00369447  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0036944B  80 E3 0F                        and bl, 0xf
0036944E  75 10                           jne 0x140369460
00369450  48 8B 80 70 02 00 00            mov rax, qword ptr [rax + 0x270]
00369457  48 85 C0                        test rax, rax
0036945A  0F 85 02 04 00 00               jne 0x140369862
00369460  41 0F B7 8A AE 00 00 00         movzx ecx, word ptr [r10 + 0xae]
00369468  41 BA 01 00 00 00               mov r10d, 1
0036946E  48 8B 05 13 6C AC 00            mov rax, qword ptr [rip + 0xac6c13]
00369475  41 8B 7B 10                     mov edi, dword ptr [r11 + 0x10]
00369479  48 C1 EF 05                     shr rdi, 5
0036947D  83 E7 1F                        and edi, 0x1f
00369480  89 75 AB                        mov dword ptr [rbp - 0x55], esi
00369483  4C 8B 0C C8                     mov r9, qword ptr [rax + rcx*8]
00369487  45 8D 62 01                     lea r12d, [r10 + 1]
0036948B  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00369495  4C 89 4D AF                     mov qword ptr [rbp - 0x51], r9
00369499  48 3B D0                        cmp rdx, rax
0036949C  0F 83 B1 04 00 00               jae 0x140369953
003694A2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003694AB  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003694B2  44 84 91 70 01 00 00            test byte ptr [rcx + 0x170], r10b
003694B9  0F 84 A6 04 00 00               je 0x140369965
003694BF  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003694C9  48 8B CA                        mov rcx, rdx
003694CC  48 C1 E9 09                     shr rcx, 9
003694D0  48 23 C8                        and rcx, rax
003694D3  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003694DD  48 8B C0                        mov rax, rax
003694E0  48 03 C8                        add rcx, rax
003694E3  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
003694E7  48 8B 01                        mov rax, qword ptr [rcx]
003694EA  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
003694EE  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003694F8  48 8B C0                        mov rax, rax
003694FB  4D 8B FB                        mov r15, r11
003694FE  45 8B C4                        mov r8d, r12d
00369501  4C 2B F8                        sub r15, rax
00369504  49 8B D2                        mov rdx, r10
00369507  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00369511  49 C1 FF 04                     sar r15, 4
00369515  4C 0F AF F8                     imul r15, rax
00369519  49 8B C9                        mov rcx, r9
0036951C  4C 89 7D DF                     mov qword ptr [rbp - 0x21], r15
00369520  E8 8B 19 F2 FF                  call 0x14028aeb0
00369525  39 75 AB                        cmp dword ptr [rbp - 0x55], esi
00369528  0F 84 72 04 00 00               je 0x1403699a0
0036952E  49 8B CF                        mov rcx, r15
00369531  E8 EA E2 FC FF                  call 0x140337820
00369536  4C 8B 6D AF                     mov r13, qword ptr [rbp - 0x51]
0036953A  41 B8 01 00 00 00               mov r8d, 1
00369540  49 8B CD                        mov rcx, r13
00369543  8B D0                           mov edx, eax
00369545  E8 76 EF F1 FF                  call 0x1402884c0
0036954A  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0036954E  4C 8B F8                        mov r15, rax
00369551  48 8B D0                        mov rdx, rax
00369554  48 83 F8 FF                     cmp rax, -1
00369558  0F 84 27 05 00 00               je 0x140369a85
0036955E  48 8D 3C 52                     lea rdi, [rdx + rdx*2]
00369562  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036956C  48 C1 E7 04                     shl rdi, 4
00369570  48 8B C0                        mov rax, rax
00369573  33 D2                           xor edx, edx
00369575  41 8B CC                        mov ecx, r12d
00369578  48 03 F8                        add rdi, rax
0036957B  E8 80 8F FF FF                  call 0x140362500
00369580  4C 8B E8                        mov r13, rax
00369583  48 85 C0                        test rax, rax
00369586  0F 84 00 05 00 00               je 0x140369a8c
0036958C  49 8B CE                        mov rcx, r14
0036958F  89 75 AF                        mov dword ptr [rbp - 0x51], esi
00369592  E8 49 91 FF FF                  call 0x1403626e0
00369597  4C 8B 7D B7                     mov r15, qword ptr [rbp - 0x49]
0036959B  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0036959F  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
003695A3  24 07                           and al, 7
003695A5  0C 48                           or al, 0x48
003695A7  49 89 BD F8 00 00 00            mov qword ptr [r13 + 0xf8], rdi
003695AE  88 45 AF                        mov byte ptr [rbp - 0x51], al
003695B1  4D 8B CF                        mov r9, r15
003695B4  41 8B 85 C0 00 00 00            mov eax, dword ptr [r13 + 0xc0]
003695BB  41 B8 01 00 00 00               mov r8d, 1
003695C1  0F BA E8 07                     bts eax, 7
003695C5  41 89 85 C0 00 00 00            mov dword ptr [r13 + 0xc0], eax
003695CC  8B 45 AF                        mov eax, dword ptr [rbp - 0x51]
003695CF  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003695D3  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
003695D8  41 89 75 50                     mov dword ptr [r13 + 0x50], esi
003695DC  49 89 75 58                     mov qword ptr [r13 + 0x58], rsi
003695E0  E8 AB D3 F4 FF                  call 0x1402b6990
003695E5  84 DB                           test bl, bl
003695E7  75 0C                           jne 0x1403695f5
003695E9  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
003695ED  F0 48 FF 80 88 02 00 00         lock inc qword ptr [rax + 0x288]
003695F5  49 8B 07                        mov rax, qword ptr [r15]
003695F8  BB 01 00 00 00                  mov ebx, 1
003695FD  48 8B 4D 5F                     mov rcx, qword ptr [rbp + 0x5f]
00369601  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00369605  48 8B 01                        mov rax, qword ptr [rcx]
00369608  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0036960C  49 89 8D D0 00 00 00            mov qword ptr [r13 + 0xd0], rcx
00369613  F0 48 01 58 70                  lock add qword ptr [rax + 0x70], rbx
00369618  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
0036961C  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00369620  8A D3                           mov dl, bl
00369622  E8 69 3C F1 FF                  call 0x14027d290
00369627  66 41 29 9E E6 01 00 00         sub word ptr [r14 + 0x1e6], bx
0036962F  90                              nop
00369630  39 35 EA D6 C5 00               cmp dword ptr [rip + 0xc5d6ea], esi
00369636  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0036963A  74 0C                           je 0x140369648
0036963C  44 0F 20 C1                     mov rcx, cr8
00369640  8A 55 A7                        mov dl, byte ptr [rbp - 0x59]
00369643  E8 50 C0 18 00                  call 0x1404f5698
00369648  0F B6 45 A7                     movzx eax, byte ptr [rbp - 0x59]
0036964C  44 0F 22 C0                     mov cr8, rax
00369650  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00369653  48 8B 5D BF                     mov rbx, qword ptr [rbp - 0x41]
00369657  F7 D8                           neg eax
00369659  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
0036965D  48 8B CB                        mov rcx, rbx
00369660  45 1B C0                        sbb r8d, r8d
00369663  41 83 E0 38                     and r8d, 0x38
00369667  41 83 C0 11                     add r8d, 0x11
0036966B  E8 C0 84 F4 FF                  call 0x1402b1b30
00369670  39 75 AB                        cmp dword ptr [rbp - 0x55], esi
00369673  0F 84 1C 03 00 00               je 0x140369995
00369679  BA 01 00 00 00                  mov edx, 1
0036967E  48 8D 0D E3 DF AC 00            lea rcx, [rip + 0xacdfe3]
00369685  E8 96 F6 FA FF                  call 0x140318d20
0036968A  4C 8B F8                        mov r15, rax
0036968D  48 85 C0                        test rax, rax
00369690  0F 84 FD 03 00 00               je 0x140369a93
00369696  48 8B D7                        mov rdx, rdi
00369699  B9 04 00 00 00                  mov ecx, 4
0036969E  E8 2D 06 EC FF                  call 0x140229cd0
003696A3  0D 00 00 00 A0                  or eax, 0xa0000000
003696A8  48 8B D3                        mov rdx, rbx
003696AB  44 8B C0                        mov r8d, eax
003696AE  49 8B CF                        mov rcx, r15
003696B1  E8 DA BE F5 FF                  call 0x1402c5590
003696B6  48 0F BA 25 C9 D3 C5 00 24      bt qword ptr [rip + 0xc5d3c9], 0x24
003696BF  48 8B D8                        mov rbx, rax
003696C2  0F 82 49 02 00 00               jb 0x140369911
003696C8  49 89 1F                        mov qword ptr [r15], rbx
003696CB  49 8B DF                        mov rbx, r15
003696CE  48 C1 E3 19                     shl rbx, 0x19
003696D2  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003696DC  48 8B C0                        mov rax, rax
003696DF  48 8B 4D 6F                     mov rcx, qword ptr [rbp + 0x6f]
003696E3  48 C1 E0 19                     shl rax, 0x19
003696E7  48 2B D8                        sub rbx, rax
003696EA  48 C1 FB 10                     sar rbx, 0x10
003696EE  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
003696F2  48 0F BA E0 28                  bt rax, 0x28
003696F7  72 0D                           jb 0x140369706
003696F9  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
003696FD  48 85 C0                        test rax, rax
00369700  0F 89 D1 03 00 00               jns 0x140369ad7
00369706  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00369709  48 8B D3                        mov rdx, rbx
0036970C  4C 8B 4D BF                     mov r9, qword ptr [rbp - 0x41]
00369710  83 C8 24                        or eax, 0x24
00369713  44 8B 45 67                     mov r8d, dword ptr [rbp + 0x67]
00369717  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
0036971B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0036971F  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00369723  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00369728  E8 7B 5B 5D 00                  call 0x14093f2a8
0036972D  4C 3B 3D EC 3F AC 00            cmp r15, qword ptr [rip + 0xac3fec]
00369734  0F 84 AF 03 00 00               je 0x140369ae9
0036973A  41 BC 01 00 00 00               mov r12d, 1
00369740  48 8D 0D 21 DF AC 00            lea rcx, [rip + 0xacdf21]
00369747  45 8B C4                        mov r8d, r12d
0036974A  49 8B D7                        mov rdx, r15
0036974D  E8 EE DA ED FF                  call 0x140247240
00369752  4C 8B 7D B7                     mov r15, qword ptr [rbp - 0x49]
00369756  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
0036975A  48 83 CA FF                     or rdx, 0xffffffffffffffff
0036975E  48 8B C2                        mov rax, rdx
00369761  F0 48 0F C1 41 70               lock xadd qword ptr [rcx + 0x70], rax
00369767  48 03 C2                        add rax, rdx
0036976A  0F 84 8A 01 00 00               je 0x1403698fa
00369770  44 0F 20 C1                     mov rcx, cr8
00369774  45 0F 22 C4                     mov cr8, r12
00369778  39 35 A2 D5 C5 00               cmp dword ptr [rip + 0xc5d5a2], esi
0036977E  0F 85 80 01 00 00               jne 0x140369904
00369784  90                              nop
00369785  66 45 01 A6 E6 01 00 00         add word ptr [r14 + 0x1e6], r12w
0036978D  75 12                           jne 0x1403697a1
0036978F  49 8D 86 98 00 00 00            lea rax, [r14 + 0x98]
00369796  90                              nop
00369797  48 39 00                        cmp qword ptr [rax], rax
0036979A  74 05                           je 0x1403697a1
0036979C  E8 DF 94 F7 FF                  call 0x1402e2c80
003697A1  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
003697A5  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
003697A9  E8 82 0A 00 00                  call 0x14036a230
003697AE  48 8B 4D 57                     mov rcx, qword ptr [rbp + 0x57]
003697B2  4C 8D 4D F7                     lea r9, [rbp - 9]
003697B6  4D 8B C7                        mov r8, r15
003697B9  48 8B 11                        mov rdx, qword ptr [rcx]
003697BC  E8 DF F0 FB FF                  call 0x1403288a0
003697C1  44 8B F0                        mov r14d, eax
003697C4  8B DE                           mov ebx, esi
003697C6  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
003697CD  0F 82 07 01 00 00               jb 0x1403698da
003697D3  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
003697D6  89 45 57                        mov dword ptr [rbp + 0x57], eax
003697D9  C1 E8 10                        shr eax, 0x10
003697DC  24 DF                           and al, 0xdf
003697DE  88 45 59                        mov byte ptr [rbp + 0x59], al
003697E1  8B 45 57                        mov eax, dword ptr [rbp + 0x57]
003697E4  89 47 20                        mov dword ptr [rdi + 0x20], eax
003697E7  48 89 37                        mov qword ptr [rdi], rsi
003697EA  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
003697EE  48 0F BA E0 3E                  bt rax, 0x3e
003697F3  72 0B                           jb 0x140369800
003697F5  41 8B D4                        mov edx, r12d
003697F8  48 8B CF                        mov rcx, rdi
003697FB  E8 60 91 FF FF                  call 0x140362960
00369800  45 85 F6                        test r14d, r14d
00369803  75 6D                           jne 0x140369872
00369805  BE 34 04 00 C0                  mov esi, 0xc0000434
0036980A  48 8B CF                        mov rcx, rdi
0036980D  E8 BE C1 ED FF                  call 0x1402459d0
00369812  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0036981C  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
00369821  41 8B 8D C0 00 00 00            mov ecx, dword ptr [r13 + 0xc0]
00369828  0F BA F1 07                     btr ecx, 7
0036982C  41 89 8D C0 00 00 00            mov dword ptr [r13 + 0xc0], ecx
00369833  41 8B 8D B0 00 00 00            mov ecx, dword ptr [r13 + 0xb0]
0036983A  41 3B CC                        cmp ecx, r12d
0036983D  0F 8F EB 02 00 00               jg 0x140369b2e
00369843  49 8B CD                        mov rcx, r13
00369846  E8 B5 C0 F4 FF                  call 0x1402b5900
0036984B  8B C6                           mov eax, esi
0036984D  48 81 C4 A8 00 00 00            add rsp, 0xa8
00369854  41 5F                           pop r15
00369856  41 5E                           pop r14
00369858  41 5D                           pop r13
0036985A  41 5C                           pop r12
0036985C  5F                              pop rdi
0036985D  5E                              pop rsi
0036985E  5B                              pop rbx
0036985F  5D                              pop rbp
00369860  C3                              ret
00369861  CC                              int3
00369862  49 3B C6                        cmp rax, r14
00369865  0F 85 F8 01 00 00               jne 0x140369a63
0036986B  B8 29 01 00 00                  mov eax, 0x129
00369870  EB DB                           jmp 0x14036984d
00369872  BA 03 00 00 00                  mov edx, 3
00369877  48 8B CF                        mov rcx, rdi
0036987A  E8 D1 1C F2 FF                  call 0x14028b550
0036987F  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00369883  48 BA 00 00 00 00 00 00 00 C0   movabs rdx, 0xc000000000000000
0036988D  48 8D 48 01                     lea rcx, [rax + 1]
00369891  48 33 C1                        xor rax, rcx
00369894  48 23 C2                        and rax, rdx
00369897  48 33 C1                        xor rax, rcx
0036989A  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
0036989E  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
003698A1  89 45 57                        mov dword ptr [rbp + 0x57], eax
003698A4  C1 E8 10                        shr eax, 0x10
003698A7  24 FE                           and al, 0xfe
003698A9  0C 06                           or al, 6
003698AB  88 45 59                        mov byte ptr [rbp + 0x59], al
003698AE  8B 45 57                        mov eax, dword ptr [rbp + 0x57]
003698B1  89 47 20                        mov dword ptr [rdi + 0x20], eax
003698B4  39 75 AB                        cmp dword ptr [rbp - 0x55], esi
003698B7  0F 85 4D FF FF FF               jne 0x14036980a
003698BD  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
003698C7  48 39 45 C7                     cmp qword ptr [rbp - 0x39], rax
003698CB  0F 82 39 FF FF FF               jb 0x14036980a
003698D1  80 4F 23 08                     or byte ptr [rdi + 0x23], 8
003698D5  E9 30 FF FF FF                  jmp 0x14036980a
003698DA  41 03 DC                        add ebx, r12d
003698DD  85 1D C9 B9 C5 00               test dword ptr [rip + 0xc5b9c9], ebx
003698E3  0F 84 85 00 00 00               je 0x14036996e
003698E9  F3 90                           pause
003698EB  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
003698EF  48 85 C0                        test rax, rax
003698F2  0F 89 CE FE FF FF               jns 0x1403697c6
003698F8  EB E0                           jmp 0x1403698da
003698FA  E8 F5 F8 FF FF                  call 0x1403691f4
003698FF  E9 6C FE FF FF                  jmp 0x140369770
00369904  41 8A D4                        mov dl, r12b
00369907  E8 F0 BD 18 00                  call 0x1404f56fc
0036990C  E9 73 FE FF FF                  jmp 0x140369784
00369911  F6 C3 20                        test bl, 0x20
00369914  0F 85 AE FD FF FF               jne 0x1403696c8
0036991A  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00369924  48 8B C0                        mov rax, rax
00369927  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00369931  48 03 C1                        add rax, rcx
00369934  4C 3B F8                        cmp r15, rax
00369937  0F 82 8B FD FF FF               jb 0x1403696c8
0036993D  41 B8 80 00 00 00               mov r8d, 0x80
00369943  48 8B D3                        mov rdx, rbx
00369946  49 8B CF                        mov rcx, r15
00369949  E8 32 94 F2 FF                  call 0x140292d80
0036994E  E9 75 FD FF FF                  jmp 0x1403696c8
00369953  48 8B 05 2E D1 C5 00            mov rax, qword ptr [rip + 0xc5d12e]
0036995A  48 0F BA E0 0F                  bt rax, 0xf
0036995F  0F 82 0D 01 00 00               jb 0x140369a72
00369965  44 89 55 AB                     mov dword ptr [rbp - 0x55], r10d
00369969  E9 51 FB FF FF                  jmp 0x1403694bf
0036996E  8B 05 44 D1 C5 00               mov eax, dword ptr [rip + 0xc5d144]
00369974  A8 40                           test al, 0x40
00369976  0F 84 6D FF FF FF               je 0x1403698e9
0036997C  E8 0F 5B FA FF                  call 0x14030f490
00369981  84 C0                           test al, al
00369983  0F 84 60 FF FF FF               je 0x1403698e9
00369989  8B CB                           mov ecx, ebx
0036998B  E8 D0 5A FA FF                  call 0x14030f460
00369990  E9 56 FF FF FF                  jmp 0x1403698eb
00369995  41 BC 01 00 00 00               mov r12d, 1
0036999B  E9 B6 FD FF FF                  jmp 0x140369756
003699A0  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
003699AA  48 39 45 C7                     cmp qword ptr [rbp - 0x39], rax
003699AE  0F 82 7A FB FF FF               jb 0x14036952e
003699B4  4C 8D 45 A7                     lea r8, [rbp - 0x59]
003699B8  B2 01                           mov dl, 1
003699BA  49 8D 4D 38                     lea rcx, [r13 + 0x38]
003699BE  E8 CD 38 F1 FF                  call 0x14027d290
003699C3  39 35 57 D3 C5 00               cmp dword ptr [rip + 0xc5d357], esi
003699C9  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
003699CD  74 0C                           je 0x1403699db
003699CF  44 0F 20 C1                     mov rcx, cr8
003699D3  8A 55 A7                        mov dl, byte ptr [rbp - 0x59]
003699D6  E8 BD BC 18 00                  call 0x1404f5698
003699DB  0F B6 45 A7                     movzx eax, byte ptr [rbp - 0x59]
003699DF  44 0F 22 C0                     mov cr8, rax
003699E3  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
003699E7  45 33 C0                        xor r8d, r8d
003699EA  8B D7                           mov edx, edi
003699EC  E8 37 67 71 00                  call 0x140a80128
003699F1  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
003699F5  49 8D 4D 38                     lea rcx, [r13 + 0x38]
003699F9  4C 8B F8                        mov r15, rax
003699FC  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00369A00  E8 2B 08 00 00                  call 0x14036a230
00369A05  4C 8B 45 B7                     mov r8, qword ptr [rbp - 0x49]
00369A09  4C 8D 4D EF                     lea r9, [rbp - 0x11]
00369A0D  49 8B 55 00                     mov rdx, qword ptr [r13]
00369A11  49 8B CD                        mov rcx, r13
00369A14  E8 87 EE FB FF                  call 0x1403288a0
00369A19  8B C8                           mov ecx, eax
00369A1B  49 8B D7                        mov rdx, r15
00369A1E  F7 D8                           neg eax
00369A20  1B FF                           sbb edi, edi
00369A22  F7 D7                           not edi
00369A24  81 E7 34 04 00 C0               and edi, 0xc0000434
00369A2A  85 C9                           test ecx, ecx
00369A2C  0F 85 2C FB FF FF               jne 0x14036955e
00369A32  4C 8B 6D AF                     mov r13, qword ptr [rbp - 0x51]
00369A36  49 83 FF FF                     cmp r15, -1
00369A3A  0F 84 CE A0 37 00               je 0x1406e3b0e
00369A40  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
00369A44  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00369A4E  48 C1 E1 04                     shl rcx, 4
00369A52  48 8B C0                        mov rax, rax
00369A55  48 03 C8                        add rcx, rax
00369A58  E8 F3 B0 FC FF                  call 0x140334b50
00369A5D  90                              nop
00369A5E  E9 AB A0 37 00                  jmp 0x1406e3b0e
00369A63  41 BC 02 00 00 00               mov r12d, 2
00369A69  44 09 61 50                     or dword ptr [rcx + 0x50], r12d
00369A6D  E9 F9 FD FF FF                  jmp 0x14036986b
00369A72  48 0F BA E0 0D                  bt rax, 0xd
00369A77  0F 83 E8 FE FF FF               jae 0x140369965
00369A7D  41 84 FC                        test r12b, dil
00369A80  E9 34 FA FF FF                  jmp 0x1403694b9
00369A85  BF 9A 00 00 C0                  mov edi, 0xc000009a
00369A8A  EB AA                           jmp 0x140369a36
00369A8C  BF 9A 00 00 C0                  mov edi, 0xc000009a
00369A91  EB 9F                           jmp 0x140369a32
00369A93  48 83 C8 FF                     or rax, 0xffffffffffffffff
00369A97  4C 8D 3D 7A 3C AC 00            lea r15, [rip + 0xac3c7a]
00369A9E  66 41 01 86 E6 01 00 00         add word ptr [r14 + 0x1e6], ax
00369AA6  49 8B CF                        mov rcx, r15
00369AA9  45 33 C0                        xor r8d, r8d
00369AAC  33 D2                           xor edx, edx
00369AAE  90                              nop
00369AAF  E8 7C 67 EA FF                  call 0x140210230
00369AB4  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
00369ABA  48 8B D8                        mov rbx, rax
00369ABD  0F 83 62 A0 37 00               jae 0x1406e3b25
00369AC3  4D 8B C7                        mov r8, r15
00369AC6  48 8B D0                        mov rdx, rax
00369AC9  49 8B CF                        mov rcx, r15
00369ACC  E8 BF 61 EA FF                  call 0x14020fc90
00369AD1  90                              nop
00369AD2  E9 4E A0 37 00                  jmp 0x1406e3b25
00369AD7  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00369ADB  48 85 C0                        test rax, rax
00369ADE  0F 85 49 FC FF FF               jne 0x14036972d
00369AE4  E9 1D FC FF FF                  jmp 0x140369706
00369AE9  48 8B 05 90 6D CA FF            mov rax, qword ptr [rip - 0x359270]
00369AF0  41 B8 01 00 00 00               mov r8d, 1
00369AF6  41 8B D4                        mov edx, r12d
00369AF9  49 89 07                        mov qword ptr [r15], rax
00369AFC  48 8B CB                        mov rcx, rbx
00369AFF  E8 2C 4C F2 FF                  call 0x14028e730
00369B04  48 83 C8 FF                     or rax, 0xffffffffffffffff
00369B08  F0 48 0F C1 05 07 3C AC 00      lock xadd qword ptr [rip + 0xac3c07], rax
00369B11  24 06                           and al, 6
00369B13  41 3A C4                        cmp al, r12b
00369B16  0F 85 22 A0 37 00               jne 0x1406e3b3e
00369B1C  48 8D 0D F5 3B AC 00            lea rcx, [rip + 0xac3bf5]
00369B23  E8 A8 C2 EF FF                  call 0x140265dd0
00369B28  90                              nop
00369B29  E9 10 A0 37 00                  jmp 0x1406e3b3e
00369B2E  49 8D 4D 38                     lea rcx, [r13 + 0x38]
00369B32  45 33 C0                        xor r8d, r8d
00369B35  33 D2                           xor edx, edx
00369B37  E8 D4 57 FD FF                  call 0x14033f310
00369B3C  E9 02 FD FF FF                  jmp 0x140369843
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPrivateFixup(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (168);
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 41) = a1 + 56;
    *(unsigned __int8 *)(v_rsp - 79 - 89) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 57) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(v_rsp - 79 - 49) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_rbx = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 184))) & (15));
    if (condition_is_not_equal) goto loc_00369460;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 624) != 0) goto loc_00369862;
loc_00369460:
    v_rdi = ((unsigned int)(*(unsigned int *)(a4 + 16))) >> (5);
    v_rdi = (unsigned int)((v_rdi) & (31));
    *(unsigned int *)(v_rsp - 79 - 85) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 81) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11299859) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 56) + 174) * 8);
    if ((*(unsigned __int64 *)(a1)) >= (*(unsigned __int64 *)(v_rip + 11299859))) goto loc_00369953;
loc_003694B9:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 368)) & (1)) == 0) goto loc_00369965;
loc_003694BF:
    a1 = (*(unsigned __int64 *)(a1)) >> (9);
    a1 = (a1) & (*(unsigned __int64 *)(gs_base + (0 + 392)));
    a1 = (a1) + (*(unsigned __int64 *)(gs_base + (0 + 392)));
    *(unsigned __int64 *)(v_rsp - 79 - 73) = a1;
    *(unsigned __int64 *)(v_rsp - 79 - 17) = *(unsigned __int64 *)(a1);
    v_r15 = (a4) - (*(unsigned __int64 *)(a1));
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (*(unsigned __int64 *)(a1));
    *(unsigned __int64 *)(v_rsp - 79 - 33) = v_r15;
    result = MiObtainFaultCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11299859) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 56) + 174) * 8), 1, (unsigned int)((unsigned int)(1 + 1)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11299859) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 56) + 174) * 8));
    if ((*(unsigned int *)(v_rsp - 79 - 85)) == 0) goto loc_003699A0;
loc_0036952E:
    result = MI_PAGE_TO_FULL_COLOR(v_r15, 1, (unsigned int)((unsigned int)(1 + 1)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11299859) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 56) + 174) * 8));
    result = MiGetPage(*(unsigned __int64 *)(v_rsp - 79 - 81), (unsigned int)((unsigned int)(result)), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11299859) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 56) + 174) * 8));
    *(unsigned __int64 *)(v_rsp - 79 - 65) = result;
    if (result == -1) goto loc_00369A85;
loc_0036955E:
    v_rdi = (result + result * 2) << (4);
    a2 = 0;
    v_rdi = (v_rdi) + (result);
    result = MiGetInPageSupportBlock((unsigned int)((unsigned int)(1 + 1)), a2, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11299859) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 56) + 174) * 8));
    if (result == 0) goto loc_00369A8C;
    *(unsigned int *)(v_rsp - 79 - 81) = 0;
    result = MiGetEffectivePagePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11299859) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 56) + 174) * 8));
    result = (unsigned __int8)((result) & (7));
    result = (unsigned __int8)((result) | (72));
    *(unsigned __int64 *)(result + 248) = v_rdi;
    *(unsigned __int8 *)(v_rsp - 79 - 81) = (unsigned __int8)(result);
    *(unsigned int *)(result + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 192)));
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 81)));
    v_stack_mC8 = result;
    *(unsigned int *)(result + 80) = 0;
    *(unsigned __int64 *)(result + 88) = 0;
    result = MiInitializeReadInProgressPfn(*(unsigned __int64 *)(v_rsp - 79 - 57), v_rsp - 79 - 65, 1, *(unsigned __int64 *)(v_rsp - 79 - 73));
    if ((unsigned __int8)(v_rbx) == 0) {
        result = *(unsigned __int64 *)(v_rsp - 79 - 49);
    }
    *(unsigned __int64 *)(v_rsp - 79 - 9) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 - 73));
    *(unsigned __int64 *)(v_rsp - 79 - 81) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 95));
    *(unsigned __int64 *)(result + 208) = *(unsigned __int64 *)(v_rsp - 79 + 95);
    result = MiReleaseFaultState(*(unsigned __int64 *)(v_rsp - 79 - 41), 1, v_rsp - 79 - 89, *(unsigned __int64 *)(v_rsp - 79 - 73));
    *(unsigned __int64 *)(v_rsp - 79 - 49) = result;
    if ((*(unsigned int *)(v_rip + 12965610)) != 0) {
        a1 = v_cr8;
        a2 = *(unsigned __int8 *)(v_rsp - 79 - 89);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_rsp - 79 - 89, *(unsigned __int64 *)(v_rsp - 79 - 73));
    }
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rsp - 79 - 85))));
    a3 = (unsigned int)((v_rsp - 79 - 89) & (56));
    a3 = (unsigned int)((a3) + (17));
    result = MiCopyPage(*(unsigned __int64 *)(v_rsp - 79 - 65), *(unsigned __int64 *)(v_rsp - 79 - 33), a3, *(unsigned __int64 *)(v_rsp - 79 - 73));
    if ((*(unsigned int *)(v_rsp - 79 - 85)) == 0) goto loc_00369995;
    result = MiReservePtes(v_rip + 11329507, 1, a3, *(unsigned __int64 *)(v_rsp - 79 - 73));
    if (result == 0) goto loc_00369A93;
    result = MiMakeProtectionPfnCompatible(4, v_rdi, a3, *(unsigned __int64 *)(v_rsp - 79 - 73));
    result = (unsigned int)((result) | (0xA0000000ULL));
    result = MiMakeValidPte(result, *(unsigned __int64 *)(v_rsp - 79 - 65), (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_rsp - 79 - 73));
    if (condition_is_below) goto loc_00369911;
loc_003696C8:
    *(unsigned __int64 *)(result) = result;
    v_rbx = (result) << (25);
    result = (result) << (25);
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) >> (16);
    if (condition_is_below) goto loc_00369706;
    if (!sign_flag) goto loc_00369AD7;
loc_00369706:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 79 + 127))) | (36));
    v_stack_mB8 = (unsigned int)(result);
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 79 + 119);
    result = MiRelocateImagePfn(*(unsigned __int64 *)(v_rsp - 79 - 81), v_rbx, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 103)), *(unsigned __int64 *)(v_rsp - 79 - 65));
loc_0036972D:
    if (result == (*(unsigned __int64 *)(v_rip + 11288556))) goto loc_00369AE9;
    result = MiReleasePtes(v_rip + 11329313, result, 1, *(unsigned __int64 *)(v_rsp - 79 - 65));
loc_00369756:
    a2 = (result) | (-1);
    result = (a2) + (a2);
    if (condition_is_equal) goto loc_003698FA;
loc_00369770:
    if ((*(unsigned int *)(v_rip + 12965282)) != 0) goto loc_00369904;
loc_00369784:
    if ((*(unsigned int *)(v_rip + 12965282)) != 0) goto loc_003697A1;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int8 *)(v_rsp - 79 - 89), a2, 1, *(unsigned __int64 *)(v_rsp - 79 - 65));
    }
    result = MiRelockFaultState(*(unsigned __int64 *)(v_rsp - 79 - 41), *(unsigned __int64 *)(v_rsp - 79 - 49), 1, *(unsigned __int64 *)(v_rsp - 79 - 65));
    result = MiIsFaultPteIntact(*(unsigned __int64 *)(v_rsp - 79 + 87), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 87)), *(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 9);
loc_003697C6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) < (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) goto loc_003698DA;
    *(unsigned int *)(v_rsp - 79 + 87) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    result = (unsigned __int8)((result) & (223));
    *(unsigned __int8 *)(v_rsp - 79 + 89) = (unsigned __int8)(result);
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)));
    *(unsigned __int64 *)(v_rdi) = 0;
    result = *(unsigned __int64 *)(v_rdi + 24);
    if (!(condition_is_below)) {
        a2 = 1;
        a1 = v_rdi;
        result = MiSetPfnModified(a1, a2, *(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 9);
    }
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_00369872;
loc_0036980A:
    result = MiRemoveLockedPageChargeAndDecRef(v_rdi, a2, *(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 9);
    *(unsigned int *)(result + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 192)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 176)))) > 1) goto loc_00369B2E;
loc_00369843:
    result = MiFreeInPageSupportBlock(result, a2, *(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 9);
loc_0036984D:
    v_rsp = (v_rsp) + (168);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000434ULL)));
loc_00369862:
    if (((unsigned int)((unsigned int)((unsigned int)(0xC0000434ULL)))) != ((unsigned int)((unsigned int)(result)))) goto loc_00369A63;
loc_0036986B:
    goto loc_0036984D;
loc_00369872:
    result = MiAddLockedPageCharge(v_rdi, 3, *(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 9);
    result = (*(unsigned __int64 *)(v_rdi + 24)) ^ (*(unsigned __int64 *)(v_rdi + 24) + 1);
    result = (result) & (3);
    result = (result) ^ (*(unsigned __int64 *)(v_rdi + 24) + 1);
    *(unsigned __int64 *)(v_rdi + 24) = result;
    *(unsigned int *)(v_rsp - 79 + 87) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    result = (unsigned __int8)((result) & (254));
    result = (unsigned __int8)((result) | (6));
    *(unsigned __int8 *)(v_rsp - 79 + 89) = (unsigned __int8)(result);
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)));
    if ((*(unsigned int *)(v_rsp - 79 - 85)) != ((unsigned int)((unsigned int)(0xC0000434ULL)))) goto loc_0036980A;
    if ((*(unsigned __int64 *)(v_rsp - 79 - 57)) < ((unsigned int)(*(unsigned int *)(v_rsp - 79 + 87)))) goto loc_0036980A;
    goto loc_0036980A;
loc_003698DA:
    v_rbx = (unsigned int)((0) + (1));
    if (((*(unsigned int *)(v_rip + 12958153)) & ((unsigned int)(v_rbx))) == 0) goto loc_0036996E;
loc_003698E9:
loc_003698EB:
    if (!sign_flag) goto loc_003697C6;
    goto loc_003698DA;
loc_003698FA:
    result = MiDeleteControlArea(*(unsigned __int64 *)(v_rdi + 24) + 1, 3, *(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 9);
    goto loc_00369770;
loc_00369904:
    result = KiRaiseIrqlProcessIrqlFlags(*(unsigned __int64 *)(v_rdi + 24) + 1, 1, *(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 9);
    goto loc_00369784;
loc_00369911:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_003696C8;
    result = (result) + (*(unsigned __int64 *)(v_rdi + 24) + 1);
    if ((*(unsigned __int64 *)(v_rsp - 79 - 73)) < result) goto loc_003696C8;
    result = MiCheckLinearProtectedPteAccessedBit(*(unsigned __int64 *)(v_rsp - 79 - 73), v_rbx, 128, v_rsp - 79 - 9);
    goto loc_003696C8;
loc_00369953:
    if ((*(unsigned __int64 *)(v_rsp - 79 - 73)) < result) goto loc_00369A72;
loc_00369965:
    *(unsigned int *)(v_rsp - 79 - 85) = 1;
    goto loc_003694BF;
loc_0036996E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12964164)))) & (64)) == 0) goto loc_003698E9;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_rsp - 79 - 73), v_rbx, 128, v_rsp - 79 - 9);
    if ((unsigned __int8)(result) == 0) goto loc_003698E9;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_rbx, 128, v_rsp - 79 - 9);
    goto loc_003698EB;
loc_00369995:
    goto loc_00369756;
loc_003699A0:
    if ((*(unsigned __int64 *)(v_rsp - 79 - 57)) < result) goto loc_0036952E;
    result = MiReleaseFaultState(result + 56, 1, v_rsp - 79 - 89, v_rsp - 79 - 9);
    *(unsigned __int64 *)(v_rsp - 79 - 25) = result;
    if ((*(unsigned int *)(v_rip + 12964695)) != ((unsigned int)((unsigned int)(0xC0000434ULL)))) {
        a1 = 1;
        a2 = *(unsigned __int8 *)(v_rsp - 79 - 89);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_rsp - 79 - 89, v_rsp - 79 - 9);
    }
    a3 = 0;
    result = MiAllocateDriverPage(*(unsigned __int64 *)(v_rsp - 79 - 81), (unsigned int)((unsigned int)(v_rdi)), a3, v_rsp - 79 - 9);
    *(unsigned __int64 *)(v_rsp - 79 - 65) = result;
    result = MiRelockFaultState(result + 56, *(unsigned __int64 *)(v_rsp - 79 - 25), a3, v_rsp - 79 - 9);
    result = MiIsFaultPteIntact(result, *(unsigned __int64 *)(result), *(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 17);
    result = (unsigned int)(-(result));
    v_rdi = (unsigned int)(~(v_rdi));
    v_rdi = (unsigned int)((v_rdi) & (0xC0000434ULL));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0036955E;
loc_00369A32:
loc_00369A36:
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = MiReleaseFreshPageAtDpc(a1, result, *(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 17);
loc_00369A63:
    goto loc_0036986B;
loc_00369A72:
    if (condition_is_above_or_equal) goto loc_00369965;
    goto loc_003694B9;
loc_00369A85:
    goto loc_00369A36;
loc_00369A8C:
    goto loc_00369A32;
loc_00369A93:
    result = (result) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 11287674, a2, a3, v_rsp - 79 - 17);
    result = ExfAcquirePushLockExclusiveEx(v_rip + 11287674, result, v_rip + 11287674, v_rsp - 79 - 17);
loc_00369AD7:
    if (*(unsigned __int64 *)(v_rip + 11287674 + 8) != 0) goto loc_0036972D;
    goto loc_00369706;
loc_00369AE9:
    *(unsigned __int64 *)(v_rip + 11287674) = *(unsigned __int64 *)(v_rip - 3510896);
    result = MiFlushSingleTbEntry(result, 2, 1, v_rsp - 79 - 17);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    result = ExfTryToWakePushLock(v_rip + 11287541, 2, 1, v_rsp - 79 - 17);
loc_00369B2E:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(v_rsp - 79 - 81) + 56, a2, a3, v_rsp - 79 - 17);
    goto loc_00369843;
}
```

## 5. (Beta) C Style

```c
int64_t MiPrivateFixup(void *Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;

    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (168);
    local_rsi = 0;
    *(void **)(local_rsp - 0x4F - 0x29) = Arg1 + 56;
    *(uint8_t *)(local_rsp - 0x4F - 0x59) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x39) = *(uint64_t *)(arg1);
    *(uint64_t *)(local_rsp - 0x4F - 0x31) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    local_rbx = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00369460;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x270) != 0) goto loc_00369862;
loc_00369460:
    local_rdi = ((uint32_t)(*(uint32_t *)(arg4 + 0x10))) >> (5);
    local_rdi = (uint32_t)((local_rdi) & (31));
    *(uint32_t *)(local_rsp - 0x4F - 0x55) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x51) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC6C13) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x38) + 0xAE) * 8);
    if ((*(uint64_t *)(arg1)) >= (*(uint64_t *)(v_rip + 0xAC6C13))) goto loc_00369953;
loc_003694B9:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x170)) & (1)) == 0) goto loc_00369965;
loc_003694BF:
    Arg1 = (*(uint64_t *)(arg1)) >> (9);
    Arg1 = (Arg1) & (*(uint64_t *)(gs_base + (0 + 0x188)));
    Arg1 = (Arg1) + (*(uint64_t *)(gs_base + (0 + 0x188)));
    *(void **)(local_rsp - 0x4F - 0x49) = Arg1;
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = *(uint64_t *)(arg1);
    local_r15 = (Arg4) - (*(uint64_t *)(arg1));
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (*(uint64_t *)(arg1));
    *(uint64_t *)(local_rsp - 0x4F - 0x21) = local_r15;
    result = MiObtainFaultCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC6C13) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x38) + 0xAE) * 8), 1, (uint32_t)((uint32_t)(1 + 1)), *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC6C13) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x38) + 0xAE) * 8));
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x55)) == 0) goto loc_003699A0;
loc_0036952E:
    result = MI_PAGE_TO_FULL_COLOR(local_r15, 1, (uint32_t)((uint32_t)(1 + 1)), *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC6C13) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x38) + 0xAE) * 8));
    result = MiGetPage(*(uint64_t *)(local_rsp - 0x4F - 0x51), (uint32_t)((uint32_t)(result)), 1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC6C13) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x38) + 0xAE) * 8));
    *(uint64_t *)(local_rsp - 0x4F - 0x41) = result;
    if (result == -1) goto loc_00369A85;
loc_0036955E:
    local_rdi = (result + result * 2) << (4);
    Arg2 = 0;
    local_rdi = (local_rdi) + (result);
    result = MiGetInPageSupportBlock((uint32_t)((uint32_t)(1 + 1)), Arg2, 1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC6C13) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x38) + 0xAE) * 8));
    if (result == 0) goto loc_00369A8C;
    *(uint32_t *)(local_rsp - 0x4F - 0x51) = 0;
    result = MiGetEffectivePagePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, 1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC6C13) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x38) + 0xAE) * 8));
    result = (uint8_t)((result) & (7));
    result = (uint8_t)((result) | (72));
    *(uint64_t *)(result + 0xF8) = local_rdi;
    *(uint8_t *)(local_rsp - 0x4F - 0x51) = (uint8_t)(result);
    *(uint32_t *)(result + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC0)));
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x51)));
    v_stack_mC8 = result;
    *(uint32_t *)(result + 0x50) = 0;
    *(uint64_t *)(result + 0x58) = 0;
    result = MiInitializeReadInProgressPfn(*(uint64_t *)(local_rsp - 0x4F - 0x39), local_rsp - 79 - 65, 1, *(uint64_t *)(local_rsp - 0x4F - 0x49));
    if ((uint8_t)(local_rbx) == 0) {
        result = *(uint64_t *)(local_rsp - 0x4F - 0x31);
    }
    *(uint64_t *)(local_rsp - 0x4F - 0x9) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F - 0x49));
    *(uint64_t *)(local_rsp - 0x4F - 0x51) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x5F));
    *(uint64_t *)(result + 0xD0) = *(uint64_t *)(local_rsp - 0x4F + 0x5F);
    result = MiReleaseFaultState(*(uint64_t *)(local_rsp - 0x4F - 0x29), 1, local_rsp - 79 - 89, *(uint64_t *)(local_rsp - 0x4F - 0x49));
    *(uint64_t *)(local_rsp - 0x4F - 0x31) = result;
    if ((*(uint32_t *)(v_rip + 0xC5D6EA)) != 0) {
        Arg1 = v_cr8;
        Arg2 = *(uint8_t *)(local_rsp - 0x4F - 0x59);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, local_rsp - 79 - 89, *(uint64_t *)(local_rsp - 0x4F - 0x49));
    }
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x55))));
    Arg3 = (uint32_t)((local_rsp - 79 - 89) & (56));
    Arg3 = (uint32_t)((Arg3) + (17));
    result = MiCopyPage(*(uint64_t *)(local_rsp - 0x4F - 0x41), *(uint64_t *)(local_rsp - 0x4F - 0x21), Arg3, *(uint64_t *)(local_rsp - 0x4F - 0x49));
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x55)) == 0) goto loc_00369995;
    result = MiReservePtes(v_rip + 11329507, 1, Arg3, *(uint64_t *)(local_rsp - 0x4F - 0x49));
    if (result == 0) goto loc_00369A93;
    result = MiMakeProtectionPfnCompatible(4, local_rdi, Arg3, *(uint64_t *)(local_rsp - 0x4F - 0x49));
    result = (uint32_t)((result) | (0xA0000000ULL));
    result = MiMakeValidPte(result, *(uint64_t *)(local_rsp - 0x4F - 0x41), (uint32_t)((uint32_t)(result)), *(uint64_t *)(local_rsp - 0x4F - 0x49));
    if (condition_is_below) goto loc_00369911;
loc_003696C8:
    *(uint64_t *)(result) = result;
    local_rbx = (result) << (25);
    result = (result) << (25);
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) >> (16);
    if (condition_is_below) goto loc_00369706;
    if (!sign_flag) goto loc_00369AD7;
loc_00369706:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x7F))) | (36));
    v_stack_mB8 = (uint32_t)(result);
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x4F + 0x77);
    result = MiRelocateImagePfn(*(uint64_t *)(local_rsp - 0x4F - 0x51), local_rbx, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x67)), *(uint64_t *)(local_rsp - 0x4F - 0x41));
loc_0036972D:
    if (result == (*(uint64_t *)(v_rip + 0xAC3FEC))) goto loc_00369AE9;
    result = MiReleasePtes(v_rip + 11329313, result, 1, *(uint64_t *)(local_rsp - 0x4F - 0x41));
loc_00369756:
    Arg2 = (result) | (-1);
    result = (Arg2) + (Arg2);
    if (condition_is_equal) goto loc_003698FA;
loc_00369770:
    if ((*(uint32_t *)(v_rip + 0xC5D5A2)) != 0) goto loc_00369904;
loc_00369784:
    if ((*(uint32_t *)(v_rip + 0xC5D5A2)) != 0) goto loc_003697A1;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint8_t *)(local_rsp - 0x4F - 0x59), Arg2, 1, *(uint64_t *)(local_rsp - 0x4F - 0x41));
    }
    result = MiRelockFaultState(*(uint64_t *)(local_rsp - 0x4F - 0x29), *(uint64_t *)(local_rsp - 0x4F - 0x31), 1, *(uint64_t *)(local_rsp - 0x4F - 0x41));
    result = MiIsFaultPteIntact(*(uint64_t *)(local_rsp - 0x4F + 0x57), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x57)), *(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 9);
loc_003697C6:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) < (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) goto loc_003698DA;
    *(uint32_t *)(local_rsp - 0x4F + 0x57) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    result = (uint8_t)((result) & (223));
    *(uint8_t *)(local_rsp - 0x4F + 0x59) = (uint8_t)(result);
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)));
    *(uint64_t *)(local_rdi) = 0;
    result = *(uint64_t *)(local_rdi + 0x18);
    if (!(condition_is_below)) {
        Arg2 = 1;
        Arg1 = local_rdi;
        result = MiSetPfnModified(Arg1, Arg2, *(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 9);
    }
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_00369872;
loc_0036980A:
    result = MiRemoveLockedPageChargeAndDecRef(local_rdi, Arg2, *(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 9);
    *(uint32_t *)(result + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC0)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xB0)))) > 1) goto loc_00369B2E;
loc_00369843:
    result = MiFreeInPageSupportBlock(result, Arg2, *(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 9);
loc_0036984D:
    local_rsp = (local_rsp) + (168);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000434ULL)));
loc_00369862:
    if (((uint32_t)((uint32_t)((uint32_t)(0xC0000434ULL)))) != ((uint32_t)((uint32_t)(result)))) goto loc_00369A63;
loc_0036986B:
    goto loc_0036984D;
loc_00369872:
    result = MiAddLockedPageCharge(local_rdi, 3, *(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 9);
    result = (*(uint64_t *)(local_rdi + 0x18)) ^ (*(uint64_t *)(local_rdi + 0x18) + 1);
    result = (result) & (3);
    result = (result) ^ (*(uint64_t *)(local_rdi + 0x18) + 1);
    *(uint64_t *)(local_rdi + 0x18) = result;
    *(uint32_t *)(local_rsp - 0x4F + 0x57) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    result = (uint8_t)((result) & (254));
    result = (uint8_t)((result) | (6));
    *(uint8_t *)(local_rsp - 0x4F + 0x59) = (uint8_t)(result);
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)));
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x55)) != ((uint32_t)((uint32_t)(0xC0000434ULL)))) goto loc_0036980A;
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x39)) < ((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x57)))) goto loc_0036980A;
    goto loc_0036980A;
loc_003698DA:
    local_rbx = (uint32_t)((0) + (1));
    if (((*(uint32_t *)(v_rip + 0xC5B9C9)) & ((uint32_t)(local_rbx))) == 0) goto loc_0036996E;
loc_003698E9:
loc_003698EB:
    if (!sign_flag) goto loc_003697C6;
    goto loc_003698DA;
loc_003698FA:
    result = MiDeleteControlArea(*(uint64_t *)(local_rdi + 0x18) + 1, 3, *(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 9);
    goto loc_00369770;
loc_00369904:
    result = KiRaiseIrqlProcessIrqlFlags(*(uint64_t *)(local_rdi + 0x18) + 1, 1, *(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 9);
    goto loc_00369784;
loc_00369911:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_003696C8;
    result = (result) + (*(uint64_t *)(local_rdi + 0x18) + 1);
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x49)) < result) goto loc_003696C8;
    result = MiCheckLinearProtectedPteAccessedBit(*(uint64_t *)(local_rsp - 0x4F - 0x49), local_rbx, 128, local_rsp - 79 - 9);
    goto loc_003696C8;
loc_00369953:
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x49)) < result) goto loc_00369A72;
loc_00369965:
    *(uint32_t *)(local_rsp - 0x4F - 0x55) = 1;
    goto loc_003694BF;
loc_0036996E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC5D144)))) & (64)) == 0) goto loc_003698E9;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(local_rsp - 0x4F - 0x49), local_rbx, 128, local_rsp - 79 - 9);
    if ((uint8_t)(result) == 0) goto loc_003698E9;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), local_rbx, 128, local_rsp - 79 - 9);
    goto loc_003698EB;
loc_00369995:
    goto loc_00369756;
loc_003699A0:
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x39)) < result) goto loc_0036952E;
    result = MiReleaseFaultState(result + 56, 1, local_rsp - 79 - 89, local_rsp - 79 - 9);
    *(uint64_t *)(local_rsp - 0x4F - 0x19) = result;
    if ((*(uint32_t *)(v_rip + 0xC5D357)) != ((uint32_t)((uint32_t)(0xC0000434ULL)))) {
        Arg1 = 1;
        Arg2 = *(uint8_t *)(local_rsp - 0x4F - 0x59);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, local_rsp - 79 - 89, local_rsp - 79 - 9);
    }
    Arg3 = 0;
    result = MiAllocateDriverPage(*(uint64_t *)(local_rsp - 0x4F - 0x51), (uint32_t)((uint32_t)(local_rdi)), Arg3, local_rsp - 79 - 9);
    *(uint64_t *)(local_rsp - 0x4F - 0x41) = result;
    result = MiRelockFaultState(result + 56, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, local_rsp - 79 - 9);
    result = MiIsFaultPteIntact(result, *(uint64_t *)(result), *(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 17);
    result = (uint32_t)(-(result));
    local_rdi = (uint32_t)(~(local_rdi));
    local_rdi = (uint32_t)((local_rdi) & (0xC0000434ULL));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0036955E;
loc_00369A32:
loc_00369A36:
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiReleaseFreshPageAtDpc(Arg1, result, *(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 17);
loc_00369A63:
    goto loc_0036986B;
loc_00369A72:
    if (condition_is_above_or_equal) goto loc_00369965;
    goto loc_003694B9;
loc_00369A85:
    goto loc_00369A36;
loc_00369A8C:
    goto loc_00369A32;
loc_00369A93:
    result = (result) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 11287674, Arg2, Arg3, local_rsp - 79 - 17);
    result = ExfAcquirePushLockExclusiveEx(v_rip + 11287674, result, v_rip + 11287674, local_rsp - 79 - 17);
loc_00369AD7:
    if (*(uint64_t *)(v_rip + 0xAC3C7A + 0x8) != 0) goto loc_0036972D;
    goto loc_00369706;
loc_00369AE9:
    *(uint64_t *)(v_rip + 0xAC3C7A) = *(uint64_t *)(v_rip - 0x359270);
    result = MiFlushSingleTbEntry(result, 2, 1, local_rsp - 79 - 17);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    result = ExfTryToWakePushLock(v_rip + 11287541, 2, 1, local_rsp - 79 - 17);
loc_00369B2E:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(local_rsp - 0x4F - 0x51) + 56, Arg2, Arg3, local_rsp - 79 - 17);
    goto loc_00369843;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R/W` |
| `Arg4` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003693E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
