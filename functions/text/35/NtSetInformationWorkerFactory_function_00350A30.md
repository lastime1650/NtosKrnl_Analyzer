# NtSetInformationWorkerFactory

- RVA: `0x00350A30`–`0x0035140C` (길이 `2,524` bytes)
- VA: `0x0000000140350A30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00078DB8`
- 디코드: `601`개 명령, `2,524/2,524` bytes 표시
- 미해석 바이트: `3` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **21**

### Outgoing calls
- `0x00350A92` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00350B6B` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00350BA0` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00350BCA` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00350C01` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00350C3E` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00350D25` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00350D32` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00350D45` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00350D74` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00350DB9` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00350DFB` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00350E7F` → [ExpLeaveWorkerFactoryAwayMode](../34/ExpLeaveWorkerFactoryAwayMode_function_00344350.md) (function, `0x00344350`)
- `0x00350F29` → [ExpLeaveWorkerFactoryAwayMode](../34/ExpLeaveWorkerFactoryAwayMode_function_00344350.md) (function, `0x00344350`)
- `0x00350F39` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00350F43` → [ExpWorkerFactoryCreateThread](../34/ExpWorkerFactoryCreateThread_function_0034B620.md) (function, `0x0034B620`)
- `0x00350F5E` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x00350FB2` → [ExpTryEnterWorkerFactoryAwayMode](../39/ExpTryEnterWorkerFactoryAwayMode_function_003930B0.md) (function, `0x003930B0`)
- `0x00350FCA` → [ExpWorkerFactoryCheckCreate](../34/ExpWorkerFactoryCheckCreate_function_00344460.md) (function, `0x00344460`)
- `0x0035106B` → [KeTimeOutQueueWaiters](../34/KeTimeOutQueueWaiters_function_0034FB58.md) (function, `0x0034FB58`)
- `0x00351078` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00351105` → [KeSetTimer2](../3A/KeSetTimer2_function_003A08E0.md) (function, `0x003A08E0`)
- `0x00351177` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0035117F` → [ExpWorkerFactoryCreateThread](../34/ExpWorkerFactoryCreateThread_function_0034B620.md) (function, `0x0034B620`)
- `0x00351190` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003512AB` → [ExpLeaveWorkerFactoryAwayMode](../34/ExpLeaveWorkerFactoryAwayMode_function_00344350.md) (function, `0x00344350`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00350A43` → RVA `0x00E0A740` (`.data`; read)
- `0x00350AA0` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00350C15` → RVA `0x00FC51E0` (`ALMOSTRO`; read)
- `0x00350C7B` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00350C8D` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00350D5E` → RVA `0x00F0DE58` (`.data`; read)
- `0x0035127F` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x0035135D` → RVA `0x35402E63` (`image boundary/outside`; read)
- `0x00351365` → RVA `0x35402E6B` (`image boundary/outside`; read)
- `0x00351375` → RVA `0x0035137B` (`.text`; read)
- `0x0035137D` → RVA `0x35402E83` (`image boundary/outside`; read)
- `0x00351383` → RVA `0x1B354894` (`image boundary/outside`; read/write)
- `0x00351389` → RVA `0x35402E8F` (`image boundary/outside`; read)
- `0x00351395` → RVA `0x3543429B` (`image boundary/outside`; read/write)
- `0x003513B5` → RVA `0x3546C3BB` (`image boundary/outside`; read/write)
- `0x003513BD` → RVA `0x003513C3` (`.text`; read/write)
- `0x003513C9` → RVA `0x35476FCF` (`image boundary/outside`; read)
- `0x003513D5` → RVA `0x353FBADB` (`image boundary/outside`; read/write)
- `0x003513E1` → RVA `0x354338E7` (`image boundary/outside`; read)
- `0x003513F1` → RVA `0x3546B8F7` (`image boundary/outside`; read)
- `0x00351401` → RVA `0x353FBB07` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00350B6B` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x00350BA0` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x00350C01` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x00350C3E` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00351247` → [sub_006E25FA](../6E/Unknown_function_006E25FA.md) (`tail-transfer`)
  - `0x00351279` → [sub_006E25FA + 0xB](../6E/Unknown_function_006E25FA.md) (`tail-transfer`)
  - `0x0035128A` → [sub_006E25FA + 0xB](../6E/Unknown_function_006E25FA.md) (`tail-transfer`)
  - `0x003512FF` → [sub_006E25FA + 0x1F](../6E/Unknown_function_006E25FA.md) (`tail-transfer`)
  - `0x00351329` → [sub_006E25FA + 0x6E](../6E/Unknown_function_006E25FA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00350A30  40 53                           push rbx
00350A32  56                              push rsi
00350A33  57                              push rdi
00350A34  41 54                           push r12
00350A36  41 55                           push r13
00350A38  41 56                           push r14
00350A3A  41 57                           push r15
00350A3C  48 81 EC 80 01 00 00            sub rsp, 0x180
00350A43  48 8B 05 F6 9C AB 00            mov rax, qword ptr [rip + 0xab9cf6]
00350A4A  48 33 C4                        xor rax, rsp
00350A4D  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
00350A55  45 8B F1                        mov r14d, r9d
00350A58  49 8B F0                        mov rsi, r8
00350A5B  48 63 DA                        movsxd rbx, edx
00350A5E  4C 8B E1                        mov r12, rcx
00350A61  0F 57 C0                        xorps xmm0, xmm0
00350A64  33 C0                           xor eax, eax
00350A66  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00350A6B  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00350A70  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00350A75  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00350A7E  0F B6 B8 32 02 00 00            movzx edi, byte ptr [rax + 0x232]
00350A85  33 D2                           xor edx, edx
00350A87  41 B8 00 01 00 00               mov r8d, 0x100
00350A8D  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00350A92  E8 A9 61 37 00                  call 0x1406c6c40
00350A97  83 FB 0B                        cmp ebx, 0xb
00350A9A  0F 85 65 03 00 00               jne 0x140350e05
00350AA0  48 8D 15 59 F5 CA FF            lea rdx, [rip - 0x350aa7]
00350AA7  41 B8 04 00 00 00               mov r8d, 4
00350AAD  44 89 44 24 3C                  mov dword ptr [rsp + 0x3c], r8d
00350AB2  45 3B F0                        cmp r14d, r8d
00350AB5  0F 85 31 03 00 00               jne 0x140350dec
00350ABB  83 FB 09                        cmp ebx, 9
00350ABE  75 3A                           jne 0x140350afa
00350AC0  40 84 FF                        test dil, dil
00350AC3  74 2A                           je 0x140350aef
00350AC5  40 F6 C6 03                     test sil, 3
00350AC9  0F 85 32 01 00 00               jne 0x140350c01
00350ACF  48 8D 46 04                     lea rax, [rsi + 4]
00350AD3  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00350ADD  48 3B C1                        cmp rax, rcx
00350AE0  0F 87 20 01 00 00               ja 0x140350c06
00350AE6  48 3B C6                        cmp rax, rsi
00350AE9  0F 82 17 01 00 00               jb 0x140350c06
00350AEF  8B 06                           mov eax, dword ptr [rsi]
00350AF1  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00350AF5  E9 14 01 00 00                  jmp 0x140350c0e
00350AFA  8D 43 FE                        lea eax, [rbx - 2]
00350AFD  83 F8 0D                        cmp eax, 0xd
00350B00  77 12                           ja 0x140350b14
00350B02  48 98                           cdqe
00350B04  8B 8C 82 5C 13 35 00            mov ecx, dword ptr [rdx + rax*4 + 0x35135c]
00350B0B  48 03 CA                        add rcx, rdx
00350B0E  FF E1                           jmp rcx
00350B10  CC                              int3
00350B11  CC                              int3
00350B12  CC                              int3
00350B13  CC                              int3
00350B14  B9 25 00 00 00                  mov ecx, 0x25
00350B19  CD 29                           int 0x29
00350B1B  40 84 FF                        test dil, dil
00350B1E  74 CF                           je 0x140350aef
00350B20  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00350B2A  48 3B F1                        cmp rsi, rcx
00350B2D  48 0F 42 CE                     cmovb rcx, rsi
00350B31  90                              nop
00350B32  8B 01                           mov eax, dword ptr [rcx]
00350B34  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00350B38  E9 D1 00 00 00                  jmp 0x140350c0e
00350B3D  40 84 FF                        test dil, dil
00350B40  0F 84 C8 00 00 00               je 0x140350c0e
00350B46  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00350B50  48 3B F1                        cmp rsi, rcx
00350B53  48 0F 42 CE                     cmovb rcx, rsi
00350B57  8B 01                           mov eax, dword ptr [rcx]
00350B59  89 01                           mov dword ptr [rcx], eax
00350B5B  E9 AE 00 00 00                  jmp 0x140350c0e
00350B60  40 84 FF                        test dil, dil
00350B63  74 21                           je 0x140350b86
00350B65  40 F6 C6 03                     test sil, 3
00350B69  74 06                           je 0x140350b71
00350B6B  E8 60 94 54 00                  call 0x140899fd0
00350B70  CC                              int3
00350B71  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00350B7B  48 3B F1                        cmp rsi, rcx
00350B7E  48 0F 42 CE                     cmovb rcx, rsi
00350B82  90                              nop
00350B83  0F B6 01                        movzx eax, byte ptr [rcx]
00350B86  48 8B 06                        mov rax, qword ptr [rsi]
00350B89  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00350B8E  EB 7E                           jmp 0x140350c0e
00350B90  40 84 FF                        test dil, dil
00350B93  74 2D                           je 0x140350bc2
00350B95  45 85 C0                        test r8d, r8d
00350B98  74 28                           je 0x140350bc2
00350B9A  40 F6 C6 03                     test sil, 3
00350B9E  74 05                           je 0x140350ba5
00350BA0  E8 2B 94 54 00                  call 0x140899fd0
00350BA5  41 8B D0                        mov edx, r8d
00350BA8  48 03 D6                        add rdx, rsi
00350BAB  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00350BB5  48 3B D1                        cmp rdx, rcx
00350BB8  77 05                           ja 0x140350bbf
00350BBA  48 3B D6                        cmp rdx, rsi
00350BBD  73 03                           jae 0x140350bc2
00350BBF  0F B6 01                        movzx eax, byte ptr [rcx]
00350BC2  48 8B D6                        mov rdx, rsi
00350BC5  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00350BCA  E8 71 5C 37 00                  call 0x1406c6840
00350BCF  EB 3D                           jmp 0x140350c0e
00350BD1  40 84 FF                        test dil, dil
00350BD4  74 1B                           je 0x140350bf1
00350BD6  40 F6 C6 03                     test sil, 3
00350BDA  75 8F                           jne 0x140350b6b
00350BDC  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00350BE6  48 3B F1                        cmp rsi, rcx
00350BE9  48 0F 42 CE                     cmovb rcx, rsi
00350BED  90                              nop
00350BEE  0F B6 01                        movzx eax, byte ptr [rcx]
00350BF1  0F 10 06                        movups xmm0, xmmword ptr [rsi]
00350BF4  0F 29 44 24 70                  movaps xmmword ptr [rsp + 0x70], xmm0
00350BF9  66 0F 7E 44 24 70               movd dword ptr [rsp + 0x70], xmm0
00350BFF  EB 0D                           jmp 0x140350c0e
00350C01  E8 CA 93 54 00                  call 0x140899fd0
00350C06  0F B6 01                        movzx eax, byte ptr [rcx]
00350C09  E9 E1 FE FF FF                  jmp 0x140350aef
00350C0E  EB 05                           jmp 0x140350c15
00350C10  E9 25 01 00 00                  jmp 0x140350d3a
00350C15  4C 8B 05 C4 45 C7 00            mov r8, qword ptr [rip + 0xc745c4]
00350C1C  45 33 FF                        xor r15d, r15d
00350C1F  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00350C24  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00350C29  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00350C2E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00350C33  44 0F B6 CF                     movzx r9d, dil
00350C37  41 8D 57 04                     lea edx, [r15 + 4]
00350C3B  49 8B CC                        mov rcx, r12
00350C3E  E8 6D 81 51 00                  call 0x140868db0
00350C43  85 C0                           test eax, eax
00350C45  0F 88 EF 00 00 00               js 0x140350d3a
00350C4B  83 FB 08                        cmp ebx, 8
00350C4E  0F 84 12 06 00 00               je 0x140351266
00350C54  45 8B F7                        mov r14d, r15d
00350C57  45 32 E4                        xor r12b, r12b
00350C5A  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00350C5F  48 8B 78 10                     mov rdi, qword ptr [rax + 0x10]
00350C63  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00350C68  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00350C6D  90                              nop
00350C6E  45 0F 20 C5                     mov r13, cr8
00350C72  B8 02 00 00 00                  mov eax, 2
00350C77  44 0F 22 C0                     mov cr8, rax
00350C7B  44 39 3D 9E 60 C7 00            cmp dword ptr [rip + 0xc7609e], r15d
00350C82  0F 85 2A 01 00 00               jne 0x140350db2
00350C88  44 88 6C 24 50                  mov byte ptr [rsp + 0x50], r13b
00350C8D  F6 05 72 5E C7 00 21            test byte ptr [rip + 0xc75e72], 0x21
00350C94  0F 85 C4 00 00 00               jne 0x140350d5e
00350C9A  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00350C9F  48 87 17                        xchg qword ptr [rdi], rdx
00350CA2  48 85 D2                        test rdx, rdx
00350CA5  0F 85 4B 01 00 00               jne 0x140350df6
00350CAB  83 FB 09                        cmp ebx, 9
00350CAE  75 34                           jne 0x140350ce4
00350CB0  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
00350CB4  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00350CB9  83 F9 02                        cmp ecx, 2
00350CBC  0F 85 BC 00 00 00               jne 0x140350d7e
00350CC2  8B 87 80 01 00 00               mov eax, dword ptr [rdi + 0x180]
00350CC8  85 C0                           test eax, eax
00350CCA  0F 84 D7 00 00 00               je 0x140350da7
00350CD0  83 E8 01                        sub eax, 1
00350CD3  89 87 80 01 00 00               mov dword ptr [rdi + 0x180], eax
00350CD9  75 33                           jne 0x140350d0e
00350CDB  41 B4 01                        mov r12b, 1
00350CDE  41 0F B6 DC                     movzx ebx, r12b
00350CE2  EB 2C                           jmp 0x140350d10
00350CE4  83 FB 0D                        cmp ebx, 0xd
00350CE7  0F 85 D6 00 00 00               jne 0x140350dc3
00350CED  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00350CF2  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
00350CF6  83 E1 01                        and ecx, 1
00350CF9  C1 E1 0B                        shl ecx, 0xb
00350CFC  8B 87 98 01 00 00               mov eax, dword ptr [rdi + 0x198]
00350D02  0F BA F0 0B                     btr eax, 0xb
00350D06  0B C8                           or ecx, eax
00350D08  89 8F 98 01 00 00               mov dword ptr [rdi + 0x198], ecx
00350D0E  B3 01                           mov bl, 1
00350D10  40 32 F6                        xor sil, sil
00350D13  45 84 E4                        test r12b, r12b
00350D16  0F 85 6D 01 00 00               jne 0x140350e89
00350D1C  84 DB                           test bl, bl
00350D1E  74 0A                           je 0x140350d2a
00350D20  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00350D25  E8 B6 1F FF FF                  call 0x140342ce0
00350D2A  BA 44 66 6C 74                  mov edx, 0x746c6644
00350D2F  48 8B CF                        mov rcx, rdi
00350D32  E8 A9 6B FA FF                  call 0x1402f78e0
00350D37  41 8B C6                        mov eax, r14d
00350D3A  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
00350D42  48 33 CC                        xor rcx, rsp
00350D45  E8 F6 B8 35 00                  call 0x1406ac640
00350D4A  48 81 C4 80 01 00 00            add rsp, 0x180
00350D51  41 5F                           pop r15
00350D53  41 5E                           pop r14
00350D55  41 5D                           pop r13
00350D57  41 5C                           pop r12
00350D59  5F                              pop rdi
00350D5A  5E                              pop rsi
00350D5B  5B                              pop rbx
00350D5C  C3                              ret
00350D5D  CC                              int3
00350D5E  8B 05 F4 D0 BB 00               mov eax, dword ptr [rip + 0xbbd0f4]
00350D64  85 C0                           test eax, eax
00350D66  0F 85 2E FF FF FF               jne 0x140350c9a
00350D6C  48 8B D7                        mov rdx, rdi
00350D6F  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00350D74  E8 D7 4A F2 FF                  call 0x140275850
00350D79  E9 2D FF FF FF                  jmp 0x140350cab
00350D7E  85 C9                           test ecx, ecx
00350D80  0F 85 8A 05 00 00               jne 0x140351310
00350D86  8B 87 80 01 00 00               mov eax, dword ptr [rdi + 0x180]
00350D8C  B3 01                           mov bl, 1
00350D8E  3B 87 84 01 00 00               cmp eax, dword ptr [rdi + 0x184]
00350D94  0F 84 A0 05 00 00               je 0x14035133a
00350D9A  FF C0                           inc eax
00350D9C  89 87 80 01 00 00               mov dword ptr [rdi + 0x180], eax
00350DA2  E9 69 FF FF FF                  jmp 0x140350d10
00350DA7  41 BE 01 00 00 C0               mov r14d, 0xc0000001
00350DAD  E9 5C FF FF FF                  jmp 0x140350d0e
00350DB2  0F B6 D0                        movzx edx, al
00350DB5  41 0F B6 CD                     movzx ecx, r13b
00350DB9  E8 3E 49 1A 00                  call 0x1404f56fc
00350DBE  E9 C5 FE FF FF                  jmp 0x140350c88
00350DC3  83 C3 FE                        add ebx, -2
00350DC6  83 FB 0D                        cmp ebx, 0xd
00350DC9  77 1A                           ja 0x140350de5
00350DCB  48 63 C3                        movsxd rax, ebx
00350DCE  48 8D 15 2B F2 CA FF            lea rdx, [rip - 0x350dd5]
00350DD5  8B 8C 82 94 13 35 00            mov ecx, dword ptr [rdx + rax*4 + 0x351394]
00350DDC  48 03 CA                        add rcx, rdx
00350DDF  FF E1                           jmp rcx
00350DE1  CC                              int3
00350DE2  CC                              int3
00350DE3  CC                              int3
00350DE4  CC                              int3
00350DE5  B9 25 00 00 00                  mov ecx, 0x25
00350DEA  CD 29                           int 0x29
00350DEC  B8 04 00 00 C0                  mov eax, 0xc0000004
00350DF1  E9 44 FF FF FF                  jmp 0x140350d3a
00350DF6  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00350DFB  E8 B0 70 F0 FF                  call 0x140257eb0
00350E00  E9 A6 FE FF FF                  jmp 0x140350cab
00350E05  83 FB 0F                        cmp ebx, 0xf
00350E08  0F 87 4E 04 00 00               ja 0x14035125c
00350E0E  48 8D 15 EB F1 CA FF            lea rdx, [rip - 0x350e15]
00350E15  8B 84 9A CC 13 35 00            mov eax, dword ptr [rdx + rbx*4 + 0x3513cc]
00350E1C  48 03 C2                        add rax, rdx
00350E1F  FF E0                           jmp rax
00350E21  CC                              int3
00350E22  CC                              int3
00350E23  CC                              int3
00350E24  CC                              int3
00350E25  B8 02 00 00 C0                  mov eax, 0xc0000002
00350E2A  E9 0B FF FF FF                  jmp 0x140350d3a
00350E2F  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00350E34  8B 8F 94 01 00 00               mov ecx, dword ptr [rdi + 0x194]
00350E3A  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
00350E3E  85 D2                           test edx, edx
00350E40  0F 89 4F 01 00 00               jns 0x140350f95
00350E46  8B C2                           mov eax, edx
00350E48  F7 D8                           neg eax
00350E4A  3B C8                           cmp ecx, eax
00350E4C  0F 87 3D 04 00 00               ja 0x14035128f
00350E52  44 89 BF 94 01 00 00            mov dword ptr [rdi + 0x194], r15d
00350E59  41 8B C7                        mov eax, r15d
00350E5C  85 C9                           test ecx, ecx
00350E5E  0F 84 47 01 00 00               je 0x140350fab
00350E64  85 C0                           test eax, eax
00350E66  0F 85 A2 FE FF FF               jne 0x140350d0e
00350E6C  F7 87 98 01 00 00 00 02 00 00   test dword ptr [rdi + 0x198], 0x200
00350E76  0F 84 92 FE FF FF               je 0x140350d0e
00350E7C  48 8B CF                        mov rcx, rdi
00350E7F  E8 CC 34 FF FF                  call 0x140344350
00350E84  E9 85 FE FF FF                  jmp 0x140350d0e
00350E89  8B 8F 80 01 00 00               mov ecx, dword ptr [rdi + 0x180]
00350E8F  8B 97 88 01 00 00               mov edx, dword ptr [rdi + 0x188]
00350E95  03 D1                           add edx, ecx
00350E97  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00350E9B  80 78 21 00                     cmp byte ptr [rax + 0x21], 0
00350E9F  0F 85 79 03 00 00               jne 0x14035121e
00350EA5  8B 87 7C 01 00 00               mov eax, dword ptr [rdi + 0x17c]
00350EAB  3B C8                           cmp ecx, eax
00350EAD  0F 83 92 04 00 00               jae 0x140351345
00350EB3  83 BF 90 01 00 00 00            cmp dword ptr [rdi + 0x190], 0
00350EBA  76 5A                           jbe 0x140350f16
00350EBC  45 8B F7                        mov r14d, r15d
00350EBF  E9 58 FE FF FF                  jmp 0x140350d1c
00350EC4  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00350EC9  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00350ECD  44 38 60 21                     cmp byte ptr [rax + 0x21], r12b
00350ED1  0F 85 B3 00 00 00               jne 0x140350f8a
00350ED7  40 B6 01                        mov sil, 1
00350EDA  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
00350EDE  85 C9                           test ecx, ecx
00350EE0  74 1B                           je 0x140350efd
00350EE2  44 39 BF 7C 01 00 00            cmp dword ptr [rdi + 0x17c], r15d
00350EE9  0F 84 C6 03 00 00               je 0x1403512b5
00350EEF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00350EF3  44 39 78 04                     cmp dword ptr [rax + 4], r15d
00350EF7  0F 8F C2 03 00 00               jg 0x1403512bf
00350EFD  89 8F 7C 01 00 00               mov dword ptr [rdi + 0x17c], ecx
00350F03  3B 8F 78 01 00 00               cmp ecx, dword ptr [rdi + 0x178]
00350F09  0F 82 B9 03 00 00               jb 0x1403512c8
00350F0F  B3 01                           mov bl, 1
00350F11  E9 FD FD FF FF                  jmp 0x140350d13
00350F16  3B D0                           cmp edx, eax
00350F18  73 A2                           jae 0x140350ebc
00350F1A  F7 87 98 01 00 00 00 02 00 00   test dword ptr [rdi + 0x198], 0x200
00350F24  74 08                           je 0x140350f2e
00350F26  48 8B CF                        mov rcx, rdi
00350F29  E8 22 34 FF FF                  call 0x140344350
00350F2E  FF 87 90 01 00 00               inc dword ptr [rdi + 0x190]
00350F34  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00350F39  E8 A2 1D FF FF                  call 0x140342ce0
00350F3E  32 DB                           xor bl, bl
00350F40  48 8B CF                        mov rcx, rdi
00350F43  E8 D8 A6 FF FF                  call 0x14034b620
00350F48  44 8B F0                        mov r14d, eax
00350F4B  85 C0                           test eax, eax
00350F4D  0F 89 C9 FD FF FF               jns 0x140350d1c
00350F53  B3 01                           mov bl, 1
00350F55  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00350F5A  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00350F5E  E8 3D 48 F2 FF                  call 0x1402757a0
00350F63  FF 8F 90 01 00 00               dec dword ptr [rdi + 0x190]
00350F69  40 84 F6                        test sil, sil
00350F6C  0F 84 AA FD FF FF               je 0x140350d1c
00350F72  E9 45 FF FF FF                  jmp 0x140350ebc
00350F77  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00350F7C  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00350F80  44 38 60 21                     cmp byte ptr [rax + 0x21], r12b
00350F84  0F 84 85 01 00 00               je 0x14035110f
00350F8A  41 BE 80 00 00 00               mov r14d, 0x80
00350F90  E9 79 FD FF FF                  jmp 0x140350d0e
00350F95  8D 04 11                        lea eax, [rcx + rdx]
00350F98  3B C8                           cmp ecx, eax
00350F9A  0F 83 38 02 00 00               jae 0x1403511d8
00350FA0  89 87 94 01 00 00               mov dword ptr [rdi + 0x194], eax
00350FA6  E9 B1 FE FF FF                  jmp 0x140350e5c
00350FAB  85 C0                           test eax, eax
00350FAD  74 27                           je 0x140350fd6
00350FAF  48 8B CF                        mov rcx, rdi
00350FB2  E8 F9 20 04 00                  call 0x1403930b0
00350FB7  84 C0                           test al, al
00350FB9  0F 84 4F FD FF FF               je 0x140350d0e
00350FBF  45 33 C0                        xor r8d, r8d
00350FC2  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00350FC7  48 8B CF                        mov rcx, rdi
00350FCA  E8 91 34 FF FF                  call 0x140344460
00350FCF  32 DB                           xor bl, bl
00350FD1  E9 3A FD FF FF                  jmp 0x140350d10
00350FD6  85 C9                           test ecx, ecx
00350FD8  0F 84 30 FD FF FF               je 0x140350d0e
00350FDE  E9 81 FE FF FF                  jmp 0x140350e64
00350FE3  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00350FE8  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00350FEC  44 38 60 21                     cmp byte ptr [rax + 0x21], r12b
00350FF0  75 98                           jne 0x140350f8a
00350FF2  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00350FF6  89 87 8C 01 00 00               mov dword ptr [rdi + 0x18c], eax
00350FFC  85 C0                           test eax, eax
00350FFE  0F 84 0A FD FF FF               je 0x140350d0e
00351004  8B 8F 78 01 00 00               mov ecx, dword ptr [rdi + 0x178]
0035100A  3B C1                           cmp eax, ecx
0035100C  0F 82 C5 02 00 00               jb 0x1403512d7
00351012  8B 8F 7C 01 00 00               mov ecx, dword ptr [rdi + 0x17c]
00351018  40 32 F6                        xor sil, sil
0035101B  3B C1                           cmp eax, ecx
0035101D  0F 86 EC FE FF FF               jbe 0x140350f0f
00351023  89 8F 8C 01 00 00               mov dword ptr [rdi + 0x18c], ecx
00351029  B3 01                           mov bl, 1
0035102B  E9 E3 FC FF FF                  jmp 0x140350d13
00351030  41 B8 08 00 00 00               mov r8d, 8
00351036  E9 72 FA FF FF                  jmp 0x140350aad
0035103B  45 8B EF                        mov r13d, r15d
0035103E  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00351043  44 39 BF 90 01 00 00            cmp dword ptr [rdi + 0x190], r15d
0035104A  75 27                           jne 0x140351073
0035104C  44 8B 87 80 01 00 00            mov r8d, dword ptr [rdi + 0x180]
00351053  8B 87 78 01 00 00               mov eax, dword ptr [rdi + 0x178]
00351059  44 3B C0                        cmp r8d, eax
0035105C  76 15                           jbe 0x140351073
0035105E  44 2B C0                        sub r8d, eax
00351061  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00351065  33 D2                           xor edx, edx
00351067  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0035106B  E8 E8 EA FF FF                  call 0x14034fb58
00351070  44 8B E8                        mov r13d, eax
00351073  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00351078  E8 63 1C FF FF                  call 0x140342ce0
0035107D  32 DB                           xor bl, bl
0035107F  44 89 2E                        mov dword ptr [rsi], r13d
00351082  40 32 F6                        xor sil, sil
00351085  E9 89 FC FF FF                  jmp 0x140350d13
0035108A  45 33 FF                        xor r15d, r15d
0035108D  41 0F B6 F7                     movzx esi, r15b
00351091  41 0F B6 DF                     movzx ebx, r15b
00351095  45 8B F7                        mov r14d, r15d
00351098  45 0F B6 E7                     movzx r12d, r15b
0035109C  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
003510A1  E9 6D FC FF FF                  jmp 0x140350d13
003510A6  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
003510AB  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003510AF  44 38 60 21                     cmp byte ptr [rax + 0x21], r12b
003510B3  0F 85 D1 FE FF FF               jne 0x140350f8a
003510B9  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
003510BE  48 85 D2                        test rdx, rdx
003510C1  0F 89 25 01 00 00               jns 0x1403511ec
003510C7  48 C7 C0 80 69 67 FF            mov rax, 0xffffffffff676980
003510CE  48 3B D0                        cmp rdx, rax
003510D1  48 0F 4F D0                     cmovg rdx, rax
003510D5  48 B8 00 44 5F 9A FE FF FF FF   movabs rax, 0xfffffffe9a5f4400
003510DF  48 3B D0                        cmp rdx, rax
003510E2  48 0F 4C D0                     cmovl rdx, rax
003510E6  48 89 57 70                     mov qword ptr [rdi + 0x70], rdx
003510EA  48 C7 44 24 68 FF FF FF FF      mov qword ptr [rsp + 0x68], 0xffffffffffffffff
003510F3  4C 8B C2                        mov r8, rdx
003510F6  49 F7 D8                        neg r8
003510F9  48 8D 8F A8 01 00 00            lea rcx, [rdi + 0x1a8]
00351100  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00351105  E8 D6 F7 04 00                  call 0x1403a08e0
0035110A  E9 FF FB FF FF                  jmp 0x140350d0e
0035110F  45 0F B6 E4                     movzx r12d, r12b
00351113  BA 01 00 00 00                  mov edx, 1
00351118  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
0035111C  3B 87 78 01 00 00               cmp eax, dword ptr [rdi + 0x178]
00351122  44 0F 47 E2                     cmova r12d, edx
00351126  89 87 78 01 00 00               mov dword ptr [rdi + 0x178], eax
0035112C  39 87 7C 01 00 00               cmp dword ptr [rdi + 0x17c], eax
00351132  0F 82 65 01 00 00               jb 0x14035129d
00351138  45 84 E4                        test r12b, r12b
0035113B  0F 84 B6 00 00 00               je 0x1403511f7
00351141  45 32 E4                        xor r12b, r12b
00351144  F7 87 98 01 00 00 00 02 00 00   test dword ptr [rdi + 0x198], 0x200
0035114E  0F 85 54 01 00 00               jne 0x1403512a8
00351154  8B 87 88 01 00 00               mov eax, dword ptr [rdi + 0x188]
0035115A  03 87 80 01 00 00               add eax, dword ptr [rdi + 0x180]
00351160  3B 87 78 01 00 00               cmp eax, dword ptr [rdi + 0x178]
00351166  0F 83 A2 FB FF FF               jae 0x140350d0e
0035116C  FF 87 90 01 00 00               inc dword ptr [rdi + 0x190]
00351172  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00351177  E8 64 1B FF FF                  call 0x140342ce0
0035117C  48 8B CF                        mov rcx, rdi
0035117F  E8 9C A4 FF FF                  call 0x14034b620
00351184  44 8B F0                        mov r14d, eax
00351187  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0035118C  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00351190  E8 0B 46 F2 FF                  call 0x1402757a0
00351195  45 85 F6                        test r14d, r14d
00351198  79 BA                           jns 0x140351154
0035119A  FF 8F 90 01 00 00               dec dword ptr [rdi + 0x190]
003511A0  E9 69 FB FF FF                  jmp 0x140350d0e
003511A5  41 B8 10 00 00 00               mov r8d, 0x10
003511AB  E9 FD F8 FF FF                  jmp 0x140350aad
003511B0  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
003511B5  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003511B9  0F B6 48 21                     movzx ecx, byte ptr [rax + 0x21]
003511BD  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
003511C1  89 87 9C 01 00 00               mov dword ptr [rdi + 0x19c], eax
003511C7  F6 D9                           neg cl
003511C9  45 1B F6                        sbb r14d, r14d
003511CC  41 81 E6 80 00 00 00            and r14d, 0x80
003511D3  E9 36 FB FF FF                  jmp 0x140350d0e
003511D8  C7 87 94 01 00 00 FF FF FF FF   mov dword ptr [rdi + 0x194], 0xffffffff
003511E2  B8 FF FF FF FF                  mov eax, 0xffffffff
003511E7  E9 70 FC FF FF                  jmp 0x140350e5c
003511EC  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
003511F2  E9 17 FB FF FF                  jmp 0x140350d0e
003511F7  40 32 F6                        xor sil, sil
003511FA  E9 10 FD FF FF                  jmp 0x140350f0f
003511FF  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00351204  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00351208  B3 01                           mov bl, 1
0035120A  40 32 F6                        xor sil, sil
0035120D  44 38 60 21                     cmp byte ptr [rax + 0x21], r12b
00351211  74 16                           je 0x140351229
00351213  41 BE 80 00 00 00               mov r14d, 0x80
00351219  E9 F5 FA FF FF                  jmp 0x140350d13
0035121E  41 BE 80 00 00 00               mov r14d, 0x80
00351224  E9 F3 FA FF FF                  jmp 0x140350d1c
00351229  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0035122E  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
00351232  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00351237  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
0035123B  E9 D3 FA FF FF                  jmp 0x140350d13
00351240  41 81 FE 00 01 00 00            cmp r14d, 0x100
00351247  0F 83 AD 13 39 00               jae 0x1406e25fa
0035124D  45 8B C6                        mov r8d, r14d
00351250  41 83 E0 07                     and r8d, 7
00351254  45 03 C6                        add r8d, r14d
00351257  E9 51 F8 FF FF                  jmp 0x140350aad
0035125C  B8 03 00 00 C0                  mov eax, 0xc0000003
00351261  E9 D4 FA FF FF                  jmp 0x140350d3a
00351266  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0035126B  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0035126F  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00351273  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00351277  85 C0                           test eax, eax
00351279  0F 85 86 13 39 00               jne 0x1406e2605
0035127F  8B 05 FB 57 C7 00               mov eax, dword ptr [rip + 0xc757fb]
00351285  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0035128A  E9 76 13 39 00                  jmp 0x1406e2605
0035128F  8D 04 11                        lea eax, [rcx + rdx]
00351292  89 87 94 01 00 00               mov dword ptr [rdi + 0x194], eax
00351298  E9 BF FB FF FF                  jmp 0x140350e5c
0035129D  89 87 7C 01 00 00               mov dword ptr [rdi + 0x17c], eax
003512A3  E9 90 FE FF FF                  jmp 0x140351138
003512A8  48 8B CF                        mov rcx, rdi
003512AB  E8 A0 30 FF FF                  call 0x140344350
003512B0  E9 9F FE FF FF                  jmp 0x140351154
003512B5  44 39 78 18                     cmp dword ptr [rax + 0x18], r15d
003512B9  0F 84 30 FC FF FF               je 0x140350eef
003512BF  44 0F B6 E6                     movzx r12d, sil
003512C3  E9 35 FC FF FF                  jmp 0x140350efd
003512C8  89 8F 78 01 00 00               mov dword ptr [rdi + 0x178], ecx
003512CE  40 0F B6 DE                     movzx ebx, sil
003512D2  E9 3C FA FF FF                  jmp 0x140350d13
003512D7  89 8F 8C 01 00 00               mov dword ptr [rdi + 0x18c], ecx
003512DD  E9 2C FA FF FF                  jmp 0x140350d0e
003512E2  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
003512E7  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003512EB  44 38 60 21                     cmp byte ptr [rax + 0x21], r12b
003512EF  0F 85 95 FC FF FF               jne 0x140350f8a
003512F5  F7 87 98 01 00 00 00 80 00 00   test dword ptr [rdi + 0x198], 0x8000
003512FF  0F 84 14 13 39 00               je 0x1406e2619
00351305  41 BE 03 A0 00 C0               mov r14d, 0xc000a003
0035130B  E9 FE F9 FF FF                  jmp 0x140350d0e
00351310  83 E9 01                        sub ecx, 1
00351313  0F 84 C2 F9 FF FF               je 0x140350cdb
00351319  83 F9 02                        cmp ecx, 2
0035131C  0F 85 CA FE FF FF               jne 0x1403511ec
00351322  44 39 BF 80 01 00 00            cmp dword ptr [rdi + 0x180], r15d
00351329  0F 85 39 13 39 00               jne 0x1406e2668
0035132F  41 BE 01 00 00 C0               mov r14d, 0xc0000001
00351335  E9 D4 F9 FF FF                  jmp 0x140350d0e
0035133A  41 BE 01 00 00 C0               mov r14d, 0xc0000001
00351340  E9 CB F9 FF FF                  jmp 0x140350d10
00351345  40 84 F6                        test sil, sil
00351348  0F 85 CE F9 FF FF               jne 0x140350d1c
0035134E  41 BE 29 01 00 C0               mov r14d, 0xc0000129
00351354  E9 C3 F9 FF FF                  jmp 0x140350d1c
00351359  0F 1F 00                        nop dword ptr [rax]
0035135C  60                              .byte 0x60
0035135D  0B 35 00 1B 0B 35               or esi, dword ptr [rip + 0x350b1b00]
00351363  00 1B                           add byte ptr [rbx], bl
00351365  0B 35 00 1B 0B 35               or esi, dword ptr [rip + 0x350b1b00]
0035136B  00 00                           add byte ptr [rax], al
0035136D  00 00                           add byte ptr [rax], al
0035136F  00 00                           add byte ptr [rax], al
00351371  00 00                           add byte ptr [rax], al
00351373  00 1B                           add byte ptr [rbx], bl
00351375  0B 35 00 00 00 00               or esi, dword ptr [rip]
0035137B  00 D1                           add cl, dl
0035137D  0B 35 00 1B 0B 35               or esi, dword ptr [rip + 0x350b1b00]
00351383  00 3D 0B 35 00 1B               add byte ptr [rip + 0x1b00350b], bh
00351389  0B 35 00 1B 0B 35               or esi, dword ptr [rip + 0x350b1b00]
0035138F  00 90 0B 35 00 A6               add byte ptr [rax - 0x59ffcaf5], dl
00351395  10 35 00 2F 0E 35               adc byte ptr [rip + 0x350e2f00], dh
0035139B  00 77 0F                        add byte ptr [rdi + 0xf], dh
0035139E  35 00 C4 0E 35                  xor eax, 0x350ec400
003513A3  00 00                           add byte ptr [rax], al
003513A5  00 00                           add byte ptr [rax], al
003513A7  00 00                           add byte ptr [rax], al
003513A9  00 00                           add byte ptr [rax], al
003513AB  00 00                           add byte ptr [rax], al
003513AD  00 00                           add byte ptr [rax], al
003513AF  00 00                           add byte ptr [rax], al
003513B1  00 00                           add byte ptr [rax], al
003513B3  00 FF                           add bh, bh
003513B5  11 35 00 B0 11 35               adc dword ptr [rip + 0x3511b000], esi
003513BB  00 3B                           add byte ptr [rbx], bh
003513BD  10 35 00 00 00 00               adc byte ptr [rip], dh
003513C3  00 E3                           add bl, ah
003513C5  0F 35                           sysexit
003513C7  00 E2                           add dl, ah
003513C9  12 35 00 5C 12 35               adc dh, byte ptr [rip + 0x35125c00]
003513CF  00 5C 12 35                     add byte ptr [rdx + rdx + 0x35], bl
003513D3  00 30                           add byte ptr [rax], dh
003513D5  10 35 00 A7 0A 35               adc byte ptr [rip + 0x350aa700], dh
003513DB  00 A7 0A 35 00 A7               add byte ptr [rdi - 0x58ffcaf6], ah
003513E1  0A 35 00 25 0E 35               or dh, byte ptr [rip + 0x350e2500]
003513E7  00 5C 12 35                     add byte ptr [rdx + rdx + 0x35], bl
003513EB  00 A7 0A 35 00 A7               add byte ptr [rdi - 0x58ffcaf6], ah
003513F1  0A 35 00 A5 11 35               or dh, byte ptr [rip + 0x3511a500]
003513F7  00 5C 12 35                     add byte ptr [rdx + rdx + 0x35], bl
003513FB  00 A7 0A 35 00 A7               add byte ptr [rdi - 0x58ffcaf6], ah
00351401  0A 35 00 A7 0A 35               or dh, byte ptr [rip + 0x350aa700]
00351407  00 40 12                        add byte ptr [rax + 0x12], al
0035140A  35                              .byte 0x35
0035140B  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetInformationWorkerFactory(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 11246838)) ^ (v_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = 0;
    v_stack_m158 = v_xmm0;
    a2 = 0;
    result = memset(v_stack_m148, a2, 256, a4);
    if (((unsigned int)((int)(a2))) != 11) goto loc_00350E05;
loc_00350AAD:
    v_stack_m17C = 4;
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00350DEC;
    if (((unsigned int)((int)(a2))) != 9) goto loc_00350AFA;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00350AEF;
    if ((((unsigned __int8)(a3)) & (3)) != 0) goto loc_00350C01;
    if ((a3 + 4) > v_stack_m148) goto loc_00350C06;
    if ((a3 + 4) < a3) goto loc_00350C06;
loc_00350AEF:
    v_stack_m148 = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    goto loc_00350C0E;
loc_00350AFA:
    if (((unsigned int)((int)(a2) - 2)) > 13) goto loc_00350B14;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 3476135 + (int)(a2) - 2 * 4 + 3478364))) + (v_rip - 3476135);
loc_00350B14:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00350AEF;
    a1 = 37;
    if (a3 < 37) { a1 = a3; }
    v_stack_m148 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    goto loc_00350C0E;
loc_00350C01:
    result = ExRaiseDatatypeMisalignment(a1, v_rip - 3476135, 4, a4);
loc_00350C06:
    goto loc_00350AEF;
loc_00350C0E:
    goto loc_00350C15;
loc_00350C15:
    v_r15 = 0;
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m188;
    result = ObReferenceObjectByHandle(a1, v_r15 + 4, *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00350D3A;
    if (((unsigned int)((int)(a2))) == 8) goto loc_00351266;
    v_r12 = 0;
    v_stack_m170 = *(unsigned __int64 *)(v_stack_m188 + 16);
    v_stack_m178 = 0;
    if ((*(unsigned int *)(v_rip + 13066398)) != 0) goto loc_00350DB2;
loc_00350C88:
    v_stack_m168 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 13065842)) & (33)) != 0) goto loc_00350D5E;
loc_00350C9A:
    if (v_stack_m178 != 0) goto loc_00350DF6;
loc_00350CAB:
    if (((unsigned int)((int)(a2))) != 9) goto loc_00350CE4;
    if (((unsigned int)((unsigned int)(v_stack_m148))) != 2) goto loc_00350D7E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 384))) == 0) goto loc_00350DA7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m188 + 384))) - (1));
    *(unsigned int *)(v_stack_m188 + 384) = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_00350D0E;
loc_00350CDB:
    goto loc_00350D10;
loc_00350CE4:
    if (1 != 13) goto loc_00350DC3;
    a1 = (unsigned int)(((unsigned int)(v_stack_m148)) & (1));
    a1 = (unsigned int)((a1) << (11));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 408)))));
    *(unsigned int *)(v_stack_m188 + 408) = (unsigned int)(a1);
loc_00350D0E:
loc_00350D10:
    v_rsi = 0;
loc_00350D13:
    if (1 != 0) goto loc_00350E89;
loc_00350D1C:
    result = (unsigned int)(*(unsigned int *)(v_stack_m188 + 408));
    if (1 != 0) {
        a1 = v_stack_m178;
        result = KeReleaseInStackQueuedSpinLock(a1, v_stack_m178, *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    result = ObfDereferenceObjectWithTag(v_stack_m188, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
loc_00350D3A:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_rsp = (v_rsp) + (384);
    return result;
loc_00350D5E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12308724))) != 0) goto loc_00350C9A;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p40, v_stack_m188, *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00350CAB;
loc_00350D7E:
    if ((unsigned int)(v_stack_p40) != 0) goto loc_00351310;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 384)))) == (*(unsigned int *)(v_stack_m188 + 388))) goto loc_0035133A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m188 + 384))) + 1);
    *(unsigned int *)(v_stack_m188 + 384) = (unsigned int)(result);
    goto loc_00350D10;
loc_00350DA7:
    goto loc_00350D0E;
loc_00350DB2:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), (unsigned __int8)(result), *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00350C88;
loc_00350DC3:
    v_rbx = (unsigned int)((1) + (-2));
    if (((unsigned int)(v_rbx)) > 13) goto loc_00350DE5;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 3476949 + (int)((unsigned int)(v_rbx)) * 4 + 3478420))) + (v_rip - 3476949);
loc_00350DE5:
loc_00350DEC:
    goto loc_00350D3A;
loc_00350DF6:
    result = KxWaitForLockOwnerShip(v_stack_p40, v_rip - 3476949, *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00350CAB;
loc_00350E05:
    if (((unsigned int)(v_rbx)) > 15) goto loc_0035125C;
    result = ((unsigned int)(*(unsigned int *)(v_rip - 3477013 + v_rbx * 4 + 3478476))) + (v_rip - 3477013);
loc_00350E89:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m188 + 392))) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 384)))));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m188 + 16) + 33)) != 0) goto loc_0035121E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 384)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 380))))) goto loc_00351345;
    if ((*(unsigned int *)(v_stack_m188 + 400)) <= 0) goto loc_00350F16;
loc_00350EBC:
    goto loc_00350D1C;
loc_00350F16:
    if (a2 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 380))))) goto loc_00350EBC;
    result = (unsigned int)(*(unsigned int *)(v_stack_m188 + 380));
    if (((*(unsigned int *)(v_stack_m188 + 408)) & (512)) != 0) {
        a1 = v_stack_m188;
        result = ExpLeaveWorkerFactoryAwayMode(a1, a2, *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_p40, a2, *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_rbx = 0;
    result = ExpWorkerFactoryCreateThread(v_stack_m188, a2, *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (!sign_flag) goto loc_00350D1C;
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(v_stack_m188 + 16), v_stack_p40, *(unsigned __int64 *)(v_rip + 13059524), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (0 == 0) goto loc_00350D1C;
    goto loc_00350EBC;
loc_003511EC:
    goto loc_00350D0E;
loc_0035121E:
    goto loc_00350D1C;
loc_0035125C:
    goto loc_00350D3A;
loc_00351266:
loc_00351310:
    a1 = (unsigned int)((v_stack_p30) - (1));
    if (condition_is_equal) goto loc_00350CDB;
    if (((unsigned int)(a1)) != 2) goto loc_003511EC;
    goto loc_00350D0E;
loc_0035133A:
    goto loc_00350D10;
loc_00351345:
    if (0 != 0) goto loc_00350D1C;
    goto loc_00350D1C;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetInformationWorkerFactory(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m48;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0xAB9CF6)) ^ (local_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = 0;
    v_stack_m158 = v_xmm0;
    Arg2 = 0;
    result = memset(v_stack_m148, Arg2, 256, Arg4);
    if (((uint32_t)((int32_t)(Arg2))) != 11) goto loc_00350E05;
loc_00350AAD:
    v_stack_m17C = 4;
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00350DEC;
    if (((uint32_t)((int32_t)(Arg2))) != 9) goto loc_00350AFA;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00350AEF;
    if ((((uint8_t)(Arg3)) & (3)) != 0) goto loc_00350C01;
    if ((Arg3 + 4) > v_stack_m148) goto loc_00350C06;
    if ((Arg3 + 4) < Arg3) goto loc_00350C06;
loc_00350AEF:
    v_stack_m148 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3)));
    goto loc_00350C0E;
loc_00350AFA:
    if (((uint32_t)((int32_t)(Arg2) - 2)) > 13) goto loc_00350B14;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x350AA7 + (int32_t)(Arg2) - 0x2 * 4 + 0x35135C))) + (v_rip - 3476135);
loc_00350B14:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00350AEF;
    Arg1 = 37;
    if (Arg3 < 37) { Arg1 = Arg3; }
    v_stack_m148 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    goto loc_00350C0E;
loc_00350C01:
    result = ExRaiseDatatypeMisalignment(Arg1, v_rip - 3476135, 4, Arg4);
loc_00350C06:
    goto loc_00350AEF;
loc_00350C0E:
    goto loc_00350C15;
loc_00350C15:
    local_r15 = 0;
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m188;
    result = ObReferenceObjectByHandle(Arg1, local_r15 + 4, *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00350D3A;
    if (((uint32_t)((int32_t)(Arg2))) == 8) goto loc_00351266;
    local_r12 = 0;
    v_stack_m170 = *(uint64_t *)(v_stack_m188 + 0x10);
    v_stack_m178 = 0;
    if ((*(uint32_t *)(v_rip + 0xC7609E)) != 0) goto loc_00350DB2;
loc_00350C88:
    v_stack_m168 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xC75E72)) & (33)) != 0) goto loc_00350D5E;
loc_00350C9A:
    if (v_stack_m178 != 0) goto loc_00350DF6;
loc_00350CAB:
    if (((uint32_t)((int32_t)(Arg2))) != 9) goto loc_00350CE4;
    if (((uint32_t)((uint32_t)(v_stack_m148))) != 2) goto loc_00350D7E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x180))) == 0) goto loc_00350DA7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x180))) - (1));
    *(uint32_t *)(v_stack_m188 + 0x180) = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_00350D0E;
loc_00350CDB:
    goto loc_00350D10;
loc_00350CE4:
    if (1 != 13) goto loc_00350DC3;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m148)) & (1));
    Arg1 = (uint32_t)((Arg1) << (11));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x198)))));
    *(uint32_t *)(v_stack_m188 + 0x198) = (uint32_t)(Arg1);
loc_00350D0E:
loc_00350D10:
    local_rsi = 0;
loc_00350D13:
    if (1 != 0) goto loc_00350E89;
loc_00350D1C:
    result = (uint32_t)(*(uint32_t *)(v_stack_m188 + 0x198));
    if (1 != 0) {
        Arg1 = v_stack_m178;
        result = KeReleaseInStackQueuedSpinLock(Arg1, v_stack_m178, *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    result = ObfDereferenceObjectWithTag(v_stack_m188, (uint32_t)(0x746C6644ULL), *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
loc_00350D3A:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x746C6644ULL), *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    local_rsp = (local_rsp) + (384);
    return result;
loc_00350D5E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBBD0F4))) != 0) goto loc_00350C9A;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p40, v_stack_m188, *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00350CAB;
loc_00350D7E:
    if ((uint32_t)(v_stack_p40) != 0) goto loc_00351310;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x180)))) == (*(uint32_t *)(v_stack_m188 + 0x184))) goto loc_0035133A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x180))) + 1);
    *(uint32_t *)(v_stack_m188 + 0x180) = (uint32_t)(result);
    goto loc_00350D10;
loc_00350DA7:
    goto loc_00350D0E;
loc_00350DB2:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), (uint8_t)(result), *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00350C88;
loc_00350DC3:
    local_rbx = (uint32_t)((1) + (-2));
    if (((uint32_t)(local_rbx)) > 13) goto loc_00350DE5;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x350DD5 + (int32_t)((uint32_t)(local_rbx)) * 4 + 0x351394))) + (v_rip - 3476949);
loc_00350DE5:
loc_00350DEC:
    goto loc_00350D3A;
loc_00350DF6:
    result = KxWaitForLockOwnerShip(v_stack_p40, v_rip - 3476949, *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00350CAB;
loc_00350E05:
    if (((uint32_t)(local_rbx)) > 15) goto loc_0035125C;
    result = ((uint32_t)(*(uint32_t *)(v_rip - 0x350E15 + local_rbx * 4 + 0x3513CC))) + (v_rip - 3477013);
loc_00350E89:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x188))) + ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x180)))));
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m188 + 0x10) + 0x21)) != 0) goto loc_0035121E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x180)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x17C))))) goto loc_00351345;
    if ((*(uint32_t *)(v_stack_m188 + 0x190)) <= 0) goto loc_00350F16;
loc_00350EBC:
    goto loc_00350D1C;
loc_00350F16:
    if (Arg2 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x17C))))) goto loc_00350EBC;
    result = (uint32_t)(*(uint32_t *)(v_stack_m188 + 0x17C));
    if (((*(uint32_t *)(v_stack_m188 + 0x198)) & (512)) != 0) {
        Arg1 = v_stack_m188;
        result = ExpLeaveWorkerFactoryAwayMode(Arg1, Arg2, *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_p40, Arg2, *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    local_rbx = 0;
    result = ExpWorkerFactoryCreateThread(v_stack_m188, Arg2, *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (!sign_flag) goto loc_00350D1C;
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(v_stack_m188 + 0x10), v_stack_p40, *(uint64_t *)(v_rip + 0xC745C4), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (0 == 0) goto loc_00350D1C;
    goto loc_00350EBC;
loc_003511EC:
    goto loc_00350D0E;
loc_0035121E:
    goto loc_00350D1C;
loc_0035125C:
    goto loc_00350D3A;
loc_00351266:
loc_00351310:
    Arg1 = (uint32_t)((v_stack_p30) - (1));
    if (condition_is_equal) goto loc_00350CDB;
    if (((uint32_t)(Arg1)) != 2) goto loc_003511EC;
    goto loc_00350D0E;
loc_0035133A:
    goto loc_00350D10;
loc_00351345:
    if (0 != 0) goto loc_00350D1C;
    goto loc_00350D1C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00350A30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
