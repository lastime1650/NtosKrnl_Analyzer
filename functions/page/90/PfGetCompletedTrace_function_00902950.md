# PfGetCompletedTrace

- RVA: `0x00902950`–`0x00902E41` (길이 `1,265` bytes)
- VA: `0x0000000140902950`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00088878`
- 디코드: `288`개 명령, `1,265/1,265` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00902A13` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00902A99` → [PfpPartitionFindByHandle](PfpPartitionFindByHandle_function_00902E48.md) (function, `0x00902E48`)
- `0x00902AC4` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x00902B62` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00902B8E` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00902C01` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00902C51` → [PfTFreeTraceDump](../../text/4B/PfTFreeTraceDump_function_004B3550.md) (function, `0x004B3550`)
- `0x00902C75` → [PfpPartitionRundownProtectionRelease](../../text/47/PfpPartitionRundownProtectionRelease_function_0047BB54.md) (function, `0x0047BB54`)
- `0x00902C87` → [PfpPartitionDereferenceParent](../../text/34/PfpPartitionDereferenceParent_function_00341CDC.md) (function, `0x00341CDC`)
- `0x00902C99` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00902D01` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00902D10` → [PfFbBufferListFlushStandby](../../text/48/PfFbBufferListFlushStandby_function_00484174.md) (function, `0x00484174`)
- `0x00902D33` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x00902DE7` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00902E15` → [PfTAccessTracingStart](../../pagelk/B6/PfTAccessTracingStart_function_00B6B9F0.md) (function, `0x00B6B9F0`)
- `0x00902E26` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00902E37` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)

### Direct callers
- [PfQuerySuperfetchInformation](PfQuerySuperfetchInformation_function_0090210C.md) at `0x00902261`

### Static image references
- `0x00902962` → RVA `0x00E0A740` (`.data`; read)
- `0x009029CD` → RVA `0x00E074D8` (`.data`; read)
- `0x009029DA` → RVA `0x00E074E8` (`.data`; reference)
- `0x00902BB3` → RVA `0x00E671D8` (`.data`; read)
- `0x00902D61` → RVA `0x00E074F0` (`.data`; read)
- `0x00902DD9` → RVA `0x000489D9` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00902AC4` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x00902B62` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x00902C01` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00902C51` → [PfTFreeTraceDump](../../text/4B/PfTFreeTraceDump_function_004B3550.md) (`PAGE` → `.text`)
  - `0x00902C75` → [PfpPartitionRundownProtectionRelease](../../text/47/PfpPartitionRundownProtectionRelease_function_0047BB54.md) (`PAGE` → `.text`)
  - `0x00902C87` → [PfpPartitionDereferenceParent](../../text/34/PfpPartitionDereferenceParent_function_00341CDC.md) (`PAGE` → `.text`)
  - `0x00902C99` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00902D01` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x00902D10` → [PfFbBufferListFlushStandby](../../text/48/PfFbBufferListFlushStandby_function_00484174.md) (`PAGE` → `.text`)
  - `0x00902D33` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x00902DE7` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00902E15` → [PfTAccessTracingStart](../../pagelk/B6/PfTAccessTracingStart_function_00B6B9F0.md) (`PAGE` → `PAGELK`)
  - `0x00902E26` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00902E37` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00902CE8` → [sub_00B20874](../B2/Unknown_function_00B20874.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00902950  40 56                           push rsi
00902952  57                              push rdi
00902953  41 54                           push r12
00902955  41 55                           push r13
00902957  41 56                           push r14
00902959  41 57                           push r15
0090295B  48 81 EC 08 01 00 00            sub rsp, 0x108
00902962  48 8B 05 D7 7D 50 00            mov rax, qword ptr [rip + 0x507dd7]
00902969  48 33 C4                        xor rax, rsp
0090296C  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00902974  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
00902979  44 88 44 24 30                  mov byte ptr [rsp + 0x30], r8b
0090297E  8B F2                           mov esi, edx
00902980  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00902984  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00902989  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
0090298E  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
00902996  48 83 A4 24 80 00 00 00 00      and qword ptr [rsp + 0x80], 0
0090299F  33 C0                           xor eax, eax
009029A1  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
009029A5  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009029A9  33 FF                           xor edi, edi
009029AB  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
009029B0  45 33 ED                        xor r13d, r13d
009029B3  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
009029B8  45 33 F6                        xor r14d, r14d
009029BB  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
009029C0  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
009029C5  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
009029C9  44 8D 60 02                     lea r12d, [rax + 2]
009029CD  83 3D 04 4B 50 00 04            cmp dword ptr [rip + 0x504b04], 4
009029D4  0F 86 EE 02 00 00               jbe 0x140902cc8
009029DA  44 84 25 07 4B 50 00            test byte ptr [rip + 0x504b07], r12b
009029E1  0F 85 7A 03 00 00               jne 0x140902d61
009029E7  32 C0                           xor al, al
009029E9  41 BF 01 00 00 00               mov r15d, 1
009029EF  84 C0                           test al, al
009029F1  0F 85 CA 03 00 00               jne 0x140902dc1
009029F7  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009029FC  B8 18 00 00 00                  mov eax, 0x18
00902A01  3B F0                           cmp esi, eax
00902A03  0F 82 49 03 00 00               jb 0x140902d52
00902A09  45 84 C0                        test r8b, r8b
00902A0C  74 2E                           je 0x140902a3c
00902A0E  F6 C1 07                        test cl, 7
00902A11  74 06                           je 0x140902a19
00902A13  E8 B8 75 F9 FF                  call 0x140899fd0
00902A18  CC                              int3
00902A19  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00902A23  48 3B C8                        cmp rcx, rax
00902A26  48 0F 42 C1                     cmovb rax, rcx
00902A2A  90                              nop
00902A2B  8A 00                           mov al, byte ptr [rax]
00902A2D  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00902A32  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00902A37  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00902A3C  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00902A3F  0F 11 84 24 98 00 00 00         movups xmmword ptr [rsp + 0x98], xmm0
00902A47  F2 0F 10 49 10                  movsd xmm1, qword ptr [rcx + 0x10]
00902A4C  F2 0F 11 8C 24 A8 00 00 00      movsd qword ptr [rsp + 0xa8], xmm1
00902A55  EB 1B                           jmp 0x140902a72
00902A57  8B F0                           mov esi, eax
00902A59  41 BC 02 00 00 00               mov r12d, 2
00902A5F  45 8D 7C 24 FF                  lea r15d, [r12 - 1]
00902A64  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00902A68  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00902A6D  E9 EA 01 00 00                  jmp 0x140902c5c
00902A72  66 44 39 A4 24 98 00 00 00      cmp word ptr [rsp + 0x98], r12w
00902A7B  0F 85 C7 02 00 00               jne 0x140902d48
00902A81  45 8A C8                        mov r9b, r8b
00902A84  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
00902A8C  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
00902A94  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00902A99  E8 AA 03 00 00                  call 0x140902e48
00902A9E  8B F0                           mov esi, eax
00902AA0  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00902AA5  85 C0                           test eax, eax
00902AA7  0F 88 AB 01 00 00               js 0x140902c58
00902AAD  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
00902AB2  48 8D B7 70 02 00 00            lea rsi, [rdi + 0x270]
00902AB9  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
00902AC1  48 8B CE                        mov rcx, rsi
00902AC4  E8 D7 BA 90 FF                  call 0x14020e5a0
00902AC9  83 BF 68 02 00 00 00            cmp dword ptr [rdi + 0x268], 0
00902AD0  0F 85 21 02 00 00               jne 0x140902cf7
00902AD6  4C 8D 87 58 02 00 00            lea r8, [rdi + 0x258]
00902ADD  45 8B 08                        mov r9d, dword ptr [r8]
00902AE0  44 8B 97 5C 02 00 00            mov r10d, dword ptr [rdi + 0x25c]
00902AE7  33 D2                           xor edx, edx
00902AE9  41 3B D4                        cmp edx, r12d
00902AEC  73 68                           jae 0x140902b56
00902AEE  85 D2                           test edx, edx
00902AF0  0F 85 C3 01 00 00               jne 0x140902cb9
00902AF6  4C 8D B7 48 02 00 00            lea r14, [rdi + 0x248]
00902AFD  48 8D 8F 60 02 00 00            lea rcx, [rdi + 0x260]
00902B04  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00902B09  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00902B0E  49 8B 06                        mov rax, qword ptr [r14]
00902B11  49 3B C6                        cmp rax, r14
00902B14  0F 84 97 01 00 00               je 0x140902cb1
00902B1A  4C 8B E8                        mov r13, rax
00902B1D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00902B22  8B 50 18                        mov edx, dword ptr [rax + 0x18]
00902B25  83 C2 18                        add edx, 0x18
00902B28  89 54 24 3C                     mov dword ptr [rsp + 0x3c], edx
00902B2C  3B 54 24 38                     cmp edx, dword ptr [rsp + 0x38]
00902B30  0F 87 E4 01 00 00               ja 0x140902d1a
00902B36  48 8B 10                        mov rdx, qword ptr [rax]
00902B39  4C 39 70 08                     cmp qword ptr [rax + 8], r14
00902B3D  0F 85 FE 01 00 00               jne 0x140902d41
00902B43  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00902B47  0F 85 F4 01 00 00               jne 0x140902d41
00902B4D  49 89 16                        mov qword ptr [r14], rdx
00902B50  4C 89 72 08                     mov qword ptr [rdx + 8], r14
00902B54  FF 09                           dec dword ptr [rcx]
00902B56  45 3B CA                        cmp r9d, r10d
00902B59  0F 83 A1 02 00 00               jae 0x140902e00
00902B5F  48 8B CE                        mov rcx, rsi
00902B62  E8 59 EE 94 FF                  call 0x1402519c0
00902B67  33 F6                           xor esi, esi
00902B69  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
00902B6D  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00902B71  4D 85 ED                        test r13, r13
00902B74  0F 84 73 01 00 00               je 0x140902ced
00902B7A  40 38 74 24 30                  cmp byte ptr [rsp + 0x30], sil
00902B7F  74 12                           je 0x140902b93
00902B81  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
00902B85  44 8D 46 08                     lea r8d, [rsi + 8]
00902B89  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00902B8E  E8 2D 66 FE FF                  call 0x1408e91c0
00902B93  0F 57 C0                        xorps xmm0, xmm0
00902B96  33 C0                           xor eax, eax
00902B98  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00902B9D  0F 11 01                        movups xmmword ptr [rcx], xmm0
00902BA0  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00902BA4  C7 01 02 00 18 00               mov dword ptr [rcx], 0x180002
00902BAA  44 8D 48 18                     lea r9d, [rax + 0x18]
00902BAE  48 21 44 24 70                  and qword ptr [rsp + 0x70], rax
00902BB3  48 8B 05 1E 46 56 00            mov rax, qword ptr [rip + 0x56461e]
00902BBA  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00902BBF  48 BA 04 00 00 00 80 F7 FF FF   movabs rdx, 0xfffff78000000004
00902BC9  8B 12                           mov edx, dword ptr [rdx]
00902BCB  44 8B C0                        mov r8d, eax
00902BCE  4C 0F AF C2                     imul r8, rdx
00902BD2  49 C1 E8 18                     shr r8, 0x18
00902BD6  48 C1 E8 20                     shr rax, 0x20
00902BDA  48 0F AF C2                     imul rax, rdx
00902BDE  48 C1 E0 08                     shl rax, 8
00902BE2  4C 03 C0                        add r8, rax
00902BE5  4C 89 41 08                     mov qword ptr [rcx + 8], r8
00902BE9  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00902BF1  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00902BF5  90                              nop
00902BF6  49 03 C9                        add rcx, r9
00902BF9  45 8B 45 18                     mov r8d, dword ptr [r13 + 0x18]
00902BFD  49 8D 55 10                     lea rdx, [r13 + 0x10]
00902C01  E8 3A 3C DC FF                  call 0x1406c6840
00902C06  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
00902C0A  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00902C0F  EB 30                           jmp 0x140902c41
00902C11  8B F0                           mov esi, eax
00902C13  41 BC 02 00 00 00               mov r12d, 2
00902C19  45 8D 7C 24 FF                  lea r15d, [r12 - 1]
00902C1E  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
00902C23  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00902C27  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00902C2B  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00902C30  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
00902C34  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00902C39  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00902C41  85 F6                           test esi, esi
00902C43  0F 88 E2 00 00 00               js 0x140902d2b
00902C49  89 01                           mov dword ptr [rcx], eax
00902C4B  49 8B D5                        mov rdx, r13
00902C4E  48 8B CF                        mov rcx, rdi
00902C51  E8 FA 08 BB FF                  call 0x1404b3550
00902C56  33 F6                           xor esi, esi
00902C58  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00902C5C  85 C0                           test eax, eax
00902C5E  0F 85 CC 01 00 00               jne 0x140902e30
00902C64  83 3D 6D 48 50 00 04            cmp dword ptr [rip + 0x50486d], 4
00902C6B  77 66                           ja 0x140902cd3
00902C6D  48 85 FF                        test rdi, rdi
00902C70  74 08                           je 0x140902c7a
00902C72  48 8B CF                        mov rcx, rdi
00902C75  E8 DA 8E B7 FF                  call 0x14047bb54
00902C7A  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00902C82  48 85 C9                        test rcx, rcx
00902C85  74 05                           je 0x140902c8c
00902C87  E8 50 F0 A3 FF                  call 0x140341cdc
00902C8C  8B C6                           mov eax, esi
00902C8E  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00902C96  48 33 CC                        xor rcx, rsp
00902C99  E8 A2 99 DA FF                  call 0x1406ac640
00902C9E  48 81 C4 08 01 00 00            add rsp, 0x108
00902CA5  41 5F                           pop r15
00902CA7  41 5E                           pop r14
00902CA9  41 5D                           pop r13
00902CAB  41 5C                           pop r12
00902CAD  5F                              pop rdi
00902CAE  5E                              pop rsi
00902CAF  C3                              ret
00902CB0  CC                              int3
00902CB1  41 03 D7                        add edx, r15d
00902CB4  E9 30 FE FF FF                  jmp 0x140902ae9
00902CB9  4C 8D B7 38 02 00 00            lea r14, [rdi + 0x238]
00902CC0  49 8B C8                        mov rcx, r8
00902CC3  E9 3C FE FF FF                  jmp 0x140902b04
00902CC8  41 BF 01 00 00 00               mov r15d, 1
00902CCE  E9 29 FD FF FF                  jmp 0x1409029fc
00902CD3  44 84 25 0E 48 50 00            test byte ptr [rip + 0x50480e], r12b
00902CDA  0F 85 A6 00 00 00               jne 0x140902d86
00902CE0  45 32 FF                        xor r15b, r15b
00902CE3  45 84 FF                        test r15b, r15b
00902CE6  74 85                           je 0x140902c6d
00902CE8  E9 87 DB 21 00                  jmp 0x140b20874
00902CED  BE 1A 00 00 80                  mov esi, 0x8000001a
00902CF2  E9 61 FF FF FF                  jmp 0x140902c58
00902CF7  83 A7 68 02 00 00 00            and dword ptr [rdi + 0x268], 0
00902CFE  48 8B CE                        mov rcx, rsi
00902D01  E8 BA EC 94 FF                  call 0x1402519c0
00902D06  48 8D 97 20 01 00 00            lea rdx, [rdi + 0x120]
00902D0D  48 8B CF                        mov rcx, rdi
00902D10  E8 5F 14 B8 FF                  call 0x140484174
00902D15  E9 A7 FD FF FF                  jmp 0x140902ac1
00902D1A  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00902D1F  89 11                           mov dword ptr [rcx], edx
00902D21  BE 23 00 00 C0                  mov esi, 0xc0000023
00902D26  E9 2D FF FF FF                  jmp 0x140902c58
00902D2B  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00902D33  E8 68 B8 90 FF                  call 0x14020e5a0
00902D38  49 8B 06                        mov rax, qword ptr [r14]
00902D3B  4C 39 70 08                     cmp qword ptr [rax + 8], r14
00902D3F  74 61                           je 0x140902da2
00902D41  B9 03 00 00 00                  mov ecx, 3
00902D46  CD 29                           int 0x29
00902D48  BE 59 00 00 C0                  mov esi, 0xc0000059
00902D4D  E9 06 FF FF FF                  jmp 0x140902c58
00902D52  41 89 01                        mov dword ptr [r9], eax
00902D55  BE 23 00 00 C0                  mov esi, 0xc0000023
00902D5A  8B C7                           mov eax, edi
00902D5C  E9 FB FE FF FF                  jmp 0x140902c5c
00902D61  48 8B 05 88 47 50 00            mov rax, qword ptr [rip + 0x504788]
00902D68  49 23 C4                        and rax, r12
00902D6B  48 3B 05 7E 47 50 00            cmp rax, qword ptr [rip + 0x50477e]
00902D72  0F 85 6F FC FF FF               jne 0x1409029e7
00902D78  41 BF 01 00 00 00               mov r15d, 1
00902D7E  41 8A C7                        mov al, r15b
00902D81  E9 69 FC FF FF                  jmp 0x1409029ef
00902D86  48 8B 05 63 47 50 00            mov rax, qword ptr [rip + 0x504763]
00902D8D  49 23 C4                        and rax, r12
00902D90  48 3B 05 59 47 50 00            cmp rax, qword ptr [rip + 0x504759]
00902D97  0F 85 43 FF FF FF               jne 0x140902ce0
00902D9D  E9 41 FF FF FF                  jmp 0x140902ce3
00902DA2  49 89 45 00                     mov qword ptr [r13], rax
00902DA6  4D 89 75 08                     mov qword ptr [r13 + 8], r14
00902DAA  4C 89 68 08                     mov qword ptr [rax + 8], r13
00902DAE  4D 89 2E                        mov qword ptr [r14], r13
00902DB1  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00902DB6  44 01 38                        add dword ptr [rax], r15d
00902DB9  41 8B C7                        mov eax, r15d
00902DBC  E9 9B FE FF FF                  jmp 0x140902c5c
00902DC1  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
00902DC9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00902DCE  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00902DD3  45 33 C9                        xor r9d, r9d
00902DD6  45 33 C0                        xor r8d, r8d
00902DD9  48 8D 15 F9 5B 74 FF            lea rdx, [rip - 0x8ba407]
00902DE0  48 8D 0D F1 46 50 00            lea rcx, [rip + 0x5046f1]
00902DE7  E8 F4 32 B2 FF                  call 0x1404260e0
00902DEC  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00902DF1  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
00902DF6  44 8A 44 24 30                  mov r8b, byte ptr [rsp + 0x30]
00902DFB  E9 FC FB FF FF                  jmp 0x1409029fc
00902E00  8B 87 5C 02 00 00               mov eax, dword ptr [rdi + 0x25c]
00902E06  41 39 00                        cmp dword ptr [r8], eax
00902E09  0F 83 50 FD FF FF               jae 0x140902b5f
00902E0F  41 8B D4                        mov edx, r12d
00902E12  48 8B CF                        mov rcx, rdi
00902E15  E8 D6 8B 26 00                  call 0x140b6b9f0
00902E1A  48 8D 8F E0 02 00 00            lea rcx, [rdi + 0x2e0]
00902E21  45 33 C0                        xor r8d, r8d
00902E24  33 D2                           xor edx, edx
00902E26  E8 E5 C4 A3 FF                  call 0x14033f310
00902E2B  E9 2F FD FF FF                  jmp 0x140902b5f
00902E30  48 8D 8F 70 02 00 00            lea rcx, [rdi + 0x270]
00902E37  E8 84 EB 94 FF                  call 0x1402519c0
00902E3C  E9 23 FE FF FF                  jmp 0x140902c64
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfGetCompletedTrace(__int64 a1, int a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned __int8 v_stack_m108;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pB0;

    v_rsp = (v_rsp) - (264);
    result = (*(unsigned __int64 *)(v_rip + 5275095)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mE8 = a4;
    v_stack_m108 = a3;
    v_stack_m100 = a2;
    v_stack_mE0 = a1;
    v_stack_mC8 = a1;
    v_stack_mB0 = a4;
    result = 0;
    v_stack_m104 = 0;
    v_stack_mF8 = 0;
    v_rdi = 0;
    v_stack_mF0 = 0;
    v_r13 = 0;
    v_stack_mC0 = 0;
    v_r14 = 0;
    v_stack_mD8 = 0;
    v_stack_mD0 = 0;
    v_stack_mFC = 0;
    if ((*(unsigned int *)(v_rip + 5262084)) <= 4) goto loc_00902CC8;
    if (((*(unsigned __int8 *)(v_rip + 5262087)) & ((unsigned __int8)(result + 2))) != 0) goto loc_00902D61;
loc_009029E7:
    result = 0;
loc_009029EF:
    if (0 != 0) goto loc_00902DC1;
loc_009029FC:
    if (((unsigned int)((unsigned int)(a2))) < 24) goto loc_00902D52;
    if (a3 == 0) goto loc_00902A3C;
    result = 24;
    if ((((unsigned __int8)(v_stack_mE0)) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_mE0, a2, a3, a4);
    }
    if (v_stack_mE0 < result) { result = v_stack_mE0; }
    v_stack_mE0 = v_stack_mC8;
loc_00902A3C:
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm1;
    goto loc_00902A72;
loc_00902A72:
    if (v_stack_mA0 != ((unsigned __int16)(result + 2))) goto loc_00902D48;
    result = PfpPartitionFindByHandle(v_stack_mF0, v_stack_mB8, v_stack_m90, a3);
    if (sign_flag) goto loc_00902C58;
    v_stack_m104 = 1;
    v_stack_mA8 = v_stack_mF0 + 624;
loc_00902AC1:
    result = ExAcquireFastMutex(v_stack_mF0 + 624, v_stack_mB8, v_stack_m90, a3);
    if ((*(unsigned int *)(v_stack_mF0 + 616)) != 0) goto loc_00902CF7;
    a2 = 0;
loc_00902AE9:
    if (0 >= ((unsigned int)(result + 2))) goto loc_00902B56;
    if (0 != 0) goto loc_00902CB9;
loc_00902B04:
    v_stack_mD0 = v_stack_mF0 + 608;
    v_stack_mD8 = v_stack_mF0 + 584;
    if ((*(unsigned __int64 *)(v_stack_mF0 + 584)) == (v_stack_mF0 + 584)) goto loc_00902CB1;
    v_stack_mC0 = *(unsigned __int64 *)(v_stack_mF0 + 584);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 24))) + (24));
    v_stack_mFC = a2;
    if (a2 > v_stack_m100) goto loc_00902D1A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 8)) != (v_stack_mF0 + 584)) goto loc_00902D41;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 584)) + 8)) != (*(unsigned __int64 *)(v_stack_mF0 + 584))) goto loc_00902D41;
    *(unsigned __int64 *)(v_stack_mF0 + 584) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 584));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 584)) + 8) = v_stack_mF0 + 584;
loc_00902B56:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 600)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 604))))) goto loc_00902E00;
loc_00902B5F:
    result = ExReleaseFastMutex(v_stack_mF0 + 624, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 584)), v_stack_mF0 + 600, (unsigned int)(*(unsigned int *)(v_stack_mF0 + 600)));
    v_rsi = 0;
    v_stack_m104 = 0;
    v_stack_mF8 = 0;
    if (*(unsigned __int64 *)(v_stack_mF0 + 584) == 0) goto loc_00902CED;
    if (v_stack_m108 != 0) {
        a2 = v_stack_m100;
        a3 = v_rsi + 8;
        a1 = v_stack_mE0;
        result = ProbeForWrite(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_mF0 + 600)));
    }
    result = 0;
    *(unsigned __int64 *)(v_stack_mE0) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mE0 + 16) = 0;
    *(unsigned int *)(v_stack_mE0) = 0x180002ULL;
    v_stack_mC8 = *(unsigned __int64 *)(v_rip + 5654046);
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 5654046)))) * ((unsigned int)(*(unsigned int *)(a2)));
    a3 = (a3) >> (24);
    result = (*(unsigned __int64 *)(v_rip + 5654046)) >> (32);
    result = (result) * ((unsigned int)(*(unsigned int *)(a2)));
    result = (result) << (8);
    a3 = (a3) + (result);
    *(unsigned __int64 *)(v_stack_mE0 + 8) = a3;
    *(unsigned __int64 *)(v_stack_mE0 + 16) = v_stack_m90;
    a1 = (v_stack_mE0) + (result + 24);
    result = memcpy(a1, *(unsigned __int64 *)(v_stack_mF0 + 584) + 16, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 24)), result + 24);
    goto loc_00902C41;
loc_00902C41:
    if (sign_flag) goto loc_00902D2B;
    *(unsigned int *)(v_stack_mE8) = (unsigned int)((unsigned int)(v_stack_mFC));
    result = PfTFreeTraceDump(v_stack_mF0, *(unsigned __int64 *)(v_stack_mF0 + 584), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 24)), result + 24);
    v_rsi = 0;
loc_00902C58:
loc_00902C5C:
    if ((unsigned int)((unsigned int)(v_stack_m104)) != 0) goto loc_00902E30;
loc_00902C64:
    if ((*(unsigned int *)(v_rip + 5261421)) > 4) goto loc_00902CD3;
loc_00902C6D:
    result = (unsigned int)(v_stack_m104);
    if (v_stack_mF0 != 0) {
        a1 = v_stack_mF0;
        result = PfpPartitionRundownProtectionRelease(a1, *(unsigned __int64 *)(v_stack_mF0 + 584), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 24)), result + 24);
    }
    if (v_stack_mB8 != 0) {
        result = PfpPartitionDereferenceParent(v_stack_mB8, *(unsigned __int64 *)(v_stack_mF0 + 584), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 24)), result + 24);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(v_stack_mF0 + 584), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 24)), result + 24);
    v_rsp = (v_rsp) + (264);
    return result;
loc_00902CB1:
    a2 = (unsigned int)((*(unsigned __int64 *)(v_stack_mF0 + 584)) + (1));
    goto loc_00902AE9;
loc_00902CB9:
    goto loc_00902B04;
loc_00902CC8:
    goto loc_009029FC;
loc_00902CD3:
    if (((*(unsigned __int8 *)(v_rip + 5261326)) & ((unsigned __int8)(result + 2))) != 0) goto loc_00902D86;
loc_00902CE0:
    v_r15 = 0;
loc_00902CE3:
    if (0 == 0) goto loc_00902C6D;
loc_00902CED:
    goto loc_00902C58;
loc_00902CF7:
    result = ExReleaseFastMutex((unsigned int)(0x8000001AULL), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 24)), result + 24);
    result = PfFbBufferListFlushStandby(v_stack_mF0, v_stack_mF0 + 288, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 24)), result + 24);
    goto loc_00902AC1;
loc_00902D1A:
    *(unsigned int *)(v_stack_p50) = (unsigned int)(v_stack_mF0 + 288);
    goto loc_00902C58;
loc_00902D2B:
    result = ExAcquireFastMutex(v_stack_p90, v_stack_mF0 + 288, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 24)), result + 24);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 568) + 8)) == (v_stack_mF0 + 568)) goto loc_00902DA2;
loc_00902D41:
loc_00902D48:
    goto loc_00902C58;
loc_00902D52:
    *(unsigned int *)(result + 24) = (unsigned int)(*(unsigned __int64 *)(v_stack_mF0 + 568));
    goto loc_00902C5C;
loc_00902D61:
    result = (*(unsigned __int64 *)(v_rip + 5261192)) & (result + 2);
    if (result != (*(unsigned __int64 *)(v_rip + 5261182))) goto loc_009029E7;
    goto loc_009029EF;
loc_00902D86:
    result = (*(unsigned __int64 *)(v_rip + 5261155)) & (result + 2);
    if (result != (*(unsigned __int64 *)(v_rip + 5261145))) goto loc_00902CE0;
    goto loc_00902CE3;
loc_00902DA2:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 584)) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 584) + 8) = v_stack_mF0 + 568;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_stack_mF0 + 584);
    *(unsigned __int64 *)(v_stack_mF0 + 568) = *(unsigned __int64 *)(v_stack_mF0 + 584);
    goto loc_00902C5C;
loc_00902DC1:
    v_stack_p28 = v_stack_pB0;
    v_stack_p20 = (unsigned int)(result + 2);
    a4 = 0;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 5261041, v_rip - 9151495, a3, a4);
    goto loc_009029FC;
loc_00902E00:
    if ((*(unsigned int *)(v_stack_p30)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 604))))) goto loc_00902B5F;
    result = PfTAccessTracingStart(v_stack_mF0, (unsigned int)((unsigned int)(result + 2)), v_stack_p30, v_stack_p50);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_stack_mF0 + 736, a2, a3, v_stack_p50);
    goto loc_00902B5F;
loc_00902E30:
    result = ExReleaseFastMutex(v_stack_mF0 + 624, a2, a3, v_stack_p50);
    goto loc_00902C64;
}
```

## 5. (Beta) C Style

```c
int64_t PfGetCompletedTrace(int64_t Arg1, int32_t Arg2, uint8_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint8_t v_stack_m108;
    uint64_t v_stack_m48;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p90;
    uint64_t v_stack_pB0;

    local_rsp = (local_rsp) - (264);
    result = (*(uint64_t *)(v_rip + 0x507DD7)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mE8 = Arg4;
    v_stack_m108 = Arg3;
    v_stack_m100 = Arg2;
    v_stack_mE0 = Arg1;
    v_stack_mC8 = Arg1;
    v_stack_mB0 = Arg4;
    result = 0;
    v_stack_m104 = 0;
    v_stack_mF8 = 0;
    local_rdi = 0;
    v_stack_mF0 = 0;
    local_r13 = 0;
    v_stack_mC0 = 0;
    local_r14 = 0;
    v_stack_mD8 = 0;
    v_stack_mD0 = 0;
    v_stack_mFC = 0;
    if ((*(uint32_t *)(v_rip + 0x504B04)) <= 4) goto loc_00902CC8;
    if (((*(uint8_t *)(v_rip + 0x504B07)) & ((uint8_t)(result + 2))) != 0) goto loc_00902D61;
loc_009029E7:
    result = 0;
loc_009029EF:
    if (0 != 0) goto loc_00902DC1;
loc_009029FC:
    if (((uint32_t)((uint32_t)(Arg2))) < 24) goto loc_00902D52;
    if (Arg3 == 0) goto loc_00902A3C;
    result = 24;
    if ((((uint8_t)(v_stack_mE0)) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_mE0, Arg2, Arg3, Arg4);
    }
    if (v_stack_mE0 < result) { result = v_stack_mE0; }
    v_stack_mE0 = v_stack_mC8;
loc_00902A3C:
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm1;
    goto loc_00902A72;
loc_00902A72:
    if (v_stack_mA0 != ((uint16_t)(result + 2))) goto loc_00902D48;
    result = PfpPartitionFindByHandle(v_stack_mF0, v_stack_mB8, v_stack_m90, Arg3);
    if (sign_flag) goto loc_00902C58;
    v_stack_m104 = 1;
    v_stack_mA8 = v_stack_mF0 + 624;
loc_00902AC1:
    result = ExAcquireFastMutex(v_stack_mF0 + 624, v_stack_mB8, v_stack_m90, Arg3);
    if ((*(uint32_t *)(v_stack_mF0 + 0x268)) != 0) goto loc_00902CF7;
    Arg2 = 0;
loc_00902AE9:
    if (0 >= ((uint32_t)(result + 2))) goto loc_00902B56;
    if (0 != 0) goto loc_00902CB9;
loc_00902B04:
    v_stack_mD0 = v_stack_mF0 + 608;
    v_stack_mD8 = v_stack_mF0 + 584;
    if ((*(uint64_t *)(v_stack_mF0 + 0x248)) == (v_stack_mF0 + 584)) goto loc_00902CB1;
    v_stack_mC0 = *(uint64_t *)(v_stack_mF0 + 0x248);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x18))) + (24));
    v_stack_mFC = Arg2;
    if (Arg2 > v_stack_m100) goto loc_00902D1A;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x8)) != (v_stack_mF0 + 584)) goto loc_00902D41;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x248)) + 0x8)) != (*(uint64_t *)(v_stack_mF0 + 0x248))) goto loc_00902D41;
    *(uint64_t *)(v_stack_mF0 + 0x248) = *(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x248));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x248)) + 0x8) = v_stack_mF0 + 584;
loc_00902B56:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x258)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x25C))))) goto loc_00902E00;
loc_00902B5F:
    result = ExReleaseFastMutex(v_stack_mF0 + 624, *(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x248)), v_stack_mF0 + 600, (uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x258)));
    local_rsi = 0;
    v_stack_m104 = 0;
    v_stack_mF8 = 0;
    if (*(uint64_t *)(v_stack_mF0 + 0x248) == 0) goto loc_00902CED;
    if (v_stack_m108 != 0) {
        Arg2 = v_stack_m100;
        Arg3 = local_rsi + 8;
        Arg1 = v_stack_mE0;
        result = ProbeForWrite(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x258)));
    }
    result = 0;
    *(uint64_t *)(v_stack_mE0) = v_xmm0;
    *(uint64_t *)(v_stack_mE0 + 0x10) = 0;
    *(uint32_t *)(v_stack_mE0) = 0x180002ULL;
    v_stack_mC8 = *(uint64_t *)(v_rip + 0x56461E);
    Arg3 = ((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x56461E)))) * ((uint32_t)(*(uint32_t *)(Arg2)));
    Arg3 = (Arg3) >> (24);
    result = (*(uint64_t *)(v_rip + 0x56461E)) >> (32);
    result = (result) * ((uint32_t)(*(uint32_t *)(Arg2)));
    result = (result) << (8);
    Arg3 = (Arg3) + (result);
    *(uint64_t *)(v_stack_mE0 + 0x8) = Arg3;
    *(uint64_t *)(v_stack_mE0 + 0x10) = v_stack_m90;
    Arg1 = (v_stack_mE0) + (result + 24);
    result = memcpy(Arg1, *(uint64_t *)(v_stack_mF0 + 0x248) + 16, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x18)), result + 24);
    goto loc_00902C41;
loc_00902C41:
    if (sign_flag) goto loc_00902D2B;
    *(uint32_t *)(v_stack_mE8) = (uint32_t)((uint32_t)(v_stack_mFC));
    result = PfTFreeTraceDump(v_stack_mF0, *(uint64_t *)(v_stack_mF0 + 0x248), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x18)), result + 24);
    local_rsi = 0;
loc_00902C58:
loc_00902C5C:
    if ((uint32_t)((uint32_t)(v_stack_m104)) != 0) goto loc_00902E30;
loc_00902C64:
    if ((*(uint32_t *)(v_rip + 0x50486D)) > 4) goto loc_00902CD3;
loc_00902C6D:
    result = (uint32_t)(v_stack_m104);
    if (v_stack_mF0 != 0) {
        Arg1 = v_stack_mF0;
        result = PfpPartitionRundownProtectionRelease(Arg1, *(uint64_t *)(v_stack_mF0 + 0x248), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x18)), result + 24);
    }
    if (v_stack_mB8 != 0) {
        result = PfpPartitionDereferenceParent(v_stack_mB8, *(uint64_t *)(v_stack_mF0 + 0x248), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x18)), result + 24);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(v_stack_mF0 + 0x248), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x18)), result + 24);
    local_rsp = (local_rsp) + (264);
    return result;
loc_00902CB1:
    Arg2 = (uint32_t)((*(uint64_t *)(v_stack_mF0 + 0x248)) + (1));
    goto loc_00902AE9;
loc_00902CB9:
    goto loc_00902B04;
loc_00902CC8:
    goto loc_009029FC;
loc_00902CD3:
    if (((*(uint8_t *)(v_rip + 0x50480E)) & ((uint8_t)(result + 2))) != 0) goto loc_00902D86;
loc_00902CE0:
    local_r15 = 0;
loc_00902CE3:
    if (0 == 0) goto loc_00902C6D;
loc_00902CED:
    goto loc_00902C58;
loc_00902CF7:
    result = ExReleaseFastMutex((uint32_t)(0x8000001AULL), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x18)), result + 24);
    result = PfFbBufferListFlushStandby(v_stack_mF0, v_stack_mF0 + 288, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x18)), result + 24);
    goto loc_00902AC1;
loc_00902D1A:
    *(uint32_t *)(v_stack_p50) = (uint32_t)(v_stack_mF0 + 288);
    goto loc_00902C58;
loc_00902D2B:
    result = ExAcquireFastMutex(v_stack_p90, v_stack_mF0 + 288, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x18)), result + 24);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x238) + 0x8)) == (v_stack_mF0 + 568)) goto loc_00902DA2;
loc_00902D41:
loc_00902D48:
    goto loc_00902C58;
loc_00902D52:
    *(uint32_t *)(result + 0x18) = (uint32_t)(*(uint64_t *)(v_stack_mF0 + 0x238));
    goto loc_00902C5C;
loc_00902D61:
    result = (*(uint64_t *)(v_rip + 0x504788)) & (result + 2);
    if (result != (*(uint64_t *)(v_rip + 0x50477E))) goto loc_009029E7;
    goto loc_009029EF;
loc_00902D86:
    result = (*(uint64_t *)(v_rip + 0x504763)) & (result + 2);
    if (result != (*(uint64_t *)(v_rip + 0x504759))) goto loc_00902CE0;
    goto loc_00902CE3;
loc_00902DA2:
    *(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x248)) = result;
    *(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x248) + 0x8) = v_stack_mF0 + 568;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_stack_mF0 + 0x248);
    *(uint64_t *)(v_stack_mF0 + 0x238) = *(uint64_t *)(v_stack_mF0 + 0x248);
    goto loc_00902C5C;
loc_00902DC1:
    v_stack_p28 = v_stack_pB0;
    v_stack_p20 = (uint32_t)(result + 2);
    Arg4 = 0;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 5261041, v_rip - 9151495, Arg3, Arg4);
    goto loc_009029FC;
loc_00902E00:
    if ((*(uint32_t *)(v_stack_p30)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x25C))))) goto loc_00902B5F;
    result = PfTAccessTracingStart(v_stack_mF0, (uint32_t)((uint32_t)(result + 2)), v_stack_p30, v_stack_p50);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_stack_mF0 + 736, Arg2, Arg3, v_stack_p50);
    goto loc_00902B5F;
loc_00902E30:
    result = ExReleaseFastMutex(v_stack_mF0 + 624, Arg2, Arg3, v_stack_p50);
    goto loc_00902C64;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00902950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
