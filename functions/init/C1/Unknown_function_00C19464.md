# sub_00C19464

- RVA: `0x00C19464`–`0x00C1A67B` (길이 `4,631` bytes)
- VA: `0x0000000140C19464`
- 실행 섹션: `INIT`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2B08`
- 디코드: `1,231`개 명령, `4,631/4,631` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00C194C3` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00C1952A` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00C19AC1` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00C19BFB` → [KeKvaShadowingActive](../../text/4B/KeKvaShadowingActive_function_004B2CA8.md) (function, `0x004B2CA8`)
- `0x00C1A468` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00C1A4B5` → [MmGetPhysicalAddress](../../text/23/MmGetPhysicalAddress_function_0023A500.md) (function, `0x0023A500`)
- `0x00C1A675` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) at `0x00BF7DD5`

### Static image references
- `0x00C1948F` → RVA `0x00BEAA60` (`KeGuardDispatchICall`; read)
- `0x00C1949F` → RVA `0x00BEAA70` (`KeGuardCheckICall`; read)
- `0x00C194B2` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00C194DC` → RVA `0x010085E0` (`INITDATA`; read)
- `0x00C194E8` → RVA `0x01008618` (`INITDATA`; read)
- `0x00C194F4` → RVA `0x00FC5060` (`ALMOSTRO`; read)
- `0x00C19500` → RVA `0x010085E8` (`INITDATA`; read)
- `0x00C19C39` → RVA `0x00E0A74C` (`.data`; read)
- `0x00C19E39` → RVA `0x01008088` (`INITDATA`; read)
- `0x00C19FB5` → RVA `0x01008080` (`INITDATA`; read)
- `0x00C1A470` → RVA `0x01008080` (`INITDATA`; write)
- `0x00C1A573` → RVA `0x00BEA8C0` (`KiMceThunk`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00C194C3` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`INIT` → `.text`)
  - `0x00C1952A` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00C19AC1` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00C19BFB` → [KeKvaShadowingActive](../../text/4B/KeKvaShadowingActive_function_004B2CA8.md) (`INIT` → `.text`)
  - `0x00C1A468` → [KeGuardDispatchICall](../../initkdbg/BE/KeGuardDispatchICall_function_00BEAA60.md) (`INIT` → `INITKDBG`)
  - `0x00C1A4B5` → [MmGetPhysicalAddress](../../text/23/MmGetPhysicalAddress_function_0023A500.md) (`INIT` → `.text`)
  - `0x00C1A675` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C19464  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00C19469  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00C1946E  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00C19473  53                              push rbx
00C19474  56                              push rsi
00C19475  57                              push rdi
00C19476  41 54                           push r12
00C19478  41 55                           push r13
00C1947A  41 56                           push r14
00C1947C  41 57                           push r15
00C1947E  48 81 EC F0 00 00 00            sub rsp, 0xf0
00C19485  48 8B F9                        mov rdi, rcx
00C19488  8B CA                           mov ecx, edx
00C1948A  45 85 C9                        test r9d, r9d
00C1948D  74 10                           je 0x140c1949f
00C1948F  48 8D 05 CA 15 FD FF            lea rax, [rip - 0x2ea36]
00C19496  2B C2                           sub eax, edx
00C19498  66 42 C7 04 00 FF E0            mov word ptr [rax + r8], 0xe0ff
00C1949F  48 8D 05 CA 15 FD FF            lea rax, [rip - 0x2ea36]
00C194A6  2B C1                           sub eax, ecx
00C194A8  45 85 C9                        test r9d, r9d
00C194AB  74 05                           je 0x140c194b2
00C194AD  42 C6 04 00 C3                  mov byte ptr [rax + r8], 0xc3
00C194B2  48 8D 1D 47 6B 3E FF            lea rbx, [rip - 0xc194b9]
00C194B9  48 89 9F E8 08 00 00            mov qword ptr [rdi + 0x8e8], rbx
00C194C0  48 8B CB                        mov rcx, rbx
00C194C3  E8 98 A6 82 FF                  call 0x140443b60
00C194C8  48 89 87 F8 08 00 00            mov qword ptr [rdi + 0x8f8], rax
00C194CF  8B 48 50                        mov ecx, dword ptr [rax + 0x50]
00C194D2  48 03 CB                        add rcx, rbx
00C194D5  48 89 8F F0 08 00 00            mov qword ptr [rdi + 0x8f0], rcx
00C194DC  8B 05 FE F0 3E 00               mov eax, dword ptr [rip + 0x3ef0fe]
00C194E2  89 87 CC 08 00 00               mov dword ptr [rdi + 0x8cc], eax
00C194E8  8B 05 2A F1 3E 00               mov eax, dword ptr [rip + 0x3ef12a]
00C194EE  89 87 D0 08 00 00               mov dword ptr [rdi + 0x8d0], eax
00C194F4  8B 05 66 BB 3A 00               mov eax, dword ptr [rip + 0x3abb66]
00C194FA  89 87 D4 08 00 00               mov dword ptr [rdi + 0x8d4], eax
00C19500  4C 8B 0D E1 F0 3E 00            mov r9, qword ptr [rip + 0x3ef0e1]
00C19507  41 83 F9 08                     cmp r9d, 8
00C1950B  0F 85 3F 11 00 00               jne 0x140c1a650
00C19511  44 0F 20 C3                     mov rbx, cr8
00C19515  B8 0F 00 00 00                  mov eax, 0xf
00C1951A  44 0F 22 C0                     mov cr8, rax
00C1951E  48 8B 87 70 04 00 00            mov rax, qword ptr [rdi + 0x470]
00C19525  B9 FE 00 00 00                  mov ecx, 0xfe
00C1952A  E8 31 15 FD FF                  call 0x140beaa60
00C1952F  48 8B 08                        mov rcx, qword ptr [rax]
00C19532  8B 87 D0 08 00 00               mov eax, dword ptr [rdi + 0x8d0]
00C19538  48 8B 0C 08                     mov rcx, qword ptr [rax + rcx]
00C1953C  48 89 8F D8 08 00 00            mov qword ptr [rdi + 0x8d8], rcx
00C19543  0F B6 C3                        movzx eax, bl
00C19546  44 0F 22 C0                     mov cr8, rax
00C1954A  66 C7 87 98 08 00 00 48 CF      mov word ptr [rdi + 0x898], 0xcf48
00C19553  65 48 8B 04 25 18 00 00 00      mov rax, qword ptr gs:[0x18]
00C1955C  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
00C19560  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
00C19568  0F 10 41 10                     movups xmm0, xmmword ptr [rcx + 0x10]
00C1956C  F3 0F 7F 87 68 08 00 00         movdqu xmmword ptr [rdi + 0x868], xmm0
00C19574  0F 10 49 20                     movups xmm1, xmmword ptr [rcx + 0x20]
00C19578  F3 0F 7F 8F 78 08 00 00         movdqu xmmword ptr [rdi + 0x878], xmm1
00C19580  0F 10 81 20 01 00 00            movups xmm0, xmmword ptr [rcx + 0x120]
00C19587  F3 0F 7F 87 88 08 00 00         movdqu xmmword ptr [rdi + 0x888], xmm0
00C1958F  0F 31                           rdtsc
00C19591  48 C1 E2 20                     shl rdx, 0x20
00C19595  48 0B C2                        or rax, rdx
00C19598  48 8B D0                        mov rdx, rax
00C1959B  48 8B C8                        mov rcx, rax
00C1959E  48 C1 C9 03                     ror rcx, 3
00C195A2  48 33 D1                        xor rdx, rcx
00C195A5  49 B8 01 20 00 04 80 00 10 70   movabs r8, 0x7010008004002001
00C195AF  49 8B C0                        mov rax, r8
00C195B2  48 F7 E2                        mul rdx
00C195B5  48 8B DA                        mov rbx, rdx
00C195B8  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
00C195C0  48 33 D8                        xor rbx, rax
00C195C3  48 B8 A3 8B 2E BA E8 A2 8B 2E   movabs rax, 0x2e8ba2e8ba2e8ba3
00C195CD  48 F7 E3                        mul rbx
00C195D0  48 D1 EA                        shr rdx, 1
00C195D3  48 6B C2 0B                     imul rax, rdx, 0xb
00C195D7  48 2B D8                        sub rbx, rax
00C195DA  83 FB 05                        cmp ebx, 5
00C195DD  0F 87 72 02 00 00               ja 0x140c19855
00C195E3  BE AB AA AA AA                  mov esi, 0xaaaaaaab
00C195E8  8B CB                           mov ecx, ebx
00C195EA  0F 84 F8 01 00 00               je 0x140c197e8
00C195F0  8B C3                           mov eax, ebx
00C195F2  85 DB                           test ebx, ebx
00C195F4  0F 84 87 01 00 00               je 0x140c19781
00C195FA  83 E8 01                        sub eax, 1
00C195FD  0F 84 1D 01 00 00               je 0x140c19720
00C19603  83 E8 01                        sub eax, 1
00C19606  0F 84 C1 00 00 00               je 0x140c196cd
00C1960C  83 F8 01                        cmp eax, 1
00C1960F  8B C6                           mov eax, esi
00C19611  74 6F                           je 0x140c19682
00C19613  F7 E3                           mul ebx
00C19615  D1 EA                           shr edx, 1
00C19617  8D 04 52                        lea eax, [rdx + rdx*2]
00C1961A  2B C8                           sub ecx, eax
00C1961C  74 35                           je 0x140c19653
00C1961E  B8 46 49 76 70                  mov eax, 0x70764946
00C19623  83 F9 01                        cmp ecx, 1
00C19626  8B CB                           mov ecx, ebx
00C19628  74 13                           je 0x140c1963d
00C1962A  D3 C0                           rol eax, cl
00C1962C  89 84 24 48 01 00 00            mov dword ptr [rsp + 0x148], eax
00C19633  44 8B 8C 24 48 01 00 00         mov r9d, dword ptr [rsp + 0x148]
00C1963B  EB 37                           jmp 0x140c19674
00C1963D  D3 C8                           ror eax, cl
00C1963F  89 84 24 48 01 00 00            mov dword ptr [rsp + 0x148], eax
00C19646  44 8B 8C 24 48 01 00 00         mov r9d, dword ptr [rsp + 0x148]
00C1964E  41 D3 C1                        rol r9d, cl
00C19651  EB 24                           jmp 0x140c19677
00C19653  8D 43 02                        lea eax, [rbx + 2]
00C19656  8D 0C 40                        lea ecx, [rax + rax*2]
00C19659  B8 46 49 76 70                  mov eax, 0x70764946
00C1965E  D3 C0                           rol eax, cl
00C19660  33 C3                           xor eax, ebx
00C19662  89 84 24 48 01 00 00            mov dword ptr [rsp + 0x148], eax
00C19669  44 8B 8C 24 48 01 00 00         mov r9d, dword ptr [rsp + 0x148]
00C19671  44 33 CB                        xor r9d, ebx
00C19674  41 D3 C9                        ror r9d, cl
00C19677  41 BD 4E 74 46 57               mov r13d, 0x5746744e
00C1967D  E9 19 04 00 00                  jmp 0x140c19a9b
00C19682  F7 E3                           mul ebx
00C19684  D1 EA                           shr edx, 1
00C19686  8D 04 52                        lea eax, [rdx + rdx*2]
00C19689  2B C8                           sub ecx, eax
00C1968B  74 26                           je 0x140c196b3
00C1968D  B8 44 50 77 72                  mov eax, 0x72775044
00C19692  83 F9 01                        cmp ecx, 1
00C19695  8B CB                           mov ecx, ebx
00C19697  74 0D                           je 0x140c196a6
00C19699  D3 C0                           rol eax, cl
00C1969B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00C1969F  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
00C196A4  EB CE                           jmp 0x140c19674
00C196A6  D3 C8                           ror eax, cl
00C196A8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00C196AC  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
00C196B1  EB 9B                           jmp 0x140c1964e
00C196B3  8D 43 02                        lea eax, [rbx + 2]
00C196B6  8D 0C 40                        lea ecx, [rax + rax*2]
00C196B9  B8 44 50 77 72                  mov eax, 0x72775044
00C196BE  D3 C0                           rol eax, cl
00C196C0  33 C3                           xor eax, ebx
00C196C2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00C196C6  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
00C196CB  EB A4                           jmp 0x140c19671
00C196CD  8B C6                           mov eax, esi
00C196CF  F7 E3                           mul ebx
00C196D1  D1 EA                           shr edx, 1
00C196D3  8D 04 52                        lea eax, [rdx + rdx*2]
00C196D6  2B C8                           sub ecx, eax
00C196D8  74 29                           je 0x140c19703
00C196DA  B8 43 64 6D 61                  mov eax, 0x616d6443
00C196DF  83 F9 01                        cmp ecx, 1
00C196E2  8B CB                           mov ecx, ebx
00C196E4  74 0D                           je 0x140c196f3
00C196E6  D3 C0                           rol eax, cl
00C196E8  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00C196EC  44 8B 4C 24 34                  mov r9d, dword ptr [rsp + 0x34]
00C196F1  EB 81                           jmp 0x140c19674
00C196F3  D3 C8                           ror eax, cl
00C196F5  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00C196F9  44 8B 4C 24 34                  mov r9d, dword ptr [rsp + 0x34]
00C196FE  E9 4B FF FF FF                  jmp 0x140c1964e
00C19703  8D 43 02                        lea eax, [rbx + 2]
00C19706  8D 0C 40                        lea ecx, [rax + rax*2]
00C19709  B8 43 64 6D 61                  mov eax, 0x616d6443
00C1970E  D3 C0                           rol eax, cl
00C19710  33 C3                           xor eax, ebx
00C19712  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00C19716  44 8B 4C 24 34                  mov r9d, dword ptr [rsp + 0x34]
00C1971B  E9 51 FF FF FF                  jmp 0x140c19671
00C19720  8B C6                           mov eax, esi
00C19722  F7 E3                           mul ebx
00C19724  D1 EA                           shr edx, 1
00C19726  8D 04 52                        lea eax, [rdx + rdx*2]
00C19729  2B C8                           sub ecx, eax
00C1972B  41 BC 43 63 5A 65               mov r12d, 0x655a6343
00C19731  74 27                           je 0x140c1975a
00C19733  41 8B C4                        mov eax, r12d
00C19736  83 F9 01                        cmp ecx, 1
00C19739  8B CB                           mov ecx, ebx
00C1973B  74 0D                           je 0x140c1974a
00C1973D  D3 C0                           rol eax, cl
00C1973F  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00C19743  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
00C19748  EB 29                           jmp 0x140c19773
00C1974A  D3 C8                           ror eax, cl
00C1974C  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00C19750  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
00C19755  41 D3 C1                        rol r9d, cl
00C19758  EB 1C                           jmp 0x140c19776
00C1975A  8D 43 02                        lea eax, [rbx + 2]
00C1975D  8D 0C 40                        lea ecx, [rax + rax*2]
00C19760  41 8B C4                        mov eax, r12d
00C19763  D3 C0                           rol eax, cl
00C19765  33 C3                           xor eax, ebx
00C19767  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00C1976B  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
00C19770  44 33 CB                        xor r9d, ebx
00C19773  41 D3 C9                        ror r9d, cl
00C19776  41 BD 4E 74 46 57               mov r13d, 0x5746744e
00C1977C  E9 20 03 00 00                  jmp 0x140c19aa1
00C19781  8B C6                           mov eax, esi
00C19783  F7 E3                           mul ebx
00C19785  D1 EA                           shr edx, 1
00C19787  8D 04 52                        lea eax, [rdx + rdx*2]
00C1978A  2B C8                           sub ecx, eax
00C1978C  41 BF 43 63 42 63               mov r15d, 0x63426343
00C19792  74 27                           je 0x140c197bb
00C19794  41 8B C7                        mov eax, r15d
00C19797  83 F9 01                        cmp ecx, 1
00C1979A  8B CB                           mov ecx, ebx
00C1979C  74 0D                           je 0x140c197ab
00C1979E  D3 C0                           rol eax, cl
00C197A0  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00C197A4  44 8B 4C 24 3C                  mov r9d, dword ptr [rsp + 0x3c]
00C197A9  EB 29                           jmp 0x140c197d4
00C197AB  D3 C8                           ror eax, cl
00C197AD  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00C197B1  44 8B 4C 24 3C                  mov r9d, dword ptr [rsp + 0x3c]
00C197B6  41 D3 C1                        rol r9d, cl
00C197B9  EB 1C                           jmp 0x140c197d7
00C197BB  8D 43 02                        lea eax, [rbx + 2]
00C197BE  8D 0C 40                        lea ecx, [rax + rax*2]
00C197C1  41 8B C7                        mov eax, r15d
00C197C4  D3 C0                           rol eax, cl
00C197C6  33 C3                           xor eax, ebx
00C197C8  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00C197CC  44 8B 4C 24 3C                  mov r9d, dword ptr [rsp + 0x3c]
00C197D1  44 33 CB                        xor r9d, ebx
00C197D4  41 D3 C9                        ror r9d, cl
00C197D7  41 BC 43 63 5A 65               mov r12d, 0x655a6343
00C197DD  41 BD 4E 74 46 57               mov r13d, 0x5746744e
00C197E3  E9 BF 02 00 00                  jmp 0x140c19aa7
00C197E8  8B C6                           mov eax, esi
00C197EA  F7 E3                           mul ebx
00C197EC  D1 EA                           shr edx, 1
00C197EE  8D 04 52                        lea eax, [rdx + rdx*2]
00C197F1  2B C8                           sub ecx, eax
00C197F3  41 BE 4F 62 44 69               mov r14d, 0x6944624f
00C197F9  74 27                           je 0x140c19822
00C197FB  41 8B C6                        mov eax, r14d
00C197FE  83 F9 01                        cmp ecx, 1
00C19801  8B CB                           mov ecx, ebx
00C19803  74 0D                           je 0x140c19812
00C19805  D3 C0                           rol eax, cl
00C19807  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00C1980B  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
00C19810  EB 29                           jmp 0x140c1983b
00C19812  D3 C8                           ror eax, cl
00C19814  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00C19818  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
00C1981D  41 D3 C1                        rol r9d, cl
00C19820  EB 1C                           jmp 0x140c1983e
00C19822  8D 43 02                        lea eax, [rbx + 2]
00C19825  8D 0C 40                        lea ecx, [rax + rax*2]
00C19828  41 8B C6                        mov eax, r14d
00C1982B  D3 C0                           rol eax, cl
00C1982D  33 C3                           xor eax, ebx
00C1982F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00C19833  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
00C19838  44 33 CB                        xor r9d, ebx
00C1983B  41 D3 C9                        ror r9d, cl
00C1983E  41 BC 43 63 5A 65               mov r12d, 0x655a6343
00C19844  41 BF 43 63 42 63               mov r15d, 0x63426343
00C1984A  41 BD 4E 74 46 57               mov r13d, 0x5746744e
00C19850  E9 58 02 00 00                  jmp 0x140c19aad
00C19855  8B C3                           mov eax, ebx
00C19857  83 E8 06                        sub eax, 6
00C1985A  0F 84 DE 01 00 00               je 0x140c19a3e
00C19860  83 E8 01                        sub eax, 1
00C19863  0F 84 78 01 00 00               je 0x140c199e1
00C19869  83 E8 01                        sub eax, 1
00C1986C  0F 84 12 01 00 00               je 0x140c19984
00C19872  83 F8 01                        cmp eax, 1
00C19875  0F 84 AC 00 00 00               je 0x140c19927
00C1987B  0F 31                           rdtsc
00C1987D  48 C1 E2 20                     shl rdx, 0x20
00C19881  48 0B C2                        or rax, rdx
00C19884  48 8B D0                        mov rdx, rax
00C19887  48 8B C8                        mov rcx, rax
00C1988A  48 C1 C9 03                     ror rcx, 3
00C1988E  48 33 D1                        xor rdx, rcx
00C19891  49 8B C0                        mov rax, r8
00C19894  48 F7 E2                        mul rdx
00C19897  48 89 94 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdx
00C1989F  4C 8B C8                        mov r9, rax
00C198A2  44 33 CA                        xor r9d, edx
00C198A5  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00C198AA  41 F7 E1                        mul r9d
00C198AD  C1 EA 03                        shr edx, 3
00C198B0  6B CA 1A                        imul ecx, edx, 0x1a
00C198B3  41 8B D9                        mov ebx, r9d
00C198B6  2B D9                           sub ebx, ecx
00C198B8  83 C3 61                        add ebx, 0x61
00C198BB  41 C1 E9 05                     shr r9d, 5
00C198BF  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00C198C4  41 F7 E1                        mul r9d
00C198C7  C1 EA 03                        shr edx, 3
00C198CA  6B C2 1A                        imul eax, edx, 0x1a
00C198CD  45 8B C1                        mov r8d, r9d
00C198D0  44 2B C0                        sub r8d, eax
00C198D3  41 83 C0 41                     add r8d, 0x41
00C198D7  C1 E3 08                        shl ebx, 8
00C198DA  44 0B C3                        or r8d, ebx
00C198DD  41 C1 E9 05                     shr r9d, 5
00C198E1  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00C198E6  41 F7 E1                        mul r9d
00C198E9  C1 EA 03                        shr edx, 3
00C198EC  6B C2 1A                        imul eax, edx, 0x1a
00C198EF  41 8B C9                        mov ecx, r9d
00C198F2  2B C8                           sub ecx, eax
00C198F4  83 C1 61                        add ecx, 0x61
00C198F7  41 C1 E0 08                     shl r8d, 8
00C198FB  41 0B C8                        or ecx, r8d
00C198FE  41 C1 E9 05                     shr r9d, 5
00C19902  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00C19907  41 F7 E1                        mul r9d
00C1990A  C1 EA 03                        shr edx, 3
00C1990D  6B C2 1A                        imul eax, edx, 0x1a
00C19910  44 2B C8                        sub r9d, eax
00C19913  41 83 C1 41                     add r9d, 0x41
00C19917  C1 E1 08                        shl ecx, 8
00C1991A  44 0B C9                        or r9d, ecx
00C1991D  BE AB AA AA AA                  mov esi, 0xaaaaaaab
00C19922  E9 50 FD FF FF                  jmp 0x140c19677
00C19927  BE AB AA AA AA                  mov esi, 0xaaaaaaab
00C1992C  8B C6                           mov eax, esi
00C1992E  F7 E3                           mul ebx
00C19930  D1 EA                           shr edx, 1
00C19932  8D 04 52                        lea eax, [rdx + rdx*2]
00C19935  8B CB                           mov ecx, ebx
00C19937  2B C8                           sub ecx, eax
00C19939  74 2C                           je 0x140c19967
00C1993B  B8 46 4F 43 58                  mov eax, 0x58434f46
00C19940  83 F9 01                        cmp ecx, 1
00C19943  8B CB                           mov ecx, ebx
00C19945  74 10                           je 0x140c19957
00C19947  D3 C0                           rol eax, cl
00C19949  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00C1994D  44 8B 4C 24 44                  mov r9d, dword ptr [rsp + 0x44]
00C19952  E9 1D FD FF FF                  jmp 0x140c19674
00C19957  D3 C8                           ror eax, cl
00C19959  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00C1995D  44 8B 4C 24 44                  mov r9d, dword ptr [rsp + 0x44]
00C19962  E9 E7 FC FF FF                  jmp 0x140c1964e
00C19967  8D 43 02                        lea eax, [rbx + 2]
00C1996A  8D 0C 40                        lea ecx, [rax + rax*2]
00C1996D  B8 46 4F 43 58                  mov eax, 0x58434f46
00C19972  D3 C0                           rol eax, cl
00C19974  33 C3                           xor eax, ebx
00C19976  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00C1997A  44 8B 4C 24 44                  mov r9d, dword ptr [rsp + 0x44]
00C1997F  E9 ED FC FF FF                  jmp 0x140c19671
00C19984  BE AB AA AA AA                  mov esi, 0xaaaaaaab
00C19989  8B C6                           mov eax, esi
00C1998B  F7 E3                           mul ebx
00C1998D  D1 EA                           shr edx, 1
00C1998F  8D 04 52                        lea eax, [rdx + rdx*2]
00C19992  8B CB                           mov ecx, ebx
00C19994  2B C8                           sub ecx, eax
00C19996  74 2C                           je 0x140c199c4
00C19998  B8 41 66 64 42                  mov eax, 0x42646641
00C1999D  83 F9 01                        cmp ecx, 1
00C199A0  8B CB                           mov ecx, ebx
00C199A2  74 10                           je 0x140c199b4
00C199A4  D3 C0                           rol eax, cl
00C199A6  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00C199AA  44 8B 4C 24 48                  mov r9d, dword ptr [rsp + 0x48]
00C199AF  E9 C0 FC FF FF                  jmp 0x140c19674
00C199B4  D3 C8                           ror eax, cl
00C199B6  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00C199BA  44 8B 4C 24 48                  mov r9d, dword ptr [rsp + 0x48]
00C199BF  E9 8A FC FF FF                  jmp 0x140c1964e
00C199C4  8D 43 02                        lea eax, [rbx + 2]
00C199C7  8D 0C 40                        lea ecx, [rax + rax*2]
00C199CA  B8 41 66 64 42                  mov eax, 0x42646641
00C199CF  D3 C0                           rol eax, cl
00C199D1  33 C3                           xor eax, ebx
00C199D3  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00C199D7  44 8B 4C 24 48                  mov r9d, dword ptr [rsp + 0x48]
00C199DC  E9 90 FC FF FF                  jmp 0x140c19671
00C199E1  BE AB AA AA AA                  mov esi, 0xaaaaaaab
00C199E6  8B C6                           mov eax, esi
00C199E8  F7 E3                           mul ebx
00C199EA  D1 EA                           shr edx, 1
00C199EC  8D 04 52                        lea eax, [rdx + rdx*2]
00C199EF  8B CB                           mov ecx, ebx
00C199F1  2B C8                           sub ecx, eax
00C199F3  74 2C                           je 0x140c19a21
00C199F5  B8 41 6C 53 63                  mov eax, 0x63536c41
00C199FA  83 F9 01                        cmp ecx, 1
00C199FD  8B CB                           mov ecx, ebx
00C199FF  74 10                           je 0x140c19a11
00C19A01  D3 C0                           rol eax, cl
00C19A03  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
00C19A07  44 8B 4C 24 4C                  mov r9d, dword ptr [rsp + 0x4c]
00C19A0C  E9 63 FC FF FF                  jmp 0x140c19674
00C19A11  D3 C8                           ror eax, cl
00C19A13  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
00C19A17  44 8B 4C 24 4C                  mov r9d, dword ptr [rsp + 0x4c]
00C19A1C  E9 2D FC FF FF                  jmp 0x140c1964e
00C19A21  8D 43 02                        lea eax, [rbx + 2]
00C19A24  8D 0C 40                        lea ecx, [rax + rax*2]
00C19A27  B8 41 6C 53 63                  mov eax, 0x63536c41
00C19A2C  D3 C0                           rol eax, cl
00C19A2E  33 C3                           xor eax, ebx
00C19A30  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
00C19A34  44 8B 4C 24 4C                  mov r9d, dword ptr [rsp + 0x4c]
00C19A39  E9 33 FC FF FF                  jmp 0x140c19671
00C19A3E  BE AB AA AA AA                  mov esi, 0xaaaaaaab
00C19A43  8B C6                           mov eax, esi
00C19A45  F7 E3                           mul ebx
00C19A47  D1 EA                           shr edx, 1
00C19A49  8D 04 52                        lea eax, [rdx + rdx*2]
00C19A4C  8B CB                           mov ecx, ebx
00C19A4E  2B C8                           sub ecx, eax
00C19A50  41 BD 4E 74 46 57               mov r13d, 0x5746744e
00C19A56  74 27                           je 0x140c19a7f
00C19A58  41 8B C5                        mov eax, r13d
00C19A5B  83 F9 01                        cmp ecx, 1
00C19A5E  8B CB                           mov ecx, ebx
00C19A60  74 0D                           je 0x140c19a6f
00C19A62  D3 C0                           rol eax, cl
00C19A64  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00C19A68  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
00C19A6D  EB 29                           jmp 0x140c19a98
00C19A6F  D3 C8                           ror eax, cl
00C19A71  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00C19A75  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
00C19A7A  41 D3 C1                        rol r9d, cl
00C19A7D  EB 1C                           jmp 0x140c19a9b
00C19A7F  8D 43 02                        lea eax, [rbx + 2]
00C19A82  8D 0C 40                        lea ecx, [rax + rax*2]
00C19A85  41 8B C5                        mov eax, r13d
00C19A88  D3 C0                           rol eax, cl
00C19A8A  33 C3                           xor eax, ebx
00C19A8C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00C19A90  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
00C19A95  44 33 CB                        xor r9d, ebx
00C19A98  41 D3 C9                        ror r9d, cl
00C19A9B  41 BC 43 63 5A 65               mov r12d, 0x655a6343
00C19AA1  41 BF 43 63 42 63               mov r15d, 0x63426343
00C19AA7  41 BE 4F 62 44 69               mov r14d, 0x6944624f
00C19AAD  48 8B 87 00 01 00 00            mov rax, qword ptr [rdi + 0x100]
00C19AB4  45 8B C1                        mov r8d, r9d
00C19AB7  BA B0 01 00 00                  mov edx, 0x1b0
00C19ABC  B9 40 00 00 00                  mov ecx, 0x40
00C19AC1  E8 9A 0F FD FF                  call 0x140beaa60
00C19AC6  48 89 87 00 09 00 00            mov qword ptr [rdi + 0x900], rax
00C19ACD  48 85 C0                        test rax, rax
00C19AD0  0F 84 64 0B 00 00               je 0x140c1a63a
00C19AD6  48 83 E8 80                     sub rax, -0x80
00C19ADA  48 83 E0 80                     and rax, 0xffffffffffffff80
00C19ADE  48 89 87 00 09 00 00            mov qword ptr [rdi + 0x900], rax
00C19AE5  C7 87 9C 08 00 00 0F 05 48 87   mov dword ptr [rdi + 0x89c], 0x8748050f
00C19AEF  C7 87 A0 08 00 00 0C 24 81 64   mov dword ptr [rdi + 0x8a0], 0x6481240c
00C19AF9  C7 87 A4 08 00 00 24 10 FF FE   mov dword ptr [rdi + 0x8a4], 0xfeff1024
00C19B03  C7 87 A8 08 00 00 FF FF 48 CF   mov dword ptr [rdi + 0x8a8], 0xcf48ffff
00C19B0D  C6 87 9A 08 00 00 C3            mov byte ptr [rdi + 0x89a], 0xc3
00C19B14  4C 8B 87 E0 07 00 00            mov r8, qword ptr [rdi + 0x7e0]
00C19B1B  45 33 DB                        xor r11d, r11d
00C19B1E  48 8B 8F 78 06 00 00            mov rcx, qword ptr [rdi + 0x678]
00C19B25  8A 87 80 06 00 00               mov al, byte ptr [rdi + 0x680]
00C19B2B  41 38 04 08                     cmp byte ptr [r8 + rcx], al
00C19B2F  0F 85 B5 00 00 00               jne 0x140c19bea
00C19B35  33 C0                           xor eax, eax
00C19B37  33 C9                           xor ecx, ecx
00C19B39  0F A2                           cpuid
00C19B3B  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00C19B42  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00C19B49  89 8C 24 88 00 00 00            mov dword ptr [rsp + 0x88], ecx
00C19B50  89 94 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], edx
00C19B57  48 8B 8F 70 06 00 00            mov rcx, qword ptr [rdi + 0x670]
00C19B5E  45 8A 0C 08                     mov r9b, byte ptr [r8 + rcx]
00C19B62  48 8B 8F 68 06 00 00            mov rcx, qword ptr [rdi + 0x668]
00C19B69  45 8A 14 08                     mov r10b, byte ptr [r8 + rcx]
00C19B6D  83 F8 07                        cmp eax, 7
00C19B70  72 32                           jb 0x140c19ba4
00C19B72  41 8D 43 07                     lea eax, [r11 + 7]
00C19B76  33 C9                           xor ecx, ecx
00C19B78  0F A2                           cpuid
00C19B7A  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00C19B81  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00C19B88  89 8C 24 88 00 00 00            mov dword ptr [rsp + 0x88], ecx
00C19B8F  89 94 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], edx
00C19B96  0F BA E3 0B                     bt ebx, 0xb
00C19B9A  41 8D 5B 01                     lea ebx, [r11 + 1]
00C19B9E  44 0F 42 DB                     cmovb r11d, ebx
00C19BA2  EB 05                           jmp 0x140c19ba9
00C19BA4  BB 01 00 00 00                  mov ebx, 1
00C19BA9  48 8B 87 60 06 00 00            mov rax, qword ptr [rdi + 0x660]
00C19BB0  41 80 3C 00 06                  cmp byte ptr [r8 + rax], 6
00C19BB5  75 38                           jne 0x140c19bef
00C19BB7  41 80 F9 3C                     cmp r9b, 0x3c
00C19BBB  75 06                           jne 0x140c19bc3
00C19BBD  41 80 FA 03                     cmp r10b, 3
00C19BC1  74 22                           je 0x140c19be5
00C19BC3  41 80 F9 3F                     cmp r9b, 0x3f
00C19BC7  75 06                           jne 0x140c19bcf
00C19BC9  41 80 FA 02                     cmp r10b, 2
00C19BCD  74 16                           je 0x140c19be5
00C19BCF  41 80 F9 45                     cmp r9b, 0x45
00C19BD3  75 05                           jne 0x140c19bda
00C19BD5  44 3A D3                        cmp r10b, bl
00C19BD8  74 0B                           je 0x140c19be5
00C19BDA  41 80 F9 46                     cmp r9b, 0x46
00C19BDE  75 0F                           jne 0x140c19bef
00C19BE0  44 3A D3                        cmp r10b, bl
00C19BE3  75 0A                           jne 0x140c19bef
00C19BE5  45 33 DB                        xor r11d, r11d
00C19BE8  EB 05                           jmp 0x140c19bef
00C19BEA  BB 01 00 00 00                  mov ebx, 1
00C19BEF  45 85 DB                        test r11d, r11d
00C19BF2  74 07                           je 0x140c19bfb
00C19BF4  80 8F 9B 08 00 00 04            or byte ptr [rdi + 0x89b], 4
00C19BFB  E8 A8 90 89 FF                  call 0x1404b2ca8
00C19C00  85 C0                           test eax, eax
00C19C02  74 07                           je 0x140c19c0b
00C19C04  80 8F 9B 08 00 00 08            or byte ptr [rdi + 0x89b], 8
00C19C0B  C7 87 AC 08 00 00 48 83 2C 24   mov dword ptr [rdi + 0x8ac], 0x242c8348
00C19C15  66 C7 87 B0 08 00 00 02 48      mov word ptr [rdi + 0x8b0], 0x4802
00C19C1E  C6 87 B2 08 00 00 CF            mov byte ptr [rdi + 0x8b2], 0xcf
00C19C25  48 B8 89 02 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000289
00C19C2F  45 33 DB                        xor r11d, r11d
00C19C32  44 38 18                        cmp byte ptr [rax], r11b
00C19C35  41 0F 95 C3                     setne r11b
00C19C39  8B 05 0D 0B 1F 00               mov eax, dword ptr [rip + 0x1f0b0d]
00C19C3F  25 00 00 00 F0                  and eax, 0xf0000000
00C19C44  3D 00 00 00 C0                  cmp eax, 0xc0000000
00C19C49  44 0F 44 DB                     cmove r11d, ebx
00C19C4D  4C 8D 87 D8 09 00 00            lea r8, [rdi + 0x9d8]
00C19C54  41 F7 00 00 00 00 08            test dword ptr [r8], 0x8000000
00C19C5B  0F 85 C4 01 00 00               jne 0x140c19e25
00C19C61  8B 8F 0C 08 00 00               mov ecx, dword ptr [rdi + 0x80c]
00C19C67  8B C1                           mov eax, ecx
00C19C69  F7 D8                           neg eax
00C19C6B  89 44 39 0B                     mov dword ptr [rcx + rdi + 0xb], eax
00C19C6F  0F 31                           rdtsc
00C19C71  48 C1 E2 20                     shl rdx, 0x20
00C19C75  48 0B C2                        or rax, rdx
00C19C78  48 8B D0                        mov rdx, rax
00C19C7B  48 8B C8                        mov rcx, rax
00C19C7E  48 C1 C9 03                     ror rcx, 3
00C19C82  48 33 D1                        xor rdx, rcx
00C19C85  49 B9 01 20 00 04 80 00 10 70   movabs r9, 0x7010008004002001
00C19C8F  49 8B C1                        mov rax, r9
00C19C92  48 F7 E2                        mul rdx
00C19C95  48 8B CA                        mov rcx, rdx
00C19C98  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
00C19CA0  49 8B D8                        mov rbx, r8
00C19CA3  48 33 C8                        xor rcx, rax
00C19CA6  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
00C19CB0  48 F7 E1                        mul rcx
00C19CB3  48 C1 EA 03                     shr rdx, 3
00C19CB7  48 8D 04 92                     lea rax, [rdx + rdx*4]
00C19CBB  48 03 C0                        add rax, rax
00C19CBE  48 2B C8                        sub rcx, rax
00C19CC1  41 BA 00 80 00 40               mov r10d, 0x40008000
00C19CC7  48 83 F9 01                     cmp rcx, 1
00C19CCB  73 1C                           jae 0x140c19ce9
00C19CCD  45 85 10                        test dword ptr [r8], r10d
00C19CD0  75 17                           jne 0x140c19ce9
00C19CD2  83 BF 58 08 00 00 07            cmp dword ptr [rdi + 0x858], 7
00C19CD9  74 0E                           je 0x140c19ce9
00C19CDB  80 8F 9B 08 00 00 01            or byte ptr [rdi + 0x89b], 1
00C19CE2  48 8D 9F D8 09 00 00            lea rbx, [rdi + 0x9d8]
00C19CE9  0F 31                           rdtsc
00C19CEB  48 C1 E2 20                     shl rdx, 0x20
00C19CEF  48 0B C2                        or rax, rdx
00C19CF2  48 8B D0                        mov rdx, rax
00C19CF5  48 8B C8                        mov rcx, rax
00C19CF8  48 C1 C9 03                     ror rcx, 3
00C19CFC  48 33 D1                        xor rdx, rcx
00C19CFF  49 8B C1                        mov rax, r9
00C19D02  48 F7 E2                        mul rdx
00C19D05  48 8B CA                        mov rcx, rdx
00C19D08  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
00C19D10  4C 8B CB                        mov r9, rbx
00C19D13  48 33 C8                        xor rcx, rax
00C19D16  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
00C19D20  48 F7 E1                        mul rcx
00C19D23  48 C1 EA 03                     shr rdx, 3
00C19D27  48 8D 04 92                     lea rax, [rdx + rdx*4]
00C19D2B  48 03 C0                        add rax, rax
00C19D2E  48 2B C8                        sub rcx, rax
00C19D31  48 83 F9 01                     cmp rcx, 1
00C19D35  73 1C                           jae 0x140c19d53
00C19D37  45 85 10                        test dword ptr [r8], r10d
00C19D3A  75 17                           jne 0x140c19d53
00C19D3C  83 BF 58 08 00 00 07            cmp dword ptr [rdi + 0x858], 7
00C19D43  74 0E                           je 0x140c19d53
00C19D45  80 8F 9B 08 00 00 02            or byte ptr [rdi + 0x89b], 2
00C19D4C  4C 8D 8F D8 09 00 00            lea r9, [rdi + 0x9d8]
00C19D53  0F 31                           rdtsc
00C19D55  48 C1 E2 20                     shl rdx, 0x20
00C19D59  48 0B C2                        or rax, rdx
00C19D5C  48 8B D0                        mov rdx, rax
00C19D5F  48 8B C8                        mov rcx, rax
00C19D62  48 C1 C9 03                     ror rcx, 3
00C19D66  48 33 D1                        xor rdx, rcx
00C19D69  49 B8 01 20 00 04 80 00 10 70   movabs r8, 0x7010008004002001
00C19D73  49 8B C0                        mov rax, r8
00C19D76  48 F7 E2                        mul rdx
00C19D79  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
00C19D81  32 D0                           xor dl, al
00C19D83  F6 C2 03                        test dl, 3
00C19D86  75 1F                           jne 0x140c19da7
00C19D88  8B 03                           mov eax, dword ptr [rbx]
00C19D8A  49 8B D9                        mov rbx, r9
00C19D8D  41 85 C2                        test r10d, eax
00C19D90  75 15                           jne 0x140c19da7
00C19D92  45 85 DB                        test r11d, r11d
00C19D95  74 10                           je 0x140c19da7
00C19D97  83 BF 58 08 00 00 07            cmp dword ptr [rdi + 0x858], 7
00C19D9E  74 07                           je 0x140c19da7
00C19DA0  80 8F 9B 08 00 00 20            or byte ptr [rdi + 0x89b], 0x20
00C19DA7  0F 31                           rdtsc
00C19DA9  48 C1 E2 20                     shl rdx, 0x20
00C19DAD  48 0B C2                        or rax, rdx
00C19DB0  48 8B D0                        mov rdx, rax
00C19DB3  48 8B C8                        mov rcx, rax
00C19DB6  48 C1 C9 03                     ror rcx, 3
00C19DBA  48 33 D1                        xor rdx, rcx
00C19DBD  49 8B C0                        mov rax, r8
00C19DC0  48 F7 E2                        mul rdx
00C19DC3  48 8B CA                        mov rcx, rdx
00C19DC6  48 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdx
00C19DCE  4C 8B C3                        mov r8, rbx
00C19DD1  48 33 C8                        xor rcx, rax
00C19DD4  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
00C19DDE  48 F7 E1                        mul rcx
00C19DE1  48 C1 EA 03                     shr rdx, 3
00C19DE5  48 8D 04 92                     lea rax, [rdx + rdx*4]
00C19DE9  48 03 C0                        add rax, rax
00C19DEC  48 2B C8                        sub rcx, rax
00C19DEF  48 83 F9 01                     cmp rcx, 1
00C19DF3  73 2B                           jae 0x140c19e20
00C19DF5  44 85 13                        test dword ptr [rbx], r10d
00C19DF8  75 26                           jne 0x140c19e20
00C19DFA  45 85 DB                        test r11d, r11d
00C19DFD  74 21                           je 0x140c19e20
00C19DFF  BB 01 00 00 00                  mov ebx, 1
00C19E04  49 BA CD CC CC CC CC CC CC CC   movabs r10, 0xcccccccccccccccd
00C19E0E  83 BF 58 08 00 00 07            cmp dword ptr [rdi + 0x858], 7
00C19E15  74 18                           je 0x140c19e2f
00C19E17  80 8F 9B 08 00 00 10            or byte ptr [rdi + 0x89b], 0x10
00C19E1E  EB 0F                           jmp 0x140c19e2f
00C19E20  BB 01 00 00 00                  mov ebx, 1
00C19E25  49 BA CD CC CC CC CC CC CC CC   movabs r10, 0xcccccccccccccccd
00C19E2F  49 BB 01 20 00 04 80 00 10 70   movabs r11, 0x7010008004002001
00C19E39  83 3D 48 E2 3E 00 00            cmp dword ptr [rip + 0x3ee248], 0
00C19E40  0F 84 C5 00 00 00               je 0x140c19f0b
00C19E46  45 8B 08                        mov r9d, dword ptr [r8]
00C19E49  41 0F BA E1 1B                  bt r9d, 0x1b
00C19E4E  0F 82 B7 00 00 00               jb 0x140c19f0b
00C19E54  0F 31                           rdtsc
00C19E56  48 C1 E2 20                     shl rdx, 0x20
00C19E5A  48 0B C2                        or rax, rdx
00C19E5D  48 8B D0                        mov rdx, rax
00C19E60  48 8B C8                        mov rcx, rax
00C19E63  48 C1 C9 03                     ror rcx, 3
00C19E67  48 33 D1                        xor rdx, rcx
00C19E6A  49 8B C3                        mov rax, r11
00C19E6D  48 F7 E2                        mul rdx
00C19E70  48 8B CA                        mov rcx, rdx
00C19E73  48 89 94 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rdx
00C19E7B  48 33 C8                        xor rcx, rax
00C19E7E  49 8B C2                        mov rax, r10
00C19E81  48 F7 E1                        mul rcx
00C19E84  48 C1 EA 03                     shr rdx, 3
00C19E88  48 8D 04 92                     lea rax, [rdx + rdx*4]
00C19E8C  48 03 C0                        add rax, rax
00C19E8F  48 2B C8                        sub rcx, rax
00C19E92  48 83 F9 05                     cmp rcx, 5
00C19E96  73 73                           jae 0x140c19f0b
00C19E98  44 8B 87 DC 09 00 00            mov r8d, dword ptr [rdi + 0x9dc]
00C19E9F  41 0F BA E8 0A                  bts r8d, 0xa
00C19EA4  44 89 87 DC 09 00 00            mov dword ptr [rdi + 0x9dc], r8d
00C19EAB  41 0F BA E1 1E                  bt r9d, 0x1e
00C19EB0  72 59                           jb 0x140c19f0b
00C19EB2  0F 31                           rdtsc
00C19EB4  48 C1 E2 20                     shl rdx, 0x20
00C19EB8  48 0B C2                        or rax, rdx
00C19EBB  48 8B D0                        mov rdx, rax
00C19EBE  48 8B C8                        mov rcx, rax
00C19EC1  48 C1 C9 03                     ror rcx, 3
00C19EC5  48 33 D1                        xor rdx, rcx
00C19EC8  49 8B C3                        mov rax, r11
00C19ECB  48 F7 E2                        mul rdx
00C19ECE  48 8B CA                        mov rcx, rdx
00C19ED1  48 89 94 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdx
00C19ED9  48 33 C8                        xor rcx, rax
00C19EDC  49 8B C2                        mov rax, r10
00C19EDF  48 F7 E1                        mul rcx
00C19EE2  48 C1 EA 03                     shr rdx, 3
00C19EE6  48 8D 04 92                     lea rax, [rdx + rdx*4]
00C19EEA  48 03 C0                        add rax, rax
00C19EED  48 2B C8                        sub rcx, rax
00C19EF0  48 83 F9 03                     cmp rcx, 3
00C19EF4  73 15                           jae 0x140c19f0b
00C19EF6  83 BF 58 08 00 00 07            cmp dword ptr [rdi + 0x858], 7
00C19EFD  74 0C                           je 0x140c19f0b
00C19EFF  41 0F BA E8 0B                  bts r8d, 0xb
00C19F04  44 89 87 DC 09 00 00            mov dword ptr [rdi + 0x9dc], r8d
00C19F0B  33 C9                           xor ecx, ecx
00C19F0D  48 B8 89 02 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000289
00C19F17  38 08                           cmp byte ptr [rax], cl
00C19F19  74 0A                           je 0x140c19f25
00C19F1B  F6 87 9B 08 00 00 04            test byte ptr [rdi + 0x89b], 4
00C19F22  0F 45 CB                        cmovne ecx, ebx
00C19F25  8B 05 21 08 1F 00               mov eax, dword ptr [rip + 0x1f0821]
00C19F2B  25 00 00 00 F0                  and eax, 0xf0000000
00C19F30  3D 00 00 00 C0                  cmp eax, 0xc0000000
00C19F35  0F 44 CB                        cmove ecx, ebx
00C19F38  85 C9                           test ecx, ecx
00C19F3A  0F 84 7C 06 00 00               je 0x140c1a5bc
00C19F40  F7 87 D8 09 00 00 00 00 00 48   test dword ptr [rdi + 0x9d8], 0x48000000
00C19F4A  0F 85 6C 06 00 00               jne 0x140c1a5bc
00C19F50  83 BF 58 08 00 00 07            cmp dword ptr [rdi + 0x858], 7
00C19F57  0F 84 5F 06 00 00               je 0x140c1a5bc
00C19F5D  F7 87 DC 09 00 00 00 00 01 00   test dword ptr [rdi + 0x9dc], 0x10000
00C19F67  0F 85 4F 06 00 00               jne 0x140c1a5bc
00C19F6D  0F 31                           rdtsc
00C19F6F  48 C1 E2 20                     shl rdx, 0x20
00C19F73  48 0B C2                        or rax, rdx
00C19F76  48 8B D0                        mov rdx, rax
00C19F79  48 8B C8                        mov rcx, rax
00C19F7C  48 C1 C9 03                     ror rcx, 3
00C19F80  48 33 D1                        xor rdx, rcx
00C19F83  49 8B C3                        mov rax, r11
00C19F86  48 F7 E2                        mul rdx
00C19F89  48 8B CA                        mov rcx, rdx
00C19F8C  48 89 94 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdx
00C19F94  48 33 C8                        xor rcx, rax
00C19F97  49 8B C2                        mov rax, r10
00C19F9A  48 F7 E1                        mul rcx
00C19F9D  48 C1 EA 03                     shr rdx, 3
00C19FA1  48 8D 04 92                     lea rax, [rdx + rdx*4]
00C19FA5  48 03 C0                        add rax, rax
00C19FA8  48 2B C8                        sub rcx, rax
00C19FAB  48 83 F9 03                     cmp rcx, 3
00C19FAF  0F 83 07 06 00 00               jae 0x140c1a5bc
00C19FB5  48 8B 0D C4 E0 3E 00            mov rcx, qword ptr [rip + 0x3ee0c4]
00C19FBC  48 85 C9                        test rcx, rcx
00C19FBF  0F 85 A4 05 00 00               jne 0x140c1a569
00C19FC5  0F 31                           rdtsc
00C19FC7  48 C1 E2 20                     shl rdx, 0x20
00C19FCB  48 0B C2                        or rax, rdx
00C19FCE  48 8B D0                        mov rdx, rax
00C19FD1  48 8B C8                        mov rcx, rax
00C19FD4  48 C1 C9 03                     ror rcx, 3
00C19FD8  48 33 D1                        xor rdx, rcx
00C19FDB  49 8B C3                        mov rax, r11
00C19FDE  48 F7 E2                        mul rdx
00C19FE1  48 8B DA                        mov rbx, rdx
00C19FE4  48 89 94 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdx
00C19FEC  48 33 D8                        xor rbx, rax
00C19FEF  48 B8 A3 8B 2E BA E8 A2 8B 2E   movabs rax, 0x2e8ba2e8ba2e8ba3
00C19FF9  48 F7 E3                        mul rbx
00C19FFC  48 D1 EA                        shr rdx, 1
00C19FFF  48 6B C2 0B                     imul rax, rdx, 0xb
00C1A003  48 2B D8                        sub rbx, rax
00C1A006  8B CB                           mov ecx, ebx
00C1A008  83 FB 05                        cmp ebx, 5
00C1A00B  0F 87 20 02 00 00               ja 0x140c1a231
00C1A011  0F 84 C7 01 00 00               je 0x140c1a1de
00C1A017  8B C3                           mov eax, ebx
00C1A019  85 DB                           test ebx, ebx
00C1A01B  0F 84 6A 01 00 00               je 0x140c1a18b
00C1A021  83 E8 01                        sub eax, 1
00C1A024  0F 84 0E 01 00 00               je 0x140c1a138
00C1A02A  83 E8 01                        sub eax, 1
00C1A02D  0F 84 AF 00 00 00               je 0x140c1a0e2
00C1A033  83 F8 01                        cmp eax, 1
00C1A036  8B C6                           mov eax, esi
00C1A038  74 54                           je 0x140c1a08e
00C1A03A  F7 E3                           mul ebx
00C1A03C  D1 EA                           shr edx, 1
00C1A03E  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A041  2B C8                           sub ecx, eax
00C1A043  74 2C                           je 0x140c1a071
00C1A045  B8 46 49 76 70                  mov eax, 0x70764946
00C1A04A  83 F9 01                        cmp ecx, 1
00C1A04D  8B CB                           mov ecx, ebx
00C1A04F  74 10                           je 0x140c1a061
00C1A051  D3 C0                           rol eax, cl
00C1A053  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00C1A057  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00C1A05C  E9 EA 03 00 00                  jmp 0x140c1a44b
00C1A061  D3 C8                           ror eax, cl
00C1A063  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00C1A067  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00C1A06C  E9 BC 03 00 00                  jmp 0x140c1a42d
00C1A071  8D 43 02                        lea eax, [rbx + 2]
00C1A074  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A077  B8 46 49 76 70                  mov eax, 0x70764946
00C1A07C  D3 C0                           rol eax, cl
00C1A07E  33 C3                           xor eax, ebx
00C1A080  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00C1A084  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00C1A089  E9 BA 03 00 00                  jmp 0x140c1a448
00C1A08E  F7 E3                           mul ebx
00C1A090  D1 EA                           shr edx, 1
00C1A092  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A095  2B C8                           sub ecx, eax
00C1A097  74 2C                           je 0x140c1a0c5
00C1A099  B8 44 50 77 72                  mov eax, 0x72775044
00C1A09E  83 F9 01                        cmp ecx, 1
00C1A0A1  8B CB                           mov ecx, ebx
00C1A0A3  74 10                           je 0x140c1a0b5
00C1A0A5  D3 C0                           rol eax, cl
00C1A0A7  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00C1A0AB  44 8B 4C 24 58                  mov r9d, dword ptr [rsp + 0x58]
00C1A0B0  E9 96 03 00 00                  jmp 0x140c1a44b
00C1A0B5  D3 C8                           ror eax, cl
00C1A0B7  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00C1A0BB  44 8B 4C 24 58                  mov r9d, dword ptr [rsp + 0x58]
00C1A0C0  E9 68 03 00 00                  jmp 0x140c1a42d
00C1A0C5  8D 43 02                        lea eax, [rbx + 2]
00C1A0C8  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A0CB  B8 44 50 77 72                  mov eax, 0x72775044
00C1A0D0  D3 C0                           rol eax, cl
00C1A0D2  33 C3                           xor eax, ebx
00C1A0D4  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00C1A0D8  44 8B 4C 24 58                  mov r9d, dword ptr [rsp + 0x58]
00C1A0DD  E9 66 03 00 00                  jmp 0x140c1a448
00C1A0E2  8B C6                           mov eax, esi
00C1A0E4  F7 E3                           mul ebx
00C1A0E6  D1 EA                           shr edx, 1
00C1A0E8  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A0EB  2B C8                           sub ecx, eax
00C1A0ED  74 2C                           je 0x140c1a11b
00C1A0EF  B8 43 64 6D 61                  mov eax, 0x616d6443
00C1A0F4  83 F9 01                        cmp ecx, 1
00C1A0F7  8B CB                           mov ecx, ebx
00C1A0F9  74 10                           je 0x140c1a10b
00C1A0FB  D3 C0                           rol eax, cl
00C1A0FD  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00C1A101  44 8B 4C 24 5C                  mov r9d, dword ptr [rsp + 0x5c]
00C1A106  E9 40 03 00 00                  jmp 0x140c1a44b
00C1A10B  D3 C8                           ror eax, cl
00C1A10D  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00C1A111  44 8B 4C 24 5C                  mov r9d, dword ptr [rsp + 0x5c]
00C1A116  E9 12 03 00 00                  jmp 0x140c1a42d
00C1A11B  8D 43 02                        lea eax, [rbx + 2]
00C1A11E  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A121  B8 43 64 6D 61                  mov eax, 0x616d6443
00C1A126  D3 C0                           rol eax, cl
00C1A128  33 C3                           xor eax, ebx
00C1A12A  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00C1A12E  44 8B 4C 24 5C                  mov r9d, dword ptr [rsp + 0x5c]
00C1A133  E9 10 03 00 00                  jmp 0x140c1a448
00C1A138  8B C6                           mov eax, esi
00C1A13A  F7 E3                           mul ebx
00C1A13C  D1 EA                           shr edx, 1
00C1A13E  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A141  2B C8                           sub ecx, eax
00C1A143  74 2B                           je 0x140c1a170
00C1A145  83 F9 01                        cmp ecx, 1
00C1A148  8B CB                           mov ecx, ebx
00C1A14A  74 12                           je 0x140c1a15e
00C1A14C  41 D3 C4                        rol r12d, cl
00C1A14F  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00C1A154  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
00C1A159  E9 ED 02 00 00                  jmp 0x140c1a44b
00C1A15E  41 D3 CC                        ror r12d, cl
00C1A161  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00C1A166  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
00C1A16B  E9 BD 02 00 00                  jmp 0x140c1a42d
00C1A170  8D 43 02                        lea eax, [rbx + 2]
00C1A173  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A176  41 D3 C4                        rol r12d, cl
00C1A179  44 33 E3                        xor r12d, ebx
00C1A17C  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
00C1A181  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
00C1A186  E9 BD 02 00 00                  jmp 0x140c1a448
00C1A18B  8B C6                           mov eax, esi
00C1A18D  F7 E3                           mul ebx
00C1A18F  D1 EA                           shr edx, 1
00C1A191  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A194  2B C8                           sub ecx, eax
00C1A196  74 2B                           je 0x140c1a1c3
00C1A198  83 F9 01                        cmp ecx, 1
00C1A19B  8B CB                           mov ecx, ebx
00C1A19D  74 12                           je 0x140c1a1b1
00C1A19F  41 D3 C7                        rol r15d, cl
00C1A1A2  44 89 7C 24 64                  mov dword ptr [rsp + 0x64], r15d
00C1A1A7  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
00C1A1AC  E9 9A 02 00 00                  jmp 0x140c1a44b
00C1A1B1  41 D3 CF                        ror r15d, cl
00C1A1B4  44 89 7C 24 64                  mov dword ptr [rsp + 0x64], r15d
00C1A1B9  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
00C1A1BE  E9 6A 02 00 00                  jmp 0x140c1a42d
00C1A1C3  8D 43 02                        lea eax, [rbx + 2]
00C1A1C6  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A1C9  41 D3 C7                        rol r15d, cl
00C1A1CC  44 33 FB                        xor r15d, ebx
00C1A1CF  44 89 7C 24 64                  mov dword ptr [rsp + 0x64], r15d
00C1A1D4  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
00C1A1D9  E9 6A 02 00 00                  jmp 0x140c1a448
00C1A1DE  8B C6                           mov eax, esi
00C1A1E0  F7 E3                           mul ebx
00C1A1E2  D1 EA                           shr edx, 1
00C1A1E4  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A1E7  2B C8                           sub ecx, eax
00C1A1E9  74 2B                           je 0x140c1a216
00C1A1EB  83 F9 01                        cmp ecx, 1
00C1A1EE  8B CB                           mov ecx, ebx
00C1A1F0  74 12                           je 0x140c1a204
00C1A1F2  41 D3 C6                        rol r14d, cl
00C1A1F5  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
00C1A1FA  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
00C1A1FF  E9 47 02 00 00                  jmp 0x140c1a44b
00C1A204  41 D3 CE                        ror r14d, cl
00C1A207  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
00C1A20C  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
00C1A211  E9 17 02 00 00                  jmp 0x140c1a42d
00C1A216  8D 43 02                        lea eax, [rbx + 2]
00C1A219  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A21C  41 D3 C6                        rol r14d, cl
00C1A21F  44 33 F3                        xor r14d, ebx
00C1A222  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
00C1A227  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
00C1A22C  E9 17 02 00 00                  jmp 0x140c1a448
00C1A231  83 E9 06                        sub ecx, 6
00C1A234  0F 84 C1 01 00 00               je 0x140c1a3fb
00C1A23A  83 E9 01                        sub ecx, 1
00C1A23D  0F 84 69 01 00 00               je 0x140c1a3ac
00C1A243  83 E9 01                        sub ecx, 1
00C1A246  0F 84 08 01 00 00               je 0x140c1a354
00C1A24C  83 F9 01                        cmp ecx, 1
00C1A24F  0F 84 A7 00 00 00               je 0x140c1a2fc
00C1A255  0F 31                           rdtsc
00C1A257  48 C1 E2 20                     shl rdx, 0x20
00C1A25B  48 0B C2                        or rax, rdx
00C1A25E  48 8B D0                        mov rdx, rax
00C1A261  48 8B C8                        mov rcx, rax
00C1A264  48 C1 C9 03                     ror rcx, 3
00C1A268  48 33 D1                        xor rdx, rcx
00C1A26B  49 8B C3                        mov rax, r11
00C1A26E  48 F7 E2                        mul rdx
00C1A271  48 89 94 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdx
00C1A279  4C 8B C8                        mov r9, rax
00C1A27C  44 33 CA                        xor r9d, edx
00C1A27F  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00C1A284  41 F7 E1                        mul r9d
00C1A287  C1 EA 03                        shr edx, 3
00C1A28A  6B CA 1A                        imul ecx, edx, 0x1a
00C1A28D  41 8B D9                        mov ebx, r9d
00C1A290  2B D9                           sub ebx, ecx
00C1A292  83 C3 61                        add ebx, 0x61
00C1A295  41 C1 E9 05                     shr r9d, 5
00C1A299  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00C1A29E  41 F7 E1                        mul r9d
00C1A2A1  C1 EA 03                        shr edx, 3
00C1A2A4  6B C2 1A                        imul eax, edx, 0x1a
00C1A2A7  45 8B C1                        mov r8d, r9d
00C1A2AA  44 2B C0                        sub r8d, eax
00C1A2AD  41 83 C0 41                     add r8d, 0x41
00C1A2B1  C1 E3 08                        shl ebx, 8
00C1A2B4  44 0B C3                        or r8d, ebx
00C1A2B7  41 C1 E9 05                     shr r9d, 5
00C1A2BB  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00C1A2C0  41 F7 E1                        mul r9d
00C1A2C3  C1 EA 03                        shr edx, 3
00C1A2C6  6B CA 1A                        imul ecx, edx, 0x1a
00C1A2C9  41 8B D9                        mov ebx, r9d
00C1A2CC  2B D9                           sub ebx, ecx
00C1A2CE  83 C3 61                        add ebx, 0x61
00C1A2D1  41 C1 E0 08                     shl r8d, 8
00C1A2D5  41 0B D8                        or ebx, r8d
00C1A2D8  41 C1 E9 05                     shr r9d, 5
00C1A2DC  B8 4F EC C4 4E                  mov eax, 0x4ec4ec4f
00C1A2E1  41 F7 E1                        mul r9d
00C1A2E4  C1 EA 03                        shr edx, 3
00C1A2E7  6B C2 1A                        imul eax, edx, 0x1a
00C1A2EA  44 2B C8                        sub r9d, eax
00C1A2ED  41 83 C1 41                     add r9d, 0x41
00C1A2F1  C1 E3 08                        shl ebx, 8
00C1A2F4  44 0B CB                        or r9d, ebx
00C1A2F7  E9 52 01 00 00                  jmp 0x140c1a44e
00C1A2FC  8B C6                           mov eax, esi
00C1A2FE  F7 E3                           mul ebx
00C1A300  D1 EA                           shr edx, 1
00C1A302  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A305  8B CB                           mov ecx, ebx
00C1A307  2B C8                           sub ecx, eax
00C1A309  74 2C                           je 0x140c1a337
00C1A30B  B8 46 4F 43 58                  mov eax, 0x58434f46
00C1A310  83 F9 01                        cmp ecx, 1
00C1A313  8B CB                           mov ecx, ebx
00C1A315  74 10                           je 0x140c1a327
00C1A317  D3 C0                           rol eax, cl
00C1A319  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
00C1A31D  44 8B 4C 24 6C                  mov r9d, dword ptr [rsp + 0x6c]
00C1A322  E9 24 01 00 00                  jmp 0x140c1a44b
00C1A327  D3 C8                           ror eax, cl
00C1A329  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
00C1A32D  44 8B 4C 24 6C                  mov r9d, dword ptr [rsp + 0x6c]
00C1A332  E9 F6 00 00 00                  jmp 0x140c1a42d
00C1A337  8D 43 02                        lea eax, [rbx + 2]
00C1A33A  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A33D  B8 46 4F 43 58                  mov eax, 0x58434f46
00C1A342  D3 C0                           rol eax, cl
00C1A344  33 C3                           xor eax, ebx
00C1A346  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
00C1A34A  44 8B 4C 24 6C                  mov r9d, dword ptr [rsp + 0x6c]
00C1A34F  E9 F4 00 00 00                  jmp 0x140c1a448
00C1A354  8B C6                           mov eax, esi
00C1A356  F7 E3                           mul ebx
00C1A358  D1 EA                           shr edx, 1
00C1A35A  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A35D  8B CB                           mov ecx, ebx
00C1A35F  2B C8                           sub ecx, eax
00C1A361  74 2C                           je 0x140c1a38f
00C1A363  B8 41 66 64 42                  mov eax, 0x42646641
00C1A368  83 F9 01                        cmp ecx, 1
00C1A36B  8B CB                           mov ecx, ebx
00C1A36D  74 10                           je 0x140c1a37f
00C1A36F  D3 C0                           rol eax, cl
00C1A371  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00C1A375  44 8B 4C 24 70                  mov r9d, dword ptr [rsp + 0x70]
00C1A37A  E9 CC 00 00 00                  jmp 0x140c1a44b
00C1A37F  D3 C8                           ror eax, cl
00C1A381  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00C1A385  44 8B 4C 24 70                  mov r9d, dword ptr [rsp + 0x70]
00C1A38A  E9 9E 00 00 00                  jmp 0x140c1a42d
00C1A38F  8D 43 02                        lea eax, [rbx + 2]
00C1A392  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A395  B8 41 66 64 42                  mov eax, 0x42646641
00C1A39A  D3 C0                           rol eax, cl
00C1A39C  33 C3                           xor eax, ebx
00C1A39E  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00C1A3A2  44 8B 4C 24 70                  mov r9d, dword ptr [rsp + 0x70]
00C1A3A7  E9 9C 00 00 00                  jmp 0x140c1a448
00C1A3AC  8B C6                           mov eax, esi
00C1A3AE  F7 E3                           mul ebx
00C1A3B0  D1 EA                           shr edx, 1
00C1A3B2  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A3B5  8B CB                           mov ecx, ebx
00C1A3B7  2B C8                           sub ecx, eax
00C1A3B9  74 26                           je 0x140c1a3e1
00C1A3BB  B8 41 6C 53 63                  mov eax, 0x63536c41
00C1A3C0  83 F9 01                        cmp ecx, 1
00C1A3C3  8B CB                           mov ecx, ebx
00C1A3C5  74 0D                           je 0x140c1a3d4
00C1A3C7  D3 C0                           rol eax, cl
00C1A3C9  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00C1A3CD  44 8B 4C 24 74                  mov r9d, dword ptr [rsp + 0x74]
00C1A3D2  EB 77                           jmp 0x140c1a44b
00C1A3D4  D3 C8                           ror eax, cl
00C1A3D6  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00C1A3DA  44 8B 4C 24 74                  mov r9d, dword ptr [rsp + 0x74]
00C1A3DF  EB 4C                           jmp 0x140c1a42d
00C1A3E1  8D 43 02                        lea eax, [rbx + 2]
00C1A3E4  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A3E7  B8 41 6C 53 63                  mov eax, 0x63536c41
00C1A3EC  D3 C0                           rol eax, cl
00C1A3EE  33 C3                           xor eax, ebx
00C1A3F0  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00C1A3F4  44 8B 4C 24 74                  mov r9d, dword ptr [rsp + 0x74]
00C1A3F9  EB 4D                           jmp 0x140c1a448
00C1A3FB  8B C6                           mov eax, esi
00C1A3FD  F7 E3                           mul ebx
00C1A3FF  D1 EA                           shr edx, 1
00C1A401  8D 04 52                        lea eax, [rdx + rdx*2]
00C1A404  8B CB                           mov ecx, ebx
00C1A406  2B C8                           sub ecx, eax
00C1A408  74 28                           je 0x140c1a432
00C1A40A  83 F9 01                        cmp ecx, 1
00C1A40D  8B CB                           mov ecx, ebx
00C1A40F  74 0F                           je 0x140c1a420
00C1A411  41 D3 C5                        rol r13d, cl
00C1A414  44 89 6C 24 78                  mov dword ptr [rsp + 0x78], r13d
00C1A419  44 8B 4C 24 78                  mov r9d, dword ptr [rsp + 0x78]
00C1A41E  EB 2B                           jmp 0x140c1a44b
00C1A420  41 D3 CD                        ror r13d, cl
00C1A423  44 89 6C 24 78                  mov dword ptr [rsp + 0x78], r13d
00C1A428  44 8B 4C 24 78                  mov r9d, dword ptr [rsp + 0x78]
00C1A42D  41 D3 C1                        rol r9d, cl
00C1A430  EB 1C                           jmp 0x140c1a44e
00C1A432  8D 43 02                        lea eax, [rbx + 2]
00C1A435  8D 0C 40                        lea ecx, [rax + rax*2]
00C1A438  41 D3 C5                        rol r13d, cl
00C1A43B  44 33 EB                        xor r13d, ebx
00C1A43E  44 89 6C 24 78                  mov dword ptr [rsp + 0x78], r13d
00C1A443  44 8B 4C 24 78                  mov r9d, dword ptr [rsp + 0x78]
00C1A448  44 33 CB                        xor r9d, ebx
00C1A44B  41 D3 C9                        ror r9d, cl
00C1A44E  48 8B 87 00 01 00 00            mov rax, qword ptr [rdi + 0x100]
00C1A455  45 8B C1                        mov r8d, r9d
00C1A458  BB 80 14 00 00                  mov ebx, 0x1480
00C1A45D  8B D3                           mov edx, ebx
00C1A45F  41 BF 40 00 00 00               mov r15d, 0x40
00C1A465  41 8B CF                        mov ecx, r15d
00C1A468  E8 F3 05 FD FF                  call 0x140beaa60
00C1A46D  48 8B C8                        mov rcx, rax
00C1A470  48 89 05 09 DC 3E 00            mov qword ptr [rip + 0x3edc09], rax
00C1A477  48 85 C0                        test rax, rax
00C1A47A  0F 84 BA 01 00 00               je 0x140c1a63a
00C1A480  BA 90 02 00 00                  mov edx, 0x290
00C1A485  41 8D 77 C1                     lea esi, [r15 - 0x3f]
00C1A489  41 BC F8 FF FF FF               mov r12d, 0xfffffff8
00C1A48F  48 C7 00 00 00 00 00            mov qword ptr [rax], 0
00C1A496  48 83 C0 08                     add rax, 8
00C1A49A  41 03 DC                        add ebx, r12d
00C1A49D  48 2B D6                        sub rdx, rsi
00C1A4A0  75 ED                           jne 0x140c1a48f
00C1A4A2  41 83 CE FF                     or r14d, 0xffffffff
00C1A4A6  85 DB                           test ebx, ebx
00C1A4A8  74 0B                           je 0x140c1a4b5
00C1A4AA  C6 00 00                        mov byte ptr [rax], 0
00C1A4AD  48 03 C6                        add rax, rsi
00C1A4B0  41 03 DE                        add ebx, r14d
00C1A4B3  75 F5                           jne 0x140c1a4aa
00C1A4B5  E8 46 00 62 FF                  call 0x14023a500
00C1A4BA  48 8B 0D BF DB 3E 00            mov rcx, qword ptr [rip + 0x3edbbf]
00C1A4C1  48 C1 E8 0C                     shr rax, 0xc
00C1A4C5  48 89 81 18 14 00 00            mov qword ptr [rcx + 0x1418], rax
00C1A4CC  BA 00 02 00 00                  mov edx, 0x200
00C1A4D1  44 8B C2                        mov r8d, edx
00C1A4D4  4C 8B 94 24 90 00 00 00         mov r10, qword ptr [rsp + 0x90]
00C1A4DC  49 8B DA                        mov rbx, r10
00C1A4DF  4D 8B CF                        mov r9, r15
00C1A4E2  48 8B 03                        mov rax, qword ptr [rbx]
00C1A4E5  48 89 01                        mov qword ptr [rcx], rax
00C1A4E8  48 83 C1 08                     add rcx, 8
00C1A4EC  48 83 C3 08                     add rbx, 8
00C1A4F0  45 03 C4                        add r8d, r12d
00C1A4F3  4C 2B CE                        sub r9, rsi
00C1A4F6  75 EA                           jne 0x140c1a4e2
00C1A4F8  45 85 C0                        test r8d, r8d
00C1A4FB  74 0F                           je 0x140c1a50c
00C1A4FD  8A 03                           mov al, byte ptr [rbx]
00C1A4FF  88 01                           mov byte ptr [rcx], al
00C1A501  48 03 CE                        add rcx, rsi
00C1A504  48 03 DE                        add rbx, rsi
00C1A507  45 03 C6                        add r8d, r14d
00C1A50A  75 F1                           jne 0x140c1a4fd
00C1A50C  48 8B 0D 6D DB 3E 00            mov rcx, qword ptr [rip + 0x3edb6d]
00C1A513  48 03 CA                        add rcx, rdx
00C1A516  49 8B 02                        mov rax, qword ptr [r10]
00C1A519  48 89 01                        mov qword ptr [rcx], rax
00C1A51C  48 83 C1 08                     add rcx, 8
00C1A520  49 83 C2 08                     add r10, 8
00C1A524  41 03 D4                        add edx, r12d
00C1A527  4C 2B FE                        sub r15, rsi
00C1A52A  75 EA                           jne 0x140c1a516
00C1A52C  85 D2                           test edx, edx
00C1A52E  74 10                           je 0x140c1a540
00C1A530  41 8A 02                        mov al, byte ptr [r10]
00C1A533  88 01                           mov byte ptr [rcx], al
00C1A535  48 03 CE                        add rcx, rsi
00C1A538  4C 03 D6                        add r10, rsi
00C1A53B  41 03 D6                        add edx, r14d
00C1A53E  75 F0                           jne 0x140c1a530
00C1A540  48 8B 0D 39 DB 3E 00            mov rcx, qword ptr [rip + 0x3edb39]
00C1A547  B8 FF 7F 00 00                  mov eax, 0x7fff
00C1A54C  66 21 41 44                     and word ptr [rcx + 0x44], ax
00C1A550  66 89 49 40                     mov word ptr [rcx + 0x40], cx
00C1A554  48 8B C1                        mov rax, rcx
00C1A557  48 C1 E8 10                     shr rax, 0x10
00C1A55B  66 89 41 46                     mov word ptr [rcx + 0x46], ax
00C1A55F  48 8B C1                        mov rax, rcx
00C1A562  48 C1 E8 20                     shr rax, 0x20
00C1A566  89 41 48                        mov dword ptr [rcx + 0x48], eax
00C1A569  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
00C1A571  2B D7                           sub edx, edi
00C1A573  48 8D 05 46 03 FD FF            lea rax, [rip - 0x2fcba]
00C1A57A  2B 84 24 38 01 00 00            sub eax, dword ptr [rsp + 0x138]
00C1A581  0F BA AF DC 09 00 00 0F         bts dword ptr [rdi + 0x9dc], 0xf
00C1A589  48 89 8F E0 08 00 00            mov qword ptr [rdi + 0x8e0], rcx
00C1A590  03 C2                           add eax, edx
00C1A592  89 87 14 09 00 00               mov dword ptr [rdi + 0x914], eax
00C1A598  C7 87 B3 08 00 00 48 83 EC 28   mov dword ptr [rdi + 0x8b3], 0x28ec8348
00C1A5A2  C7 87 B7 08 00 00 FF 11 48 83   mov dword ptr [rdi + 0x8b7], 0x834811ff
00C1A5AC  66 C7 87 BB 08 00 00 C4 28      mov word ptr [rdi + 0x8bb], 0x28c4
00C1A5B5  C6 87 BD 08 00 00 C3            mov byte ptr [rdi + 0x8bd], 0xc3
00C1A5BC  8B 87 D8 09 00 00               mov eax, dword ptr [rdi + 0x9d8]
00C1A5C2  0F BA E0 1E                     bt eax, 0x1e
00C1A5C6  73 0A                           jae 0x140c1a5d2
00C1A5C8  0F BA E8 1A                     bts eax, 0x1a
00C1A5CC  89 87 D8 09 00 00               mov dword ptr [rdi + 0x9d8], eax
00C1A5D2  0F BA E0 1A                     bt eax, 0x1a
00C1A5D6  72 5D                           jb 0x140c1a635
00C1A5D8  44 0F 20 C2                     mov rdx, cr8
00C1A5DC  88 94 24 48 01 00 00            mov byte ptr [rsp + 0x148], dl
00C1A5E3  B8 0F 00 00 00                  mov eax, 0xf
00C1A5E8  44 0F 22 C0                     mov cr8, rax
00C1A5EC  0F 20 C1                        mov rcx, cr0
00C1A5EF  48 89 8C 24 38 01 00 00         mov qword ptr [rsp + 0x138], rcx
00C1A5F7  48 8B C1                        mov rax, rcx
00C1A5FA  48 0F BA F0 10                  btr rax, 0x10
00C1A5FF  0F 22 C0                        mov cr0, rax
00C1A602  EB 1F                           jmp 0x140c1a623
00C1A604  48 8B BC 24 30 01 00 00         mov rdi, qword ptr [rsp + 0x130]
00C1A60C  0F BA AF DC 09 00 00 16         bts dword ptr [rdi + 0x9dc], 0x16
00C1A614  48 8B 8C 24 38 01 00 00         mov rcx, qword ptr [rsp + 0x138]
00C1A61C  8A 94 24 48 01 00 00            mov dl, byte ptr [rsp + 0x148]
00C1A623  0F 20 C0                        mov rax, cr0
00C1A626  48 3B C8                        cmp rcx, rax
00C1A629  74 03                           je 0x140c1a62e
00C1A62B  0F 22 C1                        mov cr0, rcx
00C1A62E  0F B6 C2                        movzx eax, dl
00C1A631  44 0F 22 C0                     mov cr8, rax
00C1A635  48 8B C7                        mov rax, rdi
00C1A638  EB 02                           jmp 0x140c1a63c
00C1A63A  33 C0                           xor eax, eax
00C1A63C  48 81 C4 F0 00 00 00            add rsp, 0xf0
00C1A643  41 5F                           pop r15
00C1A645  41 5E                           pop r14
00C1A647  41 5D                           pop r13
00C1A649  41 5C                           pop r12
00C1A64B  5F                              pop rdi
00C1A64C  5E                              pop rsi
00C1A64D  5B                              pop rbx
00C1A64E  C3                              ret
00C1A64F  CC                              int3
00C1A650  C7 84 24 38 01 00 00 09 00 00 E8  mov dword ptr [rsp + 0x138], 0xe8000009
00C1A65B  8B 8C 24 38 01 00 00            mov ecx, dword ptr [rsp + 0x138]
00C1A662  C1 C1 65                        rol ecx, 0x65
00C1A665  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
00C1A66E  45 33 C0                        xor r8d, r8d
00C1A671  41 8D 50 04                     lea edx, [r8 + 4]
00C1A675  E8 E6 2F 8E FF                  call 0x1404fd660
00C1A67A  90                              nop
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00C19464(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_cr0;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p138;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (240);
    if (a4 != 0) {
        result = v_rip - 191030;
        result = (unsigned int)((result) - ((unsigned int)(a2)));
        *(unsigned __int16 *)(result + a3 * 1) = 0xE0FFULL;
    }
    result = (unsigned int)((v_rip - 191030) - ((unsigned int)((unsigned int)((unsigned int)(a2)))));
    if (a4 != 0) {
        *(unsigned __int8 *)(result + a3 * 1) = 195;
    }
    *(unsigned __int64 *)(a1 + 2280) = v_rip - 12686521;
    result = RtlImageNtHeader(v_rip - 12686521, a2, a3, a4);
    *(unsigned __int64 *)(a1 + 2296) = result;
    a1 = ((unsigned int)(*(unsigned int *)(result + 80))) + (v_rip - 12686521);
    *(unsigned __int64 *)(a1 + 2288) = a1;
    *(unsigned int *)(a1 + 2252) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4124926)));
    *(unsigned int *)(a1 + 2256) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4124970)));
    *(unsigned int *)(a1 + 2260) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3849062)));
    if (((unsigned int)(*(unsigned __int64 *)(v_rip + 4124897))) != 8) goto loc_00C1A650;
    result = KeGuardDispatchICall(254, a2, a3, *(unsigned __int64 *)(v_rip + 4124897));
    *(unsigned __int64 *)(a1 + 2264) = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 2256)) + *(unsigned __int64 *)(result) * 1);
    *(unsigned __int16 *)(a1 + 2200) = 0xCF48ULL;
    v_stack_m98 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 24)) + 56);
    *(unsigned __int64 *)(a1 + 2152) = v_xmm0;
    *(unsigned __int64 *)(a1 + 2168) = v_xmm1;
    *(unsigned __int64 *)(a1 + 2184) = v_xmm0;
    a2 = (a2) << (32);
    result = (*(unsigned __int64 *)(gs_base + (0 + 24))) | (a2);
    a2 = (result) ^ (result);
    v_stack_m90 = a2;
    v_rbx = (a2) ^ (a3);
    a2 = (a2) >> (1);
    result = (a3) * (a2);
    v_rbx = (v_rbx) - (result);
    if (((unsigned int)(v_rbx)) > 5) goto loc_00C19855;
    if (((unsigned int)(v_rbx)) == 5) goto loc_00C197E8;
    if ((unsigned int)(v_rbx) == 0) goto loc_00C19781;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (1));
    if (condition_is_equal) goto loc_00C19720;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C196CD;
    if (((unsigned int)(result)) == 1) goto loc_00C19682;
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C19653;
    if (((unsigned int)(a1)) == 1) goto loc_00C1963D;
    v_stack_p20 = (unsigned int)((unsigned int)(0x70764946ULL));
    goto loc_00C19674;
loc_00C1963D:
    v_stack_p20 = (unsigned int)((unsigned int)(0x70764946ULL));
loc_00C1964E:
    goto loc_00C19677;
loc_00C19653:
    result = (unsigned int)(((unsigned int)(0x70764946ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_p20 = (unsigned int)(result);
loc_00C19671:
    a4 = (unsigned int)(((unsigned int)(v_stack_p20)) ^ ((unsigned int)(v_rbx)));
loc_00C19674:
loc_00C19677:
    goto loc_00C19A9B;
loc_00C19682:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C196B3;
    if (((unsigned int)(a1)) == 1) goto loc_00C196A6;
    v_stack_mF8 = (unsigned int)((unsigned int)(0x72775044ULL));
    goto loc_00C19674;
loc_00C196A6:
    v_stack_mF8 = (unsigned int)((unsigned int)(0x72775044ULL));
    goto loc_00C1964E;
loc_00C196B3:
    result = (unsigned int)(((unsigned int)(0x72775044ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mF8 = (unsigned int)(result);
    goto loc_00C19671;
loc_00C196CD:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C19703;
    if (((unsigned int)(a1)) == 1) goto loc_00C196F3;
    v_stack_mF4 = (unsigned int)((unsigned int)(0x616D6443ULL));
    goto loc_00C19674;
loc_00C196F3:
    v_stack_mF4 = (unsigned int)((unsigned int)(0x616D6443ULL));
    goto loc_00C1964E;
loc_00C19703:
    result = (unsigned int)(((unsigned int)(0x616D6443ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mF4 = (unsigned int)(result);
    goto loc_00C19671;
loc_00C19720:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1975A;
    if (((unsigned int)(a1)) == 1) goto loc_00C1974A;
    v_stack_mF0 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x655A6343ULL))));
    goto loc_00C19773;
loc_00C1974A:
    v_stack_mF0 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x655A6343ULL))));
    goto loc_00C19776;
loc_00C1975A:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x655A6343ULL)))) ^ ((unsigned int)(v_rbx)));
    v_stack_mF0 = (unsigned int)(result);
    a4 = (unsigned int)(((unsigned int)(v_stack_mF0)) ^ ((unsigned int)(v_rbx)));
loc_00C19773:
loc_00C19776:
    goto loc_00C19AA1;
loc_00C19781:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C197BB;
    if (((unsigned int)(a1)) == 1) goto loc_00C197AB;
    v_stack_mEC = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x63426343ULL))));
    goto loc_00C197D4;
loc_00C197AB:
    v_stack_mEC = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x63426343ULL))));
    goto loc_00C197D7;
loc_00C197BB:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x63426343ULL)))) ^ ((unsigned int)(v_rbx)));
    v_stack_mEC = (unsigned int)(result);
    a4 = (unsigned int)(((unsigned int)(v_stack_mEC)) ^ ((unsigned int)(v_rbx)));
loc_00C197D4:
loc_00C197D7:
    goto loc_00C19AA7;
loc_00C197E8:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C19822;
    if (((unsigned int)(a1)) == 1) goto loc_00C19812;
    v_stack_mE8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x6944624FULL))));
    goto loc_00C1983B;
loc_00C19812:
    v_stack_mE8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x6944624FULL))));
    goto loc_00C1983E;
loc_00C19822:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x6944624FULL)))) ^ ((unsigned int)(v_rbx)));
    v_stack_mE8 = (unsigned int)(result);
    a4 = (unsigned int)(((unsigned int)(v_stack_mE8)) ^ ((unsigned int)(v_rbx)));
loc_00C1983B:
loc_00C1983E:
    goto loc_00C19AAD;
loc_00C19855:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (6));
    if (condition_is_equal) goto loc_00C19A3E;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C199E1;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C19984;
    if (((unsigned int)(result)) == 1) goto loc_00C19927;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m88 = a2;
    a4 = (unsigned int)((a3) ^ ((unsigned int)(a2)));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned int)((result) * ((unsigned int)(a2)));
    v_rbx = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)(a1)));
    v_rbx = (unsigned int)((v_rbx) + (97));
    a4 = (unsigned int)((a4) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) * ((unsigned int)(a2)));
    a3 = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)(result)));
    a3 = (unsigned int)((a3) + (65));
    v_rbx = (unsigned int)((v_rbx) << (8));
    a3 = (unsigned int)((a3) | ((unsigned int)(v_rbx)));
    a4 = (unsigned int)((a4) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) * ((unsigned int)(a2)));
    a1 = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (97));
    a3 = (unsigned int)((a3) << (8));
    a1 = (unsigned int)((a1) | ((unsigned int)(a3)));
    a4 = (unsigned int)((a4) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) * ((unsigned int)(a2)));
    a4 = (unsigned int)((a4) - ((unsigned int)(result)));
    a4 = (unsigned int)((a4) + (65));
    a1 = (unsigned int)((a1) << (8));
    a4 = (unsigned int)((a4) | ((unsigned int)(a1)));
    goto loc_00C19677;
loc_00C19927:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C19967;
    if (((unsigned int)(a1)) == 1) goto loc_00C19957;
    v_stack_mE4 = (unsigned int)((unsigned int)(0x58434F46ULL));
    goto loc_00C19674;
loc_00C19957:
    v_stack_mE4 = (unsigned int)((unsigned int)(0x58434F46ULL));
    goto loc_00C1964E;
loc_00C19967:
    result = (unsigned int)(((unsigned int)(0x58434F46ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mE4 = (unsigned int)(result);
    goto loc_00C19671;
loc_00C19984:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C199C4;
    if (((unsigned int)(a1)) == 1) goto loc_00C199B4;
    v_stack_mE0 = (unsigned int)((unsigned int)(0x42646641ULL));
    goto loc_00C19674;
loc_00C199B4:
    v_stack_mE0 = (unsigned int)((unsigned int)(0x42646641ULL));
    goto loc_00C1964E;
loc_00C199C4:
    result = (unsigned int)(((unsigned int)(0x42646641ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mE0 = (unsigned int)(result);
    goto loc_00C19671;
loc_00C199E1:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C19A21;
    if (((unsigned int)(a1)) == 1) goto loc_00C19A11;
    v_stack_mDC = (unsigned int)((unsigned int)(0x63536C41ULL));
    goto loc_00C19674;
loc_00C19A11:
    v_stack_mDC = (unsigned int)((unsigned int)(0x63536C41ULL));
    goto loc_00C1964E;
loc_00C19A21:
    result = (unsigned int)(((unsigned int)(0x63536C41ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mDC = (unsigned int)(result);
    goto loc_00C19671;
loc_00C19A3E:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C19A7F;
    if (((unsigned int)(a1)) == 1) goto loc_00C19A6F;
    v_stack_mD8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x5746744EULL))));
    goto loc_00C19A98;
loc_00C19A6F:
    v_stack_mD8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x5746744EULL))));
    goto loc_00C19A9B;
loc_00C19A7F:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x5746744EULL)))) ^ ((unsigned int)(v_rbx)));
    v_stack_mD8 = (unsigned int)(result);
    a4 = (unsigned int)(((unsigned int)(v_stack_mD8)) ^ ((unsigned int)(v_rbx)));
loc_00C19A98:
loc_00C19A9B:
loc_00C19AA1:
loc_00C19AA7:
loc_00C19AAD:
    result = KeGuardDispatchICall(64, 432, (unsigned int)(a4), a4);
    *(unsigned __int64 *)(a1 + 2304) = result;
    if (result == 0) goto loc_00C1A63A;
    result = (result) - (-128);
    result = (result) & (-128);
    *(unsigned __int64 *)(a1 + 2304) = result;
    *(unsigned int *)(a1 + 2204) = 0x8748050FULL;
    *(unsigned int *)(a1 + 2208) = 0x6481240CULL;
    *(unsigned int *)(a1 + 2212) = 0xFEFF1024ULL;
    *(unsigned int *)(a1 + 2216) = 0xCF48FFFFULL;
    *(unsigned __int8 *)(a1 + 2202) = 195;
    v_r11 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1656) * 1)) != ((unsigned __int8)(*(unsigned __int8 *)(a1 + 1664)))) goto loc_00C19BEA;
    result = 0;
    a1 = 0;
    v_stack_mA8 = 0;
    v_stack_mA4 = (unsigned int)(v_rbx);
    v_stack_mA0 = 0;
    v_stack_m9C = 432;
    if (0 < 7) goto loc_00C19BA4;
    a1 = 0;
    v_stack_mA8 = (unsigned int)(v_r11 + 7);
    v_stack_mA4 = (unsigned int)(v_rbx);
    v_stack_mA0 = 0;
    v_stack_m9C = 432;
    if (condition_is_below) { v_r11 = (unsigned int)(v_r11 + 1); }
    goto loc_00C19BA9;
loc_00C19BA4:
loc_00C19BA9:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1632) * 1)) != 6) goto loc_00C19BEF;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1648) * 1))) != 60) goto loc_00C19BC3;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1640) * 1))) == 3) goto loc_00C19BE5;
loc_00C19BC3:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1648) * 1))) != 63) goto loc_00C19BCF;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1640) * 1))) == 2) goto loc_00C19BE5;
loc_00C19BCF:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1648) * 1))) != 69) goto loc_00C19BDA;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1640) * 1))) == 1) goto loc_00C19BE5;
loc_00C19BDA:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1648) * 1))) != 70) goto loc_00C19BEF;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1640) * 1))) != 1) goto loc_00C19BEF;
loc_00C19BE5:
    v_r11 = 0;
    goto loc_00C19BEF;
loc_00C19BEA:
loc_00C19BEF:
    if (0 != 0) {
    }
    result = KeKvaShadowingActive(a1, 432, *(unsigned __int64 *)(a1 + 2016), *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1648) * 1));
    if ((unsigned int)(result) != 0) {
    }
    *(unsigned int *)(a1 + 2220) = 0x242C8348ULL;
    *(unsigned __int16 *)(a1 + 2224) = 0x4802ULL;
    *(unsigned __int8 *)(a1 + 2226) = 207;
    v_r11 = 0;
    v_r11 = ((*(unsigned __int8 *)(result)) != 0) ? 1 : 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 2034445))) & (0xF0000000ULL));
    if (((unsigned int)(result)) == 0xC0000000ULL) { v_r11 = 1; }
    if (((*(unsigned int *)(a1 + 2520)) & (0x8000000ULL)) != 0) goto loc_00C19E25;
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2060))))));
    *(unsigned int *)((unsigned int)(*(unsigned int *)(a1 + 2060)) + a1 * 1 + 11) = (unsigned int)(result);
    a2 = (432) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m80 = a2;
    a1 = (a2) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1648) * 1));
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 >= 1) goto loc_00C19CE9;
    if (((*(unsigned int *)(a1 + 2520)) & ((unsigned int)((unsigned int)(0x40008000ULL)))) != 0) goto loc_00C19CE9;
    v_rbx = a1 + 2520;
    if ((*(unsigned int *)(a1 + 2136)) != 7) {
        v_rbx = a1 + 2520;
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m78 = a2;
    a1 = (a2) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 2016) + *(unsigned __int64 *)(a1 + 1648) * 1));
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 >= 1) goto loc_00C19D53;
    if (((*(unsigned int *)(a1 + 2520)) & ((unsigned int)((unsigned int)(0x40008000ULL)))) != 0) goto loc_00C19D53;
    if ((*(unsigned int *)(a1 + 2136)) != 7) {
        a4 = a1 + 2520;
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m70 = a2;
    a2 = (unsigned __int8)((a2) ^ ((unsigned __int8)(a1 + 2520)));
    if ((((unsigned __int8)(a2)) & (3)) != 0) goto loc_00C19DA7;
    if ((((unsigned int)((unsigned int)(0x40008000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx))))) != 0) goto loc_00C19DA7;
    if ((unsigned int)(v_r11) == 0) goto loc_00C19DA7;
    if ((*(unsigned int *)(a1 + 2136)) != 7) {
    }
    a2 = (a2) << (32);
    result = ((unsigned int)(*(unsigned int *)(v_rbx))) | (a2);
    a2 = (result) ^ (result);
    v_stack_m68 = a2;
    a1 = (a2) ^ (a1 + 2520);
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 >= 1) goto loc_00C19E20;
    if (((*(unsigned int *)(a4)) & ((unsigned int)((unsigned int)(0x40008000ULL)))) != 0) goto loc_00C19E20;
    if ((unsigned int)(v_r11) == 0) goto loc_00C19E20;
    if ((*(unsigned int *)(a1 + 2136)) == 7) goto loc_00C19E2F;
    goto loc_00C19E2F;
loc_00C19E20:
loc_00C19E25:
loc_00C19E2F:
    if ((*(unsigned int *)(v_rip + 4121160)) == 0) goto loc_00C19F0B;
    if ((*(unsigned int *)(v_rip + 4121160)) < 0) goto loc_00C19F0B;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m60 = a2;
    a1 = (a2) ^ (v_r11);
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 >= 5) goto loc_00C19F0B;
    *(unsigned int *)(a1 + 2524) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2524)));
    if (a1 < 5) goto loc_00C19F0B;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m58 = a2;
    a1 = (a2) ^ (v_r11);
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 >= 3) goto loc_00C19F0B;
    if ((*(unsigned int *)(a1 + 2136)) != 7) {
        *(unsigned int *)(a1 + 2524) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2524)));
    }
    a1 = 0;
    if ((*(unsigned __int8 *)(result)) != 0) {
        if (((*(unsigned __int8 *)(a1 + 2203)) & (4)) != 0) { a1 = 1; }
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 2033697))) & (0xF0000000ULL));
    if (((unsigned int)(result)) == 0xC0000000ULL) { a1 = 1; }
    if ((unsigned int)(a1) == 0) goto loc_00C1A5BC;
    if (((*(unsigned int *)(a1 + 2520)) & (0x48000000ULL)) != 0) goto loc_00C1A5BC;
    if ((*(unsigned int *)(a1 + 2136)) == 7) goto loc_00C1A5BC;
    if (((*(unsigned int *)(a1 + 2524)) & (0x10000ULL)) != 0) goto loc_00C1A5BC;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m50 = a2;
    a1 = (a2) ^ (v_r11);
    a2 = (a2) >> (3);
    result = (a2 + a2 * 4) + (a2 + a2 * 4);
    a1 = (a1) - (result);
    if (a1 >= 3) goto loc_00C1A5BC;
    if (*(unsigned __int64 *)(v_rip + 4120772) != 0) goto loc_00C1A569;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m48 = a2;
    v_rbx = (a2) ^ (v_r11);
    a2 = (a2) >> (1);
    result = (v_r11) * (a2);
    v_rbx = (v_rbx) - (result);
    if (((unsigned int)(v_rbx)) > 5) goto loc_00C1A231;
    if (((unsigned int)(v_rbx)) == 5) goto loc_00C1A1DE;
    if ((unsigned int)(v_rbx) == 0) goto loc_00C1A18B;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (1));
    if (condition_is_equal) goto loc_00C1A138;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C1A0E2;
    if (((unsigned int)(result)) == 1) goto loc_00C1A08E;
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A071;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A061;
    v_stack_mD4 = (unsigned int)((unsigned int)(0x70764946ULL));
    goto loc_00C1A44B;
loc_00C1A061:
    v_stack_mD4 = (unsigned int)((unsigned int)(0x70764946ULL));
    goto loc_00C1A42D;
loc_00C1A071:
    result = (unsigned int)(((unsigned int)(0x70764946ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mD4 = (unsigned int)(result);
    goto loc_00C1A448;
loc_00C1A08E:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A0C5;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A0B5;
    v_stack_mD0 = (unsigned int)((unsigned int)(0x72775044ULL));
    goto loc_00C1A44B;
loc_00C1A0B5:
    v_stack_mD0 = (unsigned int)((unsigned int)(0x72775044ULL));
    goto loc_00C1A42D;
loc_00C1A0C5:
    result = (unsigned int)(((unsigned int)(0x72775044ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mD0 = (unsigned int)(result);
    goto loc_00C1A448;
loc_00C1A0E2:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A11B;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A10B;
    v_stack_mCC = (unsigned int)((unsigned int)(0x616D6443ULL));
    goto loc_00C1A44B;
loc_00C1A10B:
    v_stack_mCC = (unsigned int)((unsigned int)(0x616D6443ULL));
    goto loc_00C1A42D;
loc_00C1A11B:
    result = (unsigned int)(((unsigned int)(0x616D6443ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mCC = (unsigned int)(result);
    goto loc_00C1A448;
loc_00C1A138:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A170;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A15E;
    v_stack_mC8 = (unsigned int)((unsigned int)(0x655A6343ULL));
    goto loc_00C1A44B;
loc_00C1A15E:
    v_stack_mC8 = (unsigned int)((unsigned int)(0x655A6343ULL));
    goto loc_00C1A42D;
loc_00C1A170:
    v_r12 = (unsigned int)(((unsigned int)(0x655A6343ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mC8 = (unsigned int)(v_r12);
    goto loc_00C1A448;
loc_00C1A18B:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A1C3;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A1B1;
    v_stack_mC4 = (unsigned int)((unsigned int)(0x63426343ULL));
    goto loc_00C1A44B;
loc_00C1A1B1:
    v_stack_mC4 = (unsigned int)((unsigned int)(0x63426343ULL));
    goto loc_00C1A42D;
loc_00C1A1C3:
    v_r15 = (unsigned int)(((unsigned int)(0x63426343ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mC4 = (unsigned int)(v_r15);
    goto loc_00C1A448;
loc_00C1A1DE:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A216;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A204;
    v_stack_mC0 = (unsigned int)((unsigned int)(0x6944624FULL));
    goto loc_00C1A44B;
loc_00C1A204:
    v_stack_mC0 = (unsigned int)((unsigned int)(0x6944624FULL));
    goto loc_00C1A42D;
loc_00C1A216:
    v_r14 = (unsigned int)(((unsigned int)(0x6944624FULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mC0 = (unsigned int)(v_r14);
    goto loc_00C1A448;
loc_00C1A231:
    a1 = (unsigned int)((v_rbx + 2 + v_rbx + 2 * 2) - (6));
    if (condition_is_equal) goto loc_00C1A3FB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00C1A3AC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00C1A354;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A2FC;
    a2 = (a2) << (32);
    result = (v_rbx + 2) | (a2);
    a2 = (result) ^ (result);
    v_stack_m40 = a2;
    a4 = (unsigned int)((v_r11) ^ ((unsigned int)(a2)));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned int)((result) * ((unsigned int)(a2)));
    v_rbx = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)(a1)));
    v_rbx = (unsigned int)((v_rbx) + (97));
    a4 = (unsigned int)((a4) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) * ((unsigned int)(a2)));
    a3 = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)(result)));
    a3 = (unsigned int)((a3) + (65));
    v_rbx = (unsigned int)((v_rbx) << (8));
    a3 = (unsigned int)((a3) | ((unsigned int)(v_rbx)));
    a4 = (unsigned int)((a4) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned int)((a1) * ((unsigned int)(a2)));
    v_rbx = (unsigned int)(((unsigned int)(a4)) - ((unsigned int)(a1)));
    v_rbx = (unsigned int)((v_rbx) + (97));
    a3 = (unsigned int)((a3) << (8));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(a3)));
    a4 = (unsigned int)((a4) >> (5));
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned int)(((unsigned int)(0x4EC4EC4FULL)) * ((unsigned int)(a2)));
    a4 = (unsigned int)((a4) - ((unsigned int)(result)));
    a4 = (unsigned int)((a4) + (65));
    v_rbx = (unsigned int)((v_rbx) << (8));
    a4 = (unsigned int)((a4) | ((unsigned int)(v_rbx)));
    goto loc_00C1A44E;
loc_00C1A2FC:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A337;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A327;
    v_stack_mBC = (unsigned int)((unsigned int)(0x58434F46ULL));
    goto loc_00C1A44B;
loc_00C1A327:
    v_stack_mBC = (unsigned int)((unsigned int)(0x58434F46ULL));
    goto loc_00C1A42D;
loc_00C1A337:
    result = (unsigned int)(((unsigned int)(0x58434F46ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mBC = (unsigned int)(result);
    goto loc_00C1A448;
loc_00C1A354:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A38F;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A37F;
    v_stack_mB8 = (unsigned int)((unsigned int)(0x42646641ULL));
    goto loc_00C1A44B;
loc_00C1A37F:
    v_stack_mB8 = (unsigned int)((unsigned int)(0x42646641ULL));
    goto loc_00C1A42D;
loc_00C1A38F:
    result = (unsigned int)(((unsigned int)(0x42646641ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mB8 = (unsigned int)(result);
    goto loc_00C1A448;
loc_00C1A3AC:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A3E1;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A3D4;
    v_stack_mB4 = (unsigned int)((unsigned int)(0x63536C41ULL));
    goto loc_00C1A44B;
loc_00C1A3D4:
    v_stack_mB4 = (unsigned int)((unsigned int)(0x63536C41ULL));
    goto loc_00C1A42D;
loc_00C1A3E1:
    result = (unsigned int)(((unsigned int)(0x63536C41ULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mB4 = (unsigned int)(result);
    goto loc_00C1A448;
loc_00C1A3FB:
    a2 = (unsigned int)((a2) >> (1));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2 + a2 * 2)));
    if (condition_is_equal) goto loc_00C1A432;
    if (((unsigned int)(a1)) == 1) goto loc_00C1A420;
    v_stack_mB0 = (unsigned int)((unsigned int)(0x5746744EULL));
    goto loc_00C1A44B;
loc_00C1A420:
    v_stack_mB0 = (unsigned int)((unsigned int)(0x5746744EULL));
loc_00C1A42D:
    goto loc_00C1A44E;
loc_00C1A432:
    v_r13 = (unsigned int)(((unsigned int)(0x5746744EULL)) ^ ((unsigned int)(v_rbx)));
    v_stack_mB0 = (unsigned int)(v_r13);
loc_00C1A448:
    a4 = (unsigned int)(((unsigned int)(v_stack_mB0)) ^ ((unsigned int)(v_rbx)));
loc_00C1A44B:
loc_00C1A44E:
    result = KeGuardDispatchICall(64, (unsigned int)((unsigned int)((unsigned int)(0x1480ULL))), (unsigned int)(a4), a4);
    *(unsigned __int64 *)(v_rip + 4119561) = result;
    if (result == 0) goto loc_00C1A63A;
loc_00C1A48F:
    *(unsigned __int64 *)(result) = 0;
    result = (result) + (8);
    v_rbx = (unsigned int)(((unsigned int)(0x1480ULL)) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    a2 = (656) - (64 - 63);
    if (condition_is_not_equal) goto loc_00C1A48F;
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    if ((unsigned int)(v_rbx) == 0) goto loc_00C1A4B5;
loc_00C1A4AA:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (64 - 63);
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_00C1A4AA;
loc_00C1A4B5:
    result = MmGetPhysicalAddress(result, a2, (unsigned int)(a4), a4);
    result = (result) >> (12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4119487) + 5144) = result;
loc_00C1A4E2:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4119487)) = *(unsigned __int64 *)(v_stack_m98);
    a1 = (*(unsigned __int64 *)(v_rip + 4119487)) + (8);
    v_rbx = (v_stack_m98) + (8);
    a3 = (unsigned int)((512) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    a4 = (64) - (64 - 63);
    if (condition_is_not_equal) goto loc_00C1A4E2;
    if ((unsigned int)(a3) == 0) goto loc_00C1A50C;
loc_00C1A4FD:
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx));
    a1 = (a1) + (64 - 63);
    v_rbx = (v_rbx) + (64 - 63);
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_00C1A4FD;
loc_00C1A50C:
    a1 = (*(unsigned __int64 *)(v_rip + 4119405)) + (512);
loc_00C1A516:
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(v_stack_m98);
    a1 = (a1) + (8);
    v_r10 = (v_stack_m98) + (8);
    a2 = (unsigned int)((512) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    v_r15 = (64) - (64 - 63);
    if (condition_is_not_equal) goto loc_00C1A516;
    if ((unsigned int)(a2) == 0) goto loc_00C1A540;
loc_00C1A530:
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(v_r10));
    a1 = (a1) + (64 - 63);
    v_r10 = (v_r10) + (64 - 63);
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_00C1A530;
loc_00C1A540:
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4119353) + 64) = (unsigned __int16)(*(unsigned __int64 *)(v_rip + 4119353));
    result = (*(unsigned __int64 *)(v_rip + 4119353)) >> (16);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4119353) + 70) = (unsigned __int16)(result);
    result = (*(unsigned __int64 *)(v_rip + 4119353)) >> (32);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4119353) + 72) = (unsigned int)(result);
loc_00C1A569:
    a2 = (unsigned int)((v_stack_p18) - ((unsigned int)(a1)));
    result = (unsigned int)((v_rip - 195770) - (v_stack_p10));
    *(unsigned __int64 *)(a1 + 2272) = *(unsigned __int64 *)(v_rip + 4119353);
    result = (unsigned int)((result) + ((unsigned int)(a2)));
    *(unsigned int *)(a1 + 2324) = (unsigned int)(result);
    *(unsigned int *)(a1 + 2227) = 0x28EC8348ULL;
    *(unsigned int *)(a1 + 2231) = 0x834811FFULL;
    *(unsigned __int16 *)(a1 + 2235) = 0x28C4ULL;
    *(unsigned __int8 *)(a1 + 2237) = 195;
loc_00C1A5BC:
    if (!(condition_is_above_or_equal)) {
        *(unsigned int *)(a1 + 2520) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2520)));
    }
    if (condition_is_below) goto loc_00C1A635;
    v_stack_p20 = (unsigned __int8)((unsigned __int8)(v_cr8));
    v_stack_p10 = v_cr0;
    goto loc_00C1A623;
loc_00C1A623:
    if (v_cr0 != v_cr0) {
        v_cr0 = v_cr0;
    }
loc_00C1A635:
    goto loc_00C1A63C;
loc_00C1A63A:
    result = 0;
loc_00C1A63C:
    v_rsp = (v_rsp) + (240);
    return result;
loc_00C1A650:
    v_stack_p138 = 0xE8000009ULL;
    v_stack_p20 = 8;
    a3 = 0;
    result = KeBugCheckEx((unsigned int)(v_stack_p138), a3 + 4, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00C19464(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t v_cr0;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p138;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (240);
    if (Arg4 != 0) {
        result = v_rip - 191030;
        result = (uint32_t)((result) - ((uint32_t)(Arg2)));
        *(uint16_t *)(result + Arg3 * 1) = 0xE0FFULL;
    }
    result = (uint32_t)((v_rip - 191030) - ((uint32_t)((uint32_t)((uint32_t)(Arg2)))));
    if (Arg4 != 0) {
        *(uint8_t *)(result + Arg3 * 1) = 195;
    }
    *(uint64_t *)(arg1 + 0x8E8) = v_rip - 12686521;
    result = RtlImageNtHeader(v_rip - 12686521, Arg2, Arg3, Arg4);
    *(uint64_t *)(arg1 + 0x8F8) = result;
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x50))) + (v_rip - 12686521);
    *(void **)(arg1 + 0x8F0) = Arg1;
    *(uint32_t *)(arg1 + 0x8CC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3EF0FE)));
    *(uint32_t *)(arg1 + 0x8D0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3EF12A)));
    *(uint32_t *)(arg1 + 0x8D4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3ABB66)));
    if (((uint32_t)(*(uint64_t *)(v_rip + 0x3EF0E1))) != 8) goto loc_00C1A650;
    result = KeGuardDispatchICall(254, Arg2, Arg3, *(uint64_t *)(v_rip + 0x3EF0E1));
    *(uint64_t *)(arg1 + 0x8D8) = *(uint64_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x8D0)) + *(uint64_t *)(result) * 1);
    *(uint16_t *)(arg1 + 0x898) = 0xCF48ULL;
    v_stack_m98 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x18)) + 0x38);
    *(uint64_t *)(arg1 + 0x868) = v_xmm0;
    *(uint64_t *)(arg1 + 0x878) = v_xmm1;
    *(uint64_t *)(arg1 + 0x888) = v_xmm0;
    Arg2 = (Arg2) << (32);
    result = (*(uint64_t *)(gs_base + (0 + 0x18))) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m90 = Arg2;
    local_rbx = (Arg2) ^ (Arg3);
    Arg2 = (Arg2) >> (1);
    result = (Arg3) * (Arg2);
    local_rbx = (local_rbx) - (result);
    if (((uint32_t)(local_rbx)) > 5) goto loc_00C19855;
    if (((uint32_t)(local_rbx)) == 5) goto loc_00C197E8;
    if ((uint32_t)(local_rbx) == 0) goto loc_00C19781;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (1));
    if (condition_is_equal) goto loc_00C19720;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C196CD;
    if (((uint32_t)(result)) == 1) goto loc_00C19682;
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C19653;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1963D;
    v_stack_p20 = (uint32_t)((uint32_t)(0x70764946ULL));
    goto loc_00C19674;
loc_00C1963D:
    v_stack_p20 = (uint32_t)((uint32_t)(0x70764946ULL));
loc_00C1964E:
    goto loc_00C19677;
loc_00C19653:
    result = (uint32_t)(((uint32_t)(0x70764946ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_p20 = (uint32_t)(result);
loc_00C19671:
    Arg4 = (uint32_t)(((uint32_t)(v_stack_p20)) ^ ((uint32_t)(local_rbx)));
loc_00C19674:
loc_00C19677:
    goto loc_00C19A9B;
loc_00C19682:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C196B3;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C196A6;
    v_stack_mF8 = (uint32_t)((uint32_t)(0x72775044ULL));
    goto loc_00C19674;
loc_00C196A6:
    v_stack_mF8 = (uint32_t)((uint32_t)(0x72775044ULL));
    goto loc_00C1964E;
loc_00C196B3:
    result = (uint32_t)(((uint32_t)(0x72775044ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mF8 = (uint32_t)(result);
    goto loc_00C19671;
loc_00C196CD:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C19703;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C196F3;
    v_stack_mF4 = (uint32_t)((uint32_t)(0x616D6443ULL));
    goto loc_00C19674;
loc_00C196F3:
    v_stack_mF4 = (uint32_t)((uint32_t)(0x616D6443ULL));
    goto loc_00C1964E;
loc_00C19703:
    result = (uint32_t)(((uint32_t)(0x616D6443ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mF4 = (uint32_t)(result);
    goto loc_00C19671;
loc_00C19720:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1975A;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1974A;
    v_stack_mF0 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x655A6343ULL))));
    goto loc_00C19773;
loc_00C1974A:
    v_stack_mF0 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x655A6343ULL))));
    goto loc_00C19776;
loc_00C1975A:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x655A6343ULL)))) ^ ((uint32_t)(local_rbx)));
    v_stack_mF0 = (uint32_t)(result);
    Arg4 = (uint32_t)(((uint32_t)(v_stack_mF0)) ^ ((uint32_t)(local_rbx)));
loc_00C19773:
loc_00C19776:
    goto loc_00C19AA1;
loc_00C19781:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C197BB;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C197AB;
    v_stack_mEC = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x63426343ULL))));
    goto loc_00C197D4;
loc_00C197AB:
    v_stack_mEC = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x63426343ULL))));
    goto loc_00C197D7;
loc_00C197BB:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x63426343ULL)))) ^ ((uint32_t)(local_rbx)));
    v_stack_mEC = (uint32_t)(result);
    Arg4 = (uint32_t)(((uint32_t)(v_stack_mEC)) ^ ((uint32_t)(local_rbx)));
loc_00C197D4:
loc_00C197D7:
    goto loc_00C19AA7;
loc_00C197E8:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C19822;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C19812;
    v_stack_mE8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x6944624FULL))));
    goto loc_00C1983B;
loc_00C19812:
    v_stack_mE8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x6944624FULL))));
    goto loc_00C1983E;
loc_00C19822:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x6944624FULL)))) ^ ((uint32_t)(local_rbx)));
    v_stack_mE8 = (uint32_t)(result);
    Arg4 = (uint32_t)(((uint32_t)(v_stack_mE8)) ^ ((uint32_t)(local_rbx)));
loc_00C1983B:
loc_00C1983E:
    goto loc_00C19AAD;
loc_00C19855:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (6));
    if (condition_is_equal) goto loc_00C19A3E;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C199E1;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C19984;
    if (((uint32_t)(result)) == 1) goto loc_00C19927;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m88 = Arg2;
    Arg4 = (uint32_t)((Arg3) ^ ((uint32_t)(Arg2)));
    Arg2 = (uint32_t)((Arg2) >> (3));
    Arg1 = (uint32_t)((result) * ((uint32_t)(Arg2)));
    local_rbx = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)(Arg1)));
    local_rbx = (uint32_t)((local_rbx) + (97));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) * ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)(result)));
    Arg3 = (uint32_t)((Arg3) + (65));
    local_rbx = (uint32_t)((local_rbx) << (8));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(local_rbx)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) * ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (97));
    Arg3 = (uint32_t)((Arg3) << (8));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(Arg3)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) * ((uint32_t)(Arg2)));
    Arg4 = (uint32_t)((Arg4) - ((uint32_t)(result)));
    Arg4 = (uint32_t)((Arg4) + (65));
    Arg1 = (uint32_t)((Arg1) << (8));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(Arg1)));
    goto loc_00C19677;
loc_00C19927:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C19967;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C19957;
    v_stack_mE4 = (uint32_t)((uint32_t)(0x58434F46ULL));
    goto loc_00C19674;
loc_00C19957:
    v_stack_mE4 = (uint32_t)((uint32_t)(0x58434F46ULL));
    goto loc_00C1964E;
loc_00C19967:
    result = (uint32_t)(((uint32_t)(0x58434F46ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mE4 = (uint32_t)(result);
    goto loc_00C19671;
loc_00C19984:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C199C4;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C199B4;
    v_stack_mE0 = (uint32_t)((uint32_t)(0x42646641ULL));
    goto loc_00C19674;
loc_00C199B4:
    v_stack_mE0 = (uint32_t)((uint32_t)(0x42646641ULL));
    goto loc_00C1964E;
loc_00C199C4:
    result = (uint32_t)(((uint32_t)(0x42646641ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mE0 = (uint32_t)(result);
    goto loc_00C19671;
loc_00C199E1:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C19A21;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C19A11;
    v_stack_mDC = (uint32_t)((uint32_t)(0x63536C41ULL));
    goto loc_00C19674;
loc_00C19A11:
    v_stack_mDC = (uint32_t)((uint32_t)(0x63536C41ULL));
    goto loc_00C1964E;
loc_00C19A21:
    result = (uint32_t)(((uint32_t)(0x63536C41ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mDC = (uint32_t)(result);
    goto loc_00C19671;
loc_00C19A3E:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C19A7F;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C19A6F;
    v_stack_mD8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x5746744EULL))));
    goto loc_00C19A98;
loc_00C19A6F:
    v_stack_mD8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x5746744EULL))));
    goto loc_00C19A9B;
loc_00C19A7F:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x5746744EULL)))) ^ ((uint32_t)(local_rbx)));
    v_stack_mD8 = (uint32_t)(result);
    Arg4 = (uint32_t)(((uint32_t)(v_stack_mD8)) ^ ((uint32_t)(local_rbx)));
loc_00C19A98:
loc_00C19A9B:
loc_00C19AA1:
loc_00C19AA7:
loc_00C19AAD:
    result = KeGuardDispatchICall(64, 432, (uint32_t)(Arg4), Arg4);
    *(uint64_t *)(arg1 + 0x900) = result;
    if (result == 0) goto loc_00C1A63A;
    result = (result) - (-128);
    result = (result) & (-128);
    *(uint64_t *)(arg1 + 0x900) = result;
    *(uint32_t *)(arg1 + 0x89C) = 0x8748050FULL;
    *(uint32_t *)(arg1 + 0x8A0) = 0x6481240CULL;
    *(uint32_t *)(arg1 + 0x8A4) = 0xFEFF1024ULL;
    *(uint32_t *)(arg1 + 0x8A8) = 0xCF48FFFFULL;
    *(uint8_t *)(arg1 + 0x89A) = 195;
    local_r11 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x678) * 1)) != ((uint8_t)(*(uint8_t *)(arg1 + 0x680)))) goto loc_00C19BEA;
    result = 0;
    Arg1 = 0;
    v_stack_mA8 = 0;
    v_stack_mA4 = (uint32_t)(local_rbx);
    v_stack_mA0 = 0;
    v_stack_m9C = 432;
    if (0 < 7) goto loc_00C19BA4;
    Arg1 = 0;
    v_stack_mA8 = (uint32_t)(local_r11 + 7);
    v_stack_mA4 = (uint32_t)(local_rbx);
    v_stack_mA0 = 0;
    v_stack_m9C = 432;
    if (condition_is_below) { local_r11 = (uint32_t)(local_r11 + 1); }
    goto loc_00C19BA9;
loc_00C19BA4:
loc_00C19BA9:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x660) * 1)) != 6) goto loc_00C19BEF;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x670) * 1))) != 60) goto loc_00C19BC3;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x668) * 1))) == 3) goto loc_00C19BE5;
loc_00C19BC3:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x670) * 1))) != 63) goto loc_00C19BCF;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x668) * 1))) == 2) goto loc_00C19BE5;
loc_00C19BCF:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x670) * 1))) != 69) goto loc_00C19BDA;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x668) * 1))) == 1) goto loc_00C19BE5;
loc_00C19BDA:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x670) * 1))) != 70) goto loc_00C19BEF;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x668) * 1))) != 1) goto loc_00C19BEF;
loc_00C19BE5:
    local_r11 = 0;
    goto loc_00C19BEF;
loc_00C19BEA:
loc_00C19BEF:
    if (0 != 0) {
    }
    result = KeKvaShadowingActive(Arg1, 432, *(uint64_t *)(arg1 + 0x7E0), *(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x670) * 1));
    if ((uint32_t)(result) != 0) {
    }
    *(uint32_t *)(arg1 + 0x8AC) = 0x242C8348ULL;
    *(uint16_t *)(arg1 + 0x8B0) = 0x4802ULL;
    *(uint8_t *)(arg1 + 0x8B2) = 207;
    local_r11 = 0;
    local_r11 = ((*(uint8_t *)(result)) != 0) ? 1 : 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x1F0B0D))) & (0xF0000000ULL));
    if (((uint32_t)(result)) == 0xC0000000ULL) { local_r11 = 1; }
    if (((*(uint32_t *)(arg1 + 0x9D8)) & (0x8000000ULL)) != 0) goto loc_00C19E25;
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80C))))));
    *(uint32_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x80C)) + arg1 * 1 + 0xB) = (uint32_t)(result);
    Arg2 = (432) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m80 = Arg2;
    Arg1 = (Arg2) ^ (*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x670) * 1));
    Arg2 = (Arg2) >> (3);
    result = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    Arg1 = (Arg1) - (result);
    if (Arg1 >= 1) goto loc_00C19CE9;
    if (((*(uint32_t *)(arg1 + 0x9D8)) & ((uint32_t)((uint32_t)(0x40008000ULL)))) != 0) goto loc_00C19CE9;
    local_rbx = Arg1 + 2520;
    if ((*(uint32_t *)(arg1 + 0x858)) != 7) {
        local_rbx = Arg1 + 2520;
    }
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m78 = Arg2;
    Arg1 = (Arg2) ^ (*(uint8_t *)(*(uint64_t *)(arg1 + 0x7E0) + *(uint64_t *)(arg1 + 0x670) * 1));
    Arg2 = (Arg2) >> (3);
    result = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    Arg1 = (Arg1) - (result);
    if (Arg1 >= 1) goto loc_00C19D53;
    if (((*(uint32_t *)(arg1 + 0x9D8)) & ((uint32_t)((uint32_t)(0x40008000ULL)))) != 0) goto loc_00C19D53;
    if ((*(uint32_t *)(arg1 + 0x858)) != 7) {
        Arg4 = Arg1 + 2520;
    }
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m70 = Arg2;
    Arg2 = (uint8_t)((Arg2) ^ ((uint8_t)(Arg1 + 2520)));
    if ((((uint8_t)(Arg2)) & (3)) != 0) goto loc_00C19DA7;
    if ((((uint32_t)((uint32_t)(0x40008000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx))))) != 0) goto loc_00C19DA7;
    if ((uint32_t)(local_r11) == 0) goto loc_00C19DA7;
    if ((*(uint32_t *)(arg1 + 0x858)) != 7) {
    }
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)(*(uint32_t *)(local_rbx))) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m68 = Arg2;
    Arg1 = (Arg2) ^ (Arg1 + 2520);
    Arg2 = (Arg2) >> (3);
    result = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    Arg1 = (Arg1) - (result);
    if (Arg1 >= 1) goto loc_00C19E20;
    if (((*(uint32_t *)(Arg4)) & ((uint32_t)((uint32_t)(0x40008000ULL)))) != 0) goto loc_00C19E20;
    if ((uint32_t)(local_r11) == 0) goto loc_00C19E20;
    if ((*(uint32_t *)(arg1 + 0x858)) == 7) goto loc_00C19E2F;
    goto loc_00C19E2F;
loc_00C19E20:
loc_00C19E25:
loc_00C19E2F:
    if ((*(uint32_t *)(v_rip + 0x3EE248)) == 0) goto loc_00C19F0B;
    if ((*(uint32_t *)(v_rip + 0x3EE248)) < 0) goto loc_00C19F0B;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m60 = Arg2;
    Arg1 = (Arg2) ^ (local_r11);
    Arg2 = (Arg2) >> (3);
    result = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    Arg1 = (Arg1) - (result);
    if (Arg1 >= 5) goto loc_00C19F0B;
    *(uint32_t *)(arg1 + 0x9DC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9DC)));
    if (Arg1 < 5) goto loc_00C19F0B;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m58 = Arg2;
    Arg1 = (Arg2) ^ (local_r11);
    Arg2 = (Arg2) >> (3);
    result = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    Arg1 = (Arg1) - (result);
    if (Arg1 >= 3) goto loc_00C19F0B;
    if ((*(uint32_t *)(arg1 + 0x858)) != 7) {
        *(uint32_t *)(arg1 + 0x9DC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9DC)));
    }
    Arg1 = 0;
    if ((*(uint8_t *)(result)) != 0) {
        if (((*(uint8_t *)(arg1 + 0x89B)) & (4)) != 0) { Arg1 = 1; }
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x1F0821))) & (0xF0000000ULL));
    if (((uint32_t)(result)) == 0xC0000000ULL) { Arg1 = 1; }
    if ((uint32_t)(Arg1) == 0) goto loc_00C1A5BC;
    if (((*(uint32_t *)(arg1 + 0x9D8)) & (0x48000000ULL)) != 0) goto loc_00C1A5BC;
    if ((*(uint32_t *)(arg1 + 0x858)) == 7) goto loc_00C1A5BC;
    if (((*(uint32_t *)(arg1 + 0x9DC)) & (0x10000ULL)) != 0) goto loc_00C1A5BC;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m50 = Arg2;
    Arg1 = (Arg2) ^ (local_r11);
    Arg2 = (Arg2) >> (3);
    result = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    Arg1 = (Arg1) - (result);
    if (Arg1 >= 3) goto loc_00C1A5BC;
    if (*(uint64_t *)(v_rip + 0x3EE0C4) != 0) goto loc_00C1A569;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m48 = Arg2;
    local_rbx = (Arg2) ^ (local_r11);
    Arg2 = (Arg2) >> (1);
    result = (local_r11) * (Arg2);
    local_rbx = (local_rbx) - (result);
    if (((uint32_t)(local_rbx)) > 5) goto loc_00C1A231;
    if (((uint32_t)(local_rbx)) == 5) goto loc_00C1A1DE;
    if ((uint32_t)(local_rbx) == 0) goto loc_00C1A18B;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (1));
    if (condition_is_equal) goto loc_00C1A138;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C1A0E2;
    if (((uint32_t)(result)) == 1) goto loc_00C1A08E;
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A071;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A061;
    v_stack_mD4 = (uint32_t)((uint32_t)(0x70764946ULL));
    goto loc_00C1A44B;
loc_00C1A061:
    v_stack_mD4 = (uint32_t)((uint32_t)(0x70764946ULL));
    goto loc_00C1A42D;
loc_00C1A071:
    result = (uint32_t)(((uint32_t)(0x70764946ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mD4 = (uint32_t)(result);
    goto loc_00C1A448;
loc_00C1A08E:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A0C5;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A0B5;
    v_stack_mD0 = (uint32_t)((uint32_t)(0x72775044ULL));
    goto loc_00C1A44B;
loc_00C1A0B5:
    v_stack_mD0 = (uint32_t)((uint32_t)(0x72775044ULL));
    goto loc_00C1A42D;
loc_00C1A0C5:
    result = (uint32_t)(((uint32_t)(0x72775044ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mD0 = (uint32_t)(result);
    goto loc_00C1A448;
loc_00C1A0E2:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A11B;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A10B;
    v_stack_mCC = (uint32_t)((uint32_t)(0x616D6443ULL));
    goto loc_00C1A44B;
loc_00C1A10B:
    v_stack_mCC = (uint32_t)((uint32_t)(0x616D6443ULL));
    goto loc_00C1A42D;
loc_00C1A11B:
    result = (uint32_t)(((uint32_t)(0x616D6443ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mCC = (uint32_t)(result);
    goto loc_00C1A448;
loc_00C1A138:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A170;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A15E;
    v_stack_mC8 = (uint32_t)((uint32_t)(0x655A6343ULL));
    goto loc_00C1A44B;
loc_00C1A15E:
    v_stack_mC8 = (uint32_t)((uint32_t)(0x655A6343ULL));
    goto loc_00C1A42D;
loc_00C1A170:
    local_r12 = (uint32_t)(((uint32_t)(0x655A6343ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mC8 = (uint32_t)(local_r12);
    goto loc_00C1A448;
loc_00C1A18B:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A1C3;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A1B1;
    v_stack_mC4 = (uint32_t)((uint32_t)(0x63426343ULL));
    goto loc_00C1A44B;
loc_00C1A1B1:
    v_stack_mC4 = (uint32_t)((uint32_t)(0x63426343ULL));
    goto loc_00C1A42D;
loc_00C1A1C3:
    local_r15 = (uint32_t)(((uint32_t)(0x63426343ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mC4 = (uint32_t)(local_r15);
    goto loc_00C1A448;
loc_00C1A1DE:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A216;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A204;
    v_stack_mC0 = (uint32_t)((uint32_t)(0x6944624FULL));
    goto loc_00C1A44B;
loc_00C1A204:
    v_stack_mC0 = (uint32_t)((uint32_t)(0x6944624FULL));
    goto loc_00C1A42D;
loc_00C1A216:
    local_r14 = (uint32_t)(((uint32_t)(0x6944624FULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mC0 = (uint32_t)(local_r14);
    goto loc_00C1A448;
loc_00C1A231:
    Arg1 = (uint32_t)((local_rbx + 2 + local_rbx + 2 * 2) - (6));
    if (condition_is_equal) goto loc_00C1A3FB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00C1A3AC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00C1A354;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A2FC;
    Arg2 = (Arg2) << (32);
    result = (local_rbx + 2) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m40 = Arg2;
    Arg4 = (uint32_t)((local_r11) ^ ((uint32_t)(Arg2)));
    Arg2 = (uint32_t)((Arg2) >> (3));
    Arg1 = (uint32_t)((result) * ((uint32_t)(Arg2)));
    local_rbx = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)(Arg1)));
    local_rbx = (uint32_t)((local_rbx) + (97));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) * ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)(result)));
    Arg3 = (uint32_t)((Arg3) + (65));
    local_rbx = (uint32_t)((local_rbx) << (8));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(local_rbx)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)(Arg2)));
    local_rbx = (uint32_t)(((uint32_t)(Arg4)) - ((uint32_t)(Arg1)));
    local_rbx = (uint32_t)((local_rbx) + (97));
    Arg3 = (uint32_t)((Arg3) << (8));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(Arg3)));
    Arg4 = (uint32_t)((Arg4) >> (5));
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint32_t)(((uint32_t)(0x4EC4EC4FULL)) * ((uint32_t)(Arg2)));
    Arg4 = (uint32_t)((Arg4) - ((uint32_t)(result)));
    Arg4 = (uint32_t)((Arg4) + (65));
    local_rbx = (uint32_t)((local_rbx) << (8));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(local_rbx)));
    goto loc_00C1A44E;
loc_00C1A2FC:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A337;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A327;
    v_stack_mBC = (uint32_t)((uint32_t)(0x58434F46ULL));
    goto loc_00C1A44B;
loc_00C1A327:
    v_stack_mBC = (uint32_t)((uint32_t)(0x58434F46ULL));
    goto loc_00C1A42D;
loc_00C1A337:
    result = (uint32_t)(((uint32_t)(0x58434F46ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mBC = (uint32_t)(result);
    goto loc_00C1A448;
loc_00C1A354:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A38F;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A37F;
    v_stack_mB8 = (uint32_t)((uint32_t)(0x42646641ULL));
    goto loc_00C1A44B;
loc_00C1A37F:
    v_stack_mB8 = (uint32_t)((uint32_t)(0x42646641ULL));
    goto loc_00C1A42D;
loc_00C1A38F:
    result = (uint32_t)(((uint32_t)(0x42646641ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mB8 = (uint32_t)(result);
    goto loc_00C1A448;
loc_00C1A3AC:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A3E1;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A3D4;
    v_stack_mB4 = (uint32_t)((uint32_t)(0x63536C41ULL));
    goto loc_00C1A44B;
loc_00C1A3D4:
    v_stack_mB4 = (uint32_t)((uint32_t)(0x63536C41ULL));
    goto loc_00C1A42D;
loc_00C1A3E1:
    result = (uint32_t)(((uint32_t)(0x63536C41ULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mB4 = (uint32_t)(result);
    goto loc_00C1A448;
loc_00C1A3FB:
    Arg2 = (uint32_t)((Arg2) >> (1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2 + Arg2 * 2)));
    if (condition_is_equal) goto loc_00C1A432;
    if (((uint32_t)(Arg1)) == 1) goto loc_00C1A420;
    v_stack_mB0 = (uint32_t)((uint32_t)(0x5746744EULL));
    goto loc_00C1A44B;
loc_00C1A420:
    v_stack_mB0 = (uint32_t)((uint32_t)(0x5746744EULL));
loc_00C1A42D:
    goto loc_00C1A44E;
loc_00C1A432:
    local_r13 = (uint32_t)(((uint32_t)(0x5746744EULL)) ^ ((uint32_t)(local_rbx)));
    v_stack_mB0 = (uint32_t)(local_r13);
loc_00C1A448:
    Arg4 = (uint32_t)(((uint32_t)(v_stack_mB0)) ^ ((uint32_t)(local_rbx)));
loc_00C1A44B:
loc_00C1A44E:
    result = KeGuardDispatchICall(64, (uint32_t)((uint32_t)((uint32_t)(0x1480ULL))), (uint32_t)(Arg4), Arg4);
    *(uint64_t *)(v_rip + 0x3EDC09) = result;
    if (result == 0) goto loc_00C1A63A;
loc_00C1A48F:
    *(uint64_t *)(result) = 0;
    result = (result) + (8);
    local_rbx = (uint32_t)(((uint32_t)(0x1480ULL)) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    Arg2 = (656) - (64 - 63);
    if (condition_is_not_equal) goto loc_00C1A48F;
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    if ((uint32_t)(local_rbx) == 0) goto loc_00C1A4B5;
loc_00C1A4AA:
    *(uint8_t *)(result) = 0;
    result = (result) + (64 - 63);
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_00C1A4AA;
loc_00C1A4B5:
    result = MmGetPhysicalAddress(result, Arg2, (uint32_t)(Arg4), Arg4);
    result = (result) >> (12);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x3EDBBF) + 0x1418) = result;
loc_00C1A4E2:
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x3EDBBF)) = *(uint64_t *)(v_stack_m98);
    Arg1 = (*(uint64_t *)(v_rip + 0x3EDBBF)) + (8);
    local_rbx = (v_stack_m98) + (8);
    Arg3 = (uint32_t)((512) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    Arg4 = (64) - (64 - 63);
    if (condition_is_not_equal) goto loc_00C1A4E2;
    if ((uint32_t)(Arg3) == 0) goto loc_00C1A50C;
loc_00C1A4FD:
    *(uint8_t *)(arg1) = (uint8_t)(*(uint8_t *)(local_rbx));
    Arg1 = (Arg1) + (64 - 63);
    local_rbx = (local_rbx) + (64 - 63);
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_00C1A4FD;
loc_00C1A50C:
    Arg1 = (*(uint64_t *)(v_rip + 0x3EDB6D)) + (512);
loc_00C1A516:
    *(uint64_t *)(arg1) = *(uint64_t *)(v_stack_m98);
    Arg1 = (Arg1) + (8);
    local_r10 = (v_stack_m98) + (8);
    Arg2 = (uint32_t)((512) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    local_r15 = (64) - (64 - 63);
    if (condition_is_not_equal) goto loc_00C1A516;
    if ((uint32_t)(Arg2) == 0) goto loc_00C1A540;
loc_00C1A530:
    *(uint8_t *)(arg1) = (uint8_t)(*(uint8_t *)(local_r10));
    Arg1 = (Arg1) + (64 - 63);
    local_r10 = (local_r10) + (64 - 63);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_00C1A530;
loc_00C1A540:
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x3EDB39) + 0x40) = (uint16_t)(*(uint64_t *)(v_rip + 0x3EDB39));
    result = (*(uint64_t *)(v_rip + 0x3EDB39)) >> (16);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x3EDB39) + 0x46) = (uint16_t)(result);
    result = (*(uint64_t *)(v_rip + 0x3EDB39)) >> (32);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3EDB39) + 0x48) = (uint32_t)(result);
loc_00C1A569:
    Arg2 = (uint32_t)((v_stack_p18) - ((uint32_t)(Arg1)));
    result = (uint32_t)((v_rip - 195770) - (v_stack_p10));
    *(uint64_t *)(arg1 + 0x8E0) = *(uint64_t *)(v_rip + 0x3EDB39);
    result = (uint32_t)((result) + ((uint32_t)(Arg2)));
    *(uint32_t *)(arg1 + 0x914) = (uint32_t)(result);
    *(uint32_t *)(arg1 + 0x8B3) = 0x28EC8348ULL;
    *(uint32_t *)(arg1 + 0x8B7) = 0x834811FFULL;
    *(uint16_t *)(arg1 + 0x8BB) = 0x28C4ULL;
    *(uint8_t *)(arg1 + 0x8BD) = 195;
loc_00C1A5BC:
    if (!(condition_is_above_or_equal)) {
        *(uint32_t *)(arg1 + 0x9D8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8)));
    }
    if (condition_is_below) goto loc_00C1A635;
    v_stack_p20 = (uint8_t)((uint8_t)(v_cr8));
    v_stack_p10 = v_cr0;
    goto loc_00C1A623;
loc_00C1A623:
    if (v_cr0 != v_cr0) {
        v_cr0 = v_cr0;
    }
loc_00C1A635:
    goto loc_00C1A63C;
loc_00C1A63A:
    result = 0;
loc_00C1A63C:
    local_rsp = (local_rsp) + (240);
    return result;
loc_00C1A650:
    v_stack_p138 = 0xE8000009ULL;
    v_stack_p20 = 8;
    Arg3 = 0;
    result = KeBugCheckEx((uint32_t)(v_stack_p138), Arg3 + 4, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x470` | `64` | `R` |
| `Arg1` | `+ 0x660` | `64` | `R` |
| `Arg1` | `+ 0x668` | `64` | `R` |
| `Arg1` | `+ 0x670` | `64` | `R` |
| `Arg1` | `+ 0x678` | `64` | `R` |
| `Arg1` | `+ 0x680` | `8` | `R` |
| `Arg1` | `+ 0x7E0` | `64` | `R` |
| `Arg1` | `+ 0x80C` | `32` | `R` |
| `Arg1` | `+ 0x858` | `32` | `R` |
| `Arg1` | `+ 0x868` | `128` | `W` |
| `Arg1` | `+ 0x878` | `128` | `W` |
| `Arg1` | `+ 0x888` | `128` | `W` |
| `Arg1` | `+ 0x898` | `16` | `W` |
| `Arg1` | `+ 0x89A` | `8` | `W` |
| `Arg1` | `+ 0x89B` | `8` | `R` |
| `Arg1` | `+ 0x89B` | `8` | `R/W` |
| `Arg1` | `+ 0x89C` | `32` | `W` |
| `Arg1` | `+ 0x8A0` | `32` | `W` |
| `Arg1` | `+ 0x8A4` | `32` | `W` |
| `Arg1` | `+ 0x8A8` | `32` | `W` |
| `Arg1` | `+ 0x8AC` | `32` | `W` |
| `Arg1` | `+ 0x8B0` | `16` | `W` |
| `Arg1` | `+ 0x8B2` | `8` | `W` |
| `Arg1` | `+ 0x8B3` | `32` | `W` |
| `Arg1` | `+ 0x8B7` | `32` | `W` |
| `Arg1` | `+ 0x8BB` | `16` | `W` |
| `Arg1` | `+ 0x8BD` | `8` | `W` |
| `Arg1` | `+ 0x8CC` | `32` | `W` |
| `Arg1` | `+ 0x8D0` | `32` | `R` |
| `Arg1` | `+ 0x8D0` | `32` | `W` |

추가 오프셋 14개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C19464&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
