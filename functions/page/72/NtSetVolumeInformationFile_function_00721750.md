# NtSetVolumeInformationFile

- RVA: `0x00721750`–`0x00721CA1` (길이 `1,361` bytes)
- VA: `0x0000000140721750`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C78FC`
- 디코드: `336`개 명령, `1,361/1,361` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00721867` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00721888` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x007218DE` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x007218F8` → [IoGetRelatedTargetDevice](../A6/IoGetRelatedTargetDevice_function_00A6DBFC.md) (function, `0x00A6DBFC`)
- `0x0072194F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00721974` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00721999` → [IopWaitAndAcquireFileObjectLock](../8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x007219AA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x007219B9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x007219DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007219F2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00721A02` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x00721A10` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x00721A18` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x00721A2E` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x00721A50` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00721A5A` → [IopAllocateIrpCleanup](../A1/IopAllocateIrpCleanup_function_00A1E2D4.md) (function, `0x00A1E2D4`)
- `0x00721A67` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00721AF2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00721B06` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00721B4D` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x00721B5A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00721BA9` → [IopSynchronousServiceTail](../8E/IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)
- `0x00721BDC` → [IopSynchronousApiServiceTail](../8A/IopSynchronousApiServiceTail_function_008ACE3C.md) (function, `0x008ACE3C`)
- `0x00721C36` → [IoReportTargetDeviceChange](../A6/IoReportTargetDeviceChange_function_00A66F20.md) (function, `0x00A66F20`)
- `0x00721C67` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x00721C76` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00721C88` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00721763` → RVA `0x00E0A740` (`.data`; read)
- `0x007217D6` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00721C1B` → RVA `0x00026BA0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x007218DE` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x0072194F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00721974` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x007219AA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x007219B9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x007219DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007219F2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00721A02` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x00721A10` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x00721A18` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x00721A2E` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x00721A50` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00721A67` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00721AF2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00721B06` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00721B5A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00721C76` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00721C88` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00721750  40 53                           push rbx
00721752  56                              push rsi
00721753  57                              push rdi
00721754  41 54                           push r12
00721756  41 55                           push r13
00721758  41 56                           push r14
0072175A  41 57                           push r15
0072175C  48 81 EC D0 00 00 00            sub rsp, 0xd0
00721763  48 8B 05 D6 8F 6E 00            mov rax, qword ptr [rip + 0x6e8fd6]
0072176A  48 33 C4                        xor rax, rsp
0072176D  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00721775  44 89 4C 24 44                  mov dword ptr [rsp + 0x44], r9d
0072177A  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
0072177F  48 8B F2                        mov rsi, rdx
00721782  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
00721787  48 8B D9                        mov rbx, rcx
0072178A  45 33 E4                        xor r12d, r12d
0072178D  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00721792  45 8B EC                        mov r13d, r12d
00721795  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
0072179A  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0072179F  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
007217A8  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
007217AD  44 8A 9F 32 02 00 00            mov r11b, byte ptr [rdi + 0x232]
007217B4  44 88 5C 24 41                  mov byte ptr [rsp + 0x41], r11b
007217B9  45 84 DB                        test r11b, r11b
007217BC  0F 84 EF 00 00 00               je 0x1407218b1
007217C2  48 63 84 24 30 01 00 00         movsxd rax, dword ptr [rsp + 0x130]
007217CA  83 F8 10                        cmp eax, 0x10
007217CD  0F 83 D4 00 00 00               jae 0x1407218a7
007217D3  48 8B D0                        mov rdx, rax
007217D6  4C 8D 15 23 E8 8D FF            lea r10, [rip - 0x7217dd]
007217DD  42 0F B6 84 10 38 B1 B4 00      movzx eax, byte ptr [rax + r10 + 0xb4b138]
007217E6  84 C0                           test al, al
007217E8  0F 84 B9 00 00 00               je 0x1407218a7
007217EE  44 3B C8                        cmp r9d, eax
007217F1  73 0A                           jae 0x1407217fd
007217F3  B8 04 00 00 C0                  mov eax, 0xc0000004
007217F8  E9 80 04 00 00                  jmp 0x140721c7d
007217FD  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
00721807  49 8B CE                        mov rcx, r14
0072180A  49 3B F6                        cmp rsi, r14
0072180D  48 0F 42 CE                     cmovb rcx, rsi
00721811  8B 01                           mov eax, dword ptr [rcx]
00721813  89 01                           mov dword ptr [rcx], eax
00721815  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
0072181C  4C 39 A0 10 03 00 00            cmp qword ptr [rax + 0x310], r12
00721823  74 47                           je 0x14072186c
00721825  0F B7 80 EC 06 00 00            movzx eax, word ptr [rax + 0x6ec]
0072182C  B9 4C 01 00 00                  mov ecx, 0x14c
00721831  66 3B C1                        cmp ax, cx
00721834  74 15                           je 0x14072184b
00721836  B9 C4 01 00 00                  mov ecx, 0x1c4
0072183B  66 3B C1                        cmp ax, cx
0072183E  74 0B                           je 0x14072184b
00721840  41 8A C4                        mov al, r12b
00721843  41 BF 01 00 00 00               mov r15d, 1
00721849  EB 09                           jmp 0x140721854
0072184B  41 BF 01 00 00 00               mov r15d, 1
00721851  41 8A C7                        mov al, r15b
00721854  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00721858  84 C0                           test al, al
0072185A  74 16                           je 0x140721872
0072185C  45 85 C9                        test r9d, r9d
0072185F  74 3F                           je 0x1407218a0
00721861  41 F6 C0 03                     test r8b, 3
00721865  74 26                           je 0x14072188d
00721867  E8 64 87 17 00                  call 0x140899fd0
0072186C  41 BF 01 00 00 00               mov r15d, 1
00721872  45 85 C9                        test r9d, r9d
00721875  74 29                           je 0x1407218a0
00721877  42 0F B6 84 12 20 B6 B4 00      movzx eax, byte ptr [rdx + r10 + 0xb4b620]
00721880  49 2B C7                        sub rax, r15
00721883  49 85 C0                        test r8, rax
00721886  74 05                           je 0x14072188d
00721888  E8 43 87 17 00                  call 0x140899fd0
0072188D  41 8B C9                        mov ecx, r9d
00721890  49 03 C8                        add rcx, r8
00721893  49 3B CE                        cmp rcx, r14
00721896  77 05                           ja 0x14072189d
00721898  49 3B C8                        cmp rcx, r8
0072189B  73 03                           jae 0x1407218a0
0072189D  41 8A 06                        mov al, byte ptr [r14]
007218A0  EB 24                           jmp 0x1407218c6
007218A2  E9 D6 03 00 00                  jmp 0x140721c7d
007218A7  B8 03 00 00 C0                  mov eax, 0xc0000003
007218AC  E9 CC 03 00 00                  jmp 0x140721c7d
007218B1  48 63 94 24 30 01 00 00         movsxd rdx, dword ptr [rsp + 0x130]
007218B9  4C 8D 15 40 E7 8D FF            lea r10, [rip - 0x7218c0]
007218C0  41 BF 01 00 00 00               mov r15d, 1
007218C6  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
007218CB  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
007218D0  45 8A C3                        mov r8b, r11b
007218D3  41 8B 94 92 30 CB B4 00         mov edx, dword ptr [r10 + rdx*4 + 0xb4cb30]
007218DB  48 8B CB                        mov rcx, rbx
007218DE  E8 4D BC B7 FF                  call 0x14029d530
007218E3  85 C0                           test eax, eax
007218E5  0F 88 92 03 00 00               js 0x140721c7d
007218EB  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007218F0  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
007218F5  49 8B CE                        mov rcx, r14
007218F8  E8 FF C2 34 00                  call 0x140a6dbfc
007218FD  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00721902  85 C0                           test eax, eax
00721904  49 0F 48 FC                     cmovs rdi, r12
00721908  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
0072190D  4D 8D 66 50                     lea r12, [r14 + 0x50]
00721911  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
00721916  41 8B 34 24                     mov esi, dword ptr [r12]
0072191A  40 F6 C6 02                     test sil, 2
0072191E  0F 84 AB 00 00 00               je 0x1407219cf
00721924  C1 EE 02                        shr esi, 2
00721927  41 22 F7                        and sil, r15b
0072192A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00721933  83 C9 FF                        or ecx, 0xffffffff
00721936  66 01 88 E4 01 00 00            add word ptr [rax + 0x1e4], cx
0072193D  90                              nop
0072193E  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00721943  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
0072194A  45 33 C0                        xor r8d, r8d
0072194D  33 D2                           xor edx, edx
0072194F  E8 DC E8 AE FF                  call 0x140210230
00721954  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
00721959  41 8B CF                        mov ecx, r15d
0072195C  87 4B 74                        xchg dword ptr [rbx + 0x74], ecx
0072195F  85 C9                           test ecx, ecx
00721961  75 1A                           jne 0x14072197d
00721963  48 85 C0                        test rax, rax
00721966  74 04                           je 0x14072196c
00721968  44 88 78 0A                     mov byte ptr [rax + 0xa], r15b
0072196C  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00721971  49 8B CE                        mov rcx, r14
00721974  E8 A7 E0 AE FF                  call 0x14020fa20
00721979  33 DB                           xor ebx, ebx
0072197B  EB 23                           jmp 0x1407219a0
0072197D  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00721982  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00721987  4C 8B C8                        mov r9, rax
0072198A  44 8A C6                        mov r8b, sil
0072198D  8A 54 24 41                     mov dl, byte ptr [rsp + 0x41]
00721991  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00721996  49 8B CE                        mov rcx, r14
00721999  E8 3A CD 18 00                  call 0x1408ae6d8
0072199E  8B D8                           mov ebx, eax
007219A0  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
007219A5  74 1E                           je 0x1407219c5
007219A7  49 8B CE                        mov rcx, r14
007219AA  E8 A1 79 BD FF                  call 0x1402f9350
007219AF  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007219B4  48 85 C9                        test rcx, rcx
007219B7  74 05                           je 0x1407219be
007219B9  E8 92 79 BD FF                  call 0x1402f9350
007219BE  8B C3                           mov eax, ebx
007219C0  E9 B8 02 00 00                  jmp 0x140721c7d
007219C5  41 8A DF                        mov bl, r15b
007219C8  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
007219CD  EB 3A                           jmp 0x140721a09
007219CF  BA 18 00 00 00                  mov edx, 0x18
007219D4  8D 4A 28                        lea ecx, [rdx + 0x28]
007219D7  41 B8 49 6F 45 76               mov r8d, 0x76456f49
007219DD  E8 0E 07 46 00                  call 0x140b820f0
007219E2  4C 8B E8                        mov r13, rax
007219E5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007219EA  48 85 C0                        test rax, rax
007219ED  75 0A                           jne 0x1407219f9
007219EF  49 8B CE                        mov rcx, r14
007219F2  E8 59 79 BD FF                  call 0x1402f9350
007219F7  EB 66                           jmp 0x140721a5f
007219F9  45 33 C0                        xor r8d, r8d
007219FC  41 8B D7                        mov edx, r15d
007219FF  48 8B C8                        mov rcx, rax
00721A02  E8 09 C3 CE FF                  call 0x14040dd10
00721A07  32 DB                           xor bl, bl
00721A09  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
00721A0D  49 8B CE                        mov rcx, r14
00721A10  E8 DB BB B7 FF                  call 0x14029d5f0
00721A15  49 8B CE                        mov rcx, r14
00721A18  E8 03 97 B7 FF                  call 0x14029b120
00721A1D  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00721A25  45 33 C0                        xor r8d, r8d
00721A28  8A 50 4C                        mov dl, byte ptr [rax + 0x4c]
00721A2B  48 8B C8                        mov rcx, rax
00721A2E  E8 ED 5C AE FF                  call 0x140207720
00721A33  48 8B F0                        mov rsi, rax
00721A36  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00721A3E  33 D2                           xor edx, edx
00721A40  48 85 C0                        test rax, rax
00721A43  75 31                           jne 0x140721a76
00721A45  41 8B 04 24                     mov eax, dword ptr [r12]
00721A49  A8 02                           test al, 2
00721A4B  75 08                           jne 0x140721a55
00721A4D  49 8B CD                        mov rcx, r13
00721A50  E8 1B 0E 46 00                  call 0x140b82870
00721A55  33 D2                           xor edx, edx
00721A57  49 8B CE                        mov rcx, r14
00721A5A  E8 75 C8 2F 00                  call 0x140a1e2d4
00721A5F  48 85 FF                        test rdi, rdi
00721A62  74 08                           je 0x140721a6c
00721A64  48 8B CF                        mov rcx, rdi
00721A67  E8 E4 78 BD FF                  call 0x1402f9350
00721A6C  B8 9A 00 00 C0                  mov eax, 0xc000009a
00721A71  E9 07 02 00 00                  jmp 0x140721c7d
00721A76  4C 89 B0 C0 00 00 00            mov qword ptr [rax + 0xc0], r14
00721A7D  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00721A82  48 89 86 98 00 00 00            mov qword ptr [rsi + 0x98], rax
00721A89  8A 44 24 41                     mov al, byte ptr [rsp + 0x41]
00721A8D  88 46 40                        mov byte ptr [rsi + 0x40], al
00721A90  0F 57 C0                        xorps xmm0, xmm0
00721A93  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
00721A9B  84 DB                           test bl, bl
00721A9D  74 0A                           je 0x140721aa9
00721A9F  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00721AA4  48 8B CA                        mov rcx, rdx
00721AA7  EB 12                           jmp 0x140721abb
00721AA9  C7 46 10 04 00 00 00            mov dword ptr [rsi + 0x10], 4
00721AB0  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00721AB8  49 8B CD                        mov rcx, r13
00721ABB  48 89 4E 50                     mov qword ptr [rsi + 0x50], rcx
00721ABF  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
00721AC3  48 89 56 58                     mov qword ptr [rsi + 0x58], rdx
00721AC7  4C 8B A6 B8 00 00 00            mov r12, qword ptr [rsi + 0xb8]
00721ACE  41 C6 44 24 B8 0B               mov byte ptr [r12 - 0x48], 0xb
00721AD4  4D 89 74 24 E8                  mov qword ptr [r12 - 0x18], r14
00721AD9  48 89 56 18                     mov qword ptr [rsi + 0x18], rdx
00721ADD  48 89 56 08                     mov qword ptr [rsi + 8], rdx
00721AE1  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00721AE5  41 B8 49 6F 53 42               mov r8d, 0x42536f49
00721AEB  8B D3                           mov edx, ebx
00721AED  B9 61 00 00 00                  mov ecx, 0x61
00721AF2  E8 F9 05 46 00                  call 0x140b820f0
00721AF7  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
00721AFB  44 8B C3                        mov r8d, ebx
00721AFE  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00721B03  48 8B C8                        mov rcx, rax
00721B06  E8 35 4D FA FF                  call 0x1406c6840
00721B0B  90                              nop
00721B0C  8A 4C 24 41                     mov cl, byte ptr [rsp + 0x41]
00721B10  84 C9                           test cl, cl
00721B12  74 55                           je 0x140721b69
00721B14  83 BC 24 30 01 00 00 02         cmp dword ptr [rsp + 0x130], 2
00721B1C  75 4B                           jne 0x140721b69
00721B1E  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00721B22  8B 00                           mov eax, dword ptr [rax]
00721B24  85 C0                           test eax, eax
00721B26  78 09                           js 0x140721b31
00721B28  83 C0 04                        add eax, 4
00721B2B  3B 44 24 44                     cmp eax, dword ptr [rsp + 0x44]
00721B2F  76 38                           jbe 0x140721b69
00721B31  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00721B36  8B 00                           mov eax, dword ptr [rax]
00721B38  D1 E8                           shr eax, 1
00721B3A  41 22 C7                        and al, r15b
00721B3D  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00721B41  4D 8B CD                        mov r9, r13
00721B44  45 33 C0                        xor r8d, r8d
00721B47  48 8B D6                        mov rdx, rsi
00721B4A  49 8B CE                        mov rcx, r14
00721B4D  E8 76 CA 18 00                  call 0x1408ae5c8
00721B52  48 85 FF                        test rdi, rdi
00721B55  74 08                           je 0x140721b5f
00721B57  48 8B CF                        mov rcx, rdi
00721B5A  E8 F1 77 BD FF                  call 0x1402f9350
00721B5F  B8 0D 00 00 C0                  mov eax, 0xc000000d
00721B64  E9 14 01 00 00                  jmp 0x140721c7d
00721B69  83 4E 10 30                     or dword ptr [rsi + 0x10], 0x30
00721B6D  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
00721B71  41 89 44 24 C0                  mov dword ptr [r12 - 0x40], eax
00721B76  8B 84 24 30 01 00 00            mov eax, dword ptr [rsp + 0x130]
00721B7D  41 89 44 24 C8                  mov dword ptr [r12 - 0x38], eax
00721B82  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
00721B8A  44 8A 64 24 40                  mov r12b, byte ptr [rsp + 0x40]
00721B8F  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
00721B94  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00721B98  45 33 C9                        xor r9d, r9d
00721B9B  4D 8B C6                        mov r8, r14
00721B9E  48 8B D6                        mov rdx, rsi
00721BA1  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00721BA9  E8 92 98 1C 00                  call 0x1408eb440
00721BAE  8B D8                           mov ebx, eax
00721BB0  45 33 F6                        xor r14d, r14d
00721BB3  45 84 E4                        test r12b, r12b
00721BB6  75 2B                           jne 0x140721be3
00721BB8  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00721BBD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00721BC2  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00721BCA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00721BCF  44 8A 4C 24 41                  mov r9b, byte ptr [rsp + 0x41]
00721BD4  4C 8B C6                        mov r8, rsi
00721BD7  49 8B D5                        mov rdx, r13
00721BDA  8B CB                           mov ecx, ebx
00721BDC  E8 5B B2 18 00                  call 0x1408ace3c
00721BE1  8B D8                           mov ebx, eax
00721BE3  48 85 FF                        test rdi, rdi
00721BE6  0F 84 D2 FD FF FF               je 0x1407219be
00721BEC  85 DB                           test ebx, ebx
00721BEE  78 4B                           js 0x140721c3b
00721BF0  44 89 B4 24 B4 00 00 00         mov dword ptr [rsp + 0xb4], r14d
00721BF8  44 89 B4 24 C4 00 00 00         mov dword ptr [rsp + 0xc4], r14d
00721C00  C7 84 24 A0 00 00 00 01 00 24 00  mov dword ptr [rsp + 0xa0], 0x240001
00721C0B  4C 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r14
00721C13  83 8C 24 C0 00 00 00 FF         or dword ptr [rsp + 0xc0], 0xffffffff
00721C1B  0F 10 05 7E 4F 90 FF            movups xmm0, xmmword ptr [rip - 0x6fb082]
00721C22  F3 0F 7F 84 24 A4 00 00 00      movdqu xmmword ptr [rsp + 0xa4], xmm0
00721C2B  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
00721C33  48 8B CF                        mov rcx, rdi
00721C36  E8 E5 52 34 00                  call 0x140a66f20
00721C3B  48 8B CF                        mov rcx, rdi
00721C3E  E9 76 FD FF FF                  jmp 0x1407219b9
00721C43  8B D8                           mov ebx, eax
00721C45  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00721C4A  0F B6 51 50                     movzx edx, byte ptr [rcx + 0x50]
00721C4E  D1 EA                           shr edx, 1
00721C50  83 E2 01                        and edx, 1
00721C53  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
00721C57  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
00721C5C  45 33 C0                        xor r8d, r8d
00721C5F  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00721C67  E8 5C C9 18 00                  call 0x1408ae5c8
00721C6C  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00721C71  48 85 C9                        test rcx, rcx
00721C74  74 05                           je 0x140721c7b
00721C76  E8 D5 76 BD FF                  call 0x1402f9350
00721C7B  8B C3                           mov eax, ebx
00721C7D  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00721C85  48 33 CC                        xor rcx, rsp
00721C88  E8 B3 A9 F8 FF                  call 0x1406ac640
00721C8D  48 81 C4 D0 00 00 00            add rsp, 0xd0
00721C94  41 5F                           pop r15
00721C96  41 5E                           pop r14
00721C98  41 5D                           pop r13
00721C9A  41 5C                           pop r12
00721C9C  5F                              pop rdi
00721C9D  5E                              pop rsi
00721C9E  5B                              pop rbx
00721C9F  C3                              ret
00721CA0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetVolumeInformationFile(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int8 v_stack_mC7;
    unsigned __int8 v_stack_mC8;
    unsigned int v_stack_mD8;
    unsigned __int8 v_stack_mE0;
    unsigned __int64 v_stack_mE8;

    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 7245782)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mC4 = a4;
    v_stack_m98 = a3;
    v_stack_mB0 = a2;
    v_r12 = 0;
    v_stack_mC0 = 0;
    v_stack_mA8 = 0;
    v_stack_mB8 = 0;
    v_stack_mA0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_mC7 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_007218B1;
    if (((unsigned int)((int)(a5))) >= 16) goto loc_007218A7;
    if ((unsigned __int8)(*(unsigned __int8 *)((int)(a5) + v_rip - 7477213 * 1 + 11841848)) == 0) goto loc_007218A7;
    if (a4 >= ((unsigned int)(*(unsigned __int8 *)((int)(a5) + v_rip - 7477213 * 1 + 11841848)))) goto loc_007217FD;
    goto loc_00721C7D;
loc_007217FD:
    a1 = v_r14;
    if (a2 < v_r14) { a1 = a2; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_0072186C;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 332) goto loc_0072184B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 452) goto loc_0072184B;
    goto loc_00721854;
loc_0072184B:
loc_00721854:
    v_stack_mC8 = 1;
    if (1 == 0) goto loc_00721872;
    if (a4 == 0) goto loc_007218A0;
    if ((((unsigned __int8)(a3)) & (3)) == 0) goto loc_0072188D;
    result = ExRaiseDatatypeMisalignment(452, (int)(a5), a3, a4);
loc_0072186C:
loc_00721872:
    if (a4 == 0) goto loc_007218A0;
    result = (*(unsigned __int8 *)((int)(a5) + v_rip - 7477213 * 1 + 11843104)) - (1);
    if (((a3) & (result)) != 0) {
        result = ExRaiseDatatypeMisalignment(452, (int)(a5), a3, a4);
    }
    a1 = ((unsigned int)(a4)) + (a3);
    if (a1 > v_r14) goto loc_0072189D;
    if (a1 < a3) {
        result = *(unsigned __int8 *)(v_r14);
    }
    goto loc_007218C6;
loc_007218A7:
    goto loc_00721C7D;
loc_007218B1:
loc_007218C6:
    v_stack_mE8 = 0;
    result = IopReferenceFileObject(a1, (unsigned int)(*(unsigned int *)(v_rip - 7477440 + (int)(a5) * 4 + 11848496)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC0);
    if (sign_flag) goto loc_00721C7D;
    result = IoGetRelatedTargetDevice(v_stack_mC0, v_stack_mB8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC0);
    v_rdi = v_stack_mB8;
    if (sign_flag) { v_rdi = 0; }
    v_stack_mB8 = v_rdi;
    v_stack_m90 = v_stack_mC0 + 80;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC0 + 80)))) & (2)) == 0) goto loc_007219CF;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mC0 + 80))) >> (2));
    v_rsi = (unsigned __int8)((v_rsi) & (1));
    a1 = (unsigned int)((v_stack_mC0) | (0xFFFFFFFFULL));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_mC0 + 128, a2, a3, v_stack_mC0);
    v_stack_mC8 = 0;
    if (1 != 0) goto loc_0072197D;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(v_stack_mC0, a2, a3, v_stack_mC0);
    v_rbx = 0;
    goto loc_007219A0;
loc_0072197D:
    v_stack_mE8 = v_stack_mC8;
    result = IopWaitAndAcquireFileObjectLock(v_stack_mC0, v_stack_mC7, (unsigned __int8)(v_rsi), result);
loc_007219A0:
    if (v_stack_mC8 == 0) goto loc_007219C5;
    result = ObfDereferenceObject(v_stack_mC0, v_stack_mC7, (unsigned __int8)(v_rsi), result);
    if (v_stack_mB8 != 0) {
        result = ObfDereferenceObject(v_stack_mB8, v_stack_mC7, (unsigned __int8)(v_rsi), result);
    }
    goto loc_00721C7D;
loc_007219C5:
    goto loc_00721A09;
loc_007219CF:
    result = ExAllocatePool2(24 + 40, 24, (unsigned int)(0x76456F49ULL), result);
    v_stack_mA8 = result;
    if (result != 0) goto loc_007219F9;
    result = ObfDereferenceObject(v_stack_mC0, 24, (unsigned int)(0x76456F49ULL), result);
    goto loc_00721A5F;
loc_007219F9:
    a3 = 0;
    result = KeInitializeEvent(result, 1, a3, result);
    v_rbx = 0;
loc_00721A09:
    v_stack_mC8 = 0;
    result = IopResetEvent(v_stack_mC0, 1, a3, result);
    result = IoGetRelatedDeviceObject(v_stack_mC0, 1, a3, result);
    v_stack_m88 = result;
    a3 = 0;
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, result);
    v_stack_m80 = result;
    a2 = 0;
    if (result != 0) goto loc_00721A76;
    result = (unsigned int)(*(unsigned int *)(v_stack_mC0 + 80));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC0 + 80)))) & (2)) == 0) {
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, result);
    }
    a2 = 0;
    result = IopAllocateIrpCleanup(v_stack_mC0, a2, a3, result);
loc_00721A5F:
    if (v_stack_mB8 != 0) {
        a1 = v_stack_mB8;
        result = ObfDereferenceObject(a1, a2, a3, result);
    }
    goto loc_00721C7D;
loc_00721A76:
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 192) = v_stack_mC0;
    *(unsigned __int64 *)(result + 152) = v_stack_mA0;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_mC7);
    v_stack_m78 = v_xmm0;
    if (0 == 0) goto loc_00721AA9;
    goto loc_00721ABB;
loc_00721AA9:
    *(unsigned int *)(result + 16) = 4;
loc_00721ABB:
    *(unsigned __int64 *)(result + 80) = result;
    *(unsigned __int64 *)(result + 72) = v_stack_m78;
    *(unsigned __int64 *)(result + 88) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72) = 11;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = v_stack_mC0;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    result = ExAllocatePool2(97, (unsigned int)((unsigned int)((unsigned int)(v_stack_mC4))), (unsigned int)(0x42536F49ULL), result);
    *(unsigned __int64 *)(result + 24) = result;
    result = memcpy(result, v_stack_m98, (unsigned int)((unsigned int)((unsigned int)(v_stack_mC4))), result);
    if ((unsigned __int8)(v_stack_mC7) == 0) goto loc_00721B69;
    if (a5 != 2) goto loc_00721B69;
    if (sign_flag) goto loc_00721B31;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24)))) + (4));
    if (((unsigned int)(result)) <= v_stack_mC4) goto loc_00721B69;
loc_00721B31:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m90))) >> (1));
    result = (unsigned __int8)((result) & (1));
    v_stack_mE8 = (unsigned __int8)(result);
    a3 = 0;
    result = IopExceptionCleanupEx(v_stack_mC0, result, a3, result);
    if (v_stack_mB8 != 0) {
        a1 = v_stack_mB8;
        result = ObfDereferenceObject(a1, result, a3, result);
    }
    goto loc_00721C7D;
loc_00721B69:
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(v_stack_mC4));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 56) = (unsigned int)((unsigned int)(a5));
    v_stack_mD8 = 2;
    v_stack_mE0 = (unsigned __int8)(v_stack_mC8);
    v_stack_mE8 = (unsigned __int8)(a1);
    a4 = 0;
    result = IopSynchronousServiceTail(v_stack_m88, result, v_stack_mC0, a4);
    v_r14 = 0;
    v_rbx = (unsigned int)((unsigned int)(result));
    if ((unsigned __int8)(v_stack_mC8) == 0) {
        result = v_stack_mB0;
        v_stack_mE0 = result;
        result = v_stack_m78;
        v_stack_mE8 = result;
        a4 = v_stack_mC7;
        a3 = result;
        a2 = result;
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = IopSynchronousApiServiceTail(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (v_stack_mB8 == 0) goto loc_007219BE;
    if (!(sign_flag)) {
        v_stack_m54 = 0;
        v_stack_m44 = 0;
        v_stack_m68 = 0x240001ULL;
        v_stack_m50 = 0;
        v_stack_m64 = v_xmm0;
        a2 = v_stack_m68;
        a1 = v_stack_mB8;
        result = IoReportTargetDeviceChange(a1, a2, a3, a4);
    }
    goto loc_007219B9;
loc_00721C7D:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (208);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetVolumeInformationFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint8_t v_stack_mC7;
    uint8_t v_stack_mC8;
    uint32_t v_stack_mD8;
    uint8_t v_stack_mE0;
    uint64_t v_stack_mE8;

    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x6E8FD6)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mC4 = Arg4;
    v_stack_m98 = Arg3;
    v_stack_mB0 = Arg2;
    local_r12 = 0;
    v_stack_mC0 = 0;
    v_stack_mA8 = 0;
    v_stack_mB8 = 0;
    v_stack_mA0 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_mC7 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_007218B1;
    if (((uint32_t)((int32_t)(Arg5))) >= 16) goto loc_007218A7;
    if ((uint8_t)(*(uint8_t *)((int32_t)(Arg5) + v_rip - 0x7217DD * 1 + 0xB4B138)) == 0) goto loc_007218A7;
    if (Arg4 >= ((uint32_t)(*(uint8_t *)((int32_t)(Arg5) + v_rip - 0x7217DD * 1 + 0xB4B138)))) goto loc_007217FD;
    goto loc_00721C7D;
loc_007217FD:
    Arg1 = local_r14;
    if (Arg2 < local_r14) { Arg1 = Arg2; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_0072186C;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 332) goto loc_0072184B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 452) goto loc_0072184B;
    goto loc_00721854;
loc_0072184B:
loc_00721854:
    v_stack_mC8 = 1;
    if (1 == 0) goto loc_00721872;
    if (Arg4 == 0) goto loc_007218A0;
    if ((((uint8_t)(Arg3)) & (3)) == 0) goto loc_0072188D;
    result = ExRaiseDatatypeMisalignment(452, (int32_t)(Arg5), Arg3, Arg4);
loc_0072186C:
loc_00721872:
    if (Arg4 == 0) goto loc_007218A0;
    result = (*(uint8_t *)((int32_t)(Arg5) + v_rip - 0x7217DD * 1 + 0xB4B620)) - (1);
    if (((Arg3) & (result)) != 0) {
        result = ExRaiseDatatypeMisalignment(452, (int32_t)(Arg5), Arg3, Arg4);
    }
    Arg1 = ((uint32_t)(Arg4)) + (Arg3);
    if (Arg1 > local_r14) goto loc_0072189D;
    if (Arg1 < Arg3) {
        result = *(uint8_t *)(local_r14);
    }
    goto loc_007218C6;
loc_007218A7:
    goto loc_00721C7D;
loc_007218B1:
loc_007218C6:
    v_stack_mE8 = 0;
    result = IopReferenceFileObject(Arg1, (uint32_t)(*(uint32_t *)(v_rip - 0x7218C0 + (int32_t)(Arg5) * 4 + 0xB4CB30)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC0);
    if (sign_flag) goto loc_00721C7D;
    result = IoGetRelatedTargetDevice(v_stack_mC0, v_stack_mB8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC0);
    local_rdi = v_stack_mB8;
    if (sign_flag) { local_rdi = 0; }
    v_stack_mB8 = local_rdi;
    v_stack_m90 = v_stack_mC0 + 80;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x50)))) & (2)) == 0) goto loc_007219CF;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x50))) >> (2));
    local_rsi = (uint8_t)((local_rsi) & (1));
    Arg1 = (uint32_t)((v_stack_mC0) | (0xFFFFFFFFULL));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_mC0 + 128, Arg2, Arg3, v_stack_mC0);
    v_stack_mC8 = 0;
    if (1 != 0) goto loc_0072197D;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(v_stack_mC0, Arg2, Arg3, v_stack_mC0);
    local_rbx = 0;
    goto loc_007219A0;
loc_0072197D:
    v_stack_mE8 = v_stack_mC8;
    result = IopWaitAndAcquireFileObjectLock(v_stack_mC0, v_stack_mC7, (uint8_t)(local_rsi), result);
loc_007219A0:
    if (v_stack_mC8 == 0) goto loc_007219C5;
    result = ObfDereferenceObject(v_stack_mC0, v_stack_mC7, (uint8_t)(local_rsi), result);
    if (v_stack_mB8 != 0) {
        result = ObfDereferenceObject(v_stack_mB8, v_stack_mC7, (uint8_t)(local_rsi), result);
    }
    goto loc_00721C7D;
loc_007219C5:
    goto loc_00721A09;
loc_007219CF:
    result = ExAllocatePool2(24 + 40, 24, (uint32_t)(0x76456F49ULL), result);
    v_stack_mA8 = result;
    if (result != 0) goto loc_007219F9;
    result = ObfDereferenceObject(v_stack_mC0, 24, (uint32_t)(0x76456F49ULL), result);
    goto loc_00721A5F;
loc_007219F9:
    Arg3 = 0;
    result = KeInitializeEvent(result, 1, Arg3, result);
    local_rbx = 0;
loc_00721A09:
    v_stack_mC8 = 0;
    result = IopResetEvent(v_stack_mC0, 1, Arg3, result);
    result = IoGetRelatedDeviceObject(v_stack_mC0, 1, Arg3, result);
    v_stack_m88 = result;
    Arg3 = 0;
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, result);
    v_stack_m80 = result;
    Arg2 = 0;
    if (result != 0) goto loc_00721A76;
    result = (uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x50));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x50)))) & (2)) == 0) {
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, result);
    }
    Arg2 = 0;
    result = IopAllocateIrpCleanup(v_stack_mC0, Arg2, Arg3, result);
loc_00721A5F:
    if (v_stack_mB8 != 0) {
        Arg1 = v_stack_mB8;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, result);
    }
    goto loc_00721C7D;
loc_00721A76:
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0xC0) = v_stack_mC0;
    *(uint64_t *)(result + 0x98) = v_stack_mA0;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_mC7);
    v_stack_m78 = v_xmm0;
    if (0 == 0) goto loc_00721AA9;
    goto loc_00721ABB;
loc_00721AA9:
    *(uint32_t *)(result + 0x10) = 4;
loc_00721ABB:
    *(uint64_t *)(result + 0x50) = result;
    *(uint64_t *)(result + 0x48) = v_stack_m78;
    *(uint64_t *)(result + 0x58) = 0;
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 11;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x18) = v_stack_mC0;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    result = ExAllocatePool2(97, (uint32_t)((uint32_t)((uint32_t)(v_stack_mC4))), (uint32_t)(0x42536F49ULL), result);
    *(uint64_t *)(result + 0x18) = result;
    result = memcpy(result, v_stack_m98, (uint32_t)((uint32_t)((uint32_t)(v_stack_mC4))), result);
    if ((uint8_t)(v_stack_mC7) == 0) goto loc_00721B69;
    if (Arg5 != 2) goto loc_00721B69;
    if (sign_flag) goto loc_00721B31;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18)))) + (4));
    if (((uint32_t)(result)) <= v_stack_mC4) goto loc_00721B69;
loc_00721B31:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m90))) >> (1));
    result = (uint8_t)((result) & (1));
    v_stack_mE8 = (uint8_t)(result);
    Arg3 = 0;
    result = IopExceptionCleanupEx(v_stack_mC0, result, Arg3, result);
    if (v_stack_mB8 != 0) {
        Arg1 = v_stack_mB8;
        result = ObfDereferenceObject(Arg1, result, Arg3, result);
    }
    goto loc_00721C7D;
loc_00721B69:
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(v_stack_mC4));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = (uint32_t)((uint32_t)(Arg5));
    v_stack_mD8 = 2;
    v_stack_mE0 = (uint8_t)(v_stack_mC8);
    v_stack_mE8 = (uint8_t)(Arg1);
    Arg4 = 0;
    result = IopSynchronousServiceTail(v_stack_m88, result, v_stack_mC0, Arg4);
    local_r14 = 0;
    local_rbx = (uint32_t)((uint32_t)(result));
    if ((uint8_t)(v_stack_mC8) == 0) {
        result = v_stack_mB0;
        v_stack_mE0 = result;
        result = v_stack_m78;
        v_stack_mE8 = result;
        Arg4 = v_stack_mC7;
        Arg3 = result;
        Arg2 = result;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = IopSynchronousApiServiceTail(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (v_stack_mB8 == 0) goto loc_007219BE;
    if (!(sign_flag)) {
        v_stack_m54 = 0;
        v_stack_m44 = 0;
        v_stack_m68 = 0x240001ULL;
        v_stack_m50 = 0;
        v_stack_m64 = v_xmm0;
        Arg2 = v_stack_m68;
        Arg1 = v_stack_mB8;
        result = IoReportTargetDeviceChange(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_007219B9;
loc_00721C7D:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (208);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00721750&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
