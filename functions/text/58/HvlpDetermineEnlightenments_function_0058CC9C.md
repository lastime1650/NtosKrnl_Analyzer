# HvlpDetermineEnlightenments

- RVA: `0x0058CC9C`–`0x0058D1B1` (길이 `1,301` bytes)
- VA: `0x000000014058CC9C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C69F4`
- 디코드: `338`개 명령, `1,301/1,301` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x0058CD01` → [HviGetEnlightenmentInformation](../66/HviGetEnlightenmentInformation_function_006665E4.md) (function, `0x006665E4`)
- `0x0058CD11` → [HviGetHypervisorFeatures](../66/HviGetHypervisorFeatures_function_00666630.md) (function, `0x00666630`)
- `0x0058CD1A` → [HviGetHypervisorFeatures](../66/HviGetHypervisorFeatures_function_00666630.md) (function, `0x00666630`)
- `0x0058CD23` → [HviGetHardwareFeatures](../4A/HviGetHardwareFeatures_function_004ADBC0.md) (function, `0x004ADBC0`)
- `0x0058CE92` → [HvlpSetRegister64](../4D/HvlpSetRegister64_function_004DDA70.md) (function, `0x004DDA70`)
- `0x0058CEA0` → [HvlpGetRegister64](../37/HvlpGetRegister64_function_00379050.md) (function, `0x00379050`)
- `0x0058CEC4` → [HvlpSetRegister64](../4D/HvlpSetRegister64_function_004DDA70.md) (function, `0x004DDA70`)
- `0x0058CF0A` → [HvlpGetRegister128](HvlpGetRegister128_function_0058CA30.md) (function, `0x0058CA30`)
- `0x0058CF7F` → [HvlpQueryHypervisorSchedulerType](HvlpQueryHypervisorSchedulerType_function_00586FB4.md) (function, `0x00586FB4`)
- `0x0058D014` → [HvlpAcquireHypercallPage](../47/HvlpAcquireHypercallPage_function_00471410.md) (function, `0x00471410`)
- `0x0058D025` → [HvcallInitiateHypercall](../31/HvcallInitiateHypercall_function_00313630.md) (function, `0x00313630`)
- `0x0058D02E` → [HvlpReleaseHypercallPage](../31/HvlpReleaseHypercallPage_function_00313480.md) (function, `0x00313480`)
- `0x0058D099` → [VslGetNestedPageProtectionFlags](../2F/VslGetNestedPageProtectionFlags_function_002F2164.md) (function, `0x002F2164`)
- `0x0058D102` → [HvlpQueryExtendedCapabilities](HvlpQueryExtendedCapabilities_function_0058D2C8.md) (function, `0x0058D2C8`)
- `0x0058D18E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HvlPhase0Initialize](../../page/71/HvlPhase0Initialize_function_00717AC8.md) at `0x00717B33`

### Static image references
- `0x0058CCBB` → RVA `0x00E0A740` (`.data`; read)
- `0x0058CCF3` → RVA `0x00FC5066` (`ALMOSTRO`; write)
- `0x0058CD7C` → RVA `0x00FC6A90` (`ALMOSTRO`; read/write)
- `0x0058CE79` → RVA `0x00FC52AC` (`ALMOSTRO`; write)
- `0x0058CEF3` → RVA `0x00FC6A90` (`ALMOSTRO`; read)
- `0x0058CF51` → RVA `0x00FC6AD8` (`ALMOSTRO`; read/write)
- `0x0058CF78` → RVA `0x00FC6BEA` (`ALMOSTRO`; write)
- `0x0058CF8D` → RVA `0x00FC6AD8` (`ALMOSTRO`; read)
- `0x0058CFA1` → RVA `0x00FC6AD8` (`ALMOSTRO`; write)
- `0x0058D036` → RVA `0x00FC6F80` (`ALMOSTRO`; write)
- `0x0058D0BB` → RVA `0x00FC6A90` (`ALMOSTRO`; write)
- `0x0058D15E` → RVA `0x00FC6FFC` (`ALMOSTRO`; read)
- `0x0058D16D` → RVA `0x00588020` (`HvlGetEnlightenmentInfo`; read)
- `0x0058D174` → RVA `0x00E00970` (`.data`; write)
- `0x0058D17B` → RVA `0x00FC6C98` (`ALMOSTRO`; write)
- `0x0058D181` → RVA `0x00FC6AB8` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058CC9C  48 8B C4                        mov rax, rsp
0058CC9F  48 89 58 08                     mov qword ptr [rax + 8], rbx
0058CCA3  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0058CCA7  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0058CCAB  55                              push rbp
0058CCAC  41 56                           push r14
0058CCAE  41 57                           push r15
0058CCB0  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0058CCB4  48 81 EC B0 00 00 00            sub rsp, 0xb0
0058CCBB  48 8B 05 7E DA 87 00            mov rax, qword ptr [rip + 0x87da7e]
0058CCC2  48 33 C4                        xor rax, rsp
0058CCC5  48 89 45 3F                     mov qword ptr [rbp + 0x3f], rax
0058CCC9  83 65 DF 00                     and dword ptr [rbp - 0x21], 0
0058CCCD  48 8D 4D DF                     lea rcx, [rbp - 0x21]
0058CCD1  48 83 65 B7 00                  and qword ptr [rbp - 0x49], 0
0058CCD6  0F 57 C0                        xorps xmm0, xmm0
0058CCD9  33 C0                           xor eax, eax
0058CCDB  0F 57 C9                        xorps xmm1, xmm1
0058CCDE  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
0058CCE2  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0058CCE6  33 FF                           xor edi, edi
0058CCE8  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
0058CCEC  89 45 D7                        mov dword ptr [rbp - 0x29], eax
0058CCEF  0F 11 4D 1F                     movups xmmword ptr [rbp + 0x1f], xmm1
0058CCF3  88 05 6D 83 A3 00               mov byte ptr [rip + 0xa3836d], al
0058CCF9  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
0058CCFD  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
0058CD01  E8 DE 98 0D 00                  call 0x1406665e4
0058CD06  0F 57 C0                        xorps xmm0, xmm0
0058CD09  48 8D 4D 0F                     lea rcx, [rbp + 0xf]
0058CD0D  0F 11 45 0F                     movups xmmword ptr [rbp + 0xf], xmm0
0058CD11  E8 1A 99 0D 00                  call 0x140666630
0058CD16  48 8D 4D 1F                     lea rcx, [rbp + 0x1f]
0058CD1A  E8 11 99 0D 00                  call 0x140666630
0058CD1F  48 8D 4D FF                     lea rcx, [rbp - 1]
0058CD23  E8 98 0E F2 FF                  call 0x1404adbc0
0058CD28  8B 75 DF                        mov esi, dword ptr [rbp - 0x21]
0058CD2B  44 8D 4F 01                     lea r9d, [rdi + 1]
0058CD2F  41 84 F1                        test r9b, sil
0058CD32  74 07                           je 0x14058cd3b
0058CD34  BF 07 00 80 00                  mov edi, 0x800007
0058CD39  EB 38                           jmp 0x14058cd73
0058CD3B  40 F6 C6 02                     test sil, 2
0058CD3F  74 07                           je 0x14058cd48
0058CD41  BF 06 00 80 00                  mov edi, 0x800006
0058CD46  EB 2B                           jmp 0x14058cd73
0058CD48  40 F6 C6 04                     test sil, 4
0058CD4C  74 25                           je 0x14058cd73
0058CD4E  0F BA E6 11                     bt esi, 0x11
0058CD52  72 1A                           jb 0x14058cd6e
0058CD54  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0058CD5D  BF 04 00 80 00                  mov edi, 0x800004
0058CD62  8B 75 DF                        mov esi, dword ptr [rbp - 0x21]
0058CD65  80 B8 8D 00 00 00 02            cmp byte ptr [rax + 0x8d], 2
0058CD6C  75 05                           jne 0x14058cd73
0058CD6E  BF 04 00 00 00                  mov edi, 4
0058CD73  48 8B 5D 0F                     mov rbx, qword ptr [rbp + 0xf]
0058CD77  F6 C3 10                        test bl, 0x10
0058CD7A  74 08                           je 0x14058cd84
0058CD7C  0F BA 2D 0C 9D A3 00 13         bts dword ptr [rip + 0xa39d0c], 0x13
0058CD84  40 F6 C6 08                     test sil, 8
0058CD88  74 0A                           je 0x14058cd94
0058CD8A  83 CF 10                        or edi, 0x10
0058CD8D  44 09 0D FC 9C A3 00            or dword ptr [rip + 0xa39cfc], r9d
0058CD94  41 BB 00 02 00 00               mov r11d, 0x200
0058CD9A  41 85 F3                        test r11d, esi
0058CD9D  74 0B                           je 0x14058cdaa
0058CD9F  0F BA EF 0C                     bts edi, 0xc
0058CDA3  83 0D E6 9C A3 00 10            or dword ptr [rip + 0xa39ce6], 0x10
0058CDAA  44 8B 7D 2B                     mov r15d, dword ptr [rbp + 0x2b]
0058CDAE  41 B8 00 00 10 00               mov r8d, 0x100000
0058CDB4  41 0F BA E7 12                  bt r15d, 0x12
0058CDB9  73 22                           jae 0x14058cddd
0058CDBB  B9 01 00 00 40                  mov ecx, 0x40000001
0058CDC0  0F 32                           rdmsr
0058CDC2  48 C1 E2 20                     shl rdx, 0x20
0058CDC6  48 0B C2                        or rax, rdx
0058CDC9  A8 02                           test al, 2
0058CDCB  75 0D                           jne 0x14058cdda
0058CDCD  48 83 C8 02                     or rax, 2
0058CDD1  48 8B D0                        mov rdx, rax
0058CDD4  48 C1 EA 20                     shr rdx, 0x20
0058CDD8  0F 30                           wrmsr
0058CDDA  41 0B F8                        or edi, r8d
0058CDDD  0F BA E6 12                     bt esi, 0x12
0058CDE1  73 08                           jae 0x14058cdeb
0058CDE3  0F BA 2D A5 9C A3 00 16         bts dword ptr [rip + 0xa39ca5], 0x16
0058CDEB  41 BA 00 00 80 00               mov r10d, 0x800000
0058CDF1  0F BA E6 10                     bt esi, 0x10
0058CDF5  73 07                           jae 0x14058cdfe
0058CDF7  44 09 15 92 9C A3 00            or dword ptr [rip + 0xa39c92], r10d
0058CDFE  8B D7                           mov edx, edi
0058CE00  45 8B F7                        mov r14d, r15d
0058CE03  0F BA EA 1D                     bts edx, 0x1d
0058CE07  41 85 F0                        test r8d, esi
0058CE0A  0F 44 D7                        cmove edx, edi
0058CE0D  41 C1 EE 04                     shr r14d, 4
0058CE11  8B CA                           mov ecx, edx
0058CE13  BF 80 00 00 00                  mov edi, 0x80
0058CE18  0B CF                           or ecx, edi
0058CE1A  45 23 F1                        and r14d, r9d
0058CE1D  0F 44 CA                        cmove ecx, edx
0058CE20  44 8B C1                        mov r8d, ecx
0058CE23  41 0F BA E8 1E                  bts r8d, 0x1e
0058CE28  41 85 F2                        test r10d, esi
0058CE2B  44 0F 44 C1                     cmove r8d, ecx
0058CE2F  0F BA E6 0B                     bt esi, 0xb
0058CE33  73 06                           jae 0x14058ce3b
0058CE35  09 3D 55 9C A3 00               or dword ptr [rip + 0xa39c55], edi
0058CE3B  41 8B D0                        mov edx, r8d
0058CE3E  83 CA 20                        or edx, 0x20
0058CE41  40 F6 C6 20                     test sil, 0x20
0058CE45  41 0F 44 D0                     cmove edx, r8d
0058CE49  8B CA                           mov ecx, edx
0058CE4B  0F BA E9 0E                     bts ecx, 0xe
0058CE4F  0F BA E6 0A                     bt esi, 0xa
0058CE53  0F 43 CA                        cmovae ecx, edx
0058CE56  8B 55 E3                        mov edx, dword ptr [rbp - 0x1d]
0058CE59  8B F9                           mov edi, ecx
0058CE5B  41 0B FB                        or edi, r11d
0058CE5E  41 F6 C7 20                     test r15b, 0x20
0058CE62  0F 44 F9                        cmove edi, ecx
0058CE65  85 D2                           test edx, edx
0058CE67  7E 16                           jle 0x14058ce7f
0058CE69  0F BD CA                        bsr ecx, edx
0058CE6C  41 8B C1                        mov eax, r9d
0058CE6F  83 CF 40                        or edi, 0x40
0058CE72  D3 E0                           shl eax, cl
0058CE74  41 2B C1                        sub eax, r9d
0058CE77  0B C2                           or eax, edx
0058CE79  89 05 2D 84 A3 00               mov dword ptr [rip + 0xa3842d], eax
0058CE7F  48 0F BA E3 2C                  bt rbx, 0x2c
0058CE84  73 4A                           jae 0x14058ced0
0058CE86  49 8B D1                        mov rdx, r9
0058CE89  4C 89 4D DF                     mov qword ptr [rbp - 0x21], r9
0058CE8D  B9 07 00 09 00                  mov ecx, 0x90007
0058CE92  E8 D9 0B F5 FF                  call 0x1404dda70
0058CE97  48 8D 55 DF                     lea rdx, [rbp - 0x21]
0058CE9B  B9 07 00 09 00                  mov ecx, 0x90007
0058CEA0  E8 AB C1 DE FF                  call 0x140379050
0058CEA5  48 B8 00 00 00 00 00 00 00 40   movabs rax, 0x4000000000000000
0058CEAF  48 85 45 DF                     test qword ptr [rbp - 0x21], rax
0058CEB3  74 1B                           je 0x14058ced0
0058CEB5  48 BA 01 00 00 00 00 00 00 80   movabs rdx, 0x8000000000000001
0058CEBF  B9 07 00 09 00                  mov ecx, 0x90007
0058CEC4  E8 A7 0B F5 FF                  call 0x1404dda70
0058CEC9  83 0D C0 9B A3 00 02            or dword ptr [rip + 0xa39bc0], 2
0058CED0  48 0F BA E3 20                  bt rbx, 0x20
0058CED5  73 08                           jae 0x14058cedf
0058CED7  0F BA 2D B1 9B A3 00 19         bts dword ptr [rip + 0xa39bb1], 0x19
0058CEDF  41 0F BA E7 1C                  bt r15d, 0x1c
0058CEE4  73 0D                           jae 0x14058cef3
0058CEE6  0F BA EF 1A                     bts edi, 0x1a
0058CEEA  45 85 F6                        test r14d, r14d
0058CEED  75 04                           jne 0x14058cef3
0058CEEF  0F BA F7 1A                     btr edi, 0x1a
0058CEF3  8B 05 97 9B A3 00               mov eax, dword ptr [rip + 0xa39b97]
0058CEF9  A8 02                           test al, 2
0058CEFB  0F 84 C6 00 00 00               je 0x14058cfc7
0058CF01  48 8D 55 EF                     lea rdx, [rbp - 0x11]
0058CF05  B9 04 02 00 00                  mov ecx, 0x204
0058CF0A  E8 21 FB FF FF                  call 0x14058ca30
0058CF0F  44 8B 45 F3                     mov r8d, dword ptr [rbp - 0xd]
0058CF13  8B CF                           mov ecx, edi
0058CF15  44 8B 75 EF                     mov r14d, dword ptr [rbp - 0x11]
0058CF19  0F BA E9 0A                     bts ecx, 0xa
0058CF1D  41 F6 C0 01                     test r8b, 1
0058CF21  0F 44 CF                        cmove ecx, edi
0058CF24  8B D1                           mov edx, ecx
0058CF26  0F BA EA 1C                     bts edx, 0x1c
0058CF2A  41 F6 C0 08                     test r8b, 8
0058CF2E  0F 44 D1                        cmove edx, ecx
0058CF31  8B CA                           mov ecx, edx
0058CF33  0F BA E9 11                     bts ecx, 0x11
0058CF37  41 F6 C0 02                     test r8b, 2
0058CF3B  0F 44 CA                        cmove ecx, edx
0058CF3E  8B F9                           mov edi, ecx
0058CF40  0F BA EF 12                     bts edi, 0x12
0058CF44  41 F6 C0 04                     test r8b, 4
0058CF48  0F 44 F9                        cmove edi, ecx
0058CF4B  41 F6 C6 01                     test r14b, 1
0058CF4F  74 07                           je 0x14058cf58
0058CF51  83 0D 80 9B A3 00 20            or dword ptr [rip + 0xa39b80], 0x20
0058CF58  41 F6 C6 02                     test r14b, 2
0058CF5C  74 07                           je 0x14058cf65
0058CF5E  83 0D 73 9B A3 00 40            or dword ptr [rip + 0xa39b73], 0x40
0058CF65  45 85 F6                        test r14d, r14d
0058CF68  79 23                           jns 0x14058cf8d
0058CF6A  81 0D 64 9B A3 00 87 01 00 00   or dword ptr [rip + 0xa39b64], 0x187
0058CF74  0F BA EF 10                     bts edi, 0x10
0058CF78  C6 05 6B 9C A3 00 01            mov byte ptr [rip + 0xa39c6b], 1
0058CF7F  E8 30 A0 FF FF                  call 0x140586fb4
0058CF84  83 F8 04                        cmp eax, 4
0058CF87  75 04                           jne 0x14058cf8d
0058CF89  0F BA EF 12                     bts edi, 0x12
0058CF8D  8B 05 45 9B A3 00               mov eax, dword ptr [rip + 0xa39b45]
0058CF93  A8 01                           test al, 1
0058CF95  74 10                           je 0x14058cfa7
0058CF97  41 F6 C6 04                     test r14b, 4
0058CF9B  74 0A                           je 0x14058cfa7
0058CF9D  0F BA E8 09                     bts eax, 9
0058CFA1  89 05 31 9B A3 00               mov dword ptr [rip + 0xa39b31], eax
0058CFA7  48 0F BA E3 28                  bt rbx, 0x28
0058CFAC  73 09                           jae 0x14058cfb7
0058CFAE  83 C8 10                        or eax, 0x10
0058CFB1  89 05 21 9B A3 00               mov dword ptr [rip + 0xa39b21], eax
0058CFB7  0F BA E6 0C                     bt esi, 0xc
0058CFBB  73 0A                           jae 0x14058cfc7
0058CFBD  0F BA E8 0A                     bts eax, 0xa
0058CFC1  89 05 11 9B A3 00               mov dword ptr [rip + 0xa39b11], eax
0058CFC7  8B CF                           mov ecx, edi
0058CFC9  0F BA E9 0B                     bts ecx, 0xb
0058CFCD  41 F6 C7 80                     test r15b, 0x80
0058CFD1  0F 44 CF                        cmove ecx, edi
0058CFD4  41 F6 C7 08                     test r15b, 8
0058CFD8  75 07                           jne 0x14058cfe1
0058CFDA  83 0D AF 9A A3 00 04            or dword ptr [rip + 0xa39aaf], 4
0058CFE1  BA 02 02 00 00                  mov edx, 0x202
0058CFE6  48 8B C3                        mov rax, rbx
0058CFE9  48 23 C2                        and rax, rdx
0058CFEC  44 8B F1                        mov r14d, ecx
0058CFEF  41 0F BA EE 08                  bts r14d, 8
0058CFF4  48 3B C2                        cmp rax, rdx
0058CFF7  44 0F 45 F1                     cmovne r14d, ecx
0058CFFB  48 0F BA E3 21                  bt rbx, 0x21
0058D000  73 3B                           jae 0x14058d03d
0058D002  41 B9 08 00 00 00               mov r9d, 8
0058D008  4C 8D 45 2F                     lea r8, [rbp + 0x2f]
0058D00C  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0058D010  41 8D 51 FA                     lea edx, [r9 - 6]
0058D014  E8 F7 43 EE FF                  call 0x140471410
0058D019  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
0058D01D  33 D2                           xor edx, edx
0058D01F  48 8B F8                        mov rdi, rax
0058D022  8D 4A 46                        lea ecx, [rdx + 0x46]
0058D025  E8 06 66 D8 FF                  call 0x140313630
0058D02A  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0058D02E  E8 4D 64 D8 FF                  call 0x140313480
0058D033  48 8B 07                        mov rax, qword ptr [rdi]
0058D036  48 89 05 43 9F A3 00            mov qword ptr [rip + 0xa39f43], rax
0058D03D  41 8B CE                        mov ecx, r14d
0058D040  BA 00 20 00 00                  mov edx, 0x2000
0058D045  0B CA                           or ecx, edx
0058D047  41 0F BA E7 0A                  bt r15d, 0xa
0058D04C  41 0F 43 CE                     cmovae ecx, r14d
0058D050  F6 C3 04                        test bl, 4
0058D053  74 07                           je 0x14058d05c
0058D055  83 0D 34 9A A3 00 20            or dword ptr [rip + 0xa39a34], 0x20
0058D05C  41 0F BA E7 0E                  bt r15d, 0xe
0058D061  72 06                           jb 0x14058d069
0058D063  09 15 27 9A A3 00               or dword ptr [rip + 0xa39a27], edx
0058D069  48 0F BA E3 30                  bt rbx, 0x30
0058D06E  73 07                           jae 0x14058d077
0058D070  83 0D 19 9A A3 00 40            or dword ptr [rip + 0xa39a19], 0x40
0058D077  8B F9                           mov edi, ecx
0058D079  41 BE 00 80 00 00               mov r14d, 0x8000
0058D07F  41 0B FE                        or edi, r14d
0058D082  48 B8 00 00 00 00 00 00 20 00   movabs rax, 0x20000000000000
0058D08C  48 85 45 0F                     test qword ptr [rbp + 0xf], rax
0058D090  0F 44 F9                        cmove edi, ecx
0058D093  85 F2                           test edx, esi
0058D095  74 14                           je 0x14058d0ab
0058D097  33 C9                           xor ecx, ecx
0058D099  E8 C6 50 D6 FF                  call 0x1402f2164
0058D09E  8B DF                           mov ebx, edi
0058D0A0  0F BA EB 13                     bts ebx, 0x13
0058D0A4  A8 02                           test al, 2
0058D0A6  0F 44 DF                        cmove ebx, edi
0058D0A9  EB 16                           jmp 0x14058d0c1
0058D0AB  8B 05 DF 99 A3 00               mov eax, dword ptr [rip + 0xa399df]
0058D0B1  8B DF                           mov ebx, edi
0058D0B3  A8 40                           test al, 0x40
0058D0B5  74 0A                           je 0x14058d0c1
0058D0B7  0F BA E8 11                     bts eax, 0x11
0058D0BB  89 05 CF 99 A3 00               mov dword ptr [rip + 0xa399cf], eax
0058D0C1  F7 45 FF 00 00 80 00            test dword ptr [rbp - 1], 0x800000
0058D0C8  74 08                           je 0x14058d0d2
0058D0CA  0F BA 2D BE 99 A3 00 18         bts dword ptr [rip + 0xa399be], 0x18
0058D0D2  0F BA E6 0F                     bt esi, 0xf
0058D0D6  0F 92 C1                        setb cl
0058D0D9  0F BA E3 08                     bt ebx, 8
0058D0DD  0F 92 C0                        setb al
0058D0E0  84 C8                           test al, cl
0058D0E2  74 08                           je 0x14058d0ec
0058D0E4  0F BA 2D A4 99 A3 00 0E         bts dword ptr [rip + 0xa399a4], 0xe
0058D0EC  BF 00 00 01 00                  mov edi, 0x10000
0058D0F1  85 7D FF                        test dword ptr [rbp - 1], edi
0058D0F4  74 08                           je 0x14058d0fe
0058D0F6  0F BA 2D 92 99 A3 00 12         bts dword ptr [rip + 0xa39992], 0x12
0058D0FE  48 8D 4D B7                     lea rcx, [rbp - 0x49]
0058D102  E8 C1 01 00 00                  call 0x14058d2c8
0058D107  F6 D8                           neg al
0058D109  48 1B C0                        sbb rax, rax
0058D10C  48 23 45 B7                     and rax, qword ptr [rbp - 0x49]
0058D110  A8 10                           test al, 0x10
0058D112  74 07                           je 0x14058d11b
0058D114  44 09 35 75 99 A3 00            or dword ptr [rip + 0xa39975], r14d
0058D11B  A8 20                           test al, 0x20
0058D11D  74 06                           je 0x14058d125
0058D11F  09 3D 6B 99 A3 00               or dword ptr [rip + 0xa3996b], edi
0058D125  A8 08                           test al, 8
0058D127  74 0A                           je 0x14058d133
0058D129  81 0D 5D 99 A3 00 00 00 18 00   or dword ptr [rip + 0xa3995d], 0x180000
0058D133  41 B8 00 00 20 00               mov r8d, 0x200000
0058D139  A8 40                           test al, 0x40
0058D13B  74 07                           je 0x14058d144
0058D13D  44 09 05 4C 99 A3 00            or dword ptr [rip + 0xa3994c], r8d
0058D144  8B D3                           mov edx, ebx
0058D146  41 0B D0                        or edx, r8d
0058D149  A8 02                           test al, 2
0058D14B  0F 44 D3                        cmove edx, ebx
0058D14E  A8 04                           test al, 4
0058D150  74 0C                           je 0x14058d15e
0058D152  0F BA EA 16                     bts edx, 0x16
0058D156  84 C0                           test al, al
0058D158  79 04                           jns 0x14058d15e
0058D15A  0F BA EA 1B                     bts edx, 0x1b
0058D15E  8B 05 98 9E A3 00               mov eax, dword ptr [rip + 0xa39e98]
0058D164  F7 D0                           not eax
0058D166  25 F7 FF FF 7C                  and eax, 0x7cfffff7
0058D16B  23 D0                           and edx, eax
0058D16D  48 8D 05 AC AE FF FF            lea rax, [rip - 0x5154]
0058D174  48 89 05 F5 37 87 00            mov qword ptr [rip + 0x8737f5], rax
0058D17B  89 15 17 9B A3 00               mov dword ptr [rip + 0xa39b17], edx
0058D181  89 15 31 99 A3 00               mov dword ptr [rip + 0xa39931], edx
0058D187  48 8B 4D 3F                     mov rcx, qword ptr [rbp + 0x3f]
0058D18B  48 33 CC                        xor rcx, rsp
0058D18E  E8 AD F4 11 00                  call 0x1406ac640
0058D193  4C 8D 9C 24 B0 00 00 00         lea r11, [rsp + 0xb0]
0058D19B  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
0058D19F  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
0058D1A3  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
0058D1A7  49 8B E3                        mov rsp, r11
0058D1AA  41 5F                           pop r15
0058D1AC  41 5E                           pop r14
0058D1AE  5D                              pop rbp
0058D1AF  C3                              ret
0058D1B0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpDetermineEnlightenments(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 8903294)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 63) = result;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = 0;
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = v_xmm0;
    *(unsigned int *)(v_rsp - 95 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 31) = v_xmm1;
    *(unsigned __int8 *)(v_rip + 10716013) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 65) = v_xmm0;
    result = HviGetEnlightenmentInformation(v_rsp - 95 - 33, a2, a3, a4);
    *(unsigned __int64 *)(v_rsp - 95 + 15) = v_xmm0;
    result = HviGetHypervisorFeatures(v_rsp - 95 + 15, a2, a3, a4);
    result = HviGetHypervisorFeatures(v_rsp - 95 + 31, a2, a3, a4);
    result = HviGetHardwareFeatures(v_rsp - 95 - 1, a2, a3, a4);
    if ((((unsigned __int8)(v_rdi + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33))))) == 0) goto loc_0058CD3B;
    goto loc_0058CD73;
loc_0058CD3B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33)))) & (2)) == 0) goto loc_0058CD48;
    goto loc_0058CD73;
loc_0058CD48:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33)))) & (4)) == 0) goto loc_0058CD73;
    if (condition_is_below) goto loc_0058CD6E;
    v_rdi = (unsigned int)(0x800004ULL);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) == 2) {
        v_rdi = 4;
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 95 + 15))) & (16)) != 0) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33)))) & (8)) != 0) {
        v_rdi = (unsigned int)((v_rdi) | (16));
    }
    if (((512) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33))))) != 0) {
    }
    if (condition_is_above_or_equal) goto loc_0058CDDD;
    a2 = (a2) << (32);
    result = (*(unsigned __int64 *)(gs_base + (0 + 32))) | (a2);
    if ((((unsigned __int8)(result)) & (2)) == 0) {
        result = (result) | (2);
        a2 = result;
        a2 = (a2) >> (32);
    }
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)((unsigned int)(0x100000ULL))));
loc_0058CDDD:
    if (!(condition_is_above_or_equal)) {
    }
    if (!(condition_is_above_or_equal)) {
    }
    a2 = (unsigned int)((unsigned int)(v_rdi));
    if ((((unsigned int)((unsigned int)(0x100000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33))))) == 0) { a2 = (unsigned int)(v_rdi); }
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 43))))) >> (4));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (128));
    v_r14 = (unsigned int)((v_r14) & ((unsigned int)(v_rdi + 1)));
    if (condition_is_equal) { a1 = (unsigned int)(a2); }
    a3 = (unsigned int)((unsigned int)(a1));
    if ((((unsigned int)((unsigned int)(0x800000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33))))) == 0) { a3 = (unsigned int)(a1); }
    if (!(condition_is_above_or_equal)) {
    }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3))) | (32));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33)))) & (32)) == 0) { a2 = (unsigned int)(a3); }
    a1 = (unsigned int)((unsigned int)(a2));
    if (condition_is_above_or_equal) { a1 = (unsigned int)(a2); }
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (512));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 43)))) & (32)) == 0) { v_rdi = (unsigned int)(a1); }
    if (!(condition_is_less_or_equal)) {
        result = (unsigned int)(v_rdi + 1);
        v_rdi = (unsigned int)((v_rdi) | (64));
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
        result = (unsigned int)((result) - ((unsigned int)(v_rdi + 1)));
        result = (unsigned int)((result) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 29)))));
        *(unsigned int *)(v_rip + 10716205) = (unsigned int)(result);
    }
    if (condition_is_above_or_equal) goto loc_0058CED0;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = v_rdi + 1;
    result = HvlpSetRegister64((unsigned int)(0x90007ULL), v_rdi + 1, a3, v_rdi + 1);
    result = HvlpGetRegister64((unsigned int)(0x90007ULL), v_rsp - 95 - 33, a3, v_rdi + 1);
    if (((*(unsigned __int64 *)(v_rsp - 95 - 33)) & (result)) != 0) {
        a1 = 0x90007ULL;
        result = HvlpSetRegister64(a1, v_rsp - 95 - 33, a3, v_rdi + 1);
    }
    if (!(condition_is_above_or_equal)) {
    }
    if (condition_is_above_or_equal) goto loc_0058CEF3;
    if ((unsigned int)(v_r14) == 0) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10722199)))) & (2)) == 0) goto loc_0058CFC7;
    result = HvlpGetRegister128(516, v_rsp - 95 - 17, a3, v_rdi + 1);
    a1 = (unsigned int)((unsigned int)(v_rdi));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 13)))) & (1)) == 0) { a1 = (unsigned int)(v_rdi); }
    a2 = (unsigned int)((unsigned int)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 13)))) & (8)) == 0) { a2 = (unsigned int)(a1); }
    a1 = (unsigned int)((unsigned int)(a2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 13)))) & (2)) == 0) { a1 = (unsigned int)(a2); }
    v_rdi = (unsigned int)((unsigned int)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 13)))) & (4)) == 0) { v_rdi = (unsigned int)(a1); }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17)))) & (1)) != 0) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17)))) & (2)) != 0) {
    }
    if (!sign_flag) goto loc_0058CF8D;
    *(unsigned __int8 *)(v_rip + 10722411) = 1;
    result = HvlpQueryHypervisorSchedulerType(a1, a2, (unsigned int)(*(unsigned int *)(v_rsp - 95 - 13)), v_rdi + 1);
    if (((unsigned int)(result)) == 4) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10722117)))) & (1)) == 0) goto loc_0058CFA7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 17)))) & (4)) != 0) {
        *(unsigned int *)(v_rip + 10722097) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10722117)));
    }
    result = (unsigned int)(*(unsigned int *)(v_rip + 10722117));
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10722117))) | (16));
        *(unsigned int *)(v_rip + 10722081) = (unsigned int)(result);
    }
    if (!(condition_is_above_or_equal)) {
        *(unsigned int *)(v_rip + 10722065) = (unsigned int)(result);
    }
    a1 = (unsigned int)((unsigned int)(v_rdi));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 43)))) & (128)) == 0) { a1 = (unsigned int)(v_rdi); }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 43)))) & (8)) == 0) {
    }
    result = (*(unsigned __int64 *)(v_rsp - 95 + 15)) & (514);
    v_r14 = (unsigned int)((unsigned int)(a1));
    if (result != 514) { v_r14 = (unsigned int)(a1); }
    if (result < 514) {
        a4 = 8;
        a3 = v_rsp - 95 + 47;
        a1 = v_rsp - 95 - 65;
        a2 = a4 - 6;
        result = HvlpAcquireHypercallPage(a1, a2, a3, a4);
        a3 = *(unsigned __int64 *)(v_rsp - 95 - 41);
        a2 = 0;
        v_rdi = result;
        a1 = a2 + 70;
        result = HvcallInitiateHypercall(a1, a2, a3, a4);
        a1 = v_rsp - 95 - 65;
        result = HvlpReleaseHypercallPage(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(v_rdi);
        *(unsigned __int64 *)(v_rip + 10723139) = result;
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) | ((unsigned int)((unsigned int)(0x2000ULL))));
    if (condition_is_above_or_equal) { a1 = (unsigned int)(v_r14); }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 95 + 15))) & (4)) != 0) {
    }
    if (!(condition_is_below)) {
    }
    if (!(condition_is_above_or_equal)) {
    }
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(a1))) | ((unsigned int)((unsigned int)(0x8000ULL))));
    if (((*(unsigned __int64 *)(v_rsp - 95 + 15)) & (result)) == 0) { v_rdi = (unsigned int)(a1); }
    if ((((unsigned int)((unsigned int)(0x2000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 33))))) == 0) goto loc_0058D0AB;
    a1 = 0;
    result = VslGetNestedPageProtectionFlags(a1, (unsigned int)(0x2000ULL), a3, a4);
    v_rbx = (unsigned int)((unsigned int)(v_rdi));
    if ((((unsigned __int8)(result)) & (2)) == 0) { v_rbx = (unsigned int)(v_rdi); }
    goto loc_0058D0C1;
loc_0058D0AB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10721759)))) & (64)) != 0) {
        *(unsigned int *)(v_rip + 10721743) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10721759)));
    }
    if (((*(unsigned int *)(v_rsp - 95 - 1)) & (0x800000ULL)) != 0) {
    }
    a1 = (condition_is_below) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
    }
    if (((*(unsigned int *)(v_rsp - 95 - 1)) & ((unsigned int)((unsigned int)(0x10000ULL)))) != 0) {
    }
    result = HvlpQueryExtendedCapabilities(v_rsp - 95 - 73, (unsigned int)(0x2000ULL), a3, a4);
    result = (unsigned __int8)(-(result));
    result = (result) & (*(unsigned __int64 *)(v_rsp - 95 - 73));
    if ((((unsigned __int8)(result)) & (16)) != 0) {
    }
    if ((((unsigned __int8)(result)) & (32)) != 0) {
    }
    if ((((unsigned __int8)(result)) & (8)) != 0) {
    }
    if ((((unsigned __int8)(result)) & (64)) != 0) {
    }
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi))))) | ((unsigned int)((unsigned int)(0x200000ULL))));
    if ((((unsigned __int8)(result)) & (2)) == 0) { a2 = (unsigned int)((unsigned int)((unsigned int)(v_rdi))); }
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0058D15E;
    if (sign_flag) {
    }
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_rip + 10722968))));
    result = (unsigned int)((result) & (0x7CFFFFF7ULL));
    a2 = (unsigned int)((a2) & ((unsigned int)(result)));
    *(unsigned __int64 *)(v_rip + 8861685) = v_rip - 20820;
    *(unsigned int *)(v_rip + 10722071) = (unsigned int)(a2);
    *(unsigned int *)(v_rip + 10721585) = (unsigned int)(a2);
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 63)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x200000ULL), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlpDetermineEnlightenments(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x87DA7E)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x3F) = result;
    result = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = 0;
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x5F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = v_xmm1;
    *(uint8_t *)(v_rip + 0xA3836D) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = v_xmm0;
    result = HviGetEnlightenmentInformation(local_rsp - 95 - 33, Arg2, a3, a4);
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = v_xmm0;
    result = HviGetHypervisorFeatures(local_rsp - 95 + 15, Arg2, a3, a4);
    result = HviGetHypervisorFeatures(local_rsp - 95 + 31, Arg2, a3, a4);
    result = HviGetHardwareFeatures(local_rsp - 95 - 1, Arg2, a3, a4);
    if ((((uint8_t)(local_rdi + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21))))) == 0) goto loc_0058CD3B;
    goto loc_0058CD73;
loc_0058CD3B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21)))) & (2)) == 0) goto loc_0058CD48;
    goto loc_0058CD73;
loc_0058CD48:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21)))) & (4)) == 0) goto loc_0058CD73;
    if (condition_is_below) goto loc_0058CD6E;
    local_rdi = (uint32_t)(0x800004ULL);
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) == 2) {
        local_rdi = 4;
    }
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0x5F + 0xF))) & (16)) != 0) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21)))) & (8)) != 0) {
        local_rdi = (uint32_t)((local_rdi) | (16));
    }
    if (((512) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21))))) != 0) {
    }
    if (condition_is_above_or_equal) goto loc_0058CDDD;
    Arg2 = (Arg2) << (32);
    result = (*(uint64_t *)(gs_base + (0 + 0x20))) | (Arg2);
    if ((((uint8_t)(result)) & (2)) == 0) {
        result = (result) | (2);
        Arg2 = result;
        Arg2 = (Arg2) >> (32);
    }
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)((uint32_t)(0x100000ULL))));
loc_0058CDDD:
    if (!(condition_is_above_or_equal)) {
    }
    if (!(condition_is_above_or_equal)) {
    }
    Arg2 = (uint32_t)((uint32_t)(local_rdi));
    if ((((uint32_t)((uint32_t)(0x100000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21))))) == 0) { Arg2 = (uint32_t)(local_rdi); }
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x2B))))) >> (4));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | (128));
    local_r14 = (uint32_t)((local_r14) & ((uint32_t)(local_rdi + 1)));
    if (condition_is_equal) { Arg1 = (uint32_t)(Arg2); }
    a3 = (uint32_t)((uint32_t)(Arg1));
    if ((((uint32_t)((uint32_t)(0x800000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21))))) == 0) { a3 = (uint32_t)(Arg1); }
    if (!(condition_is_above_or_equal)) {
    }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(a3))) | (32));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21)))) & (32)) == 0) { Arg2 = (uint32_t)(a3); }
    Arg1 = (uint32_t)((uint32_t)(Arg2));
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(Arg2); }
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (512));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x2B)))) & (32)) == 0) { local_rdi = (uint32_t)(Arg1); }
    if (!(condition_is_less_or_equal)) {
        result = (uint32_t)(local_rdi + 1);
        local_rdi = (uint32_t)((local_rdi) | (64));
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
        result = (uint32_t)((result) - ((uint32_t)(local_rdi + 1)));
        result = (uint32_t)((result) | ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x1D)))));
        *(uint32_t *)(v_rip + 0xA3842D) = (uint32_t)(result);
    }
    if (condition_is_above_or_equal) goto loc_0058CED0;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = local_rdi + 1;
    result = HvlpSetRegister64((uint32_t)(0x90007ULL), local_rdi + 1, a3, local_rdi + 1);
    result = HvlpGetRegister64((uint32_t)(0x90007ULL), local_rsp - 95 - 33, a3, local_rdi + 1);
    if (((*(uint64_t *)(local_rsp - 0x5F - 0x21)) & (result)) != 0) {
        Arg1 = 0x90007ULL;
        result = HvlpSetRegister64(Arg1, local_rsp - 95 - 33, a3, local_rdi + 1);
    }
    if (!(condition_is_above_or_equal)) {
    }
    if (condition_is_above_or_equal) goto loc_0058CEF3;
    if ((uint32_t)(local_r14) == 0) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA39B97)))) & (2)) == 0) goto loc_0058CFC7;
    result = HvlpGetRegister128(516, local_rsp - 95 - 17, a3, local_rdi + 1);
    Arg1 = (uint32_t)((uint32_t)(local_rdi));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0xD)))) & (1)) == 0) { Arg1 = (uint32_t)(local_rdi); }
    Arg2 = (uint32_t)((uint32_t)(Arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0xD)))) & (8)) == 0) { Arg2 = (uint32_t)(Arg1); }
    Arg1 = (uint32_t)((uint32_t)(Arg2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0xD)))) & (2)) == 0) { Arg1 = (uint32_t)(Arg2); }
    local_rdi = (uint32_t)((uint32_t)(Arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0xD)))) & (4)) == 0) { local_rdi = (uint32_t)(Arg1); }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11)))) & (1)) != 0) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11)))) & (2)) != 0) {
    }
    if (!sign_flag) goto loc_0058CF8D;
    *(uint8_t *)(v_rip + 0xA39C6B) = 1;
    result = HvlpQueryHypervisorSchedulerType(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0xD)), local_rdi + 1);
    if (((uint32_t)(result)) == 4) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA39B45)))) & (1)) == 0) goto loc_0058CFA7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x11)))) & (4)) != 0) {
        *(uint32_t *)(v_rip + 0xA39B31) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA39B45)));
    }
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xA39B45));
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA39B45))) | (16));
        *(uint32_t *)(v_rip + 0xA39B21) = (uint32_t)(result);
    }
    if (!(condition_is_above_or_equal)) {
        *(uint32_t *)(v_rip + 0xA39B11) = (uint32_t)(result);
    }
    Arg1 = (uint32_t)((uint32_t)(local_rdi));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x2B)))) & (128)) == 0) { Arg1 = (uint32_t)(local_rdi); }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x2B)))) & (8)) == 0) {
    }
    result = (*(uint64_t *)(local_rsp - 0x5F + 0xF)) & (514);
    local_r14 = (uint32_t)((uint32_t)(Arg1));
    if (result != 514) { local_r14 = (uint32_t)(Arg1); }
    if (result < 514) {
        a4 = 8;
        a3 = local_rsp - 95 + 47;
        Arg1 = local_rsp - 95 - 65;
        Arg2 = a4 - 6;
        result = HvlpAcquireHypercallPage(Arg1, Arg2, a3, a4);
        a3 = *(uint64_t *)(local_rsp - 0x5F - 0x29);
        Arg2 = 0;
        local_rdi = result;
        Arg1 = Arg2 + 70;
        result = HvcallInitiateHypercall(Arg1, Arg2, a3, a4);
        Arg1 = local_rsp - 95 - 65;
        result = HvlpReleaseHypercallPage(Arg1, Arg2, a3, a4);
        result = *(uint64_t *)(local_rdi);
        *(uint64_t *)(v_rip + 0xA39F43) = result;
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) | ((uint32_t)((uint32_t)(0x2000ULL))));
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)(local_r14); }
    if ((((uint8_t)(*(uint64_t *)(local_rsp - 0x5F + 0xF))) & (4)) != 0) {
    }
    if (!(condition_is_below)) {
    }
    if (!(condition_is_above_or_equal)) {
    }
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | ((uint32_t)((uint32_t)(0x8000ULL))));
    if (((*(uint64_t *)(local_rsp - 0x5F + 0xF)) & (result)) == 0) { local_rdi = (uint32_t)(Arg1); }
    if ((((uint32_t)((uint32_t)(0x2000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x21))))) == 0) goto loc_0058D0AB;
    Arg1 = 0;
    result = VslGetNestedPageProtectionFlags(Arg1, (uint32_t)(0x2000ULL), a3, a4);
    local_rbx = (uint32_t)((uint32_t)(local_rdi));
    if ((((uint8_t)(result)) & (2)) == 0) { local_rbx = (uint32_t)(local_rdi); }
    goto loc_0058D0C1;
loc_0058D0AB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA399DF)))) & (64)) != 0) {
        *(uint32_t *)(v_rip + 0xA399CF) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA399DF)));
    }
    if (((*(uint32_t *)(local_rsp - 0x5F - 0x1)) & (0x800000ULL)) != 0) {
    }
    Arg1 = (condition_is_below) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
    }
    if (((*(uint32_t *)(local_rsp - 0x5F - 0x1)) & ((uint32_t)((uint32_t)(0x10000ULL)))) != 0) {
    }
    result = HvlpQueryExtendedCapabilities(local_rsp - 95 - 73, (uint32_t)(0x2000ULL), a3, a4);
    result = (uint8_t)(-(result));
    result = (result) & (*(uint64_t *)(local_rsp - 0x5F - 0x49));
    if ((((uint8_t)(result)) & (16)) != 0) {
    }
    if ((((uint8_t)(result)) & (32)) != 0) {
    }
    if ((((uint8_t)(result)) & (8)) != 0) {
    }
    if ((((uint8_t)(result)) & (64)) != 0) {
    }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi))))) | ((uint32_t)((uint32_t)(0x200000ULL))));
    if ((((uint8_t)(result)) & (2)) == 0) { Arg2 = (uint32_t)((uint32_t)((uint32_t)(local_rdi))); }
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0058D15E;
    if (sign_flag) {
    }
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(v_rip + 0xA39E98))));
    result = (uint32_t)((result) & (0x7CFFFFF7ULL));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(result)));
    *(uint64_t *)(v_rip + 0x8737F5) = v_rip - 20820;
    *(uint32_t *)(v_rip + 0xA39B17) = (uint32_t)(Arg2);
    *(uint32_t *)(v_rip + 0xA39931) = (uint32_t)(Arg2);
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x3F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x200000ULL), a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058CC9C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
