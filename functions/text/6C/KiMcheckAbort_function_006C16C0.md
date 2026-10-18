# KiMcheckAbort

- RVA: `0x006C16C0`–`0x006C1CEF` (길이 `1,583` bytes)
- VA: `0x00000001406C16C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1CBC`
- 디코드: `342`개 명령, `1,583/1,583` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x006C1796` → [KiSetSpecCtrlNmi](../6B/KiSetSpecCtrlNmi_function_006B32B0.md) (function, `0x006B32B0`)
- `0x006C17E5` → [KiSetSpecCtrlNmi](../6B/KiSetSpecCtrlNmi_function_006B32B0.md) (function, `0x006B32B0`)
- `0x006C1822` → [KiSaveDebugRegisterState](../4F/KiSaveDebugRegisterState_function_004FD960.md) (function, `0x004FD960`)
- `0x006C1858` → [KeWakeProcessor](../5B/KeWakeProcessor_function_005BE080.md) (function, `0x005BE080`)
- `0x006C1881` → [KiCheckForSListAddress](../40/KiCheckForSListAddress_function_0040B810.md) (function, `0x0040B810`)
- `0x006C18AA` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006C18C3` → [KiMcheckFastForward](../5C/KiMcheckFastForward_function_005CB550.md) (function, `0x005CB550`)
- `0x006C1994` → [KxMcheckAbort](KxMcheckAbort_function_006C1D00.md) (function, `0x006C1D00`)
- `0x006C19CF` → [KzSetIrqlUnsafe](../5B/KzSetIrqlUnsafe_function_005B8AE0.md) (function, `0x005B8AE0`)
- `0x006C1A28` → [KiCopyCounters](../5C/KiCopyCounters_function_005C0710.md) (function, `0x005C0710`)
- `0x006C1A44` → [KiRestoreDebugRegisterState](../4F/KiRestoreDebugRegisterState_function_004FD8E0.md) (function, `0x004FD8E0`)
- `0x006C1AAE` → [KiKernelShadowStackAssistMceAlternateReturn](../5C/KiKernelShadowStackAssistMceAlternateReturn_function_005C8220.md) (function, `0x005C8220`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006C1724` → RVA `0x00FC6B34` (`ALMOSTRO`; read)
- `0x006C1763` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x006C176A` → RVA `0x00F231B8` (`.data`; read)
- `0x006C17A0` → RVA `0x01201840` (`CFGRO`; read)
- `0x006C17EA` → RVA `0x00FC7264` (`ALMOSTRO`; read)
- `0x006C185D` → RVA `0x006BA577` (`ExpInterlockedPopEntrySListResume`; read)
- `0x006C186D` → RVA `0x006BA590` (`ExpInterlockedPopEntrySListEnd`; read)
- `0x006C1890` → RVA `0x00FC6BF0` (`ALMOSTRO`; read)
- `0x006C18A1` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x006C18F6` → RVA `0x00FC5060` (`ALMOSTRO`; read)
- `0x006C1952` → RVA `0x00F10770` (`.data`; read/write)
- `0x006C1981` → RVA `0x00F10720` (`.data`; read/write)
- `0x006C1B17` → RVA `0x006C1E00` (`KxMcheckAlternateReturn`; read)
- `0x006C1BBB` → RVA `0x00BCBA40` (`KxMcheckAlternateReturnShadow`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x006C1C47` → [KiKernelIstMceExit](../../kvascode/BC/KiKernelIstMceExit_function_00BCCCC0.md) (`tail-transfer`)
  - `0x006C1C52` → [KiMcheckExit](../6B/KiMcheckExit_function_006B1C20.md) (`tail-transfer`)
  - `0x006C1CE4` → [KiKernelIstMceExit](../../kvascode/BC/KiKernelIstMceExit_function_00BCCCC0.md) (`tail-transfer`)
  - `0x006C1CE9` → [KiMcheckExit](../6B/KiMcheckExit_function_006B1C20.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006C16C0  48 83 EC 08                     sub rsp, 8
006C16C4  55                              push rbp
006C16C5  56                              push rsi
006C16C6  48 81 EC 50 01 00 00            sub rsp, 0x150
006C16CD  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
006C16D5  C6 45 AB 00                     mov byte ptr [rbp - 0x55], 0
006C16D9  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
006C16DD  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
006C16E1  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
006C16E5  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
006C16E9  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
006C16ED  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
006C16F1  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
006C16F5  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C16FC  0F 85 9E 00 00 00               jne 0x1406c17a0
006C1702  33 D2                           xor edx, edx
006C1704  F3 48 0F 1E CA                  rdsspq rdx
006C1709  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
006C170D  B9 01 01 00 C0                  mov ecx, 0xc0000101
006C1712  0F 32                           rdmsr
006C1714  89 45 E8                        mov dword ptr [rbp - 0x18], eax
006C1717  89 55 EC                        mov dword ptr [rbp - 0x14], edx
006C171A  B8 50 00 00 00                  mov eax, 0x50
006C171F  0F 03 C0                        lsl eax, eax
006C1722  74 2E                           je 0x1406c1752
006C1724  F7 05 06 54 90 00 04 00 00 00   test dword ptr [rip + 0x905406], 4
006C172E  75 11                           jne 0x1406c1741
006C1730  0F 01 45 F0                     sgdt [rbp - 0x10]
006C1734  48 8B 55 F2                     mov rdx, qword ptr [rbp - 0xe]
006C1738  48 8B 92 C0 E0 FF FF            mov rdx, qword ptr [rdx - 0x1f40]
006C173F  EB 41                           jmp 0x1406c1782
006C1741  0F 01 F9                        rdtscp
006C1744  0F B6 C1                        movzx eax, cl
006C1747  C1 E9 08                        shr ecx, 8
006C174A  C1 E1 06                        shl ecx, 6
006C174D  44 8B C1                        mov r8d, ecx
006C1750  EB 11                           jmp 0x1406c1763
006C1752  44 8B C0                        mov r8d, eax
006C1755  41 81 E0 FF 03 00 00            and r8d, 0x3ff
006C175C  41 C1 E0 06                     shl r8d, 6
006C1760  C1 E8 0E                        shr eax, 0xe
006C1763  48 8D 0D D6 74 90 00            lea rcx, [rip + 0x9074d6]
006C176A  48 8B 15 47 1A 86 00            mov rdx, qword ptr [rip + 0x861a47]
006C1771  41 0B C0                        or eax, r8d
006C1774  8B 04 82                        mov eax, dword ptr [rdx + rax*4]
006C1777  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
006C177B  48 81 EA 80 01 00 00            sub rdx, 0x180
006C1782  8B C2                           mov eax, edx
006C1784  48 C1 EA 20                     shr rdx, 0x20
006C1788  B9 01 01 00 C0                  mov ecx, 0xc0000101
006C178D  0F 30                           wrmsr
006C178F  0F 20 D0                        mov rax, cr2
006C1792  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
006C1796  E8 15 1B FF FF                  call 0x1406b32b0
006C179B  E9 87 00 00 00                  jmp 0x1406c1827
006C17A0  F6 05 99 00 B4 00 01            test byte ptr [rip + 0xb40099], 1
006C17A7  75 03                           jne 0x1406c17ac
006C17A9  0F 01 F8                        swapgs
006C17AC  0F AE E8                        lfence
006C17AF  65 48 8B 0C 25 28 9D 00 00      mov rcx, qword ptr gs:[0x9d28]
006C17B8  48 85 C9                        test rcx, rcx
006C17BB  74 1F                           je 0x1406c17dc
006C17BD  F3 48 0F 1E CA                  rdsspq rdx
006C17C2  65 4C 8B 14 25 20 9D 00 00      mov r10, qword ptr gs:[0x9d20]
006C17CB  49 83 C2 08                     add r10, 8
006C17CF  49 3B D2                        cmp rdx, r10
006C17D2  75 08                           jne 0x1406c17dc
006C17D4  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C17D8  F3 0F 01 EA                     saveprevssp
006C17DC  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
006C17E5  E8 C6 1A FF FF                  call 0x1406b32b0
006C17EA  83 3D 73 5A 90 00 00            cmp dword ptr [rip + 0x905a73], 0
006C17F1  74 1F                           je 0x1406c1812
006C17F3  B9 A7 06 00 00                  mov ecx, 0x6a7
006C17F8  0F 32                           rdmsr
006C17FA  83 FA 00                        cmp edx, 0
006C17FD  74 13                           je 0x1406c1812
006C17FF  8B CA                           mov ecx, edx
006C1801  23 15 5D 5A 90 00               and edx, dword ptr [rip + 0x905a5d]
006C1807  3B D1                           cmp edx, ecx
006C1809  74 07                           je 0x1406c1812
006C180B  B9 A7 06 00 00                  mov ecx, 0x6a7
006C1810  0F 30                           wrmsr
006C1812  41 F6 42 03 03                  test byte ptr [r10 + 3], 3
006C1817  66 C7 85 80 00 00 00 00 00      mov word ptr [rbp + 0x80], 0
006C1820  74 05                           je 0x1406c1827
006C1822  E8 39 C1 E3 FF                  call 0x1404fd960
006C1827  FC                              cld
006C1828  0F AE 5D AC                     stmxcsr dword ptr [rbp - 0x54]
006C182C  65 0F AE 14 25 80 01 00 00      ldmxcsr dword ptr gs:[0x180]
006C1835  0F 29 45 F0                     movaps xmmword ptr [rbp - 0x10], xmm0
006C1839  0F 29 4D 00                     movaps xmmword ptr [rbp], xmm1
006C183D  0F 29 55 10                     movaps xmmword ptr [rbp + 0x10], xmm2
006C1841  0F 29 5D 20                     movaps xmmword ptr [rbp + 0x20], xmm3
006C1845  0F 29 65 30                     movaps xmmword ptr [rbp + 0x30], xmm4
006C1849  0F 29 6D 40                     movaps xmmword ptr [rbp + 0x40], xmm5
006C184D  65 80 3C 25 DA 87 00 00 00      cmp byte ptr gs:[0x87da], 0
006C1856  74 05                           je 0x1406c185d
006C1858  E8 23 C8 EF FF                  call 0x1405be080
006C185D  48 8D 05 13 8D FF FF            lea rax, [rip - 0x72ed]
006C1864  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006C186B  73 19                           jae 0x1406c1886
006C186D  48 8D 05 1C 8D FF FF            lea rax, [rip - 0x72e4]
006C1874  48 3B 85 E8 00 00 00            cmp rax, qword ptr [rbp + 0xe8]
006C187B  72 09                           jb 0x1406c1886
006C187D  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006C1881  E8 8A 9F D4 FF                  call 0x14040b810
006C1886  33 F6                           xor esi, esi
006C1888  65 FF 04 25 C0 87 00 00         inc dword ptr gs:[0x87c0]
006C1890  F6 05 59 53 90 00 FF            test byte ptr [rip + 0x905359], 0xff
006C1897  74 03                           je 0x1406c189c
006C1899  0F 01 CA                        clac
006C189C  B9 0F 00 00 00                  mov ecx, 0xf
006C18A1  83 3D 78 54 90 00 00            cmp dword ptr [rip + 0x905478], 0
006C18A8  74 07                           je 0x1406c18b1
006C18AA  E8 31 72 EF FF                  call 0x1405b8ae0
006C18AF  EB 08                           jmp 0x1406c18b9
006C18B1  44 0F 20 C0                     mov rax, cr8
006C18B5  44 0F 22 C1                     mov cr8, rcx
006C18B9  88 45 A9                        mov byte ptr [rbp - 0x57], al
006C18BC  FB                              sti
006C18BD  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006C18C1  33 D2                           xor edx, edx
006C18C3  E8 88 9C F0 FF                  call 0x1405cb550
006C18C8  65 FE 04 25 27 85 00 00         inc byte ptr gs:[0x8527]
006C18D0  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C18D7  0F 85 AC 00 00 00               jne 0x1406c1989
006C18DD  48 8B 85 00 01 00 00            mov rax, qword ptr [rbp + 0x100]
006C18E4  65 48 8B 0C 25 08 00 00 00      mov rcx, qword ptr gs:[8]
006C18ED  48 8B 49 34                     mov rcx, qword ptr [rcx + 0x34]
006C18F1  48 3B C1                        cmp rax, rcx
006C18F4  77 22                           ja 0x1406c1918
006C18F6  8B 15 64 37 90 00               mov edx, dword ptr [rip + 0x903764]
006C18FC  49 C7 C0 D0 01 00 00            mov r8, 0x1d0
006C1903  F6 05 36 FF B3 00 01            test byte ptr [rip + 0xb3ff36], 1
006C190A  41 0F 45 D0                     cmovne edx, r8d
006C190E  48 2B CA                        sub rcx, rdx
006C1911  48 3B C1                        cmp rax, rcx
006C1914  76 02                           jbe 0x1406c1918
006C1916  EB 32                           jmp 0x1406c194a
006C1918  F6 05 21 FF B3 00 01            test byte ptr [rip + 0xb3ff21], 1
006C191F  74 39                           je 0x1406c195a
006C1921  65 48 8B 0C 25 08 00 00 00      mov rcx, qword ptr gs:[8]
006C192A  48 8B 49 34                     mov rcx, qword ptr [rcx + 0x34]
006C192E  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
006C1932  48 3B C1                        cmp rax, rcx
006C1935  77 23                           ja 0x1406c195a
006C1937  44 8B 05 22 37 90 00            mov r8d, dword ptr [rip + 0x903722]
006C193E  49 2B C8                        sub rcx, r8
006C1941  48 83 C1 20                     add rcx, 0x20
006C1945  48 3B C1                        cmp rax, rcx
006C1948  76 10                           jbe 0x1406c195a
006C194A  66 83 8D 08 01 00 00 04         or word ptr [rbp + 0x108], 4
006C1952  F0 48 FF 05 16 EE 84 00         lock inc qword ptr [rip + 0x84ee16]
006C195A  48 8B 85 E8 00 00 00            mov rax, qword ptr [rbp + 0xe8]
006C1961  80 38 F4                        cmp byte ptr [rax], 0xf4
006C1964  75 23                           jne 0x1406c1989
006C1966  48 FF C8                        dec rax
006C1969  66 81 38 FB F4                  cmp word ptr [rax], 0xf4fb
006C196E  75 19                           jne 0x1406c1989
006C1970  81 A5 F8 00 00 00 FF FD FF FF   and dword ptr [rbp + 0xf8], 0xfffffdff
006C197A  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
006C1981  F0 48 FF 05 97 ED 84 00         lock inc qword ptr [rip + 0x84ed97]
006C1989  48 83 EC 10                     sub rsp, 0x10
006C198D  4C 8B C4                        mov r8, rsp
006C1990  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006C1994  E8 67 03 00 00                  call 0x1406c1d00
006C1999  F7 04 24 01 00 00 00            test dword ptr [rsp], 1
006C19A0  74 13                           je 0x1406c19b5
006C19A2  66 0F 6F 04 24                  movdqa xmm0, xmmword ptr [rsp]
006C19A7  66 65 0F 7F 04 25 60 88 00 00   movdqa xmmword ptr gs:[0x8860], xmm0
006C19B1  C6 45 AB 01                     mov byte ptr [rbp - 0x55], 1
006C19B5  48 83 C4 10                     add rsp, 0x10
006C19B9  65 FE 0C 25 27 85 00 00         dec byte ptr gs:[0x8527]
006C19C1  FA                              cli
006C19C2  0F B6 4D A9                     movzx ecx, byte ptr [rbp - 0x57]
006C19C6  83 3D 53 53 90 00 00            cmp dword ptr [rip + 0x905353], 0
006C19CD  74 07                           je 0x1406c19d6
006C19CF  E8 0C 71 EF FF                  call 0x1405b8ae0
006C19D4  EB 04                           jmp 0x1406c19da
006C19D6  44 0F 22 C1                     mov cr8, rcx
006C19DA  48 8B B5 D0 00 00 00            mov rsi, qword ptr [rbp + 0xd0]
006C19E1  FA                              cli
006C19E2  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C19E9  75 1A                           jne 0x1406c1a05
006C19EB  80 7D AB 00                     cmp byte ptr [rbp - 0x55], 0
006C19EF  0F 84 62 02 00 00               je 0x1406c1c57
006C19F5  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
006C19FC  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
006C1A00  E9 95 00 00 00                  jmp 0x1406c1a9a
006C1A05  F6 05 E4 51 90 00 FF            test byte ptr [rip + 0x9051e4], 0xff
006C1A0C  74 03                           je 0x1406c1a11
006C1A0E  0F 01 CB                        stac
006C1A11  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C1A1A  F7 01 00 00 01 00               test dword ptr [rcx], 0x10000
006C1A20  74 14                           je 0x1406c1a36
006C1A22  F6 41 02 01                     test byte ptr [rcx + 2], 1
006C1A26  74 0E                           je 0x1406c1a36
006C1A28  E8 E3 EC EF FF                  call 0x1405c0710
006C1A2D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C1A36  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C1A3A  66 83 BD 80 00 00 00 00         cmp word ptr [rbp + 0x80], 0
006C1A42  74 05                           je 0x1406c1a49
006C1A44  E8 97 BE E3 FF                  call 0x1404fd8e0
006C1A49  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
006C1A52  0F BA 61 74 16                  bt dword ptr [rcx + 0x74], 0x16
006C1A57  73 2A                           jae 0x1406c1a83
006C1A59  33 C9                           xor ecx, ecx
006C1A5B  F3 48 0F 1E C9                  rdsspq rcx
006C1A60  65 4C 8B 04 25 28 9D 00 00      mov r8, qword ptr gs:[0x9d28]
006C1A69  49 83 C0 08                     add r8, 8
006C1A6D  49 3B C8                        cmp rcx, r8
006C1A70  75 11                           jne 0x1406c1a83
006C1A72  65 48 8B 0C 25 20 9D 00 00      mov rcx, qword ptr gs:[0x9d20]
006C1A7B  F3 0F 01 29                     rstorssp dword ptr [rcx]
006C1A7F  F3 0F 01 EA                     saveprevssp
006C1A83  80 7D AB 00                     cmp byte ptr [rbp - 0x55], 0
006C1A87  0F 84 45 01 00 00               je 0x1406c1bd2
006C1A8D  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
006C1A96  48 8B 4A 28                     mov rcx, qword ptr [rdx + 0x28]
006C1A9A  33 D2                           xor edx, edx
006C1A9C  F3 48 0F 1E CA                  rdsspq rdx
006C1AA1  48 85 D2                        test rdx, rdx
006C1AA4  74 11                           je 0x1406c1ab7
006C1AA6  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
006C1AAA  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006C1AAE  E8 6D 67 F0 FF                  call 0x1405c8220
006C1AB3  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
006C1AB7  48 83 E9 28                     sub rcx, 0x28
006C1ABB  48 8B 85 E8 00 00 00            mov rax, qword ptr [rbp + 0xe8]
006C1AC2  48 89 01                        mov qword ptr [rcx], rax
006C1AC5  48 0F B7 85 F0 00 00 00         movzx rax, word ptr [rbp + 0xf0]
006C1ACD  48 89 41 08                     mov qword ptr [rcx + 8], rax
006C1AD1  8B 85 F8 00 00 00               mov eax, dword ptr [rbp + 0xf8]
006C1AD7  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
006C1ADB  48 8B 85 00 01 00 00            mov rax, qword ptr [rbp + 0x100]
006C1AE2  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
006C1AE6  48 0F B7 85 08 01 00 00         movzx rax, word ptr [rbp + 0x108]
006C1AEE  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
006C1AF2  F6 85 F0 00 00 00 01            test byte ptr [rbp + 0xf0], 1
006C1AF9  75 36                           jne 0x1406c1b31
006C1AFB  66 C7 85 08 01 00 00 18 00      mov word ptr [rbp + 0x108], 0x18
006C1B04  66 C7 85 F0 00 00 00 10 00      mov word ptr [rbp + 0xf0], 0x10
006C1B0D  81 A5 F8 00 00 00 FF FD FF FF   and dword ptr [rbp + 0xf8], 0xfffffdff
006C1B17  48 8D 05 E2 02 00 00            lea rax, [rip + 0x2e2]
006C1B1E  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
006C1B25  48 89 8D 00 01 00 00            mov qword ptr [rbp + 0x100], rcx
006C1B2C  E9 26 01 00 00                  jmp 0x1406c1c57
006C1B31  66 C7 85 08 01 00 00 18 00      mov word ptr [rbp + 0x108], 0x18
006C1B3A  66 C7 85 F0 00 00 00 10 00      mov word ptr [rbp + 0xf0], 0x10
006C1B43  81 A5 F8 00 00 00 FF FD FF FF   and dword ptr [rbp + 0xf8], 0xfffffdff
006C1B4D  48 8D 05 AC 02 00 00            lea rax, [rip + 0x2ac]
006C1B54  F6 05 E5 FC B3 00 01            test byte ptr [rip + 0xb3fce5], 1
006C1B5B  74 65                           je 0x1406c1bc2
006C1B5D  65 48 8B 04 25 38 00 00 00      mov rax, qword ptr gs:[0x38]
006C1B66  65 48 8B 14 25 00 B0 00 00      mov rdx, qword ptr gs:[0xb000]
006C1B6F  48 0F BA F2 3F                  btr rdx, 0x3f
006C1B74  48 89 90 E8 45 00 00            mov qword ptr [rax + 0x45e8], rdx
006C1B7B  65 48 8B 14 25 18 00 00 00      mov rdx, qword ptr gs:[0x18]
006C1B84  48 89 90 E0 45 00 00            mov qword ptr [rax + 0x45e0], rdx
006C1B8B  48 8D 80 D8 41 00 00            lea rax, [rax + 0x41d8]
006C1B92  48 8B 11                        mov rdx, qword ptr [rcx]
006C1B95  48 89 10                        mov qword ptr [rax], rdx
006C1B98  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
006C1B9C  48 89 50 08                     mov qword ptr [rax + 8], rdx
006C1BA0  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
006C1BA4  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
006C1BA8  48 8B 51 18                     mov rdx, qword ptr [rcx + 0x18]
006C1BAC  48 89 50 18                     mov qword ptr [rax + 0x18], rdx
006C1BB0  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
006C1BB4  48 89 48 20                     mov qword ptr [rax + 0x20], rcx
006C1BB8  48 8B C8                        mov rcx, rax
006C1BBB  48 8D 05 7E 9E 50 00            lea rax, [rip + 0x509e7e]
006C1BC2  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
006C1BC9  48 89 8D 00 01 00 00            mov qword ptr [rbp + 0x100], rcx
006C1BD0  75 27                           jne 0x1406c1bf9
006C1BD2  0F B6 45 A8                     movzx eax, byte ptr [rbp - 0x58]
006C1BD6  65 88 04 25 5E 08 00 00         mov byte ptr gs:[0x85e], al
006C1BDE  66 65 83 3C 25 6A 08 00 00 00   cmp word ptr gs:[0x86a], 0
006C1BE8  74 0F                           je 0x1406c1bf9
006C1BEA  8B 85 C0 00 00 00               mov eax, dword ptr [rbp + 0xc0]
006C1BF0  B9 48 00 00 00                  mov ecx, 0x48
006C1BF5  33 D2                           xor edx, edx
006C1BF7  0F 30                           wrmsr
006C1BF9  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C1BFD  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C1C01  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C1C05  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C1C09  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C1C0D  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C1C11  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C1C15  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C1C19  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C1C1D  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C1C21  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C1C25  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C1C29  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C1C2D  48 8B E5                        mov rsp, rbp
006C1C30  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C1C37  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C1C3E  F6 05 FB FB B3 00 01            test byte ptr [rip + 0xb3fbfb], 1
006C1C45  74 05                           je 0x1406c1c4c
006C1C47  E9 74 B0 50 00                  jmp 0x140bcccc0
006C1C4C  0F 01 F8                        swapgs
006C1C4F  0F AE E8                        lfence
006C1C52  E9 C9 FF FE FF                  jmp 0x1406b1c20
006C1C57  0F AE 55 AC                     ldmxcsr dword ptr [rbp - 0x54]
006C1C5B  0F 28 45 F0                     movaps xmm0, xmmword ptr [rbp - 0x10]
006C1C5F  0F 28 4D 00                     movaps xmm1, xmmword ptr [rbp]
006C1C63  0F 28 55 10                     movaps xmm2, xmmword ptr [rbp + 0x10]
006C1C67  0F 28 5D 20                     movaps xmm3, xmmword ptr [rbp + 0x20]
006C1C6B  0F 28 65 30                     movaps xmm4, xmmword ptr [rbp + 0x30]
006C1C6F  0F 28 6D 40                     movaps xmm5, xmmword ptr [rbp + 0x40]
006C1C73  0F B6 45 A8                     movzx eax, byte ptr [rbp - 0x58]
006C1C77  65 88 04 25 5E 08 00 00         mov byte ptr gs:[0x85e], al
006C1C7F  66 65 83 3C 25 6A 08 00 00 00   cmp word ptr gs:[0x86a], 0
006C1C89  74 0F                           je 0x1406c1c9a
006C1C8B  8B 85 C0 00 00 00               mov eax, dword ptr [rbp + 0xc0]
006C1C91  B9 48 00 00 00                  mov ecx, 0x48
006C1C96  33 D2                           xor edx, edx
006C1C98  0F 30                           wrmsr
006C1C9A  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
006C1C9D  8B 55 EC                        mov edx, dword ptr [rbp - 0x14]
006C1CA0  B9 01 01 00 C0                  mov ecx, 0xc0000101
006C1CA5  0F 30                           wrmsr
006C1CA7  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
006C1CAB  0F 22 D0                        mov cr2, rax
006C1CAE  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
006C1CB2  4C 8B 55 D8                     mov r10, qword ptr [rbp - 0x28]
006C1CB6  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
006C1CBA  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
006C1CBE  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
006C1CC2  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
006C1CC6  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
006C1CCA  48 8B E5                        mov rsp, rbp
006C1CCD  48 8B AD D8 00 00 00            mov rbp, qword ptr [rbp + 0xd8]
006C1CD4  48 81 C4 E8 00 00 00            add rsp, 0xe8
006C1CDB  F6 05 5E FB B3 00 01            test byte ptr [rip + 0xb3fb5e], 1
006C1CE2  74 05                           je 0x1406c1ce9
006C1CE4  E9 D7 AF 50 00                  jmp 0x140bcccc0
006C1CE9  E9 32 FF FE FF                  jmp 0x1406b1c20
006C1CEE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiMcheckAbort(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m178;
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
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006C17A0;
    a2 = 0;
    v_stack_m90 = 0;
    v_stack_m100 = (unsigned int)(result);
    v_stack_mFC = 0;
    if (condition_is_equal) goto loc_006C1752;
    if (((*(unsigned int *)(v_rip + 9458694)) & (4)) != 0) goto loc_006C1741;
    goto loc_006C1782;
loc_006C1741:
    a1 = (unsigned int)(((unsigned int)(0xC0000101ULL)) >> (8));
    a1 = (unsigned int)((a1) << (6));
    goto loc_006C1763;
loc_006C1752:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)((unsigned int)(0xC0000101ULL))))) & (0x3FFULL));
    a3 = (unsigned int)((a3) << (6));
    result = (unsigned int)(((unsigned __int8)((unsigned int)(0xC0000101ULL))) >> (14));
loc_006C1763:
    result = (unsigned int)((result) | ((unsigned int)(a3)));
    a2 = (*(unsigned __int64 *)(v_rip + 9467094 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8788551) + result * 4)) * 8)) - (384);
loc_006C1782:
    a2 = (a2) >> (32);
    v_stack_m98 = v_cr2;
    result = KiSetSpecCtrlNmi((unsigned int)(0xC0000101ULL), a2, a3, a4);
    goto loc_006C1827;
loc_006C17A0:
    if (((*(unsigned __int8 *)(v_rip + 11796633)) & (1)) == 0) {
    }
    if (*(unsigned __int64 *)(gs_base + (0 + 40232)) == 0) goto loc_006C17DC;
    v_r10 = (*(unsigned __int64 *)(gs_base + (0 + 40224))) + (8);
    if (a2 == v_r10) {
    }
    result = KiSetSpecCtrlNmi(*(unsigned __int64 *)(gs_base + (0 + 40232)), a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 9460339)) == 0) goto loc_006C1812;
    if (((unsigned int)(a2)) == 0) goto loc_006C1812;
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_rip + 9460317)));
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
    if ((v_rip - 29421) >= v_stack_p0) goto loc_006C1886;
    result = v_rip - 29412;
    if ((v_rip - 29412) >= v_stack_p0) {
        a1 = v_stack_m168;
        result = KiCheckForSListAddress(a1, a2, a3, a4);
    }
    v_rsi = 0;
    if (((*(unsigned __int8 *)(v_rip + 9458521)) & (255)) != 0) {
    }
    if ((*(unsigned int *)(v_rip + 9458808)) == 0) goto loc_006C18B1;
    result = KzSetIrqlUnsafe(15, a2, a3, a4);
    goto loc_006C18B9;
loc_006C18B1:
loc_006C18B9:
    v_stack_m13F = (unsigned __int8)(v_cr8);
    a2 = 0;
    result = KiMcheckFastForward(v_stack_m168, a2, a3, a4);
    if (((v_stack_p8) & (1)) != 0) goto loc_006C1989;
    if (v_stack_p18 > (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 8)) + 52))) goto loc_006C1918;
    a2 = (unsigned int)(*(unsigned int *)(v_rip + 9451364));
    if (((*(unsigned __int8 *)(v_rip + 11796278)) & (1)) != 0) { a2 = 464; }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 8)) + 52)) - (a2);
    if (v_stack_p18 <= a1) goto loc_006C1918;
    goto loc_006C194A;
loc_006C1918:
    if (((*(unsigned __int8 *)(v_rip + 11796257)) & (1)) == 0) goto loc_006C195A;
    if (v_stack_p18 > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 8)) + 52) + 8))) goto loc_006C195A;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 8)) + 52) + 8)) - ((unsigned int)(*(unsigned int *)(v_rip + 9451298)));
    a1 = (a1) + (32);
    if (v_stack_p18 >= = a1) {
    }
    if ((*(unsigned __int8 *)(v_stack_p0)) != 244) goto loc_006C1989;
    result = (v_stack_p0) - 1;
    if ((*(unsigned __int16 *)(result)) == 0xF4FBULL) {
        v_stack_p0 = result;
    }
    v_rsp = (v_rsp) - (16);
    result = KxMcheckAbort(v_stack_m168, a2, v_rsp, a4);
    if (((v_stack_m178) & (1)) != 0) {
        *(unsigned __int64 *)(gs_base + (0 + 34912)) = v_xmm0;
        v_stack_m13D = 1;
    }
    v_rsp = (v_rsp) + (16);
    if ((*(unsigned int *)(v_rip + 9458515)) == 0) goto loc_006C19D6;
    result = KzSetIrqlUnsafe(v_stack_m13F, a2, v_rsp, a4);
    goto loc_006C19DA;
loc_006C19D6:
loc_006C19DA:
    if (((v_stack_p8) & (1)) != 0) goto loc_006C1A05;
    if (v_stack_m13D == 0) goto loc_006C1C57;
    a1 = (v_stack_p18) & (-16);
    goto loc_006C1A9A;
loc_006C1A05:
    if (((*(unsigned __int8 *)(v_rip + 9458148)) & (255)) != 0) {
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)))) & (0x10000ULL)) == 0) goto loc_006C1A36;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 2)) & (1)) != 0) {
        result = KiCopyCounters(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_rsp, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(a1, a2, v_rsp, a4);
    }
    if (v_stack_m68 >= 0) goto loc_006C1A83;
    a1 = 0;
    a3 = (*(unsigned __int64 *)(gs_base + (0 + 40232))) + (8);
    if (0 == a3) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 40224));
    }
    if (v_stack_m13D == 0) goto loc_006C1BD2;
loc_006C1A9A:
    a2 = 0;
    if (0 != 0) {
        v_stack_m148 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 40);
        a1 = v_stack_m168;
        result = KiKernelShadowStackAssistMceAlternateReturn(a1, a2, a3, a4);
        a1 = v_stack_m148;
    }
    a1 = (a1) - (40);
    *(unsigned __int64 *)(a1) = v_stack_p0;
    *(unsigned __int64 *)(a1 + 8) = v_stack_p8;
    *(unsigned __int64 *)(a1 + 16) = (unsigned int)(v_stack_p10);
    *(unsigned __int64 *)(a1 + 24) = v_stack_p18;
    *(unsigned __int64 *)(a1 + 32) = v_stack_p20;
    if (((v_stack_p8) & (1)) != 0) goto loc_006C1B31;
    v_stack_p20 = 24;
    v_stack_p8 = 16;
    v_stack_p0 = v_rip + 738;
    v_stack_p18 = a1;
    goto loc_006C1C57;
loc_006C1B31:
    v_stack_p20 = 24;
    v_stack_p8 = 16;
    result = v_rip + 684;
    if (((*(unsigned __int8 *)(v_rip + 11795685)) & (1)) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 56));
        a2 = *(unsigned __int64 *)(gs_base + (0 + 45056));
        *(unsigned __int64 *)(result + 17896) = a2;
        a2 = *(unsigned __int64 *)(gs_base + (0 + 24));
        *(unsigned __int64 *)(result + 17888) = a2;
        result = result + 16856;
        a2 = *(unsigned __int64 *)(a1);
        *(unsigned __int64 *)(result) = a2;
        a2 = *(unsigned __int64 *)(a1 + 8);
        *(unsigned __int64 *)(result + 8) = a2;
        a2 = *(unsigned __int64 *)(a1 + 16);
        *(unsigned __int64 *)(result + 16) = a2;
        a2 = *(unsigned __int64 *)(a1 + 24);
        *(unsigned __int64 *)(result + 24) = a2;
        a2 = *(unsigned __int64 *)(a1 + 32);
        *(unsigned __int64 *)(result + 32) = a1;
        a1 = result;
        result = v_rip + 5283454;
    }
    v_stack_p0 = result;
    v_stack_p18 = a1;
    if (((*(unsigned __int8 *)(v_rip + 11795685)) & (1)) != 0) goto loc_006C1BF9;
loc_006C1BD2:
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = (unsigned __int8)(v_stack_m140);
    result = v_stack_m140;
    if ((*(unsigned __int16 *)(gs_base + (0 + 2154))) != 0) {
        result = v_stack_m28;
        a1 = 72;
        a2 = 0;
    }
    v_rsp = (v_stack_mE8) + (232);
    if (((*(unsigned __int8 *)(v_rip + 11795451)) & (1)) == 0) goto loc_006C1C4C;
loc_006C1C4C:
loc_006C1C57:
    *(unsigned __int8 *)(gs_base + (0 + 2142)) = (unsigned __int8)(v_stack_m140);
    result = v_stack_m140;
    if ((*(unsigned __int16 *)(gs_base + (0 + 2154))) != 0) {
        result = v_stack_m28;
        a1 = 72;
        a2 = 0;
    }
    v_rsp = (v_stack_m10) + (232);
    if (((*(unsigned __int8 *)(v_rip + 11795294)) & (1)) == 0) goto loc_006C1CE9;
loc_006C1CE9:
}
```

## 5. (Beta) C Style

```c
int64_t KiMcheckAbort(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
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
    uint64_t v_stack_m148;
    uint64_t v_stack_m168;
    uint32_t v_stack_m178;
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
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
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
    if (((v_stack_p8) & (1)) != 0) goto loc_006C17A0;
    Arg2 = 0;
    v_stack_m90 = 0;
    v_stack_m100 = (uint32_t)(result);
    v_stack_mFC = 0;
    if (condition_is_equal) goto loc_006C1752;
    if (((*(uint32_t *)(v_rip + 0x905406)) & (4)) != 0) goto loc_006C1741;
    goto loc_006C1782;
loc_006C1741:
    Arg1 = (uint32_t)(((uint32_t)(0xC0000101ULL)) >> (8));
    Arg1 = (uint32_t)((Arg1) << (6));
    goto loc_006C1763;
loc_006C1752:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)((uint32_t)(0xC0000101ULL))))) & (0x3FFULL));
    Arg3 = (uint32_t)((Arg3) << (6));
    result = (uint32_t)(((uint8_t)((uint32_t)(0xC0000101ULL))) >> (14));
loc_006C1763:
    result = (uint32_t)((result) | ((uint32_t)(Arg3)));
    Arg2 = (*(uint64_t *)(v_rip + 0x9074D6 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x861A47) + result * 4)) * 8)) - (384);
loc_006C1782:
    Arg2 = (Arg2) >> (32);
    v_stack_m98 = v_cr2;
    result = KiSetSpecCtrlNmi((uint32_t)(0xC0000101ULL), Arg2, Arg3, Arg4);
    goto loc_006C1827;
loc_006C17A0:
    if (((*(uint8_t *)(v_rip + 0xB40099)) & (1)) == 0) {
    }
    if (*(uint64_t *)(gs_base + (0 + 0x9D28)) == 0) goto loc_006C17DC;
    local_r10 = (*(uint64_t *)(gs_base + (0 + 0x9D20))) + (8);
    if (Arg2 == local_r10) {
    }
    result = KiSetSpecCtrlNmi(*(uint64_t *)(gs_base + (0 + 0x9D28)), Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x905A73)) == 0) goto loc_006C1812;
    if (((uint32_t)(Arg2)) == 0) goto loc_006C1812;
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(v_rip + 0x905A5D)));
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
    if ((v_rip - 29421) >= v_stack_p0) goto loc_006C1886;
    result = v_rip - 29412;
    if ((v_rip - 29412) >= v_stack_p0) {
        Arg1 = v_stack_m168;
        result = KiCheckForSListAddress(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = 0;
    if (((*(uint8_t *)(v_rip + 0x905359)) & (255)) != 0) {
    }
    if ((*(uint32_t *)(v_rip + 0x905478)) == 0) goto loc_006C18B1;
    result = KzSetIrqlUnsafe(15, Arg2, Arg3, Arg4);
    goto loc_006C18B9;
loc_006C18B1:
loc_006C18B9:
    v_stack_m13F = (uint8_t)(v_cr8);
    Arg2 = 0;
    result = KiMcheckFastForward(v_stack_m168, Arg2, Arg3, Arg4);
    if (((v_stack_p8) & (1)) != 0) goto loc_006C1989;
    if (v_stack_p18 > (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x8)) + 0x34))) goto loc_006C1918;
    Arg2 = (uint32_t)(*(uint32_t *)(v_rip + 0x903764));
    if (((*(uint8_t *)(v_rip + 0xB3FF36)) & (1)) != 0) { Arg2 = 464; }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x8)) + 0x34)) - (Arg2);
    if (v_stack_p18 <= Arg1) goto loc_006C1918;
    goto loc_006C194A;
loc_006C1918:
    if (((*(uint8_t *)(v_rip + 0xB3FF21)) & (1)) == 0) goto loc_006C195A;
    if (v_stack_p18 > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x8)) + 0x34) + 0x8))) goto loc_006C195A;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x8)) + 0x34) + 0x8)) - ((uint32_t)(*(uint32_t *)(v_rip + 0x903722)));
    Arg1 = (Arg1) + (32);
    if (v_stack_p18 >= = Arg1) {
    }
    if ((*(uint8_t *)(v_stack_p0)) != 244) goto loc_006C1989;
    result = (v_stack_p0) - 1;
    if ((*(uint16_t *)(result)) == 0xF4FBULL) {
        v_stack_p0 = result;
    }
    local_rsp = (local_rsp) - (16);
    result = KxMcheckAbort(v_stack_m168, Arg2, local_rsp, Arg4);
    if (((v_stack_m178) & (1)) != 0) {
        *(uint64_t *)(gs_base + (0 + 0x8860)) = v_xmm0;
        v_stack_m13D = 1;
    }
    local_rsp = (local_rsp) + (16);
    if ((*(uint32_t *)(v_rip + 0x905353)) == 0) goto loc_006C19D6;
    result = KzSetIrqlUnsafe(v_stack_m13F, Arg2, local_rsp, Arg4);
    goto loc_006C19DA;
loc_006C19D6:
loc_006C19DA:
    if (((v_stack_p8) & (1)) != 0) goto loc_006C1A05;
    if (v_stack_m13D == 0) goto loc_006C1C57;
    Arg1 = (v_stack_p18) & (-16);
    goto loc_006C1A9A;
loc_006C1A05:
    if (((*(uint8_t *)(v_rip + 0x9051E4)) & (255)) != 0) {
    }
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)))) & (0x10000ULL)) == 0) goto loc_006C1A36;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2)) & (1)) != 0) {
        result = KiCopyCounters(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, local_rsp, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    if (v_stack_m68 != 0) {
        result = KiRestoreDebugRegisterState(Arg1, Arg2, local_rsp, Arg4);
    }
    if (v_stack_m68 >= 0) goto loc_006C1A83;
    Arg1 = 0;
    Arg3 = (*(uint64_t *)(gs_base + (0 + 0x9D28))) + (8);
    if (0 == Arg3) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x9D20));
    }
    if (v_stack_m13D == 0) goto loc_006C1BD2;
loc_006C1A9A:
    Arg2 = 0;
    if (0 != 0) {
        v_stack_m148 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28);
        Arg1 = v_stack_m168;
        result = KiKernelShadowStackAssistMceAlternateReturn(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m148;
    }
    Arg1 = (Arg1) - (40);
    *(uint64_t *)(Arg1) = v_stack_p0;
    *(uint64_t *)(Arg1 + 0x8) = v_stack_p8;
    *(uint64_t *)(Arg1 + 0x10) = (uint32_t)(v_stack_p10);
    *(uint64_t *)(Arg1 + 0x18) = v_stack_p18;
    *(uint64_t *)(Arg1 + 0x20) = v_stack_p20;
    if (((v_stack_p8) & (1)) != 0) goto loc_006C1B31;
    v_stack_p20 = 24;
    v_stack_p8 = 16;
    v_stack_p0 = v_rip + 738;
    v_stack_p18 = Arg1;
    goto loc_006C1C57;
loc_006C1B31:
    v_stack_p20 = 24;
    v_stack_p8 = 16;
    result = v_rip + 684;
    if (((*(uint8_t *)(v_rip + 0xB3FCE5)) & (1)) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x38));
        Arg2 = *(uint64_t *)(gs_base + (0 + 0xB000));
        *(uint64_t *)(result + 0x45E8) = Arg2;
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x18));
        *(uint64_t *)(result + 0x45E0) = Arg2;
        result = result + 16856;
        Arg2 = *(uint64_t *)(Arg1);
        *(uint64_t *)(result) = Arg2;
        Arg2 = *(uint64_t *)(Arg1 + 0x8);
        *(uint64_t *)(result + 0x8) = Arg2;
        Arg2 = *(uint64_t *)(Arg1 + 0x10);
        *(uint64_t *)(result + 0x10) = Arg2;
        Arg2 = *(uint64_t *)(Arg1 + 0x18);
        *(uint64_t *)(result + 0x18) = Arg2;
        Arg2 = *(uint64_t *)(Arg1 + 0x20);
        *(uint64_t *)(result + 0x20) = Arg1;
        Arg1 = result;
        result = v_rip + 5283454;
    }
    v_stack_p0 = result;
    v_stack_p18 = Arg1;
    if (((*(uint8_t *)(v_rip + 0xB3FCE5)) & (1)) != 0) goto loc_006C1BF9;
loc_006C1BD2:
    *(uint8_t *)(gs_base + (0 + 0x85E)) = (uint8_t)(v_stack_m140);
    result = v_stack_m140;
    if ((*(uint16_t *)(gs_base + (0 + 0x86A))) != 0) {
        result = v_stack_m28;
        Arg1 = 72;
        Arg2 = 0;
    }
    local_rsp = (v_stack_mE8) + (232);
    if (((*(uint8_t *)(v_rip + 0xB3FBFB)) & (1)) == 0) goto loc_006C1C4C;
loc_006C1C4C:
loc_006C1C57:
    *(uint8_t *)(gs_base + (0 + 0x85E)) = (uint8_t)(v_stack_m140);
    result = v_stack_m140;
    if ((*(uint16_t *)(gs_base + (0 + 0x86A))) != 0) {
        result = v_stack_m28;
        Arg1 = 72;
        Arg2 = 0;
    }
    local_rsp = (v_stack_m10) + (232);
    if (((*(uint8_t *)(v_rip + 0xB3FB5E)) & (1)) == 0) goto loc_006C1CE9;
loc_006C1CE9:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006C16C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
