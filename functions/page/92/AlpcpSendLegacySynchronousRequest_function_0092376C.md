# AlpcpSendLegacySynchronousRequest

- RVA: `0x0092376C`–`0x00923E62` (길이 `1,782` bytes)
- VA: `0x000000014092376C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D348`
- 디코드: `419`개 명령, `1,782/1,782` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x009237F8` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009238AF` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x009238D3` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00923957` → [AlpcpAvailableBufferSize](../89/AlpcpAvailableBufferSize_function_00895390.md) (function, `0x00895390`)
- `0x00923973` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00923999` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009239BA` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x009239FC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00923A20` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00923A65` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00923A6D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00923A81` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00923AA1` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00923AF4` → [AlpcpSetOwnerPortMessage](AlpcpSetOwnerPortMessage_function_00923E70.md) (function, `0x00923E70`)
- `0x00923B4C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00923B65` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00923BA7` → [AlpcpInsertMessagePendingQueue](AlpcpInsertMessagePendingQueue_function_00922830.md) (function, `0x00922830`)
- `0x00923BF1` → [AlpcpSendMessage](../88/AlpcpSendMessage_function_0088BD40.md) (function, `0x0088BD40`)
- `0x00923BFB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00923C21` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00923C6F` → [AlpcpAvailableBufferSize](../89/AlpcpAvailableBufferSize_function_00895390.md) (function, `0x00895390`)
- `0x00923C87` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00923C9C` → [AlpcpCaptureMessageData](../89/AlpcpCaptureMessageData_function_008929A0.md) (function, `0x008929A0`)
- `0x00923CE4` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00923D09` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00923D1D` → [AlpcpAllocateMessage](../89/AlpcpAllocateMessage_function_008926C0.md) (function, `0x008926C0`)
- `0x00923D3B` → [AlpcpCaptureMessageData](../89/AlpcpCaptureMessageData_function_008929A0.md) (function, `0x008929A0`)
- `0x00923D67` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00923D9A` → [AlpcpInsertMessageMainQueue](AlpcpInsertMessageMainQueue_function_00923EB0.md) (function, `0x00923EB0`)
- `0x00923DAF` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00923DBF` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00923DE4` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00923DEC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00923E0B` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00923E18` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00923E36` → [AlpcpEnterAllocationEventMessageLog](../88/AlpcpEnterAllocationEventMessageLog_function_0088B840.md) (function, `0x0088B840`)
- `0x00923E43` → [AlpcpLogSendMessage](../89/AlpcpLogSendMessage_function_008903B4.md) (function, `0x008903B4`)
- `0x00923E58` → [AlpcpLogWaitForReply](../74/AlpcpLogWaitForReply_function_0074D390.md) (function, `0x0074D390`)

### Direct callers
- [AlpcpProcessSynchronousRequest](AlpcpProcessSynchronousRequest_function_00921FCC.md) at `0x00922401`

### Static image references
- `0x00923781` → RVA `0x00E0A740` (`.data`; read)
- `0x009238E6` → RVA `0x00FCF300` (`CACHEALI`; read/write)
- `0x009238FE` → RVA `0x00F100D0` (`.data`; read)
- `0x00923B18` → RVA `0x00E66D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x009237F8` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009238D3` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00923973` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00923999` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009239BA` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x009239FC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00923A20` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00923A65` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00923A6D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00923A81` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00923AA1` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00923B4C` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00923B65` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00923BFB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00923C21` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00923C87` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00923D09` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00923D67` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00923DAF` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00923DE4` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00923DEC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00923E0B` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00923E18` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0092376C  4C 8B DC                        mov r11, rsp
0092376F  53                              push rbx
00923770  56                              push rsi
00923771  57                              push rdi
00923772  41 54                           push r12
00923774  41 55                           push r13
00923776  41 56                           push r14
00923778  41 57                           push r15
0092377A  48 81 EC C0 00 00 00            sub rsp, 0xc0
00923781  48 8B 05 B8 6F 4E 00            mov rax, qword ptr [rip + 0x4e6fb8]
00923788  48 33 C4                        xor rax, rsp
0092378B  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00923793  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
00923798  4D 8B F8                        mov r15, r8
0092379B  4C 8B D2                        mov r10, rdx
0092379E  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
009237A3  4C 8B E9                        mov r13, rcx
009237A6  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
009237AB  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
009237B0  0F 57 C0                        xorps xmm0, xmm0
009237B3  33 C0                           xor eax, eax
009237B5  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
009237BA  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
009237BF  49 89 43 90                     mov qword ptr [r11 - 0x70], rax
009237C3  33 F6                           xor esi, esi
009237C5  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
009237CA  45 84 C9                        test r9b, r9b
009237CD  0F 84 67 04 00 00               je 0x140923c3a
009237D3  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
009237D8  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
009237DC  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009237E6  4C 3B C2                        cmp r8, rdx
009237E9  49 0F 42 D0                     cmovb rdx, r8
009237ED  8D 58 28                        lea ebx, [rax + 0x28]
009237F0  44 8B C3                        mov r8d, ebx
009237F3  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
009237F8  E8 D3 91 D9 FF                  call 0x1406bc9d0
009237FD  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
00923802  44 8A 4C 24 20                  mov r9b, byte ptr [rsp + 0x20]
00923807  EB 0D                           jmp 0x140923816
00923809  44 8B F0                        mov r14d, eax
0092380C  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
00923811  E9 F4 03 00 00                  jmp 0x140923c0a
00923816  39 B4 24 80 00 00 00            cmp dword ptr [rsp + 0x80], esi
0092381D  0F 85 C5 03 00 00               jne 0x140923be8
00923823  41 8B 8D A0 01 00 00            mov ecx, dword ptr [r13 + 0x1a0]
0092382A  0F BA E1 0D                     bt ecx, 0xd
0092382E  0F 83 B4 03 00 00               jae 0x140923be8
00923834  8B C1                           mov eax, ecx
00923836  24 06                           and al, 6
00923838  3C 04                           cmp al, 4
0092383A  0F 85 A8 03 00 00               jne 0x140923be8
00923840  F6 C1 38                        test cl, 0x38
00923843  0F 85 9F 03 00 00               jne 0x140923be8
00923849  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0092384E  48 8B C1                        mov rax, rcx
00923851  48 C1 E8 30                     shr rax, 0x30
00923855  66 85 C0                        test ax, ax
00923858  0F 85 8A 03 00 00               jne 0x140923be8
0092385E  48 C1 E9 10                     shr rcx, 0x10
00923862  0F B7 D1                        movzx edx, cx
00923865  49 3B 95 10 01 00 00            cmp rdx, qword ptr [r13 + 0x110]
0092386C  0F 87 BA 05 00 00               ja 0x140923e2c
00923872  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
00923877  8D 0C 03                        lea ecx, [rbx + rax]
0092387A  66 3B C1                        cmp ax, cx
0092387D  0F 83 9F 05 00 00               jae 0x140923e22
00923883  48 03 C3                        add rax, rbx
00923886  48 3B C2                        cmp rax, rdx
00923889  0F 87 93 05 00 00               ja 0x140923e22
0092388F  66 89 4C 24 6A                  mov word ptr [rsp + 0x6a], cx
00923894  4C 8B F6                        mov r14, rsi
00923897  4D 87 B5 B8 01 00 00            xchg qword ptr [r13 + 0x1b8], r14
0092389E  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
009238A3  4D 85 F6                        test r14, r14
009238A6  0F 84 67 04 00 00               je 0x140923d13
009238AC  49 8B CE                        mov rcx, r14
009238AF  E8 FC 6F F6 FF                  call 0x14088a8b0
009238B4  48 83 CB FF                     or rbx, 0xffffffffffffffff
009238B8  66 41 01 5E E2                  add word ptr [r14 - 0x1e], bx
009238BD  41 8B BE 08 01 00 00            mov edi, dword ptr [r14 + 0x108]
009238C4  0F BA F7 1F                     btr edi, 0x1f
009238C8  33 D2                           xor edx, edx
009238CA  41 B8 18 01 00 00               mov r8d, 0x118
009238D0  49 8B CE                        mov rcx, r14
009238D3  E8 68 33 DA FF                  call 0x1406c6c40
009238D8  41 89 BE 08 01 00 00            mov dword ptr [r14 + 0x108], edi
009238DF  44 8D 63 02                     lea r12d, [rbx + 2]
009238E3  41 8B C4                        mov eax, r12d
009238E6  F0 0F C1 05 12 BA 6A 00         lock xadd dword ptr [rip + 0x6aba12], eax
009238EE  41 03 C4                        add eax, r12d
009238F1  74 F0                           je 0x1409238e3
009238F3  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
009238F8  89 81 10 01 00 00               mov dword ptr [rcx + 0x110], eax
009238FE  83 3D CB C7 5E 00 00            cmp dword ptr [rip + 0x5ec7cb], 0
00923905  0F 85 2B 05 00 00               jne 0x140923e36
0092390B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00923914  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0092391C  0F 10 80 08 05 00 00            movups xmm0, xmmword ptr [rax + 0x508]
00923923  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
00923928  F3 0F 7F 87 F8 00 00 00         movdqu xmmword ptr [rdi + 0xf8], xmm0
00923930  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
00923934  89 87 F0 00 00 00               mov dword ptr [rdi + 0xf0], eax
0092393A  66 C7 87 F4 00 00 00 01 20      mov word ptr [rdi + 0xf4], 0x2001
00923943  40 38 74 24 20                  cmp byte ptr [rsp + 0x20], sil
00923948  0F 85 18 03 00 00               jne 0x140923c66
0092394E  48 0F BF 54 24 68               movsx rdx, word ptr [rsp + 0x68]
00923954  48 8B CF                        mov rcx, rdi
00923957  E8 34 1A F7 FF                  call 0x140895390
0092395C  48 3B D0                        cmp rdx, rax
0092395F  0F 87 D2 03 00 00               ja 0x140923d37
00923965  48 8D 8F 18 01 00 00            lea rcx, [rdi + 0x118]
0092396C  4C 8B C2                        mov r8, rdx
0092396F  49 8D 57 28                     lea rdx, [r15 + 0x28]
00923973  E8 C8 2E DA FF                  call 0x1406c6840
00923978  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
0092397C  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
00923980  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00923985  4C 8D 78 F0                     lea r15, [rax - 0x10]
00923989  4C 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r15
00923991  45 33 C0                        xor r8d, r8d
00923994  33 D2                           xor edx, edx
00923996  49 8B CF                        mov rcx, r15
00923999  E8 92 C8 8E FF                  call 0x140210230
0092399E  48 8B F8                        mov rdi, rax
009239A1  B9 11 00 00 00                  mov ecx, 0x11
009239A6  33 C0                           xor eax, eax
009239A8  F0 49 0F B1 0F                  lock cmpxchg qword ptr [r15], rcx
009239AD  74 10                           je 0x1409239bf
009239AF  4D 8B CF                        mov r9, r15
009239B2  4C 8B C7                        mov r8, rdi
009239B5  33 D2                           xor edx, edx
009239B7  49 8B CF                        mov rcx, r15
009239BA  E8 8D CA 8E FF                  call 0x14021044c
009239BF  48 85 FF                        test rdi, rdi
009239C2  74 04                           je 0x1409239c8
009239C4  44 88 67 0A                     mov byte ptr [rdi + 0xa], r12b
009239C8  4D 8B B5 A8 01 00 00            mov r14, qword ptr [r13 + 0x1a8]
009239CF  49 8B 85 B0 01 00 00            mov rax, qword ptr [r13 + 0x1b0]
009239D6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009239DB  4D 85 F6                        test r14, r14
009239DE  0F 84 0A 03 00 00               je 0x140923cee
009239E4  48 85 C0                        test rax, rax
009239E7  0F 84 01 03 00 00               je 0x140923cee
009239ED  48 8D B8 60 01 00 00            lea rdi, [rax + 0x160]
009239F4  45 33 C0                        xor r8d, r8d
009239F7  33 D2                           xor edx, edx
009239F9  48 8B CF                        mov rcx, rdi
009239FC  E8 2F C8 8E FF                  call 0x140210230
00923A01  48 8B C8                        mov rcx, rax
00923A04  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00923A09  33 C0                           xor eax, eax
00923A0B  8D 50 11                        lea edx, [rax + 0x11]
00923A0E  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
00923A13  74 1A                           je 0x140923a2f
00923A15  4C 8B CF                        mov r9, rdi
00923A18  4C 8B C1                        mov r8, rcx
00923A1B  33 D2                           xor edx, edx
00923A1D  48 8B CF                        mov rcx, rdi
00923A20  E8 27 CA 8E FF                  call 0x14021044c
00923A25  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00923A2A  BA 11 00 00 00                  mov edx, 0x11
00923A2F  48 85 C9                        test rcx, rcx
00923A32  74 04                           je 0x140923a38
00923A34  44 88 61 0A                     mov byte ptr [rcx + 0xa], r12b
00923A38  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00923A3D  8B 81 A0 01 00 00               mov eax, dword ptr [rcx + 0x1a0]
00923A43  A8 20                           test al, 0x20
00923A45  0F 85 AB 03 00 00               jne 0x140923df6
00923A4B  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
00923A4F  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
00923A54  48 89 48 78                     mov qword ptr [rax + 0x78], rcx
00923A58  48 8B C2                        mov rax, rdx
00923A5B  F0 48 0F B1 37                  lock cmpxchg qword ptr [rdi], rsi
00923A60  74 08                           je 0x140923a6a
00923A62  48 8B CF                        mov rcx, rdi
00923A65  E8 D6 F9 93 FF                  call 0x140263440
00923A6A  48 8B CF                        mov rcx, rdi
00923A6D  E8 8E DB 9B FF                  call 0x1402e1600
00923A72  4D 8D A6 60 01 00 00            lea r12, [r14 + 0x160]
00923A79  45 33 C0                        xor r8d, r8d
00923A7C  33 D2                           xor edx, edx
00923A7E  49 8B CC                        mov rcx, r12
00923A81  E8 AA C7 8E FF                  call 0x140210230
00923A86  48 8B F8                        mov rdi, rax
00923A89  33 C0                           xor eax, eax
00923A8B  8D 48 11                        lea ecx, [rax + 0x11]
00923A8E  F0 49 0F B1 0C 24               lock cmpxchg qword ptr [r12], rcx
00923A94  74 10                           je 0x140923aa6
00923A96  4D 8B CC                        mov r9, r12
00923A99  4C 8B C7                        mov r8, rdi
00923A9C  33 D2                           xor edx, edx
00923A9E  49 8B CC                        mov rcx, r12
00923AA1  E8 A6 C9 8E FF                  call 0x14021044c
00923AA6  48 85 FF                        test rdi, rdi
00923AA9  74 04                           je 0x140923aaf
00923AAB  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00923AAF  41 8B 86 A0 01 00 00            mov eax, dword ptr [r14 + 0x1a0]
00923AB6  A8 20                           test al, 0x20
00923AB8  0F 85 0E 03 00 00               jne 0x140923dcc
00923ABE  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
00923AC3  48 8D 51 E2                     lea rdx, [rcx - 0x1e]
00923AC7  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00923ACC  41 B8 03 00 00 00               mov r8d, 3
00923AD2  66 44 01 02                     add word ptr [rdx], r8w
00923AD6  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00923ADE  48 87 88 B8 05 00 00            xchg qword ptr [rax + 0x5b8], rcx
00923AE5  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
00923AEA  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
00923AEE  49 8B D5                        mov rdx, r13
00923AF1  48 8B CF                        mov rcx, rdi
00923AF4  E8 77 03 00 00                  call 0x140923e70
00923AF9  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00923AFE  48 89 87 B8 00 00 00            mov qword ptr [rdi + 0xb8], rax
00923B05  48 8B 00                        mov rax, qword ptr [rax]
00923B08  48 89 87 C0 00 00 00            mov qword ptr [rdi + 0xc0], rax
00923B0F  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00923B14  48 89 78 08                     mov qword ptr [rax + 8], rdi
00923B18  80 3D E1 31 54 00 00            cmp byte ptr [rip + 0x5431e1], 0
00923B1F  0F 85 1B 03 00 00               jne 0x140923e40
00923B25  48 8B CE                        mov rcx, rsi
00923B28  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00923B2D  49 8D 86 E8 00 00 00            lea rax, [r14 + 0xe8]
00923B34  48 39 00                        cmp qword ptr [rax], rax
00923B37  0F 84 41 02 00 00               je 0x140923d7e
00923B3D  4D 8D BE E0 00 00 00            lea r15, [r14 + 0xe0]
00923B44  45 33 C0                        xor r8d, r8d
00923B47  33 D2                           xor edx, edx
00923B49  49 8B CF                        mov rcx, r15
00923B4C  E8 DF C6 8E FF                  call 0x140210230
00923B51  48 8B F8                        mov rdi, rax
00923B54  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
00923B5A  73 0E                           jae 0x140923b6a
00923B5C  4D 8B C7                        mov r8, r15
00923B5F  48 8B D0                        mov rdx, rax
00923B62  49 8B CF                        mov rcx, r15
00923B65  E8 26 C1 8E FF                  call 0x14020fc90
00923B6A  41 BD 01 00 00 00               mov r13d, 1
00923B70  48 85 FF                        test rdi, rdi
00923B73  74 04                           je 0x140923b79
00923B75  44 88 6F 0A                     mov byte ptr [rdi + 0xa], r13b
00923B79  49 8D 8E E8 00 00 00            lea rcx, [r14 + 0xe8]
00923B80  48 8B 01                        mov rax, qword ptr [rcx]
00923B83  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00923B88  48 3B C1                        cmp rax, rcx
00923B8B  0F 84 C2 01 00 00               je 0x140923d53
00923B91  48 05 38 FA FF FF               add rax, -0x5c8
00923B97  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00923B9C  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
00923BA1  48 8B D7                        mov rdx, rdi
00923BA4  49 8B CE                        mov rcx, r14
00923BA7  E8 84 EC FF FF                  call 0x140922830
00923BAC  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00923BB1  66 44 01 28                     add word ptr [rax], r13w
00923BB5  0F BA 6F 28 0D                  bts dword ptr [rdi + 0x28], 0xd
00923BBA  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00923BBF  48 89 B8 C0 05 00 00            mov qword ptr [rax + 0x5c0], rdi
00923BC6  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00923BCB  48 8B 10                        mov rdx, qword ptr [rax]
00923BCE  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00923BD2  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00923BD6  75 09                           jne 0x140923be1
00923BD8  48 39 01                        cmp qword ptr [rcx], rax
00923BDB  0F 84 68 01 00 00               je 0x140923d49
00923BE1  B9 03 00 00 00                  mov ecx, 3
00923BE6  CD 29                           int 0x29
00923BE8  45 33 C0                        xor r8d, r8d
00923BEB  49 8B D7                        mov rdx, r15
00923BEE  49 8B CA                        mov rcx, r10
00923BF1  E8 4A 81 F6 FF                  call 0x14088bd40
00923BF6  EB 1E                           jmp 0x140923c16
00923BF8  49 8B CF                        mov rcx, r15
00923BFB  E8 00 DA 9B FF                  call 0x1402e1600
00923C00  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
00923C05  44 8B 74 24 24                  mov r14d, dword ptr [rsp + 0x24]
00923C0A  45 85 F6                        test r14d, r14d
00923C0D  0F 88 C5 00 00 00               js 0x140923cd8
00923C13  41 8B C6                        mov eax, r14d
00923C16  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00923C1E  48 33 CC                        xor rcx, rsp
00923C21  E8 1A 8A D8 FF                  call 0x1406ac640
00923C26  48 81 C4 C0 00 00 00            add rsp, 0xc0
00923C2D  41 5F                           pop r15
00923C2F  41 5E                           pop r14
00923C31  41 5D                           pop r13
00923C33  41 5C                           pop r12
00923C35  5F                              pop rdi
00923C36  5E                              pop rsi
00923C37  5B                              pop rbx
00923C38  C3                              ret
00923C39  CC                              int3
00923C3A  41 0F 10 00                     movups xmm0, xmmword ptr [r8]
00923C3E  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00923C43  41 0F 10 48 10                  movups xmm1, xmmword ptr [r8 + 0x10]
00923C48  0F 11 4C 24 78                  movups xmmword ptr [rsp + 0x78], xmm1
00923C4D  F2 41 0F 10 40 20               movsd xmm0, qword ptr [r8 + 0x20]
00923C53  F2 0F 11 84 24 88 00 00 00      movsd qword ptr [rsp + 0x88], xmm0
00923C5C  BB 28 00 00 00                  mov ebx, 0x28
00923C61  E9 B0 FB FF FF                  jmp 0x140923816
00923C66  48 0F BF 54 24 68               movsx rdx, word ptr [rsp + 0x68]
00923C6C  48 8B CF                        mov rcx, rdi
00923C6F  E8 1C 17 F7 FF                  call 0x140895390
00923C74  48 3B D0                        cmp rdx, rax
00923C77  77 1C                           ja 0x140923c95
00923C79  48 8D 8F 18 01 00 00            lea rcx, [rdi + 0x118]
00923C80  4C 8B C2                        mov r8, rdx
00923C83  49 8D 57 28                     lea rdx, [r15 + 0x28]
00923C87  E8 B4 2B DA FF                  call 0x1406c6840
00923C8C  44 8B F6                        mov r14d, esi
00923C8F  89 74 24 24                     mov dword ptr [rsp + 0x24], esi
00923C93  EB 13                           jmp 0x140923ca8
00923C95  4D 8D 47 28                     lea r8, [r15 + 0x28]
00923C99  48 8B CF                        mov rcx, rdi
00923C9C  E8 FF EC F6 FF                  call 0x1408929a0
00923CA1  44 8B F0                        mov r14d, eax
00923CA4  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00923CA8  EB 25                           jmp 0x140923ccf
00923CAA  44 8B F0                        mov r14d, eax
00923CAD  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00923CB1  33 F6                           xor esi, esi
00923CB3  48 83 CB FF                     or rbx, 0xffffffffffffffff
00923CB7  44 8D 66 01                     lea r12d, [rsi + 1]
00923CBB  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
00923CC0  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
00923CC5  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00923CCA  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00923CCF  45 85 F6                        test r14d, r14d
00923CD2  0F 89 A4 FC FF FF               jns 0x14092397c
00923CD8  48 85 FF                        test rdi, rdi
00923CDB  0F 84 32 FF FF FF               je 0x140923c13
00923CE1  48 8B CF                        mov rcx, rdi
00923CE4  E8 F7 3D F7 FF                  call 0x140897ae0
00923CE9  E9 25 FF FF FF                  jmp 0x140923c13
00923CEE  C7 44 24 24 37 00 00 C0         mov dword ptr [rsp + 0x24], 0xc0000037
00923CF6  B8 11 00 00 00                  mov eax, 0x11
00923CFB  F0 49 0F B1 37                  lock cmpxchg qword ptr [r15], rsi
00923D00  0F 84 F2 FE FF FF               je 0x140923bf8
00923D06  49 8B CF                        mov rcx, r15
00923D09  E8 32 F7 93 FF                  call 0x140263440
00923D0E  E9 E5 FE FF FF                  jmp 0x140923bf8
00923D13  45 33 C0                        xor r8d, r8d
00923D16  33 D2                           xor edx, edx
00923D18  48 8D 4C 24 28                  lea rcx, [rsp + 0x28]
00923D1D  E8 9E E9 F6 FF                  call 0x1408926c0
00923D22  85 C0                           test eax, eax
00923D24  0F 88 EC FE FF FF               js 0x140923c16
00923D2A  48 83 CB FF                     or rbx, 0xffffffffffffffff
00923D2E  44 8D 63 02                     lea r12d, [rbx + 2]
00923D32  E9 D4 FB FF FF                  jmp 0x14092390b
00923D37  4D 8D 47 28                     lea r8, [r15 + 0x28]
00923D3B  E8 60 EC F6 FF                  call 0x1408929a0
00923D40  44 8B F0                        mov r14d, eax
00923D43  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00923D47  EB 86                           jmp 0x140923ccf
00923D49  48 89 11                        mov qword ptr [rcx], rdx
00923D4C  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00923D50  48 89 30                        mov qword ptr [rax], rsi
00923D53  F0 49 0F C1 1F                  lock xadd qword ptr [r15], rbx
00923D58  80 E3 06                        and bl, 6
00923D5B  80 FB 02                        cmp bl, 2
00923D5E  0F 84 B1 00 00 00               je 0x140923e15
00923D64  49 8B CF                        mov rcx, r15
00923D67  E8 94 D8 9B FF                  call 0x1402e1600
00923D6C  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
00923D71  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
00923D79  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00923D7E  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00923D83  48 89 73 20                     mov qword ptr [rbx + 0x20], rsi
00923D87  48 89 73 18                     mov qword ptr [rbx + 0x18], rsi
00923D8B  48 89 73 28                     mov qword ptr [rbx + 0x28], rsi
00923D8F  48 85 C9                        test rcx, rcx
00923D92  75 32                           jne 0x140923dc6
00923D94  48 8B D7                        mov rdx, rdi
00923D97  49 8B CE                        mov rcx, r14
00923D9A  E8 11 01 00 00                  call 0x140923eb0
00923D9F  41 F7 86 A0 01 00 00 00 02 00 00  test dword ptr [r14 + 0x1a0], 0x200
00923DAA  74 10                           je 0x140923dbc
00923DAC  49 8B CE                        mov rcx, r14
00923DAF  E8 6C BC 8E FF                  call 0x14020fa20
00923DB4  4C 89 73 20                     mov qword ptr [rbx + 0x20], r14
00923DB8  40 88 73 3A                     mov byte ptr [rbx + 0x3a], sil
00923DBC  48 8B CF                        mov rcx, rdi
00923DBF  E8 1C 3D F7 FF                  call 0x140897ae0
00923DC4  EB 0E                           jmp 0x140923dd4
00923DC6  48 89 4B 18                     mov qword ptr [rbx + 0x18], rcx
00923DCA  EB F0                           jmp 0x140923dbc
00923DCC  C7 44 24 24 37 00 00 C0         mov dword ptr [rsp + 0x24], 0xc0000037
00923DD4  B8 11 00 00 00                  mov eax, 0x11
00923DD9  F0 49 0F B1 34 24               lock cmpxchg qword ptr [r12], rsi
00923DDF  74 08                           je 0x140923de9
00923DE1  49 8B CC                        mov rcx, r12
00923DE4  E8 57 F6 93 FF                  call 0x140263440
00923DE9  49 8B CC                        mov rcx, r12
00923DEC  E8 0F D8 9B FF                  call 0x1402e1600
00923DF1  E9 00 FF FF FF                  jmp 0x140923cf6
00923DF6  C7 44 24 24 37 00 00 C0         mov dword ptr [rsp + 0x24], 0xc0000037
00923DFE  48 8B C2                        mov rax, rdx
00923E01  F0 48 0F B1 37                  lock cmpxchg qword ptr [rdi], rsi
00923E06  74 08                           je 0x140923e10
00923E08  48 8B CF                        mov rcx, rdi
00923E0B  E8 30 F6 93 FF                  call 0x140263440
00923E10  48 8B CF                        mov rcx, rdi
00923E13  EB D7                           jmp 0x140923dec
00923E15  49 8B CF                        mov rcx, r15
00923E18  E8 B3 1F 94 FF                  call 0x140265dd0
00923E1D  E9 42 FF FF FF                  jmp 0x140923d64
00923E22  B8 0D 00 00 C0                  mov eax, 0xc000000d
00923E27  E9 EA FD FF FF                  jmp 0x140923c16
00923E2C  B8 2F 00 00 C0                  mov eax, 0xc000002f
00923E31  E9 E0 FD FF FF                  jmp 0x140923c16
00923E36  E8 05 7A F6 FF                  call 0x14088b840
00923E3B  E9 CB FA FF FF                  jmp 0x14092390b
00923E40  48 8B CF                        mov rcx, rdi
00923E43  E8 6C C5 F6 FF                  call 0x1408903b4
00923E48  80 3D B1 2E 54 00 00            cmp byte ptr [rip + 0x542eb1], 0
00923E4F  0F 84 D0 FC FF FF               je 0x140923b25
00923E55  48 8B CF                        mov rcx, rdi
00923E58  E8 33 95 E2 FF                  call 0x14074d390
00923E5D  E9 C3 FC FF FF                  jmp 0x140923b25
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpSendLegacySynchronousRequest(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int16 v_stack_m8E;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD8;
    unsigned int v_stack_p24;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p98;

    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 5140408)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mD8 = a4;
    v_stack_mA0 = a2;
    v_stack_mC8 = a1;
    v_stack_mB8 = a2;
    result = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_rsi = 0;
    v_stack_mD0 = 0;
    if (a4 == 0) goto loc_00923C3A;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 72) = 0;
    if (a3 < a2) { a2 = a3; }
    result = RtlCopyVolatileMemory(v_stack_m90, a2, (unsigned int)((unsigned int)(result + 40)), a4);
    goto loc_00923816;
loc_00923816:
    if (v_stack_m78 != 0) goto loc_00923BE8;
    if (v_stack_m78 >= 0) goto loc_00923BE8;
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 416))))) & (6));
    if (((unsigned __int8)(result)) != 4) goto loc_00923BE8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 416)))) & (56)) != 0) goto loc_00923BE8;
    result = (v_stack_m90) >> (48);
    if ((unsigned __int16)(result) != 0) goto loc_00923BE8;
    a1 = (v_stack_m90) >> (16);
    if (((unsigned __int16)(a1)) > (*(unsigned __int64 *)(a1 + 272))) goto loc_00923E2C;
    if (((unsigned __int16)(v_stack_m90)) >= ((unsigned __int16)(result + 40 + v_stack_m90 * 1))) goto loc_00923E22;
    result = (v_stack_m90) + (result + 40);
    if (result > ((unsigned __int16)(a1))) goto loc_00923E22;
    v_stack_m8E = (unsigned __int16)(result + 40 + v_stack_m90 * 1);
    v_stack_mD0 = 0;
    if (0 == 0) goto loc_00923D13;
    result = AlpcpLockForCachedReferenceBlob(0, (unsigned __int16)(a1), (unsigned int)((unsigned int)(result + 40)), v_stack_mD8);
    v_rbx = (result + 40) | (-1);
    a2 = 0;
    result = memset(0, a2, 280, v_stack_mD8);
    *(unsigned int *)(0 + 264) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 264)));
loc_009238E3:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx + 2))) + ((unsigned int)(v_rbx + 2)));
    if (condition_is_equal) goto loc_009238E3;
    *(unsigned int *)(v_stack_mD0 + 272) = (unsigned int)(result);
    if ((*(unsigned int *)(v_rip + 6211531)) != 0) goto loc_00923E36;
loc_0092390B:
    v_stack_m68 = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(v_stack_mD0 + 248) = v_xmm0;
    *(unsigned int *)(v_stack_mD0 + 240) = (unsigned int)((unsigned int)(v_stack_m90));
    *(unsigned __int16 *)(v_stack_mD0 + 244) = 0x2001ULL;
    if (v_stack_mD8 != 0) goto loc_00923C66;
    result = AlpcpAvailableBufferSize(v_stack_mD0, (__int16)(v_stack_m90), 280, v_stack_mD8);
    if (((__int16)(v_stack_m90)) > result) goto loc_00923D37;
    result = memcpy(v_stack_mD0 + 280, a3 + 40, (__int16)(v_stack_m90), v_stack_mD8);
    v_stack_mD4 = 0;
loc_0092397C:
    v_stack_m98 = *(unsigned __int64 *)(a1 + 16);
    v_stack_m60 = *(unsigned __int64 *)(a1 + 16) - 16;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 16) - 16, a2, a3, v_stack_mD8);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(a1 + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_rbx + 2);
    }
    v_stack_mC8 = *(unsigned __int64 *)(a1 + 432);
    if (*(unsigned __int64 *)(a1 + 424) == 0) goto loc_00923CEE;
    if (*(unsigned __int64 *)(a1 + 432) == 0) goto loc_00923CEE;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 432) + 352, a2, a3, a4);
    v_stack_mB8 = result;
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(a1 + 432) + 352;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 432) + 352;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = v_stack_mB8;
        a2 = 17;
    }
    if (a1 != 0) {
        *(unsigned __int8 *)(a1 + 10) = (unsigned __int8)(v_rbx + 2);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC8 + 416)))) & (32)) != 0) goto loc_00923DF6;
    *(unsigned __int64 *)(v_stack_mD0 + 120) = *(unsigned __int64 *)(v_stack_mC8 + 56);
    result = a2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC8 + 416)))) & (32)) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 432) + 352;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 432) + 352, a2, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 424) + 352, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(a1 + 424) + 352;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 424) + 352;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 424) + 416)))) & (32)) != 0) goto loc_00923DCC;
    v_stack_mB8 = v_stack_mD0 - 30;
    *(unsigned __int64 *)(v_stack_mD0 + 32) = v_stack_m68;
    result = AlpcpSetOwnerPortMessage(v_stack_mD0, a1, 3, a4);
    *(unsigned __int64 *)(v_stack_mD0 + 184) = v_stack_m98;
    *(unsigned __int64 *)(v_stack_mD0 + 192) = *(unsigned __int64 *)(v_stack_m98);
    *(unsigned __int64 *)(v_stack_mA0 + 8) = v_stack_mD0;
    if ((*(unsigned __int8 *)(v_rip + 5517793)) != 0) goto loc_00923E40;
loc_00923B25:
    v_stack_mC8 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 424) + 232)) == (*(unsigned __int64 *)(a1 + 424) + 232)) goto loc_00923D7E;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 424) + 224, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1 + 424) + 224;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1 + 424) + 224;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_m98 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 424) + 232);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 424) + 232)) == (*(unsigned __int64 *)(a1 + 424) + 232)) goto loc_00923D53;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 424) + 232)) + (0xFFFFFFFFFFFFFA38ULL);
    v_stack_mC8 = result;
    result = AlpcpInsertMessagePendingQueue(*(unsigned __int64 *)(a1 + 424), v_stack_mD0, a3, a4);
    *(unsigned __int64 *)(v_stack_mC8 + 1472) = v_stack_mD0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m98) + 8)) != v_stack_m98) goto loc_00923BE1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m98 + 8))) == v_stack_m98) goto loc_00923D49;
loc_00923BE1:
loc_00923BE8:
    a3 = 0;
    result = AlpcpSendMessage(v_stack_mA0, *(unsigned __int64 *)(a1 + 424) + 224, a3, a4);
    goto loc_00923C16;
loc_00923BF8:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 424) + 224, *(unsigned __int64 *)(a1 + 424) + 224, a3, a4);
loc_00923C0A:
    if (sign_flag) goto loc_00923CD8;
loc_00923C13:
loc_00923C16:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 424) + 224, a3, a4);
    v_rsp = (v_rsp) + (192);
    return result;
loc_00923C3A:
    v_stack_p68 = v_xmm0;
    v_stack_p78 = v_xmm1;
    v_stack_p88 = v_xmm0;
    goto loc_00923816;
loc_00923C66:
    result = AlpcpAvailableBufferSize(v_stack_mD0, (__int16)(v_stack_p68), a3, a4);
    if (((__int16)(v_stack_p68)) > result) goto loc_00923C95;
    result = memcpy(v_stack_mD0 + 280, *(unsigned __int64 *)(a1 + 424) + 224 + 40, (__int16)(v_stack_p68), a4);
    v_stack_p24 = 0;
    goto loc_00923CA8;
loc_00923C95:
    result = AlpcpCaptureMessageData(v_stack_mD0, *(unsigned __int64 *)(a1 + 424) + 224 + 40, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    v_stack_p24 = (unsigned int)(result);
loc_00923CA8:
    goto loc_00923CCF;
loc_00923CCF:
    if (!sign_flag) goto loc_0092397C;
loc_00923CD8:
    if (v_stack_mD0 == 0) goto loc_00923C13;
    result = AlpcpUnlockMessage(v_stack_mD0, *(unsigned __int64 *)(a1 + 424) + 224 + 40, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    goto loc_00923C13;
loc_00923CEE:
    v_stack_p24 = 0xC0000037ULL;
loc_00923CF6:
    if (v_stack_mD0 == 0) goto loc_00923BF8;
    result = ExfReleasePushLockShared(*(unsigned __int64 *)(a1 + 424) + 224, *(unsigned __int64 *)(a1 + 424) + 224 + 40, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    goto loc_00923BF8;
loc_00923D13:
    a3 = 0;
    a2 = 0;
    result = AlpcpAllocateMessage(v_stack_p28, a2, a3, a4);
    if (sign_flag) goto loc_00923C16;
    v_rbx = (40) | (-1);
    goto loc_0092390B;
loc_00923D37:
    result = AlpcpCaptureMessageData(v_stack_p28, a2, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    v_stack_p24 = (unsigned int)(result);
    goto loc_00923CCF;
loc_00923D49:
    *(unsigned __int64 *)(v_stack_p28) = 0;
    *(unsigned __int64 *)(a2 + 8) = v_stack_p28;
    *(unsigned __int64 *)(result) = 0;
loc_00923D53:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00923E15;
loc_00923D64:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 424) + 224, a2, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
loc_00923D7E:
    *(unsigned __int64 *)(v_stack_p58 + 32) = 0;
    *(unsigned __int64 *)(v_stack_p58 + 24) = 0;
    *(unsigned __int64 *)(v_stack_p58 + 40) = 0;
    if (v_stack_p30 != 0) goto loc_00923DC6;
    result = AlpcpInsertMessageMainQueue((unsigned int)((unsigned int)(result)), v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    if (((*(unsigned int *)((unsigned int)((unsigned int)(result)) + 416)) & (512)) != 0) {
        a1 = (unsigned int)((unsigned int)(result));
        result = ObfReferenceObject(a1, v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
        *(unsigned __int64 *)(v_stack_p58 + 32) = (unsigned int)((unsigned int)(result));
        *(unsigned __int8 *)(v_stack_p58 + 58) = 0;
    }
    result = AlpcpUnlockMessage(v_stack_p28, v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    goto loc_00923DD4;
loc_00923DC6:
    *(unsigned __int64 *)(v_stack_p58 + 24) = v_stack_p28;
    goto loc_00923DBC;
loc_00923DCC:
    v_stack_p24 = 0xC0000037ULL;
loc_00923DD4:
    result = 17;
    if (((*(unsigned int *)((unsigned int)((unsigned int)(result)) + 416)) & (512)) != 0) {
        a1 = v_rbx + 2;
        result = ExfReleasePushLockShared(a1, v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    }
loc_00923DEC:
    result = KeAbPostRelease(v_rbx + 2, v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    goto loc_00923CF6;
loc_00923DF6:
    v_stack_p24 = 0xC0000037ULL;
    result = v_stack_p28;
    if (((*(unsigned int *)((unsigned int)((unsigned int)(result)) + 416)) & (512)) != 0) {
        a1 = v_stack_p28;
        result = ExfReleasePushLockShared(a1, v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    }
    goto loc_00923DEC;
loc_00923E15:
    result = ExfTryToWakePushLock(v_stack_p98, v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    goto loc_00923D64;
loc_00923E22:
    goto loc_00923C16;
loc_00923E2C:
    goto loc_00923C16;
loc_00923E36:
    result = AlpcpEnterAllocationEventMessageLog(v_stack_p98, v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    goto loc_0092390B;
loc_00923E40:
    result = AlpcpLogSendMessage(v_stack_p28, v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    if ((*(unsigned __int8 *)(v_rip + 5516977)) == 0) goto loc_00923B25;
    result = AlpcpLogWaitForReply(v_stack_p28, v_stack_p28, *(unsigned __int64 *)(a1 + 424) + 224 + 40, a4);
    goto loc_00923B25;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpSendLegacySynchronousRequest(void *Arg1, int64_t Arg2, void *Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint16_t v_stack_m8E;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD8;
    uint32_t v_stack_p24;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p78;
    uint64_t v_stack_p88;
    uint64_t v_stack_p98;

    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x4E6FB8)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mD8 = Arg4;
    v_stack_mA0 = Arg2;
    v_stack_mC8 = Arg1;
    v_stack_mB8 = Arg2;
    result = 0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    local_rsi = 0;
    v_stack_mD0 = 0;
    if (Arg4 == 0) goto loc_00923C3A;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x48) = 0;
    if (Arg3 < Arg2) { Arg2 = Arg3; }
    result = RtlCopyVolatileMemory(v_stack_m90, Arg2, (uint32_t)((uint32_t)(result + 40)), Arg4);
    goto loc_00923816;
loc_00923816:
    if (v_stack_m78 != 0) goto loc_00923BE8;
    if (v_stack_m78 >= 0) goto loc_00923BE8;
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1A0))))) & (6));
    if (((uint8_t)(result)) != 4) goto loc_00923BE8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1A0)))) & (56)) != 0) goto loc_00923BE8;
    result = (v_stack_m90) >> (48);
    if ((uint16_t)(result) != 0) goto loc_00923BE8;
    Arg1 = (v_stack_m90) >> (16);
    if (((uint16_t)(Arg1)) > (*(uint64_t *)(arg1 + 0x110))) goto loc_00923E2C;
    if (((uint16_t)(v_stack_m90)) >= ((uint16_t)(result + 40 + v_stack_m90 * 1))) goto loc_00923E22;
    result = (v_stack_m90) + (result + 40);
    if (result > ((uint16_t)(Arg1))) goto loc_00923E22;
    v_stack_m8E = (uint16_t)(result + 40 + v_stack_m90 * 1);
    v_stack_mD0 = 0;
    if (0 == 0) goto loc_00923D13;
    result = AlpcpLockForCachedReferenceBlob(0, (uint16_t)(Arg1), (uint32_t)((uint32_t)(result + 40)), v_stack_mD8);
    local_rbx = (result + 40) | (-1);
    Arg2 = 0;
    result = memset(0, Arg2, 280, v_stack_mD8);
    *(uint32_t *)(0 + 0x108) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x108)));
loc_009238E3:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx + 2))) + ((uint32_t)(local_rbx + 2)));
    if (condition_is_equal) goto loc_009238E3;
    *(uint32_t *)(v_stack_mD0 + 0x110) = (uint32_t)(result);
    if ((*(uint32_t *)(v_rip + 0x5EC7CB)) != 0) goto loc_00923E36;
loc_0092390B:
    v_stack_m68 = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(v_stack_mD0 + 0xF8) = v_xmm0;
    *(uint32_t *)(v_stack_mD0 + 0xF0) = (uint32_t)((uint32_t)(v_stack_m90));
    *(uint16_t *)(v_stack_mD0 + 0xF4) = 0x2001ULL;
    if (v_stack_mD8 != 0) goto loc_00923C66;
    result = AlpcpAvailableBufferSize(v_stack_mD0, (int16_t)(v_stack_m90), 280, v_stack_mD8);
    if (((int16_t)(v_stack_m90)) > result) goto loc_00923D37;
    result = memcpy(v_stack_mD0 + 280, Arg3 + 40, (int16_t)(v_stack_m90), v_stack_mD8);
    v_stack_mD4 = 0;
loc_0092397C:
    v_stack_m98 = *(uint64_t *)(arg1 + 0x10);
    v_stack_m60 = *(uint64_t *)(arg1 + 0x10) - 16;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x10) - 16, Arg2, Arg3, v_stack_mD8);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = *(uint64_t *)(arg1 + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_rbx + 2);
    }
    v_stack_mC8 = *(uint64_t *)(arg1 + 0x1B0);
    if (*(uint64_t *)(arg1 + 0x1A8) == 0) goto loc_00923CEE;
    if (*(uint64_t *)(arg1 + 0x1B0) == 0) goto loc_00923CEE;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x1B0) + 352, Arg2, Arg3, Arg4);
    v_stack_mB8 = result;
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = *(uint64_t *)(arg1 + 0x1B0) + 352;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x1B0) + 352;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_mB8;
        Arg2 = 17;
    }
    if (Arg1 != NULL) {
        *(uint8_t *)(arg1 + 0xA) = (uint8_t)(local_rbx + 2);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC8 + 0x1A0)))) & (32)) != 0) goto loc_00923DF6;
    *(uint64_t *)(v_stack_mD0 + 0x78) = *(uint64_t *)(v_stack_mC8 + 0x38);
    result = Arg2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC8 + 0x1A0)))) & (32)) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x1B0) + 352;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x1B0) + 352, Arg2, Arg3, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x1A8) + 352, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = *(uint64_t *)(arg1 + 0x1A8) + 352;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x1A8) + 352;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1A8) + 0x1A0)))) & (32)) != 0) goto loc_00923DCC;
    v_stack_mB8 = v_stack_mD0 - 30;
    *(uint64_t *)(v_stack_mD0 + 0x20) = v_stack_m68;
    result = AlpcpSetOwnerPortMessage(v_stack_mD0, Arg1, 3, Arg4);
    *(uint64_t *)(v_stack_mD0 + 0xB8) = v_stack_m98;
    *(uint64_t *)(v_stack_mD0 + 0xC0) = *(uint64_t *)(v_stack_m98);
    *(uint64_t *)(v_stack_mA0 + 0x8) = v_stack_mD0;
    if ((*(uint8_t *)(v_rip + 0x5431E1)) != 0) goto loc_00923E40;
loc_00923B25:
    v_stack_mC8 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x1A8) + 0xE8)) == (*(uint64_t *)(arg1 + 0x1A8) + 232)) goto loc_00923D7E;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x1A8) + 224, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1 + 0x1A8) + 224;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1 + 0x1A8) + 224;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_m98 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x1A8) + 0xE8);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x1A8) + 0xE8)) == (*(uint64_t *)(arg1 + 0x1A8) + 232)) goto loc_00923D53;
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x1A8) + 0xE8)) + (0xFFFFFFFFFFFFFA38ULL);
    v_stack_mC8 = result;
    result = AlpcpInsertMessagePendingQueue(*(uint64_t *)(arg1 + 0x1A8), v_stack_mD0, Arg3, Arg4);
    *(uint64_t *)(v_stack_mC8 + 0x5C0) = v_stack_mD0;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m98) + 0x8)) != v_stack_m98) goto loc_00923BE1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m98 + 0x8))) == v_stack_m98) goto loc_00923D49;
loc_00923BE1:
loc_00923BE8:
    Arg3 = 0;
    result = AlpcpSendMessage(v_stack_mA0, *(uint64_t *)(arg1 + 0x1A8) + 224, Arg3, Arg4);
    goto loc_00923C16;
loc_00923BF8:
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x1A8) + 224, *(uint64_t *)(arg1 + 0x1A8) + 224, Arg3, Arg4);
loc_00923C0A:
    if (sign_flag) goto loc_00923CD8;
loc_00923C13:
loc_00923C16:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x1A8) + 224, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
loc_00923C3A:
    v_stack_p68 = v_xmm0;
    v_stack_p78 = v_xmm1;
    v_stack_p88 = v_xmm0;
    goto loc_00923816;
loc_00923C66:
    result = AlpcpAvailableBufferSize(v_stack_mD0, (int16_t)(v_stack_p68), Arg3, Arg4);
    if (((int16_t)(v_stack_p68)) > result) goto loc_00923C95;
    result = memcpy(v_stack_mD0 + 280, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, (int16_t)(v_stack_p68), Arg4);
    v_stack_p24 = 0;
    goto loc_00923CA8;
loc_00923C95:
    result = AlpcpCaptureMessageData(v_stack_mD0, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    v_stack_p24 = (uint32_t)(result);
loc_00923CA8:
    goto loc_00923CCF;
loc_00923CCF:
    if (!sign_flag) goto loc_0092397C;
loc_00923CD8:
    if (v_stack_mD0 == 0) goto loc_00923C13;
    result = AlpcpUnlockMessage(v_stack_mD0, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    goto loc_00923C13;
loc_00923CEE:
    v_stack_p24 = 0xC0000037ULL;
loc_00923CF6:
    if (v_stack_mD0 == 0) goto loc_00923BF8;
    result = ExfReleasePushLockShared(*(uint64_t *)(arg1 + 0x1A8) + 224, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    goto loc_00923BF8;
loc_00923D13:
    Arg3 = 0;
    Arg2 = 0;
    result = AlpcpAllocateMessage(v_stack_p28, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00923C16;
    local_rbx = (40) | (-1);
    goto loc_0092390B;
loc_00923D37:
    result = AlpcpCaptureMessageData(v_stack_p28, Arg2, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    v_stack_p24 = (uint32_t)(result);
    goto loc_00923CCF;
loc_00923D49:
    *(uint64_t *)(v_stack_p28) = 0;
    *(uint64_t *)(Arg2 + 0x8) = v_stack_p28;
    *(uint64_t *)(result) = 0;
loc_00923D53:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00923E15;
loc_00923D64:
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x1A8) + 224, Arg2, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
loc_00923D7E:
    *(uint64_t *)(v_stack_p58 + 0x20) = 0;
    *(uint64_t *)(v_stack_p58 + 0x18) = 0;
    *(uint64_t *)(v_stack_p58 + 0x28) = 0;
    if (v_stack_p30 != 0) goto loc_00923DC6;
    result = AlpcpInsertMessageMainQueue((uint32_t)((uint32_t)(result)), v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    if (((*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x1A0)) & (512)) != 0) {
        Arg1 = (uint32_t)((uint32_t)(result));
        result = ObfReferenceObject(Arg1, v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
        *(uint64_t *)(v_stack_p58 + 0x20) = (uint32_t)((uint32_t)(result));
        *(uint8_t *)(v_stack_p58 + 0x3A) = 0;
    }
    result = AlpcpUnlockMessage(v_stack_p28, v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    goto loc_00923DD4;
loc_00923DC6:
    *(uint64_t *)(v_stack_p58 + 0x18) = v_stack_p28;
    goto loc_00923DBC;
loc_00923DCC:
    v_stack_p24 = 0xC0000037ULL;
loc_00923DD4:
    result = 17;
    if (((*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x1A0)) & (512)) != 0) {
        Arg1 = local_rbx + 2;
        result = ExfReleasePushLockShared(Arg1, v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    }
loc_00923DEC:
    result = KeAbPostRelease(local_rbx + 2, v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    goto loc_00923CF6;
loc_00923DF6:
    v_stack_p24 = 0xC0000037ULL;
    result = v_stack_p28;
    if (((*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x1A0)) & (512)) != 0) {
        Arg1 = v_stack_p28;
        result = ExfReleasePushLockShared(Arg1, v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    }
    goto loc_00923DEC;
loc_00923E15:
    result = ExfTryToWakePushLock(v_stack_p98, v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    goto loc_00923D64;
loc_00923E22:
    goto loc_00923C16;
loc_00923E2C:
    goto loc_00923C16;
loc_00923E36:
    result = AlpcpEnterAllocationEventMessageLog(v_stack_p98, v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    goto loc_0092390B;
loc_00923E40:
    result = AlpcpLogSendMessage(v_stack_p28, v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    if ((*(uint8_t *)(v_rip + 0x542EB1)) == 0) goto loc_00923B25;
    result = AlpcpLogWaitForReply(v_stack_p28, v_stack_p28, *(uint64_t *)(arg1 + 0x1A8) + 224 + 40, Arg4);
    goto loc_00923B25;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x110` | `64` | `R` |
| `Arg1` | `+ 0x1A0` | `32` | `R` |
| `Arg1` | `+ 0x1A8` | `64` | `R` |
| `Arg1` | `+ 0x1B0` | `64` | `R` |
| `Arg1` | `+ 0x1B8` | `64` | `R/W` |
| `Arg3` | `+ 0x0` | `128` | `R` |
| `Arg3` | `+ 0x10` | `128` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092376C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
