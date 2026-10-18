# KiUpdateRunTime

- RVA: `0x0039BB70`–`0x0039C132` (길이 `1,474` bytes)
- VA: `0x000000014039BB70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00081938`
- 디코드: `317`개 명령, `1,474/1,474` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0039BBCF` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0039BC06` → [KeAccumulateTicks](KeAccumulateTicks_function_0039C140.md) (function, `0x0039C140`)
- `0x0039BC3E` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x0039BD6E` → [KiSetClockTimer](KiSetClockTimer_function_0039DB2C.md) (function, `0x0039DB2C`)
- `0x0039BD84` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039BDC4` → [KiComputeThreadQos](../25/KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x0039BDDD` → [KiCheckPreferredHeteroProcessor](KiCheckPreferredHeteroProcessor_function_0039D72C.md) (function, `0x0039D72C`)
- `0x0039BDED` → [KiCheckForPendingQosUpdate](KiCheckForPendingQosUpdate_function_0039DD48.md) (function, `0x0039DD48`)
- `0x0039BE0E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0039BE5C` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x0039BEC5` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039BF1E` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039BF63` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0039BF99` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039BFBE` → [HalpDisableInterrupts](../25/HalpDisableInterrupts_function_002521A0.md) (function, `0x002521A0`)
- `0x0039C018` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x0039C028` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039C05A` → [KiSetClockTimer](KiSetClockTimer_function_0039DB2C.md) (function, `0x0039DB2C`)
- `0x0039C067` → [KiShouldScanSharedReadyQueue](../46/KiShouldScanSharedReadyQueue_function_00468B50.md) (function, `0x00468B50`)
- `0x0039C070` → [KiShouldScanLocalReadyQueue](../47/KiShouldScanLocalReadyQueue_function_00473F90.md) (function, `0x00473F90`)
- `0x0039C0A0` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039C0C7` → [KiSetDpcRequestFlag](KiSetDpcRequestFlag_function_0039DC50.md) (function, `0x0039DC50`)
- `0x0039C0D1` → [KiRequestSoftwareInterrupt](../25/KiRequestSoftwareInterrupt_function_00250950.md) (function, `0x00250950`)
- `0x0039C0DE` → [KiShouldScanSharedReadyQueue](../46/KiShouldScanSharedReadyQueue_function_00468B50.md) (function, `0x00468B50`)
- `0x0039C125` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)

### Direct callers
- [KeClockInterruptNotify](KeClockInterruptNotify_function_0039A970.md) at `0x0039ADB8`
- [KiUpdateTime](KiUpdateTime_function_0039B530.md) at `0x0039B8BB`

### Static image references
- `0x0039BB97` → RVA `0x00E0A740` (`.data`; read)
- `0x0039BC0B` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x0039BC43` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x0039BD38` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0039BD4F` → RVA `0x00FC6B3C` (`ALMOSTRO`; read)
- `0x0039BD96` → RVA `0x00FC50A0` (`ALMOSTRO`; read)
- `0x0039BE4A` → RVA `0x00FC6AA5` (`ALMOSTRO`; read)
- `0x0039BE61` → RVA `0x00FC6D5C` (`ALMOSTRO`; read)
- `0x0039BE8C` → RVA `0x00E070D8` (`.data`; read)
- `0x0039BFA8` → RVA `0x00FC6BC5` (`ALMOSTRO`; read)
- `0x0039C085` → RVA `0x00FC50C8` (`ALMOSTRO`; read)
- `0x0039C10C` → RVA `0x00FC51C4` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0039BE93` → [sub_006E5CE6](../6E/Unknown_function_006E5CE6.md) (`tail-transfer`)
  - `0x0039BF07` → [sub_006E5CE6 + 0xE9](../6E/Unknown_function_006E5CE6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0039BB70  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0039BB75  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0039BB7A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0039BB7F  55                              push rbp
0039BB80  41 54                           push r12
0039BB82  41 55                           push r13
0039BB84  41 56                           push r14
0039BB86  41 57                           push r15
0039BB88  48 8D AC 24 70 FF FF FF         lea rbp, [rsp - 0x90]
0039BB90  48 81 EC 90 01 00 00            sub rsp, 0x190
0039BB97  48 8B 05 A2 EB A6 00            mov rax, qword ptr [rip + 0xa6eba2]
0039BB9E  48 33 C4                        xor rax, rsp
0039BBA1  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
0039BBA8  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
0039BBB1  45 33 ED                        xor r13d, r13d
0039BBB4  41 8B F8                        mov edi, r8d
0039BBB7  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
0039BBBC  0F B6 F2                        movzx esi, dl
0039BBBF  44 0F B6 F9                     movzx r15d, cl
0039BBC3  FF 83 C4 38 00 00               inc dword ptr [rbx + 0x38c4]
0039BBC9  FF 83 A0 2D 00 00               inc dword ptr [rbx + 0x2da0]
0039BBCF  E8 0C C0 E7 FF                  call 0x140217be0
0039BBD4  48 B9 20 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000320
0039BBDE  44 8B 31                        mov r14d, dword ptr [rcx]
0039BBE1  44 8B A3 C0 38 00 00            mov r12d, dword ptr [rbx + 0x38c0]
0039BBE8  84 C0                           test al, al
0039BBEA  0F 85 04 01 00 00               jne 0x14039bcf4
0039BBF0  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
0039BBF4  44 0F B6 CE                     movzx r9d, sil
0039BBF8  45 8B C6                        mov r8d, r14d
0039BBFB  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
0039BC00  41 8B D4                        mov edx, r12d
0039BC03  48 8B CB                        mov rcx, rbx
0039BC06  E8 35 05 00 00                  call 0x14039c140
0039BC0B  44 38 2D 73 AE C2 00            cmp byte ptr [rip + 0xc2ae73], r13b
0039BC12  41 BC 0F 00 00 00               mov r12d, 0xf
0039BC18  C7 83 A0 83 00 00 01 00 00 00   mov dword ptr [rbx + 0x83a0], 1
0039BC22  0F 85 0D 02 00 00               jne 0x14039be35
0039BC28  48 8B 73 08                     mov rsi, qword ptr [rbx + 8]
0039BC2C  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
0039BC30  0F 85 60 01 00 00               jne 0x14039bd96
0039BC36  48 8D 4D 80                     lea rcx, [rbp - 0x80]
0039BC3A  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
0039BC3E  E8 7D E8 E6 FF                  call 0x14020a4c0
0039BC43  8B 15 57 AE C2 00               mov edx, dword ptr [rip + 0xc2ae57]
0039BC49  48 B9 20 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000320
0039BC53  48 0F AF 93 D8 8B 00 00         imul rdx, qword ptr [rbx + 0x8bd8]
0039BC5B  48 8B 09                        mov rcx, qword ptr [rcx]
0039BC5E  48 8B F8                        mov rdi, rax
0039BC61  48 3B 8B D8 8B 00 00            cmp rcx, qword ptr [rbx + 0x8bd8]
0039BC68  0F 87 69 02 00 00               ja 0x14039bed7
0039BC6E  48 3B C2                        cmp rax, rdx
0039BC71  0F 87 9C 00 00 00               ja 0x14039bd13
0039BC77  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
0039BC7B  48 85 C0                        test rax, rax
0039BC7E  0F 84 73 01 00 00               je 0x14039bdf7
0039BC84  8B 8B D8 00 00 00               mov ecx, dword ptr [rbx + 0xd8]
0039BC8A  48 03 C8                        add rcx, rax
0039BC8D  8B 83 D8 00 00 00               mov eax, dword ptr [rbx + 0xd8]
0039BC93  4C 8B C1                        mov r8, rcx
0039BC96  0F B7 51 70                     movzx edx, word ptr [rcx + 0x70]
0039BC9A  4C 2B C0                        sub r8, rax
0039BC9D  F6 C2 04                        test dl, 4
0039BCA0  0F 85 C7 02 00 00               jne 0x14039bf6d
0039BCA6  F6 C2 20                        test dl, 0x20
0039BCA9  0F 84 D0 02 00 00               je 0x14039bf7f
0039BCAF  F6 C2 12                        test dl, 0x12
0039BCB2  0F 85 78 02 00 00               jne 0x14039bf30
0039BCB8  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
0039BCBC  48 85 C0                        test rax, rax
0039BCBF  7E 19                           jle 0x14039bcda
0039BCC1  0F B6 41 70                     movzx eax, byte ptr [rcx + 0x70]
0039BCC5  84 C0                           test al, al
0039BCC7  0F 89 63 02 00 00               jns 0x14039bf30
0039BCCD  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0039BCD1  48 39 01                        cmp qword ptr [rcx], rax
0039BCD4  0F 82 56 02 00 00               jb 0x14039bf30
0039BCDA  C6 83 B9 38 00 00 01            mov byte ptr [rbx + 0x38b9], 1
0039BCE1  44 38 6B 20                     cmp byte ptr [rbx + 0x20], r13b
0039BCE5  0F 84 B8 02 00 00               je 0x14039bfa3
0039BCEB  C6 43 06 01                     mov byte ptr [rbx + 6], 1
0039BCEF  E9 10 01 00 00                  jmp 0x14039be04
0039BCF4  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0039BCFD  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0039BD04  4D 85 C0                        test r8, r8
0039BD07  0F 85 38 02 00 00               jne 0x14039bf45
0039BD0D  FB                              sti
0039BD0E  E9 DD FE FF FF                  jmp 0x14039bbf0
0039BD13  44 38 2D 6B AD C2 00            cmp byte ptr [rip + 0xc2ad6b], r13b
0039BD1A  0F 84 57 FF FF FF               je 0x14039bc77
0039BD20  44 38 AB 59 86 00 00            cmp byte ptr [rbx + 0x8659], r13b
0039BD27  41 0F 94 C4                     sete r12b
0039BD2B  45 0F 20 C7                     mov r15, cr8
0039BD2F  B8 0F 00 00 00                  mov eax, 0xf
0039BD34  44 0F 22 C0                     mov cr8, rax
0039BD38  44 39 2D E1 AF C2 00            cmp dword ptr [rip + 0xc2afe1], r13d
0039BD3F  0F 85 54 03 00 00               jne 0x14039c099
0039BD45  44 8B 05 54 AD C2 00            mov r8d, dword ptr [rip + 0xc2ad54]
0039BD4C  48 8B D7                        mov rdx, rdi
0039BD4F  44 8B 0D E6 AD C2 00            mov r9d, dword ptr [rip + 0xc2ade6]
0039BD56  49 F7 D8                        neg r8
0039BD59  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
0039BD5E  48 8B CB                        mov rcx, rbx
0039BD61  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
0039BD66  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
0039BD6E  E8 B9 1D 00 00                  call 0x14039db2c
0039BD73  44 39 2D A6 AF C2 00            cmp dword ptr [rip + 0xc2afa6], r13d
0039BD7A  74 0D                           je 0x14039bd89
0039BD7C  44 0F 20 C1                     mov rcx, cr8
0039BD80  41 0F B6 D7                     movzx edx, r15b
0039BD84  E8 0F 99 15 00                  call 0x1404f5698
0039BD89  41 0F B6 C7                     movzx eax, r15b
0039BD8D  44 0F 22 C0                     mov cr8, rax
0039BD91  E9 E1 FE FF FF                  jmp 0x14039bc77
0039BD96  44 39 2D 03 93 C2 00            cmp dword ptr [rip + 0xc29303], r13d
0039BD9D  75 0D                           jne 0x14039bdac
0039BD9F  44 39 B3 E8 83 00 00            cmp dword ptr [rbx + 0x83e8], r14d
0039BDA6  0F 88 B8 02 00 00               js 0x14039c064
0039BDAC  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
0039BDB0  48 3B 46 20                     cmp rax, qword ptr [rsi + 0x20]
0039BDB4  0F 83 20 FF FF FF               jae 0x14039bcda
0039BDBA  0F B6 BE 04 02 00 00            movzx edi, byte ptr [rsi + 0x204]
0039BDC1  48 8B CE                        mov rcx, rsi
0039BDC4  E8 47 C2 EB FF                  call 0x140258010
0039BDC9  3B F8                           cmp edi, eax
0039BDCB  0F 85 09 FF FF FF               jne 0x14039bcda
0039BDD1  41 B8 01 00 00 00               mov r8d, 1
0039BDD7  48 8B D3                        mov rdx, rbx
0039BDDA  48 8B CE                        mov rcx, rsi
0039BDDD  E8 4A 19 00 00                  call 0x14039d72c
0039BDE2  85 C0                           test eax, eax
0039BDE4  0F 85 F0 FE FF FF               jne 0x14039bcda
0039BDEA  48 8B CE                        mov rcx, rsi
0039BDED  E8 56 1F 00 00                  call 0x14039dd48
0039BDF2  E9 3F FE FF FF                  jmp 0x14039bc36
0039BDF7  44 39 B3 C8 38 00 00            cmp dword ptr [rbx + 0x38c8], r14d
0039BDFE  0F 88 D7 02 00 00               js 0x14039c0db
0039BE04  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
0039BE0B  48 33 CC                        xor rcx, rsp
0039BE0E  E8 2D 08 31 00                  call 0x1406ac640
0039BE13  4C 8D 9C 24 90 01 00 00         lea r11, [rsp + 0x190]
0039BE1B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0039BE1F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0039BE23  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0039BE27  49 8B E3                        mov rsp, r11
0039BE2A  41 5F                           pop r15
0039BE2C  41 5E                           pop r14
0039BE2E  41 5D                           pop r13
0039BE30  41 5C                           pop r12
0039BE32  5D                              pop rbp
0039BE33  C3                              ret
0039BE34  CC                              int3
0039BE35  45 0F 20 C7                     mov r15, cr8
0039BE39  45 0F 22 C4                     mov cr8, r12
0039BE3D  44 39 2D DC AE C2 00            cmp dword ptr [rip + 0xc2aedc], r13d
0039BE44  0F 85 47 01 00 00               jne 0x14039bf91
0039BE4A  44 38 2D 54 AC C2 00            cmp byte ptr [rip + 0xc2ac54], r13b
0039BE51  0F 84 DB 01 00 00               je 0x14039c032
0039BE57  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0039BE5C  E8 5F E6 E6 FF                  call 0x14020a4c0
0039BE61  8B 35 F5 AE C2 00               mov esi, dword ptr [rip + 0xc2aef5]
0039BE67  48 8B C8                        mov rcx, rax
0039BE6A  44 8B 25 CB AC C2 00            mov r12d, dword ptr [rip + 0xc2accb]
0039BE71  48 F7 DE                        neg rsi
0039BE74  44 38 2D 2A AC C2 00            cmp byte ptr [rip + 0xc2ac2a], r13b
0039BE7B  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
0039BE80  0F 84 9A 02 00 00               je 0x14039c120
0039BE86  48 8B F9                        mov rdi, rcx
0039BE89  48 2B FE                        sub rdi, rsi
0039BE8C  83 3D 45 B2 A6 00 05            cmp dword ptr [rip + 0xa6b245], 5
0039BE93  0F 87 4D 9E 34 00               ja 0x1406e5ce6
0039BE99  80 8B D4 95 00 00 03            or byte ptr [rbx + 0x95d4], 3
0039BEA0  44 89 A3 D0 95 00 00            mov dword ptr [rbx + 0x95d0], r12d
0039BEA7  41 BC 0F 00 00 00               mov r12d, 0xf
0039BEAD  48 89 BB C8 95 00 00            mov qword ptr [rbx + 0x95c8], rdi
0039BEB4  44 39 2D 65 AE C2 00            cmp dword ptr [rip + 0xc2ae65], r13d
0039BEBB  74 0D                           je 0x14039beca
0039BEBD  44 0F 20 C1                     mov rcx, cr8
0039BEC1  41 0F B6 D7                     movzx edx, r15b
0039BEC5  E8 CE 97 15 00                  call 0x1404f5698
0039BECA  41 0F B6 C7                     movzx eax, r15b
0039BECE  44 0F 22 C0                     mov cr8, rax
0039BED2  E9 51 FD FF FF                  jmp 0x14039bc28
0039BED7  44 38 2D A7 AB C2 00            cmp byte ptr [rip + 0xc2aba7], r13b
0039BEDE  0F 84 F6 FD FF FF               je 0x14039bcda
0039BEE4  44 0F 20 C7                     mov rdi, cr8
0039BEE8  45 0F 22 C4                     mov cr8, r12
0039BEEC  44 39 2D 2D AE C2 00            cmp dword ptr [rip + 0xc2ae2d], r13d
0039BEF3  0F 85 29 01 00 00               jne 0x14039c022
0039BEF9  80 A3 E4 95 00 00 FE            and byte ptr [rbx + 0x95e4], 0xfe
0039BF00  83 3D D1 B1 A6 00 05            cmp dword ptr [rip + 0xa6b1d1], 5
0039BF07  0F 87 C2 9E 34 00               ja 0x1406e5dcf
0039BF0D  44 39 2D 0C AE C2 00            cmp dword ptr [rip + 0xc2ae0c], r13d
0039BF14  74 0D                           je 0x14039bf23
0039BF16  44 0F 20 C1                     mov rcx, cr8
0039BF1A  40 0F B6 D7                     movzx edx, dil
0039BF1E  E8 75 97 15 00                  call 0x1404f5698
0039BF23  40 0F B6 C7                     movzx eax, dil
0039BF27  44 0F 22 C0                     mov cr8, rax
0039BF2B  E9 AA FD FF FF                  jmp 0x14039bcda
0039BF30  48 8B 89 A0 01 00 00            mov rcx, qword ptr [rcx + 0x1a0]
0039BF37  48 85 C9                        test rcx, rcx
0039BF3A  0F 85 4D FD FF FF               jne 0x14039bc8d
0039BF40  E9 B2 FE FF FF                  jmp 0x14039bdf7
0039BF45  41 0F 0D 08                     prefetchw byte ptr [r8]
0039BF49  41 8B 00                        mov eax, dword ptr [r8]
0039BF4C  8B D0                           mov edx, eax
0039BF4E  0F BA F2 15                     btr edx, 0x15
0039BF52  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0039BF57  75 F3                           jne 0x14039bf4c
0039BF59  0F BA E0 15                     bt eax, 0x15
0039BF5D  0F 83 AA FD FF FF               jae 0x14039bd0d
0039BF63  E8 68 72 EC FF                  call 0x1402631d0
0039BF68  E9 A0 FD FF FF                  jmp 0x14039bd0d
0039BF6D  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0039BF71  48 39 01                        cmp qword ptr [rcx], rax
0039BF74  0F 82 35 FD FF FF               jb 0x14039bcaf
0039BF7A  E9 5B FD FF FF                  jmp 0x14039bcda
0039BF7F  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0039BF83  48 39 01                        cmp qword ptr [rcx], rax
0039BF86  0F 86 23 FD FF FF               jbe 0x14039bcaf
0039BF8C  E9 49 FD FF FF                  jmp 0x14039bcda
0039BF91  41 0F B6 D4                     movzx edx, r12b
0039BF95  41 0F B6 CF                     movzx ecx, r15b
0039BF99  E8 5E 97 15 00                  call 0x1404f56fc
0039BF9E  E9 A7 FE FF FF                  jmp 0x14039be4a
0039BFA3  33 C0                           xor eax, eax
0039BFA5  0F 57 C0                        xorps xmm0, xmm0
0039BFA8  38 05 17 AC C2 00               cmp byte ptr [rip + 0xc2ac17], al
0039BFAE  F3 0F 7F 45 8C                  movdqu xmmword ptr [rbp - 0x74], xmm0
0039BFB3  74 53                           je 0x14039c008
0039BFB5  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
0039BFBE  E8 DD 61 EB FF                  call 0x1402521a0
0039BFC3  41 8B 90 A8 00 00 00            mov edx, dword ptr [r8 + 0xa8]
0039BFCA  44 0F B6 C8                     movzx r9d, al
0039BFCE  8B CA                           mov ecx, edx
0039BFD0  83 C9 04                        or ecx, 4
0039BFD3  41 89 88 A8 00 00 00            mov dword ptr [r8 + 0xa8], ecx
0039BFDA  85 D2                           test edx, edx
0039BFDC  75 24                           jne 0x14039c002
0039BFDE  B9 15 00 01 C0                  mov ecx, 0xc0010015
0039BFE3  0F 32                           rdmsr
0039BFE5  48 C1 E2 20                     shl rdx, 0x20
0039BFE9  48 0B C2                        or rax, rdx
0039BFEC  48 BA 00 00 00 00 01 00 00 00   movabs rdx, 0x100000000
0039BFF6  48 0B C2                        or rax, rdx
0039BFF9  48 8B D0                        mov rdx, rax
0039BFFC  48 C1 EA 20                     shr rdx, 0x20
0039C000  0F 30                           wrmsr
0039C002  45 84 C9                        test r9b, r9b
0039C005  74 01                           je 0x14039c008
0039C007  FB                              sti
0039C008  BA 2F 00 00 00                  mov edx, 0x2f
0039C00D  C7 45 88 05 00 00 00            mov dword ptr [rbp - 0x78], 5
0039C014  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0039C018  E8 F3 62 EB FF                  call 0x140252310
0039C01D  E9 E2 FD FF FF                  jmp 0x14039be04
0039C022  B2 0F                           mov dl, 0xf
0039C024  40 0F B6 CF                     movzx ecx, dil
0039C028  E8 CF 96 15 00                  call 0x1404f56fc
0039C02D  E9 C7 FE FF FF                  jmp 0x14039bef9
0039C032  44 8B 05 23 AD C2 00            mov r8d, dword ptr [rip + 0xc2ad23]
0039C039  33 D2                           xor edx, edx
0039C03B  44 8B 0D FA AA C2 00            mov r9d, dword ptr [rip + 0xc2aafa]
0039C042  49 F7 D8                        neg r8
0039C045  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
0039C04A  48 8B CB                        mov rcx, rbx
0039C04D  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0039C052  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
0039C05A  E8 CD 1A 00 00                  call 0x14039db2c
0039C05F  E9 50 FE FF FF                  jmp 0x14039beb4
0039C064  48 8B CB                        mov rcx, rbx
0039C067  E8 E4 CA 0C 00                  call 0x140468b50
0039C06C  85 C0                           test eax, eax
0039C06E  75 3A                           jne 0x14039c0aa
0039C070  E8 1B 7F 0D 00                  call 0x140473f90
0039C075  85 C0                           test eax, eax
0039C077  74 0C                           je 0x14039c085
0039C079  F7 83 D8 83 00 00 00 03 00 00   test dword ptr [rbx + 0x83d8], 0x300
0039C083  75 36                           jne 0x14039c0bb
0039C085  8B 0D 3D 90 C2 00               mov ecx, dword ptr [rip + 0xc2903d]
0039C08B  41 03 CE                        add ecx, r14d
0039C08E  89 8B E8 83 00 00               mov dword ptr [rbx + 0x83e8], ecx
0039C094  E9 13 FD FF FF                  jmp 0x14039bdac
0039C099  0F B6 D0                        movzx edx, al
0039C09C  41 0F B6 CF                     movzx ecx, r15b
0039C0A0  E8 57 96 15 00                  call 0x1404f56fc
0039C0A5  E9 9B FC FF FF                  jmp 0x14039bd45
0039C0AA  48 8B 83 48 8E 00 00            mov rax, qword ptr [rbx + 0x8e48]
0039C0B1  8B 40 08                        mov eax, dword ptr [rax + 8]
0039C0B4  A9 00 03 00 00                  test eax, 0x300
0039C0B9  74 B5                           je 0x14039c070
0039C0BB  BA 40 00 00 00                  mov edx, 0x40
0039C0C0  48 8D 8B BC 38 00 00            lea rcx, [rbx + 0x38bc]
0039C0C7  E8 84 1B 00 00                  call 0x14039dc50
0039C0CC  B2 02                           mov dl, 2
0039C0CE  48 8B CB                        mov rcx, rbx
0039C0D1  E8 7A 48 EB FF                  call 0x140250950
0039C0D6  E9 D1 FC FF FF                  jmp 0x14039bdac
0039C0DB  48 8B CB                        mov rcx, rbx
0039C0DE  E8 6D CA 0C 00                  call 0x140468b50
0039C0E3  85 C0                           test eax, eax
0039C0E5  74 15                           je 0x14039c0fc
0039C0E7  48 8B 83 48 8E 00 00            mov rax, qword ptr [rbx + 0x8e48]
0039C0EE  8B 40 08                        mov eax, dword ptr [rax + 8]
0039C0F1  A9 FE 7F 00 00                  test eax, 0x7ffe
0039C0F6  0F 85 08 FD FF FF               jne 0x14039be04
0039C0FC  F7 83 D8 83 00 00 FE 7F 00 00   test dword ptr [rbx + 0x83d8], 0x7ffe
0039C106  0F 85 F8 FC FF FF               jne 0x14039be04
0039C10C  8B 0D B2 90 C2 00               mov ecx, dword ptr [rip + 0xc290b2]
0039C112  41 03 CE                        add ecx, r14d
0039C115  89 8B C8 38 00 00               mov dword ptr [rbx + 0x38c8], ecx
0039C11B  E9 E4 FC FF FF                  jmp 0x14039be04
0039C120  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
0039C125  E8 96 E3 E6 FF                  call 0x14020a4c0
0039C12A  48 8B C8                        mov rcx, rax
0039C12D  E9 54 FD FF FF                  jmp 0x14039be86
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiUpdateRunTime(unsigned __int8 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int8 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int8 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int8 v_stack_m198;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 10939298)) ^ (v_rsp);
    v_stack_m38 = result;
    v_r13 = 0;
    v_stack_m168 = 0;
    result = KeDisableInterrupts(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0039BCF4;
loc_0039BBF0:
    v_stack_m190 = (unsigned int)((unsigned int)(a3));
    v_stack_m198 = a1;
    result = KeAccumulateTicks(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14528)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), a2);
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33696) = 1;
    if ((*(unsigned __int8 *)(v_rip + 12758643)) != 0) goto loc_0039BE35;
loc_0039BC28:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) goto loc_0039BD96;
loc_0039BC36:
    v_stack_m138 = 0;
    result = RtlGetInterruptTimePrecise(v_stack_m138, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14528)))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1)))), a2);
    a2 = ((unsigned int)(*(unsigned int *)(v_rip + 12758615))) * (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35800));
    if ((*(unsigned __int64 *)(v_stack_m138)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35800))) goto loc_0039BED7;
    if (result > a2) goto loc_0039BD13;
loc_0039BC77:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 104) == 0) goto loc_0039BDF7;
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 216))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 104));
loc_0039BC8D:
    a3 = (a1) - ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 216)));
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 112))) & (4)) != 0) goto loc_0039BF6D;
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 112))) & (32)) == 0) goto loc_0039BF7F;
loc_0039BCAF:
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 112))) & (18)) != 0) goto loc_0039BF30;
    if (condition_is_less_or_equal) goto loc_0039BCDA;
    if (!sign_flag) goto loc_0039BF30;
    if ((*(unsigned __int64 *)(a1)) < (*(unsigned __int64 *)(a1 + 16))) goto loc_0039BF30;
loc_0039BCDA:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14521) = 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) == 0) goto loc_0039BFA3;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 6) = 1;
    goto loc_0039BE04;
loc_0039BCF4:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0039BF45;
loc_0039BD0D:
    goto loc_0039BBF0;
loc_0039BD13:
    if ((*(unsigned __int8 *)(v_rip + 12758379)) == 0) goto loc_0039BC77;
    v_r12 = ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34393)) == 0) ? 1 : 0;
    if ((*(unsigned int *)(v_rip + 12759009)) != 0) goto loc_0039C099;
loc_0039BD45:
    a3 = -((unsigned int)(*(unsigned int *)(v_rip + 12758356)));
    v_stack_m188 = 0;
    v_stack_m190 = (unsigned __int8)(v_r12);
    v_stack_m198 = 4;
    result = KiSetClockTimer(*(unsigned __int64 *)(gs_base + (0 + 32)), result, a3, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    if ((*(unsigned int *)(v_rip + 12758950)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    }
    goto loc_0039BC77;
loc_0039BD96:
    if ((*(unsigned int *)(v_rip + 12751619)) != 0) goto loc_0039BDAC;
    if (sign_flag) goto loc_0039C064;
loc_0039BDAC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 72)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 32))) goto loc_0039BCDA;
    result = KiComputeThreadQos(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8), a2, a3, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8) + 516))) != ((unsigned int)(result))) goto loc_0039BCDA;
    result = KiCheckPreferredHeteroProcessor(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8), *(unsigned __int64 *)(gs_base + (0 + 32)), 1, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    if ((unsigned int)(result) != 0) goto loc_0039BCDA;
    result = KiCheckForPendingQosUpdate(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8), *(unsigned __int64 *)(gs_base + (0 + 32)), 1, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    goto loc_0039BC36;
loc_0039BDF7:
    if (sign_flag) goto loc_0039C0DB;
loc_0039BE04:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(gs_base + (0 + 32)), 1, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    return result;
loc_0039BE35:
    if ((*(unsigned int *)(v_rip + 12758748)) != 0) goto loc_0039BF91;
loc_0039BE4A:
    if ((*(unsigned __int8 *)(v_rip + 12758100)) == 0) goto loc_0039C032;
    result = RtlGetInterruptTimePrecise(v_stack_m140, *(unsigned __int64 *)(gs_base + (0 + 32)), 1, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    v_rsi = -((unsigned int)(*(unsigned int *)(v_rip + 12758773)));
    v_stack_m138 = 0;
    if ((*(unsigned __int8 *)(v_rip + 12758058)) == 0) goto loc_0039C120;
loc_0039BE86:
    v_rdi = (result) - (v_rsi);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 38352) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12758219)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 38344) = v_rdi;
loc_0039BEB4:
    if ((*(unsigned int *)(v_rip + 12758629)) != 0) {
        a1 = v_r12;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    }
    goto loc_0039BC28;
loc_0039BED7:
    if ((*(unsigned __int8 *)(v_rip + 12757927)) == 0) goto loc_0039BCDA;
    if ((*(unsigned int *)(v_rip + 12758573)) != 0) goto loc_0039C022;
loc_0039BEF9:
    result = (unsigned __int8)((unsigned __int8)(v_cr8));
    if ((*(unsigned int *)(v_rip + 12758540)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8)));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    }
    goto loc_0039BCDA;
loc_0039BF30:
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0039BC8D;
    goto loc_0039BDF7;
loc_0039BF45:
loc_0039BF4C:
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0039BF4C;
    if (condition_is_above_or_equal) goto loc_0039BD0D;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(a1 + 416), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(1)))), 1, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    goto loc_0039BD0D;
loc_0039BF6D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 416))) < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 416) + 24))) goto loc_0039BCAF;
    goto loc_0039BCDA;
loc_0039BF7F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 416))) <= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 416) + 8))) goto loc_0039BCAF;
    goto loc_0039BCDA;
loc_0039BF91:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(v_cr8)), 15, 1, (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    goto loc_0039BE4A;
loc_0039BFA3:
    result = 0;
    v_stack_m12C = v_xmm0;
    if ((*(unsigned __int8 *)(v_rip + 12758039)) == 0) goto loc_0039C008;
    result = HalpDisableInterrupts((unsigned __int8)((unsigned __int8)(v_cr8)), 15, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)(*(unsigned int *)(v_rip + 12758502)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))))) | (4));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168) = a1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))) == 0) {
        a1 = 0xC0010015ULL;
        a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))) << (32);
        result = (result) | (a2);
        result = (result) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
    }
    v_stack_m130 = 5;
    result = HalpInterruptSendIpi(v_stack_m130, 47, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    goto loc_0039BE04;
loc_0039C022:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)((unsigned __int8)(v_cr8))), 15, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    goto loc_0039BEF9;
loc_0039C032:
    a2 = 0;
    a3 = -((unsigned int)(*(unsigned int *)(v_rip + 12758307)));
    v_stack_m160 = 0;
    v_stack_m168 = 1;
    v_stack_m170 = 3;
    result = KiSetClockTimer(*(unsigned __int64 *)(v_stack_m28 + 48), a2, a3, (unsigned int)(*(unsigned int *)(v_rip + 12757754)));
    goto loc_0039BEB4;
loc_0039C064:
    result = KiShouldScanSharedReadyQueue(*(unsigned __int64 *)(v_stack_m28 + 48), a2, a3, (unsigned int)(*(unsigned int *)(v_rip + 12757754)));
    if ((unsigned int)(result) != 0) goto loc_0039C0AA;
loc_0039C070:
    result = KiShouldScanLocalReadyQueue(*(unsigned __int64 *)(v_stack_m28 + 48), a2, a3, (unsigned int)(*(unsigned int *)(v_rip + 12757754)));
    if ((unsigned int)(result) == 0) goto loc_0039C085;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 33752)) & (768)) != 0) goto loc_0039C0BB;
loc_0039C085:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12750909))) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 33768) = a1;
    goto loc_0039BDAC;
loc_0039C099:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(v_cr8)), (unsigned __int8)(result), a3, (unsigned int)(*(unsigned int *)(v_rip + 12757754)));
    goto loc_0039BD45;
loc_0039C0AA:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 36424) + 8)))) & (768)) == 0) goto loc_0039C070;
loc_0039C0BB:
    result = KiSetDpcRequestFlag(*(unsigned __int64 *)(v_stack_m28 + 48) + 14524, 64, a3, (unsigned int)(*(unsigned int *)(v_rip + 12757754)));
    result = KiRequestSoftwareInterrupt(*(unsigned __int64 *)(v_stack_m28 + 48), 2, a3, (unsigned int)(*(unsigned int *)(v_rip + 12757754)));
    goto loc_0039BDAC;
loc_0039C0DB:
    result = KiShouldScanSharedReadyQueue(*(unsigned __int64 *)(v_stack_m28 + 48), 2, a3, (unsigned int)(*(unsigned int *)(v_rip + 12757754)));
    if ((unsigned int)(result) == 0) goto loc_0039C0FC;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 36424) + 8)))) & (0x7FFEULL)) != 0) goto loc_0039BE04;
loc_0039C0FC:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 33752)) & (0x7FFEULL)) != 0) goto loc_0039BE04;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12751026))) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 14536) = a1;
    goto loc_0039BE04;
loc_0039C120:
    result = RtlGetInterruptTimePrecise(v_stack_m138, 2, a3, (unsigned int)(*(unsigned int *)(v_rip + 12757754)));
    goto loc_0039BE86;
}
```

## 5. (Beta) C Style

```c
int64_t KiUpdateRunTime(uint8_t Arg1, uint8_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint8_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint8_t v_stack_m188;
    uint32_t v_stack_m190;
    uint8_t v_stack_m198;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0xA6EBA2)) ^ (local_rsp);
    v_stack_m38 = result;
    local_r13 = 0;
    v_stack_m168 = 0;
    result = KeDisableInterrupts(Arg1, Arg2, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_0039BCF4;
loc_0039BBF0:
    v_stack_m190 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m198 = Arg1;
    result = KeAccumulateTicks(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38C0)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), Arg2);
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83A0) = 1;
    if ((*(uint8_t *)(v_rip + 0xC2AE73)) != 0) goto loc_0039BE35;
loc_0039BC28:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) goto loc_0039BD96;
loc_0039BC36:
    v_stack_m138 = 0;
    result = RtlGetInterruptTimePrecise(v_stack_m138, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38C0)))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))), Arg2);
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip + 0xC2AE57))) * (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BD8));
    if ((*(uint64_t *)(v_stack_m138)) > (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BD8))) goto loc_0039BED7;
    if (result > Arg2) goto loc_0039BD13;
loc_0039BC77:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x68) == 0) goto loc_0039BDF7;
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD8))) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x68));
loc_0039BC8D:
    Arg3 = (Arg1) - ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD8)));
    if ((((uint8_t)(*(uint16_t *)(Arg1 + 0x70))) & (4)) != 0) goto loc_0039BF6D;
    if ((((uint8_t)(*(uint16_t *)(Arg1 + 0x70))) & (32)) == 0) goto loc_0039BF7F;
loc_0039BCAF:
    if ((((uint8_t)(*(uint16_t *)(Arg1 + 0x70))) & (18)) != 0) goto loc_0039BF30;
    if (condition_is_less_or_equal) goto loc_0039BCDA;
    if (!sign_flag) goto loc_0039BF30;
    if ((*(uint64_t *)(Arg1)) < (*(uint64_t *)(Arg1 + 0x10))) goto loc_0039BF30;
loc_0039BCDA:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38B9) = 1;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) == 0) goto loc_0039BFA3;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6) = 1;
    goto loc_0039BE04;
loc_0039BCF4:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0039BF45;
loc_0039BD0D:
    goto loc_0039BBF0;
loc_0039BD13:
    if ((*(uint8_t *)(v_rip + 0xC2AD6B)) == 0) goto loc_0039BC77;
    local_r12 = ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8659)) == 0) ? 1 : 0;
    if ((*(uint32_t *)(v_rip + 0xC2AFE1)) != 0) goto loc_0039C099;
loc_0039BD45:
    Arg3 = -((uint32_t)(*(uint32_t *)(v_rip + 0xC2AD54)));
    v_stack_m188 = 0;
    v_stack_m190 = (uint8_t)(local_r12);
    v_stack_m198 = 4;
    result = KiSetClockTimer(*(uint64_t *)(gs_base + (0 + 0x20)), result, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    if ((*(uint32_t *)(v_rip + 0xC2AFA6)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    }
    goto loc_0039BC77;
loc_0039BD96:
    if ((*(uint32_t *)(v_rip + 0xC29303)) != 0) goto loc_0039BDAC;
    if (sign_flag) goto loc_0039C064;
loc_0039BDAC:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x48)) >= (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x20))) goto loc_0039BCDA;
    result = KiComputeThreadQos(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8), Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8) + 0x204))) != ((uint32_t)(result))) goto loc_0039BCDA;
    result = KiCheckPreferredHeteroProcessor(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8), *(uint64_t *)(gs_base + (0 + 0x20)), 1, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    if ((uint32_t)(result) != 0) goto loc_0039BCDA;
    result = KiCheckForPendingQosUpdate(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8), *(uint64_t *)(gs_base + (0 + 0x20)), 1, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    goto loc_0039BC36;
loc_0039BDF7:
    if (sign_flag) goto loc_0039C0DB;
loc_0039BE04:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(gs_base + (0 + 0x20)), 1, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    return result;
loc_0039BE35:
    if ((*(uint32_t *)(v_rip + 0xC2AEDC)) != 0) goto loc_0039BF91;
loc_0039BE4A:
    if ((*(uint8_t *)(v_rip + 0xC2AC54)) == 0) goto loc_0039C032;
    result = RtlGetInterruptTimePrecise(v_stack_m140, *(uint64_t *)(gs_base + (0 + 0x20)), 1, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    local_rsi = -((uint32_t)(*(uint32_t *)(v_rip + 0xC2AEF5)));
    v_stack_m138 = 0;
    if ((*(uint8_t *)(v_rip + 0xC2AC2A)) == 0) goto loc_0039C120;
loc_0039BE86:
    local_rdi = (result) - (local_rsi);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x95D0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC2ACCB)));
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x95C8) = local_rdi;
loc_0039BEB4:
    if ((*(uint32_t *)(v_rip + 0xC2AE65)) != 0) {
        Arg1 = local_r12;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    }
    goto loc_0039BC28;
loc_0039BED7:
    if ((*(uint8_t *)(v_rip + 0xC2ABA7)) == 0) goto loc_0039BCDA;
    if ((*(uint32_t *)(v_rip + 0xC2AE2D)) != 0) goto loc_0039C022;
loc_0039BEF9:
    result = (uint8_t)((uint8_t)(v_cr8));
    if ((*(uint32_t *)(v_rip + 0xC2AE0C)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)((uint8_t)((uint8_t)(v_cr8)));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    }
    goto loc_0039BCDA;
loc_0039BF30:
    if (*(uint64_t *)(Arg1 + 0x1A0) != 0) goto loc_0039BC8D;
    goto loc_0039BDF7;
loc_0039BF45:
loc_0039BF4C:
    if (*(uint64_t *)(Arg1 + 0x1A0) != 0) goto loc_0039BF4C;
    if (condition_is_above_or_equal) goto loc_0039BD0D;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(Arg1 + 0x1A0), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(1)))), 1, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    goto loc_0039BD0D;
loc_0039BF6D:
    if ((*(uint64_t *)(*(uint64_t *)(Arg1 + 0x1A0))) < (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x1A0) + 0x18))) goto loc_0039BCAF;
    goto loc_0039BCDA;
loc_0039BF7F:
    if ((*(uint64_t *)(*(uint64_t *)(Arg1 + 0x1A0))) <= (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x1A0) + 0x8))) goto loc_0039BCAF;
    goto loc_0039BCDA;
loc_0039BF91:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(v_cr8)), 15, 1, (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    goto loc_0039BE4A;
loc_0039BFA3:
    result = 0;
    v_stack_m12C = v_xmm0;
    if ((*(uint8_t *)(v_rip + 0xC2AC17)) == 0) goto loc_0039C008;
    result = HalpDisableInterrupts((uint8_t)((uint8_t)(v_cr8)), 15, *(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)(*(uint32_t *)(v_rip + 0xC2ADE6)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))))) | (4));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8) = Arg1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))) == 0) {
        Arg1 = 0xC0010015ULL;
        Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))) << (32);
        result = (result) | (Arg2);
        result = (result) | (Arg2);
        Arg2 = result;
        Arg2 = (Arg2) >> (32);
    }
    if ((uint8_t)((uint8_t)(result)) != 0) {
    }
    v_stack_m130 = 5;
    result = HalpInterruptSendIpi(v_stack_m130, 47, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    goto loc_0039BE04;
loc_0039C022:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)((uint8_t)(v_cr8))), 15, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    goto loc_0039BEF9;
loc_0039C032:
    Arg2 = 0;
    Arg3 = -((uint32_t)(*(uint32_t *)(v_rip + 0xC2AD23)));
    v_stack_m160 = 0;
    v_stack_m168 = 1;
    v_stack_m170 = 3;
    result = KiSetClockTimer(*(uint64_t *)(v_stack_m28 + 0x30), Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2AAFA)));
    goto loc_0039BEB4;
loc_0039C064:
    result = KiShouldScanSharedReadyQueue(*(uint64_t *)(v_stack_m28 + 0x30), Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2AAFA)));
    if ((uint32_t)(result) != 0) goto loc_0039C0AA;
loc_0039C070:
    result = KiShouldScanLocalReadyQueue(*(uint64_t *)(v_stack_m28 + 0x30), Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2AAFA)));
    if ((uint32_t)(result) == 0) goto loc_0039C085;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x83D8)) & (768)) != 0) goto loc_0039C0BB;
loc_0039C085:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC2903D))) + ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x83E8) = Arg1;
    goto loc_0039BDAC;
loc_0039C099:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(v_cr8)), (uint8_t)(result), Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2AAFA)));
    goto loc_0039BD45;
loc_0039C0AA:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8E48) + 0x8)))) & (768)) == 0) goto loc_0039C070;
loc_0039C0BB:
    result = KiSetDpcRequestFlag(*(uint64_t *)(v_stack_m28 + 0x30) + 14524, 64, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2AAFA)));
    result = KiRequestSoftwareInterrupt(*(uint64_t *)(v_stack_m28 + 0x30), 2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2AAFA)));
    goto loc_0039BDAC;
loc_0039C0DB:
    result = KiShouldScanSharedReadyQueue(*(uint64_t *)(v_stack_m28 + 0x30), 2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2AAFA)));
    if ((uint32_t)(result) == 0) goto loc_0039C0FC;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x8E48) + 0x8)))) & (0x7FFEULL)) != 0) goto loc_0039BE04;
loc_0039C0FC:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x83D8)) & (0x7FFEULL)) != 0) goto loc_0039BE04;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC290B2))) + ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x38C8) = Arg1;
    goto loc_0039BE04;
loc_0039C120:
    result = RtlGetInterruptTimePrecise(v_stack_m138, 2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0xC2AAFA)));
    goto loc_0039BE86;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039BB70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
