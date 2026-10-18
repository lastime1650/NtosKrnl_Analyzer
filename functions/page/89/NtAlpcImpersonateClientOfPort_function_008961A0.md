# NtAlpcImpersonateClientOfPort

- RVA: `0x008961A0`–`0x0089680E` (길이 `1,646` bytes)
- VA: `0x00000001408961A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007E1A8`
- 디코드: `384`개 명령, `1,646/1,646` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00896225` → [ExRaiseDatatypeMisalignment](ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0089630C` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0089637D` → [ExpLookupHandleTableEntry](../86/ExpLookupHandleTableEntry_function_00869DB0.md) (function, `0x00869DB0`)
- `0x008963BA` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x0089641C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00896438` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0089647E` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x008964F7` → [AlpcpImpersonateMessage](AlpcpImpersonateMessage_function_00896820.md) (function, `0x00896820`)
- `0x00896501` → [AlpcpUnlockMessage](AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0089650E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089651B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00896529` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00896559` → [ExpBlockOnLockedHandleEntry](../86/ExpBlockOnLockedHandleEntry_function_00868838.md) (function, `0x00868838`)
- `0x00896578` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x00896591` → [ExHandleLogBadReference](../../text/44/ExHandleLogBadReference_function_00440580.md) (function, `0x00440580`)
- `0x008965CA` → [AlpcpUnlockMessage](AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00896607` → [AlpcReferenceBlobByHandle](../88/AlpcReferenceBlobByHandle_function_00889F00.md) (function, `0x00889F00`)
- `0x0089661F` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x00896666` → [ExUnlockHandleTableEntry](../94/ExUnlockHandleTableEntry_function_0094D2D0.md) (function, `0x0094D2D0`)
- `0x0089668D` → [AlpcpUnlockMessage](AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x008966B7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008966CA` → [AlpcpReferenceConnectedPort](../9C/AlpcpReferenceConnectedPort_function_009CB030.md) (function, `0x009CB030`)
- `0x008966F4` → [AlpcpUnlockMessage](AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x008966FF` → [AlpcpDereferenceBlobEx](../88/AlpcpDereferenceBlobEx_function_0088AF00.md) (function, `0x0088AF00`)
- `0x00896768` → [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) (function, `0x008CBE10`)
- `0x008967BA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [NtImpersonateClientOfPort](../AB/NtImpersonateClientOfPort_function_00ABD230.md) at `0x00ABD237`

### Static image references
- `0x008962E1` → RVA `0x00FC6C18` (`ALMOSTRO`; read)
- `0x00896342` → RVA `0x00FC6F68` (`ALMOSTRO`; read)
- `0x00896600` → RVA `0x000014D8` (`.rdata`; read)
- `0x00896643` → RVA `0x00FCF300` (`CACHEALI`; read/write)
- `0x0089677E` → RVA `0x00FC5130` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x008963BA` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x0089641C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00896438` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0089647E` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x0089650E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089651B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00896529` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00896578` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x00896591` → [ExHandleLogBadReference](../../text/44/ExHandleLogBadReference_function_00440580.md) (`PAGE` → `.text`)
  - `0x008966B7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008967BA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008967FE` → [sub_00B197C2](../B1/Unknown_function_00B197C2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008961A0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008961A5  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
008961AA  57                              push rdi
008961AB  41 54                           push r12
008961AD  41 55                           push r13
008961AF  41 56                           push r14
008961B1  41 57                           push r15
008961B3  48 81 EC B0 00 00 00            sub rsp, 0xb0
008961BA  4C 8B D1                        mov r10, rcx
008961BD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008961C6  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008961CD  90                              nop
008961CE  45 33 ED                        xor r13d, r13d
008961D1  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
008961D6  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
008961DB  45 8B F5                        mov r14d, r13d
008961DE  4C 89 AC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r13
008961E6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008961EF  44 0F B6 98 32 02 00 00         movzx r11d, byte ptr [rax + 0x232]
008961F7  48 85 D2                        test rdx, rdx
008961FA  0F 84 9B 03 00 00               je 0x14089659b
00896200  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00896209  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00896211  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
00896218  4C 8B CA                        mov r9, rdx
0089621B  84 C9                           test cl, cl
0089621D  74 5A                           je 0x140896279
0089621F  41 83 E1 03                     and r9d, 3
00896223  74 3A                           je 0x14089625f
00896225  E8 A6 3D 00 00                  call 0x140899fd0
0089622A  CC                              int3
0089622B  66 0F BA 62 04 0C               bt word ptr [rdx + 4], 0xc
00896231  72 20                           jb 0x140896253
00896233  84 C9                           test cl, cl
00896235  74 10                           je 0x140896247
00896237  4D 85 C9                        test r9, r9
0089623A  75 E9                           jne 0x140896225
0089623C  48 3B D3                        cmp rdx, rbx
0089623F  48 0F 42 DA                     cmovb rbx, rdx
00896243  90                              nop
00896244  0F B6 03                        movzx eax, byte ptr [rbx]
00896247  8B 5A 18                        mov ebx, dword ptr [rdx + 0x18]
0089624A  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
0089624E  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
00896251  EB 36                           jmp 0x140896289
00896253  8B 5A 10                        mov ebx, dword ptr [rdx + 0x10]
00896256  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
0089625A  8B 42 14                        mov eax, dword ptr [rdx + 0x14]
0089625D  EB 2A                           jmp 0x140896289
0089625F  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00896269  48 8B C3                        mov rax, rbx
0089626C  48 3B D3                        cmp rdx, rbx
0089626F  48 0F 42 C2                     cmovb rax, rdx
00896273  90                              nop
00896274  0F B6 00                        movzx eax, byte ptr [rax]
00896277  EB B2                           jmp 0x14089622b
00896279  41 83 E1 03                     and r9d, 3
0089627D  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00896287  EB A2                           jmp 0x14089622b
00896289  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0089628D  EB 12                           jmp 0x1408962a1
0089628F  8B F0                           mov esi, eax
00896291  4C 8B B4 24 E8 00 00 00         mov r14, qword ptr [rsp + 0xe8]
00896299  4D 8B EE                        mov r13, r14
0089629C  E9 65 02 00 00                  jmp 0x140896506
008962A1  85 DB                           test ebx, ebx
008962A3  0F 84 CC 03 00 00               je 0x140896675
008962A9  4D 8B E0                        mov r12, r8
008962AC  49 C1 EC 02                     shr r12, 2
008962B0  41 83 FC 03                     cmp r12d, 3
008962B4  0F 87 BB 03 00 00               ja 0x140896675
008962BA  49 8B C0                        mov rax, r8
008962BD  83 E0 01                        and eax, 1
008962C0  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008962C5  42 8D 3C A5 00 00 00 00         lea edi, [r12*4]
008962CD  48 83 CF 02                     or rdi, 2
008962D1  49 23 F8                        and rdi, r8
008962D4  41 8B C5                        mov eax, r13d
008962D7  0F 95 C0                        setne al
008962DA  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
008962E1  4C 8B 05 30 09 73 00            mov r8, qword ptr [rip + 0x730930]
008962E8  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
008962ED  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
008962F2  48 8D 44 24 38                  lea rax, [rsp + 0x38]
008962F7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008962FC  45 0F B6 CB                     movzx r9d, r11b
00896300  41 BF 01 00 00 00               mov r15d, 1
00896306  41 8B D7                        mov edx, r15d
00896309  49 8B CA                        mov rcx, r10
0089630C  E8 9F 2A FD FF                  call 0x140868db0
00896311  8B F0                           mov esi, eax
00896313  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00896318  4C 89 B4 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r14
00896320  85 C0                           test eax, eax
00896322  0F 88 DE 01 00 00               js 0x140896506
00896328  85 DB                           test ebx, ebx
0089632A  0F 84 97 03 00 00               je 0x1408966c7
00896330  0F 88 AB 02 00 00               js 0x1408965e1
00896336  F7 C3 00 00 00 FC               test ebx, 0xfc000000
0089633C  0F 85 3C 04 00 00               jne 0x14089677e
00896342  4C 8B 3D 1F 0C 73 00            mov r15, qword ptr [rip + 0x730c1f]
00896349  4D 85 FF                        test r15, r15
0089634C  0F 84 6E 04 00 00               je 0x1408967c0
00896352  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089635B  0F B6 B0 32 02 00 00            movzx esi, byte ptr [rax + 0x232]
00896362  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
00896366  81 E7 FF FF FF 03               and edi, 0x3ffffff
0089636C  F7 C7 FC 03 00 00               test edi, 0x3fc
00896372  0F 84 0C 02 00 00               je 0x140896584
00896378  8B D7                           mov edx, edi
0089637A  49 8B CF                        mov rcx, r15
0089637D  E8 2E 3A FD FF                  call 0x140869db0
00896382  48 8B D8                        mov rbx, rax
00896385  48 85 C0                        test rax, rax
00896388  0F 84 F6 01 00 00               je 0x140896584
0089638E  66 90                           nop
00896390  0F 0D 0B                        prefetchw byte ptr [rbx]
00896393  4C 8B 03                        mov r8, qword ptr [rbx]
00896396  41 F6 C0 01                     test r8b, 1
0089639A  0F 84 AE 01 00 00               je 0x14089654e
008963A0  49 8D 48 FF                     lea rcx, [r8 - 1]
008963A4  49 8B C0                        mov rax, r8
008963A7  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
008963AC  75 E2                           jne 0x140896390
008963AE  48 85 DB                        test rbx, rbx
008963B1  0F 84 13 04 00 00               je 0x1408967ca
008963B7  48 8B CB                        mov rcx, rbx
008963BA  E8 D1 A8 B9 FF                  call 0x140430c90
008963BF  48 8B F8                        mov rdi, rax
008963C2  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
008963C6  39 87 08 01 00 00               cmp dword ptr [rdi + 0x108], eax
008963CC  0F 85 91 01 00 00               jne 0x140896563
008963D2  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
008963D6  85 C0                           test eax, eax
008963D8  74 0C                           je 0x1408963e6
008963DA  39 87 10 01 00 00               cmp dword ptr [rdi + 0x110], eax
008963E0  0F 85 7D 01 00 00               jne 0x140896563
008963E6  0F 0D 4F E8                     prefetchw byte ptr [rdi - 0x18]
008963EA  48 8B 47 E8                     mov rax, qword ptr [rdi - 0x18]
008963EE  48 85 C0                        test rax, rax
008963F1  0F 8E AA 03 00 00               jle 0x1408967a1
008963F7  48 8B D0                        mov rdx, rax
008963FA  48 8D 48 01                     lea rcx, [rax + 1]
008963FE  F0 48 0F B1 4F E8               lock cmpxchg qword ptr [rdi - 0x18], rcx
00896404  48 3B C2                        cmp rax, rdx
00896407  75 E5                           jne 0x1408963ee
00896409  48 83 C0 01                     add rax, 1
0089640D  0F 84 4D 02 00 00               je 0x140896660
00896413  45 33 C0                        xor r8d, r8d
00896416  33 D2                           xor edx, edx
00896418  48 8D 4F F0                     lea rcx, [rdi - 0x10]
0089641C  E8 0F 9E 97 FF                  call 0x140210230
00896421  4C 8B F0                        mov r14, rax
00896424  F0 48 0F BA 6F F0 00            lock bts qword ptr [rdi - 0x10], 0
0089642B  73 10                           jae 0x14089643d
0089642D  4C 8D 47 F0                     lea r8, [rdi - 0x10]
00896431  48 8B D0                        mov rdx, rax
00896434  48 8D 4F F0                     lea rcx, [rdi - 0x10]
00896438  E8 53 98 97 FF                  call 0x14020fc90
0089643D  4D 85 F6                        test r14, r14
00896440  74 05                           je 0x140896447
00896442  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
00896447  80 4F E0 01                     or byte ptr [rdi - 0x20], 1
0089644B  B8 00 00 01 00                  mov eax, 0x10000
00896450  F0 48 0F C1 47 E8               lock xadd qword ptr [rdi - 0x18], rax
00896456  48 05 00 00 01 00               add rax, 0x10000
0089645C  48 85 C0                        test rax, rax
0089645F  0F 8E 3F 02 00 00               jle 0x1408966a4
00896465  66 FF 4F E2                     dec word ptr [rdi - 0x1e]
00896469  F0 48 FF 03                     lock inc qword ptr [rbx]
0089646D  49 8D 4F 30                     lea rcx, [r15 + 0x30]
00896471  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00896476  48 83 39 00                     cmp qword ptr [rcx], 0
0089647A  74 07                           je 0x140896483
0089647C  33 D2                           xor edx, edx
0089647E  E8 5D DB A0 FF                  call 0x1402a3fe0
00896483  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00896487  39 87 08 01 00 00               cmp dword ptr [rdi + 0x108], eax
0089648D  0F 85 F7 01 00 00               jne 0x14089668a
00896493  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00896497  85 C0                           test eax, eax
00896499  74 0C                           je 0x1408964a7
0089649B  39 87 10 01 00 00               cmp dword ptr [rdi + 0x110], eax
008964A1  0F 85 E3 01 00 00               jne 0x14089668a
008964A7  48 83 7F 18 00                  cmp qword ptr [rdi + 0x18], 0
008964AC  0F 84 CD 01 00 00               je 0x14089667f
008964B2  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
008964B7  48 85 C9                        test rcx, rcx
008964BA  0F 84 E4 00 00 00               je 0x1408965a4
008964C0  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
008964C4  48 39 87 B8 00 00 00            cmp qword ptr [rdi + 0xb8], rax
008964CB  74 0D                           je 0x1408964da
008964CD  48 39 8F C0 00 00 00            cmp qword ptr [rdi + 0xc0], rcx
008964D4  0F 85 ED 00 00 00               jne 0x1408965c7
008964DA  4C 8B B4 24 F8 00 00 00         mov r14, qword ptr [rsp + 0xf8]
008964E2  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008964E7  44 8B 8C 24 E8 00 00 00         mov r9d, dword ptr [rsp + 0xe8]
008964EF  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
008964F4  48 8B D7                        mov rdx, rdi
008964F7  E8 24 03 00 00                  call 0x140896820
008964FC  8B F0                           mov esi, eax
008964FE  48 8B CF                        mov rcx, rdi
00896501  E8 DA 15 00 00                  call 0x140897ae0
00896506  4D 85 ED                        test r13, r13
00896509  74 08                           je 0x140896513
0089650B  49 8B CD                        mov rcx, r13
0089650E  E8 3D 2E A6 FF                  call 0x1402f9350
00896513  4D 85 F6                        test r14, r14
00896516  74 08                           je 0x140896520
00896518  49 8B CE                        mov rcx, r14
0089651B  E8 30 2E A6 FF                  call 0x1402f9350
00896520  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00896529  E8 C2 8A 9C FF                  call 0x14025eff0
0089652E  8B C6                           mov eax, esi
00896530  4C 8D 9C 24 B0 00 00 00         lea r11, [rsp + 0xb0]
00896538  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0089653C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00896540  49 8B E3                        mov rsp, r11
00896543  41 5F                           pop r15
00896545  41 5E                           pop r14
00896547  41 5D                           pop r13
00896549  41 5C                           pop r12
0089654B  5F                              pop rdi
0089654C  C3                              ret
0089654D  CC                              int3
0089654E  4D 85 C0                        test r8, r8
00896551  74 31                           je 0x140896584
00896553  48 8B D3                        mov rdx, rbx
00896556  49 8B CF                        mov rcx, r15
00896559  E8 DA 22 FD FF                  call 0x140868838
0089655E  E9 2D FE FF FF                  jmp 0x140896390
00896563  F0 48 FF 03                     lock inc qword ptr [rbx]
00896567  49 8D 4F 30                     lea rcx, [r15 + 0x30]
0089656B  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00896570  48 83 39 00                     cmp qword ptr [rcx], 0
00896574  74 07                           je 0x14089657d
00896576  33 D2                           xor edx, edx
00896578  E8 63 DA A0 FF                  call 0x1402a3fe0
0089657D  BE 02 07 00 C0                  mov esi, 0xc0000702
00896582  EB 82                           jmp 0x140896506
00896584  49 8B DD                        mov rbx, r13
00896587  44 0F B6 C6                     movzx r8d, sil
0089658B  48 8B D7                        mov rdx, rdi
0089658E  49 8B CF                        mov rcx, r15
00896591  E8 EA 9F BA FF                  call 0x140440580
00896596  E9 13 FE FF FF                  jmp 0x1408963ae
0089659B  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
0089659F  E9 05 FD FF FF                  jmp 0x1408962a9
008965A4  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
008965A8  48 85 D2                        test rdx, rdx
008965AB  74 1A                           je 0x1408965c7
008965AD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008965B6  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
008965BD  48 39 4A 18                     cmp qword ptr [rdx + 0x18], rcx
008965C1  0F 84 0D 02 00 00               je 0x1408967d4
008965C7  48 8B CF                        mov rcx, rdi
008965CA  E8 11 15 00 00                  call 0x140897ae0
008965CF  BE 22 00 00 C0                  mov esi, 0xc0000022
008965D4  4C 8B B4 24 F8 00 00 00         mov r14, qword ptr [rsp + 0xf8]
008965DC  E9 25 FF FF FF                  jmp 0x140896506
008965E1  4D 85 F6                        test r14, r14
008965E4  0F 84 8A 01 00 00               je 0x140896774
008965EA  49 8B F5                        mov rsi, r13
008965ED  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
008965F1  48 85 C9                        test rcx, rcx
008965F4  74 19                           je 0x14089660f
008965F6  8B D3                           mov edx, ebx
008965F8  0F BA F2 1F                     btr edx, 0x1f
008965FC  48 83 C1 28                     add rcx, 0x28
00896600  4C 8D 05 D1 AE 76 FF            lea r8, [rip - 0x89512f]
00896607  E8 F4 38 FF FF                  call 0x140889f00
0089660C  48 8B F0                        mov rsi, rax
0089660F  48 85 F6                        test rsi, rsi
00896612  0F 84 A5 00 00 00               je 0x1408966bd
00896618  48 8B 7E 18                     mov rdi, qword ptr [rsi + 0x18]
0089661C  48 8B CF                        mov rcx, rdi
0089661F  E8 8C 42 FF FF                  call 0x14088a8b0
00896624  33 C0                           xor eax, eax
00896626  F0 44 0F B1 7E 28               lock cmpxchg dword ptr [rsi + 0x28], r15d
0089662C  0F 85 BF 00 00 00               jne 0x1408966f1
00896632  81 A7 08 01 00 00 FF FF FF 7F   and dword ptr [rdi + 0x108], 0x7fffffff
0089663C  0F 1F 40 00                     nop dword ptr [rax]
00896640  41 8B C7                        mov eax, r15d
00896643  F0 0F C1 05 B5 8C 73 00         lock xadd dword ptr [rip + 0x738cb5], eax
0089664B  41 03 C7                        add eax, r15d
0089664E  74 F0                           je 0x140896640
00896650  89 87 10 01 00 00               mov dword ptr [rdi + 0x110], eax
00896656  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0089665B  E9 82 FE FF FF                  jmp 0x1408964e2
00896660  48 8B D3                        mov rdx, rbx
00896663  49 8B CF                        mov rcx, r15
00896666  E8 65 6C 0B 00                  call 0x14094d2d0
0089666B  BE 02 07 00 C0                  mov esi, 0xc0000702
00896670  E9 91 FE FF FF                  jmp 0x140896506
00896675  BE 0D 00 00 C0                  mov esi, 0xc000000d
0089667A  E9 87 FE FF FF                  jmp 0x140896506
0089667F  48 83 7F 10 00                  cmp qword ptr [rdi + 0x10], 0
00896684  0F 85 28 FE FF FF               jne 0x1408964b2
0089668A  48 8B CF                        mov rcx, rdi
0089668D  E8 4E 14 00 00                  call 0x140897ae0
00896692  BE 02 07 00 C0                  mov esi, 0xc0000702
00896697  4C 8B B4 24 F8 00 00 00         mov r14, qword ptr [rsp + 0xf8]
0089669F  E9 62 FE FF FF                  jmp 0x140896506
008966A4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008966A9  41 B9 26 00 00 00               mov r9d, 0x26
008966AF  4C 8B C7                        mov r8, rdi
008966B2  33 D2                           xor edx, edx
008966B4  8D 4A 18                        lea ecx, [rdx + 0x18]
008966B7  E8 A4 6F C6 FF                  call 0x1404fd660
008966BC  CC                              int3
008966BD  BE F0 02 00 C0                  mov esi, 0xc00002f0
008966C2  E9 3F FE FF FF                  jmp 0x140896506
008966C7  49 8B CE                        mov rcx, r14
008966CA  E8 61 49 13 00                  call 0x1409cb030
008966CF  4C 8B E8                        mov r13, rax
008966D2  48 85 C0                        test rax, rax
008966D5  0F 84 03 01 00 00               je 0x1408967de
008966DB  F7 80 00 01 00 00 00 00 01 00   test dword ptr [rax + 0x100], 0x10000
008966E5  75 27                           jne 0x14089670e
008966E7  BE 22 00 00 C0                  mov esi, 0xc0000022
008966EC  E9 15 FE FF FF                  jmp 0x140896506
008966F1  48 8B CF                        mov rcx, rdi
008966F4  E8 E7 13 00 00                  call 0x140897ae0
008966F9  41 8B D7                        mov edx, r15d
008966FC  48 8B CE                        mov rcx, rsi
008966FF  E8 FC 47 FF FF                  call 0x14088af00
00896704  BE 08 07 00 C0                  mov esi, 0xc0000708
00896709  E9 F8 FD FF FF                  jmp 0x140896506
0089670E  F7 80 A0 01 00 00 00 04 00 00   test dword ptr [rax + 0x1a0], 0x400
00896718  0F 85 CA 00 00 00               jne 0x1408967e8
0089671E  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00896722  0F 29 44 24 50                  movaps xmmword ptr [rsp + 0x50], xmm0
00896727  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
0089672B  0F 29 4C 24 60                  movaps xmmword ptr [rsp + 0x60], xmm1
00896730  48 85 FF                        test rdi, rdi
00896733  0F 85 B9 00 00 00               jne 0x1408967f2
00896739  80 7C 24 68 00                  cmp byte ptr [rsp + 0x68], 0
0089673E  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00896743  75 05                           jne 0x14089674a
00896745  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0089674A  49 C1 E9 08                     shr r9, 8
0089674E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00896757  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0089675B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0089675F  45 0F B6 C7                     movzx r8d, r15b
00896763  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00896768  E8 A3 56 03 00                  call 0x1408cbe10
0089676D  8B F0                           mov esi, eax
0089676F  E9 92 FD FF FF                  jmp 0x140896506
00896774  BE 02 07 00 C0                  mov esi, 0xc0000702
00896779  E9 88 FD FF FF                  jmp 0x140896506
0089677E  4C 8B 3D AB E9 72 00            mov r15, qword ptr [rip + 0x72e9ab]
00896785  4D 85 FF                        test r15, r15
00896788  75 08                           jne 0x140896792
0089678A  4D 8B FD                        mov r15, r13
0089678D  E9 B7 FB FF FF                  jmp 0x140896349
00896792  8B C3                           mov eax, ebx
00896794  48 C1 E8 1A                     shr rax, 0x1a
00896798  4D 8B 3C C7                     mov r15, qword ptr [r15 + rax*8]
0089679C  E9 A8 FB FF FF                  jmp 0x140896349
008967A1  0F 84 B9 FE FF FF               je 0x140896660
008967A7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008967AC  41 B9 20 00 00 00               mov r9d, 0x20
008967B2  4C 8B C7                        mov r8, rdi
008967B5  33 D2                           xor edx, edx
008967B7  8D 4A 18                        lea ecx, [rdx + 0x18]
008967BA  E8 A1 6E C6 FF                  call 0x1404fd660
008967BF  CC                              int3
008967C0  BE 02 07 00 C0                  mov esi, 0xc0000702
008967C5  E9 3C FD FF FF                  jmp 0x140896506
008967CA  BE 02 07 00 C0                  mov esi, 0xc0000702
008967CF  E9 32 FD FF FF                  jmp 0x140896506
008967D4  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
008967D9  E9 FC FC FF FF                  jmp 0x1408964da
008967DE  BE 22 00 00 C0                  mov esi, 0xc0000022
008967E3  E9 1E FD FF FF                  jmp 0x140896506
008967E8  BE 22 00 00 C0                  mov esi, 0xc0000022
008967ED  E9 14 FD FF FF                  jmp 0x140896506
008967F2  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
008967F7  48 C1 E8 20                     shr rax, 0x20
008967FB  44 3B E0                        cmp r12d, eax
008967FE  0F 8E BE 2F 28 00               jle 0x140b197c2
00896804  BE 22 00 00 C0                  mov esi, 0xc0000022
00896809  E9 F8 FC FF FF                  jmp 0x140896506
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtAlpcImpersonateClientOfPort(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (176);
    v_r13 = 0;
    v_stack_mA8 = 0;
    v_stack_mA4 = 0;
    v_stack_p10 = 0;
    if (a2 == 0) goto loc_0089659B;
    v_stack_m38 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00896279;
    a4 = (unsigned int)((a2) & (3));
    if (condition_is_equal) goto loc_0089625F;
loc_00896225:
    result = ExRaiseDatatypeMisalignment(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a2, a3, a4);
loc_0089622B:
    if (condition_is_below) goto loc_00896253;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00896247;
    if (a4 != 0) goto loc_00896225;
    if (a2 < v_rbx) { v_rbx = a2; }
loc_00896247:
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 24)));
    goto loc_00896289;
loc_00896253:
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)));
    goto loc_00896289;
loc_0089625F:
    result = (unsigned int)(*(unsigned int *)(a2 + 16));
    if (a2 < ((unsigned int)(*(unsigned int *)(a2 + 16)))) { result = a2; }
    goto loc_0089622B;
loc_00896279:
    a4 = (unsigned int)((a4) & (3));
    goto loc_0089622B;
loc_00896289:
    v_stack_mA4 = (unsigned int)(*(unsigned __int8 *)(result));
    goto loc_008962A1;
loc_008962A1:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))) == 0) goto loc_00896675;
loc_008962A9:
    v_r12 = (a3) >> (2);
    if (((unsigned int)(v_r12)) > 3) goto loc_00896675;
    result = (unsigned int)((a3) & (1));
    v_stack_m98 = result;
    v_rdi = (v_r12 * 4) | (2);
    v_rdi = (v_rdi) & (a3);
    result = (condition_is_not_equal) ? 1 : 0;
    v_stack_p10 = (unsigned int)(result);
    v_stack_mA0 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = v_stack_mA0;
    result = ObReferenceObjectByHandle(a1, 1, *(unsigned __int64 *)(v_rip + 7538992), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_p20 = v_stack_mA0;
    if (sign_flag) goto loc_00896506;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))) == 0) goto loc_008966C7;
    if (sign_flag) goto loc_008965E1;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))) & (0xFC000000ULL)) != 0) goto loc_0089677E;
loc_00896349:
    if (*(unsigned __int64 *)(v_rip + 7539743) == 0) goto loc_008967C0;
    v_rdi = (unsigned int)(((unsigned int)(v_stack_mA8)) & (0x3FFFFFFULL));
    if ((((unsigned int)(v_rdi)) & (0x3FCULL)) == 0) goto loc_00896584;
    result = ExpLookupHandleTableEntry(*(unsigned __int64 *)(v_rip + 7539743), (unsigned int)((unsigned int)(v_rdi)), *(unsigned __int64 *)(v_rip + 7538992), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (result == 0) goto loc_00896584;
loc_00896390:
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) == 0) goto loc_0089654E;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) != 0) goto loc_00896390;
loc_008963AE:
    if (result == 0) goto loc_008967CA;
    result = ExGetHandlePointer(result, (unsigned int)((unsigned int)(v_rdi)), *(unsigned __int64 *)(result), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((*(unsigned int *)(result + 264)) != ((unsigned int)((unsigned int)(v_stack_mA8)))) goto loc_00896563;
    if ((unsigned int)((unsigned int)(v_stack_mA4)) == 0) goto loc_008963E6;
    if ((*(unsigned int *)(result + 272)) != ((unsigned int)((unsigned int)(v_stack_mA4)))) goto loc_00896563;
loc_008963E6:
loc_008963EE:
    if (condition_is_less_or_equal) goto loc_008967A1;
    if ((*(unsigned __int64 *)(result - 24)) != (*(unsigned __int64 *)(result - 24))) goto loc_008963EE;
    result = (*(unsigned __int64 *)(result - 24)) + (1);
    if (condition_is_equal) goto loc_00896660;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result - 16, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (!(condition_is_above_or_equal)) {
        a3 = result - 16;
        a2 = result;
        a1 = result - 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ((unsigned int)(0x10000ULL)) + (0x10000ULL);
    if (condition_is_less_or_equal) goto loc_008966A4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7539743) + 48)) != 0) {
        a2 = 0;
        result = ExfUnblockPushLock(*(unsigned __int64 *)(v_rip + 7539743) + 48, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if ((*(unsigned int *)(result + 264)) != ((unsigned int)((unsigned int)(v_stack_mA8)))) goto loc_0089668A;
    if ((unsigned int)((unsigned int)(v_stack_mA4)) == 0) goto loc_008964A7;
    if ((*(unsigned int *)(result + 272)) != ((unsigned int)((unsigned int)(v_stack_mA4)))) goto loc_0089668A;
loc_008964A7:
    if ((*(unsigned __int64 *)(result + 24)) == 0) goto loc_0089667F;
loc_008964B2:
    if (v_stack_mA0 == 0) goto loc_008965A4;
    if ((*(unsigned __int64 *)(result + 184)) == (*(unsigned __int64 *)(v_stack_mA0 + 16))) goto loc_008964DA;
    if ((*(unsigned __int64 *)(result + 192)) != v_stack_mA0) goto loc_008965C7;
loc_008964DA:
loc_008964E2:
    v_stack_mB8 = (unsigned int)(v_r12);
    result = AlpcpImpersonateMessage(v_stack_mA0, result, (unsigned int)(v_stack_m98), (unsigned int)(v_stack_p10));
    result = AlpcpUnlockMessage(result, result, (unsigned int)(v_stack_m98), (unsigned int)(v_stack_p10));
loc_00896506:
    if (0 != 0) {
        a1 = 0;
        result = ObfDereferenceObject(a1, result, (unsigned int)(v_stack_m98), (unsigned int)(v_stack_p10));
    }
    if (v_stack_p20 != 0) {
        a1 = v_stack_p20;
        result = ObfDereferenceObject(a1, result, (unsigned int)(v_stack_m98), (unsigned int)(v_stack_p10));
    }
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), result, (unsigned int)(v_stack_m98), (unsigned int)(v_stack_p10));
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0089654E:
    if ((unsigned int)(v_stack_m98) == 0) goto loc_00896584;
    result = ExpBlockOnLockedHandleEntry(*(unsigned __int64 *)(v_rip + 7539743), *(unsigned __int64 *)(v_stack_m28 + 48), (unsigned int)(v_stack_m98), (unsigned int)(v_stack_p10));
    goto loc_00896390;
loc_00896563:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7539743) + 48)) != 0) {
        a2 = 0;
        result = ExfUnblockPushLock(*(unsigned __int64 *)(v_rip + 7539743) + 48, a2, (unsigned int)(v_stack_m98), (unsigned int)(v_stack_p10));
    }
    goto loc_00896506;
loc_00896584:
    result = ExHandleLogBadReference(*(unsigned __int64 *)(v_rip + 7539743), result, (unsigned __int8)((unsigned int)(0xC0000702ULL)), (unsigned int)(v_stack_p10));
    goto loc_008963AE;
loc_0089659B:
    goto loc_008962A9;
loc_008965A4:
    if (*(unsigned __int64 *)(result + 16) == 0) goto loc_008965C7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 24)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_008967D4;
loc_008965C7:
    result = AlpcpUnlockMessage(result, *(unsigned __int64 *)(result + 16), (unsigned __int8)((unsigned int)(0xC0000702ULL)), (unsigned int)(v_stack_p10));
    goto loc_00896506;
loc_008965E1:
    if (v_stack_p48 == 0) goto loc_00896774;
    v_rsi = 0;
    if (*(unsigned __int64 *)(v_stack_p48 + 16) != 0) {
        a2 = (unsigned int)((unsigned int)(v_stack_m80));
        a1 = (*(unsigned __int64 *)(v_stack_p48 + 16)) + (40);
        a3 = v_rip - 8999215;
        result = AlpcReferenceBlobByHandle(a1, a2, a3, (unsigned int)(v_stack_p10));
        v_rsi = result;
    }
    if (v_rsi == 0) goto loc_008966BD;
    result = AlpcpLockForCachedReferenceBlob(*(unsigned __int64 *)(v_rsi + 24), a2, a3, (unsigned int)(v_stack_p10));
    result = 0;
    if (condition_is_not_equal) goto loc_008966F1;
loc_00896640:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 7539743)))) + ((unsigned int)(*(unsigned __int64 *)(v_rip + 7539743))));
    if (condition_is_equal) goto loc_00896640;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi + 24) + 272) = (unsigned int)(result);
    goto loc_008964E2;
loc_00896660:
    result = ExUnlockHandleTableEntry(*(unsigned __int64 *)(v_rip + 7539743), (unsigned int)(v_stack_m80), a3, (unsigned int)(v_stack_p10));
    goto loc_00896506;
loc_00896675:
    goto loc_00896506;
loc_0089667F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + 16)) != 0) goto loc_008964B2;
loc_0089668A:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(v_rsi + 24), (unsigned int)(v_stack_m80), a3, (unsigned int)(v_stack_p10));
    goto loc_00896506;
loc_008966A4:
    v_stack_m90 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, *(unsigned __int64 *)(v_rsi + 24), 38);
loc_008966BD:
    goto loc_00896506;
loc_008966C7:
    result = AlpcpReferenceConnectedPort(v_stack_p48, a2, *(unsigned __int64 *)(v_rsi + 24), 38);
    if (result == 0) goto loc_008967DE;
    if (((*(unsigned int *)(result + 256)) & (0x10000ULL)) != 0) goto loc_0089670E;
    goto loc_00896506;
loc_008966F1:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(v_rsi + 24), a2, *(unsigned __int64 *)(v_rsi + 24), 38);
    result = AlpcpDereferenceBlobEx((unsigned int)(0xC0000022ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 7539743))), *(unsigned __int64 *)(v_rsi + 24), 38);
    goto loc_00896506;
loc_0089670E:
    if (((*(unsigned int *)(result + 416)) & (0x400ULL)) != 0) goto loc_008967E8;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm1;
    if (*(unsigned __int64 *)(v_rsi + 24) != 0) goto loc_008967F2;
    if (v_stack_m48 == 0) {
        a4 = v_stack_m58;
    }
    a4 = (a4) >> (8);
    v_stack_m90 = (unsigned int)((unsigned int)(v_stack_m5C));
    result = PsImpersonateClient(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m50, (unsigned __int8)(*(unsigned __int64 *)(v_rip + 7539743)), a4);
    goto loc_00896506;
loc_00896774:
    goto loc_00896506;
loc_0089677E:
    if (*(unsigned __int64 *)(v_rip + 7530923) != 0) goto loc_00896792;
    goto loc_00896349;
loc_00896792:
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m80)))) >> (26);
    goto loc_00896349;
loc_008967A1:
    if (condition_is_equal) goto loc_00896660;
    v_stack_m90 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, *(unsigned __int64 *)(v_rsi + 24), 32);
loc_008967C0:
    goto loc_00896506;
loc_008967CA:
    goto loc_00896506;
loc_008967D4:
    goto loc_008964DA;
loc_008967DE:
    goto loc_00896506;
loc_008967E8:
    goto loc_00896506;
loc_008967F2:
    result = (v_stack_m60) >> (32);
    goto loc_00896506;
}
```

## 5. (Beta) C Style

```c
int64_t NtAlpcImpersonateClientOfPort(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint8_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (176);
    local_r13 = 0;
    v_stack_mA8 = 0;
    v_stack_mA4 = 0;
    v_stack_p10 = 0;
    if (Arg2 == 0) goto loc_0089659B;
    v_stack_m38 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00896279;
    a4 = (uint32_t)((Arg2) & (3));
    if (condition_is_equal) goto loc_0089625F;
loc_00896225:
    result = ExRaiseDatatypeMisalignment(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg2, Arg3, a4);
loc_0089622B:
    if (condition_is_below) goto loc_00896253;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00896247;
    if (a4 != 0) goto loc_00896225;
    if (Arg2 < local_rbx) { local_rbx = Arg2; }
loc_00896247:
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x18)));
    goto loc_00896289;
loc_00896253:
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x10)));
    goto loc_00896289;
loc_0089625F:
    result = (uint32_t)(*(uint32_t *)(Arg2 + 0x10));
    if (Arg2 < ((uint32_t)(*(uint32_t *)(Arg2 + 0x10)))) { result = Arg2; }
    goto loc_0089622B;
loc_00896279:
    a4 = (uint32_t)((a4) & (3));
    goto loc_0089622B;
loc_00896289:
    v_stack_mA4 = (uint32_t)(*(uint8_t *)(result));
    goto loc_008962A1;
loc_008962A1:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x10))) == 0) goto loc_00896675;
loc_008962A9:
    local_r12 = (Arg3) >> (2);
    if (((uint32_t)(local_r12)) > 3) goto loc_00896675;
    result = (uint32_t)((Arg3) & (1));
    v_stack_m98 = result;
    local_rdi = (local_r12 * 4) | (2);
    local_rdi = (local_rdi) & (Arg3);
    result = (condition_is_not_equal) ? 1 : 0;
    v_stack_p10 = (uint32_t)(result);
    v_stack_mA0 = 0;
    v_stack_mB0 = 0;
    v_stack_mB8 = v_stack_mA0;
    result = ObReferenceObjectByHandle(Arg1, 1, *(uint64_t *)(v_rip + 0x730930), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_p20 = v_stack_mA0;
    if (sign_flag) goto loc_00896506;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x10))) == 0) goto loc_008966C7;
    if (sign_flag) goto loc_008965E1;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x10)))) & (0xFC000000ULL)) != 0) goto loc_0089677E;
loc_00896349:
    if (*(uint64_t *)(v_rip + 0x730C1F) == 0) goto loc_008967C0;
    local_rdi = (uint32_t)(((uint32_t)(v_stack_mA8)) & (0x3FFFFFFULL));
    if ((((uint32_t)(local_rdi)) & (0x3FCULL)) == 0) goto loc_00896584;
    result = ExpLookupHandleTableEntry(*(uint64_t *)(v_rip + 0x730C1F), (uint32_t)((uint32_t)(local_rdi)), *(uint64_t *)(v_rip + 0x730930), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (result == 0) goto loc_00896584;
loc_00896390:
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) == 0) goto loc_0089654E;
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) != 0) goto loc_00896390;
loc_008963AE:
    if (result == 0) goto loc_008967CA;
    result = ExGetHandlePointer(result, (uint32_t)((uint32_t)(local_rdi)), *(uint64_t *)(result), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((*(uint32_t *)(result + 0x108)) != ((uint32_t)((uint32_t)(v_stack_mA8)))) goto loc_00896563;
    if ((uint32_t)((uint32_t)(v_stack_mA4)) == 0) goto loc_008963E6;
    if ((*(uint32_t *)(result + 0x110)) != ((uint32_t)((uint32_t)(v_stack_mA4)))) goto loc_00896563;
loc_008963E6:
loc_008963EE:
    if (condition_is_less_or_equal) goto loc_008967A1;
    if ((*(uint64_t *)(result - 0x18)) != (*(uint64_t *)(result - 0x18))) goto loc_008963EE;
    result = (*(uint64_t *)(result - 0x18)) + (1);
    if (condition_is_equal) goto loc_00896660;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result - 16, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = result - 16;
        Arg2 = result;
        Arg1 = result - 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ((uint32_t)(0x10000ULL)) + (0x10000ULL);
    if (condition_is_less_or_equal) goto loc_008966A4;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x730C1F) + 0x30)) != 0) {
        Arg2 = 0;
        result = ExfUnblockPushLock(*(uint64_t *)(v_rip + 0x730C1F) + 48, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if ((*(uint32_t *)(result + 0x108)) != ((uint32_t)((uint32_t)(v_stack_mA8)))) goto loc_0089668A;
    if ((uint32_t)((uint32_t)(v_stack_mA4)) == 0) goto loc_008964A7;
    if ((*(uint32_t *)(result + 0x110)) != ((uint32_t)((uint32_t)(v_stack_mA4)))) goto loc_0089668A;
loc_008964A7:
    if ((*(uint64_t *)(result + 0x18)) == 0) goto loc_0089667F;
loc_008964B2:
    if (v_stack_mA0 == 0) goto loc_008965A4;
    if ((*(uint64_t *)(result + 0xB8)) == (*(uint64_t *)(v_stack_mA0 + 0x10))) goto loc_008964DA;
    if ((*(uint64_t *)(result + 0xC0)) != v_stack_mA0) goto loc_008965C7;
loc_008964DA:
loc_008964E2:
    v_stack_mB8 = (uint32_t)(local_r12);
    result = AlpcpImpersonateMessage(v_stack_mA0, result, (uint32_t)(v_stack_m98), (uint32_t)(v_stack_p10));
    result = AlpcpUnlockMessage(result, result, (uint32_t)(v_stack_m98), (uint32_t)(v_stack_p10));
loc_00896506:
    if (0 != 0) {
        Arg1 = 0;
        result = ObfDereferenceObject(Arg1, result, (uint32_t)(v_stack_m98), (uint32_t)(v_stack_p10));
    }
    if (v_stack_p20 != 0) {
        Arg1 = v_stack_p20;
        result = ObfDereferenceObject(Arg1, result, (uint32_t)(v_stack_m98), (uint32_t)(v_stack_p10));
    }
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), result, (uint32_t)(v_stack_m98), (uint32_t)(v_stack_p10));
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0089654E:
    if ((uint32_t)(v_stack_m98) == 0) goto loc_00896584;
    result = ExpBlockOnLockedHandleEntry(*(uint64_t *)(v_rip + 0x730C1F), *(uint64_t *)(v_stack_m28 + 0x30), (uint32_t)(v_stack_m98), (uint32_t)(v_stack_p10));
    goto loc_00896390;
loc_00896563:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x730C1F) + 0x30)) != 0) {
        Arg2 = 0;
        result = ExfUnblockPushLock(*(uint64_t *)(v_rip + 0x730C1F) + 48, Arg2, (uint32_t)(v_stack_m98), (uint32_t)(v_stack_p10));
    }
    goto loc_00896506;
loc_00896584:
    result = ExHandleLogBadReference(*(uint64_t *)(v_rip + 0x730C1F), result, (uint8_t)((uint32_t)(0xC0000702ULL)), (uint32_t)(v_stack_p10));
    goto loc_008963AE;
loc_0089659B:
    goto loc_008962A9;
loc_008965A4:
    if (*(uint64_t *)(result + 0x10) == 0) goto loc_008965C7;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x18)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_008967D4;
loc_008965C7:
    result = AlpcpUnlockMessage(result, *(uint64_t *)(result + 0x10), (uint8_t)((uint32_t)(0xC0000702ULL)), (uint32_t)(v_stack_p10));
    goto loc_00896506;
loc_008965E1:
    if (v_stack_p48 == 0) goto loc_00896774;
    local_rsi = 0;
    if (*(uint64_t *)(v_stack_p48 + 0x10) != 0) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_m80));
        Arg1 = (*(uint64_t *)(v_stack_p48 + 0x10)) + (40);
        Arg3 = v_rip - 8999215;
        result = AlpcReferenceBlobByHandle(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p10));
        local_rsi = result;
    }
    if (local_rsi == 0) goto loc_008966BD;
    result = AlpcpLockForCachedReferenceBlob(*(uint64_t *)(local_rsi + 0x18), Arg2, Arg3, (uint32_t)(v_stack_p10));
    result = 0;
    if (condition_is_not_equal) goto loc_008966F1;
loc_00896640:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x730C1F)))) + ((uint32_t)(*(uint64_t *)(v_rip + 0x730C1F))));
    if (condition_is_equal) goto loc_00896640;
    *(uint32_t *)(*(uint64_t *)(local_rsi + 0x18) + 0x110) = (uint32_t)(result);
    goto loc_008964E2;
loc_00896660:
    result = ExUnlockHandleTableEntry(*(uint64_t *)(v_rip + 0x730C1F), (uint32_t)(v_stack_m80), Arg3, (uint32_t)(v_stack_p10));
    goto loc_00896506;
loc_00896675:
    goto loc_00896506;
loc_0089667F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + 0x10)) != 0) goto loc_008964B2;
loc_0089668A:
    result = AlpcpUnlockMessage(*(uint64_t *)(local_rsi + 0x18), (uint32_t)(v_stack_m80), Arg3, (uint32_t)(v_stack_p10));
    goto loc_00896506;
loc_008966A4:
    v_stack_m90 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, *(uint64_t *)(local_rsi + 0x18), 38);
loc_008966BD:
    goto loc_00896506;
loc_008966C7:
    result = AlpcpReferenceConnectedPort(v_stack_p48, Arg2, *(uint64_t *)(local_rsi + 0x18), 38);
    if (result == 0) goto loc_008967DE;
    if (((*(uint32_t *)(result + 0x100)) & (0x10000ULL)) != 0) goto loc_0089670E;
    goto loc_00896506;
loc_008966F1:
    result = AlpcpUnlockMessage(*(uint64_t *)(local_rsi + 0x18), Arg2, *(uint64_t *)(local_rsi + 0x18), 38);
    result = AlpcpDereferenceBlobEx((uint32_t)(0xC0000022ULL), (uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x730C1F))), *(uint64_t *)(local_rsi + 0x18), 38);
    goto loc_00896506;
loc_0089670E:
    if (((*(uint32_t *)(result + 0x1A0)) & (0x400ULL)) != 0) goto loc_008967E8;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm1;
    if (*(uint64_t *)(local_rsi + 0x18) != 0) goto loc_008967F2;
    if (v_stack_m48 == 0) {
        a4 = v_stack_m58;
    }
    a4 = (a4) >> (8);
    v_stack_m90 = (uint32_t)((uint32_t)(v_stack_m5C));
    result = PsImpersonateClient(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m50, (uint8_t)(*(uint64_t *)(v_rip + 0x730C1F)), a4);
    goto loc_00896506;
loc_00896774:
    goto loc_00896506;
loc_0089677E:
    if (*(uint64_t *)(v_rip + 0x72E9AB) != 0) goto loc_00896792;
    goto loc_00896349;
loc_00896792:
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m80)))) >> (26);
    goto loc_00896349;
loc_008967A1:
    if (condition_is_equal) goto loc_00896660;
    v_stack_m90 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, *(uint64_t *)(local_rsi + 0x18), 32);
loc_008967C0:
    goto loc_00896506;
loc_008967CA:
    goto loc_00896506;
loc_008967D4:
    goto loc_008964DA;
loc_008967DE:
    goto loc_00896506;
loc_008967E8:
    goto loc_00896506;
loc_008967F2:
    result = (v_stack_m60) >> (32);
    goto loc_00896506;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008961A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
