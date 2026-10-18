# MiIdealClusterPage

- RVA: `0x004DB964`–`0x004DC169` (길이 `2,053` bytes)
- VA: `0x00000001404DB964`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEA74`
- 디코드: `510`개 명령, `2,053/2,053` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x004DBA60` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x004DBBEC` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x004DBC29` → [MiAcquireNonPagedResources](../28/MiAcquireNonPagedResources_function_00286C60.md) (function, `0x00286C60`)
- `0x004DBC50` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x004DBCC0` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x004DBCFA` → [MiAddLockedPageCharge](../28/MiAddLockedPageCharge_function_0028B550.md) (function, `0x0028B550`)
- `0x004DBD17` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x004DBD28` → [MiCopyPfnEntryRaw](../44/MiCopyPfnEntryRaw_function_00448500.md) (function, `0x00448500`)
- `0x004DBD46` → [MiObtainProtoReference](../31/MiObtainProtoReference_function_00318178.md) (function, `0x00318178`)
- `0x004DBD52` → [MiCopyPfnEntryRaw](../44/MiCopyPfnEntryRaw_function_00448500.md) (function, `0x00448500`)
- `0x004DBD5C` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x004DBD70` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x004DBDA2` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x004DBDB7` → [MiProtectionToCacheAttribute](../2B/MiProtectionToCacheAttribute_function_002B8530.md) (function, `0x002B8530`)
- `0x004DBDED` → [MiGetLargePage](../31/MiGetLargePage_function_0031E210.md) (function, `0x0031E210`)
- `0x004DBE09` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x004DBE1E` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x004DBE31` → [MiConvertLargeActivePageToChain](../31/MiConvertLargeActivePageToChain_function_0031D980.md) (function, `0x0031D980`)
- `0x004DBE8F` → [MiArePageContentsZero](MiArePageContentsZero_function_004D4278.md) (function, `0x004D4278`)
- `0x004DBEAE` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x004DBEDF` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x004DBF88` → [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) (function, `0x0028BDE0`)
- `0x004DBF9E` → [MiRelockFaultState](../36/MiRelockFaultState_function_0036A230.md) (function, `0x0036A230`)
- `0x004DBFC2` → [MiRelockProtoPoolPage](../31/MiRelockProtoPoolPage_function_0031826C.md) (function, `0x0031826C`)
- `0x004DBFDA` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x004DBFF7` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x004DC01B` → [MiReturnPfnReferenceCountAtDpc](../36/MiReturnPfnReferenceCountAtDpc_function_00364010.md) (function, `0x00364010`)
- `0x004DC034` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x004DC055` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x004DC079` → [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) (function, `0x00334B50`)
- `0x004DC086` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x004DC0A0` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x004DC0D9` → [MiIsFaultPteIntact](../32/MiIsFaultPteIntact_function_003288A0.md) (function, `0x003288A0`)
- `0x004DC0EE` → [MiRemoveLockedPageCharge](../24/MiRemoveLockedPageCharge_function_00246950.md) (function, `0x00246950`)
- `0x004DC111` → [MiCopyPage](../2B/MiCopyPage_function_002B1B30.md) (function, `0x002B1B30`)
- `0x004DC11F` → [MiSwapHardFaultPage](../38/MiSwapHardFaultPage_function_00385F34.md) (function, `0x00385F34`)
- `0x004DC146` → [MiReturnResident](../28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x004DC15D` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)

### Direct callers
- [sub_00283AFC](../28/Unknown_function_00283AFC.md) at `0x00283CF6`

### Static image references
- `0x004DB980` → RVA `0x00E0A740` (`.data`; read)
- `0x004DBB39` → RVA `0x00E30088` (`.data`; read)
- `0x004DBC6F` → RVA `0x00E2DCE0` (`.data`; read)
- `0x004DBD93` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x004DBE6C` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x004DBE76` → RVA `0x00E30270` (`.data`; read)
- `0x004DBE7E` → RVA `0x00FC5054` (`ALMOSTRO`; reference)
- `0x004DBE84` → RVA `0x00E30270` (`.data`; write)
- `0x004DBF2A` → RVA `0x00FC6ED0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004DB964  40 55                           push rbp
004DB966  53                              push rbx
004DB967  56                              push rsi
004DB968  57                              push rdi
004DB969  41 54                           push r12
004DB96B  41 55                           push r13
004DB96D  41 56                           push r14
004DB96F  41 57                           push r15
004DB971  48 8D AC 24 08 FF FF FF         lea rbp, [rsp - 0xf8]
004DB979  48 81 EC F8 01 00 00            sub rsp, 0x1f8
004DB980  48 8B 05 B9 ED 92 00            mov rax, qword ptr [rip + 0x92edb9]
004DB987  48 33 C4                        xor rax, rsp
004DB98A  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
004DB991  4C 8B 9D 70 01 00 00            mov r11, qword ptr [rbp + 0x170]
004DB998  45 33 FF                        xor r15d, r15d
004DB99B  48 8B BD 60 01 00 00            mov rdi, qword ptr [rbp + 0x160]
004DB9A2  0F 57 C0                        xorps xmm0, xmm0
004DB9A5  4C 8B AD 68 01 00 00            mov r13, qword ptr [rbp + 0x168]
004DB9AC  4C 8B D2                        mov r10, rdx
004DB9AF  0F 57 C9                        xorps xmm1, xmm1
004DB9B2  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
004DB9B6  48 8B D1                        mov rdx, rcx
004DB9B9  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
004DB9BD  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
004DB9C1  49 C7 C4 00 F0 FF FF            mov r12, 0xfffffffffffff000
004DB9C8  49 8B F0                        mov rsi, r8
004DB9CB  4C 89 45 D8                     mov qword ptr [rbp - 0x28], r8
004DB9CF  4C 89 4D A8                     mov qword ptr [rbp - 0x58], r9
004DB9D3  49 B8 00 00 00 00 00 00 00 80   movabs r8, 0x8000000000000000
004DB9DD  44 8B 72 50                     mov r14d, dword ptr [rdx + 0x50]
004DB9E1  48 8B 12                        mov rdx, qword ptr [rdx]
004DB9E4  48 8B C2                        mov rax, rdx
004DB9E7  41 C1 EE 08                     shr r14d, 8
004DB9EB  48 25 00 00 FF FF               and rax, 0xffffffffffff0000
004DB9F1  45 88 3B                        mov byte ptr [r11], r15b
004DB9F4  48 8B DA                        mov rbx, rdx
004DB9F7  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
004DB9FB  49 23 DC                        and rbx, r12
004DB9FE  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
004DBA02  48 2B D8                        sub rbx, rax
004DBA05  4C 89 5D B8                     mov qword ptr [rbp - 0x48], r11
004DBA09  48 C1 EB 0C                     shr rbx, 0xc
004DBA0D  41 F7 42 30 00 00 20 00         test dword ptr [r10 + 0x30], 0x200000
004DBA15  44 88 7C 24 70                  mov byte ptr [rsp + 0x70], r15b
004DBA1A  4C 89 7D B0                     mov qword ptr [rbp - 0x50], r15
004DBA1E  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
004DBA22  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
004DBA26  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
004DBA2A  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
004DBA2E  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
004DBA33  0F 11 45 48                     movups xmmword ptr [rbp + 0x48], xmm0
004DBA37  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
004DBA3B  0F 11 4D F8                     movups xmmword ptr [rbp - 8], xmm1
004DBA3F  0F 11 4D 08                     movups xmmword ptr [rbp + 8], xmm1
004DBA43  0F 11 4D 18                     movups xmmword ptr [rbp + 0x18], xmm1
004DBA47  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
004DBA4B  0F 85 AC 00 00 00               jne 0x1404dbafd
004DBA51  48 C1 EA 0C                     shr rdx, 0xc
004DBA55  4C 8D 4D B0                     lea r9, [rbp - 0x50]
004DBA59  45 8D 47 0C                     lea r8d, [r15 + 0xc]
004DBA5D  49 8B CA                        mov rcx, r10
004DBA60  E8 0B 2F E5 FF                  call 0x14032e970
004DBA65  48 85 C0                        test rax, rax
004DBA68  0F 84 71 01 00 00               je 0x1404dbbdf
004DBA6E  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
004DBA72  4D 85 C0                        test r8, r8
004DBA75  0F 84 64 01 00 00               je 0x1404dbbdf
004DBA7B  48 3B C6                        cmp rax, rsi
004DBA7E  0F 85 5B 01 00 00               jne 0x1404dbbdf
004DBA84  41 8B 48 34                     mov ecx, dword ptr [r8 + 0x34]
004DBA88  4D 8B 48 08                     mov r9, qword ptr [r8 + 8]
004DBA8C  81 E1 FF FF FF 3F               and ecx, 0x3fffffff
004DBA92  41 8B 40 2C                     mov eax, dword ptr [r8 + 0x2c]
004DBA96  48 2B C1                        sub rax, rcx
004DBA99  49 8D 0C C1                     lea rcx, [r9 + rax*8]
004DBA9D  48 8B C6                        mov rax, rsi
004DBAA0  49 23 C4                        and rax, r12
004DBAA3  49 3B C1                        cmp rax, r9
004DBAA6  4C 0F 47 C8                     cmova r9, rax
004DBAAA  48 05 00 10 00 00               add rax, 0x1000
004DBAB0  48 3B C8                        cmp rcx, rax
004DBAB3  48 0F 47 C8                     cmova rcx, rax
004DBAB7  4C 3B C9                        cmp r9, rcx
004DBABA  0F 83 1F 01 00 00               jae 0x1404dbbdf
004DBAC0  48 8D 14 DD 00 00 00 00         lea rdx, [rbx*8]
004DBAC8  48 8B C6                        mov rax, rsi
004DBACB  48 2B C2                        sub rax, rdx
004DBACE  49 3B C1                        cmp rax, r9
004DBAD1  0F 82 08 01 00 00               jb 0x1404dbbdf
004DBAD7  48 8B C6                        mov rax, rsi
004DBADA  48 2B C2                        sub rax, rdx
004DBADD  48 83 E8 80                     sub rax, -0x80
004DBAE1  48 3B C1                        cmp rax, rcx
004DBAE4  0F 87 F5 00 00 00               ja 0x1404dbbdf
004DBAEA  49 8B 00                        mov rax, qword ptr [r8]
004DBAED  4C 8B 5D B8                     mov r11, qword ptr [rbp - 0x48]
004DBAF1  0F B7 48 3C                     movzx ecx, word ptr [rax + 0x3c]
004DBAF5  81 E1 FF 03 00 00               and ecx, 0x3ff
004DBAFB  EB 3C                           jmp 0x1404dbb39
004DBAFD  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
004DBB01  49 0B C0                        or rax, r8
004DBB04  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
004DBB0E  48 3B C2                        cmp rax, rdx
004DBB11  0F 82 C8 00 00 00               jb 0x1404dbbdf
004DBB17  48 BA FF FF FF FF FF F6 FF FF   movabs rdx, 0xfffff6ffffffffff
004DBB21  48 3B C2                        cmp rax, rdx
004DBB24  0F 87 B5 00 00 00               ja 0x1404dbbdf
004DBB2A  0F B7 89 AE 00 00 00            movzx ecx, word ptr [rcx + 0xae]
004DBB31  48 8D 14 DD 00 00 00 00         lea rdx, [rbx*8]
004DBB39  48 8B 05 48 45 95 00            mov rax, qword ptr [rip + 0x954548]
004DBB40  41 B9 10 00 00 00               mov r9d, 0x10
004DBB46  45 8B C1                        mov r8d, r9d
004DBB49  4C 8B 14 C8                     mov r10, qword ptr [rax + rcx*8]
004DBB4D  45 8D 61 F1                     lea r12d, [r9 - 0xf]
004DBB51  48 8B CE                        mov rcx, rsi
004DBB54  4C 89 55 88                     mov qword ptr [rbp - 0x78], r10
004DBB58  48 2B CA                        sub rcx, rdx
004DBB5B  48 8D 45 60                     lea rax, [rbp + 0x60]
004DBB5F  48 2B C8                        sub rcx, rax
004DBB62  48 8D 55 60                     lea rdx, [rbp + 0x60]
004DBB66  48 8B 04 11                     mov rax, qword ptr [rcx + rdx]
004DBB6A  48 89 02                        mov qword ptr [rdx], rax
004DBB6D  48 8D 52 08                     lea rdx, [rdx + 8]
004DBB71  4D 2B C4                        sub r8, r12
004DBB74  75 F0                           jne 0x1404dbb66
004DBB76  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004DBB80  48 8B C0                        mov rax, rax
004DBB83  4C 8B C7                        mov r8, rdi
004DBB86  41 8B CF                        mov ecx, r15d
004DBB89  4C 2B C0                        sub r8, rax
004DBB8C  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
004DBB96  49 C1 F8 04                     sar r8, 4
004DBB9A  4C 0F AF C0                     imul r8, rax
004DBB9E  48 83 CE FF                     or rsi, 0xffffffffffffffff
004DBBA2  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
004DBBA6  8B D1                           mov edx, ecx
004DBBA8  41 3B C9                        cmp ecx, r9d
004DBBAB  73 59                           jae 0x1404dbc06
004DBBAD  48 8B 44 D5 60                  mov rax, qword ptr [rbp + rdx*8 + 0x60]
004DBBB2  41 84 C4                        test r12b, al
004DBBB5  75 05                           jne 0x1404dbbbc
004DBBB7  41 03 CC                        add ecx, r12d
004DBBBA  EB EA                           jmp 0x1404dbba6
004DBBBC  48 8B F0                        mov rsi, rax
004DBBBF  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
004DBBC9  48 C1 EE 0C                     shr rsi, 0xc
004DBBCD  48 23 F0                        and rsi, rax
004DBBD0  48 8B C6                        mov rax, rsi
004DBBD3  83 E0 0F                        and eax, 0xf
004DBBD6  48 3B C2                        cmp rax, rdx
004DBBD9  0F 84 87 00 00 00               je 0x1404dbc66
004DBBDF  48 8B C7                        mov rax, rdi
004DBBE2  48 8B 8D E0 00 00 00            mov rcx, qword ptr [rbp + 0xe0]
004DBBE9  48 33 CC                        xor rcx, rsp
004DBBEC  E8 4F 0A 1D 00                  call 0x1406ac640
004DBBF1  48 81 C4 F8 01 00 00            add rsp, 0x1f8
004DBBF8  41 5F                           pop r15
004DBBFA  41 5E                           pop r14
004DBBFC  41 5D                           pop r13
004DBBFE  41 5C                           pop r12
004DBC00  5F                              pop rdi
004DBC01  5E                              pop rsi
004DBC02  5B                              pop rbx
004DBC03  5D                              pop rbp
004DBC04  C3                              ret
004DBC05  CC                              int3
004DBC06  4D 8B E7                        mov r12, r15
004DBC09  75 55                           jne 0x1404dbc60
004DBC0B  49 8B C0                        mov rax, r8
004DBC0E  83 E0 0F                        and eax, 0xf
004DBC11  48 3B C3                        cmp rax, rbx
004DBC14  0F 84 9A 00 00 00               je 0x1404dbcb4
004DBC1A  45 33 C9                        xor r9d, r9d
004DBC1D  45 33 C0                        xor r8d, r8d
004DBC20  49 8B CA                        mov rcx, r10
004DBC23  41 8D 59 01                     lea ebx, [r9 + 1]
004DBC27  8B D3                           mov edx, ebx
004DBC29  E8 32 B0 DA FF                  call 0x140286c60
004DBC2E  85 C0                           test eax, eax
004DBC30  78 AD                           js 0x1404dbbdf
004DBC32  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
004DBC36  4C 8D 4D E8                     lea r9, [rbp - 0x18]
004DBC3A  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
004DBC3E  8D 53 02                        lea edx, [rbx + 2]
004DBC41  44 8A FB                        mov r15b, bl
004DBC44  45 8B 40 30                     mov r8d, dword ptr [r8 + 0x30]
004DBC48  41 C1 E8 0C                     shr r8d, 0xc
004DBC4C  41 83 E0 7F                     and r8d, 0x7f
004DBC50  E8 BB 47 E4 FF                  call 0x140320410
004DBC55  8B 5D F0                        mov ebx, dword ptr [rbp - 0x10]
004DBC58  C1 EB 09                        shr ebx, 9
004DBC5B  83 E3 3F                        and ebx, 0x3f
004DBC5E  EB 67                           jmp 0x1404dbcc7
004DBC60  41 BC 01 00 00 00               mov r12d, 1
004DBC66  48 8B C3                        mov rax, rbx
004DBC69  48 2B C2                        sub rax, rdx
004DBC6C  48 03 F0                        add rsi, rax
004DBC6F  48 3B 35 6A 20 95 00            cmp rsi, qword ptr [rip + 0x95206a]
004DBC76  0F 87 63 FF FF FF               ja 0x1404dbbdf
004DBC7C  48 8D 14 76                     lea rdx, [rsi + rsi*2]
004DBC80  48 03 D2                        add rdx, rdx
004DBC83  48 B9 28 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000028
004DBC8D  48 8B 0C D1                     mov rcx, qword ptr [rcx + rdx*8]
004DBC91  48 C1 E9 36                     shr rcx, 0x36
004DBC95  41 85 CC                        test r12d, ecx
004DBC98  0F 84 41 FF FF FF               je 0x1404dbbdf
004DBC9E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004DBCA8  48 8B C8                        mov rcx, rax
004DBCAB  4C 8D 24 D1                     lea r12, [rcx + rdx*8]
004DBCAF  4C 3B E7                        cmp r12, rdi
004DBCB2  75 09                           jne 0x1404dbcbd
004DBCB4  41 C6 03 01                     mov byte ptr [r11], 1
004DBCB8  E9 22 FF FF FF                  jmp 0x1404dbbdf
004DBCBD  48 8B CE                        mov rcx, rsi
004DBCC0  E8 0B D0 E5 FF                  call 0x140338cd0
004DBCC5  8B D8                           mov ebx, eax
004DBCC7  8B C3                           mov eax, ebx
004DBCC9  33 D2                           xor edx, edx
004DBCCB  48 69 C8 80 DF 00 00            imul rcx, rax, 0xdf80
004DBCD2  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
004DBCD6  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
004DBCDA  C6 84 01 43 14 00 00 01         mov byte ptr [rcx + rax + 0x1443], 1
004DBCE2  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
004DBCEC  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
004DBCF0  48 23 C8                        and rcx, rax
004DBCF3  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
004DBCF7  48 8B CF                        mov rcx, rdi
004DBCFA  E8 51 F8 DA FF                  call 0x14028b550
004DBCFF  85 C0                           test eax, eax
004DBD01  75 1E                           jne 0x1404dbd21
004DBD03  B8 01 00 00 00                  mov eax, 1
004DBD08  44 3A F8                        cmp r15b, al
004DBD0B  0F 85 CE FE FF FF               jne 0x1404dbbdf
004DBD11  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
004DBD15  8B D0                           mov edx, eax
004DBD17  E8 80 6C E4 FF                  call 0x14032299c
004DBD1C  E9 BE FE FF FF                  jmp 0x1404dbbdf
004DBD21  48 8B D7                        mov rdx, rdi
004DBD24  48 8D 4D 28                     lea rcx, [rbp + 0x28]
004DBD28  E8 D3 C7 F6 FF                  call 0x140448500
004DBD2D  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
004DBD37  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
004DBD3C  4D 85 ED                        test r13, r13
004DBD3F  74 20                           je 0x1404dbd61
004DBD41  33 D2                           xor edx, edx
004DBD43  49 8B CD                        mov rcx, r13
004DBD46  E8 2D C4 E3 FF                  call 0x140318178
004DBD4B  49 8B D5                        mov rdx, r13
004DBD4E  48 8D 4D F8                     lea rcx, [rbp - 8]
004DBD52  E8 A9 C7 F6 FF                  call 0x140448500
004DBD57  B2 11                           mov dl, 0x11
004DBD59  49 8B CD                        mov rcx, r13
004DBD5C  E8 2F A3 D6 FF                  call 0x140246090
004DBD61  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
004DBD65  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
004DBD6A  48 83 C1 38                     add rcx, 0x38
004DBD6E  B2 01                           mov dl, 1
004DBD70  E8 1B 15 DA FF                  call 0x14027d290
004DBD75  BA 01 00 00 00                  mov edx, 1
004DBD7A  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
004DBD7E  44 3A FA                        cmp r15b, dl
004DBD81  0F 85 71 01 00 00               jne 0x1404dbef8
004DBD87  45 0F 20 C6                     mov r14, cr8
004DBD8B  44 8D 7A 01                     lea r15d, [rdx + 1]
004DBD8F  45 0F 22 C7                     mov cr8, r15
004DBD93  83 3D 86 AF AE 00 00            cmp dword ptr [rip + 0xaeaf86], 0
004DBD9A  74 0B                           je 0x1404dbda7
004DBD9C  41 8A D7                        mov dl, r15b
004DBD9F  41 8A CE                        mov cl, r14b
004DBDA2  E8 55 99 01 00                  call 0x1404f56fc
004DBDA7  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
004DBDAB  48 C1 E9 05                     shr rcx, 5
004DBDAF  83 E1 1F                        and ecx, 0x1f
004DBDB2  44 88 74 24 70                  mov byte ptr [rsp + 0x70], r14b
004DBDB7  E8 74 C7 DD FF                  call 0x1402b8530
004DBDBC  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
004DBDC2  45 8B C7                        mov r8d, r15d
004DBDC5  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
004DBDC9  44 8B CB                        mov r9d, ebx
004DBDCC  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
004DBDD0  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
004DBDD5  48 8B 49 60                     mov rcx, qword ptr [rcx + 0x60]
004DBDD9  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
004DBDDE  49 8B CF                        mov rcx, r15
004DBDE1  C7 44 24 28 12 00 00 00         mov dword ptr [rsp + 0x28], 0x12
004DBDE9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
004DBDED  E8 1E 24 E4 FF                  call 0x14031e210
004DBDF2  48 8B D8                        mov rbx, rax
004DBDF5  48 85 C0                        test rax, rax
004DBDF8  75 34                           jne 0x1404dbe2e
004DBDFA  39 05 20 AF AE 00               cmp dword ptr [rip + 0xaeaf20], eax
004DBE00  74 0C                           je 0x1404dbe0e
004DBE02  44 0F 20 C1                     mov rcx, cr8
004DBE06  41 8A D6                        mov dl, r14b
004DBE09  E8 8A 98 01 00                  call 0x1404f5698
004DBE0E  41 0F B6 C6                     movzx eax, r14b
004DBE12  44 0F 22 C0                     mov cr8, rax
004DBE16  BA 01 00 00 00                  mov edx, 1
004DBE1B  49 8B CF                        mov rcx, r15
004DBE1E  E8 79 6B E4 FF                  call 0x14032299c
004DBE23  41 BE 17 00 00 C0               mov r14d, 0xc0000017
004DBE29  E9 62 01 00 00                  jmp 0x1404dbf90
004DBE2E  48 8B CB                        mov rcx, rbx
004DBE31  E8 4A 1B E4 FF                  call 0x14031d980
004DBE36  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
004DBE40  48 8B C1                        mov rax, rcx
004DBE43  4C 8B 7D C0                     mov r15, qword ptr [rbp - 0x40]
004DBE47  48 8B CB                        mov rcx, rbx
004DBE4A  48 2B C8                        sub rcx, rax
004DBE4D  BF 01 00 00 00                  mov edi, 1
004DBE52  48 C1 F9 04                     sar rcx, 4
004DBE56  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
004DBE60  48 0F AF C8                     imul rcx, rax
004DBE64  44 8D 6F 0F                     lea r13d, [rdi + 0xf]
004DBE68  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
004DBE6C  8A 05 16 AC AE 00               mov al, byte ptr [rip + 0xaeac16]
004DBE72  84 C0                           test al, al
004DBE74  79 22                           jns 0x1404dbe98
004DBE76  8B 05 F4 43 95 00               mov eax, dword ptr [rip + 0x9543f4]
004DBE7C  03 C7                           add eax, edi
004DBE7E  85 05 D0 91 AE 00               test dword ptr [rip + 0xae91d0], eax
004DBE84  89 05 E6 43 95 00               mov dword ptr [rip + 0x9543e6], eax
004DBE8A  75 0C                           jne 0x1404dbe98
004DBE8C  48 8B D7                        mov rdx, rdi
004DBE8F  E8 E4 83 FF FF                  call 0x1404d4278
004DBE94  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
004DBE98  48 8B C1                        mov rax, rcx
004DBE9B  83 E0 0F                        and eax, 0xf
004DBE9E  49 3B C7                        cmp rax, r15
004DBEA1  75 08                           jne 0x1404dbeab
004DBEA3  48 8B F1                        mov rsi, rcx
004DBEA6  4C 8B E3                        mov r12, rbx
004DBEA9  EB 0C                           jmp 0x1404dbeb7
004DBEAB  48 8B CB                        mov rcx, rbx
004DBEAE  E8 9D 8C E5 FF                  call 0x140334b50
004DBEB3  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
004DBEB7  48 03 CF                        add rcx, rdi
004DBEBA  48 83 C3 30                     add rbx, 0x30
004DBEBE  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
004DBEC2  4C 2B EF                        sub r13, rdi
004DBEC5  75 A5                           jne 0x1404dbe6c
004DBEC7  44 39 2D 52 AE AE 00            cmp dword ptr [rip + 0xaeae52], r13d
004DBECE  4C 8B 6D D0                     mov r13, qword ptr [rbp - 0x30]
004DBED2  48 8B 7D C8                     mov rdi, qword ptr [rbp - 0x38]
004DBED6  74 0C                           je 0x1404dbee4
004DBED8  44 0F 20 C1                     mov rcx, cr8
004DBEDC  41 8A D6                        mov dl, r14b
004DBEDF  E8 B4 97 01 00                  call 0x1404f5698
004DBEE4  41 0F B6 C6                     movzx eax, r14b
004DBEE8  44 0F 22 C0                     mov cr8, rax
004DBEEC  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
004DBEF0  45 33 F6                        xor r14d, r14d
004DBEF3  E9 98 00 00 00                  jmp 0x1404dbf90
004DBEF8  4C 8D 24 76                     lea r12, [rsi + rsi*2]
004DBEFC  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004DBF06  49 C1 E4 04                     shl r12, 4
004DBF0A  48 8B C0                        mov rax, rax
004DBF0D  41 F7 D6                        not r14d
004DBF10  4C 03 E0                        add r12, rax
004DBF13  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004DBF1C  44 23 F2                        and r14d, edx
004DBF1F  41 81 C6 40 20 00 00            add r14d, 0x2040
004DBF26  41 C1 E6 11                     shl r14d, 0x11
004DBF2A  48 3B 05 9F AF AE 00            cmp rax, qword ptr [rip + 0xaeaf9f]
004DBF31  75 04                           jne 0x1404dbf37
004DBF33  41 83 CE 08                     or r14d, 8
004DBF37  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
004DBF3A  45 33 C9                        xor r9d, r9d
004DBF3D  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
004DBF41  4C 8B C6                        mov r8, rsi
004DBF44  C1 E8 10                        shr eax, 0x10
004DBF47  0F B6 C8                        movzx ecx, al
004DBF4A  48 8D 45 90                     lea rax, [rbp - 0x70]
004DBF4E  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004DBF53  33 C0                           xor eax, eax
004DBF55  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
004DBF5A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004DBF5F  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
004DBF63  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
004DBF68  C6 44 24 40 FF                  mov byte ptr [rsp + 0x40], 0xff
004DBF6D  C1 E9 06                        shr ecx, 6
004DBF70  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
004DBF74  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
004DBF78  49 8B CF                        mov rcx, r15
004DBF7B  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
004DBF80  48 8B D6                        mov rdx, rsi
004DBF83  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004DBF88  E8 53 FE DA FF                  call 0x14028bde0
004DBF8D  44 8B F0                        mov r14d, eax
004DBF90  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
004DBF94  32 DB                           xor bl, bl
004DBF96  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
004DBF9A  48 83 C1 38                     add rcx, 0x38
004DBF9E  E8 8D E2 E8 FF                  call 0x14036a230
004DBFA3  4D 85 ED                        test r13, r13
004DBFA6  74 78                           je 0x1404dc020
004DBFA8  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
004DBFAC  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
004DBFB6  48 0B C8                        or rcx, rax
004DBFB9  33 D2                           xor edx, edx
004DBFBB  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
004DBFBF  49 8B CD                        mov rcx, r13
004DBFC2  E8 A5 C2 E3 FF                  call 0x14031826c
004DBFC7  83 64 24 78 00                  and dword ptr [rsp + 0x78], 0
004DBFCC  F0 49 0F BA 6D 18 3F            lock bts qword ptr [r13 + 0x18], 0x3f
004DBFD3  73 15                           jae 0x1404dbfea
004DBFD5  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
004DBFDA  E8 21 FD F1 FF                  call 0x1403fbd00
004DBFDF  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
004DBFE3  48 85 C0                        test rax, rax
004DBFE6  78 ED                           js 0x1404dbfd5
004DBFE8  EB E2                           jmp 0x1404dbfcc
004DBFEA  41 B8 30 00 00 00               mov r8d, 0x30
004DBFF0  48 8D 4D F8                     lea rcx, [rbp - 8]
004DBFF4  49 8B D5                        mov rdx, r13
004DBFF7  E8 14 AB 1E 00                  call 0x1406c6b10
004DBFFC  85 C0                           test eax, eax
004DBFFE  0F B6 DB                        movzx ebx, bl
004DC001  B8 01 00 00 00                  mov eax, 1
004DC006  0F 45 D8                        cmovne ebx, eax
004DC009  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
004DC013  F0 49 21 45 18                  lock and qword ptr [r13 + 0x18], rax
004DC018  49 8B CD                        mov rcx, r13
004DC01B  E8 F0 7F E8 FF                  call 0x140364010
004DC020  45 33 ED                        xor r13d, r13d
004DC023  44 89 6D A0                     mov dword ptr [rbp - 0x60], r13d
004DC027  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
004DC02E  73 14                           jae 0x1404dc044
004DC030  48 8D 4D A0                     lea rcx, [rbp - 0x60]
004DC034  E8 C7 FC F1 FF                  call 0x1403fbd00
004DC039  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
004DC03D  48 85 C0                        test rax, rax
004DC040  78 EE                           js 0x1404dc030
004DC042  EB E3                           jmp 0x1404dc027
004DC044  84 DB                           test bl, bl
004DC046  75 68                           jne 0x1404dc0b0
004DC048  41 B8 30 00 00 00               mov r8d, 0x30
004DC04E  48 8D 4D 28                     lea rcx, [rbp + 0x28]
004DC052  48 8B D7                        mov rdx, rdi
004DC055  E8 B6 AA 1E 00                  call 0x1406c6b10
004DC05A  85 C0                           test eax, eax
004DC05C  74 5B                           je 0x1404dc0b9
004DC05E  45 85 F6                        test r14d, r14d
004DC061  0F 88 F3 00 00 00               js 0x1404dc15a
004DC067  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
004DC071  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
004DC076  49 8B CC                        mov rcx, r12
004DC079  E8 D2 8A E5 FF                  call 0x140334b50
004DC07E  BA 01 00 00 00                  mov edx, 1
004DC083  49 8B CF                        mov rcx, r15
004DC086  E8 11 69 E4 FF                  call 0x14032299c
004DC08B  44 89 6D 80                     mov dword ptr [rbp - 0x80], r13d
004DC08F  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
004DC096  0F 83 BE 00 00 00               jae 0x1404dc15a
004DC09C  48 8D 4D 80                     lea rcx, [rbp - 0x80]
004DC0A0  E8 5B FC F1 FF                  call 0x1403fbd00
004DC0A5  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
004DC0A9  48 85 C0                        test rax, rax
004DC0AC  78 EE                           js 0x1404dc09c
004DC0AE  EB DF                           jmp 0x1404dc08f
004DC0B0  B8 01 00 00 00                  mov eax, 1
004DC0B5  3A D8                           cmp bl, al
004DC0B7  74 A5                           je 0x1404dc05e
004DC0B9  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
004DC0BD  48 0F BA E0 3E                  bt rax, 0x3e
004DC0C2  72 9A                           jb 0x1404dc05e
004DC0C4  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
004DC0C8  4C 8D 4D A8                     lea r9, [rbp - 0x58]
004DC0CC  48 8B 5D D8                     mov rbx, qword ptr [rbp - 0x28]
004DC0D0  48 8B C8                        mov rcx, rax
004DC0D3  4C 8B C3                        mov r8, rbx
004DC0D6  48 8B 10                        mov rdx, qword ptr [rax]
004DC0D9  E8 C2 C7 E4 FF                  call 0x1403288a0
004DC0DE  85 C0                           test eax, eax
004DC0E0  0F 84 78 FF FF FF               je 0x1404dc05e
004DC0E6  45 85 F6                        test r14d, r14d
004DC0E9  79 0D                           jns 0x1404dc0f8
004DC0EB  48 8B CF                        mov rcx, rdi
004DC0EE  E8 5D A8 D6 FF                  call 0x140246950
004DC0F3  E9 E7 FA FF FF                  jmp 0x1404dbbdf
004DC0F8  8A 45 A8                        mov al, byte ptr [rbp - 0x58]
004DC0FB  48 8B CE                        mov rcx, rsi
004DC0FE  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
004DC102  24 40                           and al, 0x40
004DC104  F6 D8                           neg al
004DC106  45 1B C0                        sbb r8d, r8d
004DC109  41 83 E0 08                     and r8d, 8
004DC10D  41 83 C0 0C                     add r8d, 0xc
004DC111  E8 1A 5A DD FF                  call 0x1402b1b30
004DC116  4D 8B C4                        mov r8, r12
004DC119  48 8B D7                        mov rdx, rdi
004DC11C  48 8B CB                        mov rcx, rbx
004DC11F  E8 10 9E EA FF                  call 0x140385f34
004DC124  41 8B 4C 24 20                  mov ecx, dword ptr [r12 + 0x20]
004DC129  BB 01 00 00 00                  mov ebx, 1
004DC12E  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
004DC132  8B D3                           mov edx, ebx
004DC134  66 44 89 6C 24 78               mov word ptr [rsp + 0x78], r13w
004DC13A  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
004DC13E  41 89 4C 24 20                  mov dword ptr [r12 + 0x20], ecx
004DC143  49 8B CF                        mov rcx, r15
004DC146  E8 45 A7 DA FF                  call 0x140286890
004DC14B  4C 8B 5D B8                     mov r11, qword ptr [rbp - 0x48]
004DC14F  49 8B C4                        mov rax, r12
004DC152  41 88 1B                        mov byte ptr [r11], bl
004DC155  E9 88 FA FF FF                  jmp 0x1404dbbe2
004DC15A  48 8B CF                        mov rcx, rdi
004DC15D  E8 6E 98 D6 FF                  call 0x1402459d0
004DC162  33 C0                           xor eax, eax
004DC164  E9 79 FA FF FF                  jmp 0x1404dbbe2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiIdealClusterPage(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (504);
    result = (*(unsigned __int64 *)(v_rip + 9629113)) ^ (v_rsp);
    v_stack_m58 = result;
    v_r15 = 0;
    v_stack_m1A0 = a2;
    v_stack_m1B8 = a1;
    v_stack_m160 = a3;
    v_stack_m190 = a4;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) >> (8));
    result = (*(unsigned __int64 *)(a1)) & (0xFFFFFFFFFFFF0000ULL);
    *(unsigned __int8 *)(a7) = 0;
    v_stack_m170 = a5;
    v_rbx = (*(unsigned __int64 *)(a1)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m168 = a6;
    v_rbx = (v_rbx) - (result);
    v_stack_m180 = a7;
    v_rbx = (v_rbx) >> (12);
    v_stack_m1C8 = 0;
    v_stack_m188 = 0;
    v_stack_m1A8 = 0;
    v_stack_m110 = v_xmm0;
    v_stack_m198 = *(unsigned __int64 *)(a1 + 56);
    v_stack_m100 = v_xmm0;
    v_stack_m1C0 = result;
    v_stack_mF0 = v_xmm0;
    v_stack_m178 = v_rbx;
    v_stack_m140 = v_xmm1;
    v_stack_m130 = v_xmm1;
    v_stack_m120 = v_xmm1;
    v_stack_m150 = v_xmm0;
    if (((*(unsigned int *)(a2 + 48)) & (0x200000ULL)) != 0) goto loc_004DBAFD;
    a2 = (*(unsigned __int64 *)(a1)) >> (12);
    result = MiGetProtoPteAddress(a2, a2, v_r15 + 12, v_stack_m188);
    if (result == 0) goto loc_004DBBDF;
    if (v_stack_m188 == 0) goto loc_004DBBDF;
    if (result != a3) goto loc_004DBBDF;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m188 + 52))) & (0x3FFFFFFFULL));
    result = ((unsigned int)(*(unsigned int *)(v_stack_m188 + 44))) - (a1);
    result = (a3) & (0xFFFFFFFFFFFFF000ULL);
    a4 = *(unsigned __int64 *)(v_stack_m188 + 8);
    if (result > (*(unsigned __int64 *)(v_stack_m188 + 8))) { a4 = result; }
    result = (result) + (0x1000ULL);
    a1 = *(unsigned __int64 *)(v_stack_m188 + 8) + result * 8;
    if ((*(unsigned __int64 *)(v_stack_m188 + 8) + result * 8) > result) { a1 = result; }
    if (a4 >= a1) goto loc_004DBBDF;
    result = (a3) - (v_rbx * 8);
    if (result < a4) goto loc_004DBBDF;
    result = (a3) - (v_rbx * 8);
    result = (result) - (-128);
    if (result > a1) goto loc_004DBBDF;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m188) + 60)) & (0x3FFULL));
    goto loc_004DBB39;
loc_004DBAFD:
    result = (*(unsigned __int64 *)(a5 + 8)) | (v_stack_m188);
    if (result < (v_rbx * 8)) goto loc_004DBBDF;
    if (result > (v_rbx * 8)) goto loc_004DBBDF;
loc_004DBB39:
    v_stack_m1B0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9782600) + *(unsigned __int16 *)(a1 + 174) * 8);
    a1 = (a3) - (v_rbx * 8);
    a1 = (a1) - (v_stack_mD8);
loc_004DBB66:
    *(unsigned __int64 *)(v_stack_mD8) = *(unsigned __int64 *)(a1 + v_stack_mD8 * 1);
    a3 = (16) - (16 - 15);
    if (condition_is_not_equal) goto loc_004DBB66;
    a3 = (a5) - (*(unsigned __int64 *)(a1 + v_stack_mD8 * 1));
    a3 = (a3) >> (4);
    a3 = (a3) * (*(unsigned __int64 *)(a1 + v_stack_mD8 * 1));
    v_rsi = (a3) | (-1);
    v_stack_m158 = a3;
loc_004DBBA6:
    if (0 >= 16) goto loc_004DBC06;
    if ((((unsigned __int8)(16 - 15)) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m138 + 0 * 8 + 96)))) != 0) goto loc_004DBBBC;
    a1 = (unsigned int)((0) + ((unsigned int)(16 - 15)));
    goto loc_004DBBA6;
loc_004DBBBC:
    v_rsi = (*(unsigned __int64 *)(v_stack_m138 + 0 * 8 + 96)) >> (12);
    v_rsi = (v_rsi) & (*(unsigned __int64 *)(v_stack_m138 + 0 * 8 + 96));
    result = (unsigned int)((v_rsi) & (15));
    if (result == 0) goto loc_004DBC66;
loc_004DBBDF:
loc_004DBBE2:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, 0, a3, 16);
    v_rsp = (v_rsp) + (504);
    return result;
loc_004DBC06:
    if (condition_is_not_equal) goto loc_004DBC60;
    result = (unsigned int)((a3) & (15));
    if (result == v_rbx) goto loc_004DBCB4;
    a4 = 0;
    a3 = 0;
    result = MiAcquireNonPagedResources(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9782600) + *(unsigned __int16 *)(a1 + 174) * 8), (unsigned int)((unsigned int)(a4 + 1)), a3, a4);
    if (sign_flag) goto loc_004DBBDF;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 48))) >> (12));
    a3 = (unsigned int)((a3) & (127));
    result = MiInitializePageColorBase(v_stack_m198, a4 + 1 + 2, a3, v_stack_m150);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m148)) >> (9));
    v_rbx = (unsigned int)((v_rbx) & (63));
    goto loc_004DBCC7;
loc_004DBC60:
loc_004DBC66:
    result = (v_rbx) - (a4 + 1 + 2);
    v_rsi = (v_rsi) + (result);
    if (v_rsi > (*(unsigned __int64 *)(v_rip + 9773162))) goto loc_004DBBDF;
    a2 = (v_rsi + v_rsi * 2) + (v_rsi + v_rsi * 2);
    a1 = (*(unsigned __int64 *)(v_stack_m198 + a2 * 8)) >> (54);
    if (((1) & ((unsigned int)(a1))) == 0) goto loc_004DBBDF;
    if ((result + a2 * 8) != a5) goto loc_004DBCBD;
loc_004DBCB4:
    *(unsigned __int8 *)(v_stack_m180) = 1;
    goto loc_004DBBDF;
loc_004DBCBD:
    result = MiPageToNode(v_rsi, a2, a3, v_stack_m150);
loc_004DBCC7:
    a2 = 0;
    a1 = (v_rsi) * ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    *(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_stack_m1B0 + 16) * 1 + 5187) = 1;
    a1 = (*(unsigned __int64 *)(a5 + 24)) & (*(unsigned __int64 *)(v_stack_m1B0 + 16));
    *(unsigned __int64 *)(a5 + 24) = a1;
    result = MiAddLockedPageCharge(a5, a2, a3, v_stack_m150);
    if ((unsigned int)(result) != 0) goto loc_004DBD21;
    if (((unsigned __int8)((unsigned __int8)(a4 + 1))) != 1) goto loc_004DBBDF;
    result = MiReleaseNonPagedResources(v_stack_m1B0, 1, a3, v_stack_m150);
    goto loc_004DBBDF;
loc_004DBD21:
    result = MiCopyPfnEntryRaw(v_stack_m110, a5, a3, v_stack_m150);
    if (a6 != 0) {
        a2 = 0;
        a1 = a6;
        result = MiObtainProtoReference(a1, a2, a3, v_stack_m150);
        a2 = a6;
        a1 = v_stack_m140;
        result = MiCopyPfnEntryRaw(a1, a2, a3, v_stack_m150);
        a2 = 17;
        a1 = a6;
        result = MiUnlockProtoPoolPage(a1, a2, a3, v_stack_m150);
    }
    a1 = (v_stack_m1B8) + (56);
    result = MiReleaseFaultState(a1, 1, v_stack_p70, v_stack_m150);
    v_stack_m1A0 = result;
    if (((unsigned __int8)((unsigned __int8)(a4 + 1))) != 1) goto loc_004DBEF8;
    if ((*(unsigned int *)(v_rip + 11448198)) != 0) {
        a2 = (unsigned __int8)(1 + 1);
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, v_stack_p70, v_stack_m150);
    }
    a1 = (v_stack_m190) >> (5);
    a1 = (unsigned int)((a1) & (31));
    v_stack_p70 = (unsigned __int8)(v_cr8);
    result = MiProtectionToCacheAttribute(a1, a2, v_stack_p70, v_stack_m150);
    v_stack_p30 = *(unsigned __int64 *)(v_stack_m1B8 + 96);
    v_stack_p28 = 18;
    v_stack_p20 = (unsigned int)(result);
    result = MiGetLargePage(v_stack_m1B0, v_stack_p78, (unsigned int)((unsigned int)(1 + 1)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (result != 0) goto loc_004DBE2E;
    if ((*(unsigned int *)(v_rip + 11448096)) != ((unsigned int)(result))) {
        a1 = 1 + 1;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)((unsigned int)(1 + 1)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    }
    result = MiReleaseNonPagedResources(v_stack_m1B0, 1, (unsigned int)((unsigned int)(1 + 1)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_004DBF90;
loc_004DBE2E:
    result = MiConvertLargeActivePageToChain(result, 1, (unsigned int)((unsigned int)(1 + 1)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    a1 = (result) - (result);
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    v_stack_m1A8 = a1;
loc_004DBE6C:
    if (!sign_flag) goto loc_004DBE98;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9782260))) + (1));
    *(unsigned int *)(v_rip + 9782246) = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 11440592)) & ((unsigned int)(result))) == 0) {
        a2 = 1;
        result = MiArePageContentsZero(a1, a2, (unsigned int)((unsigned int)(1 + 1)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
        a1 = v_stack_m1A8;
    }
    result = (unsigned int)((a1) & (15));
    if (result != v_stack_m178) goto loc_004DBEAB;
    goto loc_004DBEB7;
loc_004DBEAB:
    result = MiReleaseFreshPageAtDpc(result, a2, (unsigned int)((unsigned int)(1 + 1)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_004DBEB7:
    a1 = (v_stack_m1A8) + (1);
    v_rbx = (result) + (48);
    v_stack_m1A8 = a1;
    v_r13 = (1 + 15) - (1);
    if (condition_is_not_equal) goto loc_004DBE6C;
    if ((*(unsigned int *)(v_rip + 11447890)) != ((unsigned int)(v_r13))) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = (unsigned __int8)((unsigned int)(0xC0000017ULL));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)((unsigned int)(1 + 1)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    }
    v_r14 = 0;
    goto loc_004DBF90;
loc_004DBEF8:
    v_r12 = (a1 + a1 * 2) << (4);
    v_r14 = (unsigned int)(~(v_r14));
    v_r12 = (v_r12) + ((unsigned __int8)((unsigned int)(0xC0000017ULL)));
    v_r14 = (unsigned int)((v_r14) & ((unsigned int)(a2)));
    v_r14 = (unsigned int)((v_r14) + (0x2040ULL));
    v_r14 = (unsigned int)((v_r14) << (17));
    if ((*(unsigned __int64 *)(gs_base + (0 + 392))) == (*(unsigned __int64 *)(v_rip + 11448223))) {
        v_r14 = (unsigned int)((v_r14) | (8));
    }
    a4 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 32))) >> (16));
    v_stack_p68 = v_stack_m1A8;
    result = 0;
    v_stack_p60 = 0;
    v_stack_p58 = 0;
    v_stack_p50 = 0;
    v_stack_p48 = (unsigned int)(v_r14);
    v_stack_p40 = 255;
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    v_stack_p38 = (unsigned int)(v_rbx);
    v_stack_p30 = (unsigned int)(a1);
    v_stack_p28 = a2;
    v_stack_p20 = 0;
    result = MiFindContiguousPagesEx(v_stack_m1B0, a1, a1, a4);
loc_004DBF90:
    v_rbx = 0;
    a1 = (v_stack_m1B8) + (56);
    result = MiRelockFaultState(a1, v_stack_m1A0, a1, a4);
    if (v_stack_m168 == 0) goto loc_004DC020;
    a1 = (v_stack_m128) | (result);
    a2 = 0;
    v_stack_m128 = a1;
    result = MiRelockProtoPoolPage(v_stack_m168, a2, a1, a4);
loc_004DBFCC:
    if (condition_is_above_or_equal) goto loc_004DBFEA;
loc_004DBFD5:
    result = KeYieldProcessorEx(v_stack_p78, a2, a1, a4);
    if (sign_flag) goto loc_004DBFD5;
    goto loc_004DBFCC;
loc_004DBFEA:
    result = memcmp(v_stack_m140, v_stack_m168, 48, a4);
    v_rbx = 0;
    if ((unsigned int)(result) != 0) { v_rbx = 1; }
    result = MiReturnPfnReferenceCountAtDpc(v_stack_m168, v_stack_m168, 48, a4);
loc_004DC020:
    v_r13 = 0;
    v_stack_m198 = 0;
loc_004DC027:
    if (condition_is_above_or_equal) goto loc_004DC044;
loc_004DC030:
    result = KeYieldProcessorEx(v_stack_m198, v_stack_m168, 48, a4);
    if (sign_flag) goto loc_004DC030;
    goto loc_004DC027;
loc_004DC044:
    if ((unsigned __int8)(v_rbx) != 0) goto loc_004DC0B0;
    result = memcmp(v_stack_m110, v_stack_m170, 48, a4);
    if ((unsigned int)(result) == 0) goto loc_004DC0B9;
loc_004DC05E:
    if (sign_flag) goto loc_004DC15A;
    result = MiReleaseFreshPageAtDpc(v_r12, v_stack_m170, 48, a4);
    result = MiReleaseNonPagedResources(v_stack_m1B0, 1, 48, a4);
    v_stack_m1B8 = 0;
loc_004DC08F:
    if (condition_is_above_or_equal) goto loc_004DC15A;
loc_004DC09C:
    result = KeYieldProcessorEx(v_stack_m1B8, 1, 48, a4);
    if (sign_flag) goto loc_004DC09C;
    goto loc_004DC08F;
loc_004DC0B0:
    if (((unsigned __int8)(v_rbx)) == 1) goto loc_004DC05E;
loc_004DC0B9:
    if (((unsigned __int8)(v_rbx)) < 1) goto loc_004DC05E;
    result = MiIsFaultPteIntact(v_stack_m1B8, *(unsigned __int64 *)(v_stack_m1B8), v_stack_m160, v_stack_m190);
    if ((unsigned int)(result) == 0) goto loc_004DC05E;
    if (!sign_flag) goto loc_004DC0F8;
    result = MiRemoveLockedPageCharge(v_stack_m170, *(unsigned __int64 *)(v_stack_m1B8), v_stack_m160, v_stack_m190);
    goto loc_004DBBDF;
loc_004DC0F8:
    result = (unsigned __int8)((v_stack_m190) & (64));
    result = (unsigned __int8)(-(result));
    a3 = (unsigned int)((v_stack_m160) & (8));
    a3 = (unsigned int)((a3) + (12));
    result = MiCopyPage(a1, v_stack_m158, a3, v_stack_m190);
    result = MiSwapHardFaultPage(v_stack_m160, v_stack_m170, v_r12, v_stack_m190);
    v_stack_p78 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 32)));
    v_stack_p78 = 0;
    *(unsigned int *)(v_r12 + 32) = (unsigned int)((unsigned int)(v_stack_p78));
    result = MiReturnResident(v_stack_m1B0, 1, v_r12, v_stack_m190);
    *(unsigned __int8 *)(v_stack_m180) = 1;
    goto loc_004DBBE2;
loc_004DC15A:
    result = MiRemoveLockedPageChargeAndDecRef(v_stack_m170, 1, v_r12, v_stack_m190);
    result = 0;
    goto loc_004DBBE2;
}
```

## 5. (Beta) C Style

```c
int64_t MiIdealClusterPage(void *Arg1, void *Arg2, void *Arg3, int64_t Arg4, void *Arg5, int64_t Arg6, void *Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m110;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m58;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (504);
    result = (*(uint64_t *)(v_rip + 0x92EDB9)) ^ (local_rsp);
    v_stack_m58 = result;
    local_r15 = 0;
    v_stack_m1A0 = Arg2;
    v_stack_m1B8 = Arg1;
    v_stack_m160 = Arg3;
    v_stack_m190 = Arg4;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) >> (8));
    result = (*(uint64_t *)(arg1)) & (0xFFFFFFFFFFFF0000ULL);
    *(uint8_t *)(arg7) = 0;
    v_stack_m170 = Arg5;
    local_rbx = (*(uint64_t *)(arg1)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m168 = Arg6;
    local_rbx = (local_rbx) - (result);
    v_stack_m180 = Arg7;
    local_rbx = (local_rbx) >> (12);
    v_stack_m1C8 = 0;
    v_stack_m188 = 0;
    v_stack_m1A8 = 0;
    v_stack_m110 = v_xmm0;
    v_stack_m198 = *(uint64_t *)(arg1 + 0x38);
    v_stack_m100 = v_xmm0;
    v_stack_m1C0 = result;
    v_stack_mF0 = v_xmm0;
    v_stack_m178 = local_rbx;
    v_stack_m140 = v_xmm1;
    v_stack_m130 = v_xmm1;
    v_stack_m120 = v_xmm1;
    v_stack_m150 = v_xmm0;
    if (((*(uint32_t *)(arg2 + 0x30)) & (0x200000ULL)) != 0) goto loc_004DBAFD;
    Arg2 = (*(uint64_t *)(arg1)) >> (12);
    result = MiGetProtoPteAddress(Arg2, Arg2, local_r15 + 12, v_stack_m188);
    if (result == 0) goto loc_004DBBDF;
    if (v_stack_m188 == 0) goto loc_004DBBDF;
    if (result != Arg3) goto loc_004DBBDF;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x34))) & (0x3FFFFFFFULL));
    result = ((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x2C))) - (Arg1);
    result = (Arg3) & (0xFFFFFFFFFFFFF000ULL);
    Arg4 = *(uint64_t *)(v_stack_m188 + 0x8);
    if (result > (*(uint64_t *)(v_stack_m188 + 0x8))) { Arg4 = result; }
    result = (result) + (0x1000ULL);
    Arg1 = *(uint64_t *)(v_stack_m188 + 0x8) + result * 8;
    if ((*(uint64_t *)(v_stack_m188 + 0x8) + result * 8) > result) { Arg1 = result; }
    if (Arg4 >= Arg1) goto loc_004DBBDF;
    result = (Arg3) - (local_rbx * 8);
    if (result < Arg4) goto loc_004DBBDF;
    result = (Arg3) - (local_rbx * 8);
    result = (result) - (-128);
    if (result > Arg1) goto loc_004DBBDF;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_m188) + 0x3C)) & (0x3FFULL));
    goto loc_004DBB39;
loc_004DBAFD:
    result = (*(uint64_t *)(arg5 + 0x8)) | (v_stack_m188);
    if (result < (local_rbx * 8)) goto loc_004DBBDF;
    if (result > (local_rbx * 8)) goto loc_004DBBDF;
loc_004DBB39:
    v_stack_m1B0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x954548) + *(uint16_t *)(arg1 + 0xAE) * 8);
    Arg1 = (Arg3) - (local_rbx * 8);
    Arg1 = (Arg1) - (v_stack_mD8);
loc_004DBB66:
    *(uint64_t *)(v_stack_mD8) = *(uint64_t *)(arg1 + v_stack_mD8 * 1);
    Arg3 = (16) - (16 - 15);
    if (condition_is_not_equal) goto loc_004DBB66;
    Arg3 = (Arg5) - (*(uint64_t *)(arg1 + v_stack_mD8 * 1));
    Arg3 = (Arg3) >> (4);
    Arg3 = (Arg3) * (*(uint64_t *)(arg1 + v_stack_mD8 * 1));
    local_rsi = (Arg3) | (-1);
    v_stack_m158 = Arg3;
loc_004DBBA6:
    if (0 >= 16) goto loc_004DBC06;
    if ((((uint8_t)(16 - 15)) & ((uint8_t)(*(uint64_t *)(v_stack_m138 + 0x0 * 8 + 0x60)))) != 0) goto loc_004DBBBC;
    Arg1 = (uint32_t)((0) + ((uint32_t)(16 - 15)));
    goto loc_004DBBA6;
loc_004DBBBC:
    local_rsi = (*(uint64_t *)(v_stack_m138 + 0x0 * 8 + 0x60)) >> (12);
    local_rsi = (local_rsi) & (*(uint64_t *)(v_stack_m138 + 0x0 * 8 + 0x60));
    result = (uint32_t)((local_rsi) & (15));
    if (result == 0) goto loc_004DBC66;
loc_004DBBDF:
loc_004DBBE2:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 0, Arg3, 16);
    local_rsp = (local_rsp) + (504);
    return result;
loc_004DBC06:
    if (condition_is_not_equal) goto loc_004DBC60;
    result = (uint32_t)((Arg3) & (15));
    if (result == local_rbx) goto loc_004DBCB4;
    Arg4 = 0;
    Arg3 = 0;
    result = MiAcquireNonPagedResources(*(uint64_t *)(*(uint64_t *)(v_rip + 0x954548) + *(uint16_t *)(arg1 + 0xAE) * 8), (uint32_t)((uint32_t)(Arg4 + 1)), Arg3, Arg4);
    if (sign_flag) goto loc_004DBBDF;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x30))) >> (12));
    Arg3 = (uint32_t)((Arg3) & (127));
    result = MiInitializePageColorBase(v_stack_m198, Arg4 + 1 + 2, Arg3, v_stack_m150);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m148)) >> (9));
    local_rbx = (uint32_t)((local_rbx) & (63));
    goto loc_004DBCC7;
loc_004DBC60:
loc_004DBC66:
    result = (local_rbx) - (Arg4 + 1 + 2);
    local_rsi = (local_rsi) + (result);
    if (local_rsi > (*(uint64_t *)(v_rip + 0x95206A))) goto loc_004DBBDF;
    Arg2 = (local_rsi + local_rsi * 2) + (local_rsi + local_rsi * 2);
    Arg1 = (*(uint64_t *)(v_stack_m198 + arg2 * 8)) >> (54);
    if (((1) & ((uint32_t)(Arg1))) == 0) goto loc_004DBBDF;
    if ((result + Arg2 * 8) != Arg5) goto loc_004DBCBD;
loc_004DBCB4:
    *(uint8_t *)(v_stack_m180) = 1;
    goto loc_004DBBDF;
loc_004DBCBD:
    result = MiPageToNode(local_rsi, Arg2, Arg3, v_stack_m150);
loc_004DBCC7:
    Arg2 = 0;
    Arg1 = (local_rsi) * ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    *(uint8_t *)(arg1 + *(uint64_t *)(v_stack_m1B0 + 0x10) * 1 + 0x1443) = 1;
    Arg1 = (*(uint64_t *)(arg5 + 0x18)) & (*(uint64_t *)(v_stack_m1B0 + 0x10));
    *(void **)(arg5 + 0x18) = Arg1;
    result = MiAddLockedPageCharge(Arg5, Arg2, Arg3, v_stack_m150);
    if ((uint32_t)(result) != 0) goto loc_004DBD21;
    if (((uint8_t)((uint8_t)(Arg4 + 1))) != 1) goto loc_004DBBDF;
    result = MiReleaseNonPagedResources(v_stack_m1B0, 1, Arg3, v_stack_m150);
    goto loc_004DBBDF;
loc_004DBD21:
    result = MiCopyPfnEntryRaw(v_stack_m110, Arg5, Arg3, v_stack_m150);
    if (Arg6 != 0) {
        Arg2 = 0;
        Arg1 = Arg6;
        result = MiObtainProtoReference(Arg1, Arg2, Arg3, v_stack_m150);
        Arg2 = Arg6;
        Arg1 = v_stack_m140;
        result = MiCopyPfnEntryRaw(Arg1, Arg2, Arg3, v_stack_m150);
        Arg2 = 17;
        Arg1 = Arg6;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, Arg3, v_stack_m150);
    }
    Arg1 = (v_stack_m1B8) + (56);
    result = MiReleaseFaultState(Arg1, 1, v_stack_p70, v_stack_m150);
    v_stack_m1A0 = result;
    if (((uint8_t)((uint8_t)(Arg4 + 1))) != 1) goto loc_004DBEF8;
    if ((*(uint32_t *)(v_rip + 0xAEAF86)) != 0) {
        Arg2 = (uint8_t)(1 + 1);
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p70, v_stack_m150);
    }
    Arg1 = (v_stack_m190) >> (5);
    Arg1 = (uint32_t)((Arg1) & (31));
    v_stack_p70 = (uint8_t)(v_cr8);
    result = MiProtectionToCacheAttribute(Arg1, Arg2, v_stack_p70, v_stack_m150);
    v_stack_p30 = *(uint64_t *)(v_stack_m1B8 + 0x60);
    v_stack_p28 = 18;
    v_stack_p20 = (uint32_t)(result);
    result = MiGetLargePage(v_stack_m1B0, v_stack_p78, (uint32_t)((uint32_t)(1 + 1)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (result != 0) goto loc_004DBE2E;
    if ((*(uint32_t *)(v_rip + 0xAEAF20)) != ((uint32_t)(result))) {
        Arg1 = 1 + 1;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)((uint32_t)(1 + 1)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    }
    result = MiReleaseNonPagedResources(v_stack_m1B0, 1, (uint32_t)((uint32_t)(1 + 1)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_004DBF90;
loc_004DBE2E:
    result = MiConvertLargeActivePageToChain(result, 1, (uint32_t)((uint32_t)(1 + 1)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    Arg1 = (result) - (result);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    v_stack_m1A8 = Arg1;
loc_004DBE6C:
    if (!sign_flag) goto loc_004DBE98;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9543F4))) + (1));
    *(uint32_t *)(v_rip + 0x9543E6) = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xAE91D0)) & ((uint32_t)(result))) == 0) {
        Arg2 = 1;
        result = MiArePageContentsZero(Arg1, Arg2, (uint32_t)((uint32_t)(1 + 1)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
        Arg1 = v_stack_m1A8;
    }
    result = (uint32_t)((Arg1) & (15));
    if (result != v_stack_m178) goto loc_004DBEAB;
    goto loc_004DBEB7;
loc_004DBEAB:
    result = MiReleaseFreshPageAtDpc(result, Arg2, (uint32_t)((uint32_t)(1 + 1)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_004DBEB7:
    Arg1 = (v_stack_m1A8) + (1);
    local_rbx = (result) + (48);
    v_stack_m1A8 = Arg1;
    local_r13 = (1 + 15) - (1);
    if (condition_is_not_equal) goto loc_004DBE6C;
    if ((*(uint32_t *)(v_rip + 0xAEAE52)) != ((uint32_t)(local_r13))) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = (uint8_t)((uint32_t)(0xC0000017ULL));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)((uint32_t)(1 + 1)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    }
    local_r14 = 0;
    goto loc_004DBF90;
loc_004DBEF8:
    local_r12 = (Arg1 + Arg1 * 2) << (4);
    local_r14 = (uint32_t)(~(local_r14));
    local_r12 = (local_r12) + ((uint8_t)((uint32_t)(0xC0000017ULL)));
    local_r14 = (uint32_t)((local_r14) & ((uint32_t)(Arg2)));
    local_r14 = (uint32_t)((local_r14) + (0x2040ULL));
    local_r14 = (uint32_t)((local_r14) << (17));
    if ((*(uint64_t *)(gs_base + (0 + 0x188))) == (*(uint64_t *)(v_rip + 0xAEAF9F))) {
        local_r14 = (uint32_t)((local_r14) | (8));
    }
    Arg4 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x20))) >> (16));
    v_stack_p68 = v_stack_m1A8;
    result = 0;
    v_stack_p60 = 0;
    v_stack_p58 = 0;
    v_stack_p50 = 0;
    v_stack_p48 = (uint32_t)(local_r14);
    v_stack_p40 = 255;
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    v_stack_p38 = (uint32_t)(local_rbx);
    v_stack_p30 = (uint32_t)(Arg1);
    v_stack_p28 = Arg2;
    v_stack_p20 = 0;
    result = MiFindContiguousPagesEx(v_stack_m1B0, Arg1, Arg1, Arg4);
loc_004DBF90:
    local_rbx = 0;
    Arg1 = (v_stack_m1B8) + (56);
    result = MiRelockFaultState(Arg1, v_stack_m1A0, Arg1, Arg4);
    if (v_stack_m168 == 0) goto loc_004DC020;
    Arg1 = (v_stack_m128) | (result);
    Arg2 = 0;
    v_stack_m128 = Arg1;
    result = MiRelockProtoPoolPage(v_stack_m168, Arg2, Arg1, Arg4);
loc_004DBFCC:
    if (condition_is_above_or_equal) goto loc_004DBFEA;
loc_004DBFD5:
    result = KeYieldProcessorEx(v_stack_p78, Arg2, Arg1, Arg4);
    if (sign_flag) goto loc_004DBFD5;
    goto loc_004DBFCC;
loc_004DBFEA:
    result = memcmp(v_stack_m140, v_stack_m168, 48, Arg4);
    local_rbx = 0;
    if ((uint32_t)(result) != 0) { local_rbx = 1; }
    result = MiReturnPfnReferenceCountAtDpc(v_stack_m168, v_stack_m168, 48, Arg4);
loc_004DC020:
    local_r13 = 0;
    v_stack_m198 = 0;
loc_004DC027:
    if (condition_is_above_or_equal) goto loc_004DC044;
loc_004DC030:
    result = KeYieldProcessorEx(v_stack_m198, v_stack_m168, 48, Arg4);
    if (sign_flag) goto loc_004DC030;
    goto loc_004DC027;
loc_004DC044:
    if ((uint8_t)(local_rbx) != 0) goto loc_004DC0B0;
    result = memcmp(v_stack_m110, v_stack_m170, 48, Arg4);
    if ((uint32_t)(result) == 0) goto loc_004DC0B9;
loc_004DC05E:
    if (sign_flag) goto loc_004DC15A;
    result = MiReleaseFreshPageAtDpc(local_r12, v_stack_m170, 48, Arg4);
    result = MiReleaseNonPagedResources(v_stack_m1B0, 1, 48, Arg4);
    v_stack_m1B8 = 0;
loc_004DC08F:
    if (condition_is_above_or_equal) goto loc_004DC15A;
loc_004DC09C:
    result = KeYieldProcessorEx(v_stack_m1B8, 1, 48, Arg4);
    if (sign_flag) goto loc_004DC09C;
    goto loc_004DC08F;
loc_004DC0B0:
    if (((uint8_t)(local_rbx)) == 1) goto loc_004DC05E;
loc_004DC0B9:
    if (((uint8_t)(local_rbx)) < 1) goto loc_004DC05E;
    result = MiIsFaultPteIntact(v_stack_m1B8, *(uint64_t *)(v_stack_m1B8), v_stack_m160, v_stack_m190);
    if ((uint32_t)(result) == 0) goto loc_004DC05E;
    if (!sign_flag) goto loc_004DC0F8;
    result = MiRemoveLockedPageCharge(v_stack_m170, *(uint64_t *)(v_stack_m1B8), v_stack_m160, v_stack_m190);
    goto loc_004DBBDF;
loc_004DC0F8:
    result = (uint8_t)((v_stack_m190) & (64));
    result = (uint8_t)(-(result));
    Arg3 = (uint32_t)((v_stack_m160) & (8));
    Arg3 = (uint32_t)((Arg3) + (12));
    result = MiCopyPage(Arg1, v_stack_m158, Arg3, v_stack_m190);
    result = MiSwapHardFaultPage(v_stack_m160, v_stack_m170, local_r12, v_stack_m190);
    v_stack_p78 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x20)));
    v_stack_p78 = 0;
    *(uint32_t *)(local_r12 + 0x20) = (uint32_t)((uint32_t)(v_stack_p78));
    result = MiReturnResident(v_stack_m1B0, 1, local_r12, v_stack_m190);
    *(uint8_t *)(v_stack_m180) = 1;
    goto loc_004DBBE2;
loc_004DC15A:
    result = MiRemoveLockedPageChargeAndDecRef(v_stack_m170, 1, local_r12, v_stack_m190);
    result = 0;
    goto loc_004DBBE2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg3` | `+ 0x0 + rdx*1` | `64` | `R` |
| `Arg5` | `+ 0x8` | `64` | `R` |
| `Arg5` | `+ 0x18` | `64` | `R` |
| `Arg5` | `+ 0x18` | `64` | `R/W` |
| `Arg5` | `+ 0x18` | `64` | `W` |
| `Arg5` | `+ 0x20` | `32` | `R` |
| `Arg7` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004DB964&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
