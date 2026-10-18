# DifIoAllocateMdlWrapper

- RVA: `0x00627B70`–`0x00627D1F` (길이 `431` bytes)
- VA: `0x0000000140627B70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `121`개 명령, `431/431` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00627BB0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00627BD8` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00627C24` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00627C4A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00627C63` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00627C8B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00627CB8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00627CDE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00627CF7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00627BE8` → RVA `0x00F048B8` (`.data`; read)
- `0x00627C11` → RVA `0x00F04980` (`.data`; read)
- `0x00627C1D` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00627B70  48 8B C4                        mov rax, rsp
00627B73  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00627B77  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00627B7B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00627B7F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00627B83  55                              push rbp
00627B84  41 54                           push r12
00627B86  41 55                           push r13
00627B88  41 56                           push r14
00627B8A  41 57                           push r15
00627B8C  48 8B EC                        mov rbp, rsp
00627B8F  48 83 EC 70                     sub rsp, 0x70
00627B93  0F 57 C0                        xorps xmm0, xmm0
00627B96  B9 6D 01 00 00                  mov ecx, 0x16d
00627B9B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00627B9F  45 8A F9                        mov r15b, r9b
00627BA2  45 8A E0                        mov r12b, r8b
00627BA5  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00627BA9  44 8B EA                        mov r13d, edx
00627BAC  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00627BB0  E8 7F DE E6 FF                  call 0x140495a34
00627BB5  4C 8B F0                        mov r14, rax
00627BB8  48 85 C0                        test rax, rax
00627BBB  0F 84 A7 00 00 00               je 0x140627c68
00627BC1  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00627BC4  F6 C1 18                        test cl, 0x18
00627BC7  74 0A                           je 0x140627bd3
00627BC9  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00627BCD  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00627BD1  EB 0E                           jmp 0x140627be1
00627BD3  F6 C1 04                        test cl, 4
00627BD6  74 09                           je 0x140627be1
00627BD8  E8 2B C0 EA FF                  call 0x1404d3c08
00627BDD  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00627BE1  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00627BE5  40 32 F6                        xor sil, sil
00627BE8  40 38 35 C9 CC 8D 00            cmp byte ptr [rip + 0x8dccc9], sil
00627BEF  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00627BF3  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00627BF7  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00627BFB  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00627BFF  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00627C03  44 89 6D EC                     mov dword ptr [rbp - 0x14], r13d
00627C07  44 88 65 E9                     mov byte ptr [rbp - 0x17], r12b
00627C0B  44 88 7D E8                     mov byte ptr [rbp - 0x18], r15b
00627C0F  75 0C                           jne 0x140627c1d
00627C11  F7 05 65 CD 8D 00 00 08 00 00   test dword ptr [rip + 0x8dcd65], 0x800
00627C1B  74 13                           je 0x140627c30
00627C1D  48 8D 0D 5C C2 8D 00            lea rcx, [rip + 0x8dc25c]
00627C24  E8 F7 E9 BE FF                  call 0x140216620
00627C29  40 8A F0                        mov sil, al
00627C2C  84 C0                           test al, al
00627C2E  74 38                           je 0x140627c68
00627C30  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00627C34  48 8B 1F                        mov rbx, qword ptr [rdi]
00627C37  EB 19                           jmp 0x140627c52
00627C39  48 8D 43 F0                     lea rax, [rbx - 0x10]
00627C3D  48 85 C0                        test rax, rax
00627C40  74 0D                           je 0x140627c4f
00627C42  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00627C46  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00627C4A  E8 81 2E 09 00                  call 0x1406baad0
00627C4F  48 8B 1B                        mov rbx, qword ptr [rbx]
00627C52  48 3B DF                        cmp rbx, rdi
00627C55  75 E2                           jne 0x140627c39
00627C57  40 84 F6                        test sil, sil
00627C5A  74 0C                           je 0x140627c68
00627C5C  48 8D 0D 1D C2 8D 00            lea rcx, [rip + 0x8dc21d]
00627C63  E8 18 22 D2 FF                  call 0x140349e80
00627C68  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00627C6C  45 8A CF                        mov r9b, r15b
00627C6F  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00627C73  45 8A C4                        mov r8b, r12b
00627C76  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00627C7B  41 8B D5                        mov edx, r13d
00627C7E  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00627C82  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00627C87  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00627C8B  E8 40 2E 09 00                  call 0x1406baad0
00627C90  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00627C94  4D 85 F6                        test r14, r14
00627C97  74 63                           je 0x140627cfc
00627C99  40 32 FF                        xor dil, dil
00627C9C  40 38 3D 15 CC 8D 00            cmp byte ptr [rip + 0x8dcc15], dil
00627CA3  75 0C                           jne 0x140627cb1
00627CA5  F7 05 D1 CC 8D 00 00 08 00 00   test dword ptr [rip + 0x8dccd1], 0x800
00627CAF  74 13                           je 0x140627cc4
00627CB1  48 8D 0D C8 C1 8D 00            lea rcx, [rip + 0x8dc1c8]
00627CB8  E8 63 E9 BE FF                  call 0x140216620
00627CBD  40 8A F8                        mov dil, al
00627CC0  84 C0                           test al, al
00627CC2  74 38                           je 0x140627cfc
00627CC4  49 8D 76 30                     lea rsi, [r14 + 0x30]
00627CC8  48 8B 1E                        mov rbx, qword ptr [rsi]
00627CCB  EB 19                           jmp 0x140627ce6
00627CCD  48 8D 43 F0                     lea rax, [rbx - 0x10]
00627CD1  48 85 C0                        test rax, rax
00627CD4  74 0D                           je 0x140627ce3
00627CD6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00627CDA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00627CDE  E8 ED 2D 09 00                  call 0x1406baad0
00627CE3  48 8B 1B                        mov rbx, qword ptr [rbx]
00627CE6  48 3B DE                        cmp rbx, rsi
00627CE9  75 E2                           jne 0x140627ccd
00627CEB  40 84 FF                        test dil, dil
00627CEE  74 0C                           je 0x140627cfc
00627CF0  48 8D 0D 89 C1 8D 00            lea rcx, [rip + 0x8dc189]
00627CF7  E8 84 21 D2 FF                  call 0x140349e80
00627CFC  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00627D00  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00627D05  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00627D09  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00627D0D  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00627D11  49 8B E3                        mov rsp, r11
00627D14  41 5F                           pop r15
00627D16  41 5E                           pop r14
00627D18  41 5D                           pop r13
00627D1A  41 5C                           pop r12
00627D1C  5D                              pop rbp
00627D1D  C3                              ret
00627D1E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoAllocateMdlWrapper(__int64 a1, int a2, unsigned __int8 a3, unsigned __int8 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned __int8 v_stack_m3F;
    unsigned __int8 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(365, a2, a3, a4);
    if (result == 0) goto loc_00627C68;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00627BD3;
    v_stack_m58 = v_stack_p0;
    goto loc_00627BE1;
loc_00627BD3:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m48 = a5;
    v_stack_m50 = a6;
    v_stack_m3C = (unsigned int)((unsigned int)(a2));
    v_stack_m3F = a3;
    v_stack_m40 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9293001)) != 0) goto loc_00627C1D;
    if (((*(unsigned int *)(v_rip + 9293157)) & (0x800ULL)) == 0) goto loc_00627C30;
loc_00627C1D:
    result = ExAcquireRundownProtection(v_rip + 9290332, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00627C68;
loc_00627C30:
    goto loc_00627C52;
loc_00627C39:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00627C52:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00627C39;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9290269;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = a6;
    v_stack_m78 = a5;
    result = guard_dispatch_icall(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = result;
    if (result == 0) goto loc_00627CFC;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9292821)) != 0) goto loc_00627CB1;
    if (((*(unsigned int *)(v_rip + 9293009)) & (0x800ULL)) == 0) goto loc_00627CC4;
loc_00627CB1:
    result = ExAcquireRundownProtection(v_rip + 9290184, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00627CFC;
loc_00627CC4:
    goto loc_00627CE6;
loc_00627CCD:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00627CE6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00627CCD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9290121;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return v_stack_m30;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoAllocateMdlWrapper(int64_t Arg1, int32_t Arg2, uint8_t Arg3, uint8_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint8_t v_stack_m3F;
    uint8_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(365, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00627C68;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00627BD3;
    v_stack_m58 = v_stack_p0;
    goto loc_00627BE1;
loc_00627BD3:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m48 = Arg5;
    v_stack_m50 = Arg6;
    v_stack_m3C = (uint32_t)((uint32_t)(Arg2));
    v_stack_m3F = Arg3;
    v_stack_m40 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8DCCC9)) != 0) goto loc_00627C1D;
    if (((*(uint32_t *)(v_rip + 0x8DCD65)) & (0x800ULL)) == 0) goto loc_00627C30;
loc_00627C1D:
    result = ExAcquireRundownProtection(v_rip + 9290332, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00627C68;
loc_00627C30:
    goto loc_00627C52;
loc_00627C39:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00627C52:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00627C39;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9290269;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = Arg6;
    v_stack_m78 = Arg5;
    result = guard_dispatch_icall(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = result;
    if (result == 0) goto loc_00627CFC;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DCC15)) != 0) goto loc_00627CB1;
    if (((*(uint32_t *)(v_rip + 0x8DCCD1)) & (0x800ULL)) == 0) goto loc_00627CC4;
loc_00627CB1:
    result = ExAcquireRundownProtection(v_rip + 9290184, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00627CFC;
loc_00627CC4:
    goto loc_00627CE6;
loc_00627CCD:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_00627CE6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00627CCD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9290121;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return v_stack_m30;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00627B70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00627B70[BB_00627B70]
  bb_00627BC1[BB_00627BC1]
  bb_00627BC9[BB_00627BC9]
  bb_00627BD3[BB_00627BD3]
  bb_00627BD8[BB_00627BD8]
  bb_00627BE1[BB_00627BE1]
  bb_00627C11[BB_00627C11]
  bb_00627C1D[BB_00627C1D]
  bb_00627C30[BB_00627C30]
  bb_00627C39[BB_00627C39]
  bb_00627C42[BB_00627C42]
  bb_00627C4F[BB_00627C4F]
  bb_00627C52[BB_00627C52]
  bb_00627C57[BB_00627C57]
  bb_00627C5C[BB_00627C5C]
  bb_00627C68[BB_00627C68]
  bb_00627C99[BB_00627C99]
  bb_00627CA5[BB_00627CA5]
  bb_00627CB1[BB_00627CB1]
  bb_00627CC4[BB_00627CC4]
  bb_00627CCD[BB_00627CCD]
  bb_00627CD6[BB_00627CD6]
  bb_00627CE3[BB_00627CE3]
  bb_00627CE6[BB_00627CE6]
  bb_00627CEB[BB_00627CEB]
  bb_00627CF0[BB_00627CF0]
  bb_00627CFC[BB_00627CFC]
  bb_00627D1E[BB_00627D1E]
  bb_00627B70 -->|branch| bb_00627C68
  bb_00627B70 -->|fallthrough| bb_00627BC1
  bb_00627BC1 -->|branch| bb_00627BD3
  bb_00627BC1 -->|fallthrough| bb_00627BC9
  bb_00627BC9 -->|branch| bb_00627BE1
  bb_00627BD3 -->|branch| bb_00627BE1
  bb_00627BD3 -->|fallthrough| bb_00627BD8
  bb_00627BD8 -->|flow| bb_00627BE1
  bb_00627BE1 -->|branch| bb_00627C1D
  bb_00627BE1 -->|fallthrough| bb_00627C11
  bb_00627C11 -->|branch| bb_00627C30
  bb_00627C11 -->|fallthrough| bb_00627C1D
  bb_00627C1D -->|branch| bb_00627C68
  bb_00627C1D -->|fallthrough| bb_00627C30
  bb_00627C30 -->|branch| bb_00627C52
  bb_00627C39 -->|branch| bb_00627C4F
  bb_00627C39 -->|fallthrough| bb_00627C42
  bb_00627C42 -->|flow| bb_00627C4F
  bb_00627C4F -->|flow| bb_00627C52
  bb_00627C52 -->|branch| bb_00627C39
  bb_00627C52 -->|fallthrough| bb_00627C57
  bb_00627C57 -->|branch| bb_00627C68
  bb_00627C57 -->|fallthrough| bb_00627C5C
  bb_00627C5C -->|flow| bb_00627C68
  bb_00627C68 -->|branch| bb_00627CFC
  bb_00627C68 -->|fallthrough| bb_00627C99
  bb_00627C99 -->|branch| bb_00627CB1
  bb_00627C99 -->|fallthrough| bb_00627CA5
  bb_00627CA5 -->|branch| bb_00627CC4
  bb_00627CA5 -->|fallthrough| bb_00627CB1
  bb_00627CB1 -->|branch| bb_00627CFC
  bb_00627CB1 -->|fallthrough| bb_00627CC4
  bb_00627CC4 -->|branch| bb_00627CE6
  bb_00627CCD -->|branch| bb_00627CE3
  bb_00627CCD -->|fallthrough| bb_00627CD6
  bb_00627CD6 -->|flow| bb_00627CE3
  bb_00627CE3 -->|flow| bb_00627CE6
  bb_00627CE6 -->|branch| bb_00627CCD
  bb_00627CE6 -->|fallthrough| bb_00627CEB
  bb_00627CEB -->|branch| bb_00627CFC
  bb_00627CEB -->|fallthrough| bb_00627CF0
  bb_00627CF0 -->|flow| bb_00627CFC
```
