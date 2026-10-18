# NtFreeUserPhysicalPages

- RVA: `0x0080AF30`–`0x0080B44B` (길이 `1,307` bytes)
- VA: `0x000000014080AF30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D8C44`
- 디코드: `325`개 명령, `1,307/1,307` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0080AF90` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0080B049` → [MiReferenceAweHandle](../../text/4E/MiReferenceAweHandle_function_004E00A4.md) (function, `0x004E00A4`)
- `0x0080B066` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x0080B0C2` → [MiGetAwePageSize](../../text/46/MiGetAwePageSize_function_0046CFA8.md) (function, `0x0046CFA8`)
- `0x0080B116` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x0080B19A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0080B1A4` → [MiCaptureUlongPtrArray](MiCaptureUlongPtrArray_function_0080A664.md) (function, `0x0080A664`)
- `0x0080B1D8` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x0080B1F0` → [LOCK_ADDRESS_SPACE](../../text/2A/LOCK_ADDRESS_SPACE_function_002A4944.md) (function, `0x002A4944`)
- `0x0080B211` → [MiBuildPhysicalPageFreeChain](../../text/68/MiBuildPhysicalPageFreeChain_function_00687C80.md) (function, `0x00687C80`)
- `0x0080B243` → [MiReturnProcessCommitment](../../text/45/MiReturnProcessCommitment_function_0045CED4.md) (function, `0x0045CED4`)
- `0x0080B25A` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x0080B28E` → [MiFreePhysicalPageChain](../../text/2A/MiFreePhysicalPageChain_function_002A9F1C.md) (function, `0x002A9F1C`)
- `0x0080B2B0` → [MiPreparePhysicalPagesMdlForFree](../../text/68/MiPreparePhysicalPagesMdlForFree_function_006890A4.md) (function, `0x006890A4`)
- `0x0080B2C2` → [MiFreePagesFromMdl](../../text/3F/MiFreePagesFromMdl_function_003F8300.md) (function, `0x003F8300`)
- `0x0080B2CC` → [MiGetAweInfoPartition](../../text/2A/MiGetAweInfoPartition_function_002AA2CC.md) (function, `0x002AA2CC`)
- `0x0080B30E` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (function, `0x00443B10`)
- `0x0080B324` → [MiReturnCrossPartitionCharges](../../text/28/MiReturnCrossPartitionCharges_function_002867D0.md) (function, `0x002867D0`)
- `0x0080B360` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0080B3BD` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (function, `0x002A4844`)
- `0x0080B3DF` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)
- `0x0080B3F3` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0080B40D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0080B432` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0080AF43` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x0080AF90` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0080B049` → [MiReferenceAweHandle](../../text/4E/MiReferenceAweHandle_function_004E00A4.md) (`PAGE` → `.text`)
  - `0x0080B066` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x0080B0C2` → [MiGetAwePageSize](../../text/46/MiGetAwePageSize_function_0046CFA8.md) (`PAGE` → `.text`)
  - `0x0080B116` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x0080B19A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0080B1D8` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x0080B1F0` → [LOCK_ADDRESS_SPACE](../../text/2A/LOCK_ADDRESS_SPACE_function_002A4944.md) (`PAGE` → `.text`)
  - `0x0080B211` → [MiBuildPhysicalPageFreeChain](../../text/68/MiBuildPhysicalPageFreeChain_function_00687C80.md) (`PAGE` → `.text`)
  - `0x0080B243` → [MiReturnProcessCommitment](../../text/45/MiReturnProcessCommitment_function_0045CED4.md) (`PAGE` → `.text`)
  - `0x0080B25A` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x0080B28E` → [MiFreePhysicalPageChain](../../text/2A/MiFreePhysicalPageChain_function_002A9F1C.md) (`PAGE` → `.text`)
  - `0x0080B2B0` → [MiPreparePhysicalPagesMdlForFree](../../text/68/MiPreparePhysicalPagesMdlForFree_function_006890A4.md) (`PAGE` → `.text`)
  - `0x0080B2C2` → [MiFreePagesFromMdl](../../text/3F/MiFreePagesFromMdl_function_003F8300.md) (`PAGE` → `.text`)
  - `0x0080B2CC` → [MiGetAweInfoPartition](../../text/2A/MiGetAweInfoPartition_function_002AA2CC.md) (`PAGE` → `.text`)
  - `0x0080B30E` → [MiGetProcessPartition](../../text/44/MiGetProcessPartition_function_00443B10.md) (`PAGE` → `.text`)
  - `0x0080B324` → [MiReturnCrossPartitionCharges](../../text/28/MiReturnCrossPartitionCharges_function_002867D0.md) (`PAGE` → `.text`)
  - `0x0080B360` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0080B3BD` → [UNLOCK_ADDRESS_SPACE](../../text/2A/UNLOCK_ADDRESS_SPACE_function_002A4844.md) (`PAGE` → `.text`)
  - `0x0080B3DF` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (`PAGE` → `.text`)
  - `0x0080B3F3` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0080B40D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0080B432` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0080AF30  40 53                           push rbx
0080AF32  56                              push rsi
0080AF33  57                              push rdi
0080AF34  41 54                           push r12
0080AF36  41 55                           push r13
0080AF38  41 56                           push r14
0080AF3A  41 57                           push r15
0080AF3C  48 81 EC 30 11 00 00            sub rsp, 0x1130
0080AF43  48 8B 05 F6 F7 5F 00            mov rax, qword ptr [rip + 0x5ff7f6]
0080AF4A  48 33 C4                        xor rax, rsp
0080AF4D  48 89 84 24 20 11 00 00         mov qword ptr [rsp + 0x1120], rax
0080AF55  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0080AF5A  4C 8B FA                        mov r15, rdx
0080AF5D  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
0080AF62  48 8B F9                        mov rdi, rcx
0080AF65  0F 57 C0                        xorps xmm0, xmm0
0080AF68  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
0080AF70  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
0080AF78  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
0080AF80  33 D2                           xor edx, edx
0080AF82  41 B8 30 10 00 00               mov r8d, 0x1030
0080AF88  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
0080AF90  E8 AB BC EB FF                  call 0x1406c6c40
0080AF95  33 D2                           xor edx, edx
0080AF97  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0080AF9C  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0080AFA1  0F 57 C0                        xorps xmm0, xmm0
0080AFA4  33 C0                           xor eax, eax
0080AFA6  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
0080AFAE  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
0080AFB6  8B DA                           mov ebx, edx
0080AFB8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0080AFC1  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0080AFC6  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0080AFCD  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
0080AFD2  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
0080AFD8  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0080AFDC  84 C0                           test al, al
0080AFDE  75 0A                           jne 0x14080afea
0080AFE0  4D 8B 27                        mov r12, qword ptr [r15]
0080AFE3  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0080AFE8  EB 26                           jmp 0x14080b010
0080AFEA  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
0080AFF4  4C 3B F9                        cmp r15, rcx
0080AFF7  49 0F 42 CF                     cmovb rcx, r15
0080AFFB  48 8B 01                        mov rax, qword ptr [rcx]
0080AFFE  48 89 01                        mov qword ptr [rcx], rax
0080B001  4D 8B 27                        mov r12, qword ptr [r15]
0080B004  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0080B009  49 89 17                        mov qword ptr [r15], rdx
0080B00C  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
0080B010  4D 85 E4                        test r12, r12
0080B013  75 0A                           jne 0x14080b01f
0080B015  B8 F0 00 00 C0                  mov eax, 0xc00000f0
0080B01A  E9 08 04 00 00                  jmp 0x14080b427
0080B01F  4C 8B F2                        mov r14, rdx
0080B022  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0080B027  48 8D B4 24 F0 00 00 00         lea rsi, [rsp + 0xf0]
0080B02F  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0080B034  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0080B039  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0080B03E  44 8A C0                        mov r8b, al
0080B041  BA 02 00 00 00                  mov edx, 2
0080B046  48 8B CF                        mov rcx, rdi
0080B049  E8 56 50 CD FF                  call 0x1404e00a4
0080B04E  45 33 C0                        xor r8d, r8d
0080B051  85 C0                           test eax, eax
0080B053  0F 88 CE 03 00 00               js 0x14080b427
0080B059  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0080B05E  4D 85 ED                        test r13, r13
0080B061  74 13                           je 0x14080b076
0080B063  49 8B CD                        mov rcx, r13
0080B066  E8 45 9C A8 FF                  call 0x140294cb0
0080B06B  4C 8B 70 08                     mov r14, qword ptr [rax + 8]
0080B06F  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
0080B074  EB 0D                           jmp 0x14080b083
0080B076  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0080B07B  48 85 FF                        test rdi, rdi
0080B07E  75 0D                           jne 0x14080b08d
0080B080  8D 5F 04                        lea ebx, [rdi + 4]
0080B083  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0080B088  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0080B08D  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0080B092  4D 85 F6                        test r14, r14
0080B095  75 28                           jne 0x14080b0bf
0080B097  48 8B 87 10 04 00 00            mov rax, qword ptr [rdi + 0x410]
0080B09E  4C 8B B0 48 04 00 00            mov r14, qword ptr [rax + 0x448]
0080B0A5  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
0080B0AA  4D 85 F6                        test r14, r14
0080B0AD  75 10                           jne 0x14080b0bf
0080B0AF  41 BE EF 00 00 C0               mov r14d, 0xc00000ef
0080B0B5  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0080B0BA  E9 13 03 00 00                  jmp 0x14080b3d2
0080B0BF  49 8B CE                        mov rcx, r14
0080B0C2  E8 E1 1E C6 FF                  call 0x14046cfa8
0080B0C7  48 8B C8                        mov rcx, rax
0080B0CA  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0080B0D2  49 8B F0                        mov rsi, r8
0080B0D5  41 B9 00 02 00 00               mov r9d, 0x200
0080B0DB  45 8B F9                        mov r15d, r9d
0080B0DE  4D 3B E1                        cmp r12, r9
0080B0E1  76 51                           jbe 0x14080b134
0080B0E3  B8 00 00 0C 00                  mov eax, 0xc0000
0080B0E8  BA FF FF 0F 00                  mov edx, 0xfffff
0080B0ED  48 83 F9 01                     cmp rcx, 1
0080B0F1  0F 45 C2                        cmovne eax, edx
0080B0F4  4D 8B FC                        mov r15, r12
0080B0F7  4C 3B E0                        cmp r12, rax
0080B0FA  4C 0F 47 F8                     cmova r15, rax
0080B0FE  4D 3B F9                        cmp r15, r9
0080B101  76 31                           jbe 0x14080b134
0080B103  41 8B D7                        mov edx, r15d
0080B106  C1 E2 0C                        shl edx, 0xc
0080B109  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0080B10E  45 33 C9                        xor r9d, r9d
0080B111  45 33 C0                        xor r8d, r8d
0080B114  33 C9                           xor ecx, ecx
0080B116  E8 D5 3A A9 FF                  call 0x14029ebf0
0080B11B  48 8B F0                        mov rsi, rax
0080B11E  45 33 C0                        xor r8d, r8d
0080B121  41 B9 00 02 00 00               mov r9d, 0x200
0080B127  48 85 C0                        test rax, rax
0080B12A  75 05                           jne 0x14080b131
0080B12C  49 D1 EF                        shr r15, 1
0080B12F  EB CD                           jmp 0x14080b0fe
0080B131  83 CB 08                        or ebx, 8
0080B134  48 85 F6                        test rsi, rsi
0080B137  75 0B                           jne 0x14080b144
0080B139  48 8D B4 24 F0 00 00 00         lea rsi, [rsp + 0xf0]
0080B141  4D 8B F9                        mov r15, r9
0080B144  4C 8D 4E 30                     lea r9, [rsi + 0x30]
0080B148  4D 3B FC                        cmp r15, r12
0080B14B  4D 0F 47 FC                     cmova r15, r12
0080B14F  49 8B CF                        mov rcx, r15
0080B152  48 C1 E1 0C                     shl rcx, 0xc
0080B156  4C 89 06                        mov qword ptr [rsi], r8
0080B159  48 8D 81 FF 0F 00 00            lea rax, [rcx + 0xfff]
0080B160  48 C1 E8 0C                     shr rax, 0xc
0080B164  66 83 C0 06                     add ax, 6
0080B168  66 C1 E0 03                     shl ax, 3
0080B16C  66 89 46 08                     mov word ptr [rsi + 8], ax
0080B170  66 44 89 46 0A                  mov word ptr [rsi + 0xa], r8w
0080B175  4C 89 46 20                     mov qword ptr [rsi + 0x20], r8
0080B179  44 89 46 2C                     mov dword ptr [rsi + 0x2c], r8d
0080B17D  89 4E 28                        mov dword ptr [rsi + 0x28], ecx
0080B180  83 E3 FE                        and ebx, 0xfffffffe
0080B183  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0080B188  49 8B C9                        mov rcx, r9
0080B18B  44 38 44 24 30                  cmp byte ptr [rsp + 0x30], r8b
0080B190  75 0F                           jne 0x14080b1a1
0080B192  4E 8D 04 FD 00 00 00 00         lea r8, [r15*8]
0080B19A  E8 A1 B6 EB FF                  call 0x1406c6840
0080B19F  EB 1C                           jmp 0x14080b1bd
0080B1A1  4D 8B C7                        mov r8, r15
0080B1A4  E8 BB F4 FF FF                  call 0x14080a664
0080B1A9  44 8B F0                        mov r14d, eax
0080B1AC  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0080B1B0  85 C0                           test eax, eax
0080B1B2  0F 88 15 02 00 00               js 0x14080b3cd
0080B1B8  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
0080B1BD  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0080B1C2  48 39 B8 B8 00 00 00            cmp qword ptr [rax + 0xb8], rdi
0080B1C9  74 1A                           je 0x14080b1e5
0080B1CB  4C 8D 84 24 B8 00 00 00         lea r8, [rsp + 0xb8]
0080B1D3  33 D2                           xor edx, edx
0080B1D5  48 8B CF                        mov rcx, rdi
0080B1D8  E8 43 B6 A0 FF                  call 0x140216820
0080B1DD  83 CB 01                        or ebx, 1
0080B1E0  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0080B1E5  4D 85 ED                        test r13, r13
0080B1E8  75 19                           jne 0x14080b203
0080B1EA  48 8B D7                        mov rdx, rdi
0080B1ED  48 8B C8                        mov rcx, rax
0080B1F0  E8 4F 97 A9 FF                  call 0x1402a4944
0080B1F5  8B 87 F4 01 00 00               mov eax, dword ptr [rdi + 0x1f4]
0080B1FB  A8 20                           test al, 0x20
0080B1FD  0F 85 B2 01 00 00               jne 0x14080b3b5
0080B203  4C 8D 84 24 A0 00 00 00         lea r8, [rsp + 0xa0]
0080B20B  48 8B D6                        mov rdx, rsi
0080B20E  49 8B CE                        mov rcx, r14
0080B211  E8 6A CA E7 FF                  call 0x140687c80
0080B216  44 8B F0                        mov r14d, eax
0080B219  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0080B21D  8B 46 2C                        mov eax, dword ptr [rsi + 0x2c]
0080B220  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0080B228  45 33 C0                        xor r8d, r8d
0080B22B  48 85 C0                        test rax, rax
0080B22E  74 1D                           je 0x14080b24d
0080B230  4D 85 ED                        test r13, r13
0080B233  75 13                           jne 0x14080b248
0080B235  8B D0                           mov edx, eax
0080B237  48 0F AF 94 24 80 00 00 00      imul rdx, qword ptr [rsp + 0x80]
0080B240  48 8B CF                        mov rcx, rdi
0080B243  E8 8C 1C C5 FF                  call 0x14045ced4
0080B248  4C 01 7C 24 78                  add qword ptr [rsp + 0x78], r15
0080B24D  4D 85 ED                        test r13, r13
0080B250  75 10                           jne 0x14080b262
0080B252  48 8B D7                        mov rdx, rdi
0080B255  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0080B25A  E8 E5 95 A9 FF                  call 0x1402a4844
0080B25F  45 33 C0                        xor r8d, r8d
0080B262  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
0080B265  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0080B26D  48 85 C0                        test rax, rax
0080B270  0F 84 C0 00 00 00               je 0x14080b336
0080B276  48 83 BC 24 80 00 00 00 01      cmp qword ptr [rsp + 0x80], 1
0080B27F  74 1A                           je 0x14080b29b
0080B281  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
0080B289  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0080B28E  E8 89 EC A9 FF                  call 0x1402a9f1c
0080B293  45 33 C0                        xor r8d, r8d
0080B296  E9 9B 00 00 00                  jmp 0x14080b336
0080B29B  B9 02 00 00 00                  mov ecx, 2
0080B2A0  66 09 4E 0A                     or word ptr [rsi + 0xa], cx
0080B2A4  C1 E0 0C                        shl eax, 0xc
0080B2A7  89 46 28                        mov dword ptr [rsi + 0x28], eax
0080B2AA  8D 51 FF                        lea edx, [rcx - 1]
0080B2AD  48 8B CE                        mov rcx, rsi
0080B2B0  E8 EF DD E7 FF                  call 0x1406890a4
0080B2B5  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
0080B2BA  45 33 C0                        xor r8d, r8d
0080B2BD  33 D2                           xor edx, edx
0080B2BF  48 8B CE                        mov rcx, rsi
0080B2C2  E8 39 D0 BE FF                  call 0x1403f8300
0080B2C7  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0080B2CC  E8 FB EF A9 FF                  call 0x1402aa2cc
0080B2D1  4C 8B D0                        mov r10, rax
0080B2D4  4C 8B 8C 24 88 00 00 00         mov r9, qword ptr [rsp + 0x88]
0080B2DC  49 8B C1                        mov rax, r9
0080B2DF  48 F7 D8                        neg rax
0080B2E2  F0 49 01 82 A8 4C 00 00         lock add qword ptr [r10 + 0x4ca8], rax
0080B2EA  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0080B2EF  45 33 C0                        xor r8d, r8d
0080B2F2  4D 85 ED                        test r13, r13
0080B2F5  75 12                           jne 0x14080b309
0080B2F7  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0080B2FC  F0 48 01 81 70 05 00 00         lock add qword ptr [rcx + 0x570], rax
0080B304  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0080B309  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0080B30E  E8 FD 87 C3 FF                  call 0x140443b10
0080B313  4C 3B D0                        cmp r10, rax
0080B316  74 14                           je 0x14080b32c
0080B318  BA 04 00 00 00                  mov edx, 4
0080B31D  44 8D 42 FD                     lea r8d, [rdx - 3]
0080B321  49 8B CA                        mov rcx, r10
0080B324  E8 A7 B4 A7 FF                  call 0x1402867d0
0080B329  45 33 C0                        xor r8d, r8d
0080B32C  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0080B331  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
0080B336  4C 2B A4 24 90 00 00 00         sub r12, qword ptr [rsp + 0x90]
0080B33E  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0080B343  45 85 F6                        test r14d, r14d
0080B346  0F 85 81 00 00 00               jne 0x14080b3cd
0080B34C  4D 85 E4                        test r12, r12
0080B34F  74 7C                           je 0x14080b3cd
0080B351  F6 C3 01                        test bl, 1
0080B354  74 15                           je 0x14080b36b
0080B356  33 D2                           xor edx, edx
0080B358  48 8D 8C 24 B8 00 00 00         lea rcx, [rsp + 0xb8]
0080B360  E8 CB C9 A0 FF                  call 0x140217d30
0080B365  83 E3 FE                        and ebx, 0xfffffffe
0080B368  45 33 C0                        xor r8d, r8d
0080B36B  4C 39 87 10 03 00 00            cmp qword ptr [rdi + 0x310], r8
0080B372  74 29                           je 0x14080b39d
0080B374  0F B7 87 EC 06 00 00            movzx eax, word ptr [rdi + 0x6ec]
0080B37B  B9 4C 01 00 00                  mov ecx, 0x14c
0080B380  66 3B C1                        cmp ax, cx
0080B383  74 0D                           je 0x14080b392
0080B385  B9 C4 01 00 00                  mov ecx, 0x1c4
0080B38A  66 3B C1                        cmp ax, cx
0080B38D  41 8A C0                        mov al, r8b
0080B390  75 02                           jne 0x14080b394
0080B392  B0 01                           mov al, 1
0080B394  84 C0                           test al, al
0080B396  B8 04 00 00 00                  mov eax, 4
0080B39B  75 05                           jne 0x14080b3a2
0080B39D  B8 08 00 00 00                  mov eax, 8
0080B3A2  49 0F AF C7                     imul rax, r15
0080B3A6  48 01 44 24 58                  add qword ptr [rsp + 0x58], rax
0080B3AB  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
0080B3B0  E9 8F FD FF FF                  jmp 0x14080b144
0080B3B5  48 8B D7                        mov rdx, rdi
0080B3B8  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0080B3BD  E8 82 94 A9 FF                  call 0x1402a4844
0080B3C2  41 BE 0A 01 00 C0               mov r14d, 0xc000010a
0080B3C8  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
0080B3CD  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0080B3D2  F6 C3 08                        test bl, 8
0080B3D5  74 0D                           je 0x14080b3e4
0080B3D7  66 83 66 0A FD                  and word ptr [rsi + 0xa], 0xfffd
0080B3DC  48 8B CE                        mov rcx, rsi
0080B3DF  E8 9C 36 A9 FF                  call 0x14029ea80
0080B3E4  F6 C3 01                        test bl, 1
0080B3E7  74 0F                           je 0x14080b3f8
0080B3E9  33 D2                           xor edx, edx
0080B3EB  48 8D 8C 24 B8 00 00 00         lea rcx, [rsp + 0xb8]
0080B3F3  E8 38 C9 A0 FF                  call 0x140217d30
0080B3F8  F6 C3 04                        test bl, 4
0080B3FB  75 16                           jne 0x14080b413
0080B3FD  BA 4D 6D 50 68                  mov edx, 0x68506d4d
0080B402  4D 85 ED                        test r13, r13
0080B405  49 8B CD                        mov rcx, r13
0080B408  75 03                           jne 0x14080b40d
0080B40A  48 8B CF                        mov rcx, rdi
0080B40D  E8 CE C4 AE FF                  call 0x1402f78e0
0080B412  90                              nop
0080B413  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0080B418  49 89 07                        mov qword ptr [r15], rax
0080B41B  EB 05                           jmp 0x14080b422
0080B41D  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0080B422  41 8B C6                        mov eax, r14d
0080B425  EB 00                           jmp 0x14080b427
0080B427  48 8B 8C 24 20 11 00 00         mov rcx, qword ptr [rsp + 0x1120]
0080B42F  48 33 CC                        xor rcx, rsp
0080B432  E8 09 12 EA FF                  call 0x1406ac640
0080B437  48 81 C4 30 11 00 00            add rsp, 0x1130
0080B43E  41 5F                           pop r15
0080B440  41 5E                           pop r14
0080B442  41 5D                           pop r13
0080B444  41 5C                           pop r12
0080B446  5F                              pop rdi
0080B447  5E                              pop rsi
0080B448  5B                              pop rbx
0080B449  C3                              ret
0080B44A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtFreeUserPhysicalPages(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1078;
    unsigned __int64 v_stack_m1090;
    unsigned __int64 v_stack_m10A0;
    unsigned __int64 v_stack_m10B0;
    unsigned __int64 v_stack_m10B8;
    unsigned __int64 v_stack_m10C8;
    unsigned __int64 v_stack_m10D8;
    unsigned __int64 v_stack_m10E0;
    unsigned __int64 v_stack_m10E8;
    unsigned __int64 v_stack_m10F0;
    unsigned __int64 v_stack_m10F8;
    unsigned __int64 v_stack_m1100;
    unsigned __int64 v_stack_m1108;
    unsigned __int64 v_stack_m1110;
    unsigned __int64 v_stack_m1118;
    unsigned __int64 v_stack_m1120;
    unsigned __int64 v_stack_m1128;
    unsigned __int64 v_stack_m1130;
    unsigned int v_stack_m1134;
    unsigned __int8 v_stack_m1138;
    unsigned __int64 v_stack_m1148;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (0x1130ULL);
    result = (*(unsigned __int64 *)(v_rip + 6289398)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1110 = a3;
    v_stack_m1100 = a2;
    v_stack_m10B0 = v_xmm0;
    v_stack_m10A0 = v_xmm0;
    v_stack_m1090 = v_xmm0;
    a2 = 0;
    result = memset(v_stack_m1078, a2, (unsigned int)(0x1030ULL), a4);
    a2 = 0;
    v_stack_m1130 = 0;
    v_stack_m1120 = 0;
    result = 0;
    v_stack_m10C8 = v_xmm0;
    v_stack_m10B8 = 0;
    v_stack_m1108 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m10F8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m1138 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_0080AFEA;
    v_stack_m1118 = *(unsigned __int64 *)(a2);
    goto loc_0080B010;
loc_0080AFEA:
    a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    if (0 < (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) { a1 = 0; }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    v_stack_m1118 = *(unsigned __int64 *)(a2);
    *(unsigned __int64 *)(a2) = 0;
loc_0080B010:
    if (*(unsigned __int64 *)(a2) != 0) goto loc_0080B01F;
    goto loc_0080B427;
loc_0080B01F:
    v_stack_m1128 = 0;
    v_stack_m1148 = v_stack_m1120;
    result = MiReferenceAweHandle(a1, 2, (unsigned __int8)((unsigned int)(0xC00000F0ULL)), v_stack_m1130);
    a3 = 0;
    if (sign_flag) goto loc_0080B427;
    if (v_stack_m1120 == 0) goto loc_0080B076;
    result = MiSectionControlArea(v_stack_m1120, 2, a3, v_stack_m1130);
    v_stack_m1128 = *(unsigned __int64 *)(result + 8);
    goto loc_0080B083;
loc_0080B076:
    if (v_stack_m1130 != 0) goto loc_0080B08D;
loc_0080B083:
    v_stack_m1130 = v_stack_m10F8;
loc_0080B08D:
    v_stack_m10F0 = 0;
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_0080B0BF;
    v_stack_m1128 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m10F8 + 1040) + 1096);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m10F8 + 1040) + 1096) != 0) goto loc_0080B0BF;
    v_stack_m1134 = (unsigned int)((unsigned int)(0xC00000EFULL));
    goto loc_0080B3D2;
loc_0080B0BF:
    result = MiGetAwePageSize((unsigned int)(0xC00000EFULL), 2, a3, v_stack_m1130);
    v_stack_m10E8 = result;
    if ((*(unsigned __int64 *)(a2)) <= 512) goto loc_0080B134;
    result = (unsigned int)(0xC0000ULL);
    if (result != 1) { result = (unsigned int)((unsigned int)(0xFFFFFULL)); }
    v_r15 = *(unsigned __int64 *)(a2);
    if ((*(unsigned __int64 *)(a2)) > result) { v_r15 = result; }
loc_0080B0FE:
    if (v_r15 <= 512) goto loc_0080B134;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) << (12));
    v_stack_m1148 = 0;
    a4 = 0;
    a3 = 0;
    a1 = 0;
    result = IoAllocateMdl(a1, a2, a3, a4);
    a3 = 0;
    if (result != 0) goto loc_0080B131;
    v_r15 = (v_r15) >> (1);
    goto loc_0080B0FE;
loc_0080B131:
    v_rbx = (unsigned int)((v_stack_m1130 + 4) | (8));
loc_0080B134:
    v_rsi = result;
    if (result == 0) {
        v_rsi = v_stack_m1078;
        v_r15 = 512;
    }
    if (v_r15 > (*(unsigned __int64 *)(a2))) { v_r15 = *(unsigned __int64 *)(a2); }
    a1 = (v_r15) << (12);
    *(unsigned __int64 *)(v_rsi) = 0;
    result = (a1 + 4095) >> (12);
    result = (unsigned __int16)((result) + (6));
    result = (unsigned __int16)((result) << (3));
    *(unsigned __int16 *)(v_rsi + 8) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_rsi + 10) = 0;
    *(unsigned __int64 *)(v_rsi + 32) = 0;
    *(unsigned int *)(v_rsi + 44) = 0;
    *(unsigned int *)(v_rsi + 40) = (unsigned int)(a1);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFEULL));
    if (v_stack_m1138 != 0) goto loc_0080B1A1;
    result = memcpy(v_rsi + 48, v_stack_m1110, v_r15 * 8, v_rsi + 48);
    goto loc_0080B1BD;
loc_0080B1A1:
    result = MiCaptureUlongPtrArray(v_rsi + 48, v_stack_m1110, v_r15, v_rsi + 48);
    v_stack_m1134 = (unsigned int)(result);
    if (sign_flag) goto loc_0080B3CD;
loc_0080B1BD:
    result = v_stack_m1108;
    if ((*(unsigned __int64 *)(v_stack_m1108 + 184)) != v_stack_m10F8) {
        a3 = v_stack_m10B0;
        a2 = 0;
        a1 = v_stack_m10F8;
        result = KiStackAttachProcess(a1, a2, a3, v_rsi + 48);
        v_rbx = (unsigned int)((v_rbx) | (1));
        result = v_stack_m1108;
    }
    if (v_stack_m1120 != 0) goto loc_0080B203;
    result = LOCK_ADDRESS_SPACE(result, v_stack_m10F8, a3, v_rsi + 48);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m10F8 + 500)))) & (32)) != 0) goto loc_0080B3B5;
loc_0080B203:
    result = MiBuildPhysicalPageFreeChain(v_stack_m1128, v_rsi, v_stack_m10C8, v_rsi + 48);
    v_stack_m1134 = (unsigned int)(result);
    v_stack_m10D8 = (unsigned int)(*(unsigned int *)(v_rsi + 44));
    a3 = 0;
    if ((unsigned int)(*(unsigned int *)(v_rsi + 44)) == 0) goto loc_0080B24D;
    result = (unsigned int)(*(unsigned int *)(v_rsi + 44));
    if (v_stack_m1120 == 0) {
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 44)));
        a2 = (a2) * (v_stack_m10E8);
        a1 = v_stack_m10F8;
        result = MiReturnProcessCommitment(a1, a2, a3, v_rsi + 48);
    }
loc_0080B24D:
    if (v_stack_m1120 == 0) {
        a2 = v_stack_m10F8;
        a1 = v_stack_m1108;
        result = UNLOCK_ADDRESS_SPACE(a1, a2, a3, v_rsi + 48);
        a3 = 0;
    }
    v_stack_m10E0 = (unsigned int)(*(unsigned int *)(v_rsi + 40));
    if ((unsigned int)(*(unsigned int *)(v_rsi + 40)) == 0) goto loc_0080B336;
    if (v_stack_m10E8 == 1) goto loc_0080B29B;
    result = MiFreePhysicalPageChain(v_stack_m1128, v_stack_m10C8, a3, v_rsi + 48);
    a3 = 0;
    goto loc_0080B336;
loc_0080B29B:
    result = (unsigned int)((result) << (12));
    *(unsigned int *)(v_rsi + 40) = (unsigned int)(result);
    result = MiPreparePhysicalPagesMdlForFree(v_rsi, 2 - 1, a3, v_rsi + 48);
    a3 = 0;
    a2 = 0;
    result = MiFreePagesFromMdl(v_rsi, a2, a3, v_stack_m1128);
    result = MiGetAweInfoPartition(v_stack_m1128, a2, a3, v_stack_m1128);
    result = -(v_stack_m10E0);
    a3 = 0;
    v_r13 = v_stack_m1120;
    if (v_stack_m1120 == 0) {
        a1 = v_stack_m1130;
        v_r13 = v_stack_m1120;
    }
    result = MiGetProcessPartition(v_stack_m10F8, a2, a3, v_stack_m10E0);
    if (result != result) {
        a2 = 4;
        a3 = a2 - 3;
        a1 = result;
        result = MiReturnCrossPartitionCharges(a1, a2, a3, v_stack_m10E0);
        a3 = 0;
    }
loc_0080B336:
    v_r12 = (v_stack_m1118) - (v_stack_m10D8);
    v_stack_m1118 = v_r12;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0080B3CD;
    if (v_r12 == 0) goto loc_0080B3CD;
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) {
        a2 = 0;
        a1 = v_stack_m10B0;
        result = KiUnstackDetachProcess(a1, a2, a3, v_stack_m10E0);
        v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFEULL));
        a3 = 0;
    }
    if ((*(unsigned __int64 *)(v_stack_m1130 + 784)) == 0) goto loc_0080B39D;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m1130 + 1772))) == 332) goto loc_0080B392;
    result = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m1130 + 1772))) == 452) {
        result = 1;
    }
    result = 4;
    if ((unsigned __int8)(result) == 0) {
        result = 8;
    }
    result = (result) * (v_r15);
    goto loc_0080B144;
loc_0080B3B5:
    result = UNLOCK_ADDRESS_SPACE(v_stack_m1108, v_stack_m1130, a3, v_stack_m10E0);
    v_stack_m1134 = (unsigned int)((unsigned int)(0xC000010AULL));
loc_0080B3CD:
loc_0080B3D2:
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) {
        a1 = v_rsi;
        result = IoFreeMdl(a1, v_stack_m1130, a3, v_stack_m10E0);
    }
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) {
        a2 = 0;
        a1 = v_stack_m10B0;
        result = KiUnstackDetachProcess(a1, a2, a3, v_stack_m10E0);
    }
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) goto loc_0080B413;
    if (v_r13 == 0) {
        a1 = v_stack_m1130;
    }
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x68506D4DULL), a3, v_stack_m10E0);
loc_0080B413:
    *(unsigned __int64 *)(v_stack_m1100) = v_stack_m10F0;
    goto loc_0080B422;
loc_0080B422:
    goto loc_0080B427;
loc_0080B427:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x68506D4DULL), a3, v_stack_m10E0);
    v_rsp = (v_rsp) + (0x1130ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtFreeUserPhysicalPages(int64_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1078;
    uint64_t v_stack_m1090;
    uint64_t v_stack_m10A0;
    uint64_t v_stack_m10B0;
    uint64_t v_stack_m10B8;
    uint64_t v_stack_m10C8;
    uint64_t v_stack_m10D8;
    uint64_t v_stack_m10E0;
    uint64_t v_stack_m10E8;
    uint64_t v_stack_m10F0;
    uint64_t v_stack_m10F8;
    uint64_t v_stack_m1100;
    uint64_t v_stack_m1108;
    uint64_t v_stack_m1110;
    uint64_t v_stack_m1118;
    uint64_t v_stack_m1120;
    uint64_t v_stack_m1128;
    uint64_t v_stack_m1130;
    uint32_t v_stack_m1134;
    uint8_t v_stack_m1138;
    uint64_t v_stack_m1148;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (0x1130ULL);
    result = (*(uint64_t *)(v_rip + 0x5FF7F6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1110 = Arg3;
    v_stack_m1100 = Arg2;
    v_stack_m10B0 = v_xmm0;
    v_stack_m10A0 = v_xmm0;
    v_stack_m1090 = v_xmm0;
    Arg2 = 0;
    result = memset(v_stack_m1078, Arg2, (uint32_t)(0x1030ULL), a4);
    Arg2 = 0;
    v_stack_m1130 = 0;
    v_stack_m1120 = 0;
    result = 0;
    v_stack_m10C8 = v_xmm0;
    v_stack_m10B8 = 0;
    v_stack_m1108 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m10F8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m1138 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_0080AFEA;
    v_stack_m1118 = *(uint64_t *)(arg2);
    goto loc_0080B010;
loc_0080AFEA:
    Arg1 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    if (0 < (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) { Arg1 = 0; }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    v_stack_m1118 = *(uint64_t *)(arg2);
    *(uint64_t *)(arg2) = 0;
loc_0080B010:
    if (*(uint64_t *)(arg2) != 0) goto loc_0080B01F;
    goto loc_0080B427;
loc_0080B01F:
    v_stack_m1128 = 0;
    v_stack_m1148 = v_stack_m1120;
    result = MiReferenceAweHandle(Arg1, 2, (uint8_t)((uint32_t)(0xC00000F0ULL)), v_stack_m1130);
    Arg3 = 0;
    if (sign_flag) goto loc_0080B427;
    if (v_stack_m1120 == 0) goto loc_0080B076;
    result = MiSectionControlArea(v_stack_m1120, 2, Arg3, v_stack_m1130);
    v_stack_m1128 = *(uint64_t *)(result + 0x8);
    goto loc_0080B083;
loc_0080B076:
    if (v_stack_m1130 != 0) goto loc_0080B08D;
loc_0080B083:
    v_stack_m1130 = v_stack_m10F8;
loc_0080B08D:
    v_stack_m10F0 = 0;
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_0080B0BF;
    v_stack_m1128 = *(uint64_t *)(*(uint64_t *)(v_stack_m10F8 + 0x410) + 0x448);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m10F8 + 0x410) + 0x448) != 0) goto loc_0080B0BF;
    v_stack_m1134 = (uint32_t)((uint32_t)(0xC00000EFULL));
    goto loc_0080B3D2;
loc_0080B0BF:
    result = MiGetAwePageSize((uint32_t)(0xC00000EFULL), 2, Arg3, v_stack_m1130);
    v_stack_m10E8 = result;
    if ((*(uint64_t *)(arg2)) <= 512) goto loc_0080B134;
    result = (uint32_t)(0xC0000ULL);
    if (result != 1) { result = (uint32_t)((uint32_t)(0xFFFFFULL)); }
    local_r15 = *(uint64_t *)(arg2);
    if ((*(uint64_t *)(arg2)) > result) { local_r15 = result; }
loc_0080B0FE:
    if (local_r15 <= 512) goto loc_0080B134;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) << (12));
    v_stack_m1148 = 0;
    a4 = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = IoAllocateMdl(Arg1, Arg2, Arg3, a4);
    Arg3 = 0;
    if (result != 0) goto loc_0080B131;
    local_r15 = (local_r15) >> (1);
    goto loc_0080B0FE;
loc_0080B131:
    local_rbx = (uint32_t)((v_stack_m1130 + 4) | (8));
loc_0080B134:
    local_rsi = result;
    if (result == 0) {
        local_rsi = v_stack_m1078;
        local_r15 = 512;
    }
    if (local_r15 > (*(uint64_t *)(arg2))) { local_r15 = *(uint64_t *)(arg2); }
    Arg1 = (local_r15) << (12);
    *(uint64_t *)(local_rsi) = 0;
    result = (Arg1 + 4095) >> (12);
    result = (uint16_t)((result) + (6));
    result = (uint16_t)((result) << (3));
    *(uint16_t *)(local_rsi + 0x8) = (uint16_t)(result);
    *(uint16_t *)(local_rsi + 0xA) = 0;
    *(uint64_t *)(local_rsi + 0x20) = 0;
    *(uint32_t *)(local_rsi + 0x2C) = 0;
    *(uint32_t *)(local_rsi + 0x28) = (uint32_t)(Arg1);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFEULL));
    if (v_stack_m1138 != 0) goto loc_0080B1A1;
    result = memcpy(local_rsi + 48, v_stack_m1110, local_r15 * 8, local_rsi + 48);
    goto loc_0080B1BD;
loc_0080B1A1:
    result = MiCaptureUlongPtrArray(local_rsi + 48, v_stack_m1110, local_r15, local_rsi + 48);
    v_stack_m1134 = (uint32_t)(result);
    if (sign_flag) goto loc_0080B3CD;
loc_0080B1BD:
    result = v_stack_m1108;
    if ((*(uint64_t *)(v_stack_m1108 + 0xB8)) != v_stack_m10F8) {
        Arg3 = v_stack_m10B0;
        Arg2 = 0;
        Arg1 = v_stack_m10F8;
        result = KiStackAttachProcess(Arg1, Arg2, Arg3, local_rsi + 48);
        local_rbx = (uint32_t)((local_rbx) | (1));
        result = v_stack_m1108;
    }
    if (v_stack_m1120 != 0) goto loc_0080B203;
    result = LOCK_ADDRESS_SPACE(result, v_stack_m10F8, Arg3, local_rsi + 48);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m10F8 + 0x1F4)))) & (32)) != 0) goto loc_0080B3B5;
loc_0080B203:
    result = MiBuildPhysicalPageFreeChain(v_stack_m1128, local_rsi, v_stack_m10C8, local_rsi + 48);
    v_stack_m1134 = (uint32_t)(result);
    v_stack_m10D8 = (uint32_t)(*(uint32_t *)(local_rsi + 0x2C));
    Arg3 = 0;
    if ((uint32_t)(*(uint32_t *)(local_rsi + 0x2C)) == 0) goto loc_0080B24D;
    result = (uint32_t)(*(uint32_t *)(local_rsi + 0x2C));
    if (v_stack_m1120 == 0) {
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x2C)));
        Arg2 = (Arg2) * (v_stack_m10E8);
        Arg1 = v_stack_m10F8;
        result = MiReturnProcessCommitment(Arg1, Arg2, Arg3, local_rsi + 48);
    }
loc_0080B24D:
    if (v_stack_m1120 == 0) {
        Arg2 = v_stack_m10F8;
        Arg1 = v_stack_m1108;
        result = UNLOCK_ADDRESS_SPACE(Arg1, Arg2, Arg3, local_rsi + 48);
        Arg3 = 0;
    }
    v_stack_m10E0 = (uint32_t)(*(uint32_t *)(local_rsi + 0x28));
    if ((uint32_t)(*(uint32_t *)(local_rsi + 0x28)) == 0) goto loc_0080B336;
    if (v_stack_m10E8 == 1) goto loc_0080B29B;
    result = MiFreePhysicalPageChain(v_stack_m1128, v_stack_m10C8, Arg3, local_rsi + 48);
    Arg3 = 0;
    goto loc_0080B336;
loc_0080B29B:
    result = (uint32_t)((result) << (12));
    *(uint32_t *)(local_rsi + 0x28) = (uint32_t)(result);
    result = MiPreparePhysicalPagesMdlForFree(local_rsi, 2 - 1, Arg3, local_rsi + 48);
    Arg3 = 0;
    Arg2 = 0;
    result = MiFreePagesFromMdl(local_rsi, Arg2, Arg3, v_stack_m1128);
    result = MiGetAweInfoPartition(v_stack_m1128, Arg2, Arg3, v_stack_m1128);
    result = -(v_stack_m10E0);
    Arg3 = 0;
    local_r13 = v_stack_m1120;
    if (v_stack_m1120 == 0) {
        Arg1 = v_stack_m1130;
        local_r13 = v_stack_m1120;
    }
    result = MiGetProcessPartition(v_stack_m10F8, Arg2, Arg3, v_stack_m10E0);
    if (result != result) {
        Arg2 = 4;
        Arg3 = Arg2 - 3;
        Arg1 = result;
        result = MiReturnCrossPartitionCharges(Arg1, Arg2, Arg3, v_stack_m10E0);
        Arg3 = 0;
    }
loc_0080B336:
    local_r12 = (v_stack_m1118) - (v_stack_m10D8);
    v_stack_m1118 = local_r12;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0080B3CD;
    if (local_r12 == 0) goto loc_0080B3CD;
    if ((((uint8_t)(local_rbx)) & (1)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m10B0;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, v_stack_m10E0);
        local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFEULL));
        Arg3 = 0;
    }
    if ((*(uint64_t *)(v_stack_m1130 + 0x310)) == 0) goto loc_0080B39D;
    if (((uint16_t)(*(uint16_t *)(v_stack_m1130 + 0x6EC))) == 332) goto loc_0080B392;
    result = 0;
    if (((uint16_t)(*(uint16_t *)(v_stack_m1130 + 0x6EC))) == 452) {
        result = 1;
    }
    result = 4;
    if ((uint8_t)(result) == 0) {
        result = 8;
    }
    result = (result) * (local_r15);
    goto loc_0080B144;
loc_0080B3B5:
    result = UNLOCK_ADDRESS_SPACE(v_stack_m1108, v_stack_m1130, Arg3, v_stack_m10E0);
    v_stack_m1134 = (uint32_t)((uint32_t)(0xC000010AULL));
loc_0080B3CD:
loc_0080B3D2:
    if ((((uint8_t)(local_rbx)) & (8)) != 0) {
        Arg1 = local_rsi;
        result = IoFreeMdl(Arg1, v_stack_m1130, Arg3, v_stack_m10E0);
    }
    if ((((uint8_t)(local_rbx)) & (1)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m10B0;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, v_stack_m10E0);
    }
    if ((((uint8_t)(local_rbx)) & (4)) != 0) goto loc_0080B413;
    if (local_r13 == 0) {
        Arg1 = v_stack_m1130;
    }
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x68506D4DULL), Arg3, v_stack_m10E0);
loc_0080B413:
    *(uint64_t *)(v_stack_m1100) = v_stack_m10F0;
    goto loc_0080B422;
loc_0080B422:
    goto loc_0080B427;
loc_0080B427:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x68506D4DULL), Arg3, v_stack_m10E0);
    local_rsp = (local_rsp) + (0x1130ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0080AF30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
