# PopSqmThermalZoneEnumeration

- RVA: `0x00772884`–`0x00772A4A` (길이 `454` bytes)
- VA: `0x0000000140772884`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CD834`
- 디코드: `101`개 명령, `454/454` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x007728DA` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007728EF` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (function, `0x00426198`)
- `0x007729E0` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (function, `0x00426198`)
- `0x00772A27` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00772A33` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopDiagTraceThermalZoneEnumeration](../../text/5D/PopDiagTraceThermalZoneEnumeration_function_005D7154.md) at `0x005D74A4`

### Static image references
- `0x00772896` → RVA `0x00E0A740` (`.data`; read)
- `0x007728A8` → RVA `0x00AFCAD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007728BC` → RVA `0x00E07748` (`.data`; read)
- `0x007729F5` → RVA `0x00050F49` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x007728DA` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007728EF` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (`PAGE` → `.text`)
  - `0x007729E0` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (`PAGE` → `.text`)
  - `0x00772A27` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00772A33` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00772884  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00772889  55                              push rbp
0077288A  48 8D 6C 24 B0                  lea rbp, [rsp - 0x50]
0077288F  48 81 EC 50 01 00 00            sub rsp, 0x150
00772896  48 8B 05 A3 7E 69 00            mov rax, qword ptr [rip + 0x697ea3]
0077289D  48 33 C4                        xor rax, rsp
007728A0  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
007728A4  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
007728A8  4C 8D 15 21 A2 38 00            lea r10, [rip + 0x38a221]
007728AF  48 85 C0                        test rax, rax
007728B2  45 8B D8                        mov r11d, r8d
007728B5  4C 8B C1                        mov r8, rcx
007728B8  4C 0F 45 D0                     cmovne r10, rax
007728BC  83 3D 85 4E 69 00 05            cmp dword ptr [rip + 0x694e85], 5
007728C3  0F 86 63 01 00 00               jbe 0x140772a2c
007728C9  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
007728D3  48 8D 0D 6E 4E 69 00            lea rcx, [rip + 0x694e6e]
007728DA  E8 C1 C1 CB FF                  call 0x14042eaa0
007728DF  84 C0                           test al, al
007728E1  0F 84 45 01 00 00               je 0x140772a2c
007728E7  49 8B 50 08                     mov rdx, qword ptr [r8 + 8]
007728EB  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007728EF  E8 A4 38 CB FF                  call 0x140426198
007728F4  8B 8D 90 00 00 00               mov ecx, dword ptr [rbp + 0x90]
007728FA  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007728FF  83 65 9C 00                     and dword ptr [rbp - 0x64], 0
00772903  BB 04 00 00 00                  mov ebx, 4
00772908  83 65 AC 00                     and dword ptr [rbp - 0x54], 0
0077290C  49 8B D2                        mov rdx, r10
0077290F  83 65 BC 00                     and dword ptr [rbp - 0x44], 0
00772913  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
00772917  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
0077291B  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
0077291F  83 65 FC 00                     and dword ptr [rbp - 4], 0
00772923  83 65 0C 00                     and dword ptr [rbp + 0xc], 0
00772927  83 65 1C 00                     and dword ptr [rbp + 0x1c], 0
0077292B  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0077292F  8B 85 98 00 00 00               mov eax, dword ptr [rbp + 0x98]
00772935  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00772939  48 8D 44 24 34                  lea rax, [rsp + 0x34]
0077293E  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00772942  8B 85 A0 00 00 00               mov eax, dword ptr [rbp + 0xa0]
00772948  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0077294C  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00772951  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00772955  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
0077295A  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0077295E  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
00772964  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00772968  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0077296D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00772971  8B 85 A8 00 00 00               mov eax, dword ptr [rbp + 0xa8]
00772977  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0077297B  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00772980  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00772984  8B 85 88 00 00 00               mov eax, dword ptr [rbp + 0x88]
0077298A  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0077298E  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00772993  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00772997  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
0077299C  48 89 45 00                     mov qword ptr [rbp], rax
007729A0  8B 85 80 00 00 00               mov eax, dword ptr [rbp + 0x80]
007729A6  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
007729AA  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007729AF  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
007729B3  48 8D 4D 20                     lea rcx, [rbp + 0x20]
007729B7  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
007729BB  89 5D 98                        mov dword ptr [rbp - 0x68], ebx
007729BE  89 5D A8                        mov dword ptr [rbp - 0x58], ebx
007729C1  89 5D B8                        mov dword ptr [rbp - 0x48], ebx
007729C4  44 89 5C 24 3C                  mov dword ptr [rsp + 0x3c], r11d
007729C9  89 5D C8                        mov dword ptr [rbp - 0x38], ebx
007729CC  89 5D D8                        mov dword ptr [rbp - 0x28], ebx
007729CF  89 5D E8                        mov dword ptr [rbp - 0x18], ebx
007729D2  89 5D F8                        mov dword ptr [rbp - 8], ebx
007729D5  44 89 4C 24 4C                  mov dword ptr [rsp + 0x4c], r9d
007729DA  89 5D 08                        mov dword ptr [rbp + 8], ebx
007729DD  89 5D 18                        mov dword ptr [rbp + 0x18], ebx
007729E0  E8 B3 37 CB FF                  call 0x140426198
007729E5  44 8B 8D B8 00 00 00            mov r9d, dword ptr [rbp + 0xb8]
007729EC  48 8D 44 24 54                  lea rax, [rsp + 0x54]
007729F1  83 65 3C 00                     and dword ptr [rbp + 0x3c], 0
007729F5  48 8D 15 4D E5 8D FF            lea rdx, [rip - 0x721ab3]
007729FC  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00772A00  48 8D 0D 41 4D 69 00            lea rcx, [rip + 0x694d41]
00772A07  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00772A0C  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
00772A11  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00772A16  45 33 C9                        xor r9d, r9d
00772A19  45 33 C0                        xor r8d, r8d
00772A1C  C7 44 24 20 0E 00 00 00         mov dword ptr [rsp + 0x20], 0xe
00772A24  89 5D 38                        mov dword ptr [rbp + 0x38], ebx
00772A27  E8 B4 36 CB FF                  call 0x1404260e0
00772A2C  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00772A30  48 33 CC                        xor rcx, rsp
00772A33  E8 08 9C F3 FF                  call 0x1406ac640
00772A38  48 8B 9C 24 70 01 00 00         mov rbx, qword ptr [rsp + 0x170]
00772A40  48 81 C4 50 01 00 00            add rsp, 0x150
00772A47  5D                              pop rbp
00772A48  C3                              ret
00772A49  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSqmThermalZoneEnumeration(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int a10, unsigned int a11, unsigned int a12)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m10C;
    unsigned int v_stack_m110;
    unsigned int v_stack_m114;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned int v_stack_m124;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 6913699)) ^ (v_rsp);
    v_stack_m18 = result;
    v_r10 = v_rip + 3711521;
    if (*(unsigned __int64 *)(a2 + 8) != 0) { v_r10 = *(unsigned __int64 *)(a2 + 8); }
    if ((*(unsigned int *)(v_rip + 6901381)) <= 5) goto loc_00772A2C;
    result = tlgKeywordOn(v_rip + 6901358, a2, a1, a4);
    if ((unsigned __int8)(result) != 0) {
        a2 = *(unsigned __int64 *)(a1 + 8);
        a1 = v_stack_mD8;
        result = tlgCreate1Sz_wchar_t(a1, a2, a1, a4);
        a1 = a7;
        result = v_stack_m128;
        v_rbx = 4;
        a2 = v_r10;
        v_stack_mC8 = result;
        result = a8;
        v_stack_m124 = (unsigned int)(result);
        result = v_stack_m124;
        v_stack_mB8 = result;
        result = a9;
        v_stack_m120 = (unsigned int)(result);
        result = v_stack_m120;
        v_stack_mA8 = result;
        result = v_stack_m11C;
        v_stack_m98 = result;
        result = a11;
        v_stack_m118 = (unsigned int)(result);
        result = v_stack_m118;
        v_stack_m88 = result;
        result = a10;
        v_stack_m114 = (unsigned int)(result);
        result = v_stack_m114;
        v_stack_m78 = result;
        result = a6;
        v_stack_m110 = (unsigned int)(result);
        result = v_stack_m110;
        v_stack_m68 = result;
        result = v_stack_m10C;
        v_stack_m58 = result;
        result = a5;
        v_stack_m108 = (unsigned int)(result);
        result = v_stack_m108;
        v_stack_m128 = (unsigned int)(a1);
        a1 = v_stack_m38;
        v_stack_m48 = result;
        v_stack_mC0 = (unsigned int)(v_rbx);
        v_stack_mB0 = (unsigned int)(v_rbx);
        v_stack_mA0 = (unsigned int)(v_rbx);
        v_stack_m11C = (unsigned int)((unsigned int)(a3));
        v_stack_m90 = (unsigned int)(v_rbx);
        v_stack_m80 = (unsigned int)(v_rbx);
        v_stack_m70 = (unsigned int)(v_rbx);
        v_stack_m60 = (unsigned int)(v_rbx);
        v_stack_m10C = a4;
        v_stack_m50 = (unsigned int)(v_rbx);
        v_stack_m40 = (unsigned int)(v_rbx);
        result = tlgCreate1Sz_wchar_t(a1, a2, a1, a4);
        a4 = a12;
        result = v_stack_m104;
        a2 = v_rip - 7477939;
        v_stack_m28 = result;
        a1 = v_rip + 6901057;
        result = v_stack_mF8;
        v_stack_m104 = a4;
        v_stack_m130 = result;
        a4 = 0;
        a3 = 0;
        v_stack_m138 = 14;
        v_stack_m20 = (unsigned int)(v_rbx);
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (336);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopSqmThermalZoneEnumeration(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, uint32_t Arg6, uint32_t Arg7, uint32_t Arg8, uint32_t Arg9, uint32_t Arg10, uint32_t Arg11, uint32_t Arg12)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m10C;
    uint32_t v_stack_m110;
    uint32_t v_stack_m114;
    uint32_t v_stack_m118;
    uint64_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint32_t v_stack_m124;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0x697EA3)) ^ (local_rsp);
    v_stack_m18 = result;
    local_r10 = v_rip + 3711521;
    if (*(uint64_t *)(arg2 + 0x8) != 0) { local_r10 = *(uint64_t *)(arg2 + 0x8); }
    if ((*(uint32_t *)(v_rip + 0x694E85)) <= 5) goto loc_00772A2C;
    result = tlgKeywordOn(v_rip + 6901358, Arg2, Arg1, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg2 = *(uint64_t *)(Arg1 + 0x8);
        Arg1 = v_stack_mD8;
        result = tlgCreate1Sz_wchar_t(Arg1, Arg2, Arg1, Arg4);
        Arg1 = Arg7;
        result = v_stack_m128;
        local_rbx = 4;
        Arg2 = local_r10;
        v_stack_mC8 = result;
        result = Arg8;
        v_stack_m124 = (uint32_t)(result);
        result = v_stack_m124;
        v_stack_mB8 = result;
        result = Arg9;
        v_stack_m120 = (uint32_t)(result);
        result = v_stack_m120;
        v_stack_mA8 = result;
        result = v_stack_m11C;
        v_stack_m98 = result;
        result = Arg11;
        v_stack_m118 = (uint32_t)(result);
        result = v_stack_m118;
        v_stack_m88 = result;
        result = Arg10;
        v_stack_m114 = (uint32_t)(result);
        result = v_stack_m114;
        v_stack_m78 = result;
        result = Arg6;
        v_stack_m110 = (uint32_t)(result);
        result = v_stack_m110;
        v_stack_m68 = result;
        result = v_stack_m10C;
        v_stack_m58 = result;
        result = Arg5;
        v_stack_m108 = (uint32_t)(result);
        result = v_stack_m108;
        v_stack_m128 = (uint32_t)(Arg1);
        Arg1 = v_stack_m38;
        v_stack_m48 = result;
        v_stack_mC0 = (uint32_t)(local_rbx);
        v_stack_mB0 = (uint32_t)(local_rbx);
        v_stack_mA0 = (uint32_t)(local_rbx);
        v_stack_m11C = (uint32_t)((uint32_t)(Arg3));
        v_stack_m90 = (uint32_t)(local_rbx);
        v_stack_m80 = (uint32_t)(local_rbx);
        v_stack_m70 = (uint32_t)(local_rbx);
        v_stack_m60 = (uint32_t)(local_rbx);
        v_stack_m10C = Arg4;
        v_stack_m50 = (uint32_t)(local_rbx);
        v_stack_m40 = (uint32_t)(local_rbx);
        result = tlgCreate1Sz_wchar_t(Arg1, Arg2, Arg1, Arg4);
        Arg4 = Arg12;
        result = v_stack_m104;
        Arg2 = v_rip - 7477939;
        v_stack_m28 = result;
        Arg1 = v_rip + 6901057;
        result = v_stack_mF8;
        v_stack_m104 = Arg4;
        v_stack_m130 = result;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_m138 = 14;
        v_stack_m20 = (uint32_t)(local_rbx);
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (336);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00772884&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00772884[BB_00772884]
  bb_007728C9[BB_007728C9]
  bb_007728E7[BB_007728E7]
  bb_00772A2C[BB_00772A2C]
  bb_00772A49[BB_00772A49]
  bb_00772884 -->|branch| bb_00772A2C
  bb_00772884 -->|fallthrough| bb_007728C9
  bb_007728C9 -->|branch| bb_00772A2C
  bb_007728C9 -->|fallthrough| bb_007728E7
  bb_007728E7 -->|flow| bb_00772A2C
```
