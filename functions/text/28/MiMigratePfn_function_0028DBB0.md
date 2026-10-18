# MiMigratePfn

- RVA: `0x0028DBB0`–`0x0028E2C9` (길이 `1,817` bytes)
- VA: `0x000000014028DBB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00067050`
- 디코드: `449`개 명령, `1,817/1,817` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0028DBF4` → [MiGetPfnSlabType](MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x0028DC42` → [MiCanPageMove](../38/MiCanPageMove_function_00383710.md) (function, `0x00383710`)
- `0x0028DC4E` → [MI_NODE_FROM_PFN](../2B/MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x0028DC62` → [MiComputeFaultNode](../2B/MiComputeFaultNode_function_002B60C0.md) (function, `0x002B60C0`)
- `0x0028DC76` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0028DD12` → [MiIsPfnCommitNotCharged](../31/MiIsPfnCommitNotCharged_function_00317370.md) (function, `0x00317370`)
- `0x0028DD28` → [MiObtainFaultCharges](MiObtainFaultCharges_function_0028AEB0.md) (function, `0x0028AEB0`)
- `0x0028DD49` → [MiGetSystemRegionType](MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x0028DD64` → [MiGetPage](MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0028DD96` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x0028DDB4` → [MiGetInPageSupportBlock](../36/MiGetInPageSupportBlock_function_00362500.md) (function, `0x00362500`)
- `0x0028DDF3` → [MiFinalizePageAttribute](../33/MiFinalizePageAttribute_function_00332E30.md) (function, `0x00332E30`)
- `0x0028DDFE` → [MiCopyPfnEntryEx](../2B/MiCopyPfnEntryEx_function_002B2670.md) (function, `0x002B2670`)
- `0x0028DE92` → [MI_READ_PTE_LOCK_FREE](MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0028DE9E` → [MiUpdateTransitionPteFrame](../38/MiUpdateTransitionPteFrame_function_00385EDC.md) (function, `0x00385EDC`)
- `0x0028DEAF` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x0028DF06` → [MiAddLockedPageCharge](MiAddLockedPageCharge_function_0028B550.md) (function, `0x0028B550`)
- `0x0028DF19` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0028DF5B` → [MiCopyPage](../2B/MiCopyPage_function_002B1B30.md) (function, `0x002B1B30`)
- `0x0028DF6A` → [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x0028DF85` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x0028DFAA` → [MiSetPfnIdentity](../2A/MiSetPfnIdentity_function_002A2350.md) (function, `0x002A2350`)
- `0x0028DFB7` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x0028DFFC` → [MiRemoveLockedPageCharge](../24/MiRemoveLockedPageCharge_function_00246950.md) (function, `0x00246950`)
- `0x0028E0B3` → [MiCapturePfnPageFileInfoInline](../22/MiCapturePfnPageFileInfoInline_function_0022F650.md) (function, `0x0022F650`)
- `0x0028E186` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028E195` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0028E1AD` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028E1BC` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0028E1D4` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028E1E3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0028E1FB` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028E20A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0028E222` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028E231` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0028E23F` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x0028E255` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x0028E27D` → [MiReturnFreeZeroPage](../33/MiReturnFreeZeroPage_function_00334BD0.md) (function, `0x00334BD0`)
- `0x0028E29C` → [MiReturnFaultCharges](../36/MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)

### Direct callers
- [sub_00283850](Unknown_function_00283850.md) at `0x00283A37`

### Static image references
- `0x0028DC02` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x0028DC8C` → RVA `0x00E30088` (`.data`; read)
- `0x0028DCB3` → RVA `0x00E2DCC0` (`.data`; read)
- `0x0028DCCA` → RVA `0x00E2DBD0` (`.data`; read)
- `0x0028E0C3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0028E178` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x0028E096` → [sub_006DA4DA + 0x52](../6D/Unknown_function_006DA4DA.md) (`tail-transfer`)
  - `0x0028E0A5` → [sub_006DA4DA + 0x44](../6D/Unknown_function_006DA4DA.md) (`tail-transfer`)
  - `0x0028E0BB` → [sub_006DA4DA + 0x44](../6D/Unknown_function_006DA4DA.md) (`tail-transfer`)
  - `0x0028E2BF` → [sub_006DA4DA](../6D/Unknown_function_006DA4DA.md) (`tail-transfer`)
  - `0x0028E2C4` → [sub_006DA4DA + 0x20](../6D/Unknown_function_006DA4DA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0028DBB0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0028DBB5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0028DBBA  55                              push rbp
0028DBBB  53                              push rbx
0028DBBC  56                              push rsi
0028DBBD  57                              push rdi
0028DBBE  41 54                           push r12
0028DBC0  41 55                           push r13
0028DBC2  41 56                           push r14
0028DBC4  41 57                           push r15
0028DBC6  48 8B EC                        mov rbp, rsp
0028DBC9  48 83 EC 68                     sub rsp, 0x68
0028DBCD  48 0F BA 62 28 35               bt qword ptr [rdx + 0x28], 0x35
0028DBD3  48 8B 01                        mov rax, qword ptr [rcx]
0028DBD6  48 8B 79 38                     mov rdi, qword ptr [rcx + 0x38]
0028DBDA  0F 57 C0                        xorps xmm0, xmm0
0028DBDD  4C 8B 69 10                     mov r13, qword ptr [rcx + 0x10]
0028DBE1  4C 8B FA                        mov r15, rdx
0028DBE4  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
0028DBE8  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0028DBEC  48 8B D9                        mov rbx, rcx
0028DBEF  72 1B                           jb 0x14028dc0c
0028DBF1  48 8B CA                        mov rcx, rdx
0028DBF4  E8 D7 06 00 00                  call 0x14028e2d0
0028DBF9  83 F8 09                        cmp eax, 9
0028DBFC  75 0E                           jne 0x14028dc0c
0028DBFE  44 8D 70 F8                     lea r14d, [rax - 8]
0028DC02  66 44 39 35 F6 73 D3 00         cmp word ptr [rip + 0xd373f6], r14w
0028DC0A  77 15                           ja 0x14028dc21
0028DC0C  49 8B C7                        mov rax, r15
0028DC0F  48 83 C4 68                     add rsp, 0x68
0028DC13  41 5F                           pop r15
0028DC15  41 5E                           pop r14
0028DC17  41 5D                           pop r13
0028DC19  41 5C                           pop r12
0028DC1B  5F                              pop rdi
0028DC1C  5E                              pop rsi
0028DC1D  5B                              pop rbx
0028DC1E  5D                              pop rbp
0028DC1F  C3                              ret
0028DC20  CC                              int3
0028DC21  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
0028DC25  45 33 E4                        xor r12d, r12d
0028DC28  66 85 C0                        test ax, ax
0028DC2B  75 DF                           jne 0x14028dc0c
0028DC2D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0028DC36  F6 80 A8 05 00 00 40            test byte ptr [rax + 0x5a8], 0x40
0028DC3D  75 CD                           jne 0x14028dc0c
0028DC3F  49 8B CF                        mov rcx, r15
0028DC42  E8 C9 5A 0F 00                  call 0x140383710
0028DC47  85 C0                           test eax, eax
0028DC49  74 C1                           je 0x14028dc0c
0028DC4B  49 8B CF                        mov rcx, r15
0028DC4E  E8 DD 32 02 00                  call 0x1402b0f30
0028DC53  4C 8D 45 D8                     lea r8, [rbp - 0x28]
0028DC57  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
0028DC5B  33 D2                           xor edx, edx
0028DC5D  48 8B CB                        mov rcx, rbx
0028DC60  8B F0                           mov esi, eax
0028DC62  E8 59 84 02 00                  call 0x1402b60c0
0028DC67  4C 8D 4D E8                     lea r9, [rbp - 0x18]
0028DC6B  44 8B C0                        mov r8d, eax
0028DC6E  41 8D 54 24 03                  lea edx, [r12 + 3]
0028DC73  48 8B CF                        mov rcx, rdi
0028DC76  E8 95 27 09 00                  call 0x140320410
0028DC7B  8B 5D F0                        mov ebx, dword ptr [rbp - 0x10]
0028DC7E  C1 EB 09                        shr ebx, 9
0028DC81  83 E3 3F                        and ebx, 0x3f
0028DC84  3B DE                           cmp ebx, esi
0028DC86  74 84                           je 0x14028dc0c
0028DC88  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
0028DC8C  48 8B 0D F5 23 BA 00            mov rcx, qword ptr [rip + 0xba23f5]
0028DC93  48 C1 E8 2B                     shr rax, 0x2b
0028DC97  25 FF 03 00 00                  and eax, 0x3ff
0028DC9C  4C 8B 14 C1                     mov r10, qword ptr [rcx + rax*8]
0028DCA0  41 8B C6                        mov eax, r14d
0028DCA3  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
0028DCA7  4C 89 55 C8                     mov qword ptr [rbp - 0x38], r10
0028DCAB  F0 0F C1 01                     lock xadd dword ptr [rcx], eax
0028DCAF  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
0028DCB3  4C 8D 0D 06 00 BA 00            lea r9, [rip + 0xba0006]
0028DCBA  33 D2                           xor edx, edx
0028DCBC  49 8B C8                        mov rcx, r8
0028DCBF  48 C1 E9 10                     shr rcx, 0x10
0028DCC3  83 E1 03                        and ecx, 3
0028DCC6  41 F7 34 89                     div dword ptr [r9 + rcx*4]
0028DCCA  48 8B 05 FF FE B9 00            mov rax, qword ptr [rip + 0xb9feff]
0028DCD1  41 33 D0                        xor edx, r8d
0028DCD4  44 0F B6 F2                     movzx r14d, dl
0028DCD8  0F B7 15 21 73 D3 00            movzx edx, word ptr [rip + 0xd37321]
0028DCDF  45 33 F0                        xor r14d, r8d
0028DCE2  8B CA                           mov ecx, edx
0028DCE4  0F AF CB                        imul ecx, ebx
0028DCE7  4C 8D 04 88                     lea r8, [rax + rcx*4]
0028DCEB  49 8D 04 90                     lea rax, [r8 + rdx*4]
0028DCEF  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
0028DCF3  4C 3B C0                        cmp r8, rax
0028DCF6  0F 82 16 03 00 00               jb 0x14028e012
0028DCFC  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
0028DD00  41 BB 05 00 00 00               mov r11d, 5
0028DD06  48 85 C0                        test rax, rax
0028DD09  0F 88 48 03 00 00               js 0x14028e057
0028DD0F  49 8B CF                        mov rcx, r15
0028DD12  E8 59 96 08 00                  call 0x140317370
0028DD17  85 C0                           test eax, eax
0028DD19  45 0F 45 E3                     cmovne r12d, r11d
0028DD1D  45 8B C4                        mov r8d, r12d
0028DD20  BA 01 00 00 00                  mov edx, 1
0028DD25  49 8B CA                        mov rcx, r10
0028DD28  E8 83 D1 FF FF                  call 0x14028aeb0
0028DD2D  48 85 C0                        test rax, rax
0028DD30  0F 84 D6 FE FF FF               je 0x14028dc0c
0028DD36  BF 02 00 00 00                  mov edi, 2
0028DD3B  41 F6 C5 01                     test r13b, 1
0028DD3F  0F 85 1A 05 00 00               jne 0x14028e25f
0028DD45  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
0028DD49  E8 32 0F 00 00                  call 0x14028ec80
0028DD4E  83 F8 0B                        cmp eax, 0xb
0028DD51  0F 84 17 05 00 00               je 0x14028e26e
0028DD57  44 8B C7                        mov r8d, edi
0028DD5A  41 8B D6                        mov edx, r14d
0028DD5D  48 8B 7D C8                     mov rdi, qword ptr [rbp - 0x38]
0028DD61  48 8B CF                        mov rcx, rdi
0028DD64  E8 57 A7 FF FF                  call 0x1402884c0
0028DD69  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0028DD6D  48 8B C8                        mov rcx, rax
0028DD70  48 83 F8 FF                     cmp rax, -1
0028DD74  0F 84 17 05 00 00               je 0x14028e291
0028DD7A  4C 8D 34 40                     lea r14, [rax + rax*2]
0028DD7E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0028DD88  49 C1 E6 04                     shl r14, 4
0028DD8C  48 8B C0                        mov rax, rax
0028DD8F  4C 03 F0                        add r14, rax
0028DD92  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
0028DD96  E8 35 AF 0A 00                  call 0x140338cd0
0028DD9B  3B D8                           cmp ebx, eax
0028DD9D  0F 85 03 05 00 00               jne 0x14028e2a6
0028DDA3  33 F6                           xor esi, esi
0028DDA5  48 39 75 58                     cmp qword ptr [rbp + 0x58], rsi
0028DDA9  0F 84 BD 03 00 00               je 0x14028e16c
0028DDAF  33 D2                           xor edx, edx
0028DDB1  8D 4E 06                        lea ecx, [rsi + 6]
0028DDB4  E8 47 47 0D 00                  call 0x140362500
0028DDB9  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0028DDBD  4C 8B E8                        mov r13, rax
0028DDC0  48 85 C0                        test rax, rax
0028DDC3  0F 84 FB 04 00 00               je 0x14028e2c4
0028DDC9  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
0028DDCD  8B DE                           mov ebx, esi
0028DDCF  C1 E8 10                        shr eax, 0x10
0028DDD2  41 BC 01 00 00 00               mov r12d, 1
0028DDD8  0F B6 F8                        movzx edi, al
0028DDDB  C1 EF 06                        shr edi, 6
0028DDDE  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
0028DDE5  0F 82 D5 02 00 00               jb 0x14028e0c0
0028DDEB  45 8B C4                        mov r8d, r12d
0028DDEE  8B D7                           mov edx, edi
0028DDF0  49 8B CE                        mov rcx, r14
0028DDF3  E8 38 50 0A 00                  call 0x140332e30
0028DDF8  49 8B D7                        mov rdx, r15
0028DDFB  49 8B CE                        mov rcx, r14
0028DDFE  E8 6D 48 02 00                  call 0x1402b2670
0028DE03  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0028DE07  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
0028DE11  48 23 C1                        and rax, rcx
0028DE14  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
0028DE18  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
0028DE1C  89 45 48                        mov dword ptr [rbp + 0x48], eax
0028DE1F  66 44 89 65 48                  mov word ptr [rbp + 0x48], r12w
0028DE24  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
0028DE27  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
0028DE2B  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
0028DE2F  89 45 48                        mov dword ptr [rbp + 0x48], eax
0028DE32  C1 E8 10                        shr eax, 0x10
0028DE35  24 FD                           and al, 0xfd
0028DE37  0C 05                           or al, 5
0028DE39  88 45 4A                        mov byte ptr [rbp + 0x4a], al
0028DE3C  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
0028DE3F  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
0028DE43  4D 85 ED                        test r13, r13
0028DE46  74 36                           je 0x14028de7e
0028DE48  41 8B 85 C0 00 00 00            mov eax, dword ptr [r13 + 0xc0]
0028DE4F  0F BA E8 07                     bts eax, 7
0028DE53  41 89 85 C0 00 00 00            mov dword ptr [r13 + 0xc0], eax
0028DE5A  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
0028DE5E  89 45 48                        mov dword ptr [rbp + 0x48], eax
0028DE61  C1 E8 10                        shr eax, 0x10
0028DE64  0C 20                           or al, 0x20
0028DE66  88 45 4A                        mov byte ptr [rbp + 0x4a], al
0028DE69  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
0028DE6C  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
0028DE70  49 8D 45 20                     lea rax, [r13 + 0x20]
0028DE74  49 89 06                        mov qword ptr [r14], rax
0028DE77  4D 89 B5 F8 00 00 00            mov qword ptr [r13 + 0xf8], r14
0028DE7E  4D 8B 66 08                     mov r12, qword ptr [r14 + 8]
0028DE82  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0028DE8C  4C 0B E0                        or r12, rax
0028DE8F  49 8B CC                        mov rcx, r12
0028DE92  E8 09 4A FF FF                  call 0x1402828a0
0028DE97  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
0028DE9B  48 8B C8                        mov rcx, rax
0028DE9E  E8 39 80 0F 00                  call 0x140385edc
0028DEA3  49 8B CC                        mov rcx, r12
0028DEA6  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0028DEAA  48 8B D8                        mov rbx, rax
0028DEAD  8B FE                           mov edi, esi
0028DEAF  E8 4C 1C FB FF                  call 0x14023fb00
0028DEB4  85 C0                           test eax, eax
0028DEB6  0F 85 7F 03 00 00               jne 0x14028e23b
0028DEBC  49 89 1C 24                     mov qword ptr [r12], rbx
0028DEC0  85 FF                           test edi, edi
0028DEC2  0F 85 87 03 00 00               jne 0x14028e24f
0028DEC8  48 BE FF FF FF FF FF FF FF 7F   movabs rsi, 0x7fffffffffffffff
0028DED2  F0 49 21 76 18                  lock and qword ptr [r14 + 0x18], rsi
0028DED7  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0028DEDB  48 8D 58 18                     lea rbx, [rax + 0x18]
0028DEDF  48 85 C0                        test rax, rax
0028DEE2  0F 84 57 02 00 00               je 0x14028e13f
0028DEE8  33 FF                           xor edi, edi
0028DEEA  44 8D 6F 01                     lea r13d, [rdi + 1]
0028DEEE  F0 48 0F BA 2B 3F               lock bts qword ptr [rbx], 0x3f
0028DEF4  0F 82 53 02 00 00               jb 0x14028e14d
0028DEFA  48 8B 7D 58                     mov rdi, qword ptr [rbp + 0x58]
0028DEFE  BA 03 00 00 00                  mov edx, 3
0028DF03  48 8B CF                        mov rcx, rdi
0028DF06  E8 45 D6 FF FF                  call 0x14028b550
0028DF0B  F0 48 21 33                     lock and qword ptr [rbx], rsi
0028DF0F  F0 49 21 77 18                  lock and qword ptr [r15 + 0x18], rsi
0028DF14  B2 11                           mov dl, 0x11
0028DF16  48 8B CF                        mov rcx, rdi
0028DF19  E8 72 81 FB FF                  call 0x140246090
0028DF1E  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
0028DF22  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
0028DF26  4C 89 28                        mov qword ptr [rax], r13
0028DF29  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0028DF33  48 8B C0                        mov rax, rax
0028DF36  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
0028DF3A  4D 8B EF                        mov r13, r15
0028DF3D  4C 2B E8                        sub r13, rax
0028DF40  41 B8 02 01 00 00               mov r8d, 0x102
0028DF46  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0028DF50  49 C1 FD 04                     sar r13, 4
0028DF54  4C 0F AF E8                     imul r13, rax
0028DF58  49 8B D5                        mov rdx, r13
0028DF5B  E8 D0 3B 02 00                  call 0x1402b1b30
0028DF60  48 85 FF                        test rdi, rdi
0028DF63  74 2D                           je 0x14028df92
0028DF65  33 D2                           xor edx, edx
0028DF67  49 8B CC                        mov rcx, r12
0028DF6A  E8 11 AC 02 00                  call 0x1402b8b80
0028DF6F  33 FF                           xor edi, edi
0028DF71  44 8D 77 01                     lea r14d, [rdi + 1]
0028DF75  F0 48 0F BA 2B 3F               lock bts qword ptr [rbx], 0x3f
0028DF7B  0F 82 9F 01 00 00               jb 0x14028e120
0028DF81  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
0028DF85  E8 46 7A FB FF                  call 0x1402459d0
0028DF8A  F0 48 21 33                     lock and qword ptr [rbx], rsi
0028DF8E  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
0028DF92  33 DB                           xor ebx, ebx
0028DF94  44 8D 63 01                     lea r12d, [rbx + 1]
0028DF98  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
0028DF9F  0F 82 3B 01 00 00               jb 0x14028e0e0
0028DFA5  33 D2                           xor edx, edx
0028DFA7  49 8B CF                        mov rcx, r15
0028DFAA  E8 A1 43 01 00                  call 0x1402a2350
0028DFAF  BA 02 00 00 00                  mov edx, 2
0028DFB4  49 8B CD                        mov rcx, r13
0028DFB7  E8 64 6D 0A 00                  call 0x140334d20
0028DFBC  F0 49 21 77 18                  lock and qword ptr [r15 + 0x18], rsi
0028DFC1  4C 8B 65 58                     mov r12, qword ptr [rbp + 0x58]
0028DFC5  33 DB                           xor ebx, ebx
0028DFC7  44 8D 7B 01                     lea r15d, [rbx + 1]
0028DFCB  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
0028DFD2  0F 82 28 01 00 00               jb 0x14028e100
0028DFD8  41 8B 7E 20                     mov edi, dword ptr [r14 + 0x20]
0028DFDC  49 8B CE                        mov rcx, r14
0028DFDF  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
0028DFE3  89 45 48                        mov dword ptr [rbp + 0x48], eax
0028DFE6  C1 E8 10                        shr eax, 0x10
0028DFE9  24 DF                           and al, 0xdf
0028DFEB  88 45 4A                        mov byte ptr [rbp + 0x4a], al
0028DFEE  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
0028DFF1  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
0028DFF5  49 C7 06 00 00 00 00            mov qword ptr [r14], 0
0028DFFC  E8 4F 89 FB FF                  call 0x140246950
0028E001  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
0028E005  48 85 C9                        test rcx, rcx
0028E008  75 67                           jne 0x14028e071
0028E00A  49 8B C6                        mov rax, r14
0028E00D  E9 FD FB FF FF                  jmp 0x14028dc0f
0028E012  41 8B 00                        mov eax, dword ptr [r8]
0028E015  3B C6                           cmp eax, esi
0028E017  0F 84 EF FB FF FF               je 0x14028dc0c
0028E01D  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
0028E021  48 69 C8 80 DF 00 00            imul rcx, rax, 0xdf80
0028E028  48 8B 84 11 08 0F 00 00         mov rax, qword ptr [rcx + rdx + 0xf08]
0028E030  48 85 C0                        test rax, rax
0028E033  0F 85 C3 FC FF FF               jne 0x14028dcfc
0028E039  48 8B 84 11 10 0F 00 00         mov rax, qword ptr [rcx + rdx + 0xf10]
0028E041  48 85 C0                        test rax, rax
0028E044  0F 85 B2 FC FF FF               jne 0x14028dcfc
0028E04A  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0028E04E  49 83 C0 04                     add r8, 4
0028E052  E9 9C FC FF FF                  jmp 0x14028dcf3
0028E057  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
0028E05B  48 0F BA E0 0A                  bt rax, 0xa
0028E060  0F 83 A9 FC FF FF               jae 0x14028dd0f
0028E066  41 BC 01 00 00 00               mov r12d, 1
0028E06C  E9 AC FC FF FF                  jmp 0x14028dd1d
0028E071  8B 81 C0 00 00 00               mov eax, dword ptr [rcx + 0xc0]
0028E077  0F BA F0 07                     btr eax, 7
0028E07B  89 81 C0 00 00 00               mov dword ptr [rcx + 0xc0], eax
0028E081  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0028E085  48 0F BA E0 3E                  bt rax, 0x3e
0028E08A  0F 83 7A FF FF FF               jae 0x14028e00a
0028E090  33 DB                           xor ebx, ebx
0028E092  66 41 3B FF                     cmp di, r15w
0028E096  0F 85 90 C4 44 00               jne 0x1406da52c
0028E09C  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
0028E0A0  48 0F BA E0 0A                  bt rax, 0xa
0028E0A5  0F 82 73 C4 44 00               jb 0x1406da51e
0028E0AB  45 8B C7                        mov r8d, r15d
0028E0AE  33 D2                           xor edx, edx
0028E0B0  49 8B CE                        mov rcx, r14
0028E0B3  E8 98 15 FA FF                  call 0x14022f650
0028E0B8  48 8B D8                        mov rbx, rax
0028E0BB  E9 5E C4 44 00                  jmp 0x1406da51e
0028E0C0  41 03 DC                        add ebx, r12d
0028E0C3  85 1D E3 71 D3 00               test dword ptr [rip + 0xd371e3], ebx
0028E0C9  0F 84 A9 00 00 00               je 0x14028e178
0028E0CF  F3 90                           pause
0028E0D1  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0028E0D5  48 85 C0                        test rax, rax
0028E0D8  0F 89 00 FD FF FF               jns 0x14028ddde
0028E0DE  EB E0                           jmp 0x14028e0c0
0028E0E0  41 03 DC                        add ebx, r12d
0028E0E3  85 1D C3 71 D3 00               test dword ptr [rip + 0xd371c3], ebx
0028E0E9  0F 84 B0 00 00 00               je 0x14028e19f
0028E0EF  F3 90                           pause
0028E0F1  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
0028E0F5  48 85 C0                        test rax, rax
0028E0F8  0F 89 9A FE FF FF               jns 0x14028df98
0028E0FE  EB E0                           jmp 0x14028e0e0
0028E100  41 03 DF                        add ebx, r15d
0028E103  85 1D A3 71 D3 00               test dword ptr [rip + 0xd371a3], ebx
0028E109  0F 84 B7 00 00 00               je 0x14028e1c6
0028E10F  F3 90                           pause
0028E111  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0028E115  48 85 C0                        test rax, rax
0028E118  0F 89 AD FE FF FF               jns 0x14028dfcb
0028E11E  EB E0                           jmp 0x14028e100
0028E120  41 03 FE                        add edi, r14d
0028E123  85 3D 83 71 D3 00               test dword ptr [rip + 0xd37183], edi
0028E129  0F 84 BE 00 00 00               je 0x14028e1ed
0028E12F  F3 90                           pause
0028E131  48 8B 03                        mov rax, qword ptr [rbx]
0028E134  48 85 C0                        test rax, rax
0028E137  0F 89 38 FE FF FF               jns 0x14028df75
0028E13D  EB E1                           jmp 0x14028e120
0028E13F  F0 49 21 77 18                  lock and qword ptr [r15 + 0x18], rsi
0028E144  48 8B 7D 58                     mov rdi, qword ptr [rbp + 0x58]
0028E148  E9 DC FD FF FF                  jmp 0x14028df29
0028E14D  41 03 FD                        add edi, r13d
0028E150  85 3D 56 71 D3 00               test dword ptr [rip + 0xd37156], edi
0028E156  0F 84 B8 00 00 00               je 0x14028e214
0028E15C  F3 90                           pause
0028E15E  48 8B 03                        mov rax, qword ptr [rbx]
0028E161  48 85 C0                        test rax, rax
0028E164  0F 89 84 FD FF FF               jns 0x14028deee
0028E16A  EB E1                           jmp 0x14028e14d
0028E16C  4C 8B EE                        mov r13, rsi
0028E16F  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
0028E173  E9 51 FC FF FF                  jmp 0x14028ddc9
0028E178  8B 05 3A 89 D3 00               mov eax, dword ptr [rip + 0xd3893a]
0028E17E  A8 40                           test al, 0x40
0028E180  0F 84 49 FF FF FF               je 0x14028e0cf
0028E186  E8 05 13 08 00                  call 0x14030f490
0028E18B  84 C0                           test al, al
0028E18D  0F 84 3C FF FF FF               je 0x14028e0cf
0028E193  8B CB                           mov ecx, ebx
0028E195  E8 C6 12 08 00                  call 0x14030f460
0028E19A  E9 32 FF FF FF                  jmp 0x14028e0d1
0028E19F  8B 05 13 89 D3 00               mov eax, dword ptr [rip + 0xd38913]
0028E1A5  A8 40                           test al, 0x40
0028E1A7  0F 84 42 FF FF FF               je 0x14028e0ef
0028E1AD  E8 DE 12 08 00                  call 0x14030f490
0028E1B2  84 C0                           test al, al
0028E1B4  0F 84 35 FF FF FF               je 0x14028e0ef
0028E1BA  8B CB                           mov ecx, ebx
0028E1BC  E8 9F 12 08 00                  call 0x14030f460
0028E1C1  E9 2B FF FF FF                  jmp 0x14028e0f1
0028E1C6  8B 05 EC 88 D3 00               mov eax, dword ptr [rip + 0xd388ec]
0028E1CC  A8 40                           test al, 0x40
0028E1CE  0F 84 3B FF FF FF               je 0x14028e10f
0028E1D4  E8 B7 12 08 00                  call 0x14030f490
0028E1D9  84 C0                           test al, al
0028E1DB  0F 84 2E FF FF FF               je 0x14028e10f
0028E1E1  8B CB                           mov ecx, ebx
0028E1E3  E8 78 12 08 00                  call 0x14030f460
0028E1E8  E9 24 FF FF FF                  jmp 0x14028e111
0028E1ED  8B 05 C5 88 D3 00               mov eax, dword ptr [rip + 0xd388c5]
0028E1F3  A8 40                           test al, 0x40
0028E1F5  0F 84 34 FF FF FF               je 0x14028e12f
0028E1FB  E8 90 12 08 00                  call 0x14030f490
0028E200  84 C0                           test al, al
0028E202  0F 84 27 FF FF FF               je 0x14028e12f
0028E208  8B CF                           mov ecx, edi
0028E20A  E8 51 12 08 00                  call 0x14030f460
0028E20F  E9 1D FF FF FF                  jmp 0x14028e131
0028E214  8B 05 9E 88 D3 00               mov eax, dword ptr [rip + 0xd3889e]
0028E21A  A8 40                           test al, 0x40
0028E21C  0F 84 3A FF FF FF               je 0x14028e15c
0028E222  E8 69 12 08 00                  call 0x14030f490
0028E227  84 C0                           test al, al
0028E229  0F 84 2D FF FF FF               je 0x14028e15c
0028E22F  8B CF                           mov ecx, edi
0028E231  E8 2A 12 08 00                  call 0x14030f460
0028E236  E9 23 FF FF FF                  jmp 0x14028e15e
0028E23B  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0028E23F  E8 24 69 00 00                  call 0x140294b68
0028E244  48 8B 5D D0                     mov rbx, qword ptr [rbp - 0x30]
0028E248  8B F8                           mov edi, eax
0028E24A  E9 6D FC FF FF                  jmp 0x14028debc
0028E24F  48 8B D3                        mov rdx, rbx
0028E252  49 8B CC                        mov rcx, r12
0028E255  E8 52 6C 00 00                  call 0x140294eac
0028E25A  E9 69 FC FF FF                  jmp 0x14028dec8
0028E25F  49 83 E5 FE                     and r13, 0xfffffffffffffffe
0028E263  41 80 7D 00 04                  cmp byte ptr [r13], 4
0028E268  0F 85 D7 FA FF FF               jne 0x14028dd45
0028E26E  BF 82 00 00 00                  mov edi, 0x82
0028E273  E9 DF FA FF FF                  jmp 0x14028dd57
0028E278  33 D2                           xor edx, edx
0028E27A  49 8B CE                        mov rcx, r14
0028E27D  E8 4E 69 0A 00                  call 0x140334bd0
0028E282  48 BE FF FF FF FF FF FF FF 7F   movabs rsi, 0x7fffffffffffffff
0028E28C  F0 49 21 76 18                  lock and qword ptr [r14 + 0x18], rsi
0028E291  45 8B C4                        mov r8d, r12d
0028E294  BA 01 00 00 00                  mov edx, 1
0028E299  48 8B CF                        mov rcx, rdi
0028E29C  E8 87 F6 0D 00                  call 0x14036d928
0028E2A1  E9 66 F9 FF FF                  jmp 0x14028dc0c
0028E2A6  0F B7 15 53 6D D3 00            movzx edx, word ptr [rip + 0xd36d53]
0028E2AD  48 8B 0D 1C F9 B9 00            mov rcx, qword ptr [rip + 0xb9f91c]
0028E2B4  0F AF D3                        imul edx, ebx
0028E2B7  4C 8D 04 91                     lea r8, [rcx + rdx*4]
0028E2BB  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0028E2BF  E9 16 C2 44 00                  jmp 0x1406da4da
0028E2C4  E9 31 C2 44 00                  jmp 0x1406da4fa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMigratePfn(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;
    unsigned __int8 v_stack_pA;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (104);
    v_stack_m58 = v_xmm0;
    v_stack_p10 = *(unsigned __int64 *)(a1);
    if (condition_is_below) goto loc_0028DC0C;
    result = MiGetPfnSlabType(a2, a2, a3, a4);
    if (((unsigned int)(result)) != 9) goto loc_0028DC0C;
    if ((*(unsigned __int16 *)(v_rip + 13857782)) > ((unsigned __int16)(result - 8))) goto loc_0028DC21;
loc_0028DC0C:
loc_0028DC0F:
    v_rsp = (v_rsp) + (104);
    return a2;
loc_0028DC21:
    v_r12 = 0;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(a2 + 32))) != 0) goto loc_0028DC0C;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448)) & (64)) != 0) goto loc_0028DC0C;
    result = MiCanPageMove(a2, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0028DC0C;
    result = MI_NODE_FROM_PFN(a2, a2, a3, a4);
    v_stack_m68 = 0;
    a2 = 0;
    result = MiComputeFaultNode(a1, a2, v_stack_m68, a4);
    result = MiInitializePageColorBase(*(unsigned __int64 *)(a1 + 56), v_r12 + 3, (unsigned int)((unsigned int)(result)), v_stack_m58);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m50)) >> (9));
    v_rbx = (unsigned int)((v_rbx) & (63));
    if (((unsigned int)(v_rbx)) == ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_0028DC0C;
    result = (*(unsigned __int64 *)(a2 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12198901) + result * 8);
    a2 = 0;
    a1 = (v_stack_m50) >> (16);
    a1 = (unsigned int)((a1) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(v_stack_m50)));
    v_r14 = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)(v_stack_m50)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 13857569)))) * ((unsigned int)(v_rbx)));
    v_stack_p8 = *(unsigned __int64 *)(v_rip + 12189439) + a1 * 4 + *(unsigned __int16 *)(v_rip + 13857569) * 4;
loc_0028DCF3:
    if ((*(unsigned __int64 *)(v_rip + 12189439) + a1 * 4) < (*(unsigned __int64 *)(v_rip + 12189439) + a1 * 4 + *(unsigned __int16 *)(v_rip + 13857569) * 4)) goto loc_0028E012;
loc_0028DCFC:
    if (sign_flag) goto loc_0028E057;
loc_0028DD0F:
    result = MiIsPfnCommitNotCharged(a2, *(unsigned __int16 *)(v_rip + 13857569), *(unsigned __int64 *)(v_rip + 12189439) + a1 * 4, v_rip + 12189702);
    if ((unsigned int)(result) != 0) { v_r12 = 5; }
loc_0028DD1D:
    result = MiObtainFaultCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12198901) + result * 8), 1, (unsigned int)((unsigned int)(v_r12)), v_rip + 12189702);
    if (result == 0) goto loc_0028DC0C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) != 0) goto loc_0028E25F;
loc_0028DD45:
    result = MiGetSystemRegionType(v_stack_p10, 1, (unsigned int)((unsigned int)(v_r12)), v_rip + 12189702);
    if (((unsigned int)(result)) == 11) goto loc_0028E26E;
loc_0028DD57:
    result = MiGetPage(v_stack_m78, (unsigned int)((unsigned int)(v_r14)), 2, v_rip + 12189702);
    v_stack_m80 = result;
    if (result == -1) goto loc_0028E291;
    v_r14 = (result + result * 2) << (4);
    v_r14 = (v_r14) + (result);
    v_stack_m60 = v_r14;
    result = MiPageToNode(result, (unsigned int)((unsigned int)(v_r14)), 2, v_rip + 12189702);
    if (((unsigned int)(v_rbx)) != ((unsigned int)(result))) goto loc_0028E2A6;
    v_rsi = 0;
    if (v_stack_p18 == 0) goto loc_0028E16C;
    a2 = 0;
    result = MiGetInPageSupportBlock(v_rsi + 6, a2, 2, v_rip + 12189702);
    v_stack_m88 = result;
    if (result == 0) goto loc_0028E2C4;
loc_0028DDC9:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 32))) >> (16));
    v_rdi = (unsigned int)(((unsigned __int8)(result)) >> (6));
loc_0028DDDE:
    if (condition_is_below) goto loc_0028E0C0;
    result = MiFinalizePageAttribute(v_r14, (unsigned int)((unsigned int)(v_rdi)), 1, v_rip + 12189702);
    result = MiCopyPfnEntryEx(v_r14, 0, 1, v_rip + 12189702);
    result = (*(unsigned __int64 *)(v_r14 + 24)) & (v_r14);
    *(unsigned __int64 *)(v_r14 + 24) = result;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    v_stack_p8 = 1;
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_pA = (unsigned __int8)(result);
    *(unsigned int *)(a2 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    result = (unsigned int)(v_stack_p8);
    if (result != 0) {
        result = *(unsigned int *)(result + 192);
        *(unsigned int *)(result + 192) = (unsigned int)(result);
        result = *(unsigned int *)(v_r14 + 32);
        v_stack_p8 = (unsigned int)(result);
        result = (unsigned int)((result) >> (16));
        result = (unsigned __int8)((result) | (32));
        v_stack_pA = (unsigned __int8)(result);
        result = v_stack_p8;
        *(unsigned int *)(v_r14 + 32) = (unsigned int)(result);
        result = result + 32;
        *(unsigned __int64 *)(v_r14) = result;
        *(unsigned __int64 *)(result + 248) = v_r14;
    }
    v_r12 = (*(unsigned __int64 *)(v_r14 + 8)) | (result);
    result = MI_READ_PTE_LOCK_FREE(v_r12, 0, 1, v_rip + 12189702);
    result = MiUpdateTransitionPteFrame(result, v_stack_m80, 1, v_rip + 12189702);
    v_stack_m70 = result;
    result = MiPteInShadowRange(v_r12, v_stack_m80, 1, v_rip + 12189702);
    if ((unsigned int)(result) != 0) goto loc_0028E23B;
loc_0028DEBC:
    *(unsigned __int64 *)(v_r12) = result;
    if (0 != 0) goto loc_0028E24F;
loc_0028DEC8:
    if (v_stack_p18 == 0) goto loc_0028E13F;
    v_rdi = 0;
loc_0028DEEE:
    if (condition_is_below) goto loc_0028E14D;
    result = MiAddLockedPageCharge(v_stack_p18, 3, 1, v_rip + 12189702);
    result = MiUnlockProtoPoolPage(v_stack_p18, 17, 1, v_rip + 12189702);
    *(unsigned __int64 *)(v_stack_p20) = v_stack_m88;
loc_0028DF29:
    v_r13 = (0) - (v_stack_p20);
    v_r13 = (v_r13) >> (4);
    v_r13 = (v_r13) * (v_stack_p20);
    result = MiCopyPage(v_stack_m80, v_r13, 258, v_rip + 12189702);
    if (v_stack_p18 == 0) goto loc_0028DF92;
    a2 = 0;
    result = MiLockProtoPoolPage(v_r12, a2, 258, v_rip + 12189702);
    v_rdi = 0;
loc_0028DF75:
    if (condition_is_below) goto loc_0028E120;
    result = MiRemoveLockedPageChargeAndDecRef(v_stack_p18, a2, 258, v_rip + 12189702);
loc_0028DF92:
    v_rbx = 0;
loc_0028DF98:
    if (condition_is_below) goto loc_0028E0E0;
    a2 = 0;
    result = MiSetPfnIdentity(0, a2, 258, v_rip + 12189702);
    result = MiInsertPageInFreeOrZeroedList(v_r13, 2, 258, v_rip + 12189702);
    v_rbx = 0;
loc_0028DFCB:
    if (condition_is_below) goto loc_0028E100;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m60 + 32))) >> (16));
    result = (unsigned __int8)((result) & (223));
    v_stack_pA = (unsigned __int8)(result);
    *(unsigned int *)(v_stack_m60 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    *(unsigned __int64 *)(v_stack_m60) = 0;
    result = MiRemoveLockedPageCharge(v_stack_m60, 2, 258, v_rip + 12189702);
    if (v_stack_m88 != 0) goto loc_0028E071;
loc_0028E00A:
    goto loc_0028DC0F;
loc_0028E012:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(258)))) == 0) goto loc_0028DC0C;
    a1 = (v_stack_m88) * ((unsigned int)(*(unsigned int *)(258)));
    if (*(unsigned __int64 *)(a1 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12198901) + result * 8) + 16) * 1 + 3848) != 0) goto loc_0028DCFC;
    if (*(unsigned __int64 *)(a1 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12198901) + result * 8) + 16) * 1 + 3856) != 0) goto loc_0028DCFC;
    a3 = (258) + (4);
    goto loc_0028DCF3;
loc_0028E057:
    if (condition_is_above_or_equal) goto loc_0028DD0F;
    goto loc_0028DD1D;
loc_0028E071:
    *(unsigned int *)(a1 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 192)));
    if (condition_is_above_or_equal) goto loc_0028E00A;
    v_rbx = 0;
    a2 = 0;
    result = MiCapturePfnPageFileInfoInline(v_stack_m60, a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
loc_0028E0C0:
    v_rbx = (unsigned int)((result) + (1));
    if (((*(unsigned int *)(v_rip + 13857251)) & ((unsigned int)(v_rbx))) == 0) goto loc_0028E178;
loc_0028E0CF:
loc_0028E0D1:
    if (!sign_flag) goto loc_0028DDDE;
    goto loc_0028E0C0;
loc_0028E0E0:
    v_rbx = (unsigned int)((v_rbx) + (1));
    if (((*(unsigned int *)(v_rip + 13857219)) & ((unsigned int)(v_rbx))) == 0) goto loc_0028E19F;
loc_0028E0EF:
loc_0028E0F1:
    if (!sign_flag) goto loc_0028DF98;
    goto loc_0028E0E0;
loc_0028E100:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_rbx + 1)));
    if (((*(unsigned int *)(v_rip + 13857187)) & ((unsigned int)(v_rbx))) == 0) goto loc_0028E1C6;
loc_0028E10F:
loc_0028E111:
    if (!sign_flag) goto loc_0028DFCB;
    goto loc_0028E100;
loc_0028E120:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m60 + 32))) + ((unsigned int)(v_stack_m60)));
    if (((*(unsigned int *)(v_rip + 13857155)) & ((unsigned int)(v_rdi))) == 0) goto loc_0028E1ED;
loc_0028E12F:
loc_0028E131:
    if (!sign_flag) goto loc_0028DF75;
    goto loc_0028E120;
loc_0028E13F:
    goto loc_0028DF29;
loc_0028E14D:
    v_rdi = (unsigned int)((v_stack_p18) + ((unsigned int)(v_r13)));
    if (((*(unsigned int *)(v_rip + 13857110)) & ((unsigned int)(v_rdi))) == 0) goto loc_0028E214;
loc_0028E15C:
loc_0028E15E:
    if (!sign_flag) goto loc_0028DEEE;
    goto loc_0028E14D;
loc_0028E16C:
    v_stack_m88 = 0;
    goto loc_0028DDC9;
loc_0028E178:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13863226)))) & (64)) == 0) goto loc_0028E0CF;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m60, a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    if ((unsigned __int8)(result) == 0) goto loc_0028E0CF;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    goto loc_0028E0D1;
loc_0028E19F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13863187)))) & (64)) == 0) goto loc_0028E0EF;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    if ((unsigned __int8)(result) == 0) goto loc_0028E0EF;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    goto loc_0028E0F1;
loc_0028E1C6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13863148)))) & (64)) == 0) goto loc_0028E10F;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    if ((unsigned __int8)(result) == 0) goto loc_0028E10F;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    goto loc_0028E111;
loc_0028E1ED:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13863109)))) & (64)) == 0) goto loc_0028E12F;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    if ((unsigned __int8)(result) == 0) goto loc_0028E12F;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    goto loc_0028E131;
loc_0028E214:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13863070)))) & (64)) == 0) goto loc_0028E15C;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rdi)), a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    if ((unsigned __int8)(result) == 0) goto loc_0028E15C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), a2, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    goto loc_0028E15E;
loc_0028E23B:
    result = MiSanitizeShadowPxe((unsigned int)((unsigned int)(v_rdi)), v_stack_m70, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    goto loc_0028DEBC;
loc_0028E24F:
    result = MiWritePteShadow(1, v_stack_m70, (unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 12189702);
    goto loc_0028DEC8;
loc_0028E25F:
    v_r13 = (0) & (-2);
    if ((*(unsigned __int8 *)(v_r13)) != 4) goto loc_0028DD45;
loc_0028E26E:
    goto loc_0028DD57;
loc_0028E291:
    result = MiReturnFaultCharges(130, 1, 1, v_rip + 12189702);
    goto loc_0028DC0C;
loc_0028E2A6:
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rip + 13856083)) * ((unsigned int)(v_stack_m70)));
loc_0028E2C4:
}
```

## 5. (Beta) C Style

```c
void *MiMigratePfn(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;
    uint8_t v_stack_pA;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (104);
    v_stack_m58 = v_xmm0;
    v_stack_p10 = *(uint64_t *)(arg1);
    if (condition_is_below) goto loc_0028DC0C;
    result = MiGetPfnSlabType(Arg2, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) != 9) goto loc_0028DC0C;
    if ((*(uint16_t *)(v_rip + 0xD373F6)) > ((uint16_t)(result - 8))) goto loc_0028DC21;
loc_0028DC0C:
loc_0028DC0F:
    local_rsp = (local_rsp) + (104);
    return Arg2;
loc_0028DC21:
    local_r12 = 0;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20))) != 0) goto loc_0028DC0C;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8)) & (64)) != 0) goto loc_0028DC0C;
    result = MiCanPageMove(Arg2, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0028DC0C;
    result = MI_NODE_FROM_PFN(Arg2, Arg2, Arg3, Arg4);
    v_stack_m68 = 0;
    Arg2 = 0;
    result = MiComputeFaultNode(Arg1, Arg2, v_stack_m68, Arg4);
    result = MiInitializePageColorBase(*(uint64_t *)(arg1 + 0x38), local_r12 + 3, (uint32_t)((uint32_t)(result)), v_stack_m58);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m50)) >> (9));
    local_rbx = (uint32_t)((local_rbx) & (63));
    if (((uint32_t)(local_rbx)) == ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_0028DC0C;
    result = (*(uint64_t *)(arg2 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBA23F5) + result * 8);
    Arg2 = 0;
    Arg1 = (v_stack_m50) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(v_stack_m50)));
    local_r14 = (uint32_t)(((uint8_t)(Arg2)) ^ ((uint32_t)(v_stack_m50)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xD37321)))) * ((uint32_t)(local_rbx)));
    v_stack_p8 = *(uint64_t *)(v_rip + 0xB9FEFF) + Arg1 * 4 + *(uint16_t *)(v_rip + 0xD37321) * 4;
loc_0028DCF3:
    if ((*(uint64_t *)(v_rip + 0xB9FEFF) + Arg1 * 4) < (*(uint64_t *)(v_rip + 0xB9FEFF) + Arg1 * 4 + *(uint16_t *)(v_rip + 0xD37321) * 4)) goto loc_0028E012;
loc_0028DCFC:
    if (sign_flag) goto loc_0028E057;
loc_0028DD0F:
    result = MiIsPfnCommitNotCharged(Arg2, *(uint16_t *)(v_rip + 0xD37321), *(uint64_t *)(v_rip + 0xB9FEFF) + Arg1 * 4, v_rip + 12189702);
    if ((uint32_t)(result) != 0) { local_r12 = 5; }
loc_0028DD1D:
    result = MiObtainFaultCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA23F5) + result * 8), 1, (uint32_t)((uint32_t)(local_r12)), v_rip + 12189702);
    if (result == 0) goto loc_0028DC0C;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) != 0) goto loc_0028E25F;
loc_0028DD45:
    result = MiGetSystemRegionType(v_stack_p10, 1, (uint32_t)((uint32_t)(local_r12)), v_rip + 12189702);
    if (((uint32_t)(result)) == 11) goto loc_0028E26E;
loc_0028DD57:
    result = MiGetPage(v_stack_m78, (uint32_t)((uint32_t)(local_r14)), 2, v_rip + 12189702);
    v_stack_m80 = result;
    if (result == -1) goto loc_0028E291;
    local_r14 = (result + result * 2) << (4);
    local_r14 = (local_r14) + (result);
    v_stack_m60 = local_r14;
    result = MiPageToNode(result, (uint32_t)((uint32_t)(local_r14)), 2, v_rip + 12189702);
    if (((uint32_t)(local_rbx)) != ((uint32_t)(result))) goto loc_0028E2A6;
    local_rsi = 0;
    if (v_stack_p18 == 0) goto loc_0028E16C;
    Arg2 = 0;
    result = MiGetInPageSupportBlock(local_rsi + 6, Arg2, 2, v_rip + 12189702);
    v_stack_m88 = result;
    if (result == 0) goto loc_0028E2C4;
loc_0028DDC9:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x20))) >> (16));
    local_rdi = (uint32_t)(((uint8_t)(result)) >> (6));
loc_0028DDDE:
    if (condition_is_below) goto loc_0028E0C0;
    result = MiFinalizePageAttribute(local_r14, (uint32_t)((uint32_t)(local_rdi)), 1, v_rip + 12189702);
    result = MiCopyPfnEntryEx(local_r14, 0, 1, v_rip + 12189702);
    result = (*(uint64_t *)(local_r14 + 0x18)) & (local_r14);
    *(uint64_t *)(local_r14 + 0x18) = result;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    v_stack_p8 = 1;
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_pA = (uint8_t)(result);
    *(uint32_t *)(arg2 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    result = (uint32_t)(v_stack_p8);
    if (result != 0) {
        result = *(uint32_t *)(result + 0xC0);
        *(uint32_t *)(result + 0xC0) = (uint32_t)(result);
        result = *(uint32_t *)(local_r14 + 0x20);
        v_stack_p8 = (uint32_t)(result);
        result = (uint32_t)((result) >> (16));
        result = (uint8_t)((result) | (32));
        v_stack_pA = (uint8_t)(result);
        result = v_stack_p8;
        *(uint32_t *)(local_r14 + 0x20) = (uint32_t)(result);
        result = result + 32;
        *(uint64_t *)(local_r14) = result;
        *(uint64_t *)(result + 0xF8) = local_r14;
    }
    local_r12 = (*(uint64_t *)(local_r14 + 0x8)) | (result);
    result = MI_READ_PTE_LOCK_FREE(local_r12, 0, 1, v_rip + 12189702);
    result = MiUpdateTransitionPteFrame(result, v_stack_m80, 1, v_rip + 12189702);
    v_stack_m70 = result;
    result = MiPteInShadowRange(local_r12, v_stack_m80, 1, v_rip + 12189702);
    if ((uint32_t)(result) != 0) goto loc_0028E23B;
loc_0028DEBC:
    *(uint64_t *)(local_r12) = result;
    if (0 != 0) goto loc_0028E24F;
loc_0028DEC8:
    if (v_stack_p18 == 0) goto loc_0028E13F;
    local_rdi = 0;
loc_0028DEEE:
    if (condition_is_below) goto loc_0028E14D;
    result = MiAddLockedPageCharge(v_stack_p18, 3, 1, v_rip + 12189702);
    result = MiUnlockProtoPoolPage(v_stack_p18, 17, 1, v_rip + 12189702);
    *(uint64_t *)(v_stack_p20) = v_stack_m88;
loc_0028DF29:
    local_r13 = (0) - (v_stack_p20);
    local_r13 = (local_r13) >> (4);
    local_r13 = (local_r13) * (v_stack_p20);
    result = MiCopyPage(v_stack_m80, local_r13, 258, v_rip + 12189702);
    if (v_stack_p18 == 0) goto loc_0028DF92;
    Arg2 = 0;
    result = MiLockProtoPoolPage(local_r12, Arg2, 258, v_rip + 12189702);
    local_rdi = 0;
loc_0028DF75:
    if (condition_is_below) goto loc_0028E120;
    result = MiRemoveLockedPageChargeAndDecRef(v_stack_p18, Arg2, 258, v_rip + 12189702);
loc_0028DF92:
    local_rbx = 0;
loc_0028DF98:
    if (condition_is_below) goto loc_0028E0E0;
    Arg2 = 0;
    result = MiSetPfnIdentity(0, Arg2, 258, v_rip + 12189702);
    result = MiInsertPageInFreeOrZeroedList(local_r13, 2, 258, v_rip + 12189702);
    local_rbx = 0;
loc_0028DFCB:
    if (condition_is_below) goto loc_0028E100;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x20))) >> (16));
    result = (uint8_t)((result) & (223));
    v_stack_pA = (uint8_t)(result);
    *(uint32_t *)(v_stack_m60 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    *(uint64_t *)(v_stack_m60) = 0;
    result = MiRemoveLockedPageCharge(v_stack_m60, 2, 258, v_rip + 12189702);
    if (v_stack_m88 != 0) goto loc_0028E071;
loc_0028E00A:
    goto loc_0028DC0F;
loc_0028E012:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(258)))) == 0) goto loc_0028DC0C;
    Arg1 = (v_stack_m88) * ((uint32_t)(*(uint32_t *)(258)));
    if (*(uint64_t *)(arg1 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA23F5) + result * 8) + 0x10) * 1 + 0xF08) != 0) goto loc_0028DCFC;
    if (*(uint64_t *)(arg1 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA23F5) + result * 8) + 0x10) * 1 + 0xF10) != 0) goto loc_0028DCFC;
    Arg3 = (258) + (4);
    goto loc_0028DCF3;
loc_0028E057:
    if (condition_is_above_or_equal) goto loc_0028DD0F;
    goto loc_0028DD1D;
loc_0028E071:
    *(uint32_t *)(arg1 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC0)));
    if (condition_is_above_or_equal) goto loc_0028E00A;
    local_rbx = 0;
    Arg2 = 0;
    result = MiCapturePfnPageFileInfoInline(v_stack_m60, Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
loc_0028E0C0:
    local_rbx = (uint32_t)((result) + (1));
    if (((*(uint32_t *)(v_rip + 0xD371E3)) & ((uint32_t)(local_rbx))) == 0) goto loc_0028E178;
loc_0028E0CF:
loc_0028E0D1:
    if (!sign_flag) goto loc_0028DDDE;
    goto loc_0028E0C0;
loc_0028E0E0:
    local_rbx = (uint32_t)((local_rbx) + (1));
    if (((*(uint32_t *)(v_rip + 0xD371C3)) & ((uint32_t)(local_rbx))) == 0) goto loc_0028E19F;
loc_0028E0EF:
loc_0028E0F1:
    if (!sign_flag) goto loc_0028DF98;
    goto loc_0028E0E0;
loc_0028E100:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_rbx + 1)));
    if (((*(uint32_t *)(v_rip + 0xD371A3)) & ((uint32_t)(local_rbx))) == 0) goto loc_0028E1C6;
loc_0028E10F:
loc_0028E111:
    if (!sign_flag) goto loc_0028DFCB;
    goto loc_0028E100;
loc_0028E120:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x20))) + ((uint32_t)(v_stack_m60)));
    if (((*(uint32_t *)(v_rip + 0xD37183)) & ((uint32_t)(local_rdi))) == 0) goto loc_0028E1ED;
loc_0028E12F:
loc_0028E131:
    if (!sign_flag) goto loc_0028DF75;
    goto loc_0028E120;
loc_0028E13F:
    goto loc_0028DF29;
loc_0028E14D:
    local_rdi = (uint32_t)((v_stack_p18) + ((uint32_t)(local_r13)));
    if (((*(uint32_t *)(v_rip + 0xD37156)) & ((uint32_t)(local_rdi))) == 0) goto loc_0028E214;
loc_0028E15C:
loc_0028E15E:
    if (!sign_flag) goto loc_0028DEEE;
    goto loc_0028E14D;
loc_0028E16C:
    v_stack_m88 = 0;
    goto loc_0028DDC9;
loc_0028E178:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD3893A)))) & (64)) == 0) goto loc_0028E0CF;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m60, Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    if ((uint8_t)(result) == 0) goto loc_0028E0CF;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    goto loc_0028E0D1;
loc_0028E19F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD38913)))) & (64)) == 0) goto loc_0028E0EF;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    if ((uint8_t)(result) == 0) goto loc_0028E0EF;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    goto loc_0028E0F1;
loc_0028E1C6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD388EC)))) & (64)) == 0) goto loc_0028E10F;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    if ((uint8_t)(result) == 0) goto loc_0028E10F;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    goto loc_0028E111;
loc_0028E1ED:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD388C5)))) & (64)) == 0) goto loc_0028E12F;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    if ((uint8_t)(result) == 0) goto loc_0028E12F;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    goto loc_0028E131;
loc_0028E214:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD3889E)))) & (64)) == 0) goto loc_0028E15C;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rdi)), Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    if ((uint8_t)(result) == 0) goto loc_0028E15C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    goto loc_0028E15E;
loc_0028E23B:
    result = MiSanitizeShadowPxe((uint32_t)((uint32_t)(local_rdi)), v_stack_m70, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    goto loc_0028DEBC;
loc_0028E24F:
    result = MiWritePteShadow(1, v_stack_m70, (uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 12189702);
    goto loc_0028DEC8;
loc_0028E25F:
    local_r13 = (0) & (-2);
    if ((*(uint8_t *)(local_r13)) != 4) goto loc_0028DD45;
loc_0028E26E:
    goto loc_0028DD57;
loc_0028E291:
    result = MiReturnFaultCharges(130, 1, 1, v_rip + 12189702);
    goto loc_0028DC0C;
loc_0028E2A6:
    Arg2 = (uint32_t)((*(uint16_t *)(v_rip + 0xD36D53)) * ((uint32_t)(v_stack_m70)));
loc_0028E2C4:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R/W` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `W` |
| `Arg2` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0028DBB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
