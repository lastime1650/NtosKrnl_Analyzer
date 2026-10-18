# CcFlushCachePreProcess

- RVA: `0x0035A9B0`–`0x0035B02F` (길이 `1,663` bytes)
- VA: `0x000000014035A9B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00079A7C`
- 디코드: `354`개 명령, `1,663/1,663` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0035AA87` → [CcSetTelemetryPeriodicTimer](../../page/AD/CcSetTelemetryPeriodicTimer_function_00ADB788.md) (function, `0x00ADB788`)
- `0x0035AAB6` → [KeRcuReadLock](../38/KeRcuReadLock_function_0038A1A0.md) (function, `0x0038A1A0`)
- `0x0035AAC6` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x0035AB00` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x0035AB32` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0035AB3B` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0035AB40` → [KeRcuReadUnlock](../38/KeRcuReadUnlock_function_0038A070.md) (function, `0x0038A070`)
- `0x0035ABDD` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0035ABE2` → [KeRcuReadUnlock](../38/KeRcuReadUnlock_function_0038A070.md) (function, `0x0038A070`)
- `0x0035AD49` → [CcUnmapVacbArray](../38/CcUnmapVacbArray_function_0038AEAC.md) (function, `0x0038AEAC`)
- `0x0035AD68` → [MmFlushSection](../23/MmFlushSection_function_002375E4.md) (function, `0x002375E4`)
- `0x0035AEB9` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0035AEDE` → [CcBoostLowPriorityWorkerThread](../57/CcBoostLowPriorityWorkerThread_function_0057B704.md) (function, `0x0057B704`)
- `0x0035AEEC` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0035AF24` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035AF81` → [CcSerializeWithLazyWriter](../4B/CcSerializeWithLazyWriter_function_004B4490.md) (function, `0x004B4490`)
- `0x0035AFCE` → [CcPerfLogFlushCache](../47/CcPerfLogFlushCache_function_00479A54.md) (function, `0x00479A54`)
- `0x0035AFF0` → [CcPerfLogFlushSection](../47/CcPerfLogFlushSection_function_0047CE0C.md) (function, `0x0047CE0C`)

### Direct callers
- [CcWriteBehindAsync](CcWriteBehindAsync_function_003549E8.md) at `0x00354A6A`
- [CcWriteBehindInternal](CcWriteBehindInternal_function_00357540.md) at `0x003575F1`
- [CcFlushCachePriv](CcFlushCachePriv_function_0035B040.md) at `0x0035B130`
- [CcAsyncLazywriteWorkerMulti](../4D/CcAsyncLazywriteWorkerMulti_function_004D1574.md) at `0x004D18EA`

### Static image references
- `0x0035A9F9` → RVA `0x00F8F4F0` (`.data`; read)
- `0x0035AA20` → RVA `0x00F8F2E0` (`.data`; read/write)
- `0x0035AA27` → RVA `0x00F8F2A1` (`.data`; read)
- `0x0035AA68` → RVA `0x00F8F3C0` (`.data`; read)
- `0x0035AA70` → RVA `0x00F8F260` (`.data`; read)
- `0x0035AA78` → RVA `0x00F8F3C4` (`.data`; read)
- `0x0035AA80` → RVA `0x00F8F280` (`.data`; read)
- `0x0035AAA2` → RVA `0x00F8F4F8` (`.data`; read)
- `0x0035AABF` → RVA `0x00E11CC0` (`.data`; read)
- `0x0035ABF3` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x0035AC83` → RVA `0x00E65B88` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0035AA87` → [CcSetTelemetryPeriodicTimer](../../page/AD/CcSetTelemetryPeriodicTimer_function_00ADB788.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x0035AE65` → [sub_006E2C34](../6E/Unknown_function_006E2C34.md) (`tail-transfer`)
  - `0x0035AE6D` → [sub_006E2C34](../6E/Unknown_function_006E2C34.md) (`tail-transfer`)
  - `0x0035AE79` → [sub_006E2C34](../6E/Unknown_function_006E2C34.md) (`tail-transfer`)
  - `0x0035AF75` → [sub_006E2C34 + 0xE](../6E/Unknown_function_006E2C34.md) (`tail-transfer`)
  - `0x0035AF8E` → [sub_006E2C34 + 0xE](../6E/Unknown_function_006E2C34.md) (`tail-transfer`)
  - `0x0035B004` → [sub_006E2C34 + 0x37](../6E/Unknown_function_006E2C34.md) (`tail-transfer`)
  - `0x0035B010` → [sub_006E2C34 + 0x3F](../6E/Unknown_function_006E2C34.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0035A9B0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0035A9B5  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0035A9BA  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0035A9BF  55                              push rbp
0035A9C0  41 54                           push r12
0035A9C2  41 55                           push r13
0035A9C4  41 56                           push r14
0035A9C6  41 57                           push r15
0035A9C8  48 8B EC                        mov rbp, rsp
0035A9CB  48 81 EC 80 00 00 00            sub rsp, 0x80
0035A9D2  4C 8B 71 70                     mov r14, qword ptr [rcx + 0x70]
0035A9D6  33 C0                           xor eax, eax
0035A9D8  8B 71 68                        mov esi, dword ptr [rcx + 0x68]
0035A9DB  33 D2                           xor edx, edx
0035A9DD  40 8A 79 6C                     mov dil, byte ptr [rcx + 0x6c]
0035A9E1  48 8B D9                        mov rbx, rcx
0035A9E4  0F 57 C0                        xorps xmm0, xmm0
0035A9E7  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0035A9EB  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0035A9EF  0F 57 C9                        xorps xmm1, xmm1
0035A9F2  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0035A9F6  44 8A FA                        mov r15b, dl
0035A9F9  48 8D 0D F0 4A C3 00            lea rcx, [rip + 0xc34af0]
0035AA00  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0035AA04  44 8B EA                        mov r13d, edx
0035AA07  44 8B E2                        mov r12d, edx
0035AA0A  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0035AA0E  0F 11 4D E8                     movups xmmword ptr [rbp - 0x18], xmm1
0035AA12  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0035AA16  48 39 53 58                     cmp qword ptr [rbx + 0x58], rdx
0035AA1A  0F 85 D6 04 00 00               jne 0x14035aef6
0035AA20  48 FF 05 B9 48 C3 00            inc qword ptr [rip + 0xc348b9]
0035AA27  38 15 74 48 C3 00               cmp byte ptr [rip + 0xc34874], dl
0035AA2D  74 39                           je 0x14035aa68
0035AA2F  41 89 16                        mov dword ptr [r14], edx
0035AA32  48 8D 05 B7 4A C3 00            lea rax, [rip + 0xc34ab7]
0035AA39  48 8B 4B 60                     mov rcx, qword ptr [rbx + 0x60]
0035AA3D  48 89 93 98 00 00 00            mov qword ptr [rbx + 0x98], rdx
0035AA44  48 3B C8                        cmp rcx, rax
0035AA47  75 47                           jne 0x14035aa90
0035AA49  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0035AA4D  48 89 83 B0 00 00 00            mov qword ptr [rbx + 0xb0], rax
0035AA54  41 C7 06 16 00 00 80            mov dword ptr [r14], 0x80000016
0035AA5B  C6 83 84 00 00 00 01            mov byte ptr [rbx + 0x84], 1
0035AA62  48 89 53 60                     mov qword ptr [rbx + 0x60], rdx
0035AA66  EB 4A                           jmp 0x14035aab2
0035AA68  39 15 52 49 C3 00               cmp dword ptr [rip + 0xc34952], edx
0035AA6E  75 BF                           jne 0x14035aa2f
0035AA70  38 15 EA 47 C3 00               cmp byte ptr [rip + 0xc347ea], dl
0035AA76  74 B7                           je 0x14035aa2f
0035AA78  39 15 46 49 C3 00               cmp dword ptr [rip + 0xc34946], edx
0035AA7E  75 AF                           jne 0x14035aa2f
0035AA80  48 8B 0D F9 47 C3 00            mov rcx, qword ptr [rip + 0xc347f9]
0035AA87  E8 FC 0C 78 00                  call 0x140adb788
0035AA8C  33 D2                           xor edx, edx
0035AA8E  EB 9F                           jmp 0x14035aa2f
0035AA90  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0035AA93  83 C8 01                        or eax, 1
0035AA96  89 43 38                        mov dword ptr [rbx + 0x38], eax
0035AA99  40 84 FF                        test dil, dil
0035AA9C  0F 85 88 04 00 00               jne 0x14035af2a
0035AAA2  48 8D 05 4F 4A C3 00            lea rax, [rip + 0xc34a4f]
0035AAA9  48 3B C8                        cmp rcx, rax
0035AAAC  0F 84 83 04 00 00               je 0x14035af35
0035AAB2  49 89 56 08                     mov qword ptr [r14 + 8], rdx
0035AAB6  E8 E5 F6 02 00                  call 0x14038a1a0
0035AABB  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0035AABF  48 8D 0D FA 71 AB 00            lea rcx, [rip + 0xab71fa]
0035AAC6  E8 D5 AC F1 FF                  call 0x1402757a0
0035AACB  48 8B 7D 30                     mov rdi, qword ptr [rbp + 0x30]
0035AACF  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
0035AAD3  48 89 7B 10                     mov qword ptr [rbx + 0x10], rdi
0035AAD7  48 85 FF                        test rdi, rdi
0035AADA  0F 84 99 00 00 00               je 0x14035ab79
0035AAE0  4C 8B AF 18 02 00 00            mov r13, qword ptr [rdi + 0x218]
0035AAE7  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0035AAEB  4C 8B A7 58 02 00 00            mov r12, qword ptr [rdi + 0x258]
0035AAF2  4C 89 2B                        mov qword ptr [rbx], r13
0035AAF5  4C 89 63 08                     mov qword ptr [rbx + 8], r12
0035AAF9  49 8D 8D 00 03 00 00            lea rcx, [r13 + 0x300]
0035AB00  E8 3B AC F1 FF                  call 0x140275740
0035AB05  80 BB 84 00 00 00 00            cmp byte ptr [rbx + 0x84], 0
0035AB0C  41 B7 01                        mov r15b, 1
0035AB0F  75 58                           jne 0x14035ab69
0035AB11  48 8B 4B 60                     mov rcx, qword ptr [rbx + 0x60]
0035AB15  48 85 C9                        test rcx, rcx
0035AB18  0F 84 31 03 00 00               je 0x14035ae4f
0035AB1E  48 8B 11                        mov rdx, qword ptr [rcx]
0035AB21  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
0035AB25  49 3B D0                        cmp rdx, r8
0035AB28  0F 8C 14 03 00 00               jl 0x14035ae42
0035AB2E  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0035AB32  E8 79 C6 EB FF                  call 0x1402171b0
0035AB37  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0035AB3B  E8 A0 81 FE FF                  call 0x140342ce0
0035AB40  E8 2B F5 02 00                  call 0x14038a070
0035AB45  32 C0                           xor al, al
0035AB47  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
0035AB4F  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0035AB53  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0035AB57  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0035AB5B  49 8B E3                        mov rsp, r11
0035AB5E  41 5F                           pop r15
0035AB60  41 5E                           pop r14
0035AB62  41 5D                           pop r13
0035AB64  41 5C                           pop r12
0035AB66  5D                              pop rbp
0035AB67  C3                              ret
0035AB68  CC                              int3
0035AB69  F7 87 98 00 00 00 00 00 01 00   test dword ptr [rdi + 0x98], 0x10000
0035AB73  0F 85 C8 03 00 00               jne 0x14035af41
0035AB79  8A 8B 84 00 00 00               mov cl, byte ptr [rbx + 0x84]
0035AB7F  84 C9                           test cl, cl
0035AB81  0F 84 82 02 00 00               je 0x14035ae09
0035AB87  48 83 7B 60 00                  cmp qword ptr [rbx + 0x60], 0
0035AB8C  0F 85 C8 02 00 00               jne 0x14035ae5a
0035AB92  8A 83 8A 00 00 00               mov al, byte ptr [rbx + 0x8a]
0035AB98  48 85 FF                        test rdi, rdi
0035AB9B  74 33                           je 0x14035abd0
0035AB9D  84 C0                           test al, al
0035AB9F  0F 85 C9 03 00 00               jne 0x14035af6e
0035ABA5  8B 47 04                        mov eax, dword ptr [rdi + 4]
0035ABA8  FF C0                           inc eax
0035ABAA  89 47 04                        mov dword ptr [rdi + 4], eax
0035ABAD  FF 87 20 02 00 00               inc dword ptr [rdi + 0x220]
0035ABB3  48 8B 47 60                     mov rax, qword ptr [rdi + 0x60]
0035ABB7  48 83 E0 F0                     and rax, 0xfffffffffffffff0
0035ABBB  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
0035ABBF  48 89 83 A8 00 00 00            mov qword ptr [rbx + 0xa8], rax
0035ABC6  8B 47 70                        mov eax, dword ptr [rdi + 0x70]
0035ABC9  48 89 83 D8 00 00 00            mov qword ptr [rbx + 0xd8], rax
0035ABD0  45 84 FF                        test r15b, r15b
0035ABD3  0F 85 0F 03 00 00               jne 0x14035aee8
0035ABD9  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0035ABDD  E8 FE 80 FE FF                  call 0x140342ce0
0035ABE2  E8 89 F4 02 00                  call 0x14038a070
0035ABE7  45 33 FF                        xor r15d, r15d
0035ABEA  48 85 FF                        test rdi, rdi
0035ABED  0F 85 A4 01 00 00               jne 0x14035ad97
0035ABF3  F7 05 13 BF C6 00 00 00 02 00   test dword ptr [rip + 0xc6bf13], 0x20000
0035ABFD  0F 85 90 03 00 00               jne 0x14035af93
0035AC03  44 38 BB 84 00 00 00            cmp byte ptr [rbx + 0x84], r15b
0035AC0A  0F 84 F0 00 00 00               je 0x14035ad00
0035AC10  48 85 FF                        test rdi, rdi
0035AC13  0F 84 F0 00 00 00               je 0x14035ad09
0035AC19  48 8B 8B A8 00 00 00            mov rcx, qword ptr [rbx + 0xa8]
0035AC20  F6 41 06 10                     test byte ptr [rcx + 6], 0x10
0035AC24  0F 85 54 02 00 00               jne 0x14035ae7e
0035AC2A  F7 87 98 00 00 00 00 00 02 00   test dword ptr [rdi + 0x98], 0x20000
0035AC34  0F 85 CF 00 00 00               jne 0x14035ad09
0035AC3A  44 38 BB 86 00 00 00            cmp byte ptr [rbx + 0x86], r15b
0035AC41  0F 85 CF 00 00 00               jne 0x14035ad16
0035AC47  48 85 FF                        test rdi, rdi
0035AC4A  0F 85 63 01 00 00               jne 0x14035adb3
0035AC50  44 38 BB 90 00 00 00            cmp byte ptr [rbx + 0x90], r15b
0035AC57  0F 85 B9 00 00 00               jne 0x14035ad16
0035AC5D  48 85 FF                        test rdi, rdi
0035AC60  0F 84 93 00 00 00               je 0x14035acf9
0035AC66  F7 87 98 00 00 00 00 00 00 04   test dword ptr [rdi + 0x98], 0x4000000
0035AC70  0F 85 83 00 00 00               jne 0x14035acf9
0035AC76  48 8B 4B 60                     mov rcx, qword ptr [rbx + 0x60]
0035AC7A  48 85 C9                        test rcx, rcx
0035AC7D  0F 85 08 01 00 00               jne 0x14035ad8b
0035AC83  8A 15 FF AE B0 00               mov dl, byte ptr [rip + 0xb0aeff]
0035AC89  49 8D 84 24 50 04 00 00         lea rax, [r12 + 0x450]
0035AC91  84 D2                           test dl, dl
0035AC93  0F 84 82 03 00 00               je 0x14035b01b
0035AC99  48 89 83 B8 00 00 00            mov qword ptr [rbx + 0xb8], rax
0035ACA0  49 8D 84 24 94 04 00 00         lea rax, [r12 + 0x494]
0035ACA8  84 D2                           test dl, dl
0035ACAA  75 07                           jne 0x14035acb3
0035ACAC  49 8D 85 0C 05 00 00            lea rax, [r13 + 0x50c]
0035ACB3  48 89 83 C0 00 00 00            mov qword ptr [rbx + 0xc0], rax
0035ACBA  8A 83 84 00 00 00               mov al, byte ptr [rbx + 0x84]
0035ACC0  84 C0                           test al, al
0035ACC2  0F 84 00 01 00 00               je 0x14035adc8
0035ACC8  C7 43 30 01 00 00 00            mov dword ptr [rbx + 0x30], 1
0035ACCF  85 F6                           test esi, esi
0035ACD1  0F 85 50 03 00 00               jne 0x14035b027
0035ACD7  84 C0                           test al, al
0035ACD9  74 11                           je 0x14035acec
0035ACDB  48 A1 20 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000320]
0035ACE5  48 89 83 98 00 00 00            mov qword ptr [rbx + 0x98], rax
0035ACEC  44 38 3D 95 AE B0 00            cmp byte ptr [rip + 0xb0ae95], r15b
0035ACF3  0F 85 94 01 00 00               jne 0x14035ae8d
0035ACF9  B0 01                           mov al, 1
0035ACFB  E9 47 FE FF FF                  jmp 0x14035ab47
0035AD00  48 85 FF                        test rdi, rdi
0035AD03  0F 85 C1 01 00 00               jne 0x14035aeca
0035AD09  44 38 BB 84 00 00 00            cmp byte ptr [rbx + 0x84], r15b
0035AD10  0F 85 24 FF FF FF               jne 0x14035ac3a
0035AD16  C6 83 87 00 00 00 01            mov byte ptr [rbx + 0x87], 1
0035AD1D  F7 05 E9 BD C6 00 00 00 02 00   test dword ptr [rip + 0xc6bde9], 0x20000
0035AD27  0F 85 AB 02 00 00               jne 0x14035afd8
0035AD2D  48 85 FF                        test rdi, rdi
0035AD30  74 1C                           je 0x14035ad4e
0035AD32  48 8B 53 60                     mov rdx, qword ptr [rbx + 0x60]
0035AD36  45 33 C9                        xor r9d, r9d
0035AD39  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
0035AD3E  44 8B C6                        mov r8d, esi
0035AD41  48 8B CF                        mov rcx, rdi
0035AD44  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
0035AD49  E8 5E 01 03 00                  call 0x14038aeac
0035AD4E  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0035AD51  45 33 C9                        xor r9d, r9d
0035AD54  48 8B 53 60                     mov rdx, qword ptr [rbx + 0x60]
0035AD58  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0035AD5C  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0035AD60  44 8B C6                        mov r8d, esi
0035AD63  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0035AD68  E8 77 C8 ED FF                  call 0x1402375e4
0035AD6D  85 C0                           test eax, eax
0035AD6F  0F 88 85 02 00 00               js 0x14035affa
0035AD75  41 8B 06                        mov eax, dword ptr [r14]
0035AD78  85 C0                           test eax, eax
0035AD7A  0F 89 DD FE FF FF               jns 0x14035ac5d
0035AD80  89 83 80 00 00 00               mov dword ptr [rbx + 0x80], eax
0035AD86  E9 D2 FE FF FF                  jmp 0x14035ac5d
0035AD8B  48 8B 01                        mov rax, qword ptr [rcx]
0035AD8E  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
0035AD92  E9 EC FE FF FF                  jmp 0x14035ac83
0035AD97  F7 87 98 00 00 00 00 00 00 40   test dword ptr [rdi + 0x98], 0x40000000
0035ADA1  0F 84 4C FE FF FF               je 0x14035abf3
0035ADA7  C6 83 86 00 00 00 01            mov byte ptr [rbx + 0x86], 1
0035ADAE  E9 40 FE FF FF                  jmp 0x14035abf3
0035ADB3  F7 87 98 00 00 00 00 00 00 04   test dword ptr [rdi + 0x98], 0x4000000
0035ADBD  0F 84 8D FE FF FF               je 0x14035ac50
0035ADC3  E9 4E FF FF FF                  jmp 0x14035ad16
0035ADC8  44 38 BB 86 00 00 00            cmp byte ptr [rbx + 0x86], r15b
0035ADCF  0F 85 F3 FE FF FF               jne 0x14035acc8
0035ADD5  44 38 BB 90 00 00 00            cmp byte ptr [rbx + 0x90], r15b
0035ADDC  0F 85 E6 FE FF FF               jne 0x14035acc8
0035ADE2  48 85 C9                        test rcx, rcx
0035ADE5  0F 85 DD FE FF FF               jne 0x14035acc8
0035ADEB  85 F6                           test esi, esi
0035ADED  0F 85 D5 FE FF FF               jne 0x14035acc8
0035ADF3  4C 39 7B 58                     cmp qword ptr [rbx + 0x58], r15
0035ADF7  0F 85 CB FE FF FF               jne 0x14035acc8
0035ADFD  C6 83 C8 00 00 00 01            mov byte ptr [rbx + 0xc8], 1
0035AE04  E9 BF FE FF FF                  jmp 0x14035acc8
0035AE09  80 BB 8A 00 00 00 00            cmp byte ptr [rbx + 0x8a], 0
0035AE10  0F 85 71 FD FF FF               jne 0x14035ab87
0035AE16  48 85 FF                        test rdi, rdi
0035AE19  0F 84 68 FD FF FF               je 0x14035ab87
0035AE1F  83 BF 0C 02 00 00 01            cmp dword ptr [rdi + 0x20c], 1
0035AE26  77 0E                           ja 0x14035ae36
0035AE28  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
0035AE2E  A8 20                           test al, 0x20
0035AE30  0F 84 51 FD FF FF               je 0x14035ab87
0035AE36  C6 83 90 00 00 00 01            mov byte ptr [rbx + 0x90], 1
0035AE3D  E9 45 FD FF FF                  jmp 0x14035ab87
0035AE42  48 8D 04 32                     lea rax, [rdx + rsi]
0035AE46  49 3B C0                        cmp rax, r8
0035AE49  0F 8F 12 01 00 00               jg 0x14035af61
0035AE4F  FF 87 0C 02 00 00               inc dword ptr [rdi + 0x20c]
0035AE55  E9 1F FD FF FF                  jmp 0x14035ab79
0035AE5A  85 F6                           test esi, esi
0035AE5C  0F 85 30 FD FF FF               jne 0x14035ab92
0035AE62  48 85 FF                        test rdi, rdi
0035AE65  0F 84 C9 7D 38 00               je 0x1406e2c34
0035AE6B  84 C9                           test cl, cl
0035AE6D  0F 85 C1 7D 38 00               jne 0x1406e2c34
0035AE73  FF 8F 0C 02 00 00               dec dword ptr [rdi + 0x20c]
0035AE79  E9 B6 7D 38 00                  jmp 0x1406e2c34
0035AE7E  F6 41 04 20                     test byte ptr [rcx + 4], 0x20
0035AE82  0F 85 81 FE FF FF               jne 0x14035ad09
0035AE88  E9 9D FD FF FF                  jmp 0x14035ac2a
0035AE8D  44 38 BB 84 00 00 00            cmp byte ptr [rbx + 0x84], r15b
0035AE94  0F 84 5F FE FF FF               je 0x14035acf9
0035AE9A  44 38 BB 87 00 00 00            cmp byte ptr [rbx + 0x87], r15b
0035AEA1  0F 85 52 FE FF FF               jne 0x14035acf9
0035AEA7  F7 87 98 00 00 00 00 02 00 40   test dword ptr [rdi + 0x98], 0x40000200
0035AEB1  0F 85 42 FE FF FF               jne 0x14035acf9
0035AEB7  33 C9                           xor ecx, ecx
0035AEB9  E8 22 39 02 00                  call 0x14037e7e0
0035AEBE  48 89 83 E8 00 00 00            mov qword ptr [rbx + 0xe8], rax
0035AEC5  E9 2F FE FF FF                  jmp 0x14035acf9
0035AECA  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
0035AED0  A8 20                           test al, 0x20
0035AED2  0F 84 41 FD FF FF               je 0x14035ac19
0035AED8  48 8B D7                        mov rdx, rdi
0035AEDB  49 8B CD                        mov rcx, r13
0035AEDE  E8 21 08 22 00                  call 0x14057b704
0035AEE3  E9 31 FD FF FF                  jmp 0x14035ac19
0035AEE8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0035AEEC  E8 BF C2 EB FF                  call 0x1402171b0
0035AEF1  E9 E3 FC FF FF                  jmp 0x14035abd9
0035AEF6  48 8B 43 60                     mov rax, qword ptr [rbx + 0x60]
0035AEFA  48 85 C0                        test rax, rax
0035AEFD  0F 84 1D FB FF FF               je 0x14035aa20
0035AF03  48 3B C1                        cmp rax, rcx
0035AF06  0F 84 14 FB FF FF               je 0x14035aa20
0035AF0C  45 33 C9                        xor r9d, r9d
0035AF0F  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0035AF14  BA AB 16 00 00                  mov edx, 0x16ab
0035AF19  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
0035AF20  41 8D 49 34                     lea ecx, [r9 + 0x34]
0035AF24  E8 37 27 1A 00                  call 0x1404fd660
0035AF29  CC                              int3
0035AF2A  83 C8 10                        or eax, 0x10
0035AF2D  89 43 38                        mov dword ptr [rbx + 0x38], eax
0035AF30  E9 6D FB FF FF                  jmp 0x14035aaa2
0035AF35  C6 83 8A 00 00 00 01            mov byte ptr [rbx + 0x8a], 1
0035AF3C  E9 21 FB FF FF                  jmp 0x14035aa62
0035AF41  44 88 BB 85 00 00 00            mov byte ptr [rbx + 0x85], r15b
0035AF48  83 BF 0C 02 00 00 00            cmp dword ptr [rdi + 0x20c], 0
0035AF4F  0F 84 24 FC FF FF               je 0x14035ab79
0035AF55  44 88 BB 86 00 00 00            mov byte ptr [rbx + 0x86], r15b
0035AF5C  E9 18 FC FF FF                  jmp 0x14035ab79
0035AF61  8B 77 20                        mov esi, dword ptr [rdi + 0x20]
0035AF64  2B 31                           sub esi, dword ptr [rcx]
0035AF66  89 73 68                        mov dword ptr [rbx + 0x68], esi
0035AF69  E9 E1 FE FF FF                  jmp 0x14035ae4f
0035AF6E  83 BF 0C 02 00 00 02            cmp dword ptr [rdi + 0x20c], 2
0035AF75  0F 83 C7 7C 38 00               jae 0x1406e2c42
0035AF7B  48 8B D7                        mov rdx, rdi
0035AF7E  49 8B CD                        mov rcx, r13
0035AF81  E8 0A 95 15 00                  call 0x1404b4490
0035AF86  84 C0                           test al, al
0035AF88  0F 85 17 FC FF FF               jne 0x14035aba5
0035AF8E  E9 AF 7C 38 00                  jmp 0x1406e2c42
0035AF93  80 BB 86 00 00 00 01            cmp byte ptr [rbx + 0x86], 1
0035AF9A  44 8B CE                        mov r9d, esi
0035AF9D  4C 8B 43 60                     mov r8, qword ptr [rbx + 0x60]
0035AFA1  0F 94 C2                        sete dl
0035AFA4  80 BB 85 00 00 00 01            cmp byte ptr [rbx + 0x85], 1
0035AFAB  88 54 24 30                     mov byte ptr [rsp + 0x30], dl
0035AFAF  48 8B D7                        mov rdx, rdi
0035AFB2  0F 94 C1                        sete cl
0035AFB5  80 BB 84 00 00 00 01            cmp byte ptr [rbx + 0x84], 1
0035AFBC  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
0035AFC0  48 8B 8B B0 00 00 00            mov rcx, qword ptr [rbx + 0xb0]
0035AFC7  0F 94 C0                        sete al
0035AFCA  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0035AFCE  E8 81 EA 11 00                  call 0x140479a54
0035AFD3  E9 2B FC FF FF                  jmp 0x14035ac03
0035AFD8  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0035AFDB  44 8B CE                        mov r9d, esi
0035AFDE  4C 8B 43 60                     mov r8, qword ptr [rbx + 0x60]
0035AFE2  48 8B D7                        mov rdx, rdi
0035AFE5  48 8B 8B B0 00 00 00            mov rcx, qword ptr [rbx + 0xb0]
0035AFEC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0035AFF0  E8 17 1E 12 00                  call 0x14047ce0c
0035AFF5  E9 33 FD FF FF                  jmp 0x14035ad2d
0035AFFA  41 8B 0E                        mov ecx, dword ptr [r14]
0035AFFD  44 38 BB 84 00 00 00            cmp byte ptr [rbx + 0x84], r15b
0035B004  0F 84 61 7C 38 00               je 0x1406e2c6b
0035B00A  81 F9 16 00 00 80               cmp ecx, 0x80000016
0035B010  0F 84 5D 7C 38 00               je 0x1406e2c73
0035B016  E9 5A FD FF FF                  jmp 0x14035ad75
0035B01B  49 8D 85 90 04 00 00            lea rax, [r13 + 0x490]
0035B022  E9 72 FC FF FF                  jmp 0x14035ac99
0035B027  89 73 30                        mov dword ptr [rbx + 0x30], esi
0035B02A  E9 A8 FC FF FF                  jmp 0x14035acd7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcFlushCachePreProcess(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int8 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (128);
    result = 0;
    a2 = 0;
    v_stack_m30 = 0;
    v_stack_m48 = 0;
    v_stack_p8 = *(unsigned __int64 *)(a1 + 24);
    v_stack_m68 = v_xmm0;
    v_stack_m40 = v_xmm1;
    v_stack_m58 = v_xmm0;
    if ((*(unsigned __int64 *)(a1 + 88)) != 0) goto loc_0035AEF6;
loc_0035AA20:
    if ((*(unsigned __int8 *)(v_rip + 12798068)) == 0) goto loc_0035AA68;
loc_0035AA2F:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 112)) = 0;
    *(unsigned __int64 *)(a1 + 152) = 0;
    if ((*(unsigned __int64 *)(a1 + 96)) != (v_rip + 12798647)) goto loc_0035AA90;
    *(unsigned __int64 *)(a1 + 176) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 112) + 8);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 112)) = 0x80000016ULL;
    *(unsigned __int8 *)(a1 + 132) = 1;
loc_0035AA62:
    *(unsigned __int64 *)(a1 + 96) = 0;
    goto loc_0035AAB2;
loc_0035AA68:
    if ((*(unsigned int *)(v_rip + 12798290)) != 0) goto loc_0035AA2F;
    if ((*(unsigned __int8 *)(v_rip + 12797930)) == 0) goto loc_0035AA2F;
    if ((*(unsigned int *)(v_rip + 12798278)) != 0) goto loc_0035AA2F;
    result = CcSetTelemetryPeriodicTimer(*(unsigned __int64 *)(v_rip + 12797945), a2, a3, a4);
    a2 = 0;
    goto loc_0035AA2F;
loc_0035AA90:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 56))) | (1));
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 108)) != 0) goto loc_0035AF2A;
loc_0035AAA2:
    if ((*(unsigned __int64 *)(v_rip + 12797945)) == (v_rip + 12798543)) goto loc_0035AF35;
loc_0035AAB2:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 112) + 8) = 0;
    result = KeRcuReadLock(*(unsigned __int64 *)(v_rip + 12797945), a2, a3, a4);
    result = KeAcquireInStackQueuedSpinLock(v_rip + 11235834, v_stack_m40, a3, a4);
    *(unsigned __int64 *)(a1 + 16) = *(unsigned __int64 *)(v_stack_p8 + 8);
    if (*(unsigned __int64 *)(v_stack_p8 + 8) == 0) goto loc_0035AB79;
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 536);
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 600);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 536) + 768, v_stack_m58, a3, a4);
    if ((*(unsigned __int8 *)(a1 + 132)) != 0) goto loc_0035AB69;
    if (*(unsigned __int64 *)(a1 + 96) == 0) goto loc_0035AE4F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 96))) < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 32))) goto loc_0035AE42;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m58, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 96)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 32), a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m40, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 96)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 32), a4);
    result = KeRcuReadUnlock(v_stack_m40, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 96)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 32), a4);
    result = 0;
loc_0035AB47:
    return result;
loc_0035AB69:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) & (0x10000ULL)) != 0) goto loc_0035AF41;
loc_0035AB79:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 132)) == 0) goto loc_0035AE09;
loc_0035AB87:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96)) != 0) goto loc_0035AE5A;
loc_0035AB92:
    if (*(unsigned __int64 *)(v_stack_m28 + 72) == 0) goto loc_0035ABD0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 138)) != 0) goto loc_0035AF6E;
loc_0035ABA5:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 4))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 4) = (unsigned int)(result);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 96)) & (-16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 168) = *(unsigned __int64 *)(result + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 216) = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 112));
loc_0035ABD0:
    if (1 != 0) goto loc_0035AEE8;
loc_0035ABD9:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m40, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 96)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 32), a4);
    result = KeRcuReadUnlock(v_stack_m40, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 96)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 32), a4);
    v_r15 = 0;
    if (*(unsigned __int64 *)(v_stack_m28 + 72) != 0) goto loc_0035AD97;
loc_0035ABF3:
    if (((*(unsigned int *)(v_rip + 13025043)) & (0x20000ULL)) != 0) goto loc_0035AF93;
loc_0035AC03:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 132)) == 0) goto loc_0035AD00;
    if (*(unsigned __int64 *)(v_stack_m28 + 72) == 0) goto loc_0035AD09;
loc_0035AC19:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 168) + 6)) & (16)) != 0) goto loc_0035AE7E;
loc_0035AC2A:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) & (0x20000ULL)) != 0) goto loc_0035AD09;
loc_0035AC3A:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 134)) != 0) goto loc_0035AD16;
    if (*(unsigned __int64 *)(v_stack_m28 + 72) != 0) goto loc_0035ADB3;
loc_0035AC50:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 144)) != 0) goto loc_0035AD16;
loc_0035AC5D:
    if (*(unsigned __int64 *)(v_stack_m28 + 72) == 0) goto loc_0035ACF9;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) & (0x4000000ULL)) != 0) goto loc_0035ACF9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96) != 0) goto loc_0035AD8B;
loc_0035AC83:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11579135)) == 0) goto loc_0035B01B;
loc_0035AC99:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 184) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 600) + 1104;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 600) + 1172;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11579135)) == 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 536) + 1292;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 192) = result;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 132)) == 0) goto loc_0035ADC8;
loc_0035ACC8:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 48) = 1;
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)) != 0) goto loc_0035B027;
loc_0035ACD7:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 132)) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 152) = *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 132);
    }
    if ((*(unsigned __int8 *)(v_rip + 11579029)) != 0) goto loc_0035AE8D;
loc_0035ACF9:
    goto loc_0035AB47;
loc_0035AD00:
    if (*(unsigned __int64 *)(v_stack_m28 + 72) != 0) goto loc_0035AECA;
loc_0035AD09:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 132)) != 0) goto loc_0035AC3A;
loc_0035AD16:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 135) = 1;
    if (((*(unsigned int *)(v_rip + 13024745)) & (0x20000ULL)) != 0) goto loc_0035AFD8;
loc_0035AD2D:
    result = 1;
    if (*(unsigned __int64 *)(v_stack_m28 + 72) != 0) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96);
        a4 = 0;
        v_stack_m58 = 0;
        a3 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64));
        a1 = *(unsigned __int64 *)(v_stack_m28 + 72);
        v_stack_m60 = 0;
        result = CcUnmapVacbArray(a1, a2, a3, a4);
    }
    a4 = 0;
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56)));
    v_stack_m60 = *(unsigned __int64 *)(a1 + 112);
    result = MmFlushSection(v_stack_p8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), a4);
    if (sign_flag) goto loc_0035AFFA;
loc_0035AD75:
    if (!sign_flag) goto loc_0035AC5D;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 128) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 112))));
    goto loc_0035AC5D;
loc_0035AD8B:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32) = *(unsigned __int64 *)(v_stack_p8);
    goto loc_0035AC83;
loc_0035AD97:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) & (0x40000000ULL)) == 0) goto loc_0035ABF3;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 134) = 1;
    goto loc_0035ABF3;
loc_0035ADB3:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) & (0x4000000ULL)) == 0) goto loc_0035AC50;
    goto loc_0035AD16;
loc_0035ADC8:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 134)) != 0) goto loc_0035ACC8;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 144)) != 0) goto loc_0035ACC8;
    if (v_stack_p8 != 0) goto loc_0035ACC8;
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)) != 0) goto loc_0035ACC8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 88)) != 0) goto loc_0035ACC8;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 200) = 1;
    goto loc_0035ACC8;
loc_0035AE09:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 138)) != 0) goto loc_0035AB87;
    if (*(unsigned __int64 *)(v_stack_m28 + 72) == 0) goto loc_0035AB87;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 524)) > 1) goto loc_0035AE36;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)))) & (32)) == 0) goto loc_0035AB87;
loc_0035AE36:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 144) = 1;
    goto loc_0035AB87;
loc_0035AE42:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96) + *(unsigned __int64 *)(v_stack_m28 + 64) * 1) > ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))))) goto loc_0035AF61;
loc_0035AE4F:
    goto loc_0035AB79;
loc_0035AE5A:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)) != 0) goto loc_0035AB92;
loc_0035AE7E:
    if (((*(unsigned __int8 *)(v_stack_p8 + 4)) & (32)) != 0) goto loc_0035AD09;
    goto loc_0035AC2A;
loc_0035AE8D:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 132)) == 0) goto loc_0035ACF9;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 135)) != 0) goto loc_0035ACF9;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) & (0x40000200ULL)) != 0) goto loc_0035ACF9;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 232) = result;
    goto loc_0035ACF9;
loc_0035AECA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)))) & (32)) == 0) goto loc_0035AC19;
    result = CcBoostLowPriorityWorkerThread(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 536), *(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), a4);
    goto loc_0035AC19;
loc_0035AEE8:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m58, *(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), a4);
    goto loc_0035ABD9;
loc_0035AEF6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96) == 0) goto loc_0035AA20;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96)) == v_stack_m58) goto loc_0035AA20;
    a4 = 0;
    v_stack_m60 = *(unsigned __int64 *)(v_stack_m28 + 72);
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0x16ABULL), 0xFFFFFFFFC0000420ULL, a4);
loc_0035AF2A:
    result = (unsigned int)((result) | (16));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56) = (unsigned int)(result);
    goto loc_0035AAA2;
loc_0035AF35:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 138) = 1;
    goto loc_0035AA62;
loc_0035AF41:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 133) = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 524)) == 0) goto loc_0035AB79;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 134) = 0;
    goto loc_0035AB79;
loc_0035AF61:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 32))) - (*(unsigned int *)(a4 + 52)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 104) = (unsigned int)(v_rsi);
    goto loc_0035AE4F;
loc_0035AF6E:
    result = CcSerializeWithLazyWriter(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 536), *(unsigned __int64 *)(v_stack_m28 + 72), 0xFFFFFFFFC0000420ULL, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0035ABA5;
loc_0035AF93:
    a2 = ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 134)) == 1) ? 1 : 0;
    v_stack_m50 = (unsigned __int8)(a2);
    a1 = ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 133)) == 1) ? 1 : 0;
    v_stack_m58 = (unsigned __int8)(a1);
    result = ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 132)) == 1) ? 1 : 0;
    v_stack_m60 = (unsigned __int8)(result);
    result = CcPerfLogFlushCache(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 176), *(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96), (unsigned int)((unsigned int)(v_rsi)));
    goto loc_0035AC03;
loc_0035AFD8:
    v_stack_m60 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56)));
    result = CcPerfLogFlushSection(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 176), *(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 96), (unsigned int)((unsigned int)(v_rsi)));
    goto loc_0035AD2D;
loc_0035AFFA:
    goto loc_0035AD75;
loc_0035B01B:
    goto loc_0035AC99;
loc_0035B027:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 48) = (unsigned int)(v_rsi);
    goto loc_0035ACD7;
}
```

## 5. (Beta) C Style

```c
int64_t CcFlushCachePreProcess(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint8_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (128);
    result = 0;
    Arg2 = 0;
    v_stack_m30 = 0;
    v_stack_m48 = 0;
    v_stack_p8 = *(uint64_t *)(arg1 + 0x18);
    v_stack_m68 = v_xmm0;
    v_stack_m40 = v_xmm1;
    v_stack_m58 = v_xmm0;
    if ((*(uint64_t *)(arg1 + 0x58)) != 0) goto loc_0035AEF6;
loc_0035AA20:
    if ((*(uint8_t *)(v_rip + 0xC34874)) == 0) goto loc_0035AA68;
loc_0035AA2F:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x70)) = 0;
    *(uint64_t *)(arg1 + 0x98) = 0;
    if ((*(uint64_t *)(arg1 + 0x60)) != (v_rip + 12798647)) goto loc_0035AA90;
    *(uint64_t *)(arg1 + 0xB0) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x70) + 0x8);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x70)) = 0x80000016ULL;
    *(uint8_t *)(arg1 + 0x84) = 1;
loc_0035AA62:
    *(uint64_t *)(arg1 + 0x60) = 0;
    goto loc_0035AAB2;
loc_0035AA68:
    if ((*(uint32_t *)(v_rip + 0xC34952)) != 0) goto loc_0035AA2F;
    if ((*(uint8_t *)(v_rip + 0xC347EA)) == 0) goto loc_0035AA2F;
    if ((*(uint32_t *)(v_rip + 0xC34946)) != 0) goto loc_0035AA2F;
    result = CcSetTelemetryPeriodicTimer(*(uint64_t *)(v_rip + 0xC347F9), Arg2, Arg3, Arg4);
    Arg2 = 0;
    goto loc_0035AA2F;
loc_0035AA90:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x38))) | (1));
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x6C)) != 0) goto loc_0035AF2A;
loc_0035AAA2:
    if ((*(uint64_t *)(v_rip + 0xC347F9)) == (v_rip + 12798543)) goto loc_0035AF35;
loc_0035AAB2:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x70) + 0x8) = 0;
    result = KeRcuReadLock(*(uint64_t *)(v_rip + 0xC347F9), Arg2, Arg3, Arg4);
    result = KeAcquireInStackQueuedSpinLock(v_rip + 11235834, v_stack_m40, Arg3, Arg4);
    *(uint64_t *)(arg1 + 0x10) = *(uint64_t *)(v_stack_p8 + 0x8);
    if (*(uint64_t *)(v_stack_p8 + 0x8) == 0) goto loc_0035AB79;
    *(uint64_t *)(arg1) = *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x218);
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x258);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x218) + 768, v_stack_m58, Arg3, Arg4);
    if ((*(uint8_t *)(arg1 + 0x84)) != 0) goto loc_0035AB69;
    if (*(uint64_t *)(arg1 + 0x60) == 0) goto loc_0035AE4F;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x60))) < (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x20))) goto loc_0035AE42;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m58, *(uint64_t *)(*(uint64_t *)(arg1 + 0x60)), *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x20), Arg4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m40, *(uint64_t *)(*(uint64_t *)(arg1 + 0x60)), *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x20), Arg4);
    result = KeRcuReadUnlock(v_stack_m40, *(uint64_t *)(*(uint64_t *)(arg1 + 0x60)), *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x20), Arg4);
    result = 0;
loc_0035AB47:
    return result;
loc_0035AB69:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) & (0x10000ULL)) != 0) goto loc_0035AF41;
loc_0035AB79:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x84)) == 0) goto loc_0035AE09;
loc_0035AB87:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60)) != 0) goto loc_0035AE5A;
loc_0035AB92:
    if (*(uint64_t *)(v_stack_m28 + 0x48) == 0) goto loc_0035ABD0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8A)) != 0) goto loc_0035AF6E;
loc_0035ABA5:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x4))) + 1);
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x4) = (uint32_t)(result);
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x60)) & (-16);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xA8) = *(uint64_t *)(result + 0x18);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xD8) = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x70));
loc_0035ABD0:
    if (1 != 0) goto loc_0035AEE8;
loc_0035ABD9:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m40, *(uint64_t *)(*(uint64_t *)(arg1 + 0x60)), *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x20), Arg4);
    result = KeRcuReadUnlock(v_stack_m40, *(uint64_t *)(*(uint64_t *)(arg1 + 0x60)), *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x20), Arg4);
    local_r15 = 0;
    if (*(uint64_t *)(v_stack_m28 + 0x48) != 0) goto loc_0035AD97;
loc_0035ABF3:
    if (((*(uint32_t *)(v_rip + 0xC6BF13)) & (0x20000ULL)) != 0) goto loc_0035AF93;
loc_0035AC03:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x84)) == 0) goto loc_0035AD00;
    if (*(uint64_t *)(v_stack_m28 + 0x48) == 0) goto loc_0035AD09;
loc_0035AC19:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xA8) + 0x6)) & (16)) != 0) goto loc_0035AE7E;
loc_0035AC2A:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) & (0x20000ULL)) != 0) goto loc_0035AD09;
loc_0035AC3A:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x86)) != 0) goto loc_0035AD16;
    if (*(uint64_t *)(v_stack_m28 + 0x48) != 0) goto loc_0035ADB3;
loc_0035AC50:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x90)) != 0) goto loc_0035AD16;
loc_0035AC5D:
    if (*(uint64_t *)(v_stack_m28 + 0x48) == 0) goto loc_0035ACF9;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) & (0x4000000ULL)) != 0) goto loc_0035ACF9;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60) != 0) goto loc_0035AD8B;
loc_0035AC83:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xB0AEFF)) == 0) goto loc_0035B01B;
loc_0035AC99:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xB8) = *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x258) + 1104;
    result = *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x258) + 1172;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xB0AEFF)) == 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x218) + 1292;
    }
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xC0) = result;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x84)) == 0) goto loc_0035ADC8;
loc_0035ACC8:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x30) = 1;
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)) != 0) goto loc_0035B027;
loc_0035ACD7:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x84)) != 0) {
        *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x98) = *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x84);
    }
    if ((*(uint8_t *)(v_rip + 0xB0AE95)) != 0) goto loc_0035AE8D;
loc_0035ACF9:
    goto loc_0035AB47;
loc_0035AD00:
    if (*(uint64_t *)(v_stack_m28 + 0x48) != 0) goto loc_0035AECA;
loc_0035AD09:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x84)) != 0) goto loc_0035AC3A;
loc_0035AD16:
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x87) = 1;
    if (((*(uint32_t *)(v_rip + 0xC6BDE9)) & (0x20000ULL)) != 0) goto loc_0035AFD8;
loc_0035AD2D:
    result = 1;
    if (*(uint64_t *)(v_stack_m28 + 0x48) != 0) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60);
        Arg4 = 0;
        v_stack_m58 = 0;
        Arg3 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40));
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x48);
        v_stack_m60 = 0;
        result = CcUnmapVacbArray(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38)));
    v_stack_m60 = *(uint64_t *)(arg1 + 0x70);
    result = MmFlushSection(v_stack_p8, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), Arg4);
    if (sign_flag) goto loc_0035AFFA;
loc_0035AD75:
    if (!sign_flag) goto loc_0035AC5D;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x80) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x70))));
    goto loc_0035AC5D;
loc_0035AD8B:
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20) = *(uint64_t *)(v_stack_p8);
    goto loc_0035AC83;
loc_0035AD97:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) & (0x40000000ULL)) == 0) goto loc_0035ABF3;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x86) = 1;
    goto loc_0035ABF3;
loc_0035ADB3:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) & (0x4000000ULL)) == 0) goto loc_0035AC50;
    goto loc_0035AD16;
loc_0035ADC8:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x86)) != 0) goto loc_0035ACC8;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x90)) != 0) goto loc_0035ACC8;
    if (v_stack_p8 != 0) goto loc_0035ACC8;
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)) != 0) goto loc_0035ACC8;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x58)) != 0) goto loc_0035ACC8;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xC8) = 1;
    goto loc_0035ACC8;
loc_0035AE09:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8A)) != 0) goto loc_0035AB87;
    if (*(uint64_t *)(v_stack_m28 + 0x48) == 0) goto loc_0035AB87;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x20C)) > 1) goto loc_0035AE36;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)))) & (32)) == 0) goto loc_0035AB87;
loc_0035AE36:
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x90) = 1;
    goto loc_0035AB87;
loc_0035AE42:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60) + *(uint64_t *)(v_stack_m28 + 0x40) * 1) > ((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))))) goto loc_0035AF61;
loc_0035AE4F:
    goto loc_0035AB79;
loc_0035AE5A:
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)) != 0) goto loc_0035AB92;
loc_0035AE7E:
    if (((*(uint8_t *)(v_stack_p8 + 0x4)) & (32)) != 0) goto loc_0035AD09;
    goto loc_0035AC2A;
loc_0035AE8D:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x84)) == 0) goto loc_0035ACF9;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x87)) != 0) goto loc_0035ACF9;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) & (0x40000200ULL)) != 0) goto loc_0035ACF9;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), Arg4);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xE8) = result;
    goto loc_0035ACF9;
loc_0035AECA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)))) & (32)) == 0) goto loc_0035AC19;
    result = CcBoostLowPriorityWorkerThread(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x218), *(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), Arg4);
    goto loc_0035AC19;
loc_0035AEE8:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m58, *(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), Arg4);
    goto loc_0035ABD9;
loc_0035AEF6:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60) == 0) goto loc_0035AA20;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60)) == v_stack_m58) goto loc_0035AA20;
    Arg4 = 0;
    v_stack_m60 = *(uint64_t *)(v_stack_m28 + 0x48);
    result = KeBugCheckEx(Arg4 + 52, (uint32_t)(0x16ABULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_0035AF2A:
    result = (uint32_t)((result) | (16));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38) = (uint32_t)(result);
    goto loc_0035AAA2;
loc_0035AF35:
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8A) = 1;
    goto loc_0035AA62;
loc_0035AF41:
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x85) = 0;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x20C)) == 0) goto loc_0035AB79;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x86) = 0;
    goto loc_0035AB79;
loc_0035AF61:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x20))) - (*(uint32_t *)(Arg4 + 0x34)));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x68) = (uint32_t)(local_rsi);
    goto loc_0035AE4F;
loc_0035AF6E:
    result = CcSerializeWithLazyWriter(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x218), *(uint64_t *)(v_stack_m28 + 0x48), 0xFFFFFFFFC0000420ULL, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0035ABA5;
loc_0035AF93:
    Arg2 = ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x86)) == 1) ? 1 : 0;
    v_stack_m50 = (uint8_t)(Arg2);
    Arg1 = ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x85)) == 1) ? 1 : 0;
    v_stack_m58 = (uint8_t)(Arg1);
    result = ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x84)) == 1) ? 1 : 0;
    v_stack_m60 = (uint8_t)(result);
    result = CcPerfLogFlushCache(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xB0), *(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60), (uint32_t)((uint32_t)(local_rsi)));
    goto loc_0035AC03;
loc_0035AFD8:
    v_stack_m60 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38)));
    result = CcPerfLogFlushSection(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xB0), *(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x60), (uint32_t)((uint32_t)(local_rsi)));
    goto loc_0035AD2D;
loc_0035AFFA:
    goto loc_0035AD75;
loc_0035B01B:
    goto loc_0035AC99;
loc_0035B027:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x30) = (uint32_t)(local_rsi);
    goto loc_0035ACD7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x30` | `32` | `W` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `W` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x68` | `32` | `W` |
| `Arg1` | `+ 0x6C` | `8` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x80` | `32` | `W` |
| `Arg1` | `+ 0x84` | `8` | `R` |
| `Arg1` | `+ 0x84` | `8` | `W` |
| `Arg1` | `+ 0x85` | `8` | `R` |
| `Arg1` | `+ 0x85` | `8` | `W` |
| `Arg1` | `+ 0x86` | `8` | `R` |
| `Arg1` | `+ 0x86` | `8` | `W` |
| `Arg1` | `+ 0x87` | `8` | `R` |
| `Arg1` | `+ 0x87` | `8` | `W` |
| `Arg1` | `+ 0x8A` | `8` | `R` |
| `Arg1` | `+ 0x8A` | `8` | `W` |
| `Arg1` | `+ 0x90` | `8` | `R` |
| `Arg1` | `+ 0x90` | `8` | `W` |
| `Arg1` | `+ 0x98` | `64` | `W` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `W` |
| `Arg1` | `+ 0xB0` | `64` | `R` |

추가 오프셋 6개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0035A9B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
