# ExpWnfDeleteSubscription

- RVA: `0x00908528`–`0x009088BF` (길이 `919` bytes)
- VA: `0x0000000140908528`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00088E6C`
- 디코드: `250`개 명령, `919/919` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00908561` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090857A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009085B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009085CF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00908652` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0090866B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009086B8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009086F6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00908719` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00908743` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00908766` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0090876F` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0090877C` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (function, `0x002A4CB0`)
- `0x00908789` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00908820` → [ExpWnfNotifyNameSubscribers](ExpWnfNotifyNameSubscribers_function_0090C160.md) (function, `0x0090C160`)
- `0x00908835` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00908849` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00908856` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00908863` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00908870` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009088B5` → [ExpWnfNotifyNameSubscribers](ExpWnfNotifyNameSubscribers_function_0090C160.md) (function, `0x0090C160`)

### Direct callers
- [ExpWnfDeleteProcessContext](ExpWnfDeleteProcessContext_function_00908270.md) at `0x009082FF`
- [NtUnsubscribeWnfStateChange](NtUnsubscribeWnfStateChange_function_009092B0.md) at `0x0090933D`
- [ExUnsubscribeWnfStateChange](../A7/ExUnsubscribeWnfStateChange_function_00A7BE50.md) at `0x00A7BE6C`

### Static image references
- `0x00908684` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x00908561` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090857A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009085B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009085CF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00908652` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0090866B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009086B8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009086F6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00908719` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00908743` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00908766` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0090876F` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x0090877C` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (`PAGE` → `.text`)
  - `0x00908789` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00908835` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00908849` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00908856` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00908863` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00908870` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00908528  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0090852D  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00908532  55                              push rbp
00908533  56                              push rsi
00908534  57                              push rdi
00908535  41 54                           push r12
00908537  41 55                           push r13
00908539  41 56                           push r14
0090853B  41 57                           push r15
0090853D  48 83 EC 20                     sub rsp, 0x20
00908541  4C 8B BA E8 05 00 00            mov r15, qword ptr [rdx + 0x5e8]
00908548  48 8B F9                        mov rdi, rcx
0090854B  BE 01 00 00 00                  mov esi, 1
00908550  4D 85 FF                        test r15, r15
00908553  74 33                           je 0x140908588
00908555  49 8D 5F 50                     lea rbx, [r15 + 0x50]
00908559  45 33 C0                        xor r8d, r8d
0090855C  48 8B CB                        mov rcx, rbx
0090855F  33 D2                           xor edx, edx
00908561  E8 CA 7C 90 FF                  call 0x140210230
00908566  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0090856C  48 8B E8                        mov rbp, rax
0090856F  73 0E                           jae 0x14090857f
00908571  4C 8B C3                        mov r8, rbx
00908574  48 8B D0                        mov rdx, rax
00908577  48 8B CB                        mov rcx, rbx
0090857A  E8 11 77 90 FF                  call 0x14020fc90
0090857F  48 85 ED                        test rbp, rbp
00908582  74 04                           je 0x140908588
00908584  40 88 75 0A                     mov byte ptr [rbp + 0xa], sil
00908588  48 83 CB FF                     or rbx, 0xffffffffffffffff
0090858C  48 83 7F 28 00                  cmp qword ptr [rdi + 0x28], 0
00908591  0F 84 93 02 00 00               je 0x14090882a
00908597  83 64 24 70 00                  and dword ptr [rsp + 0x70], 0
0090859C  83 64 24 78 00                  and dword ptr [rsp + 0x78], 0
009085A1  48 8B 6F 30                     mov rbp, qword ptr [rdi + 0x30]
009085A5  48 85 ED                        test rbp, rbp
009085A8  74 5E                           je 0x140908608
009085AA  4C 8D 75 70                     lea r14, [rbp + 0x70]
009085AE  45 33 C0                        xor r8d, r8d
009085B1  49 8B CE                        mov rcx, r14
009085B4  33 D2                           xor edx, edx
009085B6  E8 75 7C 90 FF                  call 0x140210230
009085BB  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
009085C1  4C 8B E8                        mov r13, rax
009085C4  73 0E                           jae 0x1409085d4
009085C6  4D 8B C6                        mov r8, r14
009085C9  48 8B D0                        mov rdx, rax
009085CC  49 8B CE                        mov rcx, r14
009085CF  E8 BC 76 90 FF                  call 0x14020fc90
009085D4  4D 85 ED                        test r13, r13
009085D7  74 04                           je 0x1409085dd
009085D9  41 88 75 0A                     mov byte ptr [r13 + 0xa], sil
009085DD  48 8D 47 40                     lea rax, [rdi + 0x40]
009085E1  48 8B 10                        mov rdx, qword ptr [rax]
009085E4  48 39 42 08                     cmp qword ptr [rdx + 8], rax
009085E8  75 34                           jne 0x14090861e
009085EA  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
009085EE  48 39 01                        cmp qword ptr [rcx], rax
009085F1  75 2B                           jne 0x14090861e
009085F3  48 89 11                        mov qword ptr [rcx], rdx
009085F6  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
009085FA  8B 47 64                        mov eax, dword ptr [rdi + 0x64]
009085FD  48 83 67 30 00                  and qword ptr [rdi + 0x30], 0
00908602  23 C6                           and eax, esi
00908604  84 C0                           test al, al
00908606  75 1D                           jne 0x140908625
00908608  48 8D 47 18                     lea rax, [rdi + 0x18]
0090860C  48 8B 10                        mov rdx, qword ptr [rax]
0090860F  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00908613  75 09                           jne 0x14090861e
00908615  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00908619  48 39 01                        cmp qword ptr [rcx], rax
0090861C  74 21                           je 0x14090863f
0090861E  B9 03 00 00 00                  mov ecx, 3
00908623  CD 29                           int 0x29
00908625  8B C3                           mov eax, ebx
00908627  F0 0F C1 85 A0 00 00 00         lock xadd dword ptr [rbp + 0xa0], eax
0090862F  B9 00 00 00 00                  mov ecx, 0
00908634  03 C3                           add eax, ebx
00908636  0F 94 C1                        sete cl
00908639  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0090863D  EB C9                           jmp 0x140908608
0090863F  48 89 11                        mov qword ptr [rcx], rdx
00908642  4D 8D 77 68                     lea r14, [r15 + 0x68]
00908646  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0090864A  45 33 C0                        xor r8d, r8d
0090864D  33 D2                           xor edx, edx
0090864F  49 8B CE                        mov rcx, r14
00908652  E8 D9 7B 90 FF                  call 0x140210230
00908657  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0090865D  4C 8B E8                        mov r13, rax
00908660  73 0E                           jae 0x140908670
00908662  4D 8B C6                        mov r8, r14
00908665  48 8B D0                        mov rdx, rax
00908668  49 8B CE                        mov rcx, r14
0090866B  E8 20 76 90 FF                  call 0x14020fc90
00908670  4D 85 ED                        test r13, r13
00908673  74 04                           je 0x140908679
00908675  41 88 75 0A                     mov byte ptr [r13 + 0xa], sil
00908679  8B 4F 78                        mov ecx, dword ptr [rdi + 0x78]
0090867C  3B CE                           cmp ecx, esi
0090867E  0F 84 20 01 00 00               je 0x1409087a4
00908684  48 8B 05 25 E4 6B 00            mov rax, qword ptr [rip + 0x6be425]
0090868B  48 39 47 28                     cmp qword ptr [rdi + 0x28], rax
0090868F  74 08                           je 0x140908699
00908691  85 C9                           test ecx, ecx
00908693  0F 85 0B 01 00 00               jne 0x1409087a4
00908699  44 8B 6C 24 70                  mov r13d, dword ptr [rsp + 0x70]
0090869E  48 83 67 28 00                  and qword ptr [rdi + 0x28], 0
009086A3  48 8B C3                        mov rax, rbx
009086A6  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
009086AB  24 06                           and al, 6
009086AD  3C 02                           cmp al, 2
009086AF  0F 84 9E 01 00 00               je 0x140908853
009086B5  49 8B CE                        mov rcx, r14
009086B8  E8 43 8F 9D FF                  call 0x1402e1600
009086BD  48 85 ED                        test rbp, rbp
009086C0  0F 84 82 00 00 00               je 0x140908748
009086C6  45 33 E4                        xor r12d, r12d
009086C9  44 39 64 24 78                  cmp dword ptr [rsp + 0x78], r12d
009086CE  0F 85 5D 01 00 00               jne 0x140908831
009086D4  45 85 ED                        test r13d, r13d
009086D7  0F 85 54 01 00 00               jne 0x140908831
009086DD  4C 8D 75 70                     lea r14, [rbp + 0x70]
009086E1  48 8B C3                        mov rax, rbx
009086E4  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
009086E9  24 06                           and al, 6
009086EB  3C 02                           cmp al, 2
009086ED  0F 84 6D 01 00 00               je 0x140908860
009086F3  49 8B CE                        mov rcx, r14
009086F6  E8 05 8F 9D FF                  call 0x1402e1600
009086FB  4D 85 FF                        test r15, r15
009086FE  74 21                           je 0x140908721
00908700  4D 8D 77 50                     lea r14, [r15 + 0x50]
00908704  48 8B C3                        mov rax, rbx
00908707  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
0090870C  24 06                           and al, 6
0090870E  3C 02                           cmp al, 2
00908710  0F 84 57 01 00 00               je 0x14090886d
00908716  49 8B CE                        mov rcx, r14
00908719  E8 E2 8E 9D FF                  call 0x1402e1600
0090871E  45 33 FF                        xor r15d, r15d
00908721  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00908726  45 85 ED                        test r13d, r13d
00908729  0F 85 6D 01 00 00               jne 0x14090889c
0090872F  83 7C 24 78 00                  cmp dword ptr [rsp + 0x78], 0
00908734  0F 85 CD 00 00 00               jne 0x140908807
0090873A  45 85 E4                        test r12d, r12d
0090873D  74 09                           je 0x140908748
0090873F  48 8D 4D 08                     lea rcx, [rbp + 8]
00908743  E8 38 17 A4 FF                  call 0x140349e80
00908748  4D 85 FF                        test r15, r15
0090874B  74 1E                           je 0x14090876b
0090874D  49 8D 6F 50                     lea rbp, [r15 + 0x50]
00908751  F0 48 0F C1 5D 00               lock xadd qword ptr [rbp], rbx
00908757  80 E3 06                        and bl, 6
0090875A  80 FB 02                        cmp bl, 2
0090875D  0F 84 E3 00 00 00               je 0x140908846
00908763  48 8B CD                        mov rcx, rbp
00908766  E8 95 8E 9D FF                  call 0x1402e1600
0090876B  48 8D 4F 08                     lea rcx, [rdi + 8]
0090876F  E8 0C 17 A4 FF                  call 0x140349e80
00908774  85 F6                           test esi, esi
00908776  74 16                           je 0x14090878e
00908778  48 8D 4F 08                     lea rcx, [rdi + 8]
0090877C  E8 2F C5 99 FF                  call 0x1402a4cb0
00908781  BA 57 6E 66 20                  mov edx, 0x20666e57
00908786  48 8B CF                        mov rcx, rdi
00908789  E8 E2 A0 27 00                  call 0x140b82870
0090878E  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00908793  48 83 C4 20                     add rsp, 0x20
00908797  41 5F                           pop r15
00908799  41 5E                           pop r14
0090879B  41 5D                           pop r13
0090879D  41 5C                           pop r12
0090879F  5F                              pop rdi
009087A0  5E                              pop rsi
009087A1  5D                              pop rbp
009087A2  C3                              ret
009087A3  CC                              int3
009087A4  48 8D 47 68                     lea rax, [rdi + 0x68]
009087A8  48 8B 10                        mov rdx, qword ptr [rax]
009087AB  48 39 42 08                     cmp qword ptr [rdx + 8], rax
009087AF  0F 85 69 FE FF FF               jne 0x14090861e
009087B5  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
009087B9  48 39 01                        cmp qword ptr [rcx], rax
009087BC  0F 85 5C FE FF FF               jne 0x14090861e
009087C2  48 89 11                        mov qword ptr [rcx], rdx
009087C5  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
009087C9  48 85 ED                        test rbp, rbp
009087CC  0F 84 C7 FE FF FF               je 0x140908699
009087D2  8B 47 64                        mov eax, dword ptr [rdi + 0x64]
009087D5  23 C6                           and eax, esi
009087D7  84 C0                           test al, al
009087D9  0F 84 BA FE FF FF               je 0x140908699
009087DF  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
009087E2  23 C6                           and eax, esi
009087E4  84 C0                           test al, al
009087E6  0F 84 9B 00 00 00               je 0x140908887
009087EC  8B C3                           mov eax, ebx
009087EE  F0 0F C1 85 A4 00 00 00         lock xadd dword ptr [rbp + 0xa4], eax
009087F6  03 C3                           add eax, ebx
009087F8  41 BD 00 00 00 00               mov r13d, 0
009087FE  41 0F 94 C5                     sete r13b
00908802  E9 97 FE FF FF                  jmp 0x14090869e
00908807  45 33 C9                        xor r9d, r9d
0090880A  44 8B C6                        mov r8d, esi
0090880D  4C 3B 35 9C E2 6B 00            cmp r14, qword ptr [rip + 0x6be29c]
00908814  BA 04 00 00 00                  mov edx, 4
00908819  48 8B CD                        mov rcx, rbp
0090881C  41 0F 95 C1                     setne r9b
00908820  E8 3B 39 00 00                  call 0x14090c160
00908825  E9 10 FF FF FF                  jmp 0x14090873a
0090882A  33 F6                           xor esi, esi
0090882C  E9 17 FF FF FF                  jmp 0x140908748
00908831  48 8D 4D 08                     lea rcx, [rbp + 8]
00908835  E8 E6 DD 90 FF                  call 0x140216620
0090883A  84 C0                           test al, al
0090883C  74 3C                           je 0x14090887a
0090883E  44 8B E6                        mov r12d, esi
00908841  E9 97 FE FF FF                  jmp 0x1409086dd
00908846  48 8B CD                        mov rcx, rbp
00908849  E8 82 D5 95 FF                  call 0x140265dd0
0090884E  E9 10 FF FF FF                  jmp 0x140908763
00908853  49 8B CE                        mov rcx, r14
00908856  E8 75 D5 95 FF                  call 0x140265dd0
0090885B  E9 55 FE FF FF                  jmp 0x1409086b5
00908860  49 8B CE                        mov rcx, r14
00908863  E8 68 D5 95 FF                  call 0x140265dd0
00908868  E9 86 FE FF FF                  jmp 0x1409086f3
0090886D  49 8B CE                        mov rcx, r14
00908870  E8 5B D5 95 FF                  call 0x140265dd0
00908875  E9 9C FE FF FF                  jmp 0x140908716
0090887A  44 21 64 24 78                  and dword ptr [rsp + 0x78], r12d
0090887F  45 33 ED                        xor r13d, r13d
00908882  E9 56 FE FF FF                  jmp 0x1409086dd
00908887  8B 87 80 00 00 00               mov eax, dword ptr [rdi + 0x80]
0090888D  23 C6                           and eax, esi
0090888F  84 C0                           test al, al
00908891  0F 84 02 FE FF FF               je 0x140908699
00908897  E9 50 FF FF FF                  jmp 0x1409087ec
0090889C  45 33 C9                        xor r9d, r9d
0090889F  44 8B C6                        mov r8d, esi
009088A2  4C 3B 35 07 E2 6B 00            cmp r14, qword ptr [rip + 0x6be207]
009088A9  BA 08 00 00 00                  mov edx, 8
009088AE  48 8B CD                        mov rcx, rbp
009088B1  41 0F 95 C1                     setne r9b
009088B5  E8 A6 38 00 00                  call 0x14090c160
009088BA  E9 70 FE FF FF                  jmp 0x14090872f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWnfDeleteSubscription(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a2 + 1512) == 0) goto loc_00908588;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a2 + 1512) + 80, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a2 + 1512) + 80;
        a2 = result;
        a1 = *(unsigned __int64 *)(a2 + 1512) + 80;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rbx = (*(unsigned __int64 *)(a2 + 1512) + 80) | (-1);
    if ((*(unsigned __int64 *)(a1 + 40)) == 0) goto loc_0090882A;
    if (*(unsigned __int64 *)(a1 + 48) == 0) goto loc_00908608;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 48) + 112, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1 + 48) + 112;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1 + 48) + 112;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 8)) != (a1 + 64)) goto loc_0090861E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64 + 8))) != (a1 + 64)) goto loc_0090861E;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64 + 8)) = *(unsigned __int64 *)(a1 + 64);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 8) = *(unsigned __int64 *)(a1 + 64 + 8);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 100))) & (1));
    if ((unsigned __int8)(result) != 0) goto loc_00908625;
loc_00908608:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8)) != (a1 + 24)) goto loc_0090861E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8))) == (a1 + 24)) goto loc_0090863F;
loc_0090861E:
loc_00908625:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) + ((unsigned int)(v_rbx)));
    a1 = (condition_is_equal) ? 1 : 0;
    v_stack_p20 = (unsigned int)(a1);
    goto loc_00908608;
loc_0090863F:
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1 + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8) = a1;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a2 + 1512) + 104, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a2 + 1512) + 104;
        a2 = result;
        a1 = *(unsigned __int64 *)(a2 + 1512) + 104;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 120)))) == 1) goto loc_009087A4;
    if ((*(unsigned __int64 *)(a1 + 40)) == (*(unsigned __int64 *)(v_rip + 7070757))) goto loc_00908699;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 120))) != 0) goto loc_009087A4;
loc_00908699:
loc_0090869E:
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00908853;
loc_009086B5:
    result = KeAbPostRelease(*(unsigned __int64 *)(a2 + 1512) + 104, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 48) == 0) goto loc_00908748;
    v_r12 = 0;
    if (v_stack_p20 != 0) goto loc_00908831;
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_00908831;
loc_009086DD:
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00908860;
loc_009086F3:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 48) + 112, a2, a3, a4);
    if (*(unsigned __int64 *)(a2 + 1512) == 0) goto loc_00908721;
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0090886D;
loc_00908716:
    result = KeAbPostRelease(*(unsigned __int64 *)(a2 + 1512) + 80, a2, a3, a4);
    v_r15 = 0;
loc_00908721:
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_0090889C;
loc_0090872F:
    if (v_stack_p20 != 0) goto loc_00908807;
loc_0090873A:
    if (0 != 0) {
        a1 = *(unsigned __int64 *)(a1 + 48) + 8;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    if (0 == 0) goto loc_0090876B;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00908846;
loc_00908763:
    result = KeAbPostRelease(v_r15 + 80, a2, a3, a4);
loc_0090876B:
    result = ExReleaseRundownProtection(a1 + 8, a2, a3, a4);
    if (1 != 0) {
        a1 = a1 + 8;
        result = ExWaitForRundownProtectionRelease(a1, a2, a3, a4);
        a2 = 0x20666E57ULL;
        a1 = a1;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
loc_009087A4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8)) != (a1 + 104)) goto loc_0090861E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104 + 8))) != (a1 + 104)) goto loc_0090861E;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104 + 8)) = *(unsigned __int64 *)(a1 + 104);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8) = *(unsigned __int64 *)(a1 + 104 + 8);
    if (v_r15 + 80 == 0) goto loc_00908699;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 100))) & (1));
    if ((unsigned __int8)(result) == 0) goto loc_00908699;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 124))) & (1));
    if ((unsigned __int8)(result) == 0) goto loc_00908887;
loc_009087EC:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8))) + ((unsigned int)(v_stack_p8)));
    v_r13 = (condition_is_equal) ? 1 : 0;
    goto loc_0090869E;
loc_00908807:
    a4 = 0;
    a4 = (v_stack_p10 != (*(unsigned __int64 *)(v_rip + 7070364))) ? 1 : 0;
    result = ExpWnfNotifyNameSubscribers(v_r15 + 80, 4, 1, a4);
    goto loc_0090873A;
loc_0090882A:
    v_rsi = 0;
    goto loc_00908748;
loc_00908831:
    result = ExAcquireRundownProtection(v_r15 + 80 + 8, 4, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0090887A;
    goto loc_009086DD;
loc_00908846:
    result = ExfTryToWakePushLock(v_r15 + 80, 4, 1, a4);
    goto loc_00908763;
loc_00908853:
    result = ExfTryToWakePushLock(v_stack_p10, 4, 1, a4);
    goto loc_009086B5;
loc_00908860:
    result = ExfTryToWakePushLock(v_stack_p10, 4, 1, a4);
    goto loc_009086F3;
loc_0090886D:
    result = ExfTryToWakePushLock(v_stack_p10, 4, 1, a4);
    goto loc_00908716;
loc_0090887A:
    v_r13 = 0;
    goto loc_009086DD;
loc_00908887:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 128))) & (0));
    if ((unsigned __int8)(result) == 0) goto loc_00908699;
    goto loc_009087EC;
loc_0090889C:
    a4 = 0;
    a4 = (v_stack_p10 != (*(unsigned __int64 *)(v_rip + 7070215))) ? 1 : 0;
    result = ExpWnfNotifyNameSubscribers(v_r15 + 80, 8, 0, a4);
    goto loc_0090872F;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWnfDeleteSubscription(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p78;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg2 + 0x5E8) == 0) goto loc_00908588;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg2 + 0x5E8) + 80, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg2 + 0x5E8) + 80;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg2 + 0x5E8) + 80;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rbx = (*(uint64_t *)(arg2 + 0x5E8) + 80) | (-1);
    if ((*(uint64_t *)(arg1 + 0x28)) == 0) goto loc_0090882A;
    if (*(uint64_t *)(arg1 + 0x30) == 0) goto loc_00908608;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x30) + 112, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1 + 0x30) + 112;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1 + 0x30) + 112;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x8)) != (Arg1 + 64)) goto loc_0090861E;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x40 + 0x8))) != (Arg1 + 64)) goto loc_0090861E;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40 + 0x8)) = *(uint64_t *)(arg1 + 0x40);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x8) = *(uint64_t *)(arg1 + 0x40 + 0x8);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x64))) & (1));
    if ((uint8_t)(result) != 0) goto loc_00908625;
loc_00908608:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8)) != (Arg1 + 24)) goto loc_0090861E;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8))) == (Arg1 + 24)) goto loc_0090863F;
loc_0090861E:
loc_00908625:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) + ((uint32_t)(local_rbx)));
    Arg1 = (condition_is_equal) ? 1 : 0;
    v_stack_p20 = (uint32_t)(Arg1);
    goto loc_00908608;
loc_0090863F:
    *(uint64_t *)(arg1) = *(uint64_t *)(arg1 + 0x18);
    *(void **)(*(uint64_t *)(arg1 + 0x18) + 0x8) = Arg1;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg2 + 0x5E8) + 104, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg2 + 0x5E8) + 104;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg2 + 0x5E8) + 104;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x78)))) == 1) goto loc_009087A4;
    if ((*(uint64_t *)(arg1 + 0x28)) == (*(uint64_t *)(v_rip + 0x6BE425))) goto loc_00908699;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x78))) != 0) goto loc_009087A4;
loc_00908699:
loc_0090869E:
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00908853;
loc_009086B5:
    result = KeAbPostRelease(*(uint64_t *)(arg2 + 0x5E8) + 104, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(arg1 + 0x30) == 0) goto loc_00908748;
    local_r12 = 0;
    if (v_stack_p20 != 0) goto loc_00908831;
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_00908831;
loc_009086DD:
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00908860;
loc_009086F3:
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x30) + 112, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(arg2 + 0x5E8) == 0) goto loc_00908721;
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0090886D;
loc_00908716:
    result = KeAbPostRelease(*(uint64_t *)(arg2 + 0x5E8) + 80, Arg2, Arg3, Arg4);
    local_r15 = 0;
loc_00908721:
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_0090889C;
loc_0090872F:
    if (v_stack_p20 != 0) goto loc_00908807;
loc_0090873A:
    if (0 != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x30) + 8;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    if (0 == 0) goto loc_0090876B;
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00908846;
loc_00908763:
    result = KeAbPostRelease(local_r15 + 80, Arg2, Arg3, Arg4);
loc_0090876B:
    result = ExReleaseRundownProtection(Arg1 + 8, Arg2, Arg3, Arg4);
    if (1 != 0) {
        Arg1 = Arg1 + 8;
        result = ExWaitForRundownProtectionRelease(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 0x20666E57ULL;
        Arg1 = Arg1;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
loc_009087A4:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8)) != (Arg1 + 104)) goto loc_0090861E;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x68 + 0x8))) != (Arg1 + 104)) goto loc_0090861E;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x68 + 0x8)) = *(uint64_t *)(arg1 + 0x68);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8) = *(uint64_t *)(arg1 + 0x68 + 0x8);
    if (local_r15 + 80 == 0) goto loc_00908699;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x64))) & (1));
    if ((uint8_t)(result) == 0) goto loc_00908699;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) & (1));
    if ((uint8_t)(result) == 0) goto loc_00908887;
loc_009087EC:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8))) + ((uint32_t)(v_stack_p8)));
    local_r13 = (condition_is_equal) ? 1 : 0;
    goto loc_0090869E;
loc_00908807:
    Arg4 = 0;
    Arg4 = (v_stack_p10 != (*(uint64_t *)(v_rip + 0x6BE29C))) ? 1 : 0;
    result = ExpWnfNotifyNameSubscribers(local_r15 + 80, 4, 1, Arg4);
    goto loc_0090873A;
loc_0090882A:
    local_rsi = 0;
    goto loc_00908748;
loc_00908831:
    result = ExAcquireRundownProtection(local_r15 + 80 + 8, 4, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0090887A;
    goto loc_009086DD;
loc_00908846:
    result = ExfTryToWakePushLock(local_r15 + 80, 4, 1, Arg4);
    goto loc_00908763;
loc_00908853:
    result = ExfTryToWakePushLock(v_stack_p10, 4, 1, Arg4);
    goto loc_009086B5;
loc_00908860:
    result = ExfTryToWakePushLock(v_stack_p10, 4, 1, Arg4);
    goto loc_009086F3;
loc_0090886D:
    result = ExfTryToWakePushLock(v_stack_p10, 4, 1, Arg4);
    goto loc_00908716;
loc_0090887A:
    local_r13 = 0;
    goto loc_009086DD;
loc_00908887:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x80))) & (0));
    if ((uint8_t)(result) == 0) goto loc_00908699;
    goto loc_009087EC;
loc_0090889C:
    Arg4 = 0;
    Arg4 = (v_stack_p10 != (*(uint64_t *)(v_rip + 0x6BE207))) ? 1 : 0;
    result = ExpWnfNotifyNameSubscribers(local_r15 + 80, 8, 0, Arg4);
    goto loc_0090872F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R/W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R/W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x64` | `32` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x80` | `32` | `R` |
| `Arg2` | `+ 0x5E8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00908528&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
