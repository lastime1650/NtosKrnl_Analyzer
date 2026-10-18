# ObpCreateSymbolicLinkName

- RVA: `0x0074EB80`–`0x0074EF88` (길이 `1,032` bytes)
- VA: `0x000000014074EB80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3D64`
- 디코드: `286`개 명령, `1,032/1,032` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0074EC0A` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0074EC31` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (function, `0x004094A0`)
- `0x0074EC39` → [OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO](../../text/40/OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO_function_00409500.md) (function, `0x00409500`)
- `0x0074EC48` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0074EC59` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0074ECAE` → [ObpLockDirectoryShared](../99/ObpLockDirectoryShared_function_0099EF20.md) (function, `0x0099EF20`)
- `0x0074ECBB` → [ObpParseComponentName](../99/ObpParseComponentName_function_0099E640.md) (function, `0x0099E640`)
- `0x0074ECD2` → [ObpLookupDirectoryEntry](../85/ObpLookupDirectoryEntry_function_0085D5B0.md) (function, `0x0085D5B0`)
- `0x0074ED22` → [ObpLockChildDirectory](../9D/ObpLockChildDirectory_function_009D60F0.md) (function, `0x009D60F0`)
- `0x0074ED3E` → [Feature_2735186232__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_2735186232__private_IsEnabledDeviceUsageNoInline_function_005CD914.md) (function, `0x005CD914`)
- `0x0074ED4B` → [ObpUnlockDirectory](../99/ObpUnlockDirectory_function_0099F8A0.md) (function, `0x0099F8A0`)
- `0x0074ED55` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0074ED5E` → [ObpUnlockDirectory](../99/ObpUnlockDirectory_function_0099F8A0.md) (function, `0x0099F8A0`)
- `0x0074ED6B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0074EE75` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0074EE9B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0074EEB4` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0074EEF0` → [ObFastReplaceObject](../../text/45/ObFastReplaceObject_function_0045819C.md) (function, `0x0045819C`)
- `0x0074EF21` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0074EF29` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0074EF2E` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)
- `0x0074EF3B` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (function, `0x003FCE40`)
- `0x0074EF4C` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x0074EF51` → [Feature_2735186232__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_2735186232__private_IsEnabledDeviceUsageNoInline_function_005CD914.md) (function, `0x005CD914`)
- `0x0074EF62` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0074EF6A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [ObpCreateHandle](../86/ObpCreateHandle_function_0086B950.md) at `0x0086CDEB`

### Static image references
- `0x0074EBC3` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0074ECFD` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0074ED0F` → RVA `0x00F0F650` (`.data`; read)
- `0x0074ED29` → RVA `0x00F0F658` (`.data`; read)
- `0x0074ED94` → RVA `0x00F0F668` (`.data`; read)
- `0x0074EDDE` → RVA `0x00FC6EE0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x0074EC31` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (`PAGE` → `.text`)
  - `0x0074EC39` → [OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO](../../text/40/OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO_function_00409500.md) (`PAGE` → `.text`)
  - `0x0074EC48` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0074EC59` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0074ED3E` → [Feature_2735186232__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_2735186232__private_IsEnabledDeviceUsageNoInline_function_005CD914.md) (`PAGE` → `.text`)
  - `0x0074ED55` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0074ED6B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0074EE75` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0074EE9B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0074EEB4` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0074EEF0` → [ObFastReplaceObject](../../text/45/ObFastReplaceObject_function_0045819C.md) (`PAGE` → `.text`)
  - `0x0074EF21` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0074EF29` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0074EF2E` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (`PAGE` → `.text`)
  - `0x0074EF3B` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (`PAGE` → `.text`)
  - `0x0074EF4C` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x0074EF51` → [Feature_2735186232__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_2735186232__private_IsEnabledDeviceUsageNoInline_function_005CD914.md) (`PAGE` → `.text`)
  - `0x0074EF62` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0074EF6A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0074EB80  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0074EB85  55                              push rbp
0074EB86  56                              push rsi
0074EB87  57                              push rdi
0074EB88  41 54                           push r12
0074EB8A  41 55                           push r13
0074EB8C  41 56                           push r14
0074EB8E  41 57                           push r15
0074EB90  48 8B EC                        mov rbp, rsp
0074EB93  48 83 EC 60                     sub rsp, 0x60
0074EB97  45 33 E4                        xor r12d, r12d
0074EB9A  48 8D 51 D0                     lea rdx, [rcx - 0x30]
0074EB9E  0F B6 42 1A                     movzx eax, byte ptr [rdx + 0x1a]
0074EBA2  0F 57 C0                        xorps xmm0, xmm0
0074EBA5  4C 89 65 40                     mov qword ptr [rbp + 0x40], r12
0074EBA9  48 8B D9                        mov rbx, rcx
0074EBAC  BF 40 00 00 00                  mov edi, 0x40
0074EBB1  45 8B F4                        mov r14d, r12d
0074EBB4  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0074EBB8  A8 02                           test al, 2
0074EBBA  0F 84 AF 03 00 00               je 0x14074ef6f
0074EBC0  83 E0 03                        and eax, 3
0074EBC3  48 8D 0D 36 14 8B FF            lea rcx, [rip - 0x74ebca]
0074EBCA  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0074EBD2  48 2B D0                        sub rdx, rax
0074EBD5  0F 84 94 03 00 00               je 0x14074ef6f
0074EBDB  48 8B 02                        mov rax, qword ptr [rdx]
0074EBDE  4C 39 A0 30 01 00 00            cmp qword ptr [rax + 0x130], r12
0074EBE5  0F 84 84 03 00 00               je 0x14074ef6f
0074EBEB  8D 47 C4                        lea eax, [rdi - 0x3c]
0074EBEE  66 39 42 08                     cmp word ptr [rdx + 8], ax
0074EBF2  0F 85 77 03 00 00               jne 0x14074ef6f
0074EBF8  48 8B 4A 10                     mov rcx, qword ptr [rdx + 0x10]
0074EBFC  66 83 79 02 3A                  cmp word ptr [rcx + 2], 0x3a
0074EC01  0F 85 68 03 00 00               jne 0x14074ef6f
0074EC07  0F B7 09                        movzx ecx, word ptr [rcx]
0074EC0A  E8 E1 04 11 00                  call 0x14085f0f0
0074EC0F  8D 48 BF                        lea ecx, [rax - 0x41]
0074EC12  66 83 F9 19                     cmp cx, 0x19
0074EC16  0F 87 53 03 00 00               ja 0x14074ef6f
0074EC1C  0F B7 C0                        movzx eax, ax
0074EC1F  0F 57 C0                        xorps xmm0, xmm0
0074EC22  2B C7                           sub eax, edi
0074EC24  89 43 18                        mov dword ptr [rbx + 0x18], eax
0074EC27  33 C0                           xor eax, eax
0074EC29  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0074EC2D  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0074EC31  E8 6A A8 CB FF                  call 0x1404094a0
0074EC36  48 8B C8                        mov rcx, rax
0074EC39  E8 C2 A8 CB FF                  call 0x140409500
0074EC3E  48 8B C8                        mov rcx, rax
0074EC41  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0074EC45  4C 8B F8                        mov r15, rax
0074EC48  E8 D3 0D AC FF                  call 0x14020fa20
0074EC4D  0F 10 43 08                     movups xmm0, xmmword ptr [rbx + 8]
0074EC51  49 8B D7                        mov rdx, r15
0074EC54  F3 0F 7F 45 C0                  movdqu xmmword ptr [rbp - 0x40], xmm0
0074EC59  E8 92 F5 BA FF                  call 0x1402fe1f0
0074EC5E  4C 8B E8                        mov r13, rax
0074EC61  41 BB 08 00 00 00               mov r11d, 8
0074EC67  49 8B 4D 00                     mov rcx, qword ptr [r13]
0074EC6B  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0074EC6F  4C 8B 09                        mov r9, qword ptr [rcx]
0074EC72  4D 85 C9                        test r9, r9
0074EC75  74 33                           je 0x14074ecaa
0074EC77  0F B7 4D C0                     movzx ecx, word ptr [rbp - 0x40]
0074EC7B  66 41 3B CB                     cmp cx, r11w
0074EC7F  72 29                           jb 0x14074ecaa
0074EC81  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
0074EC85  49 BA 5C 00 3F 00 3F 00 5C 00   movabs r10, 0x5c003f003f005c
0074EC8F  4D 39 10                        cmp qword ptr [r8], r10
0074EC92  75 16                           jne 0x14074ecaa
0074EC94  4D 03 C3                        add r8, r11
0074EC97  B8 F8 FF 00 00                  mov eax, 0xfff8
0074EC9C  66 03 C8                        add cx, ax
0074EC9F  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
0074ECA3  66 89 4D C0                     mov word ptr [rbp - 0x40], cx
0074ECA7  49 8B D1                        mov rdx, r9
0074ECAA  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0074ECAE  E8 6D 02 25 00                  call 0x14099ef20
0074ECB3  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0074ECB7  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0074ECBB  E8 80 F9 24 00                  call 0x14099e640
0074ECC0  84 C0                           test al, al
0074ECC2  0F 84 80 02 00 00               je 0x14074ef48
0074ECC8  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0074ECCC  33 D2                           xor edx, edx
0074ECCE  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0074ECD2  E8 D9 E8 10 00                  call 0x14085d5b0
0074ECD7  48 8B F0                        mov rsi, rax
0074ECDA  48 85 C0                        test rax, rax
0074ECDD  0F 84 C6 00 00 00               je 0x14074eda9
0074ECE3  48 8D 48 D0                     lea rcx, [rax - 0x30]
0074ECE7  48 C1 E9 08                     shr rcx, 8
0074ECEB  44 0F B6 C1                     movzx r8d, cl
0074ECEF  0F B6 48 E8                     movzx ecx, byte ptr [rax - 0x18]
0074ECF3  48 8D 05 06 13 8B FF            lea rax, [rip - 0x74ecfa]
0074ECFA  4C 33 C1                        xor r8, rcx
0074ECFD  0F B6 0D 48 81 87 00            movzx ecx, byte ptr [rip + 0x878148]
0074ED04  4C 33 C1                        xor r8, rcx
0074ED07  4A 8B 84 C0 00 78 FC 00         mov rax, qword ptr [rax + r8*8 + 0xfc7800]
0074ED0F  48 3B 05 3A 09 7C 00            cmp rax, qword ptr [rip + 0x7c093a]
0074ED16  75 11                           jne 0x14074ed29
0074ED18  45 33 C0                        xor r8d, r8d
0074ED1B  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0074ED1F  48 8B D6                        mov rdx, rsi
0074ED22  E8 C9 73 28 00                  call 0x1409d60f0
0074ED27  EB 8A                           jmp 0x14074ecb3
0074ED29  48 3B 05 28 09 7C 00            cmp rax, qword ptr [rip + 0x7c0928]
0074ED30  75 77                           jne 0x14074eda9
0074ED32  44 39 66 18                     cmp dword ptr [rsi + 0x18], r12d
0074ED36  75 71                           jne 0x14074eda9
0074ED38  85 FF                           test edi, edi
0074ED3A  74 6A                           je 0x14074eda6
0074ED3C  FF CF                           dec edi
0074ED3E  E8 D1 EB E7 FF                  call 0x1405cd914
0074ED43  85 C0                           test eax, eax
0074ED45  75 0B                           jne 0x14074ed52
0074ED47  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0074ED4B  E8 50 0B 25 00                  call 0x14099f8a0
0074ED50  EB 25                           jmp 0x14074ed77
0074ED52  48 8B CE                        mov rcx, rsi
0074ED55  E8 C6 0C AC FF                  call 0x14020fa20
0074ED5A  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0074ED5E  E8 3D 0B 25 00                  call 0x14099f8a0
0074ED63  4D 85 F6                        test r14, r14
0074ED66  74 08                           je 0x14074ed70
0074ED68  49 8B CE                        mov rcx, r14
0074ED6B  E8 E0 A5 BA FF                  call 0x1402f9350
0074ED70  4C 8B F6                        mov r14, rsi
0074ED73  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
0074ED77  66 44 39 65 C0                  cmp word ptr [rbp - 0x40], r12w
0074ED7C  75 07                           jne 0x14074ed85
0074ED7E  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
0074ED81  A8 0E                           test al, 0xe
0074ED83  74 04                           je 0x14074ed89
0074ED85  83 63 1C DF                     and dword ptr [rbx + 0x1c], 0xffffffdf
0074ED89  0F 10 46 08                     movups xmm0, xmmword ptr [rsi + 8]
0074ED8D  F6 46 1C 01                     test byte ptr [rsi + 0x1c], 1
0074ED91  49 8B D7                        mov rdx, r15
0074ED94  48 0F 45 15 CC 08 7C 00         cmovne rdx, qword ptr [rip + 0x7c08cc]
0074ED9C  F3 0F 7F 45 C0                  movdqu xmmword ptr [rbp - 0x40], xmm0
0074EDA1  E9 BB FE FF FF                  jmp 0x14074ec61
0074EDA6  49 8B F4                        mov rsi, r12
0074EDA9  48 8D 4B D0                     lea rcx, [rbx - 0x30]
0074EDAD  BF 01 00 00 00                  mov edi, 1
0074EDB2  0F B6 41 1A                     movzx eax, byte ptr [rcx + 0x1a]
0074EDB6  48 8D 15 43 12 8B FF            lea rdx, [rip - 0x74edbd]
0074EDBD  83 E0 03                        and eax, 3
0074EDC0  0F B6 84 10 80 FF F0 00         movzx eax, byte ptr [rax + rdx + 0xf0ff80]
0074EDC8  48 2B C8                        sub rcx, rax
0074EDCB  48 8B 01                        mov rax, qword ptr [rcx]
0074EDCE  48 8B 90 30 01 00 00            mov rdx, qword ptr [rax + 0x130]
0074EDD5  48 89 55 48                     mov qword ptr [rbp + 0x48], rdx
0074EDD9  48 85 F6                        test rsi, rsi
0074EDDC  74 7E                           je 0x14074ee5c
0074EDDE  48 8B 05 FB 80 87 00            mov rax, qword ptr [rip + 0x8780fb]
0074EDE5  48 8D 4E D0                     lea rcx, [rsi - 0x30]
0074EDE9  48 C1 E9 08                     shr rcx, 8
0074EDED  32 4E E8                        xor cl, byte ptr [rsi - 0x18]
0074EDF0  32 0D 56 80 87 00               xor cl, byte ptr [rip + 0x878056]
0074EDF6  3A 48 28                        cmp cl, byte ptr [rax + 0x28]
0074EDF9  75 5E                           jne 0x14074ee59
0074EDFB  8B 46 48                        mov eax, dword ptr [rsi + 0x48]
0074EDFE  83 F8 10                        cmp eax, 0x10
0074EE01  77 2C                           ja 0x14074ee2f
0074EE03  74 4D                           je 0x14074ee52
0074EE05  83 E8 02                        sub eax, 2
0074EE08  74 1E                           je 0x14074ee28
0074EE0A  2B C7                           sub eax, edi
0074EE0C  74 1A                           je 0x14074ee28
0074EE0E  83 E8 04                        sub eax, 4
0074EE11  74 08                           je 0x14074ee1b
0074EE13  2B C7                           sub eax, edi
0074EE15  74 04                           je 0x14074ee1b
0074EE17  3B C7                           cmp eax, edi
0074EE19  75 2B                           jne 0x14074ee46
0074EE1B  8B 7E 34                        mov edi, dword ptr [rsi + 0x34]
0074EE1E  F7 D7                           not edi
0074EE20  83 E7 01                        and edi, 1
0074EE23  83 C7 02                        add edi, 2
0074EE26  EB 34                           jmp 0x14074ee5c
0074EE28  BF 05 00 00 00                  mov edi, 5
0074EE2D  EB 2D                           jmp 0x14074ee5c
0074EE2F  83 E8 12                        sub eax, 0x12
0074EE32  74 1E                           je 0x14074ee52
0074EE34  2B C7                           sub eax, edi
0074EE36  74 1A                           je 0x14074ee52
0074EE38  2B C7                           sub eax, edi
0074EE3A  74 16                           je 0x14074ee52
0074EE3C  83 E8 10                        sub eax, 0x10
0074EE3F  74 0A                           je 0x14074ee4b
0074EE41  83 F8 04                        cmp eax, 4
0074EE44  74 0C                           je 0x14074ee52
0074EE46  41 8B FC                        mov edi, r12d
0074EE49  EB 11                           jmp 0x14074ee5c
0074EE4B  BF 06 00 00 00                  mov edi, 6
0074EE50  EB 0A                           jmp 0x14074ee5c
0074EE52  BF 04 00 00 00                  mov edi, 4
0074EE57  EB 03                           jmp 0x14074ee5c
0074EE59  49 8B F4                        mov rsi, r12
0074EE5C  44 8B 63 18                     mov r12d, dword ptr [rbx + 0x18]
0074EE60  41 FF CC                        dec r12d
0074EE63  48 85 F6                        test rsi, rsi
0074EE66  74 07                           je 0x14074ee6f
0074EE68  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
0074EE6B  A8 20                           test al, 0x20
0074EE6D  75 03                           jne 0x14074ee72
0074EE6F  48 8B F3                        mov rsi, rbx
0074EE72  48 8B CE                        mov rcx, rsi
0074EE75  E8 A6 0B AC FF                  call 0x14020fa20
0074EE7A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0074EE83  4D 8D 75 78                     lea r14, [r13 + 0x78]
0074EE87  48 83 CB FF                     or rbx, 0xffffffffffffffff
0074EE8B  45 33 C0                        xor r8d, r8d
0074EE8E  33 D2                           xor edx, edx
0074EE90  49 8B CE                        mov rcx, r14
0074EE93  66 01 98 E6 01 00 00            add word ptr [rax + 0x1e6], bx
0074EE9A  90                              nop
0074EE9B  E8 90 13 AC FF                  call 0x140210230
0074EEA0  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0074EEA6  4C 8B F8                        mov r15, rax
0074EEA9  73 0E                           jae 0x14074eeb9
0074EEAB  4D 8B C6                        mov r8, r14
0074EEAE  48 8B D0                        mov rdx, rax
0074EEB1  49 8B CE                        mov rcx, r14
0074EEB4  E8 D7 0D AC FF                  call 0x14020fc90
0074EEB9  4D 85 FF                        test r15, r15
0074EEBC  74 05                           je 0x14074eec3
0074EEBE  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0074EEC3  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0074EEC7  41 8B CC                        mov ecx, r12d
0074EECA  45 8B FC                        mov r15d, r12d
0074EECD  48 8B D6                        mov rdx, rsi
0074EED0  41 88 BC 04 04 01 00 00         mov byte ptr [r12 + rax + 0x104], dil
0074EED8  41 BC 01 00 00 00               mov r12d, 1
0074EEDE  41 D3 E4                        shl r12d, cl
0074EEE1  48 8D 48 20                     lea rcx, [rax + 0x20]
0074EEE5  44 09 A0 00 01 00 00            or dword ptr [rax + 0x100], r12d
0074EEEC  4A 8D 0C F9                     lea rcx, [rcx + r15*8]
0074EEF0  E8 A7 92 D0 FF                  call 0x14045819c
0074EEF5  49 8B 4D 00                     mov rcx, qword ptr [r13]
0074EEF9  48 8B F8                        mov rdi, rax
0074EEFC  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0074EF00  48 39 4D 48                     cmp qword ptr [rbp + 0x48], rcx
0074EF04  75 06                           jne 0x14074ef0c
0074EF06  45 09 65 08                     or dword ptr [r13 + 8], r12d
0074EF0A  EB 05                           jmp 0x14074ef11
0074EF0C  43 FF 44 BD 0C                  inc dword ptr [r13 + r15*4 + 0xc]
0074EF11  F0 49 0F C1 1E                  lock xadd qword ptr [r14], rbx
0074EF16  80 E3 06                        and bl, 6
0074EF19  80 FB 02                        cmp bl, 2
0074EF1C  75 08                           jne 0x14074ef26
0074EF1E  49 8B CE                        mov rcx, r14
0074EF21  E8 AA 6E B1 FF                  call 0x140265dd0
0074EF26  49 8B CE                        mov rcx, r14
0074EF29  E8 D2 26 B9 FF                  call 0x1402e1600
0074EF2E  E8 0D 3D B9 FF                  call 0x1402e2c40
0074EF33  48 85 FF                        test rdi, rdi
0074EF36  74 08                           je 0x14074ef40
0074EF38  48 8B CF                        mov rcx, rdi
0074EF3B  E8 00 DF CA FF                  call 0x1403fce40
0074EF40  4C 8B 7D 50                     mov r15, qword ptr [rbp + 0x50]
0074EF44  4C 8B 75 40                     mov r14, qword ptr [rbp + 0x40]
0074EF48  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0074EF4C  E8 DF 4D B1 FF                  call 0x140263d30
0074EF51  E8 BE E9 E7 FF                  call 0x1405cd914
0074EF56  85 C0                           test eax, eax
0074EF58  74 0D                           je 0x14074ef67
0074EF5A  4D 85 F6                        test r14, r14
0074EF5D  74 08                           je 0x14074ef67
0074EF5F  49 8B CE                        mov rcx, r14
0074EF62  E8 E9 A3 BA FF                  call 0x1402f9350
0074EF67  49 8B CF                        mov rcx, r15
0074EF6A  E8 E1 A3 BA FF                  call 0x1402f9350
0074EF6F  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
0074EF77  48 83 C4 60                     add rsp, 0x60
0074EF7B  41 5F                           pop r15
0074EF7D  41 5E                           pop r14
0074EF7F  41 5D                           pop r13
0074EF81  41 5C                           pop r12
0074EF83  5F                              pop rdi
0074EF84  5E                              pop rsi
0074EF85  5D                              pop rbp
0074EF86  C3                              ret
0074EF87  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpCreateSymbolicLinkName(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (96);
    v_r12 = 0;
    v_stack_p8 = 0;
    v_stack_m68 = v_xmm0;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 - 48 + 26))) & (2)) == 0) goto loc_0074EF6F;
    result = (unsigned int)((*(unsigned __int8 *)(a1 - 48 + 26)) & (3));
    a2 = (a1 - 48) - (*(unsigned __int8 *)(result + v_rip - 7662538 * 1 + 15794048));
    if (condition_is_equal) goto loc_0074EF6F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 304)) == 0) goto loc_0074EF6F;
    if ((*(unsigned __int16 *)(a2 + 8)) != ((unsigned __int16)(64 - 60))) goto loc_0074EF6F;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 16) + 2)) != 58) goto loc_0074EF6F;
    result = RtlUpcaseUnicodeChar(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 16)), a2, a3, a4);
    if (((unsigned __int16)(result - 65)) > 25) goto loc_0074EF6F;
    result = (unsigned int)(((unsigned __int16)(result)) - (64));
    *(unsigned int *)(a1 + 24) = (unsigned int)(result);
    result = 0;
    v_stack_m48 = 0;
    v_stack_m58 = v_xmm0;
    result = PsGetCurrentSilo(result - 65, a2, a3, a4);
    result = OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO(result, a2, a3, a4);
    v_stack_p18 = result;
    result = ObfReferenceObject(result, a2, a3, a4);
    v_stack_m78 = v_xmm0;
    result = PsGetCurrentServerSiloGlobals(result, result, a3, a4);
loc_0074EC61:
    a1 = (*(unsigned __int64 *)(result)) & (-16);
    if (*(unsigned __int64 *)(a1) == 0) goto loc_0074ECAA;
    if (((unsigned __int16)(v_stack_m78)) < 8) goto loc_0074ECAA;
    if ((*(unsigned __int64 *)(v_stack_m70)) == v_r10) {
        a3 = (v_stack_m70) + (8);
        result = 0xFFF8ULL;
        a1 = (unsigned __int16)((v_stack_m78) + ((unsigned __int16)(result)));
        v_stack_m70 = a3;
        v_stack_m78 = (unsigned __int16)(a1);
        a2 = *(unsigned __int64 *)(a1);
    }
    result = ObpLockDirectoryShared(v_stack_m58, a2, a3, *(unsigned __int64 *)(a1));
loc_0074ECB3:
    result = ObpParseComponentName(v_stack_m78, v_stack_m68, a3, *(unsigned __int64 *)(a1));
    if ((unsigned __int8)(result) == 0) goto loc_0074EF48;
    a2 = 0;
    result = ObpLookupDirectoryEntry(v_stack_m68, a2, v_stack_m58, *(unsigned __int64 *)(a1));
    if (result == 0) goto loc_0074EDA9;
    a1 = (result - 48) >> (8);
    a3 = ((unsigned __int8)(a1)) ^ (*(unsigned __int8 *)(result - 24));
    a3 = (a3) ^ (*(unsigned __int8 *)(v_rip + 8880456));
    if ((*(unsigned __int64 *)(v_rip - 7662842 + a3 * 8 + 16545792)) != (*(unsigned __int64 *)(v_rip + 8128826))) goto loc_0074ED29;
    a3 = 0;
    result = ObpLockChildDirectory(v_stack_m58, result, a3, *(unsigned __int64 *)(a1));
    goto loc_0074ECB3;
loc_0074ED29:
    if (result != (*(unsigned __int64 *)(v_rip + 8128808))) goto loc_0074EDA9;
    if ((*(unsigned int *)(result + 24)) != 0) goto loc_0074EDA9;
    if (64 == 0) goto loc_0074EDA6;
    v_rdi = (unsigned int)((64) - 1);
    result = Feature_2735186232__private_IsEnabledDeviceUsageNoInline(v_stack_m58, result, a3, *(unsigned __int64 *)(a1));
    if ((unsigned int)(result) != 0) goto loc_0074ED52;
    result = ObpUnlockDirectory(v_stack_m58, result, a3, *(unsigned __int64 *)(a1));
    goto loc_0074ED77;
loc_0074ED52:
    result = ObfReferenceObject(result, result, a3, *(unsigned __int64 *)(a1));
    result = ObpUnlockDirectory(v_stack_m58, result, a3, *(unsigned __int64 *)(a1));
    if (0 != 0) {
        a1 = 0;
        result = ObfDereferenceObject(a1, result, a3, *(unsigned __int64 *)(a1));
    }
    v_stack_p8 = result;
loc_0074ED77:
    if (v_stack_m78 != 0) goto loc_0074ED85;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28)))) & (14)) != 0) {
    }
    a2 = result;
    if (((*(unsigned __int8 *)(result + 28)) & (1)) != 0) { a2 = *(unsigned __int64 *)(v_rip + 8128716); }
    v_stack_m78 = v_xmm0;
    goto loc_0074EC61;
loc_0074EDA6:
loc_0074EDA9:
    result = (unsigned int)((*(unsigned __int8 *)(a1 - 48 + 26)) & (3));
    a1 = (a1 - 48) - (*(unsigned __int8 *)(result + v_rip - 7663037 * 1 + 15794048));
    v_stack_p10 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 304);
    if (0 == 0) goto loc_0074EE5C;
    a1 = (0 - 48) >> (8);
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(0 - 24)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_rip + 8880214)));
    if (((unsigned __int8)(a1)) != (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 8880379) + 40))) goto loc_0074EE59;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 72)))) > 16) goto loc_0074EE2F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 72)))) == 16) goto loc_0074EE52;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 72))) - (2));
    if (condition_is_equal) goto loc_0074EE28;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_0074EE28;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_0074EE1B;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_0074EE1B;
    if (((unsigned int)(result)) != 1) goto loc_0074EE46;
loc_0074EE1B:
    v_rdi = (unsigned int)(~((unsigned int)(*(unsigned int *)(0 + 52))));
    v_rdi = (unsigned int)((v_rdi) & (1));
    v_rdi = (unsigned int)((v_rdi) + (2));
    goto loc_0074EE5C;
loc_0074EE28:
    goto loc_0074EE5C;
loc_0074EE2F:
    result = (unsigned int)((result) - (18));
    if (condition_is_equal) goto loc_0074EE52;
    result = (unsigned int)((result) - (5));
    if (condition_is_equal) goto loc_0074EE52;
    result = (unsigned int)((result) - (5));
    if (condition_is_equal) goto loc_0074EE52;
    result = (unsigned int)((result) - (16));
    if (condition_is_equal) goto loc_0074EE4B;
    if (((unsigned int)(result)) == 4) goto loc_0074EE52;
loc_0074EE46:
    goto loc_0074EE5C;
loc_0074EE4B:
    goto loc_0074EE5C;
loc_0074EE52:
    goto loc_0074EE5C;
loc_0074EE59:
loc_0074EE5C:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) - 1);
    if (0 == 0) goto loc_0074EE6F;
    v_rsi = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 28)))) & (32)) == 0) {
        v_rsi = a1;
    }
    result = ObfReferenceObject(v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 304), a3, *(unsigned __int64 *)(a1));
    v_rbx = (a1) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 120, a2, a3, *(unsigned __int64 *)(a1));
    if (!(condition_is_above_or_equal)) {
        a3 = result + 120;
        a2 = result;
        a1 = result + 120;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(a1));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int8 *)(v_r12 + v_stack_p10 * 1 + 260) = 4;
    v_r12 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r12)))));
    result = ObFastReplaceObject(v_stack_p10 + 32 + (unsigned int)((unsigned int)(v_r12)) * 8, v_rsi, a3, *(unsigned __int64 *)(a1));
    a1 = (*(unsigned __int64 *)(result)) & (-16);
    if (v_stack_p10 != a1) goto loc_0074EF0C;
    goto loc_0074EF11;
loc_0074EF0C:
loc_0074EF11:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = result + 120;
        result = ExfTryToWakePushLock(a1, v_rsi, a3, *(unsigned __int64 *)(a1));
    }
    result = KeAbPostRelease(result + 120, v_rsi, a3, *(unsigned __int64 *)(a1));
    result = KeLeaveGuardedRegion(result + 120, v_rsi, a3, *(unsigned __int64 *)(a1));
    if (result != 0) {
        a1 = result;
        result = ObDereferenceObjectDeferDelete(a1, v_rsi, a3, *(unsigned __int64 *)(a1));
    }
loc_0074EF48:
    result = ObpReleaseLookupContext(v_stack_m58, v_rsi, a3, *(unsigned __int64 *)(a1));
    result = Feature_2735186232__private_IsEnabledDeviceUsageNoInline(v_stack_m58, v_rsi, a3, *(unsigned __int64 *)(a1));
    if ((unsigned int)(result) == 0) goto loc_0074EF67;
    if (v_stack_p8 != 0) {
        a1 = v_stack_p8;
        result = ObfDereferenceObject(a1, v_rsi, a3, *(unsigned __int64 *)(a1));
    }
    result = ObfDereferenceObject(v_stack_p18, v_rsi, a3, *(unsigned __int64 *)(a1));
loc_0074EF6F:
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObpCreateSymbolicLinkName(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (96);
    local_r12 = 0;
    v_stack_p8 = 0;
    v_stack_m68 = v_xmm0;
    if ((((uint8_t)(*(uint8_t *)(arg1 - 0x30 + 0x1A))) & (2)) == 0) goto loc_0074EF6F;
    result = (uint32_t)((*(uint8_t *)(arg1 - 0x30 + 0x1A)) & (3));
    a2 = (Arg1 - 48) - (*(uint8_t *)(result + v_rip - 0x74EBCA * 1 + 0xF0FF80));
    if (condition_is_equal) goto loc_0074EF6F;
    if ((*(uint64_t *)(*(uint64_t *)(a2) + 0x130)) == 0) goto loc_0074EF6F;
    if ((*(uint16_t *)(a2 + 0x8)) != ((uint16_t)(64 - 60))) goto loc_0074EF6F;
    if ((*(uint16_t *)(*(uint64_t *)(a2 + 0x10) + 0x2)) != 58) goto loc_0074EF6F;
    result = RtlUpcaseUnicodeChar(*(uint16_t *)(*(uint64_t *)(a2 + 0x10)), a2, a3, a4);
    if (((uint16_t)(result - 65)) > 25) goto loc_0074EF6F;
    result = (uint32_t)(((uint16_t)(result)) - (64));
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)(result);
    result = 0;
    v_stack_m48 = 0;
    v_stack_m58 = v_xmm0;
    result = PsGetCurrentSilo(result - 65, a2, a3, a4);
    result = OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO(result, a2, a3, a4);
    v_stack_p18 = result;
    result = ObfReferenceObject(result, a2, a3, a4);
    v_stack_m78 = v_xmm0;
    result = PsGetCurrentServerSiloGlobals(result, result, a3, a4);
loc_0074EC61:
    Arg1 = (*(uint64_t *)(result)) & (-16);
    if (*(uint64_t *)(arg1) == 0) goto loc_0074ECAA;
    if (((uint16_t)(v_stack_m78)) < 8) goto loc_0074ECAA;
    if ((*(uint64_t *)(v_stack_m70)) == local_r10) {
        a3 = (v_stack_m70) + (8);
        result = 0xFFF8ULL;
        Arg1 = (uint16_t)((v_stack_m78) + ((uint16_t)(result)));
        v_stack_m70 = a3;
        v_stack_m78 = (uint16_t)(Arg1);
        a2 = *(uint64_t *)(arg1);
    }
    result = ObpLockDirectoryShared(v_stack_m58, a2, a3, *(uint64_t *)(arg1));
loc_0074ECB3:
    result = ObpParseComponentName(v_stack_m78, v_stack_m68, a3, *(uint64_t *)(arg1));
    if ((uint8_t)(result) == 0) goto loc_0074EF48;
    a2 = 0;
    result = ObpLookupDirectoryEntry(v_stack_m68, a2, v_stack_m58, *(uint64_t *)(arg1));
    if (result == 0) goto loc_0074EDA9;
    Arg1 = (result - 48) >> (8);
    a3 = ((uint8_t)(Arg1)) ^ (*(uint8_t *)(result - 0x18));
    a3 = (a3) ^ (*(uint8_t *)(v_rip + 0x878148));
    if ((*(uint64_t *)(v_rip - 0x74ECFA + a3 * 8 + 0xFC7800)) != (*(uint64_t *)(v_rip + 0x7C093A))) goto loc_0074ED29;
    a3 = 0;
    result = ObpLockChildDirectory(v_stack_m58, result, a3, *(uint64_t *)(arg1));
    goto loc_0074ECB3;
loc_0074ED29:
    if (result != (*(uint64_t *)(v_rip + 0x7C0928))) goto loc_0074EDA9;
    if ((*(uint32_t *)(result + 0x18)) != 0) goto loc_0074EDA9;
    if (64 == 0) goto loc_0074EDA6;
    local_rdi = (uint32_t)((64) - 1);
    result = Feature_2735186232__private_IsEnabledDeviceUsageNoInline(v_stack_m58, result, a3, *(uint64_t *)(arg1));
    if ((uint32_t)(result) != 0) goto loc_0074ED52;
    result = ObpUnlockDirectory(v_stack_m58, result, a3, *(uint64_t *)(arg1));
    goto loc_0074ED77;
loc_0074ED52:
    result = ObfReferenceObject(result, result, a3, *(uint64_t *)(arg1));
    result = ObpUnlockDirectory(v_stack_m58, result, a3, *(uint64_t *)(arg1));
    if (0 != 0) {
        Arg1 = 0;
        result = ObfDereferenceObject(Arg1, result, a3, *(uint64_t *)(arg1));
    }
    v_stack_p8 = result;
loc_0074ED77:
    if (v_stack_m78 != 0) goto loc_0074ED85;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) & (14)) != 0) {
    }
    a2 = result;
    if (((*(uint8_t *)(result + 0x1C)) & (1)) != 0) { a2 = *(uint64_t *)(v_rip + 0x7C08CC); }
    v_stack_m78 = v_xmm0;
    goto loc_0074EC61;
loc_0074EDA6:
loc_0074EDA9:
    result = (uint32_t)((*(uint8_t *)(arg1 - 0x30 + 0x1A)) & (3));
    Arg1 = (Arg1 - 48) - (*(uint8_t *)(result + v_rip - 0x74EDBD * 1 + 0xF0FF80));
    v_stack_p10 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x130);
    if (0 == 0) goto loc_0074EE5C;
    Arg1 = (0 - 48) >> (8);
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(0 - 0x18)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(v_rip + 0x878056)));
    if (((uint8_t)(Arg1)) != (*(uint8_t *)(*(uint64_t *)(v_rip + 0x8780FB) + 0x28))) goto loc_0074EE59;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x48)))) > 16) goto loc_0074EE2F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x48)))) == 16) goto loc_0074EE52;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x48))) - (2));
    if (condition_is_equal) goto loc_0074EE28;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_0074EE28;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_0074EE1B;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_0074EE1B;
    if (((uint32_t)(result)) != 1) goto loc_0074EE46;
loc_0074EE1B:
    local_rdi = (uint32_t)(~((uint32_t)(*(uint32_t *)(0 + 0x34))));
    local_rdi = (uint32_t)((local_rdi) & (1));
    local_rdi = (uint32_t)((local_rdi) + (2));
    goto loc_0074EE5C;
loc_0074EE28:
    goto loc_0074EE5C;
loc_0074EE2F:
    result = (uint32_t)((result) - (18));
    if (condition_is_equal) goto loc_0074EE52;
    result = (uint32_t)((result) - (5));
    if (condition_is_equal) goto loc_0074EE52;
    result = (uint32_t)((result) - (5));
    if (condition_is_equal) goto loc_0074EE52;
    result = (uint32_t)((result) - (16));
    if (condition_is_equal) goto loc_0074EE4B;
    if (((uint32_t)(result)) == 4) goto loc_0074EE52;
loc_0074EE46:
    goto loc_0074EE5C;
loc_0074EE4B:
    goto loc_0074EE5C;
loc_0074EE52:
    goto loc_0074EE5C;
loc_0074EE59:
loc_0074EE5C:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) - 1);
    if (0 == 0) goto loc_0074EE6F;
    local_rsi = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) & (32)) == 0) {
        local_rsi = Arg1;
    }
    result = ObfReferenceObject(local_rsi, *(uint64_t *)(*(uint64_t *)(arg1) + 0x130), a3, *(uint64_t *)(arg1));
    local_rbx = (Arg1) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 120, a2, a3, *(uint64_t *)(arg1));
    if (!(condition_is_above_or_equal)) {
        a3 = result + 120;
        a2 = result;
        Arg1 = result + 120;
        result = ExfAcquirePushLockExclusiveEx(Arg1, a2, a3, *(uint64_t *)(arg1));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint8_t *)(local_r12 + v_stack_p10 * 1 + 0x104) = 4;
    local_r12 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_r12)))));
    result = ObFastReplaceObject(v_stack_p10 + 32 + (uint32_t)((uint32_t)(local_r12)) * 8, local_rsi, a3, *(uint64_t *)(arg1));
    Arg1 = (*(uint64_t *)(result)) & (-16);
    if (v_stack_p10 != Arg1) goto loc_0074EF0C;
    goto loc_0074EF11;
loc_0074EF0C:
loc_0074EF11:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = result + 120;
        result = ExfTryToWakePushLock(Arg1, local_rsi, a3, *(uint64_t *)(arg1));
    }
    result = KeAbPostRelease(result + 120, local_rsi, a3, *(uint64_t *)(arg1));
    result = KeLeaveGuardedRegion(result + 120, local_rsi, a3, *(uint64_t *)(arg1));
    if (result != 0) {
        Arg1 = result;
        result = ObDereferenceObjectDeferDelete(Arg1, local_rsi, a3, *(uint64_t *)(arg1));
    }
loc_0074EF48:
    result = ObpReleaseLookupContext(v_stack_m58, local_rsi, a3, *(uint64_t *)(arg1));
    result = Feature_2735186232__private_IsEnabledDeviceUsageNoInline(v_stack_m58, local_rsi, a3, *(uint64_t *)(arg1));
    if ((uint32_t)(result) == 0) goto loc_0074EF67;
    if (v_stack_p8 != 0) {
        Arg1 = v_stack_p8;
        result = ObfDereferenceObject(Arg1, local_rsi, a3, *(uint64_t *)(arg1));
    }
    result = ObfDereferenceObject(v_stack_p18, local_rsi, a3, *(uint64_t *)(arg1));
loc_0074EF6F:
    local_rsp = (local_rsp) + (96);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `16` | `R` |
| `Arg1` | `+ 0x8` | `128` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x1A` | `8` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0074EB80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
