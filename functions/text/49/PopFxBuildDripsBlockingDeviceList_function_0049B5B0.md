# PopFxBuildDripsBlockingDeviceList

- RVA: `0x0049B5B0`–`0x0049BA1E` (길이 `1,134` bytes)
- VA: `0x000000014049B5B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B48BC`
- 디코드: `283`개 명령, `1,134/1,134` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x0049B659` → [IoLockUnlockPnpDeviceTree](../../page/AB/IoLockUnlockPnpDeviceTree_function_00AB953C.md) (function, `0x00AB953C`)
- `0x0049B690` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0049B6A9` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0049B6C6` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0049B6DF` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0049B71E` → [PopFxIsDripsBlockingDevice](PopFxIsDripsBlockingDevice_function_0049BA24.md) (function, `0x0049BA24`)
- `0x0049B759` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0049B7A8` → [IoGetDevicePropertyData](../../page/90/IoGetDevicePropertyData_function_009005E0.md) (function, `0x009005E0`)
- `0x0049B7F0` → [IoGetDevicePropertyData](../../page/90/IoGetDevicePropertyData_function_009005E0.md) (function, `0x009005E0`)
- `0x0049B84D` → [RtlPrefixUnicodeString](../../page/8F/RtlPrefixUnicodeString_function_008F4F70.md) (function, `0x008F4F70`)
- `0x0049B866` → [RtlPrefixUnicodeString](../../page/8F/RtlPrefixUnicodeString_function_008F4F70.md) (function, `0x008F4F70`)
- `0x0049B8A0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0049B8EA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0049B98F` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0049B9A1` → [PopFxDestroyDripsBlockingDeviceList](../../page/75/PopFxDestroyDripsBlockingDeviceList_function_00758DEC.md) (function, `0x00758DEC`)
- `0x0049B9B3` → [PopFxReferenceDevice](../2B/PopFxReferenceDevice_function_002BFD9C.md) (function, `0x002BFD9C`)

### Direct callers
- [PopDripsWatchdogCallbackHandler](../../page/76/PopDripsWatchdogCallbackHandler_function_0076C1C0.md) at `0x0076C26B`
- [PopDripsWatchdogTakeAction](../../page/77/PopDripsWatchdogTakeAction_function_007732D0.md) at `0x00773314`

### Static image references
- `0x0049B5D4` → RVA `0x00E0A740` (`.data`; read)
- `0x0049B5E2` → RVA `0x006CBEF8` (`.text`; read)
- `0x0049B603` → RVA `0x006CBF08` (`.text`; read)
- `0x0049B617` → RVA `0x006CBEF0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0049B62B` → RVA `0x006CBF00` (` ?? ::FNODOBFM::`string'`; read)
- `0x0049B663` → RVA `0x00F0E4C0` (`.data`; read)
- `0x0049B6B7` → RVA `0x00F0E408` (`.data`; read)
- `0x0049B6F1` → RVA `0x00F0E3F0` (`.data`; read)
- `0x0049B741` → RVA `0x00F0E408` (`.data`; read/write)
- `0x0049B77B` → RVA `0x0001AB78` (`.rdata`; read)
- `0x0049B7C8` → RVA `0x00011688` (`.rdata`; read)
- `0x0049B9EE` → RVA `0x000291E8` (`.rdata`; read)
- `0x0049B9FF` → RVA `0x000291F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x0049B659` → [IoLockUnlockPnpDeviceTree](../../page/AB/IoLockUnlockPnpDeviceTree_function_00AB953C.md) (`.text` → `PAGE`)
  - `0x0049B7A8` → [IoGetDevicePropertyData](../../page/90/IoGetDevicePropertyData_function_009005E0.md) (`.text` → `PAGE`)
  - `0x0049B7F0` → [IoGetDevicePropertyData](../../page/90/IoGetDevicePropertyData_function_009005E0.md) (`.text` → `PAGE`)
  - `0x0049B84D` → [RtlPrefixUnicodeString](../../page/8F/RtlPrefixUnicodeString_function_008F4F70.md) (`.text` → `PAGE`)
  - `0x0049B866` → [RtlPrefixUnicodeString](../../page/8F/RtlPrefixUnicodeString_function_008F4F70.md) (`.text` → `PAGE`)
  - `0x0049B8EA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0049B9A1` → [PopFxDestroyDripsBlockingDeviceList](../../page/75/PopFxDestroyDripsBlockingDeviceList_function_00758DEC.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x0049B941` → [sub_006F7B82 + 0x49](../6F/Unknown_function_006F7B82.md) (`tail-transfer`)
  - `0x0049B975` → [sub_006F7B82 + 0xE6](../6F/Unknown_function_006F7B82.md) (`tail-transfer`)
  - `0x0049B9BF` → [sub_006F7B82](../6F/Unknown_function_006F7B82.md) (`tail-transfer`)
  - `0x0049B9F9` → [sub_006F7B82 + 0x7](../6F/Unknown_function_006F7B82.md) (`tail-transfer`)
  - `0x0049BA0A` → [sub_006F7B82 + 0x7](../6F/Unknown_function_006F7B82.md) (`tail-transfer`)
  - `0x0049BA12` → [sub_006F7B82 + 0x15](../6F/Unknown_function_006F7B82.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0049B5B0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0049B5B5  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0049B5BA  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0049B5BF  55                              push rbp
0049B5C0  41 54                           push r12
0049B5C2  41 55                           push r13
0049B5C4  41 56                           push r14
0049B5C6  41 57                           push r15
0049B5C8  48 8D 6C 24 80                  lea rbp, [rsp - 0x80]
0049B5CD  48 81 EC 80 01 00 00            sub rsp, 0x180
0049B5D4  48 8B 05 65 F1 96 00            mov rax, qword ptr [rip + 0x96f165]
0049B5DB  48 33 C4                        xor rax, rsp
0049B5DE  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
0049B5E2  0F B7 05 0F 09 23 00            movzx eax, word ptr [rip + 0x23090f]
0049B5E9  0F 57 C0                        xorps xmm0, xmm0
0049B5EC  66 89 45 58                     mov word ptr [rbp + 0x58], ax
0049B5F0  45 33 ED                        xor r13d, r13d
0049B5F3  48 8D 45 50                     lea rax, [rbp + 0x50]
0049B5F7  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
0049B5FC  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0049B600  4C 8B E1                        mov r12, rcx
0049B603  0F B7 05 FE 08 23 00            movzx eax, word ptr [rip + 0x2308fe]
0049B60A  B1 01                           mov cl, 1
0049B60C  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
0049B610  4C 8B FA                        mov r15, rdx
0049B613  66 89 45 68                     mov word ptr [rbp + 0x68], ax
0049B617  F2 0F 10 05 D1 08 23 00         movsd xmm0, qword ptr [rip + 0x2308d1]
0049B61F  48 8D 45 60                     lea rax, [rbp + 0x60]
0049B623  F2 0F 11 45 50                  movsd qword ptr [rbp + 0x50], xmm0
0049B628  41 8B FD                        mov edi, r13d
0049B62B  F2 0F 10 05 CD 08 23 00         movsd xmm0, qword ptr [rip + 0x2308cd]
0049B633  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0049B638  44 89 6C 24 44                  mov dword ptr [rsp + 0x44], r13d
0049B63D  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
0049B642  48 C7 44 24 78 08 00 0A 00      mov qword ptr [rsp + 0x78], 0xa0008
0049B64B  F2 0F 11 45 60                  movsd qword ptr [rbp + 0x60], xmm0
0049B650  48 C7 44 24 68 08 00 0A 00      mov qword ptr [rsp + 0x68], 0xa0008
0049B659  E8 DE DE 61 00                  call 0x140ab953c
0049B65E  44 89 6C 24 54                  mov dword ptr [rsp + 0x54], r13d
0049B663  4C 8D 35 56 2E A7 00            lea r14, [rip + 0xa72e56]
0049B66A  B8 FF FF FF FF                  mov eax, 0xffffffff
0049B66F  48 83 CB FF                     or rbx, 0xffffffffffffffff
0049B673  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0049B677  45 33 C0                        xor r8d, r8d
0049B67A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0049B683  33 D2                           xor edx, edx
0049B685  49 8B CE                        mov rcx, r14
0049B688  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
0049B68F  90                              nop
0049B690  E8 9B 4B D7 FF                  call 0x140210230
0049B695  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0049B69B  48 8B F0                        mov rsi, rax
0049B69E  73 0E                           jae 0x14049b6ae
0049B6A0  4D 8B C6                        mov r8, r14
0049B6A3  48 8B D0                        mov rdx, rax
0049B6A6  49 8B CE                        mov rcx, r14
0049B6A9  E8 E2 45 D7 FF                  call 0x14020fc90
0049B6AE  48 85 F6                        test rsi, rsi
0049B6B1  74 04                           je 0x14049b6b7
0049B6B3  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0049B6B7  4C 8D 35 4A 2D A7 00            lea r14, [rip + 0xa72d4a]
0049B6BE  45 33 C0                        xor r8d, r8d
0049B6C1  49 8B CE                        mov rcx, r14
0049B6C4  33 D2                           xor edx, edx
0049B6C6  E8 65 4B D7 FF                  call 0x140210230
0049B6CB  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0049B6D1  48 8B F0                        mov rsi, rax
0049B6D4  73 0E                           jae 0x14049b6e4
0049B6D6  4D 8B C6                        mov r8, r14
0049B6D9  48 8B D0                        mov rdx, rax
0049B6DC  49 8B CE                        mov rcx, r14
0049B6DF  E8 AC 45 D7 FF                  call 0x14020fc90
0049B6E4  48 85 F6                        test rsi, rsi
0049B6E7  74 04                           je 0x14049b6ed
0049B6E9  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0049B6ED  4D 89 7F 08                     mov qword ptr [r15 + 8], r15
0049B6F1  48 8D 05 F8 2C A7 00            lea rax, [rip + 0xa72cf8]
0049B6F8  4D 89 3F                        mov qword ptr [r15], r15
0049B6FB  48 8B 35 EE 2C A7 00            mov rsi, qword ptr [rip + 0xa72cee]
0049B702  48 3B F0                        cmp rsi, rax
0049B705  74 3A                           je 0x14049b741
0049B707  4C 8D B6 90 03 00 00            lea r14, [rsi + 0x390]
0049B70E  4C 39 6E 30                     cmp qword ptr [rsi + 0x30], r13
0049B712  74 1E                           je 0x14049b732
0049B714  4D 8D 46 10                     lea r8, [r14 + 0x10]
0049B718  49 8B D4                        mov rdx, r12
0049B71B  48 8B CE                        mov rcx, rsi
0049B71E  E8 01 03 00 00                  call 0x14049ba24
0049B723  84 C0                           test al, al
0049B725  0F 85 80 02 00 00               jne 0x14049b9ab
0049B72B  48 8D 05 BE 2C A7 00            lea rax, [rip + 0xa72cbe]
0049B732  48 8B 36                        mov rsi, qword ptr [rsi]
0049B735  48 3B F0                        cmp rsi, rax
0049B738  75 CD                           jne 0x14049b707
0049B73A  4C 8D 35 C7 2C A7 00            lea r14, [rip + 0xa72cc7]
0049B741  F0 48 0F C1 1D BE 2C A7 00      lock xadd qword ptr [rip + 0xa72cbe], rbx
0049B74A  80 E3 06                        and bl, 6
0049B74D  80 FB 02                        cmp bl, 2
0049B750  0F 84 36 02 00 00               je 0x14049b98c
0049B756  49 8B CE                        mov rcx, r14
0049B759  E8 A2 5E E4 FF                  call 0x1402e1600
0049B75E  4D 8B 2F                        mov r13, qword ptr [r15]
0049B761  4D 3B EF                        cmp r13, r15
0049B764  0F 84 25 01 00 00               je 0x14049b88f
0049B76A  4D 8B B5 A0 FC FF FF            mov r14, qword ptr [r13 - 0x360]
0049B771  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0049B776  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0049B77B  48 8D 15 F6 F3 B7 FF            lea rdx, [rip - 0x480c0a]
0049B782  48 8D 44 24 54                  lea rax, [rsp + 0x54]
0049B787  45 33 C9                        xor r9d, r9d
0049B78A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0049B78F  45 33 C0                        xor r8d, r8d
0049B792  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
0049B796  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0049B79B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0049B7A0  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
0049B7A8  E8 33 4E 46 00                  call 0x1409005e0
0049B7AD  8B F8                           mov edi, eax
0049B7AF  85 C0                           test eax, eax
0049B7B1  78 07                           js 0x14049b7ba
0049B7B3  83 7C 24 40 08                  cmp dword ptr [rsp + 0x40], 8
0049B7B8  74 5A                           je 0x14049b814
0049B7BA  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
0049B7BE  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0049B7C3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0049B7C8  48 8D 15 B9 5E B7 FF            lea rdx, [rip - 0x48a147]
0049B7CF  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0049B7D4  45 33 C9                        xor r9d, r9d
0049B7D7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0049B7DC  45 33 C0                        xor r8d, r8d
0049B7DF  48 8D 45 A0                     lea rax, [rbp - 0x60]
0049B7E3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0049B7E8  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
0049B7F0  E8 EB 4D 46 00                  call 0x1409005e0
0049B7F5  8B F8                           mov edi, eax
0049B7F7  85 C0                           test eax, eax
0049B7F9  0F 89 D9 01 00 00               jns 0x14049b9d8
0049B7FF  33 FF                           xor edi, edi
0049B801  EB 08                           jmp 0x14049b80b
0049B803  85 F6                           test esi, esi
0049B805  0F 85 BC 00 00 00               jne 0x14049b8c7
0049B80B  4D 8B 6D 00                     mov r13, qword ptr [r13]
0049B80F  E9 4D FF FF FF                  jmp 0x14049b761
0049B814  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0049B818  33 F6                           xor esi, esi
0049B81A  49 8B DE                        mov rbx, r14
0049B81D  EB 07                           jmp 0x14049b826
0049B81F  48 8B D8                        mov rbx, rax
0049B822  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0049B826  48 85 C0                        test rax, rax
0049B829  75 F4                           jne 0x14049b81f
0049B82B  49 3B DE                        cmp rbx, r14
0049B82E  74 D3                           je 0x14049b803
0049B830  83 BB 9C 00 00 00 01            cmp dword ptr [rbx + 0x9c], 1
0049B837  75 3A                           jne 0x14049b873
0049B839  F0 83 A3 28 01 00 00 DF         lock and dword ptr [rbx + 0x128], 0xffffffdf
0049B841  45 33 C0                        xor r8d, r8d
0049B844  48 8D 53 28                     lea rdx, [rbx + 0x28]
0049B848  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
0049B84D  E8 1E 97 45 00                  call 0x1408f4f70
0049B852  84 C0                           test al, al
0049B854  0F 85 B5 01 00 00               jne 0x14049ba0f
0049B85A  45 33 C0                        xor r8d, r8d
0049B85D  48 8D 53 28                     lea rdx, [rbx + 0x28]
0049B861  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0049B866  E8 05 97 45 00                  call 0x1408f4f70
0049B86B  84 C0                           test al, al
0049B86D  0F 85 9C 01 00 00               jne 0x14049ba0f
0049B873  48 8B 03                        mov rax, qword ptr [rbx]
0049B876  48 85 C0                        test rax, rax
0049B879  74 0E                           je 0x14049b889
0049B87B  48 8B D8                        mov rbx, rax
0049B87E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0049B882  48 85 C0                        test rax, rax
0049B885  75 F4                           jne 0x14049b87b
0049B887  EB A2                           jmp 0x14049b82b
0049B889  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
0049B88D  EB 9C                           jmp 0x14049b82b
0049B88F  85 FF                           test edi, edi
0049B891  0F 88 07 01 00 00               js 0x14049b99e
0049B897  8B C7                           mov eax, edi
0049B899  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
0049B89D  48 33 CC                        xor rcx, rsp
0049B8A0  E8 9B 0D 21 00                  call 0x1406ac640
0049B8A5  4C 8D 9C 24 80 01 00 00         lea r11, [rsp + 0x180]
0049B8AD  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0049B8B1  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0049B8B5  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0049B8B9  49 8B E3                        mov rsp, r11
0049B8BC  41 5F                           pop r15
0049B8BE  41 5E                           pop r14
0049B8C0  41 5D                           pop r13
0049B8C2  41 5C                           pop r12
0049B8C4  5D                              pop rbp
0049B8C5  C3                              ret
0049B8C6  CC                              int3
0049B8C7  8B C6                           mov eax, esi
0049B8C9  B9 FF FF FF FF                  mov ecx, 0xffffffff
0049B8CE  48 C1 E0 03                     shl rax, 3
0049B8D2  48 3B C1                        cmp rax, rcx
0049B8D5  0F 87 BE 00 00 00               ja 0x14049b999
0049B8DB  8B D0                           mov edx, eax
0049B8DD  B9 00 01 00 00                  mov ecx, 0x100
0049B8E2  41 B8 50 46 58 4D               mov r8d, 0x4d584650
0049B8E8  33 FF                           xor edi, edi
0049B8EA  E8 01 68 6E 00                  call 0x140b820f0
0049B8EF  45 33 C9                        xor r9d, r9d
0049B8F2  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0049B8F6  4C 8B C0                        mov r8, rax
0049B8F9  48 85 C0                        test rax, rax
0049B8FC  0F 84 15 01 00 00               je 0x14049ba17
0049B902  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0049B906  41 8B D9                        mov ebx, r9d
0049B909  49 8B D6                        mov rdx, r14
0049B90C  EB 07                           jmp 0x14049b915
0049B90E  48 8B D1                        mov rdx, rcx
0049B911  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0049B915  48 85 C9                        test rcx, rcx
0049B918  75 F4                           jne 0x14049b90e
0049B91A  49 3B D6                        cmp rdx, r14
0049B91D  74 54                           je 0x14049b973
0049B91F  0F 0D 8A 28 01 00 00            prefetchw byte ptr [rdx + 0x128]
0049B926  8B 82 28 01 00 00               mov eax, dword ptr [rdx + 0x128]
0049B92C  8B C8                           mov ecx, eax
0049B92E  41 0B C9                        or ecx, r9d
0049B931  F0 0F B1 8A 28 01 00 00         lock cmpxchg dword ptr [rdx + 0x128], ecx
0049B939  75 F1                           jne 0x14049b92c
0049B93B  A8 20                           test al, 0x20
0049B93D  74 18                           je 0x14049b957
0049B93F  3B DE                           cmp ebx, esi
0049B941  0F 83 84 C2 25 00               jae 0x1406f7bcb
0049B947  F0 83 A2 28 01 00 00 DF         lock and dword ptr [rdx + 0x128], 0xffffffdf
0049B94F  8B C3                           mov eax, ebx
0049B951  FF C3                           inc ebx
0049B953  49 89 14 C0                     mov qword ptr [r8 + rax*8], rdx
0049B957  48 8B 02                        mov rax, qword ptr [rdx]
0049B95A  48 85 C0                        test rax, rax
0049B95D  74 0E                           je 0x14049b96d
0049B95F  48 8B D0                        mov rdx, rax
0049B962  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0049B966  48 85 C0                        test rax, rax
0049B969  75 F4                           jne 0x14049b95f
0049B96B  EB AD                           jmp 0x14049b91a
0049B96D  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
0049B971  EB A7                           jmp 0x14049b91a
0049B973  3B DE                           cmp ebx, esi
0049B975  0F 85 ED C2 25 00               jne 0x1406f7c68
0049B97B  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0049B97F  49 89 45 18                     mov qword ptr [r13 + 0x18], rax
0049B983  41 89 5D 20                     mov dword ptr [r13 + 0x20], ebx
0049B987  E9 7F FE FF FF                  jmp 0x14049b80b
0049B98C  49 8B CE                        mov rcx, r14
0049B98F  E8 3C A4 DC FF                  call 0x140265dd0
0049B994  E9 BD FD FF FF                  jmp 0x14049b756
0049B999  BF 95 00 00 C0                  mov edi, 0xc0000095
0049B99E  49 8B CF                        mov rcx, r15
0049B9A1  E8 46 D4 2B 00                  call 0x140758dec
0049B9A6  E9 EC FE FF FF                  jmp 0x14049b897
0049B9AB  BA 03 00 00 00                  mov edx, 3
0049B9B0  48 8B CE                        mov rcx, rsi
0049B9B3  E8 E4 43 E2 FF                  call 0x1402bfd9c
0049B9B8  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0049B9BC  4C 39 38                        cmp qword ptr [rax], r15
0049B9BF  0F 85 BD C1 25 00               jne 0x1406f7b82
0049B9C5  4D 89 3E                        mov qword ptr [r14], r15
0049B9C8  49 89 46 08                     mov qword ptr [r14 + 8], rax
0049B9CC  4C 89 30                        mov qword ptr [rax], r14
0049B9CF  4D 89 77 08                     mov qword ptr [r15 + 8], r14
0049B9D3  E9 53 FD FF FF                  jmp 0x14049b72b
0049B9D8  83 7C 24 44 0D                  cmp dword ptr [rsp + 0x44], 0xd
0049B9DD  0F 85 1C FE FF FF               jne 0x14049b7ff
0049B9E3  83 7C 24 48 10                  cmp dword ptr [rsp + 0x48], 0x10
0049B9E8  0F 85 11 FE FF FF               jne 0x14049b7ff
0049B9EE  48 8B 05 F3 D7 B8 FF            mov rax, qword ptr [rip - 0x47280d]
0049B9F5  48 2B 45 A0                     sub rax, qword ptr [rbp - 0x60]
0049B9F9  0F 85 8A C1 25 00               jne 0x1406f7b89
0049B9FF  48 8B 05 EA D7 B8 FF            mov rax, qword ptr [rip - 0x472816]
0049BA06  48 2B 45 A8                     sub rax, qword ptr [rbp - 0x58]
0049BA0A  E9 7A C1 25 00                  jmp 0x1406f7b89
0049BA0F  48 8B C3                        mov rax, rbx
0049BA12  E9 80 C1 25 00                  jmp 0x1406f7b97
0049BA17  BF 9A 00 00 C0                  mov edi, 0xc000009a
0049BA1C  EB 80                           jmp 0x14049b99e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxBuildDripsBlockingDeviceList(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned int v_stack_m160;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int16 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int16 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 9892197)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m50 = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 2296079));
    v_r13 = 0;
    v_stack_m160 = 0;
    v_stack_m128 = v_stack_m58;
    v_stack_m108 = v_xmm0;
    v_stack_m40 = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 2296062));
    v_stack_m58 = v_xmm0;
    v_stack_m138 = v_stack_m48;
    v_stack_m164 = 0;
    v_stack_m158 = 0;
    v_stack_m130 = 0xA0008ULL;
    v_stack_m48 = v_xmm0;
    v_stack_m140 = 0xA0008ULL;
    result = IoLockUnlockPnpDeviceTree(1, a2, a3, a4);
    v_stack_m154 = 0;
    v_rbx = (v_rbx) | (-1);
    v_stack_m168 = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 10956374, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 10956374;
        a2 = result;
        a1 = v_rip + 10956374;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 10956106, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 10956106;
        a2 = result;
        a1 = v_rip + 10956106;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(a2 + 8) = a2;
    *(unsigned __int64 *)(a2) = a2;
    if ((*(unsigned __int64 *)(v_rip + 10956014)) == (v_rip + 10956024)) goto loc_0049B741;
loc_0049B707:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10956014) + 48)) == 0) goto loc_0049B732;
    result = PopFxIsDripsBlockingDevice(*(unsigned __int64 *)(v_rip + 10956014), a1, *(unsigned __int64 *)(v_rip + 10956014) + 912 + 16, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0049B9AB;
loc_0049B72B:
loc_0049B732:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10956014))) != (v_rip + 10955966)) goto loc_0049B707;
loc_0049B741:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_0049B98C;
loc_0049B756:
    result = KeAbPostRelease(v_rip + 10955975, a1, *(unsigned __int64 *)(v_rip + 10956014) + 912 + 16, a4);
loc_0049B761:
    if ((*(unsigned __int64 *)(a2)) == a2) goto loc_0049B88F;
    v_stack_m170 = v_stack_m158;
    a4 = 0;
    v_stack_m178 = v_stack_m154;
    a3 = 0;
    v_stack_m180 = v_stack_m168;
    v_stack_m188 = 4;
    result = IoGetDevicePropertyData(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 32), v_rip - 4721674, a3, a4);
    if (sign_flag) goto loc_0049B7BA;
    if (v_stack_m168 == 8) goto loc_0049B814;
loc_0049B7BA:
    v_stack_m170 = v_stack_m164;
    a4 = 0;
    v_stack_m178 = v_stack_m160;
    a3 = 0;
    v_stack_m180 = v_stack_m108;
    v_stack_m188 = 16;
    result = IoGetDevicePropertyData(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 32), v_rip - 4759879, a3, a4);
    if (!sign_flag) goto loc_0049B9D8;
loc_0049B7FF:
    v_rdi = 0;
    goto loc_0049B80B;
loc_0049B803:
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10956014))) != 0) goto loc_0049B8C7;
loc_0049B80B:
    goto loc_0049B761;
loc_0049B814:
    v_rsi = 0;
    goto loc_0049B826;
loc_0049B81F:
loc_0049B826:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8) + 8) != 0) goto loc_0049B81F;
loc_0049B82B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864))) goto loc_0049B803;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8) + 156)) != 1) goto loc_0049B873;
    a3 = 0;
    result = RtlPrefixUnicodeString(v_stack_m140, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8) + 40, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0049BA0F;
    a3 = 0;
    result = RtlPrefixUnicodeString(v_stack_m130, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8) + 40, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0049BA0F;
loc_0049B873:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8)) == 0) goto loc_0049B889;
loc_0049B87B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8)) + 8) != 0) goto loc_0049B87B;
    goto loc_0049B82B;
loc_0049B889:
    goto loc_0049B82B;
loc_0049B88F:
    if (sign_flag) goto loc_0049B99E;
loc_0049B897:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8) + 40, a3, a4);
    return result;
loc_0049B8C7:
    result = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)))) << (3);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_0049B999;
    v_rdi = 0;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x4D584650ULL), a4);
    a4 = 0;
    v_stack_m110 = result;
    if (result == 0) goto loc_0049BA17;
    goto loc_0049B915;
loc_0049B90E:
loc_0049B915:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8) + 8) != 0) goto loc_0049B90E;
loc_0049B91A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864))) goto loc_0049B973;
loc_0049B92C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8) + 296))))) | (0));
    if (condition_is_not_equal) goto loc_0049B92C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8) + 296)))) & (32)) == 0) goto loc_0049B957;
    v_rbx = (unsigned int)((0) + 1);
    *(unsigned __int64 *)(result + 0 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8);
loc_0049B957:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8)) == 0) goto loc_0049B96D;
loc_0049B95F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8)) + 8) != 0) goto loc_0049B95F;
    goto loc_0049B91A;
loc_0049B96D:
    goto loc_0049B91A;
loc_0049B973:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 24) = v_stack_m110;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 32) = (unsigned int)(v_rbx);
    goto loc_0049B80B;
loc_0049B98C:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8)) + 16), result, a4);
    goto loc_0049B756;
loc_0049B999:
loc_0049B99E:
    result = PopFxDestroyDripsBlockingDeviceList(a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8)) + 16), result, a4);
    goto loc_0049B897;
loc_0049B9AB:
    result = PopFxReferenceDevice(*(unsigned __int64 *)(v_stack_m28 + 64), 3, result, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864)) = a2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864) + 8) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864);
    *(unsigned __int64 *)(a2 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2) - 864);
    goto loc_0049B72B;
loc_0049B9D8:
    if (v_stack_m13C != 13) goto loc_0049B7FF;
    if (v_stack_m138 != 16) goto loc_0049B7FF;
    result = (*(unsigned __int64 *)(v_rip - 4663309)) - (v_stack_m108);
    result = (*(unsigned __int64 *)(v_rip - 4663318)) - (v_stack_m100);
loc_0049BA0F:
loc_0049BA17:
    goto loc_0049B99E;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxBuildDripsBlockingDeviceList(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint64_t v_stack_m140;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint32_t v_stack_m160;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint16_t v_stack_m40;
    uint64_t v_stack_m48;
    uint16_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0x96F165)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m50 = (uint16_t)(*(uint16_t *)(v_rip + 0x23090F));
    local_r13 = 0;
    v_stack_m160 = 0;
    v_stack_m128 = v_stack_m58;
    v_stack_m108 = v_xmm0;
    v_stack_m40 = (uint16_t)(*(uint16_t *)(v_rip + 0x2308FE));
    v_stack_m58 = v_xmm0;
    v_stack_m138 = v_stack_m48;
    v_stack_m164 = 0;
    v_stack_m158 = 0;
    v_stack_m130 = 0xA0008ULL;
    v_stack_m48 = v_xmm0;
    v_stack_m140 = 0xA0008ULL;
    result = IoLockUnlockPnpDeviceTree(1, Arg2, Arg3, Arg4);
    v_stack_m154 = 0;
    local_rbx = (local_rbx) | (-1);
    v_stack_m168 = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 10956374, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 10956374;
        Arg2 = result;
        Arg1 = v_rip + 10956374;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 10956106, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 10956106;
        Arg2 = result;
        Arg1 = v_rip + 10956106;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(void **)(arg2 + 0x8) = Arg2;
    *(void **)(arg2) = Arg2;
    if ((*(uint64_t *)(v_rip + 0xA72CEE)) == (v_rip + 10956024)) goto loc_0049B741;
loc_0049B707:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72CEE) + 0x30)) == 0) goto loc_0049B732;
    result = PopFxIsDripsBlockingDevice(*(uint64_t *)(v_rip + 0xA72CEE), Arg1, *(uint64_t *)(v_rip + 0xA72CEE) + 912 + 16, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0049B9AB;
loc_0049B72B:
loc_0049B732:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72CEE))) != (v_rip + 10955966)) goto loc_0049B707;
loc_0049B741:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_0049B98C;
loc_0049B756:
    result = KeAbPostRelease(v_rip + 10955975, Arg1, *(uint64_t *)(v_rip + 0xA72CEE) + 912 + 16, Arg4);
loc_0049B761:
    if ((*(uint64_t *)(arg2)) == Arg2) goto loc_0049B88F;
    v_stack_m170 = v_stack_m158;
    Arg4 = 0;
    v_stack_m178 = v_stack_m154;
    Arg3 = 0;
    v_stack_m180 = v_stack_m168;
    v_stack_m188 = 4;
    result = IoGetDevicePropertyData(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x20), v_rip - 4721674, Arg3, Arg4);
    if (sign_flag) goto loc_0049B7BA;
    if (v_stack_m168 == 8) goto loc_0049B814;
loc_0049B7BA:
    v_stack_m170 = v_stack_m164;
    Arg4 = 0;
    v_stack_m178 = v_stack_m160;
    Arg3 = 0;
    v_stack_m180 = v_stack_m108;
    v_stack_m188 = 16;
    result = IoGetDevicePropertyData(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x20), v_rip - 4759879, Arg3, Arg4);
    if (!sign_flag) goto loc_0049B9D8;
loc_0049B7FF:
    local_rdi = 0;
    goto loc_0049B80B;
loc_0049B803:
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA72CEE))) != 0) goto loc_0049B8C7;
loc_0049B80B:
    goto loc_0049B761;
loc_0049B814:
    local_rsi = 0;
    goto loc_0049B826;
loc_0049B81F:
loc_0049B826:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8) + 0x8) != 0) goto loc_0049B81F;
loc_0049B82B:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(arg2) - 0x360))) goto loc_0049B803;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8) + 0x9C)) != 1) goto loc_0049B873;
    Arg3 = 0;
    result = RtlPrefixUnicodeString(v_stack_m140, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8) + 40, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0049BA0F;
    Arg3 = 0;
    result = RtlPrefixUnicodeString(v_stack_m130, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8) + 40, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0049BA0F;
loc_0049B873:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8)) == 0) goto loc_0049B889;
loc_0049B87B:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8)) + 0x8) != 0) goto loc_0049B87B;
    goto loc_0049B82B;
loc_0049B889:
    goto loc_0049B82B;
loc_0049B88F:
    if (sign_flag) goto loc_0049B99E;
loc_0049B897:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8) + 40, Arg3, Arg4);
    return result;
loc_0049B8C7:
    result = ((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)))) << (3);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_0049B999;
    local_rdi = 0;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x4D584650ULL), Arg4);
    Arg4 = 0;
    v_stack_m110 = result;
    if (result == 0) goto loc_0049BA17;
    goto loc_0049B915;
loc_0049B90E:
loc_0049B915:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8) + 0x8) != 0) goto loc_0049B90E;
loc_0049B91A:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(arg2) - 0x360))) goto loc_0049B973;
loc_0049B92C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8) + 0x128))))) | (0));
    if (condition_is_not_equal) goto loc_0049B92C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8) + 0x128)))) & (32)) == 0) goto loc_0049B957;
    local_rbx = (uint32_t)((0) + 1);
    *(uint64_t *)(result + 0x0 * 8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8);
loc_0049B957:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8)) == 0) goto loc_0049B96D;
loc_0049B95F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8)) + 0x8) != 0) goto loc_0049B95F;
    goto loc_0049B91A;
loc_0049B96D:
    goto loc_0049B91A;
loc_0049B973:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2)) + 0x18) = v_stack_m110;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2)) + 0x20) = (uint32_t)(local_rbx);
    goto loc_0049B80B;
loc_0049B98C:
    result = ExfTryToWakePushLock(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8)) + 0x10), result, Arg4);
    goto loc_0049B756;
loc_0049B999:
loc_0049B99E:
    result = PopFxDestroyDripsBlockingDeviceList(Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8)) + 0x10), result, Arg4);
    goto loc_0049B897;
loc_0049B9AB:
    result = PopFxReferenceDevice(*(uint64_t *)(v_stack_m28 + 0x40), 3, result, Arg4);
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360)) = Arg2;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) - 0x360) + 0x8) = *(uint64_t *)(arg2 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg2) - 0x360);
    *(uint64_t *)(arg2 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg2) - 0x360);
    goto loc_0049B72B;
loc_0049B9D8:
    if (v_stack_m13C != 13) goto loc_0049B7FF;
    if (v_stack_m138 != 16) goto loc_0049B7FF;
    result = (*(uint64_t *)(v_rip - 0x47280D)) - (v_stack_m108);
    result = (*(uint64_t *)(v_rip - 0x472816)) - (v_stack_m100);
loc_0049BA0F:
loc_0049BA17:
    goto loc_0049B99E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049B5B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
