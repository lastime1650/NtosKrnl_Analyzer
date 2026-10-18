# KiDetectHardwareSpecControlFeatures

- RVA: `0x005BEC4C`–`0x005BF171` (길이 `1,317` bytes)
- VA: `0x00000001405BEC4C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA60C`
- 디코드: `376`개 명령, `1,317/1,317` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x005BECC0` → [HviIsHypervisorMicrosoftCompatible](../66/HviIsHypervisorMicrosoftCompatible_function_006668C8.md) (function, `0x006668C8`)
- `0x005BECCD` → [HviGetEnlightenmentInformation](../66/HviGetEnlightenmentInformation_function_006665E4.md) (function, `0x006665E4`)
- `0x005BECDD` → [HviGetHypervisorFeatures](../66/HviGetHypervisorFeatures_function_00666630.md) (function, `0x00666630`)
- `0x005BED04` → [HviIsAnyHypervisorPresent](../4A/HviIsAnyHypervisorPresent_function_004ADC50.md) (function, `0x004ADC50`)
- `0x005BEF7E` → [KiIsBranchConfusionPresent](KiIsBranchConfusionPresent_function_005BF2E8.md) (function, `0x005BF2E8`)
- `0x005BEF93` → [KiIsTsaPresent](KiIsTsaPresent_function_005BF4CC.md) (function, `0x005BF4CC`)
- `0x005BF150` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KiDetermineRetpolineEnablement](KiDetermineRetpolineEnablement_function_005BF1C0.md) at `0x005BF20D`
- [KiSetHardwareSpeculationControlFeatures](../5C/KiSetHardwareSpeculationControlFeatures_function_005C03A8.md) at `0x005C03CF`
- [KiDetectKvaLeakage](../5C/KiDetectKvaLeakage_function_005C4CD0.md) at `0x005C4D21`
- [KiDetectKvaLeakage](../5C/KiDetectKvaLeakage_function_005C4CD0.md) at `0x005C4D73`

### Static image references
- `0x005BEC66` → RVA `0x00E0A740` (`.data`; read)
- `0x005BEE5C` → RVA `0x00FC6E54` (`ALMOSTRO`; read)
- `0x005BEEDC` → RVA `0x00F10EC0` (`.data`; read)
- `0x005BEF57` → RVA `0x00FC6B60` (`ALMOSTRO`; read)
- `0x005BF00A` → RVA `0x00FC6E7C` (`ALMOSTRO`; read)
- `0x005BF059` → RVA `0x00F10EC0` (`.data`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BEC4C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
005BEC51  55                              push rbp
005BEC52  56                              push rsi
005BEC53  57                              push rdi
005BEC54  41 54                           push r12
005BEC56  41 55                           push r13
005BEC58  41 56                           push r14
005BEC5A  41 57                           push r15
005BEC5C  48 8B EC                        mov rbp, rsp
005BEC5F  48 81 EC 80 00 00 00            sub rsp, 0x80
005BEC66  48 8B 05 D3 BA 84 00            mov rax, qword ptr [rip + 0x84bad3]
005BEC6D  48 33 C4                        xor rax, rsp
005BEC70  48 89 45 F8                     mov qword ptr [rbp - 8], rax
005BEC74  8A 81 8D 00 00 00               mov al, byte ptr [rcx + 0x8d]
005BEC7A  0F 57 C0                        xorps xmm0, xmm0
005BEC7D  44 8A 61 40                     mov r12b, byte ptr [rcx + 0x40]
005BEC81  0F 57 C9                        xorps xmm1, xmm1
005BEC84  44 8A 71 43                     mov r14b, byte ptr [rcx + 0x43]
005BEC88  B3 01                           mov bl, 1
005BEC8A  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
005BEC8E  C7 45 B0 48 00 00 00            mov dword ptr [rbp - 0x50], 0x48
005BEC95  4C 8B F9                        mov r15, rcx
005BEC98  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
005BEC9C  40 32 F6                        xor sil, sil
005BEC9F  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
005BECA3  45 32 ED                        xor r13b, r13b
005BECA6  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
005BECAA  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
005BECAE  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
005BECB6  0F 11 4D E8                     movups xmmword ptr [rbp - 0x18], xmm1
005BECBA  88 45 A0                        mov byte ptr [rbp - 0x60], al
005BECBD  88 5D A1                        mov byte ptr [rbp - 0x5f], bl
005BECC0  E8 03 7C 0A 00                  call 0x1406668c8
005BECC5  84 C0                           test al, al
005BECC7  74 3B                           je 0x1405bed04
005BECC9  48 8D 4D E8                     lea rcx, [rbp - 0x18]
005BECCD  E8 12 79 0A 00                  call 0x1406665e4
005BECD2  0F 57 C0                        xorps xmm0, xmm0
005BECD5  48 8D 4D D8                     lea rcx, [rbp - 0x28]
005BECD9  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
005BECDD  E8 4E 79 0A 00                  call 0x140666630
005BECE2  48 B8 00 00 00 00 00 10 00 00   movabs rax, 0x100000000000
005BECEC  48 85 45 D8                     test qword ptr [rbp - 0x28], rax
005BECF0  74 25                           je 0x1405bed17
005BECF2  F7 45 E8 00 10 00 00            test dword ptr [rbp - 0x18], 0x1000
005BECF9  75 1C                           jne 0x1405bed17
005BECFB  45 32 C9                        xor r9b, r9b
005BECFE  44 88 4D A1                     mov byte ptr [rbp - 0x5f], r9b
005BED02  EB 16                           jmp 0x1405bed1a
005BED04  E8 47 EF EE FF                  call 0x1404adc50
005BED09  F6 D8                           neg al
005BED0B  1A C9                           sbb cl, cl
005BED0D  22 CB                           and cl, bl
005BED0F  44 8A C9                        mov r9b, cl
005BED12  88 4D A1                        mov byte ptr [rbp - 0x5f], cl
005BED15  EB 03                           jmp 0x1405bed1a
005BED17  44 8A CB                        mov r9b, bl
005BED1A  48 8B 7D A8                     mov rdi, qword ptr [rbp - 0x58]
005BED1E  33 C0                           xor eax, eax
005BED20  33 C9                           xor ecx, ecx
005BED22  41 B3 02                        mov r11b, 2
005BED25  0F A2                           cpuid
005BED27  41 BA 00 02 00 00               mov r10d, 0x200
005BED2D  83 F8 07                        cmp eax, 7
005BED30  72 56                           jb 0x1405bed88
005BED32  33 C9                           xor ecx, ecx
005BED34  B8 07 00 00 00                  mov eax, 7
005BED39  0F A2                           cpuid
005BED3B  44 8B C2                        mov r8d, edx
005BED3E  0F BA E2 1D                     bt edx, 0x1d
005BED42  73 47                           jae 0x1405bed8b
005BED44  B9 0A 01 00 00                  mov ecx, 0x10a
005BED49  0F 32                           rdmsr
005BED4B  48 C1 E2 20                     shl rdx, 0x20
005BED4F  48 0B C2                        or rax, rdx
005BED52  41 84 C3                        test r11b, al
005BED55  74 11                           je 0x1405bed68
005BED57  49 0B FA                        or rdi, r10
005BED5A  41 B5 01                        mov r13b, 1
005BED5D  48 83 CF 01                     or rdi, 1
005BED61  41 8A F5                        mov sil, r13b
005BED64  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BED68  A8 10                           test al, 0x10
005BED6A  74 0C                           je 0x1405bed78
005BED6C  48 0F BA EF 08                  bts rdi, 8
005BED71  40 B6 01                        mov sil, 1
005BED74  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BED78  A8 04                           test al, 4
005BED7A  74 0F                           je 0x1405bed8b
005BED7C  49 0B FA                        or rdi, r10
005BED7F  40 B6 01                        mov sil, 1
005BED82  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BED86  EB 03                           jmp 0x1405bed8b
005BED88  45 33 C0                        xor r8d, r8d
005BED8B  8A 5D A0                        mov bl, byte ptr [rbp - 0x60]
005BED8E  80 FB 01                        cmp bl, 1
005BED91  0F 85 80 00 00 00               jne 0x1405bee17
005BED97  33 C9                           xor ecx, ecx
005BED99  B8 00 00 00 80                  mov eax, 0x80000000
005BED9E  0F A2                           cpuid
005BEDA0  3D 08 00 00 80                  cmp eax, 0x80000008
005BEDA5  72 0B                           jb 0x1405bedb2
005BEDA7  B8 08 00 00 80                  mov eax, 0x80000008
005BEDAC  33 C9                           xor ecx, ecx
005BEDAE  0F A2                           cpuid
005BEDB0  EB 02                           jmp 0x1405bedb4
005BEDB2  33 DB                           xor ebx, ebx
005BEDB4  0F BA E3 0C                     bt ebx, 0xc
005BEDB8  73 0B                           jae 0x1405bedc5
005BEDBA  48 83 CF 04                     or rdi, 4
005BEDBE  40 B6 01                        mov sil, 1
005BEDC1  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEDC5  0F BA E3 0E                     bt ebx, 0xe
005BEDC9  73 0B                           jae 0x1405bedd6
005BEDCB  48 83 CF 10                     or rdi, 0x10
005BEDCF  40 B6 01                        mov sil, 1
005BEDD2  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEDD6  0F BA E3 0F                     bt ebx, 0xf
005BEDDA  73 0B                           jae 0x1405bede7
005BEDDC  48 83 CF 40                     or rdi, 0x40
005BEDE0  40 B6 01                        mov sil, 1
005BEDE3  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEDE7  0F BA E3 18                     bt ebx, 0x18
005BEDEB  73 09                           jae 0x1405bedf6
005BEDED  48 0F BA EF 07                  bts rdi, 7
005BEDF2  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEDF6  0F BA E3 1A                     bt ebx, 0x1a
005BEDFA  73 0B                           jae 0x1405bee07
005BEDFC  48 81 CF 80 01 00 00            or rdi, 0x180
005BEE03  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEE07  8A 5D A0                        mov bl, byte ptr [rbp - 0x60]
005BEE0A  40 8A CF                        mov cl, dil
005BEE0D  40 84 FF                        test dil, dil
005BEE10  79 44                           jns 0x1405bee56
005BEE12  40 B6 01                        mov sil, 1
005BEE15  EB 3F                           jmp 0x1405bee56
005BEE17  41 0F BA E0 1A                  bt r8d, 0x1a
005BEE1C  73 0B                           jae 0x1405bee29
005BEE1E  48 83 CF 14                     or rdi, 0x14
005BEE22  40 B6 01                        mov sil, 1
005BEE25  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEE29  41 0F BA E0 1B                  bt r8d, 0x1b
005BEE2E  73 0B                           jae 0x1405bee3b
005BEE30  48 83 CF 44                     or rdi, 0x44
005BEE34  40 B6 01                        mov sil, 1
005BEE37  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEE3B  41 0F BA E0 1F                  bt r8d, 0x1f
005BEE40  73 11                           jae 0x1405bee53
005BEE42  48 0F BA EF 07                  bts rdi, 7
005BEE47  40 B6 01                        mov sil, 1
005BEE4A  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEE4E  48 8B CF                        mov rcx, rdi
005BEE51  EB 03                           jmp 0x1405bee56
005BEE53  40 8A CF                        mov cl, dil
005BEE56  F6 45 C0 01                     test byte ptr [rbp - 0x40], 1
005BEE5A  75 09                           jne 0x1405bee65
005BEE5C  83 3D F1 7F A0 00 01            cmp dword ptr [rip + 0xa07ff1], 1
005BEE63  75 0B                           jne 0x1405bee70
005BEE65  48 83 CF 20                     or rdi, 0x20
005BEE69  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEE6D  40 8A CF                        mov cl, dil
005BEE70  41 3A DB                        cmp bl, r11b
005BEE73  75 56                           jne 0x1405beecb
005BEE75  41 80 FC 06                     cmp r12b, 6
005BEE79  75 50                           jne 0x1405beecb
005BEE7B  41 80 FE 8E                     cmp r14b, 0x8e
005BEE7F  74 18                           je 0x1405bee99
005BEE81  41 8D 46 B2                     lea eax, [r14 - 0x4e]
005BEE85  3C 19                           cmp al, 0x19
005BEE87  77 0A                           ja 0x1405bee93
005BEE89  BA 81 00 01 03                  mov edx, 0x3010081
005BEE8E  0F A3 C2                        bt edx, eax
005BEE91  72 06                           jb 0x1405bee99
005BEE93  41 80 FE 9E                     cmp r14b, 0x9e
005BEE97  75 0A                           jne 0x1405beea3
005BEE99  49 0B FA                        or rdi, r10
005BEE9C  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEEA0  40 8A CF                        mov cl, dil
005BEEA3  41 8D 46 C9                     lea eax, [r14 - 0x37]
005BEEA7  3C 37                           cmp al, 0x37
005BEEA9  77 10                           ja 0x1405beebb
005BEEAB  48 BA 01 00 68 00 48 40 80 00   movabs rdx, 0x80404800680001
005BEEB5  48 0F A3 C2                     bt rdx, rax
005BEEB9  72 06                           jb 0x1405beec1
005BEEBB  41 80 FE 75                     cmp r14b, 0x75
005BEEBF  75 0A                           jne 0x1405beecb
005BEEC1  49 0B FA                        or rdi, r10
005BEEC4  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEEC8  40 8A CF                        mov cl, dil
005BEECB  80 E1 14                        and cl, 0x14
005BEECE  80 F9 14                        cmp cl, 0x14
005BEED1  0F 85 80 00 00 00               jne 0x1405bef57
005BEED7  45 84 C9                        test r9b, r9b
005BEEDA  74 0C                           je 0x1405beee8
005BEEDC  F7 05 DA 1F 95 00 00 80 00 00   test dword ptr [rip + 0x951fda], 0x8000
005BEEE6  74 52                           je 0x1405bef3a
005BEEE8  41 8B 8F CC 06 00 00            mov ecx, dword ptr [r15 + 0x6cc]
005BEEEF  41 84 CB                        test r11b, cl
005BEEF2  74 09                           je 0x1405beefd
005BEEF4  48 0F BA EF 0A                  bts rdi, 0xa
005BEEF9  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEEFD  F6 C1 04                        test cl, 4
005BEF00  74 1D                           je 0x1405bef1f
005BEF02  48 0F BA EF 0B                  bts rdi, 0xb
005BEF07  F7 05 AF 1F 95 00 00 40 00 00   test dword ptr [rip + 0x951faf], 0x4000
005BEF11  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEF15  74 08                           je 0x1405bef1f
005BEF17  48 83 CF 01                     or rdi, 1
005BEF1B  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEF1F  41 3A DB                        cmp bl, r11b
005BEF22  75 16                           jne 0x1405bef3a
005BEF24  45 84 C9                        test r9b, r9b
005BEF27  75 05                           jne 0x1405bef2e
005BEF29  45 84 ED                        test r13b, r13b
005BEF2C  74 05                           je 0x1405bef33
005BEF2E  F6 C1 03                        test cl, 3
005BEF31  74 24                           je 0x1405bef57
005BEF33  48 0F BA EF 0C                  bts rdi, 0xc
005BEF38  EB 19                           jmp 0x1405bef53
005BEF3A  80 FB 01                        cmp bl, 1
005BEF3D  75 18                           jne 0x1405bef57
005BEF3F  48 0F BA EF 0C                  bts rdi, 0xc
005BEF44  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEF48  40 F6 C7 40                     test dil, 0x40
005BEF4C  74 09                           je 0x1405bef57
005BEF4E  48 0F BA EF 0E                  bts rdi, 0xe
005BEF53  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEF57  48 0F BA 25 00 7C A0 00 11      bt qword ptr [rip + 0xa07c00], 0x11
005BEF60  0F 92 C1                        setb cl
005BEF63  0F BA 25 55 1F 95 00 16         bt dword ptr [rip + 0x951f55], 0x16
005BEF6B  0F 93 C0                        setae al
005BEF6E  84 C8                           test al, cl
005BEF70  74 09                           je 0x1405bef7b
005BEF72  48 0F BA EF 0D                  bts rdi, 0xd
005BEF77  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEF7B  49 8B CF                        mov rcx, r15
005BEF7E  E8 65 03 00 00                  call 0x1405bf2e8
005BEF83  85 C0                           test eax, eax
005BEF85  74 09                           je 0x1405bef90
005BEF87  48 0F BA EF 0F                  bts rdi, 0xf
005BEF8C  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEF90  49 8B CF                        mov rcx, r15
005BEF93  E8 34 05 00 00                  call 0x1405bf4cc
005BEF98  85 C0                           test eax, eax
005BEF9A  74 09                           je 0x1405befa5
005BEF9C  48 0F BA EF 1B                  bts rdi, 0x1b
005BEFA1  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEFA5  80 FB 01                        cmp bl, 1
005BEFA8  75 0D                           jne 0x1405befb7
005BEFAA  48 F7 05 AB 7B A0 00 00 00 00 02  test qword ptr [rip + 0xa07bab], 0x2000000
005BEFB5  74 08                           je 0x1405befbf
005BEFB7  48 83 CF 08                     or rdi, 8
005BEFBB  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEFBF  41 B0 02                        mov r8b, 2
005BEFC2  C6 45 B4 00                     mov byte ptr [rbp - 0x4c], 0
005BEFC6  B9 00 00 01 00                  mov ecx, 0x10000
005BEFCB  41 3A D8                        cmp bl, r8b
005BEFCE  0F 85 85 00 00 00               jne 0x1405bf059
005BEFD4  48 8B 05 85 7B A0 00            mov rax, qword ptr [rip + 0xa07b85]
005BEFDB  8A 5D A1                        mov bl, byte ptr [rbp - 0x5f]
005BEFDE  48 0F BA E0 1A                  bt rax, 0x1a
005BEFE3  72 10                           jb 0x1405beff5
005BEFE5  84 DB                           test bl, bl
005BEFE7  75 05                           jne 0x1405befee
005BEFE9  45 84 ED                        test r13b, r13b
005BEFEC  74 07                           je 0x1405beff5
005BEFEE  48 0B F9                        or rdi, rcx
005BEFF1  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BEFF5  48 85 F9                        test rcx, rdi
005BEFF8  74 5C                           je 0x1405bf056
005BEFFA  25 00 00 00 08                  and eax, 0x8000000
005BEFFF  74 09                           je 0x1405bf00a
005BF001  48 0F BA EF 11                  bts rdi, 0x11
005BF006  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BF00A  83 3D 6B 7E A0 00 00            cmp dword ptr [rip + 0xa07e6b], 0
005BF011  74 06                           je 0x1405bf019
005BF013  C6 45 B4 03                     mov byte ptr [rbp - 0x4c], 3
005BF017  EB 3D                           jmp 0x1405bf056
005BF019  48 85 C0                        test rax, rax
005BF01C  75 34                           jne 0x1405bf052
005BF01E  41 80 7F 40 06                  cmp byte ptr [r15 + 0x40], 6
005BF023  75 25                           jne 0x1405bf04a
005BF025  41 8A 47 43                     mov al, byte ptr [r15 + 0x43]
005BF029  3C 97                           cmp al, 0x97
005BF02B  75 0D                           jne 0x1405bf03a
005BF02D  41 8A 47 42                     mov al, byte ptr [r15 + 0x42]
005BF031  41 3A C0                        cmp al, r8b
005BF034  74 1C                           je 0x1405bf052
005BF036  3C 05                           cmp al, 5
005BF038  EB 0E                           jmp 0x1405bf048
005BF03A  3C 9A                           cmp al, 0x9a
005BF03C  75 0C                           jne 0x1405bf04a
005BF03E  41 8A 47 42                     mov al, byte ptr [r15 + 0x42]
005BF042  3C 03                           cmp al, 3
005BF044  74 0C                           je 0x1405bf052
005BF046  3C 04                           cmp al, 4
005BF048  74 08                           je 0x1405bf052
005BF04A  C6 45 B4 01                     mov byte ptr [rbp - 0x4c], 1
005BF04E  84 DB                           test bl, bl
005BF050  74 04                           je 0x1405bf056
005BF052  44 88 45 B4                     mov byte ptr [rbp - 0x4c], r8b
005BF056  8A 5D A0                        mov bl, byte ptr [rbp - 0x60]
005BF059  85 0D 61 1E 95 00               test dword ptr [rip + 0x951e61], ecx
005BF05F  74 0B                           je 0x1405bf06c
005BF061  48 81 E7 FE F7 FF FF            and rdi, 0xfffffffffffff7fe
005BF068  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BF06C  41 3A D8                        cmp bl, r8b
005BF06F  75 5D                           jne 0x1405bf0ce
005BF071  48 B8 00 00 00 00 00 00 08 00   movabs rax, 0x8000000000000
005BF07B  48 85 45 C0                     test qword ptr [rbp - 0x40], rax
005BF07F  74 4D                           je 0x1405bf0ce
005BF081  48 8B 05 D8 7A A0 00            mov rax, qword ptr [rip + 0xa07ad8]
005BF088  48 0F BA E0 20                  bt rax, 0x20
005BF08D  72 3F                           jb 0x1405bf0ce
005BF08F  48 0F BA EF 12                  bts rdi, 0x12
005BF094  48 0F BA E0 1F                  bt rax, 0x1f
005BF099  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BF09D  48 8B DF                        mov rbx, rdi
005BF0A0  73 29                           jae 0x1405bf0cb
005BF0A2  48 0F BA EF 13                  bts rdi, 0x13
005BF0A7  B9 23 01 00 00                  mov ecx, 0x123
005BF0AC  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BF0B0  0F 32                           rdmsr
005BF0B2  48 C1 E2 20                     shl rdx, 0x20
005BF0B6  48 0B C2                        or rax, rdx
005BF0B9  A8 20                           test al, 0x20
005BF0BB  74 0E                           je 0x1405bf0cb
005BF0BD  48 8B FB                        mov rdi, rbx
005BF0C0  48 81 CF 00 00 18 00            or rdi, 0x180000
005BF0C7  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BF0CB  8A 5D A0                        mov bl, byte ptr [rbp - 0x60]
005BF0CE  41 8A 8F 8D 00 00 00            mov cl, byte ptr [r15 + 0x8d]
005BF0D5  80 F9 01                        cmp cl, 1
005BF0D8  75 14                           jne 0x1405bf0ee
005BF0DA  48 0F BA 25 7D 7A A0 00 22      bt qword ptr [rip + 0xa07a7d], 0x22
005BF0E3  72 09                           jb 0x1405bf0ee
005BF0E5  48 0F BA EF 15                  bts rdi, 0x15
005BF0EA  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BF0EE  80 FB 01                        cmp bl, 1
005BF0F1  75 09                           jne 0x1405bf0fc
005BF0F3  48 0F BA EF 16                  bts rdi, 0x16
005BF0F8  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BF0FC  41 3A C8                        cmp cl, r8b
005BF0FF  75 27                           jne 0x1405bf128
005BF101  48 8B 05 58 7A A0 00            mov rax, qword ptr [rip + 0xa07a58]
005BF108  48 0F BA E0 23                  bt rax, 0x23
005BF10D  72 19                           jb 0x1405bf128
005BF10F  48 0F BA EF 17                  bts rdi, 0x17
005BF114  48 0F BA E0 24                  bt rax, 0x24
005BF119  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BF11D  73 09                           jae 0x1405bf128
005BF11F  48 0F BA EF 18                  bts rdi, 0x18
005BF124  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
005BF128  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
005BF12C  0F 10 45 A8                     movups xmm0, xmmword ptr [rbp - 0x58]
005BF130  F2 0F 10 4D B8                  movsd xmm1, qword ptr [rbp - 0x48]
005BF135  0F 11 00                        movups xmmword ptr [rax], xmm0
005BF138  F2 0F 11 48 10                  movsd qword ptr [rax + 0x10], xmm1
005BF13D  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
005BF141  48 85 C0                        test rax, rax
005BF144  74 03                           je 0x1405bf149
005BF146  40 88 30                        mov byte ptr [rax], sil
005BF149  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
005BF14D  48 33 CC                        xor rcx, rsp
005BF150  E8 EB D4 0E 00                  call 0x1406ac640
005BF155  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
005BF15D  48 81 C4 80 00 00 00            add rsp, 0x80
005BF164  41 5F                           pop r15
005BF166  41 5E                           pop r14
005BF168  41 5D                           pop r13
005BF16A  41 5C                           pop r12
005BF16C  5F                              pop rdi
005BF16D  5E                              pop rsi
005BF16E  5D                              pop rbp
005BF16F  C3                              ret
005BF170  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiDetectHardwareSpecControlFeatures(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int8 v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int8 v_stack_m97;
    unsigned __int8 v_stack_m98;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 8698579)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m90 = v_xmm0;
    v_stack_m88 = 72;
    v_stack_m68 = a4;
    v_rsi = 0;
    v_stack_m70 = a3;
    v_r13 = 0;
    v_stack_m78 = a2;
    v_stack_m60 = v_xmm0;
    v_stack_m80 = 4;
    v_stack_m50 = v_xmm1;
    v_stack_m98 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 141));
    v_stack_m97 = 1;
    result = HviIsHypervisorMicrosoftCompatible(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_005BED04;
    result = HviGetEnlightenmentInformation(v_stack_m50, a2, a3, a4);
    v_stack_m60 = v_xmm0;
    result = HviGetHypervisorFeatures(v_stack_m60, a2, a3, a4);
    if (((v_stack_m60) & (result)) == 0) goto loc_005BED17;
    if (((v_stack_m50) & (0x1000ULL)) != 0) goto loc_005BED17;
    a4 = 0;
    v_stack_m97 = 0;
    goto loc_005BED1A;
loc_005BED04:
    result = HviIsAnyHypervisorPresent(v_stack_m60, a2, a3, a4);
    result = (unsigned __int8)(-(result));
    a1 = (unsigned __int8)((v_stack_m60) & (1));
    v_stack_m97 = (unsigned __int8)(a1);
    goto loc_005BED1A;
loc_005BED17:
loc_005BED1A:
    result = 0;
    a1 = 0;
    if (0 < 7) goto loc_005BED88;
    a1 = 0;
    if (condition_is_above_or_equal) goto loc_005BED8B;
    a2 = (a2) << (32);
    result = (7) | (a2);
    v_rdi = v_stack_m90;
    if (((2) & ((unsigned __int8)(result))) != 0) {
        v_rdi = (v_stack_m90) | (512);
        v_r13 = 1;
        v_rdi = (v_rdi) | (1);
        v_rsi = (unsigned __int8)(v_r13);
        v_stack_m90 = v_rdi;
    }
    if ((((unsigned __int8)(result)) & (16)) != 0) {
        v_rsi = 1;
        v_stack_m90 = v_rdi;
    }
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_005BED8B;
    v_rdi = (v_rdi) | (512);
    v_stack_m90 = v_rdi;
    goto loc_005BED8B;
loc_005BED88:
    a3 = 0;
loc_005BED8B:
    if (((unsigned __int8)(v_stack_m98)) != 1) goto loc_005BEE17;
    a1 = 0;
    if (((unsigned int)((unsigned int)(0x80000000ULL))) < 0x80000008ULL) goto loc_005BEDB2;
    a1 = 0;
    goto loc_005BEDB4;
loc_005BEDB2:
    v_rbx = 0;
loc_005BEDB4:
    v_rsi = 1;
    if (!(condition_is_above_or_equal)) {
        v_rdi = (v_rdi) | (4);
        v_rsi = 1;
        v_stack_m90 = v_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        v_rdi = (v_rdi) | (16);
        v_rsi = 1;
        v_stack_m90 = v_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        v_rdi = (v_rdi) | (64);
        v_rsi = 1;
        v_stack_m90 = v_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        v_stack_m90 = v_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        v_rdi = (v_rdi) | (384);
        v_stack_m90 = v_rdi;
    }
    if (!sign_flag) goto loc_005BEE56;
    goto loc_005BEE56;
loc_005BEE17:
    v_rsi = 1;
    if (!(condition_is_above_or_equal)) {
        v_rdi = (v_rdi) | (20);
        v_rsi = 1;
        v_stack_m90 = v_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        v_rdi = (v_rdi) | (68);
        v_rsi = 1;
        v_stack_m90 = v_rdi;
    }
    if (condition_is_above_or_equal) goto loc_005BEE53;
    v_stack_m90 = v_rdi;
    goto loc_005BEE56;
loc_005BEE53:
loc_005BEE56:
    if (((v_stack_m78) & (1)) != 0) goto loc_005BEE65;
    if ((*(unsigned int *)(v_rip + 10518513)) == 1) {
        v_rdi = (v_rdi) | (32);
        v_stack_m90 = v_rdi;
        a1 = (unsigned __int8)(v_rdi);
    }
    if (((unsigned __int8)(v_stack_m98)) != 2) goto loc_005BEECB;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 64))) != 6) goto loc_005BEECB;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) == 142) goto loc_005BEE99;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67) - 78)) > 25) goto loc_005BEE93;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67) - 78)) < 25) goto loc_005BEE99;
loc_005BEE93:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) == 158) {
        v_rdi = (v_rdi) | (512);
        v_stack_m90 = v_rdi;
        a1 = (unsigned __int8)(v_rdi);
    }
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67) - 55)) > 55) goto loc_005BEEBB;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67) - 55)) < 55) goto loc_005BEEC1;
loc_005BEEBB:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) == 117) {
        v_rdi = (v_rdi) | (512);
        v_stack_m90 = v_rdi;
        a1 = (unsigned __int8)(v_rdi);
    }
    a1 = (unsigned __int8)((a1) & (20));
    if (((unsigned __int8)(a1)) != 20) goto loc_005BEF57;
    if (1 == 0) goto loc_005BEEE8;
    if (((*(unsigned int *)(v_rip + 9773018)) & (0x8000ULL)) == 0) goto loc_005BEF3A;
loc_005BEEE8:
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1740))))) != 0) {
        v_stack_m90 = v_rdi;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1740)))) & (4)) == 0) goto loc_005BEF1F;
    v_stack_m90 = v_rdi;
    if (((*(unsigned int *)(v_rip + 9772975)) & (0x4000ULL)) != 0) {
        v_rdi = (v_rdi) | (1);
        v_stack_m90 = v_rdi;
    }
    if (((unsigned __int8)(v_stack_m98)) != 2) goto loc_005BEF3A;
    if (1 != 0) goto loc_005BEF2E;
    if ((unsigned __int8)(v_r13) == 0) goto loc_005BEF33;
loc_005BEF2E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1740)))) & (3)) == 0) goto loc_005BEF57;
loc_005BEF33:
    goto loc_005BEF53;
loc_005BEF3A:
    if (((unsigned __int8)(v_stack_m98)) != 1) goto loc_005BEF57;
    v_stack_m90 = v_rdi;
    if ((((unsigned __int8)(v_rdi)) & (64)) == 0) goto loc_005BEF57;
loc_005BEF53:
    v_stack_m90 = v_rdi;
loc_005BEF57:
    a1 = (condition_is_below) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
        v_stack_m90 = v_rdi;
    }
    result = KiIsBranchConfusionPresent(a1, (unsigned int)(0x3010081ULL), a3, 1);
    if ((unsigned int)(result) != 0) {
        v_stack_m90 = v_rdi;
    }
    result = KiIsTsaPresent(a1, (unsigned int)(0x3010081ULL), a3, 1);
    if ((unsigned int)(result) != 0) {
        v_stack_m90 = v_rdi;
    }
    if (((unsigned __int8)(v_stack_m98)) != 1) goto loc_005BEFB7;
    if (((*(unsigned __int64 *)(v_rip + 10517419)) & (0x2000000ULL)) != 0) {
        v_rdi = (v_rdi) | (8);
        v_stack_m90 = v_rdi;
    }
    v_stack_m84 = 0;
    if (((unsigned __int8)(v_stack_m98)) != 2) goto loc_005BF059;
    if (((unsigned __int8)(v_stack_m98)) < 2) goto loc_005BEFF5;
    if ((unsigned __int8)(v_stack_m97) != 0) goto loc_005BEFEE;
    if ((unsigned __int8)(v_r13) != 0) {
        v_rdi = (v_rdi) | ((unsigned int)(0x10000ULL));
        v_stack_m90 = v_rdi;
    }
    if ((((unsigned int)(0x10000ULL)) & (v_rdi)) == 0) goto loc_005BF056;
    result = (unsigned int)((*(unsigned __int64 *)(v_rip + 10517381)) & (0x8000000ULL));
    if (!(condition_is_equal)) {
        v_stack_m90 = v_rdi;
    }
    if ((*(unsigned int *)(v_rip + 10518123)) == 0) goto loc_005BF019;
    v_stack_m84 = 3;
    goto loc_005BF056;
loc_005BF019:
    if (result != 0) goto loc_005BF052;
    if ((*(unsigned __int8 *)(a1 + 64)) != 6) goto loc_005BF04A;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 67))) != 151) goto loc_005BF03A;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 66))) == 2) goto loc_005BF052;
    goto loc_005BF048;
loc_005BF03A:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 66))) != 154) goto loc_005BF04A;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 66))) == 3) goto loc_005BF052;
loc_005BF048:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 66))) == 4) goto loc_005BF052;
loc_005BF04A:
    v_stack_m84 = 1;
    if ((unsigned __int8)(v_stack_m97) != 0) {
        v_stack_m84 = 2;
    }
loc_005BF059:
    if (((*(unsigned int *)(v_rip + 9772641)) & ((unsigned int)((unsigned int)(0x10000ULL)))) != 0) {
        v_rdi = (v_rdi) & (0xFFFFFFFFFFFFF7FEULL);
        v_stack_m90 = v_rdi;
    }
    if (((unsigned __int8)(v_stack_m98)) != 2) goto loc_005BF0CE;
    if (((v_stack_m78) & (*(unsigned __int8 *)(a1 + 66))) == 0) goto loc_005BF0CE;
    if (condition_is_below) goto loc_005BF0CE;
    v_stack_m90 = v_rdi;
    if (condition_is_above_or_equal) goto loc_005BF0CB;
    v_stack_m90 = v_rdi;
    a2 = ((unsigned int)(0x3010081ULL)) << (32);
    result = (*(unsigned __int64 *)(v_rip + 10517208)) | (a2);
    if ((((unsigned __int8)(result)) & (32)) != 0) {
        v_rdi = v_rdi;
        v_rdi = (v_rdi) | (0x180000ULL);
        v_stack_m90 = v_rdi;
    }
loc_005BF0CE:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 1) goto loc_005BF0EE;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) >= 1) {
        v_stack_m90 = v_rdi;
    }
    if (((unsigned __int8)(v_stack_m98)) == 1) {
        v_stack_m90 = v_rdi;
    }
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) != 2) goto loc_005BF128;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) < 2) goto loc_005BF128;
    v_stack_m90 = v_rdi;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 141))) < 2) {
        v_stack_m90 = v_rdi;
    }
    *(unsigned __int64 *)(v_stack_m70) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m70 + 16) = v_xmm1;
    if (v_stack_m68 != 0) {
        *(unsigned __int8 *)(v_stack_m68) = 1;
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 2, 1);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiDetectHardwareSpecControlFeatures(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint8_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint8_t v_stack_m97;
    uint8_t v_stack_m98;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x84BAD3)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m90 = v_xmm0;
    v_stack_m88 = 72;
    v_stack_m68 = Arg4;
    local_rsi = 0;
    v_stack_m70 = Arg3;
    local_r13 = 0;
    v_stack_m78 = Arg2;
    v_stack_m60 = v_xmm0;
    v_stack_m80 = 4;
    v_stack_m50 = v_xmm1;
    v_stack_m98 = (uint8_t)(*(uint8_t *)(arg1 + 0x8D));
    v_stack_m97 = 1;
    result = HviIsHypervisorMicrosoftCompatible(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_005BED04;
    result = HviGetEnlightenmentInformation(v_stack_m50, Arg2, Arg3, Arg4);
    v_stack_m60 = v_xmm0;
    result = HviGetHypervisorFeatures(v_stack_m60, Arg2, Arg3, Arg4);
    if (((v_stack_m60) & (result)) == 0) goto loc_005BED17;
    if (((v_stack_m50) & (0x1000ULL)) != 0) goto loc_005BED17;
    Arg4 = 0;
    v_stack_m97 = 0;
    goto loc_005BED1A;
loc_005BED04:
    result = HviIsAnyHypervisorPresent(v_stack_m60, Arg2, Arg3, Arg4);
    result = (uint8_t)(-(result));
    Arg1 = (uint8_t)((v_stack_m60) & (1));
    v_stack_m97 = (uint8_t)(Arg1);
    goto loc_005BED1A;
loc_005BED17:
loc_005BED1A:
    result = 0;
    Arg1 = 0;
    if (0 < 7) goto loc_005BED88;
    Arg1 = 0;
    if (condition_is_above_or_equal) goto loc_005BED8B;
    Arg2 = (Arg2) << (32);
    result = (7) | (Arg2);
    local_rdi = v_stack_m90;
    if (((2) & ((uint8_t)(result))) != 0) {
        local_rdi = (v_stack_m90) | (512);
        local_r13 = 1;
        local_rdi = (local_rdi) | (1);
        local_rsi = (uint8_t)(local_r13);
        v_stack_m90 = local_rdi;
    }
    if ((((uint8_t)(result)) & (16)) != 0) {
        local_rsi = 1;
        v_stack_m90 = local_rdi;
    }
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_005BED8B;
    local_rdi = (local_rdi) | (512);
    v_stack_m90 = local_rdi;
    goto loc_005BED8B;
loc_005BED88:
    Arg3 = 0;
loc_005BED8B:
    if (((uint8_t)(v_stack_m98)) != 1) goto loc_005BEE17;
    Arg1 = 0;
    if (((uint32_t)((uint32_t)(0x80000000ULL))) < 0x80000008ULL) goto loc_005BEDB2;
    Arg1 = 0;
    goto loc_005BEDB4;
loc_005BEDB2:
    local_rbx = 0;
loc_005BEDB4:
    local_rsi = 1;
    if (!(condition_is_above_or_equal)) {
        local_rdi = (local_rdi) | (4);
        local_rsi = 1;
        v_stack_m90 = local_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        local_rdi = (local_rdi) | (16);
        local_rsi = 1;
        v_stack_m90 = local_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        local_rdi = (local_rdi) | (64);
        local_rsi = 1;
        v_stack_m90 = local_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        v_stack_m90 = local_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        local_rdi = (local_rdi) | (384);
        v_stack_m90 = local_rdi;
    }
    if (!sign_flag) goto loc_005BEE56;
    goto loc_005BEE56;
loc_005BEE17:
    local_rsi = 1;
    if (!(condition_is_above_or_equal)) {
        local_rdi = (local_rdi) | (20);
        local_rsi = 1;
        v_stack_m90 = local_rdi;
    }
    if (!(condition_is_above_or_equal)) {
        local_rdi = (local_rdi) | (68);
        local_rsi = 1;
        v_stack_m90 = local_rdi;
    }
    if (condition_is_above_or_equal) goto loc_005BEE53;
    v_stack_m90 = local_rdi;
    goto loc_005BEE56;
loc_005BEE53:
loc_005BEE56:
    if (((v_stack_m78) & (1)) != 0) goto loc_005BEE65;
    if ((*(uint32_t *)(v_rip + 0xA07FF1)) == 1) {
        local_rdi = (local_rdi) | (32);
        v_stack_m90 = local_rdi;
        Arg1 = (uint8_t)(local_rdi);
    }
    if (((uint8_t)(v_stack_m98)) != 2) goto loc_005BEECB;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x40))) != 6) goto loc_005BEECB;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) == 142) goto loc_005BEE99;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43) - 78)) > 25) goto loc_005BEE93;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43) - 78)) < 25) goto loc_005BEE99;
loc_005BEE93:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) == 158) {
        local_rdi = (local_rdi) | (512);
        v_stack_m90 = local_rdi;
        Arg1 = (uint8_t)(local_rdi);
    }
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43) - 55)) > 55) goto loc_005BEEBB;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43) - 55)) < 55) goto loc_005BEEC1;
loc_005BEEBB:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) == 117) {
        local_rdi = (local_rdi) | (512);
        v_stack_m90 = local_rdi;
        Arg1 = (uint8_t)(local_rdi);
    }
    Arg1 = (uint8_t)((Arg1) & (20));
    if (((uint8_t)(Arg1)) != 20) goto loc_005BEF57;
    if (1 == 0) goto loc_005BEEE8;
    if (((*(uint32_t *)(v_rip + 0x951FDA)) & (0x8000ULL)) == 0) goto loc_005BEF3A;
loc_005BEEE8:
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x6CC))))) != 0) {
        v_stack_m90 = local_rdi;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x6CC)))) & (4)) == 0) goto loc_005BEF1F;
    v_stack_m90 = local_rdi;
    if (((*(uint32_t *)(v_rip + 0x951FAF)) & (0x4000ULL)) != 0) {
        local_rdi = (local_rdi) | (1);
        v_stack_m90 = local_rdi;
    }
    if (((uint8_t)(v_stack_m98)) != 2) goto loc_005BEF3A;
    if (1 != 0) goto loc_005BEF2E;
    if ((uint8_t)(local_r13) == 0) goto loc_005BEF33;
loc_005BEF2E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x6CC)))) & (3)) == 0) goto loc_005BEF57;
loc_005BEF33:
    goto loc_005BEF53;
loc_005BEF3A:
    if (((uint8_t)(v_stack_m98)) != 1) goto loc_005BEF57;
    v_stack_m90 = local_rdi;
    if ((((uint8_t)(local_rdi)) & (64)) == 0) goto loc_005BEF57;
loc_005BEF53:
    v_stack_m90 = local_rdi;
loc_005BEF57:
    Arg1 = (condition_is_below) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
        v_stack_m90 = local_rdi;
    }
    result = KiIsBranchConfusionPresent(Arg1, (uint32_t)(0x3010081ULL), Arg3, 1);
    if ((uint32_t)(result) != 0) {
        v_stack_m90 = local_rdi;
    }
    result = KiIsTsaPresent(Arg1, (uint32_t)(0x3010081ULL), Arg3, 1);
    if ((uint32_t)(result) != 0) {
        v_stack_m90 = local_rdi;
    }
    if (((uint8_t)(v_stack_m98)) != 1) goto loc_005BEFB7;
    if (((*(uint64_t *)(v_rip + 0xA07BAB)) & (0x2000000ULL)) != 0) {
        local_rdi = (local_rdi) | (8);
        v_stack_m90 = local_rdi;
    }
    v_stack_m84 = 0;
    if (((uint8_t)(v_stack_m98)) != 2) goto loc_005BF059;
    if (((uint8_t)(v_stack_m98)) < 2) goto loc_005BEFF5;
    if ((uint8_t)(v_stack_m97) != 0) goto loc_005BEFEE;
    if ((uint8_t)(local_r13) != 0) {
        local_rdi = (local_rdi) | ((uint32_t)(0x10000ULL));
        v_stack_m90 = local_rdi;
    }
    if ((((uint32_t)(0x10000ULL)) & (local_rdi)) == 0) goto loc_005BF056;
    result = (uint32_t)((*(uint64_t *)(v_rip + 0xA07B85)) & (0x8000000ULL));
    if (!(condition_is_equal)) {
        v_stack_m90 = local_rdi;
    }
    if ((*(uint32_t *)(v_rip + 0xA07E6B)) == 0) goto loc_005BF019;
    v_stack_m84 = 3;
    goto loc_005BF056;
loc_005BF019:
    if (result != 0) goto loc_005BF052;
    if ((*(uint8_t *)(arg1 + 0x40)) != 6) goto loc_005BF04A;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x43))) != 151) goto loc_005BF03A;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x42))) == 2) goto loc_005BF052;
    goto loc_005BF048;
loc_005BF03A:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x42))) != 154) goto loc_005BF04A;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x42))) == 3) goto loc_005BF052;
loc_005BF048:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x42))) == 4) goto loc_005BF052;
loc_005BF04A:
    v_stack_m84 = 1;
    if ((uint8_t)(v_stack_m97) != 0) {
        v_stack_m84 = 2;
    }
loc_005BF059:
    if (((*(uint32_t *)(v_rip + 0x951E61)) & ((uint32_t)((uint32_t)(0x10000ULL)))) != 0) {
        local_rdi = (local_rdi) & (0xFFFFFFFFFFFFF7FEULL);
        v_stack_m90 = local_rdi;
    }
    if (((uint8_t)(v_stack_m98)) != 2) goto loc_005BF0CE;
    if (((v_stack_m78) & (*(uint8_t *)(arg1 + 0x42))) == 0) goto loc_005BF0CE;
    if (condition_is_below) goto loc_005BF0CE;
    v_stack_m90 = local_rdi;
    if (condition_is_above_or_equal) goto loc_005BF0CB;
    v_stack_m90 = local_rdi;
    Arg2 = ((uint32_t)(0x3010081ULL)) << (32);
    result = (*(uint64_t *)(v_rip + 0xA07AD8)) | (Arg2);
    if ((((uint8_t)(result)) & (32)) != 0) {
        local_rdi = local_rdi;
        local_rdi = (local_rdi) | (0x180000ULL);
        v_stack_m90 = local_rdi;
    }
loc_005BF0CE:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 1) goto loc_005BF0EE;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) >= 1) {
        v_stack_m90 = local_rdi;
    }
    if (((uint8_t)(v_stack_m98)) == 1) {
        v_stack_m90 = local_rdi;
    }
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) != 2) goto loc_005BF128;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) < 2) goto loc_005BF128;
    v_stack_m90 = local_rdi;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x8D))) < 2) {
        v_stack_m90 = local_rdi;
    }
    *(uint64_t *)(v_stack_m70) = v_xmm0;
    *(uint64_t *)(v_stack_m70 + 0x10) = v_xmm1;
    if (v_stack_m68 != 0) {
        *(uint8_t *)(v_stack_m68) = 1;
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 2, 1);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `8` | `R` |
| `Arg1` | `+ 0x42` | `8` | `R` |
| `Arg1` | `+ 0x43` | `8` | `R` |
| `Arg1` | `+ 0x8D` | `8` | `R` |
| `Arg1` | `+ 0x6CC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BEC4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
