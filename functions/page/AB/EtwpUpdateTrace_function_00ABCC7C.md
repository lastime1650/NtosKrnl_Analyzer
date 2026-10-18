# EtwpUpdateTrace

- RVA: `0x00ABCC7C`–`0x00ABD153` (길이 `1,239` bytes)
- VA: `0x0000000140ABCC7C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD508`
- 디코드: `325`개 명령, `1,239/1,239` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00ABCCAF` → [EtwpValidateLoggerInfo](../8B/EtwpValidateLoggerInfo_function_008BF9B0.md) (function, `0x008BF9B0`)
- `0x00ABCCBC` → [EtwpValidateFlagExtension](EtwpValidateFlagExtension_function_00ABD15C.md) (function, `0x00ABD15C`)
- `0x00ABCCE4` → [EtwpAcquireLoggerContext](../93/EtwpAcquireLoggerContext_function_009326AC.md) (function, `0x009326AC`)
- `0x00ABCD8B` → [EtwpCheckLoggerControlAccess](../8C/EtwpCheckLoggerControlAccess_function_008C0AE0.md) (function, `0x008C0AE0`)
- `0x00ABCDDB` → [EtwpCaptureString](../9B/EtwpCaptureString_function_009BD754.md) (function, `0x009BD754`)
- `0x00ABCDFA` → [SeDeleteClientSecurity](../92/SeDeleteClientSecurity_function_00923F90.md) (function, `0x00923F90`)
- `0x00ABCE35` → [SeCreateClientSecurity](../89/SeCreateClientSecurity_function_008911B0.md) (function, `0x008911B0`)
- `0x00ABCE5C` → [EtwpSynchronizeWithLogger](../A6/EtwpSynchronizeWithLogger_function_00A66250.md) (function, `0x00A66250`)
- `0x00ABCE69` → [EtwpSynchronizeWithLogger](../A6/EtwpSynchronizeWithLogger_function_00A66250.md) (function, `0x00A66250`)
- `0x00ABCEDC` → [EtwpSynchronizeWithLogger](../A6/EtwpSynchronizeWithLogger_function_00A66250.md) (function, `0x00A66250`)
- `0x00ABCF38` → [EtwpUpdatePerProcessTracing](../A6/EtwpUpdatePerProcessTracing_function_00A67374.md) (function, `0x00A67374`)
- `0x00ABCF43` → [EtwpCheckForStackTracingExtension](../A6/EtwpCheckForStackTracingExtension_function_00A675F8.md) (function, `0x00A675F8`)
- `0x00ABCF66` → [EtwpCheckSystemTraceAccess](../A8/EtwpCheckSystemTraceAccess_function_00A8DE44.md) (function, `0x00A8DE44`)
- `0x00ABCF87` → [EtwpCheckForPoolTagFilterExtension](../A6/EtwpCheckForPoolTagFilterExtension_function_00A676B0.md) (function, `0x00A676B0`)
- `0x00ABCF9C` → [EtwpUpdateLoggerGroupMasks](../A6/EtwpUpdateLoggerGroupMasks_function_00A67490.md) (function, `0x00A67490`)
- `0x00ABCFBB` → [EtwpGetSystemMaximumBufferCount](../A7/EtwpGetSystemMaximumBufferCount_function_00A74890.md) (function, `0x00A74890`)
- `0x00ABCFFF` → [EtwpSynchronizeWithLogger](../A6/EtwpSynchronizeWithLogger_function_00A66250.md) (function, `0x00A66250`)
- `0x00ABD051` → [EtwpSendDbgId](../7B/EtwpSendDbgId_function_007BC1C0.md) (function, `0x007BC1C0`)
- `0x00ABD079` → [EtwpGetSecurityDescriptorByGuid](../8C/EtwpGetSecurityDescriptorByGuid_function_008C04C0.md) (function, `0x008C04C0`)
- `0x00ABD085` → [EtwpUpdateLoggerSecurityDescriptor](../AA/EtwpUpdateLoggerSecurityDescriptor_function_00AA9F64.md) (function, `0x00AA9F64`)
- `0x00ABD090` → [EtwpFreeSecurityDescriptor](../A1/EtwpFreeSecurityDescriptor_function_00A1E7DC.md) (function, `0x00A1E7DC`)
- `0x00ABD0BB` → [EtwpQueryUsedProcessorCount](../../text/3E/EtwpQueryUsedProcessorCount_function_003EB940.md) (function, `0x003EB940`)
- `0x00ABD0EC` → [EtwpGetLoggerInfoFromContext](../8B/EtwpGetLoggerInfoFromContext_function_008BEF90.md) (function, `0x008BEF90`)
- `0x00ABD101` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00ABD114` → [EtwpEventWriteTemplateSession](../9B/EtwpEventWriteTemplateSession_function_009BD120.md) (function, `0x009BD120`)
- `0x00ABD124` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ABD12E` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00ABD133` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [EtwWmitraceWorker](../7B/EtwWmitraceWorker_function_007BBD3C.md) at `0x007BBED6`
- [NtTraceControl](../A9/NtTraceControl_function_00A9ED40.md) at `0x00A9F09C`

### Static image references
- `0x00ABCEE1` → RVA `0x0002B180` (`.rdata`; read)
- `0x00ABCEF8` → RVA `0x0002B188` (`.rdata`; read)
- `0x00ABCF0E` → RVA `0x0002B020` (`.rdata`; read)
- `0x00ABCF1A` → RVA `0x0002B028` (`.rdata`; read)
- `0x00ABCF75` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x00ABD02F` → RVA `0x00F475DC` (`.data`; read)
- `0x00ABD038` → RVA `0x00E0AA1C` (`.data`; read)
- `0x00ABD041` → RVA `0x00F55CB3` (`.data`; read)
- `0x00ABD0F1` → RVA `0x00EFF840` (`.data`; read)
- `0x00ABD0F8` → RVA `0x00022E70` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00ABD0BB` → [EtwpQueryUsedProcessorCount](../../text/3E/EtwpQueryUsedProcessorCount_function_003EB940.md) (`PAGE` → `.text`)
  - `0x00ABD101` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00ABD133` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABCC7C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00ABCC81  55                              push rbp
00ABCC82  56                              push rsi
00ABCC83  57                              push rdi
00ABCC84  41 54                           push r12
00ABCC86  41 55                           push r13
00ABCC88  41 56                           push r14
00ABCC8A  41 57                           push r15
00ABCC8C  48 8B EC                        mov rbp, rsp
00ABCC8F  48 83 EC 50                     sub rsp, 0x50
00ABCC93  45 33 E4                        xor r12d, r12d
00ABCC96  4C 8B E9                        mov r13, rcx
00ABCC99  0F 57 C0                        xorps xmm0, xmm0
00ABCC9C  4C 89 65 50                     mov qword ptr [rbp + 0x50], r12
00ABCCA0  48 8B CA                        mov rcx, rdx
00ABCCA3  66 44 89 65 E2                  mov word ptr [rbp - 0x1e], r12w
00ABCCA8  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00ABCCAC  48 8B F2                        mov rsi, rdx
00ABCCAF  E8 FC 2C E0 FF                  call 0x1408bf9b0
00ABCCB4  85 C0                           test eax, eax
00ABCCB6  0F 88 7E 04 00 00               js 0x140abd13a
00ABCCBC  E8 9B 04 00 00                  call 0x140abd15c
00ABCCC1  85 C0                           test eax, eax
00ABCCC3  0F 88 71 04 00 00               js 0x140abd13a
00ABCCC9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00ABCCD2  4C 8D 45 50                     lea r8, [rbp + 0x50]
00ABCCD6  48 8B D6                        mov rdx, rsi
00ABCCD9  49 8B CD                        mov rcx, r13
00ABCCDC  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00ABCCE3  90                              nop
00ABCCE4  E8 C3 59 E7 FF                  call 0x1409326ac
00ABCCE9  8B D8                           mov ebx, eax
00ABCCEB  85 C0                           test eax, eax
00ABCCED  0F 88 40 04 00 00               js 0x140abd133
00ABCCF3  48 8B 7D 50                     mov rdi, qword ptr [rbp + 0x50]
00ABCCF7  44 8B 7E 40                     mov r15d, dword ptr [rsi + 0x40]
00ABCCFB  48 8D 47 0C                     lea rax, [rdi + 0xc]
00ABCCFF  44 8B 30                        mov r14d, dword ptr [rax]
00ABCD02  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00ABCD06  41 F6 C6 40                     test r14b, 0x40
00ABCD0A  0F 85 0B 04 00 00               jne 0x140abd11b
00ABCD10  41 8B C7                        mov eax, r15d
00ABCD13  83 E0 03                        and eax, 3
00ABCD16  3C 03                           cmp al, 3
00ABCD18  0F 84 FD 03 00 00               je 0x140abd11b
00ABCD1E  B9 00 C0 00 00                  mov ecx, 0xc000
00ABCD23  41 8B C7                        mov eax, r15d
00ABCD26  23 C1                           and eax, ecx
00ABCD28  3B C1                           cmp eax, ecx
00ABCD2A  0F 84 EB 03 00 00               je 0x140abd11b
00ABCD30  41 F6 C7 02                     test r15b, 2
00ABCD34  0F 95 C1                        setne cl
00ABCD37  41 F6 C6 02                     test r14b, 2
00ABCD3B  0F 94 C0                        sete al
00ABCD3E  84 C8                           test al, cl
00ABCD40  0F 85 D5 03 00 00               jne 0x140abd11b
00ABCD46  41 8B C7                        mov eax, r15d
00ABCD49  83 E0 06                        and eax, 6
00ABCD4C  3C 06                           cmp al, 6
00ABCD4E  0F 84 C7 03 00 00               je 0x140abd11b
00ABCD54  41 8B C7                        mov eax, r15d
00ABCD57  41 0B C6                        or eax, r14d
00ABCD5A  0F BA E0 08                     bt eax, 8
00ABCD5E  0F 93 C0                        setae al
00ABCD61  F6 D8                           neg al
00ABCD63  1B C9                           sbb ecx, ecx
00ABCD65  83 E1 E0                        and ecx, 0xffffffe0
00ABCD68  81 C1 A0 00 00 00               add ecx, 0xa0
00ABCD6E  8B C1                           mov eax, ecx
00ABCD70  4C 39 A6 88 00 00 00            cmp qword ptr [rsi + 0x88], r12
00ABCD77  74 0D                           je 0x140abcd86
00ABCD79  66 44 39 A6 80 00 00 00         cmp word ptr [rsi + 0x80], r12w
00ABCD81  76 03                           jbe 0x140abcd86
00ABCD83  83 C8 40                        or eax, 0x40
00ABCD86  48 8B D7                        mov rdx, rdi
00ABCD89  8B C8                           mov ecx, eax
00ABCD8B  E8 50 3D E0 FF                  call 0x1408c0ae0
00ABCD90  8B D8                           mov ebx, eax
00ABCD92  85 C0                           test eax, eax
00ABCD94  0F 88 86 03 00 00               js 0x140abd120
00ABCD9A  4C 39 A6 88 00 00 00            cmp qword ptr [rsi + 0x88], r12
00ABCDA1  0F 84 E0 00 00 00               je 0x140abce87
00ABCDA7  48 8D 8E 80 00 00 00            lea rcx, [rsi + 0x80]
00ABCDAE  66 44 39 21                     cmp word ptr [rcx], r12w
00ABCDB2  0F 86 CF 00 00 00               jbe 0x140abce87
00ABCDB8  41 F6 C6 08                     test r14b, 8
00ABCDBC  0F 85 59 03 00 00               jne 0x140abd11b
00ABCDC2  41 F6 C7 08                     test r15b, 8
00ABCDC6  0F 85 4F 03 00 00               jne 0x140abd11b
00ABCDCC  41 0F BA E6 0A                  bt r14d, 0xa
00ABCDD1  0F 82 44 03 00 00               jb 0x140abd11b
00ABCDD7  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00ABCDDB  E8 74 09 F0 FF                  call 0x1409bd754
00ABCDE0  8B D8                           mov ebx, eax
00ABCDE2  85 C0                           test eax, eax
00ABCDE4  0F 88 36 03 00 00               js 0x140abd120
00ABCDEA  4C 39 A7 D0 02 00 00            cmp qword ptr [rdi + 0x2d0], r12
00ABCDF1  74 13                           je 0x140abce06
00ABCDF3  48 8D 8F C0 02 00 00            lea rcx, [rdi + 0x2c0]
00ABCDFA  E8 91 71 E6 FF                  call 0x140923f90
00ABCDFF  4C 89 A7 D0 02 00 00            mov qword ptr [rdi + 0x2d0], r12
00ABCE06  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00ABCE0F  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00ABCE13  48 8B 7D 50                     mov rdi, qword ptr [rbp + 0x50]
00ABCE17  45 33 C0                        xor r8d, r8d
00ABCE1A  C7 45 D8 0C 00 00 00            mov dword ptr [rbp - 0x28], 0xc
00ABCE21  C7 45 DC 02 00 00 00            mov dword ptr [rbp - 0x24], 2
00ABCE28  66 C7 45 E0 01 01               mov word ptr [rbp - 0x20], 0x101
00ABCE2E  4C 8D 8F C0 02 00 00            lea r9, [rdi + 0x2c0]
00ABCE35  E8 76 43 DD FF                  call 0x1408911b0
00ABCE3A  8B D8                           mov ebx, eax
00ABCE3C  85 C0                           test eax, eax
00ABCE3E  0F 88 DC 02 00 00               js 0x140abd120
00ABCE44  0F 10 45 E8                     movups xmm0, xmmword ptr [rbp - 0x18]
00ABCE48  BA 04 00 00 00                  mov edx, 4
00ABCE4D  4C 89 65 F0                     mov qword ptr [rbp - 0x10], r12
00ABCE51  48 8B CF                        mov rcx, rdi
00ABCE54  F3 0F 7F 87 B8 00 00 00         movdqu xmmword ptr [rdi + 0xb8], xmm0
00ABCE5C  E8 EF 93 FA FF                  call 0x140a66250
00ABCE61  BA 02 00 00 00                  mov edx, 2
00ABCE66  48 8B CF                        mov rcx, rdi
00ABCE69  E8 E2 93 FA FF                  call 0x140a66250
00ABCE6E  8B D8                           mov ebx, eax
00ABCE70  85 C0                           test eax, eax
00ABCE72  0F 88 A8 02 00 00               js 0x140abd120
00ABCE78  44 39 A7 40 01 00 00            cmp dword ptr [rdi + 0x140], r12d
00ABCE7F  0F 84 9B 02 00 00               je 0x140abd120
00ABCE85  EB 07                           jmp 0x140abce8e
00ABCE87  41 0F BA E6 0A                  bt r14d, 0xa
00ABCE8C  72 53                           jb 0x140abcee1
00ABCE8E  B8 00 01 00 00                  mov eax, 0x100
00ABCE93  44 85 F8                        test eax, r15d
00ABCE96  74 25                           je 0x140abcebd
00ABCE98  44 0B F0                        or r14d, eax
00ABCE9B  44 39 A7 D0 00 00 00            cmp dword ptr [rdi + 0xd0], r12d
00ABCEA2  75 3D                           jne 0x140abcee1
00ABCEA4  41 8A C6                        mov al, r14b
00ABCEA7  24 10                           and al, 0x10
00ABCEA9  F6 D8                           neg al
00ABCEAB  1B C9                           sbb ecx, ecx
00ABCEAD  81 E1 E7 03 00 00               and ecx, 0x3e7
00ABCEB3  FF C1                           inc ecx
00ABCEB5  89 8F D0 00 00 00               mov dword ptr [rdi + 0xd0], ecx
00ABCEBB  EB 24                           jmp 0x140abcee1
00ABCEBD  44 85 F0                        test eax, r14d
00ABCEC0  74 1F                           je 0x140abcee1
00ABCEC2  4C 39 A7 20 03 00 00            cmp qword ptr [rdi + 0x320], r12
00ABCEC9  0F 84 4C 02 00 00               je 0x140abd11b
00ABCECF  41 0F BA F6 08                  btr r14d, 8
00ABCED4  BA 08 00 00 00                  mov edx, 8
00ABCED9  48 8B CF                        mov rcx, rdi
00ABCEDC  E8 6F 93 FA FF                  call 0x140a66250
00ABCEE1  48 8B 0D 98 E2 56 FF            mov rcx, qword ptr [rip - 0xa91d68]
00ABCEE8  4C 8D A7 14 01 00 00            lea r12, [rdi + 0x114]
00ABCEEF  49 8B 04 24                     mov rax, qword ptr [r12]
00ABCEF3  48 2B C8                        sub rcx, rax
00ABCEF6  75 0C                           jne 0x140abcf04
00ABCEF8  48 8B 0D 89 E2 56 FF            mov rcx, qword ptr [rip - 0xa91d77]
00ABCEFF  49 2B 4C 24 08                  sub rcx, qword ptr [r12 + 8]
00ABCF04  48 85 C9                        test rcx, rcx
00ABCF07  75 05                           jne 0x140abcf0e
00ABCF09  45 33 C9                        xor r9d, r9d
00ABCF0C  EB 21                           jmp 0x140abcf2f
00ABCF0E  48 8B 0D 0B E1 56 FF            mov rcx, qword ptr [rip - 0xa91ef5]
00ABCF15  48 2B C8                        sub rcx, rax
00ABCF18  75 0C                           jne 0x140abcf26
00ABCF1A  48 8B 0D 07 E1 56 FF            mov rcx, qword ptr [rip - 0xa91ef9]
00ABCF21  49 2B 4C 24 08                  sub rcx, qword ptr [r12 + 8]
00ABCF26  48 85 C9                        test rcx, rcx
00ABCF29  75 12                           jne 0x140abcf3d
00ABCF2B  44 8D 49 01                     lea r9d, [rcx + 1]
00ABCF2F  44 8B 07                        mov r8d, dword ptr [rdi]
00ABCF32  49 8B D5                        mov rdx, r13
00ABCF35  48 8B CE                        mov rcx, rsi
00ABCF38  E8 37 A4 FA FF                  call 0x140a67374
00ABCF3D  48 8B D7                        mov rdx, rdi
00ABCF40  48 8B CE                        mov rcx, rsi
00ABCF43  E8 B0 A6 FA FF                  call 0x140a675f8
00ABCF48  8B D8                           mov ebx, eax
00ABCF4A  85 C0                           test eax, eax
00ABCF4C  0F 88 CE 01 00 00               js 0x140abd120
00ABCF52  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00ABCF56  F7 00 00 00 00 02               test dword ptr [rax], 0x2000000
00ABCF5C  74 4D                           je 0x140abcfab
00ABCF5E  BA 80 00 00 00                  mov edx, 0x80
00ABCF63  48 8B CF                        mov rcx, rdi
00ABCF66  E8 D9 0E FD FF                  call 0x140a8de44
00ABCF6B  8B D8                           mov ebx, eax
00ABCF6D  85 C0                           test eax, eax
00ABCF6F  0F 88 AB 01 00 00               js 0x140abd120
00ABCF75  4C 3B 2D 2C 9B 50 00            cmp r13, qword ptr [rip + 0x509b2c]
00ABCF7C  75 18                           jne 0x140abcf96
00ABCF7E  45 33 C0                        xor r8d, r8d
00ABCF81  48 8B D6                        mov rdx, rsi
00ABCF84  48 8B CF                        mov rcx, rdi
00ABCF87  E8 24 A7 FA FF                  call 0x140a676b0
00ABCF8C  8B D8                           mov ebx, eax
00ABCF8E  85 C0                           test eax, eax
00ABCF90  0F 88 8A 01 00 00               js 0x140abd120
00ABCF96  48 8B D6                        mov rdx, rsi
00ABCF99  48 8B CF                        mov rcx, rdi
00ABCF9C  E8 EF A4 FA FF                  call 0x140a67490
00ABCFA1  8B D8                           mov ebx, eax
00ABCFA3  85 C0                           test eax, eax
00ABCFA5  0F 88 75 01 00 00               js 0x140abd120
00ABCFAB  8B 5E 38                        mov ebx, dword ptr [rsi + 0x38]
00ABCFAE  85 DB                           test ebx, ebx
00ABCFB0  74 29                           je 0x140abcfdb
00ABCFB2  83 7F 04 00                     cmp dword ptr [rdi + 4], 0
00ABCFB6  76 0E                           jbe 0x140abcfc6
00ABCFB8  48 8B CF                        mov rcx, rdi
00ABCFBB  E8 D0 78 FB FF                  call 0x140a74890
00ABCFC0  3B D8                           cmp ebx, eax
00ABCFC2  77 04                           ja 0x140abcfc8
00ABCFC4  EB 07                           jmp 0x140abcfcd
00ABCFC6  33 C0                           xor eax, eax
00ABCFC8  89 46 38                        mov dword ptr [rsi + 0x38], eax
00ABCFCB  8B D8                           mov ebx, eax
00ABCFCD  3B 9F EC 00 00 00               cmp ebx, dword ptr [rdi + 0xec]
00ABCFD3  76 06                           jbe 0x140abcfdb
00ABCFD5  89 9F EC 00 00 00               mov dword ptr [rdi + 0xec], ebx
00ABCFDB  41 0F BA E6 0A                  bt r14d, 0xa
00ABCFE0  72 22                           jb 0x140abd004
00ABCFE2  8B 46 44                        mov eax, dword ptr [rsi + 0x44]
00ABCFE5  85 C0                           test eax, eax
00ABCFE7  74 1B                           je 0x140abd004
00ABCFE9  3B 87 D0 00 00 00               cmp eax, dword ptr [rdi + 0xd0]
00ABCFEF  74 13                           je 0x140abd004
00ABCFF1  BA 04 00 00 00                  mov edx, 4
00ABCFF6  89 87 D0 00 00 00               mov dword ptr [rdi + 0xd0], eax
00ABCFFC  48 8B CF                        mov rcx, rdi
00ABCFFF  E8 4C 92 FA FF                  call 0x140a66250
00ABD004  B8 00 00 08 00                  mov eax, 0x80000
00ABD009  44 85 F8                        test eax, r15d
00ABD00C  74 50                           je 0x140abd05e
00ABD00E  83 BF 2C 01 00 00 01            cmp dword ptr [rdi + 0x12c], 1
00ABD015  75 0A                           jne 0x140abd021
00ABD017  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00ABD01C  E9 FF 00 00 00                  jmp 0x140abd120
00ABD021  F0 81 8F 38 03 00 00 00 08 00 00  lock or dword ptr [rdi + 0x338], 0x800
00ABD02C  44 0B F0                        or r14d, eax
00ABD02F  80 3D A6 A5 48 00 00            cmp byte ptr [rip + 0x48a5a6], 0
00ABD036  75 09                           jne 0x140abd041
00ABD038  80 3D DD D9 34 00 00            cmp byte ptr [rip + 0x34d9dd], 0
00ABD03F  74 09                           je 0x140abd04a
00ABD041  80 3D 6B 8C 49 00 00            cmp byte ptr [rip + 0x498c6b], 0
00ABD048  74 0E                           je 0x140abd058
00ABD04A  48 8B 7D 50                     mov rdi, qword ptr [rbp + 0x50]
00ABD04E  48 8B CF                        mov rcx, rdi
00ABD051  E8 6A F1 CF FF                  call 0x1407bc1c0
00ABD056  EB 10                           jmp 0x140abd068
00ABD058  48 8B 7D 50                     mov rdi, qword ptr [rbp + 0x50]
00ABD05C  EB 0A                           jmp 0x140abd068
00ABD05E  44 85 F0                        test eax, r14d
00ABD061  74 05                           je 0x140abd068
00ABD063  41 0F BA F6 13                  btr r14d, 0x13
00ABD068  45 84 FF                        test r15b, r15b
00ABD06B  79 30                           jns 0x140abd09d
00ABD06D  48 83 65 58 00                  and qword ptr [rbp + 0x58], 0
00ABD072  48 8D 55 58                     lea rdx, [rbp + 0x58]
00ABD076  49 8B CC                        mov rcx, r12
00ABD079  E8 42 34 E0 FF                  call 0x1408c04c0
00ABD07E  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
00ABD082  48 8B CF                        mov rcx, rdi
00ABD085  E8 DA CE FE FF                  call 0x140aa9f64
00ABD08A  48 8D 4D 58                     lea rcx, [rbp + 0x58]
00ABD08E  8B D8                           mov ebx, eax
00ABD090  E8 47 17 F6 FF                  call 0x140a1e7dc
00ABD095  85 DB                           test ebx, ebx
00ABD097  0F 88 83 00 00 00               js 0x140abd120
00ABD09D  44 89 77 0C                     mov dword ptr [rdi + 0xc], r14d
00ABD0A1  8B 46 4C                        mov eax, dword ptr [rsi + 0x4c]
00ABD0A4  85 C0                           test eax, eax
00ABD0A6  74 38                           je 0x140abd0e0
00ABD0A8  83 BF D0 00 00 00 00            cmp dword ptr [rdi + 0xd0], 0
00ABD0AF  77 29                           ja 0x140abd0da
00ABD0B1  41 0F BA E6 0A                  bt r14d, 0xa
00ABD0B6  72 22                           jb 0x140abd0da
00ABD0B8  48 8B CF                        mov rcx, rdi
00ABD0BB  E8 80 E8 92 FF                  call 0x1403eb940
00ABD0C0  8B 8F EC 00 00 00               mov ecx, dword ptr [rdi + 0xec]
00ABD0C6  2B C8                           sub ecx, eax
00ABD0C8  8B 46 4C                        mov eax, dword ptr [rsi + 0x4c]
00ABD0CB  FF C9                           dec ecx
00ABD0CD  3B C1                           cmp eax, ecx
00ABD0CF  7E 05                           jle 0x140abd0d6
00ABD0D1  89 4E 4C                        mov dword ptr [rsi + 0x4c], ecx
00ABD0D4  8B C1                           mov eax, ecx
00ABD0D6  85 C0                           test eax, eax
00ABD0D8  79 06                           jns 0x140abd0e0
00ABD0DA  83 66 4C 00                     and dword ptr [rsi + 0x4c], 0
00ABD0DE  33 C0                           xor eax, eax
00ABD0E0  48 8B D7                        mov rdx, rdi
00ABD0E3  89 87 D4 00 00 00               mov dword ptr [rdi + 0xd4], eax
00ABD0E9  48 8B CE                        mov rcx, rsi
00ABD0EC  E8 9F 1E E0 FF                  call 0x1408bef90
00ABD0F1  48 8B 0D 48 27 44 00            mov rcx, qword ptr [rip + 0x442748]
00ABD0F8  48 8D 15 71 5D 56 FF            lea rdx, [rip - 0xa9a28f]
00ABD0FF  8B D8                           mov ebx, eax
00ABD101  E8 4A 53 8D FF                  call 0x140392450
00ABD106  84 C0                           test al, al
00ABD108  74 16                           je 0x140abd120
00ABD10A  4C 8B C7                        mov r8, rdi
00ABD10D  48 8D 15 5C 5D 56 FF            lea rdx, [rip - 0xa9a2a4]
00ABD114  E8 07 00 F0 FF                  call 0x1409bd120
00ABD119  EB 05                           jmp 0x140abd120
00ABD11B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00ABD120  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00ABD124  E8 D7 36 F0 FF                  call 0x1409c0800
00ABD129  B2 01                           mov dl, 1
00ABD12B  48 8B CF                        mov rcx, rdi
00ABD12E  E8 2D 70 F4 FF                  call 0x140a04160
00ABD133  E8 78 07 7A FF                  call 0x14025d8b0
00ABD138  8B C3                           mov eax, ebx
00ABD13A  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00ABD142  48 83 C4 50                     add rsp, 0x50
00ABD146  41 5F                           pop r15
00ABD148  41 5E                           pop r14
00ABD14A  41 5D                           pop r13
00ABD14C  41 5C                           pop r12
00ABD14E  5F                              pop rdi
00ABD14F  5E                              pop rsi
00ABD150  5D                              pop rbp
00ABD151  C3                              ret
00ABD152  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpUpdateTrace(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int16 v_stack_m56;
    unsigned __int16 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    v_r12 = 0;
    v_stack_p18 = 0;
    v_stack_m56 = 0;
    v_stack_m50 = v_xmm0;
    result = EtwpValidateLoggerInfo(a2, a2, a3, a4);
    if (sign_flag) goto loc_00ABD13A;
    result = EtwpValidateFlagExtension(a2, a2, a3, a4);
    if (sign_flag) goto loc_00ABD13A;
    result = EtwpAcquireLoggerContext(a1, a2, v_stack_p18, a4);
    if (sign_flag) goto loc_00ABD133;
    v_stack_m68 = v_stack_p18 + 12;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18 + 12)))) & (64)) != 0) goto loc_00ABD11B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 64))))) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_00ABD11B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 64))))) & ((unsigned int)((unsigned int)(0xC000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC000ULL)))) goto loc_00ABD11B;
    a1 = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 64)))) & (2)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18 + 12)))) & (2)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00ABD11B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 64))))) & (6));
    if (((unsigned __int8)(result)) == 6) goto loc_00ABD11B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 64))))) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 12)))));
    result = (condition_is_above_or_equal) ? 1 : 0;
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)((a1) & (0xFFFFFFE0ULL));
    a1 = (unsigned int)((a1) + (160));
    if ((*(unsigned __int64 *)(a2 + 136)) == 0) goto loc_00ABCD86;
    result = (unsigned int)((unsigned int)(a1));
    if ((*(unsigned __int16 *)(a2 + 128)) >= = 0) {
        result = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (64));
    }
    result = EtwpCheckLoggerControlAccess((unsigned int)((unsigned int)(result)), v_stack_p18, v_stack_p18, a4);
    if (sign_flag) goto loc_00ABD120;
    if ((*(unsigned __int64 *)(a2 + 136)) == 0) goto loc_00ABCE87;
    if ((*(unsigned __int16 *)(a2 + 128)) <= 0) goto loc_00ABCE87;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18 + 12)))) & (8)) != 0) goto loc_00ABD11B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 64)))) & (8)) != 0) goto loc_00ABD11B;
    if (condition_is_below) goto loc_00ABD11B;
    result = EtwpCaptureString(a2 + 128, v_stack_m50, v_stack_p18, a4);
    if (sign_flag) goto loc_00ABD120;
    if ((*(unsigned __int64 *)(v_stack_p18 + 720)) != 0) {
        a1 = v_stack_p18 + 704;
        result = SeDeleteClientSecurity(a1, v_stack_m50, v_stack_p18, a4);
        *(unsigned __int64 *)(v_stack_p18 + 720) = 0;
    }
    a3 = 0;
    v_stack_m60 = 12;
    v_stack_m5C = 2;
    v_stack_m58 = 257;
    result = SeCreateClientSecurity(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m60, a3, v_stack_p18 + 704);
    if (sign_flag) goto loc_00ABD120;
    v_stack_m48 = 0;
    *(unsigned __int64 *)(v_stack_p18 + 184) = v_xmm0;
    result = EtwpSynchronizeWithLogger(v_stack_p18, 4, a3, v_stack_p18 + 704);
    result = EtwpSynchronizeWithLogger(v_stack_p18, 2, a3, v_stack_p18 + 704);
    if (sign_flag) goto loc_00ABD120;
    if ((*(unsigned int *)(v_stack_p18 + 320)) == 0) goto loc_00ABD120;
    goto loc_00ABCE8E;
loc_00ABCE87:
    if ((*(unsigned int *)(v_stack_p18 + 320)) < 0) goto loc_00ABCEE1;
loc_00ABCE8E:
    if (((256) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 64))))) == 0) goto loc_00ABCEBD;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 12))) | (256));
    if ((*(unsigned int *)(v_stack_p18 + 208)) != 0) goto loc_00ABCEE1;
    result = (unsigned __int8)(((unsigned __int8)(v_r14)) & (16));
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)((v_stack_p18) & (999));
    a1 = (unsigned int)((a1) + 1);
    *(unsigned int *)(v_stack_p18 + 208) = (unsigned int)(a1);
    goto loc_00ABCEE1;
loc_00ABCEBD:
    if ((((unsigned int)(result)) & ((unsigned int)(v_r14))) == 0) goto loc_00ABCEE1;
    if ((*(unsigned __int64 *)(v_stack_p18 + 800)) == 0) goto loc_00ABD11B;
    result = EtwpSynchronizeWithLogger(v_stack_p18, 8, a3, v_stack_p18 + 704);
loc_00ABCEE1:
    a1 = (*(unsigned __int64 *)(v_rip - 11083112)) - (*(unsigned __int64 *)(v_stack_p18 + 276));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rip - 11083127);
        a1 = (a1) - (*(unsigned __int64 *)(v_stack_p18 + 276 + 8));
    }
    if (a1 != 0) goto loc_00ABCF0E;
    a4 = 0;
    goto loc_00ABCF2F;
loc_00ABCF0E:
    a1 = (*(unsigned __int64 *)(v_rip - 11083509)) - (*(unsigned __int64 *)(v_stack_p18 + 276));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rip - 11083513);
        a1 = (a1) - (*(unsigned __int64 *)(v_stack_p18 + 276 + 8));
    }
    if (a1 != 0) goto loc_00ABCF3D;
loc_00ABCF2F:
    result = EtwpUpdatePerProcessTracing(a2, a1, (unsigned int)(*(unsigned int *)(v_stack_p18)), a1 + 1);
loc_00ABCF3D:
    result = EtwpCheckForStackTracingExtension(a2, v_stack_p18, (unsigned int)(*(unsigned int *)(v_stack_p18)), a1 + 1);
    if (sign_flag) goto loc_00ABD120;
    if (((*(unsigned int *)(v_stack_m68)) & (0x2000000ULL)) == 0) goto loc_00ABCFAB;
    result = EtwpCheckSystemTraceAccess(v_stack_p18, 128, (unsigned int)(*(unsigned int *)(v_stack_p18)), a1 + 1);
    if (sign_flag) goto loc_00ABD120;
    if (a1 != (*(unsigned __int64 *)(v_rip + 5282604))) goto loc_00ABCF96;
    a3 = 0;
    result = EtwpCheckForPoolTagFilterExtension(v_stack_p18, a2, a3, a1 + 1);
    if (sign_flag) goto loc_00ABD120;
loc_00ABCF96:
    result = EtwpUpdateLoggerGroupMasks(v_stack_p18, a2, a3, a1 + 1);
    if (sign_flag) goto loc_00ABD120;
loc_00ABCFAB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56))) == 0) goto loc_00ABCFDB;
    if ((*(unsigned int *)(v_stack_p18 + 4)) <= 0) goto loc_00ABCFC6;
    result = EtwpGetSystemMaximumBufferCount(v_stack_p18, a2, a3, a1 + 1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56)))) > ((unsigned int)(result))) goto loc_00ABCFC8;
    goto loc_00ABCFCD;
loc_00ABCFC6:
    result = 0;
loc_00ABCFC8:
    *(unsigned int *)(a2 + 56) = 0;
loc_00ABCFCD:
    if (0 >= = (*(unsigned int *)(v_stack_p18 + 236))) {
        *(unsigned int *)(v_stack_p18 + 236) = 0;
    }
    if (0 < (*(unsigned int *)(v_stack_p18 + 236))) goto loc_00ABD004;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68))) == 0) goto loc_00ABD004;
    result = (unsigned int)(*(unsigned int *)(a2 + 68));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)))) != (*(unsigned int *)(v_stack_p18 + 208))) {
        a2 = 4;
        *(unsigned int *)(v_stack_p18 + 208) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 68)));
        a1 = v_stack_p18;
        result = EtwpSynchronizeWithLogger(a1, a2, a3, a1 + 1);
    }
    if ((((unsigned int)((unsigned int)(0x80000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 64))))) == 0) goto loc_00ABD05E;
    if ((*(unsigned int *)(v_stack_p18 + 300)) != 1) goto loc_00ABD021;
    goto loc_00ABD120;
loc_00ABD021:
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)((unsigned int)(0x80000ULL))));
    if ((*(unsigned __int8 *)(v_rip + 4760998)) != 0) goto loc_00ABD041;
    if ((*(unsigned __int8 *)(v_rip + 3463645)) == 0) goto loc_00ABD04A;
loc_00ABD041:
    if ((*(unsigned __int8 *)(v_rip + 4820075)) == 0) goto loc_00ABD058;
loc_00ABD04A:
    result = EtwpSendDbgId(v_stack_p18, a2, a3, a1 + 1);
    goto loc_00ABD068;
loc_00ABD058:
    goto loc_00ABD068;
loc_00ABD05E:
    if ((((unsigned int)(result)) & ((unsigned int)(v_r14))) != 0) {
    }
    if (!sign_flag) goto loc_00ABD09D;
    result = EtwpGetSecurityDescriptorByGuid(v_stack_p18 + 276, v_stack_p20, a3, a1 + 1);
    result = EtwpUpdateLoggerSecurityDescriptor(v_stack_p18, v_stack_p20, a3, a1 + 1);
    result = EtwpFreeSecurityDescriptor(v_stack_p20, v_stack_p20, a3, a1 + 1);
    if (sign_flag) goto loc_00ABD120;
loc_00ABD09D:
    *(unsigned int *)(v_stack_p18 + 12) = (unsigned int)(v_r14);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 76))) == 0) goto loc_00ABD0E0;
    if ((*(unsigned int *)(v_stack_p18 + 208)) > 0) goto loc_00ABD0DA;
    if ((*(unsigned int *)(v_stack_p18 + 208)) < 0) goto loc_00ABD0DA;
    result = EtwpQueryUsedProcessorCount(v_stack_p18, v_stack_p20, a3, a1 + 1);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 236))) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) - 1);
    result = (unsigned int)(*(unsigned int *)(a2 + 76));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 76)))) >= = ((unsigned int)(a1))) {
        *(unsigned int *)(a2 + 76) = (unsigned int)(a1);
        result = (unsigned int)(a1);
    }
    if (sign_flag) {
        result = 0;
    }
    *(unsigned int *)(v_stack_p18 + 212) = 0;
    result = EtwpGetLoggerInfoFromContext(a2, v_stack_p18, a3, a1 + 1);
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4466504), v_rip - 11117199, a3, a1 + 1);
    if ((unsigned __int8)(result) == 0) goto loc_00ABD120;
    result = EtwpEventWriteTemplateSession(*(unsigned __int64 *)(v_rip + 4466504), v_rip - 11117220, v_stack_p18, a1 + 1);
    goto loc_00ABD120;
loc_00ABD11B:
loc_00ABD120:
    result = RtlFreeAnsiString(v_stack_m50, v_rip - 11117220, v_stack_p18, a1 + 1);
    result = EtwpReleaseLoggerContext(v_stack_p18, 1, v_stack_p18, a1 + 1);
loc_00ABD133:
    result = KeLeaveCriticalRegion(v_stack_p18, 1, v_stack_p18, a1 + 1);
loc_00ABD13A:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t EtwpUpdateTrace(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint16_t v_stack_m56;
    uint16_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    local_r12 = 0;
    v_stack_p18 = 0;
    v_stack_m56 = 0;
    v_stack_m50 = v_xmm0;
    result = EtwpValidateLoggerInfo(Arg2, Arg2, a3, a4);
    if (sign_flag) goto loc_00ABD13A;
    result = EtwpValidateFlagExtension(Arg2, Arg2, a3, a4);
    if (sign_flag) goto loc_00ABD13A;
    result = EtwpAcquireLoggerContext(Arg1, Arg2, v_stack_p18, a4);
    if (sign_flag) goto loc_00ABD133;
    v_stack_m68 = v_stack_p18 + 12;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xC)))) & (64)) != 0) goto loc_00ABD11B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40))))) & (3));
    if (((uint8_t)(result)) == 3) goto loc_00ABD11B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40))))) & ((uint32_t)((uint32_t)(0xC000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC000ULL)))) goto loc_00ABD11B;
    Arg1 = ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40)))) & (2)) != 0) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xC)))) & (2)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00ABD11B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40))))) & (6));
    if (((uint8_t)(result)) == 6) goto loc_00ABD11B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40))))) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xC)))));
    result = (condition_is_above_or_equal) ? 1 : 0;
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFE0ULL));
    Arg1 = (uint32_t)((Arg1) + (160));
    if ((*(uint64_t *)(arg2 + 0x88)) == 0) goto loc_00ABCD86;
    result = (uint32_t)((uint32_t)(Arg1));
    if ((*(uint16_t *)(arg2 + 0x80)) >= = 0) {
        result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (64));
    }
    result = EtwpCheckLoggerControlAccess((uint32_t)((uint32_t)(result)), v_stack_p18, v_stack_p18, a4);
    if (sign_flag) goto loc_00ABD120;
    if ((*(uint64_t *)(arg2 + 0x88)) == 0) goto loc_00ABCE87;
    if ((*(uint16_t *)(arg2 + 0x80)) <= 0) goto loc_00ABCE87;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xC)))) & (8)) != 0) goto loc_00ABD11B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40)))) & (8)) != 0) goto loc_00ABD11B;
    if (condition_is_below) goto loc_00ABD11B;
    result = EtwpCaptureString(Arg2 + 128, v_stack_m50, v_stack_p18, a4);
    if (sign_flag) goto loc_00ABD120;
    if ((*(uint64_t *)(v_stack_p18 + 0x2D0)) != 0) {
        Arg1 = v_stack_p18 + 704;
        result = SeDeleteClientSecurity(Arg1, v_stack_m50, v_stack_p18, a4);
        *(uint64_t *)(v_stack_p18 + 0x2D0) = 0;
    }
    a3 = 0;
    v_stack_m60 = 12;
    v_stack_m5C = 2;
    v_stack_m58 = 257;
    result = SeCreateClientSecurity(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m60, a3, v_stack_p18 + 704);
    if (sign_flag) goto loc_00ABD120;
    v_stack_m48 = 0;
    *(uint64_t *)(v_stack_p18 + 0xB8) = v_xmm0;
    result = EtwpSynchronizeWithLogger(v_stack_p18, 4, a3, v_stack_p18 + 704);
    result = EtwpSynchronizeWithLogger(v_stack_p18, 2, a3, v_stack_p18 + 704);
    if (sign_flag) goto loc_00ABD120;
    if ((*(uint32_t *)(v_stack_p18 + 0x140)) == 0) goto loc_00ABD120;
    goto loc_00ABCE8E;
loc_00ABCE87:
    if ((*(uint32_t *)(v_stack_p18 + 0x140)) < 0) goto loc_00ABCEE1;
loc_00ABCE8E:
    if (((256) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40))))) == 0) goto loc_00ABCEBD;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xC))) | (256));
    if ((*(uint32_t *)(v_stack_p18 + 0xD0)) != 0) goto loc_00ABCEE1;
    result = (uint8_t)(((uint8_t)(local_r14)) & (16));
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)((v_stack_p18) & (999));
    Arg1 = (uint32_t)((Arg1) + 1);
    *(uint32_t *)(v_stack_p18 + 0xD0) = (uint32_t)(Arg1);
    goto loc_00ABCEE1;
loc_00ABCEBD:
    if ((((uint32_t)(result)) & ((uint32_t)(local_r14))) == 0) goto loc_00ABCEE1;
    if ((*(uint64_t *)(v_stack_p18 + 0x320)) == 0) goto loc_00ABD11B;
    result = EtwpSynchronizeWithLogger(v_stack_p18, 8, a3, v_stack_p18 + 704);
loc_00ABCEE1:
    Arg1 = (*(uint64_t *)(v_rip - 0xA91D68)) - (*(uint64_t *)(v_stack_p18 + 0x114));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(v_rip - 0xA91D77);
        Arg1 = (Arg1) - (*(uint64_t *)(v_stack_p18 + 0x114 + 0x8));
    }
    if (Arg1 != 0) goto loc_00ABCF0E;
    a4 = 0;
    goto loc_00ABCF2F;
loc_00ABCF0E:
    Arg1 = (*(uint64_t *)(v_rip - 0xA91EF5)) - (*(uint64_t *)(v_stack_p18 + 0x114));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(v_rip - 0xA91EF9);
        Arg1 = (Arg1) - (*(uint64_t *)(v_stack_p18 + 0x114 + 0x8));
    }
    if (Arg1 != 0) goto loc_00ABCF3D;
loc_00ABCF2F:
    result = EtwpUpdatePerProcessTracing(Arg2, Arg1, (uint32_t)(*(uint32_t *)(v_stack_p18)), Arg1 + 1);
loc_00ABCF3D:
    result = EtwpCheckForStackTracingExtension(Arg2, v_stack_p18, (uint32_t)(*(uint32_t *)(v_stack_p18)), Arg1 + 1);
    if (sign_flag) goto loc_00ABD120;
    if (((*(uint32_t *)(v_stack_m68)) & (0x2000000ULL)) == 0) goto loc_00ABCFAB;
    result = EtwpCheckSystemTraceAccess(v_stack_p18, 128, (uint32_t)(*(uint32_t *)(v_stack_p18)), Arg1 + 1);
    if (sign_flag) goto loc_00ABD120;
    if (Arg1 != (*(uint64_t *)(v_rip + 0x509B2C))) goto loc_00ABCF96;
    a3 = 0;
    result = EtwpCheckForPoolTagFilterExtension(v_stack_p18, Arg2, a3, Arg1 + 1);
    if (sign_flag) goto loc_00ABD120;
loc_00ABCF96:
    result = EtwpUpdateLoggerGroupMasks(v_stack_p18, Arg2, a3, Arg1 + 1);
    if (sign_flag) goto loc_00ABD120;
loc_00ABCFAB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x38))) == 0) goto loc_00ABCFDB;
    if ((*(uint32_t *)(v_stack_p18 + 0x4)) <= 0) goto loc_00ABCFC6;
    result = EtwpGetSystemMaximumBufferCount(v_stack_p18, Arg2, a3, Arg1 + 1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x38)))) > ((uint32_t)(result))) goto loc_00ABCFC8;
    goto loc_00ABCFCD;
loc_00ABCFC6:
    result = 0;
loc_00ABCFC8:
    *(uint32_t *)(arg2 + 0x38) = 0;
loc_00ABCFCD:
    if (0 >= = (*(uint32_t *)(v_stack_p18 + 0xEC))) {
        *(uint32_t *)(v_stack_p18 + 0xEC) = 0;
    }
    if (0 < (*(uint32_t *)(v_stack_p18 + 0xEC))) goto loc_00ABD004;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44))) == 0) goto loc_00ABD004;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x44));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)))) != (*(uint32_t *)(v_stack_p18 + 0xD0))) {
        Arg2 = 4;
        *(uint32_t *)(v_stack_p18 + 0xD0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x44)));
        Arg1 = v_stack_p18;
        result = EtwpSynchronizeWithLogger(Arg1, Arg2, a3, Arg1 + 1);
    }
    if ((((uint32_t)((uint32_t)(0x80000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x40))))) == 0) goto loc_00ABD05E;
    if ((*(uint32_t *)(v_stack_p18 + 0x12C)) != 1) goto loc_00ABD021;
    goto loc_00ABD120;
loc_00ABD021:
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)((uint32_t)(0x80000ULL))));
    if ((*(uint8_t *)(v_rip + 0x48A5A6)) != 0) goto loc_00ABD041;
    if ((*(uint8_t *)(v_rip + 0x34D9DD)) == 0) goto loc_00ABD04A;
loc_00ABD041:
    if ((*(uint8_t *)(v_rip + 0x498C6B)) == 0) goto loc_00ABD058;
loc_00ABD04A:
    result = EtwpSendDbgId(v_stack_p18, Arg2, a3, Arg1 + 1);
    goto loc_00ABD068;
loc_00ABD058:
    goto loc_00ABD068;
loc_00ABD05E:
    if ((((uint32_t)(result)) & ((uint32_t)(local_r14))) != 0) {
    }
    if (!sign_flag) goto loc_00ABD09D;
    result = EtwpGetSecurityDescriptorByGuid(v_stack_p18 + 276, v_stack_p20, a3, Arg1 + 1);
    result = EtwpUpdateLoggerSecurityDescriptor(v_stack_p18, v_stack_p20, a3, Arg1 + 1);
    result = EtwpFreeSecurityDescriptor(v_stack_p20, v_stack_p20, a3, Arg1 + 1);
    if (sign_flag) goto loc_00ABD120;
loc_00ABD09D:
    *(uint32_t *)(v_stack_p18 + 0xC) = (uint32_t)(local_r14);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4C))) == 0) goto loc_00ABD0E0;
    if ((*(uint32_t *)(v_stack_p18 + 0xD0)) > 0) goto loc_00ABD0DA;
    if ((*(uint32_t *)(v_stack_p18 + 0xD0)) < 0) goto loc_00ABD0DA;
    result = EtwpQueryUsedProcessorCount(v_stack_p18, v_stack_p20, a3, Arg1 + 1);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xEC))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) - 1);
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x4C));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4C)))) >= = ((uint32_t)(Arg1))) {
        *(uint32_t *)(arg2 + 0x4C) = (uint32_t)(Arg1);
        result = (uint32_t)(Arg1);
    }
    if (sign_flag) {
        result = 0;
    }
    *(uint32_t *)(v_stack_p18 + 0xD4) = 0;
    result = EtwpGetLoggerInfoFromContext(Arg2, v_stack_p18, a3, Arg1 + 1);
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x442748), v_rip - 11117199, a3, Arg1 + 1);
    if ((uint8_t)(result) == 0) goto loc_00ABD120;
    result = EtwpEventWriteTemplateSession(*(uint64_t *)(v_rip + 0x442748), v_rip - 11117220, v_stack_p18, Arg1 + 1);
    goto loc_00ABD120;
loc_00ABD11B:
loc_00ABD120:
    result = RtlFreeAnsiString(v_stack_m50, v_rip - 11117220, v_stack_p18, Arg1 + 1);
    result = EtwpReleaseLoggerContext(v_stack_p18, 1, v_stack_p18, Arg1 + 1);
loc_00ABD133:
    result = KeLeaveCriticalRegion(v_stack_p18, 1, v_stack_p18, Arg1 + 1);
loc_00ABD13A:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x38` | `32` | `R` |
| `Arg2` | `+ 0x38` | `32` | `W` |
| `Arg2` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x44` | `32` | `R` |
| `Arg2` | `+ 0x4C` | `32` | `R` |
| `Arg2` | `+ 0x4C` | `32` | `R/W` |
| `Arg2` | `+ 0x4C` | `32` | `W` |
| `Arg2` | `+ 0x80` | `16` | `R` |
| `Arg2` | `+ 0x80` | `64` | `R` |
| `Arg2` | `+ 0x88` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABCC7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
