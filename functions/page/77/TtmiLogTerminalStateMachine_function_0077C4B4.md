# TtmiLogTerminalStateMachine

- RVA: `0x0077C4B4`–`0x0077C711` (길이 `605` bytes)
- VA: `0x000000014077C4B4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDD74`
- 디코드: `122`개 명령, `605/605` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077C508` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077C525` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0077C6DF` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077C6EE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpUpdateTerminalState](TtmpUpdateTerminalState_function_0077D7D0.md) at `0x0077D88E`

### Static image references
- `0x0077C4D6` → RVA `0x00E0A740` (`.data`; read)
- `0x0077C4E7` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077C6C6` → RVA `0x000523D4` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0077C508` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077C525` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0077C6DF` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077C6EE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077C4B4  48 8B C4                        mov rax, rsp
0077C4B7  48 89 58 08                     mov qword ptr [rax + 8], rbx
0077C4BB  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0077C4BF  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0077C4C3  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
0077C4C7  55                              push rbp
0077C4C8  48 8D A8 48 FF FF FF            lea rbp, [rax - 0xb8]
0077C4CF  48 81 EC B0 01 00 00            sub rsp, 0x1b0
0077C4D6  48 8B 05 63 E2 68 00            mov rax, qword ptr [rip + 0x68e263]
0077C4DD  48 33 C4                        xor rax, rsp
0077C4E0  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
0077C4E7  83 3D DA C3 85 00 05            cmp dword ptr [rip + 0x85c3da], 5
0077C4EE  49 8B F8                        mov rdi, r8
0077C4F1  48 8B DA                        mov rbx, rdx
0077C4F4  8B F1                           mov esi, ecx
0077C4F6  0F 86 E8 01 00 00               jbe 0x14077c6e4
0077C4FC  BA 01 00 00 00                  mov edx, 1
0077C501  48 8D 0D C0 C3 85 00            lea rcx, [rip + 0x85c3c0]
0077C508  E8 93 25 CB FF                  call 0x14042eaa0
0077C50D  84 C0                           test al, al
0077C50F  0F 84 CF 01 00 00               je 0x14077c6e4
0077C515  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0077C51E  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0077C525  E8 C6 33 AB FF                  call 0x14022f8f0
0077C52A  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0077C52E  48 8D 44 24 34                  lea rax, [rsp + 0x34]
0077C533  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0077C537  48 8D 44 24 38                  lea rax, [rsp + 0x38]
0077C53C  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0077C540  8B 03                           mov eax, dword ptr [rbx]
0077C542  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
0077C546  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
0077C54B  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0077C54F  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0077C553  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0077C558  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0077C55D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0077C561  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0077C565  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0077C56A  48 8D 44 24 58                  lea rax, [rsp + 0x58]
0077C56F  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0077C573  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0077C577  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0077C57C  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0077C581  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0077C585  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
0077C589  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0077C58E  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0077C593  48 89 45 00                     mov qword ptr [rbp], rax
0077C597  8A 43 28                        mov al, byte ptr [rbx + 0x28]
0077C59A  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0077C59E  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0077C5A3  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0077C5A7  8A 43 29                        mov al, byte ptr [rbx + 0x29]
0077C5AA  88 44 24 31                     mov byte ptr [rsp + 0x31], al
0077C5AE  48 8D 44 24 31                  lea rax, [rsp + 0x31]
0077C5B3  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0077C5B7  8B 43 2C                        mov eax, dword ptr [rbx + 0x2c]
0077C5BA  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0077C5BE  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0077C5C3  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0077C5C7  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0077C5CA  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0077C5CE  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0077C5D3  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
0077C5D7  8B 07                           mov eax, dword ptr [rdi]
0077C5D9  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0077C5DD  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0077C5E2  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0077C5E6  8A 47 04                        mov al, byte ptr [rdi + 4]
0077C5E9  88 44 24 32                     mov byte ptr [rsp + 0x32], al
0077C5ED  48 8D 44 24 32                  lea rax, [rsp + 0x32]
0077C5F2  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0077C5F6  8B 47 08                        mov eax, dword ptr [rdi + 8]
0077C5F9  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
0077C5FD  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
0077C602  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
0077C606  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0077C60A  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0077C60F  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0077C614  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
0077C61B  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0077C61F  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0077C624  48 8D 44 24 78                  lea rax, [rsp + 0x78]
0077C629  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
0077C630  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
0077C638  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0077C63C  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
0077C644  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
0077C64C  48 C7 45 D8 08 00 00 00         mov qword ptr [rbp - 0x28], 8
0077C654  48 C7 45 E8 08 00 00 00         mov qword ptr [rbp - 0x18], 8
0077C65C  48 C7 45 F8 08 00 00 00         mov qword ptr [rbp - 8], 8
0077C664  48 C7 45 08 08 00 00 00         mov qword ptr [rbp + 8], 8
0077C66C  48 C7 45 18 01 00 00 00         mov qword ptr [rbp + 0x18], 1
0077C674  48 C7 45 28 01 00 00 00         mov qword ptr [rbp + 0x28], 1
0077C67C  48 C7 45 38 04 00 00 00         mov qword ptr [rbp + 0x38], 4
0077C684  48 C7 45 48 04 00 00 00         mov qword ptr [rbp + 0x48], 4
0077C68C  48 C7 45 58 04 00 00 00         mov qword ptr [rbp + 0x58], 4
0077C694  48 C7 45 68 01 00 00 00         mov qword ptr [rbp + 0x68], 1
0077C69C  48 C7 45 78 04 00 00 00         mov qword ptr [rbp + 0x78], 4
0077C6A4  48 C7 85 88 00 00 00 08 00 00 00  mov qword ptr [rbp + 0x88], 8
0077C6AF  48 C7 85 98 00 00 00 08 00 00 00  mov qword ptr [rbp + 0x98], 8
0077C6BA  48 8D 45 80                     lea rax, [rbp - 0x80]
0077C6BE  45 33 C9                        xor r9d, r9d
0077C6C1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077C6C6  48 8D 15 07 5D 8D FF            lea rdx, [rip - 0x72a2f9]
0077C6CD  45 33 C0                        xor r8d, r8d
0077C6D0  C7 44 24 20 12 00 00 00         mov dword ptr [rsp + 0x20], 0x12
0077C6D8  48 8D 0D E9 C1 85 00            lea rcx, [rip + 0x85c1e9]
0077C6DF  E8 FC 99 CA FF                  call 0x1404260e0
0077C6E4  48 8B 8D A0 00 00 00            mov rcx, qword ptr [rbp + 0xa0]
0077C6EB  48 33 CC                        xor rcx, rsp
0077C6EE  E8 4D FF F2 FF                  call 0x1406ac640
0077C6F3  4C 8D 9C 24 B0 01 00 00         lea r11, [rsp + 0x1b0]
0077C6FB  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0077C6FF  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
0077C703  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
0077C707  4D 8B 73 28                     mov r14, qword ptr [r11 + 0x28]
0077C70B  49 8B E3                        mov rsp, r11
0077C70E  5D                              pop rbp
0077C70F  C3                              ret
0077C710  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogTerminalStateMachine(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m184;
    unsigned __int8 v_stack_m186;
    unsigned __int8 v_stack_m187;
    unsigned __int8 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (432);
    result = (*(unsigned __int64 *)(v_rip + 6873699)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 184 + 160) = result;
    if ((*(unsigned int *)(v_rip + 8766426)) <= 5) goto loc_0077C6E4;
    result = tlgKeywordOn(v_rip + 8766400, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        v_stack_m184 = (unsigned int)(result);
        result = v_stack_m184;
        *(unsigned __int64 *)(v_rsp - 184 - 96) = result;
        result = v_stack_m180;
        *(unsigned __int64 *)(v_rsp - 184 - 80) = result;
        result = *(unsigned int *)(a2);
        v_stack_m17C = (unsigned int)(result);
        result = v_stack_m17C;
        *(unsigned __int64 *)(v_rsp - 184 - 64) = result;
        result = *(unsigned __int64 *)(a2 + 8);
        v_stack_m168 = result;
        result = v_stack_m168;
        *(unsigned __int64 *)(v_rsp - 184 - 48) = result;
        result = *(unsigned __int64 *)(a2 + 16);
        v_stack_m160 = result;
        result = v_stack_m160;
        *(unsigned __int64 *)(v_rsp - 184 - 32) = result;
        result = *(unsigned __int64 *)(a2 + 24);
        v_stack_m158 = result;
        result = v_stack_m158;
        *(unsigned __int64 *)(v_rsp - 184 - 16) = result;
        result = *(unsigned __int64 *)(a2 + 32);
        v_stack_m150 = result;
        result = v_stack_m150;
        *(unsigned __int64 *)(v_rsp - 184) = result;
        result = *(unsigned __int8 *)(a2 + 40);
        v_stack_m188 = (unsigned __int8)(result);
        result = v_stack_m188;
        *(unsigned __int64 *)(v_rsp - 184 + 16) = result;
        result = *(unsigned __int8 *)(a2 + 41);
        v_stack_m187 = (unsigned __int8)(result);
        result = v_stack_m187;
        *(unsigned __int64 *)(v_rsp - 184 + 32) = result;
        result = *(unsigned int *)(a2 + 44);
        v_stack_m178 = (unsigned int)(result);
        result = v_stack_m178;
        *(unsigned __int64 *)(v_rsp - 184 + 48) = result;
        result = *(unsigned int *)(a2 + 48);
        v_stack_m174 = (unsigned int)(result);
        result = v_stack_m174;
        *(unsigned __int64 *)(v_rsp - 184 + 64) = result;
        result = *(unsigned int *)(a3);
        v_stack_m170 = (unsigned int)(result);
        result = v_stack_m170;
        *(unsigned __int64 *)(v_rsp - 184 + 80) = result;
        result = *(unsigned __int8 *)(a3 + 4);
        v_stack_m186 = (unsigned __int8)(result);
        result = v_stack_m186;
        *(unsigned __int64 *)(v_rsp - 184 + 96) = result;
        result = *(unsigned int *)(a3 + 8);
        v_stack_m16C = (unsigned int)(result);
        result = v_stack_m16C;
        *(unsigned __int64 *)(v_rsp - 184 + 112) = result;
        result = *(unsigned __int64 *)(a3 + 16);
        v_stack_m148 = result;
        result = v_stack_m148;
        *(unsigned __int64 *)(v_rsp - 184 + 128) = result;
        result = *(unsigned __int64 *)(a3 + 24);
        v_stack_m140 = result;
        result = v_stack_m140;
        *(unsigned __int64 *)(v_rsp - 184 + 144) = result;
        *(unsigned __int64 *)(v_rsp - 184 - 88) = 4;
        v_stack_m180 = (unsigned int)((unsigned int)(a1));
        *(unsigned __int64 *)(v_rsp - 184 - 72) = 4;
        *(unsigned __int64 *)(v_rsp - 184 - 56) = 4;
        *(unsigned __int64 *)(v_rsp - 184 - 40) = 8;
        *(unsigned __int64 *)(v_rsp - 184 - 24) = 8;
        *(unsigned __int64 *)(v_rsp - 184 - 8) = 8;
        *(unsigned __int64 *)(v_rsp - 184 + 8) = 8;
        *(unsigned __int64 *)(v_rsp - 184 + 24) = 1;
        *(unsigned __int64 *)(v_rsp - 184 + 40) = 1;
        *(unsigned __int64 *)(v_rsp - 184 + 56) = 4;
        *(unsigned __int64 *)(v_rsp - 184 + 72) = 4;
        *(unsigned __int64 *)(v_rsp - 184 + 88) = 4;
        *(unsigned __int64 *)(v_rsp - 184 + 104) = 1;
        *(unsigned __int64 *)(v_rsp - 184 + 120) = 4;
        *(unsigned __int64 *)(v_rsp - 184 + 136) = 8;
        *(unsigned __int64 *)(v_rsp - 184 + 152) = 8;
        result = v_rsp - 184 - 128;
        a4 = 0;
        v_stack_m190 = result;
        a2 = v_rip - 7512825;
        a3 = 0;
        v_stack_m198 = 18;
        a1 = v_rip + 8765929;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 184 + 160)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogTerminalStateMachine(int32_t Arg1, void *Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint64_t v_stack_m180;
    uint32_t v_stack_m184;
    uint8_t v_stack_m186;
    uint8_t v_stack_m187;
    uint8_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (432);
    result = (*(uint64_t *)(v_rip + 0x68E263)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xB8 + 0xA0) = result;
    if ((*(uint32_t *)(v_rip + 0x85C3DA)) <= 5) goto loc_0077C6E4;
    result = tlgKeywordOn(v_rip + 8766400, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        v_stack_m184 = (uint32_t)(result);
        result = v_stack_m184;
        *(uint64_t *)(local_rsp - 0xB8 - 0x60) = result;
        result = v_stack_m180;
        *(uint64_t *)(local_rsp - 0xB8 - 0x50) = result;
        result = *(uint32_t *)(arg2);
        v_stack_m17C = (uint32_t)(result);
        result = v_stack_m17C;
        *(uint64_t *)(local_rsp - 0xB8 - 0x40) = result;
        result = *(uint64_t *)(arg2 + 0x8);
        v_stack_m168 = result;
        result = v_stack_m168;
        *(uint64_t *)(local_rsp - 0xB8 - 0x30) = result;
        result = *(uint64_t *)(arg2 + 0x10);
        v_stack_m160 = result;
        result = v_stack_m160;
        *(uint64_t *)(local_rsp - 0xB8 - 0x20) = result;
        result = *(uint64_t *)(arg2 + 0x18);
        v_stack_m158 = result;
        result = v_stack_m158;
        *(uint64_t *)(local_rsp - 0xB8 - 0x10) = result;
        result = *(uint64_t *)(arg2 + 0x20);
        v_stack_m150 = result;
        result = v_stack_m150;
        *(uint64_t *)(local_rsp - 0xB8) = result;
        result = *(uint8_t *)(arg2 + 0x28);
        v_stack_m188 = (uint8_t)(result);
        result = v_stack_m188;
        *(uint64_t *)(local_rsp - 0xB8 + 0x10) = result;
        result = *(uint8_t *)(arg2 + 0x29);
        v_stack_m187 = (uint8_t)(result);
        result = v_stack_m187;
        *(uint64_t *)(local_rsp - 0xB8 + 0x20) = result;
        result = *(uint32_t *)(arg2 + 0x2C);
        v_stack_m178 = (uint32_t)(result);
        result = v_stack_m178;
        *(uint64_t *)(local_rsp - 0xB8 + 0x30) = result;
        result = *(uint32_t *)(arg2 + 0x30);
        v_stack_m174 = (uint32_t)(result);
        result = v_stack_m174;
        *(uint64_t *)(local_rsp - 0xB8 + 0x40) = result;
        result = *(uint32_t *)(arg3);
        v_stack_m170 = (uint32_t)(result);
        result = v_stack_m170;
        *(uint64_t *)(local_rsp - 0xB8 + 0x50) = result;
        result = *(uint8_t *)(arg3 + 0x4);
        v_stack_m186 = (uint8_t)(result);
        result = v_stack_m186;
        *(uint64_t *)(local_rsp - 0xB8 + 0x60) = result;
        result = *(uint32_t *)(arg3 + 0x8);
        v_stack_m16C = (uint32_t)(result);
        result = v_stack_m16C;
        *(uint64_t *)(local_rsp - 0xB8 + 0x70) = result;
        result = *(uint64_t *)(arg3 + 0x10);
        v_stack_m148 = result;
        result = v_stack_m148;
        *(uint64_t *)(local_rsp - 0xB8 + 0x80) = result;
        result = *(uint64_t *)(arg3 + 0x18);
        v_stack_m140 = result;
        result = v_stack_m140;
        *(uint64_t *)(local_rsp - 0xB8 + 0x90) = result;
        *(uint64_t *)(local_rsp - 0xB8 - 0x58) = 4;
        v_stack_m180 = (uint32_t)((uint32_t)(Arg1));
        *(uint64_t *)(local_rsp - 0xB8 - 0x48) = 4;
        *(uint64_t *)(local_rsp - 0xB8 - 0x38) = 4;
        *(uint64_t *)(local_rsp - 0xB8 - 0x28) = 8;
        *(uint64_t *)(local_rsp - 0xB8 - 0x18) = 8;
        *(uint64_t *)(local_rsp - 0xB8 - 0x8) = 8;
        *(uint64_t *)(local_rsp - 0xB8 + 0x8) = 8;
        *(uint64_t *)(local_rsp - 0xB8 + 0x18) = 1;
        *(uint64_t *)(local_rsp - 0xB8 + 0x28) = 1;
        *(uint64_t *)(local_rsp - 0xB8 + 0x38) = 4;
        *(uint64_t *)(local_rsp - 0xB8 + 0x48) = 4;
        *(uint64_t *)(local_rsp - 0xB8 + 0x58) = 4;
        *(uint64_t *)(local_rsp - 0xB8 + 0x68) = 1;
        *(uint64_t *)(local_rsp - 0xB8 + 0x78) = 4;
        *(uint64_t *)(local_rsp - 0xB8 + 0x88) = 8;
        *(uint64_t *)(local_rsp - 0xB8 + 0x98) = 8;
        result = local_rsp - 184 - 128;
        Arg4 = 0;
        v_stack_m190 = result;
        Arg2 = v_rip - 7512825;
        Arg3 = 0;
        v_stack_m198 = 18;
        Arg1 = v_rip + 8765929;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0xB8 + 0xA0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `8` | `R` |
| `Arg2` | `+ 0x29` | `8` | `R` |
| `Arg2` | `+ 0x2C` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x4` | `8` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077C4B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077C4B4[BB_0077C4B4]
  bb_0077C4FC[BB_0077C4FC]
  bb_0077C515[BB_0077C515]
  bb_0077C6E4[BB_0077C6E4]
  bb_0077C710[BB_0077C710]
  bb_0077C4B4 -->|branch| bb_0077C6E4
  bb_0077C4B4 -->|fallthrough| bb_0077C4FC
  bb_0077C4FC -->|branch| bb_0077C6E4
  bb_0077C4FC -->|fallthrough| bb_0077C515
  bb_0077C515 -->|flow| bb_0077C6E4
```
