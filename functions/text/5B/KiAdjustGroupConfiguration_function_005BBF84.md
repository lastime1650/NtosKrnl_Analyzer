# KiAdjustGroupConfiguration

- RVA: `0x005BBF84`–`0x005BC2F4` (길이 `880` bytes)
- VA: `0x00000001405BBF84`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA3A4`
- 디코드: `236`개 명령, `880/880` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x005BBFBF` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005BC120` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x005BC18C` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x005BC1E3` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005BC2C2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x005BC2D2` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KiAllocateProcessorNumber](KiAllocateProcessorNumber_function_005BC2FC.md) at `0x005BC384`

### Static image references
- `0x005BBF9D` → RVA `0x00E0A740` (`.data`; read)
- `0x005BBFCE` → RVA `0x00FC5014` (`ALMOSTRO`; read)
- `0x005BBFE5` → RVA `0x00FC5044` (`ALMOSTRO`; read)
- `0x005BBFED` → RVA `0x00F21AC8` (`.data`; read)
- `0x005BC000` → RVA `0x00F21AF0` (`.data`; read)
- `0x005BC17A` → RVA `0x005BC720` (`KiCompareSubNodeConfigurationCapacity`; read)
- `0x005BC1B5` → RVA `0x00FC5018` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x005BC120` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x005BC2C2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BBF84  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
005BBF89  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
005BBF8E  56                              push rsi
005BBF8F  57                              push rdi
005BBF90  41 54                           push r12
005BBF92  41 56                           push r14
005BBF94  41 57                           push r15
005BBF96  48 81 EC 30 01 00 00            sub rsp, 0x130
005BBF9D  48 8B 05 9C E7 84 00            mov rax, qword ptr [rip + 0x84e79c]
005BBFA4  48 33 C4                        xor rax, rsp
005BBFA7  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
005BBFAF  48 8B F1                        mov rsi, rcx
005BBFB2  33 D2                           xor edx, edx
005BBFB4  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
005BBFB9  41 B8 80 00 00 00               mov r8d, 0x80
005BBFBF  E8 7C AC 10 00                  call 0x1406c6c40
005BBFC4  F6 46 05 04                     test byte ptr [rsi + 5], 4
005BBFC8  0F 85 F9 02 00 00               jne 0x1405bc2c7
005BBFCE  0F B7 05 3F 90 A0 00            movzx eax, word ptr [rip + 0xa0903f]
005BBFD5  45 33 FF                        xor r15d, r15d
005BBFD8  66 44 3B F8                     cmp r15w, ax
005BBFDC  73 0F                           jae 0x1405bbfed
005BBFDE  8B C8                           mov ecx, eax
005BBFE0  48 8D 7C 24 20                  lea rdi, [rsp + 0x20]
005BBFE5  8B 05 59 90 A0 00               mov eax, dword ptr [rip + 0xa09059]
005BBFEB  F3 AB                           rep stosd dword ptr [rdi], eax
005BBFED  0F B7 0D D4 5A 96 00            movzx ecx, word ptr [rip + 0x965ad4]
005BBFF4  41 BC 01 00 00 00               mov r12d, 1
005BBFFA  66 44 3B F9                     cmp r15w, cx
005BBFFE  73 27                           jae 0x1405bc027
005BC000  48 8B 15 E9 5A 96 00            mov rdx, qword ptr [rip + 0x965ae9]
005BC007  8B F9                           mov edi, ecx
005BC009  48 83 C2 06                     add rdx, 6
005BC00D  44 84 62 FF                     test byte ptr [rdx - 1], r12b
005BC011  74 0B                           je 0x1405bc01e
005BC013  0F B7 0A                        movzx ecx, word ptr [rdx]
005BC016  0F B6 42 FE                     movzx eax, byte ptr [rdx - 2]
005BC01A  29 44 8C 20                     sub dword ptr [rsp + rcx*4 + 0x20], eax
005BC01E  48 83 C2 18                     add rdx, 0x18
005BC022  49 2B FC                        sub rdi, r12
005BC025  75 E6                           jne 0x1405bc00d
005BC027  41 0F B7 CF                     movzx ecx, r15w
005BC02B  44 0F B7 05 95 5A 96 00         movzx r8d, word ptr [rip + 0x965a95]
005BC033  66 41 3B C8                     cmp cx, r8w
005BC037  73 75                           jae 0x1405bc0ae
005BC039  48 8B 3D B0 5A 96 00            mov rdi, qword ptr [rip + 0x965ab0]
005BC040  0F B7 C1                        movzx eax, cx
005BC043  48 8D 14 40                     lea rdx, [rax + rax*2]
005BC047  8A 44 D7 05                     mov al, byte ptr [rdi + rdx*8 + 5]
005BC04B  24 07                           and al, 7
005BC04D  3C 03                           cmp al, 3
005BC04F  75 37                           jne 0x1405bc088
005BC051  4C 39 7C D7 10                  cmp qword ptr [rdi + rdx*8 + 0x10], r15
005BC056  75 30                           jne 0x1405bc088
005BC058  44 0F B6 44 D7 04               movzx r8d, byte ptr [rdi + rdx*8 + 4]
005BC05E  0F B6 46 04                     movzx eax, byte ptr [rsi + 4]
005BC062  44 3A C0                        cmp r8b, al
005BC065  76 0A                           jbe 0x1405bc071
005BC067  44 0F B7 4E 06                  movzx r9d, word ptr [rsi + 6]
005BC06C  44 2B C0                        sub r8d, eax
005BC06F  EB 0C                           jmp 0x1405bc07d
005BC071  44 0F B7 4C D7 06               movzx r9d, word ptr [rdi + rdx*8 + 6]
005BC077  41 2B C0                        sub eax, r8d
005BC07A  44 8B C0                        mov r8d, eax
005BC07D  41 0F B7 C1                     movzx eax, r9w
005BC081  44 39 44 84 20                  cmp dword ptr [rsp + rax*4 + 0x20], r8d
005BC086  73 06                           jae 0x1405bc08e
005BC088  66 41 03 CC                     add cx, r12w
005BC08C  EB 9D                           jmp 0x1405bc02b
005BC08E  0F B7 46 06                     movzx eax, word ptr [rsi + 6]
005BC092  0F B7 4C D7 06                  movzx ecx, word ptr [rdi + rdx*8 + 6]
005BC097  66 89 44 D7 06                  mov word ptr [rdi + rdx*8 + 6], ax
005BC09C  80 4E 05 02                     or byte ptr [rsi + 5], 2
005BC0A0  66 89 4E 06                     mov word ptr [rsi + 6], cx
005BC0A4  80 64 D7 05 FD                  and byte ptr [rdi + rdx*8 + 5], 0xfd
005BC0A9  E9 19 02 00 00                  jmp 0x1405bc2c7
005BC0AE  0F B7 05 5F 8F A0 00            movzx eax, word ptr [rip + 0xa08f5f]
005BC0B5  66 44 3B F8                     cmp r15w, ax
005BC0B9  73 12                           jae 0x1405bc0cd
005BC0BB  8B C8                           mov ecx, eax
005BC0BD  48 8D BC 24 A0 00 00 00         lea rdi, [rsp + 0xa0]
005BC0C5  8B 05 79 8F A0 00               mov eax, dword ptr [rip + 0xa08f79]
005BC0CB  F3 AB                           rep stosd dword ptr [rdi], eax
005BC0CD  66 45 3B F8                     cmp r15w, r8w
005BC0D1  73 37                           jae 0x1405bc10a
005BC0D3  48 8B 15 16 5A 96 00            mov rdx, qword ptr [rip + 0x965a16]
005BC0DA  49 8B F8                        mov rdi, r8
005BC0DD  48 83 C2 10                     add rdx, 0x10
005BC0E1  8A 42 F5                        mov al, byte ptr [rdx - 0xb]
005BC0E4  41 84 C4                        test r12b, al
005BC0E7  74 18                           je 0x1405bc101
005BC0E9  A8 04                           test al, 4
005BC0EB  75 05                           jne 0x1405bc0f2
005BC0ED  4C 39 3A                        cmp qword ptr [rdx], r15
005BC0F0  74 0F                           je 0x1405bc101
005BC0F2  0F B7 4A F6                     movzx ecx, word ptr [rdx - 0xa]
005BC0F6  0F B6 42 F4                     movzx eax, byte ptr [rdx - 0xc]
005BC0FA  29 84 8C A0 00 00 00            sub dword ptr [rsp + rcx*4 + 0xa0], eax
005BC101  48 83 C2 18                     add rdx, 0x18
005BC105  49 2B FC                        sub rdi, r12
005BC108  75 D7                           jne 0x1405bc0e1
005BC10A  0F B7 15 B7 59 96 00            movzx edx, word ptr [rip + 0x9659b7]
005BC111  B9 40 00 00 00                  mov ecx, 0x40
005BC116  48 C1 E2 03                     shl rdx, 3
005BC11A  41 B8 4B 41 47 43               mov r8d, 0x4347414b
005BC120  E8 CB 5F 5C 00                  call 0x140b820f0
005BC125  48 8B D8                        mov rbx, rax
005BC128  48 85 C0                        test rax, rax
005BC12B  0F 84 96 01 00 00               je 0x1405bc2c7
005BC131  0F B7 05 90 59 96 00            movzx eax, word ptr [rip + 0x965990]
005BC138  41 0F B7 FF                     movzx edi, r15w
005BC13C  66 44 3B F8                     cmp r15w, ax
005BC140  73 35                           jae 0x1405bc177
005BC142  48 8B 15 A7 59 96 00            mov rdx, qword ptr [rip + 0x9659a7]
005BC149  44 8B C0                        mov r8d, eax
005BC14C  48 83 C2 10                     add rdx, 0x10
005BC150  8A 42 F5                        mov al, byte ptr [rdx - 0xb]
005BC153  24 05                           and al, 5
005BC155  41 3A C4                        cmp al, r12b
005BC158  75 14                           jne 0x1405bc16e
005BC15A  4C 39 3A                        cmp qword ptr [rdx], r15
005BC15D  75 0F                           jne 0x1405bc16e
005BC15F  0F B7 C7                        movzx eax, di
005BC162  48 8D 4A F0                     lea rcx, [rdx - 0x10]
005BC166  66 41 03 FC                     add di, r12w
005BC16A  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
005BC16E  48 83 C2 18                     add rdx, 0x18
005BC172  4D 2B C4                        sub r8, r12
005BC175  75 D9                           jne 0x1405bc150
005BC177  0F B7 EF                        movzx ebp, di
005BC17A  4C 8D 0D 9F 05 00 00            lea r9, [rip + 0x59f]
005BC181  8B D5                           mov edx, ebp
005BC183  41 B8 08 00 00 00               mov r8d, 8
005BC189  48 8B CB                        mov rcx, rbx
005BC18C  E8 5F 48 F4 FF                  call 0x1405009f0
005BC191  66 44 3B FF                     cmp r15w, di
005BC195  73 17                           jae 0x1405bc1ae
005BC197  48 8B D3                        mov rdx, rbx
005BC19A  48 8B 0A                        mov rcx, qword ptr [rdx]
005BC19D  48 8D 52 08                     lea rdx, [rdx + 8]
005BC1A1  0F B7 41 06                     movzx eax, word ptr [rcx + 6]
005BC1A5  66 89 41 08                     mov word ptr [rcx + 8], ax
005BC1A9  49 2B EC                        sub rbp, r12
005BC1AC  75 EC                           jne 0x1405bc19a
005BC1AE  45 8A F7                        mov r14b, r15b
005BC1B1  41 0F B7 EF                     movzx ebp, r15w
005BC1B5  66 3B 2D 5C 8E A0 00            cmp bp, word ptr [rip + 0xa08e5c]
005BC1BC  0F 83 B5 00 00 00               jae 0x1405bc277
005BC1C2  0F B7 05 4B 8E A0 00            movzx eax, word ptr [rip + 0xa08e4b]
005BC1C9  66 44 3B F8                     cmp r15w, ax
005BC1CD  73 19                           jae 0x1405bc1e8
005BC1CF  44 8B C0                        mov r8d, eax
005BC1D2  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
005BC1DA  49 C1 E0 02                     shl r8, 2
005BC1DE  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
005BC1E3  E8 58 A6 10 00                  call 0x1406c6840
005BC1E8  0F B6 56 04                     movzx edx, byte ptr [rsi + 4]
005BC1EC  0F B7 CD                        movzx ecx, bp
005BC1EF  8B 44 8C 20                     mov eax, dword ptr [rsp + rcx*4 + 0x20]
005BC1F3  3B C2                           cmp eax, edx
005BC1F5  72 74                           jb 0x1405bc26b
005BC1F7  2B C2                           sub eax, edx
005BC1F9  66 89 6E 06                     mov word ptr [rsi + 6], bp
005BC1FD  89 44 8C 20                     mov dword ptr [rsp + rcx*4 + 0x20], eax
005BC201  41 0F B7 D7                     movzx edx, r15w
005BC205  66 44 3B FF                     cmp r15w, di
005BC209  73 5B                           jae 0x1405bc266
005BC20B  0F B7 C2                        movzx eax, dx
005BC20E  4C 8B 04 C3                     mov r8, qword ptr [rbx + rax*8]
005BC212  4C 3B C6                        cmp r8, rsi
005BC215  74 46                           je 0x1405bc25d
005BC217  0F B7 05 F6 8D A0 00            movzx eax, word ptr [rip + 0xa08df6]
005BC21E  41 0F B7 CF                     movzx ecx, r15w
005BC222  66 44 3B F8                     cmp r15w, ax
005BC226  73 30                           jae 0x1405bc258
005BC228  45 0F B6 50 04                  movzx r10d, byte ptr [r8 + 4]
005BC22D  44 0F B7 C9                     movzx r9d, cx
005BC231  42 8B 44 8C 20                  mov eax, dword ptr [rsp + r9*4 + 0x20]
005BC236  41 3B C2                        cmp eax, r10d
005BC239  72 0D                           jb 0x1405bc248
005BC23B  41 2B C2                        sub eax, r10d
005BC23E  66 41 89 48 06                  mov word ptr [r8 + 6], cx
005BC243  42 89 44 8C 20                  mov dword ptr [rsp + r9*4 + 0x20], eax
005BC248  0F B7 05 C5 8D A0 00            movzx eax, word ptr [rip + 0xa08dc5]
005BC24F  66 41 03 CC                     add cx, r12w
005BC253  66 3B C8                        cmp cx, ax
005BC256  72 D5                           jb 0x1405bc22d
005BC258  66 3B C8                        cmp cx, ax
005BC25B  74 09                           je 0x1405bc266
005BC25D  66 41 03 D4                     add dx, r12w
005BC261  66 3B D7                        cmp dx, di
005BC264  72 A5                           jb 0x1405bc20b
005BC266  66 3B D7                        cmp dx, di
005BC269  74 09                           je 0x1405bc274
005BC26B  66 41 03 EC                     add bp, r12w
005BC26F  E9 41 FF FF FF                  jmp 0x1405bc1b5
005BC274  45 8A F4                        mov r14b, r12b
005BC277  66 44 3B FF                     cmp r15w, di
005BC27B  73 40                           jae 0x1405bc2bd
005BC27D  4C 8B C3                        mov r8, rbx
005BC280  0F B7 FF                        movzx edi, di
005BC283  49 8B 10                        mov rdx, qword ptr [r8]
005BC286  45 84 F6                        test r14b, r14b
005BC289  74 1C                           je 0x1405bc2a7
005BC28B  0F B7 05 86 8D A0 00            movzx eax, word ptr [rip + 0xa08d86]
005BC292  66 39 42 06                     cmp word ptr [rdx + 6], ax
005BC296  8A 42 05                        mov al, byte ptr [rdx + 5]
005BC299  1A C9                           sbb cl, cl
005BC29B  24 FD                           and al, 0xfd
005BC29D  80 E1 02                        and cl, 2
005BC2A0  0A C1                           or al, cl
005BC2A2  88 42 05                        mov byte ptr [rdx + 5], al
005BC2A5  EB 08                           jmp 0x1405bc2af
005BC2A7  0F B7 42 08                     movzx eax, word ptr [rdx + 8]
005BC2AB  66 89 42 06                     mov word ptr [rdx + 6], ax
005BC2AF  49 83 C0 08                     add r8, 8
005BC2B3  66 44 89 7A 08                  mov word ptr [rdx + 8], r15w
005BC2B8  49 2B FC                        sub rdi, r12
005BC2BB  75 C6                           jne 0x1405bc283
005BC2BD  33 D2                           xor edx, edx
005BC2BF  48 8B CB                        mov rcx, rbx
005BC2C2  E8 A9 65 5C 00                  call 0x140b82870
005BC2C7  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
005BC2CF  48 33 CC                        xor rcx, rsp
005BC2D2  E8 69 03 0F 00                  call 0x1406ac640
005BC2D7  4C 8D 9C 24 30 01 00 00         lea r11, [rsp + 0x130]
005BC2DF  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
005BC2E3  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
005BC2E7  49 8B E3                        mov rsp, r11
005BC2EA  41 5F                           pop r15
005BC2EC  41 5E                           pop r14
005BC2EE  41 5C                           pop r12
005BC2F0  5F                              pop rdi
005BC2F1  5E                              pop rsi
005BC2F2  C3                              ret
005BC2F3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAdjustGroupConfiguration(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 8710044)) ^ (v_rsp);
    v_stack_m38 = result;
    a2 = 0;
    result = memset(v_stack_m138, a2, 128, a4);
    if (((*(unsigned __int8 *)(a1 + 5)) & (4)) != 0) goto loc_005BC2C7;
    v_r15 = 0;
    result = *(unsigned __int16 *)(v_rip + 10522687);
    if (0 < ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 10522687)))) {
        a1 = (unsigned int)(*(unsigned __int16 *)(v_rip + 10522687));
        v_rdi = v_stack_m138;
        result = *(unsigned int *)(v_rip + 10522713);
    }
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 9853652)))) goto loc_005BC027;
    a2 = (*(unsigned __int64 *)(v_rip + 9853673)) + (6);
loc_005BC00D:
    if (((*(unsigned __int8 *)(a2 - 1)) & (1)) != 0) {
        a1 = *(unsigned __int16 *)(a2);
        result = *(unsigned __int8 *)(a2 - 2);
    }
    a2 = (a2) + (24);
    v_rdi = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 9853652)))) - (1);
    if (condition_is_not_equal) goto loc_005BC00D;
loc_005BC027:
loc_005BC02B:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 9853589)))) goto loc_005BC0AE;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9853616) + 0 + 0 * 2 * 8 + 5)) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_005BC088;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9853616) + 0 + 0 * 2 * 8 + 16)) != 0) goto loc_005BC088;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9853616) + 0 + 0 * 2 * 8 + 4))) <= ((unsigned __int8)(*(unsigned __int8 *)(a1 + 4)))) goto loc_005BC071;
    a3 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9853616) + 0 + 0 * 2 * 8 + 4)) - ((unsigned int)(*(unsigned __int8 *)(a1 + 4))));
    goto loc_005BC07D;
loc_005BC071:
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 4)) - ((unsigned int)(a3)));
loc_005BC07D:
    if ((*(unsigned int *)(v_rsp + (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9853616) + 0 + 0 * 2 * 8 + 6)) * 4 + 32)) >= ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_005BC08E;
loc_005BC088:
    a1 = (unsigned __int16)((0) + (1));
    goto loc_005BC02B;
loc_005BC08E:
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9853616) + 0 + 0 * 2 * 8 + 6) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 6));
    *(unsigned __int16 *)(a1 + 6) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9853616) + 0 + 0 * 2 * 8 + 6));
    goto loc_005BC2C7;
loc_005BC0AE:
    result = *(unsigned __int16 *)(v_rip + 10522463);
    v_rdi = *(unsigned __int64 *)(v_rip + 9853616);
    if (0 < ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 10522463)))) {
        a1 = (unsigned int)(*(unsigned __int16 *)(v_rip + 10522463));
        v_rdi = v_stack_mB8;
        result = *(unsigned int *)(v_rip + 10522489);
    }
    if (0 >= ((unsigned __int16)((unsigned int)((unsigned int)(result))))) goto loc_005BC10A;
    a2 = (*(unsigned __int64 *)(v_rip + 9853462)) + (16);
loc_005BC0E1:
    if (((1) & ((unsigned __int8)(*(unsigned __int8 *)(a2 - 11)))) == 0) goto loc_005BC101;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 - 11))) & (4)) != 0) goto loc_005BC0F2;
    result = *(unsigned __int8 *)(a2 - 11);
    if ((*(unsigned __int64 *)(a2)) != 0) {
        a1 = *(unsigned __int16 *)(a2 - 10);
        result = *(unsigned __int8 *)(a2 - 12);
    }
    a2 = (a2) + (24);
    v_rdi = ((unsigned int)((unsigned int)(result))) - (1);
    if (condition_is_not_equal) goto loc_005BC0E1;
loc_005BC10A:
    a2 = (*(unsigned __int16 *)(v_rip + 9853367)) << (3);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x4347414BULL), *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9853616) + 0 + 0 * 2 * 8 + 6));
    if (result == 0) goto loc_005BC2C7;
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 9853328)))) goto loc_005BC177;
    a2 = (*(unsigned __int64 *)(v_rip + 9853351)) + (16);
loc_005BC150:
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 - 11)) & (5));
    if (((unsigned __int8)(result)) != 1) goto loc_005BC16E;
    v_rdi = 0;
    if ((*(unsigned __int64 *)(a2)) == 0) {
        result = 0;
        a1 = a2 - 16;
        v_rdi = (unsigned __int16)((0) + (1));
        *(unsigned __int64 *)(result + result * 8) = a1;
    }
    a2 = (a2) + (24);
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 9853328)))) - (1);
    if (condition_is_not_equal) goto loc_005BC150;
loc_005BC177:
    result = qsort(result, (unsigned int)((unsigned int)((unsigned __int16)(v_rdi))), 8, v_rip + 1439);
    if (0 >= ((unsigned __int16)(v_rdi))) goto loc_005BC1AE;
loc_005BC19A:
    *(unsigned __int16 *)(*(unsigned __int64 *)(result) + 8) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(result) + 6));
    v_rbp = ((unsigned __int16)(v_rdi)) - (1);
    if (condition_is_not_equal) goto loc_005BC19A;
loc_005BC1AE:
loc_005BC1B5:
    if (0 >= (*(unsigned __int16 *)(v_rip + 10522204))) goto loc_005BC277;
    result = *(unsigned __int16 *)(v_rip + 10522187);
    if (0 < ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 10522187)))) {
        a3 = (unsigned int)(*(unsigned __int16 *)(v_rip + 10522187));
        a2 = v_stack_mB8;
        a3 = (a3) << (2);
        a1 = v_stack_m138;
        result = memcpy(a1, a2, a3, v_rip + 1439);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 * 4 + 32)))) < ((unsigned int)(*(unsigned __int8 *)(a1 + 4)))) goto loc_005BC26B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp + 0 * 4 + 32))) - ((unsigned int)(*(unsigned __int8 *)(a1 + 4))));
    *(unsigned __int16 *)(a1 + 6) = 0;
    *(unsigned int *)(v_rsp + 0 * 4 + 32) = (unsigned int)(result);
    if (0 >= ((unsigned __int16)(v_rdi))) goto loc_005BC266;
loc_005BC20B:
    if ((*(unsigned __int64 *)(result + 0 * 8)) == a1) goto loc_005BC25D;
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 10522102)))) goto loc_005BC258;
loc_005BC22D:
    result = (unsigned int)(*(unsigned int *)(v_rsp + 0 * 4 + 32));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 * 4 + 32)))) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 0 * 8) + 4)))) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp + 0 * 4 + 32))) - ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 0 * 8) + 4))));
        *(unsigned __int16 *)(*(unsigned __int64 *)(result + 0 * 8) + 6) = 0;
        *(unsigned int *)(v_rsp + 0 * 4 + 32) = (unsigned int)(result);
    }
    a1 = (unsigned __int16)((0) + (1));
    if (((unsigned __int16)(a1)) < ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 10522053)))) goto loc_005BC22D;
loc_005BC258:
    if (((unsigned __int16)(a1)) == ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 10522053)))) goto loc_005BC266;
loc_005BC25D:
    a2 = (unsigned __int16)((0) + (1));
    if (((unsigned __int16)(a2)) < ((unsigned __int16)(v_rdi))) goto loc_005BC20B;
loc_005BC266:
    if (((unsigned __int16)(a2)) == ((unsigned __int16)(v_rdi))) goto loc_005BC274;
loc_005BC26B:
    v_rbp = (unsigned __int16)((0) + (1));
    goto loc_005BC1B5;
loc_005BC274:
loc_005BC277:
    if (0 >= ((unsigned __int16)(v_rdi))) goto loc_005BC2BD;
loc_005BC283:
    if (1 == 0) goto loc_005BC2A7;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 5)) & (253));
    a1 = (unsigned __int8)((a1) & (2));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 5) = (unsigned __int8)(result);
    goto loc_005BC2AF;
loc_005BC2A7:
    *(unsigned __int16 *)(*(unsigned __int64 *)(result) + 6) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(result) + 8));
loc_005BC2AF:
    a3 = (result) + (8);
    *(unsigned __int16 *)(*(unsigned __int64 *)(result) + 8) = 0;
    v_rdi = ((unsigned __int16)(v_rdi)) - (1);
    if (condition_is_not_equal) goto loc_005BC283;
loc_005BC2BD:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, 0);
loc_005BC2C7:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 0);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiAdjustGroupConfiguration(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x84E79C)) ^ (local_rsp);
    v_stack_m38 = result;
    Arg2 = 0;
    result = memset(v_stack_m138, Arg2, 128, a4);
    if (((*(uint8_t *)(arg1 + 0x5)) & (4)) != 0) goto loc_005BC2C7;
    local_r15 = 0;
    result = *(uint16_t *)(v_rip + 0xA0903F);
    if (0 < ((uint16_t)(*(uint16_t *)(v_rip + 0xA0903F)))) {
        Arg1 = (uint32_t)(*(uint16_t *)(v_rip + 0xA0903F));
        local_rdi = v_stack_m138;
        result = *(uint32_t *)(v_rip + 0xA09059);
    }
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x965AD4)))) goto loc_005BC027;
    Arg2 = (*(uint64_t *)(v_rip + 0x965AE9)) + (6);
loc_005BC00D:
    if (((*(uint8_t *)(Arg2 - 0x1)) & (1)) != 0) {
        Arg1 = *(uint16_t *)(Arg2);
        result = *(uint8_t *)(Arg2 - 0x2);
    }
    Arg2 = (Arg2) + (24);
    local_rdi = ((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x965AD4)))) - (1);
    if (condition_is_not_equal) goto loc_005BC00D;
loc_005BC027:
loc_005BC02B:
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x965A95)))) goto loc_005BC0AE;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x965AB0) + 0x0 + 0x0 * 2 * 8 + 0x5)) & (7));
    if (((uint8_t)(result)) != 3) goto loc_005BC088;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x965AB0) + 0x0 + 0x0 * 2 * 8 + 0x10)) != 0) goto loc_005BC088;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0x965AB0) + 0x0 + 0x0 * 2 * 8 + 0x4))) <= ((uint8_t)(*(uint8_t *)(arg1 + 0x4)))) goto loc_005BC071;
    a3 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x965AB0) + 0x0 + 0x0 * 2 * 8 + 0x4)) - ((uint32_t)(*(uint8_t *)(arg1 + 0x4))));
    goto loc_005BC07D;
loc_005BC071:
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x4)) - ((uint32_t)(a3)));
loc_005BC07D:
    if ((*(uint32_t *)(local_rsp + (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x965AB0) + 0x0 + 0x0 * 2 * 8 + 0x6)) * 4 + 0x20)) >= ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_005BC08E;
loc_005BC088:
    Arg1 = (uint16_t)((0) + (1));
    goto loc_005BC02B;
loc_005BC08E:
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x965AB0) + 0x0 + 0x0 * 2 * 8 + 0x6) = (uint16_t)(*(uint16_t *)(arg1 + 0x6));
    *(uint16_t *)(arg1 + 0x6) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x965AB0) + 0x0 + 0x0 * 2 * 8 + 0x6));
    goto loc_005BC2C7;
loc_005BC0AE:
    result = *(uint16_t *)(v_rip + 0xA08F5F);
    local_rdi = *(uint64_t *)(v_rip + 0x965AB0);
    if (0 < ((uint16_t)(*(uint16_t *)(v_rip + 0xA08F5F)))) {
        Arg1 = (uint32_t)(*(uint16_t *)(v_rip + 0xA08F5F));
        local_rdi = v_stack_mB8;
        result = *(uint32_t *)(v_rip + 0xA08F79);
    }
    if (0 >= ((uint16_t)((uint32_t)((uint32_t)(result))))) goto loc_005BC10A;
    Arg2 = (*(uint64_t *)(v_rip + 0x965A16)) + (16);
loc_005BC0E1:
    if (((1) & ((uint8_t)(*(uint8_t *)(Arg2 - 0xB)))) == 0) goto loc_005BC101;
    if ((((uint8_t)(*(uint8_t *)(Arg2 - 0xB))) & (4)) != 0) goto loc_005BC0F2;
    result = *(uint8_t *)(Arg2 - 0xB);
    if ((*(uint64_t *)(Arg2)) != 0) {
        Arg1 = *(uint16_t *)(Arg2 - 0xA);
        result = *(uint8_t *)(Arg2 - 0xC);
    }
    Arg2 = (Arg2) + (24);
    local_rdi = ((uint32_t)((uint32_t)(result))) - (1);
    if (condition_is_not_equal) goto loc_005BC0E1;
loc_005BC10A:
    Arg2 = (*(uint16_t *)(v_rip + 0x9659B7)) << (3);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x4347414BULL), *(uint16_t *)(*(uint64_t *)(v_rip + 0x965AB0) + 0x0 + 0x0 * 2 * 8 + 0x6));
    if (result == 0) goto loc_005BC2C7;
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x965990)))) goto loc_005BC177;
    Arg2 = (*(uint64_t *)(v_rip + 0x9659A7)) + (16);
loc_005BC150:
    result = (uint8_t)((*(uint8_t *)(Arg2 - 0xB)) & (5));
    if (((uint8_t)(result)) != 1) goto loc_005BC16E;
    local_rdi = 0;
    if ((*(uint64_t *)(Arg2)) == 0) {
        result = 0;
        Arg1 = Arg2 - 16;
        local_rdi = (uint16_t)((0) + (1));
        *(void **)(result + result * 8) = Arg1;
    }
    Arg2 = (Arg2) + (24);
    a3 = ((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x965990)))) - (1);
    if (condition_is_not_equal) goto loc_005BC150;
loc_005BC177:
    result = qsort(result, (uint32_t)((uint32_t)((uint16_t)(local_rdi))), 8, v_rip + 1439);
    if (0 >= ((uint16_t)(local_rdi))) goto loc_005BC1AE;
loc_005BC19A:
    *(uint16_t *)(*(uint64_t *)(result) + 0x8) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(result) + 0x6));
    local_rbp = ((uint16_t)(local_rdi)) - (1);
    if (condition_is_not_equal) goto loc_005BC19A;
loc_005BC1AE:
loc_005BC1B5:
    if (0 >= (*(uint16_t *)(v_rip + 0xA08E5C))) goto loc_005BC277;
    result = *(uint16_t *)(v_rip + 0xA08E4B);
    if (0 < ((uint16_t)(*(uint16_t *)(v_rip + 0xA08E4B)))) {
        a3 = (uint32_t)(*(uint16_t *)(v_rip + 0xA08E4B));
        Arg2 = v_stack_mB8;
        a3 = (a3) << (2);
        Arg1 = v_stack_m138;
        result = memcpy(Arg1, Arg2, a3, v_rip + 1439);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 4 + 0x20)))) < ((uint32_t)(*(uint8_t *)(arg1 + 0x4)))) goto loc_005BC26B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 4 + 0x20))) - ((uint32_t)(*(uint8_t *)(arg1 + 0x4))));
    *(uint16_t *)(arg1 + 0x6) = 0;
    *(uint32_t *)(local_rsp + 0x0 * 4 + 0x20) = (uint32_t)(result);
    if (0 >= ((uint16_t)(local_rdi))) goto loc_005BC266;
loc_005BC20B:
    if ((*(uint64_t *)(result + 0x0 * 8)) == Arg1) goto loc_005BC25D;
    if (0 >= ((uint16_t)(*(uint16_t *)(v_rip + 0xA08DF6)))) goto loc_005BC258;
loc_005BC22D:
    result = (uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 4 + 0x20));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 4 + 0x20)))) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x0 * 8) + 0x4)))) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 4 + 0x20))) - ((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x0 * 8) + 0x4))));
        *(uint16_t *)(*(uint64_t *)(result + 0x0 * 8) + 0x6) = 0;
        *(uint32_t *)(local_rsp + 0x0 * 4 + 0x20) = (uint32_t)(result);
    }
    Arg1 = (uint16_t)((0) + (1));
    if (((uint16_t)(Arg1)) < ((uint16_t)(*(uint16_t *)(v_rip + 0xA08DC5)))) goto loc_005BC22D;
loc_005BC258:
    if (((uint16_t)(Arg1)) == ((uint16_t)(*(uint16_t *)(v_rip + 0xA08DC5)))) goto loc_005BC266;
loc_005BC25D:
    Arg2 = (uint16_t)((0) + (1));
    if (((uint16_t)(Arg2)) < ((uint16_t)(local_rdi))) goto loc_005BC20B;
loc_005BC266:
    if (((uint16_t)(Arg2)) == ((uint16_t)(local_rdi))) goto loc_005BC274;
loc_005BC26B:
    local_rbp = (uint16_t)((0) + (1));
    goto loc_005BC1B5;
loc_005BC274:
loc_005BC277:
    if (0 >= ((uint16_t)(local_rdi))) goto loc_005BC2BD;
loc_005BC283:
    if (1 == 0) goto loc_005BC2A7;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x5)) & (253));
    Arg1 = (uint8_t)((Arg1) & (2));
    result = (uint8_t)((result) | ((uint8_t)(Arg1)));
    *(uint8_t *)(*(uint64_t *)(result) + 0x5) = (uint8_t)(result);
    goto loc_005BC2AF;
loc_005BC2A7:
    *(uint16_t *)(*(uint64_t *)(result) + 0x6) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(result) + 0x8));
loc_005BC2AF:
    a3 = (result) + (8);
    *(uint16_t *)(*(uint64_t *)(result) + 0x8) = 0;
    local_rdi = ((uint16_t)(local_rdi)) - (1);
    if (condition_is_not_equal) goto loc_005BC283;
loc_005BC2BD:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, 0);
loc_005BC2C7:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, 0);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x5` | `8` | `R` |
| `Arg1` | `+ 0x5` | `8` | `R/W` |
| `Arg1` | `+ 0x6` | `16` | `R` |
| `Arg1` | `+ 0x6` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BBF84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
