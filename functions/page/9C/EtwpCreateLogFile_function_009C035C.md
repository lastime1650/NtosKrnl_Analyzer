# EtwpCreateLogFile

- RVA: `0x009C035C`–`0x009C07EF` (길이 `1,171` bytes)
- VA: `0x00000001409C035C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009F554`
- 디코드: `282`개 명령, `1,171/1,171` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x009C03C9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x009C0420` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009C0439` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009C047D` → [EtwpExpandFileName](EtwpExpandFileName_function_009C147C.md) (function, `0x009C147C`)
- `0x009C04A2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009C0521` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (function, `0x006AD5B0`)
- `0x009C0562` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009C057B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009C05C5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009C05CF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x009C05E1` → [EtwpUpdateFileHeader](EtwpUpdateFileHeader_function_009C082C.md) (function, `0x009C082C`)
- `0x009C0602` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009C0631` → [EtwpEventWriteTemplateAdmin](../AA/EtwpEventWriteTemplateAdmin_function_00AA5880.md) (function, `0x00AA5880`)
- `0x009C0676` → [RtlFreeAnsiString](RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x009C0683` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x009C0692` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009C06DD` → [EtwpDelayCreate](EtwpDelayCreate_function_009C1188.md) (function, `0x009C1188`)
- `0x009C070A` → [ZwQueryVolumeInformationFile](../../text/6A/ZwQueryVolumeInformationFile_function_006AD9F0.md) (function, `0x006AD9F0`)
- `0x009C0783` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009C0790` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009C07C0` → [EtwpFinalizeHeader](EtwpFinalizeHeader_function_009C1EF0.md) (function, `0x009C1EF0`)
- `0x009C07D8` → [EtwpSendSessionNotification](../9B/EtwpSendSessionNotification_function_009BFE28.md) (function, `0x009BFE28`)
- `0x009C07E5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [EtwpBufferingModeFlush](../9B/EtwpBufferingModeFlush_function_009BD8F4.md) at `0x009BD962`
- [EtwpLogger](../9B/EtwpLogger_function_009BE310.md) at `0x009BE63F`
- [EtwpStartLogger](../A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9AB82`

### Static image references
- `0x009C0378` → RVA `0x00E0A740` (`.data`; read)
- `0x009C0447` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x009C05F4` → RVA `0x00EFF840` (`.data`; read)
- `0x009C05FB` → RVA `0x000235D0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x009C03C9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x009C0420` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009C0439` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009C04A2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009C0521` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (`PAGE` → `.text`)
  - `0x009C0562` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009C057B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009C05C5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009C05CF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x009C0602` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009C0683` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x009C0692` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009C070A` → [ZwQueryVolumeInformationFile](../../text/6A/ZwQueryVolumeInformationFile_function_006AD9F0.md) (`PAGE` → `.text`)
  - `0x009C0783` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009C0790` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009C07E5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x009C0657` → [sub_00B2EB18 + 0x1A](../B2/Unknown_function_00B2EB18.md) (`tail-transfer`)
  - `0x009C0751` → [sub_00B2EB18](../B2/Unknown_function_00B2EB18.md) (`tail-transfer`)
  - `0x009C075F` → [sub_00B2EB18](../B2/Unknown_function_00B2EB18.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009C035C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
009C0361  55                              push rbp
009C0362  56                              push rsi
009C0363  57                              push rdi
009C0364  41 54                           push r12
009C0366  41 55                           push r13
009C0368  41 56                           push r14
009C036A  41 57                           push r15
009C036C  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
009C0371  48 81 EC E0 00 00 00            sub rsp, 0xe0
009C0378  48 8B 05 C1 A3 44 00            mov rax, qword ptr [rip + 0x44a3c1]
009C037F  48 33 C4                        xor rax, rsp
009C0382  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
009C0386  45 33 E4                        xor r12d, r12d
009C0389  4C 89 45 AF                     mov qword ptr [rbp - 0x51], r8
009C038D  0F 57 C0                        xorps xmm0, xmm0
009C0390  44 88 65 87                     mov byte ptr [rbp - 0x79], r12b
009C0394  44 8A FA                        mov r15b, dl
009C0397  4C 89 65 97                     mov qword ptr [rbp - 0x69], r12
009C039B  48 8B F9                        mov rdi, rcx
009C039E  44 88 65 88                     mov byte ptr [rbp - 0x78], r12b
009C03A2  33 C0                           xor eax, eax
009C03A4  4C 89 65 8F                     mov qword ptr [rbp - 0x71], r12
009C03A8  0F 57 C9                        xorps xmm1, xmm1
009C03AB  48 89 45 F7                     mov qword ptr [rbp - 9], rax
009C03AF  33 D2                           xor edx, edx
009C03B1  44 89 65 8B                     mov dword ptr [rbp - 0x75], r12d
009C03B5  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
009C03B9  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
009C03BD  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
009C03C1  0F 11 45 C7                     movups xmmword ptr [rbp - 0x39], xmm0
009C03C5  0F 11 4D 9F                     movups xmmword ptr [rbp - 0x61], xmm1
009C03C9  E8 B2 A3 A6 FF                  call 0x14042a780
009C03CE  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
009C03D4  A8 04                           test al, 4
009C03D6  0F 84 5C 02 00 00               je 0x1409c0638
009C03DC  F0 83 A7 38 03 00 00 FC         lock and dword ptr [rdi + 0x338], 0xfffffffc
009C03E4  4C 39 A7 A0 00 00 00            cmp qword ptr [rdi + 0xa0], r12
009C03EB  75 0D                           jne 0x1409c03fa
009C03ED  4C 39 A7 C0 00 00 00            cmp qword ptr [rdi + 0xc0], r12
009C03F4  0F 84 3E 02 00 00               je 0x1409c0638
009C03FA  4C 8D AF B8 00 00 00            lea r13, [rdi + 0xb8]
009C0401  4C 39 A7 C0 00 00 00            cmp qword ptr [rdi + 0xc0], r12
009C0408  75 07                           jne 0x1409c0411
009C040A  4C 8D AF 98 00 00 00            lea r13, [rdi + 0x98]
009C0411  48 8D 9F B0 02 00 00            lea rbx, [rdi + 0x2b0]
009C0418  45 33 C0                        xor r8d, r8d
009C041B  48 8B CB                        mov rcx, rbx
009C041E  33 D2                           xor edx, edx
009C0420  E8 0B FE 84 FF                  call 0x140210230
009C0425  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
009C042B  48 8B F0                        mov rsi, rax
009C042E  73 0E                           jae 0x1409c043e
009C0430  4C 8B C3                        mov r8, rbx
009C0433  48 8B D0                        mov rdx, rax
009C0436  48 8B CB                        mov rcx, rbx
009C0439  E8 52 F8 84 FF                  call 0x14020fc90
009C043E  48 85 F6                        test rsi, rsi
009C0441  74 04                           je 0x1409c0447
009C0443  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
009C0447  48 8B 05 5A 66 60 00            mov rax, qword ptr [rip + 0x60665a]
009C044E  48 39 87 50 05 00 00            cmp qword ptr [rdi + 0x550], rax
009C0455  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
009C045B  0F 94 C1                        sete cl
009C045E  A8 02                           test al, 2
009C0460  0F 84 0A 03 00 00               je 0x1409c0770
009C0466  44 8B 87 28 01 00 00            mov r8d, dword ptr [rdi + 0x128]
009C046D  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
009C0471  4C 8D 8F 88 00 00 00            lea r9, [rdi + 0x88]
009C0478  33 C9                           xor ecx, ecx
009C047A  49 8B D5                        mov rdx, r13
009C047D  E8 FA 0F 00 00                  call 0x1409c147c
009C0482  48 83 CB FF                     or rbx, 0xffffffffffffffff
009C0486  48 8D B7 B0 02 00 00            lea rsi, [rdi + 0x2b0]
009C048D  48 8B C3                        mov rax, rbx
009C0490  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
009C0495  24 06                           and al, 6
009C0497  3C 02                           cmp al, 2
009C0499  0F 84 E1 02 00 00               je 0x1409c0780
009C049F  48 8B CE                        mov rcx, rsi
009C04A2  E8 59 11 92 FF                  call 0x1402e1600
009C04A7  44 8B 77 0C                     mov r14d, dword ptr [rdi + 0xc]
009C04AB  41 8B CE                        mov ecx, r14d
009C04AE  41 F6 C6 04                     test r14b, 4
009C04B2  74 04                           je 0x1409c04b8
009C04B4  C6 45 87 01                     mov byte ptr [rbp - 0x79], 1
009C04B8  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
009C04BE  A8 02                           test al, 2
009C04C0  0F 85 B2 02 00 00               jne 0x1409c0778
009C04C6  41 8B CE                        mov ecx, r14d
009C04C9  45 84 FF                        test r15b, r15b
009C04CC  0F 85 C8 02 00 00               jne 0x1409c079a
009C04D2  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
009C04D6  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
009C04DA  44 8B 7D 8B                     mov r15d, dword ptr [rbp - 0x75]
009C04DE  41 C1 EE 1A                     shr r14d, 0x1a
009C04E2  41 F6 D6                        not r14b
009C04E5  41 80 E6 01                     and r14b, 1
009C04E9  0F 57 C0                        xorps xmm0, xmm0
009C04EC  48 85 F6                        test rsi, rsi
009C04EF  0F 84 BE 01 00 00               je 0x1409c06b3
009C04F5  33 C0                           xor eax, eax
009C04F7  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
009C04FF  48 89 45 F7                     mov qword ptr [rbp - 9], rax
009C0503  4C 8D 45 D7                     lea r8, [rbp - 0x29]
009C0507  48 8D 55 C7                     lea rdx, [rbp - 0x39]
009C050B  C7 45 F7 00 20 00 00            mov dword ptr [rbp - 9], 0x2000
009C0512  48 8B CE                        mov rcx, rsi
009C0515  44 8D 48 28                     lea r9d, [rax + 0x28]
009C0519  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
009C051D  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
009C0521  E8 8A D0 CE FF                  call 0x1406ad5b0
009C0526  48 83 BF 20 03 00 00 00         cmp qword ptr [rdi + 0x320], 0
009C052E  0F 85 87 02 00 00               jne 0x1409c07bb
009C0534  41 B5 01                        mov r13b, 1
009C0537  48 83 BF C0 00 00 00 00         cmp qword ptr [rdi + 0xc0], 0
009C053F  4C 8B A7 20 03 00 00            mov r12, qword ptr [rdi + 0x320]
009C0546  48 89 B7 20 03 00 00            mov qword ptr [rdi + 0x320], rsi
009C054D  0F 84 85 00 00 00               je 0x1409c05d8
009C0553  48 8D B7 B0 02 00 00            lea rsi, [rdi + 0x2b0]
009C055A  45 33 C0                        xor r8d, r8d
009C055D  48 8B CE                        mov rcx, rsi
009C0560  33 D2                           xor edx, edx
009C0562  E8 C9 FC 84 FF                  call 0x140210230
009C0567  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
009C056D  4C 8B F0                        mov r14, rax
009C0570  73 0E                           jae 0x1409c0580
009C0572  4C 8B C6                        mov r8, rsi
009C0575  48 8B D0                        mov rdx, rax
009C0578  48 8B CE                        mov rcx, rsi
009C057B  E8 10 F7 84 FF                  call 0x14020fc90
009C0580  4D 85 F6                        test r14, r14
009C0583  74 05                           je 0x1409c058a
009C0585  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
009C058A  0F 10 87 98 00 00 00            movups xmm0, xmmword ptr [rdi + 0x98]
009C0591  4C 8D B7 B8 00 00 00            lea r14, [rdi + 0xb8]
009C0598  48 8B C3                        mov rax, rbx
009C059B  41 0F 10 0E                     movups xmm1, xmmword ptr [r14]
009C059F  48 8D B7 B0 02 00 00            lea rsi, [rdi + 0x2b0]
009C05A6  F3 0F 7F 45 9F                  movdqu xmmword ptr [rbp - 0x61], xmm0
009C05AB  F3 0F 7F 8F 98 00 00 00         movdqu xmmword ptr [rdi + 0x98], xmm1
009C05B3  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
009C05B8  24 06                           and al, 6
009C05BA  3C 02                           cmp al, 2
009C05BC  0F 84 CB 01 00 00               je 0x1409c078d
009C05C2  48 8B CE                        mov rcx, rsi
009C05C5  E8 36 10 92 FF                  call 0x1402e1600
009C05CA  33 D2                           xor edx, edx
009C05CC  49 8B CE                        mov rcx, r14
009C05CF  E8 AC A1 A6 FF                  call 0x14042a780
009C05D4  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
009C05D8  8A 55 87                        mov dl, byte ptr [rbp - 0x79]
009C05DB  45 8B C7                        mov r8d, r15d
009C05DE  48 8B CF                        mov rcx, rdi
009C05E1  E8 46 02 00 00                  call 0x1409c082c
009C05E6  44 8B F8                        mov r15d, eax
009C05E9  85 C0                           test eax, eax
009C05EB  79 4F                           jns 0x1409c063c
009C05ED  4C 89 A7 20 03 00 00            mov qword ptr [rdi + 0x320], r12
009C05F4  48 8B 0D 45 F2 53 00            mov rcx, qword ptr [rip + 0x53f245]
009C05FB  48 8D 15 CE 2F 66 FF            lea rdx, [rip - 0x99d032]
009C0602  E8 49 1E 9D FF                  call 0x140392450
009C0607  84 C0                           test al, al
009C0609  74 49                           je 0x1409c0654
009C060B  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
009C060E  48 8D 8F 98 00 00 00            lea rcx, [rdi + 0x98]
009C0615  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009C0619  4C 8D 8F 88 00 00 00            lea r9, [rdi + 0x88]
009C0620  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
009C0625  48 8D 15 A4 2F 66 FF            lea rdx, [rip - 0x99d05c]
009C062C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009C0631  E8 4A 52 0E 00                  call 0x140aa5880
009C0636  EB 1C                           jmp 0x1409c0654
009C0638  33 C0                           xor eax, eax
009C063A  EB 4F                           jmp 0x1409c068b
009C063C  45 84 ED                        test r13b, r13b
009C063F  0F 84 89 01 00 00               je 0x1409c07ce
009C0645  33 F6                           xor esi, esi
009C0647  48 89 75 97                     mov qword ptr [rbp - 0x69], rsi
009C064B  4D 85 E4                        test r12, r12
009C064E  0F 85 8E 01 00 00               jne 0x1409c07e2
009C0654  48 85 F6                        test rsi, rsi
009C0657  0F 85 D5 E4 16 00               jne 0x140b2eb32
009C065D  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
009C0661  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
009C0665  48 85 C9                        test rcx, rcx
009C0668  74 05                           je 0x1409c066f
009C066A  8B 45 8B                        mov eax, dword ptr [rbp - 0x75]
009C066D  89 01                           mov dword ptr [rcx], eax
009C066F  48 8D 8F B8 00 00 00            lea rcx, [rdi + 0xb8]
009C0676  E8 85 01 00 00                  call 0x1409c0800
009C067B  48 85 F6                        test rsi, rsi
009C067E  74 08                           je 0x1409c0688
009C0680  48 8B CE                        mov rcx, rsi
009C0683  E8 C8 21 1C 00                  call 0x140b82850
009C0688  41 8B C7                        mov eax, r15d
009C068B  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
009C068F  48 33 CC                        xor rcx, rsp
009C0692  E8 A9 BF CE FF                  call 0x1406ac640
009C0697  48 8B 9C 24 28 01 00 00         mov rbx, qword ptr [rsp + 0x128]
009C069F  48 81 C4 E0 00 00 00            add rsp, 0xe0
009C06A6  41 5F                           pop r15
009C06A8  41 5E                           pop r14
009C06AA  41 5D                           pop r13
009C06AC  41 5C                           pop r12
009C06AE  5F                              pop rdi
009C06AF  5E                              pop rsi
009C06B0  5D                              pop rbp
009C06B1  C3                              ret
009C06B2  CC                              int3
009C06B3  33 C9                           xor ecx, ecx
009C06B5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009C06BA  48 89 4D 0F                     mov qword ptr [rbp + 0xf], rcx
009C06BE  4C 8D 45 87                     lea r8, [rbp - 0x79]
009C06C2  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
009C06C7  45 8A CE                        mov r9b, r14b
009C06CA  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
009C06CE  49 8B D5                        mov rdx, r13
009C06D1  48 8D 4D 97                     lea rcx, [rbp - 0x69]
009C06D5  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
009C06D9  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
009C06DD  E8 A6 0A 00 00                  call 0x1409c1188
009C06E2  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
009C06E6  44 8B F8                        mov r15d, eax
009C06E9  85 C0                           test eax, eax
009C06EB  0F 88 03 FF FF FF               js 0x1409c05f4
009C06F1  41 B9 18 00 00 00               mov r9d, 0x18
009C06F7  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
009C06FF  4C 8D 45 FF                     lea r8, [rbp - 1]
009C0703  48 8B CE                        mov rcx, rsi
009C0706  48 8D 55 B7                     lea rdx, [rbp - 0x49]
009C070A  E8 E1 D2 CE FF                  call 0x1406ad9f0
009C070F  44 8B F8                        mov r15d, eax
009C0712  85 C0                           test eax, eax
009C0714  0F 88 DA FE FF FF               js 0x1409c05f4
009C071A  80 7D 87 00                     cmp byte ptr [rbp - 0x79], 0
009C071E  44 8B 7D 13                     mov r15d, dword ptr [rbp + 0x13]
009C0722  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
009C0726  44 89 7D 8B                     mov dword ptr [rbp - 0x75], r15d
009C072A  0F 85 B9 FD FF FF               jne 0x1409c04e9
009C0730  45 84 F6                        test r14b, r14b
009C0733  0F 84 B0 FD FF FF               je 0x1409c04e9
009C0739  41 8D 47 FF                     lea eax, [r15 - 1]
009C073D  85 47 04                        test dword ptr [rdi + 4], eax
009C0740  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
009C0744  0F 84 9F FD FF FF               je 0x1409c04e9
009C074A  F7 47 0C 00 04 00 00            test dword ptr [rdi + 0xc], 0x400
009C0751  0F 85 C1 E3 16 00               jne 0x140b2eb18
009C0757  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
009C075D  A8 02                           test al, 2
009C075F  0F 85 B3 E3 16 00               jne 0x140b2eb18
009C0765  41 BF 06 02 00 C0               mov r15d, 0xc0000206
009C076B  E9 84 FE FF FF                  jmp 0x1409c05f4
009C0770  45 8B C4                        mov r8d, r12d
009C0773  E9 F5 FC FF FF                  jmp 0x1409c046d
009C0778  41 B4 01                        mov r12b, 1
009C077B  E9 49 FD FF FF                  jmp 0x1409c04c9
009C0780  48 8B CE                        mov rcx, rsi
009C0783  E8 48 56 8A FF                  call 0x140265dd0
009C0788  E9 12 FD FF FF                  jmp 0x1409c049f
009C078D  48 8B CE                        mov rcx, rsi
009C0790  E8 3B 56 8A FF                  call 0x140265dd0
009C0795  E9 28 FE FF FF                  jmp 0x1409c05c2
009C079A  48 83 BF D0 02 00 00 00         cmp qword ptr [rdi + 0x2d0], 0
009C07A2  0F 84 2A FD FF FF               je 0x1409c04d2
009C07A8  48 8D 87 C0 02 00 00            lea rax, [rdi + 0x2c0]
009C07AF  44 8B F1                        mov r14d, ecx
009C07B2  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
009C07B6  E9 1B FD FF FF                  jmp 0x1409c04d6
009C07BB  33 D2                           xor edx, edx
009C07BD  48 8B CF                        mov rcx, rdi
009C07C0  E8 2B 17 00 00                  call 0x1409c1ef0
009C07C5  44 8A 6D 88                     mov r13b, byte ptr [rbp - 0x78]
009C07C9  E9 69 FD FF FF                  jmp 0x1409c0537
009C07CE  45 33 C0                        xor r8d, r8d
009C07D1  48 8B CF                        mov rcx, rdi
009C07D4  41 8D 50 01                     lea edx, [r8 + 1]
009C07D8  E8 4B F6 FF FF                  call 0x1409bfe28
009C07DD  E9 63 FE FF FF                  jmp 0x1409c0645
009C07E2  49 8B CC                        mov rcx, r12
009C07E5  E8 C6 CA CE FF                  call 0x1406ad2b0
009C07EA  E9 65 FE FF FF                  jmp 0x1409c0654
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCreateLogFile(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD7;
    unsigned __int8 v_stack_mD8;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int8 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 4498369)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r12 = 0;
    v_stack_mB0 = a3;
    v_stack_mD8 = 0;
    v_stack_mC8 = 0;
    v_stack_mD7 = 0;
    result = 0;
    v_stack_mD0 = 0;
    v_stack_m68 = 0;
    a2 = 0;
    v_stack_mD4 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    result = RtlInitUnicodeString(v_stack_mC0, a2, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 816)))) & (4)) == 0) goto loc_009C0638;
    if ((*(unsigned __int64 *)(a1 + 160)) != 0) goto loc_009C03FA;
    if ((*(unsigned __int64 *)(a1 + 192)) == 0) goto loc_009C0638;
loc_009C03FA:
    v_r13 = a1 + 184;
    if ((*(unsigned __int64 *)(a1 + 192)) == 0) {
        v_r13 = a1 + 152;
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 688, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 688;
        a2 = result;
        a1 = a1 + 688;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a1 = ((*(unsigned __int64 *)(a1 + 1360)) == (*(unsigned __int64 *)(v_rip + 6317658))) ? 1 : 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 816)))) & (2)) == 0) goto loc_009C0770;
loc_009C046D:
    v_stack_mF8 = (unsigned __int8)(a1);
    a1 = 0;
    result = EtwpExpandFileName(a1, v_r13, (unsigned int)(*(unsigned int *)(a1 + 296)), a1 + 136);
    v_rbx = (a1 + 688) | (-1);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_009C0780;
loc_009C049F:
    result = KeAbPostRelease(a1 + 688, v_r13, (unsigned int)(*(unsigned int *)(a1 + 296)), a1 + 136);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 12)))) & (4)) != 0) {
        v_stack_mD8 = 1;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 816)))) & (2)) != 0) goto loc_009C0778;
loc_009C04C9:
    if ((unsigned __int8)((unsigned __int8)(a2)) != 0) goto loc_009C079A;
loc_009C04D2:
loc_009C04D6:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 12))) >> (26));
    v_r14 = (unsigned __int8)(~(v_r14));
    v_r14 = (unsigned __int8)((v_r14) & (1));
loc_009C04E9:
    if (v_stack_mC8 == 0) goto loc_009C06B3;
    result = 0;
    v_stack_mF8 = 4;
    v_stack_m68 = 0;
    v_stack_m68 = 0x2000ULL;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    result = ZwSetInformationFile(v_stack_mC8, v_stack_m98, v_stack_m88, result + 40);
    if ((*(unsigned __int64 *)(a1 + 800)) != 0) goto loc_009C07BB;
loc_009C0537:
    *(unsigned __int64 *)(a1 + 800) = v_stack_mC8;
    if ((*(unsigned __int64 *)(a1 + 192)) == 0) goto loc_009C05D8;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 688, a2, a3, result + 40);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 688;
        a2 = result;
        a1 = a1 + 688;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, result + 40);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_mC0 = v_xmm0;
    *(unsigned __int64 *)(a1 + 152) = v_xmm1;
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_009C078D;
loc_009C05C2:
    result = KeAbPostRelease(a1 + 688, a2, a3, result + 40);
    a2 = 0;
    result = RtlInitUnicodeString(a1 + 184, a2, a3, result + 40);
loc_009C05D8:
    result = EtwpUpdateFileHeader(a1, v_stack_mD8, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))), result + 40);
    if (!sign_flag) goto loc_009C063C;
    *(unsigned __int64 *)(a1 + 800) = *(unsigned __int64 *)(a1 + 800);
loc_009C05F4:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5501509), v_rip - 10080306, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))), result + 40);
    if ((unsigned __int8)(result) == 0) goto loc_009C0654;
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)));
    v_stack_mF0 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_mF8 = a1 + 152;
    result = EtwpEventWriteTemplateAdmin(a1 + 152, v_rip - 10080348, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))), a1 + 136);
    goto loc_009C0654;
loc_009C0638:
    result = 0;
    goto loc_009C068B;
loc_009C063C:
    if (1 == 0) goto loc_009C07CE;
loc_009C0645:
    v_rsi = 0;
    v_stack_mC8 = 0;
    if (*(unsigned __int64 *)(a1 + 800) != 0) goto loc_009C07E2;
loc_009C0654:
    if (v_stack_mB0 != 0) {
        result = v_stack_mD4;
        *(unsigned int *)(v_stack_mB0) = (unsigned int)(result);
    }
    result = RtlFreeAnsiString(a1 + 184, v_rip - 10080348, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))), a1 + 136);
    if (v_stack_mB8 != 0) {
        a1 = v_stack_mB8;
        result = ExFreePool(a1, v_rip - 10080348, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))), a1 + 136);
    }
loc_009C068B:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 10080348, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD4))), a1 + 136);
    v_rsp = (v_rsp) + (224);
    return result;
loc_009C06B3:
    a1 = 0;
    v_stack_p30 = result;
    v_stack_m50 = 0;
    v_stack_p28 = (unsigned __int8)(*(unsigned __int64 *)(a1 + 800));
    v_stack_p20 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    result = EtwpDelayCreate(v_stack_mC8, 1, v_stack_mD8, (unsigned __int8)(a1 + 184));
    if (sign_flag) goto loc_009C05F4;
    v_stack_p20 = 3;
    result = ZwQueryVolumeInformationFile(v_stack_mC8, v_stack_mA8, v_stack_m60, 24);
    if (sign_flag) goto loc_009C05F4;
    v_stack_mD4 = (unsigned int)((unsigned int)(v_stack_m4C));
    if (v_stack_mD8 != 0) goto loc_009C04E9;
    if ((unsigned __int8)(a1 + 184) == 0) goto loc_009C04E9;
    if (((*(unsigned int *)(a1 + 4)) & ((unsigned int)((unsigned int)(v_stack_m4C) - 1))) == 0) goto loc_009C04E9;
    goto loc_009C05F4;
loc_009C0770:
    goto loc_009C046D;
loc_009C0778:
    goto loc_009C04C9;
loc_009C0780:
    result = ExfTryToWakePushLock(v_stack_mC8, v_stack_mA8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 800))), 24);
    goto loc_009C049F;
loc_009C078D:
    result = ExfTryToWakePushLock(v_stack_mC8, v_stack_mA8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 800))), 24);
    goto loc_009C05C2;
loc_009C079A:
    if ((*(unsigned __int64 *)(a1 + 720)) == 0) goto loc_009C04D2;
    v_stack_mD0 = a1 + 704;
    goto loc_009C04D6;
loc_009C07BB:
    a2 = 0;
    result = EtwpFinalizeHeader(0, a2, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 800))), 24);
    goto loc_009C0537;
loc_009C07CE:
    a3 = 0;
    result = EtwpSendSessionNotification(0, a3 + 1, a3, 24);
    goto loc_009C0645;
loc_009C07E2:
    result = ZwClose(1, a3 + 1, a3, 24);
    goto loc_009C0654;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCreateLogFile(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD7;
    uint8_t v_stack_mD8;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint8_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x44A3C1)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r12 = 0;
    v_stack_mB0 = Arg3;
    v_stack_mD8 = 0;
    v_stack_mC8 = 0;
    v_stack_mD7 = 0;
    result = 0;
    v_stack_mD0 = 0;
    v_stack_m68 = 0;
    Arg2 = 0;
    v_stack_mD4 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    result = RtlInitUnicodeString(v_stack_mC0, Arg2, Arg3, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x330)))) & (4)) == 0) goto loc_009C0638;
    if ((*(uint64_t *)(arg1 + 0xA0)) != 0) goto loc_009C03FA;
    if ((*(uint64_t *)(arg1 + 0xC0)) == 0) goto loc_009C0638;
loc_009C03FA:
    local_r13 = Arg1 + 184;
    if ((*(uint64_t *)(arg1 + 0xC0)) == 0) {
        local_r13 = Arg1 + 152;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 688, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 688;
        Arg2 = result;
        Arg1 = Arg1 + 688;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg1 = ((*(uint64_t *)(arg1 + 0x550)) == (*(uint64_t *)(v_rip + 0x60665A))) ? 1 : 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x330)))) & (2)) == 0) goto loc_009C0770;
loc_009C046D:
    v_stack_mF8 = (uint8_t)(Arg1);
    Arg1 = 0;
    result = EtwpExpandFileName(Arg1, local_r13, (uint32_t)(*(uint32_t *)(arg1 + 0x128)), Arg1 + 136);
    local_rbx = (Arg1 + 688) | (-1);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_009C0780;
loc_009C049F:
    result = KeAbPostRelease(Arg1 + 688, local_r13, (uint32_t)(*(uint32_t *)(arg1 + 0x128)), Arg1 + 136);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)))) & (4)) != 0) {
        v_stack_mD8 = 1;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x330)))) & (2)) != 0) goto loc_009C0778;
loc_009C04C9:
    if ((uint8_t)((uint8_t)(Arg2)) != 0) goto loc_009C079A;
loc_009C04D2:
loc_009C04D6:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC))) >> (26));
    local_r14 = (uint8_t)(~(local_r14));
    local_r14 = (uint8_t)((local_r14) & (1));
loc_009C04E9:
    if (v_stack_mC8 == 0) goto loc_009C06B3;
    result = 0;
    v_stack_mF8 = 4;
    v_stack_m68 = 0;
    v_stack_m68 = 0x2000ULL;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    result = ZwSetInformationFile(v_stack_mC8, v_stack_m98, v_stack_m88, result + 40);
    if ((*(uint64_t *)(arg1 + 0x320)) != 0) goto loc_009C07BB;
loc_009C0537:
    *(uint64_t *)(arg1 + 0x320) = v_stack_mC8;
    if ((*(uint64_t *)(arg1 + 0xC0)) == 0) goto loc_009C05D8;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 688, Arg2, Arg3, result + 40);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 688;
        Arg2 = result;
        Arg1 = Arg1 + 688;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, result + 40);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_mC0 = v_xmm0;
    *(uint64_t *)(arg1 + 0x98) = v_xmm1;
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_009C078D;
loc_009C05C2:
    result = KeAbPostRelease(Arg1 + 688, Arg2, Arg3, result + 40);
    Arg2 = 0;
    result = RtlInitUnicodeString(Arg1 + 184, Arg2, Arg3, result + 40);
loc_009C05D8:
    result = EtwpUpdateFileHeader(Arg1, v_stack_mD8, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))), result + 40);
    if (!sign_flag) goto loc_009C063C;
    *(uint64_t *)(arg1 + 0x320) = *(uint64_t *)(arg1 + 0x320);
loc_009C05F4:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x53F245), v_rip - 10080306, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))), result + 40);
    if ((uint8_t)(result) == 0) goto loc_009C0654;
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)));
    v_stack_mF0 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_mF8 = Arg1 + 152;
    result = EtwpEventWriteTemplateAdmin(Arg1 + 152, v_rip - 10080348, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))), Arg1 + 136);
    goto loc_009C0654;
loc_009C0638:
    result = 0;
    goto loc_009C068B;
loc_009C063C:
    if (1 == 0) goto loc_009C07CE;
loc_009C0645:
    local_rsi = 0;
    v_stack_mC8 = 0;
    if (*(uint64_t *)(arg1 + 0x320) != 0) goto loc_009C07E2;
loc_009C0654:
    if (v_stack_mB0 != 0) {
        result = v_stack_mD4;
        *(uint32_t *)(v_stack_mB0) = (uint32_t)(result);
    }
    result = RtlFreeAnsiString(Arg1 + 184, v_rip - 10080348, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))), Arg1 + 136);
    if (v_stack_mB8 != 0) {
        Arg1 = v_stack_mB8;
        result = ExFreePool(Arg1, v_rip - 10080348, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))), Arg1 + 136);
    }
loc_009C068B:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 10080348, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD4))), Arg1 + 136);
    local_rsp = (local_rsp) + (224);
    return result;
loc_009C06B3:
    Arg1 = 0;
    v_stack_p30 = result;
    v_stack_m50 = 0;
    v_stack_p28 = (uint8_t)(*(uint64_t *)(arg1 + 0x320));
    v_stack_p20 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    result = EtwpDelayCreate(v_stack_mC8, 1, v_stack_mD8, (uint8_t)(Arg1 + 184));
    if (sign_flag) goto loc_009C05F4;
    v_stack_p20 = 3;
    result = ZwQueryVolumeInformationFile(v_stack_mC8, v_stack_mA8, v_stack_m60, 24);
    if (sign_flag) goto loc_009C05F4;
    v_stack_mD4 = (uint32_t)((uint32_t)(v_stack_m4C));
    if (v_stack_mD8 != 0) goto loc_009C04E9;
    if ((uint8_t)(Arg1 + 184) == 0) goto loc_009C04E9;
    if (((*(uint32_t *)(arg1 + 0x4)) & ((uint32_t)((uint32_t)(v_stack_m4C) - 1))) == 0) goto loc_009C04E9;
    goto loc_009C05F4;
loc_009C0770:
    goto loc_009C046D;
loc_009C0778:
    goto loc_009C04C9;
loc_009C0780:
    result = ExfTryToWakePushLock(v_stack_mC8, v_stack_mA8, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x320))), 24);
    goto loc_009C049F;
loc_009C078D:
    result = ExfTryToWakePushLock(v_stack_mC8, v_stack_mA8, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x320))), 24);
    goto loc_009C05C2;
loc_009C079A:
    if ((*(uint64_t *)(arg1 + 0x2D0)) == 0) goto loc_009C04D2;
    v_stack_mD0 = Arg1 + 704;
    goto loc_009C04D6;
loc_009C07BB:
    Arg2 = 0;
    result = EtwpFinalizeHeader(0, Arg2, (uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x320))), 24);
    goto loc_009C0537;
loc_009C07CE:
    Arg3 = 0;
    result = EtwpSendSessionNotification(0, Arg3 + 1, Arg3, 24);
    goto loc_009C0645;
loc_009C07E2:
    result = ZwClose(1, Arg3 + 1, Arg3, 24);
    goto loc_009C0654;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0x98` | `128` | `R` |
| `Arg1` | `+ 0x98` | `128` | `W` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0x128` | `32` | `R` |
| `Arg1` | `+ 0x2B0` | `64` | `R` |
| `Arg1` | `+ 0x2C0` | `64` | `R` |
| `Arg1` | `+ 0x2D0` | `64` | `R` |
| `Arg1` | `+ 0x320` | `64` | `R` |
| `Arg1` | `+ 0x320` | `64` | `W` |
| `Arg1` | `+ 0x330` | `32` | `R` |
| `Arg1` | `+ 0x338` | `32` | `R/W` |
| `Arg1` | `+ 0x550` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C035C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
