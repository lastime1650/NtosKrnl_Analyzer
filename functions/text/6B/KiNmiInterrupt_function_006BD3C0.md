# KiNmiInterrupt

- RVA: `0x006BD3C0`–`0x006BD81D` (길이 `1,117` bytes)
- VA: `0x00000001406BD3C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1B28`
- 디코드: `251`개 명령, `1,117/1,117` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x006BD496` → [KiSetSpecCtrlNmi](KiSetSpecCtrlNmi_function_006B32B0.md) (function, `0x006B32B0`)
- `0x006BD4E5` → [KiSetSpecCtrlNmi](KiSetSpecCtrlNmi_function_006B32B0.md) (function, `0x006B32B0`)
- `0x006BD522` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006BD558` → [KeWakeProcessor](../5B/KeWakeProcessor_function_005BE080.md) (function, `0x005BE080`)
- `0x006BD581` → [KiCheckForSListAddress](../40/KiCheckForSListAddress_function_0040B810.md) (function, `0x0040B810`)
- `0x006BD5AA` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006BD5C2` → [KiMcheckFastForward](../5C/KiMcheckFastForward_function_005CB550.md) (function, `0x005CB550`)
- `0x006BD629` → [KxNmiInterrupt](KxNmiInterrupt_function_006BD840.md) (function, `0x006BD840`)
- `0x006BD644` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006BD686` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006BD6A2` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006BD816` → [KiBugCheckDispatch](../6C/KiBugCheckDispatch_function_006C5880.md) (function, `0x006C5880`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006BD424` → RVA `0x00FC6B34` (`ALMOSTRO`; read)
- `0x006BD463` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x006BD46A` → RVA `0x00F231B8` (`.data`; read)
- `0x006BD4A0` → RVA `0x01201840` (`CFGRO`; read)
- `0x006BD4EA` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006BD55D` → RVA `0x006BA577` (`ExpInterlockedPopEntrySListResume`; read)
- `0x006BD56D` → RVA `0x006BA590` (`ExpInterlockedPopEntrySListEnd`; read)
- `0x006BD590` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x006BD5A1` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x006BD5E1` → RVA `0x006BD3C0` (`KiNmiInterrupt`; read)
- `0x006BD5F1` → RVA `0x006BD806` (`KiNmiInterruptEnd`; read)
- `0x006BD605` → RVA `0x00BCB240` (`KiNmiInterruptShadow`; read)
- `0x006BD615` → RVA `0x00BCB2B5` (`KiNmiInterruptShadowEnd`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006BD756` → [KiKernelIstExit](../../kvascode/BC/KiKernelIstExit_function_00BCCC40.md) (`tail-transfer`)
  - `0x006BD7FF` → [KiKernelIstExit](../../kvascode/BC/KiKernelIstExit_function_00BCCC40.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006BD3C0  48 83 EC 08                     sub rsp, 8
006BD3C4  55                              push rbp
006BD3C5  56                              push rsi
006BD3C6  48 81 EC 50 01 00 00            sub rsp, 0x150
006BD3CD  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006BD3D5  C6 45 AB 00                     mov byte ptr [rbp - 0x55], 0
006BD3D9  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006BD3DD  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006BD3E1  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006BD3E5  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006BD3E9  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006BD3ED  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006BD3F1  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006BD3F5  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BD3FC  0F 85 9E 00 00 00               jne 0x1406bd4a0
006BD402  33 D2                           xor edx, edx
006BD404  F3 48 0F 1E CA                  rdsspq rdx
006BD409  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006BD40D  B9 01 01 00 C0                  mov ecx, 0xc0000101
006BD412  0F 32                           rdmsr
006BD414  89 45 E8                        mov dword ptr [rbp - 0x18], eax
006BD417  89 55 EC                        mov dword ptr [rbp - 0x14], edx
006BD41A  B8 50 00 00 00                  mov eax, 0x50
006BD41F  0F 03 C0                        lsl eax, eax
006BD422  74 2E                           je 0x1406bd452
006BD424  F7 05 06 97 90 00 04 00 00 00   test dword ptr [rip + 0x909706], 4
006BD42E  75 11                           jne 0x1406bd441
006BD430  0F 01 45 F0                     sgdt [rbp - 0x10]
006BD434  48 8B 55 F2                     mov rdx, qword ptr [rbp - 0xe]
006BD438  48 8B 92 C0 E0 FF FF            mov rdx, qword ptr [rdx - 0x1f40]
006BD43F  EB 41                           jmp 0x1406bd482
006BD441  0F 01 F9                        rdtscp
006BD444  0F B6 C1                        movzx eax, cl
006BD447  C1 E9 08                        shr ecx, 8
006BD44A  C1 E1 06                        shl ecx, 6
006BD44D  44 8B C1                        mov r8d, ecx
006BD450  EB 11                           jmp 0x1406bd463
006BD452  44 8B C0                        mov r8d, eax
006BD455  41 81 E0 FF 03 00 00            and r8d, 0x3ff
006BD45C  41 C1 E0 06                     shl r8d, 6
006BD460  C1 E8 0E                        shr eax, 0xe
006BD463  48 8D 0D D6 B7 90 00            lea rcx, [rip + 0x90b7d6]
006BD46A  48 8B 15 47 5D 86 00            mov rdx, qword ptr [rip + 0x865d47]
006BD471  41 0B C0                        or eax, r8d
006BD474  8B 04 82                        mov eax, dword ptr [rdx + rax*4]
006BD477  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
006BD47B  48 81 EA 80 01 00 00            sub rdx, 0x180
006BD482  8B C2                           mov eax, edx
006BD484  48 C1 EA 20                     shr rdx, 0x20
006BD488  B9 01 01 00 C0                  mov ecx, 0xc0000101
006BD48D  0F 30                           wrmsr
006BD48F  0F 20 D0                        mov rax, cr2
006BD492  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
006BD496  E8 15 5E FF FF                  call 0x1406b32b0
006BD49B  E9 87 00 00 00                  jmp 0x1406bd527
006BD4A0  F6 05 99 43 B4 00 01            test byte ptr [rip + 0xb44399], 1
006BD4A7  75 03                           jne 0x1406bd4ac
006BD4A9  0F 01 F8                        swapgs
006BD4AC  0F AE E8                        lfence
006BD4AF  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006BD4B8  48 85 C9                        test rcx, rcx
006BD4BB  74 1F                           je 0x1406bd4dc
006BD4BD  F3 48 0F 1E CA                  rdsspq rdx
006BD4C2  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006BD4CB  49 83 C2 08                     add r10, 8
006BD4CF  49 3B D2                        cmp rdx, r10
006BD4D2  75 08                           jne 0x1406bd4dc
006BD4D4  F3 0F 01 29                     rstorssp dword ptr [rcx]
006BD4D8  F3 0F 01 EA                     saveprevssp
006BD4DC  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006BD4E5  E8 C6 5D FF FF                  call 0x1406b32b0
006BD4EA  83 3D 73 9D 90 00 00            cmp dword ptr [rip + 0x909d73], 0
006BD4F1  74 1F                           je 0x1406bd512
006BD4F3  B9 A7 06 00 00                  mov ecx, 0x6a7
006BD4F8  0F 32                           rdmsr
006BD4FA  83 FA 00                        cmp edx, 0
006BD4FD  74 13                           je 0x1406bd512
006BD4FF  8B CA                           mov ecx, edx
006BD501  23 15 5D 9D 90 00               and edx, dword ptr [rip + 0x909d5d]
006BD507  3B D1                           cmp edx, ecx
006BD509  74 07                           je 0x1406bd512
006BD50B  B9 A7 06 00 00                  mov ecx, 0x6a7
006BD510  0F 30                           wrmsr
006BD512  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006BD517  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006BD520  74 05                           je 0x1406bd527
006BD522  E8 39 04 E4 FF                  call 0x1404fd960
006BD527  FC                              cld
006BD528  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006BD52C  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006BD535  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006BD539  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006BD53D  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006BD541  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006BD545  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006BD549  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006BD54D  65 80 3C 25 DA 87 00 00 00      cmp byte ptr gs:[0x87da], 0
006BD556  74 05                           je 0x1406bd55d
006BD558  E8 23 0B F0 FF                  call 0x1405be080
006BD55D  48 8D 05 13 D0 FF FF            lea rax, [rip - 0x2fed]
006BD564  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006BD56B  73 19                           jae 0x1406bd586
006BD56D  48 8D 05 1C D0 FF FF            lea rax, [rip - 0x2fe4]
006BD574  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006BD57B  72 09                           jb 0x1406bd586
006BD57D  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006BD581  E8 8A E2 D4 FF                  call 0x14040b810
006BD586  33 F6                           xor esi, esi
006BD588  65 FF 04 25 C0 87 00 00         inc dword ptr gs:[0x87c0]
006BD590  F6 05 59 96 90 00 FF            test byte ptr [rip + 0x909659], 0xff
006BD597  74 03                           je 0x1406bd59c
006BD599  0F 01 CA                        clac
006BD59C  B9 0F 00 00 00                  mov ecx, 0xf
006BD5A1  83 3D 78 97 90 00 00            cmp dword ptr [rip + 0x909778], 0
006BD5A8  74 07                           je 0x1406bd5b1
006BD5AA  E8 31 B5 EF FF                  call 0x1405b8ae0
006BD5AF  EB 08                           jmp 0x1406bd5b9
006BD5B1  44 0F 20 C0                     mov rax, cr8
006BD5B5  44 0F 22 C1                     mov cr8, rcx
006BD5B9  88 45 A9                        mov byte ptr [rbp - 0x57], al
006BD5BC  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006BD5C0  B2 01                           mov dl, 1
006BD5C2  E8 89 DF F0 FF                  call 0x1405cb550
006BD5C7  66 65 0F BA 2C 25 26 85 00 00 00  bts word ptr gs:[0x8526], 0
006BD5D2  0F 82 2E 02 00 00               jb 0x1406bd806
006BD5D8  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BD5DF  75 24                           jne 0x1406bd605
006BD5E1  48 8D 05 D8 FD FF FF            lea rax, [rip - 0x228]
006BD5E8  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006BD5EF  77 14                           ja 0x1406bd605
006BD5F1  48 8D 05 0E 02 00 00            lea rax, [rip + 0x20e]
006BD5F8  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006BD5FF  0F 87 01 02 00 00               ja 0x1406bd806
006BD605  48 8D 05 34 DC 50 00            lea rax, [rip + 0x50dc34]
006BD60C  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006BD613  77 14                           ja 0x1406bd629
006BD615  48 8D 05 99 DC 50 00            lea rax, [rip + 0x50dc99]
006BD61C  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006BD623  0F 87 DD 01 00 00               ja 0x1406bd806
006BD629  E8 12 02 00 00                  call 0x1406bd840
006BD62E  65 80 24 25 26 85 00 00 00      and byte ptr gs:[0x8526], 0
006BD637  0F B6 4D A9                     movzx ecx, byte ptr [rbp - 0x57]
006BD63B  83 3D DE 96 90 00 00            cmp dword ptr [rip + 0x9096de], 0
006BD642  74 07                           je 0x1406bd64b
006BD644  E8 97 B4 EF FF                  call 0x1405b8ae0
006BD649  EB 04                           jmp 0x1406bd64f
006BD64B  44 0F 22 C1                     mov cr8, rcx
006BD64F  48 8B B5 D0 00 00 00            mov rsi, qword ptr [rbp + 0xd0]
006BD656  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006BD65D  0F 84 0F 01 00 00               je 0x1406bd772
006BD663  F6 05 86 95 90 00 FF            test byte ptr [rip + 0x909586], 0xff
006BD66A  74 03                           je 0x1406bd66f
006BD66C  0F 01 CB                        stac
006BD66F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BD678  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006BD67E  74 14                           je 0x1406bd694
006BD680  F6 41 02 01                     test byte ptr [rcx + 2], 1
006BD684  74 0E                           je 0x1406bd694
006BD686  E8 85 30 F0 FF                  call 0x1405c0710
006BD68B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BD694  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006BD698  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006BD6A0  74 05                           je 0x1406bd6a7
006BD6A2  E8 39 02 E4 FF                  call 0x1404fd8e0
006BD6A7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006BD6B0  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006BD6B5  73 2A                           jae 0x1406bd6e1
006BD6B7  33 C9                           xor ecx, ecx
006BD6B9  F3 48 0F 1E C9                  rdsspq rcx
006BD6BE  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006BD6C7  49 83 C0 08                     add r8, 8
006BD6CB  49 3B C8                        cmp rcx, r8
006BD6CE  75 11                           jne 0x1406bd6e1
006BD6D0  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006BD6D9  F3 0F 01 29                     rstorssp dword ptr [rcx]
006BD6DD  F3 0F 01 EA                     saveprevssp
006BD6E1  0F B6 45 A8                     movzx eax, byte ptr [rbp - 0x58]
006BD6E5  65 88 04 25 5E 08 00 00         mov byte ptr gs:[0x85e], al
006BD6ED  66 65 83 3C 25 6A 08 00 00 00   cmp word ptr gs:[0x86a], 0
006BD6F7  74 0F                           je 0x1406bd708
006BD6F9  8B 85 C0 00 00 00               mov eax, dword ptr [rbp + 0xc0]
006BD6FF  B9 48 00 00 00                  mov ecx, 0x48
006BD704  33 D2                           xor edx, edx
006BD706  0F 30                           wrmsr
006BD708  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006BD70C  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006BD710  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006BD714  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006BD718  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006BD71C  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006BD720  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006BD724  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006BD728  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006BD72C  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006BD730  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006BD734  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006BD738  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006BD73C  48 8B E5                        mov rsp, rbp
006BD73F  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006BD746  48 81 C4 E8 00 00 00            add rsp, 0xe8
006BD74D  F6 05 EC 40 B4 00 01            test byte ptr [rip + 0xb440ec], 1
006BD754  74 05                           je 0x1406bd75b
006BD756  E9 E5 F4 50 00                  jmp 0x140bccc40
006BD75B  66 65 F7 04 25 58 08 00 00 00 02  test word ptr gs:[0x858], 0x200
006BD766  74 05                           je 0x1406bd76d
006BD768  0F 00 6C 24 20                  verw word ptr [rsp + 0x20]
006BD76D  0F 01 F8                        swapgs
006BD770  48 CF                           iretq
006BD772  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006BD776  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006BD77A  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006BD77E  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006BD782  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006BD786  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006BD78A  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006BD78E  0F B6 45 A8                     movzx eax, byte ptr [rbp - 0x58]
006BD792  65 88 04 25 5E 08 00 00         mov byte ptr gs:[0x85e], al
006BD79A  66 65 83 3C 25 6A 08 00 00 00   cmp word ptr gs:[0x86a], 0
006BD7A4  74 0F                           je 0x1406bd7b5
006BD7A6  8B 85 C0 00 00 00               mov eax, dword ptr [rbp + 0xc0]
006BD7AC  B9 48 00 00 00                  mov ecx, 0x48
006BD7B1  33 D2                           xor edx, edx
006BD7B3  0F 30                           wrmsr
006BD7B5  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
006BD7B8  8B 55 EC                        mov edx, dword ptr [rbp - 0x14]
006BD7BB  B9 01 01 00 C0                  mov ecx, 0xc0000101
006BD7C0  0F 30                           wrmsr
006BD7C2  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
006BD7C6  0F 22 D0                        mov cr2, rax
006BD7C9  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006BD7CD  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006BD7D1  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006BD7D5  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006BD7D9  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006BD7DD  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006BD7E1  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006BD7E5  48 8B E5                        mov rsp, rbp
006BD7E8  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006BD7EF  48 81 C4 E8 00 00 00            add rsp, 0xe8
006BD7F6  F6 05 43 40 B4 00 01            test byte ptr [rip + 0xb44043], 1
006BD7FD  74 05                           je 0x1406bd804
006BD7FF  E9 3C F4 50 00                  jmp 0x140bccc40
006BD804  48 CF                           iretq
006BD806  4D 33 D2                        xor r10, r10
006BD809  4D 33 C9                        xor r9, r9
006BD80C  4D 33 C0                        xor r8, r8
006BD80F  33 D2                           xor edx, edx
006BD811  B9 11 01 00 00                  mov ecx, 0x111
006BD816  E8 65 80 00 00                  call 0x1406c5880
006BD81B  90                              nop
006BD81C  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiNmiInterrupt(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned __int8 v_stack_m13D;
    unsigned __int8 v_stack_m13F;
    unsigned __int8 v_stack_m140;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m28;
    unsigned __int16 v_stack_m68;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF6;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p0;
    unsigned __int16 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (8);
    v_rsp = (v_rsp) - (336);
    v_stack_m13D = 0;
    v_stack_m138 = result;
    v_stack_m130 = a1;
    v_stack_m128 = a2;
    v_stack_m120 = a3;
    v_stack_m118 = a4;
    v_stack_m110 = v_r10;
    v_stack_m108 = v_r11;
    if (((v_stack_p8) & (1)) != 0) goto loc_006BD4A0;
    a2 = 0;
    v_stack_m90 = 0;
    v_stack_m100 = (unsigned int)(result);
    v_stack_mFC = 0;
    if (condition_is_equal) goto loc_006BD452;
    if (((*(unsigned int *)(v_rip + 9475846)) & (4)) != 0) goto loc_006BD441;
    goto loc_006BD482;
loc_006BD441:
    a1 = (unsigned int)(((unsigned int)(0xC0000101ULL)) >> (8));
    a1 = (unsigned int)((a1) << (6));
    goto loc_006BD463;
loc_006BD452:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)((unsigned int)(0xC0000101ULL))))) & (0x3FFULL));
    a3 = (unsigned int)((a3) << (6));
    result = (unsigned int)(((unsigned __int8)((unsigned int)(0xC0000101ULL))) >> (14));
loc_006BD463:
    result = (unsigned int)((result) | ((unsigned int)(a3)));
    a2 = (*(unsigned __int64 *)(v_rip + 9484246 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8805703) + result * 4)) * 8)) - (384);
loc_006BD482:
    a2 = (a2) >> (32);
    v_stack_m98 = v_cr2;
    result = KiSetSpecCtrlNmi((unsigned int)(0xC0000101ULL), a2, a3, a4);
    goto loc_006BD527;
loc_006BD4A0:
    if (((*(unsigned __int8 *)(v_rip + 11813785)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006BD4DC;
    v_r10 = (*(unsigned __int64 *)(gs_base + (0 + 40224))) + (8);
    if (a2 == v_r10) {
    }
    result = KiSetSpecCtrlNmi(*(unsigned __int64 *)(gs_base + (0 + 40232)), a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 9477491)) == 0) goto loc_006BD512;
    if (((unsigned int)(a2)) == 0) goto loc_006BD512;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9477469)));
    if (((unsigned int)(a2)) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) {
        a1 = 0x6A7ULL;
    }
    v_stack_m68 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 3)) & (3)) != 0) {
        result = KiSaveDebugRegisterState(a1, a2, a3, a4);
    }
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm2;
    v_stack_mC8 = v_xmm3;
    v_stack_mB8 = v_xmm4;
    v_stack_mA8 = v_xmm5;
    if ((*(unsigned __int8 *)(gs_base + (0 + 34778))) != 0) {
        result = KeWakeProcessor(a1, a2, a3, a4);
    }
    if ((v_rip - 12269) >= v_stack_p0) goto loc_006BD586;
    result = v_rip - 12260;
    if ((v_rip - 12260) >= v_stack_p0) {
        a1 = v_stack_m168;
        result = KiCheckForSListAddress(a1, a2, a3, a4);
    }
    v_rsi = 0;
    if (((*(unsigned __int8 *)(v_rip + 9475673)) & (255)) != 0) {
    }
    if ((*(unsigned int *)(v_rip + 9475960)) == 0) goto loc_006BD5B1;
    result = KzSetIrqlUnsafe(15, a2, a3, a4);
    goto loc_006BD5B9;
loc_006BD5B1:
loc_006BD5B9:
    v_stack_m13F = (unsigned __int8)(v_cr8);
    result = KiMcheckFastForward(v_stack_m168, 1, a3, a4);
    if ((*(unsigned int *)(v_rip + 9475960)) < 0) goto loc_006BD806;
    if (((v_stack_p8) & (1)) != 0) goto loc_006BD605;
    if ((v_rip - 552) > v_stack_p0) goto loc_006BD605;
    if ((v_rip + 526) > v_stack_p0) goto loc_006BD806;
loc_006BD605:
    if ((v_rip + 5299252) > v_stack_p0) goto loc_006BD629;
    if ((v_rip + 5299353) > v_stack_p0) goto loc_006BD806;
loc_006BD629:
    result = KxNmiInterrupt(v_stack_m168, 1, a3, a4);
    if ((*(unsigned int *)(v_rip + 9475806)) == 0) goto loc_006BD64B;
    result = KzSetIrqlUnsafe(v_stack_m13F, 1, a3, a4);
    goto loc_006BD64F;
loc_006BD64B:
loc_006BD64F:
    if (((v_stack_p8) & (1)) == 0) goto loc_006BD772;
    if (((*(unsigned __int8 *)(v_rip + 9475462)) & (255)) != 0) {
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006BD694;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, 1, a3, a4);
    }
    if (v_stack_m68 >= 0) goto loc_006BD6E1;
    a1 = 0;
    a3 = (*(unsigned __int64 *)(gs_base + (0 + 40232))) + (8);
    if (0 == a3) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 40224));
    }
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = (unsigned __int8)(v_stack_m140);
    result = v_stack_m140;
    if ((*(unsigned __int16 *)(gs_base + (0 + 2154))) != 0) {
        result = v_stack_m28;
        a1 = 72;
        a2 = 0;
    }
    v_rsp = (v_stack_mE8) + (232);
    if (((*(unsigned __int8 *)(v_rip + 11813100)) & (1)) == 0) goto loc_006BD75B;
loc_006BD75B:
    if (((*(unsigned __int16 *)(gs_base + (0 + 2136))) & (512)) != 0) {
    }
loc_006BD772:
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = (unsigned __int8)(v_stack_m140);
    result = v_stack_m140;
    if ((*(unsigned __int16 *)(gs_base + (0 + 2154))) != 0) {
        result = v_stack_m28;
        a1 = 72;
        a2 = 0;
    }
    v_rsp = (v_stack_m10) + (232);
    if (((*(unsigned __int8 *)(v_rip + 11812931)) & (1)) == 0) goto loc_006BD804;
loc_006BD804:
loc_006BD806:
    v_r10 = 0;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KiBugCheckDispatch(273, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiNmiInterrupt(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint8_t v_stack_m13D;
    uint8_t v_stack_m13F;
    uint8_t v_stack_m140;
    uint64_t v_stack_m168;
    uint64_t v_stack_m18;
    uint32_t v_stack_m28;
    uint16_t v_stack_m68;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF6;
    uint64_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p0;
    uint16_t v_stack_p20;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (8);
    local_rsp = (local_rsp) - (336);
    v_stack_m13D = 0;
    v_stack_m138 = result;
    v_stack_m130 = Arg1;
    v_stack_m128 = Arg2;
    v_stack_m120 = Arg3;
    v_stack_m118 = Arg4;
    v_stack_m110 = local_r10;
    v_stack_m108 = local_r11;
    if (((v_stack_p8) & (1)) != 0) goto loc_006BD4A0;
    Arg2 = 0;
    v_stack_m90 = 0;
    v_stack_m100 = (uint32_t)(result);
    v_stack_mFC = 0;
    if (condition_is_equal) goto loc_006BD452;
    if (((*(uint32_t *)(v_rip + 0x909706)) & (4)) != 0) goto loc_006BD441;
    goto loc_006BD482;
loc_006BD441:
    Arg1 = (uint32_t)(((uint32_t)(0xC0000101ULL)) >> (8));
    Arg1 = (uint32_t)((Arg1) << (6));
    goto loc_006BD463;
loc_006BD452:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)((uint32_t)(0xC0000101ULL))))) & (0x3FFULL));
    Arg3 = (uint32_t)((Arg3) << (6));
    result = (uint32_t)(((uint8_t)((uint32_t)(0xC0000101ULL))) >> (14));
loc_006BD463:
    result = (uint32_t)((result) | ((uint32_t)(Arg3)));
    Arg2 = (*(uint64_t *)(v_rip + 0x90B7D6 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x865D47) + result * 4)) * 8)) - (384);
loc_006BD482:
    Arg2 = (Arg2) >> (32);
    v_stack_m98 = v_cr2;
    result = KiSetSpecCtrlNmi((uint32_t)(0xC0000101ULL), Arg2, Arg3, Arg4);
    goto loc_006BD527;
loc_006BD4A0:
    if (((*(uint8_t *)(v_rip + 0xB44399)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006BD4DC;
    local_r10 = (*(uint64_t *)(gs_base + (0 + 0x9D20))) + (8);
    if (Arg2 == local_r10) {
    }
    result = KiSetSpecCtrlNmi(*(uint64_t *)(gs_base + (0 + 0x9D28)), Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x909D73)) == 0) goto loc_006BD512;
    if (((uint32_t)(Arg2)) == 0) goto loc_006BD512;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x909D5D)));
    if (((uint32_t)(Arg2)) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) {
        Arg1 = 0x6A7ULL;
    }
    v_stack_m68 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3)) & (3)) != 0) {
        result = KiSaveDebugRegisterState(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm1;
    v_stack_mD8 = v_xmm2;
    v_stack_mC8 = v_xmm3;
    v_stack_mB8 = v_xmm4;
    v_stack_mA8 = v_xmm5;
    if ((*(uint8_t *)(gs_base + (0 + 0x87DA))) != 0) {
        result = KeWakeProcessor(Arg1, Arg2, Arg3, Arg4);
    }
    if ((v_rip - 12269) >= v_stack_p0) goto loc_006BD586;
    result = v_rip - 12260;
    if ((v_rip - 12260) >= v_stack_p0) {
        Arg1 = v_stack_m168;
        result = KiCheckForSListAddress(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = 0;
    if (((*(uint8_t *)(v_rip + 0x909659)) & (255)) != 0) {
    }
    if ((*(uint32_t *)(v_rip + 0x909778)) == 0) goto loc_006BD5B1;
    result = KzSetIrqlUnsafe(15, Arg2, Arg3, Arg4);
    goto loc_006BD5B9;
loc_006BD5B1:
loc_006BD5B9:
    v_stack_m13F = (uint8_t)(v_cr8);
    result = KiMcheckFastForward(v_stack_m168, 1, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x909778)) < 0) goto loc_006BD806;
    if (((v_stack_p8) & (1)) != 0) goto loc_006BD605;
    if ((v_rip - 552) > v_stack_p0) goto loc_006BD605;
    if ((v_rip + 526) > v_stack_p0) goto loc_006BD806;
loc_006BD605:
    if ((v_rip + 5299252) > v_stack_p0) goto loc_006BD629;
    if ((v_rip + 5299353) > v_stack_p0) goto loc_006BD806;
loc_006BD629:
    result = KxNmiInterrupt(v_stack_m168, 1, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x9096DE)) == 0) goto loc_006BD64B;
    result = KzSetIrqlUnsafe(v_stack_m13F, 1, Arg3, Arg4);
    goto loc_006BD64F;
loc_006BD64B:
loc_006BD64F:
    if (((v_stack_p8) & (1)) == 0) goto loc_006BD772;
    if (((*(uint8_t *)(v_rip + 0x909586)) & (255)) != 0) {
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006BD694;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, 1, Arg3, Arg4);
    }
    if (v_stack_m68 >= 0) goto loc_006BD6E1;
    Arg1 = 0;
    Arg3 = (*(uint64_t *)(gs_base + (0 + 0x9D28))) + (8);
    if (0 == Arg3) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x9D20));
    }
    *(uint8_t *)(gs_base + (0 + 0x85E)) = (uint8_t)(v_stack_m140);
    result = v_stack_m140;
    if ((*(uint16_t *)(gs_base + (0 + 0x86A))) != 0) {
        result = v_stack_m28;
        Arg1 = 72;
        Arg2 = 0;
    }
    local_rsp = (v_stack_mE8) + (232);
    if (((*(uint8_t *)(v_rip + 0xB440EC)) & (1)) == 0) goto loc_006BD75B;
loc_006BD75B:
    if (((*(uint16_t *)(gs_base + (0 + 0x858))) & (512)) != 0) {
    }
loc_006BD772:
    *(uint8_t *)(gs_base + (0 + 0x85E)) = (uint8_t)(v_stack_m140);
    result = v_stack_m140;
    if ((*(uint16_t *)(gs_base + (0 + 0x86A))) != 0) {
        result = v_stack_m28;
        Arg1 = 72;
        Arg2 = 0;
    }
    local_rsp = (v_stack_m10) + (232);
    if (((*(uint8_t *)(v_rip + 0xB44043)) & (1)) == 0) goto loc_006BD804;
loc_006BD804:
loc_006BD806:
    local_r10 = 0;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KiBugCheckDispatch(273, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006BD3C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
