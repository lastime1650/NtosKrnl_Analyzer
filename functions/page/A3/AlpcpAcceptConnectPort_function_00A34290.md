# AlpcpAcceptConnectPort

- RVA: `0x00A34290`–`0x00A34D8E` (길이 `2,814` bytes)
- VA: `0x0000000140A34290`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD5FC`
- 디코드: `620`개 명령, `2,814/2,814` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **45**; 고유 호출 대상: **35**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A3432F` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A34361` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A34373` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A34455` → [AlpcpProbeAndCaptureMessageHeader](../9C/AlpcpProbeAndCaptureMessageHeader_function_009C5BB0.md) (function, `0x009C5BB0`)
- `0x00A34477` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00A34499` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00A345E5` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A3463D` → [AlpcpLookupMessage](../89/AlpcpLookupMessage_function_00895A40.md) (function, `0x00895A40`)
- `0x00A346A9` → [AlpcpReleaseAttributes](../88/AlpcpReleaseAttributes_function_0088D750.md) (function, `0x0088D750`)
- `0x00A346C7` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x00A34719` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A34739` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00A3478E` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00A34796` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A34800` → [AlpcpValidateConnectionMessage](../92/AlpcpValidateConnectionMessage_function_00921C38.md) (function, `0x00921C38`)
- `0x00A3487F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A34898` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A348D9` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A348E1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A34906` → [AlpcpCreatePort](../9E/AlpcpCreatePort_function_009E7358.md) (function, `0x009E7358`)
- `0x00A34924` → [AlpcpInitializePort](../92/AlpcpInitializePort_function_00925DC4.md) (function, `0x00925DC4`)
- `0x00A34966` → [AlpcpValidateAndSetPortAttributes](../9E/AlpcpValidateAndSetPortAttributes_function_009E73BC.md) (function, `0x009E73BC`)
- `0x00A3498B` → [AlpcpSetOwnerProcessPort](../9E/AlpcpSetOwnerProcessPort_function_009E761C.md) (function, `0x009E761C`)
- `0x00A349AE` → [AlpcpReferenceBlob](../89/AlpcpReferenceBlob_function_00890110.md) (function, `0x00890110`)
- `0x00A349BB` → [AlpcpLockBlobExclusive](../92/AlpcpLockBlobExclusive_function_009253A4.md) (function, `0x009253A4`)
- `0x00A34A13` → [AlpcpUnlockBlobUncachedExclusive](../92/AlpcpUnlockBlobUncachedExclusive_function_0092536C.md) (function, `0x0092536C`)
- `0x00A34A55` → [AlpcpSetupMessageDataForDeferredCopy](../92/AlpcpSetupMessageDataForDeferredCopy_function_00922C60.md) (function, `0x00922C60`)
- `0x00A34A86` → [AlpcpMapLegacyPortRemoteView](../A9/AlpcpMapLegacyPortRemoteView_function_00A9FEE4.md) (function, `0x00A9FEE4`)
- `0x00A34AD1` → [AlpcpMapLegacyPortView](../92/AlpcpMapLegacyPortView_function_00921588.md) (function, `0x00921588`)
- `0x00A34AEF` → [AlpcpMapLegacyPortRemoteView](../A9/AlpcpMapLegacyPortRemoteView_function_00A9FEE4.md) (function, `0x00A9FEE4`)
- `0x00A34B2B` → [AlpcpCaptureAttributes](../88/AlpcpCaptureAttributes_function_0088CD20.md) (function, `0x0088CD20`)
- `0x00A34B3D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00A34B63` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x00A34B79` → [AlpcpReleaseAttributes](../88/AlpcpReleaseAttributes_function_0088D750.md) (function, `0x0088D750`)
- `0x00A34BE1` → [PsReleaseProcessWakeCounter](../88/PsReleaseProcessWakeCounter_function_0088B940.md) (function, `0x0088B940`)
- `0x00A34C00` → [PsReleaseProcessWakeCounter](../88/PsReleaseProcessWakeCounter_function_0088B940.md) (function, `0x0088B940`)
- `0x00A34CE6` → [AlpcpDispatchMessage](../88/AlpcpDispatchMessage_function_0088F7D0.md) (function, `0x0088F7D0`)
- `0x00A34D14` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x00A34D26` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A34D39` → [AlpcpFlushResourcesPort](../92/AlpcpFlushResourcesPort_function_009253F4.md) (function, `0x009253F4`)
- `0x00A34D41` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A34D50` → [NtClose](../86/NtClose_function_00868870.md) (function, `0x00868870`)
- `0x00A34D69` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A34D82` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00A34D87` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [NtAcceptConnectPort](NtAcceptConnectPort_function_00A34180.md) at `0x00A341D4`
- [NtAlpcAcceptConnectPort](NtAlpcAcceptConnectPort_function_00A34200.md) at `0x00A34272`

### Static image references
- `0x00A342A3` → RVA `0x00E0A740` (`.data`; read)
- `0x00A345B5` → RVA `0x00FC6C18` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00A3432F` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A34361` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A34373` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A34477` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x00A34499` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x00A34719` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A34739` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00A3478E` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00A34796` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A3487F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A34898` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A348D9` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A348E1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A34B3D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00A34D26` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A34D41` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A34D69` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A34290  40 53                           push rbx
00A34292  56                              push rsi
00A34293  57                              push rdi
00A34294  41 54                           push r12
00A34296  41 55                           push r13
00A34298  41 56                           push r14
00A3429A  41 57                           push r15
00A3429C  48 81 EC 60 02 00 00            sub rsp, 0x260
00A342A3  48 8B 05 96 64 3D 00            mov rax, qword ptr [rip + 0x3d6496]
00A342AA  48 33 C4                        xor rax, rsp
00A342AD  48 89 84 24 50 02 00 00         mov qword ptr [rsp + 0x250], rax
00A342B5  4C 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r9
00A342BD  49 8B D8                        mov rbx, r8
00A342C0  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
00A342C8  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A342CC  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
00A342D4  4C 8B BC 24 F0 02 00 00         mov r15, qword ptr [rsp + 0x2f0]
00A342DC  4C 89 BC 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r15
00A342E4  4C 8B B4 24 E8 02 00 00         mov r14, qword ptr [rsp + 0x2e8]
00A342EC  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
00A342F4  48 8B B4 24 C0 02 00 00         mov rsi, qword ptr [rsp + 0x2c0]
00A342FC  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
00A34301  4C 8B AC 24 D0 02 00 00         mov r13, qword ptr [rsp + 0x2d0]
00A34309  4C 89 AC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r13
00A34311  48 8B 84 24 D8 02 00 00         mov rax, qword ptr [rsp + 0x2d8]
00A34319  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
00A34321  33 D2                           xor edx, edx
00A34323  44 8D 42 40                     lea r8d, [rdx + 0x40]
00A34327  48 8D 8C 24 C0 01 00 00         lea rcx, [rsp + 0x1c0]
00A3432F  E8 0C 29 C9 FF                  call 0x1406c6c40
00A34334  0F 57 C0                        xorps xmm0, xmm0
00A34337  33 C0                           xor eax, eax
00A34339  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
00A34341  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
00A34349  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00A34351  8D 78 48                        lea edi, [rax + 0x48]
00A34354  44 8B C7                        mov r8d, edi
00A34357  33 D2                           xor edx, edx
00A34359  48 8D 8C 24 00 02 00 00         lea rcx, [rsp + 0x200]
00A34361  E8 DA 28 C9 FF                  call 0x1406c6c40
00A34366  44 8B C7                        mov r8d, edi
00A34369  33 D2                           xor edx, edx
00A3436B  48 8D 8C 24 70 01 00 00         lea rcx, [rsp + 0x170]
00A34373  E8 C8 28 C9 FF                  call 0x1406c6c40
00A34378  0F 57 C0                        xorps xmm0, xmm0
00A3437B  0F 11 84 24 38 01 00 00         movups xmmword ptr [rsp + 0x138], xmm0
00A34383  0F 11 84 24 48 01 00 00         movups xmmword ptr [rsp + 0x148], xmm0
00A3438B  0F 11 84 24 58 01 00 00         movups xmmword ptr [rsp + 0x158], xmm0
00A34393  33 C0                           xor eax, eax
00A34395  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
00A3439D  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
00A343A5  33 FF                           xor edi, edi
00A343A7  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00A343AC  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00A343B0  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
00A343B4  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00A343B8  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00A343BD  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00A343C2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A343CB  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
00A343D1  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00A343D5  84 C0                           test al, al
00A343D7  0F 84 42 01 00 00               je 0x140a3451f
00A343DD  44 8A A4 24 F8 02 00 00         mov r12b, byte ptr [rsp + 0x2f8]
00A343E5  45 84 E4                        test r12b, r12b
00A343E8  75 1B                           jne 0x140a34405
00A343EA  40 38 BC 24 E0 02 00 00         cmp byte ptr [rsp + 0x2e0], dil
00A343F2  75 11                           jne 0x140a34405
00A343F4  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00A343FE  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
00A34403  EB 45                           jmp 0x140a3444a
00A34405  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
00A3440A  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00A34414  48 8B CB                        mov rcx, rbx
00A34417  45 85 C0                        test r8d, r8d
00A3441A  79 17                           jns 0x140a34433
00A3441C  48 39 9C 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rbx
00A34424  48 0F 42 8C 24 90 00 00 00      cmovb rcx, qword ptr [rsp + 0x90]
00A3442D  8B 01                           mov eax, dword ptr [rcx]
00A3442F  89 01                           mov dword ptr [rcx], eax
00A34431  EB 17                           jmp 0x140a3444a
00A34433  48 39 9C 24 90 00 00 00         cmp qword ptr [rsp + 0x90], rbx
00A3443B  48 0F 42 8C 24 90 00 00 00      cmovb rcx, qword ptr [rsp + 0x90]
00A34444  48 8B 01                        mov rax, qword ptr [rcx]
00A34447  48 89 01                        mov qword ptr [rcx], rax
00A3444A  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
00A34452  49 8B CD                        mov rcx, r13
00A34455  E8 56 17 F9 FF                  call 0x1409c5bb0
00A3445A  48 85 F6                        test rsi, rsi
00A3445D  74 1D                           je 0x140a3447c
00A3445F  48 8B D3                        mov rdx, rbx
00A34462  48 3B F3                        cmp rsi, rbx
00A34465  48 0F 42 D6                     cmovb rdx, rsi
00A34469  41 B8 48 00 00 00               mov r8d, 0x48
00A3446F  48 8D 8C 24 00 02 00 00         lea rcx, [rsp + 0x200]
00A34477  E8 54 85 C8 FF                  call 0x1406bc9d0
00A3447C  4D 85 F6                        test r14, r14
00A3447F  74 4F                           je 0x140a344d0
00A34481  48 8B D3                        mov rdx, rbx
00A34484  4C 3B F3                        cmp r14, rbx
00A34487  49 0F 42 D6                     cmovb rdx, r14
00A3448B  41 B8 30 00 00 00               mov r8d, 0x30
00A34491  48 8D 8C 24 38 01 00 00         lea rcx, [rsp + 0x138]
00A34499  E8 32 85 C8 FF                  call 0x1406bc9d0
00A3449E  83 BC 24 38 01 00 00 30         cmp dword ptr [rsp + 0x138], 0x30
00A344A6  74 0A                           je 0x140a344b2
00A344A8  B8 0D 00 00 C0                  mov eax, 0xc000000d
00A344AD  E9 AC 08 00 00                  jmp 0x140a34d5e
00A344B2  41 F6 C6 03                     test r14b, 3
00A344B6  0F 85 C6 08 00 00               jne 0x140a34d82
00A344BC  48 8B CB                        mov rcx, rbx
00A344BF  4C 3B F3                        cmp r14, rbx
00A344C2  49 0F 42 CE                     cmovb rcx, r14
00A344C6  8A 01                           mov al, byte ptr [rcx]
00A344C8  88 01                           mov byte ptr [rcx], al
00A344CA  8A 41 2F                        mov al, byte ptr [rcx + 0x2f]
00A344CD  88 41 2F                        mov byte ptr [rcx + 0x2f], al
00A344D0  4D 85 FF                        test r15, r15
00A344D3  74 37                           je 0x140a3450c
00A344D5  48 8B C3                        mov rax, rbx
00A344D8  4C 3B FB                        cmp r15, rbx
00A344DB  49 0F 42 C7                     cmovb rax, r15
00A344DF  90                              nop
00A344E0  8B 00                           mov eax, dword ptr [rax]
00A344E2  83 F8 18                        cmp eax, 0x18
00A344E5  74 0A                           je 0x140a344f1
00A344E7  B8 0D 00 00 C0                  mov eax, 0xc000000d
00A344EC  E9 6D 08 00 00                  jmp 0x140a34d5e
00A344F1  41 F6 C7 03                     test r15b, 3
00A344F5  0F 85 8C 08 00 00               jne 0x140a34d87
00A344FB  4C 3B FB                        cmp r15, rbx
00A344FE  49 0F 42 DF                     cmovb rbx, r15
00A34502  8A 03                           mov al, byte ptr [rbx]
00A34504  88 03                           mov byte ptr [rbx], al
00A34506  8A 43 17                        mov al, byte ptr [rbx + 0x17]
00A34509  88 43 17                        mov byte ptr [rbx + 0x17], al
00A3450C  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00A34514  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00A34518  EB 78                           jmp 0x140a34592
00A3451A  E9 3F 08 00 00                  jmp 0x140a34d5e
00A3451F  48 85 F6                        test rsi, rsi
00A34522  74 3D                           je 0x140a34561
00A34524  0F 10 06                        movups xmm0, xmmword ptr [rsi]
00A34527  0F 29 84 24 00 02 00 00         movaps xmmword ptr [rsp + 0x200], xmm0
00A3452F  0F 10 4E 10                     movups xmm1, xmmword ptr [rsi + 0x10]
00A34533  0F 29 8C 24 10 02 00 00         movaps xmmword ptr [rsp + 0x210], xmm1
00A3453B  0F 10 46 20                     movups xmm0, xmmword ptr [rsi + 0x20]
00A3453F  0F 29 84 24 20 02 00 00         movaps xmmword ptr [rsp + 0x220], xmm0
00A34547  0F 10 4E 30                     movups xmm1, xmmword ptr [rsi + 0x30]
00A3454B  0F 29 8C 24 30 02 00 00         movaps xmmword ptr [rsp + 0x230], xmm1
00A34553  F2 0F 10 46 40                  movsd xmm0, qword ptr [rsi + 0x40]
00A34558  F2 0F 11 84 24 40 02 00 00      movsd qword ptr [rsp + 0x240], xmm0
00A34561  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
00A34566  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
00A3456E  41 0F 10 4D 10                  movups xmm1, xmmword ptr [r13 + 0x10]
00A34573  0F 11 8C 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm1
00A3457B  F2 41 0F 10 45 20               movsd xmm0, qword ptr [r13 + 0x20]
00A34581  F2 0F 11 84 24 D0 00 00 00      movsd qword ptr [rsp + 0xd0], xmm0
00A3458A  44 8A A4 24 F8 02 00 00         mov r12b, byte ptr [rsp + 0x2f8]
00A34592  39 BC 24 C8 00 00 00            cmp dword ptr [rsp + 0xc8], edi
00A34599  75 0A                           jne 0x140a345a5
00A3459B  B8 1F 02 00 C0                  mov eax, 0xc000021f
00A345A0  E9 B9 07 00 00                  jmp 0x140a34d5e
00A345A5  4C 8B EF                        mov r13, rdi
00A345A8  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00A345B0  48 85 DB                        test rbx, rbx
00A345B3  74 4E                           je 0x140a34603
00A345B5  4C 8B 05 5C 26 59 00            mov r8, qword ptr [rip + 0x59265c]
00A345BC  48 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdi
00A345C4  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00A345C9  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00A345D1  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A345D6  44 8A C8                        mov r9b, al
00A345D9  41 BC 01 00 00 00               mov r12d, 1
00A345DF  41 8B D4                        mov edx, r12d
00A345E2  48 8B CB                        mov rcx, rbx
00A345E5  E8 C6 47 E3 FF                  call 0x140868db0
00A345EA  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
00A345F2  4C 89 AC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r13
00A345FA  85 C0                           test eax, eax
00A345FC  79 1B                           jns 0x140a34619
00A345FE  E9 5B 07 00 00                  jmp 0x140a34d5e
00A34603  45 84 E4                        test r12b, r12b
00A34606  0F 84 4D 07 00 00               je 0x140a34d59
00A3460C  89 BC 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], edi
00A34613  41 BC 01 00 00 00               mov r12d, 1
00A34619  4C 89 AC 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r13
00A34621  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A34626  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A3462B  44 8B 84 24 D0 00 00 00         mov r8d, dword ptr [rsp + 0xd0]
00A34633  8B 94 24 C8 00 00 00            mov edx, dword ptr [rsp + 0xc8]
00A3463A  49 8B CD                        mov rcx, r13
00A3463D  E8 FE 13 E6 FF                  call 0x140895a40
00A34642  8B F0                           mov esi, eax
00A34644  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00A34649  85 C0                           test eax, eax
00A3464B  78 3A                           js 0x140a34687
00A3464D  4D 85 ED                        test r13, r13
00A34650  75 0C                           jne 0x140a3465e
00A34652  4D 8B 6F 10                     mov r13, qword ptr [r15 + 0x10]
00A34656  4C 89 AC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r13
00A3465E  41 8B 4F 28                     mov ecx, dword ptr [r15 + 0x28]
00A34662  84 C9                           test cl, cl
00A34664  79 0A                           jns 0x140a34670
00A34666  41 8B DC                        mov ebx, r12d
00A34669  BE 03 07 00 C0                  mov esi, 0xc0000703
00A3466E  EB 1B                           jmp 0x140a3468b
00A34670  41 0F B7 87 F4 00 00 00         movzx eax, word ptr [r15 + 0xf4]
00A34678  25 FF 00 FF FF                  and eax, 0xffff00ff
00A3467D  83 F8 0A                        cmp eax, 0xa
00A34680  74 4F                           je 0x140a346d1
00A34682  BE 1F 02 00 C0                  mov esi, 0xc000021f
00A34687  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00A3468B  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00A34690  4D 85 FF                        test r15, r15
00A34693  0F 84 80 06 00 00               je 0x140a34d19
00A34699  39 7C 24 58                     cmp dword ptr [rsp + 0x58], edi
00A3469D  74 14                           je 0x140a346b3
00A3469F  48 8D 94 24 70 01 00 00         lea rdx, [rsp + 0x170]
00A346A7  33 C9                           xor ecx, ecx
00A346A9  E8 A2 90 E5 FF                  call 0x14088d750
00A346AE  44 89 64 24 68                  mov dword ptr [rsp + 0x68], r12d
00A346B3  85 DB                           test ebx, ebx
00A346B5  0F 84 56 06 00 00               je 0x140a34d11
00A346BB  41 B8 00 00 01 00               mov r8d, 0x10000
00A346C1  49 8B D7                        mov rdx, r15
00A346C4  49 8B CD                        mov rcx, r13
00A346C7  E8 54 FA E5 FF                  call 0x140894120
00A346CC  E9 48 06 00 00                  jmp 0x140a34d19
00A346D1  49 8B 57 10                     mov rdx, qword ptr [r15 + 0x10]
00A346D5  49 3B 97 C0 00 00 00            cmp rdx, qword ptr [r15 + 0xc0]
00A346DC  0F 85 1C 06 00 00               jne 0x140a34cfe
00A346E2  49 3B D5                        cmp rdx, r13
00A346E5  0F 84 DF 00 00 00               je 0x140a347ca
00A346EB  F6 C1 07                        test cl, 7
00A346EE  0F 85 AE 00 00 00               jne 0x140a347a2
00A346F4  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00A346F8  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00A34700  48 85 C0                        test rax, rax
00A34703  0F 84 F5 05 00 00               je 0x140a34cfe
00A34709  48 8B 70 10                     mov rsi, qword ptr [rax + 0x10]
00A3470D  48 8D 5E F0                     lea rbx, [rsi - 0x10]
00A34711  45 33 C0                        xor r8d, r8d
00A34714  33 D2                           xor edx, edx
00A34716  48 8B CB                        mov rcx, rbx
00A34719  E8 12 BB 7D FF                  call 0x140210230
00A3471E  4C 8B F0                        mov r14, rax
00A34721  33 C0                           xor eax, eax
00A34723  44 8D 78 11                     lea r15d, [rax + 0x11]
00A34727  F0 4C 0F B1 3B                  lock cmpxchg qword ptr [rbx], r15
00A3472C  74 10                           je 0x140a3473e
00A3472E  4C 8B CB                        mov r9, rbx
00A34731  4D 8B C6                        mov r8, r14
00A34734  33 D2                           xor edx, edx
00A34736  48 8B CB                        mov rcx, rbx
00A34739  E8 0E BD 7D FF                  call 0x14021044c
00A3473E  4D 85 F6                        test r14, r14
00A34741  74 04                           je 0x140a34747
00A34743  45 88 66 0A                     mov byte ptr [r14 + 0xa], r12b
00A34747  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00A3474F  8B 80 A0 01 00 00               mov eax, dword ptr [rax + 0x1a0]
00A34755  D1 E8                           shr eax, 1
00A34757  83 E0 03                        and eax, 3
00A3475A  83 E8 01                        sub eax, 1
00A3475D  74 1A                           je 0x140a34779
00A3475F  83 F8 01                        cmp eax, 1
00A34762  75 15                           jne 0x140a34779
00A34764  4C 39 2E                        cmp qword ptr [rsi], r13
00A34767  74 0B                           je 0x140a34774
00A34769  4C 39 6E 08                     cmp qword ptr [rsi + 8], r13
00A3476D  74 05                           je 0x140a34774
00A3476F  40 8A F7                        mov sil, dil
00A34772  EB 0D                           jmp 0x140a34781
00A34774  41 8A F4                        mov sil, r12b
00A34777  EB 08                           jmp 0x140a34781
00A34779  4C 39 6E 10                     cmp qword ptr [rsi + 0x10], r13
00A3477D  40 0F 94 C6                     sete sil
00A34781  49 8B C7                        mov rax, r15
00A34784  F0 48 0F B1 3B                  lock cmpxchg qword ptr [rbx], rdi
00A34789  74 08                           je 0x140a34793
00A3478B  48 8B CB                        mov rcx, rbx
00A3478E  E8 AD EC 82 FF                  call 0x140263440
00A34793  48 8B CB                        mov rcx, rbx
00A34796  E8 65 CE 8A FF                  call 0x1402e1600
00A3479B  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00A347A0  EB 42                           jmp 0x140a347e4
00A347A2  41 8B 85 A0 01 00 00            mov eax, dword ptr [r13 + 0x1a0]
00A347A9  83 E0 06                        and eax, 6
00A347AC  3C 06                           cmp al, 6
00A347AE  0F 85 4A 05 00 00               jne 0x140a34cfe
00A347B4  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
00A347B8  48 85 C0                        test rax, rax
00A347BB  0F 84 3D 05 00 00               je 0x140a34cfe
00A347C1  48 39 10                        cmp qword ptr [rax], rdx
00A347C4  0F 85 34 05 00 00               jne 0x140a34cfe
00A347CA  8B C1                           mov eax, ecx
00A347CC  83 E0 07                        and eax, 7
00A347CF  3C 03                           cmp al, 3
00A347D1  0F 85 27 05 00 00               jne 0x140a34cfe
00A347D7  0F BA E1 0D                     bt ecx, 0xd
00A347DB  0F 82 1D 05 00 00               jb 0x140a34cfe
00A347E1  41 8A F4                        mov sil, r12b
00A347E4  40 84 F6                        test sil, sil
00A347E7  0F 84 11 05 00 00               je 0x140a34cfe
00A347ED  44 8A 84 24 F8 02 00 00         mov r8b, byte ptr [rsp + 0x2f8]
00A347F5  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
00A347FD  49 8B CD                        mov rcx, r13
00A34800  E8 33 D4 EE FF                  call 0x140921c38
00A34805  8B F0                           mov esi, eax
00A34807  85 C0                           test eax, eax
00A34809  0F 88 78 FE FF FF               js 0x140a34687
00A3480F  49 8B 5F 18                     mov rbx, qword ptr [r15 + 0x18]
00A34813  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00A34817  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00A3481F  8B 83 A0 01 00 00               mov eax, dword ptr [rbx + 0x1a0]
00A34825  A8 20                           test al, 0x20
00A34827  74 0D                           je 0x140a34836
00A34829  41 8B DC                        mov ebx, r12d
00A3482C  BE 37 00 00 C0                  mov esi, 0xc0000037
00A34831  E9 55 FE FF FF                  jmp 0x140a3468b
00A34836  41 F7 85 00 01 00 00 00 00 10 00  test dword ptr [r13 + 0x100], 0x100000
00A34841  75 1F                           jne 0x140a34862
00A34843  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A3484C  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00A34853  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00A34858  49 3B 4D 18                     cmp rcx, qword ptr [r13 + 0x18]
00A3485C  0F 85 20 FE FF FF               jne 0x140a34682
00A34862  40 38 BC 24 E0 02 00 00         cmp byte ptr [rsp + 0x2e0], dil
00A3486A  0F 85 85 00 00 00               jne 0x140a348f5
00A34870  48 8D B3 60 01 00 00            lea rsi, [rbx + 0x160]
00A34877  45 33 C0                        xor r8d, r8d
00A3487A  33 D2                           xor edx, edx
00A3487C  48 8B CE                        mov rcx, rsi
00A3487F  E8 AC B9 7D FF                  call 0x140210230
00A34884  4C 8B F0                        mov r14, rax
00A34887  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00A3488D  73 0E                           jae 0x140a3489d
00A3488F  4C 8B C6                        mov r8, rsi
00A34892  48 8B D0                        mov rdx, rax
00A34895  48 8B CE                        mov rcx, rsi
00A34898  E8 F3 B3 7D FF                  call 0x14020fc90
00A3489D  4D 85 F6                        test r14, r14
00A348A0  74 04                           je 0x140a348a6
00A348A2  45 88 66 0A                     mov byte ptr [r14 + 0xa], r12b
00A348A6  8B 83 A0 01 00 00               mov eax, dword ptr [rbx + 0x1a0]
00A348AC  83 C8 10                        or eax, 0x10
00A348AF  89 83 A0 01 00 00               mov dword ptr [rbx + 0x1a0], eax
00A348B5  0F BA E0 08                     bt eax, 8
00A348B9  73 0C                           jae 0x140a348c7
00A348BB  48 8B 84 24 C8 02 00 00         mov rax, qword ptr [rsp + 0x2c8]
00A348C3  48 89 43 38                     mov qword ptr [rbx + 0x38], rax
00A348C7  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A348CB  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
00A348D0  24 06                           and al, 6
00A348D2  3C 02                           cmp al, 2
00A348D4  75 08                           jne 0x140a348de
00A348D6  48 8B CE                        mov rcx, rsi
00A348D9  E8 F2 14 83 FF                  call 0x140265dd0
00A348DE  48 8B CE                        mov rcx, rsi
00A348E1  E8 1A CD 8A FF                  call 0x1402e1600
00A348E6  41 8B DC                        mov ebx, r12d
00A348E9  8B F7                           mov esi, edi
00A348EB  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00A348F0  E9 96 FD FF FF                  jmp 0x140a3468b
00A348F5  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00A348FA  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
00A34902  8A 4C 24 40                     mov cl, byte ptr [rsp + 0x40]
00A34906  E8 4D 2A FB FF                  call 0x1409e7358
00A3490B  8B F0                           mov esi, eax
00A3490D  85 C0                           test eax, eax
00A3490F  0F 88 72 FD FF FF               js 0x140a34687
00A34915  45 33 C0                        xor r8d, r8d
00A34918  41 8D 50 03                     lea edx, [r8 + 3]
00A3491C  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00A34921  49 8B CE                        mov rcx, r14
00A34924  E8 9B 14 EF FF                  call 0x140925dc4
00A34929  8B F0                           mov esi, eax
00A3492B  85 C0                           test eax, eax
00A3492D  0F 88 D5 03 00 00               js 0x140a34d08
00A34933  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A34938  48 F7 D8                        neg rax
00A3493B  48 1B D2                        sbb rdx, rdx
00A3493E  48 8D 84 24 00 02 00 00         lea rax, [rsp + 0x200]
00A34946  48 23 D0                        and rdx, rax
00A34949  8A 84 24 F8 02 00 00            mov al, byte ptr [rsp + 0x2f8]
00A34950  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00A34954  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00A34959  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00A3495D  45 33 C9                        xor r9d, r9d
00A34960  4D 8B C5                        mov r8, r13
00A34963  49 8B CE                        mov rcx, r14
00A34966  E8 51 2A FB FF                  call 0x1409e73bc
00A3496B  8B F0                           mov esi, eax
00A3496D  85 C0                           test eax, eax
00A3496F  0F 88 93 03 00 00               js 0x140a34d08
00A34975  48 F7 5C 24 70                  neg qword ptr [rsp + 0x70]
00A3497A  48 1B D2                        sbb rdx, rdx
00A3497D  48 8D 84 24 00 02 00 00         lea rax, [rsp + 0x200]
00A34985  48 23 D0                        and rdx, rax
00A34988  49 8B CE                        mov rcx, r14
00A3498B  E8 8C 2C FB FF                  call 0x1409e761c
00A34990  BE 00 10 00 00                  mov esi, 0x1000
00A34995  40 38 BC 24 F8 02 00 00         cmp byte ptr [rsp + 0x2f8], dil
00A3499D  74 07                           je 0x140a349a6
00A3499F  41 09 B6 A0 01 00 00            or dword ptr [r14 + 0x1a0], esi
00A349A6  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00A349AE  E8 5D B7 E5 FF                  call 0x140890110
00A349B3  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00A349BB  E8 E4 09 EF FF                  call 0x1409253a4
00A349C0  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00A349C8  49 89 4E 10                     mov qword ptr [r14 + 0x10], rcx
00A349CC  4C 89 71 08                     mov qword ptr [rcx + 8], r14
00A349D0  4C 89 AB A8 01 00 00            mov qword ptr [rbx + 0x1a8], r13
00A349D7  4C 89 B3 B0 01 00 00            mov qword ptr [rbx + 0x1b0], r14
00A349DE  49 89 9E A8 01 00 00            mov qword ptr [r14 + 0x1a8], rbx
00A349E5  49 89 9E B0 01 00 00            mov qword ptr [r14 + 0x1b0], rbx
00A349EC  8B 93 A0 01 00 00               mov edx, dword ptr [rbx + 0x1a0]
00A349F2  85 D6                           test esi, edx
00A349F4  74 1D                           je 0x140a34a13
00A349F6  41 85 B6 A0 01 00 00            test dword ptr [r14 + 0x1a0], esi
00A349FD  74 14                           je 0x140a34a13
00A349FF  B8 00 20 00 00                  mov eax, 0x2000
00A34A04  0B D0                           or edx, eax
00A34A06  89 93 A0 01 00 00               mov dword ptr [rbx + 0x1a0], edx
00A34A0C  41 09 86 A0 01 00 00            or dword ptr [r14 + 0x1a0], eax
00A34A13  E8 54 09 EF FF                  call 0x14092536c
00A34A18  44 0F B7 8C 24 B0 00 00 00      movzx r9d, word ptr [rsp + 0xb0]
00A34A21  41 8D 41 28                     lea eax, [r9 + 0x28]
00A34A25  66 89 84 24 F4 01 00 00         mov word ptr [rsp + 0x1f4], ax
00A34A2D  C7 84 24 F6 01 00 00 0B 00 00 00  mov dword ptr [rsp + 0x1f6], 0xb
00A34A38  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00A34A3C  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A34A40  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
00A34A45  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
00A34A4A  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
00A34A52  49 8B CF                        mov rcx, r15
00A34A55  E8 06 E2 EE FF                  call 0x140922c60
00A34A5A  8B F0                           mov esi, eax
00A34A5C  85 C0                           test eax, eax
00A34A5E  0F 88 A4 02 00 00               js 0x140a34d08
00A34A64  40 38 BC 24 F8 02 00 00         cmp byte ptr [rsp + 0x2f8], dil
00A34A6C  74 2D                           je 0x140a34a9b
00A34A6E  49 39 BF 90 00 00 00            cmp qword ptr [r15 + 0x90], rdi
00A34A75  74 24                           je 0x140a34a9b
00A34A77  49 8D 57 68                     lea rdx, [r15 + 0x68]
00A34A7B  4C 8D 84 24 20 01 00 00         lea r8, [rsp + 0x120]
00A34A83  49 8B CE                        mov rcx, r14
00A34A86  E8 59 B4 06 00                  call 0x140a9fee4
00A34A8B  8B F0                           mov esi, eax
00A34A8D  85 C0                           test eax, eax
00A34A8F  0F 88 73 02 00 00               js 0x140a34d08
00A34A95  41 0F BA 6F 28 0E               bts dword ptr [r15 + 0x28], 0xe
00A34A9B  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
00A34AA0  48 39 BC 24 A8 00 00 00         cmp qword ptr [rsp + 0xa8], rdi
00A34AA8  74 62                           je 0x140a34b0c
00A34AAA  33 C0                           xor eax, eax
00A34AAC  0F 57 C0                        xorps xmm0, xmm0
00A34AAF  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
00A34AB7  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
00A34ABE  4C 8D 84 24 70 01 00 00         lea r8, [rsp + 0x170]
00A34AC6  48 8D 94 24 38 01 00 00         lea rdx, [rsp + 0x138]
00A34ACE  49 8B CE                        mov rcx, r14
00A34AD1  E8 B2 CA EE FF                  call 0x140921588
00A34AD6  8B F0                           mov esi, eax
00A34AD8  85 C0                           test eax, eax
00A34ADA  78 56                           js 0x140a34b32
00A34ADC  4C 8D 84 24 08 01 00 00         lea r8, [rsp + 0x108]
00A34AE4  48 8D 94 24 70 01 00 00         lea rdx, [rsp + 0x170]
00A34AEC  48 8B CB                        mov rcx, rbx
00A34AEF  E8 F0 B3 06 00                  call 0x140a9fee4
00A34AF4  8B F0                           mov esi, eax
00A34AF6  85 C0                           test eax, eax
00A34AF8  78 38                           js 0x140a34b32
00A34AFA  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
00A34B02  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
00A34B0A  EB 26                           jmp 0x140a34b32
00A34B0C  48 8D 84 24 70 01 00 00         lea rax, [rsp + 0x170]
00A34B14  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A34B19  4D 8B CF                        mov r9, r15
00A34B1C  4C 8B 84 24 E8 00 00 00         mov r8, qword ptr [rsp + 0xe8]
00A34B24  8B 54 24 48                     mov edx, dword ptr [rsp + 0x48]
00A34B28  49 8B CD                        mov rcx, r13
00A34B2B  E8 F0 81 E5 FF                  call 0x14088cd20
00A34B30  8B F0                           mov esi, eax
00A34B32  85 F6                           test esi, esi
00A34B34  0F 88 CE 01 00 00               js 0x140a34d08
00A34B3A  49 8B CE                        mov rcx, r14
00A34B3D  E8 DE AE 7D FF                  call 0x14020fa20
00A34B42  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00A34B47  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A34B4C  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00A34B51  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00A34B55  45 33 C9                        xor r9d, r9d
00A34B58  33 D2                           xor edx, edx
00A34B5A  41 B8 01 00 1F 00               mov r8d, 0x1f0001
00A34B60  49 8B CE                        mov rcx, r14
00A34B63  E8 38 4C E8 FF                  call 0x1408b97a0
00A34B68  8B F0                           mov esi, eax
00A34B6A  85 C0                           test eax, eax
00A34B6C  0F 88 96 01 00 00               js 0x140a34d08
00A34B72  49 8D 57 68                     lea rdx, [r15 + 0x68]
00A34B76  49 8B CF                        mov rcx, r15
00A34B79  E8 D2 8B E5 FF                  call 0x14088d750
00A34B7E  0F 28 84 24 70 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x170]
00A34B86  41 0F 11 47 68                  movups xmmword ptr [r15 + 0x68], xmm0
00A34B8B  0F 28 8C 24 80 01 00 00         movaps xmm1, xmmword ptr [rsp + 0x180]
00A34B93  41 0F 11 4F 78                  movups xmmword ptr [r15 + 0x78], xmm1
00A34B98  0F 28 84 24 90 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x190]
00A34BA0  41 0F 11 87 88 00 00 00         movups xmmword ptr [r15 + 0x88], xmm0
00A34BA8  0F 28 8C 24 A0 01 00 00         movaps xmm1, xmmword ptr [rsp + 0x1a0]
00A34BB0  41 0F 11 8F 98 00 00 00         movups xmmword ptr [r15 + 0x98], xmm1
00A34BB8  F2 0F 10 84 24 B0 01 00 00      movsd xmm0, qword ptr [rsp + 0x1b0]
00A34BC1  F2 41 0F 11 87 A8 00 00 00      movsd qword ptr [r15 + 0xa8], xmm0
00A34BCA  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
00A34BCE  49 8B 8F D0 00 00 00            mov rcx, qword ptr [r15 + 0xd0]
00A34BD5  48 85 C9                        test rcx, rcx
00A34BD8  74 13                           je 0x140a34bed
00A34BDA  41 8B 97 08 01 00 00            mov edx, dword ptr [r15 + 0x108]
00A34BE1  E8 5A 6D E5 FF                  call 0x14088b940
00A34BE6  49 89 BF D0 00 00 00            mov qword ptr [r15 + 0xd0], rdi
00A34BED  49 8B 8F D8 00 00 00            mov rcx, qword ptr [r15 + 0xd8]
00A34BF4  48 85 C9                        test rcx, rcx
00A34BF7  74 13                           je 0x140a34c0c
00A34BF9  41 8B 97 08 01 00 00            mov edx, dword ptr [r15 + 0x108]
00A34C00  E8 3B 6D E5 FF                  call 0x14088b940
00A34C05  49 89 BF D8 00 00 00            mov qword ptr [r15 + 0xd8], rdi
00A34C0C  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00A34C11  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00A34C19  39 7C 24 48                     cmp dword ptr [rsp + 0x48], edi
00A34C1D  7D 04                           jge 0x140a34c23
00A34C1F  89 08                           mov dword ptr [rax], ecx
00A34C21  EB 03                           jmp 0x140a34c26
00A34C23  48 89 08                        mov qword ptr [rax], rcx
00A34C26  48 8B 84 24 C8 02 00 00         mov rax, qword ptr [rsp + 0x2c8]
00A34C2E  48 85 C0                        test rax, rax
00A34C31  48 0F 44 C1                     cmove rax, rcx
00A34C35  49 89 46 38                     mov qword ptr [r14 + 0x38], rax
00A34C39  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00A34C41  48 85 C0                        test rax, rax
00A34C44  74 23                           je 0x140a34c69
00A34C46  0F 10 84 24 38 01 00 00         movups xmm0, xmmword ptr [rsp + 0x138]
00A34C4E  0F 11 00                        movups xmmword ptr [rax], xmm0
00A34C51  0F 10 8C 24 48 01 00 00         movups xmm1, xmmword ptr [rsp + 0x148]
00A34C59  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A34C5D  0F 10 84 24 58 01 00 00         movups xmm0, xmmword ptr [rsp + 0x158]
00A34C65  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00A34C69  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00A34C71  48 85 C0                        test rax, rax
00A34C74  74 19                           je 0x140a34c8f
00A34C76  0F 10 84 24 20 01 00 00         movups xmm0, xmmword ptr [rsp + 0x120]
00A34C7E  0F 11 00                        movups xmmword ptr [rax], xmm0
00A34C81  F2 0F 10 84 24 30 01 00 00      movsd xmm0, qword ptr [rsp + 0x130]
00A34C8A  F2 0F 11 40 10                  movsd qword ptr [rax + 0x10], xmm0
00A34C8F  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00A34C93  EB 26                           jmp 0x140a34cbb
00A34C95  8B F0                           mov esi, eax
00A34C97  33 FF                           xor edi, edi
00A34C99  44 8D 67 01                     lea r12d, [rdi + 1]
00A34C9D  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
00A34CA5  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00A34CAA  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00A34CAF  8B DF                           mov ebx, edi
00A34CB1  8B C7                           mov eax, edi
00A34CB3  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A34CB7  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00A34CBB  85 F6                           test esi, esi
00A34CBD  0F 88 CD F9 FF FF               js 0x140a34690
00A34CC3  4C 89 B4 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], r14
00A34CCB  4C 89 BC 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], r15
00A34CD3  C7 84 24 F0 01 00 00 00 00 01 00  mov dword ptr [rsp + 0x1f0], 0x10000
00A34CDE  48 8D 8C 24 C0 01 00 00         lea rcx, [rsp + 0x1c0]
00A34CE6  E8 E5 AA E5 FF                  call 0x14088f7d0
00A34CEB  8B F0                           mov esi, eax
00A34CED  85 C0                           test eax, eax
00A34CEF  78 05                           js 0x140a34cf6
00A34CF1  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00A34CF6  4C 8B FF                        mov r15, rdi
00A34CF9  E9 92 F9 FF FF                  jmp 0x140a34690
00A34CFE  BE 02 07 00 C0                  mov esi, 0xc0000702
00A34D03  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00A34D08  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00A34D0C  E9 7F F9 FF FF                  jmp 0x140a34690
00A34D11  49 8B CF                        mov rcx, r15
00A34D14  E8 C7 2D E6 FF                  call 0x140897ae0
00A34D19  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
00A34D21  48 85 C9                        test rcx, rcx
00A34D24  74 05                           je 0x140a34d2b
00A34D26  E8 25 46 8C FF                  call 0x1402f9350
00A34D2B  4D 85 F6                        test r14, r14
00A34D2E  74 16                           je 0x140a34d46
00A34D30  39 7C 24 68                     cmp dword ptr [rsp + 0x68], edi
00A34D34  74 08                           je 0x140a34d3e
00A34D36  49 8B CE                        mov rcx, r14
00A34D39  E8 B6 06 EF FF                  call 0x1409253f4
00A34D3E  49 8B CE                        mov rcx, r14
00A34D41  E8 0A 46 8C FF                  call 0x1402f9350
00A34D46  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00A34D4B  48 85 C9                        test rcx, rcx
00A34D4E  74 05                           je 0x140a34d55
00A34D50  E8 1B 3B E3 FF                  call 0x140868870
00A34D55  8B C6                           mov eax, esi
00A34D57  EB 05                           jmp 0x140a34d5e
00A34D59  B8 40 01 00 C0                  mov eax, 0xc0000140
00A34D5E  48 8B 8C 24 50 02 00 00         mov rcx, qword ptr [rsp + 0x250]
00A34D66  48 33 CC                        xor rcx, rsp
00A34D69  E8 D2 78 C7 FF                  call 0x1406ac640
00A34D6E  48 81 C4 60 02 00 00            add rsp, 0x260
00A34D75  41 5F                           pop r15
00A34D77  41 5E                           pop r14
00A34D79  41 5D                           pop r13
00A34D7B  41 5C                           pop r12
00A34D7D  5F                              pop rdi
00A34D7E  5E                              pop rsi
00A34D7F  5B                              pop rbx
00A34D80  C3                              ret
00A34D81  CC                              int3
00A34D82  E8 49 52 E6 FF                  call 0x140899fd0
00A34D87  E8 44 52 E6 FF                  call 0x140899fd0
00A34D8C  90                              nop
00A34D8D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpAcceptConnectPort(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, unsigned __int8 a9, __int64 a10, __int64 a11, unsigned __int8 a12)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned int v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned int v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m250;
    unsigned int v_stack_m254;
    unsigned __int8 v_stack_m258;
    unsigned __int8 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA2;
    unsigned __int16 v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (608);
    result = (*(unsigned __int64 *)(v_rip + 4023446)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1C0 = a4;
    v_stack_m210 = a3;
    v_stack_m250 = a2;
    v_stack_m208 = a1;
    v_stack_m1A8 = a11;
    v_stack_m1F0 = a10;
    v_stack_m228 = a5;
    v_stack_m1B8 = a7;
    v_stack_m1B0 = a8;
    a2 = 0;
    result = memset(v_stack_mD8, a2, a2 + 64, a4);
    result = 0;
    v_stack_m1E8 = v_xmm0;
    v_stack_m1D8 = v_xmm0;
    v_stack_m1C8 = 0;
    a2 = 0;
    result = memset(v_stack_m98, a2, (unsigned int)((unsigned int)(result + 72)), a4);
    a2 = 0;
    result = memset(v_stack_m128, a2, (unsigned int)((unsigned int)(result + 72)), a4);
    v_stack_m160 = v_xmm0;
    v_stack_m150 = v_xmm0;
    v_stack_m140 = v_xmm0;
    result = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = 0;
    v_rdi = 0;
    v_stack_m248 = 0;
    v_stack_m254 = 0;
    v_stack_m240 = 0;
    v_stack_m230 = 0;
    v_stack_m238 = 0;
    v_stack_m220 = 0;
    v_stack_m258 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00A3451F;
    if (a12 != 0) goto loc_00A34405;
    if (a9 != 0) goto loc_00A34405;
    goto loc_00A3444A;
loc_00A34405:
    if (!sign_flag) goto loc_00A34433;
    if (v_stack_m208 < a3) { a3 = v_stack_m208; }
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    goto loc_00A3444A;
loc_00A34433:
    if (v_stack_m208 < a3) { a3 = v_stack_m208; }
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(a3);
loc_00A3444A:
    result = AlpcpProbeAndCaptureMessageHeader(a7, v_stack_m1E8, (unsigned int)(v_stack_m250), a4);
    if (a5 != 0) {
        a2 = a3;
        if (a5 < a3) { a2 = a5; }
        a3 = 72;
        a1 = v_stack_m98;
        result = RtlCopyVolatileMemory(a1, a2, a3, a4);
    }
    if (a10 == 0) goto loc_00A344D0;
    if (a10 < a3) { a3 = a10; }
    result = RtlCopyVolatileMemory(v_stack_m160, a3, 48, a4);
    if (v_stack_m160 == 48) goto loc_00A344B2;
    goto loc_00A34D5E;
loc_00A344B2:
    if ((((unsigned __int8)(a10)) & (3)) != 0) goto loc_00A34D82;
    if (a10 < a3) { a3 = a10; }
    *(unsigned __int8 *)(a3) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    *(unsigned __int8 *)(a3 + 47) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 47));
loc_00A344D0:
    if (a11 == 0) goto loc_00A3450C;
    if (a11 < a3) { a3 = a11; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) == 24) goto loc_00A344F1;
    goto loc_00A34D5E;
loc_00A344F1:
    if ((((unsigned __int8)(a11)) & (3)) != 0) goto loc_00A34D87;
    if (a11 < a3) { a3 = a11; }
    *(unsigned __int8 *)(a3) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    *(unsigned __int8 *)(a3 + 23) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 23));
loc_00A3450C:
    goto loc_00A34592;
loc_00A3451F:
    if (a5 != 0) {
        v_stack_m98 = v_xmm0;
        v_stack_m88 = v_xmm1;
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm1;
        v_stack_m58 = v_xmm0;
    }
    v_stack_m1E8 = v_xmm0;
    v_stack_m1D8 = v_xmm1;
    v_stack_m1C8 = v_xmm0;
loc_00A34592:
    if (v_stack_m1D0 != 0) goto loc_00A345A5;
    goto loc_00A34D5E;
loc_00A345A5:
    v_stack_m210 = 0;
    if (v_stack_m210 == 0) goto loc_00A34603;
    v_stack_m1F8 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = v_stack_m1F8;
    result = ObReferenceObjectByHandle(v_stack_m210, 1, *(unsigned __int64 *)(v_rip + 5842524), (unsigned __int8)((unsigned int)(0xC000021FULL)));
    v_stack_m210 = v_stack_m1F8;
    if (!sign_flag) goto loc_00A34619;
    goto loc_00A34D5E;
loc_00A34603:
    if (1 == 0) goto loc_00A34D59;
    v_stack_m1C8 = 0;
loc_00A34619:
    v_stack_m1A0 = v_stack_m1F8;
    v_stack_m278 = v_stack_m238;
    result = AlpcpLookupMessage(v_stack_m1F8, (unsigned int)(v_stack_m1D0), (unsigned int)(v_stack_m1C8), (unsigned __int8)((unsigned int)(0xC000021FULL)));
    if (sign_flag) goto loc_00A34687;
    v_r13 = v_stack_m1F8;
    if (v_stack_m1F8 == 0) {
        v_r13 = *(unsigned __int64 *)(v_stack_m238 + 16);
        v_stack_m210 = v_r13;
    }
    if (!sign_flag) goto loc_00A34670;
    goto loc_00A3468B;
loc_00A34670:
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m238 + 244)) & (0xFFFF00FFULL));
    if (((unsigned int)(result)) == 10) goto loc_00A346D1;
loc_00A34682:
loc_00A34687:
loc_00A3468B:
loc_00A34690:
    if (v_stack_m238 == 0) goto loc_00A34D19;
    if (v_stack_m240 != 0) {
        a2 = v_stack_m128;
        a1 = 0;
        result = AlpcpReleaseAttributes(a1, a2, (unsigned int)(v_stack_m1C8), (unsigned __int8)((unsigned int)(0xC000021FULL)));
        v_stack_m230 = 1;
    }
    if ((unsigned int)((unsigned int)(v_stack_m254)) == 0) goto loc_00A34D11;
    result = AlpcpCancelMessage(v_r13, v_stack_m238, (unsigned int)(0x10000ULL), (unsigned __int8)((unsigned int)(0xC000021FULL)));
    goto loc_00A34D19;
loc_00A346D1:
    if ((*(unsigned __int64 *)(v_stack_m238 + 16)) != (*(unsigned __int64 *)(v_stack_m238 + 192))) goto loc_00A34CFE;
    if ((*(unsigned __int64 *)(v_stack_m238 + 16)) == v_r13) goto loc_00A347CA;
    if ((((unsigned __int8)(v_r13)) & (7)) != 0) goto loc_00A347A2;
    v_stack_m218 = *(unsigned __int64 *)(v_stack_m238 + 24);
    if (*(unsigned __int64 *)(v_stack_m238 + 24) == 0) goto loc_00A34CFE;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 16) - 16, a2, a3, (unsigned __int8)((unsigned int)(0xC000021FULL)));
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m218 + 416))) >> (1));
    result = (unsigned int)((result) & (3));
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A34779;
    if (((unsigned int)(result)) != 1) goto loc_00A34779;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 16))) == v_r13) goto loc_00A34774;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 16) + 8)) == v_r13) goto loc_00A34774;
    goto loc_00A34781;
loc_00A34774:
    goto loc_00A34781;
loc_00A34779:
    v_rsi = ((*(unsigned __int64 *)(1 + 16)) == v_r13) ? 1 : 0;
loc_00A34781:
    result = result + 17;
    if ((*(unsigned __int64 *)(1 + 16)) != v_r13) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 16) - 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 16) - 16, a2, a3, a4);
    goto loc_00A347E4;
loc_00A347A2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r13 + 416))) & (6));
    if (((unsigned __int8)(result)) != 6) goto loc_00A34CFE;
    if (*(unsigned __int64 *)(v_r13 + 16) == 0) goto loc_00A34CFE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 16))) != 0) goto loc_00A34CFE;
loc_00A347CA:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 16) - 16))) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_00A34CFE;
    if (((unsigned __int8)(result)) < 3) goto loc_00A34CFE;
loc_00A347E4:
    if (1 == 0) goto loc_00A34CFE;
    result = AlpcpValidateConnectionMessage(v_r13, v_stack_m1E8, a12, a4);
    if (sign_flag) goto loc_00A34687;
    v_stack_m218 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 16);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m238 + 24) + 416)))) & (32)) == 0) goto loc_00A34836;
    goto loc_00A3468B;
loc_00A34836:
    if (((*(unsigned int *)(v_r13 + 256)) & (0x100000ULL)) != 0) goto loc_00A34862;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != (*(unsigned __int64 *)(v_r13 + 24))) goto loc_00A34682;
loc_00A34862:
    if (a9 != 0) goto loc_00A348F5;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(1 + 352, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = 1 + 352;
        a2 = result;
        a1 = 1 + 352;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 416))) | (16));
    *(unsigned int *)(1 + 416) = (unsigned int)(result);
    if (!(condition_is_above_or_equal)) {
        result = a6;
        *(unsigned __int64 *)(1 + 56) = result;
    }
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = 1 + 352;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(1 + 352, a2, a3, a4);
    goto loc_00A3468B;
loc_00A348F5:
    result = AlpcpCreatePort(v_stack_m258, v_stack_m1C0, v_stack_m248, a4);
    if (sign_flag) goto loc_00A34687;
    a3 = 0;
    result = AlpcpInitializePort(v_stack_m248, a3 + 3, a3, a4);
    if (sign_flag) goto loc_00A34D08;
    result = -(v_stack_m228);
    a2 = (a3 + 3) & (v_stack_m98);
    v_stack_m268 = a12;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    a4 = 0;
    result = AlpcpValidateAndSetPortAttributes(v_stack_m248, a2, v_r13, a4);
    if (sign_flag) goto loc_00A34D08;
    a2 = (a2) & (v_stack_m98);
    result = AlpcpSetOwnerProcessPort(v_stack_m248, a2, v_r13, a4);
    if (a12 != 0) {
    }
    result = AlpcpReferenceBlob(v_stack_m218, a2, v_r13, a4);
    result = AlpcpLockBlobExclusive(v_stack_m218, a2, v_r13, a4);
    *(unsigned __int64 *)(v_stack_m248 + 16) = v_stack_m218;
    *(unsigned __int64 *)(v_stack_m218 + 8) = v_stack_m248;
    *(unsigned __int64 *)(1 + 424) = v_r13;
    *(unsigned __int64 *)(1 + 432) = v_stack_m248;
    *(unsigned __int64 *)(v_stack_m248 + 424) = 1;
    *(unsigned __int64 *)(v_stack_m248 + 432) = 1;
    if ((((unsigned int)((unsigned int)(0x1000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(1 + 416))))) == 0) goto loc_00A34A13;
    if (((*(unsigned int *)(v_stack_m248 + 416)) & ((unsigned int)((unsigned int)(0x1000ULL)))) != 0) {
        result = 0x2000ULL;
        a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 416))) | ((unsigned int)(result)));
        *(unsigned int *)(1 + 416) = a2;
    }
    result = AlpcpUnlockBlobUncachedExclusive(v_stack_m218, a2, v_r13, a4);
    v_stack_mA4 = (unsigned __int16)(v_stack_m1E8 + 40);
    v_stack_mA2 = 11;
    v_stack_m270 = (unsigned __int8)(v_stack_m258);
    v_stack_m278 = 0;
    result = AlpcpSetupMessageDataForDeferredCopy(v_stack_m238, v_stack_m1B8, (unsigned int)(v_stack_m250), v_stack_m1E8);
    if (sign_flag) goto loc_00A34D08;
    if (a12 == 0) goto loc_00A34A9B;
    if ((*(unsigned __int64 *)(v_stack_m238 + 144)) == 0) goto loc_00A34A9B;
    result = AlpcpMapLegacyPortRemoteView(v_stack_m248, v_stack_m238 + 104, v_stack_m178, v_stack_m1E8);
    if (sign_flag) goto loc_00A34D08;
loc_00A34A9B:
    v_stack_m240 = 1;
    if (v_stack_m1F0 == 0) goto loc_00A34B0C;
    result = 0;
    v_stack_m190 = v_xmm0;
    v_stack_m180 = 0;
    result = AlpcpMapLegacyPortView(v_stack_m248, v_stack_m160, v_stack_m128, v_stack_m1E8);
    if (sign_flag) goto loc_00A34B32;
    result = AlpcpMapLegacyPortRemoteView(1, v_stack_m128, v_stack_m190, v_stack_m1E8);
    if (sign_flag) goto loc_00A34B32;
    v_stack_m138 = v_stack_m180;
    goto loc_00A34B32;
loc_00A34B0C:
    v_stack_m278 = v_stack_m128;
    result = AlpcpCaptureAttributes(v_r13, (unsigned int)(v_stack_m250), v_stack_m1B0, v_stack_m238);
loc_00A34B32:
    if (sign_flag) goto loc_00A34D08;
    result = ObfReferenceObject(v_stack_m248, (unsigned int)(v_stack_m250), v_stack_m1B0, v_stack_m238);
    v_stack_m268 = v_stack_m220;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    a4 = 0;
    a2 = 0;
    result = ObInsertObjectEx(v_stack_m248, a2, (unsigned int)(0x1F0001ULL), a4);
    if (sign_flag) goto loc_00A34D08;
    result = AlpcpReleaseAttributes(v_stack_m238, v_stack_m238 + 104, (unsigned int)(0x1F0001ULL), a4);
    *(unsigned __int64 *)(v_stack_m238 + 104) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m238 + 120) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m238 + 136) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m238 + 152) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m238 + 168) = v_xmm0;
    v_stack_m240 = 0;
    if (*(unsigned __int64 *)(v_stack_m238 + 208) != 0) {
        a2 = *(unsigned int *)(v_stack_m238 + 264);
        result = PsReleaseProcessWakeCounter(*(unsigned __int64 *)(v_stack_m238 + 208), a2, (unsigned int)(0x1F0001ULL), a4);
        *(unsigned __int64 *)(v_stack_m238 + 208) = 0;
    }
    if (*(unsigned __int64 *)(v_stack_m238 + 216) != 0) {
        a2 = *(unsigned int *)(v_stack_m238 + 264);
        result = PsReleaseProcessWakeCounter(*(unsigned __int64 *)(v_stack_m238 + 216), a2, (unsigned int)(0x1F0001ULL), a4);
        *(unsigned __int64 *)(v_stack_m238 + 216) = 0;
    }
    if (v_stack_m250 >= 0) goto loc_00A34C23;
    *(unsigned int *)(v_stack_m208) = (unsigned int)(v_stack_m220);
    goto loc_00A34C26;
loc_00A34C23:
    *(unsigned __int64 *)(v_stack_m208) = v_stack_m220;
loc_00A34C26:
    if (a6 == 0) { a6 = v_stack_m220; }
    *(unsigned __int64 *)(v_stack_m248 + 56) = a6;
    if (v_stack_m1F0 != 0) {
        *(unsigned __int64 *)(v_stack_m1F0) = v_xmm0;
        *(unsigned __int64 *)(v_stack_m1F0 + 16) = v_xmm1;
        *(unsigned __int64 *)(v_stack_m1F0 + 32) = v_xmm0;
    }
    if (v_stack_m1A8 != 0) {
        *(unsigned __int64 *)(v_stack_m1A8) = v_xmm0;
        *(unsigned __int64 *)(v_stack_m1A8 + 16) = v_xmm0;
    }
    goto loc_00A34CBB;
loc_00A34CBB:
    if (sign_flag) goto loc_00A34690;
    v_stack_mD8 = v_stack_m248;
    v_stack_mD0 = v_stack_m238;
    v_stack_mA8 = 0x10000ULL;
    result = AlpcpDispatchMessage(v_stack_mD8, a2, (unsigned int)(0x1F0001ULL), a4);
    if (!(sign_flag)) {
        v_stack_m220 = 0;
    }
    goto loc_00A34690;
loc_00A34CFE:
loc_00A34D08:
    goto loc_00A34690;
loc_00A34D11:
    result = AlpcpUnlockMessage(0, a2, (unsigned int)(0x1F0001ULL), a4);
loc_00A34D19:
    if (v_stack_m1A0 != 0) {
        result = ObfDereferenceObject(v_stack_m1A0, a2, (unsigned int)(0x1F0001ULL), a4);
    }
    if (v_stack_m248 == 0) goto loc_00A34D46;
    if (v_stack_m230 != 0) {
        a1 = v_stack_m248;
        result = AlpcpFlushResourcesPort(a1, a2, (unsigned int)(0x1F0001ULL), a4);
    }
    result = ObfDereferenceObject(v_stack_m248, a2, (unsigned int)(0x1F0001ULL), a4);
loc_00A34D46:
    if (v_stack_m220 != 0) {
        result = NtClose(v_stack_m220, a2, (unsigned int)(0x1F0001ULL), a4);
    }
    goto loc_00A34D5E;
loc_00A34D59:
loc_00A34D5E:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x1F0001ULL), a4);
    v_rsp = (v_rsp) + (608);
    return result;
loc_00A34D82:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned int)(0x1F0001ULL), a4);
loc_00A34D87:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned int)(0x1F0001ULL), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpAcceptConnectPort(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, void *Arg7, int64_t Arg8, uint8_t Arg9, int64_t Arg10, int64_t Arg11, uint8_t Arg12)
{
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m150;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint64_t v_stack_m190;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint32_t v_stack_m230;
    uint64_t v_stack_m238;
    uint32_t v_stack_m240;
    uint64_t v_stack_m248;
    uint32_t v_stack_m250;
    uint32_t v_stack_m254;
    uint8_t v_stack_m258;
    uint8_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA2;
    uint16_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (608);
    result = (*(uint64_t *)(v_rip + 0x3D6496)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1C0 = Arg4;
    v_stack_m210 = Arg3;
    v_stack_m250 = Arg2;
    v_stack_m208 = Arg1;
    v_stack_m1A8 = Arg11;
    v_stack_m1F0 = Arg10;
    v_stack_m228 = Arg5;
    v_stack_m1B8 = Arg7;
    v_stack_m1B0 = Arg8;
    Arg2 = 0;
    result = memset(v_stack_mD8, Arg2, Arg2 + 64, Arg4);
    result = 0;
    v_stack_m1E8 = v_xmm0;
    v_stack_m1D8 = v_xmm0;
    v_stack_m1C8 = 0;
    Arg2 = 0;
    result = memset(v_stack_m98, Arg2, (uint32_t)((uint32_t)(result + 72)), Arg4);
    Arg2 = 0;
    result = memset(v_stack_m128, Arg2, (uint32_t)((uint32_t)(result + 72)), Arg4);
    v_stack_m160 = v_xmm0;
    v_stack_m150 = v_xmm0;
    v_stack_m140 = v_xmm0;
    result = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = 0;
    local_rdi = 0;
    v_stack_m248 = 0;
    v_stack_m254 = 0;
    v_stack_m240 = 0;
    v_stack_m230 = 0;
    v_stack_m238 = 0;
    v_stack_m220 = 0;
    v_stack_m258 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00A3451F;
    if (Arg12 != 0) goto loc_00A34405;
    if (Arg9 != 0) goto loc_00A34405;
    goto loc_00A3444A;
loc_00A34405:
    if (!sign_flag) goto loc_00A34433;
    if (v_stack_m208 < Arg3) { Arg3 = v_stack_m208; }
    *(uint32_t *)(Arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3)));
    goto loc_00A3444A;
loc_00A34433:
    if (v_stack_m208 < Arg3) { Arg3 = v_stack_m208; }
    *(uint64_t *)(Arg3) = *(uint64_t *)(Arg3);
loc_00A3444A:
    result = AlpcpProbeAndCaptureMessageHeader(Arg7, v_stack_m1E8, (uint32_t)(v_stack_m250), Arg4);
    if (Arg5 != 0) {
        Arg2 = Arg3;
        if (Arg5 < Arg3) { Arg2 = Arg5; }
        Arg3 = 72;
        Arg1 = v_stack_m98;
        result = RtlCopyVolatileMemory(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg10 == 0) goto loc_00A344D0;
    if (Arg10 < Arg3) { Arg3 = Arg10; }
    result = RtlCopyVolatileMemory(v_stack_m160, Arg3, 48, Arg4);
    if (v_stack_m160 == 48) goto loc_00A344B2;
    goto loc_00A34D5E;
loc_00A344B2:
    if ((((uint8_t)(Arg10)) & (3)) != 0) goto loc_00A34D82;
    if (Arg10 < Arg3) { Arg3 = Arg10; }
    *(uint8_t *)(Arg3) = (uint8_t)(*(uint8_t *)(Arg3));
    *(uint8_t *)(Arg3 + 0x2F) = (uint8_t)(*(uint8_t *)(Arg3 + 0x2F));
loc_00A344D0:
    if (Arg11 == 0) goto loc_00A3450C;
    if (Arg11 < Arg3) { Arg3 = Arg11; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) == 24) goto loc_00A344F1;
    goto loc_00A34D5E;
loc_00A344F1:
    if ((((uint8_t)(Arg11)) & (3)) != 0) goto loc_00A34D87;
    if (Arg11 < Arg3) { Arg3 = Arg11; }
    *(uint8_t *)(Arg3) = (uint8_t)(*(uint8_t *)(Arg3));
    *(uint8_t *)(Arg3 + 0x17) = (uint8_t)(*(uint8_t *)(Arg3 + 0x17));
loc_00A3450C:
    goto loc_00A34592;
loc_00A3451F:
    if (Arg5 != 0) {
        v_stack_m98 = v_xmm0;
        v_stack_m88 = v_xmm1;
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm1;
        v_stack_m58 = v_xmm0;
    }
    v_stack_m1E8 = v_xmm0;
    v_stack_m1D8 = v_xmm1;
    v_stack_m1C8 = v_xmm0;
loc_00A34592:
    if (v_stack_m1D0 != 0) goto loc_00A345A5;
    goto loc_00A34D5E;
loc_00A345A5:
    v_stack_m210 = 0;
    if (v_stack_m210 == 0) goto loc_00A34603;
    v_stack_m1F8 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = v_stack_m1F8;
    result = ObReferenceObjectByHandle(v_stack_m210, 1, *(uint64_t *)(v_rip + 0x59265C), (uint8_t)((uint32_t)(0xC000021FULL)));
    v_stack_m210 = v_stack_m1F8;
    if (!sign_flag) goto loc_00A34619;
    goto loc_00A34D5E;
loc_00A34603:
    if (1 == 0) goto loc_00A34D59;
    v_stack_m1C8 = 0;
loc_00A34619:
    v_stack_m1A0 = v_stack_m1F8;
    v_stack_m278 = v_stack_m238;
    result = AlpcpLookupMessage(v_stack_m1F8, (uint32_t)(v_stack_m1D0), (uint32_t)(v_stack_m1C8), (uint8_t)((uint32_t)(0xC000021FULL)));
    if (sign_flag) goto loc_00A34687;
    local_r13 = v_stack_m1F8;
    if (v_stack_m1F8 == 0) {
        local_r13 = *(uint64_t *)(v_stack_m238 + 0x10);
        v_stack_m210 = local_r13;
    }
    if (!sign_flag) goto loc_00A34670;
    goto loc_00A3468B;
loc_00A34670:
    result = (uint32_t)((*(uint16_t *)(v_stack_m238 + 0xF4)) & (0xFFFF00FFULL));
    if (((uint32_t)(result)) == 10) goto loc_00A346D1;
loc_00A34682:
loc_00A34687:
loc_00A3468B:
loc_00A34690:
    if (v_stack_m238 == 0) goto loc_00A34D19;
    if (v_stack_m240 != 0) {
        Arg2 = v_stack_m128;
        Arg1 = 0;
        result = AlpcpReleaseAttributes(Arg1, Arg2, (uint32_t)(v_stack_m1C8), (uint8_t)((uint32_t)(0xC000021FULL)));
        v_stack_m230 = 1;
    }
    if ((uint32_t)((uint32_t)(v_stack_m254)) == 0) goto loc_00A34D11;
    result = AlpcpCancelMessage(local_r13, v_stack_m238, (uint32_t)(0x10000ULL), (uint8_t)((uint32_t)(0xC000021FULL)));
    goto loc_00A34D19;
loc_00A346D1:
    if ((*(uint64_t *)(v_stack_m238 + 0x10)) != (*(uint64_t *)(v_stack_m238 + 0xC0))) goto loc_00A34CFE;
    if ((*(uint64_t *)(v_stack_m238 + 0x10)) == local_r13) goto loc_00A347CA;
    if ((((uint8_t)(local_r13)) & (7)) != 0) goto loc_00A347A2;
    v_stack_m218 = *(uint64_t *)(v_stack_m238 + 0x18);
    if (*(uint64_t *)(v_stack_m238 + 0x18) == 0) goto loc_00A34CFE;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x10) - 16, Arg2, Arg3, (uint8_t)((uint32_t)(0xC000021FULL)));
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m218 + 0x1A0))) >> (1));
    result = (uint32_t)((result) & (3));
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A34779;
    if (((uint32_t)(result)) != 1) goto loc_00A34779;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x10))) == local_r13) goto loc_00A34774;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x10) + 0x8)) == local_r13) goto loc_00A34774;
    goto loc_00A34781;
loc_00A34774:
    goto loc_00A34781;
loc_00A34779:
    local_rsi = ((*(uint64_t *)(1 + 0x10)) == local_r13) ? 1 : 0;
loc_00A34781:
    result = result + 17;
    if ((*(uint64_t *)(1 + 0x10)) != local_r13) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x10) - 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x10) - 16, Arg2, Arg3, Arg4);
    goto loc_00A347E4;
loc_00A347A2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r13 + 0x1A0))) & (6));
    if (((uint8_t)(result)) != 6) goto loc_00A34CFE;
    if (*(uint64_t *)(local_r13 + 0x10) == 0) goto loc_00A34CFE;
    if ((*(uint64_t *)(*(uint64_t *)(local_r13 + 0x10))) != 0) goto loc_00A34CFE;
loc_00A347CA:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x10) - 16))) & (7));
    if (((uint8_t)(result)) != 3) goto loc_00A34CFE;
    if (((uint8_t)(result)) < 3) goto loc_00A34CFE;
loc_00A347E4:
    if (1 == 0) goto loc_00A34CFE;
    result = AlpcpValidateConnectionMessage(local_r13, v_stack_m1E8, Arg12, Arg4);
    if (sign_flag) goto loc_00A34687;
    v_stack_m218 = *(uint64_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x10);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m238 + 0x18) + 0x1A0)))) & (32)) == 0) goto loc_00A34836;
    goto loc_00A3468B;
loc_00A34836:
    if (((*(uint32_t *)(local_r13 + 0x100)) & (0x100000ULL)) != 0) goto loc_00A34862;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != (*(uint64_t *)(local_r13 + 0x18))) goto loc_00A34682;
loc_00A34862:
    if (Arg9 != 0) goto loc_00A348F5;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(1 + 352, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = 1 + 352;
        Arg2 = result;
        Arg1 = 1 + 352;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x1A0))) | (16));
    *(uint32_t *)(1 + 0x1A0) = (uint32_t)(result);
    if (!(condition_is_above_or_equal)) {
        result = Arg6;
        *(uint64_t *)(1 + 0x38) = result;
    }
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = 1 + 352;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(1 + 352, Arg2, Arg3, Arg4);
    goto loc_00A3468B;
loc_00A348F5:
    result = AlpcpCreatePort(v_stack_m258, v_stack_m1C0, v_stack_m248, Arg4);
    if (sign_flag) goto loc_00A34687;
    Arg3 = 0;
    result = AlpcpInitializePort(v_stack_m248, Arg3 + 3, Arg3, Arg4);
    if (sign_flag) goto loc_00A34D08;
    result = -(v_stack_m228);
    Arg2 = (Arg3 + 3) & (v_stack_m98);
    v_stack_m268 = Arg12;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    Arg4 = 0;
    result = AlpcpValidateAndSetPortAttributes(v_stack_m248, Arg2, local_r13, Arg4);
    if (sign_flag) goto loc_00A34D08;
    Arg2 = (Arg2) & (v_stack_m98);
    result = AlpcpSetOwnerProcessPort(v_stack_m248, Arg2, local_r13, Arg4);
    if (Arg12 != 0) {
    }
    result = AlpcpReferenceBlob(v_stack_m218, Arg2, local_r13, Arg4);
    result = AlpcpLockBlobExclusive(v_stack_m218, Arg2, local_r13, Arg4);
    *(uint64_t *)(v_stack_m248 + 0x10) = v_stack_m218;
    *(uint64_t *)(v_stack_m218 + 0x8) = v_stack_m248;
    *(uint64_t *)(1 + 0x1A8) = local_r13;
    *(uint64_t *)(1 + 0x1B0) = v_stack_m248;
    *(uint64_t *)(v_stack_m248 + 0x1A8) = 1;
    *(uint64_t *)(v_stack_m248 + 0x1B0) = 1;
    if ((((uint32_t)((uint32_t)(0x1000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x1A0))))) == 0) goto loc_00A34A13;
    if (((*(uint32_t *)(v_stack_m248 + 0x1A0)) & ((uint32_t)((uint32_t)(0x1000ULL)))) != 0) {
        result = 0x2000ULL;
        Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x1A0))) | ((uint32_t)(result)));
        *(uint32_t *)(1 + 0x1A0) = Arg2;
    }
    result = AlpcpUnlockBlobUncachedExclusive(v_stack_m218, Arg2, local_r13, Arg4);
    v_stack_mA4 = (uint16_t)(v_stack_m1E8 + 40);
    v_stack_mA2 = 11;
    v_stack_m270 = (uint8_t)(v_stack_m258);
    v_stack_m278 = 0;
    result = AlpcpSetupMessageDataForDeferredCopy(v_stack_m238, v_stack_m1B8, (uint32_t)(v_stack_m250), v_stack_m1E8);
    if (sign_flag) goto loc_00A34D08;
    if (Arg12 == 0) goto loc_00A34A9B;
    if ((*(uint64_t *)(v_stack_m238 + 0x90)) == 0) goto loc_00A34A9B;
    result = AlpcpMapLegacyPortRemoteView(v_stack_m248, v_stack_m238 + 104, v_stack_m178, v_stack_m1E8);
    if (sign_flag) goto loc_00A34D08;
loc_00A34A9B:
    v_stack_m240 = 1;
    if (v_stack_m1F0 == 0) goto loc_00A34B0C;
    result = 0;
    v_stack_m190 = v_xmm0;
    v_stack_m180 = 0;
    result = AlpcpMapLegacyPortView(v_stack_m248, v_stack_m160, v_stack_m128, v_stack_m1E8);
    if (sign_flag) goto loc_00A34B32;
    result = AlpcpMapLegacyPortRemoteView(1, v_stack_m128, v_stack_m190, v_stack_m1E8);
    if (sign_flag) goto loc_00A34B32;
    v_stack_m138 = v_stack_m180;
    goto loc_00A34B32;
loc_00A34B0C:
    v_stack_m278 = v_stack_m128;
    result = AlpcpCaptureAttributes(local_r13, (uint32_t)(v_stack_m250), v_stack_m1B0, v_stack_m238);
loc_00A34B32:
    if (sign_flag) goto loc_00A34D08;
    result = ObfReferenceObject(v_stack_m248, (uint32_t)(v_stack_m250), v_stack_m1B0, v_stack_m238);
    v_stack_m268 = v_stack_m220;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = ObInsertObjectEx(v_stack_m248, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
    if (sign_flag) goto loc_00A34D08;
    result = AlpcpReleaseAttributes(v_stack_m238, v_stack_m238 + 104, (uint32_t)(0x1F0001ULL), Arg4);
    *(uint64_t *)(v_stack_m238 + 0x68) = v_xmm0;
    *(uint64_t *)(v_stack_m238 + 0x78) = v_xmm1;
    *(uint64_t *)(v_stack_m238 + 0x88) = v_xmm0;
    *(uint64_t *)(v_stack_m238 + 0x98) = v_xmm1;
    *(uint64_t *)(v_stack_m238 + 0xA8) = v_xmm0;
    v_stack_m240 = 0;
    if (*(uint64_t *)(v_stack_m238 + 0xD0) != 0) {
        Arg2 = *(uint32_t *)(v_stack_m238 + 0x108);
        result = PsReleaseProcessWakeCounter(*(uint64_t *)(v_stack_m238 + 0xD0), Arg2, (uint32_t)(0x1F0001ULL), Arg4);
        *(uint64_t *)(v_stack_m238 + 0xD0) = 0;
    }
    if (*(uint64_t *)(v_stack_m238 + 0xD8) != 0) {
        Arg2 = *(uint32_t *)(v_stack_m238 + 0x108);
        result = PsReleaseProcessWakeCounter(*(uint64_t *)(v_stack_m238 + 0xD8), Arg2, (uint32_t)(0x1F0001ULL), Arg4);
        *(uint64_t *)(v_stack_m238 + 0xD8) = 0;
    }
    if (v_stack_m250 >= 0) goto loc_00A34C23;
    *(uint32_t *)(v_stack_m208) = (uint32_t)(v_stack_m220);
    goto loc_00A34C26;
loc_00A34C23:
    *(uint64_t *)(v_stack_m208) = v_stack_m220;
loc_00A34C26:
    if (Arg6 == 0) { Arg6 = v_stack_m220; }
    *(uint64_t *)(v_stack_m248 + 0x38) = Arg6;
    if (v_stack_m1F0 != 0) {
        *(uint64_t *)(v_stack_m1F0) = v_xmm0;
        *(uint64_t *)(v_stack_m1F0 + 0x10) = v_xmm1;
        *(uint64_t *)(v_stack_m1F0 + 0x20) = v_xmm0;
    }
    if (v_stack_m1A8 != 0) {
        *(uint64_t *)(v_stack_m1A8) = v_xmm0;
        *(uint64_t *)(v_stack_m1A8 + 0x10) = v_xmm0;
    }
    goto loc_00A34CBB;
loc_00A34CBB:
    if (sign_flag) goto loc_00A34690;
    v_stack_mD8 = v_stack_m248;
    v_stack_mD0 = v_stack_m238;
    v_stack_mA8 = 0x10000ULL;
    result = AlpcpDispatchMessage(v_stack_mD8, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
    if (!(sign_flag)) {
        v_stack_m220 = 0;
    }
    goto loc_00A34690;
loc_00A34CFE:
loc_00A34D08:
    goto loc_00A34690;
loc_00A34D11:
    result = AlpcpUnlockMessage(0, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
loc_00A34D19:
    if (v_stack_m1A0 != 0) {
        result = ObfDereferenceObject(v_stack_m1A0, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
    }
    if (v_stack_m248 == 0) goto loc_00A34D46;
    if (v_stack_m230 != 0) {
        Arg1 = v_stack_m248;
        result = AlpcpFlushResourcesPort(Arg1, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
    }
    result = ObfDereferenceObject(v_stack_m248, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
loc_00A34D46:
    if (v_stack_m220 != 0) {
        result = NtClose(v_stack_m220, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
    }
    goto loc_00A34D5E;
loc_00A34D59:
loc_00A34D5E:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
    local_rsp = (local_rsp) + (608);
    return result;
loc_00A34D82:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
loc_00A34D87:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint32_t)(0x1F0001ULL), Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `128` | `R` |
| `Arg7` | `+ 0x10` | `128` | `R` |
| `Arg7` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A34290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
