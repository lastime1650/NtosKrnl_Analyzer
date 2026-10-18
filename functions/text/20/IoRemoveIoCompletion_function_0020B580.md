# IoRemoveIoCompletion

- RVA: `0x0020B580`–`0x0020BD2A` (길이 `1,962` bytes)
- VA: `0x000000014020B580`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005D828`
- 디코드: `449`개 명령, `1,962/1,962` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0020B60D` → [KeRemoveQueueEx](KeRemoveQueueEx_function_0020BD30.md) (function, `0x0020BD30`)
- `0x0020B644` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0020B73D` → [IopCompleteRequest](IopCompleteRequest_function_0020AF50.md) (function, `0x0020AF50`)
- `0x0020B76C` → [IopFreeMiniCompletionPacket](../../page/9A/IopFreeMiniCompletionPacket_function_009A82D0.md) (function, `0x009A82D0`)
- `0x0020B854` → [IoFreeIrp](../24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0020B8BD` → [KiAcquireSpinLockInstrumented](KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x0020B8F7` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020B92B` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0020B972` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0020B9B1` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0020B9F4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020BA15` → [KxWaitForSpinLockAndAcquire](KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x0020BA3F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020BA65` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020BA70` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020BAB4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020BAF4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020BB37` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020BB54` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x0020BB88` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x0020BB92` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x0020BBBD` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x0020BBDB` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x0020BC0F` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x0020BC19` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x0020BC44` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x0020BC62` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x0020BC96` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x0020BCA1` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x0020BCCD` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x0020BCEE` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x0020BCFB` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x0020BD08` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x0020BD16` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)

### Direct callers
- [NtWaitForWorkViaWorkerFactory](../39/NtWaitForWorkViaWorkerFactory_function_00394270.md) at `0x0039492A`
- [NtRemoveIoCompletionEx](../../page/8E/NtRemoveIoCompletionEx_function_008E8760.md) at `0x008E8881`
- [NtRemoveIoCompletion](../../page/99/NtRemoveIoCompletion_function_0099C8B0.md) at `0x0099C9DA`

### Static image references
- `0x0020B593` → RVA `0x00E0A740` (`.data`; read)
- `0x0020B891` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0020B89E` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0020B8AB` → RVA `0x00F0DE58` (`.data`; read)
- `0x0020B90F` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0020BA8C` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0020BAA1` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x0020B76C` → [IopFreeMiniCompletionPacket](../../page/9A/IopFreeMiniCompletionPacket_function_009A82D0.md) (`.text` → `PAGE`)
  - `0x0020BB88` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x0020BB92` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x0020BBBD` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
  - `0x0020BC0F` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x0020BC19` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x0020BC44` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
  - `0x0020BC96` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x0020BCA1` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x0020BCCD` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0020B715` → [sub_006D6658](../6D/Unknown_function_006D6658.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020B580  40 53                           push rbx
0020B582  56                              push rsi
0020B583  57                              push rdi
0020B584  41 54                           push r12
0020B586  41 55                           push r13
0020B588  41 56                           push r14
0020B58A  41 57                           push r15
0020B58C  48 81 EC E0 00 00 00            sub rsp, 0xe0
0020B593  48 8B 05 A6 F1 BF 00            mov rax, qword ptr [rip + 0xbff1a6]
0020B59A  48 33 C4                        xor rax, rsp
0020B59D  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0020B5A5  45 8B D1                        mov r10d, r9d
0020B5A8  49 8B F8                        mov rdi, r8
0020B5AB  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0020B5B0  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
0020B5B5  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0020B5BA  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
0020B5C2  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
0020B5CA  4C 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], r8
0020B5D2  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
0020B5DA  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0020B5E2  4C 8B 8C 24 50 01 00 00         mov r9, qword ptr [rsp + 0x150]
0020B5EA  0F 57 C0                        xorps xmm0, xmm0
0020B5ED  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0020B5F2  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
0020B5F7  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0020B5FC  44 0F B6 84 24 58 01 00 00      movzx r8d, byte ptr [rsp + 0x158]
0020B605  0F B6 94 24 48 01 00 00         movzx edx, byte ptr [rsp + 0x148]
0020B60D  E8 1E 07 00 00                  call 0x14020bd30
0020B612  8B F0                           mov esi, eax
0020B614  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0020B618  33 C0                           xor eax, eax
0020B61A  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0020B61E  33 DB                           xor ebx, ebx
0020B620  8D 48 02                        lea ecx, [rax + 2]
0020B623  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
0020B627  3B DE                           cmp ebx, esi
0020B629  72 32                           jb 0x14020b65d
0020B62B  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
0020B62F  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0020B637  89 31                           mov dword ptr [rcx], esi
0020B639  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0020B641  48 33 CC                        xor rcx, rsp
0020B644  E8 F7 0F 4A 00                  call 0x1406ac640
0020B649  48 81 C4 E0 00 00 00            add rsp, 0xe0
0020B650  41 5F                           pop r15
0020B652  41 5E                           pop r14
0020B654  41 5D                           pop r13
0020B656  41 5C                           pop r12
0020B658  5F                              pop rdi
0020B659  5E                              pop rsi
0020B65A  5B                              pop rbx
0020B65B  C3                              ret
0020B65C  CC                              int3
0020B65D  44 8B F3                        mov r14d, ebx
0020B660  48 8B 3C DF                     mov rdi, qword ptr [rdi + rbx*8]
0020B664  48 81 FF 80 00 00 00            cmp rdi, 0x80
0020B66B  0F 84 9B 01 00 00               je 0x14020b80c
0020B671  48 81 FF C0 00 00 00            cmp rdi, 0xc0
0020B678  0F 84 8E 01 00 00               je 0x14020b80c
0020B67E  48 8D 87 FF FE FF FF            lea rax, [rdi - 0x101]
0020B685  48 83 F8 01                     cmp rax, 1
0020B689  0F 86 7D 01 00 00               jbe 0x14020b80c
0020B68F  0F B6 47 10                     movzx eax, byte ptr [rdi + 0x10]
0020B693  84 C0                           test al, al
0020B695  0F 85 AE 00 00 00               jne 0x14020b749
0020B69B  48 81 C7 58 FF FF FF            add rdi, -0xa8
0020B6A2  4C 8B 6F 60                     mov r13, qword ptr [rdi + 0x60]
0020B6A6  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
0020B6AB  4C 8B 6F 78                     mov r13, qword ptr [rdi + 0x78]
0020B6AF  0F 10 47 30                     movups xmm0, xmmword ptr [rdi + 0x30]
0020B6B3  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0020B6B8  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0020B6BB  0F BA E0 0D                     bt eax, 0xd
0020B6BF  0F 83 50 01 00 00               jae 0x14020b815
0020B6C5  48 C7 84 24 80 00 00 00 00 00 00 00  mov qword ptr [rsp + 0x80], 0
0020B6D1  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
0020B6DA  4C 8B 7F 58                     mov r15, qword ptr [rdi + 0x58]
0020B6DE  49 83 E7 F9                     and r15, 0xfffffffffffffff9
0020B6E2  0F 57 C0                        xorps xmm0, xmm0
0020B6E5  0F 11 84 24 A8 00 00 00         movups xmmword ptr [rsp + 0xa8], xmm0
0020B6ED  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
0020B6F5  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
0020B6FD  48 C7 47 60 00 00 00 00         mov qword ptr [rdi + 0x60], 0
0020B705  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0020B70E  4C 3B B8 B8 00 00 00            cmp r15, qword ptr [rax + 0xb8]
0020B715  0F 85 3D AF 4C 00               jne 0x1406d6658
0020B71B  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0020B720  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0020B725  4C 8D 8F C0 00 00 00            lea r9, [rdi + 0xc0]
0020B72C  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
0020B731  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
0020B739  48 8D 4F 78                     lea rcx, [rdi + 0x78]
0020B73D  E8 0E F8 FF FF                  call 0x14020af50
0020B742  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
0020B747  EB 28                           jmp 0x14020b771
0020B749  3C 02                           cmp al, 2
0020B74B  0F 84 12 01 00 00               je 0x14020b863
0020B751  4C 8B 67 20                     mov r12, qword ptr [rdi + 0x20]
0020B755  4C 8B 6F 18                     mov r13, qword ptr [rdi + 0x18]
0020B759  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
0020B75C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0020B760  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
0020B764  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0020B769  48 8B CF                        mov rcx, rdi
0020B76C  E8 5F CB 79 00                  call 0x1409a82d0
0020B771  80 BC 24 48 01 00 00 00         cmp byte ptr [rsp + 0x148], 0
0020B779  74 68                           je 0x14020b7e3
0020B77B  49 C1 E6 05                     shl r14, 5
0020B77F  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
0020B784  4F 89 2C 3E                     mov qword ptr [r14 + r15], r13
0020B788  4F 89 64 3E 08                  mov qword ptr [r14 + r15 + 8], r12
0020B78D  0F 10 44 24 50                  movups xmm0, xmmword ptr [rsp + 0x50]
0020B792  43 0F 11 44 3E 10               movups xmmword ptr [r14 + r15 + 0x10], xmm0
0020B798  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0020B79D  B9 02 00 00 00                  mov ecx, 2
0020B7A2  EB 38                           jmp 0x14020b7dc
0020B7A4  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0020B7A8  B9 02 00 00 00                  mov ecx, 2
0020B7AD  8B 74 24 60                     mov esi, dword ptr [rsp + 0x60]
0020B7B1  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
0020B7B5  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0020B7BD  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0020B7C2  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0020B7CA  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0020B7CF  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
0020B7D7  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0020B7DC  FF C3                           inc ebx
0020B7DE  E9 40 FE FF FF                  jmp 0x14020b623
0020B7E3  49 C1 E6 05                     shl r14, 5
0020B7E7  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0020B7EC  4D 89 2C 06                     mov qword ptr [r14 + rax], r13
0020B7F0  4D 89 64 06 08                  mov qword ptr [r14 + rax + 8], r12
0020B7F5  0F 10 44 24 50                  movups xmm0, xmmword ptr [rsp + 0x50]
0020B7FA  41 0F 11 44 06 10               movups xmmword ptr [r14 + rax + 0x10], xmm0
0020B800  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0020B805  B9 02 00 00 00                  mov ecx, 2
0020B80A  EB D0                           jmp 0x14020b7dc
0020B80C  33 F6                           xor esi, esi
0020B80E  8B C7                           mov eax, edi
0020B810  E9 1A FE FF FF                  jmp 0x14020b62f
0020B815  0F BA E0 0F                     bt eax, 0xf
0020B819  73 36                           jae 0x14020b851
0020B81B  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
0020B81F  4C 8B C0                        mov r8, rax
0020B822  4C 8B C8                        mov r9, rax
0020B825  49 D1 E9                        shr r9, 1
0020B828  41 83 E1 03                     and r9d, 3
0020B82C  49 FF C9                        dec r9
0020B82F  4B 8D 14 09                     lea rdx, [r9 + r9]
0020B833  48 8B C8                        mov rcx, rax
0020B836  48 83 E1 F9                     and rcx, 0xfffffffffffffff9
0020B83A  48 0B D1                        or rdx, rcx
0020B83D  F0 48 0F B1 57 58               lock cmpxchg qword ptr [rdi + 0x58], rdx
0020B843  4C 3B C0                        cmp r8, rax
0020B846  75 D7                           jne 0x14020b81f
0020B848  45 85 C9                        test r9d, r9d
0020B84B  0F 85 CF 04 00 00               jne 0x14020bd20
0020B851  48 8B CF                        mov rcx, rdi
0020B854  E8 17 27 04 00                  call 0x14024df70
0020B859  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
0020B85E  E9 0E FF FF FF                  jmp 0x14020b771
0020B863  4C 8B 67 38                     mov r12, qword ptr [rdi + 0x38]
0020B867  4C 8B 6F 30                     mov r13, qword ptr [rdi + 0x30]
0020B86B  8B 47 48                        mov eax, dword ptr [rdi + 0x48]
0020B86E  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0020B872  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020B876  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0020B87B  48 8B 47 50                     mov rax, qword ptr [rdi + 0x50]
0020B87F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0020B884  44 0F 20 C0                     mov rax, cr8
0020B888  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0020B88D  44 0F 22 C1                     mov cr8, rcx
0020B891  83 3D 88 B4 DB 00 00            cmp dword ptr [rip + 0xdbb488], 0
0020B898  0F 85 CD 01 00 00               jne 0x14020ba6b
0020B89E  F6 05 61 B2 DB 00 21            test byte ptr [rip + 0xdbb261], 0x21
0020B8A5  0F 84 4F 01 00 00               je 0x14020b9fa
0020B8AB  8B 05 A7 25 D0 00               mov eax, dword ptr [rip + 0xd025a7]
0020B8B1  85 C0                           test eax, eax
0020B8B3  0F 85 41 01 00 00               jne 0x14020b9fa
0020B8B9  48 8D 4F 60                     lea rcx, [rdi + 0x60]
0020B8BD  E8 2E CC FF FF                  call 0x1402084f0
0020B8C2  C6 47 68 00                     mov byte ptr [rdi + 0x68], 0
0020B8C6  48 C7 47 58 00 00 00 00         mov qword ptr [rdi + 0x58], 0
0020B8CE  F6 05 31 B2 DB 00 01            test byte ptr [rip + 0xdbb231], 1
0020B8D5  0F 85 F9 03 00 00               jne 0x14020bcd4
0020B8DB  F0 48 83 67 60 00               lock and qword ptr [rdi + 0x60], 0
0020B8E1  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
0020B8E6  83 3D 33 B4 DB 00 00            cmp dword ptr [rip + 0xdbb433], 0
0020B8ED  74 0D                           je 0x14020b8fc
0020B8EF  44 0F 20 C1                     mov rcx, cr8
0020B8F3  41 0F B6 D7                     movzx edx, r15b
0020B8F7  E8 9C 9D 2E 00                  call 0x1404f5698
0020B8FC  41 0F B6 C7                     movzx eax, r15b
0020B900  44 0F 22 C0                     mov cr8, rax
0020B904  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0020B909  4D 8D 78 D0                     lea r15, [r8 - 0x30]
0020B90D  33 C0                           xor eax, eax
0020B90F  39 05 FB 96 DB 00               cmp dword ptr [rip + 0xdb96fb], eax
0020B915  0F 95 C0                        setne al
0020B918  85 C0                           test eax, eax
0020B91A  74 19                           je 0x14020b935
0020B91C  33 D2                           xor edx, edx
0020B91E  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0020B924  44 8D 42 01                     lea r8d, [rdx + 1]
0020B928  49 8B CF                        mov rcx, r15
0020B92B  E8 B4 50 00 00                  call 0x1402109e4
0020B930  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0020B935  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0020B93C  F0 49 0F C1 07                  lock xadd qword ptr [r15], rax
0020B941  48 83 E8 01                     sub rax, 1
0020B945  0F 8E D4 00 00 00               jle 0x14020ba1f
0020B94B  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0020B950  4D 8D 78 D0                     lea r15, [r8 - 0x30]
0020B954  33 C0                           xor eax, eax
0020B956  39 05 B4 96 DB 00               cmp dword ptr [rip + 0xdb96b4], eax
0020B95C  0F 95 C0                        setne al
0020B95F  85 C0                           test eax, eax
0020B961  74 19                           je 0x14020b97c
0020B963  33 D2                           xor edx, edx
0020B965  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0020B96B  44 8D 42 01                     lea r8d, [rdx + 1]
0020B96F  49 8B CF                        mov rcx, r15
0020B972  E8 6D 50 00 00                  call 0x1402109e4
0020B977  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
0020B97C  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0020B983  F0 49 0F C1 07                  lock xadd qword ptr [r15], rax
0020B988  48 83 E8 01                     sub rax, 1
0020B98C  0F 8E B3 00 00 00               jle 0x14020ba45
0020B992  33 C0                           xor eax, eax
0020B994  39 05 76 96 DB 00               cmp dword ptr [rip + 0xdb9676], eax
0020B99A  0F 95 C0                        setne al
0020B99D  85 C0                           test eax, eax
0020B99F  74 15                           je 0x14020b9b6
0020B9A1  33 D2                           xor edx, edx
0020B9A3  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0020B9A9  44 8D 42 01                     lea r8d, [rdx + 1]
0020B9AD  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0020B9B1  E8 2E 50 00 00                  call 0x1402109e4
0020B9B6  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0020B9BD  F0 48 0F C1 47 D0               lock xadd qword ptr [rdi - 0x30], rax
0020B9C3  48 83 E8 01                     sub rax, 1
0020B9C7  0F 8F A4 FD FF FF               jg 0x14020b771
0020B9CD  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
0020B9D1  48 85 C9                        test rcx, rcx
0020B9D4  0F 85 20 01 00 00               jne 0x14020bafa
0020B9DA  48 85 C0                        test rax, rax
0020B9DD  0F 89 68 02 00 00               jns 0x14020bc4b
0020B9E3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0020B9E8  44 8D 49 02                     lea r9d, [rcx + 2]
0020B9EC  4C 8B C7                        mov r8, rdi
0020B9EF  33 D2                           xor edx, edx
0020B9F1  8D 4A 18                        lea ecx, [rdx + 0x18]
0020B9F4  E8 67 1C 2F 00                  call 0x1404fd660
0020B9F9  CC                              int3
0020B9FA  F0 48 0F BA 6F 60 00            lock bts qword ptr [rdi + 0x60], 0
0020BA01  B8 00 00 00 00                  mov eax, 0
0020BA06  0F 93 C0                        setae al
0020BA09  85 C0                           test eax, eax
0020BA0B  0F 85 B1 FE FF FF               jne 0x14020b8c2
0020BA11  48 8D 4F 60                     lea rcx, [rdi + 0x60]
0020BA15  E8 A6 CB FF FF                  call 0x1402085c0
0020BA1A  E9 A3 FE FF FF                  jmp 0x14020b8c2
0020BA1F  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
0020BA23  48 85 C9                        test rcx, rcx
0020BA26  75 52                           jne 0x14020ba7a
0020BA28  48 85 C0                        test rax, rax
0020BA2B  0F 89 0C 01 00 00               jns 0x14020bb3d
0020BA31  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0020BA36  33 D2                           xor edx, edx
0020BA38  8D 4A 18                        lea ecx, [rdx + 0x18]
0020BA3B  44 8D 4A 02                     lea r9d, [rdx + 2]
0020BA3F  E8 1C 1C 2F 00                  call 0x1404fd660
0020BA44  CC                              int3
0020BA45  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
0020BA49  48 85 C9                        test rcx, rcx
0020BA4C  75 6C                           jne 0x14020baba
0020BA4E  48 85 C0                        test rax, rax
0020BA51  0F 89 6D 01 00 00               jns 0x14020bbc4
0020BA57  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0020BA5C  33 D2                           xor edx, edx
0020BA5E  8D 4A 18                        lea ecx, [rdx + 0x18]
0020BA61  44 8D 4A 02                     lea r9d, [rdx + 2]
0020BA65  E8 F6 1B 2F 00                  call 0x1404fd660
0020BA6A  CC                              int3
0020BA6B  B2 02                           mov dl, 2
0020BA6D  0F B6 C8                        movzx ecx, al
0020BA70  E8 87 9C 2E 00                  call 0x1404f56fc
0020BA75  E9 24 FE FF FF                  jmp 0x14020b89e
0020BA7A  49 8B C7                        mov rax, r15
0020BA7D  48 C1 E8 08                     shr rax, 8
0020BA81  0F B6 D0                        movzx edx, al
0020BA84  41 0F B6 47 18                  movzx eax, byte ptr [r15 + 0x18]
0020BA89  48 33 D0                        xor rdx, rax
0020BA8C  0F B6 05 B9 B3 DB 00            movzx eax, byte ptr [rip + 0xdbb3b9]
0020BA93  48 33 D0                        xor rdx, rax
0020BA96  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0020BA9B  41 B9 01 00 00 00               mov r9d, 1
0020BAA1  48 8D 05 58 45 DF FF            lea rax, [rip - 0x20baa8]
0020BAA8  48 8B 94 D0 00 78 FC 00         mov rdx, qword ptr [rax + rdx*8 + 0xfc7800]
0020BAB0  41 8D 49 17                     lea ecx, [r9 + 0x17]
0020BAB4  E8 A7 1B 2F 00                  call 0x1404fd660
0020BAB9  CC                              int3
0020BABA  49 8B C7                        mov rax, r15
0020BABD  48 C1 E8 08                     shr rax, 8
0020BAC1  0F B6 D0                        movzx edx, al
0020BAC4  41 0F B6 47 18                  movzx eax, byte ptr [r15 + 0x18]
0020BAC9  48 33 D0                        xor rdx, rax
0020BACC  0F B6 05 79 B3 DB 00            movzx eax, byte ptr [rip + 0xdbb379]
0020BAD3  48 33 D0                        xor rdx, rax
0020BAD6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0020BADB  41 B9 01 00 00 00               mov r9d, 1
0020BAE1  48 8D 05 18 45 DF FF            lea rax, [rip - 0x20bae8]
0020BAE8  48 8B 94 D0 00 78 FC 00         mov rdx, qword ptr [rax + rdx*8 + 0xfc7800]
0020BAF0  41 8D 49 17                     lea ecx, [r9 + 0x17]
0020BAF4  E8 67 1B 2F 00                  call 0x1404fd660
0020BAF9  CC                              int3
0020BAFA  48 8D 47 D0                     lea rax, [rdi - 0x30]
0020BAFE  48 C1 E8 08                     shr rax, 8
0020BB02  0F B6 D0                        movzx edx, al
0020BB05  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
0020BB09  48 33 D0                        xor rdx, rax
0020BB0C  0F B6 05 39 B3 DB 00            movzx eax, byte ptr [rip + 0xdbb339]
0020BB13  48 33 D0                        xor rdx, rax
0020BB16  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0020BB1B  41 B9 01 00 00 00               mov r9d, 1
0020BB21  4C 8B C7                        mov r8, rdi
0020BB24  48 8D 05 D5 44 DF FF            lea rax, [rip - 0x20bb2b]
0020BB2B  48 8B 94 D0 00 78 FC 00         mov rdx, qword ptr [rax + rdx*8 + 0xfc7800]
0020BB33  41 8D 49 17                     lea ecx, [r9 + 0x17]
0020BB37  E8 24 1B 2F 00                  call 0x1404fd660
0020BB3C  CC                              int3
0020BB3D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0020BB46  66 83 B8 E6 01 00 00 00         cmp word ptr [rax + 0x1e6], 0
0020BB4E  0F 85 A4 01 00 00               jne 0x14020bcf8
0020BB54  E8 07 C5 0E 00                  call 0x1402f8060
0020BB59  84 C0                           test al, al
0020BB5B  0F 84 97 01 00 00               je 0x14020bcf8
0020BB61  44 0F 20 C0                     mov rax, cr8
0020BB65  3C 01                           cmp al, 1
0020BB67  0F 83 8B 01 00 00               jae 0x14020bcf8
0020BB6D  41 0F B6 47 1A                  movzx eax, byte ptr [r15 + 0x1a]
0020BB72  A8 40                           test al, 0x40
0020BB74  75 26                           jne 0x14020bb9c
0020BB76  33 C0                           xor eax, eax
0020BB78  39 05 92 94 DB 00               cmp dword ptr [rip + 0xdb9492], eax
0020BB7E  0F 95 C0                        setne al
0020BB81  85 C0                           test eax, eax
0020BB83  74 08                           je 0x14020bb8d
0020BB85  49 8B CF                        mov rcx, r15
0020BB88  E8 EB C3 7C 00                  call 0x1409d7f78
0020BB8D  33 D2                           xor edx, edx
0020BB8F  49 8B CF                        mov rcx, r15
0020BB92  E8 C9 8E 65 00                  call 0x140864a60
0020BB97  E9 AF FD FF FF                  jmp 0x14020b94b
0020BB9C  83 E0 7F                        and eax, 0x7f
0020BB9F  48 8D 0D 5A 44 DF FF            lea rcx, [rip - 0x20bba6]
0020BBA6  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0020BBAE  49 8B CF                        mov rcx, r15
0020BBB1  48 2B C8                        sub rcx, rax
0020BBB4  48 8B 09                        mov rcx, qword ptr [rcx]
0020BBB7  80 79 18 00                     cmp byte ptr [rcx + 0x18], 0
0020BBBB  74 B9                           je 0x14020bb76
0020BBBD  E8 6E C2 7C 00                  call 0x1409d7e30
0020BBC2  EB B2                           jmp 0x14020bb76
0020BBC4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0020BBCD  66 83 B8 E6 01 00 00 00         cmp word ptr [rax + 0x1e6], 0
0020BBD5  0F 85 2A 01 00 00               jne 0x14020bd05
0020BBDB  E8 80 C4 0E 00                  call 0x1402f8060
0020BBE0  84 C0                           test al, al
0020BBE2  0F 84 1D 01 00 00               je 0x14020bd05
0020BBE8  44 0F 20 C0                     mov rax, cr8
0020BBEC  3C 01                           cmp al, 1
0020BBEE  0F 83 11 01 00 00               jae 0x14020bd05
0020BBF4  41 0F B6 47 1A                  movzx eax, byte ptr [r15 + 0x1a]
0020BBF9  A8 40                           test al, 0x40
0020BBFB  75 26                           jne 0x14020bc23
0020BBFD  33 C0                           xor eax, eax
0020BBFF  39 05 0B 94 DB 00               cmp dword ptr [rip + 0xdb940b], eax
0020BC05  0F 95 C0                        setne al
0020BC08  85 C0                           test eax, eax
0020BC0A  74 08                           je 0x14020bc14
0020BC0C  49 8B CF                        mov rcx, r15
0020BC0F  E8 64 C3 7C 00                  call 0x1409d7f78
0020BC14  33 D2                           xor edx, edx
0020BC16  49 8B CF                        mov rcx, r15
0020BC19  E8 42 8E 65 00                  call 0x140864a60
0020BC1E  E9 6F FD FF FF                  jmp 0x14020b992
0020BC23  83 E0 7F                        and eax, 0x7f
0020BC26  48 8D 0D D3 43 DF FF            lea rcx, [rip - 0x20bc2d]
0020BC2D  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0020BC35  49 8B CF                        mov rcx, r15
0020BC38  48 2B C8                        sub rcx, rax
0020BC3B  48 8B 09                        mov rcx, qword ptr [rcx]
0020BC3E  80 79 18 00                     cmp byte ptr [rcx + 0x18], 0
0020BC42  74 B9                           je 0x14020bbfd
0020BC44  E8 E7 C1 7C 00                  call 0x1409d7e30
0020BC49  EB B2                           jmp 0x14020bbfd
0020BC4B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0020BC54  66 83 B8 E6 01 00 00 00         cmp word ptr [rax + 0x1e6], 0
0020BC5C  0F 85 B0 00 00 00               jne 0x14020bd12
0020BC62  E8 F9 C3 0E 00                  call 0x1402f8060
0020BC67  84 C0                           test al, al
0020BC69  0F 84 A3 00 00 00               je 0x14020bd12
0020BC6F  44 0F 20 C0                     mov rax, cr8
0020BC73  3C 01                           cmp al, 1
0020BC75  0F 83 97 00 00 00               jae 0x14020bd12
0020BC7B  0F B6 47 EA                     movzx eax, byte ptr [rdi - 0x16]
0020BC7F  A8 40                           test al, 0x40
0020BC81  75 28                           jne 0x14020bcab
0020BC83  33 C0                           xor eax, eax
0020BC85  39 05 85 93 DB 00               cmp dword ptr [rip + 0xdb9385], eax
0020BC8B  0F 95 C0                        setne al
0020BC8E  85 C0                           test eax, eax
0020BC90  74 09                           je 0x14020bc9b
0020BC92  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0020BC96  E8 DD C2 7C 00                  call 0x1409d7f78
0020BC9B  33 D2                           xor edx, edx
0020BC9D  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0020BCA1  E8 BA 8D 65 00                  call 0x140864a60
0020BCA6  E9 C6 FA FF FF                  jmp 0x14020b771
0020BCAB  83 E0 7F                        and eax, 0x7f
0020BCAE  48 8D 0D 4B 43 DF FF            lea rcx, [rip - 0x20bcb5]
0020BCB5  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0020BCBD  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0020BCC1  48 2B C8                        sub rcx, rax
0020BCC4  48 8B 09                        mov rcx, qword ptr [rcx]
0020BCC7  80 79 18 00                     cmp byte ptr [rcx + 0x18], 0
0020BCCB  74 B6                           je 0x14020bc83
0020BCCD  E8 5E C1 7C 00                  call 0x1409d7e30
0020BCD2  EB AF                           jmp 0x14020bc83
0020BCD4  8B 05 7E 21 D0 00               mov eax, dword ptr [rip + 0xd0217e]
0020BCDA  85 C0                           test eax, eax
0020BCDC  0F 85 F9 FB FF FF               jne 0x14020b8db
0020BCE2  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
0020BCEA  48 8D 4F 60                     lea rcx, [rdi + 0x60]
0020BCEE  E8 FD 71 18 00                  call 0x140392ef0
0020BCF3  E9 E9 FB FF FF                  jmp 0x14020b8e1
0020BCF8  49 8B CF                        mov rcx, r15
0020BCFB  E8 94 66 19 00                  call 0x1403a2394
0020BD00  E9 46 FC FF FF                  jmp 0x14020b94b
0020BD05  49 8B CF                        mov rcx, r15
0020BD08  E8 87 66 19 00                  call 0x1403a2394
0020BD0D  E9 80 FC FF FF                  jmp 0x14020b992
0020BD12  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0020BD16  E8 79 66 19 00                  call 0x1403a2394
0020BD1B  E9 51 FA FF FF                  jmp 0x14020b771
0020BD20  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
0020BD25  E9 47 FA FF FF                  jmp 0x14020b771
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoRemoveIoCompletion(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned __int8 a6, __int64 a7, unsigned __int8 a8)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC8;

    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 12579238)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mA0 = a3;
    v_stack_mA8 = a2;
    v_stack_mB0 = a1;
    v_stack_m90 = a1;
    v_stack_m88 = a2;
    v_stack_m80 = a3;
    v_stack_m78 = a5;
    v_stack_mC8 = v_xmm0;
    v_stack_mF0 = (unsigned int)((unsigned int)(a4));
    v_stack_mF8 = a3;
    result = KeRemoveQueueEx(a1, a6, a8, a7);
    v_stack_mB8 = (unsigned int)(result);
    result = 0;
    v_stack_mD4 = 0;
    v_rbx = 0;
loc_0020B623:
    v_stack_mD8 = 0;
    if (0 < ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_0020B65D;
loc_0020B62F:
    *(unsigned int *)(v_stack_m78) = (unsigned int)((unsigned int)((unsigned int)(result)));
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a6, a8, a7);
    v_rsp = (v_rsp) + (224);
    return result;
loc_0020B65D:
    if ((*(unsigned __int64 *)(a3 + v_rbx * 8)) == 128) goto loc_0020B80C;
    if ((*(unsigned __int64 *)(a3 + v_rbx * 8)) == 192) goto loc_0020B80C;
    if ((*(unsigned __int64 *)(a3 + v_rbx * 8) - 257) <= 1) goto loc_0020B80C;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a3 + v_rbx * 8) + 16)) != 0) goto loc_0020B749;
    v_rdi = (*(unsigned __int64 *)(a3 + v_rbx * 8)) + (-168);
    v_stack_p30 = *(unsigned __int64 *)(v_rdi + 96);
    v_stack_p50 = v_xmm0;
    if (condition_is_above_or_equal) goto loc_0020B815;
    v_stack_p80 = 0;
    v_stack_p48 = 0;
    v_r15 = (*(unsigned __int64 *)(v_rdi + 88)) & (-7);
    v_stack_pA8 = v_xmm0;
    v_stack_pB8 = v_xmm0;
    v_stack_pC8 = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 96) = 0;
    v_stack_p20 = v_stack_p48;
    result = IopCompleteRequest(v_rdi + 120, v_stack_p80, v_stack_p48, v_rdi + 192);
    goto loc_0020B771;
loc_0020B749:
    if (((unsigned __int8)(result)) == 2) goto loc_0020B863;
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 40)));
    v_stack_p58 = *(unsigned __int64 *)(v_rdi + 48);
    result = IopFreeMiniCompletionPacket(v_rdi, v_stack_p80, v_stack_p48, v_rdi + 192);
loc_0020B771:
    if (a6 == 0) goto loc_0020B7E3;
    v_r14 = (0) << (5);
    *(unsigned __int64 *)(v_r14 + v_stack_p70 * 1) = *(unsigned __int64 *)(v_rdi + 24);
    *(unsigned __int64 *)(v_r14 + v_stack_p70 * 1 + 8) = *(unsigned __int64 *)(v_rdi + 32);
    *(unsigned __int64 *)(v_r14 + v_stack_p70 * 1 + 16) = v_xmm0;
    goto loc_0020B7DC;
loc_0020B7DC:
    v_rbx = (unsigned int)((v_rbx) + 1);
    goto loc_0020B623;
loc_0020B7E3:
    v_r14 = (v_r14) << (5);
    *(unsigned __int64 *)(v_r14 + v_stack_p70 * 1) = *(unsigned __int64 *)(v_rdi + 24);
    *(unsigned __int64 *)(v_r14 + v_stack_p70 * 1 + 8) = *(unsigned __int64 *)(v_rdi + 32);
    *(unsigned __int64 *)(v_r14 + v_stack_p70 * 1 + 16) = v_xmm0;
    goto loc_0020B7DC;
loc_0020B80C:
    v_rsi = 0;
    goto loc_0020B62F;
loc_0020B815:
    if (condition_is_above_or_equal) goto loc_0020B851;
loc_0020B81F:
    a4 = (*(unsigned __int64 *)(v_stack_p78 + 88)) >> (1);
    a4 = (unsigned int)((a4) & (3));
    a4 = (a4) - 1;
    a1 = (*(unsigned __int64 *)(v_stack_p78 + 88)) & (-7);
    a2 = (a4 + a4 * 1) | (a1);
    if ((*(unsigned __int64 *)(v_stack_p78 + 88)) != (*(unsigned __int64 *)(v_stack_p78 + 88))) goto loc_0020B81F;
    if (a4 != 0) goto loc_0020BD20;
loc_0020B851:
    result = IoFreeIrp(v_stack_p78, a2, *(unsigned __int64 *)(v_stack_p78 + 88), a4);
    goto loc_0020B771;
loc_0020B863:
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p78 + 72)));
    v_stack_p58 = *(unsigned __int64 *)(v_stack_p78 + 64);
    v_stack_p30 = *(unsigned __int64 *)(v_stack_p78 + 80);
    v_stack_p38 = v_cr8;
    if ((*(unsigned int *)(v_rip + 14398600)) != 0) goto loc_0020BA6B;
loc_0020B89E:
    if (((*(unsigned __int8 *)(v_rip + 14398049)) & (33)) == 0) goto loc_0020B9FA;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13641127))) != 0) goto loc_0020B9FA;
    result = KiAcquireSpinLockInstrumented(v_stack_p78 + 96, a2, *(unsigned __int64 *)(v_stack_p78 + 88), a4);
loc_0020B8C2:
    *(unsigned __int8 *)(v_stack_p78 + 104) = 0;
    *(unsigned __int64 *)(v_stack_p78 + 88) = 0;
    if (((*(unsigned __int8 *)(v_rip + 14398001)) & (1)) != 0) goto loc_0020BCD4;
loc_0020B8DB:
loc_0020B8E1:
    if ((*(unsigned int *)(v_rip + 14398515)) != 0) {
        a1 = v_stack_p78;
        a2 = (unsigned __int8)(v_stack_p38);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_stack_p78 + 88), a4);
    }
    result = 0;
    result = ((*(unsigned int *)(v_rip + 14391035)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a2 = 0;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        a1 = v_stack_p30 - 48;
        result = ObpPushStackInfo(a1, a2, a3, a4);
        a3 = v_stack_p30;
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_0020BA1F;
loc_0020B94B:
    result = 0;
    result = ((*(unsigned int *)(v_rip + 14390964)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a2 = 0;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        a1 = v_stack_p68 - 48;
        result = ObpPushStackInfo(a1, a2, a3, a4);
        a3 = v_stack_p68;
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_0020BA45;
loc_0020B992:
    result = 0;
    result = ((*(unsigned int *)(v_rip + 14390902)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a2 = 0;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        a1 = v_stack_p78 - 48;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_greater) goto loc_0020B771;
    if (*(unsigned __int64 *)(v_stack_p78 - 40) != 0) goto loc_0020BAFA;
    if (!sign_flag) goto loc_0020BC4B;
    v_stack_p20 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_p78, *(unsigned __int64 *)(v_stack_p78 - 40) + 2);
loc_0020B9FA:
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((unsigned int)(result) != 0) goto loc_0020B8C2;
    result = KxWaitForSpinLockAndAcquire(v_stack_p78 + 96, a2, v_stack_p78, *(unsigned __int64 *)(v_stack_p78 - 40) + 2);
    goto loc_0020B8C2;
loc_0020BA1F:
    if (*(unsigned __int64 *)(v_stack_p68 - 48 + 8) != 0) goto loc_0020BA7A;
    if (!sign_flag) goto loc_0020BB3D;
    v_stack_p20 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_p78, a2 + 2);
loc_0020BA45:
    if (*(unsigned __int64 *)(v_stack_p68 - 48 + 8) != 0) goto loc_0020BABA;
    if (!sign_flag) goto loc_0020BBC4;
    v_stack_p20 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_p78, a2 + 2);
loc_0020BA6B:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), 2, v_stack_p78, a2 + 2);
    goto loc_0020B89E;
loc_0020BA7A:
    result = (v_stack_p68 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_p68 - 48 + 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 14398393));
    v_stack_p20 = (unsigned __int8)(result);
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 2144936 + a2 * 8 + 16545792), v_stack_p78, 1);
loc_0020BABA:
    result = (v_stack_p68 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_p68 - 48 + 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 14398329));
    v_stack_p20 = 1 + 23;
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 2145000 + a2 * 8 + 16545792), v_stack_p78, 1);
loc_0020BAFA:
    result = (v_stack_p78 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_p78 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 14398265));
    v_stack_p20 = 1 + 23;
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 2145067 + a2 * 8 + 16545792), v_stack_p78, 1);
loc_0020BB3D:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_0020BCF8;
    result = KeAreInterruptsEnabled(1 + 23, *(unsigned __int64 *)(v_rip - 2145067 + a2 * 8 + 16545792), v_stack_p78, 1);
    if ((unsigned __int8)(result) == 0) goto loc_0020BCF8;
    if (((unsigned __int8)((unsigned __int8)(v_stack_p38))) >= 1) goto loc_0020BCF8;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p68 - 48 + 26))) & (64)) != 0) goto loc_0020BB9C;
loc_0020BB76:
    result = 0;
    result = ((*(unsigned int *)(v_rip + 14390418)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a1 = v_stack_p68 - 48;
        result = ObpDeregisterObject(a1, *(unsigned __int64 *)(v_rip - 2145067 + a2 * 8 + 16545792), v_stack_p78, 1);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p68 - 48, a2, v_stack_p78, 1);
    goto loc_0020B94B;
loc_0020BB9C:
    result = (unsigned int)((result) & (127));
    a1 = (v_stack_p68 - 48) - (*(unsigned __int8 *)(result + v_rip - 2145190 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_0020BB76;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, v_stack_p78, 1);
    goto loc_0020BB76;
loc_0020BBC4:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_0020BD05;
    result = KeAreInterruptsEnabled(*(unsigned __int64 *)(a1), a2, v_stack_p78, 1);
    if ((unsigned __int8)(result) == 0) goto loc_0020BD05;
    if (((unsigned __int8)((unsigned __int8)(v_stack_p38))) >= 1) goto loc_0020BD05;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p68 - 48 + 26))) & (64)) != 0) goto loc_0020BC23;
loc_0020BBFD:
    result = 0;
    result = ((*(unsigned int *)(v_rip + 14390283)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a1 = v_stack_p68 - 48;
        result = ObpDeregisterObject(a1, a2, v_stack_p78, 1);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p68 - 48, a2, v_stack_p78, 1);
    goto loc_0020B992;
loc_0020BC23:
    result = (unsigned int)((result) & (127));
    a1 = (v_stack_p68 - 48) - (*(unsigned __int8 *)(result + v_rip - 2145325 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_0020BBFD;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, v_stack_p78, 1);
    goto loc_0020BBFD;
loc_0020BC4B:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_0020BD12;
    result = KeAreInterruptsEnabled(*(unsigned __int64 *)(a1), a2, v_stack_p78, 1);
    if ((unsigned __int8)(result) == 0) goto loc_0020BD12;
    if (((unsigned __int8)((unsigned __int8)(v_stack_p38))) >= 1) goto loc_0020BD12;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p78 - 22))) & (64)) != 0) goto loc_0020BCAB;
loc_0020BC83:
    result = 0;
    result = ((*(unsigned int *)(v_rip + 14390149)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a1 = v_stack_p78 - 48;
        result = ObpDeregisterObject(a1, a2, v_stack_p78, 1);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p78 - 48, a2, v_stack_p78, 1);
    goto loc_0020B771;
loc_0020BCAB:
    result = (unsigned int)((result) & (127));
    a1 = (v_stack_p78 - 48) - (*(unsigned __int8 *)(result + v_rip - 2145461 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_0020BC83;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, v_stack_p78, 1);
    goto loc_0020BC83;
loc_0020BCD4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13640062))) != 0) goto loc_0020B8DB;
    result = KiReleaseSpinLockInstrumented(v_stack_p78 + 96, v_stack_p118, v_stack_p78, 1);
    goto loc_0020B8E1;
loc_0020BCF8:
    result = ObpDeferObjectDeletion(v_stack_p68 - 48, v_stack_p118, v_stack_p78, 1);
    goto loc_0020B94B;
loc_0020BD05:
    result = ObpDeferObjectDeletion(v_stack_p68 - 48, v_stack_p118, v_stack_p78, 1);
    goto loc_0020B992;
loc_0020BD12:
    result = ObpDeferObjectDeletion(v_stack_p78 - 48, v_stack_p118, v_stack_p78, 1);
    goto loc_0020B771;
loc_0020BD20:
    goto loc_0020B771;
}
```

## 5. (Beta) C Style

```c
int64_t IoRemoveIoCompletion(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, uint8_t Arg6, int64_t Arg7, uint8_t Arg8)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p118;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC8;

    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0xBFF1A6)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mA0 = Arg3;
    v_stack_mA8 = Arg2;
    v_stack_mB0 = Arg1;
    v_stack_m90 = Arg1;
    v_stack_m88 = Arg2;
    v_stack_m80 = Arg3;
    v_stack_m78 = Arg5;
    v_stack_mC8 = v_xmm0;
    v_stack_mF0 = (uint32_t)((uint32_t)(Arg4));
    v_stack_mF8 = Arg3;
    result = KeRemoveQueueEx(Arg1, Arg6, Arg8, Arg7);
    v_stack_mB8 = (uint32_t)(result);
    result = 0;
    v_stack_mD4 = 0;
    local_rbx = 0;
loc_0020B623:
    v_stack_mD8 = 0;
    if (0 < ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_0020B65D;
loc_0020B62F:
    *(uint32_t *)(v_stack_m78) = (uint32_t)((uint32_t)((uint32_t)(result)));
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg6, Arg8, Arg7);
    local_rsp = (local_rsp) + (224);
    return result;
loc_0020B65D:
    if ((*(uint64_t *)(Arg3 + local_rbx * 8)) == 128) goto loc_0020B80C;
    if ((*(uint64_t *)(Arg3 + local_rbx * 8)) == 192) goto loc_0020B80C;
    if ((*(uint64_t *)(Arg3 + local_rbx * 8) - 257) <= 1) goto loc_0020B80C;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(Arg3 + local_rbx * 8) + 0x10)) != 0) goto loc_0020B749;
    local_rdi = (*(uint64_t *)(Arg3 + local_rbx * 8)) + (-168);
    v_stack_p30 = *(uint64_t *)(local_rdi + 0x60);
    v_stack_p50 = v_xmm0;
    if (condition_is_above_or_equal) goto loc_0020B815;
    v_stack_p80 = 0;
    v_stack_p48 = 0;
    local_r15 = (*(uint64_t *)(local_rdi + 0x58)) & (-7);
    v_stack_pA8 = v_xmm0;
    v_stack_pB8 = v_xmm0;
    v_stack_pC8 = v_xmm0;
    *(uint64_t *)(local_rdi + 0x60) = 0;
    v_stack_p20 = v_stack_p48;
    result = IopCompleteRequest(local_rdi + 120, v_stack_p80, v_stack_p48, local_rdi + 192);
    goto loc_0020B771;
loc_0020B749:
    if (((uint8_t)(result)) == 2) goto loc_0020B863;
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x28)));
    v_stack_p58 = *(uint64_t *)(local_rdi + 0x30);
    result = IopFreeMiniCompletionPacket(local_rdi, v_stack_p80, v_stack_p48, local_rdi + 192);
loc_0020B771:
    if (Arg6 == 0) goto loc_0020B7E3;
    local_r14 = (0) << (5);
    *(uint64_t *)(local_r14 + v_stack_p70 * 1) = *(uint64_t *)(local_rdi + 0x18);
    *(uint64_t *)(local_r14 + v_stack_p70 * 1 + 0x8) = *(uint64_t *)(local_rdi + 0x20);
    *(uint64_t *)(local_r14 + v_stack_p70 * 1 + 0x10) = v_xmm0;
    goto loc_0020B7DC;
loc_0020B7DC:
    local_rbx = (uint32_t)((local_rbx) + 1);
    goto loc_0020B623;
loc_0020B7E3:
    local_r14 = (local_r14) << (5);
    *(uint64_t *)(local_r14 + v_stack_p70 * 1) = *(uint64_t *)(local_rdi + 0x18);
    *(uint64_t *)(local_r14 + v_stack_p70 * 1 + 0x8) = *(uint64_t *)(local_rdi + 0x20);
    *(uint64_t *)(local_r14 + v_stack_p70 * 1 + 0x10) = v_xmm0;
    goto loc_0020B7DC;
loc_0020B80C:
    local_rsi = 0;
    goto loc_0020B62F;
loc_0020B815:
    if (condition_is_above_or_equal) goto loc_0020B851;
loc_0020B81F:
    Arg4 = (*(uint64_t *)(v_stack_p78 + 0x58)) >> (1);
    Arg4 = (uint32_t)((Arg4) & (3));
    Arg4 = (Arg4) - 1;
    Arg1 = (*(uint64_t *)(v_stack_p78 + 0x58)) & (-7);
    Arg2 = (Arg4 + Arg4 * 1) | (Arg1);
    if ((*(uint64_t *)(v_stack_p78 + 0x58)) != (*(uint64_t *)(v_stack_p78 + 0x58))) goto loc_0020B81F;
    if (Arg4 != 0) goto loc_0020BD20;
loc_0020B851:
    result = IoFreeIrp(v_stack_p78, Arg2, *(uint64_t *)(v_stack_p78 + 0x58), Arg4);
    goto loc_0020B771;
loc_0020B863:
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0x48)));
    v_stack_p58 = *(uint64_t *)(v_stack_p78 + 0x40);
    v_stack_p30 = *(uint64_t *)(v_stack_p78 + 0x50);
    v_stack_p38 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xDBB488)) != 0) goto loc_0020BA6B;
loc_0020B89E:
    if (((*(uint8_t *)(v_rip + 0xDBB261)) & (33)) == 0) goto loc_0020B9FA;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD025A7))) != 0) goto loc_0020B9FA;
    result = KiAcquireSpinLockInstrumented(v_stack_p78 + 96, Arg2, *(uint64_t *)(v_stack_p78 + 0x58), Arg4);
loc_0020B8C2:
    *(uint8_t *)(v_stack_p78 + 0x68) = 0;
    *(uint64_t *)(v_stack_p78 + 0x58) = 0;
    if (((*(uint8_t *)(v_rip + 0xDBB231)) & (1)) != 0) goto loc_0020BCD4;
loc_0020B8DB:
loc_0020B8E1:
    if ((*(uint32_t *)(v_rip + 0xDBB433)) != 0) {
        Arg1 = v_stack_p78;
        Arg2 = (uint8_t)(v_stack_p38);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(v_stack_p78 + 0x58), Arg4);
    }
    result = 0;
    result = ((*(uint32_t *)(v_rip + 0xDB96FB)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg2 = 0;
        Arg4 = 0x746C6644ULL;
        Arg3 = Arg2 + 1;
        Arg1 = v_stack_p30 - 48;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
        Arg3 = v_stack_p30;
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_0020BA1F;
loc_0020B94B:
    result = 0;
    result = ((*(uint32_t *)(v_rip + 0xDB96B4)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg2 = 0;
        Arg4 = 0x746C6644ULL;
        Arg3 = Arg2 + 1;
        Arg1 = v_stack_p68 - 48;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
        Arg3 = v_stack_p68;
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_0020BA45;
loc_0020B992:
    result = 0;
    result = ((*(uint32_t *)(v_rip + 0xDB9676)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg2 = 0;
        Arg4 = 0x746C6644ULL;
        Arg3 = Arg2 + 1;
        Arg1 = v_stack_p78 - 48;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
    if (condition_is_greater) goto loc_0020B771;
    if (*(uint64_t *)(v_stack_p78 - 0x28) != 0) goto loc_0020BAFA;
    if (!sign_flag) goto loc_0020BC4B;
    v_stack_p20 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_p78, *(uint64_t *)(v_stack_p78 - 0x28) + 2);
loc_0020B9FA:
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((uint32_t)(result) != 0) goto loc_0020B8C2;
    result = KxWaitForSpinLockAndAcquire(v_stack_p78 + 96, Arg2, v_stack_p78, *(uint64_t *)(v_stack_p78 - 0x28) + 2);
    goto loc_0020B8C2;
loc_0020BA1F:
    if (*(uint64_t *)(v_stack_p68 - 0x30 + 0x8) != 0) goto loc_0020BA7A;
    if (!sign_flag) goto loc_0020BB3D;
    v_stack_p20 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_p78, Arg2 + 2);
loc_0020BA45:
    if (*(uint64_t *)(v_stack_p68 - 0x30 + 0x8) != 0) goto loc_0020BABA;
    if (!sign_flag) goto loc_0020BBC4;
    v_stack_p20 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_p78, Arg2 + 2);
loc_0020BA6B:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), 2, v_stack_p78, Arg2 + 2);
    goto loc_0020B89E;
loc_0020BA7A:
    result = (v_stack_p68 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_p68 - 0x30 + 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xDBB3B9));
    v_stack_p20 = (uint8_t)(result);
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x20BAA8 + Arg2 * 8 + 0xFC7800), v_stack_p78, 1);
loc_0020BABA:
    result = (v_stack_p68 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_p68 - 0x30 + 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xDBB379));
    v_stack_p20 = 1 + 23;
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x20BAE8 + Arg2 * 8 + 0xFC7800), v_stack_p78, 1);
loc_0020BAFA:
    result = (v_stack_p78 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_p78 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xDBB339));
    v_stack_p20 = 1 + 23;
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x20BB2B + Arg2 * 8 + 0xFC7800), v_stack_p78, 1);
loc_0020BB3D:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_0020BCF8;
    result = KeAreInterruptsEnabled(1 + 23, *(uint64_t *)(v_rip - 0x20BB2B + Arg2 * 8 + 0xFC7800), v_stack_p78, 1);
    if ((uint8_t)(result) == 0) goto loc_0020BCF8;
    if (((uint8_t)((uint8_t)(v_stack_p38))) >= 1) goto loc_0020BCF8;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p68 - 0x30 + 0x1A))) & (64)) != 0) goto loc_0020BB9C;
loc_0020BB76:
    result = 0;
    result = ((*(uint32_t *)(v_rip + 0xDB9492)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg1 = v_stack_p68 - 48;
        result = ObpDeregisterObject(Arg1, *(uint64_t *)(v_rip - 0x20BB2B + Arg2 * 8 + 0xFC7800), v_stack_p78, 1);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p68 - 48, Arg2, v_stack_p78, 1);
    goto loc_0020B94B;
loc_0020BB9C:
    result = (uint32_t)((result) & (127));
    Arg1 = (v_stack_p68 - 48) - (*(uint8_t *)(result + v_rip - 0x20BBA6 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(Arg1) + 0x18)) == 0) goto loc_0020BB76;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(Arg1), Arg2, v_stack_p78, 1);
    goto loc_0020BB76;
loc_0020BBC4:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_0020BD05;
    result = KeAreInterruptsEnabled(*(uint64_t *)(Arg1), Arg2, v_stack_p78, 1);
    if ((uint8_t)(result) == 0) goto loc_0020BD05;
    if (((uint8_t)((uint8_t)(v_stack_p38))) >= 1) goto loc_0020BD05;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p68 - 0x30 + 0x1A))) & (64)) != 0) goto loc_0020BC23;
loc_0020BBFD:
    result = 0;
    result = ((*(uint32_t *)(v_rip + 0xDB940B)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg1 = v_stack_p68 - 48;
        result = ObpDeregisterObject(Arg1, Arg2, v_stack_p78, 1);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p68 - 48, Arg2, v_stack_p78, 1);
    goto loc_0020B992;
loc_0020BC23:
    result = (uint32_t)((result) & (127));
    Arg1 = (v_stack_p68 - 48) - (*(uint8_t *)(result + v_rip - 0x20BC2D * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(Arg1) + 0x18)) == 0) goto loc_0020BBFD;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(Arg1), Arg2, v_stack_p78, 1);
    goto loc_0020BBFD;
loc_0020BC4B:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_0020BD12;
    result = KeAreInterruptsEnabled(*(uint64_t *)(Arg1), Arg2, v_stack_p78, 1);
    if ((uint8_t)(result) == 0) goto loc_0020BD12;
    if (((uint8_t)((uint8_t)(v_stack_p38))) >= 1) goto loc_0020BD12;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p78 - 0x16))) & (64)) != 0) goto loc_0020BCAB;
loc_0020BC83:
    result = 0;
    result = ((*(uint32_t *)(v_rip + 0xDB9385)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg1 = v_stack_p78 - 48;
        result = ObpDeregisterObject(Arg1, Arg2, v_stack_p78, 1);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p78 - 48, Arg2, v_stack_p78, 1);
    goto loc_0020B771;
loc_0020BCAB:
    result = (uint32_t)((result) & (127));
    Arg1 = (v_stack_p78 - 48) - (*(uint8_t *)(result + v_rip - 0x20BCB5 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(Arg1) + 0x18)) == 0) goto loc_0020BC83;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(Arg1), Arg2, v_stack_p78, 1);
    goto loc_0020BC83;
loc_0020BCD4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0217E))) != 0) goto loc_0020B8DB;
    result = KiReleaseSpinLockInstrumented(v_stack_p78 + 96, v_stack_p118, v_stack_p78, 1);
    goto loc_0020B8E1;
loc_0020BCF8:
    result = ObpDeferObjectDeletion(v_stack_p68 - 48, v_stack_p118, v_stack_p78, 1);
    goto loc_0020B94B;
loc_0020BD05:
    result = ObpDeferObjectDeletion(v_stack_p68 - 48, v_stack_p118, v_stack_p78, 1);
    goto loc_0020B992;
loc_0020BD12:
    result = ObpDeferObjectDeletion(v_stack_p78 - 48, v_stack_p118, v_stack_p78, 1);
    goto loc_0020B771;
loc_0020BD20:
    goto loc_0020B771;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020B580&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
