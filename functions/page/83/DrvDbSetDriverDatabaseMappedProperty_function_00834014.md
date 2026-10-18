# DrvDbSetDriverDatabaseMappedProperty

- RVA: `0x00834014`–`0x008345E0` (길이 `1,484` bytes)
- VA: `0x0000000140834014`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DABC4`
- 디코드: `380`개 명령, `1,484/1,484` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x00834061` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x008341A9` → [DrvDbFindDatabaseNode](../93/DrvDbFindDatabaseNode_function_00932628.md) (function, `0x00932628`)
- `0x00834233` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00834243` → [DrvDbLoadDatabaseNode](../93/DrvDbLoadDatabaseNode_function_00931668.md) (function, `0x00931668`)
- `0x0083424A` → [DrvDbUnloadDatabaseNode](../93/DrvDbUnloadDatabaseNode_function_0093183C.md) (function, `0x0093183C`)
- `0x0083441B` → [DrvDbFindDatabaseNode](../93/DrvDbFindDatabaseNode_function_00932628.md) (function, `0x00932628`)
- `0x00834482` → [DrvDbOpenObjectRegKey](../93/DrvDbOpenObjectRegKey_function_00931060.md) (function, `0x00931060`)
- `0x0083449F` → [DrvDbOpenDriverDatabaseRegKey](../AA/DrvDbOpenDriverDatabaseRegKey_function_00AA0FB8.md) (function, `0x00AA0FB8`)
- `0x008344D8` → [DrvDbSetRegValueMappedProperty](DrvDbSetRegValueMappedProperty_function_00834DC8.md) (function, `0x00834DC8`)
- `0x00834555` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x00834583` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x0083458C` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x008345A5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008345AA` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008345BF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [DrvDbCreateDatabaseNode](DrvDbCreateDatabaseNode_function_0083533C.md) at `0x0083562B`
- [DrvDbInitializeDatabaseNodeVersion](DrvDbInitializeDatabaseNodeVersion_function_00835B94.md) at `0x00835C03`
- [DrvDbInitializeDatabaseNodeVersion](DrvDbInitializeDatabaseNodeVersion_function_00835B94.md) at `0x00835C3A`
- [DrvDbDispatchDriverDatabase](../8E/DrvDbDispatchDriverDatabase_function_008E6EC0.md) at `0x008E6F93`

### Static image references
- `0x0083404D` → RVA `0x00AFD260` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0083407B` → RVA `0x000224C8` (`.rdata`; read)
- `0x00834088` → RVA `0x000224D0` (`.rdata`; read)
- `0x008340D4` → RVA `0x000217A0` (`.rdata`; read)
- `0x008340E1` → RVA `0x000217A8` (`.rdata`; read)
- `0x00834140` → RVA `0x00011F10` (`.rdata`; read)
- `0x0083414D` → RVA `0x00011F18` (`.rdata`; read)
- `0x00834166` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008341C7` → RVA `0x00022540` (`.rdata`; read)
- `0x008341D4` → RVA `0x00022548` (`.rdata`; read)
- `0x008342CF` → RVA `0x00022368` (`.rdata`; read)
- `0x008342DC` → RVA `0x00022370` (`.rdata`; read)
- `0x0083450F` → RVA `0x00023648` (`.rdata`; read)
- `0x0083451C` → RVA `0x00023650` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00834061` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00834233` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00834583` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x008345A5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008345AA` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008345BF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00834014  48 8B C4                        mov rax, rsp
00834017  48 89 58 08                     mov qword ptr [rax + 8], rbx
0083401B  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
0083401F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00834023  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00834027  55                              push rbp
00834028  57                              push rdi
00834029  41 54                           push r12
0083402B  41 55                           push r13
0083402D  41 57                           push r15
0083402F  48 8B EC                        mov rbp, rsp
00834032  48 83 EC 70                     sub rsp, 0x70
00834036  45 33 FF                        xor r15d, r15d
00834039  4C 8B E2                        mov r12, rdx
0083403C  48 8B F9                        mov rdi, rcx
0083403F  4C 89 7D E8                     mov qword ptr [rbp - 0x18], r15
00834043  0F 57 C0                        xorps xmm0, xmm0
00834046  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
0083404A  49 8B CC                        mov rcx, r12
0083404D  48 8D 15 0C 92 2C 00            lea rdx, [rip + 0x2c920c]
00834054  49 8B D9                        mov rbx, r9
00834057  41 8B F7                        mov esi, r15d
0083405A  45 8B EF                        mov r13d, r15d
0083405D  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00834061  E8 1A C0 CC FF                  call 0x140500080
00834066  44 8B 4B 10                     mov r9d, dword ptr [rbx + 0x10]
0083406A  85 C0                           test eax, eax
0083406C  0F 85 C5 00 00 00               jne 0x140834137
00834072  41 83 F9 06                     cmp r9d, 6
00834076  75 53                           jne 0x1408340cb
00834078  48 8B 03                        mov rax, qword ptr [rbx]
0083407B  48 2B 05 46 E4 7E FF            sub rax, qword ptr [rip - 0x811bba]
00834082  75 0B                           jne 0x14083408f
00834084  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00834088  48 2B 05 41 E4 7E FF            sub rax, qword ptr [rip - 0x811bbf]
0083408F  48 85 C0                        test rax, rax
00834092  0F 85 95 00 00 00               jne 0x14083412d
00834098  83 7D 50 11                     cmp dword ptr [rbp + 0x50], 0x11
0083409C  0F 85 0F 05 00 00               jne 0x1408345b1
008340A2  83 7D 60 01                     cmp dword ptr [rbp + 0x60], 1
008340A6  0F 85 05 05 00 00               jne 0x1408345b1
008340AC  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008340B0  48 85 C0                        test rax, rax
008340B3  0F 84 F8 04 00 00               je 0x1408345b1
008340B9  80 38 FF                        cmp byte ptr [rax], 0xff
008340BC  0F 85 F4 04 00 00               jne 0x1408345b6
008340C2  4C 89 7F 30                     mov qword ptr [rdi + 0x30], r15
008340C6  E9 EB 04 00 00                  jmp 0x1408345b6
008340CB  41 83 F9 0B                     cmp r9d, 0xb
008340CF  75 5C                           jne 0x14083412d
008340D1  48 8B 03                        mov rax, qword ptr [rbx]
008340D4  48 2B 05 C5 D6 7E FF            sub rax, qword ptr [rip - 0x81293b]
008340DB  75 0B                           jne 0x1408340e8
008340DD  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008340E1  48 2B 05 C0 D6 7E FF            sub rax, qword ptr [rip - 0x812940]
008340E8  48 85 C0                        test rax, rax
008340EB  75 40                           jne 0x14083412d
008340ED  83 7D 50 07                     cmp dword ptr [rbp + 0x50], 7
008340F1  0F 85 BA 04 00 00               jne 0x1408345b1
008340F7  83 7D 60 04                     cmp dword ptr [rbp + 0x60], 4
008340FB  0F 85 B0 04 00 00               jne 0x1408345b1
00834101  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00834105  48 85 C0                        test rax, rax
00834108  0F 84 A3 04 00 00               je 0x1408345b1
0083410E  8B 00                           mov eax, dword ptr [rax]
00834110  B9 00 00 00 D0                  mov ecx, 0xd0000000
00834115  23 C1                           and eax, ecx
00834117  89 47 0C                        mov dword ptr [rdi + 0xc], eax
0083411A  3D 00 00 00 10                  cmp eax, 0x10000000
0083411F  0F 85 91 04 00 00               jne 0x1408345b6
00834125  89 4F 0C                        mov dword ptr [rdi + 0xc], ecx
00834128  E9 89 04 00 00                  jmp 0x1408345b6
0083412D  BE BB 00 00 C0                  mov esi, 0xc00000bb
00834132  E9 7F 04 00 00                  jmp 0x1408345b6
00834137  41 83 F9 02                     cmp r9d, 2
0083413B  75 26                           jne 0x140834163
0083413D  48 8B 03                        mov rax, qword ptr [rbx]
00834140  48 2B 05 C9 DD 7D FF            sub rax, qword ptr [rip - 0x822237]
00834147  75 0B                           jne 0x140834154
00834149  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0083414D  48 2B 05 C4 DD 7D FF            sub rax, qword ptr [rip - 0x82223c]
00834154  48 85 C0                        test rax, rax
00834157  75 0A                           jne 0x140834163
00834159  BE 22 00 00 C0                  mov esi, 0xc0000022
0083415E  E9 53 04 00 00                  jmp 0x1408345b6
00834163  41 8B D7                        mov edx, r15d
00834166  4C 8D 1D 93 BE 7C FF            lea r11, [rip - 0x83416d]
0083416D  83 FA 08                        cmp edx, 8
00834170  0F 83 11 02 00 00               jae 0x140834387
00834176  8B C2                           mov eax, edx
00834178  4D 8B 84 C3 40 A5 E0 00         mov r8, qword ptr [r11 + rax*8 + 0xe0a540]
00834180  45 39 48 10                     cmp dword ptr [r8 + 0x10], r9d
00834184  75 15                           jne 0x14083419b
00834186  49 8B 08                        mov rcx, qword ptr [r8]
00834189  48 2B 0B                        sub rcx, qword ptr [rbx]
0083418C  75 08                           jne 0x140834196
0083418E  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
00834192  48 2B 4B 08                     sub rcx, qword ptr [rbx + 8]
00834196  48 85 C9                        test rcx, rcx
00834199  74 04                           je 0x14083419f
0083419B  FF C2                           inc edx
0083419D  EB CE                           jmp 0x14083416d
0083419F  4C 8D 45 E0                     lea r8, [rbp - 0x20]
008341A3  49 8B D4                        mov rdx, r12
008341A6  48 8B CF                        mov rcx, rdi
008341A9  E8 7A E4 0F 00                  call 0x140932628
008341AE  8B F0                           mov esi, eax
008341B0  85 C0                           test eax, eax
008341B2  0F 88 FE 03 00 00               js 0x1408345b6
008341B8  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
008341BB  83 F8 05                        cmp eax, 5
008341BE  0F 85 99 00 00 00               jne 0x14083425d
008341C4  48 8B 03                        mov rax, qword ptr [rbx]
008341C7  48 2B 05 72 E3 7E FF            sub rax, qword ptr [rip - 0x811c8e]
008341CE  75 0B                           jne 0x1408341db
008341D0  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008341D4  48 2B 05 6D E3 7E FF            sub rax, qword ptr [rip - 0x811c93]
008341DB  48 85 C0                        test rax, rax
008341DE  0F 85 D2 03 00 00               jne 0x1408345b6
008341E4  83 7D 50 11                     cmp dword ptr [rbp + 0x50], 0x11
008341E8  0F 85 C3 03 00 00               jne 0x1408345b1
008341EE  83 7D 60 01                     cmp dword ptr [rbp + 0x60], 1
008341F2  0F 85 B9 03 00 00               jne 0x1408345b1
008341F8  48 8B 75 58                     mov rsi, qword ptr [rbp + 0x58]
008341FC  48 85 F6                        test rsi, rsi
008341FF  0F 84 AC 03 00 00               je 0x1408345b1
00834205  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00834209  8B 48 40                        mov ecx, dword ptr [rax + 0x40]
0083420C  F6 C1 01                        test cl, 1
0083420F  0F 85 44 FF FF FF               jne 0x140834159
00834215  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0083421E  B2 01                           mov dl, 1
00834220  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
00834224  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0083422B  90                              nop
0083422C  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
00834233  E8 E8 0B 9E FF                  call 0x140214e20
00834238  80 3E FF                        cmp byte ptr [rsi], 0xff
0083423B  48 8B D3                        mov rdx, rbx
0083423E  48 8B CF                        mov rcx, rdi
00834241  75 07                           jne 0x14083424a
00834243  E8 20 D4 0F 00                  call 0x140931668
00834248  EB 05                           jmp 0x14083424f
0083424A  E8 ED D5 0F 00                  call 0x14093183c
0083424F  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
00834256  8B F0                           mov esi, eax
00834258  E9 48 03 00 00                  jmp 0x1408345a5
0083425D  83 F8 06                        cmp eax, 6
00834260  75 65                           jne 0x1408342c7
00834262  48 8B 03                        mov rax, qword ptr [rbx]
00834265  48 2B 05 5C E2 7E FF            sub rax, qword ptr [rip - 0x811da4]
0083426C  75 0B                           jne 0x140834279
0083426E  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00834272  48 2B 05 57 E2 7E FF            sub rax, qword ptr [rip - 0x811da9]
00834279  48 85 C0                        test rax, rax
0083427C  0F 85 34 03 00 00               jne 0x1408345b6
00834282  83 7D 50 11                     cmp dword ptr [rbp + 0x50], 0x11
00834286  0F 85 25 03 00 00               jne 0x1408345b1
0083428C  83 7D 60 01                     cmp dword ptr [rbp + 0x60], 1
00834290  0F 85 1B 03 00 00               jne 0x1408345b1
00834296  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0083429A  48 85 C0                        test rax, rax
0083429D  0F 84 0E 03 00 00               je 0x1408345b1
008342A3  80 38 FF                        cmp byte ptr [rax], 0xff
008342A6  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008342AA  75 09                           jne 0x1408342b5
008342AC  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
008342B0  E9 01 03 00 00                  jmp 0x1408345b6
008342B5  48 3B 47 30                     cmp rax, qword ptr [rdi + 0x30]
008342B9  0F 84 03 FE FF FF               je 0x1408340c2
008342BF  48 85 C0                        test rax, rax
008342C2  E9 F5 FD FF FF                  jmp 0x1408340bc
008342C7  83 F8 07                        cmp eax, 7
008342CA  75 5C                           jne 0x140834328
008342CC  48 8B 03                        mov rax, qword ptr [rbx]
008342CF  48 2B 05 92 E0 7E FF            sub rax, qword ptr [rip - 0x811f6e]
008342D6  75 0B                           jne 0x1408342e3
008342D8  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008342DC  48 2B 05 8D E0 7E FF            sub rax, qword ptr [rip - 0x811f73]
008342E3  48 85 C0                        test rax, rax
008342E6  0F 85 CA 02 00 00               jne 0x1408345b6
008342EC  83 7D 50 11                     cmp dword ptr [rbp + 0x50], 0x11
008342F0  0F 85 BB 02 00 00               jne 0x1408345b1
008342F6  83 7D 60 01                     cmp dword ptr [rbp + 0x60], 1
008342FA  0F 85 B1 02 00 00               jne 0x1408345b1
00834300  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00834304  48 85 C0                        test rax, rax
00834307  0F 84 A4 02 00 00               je 0x1408345b1
0083430D  80 38 FF                        cmp byte ptr [rax], 0xff
00834310  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00834314  75 09                           jne 0x14083431f
00834316  83 48 40 04                     or dword ptr [rax + 0x40], 4
0083431A  E9 97 02 00 00                  jmp 0x1408345b6
0083431F  83 60 40 FB                     and dword ptr [rax + 0x40], 0xfffffffb
00834323  E9 8E 02 00 00                  jmp 0x1408345b6
00834328  83 F8 0B                        cmp eax, 0xb
0083432B  0F 85 85 02 00 00               jne 0x1408345b6
00834331  48 8B 03                        mov rax, qword ptr [rbx]
00834334  48 2B 05 65 D4 7E FF            sub rax, qword ptr [rip - 0x812b9b]
0083433B  75 0B                           jne 0x140834348
0083433D  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00834341  48 2B 05 60 D4 7E FF            sub rax, qword ptr [rip - 0x812ba0]
00834348  48 85 C0                        test rax, rax
0083434B  0F 85 65 02 00 00               jne 0x1408345b6
00834351  83 7D 50 07                     cmp dword ptr [rbp + 0x50], 7
00834355  0F 85 56 02 00 00               jne 0x1408345b1
0083435B  83 7D 60 04                     cmp dword ptr [rbp + 0x60], 4
0083435F  0F 85 4C 02 00 00               jne 0x1408345b1
00834365  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00834369  48 85 C9                        test rcx, rcx
0083436C  0F 84 3F 02 00 00               je 0x1408345b1
00834372  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00834376  48 39 45 E0                     cmp qword ptr [rbp - 0x20], rax
0083437A  0F 85 D9 FD FF FF               jne 0x140834159
00834380  8B 01                           mov eax, dword ptr [rcx]
00834382  E9 89 FD FF FF                  jmp 0x140834110
00834387  33 D2                           xor edx, edx
00834389  83 FA 0C                        cmp edx, 0xc
0083438C  73 34                           jae 0x1408343c2
0083438E  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
00834392  4D 8D 93 E0 CC 00 00            lea r10, [r11 + 0xcce0]
00834399  4D 8D 14 CA                     lea r10, [r10 + rcx*8]
0083439D  4D 8B 02                        mov r8, qword ptr [r10]
008343A0  45 39 48 10                     cmp dword ptr [r8 + 0x10], r9d
008343A4  75 15                           jne 0x1408343bb
008343A6  49 8B 08                        mov rcx, qword ptr [r8]
008343A9  48 2B 0B                        sub rcx, qword ptr [rbx]
008343AC  75 08                           jne 0x1408343b6
008343AE  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
008343B2  48 2B 4B 08                     sub rcx, qword ptr [rbx + 8]
008343B6  48 85 C9                        test rcx, rcx
008343B9  74 04                           je 0x1408343bf
008343BB  FF C2                           inc edx
008343BD  EB CA                           jmp 0x140834389
008343BF  4D 8B FA                        mov r15, r10
008343C2  4D 85 FF                        test r15, r15
008343C5  75 67                           jne 0x14083442e
008343C7  33 D2                           xor edx, edx
008343C9  83 FA 04                        cmp edx, 4
008343CC  73 34                           jae 0x140834402
008343CE  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
008343D2  4D 8D 93 C0 CE 00 00            lea r10, [r11 + 0xcec0]
008343D9  4D 8D 14 CA                     lea r10, [r10 + rcx*8]
008343DD  4D 8B 02                        mov r8, qword ptr [r10]
008343E0  45 39 48 10                     cmp dword ptr [r8 + 0x10], r9d
008343E4  75 15                           jne 0x1408343fb
008343E6  49 8B 08                        mov rcx, qword ptr [r8]
008343E9  48 2B 0B                        sub rcx, qword ptr [rbx]
008343EC  75 08                           jne 0x1408343f6
008343EE  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
008343F2  48 2B 4B 08                     sub rcx, qword ptr [rbx + 8]
008343F6  48 85 C9                        test rcx, rcx
008343F9  74 04                           je 0x1408343ff
008343FB  FF C2                           inc edx
008343FD  EB CA                           jmp 0x1408343c9
008343FF  4D 8B FA                        mov r15, r10
00834402  4D 85 FF                        test r15, r15
00834405  75 0A                           jne 0x140834411
00834407  BE 16 00 00 C0                  mov esi, 0xc0000016
0083440C  E9 A5 01 00 00                  jmp 0x1408345b6
00834411  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00834415  49 8B D4                        mov rdx, r12
00834418  48 8B CF                        mov rcx, rdi
0083441B  E8 08 E2 0F 00                  call 0x140932628
00834420  8B F0                           mov esi, eax
00834422  85 C0                           test eax, eax
00834424  0F 88 8C 01 00 00               js 0x1408345b6
0083442A  4C 8B 6D E0                     mov r13, qword ptr [rbp - 0x20]
0083442E  44 8B 65 50                     mov r12d, dword ptr [rbp + 0x50]
00834432  45 3B 67 08                     cmp r12d, dword ptr [r15 + 8]
00834436  74 09                           je 0x140834441
00834438  45 85 E4                        test r12d, r12d
0083443B  0F 85 70 01 00 00               jne 0x1408345b1
00834441  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00834445  48 85 C9                        test rcx, rcx
00834448  75 68                           jne 0x1408344b2
0083444A  48 8D 45 E8                     lea rax, [rbp - 0x18]
0083444E  48 8B CF                        mov rcx, rdi
00834451  4D 85 ED                        test r13, r13
00834454  74 33                           je 0x140834489
00834456  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
0083445C  41 B8 01 00 00 00               mov r8d, 1
00834462  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00834468  4C 8B 4D 38                     mov r9, qword ptr [rbp + 0x38]
0083446C  48 8B 57 28                     mov rdx, qword ptr [rdi + 0x28]
00834470  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00834475  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0083447A  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
00834482  E8 D9 CB 0F 00                  call 0x140931060
00834487  EB 1B                           jmp 0x1408344a4
00834489  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0083448F  45 33 C9                        xor r9d, r9d
00834492  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
00834496  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0083449B  45 8D 41 02                     lea r8d, [r9 + 2]
0083449F  E8 14 CB 26 00                  call 0x140aa0fb8
008344A4  8B F0                           mov esi, eax
008344A6  85 C0                           test eax, eax
008344A8  0F 88 08 01 00 00               js 0x1408345b6
008344AE  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
008344B2  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
008344B6  45 8B CC                        mov r9d, r12d
008344B9  44 8B 6D 60                     mov r13d, dword ptr [rbp + 0x60]
008344BD  48 85 C0                        test rax, rax
008344C0  48 8B 7D 58                     mov rdi, qword ptr [rbp + 0x58]
008344C4  4D 8B C7                        mov r8, r15
008344C7  48 0F 45 C8                     cmovne rcx, rax
008344CB  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
008344D0  48 8B D1                        mov rdx, rcx
008344D3  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008344D8  E8 EB 08 00 00                  call 0x140834dc8
008344DD  45 33 FF                        xor r15d, r15d
008344E0  8B F0                           mov esi, eax
008344E2  85 C0                           test eax, eax
008344E4  0F 88 CC 00 00 00               js 0x1408345b6
008344EA  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008344EE  48 85 C0                        test rax, rax
008344F1  0F 84 BF 00 00 00               je 0x1408345b6
008344F7  8B 40 40                        mov eax, dword ptr [rax + 0x40]
008344FA  A8 10                           test al, 0x10
008344FC  0F 84 B4 00 00 00               je 0x1408345b6
00834502  83 7B 10 0E                     cmp dword ptr [rbx + 0x10], 0xe
00834506  0F 85 AA 00 00 00               jne 0x1408345b6
0083450C  48 8B 03                        mov rax, qword ptr [rbx]
0083450F  48 2B 05 32 F1 7E FF            sub rax, qword ptr [rip - 0x810ece]
00834516  75 0B                           jne 0x140834523
00834518  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0083451C  48 2B 05 2D F1 7E FF            sub rax, qword ptr [rip - 0x810ed3]
00834523  48 85 C0                        test rax, rax
00834526  0F 85 8A 00 00 00               jne 0x1408345b6
0083452C  45 85 E4                        test r12d, r12d
0083452F  0F 84 81 00 00 00               je 0x1408345b6
00834535  41 83 FD 02                     cmp r13d, 2
00834539  72 76                           jb 0x1408345b1
0083453B  48 85 FF                        test rdi, rdi
0083453E  74 71                           je 0x1408345b1
00834540  49 8B C5                        mov rax, r13
00834543  48 D1 E8                        shr rax, 1
00834546  66 44 39 7C 47 FE               cmp word ptr [rdi + rax*2 - 2], r15w
0083454C  75 63                           jne 0x1408345b1
0083454E  48 8B D7                        mov rdx, rdi
00834551  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00834555  E8 06 93 18 00                  call 0x1409bd860
0083455A  84 C0                           test al, al
0083455C  75 07                           jne 0x140834565
0083455E  BE 9A 00 00 C0                  mov esi, 0xc000009a
00834563  EB 51                           jmp 0x1408345b6
00834565  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0083456E  B2 01                           mov dl, 1
00834570  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
00834574  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0083457B  90                              nop
0083457C  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
00834583  E8 98 08 9E FF                  call 0x140214e20
00834588  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0083458C  E8 6F C2 18 00                  call 0x1409c0800
00834591  0F 10 45 F0                     movups xmm0, xmmword ptr [rbp - 0x10]
00834595  44 89 7F 28                     mov dword ptr [rdi + 0x28], r15d
00834599  F3 0F 7F 47 30                  movdqu xmmword ptr [rdi + 0x30], xmm0
0083459E  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
008345A5  E8 66 B4 A2 FF                  call 0x14025fa10
008345AA  E8 01 93 A2 FF                  call 0x14025d8b0
008345AF  EB 05                           jmp 0x1408345b6
008345B1  BE 0D 00 00 C0                  mov esi, 0xc000000d
008345B6  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
008345BA  48 85 C9                        test rcx, rcx
008345BD  74 05                           je 0x1408345c4
008345BF  E8 EC 8C E7 FF                  call 0x1406ad2b0
008345C4  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
008345C9  8B C6                           mov eax, esi
008345CB  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008345CF  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
008345D3  49 8B E3                        mov rsp, r11
008345D6  41 5F                           pop r15
008345D8  41 5D                           pop r13
008345DA  41 5C                           pop r12
008345DC  5F                              pop rdi
008345DD  5D                              pop rbp
008345DE  C3                              ret
008345DF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DrvDbSetDriverDatabaseMappedProperty(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (112);
    v_r15 = 0;
    v_stack_m40 = 0;
    v_stack_m48 = 0;
    v_stack_m38 = v_xmm0;
    result = wcsicmp(a2, v_rip + 2920972, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00834137;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 6) goto loc_008340CB;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 8461242));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8461247));
    }
    if (result != 0) goto loc_0083412D;
    if (a5 != 17) goto loc_008345B1;
    if (a7 != 1) goto loc_008345B1;
    if (a6 == 0) goto loc_008345B1;
loc_008340BC:
    if ((*(unsigned __int8 *)(a6)) != 255) goto loc_008345B6;
loc_008340C2:
    *(unsigned __int64 *)(a1 + 48) = 0;
    goto loc_008345B6;
loc_008340CB:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 11) goto loc_0083412D;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 8464699));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8464704));
    }
    if (result != 0) goto loc_0083412D;
    if (a5 != 7) goto loc_008345B1;
    if (a7 != 4) goto loc_008345B1;
    if (a6 == 0) goto loc_008345B1;
loc_00834110:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a6))) & ((unsigned int)((unsigned int)(0xD0000000ULL))));
    *(unsigned int *)(a1 + 12) = (unsigned int)(result);
    if (((unsigned int)(result)) != 0x10000000ULL) goto loc_008345B6;
    *(unsigned int *)(a1 + 12) = (unsigned int)((unsigned int)(0xD0000000ULL));
    goto loc_008345B6;
loc_0083412D:
    goto loc_008345B6;
loc_00834137:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 2) goto loc_00834163;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 8528439));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8528444));
    }
    if (result != 0) goto loc_00834163;
loc_00834159:
    goto loc_008345B6;
loc_00834163:
loc_0083416D:
    if (0 >= 8) goto loc_00834387;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8601965 + 0 * 8 + 14722368) + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16))))) goto loc_0083419B;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8601965 + 0 * 8 + 14722368))) - (*(unsigned __int64 *)(a4));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8601965 + 0 * 8 + 14722368) + 8);
        a1 = (a1) - (*(unsigned __int64 *)(a4 + 8));
    }
    if (a1 == 0) goto loc_0083419F;
loc_0083419B:
    a2 = (unsigned int)((0) + 1);
    goto loc_0083416D;
loc_0083419F:
    result = DrvDbFindDatabaseNode(a1, a2, v_stack_m48, (unsigned int)(*(unsigned int *)(a4 + 16)));
    if (sign_flag) goto loc_008345B6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) != 5) goto loc_0083425D;
    result = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(v_rip - 8461454));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(a4 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8461459));
    }
    if (result != 0) goto loc_008345B6;
    if (a5 != 17) goto loc_008345B1;
    if (a7 != 1) goto loc_008345B1;
    if (a6 == 0) goto loc_008345B1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m48 + 64)))) & (1)) != 0) goto loc_00834159;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m48 + 152), 1, v_stack_m48, (unsigned int)(*(unsigned int *)(a4 + 16)));
    if ((*(unsigned __int8 *)(a6)) != 255) goto loc_0083424A;
    result = DrvDbLoadDatabaseNode(a1, v_stack_m48, v_stack_m48, (unsigned int)(*(unsigned int *)(a4 + 16)));
    goto loc_0083424F;
loc_0083424A:
    result = DrvDbUnloadDatabaseNode(a1, v_stack_m48, v_stack_m48, (unsigned int)(*(unsigned int *)(a4 + 16)));
loc_0083424F:
    goto loc_008345A5;
loc_0083425D:
    if (((unsigned int)(result)) != 6) goto loc_008342C7;
    result = (*(unsigned __int64 *)(v_stack_m48)) - (*(unsigned __int64 *)(v_rip - 8461732));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_stack_m48 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8461737));
    }
    if (result != 0) goto loc_008345B6;
    if (a5 != 17) goto loc_008345B1;
    if (a7 != 1) goto loc_008345B1;
    if (a6 == 0) goto loc_008345B1;
    if ((*(unsigned __int8 *)(a6)) != 255) goto loc_008342B5;
    *(unsigned __int64 *)(a1 + 48) = v_stack_m48;
    goto loc_008345B6;
loc_008342B5:
    if (v_stack_m48 == (*(unsigned __int64 *)(a1 + 48))) goto loc_008340C2;
    goto loc_008340BC;
loc_008342C7:
    if (((unsigned int)(v_stack_m48)) != 7) goto loc_00834328;
    result = (*(unsigned __int64 *)(v_stack_m48)) - (*(unsigned __int64 *)(v_rip - 8462190));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_stack_m48 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8462195));
    }
    if (result != 0) goto loc_008345B6;
    if (a5 != 17) goto loc_008345B1;
    if (a7 != 1) goto loc_008345B1;
    if (a6 == 0) goto loc_008345B1;
    if ((*(unsigned __int8 *)(a6)) != 255) goto loc_0083431F;
    goto loc_008345B6;
loc_0083431F:
    goto loc_008345B6;
loc_00834328:
    if (((unsigned int)(v_stack_m48)) != 11) goto loc_008345B6;
    result = (*(unsigned __int64 *)(v_stack_m48)) - (*(unsigned __int64 *)(v_rip - 8465307));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_stack_m48 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8465312));
    }
    if (result != 0) goto loc_008345B6;
    if (a5 != 7) goto loc_008345B1;
    if (a7 != 4) goto loc_008345B1;
    if (a6 == 0) goto loc_008345B1;
    if (v_stack_m48 != (*(unsigned __int64 *)(a1 + 32))) goto loc_00834159;
    goto loc_00834110;
loc_00834387:
    a2 = 0;
loc_00834389:
    if (0 >= 12) goto loc_008343C2;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8601965 + 52448 + a2 + a2 * 4 * 8) + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16))))) goto loc_008343BB;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8601965 + 52448 + a2 + a2 * 4 * 8))) - (*(unsigned __int64 *)(v_stack_m48));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8601965 + 52448 + a2 + a2 * 4 * 8) + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_stack_m48 + 8));
    }
    if (a1 == 0) goto loc_008343BF;
loc_008343BB:
    a2 = (unsigned int)((a2) + 1);
    goto loc_00834389;
loc_008343BF:
loc_008343C2:
    if (v_rip - 8601965 + 52448 + a2 + a2 * 4 * 8 != 0) goto loc_0083442E;
    a2 = 0;
loc_008343C9:
    if (0 >= 4) goto loc_00834402;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8) + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16))))) goto loc_008343FB;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8))) - (*(unsigned __int64 *)(v_stack_m48));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8) + 8);
        a1 = (a1) - (*(unsigned __int64 *)(v_stack_m48 + 8));
    }
    if (a1 == 0) goto loc_008343FF;
loc_008343FB:
    a2 = (unsigned int)((a2) + 1);
    goto loc_008343C9;
loc_008343FF:
loc_00834402:
    if (v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8 != 0) goto loc_00834411;
    goto loc_008345B6;
loc_00834411:
    result = DrvDbFindDatabaseNode(a1, a2, v_stack_m48, (unsigned int)(*(unsigned int *)(a4 + 16)));
    if (sign_flag) goto loc_008345B6;
loc_0083442E:
    if (((unsigned int)((unsigned int)(a5))) == (*(unsigned int *)(v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8 + 8))) goto loc_00834441;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_008345B1;
loc_00834441:
    if (v_stack_p18 != 0) goto loc_008344B2;
    if (v_stack_m48 == 0) goto loc_00834489;
    v_stack_m68 = v_stack_m40;
    v_stack_m70 = 1;
    v_stack_m78 = 2;
    result = DrvDbOpenObjectRegKey(a1, *(unsigned __int64 *)(a1 + 40), 1, v_stack_p10);
    goto loc_008344A4;
loc_00834489:
    a4 = 0;
    v_stack_m78 = result;
    result = DrvDbOpenDriverDatabaseRegKey(a1, v_stack_p10, a4 + 2, a4);
loc_008344A4:
    if (sign_flag) goto loc_008345B6;
loc_008344B2:
    a1 = v_stack_p18;
    if (v_stack_m40 != 0) { a1 = v_stack_m40; }
    v_stack_m70 = (unsigned int)((unsigned int)(a7));
    v_stack_m78 = a6;
    result = DrvDbSetRegValueMappedProperty(a1, a1, v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    v_r15 = 0;
    if (sign_flag) goto loc_008345B6;
    if (v_stack_m48 == 0) goto loc_008345B6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m48 + 64)))) & (16)) == 0) goto loc_008345B6;
    if ((*(unsigned int *)(v_stack_m48 + 16)) != 14) goto loc_008345B6;
    result = (*(unsigned __int64 *)(v_stack_m48)) - (*(unsigned __int64 *)(v_rip - 8457934));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(v_stack_m48 + 8);
        result = (result) - (*(unsigned __int64 *)(v_rip - 8457939));
    }
    if (result != 0) goto loc_008345B6;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_008345B6;
    if (((unsigned int)((unsigned int)(a7))) < 2) goto loc_008345B1;
    if (a6 == 0) goto loc_008345B1;
    result = ((unsigned int)(a7)) >> (1);
    if ((*(unsigned __int16 *)(a6 + result * 2 - 2)) != 0) goto loc_008345B1;
    result = RtlCreateUnicodeString(v_stack_m38, a6, v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    if ((unsigned __int8)(result) != 0) goto loc_00834565;
    goto loc_008345B6;
loc_00834565:
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m48 + 152), 1, v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    result = RtlFreeAnsiString(v_stack_m48 + 48, 1, v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    *(unsigned int *)(v_stack_m48 + 40) = 0;
    *(unsigned __int64 *)(v_stack_m48 + 48) = v_xmm0;
loc_008345A5:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m48 + 152), 1, v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m48 + 152), 1, v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    goto loc_008345B6;
loc_008345B1:
loc_008345B6:
    if (v_stack_m40 != 0) {
        result = ZwClose(v_stack_m40, 1, v_rip - 8601965 + 52928 + a2 + a2 * 4 * 8, (unsigned int)((unsigned int)((unsigned int)(a5))));
    }
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t DrvDbSetDriverDatabaseMappedProperty(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint8_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (112);
    local_r15 = 0;
    v_stack_m40 = 0;
    v_stack_m48 = 0;
    v_stack_m38 = v_xmm0;
    result = wcsicmp(Arg2, v_rip + 2920972, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00834137;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 6) goto loc_008340CB;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x811BBA));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x811BBF));
    }
    if (result != 0) goto loc_0083412D;
    if (Arg5 != 17) goto loc_008345B1;
    if (Arg7 != 1) goto loc_008345B1;
    if (Arg6 == 0) goto loc_008345B1;
loc_008340BC:
    if ((*(uint8_t *)(Arg6)) != 255) goto loc_008345B6;
loc_008340C2:
    *(uint64_t *)(arg1 + 0x30) = 0;
    goto loc_008345B6;
loc_008340CB:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 11) goto loc_0083412D;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x81293B));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x812940));
    }
    if (result != 0) goto loc_0083412D;
    if (Arg5 != 7) goto loc_008345B1;
    if (Arg7 != 4) goto loc_008345B1;
    if (Arg6 == 0) goto loc_008345B1;
loc_00834110:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg6))) & ((uint32_t)((uint32_t)(0xD0000000ULL))));
    *(uint32_t *)(arg1 + 0xC) = (uint32_t)(result);
    if (((uint32_t)(result)) != 0x10000000ULL) goto loc_008345B6;
    *(uint32_t *)(arg1 + 0xC) = (uint32_t)((uint32_t)(0xD0000000ULL));
    goto loc_008345B6;
loc_0083412D:
    goto loc_008345B6;
loc_00834137:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 2) goto loc_00834163;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x822237));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x82223C));
    }
    if (result != 0) goto loc_00834163;
loc_00834159:
    goto loc_008345B6;
loc_00834163:
loc_0083416D:
    if (0 >= 8) goto loc_00834387;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip - 0x83416D + 0x0 * 8 + 0xE0A540) + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10))))) goto loc_0083419B;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x83416D + 0x0 * 8 + 0xE0A540))) - (*(uint64_t *)(arg4));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x83416D + 0x0 * 8 + 0xE0A540) + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(arg4 + 0x8));
    }
    if (Arg1 == NULL) goto loc_0083419F;
loc_0083419B:
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0083416D;
loc_0083419F:
    result = DrvDbFindDatabaseNode(Arg1, Arg2, v_stack_m48, (uint32_t)(*(uint32_t *)(arg4 + 0x10)));
    if (sign_flag) goto loc_008345B6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))) != 5) goto loc_0083425D;
    result = (*(uint64_t *)(arg4)) - (*(uint64_t *)(v_rip - 0x811C8E));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(arg4 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x811C93));
    }
    if (result != 0) goto loc_008345B6;
    if (Arg5 != 17) goto loc_008345B1;
    if (Arg7 != 1) goto loc_008345B1;
    if (Arg6 == 0) goto loc_008345B1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x40)))) & (1)) != 0) goto loc_00834159;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m48 + 0x98), 1, v_stack_m48, (uint32_t)(*(uint32_t *)(arg4 + 0x10)));
    if ((*(uint8_t *)(Arg6)) != 255) goto loc_0083424A;
    result = DrvDbLoadDatabaseNode(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(*(uint32_t *)(arg4 + 0x10)));
    goto loc_0083424F;
loc_0083424A:
    result = DrvDbUnloadDatabaseNode(Arg1, v_stack_m48, v_stack_m48, (uint32_t)(*(uint32_t *)(arg4 + 0x10)));
loc_0083424F:
    goto loc_008345A5;
loc_0083425D:
    if (((uint32_t)(result)) != 6) goto loc_008342C7;
    result = (*(uint64_t *)(v_stack_m48)) - (*(uint64_t *)(v_rip - 0x811DA4));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(v_stack_m48 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x811DA9));
    }
    if (result != 0) goto loc_008345B6;
    if (Arg5 != 17) goto loc_008345B1;
    if (Arg7 != 1) goto loc_008345B1;
    if (Arg6 == 0) goto loc_008345B1;
    if ((*(uint8_t *)(Arg6)) != 255) goto loc_008342B5;
    *(uint64_t *)(arg1 + 0x30) = v_stack_m48;
    goto loc_008345B6;
loc_008342B5:
    if (v_stack_m48 == (*(uint64_t *)(arg1 + 0x30))) goto loc_008340C2;
    goto loc_008340BC;
loc_008342C7:
    if (((uint32_t)(v_stack_m48)) != 7) goto loc_00834328;
    result = (*(uint64_t *)(v_stack_m48)) - (*(uint64_t *)(v_rip - 0x811F6E));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(v_stack_m48 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x811F73));
    }
    if (result != 0) goto loc_008345B6;
    if (Arg5 != 17) goto loc_008345B1;
    if (Arg7 != 1) goto loc_008345B1;
    if (Arg6 == 0) goto loc_008345B1;
    if ((*(uint8_t *)(Arg6)) != 255) goto loc_0083431F;
    goto loc_008345B6;
loc_0083431F:
    goto loc_008345B6;
loc_00834328:
    if (((uint32_t)(v_stack_m48)) != 11) goto loc_008345B6;
    result = (*(uint64_t *)(v_stack_m48)) - (*(uint64_t *)(v_rip - 0x812B9B));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(v_stack_m48 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x812BA0));
    }
    if (result != 0) goto loc_008345B6;
    if (Arg5 != 7) goto loc_008345B1;
    if (Arg7 != 4) goto loc_008345B1;
    if (Arg6 == 0) goto loc_008345B1;
    if (v_stack_m48 != (*(uint64_t *)(arg1 + 0x20))) goto loc_00834159;
    goto loc_00834110;
loc_00834387:
    Arg2 = 0;
loc_00834389:
    if (0 >= 12) goto loc_008343C2;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip - 0x83416D + 0xCCE0 + Arg2 + Arg2 * 4 * 8) + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10))))) goto loc_008343BB;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x83416D + 0xCCE0 + Arg2 + Arg2 * 4 * 8))) - (*(uint64_t *)(v_stack_m48));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x83416D + 0xCCE0 + Arg2 + Arg2 * 4 * 8) + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_stack_m48 + 0x8));
    }
    if (Arg1 == NULL) goto loc_008343BF;
loc_008343BB:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00834389;
loc_008343BF:
loc_008343C2:
    if (v_rip - 8601965 + 52448 + Arg2 + Arg2 * 4 * 8 != 0) goto loc_0083442E;
    Arg2 = 0;
loc_008343C9:
    if (0 >= 4) goto loc_00834402;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip - 0x83416D + 0xCEC0 + Arg2 + Arg2 * 4 * 8) + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10))))) goto loc_008343FB;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x83416D + 0xCEC0 + Arg2 + Arg2 * 4 * 8))) - (*(uint64_t *)(v_stack_m48));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x83416D + 0xCEC0 + Arg2 + Arg2 * 4 * 8) + 0x8);
        Arg1 = (Arg1) - (*(uint64_t *)(v_stack_m48 + 0x8));
    }
    if (Arg1 == NULL) goto loc_008343FF;
loc_008343FB:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_008343C9;
loc_008343FF:
loc_00834402:
    if (v_rip - 8601965 + 52928 + Arg2 + Arg2 * 4 * 8 != 0) goto loc_00834411;
    goto loc_008345B6;
loc_00834411:
    result = DrvDbFindDatabaseNode(Arg1, Arg2, v_stack_m48, (uint32_t)(*(uint32_t *)(arg4 + 0x10)));
    if (sign_flag) goto loc_008345B6;
loc_0083442E:
    if (((uint32_t)((uint32_t)(Arg5))) == (*(uint32_t *)(v_rip - 0x83416D + 0xCEC0 + Arg2 + Arg2 * 4 * 8 + 0x8))) goto loc_00834441;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_008345B1;
loc_00834441:
    if (v_stack_p18 != 0) goto loc_008344B2;
    if (v_stack_m48 == 0) goto loc_00834489;
    v_stack_m68 = v_stack_m40;
    v_stack_m70 = 1;
    v_stack_m78 = 2;
    result = DrvDbOpenObjectRegKey(Arg1, *(uint64_t *)(arg1 + 0x28), 1, v_stack_p10);
    goto loc_008344A4;
loc_00834489:
    Arg4 = 0;
    v_stack_m78 = result;
    result = DrvDbOpenDriverDatabaseRegKey(Arg1, v_stack_p10, Arg4 + 2, Arg4);
loc_008344A4:
    if (sign_flag) goto loc_008345B6;
loc_008344B2:
    Arg1 = v_stack_p18;
    if (v_stack_m40 != 0) { Arg1 = v_stack_m40; }
    v_stack_m70 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m78 = Arg6;
    result = DrvDbSetRegValueMappedProperty(Arg1, Arg1, v_rip - 8601965 + 52928 + Arg2 + Arg2 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    local_r15 = 0;
    if (sign_flag) goto loc_008345B6;
    if (v_stack_m48 == 0) goto loc_008345B6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x40)))) & (16)) == 0) goto loc_008345B6;
    if ((*(uint32_t *)(v_stack_m48 + 0x10)) != 14) goto loc_008345B6;
    result = (*(uint64_t *)(v_stack_m48)) - (*(uint64_t *)(v_rip - 0x810ECE));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(v_stack_m48 + 0x8);
        result = (result) - (*(uint64_t *)(v_rip - 0x810ED3));
    }
    if (result != 0) goto loc_008345B6;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_008345B6;
    if (((uint32_t)((uint32_t)(Arg7))) < 2) goto loc_008345B1;
    if (Arg6 == 0) goto loc_008345B1;
    result = ((uint32_t)(Arg7)) >> (1);
    if ((*(uint16_t *)(Arg6 + result * 2 - 0x2)) != 0) goto loc_008345B1;
    result = RtlCreateUnicodeString(v_stack_m38, Arg6, v_rip - 8601965 + 52928 + Arg2 + Arg2 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    if ((uint8_t)(result) != 0) goto loc_00834565;
    goto loc_008345B6;
loc_00834565:
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m48 + 0x98), 1, v_rip - 8601965 + 52928 + Arg2 + Arg2 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    result = RtlFreeAnsiString(v_stack_m48 + 48, 1, v_rip - 8601965 + 52928 + Arg2 + Arg2 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    *(uint32_t *)(v_stack_m48 + 0x28) = 0;
    *(uint64_t *)(v_stack_m48 + 0x30) = v_xmm0;
loc_008345A5:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m48 + 0x98), 1, v_rip - 8601965 + 52928 + Arg2 + Arg2 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m48 + 0x98), 1, v_rip - 8601965 + 52928 + Arg2 + Arg2 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    goto loc_008345B6;
loc_008345B1:
loc_008345B6:
    if (v_stack_m40 != 0) {
        result = ZwClose(v_stack_m40, 1, v_rip - 8601965 + 52928 + Arg2 + Arg2 * 4 * 8, (uint32_t)((uint32_t)((uint32_t)(Arg5))));
    }
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC` | `32` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00834014&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
