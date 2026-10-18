# DifZwRollbackEnlistmentWrapper

- RVA: `0x006498A0`–`0x00649A04` (길이 `356` bytes)
- VA: `0x00000001406498A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `356/356` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006498CE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006498F6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00649929` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00649950` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00649969` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00649974` → [ZwRollbackEnlistment](../6B/ZwRollbackEnlistment_function_006B0290.md) (function, `0x006B0290`)
- `0x006499A1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006499C8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006499E1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00649908` → RVA `0x00F048B8` (`.data`; read)
- `0x00649916` → RVA `0x00F04980` (`.data`; read)
- `0x00649922` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006498A0  48 8B C4                        mov rax, rsp
006498A3  48 89 58 08                     mov qword ptr [rax + 8], rbx
006498A7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006498AB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006498AF  57                              push rdi
006498B0  41 56                           push r14
006498B2  41 57                           push r15
006498B4  48 83 EC 40                     sub rsp, 0x40
006498B8  0F 57 C0                        xorps xmm0, xmm0
006498BB  4C 8B F9                        mov r15, rcx
006498BE  B9 19 00 00 00                  mov ecx, 0x19
006498C3  4C 8B F2                        mov r14, rdx
006498C6  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
006498CA  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
006498CE  E8 61 C1 E4 FF                  call 0x140495a34
006498D3  48 8B F0                        mov rsi, rax
006498D6  48 85 C0                        test rax, rax
006498D9  0F 84 8F 00 00 00               je 0x14064996e
006498DF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006498E2  A8 18                           test al, 0x18
006498E4  74 0C                           je 0x1406498f2
006498E6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006498EB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006498F0  EB 0E                           jmp 0x140649900
006498F2  A8 04                           test al, 4
006498F4  74 0A                           je 0x140649900
006498F6  E8 0D A3 E8 FF                  call 0x1404d3c08
006498FB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00649900  40 32 ED                        xor bpl, bpl
00649903  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00649908  40 38 2D A9 AF 8B 00            cmp byte ptr [rip + 0x8bafa9], bpl
0064990F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00649914  75 0C                           jne 0x140649922
00649916  F7 05 60 B0 8B 00 00 08 00 00   test dword ptr [rip + 0x8bb060], 0x800
00649920  74 13                           je 0x140649935
00649922  48 8D 0D 57 A5 8B 00            lea rcx, [rip + 0x8ba557]
00649929  E8 F2 CC BC FF                  call 0x140216620
0064992E  40 8A E8                        mov bpl, al
00649931  84 C0                           test al, al
00649933  74 39                           je 0x14064996e
00649935  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00649939  48 8B 1F                        mov rbx, qword ptr [rdi]
0064993C  EB 1A                           jmp 0x140649958
0064993E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00649942  48 85 C0                        test rax, rax
00649945  74 0E                           je 0x140649955
00649947  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064994B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00649950  E8 7B 11 07 00                  call 0x1406baad0
00649955  48 8B 1B                        mov rbx, qword ptr [rbx]
00649958  48 3B DF                        cmp rbx, rdi
0064995B  75 E1                           jne 0x14064993e
0064995D  40 84 ED                        test bpl, bpl
00649960  74 0C                           je 0x14064996e
00649962  48 8D 0D 17 A5 8B 00            lea rcx, [rip + 0x8ba517]
00649969  E8 12 05 D0 FF                  call 0x140349e80
0064996E  49 8B D6                        mov rdx, r14
00649971  49 8B CF                        mov rcx, r15
00649974  E8 17 69 06 00                  call 0x1406b0290
00649979  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0064997D  48 85 F6                        test rsi, rsi
00649980  74 64                           je 0x1406499e6
00649982  40 32 FF                        xor dil, dil
00649985  40 38 3D 2C AF 8B 00            cmp byte ptr [rip + 0x8baf2c], dil
0064998C  75 0C                           jne 0x14064999a
0064998E  F7 05 E8 AF 8B 00 00 08 00 00   test dword ptr [rip + 0x8bafe8], 0x800
00649998  74 13                           je 0x1406499ad
0064999A  48 8D 0D DF A4 8B 00            lea rcx, [rip + 0x8ba4df]
006499A1  E8 7A CC BC FF                  call 0x140216620
006499A6  40 8A F8                        mov dil, al
006499A9  84 C0                           test al, al
006499AB  74 39                           je 0x1406499e6
006499AD  48 83 C6 30                     add rsi, 0x30
006499B1  48 8B 1E                        mov rbx, qword ptr [rsi]
006499B4  EB 1A                           jmp 0x1406499d0
006499B6  48 8D 43 F0                     lea rax, [rbx - 0x10]
006499BA  48 85 C0                        test rax, rax
006499BD  74 0E                           je 0x1406499cd
006499BF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006499C3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006499C8  E8 03 11 07 00                  call 0x1406baad0
006499CD  48 8B 1B                        mov rbx, qword ptr [rbx]
006499D0  48 3B DE                        cmp rbx, rsi
006499D3  75 E1                           jne 0x1406499b6
006499D5  40 84 FF                        test dil, dil
006499D8  74 0C                           je 0x1406499e6
006499DA  48 8D 0D 9F A4 8B 00            lea rcx, [rip + 0x8ba49f]
006499E1  E8 9A 04 D0 FF                  call 0x140349e80
006499E6  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
006499EA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006499EF  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
006499F4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
006499F9  48 83 C4 40                     add rsp, 0x40
006499FD  41 5F                           pop r15
006499FF  41 5E                           pop r14
00649A01  5F                              pop rdi
00649A02  C3                              ret
00649A03  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwRollbackEnlistmentWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(25, a2, a3, a4);
    if (result == 0) goto loc_0064996E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006498F2;
    v_stack_m38 = v_stack_p0;
    goto loc_00649900;
loc_006498F2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9154473)) != 0) goto loc_00649922;
    if (((*(unsigned int *)(v_rip + 9154656)) & (0x800ULL)) == 0) goto loc_00649935;
loc_00649922:
    result = ExAcquireRundownProtection(v_rip + 9151831, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064996E;
loc_00649935:
    goto loc_00649958;
loc_0064993E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00649958:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064993E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9151767;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwRollbackEnlistment(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_006499E6;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9154348)) != 0) goto loc_0064999A;
    if (((*(unsigned int *)(v_rip + 9154536)) & (0x800ULL)) == 0) goto loc_006499AD;
loc_0064999A:
    result = ExAcquireRundownProtection(v_rip + 9151711, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006499E6;
loc_006499AD:
    v_rsi = (result) + (48);
    goto loc_006499D0;
loc_006499B6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006499D0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006499B6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9151647;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwRollbackEnlistmentWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(25, Arg2, a3, a4);
    if (result == 0) goto loc_0064996E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006498F2;
    v_stack_m38 = v_stack_p0;
    goto loc_00649900;
loc_006498F2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8BAFA9)) != 0) goto loc_00649922;
    if (((*(uint32_t *)(v_rip + 0x8BB060)) & (0x800ULL)) == 0) goto loc_00649935;
loc_00649922:
    result = ExAcquireRundownProtection(v_rip + 9151831, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064996E;
loc_00649935:
    goto loc_00649958;
loc_0064993E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00649958:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064993E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9151767;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwRollbackEnlistment(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_006499E6;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BAF2C)) != 0) goto loc_0064999A;
    if (((*(uint32_t *)(v_rip + 0x8BAFE8)) & (0x800ULL)) == 0) goto loc_006499AD;
loc_0064999A:
    result = ExAcquireRundownProtection(v_rip + 9151711, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006499E6;
loc_006499AD:
    local_rsi = (result) + (48);
    goto loc_006499D0;
loc_006499B6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006499D0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006499B6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9151647;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006498A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006498A0[BB_006498A0]
  bb_006498DF[BB_006498DF]
  bb_006498E6[BB_006498E6]
  bb_006498F2[BB_006498F2]
  bb_006498F6[BB_006498F6]
  bb_00649900[BB_00649900]
  bb_00649916[BB_00649916]
  bb_00649922[BB_00649922]
  bb_00649935[BB_00649935]
  bb_0064993E[BB_0064993E]
  bb_00649947[BB_00649947]
  bb_00649955[BB_00649955]
  bb_00649958[BB_00649958]
  bb_0064995D[BB_0064995D]
  bb_00649962[BB_00649962]
  bb_0064996E[BB_0064996E]
  bb_00649982[BB_00649982]
  bb_0064998E[BB_0064998E]
  bb_0064999A[BB_0064999A]
  bb_006499AD[BB_006499AD]
  bb_006499B6[BB_006499B6]
  bb_006499BF[BB_006499BF]
  bb_006499CD[BB_006499CD]
  bb_006499D0[BB_006499D0]
  bb_006499D5[BB_006499D5]
  bb_006499DA[BB_006499DA]
  bb_006499E6[BB_006499E6]
  bb_00649A03[BB_00649A03]
  bb_006498A0 -->|branch| bb_0064996E
  bb_006498A0 -->|fallthrough| bb_006498DF
  bb_006498DF -->|branch| bb_006498F2
  bb_006498DF -->|fallthrough| bb_006498E6
  bb_006498E6 -->|branch| bb_00649900
  bb_006498F2 -->|branch| bb_00649900
  bb_006498F2 -->|fallthrough| bb_006498F6
  bb_006498F6 -->|flow| bb_00649900
  bb_00649900 -->|branch| bb_00649922
  bb_00649900 -->|fallthrough| bb_00649916
  bb_00649916 -->|branch| bb_00649935
  bb_00649916 -->|fallthrough| bb_00649922
  bb_00649922 -->|branch| bb_0064996E
  bb_00649922 -->|fallthrough| bb_00649935
  bb_00649935 -->|branch| bb_00649958
  bb_0064993E -->|branch| bb_00649955
  bb_0064993E -->|fallthrough| bb_00649947
  bb_00649947 -->|flow| bb_00649955
  bb_00649955 -->|flow| bb_00649958
  bb_00649958 -->|branch| bb_0064993E
  bb_00649958 -->|fallthrough| bb_0064995D
  bb_0064995D -->|branch| bb_0064996E
  bb_0064995D -->|fallthrough| bb_00649962
  bb_00649962 -->|flow| bb_0064996E
  bb_0064996E -->|branch| bb_006499E6
  bb_0064996E -->|fallthrough| bb_00649982
  bb_00649982 -->|branch| bb_0064999A
  bb_00649982 -->|fallthrough| bb_0064998E
  bb_0064998E -->|branch| bb_006499AD
  bb_0064998E -->|fallthrough| bb_0064999A
  bb_0064999A -->|branch| bb_006499E6
  bb_0064999A -->|fallthrough| bb_006499AD
  bb_006499AD -->|branch| bb_006499D0
  bb_006499B6 -->|branch| bb_006499CD
  bb_006499B6 -->|fallthrough| bb_006499BF
  bb_006499BF -->|flow| bb_006499CD
  bb_006499CD -->|flow| bb_006499D0
  bb_006499D0 -->|branch| bb_006499B6
  bb_006499D0 -->|fallthrough| bb_006499D5
  bb_006499D5 -->|branch| bb_006499E6
  bb_006499D5 -->|fallthrough| bb_006499DA
  bb_006499DA -->|flow| bb_006499E6
```
