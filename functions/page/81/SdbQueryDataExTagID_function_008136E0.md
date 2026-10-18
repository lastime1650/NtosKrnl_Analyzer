# SdbQueryDataExTagID

- RVA: `0x008136E0`–`0x00813AE4` (길이 `1,028` bytes)
- VA: `0x00000001408136E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AFEC4`
- 디코드: `269`개 명령, `1,028/1,028` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00813744` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x0081376C` → [AslAlloc](../95/AslAlloc_function_0095BD34.md) (function, `0x0095BD34`)
- `0x00813797` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x008137B1` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x008137C7` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (function, `0x0026E9A4`)
- `0x008137ED` → [RtlStringCchCopyNW](../../text/47/RtlStringCchCopyNW_function_0047169C.md) (function, `0x0047169C`)
- `0x00813823` → [SdbpFindFirstNamedTagHelper](../AD/SdbpFindFirstNamedTagHelper_function_00AD4D2C.md) (function, `0x00AD4D2C`)
- `0x0081385B` → [SdbFindFirstTag](../95/SdbFindFirstTag_function_0095E34C.md) (function, `0x0095E34C`)
- `0x0081387F` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00813897` → [SdbReadDWORDTag](../95/SdbReadDWORDTag_function_0095D408.md) (function, `0x0095D408`)
- `0x008138E2` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00813914` → [SdbFindFirstTag](../95/SdbFindFirstTag_function_0095E34C.md) (function, `0x0095E34C`)
- `0x0081394B` → [SdbReadQWORDTag](SdbReadQWORDTag_function_0081706C.md) (function, `0x0081706C`)
- `0x00813997` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008139A9` → [SdbReadDWORDTag](../95/SdbReadDWORDTag_function_0095D408.md) (function, `0x0095D408`)
- `0x008139CD` → [SdbGetTagDataSize](../95/SdbGetTagDataSize_function_0095E230.md) (function, `0x0095E230`)
- `0x008139D9` → [SdbpGetMappedTagData](../95/SdbpGetMappedTagData_function_0095DD24.md) (function, `0x0095DD24`)
- `0x00813A00` → [SdbGetStringTagPtr](../95/SdbGetStringTagPtr_function_0095DDA8.md) (function, `0x0095DDA8`)
- `0x00813A30` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00813A82` → [AslLogCallPrintf](../95/AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)
- `0x00813AC4` → [AslFree](../95/AslFree_function_0095B674.md) (function, `0x0095B674`)

### Direct callers
- [SdbQueryDataEx](SdbQueryDataEx_function_0081363C.md) at `0x008136C9`

### Static image references
- `0x00813706` → RVA `0x00AFE0C0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0081372C` → RVA `0x0003CF50` (`.rdata`; read)
- `0x00813739` → RVA `0x0003CF88` (`.rdata`; read)
- `0x0081377B` → RVA `0x0003CF10` (`.rdata`; read)
- `0x00813864` → RVA `0x0003CED8` (`.rdata`; read)
- `0x008138C5` → RVA `0x0003CEA0` (`.rdata`; read)
- `0x008139EC` → RVA `0x0003CE40` (`.rdata`; read)
- `0x00813A0F` → RVA `0x0003CE70` (`.rdata`; read)
- `0x00813A59` → RVA `0x00013F90` (`.rdata`; read)
- `0x00813A65` → RVA `0x0003CE18` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x008137B1` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x008137C7` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (`PAGE` → `.text`)
  - `0x008137ED` → [RtlStringCchCopyNW](../../text/47/RtlStringCchCopyNW_function_0047169C.md) (`PAGE` → `.text`)
  - `0x00813997` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008136E0  48 8B C4                        mov rax, rsp
008136E3  48 89 58 08                     mov qword ptr [rax + 8], rbx
008136E7  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
008136EB  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
008136EF  55                              push rbp
008136F0  56                              push rsi
008136F1  57                              push rdi
008136F2  41 54                           push r12
008136F4  41 55                           push r13
008136F6  41 56                           push r14
008136F8  41 57                           push r15
008136FA  48 83 EC 40                     sub rsp, 0x40
008136FE  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
00813706  48 8D 1D B3 A9 2E 00            lea rbx, [rip + 0x2ea9b3]
0081370D  45 33 F6                        xor r14d, r14d
00813710  8B EA                           mov ebp, edx
00813712  4C 8B F9                        mov r15, rcx
00813715  44 89 70 18                     mov dword ptr [rax + 0x18], r14d
00813719  4C 89 70 C0                     mov qword ptr [rax - 0x40], r14
0081371D  4C 39 B4 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], r14
00813725  75 2B                           jne 0x140813752
00813727  4D 85 ED                        test r13, r13
0081372A  75 26                           jne 0x140813752
0081372C  4C 8D 0D 1D 98 82 FF            lea r9, [rip - 0x7d67e3]
00813733  41 B8 86 1B 00 00               mov r8d, 0x1b86
00813739  48 8D 15 48 98 82 FF            lea rdx, [rip - 0x7d67b8]
00813740  41 8D 4E 01                     lea ecx, [r14 + 1]
00813744  E8 A3 AD 14 00                  call 0x14095e4ec
00813749  41 8D 5E 57                     lea ebx, [r14 + 0x57]
0081374D  E9 77 03 00 00                  jmp 0x140813ac9
00813752  49 83 CC FF                     or r12, 0xffffffffffffffff
00813756  49 8B C4                        mov rax, r12
00813759  48 FF C0                        inc rax
0081375C  66 44 39 34 43                  cmp word ptr [rbx + rax*2], r14w
00813761  75 F6                           jne 0x140813759
00813763  FF C0                           inc eax
00813765  48 63 F0                        movsxd rsi, eax
00813768  48 8D 14 36                     lea rdx, [rsi + rsi]
0081376C  E8 C3 85 14 00                  call 0x14095bd34
00813771  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00813776  48 85 C0                        test rax, rax
00813779  75 2B                           jne 0x1408137a6
0081377B  4C 8D 0D 8E 97 82 FF            lea r9, [rip - 0x7d6872]
00813782  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00813787  41 B8 92 1B 00 00               mov r8d, 0x1b92
0081378D  48 8D 15 F4 97 82 FF            lea rdx, [rip - 0x7d680c]
00813794  8D 48 01                        lea ecx, [rax + 1]
00813797  E8 50 AD 14 00                  call 0x14095e4ec
0081379C  BB 08 00 00 00                  mov ebx, 8
008137A1  E9 23 03 00 00                  jmp 0x140813ac9
008137A6  48 8B F8                        mov rdi, rax
008137A9  BA 5C 00 00 00                  mov edx, 0x5c
008137AE  48 8B CB                        mov rcx, rbx
008137B1  E8 AA E2 CE FF                  call 0x140501a60
008137B6  4C 8B D8                        mov r11, rax
008137B9  4C 8B C3                        mov r8, rbx
008137BC  48 8B D6                        mov rdx, rsi
008137BF  48 85 C0                        test rax, rax
008137C2  75 15                           jne 0x1408137d9
008137C4  48 8B CF                        mov rcx, rdi
008137C7  E8 D8 B1 A5 FF                  call 0x14026e9a4
008137CC  85 C0                           test eax, eax
008137CE  0F 88 E6 02 00 00               js 0x140813aba
008137D4  49 8B DE                        mov rbx, r14
008137D7  EB 2F                           jmp 0x140813808
008137D9  49 8B FB                        mov rdi, r11
008137DC  48 2B FB                        sub rdi, rbx
008137DF  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008137E4  48 D1 FF                        sar rdi, 1
008137E7  48 8B CB                        mov rcx, rbx
008137EA  4C 8B CF                        mov r9, rdi
008137ED  E8 AA DE C5 FF                  call 0x14047169c
008137F2  85 C0                           test eax, eax
008137F4  0F 88 C0 02 00 00               js 0x140813aba
008137FA  66 44 89 34 7B                  mov word ptr [rbx + rdi*2], r14w
008137FF  49 8D 5B 02                     lea rbx, [r11 + 2]
00813803  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
00813808  41 B9 01 60 00 00               mov r9d, 0x6001
0081380E  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00813813  41 B8 0F 70 00 00               mov r8d, 0x700f
00813819  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0081381E  8B D5                           mov edx, ebp
00813820  49 8B CF                        mov rcx, r15
00813823  E8 04 15 2C 00                  call 0x140ad4d2c
00813828  8B E8                           mov ebp, eax
0081382A  48 85 DB                        test rbx, rbx
0081382D  74 10                           je 0x14081383f
0081382F  66 44 39 33                     cmp word ptr [rbx], r14w
00813833  74 0A                           je 0x14081383f
00813835  85 C0                           test eax, eax
00813837  0F 85 6C FF FF FF               jne 0x1408137a9
0081383D  EB 04                           jmp 0x140813843
0081383F  85 ED                           test ebp, ebp
00813841  75 0A                           jne 0x14081384d
00813843  BB 90 04 00 00                  mov ebx, 0x490
00813848  E9 72 02 00 00                  jmp 0x140813abf
0081384D  41 B8 18 40 00 00               mov r8d, 0x4018
00813853  8B D5                           mov edx, ebp
00813855  49 8B CF                        mov rcx, r15
00813858  41 8B FE                        mov edi, r14d
0081385B  E8 EC AA 14 00                  call 0x14095e34c
00813860  85 C0                           test eax, eax
00813862  75 2B                           jne 0x14081388f
00813864  4C 8D 0D 6D 96 82 FF            lea r9, [rip - 0x7d6993]
0081386B  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
0081386F  41 B8 C3 1B 00 00               mov r8d, 0x1bc3
00813875  48 8D 15 0C 97 82 FF            lea rdx, [rip - 0x7d68f4]
0081387C  8D 48 01                        lea ecx, [rax + 1]
0081387F  E8 68 AC 14 00                  call 0x14095e4ec
00813884  41 8B F6                        mov esi, r14d
00813887  41 8B DE                        mov ebx, r14d
0081388A  E9 02 02 00 00                  jmp 0x140813a91
0081388F  45 33 C0                        xor r8d, r8d
00813892  8B D0                           mov edx, eax
00813894  49 8B CF                        mov rcx, r15
00813897  E8 6C 9B 14 00                  call 0x14095d408
0081389C  8B F8                           mov edi, eax
0081389E  41 8B F6                        mov esi, r14d
008138A1  33 C0                           xor eax, eax
008138A3  85 FF                           test edi, edi
008138A5  0F 84 B6 00 00 00               je 0x140813961
008138AB  8B C7                           mov eax, edi
008138AD  83 E8 01                        sub eax, 1
008138B0  74 57                           je 0x140813909
008138B2  83 E8 02                        sub eax, 2
008138B5  74 4A                           je 0x140813901
008138B7  83 E8 01                        sub eax, 1
008138BA  74 3D                           je 0x1408138f9
008138BC  83 F8 07                        cmp eax, 7
008138BF  74 30                           je 0x1408138f1
008138C1  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
008138C5  4C 8D 0D D4 95 82 FF            lea r9, [rip - 0x7d6a2c]
008138CC  41 B8 E8 1B 00 00               mov r8d, 0x1be8
008138D2  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
008138D6  48 8D 15 AB 96 82 FF            lea rdx, [rip - 0x7d6955]
008138DD  B9 01 00 00 00                  mov ecx, 1
008138E2  E8 05 AC 14 00                  call 0x14095e4ec
008138E7  BB 4E 05 00 00                  mov ebx, 0x54e
008138EC  E9 CE 01 00 00                  jmp 0x140813abf
008138F1  41 B8 07 50 00 00               mov r8d, 0x5007
008138F7  EB 16                           jmp 0x14081390f
008138F9  41 B8 19 40 00 00               mov r8d, 0x4019
008138FF  EB 0E                           jmp 0x14081390f
00813901  41 B8 05 90 00 00               mov r8d, 0x9005
00813907  EB 06                           jmp 0x14081390f
00813909  41 B8 1E 60 00 00               mov r8d, 0x601e
0081390F  8B D5                           mov edx, ebp
00813911  49 8B CF                        mov rcx, r15
00813914  E8 33 AA 14 00                  call 0x14095e34c
00813919  8B D8                           mov ebx, eax
0081391B  33 C0                           xor eax, eax
0081391D  85 DB                           test ebx, ebx
0081391F  0F 84 2C 01 00 00               je 0x140813a51
00813925  8B C7                           mov eax, edi
00813927  83 E8 01                        sub eax, 1
0081392A  0F 84 CB 00 00 00               je 0x1408139fb
00813930  83 E8 02                        sub eax, 2
00813933  0F 84 8F 00 00 00               je 0x1408139c8
00813939  83 E8 01                        sub eax, 1
0081393C  74 63                           je 0x1408139a1
0081393E  83 F8 07                        cmp eax, 7
00813941  75 1C                           jne 0x14081395f
00813943  45 33 C0                        xor r8d, r8d
00813946  8B D3                           mov edx, ebx
00813948  49 8B CF                        mov rcx, r15
0081394B  E8 1C 37 00 00                  call 0x14081706c
00813950  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00813955  4C 8D 74 24 38                  lea r14, [rsp + 0x38]
0081395A  BE 08 00 00 00                  mov esi, 8
0081395F  33 C0                           xor eax, eax
00813961  8B D8                           mov ebx, eax
00813963  85 F6                           test esi, esi
00813965  0F 84 26 01 00 00               je 0x140813a91
0081396B  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00813973  48 85 C9                        test rcx, rcx
00813976  0F 84 10 01 00 00               je 0x140813a8c
0081397C  4D 85 ED                        test r13, r13
0081397F  0F 84 07 01 00 00               je 0x140813a8c
00813985  41 8B 45 00                     mov eax, dword ptr [r13]
00813989  3B C6                           cmp eax, esi
0081398B  0F 82 FB 00 00 00               jb 0x140813a8c
00813991  44 8B C0                        mov r8d, eax
00813994  49 8B D6                        mov rdx, r14
00813997  E8 A4 2E EB FF                  call 0x1406c6840
0081399C  E9 F5 00 00 00                  jmp 0x140813a96
008139A1  45 33 C0                        xor r8d, r8d
008139A4  8B D3                           mov edx, ebx
008139A6  49 8B CF                        mov rcx, r15
008139A9  E8 5A 9A 14 00                  call 0x14095d408
008139AE  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
008139B5  4C 8D B4 24 90 00 00 00         lea r14, [rsp + 0x90]
008139BD  33 C0                           xor eax, eax
008139BF  BE 04 00 00 00                  mov esi, 4
008139C4  8B D8                           mov ebx, eax
008139C6  EB A3                           jmp 0x14081396b
008139C8  8B D3                           mov edx, ebx
008139CA  49 8B CF                        mov rcx, r15
008139CD  E8 5E A8 14 00                  call 0x14095e230
008139D2  8B D3                           mov edx, ebx
008139D4  49 8B CF                        mov rcx, r15
008139D7  8B F0                           mov esi, eax
008139D9  E8 46 A3 14 00                  call 0x14095dd24
008139DE  4C 8B F0                        mov r14, rax
008139E1  33 C0                           xor eax, eax
008139E3  4D 85 F6                        test r14, r14
008139E6  0F 85 75 FF FF FF               jne 0x140813961
008139EC  4C 8D 0D 4D 94 82 FF            lea r9, [rip - 0x7d6bb3]
008139F3  41 B8 0C 1C 00 00               mov r8d, 0x1c0c
008139F9  EB 21                           jmp 0x140813a1c
008139FB  8B D3                           mov edx, ebx
008139FD  49 8B CF                        mov rcx, r15
00813A00  E8 A3 A3 14 00                  call 0x14095dda8
00813A05  4C 8B F0                        mov r14, rax
00813A08  33 C0                           xor eax, eax
00813A0A  4D 85 F6                        test r14, r14
00813A0D  75 2B                           jne 0x140813a3a
00813A0F  4C 8D 0D 5A 94 82 FF            lea r9, [rip - 0x7d6ba6]
00813A16  41 B8 FE 1B 00 00               mov r8d, 0x1bfe
00813A1C  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00813A20  48 8D 15 61 95 82 FF            lea rdx, [rip - 0x7d6a9f]
00813A27  B9 01 00 00 00                  mov ecx, 1
00813A2C  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
00813A30  E8 B7 AA 14 00                  call 0x14095e4ec
00813A35  E9 09 FE FF FF                  jmp 0x140813843
00813A3A  49 FF C4                        inc r12
00813A3D  66 43 39 04 66                  cmp word ptr [r14 + r12*2], ax
00813A42  75 F6                           jne 0x140813a3a
00813A44  42 8D 34 65 02 00 00 00         lea esi, [r12*2 + 2]
00813A4C  E9 10 FF FF FF                  jmp 0x140813961
00813A51  83 FF 01                        cmp edi, 1
00813A54  75 0F                           jne 0x140813a65
00813A56  8D 77 01                        lea esi, [rdi + 1]
00813A59  4C 8D 35 30 05 80 FF            lea r14, [rip - 0x7ffad0]
00813A60  E9 5F FF FF FF                  jmp 0x1408139c4
00813A65  4C 8D 0D AC 93 82 FF            lea r9, [rip - 0x7d6c54]
00813A6C  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
00813A70  41 B8 27 1C 00 00               mov r8d, 0x1c27
00813A76  48 8D 15 0B 95 82 FF            lea rdx, [rip - 0x7d6af5]
00813A7D  B9 01 00 00 00                  mov ecx, 1
00813A82  E8 65 AA 14 00                  call 0x14095e4ec
00813A87  E9 B7 FD FF FF                  jmp 0x140813843
00813A8C  BB 7A 00 00 00                  mov ebx, 0x7a
00813A91  4D 85 ED                        test r13, r13
00813A94  74 04                           je 0x140813a9a
00813A96  41 89 75 00                     mov dword ptr [r13], esi
00813A9A  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00813AA2  48 85 C0                        test rax, rax
00813AA5  74 02                           je 0x140813aa9
00813AA7  89 38                           mov dword ptr [rax], edi
00813AA9  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00813AB1  48 85 C0                        test rax, rax
00813AB4  74 09                           je 0x140813abf
00813AB6  89 28                           mov dword ptr [rax], ebp
00813AB8  EB 05                           jmp 0x140813abf
00813ABA  BB 7A 00 00 00                  mov ebx, 0x7a
00813ABF  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00813AC4  E8 AB 7B 14 00                  call 0x14095b674
00813AC9  8B C3                           mov eax, ebx
00813ACB  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00813AD3  48 83 C4 40                     add rsp, 0x40
00813AD7  41 5F                           pop r15
00813AD9  41 5E                           pop r14
00813ADB  41 5D                           pop r13
00813ADD  41 5C                           pop r12
00813ADF  5F                              pop rdi
00813AE0  5E                              pop rsi
00813AE1  5D                              pop rbp
00813AE2  C3                              ret
00813AE3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SdbQueryDataExTagID(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (64);
    v_r14 = 0;
    *(unsigned int *)(v_rsp + 24) = 0;
    *(unsigned __int64 *)(v_rsp - 64) = 0;
    if (a5 != 0) goto loc_00813752;
    if (a6 != 0) goto loc_00813752;
    result = AslLogCallPrintf(v_r14 + 1, v_rip - 8218552, (unsigned int)(0x1B86ULL), v_rip - 8218595);
    goto loc_00813AC9;
loc_00813752:
    v_r12 = (v_r12) | (-1);
loc_00813759:
    result = (v_r12) + 1;
    if ((*(unsigned __int16 *)(v_r14 + 87 + result * 2)) != 0) goto loc_00813759;
    result = (unsigned int)((result) + 1);
    result = AslAlloc(v_r14 + 1, (int)((unsigned int)(result)) + (int)((unsigned int)(result)) * 1, (unsigned int)(0x1B86ULL), v_rip - 8218595);
    v_stack_m48 = result;
    if (result != 0) goto loc_008137A6;
    v_stack_m58 = v_r14 + 87;
    result = AslLogCallPrintf(result + 1, v_rip - 8218636, (unsigned int)(0x1B92ULL), v_rip - 8218738);
    goto loc_00813AC9;
loc_008137A6:
loc_008137A9:
    result = wcschr(8, 92, (unsigned int)(0x1B92ULL), v_rip - 8218738);
    if (result != 0) goto loc_008137D9;
    result = RtlStringCchCopyW(result, (int)((unsigned int)(result)), 8, v_rip - 8218738);
    if (sign_flag) goto loc_00813ABA;
    goto loc_00813808;
loc_008137D9:
    v_rdi = (result) - (0);
    v_rdi = (v_rdi) >> (1);
    result = RtlStringCchCopyNW(v_stack_m48, (int)((unsigned int)(result)), 8, v_rdi);
    if (sign_flag) goto loc_00813ABA;
    *(unsigned __int16 *)(v_stack_m48 + v_rdi * 2) = 0;
loc_00813808:
    v_stack_m50 = 0;
    v_stack_m58 = v_stack_m48;
    result = SdbpFindFirstNamedTagHelper(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)(0x700FULL), (unsigned int)(0x6001ULL));
    if (result + 2 == 0) goto loc_0081383F;
    if ((*(unsigned __int16 *)(result + 2)) == 0) goto loc_0081383F;
    if ((unsigned int)(result) != 0) goto loc_008137A9;
    goto loc_00813843;
loc_0081383F:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0081384D;
loc_00813843:
    goto loc_00813ABF;
loc_0081384D:
    result = SdbFindFirstTag(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x4018ULL), (unsigned int)(0x6001ULL));
    if ((unsigned int)(result) != 0) goto loc_0081388F;
    v_stack_m58 = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = AslLogCallPrintf(result + 1, v_rip - 8218868, (unsigned int)(0x1BC3ULL), v_rip - 8219027);
    goto loc_00813A91;
loc_0081388F:
    a3 = 0;
    result = SdbReadDWORDTag(a1, (unsigned int)((unsigned int)(result)), a3, v_rip - 8219027);
    result = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00813961;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - (1));
    if (condition_is_equal) goto loc_00813909;
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_00813901;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_008138F9;
    if (((unsigned int)(result)) == 7) goto loc_008138F1;
    v_stack_m50 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m58 = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = AslLogCallPrintf(1, v_rip - 8218965, (unsigned int)(0x1BE8ULL), v_rip - 8219180);
    goto loc_00813ABF;
loc_008138F1:
    goto loc_0081390F;
loc_008138F9:
    goto loc_0081390F;
loc_00813901:
    goto loc_0081390F;
loc_00813909:
loc_0081390F:
    result = SdbFindFirstTag(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x601EULL), v_rip - 8219180);
    result = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00813A51;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - (1));
    if (condition_is_equal) goto loc_008139FB;
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_008139C8;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_008139A1;
    v_rsi = 0;
    if (((unsigned int)(result)) == 7) {
        a3 = 0;
        a2 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = a1;
        result = SdbReadQWORDTag(a1, a2, a3, v_rip - 8219180);
        v_stack_m40 = result;
        v_r14 = v_stack_m40;
        v_rsi = 8;
    }
    result = 0;
loc_00813961:
    if ((unsigned int)(v_rsi) == 0) goto loc_00813A91;
loc_0081396B:
    if (a5 == 0) goto loc_00813A8C;
    if (a6 == 0) goto loc_00813A8C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a6)))) < ((unsigned int)(v_rsi))) goto loc_00813A8C;
    result = memcpy(a5, v_r14, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a6)))), v_rip - 8219180);
    goto loc_00813A96;
loc_008139A1:
    a3 = 0;
    result = SdbReadDWORDTag(a1, 0, a3, v_rip - 8219180);
    v_stack_p18 = (unsigned int)(result);
    result = 0;
loc_008139C4:
    goto loc_0081396B;
loc_008139C8:
    result = SdbGetTagDataSize(a1, 0, a3, v_rip - 8219180);
    result = SdbpGetMappedTagData(a1, 0, a3, v_rip - 8219180);
    result = 0;
    if (0 != 0) goto loc_00813961;
    goto loc_00813A1C;
loc_008139FB:
    result = SdbGetStringTagPtr(a1, 0, (unsigned int)(0x1C0CULL), v_rip - 8219571);
    result = 0;
    if (0 != 0) goto loc_00813A3A;
loc_00813A1C:
    v_stack_m50 = 0;
    v_stack_m58 = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = AslLogCallPrintf(1, v_rip - 8219295, (unsigned int)(0x1BFEULL), v_rip - 8219558);
    goto loc_00813843;
loc_00813A3A:
    v_r12 = (v_r12) + 1;
    if ((*(unsigned __int16 *)(result + v_r12 * 2)) != ((unsigned __int16)(result))) goto loc_00813A3A;
    goto loc_00813961;
loc_00813A51:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 1) goto loc_00813A65;
    goto loc_008139C4;
loc_00813A65:
    v_stack_m58 = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = AslLogCallPrintf(1, v_rip - 8219381, (unsigned int)(0x1C27ULL), v_rip - 8219732);
    goto loc_00813843;
loc_00813A8C:
loc_00813A91:
    if (a6 != 0) {
        *(unsigned int *)(a6) = (unsigned int)((unsigned int)((unsigned int)(result)) + 1);
    }
    if (v_stack_p20 != 0) {
        *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)((unsigned int)(result)));
    }
    if (a7 == 0) goto loc_00813ABF;
    *(unsigned int *)(a7) = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_00813ABF;
loc_00813ABA:
loc_00813ABF:
    result = AslFree(1, v_stack_m48, (unsigned int)(0x1C27ULL), v_rip - 8219732);
loc_00813AC9:
    v_rsp = (v_rsp) + (64);
    return 122;
}
```

## 5. (Beta) C Style

```c
int64_t SdbQueryDataExTagID(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (64);
    local_r14 = 0;
    *(uint32_t *)(local_rsp + 0x18) = 0;
    *(uint64_t *)(local_rsp - 0x40) = 0;
    if (Arg5 != 0) goto loc_00813752;
    if (Arg6 != 0) goto loc_00813752;
    result = AslLogCallPrintf(local_r14 + 1, v_rip - 8218552, (uint32_t)(0x1B86ULL), v_rip - 8218595);
    goto loc_00813AC9;
loc_00813752:
    local_r12 = (local_r12) | (-1);
loc_00813759:
    result = (local_r12) + 1;
    if ((*(uint16_t *)(local_r14 + 0x57 + result * 2)) != 0) goto loc_00813759;
    result = (uint32_t)((result) + 1);
    result = AslAlloc(local_r14 + 1, (int32_t)((uint32_t)(result)) + (int32_t)((uint32_t)(result)) * 1, (uint32_t)(0x1B86ULL), v_rip - 8218595);
    v_stack_m48 = result;
    if (result != 0) goto loc_008137A6;
    v_stack_m58 = local_r14 + 87;
    result = AslLogCallPrintf(result + 1, v_rip - 8218636, (uint32_t)(0x1B92ULL), v_rip - 8218738);
    goto loc_00813AC9;
loc_008137A6:
loc_008137A9:
    result = wcschr(8, 92, (uint32_t)(0x1B92ULL), v_rip - 8218738);
    if (result != 0) goto loc_008137D9;
    result = RtlStringCchCopyW(result, (int32_t)((uint32_t)(result)), 8, v_rip - 8218738);
    if (sign_flag) goto loc_00813ABA;
    goto loc_00813808;
loc_008137D9:
    local_rdi = (result) - (0);
    local_rdi = (local_rdi) >> (1);
    result = RtlStringCchCopyNW(v_stack_m48, (int32_t)((uint32_t)(result)), 8, local_rdi);
    if (sign_flag) goto loc_00813ABA;
    *(uint16_t *)(v_stack_m48 + local_rdi * 2) = 0;
loc_00813808:
    v_stack_m50 = 0;
    v_stack_m58 = v_stack_m48;
    result = SdbpFindFirstNamedTagHelper(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)(0x700FULL), (uint32_t)(0x6001ULL));
    if (result + 2 == 0) goto loc_0081383F;
    if ((*(uint16_t *)(result + 0x2)) == 0) goto loc_0081383F;
    if ((uint32_t)(result) != 0) goto loc_008137A9;
    goto loc_00813843;
loc_0081383F:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0081384D;
loc_00813843:
    goto loc_00813ABF;
loc_0081384D:
    result = SdbFindFirstTag(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x4018ULL), (uint32_t)(0x6001ULL));
    if ((uint32_t)(result) != 0) goto loc_0081388F;
    v_stack_m58 = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = AslLogCallPrintf(result + 1, v_rip - 8218868, (uint32_t)(0x1BC3ULL), v_rip - 8219027);
    goto loc_00813A91;
loc_0081388F:
    Arg3 = 0;
    result = SdbReadDWORDTag(Arg1, (uint32_t)((uint32_t)(result)), Arg3, v_rip - 8219027);
    result = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00813961;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - (1));
    if (condition_is_equal) goto loc_00813909;
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_00813901;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_008138F9;
    if (((uint32_t)(result)) == 7) goto loc_008138F1;
    v_stack_m50 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m58 = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = AslLogCallPrintf(1, v_rip - 8218965, (uint32_t)(0x1BE8ULL), v_rip - 8219180);
    goto loc_00813ABF;
loc_008138F1:
    goto loc_0081390F;
loc_008138F9:
    goto loc_0081390F;
loc_00813901:
    goto loc_0081390F;
loc_00813909:
loc_0081390F:
    result = SdbFindFirstTag(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x601EULL), v_rip - 8219180);
    result = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00813A51;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - (1));
    if (condition_is_equal) goto loc_008139FB;
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_008139C8;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_008139A1;
    local_rsi = 0;
    if (((uint32_t)(result)) == 7) {
        Arg3 = 0;
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = Arg1;
        result = SdbReadQWORDTag(Arg1, Arg2, Arg3, v_rip - 8219180);
        v_stack_m40 = result;
        local_r14 = v_stack_m40;
        local_rsi = 8;
    }
    result = 0;
loc_00813961:
    if ((uint32_t)(local_rsi) == 0) goto loc_00813A91;
loc_0081396B:
    if (Arg5 == 0) goto loc_00813A8C;
    if (Arg6 == 0) goto loc_00813A8C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg6)))) < ((uint32_t)(local_rsi))) goto loc_00813A8C;
    result = memcpy(Arg5, local_r14, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg6)))), v_rip - 8219180);
    goto loc_00813A96;
loc_008139A1:
    Arg3 = 0;
    result = SdbReadDWORDTag(Arg1, 0, Arg3, v_rip - 8219180);
    v_stack_p18 = (uint32_t)(result);
    result = 0;
loc_008139C4:
    goto loc_0081396B;
loc_008139C8:
    result = SdbGetTagDataSize(Arg1, 0, Arg3, v_rip - 8219180);
    result = SdbpGetMappedTagData(Arg1, 0, Arg3, v_rip - 8219180);
    result = 0;
    if (0 != 0) goto loc_00813961;
    goto loc_00813A1C;
loc_008139FB:
    result = SdbGetStringTagPtr(Arg1, 0, (uint32_t)(0x1C0CULL), v_rip - 8219571);
    result = 0;
    if (0 != 0) goto loc_00813A3A;
loc_00813A1C:
    v_stack_m50 = 0;
    v_stack_m58 = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = AslLogCallPrintf(1, v_rip - 8219295, (uint32_t)(0x1BFEULL), v_rip - 8219558);
    goto loc_00813843;
loc_00813A3A:
    local_r12 = (local_r12) + 1;
    if ((*(uint16_t *)(result + local_r12 * 2)) != ((uint16_t)(result))) goto loc_00813A3A;
    goto loc_00813961;
loc_00813A51:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 1) goto loc_00813A65;
    goto loc_008139C4;
loc_00813A65:
    v_stack_m58 = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = AslLogCallPrintf(1, v_rip - 8219381, (uint32_t)(0x1C27ULL), v_rip - 8219732);
    goto loc_00813843;
loc_00813A8C:
loc_00813A91:
    if (Arg6 != 0) {
        *(uint32_t *)(Arg6) = (uint32_t)((uint32_t)((uint32_t)(result)) + 1);
    }
    if (v_stack_p20 != 0) {
        *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)((uint32_t)(result)));
    }
    if (Arg7 == 0) goto loc_00813ABF;
    *(uint32_t *)(Arg7) = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_00813ABF;
loc_00813ABA:
loc_00813ABF:
    result = AslFree(1, v_stack_m48, (uint32_t)(0x1C27ULL), v_rip - 8219732);
loc_00813AC9:
    local_rsp = (local_rsp) + (64);
    return 122;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008136E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
