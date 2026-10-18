# WheaReportHwError

- RVA: `0x004ED200`–`0x004ED6C5` (길이 `1,221` bytes)
- VA: `0x00000001404ED200`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D5E44`
- 디코드: `325`개 명령, `1,221/1,221` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x004ED2DA` → [WheapGetErrorSource](../49/WheapGetErrorSource_function_0049554C.md) (function, `0x0049554C`)
- `0x004ED312` → [WheapApplyThresholdChecks](../49/WheapApplyThresholdChecks_function_00491DE4.md) (function, `0x00491DE4`)
- `0x004ED367` → [WheapAllocErrorRecord](../49/WheapAllocErrorRecord_function_004985C0.md) (function, `0x004985C0`)
- `0x004ED3D0` → [WheapCallErrorSourceCreateRecord](../49/WheapCallErrorSourceCreateRecord_function_00495354.md) (function, `0x00495354`)
- `0x004ED3F4` → [WheapFreeErrorRecord](../48/WheapFreeErrorRecord_function_0048491C.md) (function, `0x0048491C`)
- `0x004ED415` → [Feature_Servicing_WheaLiveDumpBertSizeFix__private_IsEnabledDeviceUsageNoInline](../65/Feature_Servicing_WheaLiveDumpBertSizeFix__private_IsEnabledDeviceUsageNoInline_function_0065DBDC.md) (function, `0x0065DBDC`)
- `0x004ED426` → [WheapCompressErrorRecord](../48/WheapCompressErrorRecord_function_004849C8.md) (function, `0x004849C8`)
- `0x004ED437` → [WheaIsCriticalState](../48/WheaIsCriticalState_function_004849A0.md) (function, `0x004849A0`)
- `0x004ED451` → [WheapGenerateETWEvents](../48/WheapGenerateETWEvents_function_0048494C.md) (function, `0x0048494C`)
- `0x004ED459` → [WheapFreeErrorRecord](../48/WheapFreeErrorRecord_function_0048491C.md) (function, `0x0048491C`)
- `0x004ED478` → [WheapCompressErrorRecord](../48/WheapCompressErrorRecord_function_004849C8.md) (function, `0x004849C8`)
- `0x004ED488` → `PSHED.dll!PshedWriteErrorRecord` (import, 간접 대상; import `PSHED.dll!PshedWriteErrorRecord`)
- `0x004ED4BA` → `PSHED.dll!PshedFinalizeErrorRecord` (import, 간접 대상; import `PSHED.dll!PshedFinalizeErrorRecord`)
- `0x004ED4CA` → [WheapPersistPageForMemoryError](../65/WheapPersistPageForMemoryError_function_0065E388.md) (function, `0x0065E388`)
- `0x004ED4D7` → [WheapCompressErrorRecord](../48/WheapCompressErrorRecord_function_004849C8.md) (function, `0x004849C8`)
- `0x004ED4E4` → `PSHED.dll!PshedWriteErrorRecord` (import, 간접 대상; import `PSHED.dll!PshedWriteErrorRecord`)
- `0x004ED4F6` → [WheapAddToDumpFile](../65/WheapAddToDumpFile_function_0065E1FC.md) (function, `0x0065E1FC`)
- `0x004ED50B` → `PSHED.dll!PshedBugCheckSystem` (import, 간접 대상; import `PSHED.dll!PshedBugCheckSystem`)
- `0x004ED52F` → `PSHED.dll!PshedFinalizeErrorRecord` (import, 간접 대상; import `PSHED.dll!PshedFinalizeErrorRecord`)
- `0x004ED53E` → [WheapAttemptErrorRecovery](../65/WheapAttemptErrorRecovery_function_0065E2E0.md) (function, `0x0065E2E0`)
- `0x004ED558` → [WheaRecoveryBugCheck](../65/WheaRecoveryBugCheck_function_0065E110.md) (function, `0x0065E110`)
- `0x004ED574` → [WheaIsCriticalState](../48/WheaIsCriticalState_function_004849A0.md) (function, `0x004849A0`)
- `0x004ED58C` → [WheapFreeErrorRecord](../48/WheapFreeErrorRecord_function_0048491C.md) (function, `0x0048491C`)
- `0x004ED59F` → `PSHED.dll!PshedFinalizeErrorRecord` (import, 간접 대상; import `PSHED.dll!PshedFinalizeErrorRecord`)
- `0x004ED5B2` → [WheapWorkQueueAddItem](../38/WheapWorkQueueAddItem_function_0038662C.md) (function, `0x0038662C`)
- `0x004ED5FD` → [WheaLogInternalEvent](../66/WheaLogInternalEvent_function_006605B0.md) (function, `0x006605B0`)
- `0x004ED60B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x004ED648` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED665` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED682` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED6A5` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED6BF` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [HalpMcaReportError](../54/HalpMcaReportError_function_00541D04.md) at `0x00541DB1`
- [HalHandleNMI](../54/HalHandleNMI_function_00545800.md) at `0x00545946`
- [WheaHwErrorReportSubmitDeviceDriver](../65/WheaHwErrorReportSubmitDeviceDriver_function_0065E7F0.md) at `0x0065E8DE`
- [sub_006FA00E](../6F/Unknown_function_006FA00E.md) at `0x006FA012`

### Static image references
- `0x004ED223` → RVA `0x00E0A740` (`.data`; read)
- `0x004ED444` → RVA `0x00EF9F50` (`.data`; read)
- `0x004ED463` → RVA `0x00E09668` (`.data`; read)
- `0x004ED488` → RVA `0x00151098` (`PSHED.dll!PshedWriteErrorRecord (IAT)`; read)
- `0x004ED4BA` → RVA `0x001510A8` (`PSHED.dll!PshedFinalizeErrorRecord (IAT)`; read)
- `0x004ED50B` → RVA `0x001510A0` (`PSHED.dll!PshedBugCheckSystem (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004ED200  48 8B C4                        mov rax, rsp
004ED203  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
004ED207  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
004ED20B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
004ED20F  55                              push rbp
004ED210  41 54                           push r12
004ED212  41 55                           push r13
004ED214  41 56                           push r14
004ED216  41 57                           push r15
004ED218  48 8D 68 A1                     lea rbp, [rax - 0x5f]
004ED21C  48 81 EC 90 00 00 00            sub rsp, 0x90
004ED223  48 8B 05 16 D5 91 00            mov rax, qword ptr [rip + 0x91d516]
004ED22A  48 33 C4                        xor rax, rsp
004ED22D  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
004ED231  44 8B 59 14                     mov r11d, dword ptr [rcx + 0x14]
004ED235  33 DB                           xor ebx, ebx
004ED237  48 8B F9                        mov rdi, rcx
004ED23A  89 5D DB                        mov dword ptr [rbp - 0x25], ebx
004ED23D  B9 00 00 00 C0                  mov ecx, 0xc0000000
004ED242  88 5D D7                        mov byte ptr [rbp - 0x29], bl
004ED245  41 8B C3                        mov eax, r11d
004ED248  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
004ED24C  23 C1                           and eax, ecx
004ED24E  44 8A E3                        mov r12b, bl
004ED251  3B C1                           cmp eax, ecx
004ED253  75 0A                           jne 0x1404ed25f
004ED255  B8 0D 00 00 C0                  mov eax, 0xc000000d
004ED25A  E9 A5 03 00 00                  jmp 0x1404ed604
004ED25F  BE 01 00 00 00                  mov esi, 1
004ED264  41 0F BA E3 1E                  bt r11d, 0x1e
004ED269  73 1D                           jae 0x1404ed288
004ED26B  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
004ED26E  41 0F BA F3 1E                  btr r11d, 0x1e
004ED273  48 83 C1 07                     add rcx, 7
004ED277  40 88 75 D7                     mov byte ptr [rbp - 0x29], sil
004ED27B  48 03 CF                        add rcx, rdi
004ED27E  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
004ED282  48 89 4D DF                     mov qword ptr [rbp - 0x21], rcx
004ED286  EB 0D                           jmp 0x1404ed295
004ED288  45 85 DB                        test r11d, r11d
004ED28B  79 0C                           jns 0x1404ed299
004ED28D  41 0F BA F3 1F                  btr r11d, 0x1f
004ED292  44 8A E6                        mov r12b, sil
004ED295  44 89 5F 14                     mov dword ptr [rdi + 0x14], r11d
004ED299  41 83 FB 03                     cmp r11d, 3
004ED29D  75 09                           jne 0x1404ed2a8
004ED29F  45 84 E4                        test r12b, r12b
004ED2A2  0F 84 5A 03 00 00               je 0x1404ed602
004ED2A8  65 48 8B 04 25 18 00 00 00      mov rax, qword ptr gs:[0x18]
004ED2B1  4C 8B A8 20 8D 00 00            mov r13, qword ptr [rax + 0x8d20]
004ED2B8  4D 85 ED                        test r13, r13
004ED2BB  0F 84 FA 02 00 00               je 0x1404ed5bb
004ED2C1  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
004ED2C5  48 85 C9                        test rcx, rcx
004ED2C8  0F 84 ED 02 00 00               je 0x1404ed5bb
004ED2CE  39 59 04                        cmp dword ptr [rcx + 4], ebx
004ED2D1  0F 84 E4 02 00 00               je 0x1404ed5bb
004ED2D7  8B 57 18                        mov edx, dword ptr [rdi + 0x18]
004ED2DA  E8 6D 82 FA FF                  call 0x14049554c
004ED2DF  4C 8B F8                        mov r15, rax
004ED2E2  48 85 C0                        test rax, rax
004ED2E5  75 1E                           jne 0x1404ed305
004ED2E7  44 3B DE                        cmp r11d, esi
004ED2EA  77 0F                           ja 0x1404ed2fb
004ED2EC  40 84 77 0C                     test byte ptr [rdi + 0xc], sil
004ED2F0  75 09                           jne 0x1404ed2fb
004ED2F2  45 84 E4                        test r12b, r12b
004ED2F5  0F 84 37 03 00 00               je 0x1404ed632
004ED2FB  B8 C0 00 00 C0                  mov eax, 0xc00000c0
004ED300  E9 FF 02 00 00                  jmp 0x1404ed604
004ED305  F0 01 70 18                     lock add dword ptr [rax + 0x18], esi
004ED309  83 7F 14 02                     cmp dword ptr [rdi + 0x14], 2
004ED30D  75 51                           jne 0x1404ed360
004ED30F  49 8B CF                        mov rcx, r15
004ED312  E8 CD 4A FA FF                  call 0x140491de4
004ED317  84 C0                           test al, al
004ED319  74 45                           je 0x1404ed360
004ED31B  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
004ED31E  48 8D 4D 07                     lea rcx, [rbp + 7]
004ED322  89 45 27                        mov dword ptr [rbp + 0x27], eax
004ED325  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
004ED328  89 45 2B                        mov dword ptr [rbp + 0x2b], eax
004ED32B  C7 45 07 57 68 4C 67            mov dword ptr [rbp + 7], 0x674c6857
004ED332  89 75 0B                        mov dword ptr [rbp + 0xb], esi
004ED335  C7 45 0F 28 00 00 00            mov dword ptr [rbp + 0xf], 0x28
004ED33C  89 75 13                        mov dword ptr [rbp + 0x13], esi
004ED33F  C7 45 1B 04 00 00 80            mov dword ptr [rbp + 0x1b], 0x80000004
004ED346  C7 45 17 4B 52 4E 4C            mov dword ptr [rbp + 0x17], 0x4c4e524b
004ED34D  C7 45 1F 02 00 00 00            mov dword ptr [rbp + 0x1f], 2
004ED354  C7 45 23 08 00 00 00            mov dword ptr [rbp + 0x23], 8
004ED35B  E9 9D 02 00 00                  jmp 0x1404ed5fd
004ED360  48 8D 55 DB                     lea rdx, [rbp - 0x25]
004ED364  49 8B CF                        mov rcx, r15
004ED367  E8 54 B2 FA FF                  call 0x1404985c0
004ED36C  4C 8B F0                        mov r14, rax
004ED36F  48 85 C0                        test rax, rax
004ED372  75 22                           jne 0x1404ed396
004ED374  41 01 77 10                     add dword ptr [r15 + 0x10], esi
004ED378  39 77 14                        cmp dword ptr [rdi + 0x14], esi
004ED37B  77 0F                           ja 0x1404ed38c
004ED37D  40 84 77 0C                     test byte ptr [rdi + 0xc], sil
004ED381  75 09                           jne 0x1404ed38c
004ED383  45 84 E4                        test r12b, r12b
004ED386  0F 84 C2 02 00 00               je 0x1404ed64e
004ED38C  B8 9A 00 00 C0                  mov eax, 0xc000009a
004ED391  E9 6E 02 00 00                  jmp 0x1404ed604
004ED396  8B 40 18                        mov eax, dword ptr [rax + 0x18]
004ED399  49 8D 76 28                     lea rsi, [r14 + 0x28]
004ED39D  8B 4F 0C                        mov ecx, dword ptr [rdi + 0xc]
004ED3A0  4C 8B CE                        mov r9, rsi
004ED3A3  44 8B 45 DB                     mov r8d, dword ptr [rbp - 0x25]
004ED3A7  48 8B D7                        mov rdx, rdi
004ED3AA  C1 E9 02                        shr ecx, 2
004ED3AD  41 83 C0 D8                     add r8d, -0x28
004ED3B1  33 C8                           xor ecx, eax
004ED3B3  83 E1 04                        and ecx, 4
004ED3B6  33 C8                           xor ecx, eax
004ED3B8  41 89 4E 18                     mov dword ptr [r14 + 0x18], ecx
004ED3BC  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
004ED3BF  C1 E8 02                        shr eax, 2
004ED3C2  33 C1                           xor eax, ecx
004ED3C4  83 E0 08                        and eax, 8
004ED3C7  33 C1                           xor eax, ecx
004ED3C9  49 8B CF                        mov rcx, r15
004ED3CC  41 89 46 18                     mov dword ptr [r14 + 0x18], eax
004ED3D0  E8 7F 7F FA FF                  call 0x140495354
004ED3D5  89 45 DB                        mov dword ptr [rbp - 0x25], eax
004ED3D8  85 C0                           test eax, eax
004ED3DA  79 25                           jns 0x1404ed401
004ED3DC  83 7F 14 01                     cmp dword ptr [rdi + 0x14], 1
004ED3E0  77 0F                           ja 0x1404ed3f1
004ED3E2  F6 47 0C 01                     test byte ptr [rdi + 0xc], 1
004ED3E6  75 09                           jne 0x1404ed3f1
004ED3E8  45 84 E4                        test r12b, r12b
004ED3EB  0F 84 7A 02 00 00               je 0x1404ed66b
004ED3F1  49 8B CE                        mov rcx, r14
004ED3F4  E8 23 75 F9 FF                  call 0x14048491c
004ED3F9  8B 45 DB                        mov eax, dword ptr [rbp - 0x25]
004ED3FC  E9 03 02 00 00                  jmp 0x1404ed604
004ED401  45 84 E4                        test r12b, r12b
004ED404  75 05                           jne 0x1404ed40b
004ED406  38 5D D7                        cmp byte ptr [rbp - 0x29], bl
004ED409  74 04                           je 0x1404ed40f
004ED40B  83 4E 68 08                     or dword ptr [rsi + 0x68], 8
004ED40F  F6 46 68 02                     test byte ptr [rsi + 0x68], 2
004ED413  74 4E                           je 0x1404ed463
004ED415  E8 C2 07 17 00                  call 0x14065dbdc
004ED41A  85 C0                           test eax, eax
004ED41C  74 0D                           je 0x1404ed42b
004ED41E  48 8B D6                        mov rdx, rsi
004ED421  B9 03 00 00 00                  mov ecx, 3
004ED426  E8 9D 75 F9 FF                  call 0x1404849c8
004ED42B  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
004ED42F  A8 01                           test al, 1
004ED431  0F 84 74 01 00 00               je 0x1404ed5ab
004ED437  E8 64 75 F9 FF                  call 0x1404849a0
004ED43C  84 C0                           test al, al
004ED43E  0F 85 67 01 00 00               jne 0x1404ed5ab
004ED444  83 3D 05 CB A0 00 01            cmp dword ptr [rip + 0xa0cb05], 1
004ED44B  75 09                           jne 0x1404ed456
004ED44D  49 8D 4E 28                     lea rcx, [r14 + 0x28]
004ED451  E8 F6 74 F9 FF                  call 0x14048494c
004ED456  49 8B CE                        mov rcx, r14
004ED459  E8 BE 74 F9 FF                  call 0x14048491c
004ED45E  E9 54 01 00 00                  jmp 0x1404ed5b7
004ED463  48 8B 05 FE C1 91 00            mov rax, qword ptr [rip + 0x91c1fe]
004ED46A  38 18                           cmp byte ptr [rax], bl
004ED46C  75 34                           jne 0x1404ed4a2
004ED46E  45 84 E4                        test r12b, r12b
004ED471  75 2F                           jne 0x1404ed4a2
004ED473  48 8B D6                        mov rdx, rsi
004ED476  33 C9                           xor ecx, ecx
004ED478  E8 4B 75 F9 FF                  call 0x1404849c8
004ED47D  8B 56 14                        mov edx, dword ptr [rsi + 0x14]
004ED480  4C 8B C6                        mov r8, rsi
004ED483  B9 01 00 00 00                  mov ecx, 1
004ED488  48 FF 15 09 3C C6 FF            call qword ptr [rip - 0x39c3f7]
004ED48F  0F 1F 44 00 00                  nop dword ptr [rax + rax]
004ED494  85 C0                           test eax, eax
004ED496  79 0A                           jns 0x1404ed4a2
004ED498  48 8B 05 C9 C1 91 00            mov rax, qword ptr [rip + 0x91c1c9]
004ED49F  C6 00 01                        mov byte ptr [rax], 1
004ED4A2  8B 4F 14                        mov ecx, dword ptr [rdi + 0x14]
004ED4A5  83 F9 01                        cmp ecx, 1
004ED4A8  75 72                           jne 0x1404ed51c
004ED4AA  45 84 E4                        test r12b, r12b
004ED4AD  0F 85 E5 00 00 00               jne 0x1404ed598
004ED4B3  49 8D 57 60                     lea rdx, [r15 + 0x60]
004ED4B7  48 8B CE                        mov rcx, rsi
004ED4BA  48 FF 15 E7 3B C6 FF            call qword ptr [rip - 0x39c419]
004ED4C1  0F 1F 44 00 00                  nop dword ptr [rax + rax]
004ED4C6  49 8D 4E 28                     lea rcx, [r14 + 0x28]
004ED4CA  E8 B9 0E 17 00                  call 0x14065e388
004ED4CF  48 8B D6                        mov rdx, rsi
004ED4D2  B9 03 00 00 00                  mov ecx, 3
004ED4D7  E8 EC 74 F9 FF                  call 0x1404849c8
004ED4DC  8B 56 14                        mov edx, dword ptr [rsi + 0x14]
004ED4DF  4C 8B C6                        mov r8, rsi
004ED4E2  33 C9                           xor ecx, ecx
004ED4E4  48 FF 15 AD 3B C6 FF            call qword ptr [rip - 0x39c453]
004ED4EB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
004ED4F0  8B 56 14                        mov edx, dword ptr [rsi + 0x14]
004ED4F3  48 8B CE                        mov rcx, rsi
004ED4F6  E8 01 0D 17 00                  call 0x14065e1fc
004ED4FB  38 5D D7                        cmp byte ptr [rbp - 0x29], bl
004ED4FE  0F 85 84 01 00 00               jne 0x1404ed688
004ED504  48 8B D6                        mov rdx, rsi
004ED507  49 8D 4F 60                     lea rcx, [r15 + 0x60]
004ED50B  48 FF 15 8E 3B C6 FF            call qword ptr [rip - 0x39c472]
004ED512  0F 1F 44 00 00                  nop dword ptr [rax + rax]
004ED517  E9 9B 00 00 00                  jmp 0x1404ed5b7
004ED51C  8D 41 FE                        lea eax, [rcx - 2]
004ED51F  83 F8 01                        cmp eax, 1
004ED522  76 74                           jbe 0x1404ed598
004ED524  85 C9                           test ecx, ecx
004ED526  75 61                           jne 0x1404ed589
004ED528  49 8D 57 60                     lea rdx, [r15 + 0x60]
004ED52C  48 8B CE                        mov rcx, rsi
004ED52F  48 FF 15 72 3B C6 FF            call qword ptr [rip - 0x39c48e]
004ED536  0F 1F 44 00 00                  nop dword ptr [rax + rax]
004ED53B  48 8B CE                        mov rcx, rsi
004ED53E  E8 9D 0D 17 00                  call 0x14065e2e0
004ED543  83 7E 0C 02                     cmp dword ptr [rsi + 0xc], 2
004ED547  74 16                           je 0x1404ed55f
004ED549  45 84 E4                        test r12b, r12b
004ED54C  75 15                           jne 0x1404ed563
004ED54E  4C 8B C7                        mov r8, rdi
004ED551  49 8D 57 60                     lea rdx, [r15 + 0x60]
004ED555  48 8B CE                        mov rcx, rsi
004ED558  E8 B3 0B 17 00                  call 0x14065e110
004ED55D  EB 58                           jmp 0x1404ed5b7
004ED55F  83 4E 68 01                     or dword ptr [rsi + 0x68], 1
004ED563  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
004ED567  A8 01                           test al, 1
004ED569  74 40                           je 0x1404ed5ab
004ED56B  83 3D DE C9 A0 00 01            cmp dword ptr [rip + 0xa0c9de], 1
004ED572  75 37                           jne 0x1404ed5ab
004ED574  E8 27 74 F9 FF                  call 0x1404849a0
004ED579  84 C0                           test al, al
004ED57B  75 2E                           jne 0x1404ed5ab
004ED57D  8A 46 68                        mov al, byte ptr [rsi + 0x68]
004ED580  84 C0                           test al, al
004ED582  78 27                           js 0x1404ed5ab
004ED584  E9 C4 FE FF FF                  jmp 0x1404ed44d
004ED589  49 8B CE                        mov rcx, r14
004ED58C  E8 8B 73 F9 FF                  call 0x14048491c
004ED591  BB 0D 00 00 C0                  mov ebx, 0xc000000d
004ED596  EB 1F                           jmp 0x1404ed5b7
004ED598  49 8D 57 60                     lea rdx, [r15 + 0x60]
004ED59C  48 8B CE                        mov rcx, rsi
004ED59F  48 FF 15 02 3B C6 FF            call qword ptr [rip - 0x39c4fe]
004ED5A6  0F 1F 44 00 00                  nop dword ptr [rax + rax]
004ED5AB  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
004ED5AF  49 8B D6                        mov rdx, r14
004ED5B2  E8 75 90 E9 FF                  call 0x14038662c
004ED5B7  8B C3                           mov eax, ebx
004ED5B9  EB 49                           jmp 0x1404ed604
004ED5BB  44 3B DE                        cmp r11d, esi
004ED5BE  77 0F                           ja 0x1404ed5cf
004ED5C0  40 84 77 0C                     test byte ptr [rdi + 0xc], sil
004ED5C4  75 09                           jne 0x1404ed5cf
004ED5C6  45 84 E4                        test r12b, r12b
004ED5C9  0F 84 DC 00 00 00               je 0x1404ed6ab
004ED5CF  C7 45 E7 57 68 4C 67            mov dword ptr [rbp - 0x19], 0x674c6857
004ED5D6  48 8D 4D E7                     lea rcx, [rbp - 0x19]
004ED5DA  89 75 EB                        mov dword ptr [rbp - 0x15], esi
004ED5DD  C7 45 EF 20 00 00 00            mov dword ptr [rbp - 0x11], 0x20
004ED5E4  89 75 F3                        mov dword ptr [rbp - 0xd], esi
004ED5E7  C7 45 FB 36 00 00 80            mov dword ptr [rbp - 5], 0x80000036
004ED5EE  C7 45 F7 4B 52 4E 4C            mov dword ptr [rbp - 9], 0x4c4e524b
004ED5F5  48 C7 45 FF 02 00 00 00         mov qword ptr [rbp - 1], 2
004ED5FD  E8 AE 2F 17 00                  call 0x1406605b0
004ED602  33 C0                           xor eax, eax
004ED604  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
004ED608  48 33 CC                        xor rcx, rsp
004ED60B  E8 30 F0 1B 00                  call 0x1406ac640
004ED610  4C 8D 9C 24 90 00 00 00         lea r11, [rsp + 0x90]
004ED618  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
004ED61C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
004ED620  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
004ED624  49 8B E3                        mov rsp, r11
004ED627  41 5F                           pop r15
004ED629  41 5E                           pop r14
004ED62B  41 5D                           pop r13
004ED62D  41 5C                           pop r12
004ED62F  5D                              pop rbp
004ED630  C3                              ret
004ED631  CC                              int3
004ED632  4C 63 47 1C                     movsxd r8, dword ptr [rdi + 0x1c]
004ED636  4C 8B CA                        mov r9, rdx
004ED639  BA 09 00 00 00                  mov edx, 9
004ED63E  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004ED643  B9 22 01 00 00                  mov ecx, 0x122
004ED648  E8 13 00 01 00                  call 0x1404fd660
004ED64D  CC                              int3
004ED64E  44 8B 4F 18                     mov r9d, dword ptr [rdi + 0x18]
004ED652  BA 0A 00 00 00                  mov edx, 0xa
004ED657  4C 63 47 1C                     movsxd r8, dword ptr [rdi + 0x1c]
004ED65B  B9 22 01 00 00                  mov ecx, 0x122
004ED660  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004ED665  E8 F6 FF 00 00                  call 0x1404fd660
004ED66A  CC                              int3
004ED66B  44 8B 4F 18                     mov r9d, dword ptr [rdi + 0x18]
004ED66F  BA 0B 00 00 00                  mov edx, 0xb
004ED674  4C 63 47 1C                     movsxd r8, dword ptr [rdi + 0x1c]
004ED678  B9 22 01 00 00                  mov ecx, 0x122
004ED67D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004ED682  E8 D9 FF 00 00                  call 0x1404fd660
004ED687  CC                              int3
004ED688  4C 8B 4D DF                     mov r9, qword ptr [rbp - 0x21]
004ED68C  4C 8B C6                        mov r8, rsi
004ED68F  49 63 57 68                     movsxd rdx, dword ptr [r15 + 0x68]
004ED693  B9 24 01 00 00                  mov ecx, 0x124
004ED698  49 8B 41 50                     mov rax, qword ptr [r9 + 0x50]
004ED69C  4D 8B 49 48                     mov r9, qword ptr [r9 + 0x48]
004ED6A0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004ED6A5  E8 B6 FF 00 00                  call 0x1404fd660
004ED6AA  CC                              int3
004ED6AB  48 63 57 1C                     movsxd rdx, dword ptr [rdi + 0x1c]
004ED6AF  45 33 C9                        xor r9d, r9d
004ED6B2  45 33 C0                        xor r8d, r8d
004ED6B5  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004ED6BA  B9 24 01 00 00                  mov ecx, 0x124
004ED6BF  E8 9C FF 00 00                  call 0x1404fd660
004ED6C4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaReportHwError(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m70;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 9557270)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 47) = result;
    v_rbx = 0;
    *(unsigned int *)(v_rsp - 95 - 37) = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20))))) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_004ED25F;
    goto loc_004ED604;
loc_004ED25F:
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_004ED288;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 8))) + (7);
    *(unsigned __int8 *)(v_rsp - 95 - 41) = 1;
    a1 = (a1) + (a1);
    a1 = (a1) & (-8);
    *(unsigned __int64 *)(v_rsp - 95 - 33) = a1;
    goto loc_004ED295;
loc_004ED288:
    if (!sign_flag) goto loc_004ED299;
loc_004ED295:
    *(unsigned int *)(a1 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)));
loc_004ED299:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)))) != 3) goto loc_004ED2A8;
    if (1 == 0) goto loc_004ED602;
loc_004ED2A8:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 24)) + 36128) == 0) goto loc_004ED5BB;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 24)) + 36128) + 8) == 0) goto loc_004ED5BB;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 24)) + 36128) + 8) + 4)) == 0) goto loc_004ED5BB;
    result = WheapGetErrorSource(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 24)) + 36128) + 8), (unsigned int)(*(unsigned int *)(a1 + 24)), a3, a4);
    if (result != 0) goto loc_004ED305;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)))) > 1) goto loc_004ED2FB;
    if (((*(unsigned __int8 *)(a1 + 12)) & (1)) != 0) goto loc_004ED2FB;
    if (1 == 0) goto loc_004ED632;
loc_004ED2FB:
    goto loc_004ED604;
loc_004ED305:
    if ((*(unsigned int *)(a1 + 20)) != 2) goto loc_004ED360;
    result = WheapApplyThresholdChecks(result, (unsigned int)(*(unsigned int *)(a1 + 24)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004ED360;
    *(unsigned int *)(v_rsp - 95 + 39) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)));
    *(unsigned int *)(v_rsp - 95 + 43) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    *(unsigned int *)(v_rsp - 95 + 7) = 0x674C6857ULL;
    *(unsigned int *)(v_rsp - 95 + 11) = 1;
    *(unsigned int *)(v_rsp - 95 + 15) = 40;
    *(unsigned int *)(v_rsp - 95 + 19) = 1;
    *(unsigned int *)(v_rsp - 95 + 27) = 0x80000004ULL;
    *(unsigned int *)(v_rsp - 95 + 23) = 0x4C4E524BULL;
    *(unsigned int *)(v_rsp - 95 + 31) = 2;
    *(unsigned int *)(v_rsp - 95 + 35) = 8;
    goto loc_004ED5FD;
loc_004ED360:
    result = WheapAllocErrorRecord(result, v_rsp - 95 - 37, a3, a4);
    if (result != 0) goto loc_004ED396;
    if ((*(unsigned int *)(a1 + 20)) > 1) goto loc_004ED38C;
    if (((*(unsigned __int8 *)(a1 + 12)) & (1)) != 0) goto loc_004ED38C;
    if (1 == 0) goto loc_004ED64E;
loc_004ED38C:
    goto loc_004ED604;
loc_004ED396:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 12))) >> (2));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 - 37))) + (-40));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xC000009AULL) + 24)))));
    a1 = (unsigned int)((a1) & (4));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xC000009AULL) + 24)))));
    *(unsigned int *)(result + 24) = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 12))) >> (2));
    result = (unsigned int)((result) ^ ((unsigned int)(a1)));
    result = (unsigned int)((result) & (8));
    result = (unsigned int)((result) ^ ((unsigned int)(a1)));
    *(unsigned int *)(result + 24) = (unsigned int)(result);
    result = WheapCallErrorSourceCreateRecord(result, a1, a3, result + 40);
    *(unsigned int *)(v_rsp - 95 - 37) = (unsigned int)(result);
    if (!sign_flag) goto loc_004ED401;
    if ((*(unsigned int *)(a1 + 20)) > 1) goto loc_004ED3F1;
    if (((*(unsigned __int8 *)(a1 + 12)) & (1)) != 0) goto loc_004ED3F1;
    if (1 == 0) goto loc_004ED66B;
loc_004ED3F1:
    result = WheapFreeErrorRecord(result, a1, a3, result + 40);
    goto loc_004ED604;
loc_004ED401:
    if (1 != 0) goto loc_004ED40B;
    if ((*(unsigned __int8 *)(v_rsp - 95 - 41)) != 0) {
    }
    if (((*(unsigned __int8 *)(result + 40 + 104)) & (2)) == 0) goto loc_004ED463;
    result = Feature_Servicing_WheaLiveDumpBertSizeFix__private_IsEnabledDeviceUsageNoInline(result, a1, a3, result + 40);
    if ((unsigned int)(result) != 0) {
        a2 = result + 40;
        a1 = 3;
        result = WheapCompressErrorRecord(a1, a2, a3, result + 40);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 24)))) & (1)) == 0) goto loc_004ED5AB;
    result = WheaIsCriticalState(a1, a2, a3, result + 40);
    if ((unsigned __int8)(result) != 0) goto loc_004ED5AB;
    if ((*(unsigned int *)(v_rip + 10537733)) == 1) {
        a1 = result + 40;
        result = WheapGenerateETWEvents(a1, a2, a3, result + 40);
    }
    result = WheapFreeErrorRecord(result, a2, a3, result + 40);
    goto loc_004ED5B7;
loc_004ED463:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9552382))) != 0) goto loc_004ED4A2;
    if (1 != 0) goto loc_004ED4A2;
    a1 = 0;
    result = WheapCompressErrorRecord(a1, result + 40, a3, result + 40);
    result = PSHED_dll_PshedWriteErrorRecord(1, (unsigned int)(*(unsigned int *)(result + 40 + 20)), result + 40, result + 40);
    if (sign_flag) {
        result = *(unsigned __int64 *)(v_rip + 9552329);
        *(unsigned __int8 *)(result) = 1;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)))) != 1) goto loc_004ED51C;
    if (1 != 0) goto loc_004ED598;
    result = PSHED_dll_PshedFinalizeErrorRecord(result + 40, result + 96, result + 40, result + 40);
    result = WheapPersistPageForMemoryError(result + 40, result + 96, result + 40, result + 40);
    result = WheapCompressErrorRecord(3, result + 40, result + 40, result + 40);
    a1 = 0;
    result = PSHED_dll_PshedWriteErrorRecord(a1, (unsigned int)(*(unsigned int *)(result + 40 + 20)), result + 40, result + 40);
    result = WheapAddToDumpFile(result + 40, (unsigned int)(*(unsigned int *)(result + 40 + 20)), result + 40, result + 40);
    if ((*(unsigned __int8 *)(v_rsp - 95 - 41)) != 0) goto loc_004ED688;
    result = PSHED_dll_PshedBugCheckSystem(result + 96, result + 40, result + 40, result + 40);
    goto loc_004ED5B7;
loc_004ED51C:
    if (((unsigned int)(result + 96 - 2)) <= 1) goto loc_004ED598;
    if ((unsigned int)(result + 96) != 0) goto loc_004ED589;
    result = PSHED_dll_PshedFinalizeErrorRecord(result + 40, result + 96, result + 40, result + 40);
    result = WheapAttemptErrorRecovery(result + 40, result + 96, result + 40, result + 40);
    if ((*(unsigned int *)(result + 40 + 12)) == 2) goto loc_004ED55F;
    if (1 != 0) goto loc_004ED563;
    result = WheaRecoveryBugCheck(result + 40, result + 96, 0, result + 40);
    goto loc_004ED5B7;
loc_004ED55F:
loc_004ED563:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 24)))) & (1)) == 0) goto loc_004ED5AB;
    if ((*(unsigned int *)(v_rip + 10537438)) != 1) goto loc_004ED5AB;
    result = WheaIsCriticalState(result + 40, result + 96, 0, result + 40);
    if ((unsigned __int8)(result) != 0) goto loc_004ED5AB;
    if (sign_flag) goto loc_004ED5AB;
    goto loc_004ED44D;
loc_004ED589:
    result = WheapFreeErrorRecord(result, result + 96, 0, result + 40);
    goto loc_004ED5B7;
loc_004ED598:
    result = PSHED_dll_PshedFinalizeErrorRecord(result + 40, result + 96, 0, result + 40);
loc_004ED5AB:
    result = WheapWorkQueueAddItem(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 24)) + 36128) + 16), result, 0, result + 40);
loc_004ED5B7:
    goto loc_004ED604;
loc_004ED5BB:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)))) > ((unsigned int)(result + 40))) goto loc_004ED5CF;
    if (((*(unsigned __int8 *)(a1 + 12)) & ((unsigned __int8)(result + 40))) != 0) goto loc_004ED5CF;
    if (1 == 0) goto loc_004ED6AB;
loc_004ED5CF:
    *(unsigned int *)(v_rsp - 95 - 25) = 0x674C6857ULL;
    *(unsigned int *)(v_rsp - 95 - 21) = (unsigned int)(result + 40);
    *(unsigned int *)(v_rsp - 95 - 17) = 32;
    *(unsigned int *)(v_rsp - 95 - 13) = (unsigned int)(result + 40);
    *(unsigned int *)(v_rsp - 95 - 5) = 0x80000036ULL;
    *(unsigned int *)(v_rsp - 95 - 9) = 0x4C4E524BULL;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = 2;
loc_004ED5FD:
    result = WheaLogInternalEvent(v_rsp - 95 - 25, result, 0, result + 40);
loc_004ED602:
    result = 0;
loc_004ED604:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, result, 0, result + 40);
    return result;
loc_004ED632:
    v_stack_m70 = *(unsigned __int64 *)(v_stack_m28 + 56);
    result = KeBugCheckEx(290, 9, (int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 28)), result);
loc_004ED64E:
    v_stack_m70 = *(unsigned __int64 *)(v_stack_m28 + 56);
    result = KeBugCheckEx(290, 10, (int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 28)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 24)));
loc_004ED66B:
    v_stack_m70 = *(unsigned __int64 *)(v_stack_m28 + 56);
    result = KeBugCheckEx(290, 11, (int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 28)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 24)));
loc_004ED688:
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 80);
    result = KeBugCheckEx(292, (int)(*(unsigned int *)(result + 104)), *(unsigned __int64 *)(v_stack_m28 + 64), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 - 33) + 72));
loc_004ED6AB:
    a4 = 0;
    a3 = 0;
    v_stack_m70 = *(unsigned __int64 *)(v_stack_m28 + 56);
    result = KeBugCheckEx(292, (int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 28)), a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WheaReportHwError(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m70;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x91D516)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = result;
    local_rbx = 0;
    *(uint32_t *)(local_rsp - 0x5F - 0x25) = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14))))) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_004ED25F;
    goto loc_004ED604;
loc_004ED25F:
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_004ED288;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x8))) + (7);
    *(uint8_t *)(local_rsp - 0x5F - 0x29) = 1;
    Arg1 = (Arg1) + (Arg1);
    Arg1 = (Arg1) & (-8);
    *(void **)(local_rsp - 0x5F - 0x21) = Arg1;
    goto loc_004ED295;
loc_004ED288:
    if (!sign_flag) goto loc_004ED299;
loc_004ED295:
    *(uint32_t *)(arg1 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)));
loc_004ED299:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)))) != 3) goto loc_004ED2A8;
    if (1 == 0) goto loc_004ED602;
loc_004ED2A8:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x18)) + 0x8D20) == 0) goto loc_004ED5BB;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x18)) + 0x8D20) + 0x8) == 0) goto loc_004ED5BB;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x18)) + 0x8D20) + 0x8) + 0x4)) == 0) goto loc_004ED5BB;
    result = WheapGetErrorSource(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x18)) + 0x8D20) + 0x8), (uint32_t)(*(uint32_t *)(arg1 + 0x18)), a3, a4);
    if (result != 0) goto loc_004ED305;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)))) > 1) goto loc_004ED2FB;
    if (((*(uint8_t *)(arg1 + 0xC)) & (1)) != 0) goto loc_004ED2FB;
    if (1 == 0) goto loc_004ED632;
loc_004ED2FB:
    goto loc_004ED604;
loc_004ED305:
    if ((*(uint32_t *)(arg1 + 0x14)) != 2) goto loc_004ED360;
    result = WheapApplyThresholdChecks(result, (uint32_t)(*(uint32_t *)(arg1 + 0x18)), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_004ED360;
    *(uint32_t *)(local_rsp - 0x5F + 0x27) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    *(uint32_t *)(local_rsp - 0x5F + 0x2B) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    *(uint32_t *)(local_rsp - 0x5F + 0x7) = 0x674C6857ULL;
    *(uint32_t *)(local_rsp - 0x5F + 0xB) = 1;
    *(uint32_t *)(local_rsp - 0x5F + 0xF) = 40;
    *(uint32_t *)(local_rsp - 0x5F + 0x13) = 1;
    *(uint32_t *)(local_rsp - 0x5F + 0x1B) = 0x80000004ULL;
    *(uint32_t *)(local_rsp - 0x5F + 0x17) = 0x4C4E524BULL;
    *(uint32_t *)(local_rsp - 0x5F + 0x1F) = 2;
    *(uint32_t *)(local_rsp - 0x5F + 0x23) = 8;
    goto loc_004ED5FD;
loc_004ED360:
    result = WheapAllocErrorRecord(result, local_rsp - 95 - 37, a3, a4);
    if (result != 0) goto loc_004ED396;
    if ((*(uint32_t *)(arg1 + 0x14)) > 1) goto loc_004ED38C;
    if (((*(uint8_t *)(arg1 + 0xC)) & (1)) != 0) goto loc_004ED38C;
    if (1 == 0) goto loc_004ED64E;
loc_004ED38C:
    goto loc_004ED604;
loc_004ED396:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC))) >> (2));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x25))) + (-40));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xC000009AULL) + 0x18)))));
    Arg1 = (uint32_t)((Arg1) & (4));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xC000009AULL) + 0x18)))));
    *(uint32_t *)(result + 0x18) = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC))) >> (2));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
    result = (uint32_t)((result) & (8));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(result + 0x18) = (uint32_t)(result);
    result = WheapCallErrorSourceCreateRecord(result, Arg1, a3, result + 40);
    *(uint32_t *)(local_rsp - 0x5F - 0x25) = (uint32_t)(result);
    if (!sign_flag) goto loc_004ED401;
    if ((*(uint32_t *)(arg1 + 0x14)) > 1) goto loc_004ED3F1;
    if (((*(uint8_t *)(arg1 + 0xC)) & (1)) != 0) goto loc_004ED3F1;
    if (1 == 0) goto loc_004ED66B;
loc_004ED3F1:
    result = WheapFreeErrorRecord(result, Arg1, a3, result + 40);
    goto loc_004ED604;
loc_004ED401:
    if (1 != 0) goto loc_004ED40B;
    if ((*(uint8_t *)(local_rsp - 0x5F - 0x29)) != 0) {
    }
    if (((*(uint8_t *)(result + 0x28 + 0x68)) & (2)) == 0) goto loc_004ED463;
    result = Feature_Servicing_WheaLiveDumpBertSizeFix__private_IsEnabledDeviceUsageNoInline(result, Arg1, a3, result + 40);
    if ((uint32_t)(result) != 0) {
        a2 = result + 40;
        Arg1 = 3;
        result = WheapCompressErrorRecord(Arg1, a2, a3, result + 40);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x18)))) & (1)) == 0) goto loc_004ED5AB;
    result = WheaIsCriticalState(Arg1, a2, a3, result + 40);
    if ((uint8_t)(result) != 0) goto loc_004ED5AB;
    if ((*(uint32_t *)(v_rip + 0xA0CB05)) == 1) {
        Arg1 = result + 40;
        result = WheapGenerateETWEvents(Arg1, a2, a3, result + 40);
    }
    result = WheapFreeErrorRecord(result, a2, a3, result + 40);
    goto loc_004ED5B7;
loc_004ED463:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x91C1FE))) != 0) goto loc_004ED4A2;
    if (1 != 0) goto loc_004ED4A2;
    Arg1 = 0;
    result = WheapCompressErrorRecord(Arg1, result + 40, a3, result + 40);
    result = kernel_indirect_call(1, (uint32_t)(*(uint32_t *)(result + 0x28 + 0x14)), result + 40, result + 40);
    if (sign_flag) {
        result = *(uint64_t *)(v_rip + 0x91C1C9);
        *(uint8_t *)(result) = 1;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)))) != 1) goto loc_004ED51C;
    if (1 != 0) goto loc_004ED598;
    result = kernel_indirect_call(result + 40, result + 96, result + 40, result + 40);
    result = WheapPersistPageForMemoryError(result + 40, result + 96, result + 40, result + 40);
    result = WheapCompressErrorRecord(3, result + 40, result + 40, result + 40);
    Arg1 = 0;
    result = kernel_indirect_call(Arg1, (uint32_t)(*(uint32_t *)(result + 0x28 + 0x14)), result + 40, result + 40);
    result = WheapAddToDumpFile(result + 40, (uint32_t)(*(uint32_t *)(result + 0x28 + 0x14)), result + 40, result + 40);
    if ((*(uint8_t *)(local_rsp - 0x5F - 0x29)) != 0) goto loc_004ED688;
    result = kernel_indirect_call(result + 96, result + 40, result + 40, result + 40);
    goto loc_004ED5B7;
loc_004ED51C:
    if (((uint32_t)(result + 96 - 2)) <= 1) goto loc_004ED598;
    if ((uint32_t)(result + 96) != 0) goto loc_004ED589;
    result = kernel_indirect_call(result + 40, result + 96, result + 40, result + 40);
    result = WheapAttemptErrorRecovery(result + 40, result + 96, result + 40, result + 40);
    if ((*(uint32_t *)(result + 0x28 + 0xC)) == 2) goto loc_004ED55F;
    if (1 != 0) goto loc_004ED563;
    result = WheaRecoveryBugCheck(result + 40, result + 96, 0, result + 40);
    goto loc_004ED5B7;
loc_004ED55F:
loc_004ED563:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x18)))) & (1)) == 0) goto loc_004ED5AB;
    if ((*(uint32_t *)(v_rip + 0xA0C9DE)) != 1) goto loc_004ED5AB;
    result = WheaIsCriticalState(result + 40, result + 96, 0, result + 40);
    if ((uint8_t)(result) != 0) goto loc_004ED5AB;
    if (sign_flag) goto loc_004ED5AB;
    goto loc_004ED44D;
loc_004ED589:
    result = WheapFreeErrorRecord(result, result + 96, 0, result + 40);
    goto loc_004ED5B7;
loc_004ED598:
    result = kernel_indirect_call(result + 40, result + 96, 0, result + 40);
loc_004ED5AB:
    result = WheapWorkQueueAddItem(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x18)) + 0x8D20) + 0x10), result, 0, result + 40);
loc_004ED5B7:
    goto loc_004ED604;
loc_004ED5BB:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)))) > ((uint32_t)(result + 40))) goto loc_004ED5CF;
    if (((*(uint8_t *)(arg1 + 0xC)) & ((uint8_t)(result + 40))) != 0) goto loc_004ED5CF;
    if (1 == 0) goto loc_004ED6AB;
loc_004ED5CF:
    *(uint32_t *)(local_rsp - 0x5F - 0x19) = 0x674C6857ULL;
    *(uint32_t *)(local_rsp - 0x5F - 0x15) = (uint32_t)(result + 40);
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = 32;
    *(uint32_t *)(local_rsp - 0x5F - 0xD) = (uint32_t)(result + 40);
    *(uint32_t *)(local_rsp - 0x5F - 0x5) = 0x80000036ULL;
    *(uint32_t *)(local_rsp - 0x5F - 0x9) = 0x4C4E524BULL;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = 2;
loc_004ED5FD:
    result = WheaLogInternalEvent(local_rsp - 95 - 25, result, 0, result + 40);
loc_004ED602:
    result = 0;
loc_004ED604:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, result, 0, result + 40);
    return result;
loc_004ED632:
    v_stack_m70 = *(uint64_t *)(v_stack_m28 + 0x38);
    result = KeBugCheckEx(290, 9, (int32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1C)), result);
loc_004ED64E:
    v_stack_m70 = *(uint64_t *)(v_stack_m28 + 0x38);
    result = KeBugCheckEx(290, 10, (int32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1C)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x18)));
loc_004ED66B:
    v_stack_m70 = *(uint64_t *)(v_stack_m28 + 0x38);
    result = KeBugCheckEx(290, 11, (int32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1C)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x18)));
loc_004ED688:
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x50);
    result = KeBugCheckEx(292, (int32_t)(*(uint32_t *)(result + 0x68)), *(uint64_t *)(v_stack_m28 + 0x40), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x21) + 0x48));
loc_004ED6AB:
    a4 = 0;
    a3 = 0;
    v_stack_m70 = *(uint64_t *)(v_stack_m28 + 0x38);
    result = KeBugCheckEx(292, (int32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1C)), a3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `W` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004ED200&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
