# inflate_table

- RVA: `0x00600664`–`0x00600AF0` (길이 `1,164` bytes)
- VA: `0x0000000140600664`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D04EC`
- 디코드: `342`개 명령, `1,164/1,164` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x006006E1` → [_report_rangecheckfailure](../4F/_report_rangecheckfailure_function_004F5FDC.md) (function, `0x004F5FDC`)
- `0x006008C9` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [inflate](../5F/inflate_function_005F2280.md) at `0x005F2825`
- [inflate](../5F/inflate_function_005F2280.md) at `0x005F2AD3`
- [inflate](../5F/inflate_function_005F2280.md) at `0x005F2B3F`

### Static image references
- `0x00600680` → RVA `0x00E0A740` (`.data`; read)
- `0x0060082D` → RVA `0x000364E0` (`.rdata`; read)
- `0x0060083B` → RVA `0x00036420` (`.rdata`; read)
- `0x00600844` → RVA `0x000364A0` (`.rdata`; read)
- `0x00600855` → RVA `0x00036460` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00600664  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00600669  55                              push rbp
0060066A  56                              push rsi
0060066B  57                              push rdi
0060066C  41 54                           push r12
0060066E  41 55                           push r13
00600670  41 56                           push r14
00600672  41 57                           push r15
00600674  48 8D 6C 24 E9                  lea rbp, [rsp - 0x17]
00600679  48 81 EC C0 00 00 00            sub rsp, 0xc0
00600680  48 8B 05 B9 A0 80 00            mov rax, qword ptr [rip + 0x80a0b9]
00600687  48 33 C4                        xor rax, rsp
0060068A  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
0060068E  4C 8B 55 77                     mov r10, qword ptr [rbp + 0x77]
00600692  45 33 E4                        xor r12d, r12d
00600695  4C 8B 75 7F                     mov r14, qword ptr [rbp + 0x7f]
00600699  49 8B F1                        mov rsi, r9
0060069C  4C 89 4D AF                     mov qword ptr [rbp - 0x51], r9
006006A0  4C 8B FA                        mov r15, rdx
006006A3  45 8B D8                        mov r11d, r8d
006006A6  8B D9                           mov ebx, ecx
006006A8  45 8D 6C 24 01                  lea r13d, [r12 + 1]
006006AD  48 89 55 BF                     mov qword ptr [rbp - 0x41], rdx
006006B1  89 4D 83                        mov dword ptr [rbp - 0x7d], ecx
006006B4  45 8B CC                        mov r9d, r12d
006006B7  4C 89 55 C7                     mov qword ptr [rbp - 0x39], r10
006006BB  4C 89 75 B7                     mov qword ptr [rbp - 0x49], r14
006006BF  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
006006C4  41 83 F9 0F                     cmp r9d, 0xf
006006C8  77 1D                           ja 0x1406006e7
006006CA  41 8B C1                        mov eax, r9d
006006CD  48 03 C0                        add rax, rax
006006D0  48 83 F8 20                     cmp rax, 0x20
006006D4  73 0B                           jae 0x1406006e1
006006D6  66 44 89 64 05 CF               mov word ptr [rbp + rax - 0x31], r12w
006006DC  45 03 CD                        add r9d, r13d
006006DF  EB E3                           jmp 0x1406006c4
006006E1  E8 F6 58 EF FF                  call 0x1404f5fdc
006006E6  CC                              int3
006006E7  BF 02 00 00 00                  mov edi, 2
006006EC  45 85 C0                        test r8d, r8d
006006EF  74 17                           je 0x140600708
006006F1  49 8B CF                        mov rcx, r15
006006F4  49 8B D3                        mov rdx, r11
006006F7  0F B7 01                        movzx eax, word ptr [rcx]
006006FA  48 03 CF                        add rcx, rdi
006006FD  66 44 01 6C 45 CF               add word ptr [rbp + rax*2 - 0x31], r13w
00600703  49 2B D5                        sub rdx, r13
00600706  75 EF                           jne 0x1406006f7
00600708  41 8B 12                        mov edx, dword ptr [r10]
0060070B  83 C9 FF                        or ecx, 0xffffffff
0060070E  89 4D 87                        mov dword ptr [rbp - 0x79], ecx
00600711  41 B8 0F 00 00 00               mov r8d, 0xf
00600717  41 8B C0                        mov eax, r8d
0060071A  66 44 39 64 45 CF               cmp word ptr [rbp + rax*2 - 0x31], r12w
00600720  75 08                           jne 0x14060072a
00600722  44 03 C1                        add r8d, ecx
00600725  45 3B C5                        cmp r8d, r13d
00600728  73 ED                           jae 0x140600717
0060072A  41 3B D0                        cmp edx, r8d
0060072D  41 8B C8                        mov ecx, r8d
00600730  0F 46 CA                        cmovbe ecx, edx
00600733  45 85 C0                        test r8d, r8d
00600736  75 24                           jne 0x14060075c
00600738  C7 44 24 20 40 01 00 00         mov dword ptr [rsp + 0x20], 0x140
00600740  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
00600744  48 8B 0E                        mov rcx, qword ptr [rsi]
00600747  89 01                           mov dword ptr [rcx], eax
00600749  48 83 06 04                     add qword ptr [rsi], 4
0060074D  49 2B FD                        sub rdi, r13
00600750  75 F2                           jne 0x140600744
00600752  45 89 2A                        mov dword ptr [r10], r13d
00600755  33 C0                           xor eax, eax
00600757  E9 66 01 00 00                  jmp 0x1406008c2
0060075C  45 8B D5                        mov r10d, r13d
0060075F  45 3B C5                        cmp r8d, r13d
00600762  76 15                           jbe 0x140600779
00600764  48 8D 45 D1                     lea rax, [rbp - 0x2f]
00600768  66 44 39 20                     cmp word ptr [rax], r12w
0060076C  75 0B                           jne 0x140600779
0060076E  45 03 D5                        add r10d, r13d
00600771  48 03 C7                        add rax, rdi
00600774  45 3B D0                        cmp r10d, r8d
00600777  72 EF                           jb 0x140600768
00600779  B8 01 00 00 00                  mov eax, 1
0060077E  41 3B CA                        cmp ecx, r10d
00600781  45 8B EA                        mov r13d, r10d
00600784  8B D0                           mov edx, eax
00600786  44 0F 43 E9                     cmovae r13d, ecx
0060078A  44 8B C8                        mov r9d, eax
0060078D  41 83 F9 0F                     cmp r9d, 0xf
00600791  77 18                           ja 0x1406007ab
00600793  41 8B C1                        mov eax, r9d
00600796  03 D2                           add edx, edx
00600798  0F B7 4C 45 CF                  movzx ecx, word ptr [rbp + rax*2 - 0x31]
0060079D  2B D1                           sub edx, ecx
0060079F  78 17                           js 0x1406007b8
006007A1  B8 01 00 00 00                  mov eax, 1
006007A6  44 03 C8                        add r9d, eax
006007A9  EB E2                           jmp 0x14060078d
006007AB  85 D2                           test edx, edx
006007AD  74 11                           je 0x1406007c0
006007AF  85 DB                           test ebx, ebx
006007B1  74 05                           je 0x1406007b8
006007B3  44 3B C0                        cmp r8d, eax
006007B6  74 08                           je 0x1406007c0
006007B8  83 C8 FF                        or eax, 0xffffffff
006007BB  E9 02 01 00 00                  jmp 0x1406008c2
006007C0  BB 01 00 00 00                  mov ebx, 1
006007C5  66 44 89 65 F1                  mov word ptr [rbp - 0xf], r12w
006007CA  49 8B D4                        mov rdx, r12
006007CD  44 8D 4B 0D                     lea r9d, [rbx + 0xd]
006007D1  0F B7 4C 15 D1                  movzx ecx, word ptr [rbp + rdx - 0x2f]
006007D6  66 03 4C 15 F1                  add cx, word ptr [rbp + rdx - 0xf]
006007DB  66 89 4C 15 F3                  mov word ptr [rbp + rdx - 0xd], cx
006007E0  48 03 D7                        add rdx, rdi
006007E3  4C 2B CB                        sub r9, rbx
006007E6  75 E9                           jne 0x1406007d1
006007E8  8B 5D 83                        mov ebx, dword ptr [rbp - 0x7d]
006007EB  45 8B CC                        mov r9d, r12d
006007EE  45 85 DB                        test r11d, r11d
006007F1  74 31                           je 0x140600824
006007F3  49 8B D7                        mov rdx, r15
006007F6  BE 01 00 00 00                  mov esi, 1
006007FB  0F B7 02                        movzx eax, word ptr [rdx]
006007FE  66 85 C0                        test ax, ax
00600801  74 12                           je 0x140600815
00600803  0F B7 4C 45 EF                  movzx ecx, word ptr [rbp + rax*2 - 0x11]
00600808  66 45 89 0C 4E                  mov word ptr [r14 + rcx*2], r9w
0060080D  0F B7 02                        movzx eax, word ptr [rdx]
00600810  66 01 74 45 EF                  add word ptr [rbp + rax*2 - 0x11], si
00600815  44 03 CE                        add r9d, esi
00600818  48 03 D7                        add rdx, rdi
0060081B  45 3B CB                        cmp r9d, r11d
0060081E  72 DB                           jb 0x1406007fb
00600820  48 8B 75 AF                     mov rsi, qword ptr [rbp - 0x51]
00600824  85 DB                           test ebx, ebx
00600826  74 36                           je 0x14060085e
00600828  83 FB 01                        cmp ebx, 1
0060082B  74 17                           je 0x140600844
0060082D  4C 8D 35 AC 5C A3 FF            lea r14, [rip - 0x5ca354]
00600834  45 8B FC                        mov r15d, r12d
00600837  4C 89 75 A7                     mov qword ptr [rbp - 0x59], r14
0060083B  4C 8D 35 DE 5B A3 FF            lea r14, [rip - 0x5ca422]
00600842  EB 24                           jmp 0x140600868
00600844  4C 8D 35 55 5C A3 FF            lea r14, [rip - 0x5ca3ab]
0060084B  41 BF 01 01 00 00               mov r15d, 0x101
00600851  4C 89 75 A7                     mov qword ptr [rbp - 0x59], r14
00600855  4C 8D 35 04 5C A3 FF            lea r14, [rip - 0x5ca3fc]
0060085C  EB 0A                           jmp 0x140600868
0060085E  4C 89 75 A7                     mov qword ptr [rbp - 0x59], r14
00600862  41 BF 14 00 00 00               mov r15d, 0x14
00600868  48 8B 06                        mov rax, qword ptr [rsi]
0060086B  41 8B CD                        mov ecx, r13d
0060086E  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
00600872  45 8B CC                        mov r9d, r12d
00600875  33 C0                           xor eax, eax
00600877  4C 89 75 9F                     mov qword ptr [rbp - 0x61], r14
0060087B  8B D0                           mov edx, eax
0060087D  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00600881  45 8B F4                        mov r14d, r12d
00600884  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00600889  45 8B E5                        mov r12d, r13d
0060088C  44 8D 58 01                     lea r11d, [rax + 1]
00600890  41 D3 E3                        shl r11d, cl
00600893  41 8D 43 FF                     lea eax, [r11 - 1]
00600897  89 45 97                        mov dword ptr [rbp - 0x69], eax
0060089A  83 FB 01                        cmp ebx, 1
0060089D  75 09                           jne 0x1406008a8
0060089F  41 81 FB 34 05 00 00            cmp r11d, 0x534
006008A6  77 15                           ja 0x1406008bd
006008A8  3B DF                           cmp ebx, edi
006008AA  0F 85 06 02 00 00               jne 0x140600ab6
006008B0  41 81 FB 50 02 00 00            cmp r11d, 0x250
006008B7  0F 86 F9 01 00 00               jbe 0x140600ab6
006008BD  B8 01 00 00 00                  mov eax, 1
006008C2  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
006008C6  48 33 CC                        xor rcx, rsp
006008C9  E8 72 BD 0A 00                  call 0x1406ac640
006008CE  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
006008D6  48 81 C4 C0 00 00 00            add rsp, 0xc0
006008DD  41 5F                           pop r15
006008DF  41 5E                           pop r14
006008E1  41 5D                           pop r13
006008E3  41 5C                           pop r12
006008E5  5F                              pop rdi
006008E6  5E                              pop rsi
006008E7  5D                              pop rbp
006008E8  C3                              ret
006008E9  CC                              int3
006008EA  44 8B 74 24 28                  mov r14d, dword ptr [rsp + 0x28]
006008EF  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
006008F3  41 8A C2                        mov al, r10b
006008F6  2A C2                           sub al, dl
006008F8  88 44 24 21                     mov byte ptr [rsp + 0x21], al
006008FC  41 8B C6                        mov eax, r14d
006008FF  0F B7 0C 41                     movzx ecx, word ptr [rcx + rax*2]
00600903  8D 41 01                        lea eax, [rcx + 1]
00600906  41 3B C7                        cmp eax, r15d
00600909  73 0B                           jae 0x140600916
0060090B  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
0060090F  66 89 4C 24 22                  mov word ptr [rsp + 0x22], cx
00600914  EB 2C                           jmp 0x140600942
00600916  41 3B CF                        cmp ecx, r15d
00600919  72 1D                           jb 0x140600938
0060091B  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0060091F  41 2B CF                        sub ecx, r15d
00600922  8A 04 48                        mov al, byte ptr [rax + rcx*2]
00600925  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00600929  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
0060092D  0F B7 04 48                     movzx eax, word ptr [rax + rcx*2]
00600931  66 89 44 24 22                  mov word ptr [rsp + 0x22], ax
00600936  EB 0A                           jmp 0x140600942
00600938  C6 44 24 20 60                  mov byte ptr [rsp + 0x20], 0x60
0060093D  66 89 5C 24 22                  mov word ptr [rsp + 0x22], bx
00600942  48 8B 75 8F                     mov rsi, qword ptr [rbp - 0x71]
00600946  B8 01 00 00 00                  mov eax, 1
0060094B  44 8B F0                        mov r14d, eax
0060094E  41 8B CA                        mov ecx, r10d
00600951  2B CA                           sub ecx, edx
00600953  41 8B D9                        mov ebx, r9d
00600956  41 D3 E6                        shl r14d, cl
00600959  8B D0                           mov edx, eax
0060095B  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
0060095F  41 8B CC                        mov ecx, r12d
00600962  D3 E2                           shl edx, cl
00600964  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
00600968  D3 EB                           shr ebx, cl
0060096A  03 DA                           add ebx, edx
0060096C  89 55 9B                        mov dword ptr [rbp - 0x65], edx
0060096F  41 2B DE                        sub ebx, r14d
00600972  89 04 9E                        mov dword ptr [rsi + rbx*4], eax
00600975  41 2B D6                        sub edx, r14d
00600978  75 F5                           jne 0x14060096f
0060097A  48 8B 75 AF                     mov rsi, qword ptr [rbp - 0x51]
0060097E  8D 42 01                        lea eax, [rdx + 1]
00600981  8B D0                           mov edx, eax
00600983  41 8D 4A FF                     lea ecx, [r10 - 1]
00600987  D3 E2                           shl edx, cl
00600989  EB 02                           jmp 0x14060098d
0060098B  D1 EA                           shr edx, 1
0060098D  41 85 D1                        test r9d, edx
00600990  75 F9                           jne 0x14060098b
00600992  33 DB                           xor ebx, ebx
00600994  85 D2                           test edx, edx
00600996  74 0E                           je 0x1406009a6
00600998  8D 42 FF                        lea eax, [rdx - 1]
0060099B  44 23 C8                        and r9d, eax
0060099E  8D 43 01                        lea eax, [rbx + 1]
006009A1  44 03 CA                        add r9d, edx
006009A4  EB 03                           jmp 0x1406009a9
006009A6  44 8B CB                        mov r9d, ebx
006009A9  44 8B 74 24 28                  mov r14d, dword ptr [rsp + 0x28]
006009AE  B9 FF FF 00 00                  mov ecx, 0xffff
006009B3  44 03 F0                        add r14d, eax
006009B6  41 8B C2                        mov eax, r10d
006009B9  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
006009BE  66 01 4C 45 CF                  add word ptr [rbp + rax*2 - 0x31], cx
006009C3  75 1B                           jne 0x1406009e0
006009C5  45 3B D0                        cmp r10d, r8d
006009C8  0F 84 EF 00 00 00               je 0x140600abd
006009CE  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
006009D2  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
006009D6  42 0F B7 0C 71                  movzx ecx, word ptr [rcx + r14*2]
006009DB  44 0F B7 14 48                  movzx r10d, word ptr [rax + rcx*2]
006009E0  8B 54 24 24                     mov edx, dword ptr [rsp + 0x24]
006009E4  45 3B D5                        cmp r10d, r13d
006009E7  0F 86 02 FF FF FF               jbe 0x1406008ef
006009ED  44 8B 75 97                     mov r14d, dword ptr [rbp - 0x69]
006009F1  45 23 F1                        and r14d, r9d
006009F4  44 3B 75 87                     cmp r14d, dword ptr [rbp - 0x79]
006009F8  0F 84 EC FE FF FF               je 0x1406008ea
006009FE  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00600A01  85 D2                           test edx, edx
00600A03  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
00600A07  45 8B E2                        mov r12d, r10d
00600A0A  41 0F 44 D5                     cmove edx, r13d
00600A0E  44 2B E2                        sub r12d, edx
00600A11  89 54 24 24                     mov dword ptr [rsp + 0x24], edx
00600A15  48 8D 0C 81                     lea rcx, [rcx + rax*4]
00600A19  B8 01 00 00 00                  mov eax, 1
00600A1E  48 89 4D 8F                     mov qword ptr [rbp - 0x71], rcx
00600A22  8B D0                           mov edx, eax
00600A24  41 8B CC                        mov ecx, r12d
00600A27  D3 E2                           shl edx, cl
00600A29  45 3B D0                        cmp r10d, r8d
00600A2C  73 2A                           jae 0x140600a58
00600A2E  41 8B DA                        mov ebx, r10d
00600A31  8B F8                           mov edi, eax
00600A33  8B C3                           mov eax, ebx
00600A35  0F B7 4C 45 CF                  movzx ecx, word ptr [rbp + rax*2 - 0x31]
00600A3A  2B D1                           sub edx, ecx
00600A3C  85 D2                           test edx, edx
00600A3E  7E 0C                           jle 0x140600a4c
00600A40  44 03 E7                        add r12d, edi
00600A43  03 DF                           add ebx, edi
00600A45  03 D2                           add edx, edx
00600A47  41 3B D8                        cmp ebx, r8d
00600A4A  72 E7                           jb 0x140600a33
00600A4C  48 8B 75 AF                     mov rsi, qword ptr [rbp - 0x51]
00600A50  BF 02 00 00 00                  mov edi, 2
00600A55  8D 47 FF                        lea eax, [rdi - 1]
00600A58  8B 5D 83                        mov ebx, dword ptr [rbp - 0x7d]
00600A5B  41 8B CC                        mov ecx, r12d
00600A5E  D3 E0                           shl eax, cl
00600A60  44 03 D8                        add r11d, eax
00600A63  83 FB 01                        cmp ebx, 1
00600A66  75 0D                           jne 0x140600a75
00600A68  41 81 FB 34 05 00 00            cmp r11d, 0x534
00600A6F  0F 87 48 FE FF FF               ja 0x1406008bd
00600A75  3B DF                           cmp ebx, edi
00600A77  75 0D                           jne 0x140600a86
00600A79  41 81 FB 50 02 00 00            cmp r11d, 0x250
00600A80  0F 87 37 FE FF FF               ja 0x1406008bd
00600A86  48 8B 06                        mov rax, qword ptr [rsi]
00600A89  8B 54 24 24                     mov edx, dword ptr [rsp + 0x24]
00600A8D  44 89 75 87                     mov dword ptr [rbp - 0x79], r14d
00600A91  46 88 24 B0                     mov byte ptr [rax + r14*4], r12b
00600A95  48 8B 06                        mov rax, qword ptr [rsi]
00600A98  46 88 6C B0 01                  mov byte ptr [rax + r14*4 + 1], r13b
00600A9D  48 8B 0E                        mov rcx, qword ptr [rsi]
00600AA0  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00600AA4  48 2B C1                        sub rax, rcx
00600AA7  48 C1 F8 02                     sar rax, 2
00600AAB  66 42 89 44 B1 02               mov word ptr [rcx + r14*4 + 2], ax
00600AB1  44 8B 74 24 28                  mov r14d, dword ptr [rsp + 0x28]
00600AB6  33 DB                           xor ebx, ebx
00600AB8  E9 32 FE FF FF                  jmp 0x1406008ef
00600ABD  45 85 C9                        test r9d, r9d
00600AC0  74 18                           je 0x140600ada
00600AC2  48 8B 55 8F                     mov rdx, qword ptr [rbp - 0x71]
00600AC6  41 8B C9                        mov ecx, r9d
00600AC9  C6 44 24 20 40                  mov byte ptr [rsp + 0x20], 0x40
00600ACE  66 89 5C 24 22                  mov word ptr [rsp + 0x22], bx
00600AD3  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
00600AD7  89 04 8A                        mov dword ptr [rdx + rcx*4], eax
00600ADA  41 8B C3                        mov eax, r11d
00600ADD  48 C1 E0 02                     shl rax, 2
00600AE1  48 01 06                        add qword ptr [rsi], rax
00600AE4  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00600AE8  44 89 28                        mov dword ptr [rax], r13d
00600AEB  E9 65 FC FF FF                  jmp 0x140600755
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall inflate_table(int a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m4F;
    unsigned __int16 v_stack_m5E;
    unsigned __int64 v_stack_m7E;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p21;
    unsigned __int16 v_stack_p22;
    unsigned int v_stack_p24;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 8429753)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r12 = 0;
    v_stack_mA0 = a4;
    v_stack_m90 = a2;
    v_stack_mCC = a1;
    v_stack_m88 = a5;
    v_stack_m98 = a6;
    v_stack_mD8 = 0;
loc_006006C4:
    if (0 > 15) goto loc_006006E7;
    result = (0) + (0);
    if (result >= 32) goto loc_006006E1;
    *(unsigned __int16 *)(v_stack_m4F + result * 1 - 49) = 0;
    a4 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    goto loc_006006C4;
loc_006006E1:
    result = _report_rangecheckfailure(a1, a2, a3, a4);
loc_006006E7:
    if (a3 == 0) goto loc_00600708;
loc_006006F7:
    a1 = (a2) + (2);
    a2 = ((unsigned int)(a3)) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_006006F7;
loc_00600708:
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    v_stack_mC8 = a1;
loc_00600717:
    if ((*(unsigned __int16 *)(v_stack_m4F + 15 * 2 - 49)) != 0) goto loc_0060072A;
    a3 = (unsigned int)((15) + (a1));
    if (a3 >= ((unsigned int)(v_r12 + 1))) goto loc_00600717;
loc_0060072A:
    a1 = (unsigned int)(a3);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5)))) <= a3) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a5))); }
    if (a3 != 0) goto loc_0060075C;
    v_stack_mD8 = 320;
loc_00600744:
    *(unsigned int *)(*(unsigned __int64 *)(a4)) = (unsigned int)((unsigned int)(v_stack_mD8));
    v_rdi = (2) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_00600744;
    *(unsigned int *)(a5) = (unsigned int)(v_r12 + 1);
loc_00600755:
    result = 0;
    goto loc_006008C2;
loc_0060075C:
    if (a3 <= ((unsigned int)(v_r12 + 1))) goto loc_00600779;
loc_00600768:
    if ((*(unsigned __int16 *)(v_stack_m7E)) != 0) goto loc_00600779;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r12 + 1))) + ((unsigned int)(v_r12 + 1)));
    result = (v_stack_m7E) + (v_rdi);
    if (((unsigned int)(v_r10)) < a3) goto loc_00600768;
loc_00600779:
    v_r13 = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(*(unsigned __int64 *)(a4))) >= ((unsigned int)(v_r10))) { v_r13 = (unsigned int)(*(unsigned __int64 *)(a4)); }
loc_0060078D:
    if (1 > 15) goto loc_006007AB;
    a2 = (unsigned int)((1) + (1));
    a2 = (unsigned int)((a2) - ((unsigned int)(*(unsigned __int16 *)(v_stack_m4F + 1 * 2 - 49))));
    if (sign_flag) goto loc_006007B8;
    a4 = (unsigned int)((1) + (1));
    goto loc_0060078D;
loc_006007AB:
    if ((unsigned int)(a2) == 0) goto loc_006007C0;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_006007B8;
    if (a3 == 1) goto loc_006007C0;
loc_006007B8:
    result = (unsigned int)((1) | (0xFFFFFFFFULL));
    goto loc_006008C2;
loc_006007C0:
    v_stack_m5E = 0;
loc_006007D1:
    a1 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m4F + 0 * 1 - 47)) + (*(unsigned __int16 *)(v_stack_m4F + 0 * 1 - 15)));
    *(unsigned __int16 *)(v_stack_m4F + 0 * 1 - 13) = (unsigned __int16)(a1);
    a2 = (0) + (v_rdi);
    a4 = (1 + 13) - (1);
    if (condition_is_not_equal) goto loc_006007D1;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00600824;
loc_006007FB:
    result = *(unsigned __int16 *)(a2);
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) != 0) {
        a1 = *(unsigned __int16 *)(v_stack_m4F + *(unsigned __int16 *)(a2) * 2 - 17);
        *(unsigned __int16 *)(a6 + a1 * 2) = 0;
        result = *(unsigned __int16 *)(a2);
    }
    a4 = (unsigned int)((0) + (1));
    a2 = (a2) + (v_rdi);
    if (((unsigned int)(a4)) < ((unsigned int)((unsigned int)(a3)))) goto loc_006007FB;
loc_00600824:
    if ((unsigned int)((unsigned int)(v_stack_mCC)) == 0) goto loc_0060085E;
    if (((unsigned int)((unsigned int)(v_stack_mCC))) == 1) goto loc_00600844;
    v_stack_mA8 = v_rip - 6071124;
    goto loc_00600868;
loc_00600844:
    v_stack_mA8 = v_rip - 6071211;
    goto loc_00600868;
loc_0060085E:
    v_stack_mA8 = v_rip - 6071292;
loc_00600868:
    v_stack_mC0 = *(unsigned __int64 *)(v_stack_mA0);
    result = 0;
    v_stack_mB0 = v_rip - 6071292;
    v_stack_mD4 = 0;
    v_stack_mD0 = 0;
    v_r11 = (unsigned int)((result + 1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r13)))));
    v_stack_mB8 = (unsigned int)(v_r11 - 1);
    if (((unsigned int)((unsigned int)(v_stack_mCC))) != 1) goto loc_006008A8;
    if (((unsigned int)(v_r11)) > 0x534ULL) goto loc_006008BD;
loc_006008A8:
    if (((unsigned int)((unsigned int)(v_stack_mCC))) != ((unsigned int)(v_rdi))) goto loc_00600AB6;
    if (((unsigned int)(v_r11)) <= 592) goto loc_00600AB6;
loc_006008BD:
loc_006008C2:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, 0, a3, 0);
    v_rsp = (v_rsp) + (192);
    return result;
loc_006008EA:
loc_006008EF:
    result = (unsigned __int8)(((unsigned __int8)(v_r10)) - (0));
    v_stack_p21 = (unsigned __int8)(result);
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m98 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p28))) * 2) + 1)) >= 20) goto loc_00600916;
    v_stack_p20 = (unsigned __int8)(v_stack_p8);
    v_stack_p22 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m98 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p28))) * 2));
    goto loc_00600942;
loc_00600916:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m98 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p28))) * 2))) < 20) goto loc_00600938;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_m98 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p28))) * 2)) - (20));
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mB0 + a1 * 2));
    v_stack_p22 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_mA8 + a1 * 2));
    goto loc_00600942;
loc_00600938:
    v_stack_p20 = 96;
    v_stack_p22 = (unsigned __int16)(v_stack_p8);
loc_00600942:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - (0));
    v_r14 = (unsigned int)((1) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13)))))));
    v_rbx = (unsigned int)((0) >> ((unsigned __int8)((unsigned int)(v_stack_p24))));
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(a2)));
    v_stack_mB4 = (unsigned int)(a2);
loc_0060096F:
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_r14)));
    *(unsigned int *)(v_stack_mC0 + v_rbx * 4) = (unsigned int)((unsigned int)(v_stack_p20));
    a2 = (unsigned int)((a2) - ((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_0060096F;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) << ((unsigned __int8)(v_r10 - 1)));
    goto loc_0060098D;
loc_0060098B:
    a2 = (unsigned int)((a2) >> (1));
loc_0060098D:
    if (((0) & ((unsigned int)(a2))) != 0) goto loc_0060098B;
    v_rbx = 0;
    if ((unsigned int)(a2) == 0) goto loc_006009A6;
    a4 = (unsigned int)((0) & ((unsigned int)(a2 - 1)));
    a4 = (unsigned int)((a4) + ((unsigned int)(a2)));
    goto loc_006009A9;
loc_006009A6:
loc_006009A9:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_p28)) + ((unsigned int)(v_rbx + 1)));
    v_stack_p28 = (unsigned int)(v_r14);
    if (condition_is_not_equal) goto loc_006009E0;
    if (((unsigned int)(v_r10)) == a3) goto loc_00600ABD;
loc_006009E0:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m90 + *(unsigned __int16 *)(v_stack_m98 + v_r14 * 2) * 2))) <= ((unsigned int)(v_r13))) goto loc_006008EF;
    v_r14 = (unsigned int)(((unsigned int)(v_stack_mB8)) & (0));
    if (((unsigned int)(v_r14)) == v_stack_mC8) goto loc_006008EA;
    a2 = (unsigned int)(v_stack_p24);
    if ((unsigned int)((unsigned int)(v_stack_p24)) == 0) { a2 = (unsigned int)(v_r13); }
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m90 + *(unsigned __int16 *)(v_stack_m98 + v_r14 * 2) * 2)))) - ((unsigned int)(a2)));
    v_stack_p24 = (unsigned int)(a2);
    v_stack_mC0 = v_stack_mC0 + (unsigned int)(v_stack_mB4) * 4;
    a2 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r12)))));
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m90 + *(unsigned __int16 *)(v_stack_m98 + v_r14 * 2) * 2))) >= a3) goto loc_00600A58;
loc_00600A33:
    a2 = (unsigned int)((a2) - ((unsigned int)(*(unsigned __int16 *)(v_stack_m4F + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m90 + *(unsigned __int16 *)(v_stack_m98 + v_r14 * 2) * 2))))) * 2 - 49))));
    if (condition_is_less_or_equal) goto loc_00600A4C;
    v_r12 = (unsigned int)((v_r12) + (1));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m90 + *(unsigned __int16 *)(v_stack_m98 + v_r14 * 2) * 2)))) + (1));
    a2 = (unsigned int)((a2) + ((unsigned int)(a2)));
    if (((unsigned int)(v_rbx)) < a3) goto loc_00600A33;
loc_00600A4C:
loc_00600A58:
    result = (unsigned int)((2 - 1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r12)))));
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(result)));
    if (((unsigned int)((unsigned int)(v_stack_mCC))) != 1) goto loc_00600A75;
    if (((unsigned int)(v_r11)) > 0x534ULL) goto loc_006008BD;
loc_00600A75:
    if (((unsigned int)((unsigned int)(v_stack_mCC))) != 2) goto loc_00600A86;
    if (((unsigned int)(v_r11)) > 592) goto loc_006008BD;
loc_00600A86:
    v_stack_mC8 = (unsigned int)(v_r14);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_mA0) + v_r14 * 4) = (unsigned __int8)(v_r12);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_mA0) + v_r14 * 4 + 1) = (unsigned __int8)(v_r13);
    result = (v_stack_mC0) - (*(unsigned __int64 *)(v_stack_mA0));
    result = (result) >> (2);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mA0) + v_r14 * 4 + 2) = (unsigned __int16)(result);
loc_00600AB6:
    v_rbx = 0;
    goto loc_006008EF;
loc_00600ABD:
    if (0 != 0) {
        a2 = v_stack_mC0;
        a1 = 0;
        v_stack_p20 = 64;
        v_stack_p22 = 0;
        result = v_stack_p20;
        *(unsigned int *)(a2 + a1 * 4) = (unsigned int)(result);
    }
    result = ((unsigned int)((unsigned int)(v_r11))) << (2);
    *(unsigned int *)(v_stack_m88) = (unsigned int)(v_r13);
    goto loc_00600755;
}
```

## 5. (Beta) C Style

```c
int64_t inflate_table(int32_t Arg1, void *Arg2, int32_t Arg3, void *Arg4, int64_t Arg5, void *Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m4F;
    uint16_t v_stack_m5E;
    uint64_t v_stack_m7E;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint8_t v_stack_p20;
    uint8_t v_stack_p21;
    uint16_t v_stack_p22;
    uint32_t v_stack_p24;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x80A0B9)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r12 = 0;
    v_stack_mA0 = Arg4;
    v_stack_m90 = Arg2;
    v_stack_mCC = Arg1;
    v_stack_m88 = Arg5;
    v_stack_m98 = Arg6;
    v_stack_mD8 = 0;
loc_006006C4:
    if (0 > 15) goto loc_006006E7;
    result = (0) + (0);
    if (result >= 32) goto loc_006006E1;
    *(uint16_t *)(v_stack_m4F + result * 1 - 0x31) = 0;
    Arg4 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    goto loc_006006C4;
loc_006006E1:
    result = _report_rangecheckfailure(Arg1, Arg2, Arg3, Arg4);
loc_006006E7:
    if (Arg3 == 0) goto loc_00600708;
loc_006006F7:
    Arg1 = (Arg2) + (2);
    Arg2 = ((uint32_t)(Arg3)) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_006006F7;
loc_00600708:
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    v_stack_mC8 = Arg1;
loc_00600717:
    if ((*(uint16_t *)(v_stack_m4F + 0xF * 2 - 0x31)) != 0) goto loc_0060072A;
    Arg3 = (uint32_t)((15) + (Arg1));
    if (Arg3 >= ((uint32_t)(local_r12 + 1))) goto loc_00600717;
loc_0060072A:
    Arg1 = (uint32_t)(Arg3);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg5)))) <= Arg3) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg5))); }
    if (Arg3 != 0) goto loc_0060075C;
    v_stack_mD8 = 320;
loc_00600744:
    *(uint32_t *)(*(uint64_t *)(arg4)) = (uint32_t)((uint32_t)(v_stack_mD8));
    local_rdi = (2) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_00600744;
    *(uint32_t *)(Arg5) = (uint32_t)(local_r12 + 1);
loc_00600755:
    result = 0;
    goto loc_006008C2;
loc_0060075C:
    if (Arg3 <= ((uint32_t)(local_r12 + 1))) goto loc_00600779;
loc_00600768:
    if ((*(uint16_t *)(v_stack_m7E)) != 0) goto loc_00600779;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r12 + 1))) + ((uint32_t)(local_r12 + 1)));
    result = (v_stack_m7E) + (local_rdi);
    if (((uint32_t)(local_r10)) < Arg3) goto loc_00600768;
loc_00600779:
    local_r13 = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(*(uint64_t *)(arg4))) >= ((uint32_t)(local_r10))) { local_r13 = (uint32_t)(*(uint64_t *)(arg4)); }
loc_0060078D:
    if (1 > 15) goto loc_006007AB;
    Arg2 = (uint32_t)((1) + (1));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(*(uint16_t *)(v_stack_m4F + 0x1 * 2 - 0x31))));
    if (sign_flag) goto loc_006007B8;
    Arg4 = (uint32_t)((1) + (1));
    goto loc_0060078D;
loc_006007AB:
    if ((uint32_t)(Arg2) == 0) goto loc_006007C0;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_006007B8;
    if (Arg3 == 1) goto loc_006007C0;
loc_006007B8:
    result = (uint32_t)((1) | (0xFFFFFFFFULL));
    goto loc_006008C2;
loc_006007C0:
    v_stack_m5E = 0;
loc_006007D1:
    Arg1 = (uint16_t)((*(uint16_t *)(v_stack_m4F + 0x0 * 1 - 0x2F)) + (*(uint16_t *)(v_stack_m4F + 0x0 * 1 - 0xF)));
    *(uint16_t *)(v_stack_m4F + 0x0 * 1 - 0xD) = (uint16_t)(Arg1);
    Arg2 = (0) + (local_rdi);
    Arg4 = (1 + 13) - (1);
    if (condition_is_not_equal) goto loc_006007D1;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00600824;
loc_006007FB:
    result = *(uint16_t *)(arg2);
    if ((uint16_t)(*(uint16_t *)(arg2)) != 0) {
        Arg1 = *(uint16_t *)(v_stack_m4F + *(uint16_t *)(arg2) * 2 - 0x11);
        *(uint16_t *)(arg6 + Arg1 * 2) = 0;
        result = *(uint16_t *)(arg2);
    }
    Arg4 = (uint32_t)((0) + (1));
    Arg2 = (Arg2) + (local_rdi);
    if (((uint32_t)(Arg4)) < ((uint32_t)((uint32_t)(Arg3)))) goto loc_006007FB;
loc_00600824:
    if ((uint32_t)((uint32_t)(v_stack_mCC)) == 0) goto loc_0060085E;
    if (((uint32_t)((uint32_t)(v_stack_mCC))) == 1) goto loc_00600844;
    v_stack_mA8 = v_rip - 6071124;
    goto loc_00600868;
loc_00600844:
    v_stack_mA8 = v_rip - 6071211;
    goto loc_00600868;
loc_0060085E:
    v_stack_mA8 = v_rip - 6071292;
loc_00600868:
    v_stack_mC0 = *(uint64_t *)(v_stack_mA0);
    result = 0;
    v_stack_mB0 = v_rip - 6071292;
    v_stack_mD4 = 0;
    v_stack_mD0 = 0;
    local_r11 = (uint32_t)((result + 1) << ((uint8_t)((uint32_t)((uint32_t)(local_r13)))));
    v_stack_mB8 = (uint32_t)(local_r11 - 1);
    if (((uint32_t)((uint32_t)(v_stack_mCC))) != 1) goto loc_006008A8;
    if (((uint32_t)(local_r11)) > 0x534ULL) goto loc_006008BD;
loc_006008A8:
    if (((uint32_t)((uint32_t)(v_stack_mCC))) != ((uint32_t)(local_rdi))) goto loc_00600AB6;
    if (((uint32_t)(local_r11)) <= 592) goto loc_00600AB6;
loc_006008BD:
loc_006008C2:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 0, Arg3, 0);
    local_rsp = (local_rsp) + (192);
    return result;
loc_006008EA:
loc_006008EF:
    result = (uint8_t)(((uint8_t)(local_r10)) - (0));
    v_stack_p21 = (uint8_t)(result);
    if (((uint32_t)(*(uint16_t *)(v_stack_m98 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p28))) * 2) + 1)) >= 20) goto loc_00600916;
    v_stack_p20 = (uint8_t)(v_stack_p8);
    v_stack_p22 = (uint16_t)(*(uint16_t *)(v_stack_m98 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p28))) * 2));
    goto loc_00600942;
loc_00600916:
    if (((uint32_t)(*(uint16_t *)(v_stack_m98 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p28))) * 2))) < 20) goto loc_00600938;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_m98 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p28))) * 2)) - (20));
    v_stack_p20 = (uint8_t)(*(uint8_t *)(v_stack_mB0 + Arg1 * 2));
    v_stack_p22 = (uint16_t)(*(uint16_t *)(v_stack_mA8 + Arg1 * 2));
    goto loc_00600942;
loc_00600938:
    v_stack_p20 = 96;
    v_stack_p22 = (uint16_t)(v_stack_p8);
loc_00600942:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - (0));
    local_r14 = (uint32_t)((1) << ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13)))))));
    local_rbx = (uint32_t)((0) >> ((uint8_t)((uint32_t)(v_stack_p24))));
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(Arg2)));
    v_stack_mB4 = (uint32_t)(Arg2);
loc_0060096F:
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_r14)));
    *(uint32_t *)(v_stack_mC0 + local_rbx * 4) = (uint32_t)((uint32_t)(v_stack_p20));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_0060096F;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) << ((uint8_t)(local_r10 - 1)));
    goto loc_0060098D;
loc_0060098B:
    Arg2 = (uint32_t)((Arg2) >> (1));
loc_0060098D:
    if (((0) & ((uint32_t)(Arg2))) != 0) goto loc_0060098B;
    local_rbx = 0;
    if ((uint32_t)(Arg2) == 0) goto loc_006009A6;
    Arg4 = (uint32_t)((0) & ((uint32_t)(Arg2 - 1)));
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(Arg2)));
    goto loc_006009A9;
loc_006009A6:
loc_006009A9:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_p28)) + ((uint32_t)(local_rbx + 1)));
    v_stack_p28 = (uint32_t)(local_r14);
    if (condition_is_not_equal) goto loc_006009E0;
    if (((uint32_t)(local_r10)) == Arg3) goto loc_00600ABD;
loc_006009E0:
    if (((uint32_t)(*(uint16_t *)(v_stack_m90 + *(uint16_t *)(v_stack_m98 + local_r14 * 2) * 2))) <= ((uint32_t)(local_r13))) goto loc_006008EF;
    local_r14 = (uint32_t)(((uint32_t)(v_stack_mB8)) & (0));
    if (((uint32_t)(local_r14)) == v_stack_mC8) goto loc_006008EA;
    Arg2 = (uint32_t)(v_stack_p24);
    if ((uint32_t)((uint32_t)(v_stack_p24)) == 0) { Arg2 = (uint32_t)(local_r13); }
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m90 + *(uint16_t *)(v_stack_m98 + local_r14 * 2) * 2)))) - ((uint32_t)(Arg2)));
    v_stack_p24 = (uint32_t)(Arg2);
    v_stack_mC0 = v_stack_mC0 + (uint32_t)(v_stack_mB4) * 4;
    Arg2 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_r12)))));
    if (((uint32_t)(*(uint16_t *)(v_stack_m90 + *(uint16_t *)(v_stack_m98 + local_r14 * 2) * 2))) >= Arg3) goto loc_00600A58;
loc_00600A33:
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(*(uint16_t *)(v_stack_m4F + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m90 + *(uint16_t *)(v_stack_m98 + local_r14 * 2) * 2))))) * 2 - 0x31))));
    if (condition_is_less_or_equal) goto loc_00600A4C;
    local_r12 = (uint32_t)((local_r12) + (1));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m90 + *(uint16_t *)(v_stack_m98 + local_r14 * 2) * 2)))) + (1));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg2)));
    if (((uint32_t)(local_rbx)) < Arg3) goto loc_00600A33;
loc_00600A4C:
loc_00600A58:
    result = (uint32_t)((2 - 1) << ((uint8_t)((uint32_t)((uint32_t)(local_r12)))));
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(result)));
    if (((uint32_t)((uint32_t)(v_stack_mCC))) != 1) goto loc_00600A75;
    if (((uint32_t)(local_r11)) > 0x534ULL) goto loc_006008BD;
loc_00600A75:
    if (((uint32_t)((uint32_t)(v_stack_mCC))) != 2) goto loc_00600A86;
    if (((uint32_t)(local_r11)) > 592) goto loc_006008BD;
loc_00600A86:
    v_stack_mC8 = (uint32_t)(local_r14);
    *(uint8_t *)(*(uint64_t *)(v_stack_mA0) + local_r14 * 4) = (uint8_t)(local_r12);
    *(uint8_t *)(*(uint64_t *)(v_stack_mA0) + local_r14 * 4 + 0x1) = (uint8_t)(local_r13);
    result = (v_stack_mC0) - (*(uint64_t *)(v_stack_mA0));
    result = (result) >> (2);
    *(uint16_t *)(*(uint64_t *)(v_stack_mA0) + local_r14 * 4 + 0x2) = (uint16_t)(result);
loc_00600AB6:
    local_rbx = 0;
    goto loc_006008EF;
loc_00600ABD:
    if (0 != 0) {
        Arg2 = v_stack_mC0;
        Arg1 = 0;
        v_stack_p20 = 64;
        v_stack_p22 = 0;
        result = v_stack_p20;
        *(uint32_t *)(arg2 + Arg1 * 4) = (uint32_t)(result);
    }
    result = ((uint32_t)((uint32_t)(local_r11))) << (2);
    *(uint32_t *)(v_stack_m88) = (uint32_t)(local_r13);
    goto loc_00600755;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R/W` |
| `Arg6` | `+ 0x0 + rcx*2` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00600664&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
