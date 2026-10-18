# LZ4HC_compress_generic

- RVA: `0x005F564C`–`0x005F7D8E` (길이 `10,050` bytes)
- VA: `0x00000001405F564C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000D04A8`
- 디코드: `2,789`개 명령, `10,050/10,050` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005F59DD` → [LZ4HC_countPattern](LZ4HC_countPattern_function_005FF974.md) (function, `0x005FF974`)
- `0x005F5CA8` → [LZ4HC_countPattern](LZ4HC_countPattern_function_005FF974.md) (function, `0x005FF974`)
- `0x005F5CDE` → [LZ4HC_countPattern](LZ4HC_countPattern_function_005FF974.md) (function, `0x005FF974`)
- `0x005F5CF8` → [LZ4HC_reverseCountPattern](LZ4HC_reverseCountPattern_function_005FFA60.md) (function, `0x005FFA60`)
- `0x005F5D30` → [LZ4HC_reverseCountPattern](LZ4HC_reverseCountPattern_function_005FFA60.md) (function, `0x005FFA60`)
- `0x005F648E` → [LZ4HC_countPattern](LZ4HC_countPattern_function_005FF974.md) (function, `0x005FF974`)
- `0x005F658B` → [LZ4HC_countPattern](LZ4HC_countPattern_function_005FF974.md) (function, `0x005FF974`)
- `0x005F65C3` → [LZ4HC_countPattern](LZ4HC_countPattern_function_005FF974.md) (function, `0x005FF974`)
- `0x005F65E2` → [LZ4HC_reverseCountPattern](LZ4HC_reverseCountPattern_function_005FFA60.md) (function, `0x005FFA60`)
- `0x005F6622` → [LZ4HC_reverseCountPattern](LZ4HC_reverseCountPattern_function_005FFA60.md) (function, `0x005FFA60`)
- `0x005F6E31` → [LZ4HC_countPattern](LZ4HC_countPattern_function_005FF974.md) (function, `0x005FF974`)
- `0x005F6F35` → [LZ4HC_countPattern](LZ4HC_countPattern_function_005FF974.md) (function, `0x005FF974`)
- `0x005F6F6C` → [LZ4HC_countPattern](LZ4HC_countPattern_function_005FF974.md) (function, `0x005FF974`)
- `0x005F6F87` → [LZ4HC_reverseCountPattern](LZ4HC_reverseCountPattern_function_005FFA60.md) (function, `0x005FFA60`)
- `0x005F6FC8` → [LZ4HC_reverseCountPattern](LZ4HC_reverseCountPattern_function_005FFA60.md) (function, `0x005FFA60`)
- `0x005F71F6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005F7405` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005F75D6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005F776A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005F7905` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005F7B3D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005F7CEC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005F7D26` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005F7D74` → [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) (function, `0x005F7D94`)

### Direct callers
- [LZ4_compress_HC_extStateHC_fastReset](LZ4_compress_HC_extStateHC_fastReset_function_005FFBB0.md) at `0x005FFC18`

### Static image references
- `0x005F56D4` → RVA `0x000363EC` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F564C  48 8B C4                        mov rax, rsp
005F564F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
005F5653  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
005F5657  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
005F565B  48 89 48 08                     mov qword ptr [rax + 8], rcx
005F565F  55                              push rbp
005F5660  53                              push rbx
005F5661  56                              push rsi
005F5662  57                              push rdi
005F5663  41 54                           push r12
005F5665  41 55                           push r13
005F5667  41 56                           push r14
005F5669  41 57                           push r15
005F566B  48 8D 6C 24 A8                  lea rbp, [rsp - 0x58]
005F5670  48 81 EC 58 01 00 00            sub rsp, 0x158
005F5677  45 33 D2                        xor r10d, r10d
005F567A  4D 8B F9                        mov r15, r9
005F567D  4D 8B E8                        mov r13, r8
005F5680  4C 8B E2                        mov r12, rdx
005F5683  4C 8B C9                        mov r9, rcx
005F5686  4C 39 91 28 00 04 00            cmp qword ptr [rcx + 0x40028], r10
005F568D  0F 85 C3 26 00 00               jne 0x1405f7d56
005F5693  83 BD D0 00 00 00 02            cmp dword ptr [rbp + 0xd0], 2
005F569A  41 8D 42 01                     lea eax, [r10 + 1]
005F569E  75 0C                           jne 0x1405f56ac
005F56A0  39 85 C0 00 00 00               cmp dword ptr [rbp + 0xc0], eax
005F56A6  0F 8C A5 26 00 00               jl 0x1405f7d51
005F56AC  49 63 07                        movsxd rax, dword ptr [r15]
005F56AF  3D 00 00 00 7E                  cmp eax, 0x7e000000
005F56B4  0F 87 97 26 00 00               ja 0x1405f7d51
005F56BA  48 01 81 00 00 04 00            add qword ptr [rcx + 0x40000], rax
005F56C1  49 8B FC                        mov rdi, r12
005F56C4  49 63 17                        movsxd rdx, dword ptr [r15]
005F56C7  4D 8B DC                        mov r11, r12
005F56CA  48 63 8D C0 00 00 00            movsxd rcx, dword ptr [rbp + 0xc0]
005F56D1  4D 8B F5                        mov r14, r13
005F56D4  48 8B 05 11 0D A4 FF            mov rax, qword ptr [rip - 0x5bf2ef]
005F56DB  49 03 CD                        add rcx, r13
005F56DE  F2 0F 10 05 06 0D A4 FF         movsd xmm0, qword ptr [rip - 0x5bf2fa]
005F56E6  48 C1 E8 20                     shr rax, 0x20
005F56EA  49 8D 1C 14                     lea rbx, [r12 + rdx]
005F56EE  83 BD D0 00 00 00 02            cmp dword ptr [rbp + 0xd0], 2
005F56F5  4C 8D 43 F4                     lea r8, [rbx - 0xc]
005F56F9  48 8D 71 FB                     lea rsi, [rcx - 5]
005F56FD  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
005F5701  48 0F 45 F1                     cmovne rsi, rcx
005F5705  F2 0F 11 45 20                  movsd qword ptr [rbp + 0x20], xmm0
005F570A  48 89 75 A8                     mov qword ptr [rbp - 0x58], rsi
005F570E  48 8D 43 FB                     lea rax, [rbx - 5]
005F5712  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
005F5717  4C 89 65 98                     mov qword ptr [rbp - 0x68], r12
005F571B  48 89 5D 00                     mov qword ptr [rbp], rbx
005F571F  4C 89 45 F0                     mov qword ptr [rbp - 0x10], r8
005F5723  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
005F5728  4C 89 6D C8                     mov qword ptr [rbp - 0x38], r13
005F572C  4C 89 55 80                     mov qword ptr [rbp - 0x80], r10
005F5730  4C 89 55 E0                     mov qword ptr [rbp - 0x20], r10
005F5734  45 89 17                        mov dword ptr [r15], r10d
005F5737  83 FA 0D                        cmp edx, 0xd
005F573A  0F 8C EE 24 00 00               jl 0x1405f7c2e
005F5740  49 3B F8                        cmp rdi, r8
005F5743  0F 87 CC 24 00 00               ja 0x1405f7c15
005F5749  41 8B 91 1C 00 04 00            mov edx, dword ptr [r9 + 0x4001c]
005F5750  44 8B FF                        mov r15d, edi
005F5753  49 8B 89 08 00 04 00            mov rcx, qword ptr [r9 + 0x40008]
005F575A  BE 03 00 00 00                  mov esi, 3
005F575F  45 8B A9 18 00 04 00            mov r13d, dword ptr [r9 + 0x40018]
005F5766  44 2B F9                        sub r15d, ecx
005F5769  45 03 FD                        add r15d, r13d
005F576C  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
005F5770  8D 82 00 00 01 00               lea eax, [rdx + 0x10000]
005F5776  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
005F577A  44 89 7C 24 78                  mov dword ptr [rsp + 0x78], r15d
005F577F  8B DA                           mov ebx, edx
005F5781  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
005F5785  41 3B C7                        cmp eax, r15d
005F5788  77 07                           ja 0x1405f5791
005F578A  41 8D 9F 01 00 FF FF            lea ebx, [r15 - 0xffff]
005F5791  4D 8B 81 10 00 04 00            mov r8, qword ptr [r9 + 0x40010]
005F5798  4D 8B CD                        mov r9, r13
005F579B  8B 45 24                        mov eax, dword ptr [rbp + 0x24]
005F579E  4C 2B CA                        sub r9, rdx
005F57A1  44 8B 27                        mov r12d, dword ptr [rdi]
005F57A4  4D 03 C8                        add r9, r8
005F57A7  89 45 90                        mov dword ptr [rbp - 0x70], eax
005F57AA  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
005F57B1  4C 89 4D D8                     mov qword ptr [rbp - 0x28], r9
005F57B5  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
005F57B9  45 8B C2                        mov r8d, r10d
005F57BC  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
005F57C0  44 8B 88 20 00 04 00            mov r9d, dword ptr [rax + 0x40020]
005F57C7  44 89 95 C8 00 00 00            mov dword ptr [rbp + 0xc8], r10d
005F57CE  4C 89 55 A0                     mov qword ptr [rbp - 0x60], r10
005F57D2  44 89 55 88                     mov dword ptr [rbp - 0x78], r10d
005F57D6  45 3B CF                        cmp r9d, r15d
005F57D9  73 5A                           jae 0x1405f5835
005F57DB  45 8B C1                        mov r8d, r9d
005F57DE  4C 8B D8                        mov r11, rax
005F57E1  4D 2B C5                        sub r8, r13
005F57E4  BE 01 00 00 00                  mov esi, 1
005F57E9  4C 03 C1                        add r8, rcx
005F57EC  BB FF FF 00 00                  mov ebx, 0xffff
005F57F1  41 69 10 B1 79 37 9E            imul edx, dword ptr [r8], 0x9e3779b1
005F57F8  41 8B C9                        mov ecx, r9d
005F57FB  41 0F B7 C1                     movzx eax, r9w
005F57FF  48 C1 EA 11                     shr rdx, 0x11
005F5803  41 2B 0C 93                     sub ecx, dword ptr [r11 + rdx*4]
005F5807  48 3B CB                        cmp rcx, rbx
005F580A  48 0F 47 CB                     cmova rcx, rbx
005F580E  4C 03 C6                        add r8, rsi
005F5811  66 41 89 8C 43 00 00 02 00      mov word ptr [r11 + rax*2 + 0x20000], cx
005F581A  45 89 0C 93                     mov dword ptr [r11 + rdx*4], r9d
005F581E  44 03 CE                        add r9d, esi
005F5821  45 3B CF                        cmp r9d, r15d
005F5824  72 CB                           jb 0x1405f57f1
005F5826  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
005F582A  45 8B C2                        mov r8d, r10d
005F582D  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
005F5831  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
005F5835  4C 8B 8D A0 00 00 00            mov r9, qword ptr [rbp + 0xa0]
005F583C  45 89 B9 20 00 04 00            mov dword ptr [r9 + 0x40020], r15d
005F5843  69 0F B1 79 37 9E               imul ecx, dword ptr [rdi], 0x9e3779b1
005F5849  48 C1 E9 11                     shr rcx, 0x11
005F584D  45 8B 1C 89                     mov r11d, dword ptr [r9 + rcx*4]
005F5851  44 3B DB                        cmp r11d, ebx
005F5854  0F 82 A7 03 00 00               jb 0x1405f5c01
005F585A  4C 8B 75 B0                     mov r14, qword ptr [rbp - 0x50]
005F585E  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
005F5861  45 33 C9                        xor r9d, r9d
005F5864  41 8B F8                        mov edi, r8d
005F5867  85 C0                           test eax, eax
005F5869  0F 8E 7E 03 00 00               jle 0x1405f5bed
005F586F  FF C8                           dec eax
005F5871  89 45 90                        mov dword ptr [rbp - 0x70], eax
005F5874  45 3B DD                        cmp r11d, r13d
005F5877  0F 82 77 01 00 00               jb 0x1405f59f4
005F587D  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
005F5882  41 8B D3                        mov edx, r11d
005F5885  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
005F588A  41 2B D5                        sub edx, r13d
005F588D  49 03 D6                        add rdx, r14
005F5890  48 63 CE                        movsxd rcx, esi
005F5893  0F B7 44 11 FF                  movzx eax, word ptr [rcx + rdx - 1]
005F5898  66 42 39 44 11 FF               cmp word ptr [rcx + r10 - 1], ax
005F589E  0F 85 C0 00 00 00               jne 0x1405f5964
005F58A4  44 39 22                        cmp dword ptr [rdx], r12d
005F58A7  0F 85 B7 00 00 00               jne 0x1405f5964
005F58AD  49 83 C2 04                     add r10, 4
005F58B1  4C 8D 4B F9                     lea r9, [rbx - 7]
005F58B5  48 83 C2 04                     add rdx, 4
005F58B9  49 8B CA                        mov rcx, r10
005F58BC  4D 3B D1                        cmp r10, r9
005F58BF  73 18                           jae 0x1405f58d9
005F58C1  4D 8B 02                        mov r8, qword ptr [r10]
005F58C4  4C 33 02                        xor r8, qword ptr [rdx]
005F58C7  75 06                           jne 0x1405f58cf
005F58C9  49 8D 4A 08                     lea rcx, [r10 + 8]
005F58CD  EB 1B                           jmp 0x1405f58ea
005F58CF  F3 49 0F BC C8                  tzcnt rcx, r8
005F58D4  C1 E9 03                        shr ecx, 3
005F58D7  EB 67                           jmp 0x1405f5940
005F58D9  49 3B C9                        cmp rcx, r9
005F58DC  73 21                           jae 0x1405f58ff
005F58DE  4C 8B 01                        mov r8, qword ptr [rcx]
005F58E1  4C 33 02                        xor r8, qword ptr [rdx]
005F58E4  75 0A                           jne 0x1405f58f0
005F58E6  48 83 C1 08                     add rcx, 8
005F58EA  48 83 C2 08                     add rdx, 8
005F58EE  EB E9                           jmp 0x1405f58d9
005F58F0  F3 49 0F BC C0                  tzcnt rax, r8
005F58F5  C1 E8 03                        shr eax, 3
005F58F8  41 2B C2                        sub eax, r10d
005F58FB  03 C8                           add ecx, eax
005F58FD  EB 41                           jmp 0x1405f5940
005F58FF  48 8D 43 FD                     lea rax, [rbx - 3]
005F5903  48 3B C8                        cmp rcx, rax
005F5906  73 0E                           jae 0x1405f5916
005F5908  8B 01                           mov eax, dword ptr [rcx]
005F590A  39 02                           cmp dword ptr [rdx], eax
005F590C  75 08                           jne 0x1405f5916
005F590E  48 83 C1 04                     add rcx, 4
005F5912  48 83 C2 04                     add rdx, 4
005F5916  48 8D 43 FF                     lea rax, [rbx - 1]
005F591A  48 3B C8                        cmp rcx, rax
005F591D  73 10                           jae 0x1405f592f
005F591F  0F B7 01                        movzx eax, word ptr [rcx]
005F5922  66 39 02                        cmp word ptr [rdx], ax
005F5925  75 08                           jne 0x1405f592f
005F5927  48 83 C1 02                     add rcx, 2
005F592B  48 83 C2 02                     add rdx, 2
005F592F  48 3B CB                        cmp rcx, rbx
005F5932  73 09                           jae 0x1405f593d
005F5934  8A 01                           mov al, byte ptr [rcx]
005F5936  38 02                           cmp byte ptr [rdx], al
005F5938  75 03                           jne 0x1405f593d
005F593A  48 FF C1                        inc rcx
005F593D  41 2B CA                        sub ecx, r10d
005F5940  44 8B 85 C8 00 00 00            mov r8d, dword ptr [rbp + 0xc8]
005F5947  83 C1 04                        add ecx, 4
005F594A  3B CE                           cmp ecx, esi
005F594C  7E 0E                           jle 0x1405f595c
005F594E  45 8B D7                        mov r10d, r15d
005F5951  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
005F5955  45 2B D3                        sub r10d, r11d
005F5958  44 89 55 88                     mov dword ptr [rbp - 0x78], r10d
005F595C  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
005F5961  45 33 C9                        xor r9d, r9d
005F5964  81 7D 18 80 00 00 00            cmp dword ptr [rbp + 0x18], 0x80
005F596B  0F 8E 44 02 00 00               jle 0x1405f5bb5
005F5971  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
005F5978  41 BF 01 00 00 00               mov r15d, 1
005F597E  41 0F B7 C3                     movzx eax, r11w
005F5982  66 44 39 BC 41 00 00 02 00      cmp word ptr [rcx + rax*2 + 0x20000], r15w
005F598B  0F 85 24 02 00 00               jne 0x1405f5bb5
005F5991  41 8D 73 FF                     lea esi, [r11 - 1]
005F5995  45 85 C0                        test r8d, r8d
005F5998  0F 85 A2 02 00 00               jne 0x1405f5c40
005F599E  45 8B C1                        mov r8d, r9d
005F59A1  41 8B C9                        mov ecx, r9d
005F59A4  41 8B C4                        mov eax, r12d
005F59A7  41 8B D4                        mov edx, r12d
005F59AA  C1 E8 18                        shr eax, 0x18
005F59AD  44 3A E0                        cmp r12b, al
005F59B0  41 0F B7 C4                     movzx eax, r12w
005F59B4  41 0F 94 C0                     sete r8b
005F59B8  C1 EA 10                        shr edx, 0x10
005F59BB  3B C2                           cmp eax, edx
005F59BD  0F 94 C1                        sete cl
005F59C0  44 85 C1                        test ecx, r8d
005F59C3  0F 84 E5 01 00 00               je 0x1405f5bae
005F59C9  49 8D 4A 04                     lea rcx, [r10 + 4]
005F59CD  C7 85 C8 00 00 00 02 00 00 00   mov dword ptr [rbp + 0xc8], 2
005F59D7  45 8B C4                        mov r8d, r12d
005F59DA  48 8B D3                        mov rdx, rbx
005F59DD  E8 92 9F 00 00                  call 0x1405ff974
005F59E2  8B D8                           mov ebx, eax
005F59E4  48 83 C3 04                     add rbx, 4
005F59E8  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
005F59EC  45 33 C9                        xor r9d, r9d
005F59EF  E9 5B 02 00 00                  jmp 0x1405f5c4f
005F59F4  41 8B C3                        mov eax, r11d
005F59F7  2B C2                           sub eax, edx
005F59F9  8B D0                           mov edx, eax
005F59FB  41 8D 45 FC                     lea eax, [r13 - 4]
005F59FF  48 03 55 B8                     add rdx, qword ptr [rbp - 0x48]
005F5A03  44 3B D8                        cmp r11d, eax
005F5A06  0F 87 9B 01 00 00               ja 0x1405f5ba7
005F5A0C  44 39 22                        cmp dword ptr [rdx], r12d
005F5A0F  0F 85 92 01 00 00               jne 0x1405f5ba7
005F5A15  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
005F5A1A  45 8B C5                        mov r8d, r13d
005F5A1D  45 2B C3                        sub r8d, r11d
005F5A20  4C 03 C0                        add r8, rax
005F5A23  4C 3B 44 24 60                  cmp r8, qword ptr [rsp + 0x60]
005F5A28  48 8D 58 04                     lea rbx, [rax + 4]
005F5A2C  4C 0F 47 44 24 60               cmova r8, qword ptr [rsp + 0x60]
005F5A32  48 8B CB                        mov rcx, rbx
005F5A35  48 83 C2 04                     add rdx, 4
005F5A39  4D 8D 50 F9                     lea r10, [r8 - 7]
005F5A3D  49 3B DA                        cmp rbx, r10
005F5A40  73 18                           jae 0x1405f5a5a
005F5A42  4C 8B 0B                        mov r9, qword ptr [rbx]
005F5A45  4C 33 0A                        xor r9, qword ptr [rdx]
005F5A48  75 06                           jne 0x1405f5a50
005F5A4A  48 8D 4B 08                     lea rcx, [rbx + 8]
005F5A4E  EB 1B                           jmp 0x1405f5a6b
005F5A50  F3 49 0F BC C9                  tzcnt rcx, r9
005F5A55  C1 E9 03                        shr ecx, 3
005F5A58  EB 65                           jmp 0x1405f5abf
005F5A5A  49 3B CA                        cmp rcx, r10
005F5A5D  73 20                           jae 0x1405f5a7f
005F5A5F  4C 8B 09                        mov r9, qword ptr [rcx]
005F5A62  4C 33 0A                        xor r9, qword ptr [rdx]
005F5A65  75 0A                           jne 0x1405f5a71
005F5A67  48 83 C1 08                     add rcx, 8
005F5A6B  48 83 C2 08                     add rdx, 8
005F5A6F  EB E9                           jmp 0x1405f5a5a
005F5A71  F3 49 0F BC C1                  tzcnt rax, r9
005F5A76  C1 E8 03                        shr eax, 3
005F5A79  2B C3                           sub eax, ebx
005F5A7B  03 C8                           add ecx, eax
005F5A7D  EB 40                           jmp 0x1405f5abf
005F5A7F  49 8D 40 FD                     lea rax, [r8 - 3]
005F5A83  48 3B C8                        cmp rcx, rax
005F5A86  73 0E                           jae 0x1405f5a96
005F5A88  8B 01                           mov eax, dword ptr [rcx]
005F5A8A  39 02                           cmp dword ptr [rdx], eax
005F5A8C  75 08                           jne 0x1405f5a96
005F5A8E  48 83 C1 04                     add rcx, 4
005F5A92  48 83 C2 04                     add rdx, 4
005F5A96  49 8D 40 FF                     lea rax, [r8 - 1]
005F5A9A  48 3B C8                        cmp rcx, rax
005F5A9D  73 10                           jae 0x1405f5aaf
005F5A9F  0F B7 01                        movzx eax, word ptr [rcx]
005F5AA2  66 39 02                        cmp word ptr [rdx], ax
005F5AA5  75 08                           jne 0x1405f5aaf
005F5AA7  48 83 C1 02                     add rcx, 2
005F5AAB  48 83 C2 02                     add rdx, 2
005F5AAF  49 3B C8                        cmp rcx, r8
005F5AB2  73 09                           jae 0x1405f5abd
005F5AB4  8A 01                           mov al, byte ptr [rcx]
005F5AB6  38 02                           cmp byte ptr [rdx], al
005F5AB8  75 03                           jne 0x1405f5abd
005F5ABA  48 FF C1                        inc rcx
005F5ABD  2B CB                           sub ecx, ebx
005F5ABF  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
005F5AC4  8D 59 04                        lea ebx, [rcx + 4]
005F5AC7  4C 63 CB                        movsxd r9, ebx
005F5ACA  4D 03 CA                        add r9, r10
005F5ACD  4D 3B C8                        cmp r9, r8
005F5AD0  0F 85 AC 00 00 00               jne 0x1405f5b82
005F5AD6  4C 3B 44 24 60                  cmp r8, qword ptr [rsp + 0x60]
005F5ADB  0F 83 A1 00 00 00               jae 0x1405f5b82
005F5AE1  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
005F5AE6  49 8B D6                        mov rdx, r14
005F5AE9  49 83 C2 F9                     add r10, -7
005F5AED  49 8B C9                        mov rcx, r9
005F5AF0  4D 3B CA                        cmp r9, r10
005F5AF3  73 10                           jae 0x1405f5b05
005F5AF5  49 8B 11                        mov rdx, qword ptr [r9]
005F5AF8  49 33 16                        xor rdx, qword ptr [r14]
005F5AFB  75 1F                           jne 0x1405f5b1c
005F5AFD  49 8D 49 08                     lea rcx, [r9 + 8]
005F5B01  49 8D 56 08                     lea rdx, [r14 + 8]
005F5B05  49 3B CA                        cmp rcx, r10
005F5B08  73 2B                           jae 0x1405f5b35
005F5B0A  4C 8B 01                        mov r8, qword ptr [rcx]
005F5B0D  4C 33 02                        xor r8, qword ptr [rdx]
005F5B10  75 14                           jne 0x1405f5b26
005F5B12  48 83 C1 08                     add rcx, 8
005F5B16  48 83 C2 08                     add rdx, 8
005F5B1A  EB E9                           jmp 0x1405f5b05
005F5B1C  F3 48 0F BC CA                  tzcnt rcx, rdx
005F5B21  C1 E9 03                        shr ecx, 3
005F5B24  EB 55                           jmp 0x1405f5b7b
005F5B26  F3 49 0F BC C0                  tzcnt rax, r8
005F5B2B  C1 E8 03                        shr eax, 3
005F5B2E  41 2B C1                        sub eax, r9d
005F5B31  03 C8                           add ecx, eax
005F5B33  EB 46                           jmp 0x1405f5b7b
005F5B35  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
005F5B3A  49 8D 40 FD                     lea rax, [r8 - 3]
005F5B3E  48 3B C8                        cmp rcx, rax
005F5B41  73 0E                           jae 0x1405f5b51
005F5B43  8B 01                           mov eax, dword ptr [rcx]
005F5B45  39 02                           cmp dword ptr [rdx], eax
005F5B47  75 08                           jne 0x1405f5b51
005F5B49  48 83 C1 04                     add rcx, 4
005F5B4D  48 83 C2 04                     add rdx, 4
005F5B51  49 8D 40 FF                     lea rax, [r8 - 1]
005F5B55  48 3B C8                        cmp rcx, rax
005F5B58  73 10                           jae 0x1405f5b6a
005F5B5A  0F B7 01                        movzx eax, word ptr [rcx]
005F5B5D  66 39 02                        cmp word ptr [rdx], ax
005F5B60  75 08                           jne 0x1405f5b6a
005F5B62  48 83 C1 02                     add rcx, 2
005F5B66  48 83 C2 02                     add rdx, 2
005F5B6A  49 3B C8                        cmp rcx, r8
005F5B6D  73 09                           jae 0x1405f5b78
005F5B6F  8A 01                           mov al, byte ptr [rcx]
005F5B71  38 02                           cmp byte ptr [rdx], al
005F5B73  75 03                           jne 0x1405f5b78
005F5B75  48 FF C1                        inc rcx
005F5B78  41 2B C9                        sub ecx, r9d
005F5B7B  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
005F5B80  03 D9                           add ebx, ecx
005F5B82  44 8B 85 C8 00 00 00            mov r8d, dword ptr [rbp + 0xc8]
005F5B89  3B DE                           cmp ebx, esi
005F5B8B  7E 0D                           jle 0x1405f5b9a
005F5B8D  41 8B C7                        mov eax, r15d
005F5B90  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
005F5B94  41 2B C3                        sub eax, r11d
005F5B97  89 45 88                        mov dword ptr [rbp - 0x78], eax
005F5B9A  45 33 C9                        xor r9d, r9d
005F5B9D  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
005F5BA2  E9 BD FD FF FF                  jmp 0x1405f5964
005F5BA7  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
005F5BAC  EB EF                           jmp 0x1405f5b9d
005F5BAE  44 89 BD C8 00 00 00            mov dword ptr [rbp + 0xc8], r15d
005F5BB5  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
005F5BBA  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
005F5BC1  41 0F B7 CB                     movzx ecx, r11w
005F5BC5  0F B7 84 48 00 00 02 00         movzx eax, word ptr [rax + rcx*2 + 0x20000]
005F5BCD  44 2B D8                        sub r11d, eax
005F5BD0  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
005F5BD4  45 3B D8                        cmp r11d, r8d
005F5BD7  44 8B 85 C8 00 00 00            mov r8d, dword ptr [rbp + 0xc8]
005F5BDE  44 8B 7C 24 78                  mov r15d, dword ptr [rsp + 0x78]
005F5BE3  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
005F5BE7  0F 83 71 FC FF FF               jae 0x1405f585e
005F5BED  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
005F5BF1  44 8B 55 88                     mov r10d, dword ptr [rbp - 0x78]
005F5BF5  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
005F5BFA  4C 8B 8D A0 00 00 00            mov r9, qword ptr [rbp + 0xa0]
005F5C01  89 75 34                        mov dword ptr [rbp + 0x34], esi
005F5C04  44 89 55 30                     mov dword ptr [rbp + 0x30], r10d
005F5C08  4C 8B 5D 30                     mov r11, qword ptr [rbp + 0x30]
005F5C0C  49 8B C3                        mov rax, r11
005F5C0F  4C 89 5D D8                     mov qword ptr [rbp - 0x28], r11
005F5C13  48 C1 E8 20                     shr rax, 0x20
005F5C17  4C 89 5D A0                     mov qword ptr [rbp - 0x60], r11
005F5C1B  83 F8 04                        cmp eax, 4
005F5C1E  0F 8D D7 01 00 00               jge 0x1405f5dfb
005F5C24  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F5C28  48 FF C7                        inc rdi
005F5C2B  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F5C2F  45 33 D2                        xor r10d, r10d
005F5C32  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
005F5C36  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
005F5C3B  E9 00 FB FF FF                  jmp 0x1405f5740
005F5C40  89 BD C8 00 00 00               mov dword ptr [rbp + 0xc8], edi
005F5C46  83 FF 02                        cmp edi, 2
005F5C49  0F 85 66 FF FF FF               jne 0x1405f5bb5
005F5C4F  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
005F5C54  41 3B F0                        cmp esi, r8d
005F5C57  0F 82 5D FF FF FF               jb 0x1405f5bba
005F5C5D  41 8B C5                        mov eax, r13d
005F5C60  2B C6                           sub eax, esi
005F5C62  41 2B C7                        sub eax, r15d
005F5C65  83 F8 03                        cmp eax, 3
005F5C68  0F 82 4C FF FF FF               jb 0x1405f5bba
005F5C6E  8B DE                           mov ebx, esi
005F5C70  41 3B F5                        cmp esi, r13d
005F5C73  73 0A                           jae 0x1405f5c7f
005F5C75  2B 5C 24 68                     sub ebx, dword ptr [rsp + 0x68]
005F5C79  48 03 5D B8                     add rbx, qword ptr [rbp - 0x48]
005F5C7D  EB 09                           jmp 0x1405f5c88
005F5C7F  41 2B DD                        sub ebx, r13d
005F5C82  45 8B F9                        mov r15d, r9d
005F5C85  49 03 DE                        add rbx, r14
005F5C88  44 39 23                        cmp dword ptr [rbx], r12d
005F5C8B  0F 85 29 FF FF FF               jne 0x1405f5bba
005F5C91  4C 8B 5C 24 60                  mov r11, qword ptr [rsp + 0x60]
005F5C96  48 8D 4B 04                     lea rcx, [rbx + 4]
005F5C9A  45 85 FF                        test r15d, r15d
005F5C9D  45 8B C4                        mov r8d, r12d
005F5CA0  4C 0F 45 5D D8                  cmovne r11, qword ptr [rbp - 0x28]
005F5CA5  49 8B D3                        mov rdx, r11
005F5CA8  E8 C7 9C 00 00                  call 0x1405ff974
005F5CAD  8B F8                           mov edi, eax
005F5CAF  48 83 C7 04                     add rdi, 4
005F5CB3  45 85 FF                        test r15d, r15d
005F5CB6  74 37                           je 0x1405f5cef
005F5CB8  48 8D 04 1F                     lea rax, [rdi + rbx]
005F5CBC  49 3B C3                        cmp rax, r11
005F5CBF  75 28                           jne 0x1405f5ce9
005F5CC1  48 8B CF                        mov rcx, rdi
005F5CC4  45 8B C4                        mov r8d, r12d
005F5CC7  83 E1 03                        and ecx, 3
005F5CCA  48 C1 E1 03                     shl rcx, 3
005F5CCE  48 85 C9                        test rcx, rcx
005F5CD1  74 03                           je 0x1405f5cd6
005F5CD3  41 D3 C0                        rol r8d, cl
005F5CD6  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
005F5CDB  49 8B CE                        mov rcx, r14
005F5CDE  E8 91 9C 00 00                  call 0x1405ff974
005F5CE3  44 8B D8                        mov r11d, eax
005F5CE6  49 03 FB                        add rdi, r11
005F5CE9  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
005F5CED  EB 03                           jmp 0x1405f5cf2
005F5CEF  49 8B D6                        mov rdx, r14
005F5CF2  45 8B C4                        mov r8d, r12d
005F5CF5  48 8B CB                        mov rcx, rbx
005F5CF8  E8 63 9D 00 00                  call 0x1405ffa60
005F5CFD  44 8B D8                        mov r11d, eax
005F5D00  45 85 FF                        test r15d, r15d
005F5D03  75 36                           jne 0x1405f5d3b
005F5D05  49 2B DB                        sub rbx, r11
005F5D08  49 3B DE                        cmp rbx, r14
005F5D0B  75 2E                           jne 0x1405f5d3b
005F5D0D  44 39 6C 24 68                  cmp dword ptr [rsp + 0x68], r13d
005F5D12  73 27                           jae 0x1405f5d3b
005F5D14  41 8B CB                        mov ecx, r11d
005F5D17  F7 D9                           neg ecx
005F5D19  83 E1 03                        and ecx, 3
005F5D1C  48 C1 E1 03                     shl rcx, 3
005F5D20  48 85 C9                        test rcx, rcx
005F5D23  74 03                           je 0x1405f5d28
005F5D25  41 D3 C0                        rol r8d, cl
005F5D28  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
005F5D2C  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
005F5D30  E8 2B 9D 00 00                  call 0x1405ffa60
005F5D35  44 8B C0                        mov r8d, eax
005F5D38  4D 03 D8                        add r11, r8
005F5D3B  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
005F5D40  8B CE                           mov ecx, esi
005F5D42  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
005F5D46  8B C6                           mov eax, esi
005F5D48  41 2B C3                        sub eax, r11d
005F5D4B  45 8B D8                        mov r11d, r8d
005F5D4E  41 3B C0                        cmp eax, r8d
005F5D51  44 0F 47 D8                     cmova r11d, eax
005F5D55  41 2B CB                        sub ecx, r11d
005F5D58  48 03 CF                        add rcx, rdi
005F5D5B  48 3B CB                        cmp rcx, rbx
005F5D5E  72 1F                           jb 0x1405f5d7f
005F5D60  48 3B FB                        cmp rdi, rbx
005F5D63  77 1A                           ja 0x1405f5d7f
005F5D65  2B FB                           sub edi, ebx
005F5D67  41 8B C5                        mov eax, r13d
005F5D6A  03 FE                           add edi, esi
005F5D6C  45 8B DD                        mov r11d, r13d
005F5D6F  2B C7                           sub eax, edi
005F5D71  FF C8                           dec eax
005F5D73  83 F8 03                        cmp eax, 3
005F5D76  44 0F 43 DF                     cmovae r11d, edi
005F5D7A  E9 51 FE FF FF                  jmp 0x1405f5bd0
005F5D7F  41 8B C5                        mov eax, r13d
005F5D82  41 2B C3                        sub eax, r11d
005F5D85  FF C8                           dec eax
005F5D87  83 F8 03                        cmp eax, 3
005F5D8A  72 67                           jb 0x1405f5df3
005F5D8C  48 63 74 24 48                  movsxd rsi, dword ptr [rsp + 0x48]
005F5D91  48 3B CB                        cmp rcx, rbx
005F5D94  48 8B D3                        mov rdx, rbx
005F5D97  48 0F 42 D1                     cmovb rdx, rcx
005F5D9B  48 3B F2                        cmp rsi, rdx
005F5D9E  73 2F                           jae 0x1405f5dcf
005F5DA0  41 8B C3                        mov eax, r11d
005F5DA3  49 8B CD                        mov rcx, r13
005F5DA6  48 2B C8                        sub rcx, rax
005F5DA9  B8 FF FF 00 00                  mov eax, 0xffff
005F5DAE  49 2B CE                        sub rcx, r14
005F5DB1  48 03 4C 24 58                  add rcx, qword ptr [rsp + 0x58]
005F5DB6  48 3B C8                        cmp rcx, rax
005F5DB9  0F 87 2E FE FF FF               ja 0x1405f5bed
005F5DBF  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
005F5DC3  8B F2                           mov esi, edx
005F5DC5  41 2B C3                        sub eax, r11d
005F5DC8  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
005F5DCC  89 45 88                        mov dword ptr [rbp - 0x78], eax
005F5DCF  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
005F5DD6  41 0F B7 C3                     movzx eax, r11w
005F5DDA  0F B7 8C 41 00 00 02 00         movzx ecx, word ptr [rcx + rax*2 + 0x20000]
005F5DE2  41 3B CB                        cmp ecx, r11d
005F5DE5  0F 87 02 FE FF FF               ja 0x1405f5bed
005F5DEB  44 2B D9                        sub r11d, ecx
005F5DEE  E9 DD FD FF FF                  jmp 0x1405f5bd0
005F5DF3  45 8B DD                        mov r11d, r13d
005F5DF6  E9 D5 FD FF FF                  jmp 0x1405f5bd0
005F5DFB  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
005F5E00  49 8B CD                        mov rcx, r13
005F5E03  4C 89 5D E8                     mov qword ptr [rbp - 0x18], r11
005F5E07  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
005F5E0B  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
005F5E0F  4C 63 4D A4                     movsxd r9, dword ptr [rbp - 0x5c]
005F5E13  44 89 8D C8 00 00 00            mov dword ptr [rbp + 0xc8], r9d
005F5E1A  4B 8D 04 29                     lea rax, [r9 + r13]
005F5E1E  48 3B C3                        cmp rax, rbx
005F5E21  0F 87 DD 08 00 00               ja 0x1405f6704
005F5E27  48 8B 95 A0 00 00 00            mov rdx, qword ptr [rbp + 0xa0]
005F5E2E  48 83 C0 FE                     add rax, -2
005F5E32  45 8B F9                        mov r15d, r9d
005F5E35  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
005F5E3A  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
005F5E3E  48 8B D8                        mov rbx, rax
005F5E41  48 89 45 F8                     mov qword ptr [rbp - 8], rax
005F5E45  44 8B 82 18 00 04 00            mov r8d, dword ptr [rdx + 0x40018]
005F5E4C  48 8B 8A 08 00 04 00            mov rcx, qword ptr [rdx + 0x40008]
005F5E53  41 8B F8                        mov edi, r8d
005F5E56  44 8B 8A 1C 00 04 00            mov r9d, dword ptr [rdx + 0x4001c]
005F5E5D  2B F9                           sub edi, ecx
005F5E5F  03 F8                           add edi, eax
005F5E61  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
005F5E65  44 89 44 24 44                  mov dword ptr [rsp + 0x44], r8d
005F5E6A  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
005F5E6E  41 8D 81 00 00 01 00            lea eax, [r9 + 0x10000]
005F5E75  44 89 4D 90                     mov dword ptr [rbp - 0x70], r9d
005F5E79  3B C7                           cmp eax, edi
005F5E7B  76 07                           jbe 0x1405f5e84
005F5E7D  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
005F5E82  EB 0A                           jmp 0x1405f5e8e
005F5E84  8D 87 01 00 FF FF               lea eax, [rdi - 0xffff]
005F5E8A  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
005F5E8E  48 8B 92 10 00 04 00            mov rdx, qword ptr [rdx + 0x40010]
005F5E95  49 8B C1                        mov rax, r9
005F5E98  8B 33                           mov esi, dword ptr [rbx]
005F5E9A  4C 8B CA                        mov r9, rdx
005F5E9D  4C 2B C8                        sub r9, rax
005F5EA0  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
005F5EA5  8B 45 24                        mov eax, dword ptr [rbp + 0x24]
005F5EA8  4D 03 C8                        add r9, r8
005F5EAB  4C 89 4D 08                     mov qword ptr [rbp + 8], r9
005F5EAF  44 8B D3                        mov r10d, ebx
005F5EB2  44 2B 54 24 58                  sub r10d, dword ptr [rsp + 0x58]
005F5EB7  45 33 C9                        xor r9d, r9d
005F5EBA  89 45 C0                        mov dword ptr [rbp - 0x40], eax
005F5EBD  45 8B E1                        mov r12d, r9d
005F5EC0  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
005F5EC7  4D 8B E8                        mov r13, r8
005F5ECA  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
005F5ECF  4C 89 4D 10                     mov qword ptr [rbp + 0x10], r9
005F5ED3  44 89 4C 24 78                  mov dword ptr [rsp + 0x78], r9d
005F5ED8  44 8B 88 20 00 04 00            mov r9d, dword ptr [rax + 0x40020]
005F5EDF  89 74 24 4C                     mov dword ptr [rsp + 0x4c], esi
005F5EE3  44 3B CF                        cmp r9d, edi
005F5EE6  73 64                           jae 0x1405f5f4c
005F5EE8  45 8B C1                        mov r8d, r9d
005F5EEB  41 BF 01 00 00 00               mov r15d, 1
005F5EF1  4D 2B C5                        sub r8, r13
005F5EF4  41 BB FF FF 00 00               mov r11d, 0xffff
005F5EFA  4C 03 C1                        add r8, rcx
005F5EFD  4C 8B E8                        mov r13, rax
005F5F00  41 69 10 B1 79 37 9E            imul edx, dword ptr [r8], 0x9e3779b1
005F5F07  41 8B C9                        mov ecx, r9d
005F5F0A  41 0F B7 C1                     movzx eax, r9w
005F5F0E  48 C1 EA 11                     shr rdx, 0x11
005F5F12  41 2B 4C 95 00                  sub ecx, dword ptr [r13 + rdx*4]
005F5F17  49 3B CB                        cmp rcx, r11
005F5F1A  49 0F 47 CB                     cmova rcx, r11
005F5F1E  4D 03 C7                        add r8, r15
005F5F21  66 41 89 8C 45 00 00 02 00      mov word ptr [r13 + rax*2 + 0x20000], cx
005F5F2A  45 89 4C 95 00                  mov dword ptr [r13 + rdx*4], r9d
005F5F2F  45 03 CF                        add r9d, r15d
005F5F32  44 3B CF                        cmp r9d, edi
005F5F35  72 C9                           jb 0x1405f5f00
005F5F37  4C 8B 5D D8                     mov r11, qword ptr [rbp - 0x28]
005F5F3B  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
005F5F40  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
005F5F45  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
005F5F4A  EB 07                           jmp 0x1405f5f53
005F5F4C  4C 8B AD A0 00 00 00            mov r13, qword ptr [rbp + 0xa0]
005F5F53  41 89 BD 20 00 04 00            mov dword ptr [r13 + 0x40020], edi
005F5F5A  69 0B B1 79 37 9E               imul ecx, dword ptr [rbx], 0x9e3779b1
005F5F60  4D 63 CA                        movsxd r9, r10d
005F5F63  4C 89 4D B8                     mov qword ptr [rbp - 0x48], r9
005F5F67  48 C1 E9 11                     shr rcx, 0x11
005F5F6B  45 8B 6C 8D 00                  mov r13d, dword ptr [r13 + rcx*4]
005F5F70  44 3B 6C 24 50                  cmp r13d, dword ptr [rsp + 0x50]
005F5F75  0F 82 7D 05 00 00               jb 0x1405f64f8
005F5F7B  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
005F5F7F  4C 8B 5D F8                     mov r11, qword ptr [rbp - 8]
005F5F83  4C 8B 75 88                     mov r14, qword ptr [rbp - 0x78]
005F5F87  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
005F5F8B  44 8B 54 24 40                  mov r10d, dword ptr [rsp + 0x40]
005F5F90  45 33 E4                        xor r12d, r12d
005F5F93  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
005F5F96  41 8B CA                        mov ecx, r10d
005F5F99  89 4D 88                        mov dword ptr [rbp - 0x78], ecx
005F5F9C  85 C0                           test eax, eax
005F5F9E  0F 8E 47 05 00 00               jle 0x1405f64eb
005F5FA4  41 8D 5C 24 01                  lea ebx, [r12 + 1]
005F5FA9  2B C3                           sub eax, ebx
005F5FAB  89 45 C0                        mov dword ptr [rbp - 0x40], eax
005F5FAE  41 8B C5                        mov eax, r13d
005F5FB1  45 3B E8                        cmp r13d, r8d
005F5FB4  0F 82 C4 01 00 00               jb 0x1405f617e
005F5FBA  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
005F5FBF  41 2B C0                        sub eax, r8d
005F5FC2  8B F0                           mov esi, eax
005F5FC4  49 63 CF                        movsxd rcx, r15d
005F5FC7  4A 8D 3C 30                     lea rdi, [rax + r14]
005F5FCB  48 8B C7                        mov rax, rdi
005F5FCE  49 2B C1                        sub rax, r9
005F5FD1  0F B7 44 08 FF                  movzx eax, word ptr [rax + rcx - 1]
005F5FD6  66 39 44 11 FF                  cmp word ptr [rcx + rdx - 1], ax
005F5FDB  0F 85 23 04 00 00               jne 0x1405f6404
005F5FE1  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
005F5FE5  39 07                           cmp dword ptr [rdi], eax
005F5FE7  0F 85 17 04 00 00               jne 0x1405f6404
005F5FED  45 8B FC                        mov r15d, r12d
005F5FF0  4D 85 C9                        test r9, r9
005F5FF3  74 67                           je 0x1405f605c
005F5FF5  48 8B CA                        mov rcx, rdx
005F5FF8  49 8B C6                        mov rax, r14
005F5FFB  49 2B CB                        sub rcx, r11
005F5FFE  48 2B C7                        sub rax, rdi
005F6001  41 8B DC                        mov ebx, r12d
005F6004  48 3B C8                        cmp rcx, rax
005F6007  7E 07                           jle 0x1405f6010
005F6009  8B CA                           mov ecx, edx
005F600B  41 2B CB                        sub ecx, r11d
005F600E  EB 05                           jmp 0x1405f6015
005F6010  41 8B CE                        mov ecx, r14d
005F6013  2B CF                           sub ecx, edi
005F6015  8B D1                           mov edx, ecx
005F6017  4C 8D 4F FC                     lea r9, [rdi - 4]
005F601B  F7 DA                           neg edx
005F601D  4D 8B D3                        mov r10, r11
005F6020  4C 2B D7                        sub r10, rdi
005F6023  83 FA 03                        cmp edx, 3
005F6026  7E 5B                           jle 0x1405f6083
005F6028  47 8B 04 0A                     mov r8d, dword ptr [r10 + r9]
005F602C  45 33 01                        xor r8d, dword ptr [r9]
005F602F  75 11                           jne 0x1405f6042
005F6031  41 83 EF 04                     sub r15d, 4
005F6035  83 EA 04                        sub edx, 4
005F6038  48 83 EB 04                     sub rbx, 4
005F603C  49 83 E9 04                     sub r9, 4
005F6040  EB E1                           jmp 0x1405f6023
005F6042  41 0F BD C0                     bsr eax, r8d
005F6046  B9 1F 00 00 00                  mov ecx, 0x1f
005F604B  44 89 65 F8                     mov dword ptr [rbp - 8], r12d
005F604F  2B C8                           sub ecx, eax
005F6051  C1 E9 03                        shr ecx, 3
005F6054  44 2B F9                        sub r15d, ecx
005F6057  BB 01 00 00 00                  mov ebx, 1
005F605C  4D 8D 53 04                     lea r10, [r11 + 4]
005F6060  48 8D 57 04                     lea rdx, [rdi + 4]
005F6064  49 8B CA                        mov rcx, r10
005F6067  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005F606C  4C 8D 4F F9                     lea r9, [rdi - 7]
005F6070  4D 3B D1                        cmp r10, r9
005F6073  73 63                           jae 0x1405f60d8
005F6075  4D 8B 02                        mov r8, qword ptr [r10]
005F6078  4C 33 02                        xor r8, qword ptr [rdx]
005F607B  75 51                           jne 0x1405f60ce
005F607D  49 8D 4A 08                     lea rcx, [r10 + 8]
005F6081  EB 66                           jmp 0x1405f60e9
005F6083  4C 63 C1                        movsxd r8, ecx
005F6086  49 3B D8                        cmp rbx, r8
005F6089  7E CC                           jle 0x1405f6057
005F608B  4C 63 8D C8 00 00 00            movsxd r9, dword ptr [rbp + 0xc8]
005F6092  49 8D 4E FF                     lea rcx, [r14 - 1]
005F6096  48 03 CB                        add rcx, rbx
005F6099  4D 2B CE                        sub r9, r14
005F609C  4C 2B CE                        sub r9, rsi
005F609F  BB 01 00 00 00                  mov ebx, 1
005F60A4  4C 03 4C 24 58                  add r9, qword ptr [rsp + 0x58]
005F60A9  8B D3                           mov edx, ebx
005F60AB  49 2B D6                        sub rdx, r14
005F60AE  48 03 CE                        add rcx, rsi
005F60B1  48 2B D6                        sub rdx, rsi
005F60B4  8A 01                           mov al, byte ptr [rcx]
005F60B6  41 38 44 09 FE                  cmp byte ptr [r9 + rcx - 2], al
005F60BB  75 9F                           jne 0x1405f605c
005F60BD  48 2B CB                        sub rcx, rbx
005F60C0  44 2B FB                        sub r15d, ebx
005F60C3  48 8D 04 0A                     lea rax, [rdx + rcx]
005F60C7  49 3B C0                        cmp rax, r8
005F60CA  7F E8                           jg 0x1405f60b4
005F60CC  EB 8E                           jmp 0x1405f605c
005F60CE  F3 49 0F BC C8                  tzcnt rcx, r8
005F60D3  C1 E9 03                        shr ecx, 3
005F60D6  EB 67                           jmp 0x1405f613f
005F60D8  49 3B C9                        cmp rcx, r9
005F60DB  73 21                           jae 0x1405f60fe
005F60DD  4C 8B 01                        mov r8, qword ptr [rcx]
005F60E0  4C 33 02                        xor r8, qword ptr [rdx]
005F60E3  75 0A                           jne 0x1405f60ef
005F60E5  48 83 C1 08                     add rcx, 8
005F60E9  48 83 C2 08                     add rdx, 8
005F60ED  EB E9                           jmp 0x1405f60d8
005F60EF  F3 49 0F BC C0                  tzcnt rax, r8
005F60F4  C1 E8 03                        shr eax, 3
005F60F7  41 2B C2                        sub eax, r10d
005F60FA  03 C8                           add ecx, eax
005F60FC  EB 41                           jmp 0x1405f613f
005F60FE  48 8D 47 FD                     lea rax, [rdi - 3]
005F6102  48 3B C8                        cmp rcx, rax
005F6105  73 0E                           jae 0x1405f6115
005F6107  8B 01                           mov eax, dword ptr [rcx]
005F6109  39 02                           cmp dword ptr [rdx], eax
005F610B  75 08                           jne 0x1405f6115
005F610D  48 83 C1 04                     add rcx, 4
005F6111  48 83 C2 04                     add rdx, 4
005F6115  48 8D 47 FF                     lea rax, [rdi - 1]
005F6119  48 3B C8                        cmp rcx, rax
005F611C  73 10                           jae 0x1405f612e
005F611E  0F B7 01                        movzx eax, word ptr [rcx]
005F6121  66 39 02                        cmp word ptr [rdx], ax
005F6124  75 08                           jne 0x1405f612e
005F6126  48 83 C1 02                     add rcx, 2
005F612A  48 83 C2 02                     add rdx, 2
005F612E  48 3B CF                        cmp rcx, rdi
005F6131  73 09                           jae 0x1405f613c
005F6133  8A 01                           mov al, byte ptr [rcx]
005F6135  38 02                           cmp byte ptr [rdx], al
005F6137  75 03                           jne 0x1405f613c
005F6139  48 03 CB                        add rcx, rbx
005F613C  41 2B CA                        sub ecx, r10d
005F613F  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
005F6144  41 2B CF                        sub ecx, r15d
005F6147  8B 74 24 4C                     mov esi, dword ptr [rsp + 0x4c]
005F614B  83 C1 04                        add ecx, 4
005F614E  3B 4C 24 48                     cmp ecx, dword ptr [rsp + 0x48]
005F6152  0F 8E BA 02 00 00               jle 0x1405f6412
005F6158  44 8B 64 24 68                  mov r12d, dword ptr [rsp + 0x68]
005F615D  45 2B E5                        sub r12d, r13d
005F6160  49 63 C7                        movsxd rax, r15d
005F6163  49 03 C3                        add rax, r11
005F6166  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
005F616A  8B 4D 88                        mov ecx, dword ptr [rbp - 0x78]
005F616D  44 8B D1                        mov r10d, ecx
005F6170  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
005F6174  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
005F6179  E9 A1 02 00 00                  jmp 0x1405f641f
005F617E  2B 45 90                        sub eax, dword ptr [rbp - 0x70]
005F6181  44 8B E0                        mov r12d, eax
005F6184  4C 8D 3C 10                     lea r15, [rax + rdx]
005F6188  41 8D 40 FC                     lea eax, [r8 - 4]
005F618C  44 3B E8                        cmp r13d, eax
005F618F  0F 87 85 02 00 00               ja 0x1405f641a
005F6195  41 39 37                        cmp dword ptr [r15], esi
005F6198  0F 85 7C 02 00 00               jne 0x1405f641a
005F619E  45 8B D0                        mov r10d, r8d
005F61A1  49 8D 5B 04                     lea rbx, [r11 + 4]
005F61A5  45 2B D5                        sub r10d, r13d
005F61A8  49 8D 57 04                     lea rdx, [r15 + 4]
005F61AC  4D 03 D3                        add r10, r11
005F61AF  48 8B CB                        mov rcx, rbx
005F61B2  4C 3B 54 24 60                  cmp r10, qword ptr [rsp + 0x60]
005F61B7  4C 0F 47 54 24 60               cmova r10, qword ptr [rsp + 0x60]
005F61BD  4D 8D 4A F9                     lea r9, [r10 - 7]
005F61C1  49 3B D9                        cmp rbx, r9
005F61C4  73 18                           jae 0x1405f61de
005F61C6  4C 8B 03                        mov r8, qword ptr [rbx]
005F61C9  4C 33 02                        xor r8, qword ptr [rdx]
005F61CC  75 06                           jne 0x1405f61d4
005F61CE  48 8D 4B 08                     lea rcx, [rbx + 8]
005F61D2  EB 1B                           jmp 0x1405f61ef
005F61D4  F3 49 0F BC C8                  tzcnt rcx, r8
005F61D9  C1 E9 03                        shr ecx, 3
005F61DC  EB 65                           jmp 0x1405f6243
005F61DE  49 3B C9                        cmp rcx, r9
005F61E1  73 20                           jae 0x1405f6203
005F61E3  4C 8B 01                        mov r8, qword ptr [rcx]
005F61E6  4C 33 02                        xor r8, qword ptr [rdx]
005F61E9  75 0A                           jne 0x1405f61f5
005F61EB  48 83 C1 08                     add rcx, 8
005F61EF  48 83 C2 08                     add rdx, 8
005F61F3  EB E9                           jmp 0x1405f61de
005F61F5  F3 49 0F BC C0                  tzcnt rax, r8
005F61FA  C1 E8 03                        shr eax, 3
005F61FD  2B C3                           sub eax, ebx
005F61FF  03 C8                           add ecx, eax
005F6201  EB 40                           jmp 0x1405f6243
005F6203  49 8D 42 FD                     lea rax, [r10 - 3]
005F6207  48 3B C8                        cmp rcx, rax
005F620A  73 0E                           jae 0x1405f621a
005F620C  8B 01                           mov eax, dword ptr [rcx]
005F620E  39 02                           cmp dword ptr [rdx], eax
005F6210  75 08                           jne 0x1405f621a
005F6212  48 83 C1 04                     add rcx, 4
005F6216  48 83 C2 04                     add rdx, 4
005F621A  49 8D 42 FF                     lea rax, [r10 - 1]
005F621E  48 3B C8                        cmp rcx, rax
005F6221  73 10                           jae 0x1405f6233
005F6223  0F B7 01                        movzx eax, word ptr [rcx]
005F6226  66 39 02                        cmp word ptr [rdx], ax
005F6229  75 08                           jne 0x1405f6233
005F622B  48 83 C1 02                     add rcx, 2
005F622F  48 83 C2 02                     add rdx, 2
005F6233  49 3B CA                        cmp rcx, r10
005F6236  73 09                           jae 0x1405f6241
005F6238  8A 01                           mov al, byte ptr [rcx]
005F623A  38 02                           cmp byte ptr [rdx], al
005F623C  75 03                           jne 0x1405f6241
005F623E  48 FF C1                        inc rcx
005F6241  2B CB                           sub ecx, ebx
005F6243  8D 71 04                        lea esi, [rcx + 4]
005F6246  48 63 DE                        movsxd rbx, esi
005F6249  49 03 DB                        add rbx, r11
005F624C  49 3B DA                        cmp rbx, r10
005F624F  0F 85 A3 00 00 00               jne 0x1405f62f8
005F6255  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
005F625A  4D 3B D0                        cmp r10, r8
005F625D  0F 83 95 00 00 00               jae 0x1405f62f8
005F6263  4D 8D 48 F9                     lea r9, [r8 - 7]
005F6267  49 8B D6                        mov rdx, r14
005F626A  48 8B CB                        mov rcx, rbx
005F626D  49 3B D9                        cmp rbx, r9
005F6270  73 10                           jae 0x1405f6282
005F6272  49 8B 0E                        mov rcx, qword ptr [r14]
005F6275  48 33 0B                        xor rcx, qword ptr [rbx]
005F6278  75 1F                           jne 0x1405f6299
005F627A  48 8D 4B 08                     lea rcx, [rbx + 8]
005F627E  49 8D 56 08                     lea rdx, [r14 + 8]
005F6282  49 3B C9                        cmp rcx, r9
005F6285  73 2A                           jae 0x1405f62b1
005F6287  4C 8B 01                        mov r8, qword ptr [rcx]
005F628A  4C 33 02                        xor r8, qword ptr [rdx]
005F628D  75 14                           jne 0x1405f62a3
005F628F  48 83 C1 08                     add rcx, 8
005F6293  48 83 C2 08                     add rdx, 8
005F6297  EB E9                           jmp 0x1405f6282
005F6299  F3 48 0F BC C9                  tzcnt rcx, rcx
005F629E  C1 E9 03                        shr ecx, 3
005F62A1  EB 53                           jmp 0x1405f62f6
005F62A3  F3 49 0F BC C0                  tzcnt rax, r8
005F62A8  C1 E8 03                        shr eax, 3
005F62AB  2B C3                           sub eax, ebx
005F62AD  03 C8                           add ecx, eax
005F62AF  EB 45                           jmp 0x1405f62f6
005F62B1  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
005F62B6  49 8D 40 FD                     lea rax, [r8 - 3]
005F62BA  48 3B C8                        cmp rcx, rax
005F62BD  73 0E                           jae 0x1405f62cd
005F62BF  8B 01                           mov eax, dword ptr [rcx]
005F62C1  39 02                           cmp dword ptr [rdx], eax
005F62C3  75 08                           jne 0x1405f62cd
005F62C5  48 83 C1 04                     add rcx, 4
005F62C9  48 83 C2 04                     add rdx, 4
005F62CD  49 8D 40 FF                     lea rax, [r8 - 1]
005F62D1  48 3B C8                        cmp rcx, rax
005F62D4  73 10                           jae 0x1405f62e6
005F62D6  0F B7 01                        movzx eax, word ptr [rcx]
005F62D9  66 39 02                        cmp word ptr [rdx], ax
005F62DC  75 08                           jne 0x1405f62e6
005F62DE  48 83 C1 02                     add rcx, 2
005F62E2  48 83 C2 02                     add rdx, 2
005F62E6  49 3B C8                        cmp rcx, r8
005F62E9  73 09                           jae 0x1405f62f4
005F62EB  8A 01                           mov al, byte ptr [rcx]
005F62ED  38 02                           cmp byte ptr [rdx], al
005F62EF  75 03                           jne 0x1405f62f4
005F62F1  48 FF C1                        inc rcx
005F62F4  2B CB                           sub ecx, ebx
005F62F6  03 F1                           add esi, ecx
005F62F8  33 C0                           xor eax, eax
005F62FA  48 39 45 B8                     cmp qword ptr [rbp - 0x48], rax
005F62FE  0F 84 D0 00 00 00               je 0x1405f63d4
005F6304  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
005F6309  8B D0                           mov edx, eax
005F630B  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
005F6310  8B F8                           mov edi, eax
005F6312  49 8B C8                        mov rcx, r8
005F6315  49 8B C1                        mov rax, r9
005F6318  49 2B CF                        sub rcx, r15
005F631B  49 2B C3                        sub rax, r11
005F631E  48 3B C1                        cmp rax, rcx
005F6321  7E 08                           jle 0x1405f632b
005F6323  41 8B C9                        mov ecx, r9d
005F6326  41 2B CB                        sub ecx, r11d
005F6329  EB 06                           jmp 0x1405f6331
005F632B  41 8B C8                        mov ecx, r8d
005F632E  41 2B CF                        sub ecx, r15d
005F6331  44 8B C9                        mov r9d, ecx
005F6334  4D 8D 57 FC                     lea r10, [r15 - 4]
005F6338  41 F7 D9                        neg r9d
005F633B  49 8B DB                        mov rbx, r11
005F633E  49 2B DF                        sub rbx, r15
005F6341  41 83 F9 03                     cmp r9d, 3
005F6345  7E 37                           jle 0x1405f637e
005F6347  46 8B 04 13                     mov r8d, dword ptr [rbx + r10]
005F634B  45 33 02                        xor r8d, dword ptr [r10]
005F634E  75 11                           jne 0x1405f6361
005F6350  83 EA 04                        sub edx, 4
005F6353  41 83 E9 04                     sub r9d, 4
005F6357  48 83 EF 04                     sub rdi, 4
005F635B  49 83 EA 04                     sub r10, 4
005F635F  EB E0                           jmp 0x1405f6341
005F6361  8B 7C 24 68                     mov edi, dword ptr [rsp + 0x68]
005F6365  45 33 E4                        xor r12d, r12d
005F6368  41 0F BD C0                     bsr eax, r8d
005F636C  41 8D 4C 24 1F                  lea ecx, [r12 + 0x1f]
005F6371  44 89 65 F8                     mov dword ptr [rbp - 8], r12d
005F6375  2B C8                           sub ecx, eax
005F6377  C1 E9 03                        shr ecx, 3
005F637A  2B D1                           sub edx, ecx
005F637C  EB 5C                           jmp 0x1405f63da
005F637E  4C 63 C9                        movsxd r9, ecx
005F6381  49 3B F9                        cmp rdi, r9
005F6384  7E 45                           jle 0x1405f63cb
005F6386  48 63 85 C8 00 00 00            movsxd rax, dword ptr [rbp + 0xc8]
005F638D  48 8D 4F FF                     lea rcx, [rdi - 1]
005F6391  48 2B 44 24 70                  sub rax, qword ptr [rsp + 0x70]
005F6396  BF 01 00 00 00                  mov edi, 1
005F639B  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
005F63A0  49 2B C4                        sub rax, r12
005F63A3  44 8B C7                        mov r8d, edi
005F63A6  4C 03 D0                        add r10, rax
005F63A9  4C 2B 44 24 70                  sub r8, qword ptr [rsp + 0x70]
005F63AE  49 03 CF                        add rcx, r15
005F63B1  4D 2B C4                        sub r8, r12
005F63B4  8A 01                           mov al, byte ptr [rcx]
005F63B6  41 38 44 0A FE                  cmp byte ptr [r10 + rcx - 2], al
005F63BB  75 0E                           jne 0x1405f63cb
005F63BD  48 2B CF                        sub rcx, rdi
005F63C0  2B D7                           sub edx, edi
005F63C2  49 8D 04 08                     lea rax, [r8 + rcx]
005F63C6  49 3B C1                        cmp rax, r9
005F63C9  7F E9                           jg 0x1405f63b4
005F63CB  8B 7C 24 68                     mov edi, dword ptr [rsp + 0x68]
005F63CF  45 33 E4                        xor r12d, r12d
005F63D2  EB 06                           jmp 0x1405f63da
005F63D4  45 33 E4                        xor r12d, r12d
005F63D7  41 8B D4                        mov edx, r12d
005F63DA  8B 4D 88                        mov ecx, dword ptr [rbp - 0x78]
005F63DD  2B F2                           sub esi, edx
005F63DF  44 8B D1                        mov r10d, ecx
005F63E2  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
005F63E7  3B 74 24 48                     cmp esi, dword ptr [rsp + 0x48]
005F63EB  7E 1A                           jle 0x1405f6407
005F63ED  41 2B FD                        sub edi, r13d
005F63F0  48 63 C2                        movsxd rax, edx
005F63F3  49 03 C3                        add rax, r11
005F63F6  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
005F63FA  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
005F63FE  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
005F6402  EB 03                           jmp 0x1405f6407
005F6404  41 8B CA                        mov ecx, r10d
005F6407  8B 74 24 4C                     mov esi, dword ptr [rsp + 0x4c]
005F640B  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005F6410  EB 10                           jmp 0x1405f6422
005F6412  8B 4D 88                        mov ecx, dword ptr [rbp - 0x78]
005F6415  44 8B D1                        mov r10d, ecx
005F6418  EB 08                           jmp 0x1405f6422
005F641A  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
005F641F  45 33 E4                        xor r12d, r12d
005F6422  81 7D 18 80 00 00 00            cmp dword ptr [rbp + 0x18], 0x80
005F6429  0F 8E 83 00 00 00               jle 0x1405f64b2
005F642F  48 8B 95 A0 00 00 00            mov rdx, qword ptr [rbp + 0xa0]
005F6436  41 B9 01 00 00 00               mov r9d, 1
005F643C  41 0F B7 C5                     movzx eax, r13w
005F6440  66 44 39 8C 42 00 00 02 00      cmp word ptr [rdx + rax*2 + 0x20000], r9w
005F6449  75 67                           jne 0x1405f64b2
005F644B  45 8D 7D FF                     lea r15d, [r13 - 1]
005F644F  45 85 D2                        test r10d, r10d
005F6452  0F 85 D1 00 00 00               jne 0x1405f6529
005F6458  45 8B C4                        mov r8d, r12d
005F645B  41 8B CC                        mov ecx, r12d
005F645E  8B C6                           mov eax, esi
005F6460  8B D6                           mov edx, esi
005F6462  C1 E8 18                        shr eax, 0x18
005F6465  40 3A F0                        cmp sil, al
005F6468  0F B7 C6                        movzx eax, si
005F646B  41 0F 94 C0                     sete r8b
005F646F  C1 EA 10                        shr edx, 0x10
005F6472  3B C2                           cmp eax, edx
005F6474  0F 94 C1                        sete cl
005F6477  44 85 C1                        test ecx, r8d
005F647A  74 2C                           je 0x1405f64a8
005F647C  49 8D 4B 04                     lea rcx, [r11 + 4]
005F6480  C7 44 24 40 02 00 00 00         mov dword ptr [rsp + 0x40], 2
005F6488  44 8B C6                        mov r8d, esi
005F648B  48 8B D7                        mov rdx, rdi
005F648E  E8 E1 94 00 00                  call 0x1405ff974
005F6493  8B C0                           mov eax, eax
005F6495  41 B9 01 00 00 00               mov r9d, 1
005F649B  48 83 C0 04                     add rax, 4
005F649F  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
005F64A3  E9 8A 00 00 00                  jmp 0x1405f6532
005F64A8  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
005F64AD  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
005F64B2  8B 5C 24 50                     mov ebx, dword ptr [rsp + 0x50]
005F64B6  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
005F64BD  41 0F B7 CD                     movzx ecx, r13w
005F64C1  0F B7 84 48 00 00 02 00         movzx eax, word ptr [rax + rcx*2 + 0x20000]
005F64C9  44 2B E8                        sub r13d, eax
005F64CC  8B 74 24 4C                     mov esi, dword ptr [rsp + 0x4c]
005F64D0  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
005F64D5  8B 7C 24 68                     mov edi, dword ptr [rsp + 0x68]
005F64D9  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
005F64DE  4C 8B 4D B8                     mov r9, qword ptr [rbp - 0x48]
005F64E2  44 3B EB                        cmp r13d, ebx
005F64E5  0F 83 A0 FA FF FF               jae 0x1405f5f8b
005F64EB  4C 8B 5D D8                     mov r11, qword ptr [rbp - 0x28]
005F64EF  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
005F64F3  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
005F64F8  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
005F64FC  45 33 D2                        xor r10d, r10d
005F64FF  44 8B 8D C8 00 00 00            mov r9d, dword ptr [rbp + 0xc8]
005F6506  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
005F650B  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
005F650F  44 89 7D 3C                     mov dword ptr [rbp + 0x3c], r15d
005F6513  44 89 65 38                     mov dword ptr [rbp + 0x38], r12d
005F6517  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
005F651B  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
005F6520  8B 74 24 74                     mov esi, dword ptr [rsp + 0x74]
005F6524  E9 E9 01 00 00                  jmp 0x1405f6712
005F6529  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
005F652D  83 F9 02                        cmp ecx, 2
005F6530  75 80                           jne 0x1405f64b2
005F6532  8B 5C 24 50                     mov ebx, dword ptr [rsp + 0x50]
005F6536  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
005F653B  44 3B FB                        cmp r15d, ebx
005F653E  0F 82 72 FF FF FF               jb 0x1405f64b6
005F6544  41 8B C0                        mov eax, r8d
005F6547  41 2B C7                        sub eax, r15d
005F654A  41 2B C1                        sub eax, r9d
005F654D  83 F8 03                        cmp eax, 3
005F6550  0F 82 60 FF FF FF               jb 0x1405f64b6
005F6556  41 8B DF                        mov ebx, r15d
005F6559  45 3B F8                        cmp r15d, r8d
005F655C  73 0D                           jae 0x1405f656b
005F655E  2B 5D 90                        sub ebx, dword ptr [rbp - 0x70]
005F6561  45 8B E1                        mov r12d, r9d
005F6564  48 03 5C 24 70                  add rbx, qword ptr [rsp + 0x70]
005F6569  EB 06                           jmp 0x1405f6571
005F656B  41 2B D8                        sub ebx, r8d
005F656E  49 03 DE                        add rbx, r14
005F6571  39 33                           cmp dword ptr [rbx], esi
005F6573  0F 85 39 FF FF FF               jne 0x1405f64b2
005F6579  45 85 E4                        test r12d, r12d
005F657C  48 8D 4B 04                     lea rcx, [rbx + 4]
005F6580  44 8B C6                        mov r8d, esi
005F6583  48 0F 45 7D 08                  cmovne rdi, qword ptr [rbp + 8]
005F6588  48 8B D7                        mov rdx, rdi
005F658B  E8 E4 93 00 00                  call 0x1405ff974
005F6590  8B F0                           mov esi, eax
005F6592  48 83 C6 04                     add rsi, 4
005F6596  45 85 E4                        test r12d, r12d
005F6599  74 39                           je 0x1405f65d4
005F659B  48 8D 04 1E                     lea rax, [rsi + rbx]
005F659F  48 3B C7                        cmp rax, rdi
005F65A2  75 29                           jne 0x1405f65cd
005F65A4  44 8B 44 24 4C                  mov r8d, dword ptr [rsp + 0x4c]
005F65A9  48 8B CE                        mov rcx, rsi
005F65AC  83 E1 03                        and ecx, 3
005F65AF  48 C1 E1 03                     shl rcx, 3
005F65B3  48 85 C9                        test rcx, rcx
005F65B6  74 03                           je 0x1405f65bb
005F65B8  41 D3 C0                        rol r8d, cl
005F65BB  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
005F65C0  49 8B CE                        mov rcx, r14
005F65C3  E8 AC 93 00 00                  call 0x1405ff974
005F65C8  8B C0                           mov eax, eax
005F65CA  48 03 F0                        add rsi, rax
005F65CD  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
005F65D2  EB 03                           jmp 0x1405f65d7
005F65D4  49 8B D6                        mov rdx, r14
005F65D7  44 8B 6C 24 4C                  mov r13d, dword ptr [rsp + 0x4c]
005F65DC  48 8B CB                        mov rcx, rbx
005F65DF  45 8B C5                        mov r8d, r13d
005F65E2  E8 79 94 00 00                  call 0x1405ffa60
005F65E7  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
005F65EC  33 D2                           xor edx, edx
005F65EE  8B F8                           mov edi, eax
005F65F0  45 85 E4                        test r12d, r12d
005F65F3  75 3F                           jne 0x1405f6634
005F65F5  48 2B DF                        sub rbx, rdi
005F65F8  49 3B DE                        cmp rbx, r14
005F65FB  75 37                           jne 0x1405f6634
005F65FD  44 39 45 90                     cmp dword ptr [rbp - 0x70], r8d
005F6601  73 31                           jae 0x1405f6634
005F6603  8B CF                           mov ecx, edi
005F6605  45 8B C5                        mov r8d, r13d
005F6608  F7 D9                           neg ecx
005F660A  83 E1 03                        and ecx, 3
005F660D  48 C1 E1 03                     shl rcx, 3
005F6611  48 85 C9                        test rcx, rcx
005F6614  74 03                           je 0x1405f6619
005F6616  41 D3 C0                        rol r8d, cl
005F6619  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
005F661E  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
005F6622  E8 39 94 00 00                  call 0x1405ffa60
005F6627  44 8B C0                        mov r8d, eax
005F662A  49 03 F8                        add rdi, r8
005F662D  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
005F6632  33 D2                           xor edx, edx
005F6634  8B 5C 24 50                     mov ebx, dword ptr [rsp + 0x50]
005F6638  41 8B CF                        mov ecx, r15d
005F663B  4C 8B 4D 10                     mov r9, qword ptr [rbp + 0x10]
005F663F  41 8B C7                        mov eax, r15d
005F6642  2B C7                           sub eax, edi
005F6644  44 8B EB                        mov r13d, ebx
005F6647  3B C3                           cmp eax, ebx
005F6649  44 0F 47 E8                     cmova r13d, eax
005F664D  41 2B CD                        sub ecx, r13d
005F6650  48 03 CE                        add rcx, rsi
005F6653  49 3B C9                        cmp rcx, r9
005F6656  72 22                           jb 0x1405f667a
005F6658  49 3B F1                        cmp rsi, r9
005F665B  77 1D                           ja 0x1405f667a
005F665D  45 2B F9                        sub r15d, r9d
005F6660  41 8B C0                        mov eax, r8d
005F6663  44 03 FE                        add r15d, esi
005F6666  45 8B E8                        mov r13d, r8d
005F6669  41 2B C7                        sub eax, r15d
005F666C  FF C8                           dec eax
005F666E  83 F8 03                        cmp eax, 3
005F6671  45 0F 43 EF                     cmovae r13d, r15d
005F6675  E9 52 FE FF FF                  jmp 0x1405f64cc
005F667A  41 8B C0                        mov eax, r8d
005F667D  41 2B C5                        sub eax, r13d
005F6680  FF C8                           dec eax
005F6682  83 F8 03                        cmp eax, 3
005F6685  72 75                           jb 0x1405f66fc
005F6687  48 39 55 B8                     cmp qword ptr [rbp - 0x48], rdx
005F668B  0F 85 3B FE FF FF               jne 0x1405f64cc
005F6691  4C 63 7C 24 48                  movsxd r15, dword ptr [rsp + 0x48]
005F6696  49 3B C9                        cmp rcx, r9
005F6699  49 8B D1                        mov rdx, r9
005F669C  48 0F 42 D1                     cmovb rdx, rcx
005F66A0  4C 3B FA                        cmp r15, rdx
005F66A3  73 33                           jae 0x1405f66d8
005F66A5  41 8B C5                        mov eax, r13d
005F66A8  41 8B C8                        mov ecx, r8d
005F66AB  48 2B C8                        sub rcx, rax
005F66AE  B8 FF FF 00 00                  mov eax, 0xffff
005F66B3  49 2B CE                        sub rcx, r14
005F66B6  49 03 CB                        add rcx, r11
005F66B9  48 3B C8                        cmp rcx, rax
005F66BC  0F 87 29 FE FF FF               ja 0x1405f64eb
005F66C2  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
005F66C6  44 8B FA                        mov r15d, edx
005F66C9  41 2B C5                        sub eax, r13d
005F66CC  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
005F66D0  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
005F66D4  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
005F66D8  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
005F66DF  41 0F B7 C5                     movzx eax, r13w
005F66E3  0F B7 8C 41 00 00 02 00         movzx ecx, word ptr [rcx + rax*2 + 0x20000]
005F66EB  41 3B CD                        cmp ecx, r13d
005F66EE  0F 87 F7 FD FF FF               ja 0x1405f64eb
005F66F4  44 2B E9                        sub r13d, ecx
005F66F7  E9 D0 FD FF FF                  jmp 0x1405f64cc
005F66FC  45 8B E8                        mov r13d, r8d
005F66FF  E9 C8 FD FF FF                  jmp 0x1405f64cc
005F6704  45 33 D2                        xor r10d, r10d
005F6707  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
005F670C  41 8B F2                        mov esi, r10d
005F670F  41 8B FA                        mov edi, r10d
005F6712  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
005F6716  41 3B F1                        cmp esi, r9d
005F6719  0F 8E 65 11 00 00               jle 0x1405f7884
005F671F  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
005F6723  49 3B CD                        cmp rcx, r13
005F6726  73 23                           jae 0x1405f674b
005F6728  48 63 45 EC                     movsxd rax, dword ptr [rbp - 0x14]
005F672C  49 03 C5                        add rax, r13
005F672F  4C 3B E0                        cmp r12, rax
005F6732  73 17                           jae 0x1405f674b
005F6734  4C 89 5D A0                     mov qword ptr [rbp - 0x60], r11
005F6738  4C 8B E9                        mov r13, rcx
005F673B  44 8B 4D A4                     mov r9d, dword ptr [rbp - 0x5c]
005F673F  44 89 8D C8 00 00 00            mov dword ptr [rbp + 0xc8], r9d
005F6746  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
005F674B  49 8B C4                        mov rax, r12
005F674E  49 2B C5                        sub rax, r13
005F6751  48 83 F8 03                     cmp rax, 3
005F6755  7D 11                           jge 0x1405f6768
005F6757  4D 8B EC                        mov r13, r12
005F675A  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
005F675F  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
005F6763  E9 A7 F6 FF FF                  jmp 0x1405f5e0f
005F6768  41 BB 12 00 00 00               mov r11d, 0x12
005F676E  49 8B C4                        mov rax, r12
005F6771  49 2B C5                        sub rax, r13
005F6774  49 3B C3                        cmp rax, r11
005F6777  7D 52                           jge 0x1405f67cb
005F6779  45 3B CB                        cmp r9d, r11d
005F677C  48 63 CE                        movsxd rcx, esi
005F677F  45 8B C1                        mov r8d, r9d
005F6782  45 0F 4F C3                     cmovg r8d, r11d
005F6786  48 83 C1 FC                     add rcx, -4
005F678A  49 63 D0                        movsxd rdx, r8d
005F678D  49 03 CC                        add rcx, r12
005F6790  49 03 D5                        add rdx, r13
005F6793  48 3B D1                        cmp rdx, rcx
005F6796  76 0D                           jbe 0x1405f67a5
005F6798  45 8B C4                        mov r8d, r12d
005F679B  45 2B C5                        sub r8d, r13d
005F679E  41 83 C0 FC                     add r8d, -4
005F67A2  44 03 C6                        add r8d, esi
005F67A5  41 8B CD                        mov ecx, r13d
005F67A8  41 2B CC                        sub ecx, r12d
005F67AB  41 03 C8                        add ecx, r8d
005F67AE  85 C9                           test ecx, ecx
005F67B0  7E 19                           jle 0x1405f67cb
005F67B2  48 63 C1                        movsxd rax, ecx
005F67B5  4C 03 E0                        add r12, rax
005F67B8  2B F1                           sub esi, ecx
005F67BA  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
005F67BE  89 74 24 74                     mov dword ptr [rsp + 0x74], esi
005F67C2  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
005F67C7  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
005F67CB  48 63 CE                        movsxd rcx, esi
005F67CE  49 03 CC                        add rcx, r12
005F67D1  48 3B CB                        cmp rcx, rbx
005F67D4  0F 87 CC 08 00 00               ja 0x1405f70a6
005F67DA  4C 8B 85 A0 00 00 00            mov r8, qword ptr [rbp + 0xa0]
005F67E1  48 8D 41 FD                     lea rax, [rcx - 3]
005F67E5  44 8B E8                        mov r13d, eax
005F67E8  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
005F67EC  4C 8B D8                        mov r11, rax
005F67EF  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
005F67F3  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
005F67F7  41 8B 90 1C 00 04 00            mov edx, dword ptr [r8 + 0x4001c]
005F67FE  4D 8B A0 08 00 04 00            mov r12, qword ptr [r8 + 0x40008]
005F6805  41 8B 88 18 00 04 00            mov ecx, dword ptr [r8 + 0x40018]
005F680C  45 2B EC                        sub r13d, r12d
005F680F  44 03 E9                        add r13d, ecx
005F6812  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
005F6816  8D 82 00 00 01 00               lea eax, [rdx + 0x10000]
005F681C  89 4D 90                        mov dword ptr [rbp - 0x70], ecx
005F681F  44 89 6C 24 68                  mov dword ptr [rsp + 0x68], r13d
005F6824  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
005F6828  41 3B C5                        cmp eax, r13d
005F682B  76 06                           jbe 0x1405f6833
005F682D  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
005F6831  EB 0B                           jmp 0x1405f683e
005F6833  41 8D 85 01 00 FF FF            lea eax, [r13 - 0xffff]
005F683A  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
005F683E  4D 8B 80 10 00 04 00            mov r8, qword ptr [r8 + 0x40010]
005F6845  4C 8B C9                        mov r9, rcx
005F6848  8B 45 24                        mov eax, dword ptr [rbp + 0x24]
005F684B  4C 2B CA                        sub r9, rdx
005F684E  41 8B 1B                        mov ebx, dword ptr [r11]
005F6851  4D 03 C8                        add r9, r8
005F6854  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
005F6858  45 8B D3                        mov r10d, r11d
005F685B  44 2B 55 80                     sub r10d, dword ptr [rbp - 0x80]
005F685F  45 33 C9                        xor r9d, r9d
005F6862  89 45 C0                        mov dword ptr [rbp - 0x40], eax
005F6865  45 8B F9                        mov r15d, r9d
005F6868  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
005F686F  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
005F6874  4C 89 4D B0                     mov qword ptr [rbp - 0x50], r9
005F6878  44 89 4C 24 78                  mov dword ptr [rsp + 0x78], r9d
005F687D  44 8B 88 20 00 04 00            mov r9d, dword ptr [rax + 0x40020]
005F6884  4C 89 45 D0                     mov qword ptr [rbp - 0x30], r8
005F6888  89 5C 24 4C                     mov dword ptr [rsp + 0x4c], ebx
005F688C  45 3B CD                        cmp r9d, r13d
005F688F  73 5F                           jae 0x1405f68f0
005F6891  45 8B C1                        mov r8d, r9d
005F6894  48 8B D8                        mov rbx, rax
005F6897  4C 2B C1                        sub r8, rcx
005F689A  41 BB FF FF 00 00               mov r11d, 0xffff
005F68A0  4D 03 C4                        add r8, r12
005F68A3  41 BC 01 00 00 00               mov r12d, 1
005F68A9  41 69 10 B1 79 37 9E            imul edx, dword ptr [r8], 0x9e3779b1
005F68B0  41 8B C9                        mov ecx, r9d
005F68B3  41 0F B7 C1                     movzx eax, r9w
005F68B7  48 C1 EA 11                     shr rdx, 0x11
005F68BB  2B 0C 93                        sub ecx, dword ptr [rbx + rdx*4]
005F68BE  49 3B CB                        cmp rcx, r11
005F68C1  49 0F 47 CB                     cmova rcx, r11
005F68C5  4D 03 C4                        add r8, r12
005F68C8  66 89 8C 43 00 00 02 00         mov word ptr [rbx + rax*2 + 0x20000], cx
005F68D0  44 89 0C 93                     mov dword ptr [rbx + rdx*4], r9d
005F68D4  45 03 CC                        add r9d, r12d
005F68D7  45 3B CD                        cmp r9d, r13d
005F68DA  72 CD                           jb 0x1405f68a9
005F68DC  4C 8B 5D 10                     mov r11, qword ptr [rbp + 0x10]
005F68E0  4C 8B 65 88                     mov r12, qword ptr [rbp - 0x78]
005F68E4  8B 5C 24 4C                     mov ebx, dword ptr [rsp + 0x4c]
005F68E8  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
005F68EC  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
005F68F0  4C 8B 8D A0 00 00 00            mov r9, qword ptr [rbp + 0xa0]
005F68F7  45 89 A9 20 00 04 00            mov dword ptr [r9 + 0x40020], r13d
005F68FE  41 69 0B B1 79 37 9E            imul ecx, dword ptr [r11], 0x9e3779b1
005F6905  48 C1 E9 11                     shr rcx, 0x11
005F6909  45 8B 2C 89                     mov r13d, dword ptr [r9 + rcx*4]
005F690D  4D 63 CA                        movsxd r9, r10d
005F6910  4C 89 4D D8                     mov qword ptr [rbp - 0x28], r9
005F6914  44 3B 6C 24 48                  cmp r13d, dword ptr [rsp + 0x48]
005F6919  0F 82 7A 05 00 00               jb 0x1405f6e99
005F691F  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
005F6923  44 8B 75 90                     mov r14d, dword ptr [rbp - 0x70]
005F6927  48 8B 7D 10                     mov rdi, qword ptr [rbp + 0x10]
005F692B  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
005F692F  48 63 C6                        movsxd rax, esi
005F6932  48 89 45 08                     mov qword ptr [rbp + 8], rax
005F6936  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
005F6939  45 33 D2                        xor r10d, r10d
005F693C  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
005F6940  44 8B F9                        mov r15d, ecx
005F6943  85 C0                           test eax, eax
005F6945  0F 8E 3D 05 00 00               jle 0x1405f6e88
005F694B  FF C8                           dec eax
005F694D  89 45 C0                        mov dword ptr [rbp - 0x40], eax
005F6950  45 3B EE                        cmp r13d, r14d
005F6953  0F 82 D2 01 00 00               jb 0x1405f6b2b
005F6959  4C 63 5C 24 40                  movsxd r11, dword ptr [rsp + 0x40]
005F695E  41 8B DD                        mov ebx, r13d
005F6961  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
005F6965  41 2B DE                        sub ebx, r14d
005F6968  49 03 DC                        add rbx, r12
005F696B  49 8B C3                        mov rax, r11
005F696E  49 2B C1                        sub rax, r9
005F6971  0F B7 44 18 FF                  movzx eax, word ptr [rax + rbx - 1]
005F6976  66 41 39 44 13 FF               cmp word ptr [r11 + rdx - 1], ax
005F697C  0F 85 37 04 00 00               jne 0x1405f6db9
005F6982  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
005F6986  39 03                           cmp dword ptr [rbx], eax
005F6988  0F 85 2B 04 00 00               jne 0x1405f6db9
005F698E  41 8B F2                        mov esi, r10d
005F6991  4D 85 C9                        test r9, r9
005F6994  0F 84 BD 00 00 00               je 0x1405f6a57
005F699A  49 8B CC                        mov rcx, r12
005F699D  48 8B C2                        mov rax, rdx
005F69A0  48 2B CB                        sub rcx, rbx
005F69A3  48 2B C7                        sub rax, rdi
005F69A6  45 8B DA                        mov r11d, r10d
005F69A9  48 3B C1                        cmp rax, rcx
005F69AC  7E 06                           jle 0x1405f69b4
005F69AE  8B CA                           mov ecx, edx
005F69B0  2B CF                           sub ecx, edi
005F69B2  EB 05                           jmp 0x1405f69b9
005F69B4  41 8B CC                        mov ecx, r12d
005F69B7  2B CB                           sub ecx, ebx
005F69B9  8B D1                           mov edx, ecx
005F69BB  4C 8D 4F FC                     lea r9, [rdi - 4]
005F69BF  F7 DA                           neg edx
005F69C1  4C 8B D3                        mov r10, rbx
005F69C4  4C 2B D7                        sub r10, rdi
005F69C7  83 FA 03                        cmp edx, 3
005F69CA  7E 2F                           jle 0x1405f69fb
005F69CC  47 8B 04 0A                     mov r8d, dword ptr [r10 + r9]
005F69D0  45 33 01                        xor r8d, dword ptr [r9]
005F69D3  75 10                           jne 0x1405f69e5
005F69D5  83 EE 04                        sub esi, 4
005F69D8  83 EA 04                        sub edx, 4
005F69DB  49 83 EB 04                     sub r11, 4
005F69DF  49 83 E9 04                     sub r9, 4
005F69E3  EB E2                           jmp 0x1405f69c7
005F69E5  83 65 F8 00                     and dword ptr [rbp - 8], 0
005F69E9  B9 1F 00 00 00                  mov ecx, 0x1f
005F69EE  41 0F BD C0                     bsr eax, r8d
005F69F2  2B C8                           sub ecx, eax
005F69F4  C1 E9 03                        shr ecx, 3
005F69F7  2B F1                           sub esi, ecx
005F69F9  EB 57                           jmp 0x1405f6a52
005F69FB  4C 63 C1                        movsxd r8, ecx
005F69FE  4D 3B D8                        cmp r11, r8
005F6A01  7E 4F                           jle 0x1405f6a52
005F6A03  4C 8B 55 08                     mov r10, qword ptr [rbp + 8]
005F6A07  45 8B CD                        mov r9d, r13d
005F6A0A  45 2B CE                        sub r9d, r14d
005F6A0D  B9 04 00 00 00                  mov ecx, 4
005F6A12  4D 2B CA                        sub r9, r10
005F6A15  49 2B CA                        sub rcx, r10
005F6A18  41 BE 01 00 00 00               mov r14d, 1
005F6A1E  4B 8D 04 13                     lea rax, [r11 + r10]
005F6A22  4C 8B 5D 80                     mov r11, qword ptr [rbp - 0x80]
005F6A26  4D 2B CB                        sub r9, r11
005F6A29  4D 03 CC                        add r9, r12
005F6A2C  49 8D 53 FC                     lea rdx, [r11 - 4]
005F6A30  48 03 D0                        add rdx, rax
005F6A33  49 2B CB                        sub rcx, r11
005F6A36  41 8A 44 11 03                  mov al, byte ptr [r9 + rdx + 3]
005F6A3B  38 02                           cmp byte ptr [rdx], al
005F6A3D  75 0F                           jne 0x1405f6a4e
005F6A3F  49 2B D6                        sub rdx, r14
005F6A42  41 2B F6                        sub esi, r14d
005F6A45  48 8D 04 11                     lea rax, [rcx + rdx]
005F6A49  49 3B C0                        cmp rax, r8
005F6A4C  7F E8                           jg 0x1405f6a36
005F6A4E  44 8B 75 90                     mov r14d, dword ptr [rbp - 0x70]
005F6A52  44 8B 5C 24 40                  mov r11d, dword ptr [rsp + 0x40]
005F6A57  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
005F6A5C  4C 8D 57 04                     lea r10, [rdi + 4]
005F6A60  49 83 C1 F9                     add r9, -7
005F6A64  48 8D 53 04                     lea rdx, [rbx + 4]
005F6A68  49 8B CA                        mov rcx, r10
005F6A6B  4D 3B D1                        cmp r10, r9
005F6A6E  73 18                           jae 0x1405f6a88
005F6A70  4D 8B 02                        mov r8, qword ptr [r10]
005F6A73  4C 33 02                        xor r8, qword ptr [rdx]
005F6A76  75 06                           jne 0x1405f6a7e
005F6A78  49 8D 4A 08                     lea rcx, [r10 + 8]
005F6A7C  EB 1B                           jmp 0x1405f6a99
005F6A7E  F3 49 0F BC C8                  tzcnt rcx, r8
005F6A83  C1 E9 03                        shr ecx, 3
005F6A86  EB 6C                           jmp 0x1405f6af4
005F6A88  49 3B C9                        cmp rcx, r9
005F6A8B  73 21                           jae 0x1405f6aae
005F6A8D  4C 8B 01                        mov r8, qword ptr [rcx]
005F6A90  4C 33 02                        xor r8, qword ptr [rdx]
005F6A93  75 0A                           jne 0x1405f6a9f
005F6A95  48 83 C1 08                     add rcx, 8
005F6A99  48 83 C2 08                     add rdx, 8
005F6A9D  EB E9                           jmp 0x1405f6a88
005F6A9F  F3 49 0F BC C0                  tzcnt rax, r8
005F6AA4  C1 E8 03                        shr eax, 3
005F6AA7  41 2B C2                        sub eax, r10d
005F6AAA  03 C8                           add ecx, eax
005F6AAC  EB 46                           jmp 0x1405f6af4
005F6AAE  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
005F6AB3  49 8D 40 FD                     lea rax, [r8 - 3]
005F6AB7  48 3B C8                        cmp rcx, rax
005F6ABA  73 0E                           jae 0x1405f6aca
005F6ABC  8B 01                           mov eax, dword ptr [rcx]
005F6ABE  39 02                           cmp dword ptr [rdx], eax
005F6AC0  75 08                           jne 0x1405f6aca
005F6AC2  48 83 C1 04                     add rcx, 4
005F6AC6  48 83 C2 04                     add rdx, 4
005F6ACA  49 8D 40 FF                     lea rax, [r8 - 1]
005F6ACE  48 3B C8                        cmp rcx, rax
005F6AD1  73 10                           jae 0x1405f6ae3
005F6AD3  0F B7 01                        movzx eax, word ptr [rcx]
005F6AD6  66 39 02                        cmp word ptr [rdx], ax
005F6AD9  75 08                           jne 0x1405f6ae3
005F6ADB  48 83 C1 02                     add rcx, 2
005F6ADF  48 83 C2 02                     add rdx, 2
005F6AE3  49 3B C8                        cmp rcx, r8
005F6AE6  73 09                           jae 0x1405f6af1
005F6AE8  8A 01                           mov al, byte ptr [rcx]
005F6AEA  38 02                           cmp byte ptr [rdx], al
005F6AEC  75 03                           jne 0x1405f6af1
005F6AEE  48 FF C1                        inc rcx
005F6AF1  41 2B CA                        sub ecx, r10d
005F6AF4  8B 5C 24 4C                     mov ebx, dword ptr [rsp + 0x4c]
005F6AF8  2B CE                           sub ecx, esi
005F6AFA  83 C1 04                        add ecx, 4
005F6AFD  41 3B CB                        cmp ecx, r11d
005F6B00  44 8B 5C 24 44                  mov r11d, dword ptr [rsp + 0x44]
005F6B05  7E 19                           jle 0x1405f6b20
005F6B07  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
005F6B0B  41 2B C5                        sub eax, r13d
005F6B0E  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
005F6B12  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
005F6B16  48 63 C6                        movsxd rax, esi
005F6B19  48 03 C7                        add rax, rdi
005F6B1C  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
005F6B20  41 8B CF                        mov ecx, r15d
005F6B23  45 33 D2                        xor r10d, r10d
005F6B26  E9 97 02 00 00                  jmp 0x1405f6dc2
005F6B2B  41 8B F5                        mov esi, r13d
005F6B2E  41 8D 46 FC                     lea eax, [r14 - 4]
005F6B32  2B F2                           sub esi, edx
005F6B34  49 03 F0                        add rsi, r8
005F6B37  44 3B E8                        cmp r13d, eax
005F6B3A  0F 87 7D 02 00 00               ja 0x1405f6dbd
005F6B40  39 1E                           cmp dword ptr [rsi], ebx
005F6B42  0F 85 75 02 00 00               jne 0x1405f6dbd
005F6B48  45 8B D6                        mov r10d, r14d
005F6B4B  4C 8D 5F 04                     lea r11, [rdi + 4]
005F6B4F  45 2B D5                        sub r10d, r13d
005F6B52  48 8D 56 04                     lea rdx, [rsi + 4]
005F6B56  4C 03 D7                        add r10, rdi
005F6B59  49 8B CB                        mov rcx, r11
005F6B5C  4C 3B 54 24 60                  cmp r10, qword ptr [rsp + 0x60]
005F6B61  4C 0F 47 54 24 60               cmova r10, qword ptr [rsp + 0x60]
005F6B67  4D 8D 4A F9                     lea r9, [r10 - 7]
005F6B6B  4D 3B D9                        cmp r11, r9
005F6B6E  73 18                           jae 0x1405f6b88
005F6B70  4D 8B 03                        mov r8, qword ptr [r11]
005F6B73  4C 33 02                        xor r8, qword ptr [rdx]
005F6B76  75 06                           jne 0x1405f6b7e
005F6B78  49 8D 4B 08                     lea rcx, [r11 + 8]
005F6B7C  EB 1B                           jmp 0x1405f6b99
005F6B7E  F3 49 0F BC C8                  tzcnt rcx, r8
005F6B83  C1 E9 03                        shr ecx, 3
005F6B86  EB 67                           jmp 0x1405f6bef
005F6B88  49 3B C9                        cmp rcx, r9
005F6B8B  73 21                           jae 0x1405f6bae
005F6B8D  4C 8B 01                        mov r8, qword ptr [rcx]
005F6B90  4C 33 02                        xor r8, qword ptr [rdx]
005F6B93  75 0A                           jne 0x1405f6b9f
005F6B95  48 83 C1 08                     add rcx, 8
005F6B99  48 83 C2 08                     add rdx, 8
005F6B9D  EB E9                           jmp 0x1405f6b88
005F6B9F  F3 49 0F BC C0                  tzcnt rax, r8
005F6BA4  C1 E8 03                        shr eax, 3
005F6BA7  41 2B C3                        sub eax, r11d
005F6BAA  03 C8                           add ecx, eax
005F6BAC  EB 41                           jmp 0x1405f6bef
005F6BAE  49 8D 42 FD                     lea rax, [r10 - 3]
005F6BB2  48 3B C8                        cmp rcx, rax
005F6BB5  73 0E                           jae 0x1405f6bc5
005F6BB7  8B 01                           mov eax, dword ptr [rcx]
005F6BB9  39 02                           cmp dword ptr [rdx], eax
005F6BBB  75 08                           jne 0x1405f6bc5
005F6BBD  48 83 C1 04                     add rcx, 4
005F6BC1  48 83 C2 04                     add rdx, 4
005F6BC5  49 8D 42 FF                     lea rax, [r10 - 1]
005F6BC9  48 3B C8                        cmp rcx, rax
005F6BCC  73 10                           jae 0x1405f6bde
005F6BCE  0F B7 01                        movzx eax, word ptr [rcx]
005F6BD1  66 39 02                        cmp word ptr [rdx], ax
005F6BD4  75 08                           jne 0x1405f6bde
005F6BD6  48 83 C1 02                     add rcx, 2
005F6BDA  48 83 C2 02                     add rdx, 2
005F6BDE  49 3B CA                        cmp rcx, r10
005F6BE1  73 09                           jae 0x1405f6bec
005F6BE3  8A 01                           mov al, byte ptr [rcx]
005F6BE5  38 02                           cmp byte ptr [rdx], al
005F6BE7  75 03                           jne 0x1405f6bec
005F6BE9  48 FF C1                        inc rcx
005F6BEC  41 2B CB                        sub ecx, r11d
005F6BEF  8D 59 04                        lea ebx, [rcx + 4]
005F6BF2  4C 63 DB                        movsxd r11, ebx
005F6BF5  4C 03 DF                        add r11, rdi
005F6BF8  4D 3B DA                        cmp r11, r10
005F6BFB  0F 85 A7 00 00 00               jne 0x1405f6ca8
005F6C01  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
005F6C06  4D 3B D0                        cmp r10, r8
005F6C09  0F 83 99 00 00 00               jae 0x1405f6ca8
005F6C0F  4D 8D 48 F9                     lea r9, [r8 - 7]
005F6C13  49 8B D4                        mov rdx, r12
005F6C16  49 8B CB                        mov rcx, r11
005F6C19  4D 3B D9                        cmp r11, r9
005F6C1C  73 12                           jae 0x1405f6c30
005F6C1E  49 8B 13                        mov rdx, qword ptr [r11]
005F6C21  49 33 14 24                     xor rdx, qword ptr [r12]
005F6C25  75 20                           jne 0x1405f6c47
005F6C27  49 8D 4B 08                     lea rcx, [r11 + 8]
005F6C2B  49 8D 54 24 08                  lea rdx, [r12 + 8]
005F6C30  49 3B C9                        cmp rcx, r9
005F6C33  73 2B                           jae 0x1405f6c60
005F6C35  4C 8B 01                        mov r8, qword ptr [rcx]
005F6C38  4C 33 02                        xor r8, qword ptr [rdx]
005F6C3B  75 14                           jne 0x1405f6c51
005F6C3D  48 83 C1 08                     add rcx, 8
005F6C41  48 83 C2 08                     add rdx, 8
005F6C45  EB E9                           jmp 0x1405f6c30
005F6C47  F3 48 0F BC CA                  tzcnt rcx, rdx
005F6C4C  C1 E9 03                        shr ecx, 3
005F6C4F  EB 55                           jmp 0x1405f6ca6
005F6C51  F3 49 0F BC C0                  tzcnt rax, r8
005F6C56  C1 E8 03                        shr eax, 3
005F6C59  41 2B C3                        sub eax, r11d
005F6C5C  03 C8                           add ecx, eax
005F6C5E  EB 46                           jmp 0x1405f6ca6
005F6C60  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
005F6C65  49 8D 40 FD                     lea rax, [r8 - 3]
005F6C69  48 3B C8                        cmp rcx, rax
005F6C6C  73 0E                           jae 0x1405f6c7c
005F6C6E  8B 01                           mov eax, dword ptr [rcx]
005F6C70  39 02                           cmp dword ptr [rdx], eax
005F6C72  75 08                           jne 0x1405f6c7c
005F6C74  48 83 C1 04                     add rcx, 4
005F6C78  48 83 C2 04                     add rdx, 4
005F6C7C  49 8D 40 FF                     lea rax, [r8 - 1]
005F6C80  48 3B C8                        cmp rcx, rax
005F6C83  73 10                           jae 0x1405f6c95
005F6C85  0F B7 01                        movzx eax, word ptr [rcx]
005F6C88  66 39 02                        cmp word ptr [rdx], ax
005F6C8B  75 08                           jne 0x1405f6c95
005F6C8D  48 83 C1 02                     add rcx, 2
005F6C91  48 83 C2 02                     add rdx, 2
005F6C95  49 3B C8                        cmp rcx, r8
005F6C98  73 09                           jae 0x1405f6ca3
005F6C9A  8A 01                           mov al, byte ptr [rcx]
005F6C9C  38 02                           cmp byte ptr [rdx], al
005F6C9E  75 03                           jne 0x1405f6ca3
005F6CA0  48 FF C1                        inc rcx
005F6CA3  41 2B CB                        sub ecx, r11d
005F6CA6  03 D9                           add ebx, ecx
005F6CA8  45 33 D2                        xor r10d, r10d
005F6CAB  45 8B C2                        mov r8d, r10d
005F6CAE  4C 39 55 D8                     cmp qword ptr [rbp - 0x28], r10
005F6CB2  74 68                           je 0x1405f6d1c
005F6CB4  4C 8B 65 D0                     mov r12, qword ptr [rbp - 0x30]
005F6CB8  45 8B DA                        mov r11d, r10d
005F6CBB  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
005F6CBF  49 8B CC                        mov rcx, r12
005F6CC2  48 8B C2                        mov rax, rdx
005F6CC5  48 2B CE                        sub rcx, rsi
005F6CC8  48 2B C7                        sub rax, rdi
005F6CCB  48 3B C1                        cmp rax, rcx
005F6CCE  7E 06                           jle 0x1405f6cd6
005F6CD0  8B CA                           mov ecx, edx
005F6CD2  2B CF                           sub ecx, edi
005F6CD4  EB 05                           jmp 0x1405f6cdb
005F6CD6  41 8B CC                        mov ecx, r12d
005F6CD9  2B CE                           sub ecx, esi
005F6CDB  8B D1                           mov edx, ecx
005F6CDD  4C 8D 57 FC                     lea r10, [rdi - 4]
005F6CE1  F7 DA                           neg edx
005F6CE3  48 2B F7                        sub rsi, rdi
005F6CE6  83 FA 03                        cmp edx, 3
005F6CE9  7E 61                           jle 0x1405f6d4c
005F6CEB  46 8B 0C 16                     mov r9d, dword ptr [rsi + r10]
005F6CEF  45 33 0A                        xor r9d, dword ptr [r10]
005F6CF2  75 11                           jne 0x1405f6d05
005F6CF4  41 83 E8 04                     sub r8d, 4
005F6CF8  83 EA 04                        sub edx, 4
005F6CFB  49 83 EB 04                     sub r11, 4
005F6CFF  49 83 EA 04                     sub r10, 4
005F6D03  EB E1                           jmp 0x1405f6ce6
005F6D05  45 33 D2                        xor r10d, r10d
005F6D08  41 0F BD C1                     bsr eax, r9d
005F6D0C  41 8D 4A 1F                     lea ecx, [r10 + 0x1f]
005F6D10  44 89 55 F8                     mov dword ptr [rbp - 8], r10d
005F6D14  2B C8                           sub ecx, eax
005F6D16  C1 E9 03                        shr ecx, 3
005F6D19  44 2B C1                        sub r8d, ecx
005F6D1C  44 8B 5C 24 44                  mov r11d, dword ptr [rsp + 0x44]
005F6D21  41 2B D8                        sub ebx, r8d
005F6D24  41 8B CF                        mov ecx, r15d
005F6D27  3B 5C 24 40                     cmp ebx, dword ptr [rsp + 0x40]
005F6D2B  7E 19                           jle 0x1405f6d46
005F6D2D  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
005F6D31  41 2B C5                        sub eax, r13d
005F6D34  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
005F6D38  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
005F6D3C  49 63 C0                        movsxd rax, r8d
005F6D3F  48 03 C7                        add rax, rdi
005F6D42  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
005F6D46  8B 5C 24 4C                     mov ebx, dword ptr [rsp + 0x4c]
005F6D4A  EB 76                           jmp 0x1405f6dc2
005F6D4C  4C 63 C9                        movsxd r9, ecx
005F6D4F  4D 3B D9                        cmp r11, r9
005F6D52  7E 58                           jle 0x1405f6dac
005F6D54  48 8B 75 08                     mov rsi, qword ptr [rbp + 8]
005F6D58  45 8B D5                        mov r10d, r13d
005F6D5B  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
005F6D5F  B9 04 00 00 00                  mov ecx, 4
005F6D64  48 83 C2 FC                     add rdx, -4
005F6D68  48 2B CE                        sub rcx, rsi
005F6D6B  41 BE 01 00 00 00               mov r14d, 1
005F6D71  49 8D 04 33                     lea rax, [r11 + rsi]
005F6D75  44 8B 5C 24 44                  mov r11d, dword ptr [rsp + 0x44]
005F6D7A  45 2B D3                        sub r10d, r11d
005F6D7D  48 03 D0                        add rdx, rax
005F6D80  4C 2B D6                        sub r10, rsi
005F6D83  4C 2B 55 80                     sub r10, qword ptr [rbp - 0x80]
005F6D87  4D 03 D4                        add r10, r12
005F6D8A  48 2B 4D 80                     sub rcx, qword ptr [rbp - 0x80]
005F6D8E  41 8A 44 12 03                  mov al, byte ptr [r10 + rdx + 3]
005F6D93  38 02                           cmp byte ptr [rdx], al
005F6D95  75 0F                           jne 0x1405f6da6
005F6D97  49 2B D6                        sub rdx, r14
005F6D9A  45 2B C6                        sub r8d, r14d
005F6D9D  48 8D 04 11                     lea rax, [rcx + rdx]
005F6DA1  49 3B C1                        cmp rax, r9
005F6DA4  7F E8                           jg 0x1405f6d8e
005F6DA6  44 8B 75 90                     mov r14d, dword ptr [rbp - 0x70]
005F6DAA  EB 05                           jmp 0x1405f6db1
005F6DAC  44 8B 5C 24 44                  mov r11d, dword ptr [rsp + 0x44]
005F6DB1  45 33 D2                        xor r10d, r10d
005F6DB4  E9 68 FF FF FF                  jmp 0x1405f6d21
005F6DB9  8B 5C 24 4C                     mov ebx, dword ptr [rsp + 0x4c]
005F6DBD  44 8B 5C 24 44                  mov r11d, dword ptr [rsp + 0x44]
005F6DC2  81 7D 18 80 00 00 00            cmp dword ptr [rbp + 0x18], 0x80
005F6DC9  0F 8E 82 00 00 00               jle 0x1405f6e51
005F6DCF  48 8B 95 A0 00 00 00            mov rdx, qword ptr [rbp + 0xa0]
005F6DD6  41 B9 01 00 00 00               mov r9d, 1
005F6DDC  41 0F B7 C5                     movzx eax, r13w
005F6DE0  66 44 39 8C 42 00 00 02 00      cmp word ptr [rdx + rax*2 + 0x20000], r9w
005F6DE9  75 66                           jne 0x1405f6e51
005F6DEB  45 8D 65 FF                     lea r12d, [r13 - 1]
005F6DEF  85 C9                           test ecx, ecx
005F6DF1  0F 85 CD 00 00 00               jne 0x1405f6ec4
005F6DF7  45 8B C2                        mov r8d, r10d
005F6DFA  41 8B CA                        mov ecx, r10d
005F6DFD  8B C3                           mov eax, ebx
005F6DFF  8B D3                           mov edx, ebx
005F6E01  C1 E8 18                        shr eax, 0x18
005F6E04  3A D8                           cmp bl, al
005F6E06  0F B7 C3                        movzx eax, bx
005F6E09  41 0F 94 C0                     sete r8b
005F6E0D  C1 EA 10                        shr edx, 0x10
005F6E10  3B C2                           cmp eax, edx
005F6E12  0F 94 C1                        sete cl
005F6E15  44 85 C1                        test ecx, r8d
005F6E18  74 32                           je 0x1405f6e4c
005F6E1A  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
005F6E1F  48 8D 4F 04                     lea rcx, [rdi + 4]
005F6E23  48 8B D6                        mov rdx, rsi
005F6E26  C7 44 24 50 02 00 00 00         mov dword ptr [rsp + 0x50], 2
005F6E2E  44 8B C3                        mov r8d, ebx
005F6E31  E8 3E 8B 00 00                  call 0x1405ff974
005F6E36  8B C0                           mov eax, eax
005F6E38  48 83 C0 04                     add rax, 4
005F6E3C  45 33 D2                        xor r10d, r10d
005F6E3F  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
005F6E43  45 8D 4A 01                     lea r9d, [r10 + 1]
005F6E47  E9 88 00 00 00                  jmp 0x1405f6ed4
005F6E4C  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
005F6E51  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
005F6E55  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
005F6E5C  41 0F B7 CD                     movzx ecx, r13w
005F6E60  0F B7 84 48 00 00 02 00         movzx eax, word ptr [rax + rcx*2 + 0x20000]
005F6E68  44 2B E8                        sub r13d, eax
005F6E6B  4C 8B 65 88                     mov r12, qword ptr [rbp - 0x78]
005F6E6F  44 3B EB                        cmp r13d, ebx
005F6E72  8B 5C 24 4C                     mov ebx, dword ptr [rsp + 0x4c]
005F6E76  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
005F6E7A  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
005F6E7E  4C 8B 4D D8                     mov r9, qword ptr [rbp - 0x28]
005F6E82  0F 83 AE FA FF FF               jae 0x1405f6936
005F6E88  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
005F6E8C  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
005F6E90  8B 74 24 74                     mov esi, dword ptr [rsp + 0x74]
005F6E94  44 8B 7C 24 78                  mov r15d, dword ptr [rsp + 0x78]
005F6E99  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
005F6E9D  45 33 D2                        xor r10d, r10d
005F6EA0  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
005F6EA5  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
005F6EA9  89 45 44                        mov dword ptr [rbp + 0x44], eax
005F6EAC  44 89 7D 40                     mov dword ptr [rbp + 0x40], r15d
005F6EB0  45 8D 5A 12                     lea r11d, [r10 + 0x12]
005F6EB4  48 8B 5D 40                     mov rbx, qword ptr [rbp + 0x40]
005F6EB8  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
005F6EBC  8B 45 D4                        mov eax, dword ptr [rbp - 0x2c]
005F6EBF  E9 F0 01 00 00                  jmp 0x1405f70b4
005F6EC4  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
005F6EC9  41 83 FF 02                     cmp r15d, 2
005F6ECD  75 82                           jne 0x1405f6e51
005F6ECF  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
005F6ED4  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
005F6ED8  44 3B E3                        cmp r12d, ebx
005F6EDB  0F 82 74 FF FF FF               jb 0x1405f6e55
005F6EE1  41 8B C6                        mov eax, r14d
005F6EE4  41 2B C4                        sub eax, r12d
005F6EE7  41 2B C1                        sub eax, r9d
005F6EEA  83 F8 03                        cmp eax, 3
005F6EED  0F 82 62 FF FF FF               jb 0x1405f6e55
005F6EF3  41 8B DC                        mov ebx, r12d
005F6EF6  45 3B E6                        cmp r12d, r14d
005F6EF9  73 0C                           jae 0x1405f6f07
005F6EFB  41 2B DB                        sub ebx, r11d
005F6EFE  45 8B F9                        mov r15d, r9d
005F6F01  48 03 5D D0                     add rbx, qword ptr [rbp - 0x30]
005F6F05  EB 0A                           jmp 0x1405f6f11
005F6F07  41 2B DE                        sub ebx, r14d
005F6F0A  45 8B FA                        mov r15d, r10d
005F6F0D  48 03 5D 88                     add rbx, qword ptr [rbp - 0x78]
005F6F11  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
005F6F15  39 03                           cmp dword ptr [rbx], eax
005F6F17  0F 85 34 FF FF FF               jne 0x1405f6e51
005F6F1D  45 85 FF                        test r15d, r15d
005F6F20  48 8D 4B 04                     lea rcx, [rbx + 4]
005F6F24  4C 8B DE                        mov r11, rsi
005F6F27  44 8B C0                        mov r8d, eax
005F6F2A  4C 0F 45 5D E8                  cmovne r11, qword ptr [rbp - 0x18]
005F6F2F  44 8B E8                        mov r13d, eax
005F6F32  49 8B D3                        mov rdx, r11
005F6F35  E8 3A 8A 00 00                  call 0x1405ff974
005F6F3A  8B F0                           mov esi, eax
005F6F3C  48 83 C6 04                     add rsi, 4
005F6F40  45 85 FF                        test r15d, r15d
005F6F43  74 38                           je 0x1405f6f7d
005F6F45  48 8D 04 1E                     lea rax, [rsi + rbx]
005F6F49  49 3B C3                        cmp rax, r11
005F6F4C  75 29                           jne 0x1405f6f77
005F6F4E  48 8B CE                        mov rcx, rsi
005F6F51  45 8B C5                        mov r8d, r13d
005F6F54  83 E1 03                        and ecx, 3
005F6F57  48 C1 E1 03                     shl rcx, 3
005F6F5B  48 85 C9                        test rcx, rcx
005F6F5E  74 03                           je 0x1405f6f63
005F6F60  41 D3 C0                        rol r8d, cl
005F6F63  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
005F6F68  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
005F6F6C  E8 03 8A 00 00                  call 0x1405ff974
005F6F71  44 8B D8                        mov r11d, eax
005F6F74  49 03 F3                        add rsi, r11
005F6F77  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
005F6F7B  EB 04                           jmp 0x1405f6f81
005F6F7D  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
005F6F81  45 8B C5                        mov r8d, r13d
005F6F84  48 8B CB                        mov rcx, rbx
005F6F87  E8 D4 8A 00 00                  call 0x1405ffa60
005F6F8C  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
005F6F90  33 D2                           xor edx, edx
005F6F92  44 8B D8                        mov r11d, eax
005F6F95  45 85 FF                        test r15d, r15d
005F6F98  75 3F                           jne 0x1405f6fd9
005F6F9A  49 2B DB                        sub rbx, r11
005F6F9D  49 3B D8                        cmp rbx, r8
005F6FA0  75 37                           jne 0x1405f6fd9
005F6FA2  44 39 74 24 44                  cmp dword ptr [rsp + 0x44], r14d
005F6FA7  73 30                           jae 0x1405f6fd9
005F6FA9  41 8B CB                        mov ecx, r11d
005F6FAC  45 8B C5                        mov r8d, r13d
005F6FAF  F7 D9                           neg ecx
005F6FB1  83 E1 03                        and ecx, 3
005F6FB4  48 C1 E1 03                     shl rcx, 3
005F6FB8  48 85 C9                        test rcx, rcx
005F6FBB  74 03                           je 0x1405f6fc0
005F6FBD  41 D3 C0                        rol r8d, cl
005F6FC0  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
005F6FC4  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
005F6FC8  E8 93 8A 00 00                  call 0x1405ffa60
005F6FCD  44 8B C0                        mov r8d, eax
005F6FD0  4D 03 D8                        add r11, r8
005F6FD3  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
005F6FD7  33 D2                           xor edx, edx
005F6FD9  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
005F6FDD  41 8B CC                        mov ecx, r12d
005F6FE0  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
005F6FE4  41 8B C4                        mov eax, r12d
005F6FE7  41 2B C3                        sub eax, r11d
005F6FEA  44 8B EB                        mov r13d, ebx
005F6FED  3B C3                           cmp eax, ebx
005F6FEF  44 0F 47 E8                     cmova r13d, eax
005F6FF3  41 2B CD                        sub ecx, r13d
005F6FF6  48 03 CE                        add rcx, rsi
005F6FF9  49 3B C9                        cmp rcx, r9
005F6FFC  72 21                           jb 0x1405f701f
005F6FFE  49 3B F1                        cmp rsi, r9
005F7001  77 1C                           ja 0x1405f701f
005F7003  41 2B F1                        sub esi, r9d
005F7006  41 8B C6                        mov eax, r14d
005F7009  41 03 F4                        add esi, r12d
005F700C  45 8B EE                        mov r13d, r14d
005F700F  2B C6                           sub eax, esi
005F7011  FF C8                           dec eax
005F7013  83 F8 03                        cmp eax, 3
005F7016  44 0F 43 EE                     cmovae r13d, esi
005F701A  E9 4C FE FF FF                  jmp 0x1405f6e6b
005F701F  41 8B C6                        mov eax, r14d
005F7022  41 2B C5                        sub eax, r13d
005F7025  FF C8                           dec eax
005F7027  83 F8 03                        cmp eax, 3
005F702A  72 72                           jb 0x1405f709e
005F702C  48 39 55 D8                     cmp qword ptr [rbp - 0x28], rdx
005F7030  0F 85 35 FE FF FF               jne 0x1405f6e6b
005F7036  48 63 44 24 40                  movsxd rax, dword ptr [rsp + 0x40]
005F703B  49 3B C9                        cmp rcx, r9
005F703E  49 8B D1                        mov rdx, r9
005F7041  48 0F 42 D1                     cmovb rdx, rcx
005F7045  48 3B C2                        cmp rax, rdx
005F7048  73 30                           jae 0x1405f707a
005F704A  41 8B C5                        mov eax, r13d
005F704D  41 8B CE                        mov ecx, r14d
005F7050  48 2B C8                        sub rcx, rax
005F7053  B8 FF FF 00 00                  mov eax, 0xffff
005F7058  49 2B C8                        sub rcx, r8
005F705B  48 03 CF                        add rcx, rdi
005F705E  48 3B C8                        cmp rcx, rax
005F7061  0F 87 21 FE FF FF               ja 0x1405f6e88
005F7067  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
005F706B  41 2B C5                        sub eax, r13d
005F706E  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
005F7072  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
005F7076  48 89 7D E0                     mov qword ptr [rbp - 0x20], rdi
005F707A  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
005F7081  41 0F B7 C5                     movzx eax, r13w
005F7085  0F B7 8C 41 00 00 02 00         movzx ecx, word ptr [rcx + rax*2 + 0x20000]
005F708D  41 3B CD                        cmp ecx, r13d
005F7090  0F 87 F2 FD FF FF               ja 0x1405f6e88
005F7096  44 2B E9                        sub r13d, ecx
005F7099  E9 CD FD FF FF                  jmp 0x1405f6e6b
005F709E  45 8B EE                        mov r13d, r14d
005F70A1  E9 C5 FD FF FF                  jmp 0x1405f6e6b
005F70A6  41 8B C2                        mov eax, r10d
005F70A9  44 89 55 D0                     mov dword ptr [rbp - 0x30], r10d
005F70AD  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
005F70B0  48 8B 5D D0                     mov rbx, qword ptr [rbp - 0x30]
005F70B4  3B C6                           cmp eax, esi
005F70B6  0F 8E 86 04 00 00               jle 0x1405f7542
005F70BC  4C 63 8D C8 00 00 00            movsxd r9, dword ptr [rbp + 0xc8]
005F70C3  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
005F70C7  4B 8D 0C 29                     lea rcx, [r9 + r13]
005F70CB  48 8D 41 03                     lea rax, [rcx + 3]
005F70CF  48 3B D0                        cmp rdx, rax
005F70D2  73 29                           jae 0x1405f70fd
005F70D4  48 3B D1                        cmp rdx, rcx
005F70D7  0F 83 71 02 00 00               jae 0x1405f734e
005F70DD  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
005F70E2  48 8B FB                        mov rdi, rbx
005F70E5  8B 74 24 74                     mov esi, dword ptr [rsp + 0x74]
005F70E9  4C 8B E2                        mov r12, rdx
005F70EC  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
005F70F0  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
005F70F4  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
005F70F8  E9 71 F6 FF FF                  jmp 0x1405f676e
005F70FD  4C 3B E1                        cmp r12, rcx
005F7100  73 73                           jae 0x1405f7175
005F7102  49 8B C4                        mov rax, r12
005F7105  49 2B C5                        sub rax, r13
005F7108  49 3B C3                        cmp rax, r11
005F710B  7D 5B                           jge 0x1405f7168
005F710D  45 3B CB                        cmp r9d, r11d
005F7110  48 63 CE                        movsxd rcx, esi
005F7113  45 0F 4F CB                     cmovg r9d, r11d
005F7117  48 83 C1 FC                     add rcx, -4
005F711B  49 63 C1                        movsxd rax, r9d
005F711E  49 03 CC                        add rcx, r12
005F7121  49 03 C5                        add rax, r13
005F7124  44 89 8D C8 00 00 00            mov dword ptr [rbp + 0xc8], r9d
005F712B  48 3B C1                        cmp rax, rcx
005F712E  76 14                           jbe 0x1405f7144
005F7130  45 8B CC                        mov r9d, r12d
005F7133  45 2B CD                        sub r9d, r13d
005F7136  41 83 C1 FC                     add r9d, -4
005F713A  44 03 CE                        add r9d, esi
005F713D  44 89 8D C8 00 00 00            mov dword ptr [rbp + 0xc8], r9d
005F7144  41 8B CD                        mov ecx, r13d
005F7147  41 2B CC                        sub ecx, r12d
005F714A  41 03 C9                        add ecx, r9d
005F714D  85 C9                           test ecx, ecx
005F714F  7E 24                           jle 0x1405f7175
005F7151  48 63 C1                        movsxd rax, ecx
005F7154  4C 03 E0                        add r12, rax
005F7157  2B F1                           sub esi, ecx
005F7159  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
005F715D  89 74 24 74                     mov dword ptr [rsp + 0x74], esi
005F7161  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
005F7166  EB 0D                           jmp 0x1405f7175
005F7168  45 8B CC                        mov r9d, r12d
005F716B  45 2B CD                        sub r9d, r13d
005F716E  44 89 8D C8 00 00 00            mov dword ptr [rbp + 0xc8], r9d
005F7175  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F7179  BE 01 00 00 00                  mov esi, 1
005F717E  4D 8B E5                        mov r12, r13
005F7181  4D 8B FE                        mov r15, r14
005F7184  4D 8B C6                        mov r8, r14
005F7187  4D 8B D6                        mov r10, r14
005F718A  4C 03 F6                        add r14, rsi
005F718D  4D 2B E3                        sub r12, r11
005F7190  83 BD D0 00 00 00 00            cmp dword ptr [rbp + 0xd0], 0
005F7197  48 B9 81 80 80 80 80 80 80 80   movabs rcx, 0x8080808080808081
005F71A1  74 26                           je 0x1405f71c9
005F71A3  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F71A7  48 8B C1                        mov rax, rcx
005F71AA  49 F7 E4                        mul r12
005F71AD  48 C1 EA 07                     shr rdx, 7
005F71B1  48 8D 42 08                     lea rax, [rdx + 8]
005F71B5  49 03 C4                        add rax, r12
005F71B8  49 03 C6                        add rax, r14
005F71BB  48 3B C6                        cmp rax, rsi
005F71BE  0F 87 AD 08 00 00               ja 0x1405f7a71
005F71C4  BE 01 00 00 00                  mov esi, 1
005F71C9  49 83 FC 0F                     cmp r12, 0xf
005F71CD  72 55                           jb 0x1405f7224
005F71CF  4D 8D 6C 24 F1                  lea r13, [r12 - 0xf]
005F71D4  41 C6 00 F0                     mov byte ptr [r8], 0xf0
005F71D8  49 81 FD FF 00 00 00            cmp r13, 0xff
005F71DF  72 36                           jb 0x1405f7217
005F71E1  48 8B C1                        mov rax, rcx
005F71E4  49 8B CE                        mov rcx, r14
005F71E7  49 F7 E5                        mul r13
005F71EA  48 8B F2                        mov rsi, rdx
005F71ED  B2 FF                           mov dl, 0xff
005F71EF  48 C1 EE 07                     shr rsi, 7
005F71F3  4C 8B C6                        mov r8, rsi
005F71F6  E8 45 FA 0C 00                  call 0x1406c6c40
005F71FB  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F71FF  4C 03 F6                        add r14, rsi
005F7202  48 69 C6 01 FF FF FF            imul rax, rsi, -0xff
005F7209  4D 8B C7                        mov r8, r15
005F720C  4D 8B D7                        mov r10, r15
005F720F  4C 03 E8                        add r13, rax
005F7212  BE 01 00 00 00                  mov esi, 1
005F7217  45 88 2E                        mov byte ptr [r14], r13b
005F721A  4C 03 F6                        add r14, rsi
005F721D  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
005F7222  EB 09                           jmp 0x1405f722d
005F7224  41 8A C4                        mov al, r12b
005F7227  C0 E0 04                        shl al, 4
005F722A  41 88 00                        mov byte ptr [r8], al
005F722D  49 8B D3                        mov rdx, r11
005F7230  4F 8D 0C 34                     lea r9, [r12 + r14]
005F7234  49 2B D6                        sub rdx, r14
005F7237  49 8B CE                        mov rcx, r14
005F723A  48 8B 04 0A                     mov rax, qword ptr [rdx + rcx]
005F723E  48 89 01                        mov qword ptr [rcx], rax
005F7241  48 83 C1 08                     add rcx, 8
005F7245  49 3B C9                        cmp rcx, r9
005F7248  72 F0                           jb 0x1405f723a
005F724A  0F B7 45 A0                     movzx eax, word ptr [rbp - 0x60]
005F724E  4D 03 F4                        add r14, r12
005F7251  4C 63 8D C8 00 00 00            movsxd r9, dword ptr [rbp + 0xc8]
005F7258  49 BC 81 80 80 80 80 80 80 80   movabs r12, 0x8080808080808081
005F7262  66 41 89 06                     mov word ptr [r14], ax
005F7266  49 83 C6 02                     add r14, 2
005F726A  83 BD D0 00 00 00 00            cmp dword ptr [rbp + 0xd0], 0
005F7271  49 8D 49 FC                     lea rcx, [r9 - 4]
005F7275  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
005F7279  74 23                           je 0x1405f729e
005F727B  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F727F  49 8B C4                        mov rax, r12
005F7282  48 F7 E1                        mul rcx
005F7285  48 C1 EA 07                     shr rdx, 7
005F7289  48 8D 42 06                     lea rax, [rdx + 6]
005F728D  49 03 C6                        add rax, r14
005F7290  48 3B C6                        cmp rax, rsi
005F7293  0F 87 D0 07 00 00               ja 0x1405f7a69
005F7299  BE 01 00 00 00                  mov esi, 1
005F729E  41 8A 02                        mov al, byte ptr [r10]
005F72A1  48 83 F9 0F                     cmp rcx, 0xf
005F72A5  72 5C                           jb 0x1405f7303
005F72A7  04 0F                           add al, 0xf
005F72A9  48 83 E9 0F                     sub rcx, 0xf
005F72AD  41 88 00                        mov byte ptr [r8], al
005F72B0  48 81 F9 FE 01 00 00            cmp rcx, 0x1fe
005F72B7  72 27                           jb 0x1405f72e0
005F72B9  49 8B C4                        mov rax, r12
005F72BC  48 F7 E1                        mul rcx
005F72BF  48 C1 EA 08                     shr rdx, 8
005F72C3  48 69 C2 02 FE FF FF            imul rax, rdx, -0x1fe
005F72CA  48 03 C8                        add rcx, rax
005F72CD  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F72D1  4C 03 F6                        add r14, rsi
005F72D4  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F72D8  4C 03 F6                        add r14, rsi
005F72DB  48 2B D6                        sub rdx, rsi
005F72DE  75 ED                           jne 0x1405f72cd
005F72E0  48 81 F9 FF 00 00 00            cmp rcx, 0xff
005F72E7  72 0E                           jb 0x1405f72f7
005F72E9  48 81 E9 FF 00 00 00            sub rcx, 0xff
005F72F0  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F72F4  4C 03 F6                        add r14, rsi
005F72F7  41 88 0E                        mov byte ptr [r14], cl
005F72FA  4C 03 F6                        add r14, rsi
005F72FD  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
005F7301  EB 05                           jmp 0x1405f7308
005F7303  02 C1                           add al, cl
005F7305  41 88 00                        mov byte ptr [r8], al
005F7308  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
005F730C  4D 03 E9                        add r13, r9
005F730F  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
005F7313  4C 8B E0                        mov r12, rax
005F7316  44 8B 4D A4                     mov r9d, dword ptr [rbp - 0x5c]
005F731A  48 8B FB                        mov rdi, rbx
005F731D  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
005F7322  45 33 D2                        xor r10d, r10d
005F7325  8B 74 24 74                     mov esi, dword ptr [rsp + 0x74]
005F7329  4C 89 6D 98                     mov qword ptr [rbp - 0x68], r13
005F732D  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
005F7331  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
005F7335  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
005F7339  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
005F733E  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
005F7342  44 89 8D C8 00 00 00            mov dword ptr [rbp + 0xc8], r9d
005F7349  E9 1A F4 FF FF                  jmp 0x1405f6768
005F734E  4C 3B E1                        cmp r12, rcx
005F7351  73 31                           jae 0x1405f7384
005F7353  41 8B CD                        mov ecx, r13d
005F7356  41 2B CC                        sub ecx, r12d
005F7359  41 03 C9                        add ecx, r9d
005F735C  2B F1                           sub esi, ecx
005F735E  48 63 C1                        movsxd rax, ecx
005F7361  4C 03 E0                        add r12, rax
005F7364  89 74 24 74                     mov dword ptr [rsp + 0x74], esi
005F7368  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
005F736C  83 FE 04                        cmp esi, 4
005F736F  7D 0E                           jge 0x1405f737f
005F7371  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
005F7375  48 8B FB                        mov rdi, rbx
005F7378  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
005F737D  EB 05                           jmp 0x1405f7384
005F737F  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
005F7384  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F7388  BE 01 00 00 00                  mov esi, 1
005F738D  4D 8B E5                        mov r12, r13
005F7390  4D 8B FE                        mov r15, r14
005F7393  4D 8B C6                        mov r8, r14
005F7396  4D 8B D6                        mov r10, r14
005F7399  4C 03 F6                        add r14, rsi
005F739C  4D 2B E3                        sub r12, r11
005F739F  83 BD D0 00 00 00 00            cmp dword ptr [rbp + 0xd0], 0
005F73A6  48 B9 81 80 80 80 80 80 80 80   movabs rcx, 0x8080808080808081
005F73B0  74 26                           je 0x1405f73d8
005F73B2  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F73B6  48 8B C1                        mov rax, rcx
005F73B9  49 F7 E4                        mul r12
005F73BC  48 C1 EA 07                     shr rdx, 7
005F73C0  48 8D 42 08                     lea rax, [rdx + 8]
005F73C4  49 03 C4                        add rax, r12
005F73C7  49 03 C6                        add rax, r14
005F73CA  48 3B C6                        cmp rax, rsi
005F73CD  0F 87 9E 06 00 00               ja 0x1405f7a71
005F73D3  BE 01 00 00 00                  mov esi, 1
005F73D8  49 83 FC 0F                     cmp r12, 0xf
005F73DC  72 55                           jb 0x1405f7433
005F73DE  4D 8D 6C 24 F1                  lea r13, [r12 - 0xf]
005F73E3  41 C6 00 F0                     mov byte ptr [r8], 0xf0
005F73E7  49 81 FD FF 00 00 00            cmp r13, 0xff
005F73EE  72 36                           jb 0x1405f7426
005F73F0  48 8B C1                        mov rax, rcx
005F73F3  49 8B CE                        mov rcx, r14
005F73F6  49 F7 E5                        mul r13
005F73F9  48 8B F2                        mov rsi, rdx
005F73FC  B2 FF                           mov dl, 0xff
005F73FE  48 C1 EE 07                     shr rsi, 7
005F7402  4C 8B C6                        mov r8, rsi
005F7405  E8 36 F8 0C 00                  call 0x1406c6c40
005F740A  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F740E  4C 03 F6                        add r14, rsi
005F7411  48 69 C6 01 FF FF FF            imul rax, rsi, -0xff
005F7418  4D 8B C7                        mov r8, r15
005F741B  4D 8B D7                        mov r10, r15
005F741E  4C 03 E8                        add r13, rax
005F7421  BE 01 00 00 00                  mov esi, 1
005F7426  45 88 2E                        mov byte ptr [r14], r13b
005F7429  4C 03 F6                        add r14, rsi
005F742C  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
005F7431  EB 09                           jmp 0x1405f743c
005F7433  41 8A C4                        mov al, r12b
005F7436  C0 E0 04                        shl al, 4
005F7439  41 88 00                        mov byte ptr [r8], al
005F743C  49 8B D3                        mov rdx, r11
005F743F  4F 8D 0C 34                     lea r9, [r12 + r14]
005F7443  49 2B D6                        sub rdx, r14
005F7446  49 8B CE                        mov rcx, r14
005F7449  48 8B 04 0A                     mov rax, qword ptr [rdx + rcx]
005F744D  48 89 01                        mov qword ptr [rcx], rax
005F7450  48 83 C1 08                     add rcx, 8
005F7454  49 3B C9                        cmp rcx, r9
005F7457  72 F0                           jb 0x1405f7449
005F7459  0F B7 45 A0                     movzx eax, word ptr [rbp - 0x60]
005F745D  4D 03 F4                        add r14, r12
005F7460  4C 63 8D C8 00 00 00            movsxd r9, dword ptr [rbp + 0xc8]
005F7467  49 BC 81 80 80 80 80 80 80 80   movabs r12, 0x8080808080808081
005F7471  66 41 89 06                     mov word ptr [r14], ax
005F7475  49 83 C6 02                     add r14, 2
005F7479  83 BD D0 00 00 00 00            cmp dword ptr [rbp + 0xd0], 0
005F7480  49 8D 49 FC                     lea rcx, [r9 - 4]
005F7484  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
005F7488  74 23                           je 0x1405f74ad
005F748A  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F748E  49 8B C4                        mov rax, r12
005F7491  48 F7 E1                        mul rcx
005F7494  48 C1 EA 07                     shr rdx, 7
005F7498  48 8D 42 06                     lea rax, [rdx + 6]
005F749C  49 03 C6                        add rax, r14
005F749F  48 3B C6                        cmp rax, rsi
005F74A2  0F 87 C1 05 00 00               ja 0x1405f7a69
005F74A8  BE 01 00 00 00                  mov esi, 1
005F74AD  41 8A 02                        mov al, byte ptr [r10]
005F74B0  48 83 F9 0F                     cmp rcx, 0xf
005F74B4  72 5C                           jb 0x1405f7512
005F74B6  04 0F                           add al, 0xf
005F74B8  48 83 E9 0F                     sub rcx, 0xf
005F74BC  41 88 00                        mov byte ptr [r8], al
005F74BF  48 81 F9 FE 01 00 00            cmp rcx, 0x1fe
005F74C6  72 27                           jb 0x1405f74ef
005F74C8  49 8B C4                        mov rax, r12
005F74CB  48 F7 E1                        mul rcx
005F74CE  48 C1 EA 08                     shr rdx, 8
005F74D2  48 69 C2 02 FE FF FF            imul rax, rdx, -0x1fe
005F74D9  48 03 C8                        add rcx, rax
005F74DC  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F74E0  4C 03 F6                        add r14, rsi
005F74E3  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F74E7  4C 03 F6                        add r14, rsi
005F74EA  48 2B D6                        sub rdx, rsi
005F74ED  75 ED                           jne 0x1405f74dc
005F74EF  48 81 F9 FF 00 00 00            cmp rcx, 0xff
005F74F6  72 0E                           jb 0x1405f7506
005F74F8  48 81 E9 FF 00 00 00            sub rcx, 0xff
005F74FF  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F7503  4C 03 F6                        add r14, rsi
005F7506  41 88 0E                        mov byte ptr [r14], cl
005F7509  4C 03 F6                        add r14, rsi
005F750C  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
005F7510  EB 05                           jmp 0x1405f7517
005F7512  02 C1                           add al, cl
005F7514  41 88 00                        mov byte ptr [r8], al
005F7517  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
005F751B  4D 03 E9                        add r13, r9
005F751E  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
005F7522  4C 8B DF                        mov r11, rdi
005F7525  4C 89 6D 98                     mov qword ptr [rbp - 0x68], r13
005F7529  4C 8B E8                        mov r13, rax
005F752C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
005F7531  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
005F7535  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
005F7539  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
005F753D  E9 C5 E8 FF FF                  jmp 0x1405f5e07
005F7542  48 63 85 C8 00 00 00            movsxd rax, dword ptr [rbp + 0xc8]
005F7549  49 03 C5                        add rax, r13
005F754C  4C 3B E0                        cmp r12, rax
005F754F  73 0C                           jae 0x1405f755d
005F7551  41 8B C4                        mov eax, r12d
005F7554  41 2B C5                        sub eax, r13d
005F7557  89 85 C8 00 00 00               mov dword ptr [rbp + 0xc8], eax
005F755D  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
005F7562  4D 8B FE                        mov r15, r14
005F7565  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
005F7569  49 8B F3                        mov rsi, r11
005F756C  4D 8B EE                        mov r13, r14
005F756F  4D 8B CE                        mov r9, r14
005F7572  48 2B F3                        sub rsi, rbx
005F7575  49 FF C6                        inc r14
005F7578  49 B8 81 80 80 80 80 80 80 80   movabs r8, 0x8080808080808081
005F7582  44 39 95 D0 00 00 00            cmp dword ptr [rbp + 0xd0], r10d
005F7589  74 1E                           je 0x1405f75a9
005F758B  49 8B C0                        mov rax, r8
005F758E  48 F7 E6                        mul rsi
005F7591  48 C1 EA 07                     shr rdx, 7
005F7595  48 8D 42 08                     lea rax, [rdx + 8]
005F7599  49 03 C6                        add rax, r14
005F759C  48 03 C6                        add rax, rsi
005F759F  48 3B 45 A8                     cmp rax, qword ptr [rbp - 0x58]
005F75A3  0F 87 B0 04 00 00               ja 0x1405f7a59
005F75A9  48 83 FE 0F                     cmp rsi, 0xf
005F75AD  72 54                           jb 0x1405f7603
005F75AF  4C 8D 66 F1                     lea r12, [rsi - 0xf]
005F75B3  41 C6 45 00 F0                  mov byte ptr [r13], 0xf0
005F75B8  49 81 FC FF 00 00 00            cmp r12, 0xff
005F75BF  72 36                           jb 0x1405f75f7
005F75C1  49 8B C0                        mov rax, r8
005F75C4  49 8B CE                        mov rcx, r14
005F75C7  49 F7 E4                        mul r12
005F75CA  48 8B DA                        mov rbx, rdx
005F75CD  B2 FF                           mov dl, 0xff
005F75CF  48 C1 EB 07                     shr rbx, 7
005F75D3  4C 8B C3                        mov r8, rbx
005F75D6  E8 65 F6 0C 00                  call 0x1406c6c40
005F75DB  4C 8B 5C 24 58                  mov r11, qword ptr [rsp + 0x58]
005F75E0  4C 03 F3                        add r14, rbx
005F75E3  48 69 C3 01 FF FF FF            imul rax, rbx, -0xff
005F75EA  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
005F75EE  4D 8B CD                        mov r9, r13
005F75F1  4C 03 E0                        add r12, rax
005F75F4  45 33 D2                        xor r10d, r10d
005F75F7  45 88 26                        mov byte ptr [r14], r12b
005F75FA  49 FF C6                        inc r14
005F75FD  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
005F7601  EB 0A                           jmp 0x1405f760d
005F7603  40 8A C6                        mov al, sil
005F7606  C0 E0 04                        shl al, 4
005F7609  41 88 45 00                     mov byte ptr [r13], al
005F760D  48 8B D3                        mov rdx, rbx
005F7610  4D 8D 04 36                     lea r8, [r14 + rsi]
005F7614  49 2B D6                        sub rdx, r14
005F7617  49 8B CE                        mov rcx, r14
005F761A  48 8B 04 0A                     mov rax, qword ptr [rdx + rcx]
005F761E  48 89 01                        mov qword ptr [rcx], rax
005F7621  48 83 C1 08                     add rcx, 8
005F7625  49 3B C8                        cmp rcx, r8
005F7628  72 F0                           jb 0x1405f761a
005F762A  0F B7 45 A0                     movzx eax, word ptr [rbp - 0x60]
005F762E  4C 03 F6                        add r14, rsi
005F7631  4C 63 85 C8 00 00 00            movsxd r8, dword ptr [rbp + 0xc8]
005F7638  48 BB 81 80 80 80 80 80 80 80   movabs rbx, 0x8080808080808081
005F7642  66 41 89 06                     mov word ptr [r14], ax
005F7646  49 83 C6 02                     add r14, 2
005F764A  49 8D 48 FC                     lea rcx, [r8 - 4]
005F764E  44 39 95 D0 00 00 00            cmp dword ptr [rbp + 0xd0], r10d
005F7655  74 1E                           je 0x1405f7675
005F7657  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F765B  48 8B C3                        mov rax, rbx
005F765E  48 F7 E1                        mul rcx
005F7661  48 C1 EA 07                     shr rdx, 7
005F7665  48 8D 42 06                     lea rax, [rdx + 6]
005F7669  49 03 C6                        add rax, r14
005F766C  48 3B C6                        cmp rax, rsi
005F766F  0F 87 D7 03 00 00               ja 0x1405f7a4c
005F7675  41 8A 01                        mov al, byte ptr [r9]
005F7678  48 83 F9 0F                     cmp rcx, 0xf
005F767C  72 65                           jb 0x1405f76e3
005F767E  04 0F                           add al, 0xf
005F7680  48 83 E9 0F                     sub rcx, 0xf
005F7684  41 88 45 00                     mov byte ptr [r13], al
005F7688  48 81 F9 FE 01 00 00            cmp rcx, 0x1fe
005F768F  72 2E                           jb 0x1405f76bf
005F7691  48 8B C3                        mov rax, rbx
005F7694  BB 01 00 00 00                  mov ebx, 1
005F7699  48 F7 E1                        mul rcx
005F769C  48 C1 EA 08                     shr rdx, 8
005F76A0  48 69 C2 02 FE FF FF            imul rax, rdx, -0x1fe
005F76A7  48 03 C8                        add rcx, rax
005F76AA  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F76AE  4C 03 F3                        add r14, rbx
005F76B1  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F76B5  4C 03 F3                        add r14, rbx
005F76B8  48 2B D3                        sub rdx, rbx
005F76BB  75 ED                           jne 0x1405f76aa
005F76BD  EB 05                           jmp 0x1405f76c4
005F76BF  BB 01 00 00 00                  mov ebx, 1
005F76C4  48 81 F9 FF 00 00 00            cmp rcx, 0xff
005F76CB  72 0E                           jb 0x1405f76db
005F76CD  48 81 E9 FF 00 00 00            sub rcx, 0xff
005F76D4  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F76D8  4C 03 F3                        add r14, rbx
005F76DB  41 88 0E                        mov byte ptr [r14], cl
005F76DE  4C 03 F3                        add r14, rbx
005F76E1  EB 0B                           jmp 0x1405f76ee
005F76E3  02 C8                           add cl, al
005F76E5  BB 01 00 00 00                  mov ebx, 1
005F76EA  41 88 4D 00                     mov byte ptr [r13], cl
005F76EE  4D 03 D8                        add r11, r8
005F76F1  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
005F76F6  49 8B F4                        mov rsi, r12
005F76F9  4C 89 5D 98                     mov qword ptr [rbp - 0x68], r11
005F76FD  4D 8B FE                        mov r15, r14
005F7700  4D 8B EE                        mov r13, r14
005F7703  4D 8B CE                        mov r9, r14
005F7706  49 2B F3                        sub rsi, r11
005F7709  4C 03 F3                        add r14, rbx
005F770C  49 B8 81 80 80 80 80 80 80 80   movabs r8, 0x8080808080808081
005F7716  44 39 95 D0 00 00 00            cmp dword ptr [rbp + 0xd0], r10d
005F771D  74 1E                           je 0x1405f773d
005F771F  49 8B C0                        mov rax, r8
005F7722  48 F7 E6                        mul rsi
005F7725  48 C1 EA 07                     shr rdx, 7
005F7729  48 8D 42 08                     lea rax, [rdx + 8]
005F772D  48 03 C6                        add rax, rsi
005F7730  49 03 C6                        add rax, r14
005F7733  48 3B 45 A8                     cmp rax, qword ptr [rbp - 0x58]
005F7737  0F 87 F1 02 00 00               ja 0x1405f7a2e
005F773D  48 83 FE 0F                     cmp rsi, 0xf
005F7741  72 53                           jb 0x1405f7796
005F7743  4C 8D 66 F1                     lea r12, [rsi - 0xf]
005F7747  41 C6 45 00 F0                  mov byte ptr [r13], 0xf0
005F774C  49 81 FC FF 00 00 00            cmp r12, 0xff
005F7753  72 35                           jb 0x1405f778a
005F7755  49 8B C0                        mov rax, r8
005F7758  49 8B CE                        mov rcx, r14
005F775B  49 F7 E4                        mul r12
005F775E  48 8B DA                        mov rbx, rdx
005F7761  B2 FF                           mov dl, 0xff
005F7763  48 C1 EB 07                     shr rbx, 7
005F7767  4C 8B C3                        mov r8, rbx
005F776A  E8 D1 F4 0C 00                  call 0x1406c6c40
005F776F  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F7773  4C 03 F3                        add r14, rbx
005F7776  48 69 C3 01 FF FF FF            imul rax, rbx, -0xff
005F777D  4D 8B CD                        mov r9, r13
005F7780  4C 03 E0                        add r12, rax
005F7783  45 33 D2                        xor r10d, r10d
005F7786  41 8D 5A 01                     lea ebx, [r10 + 1]
005F778A  45 88 26                        mov byte ptr [r14], r12b
005F778D  4C 03 F3                        add r14, rbx
005F7790  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
005F7794  EB 0A                           jmp 0x1405f77a0
005F7796  40 8A C6                        mov al, sil
005F7799  C0 E0 04                        shl al, 4
005F779C  41 88 45 00                     mov byte ptr [r13], al
005F77A0  49 8B D3                        mov rdx, r11
005F77A3  4E 8D 04 36                     lea r8, [rsi + r14]
005F77A7  49 2B D6                        sub rdx, r14
005F77AA  49 8B CE                        mov rcx, r14
005F77AD  48 8B 04 0A                     mov rax, qword ptr [rdx + rcx]
005F77B1  48 89 01                        mov qword ptr [rcx], rax
005F77B4  48 83 C1 08                     add rcx, 8
005F77B8  49 3B C8                        cmp rcx, r8
005F77BB  72 F0                           jb 0x1405f77ad
005F77BD  0F B7 44 24 70                  movzx eax, word ptr [rsp + 0x70]
005F77C2  4C 03 F6                        add r14, rsi
005F77C5  4C 63 44 24 74                  movsxd r8, dword ptr [rsp + 0x74]
005F77CA  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F77CE  66 41 89 06                     mov word ptr [r14], ax
005F77D2  49 83 C6 02                     add r14, 2
005F77D6  49 8D 48 FC                     lea rcx, [r8 - 4]
005F77DA  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
005F77DE  44 39 95 D0 00 00 00            cmp dword ptr [rbp + 0xd0], r10d
005F77E5  74 21                           je 0x1405f7808
005F77E7  48 B8 81 80 80 80 80 80 80 80   movabs rax, 0x8080808080808081
005F77F1  48 F7 E1                        mul rcx
005F77F4  48 C1 EA 07                     shr rdx, 7
005F77F8  48 8D 42 06                     lea rax, [rdx + 6]
005F77FC  49 03 C6                        add rax, r14
005F77FF  48 3B C6                        cmp rax, rsi
005F7802  0F 87 30 02 00 00               ja 0x1405f7a38
005F7808  41 8A 01                        mov al, byte ptr [r9]
005F780B  48 83 F9 0F                     cmp rcx, 0xf
005F780F  72 64                           jb 0x1405f7875
005F7811  04 0F                           add al, 0xf
005F7813  48 83 E9 0F                     sub rcx, 0xf
005F7817  41 88 45 00                     mov byte ptr [r13], al
005F781B  48 81 F9 FE 01 00 00            cmp rcx, 0x1fe
005F7822  72 2E                           jb 0x1405f7852
005F7824  48 B8 81 80 80 80 80 80 80 80   movabs rax, 0x8080808080808081
005F782E  48 F7 E1                        mul rcx
005F7831  48 C1 EA 08                     shr rdx, 8
005F7835  48 69 C2 02 FE FF FF            imul rax, rdx, -0x1fe
005F783C  48 03 C8                        add rcx, rax
005F783F  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F7843  4C 03 F3                        add r14, rbx
005F7846  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F784A  4C 03 F3                        add r14, rbx
005F784D  48 2B D3                        sub rdx, rbx
005F7850  75 ED                           jne 0x1405f783f
005F7852  48 81 F9 FF 00 00 00            cmp rcx, 0xff
005F7859  72 0E                           jb 0x1405f7869
005F785B  48 81 E9 FF 00 00 00            sub rcx, 0xff
005F7862  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F7866  4C 03 F3                        add r14, rbx
005F7869  41 88 0E                        mov byte ptr [r14], cl
005F786C  4C 03 F3                        add r14, rbx
005F786F  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
005F7873  EB 06                           jmp 0x1405f787b
005F7875  02 C8                           add cl, al
005F7877  41 88 4D 00                     mov byte ptr [r13], cl
005F787B  4B 8D 3C 04                     lea rdi, [r12 + r8]
005F787F  E9 97 01 00 00                  jmp 0x1405f7a1b
005F7884  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
005F7889  BB 01 00 00 00                  mov ebx, 1
005F788E  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F7892  48 8B F9                        mov rdi, rcx
005F7895  4D 8B FE                        mov r15, r14
005F7898  4D 8B E6                        mov r12, r14
005F789B  4D 8B EE                        mov r13, r14
005F789E  49 2B FB                        sub rdi, r11
005F78A1  4C 03 F3                        add r14, rbx
005F78A4  49 B8 81 80 80 80 80 80 80 80   movabs r8, 0x8080808080808081
005F78AE  44 39 95 D0 00 00 00            cmp dword ptr [rbp + 0xd0], r10d
005F78B5  74 21                           je 0x1405f78d8
005F78B7  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F78BB  49 8B C0                        mov rax, r8
005F78BE  48 F7 E7                        mul rdi
005F78C1  48 8D 47 08                     lea rax, [rdi + 8]
005F78C5  48 C1 EA 07                     shr rdx, 7
005F78C9  48 03 C2                        add rax, rdx
005F78CC  49 03 C6                        add rax, r14
005F78CF  48 3B C6                        cmp rax, rsi
005F78D2  0F 87 B0 01 00 00               ja 0x1405f7a88
005F78D8  48 83 FF 0F                     cmp rdi, 0xf
005F78DC  72 53                           jb 0x1405f7931
005F78DE  48 8D 77 F1                     lea rsi, [rdi - 0xf]
005F78E2  41 C6 04 24 F0                  mov byte ptr [r12], 0xf0
005F78E7  48 81 FE FF 00 00 00            cmp rsi, 0xff
005F78EE  72 39                           jb 0x1405f7929
005F78F0  49 8B C0                        mov rax, r8
005F78F3  49 8B CE                        mov rcx, r14
005F78F6  48 F7 E6                        mul rsi
005F78F9  48 8B DA                        mov rbx, rdx
005F78FC  B2 FF                           mov dl, 0xff
005F78FE  48 C1 EB 07                     shr rbx, 7
005F7902  4C 8B C3                        mov r8, rbx
005F7905  E8 36 F3 0C 00                  call 0x1406c6c40
005F790A  44 8B 8D C8 00 00 00            mov r9d, dword ptr [rbp + 0xc8]
005F7911  4C 03 F3                        add r14, rbx
005F7914  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F7918  48 69 C3 01 FF FF FF            imul rax, rbx, -0xff
005F791F  48 03 F0                        add rsi, rax
005F7922  45 33 D2                        xor r10d, r10d
005F7925  41 8D 5A 01                     lea ebx, [r10 + 1]
005F7929  41 88 36                        mov byte ptr [r14], sil
005F792C  4C 03 F3                        add r14, rbx
005F792F  EB 0A                           jmp 0x1405f793b
005F7931  40 8A C7                        mov al, dil
005F7934  C0 E0 04                        shl al, 4
005F7937  41 88 04 24                     mov byte ptr [r12], al
005F793B  49 8B D3                        mov rdx, r11
005F793E  4E 8D 04 37                     lea r8, [rdi + r14]
005F7942  49 2B D6                        sub rdx, r14
005F7945  49 8B CE                        mov rcx, r14
005F7948  48 8B 04 0A                     mov rax, qword ptr [rdx + rcx]
005F794C  48 89 01                        mov qword ptr [rcx], rax
005F794F  48 83 C1 08                     add rcx, 8
005F7953  49 3B C8                        cmp rcx, r8
005F7956  72 F0                           jb 0x1405f7948
005F7958  0F B7 45 A0                     movzx eax, word ptr [rbp - 0x60]
005F795C  4C 03 F7                        add r14, rdi
005F795F  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F7963  49 B8 81 80 80 80 80 80 80 80   movabs r8, 0x8080808080808081
005F796D  49 63 C9                        movsxd rcx, r9d
005F7970  48 83 E9 04                     sub rcx, 4
005F7974  66 41 89 06                     mov word ptr [r14], ax
005F7978  49 83 C6 02                     add r14, 2
005F797C  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
005F7980  44 39 95 D0 00 00 00            cmp dword ptr [rbp + 0xd0], r10d
005F7987  74 1A                           je 0x1405f79a3
005F7989  49 8B C0                        mov rax, r8
005F798C  48 F7 E1                        mul rcx
005F798F  48 C1 EA 07                     shr rdx, 7
005F7993  48 8D 42 06                     lea rax, [rdx + 6]
005F7997  49 03 C6                        add rax, r14
005F799A  48 3B C6                        cmp rax, rsi
005F799D  0F 87 E0 00 00 00               ja 0x1405f7a83
005F79A3  41 8A 45 00                     mov al, byte ptr [r13]
005F79A7  48 83 F9 0F                     cmp rcx, 0xf
005F79AB  72 5D                           jb 0x1405f7a0a
005F79AD  04 0F                           add al, 0xf
005F79AF  48 83 E9 0F                     sub rcx, 0xf
005F79B3  41 88 04 24                     mov byte ptr [r12], al
005F79B7  48 81 F9 FE 01 00 00            cmp rcx, 0x1fe
005F79BE  72 27                           jb 0x1405f79e7
005F79C0  49 8B C0                        mov rax, r8
005F79C3  48 F7 E1                        mul rcx
005F79C6  48 C1 EA 08                     shr rdx, 8
005F79CA  48 69 C2 02 FE FF FF            imul rax, rdx, -0x1fe
005F79D1  48 03 C8                        add rcx, rax
005F79D4  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F79D8  4C 03 F3                        add r14, rbx
005F79DB  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F79DF  4C 03 F3                        add r14, rbx
005F79E2  48 2B D3                        sub rdx, rbx
005F79E5  75 ED                           jne 0x1405f79d4
005F79E7  48 81 F9 FF 00 00 00            cmp rcx, 0xff
005F79EE  72 0E                           jb 0x1405f79fe
005F79F0  48 81 E9 FF 00 00 00            sub rcx, 0xff
005F79F7  41 C6 06 FF                     mov byte ptr [r14], 0xff
005F79FB  4C 03 F3                        add r14, rbx
005F79FE  41 88 0E                        mov byte ptr [r14], cl
005F7A01  4C 03 F3                        add r14, rbx
005F7A04  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
005F7A08  EB 06                           jmp 0x1405f7a10
005F7A0A  02 C1                           add al, cl
005F7A0C  41 88 04 24                     mov byte ptr [r12], al
005F7A10  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
005F7A15  49 63 C1                        movsxd rax, r9d
005F7A18  48 03 F8                        add rdi, rax
005F7A1B  4C 8B 8D A0 00 00 00            mov r9, qword ptr [rbp + 0xa0]
005F7A22  4C 8B DF                        mov r11, rdi
005F7A25  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
005F7A29  E9 04 E2 FF FF                  jmp 0x1405f5c32
005F7A2E  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F7A32  4C 89 5D 98                     mov qword ptr [rbp - 0x68], r11
005F7A36  EB 0A                           jmp 0x1405f7a42
005F7A38  49 B8 81 80 80 80 80 80 80 80   movabs r8, 0x8080808080808081
005F7A42  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
005F7A46  44 8B 4D A4                     mov r9d, dword ptr [rbp - 0x5c]
005F7A4A  EB 37                           jmp 0x1405f7a83
005F7A4C  44 8B 8D C8 00 00 00            mov r9d, dword ptr [rbp + 0xc8]
005F7A53  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F7A57  EB 1B                           jmp 0x1405f7a74
005F7A59  44 8B 8D C8 00 00 00            mov r9d, dword ptr [rbp + 0xc8]
005F7A60  4C 8B DB                        mov r11, rbx
005F7A63  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F7A67  EB 15                           jmp 0x1405f7a7e
005F7A69  45 33 D2                        xor r10d, r10d
005F7A6C  4D 8B C4                        mov r8, r12
005F7A6F  EB 0D                           jmp 0x1405f7a7e
005F7A71  45 33 D2                        xor r10d, r10d
005F7A74  49 B8 81 80 80 80 80 80 80 80   movabs r8, 0x8080808080808081
005F7A7E  BB 01 00 00 00                  mov ebx, 1
005F7A83  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
005F7A88  83 BD D0 00 00 00 02            cmp dword ptr [rbp + 0xd0], 2
005F7A8F  0F 85 D1 01 00 00               jne 0x1405f7c66
005F7A95  48 8B F9                        mov rdi, rcx
005F7A98  49 8B C0                        mov rax, r8
005F7A9B  49 2B FB                        sub rdi, r11
005F7A9E  4D 8B F7                        mov r14, r15
005F7AA1  48 8D 8F F0 00 00 00            lea rcx, [rdi + 0xf0]
005F7AA8  48 F7 E1                        mul rcx
005F7AAB  4C 8D 47 01                     lea r8, [rdi + 1]
005F7AAF  48 C1 EA 07                     shr rdx, 7
005F7AB3  48 8D 4E FD                     lea rcx, [rsi - 3]
005F7AB7  4C 03 C2                        add r8, rdx
005F7ABA  4B 8D 04 38                     lea rax, [r8 + r15]
005F7ABE  48 3B C1                        cmp rax, rcx
005F7AC1  0F 87 4E 01 00 00               ja 0x1405f7c15
005F7AC7  49 2B C8                        sub rcx, r8
005F7ACA  49 63 C1                        movsxd rax, r9d
005F7ACD  49 2B CF                        sub rcx, r15
005F7AD0  48 69 C9 FF 00 00 00            imul rcx, rcx, 0xff
005F7AD7  48 83 C1 12                     add rcx, 0x12
005F7ADB  48 3B C1                        cmp rax, rcx
005F7ADE  44 0F 47 C9                     cmova r9d, ecx
005F7AE2  49 63 C1                        movsxd rax, r9d
005F7AE5  49 2B C0                        sub rax, r8
005F7AE8  44 89 8D C8 00 00 00            mov dword ptr [rbp + 0xc8], r9d
005F7AEF  49 2B C7                        sub rax, r15
005F7AF2  48 83 C0 02                     add rax, 2
005F7AF6  48 03 C6                        add rax, rsi
005F7AF9  48 83 F8 0C                     cmp rax, 0xc
005F7AFD  0F 8C 12 01 00 00               jl 0x1405f7c15
005F7B03  4D 8D 77 01                     lea r14, [r15 + 1]
005F7B07  41 BC FF 00 00 00               mov r12d, 0xff
005F7B0D  48 83 FF 0F                     cmp rdi, 0xf
005F7B11  72 58                           jb 0x1405f7b6b
005F7B13  48 8D 77 F1                     lea rsi, [rdi - 0xf]
005F7B17  41 C6 07 F0                     mov byte ptr [r15], 0xf0
005F7B1B  49 3B F4                        cmp rsi, r12
005F7B1E  72 3F                           jb 0x1405f7b5f
005F7B20  48 B8 81 80 80 80 80 80 80 80   movabs rax, 0x8080808080808081
005F7B2A  49 8B CE                        mov rcx, r14
005F7B2D  48 F7 E6                        mul rsi
005F7B30  48 8B DA                        mov rbx, rdx
005F7B33  41 8A D4                        mov dl, r12b
005F7B36  48 C1 EB 07                     shr rbx, 7
005F7B3A  4C 8B C3                        mov r8, rbx
005F7B3D  E8 FE F0 0C 00                  call 0x1406c6c40
005F7B42  44 8B 8D C8 00 00 00            mov r9d, dword ptr [rbp + 0xc8]
005F7B49  4C 03 F3                        add r14, rbx
005F7B4C  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F7B50  48 69 C3 01 FF FF FF            imul rax, rbx, -0xff
005F7B57  BB 01 00 00 00                  mov ebx, 1
005F7B5C  48 03 F0                        add rsi, rax
005F7B5F  41 88 36                        mov byte ptr [r14], sil
005F7B62  4C 03 F3                        add r14, rbx
005F7B65  48 8B 75 A8                     mov rsi, qword ptr [rbp - 0x58]
005F7B69  EB 09                           jmp 0x1405f7b74
005F7B6B  40 8A C7                        mov al, dil
005F7B6E  C0 E0 04                        shl al, 4
005F7B71  41 88 07                        mov byte ptr [r15], al
005F7B74  49 8B CE                        mov rcx, r14
005F7B77  4A 8D 14 37                     lea rdx, [rdi + r14]
005F7B7B  4D 2B DE                        sub r11, r14
005F7B7E  4A 8B 04 19                     mov rax, qword ptr [rcx + r11]
005F7B82  48 89 01                        mov qword ptr [rcx], rax
005F7B85  48 83 C1 08                     add rcx, 8
005F7B89  48 3B CA                        cmp rcx, rdx
005F7B8C  72 F0                           jb 0x1405f7b7e
005F7B8E  0F B7 45 A0                     movzx eax, word ptr [rbp - 0x60]
005F7B92  4C 03 F7                        add r14, rdi
005F7B95  49 63 C9                        movsxd rcx, r9d
005F7B98  48 83 E9 04                     sub rcx, 4
005F7B9C  66 41 89 06                     mov word ptr [r14], ax
005F7BA0  49 83 C6 02                     add r14, 2
005F7BA4  41 8A 07                        mov al, byte ptr [r15]
005F7BA7  48 83 F9 0F                     cmp rcx, 0xf
005F7BAB  72 54                           jb 0x1405f7c01
005F7BAD  04 0F                           add al, 0xf
005F7BAF  48 83 E9 0F                     sub rcx, 0xf
005F7BB3  41 88 07                        mov byte ptr [r15], al
005F7BB6  48 81 F9 FE 01 00 00            cmp rcx, 0x1fe
005F7BBD  72 2C                           jb 0x1405f7beb
005F7BBF  48 B8 81 80 80 80 80 80 80 80   movabs rax, 0x8080808080808081
005F7BC9  48 F7 E1                        mul rcx
005F7BCC  48 C1 EA 08                     shr rdx, 8
005F7BD0  48 69 C2 02 FE FF FF            imul rax, rdx, -0x1fe
005F7BD7  48 03 C8                        add rcx, rax
005F7BDA  45 88 26                        mov byte ptr [r14], r12b
005F7BDD  4C 03 F3                        add r14, rbx
005F7BE0  45 88 26                        mov byte ptr [r14], r12b
005F7BE3  4C 03 F3                        add r14, rbx
005F7BE6  48 2B D3                        sub rdx, rbx
005F7BE9  75 EF                           jne 0x1405f7bda
005F7BEB  49 3B CC                        cmp rcx, r12
005F7BEE  72 09                           jb 0x1405f7bf9
005F7BF0  49 2B CC                        sub rcx, r12
005F7BF3  45 88 26                        mov byte ptr [r14], r12b
005F7BF6  4C 03 F3                        add r14, rbx
005F7BF9  41 88 0E                        mov byte ptr [r14], cl
005F7BFC  4C 03 F3                        add r14, rbx
005F7BFF  EB 05                           jmp 0x1405f7c06
005F7C01  02 C1                           add al, cl
005F7C03  41 88 07                        mov byte ptr [r15], al
005F7C06  4D 63 D9                        movsxd r11, r9d
005F7C09  4C 03 5C 24 58                  add r11, qword ptr [rsp + 0x58]
005F7C0E  4C 89 5D 98                     mov qword ptr [rbp - 0x68], r11
005F7C12  45 33 D2                        xor r10d, r10d
005F7C15  4C 8B AD B0 00 00 00            mov r13, qword ptr [rbp + 0xb0]
005F7C1C  4C 8B A5 A8 00 00 00            mov r12, qword ptr [rbp + 0xa8]
005F7C23  4C 8B BD B8 00 00 00            mov r15, qword ptr [rbp + 0xb8]
005F7C2A  48 8B 5D 00                     mov rbx, qword ptr [rbp]
005F7C2E  49 2B DB                        sub rbx, r11
005F7C31  49 B9 81 80 80 80 80 80 80 80   movabs r9, 0x8080808080808081
005F7C3B  49 8B C1                        mov rax, r9
005F7C3E  48 89 5D 00                     mov qword ptr [rbp], rbx
005F7C42  4D 8B C6                        mov r8, r14
005F7C45  48 8D 8B F0 00 00 00            lea rcx, [rbx + 0xf0]
005F7C4C  48 F7 E1                        mul rcx
005F7C4F  48 8D 43 01                     lea rax, [rbx + 1]
005F7C53  48 C1 EA 07                     shr rdx, 7
005F7C57  83 BD D0 00 00 00 02            cmp dword ptr [rbp + 0xd0], 2
005F7C5E  75 0E                           jne 0x1405f7c6e
005F7C60  48 83 C6 05                     add rsi, 5
005F7C64  EB 11                           jmp 0x1405f7c77
005F7C66  45 8B F2                        mov r14d, r10d
005F7C69  E9 CE 00 00 00                  jmp 0x1405f7d3c
005F7C6E  44 39 95 D0 00 00 00            cmp dword ptr [rbp + 0xd0], r10d
005F7C75  74 3D                           je 0x1405f7cb4
005F7C77  48 03 C2                        add rax, rdx
005F7C7A  B9 01 00 00 00                  mov ecx, 1
005F7C7F  49 03 C6                        add rax, r14
005F7C82  48 3B C6                        cmp rax, rsi
005F7C85  76 32                           jbe 0x1405f7cb9
005F7C87  39 8D D0 00 00 00               cmp dword ptr [rbp + 0xd0], ecx
005F7C8D  75 08                           jne 0x1405f7c97
005F7C8F  45 8B F2                        mov r14d, r10d
005F7C92  E9 AA 00 00 00                  jmp 0x1405f7d41
005F7C97  48 8B DE                        mov rbx, rsi
005F7C9A  49 2B DE                        sub rbx, r14
005F7C9D  48 2B D9                        sub rbx, rcx
005F7CA0  48 8D 83 F1 00 00 00            lea rax, [rbx + 0xf1]
005F7CA7  48 C1 E8 08                     shr rax, 8
005F7CAB  48 2B D8                        sub rbx, rax
005F7CAE  48 89 5D 00                     mov qword ptr [rbp], rbx
005F7CB2  EB 05                           jmp 0x1405f7cb9
005F7CB4  B9 01 00 00 00                  mov ecx, 1
005F7CB9  4A 8D 34 1B                     lea rsi, [rbx + r11]
005F7CBD  48 83 FB 0F                     cmp rbx, 0xf
005F7CC1  72 4E                           jb 0x1405f7d11
005F7CC3  41 C6 06 F0                     mov byte ptr [r14], 0xf0
005F7CC7  48 8D 7B F1                     lea rdi, [rbx - 0xf]
005F7CCB  4C 03 F1                        add r14, rcx
005F7CCE  48 81 FF FF 00 00 00            cmp rdi, 0xff
005F7CD5  72 2F                           jb 0x1405f7d06
005F7CD7  49 8B C1                        mov rax, r9
005F7CDA  49 8B CE                        mov rcx, r14
005F7CDD  48 F7 E7                        mul rdi
005F7CE0  48 8B DA                        mov rbx, rdx
005F7CE3  B2 FF                           mov dl, 0xff
005F7CE5  48 C1 EB 07                     shr rbx, 7
005F7CE9  4C 8B C3                        mov r8, rbx
005F7CEC  E8 4F EF 0C 00                  call 0x1406c6c40
005F7CF1  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
005F7CF5  4C 03 F3                        add r14, rbx
005F7CF8  48 69 C3 01 FF FF FF            imul rax, rbx, -0xff
005F7CFF  48 8B 5D 00                     mov rbx, qword ptr [rbp]
005F7D03  48 03 F8                        add rdi, rax
005F7D06  4D 8B C6                        mov r8, r14
005F7D09  41 88 3E                        mov byte ptr [r14], dil
005F7D0C  49 FF C6                        inc r14
005F7D0F  EB 0B                           jmp 0x1405f7d1c
005F7D11  8A C3                           mov al, bl
005F7D13  C0 E0 04                        shl al, 4
005F7D16  41 88 06                        mov byte ptr [r14], al
005F7D19  4C 03 F1                        add r14, rcx
005F7D1C  49 8D 48 01                     lea rcx, [r8 + 1]
005F7D20  49 8B D3                        mov rdx, r11
005F7D23  4C 8B C3                        mov r8, rbx
005F7D26  E8 15 EB 0C 00                  call 0x1406c6840
005F7D2B  45 2B F5                        sub r14d, r13d
005F7D2E  41 2B F4                        sub esi, r12d
005F7D31  44 03 F3                        add r14d, ebx
005F7D34  41 89 37                        mov dword ptr [r15], esi
005F7D37  45 85 F6                        test r14d, r14d
005F7D3A  7F 12                           jg 0x1405f7d4e
005F7D3C  B9 01 00 00 00                  mov ecx, 1
005F7D41  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
005F7D48  88 88 27 00 04 00               mov byte ptr [rax + 0x40027], cl
005F7D4E  45 8B D6                        mov r10d, r14d
005F7D51  41 8B C2                        mov eax, r10d
005F7D54  EB 23                           jmp 0x1405f7d79
005F7D56  8B 85 D0 00 00 00               mov eax, dword ptr [rbp + 0xd0]
005F7D5C  4D 8B CF                        mov r9, r15
005F7D5F  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
005F7D66  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005F7D6A  8B 85 C0 00 00 00               mov eax, dword ptr [rbp + 0xc0]
005F7D70  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
005F7D74  E8 1B 00 00 00                  call 0x1405f7d94
005F7D79  48 81 C4 58 01 00 00            add rsp, 0x158
005F7D80  41 5F                           pop r15
005F7D82  41 5E                           pop r14
005F7D84  41 5D                           pop r13
005F7D86  41 5C                           pop r12
005F7D88  5F                              pop rdi
005F7D89  5E                              pop rsi
005F7D8A  5B                              pop rbx
005F7D8B  5D                              pop rbp
005F7D8C  C3                              ret
005F7D8D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LZ4HC_compress_generic(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m124;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned int v_stack_m168;
    unsigned int v_stack_m178;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (344);
    v_r10 = 0;
    if ((*(unsigned __int64 *)(a1 + 262184)) != 0) goto loc_005F7D56;
    if (a7 != 2) goto loc_005F56AC;
    if (a5 < ((unsigned int)(v_r10 + 1))) goto loc_005F7D51;
loc_005F56AC:
    if (((unsigned int)((int)(*(unsigned int *)(a4)))) > 0x7E000000ULL) goto loc_005F7D51;
    a1 = ((int)(a5)) + (a3);
    result = (*(unsigned __int64 *)(v_rip - 6025967)) >> (32);
    v_stack_m80 = result;
    v_rsi = a1 - 5;
    if (a7 != 2) { v_rsi = a1; }
    v_stack_m78 = v_xmm0;
    v_stack_mF0 = v_rsi;
    v_stack_m140 = a2;
    v_stack_m100 = a2;
    v_stack_m98 = a2 + (int)(*(unsigned int *)(a4)) * 1;
    v_stack_mA8 = a2 + (int)(*(unsigned int *)(a4)) * 1 - 12;
    v_stack_m138 = a2 + (int)(*(unsigned int *)(a4)) * 1 - 5;
    v_stack_mD0 = a3;
    v_stack_m118 = 0;
    v_stack_mB8 = 0;
    *(unsigned int *)(a4) = 0;
    if (((unsigned int)((int)(*(unsigned int *)(a4)))) < 13) goto loc_005F7C2E;
loc_005F5740:
    if (a2 > (a2 + (int)(*(unsigned int *)(a4)) * 1 - 12)) goto loc_005F7C15;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(*(unsigned __int64 *)(a1 + 262152))));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168)))));
    v_stack_m150 = 3;
    v_stack_mE8 = *(unsigned __int64 *)(a1 + 262152);
    v_stack_m120 = (unsigned int)(v_r15);
    v_stack_m130 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262172)));
    v_rbx = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262172))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262172)) + 65536)) <= ((unsigned int)(v_r15))) {
        v_rbx = v_r15 - 65535;
    }
    a4 = ((unsigned int)(*(unsigned int *)(a1 + 262168))) - ((unsigned int)(*(unsigned int *)(a1 + 262172)));
    a4 = (a4) + (*(unsigned __int64 *)(a1 + 262160));
    v_stack_m108 = (unsigned int)((unsigned int)(v_stack_m74));
    v_stack_mC0 = a4;
    v_stack_mE0 = *(unsigned __int64 *)(a1 + 262160);
    v_stack_m158 = (unsigned int)(v_rbx);
    v_stack_p30 = 0;
    v_stack_mF8 = 0;
    v_stack_m110 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176)))) >= ((unsigned int)(v_r15))) goto loc_005F5835;
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))))) - ((unsigned int)(*(unsigned int *)(a1 + 262168)));
    a3 = (a3) + (*(unsigned __int64 *)(a1 + 262152));
loc_005F57F1:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 262172))) * (*(unsigned int *)(a3)));
    a2 = (a2) >> (17);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))))) - (*(unsigned int *)(v_stack_p8 + a2 * 4)));
    if (a1 > ((unsigned int)(0xFFFFULL))) { a1 = (unsigned int)(0xFFFFULL); }
    a3 = (a3) + (1);
    *(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))) * 2 + 131072) = (unsigned __int16)(a1);
    *(unsigned int *)(v_stack_p8 + a2 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176)));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))) + (1));
    if (((unsigned int)(a4)) < ((unsigned int)(v_r15))) goto loc_005F57F1;
loc_005F5835:
    *(unsigned int *)(v_stack_p8 + 262176) = (unsigned int)(v_r15);
    a1 = (unsigned int)((a1) * (*(unsigned int *)(a2)));
    a1 = (a1) >> (17);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))) < ((unsigned int)((unsigned int)(v_stack_m158)))) goto loc_005F5C01;
loc_005F585E:
    a4 = 0;
    if (condition_is_less_or_equal) goto loc_005F5BED;
    result = (unsigned int)(((unsigned int)(v_stack_m108)) - 1);
    v_stack_m108 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168))))) goto loc_005F59F4;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168)))));
    a2 = (a2) + (v_stack_mE8);
    if ((*(unsigned __int16 *)((int)((unsigned int)((unsigned int)(v_stack_m150))) + v_stack_m140 * 1 - 1)) != ((unsigned __int16)(*(unsigned __int16 *)((int)((unsigned int)((unsigned int)(v_stack_m150))) + a2 * 1 - 1)))) goto loc_005F5964;
    if ((*(unsigned int *)(a2)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_005F5964;
    v_r10 = (v_stack_m140) + (4);
    a2 = (a2) + (4);
    if (v_r10 >= (v_stack_m138 - 7)) goto loc_005F58D9;
    a3 = (*(unsigned __int64 *)(v_r10)) ^ (*(unsigned __int64 *)(a2));
    if (condition_is_not_equal) goto loc_005F58CF;
    goto loc_005F58EA;
loc_005F58CF:
    a1 = (unsigned int)((v_r10 + 8) >> (3));
    goto loc_005F5940;
loc_005F58D9:
    if (a1 >= (v_stack_m138 - 7)) goto loc_005F58FF;
    a3 = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(a2));
    if (condition_is_not_equal) goto loc_005F58F0;
    a1 = (a1) + (8);
loc_005F58EA:
    a2 = (a2) + (8);
    goto loc_005F58D9;
loc_005F58F0:
    result = (unsigned int)((*(unsigned __int16 *)((int)((unsigned int)((unsigned int)(v_stack_m150))) + a2 * 1 - 1)) >> (3));
    result = (unsigned int)((result) - ((unsigned int)(v_r10)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_005F5940;
loc_005F58FF:
    if (a1 >= (v_stack_m138 - 3)) goto loc_005F5916;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (a2) + (4);
    }
    if (a1 >= (v_stack_m138 - 1)) goto loc_005F592F;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= v_stack_m138) goto loc_005F593D;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r10)));
loc_005F5940:
    a1 = (unsigned int)((a1) + (4));
    if (((unsigned int)(a1)) >= = ((unsigned int)((unsigned int)(v_stack_m150)))) {
        v_r10 = (unsigned int)(v_r15);
        v_stack_m150 = (unsigned int)(a1);
        v_r10 = (unsigned int)((v_r10) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))));
        v_stack_m110 = (unsigned int)(v_r10);
    }
    a4 = 0;
loc_005F5964:
    if (v_stack_m80 <= 128) goto loc_005F5BB5;
    if ((*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))) * 2 + 131072)) != 1) goto loc_005F5BB5;
    if ((unsigned int)((unsigned int)(a6)) != 0) goto loc_005F5C40;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) >> (24));
    a3 = (((unsigned __int8)((unsigned int)(*(unsigned int *)(a2)))) == ((unsigned __int8)(result))) ? 1 : 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) >> (16));
    a1 = (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(a2))))) == ((unsigned int)(a2))) ? 1 : 0;
    if ((((unsigned int)(a1)) & ((unsigned int)(a3))) == 0) goto loc_005F5BAE;
    v_stack_p30 = 2;
    result = LZ4HC_countPattern(v_stack_m140 + 4, v_stack_m138, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2)))), a4);
    v_rbx = ((unsigned int)((unsigned int)(result))) + (4);
    v_stack_mF8 = v_rbx;
    a4 = 0;
    goto loc_005F5C4F;
loc_005F59F4:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))))) - ((unsigned int)(v_stack_m138)));
    a2 = ((unsigned int)((unsigned int)(result))) + (v_stack_mE0);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168)) - 4))) goto loc_005F5BA7;
    if ((*(unsigned int *)(a2)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_005F5BA7;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))));
    a3 = (a3) + (v_stack_m140);
    if (a3 > v_stack_m138) { a3 = v_stack_m138; }
    a2 = (a2) + (4);
    if ((v_stack_m140 + 4) >= (a3 - 7)) goto loc_005F5A5A;
    a4 = (*(unsigned __int64 *)(v_stack_m140 + 4)) ^ (*(unsigned __int64 *)(a2));
    if (condition_is_not_equal) goto loc_005F5A50;
    goto loc_005F5A6B;
loc_005F5A50:
    a1 = (unsigned int)((v_stack_m140 + 4 + 8) >> (3));
    goto loc_005F5ABF;
loc_005F5A5A:
    if (a1 >= (a3 - 7)) goto loc_005F5A7F;
    a4 = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(a2));
    if (condition_is_not_equal) goto loc_005F5A71;
    a1 = (a1) + (8);
loc_005F5A6B:
    a2 = (a2) + (8);
    goto loc_005F5A5A;
loc_005F5A71:
    result = (unsigned int)((v_stack_m140) >> (3));
    result = (unsigned int)((result) - ((unsigned int)(v_stack_m140 + 4)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_005F5ABF;
loc_005F5A7F:
    if (a1 >= (a3 - 3)) goto loc_005F5A96;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (a2) + (4);
    }
    if (a1 >= (a3 - 1)) goto loc_005F5AAF;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= a3) goto loc_005F5ABD;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_m140 + 4)));
loc_005F5ABF:
    a4 = ((int)((unsigned int)(a1 + 4))) + (v_stack_m140);
    if (a4 != a3) goto loc_005F5B82;
    if (a3 >= v_stack_m138) goto loc_005F5B82;
    v_r10 = (v_stack_m138) + (-7);
    if (a4 >= v_r10) goto loc_005F5B05;
    a2 = (*(unsigned __int64 *)(a4)) ^ (*(unsigned __int64 *)(v_stack_mE8));
    if (condition_is_not_equal) goto loc_005F5B1C;
loc_005F5B05:
    if ((a4 + 8) >= v_r10) goto loc_005F5B35;
    a3 = (*(unsigned __int64 *)(a4 + 8)) ^ (*(unsigned __int64 *)(v_stack_mE8 + 8));
    if (condition_is_not_equal) goto loc_005F5B26;
    a1 = (a4 + 8) + (8);
    a2 = (v_stack_mE8 + 8) + (8);
    goto loc_005F5B05;
loc_005F5B1C:
    a1 = (unsigned int)((a1) >> (3));
    goto loc_005F5B7B;
loc_005F5B26:
    result = (unsigned int)((*(unsigned __int8 *)(a1)) >> (3));
    result = (unsigned int)((result) - ((unsigned int)(a4)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_005F5B7B;
loc_005F5B35:
    if (a1 >= (v_stack_m138 - 3)) goto loc_005F5B51;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (a2) + (4);
    }
    if (a1 >= (v_stack_m138 - 1)) goto loc_005F5B6A;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= v_stack_m138) goto loc_005F5B78;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(a4)));
loc_005F5B7B:
    v_rbx = (unsigned int)((a1 + 4) + ((unsigned int)(a1)));
loc_005F5B82:
    result = *(unsigned __int8 *)(a1);
    if (((unsigned int)(v_rbx)) >= = ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)) - 1))) {
        result = 1;
        v_stack_m150 = (unsigned int)(v_rbx);
        result = (unsigned int)((result) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))));
        v_stack_m110 = (unsigned int)(result);
    }
    a4 = 0;
loc_005F5B9D:
    goto loc_005F5964;
loc_005F5BA7:
    goto loc_005F5B9D;
loc_005F5BAE:
    v_stack_p30 = 1;
loc_005F5BB5:
loc_005F5BBA:
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))) - ((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))) * 2 + 131072))));
loc_005F5BD0:
    if (((unsigned int)(v_r11)) >= ((unsigned int)((unsigned int)(v_stack_m158)))) goto loc_005F585E;
loc_005F5BED:
loc_005F5C01:
    v_stack_m64 = (unsigned int)((unsigned int)(v_stack_m150));
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m110));
    v_stack_mC0 = v_stack_m68;
    result = (v_stack_m68) >> (32);
    v_stack_mF8 = v_stack_m68;
    if (((unsigned int)(result)) >= 4) goto loc_005F5DFB;
    v_rdi = (v_stack_m140) + 1;
    v_r10 = 0;
loc_005F5C32:
    v_stack_m140 = v_rdi;
    goto loc_005F5740;
loc_005F5C40:
    v_stack_p30 = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) != 2) goto loc_005F5BB5;
loc_005F5C4F:
    if (((unsigned int)(v_stack_mF0)) < ((unsigned int)((unsigned int)(v_stack_m158)))) goto loc_005F5BBA;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168))))) - ((unsigned int)(v_stack_mF0)));
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(v_stack_m120))));
    if (((unsigned int)(result)) < 3) goto loc_005F5BBA;
    if (((unsigned int)(v_stack_mF0)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168))))) goto loc_005F5C7F;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mF0))) - (v_stack_m130));
    v_rbx = (v_rbx) + (v_stack_mE0);
    goto loc_005F5C88;
loc_005F5C7F:
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168)))));
    v_rbx = (v_rbx) + (v_stack_mD0);
loc_005F5C88:
    if ((*(unsigned int *)(v_rbx)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_005F5BBA;
    v_r11 = v_stack_m138;
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) != 0) { v_r11 = v_stack_mC0; }
    result = LZ4HC_countPattern(v_rbx + 4, v_r11, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2)))), v_stack_p8);
    v_rdi = ((unsigned int)((unsigned int)(result))) + (4);
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) == 0) goto loc_005F5CEF;
    if ((v_rdi + v_rbx * 1) != v_r11) goto loc_005F5CE9;
    a1 = (unsigned int)((v_rdi) & (3));
    a1 = (a1) << (3);
    if (a1 != 0) {
    }
    result = LZ4HC_countPattern(v_stack_mD0, v_stack_m138, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2)))), v_stack_p8);
    v_rdi = (v_rdi) + ((unsigned int)((unsigned int)(result)));
loc_005F5CE9:
    goto loc_005F5CF2;
loc_005F5CEF:
loc_005F5CF2:
    result = LZ4HC_reverseCountPattern(v_rbx, v_stack_mD0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2)))), v_stack_p8);
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))) != 0) goto loc_005F5D3B;
    v_rbx = (v_rbx) - ((unsigned int)((unsigned int)(result)));
    if (v_rbx != v_stack_mD0) goto loc_005F5D3B;
    if (v_stack_m130 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168))))) goto loc_005F5D3B;
    a1 = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))));
    a1 = (unsigned int)((a1) & (3));
    a1 = (a1) << (3);
    if (a1 != 0) {
    }
    result = LZ4HC_reverseCountPattern(v_stack_mC0, v_stack_mE0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2)))), v_stack_p8);
    v_r11 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
loc_005F5D3B:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mF0))) - ((unsigned int)(v_r11)));
    v_r11 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m158)));
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(v_stack_m158)))) { v_r11 = (unsigned int)(result); }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mF0))) - ((unsigned int)(v_r11)));
    a1 = (a1) + (v_rdi);
    if (a1 < v_stack_mF8) goto loc_005F5D7F;
    if (v_rdi > v_stack_mF8) goto loc_005F5D7F;
    v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(v_stack_mF8)));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_stack_mF0)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168))))) - ((unsigned int)(v_rdi)));
    result = (unsigned int)((result) - 1);
    v_r11 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168))));
    if (((unsigned int)(result)) >= 3) { v_r11 = (unsigned int)(v_rdi); }
    goto loc_005F5BD0;
loc_005F5D7F:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168))))) - ((unsigned int)(v_r11)));
    result = (unsigned int)((result) - 1);
    if (((unsigned int)(result)) < 3) goto loc_005F5DF3;
    a2 = v_stack_mF8;
    if (a1 < v_stack_mF8) { a2 = a1; }
    if (((int)(v_stack_m150)) >= a2) goto loc_005F5DCF;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 262168))) - ((unsigned int)((unsigned int)(v_r11)));
    a1 = (a1) - (v_stack_mD0);
    a1 = (a1) + (v_stack_m140);
    if (a1 > ((unsigned int)(0xFFFFULL))) goto loc_005F5BED;
    result = (unsigned int)(((unsigned int)(v_stack_m120)) - ((unsigned int)(v_r11)));
    v_stack_m150 = (unsigned int)(a2);
    v_stack_m110 = (unsigned int)(result);
loc_005F5DCF:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)(v_r11) * 2 + 131072))) > ((unsigned int)(v_r11))) goto loc_005F5BED;
    v_r11 = (unsigned int)((v_r11) - ((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)(v_r11) * 2 + 131072))));
    goto loc_005F5BD0;
loc_005F5DF3:
    goto loc_005F5BD0;
loc_005F5DFB:
    v_stack_mB0 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 262168))));
loc_005F5E07:
    v_stack_mE8 = v_stack_m140;
loc_005F5E0F:
    v_stack_p30 = (unsigned int)((int)(v_stack_mF4));
    if (((int)(v_stack_mF4) + v_stack_m140 * 1) > v_stack_mA8) goto loc_005F6704;
    result = ((int)(v_stack_mF4) + v_stack_m140 * 1) + (-2);
    v_stack_m150 = (unsigned int)((int)(v_stack_mF4));
    v_stack_m118 = result;
    v_stack_mA0 = result;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262168))))) - ((unsigned int)(*(unsigned __int64 *)(v_stack_p8 + 262152))));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(result)));
    v_stack_m110 = *(unsigned __int64 *)(v_stack_p8 + 262152);
    v_stack_m154 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262168)));
    v_stack_m130 = (unsigned int)(v_rdi);
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262172)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262172)) + 65536)) <= ((unsigned int)(v_rdi))) goto loc_005F5E84;
    v_stack_m148 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262172)));
    goto loc_005F5E8E;
loc_005F5E84:
    v_stack_m148 = (unsigned int)(v_rdi - 65535);
loc_005F5E8E:
    a4 = (*(unsigned __int64 *)(v_stack_p8 + 262160)) - ((unsigned int)(*(unsigned int *)(v_stack_p8 + 262172)));
    v_stack_m128 = *(unsigned __int64 *)(v_stack_p8 + 262160);
    a4 = (a4) + ((unsigned int)(*(unsigned int *)(v_stack_p8 + 262168)));
    v_stack_m90 = a4;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (v_stack_m140));
    a4 = 0;
    v_stack_mD8 = (unsigned int)((unsigned int)(v_stack_m74));
    v_stack_m158 = 0;
    v_stack_m88 = 0;
    v_stack_m120 = 0;
    v_stack_m14C = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176)))) >= ((unsigned int)(v_rdi))) goto loc_005F5F4C;
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))))) - ((unsigned int)(*(unsigned int *)(v_stack_p8 + 262168)));
    a3 = (a3) + (*(unsigned __int64 *)(v_stack_p8 + 262152));
loc_005F5F00:
    a2 = (unsigned int)((*(unsigned __int64 *)(v_stack_p8 + 262160)) * (*(unsigned int *)(a3)));
    a2 = (a2) >> (17);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))))) - (*(unsigned int *)(v_stack_p8 + a2 * 4)));
    if (a1 > ((unsigned int)(0xFFFFULL))) { a1 = (unsigned int)(0xFFFFULL); }
    a3 = (a3) + (1);
    *(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))) * 2 + 131072) = (unsigned __int16)(a1);
    *(unsigned int *)(v_stack_p8 + a2 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176)));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))) + (1));
    if (((unsigned int)(a4)) < ((unsigned int)(v_rdi))) goto loc_005F5F00;
    goto loc_005F5F53;
loc_005F5F4C:
loc_005F5F53:
    *(unsigned int *)(v_stack_p8 + 262176) = (unsigned int)(v_rdi);
    a1 = (unsigned int)((a1) * (*(unsigned int *)(result)));
    v_stack_mE0 = (int)((unsigned int)(v_r10));
    a1 = (a1) >> (17);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))) < v_stack_m148) goto loc_005F64F8;
    v_stack_m118 = v_stack_m118;
loc_005F5F8B:
    v_r12 = 0;
    v_stack_m110 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m158))));
    if (condition_is_less_or_equal) goto loc_005F64EB;
    result = (unsigned int)(((unsigned int)(v_stack_mD8)) - ((unsigned int)(v_r12 + 1)));
    v_stack_mD8 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))) < ((unsigned int)((unsigned int)(v_stack_m154)))) goto loc_005F617E;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))))) - ((unsigned int)((unsigned int)(v_stack_m154))));
    result = (result + v_stack_m110 * 1) - ((int)((unsigned int)(v_r10)));
    if ((*(unsigned __int16 *)((int)((unsigned int)((unsigned int)(v_stack_m150))) + v_stack_m140 * 1 - 1)) != ((unsigned __int16)(*(unsigned __int16 *)(result + (int)((unsigned int)((unsigned int)(v_stack_m150))) * 1 - 1)))) goto loc_005F6404;
    if ((*(unsigned int *)(result + v_stack_m110 * 1)) != ((unsigned int)((unsigned int)(v_stack_m14C)))) goto loc_005F6404;
    if ((int)((unsigned int)(v_r10)) == 0) goto loc_005F605C;
    a1 = (v_stack_m140) - (v_stack_mA0);
    result = (v_stack_m110) - (result + v_stack_m110 * 1);
    if (a1 <= result) goto loc_005F6010;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m140))) - ((unsigned int)(v_stack_mA0)));
    goto loc_005F6015;
loc_005F6010:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m110))) - ((unsigned int)(result + v_stack_m110 * 1)));
loc_005F6015:
    a2 = (unsigned int)(-((unsigned int)((unsigned int)(a1))));
    v_r10 = (v_stack_mA0) - (result + v_stack_m110 * 1);
loc_005F6023:
    if (((unsigned int)(a2)) <= 3) goto loc_005F6083;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10 + result + v_stack_m110 * 1 - 4 * 1))) ^ (*(unsigned int *)(result + v_stack_m110 * 1 - 4)));
    if (condition_is_not_equal) goto loc_005F6042;
    v_r15 = (unsigned int)((0) - (4));
    a2 = (unsigned int)((a2) - (4));
    v_rbx = (0) - (4);
    a4 = (result + v_stack_m110 * 1 - 4) - (4);
    goto loc_005F6023;
loc_005F6042:
    v_stack_mA0 = 0;
    a1 = (unsigned int)((31) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) >> (3));
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)(a1)));
loc_005F6057:
loc_005F605C:
    if ((v_stack_mA0 + 4) >= (v_stack_m138 - 7)) goto loc_005F60D8;
    a3 = (*(unsigned __int64 *)(v_stack_mA0 + 4)) ^ (*(unsigned __int64 *)(result + v_stack_m110 * 1 + 4));
    if (condition_is_not_equal) goto loc_005F60CE;
    goto loc_005F60E9;
loc_005F6083:
    if (1 <= ((int)((unsigned int)(v_stack_mA0 + 4 + 8)))) goto loc_005F6057;
    a1 = (v_stack_m110 - 1) + (1);
    a4 = ((int)(a6)) - (v_stack_m110);
    a4 = (a4) - ((unsigned int)((unsigned int)(result)));
    a4 = (a4) + (v_stack_m140);
    a2 = (1) - (v_stack_m110);
    a1 = (a1) + ((unsigned int)((unsigned int)(result)));
    a2 = (a2) - ((unsigned int)((unsigned int)(result)));
loc_005F60B4:
    if ((*(unsigned __int8 *)(a4 + a1 * 1 - 2)) != ((unsigned __int8)(*(unsigned __int8 *)(a1)))) goto loc_005F605C;
    a1 = (a1) - (1);
    v_r15 = (unsigned int)((v_r15) - (1));
    if ((a2 + a1 * 1) > ((int)((unsigned int)(v_stack_mA0 + 4 + 8)))) goto loc_005F60B4;
    goto loc_005F605C;
loc_005F60CE:
    a1 = (unsigned int)((a1) >> (3));
    goto loc_005F613F;
loc_005F60D8:
    if (a1 >= a4) goto loc_005F60FE;
    a3 = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(a2));
    if (condition_is_not_equal) goto loc_005F60EF;
    a1 = (a1) + (8);
loc_005F60E9:
    a2 = (a2) + (8);
    goto loc_005F60D8;
loc_005F60EF:
    result = (unsigned int)((a2 + a1 * 1) >> (3));
    result = (unsigned int)((result) - ((unsigned int)(v_stack_mA0 + 4)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_005F613F;
loc_005F60FE:
    if (a1 >= (v_stack_m138 - 3)) goto loc_005F6115;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (a2) + (4);
    }
    if (a1 >= (v_stack_m138 - 1)) goto loc_005F612E;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= v_stack_m138) goto loc_005F613C;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + (1);
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_mA0 + 4)));
loc_005F613F:
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r15)));
    a1 = (unsigned int)((a1) + (4));
    if (((unsigned int)(a1)) <= v_stack_m150) goto loc_005F6412;
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m130)) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))));
    result = ((int)((unsigned int)(v_r15))) + (v_stack_mA0);
    v_stack_m150 = (unsigned int)(a1);
    v_stack_m118 = result;
    v_stack_m120 = (unsigned int)(v_r12);
    goto loc_005F641F;
loc_005F617E:
    result = (unsigned int)((result) - (v_stack_m108));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))) > ((unsigned int)((unsigned int)(v_stack_m154) - 4))) goto loc_005F641A;
    if ((*(unsigned int *)(result + a2 * 1)) != ((unsigned int)((unsigned int)(v_stack_m14C)))) goto loc_005F641A;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m154)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))));
    v_r10 = (v_r10) + (v_stack_mA0);
    if (v_r10 > v_stack_m138) { v_r10 = v_stack_m138; }
    if ((v_stack_mA0 + 4) >= (v_r10 - 7)) goto loc_005F61DE;
    a3 = (*(unsigned __int64 *)(v_stack_mA0 + 4)) ^ (*(unsigned __int64 *)(result + a2 * 1 + 4));
    if (condition_is_not_equal) goto loc_005F61D4;
    goto loc_005F61EF;
loc_005F61D4:
    a1 = (unsigned int)((v_stack_mA0 + 4 + 8) >> (3));
    goto loc_005F6243;
loc_005F61DE:
    if (a1 >= (v_r10 - 7)) goto loc_005F6203;
    a3 = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(result + a2 * 1 + 4));
    if (condition_is_not_equal) goto loc_005F61F5;
    a1 = (a1) + (8);
loc_005F61EF:
    a2 = (result + a2 * 1 + 4) + (8);
    goto loc_005F61DE;
loc_005F61F5:
    result = (unsigned int)(((unsigned int)(v_stack_m154) - 4) >> (3));
    result = (unsigned int)((result) - ((unsigned int)(v_stack_mA0 + 4)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_005F6243;
loc_005F6203:
    if (a1 >= (v_r10 - 3)) goto loc_005F621A;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (a2) + (4);
    }
    if (a1 >= (v_r10 - 1)) goto loc_005F6233;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= v_r10) goto loc_005F6241;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_mA0 + 4)));
loc_005F6243:
    v_rbx = ((int)((unsigned int)(a1 + 4))) + (v_stack_mA0);
    if (v_rbx != v_r10) goto loc_005F62F8;
    if (v_r10 >= v_stack_m138) goto loc_005F62F8;
    if (v_rbx >= (v_stack_m138 - 7)) goto loc_005F6282;
    a1 = (*(unsigned __int64 *)(v_stack_m110)) ^ (*(unsigned __int64 *)(v_rbx));
    if (condition_is_not_equal) goto loc_005F6299;
loc_005F6282:
    if ((v_rbx + 8) >= (v_stack_m138 - 7)) goto loc_005F62B1;
    a3 = (*(unsigned __int64 *)(v_rbx + 8)) ^ (*(unsigned __int64 *)(v_stack_m110 + 8));
    if (condition_is_not_equal) goto loc_005F62A3;
    a1 = (v_rbx + 8) + (8);
    a2 = (v_stack_m110 + 8) + (8);
    goto loc_005F6282;
loc_005F6299:
    a1 = (unsigned int)((a1) >> (3));
    goto loc_005F62F6;
loc_005F62A3:
    result = (unsigned int)((*(unsigned __int8 *)(a1)) >> (3));
    result = (unsigned int)((result) - ((unsigned int)(v_rbx)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_005F62F6;
loc_005F62B1:
    if (a1 >= (v_stack_m138 - 3)) goto loc_005F62CD;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (a2) + (4);
    }
    if (a1 >= (v_stack_m138 - 1)) goto loc_005F62E6;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= v_stack_m138) goto loc_005F62F4;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(v_rbx)));
loc_005F62F6:
    v_rsi = (unsigned int)((a1 + 4) + ((unsigned int)(a1)));
loc_005F62F8:
    result = 0;
    if (v_stack_mE0 == 0) goto loc_005F63D4;
    a1 = (v_stack_m128) - (result + a2 * 1);
    result = (v_stack_m140) - (v_stack_mA0);
    if (result <= a1) goto loc_005F632B;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m140))) - ((unsigned int)(v_stack_mA0)));
    goto loc_005F6331;
loc_005F632B:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m128))) - ((unsigned int)(result + a2 * 1)));
loc_005F6331:
    a4 = (unsigned int)(-((unsigned int)((unsigned int)(a1))));
    v_rbx = (v_stack_mA0) - (result + a2 * 1);
loc_005F6341:
    if (((unsigned int)(a4)) <= 3) goto loc_005F637E;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + result + a2 * 1 - 4 * 1))) ^ (*(unsigned int *)(result + a2 * 1 - 4)));
    if (condition_is_not_equal) goto loc_005F6361;
    a2 = (unsigned int)((0) - (4));
    a4 = (unsigned int)((a4) - (4));
    v_rdi = (0) - (4);
    v_r10 = (result + a2 * 1 - 4) - (4);
    goto loc_005F6341;
loc_005F6361:
    v_r12 = 0;
    v_stack_mA0 = 0;
    a1 = (unsigned int)((v_r12 + 31) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) >> (3));
    a2 = (unsigned int)((a2) - ((unsigned int)(a1)));
    goto loc_005F63DA;
loc_005F637E:
    if (((unsigned int)(v_stack_m130)) <= ((int)((unsigned int)(a1)))) goto loc_005F63CB;
    result = ((int)(a6)) - (v_stack_m128);
    result = (result) - (0);
    v_r10 = (v_stack_m140) + (result);
    a3 = (1) - (v_stack_m128);
    a1 = ((unsigned int)(v_stack_m130) - 1) + (result + a2 * 1);
    a3 = (a3) - (0);
loc_005F63B4:
    if ((*(unsigned __int8 *)(v_r10 + a1 * 1 - 2)) != ((unsigned __int8)(*(unsigned __int8 *)(a1)))) goto loc_005F63CB;
    a1 = (a1) - (1);
    a2 = (unsigned int)((a2) - (1));
    if ((a3 + a1 * 1) > ((int)((unsigned int)(a1)))) goto loc_005F63B4;
loc_005F63CB:
    v_r12 = 0;
    goto loc_005F63DA;
loc_005F63D4:
    v_r12 = 0;
loc_005F63DA:
    v_rsi = (unsigned int)((v_rsi) - (0));
    if (((unsigned int)(v_rsi)) <= v_stack_m150) goto loc_005F6407;
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m130)) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))));
    result = ((int)(0)) + (v_stack_mA0);
    v_stack_m150 = (unsigned int)(v_rsi);
    v_stack_m118 = result;
    v_stack_m120 = (unsigned int)(v_rdi);
    goto loc_005F6407;
loc_005F6404:
loc_005F6407:
    goto loc_005F6422;
loc_005F6412:
    goto loc_005F6422;
loc_005F641A:
loc_005F641F:
    v_r12 = 0;
loc_005F6422:
    if (v_stack_m80 <= 128) goto loc_005F64B2;
    if ((*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))) * 2 + 131072)) != 1) goto loc_005F64B2;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m110)))) != 0) goto loc_005F6529;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m14C)))) >> (24));
    a3 = (((unsigned __int8)((unsigned int)(v_stack_m14C))) == ((unsigned __int8)(result))) ? 1 : 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m14C)))) >> (16));
    a1 = (((unsigned int)((unsigned __int16)((unsigned int)(v_stack_m14C)))) == ((unsigned int)(a2))) ? 1 : 0;
    if ((((unsigned int)(a1)) & ((unsigned int)(a3))) == 0) goto loc_005F64A8;
    v_stack_m158 = 2;
    result = LZ4HC_countPattern(v_stack_mA0 + 4, v_stack_m138, (unsigned int)((unsigned int)((unsigned int)(v_stack_m14C))), 1);
    result = ((unsigned int)((unsigned int)(result))) + (4);
    v_stack_m88 = result;
    goto loc_005F6532;
loc_005F64A8:
    v_stack_m158 = 1;
loc_005F64B2:
loc_005F64B6:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))) - ((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))) * 2 + 131072))));
loc_005F64CC:
    if (((unsigned int)(v_r13)) >= ((unsigned int)((unsigned int)(v_stack_m148)))) goto loc_005F5F8B;
loc_005F64EB:
loc_005F64F8:
    v_r10 = 0;
    v_stack_m5C = (unsigned int)((unsigned int)(v_stack_m150));
    v_stack_m60 = (unsigned int)((unsigned int)(v_stack_m120));
    v_stack_m128 = v_stack_m60;
    goto loc_005F6712;
loc_005F6529:
    v_stack_m158 = (unsigned int)(v_stack_mE8);
    if (((unsigned int)(v_stack_mE8)) != 2) goto loc_005F64B2;
loc_005F6532:
    if (((unsigned int)((unsigned int)(v_stack_m150))) < ((unsigned int)((unsigned int)(v_stack_m148)))) goto loc_005F64B6;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m154)))) - ((unsigned int)((unsigned int)(v_stack_m150))));
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(a6))));
    if (((unsigned int)(result)) < 3) goto loc_005F64B6;
    if (((unsigned int)((unsigned int)(v_stack_m150))) >= ((unsigned int)((unsigned int)(v_stack_m154)))) goto loc_005F656B;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m150)))) - (v_stack_m108));
    v_rbx = (v_rbx) + (v_stack_m128);
    goto loc_005F6571;
loc_005F656B:
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)((unsigned int)(v_stack_m154))));
    v_rbx = (v_rbx) + (v_stack_mD0);
loc_005F6571:
    if ((*(unsigned int *)(v_rbx)) != ((unsigned int)((unsigned int)(v_stack_m124)))) goto loc_005F64B2;
    v_rdi = v_stack_m60;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6)))) != 0) { v_rdi = v_stack_m90; }
    result = LZ4HC_countPattern(v_rbx + 4, v_rdi, (unsigned int)((unsigned int)((unsigned int)(v_stack_m124))), (unsigned int)(a6));
    v_rsi = ((unsigned int)((unsigned int)(result))) + (4);
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6)))) == 0) goto loc_005F65D4;
    if ((v_rsi + v_rbx * 1) != v_rdi) goto loc_005F65CD;
    a1 = (unsigned int)((v_rsi) & (3));
    a1 = (a1) << (3);
    if (a1 != 0) {
    }
    result = LZ4HC_countPattern(v_stack_mD0, v_stack_m138, (unsigned int)(v_stack_m14C), (unsigned int)(a6));
    v_rsi = (v_rsi) + ((unsigned int)((unsigned int)(result)));
loc_005F65CD:
    goto loc_005F65D7;
loc_005F65D4:
loc_005F65D7:
    result = LZ4HC_reverseCountPattern(v_rbx, v_stack_mD0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m14C))), (unsigned int)(a6));
    a2 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a6)))) != 0) goto loc_005F6634;
    v_rbx = (v_rbx) - ((unsigned int)((unsigned int)(result)));
    if (v_rbx != v_stack_mD0) goto loc_005F6634;
    if (v_stack_m108 >= ((unsigned int)((unsigned int)(v_stack_m154)))) goto loc_005F6634;
    a1 = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))));
    a1 = (unsigned int)((a1) & (3));
    a1 = (a1) << (3);
    if (a1 != 0) {
    }
    result = LZ4HC_reverseCountPattern(v_stack_m90, v_stack_m128, (unsigned int)((unsigned int)((unsigned int)(v_stack_m14C))), (unsigned int)(a6));
    v_rdi = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    a2 = 0;
loc_005F6634:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m150)))) - ((unsigned int)(v_rdi)));
    v_r13 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m148)));
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(v_stack_m148)))) { v_r13 = (unsigned int)(result); }
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m150)))) - ((unsigned int)(v_r13)));
    a1 = (a1) + (v_rsi);
    if (a1 < v_stack_m88) goto loc_005F667A;
    if (v_rsi > v_stack_m88) goto loc_005F667A;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m150)) - ((unsigned int)(v_stack_m88)));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_rsi)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m154)))) - ((unsigned int)(v_r15)));
    result = (unsigned int)((result) - 1);
    v_r13 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m154)));
    if (((unsigned int)(result)) >= 3) { v_r13 = (unsigned int)(v_r15); }
    goto loc_005F64CC;
loc_005F667A:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m154)))) - ((unsigned int)(v_r13)));
    result = (unsigned int)((result) - 1);
    if (((unsigned int)(result)) < 3) goto loc_005F66FC;
    if (v_stack_mE0 != 0) goto loc_005F64CC;
    a2 = v_stack_m88;
    if (a1 < v_stack_m88) { a2 = a1; }
    if (((int)(v_stack_m150)) >= a2) goto loc_005F66D8;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m154)))) - ((unsigned int)((unsigned int)(v_r13)));
    a1 = (a1) - (v_stack_mD0);
    a1 = (a1) + (v_stack_mC0);
    if (a1 > ((unsigned int)(0xFFFFULL))) goto loc_005F64EB;
    result = (unsigned int)(((unsigned int)(v_stack_m130)) - ((unsigned int)(v_r13)));
    v_stack_m150 = (unsigned int)(a2);
    v_stack_m120 = (unsigned int)(result);
    v_stack_m118 = v_stack_mC0;
loc_005F66D8:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)(v_r13) * 2 + 131072))) > ((unsigned int)(v_r13))) goto loc_005F64EB;
    v_r13 = (unsigned int)((v_r13) - ((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)(v_r13) * 2 + 131072))));
    goto loc_005F64CC;
loc_005F66FC:
    goto loc_005F64CC;
loc_005F6704:
    v_r10 = 0;
    v_stack_m128 = 0;
loc_005F6712:
    v_stack_mE0 = 0;
    if (0 <= ((unsigned int)(v_stack_m88))) goto loc_005F7884;
    if ((*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)(v_r13) * 2 + 131072)) >= ((unsigned int)((unsigned int)((unsigned int)(v_stack_m154))))) goto loc_005F674B;
    result = ((int)(v_stack_mAC)) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_m154))));
    v_r13 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m154)));
    if (v_stack_m118 < result) {
        v_stack_mF8 = v_stack_mC0;
        v_r13 = *(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)(v_r13) * 2 + 131072);
        a4 = v_stack_mF4;
        v_stack_p30 = (unsigned int)(a4);
        v_stack_m140 = *(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)(v_r13) * 2 + 131072);
    }
    result = (v_stack_m118) - (v_r13);
    if (result >= 3) goto loc_005F6768;
    v_stack_m140 = v_stack_m118;
    v_stack_mF8 = 0;
    goto loc_005F5E0F;
loc_005F6768:
loc_005F676E:
    result = (v_stack_m118) - (v_stack_m118);
    if (result >= 18) goto loc_005F67CB;
    a3 = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(a4)) > 18) { a3 = 18; }
    a1 = ((int)(0)) + (-4);
    a1 = (a1) + (v_stack_m118);
    a2 = ((int)((unsigned int)(a3))) + (v_stack_m118);
    if (a2 >= = a1) {
        a3 = (unsigned int)(v_stack_m118);
        a3 = (unsigned int)((a3) - ((unsigned int)(v_stack_m118)));
        a3 = (unsigned int)((a3) + (-4));
        a3 = (unsigned int)((a3) + (0));
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m118))) - ((unsigned int)(v_stack_m118)));
    a1 = (unsigned int)((a1) + ((unsigned int)(a3)));
    v_rsi = 0;
    v_rdi = 0;
    v_r12 = v_stack_m118;
    if (!(condition_is_less_or_equal)) {
        result = (int)((unsigned int)(a1));
        v_r12 = (v_stack_m118) + (result);
        v_rsi = (unsigned int)((0) - ((unsigned int)(a1)));
        v_stack_m118 = v_r12;
        v_stack_m124 = (unsigned int)(v_rsi);
        v_rdi = v_stack_m128;
        v_stack_mE0 = v_rdi;
    }
    a1 = ((int)((unsigned int)(v_rsi))) + (v_r12);
    if (a1 > ((unsigned int)(v_stack_m148))) goto loc_005F70A6;
    v_stack_mB8 = a1 - 3;
    v_stack_m88 = a1 - 3;
    v_stack_m158 = (unsigned int)(v_rsi);
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(a1 - 3))) - ((unsigned int)(*(unsigned __int64 *)(v_stack_p8 + 262152))));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262168)))));
    v_stack_m110 = *(unsigned __int64 *)(v_stack_p8 + 262152);
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262168)));
    v_stack_m130 = (unsigned int)(v_r13);
    v_stack_m154 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262172)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262172)) + 65536)) <= ((unsigned int)(v_r13))) goto loc_005F6833;
    v_stack_m150 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262172)));
    goto loc_005F683E;
loc_005F6833:
    v_stack_m150 = (unsigned int)(v_r13 - 65535);
loc_005F683E:
    a4 = ((unsigned int)(*(unsigned int *)(v_stack_p8 + 262168))) - ((unsigned int)(*(unsigned int *)(v_stack_p8 + 262172)));
    a4 = (a4) + (*(unsigned __int64 *)(v_stack_p8 + 262160));
    v_stack_mB0 = a4;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(a1 - 3))) - (v_stack_m118));
    a4 = 0;
    v_stack_mD8 = (unsigned int)((unsigned int)(v_stack_m74));
    v_stack_m148 = 0;
    v_stack_mE8 = 0;
    v_stack_m120 = 0;
    v_stack_mC8 = *(unsigned __int64 *)(v_stack_p8 + 262160);
    v_stack_m14C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 - 3)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176)))) >= ((unsigned int)(v_r13))) goto loc_005F68F0;
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))))) - ((unsigned int)(*(unsigned int *)(v_stack_p8 + 262168)));
    a3 = (a3) + (*(unsigned __int64 *)(v_stack_p8 + 262152));
loc_005F68A9:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 262172))) * (*(unsigned int *)(a3)));
    a2 = (a2) >> (17);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))))) - (*(unsigned int *)(v_stack_p8 + a2 * 4)));
    if (a1 > ((unsigned int)(0xFFFFULL))) { a1 = (unsigned int)(0xFFFFULL); }
    a3 = (a3) + (1);
    *(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))) * 2 + 131072) = (unsigned __int16)(a1);
    *(unsigned int *)(v_stack_p8 + a2 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176)));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 262176))) + (1));
    if (((unsigned int)(a4)) < ((unsigned int)(v_r13))) goto loc_005F68A9;
loc_005F68F0:
    *(unsigned int *)(v_stack_p8 + 262176) = (unsigned int)(v_r13);
    a1 = (unsigned int)((a1) * (*(unsigned int *)(v_stack_m88)));
    a1 = (a1) >> (17);
    v_stack_mC0 = (int)((unsigned int)(v_r10));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))) < v_stack_m150) goto loc_005F6E99;
    v_stack_mB8 = v_stack_mB8;
    v_stack_m90 = (int)((unsigned int)(v_rsi));
loc_005F6936:
    v_r10 = 0;
    if (condition_is_less_or_equal) goto loc_005F6E88;
    result = (unsigned int)(((unsigned int)(v_stack_mD8)) - 1);
    v_stack_mD8 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))) < ((unsigned int)((unsigned int)(v_stack_m108)))) goto loc_005F6B2B;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))))) - ((unsigned int)((unsigned int)(v_stack_m108))));
    v_rbx = (v_rbx) + (v_stack_m110);
    result = ((int)(v_stack_m158)) - ((int)((unsigned int)(v_r10)));
    if ((*(unsigned __int16 *)((int)(v_stack_m158) + v_stack_m118 * 1 - 1)) != ((unsigned __int16)(*(unsigned __int16 *)(result + v_rbx * 1 - 1)))) goto loc_005F6DB9;
    if ((*(unsigned int *)(v_rbx)) != ((unsigned int)((unsigned int)(v_stack_m14C)))) goto loc_005F6DB9;
    if ((int)((unsigned int)(v_r10)) == 0) goto loc_005F6A57;
    a1 = (v_stack_m110) - (v_rbx);
    result = (v_stack_m118) - (v_stack_m88);
    if (result <= a1) goto loc_005F69B4;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m118))) - ((unsigned int)(v_stack_m88)));
    goto loc_005F69B9;
loc_005F69B4:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m110))) - ((unsigned int)(v_rbx)));
loc_005F69B9:
    a2 = (unsigned int)(-((unsigned int)((unsigned int)(a1))));
    v_r10 = (v_rbx) - (v_stack_m88);
loc_005F69C7:
    if (((unsigned int)(a2)) <= 3) goto loc_005F69FB;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10 + v_stack_m88 - 4 * 1))) ^ (*(unsigned int *)(v_stack_m88 - 4)));
    if (condition_is_not_equal) goto loc_005F69E5;
    v_rsi = (unsigned int)((0) - (4));
    a2 = (unsigned int)((a2) - (4));
    v_r11 = (0) - (4);
    a4 = (v_stack_m88 - 4) - (4);
    goto loc_005F69C7;
loc_005F69E5:
    a1 = (unsigned int)((31) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) >> (3));
    v_rsi = (unsigned int)((v_rsi) - ((unsigned int)(a1)));
    goto loc_005F6A52;
loc_005F69FB:
    if (v_r11 <= ((int)((unsigned int)(a1)))) goto loc_005F6A52;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))))) - ((unsigned int)((unsigned int)(v_stack_m108))));
    a4 = (a4) - (v_stack_m90);
    a1 = (4) - (v_stack_m90);
    a4 = (a4) - (v_stack_m118);
    a4 = (a4) + (v_stack_m110);
    a2 = (v_stack_m118 - 4) + (v_r11 + v_stack_m90 * 1);
    a1 = (a1) - (v_stack_m118);
loc_005F6A36:
    if ((*(unsigned __int8 *)(a2)) != ((unsigned __int8)(*(unsigned __int8 *)(a4 + a2 * 1 + 3)))) goto loc_005F6A4E;
    a2 = (a2) - (1);
    v_rsi = (unsigned int)((v_rsi) - (1));
    if ((a1 + a2 * 1) > ((int)((unsigned int)(a1)))) goto loc_005F6A36;
loc_005F6A4E:
loc_005F6A52:
loc_005F6A57:
    a4 = (v_stack_m138) + (-7);
    if ((v_stack_m88 + 4) >= a4) goto loc_005F6A88;
    a3 = (*(unsigned __int64 *)(v_stack_m88 + 4)) ^ (*(unsigned __int64 *)(v_rbx + 4));
    if (condition_is_not_equal) goto loc_005F6A7E;
    goto loc_005F6A99;
loc_005F6A7E:
    a1 = (unsigned int)((v_stack_m88 + 4 + 8) >> (3));
    goto loc_005F6AF4;
loc_005F6A88:
    if (a1 >= a4) goto loc_005F6AAE;
    a3 = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(v_rbx + 4));
    if (condition_is_not_equal) goto loc_005F6A9F;
    a1 = (a1) + (8);
loc_005F6A99:
    a2 = (v_rbx + 4) + (8);
    goto loc_005F6A88;
loc_005F6A9F:
    result = (unsigned int)((a1 + a2 * 1) >> (3));
    result = (unsigned int)((result) - ((unsigned int)(v_stack_m88 + 4)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_005F6AF4;
loc_005F6AAE:
    if (a1 >= (v_stack_m138 - 3)) goto loc_005F6ACA;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (a2) + (4);
    }
    if (a1 >= (v_stack_m138 - 1)) goto loc_005F6AE3;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= v_stack_m138) goto loc_005F6AF1;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_m88 + 4)));
loc_005F6AF4:
    a1 = (unsigned int)((a1) - ((unsigned int)(v_rsi)));
    a1 = (unsigned int)((a1) + (4));
    result = *(unsigned __int8 *)(a1);
    if (((unsigned int)(a1)) >= = ((unsigned int)((unsigned int)(v_stack_m158)))) {
        result = v_stack_m130;
        result = (unsigned int)((result) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))));
        v_stack_m158 = (unsigned int)(a1);
        v_stack_m120 = (unsigned int)(result);
        result = (int)((unsigned int)(v_rsi));
        result = (result) + (v_stack_m88);
        v_stack_mB8 = result;
    }
    v_r10 = 0;
    goto loc_005F6DC2;
loc_005F6B2B:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))))) - ((unsigned int)(a2)));
    v_rsi = (v_rsi) + (v_stack_m138);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))) > ((unsigned int)((unsigned int)(v_stack_m108) - 4))) goto loc_005F6DBD;
    if ((*(unsigned int *)(v_rsi)) != ((unsigned int)((unsigned int)(v_stack_m14C)))) goto loc_005F6DBD;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m108)))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))));
    v_r10 = (v_r10) + (v_stack_m88);
    if (v_r10 > v_stack_m138) { v_r10 = v_stack_m138; }
    if ((v_stack_m88 + 4) >= (v_r10 - 7)) goto loc_005F6B88;
    a3 = (*(unsigned __int64 *)(v_stack_m88 + 4)) ^ (*(unsigned __int64 *)(v_rsi + 4));
    if (condition_is_not_equal) goto loc_005F6B7E;
    goto loc_005F6B99;
loc_005F6B7E:
    a1 = (unsigned int)((v_stack_m88 + 4 + 8) >> (3));
    goto loc_005F6BEF;
loc_005F6B88:
    if (a1 >= (v_r10 - 7)) goto loc_005F6BAE;
    a3 = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(v_rsi + 4));
    if (condition_is_not_equal) goto loc_005F6B9F;
    a1 = (a1) + (8);
loc_005F6B99:
    a2 = (v_rsi + 4) + (8);
    goto loc_005F6B88;
loc_005F6B9F:
    result = (unsigned int)(((unsigned int)(v_stack_m108) - 4) >> (3));
    result = (unsigned int)((result) - ((unsigned int)(v_stack_m88 + 4)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_005F6BEF;
loc_005F6BAE:
    if (a1 >= (v_r10 - 3)) goto loc_005F6BC5;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (a2) + (4);
    }
    if (a1 >= (v_r10 - 1)) goto loc_005F6BDE;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= v_r10) goto loc_005F6BEC;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_m88 + 4)));
loc_005F6BEF:
    v_r11 = ((int)((unsigned int)(a1 + 4))) + (v_stack_m88);
    if (v_r11 != v_r10) goto loc_005F6CA8;
    if (v_r10 >= v_stack_m138) goto loc_005F6CA8;
    if (v_r11 >= (v_stack_m138 - 7)) goto loc_005F6C30;
    a2 = (*(unsigned __int64 *)(v_r11)) ^ (*(unsigned __int64 *)(v_stack_m110));
    if (condition_is_not_equal) goto loc_005F6C47;
loc_005F6C30:
    if ((v_r11 + 8) >= (v_stack_m138 - 7)) goto loc_005F6C60;
    a3 = (*(unsigned __int64 *)(v_r11 + 8)) ^ (*(unsigned __int64 *)(v_stack_m110 + 8));
    if (condition_is_not_equal) goto loc_005F6C51;
    a1 = (v_r11 + 8) + (8);
    a2 = (v_stack_m110 + 8) + (8);
    goto loc_005F6C30;
loc_005F6C47:
    a1 = (unsigned int)((a1) >> (3));
    goto loc_005F6CA6;
loc_005F6C51:
    result = (unsigned int)((*(unsigned __int8 *)(a1)) >> (3));
    result = (unsigned int)((result) - ((unsigned int)(v_r11)));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_005F6CA6;
loc_005F6C60:
    if (a1 >= (v_stack_m138 - 3)) goto loc_005F6C7C;
    if ((*(unsigned int *)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) {
        a1 = (a1) + (4);
        a2 = (a2) + (4);
    }
    if (a1 >= (v_stack_m138 - 1)) goto loc_005F6C95;
    if ((*(unsigned __int16 *)(a2)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) {
        a1 = (a1) + (2);
        a2 = (a2) + (2);
    }
    if (a1 >= v_stack_m138) goto loc_005F6CA3;
    if ((*(unsigned __int8 *)(a2)) == ((unsigned __int8)(*(unsigned __int8 *)(a1)))) {
        a1 = (a1) + 1;
    }
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r11)));
loc_005F6CA6:
    v_rbx = (unsigned int)((a1 + 4) + ((unsigned int)(a1)));
loc_005F6CA8:
    v_r10 = 0;
    if (v_stack_mC0 == 0) goto loc_005F6D1C;
    a1 = (v_stack_mC8) - (v_rsi);
    result = (v_stack_m118) - (v_stack_m88);
    if (result <= a1) goto loc_005F6CD6;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m118))) - ((unsigned int)(v_stack_m88)));
    goto loc_005F6CDB;
loc_005F6CD6:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mC8))) - ((unsigned int)(v_rsi)));
loc_005F6CDB:
    a2 = (unsigned int)(-((unsigned int)((unsigned int)(a1))));
    v_rsi = (v_rsi) - (v_stack_m88);
loc_005F6CE6:
    if (((unsigned int)(a2)) <= 3) goto loc_005F6D4C;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + v_stack_m88 - 4 * 1))) ^ (*(unsigned int *)(v_stack_m88 - 4)));
    if (condition_is_not_equal) goto loc_005F6D05;
    a3 = (unsigned int)((0) - (4));
    a2 = (unsigned int)((a2) - (4));
    v_r11 = (0) - (4);
    v_r10 = (v_stack_m88 - 4) - (4);
    goto loc_005F6CE6;
loc_005F6D05:
    v_r10 = 0;
    v_stack_mA0 = 0;
    a1 = (unsigned int)((v_r10 + 31) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) >> (3));
    a3 = (unsigned int)((a3) - ((unsigned int)(a1)));
loc_005F6D1C:
loc_005F6D21:
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(a3)));
    if (((unsigned int)(v_rbx)) >= = v_stack_m158) {
        result = v_stack_m130;
        result = (unsigned int)((result) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4)))));
        v_stack_m158 = (unsigned int)(v_rbx);
        v_stack_m120 = (unsigned int)(result);
        result = (int)((unsigned int)(a3));
        result = (result) + (v_stack_m88);
        v_stack_mB8 = result;
    }
    goto loc_005F6DC2;
loc_005F6D4C:
    if (((unsigned int)(v_stack_m154)) <= ((int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m148))))))))) goto loc_005F6DAC;
    a2 = (v_stack_m118) + (-4);
    a1 = (4) - (v_stack_m90);
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))))) - ((unsigned int)((unsigned int)(v_stack_m154))));
    a2 = (a2) + ((unsigned int)(v_stack_m154) + v_stack_m90 * 1);
    v_r10 = (v_r10) - (v_stack_m90);
    v_r10 = (v_r10) - (v_stack_m118);
    v_r10 = (v_r10) + (v_stack_mC8);
    a1 = (a1) - (v_stack_m118);
loc_005F6D8E:
    if ((*(unsigned __int8 *)(a2)) != ((unsigned __int8)(*(unsigned __int8 *)(v_r10 + a2 * 1 + 3)))) goto loc_005F6DA6;
    a2 = (a2) - (1);
    a3 = (unsigned int)((a3) - (1));
    if ((a1 + a2 * 1) > ((int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m148))))))))) goto loc_005F6D8E;
loc_005F6DA6:
    goto loc_005F6DB1;
loc_005F6DAC:
loc_005F6DB1:
    v_r10 = 0;
    goto loc_005F6D21;
loc_005F6DB9:
loc_005F6DBD:
loc_005F6DC2:
    if (v_stack_m80 <= 128) goto loc_005F6E51;
    if ((*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))) * 2 + 131072)) != 1) goto loc_005F6E51;
    if ((unsigned int)(a1) != 0) goto loc_005F6EC4;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m14C)))) >> (24));
    a3 = (((unsigned __int8)((unsigned int)(v_stack_m14C))) == ((unsigned __int8)(result))) ? 1 : 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m14C)))) >> (16));
    a1 = (((unsigned int)((unsigned __int16)((unsigned int)(v_stack_m14C)))) == ((unsigned int)(a2))) ? 1 : 0;
    if ((((unsigned int)(a1)) & ((unsigned int)(a3))) == 0) goto loc_005F6E4C;
    v_stack_m148 = 2;
    result = LZ4HC_countPattern(v_stack_m88 + 4, v_stack_m138, (unsigned int)((unsigned int)((unsigned int)(v_stack_m14C))), 1);
    result = ((unsigned int)((unsigned int)(result))) + (4);
    v_r10 = 0;
    v_stack_mE8 = result;
    goto loc_005F6ED4;
loc_005F6E4C:
    v_stack_m148 = (unsigned int)(v_r10 + 1);
loc_005F6E51:
loc_005F6E55:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))) - ((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p8 + a1 * 4))) * 2 + 131072))));
loc_005F6E6B:
    if (((unsigned int)(v_r13)) >= ((unsigned int)((unsigned int)(v_stack_m150)))) goto loc_005F6936;
loc_005F6E88:
loc_005F6E99:
    v_r10 = 0;
    v_stack_m54 = (unsigned int)((unsigned int)(v_stack_m158));
    v_stack_m58 = (unsigned int)((unsigned int)(v_stack_m120));
    v_stack_mC8 = v_stack_m58;
    goto loc_005F70B4;
loc_005F6EC4:
    v_stack_m148 = (unsigned int)((unsigned int)(v_stack_m120));
    if (((unsigned int)((unsigned int)(v_stack_m120))) != 2) goto loc_005F6E51;
loc_005F6ED4:
    if (((unsigned int)(v_stack_m118)) < ((unsigned int)((unsigned int)(v_stack_m150)))) goto loc_005F6E55;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mD0))) - ((unsigned int)(v_stack_m118)));
    result = (unsigned int)((result) - ((unsigned int)(v_stack_mC0)));
    if (((unsigned int)(result)) < 3) goto loc_005F6E55;
    if (((unsigned int)(v_stack_m118)) >= ((unsigned int)(v_stack_mD0))) goto loc_005F6F07;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m118))) - ((unsigned int)(v_r10 + 18)));
    v_rbx = (v_rbx) + (v_stack_mC8);
    goto loc_005F6F11;
loc_005F6F07:
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_stack_mD0)));
    v_rbx = (v_rbx) + (v_stack_m110);
loc_005F6F11:
    if ((*(unsigned int *)(v_rbx)) != ((unsigned int)((unsigned int)(v_stack_m14C)))) goto loc_005F6E51;
    v_r11 = v_stack_m138;
    if (0 != 0) { v_r11 = v_stack_mB0; }
    result = LZ4HC_countPattern(v_rbx + 4, v_r11, (unsigned int)((unsigned int)((unsigned int)(v_stack_m14C))), v_stack_mC0);
    v_rsi = ((unsigned int)((unsigned int)(result))) + (4);
    if (0 == 0) goto loc_005F6F7D;
    if ((v_rsi + v_rbx * 1) != v_r11) goto loc_005F6F77;
    a1 = (unsigned int)((v_rsi) & (3));
    a1 = (a1) << (3);
    if (a1 != 0) {
    }
    result = LZ4HC_countPattern(v_stack_m110, v_stack_m138, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m14C))))), v_stack_mC0);
    v_rsi = (v_rsi) + ((unsigned int)((unsigned int)(result)));
loc_005F6F77:
    goto loc_005F6F81;
loc_005F6F7D:
loc_005F6F81:
    result = LZ4HC_reverseCountPattern(v_rbx, v_stack_m110, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m14C))))), v_stack_mC0);
    a2 = 0;
    if (0 != 0) goto loc_005F6FD9;
    v_rbx = (v_rbx) - ((unsigned int)((unsigned int)(result)));
    if (v_rbx != v_stack_m110) goto loc_005F6FD9;
    if (v_stack_m154 >= ((unsigned int)(v_stack_mD0))) goto loc_005F6FD9;
    a1 = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))));
    a1 = (unsigned int)((a1) & (3));
    a1 = (a1) << (3);
    if (a1 != 0) {
    }
    result = LZ4HC_reverseCountPattern(v_stack_mB0, v_stack_mC8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m14C))))), v_stack_mC0);
    v_r11 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    a2 = 0;
loc_005F6FD9:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m118))) - ((unsigned int)(v_r11)));
    v_r13 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m150)));
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(v_stack_m150)))) { v_r13 = (unsigned int)(result); }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m118))) - ((unsigned int)(v_r13)));
    a1 = (a1) + (v_rsi);
    if (a1 < v_stack_mE8) goto loc_005F701F;
    if (v_rsi > v_stack_mE8) goto loc_005F701F;
    v_rsi = (unsigned int)((v_rsi) - ((unsigned int)(v_stack_mE8)));
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_stack_m118)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mD0))) - ((unsigned int)(v_rsi)));
    result = (unsigned int)((result) - 1);
    v_r13 = (unsigned int)((unsigned int)(v_stack_mD0));
    if (((unsigned int)(result)) >= 3) { v_r13 = (unsigned int)(v_rsi); }
    goto loc_005F6E6B;
loc_005F701F:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mD0))) - ((unsigned int)(v_r13)));
    result = (unsigned int)((result) - 1);
    if (((unsigned int)(result)) < 3) goto loc_005F709E;
    if (v_stack_mC0 != 0) goto loc_005F6E6B;
    a2 = v_stack_mE8;
    if (a1 < v_stack_mE8) { a2 = a1; }
    if (((int)(v_stack_m158)) >= a2) goto loc_005F707A;
    a1 = ((unsigned int)((unsigned int)(v_stack_mD0))) - ((unsigned int)((unsigned int)(v_r13)));
    a1 = (a1) - (v_stack_m110);
    a1 = (a1) + (v_stack_mE0);
    if (a1 > ((unsigned int)(0xFFFFULL))) goto loc_005F6E88;
    result = (unsigned int)(((unsigned int)(v_stack_m130)) - ((unsigned int)(v_r13)));
    v_stack_m158 = (unsigned int)(a2);
    v_stack_m120 = (unsigned int)(result);
    v_stack_mB8 = v_stack_mE0;
loc_005F707A:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)(v_r13) * 2 + 131072))) > ((unsigned int)(v_r13))) goto loc_005F6E88;
    v_r13 = (unsigned int)((v_r13) - ((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + (unsigned __int16)(v_r13) * 2 + 131072))));
    goto loc_005F6E6B;
loc_005F709E:
    goto loc_005F6E6B;
loc_005F70A6:
    v_stack_mC8 = 0;
    v_stack_mC4 = 0;
loc_005F70B4:
    if (0 <= ((unsigned int)(v_rsi))) goto loc_005F7542;
    if (v_stack_mB8 >= ((int)(a6) + (unsigned int)((unsigned int)(v_stack_mD0)) * 1 + 3)) goto loc_005F70FD;
    if (v_stack_mB8 >= ((int)(a6) + (unsigned int)((unsigned int)(v_stack_mD0)) * 1)) goto loc_005F734E;
    v_stack_m128 = v_stack_mC8;
    v_stack_mE0 = v_stack_mC8;
    v_stack_m118 = v_stack_mB8;
    goto loc_005F676E;
loc_005F70FD:
    if (v_stack_mB8 >= ((int)(a6) + (unsigned int)((unsigned int)(v_stack_mD0)) * 1)) goto loc_005F7175;
    result = (v_stack_mB8) - ((unsigned int)((unsigned int)(v_stack_mD0)));
    if (result >= v_r11) goto loc_005F7168;
    a4 = (int)(a6);
    if (((unsigned int)((int)(a6))) > ((unsigned int)(v_r11))) { a4 = (unsigned int)(v_r11); }
    a1 = ((int)((unsigned int)((unsigned int)(v_stack_m124)))) + (-4);
    a1 = (a1) + (v_stack_mB8);
    result = ((int)((unsigned int)(a4))) + ((unsigned int)((unsigned int)(v_stack_mD0)));
    v_stack_p30 = (unsigned int)(a4);
    if (result >= = a1) {
        a4 = (unsigned int)(v_stack_mB8);
        a4 = (unsigned int)((a4) - ((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0)))));
        a4 = (unsigned int)((a4) + (-4));
        a4 = (unsigned int)((a4) + ((unsigned int)((unsigned int)(v_stack_m124))));
        v_stack_p30 = (unsigned int)(a4);
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0))))) - ((unsigned int)(v_stack_mB8)));
    a1 = (unsigned int)((a1) + ((unsigned int)(a4)));
    if (condition_is_less_or_equal) goto loc_005F7175;
    v_r12 = (v_stack_mB8) + ((int)((unsigned int)(a1)));
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m124)) - ((unsigned int)(a1)));
    v_stack_m118 = v_r12;
    v_stack_m124 = (unsigned int)(v_rsi);
    goto loc_005F7175;
loc_005F7168:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0)))));
    v_stack_p30 = (unsigned int)(a4);
loc_005F7175:
    v_r14 = (v_stack_mD0) + (1);
    v_r12 = ((unsigned int)((unsigned int)(v_stack_mD0))) - (v_stack_m100);
    if (a7 == 0) goto loc_005F71C9;
    a2 = (v_stack_mB8) >> (7);
    result = (a2 + 8) + (v_r12);
    result = (result) + (v_r14);
    if (result > v_stack_mF0) goto loc_005F7A71;
loc_005F71C9:
    if (v_r12 < 15) goto loc_005F7224;
    *(unsigned __int8 *)(v_stack_mD0) = 240;
    v_rsi = 1;
    v_r10 = v_stack_mD0;
    v_r11 = v_stack_m100;
    v_r13 = v_r12 - 15;
    if ((v_r12 - 15) >= 255) {
        result = a1;
        a1 = v_r14;
        v_rsi = a2;
        a2 = 255;
        v_rsi = (v_rsi) >> (7);
        a3 = v_rsi;
        result = memset(a1, a2, a3, a4);
        v_r11 = v_stack_m100;
        v_r14 = (v_r14) + (v_rsi);
        result = (result) * (v_rsi);
        a3 = v_stack_mD0;
        v_r10 = v_stack_mD0;
        v_r13 = (v_r12 - 15) + (result);
        v_rsi = 1;
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(v_r13);
    v_r14 = (v_r14) + (v_rsi);
    goto loc_005F722D;
loc_005F7224:
    result = (unsigned __int8)(((unsigned __int8)(v_r12)) << (4));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
loc_005F722D:
    a2 = (v_r11) - (v_r14);
loc_005F723A:
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(a2 + v_r14 * 1);
    a1 = (v_r14) + (8);
    if (a1 < (v_r12 + v_r14 * 1)) goto loc_005F723A;
    v_r14 = (v_r14) + (v_r12);
    *(unsigned __int16 *)(v_r14) = (unsigned __int16)(v_stack_mF8);
    v_r14 = (v_r14) + (2);
    v_stack_mD0 = v_r14;
    if (a7 == 0) goto loc_005F729E;
    a2 = (a2) >> (7);
    result = (a2 + 6) + (v_r14);
    if (result > v_stack_mF0) goto loc_005F7A69;
loc_005F729E:
    if (((int)(a6) - 4) < 15) goto loc_005F7303;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r10)) + (15));
    a1 = ((int)(a6) - 4) - (15);
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
    if (a1 < 510) goto loc_005F72E0;
    a2 = (a2) >> (8);
    result = (v_r12) * (a2);
    a1 = (a1) + (result);
loc_005F72CD:
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (1);
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (1);
    a2 = (a2) - (1);
    if (condition_is_not_equal) goto loc_005F72CD;
loc_005F72E0:
    if (a1 >= 255) {
        a1 = (a1) - (255);
        *(unsigned __int8 *)(v_r14) = 255;
        v_r14 = (v_r14) + (1);
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a1);
    v_r14 = (v_r14) + (1);
    v_stack_mD0 = v_r14;
    goto loc_005F7308;
loc_005F7303:
    result = (unsigned __int8)((result) + ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
loc_005F7308:
    v_r13 = (v_stack_m140) + ((int)(a6));
    v_stack_mF8 = v_stack_m128;
    v_stack_m128 = v_stack_mA8;
    v_r10 = 0;
    v_stack_m100 = v_r13;
    v_stack_mE0 = v_stack_mA8;
    v_stack_m140 = v_stack_m118;
    v_stack_m118 = v_stack_mB8;
    v_stack_p30 = (unsigned int)((unsigned int)(v_stack_mF4));
    goto loc_005F6768;
loc_005F734E:
    if (v_stack_mB8 >= a1) goto loc_005F7384;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m118))) - ((unsigned int)(v_stack_mB8)));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(v_stack_mF4))));
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m124)) - ((unsigned int)(a1)));
    v_r12 = (v_stack_mB8) + ((int)((unsigned int)(a1)));
    v_stack_m124 = (unsigned int)(v_rsi);
    v_stack_m118 = v_r12;
    if (((unsigned int)(v_rsi)) >= 4) goto loc_005F737F;
    v_stack_m118 = a2;
    v_stack_m128 = v_stack_mA8;
    goto loc_005F7384;
loc_005F737F:
loc_005F7384:
    v_r14 = (v_r14) + (1);
    v_r12 = (v_stack_m118) - (v_stack_m100);
    if (a7 == 0) goto loc_005F73D8;
    a2 = (a2) >> (7);
    result = (a2 + 8) + (v_r12);
    result = (result) + (v_r14);
    if (result > v_stack_mF0) goto loc_005F7A71;
loc_005F73D8:
    if (v_r12 < 15) goto loc_005F7433;
    *(unsigned __int8 *)(v_r14) = 240;
    v_rsi = 1;
    v_r10 = v_r14;
    v_r11 = v_stack_m100;
    v_r13 = v_r12 - 15;
    if ((v_r12 - 15) >= 255) {
        result = a1;
        a1 = v_r14;
        v_rsi = a2;
        a2 = 255;
        v_rsi = (v_rsi) >> (7);
        a3 = v_rsi;
        result = memset(a1, a2, a3, (unsigned int)(v_stack_mF4));
        v_r11 = v_stack_m100;
        v_r14 = (v_r14) + (v_rsi);
        result = (result) * (v_rsi);
        a3 = v_r14;
        v_r10 = v_r14;
        v_r13 = (v_r12 - 15) + (result);
        v_rsi = 1;
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(v_r13);
    v_r14 = (v_r14) + (v_rsi);
    goto loc_005F743C;
loc_005F7433:
    result = (unsigned __int8)(((unsigned __int8)(v_r12)) << (4));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
loc_005F743C:
    a2 = (v_r11) - (v_r14);
loc_005F7449:
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(a2 + v_r14 * 1);
    a1 = (v_r14) + (8);
    if (a1 < (v_r12 + v_r14 * 1)) goto loc_005F7449;
    v_r14 = (v_r14) + (v_r12);
    *(unsigned __int16 *)(v_r14) = (unsigned __int16)(v_stack_mF8);
    v_r14 = (v_r14) + (2);
    v_stack_mD0 = v_r14;
    if (a7 == 0) goto loc_005F74AD;
    a2 = (a2) >> (7);
    result = (a2 + 6) + (v_r14);
    if (result > v_stack_mF0) goto loc_005F7A69;
loc_005F74AD:
    if (((int)(a6) - 4) < 15) goto loc_005F7512;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r10)) + (15));
    a1 = ((int)(a6) - 4) - (15);
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
    if (a1 < 510) goto loc_005F74EF;
    a2 = (a2) >> (8);
    result = (v_r12) * (a2);
    a1 = (a1) + (result);
loc_005F74DC:
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (1);
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (1);
    a2 = (a2) - (1);
    if (condition_is_not_equal) goto loc_005F74DC;
loc_005F74EF:
    if (a1 >= 255) {
        a1 = (a1) - (255);
        *(unsigned __int8 *)(v_r14) = 255;
        v_r14 = (v_r14) + (1);
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a1);
    v_r14 = (v_r14) + (1);
    v_stack_mD0 = v_r14;
    goto loc_005F7517;
loc_005F7512:
    result = (unsigned __int8)((result) + ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
loc_005F7517:
    v_r13 = (v_stack_m140) + ((int)(a6));
    v_stack_m100 = v_r13;
    v_stack_m140 = v_stack_mB8;
    v_stack_mF8 = v_stack_mA8;
    v_stack_mC0 = v_stack_m128;
    v_stack_mB0 = v_stack_m128;
    goto loc_005F5E07;
loc_005F7542:
    result = ((int)(a6)) + (v_stack_mB8);
    if (v_r12 < result) {
        result = (unsigned int)(v_r12);
        result = (unsigned int)((result) - ((unsigned int)(v_stack_mB8)));
        v_stack_p30 = (unsigned int)(result);
    }
    v_rsi = (v_stack_m140) - (v_stack_m100);
    v_r14 = (v_r14) + 1;
    if (a7 == ((unsigned int)(v_r10))) goto loc_005F75A9;
    a2 = (a2) >> (7);
    result = (a2 + 8) + (v_r14);
    result = (result) + (v_rsi);
    if (result > v_stack_mF0) goto loc_005F7A59;
loc_005F75A9:
    if (v_rsi < 15) goto loc_005F7603;
    *(unsigned __int8 *)(v_r14) = 240;
    v_rbx = v_stack_m100;
    v_r11 = v_stack_m140;
    v_r12 = v_rsi - 15;
    if ((v_rsi - 15) >= 255) {
        result = a3;
        a1 = v_r14;
        v_rbx = a2;
        a2 = 255;
        v_rbx = (v_rbx) >> (7);
        a3 = v_rbx;
        result = memset(a1, a2, a3, v_r14);
        v_r11 = v_stack_m140;
        v_r14 = (v_r14) + (v_rbx);
        result = (result) * (v_rbx);
        v_rbx = v_stack_m100;
        a4 = v_r14;
        v_r12 = (v_rsi - 15) + (result);
        v_r10 = 0;
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(v_r12);
    v_r14 = (v_r14) + 1;
    goto loc_005F760D;
loc_005F7603:
    result = (unsigned __int8)(((unsigned __int8)(v_rsi)) << (4));
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
loc_005F760D:
    a2 = (v_rbx) - (v_r14);
loc_005F761A:
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(a2 + v_r14 * 1);
    a1 = (v_r14) + (8);
    if (a1 < (v_r14 + v_rsi * 1)) goto loc_005F761A;
    v_r14 = (v_r14) + (v_rsi);
    *(unsigned __int16 *)(v_r14) = (unsigned __int16)(v_stack_mF8);
    v_r14 = (v_r14) + (2);
    if (a7 == 0) goto loc_005F7675;
    a2 = (a2) >> (7);
    result = (a2 + 6) + (v_r14);
    if (result > v_stack_mF0) goto loc_005F7A4C;
loc_005F7675:
    if (((int)(a6) - 4) < 15) goto loc_005F76E3;
    result = (unsigned __int8)((*(unsigned __int8 *)(a4)) + (15));
    a1 = ((int)(a6) - 4) - (15);
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
    if (a1 < 510) goto loc_005F76BF;
    a2 = (a2) >> (8);
    result = (v_rbx) * (a2);
    a1 = (a1) + (result);
loc_005F76AA:
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (1);
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (1);
    a2 = (a2) - (1);
    if (condition_is_not_equal) goto loc_005F76AA;
    goto loc_005F76C4;
loc_005F76BF:
loc_005F76C4:
    if (a1 >= 255) {
        a1 = (a1) - (255);
        *(unsigned __int8 *)(v_r14) = 255;
        v_r14 = (v_r14) + (1);
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a1);
    v_r14 = (v_r14) + (1);
    goto loc_005F76EE;
loc_005F76E3:
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a1);
loc_005F76EE:
    v_r11 = (v_r11) + ((int)(a6));
    v_stack_m140 = v_stack_m118;
    v_stack_m100 = v_r11;
    v_rsi = (v_stack_m118) - (v_r11);
    v_r14 = (v_r14) + (1);
    if (a7 == 0) goto loc_005F773D;
    a2 = (a2) >> (7);
    result = (a2 + 8) + (v_rsi);
    result = (result) + (v_r14);
    if (result > v_stack_mF0) goto loc_005F7A2E;
loc_005F773D:
    if (v_rsi < 15) goto loc_005F7796;
    *(unsigned __int8 *)(v_r14) = 240;
    v_rbx = 1;
    v_r12 = v_rsi - 15;
    if ((v_rsi - 15) >= 255) {
        result = (int)(a6);
        a1 = v_r14;
        v_rbx = a2;
        a2 = 255;
        v_rbx = (v_rbx) >> (7);
        a3 = v_rbx;
        result = memset(a1, a2, a3, v_r14);
        v_r11 = v_stack_m100;
        v_r14 = (v_r14) + (v_rbx);
        result = (result) * (v_rbx);
        a4 = v_r14;
        v_r12 = (v_rsi - 15) + (result);
        v_r10 = 0;
        v_rbx = v_r10 + 1;
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(v_r12);
    v_r14 = (v_r14) + (v_rbx);
    goto loc_005F77A0;
loc_005F7796:
    result = (unsigned __int8)(((unsigned __int8)(v_rsi)) << (4));
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
loc_005F77A0:
    a2 = (v_r11) - (v_r14);
loc_005F77AD:
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(a2 + v_r14 * 1);
    a1 = (v_r14) + (8);
    if (a1 < (v_rsi + v_r14 * 1)) goto loc_005F77AD;
    v_r14 = (v_r14) + (v_rsi);
    *(unsigned __int16 *)(v_r14) = (unsigned __int16)(v_stack_m128);
    v_r14 = (v_r14) + (2);
    v_stack_mD0 = v_r14;
    if (a7 == 0) goto loc_005F7808;
    a2 = (a2) >> (7);
    result = (a2 + 6) + (v_r14);
    if (result > v_stack_mF0) goto loc_005F7A38;
loc_005F7808:
    if (((int)(v_stack_m124) - 4) < 15) goto loc_005F7875;
    result = (unsigned __int8)((*(unsigned __int8 *)(a4)) + (15));
    a1 = ((int)(v_stack_m124) - 4) - (15);
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
    if (a1 < 510) goto loc_005F7852;
    a2 = (a2) >> (8);
    result = (result) * (a2);
    a1 = (a1) + (result);
loc_005F783F:
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (v_rbx);
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (v_rbx);
    a2 = (a2) - (v_rbx);
    if (condition_is_not_equal) goto loc_005F783F;
loc_005F7852:
    if (a1 >= 255) {
        a1 = (a1) - (255);
        *(unsigned __int8 *)(v_r14) = 255;
        v_r14 = (v_r14) + (v_rbx);
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a1);
    v_r14 = (v_r14) + (v_rbx);
    v_stack_mD0 = v_r14;
    goto loc_005F787B;
loc_005F7875:
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a1);
loc_005F787B:
    goto loc_005F7A1B;
loc_005F7884:
    v_rdi = (v_stack_m140) - (v_stack_m100);
    v_r14 = (v_r14) + (1);
    if (a7 == 0) goto loc_005F78D8;
    a2 = (a2) >> (7);
    result = (v_rdi + 8) + (a2);
    result = (result) + (v_r14);
    if (result > v_stack_mF0) goto loc_005F7A88;
loc_005F78D8:
    if (v_rdi < 15) goto loc_005F7931;
    *(unsigned __int8 *)(v_r14) = 240;
    v_rbx = 1;
    v_rsi = v_rdi - 15;
    v_r11 = v_stack_m100;
    if ((v_rdi - 15) >= 255) {
        result = (int)(v_stack_m124);
        a1 = v_r14;
        v_rbx = a2;
        a2 = 255;
        v_rbx = (v_rbx) >> (7);
        a3 = v_rbx;
        result = memset(a1, a2, a3, a4);
        a4 = a6;
        v_r14 = (v_r14) + (v_rbx);
        v_r11 = v_stack_m100;
        result = (result) * (v_rbx);
        v_rsi = (v_rdi - 15) + (result);
        v_r10 = 0;
        v_rbx = v_r10 + 1;
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(v_rsi);
    v_r14 = (v_r14) + (v_rbx);
    goto loc_005F793B;
loc_005F7931:
    result = (unsigned __int8)(((unsigned __int8)(v_rdi)) << (4));
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
loc_005F793B:
    a2 = (v_r11) - (v_r14);
loc_005F7948:
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(a2 + v_r14 * 1);
    a1 = (v_r14) + (8);
    if (a1 < (v_rdi + v_r14 * 1)) goto loc_005F7948;
    v_r14 = (v_r14) + (v_rdi);
    a1 = ((int)((unsigned int)(a4))) - (4);
    *(unsigned __int16 *)(v_r14) = (unsigned __int16)(v_stack_mF8);
    v_r14 = (v_r14) + (2);
    v_stack_mD0 = v_r14;
    if (a7 == 0) goto loc_005F79A3;
    a2 = (a2) >> (7);
    result = (a2 + 6) + (v_r14);
    if (result > v_stack_mF0) goto loc_005F7A83;
loc_005F79A3:
    if (a1 < 15) goto loc_005F7A0A;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r14)) + (15));
    a1 = (a1) - (15);
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
    if (a1 < 510) goto loc_005F79E7;
    a2 = (a2) >> (8);
    result = (v_rdi + v_r14 * 1) * (a2);
    a1 = (a1) + (result);
loc_005F79D4:
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (v_rbx);
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (v_rbx);
    a2 = (a2) - (v_rbx);
    if (condition_is_not_equal) goto loc_005F79D4;
loc_005F79E7:
    if (a1 >= 255) {
        a1 = (a1) - (255);
        *(unsigned __int8 *)(v_r14) = 255;
        v_r14 = (v_r14) + (v_rbx);
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a1);
    v_r14 = (v_r14) + (v_rbx);
    v_stack_mD0 = v_r14;
    goto loc_005F7A10;
loc_005F7A0A:
    result = (unsigned __int8)((result) + ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
loc_005F7A10:
    v_rdi = (v_stack_m140) + ((int)((unsigned int)(a4)));
loc_005F7A1B:
    v_stack_m100 = v_rdi;
    goto loc_005F5C32;
loc_005F7A2E:
    v_stack_m100 = v_rdi;
    goto loc_005F7A42;
loc_005F7A38:
loc_005F7A42:
    v_stack_mF8 = v_rdi;
    goto loc_005F7A83;
loc_005F7A4C:
    goto loc_005F7A74;
loc_005F7A59:
    goto loc_005F7A7E;
loc_005F7A69:
    v_r10 = 0;
    goto loc_005F7A7E;
loc_005F7A71:
    v_r10 = 0;
loc_005F7A74:
loc_005F7A7E:
loc_005F7A83:
loc_005F7A88:
    if (a7 != 2) goto loc_005F7C66;
    v_rdi = (v_stack_m140) - (v_rbx);
    a2 = (a2) >> (7);
    a3 = (v_rdi + 1) + (a2);
    if ((a3 + v_r14 * 1) > (v_stack_mF0 - 3)) goto loc_005F7C15;
    a1 = (v_stack_mF0 - 3) - (a3);
    a1 = (a1) - (v_r14);
    a1 = (a1) * (a1);
    a1 = (a1) + (18);
    a4 = (unsigned int)(a6);
    if (((int)((unsigned int)((unsigned int)(a6)))) > a1) { a4 = (unsigned int)(a1); }
    result = ((int)((unsigned int)(a4))) - (a3);
    v_stack_p30 = (unsigned int)(a4);
    result = (result) - (v_r14);
    result = (result) + (2);
    result = (result) + (v_stack_mF0);
    if (result < 12) goto loc_005F7C15;
    if (v_rdi < 15) goto loc_005F7B6B;
    *(unsigned __int8 *)(v_r14) = 240;
    v_rbx = 1;
    v_rsi = v_rdi - 15;
    v_r11 = v_rbx;
    v_r14 = v_r14 + 1;
    if ((v_rdi - 15) >= 255) {
        a1 = v_r14 + 1;
        v_rbx = a2;
        a2 = 255;
        v_rbx = (v_rbx) >> (7);
        a3 = v_rbx;
        result = memset(a1, a2, a3, a4);
        a4 = a6;
        v_r14 = (v_r14 + 1) + (v_rbx);
        v_r11 = v_stack_m100;
        result = (result) * (v_rbx);
        v_rbx = 1;
        v_rsi = (v_rdi - 15) + (result);
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(v_rsi);
    v_r14 = (v_r14) + (v_rbx);
    goto loc_005F7B74;
loc_005F7B6B:
    result = (unsigned __int8)(((unsigned __int8)(v_rdi)) << (4));
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
loc_005F7B74:
    v_r11 = (v_r11) - (v_r14);
loc_005F7B7E:
    *(unsigned __int64 *)(v_r14) = *(unsigned __int64 *)(v_r14 + v_r11 * 1);
    a1 = (v_r14) + (8);
    if (a1 < (v_rdi + v_r14 * 1)) goto loc_005F7B7E;
    v_r14 = (v_r14) + (v_rdi);
    a1 = ((int)((unsigned int)(a4))) - (4);
    *(unsigned __int16 *)(v_r14) = (unsigned __int16)(v_stack_mF8);
    v_r14 = (v_r14) + (2);
    if (a1 < 15) goto loc_005F7C01;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r14)) + (15));
    a1 = (a1) - (15);
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
    if (a1 < 510) goto loc_005F7BEB;
    a2 = (v_rdi + v_r14 * 1) >> (8);
    result = (result) * (a2);
    a1 = (a1) + (result);
loc_005F7BDA:
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (v_rbx);
    *(unsigned __int8 *)(v_r14) = 255;
    v_r14 = (v_r14) + (v_rbx);
    a2 = (a2) - (v_rbx);
    if (condition_is_not_equal) goto loc_005F7BDA;
loc_005F7BEB:
    if (a1 >= 255) {
        a1 = (a1) - (255);
        *(unsigned __int8 *)(v_r14) = 255;
        v_r14 = (v_r14) + (v_rbx);
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(a1);
    v_r14 = (v_r14) + (v_rbx);
    goto loc_005F7C06;
loc_005F7C01:
    result = (unsigned __int8)((result) + ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
loc_005F7C06:
    v_r11 = ((int)((unsigned int)(a4))) + (v_stack_m140);
    v_stack_m100 = v_r11;
    v_r10 = 0;
loc_005F7C15:
loc_005F7C2E:
    v_rbx = (v_stack_m98) - (v_r11);
    v_stack_m98 = v_rbx;
    a2 = (a2) >> (7);
    if (a7 != 2) goto loc_005F7C6E;
    v_rsi = (v_stack_mF0) + (5);
    goto loc_005F7C77;
loc_005F7C66:
    goto loc_005F7D3C;
loc_005F7C6E:
    if (a7 == 0) goto loc_005F7CB4;
loc_005F7C77:
    result = (v_rbx + 1) + (a2);
    result = (result) + (0);
    if (result <= v_rsi) goto loc_005F7CB9;
    if (a7 != 1) goto loc_005F7C97;
    goto loc_005F7D41;
loc_005F7C97:
    v_rbx = (v_rsi) - (0);
    v_rbx = (v_rbx) - (1);
    result = (v_rbx + 241) >> (8);
    v_rbx = (v_rbx) - (result);
    v_stack_m98 = v_rbx;
    goto loc_005F7CB9;
loc_005F7CB4:
loc_005F7CB9:
    if (v_rbx < 15) goto loc_005F7D11;
    *(unsigned __int8 *)(0) = 240;
    v_r14 = (0) + (1);
    v_rdi = v_rbx - 15;
    if ((v_rbx - 15) >= 255) {
        result = a4;
        a1 = v_r14;
        v_rbx = a2;
        a2 = 255;
        v_rbx = (v_rbx) >> (7);
        a3 = v_rbx;
        result = memset(a1, a2, a3, a4);
        v_r11 = v_stack_m100;
        v_r14 = (v_r14) + (v_rbx);
        result = (result) * (v_rbx);
        v_rbx = v_stack_m98;
        v_rdi = (v_rbx - 15) + (result);
    }
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(v_rdi);
    v_r14 = (v_r14) + 1;
    goto loc_005F7D1C;
loc_005F7D11:
    result = (unsigned __int8)(((unsigned __int8)(v_rbx)) << (4));
    *(unsigned __int8 *)(v_r14) = (unsigned __int8)(result);
    v_r14 = (v_r14) + (a1);
loc_005F7D1C:
    result = memcpy(v_r14 + 1, v_r11, v_rbx, a4);
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(v_stack_p18)));
    v_rsi = (unsigned int)((v_rbx + v_r11 * 1) - ((unsigned int)(v_stack_p10)));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_rbx)));
    *(unsigned int *)(v_stack_p20) = (unsigned int)(v_rsi);
    if (condition_is_greater) goto loc_005F7D4E;
loc_005F7D3C:
loc_005F7D41:
    *(unsigned __int8 *)(v_stack_p8 + 262183) = 1;
loc_005F7D4E:
loc_005F7D51:
    goto loc_005F7D79;
loc_005F7D56:
    v_stack_m168 = (unsigned int)((unsigned int)(a7));
    v_stack_m178 = (unsigned int)((unsigned int)(a5));
    result = LZ4HC_compress_generic_dictCtx(v_stack_p8, v_r11, v_rbx, v_stack_p20);
loc_005F7D79:
    v_rsp = (v_rsp) + (344);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t LZ4HC_compress_generic(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4, void *Arg5, void *Arg6, uint32_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m124;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint32_t v_stack_m168;
    uint32_t v_stack_m178;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p8;

    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (344);
    local_r10 = 0;
    if ((*(uint64_t *)(arg1 + 0x40028)) != 0) goto loc_005F7D56;
    if (Arg7 != 2) goto loc_005F56AC;
    if (Arg5 < ((uint32_t)(local_r10 + 1))) goto loc_005F7D51;
loc_005F56AC:
    if (((uint32_t)((int32_t)(*(uint32_t *)(arg4)))) > 0x7E000000ULL) goto loc_005F7D51;
    Arg1 = ((int32_t)(Arg5)) + (Arg3);
    result = (*(uint64_t *)(v_rip - 0x5BF2EF)) >> (32);
    v_stack_m80 = result;
    local_rsi = Arg1 - 5;
    if (Arg7 != 2) { local_rsi = Arg1; }
    v_stack_m78 = v_xmm0;
    v_stack_mF0 = local_rsi;
    v_stack_m140 = Arg2;
    v_stack_m100 = Arg2;
    v_stack_m98 = Arg2 + (int32_t)(*(uint32_t *)(arg4)) * 1;
    v_stack_mA8 = Arg2 + (int32_t)(*(uint32_t *)(arg4)) * 1 - 12;
    v_stack_m138 = Arg2 + (int32_t)(*(uint32_t *)(arg4)) * 1 - 5;
    v_stack_mD0 = Arg3;
    v_stack_m118 = 0;
    v_stack_mB8 = 0;
    *(uint32_t *)(arg4) = 0;
    if (((uint32_t)((int32_t)(*(uint32_t *)(arg4)))) < 13) goto loc_005F7C2E;
loc_005F5740:
    if (Arg2 > (Arg2 + (int32_t)(*(uint32_t *)(arg4)) * 1 - 12)) goto loc_005F7C15;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(*(uint64_t *)(arg1 + 0x40008))));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018)))));
    v_stack_m150 = 3;
    v_stack_mE8 = *(uint64_t *)(arg1 + 0x40008);
    v_stack_m120 = (uint32_t)(local_r15);
    v_stack_m130 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4001C)));
    local_rbx = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4001C))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4001C)) + 65536)) <= ((uint32_t)(local_r15))) {
        local_rbx = local_r15 - 65535;
    }
    Arg4 = ((uint32_t)(*(uint32_t *)(arg1 + 0x40018))) - ((uint32_t)(*(uint32_t *)(arg1 + 0x4001C)));
    Arg4 = (Arg4) + (*(uint64_t *)(arg1 + 0x40010));
    v_stack_m108 = (uint32_t)((uint32_t)(v_stack_m74));
    v_stack_mC0 = Arg4;
    v_stack_mE0 = *(uint64_t *)(arg1 + 0x40010);
    v_stack_m158 = (uint32_t)(local_rbx);
    v_stack_p30 = 0;
    v_stack_mF8 = 0;
    v_stack_m110 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020)))) >= ((uint32_t)(local_r15))) goto loc_005F5835;
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))))) - ((uint32_t)(*(uint32_t *)(arg1 + 0x40018)));
    Arg3 = (Arg3) + (*(uint64_t *)(arg1 + 0x40008));
loc_005F57F1:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4001C))) * (*(uint32_t *)(Arg3)));
    Arg2 = (Arg2) >> (17);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))))) - (*(uint32_t *)(v_stack_p8 + arg2 * 4)));
    if (Arg1 > ((uint32_t)(0xFFFFULL))) { Arg1 = (uint32_t)(0xFFFFULL); }
    Arg3 = (Arg3) + (1);
    *(uint16_t *)(v_stack_p8 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))) * 2 + 0x20000) = (uint16_t)(Arg1);
    *(uint32_t *)(v_stack_p8 + arg2 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020)));
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))) + (1));
    if (((uint32_t)(Arg4)) < ((uint32_t)(local_r15))) goto loc_005F57F1;
loc_005F5835:
    *(uint32_t *)(v_stack_p8 + 0x40020) = (uint32_t)(local_r15);
    Arg1 = (uint32_t)((Arg1) * (*(uint32_t *)(arg2)));
    Arg1 = (Arg1) >> (17);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))) < ((uint32_t)((uint32_t)(v_stack_m158)))) goto loc_005F5C01;
loc_005F585E:
    Arg4 = 0;
    if (condition_is_less_or_equal) goto loc_005F5BED;
    result = (uint32_t)(((uint32_t)(v_stack_m108)) - 1);
    v_stack_m108 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018))))) goto loc_005F59F4;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018)))));
    Arg2 = (Arg2) + (v_stack_mE8);
    if ((*(uint16_t *)((int32_t)((uint32_t)((uint32_t)(v_stack_m150))) + v_stack_m140 * 1 - 0x1)) != ((uint16_t)(*(uint16_t *)((int32_t)((uint32_t)((uint32_t)(v_stack_m150))) + arg2 * 1 - 0x1)))) goto loc_005F5964;
    if ((*(uint32_t *)(arg2)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_005F5964;
    local_r10 = (v_stack_m140) + (4);
    Arg2 = (Arg2) + (4);
    if (local_r10 >= (v_stack_m138 - 7)) goto loc_005F58D9;
    Arg3 = (*(uint64_t *)(local_r10)) ^ (*(uint64_t *)(arg2));
    if (condition_is_not_equal) goto loc_005F58CF;
    goto loc_005F58EA;
loc_005F58CF:
    Arg1 = (uint32_t)((local_r10 + 8) >> (3));
    goto loc_005F5940;
loc_005F58D9:
    if (Arg1 >= (v_stack_m138 - 7)) goto loc_005F58FF;
    Arg3 = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(arg2));
    if (condition_is_not_equal) goto loc_005F58F0;
    Arg1 = (Arg1) + (8);
loc_005F58EA:
    Arg2 = (Arg2) + (8);
    goto loc_005F58D9;
loc_005F58F0:
    result = (uint32_t)((*(uint16_t *)((int32_t)((uint32_t)((uint32_t)(v_stack_m150))) + arg2 * 1 - 0x1)) >> (3));
    result = (uint32_t)((result) - ((uint32_t)(local_r10)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_005F5940;
loc_005F58FF:
    if (Arg1 >= (v_stack_m138 - 3)) goto loc_005F5916;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (Arg2) + (4);
    }
    if (Arg1 >= (v_stack_m138 - 1)) goto loc_005F592F;
    if ((*(uint16_t *)(arg2)) == ((uint16_t)(*(uint16_t *)(arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= v_stack_m138) goto loc_005F593D;
    if ((*(uint8_t *)(arg2)) == ((uint8_t)(*(uint8_t *)(arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r10)));
loc_005F5940:
    Arg1 = (uint32_t)((Arg1) + (4));
    if (((uint32_t)(Arg1)) >= = ((uint32_t)((uint32_t)(v_stack_m150)))) {
        local_r10 = (uint32_t)(local_r15);
        v_stack_m150 = (uint32_t)(Arg1);
        local_r10 = (uint32_t)((local_r10) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))));
        v_stack_m110 = (uint32_t)(local_r10);
    }
    Arg4 = 0;
loc_005F5964:
    if (v_stack_m80 <= 128) goto loc_005F5BB5;
    if ((*(uint16_t *)(v_stack_p8 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))) * 2 + 0x20000)) != 1) goto loc_005F5BB5;
    if ((uint32_t)((uint32_t)(Arg6)) != 0) goto loc_005F5C40;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) >> (24));
    Arg3 = (((uint8_t)((uint32_t)(*(uint32_t *)(arg2)))) == ((uint8_t)(result))) ? 1 : 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) >> (16));
    Arg1 = (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(arg2))))) == ((uint32_t)(Arg2))) ? 1 : 0;
    if ((((uint32_t)(Arg1)) & ((uint32_t)(Arg3))) == 0) goto loc_005F5BAE;
    v_stack_p30 = 2;
    result = LZ4HC_countPattern(v_stack_m140 + 4, v_stack_m138, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))), Arg4);
    local_rbx = ((uint32_t)((uint32_t)(result))) + (4);
    v_stack_mF8 = local_rbx;
    Arg4 = 0;
    goto loc_005F5C4F;
loc_005F59F4:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))))) - ((uint32_t)(v_stack_m138)));
    Arg2 = ((uint32_t)((uint32_t)(result))) + (v_stack_mE0);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018)) - 4))) goto loc_005F5BA7;
    if ((*(uint32_t *)(arg2)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_005F5BA7;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))));
    Arg3 = (Arg3) + (v_stack_m140);
    if (Arg3 > v_stack_m138) { Arg3 = v_stack_m138; }
    Arg2 = (Arg2) + (4);
    if ((v_stack_m140 + 4) >= (Arg3 - 7)) goto loc_005F5A5A;
    Arg4 = (*(uint64_t *)(v_stack_m140 + 0x4)) ^ (*(uint64_t *)(arg2));
    if (condition_is_not_equal) goto loc_005F5A50;
    goto loc_005F5A6B;
loc_005F5A50:
    Arg1 = (uint32_t)((v_stack_m140 + 4 + 8) >> (3));
    goto loc_005F5ABF;
loc_005F5A5A:
    if (Arg1 >= (Arg3 - 7)) goto loc_005F5A7F;
    Arg4 = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(arg2));
    if (condition_is_not_equal) goto loc_005F5A71;
    Arg1 = (Arg1) + (8);
loc_005F5A6B:
    Arg2 = (Arg2) + (8);
    goto loc_005F5A5A;
loc_005F5A71:
    result = (uint32_t)((v_stack_m140) >> (3));
    result = (uint32_t)((result) - ((uint32_t)(v_stack_m140 + 4)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_005F5ABF;
loc_005F5A7F:
    if (Arg1 >= (Arg3 - 3)) goto loc_005F5A96;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (Arg2) + (4);
    }
    if (Arg1 >= (Arg3 - 1)) goto loc_005F5AAF;
    if ((*(uint16_t *)(arg2)) == ((uint16_t)(*(uint16_t *)(arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= Arg3) goto loc_005F5ABD;
    if ((*(uint8_t *)(arg2)) == ((uint8_t)(*(uint8_t *)(arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_m140 + 4)));
loc_005F5ABF:
    Arg4 = ((int32_t)((uint32_t)(Arg1 + 4))) + (v_stack_m140);
    if (Arg4 != Arg3) goto loc_005F5B82;
    if (Arg3 >= v_stack_m138) goto loc_005F5B82;
    local_r10 = (v_stack_m138) + (-7);
    if (Arg4 >= local_r10) goto loc_005F5B05;
    Arg2 = (*(uint64_t *)(arg4)) ^ (*(uint64_t *)(v_stack_mE8));
    if (condition_is_not_equal) goto loc_005F5B1C;
loc_005F5B05:
    if ((Arg4 + 8) >= local_r10) goto loc_005F5B35;
    Arg3 = (*(uint64_t *)(arg4 + 0x8)) ^ (*(uint64_t *)(v_stack_mE8 + 0x8));
    if (condition_is_not_equal) goto loc_005F5B26;
    Arg1 = (Arg4 + 8) + (8);
    Arg2 = (v_stack_mE8 + 8) + (8);
    goto loc_005F5B05;
loc_005F5B1C:
    Arg1 = (uint32_t)((Arg1) >> (3));
    goto loc_005F5B7B;
loc_005F5B26:
    result = (uint32_t)((*(uint8_t *)(arg1)) >> (3));
    result = (uint32_t)((result) - ((uint32_t)(Arg4)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_005F5B7B;
loc_005F5B35:
    if (Arg1 >= (v_stack_m138 - 3)) goto loc_005F5B51;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (Arg2) + (4);
    }
    if (Arg1 >= (v_stack_m138 - 1)) goto loc_005F5B6A;
    if ((*(uint16_t *)(arg2)) == ((uint16_t)(*(uint16_t *)(arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= v_stack_m138) goto loc_005F5B78;
    if ((*(uint8_t *)(arg2)) == ((uint8_t)(*(uint8_t *)(arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg4)));
loc_005F5B7B:
    local_rbx = (uint32_t)((Arg1 + 4) + ((uint32_t)(Arg1)));
loc_005F5B82:
    result = *(uint8_t *)(arg1);
    if (((uint32_t)(local_rbx)) >= = ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)) - 1))) {
        result = 1;
        v_stack_m150 = (uint32_t)(local_rbx);
        result = (uint32_t)((result) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))));
        v_stack_m110 = (uint32_t)(result);
    }
    Arg4 = 0;
loc_005F5B9D:
    goto loc_005F5964;
loc_005F5BA7:
    goto loc_005F5B9D;
loc_005F5BAE:
    v_stack_p30 = 1;
loc_005F5BB5:
loc_005F5BBA:
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))) - ((uint32_t)(*(uint16_t *)(v_stack_p8 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))) * 2 + 0x20000))));
loc_005F5BD0:
    if (((uint32_t)(local_r11)) >= ((uint32_t)((uint32_t)(v_stack_m158)))) goto loc_005F585E;
loc_005F5BED:
loc_005F5C01:
    v_stack_m64 = (uint32_t)((uint32_t)(v_stack_m150));
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m110));
    v_stack_mC0 = v_stack_m68;
    result = (v_stack_m68) >> (32);
    v_stack_mF8 = v_stack_m68;
    if (((uint32_t)(result)) >= 4) goto loc_005F5DFB;
    local_rdi = (v_stack_m140) + 1;
    local_r10 = 0;
loc_005F5C32:
    v_stack_m140 = local_rdi;
    goto loc_005F5740;
loc_005F5C40:
    v_stack_p30 = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) != 2) goto loc_005F5BB5;
loc_005F5C4F:
    if (((uint32_t)(v_stack_mF0)) < ((uint32_t)((uint32_t)(v_stack_m158)))) goto loc_005F5BBA;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018))))) - ((uint32_t)(v_stack_mF0)));
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(v_stack_m120))));
    if (((uint32_t)(result)) < 3) goto loc_005F5BBA;
    if (((uint32_t)(v_stack_mF0)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018))))) goto loc_005F5C7F;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mF0))) - (v_stack_m130));
    local_rbx = (local_rbx) + (v_stack_mE0);
    goto loc_005F5C88;
loc_005F5C7F:
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018)))));
    local_rbx = (local_rbx) + (v_stack_mD0);
loc_005F5C88:
    if ((*(uint32_t *)(local_rbx)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_005F5BBA;
    local_r11 = v_stack_m138;
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) != 0) { local_r11 = v_stack_mC0; }
    result = LZ4HC_countPattern(local_rbx + 4, local_r11, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))), v_stack_p8);
    local_rdi = ((uint32_t)((uint32_t)(result))) + (4);
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) == 0) goto loc_005F5CEF;
    if ((local_rdi + local_rbx * 1) != local_r11) goto loc_005F5CE9;
    Arg1 = (uint32_t)((local_rdi) & (3));
    Arg1 = (Arg1) << (3);
    if (Arg1 != NULL) {
    }
    result = LZ4HC_countPattern(v_stack_mD0, v_stack_m138, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))), v_stack_p8);
    local_rdi = (local_rdi) + ((uint32_t)((uint32_t)(result)));
loc_005F5CE9:
    goto loc_005F5CF2;
loc_005F5CEF:
loc_005F5CF2:
    result = LZ4HC_reverseCountPattern(local_rbx, v_stack_mD0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))), v_stack_p8);
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))) != 0) goto loc_005F5D3B;
    local_rbx = (local_rbx) - ((uint32_t)((uint32_t)(result)));
    if (local_rbx != v_stack_mD0) goto loc_005F5D3B;
    if (v_stack_m130 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018))))) goto loc_005F5D3B;
    Arg1 = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))));
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (Arg1) << (3);
    if (Arg1 != NULL) {
    }
    result = LZ4HC_reverseCountPattern(v_stack_mC0, v_stack_mE0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))), v_stack_p8);
    local_r11 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
loc_005F5D3B:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mF0))) - ((uint32_t)(local_r11)));
    local_r11 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m158)));
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(v_stack_m158)))) { local_r11 = (uint32_t)(result); }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mF0))) - ((uint32_t)(local_r11)));
    Arg1 = (Arg1) + (local_rdi);
    if (Arg1 < v_stack_mF8) goto loc_005F5D7F;
    if (local_rdi > v_stack_mF8) goto loc_005F5D7F;
    local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(v_stack_mF8)));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(v_stack_mF0)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018))))) - ((uint32_t)(local_rdi)));
    result = (uint32_t)((result) - 1);
    local_r11 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018))));
    if (((uint32_t)(result)) >= 3) { local_r11 = (uint32_t)(local_rdi); }
    goto loc_005F5BD0;
loc_005F5D7F:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018))))) - ((uint32_t)(local_r11)));
    result = (uint32_t)((result) - 1);
    if (((uint32_t)(result)) < 3) goto loc_005F5DF3;
    Arg2 = v_stack_mF8;
    if (Arg1 < v_stack_mF8) { Arg2 = Arg1; }
    if (((int32_t)(v_stack_m150)) >= Arg2) goto loc_005F5DCF;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x40018))) - ((uint32_t)((uint32_t)(local_r11)));
    Arg1 = (Arg1) - (v_stack_mD0);
    Arg1 = (Arg1) + (v_stack_m140);
    if (Arg1 > ((uint32_t)(0xFFFFULL))) goto loc_005F5BED;
    result = (uint32_t)(((uint32_t)(v_stack_m120)) - ((uint32_t)(local_r11)));
    v_stack_m150 = (uint32_t)(Arg2);
    v_stack_m110 = (uint32_t)(result);
loc_005F5DCF:
    if (((uint32_t)(*(uint16_t *)(v_stack_p8 + (uint16_t)(local_r11) * 2 + 0x20000))) > ((uint32_t)(local_r11))) goto loc_005F5BED;
    local_r11 = (uint32_t)((local_r11) - ((uint32_t)(*(uint16_t *)(v_stack_p8 + (uint16_t)(local_r11) * 2 + 0x20000))));
    goto loc_005F5BD0;
loc_005F5DF3:
    goto loc_005F5BD0;
loc_005F5DFB:
    v_stack_mB0 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40018))));
loc_005F5E07:
    v_stack_mE8 = v_stack_m140;
loc_005F5E0F:
    v_stack_p30 = (uint32_t)((int32_t)(v_stack_mF4));
    if (((int32_t)(v_stack_mF4) + v_stack_m140 * 1) > v_stack_mA8) goto loc_005F6704;
    result = ((int32_t)(v_stack_mF4) + v_stack_m140 * 1) + (-2);
    v_stack_m150 = (uint32_t)((int32_t)(v_stack_mF4));
    v_stack_m118 = result;
    v_stack_mA0 = result;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40018))))) - ((uint32_t)(*(uint64_t *)(v_stack_p8 + 0x40008))));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(result)));
    v_stack_m110 = *(uint64_t *)(v_stack_p8 + 0x40008);
    v_stack_m154 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40018)));
    v_stack_m130 = (uint32_t)(local_rdi);
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4001C)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4001C)) + 65536)) <= ((uint32_t)(local_rdi))) goto loc_005F5E84;
    v_stack_m148 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4001C)));
    goto loc_005F5E8E;
loc_005F5E84:
    v_stack_m148 = (uint32_t)(local_rdi - 65535);
loc_005F5E8E:
    Arg4 = (*(uint64_t *)(v_stack_p8 + 0x40010)) - ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4001C)));
    v_stack_m128 = *(uint64_t *)(v_stack_p8 + 0x40010);
    Arg4 = (Arg4) + ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40018)));
    v_stack_m90 = Arg4;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (v_stack_m140));
    Arg4 = 0;
    v_stack_mD8 = (uint32_t)((uint32_t)(v_stack_m74));
    v_stack_m158 = 0;
    v_stack_m88 = 0;
    v_stack_m120 = 0;
    v_stack_m14C = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020)))) >= ((uint32_t)(local_rdi))) goto loc_005F5F4C;
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))))) - ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40018)));
    Arg3 = (Arg3) + (*(uint64_t *)(v_stack_p8 + 0x40008));
loc_005F5F00:
    Arg2 = (uint32_t)((*(uint64_t *)(v_stack_p8 + 0x40010)) * (*(uint32_t *)(Arg3)));
    Arg2 = (Arg2) >> (17);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))))) - (*(uint32_t *)(v_stack_p8 + arg2 * 4)));
    if (Arg1 > ((uint32_t)(0xFFFFULL))) { Arg1 = (uint32_t)(0xFFFFULL); }
    Arg3 = (Arg3) + (1);
    *(uint16_t *)(v_stack_p8 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))) * 2 + 0x20000) = (uint16_t)(Arg1);
    *(uint32_t *)(v_stack_p8 + arg2 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020)));
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))) + (1));
    if (((uint32_t)(Arg4)) < ((uint32_t)(local_rdi))) goto loc_005F5F00;
    goto loc_005F5F53;
loc_005F5F4C:
loc_005F5F53:
    *(uint32_t *)(v_stack_p8 + 0x40020) = (uint32_t)(local_rdi);
    Arg1 = (uint32_t)((Arg1) * (*(uint32_t *)(result)));
    v_stack_mE0 = (int32_t)((uint32_t)(local_r10));
    Arg1 = (Arg1) >> (17);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))) < v_stack_m148) goto loc_005F64F8;
    v_stack_m118 = v_stack_m118;
loc_005F5F8B:
    local_r12 = 0;
    v_stack_m110 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m158))));
    if (condition_is_less_or_equal) goto loc_005F64EB;
    result = (uint32_t)(((uint32_t)(v_stack_mD8)) - ((uint32_t)(local_r12 + 1)));
    v_stack_mD8 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))) < ((uint32_t)((uint32_t)(v_stack_m154)))) goto loc_005F617E;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))))) - ((uint32_t)((uint32_t)(v_stack_m154))));
    result = (result + v_stack_m110 * 1) - ((int32_t)((uint32_t)(local_r10)));
    if ((*(uint16_t *)((int32_t)((uint32_t)((uint32_t)(v_stack_m150))) + v_stack_m140 * 1 - 0x1)) != ((uint16_t)(*(uint16_t *)(result + (int32_t)((uint32_t)((uint32_t)(v_stack_m150))) * 1 - 0x1)))) goto loc_005F6404;
    if ((*(uint32_t *)(result + v_stack_m110 * 1)) != ((uint32_t)((uint32_t)(v_stack_m14C)))) goto loc_005F6404;
    if ((int32_t)((uint32_t)(local_r10)) == 0) goto loc_005F605C;
    Arg1 = (v_stack_m140) - (v_stack_mA0);
    result = (v_stack_m110) - (result + v_stack_m110 * 1);
    if (Arg1 <= result) goto loc_005F6010;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m140))) - ((uint32_t)(v_stack_mA0)));
    goto loc_005F6015;
loc_005F6010:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m110))) - ((uint32_t)(result + v_stack_m110 * 1)));
loc_005F6015:
    Arg2 = (uint32_t)(-((uint32_t)((uint32_t)(Arg1))));
    local_r10 = (v_stack_mA0) - (result + v_stack_m110 * 1);
loc_005F6023:
    if (((uint32_t)(Arg2)) <= 3) goto loc_005F6083;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10 + result + v_stack_m110 * 1 - 0x4 * 1))) ^ (*(uint32_t *)(result + v_stack_m110 * 1 - 0x4)));
    if (condition_is_not_equal) goto loc_005F6042;
    local_r15 = (uint32_t)((0) - (4));
    Arg2 = (uint32_t)((Arg2) - (4));
    local_rbx = (0) - (4);
    Arg4 = (result + v_stack_m110 * 1 - 4) - (4);
    goto loc_005F6023;
loc_005F6042:
    v_stack_mA0 = 0;
    Arg1 = (uint32_t)((31) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) >> (3));
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)(Arg1)));
loc_005F6057:
loc_005F605C:
    if ((v_stack_mA0 + 4) >= (v_stack_m138 - 7)) goto loc_005F60D8;
    Arg3 = (*(uint64_t *)(v_stack_mA0 + 0x4)) ^ (*(uint64_t *)(result + v_stack_m110 * 1 + 0x4));
    if (condition_is_not_equal) goto loc_005F60CE;
    goto loc_005F60E9;
loc_005F6083:
    if (1 <= ((int32_t)((uint32_t)(v_stack_mA0 + 4 + 8)))) goto loc_005F6057;
    Arg1 = (v_stack_m110 - 1) + (1);
    Arg4 = ((int32_t)(Arg6)) - (v_stack_m110);
    Arg4 = (Arg4) - ((uint32_t)((uint32_t)(result)));
    Arg4 = (Arg4) + (v_stack_m140);
    Arg2 = (1) - (v_stack_m110);
    Arg1 = (Arg1) + ((uint32_t)((uint32_t)(result)));
    Arg2 = (Arg2) - ((uint32_t)((uint32_t)(result)));
loc_005F60B4:
    if ((*(uint8_t *)(arg4 + arg1 * 1 - 0x2)) != ((uint8_t)(*(uint8_t *)(arg1)))) goto loc_005F605C;
    Arg1 = (Arg1) - (1);
    local_r15 = (uint32_t)((local_r15) - (1));
    if ((Arg2 + Arg1 * 1) > ((int32_t)((uint32_t)(v_stack_mA0 + 4 + 8)))) goto loc_005F60B4;
    goto loc_005F605C;
loc_005F60CE:
    Arg1 = (uint32_t)((Arg1) >> (3));
    goto loc_005F613F;
loc_005F60D8:
    if (Arg1 >= Arg4) goto loc_005F60FE;
    Arg3 = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(arg2));
    if (condition_is_not_equal) goto loc_005F60EF;
    Arg1 = (Arg1) + (8);
loc_005F60E9:
    Arg2 = (Arg2) + (8);
    goto loc_005F60D8;
loc_005F60EF:
    result = (uint32_t)((Arg2 + Arg1 * 1) >> (3));
    result = (uint32_t)((result) - ((uint32_t)(v_stack_mA0 + 4)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_005F613F;
loc_005F60FE:
    if (Arg1 >= (v_stack_m138 - 3)) goto loc_005F6115;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (Arg2) + (4);
    }
    if (Arg1 >= (v_stack_m138 - 1)) goto loc_005F612E;
    if ((*(uint16_t *)(arg2)) == ((uint16_t)(*(uint16_t *)(arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= v_stack_m138) goto loc_005F613C;
    if ((*(uint8_t *)(arg2)) == ((uint8_t)(*(uint8_t *)(arg1)))) {
        Arg1 = (Arg1) + (1);
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_mA0 + 4)));
loc_005F613F:
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r15)));
    Arg1 = (uint32_t)((Arg1) + (4));
    if (((uint32_t)(Arg1)) <= v_stack_m150) goto loc_005F6412;
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m130)) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))));
    result = ((int32_t)((uint32_t)(local_r15))) + (v_stack_mA0);
    v_stack_m150 = (uint32_t)(Arg1);
    v_stack_m118 = result;
    v_stack_m120 = (uint32_t)(local_r12);
    goto loc_005F641F;
loc_005F617E:
    result = (uint32_t)((result) - (v_stack_m108));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))) > ((uint32_t)((uint32_t)(v_stack_m154) - 4))) goto loc_005F641A;
    if ((*(uint32_t *)(result + arg2 * 1)) != ((uint32_t)((uint32_t)(v_stack_m14C)))) goto loc_005F641A;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m154)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))));
    local_r10 = (local_r10) + (v_stack_mA0);
    if (local_r10 > v_stack_m138) { local_r10 = v_stack_m138; }
    if ((v_stack_mA0 + 4) >= (local_r10 - 7)) goto loc_005F61DE;
    Arg3 = (*(uint64_t *)(v_stack_mA0 + 0x4)) ^ (*(uint64_t *)(result + arg2 * 1 + 0x4));
    if (condition_is_not_equal) goto loc_005F61D4;
    goto loc_005F61EF;
loc_005F61D4:
    Arg1 = (uint32_t)((v_stack_mA0 + 4 + 8) >> (3));
    goto loc_005F6243;
loc_005F61DE:
    if (Arg1 >= (local_r10 - 7)) goto loc_005F6203;
    Arg3 = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(result + arg2 * 1 + 0x4));
    if (condition_is_not_equal) goto loc_005F61F5;
    Arg1 = (Arg1) + (8);
loc_005F61EF:
    Arg2 = (result + Arg2 * 1 + 4) + (8);
    goto loc_005F61DE;
loc_005F61F5:
    result = (uint32_t)(((uint32_t)(v_stack_m154) - 4) >> (3));
    result = (uint32_t)((result) - ((uint32_t)(v_stack_mA0 + 4)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_005F6243;
loc_005F6203:
    if (Arg1 >= (local_r10 - 3)) goto loc_005F621A;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (Arg2) + (4);
    }
    if (Arg1 >= (local_r10 - 1)) goto loc_005F6233;
    if ((*(uint16_t *)(arg2)) == ((uint16_t)(*(uint16_t *)(arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= local_r10) goto loc_005F6241;
    if ((*(uint8_t *)(arg2)) == ((uint8_t)(*(uint8_t *)(arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_mA0 + 4)));
loc_005F6243:
    local_rbx = ((int32_t)((uint32_t)(Arg1 + 4))) + (v_stack_mA0);
    if (local_rbx != local_r10) goto loc_005F62F8;
    if (local_r10 >= v_stack_m138) goto loc_005F62F8;
    if (local_rbx >= (v_stack_m138 - 7)) goto loc_005F6282;
    Arg1 = (*(uint64_t *)(v_stack_m110)) ^ (*(uint64_t *)(local_rbx));
    if (condition_is_not_equal) goto loc_005F6299;
loc_005F6282:
    if ((local_rbx + 8) >= (v_stack_m138 - 7)) goto loc_005F62B1;
    Arg3 = (*(uint64_t *)(local_rbx + 0x8)) ^ (*(uint64_t *)(v_stack_m110 + 0x8));
    if (condition_is_not_equal) goto loc_005F62A3;
    Arg1 = (local_rbx + 8) + (8);
    Arg2 = (v_stack_m110 + 8) + (8);
    goto loc_005F6282;
loc_005F6299:
    Arg1 = (uint32_t)((Arg1) >> (3));
    goto loc_005F62F6;
loc_005F62A3:
    result = (uint32_t)((*(uint8_t *)(arg1)) >> (3));
    result = (uint32_t)((result) - ((uint32_t)(local_rbx)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_005F62F6;
loc_005F62B1:
    if (Arg1 >= (v_stack_m138 - 3)) goto loc_005F62CD;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (Arg2) + (4);
    }
    if (Arg1 >= (v_stack_m138 - 1)) goto loc_005F62E6;
    if ((*(uint16_t *)(arg2)) == ((uint16_t)(*(uint16_t *)(arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= v_stack_m138) goto loc_005F62F4;
    if ((*(uint8_t *)(arg2)) == ((uint8_t)(*(uint8_t *)(arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_rbx)));
loc_005F62F6:
    local_rsi = (uint32_t)((Arg1 + 4) + ((uint32_t)(Arg1)));
loc_005F62F8:
    result = 0;
    if (v_stack_mE0 == 0) goto loc_005F63D4;
    Arg1 = (v_stack_m128) - (result + Arg2 * 1);
    result = (v_stack_m140) - (v_stack_mA0);
    if (result <= Arg1) goto loc_005F632B;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m140))) - ((uint32_t)(v_stack_mA0)));
    goto loc_005F6331;
loc_005F632B:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m128))) - ((uint32_t)(result + Arg2 * 1)));
loc_005F6331:
    Arg4 = (uint32_t)(-((uint32_t)((uint32_t)(Arg1))));
    local_rbx = (v_stack_mA0) - (result + Arg2 * 1);
loc_005F6341:
    if (((uint32_t)(Arg4)) <= 3) goto loc_005F637E;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + result + arg2 * 1 - 0x4 * 1))) ^ (*(uint32_t *)(result + arg2 * 1 - 0x4)));
    if (condition_is_not_equal) goto loc_005F6361;
    Arg2 = (uint32_t)((0) - (4));
    Arg4 = (uint32_t)((Arg4) - (4));
    local_rdi = (0) - (4);
    local_r10 = (result + Arg2 * 1 - 4) - (4);
    goto loc_005F6341;
loc_005F6361:
    local_r12 = 0;
    v_stack_mA0 = 0;
    Arg1 = (uint32_t)((local_r12 + 31) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) >> (3));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(Arg1)));
    goto loc_005F63DA;
loc_005F637E:
    if (((uint32_t)(v_stack_m130)) <= ((int32_t)((uint32_t)(Arg1)))) goto loc_005F63CB;
    result = ((int32_t)(Arg6)) - (v_stack_m128);
    result = (result) - (0);
    local_r10 = (v_stack_m140) + (result);
    Arg3 = (1) - (v_stack_m128);
    Arg1 = ((uint32_t)(v_stack_m130) - 1) + (result + Arg2 * 1);
    Arg3 = (Arg3) - (0);
loc_005F63B4:
    if ((*(uint8_t *)(local_r10 + arg1 * 1 - 0x2)) != ((uint8_t)(*(uint8_t *)(arg1)))) goto loc_005F63CB;
    Arg1 = (Arg1) - (1);
    Arg2 = (uint32_t)((Arg2) - (1));
    if ((Arg3 + Arg1 * 1) > ((int32_t)((uint32_t)(Arg1)))) goto loc_005F63B4;
loc_005F63CB:
    local_r12 = 0;
    goto loc_005F63DA;
loc_005F63D4:
    local_r12 = 0;
loc_005F63DA:
    local_rsi = (uint32_t)((local_rsi) - (0));
    if (((uint32_t)(local_rsi)) <= v_stack_m150) goto loc_005F6407;
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m130)) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))));
    result = ((int32_t)(0)) + (v_stack_mA0);
    v_stack_m150 = (uint32_t)(local_rsi);
    v_stack_m118 = result;
    v_stack_m120 = (uint32_t)(local_rdi);
    goto loc_005F6407;
loc_005F6404:
loc_005F6407:
    goto loc_005F6422;
loc_005F6412:
    goto loc_005F6422;
loc_005F641A:
loc_005F641F:
    local_r12 = 0;
loc_005F6422:
    if (v_stack_m80 <= 128) goto loc_005F64B2;
    if ((*(uint16_t *)(v_stack_p8 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))) * 2 + 0x20000)) != 1) goto loc_005F64B2;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m110)))) != 0) goto loc_005F6529;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m14C)))) >> (24));
    Arg3 = (((uint8_t)((uint32_t)(v_stack_m14C))) == ((uint8_t)(result))) ? 1 : 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m14C)))) >> (16));
    Arg1 = (((uint32_t)((uint16_t)((uint32_t)(v_stack_m14C)))) == ((uint32_t)(Arg2))) ? 1 : 0;
    if ((((uint32_t)(Arg1)) & ((uint32_t)(Arg3))) == 0) goto loc_005F64A8;
    v_stack_m158 = 2;
    result = LZ4HC_countPattern(v_stack_mA0 + 4, v_stack_m138, (uint32_t)((uint32_t)((uint32_t)(v_stack_m14C))), 1);
    result = ((uint32_t)((uint32_t)(result))) + (4);
    v_stack_m88 = result;
    goto loc_005F6532;
loc_005F64A8:
    v_stack_m158 = 1;
loc_005F64B2:
loc_005F64B6:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))) - ((uint32_t)(*(uint16_t *)(v_stack_p8 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))) * 2 + 0x20000))));
loc_005F64CC:
    if (((uint32_t)(local_r13)) >= ((uint32_t)((uint32_t)(v_stack_m148)))) goto loc_005F5F8B;
loc_005F64EB:
loc_005F64F8:
    local_r10 = 0;
    v_stack_m5C = (uint32_t)((uint32_t)(v_stack_m150));
    v_stack_m60 = (uint32_t)((uint32_t)(v_stack_m120));
    v_stack_m128 = v_stack_m60;
    goto loc_005F6712;
loc_005F6529:
    v_stack_m158 = (uint32_t)(v_stack_mE8);
    if (((uint32_t)(v_stack_mE8)) != 2) goto loc_005F64B2;
loc_005F6532:
    if (((uint32_t)((uint32_t)(v_stack_m150))) < ((uint32_t)((uint32_t)(v_stack_m148)))) goto loc_005F64B6;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m154)))) - ((uint32_t)((uint32_t)(v_stack_m150))));
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(Arg6))));
    if (((uint32_t)(result)) < 3) goto loc_005F64B6;
    if (((uint32_t)((uint32_t)(v_stack_m150))) >= ((uint32_t)((uint32_t)(v_stack_m154)))) goto loc_005F656B;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m150)))) - (v_stack_m108));
    local_rbx = (local_rbx) + (v_stack_m128);
    goto loc_005F6571;
loc_005F656B:
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)((uint32_t)(v_stack_m154))));
    local_rbx = (local_rbx) + (v_stack_mD0);
loc_005F6571:
    if ((*(uint32_t *)(local_rbx)) != ((uint32_t)((uint32_t)(v_stack_m124)))) goto loc_005F64B2;
    local_rdi = v_stack_m60;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6)))) != 0) { local_rdi = v_stack_m90; }
    result = LZ4HC_countPattern(local_rbx + 4, local_rdi, (uint32_t)((uint32_t)((uint32_t)(v_stack_m124))), (uint32_t)(Arg6));
    local_rsi = ((uint32_t)((uint32_t)(result))) + (4);
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6)))) == 0) goto loc_005F65D4;
    if ((local_rsi + local_rbx * 1) != local_rdi) goto loc_005F65CD;
    Arg1 = (uint32_t)((local_rsi) & (3));
    Arg1 = (Arg1) << (3);
    if (Arg1 != NULL) {
    }
    result = LZ4HC_countPattern(v_stack_mD0, v_stack_m138, (uint32_t)(v_stack_m14C), (uint32_t)(Arg6));
    local_rsi = (local_rsi) + ((uint32_t)((uint32_t)(result)));
loc_005F65CD:
    goto loc_005F65D7;
loc_005F65D4:
loc_005F65D7:
    result = LZ4HC_reverseCountPattern(local_rbx, v_stack_mD0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m14C))), (uint32_t)(Arg6));
    Arg2 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg6)))) != 0) goto loc_005F6634;
    local_rbx = (local_rbx) - ((uint32_t)((uint32_t)(result)));
    if (local_rbx != v_stack_mD0) goto loc_005F6634;
    if (v_stack_m108 >= ((uint32_t)((uint32_t)(v_stack_m154)))) goto loc_005F6634;
    Arg1 = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))));
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (Arg1) << (3);
    if (Arg1 != NULL) {
    }
    result = LZ4HC_reverseCountPattern(v_stack_m90, v_stack_m128, (uint32_t)((uint32_t)((uint32_t)(v_stack_m14C))), (uint32_t)(Arg6));
    local_rdi = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    Arg2 = 0;
loc_005F6634:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m150)))) - ((uint32_t)(local_rdi)));
    local_r13 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m148)));
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(v_stack_m148)))) { local_r13 = (uint32_t)(result); }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m150)))) - ((uint32_t)(local_r13)));
    Arg1 = (Arg1) + (local_rsi);
    if (Arg1 < v_stack_m88) goto loc_005F667A;
    if (local_rsi > v_stack_m88) goto loc_005F667A;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m150)) - ((uint32_t)(v_stack_m88)));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(local_rsi)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m154)))) - ((uint32_t)(local_r15)));
    result = (uint32_t)((result) - 1);
    local_r13 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m154)));
    if (((uint32_t)(result)) >= 3) { local_r13 = (uint32_t)(local_r15); }
    goto loc_005F64CC;
loc_005F667A:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m154)))) - ((uint32_t)(local_r13)));
    result = (uint32_t)((result) - 1);
    if (((uint32_t)(result)) < 3) goto loc_005F66FC;
    if (v_stack_mE0 != 0) goto loc_005F64CC;
    Arg2 = v_stack_m88;
    if (Arg1 < v_stack_m88) { Arg2 = Arg1; }
    if (((int32_t)(v_stack_m150)) >= Arg2) goto loc_005F66D8;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m154)))) - ((uint32_t)((uint32_t)(local_r13)));
    Arg1 = (Arg1) - (v_stack_mD0);
    Arg1 = (Arg1) + (v_stack_mC0);
    if (Arg1 > ((uint32_t)(0xFFFFULL))) goto loc_005F64EB;
    result = (uint32_t)(((uint32_t)(v_stack_m130)) - ((uint32_t)(local_r13)));
    v_stack_m150 = (uint32_t)(Arg2);
    v_stack_m120 = (uint32_t)(result);
    v_stack_m118 = v_stack_mC0;
loc_005F66D8:
    if (((uint32_t)(*(uint16_t *)(v_stack_p8 + (uint16_t)(local_r13) * 2 + 0x20000))) > ((uint32_t)(local_r13))) goto loc_005F64EB;
    local_r13 = (uint32_t)((local_r13) - ((uint32_t)(*(uint16_t *)(v_stack_p8 + (uint16_t)(local_r13) * 2 + 0x20000))));
    goto loc_005F64CC;
loc_005F66FC:
    goto loc_005F64CC;
loc_005F6704:
    local_r10 = 0;
    v_stack_m128 = 0;
loc_005F6712:
    v_stack_mE0 = 0;
    if (0 <= ((uint32_t)(v_stack_m88))) goto loc_005F7884;
    if ((*(uint16_t *)(v_stack_p8 + (uint16_t)(local_r13) * 2 + 0x20000)) >= ((uint32_t)((uint32_t)((uint32_t)(v_stack_m154))))) goto loc_005F674B;
    result = ((int32_t)(v_stack_mAC)) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_m154))));
    local_r13 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m154)));
    if (v_stack_m118 < result) {
        v_stack_mF8 = v_stack_mC0;
        local_r13 = *(uint16_t *)(v_stack_p8 + (uint16_t)(local_r13) * 2 + 0x20000);
        Arg4 = v_stack_mF4;
        v_stack_p30 = (uint32_t)(Arg4);
        v_stack_m140 = *(uint16_t *)(v_stack_p8 + (uint16_t)(local_r13) * 2 + 0x20000);
    }
    result = (v_stack_m118) - (local_r13);
    if (result >= 3) goto loc_005F6768;
    v_stack_m140 = v_stack_m118;
    v_stack_mF8 = 0;
    goto loc_005F5E0F;
loc_005F6768:
loc_005F676E:
    result = (v_stack_m118) - (v_stack_m118);
    if (result >= 18) goto loc_005F67CB;
    Arg3 = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(Arg4)) > 18) { Arg3 = 18; }
    Arg1 = ((int32_t)(0)) + (-4);
    Arg1 = (Arg1) + (v_stack_m118);
    Arg2 = ((int32_t)((uint32_t)(Arg3))) + (v_stack_m118);
    if (Arg2 >= = Arg1) {
        Arg3 = (uint32_t)(v_stack_m118);
        Arg3 = (uint32_t)((Arg3) - ((uint32_t)(v_stack_m118)));
        Arg3 = (uint32_t)((Arg3) + (-4));
        Arg3 = (uint32_t)((Arg3) + (0));
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m118))) - ((uint32_t)(v_stack_m118)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg3)));
    local_rsi = 0;
    local_rdi = 0;
    local_r12 = v_stack_m118;
    if (!(condition_is_less_or_equal)) {
        result = (int32_t)((uint32_t)(Arg1));
        local_r12 = (v_stack_m118) + (result);
        local_rsi = (uint32_t)((0) - ((uint32_t)(Arg1)));
        v_stack_m118 = local_r12;
        v_stack_m124 = (uint32_t)(local_rsi);
        local_rdi = v_stack_m128;
        v_stack_mE0 = local_rdi;
    }
    Arg1 = ((int32_t)((uint32_t)(local_rsi))) + (local_r12);
    if (Arg1 > ((uint32_t)(v_stack_m148))) goto loc_005F70A6;
    v_stack_mB8 = Arg1 - 3;
    v_stack_m88 = Arg1 - 3;
    v_stack_m158 = (uint32_t)(local_rsi);
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(Arg1 - 3))) - ((uint32_t)(*(uint64_t *)(v_stack_p8 + 0x40008))));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40018)))));
    v_stack_m110 = *(uint64_t *)(v_stack_p8 + 0x40008);
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40018)));
    v_stack_m130 = (uint32_t)(local_r13);
    v_stack_m154 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4001C)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4001C)) + 65536)) <= ((uint32_t)(local_r13))) goto loc_005F6833;
    v_stack_m150 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4001C)));
    goto loc_005F683E;
loc_005F6833:
    v_stack_m150 = (uint32_t)(local_r13 - 65535);
loc_005F683E:
    Arg4 = ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40018))) - ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4001C)));
    Arg4 = (Arg4) + (*(uint64_t *)(v_stack_p8 + 0x40010));
    v_stack_mB0 = Arg4;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(Arg1 - 3))) - (v_stack_m118));
    Arg4 = 0;
    v_stack_mD8 = (uint32_t)((uint32_t)(v_stack_m74));
    v_stack_m148 = 0;
    v_stack_mE8 = 0;
    v_stack_m120 = 0;
    v_stack_mC8 = *(uint64_t *)(v_stack_p8 + 0x40010);
    v_stack_m14C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 - 0x3)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020)))) >= ((uint32_t)(local_r13))) goto loc_005F68F0;
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))))) - ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40018)));
    Arg3 = (Arg3) + (*(uint64_t *)(v_stack_p8 + 0x40008));
loc_005F68A9:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4001C))) * (*(uint32_t *)(Arg3)));
    Arg2 = (Arg2) >> (17);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))))) - (*(uint32_t *)(v_stack_p8 + arg2 * 4)));
    if (Arg1 > ((uint32_t)(0xFFFFULL))) { Arg1 = (uint32_t)(0xFFFFULL); }
    Arg3 = (Arg3) + (1);
    *(uint16_t *)(v_stack_p8 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))) * 2 + 0x20000) = (uint16_t)(Arg1);
    *(uint32_t *)(v_stack_p8 + arg2 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020)));
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40020))) + (1));
    if (((uint32_t)(Arg4)) < ((uint32_t)(local_r13))) goto loc_005F68A9;
loc_005F68F0:
    *(uint32_t *)(v_stack_p8 + 0x40020) = (uint32_t)(local_r13);
    Arg1 = (uint32_t)((Arg1) * (*(uint32_t *)(v_stack_m88)));
    Arg1 = (Arg1) >> (17);
    v_stack_mC0 = (int32_t)((uint32_t)(local_r10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))) < v_stack_m150) goto loc_005F6E99;
    v_stack_mB8 = v_stack_mB8;
    v_stack_m90 = (int32_t)((uint32_t)(local_rsi));
loc_005F6936:
    local_r10 = 0;
    if (condition_is_less_or_equal) goto loc_005F6E88;
    result = (uint32_t)(((uint32_t)(v_stack_mD8)) - 1);
    v_stack_mD8 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))) < ((uint32_t)((uint32_t)(v_stack_m108)))) goto loc_005F6B2B;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))))) - ((uint32_t)((uint32_t)(v_stack_m108))));
    local_rbx = (local_rbx) + (v_stack_m110);
    result = ((int32_t)(v_stack_m158)) - ((int32_t)((uint32_t)(local_r10)));
    if ((*(uint16_t *)((int32_t)(v_stack_m158) + v_stack_m118 * 1 - 0x1)) != ((uint16_t)(*(uint16_t *)(result + local_rbx * 1 - 0x1)))) goto loc_005F6DB9;
    if ((*(uint32_t *)(local_rbx)) != ((uint32_t)((uint32_t)(v_stack_m14C)))) goto loc_005F6DB9;
    if ((int32_t)((uint32_t)(local_r10)) == 0) goto loc_005F6A57;
    Arg1 = (v_stack_m110) - (local_rbx);
    result = (v_stack_m118) - (v_stack_m88);
    if (result <= Arg1) goto loc_005F69B4;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m118))) - ((uint32_t)(v_stack_m88)));
    goto loc_005F69B9;
loc_005F69B4:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m110))) - ((uint32_t)(local_rbx)));
loc_005F69B9:
    Arg2 = (uint32_t)(-((uint32_t)((uint32_t)(Arg1))));
    local_r10 = (local_rbx) - (v_stack_m88);
loc_005F69C7:
    if (((uint32_t)(Arg2)) <= 3) goto loc_005F69FB;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10 + v_stack_m88 - 0x4 * 1))) ^ (*(uint32_t *)(v_stack_m88 - 0x4)));
    if (condition_is_not_equal) goto loc_005F69E5;
    local_rsi = (uint32_t)((0) - (4));
    Arg2 = (uint32_t)((Arg2) - (4));
    local_r11 = (0) - (4);
    Arg4 = (v_stack_m88 - 4) - (4);
    goto loc_005F69C7;
loc_005F69E5:
    Arg1 = (uint32_t)((31) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) >> (3));
    local_rsi = (uint32_t)((local_rsi) - ((uint32_t)(Arg1)));
    goto loc_005F6A52;
loc_005F69FB:
    if (local_r11 <= ((int32_t)((uint32_t)(Arg1)))) goto loc_005F6A52;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))))) - ((uint32_t)((uint32_t)(v_stack_m108))));
    Arg4 = (Arg4) - (v_stack_m90);
    Arg1 = (4) - (v_stack_m90);
    Arg4 = (Arg4) - (v_stack_m118);
    Arg4 = (Arg4) + (v_stack_m110);
    Arg2 = (v_stack_m118 - 4) + (local_r11 + v_stack_m90 * 1);
    Arg1 = (Arg1) - (v_stack_m118);
loc_005F6A36:
    if ((*(uint8_t *)(arg2)) != ((uint8_t)(*(uint8_t *)(arg4 + arg2 * 1 + 0x3)))) goto loc_005F6A4E;
    Arg2 = (Arg2) - (1);
    local_rsi = (uint32_t)((local_rsi) - (1));
    if ((Arg1 + Arg2 * 1) > ((int32_t)((uint32_t)(Arg1)))) goto loc_005F6A36;
loc_005F6A4E:
loc_005F6A52:
loc_005F6A57:
    Arg4 = (v_stack_m138) + (-7);
    if ((v_stack_m88 + 4) >= Arg4) goto loc_005F6A88;
    Arg3 = (*(uint64_t *)(v_stack_m88 + 0x4)) ^ (*(uint64_t *)(local_rbx + 0x4));
    if (condition_is_not_equal) goto loc_005F6A7E;
    goto loc_005F6A99;
loc_005F6A7E:
    Arg1 = (uint32_t)((v_stack_m88 + 4 + 8) >> (3));
    goto loc_005F6AF4;
loc_005F6A88:
    if (Arg1 >= Arg4) goto loc_005F6AAE;
    Arg3 = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(local_rbx + 0x4));
    if (condition_is_not_equal) goto loc_005F6A9F;
    Arg1 = (Arg1) + (8);
loc_005F6A99:
    Arg2 = (local_rbx + 4) + (8);
    goto loc_005F6A88;
loc_005F6A9F:
    result = (uint32_t)((Arg1 + Arg2 * 1) >> (3));
    result = (uint32_t)((result) - ((uint32_t)(v_stack_m88 + 4)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_005F6AF4;
loc_005F6AAE:
    if (Arg1 >= (v_stack_m138 - 3)) goto loc_005F6ACA;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (Arg2) + (4);
    }
    if (Arg1 >= (v_stack_m138 - 1)) goto loc_005F6AE3;
    if ((*(uint16_t *)(arg2)) == ((uint16_t)(*(uint16_t *)(arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= v_stack_m138) goto loc_005F6AF1;
    if ((*(uint8_t *)(arg2)) == ((uint8_t)(*(uint8_t *)(arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_m88 + 4)));
loc_005F6AF4:
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_rsi)));
    Arg1 = (uint32_t)((Arg1) + (4));
    result = *(uint8_t *)(arg1);
    if (((uint32_t)(Arg1)) >= = ((uint32_t)((uint32_t)(v_stack_m158)))) {
        result = v_stack_m130;
        result = (uint32_t)((result) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))));
        v_stack_m158 = (uint32_t)(Arg1);
        v_stack_m120 = (uint32_t)(result);
        result = (int32_t)((uint32_t)(local_rsi));
        result = (result) + (v_stack_m88);
        v_stack_mB8 = result;
    }
    local_r10 = 0;
    goto loc_005F6DC2;
loc_005F6B2B:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))))) - ((uint32_t)(Arg2)));
    local_rsi = (local_rsi) + (v_stack_m138);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))) > ((uint32_t)((uint32_t)(v_stack_m108) - 4))) goto loc_005F6DBD;
    if ((*(uint32_t *)(local_rsi)) != ((uint32_t)((uint32_t)(v_stack_m14C)))) goto loc_005F6DBD;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m108)))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))));
    local_r10 = (local_r10) + (v_stack_m88);
    if (local_r10 > v_stack_m138) { local_r10 = v_stack_m138; }
    if ((v_stack_m88 + 4) >= (local_r10 - 7)) goto loc_005F6B88;
    Arg3 = (*(uint64_t *)(v_stack_m88 + 0x4)) ^ (*(uint64_t *)(local_rsi + 0x4));
    if (condition_is_not_equal) goto loc_005F6B7E;
    goto loc_005F6B99;
loc_005F6B7E:
    Arg1 = (uint32_t)((v_stack_m88 + 4 + 8) >> (3));
    goto loc_005F6BEF;
loc_005F6B88:
    if (Arg1 >= (local_r10 - 7)) goto loc_005F6BAE;
    Arg3 = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(local_rsi + 0x4));
    if (condition_is_not_equal) goto loc_005F6B9F;
    Arg1 = (Arg1) + (8);
loc_005F6B99:
    Arg2 = (local_rsi + 4) + (8);
    goto loc_005F6B88;
loc_005F6B9F:
    result = (uint32_t)(((uint32_t)(v_stack_m108) - 4) >> (3));
    result = (uint32_t)((result) - ((uint32_t)(v_stack_m88 + 4)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_005F6BEF;
loc_005F6BAE:
    if (Arg1 >= (local_r10 - 3)) goto loc_005F6BC5;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (Arg2) + (4);
    }
    if (Arg1 >= (local_r10 - 1)) goto loc_005F6BDE;
    if ((*(uint16_t *)(arg2)) == ((uint16_t)(*(uint16_t *)(arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= local_r10) goto loc_005F6BEC;
    if ((*(uint8_t *)(arg2)) == ((uint8_t)(*(uint8_t *)(arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_m88 + 4)));
loc_005F6BEF:
    local_r11 = ((int32_t)((uint32_t)(Arg1 + 4))) + (v_stack_m88);
    if (local_r11 != local_r10) goto loc_005F6CA8;
    if (local_r10 >= v_stack_m138) goto loc_005F6CA8;
    if (local_r11 >= (v_stack_m138 - 7)) goto loc_005F6C30;
    Arg2 = (*(uint64_t *)(local_r11)) ^ (*(uint64_t *)(v_stack_m110));
    if (condition_is_not_equal) goto loc_005F6C47;
loc_005F6C30:
    if ((local_r11 + 8) >= (v_stack_m138 - 7)) goto loc_005F6C60;
    Arg3 = (*(uint64_t *)(local_r11 + 0x8)) ^ (*(uint64_t *)(v_stack_m110 + 0x8));
    if (condition_is_not_equal) goto loc_005F6C51;
    Arg1 = (local_r11 + 8) + (8);
    Arg2 = (v_stack_m110 + 8) + (8);
    goto loc_005F6C30;
loc_005F6C47:
    Arg1 = (uint32_t)((Arg1) >> (3));
    goto loc_005F6CA6;
loc_005F6C51:
    result = (uint32_t)((*(uint8_t *)(arg1)) >> (3));
    result = (uint32_t)((result) - ((uint32_t)(local_r11)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_005F6CA6;
loc_005F6C60:
    if (Arg1 >= (v_stack_m138 - 3)) goto loc_005F6C7C;
    if ((*(uint32_t *)(arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) {
        Arg1 = (Arg1) + (4);
        Arg2 = (Arg2) + (4);
    }
    if (Arg1 >= (v_stack_m138 - 1)) goto loc_005F6C95;
    if ((*(uint16_t *)(arg2)) == ((uint16_t)(*(uint16_t *)(arg1)))) {
        Arg1 = (Arg1) + (2);
        Arg2 = (Arg2) + (2);
    }
    if (Arg1 >= v_stack_m138) goto loc_005F6CA3;
    if ((*(uint8_t *)(arg2)) == ((uint8_t)(*(uint8_t *)(arg1)))) {
        Arg1 = (Arg1) + 1;
    }
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r11)));
loc_005F6CA6:
    local_rbx = (uint32_t)((Arg1 + 4) + ((uint32_t)(Arg1)));
loc_005F6CA8:
    local_r10 = 0;
    if (v_stack_mC0 == 0) goto loc_005F6D1C;
    Arg1 = (v_stack_mC8) - (local_rsi);
    result = (v_stack_m118) - (v_stack_m88);
    if (result <= Arg1) goto loc_005F6CD6;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m118))) - ((uint32_t)(v_stack_m88)));
    goto loc_005F6CDB;
loc_005F6CD6:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mC8))) - ((uint32_t)(local_rsi)));
loc_005F6CDB:
    Arg2 = (uint32_t)(-((uint32_t)((uint32_t)(Arg1))));
    local_rsi = (local_rsi) - (v_stack_m88);
loc_005F6CE6:
    if (((uint32_t)(Arg2)) <= 3) goto loc_005F6D4C;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + v_stack_m88 - 0x4 * 1))) ^ (*(uint32_t *)(v_stack_m88 - 0x4)));
    if (condition_is_not_equal) goto loc_005F6D05;
    Arg3 = (uint32_t)((0) - (4));
    Arg2 = (uint32_t)((Arg2) - (4));
    local_r11 = (0) - (4);
    local_r10 = (v_stack_m88 - 4) - (4);
    goto loc_005F6CE6;
loc_005F6D05:
    local_r10 = 0;
    v_stack_mA0 = 0;
    Arg1 = (uint32_t)((local_r10 + 31) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) >> (3));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)(Arg1)));
loc_005F6D1C:
loc_005F6D21:
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(Arg3)));
    if (((uint32_t)(local_rbx)) >= = v_stack_m158) {
        result = v_stack_m130;
        result = (uint32_t)((result) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4)))));
        v_stack_m158 = (uint32_t)(local_rbx);
        v_stack_m120 = (uint32_t)(result);
        result = (int32_t)((uint32_t)(Arg3));
        result = (result) + (v_stack_m88);
        v_stack_mB8 = result;
    }
    goto loc_005F6DC2;
loc_005F6D4C:
    if (((uint32_t)(v_stack_m154)) <= ((int32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m148))))))))) goto loc_005F6DAC;
    Arg2 = (v_stack_m118) + (-4);
    Arg1 = (4) - (v_stack_m90);
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))))) - ((uint32_t)((uint32_t)(v_stack_m154))));
    Arg2 = (Arg2) + ((uint32_t)(v_stack_m154) + v_stack_m90 * 1);
    local_r10 = (local_r10) - (v_stack_m90);
    local_r10 = (local_r10) - (v_stack_m118);
    local_r10 = (local_r10) + (v_stack_mC8);
    Arg1 = (Arg1) - (v_stack_m118);
loc_005F6D8E:
    if ((*(uint8_t *)(arg2)) != ((uint8_t)(*(uint8_t *)(local_r10 + arg2 * 1 + 0x3)))) goto loc_005F6DA6;
    Arg2 = (Arg2) - (1);
    Arg3 = (uint32_t)((Arg3) - (1));
    if ((Arg1 + Arg2 * 1) > ((int32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m148))))))))) goto loc_005F6D8E;
loc_005F6DA6:
    goto loc_005F6DB1;
loc_005F6DAC:
loc_005F6DB1:
    local_r10 = 0;
    goto loc_005F6D21;
loc_005F6DB9:
loc_005F6DBD:
loc_005F6DC2:
    if (v_stack_m80 <= 128) goto loc_005F6E51;
    if ((*(uint16_t *)(v_stack_p8 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))) * 2 + 0x20000)) != 1) goto loc_005F6E51;
    if ((uint32_t)(Arg1) != 0) goto loc_005F6EC4;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m14C)))) >> (24));
    Arg3 = (((uint8_t)((uint32_t)(v_stack_m14C))) == ((uint8_t)(result))) ? 1 : 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m14C)))) >> (16));
    Arg1 = (((uint32_t)((uint16_t)((uint32_t)(v_stack_m14C)))) == ((uint32_t)(Arg2))) ? 1 : 0;
    if ((((uint32_t)(Arg1)) & ((uint32_t)(Arg3))) == 0) goto loc_005F6E4C;
    v_stack_m148 = 2;
    result = LZ4HC_countPattern(v_stack_m88 + 4, v_stack_m138, (uint32_t)((uint32_t)((uint32_t)(v_stack_m14C))), 1);
    result = ((uint32_t)((uint32_t)(result))) + (4);
    local_r10 = 0;
    v_stack_mE8 = result;
    goto loc_005F6ED4;
loc_005F6E4C:
    v_stack_m148 = (uint32_t)(local_r10 + 1);
loc_005F6E51:
loc_005F6E55:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))) - ((uint32_t)(*(uint16_t *)(v_stack_p8 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + arg1 * 4))) * 2 + 0x20000))));
loc_005F6E6B:
    if (((uint32_t)(local_r13)) >= ((uint32_t)((uint32_t)(v_stack_m150)))) goto loc_005F6936;
loc_005F6E88:
loc_005F6E99:
    local_r10 = 0;
    v_stack_m54 = (uint32_t)((uint32_t)(v_stack_m158));
    v_stack_m58 = (uint32_t)((uint32_t)(v_stack_m120));
    v_stack_mC8 = v_stack_m58;
    goto loc_005F70B4;
loc_005F6EC4:
    v_stack_m148 = (uint32_t)((uint32_t)(v_stack_m120));
    if (((uint32_t)((uint32_t)(v_stack_m120))) != 2) goto loc_005F6E51;
loc_005F6ED4:
    if (((uint32_t)(v_stack_m118)) < ((uint32_t)((uint32_t)(v_stack_m150)))) goto loc_005F6E55;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mD0))) - ((uint32_t)(v_stack_m118)));
    result = (uint32_t)((result) - ((uint32_t)(v_stack_mC0)));
    if (((uint32_t)(result)) < 3) goto loc_005F6E55;
    if (((uint32_t)(v_stack_m118)) >= ((uint32_t)(v_stack_mD0))) goto loc_005F6F07;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m118))) - ((uint32_t)(local_r10 + 18)));
    local_rbx = (local_rbx) + (v_stack_mC8);
    goto loc_005F6F11;
loc_005F6F07:
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(v_stack_mD0)));
    local_rbx = (local_rbx) + (v_stack_m110);
loc_005F6F11:
    if ((*(uint32_t *)(local_rbx)) != ((uint32_t)((uint32_t)(v_stack_m14C)))) goto loc_005F6E51;
    local_r11 = v_stack_m138;
    if (0 != 0) { local_r11 = v_stack_mB0; }
    result = LZ4HC_countPattern(local_rbx + 4, local_r11, (uint32_t)((uint32_t)((uint32_t)(v_stack_m14C))), v_stack_mC0);
    local_rsi = ((uint32_t)((uint32_t)(result))) + (4);
    if (0 == 0) goto loc_005F6F7D;
    if ((local_rsi + local_rbx * 1) != local_r11) goto loc_005F6F77;
    Arg1 = (uint32_t)((local_rsi) & (3));
    Arg1 = (Arg1) << (3);
    if (Arg1 != NULL) {
    }
    result = LZ4HC_countPattern(v_stack_m110, v_stack_m138, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m14C))))), v_stack_mC0);
    local_rsi = (local_rsi) + ((uint32_t)((uint32_t)(result)));
loc_005F6F77:
    goto loc_005F6F81;
loc_005F6F7D:
loc_005F6F81:
    result = LZ4HC_reverseCountPattern(local_rbx, v_stack_m110, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m14C))))), v_stack_mC0);
    Arg2 = 0;
    if (0 != 0) goto loc_005F6FD9;
    local_rbx = (local_rbx) - ((uint32_t)((uint32_t)(result)));
    if (local_rbx != v_stack_m110) goto loc_005F6FD9;
    if (v_stack_m154 >= ((uint32_t)(v_stack_mD0))) goto loc_005F6FD9;
    Arg1 = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))));
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (Arg1) << (3);
    if (Arg1 != NULL) {
    }
    result = LZ4HC_reverseCountPattern(v_stack_mB0, v_stack_mC8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m14C))))), v_stack_mC0);
    local_r11 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    Arg2 = 0;
loc_005F6FD9:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m118))) - ((uint32_t)(local_r11)));
    local_r13 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m150)));
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(v_stack_m150)))) { local_r13 = (uint32_t)(result); }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m118))) - ((uint32_t)(local_r13)));
    Arg1 = (Arg1) + (local_rsi);
    if (Arg1 < v_stack_mE8) goto loc_005F701F;
    if (local_rsi > v_stack_mE8) goto loc_005F701F;
    local_rsi = (uint32_t)((local_rsi) - ((uint32_t)(v_stack_mE8)));
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(v_stack_m118)));
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mD0))) - ((uint32_t)(local_rsi)));
    result = (uint32_t)((result) - 1);
    local_r13 = (uint32_t)((uint32_t)(v_stack_mD0));
    if (((uint32_t)(result)) >= 3) { local_r13 = (uint32_t)(local_rsi); }
    goto loc_005F6E6B;
loc_005F701F:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mD0))) - ((uint32_t)(local_r13)));
    result = (uint32_t)((result) - 1);
    if (((uint32_t)(result)) < 3) goto loc_005F709E;
    if (v_stack_mC0 != 0) goto loc_005F6E6B;
    Arg2 = v_stack_mE8;
    if (Arg1 < v_stack_mE8) { Arg2 = Arg1; }
    if (((int32_t)(v_stack_m158)) >= Arg2) goto loc_005F707A;
    Arg1 = ((uint32_t)((uint32_t)(v_stack_mD0))) - ((uint32_t)((uint32_t)(local_r13)));
    Arg1 = (Arg1) - (v_stack_m110);
    Arg1 = (Arg1) + (v_stack_mE0);
    if (Arg1 > ((uint32_t)(0xFFFFULL))) goto loc_005F6E88;
    result = (uint32_t)(((uint32_t)(v_stack_m130)) - ((uint32_t)(local_r13)));
    v_stack_m158 = (uint32_t)(Arg2);
    v_stack_m120 = (uint32_t)(result);
    v_stack_mB8 = v_stack_mE0;
loc_005F707A:
    if (((uint32_t)(*(uint16_t *)(v_stack_p8 + (uint16_t)(local_r13) * 2 + 0x20000))) > ((uint32_t)(local_r13))) goto loc_005F6E88;
    local_r13 = (uint32_t)((local_r13) - ((uint32_t)(*(uint16_t *)(v_stack_p8 + (uint16_t)(local_r13) * 2 + 0x20000))));
    goto loc_005F6E6B;
loc_005F709E:
    goto loc_005F6E6B;
loc_005F70A6:
    v_stack_mC8 = 0;
    v_stack_mC4 = 0;
loc_005F70B4:
    if (0 <= ((uint32_t)(local_rsi))) goto loc_005F7542;
    if (v_stack_mB8 >= ((int32_t)(Arg6) + (uint32_t)((uint32_t)(v_stack_mD0)) * 1 + 3)) goto loc_005F70FD;
    if (v_stack_mB8 >= ((int32_t)(Arg6) + (uint32_t)((uint32_t)(v_stack_mD0)) * 1)) goto loc_005F734E;
    v_stack_m128 = v_stack_mC8;
    v_stack_mE0 = v_stack_mC8;
    v_stack_m118 = v_stack_mB8;
    goto loc_005F676E;
loc_005F70FD:
    if (v_stack_mB8 >= ((int32_t)(Arg6) + (uint32_t)((uint32_t)(v_stack_mD0)) * 1)) goto loc_005F7175;
    result = (v_stack_mB8) - ((uint32_t)((uint32_t)(v_stack_mD0)));
    if (result >= local_r11) goto loc_005F7168;
    Arg4 = (int32_t)(Arg6);
    if (((uint32_t)((int32_t)(Arg6))) > ((uint32_t)(local_r11))) { Arg4 = (uint32_t)(local_r11); }
    Arg1 = ((int32_t)((uint32_t)((uint32_t)(v_stack_m124)))) + (-4);
    Arg1 = (Arg1) + (v_stack_mB8);
    result = ((int32_t)((uint32_t)(Arg4))) + ((uint32_t)((uint32_t)(v_stack_mD0)));
    v_stack_p30 = (uint32_t)(Arg4);
    if (result >= = Arg1) {
        Arg4 = (uint32_t)(v_stack_mB8);
        Arg4 = (uint32_t)((Arg4) - ((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0)))));
        Arg4 = (uint32_t)((Arg4) + (-4));
        Arg4 = (uint32_t)((Arg4) + ((uint32_t)((uint32_t)(v_stack_m124))));
        v_stack_p30 = (uint32_t)(Arg4);
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0))))) - ((uint32_t)(v_stack_mB8)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg4)));
    if (condition_is_less_or_equal) goto loc_005F7175;
    local_r12 = (v_stack_mB8) + ((int32_t)((uint32_t)(Arg1)));
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m124)) - ((uint32_t)(Arg1)));
    v_stack_m118 = local_r12;
    v_stack_m124 = (uint32_t)(local_rsi);
    goto loc_005F7175;
loc_005F7168:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0)))));
    v_stack_p30 = (uint32_t)(Arg4);
loc_005F7175:
    local_r14 = (v_stack_mD0) + (1);
    local_r12 = ((uint32_t)((uint32_t)(v_stack_mD0))) - (v_stack_m100);
    if (Arg7 == 0) goto loc_005F71C9;
    Arg2 = (v_stack_mB8) >> (7);
    result = (Arg2 + 8) + (local_r12);
    result = (result) + (local_r14);
    if (result > v_stack_mF0) goto loc_005F7A71;
loc_005F71C9:
    if (local_r12 < 15) goto loc_005F7224;
    *(uint8_t *)(v_stack_mD0) = 240;
    local_rsi = 1;
    local_r10 = v_stack_mD0;
    local_r11 = v_stack_m100;
    local_r13 = local_r12 - 15;
    if ((local_r12 - 15) >= 255) {
        result = Arg1;
        Arg1 = local_r14;
        local_rsi = Arg2;
        Arg2 = 255;
        local_rsi = (local_rsi) >> (7);
        Arg3 = local_rsi;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        local_r11 = v_stack_m100;
        local_r14 = (local_r14) + (local_rsi);
        result = (result) * (local_rsi);
        Arg3 = v_stack_mD0;
        local_r10 = v_stack_mD0;
        local_r13 = (local_r12 - 15) + (result);
        local_rsi = 1;
    }
    *(uint8_t *)(local_r14) = (uint8_t)(local_r13);
    local_r14 = (local_r14) + (local_rsi);
    goto loc_005F722D;
loc_005F7224:
    result = (uint8_t)(((uint8_t)(local_r12)) << (4));
    *(uint8_t *)(Arg3) = (uint8_t)(result);
loc_005F722D:
    Arg2 = (local_r11) - (local_r14);
loc_005F723A:
    *(uint64_t *)(local_r14) = *(uint64_t *)(arg2 + local_r14 * 1);
    Arg1 = (local_r14) + (8);
    if (Arg1 < (local_r12 + local_r14 * 1)) goto loc_005F723A;
    local_r14 = (local_r14) + (local_r12);
    *(uint16_t *)(local_r14) = (uint16_t)(v_stack_mF8);
    local_r14 = (local_r14) + (2);
    v_stack_mD0 = local_r14;
    if (Arg7 == 0) goto loc_005F729E;
    Arg2 = (Arg2) >> (7);
    result = (Arg2 + 6) + (local_r14);
    if (result > v_stack_mF0) goto loc_005F7A69;
loc_005F729E:
    if (((int32_t)(Arg6) - 4) < 15) goto loc_005F7303;
    result = (uint8_t)((*(uint8_t *)(local_r10)) + (15));
    Arg1 = ((int32_t)(Arg6) - 4) - (15);
    *(uint8_t *)(Arg3) = (uint8_t)(result);
    if (Arg1 < 510) goto loc_005F72E0;
    Arg2 = (Arg2) >> (8);
    result = (local_r12) * (Arg2);
    Arg1 = (Arg1) + (result);
loc_005F72CD:
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (1);
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (1);
    Arg2 = (Arg2) - (1);
    if (condition_is_not_equal) goto loc_005F72CD;
loc_005F72E0:
    if (Arg1 >= 255) {
        Arg1 = (Arg1) - (255);
        *(uint8_t *)(local_r14) = 255;
        local_r14 = (local_r14) + (1);
    }
    *(uint8_t *)(local_r14) = (uint8_t)(Arg1);
    local_r14 = (local_r14) + (1);
    v_stack_mD0 = local_r14;
    goto loc_005F7308;
loc_005F7303:
    result = (uint8_t)((result) + ((uint8_t)(Arg1)));
    *(uint8_t *)(Arg3) = (uint8_t)(result);
loc_005F7308:
    local_r13 = (v_stack_m140) + ((int32_t)(Arg6));
    v_stack_mF8 = v_stack_m128;
    v_stack_m128 = v_stack_mA8;
    local_r10 = 0;
    v_stack_m100 = local_r13;
    v_stack_mE0 = v_stack_mA8;
    v_stack_m140 = v_stack_m118;
    v_stack_m118 = v_stack_mB8;
    v_stack_p30 = (uint32_t)((uint32_t)(v_stack_mF4));
    goto loc_005F6768;
loc_005F734E:
    if (v_stack_mB8 >= Arg1) goto loc_005F7384;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m118))) - ((uint32_t)(v_stack_mB8)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(v_stack_mF4))));
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m124)) - ((uint32_t)(Arg1)));
    local_r12 = (v_stack_mB8) + ((int32_t)((uint32_t)(Arg1)));
    v_stack_m124 = (uint32_t)(local_rsi);
    v_stack_m118 = local_r12;
    if (((uint32_t)(local_rsi)) >= 4) goto loc_005F737F;
    v_stack_m118 = Arg2;
    v_stack_m128 = v_stack_mA8;
    goto loc_005F7384;
loc_005F737F:
loc_005F7384:
    local_r14 = (local_r14) + (1);
    local_r12 = (v_stack_m118) - (v_stack_m100);
    if (Arg7 == 0) goto loc_005F73D8;
    Arg2 = (Arg2) >> (7);
    result = (Arg2 + 8) + (local_r12);
    result = (result) + (local_r14);
    if (result > v_stack_mF0) goto loc_005F7A71;
loc_005F73D8:
    if (local_r12 < 15) goto loc_005F7433;
    *(uint8_t *)(local_r14) = 240;
    local_rsi = 1;
    local_r10 = local_r14;
    local_r11 = v_stack_m100;
    local_r13 = local_r12 - 15;
    if ((local_r12 - 15) >= 255) {
        result = Arg1;
        Arg1 = local_r14;
        local_rsi = Arg2;
        Arg2 = 255;
        local_rsi = (local_rsi) >> (7);
        Arg3 = local_rsi;
        result = memset(Arg1, Arg2, Arg3, (uint32_t)(v_stack_mF4));
        local_r11 = v_stack_m100;
        local_r14 = (local_r14) + (local_rsi);
        result = (result) * (local_rsi);
        Arg3 = local_r14;
        local_r10 = local_r14;
        local_r13 = (local_r12 - 15) + (result);
        local_rsi = 1;
    }
    *(uint8_t *)(local_r14) = (uint8_t)(local_r13);
    local_r14 = (local_r14) + (local_rsi);
    goto loc_005F743C;
loc_005F7433:
    result = (uint8_t)(((uint8_t)(local_r12)) << (4));
    *(uint8_t *)(Arg3) = (uint8_t)(result);
loc_005F743C:
    Arg2 = (local_r11) - (local_r14);
loc_005F7449:
    *(uint64_t *)(local_r14) = *(uint64_t *)(arg2 + local_r14 * 1);
    Arg1 = (local_r14) + (8);
    if (Arg1 < (local_r12 + local_r14 * 1)) goto loc_005F7449;
    local_r14 = (local_r14) + (local_r12);
    *(uint16_t *)(local_r14) = (uint16_t)(v_stack_mF8);
    local_r14 = (local_r14) + (2);
    v_stack_mD0 = local_r14;
    if (Arg7 == 0) goto loc_005F74AD;
    Arg2 = (Arg2) >> (7);
    result = (Arg2 + 6) + (local_r14);
    if (result > v_stack_mF0) goto loc_005F7A69;
loc_005F74AD:
    if (((int32_t)(Arg6) - 4) < 15) goto loc_005F7512;
    result = (uint8_t)((*(uint8_t *)(local_r10)) + (15));
    Arg1 = ((int32_t)(Arg6) - 4) - (15);
    *(uint8_t *)(Arg3) = (uint8_t)(result);
    if (Arg1 < 510) goto loc_005F74EF;
    Arg2 = (Arg2) >> (8);
    result = (local_r12) * (Arg2);
    Arg1 = (Arg1) + (result);
loc_005F74DC:
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (1);
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (1);
    Arg2 = (Arg2) - (1);
    if (condition_is_not_equal) goto loc_005F74DC;
loc_005F74EF:
    if (Arg1 >= 255) {
        Arg1 = (Arg1) - (255);
        *(uint8_t *)(local_r14) = 255;
        local_r14 = (local_r14) + (1);
    }
    *(uint8_t *)(local_r14) = (uint8_t)(Arg1);
    local_r14 = (local_r14) + (1);
    v_stack_mD0 = local_r14;
    goto loc_005F7517;
loc_005F7512:
    result = (uint8_t)((result) + ((uint8_t)(Arg1)));
    *(uint8_t *)(Arg3) = (uint8_t)(result);
loc_005F7517:
    local_r13 = (v_stack_m140) + ((int32_t)(Arg6));
    v_stack_m100 = local_r13;
    v_stack_m140 = v_stack_mB8;
    v_stack_mF8 = v_stack_mA8;
    v_stack_mC0 = v_stack_m128;
    v_stack_mB0 = v_stack_m128;
    goto loc_005F5E07;
loc_005F7542:
    result = ((int32_t)(Arg6)) + (v_stack_mB8);
    if (local_r12 < result) {
        result = (uint32_t)(local_r12);
        result = (uint32_t)((result) - ((uint32_t)(v_stack_mB8)));
        v_stack_p30 = (uint32_t)(result);
    }
    local_rsi = (v_stack_m140) - (v_stack_m100);
    local_r14 = (local_r14) + 1;
    if (Arg7 == ((uint32_t)(local_r10))) goto loc_005F75A9;
    Arg2 = (Arg2) >> (7);
    result = (Arg2 + 8) + (local_r14);
    result = (result) + (local_rsi);
    if (result > v_stack_mF0) goto loc_005F7A59;
loc_005F75A9:
    if (local_rsi < 15) goto loc_005F7603;
    *(uint8_t *)(local_r14) = 240;
    local_rbx = v_stack_m100;
    local_r11 = v_stack_m140;
    local_r12 = local_rsi - 15;
    if ((local_rsi - 15) >= 255) {
        result = Arg3;
        Arg1 = local_r14;
        local_rbx = Arg2;
        Arg2 = 255;
        local_rbx = (local_rbx) >> (7);
        Arg3 = local_rbx;
        result = memset(Arg1, Arg2, Arg3, local_r14);
        local_r11 = v_stack_m140;
        local_r14 = (local_r14) + (local_rbx);
        result = (result) * (local_rbx);
        local_rbx = v_stack_m100;
        Arg4 = local_r14;
        local_r12 = (local_rsi - 15) + (result);
        local_r10 = 0;
    }
    *(uint8_t *)(local_r14) = (uint8_t)(local_r12);
    local_r14 = (local_r14) + 1;
    goto loc_005F760D;
loc_005F7603:
    result = (uint8_t)(((uint8_t)(local_rsi)) << (4));
    *(uint8_t *)(local_r14) = (uint8_t)(result);
loc_005F760D:
    Arg2 = (local_rbx) - (local_r14);
loc_005F761A:
    *(uint64_t *)(local_r14) = *(uint64_t *)(arg2 + local_r14 * 1);
    Arg1 = (local_r14) + (8);
    if (Arg1 < (local_r14 + local_rsi * 1)) goto loc_005F761A;
    local_r14 = (local_r14) + (local_rsi);
    *(uint16_t *)(local_r14) = (uint16_t)(v_stack_mF8);
    local_r14 = (local_r14) + (2);
    if (Arg7 == 0) goto loc_005F7675;
    Arg2 = (Arg2) >> (7);
    result = (Arg2 + 6) + (local_r14);
    if (result > v_stack_mF0) goto loc_005F7A4C;
loc_005F7675:
    if (((int32_t)(Arg6) - 4) < 15) goto loc_005F76E3;
    result = (uint8_t)((*(uint8_t *)(arg4)) + (15));
    Arg1 = ((int32_t)(Arg6) - 4) - (15);
    *(uint8_t *)(local_r14) = (uint8_t)(result);
    if (Arg1 < 510) goto loc_005F76BF;
    Arg2 = (Arg2) >> (8);
    result = (local_rbx) * (Arg2);
    Arg1 = (Arg1) + (result);
loc_005F76AA:
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (1);
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (1);
    Arg2 = (Arg2) - (1);
    if (condition_is_not_equal) goto loc_005F76AA;
    goto loc_005F76C4;
loc_005F76BF:
loc_005F76C4:
    if (Arg1 >= 255) {
        Arg1 = (Arg1) - (255);
        *(uint8_t *)(local_r14) = 255;
        local_r14 = (local_r14) + (1);
    }
    *(uint8_t *)(local_r14) = (uint8_t)(Arg1);
    local_r14 = (local_r14) + (1);
    goto loc_005F76EE;
loc_005F76E3:
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(result)));
    *(uint8_t *)(local_r14) = (uint8_t)(Arg1);
loc_005F76EE:
    local_r11 = (local_r11) + ((int32_t)(Arg6));
    v_stack_m140 = v_stack_m118;
    v_stack_m100 = local_r11;
    local_rsi = (v_stack_m118) - (local_r11);
    local_r14 = (local_r14) + (1);
    if (Arg7 == 0) goto loc_005F773D;
    Arg2 = (Arg2) >> (7);
    result = (Arg2 + 8) + (local_rsi);
    result = (result) + (local_r14);
    if (result > v_stack_mF0) goto loc_005F7A2E;
loc_005F773D:
    if (local_rsi < 15) goto loc_005F7796;
    *(uint8_t *)(local_r14) = 240;
    local_rbx = 1;
    local_r12 = local_rsi - 15;
    if ((local_rsi - 15) >= 255) {
        result = (int32_t)(Arg6);
        Arg1 = local_r14;
        local_rbx = Arg2;
        Arg2 = 255;
        local_rbx = (local_rbx) >> (7);
        Arg3 = local_rbx;
        result = memset(Arg1, Arg2, Arg3, local_r14);
        local_r11 = v_stack_m100;
        local_r14 = (local_r14) + (local_rbx);
        result = (result) * (local_rbx);
        Arg4 = local_r14;
        local_r12 = (local_rsi - 15) + (result);
        local_r10 = 0;
        local_rbx = local_r10 + 1;
    }
    *(uint8_t *)(local_r14) = (uint8_t)(local_r12);
    local_r14 = (local_r14) + (local_rbx);
    goto loc_005F77A0;
loc_005F7796:
    result = (uint8_t)(((uint8_t)(local_rsi)) << (4));
    *(uint8_t *)(local_r14) = (uint8_t)(result);
loc_005F77A0:
    Arg2 = (local_r11) - (local_r14);
loc_005F77AD:
    *(uint64_t *)(local_r14) = *(uint64_t *)(arg2 + local_r14 * 1);
    Arg1 = (local_r14) + (8);
    if (Arg1 < (local_rsi + local_r14 * 1)) goto loc_005F77AD;
    local_r14 = (local_r14) + (local_rsi);
    *(uint16_t *)(local_r14) = (uint16_t)(v_stack_m128);
    local_r14 = (local_r14) + (2);
    v_stack_mD0 = local_r14;
    if (Arg7 == 0) goto loc_005F7808;
    Arg2 = (Arg2) >> (7);
    result = (Arg2 + 6) + (local_r14);
    if (result > v_stack_mF0) goto loc_005F7A38;
loc_005F7808:
    if (((int32_t)(v_stack_m124) - 4) < 15) goto loc_005F7875;
    result = (uint8_t)((*(uint8_t *)(arg4)) + (15));
    Arg1 = ((int32_t)(v_stack_m124) - 4) - (15);
    *(uint8_t *)(local_r14) = (uint8_t)(result);
    if (Arg1 < 510) goto loc_005F7852;
    Arg2 = (Arg2) >> (8);
    result = (result) * (Arg2);
    Arg1 = (Arg1) + (result);
loc_005F783F:
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (local_rbx);
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (local_rbx);
    Arg2 = (Arg2) - (local_rbx);
    if (condition_is_not_equal) goto loc_005F783F;
loc_005F7852:
    if (Arg1 >= 255) {
        Arg1 = (Arg1) - (255);
        *(uint8_t *)(local_r14) = 255;
        local_r14 = (local_r14) + (local_rbx);
    }
    *(uint8_t *)(local_r14) = (uint8_t)(Arg1);
    local_r14 = (local_r14) + (local_rbx);
    v_stack_mD0 = local_r14;
    goto loc_005F787B;
loc_005F7875:
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(result)));
    *(uint8_t *)(local_r14) = (uint8_t)(Arg1);
loc_005F787B:
    goto loc_005F7A1B;
loc_005F7884:
    local_rdi = (v_stack_m140) - (v_stack_m100);
    local_r14 = (local_r14) + (1);
    if (Arg7 == 0) goto loc_005F78D8;
    Arg2 = (Arg2) >> (7);
    result = (local_rdi + 8) + (Arg2);
    result = (result) + (local_r14);
    if (result > v_stack_mF0) goto loc_005F7A88;
loc_005F78D8:
    if (local_rdi < 15) goto loc_005F7931;
    *(uint8_t *)(local_r14) = 240;
    local_rbx = 1;
    local_rsi = local_rdi - 15;
    local_r11 = v_stack_m100;
    if ((local_rdi - 15) >= 255) {
        result = (int32_t)(v_stack_m124);
        Arg1 = local_r14;
        local_rbx = Arg2;
        Arg2 = 255;
        local_rbx = (local_rbx) >> (7);
        Arg3 = local_rbx;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        Arg4 = Arg6;
        local_r14 = (local_r14) + (local_rbx);
        local_r11 = v_stack_m100;
        result = (result) * (local_rbx);
        local_rsi = (local_rdi - 15) + (result);
        local_r10 = 0;
        local_rbx = local_r10 + 1;
    }
    *(uint8_t *)(local_r14) = (uint8_t)(local_rsi);
    local_r14 = (local_r14) + (local_rbx);
    goto loc_005F793B;
loc_005F7931:
    result = (uint8_t)(((uint8_t)(local_rdi)) << (4));
    *(uint8_t *)(local_r14) = (uint8_t)(result);
loc_005F793B:
    Arg2 = (local_r11) - (local_r14);
loc_005F7948:
    *(uint64_t *)(local_r14) = *(uint64_t *)(arg2 + local_r14 * 1);
    Arg1 = (local_r14) + (8);
    if (Arg1 < (local_rdi + local_r14 * 1)) goto loc_005F7948;
    local_r14 = (local_r14) + (local_rdi);
    Arg1 = ((int32_t)((uint32_t)(Arg4))) - (4);
    *(uint16_t *)(local_r14) = (uint16_t)(v_stack_mF8);
    local_r14 = (local_r14) + (2);
    v_stack_mD0 = local_r14;
    if (Arg7 == 0) goto loc_005F79A3;
    Arg2 = (Arg2) >> (7);
    result = (Arg2 + 6) + (local_r14);
    if (result > v_stack_mF0) goto loc_005F7A83;
loc_005F79A3:
    if (Arg1 < 15) goto loc_005F7A0A;
    result = (uint8_t)((*(uint8_t *)(local_r14)) + (15));
    Arg1 = (Arg1) - (15);
    *(uint8_t *)(local_r14) = (uint8_t)(result);
    if (Arg1 < 510) goto loc_005F79E7;
    Arg2 = (Arg2) >> (8);
    result = (local_rdi + local_r14 * 1) * (Arg2);
    Arg1 = (Arg1) + (result);
loc_005F79D4:
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (local_rbx);
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (local_rbx);
    Arg2 = (Arg2) - (local_rbx);
    if (condition_is_not_equal) goto loc_005F79D4;
loc_005F79E7:
    if (Arg1 >= 255) {
        Arg1 = (Arg1) - (255);
        *(uint8_t *)(local_r14) = 255;
        local_r14 = (local_r14) + (local_rbx);
    }
    *(uint8_t *)(local_r14) = (uint8_t)(Arg1);
    local_r14 = (local_r14) + (local_rbx);
    v_stack_mD0 = local_r14;
    goto loc_005F7A10;
loc_005F7A0A:
    result = (uint8_t)((result) + ((uint8_t)(Arg1)));
    *(uint8_t *)(local_r14) = (uint8_t)(result);
loc_005F7A10:
    local_rdi = (v_stack_m140) + ((int32_t)((uint32_t)(Arg4)));
loc_005F7A1B:
    v_stack_m100 = local_rdi;
    goto loc_005F5C32;
loc_005F7A2E:
    v_stack_m100 = local_rdi;
    goto loc_005F7A42;
loc_005F7A38:
loc_005F7A42:
    v_stack_mF8 = local_rdi;
    goto loc_005F7A83;
loc_005F7A4C:
    goto loc_005F7A74;
loc_005F7A59:
    goto loc_005F7A7E;
loc_005F7A69:
    local_r10 = 0;
    goto loc_005F7A7E;
loc_005F7A71:
    local_r10 = 0;
loc_005F7A74:
loc_005F7A7E:
loc_005F7A83:
loc_005F7A88:
    if (Arg7 != 2) goto loc_005F7C66;
    local_rdi = (v_stack_m140) - (local_rbx);
    Arg2 = (Arg2) >> (7);
    Arg3 = (local_rdi + 1) + (Arg2);
    if ((Arg3 + local_r14 * 1) > (v_stack_mF0 - 3)) goto loc_005F7C15;
    Arg1 = (v_stack_mF0 - 3) - (Arg3);
    Arg1 = (Arg1) - (local_r14);
    Arg1 = (Arg1) * (Arg1);
    Arg1 = (Arg1) + (18);
    Arg4 = (uint32_t)(Arg6);
    if (((int32_t)((uint32_t)((uint32_t)(Arg6)))) > Arg1) { Arg4 = (uint32_t)(Arg1); }
    result = ((int32_t)((uint32_t)(Arg4))) - (Arg3);
    v_stack_p30 = (uint32_t)(Arg4);
    result = (result) - (local_r14);
    result = (result) + (2);
    result = (result) + (v_stack_mF0);
    if (result < 12) goto loc_005F7C15;
    if (local_rdi < 15) goto loc_005F7B6B;
    *(uint8_t *)(local_r14) = 240;
    local_rbx = 1;
    local_rsi = local_rdi - 15;
    local_r11 = local_rbx;
    local_r14 = local_r14 + 1;
    if ((local_rdi - 15) >= 255) {
        Arg1 = local_r14 + 1;
        local_rbx = Arg2;
        Arg2 = 255;
        local_rbx = (local_rbx) >> (7);
        Arg3 = local_rbx;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        Arg4 = Arg6;
        local_r14 = (local_r14 + 1) + (local_rbx);
        local_r11 = v_stack_m100;
        result = (result) * (local_rbx);
        local_rbx = 1;
        local_rsi = (local_rdi - 15) + (result);
    }
    *(uint8_t *)(local_r14) = (uint8_t)(local_rsi);
    local_r14 = (local_r14) + (local_rbx);
    goto loc_005F7B74;
loc_005F7B6B:
    result = (uint8_t)(((uint8_t)(local_rdi)) << (4));
    *(uint8_t *)(local_r14) = (uint8_t)(result);
loc_005F7B74:
    local_r11 = (local_r11) - (local_r14);
loc_005F7B7E:
    *(uint64_t *)(local_r14) = *(uint64_t *)(local_r14 + local_r11 * 1);
    Arg1 = (local_r14) + (8);
    if (Arg1 < (local_rdi + local_r14 * 1)) goto loc_005F7B7E;
    local_r14 = (local_r14) + (local_rdi);
    Arg1 = ((int32_t)((uint32_t)(Arg4))) - (4);
    *(uint16_t *)(local_r14) = (uint16_t)(v_stack_mF8);
    local_r14 = (local_r14) + (2);
    if (Arg1 < 15) goto loc_005F7C01;
    result = (uint8_t)((*(uint8_t *)(local_r14)) + (15));
    Arg1 = (Arg1) - (15);
    *(uint8_t *)(local_r14) = (uint8_t)(result);
    if (Arg1 < 510) goto loc_005F7BEB;
    Arg2 = (local_rdi + local_r14 * 1) >> (8);
    result = (result) * (Arg2);
    Arg1 = (Arg1) + (result);
loc_005F7BDA:
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (local_rbx);
    *(uint8_t *)(local_r14) = 255;
    local_r14 = (local_r14) + (local_rbx);
    Arg2 = (Arg2) - (local_rbx);
    if (condition_is_not_equal) goto loc_005F7BDA;
loc_005F7BEB:
    if (Arg1 >= 255) {
        Arg1 = (Arg1) - (255);
        *(uint8_t *)(local_r14) = 255;
        local_r14 = (local_r14) + (local_rbx);
    }
    *(uint8_t *)(local_r14) = (uint8_t)(Arg1);
    local_r14 = (local_r14) + (local_rbx);
    goto loc_005F7C06;
loc_005F7C01:
    result = (uint8_t)((result) + ((uint8_t)(Arg1)));
    *(uint8_t *)(local_r14) = (uint8_t)(result);
loc_005F7C06:
    local_r11 = ((int32_t)((uint32_t)(Arg4))) + (v_stack_m140);
    v_stack_m100 = local_r11;
    local_r10 = 0;
loc_005F7C15:
loc_005F7C2E:
    local_rbx = (v_stack_m98) - (local_r11);
    v_stack_m98 = local_rbx;
    Arg2 = (Arg2) >> (7);
    if (Arg7 != 2) goto loc_005F7C6E;
    local_rsi = (v_stack_mF0) + (5);
    goto loc_005F7C77;
loc_005F7C66:
    goto loc_005F7D3C;
loc_005F7C6E:
    if (Arg7 == 0) goto loc_005F7CB4;
loc_005F7C77:
    result = (local_rbx + 1) + (Arg2);
    result = (result) + (0);
    if (result <= local_rsi) goto loc_005F7CB9;
    if (Arg7 != 1) goto loc_005F7C97;
    goto loc_005F7D41;
loc_005F7C97:
    local_rbx = (local_rsi) - (0);
    local_rbx = (local_rbx) - (1);
    result = (local_rbx + 241) >> (8);
    local_rbx = (local_rbx) - (result);
    v_stack_m98 = local_rbx;
    goto loc_005F7CB9;
loc_005F7CB4:
loc_005F7CB9:
    if (local_rbx < 15) goto loc_005F7D11;
    *(uint8_t *)(0) = 240;
    local_r14 = (0) + (1);
    local_rdi = local_rbx - 15;
    if ((local_rbx - 15) >= 255) {
        result = Arg4;
        Arg1 = local_r14;
        local_rbx = Arg2;
        Arg2 = 255;
        local_rbx = (local_rbx) >> (7);
        Arg3 = local_rbx;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        local_r11 = v_stack_m100;
        local_r14 = (local_r14) + (local_rbx);
        result = (result) * (local_rbx);
        local_rbx = v_stack_m98;
        local_rdi = (local_rbx - 15) + (result);
    }
    *(uint8_t *)(local_r14) = (uint8_t)(local_rdi);
    local_r14 = (local_r14) + 1;
    goto loc_005F7D1C;
loc_005F7D11:
    result = (uint8_t)(((uint8_t)(local_rbx)) << (4));
    *(uint8_t *)(local_r14) = (uint8_t)(result);
    local_r14 = (local_r14) + (Arg1);
loc_005F7D1C:
    result = memcpy(local_r14 + 1, local_r11, local_rbx, Arg4);
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(v_stack_p18)));
    local_rsi = (uint32_t)((local_rbx + local_r11 * 1) - ((uint32_t)(v_stack_p10)));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_rbx)));
    *(uint32_t *)(v_stack_p20) = (uint32_t)(local_rsi);
    if (condition_is_greater) goto loc_005F7D4E;
loc_005F7D3C:
loc_005F7D41:
    *(uint8_t *)(v_stack_p8 + 0x40027) = 1;
loc_005F7D4E:
loc_005F7D51:
    goto loc_005F7D79;
loc_005F7D56:
    v_stack_m168 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m178 = (uint32_t)((uint32_t)(Arg5));
    result = LZ4HC_compress_generic_dictCtx(v_stack_p8, local_r11, local_rbx, v_stack_p20);
loc_005F7D79:
    local_rsp = (local_rsp) + (344);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40000` | `64` | `R/W` |
| `Arg1` | `+ 0x40028` | `64` | `R` |
| `Arg2` | `- 0xC` | `64` | `R` |
| `Arg2` | `- 0x5` | `64` | `R` |
| `Arg2` | `+ 0x0 + rdx*1` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg5` | `- 0x5` | `64` | `R` |
| `Arg6` | `- 0x4` | `64` | `R` |
| `Arg6` | `- 0x2 + rcx*1` | `8` | `R` |
| `Arg6` | `+ 0x0 + r13*1` | `64` | `R` |
| `Arg6` | `+ 0x3` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F564C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
