# IoSetInformation

- RVA: `0x0071DBF0`–`0x0071DF89` (길이 `921` bytes)
- VA: `0x000000014071DBF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C7604`
- 디코드: `270`개 명령, `921/921` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0071DC35` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0071DC69` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0071DC89` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0071DC95` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x0071DCB3` → [IopWaitAndAcquireFileObjectLock](../8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x0071DCC3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0071DCD8` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x0071DCE4` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x0071DD3B` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x0071DD4D` → [IopAllocateIrpCleanup](../A1/IopAllocateIrpCleanup_function_00A1E2D4.md) (function, `0x00A1E2D4`)
- `0x0071DDDE` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (function, `0x002075C0`)
- `0x0071DE71` → [IopSetFileMemoryPartitionInformation](IopSetFileMemoryPartitionInformation_function_0071E414.md) (function, `0x0071E414`)
- `0x0071DEBA` → [IopOpenLinkOrRenameTarget](../8A/IopOpenLinkOrRenameTarget_function_008AAC04.md) (function, `0x008AAC04`)
- `0x0071DED5` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x0071DEE3` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (function, `0x0029B4B0`)
- `0x0071DF18` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0071DF2A` → [IopCancelAlertedRequest](../A9/IopCancelAlertedRequest_function_00A948F8.md) (function, `0x00A948F8`)
- `0x0071DF35` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x0071DF55` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0071DF68` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)

### Direct callers
- [MiAttemptPageFileReduction](../../text/48/MiAttemptPageFileReduction_function_004813E4.md) at `0x00481586`
- [MiAttemptPageFileExtension](../7F/MiAttemptPageFileExtension_function_007FEA2C.md) at `0x007FEB5C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x0071DC35` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0071DC69` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0071DC89` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0071DC95` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x0071DCC3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0071DCD8` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x0071DCE4` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x0071DD3B` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x0071DDDE` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (`PAGE` → `.text`)
  - `0x0071DED5` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (`PAGE` → `.text`)
  - `0x0071DEE3` → [IofCallDriver](../../text/29/IofCallDriver_function_0029B4B0.md) (`PAGE` → `.text`)
  - `0x0071DF18` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0071DF35` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x0071DF55` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0071DBF0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0071DBF5  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0071DBFA  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0071DBFF  55                              push rbp
0071DC00  57                              push rdi
0071DC01  41 54                           push r12
0071DC03  41 55                           push r13
0071DC05  41 57                           push r15
0071DC07  48 8B EC                        mov rbp, rsp
0071DC0A  48 83 EC 70                     sub rsp, 0x70
0071DC0E  0F 57 C0                        xorps xmm0, xmm0
0071DC11  45 33 FF                        xor r15d, r15d
0071DC14  33 C0                           xor eax, eax
0071DC16  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
0071DC1A  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
0071DC1E  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0071DC22  45 8A EF                        mov r13b, r15b
0071DC25  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0071DC29  44 88 7D C0                     mov byte ptr [rbp - 0x40], r15b
0071DC2D  4D 8B E1                        mov r12, r9
0071DC30  8B F2                           mov esi, edx
0071DC32  48 8B F9                        mov rdi, rcx
0071DC35  E8 E6 1D AF FF                  call 0x14020fa20
0071DC3A  8B 5F 50                        mov ebx, dword ptr [rdi + 0x50]
0071DC3D  45 33 C0                        xor r8d, r8d
0071DC40  F6 C3 02                        test bl, 2
0071DC43  0F 84 86 00 00 00               je 0x14071dccf
0071DC49  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0071DC52  48 8D 8F 80 00 00 00            lea rcx, [rdi + 0x80]
0071DC59  C1 EB 02                        shr ebx, 2
0071DC5C  33 D2                           xor edx, edx
0071DC5E  80 E3 01                        and bl, 1
0071DC61  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0071DC68  90                              nop
0071DC69  E8 C2 25 AF FF                  call 0x140210230
0071DC6E  41 8D 4F 01                     lea ecx, [r15 + 1]
0071DC72  44 88 7D 30                     mov byte ptr [rbp + 0x30], r15b
0071DC76  87 4F 74                        xchg dword ptr [rdi + 0x74], ecx
0071DC79  85 C9                           test ecx, ecx
0071DC7B  75 22                           jne 0x14071dc9f
0071DC7D  48 85 C0                        test rax, rax
0071DC80  74 04                           je 0x14071dc86
0071DC82  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0071DC86  48 8B CF                        mov rcx, rdi
0071DC89  E8 92 1D AF FF                  call 0x14020fa20
0071DC8E  48 8D 8F 98 00 00 00            lea rcx, [rdi + 0x98]
0071DC95  E8 B6 A6 B2 FF                  call 0x140248350
0071DC9A  41 B7 01                        mov r15b, 1
0071DC9D  EB 3E                           jmp 0x14071dcdd
0071DC9F  48 8D 4D 30                     lea rcx, [rbp + 0x30]
0071DCA3  4C 8B C8                        mov r9, rax
0071DCA6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0071DCAB  44 8A C3                        mov r8b, bl
0071DCAE  48 8B CF                        mov rcx, rdi
0071DCB1  33 D2                           xor edx, edx
0071DCB3  E8 20 0A 19 00                  call 0x1408ae6d8
0071DCB8  8B D8                           mov ebx, eax
0071DCBA  44 38 7D 30                     cmp byte ptr [rbp + 0x30], r15b
0071DCBE  74 CE                           je 0x14071dc8e
0071DCC0  48 8B CF                        mov rcx, rdi
0071DCC3  E8 88 B6 BD FF                  call 0x1402f9350
0071DCC8  8B C3                           mov eax, ebx
0071DCCA  E9 A0 02 00 00                  jmp 0x14071df6f
0071DCCF  BA 01 00 00 00                  mov edx, 1
0071DCD4  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0071DCD8  E8 33 00 CF FF                  call 0x14040dd10
0071DCDD  48 8B CF                        mov rcx, rdi
0071DCE0  44 88 7D 30                     mov byte ptr [rbp + 0x30], r15b
0071DCE4  E8 37 D4 B7 FF                  call 0x14029b120
0071DCE9  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0071DCED  83 FE 38                        cmp esi, 0x38
0071DCF0  75 07                           jne 0x14071dcf9
0071DCF2  BE 0A 00 00 00                  mov esi, 0xa
0071DCF7  EB 22                           jmp 0x14071dd1b
0071DCF9  83 FE 42                        cmp esi, 0x42
0071DCFC  75 07                           jne 0x14071dd05
0071DCFE  BE 41 00 00 00                  mov esi, 0x41
0071DD03  EB 16                           jmp 0x14071dd1b
0071DD05  83 FE 39                        cmp esi, 0x39
0071DD08  75 07                           jne 0x14071dd11
0071DD0A  BE 0B 00 00 00                  mov esi, 0xb
0071DD0F  EB 0A                           jmp 0x14071dd1b
0071DD11  83 FE 49                        cmp esi, 0x49
0071DD14  75 0A                           jne 0x14071dd20
0071DD16  BE 48 00 00 00                  mov esi, 0x48
0071DD1B  41 B5 01                        mov r13b, 1
0071DD1E  EB 0E                           jmp 0x14071dd2e
0071DD20  83 FE 4B                        cmp esi, 0x4b
0071DD23  75 09                           jne 0x14071dd2e
0071DD25  BE 47 00 00 00                  mov esi, 0x47
0071DD2A  C6 45 C0 01                     mov byte ptr [rbp - 0x40], 1
0071DD2E  8A 50 4C                        mov dl, byte ptr [rax + 0x4c]
0071DD31  45 8A C7                        mov r8b, r15b
0071DD34  41 80 F0 01                     xor r8b, 1
0071DD38  48 8B C8                        mov rcx, rax
0071DD3B  E8 E0 99 AE FF                  call 0x140207720
0071DD40  48 8B D8                        mov rbx, rax
0071DD43  48 85 C0                        test rax, rax
0071DD46  75 14                           jne 0x14071dd5c
0071DD48  33 D2                           xor edx, edx
0071DD4A  48 8B CF                        mov rcx, rdi
0071DD4D  E8 82 05 30 00                  call 0x140a1e2d4
0071DD52  B8 9A 00 00 C0                  mov eax, 0xc000009a
0071DD57  E9 13 02 00 00                  jmp 0x14071df6f
0071DD5C  48 89 B8 C0 00 00 00            mov qword ptr [rax + 0xc0], rdi
0071DD63  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0071DD6C  48 89 83 98 00 00 00            mov qword ptr [rbx + 0x98], rax
0071DD73  C6 43 40 00                     mov byte ptr [rbx + 0x40], 0
0071DD77  45 84 FF                        test r15b, r15b
0071DD7A  74 08                           je 0x14071dd84
0071DD7C  80 4B 47 02                     or byte ptr [rbx + 0x47], 2
0071DD80  33 C9                           xor ecx, ecx
0071DD82  EB 0B                           jmp 0x14071dd8f
0071DD84  C7 43 10 04 00 00 00            mov dword ptr [rbx + 0x10], 4
0071DD8B  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0071DD8F  48 89 4B 50                     mov qword ptr [rbx + 0x50], rcx
0071DD93  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0071DD97  4C 8B BB B8 00 00 00            mov r15, qword ptr [rbx + 0xb8]
0071DD9E  8B 45 40                        mov eax, dword ptr [rbp + 0x40]
0071DDA1  48 89 4B 48                     mov qword ptr [rbx + 0x48], rcx
0071DDA5  41 C6 47 B8 06                  mov byte ptr [r15 - 0x48], 6
0071DDAA  49 89 7F E8                     mov qword ptr [r15 - 0x18], rdi
0071DDAE  83 4B 10 10                     or dword ptr [rbx + 0x10], 0x10
0071DDB2  4C 89 63 18                     mov qword ptr [rbx + 0x18], r12
0071DDB6  41 89 47 C0                     mov dword ptr [r15 - 0x40], eax
0071DDBA  41 89 77 C8                     mov dword ptr [r15 - 0x38], esi
0071DDBE  45 84 ED                        test r13b, r13b
0071DDC1  74 0A                           je 0x14071ddcd
0071DDC3  41 80 4F BA 01                  or byte ptr [r15 - 0x46], 1
0071DDC8  45 33 ED                        xor r13d, r13d
0071DDCB  EB 0E                           jmp 0x14071dddb
0071DDCD  45 33 ED                        xor r13d, r13d
0071DDD0  44 38 6D C0                     cmp byte ptr [rbp - 0x40], r13b
0071DDD4  74 05                           je 0x14071dddb
0071DDD6  41 80 4F BA 01                  or byte ptr [r15 - 0x46], 1
0071DDDB  48 8B CB                        mov rcx, rbx
0071DDDE  E8 DD 97 AE FF                  call 0x1402075c0
0071DDE3  83 FE 10                        cmp esi, 0x10
0071DDE6  75 61                           jne 0x14071de49
0071DDE8  8B 57 50                        mov edx, dword ptr [rdi + 0x50]
0071DDEB  F6 C2 08                        test dl, 8
0071DDEE  75 12                           jne 0x14071de02
0071DDF0  41 8B 04 24                     mov eax, dword ptr [r12]
0071DDF4  A8 02                           test al, 2
0071DDF6  74 04                           je 0x14071ddfc
0071DDF8  0B D6                           or edx, esi
0071DDFA  EB 03                           jmp 0x14071ddff
0071DDFC  83 E2 EF                        and edx, 0xffffffef
0071DDFF  89 57 50                        mov dword ptr [rdi + 0x50], edx
0071DE02  8B C2                           mov eax, edx
0071DE04  83 CA 20                        or edx, 0x20
0071DE07  83 E0 DF                        and eax, 0xffffffdf
0071DE0A  41 F6 04 24 04                  test byte ptr [r12], 4
0071DE0F  0F 44 D0                        cmove edx, eax
0071DE12  89 57 50                        mov dword ptr [rdi + 0x50], edx
0071DE15  41 8B 04 24                     mov eax, dword ptr [r12]
0071DE19  A8 02                           test al, 2
0071DE1B  74 0F                           je 0x14071de2c
0071DE1D  A8 10                           test al, 0x10
0071DE1F  74 05                           je 0x14071de26
0071DE21  83 CA 04                        or edx, 4
0071DE24  EB 03                           jmp 0x14071de29
0071DE26  83 E2 FB                        and edx, 0xfffffffb
0071DE29  89 57 50                        mov dword ptr [rdi + 0x50], edx
0071DE2C  FE 4B 43                        dec byte ptr [rbx + 0x43]
0071DE2F  41 8B F5                        mov esi, r13d
0071DE32  48 83 83 B8 00 00 00 B8         add qword ptr [rbx + 0xb8], -0x48
0071DE3A  33 D2                           xor edx, edx
0071DE3C  44 89 6B 30                     mov dword ptr [rbx + 0x30], r13d
0071DE40  4C 89 6B 38                     mov qword ptr [rbx + 0x38], r13
0071DE44  E9 89 00 00 00                  jmp 0x14071ded2
0071DE49  83 FE 0A                        cmp esi, 0xa
0071DE4C  74 47                           je 0x14071de95
0071DE4E  83 FE 41                        cmp esi, 0x41
0071DE51  74 3A                           je 0x14071de8d
0071DE53  83 FE 0B                        cmp esi, 0xb
0071DE56  74 3D                           je 0x14071de95
0071DE58  83 FE 48                        cmp esi, 0x48
0071DE5B  74 30                           je 0x14071de8d
0071DE5D  83 FE 1F                        cmp esi, 0x1f
0071DE60  74 21                           je 0x14071de83
0071DE62  83 FE 45                        cmp esi, 0x45
0071DE65  75 75                           jne 0x14071dedc
0071DE67  44 8B 45 40                     mov r8d, dword ptr [rbp + 0x40]
0071DE6B  49 8B D4                        mov rdx, r12
0071DE6E  48 8B CF                        mov rcx, rdi
0071DE71  E8 9E 05 00 00                  call 0x14071e414
0071DE76  8B F0                           mov esi, eax
0071DE78  89 43 30                        mov dword ptr [rbx + 0x30], eax
0071DE7B  33 D2                           xor edx, edx
0071DE7D  4C 89 6B 38                     mov qword ptr [rbx + 0x38], r13
0071DE81  EB 44                           jmp 0x14071dec7
0071DE83  41 8B 04 24                     mov eax, dword ptr [r12]
0071DE87  41 89 47 D8                     mov dword ptr [r15 - 0x28], eax
0071DE8B  EB 10                           jmp 0x14071de9d
0071DE8D  41 8A 04 24                     mov al, byte ptr [r12]
0071DE91  24 01                           and al, 1
0071DE93  EB 04                           jmp 0x14071de99
0071DE95  41 8A 04 24                     mov al, byte ptr [r12]
0071DE99  41 88 47 D8                     mov byte ptr [r15 - 0x28], al
0071DE9D  66 41 83 7C 24 14 5C            cmp word ptr [r12 + 0x14], 0x5c
0071DEA4  74 07                           je 0x14071dead
0071DEA6  4D 39 6C 24 08                  cmp qword ptr [r12 + 8], r13
0071DEAB  74 2F                           je 0x14071dedc
0071DEAD  4C 8B CF                        mov r9, rdi
0071DEB0  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0071DEB4  4D 8B C4                        mov r8, r12
0071DEB7  48 8B D3                        mov rdx, rbx
0071DEBA  E8 45 CD 18 00                  call 0x1408aac04
0071DEBF  8B F0                           mov esi, eax
0071DEC1  85 C0                           test eax, eax
0071DEC3  79 17                           jns 0x14071dedc
0071DEC5  B2 02                           mov dl, 2
0071DEC7  FE 4B 43                        dec byte ptr [rbx + 0x43]
0071DECA  48 83 83 B8 00 00 00 B8         add qword ptr [rbx + 0xb8], -0x48
0071DED2  48 8B CB                        mov rcx, rbx
0071DED5  E8 E6 D6 B7 FF                  call 0x14029b5c0
0071DEDA  EB 0E                           jmp 0x14071deea
0071DEDC  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0071DEE0  48 8B D3                        mov rdx, rbx
0071DEE3  E8 C8 D5 B7 FF                  call 0x14029b4b0
0071DEE8  8B F0                           mov esi, eax
0071DEEA  44 38 6D 30                     cmp byte ptr [rbp + 0x30], r13b
0071DEEE  74 4C                           je 0x14071df3c
0071DEF0  81 FE 03 01 00 00               cmp esi, 0x103
0071DEF6  75 3A                           jne 0x14071df32
0071DEF8  44 8B 4F 50                     mov r9d, dword ptr [rdi + 0x50]
0071DEFC  48 8D B7 98 00 00 00            lea rsi, [rdi + 0x98]
0071DF03  41 C1 E9 02                     shr r9d, 2
0071DF07  45 33 C0                        xor r8d, r8d
0071DF0A  41 80 E1 01                     and r9b, 1
0071DF0E  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0071DF13  33 D2                           xor edx, edx
0071DF15  48 8B CE                        mov rcx, rsi
0071DF18  E8 93 07 AF FF                  call 0x14020e6b0
0071DF1D  3D 01 01 00 00                  cmp eax, 0x101
0071DF22  75 0B                           jne 0x14071df2f
0071DF24  48 8B D3                        mov rdx, rbx
0071DF27  48 8B CE                        mov rcx, rsi
0071DF2A  E8 C9 69 37 00                  call 0x140a948f8
0071DF2F  8B 77 38                        mov esi, dword ptr [rdi + 0x38]
0071DF32  48 8B CF                        mov rcx, rdi
0071DF35  E8 56 2B B3 FF                  call 0x140250a90
0071DF3A  EB 21                           jmp 0x14071df5d
0071DF3C  81 FE 03 01 00 00               cmp esi, 0x103
0071DF42  75 19                           jne 0x14071df5d
0071DF44  45 33 C9                        xor r9d, r9d
0071DF47  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0071DF4C  45 33 C0                        xor r8d, r8d
0071DF4F  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0071DF53  33 D2                           xor edx, edx
0071DF55  E8 56 07 AF FF                  call 0x14020e6b0
0071DF5A  8B 75 D8                        mov esi, dword ptr [rbp - 0x28]
0071DF5D  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
0071DF61  48 85 C9                        test rcx, rcx
0071DF64  74 07                           je 0x14071df6d
0071DF66  33 D2                           xor edx, edx
0071DF68  E8 03 39 18 00                  call 0x1408a1870
0071DF6D  8B C6                           mov eax, esi
0071DF6F  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0071DF74  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0071DF78  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
0071DF7C  49 8B E3                        mov rsp, r11
0071DF7F  41 5F                           pop r15
0071DF81  41 5D                           pop r13
0071DF83  41 5C                           pop r12
0071DF85  5F                              pop rdi
0071DF86  5D                              pop rbp
0071DF87  C3                              ret
0071DF88  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoSetInformation(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = v_rsi;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (112);
    v_r15 = 0;
    result = 0;
    v_stack_m58 = 0;
    v_stack_m40 = v_xmm0;
    v_stack_m30 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m68 = 0;
    result = ObfReferenceObject(a1, a2, a3, a4);
    a3 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (2)) == 0) goto loc_0071DCCF;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) >> (2));
    a2 = 0;
    v_rbx = (unsigned __int8)((v_rbx) & (1));
    result = KeAbPreAcquire(a1 + 128, a2, a3, a4);
    v_stack_p8 = 0;
    if ((unsigned int)(v_r15 + 1) != 0) goto loc_0071DC9F;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(a1, a2, a3, a4);
loc_0071DC8E:
    result = KeResetEvent(a1 + 152, a2, a3, a4);
    goto loc_0071DCDD;
loc_0071DC9F:
    v_stack_m78 = v_stack_p8;
    a2 = 0;
    result = IopWaitAndAcquireFileObjectLock(a1, a2, (unsigned __int8)(v_rbx), result);
    if (v_stack_p8 == 1) goto loc_0071DC8E;
    result = ObfDereferenceObject(a1, a2, (unsigned __int8)(v_rbx), result);
    goto loc_0071DF6F;
loc_0071DCCF:
    result = KeInitializeEvent(v_stack_m40, 1, (unsigned __int8)(v_rbx), result);
loc_0071DCDD:
    v_stack_p8 = 1;
    result = IoGetRelatedDeviceObject(a1, 1, (unsigned __int8)(v_rbx), result);
    v_stack_m60 = result;
    if (((unsigned int)((unsigned int)(a2))) != 56) goto loc_0071DCF9;
    goto loc_0071DD1B;
loc_0071DCF9:
    if (10 != 66) goto loc_0071DD05;
    goto loc_0071DD1B;
loc_0071DD05:
    if (65 != 57) goto loc_0071DD11;
    goto loc_0071DD1B;
loc_0071DD11:
    if (11 != 73) goto loc_0071DD20;
loc_0071DD1B:
    goto loc_0071DD2E;
loc_0071DD20:
    v_rsi = 72;
    if (72 == 75) {
        v_rsi = 71;
        v_stack_m68 = 1;
    }
    a3 = (unsigned __int8)((1) ^ (1));
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, result);
    if (result != 0) goto loc_0071DD5C;
    a2 = 0;
    result = IopAllocateIrpCleanup(a1, a2, a3, result);
    goto loc_0071DF6F;
loc_0071DD5C:
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 192) = a1;
    *(unsigned __int64 *)(result + 152) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int8 *)(result + 64) = 0;
    if (1 == 0) goto loc_0071DD84;
    a1 = 0;
    goto loc_0071DD8F;
loc_0071DD84:
    *(unsigned int *)(result + 16) = 4;
loc_0071DD8F:
    *(unsigned __int64 *)(result + 80) = v_stack_m40;
    *(unsigned __int64 *)(result + 72) = v_stack_m50;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72) = 6;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = 0;
    *(unsigned __int64 *)(result + 24) = a4;
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(v_stack_p18));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 56) = (unsigned int)(v_rsi);
    if (1 == 0) goto loc_0071DDCD;
    v_r13 = 0;
    goto loc_0071DDDB;
loc_0071DDCD:
    v_r13 = 0;
    if (v_stack_m68 != 0) {
    }
    result = IopQueueThreadIrp(result, a2, a3, result);
    if (((unsigned int)(v_rsi)) != 16) goto loc_0071DE49;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (8)) != 0) goto loc_0071DE02;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4)))) & (2)) == 0) goto loc_0071DDFC;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) | ((unsigned int)(v_rsi)));
    goto loc_0071DDFF;
loc_0071DDFC:
    a2 = (unsigned int)((a2) & (0xFFFFFFEFULL));
loc_0071DDFF:
    *(unsigned int *)(a1 + 80) = a2;
loc_0071DE02:
    a2 = (unsigned int)((a2) | (32));
    result = (unsigned int)(((unsigned int)(a2)) & (0xFFFFFFDFULL));
    if (((*(unsigned __int8 *)(a4)) & (4)) == 0) { a2 = (unsigned int)(result); }
    *(unsigned int *)(a1 + 80) = a2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4)))) & (2)) == 0) goto loc_0071DE2C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4)))) & (16)) == 0) goto loc_0071DE26;
    a2 = (unsigned int)((a2) | (4));
    goto loc_0071DE29;
loc_0071DE26:
    a2 = (unsigned int)((a2) & (0xFFFFFFFBULL));
loc_0071DE29:
    *(unsigned int *)(a1 + 80) = a2;
loc_0071DE2C:
    a2 = 0;
    *(unsigned int *)(result + 48) = 0;
    *(unsigned __int64 *)(result + 56) = 0;
    goto loc_0071DED2;
loc_0071DE49:
    if (0 == 10) goto loc_0071DE95;
    if (0 == 65) goto loc_0071DE8D;
    if (0 == 11) goto loc_0071DE95;
    if (0 == 72) goto loc_0071DE8D;
    if (0 == 31) goto loc_0071DE83;
    if (0 != 69) goto loc_0071DEDC;
    result = IopSetFileMemoryPartitionInformation(0, a4, (unsigned int)(v_stack_p18), result);
    *(unsigned int *)(result + 48) = (unsigned int)(result);
    a2 = 0;
    *(unsigned __int64 *)(result + 56) = 0;
    goto loc_0071DEC7;
loc_0071DE83:
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 40) = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    goto loc_0071DE9D;
loc_0071DE8D:
    result = (unsigned __int8)((*(unsigned __int8 *)(a4)) & (1));
    goto loc_0071DE99;
loc_0071DE95:
loc_0071DE99:
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 40) = (unsigned __int8)(*(unsigned __int8 *)(a4));
loc_0071DE9D:
    if ((*(unsigned __int16 *)(a4 + 20)) == 92) goto loc_0071DEAD;
    if ((*(unsigned __int64 *)(a4 + 8)) == 0) goto loc_0071DEDC;
loc_0071DEAD:
    result = IopOpenLinkOrRenameTarget(v_stack_m58, result, a4, 0);
    if (!sign_flag) goto loc_0071DEDC;
loc_0071DEC7:
loc_0071DED2:
    result = IofCompleteRequest(result, 2, a4, 0);
    goto loc_0071DEEA;
loc_0071DEDC:
    result = IofCallDriver(v_stack_m60, result, a4, 0);
loc_0071DEEA:
    if (v_stack_p8 == 0) goto loc_0071DF3C;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 259) goto loc_0071DF32;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) >> (2));
    a3 = 0;
    a4 = (unsigned __int8)((a4) & (1));
    v_stack_m78 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(a1 + 152, a2, a3, a4);
    if (((unsigned int)(result)) == 257) {
        a2 = result;
        a1 = a1 + 152;
        result = IopCancelAlertedRequest(a1, a2, a3, a4);
    }
loc_0071DF32:
    result = IopReleaseFileObjectLock(a1, a2, a3, a4);
    goto loc_0071DF5D;
loc_0071DF3C:
    v_rsi = (unsigned int)(*(unsigned int *)(a1 + 56));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)))) == 259) {
        a4 = 0;
        v_stack_m78 = 0;
        a3 = 0;
        a1 = v_stack_m40;
        a2 = 0;
        result = KeWaitForSingleObject(a1, a2, a3, a4);
        v_rsi = v_stack_m50;
    }
    if (v_stack_m58 != 0) {
        a2 = 0;
        result = ObCloseHandle(v_stack_m58, a2, a3, a4);
    }
loc_0071DF6F:
    return (unsigned int)((unsigned int)(v_rsi));
}
```

## 5. (Beta) C Style

```c
int64_t IoSetInformation(void *Arg1, int32_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint8_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = local_rsi;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (112);
    local_r15 = 0;
    result = 0;
    v_stack_m58 = 0;
    v_stack_m40 = v_xmm0;
    v_stack_m30 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m68 = 0;
    result = ObfReferenceObject(Arg1, Arg2, Arg3, Arg4);
    Arg3 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (2)) == 0) goto loc_0071DCCF;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) >> (2));
    Arg2 = 0;
    local_rbx = (uint8_t)((local_rbx) & (1));
    result = KeAbPreAcquire(Arg1 + 128, Arg2, Arg3, Arg4);
    v_stack_p8 = 0;
    if ((uint32_t)(local_r15 + 1) != 0) goto loc_0071DC9F;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(Arg1, Arg2, Arg3, Arg4);
loc_0071DC8E:
    result = KeResetEvent(Arg1 + 152, Arg2, Arg3, Arg4);
    goto loc_0071DCDD;
loc_0071DC9F:
    v_stack_m78 = v_stack_p8;
    Arg2 = 0;
    result = IopWaitAndAcquireFileObjectLock(Arg1, Arg2, (uint8_t)(local_rbx), result);
    if (v_stack_p8 == 1) goto loc_0071DC8E;
    result = ObfDereferenceObject(Arg1, Arg2, (uint8_t)(local_rbx), result);
    goto loc_0071DF6F;
loc_0071DCCF:
    result = KeInitializeEvent(v_stack_m40, 1, (uint8_t)(local_rbx), result);
loc_0071DCDD:
    v_stack_p8 = 1;
    result = IoGetRelatedDeviceObject(Arg1, 1, (uint8_t)(local_rbx), result);
    v_stack_m60 = result;
    if (((uint32_t)((uint32_t)(Arg2))) != 56) goto loc_0071DCF9;
    goto loc_0071DD1B;
loc_0071DCF9:
    if (10 != 66) goto loc_0071DD05;
    goto loc_0071DD1B;
loc_0071DD05:
    if (65 != 57) goto loc_0071DD11;
    goto loc_0071DD1B;
loc_0071DD11:
    if (11 != 73) goto loc_0071DD20;
loc_0071DD1B:
    goto loc_0071DD2E;
loc_0071DD20:
    local_rsi = 72;
    if (72 == 75) {
        local_rsi = 71;
        v_stack_m68 = 1;
    }
    Arg3 = (uint8_t)((1) ^ (1));
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, result);
    if (result != 0) goto loc_0071DD5C;
    Arg2 = 0;
    result = IopAllocateIrpCleanup(Arg1, Arg2, Arg3, result);
    goto loc_0071DF6F;
loc_0071DD5C:
    *(void **)((uint32_t)(0xC000009AULL) + 0xC0) = Arg1;
    *(uint64_t *)(result + 0x98) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint8_t *)(result + 0x40) = 0;
    if (1 == 0) goto loc_0071DD84;
    Arg1 = 0;
    goto loc_0071DD8F;
loc_0071DD84:
    *(uint32_t *)(result + 0x10) = 4;
loc_0071DD8F:
    *(uint64_t *)(result + 0x50) = v_stack_m40;
    *(uint64_t *)(result + 0x48) = v_stack_m50;
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 6;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x18) = 0;
    *(void **)(result + 0x18) = Arg4;
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(v_stack_p18));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = (uint32_t)(local_rsi);
    if (1 == 0) goto loc_0071DDCD;
    local_r13 = 0;
    goto loc_0071DDDB;
loc_0071DDCD:
    local_r13 = 0;
    if (v_stack_m68 != 0) {
    }
    result = IopQueueThreadIrp(result, Arg2, Arg3, result);
    if (((uint32_t)(local_rsi)) != 16) goto loc_0071DE49;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (8)) != 0) goto loc_0071DE02;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg4)))) & (2)) == 0) goto loc_0071DDFC;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) | ((uint32_t)(local_rsi)));
    goto loc_0071DDFF;
loc_0071DDFC:
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFEFULL));
loc_0071DDFF:
    *(uint32_t *)(arg1 + 0x50) = Arg2;
loc_0071DE02:
    Arg2 = (uint32_t)((Arg2) | (32));
    result = (uint32_t)(((uint32_t)(Arg2)) & (0xFFFFFFDFULL));
    if (((*(uint8_t *)(arg4)) & (4)) == 0) { Arg2 = (uint32_t)(result); }
    *(uint32_t *)(arg1 + 0x50) = Arg2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg4)))) & (2)) == 0) goto loc_0071DE2C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg4)))) & (16)) == 0) goto loc_0071DE26;
    Arg2 = (uint32_t)((Arg2) | (4));
    goto loc_0071DE29;
loc_0071DE26:
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFFBULL));
loc_0071DE29:
    *(uint32_t *)(arg1 + 0x50) = Arg2;
loc_0071DE2C:
    Arg2 = 0;
    *(uint32_t *)(result + 0x30) = 0;
    *(uint64_t *)(result + 0x38) = 0;
    goto loc_0071DED2;
loc_0071DE49:
    if (0 == 10) goto loc_0071DE95;
    if (0 == 65) goto loc_0071DE8D;
    if (0 == 11) goto loc_0071DE95;
    if (0 == 72) goto loc_0071DE8D;
    if (0 == 31) goto loc_0071DE83;
    if (0 != 69) goto loc_0071DEDC;
    result = IopSetFileMemoryPartitionInformation(0, Arg4, (uint32_t)(v_stack_p18), result);
    *(uint32_t *)(result + 0x30) = (uint32_t)(result);
    Arg2 = 0;
    *(uint64_t *)(result + 0x38) = 0;
    goto loc_0071DEC7;
loc_0071DE83:
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4)));
    goto loc_0071DE9D;
loc_0071DE8D:
    result = (uint8_t)((*(uint8_t *)(arg4)) & (1));
    goto loc_0071DE99;
loc_0071DE95:
loc_0071DE99:
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x28) = (uint8_t)(*(uint8_t *)(arg4));
loc_0071DE9D:
    if ((*(uint16_t *)(arg4 + 0x14)) == 92) goto loc_0071DEAD;
    if ((*(uint64_t *)(arg4 + 0x8)) == 0) goto loc_0071DEDC;
loc_0071DEAD:
    result = IopOpenLinkOrRenameTarget(v_stack_m58, result, Arg4, 0);
    if (!sign_flag) goto loc_0071DEDC;
loc_0071DEC7:
loc_0071DED2:
    result = IofCompleteRequest(result, 2, Arg4, 0);
    goto loc_0071DEEA;
loc_0071DEDC:
    result = IofCallDriver(v_stack_m60, result, Arg4, 0);
loc_0071DEEA:
    if (v_stack_p8 == 0) goto loc_0071DF3C;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 259) goto loc_0071DF32;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) >> (2));
    Arg3 = 0;
    Arg4 = (uint8_t)((Arg4) & (1));
    v_stack_m78 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(Arg1 + 152, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) == 257) {
        Arg2 = result;
        Arg1 = Arg1 + 152;
        result = IopCancelAlertedRequest(Arg1, Arg2, Arg3, Arg4);
    }
loc_0071DF32:
    result = IopReleaseFileObjectLock(Arg1, Arg2, Arg3, Arg4);
    goto loc_0071DF5D;
loc_0071DF3C:
    local_rsi = (uint32_t)(*(uint32_t *)(arg1 + 0x38));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) == 259) {
        Arg4 = 0;
        v_stack_m78 = 0;
        Arg3 = 0;
        Arg1 = v_stack_m40;
        Arg2 = 0;
        result = KeWaitForSingleObject(Arg1, Arg2, Arg3, Arg4);
        local_rsi = v_stack_m50;
    }
    if (v_stack_m58 != 0) {
        Arg2 = 0;
        result = ObCloseHandle(v_stack_m58, Arg2, Arg3, Arg4);
    }
loc_0071DF6F:
    return (uint32_t)((uint32_t)(local_rsi));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `W` |
| `Arg1` | `+ 0x74` | `32` | `R/W` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg4` | `+ 0x0` | `8` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x14` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0071DBF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
