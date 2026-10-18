# DifIoDetachDeviceWrapper

- RVA: `0x00629EF0`–`0x0062A040` (길이 `336` bytes)
- VA: `0x0000000140629EF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00629F18` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00629F40` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00629F6E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00629F95` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00629FAE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00629FB6` → [IoDetachDevice](../26/IoDetachDevice_function_0026FA10.md) (function, `0x0026FA10`)
- `0x00629FDF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062A006` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062A01F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00629F52` → RVA `0x00F048B8` (`.data`; read)
- `0x00629F5B` → RVA `0x00F04980` (`.data`; read)
- `0x00629F67` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00629EF0  48 8B C4                        mov rax, rsp
00629EF3  48 89 58 08                     mov qword ptr [rax + 8], rbx
00629EF7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00629EFB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00629EFF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00629F03  41 56                           push r14
00629F05  48 83 EC 30                     sub rsp, 0x30
00629F09  48 8B E9                        mov rbp, rcx
00629F0C  0F 57 C0                        xorps xmm0, xmm0
00629F0F  B9 58 01 00 00                  mov ecx, 0x158
00629F14  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00629F18  E8 17 BB E6 FF                  call 0x140495a34
00629F1D  48 8B F8                        mov rdi, rax
00629F20  48 85 C0                        test rax, rax
00629F23  0F 84 8A 00 00 00               je 0x140629fb3
00629F29  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00629F2C  A8 18                           test al, 0x18
00629F2E  74 0C                           je 0x140629f3c
00629F30  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00629F35  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00629F3A  EB 0E                           jmp 0x140629f4a
00629F3C  A8 04                           test al, 4
00629F3E  74 0A                           je 0x140629f4a
00629F40  E8 C3 9C EA FF                  call 0x1404d3c08
00629F45  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00629F4A  40 32 F6                        xor sil, sil
00629F4D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00629F52  40 38 35 5F A9 8D 00            cmp byte ptr [rip + 0x8da95f], sil
00629F59  75 0C                           jne 0x140629f67
00629F5B  F7 05 1B AA 8D 00 00 08 00 00   test dword ptr [rip + 0x8daa1b], 0x800
00629F65  74 13                           je 0x140629f7a
00629F67  48 8D 0D 12 9F 8D 00            lea rcx, [rip + 0x8d9f12]
00629F6E  E8 AD C6 BE FF                  call 0x140216620
00629F73  40 8A F0                        mov sil, al
00629F76  84 C0                           test al, al
00629F78  74 39                           je 0x140629fb3
00629F7A  4C 8D 77 20                     lea r14, [rdi + 0x20]
00629F7E  49 8B 1E                        mov rbx, qword ptr [r14]
00629F81  EB 1A                           jmp 0x140629f9d
00629F83  48 8D 43 F0                     lea rax, [rbx - 0x10]
00629F87  48 85 C0                        test rax, rax
00629F8A  74 0E                           je 0x140629f9a
00629F8C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00629F90  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00629F95  E8 36 0B 09 00                  call 0x1406baad0
00629F9A  48 8B 1B                        mov rbx, qword ptr [rbx]
00629F9D  49 3B DE                        cmp rbx, r14
00629FA0  75 E1                           jne 0x140629f83
00629FA2  40 84 F6                        test sil, sil
00629FA5  74 0C                           je 0x140629fb3
00629FA7  48 8D 0D D2 9E 8D 00            lea rcx, [rip + 0x8d9ed2]
00629FAE  E8 CD FE D1 FF                  call 0x140349e80
00629FB3  48 8B CD                        mov rcx, rbp
00629FB6  E8 55 5A C4 FF                  call 0x14026fa10
00629FBB  48 85 FF                        test rdi, rdi
00629FBE  74 64                           je 0x14062a024
00629FC0  40 32 F6                        xor sil, sil
00629FC3  40 38 35 EE A8 8D 00            cmp byte ptr [rip + 0x8da8ee], sil
00629FCA  75 0C                           jne 0x140629fd8
00629FCC  F7 05 AA A9 8D 00 00 08 00 00   test dword ptr [rip + 0x8da9aa], 0x800
00629FD6  74 13                           je 0x140629feb
00629FD8  48 8D 0D A1 9E 8D 00            lea rcx, [rip + 0x8d9ea1]
00629FDF  E8 3C C6 BE FF                  call 0x140216620
00629FE4  40 8A F0                        mov sil, al
00629FE7  84 C0                           test al, al
00629FE9  74 39                           je 0x14062a024
00629FEB  48 83 C7 30                     add rdi, 0x30
00629FEF  48 8B 1F                        mov rbx, qword ptr [rdi]
00629FF2  EB 1A                           jmp 0x14062a00e
00629FF4  48 8D 43 F0                     lea rax, [rbx - 0x10]
00629FF8  48 85 C0                        test rax, rax
00629FFB  74 0E                           je 0x14062a00b
00629FFD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062A001  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062A006  E8 C5 0A 09 00                  call 0x1406baad0
0062A00B  48 8B 1B                        mov rbx, qword ptr [rbx]
0062A00E  48 3B DF                        cmp rbx, rdi
0062A011  75 E1                           jne 0x140629ff4
0062A013  40 84 F6                        test sil, sil
0062A016  74 0C                           je 0x14062a024
0062A018  48 8D 0D 61 9E 8D 00            lea rcx, [rip + 0x8d9e61]
0062A01F  E8 5C FE D1 FF                  call 0x140349e80
0062A024  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0062A029  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0062A02E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0062A033  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0062A038  48 83 C4 30                     add rsp, 0x30
0062A03C  41 5E                           pop r14
0062A03E  C3                              ret
0062A03F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoDetachDeviceWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(344, a2, a3, a4);
    if (result == 0) goto loc_00629FB3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00629F3C;
    v_stack_m18 = v_stack_p0;
    goto loc_00629F4A;
loc_00629F3C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9283935)) != 0) goto loc_00629F67;
    if (((*(unsigned int *)(v_rip + 9284123)) & (0x800ULL)) == 0) goto loc_00629F7A;
loc_00629F67:
    result = ExAcquireRundownProtection(v_rip + 9281298, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00629FB3;
loc_00629F7A:
    goto loc_00629F9D;
loc_00629F83:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00629F9D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00629F83;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9281234;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoDetachDevice(a1, a2, a3, a4);
    if (result == 0) goto loc_0062A024;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9283822)) != 0) goto loc_00629FD8;
    if (((*(unsigned int *)(v_rip + 9284010)) & (0x800ULL)) == 0) goto loc_00629FEB;
loc_00629FD8:
    result = ExAcquireRundownProtection(v_rip + 9281185, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062A024;
loc_00629FEB:
    v_rdi = (result) + (48);
    goto loc_0062A00E;
loc_00629FF4:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062A00E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_00629FF4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9281121;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoDetachDeviceWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(344, a2, a3, a4);
    if (result == 0) goto loc_00629FB3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00629F3C;
    v_stack_m18 = v_stack_p0;
    goto loc_00629F4A;
loc_00629F3C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8DA95F)) != 0) goto loc_00629F67;
    if (((*(uint32_t *)(v_rip + 0x8DAA1B)) & (0x800ULL)) == 0) goto loc_00629F7A;
loc_00629F67:
    result = ExAcquireRundownProtection(v_rip + 9281298, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00629FB3;
loc_00629F7A:
    goto loc_00629F9D;
loc_00629F83:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00629F9D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00629F83;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9281234;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = IoDetachDevice(Arg1, a2, a3, a4);
    if (result == 0) goto loc_0062A024;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DA8EE)) != 0) goto loc_00629FD8;
    if (((*(uint32_t *)(v_rip + 0x8DA9AA)) & (0x800ULL)) == 0) goto loc_00629FEB;
loc_00629FD8:
    result = ExAcquireRundownProtection(v_rip + 9281185, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062A024;
loc_00629FEB:
    local_rdi = (result) + (48);
    goto loc_0062A00E;
loc_00629FF4:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062A00E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_00629FF4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9281121;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00629EF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00629EF0[BB_00629EF0]
  bb_00629F29[BB_00629F29]
  bb_00629F30[BB_00629F30]
  bb_00629F3C[BB_00629F3C]
  bb_00629F40[BB_00629F40]
  bb_00629F4A[BB_00629F4A]
  bb_00629F5B[BB_00629F5B]
  bb_00629F67[BB_00629F67]
  bb_00629F7A[BB_00629F7A]
  bb_00629F83[BB_00629F83]
  bb_00629F8C[BB_00629F8C]
  bb_00629F9A[BB_00629F9A]
  bb_00629F9D[BB_00629F9D]
  bb_00629FA2[BB_00629FA2]
  bb_00629FA7[BB_00629FA7]
  bb_00629FB3[BB_00629FB3]
  bb_00629FC0[BB_00629FC0]
  bb_00629FCC[BB_00629FCC]
  bb_00629FD8[BB_00629FD8]
  bb_00629FEB[BB_00629FEB]
  bb_00629FF4[BB_00629FF4]
  bb_00629FFD[BB_00629FFD]
  bb_0062A00B[BB_0062A00B]
  bb_0062A00E[BB_0062A00E]
  bb_0062A013[BB_0062A013]
  bb_0062A018[BB_0062A018]
  bb_0062A024[BB_0062A024]
  bb_0062A03F[BB_0062A03F]
  bb_00629EF0 -->|branch| bb_00629FB3
  bb_00629EF0 -->|fallthrough| bb_00629F29
  bb_00629F29 -->|branch| bb_00629F3C
  bb_00629F29 -->|fallthrough| bb_00629F30
  bb_00629F30 -->|branch| bb_00629F4A
  bb_00629F3C -->|branch| bb_00629F4A
  bb_00629F3C -->|fallthrough| bb_00629F40
  bb_00629F40 -->|flow| bb_00629F4A
  bb_00629F4A -->|branch| bb_00629F67
  bb_00629F4A -->|fallthrough| bb_00629F5B
  bb_00629F5B -->|branch| bb_00629F7A
  bb_00629F5B -->|fallthrough| bb_00629F67
  bb_00629F67 -->|branch| bb_00629FB3
  bb_00629F67 -->|fallthrough| bb_00629F7A
  bb_00629F7A -->|branch| bb_00629F9D
  bb_00629F83 -->|branch| bb_00629F9A
  bb_00629F83 -->|fallthrough| bb_00629F8C
  bb_00629F8C -->|flow| bb_00629F9A
  bb_00629F9A -->|flow| bb_00629F9D
  bb_00629F9D -->|branch| bb_00629F83
  bb_00629F9D -->|fallthrough| bb_00629FA2
  bb_00629FA2 -->|branch| bb_00629FB3
  bb_00629FA2 -->|fallthrough| bb_00629FA7
  bb_00629FA7 -->|flow| bb_00629FB3
  bb_00629FB3 -->|branch| bb_0062A024
  bb_00629FB3 -->|fallthrough| bb_00629FC0
  bb_00629FC0 -->|branch| bb_00629FD8
  bb_00629FC0 -->|fallthrough| bb_00629FCC
  bb_00629FCC -->|branch| bb_00629FEB
  bb_00629FCC -->|fallthrough| bb_00629FD8
  bb_00629FD8 -->|branch| bb_0062A024
  bb_00629FD8 -->|fallthrough| bb_00629FEB
  bb_00629FEB -->|branch| bb_0062A00E
  bb_00629FF4 -->|branch| bb_0062A00B
  bb_00629FF4 -->|fallthrough| bb_00629FFD
  bb_00629FFD -->|flow| bb_0062A00B
  bb_0062A00B -->|flow| bb_0062A00E
  bb_0062A00E -->|branch| bb_00629FF4
  bb_0062A00E -->|fallthrough| bb_0062A013
  bb_0062A013 -->|branch| bb_0062A024
  bb_0062A013 -->|fallthrough| bb_0062A018
  bb_0062A018 -->|flow| bb_0062A024
```
