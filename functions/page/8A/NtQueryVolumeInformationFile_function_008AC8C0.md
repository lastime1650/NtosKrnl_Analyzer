# NtQueryVolumeInformationFile

- RVA: `0x008AC8C0`–`0x008ACE36` (길이 `1,398` bytes)
- VA: `0x00000001408AC8C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007F7AC`
- 디코드: `336`개 명령, `1,398/1,398` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008ACA07` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x008ACA14` → [ExRaiseAccessViolation](../8E/ExRaiseAccessViolation_function_008E9240.md) (function, `0x008E9240`)
- `0x008ACA1A` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008ACA3B` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x008ACAA7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008ACAD2` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008ACAF7` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x008ACAFF` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x008ACB20` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x008ACBA8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008ACBF3` → [IopSynchronousServiceTail](../8E/IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)
- `0x008ACC22` → [IopSynchronousApiServiceTail](IopSynchronousApiServiceTail_function_008ACE3C.md) (function, `0x008ACE3C`)
- `0x008ACCDA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ACD19` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ACD3F` → [IopGetMountFlag](../../text/27/IopGetMountFlag_function_00272444.md) (function, `0x00272444`)
- `0x008ACD5A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008ACD76` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x008ACD89` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ACDA3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ACDCD` → [IopWaitAndAcquireFileObjectLock](IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x008ACDDC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008ACDFA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008ACE07` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008ACE27` → [IopExceptionCleanupEx](IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)

### Direct callers
- [PfSnIsVolumeMounted](PfSnIsVolumeMounted_function_008AAACC.md) at `0x008AABB0`
- [PfSnQueryVolumeInfo](PfSnQueryVolumeInfo_function_008AD38C.md) at `0x008AD445`
- [PfpVolumeOpenAndVerify](../93/PfpVolumeOpenAndVerify_function_009381F4.md) at `0x00938338`
- [sub_00B24F64](../B2/Unknown_function_00B24F64.md) at `0x00B24F7E`

### Static image references
- `0x008AC930` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x008ACA3B` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x008ACAA7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008ACAD2` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008ACAF7` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x008ACAFF` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x008ACB20` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x008ACBA8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008ACCDA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008ACD19` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008ACD3F` → [IopGetMountFlag](../../text/27/IopGetMountFlag_function_00272444.md) (`PAGE` → `.text`)
  - `0x008ACD5A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008ACD76` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x008ACD89` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008ACDA3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008ACDDC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008ACDFA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008ACE07` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008ACAEE` → [sub_00B1A4B8](../B1/Unknown_function_00B1A4B8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008AC8C0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008AC8C5  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
008AC8CA  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
008AC8CF  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008AC8D4  57                              push rdi
008AC8D5  41 54                           push r12
008AC8D7  41 55                           push r13
008AC8D9  41 56                           push r14
008AC8DB  41 57                           push r15
008AC8DD  48 81 EC 80 00 00 00            sub rsp, 0x80
008AC8E4  4D 8B E8                        mov r13, r8
008AC8E7  48 8B F1                        mov rsi, rcx
008AC8EA  45 33 FF                        xor r15d, r15d
008AC8ED  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
008AC8F2  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
008AC8F7  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
008AC900  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
008AC905  45 0F B6 82 32 02 00 00         movzx r8d, byte ptr [r10 + 0x232]
008AC90D  44 88 44 24 41                  mov byte ptr [rsp + 0x41], r8b
008AC912  4C 63 A4 24 D0 00 00 00         movsxd r12, dword ptr [rsp + 0xd0]
008AC91A  45 84 C0                        test r8b, r8b
008AC91D  0F 84 CE 03 00 00               je 0x1408accf1
008AC923  41 83 FC 10                     cmp r12d, 0x10
008AC927  0F 83 69 04 00 00               jae 0x1408acd96
008AC92D  49 8B DC                        mov rbx, r12
008AC930  48 8D 3D C9 36 75 FF            lea rdi, [rip - 0x8ac937]
008AC937  41 0F B6 84 3C 20 B1 B4 00      movzx eax, byte ptr [r12 + rdi + 0xb4b120]
008AC940  84 C0                           test al, al
008AC942  0F 84 4E 04 00 00               je 0x1408acd96
008AC948  44 3B C8                        cmp r9d, eax
008AC94B  0F 82 9A 04 00 00               jb 0x1408acdeb
008AC951  49 BB 00 00 FF FF FF 7F 00 00   movabs r11, 0x7fffffff0000
008AC95B  49 8B CB                        mov rcx, r11
008AC95E  49 3B D3                        cmp rdx, r11
008AC961  48 0F 42 CA                     cmovb rcx, rdx
008AC965  8B 01                           mov eax, dword ptr [rcx]
008AC967  89 01                           mov dword ptr [rcx], eax
008AC969  49 8B 82 B8 00 00 00            mov rax, qword ptr [r10 + 0xb8]
008AC970  4C 39 B8 10 03 00 00            cmp qword ptr [rax + 0x310], r15
008AC977  74 1F                           je 0x1408ac998
008AC979  0F B7 88 EC 06 00 00            movzx ecx, word ptr [rax + 0x6ec]
008AC980  B8 4C 01 00 00                  mov eax, 0x14c
008AC985  66 3B C8                        cmp cx, ax
008AC988  75 04                           jne 0x1408ac98e
008AC98A  B0 01                           mov al, 1
008AC98C  EB 0C                           jmp 0x1408ac99a
008AC98E  B8 C4 01 00 00                  mov eax, 0x1c4
008AC993  66 3B C8                        cmp cx, ax
008AC996  74 F2                           je 0x1408ac98a
008AC998  32 C0                           xor al, al
008AC99A  88 44 24 42                     mov byte ptr [rsp + 0x42], al
008AC99E  45 8B C9                        mov r9d, r9d
008AC9A1  84 C0                           test al, al
008AC9A3  75 56                           jne 0x1408ac9fb
008AC9A5  41 0F B6 8C 3C 20 B6 B4 00      movzx ecx, byte ptr [r12 + rdi + 0xb4b620]
008AC9AE  4D 85 C9                        test r9, r9
008AC9B1  74 45                           je 0x1408ac9f8
008AC9B3  49 8B C5                        mov rax, r13
008AC9B6  8D 51 FF                        lea edx, [rcx - 1]
008AC9B9  49 85 D5                        test r13, rdx
008AC9BC  75 5C                           jne 0x1408aca1a
008AC9BE  49 8D 55 FF                     lea rdx, [r13 - 1]
008AC9C2  49 03 D1                        add rdx, r9
008AC9C5  4C 3B EA                        cmp r13, rdx
008AC9C8  77 4A                           ja 0x1408aca14
008AC9CA  49 3B D3                        cmp rdx, r11
008AC9CD  73 45                           jae 0x1408aca14
008AC9CF  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
008AC9D6  48 81 C2 00 10 00 00            add rdx, 0x1000
008AC9DD  0F 1F 00                        nop dword ptr [rax]
008AC9E0  0F B6 08                        movzx ecx, byte ptr [rax]
008AC9E3  88 08                           mov byte ptr [rax], cl
008AC9E5  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
008AC9EB  48 05 00 10 00 00               add rax, 0x1000
008AC9F1  48 3B C2                        cmp rax, rdx
008AC9F4  75 EA                           jne 0x1408ac9e0
008AC9F6  EB 28                           jmp 0x1408aca20
008AC9F8  90                              nop
008AC9F9  EB 25                           jmp 0x1408aca20
008AC9FB  41 B8 04 00 00 00               mov r8d, 4
008ACA01  49 8B D1                        mov rdx, r9
008ACA04  49 8B CD                        mov rcx, r13
008ACA07  E8 B4 C7 03 00                  call 0x1408e91c0
008ACA0C  44 0F B6 44 24 41               movzx r8d, byte ptr [rsp + 0x41]
008ACA12  EB 0C                           jmp 0x1408aca20
008ACA14  E8 27 C8 03 00                  call 0x1408e9240
008ACA19  CC                              int3
008ACA1A  E8 B1 D5 FE FF                  call 0x140899fd0
008ACA1F  CC                              int3
008ACA20  EB 05                           jmp 0x1408aca27
008ACA22  E9 00 02 00 00                  jmp 0x1408acc27
008ACA27  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
008ACA2C  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
008ACA31  8B 94 9F E0 CA B4 00            mov edx, dword ptr [rdi + rbx*4 + 0xb4cae0]
008ACA38  48 8B CE                        mov rcx, rsi
008ACA3B  E8 F0 0A 9F FF                  call 0x14029d530
008ACA40  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008ACA44  85 C0                           test eax, eax
008ACA46  0F 88 DB 01 00 00               js 0x1408acc27
008ACA4C  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008ACA51  4C 8D 77 50                     lea r14, [rdi + 0x50]
008ACA55  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
008ACA5A  41 8B 36                        mov esi, dword ptr [r14]
008ACA5D  8B C6                           mov eax, esi
008ACA5F  25 00 08 00 00                  and eax, 0x800
008ACA64  0F 85 DB 01 00 00               jne 0x1408acc45
008ACA6A  41 83 FC 04                     cmp r12d, 4
008ACA6E  0F 84 DB 01 00 00               je 0x1408acc4f
008ACA74  40 F6 C6 02                     test sil, 2
008ACA78  0F 84 69 02 00 00               je 0x1408acce7
008ACA7E  C1 EE 02                        shr esi, 2
008ACA81  40 80 E6 01                     and sil, 1
008ACA85  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008ACA8E  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008ACA95  90                              nop
008ACA96  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008ACA9B  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
008ACAA2  45 33 C0                        xor r8d, r8d
008ACAA5  33 D2                           xor edx, edx
008ACAA7  E8 84 37 96 FF                  call 0x140210230
008ACAAC  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
008ACAB1  B9 01 00 00 00                  mov ecx, 1
008ACAB6  87 4B 74                        xchg dword ptr [rbx + 0x74], ecx
008ACAB9  85 C9                           test ecx, ecx
008ACABB  0F 85 EE 02 00 00               jne 0x1408acdaf
008ACAC1  48 85 C0                        test rax, rax
008ACAC4  74 04                           je 0x1408acaca
008ACAC6  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
008ACACA  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008ACACF  48 8B CF                        mov rcx, rdi
008ACAD2  E8 49 2F 96 FF                  call 0x14020fa20
008ACAD7  41 8B DF                        mov ebx, r15d
008ACADA  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008ACADF  0F 85 BB 02 00 00               jne 0x1408acda0
008ACAE5  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
008ACAEA  41 83 FC 09                     cmp r12d, 9
008ACAEE  0F 84 C4 D9 26 00               je 0x140b1a4b8
008ACAF4  48 8B CF                        mov rcx, rdi
008ACAF7  E8 F4 0A 9F FF                  call 0x14029d5f0
008ACAFC  48 8B CF                        mov rcx, rdi
008ACAFF  E8 1C E6 9E FF                  call 0x14029b120
008ACB04  48 8B F0                        mov rsi, rax
008ACB07  41 8B 0E                        mov ecx, dword ptr [r14]
008ACB0A  F6 C1 02                        test cl, 2
008ACB0D  0F 84 39 02 00 00               je 0x1408acd4c
008ACB13  4D 8B F7                        mov r14, r15
008ACB16  45 33 C0                        xor r8d, r8d
008ACB19  0F B6 56 4C                     movzx edx, byte ptr [rsi + 0x4c]
008ACB1D  48 8B CE                        mov rcx, rsi
008ACB20  E8 FB AB 95 FF                  call 0x140207720
008ACB25  48 8B D8                        mov rbx, rax
008ACB28  48 85 C0                        test rax, rax
008ACB2B  0F 84 CF 01 00 00               je 0x1408acd00
008ACB31  48 89 B8 C0 00 00 00            mov qword ptr [rax + 0xc0], rdi
008ACB38  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008ACB3D  48 89 83 98 00 00 00            mov qword ptr [rbx + 0x98], rax
008ACB44  0F B6 44 24 41                  movzx eax, byte ptr [rsp + 0x41]
008ACB49  88 43 40                        mov byte ptr [rbx + 0x40], al
008ACB4C  0F 57 C0                        xorps xmm0, xmm0
008ACB4F  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
008ACB54  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008ACB59  0F 84 C9 01 00 00               je 0x1408acd28
008ACB5F  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
008ACB67  49 8B CF                        mov rcx, r15
008ACB6A  48 89 4B 50                     mov qword ptr [rbx + 0x50], rcx
008ACB6E  48 89 43 48                     mov qword ptr [rbx + 0x48], rax
008ACB72  4C 89 7B 58                     mov qword ptr [rbx + 0x58], r15
008ACB76  4C 8B B3 B8 00 00 00            mov r14, qword ptr [rbx + 0xb8]
008ACB7D  41 C6 46 B8 0A                  mov byte ptr [r14 - 0x48], 0xa
008ACB82  49 89 7E E8                     mov qword ptr [r14 - 0x18], rdi
008ACB86  4C 89 6B 70                     mov qword ptr [rbx + 0x70], r13
008ACB8A  4C 89 7B 18                     mov qword ptr [rbx + 0x18], r15
008ACB8E  4C 89 7B 08                     mov qword ptr [rbx + 8], r15
008ACB92  44 8B BC 24 C8 00 00 00         mov r15d, dword ptr [rsp + 0xc8]
008ACB9A  41 8B D7                        mov edx, r15d
008ACB9D  B9 41 00 00 00                  mov ecx, 0x41
008ACBA2  41 B8 49 6F 53 42               mov r8d, 0x42536f49
008ACBA8  E8 43 55 2D 00                  call 0x140b820f0
008ACBAD  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
008ACBB1  48 8B D3                        mov rdx, rbx
008ACBB4  48 85 C0                        test rax, rax
008ACBB7  0F 84 54 02 00 00               je 0x1408ace11
008ACBBD  81 4B 10 70 08 00 00            or dword ptr [rbx + 0x10], 0x870
008ACBC4  45 89 7E C0                     mov dword ptr [r14 - 0x40], r15d
008ACBC8  45 89 66 C8                     mov dword ptr [r14 - 0x38], r12d
008ACBCC  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
008ACBD4  44 0F B6 74 24 40               movzx r14d, byte ptr [rsp + 0x40]
008ACBDA  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
008ACBDF  44 0F B6 7C 24 41               movzx r15d, byte ptr [rsp + 0x41]
008ACBE5  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
008ACBEA  41 B1 01                        mov r9b, 1
008ACBED  4C 8B C7                        mov r8, rdi
008ACBF0  48 8B CE                        mov rcx, rsi
008ACBF3  E8 48 E8 03 00                  call 0x1408eb440
008ACBF8  45 84 F6                        test r14b, r14b
008ACBFB  75 2A                           jne 0x1408acc27
008ACBFD  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
008ACC05  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008ACC0A  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
008ACC0F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008ACC14  45 0F B6 CF                     movzx r9d, r15b
008ACC18  4C 8B C3                        mov r8, rbx
008ACC1B  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
008ACC20  8B C8                           mov ecx, eax
008ACC22  E8 15 02 00 00                  call 0x1408ace3c
008ACC27  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
008ACC2F  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008ACC33  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
008ACC37  49 8B E3                        mov rsp, r11
008ACC3A  41 5F                           pop r15
008ACC3C  41 5E                           pop r14
008ACC3E  41 5D                           pop r13
008ACC40  41 5C                           pop r12
008ACC42  5F                              pop rdi
008ACC43  C3                              ret
008ACC44  CC                              int3
008ACC45  41 83 FC 04                     cmp r12d, 4
008ACC49  0F 85 8A 01 00 00               jne 0x1408acdd9
008ACC4F  85 C0                           test eax, eax
008ACC51  75 0E                           jne 0x1408acc61
008ACC53  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008ACC57  83 78 48 14                     cmp dword ptr [rax + 0x48], 0x14
008ACC5B  0F 84 13 FE FF FF               je 0x1408aca74
008ACC61  41 8B CF                        mov ecx, r15d
008ACC64  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
008ACC68  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
008ACC6C  48 85 C0                        test rax, rax
008ACC6F  74 19                           je 0x1408acc8a
008ACC71  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
008ACC75  48 3B C8                        cmp rcx, rax
008ACC78  0F 85 BE 00 00 00               jne 0x1408acd3c
008ACC7E  0F B7 49 04                     movzx ecx, word ptr [rcx + 4]
008ACC82  83 E1 01                        and ecx, 1
008ACC85  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008ACC8A  83 BC 24 C8 00 00 00 08         cmp dword ptr [rsp + 0xc8], 8
008ACC92  0F 82 E8 00 00 00               jb 0x1408acd80
008ACC98  8B 43 48                        mov eax, dword ptr [rbx + 0x48]
008ACC9B  41 89 45 00                     mov dword ptr [r13], eax
008ACC9F  8B 43 34                        mov eax, dword ptr [rbx + 0x34]
008ACCA2  41 89 45 04                     mov dword ptr [r13 + 4], eax
008ACCA6  85 C9                           test ecx, ecx
008ACCA8  74 07                           je 0x1408accb1
008ACCAA  83 C8 20                        or eax, 0x20
008ACCAD  41 89 45 04                     mov dword ptr [r13 + 4], eax
008ACCB1  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
008ACCB9  44 89 38                        mov dword ptr [rax], r15d
008ACCBC  48 C7 40 08 08 00 00 00         mov qword ptr [rax + 8], 8
008ACCC4  44 89 7C 24 44                  mov dword ptr [rsp + 0x44], r15d
008ACCC9  EB 0C                           jmp 0x1408accd7
008ACCCB  44 8B F8                        mov r15d, eax
008ACCCE  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008ACCD2  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008ACCD7  48 8B CF                        mov rcx, rdi
008ACCDA  E8 71 C6 A4 FF                  call 0x1402f9350
008ACCDF  41 8B C7                        mov eax, r15d
008ACCE2  E9 40 FF FF FF                  jmp 0x1408acc27
008ACCE7  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
008ACCEC  E9 F9 FD FF FF                  jmp 0x1408acaea
008ACCF1  49 8B DC                        mov rbx, r12
008ACCF4  48 8D 3D 05 33 75 FF            lea rdi, [rip - 0x8accfb]
008ACCFB  E9 27 FD FF FF                  jmp 0x1408aca27
008ACD00  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
008ACD03  A8 02                           test al, 2
008ACD05  0F 84 EA 00 00 00               je 0x1408acdf5
008ACD0B  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
008ACD0E  A8 02                           test al, 2
008ACD10  0F 85 EE 00 00 00               jne 0x1408ace04
008ACD16  48 8B CF                        mov rcx, rdi
008ACD19  E8 32 C6 A4 FF                  call 0x1402f9350
008ACD1E  B8 9A 00 00 C0                  mov eax, 0xc000009a
008ACD23  E9 FF FE FF FF                  jmp 0x1408acc27
008ACD28  C7 43 10 04 00 00 00            mov dword ptr [rbx + 0x10], 4
008ACD2F  48 8D 44 24 70                  lea rax, [rsp + 0x70]
008ACD34  49 8B CE                        mov rcx, r14
008ACD37  E9 2E FE FF FF                  jmp 0x1408acb6a
008ACD3C  48 8B CB                        mov rcx, rbx
008ACD3F  E8 00 57 9C FF                  call 0x140272444
008ACD44  0F B6 C8                        movzx ecx, al
008ACD47  E9 3E FF FF FF                  jmp 0x1408acc8a
008ACD4C  BA 18 00 00 00                  mov edx, 0x18
008ACD51  8D 4A 28                        lea ecx, [rdx + 0x28]
008ACD54  41 B8 49 6F 45 76               mov r8d, 0x76456f49
008ACD5A  E8 91 53 2D 00                  call 0x140b820f0
008ACD5F  4C 8B F0                        mov r14, rax
008ACD62  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008ACD67  48 85 C0                        test rax, rax
008ACD6A  74 AA                           je 0x1408acd16
008ACD6C  45 33 C0                        xor r8d, r8d
008ACD6F  41 8D 50 01                     lea edx, [r8 + 1]
008ACD73  48 8B C8                        mov rcx, rax
008ACD76  E8 95 0F B6 FF                  call 0x14040dd10
008ACD7B  E9 96 FD FF FF                  jmp 0x1408acb16
008ACD80  41 BF 04 00 00 C0               mov r15d, 0xc0000004
008ACD86  48 8B CF                        mov rcx, rdi
008ACD89  E8 C2 C5 A4 FF                  call 0x1402f9350
008ACD8E  41 8B C7                        mov eax, r15d
008ACD91  E9 91 FE FF FF                  jmp 0x1408acc27
008ACD96  B8 03 00 00 C0                  mov eax, 0xc0000003
008ACD9B  E9 87 FE FF FF                  jmp 0x1408acc27
008ACDA0  48 8B CF                        mov rcx, rdi
008ACDA3  E8 A8 C5 A4 FF                  call 0x1402f9350
008ACDA8  8B C3                           mov eax, ebx
008ACDAA  E9 78 FE FF FF                  jmp 0x1408acc27
008ACDAF  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
008ACDB4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008ACDB9  4C 8B C8                        mov r9, rax
008ACDBC  44 0F B6 C6                     movzx r8d, sil
008ACDC0  0F B6 54 24 41                  movzx edx, byte ptr [rsp + 0x41]
008ACDC5  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008ACDCA  48 8B CF                        mov rcx, rdi
008ACDCD  E8 06 19 00 00                  call 0x1408ae6d8
008ACDD2  8B D8                           mov ebx, eax
008ACDD4  E9 01 FD FF FF                  jmp 0x1408acada
008ACDD9  48 8B CF                        mov rcx, rdi
008ACDDC  E8 6F C5 A4 FF                  call 0x1402f9350
008ACDE1  B8 10 00 00 C0                  mov eax, 0xc0000010
008ACDE6  E9 3C FE FF FF                  jmp 0x1408acc27
008ACDEB  B8 04 00 00 C0                  mov eax, 0xc0000004
008ACDF0  E9 32 FE FF FF                  jmp 0x1408acc27
008ACDF5  33 D2                           xor edx, edx
008ACDF7  49 8B CE                        mov rcx, r14
008ACDFA  E8 71 5A 2D 00                  call 0x140b82870
008ACDFF  E9 07 FF FF FF                  jmp 0x1408acd0b
008ACE04  48 8B CF                        mov rcx, rdi
008ACE07  E8 84 3C 9A FF                  call 0x140250a90
008ACE0C  E9 05 FF FF FF                  jmp 0x1408acd16
008ACE11  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
008ACE14  D1 E8                           shr eax, 1
008ACE16  24 01                           and al, 1
008ACE18  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008ACE1C  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
008ACE21  45 33 C0                        xor r8d, r8d
008ACE24  48 8B CF                        mov rcx, rdi
008ACE27  E8 9C 17 00 00                  call 0x1408ae5c8
008ACE2C  B8 9A 00 00 C0                  mov eax, 0xc000009a
008ACE31  E9 F1 FD FF FF                  jmp 0x1408acc27
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryVolumeInformationFile(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned __int8 v_stack_m3F;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int8 v_stack_m66;
    unsigned __int8 v_stack_m67;
    unsigned __int8 v_stack_m68;
    unsigned int v_stack_m78;
    unsigned __int8 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = a4;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    v_r15 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m40 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m67 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008ACCF1;
    if (((unsigned int)((int)(a5))) >= 16) goto loc_008ACD96;
    if ((unsigned __int8)(*(unsigned __int8 *)((int)(a5) + v_rip - 9095479 * 1 + 11841824)) == 0) goto loc_008ACD96;
    if (a4 < ((unsigned int)(*(unsigned __int8 *)((int)(a5) + v_rip - 9095479 * 1 + 11841824)))) goto loc_008ACDEB;
    a1 = v_r11;
    if (a2 < v_r11) { a1 = a2; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_008AC998;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) != 332) goto loc_008AC98E;
loc_008AC98A:
    goto loc_008AC99A;
loc_008AC98E:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 452) goto loc_008AC98A;
loc_008AC998:
    result = 0;
loc_008AC99A:
    v_stack_m66 = 0;
    if (0 != 0) goto loc_008AC9FB;
    if ((unsigned int)(a4) == 0) goto loc_008AC9F8;
    if (((a3) & (*(unsigned __int8 *)((int)(a5) + v_rip - 9095479 * 1 + 11843104) - 1)) != 0) goto loc_008ACA1A;
    a2 = (a3 - 1) + ((unsigned int)(a4));
    if (a3 > a2) goto loc_008ACA14;
    if (a2 >= v_r11) goto loc_008ACA14;
    a2 = (a2) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a2) + (0x1000ULL);
loc_008AC9E0:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    result = (a3) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != a2) goto loc_008AC9E0;
    goto loc_008ACA20;
loc_008AC9F8:
    goto loc_008ACA20;
loc_008AC9FB:
    result = ProbeForWrite(a3, (unsigned int)(a4), 4, (unsigned int)(a4));
    goto loc_008ACA20;
loc_008ACA14:
    result = ExRaiseAccessViolation(a3, (unsigned int)(a4), v_stack_m67, (unsigned int)(a4));
loc_008ACA1A:
    result = ExRaiseDatatypeMisalignment(a3, (unsigned int)(a4), v_stack_m67, (unsigned int)(a4));
loc_008ACA20:
    goto loc_008ACA27;
loc_008ACA27:
    v_stack_m88 = 0;
    result = IopReferenceFileObject(a1, (unsigned int)(*(unsigned int *)(v_rip - 9095479 + (int)(a5) * 4 + 11848416)), v_stack_m67, v_stack_m60);
    v_stack_m64 = (unsigned int)(result);
    if (sign_flag) goto loc_008ACC27;
    v_stack_m48 = v_stack_m60 + 80;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60 + 80))))) & (0x800ULL));
    if (condition_is_not_equal) goto loc_008ACC45;
    if (((unsigned int)((int)(a5))) == 4) goto loc_008ACC4F;
loc_008ACA74:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m60 + 80)))) & (2)) == 0) goto loc_008ACCE7;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m60 + 80))) >> (2));
    v_rsi = (unsigned __int8)((v_rsi) & (1));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m60 + 128, a2, a3, v_stack_m60);
    v_stack_m68 = 0;
    if (1 != 0) goto loc_008ACDAF;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(v_stack_m60, a2, a3, v_stack_m60);
loc_008ACADA:
    if (v_stack_m68 != 0) goto loc_008ACDA0;
    v_stack_m68 = 1;
loc_008ACAEA:
    result = IopResetEvent(v_stack_m60, a2, a3, v_stack_m60);
    result = IoGetRelatedDeviceObject(v_stack_m60, a2, a3, v_stack_m60);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m60 + 80)))) & (2)) == 0) goto loc_008ACD4C;
loc_008ACB16:
    a3 = 0;
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, v_stack_m60);
    if (result == 0) goto loc_008ACD00;
    *(unsigned __int64 *)(result + 192) = v_stack_m60;
    *(unsigned __int64 *)(result + 152) = v_stack_m40;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_m67);
    v_stack_m38 = v_xmm0;
    if (v_stack_m68 == 0) goto loc_008ACD28;
loc_008ACB6A:
    *(unsigned __int64 *)(result + 80) = 0;
    *(unsigned __int64 *)(result + 72) = v_stack_p10;
    *(unsigned __int64 *)(result + 88) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72) = 10;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = v_stack_m60;
    *(unsigned __int64 *)(result + 112) = 0;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    result = ExAllocatePool2(65, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), (unsigned int)(0x42536F49ULL), v_stack_m60);
    *(unsigned __int64 *)(result + 24) = result;
    if (result == 0) goto loc_008ACE11;
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 56) = (unsigned int)((int)(a5));
    v_stack_m78 = 2;
    v_stack_m80 = (unsigned __int8)(v_stack_m68);
    v_stack_m88 = (unsigned __int8)(v_stack_m67);
    result = IopSynchronousServiceTail(result, result, v_stack_m60, 1);
    if ((unsigned __int8)(v_stack_m68) == 0) {
        a1 = v_stack_p10;
        v_stack_m80 = a1;
        a1 = v_stack_m38;
        v_stack_m88 = a1;
        a4 = (unsigned __int8)(v_stack_m67);
        a3 = result;
        a2 = v_stack_m58;
        a1 = (unsigned int)(result);
        result = IopSynchronousApiServiceTail(a1, a2, a3, a4);
    }
    return result;
loc_008ACC45:
    if (((unsigned int)((int)(a5))) != 4) goto loc_008ACDD9;
loc_008ACC4F:
    if ((unsigned int)(result) != 0) goto loc_008ACC61;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m60 + 8) + 72)) == 20) goto loc_008ACA74;
loc_008ACC61:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m60 + 8) + 56) == 0) goto loc_008ACC8A;
    if ((*(unsigned __int64 *)(v_stack_m60 + 16)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m60 + 8) + 56))) goto loc_008ACD3C;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m60 + 16) + 4)) & (1));
loc_008ACC8A:
    if (v_stack_p48 < 8) goto loc_008ACD80;
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m60 + 8) + 72)));
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m60 + 8) + 52)));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m60 + 8) + 52));
    if ((unsigned int)(a1) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m60 + 8) + 52))) | (32));
        *(unsigned int *)(a3 + 4) = (unsigned int)(result);
    }
    *(unsigned int *)(v_stack_p38) = (unsigned int)(v_stack_m67);
    *(unsigned __int64 *)(v_stack_p38 + 8) = 8;
    v_stack_m3C = (unsigned int)(v_stack_m67);
    goto loc_008ACCD7;
loc_008ACCD7:
    result = ObfDereferenceObject(v_stack_m38, a2, a3, a4);
    goto loc_008ACC27;
loc_008ACCE7:
    v_stack_m40 = 0;
    goto loc_008ACAEA;
loc_008ACCF1:
    goto loc_008ACA27;
loc_008ACD00:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 9096443 + 80)))) & (2)) == 0) goto loc_008ACDF5;
loc_008ACD0B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 9096443 + 80)))) & (2)) != 0) goto loc_008ACE04;
loc_008ACD16:
    result = ObfDereferenceObject(v_rip - 9096443, a2, a3, a4);
    goto loc_008ACC27;
loc_008ACD28:
    *(unsigned int *)((int)(a5) + 16) = 4;
    goto loc_008ACB6A;
loc_008ACD3C:
    result = IopGetMountFlag((int)(a5), a2, a3, a4);
    goto loc_008ACC8A;
loc_008ACD4C:
    result = ExAllocatePool2(24 + 40, 24, (unsigned int)(0x76456F49ULL), a4);
    v_stack_m30 = result;
    if (result == 0) goto loc_008ACD16;
    a3 = 0;
    result = KeInitializeEvent(result, a3 + 1, a3, a4);
    goto loc_008ACB16;
loc_008ACD80:
    result = ObfDereferenceObject(v_rip - 9096443, a3 + 1, a3, a4);
    goto loc_008ACC27;
loc_008ACD96:
    goto loc_008ACC27;
loc_008ACDA0:
    result = ObfDereferenceObject(v_rip - 9096443, a3 + 1, a3, a4);
    goto loc_008ACC27;
loc_008ACDAF:
    v_stack_m60 = v_stack_m40;
    result = IopWaitAndAcquireFileObjectLock(v_stack_m38, v_stack_m3F, (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)), (unsigned int)((unsigned int)((int)(a5))));
    goto loc_008ACADA;
loc_008ACDD9:
    result = ObfDereferenceObject(v_stack_m38, v_stack_m3F, (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)), (unsigned int)((unsigned int)((int)(a5))));
    goto loc_008ACC27;
loc_008ACDEB:
    goto loc_008ACC27;
loc_008ACDF5:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)), (unsigned int)((unsigned int)((int)(a5))));
    goto loc_008ACD0B;
loc_008ACE04:
    result = IopReleaseFileObjectLock(v_stack_m38, a2, (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)), (unsigned int)((unsigned int)((int)(a5))));
    goto loc_008ACD16;
loc_008ACE11:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m38 + 80))) >> (1));
    result = (unsigned __int8)((result) & (1));
    v_stack_m60 = (unsigned __int8)(result);
    a3 = 0;
    result = IopExceptionCleanupEx(v_stack_m38, a2, a3, v_stack_m30);
    goto loc_008ACC27;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryVolumeInformationFile(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint8_t v_stack_m3F;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint8_t v_stack_m66;
    uint8_t v_stack_m67;
    uint8_t v_stack_m68;
    uint32_t v_stack_m78;
    uint8_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p38;
    uint32_t v_stack_p48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = Arg4;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    local_r15 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m40 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m67 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008ACCF1;
    if (((uint32_t)((int32_t)(Arg5))) >= 16) goto loc_008ACD96;
    if ((uint8_t)(*(uint8_t *)((int32_t)(Arg5) + v_rip - 0x8AC937 * 1 + 0xB4B120)) == 0) goto loc_008ACD96;
    if (Arg4 < ((uint32_t)(*(uint8_t *)((int32_t)(Arg5) + v_rip - 0x8AC937 * 1 + 0xB4B120)))) goto loc_008ACDEB;
    Arg1 = local_r11;
    if (Arg2 < local_r11) { Arg1 = Arg2; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_008AC998;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) != 332) goto loc_008AC98E;
loc_008AC98A:
    goto loc_008AC99A;
loc_008AC98E:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 452) goto loc_008AC98A;
loc_008AC998:
    result = 0;
loc_008AC99A:
    v_stack_m66 = 0;
    if (0 != 0) goto loc_008AC9FB;
    if ((uint32_t)(Arg4) == 0) goto loc_008AC9F8;
    if (((Arg3) & (*(uint8_t *)((int32_t)(Arg5) + v_rip - 0x8AC937 * 1 + 0xB4B620) - 1)) != 0) goto loc_008ACA1A;
    Arg2 = (Arg3 - 1) + ((uint32_t)(Arg4));
    if (Arg3 > Arg2) goto loc_008ACA14;
    if (Arg2 >= local_r11) goto loc_008ACA14;
    Arg2 = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg2) + (0x1000ULL);
loc_008AC9E0:
    *(uint8_t *)(arg3) = (uint8_t)(*(uint8_t *)(arg3));
    result = (Arg3) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != Arg2) goto loc_008AC9E0;
    goto loc_008ACA20;
loc_008AC9F8:
    goto loc_008ACA20;
loc_008AC9FB:
    result = ProbeForWrite(Arg3, (uint32_t)(Arg4), 4, (uint32_t)(Arg4));
    goto loc_008ACA20;
loc_008ACA14:
    result = ExRaiseAccessViolation(Arg3, (uint32_t)(Arg4), v_stack_m67, (uint32_t)(Arg4));
loc_008ACA1A:
    result = ExRaiseDatatypeMisalignment(Arg3, (uint32_t)(Arg4), v_stack_m67, (uint32_t)(Arg4));
loc_008ACA20:
    goto loc_008ACA27;
loc_008ACA27:
    v_stack_m88 = 0;
    result = IopReferenceFileObject(Arg1, (uint32_t)(*(uint32_t *)(v_rip - 0x8AC937 + (int32_t)(Arg5) * 4 + 0xB4CAE0)), v_stack_m67, v_stack_m60);
    v_stack_m64 = (uint32_t)(result);
    if (sign_flag) goto loc_008ACC27;
    v_stack_m48 = v_stack_m60 + 80;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x50))))) & (0x800ULL));
    if (condition_is_not_equal) goto loc_008ACC45;
    if (((uint32_t)((int32_t)(Arg5))) == 4) goto loc_008ACC4F;
loc_008ACA74:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x50)))) & (2)) == 0) goto loc_008ACCE7;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x50))) >> (2));
    local_rsi = (uint8_t)((local_rsi) & (1));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m60 + 128, Arg2, Arg3, v_stack_m60);
    v_stack_m68 = 0;
    if (1 != 0) goto loc_008ACDAF;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(v_stack_m60, Arg2, Arg3, v_stack_m60);
loc_008ACADA:
    if (v_stack_m68 != 0) goto loc_008ACDA0;
    v_stack_m68 = 1;
loc_008ACAEA:
    result = IopResetEvent(v_stack_m60, Arg2, Arg3, v_stack_m60);
    result = IoGetRelatedDeviceObject(v_stack_m60, Arg2, Arg3, v_stack_m60);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x50)))) & (2)) == 0) goto loc_008ACD4C;
loc_008ACB16:
    Arg3 = 0;
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, v_stack_m60);
    if (result == 0) goto loc_008ACD00;
    *(uint64_t *)(result + 0xC0) = v_stack_m60;
    *(uint64_t *)(result + 0x98) = v_stack_m40;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_m67);
    v_stack_m38 = v_xmm0;
    if (v_stack_m68 == 0) goto loc_008ACD28;
loc_008ACB6A:
    *(uint64_t *)(result + 0x50) = 0;
    *(uint64_t *)(result + 0x48) = v_stack_p10;
    *(uint64_t *)(result + 0x58) = 0;
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 10;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x18) = v_stack_m60;
    *(uint64_t *)(result + 0x70) = 0;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    result = ExAllocatePool2(65, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), (uint32_t)(0x42536F49ULL), v_stack_m60);
    *(uint64_t *)(result + 0x18) = result;
    if (result == 0) goto loc_008ACE11;
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = (uint32_t)((int32_t)(Arg5));
    v_stack_m78 = 2;
    v_stack_m80 = (uint8_t)(v_stack_m68);
    v_stack_m88 = (uint8_t)(v_stack_m67);
    result = IopSynchronousServiceTail(result, result, v_stack_m60, 1);
    if ((uint8_t)(v_stack_m68) == 0) {
        Arg1 = v_stack_p10;
        v_stack_m80 = Arg1;
        Arg1 = v_stack_m38;
        v_stack_m88 = Arg1;
        Arg4 = (uint8_t)(v_stack_m67);
        Arg3 = result;
        Arg2 = v_stack_m58;
        Arg1 = (uint32_t)(result);
        result = IopSynchronousApiServiceTail(Arg1, Arg2, Arg3, Arg4);
    }
    return result;
loc_008ACC45:
    if (((uint32_t)((int32_t)(Arg5))) != 4) goto loc_008ACDD9;
loc_008ACC4F:
    if ((uint32_t)(result) != 0) goto loc_008ACC61;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m60 + 0x8) + 0x48)) == 20) goto loc_008ACA74;
loc_008ACC61:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m60 + 0x8) + 0x38) == 0) goto loc_008ACC8A;
    if ((*(uint64_t *)(v_stack_m60 + 0x10)) != (*(uint64_t *)(*(uint64_t *)(v_stack_m60 + 0x8) + 0x38))) goto loc_008ACD3C;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_m60 + 0x10) + 0x4)) & (1));
loc_008ACC8A:
    if (v_stack_p48 < 8) goto loc_008ACD80;
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m60 + 0x8) + 0x48)));
    *(uint32_t *)(arg3 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m60 + 0x8) + 0x34)));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m60 + 0x8) + 0x34));
    if ((uint32_t)(Arg1) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m60 + 0x8) + 0x34))) | (32));
        *(uint32_t *)(arg3 + 0x4) = (uint32_t)(result);
    }
    *(uint32_t *)(v_stack_p38) = (uint32_t)(v_stack_m67);
    *(uint64_t *)(v_stack_p38 + 0x8) = 8;
    v_stack_m3C = (uint32_t)(v_stack_m67);
    goto loc_008ACCD7;
loc_008ACCD7:
    result = ObfDereferenceObject(v_stack_m38, Arg2, Arg3, Arg4);
    goto loc_008ACC27;
loc_008ACCE7:
    v_stack_m40 = 0;
    goto loc_008ACAEA;
loc_008ACCF1:
    goto loc_008ACA27;
loc_008ACD00:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x8ACCFB + 0x50)))) & (2)) == 0) goto loc_008ACDF5;
loc_008ACD0B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x8ACCFB + 0x50)))) & (2)) != 0) goto loc_008ACE04;
loc_008ACD16:
    result = ObfDereferenceObject(v_rip - 9096443, Arg2, Arg3, Arg4);
    goto loc_008ACC27;
loc_008ACD28:
    *(uint32_t *)((int32_t)(Arg5) + 0x10) = 4;
    goto loc_008ACB6A;
loc_008ACD3C:
    result = IopGetMountFlag((int32_t)(Arg5), Arg2, Arg3, Arg4);
    goto loc_008ACC8A;
loc_008ACD4C:
    result = ExAllocatePool2(24 + 40, 24, (uint32_t)(0x76456F49ULL), Arg4);
    v_stack_m30 = result;
    if (result == 0) goto loc_008ACD16;
    Arg3 = 0;
    result = KeInitializeEvent(result, Arg3 + 1, Arg3, Arg4);
    goto loc_008ACB16;
loc_008ACD80:
    result = ObfDereferenceObject(v_rip - 9096443, Arg3 + 1, Arg3, Arg4);
    goto loc_008ACC27;
loc_008ACD96:
    goto loc_008ACC27;
loc_008ACDA0:
    result = ObfDereferenceObject(v_rip - 9096443, Arg3 + 1, Arg3, Arg4);
    goto loc_008ACC27;
loc_008ACDAF:
    v_stack_m60 = v_stack_m40;
    result = IopWaitAndAcquireFileObjectLock(v_stack_m38, v_stack_m3F, (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)), (uint32_t)((uint32_t)((int32_t)(Arg5))));
    goto loc_008ACADA;
loc_008ACDD9:
    result = ObfDereferenceObject(v_stack_m38, v_stack_m3F, (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)), (uint32_t)((uint32_t)((int32_t)(Arg5))));
    goto loc_008ACC27;
loc_008ACDEB:
    goto loc_008ACC27;
loc_008ACDF5:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)), (uint32_t)((uint32_t)((int32_t)(Arg5))));
    goto loc_008ACD0B;
loc_008ACE04:
    result = IopReleaseFileObjectLock(v_stack_m38, Arg2, (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)), (uint32_t)((uint32_t)((int32_t)(Arg5))));
    goto loc_008ACD16;
loc_008ACE11:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m38 + 0x50))) >> (1));
    result = (uint8_t)((result) & (1));
    v_stack_m60 = (uint8_t)(result);
    Arg3 = 0;
    result = IopExceptionCleanupEx(v_stack_m38, Arg2, Arg3, v_stack_m30);
    goto loc_008ACC27;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AC8C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
